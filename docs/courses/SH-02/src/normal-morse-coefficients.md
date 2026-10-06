# SH02-NMC-UNIT — Normal Morse data and change of coefficients

Proof draft, independently reviewed at the scope stated here. The coefficient argument below supplies the normal-Morse input used by the [finite holomorphic map proof](finite-holomorphic-microsupport.md#SH02-FH-NORMAL-MORSE-INPUT). It retains the geometric normal-pair and stratified-continuation theorems as explicit external prerequisites.

Let $X$ be a complex analytic manifold, or a closed analytic subset of a complex manifold $M$, and let $A$ be a bounded complex of sheaves of $k$-modules on $X$. In the manifold case take $M=X$. For a closed analytic embedding $i:X\hookrightarrow M$, every microsupport in the statement means the microsupport of $i_*A$ in $T^*M$. All manifolds have finite dimension, are Hausdorff and are countable at infinity. Fix a locally finite complex analytic Whitney stratification on which every cohomology sheaf of $A$ is locally constant. The coefficient ring $k$ can be any commutative ring with identity for the comparison with underlying abelian sheaves below. For the full statement used in the finite-map lesson, assume that $k$ has finite global dimension and every stalk of $A$ is perfect over $k$. These assumptions are needed only for the subsequent boundedness and perfection conclusions. A perfect complex is represented by a bounded complex of finite projective modules.

## SH02-NMC-FORGET — Exact restriction of scalars

Write $U$ for the functor from sheaves of $k$-modules to sheaves of abelian groups. It is exact and conservative. Exactness can be checked on stalks, where it is exact restriction of scalars along $\mathbb Z\to k$; conservativity follows from the same observation. It commutes with inverse image, stalks, sections, products and restriction maps. Consequently it preserves finite sums, fibres and cones of complexes.

## SH02-NMC-DERIVED — Derived direct images on the same resolutions

Here is a derived justification that does not assume that an injective $k$-module is injective over $\mathbb Z$. Every injective sheaf of $k$-modules is flabby. For open inclusions $V\subset W$, extension of a section follows by applying injectivity to the monomorphism $k_V\to k_W$, with extension by zero interpreted on the ambient space. Flabbiness is a condition on the underlying restriction maps, so forgetting coefficients preserves it. Flabby sheaves are acyclic for sections on every open set, with the precise direct-image acyclicity argument given in the coefficient bridge. An injective resolution over $k$, after forgetting, is therefore a resolution by sheaves acyclic for the section functors that compute a direct image. A bounded-below resolution suffices because $A$ is bounded.

It follows, with the usual comparison maps, that

$$
 U Rq_* A \simeq Rq_* U A,
 \qquad U R\Gamma(T;A)\simeq R\Gamma(T;UA).
 \tag{NMC1}
$$

For the second identity, $T$ can be any of the spaces used below, after restricting the sheaf to that space. For the first identity, $q$ is a continuous map between the relevant spaces. Each direct-image stalk is obtained from sections on inverse images of open sets, so the same resolution verifies the assertion. These comparisons preserve the adjunction units and restriction maps: all are computed by the original maps on the same underlying resolutions.

## SH02-NMC-SUPPORT — Supported tests and the actual restriction maps

For a closed set $Z$ and its open complement $j$, the local-support object is the fibre of $A\to Rj_*j^{-1}A$. Applying the preceding argument to that triangle gives

$$
 U R\Gamma_Z A\simeq R\Gamma_Z UA.
 \tag{NMC2}
$$

Similarly, a relative cohomology object is the fibre of the restriction from $K$ to $L$, and hence

$$
 U R\Gamma(K,L;A)\simeq R\Gamma(K,L;UA).
 \tag{NMC3}
$$

These are comparisons of the actual morphisms. They are not assertions that an arbitrary isomorphism of underlying abelian complexes lifts to an isomorphism of $k$-complexes. In particular, a $k$-linear comparison constructed by restriction, localization, inverse image, or a chosen geometric continuation is an isomorphism as soon as its underlying comparison is one. For chosen continuations, one retains the original zigzag of restriction and pullback maps and inverts only those maps proved to be isomorphisms. Their inverses remain $k$-linear.

Forgetting coefficients preserves weak constructibility on the fixed stratification: the same local trivializations of the cohomology sheaves are trivializations of the underlying abelian sheaves. It need not preserve finite generation. This distinction is why the weakly constructible versions of the source results are required.

The definition by supported local tests and NMC2 also give the exact equality

$$
 \operatorname{SS}_k(A)=\operatorname{SS}_{\mathbb Z}(UA).
 \tag{NMC4}
$$

Indeed each test object vanishes over $k$ if and only if its underlying abelian object vanishes, with the same neighborhoods, covectors and real test functions.

## SH02-NMC-PAIR — An actual compact normal pair

At a point $x$ of a connected stratum $S$, take a transverse complex normal slice $N$, of complex codimension $\dim S$. Choose a holomorphic germ $g$ with $g(x)=0$ whose differential at $x$ is a nondegenerate conormal for the fixed stratification. Here $dg_x$ annihilates $T_xS$ and does not vanish identically on any generalized tangent space of an incident higher stratum, as in [Maxim–Schürmann, Definition 3.9, p. 27](https://people.math.wisc.edu/~lmaxim/handbook.pdf#page=27). On the normal slice, $x$ is an isolated stratified critical point of $g$. For sufficiently small nested parameters, put

$$
 K=X\cap N\cap\{r\leq\epsilon\},
 \qquad L=K\cap\{g=w\},
 \qquad 0<|w|\ll\epsilon,
 \tag{NMC5}
$$

where $r$ is squared distance in local ambient coordinates. Shrink inside a relatively compact coordinate neighborhood. Both sets are compact, and $L$ is closed in $K$. The direction of $w$ and continuation paths are fixed once; no canonical trivialization of all possible choices is claimed.

The geometric inputs are stated in Maxim–Schürmann, *Constructible sheaf complexes in complex geometry and applications*: [Theorem 3.12, pp. 28–29](https://people.math.wisc.edu/~lmaxim/handbook.pdf#page=28), [Proposition 3.14, pp. 29–30](https://people.math.wisc.edu/~lmaxim/handbook.pdf#page=29), and [Proposition 4.11, Corollary 4.14 and Remark 4.18, pp. 65–66](https://people.math.wisc.edu/~lmaxim/handbook.pdf#page=65). These provide the normal slice, the small regular fibre with boundary, and the geometric comparison with the supported real test. Their [coefficient convention and Definition 2.2, p. 6](https://people.math.wisc.edu/~lmaxim/handbook.pdf#page=6), require a noetherian commutative coefficient ring of finite global dimension. The stated theorems apply to **weakly** constructible complexes, which may have infinitely generated stalk cohomology. Apply them with coefficient ring $\mathbb Z$ to $UA$. Thus no finite-generation condition on the underlying abelian stalks is introduced.

The maps in this local calculation are the restriction maps from the normal ball to its link and the maps from the localization triangle. Boundary regularity gives the geometric continuation between the negative real test region and the chosen regular fibre. Choose that continuation at the level of the fixed Whitney stratification and perform the restriction/pullback zigzag with $k$-sheaves. After applying $U$, it is the same zigzag appearing in the local calculation over $\mathbb Z$; its arrows that are inverted are isomorphisms there. NMC1–NMC3 therefore allow the same inversions over $k$. This gives

$$
 M_S(A):=R\Gamma(K,L;A)
 \simeq
 \bigl(R\Gamma_{\{\operatorname{Re}g\geq0\}}(A|_{X\cap N})\bigr)_x.
 \tag{NMC6}
$$

One can describe the restriction arrow in NMC6 without forgetting its provenance. Restriction from a small normal ball to its centre is an isomorphism; this small-radius stabilization holds after a compact local truncation, which supplies the needed properness. Invert this map in the derived category and then restrict from the ball to $L$. The resulting arrow is $A_x\to R\Gamma(L;A)$. Its fibre is the first normal-Morse triangle of Proposition 3.14, equation (27). This fixes the same shift as the supported-test definition: the normal pair computes the fibre, rather than the unshifted cone of the specialization arrow.

This invocation concerns an isolated critical point on a normal slice. It fixes a concrete local pair and its comparison maps. The stronger nonisolated critical-support theorem discussed in the finite-map lesson is a separate dependency.

## SH02-NMC-STABILITY — Small choices, continuation and the open stratum

The normal-pair geometry and the allowed ranges of radii are selected using the stratification, the normal slice and $g$. They are independent of the coefficients and of scalar extension. The normal-Morse continuation and invariance in Theorem 3.12(2), and the link invariance in Proposition 3.14, use the same kind of geometric maps. Applying the same $k$-linear construction and NMC1–NMC3 proves stability for sufficiently small parameters and invariance up to isomorphism under admissible choices and motion along a connected generic conormal component. No global choice of a trivialization of the Morse local system is needed.

For an open stratum the normal slice is a point, $L$ is empty, and $M_S(A)=A_x$. This also supplies the zero-section component. Empty data and the zero coefficient ring give zero objects throughout.

## SH02-NMC-TRIANGULATION — A finite model with perfect simplex data

Every set in NMC5 is real subanalytic. Refine the locally finite subanalytic partition consisting of the fixed strata, $K$, $L$ and their complements. [Kashiwara–Schapira, Proposition 8.2.5, p. 328](https://doi.org/10.1007/978-3-662-02661-8), gives a compatible locally finite triangulation of the ambient neighborhood. Since $K$ and $L$ are closed unions of simplices, they are subcomplexes; compactness and local finiteness imply that only finitely many simplices occur in $K$. Thus $(K,L)$ is an actual finite compact pair, not a formal limiting object.

On each open simplex, the cohomology of $A$ is locally constant. The simplex is contractible. The ordinary local-system calculation on a simplex and the bounded cohomology spectral sequence with its natural edge show that the counit from the constant complex with value $R\Gamma(\sigma;A)$ to $A$ is a quasi-isomorphism there. Its stalk is a perfect $k$-complex under the hypotheses above. Thus the pair has a compatible finite triangulation and the restriction to every open simplex is a constant perfect complex. The cohomology modules need not be free.

## SH02-NMC-COEFFICIENTS — The finite skeletal coefficient comparison

We give the finite-pair argument, including its restriction map. Let $(K,L)$ be a compact finite simplicial pair, with $L$ a subcomplex, and let $A$ restrict on every open simplex to a constant perfect complex. Filter $K$ by its closed skeleta. The difference between two consecutive skeleta is a finite union of open simplices. For an oriented $d$-simplex $\sigma$ and its constant perfect coefficient complex $P$, the compactly supported orientation calculation gives

$$
R\Gamma_c(\sigma;P)\simeq P[-d].
\tag{NMC7}
$$

This is the Euclidean orientation calculation in manifold duality. Its scalar comparison uses the same orientation generator after tensoring. The generator is selected only for this local calculation; no global orientation of the stratified space is required.

At each skeletal step, the open-closed localization triangle gives a triangle of compactly supported cohomology objects. The coefficient comparison is natural for all three arrows. It is an isomorphism on the open simplices by NMC7, and hence on the next skeleton by induction. Finite sums and cones of perfect complexes are perfect. This proves both perfection and the coefficient comparison for $R\Gamma_c(K;A)$. Compactness identifies this with ordinary cohomology.

Apply the same argument to $L$. Relative cohomology is the fibre of the restriction $R\Gamma(K;A)\to R\Gamma(L;A)$. The two coefficient comparisons commute with that restriction, so taking their fibres gives the natural isomorphism

$$
R\Gamma(K,L;A)\otimes_k^L B
\xrightarrow{\sim}
R\Gamma(K,L;A\otimes_k^L B).
\tag{NMC8}
$$

The relative complex is perfect as well. For the fixed normal pair, this proves

$$
 M_S(A)\in\operatorname{Perf}(k),
 \qquad
 M_S(A)\otimes_k^L B\xrightarrow{\sim}
 M_S(A\otimes_k^L B).
 \tag{NMC9}
$$

Here $B$ is any ordinary coefficient $k$-algebra. Finite global dimension of $k$ bounds the Tor amplitude of $B$, so $A\otimes_k^L B$ remains bounded. Its cohomology is locally constant on the same strata and its stalks are perfect over $B$: scalar extension sends a finite projective $k$-module to a finite projective $B$-module. The geometric pair on both sides is identical. All tensor comparisons in this proof concern a finite skeletal construction.

## SH02-NMC-VISIBLE — The conormals that detect microsupport

[Proposition 3.13 of Maxim–Schürmann, p. 29](https://people.math.wisc.edu/~lmaxim/handbook.pdf#page=29), applies to the $\mathbb Z$-weakly constructible object $UA$. It identifies its microsupport as the union of closed conormals with nonzero normal Morse data. The preceding paragraphs identify those data with the underlying objects of $M_S(A)$. Exact conservativity and NMC4 give

$$
 \operatorname{SS}_k(A)
 =\bigcup_{M_S(A)\not\simeq0}\overline{T^*_S M}.
 \tag{NMC10}
$$

The conormal in NMC10 is taken in the fixed ambient manifold $M$. Locally only finitely many strata occur. A connected generic conormal component is either visible everywhere on its generic locus or invisible there, by the continuation established above. Formula NMC10 uses closures and does not require nonzero Morse data at every boundary point of such a closure.

## SH02-NMC-STATUS — What the coefficient argument supplies

The compact pair, its supported-test identification, the scalar comparison and the visible-conormal formula supply the normal-Morse portion of the [finite-map prerequisites](finite-holomorphic-microsupport.md#SH02-FH-NORMAL-MORSE-INPUT). In particular, the same normal object can be tested over every residue field of $k$ using a finite pair.

The geometric prerequisites are the existence and continuation of the normal pair, its comparison with a supported test, the normal-Morse description of microsupport, and compatible subanalytic triangulation. The exact external statements are cited above. The coefficient extension proved here does not remove the other analytic, controlled-Morse or field-perverse prerequisites of the finite-map theorem.
