# Geometric class field theory

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Draft under mathematical proof repair; full proof closure pending. Public domain (CC0).*

For a rank-one local system, tensoring its fibres over the points of an effective divisor gives a local system on a symmetric power of the curve. Deligne's construction descends it through the Abel–Jacobi map, whose large-degree fibres are projective spaces. Translation then reaches every degree of the Picard scheme. The multiplication and eigen-isomorphisms descend too, with their coherence.

The geometric and arithmetic constructions below are proved relative to the explicitly named geometric and cohomological foundations. Section 9 records every remaining proof obligation. The local categorical theorem also retains its unfinished derived and relative proofs.

Let \(X/k\) be smooth, projective and connected, of genus \(g\), over an algebraically closed field of characteristic zero. A rank-one de Rham local system means a line bundle with integrable algebraic connection. We first work with these unshifted connections and their ordinary tensor product. Over \(\mathbb C\) they also have ordinary topological local-system realizations. The finite-field example uses unshifted lisse \(\overline{\mathbb Q}_\ell\)-sheaves with Weil structure, for \(\ell\ne\operatorname{char}k\).

Write
\[
P=\coprod_{d\in\mathbb Z}P^d,\qquad P^d=\operatorname{Pic}^d_{X/k}.
\]
This is the Picard **scheme**. The Picard stack is
\(\mathcal P=\operatorname{Bun}_{\mathbb G_m}\); its map \(q:\mathcal P\to P\) retains the scalar automorphisms of a line bundle. The family-and-arrow distinction was proved in [Lesson 3](sheaves-and-d-modules-on-bun-g.md). We construct a connection on \(P\), then pull it back to \(\mathcal P\) in the ordinary-local-system normalization.

