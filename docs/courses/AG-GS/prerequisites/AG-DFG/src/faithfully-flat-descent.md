# Faithfully flat descent

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Public domain (CC0).*

An open cover replaces a scheme by several visible pieces. A faithfully flat cover can instead enlarge its rings, making an object easier to describe without discarding information. The extra information must then be removed by comparing the two enlargements on their fibre product. The cocycle on the triple product is what makes this removal consistent.

We prove the algebraic mechanism first, including how it acts on morphisms. We then use it to descend quasi-coherent sheaves, maps of schemes, and affine schemes. The final examples turn descent into a concrete classification of real forms of the complex projective line.

We assume [Fibred categories and descent data](fibred-categories-and-descent-data.md), flat tensor products and faithful flatness from *Commutative algebra*, and pullback of quasi-coherent sheaves from *Schemes and sheaves*. References are [Stacks] and, for additional exposition, [Vistoli]. A module is not assumed finitely generated unless that condition is stated.

## 1. An enlargement that detects equations

A ring map \(R\to A\) is faithfully flat if tensoring with \(A\) is exact and detects zero modules. In particular a map of \(R\)-modules is an isomorphism if and only if it becomes one after tensoring with \(A\): tensor the kernel and cokernel, and use those two properties.

For an \(R\)-module \(M\), form the augmented Amitsur complex

\[
0\longrightarrow M\longrightarrow M\otimes_RA
\longrightarrow M\otimes_RA\otimes_RA\longrightarrow\cdots.
\tag{1.1}
\]

The term \(C^n\), for \(n\geq0\), is \(M\otimes_RA^{\otimes(n+1)}\). The differential inserts \(1\) in each position with alternating signs:

\[
d^n(m\otimes a_0\otimes\cdots\otimes a_n)
=\sum_{i=0}^{n+1}(-1)^i
m\otimes a_0\otimes\cdots\otimes a_{i-1}
\otimes1\otimes a_i\otimes\cdots\otimes a_n.
\tag{1.2}
\]

The augmentation sends \(m\) to \(m\otimes1\). Every term in \(d^{n+1}d^n\) inserts two units. Inserting the earlier unit first or the later unit first produces the same tensor with opposite signs, proving \(d^2=0\). In degree zero, the kernel consists of sections for which the two pullbacks agree.

The individual unit-insertion maps are the cofaces of a cosimplicial module. Its codegeneracies multiply two adjacent \(A\)-factors. Inserting units commutes in the prescribed order, adjacent multiplication is associative, and multiplying a newly inserted unit removes it. These identities give the cosimplicial equations; (1.2) is their alternating-sum complex. We will only need the explicit formulas above.

**Theorem 1.3.** If \(R\to A\) is faithfully flat, the whole augmented complex (1.1) is exact.

**Proof.** Suppose first that the ring map admits an \(R\)-algebra retraction \(\sigma:A\to R\). Define \(h^n:C^n\to C^{n-1}\), including \(C^{-1}=M\), by applying \(\sigma\) to the first \(A\)-factor:

\[
h^n(m\otimes a_0\otimes\cdots\otimes a_n)
=\sigma(a_0)m\otimes a_1\otimes\cdots\otimes a_n.
\]

In \(h^{n+1}d^n\), the term inserting a unit in the first position is the original tensor. Each other term cancels the corresponding term in \(d^{n-1}h^n\), since its sign changes when its position decreases by one. Thus \(hd+dh=\operatorname{id}\). In augmentation degree, \(h^0d^{-1}=\operatorname{id}_M\). This proves exactness whenever a retraction exists.

For a faithfully flat map, tensor (1.1) with \(A\). The resulting complex is the Amitsur complex for the \(A\)-algebra \(A\otimes_RA\), with coefficient module \(A\otimes_RM\). The map \(A\to A\otimes_RA\), \(a\mapsto a\otimes1\), has the retraction \(a\otimes b\mapsto ab\). Hence the tensorized complex is exact by the preceding contraction. Because \(A\) is flat, its tensor product commutes with the kernels and cokernels that compute cohomology; because it is faithful, vanishing after this tensor product implies vanishing before it. This includes the augmentation degrees and proves the theorem. \(\square\)

Taking \(M=R\), we obtain the ring equalizer

\[
R=\{a\in A:1\otimes a=a\otimes1\text{ in }A\otimes_RA\}.
\tag{1.4}
\]

Thus faithful flatness recovers coefficients, not only the truth of an equation.

## 2. Recovering a module from a cocycle

Let \(N\) be an \(A\)-module. A descent datum is an \(A\otimes_RA\)-linear isomorphism

\[
\phi:N\otimes_RA\xrightarrow{\sim}A\otimes_RN
\]

whose two successive pullbacks agree with its direct pullback on \(A\otimes_RA\otimes_RA\). In the source the first scalar acts on \(N\), and in the target the second scalar acts on \(N\). This convention fixes the direction of every comparison.

Set

\[
\rho(n)=\phi(n\otimes1),\qquad
M=\{n\in N:\rho(n)=1\otimes n\}.
\tag{2.1}
\]

The map \(\rho:N\to A\otimes_RN\) is \(R\)-linear and satisfies

\[
\rho(an)=(a\otimes1)\rho(n).
\tag{2.2}
\]

The diagonal pullback of \(\phi\) is the identity. Indeed the cocycle pulled back to the triple diagonal says that this invertible endomorphism is idempotent. If \(\mu:A\otimes_RN\to N\) is scalar multiplication, diagonal normalization gives

