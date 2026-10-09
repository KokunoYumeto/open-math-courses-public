# Derived module coefficients and their spectrum model

*Written by GPT-6.1 Sol (OpenAI). Self-checked by the writing AI. CC0 1.0.*

The coefficient category in the modern sheaf construction is the category of complexes with quasi-isomorphisms inverted. To compare it with module spectra, one must identify the actual tensor product as well as the objects. We prove that comparison for every commutative unital ring, including rings of infinite global dimension.

<a id="COEFF0"></a>

## COEFF0. Models and the formal categorical operations

Fix a commutative unital ring \(k\). Write \(D_\infty(k)\) for the derived infinity-category of all cochain complexes of \(k\)-modules. Its standard complex model supplies a stable category with small colimits, closed derived tensor product, unit \(k[0]\), and tensor preserving colimits in each variable. The category of spectra supplies its usual stable mapping objects and tensor action on this category. These are the ambient complex, spectrum and localization constructions; no assertion about an infinity-category of sheaves is used here.

We use geometric realizations and the ordinary two-sided bar construction for an associative ring spectrum acting on an object of a stable category. Its universal property is proved in COEFF2. Spectra are generated under shifts, coproducts and cofibres by the sphere spectrum. One verification uses a cellular approximation: add sphere cells representing all homotopy classes, add cells killing all kernels, and repeat; homotopy groups of the resulting filtered union agree with the prescribed spectrum. Homotopy groups detect equivalences of spectra.

We use the cohomological convention \(H^q(C[s])=H^{q+s}(C)\). Mapping spectra then have

\[
 \pi_n\operatorname{Map}(k,C)=H^{-n}(C).
 \tag{COEFF0a}
\]

Indeed the chain complex \(\operatorname{Hom}^\bullet(k,C)\) is exactly \(C\), and \(k\) is K-projective: this Hom complex is acyclic when \(C\) is acyclic. Thus the formula computes derived maps for arbitrary unbounded \(C\).

<a id="COEFF1"></a>

## COEFF1. The unit generates all complexes and mapping preserves colimits

Every object of \(D_\infty(k)\) is constructed from shifts of \(k\) by coproducts and cofibres followed by a sequential colimit. Here is an explicit construction. For a representative complex \(C\), choose cycles representing every element of every \(H^n(C)\). Their sum gives

\[
 P_0=\bigoplus_{n,\,c\in H^n(C)} k[-n]\longrightarrow C,
 \tag{COEFF1a}
\]

surjective on every cohomology group. Suppose \(P_r\to C\) is constructed with that property. For every class in the kernel of \(H^n(P_r)\to H^n(C)\), choose a representing cycle in \(P_r\) and a primitive for its image in \(C\). Attach the cone of the corresponding map \(k[-n]\to P_r\). The chosen primitive extends the map of that cone to \(C\). Perform all these attachments at once by the coproduct of the maps. The resulting \(P_{r+1}\to C\) is still surjective on cohomology, and every previous kernel class has become zero.

Take the sequential colimit of this complex diagram. Filtered colimits of modules are exact, so cohomology commutes with this colimit. Every class is represented at a finite stage and every kernel class is killed at the next stage. The colimit map to \(C\) is therefore a quasi-isomorphism. This proves the generation assertion, without any finite-generation or boundedness hypothesis. The sequential derived colimit is computed by the mapping telescope: the map \(1-\mathrm{shift}\) on the coproduct of the stages is degreewise monic, with cokernel their termwise colimit, so its cofiber gives the same object.

Let \(G=k[0]\), and set \(R=\operatorname{End}(G)\), with its composition multiplication. Since \(G\) is the tensor unit, this is an E-infinity ring spectrum; the tensor interchange law supplies its commutative coherences. Precomposition equips the mapping spectrum with a right \(R\)-module action. Define

\[
 \Omega(C)=\operatorname{Map}(G,C)\in\operatorname{Mod}_R.
 \tag{COEFF1b}
\]

The functor is exact, since mapping preserves limits and finite limits equal finite colimits in stable categories. It preserves coproducts: the comparison on homotopy groups is the direct-sum identity in (COEFF0a), because cohomology commutes with direct sums of modules. The comparison is therefore an equivalence of spectra, retaining its \(R\)-action. Exactness and preservation of coproducts imply preservation of all small colimits. To check the last implication, realize a simplicial replacement of a diagram. Each skeleton is built using coproducts and finite cofibres, and its sequential assembly is the coproduct-and-cofiber telescope. These are precisely the operations already preserved. Thus this implication does not assume the Morita theorem we are proving.

Formula (COEFF0a) also gives

\[
 \pi_n R=
 \begin{cases}k,&n=0,\\0,&n\ne0.\end{cases}
 \tag{COEFF1c}
\]

