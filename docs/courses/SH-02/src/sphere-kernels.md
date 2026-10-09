# SH02-SPH — Inverse operators from complementary hemisphere boundaries

Local unit: `SH02-SPH`. Intended license: CC0-1.0. The arguments below are complete relative to the stated proper-support, orientation and kernel-composition imports. Formalization, translation and publication have not occurred.

An integral kernel can recover all of an input sheaf even when its support is much larger than a diagonal. Here the intermediate variable ranges over covector directions. A closed inequality followed by an open inequality leaves an open hemisphere above the diagonal. Away from the diagonal it leaves a closed halfspace, whose compactly supported cohomology vanishes. The boundary condition is the mechanism of inversion.

## SH02-SPH-SETUP — Directions and relative correspondences

Fix a commutative ring $k$ of finite global dimension. Let $E\to B$ be a real vector bundle of fixed rank $n$ over a locally compact Hausdorff space. There is no orientation, constructibility, field, finite-stalk or compact-base assumption. Put

\[
S=S(E)=(E\setminus0)/\mathbb R_{>0},\qquad
S^\vee=S(E^*)=(E^*\setminus0)/\mathbb R_{>0}.
\]

These are spaces of positive rays; opposite rays are distinct. Local bundle trivializations identify each projection with $U\times S^{n-1}\to U$ when $n>0$. Thus the projections are proper topological submersions of relative dimension $n-1$. This construction uses no globally chosen metric. A local metric can identify positive rays with unit vectors, and the resulting ray space is independent of that choice.

We use relative products over $B$. Write $p:S\times_B S^\vee\to S$ and $q:S\times_B S^\vee\to S^\vee$. Define two incidence sets, with the order of the variables indicated:

\[
D=\{(u,\xi):\xi(u)\geq0\}\subset S\times_B S^\vee,
\qquad
J=\{(\xi,u):\xi(u)>0\}\subset S^\vee\times_B S.
\tag{SPH1}
\]

Evaluation has a well-defined sign on rays because changing either representative multiplies it by a positive number. The sets $D$ and $J$ are respectively closed and open in their relative products. As elsewhere, $k_D$ and $k_J$ mean restriction of constant coefficients followed by extension by zero. They do not denote local-cohomology functors.

Let $O_E$ be the orientation local system of $E$ on $B$. There is a positive dual-orientation identification $O_E\simeq O_{E^*}$ and a canonical pairing $O_E\otimes O_{E^*}\simeq k_B$. Let

\[
\omega_{S^\vee/B}=\operatorname{or}_{S^\vee/B}[n-1].
\]

The first kernel includes this complex pulled back from its second factor:

\[
K=k_D\otimes q^{-1}\omega_{S^\vee/B},
\qquad L=k_J.
\tag{SPH2}
\]

The tensor products are derived. The cutoff sheaves are flat: each stalk is either $k$ or zero. Orientation sheaves are locally free of rank one.

For relative kernels $A$ on $P\times_B Q$ and $C$ on $Q\times_B R$, define

\[
A\circ C=Rr_{13!}(r_{12}^{-1}A\otimes r_{23}^{-1}C).
\tag{SPH3}
\]

The projections in this unit have finite-dimensional sphere or Euclidean fibres. Proper-support base change and the fibre dimension bound give the required finite cohomological dimensions. Consequently these convolution operations and their exceptional adjoints are available on $D^+$ and preserve $D^b$ in the instances below. This relative formulation requires no finite c-soft dimension of the base. When the absolute product kernel formalism of SH02-KER is used, its ambient finite c-soft dimension assumptions are retained; extending the relative kernels by the closed embeddings into the absolute products gives the same ordinary integral operators.

The proof uses the actual composition and adjunction comparisons of SH02-KER-006 and SH02-KER-008. Their relative versions follow from the same Cartesian projection squares and the same tensor/Hom adjunctions. It also uses proper-support base change and the oriented-submersion trace: for an oriented $d$-dimensional Euclidean fibre, integration identifies $R\Gamma_c(\mathbb R^d;k[d])$ with $k$. The manifold-duality unit must supply that trace and its orientation and base-change compatibilities. These are explicit imports, not consequences of stalk calculations alone.

## SH02-SPH-HALFSPACE — Why a closed boundary kills compact cohomology

For a $k$-module $M$ and $d\geq1$,

\[
R\Gamma_c([0,\infty)\times\mathbb R^{d-1};M)=0.
\tag{SPH4}
\]

Here the coefficient sheaf is constant on the displayed space. To prove the statement, compactify each coordinate. The space becomes