\[
\mu\rho=\operatorname{id}_N.
\tag{2.3}
\]

Evaluate the triple-product cocycle on \(n\otimes1\otimes1\). Writing \(\rho(n)=\sum_i a_i\otimes n_i\), it gives

\[
\sum_i a_i\otimes\rho(n_i)
=\sum_i a_i\otimes1\otimes n_i
\quad\text{in }A\otimes_RA\otimes_RN.
\tag{2.4}
\]

These formulas express the descent datum as a coaction. The word refers here to equations (2.2)–(2.4); no finiteness condition is implicit.

They also construct the cosimplicial module associated with an arbitrary datum. Put \(T^n=A^{\otimes_R n}\otimes_RN\), with \(T^0=N\). Of the \(n+2\) cofaces \(T^n\to T^{n+1}\), the first \(n+1\) insert a unit in the list of \(A\)-factors and the last applies \(\rho\) to \(N\). Of the \(n+1\) codegeneracies \(T^{n+1}\to T^n\), the first \(n\) multiply adjacent \(A\)-factors and the last lets the final scalar act on \(N\). All cosimplicial identities can be checked by the factors they change. For two insertions away from \(N\), the units commute in the required positions; the only two-coface identity involving two coactions is (2.4). For two multiplications the identities are associativity of the algebra and its module action. For a multiplication and insertion, cancellation of a scalar with an inserted unit gives the identity. The final such cancellation is \(\mu\rho=1\); moving a multiplication past the coaction is (2.2). Disjoint operations commute. These cases exhaust the coface, codegeneracy and mixed identities. Compatible maps of descent data commute with every operation, so the construction is functorial.

For the canonical datum on \(N=A\otimes_RM\), moving \(M\) to the first position identifies \(T^n\) with \(M\otimes_RA^{\otimes(n+1)}\). Its coaction moves the last scalar into a new \(A\)-factor and leaves \(1\otimes m\) in \(N\). Thus all its cofaces insert units, its codegeneracies multiply adjacent scalars, and its complex is exactly (1.1). This explains the relationship between [Stacks, Tags [023H](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-lemma-descent-datum-cosimplicial), [023I](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-lemma-canonical-descent-datum-cosimplicial)] and the Amitsur proof.

**Theorem 2.5 (module descent).** For a faithfully flat map \(R\to A\), the natural functor from \(R\)-modules to \(A\)-modules with descent data is an equivalence. Its inverse is the invariant module \(M\) in (2.1).

**Proof.** As an \(R\)-module, \(M\) is the kernel of \(\rho-\eta\), where \(\eta(n)=1\otimes n\). Flatness identifies \(A\otimes_RM\) with

\[
\ker\bigl(\operatorname{id}_A\otimes\rho-
\operatorname{id}_A\otimes\eta:
A\otimes_RN\longrightarrow A\otimes_RA\otimes_RN\bigr).
\]

Equation (2.4) says that \(\rho(n)\) belongs to this kernel. Thus \(\rho\) factors through a map \(\beta:N\to A\otimes_RM\). Let \(\alpha:A\otimes_RM\to N\) send \(a\otimes m\) to \(am\). Equation (2.3) gives \(\alpha\beta=\operatorname{id}\). Equations (2.1) and (2.2) give

\[
\beta\alpha(a\otimes m)=\rho(am)=a\otimes m,
\]

as an equality inside \(A\otimes_RN\); that inclusion is injective by flatness. Hence \(\alpha\) is an isomorphism.

It respects the descent maps: for \(m\in M\),

\[
\phi((am)\otimes b)=a\otimes bm,
\]

which is exactly the canonical comparison for \(A\otimes_RM\). A morphism of descent data \(N\to N'\) commutes with \(\rho\), so restricts to a map \(M\to M'\). The displayed isomorphisms identify the original morphism with the tensor product of that restriction. This proves that the inverse construction works on arrows as well as on objects.

Conversely, for \(N=A\otimes_RM_0\) with the canonical datum, equation (2.1) is the equalizer of the first two arrows in the Amitsur complex for \(M_0\), up to interchanging the tensor factors. Theorem 1.3 identifies that equalizer with \(M_0\). Both constructions therefore have natural inverse isomorphisms. This proves the equivalence in full. \(\square\)

The source statement is [Stacks, Tag 023N](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-proposition-descent-module). The first half of the proof constructs a descended object for any flat ring map. Faithfulness is needed for the full equivalence, including recovery of the original global module. Flatness alone does not make the functor an equivalence. For example, projection \(k\times k\to k\) is flat and forgets every module supported on the second factor. It cannot be faithful.

## 3. Conditions on the descended module

**Proposition 3.1.** For a faithfully flat map \(R\to A\), an \(R\)-module \(M\) is finitely generated, finitely presented, flat, or finite locally free if and only if \(A\otimes_RM\) has the respective property over \(A\).

**Proof.** Ascent of finite generation and finite presentation follows by tensoring a presentation. If \(A\otimes_RM\) has finitely many generators, express them as finite sums of tensors and collect their \(M\)-components. Let \(M_0\) be the submodule generated by those finitely many components. The cokernel of \(M_0\to M\) becomes zero after tensoring with \(A\), so is zero by faithfulness. This proves descent of finite generation.

For finite presentation, first descend finite generation and choose an exact sequence \(0\to K\to R^n\to M\to0\). Flatness of \(A\) identifies its tensor product with the kernel sequence for \(A^n\to A\otimes_RM\). That kernel is finitely generated when the target is finitely presented. Here is why this holds for any finite free surjection: compare it with a finite presentation using their pullback over the target. Both projections from the pullback split because the free modules are projective. Consequently the two kernels, after adding the opposite finite free module, are isomorphic. The kernel of a finite presentation is finitely generated, so the other kernel is a direct summand of a finitely generated module. It is finitely generated too. Apply finite-generation descent to \(K\), obtaining a finite presentation of \(M\).

