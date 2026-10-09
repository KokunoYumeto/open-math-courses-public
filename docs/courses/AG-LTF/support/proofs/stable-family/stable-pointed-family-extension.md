# Stable pointed-family extension after a separable projective alteration

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Self-checked by the writing AI. Public domain (CC0 1.0).*

Independent exposition, CC0 1.0. We prove extension of a smooth ordered pointed family after a projective alteration with separable function field.

The [numerical model arguments](owned/AG-GS/numerical-completion-NS11a.md) and [genus and torsion arguments](numerical-source-corrections.md), together with [Regular surface models](regular-surface-models.md), supply the model inputs used in Section 3.

<a id="S1"></a>

## 1. The extension problem and elliptic tails

Let \(k\) be algebraically closed, let \(S\) be an integral projective \(k\)-scheme, and let \(U\) be a nonempty open. Suppose
\[
 (C_U\longrightarrow U;s_1,\ldots,s_n)
\]
is a smooth proper geometrically connected genus-\(g\) family with disjoint ordered sections, where \(g\) is any nonnegative integer and \(n\ge3\). We seek an integral projective \(S'\) and a proper dominant generically finite morphism \(S'\to S\), with \(k(S')/k(S)\) separable, on which this family extends, after restricting the original \(U\) if needed, to a projective stable \(n\)-pointed family. Restricting \(U\) is harmless for the generic-curve and graph construction.

Replace \(S\) first by its normalization. Normalization of a variety over a field is finite; this is a projective birational modification and makes no extension of the function field. We will normalize a later projective scheme as well. Thus all final bases in the proof are normal excellent Noetherian schemes.

Choose a smooth pointed elliptic curve \((E,e)\) over \(k\). In characteristic different from two one may use \(y^2=x^3-x\) with e at infinity; in characteristic two use \(y^2+y=x^3\), again with the point at infinity. Both projective cubics are smooth. Attach a copy of \(E\) at each \(s_i\). The result
\[
 D_U=C_U\underset{s_1=e_1}{\cup}E_1\underset{\cdots}{\cup}E_n
 \longrightarrow U
\tag{S.1}
\]
has genus \(G=g+n\ge3\). Its dual graph is a star, so it has compact type. Each elliptic tail has one attaching branch and dualizing degree one. On the core the dualizing degree is \(2g-2+n>0\). Hence every component is stable, including a rational core when \(g=0\). The pushout at sections is the local algebra \(A[x]\times_A A[y]=A[x,y]/(xy)\); it is flat, projective and nodal. Projectivity follows by gluing ample bundles with equal identified fibres at the sections. Flatness and the arithmetic-genus formula also follow from the normalization exact sequence.

We therefore need only the unpointed stable genus-\(G\) stack, its normalized level cover, and a scheme alteration of an algebraic-space graph. The \(n\) labelled, persistent attaching nodes will recover the pointed core after extension. This avoids both a characteristic-zero projectivity theorem for pointed moduli and an unsupported appeal to de Jong's theorem.

<a id="S2"></a>

## 2. Constructing the proper stack of unpointed stable curves

For stabilization, uniqueness and tricanonical frames use [Stable reduction and properness](../../AG-AS--AG-AS-10.html#2-stabilization-over-an-arbitrary-base); for nodal deformations and smoothing, [The stack of curves](../../../../AG-AS/the-stack-of-curves.html#4-nodal-curves-and-smoothness-over-the-integers); for quotients and trivial inertia, [Algebraic stacks](../../../../AG-AS/algebraic-stacks.html#2-algebraic-stacks-and-trivial-inertia); for the étale-atlas criterion, [Quotient and DM stacks](../../../../AG-AS/quotient-and-dm-stacks.html#2-cutting-an-%C3%A9tale-atlas); and for the fixed-polynomial Hilbert proof, [Hilbert and Quot schemes](../../../../AG-HP/hilbert-and-quot-schemes.html#4-the-flattening-stratum-is-the-quot-scheme).

For \(G\ge2\), the following course proofs apply:

- *Stable reduction and properness*, Lemma 5.1 and Proposition 5.2: \(\omega^3\) is very ample, \(H^1(\omega^3)=0\), \(h^0=5G-5\), and framed tricanonical families form a finite-type Hilbert/Isom scheme \(Q\).
- *Stable reduction and properness*, Theorems 2.3 and 3.2: relative stabilization and marked stable-model uniqueness.
- *The stack of curves*, Sections 4 and 6.4: the nodal cotangent-complex calculation, independent local smoothing parameters, unobstructedness, and density of smooth curves. These calculations are statements about the actual projective families and remain usable after the quotient presentation constructed here.
- *Algebraic stacks*, Proposition 5.1 and Theorem 2.3: algebraicity of a quotient by a smooth group and the trivial-inertia criterion.
- *Quotient and DM stacks*, Theorem 2.2: the unramified-diagonal criterion for an étale atlas.

For the algebraicity assertion needed here, \(Q\) is constructed directly from the fixed-polynomial Hilbert scheme, the stable open, a sheaf isomorphism \(\mathcal O_C(1)\simeq\omega_C^3\), and the open determinant condition specifying a frame. For an abstract stable family, its fibre product with \(Q\) is exactly the frame torsor of \(f_*\omega^3\), including the scalar in the sheaf isomorphism. Consequently
\[
 \mathcal X_G=[Q/\operatorname{GL}_{5G-5}]
\tag{S.2}
\]
is the stable-curve stack on every test scheme. This proves its algebraicity and finite type directly. Isomorphisms are represented by the Hilbert graph construction. Infinitesimal automorphisms vanish: on the normalization a vector field must vanish at every node branch; its line-bundle degree is negative on a positive-genus component or it has at least three zeros on a rational component. Thus the diagonal is unramified and the étale-atlas criterion makes \(\mathcal X_G\) Deligne–Mumford. The nodal deformation calculation makes it smooth over \(k\), hence normal on an étale atlas.

The Isom schemes obtained from Hilbert graphs are separated and of finite presentation. Thus the diagonal of \(\mathcal X_G\) is itself a separated finite-type morphism. Apply [Stable reduction and properness, Theorem 6.0 and Proposition 6.1](../../AG-AS--AG-AS-10.html#6-2-separatedness-from-marked-uniqueness) to this diagonal. The dense test locus consists of smooth curves; a test square retains the specified generic isomorphism between two stable models. Theorem 3.2 extends precisely that isomorphism, so the diagonal is proper. This establishes separation before applying the properness criterion to the structural morphism.

Now use [Stable reduction and properness, Theorem 6.0](../../AG-AS--AG-AS-10.html#6-1-the-precise-valuative-input), whose Sections 6.1.1–6.1.7 include the space cover, valuation descent and return of the specified generic comparison. The stack and its smooth open are finite type over the Noetherian field, and the smooth open is dense by the nodal smoothing calculation. Section 3 supplies a model after a dominating trait extension for each smooth generic curve, and relative stabilization retains its generic identification. These are all the criterion's hypotheses, so \(\mathcal X_G\) is proper. The comparison tags are [Stacks 0CQM](https://stacks.math.columbia.edu/tag/0CQM) for properness and [0E95](https://stacks.math.columbia.edu/tag/0E95) for the dense smooth separatedness test.

The universal curve is the family encoded by this stack and its quotient presentation. Its tricanonical embedding over each frame torsor descends to a projective curve over the stack. Pullback to a scheme is therefore projective, not merely proper.

<a id="S3"></a>

## 3. Semistable models over the traits needed for properness

We prove the semistable existence input over the traits needed for the properness test. The numerical results, including the complete long-chain calculation, are in [Numerical completion of the long weighted chains](owned/AG-GS/numerical-completion-NS11a.md#ns11a). The [genus and torsion comparison](numerical-source-corrections.md#g-torsion) includes the exact regular-model Picard sequence and specialization proof. We use [Regular surface models](regular-surface-models.md) for projective resolution and contraction. The primary comparison for the resulting semistable argument is [Stacks 0CDN](https://stacks.math.columbia.edu/tag/0CDN).

<a id="s-torsion-visible"></a>

**Lemma S.3.1 (visible torsion).** Suppose \(C/K\) is smooth, proper and geometrically connected, with genus \(G\), and \(\ell\) is prime to \(\operatorname{char}K\). One finite separable extension of \(K\) gives a rational point of \(C\) and identifies its line-bundle \(\ell\)-torsion with \((\mathbf Z/\ell)^{2G}\).

**Proof.** A smooth nonempty finite-type \(K\)-scheme has a closed point with separable residue field. For a curve, choose an étale coordinate neighbourhood into \(\mathbf A^1_K\); over a suitable closed point of its open image with separable residue, a point of the finite étale fibre has finite separable residue over \(K\). Such a point in that open exists also over a finite field, by choosing a sufficiently large finite separable extension. Adjoin its residue field. A rational point now rigidifies line bundles. Pass temporarily to the separable closure \(K^{\mathrm s}\). Over this separably closed field, the [The Picard functor and the Picard scheme of a curve, Theorems 2.1, 6.2 and 7.2](../../../../AG-HP/the-picard-functor-and-the-picard-scheme-of-a-curve.html#7-degree-pieces-abel-fibres-and-properness) represents degree-zero classes by the genus-\(G\) Jacobian. The [Abelian varieties, Sections 6–7](../../../../AG-GS/AG-GS-06.html#7-torsion-points-and-tate-modules) give an étale \(\ell\)-kernel whose \(K^{\mathrm s}\)-points form \((\mathbf Z/\ell)^{2G}\). Take a basis of these classes, with normalized line-bundle representatives and their \(\ell\)-power trivializations. Line bundles, isomorphisms and their finitely many group relations have finite presentation. Their defining data therefore descend from the filtered union \(K^{\mathrm s}\) to one finite separable extension of \(K\). The descended classes generate the full displayed torsion group: after extension they form its basis, and equality of normalized classes is faithfully flat detectable by Theorem 2.1's descent proof. There can be no further \(\ell\)-torsion class over this finite extension, since its injection into the classes over \(K^{\mathrm s}\) has already been exhausted. Torsion of a line bundle necessarily has degree zero. This proves the assertion. [Comparison: Stacks 0CDU](https://stacks.math.columbia.edu/tag/0CDU). \(\square\)

<a id="s-reduced-torsion"></a>

**Lemma S.3.2 (the reduced-curve rank and its equality case).** Let \(Y\) be a connected reduced proper curve over an algebraically closed field \(F\). Set \(h=h^1(Y,\mathcal O_Y)\), and let \(a\) be the sum of the genera of its normalized components. For \(\ell\ne\operatorname{char}F\),
\[
 \dim_{\mathbf F_\ell}\operatorname{Pic}(Y)[\ell]\le h+a.
\]
Equality means exactly that every singularity is a multicross, including an arbitrary number of smooth branches.

**Proof.** Let \(v\) be the number of components of the normalization \(\widetilde Y\). At a singular point \(x\), let \(r_x\) count its normalization branches and put \(\delta_x=\dim_F(\nu_*\mathcal O_{\widetilde Y}/\mathcal O_Y)_x\). The additive normalization sequence, with global functions \(F\) on \(Y\) and \(F^v\) on \(\widetilde Y\), gives
\[
 h=a+\sum_x\delta_x-v+1.
\tag{S.3.2a}
\]
The complete normalization algebra is \(B_x=\prod_{j=1}^{r_x}F[[t_j]]\). Write \(A_x=\widehat{\mathcal O}_{Y,x}\subset B_x\). Its residues all coincide, since it is local with residue field \(F\). Therefore
\[
 A_x\subset A'_x=F+\prod_j t_jF[[t_j]],\qquad
 \dim_F(B_x/A'_x)=r_x-1.
\]
Consequently \(e_x=\delta_x-(r_x-1)=\dim_F(A'_x/A_x)\ge0\). Equality \(e_x=0\) says \(A_x=A'_x\), the multicross ring.

Here is the corresponding multiplicative calculation. Use a common conductor ideal to replace the local unit quotient \(B_x^*/A_x^*\) by the quotient of units of two finite-dimensional \(F\)-algebras. The residue units contribute \((F^*)^{r_x}/F^*\), a torus of rank \(r_x-1\). Units congruent to one are filtered by powers of the nilpotent radical; each successive quotient is an additive \(F\)-vector space. Raising to the \(\ell\)-th power is bijective on this latter part: it is multiplication by \(\ell\) on each successive quotient, and finite induction proves both injectivity and surjectivity. On the torus it is surjective, with \(\ell\)-kernel of rank \(r_x-1\).

Taking the cohomology of
\(1\to\mathcal O_Y^*\to\nu_*\mathcal O_{\widetilde Y}^*\to\nu_*\mathcal O_{\widetilde Y}^*/\mathcal O_Y^*\to1\)
gives the kernel of \(\operatorname{Pic}(Y)\to\operatorname{Pic}(\widetilde Y)\) as these local unit groups modulo the component rescalings \((F^*)^v/F^*\). The singularities' incidence graph is connected. A spanning tree eliminates exactly \(v-1\) independent rescalings with coefficient one, so the remaining torus has rank
\[
 t=\sum_x(r_x-1)-v+1.
\]
There is no additional finite quotient: the same tree elimination gives an integral basis for the quotient lattice. The nilpotent unit part still has bijective \(\ell\)-multiplication. Thus the entire kernel is \(\ell\)-divisible, and its \(\ell\)-torsion has rank \(t\). The sheaf quotient is supported at finitely many points, hence has no first cohomology, so the map to the normalization Picard group is surjective. Given a torsion class downstairs, lift it and divide the \(\ell\)-multiple of that lift in the kernel; this proves exactness on \(\ell\)-torsion. Each normalized component has Jacobian torsion rank twice its genus by Lemma S.3.1. We obtain
\[
 \dim_{\mathbf F_\ell}\operatorname{Pic}(Y)[\ell]=2a+t,
 \qquad h=a+t+\sum_xe_x.
\tag{S.3.2b}
\]
These formulas prove both the bound and its equality statement. The conductor calculation also proves the converse without choosing or omitting a sequence of point gluings. [Comparison: Stacks 0C20](https://stacks.math.columbia.edu/tag/0C20). \(\square\)

Choose a prime \(\ell>768G\) different from the trait's residue characteristic. Lemma S.3.1 makes all \(\ell\)-torsion and a rational point visible after a finite separable extension. Take a minimal projective regular model \(X\) over the resulting complete trait, using the surface construction below. If its fibre is \(\sum m_iC_i\), the rational point extends to a section by properness. Pulling the fibre divisor back along that section gives
\(1=\sum_i m_i\operatorname{length}(s^*C_i)\), so \(\gcd_i m_i=1\).

Write \(T\) for the model's numerical type and \(b\) for the graph genus. The [numerical Picard calculation](owned/AG-GS/numerical-completion-NS11a.md#n-picard) gives
\(\dim_{\mathbf F_\ell}\operatorname{Pic}(T)[\ell]\le b\).
The [model torsion sequence and specialization injection](numerical-source-corrections.md#g-torsion) therefore place at least \(2G-b\) independent classes in \(\operatorname{Pic}(X_{F,\mathrm{red}})[\ell]\). Those proofs extend generic line bundles by divisors, use the intersection-matrix kernel for exactness, and prove specialization by compatible infinitesimal trivializations and formal functions. Put \(h=h^1(X_{F,\mathrm{red}},\mathcal O)\), and let \(a\) sum its normalization genera. Lemma S.3.2 and the [model genus comparisons](numerical-source-corrections.md#g-reduction-genus) now give
\[
 2G-b\le h+a,\qquad G\ge h\ge b+a.
\tag{S.3}
\]
Writing \(u=G-h\) and \(v=h-b-a\), the first inequality becomes \(2u+v\le0\). Both numbers are nonnegative, so both vanish. The strict inequality for a nonreduced minimal fibre proves \(m_i=1\) for every component. The geometric-genus equality makes each component smooth; the equality in Lemma S.3.2 makes every singularity a multicross.

The special fibre is a Cartier divisor in a regular surface, so its local rings are Gorenstein. At an \(r\)-branch multicross, dividing by the parameter \(x_1+\cdots+x_r\) leaves a square-zero maximal ideal of dimension \(r-1\). Its socle is that ideal. A zero-dimensional Gorenstein ring has one-dimensional socle, so a singular multicross here has \(r=2\). Thus the fibre is nodal. This is the semistable model, and relative stabilization supplies the stable model.

**Residue-field hypothesis S.3a.** The equality argument just used assumes algebraically closed residue field. Over an arbitrary residue field, an equality \(w_ig_i=[\kappa_i:F]_{\mathrm s}g_i\) does not force \(\kappa_i/F\) separable when \(g_i=0\). Accordingly the unrestricted nonminimal equality statement is not an input here. Nor does removing an arbitrary rational component prove it: that component need not be a leaf of a rooted tree.

For the properness test, first complete the equicharacteristic DVR. The ground field \(k\) is perfect; a coefficient field containing \(k\) identifies this completion with \(F[[\pi]]\). Replacing \(F\) by its algebraic closure gives the dominating DVR \(\overline F[[\pi]]\). Apply the preceding proof and its finite extension to that trait. The dense-locus stack criterion explicitly permits such valuation and fraction-field extensions. All component constant fields in the numerical equality calculation are now the residue field, so \(w_i=1\). These valuation extensions are used only to prove properness. Section 8 obtains the final alteration's function field from finite étale level structures and the separable scheme cover; no arbitrary-residue-field stable-reduction assertion is needed.

**Surface-model bridge S.3b.** The complete resolution and contraction arguments are in [Regular surface models](regular-surface-models.md). Start with a projective closure of the smooth generic curve and normalize it. Excellence makes that normalization finite. The main-component resolution proof gives a finite succession of normalized point blowups, each projective because both blowup and finite normalization are projective. Its resulting regular surface is projective over the trait. The proved contraction of an exceptional curve of the first kind preserves regularity and projectivity, and removes one special-fibre component. Finitely many such contractions give the minimal regular proper model used above. The primary comparison tags are [0BGP](https://stacks.math.columbia.edu/tag/0BGP), [0BGN](https://stacks.math.columbia.edu/tag/0BGN) and [0C2M](https://stacks.math.columbia.edu/tag/0C2M).

<a id="S4"></a>

## 4. Automorphisms are detected by invertible level structures

Human primary comparisons: [Pierre Deligne and David Mumford, Theorem (1.13), printed pp.85–87](https://people.mpim-bonn.mpg.de/gaitsgde/grad_2009/Deligne-Mumford.pdf); [Pierre Deligne, Le lemme de Gabber, §§3.3–3.5](https://www.numdam.org/item/AST_1985__127__131_0/). [Abelian varieties, Sections 6–7](../../../../AG-GS/AG-GS-06.html#6-the-degree-and-%C3%A9taleness-of-multiplication) supply the precise abelian inputs. 

We reconstruct the rigidity needed in Deligne, *Le lemme de Gabber*, Sections 3.3–3.5. The arguments below apply to stable unpointed curves of genus \(G\ge2\) in every characteristic.

**Lemma S.4.** An automorphism of a stable curve acting identically on \(\operatorname{Pic}^0\) is the identity.

For a smooth curve \(Y\) of genus at least two there is a short algebraic proof. If a nontrivial automorphism \(h\) acts trivially on its Jacobian, let \(r\) be its finite order and let \(Y\to Z=Y/\langle h\rangle\) be the finite separable quotient. Norm and pullback satisfy \(\operatorname{pullback}\circ\operatorname{norm}=\sum_{j=0}^{r-1}(h^j)^*=[r]\) on \(\operatorname{Jac}(Y)\). Multiplication by \(r\) is surjective, including when \(r\) is divisible by the characteristic. Hence \(\operatorname{Jac}(Z)\to\operatorname{Jac}(Y)\) is surjective and \(g(Z)\ge g(Y)\). The opposite inequality follows from Riemann–Hurwitz; more precisely \(2g(Y)-2\ge r(2g(Z)-2)\). These two inequalities contradict \(r>1\) and \(g(Y)\ge2\). For a smooth genus-one component, an automorphism with trivial Jacobian action is a translation; a fixed attaching point makes it the identity.

For a general stable curve, form the graph \(\Gamma\) whose vertices are its irreducible components and whose edges are nodes joining **different** components. Internal nodes stay in the Picard variety of the corresponding irreducible component. The kernel of restriction \(\operatorname{Pic}^0(C)\to\prod_i\operatorname{Pic}^0(C_i)\) is the torus with character lattice \(H_1(\Gamma,\mathbf Z)\). Thus the automorphism acts identically on \(H_1(\Gamma,\mathbf Z)\). Each vertex whose component has nontrivial \(\operatorname{Pic}^0\) is fixed, because the restriction quotient has that factor. Every vertex of valence at most two is such a vertex: a smooth rational component of that valence would violate stability, while a rational component with an internal node has a nontrivial torus in its \(\operatorname{Pic}^0\).

The following finite-graph fact now applies: a graph automorphism which fixes every vertex of \(\operatorname{valence}\le2\) and acts identically on \(H_1\) is the identity. Delete a fixed isolated vertex or a fixed leaf with its edge; its neighbouring vertex is fixed too. At a fixed valence-two vertex, either its two edges join the same neighbour, in which case exchanging them reverses a nonzero cycle and is excluded, or suppress the vertex and join its neighbours. Fixed endpoints introduced by a deletion retain their fixed status. One may also delete an edge whose endpoints and orientation are fixed. These operations preserve the hypotheses and reduce vertices plus edges. If none applies, every remaining component has minimum valence at least three, and there is no edge fixed with its orientation. The trace on the graph's cellular complex gives
\[
 \#\{\text{fixed vertices}\}+\#\{\text{reversed edges}\}
 =\operatorname{Tr}(H_0)-\operatorname{Tr}(H_1)<0,
\]
because each such component has first Betti number greater than one, \(\operatorname{Tr}(H_0)\le b_0\), and the action on \(H_1\) is the identity. The left side is nonnegative, a contradiction. This proves the graph fact and fixes every external node and component.

On a fixed component, the identity action on its own \(\operatorname{Pic}^0\) fixes each internal node and its two ordered branches: the torus character of an internal node distinguishes it, and reversing branches changes its sign. On its smooth normalization, the positive-genus argument just given applies. In genus one there is an attaching or internal-node branch, so the possible translation is zero. In genus zero every attaching and internal branch is fixed, and stability provides at least three such points; an automorphism of \(\mathbf P^1\) fixing three distinct points is the identity. The component maps and all gluings are therefore the identity. This proves the lemma. The primary comparison is Deligne–Mumford, Theorem (1.13) and its graph proof, printed pp.85–87; the norm/Riemann–Hurwitz argument above replaces that paper's smooth-component Lefschetz argument.

**Lemma S.5.** If \(N\ge3\) is invertible in \(k\), an automorphism of a stable curve acting trivially on \(\operatorname{Pic}^0(C)[N]\) is the identity.

The nodal Picard gluing sequence expresses \(J=\operatorname{Pic}^0(C)\) as an extension \(0\to T\to J\to A\to0\) of an abelian variety by a torus. Its invertible torsion sequence is exact. Let \(h\) be the induced finite-order automorphism. Choose an odd prime \(\ell\) dividing \(N\), if there is one; otherwise \(4\mid N\). On the character lattice of \(T\) and the Tate module of \(A\), \(h\) is congruent to one modulo \(\ell\), or modulo four in the second case.

The relevant congruence kernel is torsion-free. Indeed write \(B=1+\ell^aV\) with \(V\) nonzero modulo \(\ell\), \(a\ge1\) for odd \(\ell\) or \(a\ge2\) for \(\ell=2\). If \(B\) had finite order, take a nonidentity power of prime order \(q\) and write that power afresh in this form, with \(V\) nonzero modulo \(\ell\). For \(q\ne\ell\) the first term of \(B^q-1\) is \(q\ell^aV\) and higher terms have larger valuation. For \(q=\ell\) it is \(\ell^{a+1}V\) and again all later terms have larger valuation, using \(\ell\ge3\) or \(a\ge2\). Neither can vanish. The same proof works for the integral character lattice by embedding it in its \(\ell\)-adic completion.

The Tate representation detects endomorphisms of A. If an endomorphism vanishes on all \(\ell^r\)-torsion, its kernel contains \(\ell^{2\dim(A)r}\) geometric points for every \(r\). A closed subgroup of dimension \(d\) with c components has at most \(c\ell^{2dr}\) such torsion points. Therefore its reduced identity component is all of A, and the endomorphism vanishes. Thus \(h\) is the identity on both A and \(T\). The homomorphism \(h\)-1 factors through A with values in \(T\). \(\operatorname{Hom}(A,T)=0\) because A is proper and \(T\) is affine. Hence \(h\) is the identity on \(J\), and Lemma S.4 finishes the proof. This proves precisely the \(N\ge3\), \(N\) invertible stabilizer assertion, without excluding wild automorphisms of the original curve. Level two is not included.

<a id="S8"></a>

## 5. Persistent nodes, connected pieces and the pointed core

The Stein inputs are [Proper fundamental groups, Theorem 2.1](../../../../AG-DFG/proper-fundamental-groups.html#2-covers-over-a-complete-local-base) and [Proper fundamental groups, Theorem 5.1](../../../../AG-DFG/proper-fundamental-groups.html#5-the-finite-%C3%A9tale-part-of-stein-factorization).

We first prove a lemma for any projective flat nodal family \(D'/S'\) over a normal excellent integral base, with generically distinct labelled rational persistent nodes and split generic branches. No level space or alteration conclusion is assumed. Later we apply this lemma to the stable family constructed in Section 8; its persistent-node and Stein parts are already available for the compact-type trait calculation in Section 6.

The relative nodal locus \(\Sigma\) of \(D'/S'\) is finite and unramified. Locally at a node its presentation is \(xy=a\) and \(\Sigma\) is \(x=y=0\), namely \(\operatorname{Spec}(A/(a))\); properness and quasi-finiteness make it finite globally. The \(n\) attaching nodes in the generic \(D'\) are rational labelled nodes. Each reduced closure in \(\Sigma\) is finite birational over the normal integral \(S'\), hence is a copy of \(S'\). They give \(n\) node sections. Distinct sections never collide: the diagonal of a separated unramified map is open and closed, so their equality locus is open and closed, and it misses the generic point.

The two branches at a persistent node form a finite étale double cover of \(S'\). Its generic branch labels, inherited from core and tail, split it; normality extends that splitting to all \(S'\). A persistent node section forces the local smoothing parameter a to vanish on all \(S'\). Normalize partially at these \(n\) disjoint split nodes. Locally this is the finite map
\[
 A[x,y]/(xy)\longrightarrow A[x]\oplus A[y].
\tag{S.9}
\]
The local constructions glue because the branches are labelled. The resulting family \(D^\dagger/S'\) is projective, flat and finitely presented; both branches in (S.9) are flat, and elsewhere it is the original nodal family. Its geometric fibres are reduced nodal curves. The preimages of the chosen nodes are disjoint smooth sections.

Use the finite-étale Stein proof for this **already flat, geometrically reduced** family. AG-DFG *Proper fundamental groups*, Theorem 5.1, gives \(f_*\mathcal O\) finite étale with geometrically connected fibres of the evaluation map. In the present excellent Noetherian scope its idempotent-lifting step can be confined to the complete-local Theorem 2.1: pass to the completed strict local ring, lift the special-fibre idempotents there, and use the displayed finite-free cohomology-complex splitting and faithful flat descent.

For the pointed-core conclusion, now assume that \(D'\) is stable and its generic labelled fibre is the elliptic-tail family of Section 1, with these \(n\) attaching nodes. The general persistent-node, partial-normalization and flat-Stein statements above require none of this extra hypothesis and are the part used in Section 6.

The generic decomposition has exactly \(n+1\) labelled connected pieces: the original core and the \(n\) elliptic tails. A finite étale algebra over a normal integral base with this split generic fibre is the product of \(n+1\) copies of its base ring. Therefore \(D^\dagger\) splits globally into open-and-closed projective flat families
\[
 D^\dagger=C'\amalg E'_1\amalg\cdots\amalg E'_n.
\tag{S.10}
\]
The core \(C'\) has geometrically connected nodal fibres and genus \(g\), by Euler-characteristic constancy. The core branches in (S.9) give \(n\) ordered disjoint smooth marked sections. Each geometric component has exactly the same canonical-degree expression as its component in \(D'\): every removed tail branch is replaced by one marked point. Thus
\[
 \deg\bigl(\omega_{C'}(s'_1+\cdots+s'_n)\bigr)|_V
 =2g_V-2+\#\{\text{node branches on }V\}+\#\{\text{marks on }V\}>0.
\tag{S.11}
\]
The inequality holds because \(D'\) was stable. This proves that \(C'\) is a stable ordered \(n\)-pointed family. It agrees with the original marked family over the chosen generic open, with the identifying arrow retained in S.7.

<a id="S5"></a>

## 6. The normal level space and compact-type curves

Picard representation uses [Moduli stacks are algebraic, Theorems 5.2, 7.2 and 7.3](../../../../AG-AS/moduli-stacks-are-algebraic.html#7-picard-stacks-and-picard-spaces), including coherent-sheaf algebraicity and the complete rigidification and fppf descent argument. Compare [Stacks 0D2C](https://stacks.math.columbia.edu/tag/0D2C).

Fix a prime \(\ell\ge3\) distinct from \(\operatorname{char}(k)\). On the smooth open \(\mathcal X_G^{\mathrm{sm}}\) the sheaf \(\operatorname{Pic}^0[\ell]\) is finite étale of rank \(\ell^{2G}\). The sheaf of bases
\[
 L^{sm}=\operatorname{Isom}(\operatorname{Pic}^0[l],(\mathbf Z/l)^{2G})
 \longrightarrow X_G^{sm}
\tag{S.4}
\]
is finite étale and surjective. Normalize \(\mathcal X_G\) in this cover. On a normal excellent étale atlas this means finite normalization in the component function fields; normalization commutes with étale base change, so the normalizations of the atlas and arrow spaces descend. This gives a finite representable surjective map
\[
 L\longrightarrow X_G.
\tag{S.5}
\]
Finite surjectivity follows because every atlas component has a dense smooth open and its finite normalization is dominant and closed.

We need the exact specialization argument killing inertia. For a projective flat nodal family with geometrically connected fibres, the universal-functions identity \(f_*\mathcal O=\mathcal O\) holds after every base change. AG-AS *Moduli stacks are algebraic*, Theorems 7.2–7.3, therefore represents the relative Picard functor, using its flat coherent-sheaf proof Theorem 5.2 and rigidification argument. Its deformation obstruction is \(H^2(\mathcal O)\), which vanishes for curves, so it is smooth. Since \(\ell\) is invertible, its \(\ell\)-torsion is an étale algebraic-space sheaf, locally of finite presentation and initially only locally quasi-finite. Quasi-compactness is established below after the level space is an algebraic space.

On every trait used below, first pass faithfully flat and étale locally so that the relevant branches split and the smooth locus of the closed fibre has a rational point. A smooth point lifts over the henselian trait; its finite-presentation section descends from the strict henselization to an étale neighbourhood. Finitely many components can be treated after one common extension. The section and the rigidification proof represent the Picard class by a normalized line bundle. A torsion class becomes an actual torsion bundle, since the Picard group of a trait is zero. The subsequent arguments concern that representative. Their uniquely extended Picard class descends along the faithfully flat cover. This distinction matters: without a section a Picard-sheaf class need not be a line bundle on its given family.

This torsion sheaf is separated. On a trait with smooth generic fibre, resolve \(xy=\pi^a\) by the nodal blowups of Stable reduction and properness, Section 3. The resulting regular model has reduced special fibre. An \(\ell\)-torsion line bundle trivial generically is \(\mathcal O(\sum b_iC_i)\). If its \(\ell\)-th power is trivial, a trivializing rational function has no horizontal divisor, hence is in the fraction field of the trait. Its divisor is an integral multiple of the entire reduced fibre. Consequently every \(b_i\) is the same integer, so the bundle is trivial. Pullback along the nodal resolution detects triviality because \(r_*\mathcal O=\mathcal O\). If the generic curve is nodal, first split and partially normalize its persistent nodes. The same argument applies to the smooth generic components. Remaining gluing parameters are units of the trait. A generically trivial gluing cocycle is already trivial over the trait: vertex rescalings over the fraction field have equal valuations along each unit edge, and subtracting the common valuation makes them all units. Faithful étale descent handles nonsplit branches. This proves the separation test for the whole \(\ell\)-torsion sheaf.

On a normal atlas of \(L\), write \(j:V\to T\) for the dense inverse image of \(\mathcal X_G^{\mathrm{sm}}\). Separation gives an injection \(\operatorname{Pic}[\ell]\to j_*\operatorname{Pic}[\ell]|_V\). The generic level identification gives
\[
 \operatorname{Pic}[l]\hookrightarrow j_*(\mathbf Z/l)^{2G}
 =(\mathbf Z/l)^{2G}.
\tag{S.6}
\]
The last equality holds on the étale site of a normal scheme: a connected étale piece is normal integral, and its dense open is connected. The construction is natural under the arrow space. Its two pulled-back constant sheaves have the same frame on the dense smooth open; hence their comparison is the identity everywhere on each normal arrow component. Any stabilizer of a geometric point of \(L\) injects into the stable curve's automorphism group, because (S.5) is representable, and acts trivially on the injection (S.6). Lemma S.5 kills it. This also kills the whole inertia, including tests with nilpotents: stable-curve inertia is finite unramified after properness, so the inertia over a level atlas is finite unramified with every geometric fibre the identity point. Its finite algebra is generated by one modulo every maximal ideal; Nakayama makes the unit surjective locally, and the identity section makes it an isomorphism. The trivial-inertia criterion therefore makes \(L\) an **algebraic space**. It is proper over \(k\) because (S.5) is finite and \(\mathcal X_G\) is proper. The universal stable curve pulls back to \(L\).

Before invoking quasi-finiteness or properness of the torsion sheaf, note its quasi-compactness. Pull back to a quasi-compact normal Noetherian étale atlas of \(L\). The separated injection into the finite constant sheaf in (S.6) is an étale monomorphism, hence an open immersion. Every such open in the Noetherian finite constant space is quasi-compact. Quasi-compactness descends to the base of \(L\), and then along the finite surjective map \(L\to\mathcal X_G\). The torsion sheaf is therefore quasi-finite, not merely locally quasi-finite.

The inverse image of the **compact-type** open is finite étale, not only the inverse image of the smooth open. Here is the needed proof, since (S.1) is nodal. On a compact-type geometric fibre, normalization/gluing identifies \(\operatorname{Pic}^0\) with the product of component Jacobians: its dual graph is a tree and the torus is zero. Over a trait in this open, first split the branches. Partially normalize the persistent generic nodes, which are all separating; their sections and branch labels extend on the normal trait by the finite-unramified argument of S.8. The flat partial normalization and finite-étale Stein argument of S.8 then give families with smooth geometrically connected generic fibres. Resolve only their remaining nodes of positive thickness. Each resulting regular special dual graph is a tree. Extend a degree-zero generic line bundle to each regular surface. Its component degrees \(d_i\) have sum zero. The integral graph Laplacian of a tree has image exactly the sum-zero integer lattice: remove a leaf, send its integer degree along its sole edge, and continue. Twisting by the resulting vertical divisor makes every component degree zero. An \(\ell\)-torsion generic bundle thus extends uniquely as \(\ell\)-torsion: its \(\ell\)-th power is a vertical bundle of degree zero, and the connected graph's Laplacian kernel consists of constants, hence it is the whole principal fibre. It descends through the nodal resolution by the following Picard descent argument, which allows a nonflat resolution. The comparison is [Stacks 0E24](https://stacks.math.columbia.edu/tag/0E24). Write the resolution as \(q:Y\to X\). We have \(q_*\mathcal O_Y=\mathcal O_X\). The scheme-theoretic exceptional fibre is a reduced rational chain: in the chart \(xy=\pi^a\), the first nodal blowup principalizes the original ideal \((x,y,\pi)\). Its outer charts have that ideal generated by \(x\) or \(y\), and the central chart by \(\pi\); successive central blowups keep the latter generator. The resolved special fibre is reduced, so the fibre over the original node is exactly its reduced exceptional chain. The normalization sequence gives \(H^1(\mathcal O)=0\), and the degree-zero bundle is fibre-trivial; the other fibres are points. For a local target point with maximal ideal \(\mathfrak m\), each successive ideal quotient \(\mathfrak m^j\mathcal O_Y/\mathfrak m^{j+1}\mathcal O_Y\) is a quotient of a finite sum of copies of the fibre structure sheaf. The quotient has \(H^1=0\): in the cohomology sequence, the finite sum of fibre structure sheaves has \(H^1=0\), and the kernel has \(H^2=0\) because the fibre has dimension at most one. The first-order unit sequence therefore lifts a trivialization through each thickening; the same vanishing makes the units lift, so the trivializations can be chosen compatibly. Formal functions identifies the completion of \(q_*L\) with the completed target ring. Faithfully flat completion makes \(q_*L\) invertible. The completed evaluation \(q^*q_*L\to L\) is the chosen compatible formal trivialization, hence is an isomorphism on the special fibre. The cokernel vanishes near every fibre point by Nakayama; a surjection between these rank-one invertible sheaves is an isomorphism.  Glue back across the persistent nodes. Since their graph is a tree, any fibre identifications can be made and all choices differ by component rescaling; there is no cyclic gluing parameter. This gives the unique \(\ell\)-torsion class on the original compact-type family.

This is the valuative properness test for the separated quasi-finite étale torsion sheaf, so \(\operatorname{Pic}^0[\ell]\) is finite étale on the compact-type open, with rank \(\ell^{2G}\). Its basis torsor is finite étale there. That torsor is normal on a normal atlas and agrees with (S.4) on the dense smooth open; uniqueness of normalization identifies it with the restriction of \(L\). This proves exactly the étaleness needed for the elliptic-tail construction. It does not assert a finite étale cover of the full boundary.

<a id="S6"></a>

## 7. A separable projective scheme cover

The following construction proves the scheme cover and the separability needed here. Its primary comparison is [Stacks 089J](https://stacks.math.columbia.edu/tag/089J).

**Lemma S.6 (separable weak Chow construction).** A proper integral algebraic space \(Z\) over \(k\) admits a projective scheme \(P\) and a proper surjection \(P\to Z\) which is finite étale over a nonempty open after retaining the components dominating \(Z\). In particular such a component induces a finite separable extension of \(k(Z)\).

Here is the full construction needed. Take an affine étale scheme atlas \(W\to Z\). Over a nonempty open \(Z_0\) it is finite étale of degree \(d\). This is also the maximum geometric fibre cardinality: any \(r\) distinct geometric fibre points of an étale map persist, after étale localisation, as \(r\) disjoint sheets over a neighbourhood, and therefore force at least \(r\) geometric generic points of the integral \(Z\). In \(W_Z^d\) take \(V\) of ordered \(d\)-tuples of distinct points. The diagonal is open and closed because \(W\to Z\) is separated étale. Thus \(V\) is a quasi-compact scheme, finite étale over \(Z_0\). Compactify the affine \(W\) inside a projective \(k\)-scheme \(Y\). Let \(B\) be the reduced closure of \(V\) in \(Y^d\), and put \(P=\bigcup_i\operatorname{pr}_i^{-1}(W)\) inside \(B\).

On \(\operatorname{pr}_i^{-1}(W)\) the map to \(Z\) is \(W\to Z\) composed with the projection. These maps agree on their intersections: they agree on the schematically dense \(V\) and \(Z\) is separated. They glue to \(P\to Z\). It is proper by the dense-locus valuative criterion. Given a generic tuple in \(V\) and a valuation lift to \(Z\), an étale atlas point exists after a valuation extension. Its generic point is one of the complete \(d\)-tuple. Properness of the corresponding projective projection \(B\to Y\) supplies the lift to \(B\), which lies in \(\operatorname{pr}_i^{-1}(W)\). This supplies every dense-locus valuation lift. Its proper image contains \(Z_0\) and hence all integral \(Z\).

Over \(Z_0\) each projection lands in \(W_{Z_0}\), which is closed in \(Y\times Z_0\) because it is finite over \(Z_0\). The distinctness condition is open and closed in the resulting finite étale \(d\)-fold fibre product. Density therefore gives \(P_{Z_0}=V\). This checks the generic étale assertion explicitly. Finally \(P\) is quasi-projective over \(k\) and proper over proper \(Z\); it is proper over \(k\). Its open immersion in the projective \(B\) is then also proper, so its image is closed. Thus \(P\) is projective. Retain an integral component dominating \(Z\) and normalize it; its finite separable function-field extension is unchanged.

The resulting projective scheme carries the universal curve after pullback from \(L\).

<a id="S7"></a>

## 8. Normalizing the base and retaining the identifying isomorphism

Pull back (S.5) along \(D_U\). Because \(D_U\) has compact type,
\[
 T=U\times_{X_G}L\longrightarrow U
\tag{S.7}
\]
is finite étale and surjective. It is a scheme, since it is finite over the scheme \(U\). Retain a connected component \(T_0\) dominating \(U\). It is normal integral and its function field \(F/k(S)\) is finite separable.

Normalize \(S\) in \(F\); call this finite projective map \(S_1\to S\). Over \(U\) its corresponding open is \(T_0\), by normality and the finite étale description. The specified object of the fibre product gives an actual morphism \(T_0\to L\), with its identifying isomorphism between \(D_{T_0}\) and the universal family. Take the closure of its graph in the proper algebraic space \(S_1\times L\). Its reduced closure \(Z\) is integral, proper over \(S_1\), and is **isomorphic to \(T_0\)** over that open. Apply Lemma S.6 to \(Z\), retain a dominant integral component, and normalize. The result is an integral projective scheme \(S'\). Its morphism to \(S\) is proper and generically finite, and
\[
 k(S)\subset F=k(S_1)=k(Z)\subset k(S')
\tag{S.8}
\]
is a tower of finite separable extensions. The stable universal curve pulls back to a projective stable family \(D'/S'\). It identifies with \(D_U\) over the inverse image of a smaller dense open in \(U\).

**The normalization before the graph is essential.** For a scheme \(M\) mapping to a stack with automorphisms, \(U\times_{\mathcal X}M\) need not embed in \(S\times M\): changing the isomorphism of the original curve with the universal curve can give several fibre-product points with the same pair of endpoints. Taking its image alone can lose the identifying arrow. Our graph is instead the graph of the actual algebraic-space morphism \(T_0\to L\) on the open \(T_0\) of \(S_1\), so it is an immersion and retains that arrow. No graph-is-a-closed-immersion assertion is made for a morphism to the original stack.

<a id="S9"></a>

## 9. The stable pointed-family extension theorem

**Theorem S.9.** Let \(k\) be algebraically closed, \(S\) an integral projective \(k\)-scheme, and \(U\) a dense open. Let \((C_U\to U;s_1,\ldots,s_n)\) be a smooth proper geometrically connected genus-\(g\) family with ordered disjoint sections, where \(g\ge0\) and \(n\ge3\). There exist a normal integral projective \(k\)-scheme \(S'\), a proper dominant generically finite morphism \(S'\to S\) with finite separable function-field extension \(k(S')/k(S)\), a smaller nonempty dense open \(U_0\subset U\), and a projective stable ordered \(n\)-pointed family \((C'\to S';s_1',\ldots,s_n')\). Over \(S'\times_S U_0\) there is an isomorphism of ordered pointed families between its restriction and the pullback of the original \((C_U;s_1,\ldots,s_n)\). The isomorphism is the retained labelled identifying arrow of the construction.

The proof is S.1–S.8. The only finite extensions of the base function field occur in (S.7) and in the generic étale Chow cover. Both are separable; all normalization and graph modifications are birational. Stabilizer rigidity requires an invertible level \(N\ge3\) and includes positive characteristic. Genus zero and genus one require no separate compactified moduli theorem, since the elliptic-tail reduction uses genus \(G=g+n\ge3\). The universal family is the actual stable family over \(\mathcal X_G\) pulled back along \(L\), then along the graph cover; it is not a family postulated on a coarse space.

Theorem S.9 supplies exactly the family-extension input used in [Smooth projective alterations, §5](../../AG-LTF--smooth-projective-alterations.html). The later graph-extension and normal-crossing arguments require the stable pointed family and projective separable base alteration, exactly as obtained here. They do not require \(L\) to be projective, a finite projective cover of the entire pointed moduli stack, or a characteristic-zero GIT theorem.