\[
W=[0,1)\times(-1,1)^{d-1}\subset Q=[0,1]\times[-1,1]^{d-1}.
\]

Its closed complement is

\[
A=(\{1\}\times[-1,1]^{d-1})
\cup([0,1]\times\partial[-1,1]^{d-1}).
\]

For $d=1$, this means $A=\{1\}$. The homotopy $(s,y)\mapsto((1-t)s+t,y)$ preserves $A$ and retracts it onto its right face. That face and $Q$ are nonempty compact convex sets, so their constant-coefficient cohomology is $M$ in degree zero by SH02-OR-CONVEX-COMPACT.

For clarity, the homotopy assertion used here has a sheaf proof. If $T$ is compact Hausdorff, the projection $T\times[0,1]\to T$ is proper. Proper base change and interval acyclicity make the constant-coefficient pullback unit an isomorphism. Each endpoint restriction is its inverse. Thus homotopic maps induce the same map on constant-coefficient cohomology. Applying this to the displayed retraction gives $R\Gamma(A;M_A)\simeq M$. The restriction from $Q$ to $A$ is the identity on constant sections and therefore is an isomorphism on all cohomology groups.

The exact sequence for an open subset and its closed complement gives the triangle

\[
R\Gamma(Q;j_!M_W)\longrightarrow R\Gamma(Q;M_Q)
\longrightarrow R\Gamma(A;M_A)\xrightarrow{+1}.
\]

The last nonshifted arrow is an isomorphism. Since $Q$ is compact, the first term is $R\Gamma_c(W;M_W)$. This proves (SPH4). It holds for arbitrary modules, including torsion and infinitely generated modules. For a bounded-below constant coefficient complex, the compact-support hypercohomology spectral sequence gives the same vanishing; boundedness below ensures convergence in each total degree.

By contrast, an open halfspace in $\mathbb R^d$ is homeomorphic to $\mathbb R^d$ and has compact cohomology $M[-d]$ after an orientation is chosen. It cannot be substituted into (SPH4).

## SH02-SPH-FIRST — Eliminating the covector direction

There is an isomorphism of kernels on $S\times_B S$,

\[
K\circ L\simeq k_{\Delta_S}.
\tag{SPH5}
\]

The isomorphism will be obtained from a restriction to the diagonal followed by the oriented trace.

On $S\times_B S^\vee\times_B S$ the support of the convolution integrand is

\[
T=\{(u,\xi,v):\xi(u)\geq0,\ \xi(v)>0\}.
\]

Fix $(u,v)$ in a fibre over $b$. Choose a nonzero representative of $v$. Each positive covector ray satisfying $\xi(v)>0$ has a unique representative satisfying $\xi(v)=1$. The remaining variables form an affine space of dimension $n-1$. In this affine space the other condition is $\xi(u)\geq0$.

There are exactly three cases. If $u=v$ as positive rays, the condition holds throughout the affine space. If $u=-v$, it holds nowhere. Otherwise $u$ and $v$ are linearly independent, the affine function $\xi\mapsto\xi(u)$ is nonconstant, and the condition cuts out a closed affine halfspace. In the last case necessarily $n\geq2$.

Proper-support base change identifies the convolution stalk with compact cohomology of this fibre with coefficients in the restricted orientation complex. On a hemisphere the orientation sheaf is locally constant on an affine space and is therefore constant; its shift is $[n-1]$. The empty and closed-halfspace cases have zero compact cohomology by (SPH4). Thus every cohomology sheaf of $K\circ L$ vanishes away from $\Delta_S$.

Let $i:\Delta_S\hookrightarrow S\times_B S$. The unit

\[
K\circ L\longrightarrow i_*i^{-1}(K\circ L)
\tag{SPH6}
\]

is an isomorphism: it is the identity on stalks on the diagonal, and both sides vanish elsewhere. This step identifies the sheaf object, rather than inferring an object from a list of stalk groups.

Base change identifies the restriction on the right with the compact direct image along

\[
h:\{(u,\xi):\xi(u)>0\}\longrightarrow S.
\]

Locally on $S$, choose a continuously varying representative of $u$ and a covector evaluating to one on it. The remaining covectors form a vector space of dimension $n-1$. Hence $h$ is locally a Euclidean-space bundle. Its relative dualizing complex is the restriction of $q^{-1}\omega_{S^\vee/B}$, because it is an open subspace of the product of the two ray spheres over $B$. The counit

\[
Rh_!h^!k_S\longrightarrow k_S
\tag{SPH7}
\]

