# Base change and the Grothendieck complex

*Written by GPT-6.1 Sol (OpenAI), in Codex, at Ultra effort, October 2026. Self-checked by the writing AI, GPT-6.1 Sol, at Ultra effort. Public domain (CC0).*

Pulling back a cohomology sheaf and computing cohomology on the pulled-back family are different operations. Flat change of the base makes them agree. For a proper family with a flat coherent sheaf, a stronger statement is available: one finite projective complex computes cohomology after every change of the base. Its differentials, rather than the ranks of its cohomology modules, retain the information needed at exceptional fibers.

We use [affine cohomology and quasi-coherent direct images](affine-cohomology-and-serres-criterion.md), proper cohomology finiteness, and the flat-module results assigned to *Tor and flat modules* in *Commutative algebra for geometry*. For the initial derived construction we use [K-flat resolutions](https://kokunoyumeto.github.io/open-math-courses-public/courses/derived-categories-and-sheaf-operations/flat-modules-and-k-flat-resolutions.html), [derived tensor](https://kokunoyumeto.github.io/open-math-courses-public/courses/derived-categories-and-sheaf-operations/derived-tensor-products-and-tor-sheaves.html) and the [pullback–pushforward adjunction](https://kokunoyumeto.github.io/open-math-courses-public/courses/derived-categories-and-sheaf-operations/derived-pullback-and-pushforward.html). The exact open adjunction proof is [Stacks, Tag 079W], with its derived-adjunction construction linked below. Our finite projective replacement and its universal tensor comparison are proved in Section 3.

## 1. Constructing the comparison

Fix a cartesian square
\[
\begin{array}{ccc}
X'&\xrightarrow{g'}&X\\
{\scriptstyle f'}\downarrow&&\downarrow{\scriptstyle f}\\
S'&\xrightarrow{g}&S.
\end{array}
\]
Let \(F\) be quasi-coherent on \(X\), and put \(F'=g'^*F\). A sheaf is **flat over \(S\)** when every \(F_x\) is flat over \(\mathcal O_{S,f(x)}\); for \(F=\mathcal O_X\), this defines a flat morphism. Base change preserves this stalkwise condition. Flatness of \(F\) and flatness of \(g\) will enter different theorems.

The canonical comparison maps are
\[
\beta^q:g^*R^qf_*F\longrightarrow R^qf'_*F'.
\]
Here is a derived construction that also applies to a nonflat \(g\). Derived adjunction turns the composite
\[
Lf'^*Lg^*Rf_*F
\cong Lg'^*Lf^*Rf_*F
\longrightarrow Lg'^*F
\longrightarrow g'^*F
\]
into a map \(Lg^*Rf_*F\to Rf'_*F'\). The first arrow is the pullback–pushforward counit; the last is the natural map from derived pullback of a sheaf to its degree-zero, ordinary pullback. Commutation of the two derived pullbacks follows from equality of the composite morphisms and composition of derived pullback. It does not assert that derived pullback is exact.

There is a natural cohomology edge map
\[
g^*H^q(C)\longrightarrow H^q(Lg^*C)
\]
for a bounded-above cohomology object \(C\). Locally, choose a bounded-above free resolution \(P\) of its complex over \(A\), and use the cocycle map
\[
H^q(P)\otimes_A B\longrightarrow H^q(P\otimes_A B).
\]
A cocycle tensored with an element of \(B\) is still a cocycle; an original boundary becomes a boundary. Right exactness of tensor lets this descend from the cocycle module to \(H^q(P)\otimes B\). Homotopic comparison maps of free resolutions induce the same map, so the edge is intrinsic and compatible with restriction. Composing it with the cohomology map of the derived comparison defines \(\beta^q\). For the quasi-compact, quasi-separated morphisms used below, the boundedness needed here is the affine-cover bound from the third lesson. For flat \(g\), the edge is simply the identification \(g^*H^q(C)=H^q(g^*C)\).

The construction is functorial in \(F\) and in successive base changes: units, counits and pullback composition give the same map for a composite square as for the two successive squares. On affine charts with a Čech model, it is the cocycle comparison just described. Thus the isomorphisms proved below concern these canonical maps, not a separately chosen identification of abstract vector spaces.

**Proposition 1.1 (affine morphisms).** If \(f\) is affine, every \(\beta^q\) is an isomorphism for every base change \(g\), without a flatness assumption.

**Proof.** Higher direct images of a quasi-coherent sheaf under an affine morphism are zero, and the same holds for \(f'\). Locally write \(S=\operatorname{Spec}A\), \(X=\operatorname{Spec}R\), \(S'=\operatorname{Spec}B\), and \(F=\widetilde M\). The pullback sheaf corresponds to
\[
M\otimes_R(R\otimes_A B)\cong M\otimes_A B.
\]
This is precisely the degree-zero base-change map. The tensor identity proves the assertion in degree zero, and the vanishing proves it in higher degrees. \(\square\)

The hypothesis concerns the morphism \(f\). Affineness of \(g\) alone does not guarantee comparison isomorphisms; a closed point of an affine parameter scheme is already a nonflat affine base change.

## 2. Flat base change, including nonseparated schemes

**Theorem 2.1 (flat base change).** If \(f\) is quasi-compact and quasi-separated, \(F\) is quasi-coherent, and \(g\) is flat, then
\[
g^*R^qf_*F\xrightarrow{\sim}R^qf'_*F'\quad(q\geq0).
\]
In particular, for a flat ring map \(A\to B\) and a quasi-compact, quasi-separated \(A\)-scheme,
\[
H^q(X,F)\otimes_A B\xrightarrow{\sim}H^q(X_B,F_B).
\]

**Proof.** First suppose \(S,S'\) are affine and \(X\) is separated. Choose a finite affine cover \(U_1,\ldots,U_r\). Its intersections are affine, so the finite ordered complex \(C^\bullet\) of their section modules computes cohomology. The induced cover after base change again has affine intersections. Proposition 1.1 identifies its section complex with \(C^\bullet\otimes_A B\). Flatness of \(B\) preserves kernels and images and gives
\[
H^q(C^\bullet)\otimes_A B\cong H^q(C^\bullet\otimes_A B).
\]
The identification is the canonical cocycle map.

For a quasi-separated \(X\), a finite affine cover still exists, but its intersections need not be affine. Each intersection \(U_I\) is quasi-compact and separated: it is an open subscheme of one of the affine \(U_i\). The case just proved therefore applies to every \(U_I\). Use the Čech-to-cohomology spectral sequence of the second lesson, in the form
\[
E_1^{p,q}=\bigoplus_{|I|=p+1}H^q(U_I,F)\Longrightarrow H^{p+q}(X,F).
\]
Tensoring this spectral sequence with flat \(B\) preserves its successive kernels, images and cohomology. The comparison with the base-changed cover is an isomorphism on every first-page term, by the separated case. Hence it is an isomorphism on every page and on the filtered abutments. The cover has finitely many intersections and each has a finite affine-cover cohomological bound, so there are only finitely many possibly nonzero terms. Convergence and comparison therefore involve finite filtrations and prove the asserted global identity.

Finally work locally on \(S'\), with its affine open contained over an affine open of \(S\). The higher direct images are quasi-coherent by the third lesson, and over this affine base they are the sheaves associated to the cohomology modules just compared. The global identities give the sheaf comparison locally, and canonical functoriality glues them. \(\square\)

Notice that \(F\) need not be flat over the original base in this theorem. Tensor is exact because the *change of base* is flat. In contrast, we next keep \(F\) flat and permit every change of base.

## 3. A finite projective replacement

We first prove the algebraic step, retaining its tensor behavior rather than only its cohomology over the original ring.

**Lemma 3.1 (bounded flat complexes).** Let \(A\) be Noetherian. Let \(C^\bullet\) be a complex of flat \(A\)-modules, zero outside \([a,b]\), with finite cohomology modules. There is a complex \(K^\bullet\) of finite projective modules, also zero outside \([a,b]\), and a quasi-isomorphism
\[
K^\bullet\longrightarrow C^\bullet
\]
that remains a quasi-isomorphism after tensoring with every \(A\)-module.

**Proof.** We construct a bounded-above finite free resolution of the complex, then truncate its unnecessary left tail.

Start with no terms of \(P\), and attach them in descending degrees, beginning at \(b\). Suppose terms \(P^{j+1},\ldots,P^b\) and a chain map \(f:P\to C\) have been constructed, with its cone \(D\) having zero cohomology in degrees above \(j\). The cone terms and differential are
\[
D^i=C^i\oplus P^{i+1},\qquad d_D(c,p)=(d_Cc+f(p),-d_Pp).
\]
Its cohomology modules are finite. This holds initially for \(C\), and remains true for a cone of a map from a finite complex of finite free modules: its long exact sequence expresses cohomology as extensions of subquotients of finite modules, which are finite because \(A\) is Noetherian.

Choose finitely many cocycles \((c_\ell,p_\ell)\) generating \(H^j(D)\). Set \(P^j\) equal to the finite free module on these choices and define
\[
f(e_\ell)=c_\ell,\qquad d_P(e_\ell)=-p_\ell.
\]
The cocycle equations give \(d_P^2=0\) and \(d_Cf=fd_P\). In the new cone, the differential of \((0,e_\ell)\) is \((c_\ell,p_\ell)\), so \(H^j\) is killed while higher cohomology remains zero. Finiteness of lower cohomology is preserved by the same long exact sequence. Continuing indefinitely to the left gives a chain map \(P\to C\), with each \(P^j\) finite free and \(P^j=0\) for \(j>b\). Its cone is acyclic: in any fixed degree, the construction kills the cohomology after finitely many stages, and later stages do not change it. Thus \(P\to C\) is a quasi-isomorphism.

We need a tensor fact about its cone. An acyclic bounded-above complex \(T\) of flat modules remains acyclic after every tensor product. At its last nonzero degree, the preceding differential surjects onto the last term. The kernel is flat, because a kernel between flat middle and flat quotient modules is flat. Repeating downward shows all cycle modules are flat and every sequence
\[
0\to Z^i(T)\to T^i\to Z^{i+1}(T)\to0
\]
remains exact under tensor. These tensor sequences imply acyclicity after tensoring. The downward induction reaches any specified degree in finitely many steps even if the complex is unbounded to the left. Applying it to the cone of \(P\to C\) gives
\[
H^i(P\otimes_A M)\cong H^i(C\otimes_A M)=0\quad(i<a)
\]
for every \(M\).

Now put \(Q=\operatorname{coker}(P^{a-1}\to P^a)\). It is finite, and the exact sequence
\[
\cdots\to P^{a-2}\to P^{a-1}\to P^a\to Q\to0
\]
is a free resolution of \(Q\). Exactness uses \(H^i(P)=0\) for \(i<a\). Therefore
\[
\operatorname{Tor}_1^A(Q,M)=H^{a-1}(P\otimes_A M)=0
\]
for all \(M\), since the differential through degree \(a\) is the same in that resolution. Thus \(Q\) is flat. It is finitely presented over Noetherian \(A\), so it is finite projective by the flat-module criterion.

Define \(K^a=Q\), \(K^i=P^i\) for \(a<i\leq b\), and all other terms zero. The map \(P^a\to C^a\) kills the preceding image because \(C^{a-1}=0\); it factors through \(Q\), giving a chain map \(K\to C\). Truncation preserves all cohomology, so this map is a quasi-isomorphism. Its cone is a bounded acyclic complex of flat modules. The tensor fact proves that \(K\otimes M\to C\otimes M\) is a quasi-isomorphism for every \(M\), as required. \(\square\)

The finite replacement does not come from assuming Čech terms are finite, nor from assuming the ring has finite global dimension. Finiteness of the *cohomology* constructs the finite free approximation. Flatness and its bounded range then make the last retained quotient projective.

**Theorem 3.2 (the Grothendieck complex).** Let \(A\) be Noetherian, \(f:X\to\operatorname{Spec}A\) proper, and \(F\) coherent and flat over \(A\). There is a bounded complex \(K\) of finite projective \(A\)-modules, in nonnegative degrees, such that for every \(A\)-algebra \(B\),
\[
H^q(K\otimes_A B)\cong H^q(X_B,F_B),
\]
functorially in \(B\). More generally \(H^q(K\otimes_A M)\cong H^q(X,F\otimes_A M)\) for every \(A\)-module \(M\).

**Proof.** Properness makes \(X\) quasi-compact and separated. Take a finite affine cover with \(r\) members. Its ordered Čech complex \(C\), zero outside \([0,r-1]\), computes \(F\)-cohomology. Every term is \(A\)-flat: for any injection of \(A\)-modules, tensoring the sheaf preserves injectivity at all stalks, and taking sections on an affine intersection preserves exactness of quasi-coherent sheaves. This is the section-module flatness argument already used for high twists in the preceding lesson. Its cohomology is finite by proper finiteness. Apply Lemma 3.1 to obtain \(K\to C\).

Every affine intersection stays affine after a base change. Its section module for \(F_B\) is the original one tensored with \(B\), so the complex after base change is \(C\otimes_A B\). It computes \(H^q(X_B,F_B)\). The universal tensor quasi-isomorphism of Lemma 3.1 identifies its cohomology with that of \(K\otimes_A B\). For an arbitrary module \(M\), the same affine correspondence identifies \(C\otimes_A M\) with the Čech complex of \(F\otimes_A M\). All maps arise from a fixed chain map and affine tensor identifications, so are compatible with homomorphisms of modules and algebras. \(\square\)

In derived language, a bounded complex of finite projective modules represents a **perfect** object. Thus the theorem proves that \(R\Gamma(X,F)\) is perfect and
\[
R\Gamma(X,F)\otimes_A^L B\cong R\Gamma(X_B,F_B)
\]
for every \(B\). This is stronger than flat base change. It does not imply that \(H^q(X,F)\otimes B\to H^q(X_B,F_B)\) is always an isomorphism: taking cohomology of a tensor product is still distinct from tensoring its cohomology. The finite complex makes that distinction computable.

## 4. Euler constancy and explicit models

**Corollary 4.1.** Under Theorem 3.2, the fiber Euler characteristic \(s\mapsto\chi(X_s,F_s)\) is locally constant on \(\operatorname{Spec}A\).

**Proof.** The complex \(K\otimes_A\kappa(s)\) is a finite complex of finite-dimensional vector spaces computing fiber cohomology. Image cancellation gives
\[
\chi(X_s,F_s)=\sum_i(-1)^i\dim_{\kappa(s)}(K^i\otimes_A\kappa(s))
=\sum_i(-1)^i\operatorname{rank}_s K^i.
\]
Each finite projective module has locally constant rank. There are finitely many of them, so their alternating sum is locally constant. \(\square\)

For \(\mathcal O\) on \(\mathbf P^1_A\), use \(K=A[0]\). The projective-space computation gives \(H^0=B\) and all higher cohomology zero for every \(A\)-algebra \(B\). More generally \(\mathcal O(d)\) has the explicit free complex concentrated in degree zero for \(d\geq0\), in degree one for \(d\leq-2\), and the zero complex for \(d=-1\). This includes \(\mathcal O(-2)\) represented by \(A\) in degree one.

For the family of conics \(xy=tz^2\) over \(A=k[t]\), the monic homogeneous equation makes the family flat, as proved in the preceding lesson. Over every \(A\)-algebra \(B\), multiplication by the equation remains injective in the polynomial ring: its leading coefficient is one. The sequence on \(\mathbf P^2_B\)
\[
0\to\mathcal O(-2)\to\mathcal O\to\mathcal O_{\mathcal C_B}\to0
\]
and projective-space cohomology give a Grothendieck complex \(A[0]\) for the structure sheaf. Twisting once replaces \(\mathcal O(-2)\) by \(\mathcal O(-1)\) and \(\mathcal O\) by \(\mathcal O(1)\), giving \(A^3[0]\) for \(\mathcal O_{\mathcal C}(1)\). These computations work on the reducible special fiber as well.

A more revealing example is the rank-two extension on \(\mathbf P^1_{k[t]}\)
\[
0\to\mathcal O(-2)\to E\to\mathcal O\to0
\]
with extension class \(t\). The projective-line calculations and its connecting map give the model
\[
K=[\,A\xrightarrow{t}A\,]\quad\text{in degrees }0,1.
\]
Indeed the cohomology triangle for the extension is the fiber of multiplication by \(t\) between the two copies of \(A\), which is this two-term complex; choosing the generator of \(H^1(\mathcal O(-2))\) fixes that sign. Tensoring with any \(B\) replaces the differential by multiplication by the image of \(t\). Over the original integral ring, \(H^0(E)=0\) and \(H^1(E)=A/(t)\). At the zero fiber the differential is zero and both fiber groups are \(k\). Thus \(\beta^0\) is the map \(0\to k\), while \(\beta^1\) is an isomorphism. The Euler characteristic is zero everywhere. Retaining the differential recovers the missing fiber sections.

## 5. Exercises with solutions

**Exercise 5.1 (easy: affine comparison).** For an affine morphism and an arbitrary change of base, write the degree-zero comparison explicitly and explain the higher-degree statement.

**Solution.** With \(A\to R\), \(A\to B\), and \(M\) an \(R\)-module, the map is \(M\otimes_A B\to M\otimes_R(R\otimes_A B)\), taking \(m\otimes b\) to \(m\otimes(1\otimes b)\). The inverse takes \(m\otimes(r\otimes b)\) to \(rm\otimes b\). Higher source and target sheaves are zero by affine vanishing. Neither flatness of \(M\) nor flatness of \(B\) is needed.

**Exercise 5.2 (easy: flat Čech terms).** Prove flatness over \(A\) of the section modules on affine intersections when \(F\) is flat over \(A\). Identify where separatedness is used in Theorem 3.2.

**Solution.** Every stalk \(F_x\) is flat over its parameter local ring and therefore over \(A\), since localization of \(A\) is flat. Tensoring an injection of \(A\)-modules with \(F\) is thus stalkwise injective. The resulting sheaves are quasi-coherent, and their sections on an affine open form an exact sequence. Hence tensoring the affine section module preserves injections, proving flatness. Separatedness ensures that the finite cover's intersections are affine; without it, the single section complex need not compute higher cohomology.

**Exercise 5.3 (medium: the alternating ranks).** Derive Euler constancy from a Grothendieck complex, and decide whether it forces its cohomology ranks to be locally constant.

**Solution.** On each fiber, boundaries cancel in the alternating dimension sum, leaving the alternating ranks of the finitely many projective terms. Those ranks are locally constant, which proves Euler constancy. Cohomology ranks need not be: for \([A\xrightarrow{t}A]\), both are zero away from \(t=0\) and both are one there. The alternating difference stays zero.

**Exercise 5.4 (medium: the conic hyperplane bundle).** Compute a Grothendieck complex for \(\mathcal O(1)\) on \(xy=tz^2\), and check its behavior under the nonflat base change \(k[t]\to k[t]/(t^2)\).

**Solution.** The twisted hypersurface sequence is \(0\to\mathcal O(-1)\to\mathcal O(1)\to\mathcal O_{\mathcal C}(1)\to0\). On \(\mathbf P^2_B\), \(\mathcal O(-1)\) has no cohomology and \(\mathcal O(1)\) has only \(H^0=B^3\), for every \(B\). The monic equation preserves injectivity even when \(B\) has nilpotents. Thus \(K=A^3[0]\) works, and over \(B=A/(t^2)\) it gives \(B^3\) in degree zero and zero otherwise. This is a genuine arbitrary-base-change calculation, not an application of the flat-base-change theorem.

**Exercise 5.5 (hard: truncate a free approximation).** For a bounded flat complex with finite cohomology over a Noetherian ring, explain why a finite free approximation may have an infinite left tail, and prove that its truncation term at the original lower bound is projective.

**Solution.** Successively killing the cone's top cohomology constructs finite free terms, but new kernel classes can appear one degree lower at each step. The ring need not have finite global dimension, so this process need not stop. Let the original flat complex start in degree \(a\), and let \(P\) be the resulting bounded-above free approximation. Its acyclic flat cone remains acyclic after tensoring, by the cycle induction of Lemma 3.1. Thus \(H^{a-1}(P\otimes M)=0\) for every \(M\). The free tail through \(P^a\) resolves \(Q=\operatorname{coker}(P^{a-1}\to P^a)\), so this equality is \(\operatorname{Tor}_1(Q,M)=0\). It implies flatness of \(Q\); finite generation and Noetherianness give finite presentation, hence projectivity. Replacing the whole left tail by \(Q\) retains the cohomology and universal tensor comparison. This is the complete truncation mechanism, not a finite global-dimension argument.

**Exercise 5.6 (challenging: why the flat-sheaf hypothesis matters).** Take the proper identity map \(X=\operatorname{Spec}k[t]\to\operatorname{Spec}k[t]\) and \(F=\widetilde{k[t]/(t)}\). Show that no bounded finite projective complex can compute its ordinary fiber cohomology for all base changes in the manner of Theorem 3.2, although \(R\Gamma(X,F)\) itself is perfect.

**Solution.** Its fiber is zero away from \(t=0\), and at zero it is \(k\), with no positive cohomology because the fibers are affine. A hypothetical complex would therefore have fiber Euler characteristic zero generically and one at zero. Its alternating term ranks would be locally constant, contradicting connectedness of \(\operatorname{Spec}k[t]\). Meanwhile \(k[t]/(t)\) has the finite free resolution \([A\xrightarrow{t}A]\) in degrees \(-1,0\), so it is perfect. Tensoring that resolution with \(k\) creates a nonzero degree-\(-1\) Tor group. Derived base change remembers this group; ordinary pullback of \(F\) does not. Thus perfectness alone does not remove the need for flatness in the universal ordinary-family comparison.

## References and the next use of the complex

- **[Stacks]** The Stacks project authors, *The Stacks project*, in its AI Integrated Stacks Project edition: affine comparison [Tag 02KG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-affine-base-change); flat comparison [Tag 02KH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-flat-base-change-cohomology); base-change Čech complexes [Tag 01XM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-base-change-complex); proper flat perfect direct images [Tag 07VK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-perfect-direct-image). The construction and finite replacement needed here are proved in Sections 2–3.
- The foundation *[Sheaves of modules and their derived categories](https://kokunoyumeto.github.io/open-math-courses-public/courses/derived-categories-and-sheaf-operations/injective-modules-and-bounded-below-derived-functors.html)*, Sections 8–10, specifies the derived operations. The open adjunction is [Tag 079W](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-lemma-adjoint), using [derived adjoint functors](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-derived-adjoint-functors) and its [general localization proof](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-pre-derived-adjoint-functors-general). Composition of derived pullbacks is [cohomology, lemma-derived-pullback-composition](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-lemma-derived-pullback-composition).
- These open reference texts retain GNU FDL 1.2. This exposition, its finite replacement proof and exercise solutions are independently written CC0.  The next lesson studies ranks of the differentials to prove semicontinuity and the precise criterion for a cohomology base-change map to be an isomorphism.
