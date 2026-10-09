# SH02-IHM-UNIT — An isolated holomorphic test and its Morse filtration

This supplement supplies the field-valued controlled Morse step used in `SH02-FH-MORSE-FILTRATION`. Its geometric imports are stated precisely below. The constructions after those imports prove the direction of the filtration maps, the degree shift and the integer nonvanishing statement. The imported geometric results themselves are not proved here.

Let $K$ be any field. Work in a complex manifold $Y$, near a point $y$, with a locally finite complex analytic Whitney stratification adapted to a bounded complex-constructible $K$-complex $A$. Shrink around $y$ until only finitely many strata are relevant. Suppose a holomorphic germ $g:(Y,y)\to(\mathbb C,0)$ has no stratified critical point in this neighborhood other than $y$. The stratum through $y$ need not be a point stratum. Put

$$
M_g(A)_y=(R\Gamma_{\{\operatorname{Re}g\geq0\}}A)_y.
\tag{IHM1}
$$

<a id="SH02-IHM-FULL-ISOLATED-PROOF"></a>

The independently authored [original-pair proof IH0–IH9](../isolated-holomorphic-pair-and-cluster.html#IH0) supplies the relative comparison below on the original ball and fibre for bounded weakly constructible abelian complexes and its actual arbitrary-ring coefficient comparison. The [whole-cluster proof IH10–IH22](../isolated-holomorphic-pair-and-cluster.html#IH10) supplies the controlled perturbation, actual continuation maps, reverse exit filtration, ordered orientation and every-field integer count. The [finite analytic/Samuel bridge IHA1–IHA3](../isolated-holomorphic-pair-and-cluster.html#IHA1) includes non-Cohen–Macaulay conormals. Its [exact retained floor](../isolated-holomorphic-pair-and-cluster.html#IH-PROVIDERS) keeps the broader singular-form and nonisolated alternatives distinct. The following antecedents and original formulas are retained as the original theorem route.

## SH02-IHM-IMPORTS — The exact geometric results used

Massey's isolated stratified theorem, Theorem 1.1 in *A Little Microlocal Morse Theory*, version 2, pp. 3–4, supplies a small Milnor pair, a generic linear perturbation with finitely many stratified Morse points, and their counts as conormal intersection multiplicities. The discussion following that theorem separates critical values and identifies the cluster pair under perturbation. Lemmas 5.1–5.2, pp. 15–16, supply the explicit boundary exclusion needed for the radial Morse function. Every field satisfies the coefficient assumptions used here. We use the stratified-isolated case, rather than the paper's stronger theorem about isolated vanishing-cycle support. [Massey, version 2](https://arxiv.org/abs/math/0006185v2)

Maxim–Schürmann, Corollary 4.14, equation (94), pp. 65–66, identifies IHM1 with the relative Milnor-pair complex. Corollary 3.7, Lemma 3.8 and Theorem 3.12, pp. 26–28, give the change at one critical level and its normal Morse factor. These are derived statements for weakly constructible complexes. [Constructible sheaf complexes, June 2, 2021](https://people.math.wisc.edu/~lmaxim/handbook.pdf)

These references specify mathematical inputs. They do not grant a right to redistribute their source text, and the results on which they depend are not proved here. In particular the existence of the stratification, the isotopy and controlled-boundary results, and the analytic intersection theory retain their separate dependency identities.

<a id="SH02-IHM-CHARACTERISTIC-VALUES"></a>

The [characteristic-value theorem](../characteristic-values-from-analytic-cells.html#CV0) supplies the geometric discreteness statement for radial value avoidance when the cotangent set is closed, conic, subanalytic and isotropic, and the radius is proper on its base support. Its [singular-incidence argument](../characteristic-values-from-analytic-cells.html#CV2) includes zero covectors and retains the exact properness hypothesis.

## SH02-IHM-BOUNDARY — From a local test to one compact cluster

Here is why the boundary argument applies. Away from $y$, the differential of $g$ is nonzero on every stratum. A supported test in this differential direction therefore vanishes by the constructible conormal estimate. The local comparison in equation (94) identifies this same test with the shifted vanishing-cycle stalk, so those stalks vanish away from $y$. Thus their support is either empty or isolated at $y$. When it contains $y$, this verifies the literal hypothesis of Massey's Lemma 5.2. No theorem identifying the full nonisolated critical support is used in this verification.

The same boundary conclusion also holds in the empty-support case. This follows from the proof of that lemma, not from extending its printed hypothesis without explanation. Its use of isolated support is to obtain the punctured exclusion of $dg$ from the microsupport. Here that exclusion already follows from stratified regularity, including in the empty case. The rest of the proof first chooses a radial covector outside the microlocal sum of the microsupport and the conormal to $g^{-1}(0)$, using its stated microlocal Bertini–Sard input. On the compact boundary over $g=0$, these exclusions keep the radial covector, the real and imaginary differentials of $g$, and every unit microsupport covector independent. This condition is open. Compactness of the unit covectors over that boundary makes it uniform under a small perturbation. The closed-ball microsupport estimate then gives the same exclusion for the ball-restricted complex. None of these steps uses a nonzero stalk at $y$. If the microsupport itself is empty, the assertion is immediate. Thus boundary control and the filtration below apply in both cases, rather than only giving a zero-test shortcut.

Choose a sufficiently small closed ball $C$ and a small nonzero regular value $v$ of $g$. The imported local comparison and stabilization identify the relative complex of $C$ and its Milnor fibre with IHM1. Perturb $g$ to $g_t=g+tL$, with $L$ generic. The imported controlled continuation identifies the relative complex containing the entire cluster with the unperturbed one. It does not identify the original test with the perturbed stalk at $y$.

For the radial function

$$
h=|g_t-v|^2,
\tag{IHM2}
$$

the small level at the bottom retracts, with its constructible sheaf data, onto the Milnor fibre. Choose a regular top value $b_N$ above the cluster in the permitted Milnor range, and set $B=C\cap\{h\leq b_N\}$. The controlled comparison gives a quasi-isomorphism from the cohomology of $C$ to that of $B$ by restriction; $B$ is not asserted to equal $C$. The bottom-level comparison and this top restriction identify the relative complex with the original local test. The boundary exclusion says that the intervening boundary strata contribute zero local tests. On the interior, $h$ can change the relative complex only at the finitely many Morse points of $g_t$.

One can arrange distinct positive critical levels of $h$. First choose the perturbation with distinct complex critical values $c_1,\ldots,c_N$. Then choose $v$ outside those points and outside the finitely many real perpendicular bisectors defined by $|c_i-v|=|c_j-v|$. This is possible in any sufficiently small open disk of permitted regular values. The imported boundary control is uniform for the sufficiently small choices. The resulting radii $|c_i-v|^2$ are positive and pairwise different.

## SH02-IHM-FILTRATION — Choosing the maps in the right direction

Let

$$
B_0\subset B_1\subset\cdots\subset B_N=B
\tag{IHM3}
$$

be the sets $B_j=C\cap\{h\leq b_j\}$ for regular values, beginning below every positive critical value and crossing one point at each step. Here $B_N=B$ is the final regular sublevel, while $C$ remains the original closed ball. Boundary terms vanish as above. Write

$$
R\Gamma(C,D;A)
=\operatorname{Fib}\bigl(R\Gamma(C;A)\longrightarrow R\Gamma(D;A)\bigr)
\tag{IHM4}
$$

for relative cohomology with its restriction map. The single-level triangle identifies

$$
Q_j=R\Gamma(B_j,B_{j-1};A)
\tag{IHM5}
$$

with the supported Morse test at the unique interior point of that interval. The initial regular interval can be inserted or removed without changing the relative complex.

The complexes $R\Gamma(B_j,B_0;A)$ have restriction maps in decreasing $j$. To obtain the increasing filtration used in FH55, keep the final space fixed and remove levels from the relative subspace. Define

$$
F_r=R\Gamma(B,B_{N-r};A),\qquad 0\leq r\leq N.
\tag{IHM6}
$$

Then $F_0=0$ and $F_N\simeq M_g(A)_y$. The composable restriction maps

$$
R\Gamma(B;A)\longrightarrow R\Gamma(B_{N-r+1};A)
\longrightarrow R\Gamma(B_{N-r};A)
$$

give the fibre triangle

$$
F_{r-1}\longrightarrow F_r\longrightarrow Q_{N-r+1}
\longrightarrow F_{r-1}[1].
\tag{IHM7}
$$

For completeness, this triangle follows by applying the cone construction to the two composable maps: the fibre of the composite maps to the fibre of the second map, and its fibre is the fibre of the first map. Thus IHM7 uses the actual restriction maps. No duality, arbitrary splitting or reversal of the cohomological functor is required.

## SH02-IHM-DEGREE — The tangential index is the complex dimension

Let the critical point lie on a stratum $S$ of complex dimension $d$. Write $c=g_t(p)$, with $c-v\ne0$. At the critical point of $g_t|_S$, the quadratic part of IHM2 on $S$ is

$$
2\operatorname{Re}\left(\overline{c-v}\,q\right),
\tag{IHM8}
$$

where $q$ is its nondegenerate complex quadratic part. The additional term $|g_t-c|^2$ begins in order four. Complex linear coordinates diagonalize $\overline{c-v}\,q$ as a sum of squares. Each complex coordinate contributes one positive and one negative real square. Consequently the real Morse index is $d$.

The nonzero complex scalar multiplying the normal covector stays in the connected set of generic complex conormal directions. The normal Morse datum is therefore isomorphic to the fixed normal object $N_S(A)$. The normal-tangential theorem gives

$$
Q_j\simeq N_S(A)[-d].
\tag{IHM9}
$$

The isomorphism class is enough for the argument. It does not require a global trivialization of the normal Morse local system or a preferred transport around its monodromy.

## SH02-IHM-POSITIVITY — A nonempty isolated intersection contributes a point

The count theorem already identifies the number of perturbed Morse points with the conormal intersection multiplicity. We prove the strict positivity needed here from finite analytic maps, so a second unspecified intersection-positivity theorem is unnecessary.

Let $\dim_{\mathbb C}Y=n$, let $\Lambda$ be an irreducible component of $\overline{T^*_S Y}$ through $p=(y,dg_y)$, and suppose that $p$ is isolated in its intersection with $\operatorname{graph}(dg)$. The analytic conormal construction makes $\Lambda$ pure of dimension $n$. In local cotangent coordinates, consider the holomorphic map $H(z,\xi)=\xi-dg_z$ from $\Lambda$ to $\mathbb C^n$. Its zero fibre is isolated at $p$.

Choose a small closed coordinate ball whose intersection with this zero fibre is just $p$. The norm of $H$ has a positive minimum on the compact part of $\Lambda$ on the boundary. If that boundary part is empty, any sufficiently small positive radius has the same property. Restrict the target to a ball of smaller radius, and restrict the source to its inverse image inside the open coordinate ball. This representative of $H$ is proper: the inverse image of a compact target set is closed in the original closed ball and misses its boundary.

Every fibre is a compact analytic subset of an open affine chart, hence is finite. The exact analytic fact used here is [Demailly, II.5.9, p.104](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf#page=104): compact analytic subsets are finite when global holomorphic functions separate points. Coordinate functions supply that condition in an affine chart. This fact applies to singular analytic spaces as well.

Thus $H$ is finite. The finite-image dimension theorem shows that the image of each source component through $p$ is closed analytic of dimension $n$ in the connected $n$-dimensional target ball. It is therefore the whole ball: a proper analytic subset has smaller dimension. Consequently every sufficiently small target value has a nonempty fibre in this representative.

Remove from $\Lambda$ its singular locus, its part over the boundary of $S$, and the locus where $dH$ has rank less than $n$. These are contained in a proper closed analytic subset. For the rank condition this is the augmented-minor construction and finite-map rank lemma in FAG3; the other two subsets are analytic because the conormal and the stratum boundary are analytic. They are proper because the conormal over $S$ is dense and smooth. Their image under the finite proper map is a proper analytic subset of the target.

Choose a constant covector $\lambda$ such that the small punctured line $t\lambda$ avoids this bad image. To see such choices exist, take a nonzero holomorphic equation vanishing on the image and choose $\lambda$ outside the zero set of its first nonzero homogeneous part. The restriction of this equation to the line then has an isolated zero at $t=0$. One can simultaneously make the generic choice required by Massey's isolated count theorem.

Write $L(z)=\langle\lambda,z\rangle$. For small nonzero $t$, the nonempty fibre $H^{-1}(t\lambda)$ consists of transverse intersections of the smooth conormal over $S$ with $\operatorname{graph}(d(g+tL))$. These are precisely the Morse critical points of $(g+tL)|_S$: the intersection equation says that its differential annihilates $TS$, and transversality says that the tangential Hessian is nondegenerate. The genericity in the count theorem supplies the stratified normal nondegeneracy as well. Compactness and isolation of the zero fibre show that these points converge to $p$ as $t$ tends to zero, so they belong to its local cluster.

The count in Massey's Theorem 1.1, pp.3–4, is therefore at least one. Since that theorem identifies it with the local conormal intersection multiplicity, the latter is strictly positive. For $n=0$ the component and target are points and the count is one. The proof concerns geometric counts before a coefficient field is introduced.

## SH02-IHM-INTEGER — Positivity is an integer assertion

For a perverse $K$-sheaf $P$, the field-perverse normal-Morse theorem says that $N_S(P)[-\dim S]$ is a finite-dimensional vector space in degree zero. Apply this to IHM7. Inductively every $F_r$ is concentrated in degree zero, and its cohomology sequence is short exact:

$$
0\longrightarrow H^0F_{r-1}\longrightarrow H^0F_r
\longrightarrow H^0Q_{N-r+1}\longrightarrow0.
\tag{IHM10}
$$

Taking ordinary vector-space dimensions and grouping the points by conormal component gives

$$
\begin{aligned}
\dim_K H^0M_g(P)_y
&=\sum_S n_S\,\dim_K\bigl(N_S(P)[-\dim S]\bigr),\\
n_S&=I_{(y,dg_y)}\bigl(\overline{T^*_S Y},\operatorname{graph}(dg)\bigr).
\end{aligned}
\tag{IHM11}
$$

The counts $n_S$ are the nonnegative integers of the isolated theorem. At a nonempty isolated intersection they are strictly positive by the preceding finite-map argument. This is a geometric positivity statement before coefficients are introduced. In particular IHM11 is an equality in $\mathbb Z$ even when $K$ has positive characteristic. It is not the trace of an endomorphism reduced modulo that characteristic.

If a visible conormal meets the graph at this isolated point, one term of IHM11 is positive, while all terms are nonnegative. Therefore the actual supported test is nonzero. If $y$ had empty vanishing-cycle support in the preliminary alternative above, the same isolated theorem would give a zero left side and force every term to vanish. Thus that alternative cannot occur in the presence of a visible isolated conormal intersection.

## SH02-IHM-SCOPE — What this supplies to the finite-map proof

This calculation supplies the controlled filtration, its maps and the integer nonvanishing consequence for every field. It includes a point stratum ($d=0$), an empty collection of contributing Morse points, invisible strata with zero normal object, and a zero pulled-back covector whenever the graph intersection is isolated. The isolation must be checked against every stratum in the adapted finite local stratification, as done in the finite-map proof.

The original coefficient ring in FH1 is not required to be a field or noetherian. This supplement is applied only after the finite-map proof passes to a residue field. Perfect finite normal-pair models and derived residue-field detection are separate steps; IHM11 neither replaces those steps nor assumes perverse theory over the original ring. The full finite-map equality also depends on the other three explicit geometric inputs, which are not proved here.