is an isomorphism by the Euclidean-fibre integration trace. Compose (SPH6), base change, and (SPH7) to obtain (SPH5). No global orientation or basis was chosen, and the orientation transitions in the integrand are precisely the transitions in the trace.

## SH02-SPH-SECOND — Eliminating the vector direction

The other convolution satisfies

\[
L\circ K\simeq k_{\Delta_{S^\vee}}.
\tag{SPH8}
\]

Its support above a pair $(\xi,\eta)$ consists of rays $u$ satisfying $\xi(u)>0$ and $\eta(u)\geq0$. Normalize by $\xi(u)=1$. The same affine calculation gives all of $\mathbb R^{n-1}$ when $\eta=\xi$, the empty set when $\eta=-\xi$, and a closed halfspace otherwise. Therefore the convolution again vanishes off its diagonal, and its canonical restriction unit identifies it with the pushforward of its diagonal restriction.

There is an extra orientation issue: the complex in $K$ comes from the endpoint $\eta$, whereas the integration variable is now $u$. We make the cancellation explicit. For a positive vector ray $u$, place its positive radial direction first in an oriented basis of $E_b$. This gives

\[
\operatorname{or}_{S/B}|_u\simeq O_{E,b}.
\]

There is the corresponding convention for covector rays. On the incidence space $\xi(u)>0$, choose a representative with $\xi(u)=1$. Then

\[
E_b=\mathbb Ru\oplus\ker\xi,
\qquad
E_b^*=\mathbb R\xi\oplus\operatorname{ann}(u).
\]

The last two summands are perfectly paired, and the first two one-dimensional summands pair positively. A basis of $\ker\xi$ and its dual basis in $\operatorname{ann}(u)$ therefore induce the positive dual-orientation identification. Replacing such a basis multiplies both orientation generators by the same sign. Scaling $u$ or $\xi$ positively changes no orientation. These identifications hence glue over the whole incidence space.

In particular, on the incidence space above the diagonal $\eta=\xi$, the pulled-back endpoint complex $\omega_{S^\vee/B}$ is canonically the relative dualizing complex for projection onto $\xi$. Its degree is $n-1$, and its orientation local system agrees with that of the integrated hemisphere. Integration therefore gives

\[
R\widetilde h_!\bigl(\widetilde h^{-1}\omega_{S^\vee/B}
\big|_{\{\xi(u)>0\}}\bigr)\simeq k_{S^\vee},
\]

where the notation inside the pushforward means the endpoint orientation complex on the incidence space. More explicitly, locally this is $O_E[-(n-1)]\otimes O_{E^*}[n-1]\simeq k$. This cancellation is transported from the integration counit, with the tensor-shift signs included; it is not an independently chosen degree-zero multiplication. The positive dual pairing fixes its orientation convention, and the two shifts cancel. The restriction-to-diagonal construction followed by this trace proves (SPH8). It introduces neither an antipodal map nor a residual shift.

## SH02-SPH-EQUIVALENCE — The induced inverse operators

For $F\in D^+(S^\vee;k)$ and $G\in D^+(S;k)$, put

\[
\Phi_K(F)=Rp_!(K\otimes q^{-1}F),
\qquad
\Phi_L(G)=R\widetilde p_!(L\otimes\widetilde q^{-1}G),
\]

where $\widetilde p:S^\vee\times_B S\to S^\vee$ and $\widetilde q:S^\vee\times_B S\to S$. The kernel-composition comparison and the diagonal kernel unit give

\[
\Phi_K\Phi_L\simeq1_{D^+(S;k)},\qquad
\Phi_L\Phi_K\simeq1_{D^+(S^\vee;k)}.
\tag{SPH9}
\]

These are equivalences on all sheaves in the indicated bounded-below categories, and restrict to bounded categories. The projections have fibres of uniformly bounded finite dimension, the kernel shifts are fixed, and the coefficient ring has finite global dimension; these facts supply the bounds for the displayed operations.

Each operator has the actual kernel right adjoint, for example

\[
\Psi_K(G)=Rq_*R\mathcal Hom(K,p^!G).
\]

The unit and counit of $\Phi_K\dashv\Psi_K$ are isomorphisms because $\Phi_K$ is an equivalence. Here is the categorical reason without assuming a chosen inverse is automatically the given adjoint. Fully faithfulness makes the adjunction unit an isomorphism; essential surjectivity and the triangle identity then make the counit an isomorphism. Thus $\Psi_K$ is an inverse equivalence and is isomorphic to $\Phi_L$ as the inverse right adjoint. The corresponding assertion holds for $\Psi_L$. This proves equivalence of all four operators. It does not identify arbitrary, separately normalized natural transformations merely from their invertibility.

