# Brauer groups of local and global fields

*Written by OpenAI GPT-6.1 Sol in Codex, Ultra effort, October 2026. Self-checked by the writing AI; no independent review is claimed. Public domain (CC0).*

**Lesson 24.** A Brauer class measures the obstruction to making a central simple algebra into a matrix algebra. Over a nonarchimedean local field, one rational number modulo integers measures the entire obstruction. Over a global field, the local numbers determine the algebra, and their sum must vanish. We prove both assertions, then use their cohomology to construct fundamental classes, Weil extensions and the class-field-tower bound.

The algebraic prerequisites are the written Noether-course lessons [Central simple algebras and the Brauer group](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-LTF/support/NOE-HYP--NOE-HYP-04.html#4-maximal-subfields-and-splitting-fields), Theorems 4.2–4.3 and 5.1, and [Crossed products and factor systems](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-LTF/support/NOE-HYP--NOE-HYP-05.html#3-multiplication-in-the-relative-brauer-group), Theorems 3.2 and 4.1 and Proposition 6.2. In particular, every class has a finite Galois splitting field, and, for finite Galois \(L/K\) with group \(G\),
\[
\operatorname{Br}(L/K)=H^2(G,L^\times),\qquad
\operatorname{Br}(K)=H^2_{\mathrm{cont}}(G_K,(K^s)^\times).
\tag{1}
\]
These are actual preceding algebra proofs, including the convention on crossed products. We use ordinary cochains and Shapiro from [Galois cohomology and the étale cohomology of a field](https://kokunoyumeto.github.io/open-math-courses-public/courses/ag-etale-cohomology/galois-cohomology-and-the-etale-cohomology-of-a-field.html), §§2–3 and 5.1–5.2. The finite-group Tate constructions needed beyond those sections are developed below.

Our arithmetic prerequisites are [Local reciprocity and norm groups](local-reciprocity-and-norm-groups.md), [The norm-index bound and Hasse's norm theorem](the-norm-index-bound-and-hasses-norm-theorem.md), and [The global reciprocity law](the-global-reciprocity-law.md). Their proofs precede the present Brauer reformulation. The invariant is normalized by **arithmetic** Frobenius: an unramified cyclic algebra with Frobenius generator and uniformizer parameter has invariant \(1/n\).


**Prerequisite proof availability.** The named results below identify specific programme lessons. The [prerequisite record](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-CFT/proof-dependencies.html#lesson-24) distinguishes published proofs, supplied owner texts awaiting publication, and missing full proofs. A record or external reference is not a supplied proof; arguments using an unavailable prerequisite retain that dependency.

## 1. Cohomological tools for a finite extension

We first isolate the arguments that turn cyclic computations into statements about arbitrary finite Galois groups. Coefficients in this section are written additively.

### Restriction, norms and inflation

For \(H\subseteq G\), restriction and corestriction satisfy
\[
\operatorname{Cor}_H^G\operatorname{Res}_H^G=[G:H].
\tag{2}
\]
Here is a construction, rather than an appeal to the identity. With
\(\operatorname{Coind}_H^G A=\{f:G\to A:f(hg)=hf(g)\}\), the maps
\[
A\longrightarrow\operatorname{Coind}_H^G A,\quad a\longmapsto(g\mapsto ga),
\qquad
f\longmapsto\sum_{g\in H\backslash G}g^{-1}f(g)
\tag{3}
\]
are \(G\)-linear, and their composite is \([G:H]\). The summand is independent of the coset representative. Replacing \(g\) by \(gx\) proves equivariance of the sum. Under Shapiro the first map induces restriction, so the second defines corestriction and proves (2). Consequently restriction to a Sylow \(p\)-subgroup injects the \(p\)-primary part of positive cohomology. Every positive cohomology class is killed by \(|G|\): in homogeneous cochains the sum of the contractions inserting each element of \(G\) is an equivariant homotopy for multiplication by \(|G|\).

For \(H\triangleleft G\), \(Q=G/H\), we shall also use
\[
0\to H^1(Q,A^H)\to H^1(G,A)\to H^1(H,A),
\tag{4}
\]
and, when \(H^1(H,A)=0\),
\[
0\to H^2(Q,A^H)\xrightarrow{\mathrm{Inf}}H^2(G,A)
\xrightarrow{\mathrm{Res}}H^2(H,A).
\tag{5}
\]
To verify these low-degree assertions, take an injective \(G\)-resolution \(I^\bullet\) of \(A\). Restriction makes its terms \(H\)-injective, because induction is an exact left adjoint. The terms \((I^j)^H\) are \(Q\)-injective, because inflation is an exact left adjoint to taking \(H\)-invariants. Apply the free bar resolution of \(Q\) to the complex \((I^\bullet)^H\). The two filtrations of the resulting first-quadrant double complex have respectively cohomology \(H^*(G,A)\) and second page
\[
H^i(Q,H^j(H,A)).
\tag{6}
\]
Indeed the first filtration kills positive horizontal degrees termwise by injectivity; the second first takes the vertical cohomology \(H^j(H,A)\). Each total degree has finitely many terms, so the filtrations converge without a limit issue. The entries of total degree one give (4). If the row \(j=1\) vanishes, the edge in total degree two gives exactly (5). If \(H^j(H,A)=0\) for \(1\leq j\leq m\), inflation is an isomorphism in degrees \(1,\ldots,m\). The edge maps are the displayed cochain inflation and restriction: they agree in degree zero and on connecting maps. This supplies the particular spectral-sequence calculation used here.

### A cyclic-to-general lemma

Suppose a system of modules \(A_L\) indexed by finite Galois field extensions has \(A_L^H=A_{L^H}\), and that for every cyclic extension of prime degree \(p\),
\[
H^1(C_p,A_L)=0,\qquad |H^2(C_p,A_L)|=p.
\tag{7}
\]
Then for arbitrary finite Galois \(L/K\),
\[
H^1(G,A_L)=0,\qquad |H^2(G,A_L)|\text{ divides }|G|.
\tag{8}
\]
**Proof.** First take a \(p\)-group and induct on its order. It has a normal subgroup \(H\) of index \(p\): a nontrivial finite \(p\)-group has a nontrivial center, and induction on the quotient by a central order-\(p\) subgroup gives an order-\(p\) quotient. Equations (4) and (7) kill \(H^1(G,A_L)\). Equation (5) embeds a group of order \(p\) as the kernel of restriction in degree two, whose image has order dividing \(|H|\) by induction. Thus the order divides \(p|H|\). For a general group, restrict to its Sylow groups and use (2): \(H^1\) vanishes primary part by primary part, and the \(p\)-primary part of \(H^2\) embeds in a group of order dividing the order of the Sylow group. These injections also prove finiteness. Multiplying the bounds proves (8). \(\square\)

For \(A_L=L^\times\), Hilbert 90 and cyclic local reciprocity prove (7). For \(A_L=C_L\), fixed classes descend by lesson 13. The cyclic Herbrand quotient of lesson 14 and the exact norm index of lesson 16 give \(H^1(C_p,C_L)=0\); cyclic periodicity gives \(H^2(C_p,C_L)=C_K/NC_L\) of order \(p\). Thus (8) applies to both arithmetic systems, in both characteristics.

## 2. Unramified algebras and the invariant

Let \(K\) be a nonarchimedean local field with finite residue field, \(K_n/K\) its unramified extension of degree \(n\), and \(F\) arithmetic Frobenius. Valuations are normalized to have image \(\mathbf Z\).

### Proposition 24.1. The unramified invariant

Valuation induces an isomorphism
\[
H^2(\operatorname{Gal}(K_n/K),K_n^\times)
\xrightarrow{\sim}H^2(C_n,\mathbf Z)
\xrightarrow{\sim}\tfrac1n\mathbf Z/\mathbf Z.
\tag{9}
\]
The cyclic algebra \((K_n/K,F,a)\), defined by \(ux=F(x)u\), \(u^n=a\), maps to \(v_K(a)/n\). Inflation between unramified extensions preserves this rational invariant. Their union therefore gives
\[
\operatorname{Br}(K^{\mathrm{ur}}/K)\simeq\mathbf Q/\mathbf Z.
\tag{10}
\]

**Proof.** The unit module \(U_{K_n}\) has zero Tate cohomology in every degree. In degree zero this is surjectivity of unramified unit norms. In degree minus one, Hilbert 90 writes a norm-one unit as \(F(b)/b\); multiplication of \(b\) by a power of a uniformizer in \(K\) makes \(b\) a unit. The same statements hold for every subgroup. Cyclic periodicity proves the assertion in all degrees. The exact sequence
\[
1\to U_{K_n}\to K_n^\times\xrightarrow{v_{K_n}}\mathbf Z\to0
\]
therefore makes valuation an isomorphism in degree two. The cyclic resolution identifies \(H^2(C_n,\mathbf Z)\) with \(\mathbf Z/n\mathbf Z\). Equivalently the boundary from \(0\to\mathbf Z\to\mathbf Q\to\mathbf Q/\mathbf Z\to0\) identifies it with characters of \(C_n\); evaluation at \(F\) gives (9). The parameter cocycle is 1 except at a carry in adding Frobenius exponents, where it is \(a\). Its valuation is the carry cocycle with parameter \(v_K(a)\). This proves the stated formula. Inflation pulls back the character on Frobenius, keeping its value unchanged. All rational numbers modulo integers occur at some finite level. \(\square\)

There is an important base-change calculation before passing to the whole Brauer group. If \(E/K\) is any finite extension, with ramification index \(e\) and residue degree \(f\), an unramified class of invariant \(r\) restricts to an unramified class over \(E\) of invariant
\[
\operatorname{inv}_E(\operatorname{Res}_{E/K}b)=efr=[E:K]r.
\tag{11}
\]
To see this on the preceding construction, restrict the character to the unramified base change. Its Frobenius restricts to \(F^f\), multiplying the character value by \(f\). Changing normalized valuations multiplies the valuation cocycle by \(e\). Boundary maps commute with both operations, yielding (11). This argument also permits \(E/K\) to be non-Galois.

### Theorem 24.2. Local Brauer groups

For every nonarchimedean local field with finite residue field,
\[
\operatorname{inv}_K:\operatorname{Br}(K)\xrightarrow{\sim}\mathbf Q/\mathbf Z.
\tag{12}
\]
For \(L/K\) finite Galois of degree \(n\), its relative group is exactly the subgroup \(\tfrac1n\mathbf Z/\mathbf Z\). Restriction multiplies invariants by the extension degree; corestriction preserves them. Also
\[
\operatorname{Br}(\mathbf R)=\tfrac12\mathbf Z/\mathbf Z,
\qquad \operatorname{Br}(\mathbf C)=0.
\tag{13}
\]

**Proof.** Put \(M=LK_n\). Every class split by \(K_n\) restricts to zero over \(L\): its invariant over \(L\), calculated in the unramified extension \(M/L\), is \(n\) times its original invariant by (11). Equation (5), applied to \(M/L/K\) and Hilbert 90, then places it in \(H^2(G,L^\times)\). This gives a subgroup of order \(n\) there. The bound (8) says that the whole group has order dividing \(n\), so it is precisely that subgroup. Every Brauer class has a finite Galois splitting field by (1), proving (12) and the relative assertion. Formula (11) now applies to every class.

For corestriction, restriction \(\operatorname{Br}(K)\to\operatorname{Br}(E)\) is surjective because multiplication by \([E:K]\) on \(\mathbf Q/\mathbf Z\) is surjective. Write a class \(c\) over \(E\) as \(\operatorname{Res}b\). Then (2) gives
\(\operatorname{inv}_K(\operatorname{Cor}c)=[E:K]\operatorname{inv}_K(b)=\operatorname{inv}_E(c)\).

Over \(\mathbf C\), all central simple algebras split. Over \(\mathbf R\), every class is split by \(\mathbf C\), so (1) and the cyclic resolution give
\(H^2(C_2,\mathbf C^\times)=\mathbf R^\times/N\mathbf C^\times\).
Complex norms are exactly the positive reals; this group has two elements, with negative parameter giving Hamilton's algebra. Assign that class invariant \(1/2\). This proves (13) without importing a classification of real division algebras. \(\square\)

### Cyclic algebras and the Artin character

If \(L/K\) is cyclic, \(\sigma\) a generator, and \(\chi(\sigma)=1/n\), then
\[
\operatorname{inv}_K(L/K,\sigma,a)
=\chi(\operatorname{rec}_{K,\mathrm{arith}}(a)).
\tag{14}
\]
One must check this normalization for ramified extensions as well. Regard the class as \(\delta\chi\cup a\); rational lifts of \(\chi\) give exactly the carry cocycle used in the cyclic algebra. The cochain cup product and transfer satisfy the projection formula: distribute the coset sum (3) over a cup product whose other factor is restricted from \(G\); the restricted factor is pulled outside each summand. In degree zero the coefficient transfer is the field norm.

Now choose the positive Frobenius lift of \(\sigma\) and its fixed field \(\Sigma\) in the enlarged unramified extension, as in [Frobenius lifts and abstract reciprocity](frobenius-lifts-and-abstract-reciprocity.md), sections 2 and 5–6. Over \(\Sigma\), the character becomes unramified and its arithmetic Frobenius has value \(\chi(\sigma)\). For a uniformizer \(\pi_\Sigma\), Proposition 24.1 gives
\(\operatorname{inv}_\Sigma(\delta\chi|_\Sigma\cup\pi_\Sigma)=\chi(\sigma)\).
Corestriction preserves the invariant by Theorem 24.2, so the projection formula gives that same invariant for parameter \(N_{\Sigma/K}\pi_\Sigma\). The Frobenius-lift definition in lesson 4 says that this parameter represents the inverse reciprocity image of \(\sigma\). Its class generates \(K^\times/NL^\times\). Both sides of (14) are homomorphisms on that cyclic quotient, so agreement on this generator proves (14). The real version is the same sign calculation, and the complex version is zero.

## 3. Tate cohomology and the fundamental class

For a finite group, extend ordinary cohomology to all integer degrees by a complete resolution. Concretely, splice the free bar resolution of \(\mathbf Z\) to its integral dual, using the norm between the two degree-zero terms. The bar resolution is exact by insertion of the identity on underlying abelian groups; its dual is exact because those underlying sequences split over \(\mathbf Z\). The splice is exact at the middle since the kernel of augmentation is the augmentation ideal and the invariant elements of \(\mathbf Z[G]\) are multiples of the norm. Applying \(\operatorname{Hom}_G(-,A)\) defines \(\widehat H^q(G,A)\). It agrees with ordinary \(H^q\) for \(q>0\), and
\[
\widehat H^0=A^G/N_GA,\quad
\widehat H^{-1}=\ker N_G/I_GA,\quad
\widehat H^{-q-1}(G,\mathbf Z)=H_q(G,\mathbf Z)\quad(q\geq1).
\tag{15}
\]
In particular \(\widehat H^{-2}(G,\mathbf Z)=G^{\mathrm{ab}}\). The degree-one bar boundary imposes precisely \([gh]=[g]+[h]\), giving this identification.

Short exact sequences give long exact Tate sequences: all the resolution terms are free, so taking cochains is termwise exact. Induced modules \(\mathbf Z[G]\otimes B\) have zero Tate cohomology, including after restriction to any subgroup. Identify their cochains with the underlying split bar complex by evaluation on a coset coordinate; the insertion contraction and its dual prove this assertion also in the two middle degrees. The maps (3) and their bar comparisons extend restriction, corestriction and (2) to Tate degrees. Cup products extend by the bar diagonal and dimension shifting; on nonnegative cochains they are
\[
(c\cup d)(g_1,\ldots,g_{r+s})
=c(g_1,\ldots,g_r)\otimes(g_1\cdots g_r)d(g_{r+1},\ldots,g_{r+s}).
\tag{16}
\]
Splitting the alternating boundary at the join proves its Leibniz rule. The long exact sequences extend this product to negative degrees and make connecting maps commute with it, with the usual degree sign. We place the degree-two class on the right; its even degree introduces no sign in the isomorphisms below.

### Tate's two-degree criterion

If \(\widehat H^j(H,B)=\widehat H^{j+1}(H,B)=0\) for every subgroup \(H\), then all its Tate groups vanish.

**Proof.** There are shifts in both directions. The surjection
\(\mathbf Z[G]\otimes B\to B\), \(g\otimes b\mapsto gb\), and the injection
\(B\to\operatorname{Maps}(G,B)\), \(b\mapsto(g\mapsto gb)\), have Tate-acyclic middle modules; their kernels and cokernels shift cohomology by one, simultaneously for all subgroups. Shift to \(j=1\). It suffices to prove vanishing in degrees 0 and 3; iteration then proves all degrees.

Induct on \(|G|\). For a group that is not a \(p\)-group, all Sylow subgroups are proper, and (2) kills the two groups primary part by primary part. For a \(p\)-group take \(H\triangleleft G\) of index \(p\). Induction gives vanishing for \(H\) in degrees 0 through 3. The inflation consequence of (6) gives isomorphisms in degrees 1, 2 and 3 with the corresponding groups of \(C_p\) on \(B^H\). Cyclic periodicity gives degree-three vanishing from degree one and
\((B^H)^{C_p}=N_{C_p}B^H\) from degree-two vanishing. Degree-zero vanishing for \(H\) says \(B^H=N_HB\), so \(B^G=N_GB\). This proves degree-zero vanishing for \(G\) and completes the induction. \(\square\)

### Tate's cup-product theorem

Suppose for every \(H\subseteq G\), \(H^1(H,A)=0\) and \(H^2(H,A)\) is cyclic of order \(|H|\). If \(u\) generates \(H^2(G,A)\), then
\[
\widehat H^q(G,\mathbf Z)\xrightarrow{x\mapsto x\cup u}
\widehat H^{q+2}(G,A)
\tag{17}
\]
is an isomorphism for every integer \(q\).

**Proof.** First restriction of \(u\) generates each \(H^2(H,A)\). Its order is at least \(|H|\), because corestriction of it is \([G:H]u\), which has exactly that order by (2); the target itself has order \(|H|\).

Twice take the cokernel of the injection into the induced module just used. The resulting module \(B\) has natural shifts
\(\widehat H^q(H,B)=\widehat H^{q+2}(H,A)\).
Thus \(\widehat H^{-1}(H,B)=0\) and \(\widehat H^0(H,B)\) is cyclic of order \(|H|\). Lift the shifted class of \(u\) to \(b\in B^G\). Adjoin \(\mathbf Z[G]\) to \(B\), which does not change any Tate group, and inject
\[
\mathbf Z\longrightarrow B\oplus\mathbf Z[G],
\qquad 1\longmapsto(b,N_G).
\]
The second coordinate proves injectivity. On degree-zero cohomology of every subgroup this is an isomorphism: the image of 1 is the restricted generator just proved. In the long exact sequence for its cokernel \(D\), the facts \(\widehat H^{-1}(H,B)=0\) and \(H^1(H,\mathbf Z)=0\) consequently give
\(\widehat H^{-1}(H,D)=\widehat H^0(H,D)=0\).
The two-degree criterion makes \(D\) Tate-acyclic. The injection of \(\mathbf Z\) therefore induces isomorphisms in every degree. Its first coordinate is multiplication by the shifted class of \(u\); commuting the two connecting maps with (16) gives precisely (17). \(\square\)

### Proposition 24.3. Local fundamental classes and reciprocity

For \(L/K\) finite Galois of degree \(n\), let \(u_{L/K}\) be the unique class with local invariant \(1/n\). Cup product gives
\[
\widehat H^q(G,\mathbf Z)\simeq\widehat H^{q+2}(G,L^\times),
\qquad
G^{\mathrm{ab}}\simeq K^\times/N_{L/K}L^\times.
\tag{18}
\]
The last map is the inverse of **arithmetic** reciprocity.

**Proof.** Hilbert 90 and Theorem 24.2 verify every hypothesis of (17), including for subgroups. For \(H\subset G\) with fixed field \(E\), restriction multiplies the invariant by \([E:K]\), giving \(1/[L:E]\); it is exactly \(u_{L/E}\). In a cyclic group with generator \(\sigma\), the bar and periodic resolutions give \([\sigma]\cup[a]=a\) in the norm quotient: summing the carry cocycle once round the cycle yields its parameter. Formula (14) therefore identifies this map with inverse arithmetic reciprocity. For arbitrary \(G\), take \(H=\langle g\rangle\). Corestriction on \(H_1\) in the negative Tate notation is induced by inclusion, and on \(\widehat H^0\) it is \(N_{E/K}\). The projection formula and the restriction identity for \(u\) reduce the image of \([g]\) to the cyclic result over \(E\). Norm functoriality of lesson 5 gives precisely \(g\) in \(G^{\mathrm{ab}}\). Every abelianized element is represented by such a \(g\), proving the identification without an undetermined inverse. \(\square\)

## 4. The local–global theorem

Let \(K\) be a global field. At a real place use the invariant in (13); at a complex place use zero. Only finitely many localizations of a Brauer class are nonzero. Here is a direct justification of this support assertion using (1). Represent the class by a cocycle on a finite Galois splitting field. Outside finitely many places that extension is unramified and all its finitely many cocycle values are units. Localization lies in the cohomology of the unramified unit module, which vanishes by Proposition 24.1. No global sum law is being assumed in this argument.

### General injectivity from the cyclic norm theorem

If a global Brauer class is zero at every place, it is zero globally.

**Proof.** Induct on the order of a finite Galois splitting group \(G\). For a cyclic extension, the parameter is a local norm everywhere; Hasse's norm theorem in lesson 15 makes it a global norm, and the cyclic algebra splits. If \(G\) is a \(p\)-group of larger order, choose \(H\triangleleft G\) of index \(p\). Over \(E=L^H\) the class is locally zero, so induction kills its restriction. Equation (5) and Hilbert 90 make it a cyclic relative class for \(E/K\), to which the first argument applies. If \(G\) is not a \(p\)-group, every Sylow subgroup is proper; restriction to its fixed field vanishes by induction. Equation (2) kills every primary part. Thus the original class vanishes. \(\square\)

### A supply of cyclic splitting extensions

Given finitely many finite places \(S\) and a prescribed power \(p^{a_v}\) at each, there is a cyclic extension whose local degree at every \(v\in S\) is divisible by \(p^{a_v}\). For \(p=2\) it can additionally make any specified real places complex.

**Proof for number fields.** Start with the cyclotomic \(\mathbf Z_p\)-extension of \(\mathbf Q\) supplied by lesson 20 and restrict its characters to \(G_K\). Its image is an open subgroup of \(\mathbf Z_p\), because a number field intersects that tower in a finite field. At a place over \(p\), the local image is open by total cyclotomic ramification and the finite degree of \(K_v\). At \(v\nmid p\), Frobenius has image the principal-unit component of the integer \(Nv>1\). This component is nonzero: if it were zero, \(Nv\) would be a \(p\)-adic root of unity, hence \((Nv)^{p-1}=1\) for odd \(p\), or \((Nv)^2=1\) for \(p=2\), impossible for that positive integer. A nonzero subgroup generated in \(\mathbf Z_p\) is open. Thus finite cyclic quotients at sufficiently high levels have arbitrarily large local \(p\)-power degrees at every place of the finite set.

For \(p=2\), this tower is real. Take a finite quotient character of order \(2^N\) and multiply it by the quadratic character of \(\mathbf Q(i)\), also restricted to \(G_K\). At a real place complex conjugation now maps to \(-1\). Choose the initial level to give finite local image order at least \(\max(4,2^{a_v})\). An element of order \(2^b\), \(b\geq2\), in the cyclic group of order \(2^N\) has exponent of valuation \(N-b\); adding 0 or \(2^{N-1}\) does not change that valuation. Hence twisting does not reduce the required local orders. The image of the twisted character is still cyclic, and its fixed field has all the asserted properties. Odd-primary local classes have no real obstruction.

For a function field with full constant field \(\mathbf F_q\), use a constant extension of degree \(n\). At a place of residue degree \(d_v\), the local degree is \(n/\gcd(n,d_v)\): the tensor product of the two finite residue fields has that degree in each factor. Choose \(n\) divisible by \(p^{a_v}d_v\) for every \(v\in S\). Then its local degree is divisible by \(p^{a_v}\). There are no archimedean places. \(\square\)

### Theorem 24.4. Albert–Brauer–Hasse–Noether

For every global field the following sequence is exact:
\[
0\longrightarrow\operatorname{Br}(K)
\longrightarrow\bigoplus_v\operatorname{Br}(K_v)
\xrightarrow{\ \sum_v\operatorname{inv}_v\ }\mathbf Q/\mathbf Z
\longrightarrow0.
\tag{19}
\]

**Proof.** Injectivity has just been proved for arbitrary splitting groups. To prove the sum law, first take a \(p\)-primary global class \(b\). Choose a cyclic extension whose local degrees at its finite support are divisible by all local orders, and which complexifies any real support when \(p=2\). Restriction multiplies local invariants by these degrees, so \(b\) becomes locally zero over the extension. General injectivity over that global field makes it globally zero. Thus \(b\) is represented by a cyclic algebra \((L/K,\sigma,a)\), by (1). Formula (14), including its archimedean cases and restricted characters at each completion, gives
\[
\sum_v\operatorname{inv}_v(b)
=\sum_v\chi(\operatorname{rec}_{K_v}(a))
=\chi(\operatorname{rec}_K(a))=0.
\tag{20}
\]
The last equality is the principal product law already proved in lesson 16. Every Brauer class is torsion by the finite splitting field and (2), so summing its finitely many primary components proves (20) generally. In particular, cyclic splitting was proved here, not presumed as an external classification theorem.

Conversely take a finite tuple \((r_v)\) with sum zero, and split it into its primary tuples. For a single primary tuple choose a cyclic \(L/K\), of degree \(n\), with local decomposition orders divisible by the denominators at its support. Fix a faithful character \(\chi:G\to\tfrac1n\mathbf Z/\mathbf Z\). At each support place local reciprocity is onto the decomposition group, whose character image contains \(r_v\); choose \(a_v\in K_v^\times\) giving that value. Put \(a_v=1\) elsewhere. This is an idèle. Its global Artin image is trivial, since its faithful character value is \(\sum r_v=0\). Lesson 16's exact norm kernel gives
\[
a=xN_{L/K}y,\qquad x\in K^\times,\quad y\in J_L.
\]
The cyclic algebra with parameter \(x\) has local invariant \(r_v\) at every place by (14); local norms contribute zero, also outside the original support. Add the primary classes to realize the tuple. Finally the sum map is onto: choose any nonarchimedean place and the local invariant desired in \(\mathbf Q/\mathbf Z\). This proves every part of (19). \(\square\)

## 5. Quaternion algebras and ramification

Assume characteristic different from 2 for the symbol presentation \((a,b)_K\). At a nonarchimedean or real place, the Hilbert symbol of lesson 11 gives
\[
\operatorname{inv}_v(a,b)=
\begin{cases}0,&(a,b)_v=1,\\[2pt]1/2,&(a,b)_v=-1.\end{cases}
\tag{21}
\]
Indeed a quaternion algebra is the quadratic cyclic algebra with parameter \(b\); it splits exactly when \(b\) is a norm from \(K_v(\sqrt a)\). The first-entry reciprocity convention of lesson 11 gives the same split criterion, irrespective of the interchangeable entries of a quadratic symbol.

### Corollary 24.5. Quaternion algebras over \(\mathbf Q\)

The ramification set of a quaternion algebra over \(\mathbf Q\) is a finite set of places of even cardinality. Every such set occurs, and it determines the algebra up to isomorphism.

**Proof.** Equation (21) and the sum law imply finiteness and even cardinality. For an even finite set, (19) realizes the tuple having invariant \(1/2\) there and zero elsewhere. Choose a rational \(d\) that is a nonsquare in every specified finite completion and negative if the real place is specified. This is possible by weak approximation: each finite nonsquare class contains an open neighborhood, and negativity is open at infinity. If the set is nonempty this makes \(\mathbf Q(\sqrt d)\) quadratic and locally of degree two throughout the set. The realized class restricts to zero everywhere over that field, hence globally by injectivity. The algebraic splitting criterion in the Noether lesson makes its index divide two. A nonzero class is therefore a division algebra of degree two containing that quadratic field, hence its cyclic crossed product is a quaternion algebra. The empty set is represented by \(M_2(\mathbf Q)\). If two quaternion algebras have the same set, (19) makes their classes equal, and Wedderburn uniqueness together with their equal degree two makes the algebras isomorphic. \(\square\)

For Hamilton's algebra \((-1,-1)_{\mathbf Q}\), every odd finite place has invariant zero by the odd-prime unit formula of lesson 11. At 2 the odd-unit formula gives \((-1,-1)_2=-1\), and at the real place both entries are negative, giving \(-1\). Its ramification set is exactly \(\{2,\infty\}\), in agreement with the even-set theorem.

## 6. Global fundamental classes

The global formation uses \(C_L\), not \(L^\times\). The two coefficient modules have quite different degree-two cohomology. We now construct the invariant for the former.

### The cyclic class-group invariant

For a cyclic extension \(L/K\), of degree \(n\), the idèle sequence and Hilbert 90 give
\[
0\to H^2(G,L^\times)\to H^2(G,J_L)
\to H^2(G,C_L)\to0.
\tag{22}
\]
The term on the right after this sequence is \(H^3(G,L^\times)=H^1(G,L^\times)=0\), by cyclic periodicity. The fixed-class and \(H^1\)-vanishing arguments in §§1 and lesson 13 justify the injection on the left. Shapiro and the unit-tail argument of lesson 13, now applied to degree two, identify the middle term as
\[
\bigoplus_v H^2(D_w,L_w^\times).
\tag{23}
\]
The proof for the tail works in this degree because every unramified local unit Tate group vanishes; a finite cocycle and a cochain relation belong to one finite chart, and all remaining primitives can be chosen as units.

By Theorem 24.4, the image on the left of (22) consists exactly of the tuples in (23) whose invariant sum is zero. For the converse part of this claim, realize such a tuple as a global Brauer class. Its restriction to \(L\) has every local invariant zero because each denominator divides its local extension degree. Global injectivity over \(L\) makes it a relative class. Thus the invariant sum identifies \(H^2(G,C_L)\) with \(\tfrac1n\mathbf Z/\mathbf Z\). Its image is that entire group: Chebotarev in lesson 22 gives an unramified place whose Frobenius generates the cyclic group, hence local degree \(n\). With generator \(\sigma\) and \(\chi(\sigma)=1/n\), the periodic-resolution identification gives
\[
H^2(G,C_L)=C_K/NC_L,
\qquad \operatorname{inv}(c)=\chi(\operatorname{rec}_K(c)).
\tag{24}
\]
Indeed lift a representative class to an idèle; (14) computes the sum in (22), and the principal product law makes it independent of the lift.

### Theorem 24.6. The global class formation

For finite Galois \(L/K\) of degree \(n\), there is a canonical invariant
\[
H^2(G,C_L)\simeq\tfrac1n\mathbf Z/\mathbf Z,
\qquad H^1(G,C_L)=0.
\tag{25}
\]
Inflation preserves the invariant and restriction to a finite base extension multiplies it by the extension degree. The fundamental class \(u_{L/K}\), of invariant \(1/n\), gives
\[
\widehat H^q(G,\mathbf Z)\simeq\widehat H^{q+2}(G,C_L).
\tag{26}
\]
In degree \(-2\), this is inverse arithmetic global reciprocity.

**Proof.** The \(H^1\)-vanishing and order bound \(|H^2(G,C_L)|\mid n\) are already proved in §1. Choose a cyclic extension \(T/K\) of degree \(n\). For function fields take constants. For number fields choose a rational prime \(\ell\equiv1\pmod n\) unramified in \(K\), using the rational ray-class prime result in lesson 22. The degree-\(n\) subfield of \(\mathbf Q(\zeta_\ell)\) intersects \(K\) trivially: it is totally ramified at \(\ell\), whereas every subfield of \(K\) is unramified there. Its compositum with \(K\) supplies \(T\).

Put \(N=LT\). Inflation of both groups \(H^2(T/K,C_T)\) and \(H^2(L/K,C_L)\) into \(H^2(N/K,C_N)\) is injective by (5) and the \(H^1\)-vanishing. Every class from the cyclic field \(T\) lifts to \(H^2(T/K,J_T)\), by (22). After restricting to \(L\), its idelic invariant sum is multiplied by \([L:K]=n\): at each base place, sum the local degrees \([L_{v'}:K_v]\), which sum to \(n\). Its original invariant lies in \(\tfrac1n\mathbf Z/\mathbf Z\), so the new sum is zero. The extension \(N/L\) is cyclic. The cyclic case (22) therefore kills the restricted class in \(H^2(N/L,C_N)\). By (5) the class descends to \(H^2(L/K,C_L)\). The cyclic subgroup from \(T\) has order \(n\); the order bound makes the two inflated subgroups equal.

To make the invariant independent of this auxiliary field, put
\(\mathcal J=\bigcup_L J_L\) and \(\mathcal C=\bigcup_L C_L\), with the extension embeddings of lesson 13, regarded as discrete \(G_K\)-modules. Their fixed modules are \(J_L\) and \(C_L\). Continuous cochains have finite image, so their cohomology is the direct limit of finite-extension cohomology. The same finite-chart argument as (23) gives
\[
H^2(G_K,\mathcal J)=\bigoplus_v\operatorname{Br}(K_v).
\tag{27}
\]
There is no missing local class in this limit: for a finite local tuple, the cyclic-extension construction of §4 supplies one global extension whose local degrees split every entry. Thus the finite relative groups in (23) exhaust the displayed direct sum.

The auxiliary-field comparison just proved shows that every class in \(H^2(G_K,\mathcal C)\) comes from an idelic class: at a common finite level it equals a class from a cyclic extension, and those lift by (22). The exact sequence
\(1\to(K^s)^\times\to\mathcal J\to\mathcal C\to1\)
therefore identifies
\[
H^2(G_K,\mathcal C)
=\left(\bigoplus_v\operatorname{Br}(K_v)\right)/\operatorname{Br}(K)
\xrightarrow{\sum\operatorname{inv}_v}\mathbf Q/\mathbf Z.
\tag{28}
\]
Exactness uses \(H^1(G_K,\mathcal C)=0\), which follows from the finite vanishing. Formula (19) proves the last isomorphism. Finite \(H^2(G,C_L)\) injects into (28) by (5), has order \(n\), and hence is the unique subgroup \(\tfrac1n\mathbf Z/\mathbf Z\). This defines the canonical invariant. Inflation compatibility is built into this injection. Restriction compatibility follows from (27) and local degree multiplication, summed over places. The same reasoning gives preservation of the invariant by corestriction, using local corestriction and its sum.

For \(H\subset G\), restriction of \(u_{L/K}\) has invariant
\([L^H:K]/n=1/|H|\), so it is \(u_{L/L^H}\). Tate's cup-product theorem now proves (26). In a cyclic group the parameter computation of §3 and (24) give inverse reciprocity with the asserted sign. For an arbitrary \(g\in G\), restrict to \(\langle g\rangle\), apply the cyclic result and corestrict back. The projection formula and the norm functoriality of lesson 16 give \(g\) in \(G^{\mathrm{ab}}\), exactly as in the local argument for (18). This proves the full assertion. \(\square\)

## 7. Relative Weil groups and their transition maps

For this section \(K\) is a number field. Write a multiplicative normalized cocycle \(f\) for \(u_{L/K}\). Define
\[
W_{L/K}=C_L\times G,
\qquad (a,g)(b,h)=(a\,g(b)\,f(g,h),gh).
\tag{29}
\]
The cocycle identity proves associativity. Give this group the topology consisting of finitely many copies of the locally compact group \(C_L\); the action and multiplication are continuous. Changing the cocycle by a coboundary gives the continuous isomorphism that changes the chosen lifts by that cochain. Thus
\[
1\to C_L\to W_{L/K}\to G\to1
\tag{30}
\]
is the extension represented by the fundamental class.

### Transfer and abelianization of a fundamental extension

For an extension \(1\to A\to E\to G\to1\), with \(G\) finite and \(A\) abelian, transfer to \(A\) lands in \(A^G\). Choose lifts \(s(t)\), and for \(x\) mapping to \(g\), write
\(xs(t)=s(gt)a_t\). The transfer is \(\prod_t a_t\). A change of lifts cancels by the permutation of \(G\); multiplying two elements gives the product of their transfers. Conjugation consequently leaves the transfer unchanged, while its effect on the target is the given \(G\)-action. This proves that the value is invariant. On \(A\) it is \(N_G\).

For a fundamental class the resulting map
\[
E^{\mathrm{ab}}\longrightarrow A^G
\tag{31}
\]
is an isomorphism. To verify its kernel, the degree-one bar calculation for this extension gives the exact sequence
\[
H_2(G,\mathbf Z)\longrightarrow A_G
\longrightarrow E_{\mathrm{ab}}\longrightarrow G_{\mathrm{ab}}\to0.
\tag{32}
\]
The first arrow evaluates the extension cocycle on a bar two-cycle. Indeed lift the successive edges of that cycle to \(E\); their boundary products cancel in the quotient, and the remaining factors are precisely its cocycle values, modulo conjugate differences. Thus its image in \(A_G\) is the image of
\(\widehat H^{-3}(G,\mathbf Z)\xrightarrow{\cup u}\widehat H^{-1}(G,A)\).
Tate's theorem makes that image all of \(\ker(N_G:A_G\to A^G)\). On the final quotient of (32), the transfer is
\(G_{\mathrm{ab}}\xrightarrow{\cup u}A^G/N_GA\): substitute the lift products in the transfer formula, the same bar evaluation as (18). This is again an isomorphism. Hence transfer is injective and surjective in (31).

For \(A=C_L\), the field norm \(C_L\to NC_L\) is open and has compact kernel. Its modulus map identifies the noncompact positive-real direction, while its norm-one kernel lies in the compact norm-one idèle class group of lesson 14. Openness follows either from the local norm charts of lesson 13 and quotient topology, or from their induced open map on class groups. Transfer, restricted to each component of \(E\), is a translate of this norm map. It is therefore open onto \(C_K\), whose norm subgroup has finite index, and has closed kernel. The algebraic commutator kernel found in (32) is consequently already closed. Thus (31) is a topological isomorphism
\[
W_{L/K}^{\mathrm{ab}}\simeq C_K.
\tag{33}
\]
It is inverse arithmetic reciprocity after projection to \(G^{\mathrm{ab}}\).

### The quotient in a tower

Let \(M/L/K\) be finite Galois over \(K\), \(H=\operatorname{Gal}(M/L)\), and \(E=W_{M/K}\). The inverse image \(E_H\) of \(H\) has fundamental class \(u_{M/L}\). Its transfer identifies \(E_H^{\mathrm{ab}}\) with \(C_L\). Consequently
\(F=E/[E_H,E_H]\) is an extension of \(\operatorname{Gal}(L/K)\) by \(C_L\).
Its class is exactly \(u_{L/K}\), as follows.

If \(v\) denotes the class of \(F\), inflate it to \(\operatorname{Gal}(M/K)\) and include its coefficients \(C_L\subset C_M\). Pushing (29) through the transfer on its kernel says that this class is \(N_Hu_{M/K}\). Since \(H\) is normal, \(N_H\) is central in \(\mathbf Z[G]\). A central group-ring element acts on \(\operatorname{Ext}_{\mathbf Z[G]}^*(\mathbf Z,A)\) by its augmentation: multiplication on a free resolution lifts its augmentation on \(\mathbf Z\), and the comparison homotopy between those two lifts gives the equality on cohomology. Here this gives
\(N_Hu_{M/K}=|H|u_{M/K}\), of invariant \(1/[L:K]\). Inflation of \(u_{L/K}\) has that same invariant by (25). Inflation with the coefficient inclusion is injective by \(H^1(H,C_M)=0\) and (5); hence \(v=u_{L/K}\).

Choose an isomorphism of this quotient with \(W_{L/K}\). This provides a surjective transition homomorphism
\[
W_{M/K}\longrightarrow W_{L/K},
\tag{34}
\]
whose restriction to \(C_M\) is \(N_{M/L}\). Its kernel is the closed commutator subgroup of \(E_H\), and is compact: the transfer kernel meets each of its finitely many components in a translate of the compact norm kernel. This also proves that (34) is proper. Nested quotients give transitive transitions. Isomorphism choices differ by a cocycle with coefficients \(C_L\); \(H^1(G,C_L)=0\) makes those differences inner coefficient conjugations.

### The absolute group and its topology

A number field and its separable closure are countable. Enumerate the finite Galois extensions and take successive composita to obtain a cofinal tower \(K=L_0\subset L_1\subset\cdots\). Choose the adjacent quotient isomorphisms (34), and use their composites for all tower transitions. This is a coherent system, rather than a claim that cocycles have canonical rigid representatives. Define
\[
W_K=\varprojlim_i W_{L_i/K}.
\tag{35}
\]
Every projection is surjective: over a fixed finite-level point the higher fibres form a system of nonempty compact sets, and their finite compatibility conditions have a common solution. The same compactness argument says that the inverse image of a compact set at any level is compact. The inverse image of a compact identity neighborhood is therefore a compact neighborhood in the limit, proving local compactness. Projection to the finite Galois quotients gives a continuous map \(W_K\to G_K\) with dense image, since it is onto every finite quotient.

The projection to \(W_{K/K}=C_K\) is the compatible transfer. Its kernel is exactly the closure of the commutator subgroup of \(W_K\). One inclusion follows because \(C_K\) is abelian. For the other, take an element in that kernel and a basic neighborhood determined at level \(i\). Its component lies in the commutator kernel of (33). Approximate that component by a finite product of commutators, and lift each factor to \(W_K\), using projection surjectivity. Their commutator product belongs to the neighborhood. This proves the required density in the kernel. The projection is open: a basic open set from level \(i\) has image under the open transfer at that level. Thus
\[
W_K^{\mathrm{ab}}\xrightarrow{\sim}C_K
\tag{36}
\]
is a homeomorphism. Choice independence can be proved without assuming surjectivity of coefficient norms. For two systems at a common field \(L\), isomorphisms fixing \(C_L\) and the Galois quotient form a nonempty torsor for \(C_L/C_K\): their differences are cocycles, killed by \(H^1(G,C_L)=0\), and an inner coefficient conjugation is trivial exactly on \(C_L^G=C_K\). This quotient is compact, since the embedded positive modulus direction of \(C_K\) covers that of \(C_L\). Quotienting commutator subgroups gives continuous transition maps on these compact isomorphism spaces. Every finite list of compatibility conditions is met at one higher common field. Compactness supplies an inverse-limit isomorphism, continuous with continuous inverse. Aligning two cofinal towers by composita applies this argument to (35). This proves the asserted topological choice independence with the coefficient and Galois maps preserved.

### Local-to-global compatibility

Fix a place \(v\) and an embedding of separable closures realizing its decomposition group. There is a continuous homomorphism
\[
\theta_v:W_{K_v}\longrightarrow W_K
\tag{37}
\]
compatible with that embedding on Galois groups and with the idèle inclusion \(K_v^\times\to C_K\) on Hausdorff abelianizations. We give the compatibility argument, including the inverse-limit choice.

First the local group of lesson 12 has relative quotient
\(W_{K_v}/\overline{[W_{L_w},W_{L_w}]}\)
represented by the local fundamental class. Its kernel is \(L_w^\times\) by Theorem 12.2. Transfer is the inclusion on multiplicative abelianizations, since the finite transfer identities of lesson 5 commute with the continuous local reciprocity homeomorphisms of lesson 12. For an unramified cyclic extension, a Frobenius lift raised to its degree is the Frobenius of \(L_w\), whose abelianized image is a uniformizer; the carry cocycle has invariant \(1/[L_w:K_v]\). For a general local extension compare with the unramified extension of the same degree in a common finite Galois extension. The quotient-by-commutators identity and transfer give the inflation identity
\(\mathrm{Inf}\,\alpha_{L_w/K_v}=[M_w:L_w]\alpha_{M_w/K_v}\)
for its extension classes: the coefficient map followed by inclusion is the central norm operator, exactly as in the proof of (34). The equal-degree comparison therefore identifies the two inflated classes. Hilbert 90 makes inflation injective, proving that the general class is the normalized \(u_{L_w/K_v}\). For real and complex places, (20)–(21) of lesson 12 give respectively the parameter \(-1\) class and the trivial class, with the same invariants.

For global \(L/K\), let \(D=D_w\) and \(E=L^D\). The map \(L_w^\times\to C_L\), inserting a component at \(w\), takes the local fundamental class to the restriction of \(u_{L/K}\). Indeed the resulting class is an idelic class over \(E\) supported at its distinguished place, with sum of invariants \(1/|D|\); (25) identifies it with \(u_{L/E}\). Equality of these cocycle classes gives a continuous homomorphism from the local relative extension to the inverse image of \(D\) in \(W_{L/K}\), with the specified coefficient and quotient maps. An explicit construction changes one lifted cocycle by the cochain whose boundary is their quotient, then uses (29).

Let \(I_L\) be the set of those homomorphisms. It is nonempty. Two members differ by a \(D\)-cocycle in \(C_L\); \(H^1(D,C_L)=0\) makes it an inner conjugation. Thus \(I_L\) is a torsor for
\[
C_L/C_L^D=C_L/C_E.
\tag{38}
\]
This quotient is compact: the positive modulus direction of \(C_E\) covers that of \(C_L\), leaving a quotient of the compact norm-one group. It supplies \(I_L\) with a compact topology. If \(M\supset L\), a member of \(I_M\) descends to a member of \(I_L\): local commutators over \(L_w\) map into the global commutator kernel in (34). The induced map is continuous, its change under inner conjugation being the norm \(C_M\to C_L\). Finite compatibility conditions can all be met by choosing a member at one higher common level and descending it. Compactness therefore supplies an element of \(\varprojlim I_L\), without requiring any individual norm map to be onto. The resulting compatible homomorphisms define (37); continuity follows componentwise.

Finally transfer commutes with these local maps. Within the subgroup over \(D\), choose its coset lifts as the images of local lifts. Formula (31) then shows that transfer of the local map is exactly the coefficient inclusion on the local transfer: on abelianizations it is \(K_v^\times\to C_E\), inserted at the distinguished place of \(E=L^D\), whose completion is \(K_v\). Inclusion of that subgroup into the full relative Weil group induces the field norm \(C_E\to C_K\). To check this last identity, the transfer formula, decomposed into cosets of \(D\), gives
\[
V_G(x)=\prod_{gD\in G/D}g\bigl(V_D(x)\bigr)
\qquad(x\text{ in the subgroup over }D).
\]
This is the transfer double-coset identity when the target normal subgroup is the common coefficient group: multiply the coefficients within each block, and the changes of lifts telescope between permuted blocks. The displayed product is the field norm on the \(D\)-fixed coefficient group. The norm of the distinguished single-place idèle is the same single component in \(C_K\). Passing to the limit therefore proves the commuting diagram
\[
\begin{array}{ccc}
W_{K_v}^{\mathrm{ab}}&\xrightarrow{\theta_v^{\mathrm{ab}}}&W_K^{\mathrm{ab}}\\
\downarrow\wr&&\downarrow\wr\\
K_v^\times&\longrightarrow&C_K.
\end{array}
\tag{39}
\]
Together with (35)–(36), this is the number-field construction and compatibility asserted in lesson 12. Choosing geometric reciprocity inverts both vertical identifications. Weil's construction and Tate's formulation of its local relationship are credited in the references; the cocycle, compactness and normalization arguments here supply the proof.

## 8. Unit cohomology and infinite class field towers

We finish the tower argument stated in lesson 19. Here \(K\) is a number field, \(p\) a prime, and an everywhere-unramified extension includes splitting at real places. For a finite \(p\)-group \(G\), put
\[
d=\dim_{\mathbf F_p}H^1(G,\mathbf F_p),\qquad
r=\dim_{\mathbf F_p}H^2(G,\mathbf F_p).
\tag{40}
\]
Both coefficients have trivial action.

### Theorem 24.7. The finite-group Golod–Shafarevich bound

If \(G\) is a nontrivial finite \(p\)-group, then
\[
r>\frac{d^2}{4}.
\tag{41}
\]

**Proof.** We supply the presentation and filtered-algebra argument. The Frattini quotient
\(G/(G^p[G,G])\) is an elementary abelian group of rank \(d\). Lifts of a basis generate \(G\): a proper generated subgroup is contained in a maximal subgroup, which in a finite \(p\)-group is normal of index \(p\), and that subgroup cannot contain a basis of the quotient. To check the index assertion, induct using the nontrivial center; if the center is not contained in the maximal subgroup its product with that subgroup is the whole group, forcing index \(p\); otherwise pass to the central quotient.

Take the free pro-\(p\) group \(F\) on these \(d\) generators, with kernel \(R\) onto \(G\). Its completed group algebra is the noncommutative power-series algebra
\[
T=\mathbf F_p\langle\!\langle X_1,\ldots,X_d\rangle\!\rangle,
\qquad x_i\longmapsto1+X_i.
\tag{42}
\]
Here is the universal construction behind this identification. In every finite nilpotent augmentation quotient of \(T\), the group \(1+(X_1,\ldots,X_d)\) is a finite \(p\)-group, so freeness gives the map from \(F\). Conversely substitute \(x_i-1\) in power series in the completed group algebra. Both continuous algebra maps are inverse on their generators and on the dense polynomial algebra. The augmentation topology agrees with the finite-group-quotient topology: in a finite \(p\)-group algebra the augmentation ideal is nilpotent. Indeed choose a central \(z\) of order \(p\); \((z-1)^p=0\), and induction on \(G/\langle z\rangle\) puts a sufficiently high augmentation power in \((z-1)\), whose \(p\)th power is zero. Conversely the augmentation quotients on \(d\) generators have finite dimension, bounded by the number of words of bounded length. This proves the topology assertion used in (42).

The augmentation ideal in \(T\), as a right module, is freely \(\bigoplus_i X_iT\), by the unique first letter of each word. Thus
\(0\to T^d\to T\to\mathbf F_p\to0\)
is a free resolution, proving \(H^2(F,\mathbf F_p)=0\). The low-degree sequence (6) for \(1\to R\to F\to G\to1\), valid also for continuous cochains by finite-quotient passage, identifies
\[
H^2(G,\mathbf F_p)
=\operatorname{Hom}_{\mathrm{cont}}
   (R/\overline{R^p[R,F]},\mathbf F_p).
\tag{43}
\]
The preceding \(H^1(G)\to H^1(F)\) is an isomorphism because the chosen generators are minimal. Hence \(R/\overline{R^p[R,F]}\) has rank \(r\). Choose \(r\) relators \(\rho_j\) lifting a basis. They normally generate \(R\). To prove this last claim, quotient by their closed normal closure. If the remaining image of \(R\) were nontrivial, it would be detected in a finite \(p\)-group quotient. Its nonzero Frattini quotient has nonzero coinvariants under the ambient \(p\)-group: the augmentation ideal of that finite group algebra is nilpotent, so a nonzero finite module cannot equal its augmentation multiple. Those coinvariants would be a nonzero quotient of (43)'s relation module with all the chosen basis classes zero, a contradiction.

Put \(f_j=\rho_j-1\in T\). Minimality puts each \(f_j\) in augmentation degree at least two, since \(R\subseteq\overline{F^p[F,F]}\). The algebra
\(A=\mathbf F_p[G]\) is \(T\) modulo the closed two-sided ideal of these \(r\) series. Let \(I\) be its augmentation ideal, and
\[
b_n=\dim_{\mathbf F_p}(A/I^{n+1}),\qquad b_{-1}=b_{-2}=0.
\]
Write \(f_j=\sum_i X_i f_{ij}\); every \(f_{ij}\) has degree at least one. There is an exact sequence of right \(A\)-modules
\[
A^r\xrightarrow{(f_{ij})}A^d
\xrightarrow{(v_i)\mapsto\sum X_iv_i}I\to0.
\tag{44}
\]
For exactness in the middle, lift a kernel vector to \(T^d\); the series \(\sum X_iv_i\) lies in the relator ideal. The first-letter derivative obeys
\(\partial_i(uv)=(\partial_i u)v+\epsilon(u)\partial_i v\).
Differentiating a sum of \(u f_j v\) and reducing modulo the relator ideal leaves exactly combinations of the columns \((f_{ij})\). Passage to limits is valid because the target \(A^d\) is finite-dimensional. This proves (44), including the absence of an additional hidden relation module.

The induced surjection
\(A^d/I^nA^d\to I/I^{n+1}\)
has kernel of dimension \(d b_{n-1}-(b_n-1)\). Any vector in that kernel lifts to an actual kernel vector: subtract a vector in \(I^nA^d\) expressing its error, using \(I^{n+1}=\sum_i X_iI^n\). Equation (44) generates these lifts, and its column entries lie in \(I\), so its image modulo \(I^nA^d\) has dimension at most \(r b_{n-2}\). Therefore, for every \(n\geq0\),
\[
b_n-d b_{n-1}+r b_{n-2}\geq1.
\tag{45}
\]
For \(n=0\) this is \(b_0=1\). Let
\(H_A(t)=\sum_{n\geq0}\dim(I^n/I^{n+1})t^n\).
Since \(I\) is nilpotent it is a polynomial with positive constant term, and
\(\sum b_nt^n=H_A(t)/(1-t)\). Sum (45) for \(0<t<1\) to obtain
\[
(1-dt+rt^2)H_A(t)\geq1.
\tag{46}
\]
If \(d\geq3\) and \(r\leq d^2/4\), put \(t=2/d\); the left factor is nonpositive, a contradiction. If \(d=2\), \(r\leq1\) gives the same contradiction as \(t\to1\). If \(d=1\), \(G\) is nontrivial cyclic and its periodic resolution gives \(r=1>1/4\). This proves (41) in every case. \(\square\)

### Theorem 24.8. The terminal unramified relation bound

If the maximal everywhere-unramified pro-\(p\) extension \(M/K\) is finite, with group \(G\), then
\[
r-d\leq r_1(K)+r_2(K)\leq[K:\mathbf Q].
\tag{47}
\]

**Proof.** The class group of \(M\) has order prime to \(p\). Otherwise its Hilbert class field supplies an everywhere-unramified cyclic degree-\(p\) extension of \(M\). The compositum of its finitely many conjugates over \(K\) is still everywhere unramified, and its group over \(K\) is a \(p\)-group, contradicting maximality.

Let \(U_M\) be the product of all finite local unit groups and all archimedean multiplicative groups, and \(E_M=\mathcal O_M^\times\). Every finite decomposition group is unramified cyclic, and its local unit Tate groups vanish as in Proposition 24.1. Every archimedean decomposition group is trivial because real places split. Shapiro makes \(U_M\) Tate-acyclic. Infinite products introduce no obstruction: the finite-group complete resolution has finitely generated free terms in each degree, so its cochains commute with these products; choose the local primitives componentwise. The finite class group \(\operatorname{Cl}(M)\) is also Tate-acyclic for the \(p\)-group, since its order is prime to \(p\) and every Tate group is killed by \(|G|\).

Break the idelic ideal sequence into
\[
1\to E_M\to U_M\to C_M^{\mathrm{unit}}\to1,
\qquad
1\to C_M^{\mathrm{unit}}\to C_M\to\operatorname{Cl}(M)\to1.
\]
Its Tate sequences give \(\widehat H^q(G,C_M)=\widehat H^{q+1}(G,E_M)\). In degree minus one, (26) consequently gives
\[
H_2(G,\mathbf Z)
=\widehat H^{-3}(G,\mathbf Z)
\simeq\widehat H^{-1}(G,C_M)
\simeq E_K/N_{M/K}E_M.
\tag{48}
\]
The unit group \(E_K\) has free rank \(r_1+r_2-1\) and cyclic finite torsion, by the unit theorem already used in lesson 14. Thus the finite \(p\)-group on the right of (48) needs at most \(r_1+r_2\) generators.

For completeness, the coefficient sequence
\(0\to\mathbf Z\xrightarrow{p}\mathbf Z\to\mathbf F_p\to0\)
gives
\[
0\to H^2(G,\mathbf Z)/p\to H^2(G,\mathbf F_p)
\to H^3(G,\mathbf Z)[p]\to0.
\tag{49}
\]
The rational coefficient sequence identifies
\(H^2(G,\mathbf Z)=\operatorname{Hom}(G^{\mathrm{ab}},\mathbf Q/\mathbf Z)\)
and
\(H^3(G,\mathbf Z)=\operatorname{Hom}(H_2(G,\mathbf Z),\mathbf Q/\mathbf Z)\).
Indeed positive rational cohomology vanishes by averaging, and applying \(\operatorname{Hom}(-,\mathbf Q/\mathbf Z)\) to the free bar chain complex takes its homology to its cohomology, since a character extends from a subgroup by divisibility. Finite \(p\)-groups and their character duals have the same number of cyclic factors. The first term of (49) therefore has dimension \(d\), and the last has dimension at most \(r_1+r_2\) by (48). This proves (47). \(\square\)

### Theorem 24.9. An infinite Hilbert class field tower

The ordinary Hilbert class field tower is infinite for
\[
K=\mathbf Q\!\left(\sqrt{-5\cdot13\cdot17\cdot29\cdot37\cdot41}\right),
\]
**Proof.** Proposition 19.3 gives genus rank six from the seven prime discriminants, \(-4\) and the six positive primes displayed above. Hence the maximal unramified pro-2 group has \(d\geq6\). If it were finite, (47) would give \(r\leq d+2\), whereas (41) gives \(r>d^2/4\); for every \(d\geq6\), \(d^2/4>d+2\). This is impossible. Its pro-2 extension is infinite. The ordinary Hilbert class field tower is therefore infinite as well: a stabilized finite top field has class number one, but base change of the infinite unramified pro-2 extension gives an infinite pro-2 extension of that top field. Such a group has a nontrivial finite \(p\)-group quotient and therefore a cyclic order-\(p\) quotient, contradicting class number one. This closes the tower argument using the genus calculation of lesson 19 and the proofs (41), (47) here. \(\square\)

## 9. Exercises with solutions

### Exercise 1. Local quaternion invariants — easy

Compute the invariant of \((a,b)_{\mathbf Q_p}\) from the Hilbert symbol, including a formula that can be used at every prime.

**Solution.** It is zero for symbol 1 and \(1/2\) for symbol \(-1\), by (21). For odd \(p\), write \(a=p^\alpha u\), \(b=p^\beta v\), with units \(u,v\). Lesson 11 proves
\[
(a,b)_p=(-1)^{\alpha\beta(p-1)/2}
\left(\frac{\bar u}{p}\right)^\beta
\left(\frac{\bar v}{p}\right)^\alpha.
\]
At 2, with odd units \(u,v\), its exponent of \(-1\), modulo two, is
\[
\frac{u-1}{2}\frac{v-1}{2}
+\alpha\frac{v^2-1}{8}+\beta\frac{u^2-1}{8}.
\]
Each quotient is integral and depends only on the appropriate odd residue class. Choose invariant \(1/2\) exactly when the indicated parity is odd. Negative valuations cause no change in these parity computations. This includes every \(a,b\ne0\).

### Exercise 2. The infinite places — medium

Prove \(\operatorname{Br}(\mathbf R)=\mathbf Z/2\) and \(\operatorname{Br}(\mathbf C)=0\), and identify the invariant of Hamilton's algebra.

**Solution.** Over an algebraically closed field a division representative is the field: factor the minimal polynomial of an element into linear factors and use absence of zero divisors. Thus every complex central simple algebra is a matrix algebra. Every real class is consequently split by \(\mathbf C\); the relative crossed-product theorem and cyclic resolution give
\(\operatorname{Br}(\mathbf R)=\mathbf R^\times/N\mathbf C^\times\).
The norm \(z\mapsto |z|^2\) has image precisely \(\mathbf R_{>0}\), so the quotient has order two. Its negative parameter gives relations \(i^2=j^2=-1\), \(ji=-ij\), hence Hamilton's algebra. It is the nonzero class, assigned invariant \(1/2\). No classification of arbitrary real division algebras was needed.

### Exercise 3. Hamilton's ramification — medium

Determine every ramified place of \((-1,-1)_{\mathbf Q}\) directly from local formulas.

**Solution.** For odd \(p\), both valuations are zero, and the odd-prime formula of Exercise 1 is 1. At 2, the unit cross term is \((-2/2)(-2/2)=1\) modulo two; the valuation terms are zero, so the symbol is \(-1\). At infinity two negative entries give symbol \(-1\). Thus exactly 2 and infinity have invariant \(1/2\); their sum is 1, zero in \(\mathbf Q/\mathbf Z\). All other places have invariant zero. This both determines the set and checks the global sum law in this example.

### Exercise 4. The local degree-two bound — hard

For every finite Galois extension of nonarchimedean local fields, prove that \(|H^2(G,L^\times)|\) divides \([L:K]\), including positive characteristic and noncyclic groups. Explain why that bound alone is not the local invariant theorem.

**Solution.** In a prime cyclic extension, Hilbert 90 kills \(H^1\), and cyclic periodicity identifies \(H^2\) with the norm quotient. Local reciprocity gives its order \(p\). Induct in a \(p\)-group using a normal index-\(p\) subgroup. Equation (5) makes the restriction kernel a group of order \(p\), while its image has order dividing the smaller group order. Hence the total order divides \(|G|\). For a general group, restriction injects each primary part into its Sylow-group cohomology by (2), giving the corresponding Sylow bound. Multiplying gives the stated divisibility and finiteness. This argument uses neither characteristic-zero logarithms nor solvability. To obtain an invariant isomorphism, one still has to exhibit a subgroup of the full degree: Theorem 24.2 does this by comparing with the unramified extension of equal degree and using (11). The bound then forces equality.

## Editable edition

The reading edition provides the complete LaTeX source of this lesson, the cumulative course LaTeX and the editable source ZIP. The archive contains all twenty-four Markdown lessons, complete LaTeX bodies, original diagrams, metadata and reproduction instructions.

## References

The local invariant, global Brauer exact sequence and Tate fundamental-class theorem are proved using the exact internal algebra and cochain prerequisites. The number-field Weil construction, complete filtered group-algebra inequality and arithmetic unit-cohomology relation bound are supplied here; a survey statement is not counted as their proof.

- [J. S. Milne, Class Field Theory, version 4.03](https://www.jmilne.org/math/CourseNotes/CFT.pdf).
- [John Tate, Number theoretic background (1979), freely available paper](https://ncatlab.org/nlab/files/TateNumberTheory.pdf).
- [Mikhail Ershov, Golod–Shafarevich groups: a survey, author preprint (2012)](https://m-ershov.github.io/Research/gssurvey_revised.pdf).

The [proof guide](../FREE_PROOFS.md) gives the lesson sequence and the exact prerequisite record. External references accompany the written arguments.