There are two objects to distinguish. For a local system \(E\), we construct the positive-Abel object \(C_E\), characterized by
\[
\operatorname{AJ}_d^*C_E^d\simeq E^{(d)},\qquad
m^*C_E\simeq C_E\boxtimes C_E .                         \tag{0.1}
\]
Here \(m(L,M)=L\otimes M\). In the downward Hecke convention of [Lesson 4](hecke-functors-and-hecke-eigensheaves.md), \(C_E\) has eigenvalue \(E^{-1}=E^\vee\). The object with eigenvalue \(E\) is
\[
A_E=C_{E^{-1}}.                                        \tag{0.2}
\]
The positive-arrow convention in [Frenkel §4.1](https://arxiv.org/abs/hep-th/0512172) calls \(C_E\) the eigensheaf with eigenvalue \(E\). Formula (0.2) reconciles that convention with this course rather than reversing an arrow halfway through the proof.

## 1. Abel–Jacobi as a projective bundle

For an integer \(d\ge0\), the symmetric power \(X^{(d)}\) parameterizes effective divisors of degree \(d\). Put
\[
\operatorname{AJ}_d:X^{(d)}\longrightarrow P^d,\qquad
D\longmapsto\mathcal O_X(D).
\]
A point \(x_0\in X(k)\) provides a normalized Poincaré line bundle \(\mathcal L_d\) on \(X\times P^d\). Picard representability and this normalization are the background inputs from the Picard-functor prerequisites; the [AI Integrated Stacks Project Picard chapter](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pic.html) retains Tags 0B92, 0B9K and 0B9Z.

**Proposition 1.1.** If \(d\ge0\) and \(d>2g-2\), then \(\operatorname{AJ}_d\) is the projective bundle of lines in a vector bundle of rank \(d+1-g\). Its fibres are \(\mathbb P^{d-g}\).

**Proof.** For a degree-\(d\) line bundle \(L\), Serre duality gives
\[
H^1(X,L)=H^0(X,\omega_X\otimes L^{-1})^\vee=0,
\]
since the latter line has negative degree \(2g-2-d\). Riemann–Roch then gives \(h^0(X,L)=d+1-g\). This rank is positive under the stated conditions, including \(g=0,d=0\).

Let \(p:X\times P^d\to P^d\). Cohomology and base change, applied to the Poincaré family and the vanishing just proved, make
\[
\mathcal V_d=p_*\mathcal L_d
\]
locally free of that rank, with fibre \(H^0(X,L)\). A nonzero section of \(L\), up to nonzero scalar, has an effective zero divisor \(D\) with \(L\simeq\mathcal O(D)\). Conversely such a divisor gives its canonical section and hence a line in \(H^0(X,L)\).

This works on families. A line subbundle of the pullback of \(\mathcal V_d\) gives a section of \(\mathcal L_d\) tensored with a base line; its restriction is nonzero on every fibre. Its zero scheme is a relative effective Cartier divisor of degree \(d\). Conversely the canonical section of a relative divisor gives that line of sections, unaffected by tensoring the representing line bundle with a base line. The two constructions commute with base change and are inverse. Thus
\[
X^{(d)}\simeq\mathbb P_{\mathrm{lines}}(\mathcal V_d)
\]
over \(P^d\), proving the assertion on schemes, not only on closed points. \(\square\)

We use the line convention for projectivization; with a convention parameterizing quotient lines the same space is written using \(\mathcal V_d^\vee\). The Riemann–Roch and duality inputs are [Tag 0B5B](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#section-Riemann-Roch) and the [duality section](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#section-duality), already consulted in Lesson 2.

For every subsequent descent choose
\[
d\ge d_0:=\max(0,2g-1).                                \tag{1.1}
\]
The qualification \(d\ge0\) matters in genus zero: \(X^{(-1)}\) is not a symmetric power used here. Below the bound, the fibres can have different dimensions or be empty. For example on an elliptic curve \(h^0(\mathcal O)=1\), whereas a nontrivial degree-zero line has no sections. We do not assume that every small-degree fibre jumps in every genus.

## 2. Symmetric powers of a rank-one local system

Let \(\pi_d:X^d\to X^{(d)}\) be the finite quotient. The ordinary permutation action on \(E^{\boxtimes d}\) gives
\[
E^{(d)}=(\pi_{d,*}E^{\boxtimes d})^{S_d},\qquad
E^{(0)}=k.                                            \tag{2.1}
\]
For de Rham connections, (2.1) denotes descent of the equivariant line with connection; the sheaf notation is its topological counterpart. We do not take symmetric invariants after a perverse shift: the factors here are lines in degree zero.

**Lemma 2.1.** The descent in (2.1) is a rank-one local system everywhere, including divisors with repeated points. Addition of divisors gives canonical isomorphisms
\[
a_{r,s}^*E^{(r+s)}\simeq E^{(r)}\boxtimes E^{(s)},
\qquad a_{r,s}(D,D')=D+D',                             \tag{2.2}
\]
which are associative, symmetric and unital.

**Proof.** At \(D=\sum_i n_i x_i\), the stabilizer permutes the \(n_i\) identical one-dimensional fibres. Its action on their ordinary tensor product is trivial, and the descended fibre is
\[
E^{(d)}_D=\bigotimes_i E_{x_i}^{\otimes n_i}.           \tag{2.3}
\]
Over \(\mathbb C\), take disjoint discs about the \(x_i\) trivializing \(E\). The corresponding neighbourhood in the symmetric power is a product of symmetric powers of discs. Elementary symmetric coordinates make these smooth polydiscs; invariant tensors of the trivial line give a constant line there. This proves local-system lissity across the diagonals.

Here is a global algebraic construction of the underlying line. Let \(u:\mathcal D_d\to X^{(d)}\) be the universal degree-\(d\) divisor, a finite flat map, and let \(\mathcal L\) be the underlying line of \(E\), restricted to \(\mathcal D_d\). Its norm line is
\[
\det(u_*\mathcal L)\otimes\det(u_*\mathcal O_{\mathcal D_d})^{-1}.
\]
For a repeated divisor, the length filtration has graded factors \(E_{x_i}\) tensored with powers of the cotangent line. The cotangent factors cancel against the denominator, yielding (2.3). The two determinant permutation signs cancel too, giving the ordinary rank-one symmetry.

For the connection check, trivialize \(E\)'s underlying line near each \(x_i\). The norm frame is the product frame. On the distinct-point locus the connection descends by finite étale descent. Its form for a cluster of \(n\) points is
\[
\sum_{j=1}^n f(t_j)\,dt_j
\]
in completed local coordinates. Characteristic zero supplies a formal primitive \(F(t)\) of \(f(t)\). The symmetric formal series \(\sum_jF(t_j)\) is a formal series in the elementary symmetric coordinates. Its differential is therefore a regular form on the completed symmetric quotient. The generically descended algebraic form has no pole at the diagonals: regularity can be checked in these faithfully flat completed local rings. It extends as an algebraic connection on the descended line. Its curvature is zero because its pullback is zero on the dense distinct-point locus. This proves the de Rham statement over \(k\).

Grouping tensor factors defines (2.2). In a product frame, the two sides have the same frame and the same connection form, including on a repeated-point cluster. Thus the grouping map extends across collisions. Regrouping three sets of factors gives exactly the same map as grouping them at once; permutations give the ordinary symmetry, and the empty tensor gives the unit. This proves all stated compatibilities. \(\square\)

The trivial stabilizer action is specific to rank one with this symmetry. For an arbitrary higher-rank tensor, a repeated-point stabilizer need not act trivially, so the same invariant construction need not give a local system of constant rank on the symmetric power.

### 2.2. Lissity at collisions in the étale setting

In positive characteristic we use a finite-coefficient argument. We use the actual finite-pushforward and strict-local-factor arguments in AG-ET-07, §§3–4, not general proper base change.

Let \(E_a\) be a rank-one lisse \(O/\varpi^a\)-sheaf on a smooth curve over an algebraically closed field. For the finite symmetric quotient \(\pi:X^d\to X^{(d)}\), put

\[
E_a^{(d)}=(\pi_*E_a^{\boxtimes d})^{S_d}.
\]

Fix \(D=\sum_i n_i x_i\), and let \(R\) be its strict local ring in the symmetric power. The finite algebra of \(X^d_R\) is a product of strictly henselian local factors by AG-ET-07, Lemma 3.2 and Theorem 3.3. Their closed points are the orderings of the multiset underlying \(D\). On the local factor corresponding to one ordering, all the pullbacks of \(E_a\) are constant. Choose a frame in \(E_{a,x_i}\) once for each support point; strict-local lifting extends each frame uniquely to the corresponding pullback sheaf on every factor. Their tensor product gives a frame of \(E_a^{\boxtimes d}\). The stabilizer \(\prod_iS_{n_i}\) fixes that frame: it only permutes identical frames in an ordinary unshifted rank-one tensor product. The frames on all factors are therefore \(S_d\)-equivariant, so identify this sheaf on \(X^d_R\) with the constant rank-one module with its trivial coefficient action.

For completeness, \((\pi_*\underline M)^{S_d}=\underline M\) on this strict local base. This can be checked on every geometric stalk using AG-ET-07, Theorem 4.1: it is the invariants of the product of copies of \(M\) indexed by the fibre's ordered tuples. The permutation group acts transitively on that set, so its invariants are the diagonal copy of \(M\). Invariants here are a finite equalizer, hence commute with stalks. The diagonal map is consequently an isomorphism of sheaves. Base change to the strict local base is legitimate by AG-ET-07, Corollary 4.2, and preservation of finite limits by inverse image. No division by \(d!\) is used.

These finite frames and their equivariance equations spread to an étale neighbourhood of \(D\): the finite covers representing their frame torsors, sections, and equalities are finitely presented; only finitely many factors and permutations occur. Thus \(E_a^{(d)}\) is a lisse rank-one module across collisions. The same local frame argument proves compatibility with coefficient reduction; the \(E_a^{(d)}\) form a strict lisse system. It also gives canonically

\[
E^{(d)}_D=\bigotimes_i E_{x_i}^{\otimes n_i},\qquad
\operatorname{add}_{r,s}^*E^{(r+s)}=E^{(r)}\boxtimes E^{(s)},
\]

with the ordinary symmetric associativity and unit. The construction is functorial, so a Weil comparison descends as well. The finite symmetric quotient, its geometric orbit fibres and its base change under étale maps remain geometric prerequisites to certify; this argument supplies the local-system proof, not a construction of that quotient scheme.

## 3. Descent through a projective bundle

Deligne's argument uses that a projective-space fibre has no rank-one monodromy. We give a connection proof of the relative descent, including its full faithfulness.

**Lemma 3.1.** Let \(p:Z=\mathbb P_{\mathrm{lines}}(V)\to B\) be a projective bundle of positive rank over a smooth \(k\)-scheme. Every line bundle with flat connection on \(Z\) is the pullback of a unique such line on \(B\), up to the unique isomorphism compatible with its pullback identification. Pullback is fully faithful on these connections and their morphisms.

**Proof.** First a flat line on \(\mathbb P^r\) is trivial. For \(r\ge1\), its underlying line is \(\mathcal O(m)\). Restrict to a projective line. Connection forms on its two affine charts differ by \(m\,dt/t\), from the transition \(t^m\). A form regular on the first chart has powers \(t^jdt\) with \(j\ge0\); one regular on the other has powers with \(j\le-2\). Their difference has no \(t^{-1}dt\) coefficient, so \(m=0\) in characteristic zero. The connection on the trivial line is then the standard one, since \(H^0(\mathbb P^r,\Omega^1)=0\); this last vanishing also follows from the Euler sequence. For \(r=0\) the claim is the statement for a point.

Let \(M\) be the underlying line on \(Z\). It is trivial on every fibre. Cohomology and base change give a line \(N=p_*M\), and the evaluation map \(p^*N\to M\) is an isomorphism: it is an isomorphism on every fibre. The identities \(p_*\mathcal O_Z=\mathcal O_B\) and \(p_*\Omega^1_{Z/B}=0\), together with
\[
0\to p^*\Omega^1_B\to\Omega^1_Z\to\Omega^1_{Z/B}\to0,
\]
give \(p_*\Omega^1_Z=\Omega^1_B\). The projection formula now identifies \(p_*(M\otimes\Omega^1_Z)\) with \(N\otimes\Omega^1_B\). Push the connection on \(M\) through this identification. It satisfies the Leibniz rule, hence defines a connection on \(N\). Its pullback is the original connection: locally the evaluation isomorphism is generated by the base sections used to define the pushed connection, and the Leibniz rule handles their multiples. Its curvature vanishes after this faithfully flat pullback and therefore vanishes on \(B\).

Finally, a bundle map between two pullbacks descends uniquely because \(p_*\mathcal O_Z=\mathcal O_B\). It is horizontal if and only if its pullback is horizontal. This proves full faithfulness and the specified uniqueness. \(\square\)

Apply Lemma 3.1 to Proposition 1.1 and Lemma 2.1. For \(d\ge d_0\), it gives a rank-one connection \(C_E^d\) with a specified identification
\[
\operatorname{AJ}_d^*C_E^d\simeq E^{(d)}.               \tag{3.1}
\]
In the Betti formulation, a projective bundle is locally topologically trivial and its fibre \(\mathbb P^r(\mathbb C)\) is connected and simply connected. Its homotopy exact sequence identifies the two fundamental groups and yields the same descent. For the étale formulation we now prove relative descent directly, using finite covers and coherent cohomology.

### 3.2. Finite covers, local systems and the fibre functor

The finite-cover descent below and the arithmetic representation statement use two categorical comparisons. We prove both here on a Noetherian scheme \(Z\); for the profinite comparison \(Z\) is also nonempty and connected and a geometric point is fixed. In this subsection only, write that base as \(X\). This covers the finite-type curves and Picard components occurring in the arithmetic construction. It imposes no normality, smoothness, properness or characteristic hypothesis. A general connected non-Noetherian base is outside this proof.

A finite cover may be empty; a connected pointed cover is nonempty. All covers and algebras lie in a fixed universe. We use the earlier definition of étale as finitely presented and formally étale, with unique lifts through square-zero ideals. The exact earlier algebra and scheme arguments invoked below are supporting proofs whose remaining transitive foundations are recorded in §9; this subsection does not declare that recursive chain complete.

#### 3.2.1. A finite algebra criterion, including nilpotent bases

On a Noetherian affine base \(\operatorname{Spec}R\), a finite \(R\)-algebra \(B\) is finite étale if and only if its underlying module is finite projective and every geometric fibre is a product of copies of its algebraically closed field.

For the forward implication, an étale algebra is flat by the actual proof of AG-CA-18, Theorem 5.1 and Corollary 6.2, or its arbitrary-base Theorem 6.1. A finite module over Noetherian \(R\) is finitely presented. The finite-presentation-and-flatness argument recalled and proved in AG-DFG-02, Proposition 3.1, makes it finite locally free, hence finite projective.

Here is a direct finite-dimensional argument for its geometric fibres. Let \(C\) be a finite-dimensional formally étale algebra over an algebraically closed field \(K\). The actual Artinian structure proof in AG-CA-03, Lemma 4.1 and Theorem 4.2, gives a product of local Artinian factors. Each residue field is a finite extension of \(K\), hence \(K\), and each maximal ideal is nilpotent. Formal étaleness passes to a direct factor: a lifting problem for that factor is a lifting problem for the product, with the other coordinate idempotents sent to zero. For a local factor, both the identity map and the composite
\[
C\longrightarrow C/\mathfrak m=K\longrightarrow C
\]
lift the same map to \(C/\mathfrak m\). Unique lifting through a nilpotent ideal, obtained by successive square-zero quotients, makes them equal. Thus the factor is \(K\). This proves the fibre assertion without using the general classification of étale algebras over a field.

For the converse, we construct a splitting cover and verify formal étaleness. Define
\[
\tau(b)=\operatorname{Tr}_R(m_b),\qquad
m_b:B\to B,\quad z\mapsto bz.
\]
Trace commutes with base change, by a local matrix calculation. On a geometric fibre \(K^d\), the pairing \((b,c)\mapsto\tau(bc)\) is the standard diagonal pairing. The resulting map \(B\to B^\vee\) is therefore an isomorphism: on each free chart its determinant is nonzero in every residue field, so is a unit. This argument works over nonreduced \(R\).

Let \(e\in B\otimes_RB\) be the tensor corresponding to the identity endomorphism of \(B\) under
\[
B\otimes_RB \longrightarrow \operatorname{End}_R(B),\qquad
c\otimes d\longmapsto [z\mapsto c\tau(dz)].
\]
In a local basis with trace-dual basis, \(e=\sum_i b_i\otimes b_i^*\). For \(b\in B\),
\[
(b\otimes1)e=(1\otimes b)e,
\qquad \mu(e)=1,
\]
where \(\mu\) is multiplication. The first equality follows because both tensors represent multiplication by \(b\). For the second, compute
\[
\tau(b\mu(e))=\sum_i\tau(bb_i b_i^*)
=\operatorname{Tr}_R(m_b)=\tau(b)
\]
and use the perfect pairing. This is an equality in \(R\), not merely an equality on reduced fibres.

These identities give \(e^2=e\). They also give
\[
\ker\mu=(1-e)(B\otimes_RB),\qquad
e(B\otimes_RB)\xrightarrow[\mu]{\sim} B,
\]
with inverse \(b\mapsto(1\otimes b)e\): for any tensor \(z\), one has \(ze=(1\otimes\mu(z))e\). Consequently the diagonal of \(\operatorname{Spec}B\) over \(\operatorname{Spec}R\) is an open-and-closed direct factor of its square.

Tensor products and direct factors of finite projective algebras with split geometric fibres have the same property. Thus, on a rank-\(d\) locus, remove all pairwise diagonals from the \(d\)-fold fibre product of \(Y=\operatorname{Spec}B\). The resulting ordering scheme \(O(Y)\) is a direct-factor finite projective algebra with geometric fibres the \(d!\) orderings of the \(d\)-element fibre. For \(d=0\), set \(O(Y)=X\). For \(d>0\), its positive constant rank makes \(O(Y)\to X\) faithfully flat. Indeed flatness preserves any nonzero cyclic submodule \(R/I\), and a fibre over a maximal ideal containing \(I\) shows that its tensor product is nonzero. This is the faithful-flatness argument actually written in AG-DFG-02, Example 4.2.

Over \(O(Y)\), the \(d\) tautological sections give
\[
\coprod_{i=1}^d O(Y)\xrightarrow{\sim}Y_{O(Y)}.
\]
It is an isomorphism because on every geometric fibre it is the ordering bijection; the corresponding map between finite locally free modules of equal rank is invertible by its local determinant.

Write \(R\to A\) for an affine ordering cover. To prove that \(B\) is formally étale, take an \(R\)-algebra \(C\) and a square-zero ideal \(I\subset C\). After the faithfully flat extension \(C\to C\otimes_RA\), a map \(B\to C/I\) becomes a map from \(A^d\) to \((C\otimes_RA)/(I\otimes_RA)\). Such maps are complete orthogonal families of idempotents. They lift uniquely. Explicitly, if \(a^2-a=r\in I\), then \(u=2a-1\) has \(u^2=1+4r\) and is a unit, and
\[
a-u^{-1}r
\]
is an idempotent lifting \(a\bmod I\). Two idempotent lifts \(e,f\) satisfy \((e+f-1)(e-f)=0\); the first factor is a unit since its reduction has square one. Products of distinct lifted idempotents and their sum are forced to be zero and one by the same uniqueness. No division by \(2\) or by \(d!\) occurs.

On the double scalar extension the two lifted algebra maps agree, by this same uniqueness. The faithfully flat ring equalizer of AG-DFG-02, Theorem 1.3, descends their values to a unique \(R\)-algebra map \(B\to C\). Multiplication and the unit descend because their equations hold after an injective faithfully flat extension. This proves formal étaleness. Finite presentation as an algebra follows from Noetherianity and the Hilbert basis proof in AG-CA-03, Theorem 2.1. Thus \(B\) is étale by the stated definition, completing the criterion. Applying this now-proved criterion to the ordering algebra itself shows that the faithfully flat ordering cover is finite étale. Its étaleness was not assumed in the lifting argument.

#### 3.2.2. Finite étale algebras descend effectively

For a faithfully flat map \(R\to A\), use the actual invariant-module construction of AG-DFG-02, Theorem 2.5. In its convention a datum on an \(A\)-module \(N\) has
\[
\rho:N\to A\otimes_RN,\qquad
M=\{n:\rho(n)=1\otimes n\}.
\]
The cocycle gives
\[
(\operatorname{id}_A\otimes\rho)\rho(n)
=(\operatorname{id}_A\otimes\eta)\rho(n),\qquad
\mu\rho(n)=n.
\]
Flatness identifies \(A\otimes_RM\) with the relevant kernel. These identities make the multiplication map \(A\otimes_RM\to N\) inverse to the factorization of \(\rho\) through that kernel. For the canonical datum, the Amitsur equalizer recovers the original \(M\). The same calculation descends all maps.

If \(N\) is an algebra and the datum consists of algebra maps, the invariant module is closed under multiplication and contains its unit. Hence it is a descended algebra. Algebra maps descend and retain their identities by faithful flatness. Proposition 3.1 of that lesson proves descent of finite presentation and flatness, and thus of finite local freeness; its proof is written for arbitrary faithfully flat ring maps.

For finite étale \(N\), the descended finite locally free algebra \(M\) has split geometric fibres. At a geometric point of the base, choose a geometric point above it on the surjective cover, possibly over a larger algebraically closed field. There its scalar extension is a product of fields. A nilpotent in the original finite-dimensional geometric-fibre algebra would remain a nilpotent after this injective field extension, so it is zero. An algebraically closed field admits no nontrivial finite residue extension. The Artinian structure argument therefore gives a product of copies of that original field. The criterion 3.2.1 now proves that \(M\) is finite étale. This fills the property-descent assertion instead of importing “étaleness descends.”

On schemes, perform the same construction on standard affine refinements of an fpqc cover, and use AG-DFG-02, Theorem 5.1 and §7 to glue its quasi-coherent algebras and their maps. AG-MO-05, Theorem 1.1, constructs their relative spectra and proves base-change compatibility. Thus finite étale schemes, their morphisms and their algebra operations satisfy effective fpqc descent. General nonaffine scheme-valued effectivity is not needed.

#### 3.2.3. Étale covering families are adequate descent covers

We need this fact because a locally constant sheaf is trivialized by an étale family, which need not consist of finite covers. It would be incorrect to replace an arbitrary étale family by a global finite étale cover at this stage.

An étale map is flat and locally of finite presentation, by AG-FSE-04, Lemma 1.1. Its images of open subsets are open, by AG-FSE-01, Theorem 3.2. Its actual proof uses flat lifting of generizations, the constructible-topology Lemma 3.1, and Chevalley. At the Noetherian generality needed here, the exact Chevalley argument is AG-MO-06, Lemma 4.1 and Theorem 4.2: Noether normalization and denominator clearing supply a dense open in a dominant image, and finite irreducible decomposition plus Noetherian induction supplies constructibility.

For each affine open \(W\subset X\), take affine opens of the covering schemes mapping into \(W\). Their open images cover \(W\). Quasi-compactness selects finitely many. Their disjoint union is affine, flat and surjective over \(W\), and hence its ring map is faithfully flat. This is exactly the standard fpqc refinement of AG-DFG-02, §4. Therefore 3.2.2 applies to every étale trivializing family used below. These exact earlier arguments have been read; no planned openness lesson is being substituted.

#### 3.2.4. Finite locally constant sheaves

**Theorem 3.A.** On the small étale site of a Noetherian \(X\), the functor
\[
Y\longmapsto h_Y,\qquad
h_Y(U)=\operatorname{Hom}_X(U,Y),
\]
is an equivalence between finite étale \(X\)-schemes and finite locally constant sheaves of sets.

First, \(h_Y\) is a sheaf. Morphisms of schemes satisfy fpqc gluing by the explicit coefficient-equalizer and quotient-topology proof of AG-DFG-02, Theorem 6.2, and 3.2.3 applies this to étale covers. Over an ordering cover from 3.2.1, \(Y\) is a finite disjoint union of copies of the base. Such a union represents the constant sheaf: a map to it is an open-and-closed partition of its source into the finite labels, and every partition is locally a constant label. Conversely local labels glue to that partition. This is the associated-sheaf condition for the constant presheaf. Thus \(h_Y\) is finite locally constant. The rank loci are open and closed; on a Noetherian \(X\) only finitely many occur, so the construction applies to all ranks, including zero.

Conversely, let \(\mathcal F\) be finite locally constant. On a trivializing étale family \(U_a\to X\), choose finite sets \(S_a\) and isomorphisms
\[
\mathcal F|_{U_a}\simeq h_{\coprod_{S_a}U_a}.
\]
On \(U_a\times_XU_b\), these identifications give an isomorphism of represented sheaves. Yoneda on that small étale site gives the unique corresponding isomorphism of the representing finite étale schemes. The triple-overlap cocycle holds because it holds for the sheaf identifications, and Yoneda is faithful. 3.2.2–3.2.3 descend the finite étale algebras effectively. Their relative spectrum is a finite étale \(Y\to X\). Its local identifications with \(\mathcal F\) have the prescribed cocycle, so give \(h_Y\simeq\mathcal F\).

Both \(Y\) and \(Z\) are objects of the small étale site of \(X\). Yoneda therefore identifies every sheaf map \(h_Y\to h_Z\) with a unique \(X\)-morphism \(Y\to Z\). This proves full faithfulness and the equivalence.

For completeness, the stalk of \(h_Y\) at \(\bar x\) is the geometric fibre \(Y(\Omega)\). A point \(\bar y\) over \(\bar x\) is represented by the pointed étale neighbourhood \((Y,\bar y)\) and its identity section. If two germs have the same fibre point, put their representatives on their pointed fibre product. The equalizer of their sections is the pullback of the open diagonal of \(Y\); it contains the selected point, so is a further pointed neighbourhood where the sections agree. This proves both directions of the stalk identification. Neither strict henselization nor an “enough points” theorem is used to obtain 3.A.

#### 3.2.5. Connected covers and Galois closures

Assume henceforth that \(X\) is nonempty and connected.

A finite étale \(X\)-scheme is Noetherian: on each affine chart its finite algebra is a finite-type algebra over a Noetherian ring, hence Noetherian by AG-CA-03, Theorem 2.1; finitely many such inverse-image charts cover it. Its topology is Noetherian by AG-SS-08, Theorem 3.2.

A Noetherian space has finitely many irreducible components. One proves this by taking a minimal closed counterexample: a reducible counterexample is the union of two proper closed subsets, each already having a finite irreducible decomposition. Make a finite graph whose vertices are these components, with edges when they intersect. A connected component of that graph is a connected union of irreducible sets. Different such unions are disjoint closed sets whose finite union is the whole space; each is also open. Hence the scheme has finitely many connected components, all open and closed. Each component of a finite étale scheme is again finite étale over \(X\). Its rank is locally constant; if it is nonempty, connectedness of \(X\) makes the rank positive everywhere, so it surjects onto \(X\).

We will use two elementary consequences of 3.2.1–3.2.2.

1. Every \(X\)-morphism \(Y\to Z\) between finite étale schemes is finite étale. Finiteness itself is elementary: over an affine open \(\operatorname{Spec}R\subset X\), write the two schemes as \(\operatorname{Spec}B,\operatorname{Spec}C\), with both algebras finite over \(R\). The \(R\)-module generators of \(B\) also generate it over \(C\) through the map \(C\to B\); these inverse-image affine charts cover \(Z\). On a common ordering cover, the two schemes split into copies of the base. On the finite open-and-closed partition where the map of labels is fixed, it is the map attached to a finite set map, hence finite étale. 3.2.2 descends the finite-projective algebra condition and its split geometric fibres over the target, proving étaleness before the cover. Its image is open and closed in \(Z\), since the rank of this finite locally free map is locally constant. Thus a morphism between nonempty connected covers is surjective.
2. The equalizer of two maps \(Y\rightrightarrows Z\) is open and closed, as the pullback of the open-and-closed diagonal in 3.2.1. If \(Y\) is connected and the maps agree at one geometric point, the equalizer is all of \(Y\). In particular a pointed map from a connected cover is unique. On arbitrary \(Y\), agreement on the entire fibre at \(\bar x\) also implies equality: the complementary equalizer is finite étale over \(X\), with empty fibre and hence rank zero everywhere. Thus the geometric-fibre functor is faithful.

Call a connected finite étale cover \(P\to X\) **Galois** if, for \(D=\operatorname{Aut}_X(P)\), the natural morphism
\[
D\times P\longrightarrow P\times_XP,\qquad
(\sigma,p)\longmapsto(p,\sigma(p))
\]
is an isomorphism. This definition will be established constructively for the covers we need.

**Lemma 3.B.** Every finite étale \(Y\to X\) is trivialized by a connected finite Galois cover \(P\to X\). Every pointed connected \(Y\) is dominated by a pointed such \(P\).

Let \(d\) be the degree of \(Y\). Its ordering cover \(O(Y)\) has a permutation action of \(S_d\), free and transitive on every geometric fibre. Choose a point of \(O(Y)\) above \(\bar x\), and let \(P\) be its connected component. Let \(H\subset S_d\) be the subgroup preserving \(P\).

For any two points in \(P_{\bar x}\), the unique permutation carrying the first ordering to the second carries \(P\) to a component meeting \(P\), and therefore preserves \(P\). Hence \(H\) acts freely and transitively on \(P_{\bar x}\). In particular \(\deg P=|H|\), by connectedness of \(X\). Its action on any other geometric fibre is free because the action on \(O(Y)\) is free; that fibre also has \(|H|\) points, so it is transitive. The displayed torsor morphism for \(H\) is a bijection on every geometric fibre and hence an isomorphism of finite étale covers, by the matrix criterion in 3.2.1. Any deck automorphism of \(P\) is determined by its value on the chosen point, and \(H\) supplies every such value. Thus \(H=D\) and \(P\) is Galois.

The tautological ordering trivializes \(Y_P\). If \(Y\) is connected and pointed, choose an ordering whose first entry is its selected point. Its first-coordinate map \(P\to Y\) respects the point and is surjective by the preceding consequence 1. Degree zero uses \(P=X\).

The category of pointed connected finite étale covers is cofiltered. The identity cover supplies an object; for two covers take the connected component through their point in their fibre product; parallel pointed arrows already agree by consequence 2. Lemma 3.B makes the pointed Galois covers cofinal. Repeating the product-component construction and then 3.B gives a pointed Galois refinement of any finite collection of pointed Galois covers. Up to pointed isomorphism they form a directed partially ordered set under refinement: pointed maps are unique, and maps in both directions have identity composites by that same uniqueness. A set of representatives exists in our universe, since finite presented algebras on the finitely many affine charts and their overlap maps form a set.

#### 3.2.6. The profinite group and its actions

Index these pointed Galois covers by \(i\), writing \((P_i,p_i)\). If \(j\) refines \(i\), let \(f_{ji}:P_j\to P_i\) be the unique pointed map, and put \(D_i=\operatorname{Aut}_X(P_i)\).

For \(\sigma\in D_j\), there is a unique \(\tau\in D_i\) with
\[
f_{ji}\sigma=\tau f_{ji}.
\]
Indeed choose the unique \(\tau\) sending \(p_i\) to \(f_{ji}(\sigma p_j)\); the two maps agree at \(p_j\), so agree everywhere. This defines a homomorphism \(D_j\to D_i\). It is surjective: the map of finite covers \(f_{ji}\) is surjective, hence surjective on geometric fibres, and \(D_j\) acts regularly on its fibre. Uniqueness also proves compatibility for successive refinements.

To keep left-action conventions explicit, put \(G_i=D_i^{\mathrm{op}}\). The same transition maps are surjective homomorphisms between these opposite groups. We regard \(P_i\) as a right \(G_i\)-torsor by
\[
p\cdot\sigma^{\mathrm{op}}=\sigma(p),
\qquad
\sigma^{\mathrm{op}}\tau^{\mathrm{op}}=(\tau\sigma)^{\mathrm{op}}.
\]
Define
\[
\pi=\varprojlim_i G_i.
\]
It is a compact Hausdorff profinite group, and every projection \(\pi\to G_i\) is onto. Here is the finite-set compactness step explicitly. The compatibility conditions in the product of the finite \(G_i\) have the finite intersection property: for finitely many indices choose a common refinement, an element there, and its images. To prescribe an element at a fixed index, choose its preimage at the common refinement by surjectivity. Extend the resulting filter to an ultrafilter by Zorn's lemma. In each finite coordinate partition exactly one cell belongs to that ultrafilter. Its chosen coordinate values satisfy all the compatibility conditions, proving existence and the projection assertion. The same ultrafilter argument proves compactness of a product of finite discrete spaces; the compatible locus is closed. Its Hausdorff topology and continuous coordinatewise group operations are inherited from that product. This is also the exact written compactness argument preceding AG-ET-02, Theorem 7.2.

If \(P_i\) trivializes \(Y\), evaluation at \(p_i\) is a bijection
\[
\operatorname{Hom}_X(P_i,Y)\xrightarrow{\sim}Y_{\bar x}.
\]
Indeed a section of the split \(Y_{P_i}\) chooses a locally constant label, and \(P_i\) is connected, so the label is constant. For \(y\in Y_{\bar x}\), write \(s_y\) for this map. Define a left \(G_i\)-action by
\[
\sigma^{\mathrm{op}}\cdot y=(s_y\circ\sigma)(p_i).
\]
Precomposition reverses composition, so the opposite-group convention makes this exactly a left action. A refinement satisfies \(f_{ji}\sigma=\tau f_{ji}\), so gives the same action after its transition homomorphism. A common refinement proves independence of the splitting cover. Hence every \(Y_{\bar x}\) has a continuous left \(\pi\)-action, and every \(X\)-morphism induces an equivariant map.

**Theorem 3.C.** The geometric-fibre functor is an equivalence
\[
\mathrm{F\acute Et}_X
 \xrightarrow{\sim}
\{\text{finite continuous left }\pi\text{-sets}\}.
\]

For full faithfulness, choose one \(P_i\) trivializing both \(Y\) and \(Z\). Over this connected cover, a map between the two split schemes is exactly a function \(Y_{\bar x}\to Z_{\bar x}\). It descends precisely when it respects the descent data on
\[
P_i\times_XP_i\simeq P_i\times G_i.
\]
In the right-torsor convention, the descent relation is
\[
(p\cdot g,s)\sim(p,g\cdot s).
\]
A function respects it precisely when it is \(G_i\)-equivariant. Effectivity and full faithfulness of algebra descent in 3.2.2 prove existence and uniqueness of the descended morphism. Since \(\pi\to G_i\) is onto, \(G_i\)-equivariance is the same as \(\pi\)-equivariance. This proves the Hom comparison.

For essential surjectivity, let \(S\) be a finite continuous \(\pi\)-set. The kernel of its action is open: it is the intersection of finitely many open stabilizers. A basic neighbourhood of the identity in this inverse-limit topology imposes conditions at finitely many coordinates. Choose one common refining index \(i\). Then \(\ker(\pi\to G_i)\) is contained in the action kernel, and surjectivity of the projection gives a well-defined \(G_i\)-action on \(S\).

Over the right \(G_i\)-torsor \(P_i\), start with \(\coprod_S P_i\), or its finite product algebra \(\mathcal O_{P_i}^{S}\). Give it the datum \((p\cdot g,s)\sim(p,g\cdot s)\). On triples its cocycle is the group-action law; with \((p,p\cdot g,p\cdot gh)\), the two successive comparisons agree with the direct one. 3.2.2 descends this finite étale algebra, producing \(Y\to X\). At \(p_i\) its fibre is canonically \(S\), and the action constructed above is the given action: the section with constant label \(s\), evaluated at \(p_i\cdot g\), represents \([p_i,g\cdot s]\). Thus its geometric fibre recovers \(S\). This completes the equivalence.

Under this equivalence, \(Y\) is connected if and only if \(\pi\) acts transitively on \(Y_{\bar x}\). For a connected \(Y\), choose a pointed Galois cover \(P_i\to Y\). It is surjective on fibres. Deck transformations are transitive on the fibre of \(P_i\), so their images under the first-coordinate section give the full orbit of the selected point of \(Y_{\bar x}\). Conversely an invariant proper subset of a finite \(\pi\)-set descends by the same product-algebra construction to an open-and-closed subcover. Decomposing into orbits gives the connected-component decomposition. This proves the orbit assertion rather than importing it as a Galois-category axiom.

#### 3.2.7. This group is the automorphism group of the fibre functor

Let \(F(Y)=Y_{\bar x}\), and endow \(\operatorname{Aut}(F)\) with the topology of pointwise agreement on the finite fibres. The actions above define a homomorphism \(\pi\to\operatorname{Aut}(F)\).

It is injective: if an element acts trivially on every \(F(P_i)\), it fixes \(p_i\), so its \(G_i\)-coordinate is the identity by the regular deck action.

Let \(\theta\) be any natural automorphism of \(F\). Choose the unique \(\sigma_i\in D_i\) with
\[
\theta_{P_i}(p_i)=\sigma_i(p_i).
\]
Naturality with the pointed transition maps implies \(f_{ji}\sigma_j=\sigma_i f_{ji}\), first at the selected point and then everywhere by connectedness. Hence the \(\sigma_i^{\mathrm{op}}\) are a compatible element of \(\pi\). For \(y\in F(Y)\), choose a splitting \(P_i\) and its section \(s_y\). Naturality gives
\[
\theta_Y(y)=F(s_y)(\theta_{P_i}(p_i))
=s_y(\sigma_i p_i),
\]
which is exactly the already defined \(\pi\)-action. Thus every natural automorphism arises.

Composition has the opposite convention asserted above: naturality with the deck map \(\tau_i\) gives
\[
(\theta_\sigma\theta_\tau)_{P_i}(p_i)
=\tau_i\sigma_i(p_i).
\]
This corresponds to \(\sigma_i^{\mathrm{op}}\tau_i^{\mathrm{op}}\), so the bijection is an isomorphism of groups. Finally, agreement on \(p_i\) determines agreement on all of \(F(P_i)\), by naturality with deck maps; agreement on that fibre also forces agreement on the fibres of covers it trivializes, by their sections. Thus the finite-fibre topology is exactly the inverse-limit topology. We have proved
\[
\pi\simeq\operatorname{Aut}(F)
\]
as profinite groups. This supplies the definition and the representation comparison claimed for \(\pi_1(X,\bar x)\) in the lesson, rather than citing a separate abstract Galois-category theorem.

#### 3.2.8. Finite and adic coefficients

Combining 3.A and 3.C gives the finite-locally-constant-sheaf comparison with finite continuous \(\pi_1(X,\bar x)\)-sets at this stated Noetherian generality. Finite products are preserved: both are the fibre products of representing schemes, whose geometric fibres are the products of the finite sets.

For a finite ring \(\Lambda\), a finite locally constant sheaf of \(\Lambda\)-modules is a finite locally constant set sheaf with addition, zero, inverse and scalar-operation maps. Full faithfulness transports these maps to its fibre; faithfulness transports their identities in both directions. Thus the comparison is an equivalence with finite \(\Lambda\)-modules with continuous \(\pi_1\)-action, including all module maps. A finitely generated module over a finite ring has a finite underlying set. No unrestricted infinite-coefficient set-sheaf statement is asserted here.

For \(O\) the coefficient ring used in AG-LTF-01 and \(O_n=O/\ell^nO\), apply this finite-ring equivalence at every level. The actual argument of AG-LTF-01, Lemma 1.2, reconstructs a finite \(O\)-module from a strict inverse system: surjectivity lifts elements successively; compact finite solution sets show that the reduction kernel is exactly \(\ell^nM\); lifted generators modulo \(\ell\), successive approximation and compactness show finite generation. Its Proposition 1.3 then proves the adic comparison using exactly the finite-level equivalence proved here. This is a valid provider for the inverse-limit and continuity step; its former fundamental-group dependency is now supplied, rather than assumed.

These comparisons supply the coefficient-level and representation passages in the arithmetic construction at their stated Noetherian scope. Finite-cover and finite-coefficient descent over a locally Noetherian projective-bundle base can be performed on Noetherian affine opens and glued by full faithfulness. We do not assert a global profinite comparison for a connected base without quasi-compactness. No Chebotarev theorem, global class field theorem or averaging by a cover degree occurs in this argument.


### 3.3. Finite étale covers of projective space

We first need only vector-bundle Serre duality on \(\mathbb P^1\), not curve Riemann–Roch or an imported Riemann–Hurwitz formula. Its actual programme proof is AG-QC-14, Corollary 5.2, with \(\omega_{\mathbb P^1}=\mathcal O(-2)\). The monomial trace, presentation argument and dimension shifting are written in that lesson's §§3–5. Coherent projective finiteness and the finite affine-cover comparison are supplied by AG-QC-05, Theorem 2.1 and Corollary 2.3, and AG-QC-04, Theorem 2.2. This only uses the projective case of finiteness: the planned Chow-lemma prerequisite in AG-QC-06 is unnecessary here.

**Lemma 3.2.** Over an algebraically closed field of any characteristic, every finite étale cover of \(\mathbb P^1\) is a disjoint union of copies of \(\mathbb P^1\).

**Proof.** Treat one nonempty connected component \(f:T\to\mathbb P^1\), of degree \(m\geq1\). The curve \(T\) is smooth; its local rings are regular domains, so different irreducible components cannot meet. Connectedness therefore makes it integral. Put \(A=f_*\mathcal O_T\), a vector bundle of rank \(m\). Its trace pairing is perfect. Indeed, after taking an algebraic closure of any residue field, the fibre algebra is a product of copies of that field, and the pairing is \((a_i),(b_i)\mapsto\sum_i a_i b_i\). Thus the trace map \(A\to A^\vee\) is an isomorphism on every fibre and hence an isomorphism of vector bundles. This holds even when the characteristic divides \(m\); the assertion concerns the whole trace pairing, not the scalar \(\operatorname{Tr}(1)=m\).

Projective finiteness makes \(H^0(T,\mathcal O_T)=H^0(\mathbb P^1,A)\) a finite-dimensional domain over the algebraically closed ground field \(k\). It is a finite field extension and consequently equals \(k\). Set \(g=\dim_k H^1(T,\mathcal O_T)\geq0\). Cohomology above degree one vanishes: the inverse images of the two standard affine charts, and their intersection, are affine because \(f\) is finite. Thus \(\chi(\mathcal O_T)=1-g\).

Let \(p\in\mathbb P^1(k)\) and \(D=f^{-1}(p)\). It is a reduced effective Cartier divisor consisting of \(m\) points. Tensoring \(0\to\mathcal O_T(-D)\to\mathcal O_T\to\mathcal O_D\to0\) by any line bundle subtracts \(m\) from its Euler characteristic when twisting by \(-D\): its restriction to \(D\) has \(m\) independent one-dimensional sections and no higher cohomology. Applying this twice gives

\[
\chi(f^*\mathcal O(-2))=\chi(\mathcal O_T)-2m=1-g-2m.
\]

Finite pushforward and the projection formula identify its cohomology with that of \(A(-2)\) on \(\mathbb P^1\). Vector-bundle duality, together with \(A\simeq A^\vee\), gives

\[
h^0(A(-2))=h^1(A)=g,\qquad h^1(A(-2))=h^0(A)=1.
\]

Consequently \(g-1=1-g-2m\), or \(m=1-g\). Since \(m\geq1\) and \(g\geq0\), we obtain \(m=1\) and \(g=0\). A finite étale algebra of rank one is its base ring: its unit is a fibrewise isomorphism and hence a bundle isomorphism. Thus \(f\) is an isomorphism. The connected-component argument proves the lemma. \(\square\)

Here is the relative step, stated with its precise coherent-cohomology requirement before using it to prove the higher-dimensional assertion.

**Lemma 3.3 (relative descent).** Let \(p:Z=\mathbb P_B(V)\to B\), with \(B\) locally Noetherian and \(V\) a vector bundle of positive rank. Suppose all finite étale covers of its geometric projective-space fibres are trivial. Then pullback gives an equivalence of categories of finite étale covers of \(B\) and \(Z\).

**Proof.** A finite étale cover \(Y\to Z\) has a finite locally free algebra \(\mathcal A\) on \(Z\). Since \(p\) is flat, \(\mathcal A\) is flat over \(B\). On a geometric fibre it is the algebra \(\mathcal O^{\oplus m}\), so positive coherent cohomology vanishes and the degree-zero cohomology has dimension \(m\). The projective-space computation is AG-QC-04, Theorem 2.2, with twist zero. Field-extension comparison, AG-QC-08, Theorem 2.1, transfers this vanishing to every ordinary residue-field fibre.

By AG-QC-08, Theorem 3.2, restricted to projective morphisms, and AG-QC-09, Corollary 5.3,

\[
\mathcal B=p_*\mathcal A
\]

is finite locally free and commutes with arbitrary base change. The latter corollary is proved by cancelling invertible differential blocks in the finite projective cohomology complex: at a chosen point the remaining positive-degree terms have ranks equal to the zero fibre cohomology, so are absent. It does not require a reduced base.

The evaluation \(p^*\mathcal B\to\mathcal A\) is a map of algebras. On every geometric fibre it is the evaluation from constant sections of \(\mathcal O^{\oplus m}\), an isomorphism. A map between finite locally free modules which is an isomorphism on all residue fields is an isomorphism, by the local determinant criterion (or a cokernel and Nakayama argument). Hence

\[
p^*\mathcal B\simeq\mathcal A.
\]

The geometric fibres of \(\mathcal B\) are products of copies of their algebraically closed field. The finite-projective algebra criterion proved in §3.2.1, applied on Noetherian affine opens of \(B\), therefore makes \(\operatorname{Spec}_B\mathcal B\to B\) finite étale. Its ordering cover gives the étale local splitting explicitly. This uses neither a separate finite-flat unramified criterion nor strict henselization.

Finally \(p_*\mathcal O_Z=\mathcal O_B\), universally, by the same monomial computation with twist zero. Thus \(p_*p^*\mathcal B=\mathcal B\). Adjunction identifies every map between pulled-back finite locally free algebras with a unique map downstairs, and recovers \(\mathcal B\) from \(\mathcal A\). This proves full faithfulness as well as effectivity. \(\square\)

**Lemma 3.4.** Over an algebraically closed field of any characteristic, every finite étale cover of \(\mathbb P^n\) is trivial, for every \(n\geq0\).

**Proof.** The cases \(n=0,1\) are respectively the field case and Lemma 3.2. For \(n\geq2\), put \(o=[1:0:\cdots:0]\), and let

\[
Z=\{([x_0:\cdots:x_n],[u_1:\cdots:u_n]):x_i u_j=x_j u_i\ (1\leq i,j\leq n)\}
\subset\mathbb P^n\times\mathbb P^{n-1}.
\]

The second projection \(r\) is a \(\mathbb P^1\)-bundle. On \(u_i\ne0\), write \(v_j=u_j/u_i\), with \(v_i=1\); its points are

\[
([a:bv_1:\cdots:bv_n],[v_1:\cdots:v_n]),\qquad [a:b]\in\mathbb P^1.
\]

This gives the local trivializations and their transition maps. The locus \(b=0\) is a section \(s:\mathbb P^{n-1}\to Z\). The first projection \(b:Z\to\mathbb P^n\) is proper and is an isomorphism away from \(o\); this incidence construction is the usual blow-up, but its universal property is not needed.

Pull back a finite étale cover \(Y\to\mathbb P^n\) to \(Z\). Lemma 3.3 already applies to \(r\), since its fibres are \(\mathbb P^1\), whose covers were proved trivial first. It follows that \(Y_Z=r^*W\) for a finite étale cover \(W\) of \(\mathbb P^{n-1}\). Restrict to the section. Since \(b\circ s\) is the constant map to \(o\),

\[
W=s^*Y_Z=Y_o\times\mathbb P^{n-1}.
\]

Thus \(Y_Z\) is a trivial cover. This argument does not assume that \(\mathbb P^{n-1}\) has trivial covers.

We also have \(b_*\mathcal O_Z=\mathcal O_{\mathbb P^n}\). Only the neighbourhood of \(o\) needs checking. On the chart \(x_0\ne0\), put \(R=k[t_1,\ldots,t_n]\). A function on the inverse image of a principal neighbourhood \(D(f)\), \(f(o)\ne0\), restricts to a function on \(D(f)\setminus\{o\}\). Such a function belongs to

\[
\bigcap_{i=1}^n R_f[t_i^{-1}]=R_f
\]

inside its fraction field: in the unique-factorization domain \(R_f\), any denominator would have to divide a power of every \(t_i\); distinct coordinate variables have no common irreducible factor. The extension pulls back to the original function, since the integral scheme \(Z\) has the inverse image of the punctured chart dense. These principal neighbourhoods are a basis, proving the sheaf identity.

For the finite étale algebra \(\mathcal A\) of \(Y\), the trivialization above gives \(b^*\mathcal A\simeq\mathcal O_Z^m\) as algebras. Pushing forward, and using the elementary locally free projection formula and the sheaf identity, gives \(\mathcal A\simeq\mathcal O_{\mathbb P^n}^m\) as algebras. This proves the assertion. \(\square\)

Combining Lemmas 3.3 and 3.4 proves finite étale descent through every projective bundle over a locally Noetherian base, in arbitrary characteristic.

### 3.4. Descent of lisse and Weil lines

Let \(K/\mathbb Q_\ell\) be finite, with ring of integers \(O\), uniformizer \(\varpi\), and \(\ell\) invertible on the schemes. A rank-one lisse \(K\)-sheaf has a stable \(O\)-lattice. Its underlying continuous geometric representation has compact image. The valuation of that image is a compact subgroup of \(\mathbb Z\), hence zero, so in rank one any lattice is stable after choosing a basis. This is also the rank-one case of AG-LTF-01, §4's written stable-lattice argument.

Each reduction modulo \(\varpi^a\) is a finite locally constant rank-one module. Its underlying finite set is represented by a finite étale cover by Theorem 3.A, applied on Noetherian affine base opens. The algebraic descent of Lemmas 3.3–3.4 descends that finite set, every module-operation map, and every identity between those maps. Thus it descends the finite locally constant module and all its morphisms. Full faithfulness descends the transition maps and their reduction identities. The resulting strict inverse system is lisse on \(B\), by the definition in AG-LTF-01, Definition 1.1; its inverse-limit stalk is a free rank-one \(O\)-module by that lesson's Lemma 1.2. Invert \(\varpi\). This proves that

\[
p^*:\operatorname{Loc}_1(B,K)\xrightarrow{\sim}\operatorname{Loc}_1(\mathbb P_B(V),K).
\]

The finite-set descent is an equivalence respecting products; therefore the inverse also respects tensor products, their associativity and units. Coefficient extension commutes with it. A \(\overline{\mathbb Q}_\ell\)-sheaf in the programme is defined over some finite extension, so the same result applies to those sheaves.

When the bundle and its base are defined over \(\mathbb F_q\), apply the equivalence over \(\overline{\mathbb F}_q\). A Frobenius comparison upstairs descends uniquely by full faithfulness, since projective-bundle pullback commutes with Frobenius pullback. Thus pullback is also an equivalence for rank-one lisse **Weil** sheaves. Its Frobenius eigenvalue need not be an \(\ell\)-adic unit: the stable lattice is used for the continuous geometric local system, and the separate Weil comparison is descended after rationalizing coefficients. This proves the arithmetic input needed here without invoking projective-space simple connectedness or proper smooth étale base change.

### 3.5. Descending multiplication and the moving Abel map

The comparison between symmetric addition and tensoring line bundles is the square
\[
\begin{array}{ccc}
X^{(r)}\times X^{(s)}&\xrightarrow{a_{r,s}}&X^{(r+s)}\\
\downarrow{\operatorname{AJ}_r\times\operatorname{AJ}_s}
 &&\downarrow{\operatorname{AJ}_{r+s}}\\
P^r\times P^s&\xrightarrow{m}&P^{r+s}.
\end{array}                                           \tag{3.2}
\]
For \(r,s\ge d_0\), the left vertical map is a product of projective bundles. Pullback along it is fully faithful, by applying Lemma 3.1 successively with the other factor as base. Thus (2.2) descends to
\[
m^*C_E^{r+s}\simeq C_E^r\boxtimes C_E^s.                \tag{3.3}
\]
Likewise adding one moving point descends, using \(\operatorname{AJ}_d\times1_X\), to
\[
h_+^*C_E^{d+1}\simeq C_E^d\boxtimes E,\qquad
h_+(L,x)=L(x),\quad d\ge d_0.                          \tag{3.4}
\]
Associativity, permutations and collision compatibilities descend because fully faithful pullback reflects equality of the maps in question.

## 4. All degrees, multiplicativity and uniqueness

Fix \(x_0\) for the construction, and write \(V_0=E_{x_0}\). For any integer \(d\), choose \(N\ge0\) with \(d+N\ge d_0\). Let
\[
\tau_N:P^d\to P^{d+N},\qquad L\mapsto L(Nx_0).
\]
Define
\[
C_E^d=\tau_N^*C_E^{d+N}\otimes V_0^{-N},               \tag{4.1}
\]
where the negative power denotes the tensor power of the dual line.

**Theorem 4.1 (rank-one geometric class field theory).** For every rank-one de Rham local system \(E\) on \(X\), there is a multiplicative rank-one local system \(C_E\) on \(P\), equipped with a unit \(C_E|_{\mathcal O_X}\simeq k\) and \(\operatorname{AJ}_1^*C_E\simeq E\). It satisfies (3.1) for every \(d\ge0\), and its multiplication, positive Hecke and symmetric-power identifications are coherent. With these specified comparisons, it is unique up to unique isomorphism.

**Proof.** We first check (4.1) rather than assume its independence of \(N\). Formula (3.4) at \(x_0\) identifies
\[
\tau_1^*C_E^{a+1}\simeq C_E^a\otimes V_0
\qquad(a\ge d_0).
\]
Pulling this back by \(\tau_N\) and tensoring with \(V_0^{-(N+1)}\) canonically identifies the definitions using \(N+1\) and \(N\). The identifications for several increments compose to the one obtained by adding all the copies of \(x_0\), by Lemma 2.1. They form a transitive system, so all sufficiently large choices give canonically the same object. For a large \(d\), \(N=0\) recovers (3.1).

To prove the positive Hecke property in every degree, choose \(N\) with \(d+N\ge d_0\). The equality
\[
\tau_N(L(x))=(\tau_N L)(x)
\]
lets us pull (3.4) back from large degree and cancel \(V_0^N\) on both sides. We obtain
\[
h_+^*C_E^{d+1}\simeq C_E^d\boxtimes E
\qquad(d\in\mathbb Z).                                \tag{4.2}
\]
The transition maps in \(N\) respect this identification, since they are all induced by the associative symmetric grouping of the same factors.

For multiplication in degrees \(a,b\), choose \(N,M\ge0\) with \(a+N,b+M\ge d_0\). Since
\[
(\tau_NL)\otimes(\tau_MM)=\tau_{N+M}(L\otimes M),
\]
pulling (3.3) back from these large degrees and cancelling \(V_0^{N+M}\) gives
\[
m^*C_E^{a+b}\simeq C_E^a\boxtimes C_E^b.               \tag{4.3}
\]
Increasing either translating integer gives the same map: before descent, both comparisons group the same divisor factors and the same extra \(x_0\)-factors. This proves that (4.3) is independent of the choices. For three input degrees translate all three high enough. The associativity diagram becomes, under the fully faithful symmetric-power pullback, associativity of grouping tensor factors. It commutes by Lemma 2.1. The same argument proves symmetry and the compatibility with (4.2), including repeated points.

There is a canonical unit. For \(N\ge d_0\), the divisor \(Nx_0\) maps to \(\mathcal O(Nx_0)\), and (3.1) identifies the fibre there with \(V_0^N\). Formula (4.1) consequently identifies \(C_E^0|_{\mathcal O_X}\) with \(V_0^N\otimes V_0^{-N}=k\). This identification is independent of \(N\). The two unit diagrams for (4.3) are the same tensor cancellation; the previous fully faithful checks prove them.

Iterate (4.2), starting at \(\mathcal O_X\) with this unit. At an effective divisor \(D=\sum x_i\) the result is \(C_E|_{\mathcal O(D)}\simeq\bigotimes_iE_{x_i}\), naturally in the divisor. Permutation and collision compatibility show that this is exactly (3.1) in every nonnegative degree, not merely for distinct points. In degree one it gives the required Abel identification.

For uniqueness, let \(B\) have the stated unit, Abel comparison and coherent multiplication. Repeated multiplication pulls \(B^d\) back along \(\operatorname{AJ}_d\) to \(E^{(d)}\). For \(d\ge d_0\), full faithfulness in Lemma 3.1 therefore gives a unique comparison \(B^d\simeq C_E^d\) inducing that specified identification. In any remaining degree, multiplication by \(\mathcal O(Nx_0)\), whose fibre is canonically \(V_0^N\), forces the comparison (4.1). The transitive transition system shows its independence of \(N\). These comparisons respect multiplication and the unit because they do so after translation to large degree and fully faithful pullback. They are consequently a unique multiplicative comparison with the required Abel map. This also proves independence of the point \(x_0\) used in the construction. \(\square\)

Specifying the comparisons is necessary for “unique up to unique isomorphism.” If the Abel comparison is omitted, the multiplication-preserving automorphisms can multiply component \(d\) by \(c^d\), for \(c\in k^\times\). Fixing the Abel comparison forces \(c=1\); then the unit and multiplication force the identity on every component.

The theorem follows Deligne's descent strategy as presented in Frenkel §4.1. Our proof includes the all-degree transition maps, unit, multiplicativity and coherence. In the consulted TeX, the fixed-point formula in that section displays \(h_{x}^*\operatorname{Aut}^d\) with the wrong target degree. A map \(P^d\to P^{d+1}\) pulls back the object of degree \(d+1\). Formulas (3.4) and (4.1) use these degree indices consistently.

## 5. The downward eigensheaf and two curve examples

Let \(\operatorname{inv}:P\to P\) send \(L\) to \(L^{-1}\). The unit and multiplication imply
\[
\operatorname{inv}^*C_E\simeq C_E^\vee:
\]
pull multiplication back along \(L\mapsto(L,L^{-1})\) and use its unit fibre. At a point \(x\), (4.2), applied to \(L(-x)\), therefore gives
\[
C_E|_{L(-x)}\simeq C_E|_L\otimes E_x^{-1}.             \tag{5.1}
\]
The corresponding moving isomorphism is an isomorphism of connections on \(P\times X\). Tensoring by \(\mathcal O(-mx)\) yields \(E^{-m}\) for every integer weight \(m\).

Pull \(A_E=C_{E^{-1}}\) back along \(q:\mathcal P\to P\). In the ordinary-local-system normalization and the half-gerbe trivialization for \(\mathbb G_m\), it is an automorphic object with
\[
H_m(q^*A_E)\simeq
 q^*A_E\boxtimes(E^{\otimes m})^\omega.                \tag{5.2}
\]
The superscript \(\omega\) is precisely Lesson 4's dualizing-normalized curve factor. The fixed-point version uses \(i_x^!\) and has eigenvalue \(E_x^{\otimes m}\). Associativity and symmetry in Theorem 4.1 give the full eigen-coherence. Ordinary rank-one connections were used in the construction; a perverse shift or a change of crystal normalization must be recorded when comparing to another convention.

**Example 5.1: the projective line.** A flat line on \(\mathbb P^1\) has underlying degree zero by the two-chart argument in Lemma 3.1, hence is trivial as a bundle, and its connection is trivial because \(H^0(\Omega^1_{\mathbb P^1})=0\). Thus \(E\) is a constant one-dimensional local system, with fibre \(V\). Each \(P^d\) is a point. The construction gives
\[
C_E^d=V^{\otimes d},\qquad A_E^d=V^{\otimes(-d)}
\quad(d\in\mathbb Z).
\]
For \(d\ge0\), \(X^{(d)}=\mathbb P^d\), its local system is the constant line \(V^d\), and this is its descent. Translation supplies the displayed negative degrees. The downward operator changes \(d\) to \(d-1\); the line \(A_E^{d-1}=A_E^d\otimes V\) verifies its eigenvalue directly.

Over \(\mathbb F_q\), a geometrically constant \(E\) can still have geometric Frobenius \(\alpha\in\overline{\mathbb Q}_\ell^\times\). Its positive-Abel trace is \(\alpha^d\), whereas the downward eigensheaf has trace \(\alpha^{-d}\). Thus \(T_x f(d)=f(d-1)=\alpha f(d)\) at a rational point, exactly the direction checked in Lesson 1. This describes Weil structures; for a continuous étale representation the corresponding eigenvalue must satisfy the continuity condition discussed there.

**Example 5.2: an elliptic curve.** Let \(X\) be an elliptic curve with origin \(0\). Identify
\[
P^d\simeq X,\qquad z\longmapsto\mathcal O_X(z+(d-1)0).
\]
In these coordinates tensor product is \((z,w)\mapsto z+w\), and adding a point \(x\) is \(z\mapsto z+x\). Put \(V=E_0\) and \(\widetilde E=E\otimes V^{-1}\). The theorem makes \(\widetilde E\) a multiplicative local system on \(X\) with unit \(k\). Since \(P^1\simeq X\) by the Abel map, (4.1) gives the fully specified formula
\[
C_E^d\simeq \widetilde E\otimes V^d,\qquad
A_E^d\simeq \widetilde E^\vee\otimes V^{-d}.            \tag{5.3}
\]
For \(X(\mathbb C)=\mathbb C/(\mathbb Z+\tau\mathbb Z)\), a rank-one monodromy is given by two nonzero scalars \(u,v\). The monodromies of \(C_E^d\) are \(u,v\) on every component; those of \(A_E^d\) are \(u^{-1},v^{-1}\). The factor \(V^{\pm d}\) records the canonical fibres across degrees and does not change these loop monodromies.

For a direct check of the moving eigenvalue,
\[
C_E^{d-1}|_{z-x}
 =\widetilde E_z\otimes\widetilde E_x^{-1}\otimes V^{d-1}
 =C_E^d|_z\otimes E_x^{-1}.
\]
Dualizing gives eigenvalue \(E_x\) for \(A_E\). Keeping \(V\) in this calculation avoids an implicit choice of a basis of the fibre at the origin.

## 6. Trace characters and reciprocity

Now take a smooth projective geometrically connected curve over \(\mathbb F_q\) and a rank-one lisse Weil local system \(E\). The symmetric-power construction and large-degree descent have the same arithmetic form, using the étale projective-bundle descent specified in §3. They give \(C_E\) over the algebraic closure. The specified unit and Abel comparison make the construction functorial in \(E\). Applying it to the Frobenius comparison for \(E\) gives the Weil comparison for \(C_E\), uniquely and compatibly with multiplication. A rational base point is therefore unnecessary for the descended object, even if one was chosen over the algebraic closure to perform the intermediate construction.

Let
\[
\chi_E(L)=\operatorname{Tr}(\operatorname{Frob}_q,C_E|_L),
\qquad L\in P(\mathbb F_q).
\]
The descent proof in §6.2 identifies these rational Picard points with line-bundle classes.
The unit has trace \(1\), and multiplication identifies the one-dimensional Frobenius lines. Hence
\[
\chi_E(L\otimes M)=\chi_E(L)\chi_E(M),\qquad
\chi_E(\mathcal O_X)=1.                               \tag{6.1}
\]
The downward eigensheaf has trace \(\chi_E^{-1}\).

For a closed point \(x\), put
\(\alpha_x=\operatorname{Tr}(\operatorname{Frob}_x,E_{\bar x})\).
At an effective rational divisor \(D=\sum_x n_x x\), Frobenius cyclically permutes the factors at the conjugate points in (2.3). On unshifted lines, its trace is the trace of the composite around each cycle. Thus
\[
\chi_E(\mathcal O(D))=\prod_x\alpha_x^{n_x}.            \tag{6.2}
\]
Multiplicativity extends this to arbitrary rational divisors, by writing each as a difference of two effective divisors. In particular, for a rational function \(f\),
\[
\prod_x\alpha_x^{\operatorname{ord}_x(f)}=1,            \tag{6.3}
\]
because \(\mathcal O(\operatorname{div}f)\simeq\mathcal O_X\). This is the unramified reciprocity identity obtained from geometric descent. For \(A_E\), the character of \(\mathcal O(-x)\) is \(\alpha_x\), and
\[
T_xf_{A_E}(L)=f_{A_E}(L(-x))=\alpha_x f_{A_E}(L).
\]
At a nonrational place this uses the whole-closed-divisor correspondence of Lesson 4. There is no IC shift or half Tate factor for the torus's point fibre.

### 6.1. The Lang torsor and its character line

Let \(J\) be an abelian variety over \(\mathbb F_q\). The property that \(J=\operatorname{Pic}^0_X\) is such an abelian variety is a separate Picard-geometry prerequisite. Define

\[
\lambda:J\longrightarrow J,\qquad a\longmapsto F(a)-a.
\]

**Lemma 6.1.** The map \(\lambda\) is a finite étale surjection, with constant kernel \(J(\mathbb F_q)\), and is a torsor for this finite group acting by translations.

**Proof.** Since \(q\) is zero in the ground field, the differential of \(F\) is zero. The differential of \(\lambda\) at the identity is \(-1\), and translation identifies the differential at every point with this one. The étale Jacobian criterion for a map between smooth varieties of the same dimension therefore makes \(\lambda\) étale. Its geometric kernel has precisely the fixed points of \(q\)-power Frobenius, namely \(J(\mathbb F_q)\); this set is finite because a finite-type scheme over a finite field has finitely many rational points. The kernel is reduced, since its morphism to a point is an étale base change. It is thus the constant finite étale scheme on those rational points.

Every nonempty geometric fibre is a translate of the kernel, since \(\lambda\) is a homomorphism. The map is proper, as a map from a proper scheme to a separated scheme, and has finite fibres. One may prove its finiteness here without quoting a proper-quasi-finite theorem. After extending to an algebraic closure, use the projective graph of \(\lambda\) and choose a hyperplane avoiding the finite fibre over a chosen point. The image of the graph's closed intersection with that hyperplane is closed by properness and misses the point. Over a smaller affine target neighbourhood, the entire graph is therefore a closed subscheme of the complementary affine projective chart. Its inverse image is affine. Projective coherent finiteness, AG-QC-05, Corollary 2.3, then makes its coordinate algebra finite over the target ring. This proves finiteness locally, and finite morphisms descend under faithfully flat field extension (algebra descent, AG-DFG-02, Theorems 2.5 and 7.1, with Proposition 3.1).

The image is closed by properness and open by étaleness; it contains zero. Geometric connectedness of \(J\) makes it all of \(J\). Finally two points \(a,b\) in the same fibre differ by a unique kernel point. The inverse to the torsor map on scheme points is \((a,b)\mapsto(a,b-a)\), so the torsor assertion is a scheme identity, not only a geometric-point count. \(\square\)

Let \(\eta:J(\mathbb F_q)\to K^\times\) be a character; its image is finite. Define the line \(\mathcal L_\eta\) associated with this torsor by giving its fibre over \(y\) generators \(v_a\) for \(\lambda(a)=y\), with relations

\[
v_{a+t}=\eta(t)^{-1}v_a,\qquad t\in J(\mathbb F_q).
\]

On an étale splitting of the torsor this is a constant line; the displayed relations are its transition maps and satisfy the descent cocycle. It is consequently a lisse rank-one sheaf with finite monodromy, defined over \(\mathbb F_q\). Addition of lifts gives a canonical multiplication

\[
v_a\otimes v_b\longmapsto v_{a+b}.
\]

The relations make it well defined; addition makes it associative and symmetric. The generator \(v_0\) gives its unit. If \(y\in J(\mathbb F_q)\), the equality \(F(a)=a+y\) shows that **geometric** Frobenius sends the lift \(a\) to \(a-y\), hence

\[
\operatorname{Frob}_y(v_a)=v_{a-y}=\eta(y)v_a.
\]

Thus its geometric-Frobenius trace is \(\eta(y)\), with exactly the inverse in the transition relation needed for this sign. See the free author manuscript of [Forey–Fresán–Kowalski, *Arithmetic Fourier transforms over finite fields*, §1.6](https://arxiv.org/pdf/2109.11961) for a comparison of the Lang character-line convention; the fibre calculation here proves the sign used in this lesson.

**Lemma 6.2 (uniqueness on \(J\)).** A rank-one multiplicative Weil local system on \(J\) with specified Frobenius-invariant unit is determined, with its multiplication and unit, by its trace character on \(J(\mathbb F_q)\).

**Proof.** For such a line \(C\), multiplication and inverse give

\[
\lambda^*C\simeq F^*C\otimes C^{-1}.
\]

The Weil comparison identifies the right side with \(C\otimes C^{-1}\), canonically trivialized by the specified unit and evaluation. Thus \(C\) becomes a trivial Weil line on the Lang torsor, with the unit-compatible trivialization. The descent datum for a trivial line along this torsor is a scalar for each deck translation \(t\); that scalar is constant in \(a\), because \(J\) is geometrically connected and a morphism of constant local systems is a locally constant scalar. The cocycle makes those scalars a character of \(J(\mathbb F_q)\). The multiplication of lifts makes the trivialization multiplicative. Its Frobenius comparison is the constant identity: all maps used commute with Weil comparisons, and the specified unit fixes the scalar at zero. The preceding fibre computation says that the inverse deck character is exactly the trace character. Ordinary étale sheaf descent now identifies \(C\) with the corresponding \(\mathcal L_\eta\), preserving its multiplication and unit. The scalar automorphism of a rank-one multiplicative line preserving the unit must be one: multiplicativity gives \(c=c^2\). Hence the normalized comparison is unique. \(\square\)

### 6.2. Rational Picard points are line-bundle classes

The use of \(L_1\) as a rational **Picard point** below needs no representative line bundle on \(X\). To identify \(P(\mathbb F_q)\) with \(\operatorname{Pic}(X)\), rather than silently import \(\operatorname{Br}(\mathbb F_q)=0\), the following descent argument suffices.

AG-ET-08, Theorem 6.1 and equation (6.5), prove \(G_{\mathbb F_q}=\widehat{\mathbb Z}\) and the vanishing of its continuous \(H^2\) on torsion discrete modules. Its §3 proves the finite-quotient cochain comparison and its §6 writes the cyclic resolution and inflation maps. Every element of \(\overline{\mathbb F}_q^\times\) lies in a finite field, hence has finite order, so

\[
H^2(G_{\mathbb F_q},\overline{\mathbb F}_q^\times)=0.
\]

A Frobenius-invariant geometric line-bundle class can be represented over a finite extension. Choose finite descent isomorphisms between its conjugates, normalizing those in the open subgroup where the representative is defined. Their failure of the triple cocycle is multiplication by constants, because the only global units on a geometrically connected projective curve over the algebraic closure are its ground-field units. They give a continuous two-cocycle with values in \(\overline{\mathbb F}_q^\times\): all its data are over a finite extension. The vanishing just proved makes it a coboundary. Rescale the isomorphisms by that one-cochain; they now satisfy the cocycle and descend the line bundle by faithfully flat module descent, AG-DFG-02, Theorems 2.5 and 5.1. The finite data spread to a finite Galois extension. Uniqueness of the descended isomorphism class follows from Hilbert 90, AG-ET-08, Theorem 4.1: two descents differ by a scalar one-cocycle, which is a coboundary. Thus rational Picard points identify with line-bundle classes, including the degree-one class used above. This proves the needed finite-field assertion directly at the level of line-bundle descent; algebraic central-simple-algebra classification is unnecessary.

### 6.3. Constructing the inverse and checking continuity

Suppose the Picard geometry and large-degree Abel projective bundles used in §§1–4 have been established. Write \(P=\coprod_{d\in\mathbb Z}\operatorname{Pic}^d_X\), \(J=\operatorname{Pic}^0_X\). Let

\[
\chi:P(\mathbb F_q)\longrightarrow\overline{\mathbb Q}_\ell^\times
\]

be any character. If \(x_0\in X(\mathbb F_q)\), take \(L_1=\mathcal O(x_0)\). More generally, a degree-one rational Picard point exists even when \(X(\mathbb F_q)\) is empty. To prove this, choose a geometric point \(M\in\operatorname{Pic}^1_X(\overline{\mathbb F}_q)\). The latter space is a torsor for \(J\). Put \(c=F(M)-M\in J(\overline{\mathbb F}_q)\). Surjectivity of the Lang map gives \(a\) with \(F(a)-a=-c\); then \(M+a\) is Frobenius-fixed and defines \(L_1\in\operatorname{Pic}^1_X(\mathbb F_q)\). This argument uses no point-counting bound or degree-one divisor on \(X\).

Define

\[
\beta=\chi(L_1),\qquad \eta=\chi|_{J(\mathbb F_q)},\qquad
j_d:\operatorname{Pic}^d_X\longrightarrow J,\quad L\longmapsto L\otimes L_1^{-d}.
\]

The maps \(j_d\) are isomorphisms over \(\mathbb F_q\). Choose one finite coefficient field containing \(\beta\) and the finitely many values of \(\eta\). Let \(V_\beta\) be the constant geometric line with geometric-Frobenius comparison \(\beta\), and set

\[
C_\chi|_{\operatorname{Pic}^d}=j_d^*\mathcal L_\eta\otimes V_\beta^{\otimes d}.
\tag{6.4}
\]

Negative powers are dual powers. Since \(j_{r+s}(L\otimes M)=j_r(L)+j_s(M)\), the multiplication of \(\mathcal L_\eta\) makes this a multiplicative Weil line on all \(P\), with specified unit. At each rational \(L\) of degree \(d\), its trace is

\[
\eta(L\otimes L_1^{-d})\beta^d=\chi(L).
\]

Let \(a:X\to\operatorname{Pic}^1_X\), \(x\mapsto\mathcal O(x)\), and put

\[
E_\chi=a^*C_\chi.
\tag{6.5}
\]

This is a rank-one lisse Weil local system on \(X\). Multiplication gives a symmetric isomorphism \(\operatorname{AJ}_d^*C_\chi\simeq E_\chi^{(d)}\). It follows either directly from the tensor fibres and §2.2, or by pulling to \(X^d\) and using those same invariant frames at collisions. Large-degree projective-bundle full faithfulness from §3.4, and the all-degree uniqueness argument already written in Lesson 5 §4 show

\[
C_{E_\chi}\simeq C_\chi
\]

with the unit, multiplicativity and Abel comparison. Thus the construction from \(E\) to \(\chi_E\) is surjective onto all Weil characters.

It is also injective, without a Frobenius density theorem. For any normalized multiplicative Weil line \(C\) on \(P\), write \(V=C|_{L_1}\). Multiplication identifies its degree-\(d\) component with \(j_d^*C|_J\otimes V^{\otimes d}\). The trace of \(V\) is \(\beta\); as a Weil line on a rational point it is classified by this scalar. Lemma 6.2 identifies \(C|_J\) from \(\eta\). Hence its trace character determines \(C\) and then its Abel pullback \(E\). Applying this to \(C_E\) proves the inverse assertion. A different choice of \(L_1\) gives the same normalized \(C_\chi\) and \(E_\chi\) by this uniqueness.

For a closed point \(x\) of degree \(e\), multiplication over its Frobenius orbit gives, with ordinary unshifted tensor permutation,

\[
\operatorname{Tr}(\operatorname{Frob}_x,E_\chi|_{\bar x})
=\chi(\mathcal O(x)).
\tag{6.6}
\]

This is the same cycle-composite calculation as the trace calculation above, now applied to the constructed converse. No Chebotarev theorem or global class field theorem enters either inverse construction or uniqueness.

**Continuity qualification.** The Weil line \(E_\chi\) extends to a continuous rank-one representation of \(\pi_1(X)\) exactly when \(\beta\) is an \(\ell\)-adic unit. Indeed (6.4)–(6.5) express it as a finite-monodromy étale line times a constant Weil line \(V_\beta\). If \(\beta\in O^\times\), the maps \(\mathbb Z\to(O/\varpi^a)^\times\), \(n\mapsto\beta^n\), have finite image and factor through finite cyclic quotients. They extend compatibly to \(\widehat{\mathbb Z}\); their inverse limit gives the required continuous constant étale character. Conversely choose any closed point \(x\), of degree \(e>0\). Its eigenvalue in (6.6) is \(\beta^e\) times the finite-order eigenvalue of the Lang line. The image of a continuous profinite representation is compact, whose valuation subgroup is zero. Therefore \(e\,v_\ell(\beta)=0\) and \(v_\ell(\beta)=0\). A nonempty finite-type curve has a closed point, so no rational point is required. Equivalently, the admissible characters are the unit-valued characters, since every rational Picard point has the unique form \(j+dL_1\), with \(j\in J(\mathbb F_q)\) of finite order.

## 7. The local de Rham theorem for tori

Put \(D_x=\operatorname{Spec}k[[t]]\), \(D_x^\times=\operatorname{Spec}k((t))\), and \(LT=T(k((t)))\) in prestack notation, for a torus \(T\) with dual \(\check T\). The derived prestack \(\operatorname{LocSys}_{\check T}(D_x^\times)\) classifies flat \(\check T\)-bundles on the punctured formal disc. The field is algebraically closed of characteristic zero throughout this section.

The assigned local theorem is the symmetric monoidal equivalence
\[
\operatorname{Dmod}_{\mathrm{loop}}(LT)\simeq\operatorname{QCoh}(\operatorname{LocSys}_{\check T}(D_x^\times)).\tag{7.1}
\]
We prove its finite-level Weyl and difference-algebra calculation, its signs, transitions and coordinate-independent kernel below. The all-unbounded left affine comparison is proved in §7.2. The geometric right realization and pushforward still require the exact foundations specified there, and relative factorization remains unfinished. These remain obligations within this lesson.

### 7.1. Normal forms in families

Work over an algebraically closed characteristic-zero field \(k\). Write a connection as \(d-\omega\), so the \(\alpha\) in the convention \(d+\alpha\) is \(-\omega\). Under the active gauge action, \(\omega\) changes by \(d\log g\). For \(n\ge1\), put
\[
K_n=1+t^nR[[t]],\qquad
V_n=\bigoplus_{j=1}^{n-1} k\,t^{-j-1}dt.
\]
Here \(K_n\) is a group functor and \(V_n\) denotes a vector space, not just its set of \(k\)-points.

For \(n\geq1\), define
\[
\Omega^{\leq n}=t^{-n}R[[t]]\,dt,
\qquad
G^{\leq n}=\{g\in R((t))^\times:d_t\log g\in\Omega^{\leq n}\}.
\]
The bounded prestack is \([\Omega^{\leq n}/G^{\leq n}]\). This supplies an action that really preserves its space of connections. Equivalently, take the full groupoid on bounded representatives inside the unrestricted quotient: if both \(\omega\) and \(\omega+d\log g\) are bounded, their difference forces \(g\in G^{\leq n}\).

In the Laurent normal form, the derivative of the term \(t^{-j}\) is \(-j t^{-j-1}dt\). Thus the negative logarithm of a bounded gauge has only terms with \(1\leq j\leq n-1\). Its formal infinitesimal polar action is exactly \(\widehat{V_n}_0\). This also explains why unrestricted high-pole negative gauges must not be declared to act on the literal bounded connection space.

On connective derived test algebras, the displayed classical group and ind-scheme presentations are evaluated as spaces; every fibre and quotient below is a homotopy fibre or quotient.

The positive loop group is
\[
L^+\mathbb G_m=\mathbb G_m\times(1+tR[[t]]).
\]
The formal logarithm and exponential give inverse isomorphisms between \(1+tR[[t]]\) and \(tR[[t]]\), for every \(k\)-algebra \(R\). Each coefficient uses only finitely many terms. Differentiation identifies the latter space with the regular one-forms: integration divides the coefficient of \(t^{j-1}dt\) by \(j\), which is invertible. Consequently positive nonconstant gauge transformations eliminate every regular connection coefficient, uniquely.

An invertible Laurent series has, locally on its base, the form
\[
u=t^m s\,\exp(b_+(t))\exp(b_-(t)),                    \tag{L1}
\]
where \(m\in\mathbb Z\), \(s\in R^\times\), \(b_+\in tR[[t]]\), and \(b_-\) is a finite negative-power polynomial with nilpotent coefficients. To justify the infinitesimal part, first reduce the base. An invertible Laurent series over a reduced ring has a locally constant order: the orders of it and its Laurent inverse add to zero at every prime, and their finite pole bounds make the loci of a given order open and closed. On each such locus its leading coefficient is a unit; it is then \(t^m s\) times a positive unit. In the general case the finitely many negative coefficients left after this normalization generate a nilpotent ideal \(I\). Modulo \(I\) the required factorization is known. Inductively modulo \(I^{a+1}\), split the correction in \(I^a((t))/I^{a+1}((t))\) into its negative, constant and positive terms and absorb them into the corresponding factors. Cross terms lie in \(I^{a+1}\). Since \(I^N=0\), this process ends. Uniqueness follows at the first quotient in which two factorizations differ. Logarithm then gives (L1).

The negative factor is the formal completion of the negative-power vector space at zero. Its logarithmic derivative identifies it with the formal completion of the residue-zero polar one-forms: \(t^{-j}\) maps to \(-j t^{-j-1}dt\). The valuation factor \(t^m\) changes the residue by \(m\), and constant gauges remain the automorphism group \(\mathbb G_m\). Thus, writing \(W_{\mathrm{dR}}\) for the quotient of a vector space by its formal infinitesimal translations,
\[
\operatorname{LocSys}^{\le n}_{\mathbb G_m}(D^\times)
\simeq [\mathbb A^1/\underline{\mathbb Z}]
          \times(V_n)_{\mathrm{dR}}\times B\mathbb G_m. \tag{L2}
\]
The residue coordinate is \(a\) in \(\omega=a\,dt/t+\omega_{\mathrm{irr}}\). The integer action is translation \(a\mapsto a+m\). For \(S=\operatorname{Spec}A\), with \(A\) a connective characteristic-zero DG algebra, put \(A_{\mathrm{red}}=H^0(A)_{\mathrm{red}}\). For a finite-dimensional vector space \(V\), the map
\[
V(S)\longrightarrow V(S_{\mathrm{red}})
\]
is surjective on connected components, since \(H^0(A)\to A_{\mathrm{red}}\) is surjective. Its homotopy fibre over zero is, by definition, \(\widehat V_0(S)\). Translation identifies its Čech nerve with the action nerve
\[
V(S)\times\widehat V_0(S)^p
\]
in degree \(p\). The realization of this Čech nerve is \(V(S_{\mathrm{red}})\): over each point the nerve is that of its nonempty space of lifts, with its contractible groupoid of translation identifications. Consequently
\[
[V/\widehat V_0](S)\simeq V(S_{\mathrm{red}})=V_{\mathrm{dR}}(S).
\]
The homotopy-fibre formulation retains higher automorphisms on derived tests. An argument only with ordinary nilpotent coefficients does not itself state those higher identifications.

The reduction of \(L\mathbb G_m/K_n\) is
\[
\underline{\mathbb Z}\times\mathbb G_m\times\mathbb A^{n-1},
\qquad
u=t^m s\exp\left(\sum_{j=1}^{n-1}b_jt^j\right).
\]
Its formal negative factor disappears on taking the de Rham prestack. D-modules, defined as crystals, depend on that prestack. Hence
\[
D(L\mathbb G_m/K_n)
\simeq D(\underline{\mathbb Z}\times\mathbb G_m\times
                    \mathbb A^{n-1}).                 \tag{L3}
\]
This uses the actual quotient including nilpotent loops; it does not replace the loop group by its \(k\)-points.

For a field-valued regular-singular example, write the connection as \(d+r\,dt/t\). Its horizontal solution over \(\mathbb C\) is \(t^{-r}\), with monodromy \(e^{-2\pi i r}\). An active gauge \(t^m\) changes \(r\) to \(r-m\), so the monodromy is unchanged. In our \(d-\omega\) coordinates this is \(a=-r\) and \(a\mapsto a+m\). Constant gauges still give the scalar automorphisms in (L2).

### 7.2. Affine crystals and three algebra equivalences

In this subsection \(X\) denotes \(\mathbb A^d\) or \(\mathbb G_m\times\mathbb A^{d-1}\). We prove the left-crystal comparison on all DG modules, construct the admissible-affine exceptional pullback, and identify the standard right realization and geometric projection direct image in §§7.2.6–7.2.8. The categorical platform retains its exact recursive programme proof obligations. In particular the full local geometric theorem (7.1) is still conditional on them.

The field \(k\) has characteristic zero. All module categories below are the categories of **all** DG modules, with cohomological grading and quasi-isomorphisms inverted. There is no boundedness, coherence, holonomicity or finite-rank restriction.

We prove the comparison needed for
\[
X=\mathbb A^d\quad\text{or}\quad X=\mathbb G_m\times\mathbb A^{d-1}.
\]
The case \(d=0\) is the identity comparison for a point. Put
\[
A=k[x_1,\ldots,x_d]
\quad\text{or}\quad
A=k[x_1,x_1^{-1},x_2,\ldots,x_d].
\]
Write \(D\) for the Weyl algebra over \(A\): it is generated by \(A\) and commuting \(\partial_i\), with \([\partial_i,f]=\partial_i(f)\). In the second case this is the localized Weyl algebra. Equivalently its multiplicative coordinate can be written \(s=x_1\), \(\theta=s\partial_1\), with \([\theta,s]=s\).

The result, with the normalization made explicit, is
\[
\Phi_X:D\text{-}\mathrm{Mod}\ \xrightarrow{\sim}\
\operatorname{QCoh}(X_{\mathrm{dR}}).                 \tag{DC1}
\]
Evaluation on \(X\) is ordinary restriction from \(D\)-modules to \(A\)-modules. Its left adjoint is \(D\otimes_A^L-\), and its monad is this differential-operator algebra, including the algebra multiplication. All derived mapping complexes agree. Conditional on the full affine IndCoh foundation specified below, we also prove the right-crystal realization and the difference between the canonical **line** and the dualizing **complex**.

The proof uses finite formal neighborhoods, their explicit distribution duals, and a split free bar resolution. In particular, it does not deduce (DC1) from an equivalence of hearts.

#### 7.2.1. The derived infinitesimal groupoid

For a connective commutative DG algebra \(R\), let \(R_{\mathrm{red}}=H^0(R)_{\mathrm{red}}\). By definition
\[
X_{\mathrm{dR}}(\operatorname{Spec}R)=X(\operatorname{Spec}R_{\mathrm{red}}).
\]
The map \(X(R)\to X(R_{\mathrm{red}})\) is surjective on connected components: lift each coordinate through \(H^0(R)\to R_{\mathrm{red}}\). A lift of an invertible coordinate is invertible, because an element invertible modulo a nil ideal is invertible. Maps from a polynomial algebra to a DG algebra retain all higher homotopies; this assertion concerns surjectivity on components, not a replacement of their mapping spaces by sets.

Let \(G_p=X^{p+1}_{/X_{\mathrm{dR}}}\) be the Čech nerve, with vertices \(x^{(0)},\ldots,x^{(p)}\). Its value on \(R\) consists of tuples whose reductions coincide. The realization of this nerve is \(X_{\mathrm{dR}}\). To see this pointwise, the fibre over any reduced tuple is the nonempty space of its lifts; the Čech nerve of that space over a point has contractible realization. The nerve is therefore an effective equivalence-relation presentation on every derived test algebra.

Use adjacent differences
\[
h^{(j)}_i=x^{(j)}_i-x^{(j-1)}_i,
\qquad 1\leq j\leq p,\quad1\leq i\leq d.
\]
They have nilpotent classes in \(H^0(R)\). Put
\[
B_{p,n}=A[h^{(j)}_i]/((h^{(j)}_i)^n\text{ for all }i,j),
\qquad n\geq1.                                      \tag{DC2}
\]
Every vertex map \(q_j:\operatorname{Spec}B_{p,n}\to X\) is finite and flat. Indeed solve \(x^{(0)}=x^{(j)}-\sum_{l\leq j}h^{(l)}\); this identifies \(B_{p,n}\), as an algebra over the vertex copy of \(A\), with a truncated polynomial algebra in the differences. An invertible coordinate stays invertible under a nilpotent translation; its inverse is the finite geometric expansion. The monomials with each difference exponent less than \(n\) form a finite free basis over every vertex ring.

We need the presentation
\[
G_p\simeq\operatorname*{colim}_{n}\operatorname{Spec}B_{p,n}
\quad\text{as derived prestacks}.                    \tag{DC3}
\]
Here is a verification retaining the derived mapping spaces. In the smooth ambient product the elements \((h^{(j)}_i)^n\) are a regular sequence: after quotienting by any preceding powers, the monomials in those variables below their truncation bounds form a free basis over the remaining variables, so the next power is still injective. Localization for the invertible coordinates preserves this argument. The two-term Koszul complex of one such injective multiplication resolves its quotient. Tensoring successively with the next two-term complex proves the same assertion for the whole sequence. Its Koszul DG algebra, with generators \(e^{(j)}_i\) of degree \(-1\) and differential \(de^{(j)}_i=(h^{(j)}_i)^n\), is therefore a free DG resolution of \(B_{p,n}\). A lift of a fixed ambient map to this resolution chooses nullhomotopies of these powers. Such a lift exists for a sufficiently large \(n\), because the classes of the differences are nilpotent. Increasing \(n\) sends each chosen nullhomotopy to its product with the corresponding difference.

The difference between two choices is a loop in the mapping space of a coordinate, whose homotopy groups are modules over \(H^0(R)\). Multiplication by a difference is nilpotent on all of them, with the same nilpotence bound as its class in \(H^0(R)\). Consequently the filtered colimit of the spaces of choices is contractible. For several coordinates take the product of these nullhomotopy spaces. This proves (DC3), not merely its assertion on classical rings. Coordinate addition in a face map may increase a nilpotence bound, but it does so by a finite amount; using a larger \(n\) defines all nerve maps in (DC3).

We use the descent definition of quasicoherent sheaves on a prestack: an object is compatible quasicoherent data on its derived affine test schemes. This definition sends a colimit of prestacks to a limit of categories. Indeed compatible data on a colimit is exactly data on the pieces, with their compatibility over all arrows and higher simplices; the same description applies to mapping spaces. Hence
\[
\operatorname{QCoh}(G_p)=\lim_n B_{p,n}\text{-}\mathrm{Mod},
\qquad
\operatorname{QCoh}(X_{\mathrm{dR}})
=\operatorname{Tot}_{p}\operatorname{QCoh}(G_p).       \tag{DC4}
\]
The transitions in the first limit are derived tensor pullbacks. Colimits of compatible objects in these categories are computed componentwise, because derived pullback preserves colimits. Evaluation at degree zero in the second limit is conservative: every other component of a cartesian object is the pullback of that component along a vertex map.

#### 7.2.2. Distributions and the nerve adjunction

The ordered monomials \(\partial^I\) give \(D\) a free left and a free right \(A\)-module structure. For completeness, commuting a coordinate past a derivative using the displayed relations gives spanning. If a left-normal-ordered finite sum \(\sum_I f_I\partial^I\) acts as zero on \(A\), apply it coefficientwise to \(\exp(\sum_i x_i z_i)\in A[[z]]\). The result is \(\exp(\sum_i x_i z_i)\sum_I f_Iz^I\), so all \(f_I\) vanish. This proves independence. Right ordering follows by the same commutation relations. The argument uses polynomial coefficients of the formal exponential and works when \(x_1\) is inverted.

For an \(A\)-module complex \(N\), use the identification
\[
\operatorname{RHom}_A(D,N)
\ \xrightarrow{\sim}\ N[[h_1,\ldots,h_d]],
\qquad
\lambda\longmapsto
\sum_I\frac{\lambda(\partial^I)}{I!}h^I.              \tag{DC5}
\]
There is no hidden completion of a tensor product in this formula. The left \(A\)-module \(D\) is the direct sum of its displayed free summands, so its derived Hom is the product of copies of \(N\). On the right the same product is the inverse limit of finite truncated polynomial modules. The transition maps of that tower are surjective in every complex degree. Its derived inverse limit is its ordinary degreewise inverse limit: the difference map between the two products in the usual homotopy-limit cone is degreewise surjective, by recursively choosing lifts. This argument has no cohomological boundedness hypothesis.

The right \(A\)-action on \(D\) makes the left-hand side of (DC5) an \(A\)-module by \((f\lambda)(P)=\lambda(Pf)\). For a coordinate, the identity
\[
\partial^I x_i=x_i\partial^I+I_i\partial^{I-e_i}
\]
shows that this action becomes multiplication by \(x_i+h_i\) on the series in (DC5). The factorial is essential to this calculation. Thus (DC5) is an identification with the other-vertex action, not only an identification of underlying complexes. The formula for \(x_1^{-1}\) follows by inverting \(x_1+h_1\), or by the Leibniz rule for the inverse; each coefficient uses finitely many terms.

Put \(T(M)=D\otimes_A^L M\). Since \(D\) is free on the right, this tensor is exact on complexes. For any unbounded \(M,N\), affine tensor–Hom adjunction in the finite neighborhoods gives
\[
\begin{aligned}
\operatorname{RHom}_{G_1}(q_1^*M,q_0^*N)
&=\lim_n\operatorname{RHom}_{B_{1,n}}
 (B_{1,n}\otimes_{A_1}^L M,B_{1,n}\otimes_{A_0}^L N)\\
&=\operatorname{RHom}_{A_1}
 (M,N[[h]])\\
&=\operatorname{RHom}_{A_0}(T(M),N).
\end{aligned}
\tag{DC6}
\]
The middle equality follows because derived Hom out of \(M\) preserves limits. The limit of the targets is precisely (DC5) with its \(A_1\)-action. We have not moved an infinite direct sum past an infinite product.

The same calculation for \(p\) adjacent differences gives
\[
\operatorname{RHom}_{G_p}(q_p^*M,q_0^*N)
\simeq \operatorname{RHom}_A(T^p(M),N).              \tag{DC7}
\]
One can verify this by applying (DC6) successively. Algebraically, \(D\otimes_A\cdots\otimes_A D\) has a free left \(A\)-basis indexed by one derivative multi-index for each adjacent difference. Its Hom dual is the series module in those differences, with the final vertex acting at \(x^{(0)}+h^{(1)}+\cdots+h^{(p)}\). All these identifications are equivalences of mapping complexes and therefore of their mapping spaces and higher homotopies.

Nerve composition merges adjacent differences by addition. Dualizing the substitution \(h\mapsto h'+h''\) gives multiplication of derivative distributions: \(\partial^I\partial^J=\partial^{I+J}\), with the factorials supplying the binomial coefficients. Coefficients at an intermediate vertex are translated before pairing; the resulting identity is exactly \(\partial_i f-f\partial_i=\partial_i(f)\). The diagonal gives \(1\in D\). Thus the mates in (DC6)–(DC7) identify nerve composition and diagonal maps with the multiplication \(T^2\to T\) and unit \(\mathrm{id}\to T\) of the **derived** differential-operator monad. This identifies its algebra structure, not merely its underlying functor.

#### 7.2.3. Taylor transport and derived full faithfulness

For a DG \(D\)-module \(P\), write \(P_0\) for its underlying \(A\)-module complex. On a finite neighborhood define
\[
q_1^*P_0\longrightarrow q_0^*P_0,
\qquad
m\longmapsto\sum_I\frac{h^I}{I!}\partial^I m.         \tag{DC8}
\]
Only finitely many terms survive there. The Leibniz relation makes this map balanced for the two vertex actions. Substitution of two successive differences and the binomial identity give its cocycle. Its inverse uses the opposite difference, with the vertex coordinate also changed. Derivatives commute with the DG differential. These maps and their iterated versions give a genuine cartesian object of the entire derived nerve. This defines \(\Phi_X\) in (DC1); it preserves colimits, since every finite-neighborhood component is a derived tensor pullback of \(P_0\), and colimits in (DC4) are componentwise.

We now compute its derived maps. Mapping complexes in a limit of DG categories are the homotopy limit of the component mapping complexes. Use the transport of \(P\) to replace the source at vertex zero by its source at the last vertex. For DG \(D\)-modules \(P,Q\), (DC7) therefore identifies
\[
\operatorname{RHom}_{\operatorname{QCoh}(X_{\mathrm{dR}})}
 (\Phi_XP,\Phi_XQ)
\]
with the totalization of the cosimplicial complexes
\[
C^p=\operatorname{RHom}_A(T^pP_0,Q_0).               \tag{DC9}
\]
Its first and last cofaces use the derivative actions on \(Q\) and \(P\); intermediate cofaces multiply adjacent copies of \(D\), and codegeneracies insert their unit. This follows directly from the addition and diagonal computations after (DC7), together with (DC8). These are the cofaces and codegeneracies of the differential-operator bar mapping complex.

Here is a complete reason that this totalization computes \(\operatorname{RHom}_D(P,Q)\) for unbounded complexes. Form the augmented simplicial \(D\)-module
\[
\mathcal B_p(P)=D\otimes_A^L T^p(P_0),
\qquad p\geq0,                                      \tag{DC10}
\]
with faces given by multiplication or the action on \(P\), and degeneracies by the unit. After forgetting to \(A\)-modules its augmentation has an extra degeneracy, inserting \(1\in D\) in the first position. The simplicial identities give a contraction of its augmented normalized chain complex. If one represents the realization by a double complex, it uses the direct sum along the simplicial direction; multiplying the extra degeneracy by the internal-degree sign gives the contracting homotopy for the total differential. Every input has finite support in that direct sum, and the homotopy preserves finite support. Thus
\[
|\mathcal B_\bullet(P)|\simeq P                      \tag{DC11}
\]
without a boundedness or a spectral-sequence convergence assumption. This can also be expressed as the defining contraction of a split augmented simplicial object.

Derived tensor–Hom adjunction gives
\[
\operatorname{RHom}_D(\mathcal B_p(P),Q)
=\operatorname{RHom}_A(T^pP_0,Q_0).
\]
Mapping out of the realization (DC11) is its homotopy limit. Therefore (DC9) equals \(\operatorname{RHom}_D(P,Q)\), with its entire differential and higher mapping data. This proves full faithfulness of \(\Phi_X\) on **all** DG modules.

#### 7.2.4. The coherent free adjunction and generation

Let \(\mathcal N\) be an arbitrary object of the totalization in (DC4), and put \(M=\mathcal N|_X\). Its transport is an equivalence \(q_1^*M\to q_0^*M\) on \(G_1\), with all its cocycle homotopies on the higher nerve terms. Transpose that equivalence through (DC6). It gives
\[
\alpha:T(M)\longrightarrow M.                       \tag{DC12}
\]
The diagonal condition is the unit identity. The triangle cocycle, transposed through (DC7), is the associative action identity. All higher cocycle homotopies give the corresponding higher associative homotopies. This is justified on mapping spaces, not by differentiating an assertion in a heart: (DC6)–(DC7) are equivalences of derived mapping complexes, and the computations after them commute with every face and degeneracy.

More explicitly, on two adjacent differences the direct comparison using their sum transposes to \(\alpha\circ\mu_M:T^2M\to M\). The comparison through the middle vertex transposes to \(\alpha\circ T(\alpha)\). Hence the actual triangle homotopy transposes to
\[
\alpha\circ\mu_M\simeq\alpha\circ T(\alpha).
\]
On \(G_p\), composing through any string of intermediate vertices gives the corresponding sequence of multiplications and actions on \(T^pM\); insertion of a repeated vertex inserts its unit. The provided higher homotopies between these strings are sent by (DC7) to the higher homotopies between those same module-action composites. Equivalences of mapping complexes preserve paths and higher paths, so this describes the complete coherent action, rather than requiring it to be reconstructed from its first-order coefficient.

Keep \(T=D\otimes_A^L-\), and let \(\mathcal N\) be a genuine cartesian object of the **full** derived nerve, with \(N=\operatorname{ev}_X\mathcal N\). For \(M\in A\text{-}\mathrm{Mod}\), set \(L(M)=\Phi(D\otimes_A^L M)\). Compute the mapping object from \(L(M)\) to \(\mathcal N\) directly, before asserting an adjunction.

Using the Taylor transport of the free source and then (DC7), its cosimplicial mapping object is
\[
C^p(M,\mathcal N)=\operatorname{RHom}_A(T^{p+1}M,N).
\]
This is an identification of the whole cosimplicial object. Start with the genuine mapping diagram on the geometric nerve, apply the natural equivalences (DC7), and retain its given higher simplices. The multiplication/unit calculations identify the generating arrows of \(\Delta\); their relations hold before coefficient pairing, so transporting the entire diagram does not create a strictification obligation.

Write \(\alpha:TN\to N\) for the mate of \(\mathcal N\)'s one-edge transport. On endpoints, the cofaces are
\[
d^0(f)=\alpha\circ T(f),\qquad
d^i(f)=f\circ T^{i-1}\mu_{T^{p+1-i}M}\quad(1\le i\le p+1),
\]
for \(f:T^{p+1}M\to N\). The codegeneracies from degree \(p\) to degree \(p-1\) are precomposition with
\[
T^i\eta_{T^{p-i}M}:T^pM\to T^{p+1}M,\qquad 0\le i<p.
\]
These expressions suppress the actual higher coherences already supplied by the transported geometric mapping diagram; they are not a replacement of that diagram by a strict action.

Augment it by
\[
C^{-1}=\operatorname{RHom}_A(M,N),\qquad
a(g)=\alpha\circ T(g).
\]
There is an extra **last** codegeneracy
\[
h_p(f)=f\circ T^p\eta_M:C^p\longrightarrow C^{p-1}\quad(p\ge0).
\]
The monad unit identities give
\[
h_{p+1}d^{p+1}=\mathrm{id},\qquad h_0a=\mathrm{id}.
\]
Naturality of \(\eta\) gives \(h_{p+1}d^i=d^i h_p\) for \(0\le i\le p\); associativity with an inserted final unit gives the codegeneracy identities. At \(i=0\), the computation is
\[
\alpha T(f)\,T^{p+1}\eta_M
=\alpha T(f\,T^p\eta_M).
\]
For the other cofaces, a unit at the final slot commutes with an earlier multiplication, while its encounter with the last multiplication is exactly \(\mu\,T\eta=\mathrm{id}\).

Here is why these are coherent identities, not just equalities in the homotopy category. Each identity involving only multiplication and unit is an equality of actual DG bimodule maps. Each one involving \(\alpha\), including the augmentation compatibilities, is the image under the natural enriched adjunction of the corresponding face/repeated-vertex identity in the given cartesian nerve object \(\mathcal N\). That object already provides its entire simplicial coherence. The adjunction is an equivalence of mapping complexes, hence transports the full simplices and their faces, not just the endpoint maps. Adding a final unit uses these natural unit maps and the given simplices, so all relations between different strings of faces and degeneracies are transported together. This constructs the augmented split cosimplicial mapping object.

A split augmented cosimplicial object has limit its augmentation object. In the present complexes this can be checked by the alternating extra-codegeneracy contraction of the augmented normalized cochain object. On the product totalization, each output uses only one adjacent input component; the contraction therefore exists for an unbounded internal complex as well. There is no infinite sum to evaluate. We obtain naturally in both variables
\[
\operatorname{RHom}(L(M),\mathcal N)
\simeq\operatorname{RHom}_A(M,N).
\]
Taking \(M=N\) and the identity gives the counit \(\epsilon_{\mathcal N}\) of (DC13), as a map in the actual totalization with all its coherences. Naturality of this mapping equivalence proves the adjunction identities on mapping spaces. Its monad is \(T\), with multiplication already computed by the difference-coordinate pairing. The adjunction therefore constructs a genuine augmented simplicial bar, not a list of its objects. Its evaluation is split; continuity and conservativity give (DC15).

This constructs the adjunction and its bar without invoking a general monadicity theorem. Its input (DC7) must retain the indicated naturality for the entire geometric mapping diagram. It does not follow from the action identity in the heart alone.

The counit just constructed is the actual crystal map
\[
\epsilon_{\mathcal N}:\Phi_X(D\otimes_A^L M)\longrightarrow\mathcal N.
\tag{DC13}
\]

Now take the augmented free bar object in the crystal category,
\[
\mathcal B_p(\mathcal N)
=\Phi_X(D\otimes_A^L T^p M).                         \tag{DC14}
\]
Multiplication gives its first and intermediate faces; the last face uses (DC12); (DC13) gives its augmentation to \(\mathcal N\). The unit gives degeneracies. The full coherence just proved makes this a simplicial object, including its higher simplicial identities. After evaluation on \(X\) it is the monad bar complex with terms \(T^{p+1}M\), augmented by \(\alpha\). Insertion of the unit is again an extra degeneracy. The argument of (DC11) gives
\[
|\mathcal B_\bullet(\mathcal N)|\big|_X\simeq M.
\]
Evaluation preserves this realization and is conservative, by §7.2.1. Hence
\[
|\mathcal B_\bullet(\mathcal N)|\simeq\mathcal N.      \tag{DC15}
\]

Every term of (DC14) lies in the image of \(\Phi_X\). Full faithfulness, already established, lifts its whole simplicial diagram to \(D\)-modules, including all higher maps and homotopies. Since \(\Phi_X\) preserves realizations, its image contains (DC15). This proves essential surjectivity and completes (DC1).

This is the missing generation argument: arbitrary derived crystals are resolved by differential-induced free objects. It is not a statement that an ordinary Taylor equivalence automatically extends to the unbounded descent category.

#### 7.2.5. Evaluation, tensor products and totalization

Under (DC1), evaluation is the restriction functor
\[
U:D\text{-}\mathrm{Mod}\to A\text{-}\mathrm{Mod}.
\]
It is conservative and preserves all colimits. Its left adjoint is
\[
L(M)=\Phi_X(D\otimes_A^L M).
\]
This adjunction can either be read from the established equivalence or checked by the free-to-arbitrary map (DC13). A map \(M\to U\mathcal N\) extends to the unique derived crystal map \(L(M)\to\mathcal N\) by composing its induced map with (DC13). Restricting such a map to \(1\otimes M\) is inverse; the diagonal and triangle cocycles prove the two identities on mapping spaces.

Its unit is \(m\mapsto1\otimes m\), and its counit is (DC13). The monad \(UL\) is \(D\otimes_A^L-\); multiplication is composition of differential distributions, as computed after (DC7). The augmented bar realizations are equivalences because their evaluated augmented bars are split and evaluation is conservative. These supply the unit and counit of the comparison with coherent monad modules. The ordinary induction–restriction unit and counit themselves need not be equivalences. This proves monadicity here by its bar construction, without importing a monadicity theorem.

The object \(L(A)=\Phi_X(D)\) is a compact generator. Indeed
\[
\operatorname{RHom}(L(A),\mathcal N)=U\mathcal N
\]
as a complex, which commutes with colimits and detects zero. Its endomorphism algebra is \(D^{\mathrm{op}}\), as appropriate for the free **left** \(D\)-module; the induction monad is \(D\), not its opposite.

The comparison also identifies the tensor product needed on the spectral side. Resolve two DG \(D\)-modules by free \(D\)-modules using the same split bar construction over \(k\). These resolutions are \(A\)-K-flat: each free term is a direct sum of \(A\) tensored with a complex of vector spaces, and its realization is built from these terms by sums and cones. On the resolutions the derivative on the tensor is \(\partial_i\otimes1+1\otimes\partial_i\), and the Taylor comparison is the product of the two Taylor comparisons. Affine pullback and tensor give the same formula at every finite neighborhood. Passing to the resolutions therefore gives
\[
\Phi_X(P\otimes_A^L Q)\simeq\Phi_X(P)\otimes\Phi_X(Q),
\qquad \Phi_X(A)=\mathcal O_{X_{\mathrm{dR}}}.
\]
The comparison respects the ordinary complex symmetry and its Koszul signs. This is the left-crystal tensor convention; the density correction for right-crystal convolution is treated below.

There are two different infinite operations in this proof. The formal coefficient limit in §7.2.2 is a surjective inverse system and is computed by the product series module (DC5). The descent totalization of mapping complexes is the derived Hom out of the split bar realization (DC10). Its convergence is therefore the identity (DC11), with an actual contracting extra degeneracy. We have not used an unbounded first-quadrant spectral sequence, exchanged two infinite limits and colimits, or inferred convergence from the number of coordinates. The finite number of coordinates ensures that each finite-stage algebra and its coordinate maps have the stated finite free descriptions; it does not replace the split-bar argument.

#### 7.2.6. Affine exceptional pullback and standard right crystals

An **admissible affine test** here is \(\operatorname{Spec}C\), where \(C\) is a connective commutative DG \(k\)-algebra, \(H^0(C)\) is finitely generated over \(k\), each \(H^i(C)\) is finite over \(H^0(C)\), and only finitely many \(H^i(C)\) are nonzero. These are the eventually coconnective almost-finite-type affine tests used in the right-crystal definition. The construction below covers every map between these tests. It does not claim an \(\operatorname{IndCoh}^!\) construction on arbitrary unbounded derived affines, infinite polynomial algebras, or arbitrary prestacks outside the right-Kan definition.

We write \(\operatorname{Coh}(C)\) for DG \(C\)-modules with bounded finite cohomology, and
\[
\operatorname{IndCoh}(C)=\operatorname{Ind}(\operatorname{Coh}(C)).
\]
Its compact mapping complexes on coherent objects are the actual derived \(C\)-module mapping complexes. Derived tensor and Hom are taken in DG modules, with all higher mapping data retained.

##### 7.2.6.1. Polynomial algebra foundations

Let \(P=k[z_1,\ldots,z_n]\). It is Noetherian: the leading coefficients of an ideal in \(R[z]\) form a finite ideal when \(R\) is Noetherian. Choose polynomials realizing its generators; subtract their appropriate multiples to reduce any polynomial above the maximum chosen degree. Remainders form a submodule of a finite free \(R\)-module and are finite. Induction starts with \(k\).

Every \(P\)-module has projective dimension at most \(n\). In \(P\otimes_kP\), the differences \(z_i\otimes1-1\otimes z_i\) form a regular sequence, since successive quotients are polynomial rings in the remaining variables. The Koszul complex resolves the diagonal \(P\). Exactness follows by adjoining one non-zero-divisor at a time and its two-term resolution. As a complex of right \(P\)-modules, this finite augmented resolution splits: its last quotient is the free right module \(P\), and recursively each kernel is a projective summand of the preceding free term. Tensoring it over the right \(P\) with any module \(M\) gives a length-\(n\) resolution by left modules \(P\otimes_kM\), which are free after choosing a vector-space basis. For finite modules, Noetherianity permits finite free surjections and finite kernels. The last kernel after \(n\) steps is projective by dimension shifting; its free surjection splits since its extension class is zero. Thus bounded coherent \(P\)-complexes are perfect.

There is also a bounded injective resolution of \(P\), of length at most \(n\). An injective embedding of any \(P\)-module \(V\) is
\[
V\longrightarrow\operatorname{Hom}_k(P,V),\qquad
v\longmapsto (a\mapsto av).
\]
The target is injective because Hom into it is \(\operatorname{Hom}_k(-,V)\), which is exact. Iterate on cokernels. At stage \(n\), dimension shifting gives \(\operatorname{Ext}^1_P(-,\text{last cokernel})=0\), so that cokernel is injective. A bounded complex of injectives is K-injective even against unbounded acyclic complexes: Hom into each injective is exact, and the finite totalization preserves exactness.

Put \(\Omega_P=\omega_P[n]\), using the coordinate top-form line. A bounded injective representative has degrees \(-n,\ldots,0\). Consequently
\[
L\in\operatorname{Mod}_P^{\le b}\Longrightarrow
\operatorname{RHom}_P(L,\Omega_P)\in\operatorname{Mod}_P^{\ge-b-n},
\]
\[
L\in\operatorname{Mod}_P^{\ge a}\Longrightarrow
\operatorname{RHom}_P(L,\Omega_P)\in\operatorname{Mod}_P^{\le-a}.
                                                               \tag{RF1}
\]
These bounds hold for arbitrary one-sided unbounded complexes and will control every truncation limit below. No first-quadrant convergence argument is used.

##### 7.2.6.2. Absolute affine coherent duality and presentation independence

Choose a polynomial map \(P\to C\) surjective on \(H^0\). Such a map exists by choosing cycle representatives of finitely many algebra generators. As a \(P\)-complex, \(C\) is bounded coherent, hence perfect. Define
\[
\Omega_C=\operatorname{RHom}_P(C,\Omega_P),\qquad
\mathbb D_C(F)=\operatorname{RHom}_C(F,\Omega_C).
                                                               \tag{RF2}
\]
Derived coinduction gives naturally, including the \(C\)-action,
\[
\mathbb D_C(F)=\operatorname{RHom}_P(F,\Omega_P).                 \tag{RF3}
\]
A coherent \(C\)-complex is a perfect \(P\)-complex. The same conclusion holds for any polynomial map over which \(C\) is bounded coherent, even if that map is not surjective on \(H^0\); this wider form will be used when a finite extension inherits its source's ambient ring. Termwise evaluation on a finite projective resolution therefore gives
\[
F\xrightarrow{\sim}\mathbb D_C\mathbb D_C F
\quad(F\in\operatorname{Coh}(C)).
                                                               \tag{RF4}
\]
The evaluation is the usual signed DG evaluation; its two duality triangle identities hold on those projective complexes. Both duals have finite \(H^0(C)\)-cohomology because the \(P\)-cohomology is finite and its action factors through \(H^0(C)\).

Here is an explicit comparison of polynomial presentations, needed rather than an assertion that a dualizing complex is intrinsic. Add a polynomial block \(Q=k[y_1,\ldots,y_m]\) with a map \(Q\to C\), and compare \(P\) with \(S=P\otimes_k Q\). The new presentation is again finite on cohomology. Write the chosen cycle images as \(b_i\in C^0\). On \(C[y]\), the monic elements \(y_i-b_i\) have the Koszul resolution
\[
K=C[y,e_1,\ldots,e_m],\qquad |e_i|=-1,\quad de_i=y_i-b_i,
\]
augmented by \(y_i\mapsto b_i\). For one variable multiplication by \(y-b\) is injective in every graded degree and has quotient \(C\); tensoring the successive two-term resolutions proves the assertion for the entire DG complex. Meanwhile perfect base change over \(P\) gives
\[
\operatorname{RHom}_{S}(C[y],\Omega_S)
=\Omega_C\otimes_k\omega_Q[m].
\]
Coinduction followed by the finite Koszul dual gives
\[
\operatorname{RHom}_{S}(C,\Omega_S)
=
\operatorname{RHom}_{C[y]}
 \bigl(C,\Omega_C\otimes_k\omega_Q[m]\bigr)
\xrightarrow{\sim}\Omega_C.                                  \tag{RF5}
\]
The last map is contraction of the ordered top Koszul generator against \(dy_1\wedge\cdots\wedge dy_m\); the normal length \(m\) cancels its shift \([m]\). The same map gives an identification of the entire coherent duality functors, by coinduction for each \(F\), not only of the objects \(\Omega_C\).

For two arbitrary presentations \(P,Q\), use their common product \(P\otimes Q\) and (RF5) in both directions. For three presentations use \(P\otimes Q\otimes R\). Killing two graph blocks successively is the augmentation of the tensor product of their Koszul complexes; it agrees with killing their union. These are actual DG augmentations. Hence the pairwise identifications obey the triangle cocycle. Four and more blocks give the same equality of tensor-product augmentations, so all associativity coherences are provided at once. Permuting blocks uses the usual Koszul symmetry on their exterior generators and the same symmetry on the shifted top differential lines; contraction respects both.

Dependence on maps into a derived \(C\) also retains higher homotopies. Use the **fixed universal** diagonal resolution
\[
K_Q=(Q\otimes_kQ)[e_1,\ldots,e_m],\qquad de_i=y_i-u_i,
\]
augmented to \(Q\). It is free over the first copy of \(Q\), and its augmentation is the same successive monic Koszul resolution. Derived base change along an evaluation map \(Q\to C\) gives exactly the graph resolution above. The augmentation, its dual and its top contraction are fixed morphisms before this base change. The derived base-change functor acts on the entire mapping space of evaluation maps; its coherent maps can be constructed from the functorial two-sided module bar, whose augmentations are split and whose multiple tensor comparisons come from the same multi-bar complex. Applying this functor to these fixed morphisms therefore provides all their higher comparisons and all their faces simultaneously. It does not ask for a choice of new homotopies after pairing coefficients. As an explicit degree-one check, if \(b_i'=b_i+dt_i\), the map from the primed resolution to the unprimed one sends \(e_i'\) to \(e_i-t_i\), whose differential is \(y_i-b_i'\). Thus (RF5) gives coherent presentation independence, not merely equality on \(H^0\). We can use (RF2) with any choices without changing the resulting affine duality or its comparison maps.

The same duality extends to one-sided complexes with finite cohomology in each degree. If \(L\) is bounded above and coherent degreewise, truncate below it. The maps
\(\mathbb D_C(\tau^{\ge a}L)\to\mathbb D_CL\) become equivalences in each fixed degree as \(a\to-\infty\), by (RF1). Their duals and (RF4) give
\[
\mathbb D_C\mathbb D_C L
=\lim_{a\to-\infty}\tau^{\ge a}L=L.
\]
The inverse limit of these truncations is checked degreewise; its tails eventually vanish in each degree. Bounded-below degreewise coherent complexes are treated dually, using their increasing upper truncations and the fact that derived Hom takes colimits in its first argument to limits. Finite projective \(P\)-resolutions of bounded coherent windows prove finite cohomology of every dual window. Evaluation and its duality triangle identities are the natural windowwise maps; their limits and colimits are those same maps on the one-sided complexes. Thus \(\mathbb D_C\) exchanges bounded-above and bounded-below degreewise coherent complexes with genuine coherent biduality.

##### 7.2.6.3. A canonical bounded-below lift into IndCoh

For a bounded-below, degreewise coherent \(C\)-module \(M\), define
\[
J_C(M)=\operatorname*{colim}_{b\to+\infty}\tau^{\le b}M
\quad\text{in }\operatorname{IndCoh}(C).                       \tag{RF6}
\]
Each truncation is coherent. For \(F\in\operatorname{Coh}(C)\), compactness gives
\[
\operatorname{RHom}_{\operatorname{IndCoh}(C)}(F,J_C M)
=
\operatorname*{colim}_b\operatorname{RHom}_C(F,\tau^{\le b}M)
=
\operatorname{RHom}_C(F,M).                                  \tag{RF7}
\]
For the second equality, if \(F\le c\), the omitted target tail is at least \(b+1\); its Hom from \(F\) is at least \(b+1-c\). Thus each mapping cohomology degree stabilizes. This argument includes an arbitrarily long projective resolution of \(F\).

Mapping out of (RF6), and then using (RF7), proves that \(J_C\) is fully faithful on this one-sided category. It is exact: testing a triangle against every coherent compact object gives precisely its ordinary derived-Hom triangle, and those tests detect equivalences in the Ind-completion. On a bounded coherent \(M\), the lift is its original compact object.

We will also use the following consequence. If \(M_b\to M\) are maps of bounded-below degreewise coherent complexes and their cones have lower bounds tending to \(+\infty\), then
\[
\operatorname*{colim}_b J_C(M_b)\simeq J_C(M).
                                                               \tag{RF8}
\]
Test against coherent \(F\le c\); its Hom into those cones has lower bounds tending to \(+\infty\). The mapping complexes stabilize and (RF7) proves (RF8). This is the precise continuity argument used in composition; it does not replace IndCoh by all ordinary modules.

##### 7.2.6.4. Construction of affine \(!\), composition and finite-map adjoints

For a map \(f:\operatorname{Spec}B\to\operatorname{Spec}C\), and coherent \(N\), set
\[
f^!(N)=
J_B\mathbb D_B\bigl(B\otimes_C^L\mathbb D_C N\bigr).
                                                               \tag{RF9}
\]
The tensor in parentheses is bounded above and coherent degreewise. To verify this, a bounded-above coherent complex over a connective Noetherian DG ring has a resolution by finite free cells in successively lower degrees. At its highest nonzero cohomology choose finitely many generators, map the corresponding finite free shifts, and take the cone. Its highest cohomology disappears; its remaining cohomology is finite by Noetherianity. Repeat. The partial resolutions have cones whose upper bounds tend to \(-\infty\). Derived tensor with a connective \(B\) preserves these upper bounds. In each fixed degree the tensor is therefore computed by a finite stage of finite free \(B\)-cells and is finite over \(H^0(B)\). Duality then makes the output bounded below and degreewise coherent, as required for \(J_B\).

The expression (RF9) is exact on coherent \(N\). The Ind universal property extends it uniquely to a continuous functor on all of \(\operatorname{IndCoh}(C)\). Here “continuous” includes all colimits: an exact extension preserving filtered colimits preserves coproducts as filtered colimits of finite sums, and preserves realizations as the sequential colimits of their finite skeleta.

It remains to prove composition on the noncompact output of (RF9). Let \(K\) be bounded below and degreewise coherent. By (RF6), \(J_B K=\operatorname{colim}_b\tau^{\le b}K\) in IndCoh. Dualizing the omitted positive tail puts its dual in degrees at most \(-b-1\), by (RF1). Tensor with a connective algebra \(E\) preserves that upper bound. Dualizing over a polynomial presentation of \(E\), of dimension \(e\), then puts the error in degrees at least \(b+1-e\). Formula (RF8) consequently proves
\[
g^!(J_BK)=
J_E\mathbb D_E\bigl(E\otimes_B^L\mathbb D_BK\bigr).
                                                               \tag{RF10}
\]
Applying this to \(K=\mathbb D_B(B\otimes_C^L\mathbb D_CN)\), its one-sided biduality and tensor associativity give
\[
g^!f^!N
=
J_E\mathbb D_E(E\otimes_C^L\mathbb D_CN)
=(f\circ g)^!N.                                                \tag{RF11}
\]
For the identity map (RF4) gives the identity functor. The composition maps use the natural bidual evaluation and tensor associativity. For three maps, the two comparisons remove the same adjacent duality pairs in the same tensor diagram; the duality triangle identities and associativity identify them. Arbitrary strings give the corresponding associative tensor diagram with these same evaluation maps. This provides the coherent contravariant functor, rather than only isomorphisms of functors in a homotopy category. Extension from coherent generators retains this full diagram.

Suppose now that \(f\) is finite, meaning \(B\) is bounded coherent over \(C\). With a common polynomial presentation \(P\to C\), \(B\) is also perfect over \(P\). Coinduction gives the canonical identification
\[
\Omega_B=\operatorname{RHom}_C(B,\Omega_C).
\]
Therefore the underlying one-sided module in (RF9) is
\[
\begin{aligned}
\mathbb D_B(B\otimes_C^L\mathbb D_CN)
&=\operatorname{RHom}_C(B\otimes_C^L\mathbb D_CN,\Omega_C)\\
&=\operatorname{RHom}_C(B,N).
\end{aligned}                                                  \tag{RF12}
\]
Presentation independence from (RF5) identifies this computation with any chosen presentation for \(B\).

Restriction of scalars preserves coherent objects for a finite map, so its continuous Ind-extension \(f_*\) preserves compact objects. For coherent \(F\) over \(B\), (RF7), (RF12) and ordinary derived coinduction give
\[
\operatorname{RHom}(F,f^!N)=\operatorname{RHom}(f_*F,N).
\]
This first holds for coherent \(N\), and then for all IndCoh \(N\): both sides commute with its colimits because \(F\) and \(f_*F\) are compact and \(f^!\) is continuous. Finally write arbitrary \(F\) as a filtered colimit of coherent objects; both mapping functors take that colimit to a limit. This proves \(f_*\dashv f^!\) on all objects and all derived mapping spaces. Thus the finite arrows of the earlier formal diagram use exactly these adjoints, with their canonical composition comparisons.

An infinite-Tor check explains why the bounded-below lift matters. For \(C=k[\epsilon]/(\epsilon^2)\to B=k\), the resolution of \(k\) has a free \(C\) in every nonpositive degree and differential multiplication by \(\epsilon\). Applying Hom into \(k\) gives zero differentials and one \(k\) in every nonnegative degree. Accordingly \(f^!k=J_k(\operatorname{RHom}_C(k,k))\) is generally noncompact, although the finite-map adjunction holds on all objects. Formula (RF10), rather than an assumption that \(f^!\) preserves coherent objects, is what makes composition valid in this case.

For a smooth affine product projection with
\(B=C[v_1,\ldots,v_r]\), perfect base change in a polynomial ambient presentation gives
\[
\Omega_B=B\otimes_C^L\Omega_C\otimes\omega_{B/C}[r].
\]
For coherent \(N\), its \(\mathbb D_CN\) is perfect over the polynomial ambient ring. The same base-change computation of its dual therefore gives
\[
f^!N=\omega_{B/C}[r]\otimes_C N.                              \tag{RF13}
\]
The right side denotes the Ind-extension of flat coherent pullback and this line/shift. If a vertical coordinate is inverted, use the polynomial ambient block \(P[v,t]\) and its regular relation \(vt-1\). Injectivity is seen from the highest \(v\)-power: its coefficient is multiplied by \(t\), which is injective in the polynomial ring. The one-equation Koszul dual gives the top differential line of \(P[v,v^{-1}]\), shifted by its dimension: the conormal differential \(d(vt-1)\) removes the normal line, and its \(dt\)-coefficient \(v\) is a unit on the quotient. Finite coinduction through that quotient followed by perfect base change from \(P\) gives exactly (RF13), with the canonical relative line on the multiplicative coordinate. This proves the localized case without importing an open-base-change theorem. Both functors are continuous, so (RF13) holds on all IndCoh objects. This is an actual smooth projection computation, distinct from the finite-map adjunction.

For any admissible \(C\to B\), choose a polynomial algebra \(Q=k[y_1,\ldots,y_s]\to B\) surjective on \(H^0(B)\). Factor the corresponding arrow through \(\operatorname{Spec}(C\otimes_kQ)\). This middle algebra is admissible. The arrow from \(\operatorname{Spec}B\) is finite in the derived sense used here: its bounded cohomology is finite over the middle algebra because it is finite over the quotient \(H^0(B)\). The other arrow is a smooth polynomial projection. Equation (RF11) consequently expresses the constructed pullback as the finite restriction right adjoint after the smooth relative-line pullback of (RF13). Adding generators gives a common factorization, whose comparisons are the graph-Koszul and composition maps already constructed. Thus this functor has the actual finite/smooth characterization of affine exceptional pullback.

##### 7.2.6.5. Comparison on the formal presentation and all affine arrows

The derived \(C\)-module category acts continuously on \(\operatorname{IndCoh}(C)\). On perfect modules this action is tensoring coherent objects with finite projective complexes; extend from finite free cells, sums and free module bars in both variables. The bar augmentation is split after forgetting the free action, so this defines the associative action and its unbounded extension. Define
\[
\Upsilon_C(M)=\Omega_C\otimes_C^L M
\quad\text{using this IndCoh action}.                          \tag{RF14}
\]
Duality gives \(\operatorname{RHom}_{\operatorname{Coh}(C)}(\Omega_C,\Omega_C)=C\): it is the dual of \(\operatorname{RHom}_C(C,C)\), including its DG algebra action. Since \(\Omega_C\) is compact, the unit for the tensor–Hom adjunction of (RF14) is an equivalence on \(C\), its sums and shifts, and then on every DG module by the split free bar. Thus \(\Upsilon_C\) is fully faithful. It is generally not essentially surjective on a singular affine.

Formula (RF9), with \(\mathbb D_C\Omega_C=C\), gives
\[
f^!\Omega_C=\Omega_B.
\]
The induced action of a function of \(C\) is its actual image in \(B\), by the two dual evaluations and derived tensor in (RF9). The two continuous functors
\[
f^!\Upsilon_C,\qquad \Upsilon_B(B\otimes_C^L-)
\]
therefore agree on the free generator with its entire endomorphism DG algebra, and agree on its functorial free bars. This constructs their natural equivalence on all modules. On composites its comparison is exactly (RF11) on the generator; the same free bars extend the coherent identity. Hence \(\Upsilon\) is a natural transformation for **all admissible affine arrows**, not just the finite ones.

Extend the affine \(!\)-functor to prestacks on admissible tests by its right-Kan formula. This is a construction, with no general prestack comparison theorem imported. The extension sends a colimit of prestacks to a limit of categories: a functor from any category \(K\) into its value is compatible data on the elements of the prestack, equivalently a map to the presheaf \(S\mapsto\operatorname{Map}(K,\operatorname{IndCoh}(S))\). Mapping out of a presheaf colimit gives the desired limit; testing every \(K\) proves the categorical identity.

For the \(X\) of the affine crystal lemma, restrict its pointwise derived presentations
\[
G_p=\operatorname{colim}_n\operatorname{Spec}B_{p,n},
\qquad X_{\mathrm{dR}}=|G_\bullet|
\]
to admissible tests. Both identities remain pointwise identities. The right-Kan category is consequently the \(!\)-limit over those finite stages followed by the nerve totalization. Formula (RF12) proves that its arrows are the actual finite-map adjoints used in the candidate. The left QCoh construction on all derived tests and its restricted construction on admissible tests give the same category here, since both presentations use these same classical finite-stage rings. No restriction/cofinality theorem for arbitrary prestacks is needed.

At degree zero \(X\) is regular, so \(\operatorname{IndCoh}(X)=\operatorname{Mod}_A\), by the polynomial global-dimension proof and its localization. Every cartesian right-descent object is pulled from this degree-zero object. Along each vertex the truncated-coefficient dual is free of rank one, and (RF12) identifies the pullback with \(\Upsilon_{B_{p,n}}\) of the corresponding ordinary vertex pullback. Full faithfulness of (RF14) transports all mapping spaces and all coherent nerve data. Conversely left data gives right data. This is the right comparison for \(X\) with the full affine functor now actually constructed; no unstated GL-DMOD-17 theorem is filling that step.

##### 7.2.6.6. Positive-dimensional projection: pullback, pushforward and shifts

Let \(Y,V\) be the smooth affine spaces, with the indicated invertible coordinate, used in Lesson 5. Write \(W=Y\times V\), \(r=\dim V\), and \(p:W\to Y\). The de Rham prestack map gives the intrinsic right-crystal pullback \(p^{!,\mathrm{cr}}\). Naturality in section 5 identifies it through \(\Upsilon\) with left QCoh crystal pullback.

For an ordinary left \(D_X\)-module complex define its dimension-normalized right realization by
\[
R_X(M)=\Upsilon_{X_{\mathrm{dR}}}\bigl(\Phi_X(M)[-\dim X]\bigr).
                                                               \tag{RF15}
\]
Its evaluation is \(\omega_X\otimes M\), the canonical **line**, with the usual right action and no residual shift. Taylor pullback along the product projection is ordinary flat connection pullback; vertical derivatives differentiate only the vertical coefficients. Thus
\[
p^{!,\mathrm{cr}}R_Y(N)
=R_W\bigl(p^*_{\mathrm{conn}}N[r]\bigr).                       \tag{RF16}
\]
This computes geometric pullback from the prestack definition and the established affine naturality. The \([r]\) is precisely \(\dim W-\dim Y\). The shifted smooth functor \(p^{!,\mathrm{cr}}[-2r]\) therefore corresponds to \(p^*_{\mathrm{conn}}[-r]\).

Construct the right adjoint of this intrinsic shifted smooth functor. On ordinary modules, the bounded free left \(D_V\)-Spencer resolution of \(\mathcal O_V\) has terms \(D_V\otimes\bigwedge^jT_V\) in degrees \(-j\). Its exactness follows from the regular vertical-symbol Koszul complex: a finite-order cycle is corrected by a boundary with the same top symbol; repeated correction strictly lowers its finite order and terminates. Tensor–Hom adjunction with this finite free complex gives, for **all** unbounded DG \(M,N\),
\[
\operatorname{RHom}_{D_W}
 \bigl(p^*_{\mathrm{conn}}N[-r],M\bigr)
=
\operatorname{RHom}_{D_Y}
 \bigl(N,\Gamma(W,\operatorname{DR}_{W/Y}^0M)[r]\bigr).
                                                               \tag{RF17}
\]
There are only \(r+1\) resolution degrees. Any resolution of \(N\) is handled by derived tensor–Hom adjunction; no finite-generation or boundedness of \(N\) is assumed.

Transport this adjunction through (RF15). It constructs intrinsically, for these geometric smooth projections, the de Rham direct image as the right adjoint of \(p^{!,\mathrm{cr}}[-2r]\), and proves
\[
p_*^{\mathrm{cr}}R_W(M)
=
R_Y\bigl(\Gamma(W,\operatorname{DR}_{W/Y}^0M)[r]\bigr).
                                                               \tag{RF18}
\]
Uniqueness of right adjoints supplies its unit, counit and coherent composition for product projections. This is a local construction of geometric pushforward, not an invocation of a general six-functor theorem.

To compare it with the programme's independent ordinary transfer definition, resolve
\[
T_p=B\otimes_{A_Y}D_Y
\]
as a left \(D_W\)-module by the relative Spencer complex \(D_W\otimes_B\bigwedge^jT_{W/Y}\). Its exactness is the same finite-symbol argument. Its terms are finite free, hence K-flat, and its finite length computes \(Q\otimes_{D_W}^LT_p\) for every unbounded right module \(Q\). Changing sides by canonical **lines** contracts
\(\omega_{W/Y}\otimes\bigwedge^jT_{W/Y}\) to \(\Omega^{r-j}_{W/Y}\). The contraction sign is
\[
(-1)^{j(r-1)+\binom j2}.
\]
Together with the shifted-complex differential it gives exactly \(\operatorname{DR}^0[r]\), including the divergence term. Affine global sections compute these terms. Thus (RF18) is the ordinary transfer direct image of GL-DMOD-08 extended to all unbounded complexes, not a newly assigned name for a different functor.

There is also its intrinsic induction check. Under (RF15), induction from ordinary right \(\mathcal O_X\)-modules is \(F\mapsto F\otimes_{\mathcal O_X}D_X\). The transfer computation gives
\[
p_*^{\mathrm{cr}}\operatorname{Ind}_W(F)
=
\operatorname{Ind}_Y(\operatorname{Res}_{A_Y}F),
\]
because \((F\otimes_BD_W)\otimes_{D_W}T_p
=F\otimes_{A_Y}D_Y\). On these regular affines restriction is the actual affine IndCoh direct image. This identifies the geometric pushforward's induction compatibility as well as its shifted smooth adjunction. Applying the free induction bar resolves arbitrary right crystals, so the compatibility includes all higher bar maps.

For \(\mathbb A^1\to\mathrm{pt}\), ordinary differentiation is surjective on \(k[x]\) with constant kernel. Accordingly ordinary pushforward of \(\mathcal O\) is \(k[1]\), and (RF18) gives exactly that answer on \(R_{\mathbb A^1}(\mathcal O)\). Unshifted left-crystal cohomology gives \(k\); the normalized realization accounts for the difference. The ordinary smooth \(!\)-pullback of \(k\) is \(\mathcal O[1]\), and its \([-2]\)-shift is \(\mathcal O[-1]\), as (RF17) requires. For \(\delta_0=D/Dx=k[\partial]v\), the shifted de Rham differential is multiplication by \(\partial\); it is injective with cokernel \(k\), giving \(p_*\delta_0=k\). For \(\mathbb G_m\), use \(d\log s\) and the Euler derivative on \(k[s,s^{-1}]\): it has constant kernel and constant cokernel, since every nonzero weight is invertible in characteristic zero. The pushforward of its constant connection is consequently \(k[1]\oplus k\). These checks distinguish the shifts and the multiplicative coordinate. The canonical-density flip and the shifted relative-form signs remain those already checked in the crystal review.

Multiplication on the additive or multiplicative affine groups in Lesson 5 becomes such a projection after its displayed algebraic coordinate change. Product projections in several blocks compose by tensoring their finite Spencer resolutions; their exterior/Koszul signs are the ordinary tensor signs. These constructions therefore apply to the finite-dimensional convolutions and transitions actually needed. They do not prove moving-point factorization, collision descent or renormalized infinite-dimensional pushforward.

The derived tensor–Hom, Ind-completion, compact coherent embedding, t-structure and mapping-space universal properties used in this construction are explicit categorical platform inputs. Their complete earlier programme proof chains remain certification obligations. The constructions above prove the specialized affine and projection statements within that platform; they do not certify arbitrary nonaffine, stack or infinite-dimensional pushforward.

##### 7.2.6.7. The finite right diagram and its standard realization

The presentation step has the following universal-property proof. Let \(\mathcal A\) be the chosen category of admissible derived affine tests, and let \(F:\mathcal A^{\mathrm{op}}\to\mathrm{Cat}_\infty\) be an actual functor. Define its prestack extension by
\[
\widehat F(Y)=\lim_{(S\to Y)\in(\mathcal A/Y)^{\mathrm{op}}}F(S).
\]
Then \(\widehat F\) sends colimits of prestacks on \(\mathcal A\) to limits of categories.

To prove this without an unsupported cofinality assertion, test the proposed categorical identity by maps from any category \(K\). Such a map is a compatible family of functors \(K\to F(S)\) over the elements of \(Y\), including all their higher compatibility data. This is equivalently a map of space-valued presheaves from \(Y\) into the presheaf \(S\mapsto\operatorname{Map}_{\mathrm{Cat}_\infty}(K,F(S))\). Mapping out of a presheaf colimit is the limit of these mapping spaces. Yoneda in \(\mathrm{Cat}_\infty\) gives the assertion. For a representable, the test diagram has its identity terminal in the affine-over-object category, so \(\widehat F(S)=F(S)\).

Apply this to the two explicit presentations proved in §7.2.1: \(G_p=\operatorname{colim}_n\operatorname{Spec}B_{p,n}\) and \(X_{\mathrm{dR}}=|G_\bullet|\). For the constructed \(F=\operatorname{IndCoh}^!\), it identifies the programme's right-Kan definition with precisely the finite-stage \(!\)-limit and nerve totalization constructed in §7.2.6. The finite maps in these presentations must use the actual adjoints to restriction of coherent complexes; those adjoints are constructed below. This bridge applies equally after restricting the prestack presentations to eventually coconnective finite-type affine tests.

Equations (RF9)–(RF13) construct that whole affine functor and identify its finite maps with the actual restriction adjoints. The prestack extension therefore uses these constructed transitions. For comparison of definitions, the free author edition [Gaitsgory–Rozenblyum, *Crystals and D-modules*, §§2.3 and 3.1](https://arxiv.org/pdf/1111.2087v4) defines right crystals by the same admissible-affine IndCoh data. Its citation supplies comparison and credit; the construction above supplies the local proof.

We give the comparison with right crystals, rather than silently replacing their realization by left crystals. Only the following explicit affine rings occur: the smooth ring \(A\) and the finite complete-intersection rings \(B_{p,n}\).

For a classical Noetherian ring \(C\), use
\[
\operatorname{IndCoh}(\operatorname{Spec}C)
=\operatorname{Ind}(D^b_{\mathrm{coh}}(C)),
\]
with the bounded coherent derived category as its full category of compact objects. For a finite map \(C\to C'\), restriction of scalars preserves bounded coherent objects, so it extends by colimits to \(f_*\) on these categories. Its right adjoint can be constructed by prescribing its restricted Yoneda functor on a compact object \(F\) as \(\operatorname{RHom}(f_*F,N)\). This exact functor is an object of the Ind category: the restricted Yoneda description of an Ind of a small stable category is obtained by expressing an exact functor as the filtered system of its finite representable approximations. Finite cones and sums make that approximation system filtered, and evaluation on each compact object verifies its colimit. This also proves the prescribed adjunction. The resulting \(f^!\) preserves colimits: testing a coproduct against any compact object reduces this assertion to compact preservation of \(f_*\), and stability then gives arbitrary colimits. Adjoints to successive restrictions compose, so these \(!\)-pullbacks have their coherent composition maps. For the affine functor constructed in (RF9)–(RF13), the right-Kan argument identifies its extension to (DC3) with the limit of these \(!\)-transitions. This is the right-crystal descent convention used here.

We record the elementary facts that make this concrete. The polynomial ring \(A\), and its indicated localization, are Noetherian. The usual leading-coefficient induction proves that if \(R\) is Noetherian then \(R[x]\) is Noetherian: the leading coefficients of an ideal form a finitely generated ideal, choose polynomials realizing generators, and repeatedly subtract their multiples until the remaining degree is below their maximum; the bounded-degree remainder is a submodule of a finite free \(R\)-module and is finitely generated. Start with \(k\); localization preserves finite generation of ideals.

Every \(A\)-module has projective dimension at most \(d\). In \(A\otimes_k A\), the coordinate differences are a regular sequence of length \(d\): after each quotient the ring is again a polynomial ring with the remaining coordinates, with the indicated invertible coordinates localized. Their Koszul complex resolves the diagonal \(A\) by the two-term induction just used. Viewed as a complex of right \(A\)-modules this augmented finite resolution splits: its terms are free, its last quotient \(A\) is projective, and successively its kernels are projective summands. Tensor it over that right copy with any module. The resulting length-\(d\) resolution has terms \(A\otimes_k M\), which are free on the left. In the localized case the same argument applies. For a finitely generated module choose finite free surjections successively; the Noetherian property makes all kernels finitely generated. After \(d\) steps the last kernel is projective: dimension shifting makes its \(\operatorname{Ext}^1\) against every module vanish; a free surjection onto it consequently has a split extension class. Thus bounded coherent complexes over \(A\) are perfect. Taking Ind and using the free module bar construction gives
\[
\operatorname{IndCoh}(X)=A\text{-}\mathrm{Mod}.        \tag{DC16}
\]

Let \(q_j:\operatorname{Spec}B_{p,n}\to X\) be any vertex map. Since \(B_{p,n}\) is finite free over that vertex \(A\), derived tensor–Hom adjunction shows
\[
q_j^!N=B_{p,n}^{\vee,j}\otimes_{A_j}^L N,
\qquad B_{p,n}^{\vee,j}=\operatorname{Hom}_{A_j}(B_{p,n},A_j),
                                                               \tag{DC17}
\]
as an object of \(\operatorname{IndCoh}(B_{p,n})\). To prove the formula first take \(N=A_j\) and test against a bounded coherent \(B_{p,n}\)-complex: both sides represent \(\operatorname{RHom}_{A_j}(q_{j,*}F,A_j)\). For arbitrary \(N\), resolve it by free \(A_j\)-modules and use continuity of \(q_j^!\). This proves the formula for unbounded \(N\), not only for coherent \(N\).

The coefficient pairing on truncated polynomials
\[
(b,c)\longmapsto
[\prod_{i,l}(h_i^{(l)})^{n-1}](bc)
\]
is a perfect \(A_j\)-pairing. Its matrix pairs each monomial with its complementary exponents. Consequently \(B_{p,n}^{\vee,j}\) is free of rank one over \(B_{p,n}\). Define its dualizing complex by
\[
\omega_{p,n}=q_j^!(\omega_X[d]).                     \tag{DC18}
\]
This definition is independent of the vertex, with the canonical coordinate-change identification. Here is an algebraic check. Embed the finite neighborhood in its smooth ambient coordinate product and resolve it by the Koszul complex for the powers of the differences. The top dual of that resolution is its ambient top differential line tensored with the inverse determinant of those equations, shifted by \(d\). The residue coefficient pairing above identifies this line with (DC18). Replacing vertex-zero coordinates by vertex-\(j\) coordinates is a triangular substitution with determinant one before the normal directions are removed. The same top Koszul pairing therefore gives the same dualizing line. For a different volume form multiply by its Jacobian; this is exactly its canonical differential-line transformation. These identifications compose because the determinant and the Koszul top pairing do.

The functor
\[
\Upsilon_{p,n}:B_{p,n}\text{-}\mathrm{Mod}
\to\operatorname{IndCoh}(B_{p,n}),
\qquad F\mapsto\omega_{p,n}\otimes_{B_{p,n}}^L F     \tag{DC19}
\]
is fully faithful on all complexes. Here is a proof avoiding an assumption that the singular finite neighborhood has \(\operatorname{IndCoh}=\operatorname{QCoh}\). Its object \(\omega_{p,n}\) is compact, since it is bounded coherent, and its endomorphism algebra is \(B_{p,n}\): it is a free rank-one module with a shift, so the derived endomorphism complex has no higher terms. Tensor–Hom adjunction gives the unit for (DC19). It is an equivalence on the free module \(B_{p,n}\), on its sums and shifts, and then on every DG module by its free bar resolution. Compactness makes Hom out of \(\omega_{p,n}\) commute with that realization. This proves full faithfulness. No essential-surjectivity assertion about (DC19) on a singular finite neighborhood is made.

Equations (DC17)–(DC19) give, for every unbounded \(M\),
\[
q_j^!(\omega_X[d]\otimes_A^L M)
\simeq\Upsilon_{p,n}(q_j^*M).                       \tag{DC20}
\]
For a transition between finite neighborhoods, or a nerve face after increasing its nilpotence bound, choose a vertex preserved by that map. The finite map is over this vertex copy of \(A\). Composition of its finite pushforward adjunctions gives
\(f^!\omega_{\mathrm{target}}=\omega_{\mathrm{source}}\).
The equality intertwines the action of the target coordinate ring with its image in the source ring. Therefore the two continuous functors
\[
f^!\Upsilon_{\mathrm{target}}\quad\text{and}\quad
\Upsilon_{\mathrm{source}}f^*
\]
agree on the free module of that target ring, on its ring action, and on all its free bar resolutions. They consequently agree on every module complex, including their maps. Independence of the chosen vertex is the Koszul/coordinate calculation after (DC18). These comparisons compose coherently because both are the same composed adjunction on the free generators, and the free bar extends their identity to all objects. Thus (DC20) and the fully faithful maps (DC19) pass to the complete formal nerve, including all coherences.

Every cartesian right-descent object is pulled from its degree-zero object along a vertex. By (DC16), that degree-zero object uniquely has the form \(\omega_X[d]\otimes M\). On every formal nerve term its component is therefore the right-hand side of (DC20). The fully faithful mapping-space identifications (DC19), and their compatibility just proved, transport all its descent equivalences and higher cocycles uniquely to left-descent data. Conversely left data gives those right data. We have proved
\[
\Upsilon_{X_{\mathrm{dR}}}:
\operatorname{QCoh}(X_{\mathrm{dR}})
\xrightarrow{\sim}\operatorname{IndCoh}(X_{\mathrm{dR}}),
\qquad
\operatorname{ev}_X\Upsilon(\Phi_X M)
=\omega_X[d]\otimes_A M.                           \tag{DC21}
\]
This proves the finite right-diagram comparison on its full derived groupoid and identifies it with the standard right-crystal category using the constructed admissible-affine functor.

#### 7.2.7. Canonical densities and dimension normalization

Ordinary side changing tensors a left module with the canonical **line**:
\[
M^r=\omega_X\otimes_A M.
\]
For a vector field \(\xi\) and a top form \(\rho\), its right action is
\[
(\rho\otimes m)\cdot\xi
=-\mathcal L_\xi(\rho)\otimes m-\rho\otimes\xi m.    \tag{DC22}
\]
In a coordinate volume frame this is \(\partial_i\mapsto-\partial_i\), with coordinates unchanged; it is the transposition anti-isomorphism of the Weyl algebra. Indeed the right relation \((m\partial_i)x_i-(mx_i)\partial_i=m\) follows directly from the left relation and the minus sign. For a volume rescaling \(\rho'=f\rho\), the first term of (DC22) supplies precisely the derivative of \(f\), so the formula respects the change of frame. The Lie identity follows by applying the commuting coordinate derivatives and then changing coordinates. Tensoring by the inverse line and using the reverse formula is an exact inverse. Thus (DC22) is an equivalence of all left and right DG-module categories and their derived mapping complexes.

In the frame \(ds\) on the multiplicative line, right \(\theta\) is \(-\theta-1\); in the invariant frame \(ds/s\), its divergence is zero and right \(\theta\) is \(-\theta\). These are the same canonical-line equivalence in two frames. This distinguishes a genuine density correction from a change of spectral sign.

The crystal comparison (DC21) instead tensors with \(\omega_X[d]\). Therefore the ordinary right module \(\omega_X\otimes M\), in its usual cohomological degrees, corresponds to
\[
\Upsilon_{X_{\mathrm{dR}}}\bigl(\Phi_X(M)[-d]\bigr).  \tag{DC23}
\]
The shifts in (DC23) cancel on evaluation. Together with (RF15)–(RF18), this is the dimension normalization for geometric right-crystal convolution written in ordinary left-module notation.

On a product, canonical lines are identified by wedging the top-form blocks. Exchanging dimension-\(d\) blocks introduces \((-1)^{d^2}=(-1)^d\). Transport of geometric symmetry through (DC22) retains this density sign. For a relative de Rham \(q\)-form in a convolution fibre the flip additionally contributes \((-1)^q\). After the direct-image shift \([d]\), their product \((-1)^{d+q}\) equals the spectral Koszul sign \((-1)^{d-q}\). This recovers the sign required in the local Fourier calculation below. The same rule covers an invariant logarithmic density in the multiplicative coordinate.



#### 7.2.8. All-unbounded ordinary direct image

Let \(W=Y\times V\) and \(p:W\to Y\) be an affine product projection, where the rings of \(Y,V\) are polynomial rings with the indicated invertible coordinates, and \(\dim V=r\). Write \(C=\Gamma(W,\mathcal O_W)\) and let \(D_W,D_Y\) be their differential-operator algebras. The transfer bimodule is
\[
T_p=C\otimes_{\Gamma(Y,\mathcal O_Y)}D_Y.
\]
It is resolved by the relative Spencer complex
\[
D_W\otimes_C\bigwedge^j T_{W/Y},\qquad -r\le -j\le0.
\]
In commuting vertical coordinates its differential is the signed sum of right multiplications by the vertical derivatives. Its augmentation sends an operator to its class in \(T_p\). Filter degree \(-j\) by operator order at most \(q-j\). The associated graded augmented complex is the Koszul complex of the vertical symbol variables in the polynomial symbol ring. They form a regular sequence: quotienting successively leaves a polynomial ring in the remaining variables, with the prescribed localization.

The Koszul complex is exact by induction on this sequence. A cycle in the original Spencer complex has finite operator order. Lift a boundary for its leading symbol and subtract it. Each subtraction lowers that finite filtration degree, so the process terminates. This proves the resolution's exactness. Its length is \(r\), and each term is a finite free left \(D_W\)-module. Thus it is K-flat and computes the derived transfer tensor with **every** unbounded right DG \(D_W\)-module \(Q\). Tensoring gives a double complex with only \(r+1\) Spencer degrees, so totalization involves finitely many terms in each internal degree. No boundedness or convergence hypothesis is introduced.

Change sides using the canonical line. Contraction with the relative top form identifies the degree \(-j\) term with \(\Omega^{r-j}_{W/Y}\otimes M\), for the corresponding left module \(M\). The actual earlier sign computation multiplies contraction by
\[
(-1)^{j(r-1)+\binom j2}.
\]
It carries the Spencer differential, including volume divergence, to the shifted relative de Rham differential. For the affine product there is no sheaf-cohomology obstruction: these quasi-coherent terms are computed by their module global sections. We conclude for arbitrary unbounded DG \(M\)
\[
p_{\mathrm{DR},*}^{\mathrm{ordinary}}(M)
=\Gamma\!\left(W,\operatorname{DR}_{W/Y}^0(M)\right)[r],
\]
with the residual \(D_Y\)-action. This extends the bounded assertion of GL-DMOD-08 §2, Theorem 2.1, by the finite K-flat resolution argument just given. It does not cite the bounded theorem as though it already had all-unbounded scope.

There is also a useful all-unbounded adjunction check. The left \(D_V\)-module \(\mathcal O_V\) has the bounded finite-free vertical Spencer resolution. For a \(D_Y\)-module \(N\), tensoring that resolution with \(N\) and applying derived Hom yields
\[
\operatorname{RHom}_{D_W}
 \bigl(\mathcal O_V\otimes_k N[-r],M\bigr)
\simeq
\operatorname{RHom}_{D_Y}
 \bigl(N,\operatorname{DR}_{W/Y}^0(M)[r]\bigr).
\]
The bounded free resolution again justifies this for unbounded \(M,N\). Hence the ordinary direct image is right adjoint to the ordinary smooth functor \(p^![-2r]=\mathcal O_V\otimes_k-[-r]\).

Equations (RF16)–(RF18) construct the geometric smooth pullback and the right adjoint of its \([-2r]\)-shift. The bounded Spencer mapping-complex adjunction and independent transfer calculation identify that adjoint with this ordinary direct image on all unbounded complexes, retaining both module actions. Thus the positive-dimensional comparison follows from an actual shifted geometric adjunction.

A degree test prevents a normalization shortcut. For \(V=\mathbb A^1\),
\[
p_{\mathrm{DR},*}^{\mathrm{ordinary}}\mathcal O_V=k[1],
\]
because differentiation on \(k[x]\) is surjective with constant kernel. Unshifted left-crystal cohomology gives \(k\). The dimension normalization is essential, and cannot be supplied just by calling both functors “pushforward”.


#### 7.2.9. The three algebra equivalences

We use left connections for the algebra calculation. Using the standard right realization and geometric projection comparison proved in §§7.2.6–7.2.8, the canonical-bundle identification transports the geometric convolution and its symmetry to this calculation. Ordinary direct image along a smooth affine projection of relative dimension \(r\), proved in §7.2.8, is the relative de Rham complex shifted by \([r]\). Convolution in this convention has the ordinary delta object at the identity as its unit, and the Koszul complex for a relative derivative lies in degrees \(-1,0\). The transported symmetry includes the canonical-bundle sign computed above.

First, D-modules on \(\underline{\mathbb Z}\) are families \((M_m)\) of complexes. A quasicoherent sheaf on \(B\mathbb G_m\) is a Laurent-polynomial comodule, equivalently a family of weight complexes. Indeed every coaction has a finite expansion on each vector, and coassociativity extracts its unique weight components. Assign \(M_m\) to weight \(m\). Convolution takes
\[
(M*N)_r=\bigoplus_{m+l=r}M_m\otimes_kN_l;
\]
tensor product of weight representations has the identical formula. This proves the monoidal equivalence, including arbitrary infinite families and the weight-zero unit.

Second, the algebra of global differential operators on \(\mathbb G_m\) is
\[
\mathcal W_\times
 =k\langle s,s^{-1},\theta\rangle/
       (\theta s-s\theta-s),\qquad \theta=s\partial_s.
\]
A quasicoherent D-module on this affine scheme is precisely a DG module over this algebra. A quasicoherent sheaf on \([\mathbb A^1/\mathbb Z]\) is a \(k[a]\)-module with an invertible semilinear operator \(S\) satisfying
\[
aS=S(a-1).
\]
This is descent along the action groupoid; its cocycle requires \(S^rS^l=S^{r+l}\). The assignments
\[
a=-\theta,\qquad S=s                                   \tag{L4}
\]
identify the two module categories, including their derived mapping complexes. They identify the defining algebras, so no finite-dimensional or regular-singular restriction is imposed.

For convolution, change coordinates on \(\mathbb G_m^2\) to \(z=s_1s_2\) and \(v=s_1\). The relative Euler derivative is \(\theta_1-\theta_2\), the output Euler derivative is \(\theta_2\), and multiplication by \(z\) is \(s_1s_2\). Relative direct image is therefore the Koszul cofiber of \(\theta_1-\theta_2\) acting on \(M\otimes_kN\). Under (L4), this is the derived tensor product over \(k[a]\); its semilinear operator is \(S_M\otimes S_N\). This is exactly the tensor product of the two descended sheaves. The delta object at \(s=1\) is \(k[\theta]\), with \(s f(\theta)=f(\theta-1)\), and becomes the equivariant structure sheaf \(k[a]\). This checks the unit and its normalization.

Third, for one additive jet coordinate the Weyl algebra is
\[
\mathcal W_+=k\langle b,\partial_b\rangle/
                  (\partial_b b-b\partial_b-1).
\]
Fourier transform is the algebra isomorphism
\[
\partial_b\longmapsto-a,\qquad
b\longmapsto\partial_a.                               \tag{L5}
\]
The relation is preserved since \([-a,\partial_a]=1\). The inverse sends \(a\) to \(-\partial_b\) and \(\partial_a\) to \(b\). It therefore proves an equivalence on all DG modules.

For ordinary quasicoherent modules, crystals on \((\mathbb A^r)_{\mathrm{dR}}\) are the same as quasicoherent left D-modules on \(\mathbb A^r\). On the infinitesimal diagonal, put \(h_i=x_i'-x_i\). A crystal's comparison is uniquely
\[
m\longmapsto
 \sum_I\frac{h^I}{I!}\nabla^I(m).
\]
Modulo any power of the diagonal ideal this is a finite sum. The cocycle on three infinitesimally close points is equivalent to commuting \(\nabla_i\), and compatibility with multiplication is equivalent to
\(\nabla_i(fm)=\partial_i(f)m+f\nabla_i(m)\).
These are precisely the Weyl algebra relations. Conversely these relations give the displayed comparison at every finite infinitesimal order, with its inverse obtained by replacing \(h\) by \(-h\). They are compatible as the order increases and thus define the ordinary crystal. No convergence or finite-rank assumption enters this heart-level calculation. On an affine space quasicoherent left D-modules, and their unbounded derived category, are recovered from modules over the Weyl algebra. This latter affine algebra assertion does not by itself identify the unbounded derived formal-groupoid descent category.

**Derived-crystal comparison lemma (remaining proof obligation).** The evaluation functor from \(\operatorname{QCoh}((\mathbb A^r)_{\mathrm{dR}})\), defined by derived prestack descent, to \(\operatorname{QCoh}(\mathbb A^r)\) is conservative and preserves colimits, has the differential-induction left adjoint, and its monad is the Weyl algebra. Its adjunction bar construction gives an equivalence on all unbounded complexes, including their mapping complexes. The ordinary Taylor formula above verifies the proposed action in the heart. A complete proof must still establish the derived adjunction/monad and its bar unit and counit. Until that is supplied, the use of this lemma in (L7)–(L8) is conditional.

For additive convolution, use \(z=b_1+b_2\), \(v=b_1\). The relative derivative is \(\partial_1-\partial_2\); the output derivative is \(\partial_2\), and the output coordinate is \(b_1+b_2\). After (L5), its Koszul cofiber is the derived tensor product over \(k[a]\), the output spectral coordinate is \(a\), and its connection derivative is \(\partial_{a_1}+\partial_{a_2}\). This is the tensor product connection. The delta object at \(b=0\) transforms into the trivial connection on the dual line. For \(r\) coordinates use the tensor product of these algebras and the \(r\)-variable Koszul complex. The identification is independent of the order of the coordinates, including the usual Koszul signs.

Here is the density sign in the symmetry comparison. For a group of dimension \(r\), the identification of a left module with a right module tensors by its top differential line. On the product of two groups, these lines are identified by wedging the two blocks of \(r\) forms. Exchanging the blocks multiplies this identification by \((-1)^{r^2}=(-1)^r\). The symmetry transported to the left-module convolution therefore includes this factor in addition to the usual signs of the two coefficient complexes.

In the addition coordinates \(z=b_1+b_2,v=b_1\), exchange sends the relative coordinate to \(z-v\). On relative \(q\)-forms it acts by \((-1)^q\). The total sign on the relative de Rham complex is consequently \((-1)^{r+q}\). This complex is shifted by \([r]\), and a \(q\)-form corresponds to the homological Koszul degree \(r-q\) resolving the spectral diagonal. Its tensor-product symmetry has precisely \((-1)^{r-q}\); the two signs agree. For multiplicative coordinates \(z=s_1s_2,v=s_1\), exchange sends \(v\) to \(z/v\) and \(d_{\mathrm{rel}}\log v\) to its negative, so the identical calculation applies. Tensoring the additive and multiplicative blocks gives the general finite-level calculation. A useful test is the additive constant connection: its convolution with itself is \(\mathcal O_{\mathbb A^1}[1]\), and the transported flip on its degree-\(-1\) class is negative, just as the flip on the degree-\(-1\) Tor class of the two spectral delta modules. Omitting the density factor would incorrectly give a positive flip.

For three or more inputs, either parenthesization resolves the same diagonal equalities between the spectral coordinates by the same Koszul complex, and the output semilinear operator or connection is the diagonal one. The augmentation to the derived tensor product identifies these comparisons. Adjacent transpositions have the signs just computed; composing them is the determinant rule for permuting the form blocks, so they obey the permutation relations and the symmetry hexagon. The identity delta gives the structure sheaf. Its relative top-form sign cancels the density sign, and its unit comparisons are the structure-sheaf multiplication comparisons. This proves the associativity, symmetry and unit compatibility in the stated geometric convention.

### 7.3. Finite congruence level and the full limit

Pair the jet coordinate \(b_j\) with the coefficient \(a_j\) of \(t^{-j-1}dt\) by
\[
\operatorname{Res}\left(
  \left(\sum_{j=1}^{n-1}b_jt^j\right)
  \left(\sum_{j=1}^{n-1}a_jt^{-j-1}dt\right)\right)
       =\sum_{j=1}^{n-1}b_ja_j.                       \tag{L6}
\]
Combine the weight equivalence, (L4), and (L5) in this order. Using the standard right realization and geometric projection comparison proved in §§7.2.6–7.2.8, equations (L2)–(L3) give a symmetric monoidal equivalence
\[
D(L\mathbb G_m/K_n)
\simeq
\operatorname{QCoh}
   (\operatorname{LocSys}^{\le n}_{\mathbb G_m}(D^\times)).
                                                               \tag{L7}
\]
The tensor product of categories here does not need a Künneth theorem as an unproved input: the coordinate D-algebra is the tensor product of the displayed algebras, the discrete factor is a family of such modules, and the spectral descent gives exactly the same algebra and family description.

When \(n\) increases by one, the automorphic transition forgets the last additive jet and takes its normalized de Rham direct image. Under (L5) this is the Koszul complex for multiplication by the last \(a\), hence derived restriction to \(a=0\). That is pullback from pole bound \(n+1\) to pole bound \(n\). Its connection operators and all other factors remain the ones displayed above. Thus (L7) identifies the actual transition functors, not just their individual categories.

Use the convention
\[
D^*(L\mathbb G_m)=
   \lim_{n\ge1,\ q_{\mathrm{dR},*}}
                  D(L\mathbb G_m/K_n).
\]
Every meromorphic connection has bounded pole order locally on its test scheme; the full spectral prestack is the colimit of the bounded-pole substacks. Quasicoherent sheaves on a prestack, defined by descent over all its affine test schemes, send this colimit to the limit of the categories with pullback transitions. Taking limits of (L7) therefore gives
\[
D^*(L\mathbb G_m)
\simeq\operatorname{QCoh}
       (\operatorname{LocSys}_{\mathbb G_m}(D^\times)). \tag{L8}
\]
Convolution and tensor product are compatible with the transition functors already checked; the coherent monoidal comparisons pass to this limit. This proves the formal passage to the full local assertion in the stated \(D^*\) convention, within the categorical platform whose recursive proof obligations are recorded above.

### 7.4. The pairing, signs and a torus

The residue calculation also identifies the geometric kernel and its gauge descent. If \(u=t^ms\exp(b_++b_-)\) and \(g=t^nc\exp(c_++c_-)\), define
\[
\langle u,g\rangle
 =(-1)^{mn}s^nc^{-m}
 \exp\operatorname{Res}
       (b_+\,dc_- - c_+\,db_-).                       \tag{L9}
\]
The negative coefficients are nilpotent, so the exponential in (L9) is well-defined by a finite nilpotent expansion on every test algebra. The formula is bimultiplicative: valuations add, constant coefficients multiply, logarithms add, and every exponent is bilinear. Its two unit identities follow by setting one factor to \(1\).

Differentiating (L9) in the parameter \(u\), with \(g\) fixed, gives
\[
d_u\log\langle u,g\rangle
 =\operatorname{Res}(d_t\log g\,d_u\log u).            \tag{L10}
\]
For the negative term, use
\(\operatorname{Res}d_t(c_+d_ub_-)=0\) to integrate by parts; the constant term contributes \(n\,d\log s\). This proves (L10) directly. It implies that the universal connection
\[
d-\operatorname{Res}(\omega\,d_u\log u)
\]
descends under the gauge arrow \(\omega\to\omega+d_t\log g\) by the horizontal map from the old connection to the new one which multiplies by \(\langle u,g\rangle\). Indeed the new one-form is the old one-form minus \(d_u\log\langle u,g\rangle\); the Leibniz rule checks horizontality of this map. The forward dual kernel has the inverse horizontal map, multiplying by \(\langle u,g\rangle^{-1}\), and gives (L4)–(L5). Our \(B\mathbb G_m\) coordinate uses the actual gauge automorphism \(g=c\). Since \(\langle t^m,c\rangle=c^{-m}\), its action on that forward kernel is \(c^m\), explaining weight \(m\). A comparison in the reverse direction has the reciprocal multiplier and must not be mistaken for this representation action. At \(\omega=a\,dt/t+\sum a_jt^{-j-1}dt\) the dual kernel has form
\[
d+a\,d\log s+\sum_j a_j\,db_j.
\]
The Koszul integrations above identify its transform with the algebra functor. A flat line \(d-a\,d\log s\), or \(d-a_j\,db_j\), therefore goes to the indicated spectral parameter rather than its negative. Composing with inversion on the dual torus changes all those parameters and weights together. A comparison with a different Hecke-arrow convention must record that inversion explicitly, as in Lesson 6.

For a split torus \(T\), apply this calculation to its character and cocharacter lattices. A choice \(T\simeq\mathbb G_m^r\) gives the product of (L7) or (L8). The resulting functor is independent of the basis: the constant loop differential operators transform by the integral change-of-basis matrix, the residues by its dual, and the jet Fourier operators by the same dual vector-space pairing (L6). Formula (L9) is evaluated through the intrinsic pairing
\(X_*(T)\otimes X^*(T)\to\mathbb Z\); each bilinear term and the corresponding descent multiplier are invariant under those paired changes. Thus the identified kernel and functor agree on basis overlaps. Since a torus over the algebraically closed field is split, this extends the conditional fixed-disc statement to the tori of the lesson.

We prove coordinate independence of the entire symbol (L9); its individual factors need not be invariant. First let \(u\) have valuation zero, and write \(u=s\exp(b_++b_-)\). Its logarithm after dividing by \(s\) exists in the sum of the positive-power completion and the nilpotent negative-power part. Integration by parts gives
\[
\langle u,g\rangle
 =s^n\exp\operatorname{Res}\bigl(\log(u/s)\,d_t\log g\bigr),
\qquad n=\operatorname{val}(g).
\tag{L11}
\]
Indeed the two mixed terms of this residue are the exponent in (L9), and all same-sign terms and the \(dt/t\) term of the zero-constant logarithm have zero residue.

After a change of parameter, the new normalized constant \(s'\) differs from \(s\) by a nilpotent unit. Reduction removes every negative coefficient, and the constant term of a positive series is unchanged by a change of parameter, proving this assertion. Put \(c=\log(s'/s)\), a finite nilpotent logarithm. The two formal logarithms satisfy
\(\log(u/s')=\log(u/s)-c\).
Residue is invariant under formal change of parameter, and \(\operatorname{Res}d_t\log g=n\); therefore the residue exponent in (L11) decreases by \(nc\), while the factor \(s^n\) increases by \(\exp(nc)\). They cancel. This proves invariance whenever the first loop has valuation zero.

Formula (L9) is antisymmetric:
\(\langle u,g\rangle\langle g,u\rangle=1\).
For a uniformizer \(t\), \(\langle t,t\rangle=-1\) in every parameter: write \(t=\tau w\) with \(w\) of valuation zero, use bimultiplicativity, cancel the two mixed factors by antisymmetry, and note that \(\langle w,w\rangle=1\). For arbitrary \(g=t^n v\), the symbol \(\langle t,g\rangle\) reduces to \((-1)^n\langle v,t\rangle^{-1}\), which is invariant by the valuation-zero case. Finally every \(u=t^m w\) reduces to that case and this uniformizer case. This proves invariance for all loops and hence gluing of the kernel under changes of parameter. The cancellation is essential; for example \(u=1-\varepsilon/t\) with \(\varepsilon^2=0\) and \(\tau=t/(1+ct)\) changes the constant term to \(1+\varepsilon c\), which cancels the changed residue exponential.

**Remaining relative obligation.**

This argument proves the finite-congruence algebra, its monoidal calculation with density signs, the compatible formal limit, and the bimultiplicative kernel. Section 7.2 proves the all-unbounded left affine crystal comparison, constructs admissible-affine exceptional pullback and the standard right realization, and identifies geometric projection pushforward. The exact recursive categorical platform remains a programme certification obligation. A further obligation is the relative kernel over the whole Beilinson–Drinfeld configuration space: its equivalence of lax-unital factorization categories must extend across moving-point collision strata. Chinese remainders prove the disjoint-point product rule, and (L9) gives its kernel comparison; the relative equivalence and its collision and unit descent are still needed for the full diagram (7.2).

Comparison sources actually read: Hilburn–Raskin, *Tate's thesis in the de Rham setting*, arXiv:2107.11325v1, rank-one normal forms and §5.3; Campbell–Raskin, *Langlands duality on the Beilinson–Drinfeld Grassmannian*, arXiv:2310.19734, §§7.3–7.6. Neither citation substitutes for the algebra proof above or closes the remaining relative obligation.

### 7.5. Identifying the exponential kernel on every DG module

Let \(M\) be any DG module over the Weyl algebra in variables \(b_1,\ldots,b_r\), and write \(D_i\) for its commuting derivative operators. Tensor with the forward exponential connection \(d+\sum_i a_i\,db_i\). The normalized relative de Rham direct image is the Koszul complex on
\[
M[a_1,\ldots,a_r],\qquad T_i=D_i+a_i,
\]
in degrees \(-r,\ldots,0\). The operator
\[
U=\exp\left(\sum_iD_i\partial_{a_i}\right)
\]
is well defined on this polynomial module: every summand of sufficiently high order kills a fixed polynomial. It commutes with the DG differential, has the exponential with the opposite sign as inverse, and satisfies \(Ua_iU^{-1}=a_i+D_i\). It conjugates the displayed Koszul complex to that for multiplication by the \(a_i\).

Those multiplications are successively injective, with quotients deleting the corresponding polynomial variable. The Koszul augmentation is therefore a quasi-isomorphism to \(M\) in degree zero. This remains true for an unbounded complex: the Koszul complex has only finitely many columns, and the conjugation and quotient are chain maps. Under the augmentation, \(a_i\) acts by \(-D_i\). The output operator \(\partial_{a_i}+b_i\) commutes with every \(T_j\), and induces \(b_i\) on constant representatives. This proves precisely the Weyl-algebra transport \(\partial_{b_i}\mapsto-a_i\), \(b_i\mapsto\partial_{a_i}\), including its geometric exponential-kernel description.

The one-variable multiplicative calculation uses \(T=\theta+a\) on \(M[a]\). The same finite polynomial conjugation proves the augmentation. The operator \(P(a)m\mapsto P(a+1)sm\) commutes with \(T\), and induces \(S=s\) on its quotient. Thus its output satisfies \(aS=S(a-1)\). When identifying descent with actual gauge arrows, specify whether the comparison is from the new fibre to the old one or its inverse; these two maps have reciprocal multipliers.

This argument identifies the kernel functor once the geometric source and target have been identified with the indicated affine DG-module categories. It does not establish that remaining identification.

### 7.6. Residue invariance under a change of parameter

A fixed-disc change of parameter preserves its marked section: \(t=\tau w(\tau)\), with \(w\in R[[\tau]]^\times\). For \(j\neq-1\), \(t^jdt=d(t^{j+1}/(j+1))\), and the derivative of any Laurent series has zero residue. For \(j=-1\),
\[
dt/t=d\tau/\tau+d\log w.
\]
The second term is a regular form, so its residue is zero and the first has residue one. This proves invariance on Laurent monomials; the negative part is finite and a positive series contributes no negative terms after this section-preserving substitution, so it proves the complete rule. The same proof covers nilpotent constant displacement when that broader substitution is intended, using the Laurent logarithmic normal form of \(w\) to obtain \(\operatorname{Res}d\log w=0\); a bounded finite pole/finite nilpotence calculation justifies each residue coefficient. Such displacement moves the marked section and must not be confused with an automorphism preserving every \(K_n\).

### 7.7. The relative factorization statement

For general \(T\), [Campbell–Raskin §7.3, Theorem 7.3.2, and §7.6](https://arxiv.org/abs/2310.19734) give the factorization version and its fibre at \(x\). The hypotheses are a smooth curve over an algebraically closed characteristic-zero field and a torus \(T\). Their space \(\operatorname{Gr}_T^{\infty\cdot x}\) is the Beilinson–Drinfeld torus Grassmannian with full level structure at \(x\); its fibre at \(x\) is \(LT\). Their spectral space \(\operatorname{LocSys}_{\check T}(D)^{x\mathrm{ram}}\) permits meromorphic connections and gauge transformations at that point. The assigned relative theorem asserts an equivalence of commutative algebra objects in factorization categories with lax unital morphisms and commutes with
\[
\begin{array}{ccc}
\operatorname{Dmod}(\operatorname{Gr}_T^{\infty\cdot x})
 &\longrightarrow&
\operatorname{QCoh}(\operatorname{LocSys}_{\check T}(D)^{x\mathrm{ram}})\\
\downarrow{p_{\mathrm{dR},*}}&&\downarrow{\iota^*}\\
\operatorname{Dmod}(\operatorname{Gr}_T)
 &\longrightarrow&
\operatorname{QCoh}(\operatorname{LocSys}_{\check T}(D)).
\end{array}                                                    \tag{7.2}
\]
Here \(p\) forgets level structure and \(\iota\) includes unramified connections. The monoidal and factorization units have distinct comparison maps; the source's remarks in §§7.2–7.3 keep that distinction explicit. Its functor is constructed from the Contou–Carrère bimultiplicative pairing. The fixed-disc algebra proof below advances the first assertion. The relative enhancement, including collision strata and lax units, still needs its own proof. Fibrewise checks cannot establish diagram (7.2).

## 8. Exercises and complete solutions

**Exercise 8.1 (easy).** Prove the large-degree Abel–Jacobi fibre formula, identify the vector bundle in its family version, and state the genus-zero qualification.

**Solution 8.1.** If \(d>2g-2\), then \(\deg(\omega_XL^{-1})<0\), so Serre duality gives \(H^1(X,L)=0\). Riemann–Roch gives \(h^0(X,L)=d+1-g\). A divisor in the fibre is the zero divisor of a nonzero section of \(L\) up to scalar, so the fibre is the projective space of lines in this vector space, of dimension \(d-g\). For \(d\ge0\) its rank is positive. With the normalized Poincaré family, base change gives the bundle \(p_*\mathcal L_d\); sections and relative Cartier divisors identify the full map with its projective bundle of lines, as in Proposition 1.1. In genus zero we start at \(d=0\); the inequality alone would also permit \(d=-1\), which is outside the defined symmetric powers.

**Exercise 8.2 (easy).** Compute \(C_E\) and the downward eigensheaf for \(X=\mathbb P^1\), including a Weil structure with Frobenius \(\alpha\).

**Solution 8.2.** The two-chart connection calculation forces the underlying flat line to have degree zero. Its remaining global connection form vanishes, so \(E\) is a constant line \(V\). Since \(P^d\) is a point, symmetric-power descent gives \(C_E^d=V^d\) for \(d\ge0\). The unit and multiplication extend the same formula to all integers. The downward object is \(A_E^d=V^{-d}\), so translating from \(d\) to \(d-1\) tensors it with \(V\). Frobenius \(\alpha\) on \(V\) gives traces \(\alpha^d\) for \(C_E\) and \(\alpha^{-d}\) for \(A_E\). Therefore \(f_{A_E}(d-1)=\alpha f_{A_E}(d)\); at a degree-\(e\) place the eigenvalue is \(\alpha^e\). The scalar on \(C_E\) is the inverse for the same downward operator.

**Exercise 8.3 (medium).** Explain why \(E^{(d)}\) is lisse at repeated divisors and why it descends along large-degree Abel–Jacobi. Do not infer descent solely from a calculation of one fibre.

**Solution 8.3.** At \(\sum_i n_ix_i\), the stabilizer \(\prod_iS_{n_i}\) permutes identical rank-one factors trivially. In local product frames the quotient line has fibre \(\bigotimes_iE_{x_i}^{n_i}\). For the connection, the clustered form \(\sum_j f(t_j)dt_j\) equals \(d\sum_jF(t_j)\) formally. The latter sum is symmetric and hence a formal function of elementary symmetric coordinates; its differential is regular on the quotient. The descended form therefore extends across all diagonals, proving lissity. In the complex local-system picture this is the constant line on the corresponding symmetric polydiscs.

When \(d\ge d_0\), Proposition 1.1 supplies an entire projective bundle, not merely set-theoretic projective fibres. A flat line on each projective space is trivial by Lemma 3.1. Base change makes its pushforward a line bundle and evaluation recovers the original line. Pushing the connection via \(p_*\Omega^1_Z=\Omega^1_B\) gives its flat connection on the base. Full faithfulness gives the unique descended connection with the specified pullback identification. These relative statements establish descent and allow the subsequent eigenmaps to descend.

**Exercise 8.4 (medium).** Prove uniqueness of the multiplicative local system with its unit and specified positive-Abel identification. Explain the automorphism ambiguity when that identification is omitted.

**Solution 8.4.** Multiplication and the Abel identification determine its pullback to \(X^d\) as \(E^{\boxtimes d}\), compatibly with permutations. Thus its pullback to \(X^{(d)}\) is the specified \(E^{(d)}\). For \(d\ge d_0\), fully faithful Abel–Jacobi pullback identifies it uniquely with \(C_E^d\). For any integer \(d\), choose \(N\) with \(d+N\ge d_0\); multiplication by \(\mathcal O(Nx_0)\) identifies it with the translated large-degree object tensored with \(E_{x_0}^{-N}\). This is forced by its Abel map and agrees with (4.1). The symmetric-power grouping makes these comparisons transitive and multiplicative, proving uniqueness in all degrees.

For the ambiguity, each \(P^d\) is connected, so an automorphism of its rank-one connection is a constant scalar \(c_d\). The unit forces \(c_0=1\) and multiplication forces \(c_{a+b}=c_ac_b\). Hence \(c_d=c_1^d\). Fixing the Abel comparison makes \(c_1=1\), leaving only the identity. Without it, this scalar freedom remains even though the underlying isomorphism class is determined.

**Exercise 8.5 (hard).** Construct the multiplication and strong Hecke maps in arbitrary degrees from the large-degree descent. Check independence of translating integers, associativity, collisions, and the course's eigenvalue direction.

**Solution 8.5.** In large degrees \(a,b\), pull multiplication back along \(\operatorname{AJ}_a\times\operatorname{AJ}_b\). Symmetric addition identifies the pullback of \(C_E^{a+b}\) with \(E^{(a)}\boxtimes E^{(b)}\). Full faithfulness descends this identification, giving (3.3). Pulling the moving positive Hecke map back along \(\operatorname{AJ}_a\times1_X\) similarly gives addition of one point and hence (3.4).

For arbitrary \(a,b\), translate by \(Nx_0,Mx_0\) to large degrees and use (4.1). The tensor-product equality \(\tau_N(L)\otimes\tau_M(M)=\tau_{N+M}(L\otimes M)\) cancels the constant fibres \(E_{x_0}^{N+M}\) and gives (4.3). Increasing \(N\) or \(M\) adds an \(x_0\)-factor to the same grouping map on symmetric powers, so both definitions agree through the canonical transition maps. For any associativity or symmetry diagram, translate all its finitely many degrees high enough. Fully faithful pullback identifies the diagram with regrouping or permuting the same rank-one tensors, so it commutes. The cluster calculation in Lemma 2.1 supplies the identical statement on collision loci. The unit is the cancellation at the divisor \(Nx_0\).

For the Hecke map, commute translation with \(L\mapsto L(x)\) and cancel \(E_{x_0}^N\); this gives (4.2) in all degrees. Substituting \(L(-x)\) gives (5.1), with eigenvalue \(E^{-1}\) on \(C_E\). Replacing \(E\) by \(E^{-1}\) gives the desired \(E\)-eigenobject \(A_E\). For weight \(m\), iterate tensoring by \(\mathcal O(-x)\), using its inverse for negative \(m\); multiplication and its symmetry supply exactly the weight-addition and factorization coherences of (5.2).

## 9. Proof status and sources

The geometric construction includes symmetric-power line and connection descent, the relative projective-bundle connection proof, all-degree translation maps, multiplicativity, the unit, and uniqueness with the specified Abel comparison. The arithmetic arguments now include projective-space finite covers in every characteristic, relative finite-cover and lisse/Weil descent, lissity across collisions without averaging, the Lang character line, its normalized uniqueness, rational Picard-point descent, the converse construction even without a rational point, and the precise unit-valued continuity condition. The local calculation includes all DG modules over the explicit affine algebras, the convolution density signs, finite-level transitions, the Contou–Carrère kernel and its coordinate invariance.

The lesson remains under proof repair. Its geometric and arithmetic constructions use the following outstanding foundations: the full Picard representability, abelian-variety and Poincaré geometry; the finite symmetric quotient of a curve and its orbit fibres; and the complete earlier chains for curve duality, projective coherent cohomology/base change, module descent, henselizations and the étale Jacobian criterion. The named actual AG-QC-04/05/08/09/14, AG-ET-06/07/08/11, AG-LTF-01 and AG-DFG-02 arguments have matching locators in the proofs above, but their unfinished transitive imports are not certified by this lesson. AG-GS-06 excludes Picard schemes and dual abelian varieties and supplies no proof of that geometry. Section 3.2 proves the finite-cover, finite-local-system and profinite fibre-functor comparisons on Noetherian bases, replacing the external import in AG-ET-11 equation (2.1). Its trace-idempotent, ordering-cover and pointed-Galois constructions are explicit. Its supporting étale-flatness, openness, faithful-flat descent, relative-spectrum and adic-module proofs have actual matching programme locators, but their complete recursive algebra and scheme foundation chains still require review. The general non-Noetherian profinite comparison is not claimed.

Section 7.2 now proves the all-unbounded left affine crystal comparison, its coherent induction adjunction and free-bar generation, and the ordinary finite-Spencer direct image. The finite right diagram and density shifts are checked. Sections 7.2.6.1–7.2.6.6 construct the whole admissible-affine IndCoh ! functor, finite-map adjunction, higher composition coherence and geometric projection compatibility at the exact displayed shifts. These specialized proofs use the categorical platform of derived tensor–Hom, Ind-completion, compact coherent embedding, t-structures and mapping-space universal properties; its complete earlier programme foundation chains remain open. The stated general theorem in GL-DMOD-17 is not a substitute for those proofs. The relative Beilinson–Drinfeld enhancement in §7.7 requires moving-point and collision descent, relative kernel duality, renormalized spectral pushforward, factorization coherences and lax-unit comparisons. These are mathematical proof obligations, not conjectural exceptions, and neither the algebra equivalence nor a source citation discharges them. No categorical equivalence for general reductive groups follows from this rank-one construction.

The human sources are the free author editions of [Frenkel, *Lectures on the Langlands program and conformal field theory*, §§4.1–4.3](https://arxiv.org/abs/hep-th/0512172), [Hilburn–Raskin, *Tate's thesis in the de Rham setting*, §5.3, v1](https://arxiv.org/abs/2107.11325v1), [Campbell–Raskin, *Langlands duality on the Beilinson–Drinfeld Grassmannian*, §§7.3–7.6](https://arxiv.org/abs/2310.19734), and [Forey–Fresán–Kowalski, *Arithmetic Fourier transforms over finite fields*, §1.6](https://arxiv.org/abs/2109.11961). Their mathematics informs the independently written arguments and receives credit; their theorem statements are never substituted for programme proofs.

For the coherent and étale comparisons, the freely readable [Stacks projective-space computation](https://stacks.math.columbia.edu/tag/01XT), [finite étale chapter](https://stacks.math.columbia.edu/tag/0BL6), [étale criteria](https://stacks.math.columbia.edu/tag/02GU) and [fibrewise étale criterion](https://stacks.math.columbia.edu/tag/03PC) identify the relevant hypotheses. The [AI Integrated Stacks Project English edition](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/) retains the underlying Stacks tags. Its AI additions and proposed corrections have not been reviewed by the Stacks project's maintainers. The lesson reproduces no text from either edition.

Lesson 6 matches the Picard, stabilizer and degree factors with the derived spectral side. A rank-one eigenobject is one part of that correspondence; its categorical theorem still requires the remaining complete proofs.