When $n=0$, both ray spaces are empty, and all their sheaf categories are the zero category. The kernels and diagonals are zero; the assertions are the unique equivalences of zero categories. This case requires no expression with a sphere of dimension minus one. For $n=1$, the ray fibres have two points, there is no halfspace case, and all traces have degree zero.

<a id="SH02-SPH-BOUNDARY-ADJOINT"></a>

## How the boundary determines the actual adjoint

Put \(X=S\times_BS^\vee\), \(U=\{(u,\xi):\xi(u)>0\}\) in this order, and \(W=q^{-1}\omega_{S^\vee/B}\). Thus \(D=\overline U\), and transposing \(U\) gives the support \(J\) of \(L\). For every \(G\in D^+(S;k)\), write \(H=p^{-1}G\). The two canonical boundary comparisons are

\[
\begin{gathered}
H_U\xrightarrow{\sim}R\mathcal Hom(k_D,H),\\
H_D\xrightarrow{\sim}R\mathcal Hom(k_U,H).
\end{gathered}
\tag{SPH10}
\]

These comparisons concern a coefficient complex pulled back from the first sphere. They do not assert either identity for an arbitrary complex on \(X\).

Here is a local proof that retains arbitrary coefficient modules and the bounded-below range. At a boundary point, \(\xi(u)=0\) with \(u,\xi\ne0\). Varying the covector in a direction that is nonzero on \(u\) makes evaluation a transverse real coordinate. Local bundle charts therefore identify the incidence boundary, relative to \(p\), with \(t=0\) in \(Y\times\mathbb R\), with the other covector coordinates included in \(Y\). The coefficient complex has the form \(r^{-1}A\), where \(r:Y\times\mathbb R\to Y\) and \(A\in D^+(Y;k)\). Only local intervals are needed, and an interval can be reparametrized by the real line. In rank one the incidence boundary is empty; in rank zero the entire ray space is empty.