For flatness, tensor an injection \(P\to Q\) of \(R\)-modules with \(M\). After tensoring with \(A\), this is the injection obtained by first forming \(A\otimes_RP\to A\otimes_RQ\) and then tensoring over \(A\) with the flat module \(A\otimes_RM\). Its kernel is therefore zero after faithfully flat tensoring, hence zero. Thus \(M\) is flat. Ascent follows from the same tensor identities.

A finite locally free module is finitely presented and flat; conversely every finitely presented flat module is finite locally free. To recall the local argument, over a local ring choose generators lifting a basis of the residue-field fibre. The kernel of the resulting finite free surjection is finitely generated. Flatness makes its residue-field fibre inject into that of the free module, and the chosen basis makes this injection zero. Nakayama's lemma gives zero kernel. Finite presentation extends this isomorphism to a neighbourhood of the prime. This proves the characterization, so the first three cases imply the fourth. Ranks are read on residue-field fibres, and hence are preserved after field extension at a point lying above the given prime. \(\square\)

We use finite local freeness here. Local freeness with arbitrary rank does not in general descend for fpqc coverings; [Stacks, Tag 05VF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-remark-locally-free-descends) records the distinction. Applied on affine opens, the proposition descends the four stated conditions for quasi-coherent sheaves.

## 4. Which families are faithfully flat covers?