The degree-zero multiplication is the multiplication of \(k\). A spectrum concentrated in degree zero is its Eilenberg–Mac Lane spectrum; the degree-zero truncation of this E-infinity algebra identifies it with the discrete commutative ring spectrum \(Hk\). This identification includes its unit and multiplication, rather than identifying only the underlying homotopy groups.

<a id="COEFF2"></a>

## COEFF2. The actual bar adjunction and equivalence

The evaluation action of \(R\) on \(G\) defines

\[
\begin{gathered}
L(M)=M\otimes_R G\\
=\left|[n]\longmapsto M\otimes R^{\otimes n}\otimes G\right|.
\end{gathered}
\tag{COEFF2a}
\]

The tensors preceding \(G\) are spectral tensors acting on the complex category. The face maps use the action on \(M\), multiplication in \(R\), and evaluation on \(G\); the degeneracies insert the unit of \(R\). This is an actual functor, with these maps, and preserves colimits.

Mapping its realization to \(C\) is the limit of the corresponding mapping spectra. Tensor–mapping adjunction turns that cosimplicial diagram into the diagram of maps from the free \(R\)-module bar resolution of \(M\) to \(\Omega C\). The augmented free bar resolution realizes to \(M\): after forgetting the module action, insertion of the unit is an extra degeneracy contracting the augmentation. Forgetting module action creates this realization, since the \(R\)-action is formed on the coefficient colimit and \(R\otimes-\) preserves it. Consequently the limit is the mapping spectrum of \(R\)-linear maps. We have proved the specific enriched adjunction

\[
\begin{gathered}
\operatorname{Map}_{D_\infty(k)}(L(M),C)\\
\simeq\operatorname{Map}_{\operatorname{Mod}_R}(M,\Omega C).
\end{gathered}
\tag{COEFF2b}
\]

Its unit is the action-compatible map \(M\to\operatorname{Map}(G,L(M))\); its counit is the bar evaluation \(L\Omega C\to C\). For the free rank-one module, the unit insertion contracts its bar construction and gives \(L(R)=G\). The unit at \(R\) is then the identity \(R=\operatorname{Map}(G,G)\), and the counit at \(G\) is evaluation of this same identity. Both are equivalences.

The module category is generated under colimits and stable operations by \(R\). Indeed the preceding free bar resolution writes a module as the realization of free modules. A free module is \(R\otimes S\) for a spectrum \(S\); the sphere-cell construction in COEFF0 writes this free module using shifts, coproducts and cofibres of \(R\). Thus no separate compact-generator Morita theorem is being invoked in this argument.

Both \(L\) and \(\Omega\) preserve colimits and are exact. The full class of modules on which the unit is an equivalence is therefore closed under those operations and contains \(R\); it is all modules. The corresponding class of complexes on which the counit is an equivalence contains \(G\), and COEFF1 shows it is all complexes. The adjunction (COEFF2b) is an equivalence, with its specified unit and counit.

<a id="COEFF3"></a>

## COEFF3. The symmetric monoidal comparison

Mapping out of the tensor unit has the canonical lax symmetric monoidal pairing. For complexes \(C,D\), tensor two maps out of \(G\) and use \(G\otimes_k^L G=G\). Its balanced coefficient form is

\[
 \Omega C\otimes_R\Omega D
 \longrightarrow\Omega(C\otimes_k^L D).
 \tag{COEFF3a}
\]

Its unit is \(R=\Omega G\). The balance relation uses the same evaluation action as COEFF2; associativity and symmetry are the tensor product's coherent ones, including the Koszul sign on homogeneous complex terms. These are natural maps before we assert their invertibility.

For \(C=G\), (COEFF3a) is the unit isomorphism for every \(D\). Fix any \(D\). Both sides preserve colimits and are exact as functors of \(C\), by COEFF1 and the coefficient tensor hypotheses. The class on which this natural map is an equivalence is consequently closed under the operations that generate all complexes from \(G\). The map is an equivalence for every \(C,D\). The canonical lax comparison is thus a strong symmetric monoidal comparison. Together with COEFF1c and COEFF2, it gives

\[
\begin{gathered}
D_\infty(k)\simeq\operatorname{Mod}_{Hk}\\
\text{as symmetric monoidal }\\
\text{infinity-categories.}
\end{gathered}
\tag{COEFF3b}
\]

No finite global dimension has been used. Such a bound enters later when requiring tensor products of arbitrary bounded-below sheaf complexes to retain a uniform lower bound. The coefficient equivalence here concerns all module complexes; identifying an ordinary infinity-category of sheaves with a classical sheaf derived category is a separate recognition theorem.

The classical coefficient comparison is Jacob Lurie's [Higher Algebra](https://www.math.ias.edu/~lurie/papers/HA.pdf), September 18, 2017, Theorem 7.1.2.13, pages 1212–1213. The proof above expands its compact-unit mechanism through the explicit cell construction and bar adjunction, rather than using its compact-generator theorem as an unexplained step. The ambient projective complex model, spectral tensors and stable categorical operations are the models specified in COEFF0.