Write \(C=\{t\ge0\}\), \(V=\{t>0\}\), \(Z=\{t=0\}\) and \(H_0=r^{-1}A\). The normal halfline complex \((H_0)_C\) is conic for positive scaling in \(t\). The [proper-support contraction](../../sheaf-proof-readings/SH02-conic-descent.html#SH02-CON-RADIAL-SUPPORT), followed by the projection formula and the halfline case of SPH4, gives

\[
\begin{gathered}
i_Z^!(H_0)_C\xrightarrow{\sim}Rr_!((H_0)_C)\\
\simeq A\otimes^LR\Gamma_c([0,\infty);k)\\
=0.
\end{gathered}
\tag{SPH11}
\]

Here \(i_Z:Y\to Y\times\mathbb R\) is the zero section. The contraction has no additional shift, and its proof uses the stated proper-support and continuity contracts. The tensor factor on the right vanishes before any coefficient finiteness condition could enter. Applying the open-complement localization triangle to \((H_0)_C\) consequently makes its restriction unit an isomorphism onto \(Rj_{V*}j_V^{-1}H_0=R\Gamma_VH_0\). This proves the second map in SPH10 in the local chart.

For the first map use the localization triangle for \(C\) and its open complement \(\{t<0\}\). The [cylinder unit](../../sheaf-proof-readings/SH02-conic-descent.html#SH02-CON-CYLINDER) identifies sections of \(r^{-1}A\) on every product of a base neighbourhood and a negative interval with the corresponding sections of \(A\). These units are compatible with restriction of both neighbourhoods and intervals. At \(t=0\) the map from \(H_0\) to the ordinary direct image from \(t<0\) is therefore the identity on \(A\). The stalk of \(R\Gamma_CH_0\) at that boundary is zero. In the positive interior it is \(H_0\), and in the negative interior it is zero. The canonical map \((H_0)_V\to R\Gamma_CH_0\) is induced by applying \(R\Gamma_C\) to \((H_0)_V\to H_0\); its source is already supported in \(C\). It is an isomorphism on every stalk, which proves the first map. This constructs the comparison, rather than inferring it from unchosen stalk identifications. Both local proofs use natural restriction or support maps, so they glue to SPH10. The cylinder argument retains its explicit closed-exhaustion and interval hypotheses; they are not replaced by an unconditional inverse-limit rule.

Now apply the actual kernel-adjunction formula already used above. Smooth relative purity gives \(p^!G\simeq p^{-1}G\otimes W\). Tensoring both internal-Hom arguments by the same invertible complex cancels that complex by its specified tensor equivalence, so

\[
\begin{gathered}
\Psi_K(G)\\
=Rq_*R\mathcal Hom(\\
k_D\otimes W,p^{-1}G\otimes W)\\
\simeq Rq_*R\mathcal Hom(k_D,p^{-1}G)\\
\simeq Rq_*((p^{-1}G)_U)\\
\simeq Rq_!((p^{-1}G)_U)=\Phi_L(G).
\end{gathered}
\tag{SPH12}
\]

The last comparison uses properness of \(q\), whose fibre is the compact vector-ray sphere; it does not require a compact base. Transposition identifies the last expression with the previously defined \(\Phi_L\). This gives a geometric natural identification of the actual right adjoint, with no coefficient dualization, antipode or remaining shift. Together with SPH5 and SPH8, it makes the unit and counit of the transported adjunction \(\Phi_K\dashv\Phi_L\) isomorphisms. It still does not identify an independently normalized natural transformation with those adjunction maps solely from invertibility.

## SH02-SPH-EXAMPLES — Boundary and orientation tests

**An open-open replacement is not inverse.** Take $B$ a point and $E=\mathbb R^2$. Replace the closed condition in $D$ by a strict one. At the distinct vector rays $u=(1,0)$ and $v=(0,1)$, normalization gives $\xi=(a,1)$ with $a>0$. This is an open line interval and has compact cohomology $k[-1]$. The orientation shift in $K$ is $[1]$, so the resulting convolution stalk is $k$ in degree zero. It is nonzero away from the diagonal when $k\ne0$. The change of one boundary inequality destroys (SPH5).

**A line with orientation monodromy.** Let $E$ be the Möbius real line bundle on a circle. Its ray bundle is the connected double cover of that circle. A positive vector ray determines the positive dual covector ray by the condition $\xi(u)>0$, giving a canonical isomorphism $S(E)\simeq S(E^*)$. In rank one, the closed and open conditions in (SPH1) coincide, since a nonzero covector never vanishes on a nonzero vector. Both incidence kernels are graphs of this isomorphism. The relative ray-space orientation is canonically trivial in dimension zero. Hence the two operators are transport along mutually inverse graph maps. No choice of orientation of the Möbius bundle is involved.

## SH02-SPH-EXERCISES — Calculations with solutions

1. For $n=3$, fix independent representatives $u,v$. Describe the off-diagonal fibre and explain why its orientation shift cannot rescue a nonzero compact cohomology class.

   *Solution.* Choose coordinates with $v=e_3$ and $u=e_1$. A covector normalized by $\xi(v)=1$ has coordinates $(a,b,1)$. The condition $\xi(u)\geq0$ is $a\geq0$, so the fibre is $[0,\infty)\times\mathbb R$. Its constant-coefficient compact cohomology is zero by (SPH4). Tensoring by a rank-one orientation line and shifting by two leaves the zero object zero. The vanishing depends on retaining the boundary $a=0$.

2. Explain why proving only that all diagonal stalks are isomorphic to $k$ would not finish the convolution calculation.

   *Solution.* A locally constant sheaf can have stalk $k$ everywhere while carrying nontrivial monodromy. Stalk dimensions also do not specify a preferred map. The restriction unit (SPH6) first places the convolution on the diagonal as a sheaf object. The globally defined, orientation-compatible integration trace then identifies that object with the constant diagonal sheaf. These maps eliminate the possible local-system ambiguity.

3. Replace $K$ by $K[r]$ and $L$ by $L[-r]$ for an integer $r$. Determine both convolutions and the corresponding change of operators.

   *Solution.* Derived tensor and direct image commute with shifts, so each convolution receives total shift $r-r=0$. They remain the diagonal kernels with the isomorphisms induced from (SPH5) and (SPH8). The operators become $\Phi_K[r]$ and $\Phi_L[-r]$, which are still inverse. This calculation concerns complementary shifts of actual kernels; it does not assert that an arbitrary object with the same stalks defines the same kernel.

## SH02-SPH-BOUNDARY — Antecedents and remaining verification

The ray–sphere kernel construction comes from the Fourier–Sato theory of M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), §2.1. The lesson is organized around the separate closed-halfspace calculation, the two diagonal restriction maps and their differently placed orientation factors.

The exact foundations needed are proper-support base change and composition, the compact constant-coefficient calculations in SH02-CA, the relative orientation trace with positive dual orientation in SH02-MD-TRACE and SH02-MD-SPHERE, and the actual kernel-composition/adjunction comparisons in SH02-KER. No source image, exercise or proof paragraph is copied into this lesson.