An **fpqc covering** of \(S\) is a family \(\{U_i\to S\}\) of flat morphisms with the following finiteness condition: for every affine open \(W\subseteq S\), finitely many affine open subsets \(V_j\) of the \(U_i\), mapping into \(W\), have images covering \(W\). In particular the family is jointly surjective. This is the convention of [Stacks, Section 022A](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/topologies.html#topologies-section-fpqc).

The finite disjoint union \(V=\coprod_jV_j\) is affine, and \(V\to W\) is a surjective flat morphism of affines. Its ring map is faithfully flat. Such a refinement is called a **standard fpqc cover**. It is the reason an algebraic theorem about one ring map can handle an arbitrary scheme covering.

An **fppf covering** consists of jointly surjective flat morphisms locally of finite presentation. A flat morphism locally of finite presentation is open, as proved in *Flat morphisms*. Its affine open pieces therefore have open images. Quasi-compactness of each affine \(W\) selects finitely many such images, giving the fpqc condition. Open coverings and étale coverings are special cases. A single surjective flat quasi-compact morphism is also fpqc, by taking a finite affine cover of its inverse image of each affine target open.

Fpqc families remain fpqc after base change. Locally on the new base, cover an affine open by finitely many affine opens mapping into affine opens of the old base. Pull back the finite affine refinements there; affine fibre products give finite affine refinements on the new pieces. Their finite union covers the affine open. Flatness is stable under base change. The same finite-refinement procedure proves stability under composition of coverings.

**Example 4.1.** If \(f_1,\ldots,f_r\) generate the unit ideal of \(R\), then

\[
R\longrightarrow\prod_{j=1}^rR_{f_j}
\]

is faithfully flat. A finite product of flat modules is flat, and the principal opens \(D(f_j)\) cover \(\operatorname{Spec}R\). Equivalently, if a module vanishes after localization at all the \(f_j\), each element is killed by suitable powers of all of them. Those powers still generate the unit ideal, so that element is zero. Module descent for this map recovers ordinary open gluing.

**Example 4.2.** The map \(\mathbf Z\to\prod_p\mathbf Z_p\), over all primes \(p\), is faithfully flat. The product is torsion-free as a \(\mathbf Z\)-module, so is flat over this principal ideal domain. For every prime \(p\), its reduction modulo \(p\) has the nonzero quotient \(\mathbf F_p\) supplied by the \(p\)-component. A flat algebra with nonzero fibres at every maximal ideal is faithful: if \(M\neq0\), a nonzero cyclic submodule is \(R/I\) for some proper ideal \(I\); choose a maximal ideal containing \(I\), observe \(A/IA\neq0\), and use flatness to preserve the inclusion of that cyclic submodule into \(M\). This proves the claim.

The single affine spectrum of the product is an fpqc cover. The separate family \(\{\operatorname{Spec}\mathbf Z_p\to\operatorname{Spec}\mathbf Z\}_p\) is not fpqc in this convention: finitely many members miss all the other closed primes. Its disjoint-union morphism is likewise surjective and flat but is not an fpqc cover. Spectrum does not turn this infinite product of rings into the disjoint union of their spectra.

## 5. Quasi-coherent descent on arbitrary schemes

**Theorem 5.1.** For an fpqc covering \(\{U_i\to S\}\), restriction gives an equivalence from \(\operatorname{QCoh}(S)\) to quasi-coherent sheaves on the \(U_i\) with descent isomorphisms on double fibre products and the cocycle on triple fibre products.

**Proof.** First suppose \(S\) is affine. Choose a standard fpqc refinement \(V=\coprod_jV_j\to S\). Restrict the given datum to \(V\); quasi-coherent sheaves on the finite disjoint union are modules over its product ring. Theorem 2.5 constructs a quasi-coherent sheaf \(\mathcal M\) on \(S\) whose pullback to \(V\) is this restricted datum.

We must recover the data on every original \(U_i\), including those not used in the refinement. On an affine open \(T\subseteq U_i\), the cover \(T\times_SV\to T\) is a surjective flat morphism of affines. The comparisons in the original datum give an isomorphism between the pullbacks of \(\mathcal M|_T\) and the given sheaf on \(T\). On its double fibre product these isomorphisms commute with the canonical descent structures: this is exactly the original triple-product cocycle, with one coordinate in \(T\) and the other two in \(V\). Full faithfulness of Theorem 2.5 descends the isomorphism to \(T\). Its inverse descends too. Uniqueness makes these local isomorphisms agree on overlaps, by applying the same assertion on affine opens inside an overlap. They therefore glue to the required isomorphism on \(U_i\). The same uniqueness shows that the identifications recover every original transition map.

For general \(S\), cover it by affine opens \(S_a\). The preceding argument constructs \(\mathcal M_a\) on each one. On an affine open inside \(S_a\cap S_b\), compare the constructions after the common fpqc refinement obtained by taking the fibre product of their standard refinements. The original datum identifies their pullbacks. Module full faithfulness descends a unique comparison \(\mathcal M_a\simeq\mathcal M_b\) there. Uniqueness makes the comparisons agree on further overlaps and satisfy the triple equation. Zariski descent from the preceding lesson glues them to \(\mathcal M\) on \(S\). Their local identifications with the sheaves on every \(U_i\) glue in the same way.

Finally, compatible morphisms of the original data restrict to morphisms on each standard affine refinement. Module full faithfulness gives unique maps of the \(\mathcal M_a\); uniqueness on overlaps glues them to one map on \(S\). A global morphism is recovered by this procedure, and a morphism whose restrictions vanish vanishes on every affine base piece by faithful module descent. This proves full faithfulness as well as effectivity. \(\square\)

The theorem has no quasi-compactness or separation hypothesis on \(S\), and no finite-generation hypothesis on the sheaves. Its source counterpart is [Stacks, Tag 023T](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-proposition-fpqc-descent-quasi-coherent). The comparisons on a nonaffine intersection were made on its affine open cover; assuming all intersections affine would unnecessarily restrict the theorem.

## 6. Descent of maps and the quotient topology

To descend a map into an arbitrary scheme, coefficients alone are insufficient. We must also descend the inverse images of its affine open subsets.

**Lemma 6.1.** A surjective flat map of affine schemes is a quotient map on underlying topological spaces, and remains one after arbitrary base change.

**Proof.** Write \(q:\operatorname{Spec}A\to\operatorname{Spec}R\). Suppose \(q^{-1}(W)\) is open, and let \(C=\operatorname{Spec}R\setminus W\). We show \(C\) is closed.

Give each spectrum its constructible topology, in which both \(D(f)\) and \(V(f)\) are open and closed. This topology is compact: an ultrafilter on its basic clopen subsets determines the prime ideal of all \(f\) for which \(V(f)\) belongs to the ultrafilter. The identities \(V(fg)=V(f)\cup V(g)\) and \(V(f)\cap V(g)\subseteq V(f+g)\), together with \(V(1)=\varnothing\), prove that this is a prime ideal. Membership of every basic clopen set then shows convergence to that prime. It is Hausdorff because distinct primes are separated by some \(D(f)\) and \(V(f)\). A ring-induced map is continuous for this topology.

The Zariski-closed subset \(q^{-1}(C)\) is closed in the constructible topology, so compact. Its image \(C\) is compact there, and hence closed there. Also \(C\) is stable under specialization. If \(\mathfrak p\subseteq\mathfrak p'\) and \(\mathfrak p\in C\), choose \(\mathfrak q'\) over \(\mathfrak p'\). Flatness gives a prime \(\mathfrak q\subseteq\mathfrak q'\) over \(\mathfrak p\). To justify this last assertion, the localized map \(R_{\mathfrak p'}\to A_{\mathfrak q'}\) is flat and local, hence faithfully flat by the cyclic-module criterion in Example 4.2. Its fibre at \(\mathfrak p\) is nonzero and has a prime, providing \(\mathfrak q\). Since \(q^{-1}(C)\) is Zariski closed and contains \(\mathfrak q\), it contains \(\mathfrak q'\); hence \(\mathfrak p'\in C\).

A constructibly compact specialization-stable subset \(C\) is Zariski closed. Indeed if \(\mathfrak p\notin C\) and every basic neighbourhood \(D(f)\), \(f\notin\mathfrak p\), met \(C\), compactness would give a point \(\mathfrak r\in C\) lying in all of those \(D(f)\). Then \(\mathfrak r\subseteq\mathfrak p\), and specialization stability would put \(\mathfrak p\) in \(C\), a contradiction. Some basic neighbourhood therefore avoids \(C\). Thus \(W\) is open, proving the quotient property.

After base change to an affine open of any new base, the map is again a surjective flat map of affines. The same proof applies, and quotient properties glue over those open base pieces. \(\square\)

**Theorem 6.2.** Every fpqc covering is a universal effective epimorphism in the category of schemes. Equivalently, for every scheme \(X\), the functor \(T\mapsto\operatorname{Hom}(T,X)\) satisfies fpqc gluing.

**Proof.** First let \(q:\operatorname{Spec}A\to\operatorname{Spec}R\) be surjective flat, and suppose \(u:\operatorname{Spec}A\to X\) has equal pullbacks along the two projections. Two points of \(\operatorname{Spec}A\) over the same base point occur as the projections of a point of their fibre product: their residue fields have a nonzero tensor product over the common residue field, and a prime of that tensor product provides the point. The equality of pullbacks makes \(u\) constant on every fibre. It therefore defines a set map \(g:\operatorname{Spec}R\to X\). Lemma 6.1 makes \(g\) continuous.

For a point \(y\), choose an affine open \(\operatorname{Spec}B\subseteq X\) around \(g(y)\), and choose a principal open \(D(r)\) about \(y\) contained in its inverse image. The restriction of \(u\) gives a ring map \(B\to A_r\). Its two pullbacks to \(A_r\otimes_{R_r}A_r\) coincide. The equalizer (1.4) factors it uniquely through \(B\to R_r\), giving a morphism \(D(r)\to X\).

These morphisms agree on overlaps. They have the same point map, and near each point both land in a common affine open of \(X\). Their coefficient maps become equal after the faithfully flat affine cover; the injection of the base ring into its faithfully flat algebra makes them equal before the cover. They glue to a unique morphism \(g\). The same argument proves that two morphisms equal after this cover are equal.

For an arbitrary fpqc family, choose the standard affine refinements of Section 4 on affine base opens. The preceding proof constructs a morphism on each base open. Its pullback agrees with each original \(u_i\): pull back the standard refinement to an affine open of \(U_i\), use the given double-product equality, and apply the uniqueness just proved. The local morphisms agree on affine opens of intersections by the same uniqueness and hence glue. Fpqc families remain fpqc under base change, so the result is universal. \(\square\)

This proves [Stacks, Tag 023Q](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-lemma-fpqc-universal-effective-epimorphisms) directly. In a relative category over a fixed base, the descended map still respects that base: its two possible composites to the base agree after the cover and hence agree by uniqueness. In particular compatible morphisms between already descended schemes descend, even when effectivity of an arbitrary scheme-valued object datum is unavailable.

**Proposition 6.3.** Every surjective flat morphism is an epimorphism of schemes. Consequently base change along a surjective flat morphism is faithful, even without the fpqc finiteness condition.

**Proof.** Suppose \(q:T\to S\) is surjective flat and \(a,b:S\to X\) satisfy \(aq=bq\). Surjectivity makes their point maps equal. For each \(s\in S\), choose \(t\) over it. The maps from \(\mathcal O_{X,a(s)}\) to \(\mathcal O_{S,s}\) become equal in \(\mathcal O_{T,t}\). The latter local extension is faithfully flat, hence injective by (1.1). Their stalk maps were therefore equal. Equality of the point maps and all stalk maps gives \(a=b\). For the base-change assertion, two arrows over \(S\) that become equal over \(T\) agree after the surjective flat projection from the base change of their source. Apply the epimorphism assertion to that projection. \(\square\)

**Proposition 6.4.** Refining an fpqc cover by another fpqc cover gives a fully faithful functor on scheme-valued descent data.

**Proof.** Write the original cover as \(\{V_j\to S\}\) and the refinement as \(\{U_i\to S\}\), with maps \(U_i\to V_{a(i)}\). Let \((Y_j,\theta^Y)\) and \((Z_j,\theta^Z)\) be original data, and suppose \(\alpha_i\) is a compatible family of maps between their refinements. For each \(j\), transport \(\alpha_i\) from the \(a(i)\)-coordinate to the \(j\)-coordinate on \(U_i\times_SV_j\), using

\[
\theta^Z_{a(i),j}\,\alpha_i\,(\theta^Y_{a(i),j})^{-1}.
\]

On \(U_i\times_SU_k\times_SV_j\), the two transported maps agree: substitute the compatibility of \(\alpha_i,\alpha_k\) and the two triple cocycles. The family \(\{U_i\times_SV_j\to V_j\}\) is fpqc. Its further base change to \(Y_j\) is therefore fpqc too. Theorem 6.2 descends the transported maps to a unique map \(\alpha_j:Y_j\to Z_j\). Its composite to \(V_j\) is the prescribed structure map, by the same uniqueness, so it is a map over \(V_j\).

On \(V_j\times_SV_l\), compatibility of \(\alpha_j,\alpha_l\) with the original transition maps can be checked after the fpqc base change from the \(U_i\). There it is the transport formula and the cocycle, so Theorem 6.2 proves compatibility before the cover. On \(U_i\), the map \(\alpha_{a(i)}\) recovers \(\alpha_i\); use the same formula and the identity of diagonal transition maps. This gives fullness. Two maps equal after refinement have equal transported maps on every \(V_j\), so uniqueness gives equality; this is faithfulness. \(\square\)

The two propositions supply [Stacks, Tags [02VW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-lemma-surjective-flat-epi), [02VX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-lemma-ff-base-change-faithful), [0241](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-lemma-fully-faithful), [02W0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-lemma-refine-coverings-fully-faithful), [040L](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-remark-morphisms-of-schemes-satisfy-fpqc-descent)]. In particular, for schemes \(Y,Z\) over \(S\), compatible arrows \(Y_{U_i}\to Z_{U_i}\) descend to \(Y\to Z\): apply Theorem 6.2 to the fpqc family \(Y_{U_i}\to Y\), then check the structure map and pullbacks by uniqueness.

## 7. Algebras and affine schemes

The invariant-module construction preserves algebra structures. If \(N\) is an \(A\)-algebra and \(\phi\) is an algebra isomorphism, invariants in (2.1) are closed under multiplication and contain \(1\), giving an \(R\)-algebra \(M\). The isomorphism \(A\otimes_RM\simeq N\) is an algebra isomorphism. Compatible algebra maps descend as module maps and remain multiplicative because that equation can be checked after faithful flat tensoring.

For quasi-coherent algebras on a scheme the same argument works on the standard affine refinements. Their multiplication maps glue under Theorem 5.1, or equivalently can be checked on each affine descended algebra. Units glue too. Thus quasi-coherent algebras satisfy effective fpqc descent.

**Theorem 7.1.** Scheme-valued descent data for an fpqc covering are effective if the schemes over the members of the cover are affine over those members. Morphisms of such data descend uniquely.

**Proof.** An affine \(U_i\)-scheme is the relative spectrum of a quasi-coherent \(\mathcal O_{U_i}\)-algebra \(\mathcal B_i\). The scheme isomorphisms on double fibre products give algebra isomorphisms in the opposite direction. Invert those comparisons to put them into the convention of Theorem 5.1. Descend the \(\mathcal B_i\) to an algebra \(\mathcal B\) on \(S\). Relative spectrum commutes with base change, so \(\operatorname{Spec}_S\mathcal B\) gives exactly the original schemes and their transition maps. Maps of affine schemes correspond contravariantly to algebra maps; those maps descend uniquely. This proves the theorem. \(\square\)

**Corollary 7.2.** Closed-immersion descent data are effective, and a given morphism is a closed immersion if its fpqc pullbacks are closed immersions.

**Proof.** Closed immersions are affine, so Theorem 7.1 descends the object data. On affine base pieces their algebra maps \(R\to B\) become surjective after a faithfully flat extension. The cokernel as a module therefore vanishes, making \(R\to B\) surjective. Equivalently descend their ideals by module descent and take the quotient algebra. For a given morphism, first compare it with the affine object obtained from its pullback datum. Its canonical comparison is an isomorphism after the cover, and the inverse descends by Theorem 6.2. Thus the given morphism is the descended affine morphism, and the same surjectivity argument applies. \(\square\)

These results are [Stacks, Tags [0245](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-lemma-affine), [03I0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-lemma-closed-immersion)]. General scheme-valued descent requires additional hypotheses; this affine argument does not establish effectivity for every scheme. A useful further theorem is that a quasi-projective scheme descends along a surjective finite locally free morphism [Stacks, Tag 0CCJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/groupoids.html#groupoids-lemma-descend-along-finite-quasi-projective). We use that stated theorem for the real forms below.

**Example 7.3 (an ineffective étale datum).** Glue two copies of \(\mathbf A^1_{\mathbf C}\) by the identity on \(\mathbf G_{m,\mathbf C}\). Call the resulting scheme \(D\), with origins \(o_+\) and \(o_-\). Conjugating the coordinate and exchanging the two copies defines a conjugate-semilinear involution \(\tau\) of \(D\). Its square is the identity. The decomposition of \(\mathbf C\otimes_{\mathbf R}\mathbf C\) into the identity and conjugation components turns \(\tau\) into descent data along the finite étale cover \(\operatorname{Spec}\mathbf C\to\operatorname{Spec}\mathbf R\); on the triple product the cocycle is \(\tau^2=1\).

There is no affine open of \(D\) containing both origins. Indeed suppose such an open \(U\) existed. The point \((o_+,o_-)\) of \(U\times_{\mathbf C}U\) lies in the closure of its diagonal. To check this, pull back a neighbourhood of that point to the product of the two affine-line charts. It contains a basic open \(D(F)\) containing \((0,0)\), so \(F(0,0)\neq0\). The polynomial \(F(t,t)\) is then nonzero at zero and hence at some nonzero complex number sufficiently chosen to lie in both chart neighbourhoods. That pair is a diagonal point of the glued punctured line. But \((o_+,o_-)\) itself is not on the diagonal. Thus the diagonal of \(U\) is not closed, contrary to the closed diagonal of an affine scheme.

If the datum were effective, write \(D\simeq Y_{\mathbf C}\) for a real scheme \(Y\), compatibly with \(\tau\). The two origins would map to the same point of \(Y\), since the projection is invariant under \(\tau\). An affine neighbourhood of that point would pull back to an affine open of \(D\) containing both origins, a contradiction. This is a scheme-valued descent datum that is ineffective even for a finite étale cover. The scheme \(D\) is not quasi-projective: quasi-projective schemes over a field are separated, whereas its doubled origins give the diagonal failure just proved. Algebraic spaces provide a setting in which this datum has an effective quotient.

## 8. Galois descent and two real projective lines

Let \(L/K\) be a finite Galois extension with group \(G\). The isomorphism

\[
L\otimes_KL\xrightarrow{\sim}\prod_{g\in G}L,
\qquad a\otimes b\longmapsto(a\,g(b))_g,
\tag{8.1}
\]

decomposes the double product into the graphs of the automorphisms. The triple product similarly has components indexed by pairs in \(G\). A descent isomorphism on these graphs is exactly a semilinear action on an \(L\)-vector space \(V\): maps \(\tau_g\) satisfying

\[
\tau_g(av)=g(a)\tau_g(v),\qquad
\tau_g\tau_h=\tau_{gh}.
\]

One may index the comparison from the graph of \(g\) by \(g^{-1}\) if its arrow direction is reversed; the semilinear convention above fixes our indexing. The triple cocycle is exactly the group law, and (2.1) is \(V^G\). Theorem 2.5 gives

\[
L\otimes_KV^G\xrightarrow{\sim}V.
\tag{8.2}
\]

For completeness, (8.1) follows by choosing a primitive element of the finite separable extension: its minimal polynomial has distinct roots indexed by the embeddings into \(L\), and the Chinese remainder theorem splits its scalar extension into the displayed factors. Applying this twice gives the triple decomposition.

For a \(K\)-scheme \(X\), the same graph decomposition of \(X_L\times_XX_L\) turns descent data into a compatible semilinear \(G\)-action on a quasi-coherent sheaf on \(X_L\). Explicitly, put \(f_g=\operatorname{id}_X\times\operatorname{Spec}(g)\). The sheaf data can be written as isomorphisms \(\varphi_g:\mathcal F\to f_g^*\mathcal F\) with \(\varphi_{gh}=f_g^*(\varphi_h)\circ\varphi_g\); the equality \(f_{gh}=f_h\circ f_g\) makes the codomain correct. Theorem 5.1 proves the equivalence with \(\operatorname{QCoh}(X)\), without a compactness assumption on \(X\). More generally, for a finite étale \(G\)-torsor \(Y\to X\), the identity \(Y\times_XY\simeq\coprod_{g\in G}Y\) gives the same equivalence between quasi-coherent sheaves on \(X\) and \(G\)-equivariant quasi-coherent sheaves on \(Y\). These are the versions of [Stacks, Tags [0CDR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-lemma-galois-descent), [0D1V](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-lemma-galois-descent-more-general)].

For \(\mathbf C/\mathbf R\), a semilinear action is a conjugate-linear involution \(J\). The vector-space statement is especially transparent:

\[
v=\frac{v+Jv}{2}+i\frac{v-Jv}{2i},
\]

and both displayed real components are fixed by \(J\). Their intersection after multiplication by \(i\) is zero, proving \(V=V^J\oplus iV^J\) as real vector spaces.

**Theorem 8.3.** There are precisely two real forms of \(\mathbf P^1_{\mathbf C}\): \(\mathbf P^1_{\mathbf R}\) and the real conic \(x^2+y^2+z^2=0\).

**Proof.** An isomorphism of the complexification of a real form with \(\mathbf P^1_{\mathbf C}\) gives a conjugate-semilinear projective involution \(\tau\). Conversely such an involution gives a descent datum, effective by the stated quasi-projective descent theorem. Two data give isomorphic real forms exactly when their involutions are conjugate by a complex projective automorphism, by full faithfulness of scheme descent.

Every automorphism of \(\mathbf P^1_{\mathbf C}\) is fractional linear: its rational function has degree one, since degrees of nonconstant maps multiply under composition and it has an inverse. Consequently \(\tau\) lifts to a conjugate-linear map \(J(v)=A\bar v\) on \(\mathbf C^2\), with \(A\) invertible. Its projective square is the identity, so \(A\bar A=\lambda I\). The scalar \(\lambda\) is real: the equation gives \(\bar A A=\lambda I\) by conjugating with \(A\), while complex conjugation gives \(\bar A A=\bar\lambda I\). It is nonzero. Scaling the lift changes \(\lambda\) by a positive factor, so normalize \(J^2=I\) or \(J^2=-I\).

If \(J^2=I\), the preceding real-vector-space decomposition supplies a basis of fixed vectors. In that basis \(J\) is ordinary conjugation, and the descended form is \(\mathbf P^1_{\mathbf R}\).

If \(J^2=-I\), choose a nonzero \(v\). The vectors \(v,Jv\) are independent: \(Jv=cv\) would give \(J^2v=|c|^2v\), contradicting \(-v\). In this basis the projective involution is

\[
[u:v]\longmapsto[-\bar v:\bar u].
\tag{8.4}
\]

It has no fixed projective point, by the same scalar argument. The map

\[
[u:v]\longmapsto[u^2-v^2:i(u^2+v^2):2uv]
\tag{8.5}
\]

is an isomorphism onto the complex conic \(x^2+y^2+z^2=0\). Indeed it is the quadratic Veronese embedding followed by an invertible linear change of its three coordinates, and its coordinates satisfy that equation. Substitution of (8.4) into (8.5) gives the complex conjugate of (8.5), up to multiplication of all coordinates by \(-1\). Thus the map is equivariant for (8.4) and the ordinary real structure of the conic. It identifies their descent data, so this is the second real form.

The two forms are different because the first has real points and the second has none: a sum of three real squares vanishes only when all three coordinates vanish. The two signs exhausted all lifts and each sign gave one conjugacy class, proving completeness. \(\square\)

## 9. Exercises

**Exercise 9.1 (easy).** Verify the contraction in Theorem 1.3 in degrees zero and one, including its signs. Explain why a ring retraction alone proves exactness even if flatness was not assumed.

**Exercise 9.2 (medium).** For a finite Galois extension \(L/K\), show that taking invariants and extending scalars are inverse functors between \(K\)-vector spaces and \(L\)-vector spaces with semilinear \(G\)-action. Include the assertion for equivariant linear maps.

**Exercise 9.3 (medium).** Descend finite generation and flatness along a faithfully flat ring map. Give a flat nonfaithful map showing why one cannot recover these properties merely by looking at an arbitrary flat scalar extension.

**Exercise 9.4 (medium).** Starting from compatible ideal sheaves \(\mathcal I_i\subseteq\mathcal O_{U_i}\) on an fpqc cover, construct the descended closed subscheme. Check its pullbacks as closed subschemes, not just as sets, and use the construction to show that being a closed immersion descends for a given morphism.

**Exercise 9.5 (hard).** Classify the conjugate-semilinear involutions of \(\mathbf P^1_{\mathbf C}\) up to projective conjugacy. Explain why a lift on \(\mathbf C^2\) may square to \(-I\) even though the induced projective map squares to the identity, and exhibit the corresponding real conic.

### Solutions

**9.1.** In degree zero, \(d(m\otimes a)=m\otimes1\otimes a-m\otimes a\otimes1\). Applying \(h\) gives \(m\otimes a-\sigma(a)m\otimes1\); the missing term is exactly the augmentation applied to \(h(m\otimes a)\). In degree one, insert a unit into \(m\otimes a\otimes b\) in the three positions. After \(h\), this gives \(m\otimes a\otimes b-\sigma(a)m\otimes1\otimes b+\sigma(a)m\otimes b\otimes1\). The last two terms cancel \(dh\). The same cancellation works in every degree. A contraction is an actual identity of maps of the original complex, so does not require tensor exactness or flatness.

**9.2.** Use (8.1) to convert the semilinear action into descent data. Theorem 2.5 gives the natural isomorphism (8.2). For a \(K\)-vector space \(W\), invariants in \(L\otimes_KW\) are exactly \(1\otimes W\), either by the Amitsur equalizer or by expanding a vector in a \(K\)-basis of \(W\) and checking that each coefficient is fixed by \(G\). An equivariant \(L\)-linear map preserves invariants. Under (8.2), it is the scalar extension of that restriction; conversely any \(K\)-linear map extends equivariantly. This gives the two functors and both natural inverse isomorphisms.

**9.3.** Collect the finitely many module components occurring in a finite generating set after extension; the quotient by their span has zero scalar extension and hence vanishes. To descend flatness, test an arbitrary injection after tensoring with the module, extend scalars to the faithfully flat algebra, and use flatness there to kill its kernel; faithful flatness then kills the original kernel. For a counterexample take \(R=k\times k[t]\), \(A=k\), and \(M=0\times\bigoplus_{n\geq1}k[t]/(t)\). Projection is flat. The extension of \(M\) is zero, hence finitely generated and flat, while \(M\) is neither finitely generated nor flat over \(R\). The second property fails because multiplication by \(t\) is injective on the second-factor ring but becomes the zero map on its nonzero tensor product with \(M\).

**9.4.** Theorem 5.1 descends the ideal modules and their maps into the structure sheaf. The descended map is injective, since its kernel vanishes after the flat cover. Its image \(\mathcal I\) is an ideal: multiplication by any local section of \(\mathcal O_S\) preserves it after pullback, and equality of the required module maps descends. Form \(\mathcal O_S/\mathcal I\) and its relative spectrum. Flatness identifies its pullback with \(\mathcal O_{U_i}/\mathcal I_i\), preserving the quotient algebra and thus the closed scheme structure. Compatible comparisons and uniqueness of the ideal descent give exactly the original closed-subscheme datum. If a given morphism becomes a closed immersion, compare it with this descended affine object. The local isomorphism and its inverse descend by Theorem 6.2, as in Corollary 7.2, so the given morphism is the resulting closed immersion.

**9.5.** Lift the semilinear projective map to \(J(v)=A\bar v\). The projective involution condition is \(J^2=\lambda I\). The scalar is real and can be normalized to \(+1\) or \(-1\), as in Theorem 8.3. A lift may have negative square because projectivization discards every nonzero scalar, including \(-1\); multiplying a semilinear lift by a scalar changes its square by a positive norm and cannot change that sign. The positive case has a real basis of fixed vectors and descends to \(\mathbf P^1_{\mathbf R}\). In the negative case the basis \(v,Jv\) gives (8.4). Formula (8.5) identifies its descent with \(x^2+y^2+z^2=0\). The existence or absence of a real point distinguishes the two, and the normal forms prove that there are no further cases.

## What this lesson does not prove

We assume the elementary theory of flat modules, localization, Nakayama's lemma, finite Galois extensions and their primitive elements, and the affine correspondence for quasi-coherent sheaves. From *Flat morphisms* we use: a flat morphism locally of finite presentation is universally open [Stacks, Tag 01UA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-fppf-open). From *Schemes and sheaves* we use the construction of relative spectrum, the correspondence between affine morphisms and quasi-coherent algebras, and compatibility of relative spectrum with base change [Stacks, Tags [01LS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/constructions.html#constructions-lemma-spec-base-change), [01LX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/constructions.html#constructions-lemma-spec-properties)]. The further effectivity theorem for quasi-projective schemes along surjective finite locally free morphisms is stated from [Stacks, Tag 0CCJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/groupoids.html#groupoids-lemma-descend-along-finite-quasi-projective); we used it only for the projective-line forms. The failure of arbitrary-rank local freeness to descend is stated from [Stacks, Tag 05VF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-remark-locally-free-descends); the four positive descent assertions in Proposition 3.1 were proved here. General sites, stacks in groupoids, and the general existence of algebraic-space quotients are treated elsewhere.

## References

- **[Stacks]** The Stacks Project, *Descent*, module descent, fpqc descent of quasi-coherent sheaves, morphism descent and affine descent; *Topologies*, fpqc coverings; *Groupoid Schemes*, quasi-projective descent. Read in AI Integrated Stacks Project Stacks. Tags [023M](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-lemma-ff-exact), [023N](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-proposition-descent-module), [023T](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-proposition-fpqc-descent-quasi-coherent), [023Q](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-lemma-fpqc-universal-effective-epimorphisms), and [0245](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-lemma-affine).
- **[Vistoli]** Angelo Vistoli, *Notes on Grothendieck topologies, fibered categories and descent theory*, [arXiv:math/0412512](https://arxiv.org/abs/math/0412512). Further reading on the categorical organization of descent.
