# Stable pointed-family extension after a separable projective alteration

Independent teaching exposition, CC0 1.0. This proves the family-extension consequence used by the alteration argument. The stronger assertion of an everywhere finite projective fine pointed-moduli cover is not claimed. Two bounded internal mathematical reviews and the writing owner’s integration check are complete; their source scopes and retained foundations are recorded in the accompanying proof record.

The full editable licensed proof corpus is included in [the native source index](native-proof-index.md). Its human Stacks authorship, AI Integrated Stacks provenance and GFDL terms remain distinct from this exposition. The [regular surface-model argument](regular-surface-models.md) supplies the complete bounded surface input. The manifest identifies source versions and authorship.

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

Proof sources: [stabilization, uniqueness and tricanonical frames](owned/AG-AS/stable-reduction-and-properness.md#2-stabilization-over-an-arbitrary-base); [nodal deformations and smoothing](owned/AG-AS/the-stack-of-curves.md#4-nodal-curves-and-smoothness-over-the-integers); [quotients and trivial inertia](owned/AG-AS/algebraic-stacks.md#2-algebraic-stacks-and-trivial-inertia); [the étale-atlas criterion](owned/AG-AS/quotient-and-dm-stacks.md#2-cutting-an-étale-atlas); [the fixed-polynomial Hilbert proof](owned/AG-HP/hilbert-and-quot-schemes.md#4-the-flattening-stratum-is-the-quot-scheme).

For \(G\ge2\) the current AG-AS lessons contain the following genuine arguments:

- *Stable reduction and properness*, Lemma 5.1 and Proposition 5.2: \(\omega^3\) is very ample, \(H^1(\omega^3)=0\), \(h^0=5G-5\), and framed tricanonical families form a finite-type Hilbert/Isom scheme \(Q\).
- The same lesson, Theorem 2.3 and Theorem 3.2: relative stabilization and marked stable-model uniqueness.
- *The stack of curves*, Sections 4 and 6.4: the nodal cotangent-complex calculation, independent local smoothing parameters, unobstructedness, and density of smooth curves. These calculations are statements about the actual projective families and remain usable after the quotient presentation constructed here.
- *Algebraic stacks*, Proposition 5.1 and Theorem 2.3: algebraicity of a quotient by a smooth group and the trivial-inertia criterion.
- *Quotient and DM stacks*, Theorem 2.2: the unramified-diagonal criterion for an étale atlas.

The full curve-stack algebraicity theorem stated in the earlier AG-AS lesson is unnecessary here. Indeed \(Q\) is constructed directly from the fixed-polynomial Hilbert scheme, the stable open, a sheaf isomorphism \(\mathcal O_C(1)\simeq\omega_C^3\), and the open determinant condition specifying a frame. For an abstract stable family, its fibre product with \(Q\) is exactly the frame torsor of \(f_*\omega^3\), including the scalar in the sheaf isomorphism. Consequently
\[
 \mathcal X_G=[Q/\operatorname{GL}_{5G-5}]
\tag{S.2}
\]
is the stable-curve stack on every test scheme. This proves its algebraicity and finite type directly. Isomorphisms are represented by the Hilbert graph construction. Infinitesimal automorphisms vanish: on the normalization a vector field must vanish at every node branch; its line-bundle degree is negative on a positive-genus component or it has at least three zeros on a rational component. Thus the diagonal is unramified and the owned criterion makes \(\mathcal X_G\) Deligne–Mumford. The nodal deformation calculation makes it smooth over \(k\), hence normal on an étale atlas.

Theorem 3.2 supplies the diagonal's valuation lifts for **smooth generic curves**, with their specified generic isomorphisms. First use the [exact native separatedness criterion](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/stacks-more-morphisms.tex#L2755) with that dense smooth open; its proof checks the diagonal and then its diagonal. Only then apply the [properness criterion (Stacks 0CQM)](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/stacks-more-morphisms.tex#L2691), which already assumes separation, with the same dense open. This gives properness of \(\mathcal X_G\) from the **proved semistable-model input in S.3**, followed by the owned relative stabilization. The labels are `stacks-more-morphisms-lemma-refined-valuative-criterion-separated` (0E95) and `stacks-more-morphisms-lemma-refined-valuative-criterion-proper`. This uses both complete criterion proofs and their ordinary stack-geometric dependencies, rather than assuming the properness of stable moduli or using Theorem 3.2 outside its smooth-generic scope.

The universal curve is the family encoded by this stack and its quotient presentation. Its tricanonical embedding over each frame torsor descends to a projective curve over the stack. Pullback to a scheme is therefore projective, not merely proper.

<a id="S3"></a>

## 3. Semistable models over the traits needed for properness

Exact native existence and numerical proofs: [models.tex, line 6292](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/models.tex#L6292) · [editable local source](native/models.tex). [Complete numerical completion NS.11a](#numerical-completion) is reproduced below, with its existing AG-GS authorship. [Torsion visibility and the reduced-curve bound](native/curves.tex) and [the regular surface-model bridge](regular-surface-models.md) complete the inputs.

The current AG-AS Theorem 4.1 is explicitly **stated**, and is not the existence proof. The smaller actual proof is the native `models.tex`, Section 17 and Theorem `models-theorem-semistable-reduction` (0CDN), with its numerical, model and Picard proofs. The existing independently authored AG-GS addition NS.11a fills the two weighted-chain and long-fork cases left to the reader in `models-lemma-bound-wm` (0C9W). Its bounded completion is needed if the full numerical bound is used.

Here is the proof mechanism, with the claimed scope kept exact. For a smooth curve of genus \(G\ge2\) over the fraction field of a trait, choose a prime \(\ell>768G\) distinct from the residue characteristic. The smooth-curve Picard variety and the actual owned abelian multiplication/torsion theorem show that all \(\ell\)-torsion and a rational point become visible after one finite **separable** extension. The native visibility proof is `curves-lemma-torsion-picard-becomes-visible` (0CDU). The finite extension can be chosen once for all valuations over the original trait.

Take a minimal regular proper model \(X\). Write its numerical type as \(T\) and its graph genus as \(b\). The native matrix/weighted-graph proof, with NS.11a's omitted cases supplied and the [explicit numerical-source corrections](native-patches/models-corrections.md) applied in the separate annotated teaching version, gives
\[
 \dim_{\mathbf F_l}\operatorname{Pic}(T)[l]\le b.
\]
The exact vertical-divisor torsion sequence and the specialization injection (`models-lemma-sequence-torsion`, 0CAD; `models-lemma-torsion-embeds`, 0CAE) inject at least \(2G-b\) independent torsion classes into Pic of the reduced special curve. Put \(h=h^1(X_{k,\mathrm{red}},\mathcal O)\) and let \(a\) be the sum of geometric normalization genera. The independently checked normalization/gluing bound and the numerical genus inequalities give
\[
 2G-b\le h+a,\qquad G\ge h\ge b+a.
\tag{S.3}
\]
Writing \(u=G-h\) and \(v=h-b-a\) makes the first inequality \(2u+v\le0\). Both \(u\) and \(v\) are nonnegative, so all inequalities are equalities. Strictness for a nonreduced minimal fibre forces every multiplicity to be one. The equality calculation makes each component smooth over its constant field, with the qualification in the next paragraph. Equality in the reduced-curve torsion bound excludes tangent-squishing and permits only multicross singularities. The special curve is Gorenstein, being a Cartier divisor on a regular surface. For an \(r\)-branch multicross, quotienting \(k[[x_1,\ldots,x_r]]/(x_ix_j:i\ne j)\) by \(x_1+\cdots+x_r\) gives a square-zero maximal ideal of dimension \(r-1\). Its socle has that dimension. Gorenstein makes the socle dimension one, so every singular multicross has \(r=2\) and is a node. This is a regular nodal model. Stabilization gives a stable model.

**Scope restriction S.3a (inseparable constant fields).** The printed/native proof of `models-lemma-equality-genus-reduction-bigger-than` (0CEE) infers separability of \(\kappa_i/k\) from equality \(w_ig_i=[\kappa_i:k]_{\mathrm s}g_i\). This inference is valid when \(g_i>0\), but not when \(g_i=0\). The unrestricted nonminimal equality lemma is not certified here. A proposed repair by removing a rational rooted-tree leaf would require an extra proof that the component in question is such a leaf; an arbitrary component can be an articulation vertex. We do not use that repair.

For the properness assertion actually needed here, it suffices to test after a trait extension with algebraically closed residue field. First complete the equicharacteristic DVR. Since \(k\) is perfect, choose a coefficient field containing \(k\); extend that coefficient field to an algebraic closure and keep the same uniformizer. This gives a dominating DVR and an extension of the original fraction field. The stack valuative criterion permits this valuation extension. Every \(\kappa_i\) is now the residue field itself, so \(w_i=1\), and the equality proof has no inseparable-constant inference. Apply the numerical and torsion proof above over that trait and then its finite extension. These trait extensions do not determine the final alteration's function field: that is obtained separately from finite étale level covers and the separable Chow construction in S.7. No arbitrary-residue-field stable-reduction theorem is asserted by this restricted argument.
The numerical classification, regular/minimal-model existence and surface-resolution proofs remain their exact earlier licensed native providers. They are not replaced by an assertion about Jacobians, by stable-moduli properness, or by a blanket citation to a bibliography. The intended integrated provider consists of those complete proof bodies, NS.11a's completion and the algebraically closed residue-field restriction, with their source terms retained.

**Surface-model bridge S.3b.** The required actual `resolve.tex` is at the admitted interlanguage native path, not the inspected AG-AS source directory. Its complete proof of `resolve-theorem-resolve` (0BGP), the completed local induction `resolve-lemma-resolve-complete` (0BGN), the rational-singularity and rational-double-point proofs, the completion/gluing proofs and the complete contraction argument through `resolve-lemma-contract-ample` (0C2M) have been read. Their exact source binding and the small proof details extracted for the model application are in [Regular surface models](regular-surface-models.md). Start with the projective closure of the smooth generic curve. Since our trait is excellent, its finite normalization satisfies condition(4) of0BGP. The proof gives a finite sequence of normalized point blowups; these are projective because normalization is finite. The resulting regular surface is therefore already projective over the trait. Contract its exceptional curves of the first kind using0C2M; each contraction preserves projectivity and regularity and decreases the finite special-fibre component count. This yields the minimal regular proper model used above, without an unproved general assertion that every regular surface is projective.

<a id="S4"></a>

## 4. Automorphisms are detected by invertible level structures

Human primary comparisons: [Pierre Deligne and David Mumford, Theorem (1.13), printed pp.85–87](https://people.mpim-bonn.mpg.de/gaitsgde/grad_2009/Deligne-Mumford.pdf); [Pierre Deligne, Le lemme de Gabber, §§3.3–3.5](https://www.numdam.org/item/AST_1985__127__131_0/). [Owned abelian multiplication and Tate-module proofs](owned/AG-GS/abelian-varieties.md#6-the-degree-and-étaleness-of-multiplication) supply the precise abelian inputs. These links grant source reading; no source PDF is bundled.

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

Exact owned Stein inputs: [complete-local cover lifting](owned/AG-DFG/proper-fundamental-groups.md#2-covers-over-a-complete-local-base) and [the finite étale Stein part](owned/AG-DFG/proper-fundamental-groups.md#5-the-finite-étale-part-of-stein-factorization).

We first prove a lemma for any projective flat nodal family \(D'/S'\) over a normal excellent integral base, with generically distinct labelled rational persistent nodes and split generic branches. No level space or alteration conclusion is assumed. Later we apply this lemma to the stable family constructed in Section 8; its persistent-node and Stein parts are already available for the compact-type trait calculation in Section 6.

The relative nodal locus \(\Sigma\) of \(D'/S'\) is finite and unramified. Locally at a node its presentation is \(xy=a\) and \(\Sigma\) is \(x=y=0\), namely \(\operatorname{Spec}(A/(a))\); properness and quasi-finiteness make it finite globally. The \(n\) attaching nodes in the generic \(D'\) are rational labelled nodes. Each reduced closure in \(\Sigma\) is finite birational over the normal integral \(S'\), hence is a copy of \(S'\). They give \(n\) node sections. Distinct sections never collide: the diagonal of a separated unramified map is open and closed, so their equality locus is open and closed, and it misses the generic point.

The two branches at a persistent node form a finite étale double cover of \(S'\). Its generic branch labels, inherited from core and tail, split it; normality extends that splitting to all \(S'\). A persistent node section forces the local smoothing parameter a to vanish on all \(S'\). Normalize partially at these \(n\) disjoint split nodes. Locally this is the finite map
\[
 A[x,y]/(xy)\longrightarrow A[x]\oplus A[y].
\tag{S.9}
\]
The local constructions glue because the branches are labelled. The resulting family \(D^\dagger/S'\) is projective, flat and finitely presented; both branches in (S.9) are flat, and elsewhere it is the original nodal family. Its geometric fibres are reduced nodal curves. The preimages of the chosen nodes are disjoint smooth sections.

Use the genuine finite-étale Stein proof for this **already flat, geometrically reduced** family. The owned AG-DFG *Proper fundamental groups*, Theorem 5.1, gives \(f_*\mathcal O\) finite étale with geometrically connected fibres of the evaluation map. In the present excellent Noetherian scope its idempotent-lifting step can be confined to the genuinely proved complete-local Theorem 2.1: pass to the completed strict local ring, lift the special-fibre idempotents there, and use the displayed finite-free cohomology-complex splitting and faithful flat descent. This avoids treating the separately stated arbitrary henselian equivalence as an owned proof.

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

Picard representation: [the flat coherent-sheaf proof](owned/AG-AS/moduli-stacks-are-algebraic.md#5-1-flat-ambient-morphisms-a-perfect-complex-of-low-ext-groups) and [Picard rigidification](owned/AG-AS/moduli-stacks-are-algebraic.md#7-picard-stacks-and-picard-spaces). Native comparison: [quot.tex, line 3241](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/quot.tex#L3241) · [editable local source](native/quot.tex).

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

We need the exact specialization argument killing inertia. For a projective flat nodal family with geometrically connected fibres, the universal-functions identity \(f_*\mathcal O=\mathcal O\) holds after every base change. The owned AG-AS *Moduli stacks are algebraic*, Theorems 7.2–7.3, therefore represents the relative Picard functor, using its genuine flat coherent-sheaf proof Theorem 5.2 and rigidification argument. The native comparison is `quot-proposition-pic-functor` (0D2C), whose proof was also read. Its deformation obstruction is \(H^2(\mathcal O)\), which vanishes for curves, so it is smooth. Since \(\ell\) is invertible, its \(\ell\)-torsion is an étale algebraic-space sheaf, locally of finite presentation and initially only locally quasi-finite. Quasi-compactness is established below after the level space is an algebraic space.

On every trait used below, first pass faithfully flat and étale locally so that the relevant branches split and the smooth locus of the closed fibre has a rational point. A smooth point lifts over the henselian trait; its finite-presentation section descends from the strict henselization to an étale neighbourhood. Finitely many components can be treated after one common extension. The section and the owned rigidification proof represent the Picard class by a normalized line bundle. A torsion class becomes an actual torsion bundle, since the Picard group of a trait is zero. The subsequent arguments concern that representative. Their uniquely extended Picard class descends along the faithfully flat cover. This distinction matters: without a section a Picard-sheaf class need not be a line bundle on its given family.

This torsion sheaf is separated. On a trait with smooth generic fibre, resolve \(xy=\pi^a\) by the owned nodal blowups. The resulting regular model has reduced special fibre. An \(\ell\)-torsion line bundle trivial generically is \(\mathcal O(\sum b_iC_i)\). If its \(\ell\)-th power is trivial, a trivializing rational function has no horizontal divisor, hence is in the fraction field of the trait. Its divisor is an integral multiple of the entire reduced fibre. Consequently every \(b_i\) is the same integer, so the bundle is trivial. Pullback along the nodal resolution detects triviality because \(r_*\mathcal O=\mathcal O\). If the generic curve is nodal, first split and partially normalize its persistent nodes. The same argument applies to the smooth generic components. Remaining gluing parameters are units of the trait. A generically trivial gluing cocycle is already trivial over the trait: vertex rescalings over the fraction field have equal valuations along each unit edge, and subtracting the common valuation makes them all units. Faithful étale descent handles nonsplit branches. This proves the separation test for the whole \(\ell\)-torsion sheaf.

On a normal atlas of \(L\), write \(j:V\to T\) for the dense inverse image of \(\mathcal X_G^{\mathrm{sm}}\). Separation gives an injection \(\operatorname{Pic}[\ell]\to j_*\operatorname{Pic}[\ell]|_V\). The generic level identification gives
\[
 \operatorname{Pic}[l]\hookrightarrow j_*(\mathbf Z/l)^{2G}
 =(\mathbf Z/l)^{2G}.
\tag{S.6}
\]
The last equality holds on the étale site of a normal scheme: a connected étale piece is normal integral, and its dense open is connected. The construction is natural under the arrow space. Its two pulled-back constant sheaves have the same frame on the dense smooth open; hence their comparison is the identity everywhere on each normal arrow component. Any stabilizer of a geometric point of \(L\) injects into the stable curve's automorphism group, because (S.5) is representable, and acts trivially on the injection (S.6). Lemma S.5 kills it. This also kills the whole inertia, including tests with nilpotents: stable-curve inertia is finite unramified after properness, so the inertia over a level atlas is finite unramified with every geometric fibre the identity point. Its finite algebra is generated by one modulo every maximal ideal; Nakayama makes the unit surjective locally, and the identity section makes it an isomorphism. The owned trivial-inertia criterion therefore makes \(L\) an **algebraic space**. It is proper over \(k\) because (S.5) is finite and \(\mathcal X_G\) is proper. The universal stable curve pulls back to \(L\).

Before invoking quasi-finiteness or properness of the torsion sheaf, note its quasi-compactness. Pull back to a quasi-compact normal Noetherian étale atlas of \(L\). The separated injection into the finite constant sheaf in (S.6) is an étale monomorphism, hence an open immersion. Every such open in the Noetherian finite constant space is quasi-compact. Quasi-compactness descends to the base of \(L\), and then along the finite surjective map \(L\to\mathcal X_G\). The torsion sheaf is therefore quasi-finite, not merely locally quasi-finite.

The inverse image of the **compact-type** open is finite étale, not only the inverse image of the smooth open. Here is the needed proof, since (S.1) is nodal. On a compact-type geometric fibre, normalization/gluing identifies \(\operatorname{Pic}^0\) with the product of component Jacobians: its dual graph is a tree and the torus is zero. Over a trait in this open, first split the branches. Partially normalize the persistent generic nodes, which are all separating; their sections and branch labels extend on the normal trait by the finite-unramified argument of S.8. The flat partial normalization and finite-étale Stein argument of S.8 then give families with smooth geometrically connected generic fibres. Resolve only their remaining nodes of positive thickness. Each resulting regular special dual graph is a tree. Extend a degree-zero generic line bundle to each regular surface. Its component degrees \(d_i\) have sum zero. The integral graph Laplacian of a tree has image exactly the sum-zero integer lattice: remove a leaf, send its integer degree along its sole edge, and continue. Twisting by the resulting vertical divisor makes every component degree zero. An \(\ell\)-torsion generic bundle thus extends uniquely as \(\ell\)-torsion: its \(\ell\)-th power is a vertical bundle of degree zero, and the connected graph's Laplacian kernel consists of constants, hence it is the whole principal fibre. It descends through the nodal resolution by the full nonflat-safe Picard descent proof [`more-morphisms-lemma-bijection-on-Pic` (0E24)](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/more-morphisms.tex#L22421), also present as [complete editable source](native/more-morphisms.tex). Write the resolution as \(q:Y\to X\). We have \(q_*\mathcal O_Y=\mathcal O_X\). The scheme-theoretic exceptional fibre is a reduced rational chain: in the chart \(xy=\pi^a\), the first nodal blowup principalizes the original ideal \((x,y,\pi)\). Its outer charts have that ideal generated by \(x\) or \(y\), and the central chart by \(\pi\); successive central blowups keep the latter generator. The resolved special fibre is reduced, so the fibre over the original node is exactly its reduced exceptional chain. The normalization sequence gives \(H^1(\mathcal O)=0\), and the degree-zero bundle is fibre-trivial; the other fibres are points. For a local target point with maximal ideal \(\mathfrak m\), each successive ideal quotient \(\mathfrak m^j\mathcal O_Y/\mathfrak m^{j+1}\mathcal O_Y\) is a quotient of a finite sum of copies of the fibre structure sheaf. The quotient has \(H^1=0\): in the cohomology sequence, the finite sum of fibre structure sheaves has \(H^1=0\), and the kernel has \(H^2=0\) because the fibre has dimension at most one. The first-order unit sequence therefore lifts a trivialization through each thickening; the same vanishing makes the units lift, so the trivializations can be chosen compatibly. Formal functions identifies the completion of \(q_*L\) with the completed target ring. Faithfully flat completion makes \(q_*L\) invertible. The completed evaluation \(q^*q_*L\to L\) is the chosen compatible formal trivialization, hence is an isomorphism on the special fibre. The cokernel vanishes near every fibre point by Nakayama; a surjection between these rank-one invertible sheaves is an isomorphism. This supplies the evaluation detail omitted in the native paragraph without assuming flatness of the resolution. Glue back across the persistent nodes. Since their graph is a tree, any fibre identifications can be made and all choices differ by component rescaling; there is no cyclic gluing parameter. This gives the unique \(\ell\)-torsion class on the original compact-type family.

This is the valuative properness test for the separated quasi-finite étale torsion sheaf, so \(\operatorname{Pic}^0[\ell]\) is finite étale on the compact-type open, with rank \(\ell^{2G}\). Its basis torsor is finite étale there. That torsor is normal on a normal atlas and agrees with (S.4) on the dense smooth open; uniqueness of normalization identifies it with the restriction of \(L\). This proves exactly the étaleness needed for the elliptic-tail construction. It does not assert a finite étale cover of the full boundary.

<a id="S6"></a>

## 7. A separable projective scheme cover

Complete weak Chow proof: [spaces-cohomology.tex, line 3273](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/91cc89df5804b8c1949d8267602fc076649ee49b/spaces-cohomology.tex#L3273) · [editable local source](native/spaces-cohomology.tex).

**Lemma S.6 (separable weak Chow construction).** A proper integral algebraic space \(Z\) over \(k\) admits a projective scheme \(P\) and a proper surjection \(P\to Z\) which is finite étale over a nonempty open after retaining the components dominating \(Z\). In particular such a component induces a finite separable extension of \(k(Z)\).

Here is the full construction needed. Take an affine étale scheme atlas \(W\to Z\). Over a nonempty open \(Z_0\) it is finite étale of degree \(d\). This is also the maximum geometric fibre cardinality: any \(r\) distinct geometric fibre points of an étale map persist, after étale localisation, as \(r\) disjoint sheets over a neighbourhood, and therefore force at least \(r\) geometric generic points of the integral \(Z\). In \(W_Z^d\) take \(V\) of ordered \(d\)-tuples of distinct points. The diagonal is open and closed because \(W\to Z\) is separated étale. Thus \(V\) is a quasi-compact scheme, finite étale over \(Z_0\). Compactify the affine \(W\) inside a projective \(k\)-scheme \(Y\). Let \(B\) be the reduced closure of \(V\) in \(Y^d\), and put \(P=\bigcup_i\operatorname{pr}_i^{-1}(W)\) inside \(B\).

On \(\operatorname{pr}_i^{-1}(W)\) the map to \(Z\) is \(W\to Z\) composed with the projection. These maps agree on their intersections: they agree on the schematically dense \(V\) and \(Z\) is separated. They glue to \(P\to Z\). It is proper by the dense-locus valuative criterion. Given a generic tuple in \(V\) and a valuation lift to \(Z\), an étale atlas point exists after a valuation extension. Its generic point is one of the complete \(d\)-tuple. Properness of the corresponding projective projection \(B\to Y\) supplies the lift to \(B\), which lies in \(\operatorname{pr}_i^{-1}(W)\). This supplies every dense-locus valuation lift. Its proper image contains \(Z_0\) and hence all integral \(Z\).

Over \(Z_0\) each projection lands in \(W_{Z_0}\), which is closed in \(Y\times Z_0\) because it is finite over \(Z_0\). The distinctness condition is open and closed in the resulting finite étale \(d\)-fold fibre product. Density therefore gives \(P_{Z_0}=V\). This checks the generic étale assertion explicitly. Finally \(P\) is quasi-projective over \(k\) and proper over proper \(Z\); it is proper over \(k\). Its open immersion in the projective \(B\) is then also proper, so its image is closed. Thus \(P\) is projective. Retain an integral component dominating \(Z\) and normalize it; its finite separable function-field extension is unchanged.

This is the exact proof of Stacks 089J, `spaces-cohomology-lemma-weak-chow`, with the generic étale and projectivity consequences extracted. It supplies a projective cover with the required universal curve **after pullback**. It never claims that \(L\) itself is a projective scheme or that the coarse space has a universal curve.

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

Theorem S.9 supplies exactly the family-extension input used in Smooth projective alterations, §5. The later graph-extension and normal-crossing arguments require the stable pointed family and projective separable base alteration, exactly as obtained here. They do not require \(L\) to be projective, a finite projective cover of the entire pointed moduli stack, or a characteristic-zero GIT theorem.

<a id="S10"></a>

## 10. Foundations, sources and review status

This independent mathematical exposition uses the exact earlier course arguments and the complete openly licensed native proof bodies identified in the source indexes. Original human Stacks expression and cooperating AI integration retain their GFDL notices, distinct from the independent CC0 exposition and existing AG-GS numerical completion.

Pierre Deligne, David Mumford and A. Johan de Jong are named at their actual primary comparison locators. Free reading is not represented as permission to redistribute their PDFs; no source PDF is included.

Theorem S.9 is the proved family-extension consequence in the stated scope. The stronger everywhere finite projective fine pointed-moduli cover remains unclaimed. Bounded internal reviews checked the model and numerical argument, the level construction and the conversion into this teaching text. The accompanying proof record preserves those exact scopes; it does not claim independent human review or a new audit of every transitive foundation.

<a id="numerical-completion"></a>

## 11. Numerical completion of the long weighted chains

The following is the complete NS.11a of the existing independent AG-GS author workflow (recorded writer GPT-6.1 Sol, Ultra), reproduced without mathematical change under CC0 1.0. Its exact original mathematical text is also retained in [the dedicated excerpt](owned/AG-GS/numerical-completion-NS11a.md#ns11a). The human Stacks numerical classification and heart bound remain the separate GFDL source in [models.tex](native/models.tex).

**Numerical completion NS.11a. The long weighted chains in the curve provider.** The native proof of `models-lemma-bound-wm` leaves two weighted-chain cases and the long fork case to the reader. The following supplies those cases, so the required bound is not imported with an unfinished exercise.

Use the native numerical-type notation: \(A=(a_{ij})\) is symmetric, \(Am=0\), \(m_i,w_i>0\), \(w_i\mid a_{ij}\); at a \((-2)\)-vertex, \(a_{ii}=-2w_i\). A one-vertex type has \(A=0\) and torsion-free numerical Picard group, so assume more than one vertex. Let \(J\) be the non-\((-2)\)-vertices. The proved heart bound is \(m_j|a_{jj}|\le6g\) for \(j\in J\). The equation at \(j\) gives, for a neighbour \(i\),
\[
m_i a_{ij}\le m_j|a_{jj}|,
\qquad m_iw_i\le m_j|a_{jj}|.
\tag{NS.11a}
\]
In particular a \((-2)\)-vertex attached to \(J\) has \(m_iw_i\le6g\). Each successive \((-2)\)-edge can at most double the bound on \(m_i|a_{ii}|\). The native proper-subgraph classification says that every remaining short component has graph distance at most seven from \(J\); its small diagrams and the \(E_6,E_7,E_8\) diagrams have diameter at most six. Thus these components satisfy \(m_i|a_{ii}|\le2^7(6g)=768g\). The only components with unbounded length are the following chains and fork. The classification and the heart bound are retained at their exact proved earlier native locators; we now finish their bound.

In an unweighted chain, all \(w_i=w\) and consecutive \(a_{i,i+1}=w\). The multiplicities obey \(2m_i\ge m_{i-1}+m_{i+1}\) at internal vertices, with equality precisely when that vertex has no neighbour in \(J\). A maximum plateau either has an internal boundary with a smaller neighbour, in which case the inequality is strict and that vertex attaches to \(J\), or reaches an endpoint with no smaller internal neighbour. At such an endpoint the residual in \(Am=0\) is \(wm_i>0\), so it also attaches to \(J\). Hence the maximum multiplicity occurs at an attached vertex, giving \(wm_i\le6g\) throughout the chain.

In the first weighted chain, \(w_1=\cdots=w_{t-1}=w\), \(w_t=2w\), ordinary edges have weight \(w\) and the last edge has weight \(2w\). Put \(x_i=m_i\) for \(i<t\) and \(x_t=2m_t\). Then \(w_i m_i=wx_i\), all internal inequalities are \(2x_i\ge x_{i-1}+x_{i+1}\), and the terminal equation gives \(x_t\ge x_{t-1}\), with equality if vertex \(t\) has no neighbour in \(J\). If \(t\) is a maximum and the inequality is strict, it is attached and \(wx_t\le6g\). Otherwise the maximum-plateau argument just given finds an attached maximum at an ordinary vertex or at the other endpoint. Thus again every \(w_i m_i\le6g\).

In the second weighted chain, \(w_1=\cdots=w_{t-1}=2w\), \(w_t=w\), and all edges have weight \(2w\). The original \(m_i\) obey the ordinary internal concavity inequalities, and \(m_t\ge m_{t-1}\), with equality if \(t\) is unattached. The same plateau argument finds a maximum at an attached vertex. If it is an ordinary vertex, \(2w\max m_i\le6g\); if it is \(t\), \(w\max m_i\le6g\). In both cases \(w_i m_i\le12g\) throughout, and so \(m_i|a_{ii}|\le24g\).

For the long fork, all weights are \(w\). Number its long path \(1,\ldots,t-1\), with leaves \(t,t+1\) at vertex \(t-1\). Put \(s=m_t+m_{t+1}\). The path followed by \(s\) satisfies ordinary concavity, because the fork inequality is \(2m_{t-1}\ge m_{t-2}+s\); the two leaf equations give \(s\ge m_{t-1}\). A maximum plateau contained in the path has an attached maximum unless it extends to the terminal \(s\). If \(s\) is a maximum and both leaves are unattached, their equations give \(m_t=m_{t+1}=m_{t-1}/2\), hence \(s=m_{t-1}\). The plateau then either has an attached path boundary or extends to the first endpoint, whose positive residual makes it attached. This gives \(ws\le6g\). If both leaves are attached, (NS.11a) gives \(ws\le12g\). If just one is attached, say \(t\), the other has \(m_{t+1}=m_{t-1}/2\); since \(s\ge m_{t-1}\), we get \(m_t\ge m_{t-1}/2\) and \(s\le2m_t\). Again \(ws\le12g\). A larger path maximum instead has an attached plateau boundary and is bounded by \(6g/w\). Thus every vertex in the fork satisfies \(m_i|a_{ii}|\le24g\). This completes every long case and the bound \(768g\). The off-diagonal bounds follow from (NS.11a), applied with its already bounded neighbouring diagonal. \(\square\)

The precise retained ordinary foundation scopes are recorded in [Foundations and dependency boundaries](FOUNDATIONS.md). Full original chapters are included for source access; this does not certify every transitive theorem or assert a new review of an entire chapter.
