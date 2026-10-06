# ℓ-adic sheaves and their cohomology

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI; independent checking pending. Public domain (CC0).*

A finite coefficient ring remembers only a finite amount of arithmetic. Passing from \(\mathbb Z/\ell^n\mathbb Z\) to \(\mathbb Z_\ell\) keeps all these amounts at once. This passage is useful only if the resulting objects have finite stalks, finite cohomology and well behaved traces. Those are the questions of this lesson.

There are two different inverse limits to keep apart. A stalk is the inverse limit of finite modules. Cohomology is the inverse limit of finite cohomology groups. Neither construction means that one should first take an ordinary inverse limit of sheaves on the étale site and then apply ordinary sheaf cohomology. The pro-étale site gives a setting for that second description; the next lesson develops it.

We use [Constructible sheaves and extension by zero, §§2–7](course:ag-etale-cohomology/constructible-sheaves-and-extension-by-zero) for finite local systems and constructibility, [Cohomology with compact support, §§4–12](course:ag-etale-cohomology/cohomology-with-compact-support) for compact support, and [Cohomological dimension and the Künneth formula, §§7–8](course:ag-etale-cohomology/cohomological-dimension-and-the-kunneth-formula) for ordinary dimension and scalar extension. The finite-étale fundamental-group equivalence and general torsion finiteness are the explicitly stated foundations of those lessons. The needed derived-category language is explained in [Derived categories and sheaf operations](https://kokunoyumeto.github.io/open-math-courses-public/courses/derived-categories-and-sheaf-operations/index.html). We recall the exact torsion statements before using them. Basic references are [Stacks], [Milne, Étale lectures] and [Deligne, Cohomologie étale].

Throughout, \(\ell\) is a prime invertible on the schemes in question. Put \(O=\mathbb Z_\ell\), \(O_n=O/\ell^nO\) and \(E=\mathbb Q_\ell\). The word *finite* for an \(O\)-module means finitely generated, not finite as a set. A constructible \(O_n\)-sheaf has finite stalks as sets.

## 1. What a compatible system remembers

**Definition 1.1.** On a Noetherian scheme \(X\), an *adic sheaf* is a system \(\mathcal F=(\mathcal F_n)_{n\geq1}\) of constructible \(O_n\)-sheaves with transition maps inducing

\[
\mathcal F_{n+1}/\ell^n\mathcal F_{n+1}\simeq\mathcal F_n.
\]

Morphisms are compatible systems of sheaf maps. The sheaf is *lisse* if every \(\mathcal F_n\) is finite locally constant. These are also called strict constructible adic systems. The word strict concerns the displayed reduction condition.

For a geometric point \(\bar x\), define its adic stalk by

\[
\mathcal F_{\bar x}=\varprojlim_n\mathcal F_{n,\bar x}.
\]

The following elementary argument explains both finiteness and the topology on this stalk.

**Lemma 1.2.** Suppose that finite \(O_n\)-modules \(M_n\) satisfy the reduction condition of Definition 1.1. Then \(M=\varprojlim M_n\) is a finite \(O\)-module and the natural maps identify \(M/\ell^nM\) with \(M_n\). Its inverse-limit topology is its \(\ell\)-adic topology.

**Proof.** All transition maps are onto. Consequently \(M\to M_n\) is onto: successive lifts give a compatible sequence. Its kernel contains \(\ell^nM\). Conversely, let \(z\in M\) have zero image in \(M_n\). For every \(m\geq n\), strictness says that \(z_m\in\ell^nM_m\). Consider the finite sets of solutions to \(\ell^ny_m=z_m\). They form an inverse system. Every finite collection of compatibility conditions has a solution, obtained by choosing a solution at the largest index and reducing. Compactness of the product of these finite sets gives a compatible solution \(y\). Thus \(z=\ell^ny\).

Choose lifts \(v_1,\ldots,v_r\in M\) of generators of \(M_1\). The map \(O^r\to M\) they define has dense image. Indeed, after approximating an element modulo \(\ell\), divide its error by \(\ell\) and repeat; the preceding kernel calculation permits each division. Its image is also closed, because \(O^r\) is compact and \(M\) is Hausdorff. The map is therefore onto. Finally, its reduction kernels are \(\ell^nM\), proving the assertion about topology. ∎

In particular, every stalk has the form

\[
O^r\oplus\bigoplus_{a=1}^s O/\ell^{e_a}O.
\]

The stalk can have torsion even when the system has infinitely many levels. The constant sheaf attached to \(O/\ell^3O\), for example, has levels \(O/\ell^{\min(n,3)}O\).

**Proposition 1.3.** If \(X\) is connected and Noetherian, evaluation at \(\bar x\) gives an equivalence between lisse adic sheaves and finite \(O\)-modules with continuous \(\pi_1(X,\bar x)\)-action.

**Proof.** Apply the finite locally constant equivalence to every level. It respects reduction of coefficients. Lemma 1.2 then produces a finite module \(M\). Its action is continuous because the action on every finite quotient \(M/\ell^nM\) is continuous, and these quotients define its topology.

Conversely, a continuous action on \(M\) induces continuous actions on these finite quotients. The finite locally constant equivalence produces sheaves \(\mathcal F_n\), and its compatibility with tensor products gives the required reductions. A map between finite \(O\)-modules is automatically continuous: it carries \(\ell^nM\) into \(\ell^nN\). Such a map is equivariant exactly when all its reductions are equivariant. The finite-level full faithfulness therefore proves full faithfulness for the systems. The two constructions recover each other. ∎

Lisse does not assert that a single finite étale cover trivializes all levels. If the representation has infinite image, different levels require increasingly large finite covers. This distinction is particularly visible for a Tate module.

*References:* [Stacks, Tags 03UM and 0DV5]; [Deligne, Rapport, Proposition 2.4].

## 2. Finitely many strata suffice

Definition 1.1 gives a separate finite stratification at each level. To construct kernels, we need a finite stratification that works for all levels. This is a consequence of Noetherianity, not an additional assumption.

**Lemma 2.1.** A constructible sheaf of finite sets on a Noetherian scheme satisfies the ascending chain condition on subsheaves.

**Proof.** Choose finitely many locally closed strata on which the sheaf is finite locally constant. On each stratum its underlying sheaf is represented by a finite étale scheme \(Y\). A subsheaf is represented there by an open subspace of \(Y\): under the equivalence with étale spaces, a monomorphism into an étale space is an open immersion. An increasing chain of these open subspaces stabilizes because \(Y\) is Noetherian. Take the largest of the finitely many stabilization indices. Equality of restrictions to the strata is equality on every geometric stalk, hence equality of subsheaves on \(X\). ∎

**Proposition 2.2.** An adic sheaf on a Noetherian scheme admits a finite locally closed stratification on which every level is locally constant. Finitely many adic sheaves admit a common such stratification.

**Proof.** Form the graded pieces

\[
G_j=\ell^j\mathcal F_m/\ell^{j+1}\mathcal F_m\qquad(m>j).
\]

Reduction identifies this sheaf independently of \(m\). Lifting a section of \(\mathcal F_1\) and multiplying it by \(\ell^j\) gives a canonical surjection \(\mathcal F_1\to G_j\). Multiplication by \(\ell\) gives surjections \(G_j\to G_{j+1}\); therefore the kernels of \(\mathcal F_1\to G_j\) form an increasing chain. Lemma 2.1 shows that they stabilize, say at \(j=N\).

Stratify the finitely many constructible sheaves \(G_0,\ldots,G_N\) simultaneously. Every later graded piece is isomorphic to \(G_N\), so it is locally constant on these strata too. The finite filtration of \(\mathcal F_m\) by its powers of \(\ell\) has these locally constant graded pieces. Extensions of finite locally constant abelian sheaves are finite locally constant: étale locally, lift the finitely many elements of the quotient and trivialize the kernel; their finitely many addition relations can then be made constant after refining the neighborhood. Thus every \(\mathcal F_m\) is locally constant on the same strata. For finitely many systems, intersect their finite stratifications. ∎

We may refine further so that each stratum is connected. On a stratum, Proposition 1.3 describes the whole system by one finite \(O\)-module. As a result, ranks and torsion exponents have uniform finite bounds across \(X\).

*Reference:* [Deligne, Rapport, Proposition 2.5].

## 3. Kernels must remember later levels

Consider multiplication by \(\ell\) on the constant adic sheaf \(O\). Each map \(O_n\to O_n\) has a nonzero kernel. Nevertheless its adic kernel must be zero, since multiplication by \(\ell\) on \(O\) is injective. The transition maps on those finite-level kernels are zero. Their elements never survive passage to later levels.

We give the kernel construction and verify the categorical assertion it supports.

**Lemma 3.1.** Let \(K\subset M\) be finite \(O\)-modules. There is an integer \(c\geq0\) such that

\[
K\cap\ell^mM\subset\ell^{m-c}K\qquad(m\geq c).
\]

**Proof.** Choose \(c\) annihilating the torsion of \(M/K\). If \(z=\ell^my\in K\), the image of \(y\) in \(M/K\) is killed by \(\ell^m\), hence is torsion. Thus \(\ell^cy\in K\), and \(z=\ell^{m-c}(\ell^cy)\). ∎

This is the particular Artin–Rees estimate needed here. It says that the topology induced on a submodule is equivalent to its own adic topology.

An alternative formalism retains more general projective systems and identifies systems whose later transition maps vanish. Artin–Rees systems then encode the equivalence of filtrations just proved. Jouanolou develops that formalism in [SGA 5, Exposé V, §§3–5]; Exposé VI uses it for constructible adic sheaves and cohomology. We work with strict representatives and perform the needed normalization explicitly.

**Theorem 3.2.** The category of adic sheaves on a Noetherian scheme is abelian. The cokernel of \(u:\mathcal F\to\mathcal G\) is the levelwise cokernel. The kernel is obtained as follows. First put

\[
B_n=\bigcap_{m\geq n}\operatorname{im}\bigl(\ker u_m\longrightarrow\ker u_n\bigr).
\]

For each fixed \(k\), the sheaves \(B_m/\ell^kB_m\) are eventually constant. Their eventual value is the \(k\)-th level of the adic kernel.

**Proof.** We first explain the use of inverse systems in this argument. Regard an inverse system as a pro-object in constructible torsion sheaves. The category of such pro-objects is abelian; for a levelwise map its kernel and cokernel are represented by the levelwise kernels and cokernels. This follows directly from the usual kernel and cokernel universal properties after moving finitely many maps to a common later index. The Hom formula is

\[
\operatorname{Hom}_{\mathrm{pro}}((A_m),(B_n))
=\varprojlim_n\varinjlim_m\operatorname{Hom}(A_m,B_n).
\]

For strict systems the inner limit is already \(\operatorname{Hom}(A_n,B_n)\) once \(m\geq n\): a map to \(B_n\), which is killed by \(\ell^n\), factors uniquely through \(A_m/\ell^nA_m=A_n\). Thus strict systems embed fully faithfully in this abelian category.

Right exactness of reduction proves that the levelwise cokernels form a strict system. They remain constructible. To analyze the kernel, choose a common finite stratification for \(\mathcal F\) and \(\mathcal G\) by Proposition 2.2. On a connected stratum the map corresponds to \(v:M\to N\) between finite \(O\)-modules. Write \(K=\ker v\).

For each \(n\), the intersection of the images of \(\ker(v\bmod\ell^m)\) in \(M/\ell^nM\) is precisely the image of \(K\). One inclusion is immediate. For the other, a point in every image has compatible lifts satisfying \(v(y_m)=0\); the finite-solution compactness argument of Lemma 1.2 produces a lift in \(K\). Since the modules at a fixed level are finite, the descending images stabilize. The finitely many strata give a single stabilization index for each \(n\), so the intersection defining \(B_n\) is a constructible sheaf.

On the stratum we have

\[
B_m=K/(K\cap\ell^mM).
\]

By Lemma 3.1, for \(m\geq k+c\),

\[
B_m/\ell^kB_m
=K/(\ell^kK+K\cap\ell^mM)
=K/\ell^kK.
\]

Choose one \(c\) for the finitely many strata. These identifications prove eventual constancy as sheaves, since an isomorphism can be tested on geometric stalks. Denote the eventual sheaf by \(\mathcal K_k\). Quotienting twice shows \(\mathcal K_{k+1}/\ell^k\mathcal K_{k+1}=\mathcal K_k\). Thus \(\mathcal K\) is strict and constructible.

Finally, replacing the pro-kernel by its stable images, and then replacing their induced filtrations by their adic filtrations, does not change the pro-object. The first replacement removes elements that disappear at a later index; the second uses the two inclusions \(\ell^mK\subset K\cap\ell^mM\) and Lemma 3.1. Hence \(\mathcal K\) represents the kernel in the pro-category and has its universal property among strict systems. Cokernels also agree with their pro-cokernels. The canonical coimage-to-image map is an isomorphism in the pro-category, and full faithfulness makes it an isomorphism of strict systems. Finite direct sums are strict. These facts prove all the abelian-category axioms. ∎

The proof also shows that the adic stalk of a kernel or cokernel is the corresponding kernel or cokernel of finite \(O\)-modules. It does not say that each finite-level sequence is exact on the left. Tensoring an exact module sequence with \(O_n\) can create a Tor term.

**Corollary 3.3.** Every adic sheaf has a torsion subsheaf \(T\), killed by one power of \(\ell\), such that \(\mathcal F/T\) is torsion-free. Its torsion-free quotient has flat finite-level stalks.

**Proof.** On the finitely many strata choose an exponent \(c\) killing the torsion of every stalk module. Then \(T=\ker(\ell^c:\mathcal F\to\mathcal F)\) has precisely the torsion stalks. The quotient has finite torsion-free \(O\)-stalks, hence free stalks. Their reductions are free \(O_n\)-modules. Flatness of a sheaf of modules is tested on stalks. ∎

For later reference, *torsion-free* always means that the adic kernel of multiplication by \(\ell\) vanishes. It does not mean that multiplication by \(\ell\) is injective at finite levels.

*References:* [Stacks, Tags 03UN–03UP]; [Deligne, Rapport, §§2.6–2.8].

## 4. Changing the coefficient field

**Definition 4.1.** The category of \(E\)-sheaves is obtained by making multiplication by \(\ell\) invertible in the adic category. Explicitly, keep the same objects and set

\[
\operatorname{Hom}_E(\mathcal F_E,\mathcal G_E)
=\operatorname{Hom}_O(\mathcal F,\mathcal G)\otimes_OE.
\]

The objects killed by this operation are exactly the torsion sheaves. They form a Serre subcategory: subobjects and quotients preserve a killing exponent, and an extension of objects killed by \(\ell^a\) and \(\ell^b\) is killed by \(\ell^{a+b}\). Localization of this abelian category is therefore abelian. Its stalks are \(\mathcal F_{\bar x}\otimes_OE\).

Corollary 3.3 supplies a torsion-free model for every \(E\)-sheaf. An *isogeny* is a map that becomes an isomorphism here; equivalently, its kernel and cokernel are torsion. In this situation both are killed by uniform powers of \(\ell\).

For a finite extension \(E'/\mathbb Q_\ell\), use its ring of integers \(O'\) and a uniformizer \(\varpi\). Repeat the definitions with \(O'/\varpi^n\), and invert \(\varpi\). The arguments above apply because \(O'\) is a complete discrete valuation ring. The resulting coefficient category is independent of the chosen uniformizer. A \(\overline{\mathbb Q}_\ell\)-sheaf in this course is defined over some finite extension \(E'\); extending coefficients further gives the same object in the filtered union of these categories.

A lisse \(E'\)-sheaf in this classical global-model category can be described by a finite-dimensional continuous \(E'\)-representation admitting a stable lattice. In fact every continuous representation of the profinite fundamental group admits one. Its image is compact. Starting with a lattice \(L\), compactness bounds all its translates inside \(\varpi^{-a}L\). Their \(O'\)-span is a stable finite module between \(L\) and \(\varpi^{-a}L\), hence a lattice. This supplies its adic model.

*Reference:* [Stacks, Tag 03UR]; [Deligne, Rapport, §2.9].

The pro-étale definition has a wider rational coefficient category: a sheaf locally free over the topological coefficient sheaf need only have an integral lattice locally. On a non-normal scheme there can be no global lattice. [The pro-étale site and ℓ-adic complexes, §§6–7](course:AG-LTF/the-pro-etale-site-and-l-adic-complexes) proves the local-lattice comparison and constructs a rank-one example on a rational nodal curve whose loop acts by \(\ell\). Our definition above remains the strict global-model category. Thus Proposition 1.3 and the compact-image argument classify exactly the objects they construct; they do not classify every pro-étale rational local system on a singular scheme.

## 5. Finite information from torsion cohomology

From now on \(X\) is separated of finite type over an algebraically closed field \(k\), and \(d=\dim X\). For a finite coefficient ring whose characteristic is invertible in \(k\), torsion cohomology supplies the following facts.

1. A constructible torsion sheaf has finite ordinary and compactly supported cohomology. Both vanish in degrees outside \([0,2d]\).
2. Compact support is computed by \(R\Gamma(\overline X,j_!(-))\) for a compactification \(j:X\hookrightarrow\overline X\). The construction is independent of the compactification.
3. For a separated finite-type map, the torsion functor \(Rf_!\) preserves bounded constructible complexes. It has a uniform finite cohomological bound.
4. Derived scalar extension commutes with compactly supported cohomology. In particular, for a constructible flat \(O_{n+1}\)-sheaf \(A\), there is a natural isomorphism in \(D(O_n)\)

\[
R\Gamma_c(X,A)\otimes^{\mathbf L}_{O_{n+1}}O_n
\simeq R\Gamma_c(X,A\otimes_{O_{n+1}}O_n).
\]

The tensor product must be derived on the left. Naturality includes endomorphisms of \(A\).

These are torsion prerequisites, rather than conclusions about inverse limits. [Cohomology with compact support, §§4–5, 7–8 and 10–12](course:ag-etale-cohomology/cohomology-with-compact-support) proves the compact dimension bound, compactification independence, composition and projection formula. Its §12 explicitly states the general finite-coefficient finiteness theorem [Stacks, Tags 0GL0 and 0GLH]. Ordinary finiteness is [Deligne, Th. finitude, Corollary 1.10], a consequence of the direct-image finiteness theorem under its stated field hypotheses. We retain these general finiteness inputs as prerequisites.

The ordinary bound for every torsion sheaf on a finite-type scheme of dimension \(d\) over a separably closed field is proved in [Cohomological dimension and the Künneth formula, Corollary 7.2](course:ag-etale-cohomology/cohomological-dimension-and-the-kunneth-formula). Lemma 8.4 there proves the canonical comparison

\[
R\Gamma(X,B)\otimes^L_{O_n}N
\xrightarrow{\sim}R\Gamma(X,B\otimes^L_{O_n}\underline N)
\]

for arbitrary coefficient complexes \(N\): finite cohomological dimension and qcqs continuity make derived sections preserve direct sums; free resolutions and their truncation telescopes reduce the map to the identity for \(N=O_n\). The compact version uses the same argument on a proper compactification and exact \(j_!\). For a ring map \(O_n\to O_m\), derived extension of scalars and the direct-image counit form this comparison in \(D(O_m)\). Forgetting its \(O_m\)-structure gives the comparison just proved, so conservativity of that forgetful functor proves the isomorphism with its target-ring structure. These natural maps give the fourth prerequisite and commute with endomorphisms. The historical locators are [Deligne, Rapport, §4.12] and [SGA 4, Exposé XVII, §§4.2.12 and 5.2.11]. These hypotheses apply over a field; no finiteness of the cohomology of an arbitrary base field is being asserted.

Here is how to recognize perfectness from these facts.

**Lemma 5.1.** Let \(A\) be a Noetherian ring. A complex with bounded finite cohomology and finite Tor amplitude is perfect.

**Proof.** Choose a bounded-above resolution by finite free modules, constructing generators of cohomology and then of the successive kernels. Bounded finite cohomology and Noetherianity permit this construction. Far enough to the left, all remaining cohomology vanishes. Replace the still further left part by the appropriate cokernel \(C\), which is a finite module. Tensoring the resulting resolution with an arbitrary module shows that \(\operatorname{Tor}_1(C,N)=0\): the corresponding degree lies below the given Tor amplitude. Thus \(C\) is flat. A finite module over a Noetherian ring is finitely presented, and a finitely presented flat module is projective. The truncation is consequently a bounded complex of finite projectives representing the original complex. ∎

**Proposition 5.2.** If \(A\) is a constructible flat \(O_n\)-sheaf, then \(R\Gamma_c(X,A)\) is perfect. The same is true of \(R\Gamma(X,A)\).

**Proof.** Its cohomology is bounded and finite by the torsion prerequisites. For any coefficient module \(N\), the torsion projection formula identifies its derived tensor product with the cohomology of \(A\otimes N\). This sheaf is concentrated in degree zero because \(A\) is flat. The torsion cohomological bound places that tensor product in \([0,2d]\); the bound applies also when \(N\) is not finite, by filtered colimits. Hence the complex has finite Tor amplitude. Apply Lemma 5.1. The argument for ordinary cohomology uses the ordinary projection formula and ordinary dimension bound. ∎

In particular, a torsion-free adic sheaf gives compatible perfect complexes

\[
K_n=R\Gamma_c(X,\mathcal F_n),\qquad
K_{n+1}\otimes^{\mathbf L}_{O_{n+1}}O_n\simeq K_n.
\]

We next prove what this compatibility implies, without using a geometric argument.

## 6. Recovering a finite complex over the complete ring

**Theorem 6.1.** Suppose \(K_n\in D_{\mathrm{perf}}(O_n)\) and isomorphisms \(K_{n+1}\otimes^{\mathbf L}_{O_{n+1}}O_n\simeq K_n\) are given. There is a bounded finite free \(O\)-complex \(P\) whose reductions represent these complexes and their transition maps. In particular,

\[
H^i(P)\simeq\varprojlim_n H^i(K_n)
\]

is finite and is zero for all but finitely many \(i\).

If endomorphisms \(u_n\) are compatible in the derived categories, their traces form \(t\in O\), and

\[
t=\sum_i(-1)^i\operatorname{Tr}\bigl(u\mid H^i(P)\otimes_OE\bigr).
\]

**Proof.** Begin with a bounded finite free representative of \(K_n\). If a differential matrix has a unit entry, row and column operations isolate a summand \(O_n\xrightarrow{1}O_n\). The identities \(d^2=0\) make this a direct contractible summand. Remove such summands until all differential entries lie in \((\ell)\). Call the resulting complex minimal.

A quasi-isomorphism between bounded complexes of projectives is a homotopy equivalence: its bounded acyclic projective cone is contractible, by splitting from the last nonzero term downward. A homotopy equivalence between minimal complexes reduces modulo \(\ell\) to an isomorphism in every degree, since the reduced differentials are zero. Nakayama's lemma makes its degree maps isomorphisms over \(O_n\). Thus a quasi-isomorphism between minimal representatives is an actual complex isomorphism.

Reduction of a minimal representative at level \(n+1\) is still minimal at level \(n\). Use the given derived isomorphism to identify this reduction with the chosen representative \(P_n\). Lifting bases recursively makes the term modules and differential matrices compatible. The ranks in every degree equal the dimensions of \(H^i(K_1)\). In particular, the support in degrees is the fixed finite support of \(K_1\). Taking inverse limits of the matrices produces a bounded finite free complex \(P\), with \(P/\ell^nP=P_n\).

We justify the cohomology assertion explicitly. Each finite group of cycles, boundaries and cohomology satisfies the Mittag–Leffler condition: images in a fixed finite group form a descending chain that stabilizes. Inverse limit is exact on such systems. Also a compatible family of boundaries has a compatible family of preimages, by the finite-solution compactness argument used in Lemma 1.2. Consequently cycles and boundaries of \(P\) are the limits of the finite-level cycles and boundaries, and their quotient is \(\varprojlim H^i(P_n)\). It is finite because it is a cohomology module of a bounded finite free \(O\)-complex over a Noetherian ring.

For the endomorphisms, choose chain representatives on the \(P_n\). At level \(n+1\), the reduction of a chosen representative \(v_{n+1}\) and the already chosen representative \(u_n\) differ by a homotopy:

\[
u_n-(v_{n+1}\bmod\ell^n)=dh+hd.
\]

Lift the matrices of \(h\) to \(P_{n+1}\) and replace \(v_{n+1}\) by \(v_{n+1}+d\widetilde h+\widetilde h d\). Its reduction is now exactly \(u_n\), and its derived morphism is unchanged. Induction gives compatible chain maps and a chain endomorphism \(u\) of \(P\).

The same construction works for maps between two compatible systems. There is also a precise uniqueness statement. If \(P,Q\) are their bounded finite free models, the bounded complex \(\operatorname{Hom}^\bullet_O(P,Q)\) reduces to \(\operatorname{Hom}^\bullet_{O_n}(P_n,Q_n)\). The cycles-and-boundaries argument above therefore gives

\[
\operatorname{Hom}_{D(O)}(P,Q)
\xrightarrow{\sim}\varprojlim_n
\operatorname{Hom}_{D(O_n)}(P_n,Q_n).
\]

Here the Hom groups are the degree-zero cohomology of these Hom complexes, because the source complexes are bounded projective. Thus a compatible family recovers one derived map, and two chain lifts of it are homotopic. This establishes the naturality needed for universal coefficients below.

The trace of a perfect-complex endomorphism is the alternating sum of its termwise traces. A null-homotopic map has zero such sum: the terms \(d^{i-1}h^i\) and \(h^id^{i-1}\) cancel, using \(\operatorname{Tr}(ab)=\operatorname{Tr}(ba)\). Hence the sum is homotopy invariant. It is also unchanged upon replacing a perfect representative by a homotopy equivalent one, using the same identity degree by degree and the homotopies of the composites. Matrix trace commutes with coefficient reduction, so these sums give \(t\in O\).

Over \(E\), apply trace additivity to the invariant subspaces of cycles and boundaries. Each boundary trace occurs once as a contribution to a term and once with opposite sign from the adjacent degree. They cancel, leaving precisely the alternating cohomology trace in the statement. Tensoring with \(E\) is exact, so \(H^i(P\otimes E)=H^i(P)\otimes E\). ∎

No uniform degree bound was assumed for the \(K_n\). The reduction compatibility forced one through minimal complexes. Compatibility of endomorphisms only in the derived categories was also enough; the homotopy adjustment is what permits their actual inverse limit.

*Reference:* [Stacks, Tag 03V4]; [Deligne, Rapport, §§4.11–4.13].

## 7. Cohomology and its torsion correction

**Definition 7.1.** For an adic sheaf on \(X\), set

\[
H^i(X,\mathcal F)=\varprojlim_nH^i(X,\mathcal F_n),\qquad
H_c^i(X,\mathcal F)=\varprojlim_nH_c^i(X,\mathcal F_n).
\]

**Theorem 7.2.** These are finite \(O\)-modules and vanish outside \([0,2d]\). For an \(E\)-sheaf, tensoring the cohomology of an adic model with \(E\) is independent of that model and gives finite-dimensional \(E\)-spaces with the same vanishing bound.

**Proof.** For a torsion-free model, Proposition 5.2 and Theorem 6.1 give finiteness. Each finite-level cohomology vanishes outside the stated range, so its limit does too.

For a general model, use \(0\to T\to\mathcal F\to L\to0\) from Corollary 3.3. The stalks of \(L\) are free over \(O\), so reduction gives an exact sequence of sheaves

\[
0\longrightarrow T/\ell^nT\longrightarrow\mathcal F_n
\longrightarrow L_n\longrightarrow0.
\]

There is no left Tor term, precisely because \(L\) is torsion-free. For all sufficiently large \(n\), the first sheaf is the fixed constructible torsion sheaf \(T\). The finite-level long cohomology sequences consist of finite groups. Their kernels and images are also systems of finite groups, so inverse limit preserves their exactness. Thus the cohomology of \(\mathcal F\) is an extension of subquotients of the finite cohomology of \(T\) and the finite \(O\)-cohomology of \(L\). It is finite. Vanishing again follows levelwise.

To prove independence after tensoring with \(E\), let two models be isomorphic in Definition 4.1. Represent the isomorphism and its inverse by \(\ell^{-a}f\) and \(\ell^{-b}g\). Their composite identities hold after localization, so some power of \(\ell\) kills \(gf-\ell^{a+b}\) and \(fg-\ell^{a+b}\). The same equalities hold on cohomology, since cohomology is \(O\)-linear on maps of systems. Tensoring with \(E\) therefore makes the induced maps inverse isomorphisms. This also proves independence for morphisms, not just for dimensions. ∎

**Theorem 7.3 (universal coefficients).** If \(\mathcal F\) is torsion-free, there are natural exact sequences

\[
0\longrightarrow H_c^i(X,\mathcal F)/\ell^n
\longrightarrow H_c^i(X,\mathcal F_n)
\longrightarrow H_c^{i+1}(X,\mathcal F)[\ell^n]
\longrightarrow0.
\]

The same statement holds for ordinary cohomology. Here \(M[\ell^n]=\ker(\ell^n:M\to M)\).

**Proof.** Let \(P\) be the finite free complex of Theorem 6.1. Multiplication by \(\ell^n\) is injective on every term of \(P\), so

\[
0\longrightarrow P\xrightarrow{\ell^n}P\longrightarrow P/\ell^nP\longrightarrow0
\]

is a short exact sequence of complexes. The middle part of its long cohomology sequence gives exactly the asserted short exact sequence, because \(H^i(P)=H_c^i(X,\mathcal F)\) and \(H^i(P/\ell^nP)=H_c^i(X,\mathcal F_n)\). These identifications respect maps: lifts of derived maps to the free complexes exist, and two choices are homotopic. Thus the sequence is natural. Use the ordinary perfect complexes for the ordinary version. ∎

This sequence measures the failure of reducing integral cohomology to equal finite-coefficient cohomology. For the complex \([O\xrightarrow{\ell^2}O]\) in degrees zero and one, \(H^0=0\) and \(H^1=O/\ell^2O\). Its reduction modulo \(\ell\) has \(H^0=O_1\). That entire group comes from \(H^1[\ell]\); it is invisible in \(H^0/\ell\).

The torsion-free condition concerns the coefficient sheaf. Its cohomology may still contain torsion.

## 8. Familiar objects with adic coefficients

**Tate twists.** The Kummer sheaves \(\mu_{\ell^n}\), with transition \(z\mapsto z^\ell\), form \(O(1)\). Étale locally their stalks are \(O_n\), and their inverse limit is the rank-one module of compatible roots of unity. On a field \(k\), its Galois representation is the cyclotomic character. Put \(O(r)=O(1)^{\otimes r}\) for positive \(r\), and use duals for negative \(r\). On \(\mathbb F_q\), arithmetic Frobenius acts on \(O(1)\) by \(q\); geometric Frobenius acts by \(q^{-1}\). The Frobenius lesson proves the convention behind this assertion.

**Projective space.** [Poincaré duality for smooth varieties, Examples 14.1–14.2](course:ag-etale-cohomology/poincare-duality-for-smooth-varieties) computes affine-space compact cohomology by products, and then projective-space cohomology by the closed-open triangle for \(\mathbb P^{r-1}\subset\mathbb P^r\). Its hyperplane Gysin normalization identifies the generators with powers of \(c_1\mathcal O(1)\). Thus

\[
H^{2a}(\mathbb P^r_k,O_n)=O_n(-a)\quad(0\leq a\leq r),
\qquad H^{2a+1}=0.
\]

The transition maps reduce the powers of the hyperplane class. Hence

\[
H^{2a}(\mathbb P^r_k,O)=O(-a),\qquad
H^{2a}(\mathbb P^r_k,E)=E(-a).
\]

Properness makes compactly supported and ordinary cohomology equal. This example has no cohomological torsion, so its universal coefficient sequences have zero right term.

**A family of elliptic curves.** Let \(f:C\to S\) be smooth and proper with geometrically connected genus-one fibres and a section. [Smooth base change and local acyclicity, Theorem 12.2](course:ag-etale-cohomology/smooth-base-change-and-local-acyclicity) makes \(R^1f_*O_n\) finite locally constant; proper base change and the genus-one Kummer calculation give rank two. On each geometric fibre the reduction maps are reductions of a free rank-two module, as the following canonical description also shows. Hence \((R^1f_*O_n)_n\) is a lisse adic sheaf. If \(T_\ell(C_{\bar s})\) denotes the elliptic curve's Tate module, its fibre is

\[
H^1(C_{\bar s},O)=\operatorname{Hom}_O(T_\ell(C_{\bar s}),O).
\]

To verify this description, put \(A=C_{\bar s}\). Kummer and the Abel identification \(A\simeq\operatorname{Pic}^0(A)\) give \(H^1(A,\mu_{\ell^n})=A[\ell^n]\), as proved in [The multiplicative group on a curve, §6 and the elliptic example in §9](course:ag-etale-cohomology/the-multiplicative-group-on-a-curve). The ordered cup-and-trace pairing of [Poincaré duality for curves, Theorem 11.1 and §12](course:ag-etale-cohomology/poincare-duality-for-curves) identifies

\[
H^1(A,O_n)=\operatorname{Hom}_{O_n}(A[\ell^n],O_n).
\]

These identifications commute with coefficient reduction. On the Kummer side \(\mu_{\ell^{n+1}}\to\mu_{\ell^n}\) induces multiplication by \(\ell\) on \(A[\ell^{n+1}]\); trace is degree modulo \(\ell^n\), and cup product is natural. The free rank-two system \(A[\ell^n]\), with these transitions, has limit \(T_\ell A\) and quotient \(T_\ell A/\ell^n=A[\ell^n]\), by Lemma 1.2. Taking limits of the displayed duals proves the claimed formula with its monodromy. This is the dual Tate-module representation; identifying it with the Tate module itself requires the duality twist.

**Rank-one character sheaves.** Suppose \(m\) is invertible in \(k\) and choose a finite coefficient extension containing the values of a character \(\chi:\mu_m(k^{\mathrm{sep}})\to E'^\times\). Over a base where the character is defined, the finite étale torsor \(z\mapsto z^m\) on \(\mathbb G_m\) and the one-dimensional representation \(\chi\) produce a lisse rank-one sheaf \(\mathcal L_\chi\). Choose the character values in \(O'^\times\) and reduce modulo \(\varpi^n\); this supplies its strict adic lattice. This descent description works even when \(\ell\mid m\), when averaging integral idempotents would be invalid.

In characteristic \(p\), the torsor \(z^p-z=x\) on \(\mathbb A^1\) has group \(\mathbb F_p\). A character \(\psi:\mathbb F_p\to E'^\times\) similarly gives an Artin–Schreier sheaf \(\mathcal L_\psi\). Here \(\ell\ne p\). These examples turn character values into local Frobenius traces, preparing for the trace formula and exponential sums.

## 9. Functoriality and its limits

Pullback is levelwise: an inverse-image functor is exact and commutes with coefficient reduction. It therefore sends a strict system to a strict system. Extension by zero along an open immersion is also levelwise and preserves strictness.

For a separated finite-type map \(f:X\to Y\), the compact-support derived operation on torsion-free coefficients starts with \(Rf_!\mathcal F_n\). Torsion constructibility and the projection formula give compatible constructible complexes of finite Tor dimension. At a geometric point \(\bar y\), proper base change for the compactification identifies them with \(R\Gamma_c(X_{\bar y},\mathcal F_n)\). The preceding perfect-complex argument gives finite adic stalk cohomology there. The constructible adic derived formalism packages these compatible complexes as \(Rf_!\mathcal F\); the pro-étale lesson gives a precise category for that packaging. After inverting \(\ell\), the result is independent of the lattice by the same localization argument as in Theorem 7.2.

One must distinguish a compatible derived system from a strict system of its individual cohomology sheaves. The right term in Theorem 7.3 explains why \(R^if_!\mathcal F_n\) need not reduce to \(R^if_!\mathcal F_{n-1}\). Its adic cohomology sheaf is obtained in the adic formalism, with the necessary normalization of the system.

Ordinary direct image \(f_*\) is the degree-zero part of \(Rf_*\), not an exact functor. Nor does ordinary direct image of the levels automatically produce a strict system. Constructibility of \(Rf_*\) in the usual finite-type setting is a finiteness theorem; [Deligne, Th. finitude, Théorème 1.1 and Corollary 1.5] gives the relevant torsion statements for finite-type schemes over a regular Noetherian base of dimension zero or one, with the coefficient prime invertible. A field is such a base. We do not assert them for arbitrary morphisms of arbitrary Noetherian schemes. We use their adic extensions with these hypotheses.

## 10. Exercises and complete solutions

**Exercise 10.1 (first calculation).** Over an algebraically closed field of characteristic different from \(\ell\), compute integral and rational cohomology of \(\mathbb P^3\), including the transition maps.

**Solution.** Torsion cohomology has one copy of \(O_n\) in each of degrees \(0,2,4,6\), with respective twists \(0,-1,-2,-3\); the other groups vanish. The generator in degree \(2a\) is the \(a\)-th power of the hyperplane class, so transitions are coefficient reductions on these generators. Their limits are \(O,O(-1),O(-2),O(-3)\). Tensoring with \(E\) replaces \(O\) by \(E\). The same argument gives the formula for any \(\mathbb P^r\). ∎

**Exercise 10.2 (continuous characters).** For connected Noetherian \(X\), prove

\[
\varprojlim_nH^1(X,O_n)=\operatorname{Hom}_{\mathrm{cont}}(\pi_1(X,\bar x),O)
\]

with trivial coefficient action.

**Solution.** An \(O_n\)-torsor is a finite locally constant torsor. The fundamental-group equivalence identifies its class with a continuous homomorphism to the additive group \(O_n\). There is no conjugacy quotient to consider, since that group is abelian. A compatible family of these homomorphisms defines a homomorphism to \(\varprojlim O_n=O\). It is continuous because every finite quotient is continuous. Conversely, a continuous homomorphism to \(O\) reduces to such a family. These operations are inverse and additive. ∎

**Exercise 10.3 (normalizing a system).** On a geometric point, let \(G_n=O/\ell^{\lfloor(n+1)/2\rfloor}O\), with reduction transitions. Show that this system is not strict and compute the strict system obtained by eventual reduction modulo \(\ell^k\).

**Solution.** At \(n=2\), strictness would require \(G_3/\ell^2G_3=G_2\). The left side is \(O/\ell^2O\), whereas \(G_2=O/\ell O\). For any fixed \(k\), however, \(G_n/\ell^kG_n=O_k\) once \(n\geq2k-1\), and all later maps are identities under these identifications. The eventual sheaves are therefore \(F_k=O_k\); their transitions give the constant adic sheaf \(O\). This construction requires eventual constancy of the reductions; an arbitrary inverse system need not have it. ∎

**Exercise 10.4 (the misleading finite kernels).** Compute the levelwise kernels of multiplication by \(\ell\) on \(O_n\), their transitions and the adic kernel.

**Solution.** The finite kernel is \(\ell^{n-1}O/\ell^nO\), a copy of \(\mathbb F_\ell\). Its transition from level \(n+1\) sends \(\ell^n\) to zero modulo \(\ell^n\). Thus every stable image \(B_n\) in Theorem 3.2 is zero. The strictified kernel is zero. The adic cokernel is the constant torsion sheaf \(\mathbb F_\ell\), whose levels are all \(\mathbb F_\ell\). ∎

**Exercise 10.5 (universal coefficients from complexes).** Let \(P\) be bounded finite free over \(O\). Derive the universal coefficient sequence and compute it for \([O\xrightarrow{\ell^2}O]\), first modulo \(\ell\) and then modulo \(\ell^3\).

**Solution.** The exact complex sequence \(0\to P\xrightarrow{\ell^n}P\to P/\ell^nP\to0\) gives

\[
0\to H^i(P)/\ell^n\to H^i(P/\ell^nP)\to H^{i+1}(P)[\ell^n]\to0.
\]

For the stated two-term complex, \(H^0(P)=0\) and \(H^1(P)=O/\ell^2O\). Modulo \(\ell\), the differential is zero, so both reduced cohomology groups are \(O_1\). The degree-zero connecting map identifies \(O_1\) with the subgroup \(\ell O/\ell^2O\) of \(H^1(P)\). Modulo \(\ell^3\), the kernel of the differential is \(\ell O/\ell^3O\), and its cokernel is \(O/\ell^2O\). The connecting map sends the class of \(\ell a\) in that kernel to the class of \(a\) modulo \(\ell^2\): lift \(\ell a\) to \(O\), apply the differential to get \(\ell^3a\), and divide by \(\ell^3\). It is an isomorphism onto \(H^1(P)[\ell^3]=H^1(P)\), as the sequence predicts. ∎

**Exercise 10.6 (traces without free cohomology).** On \([O\xrightarrow{\ell^2}O]\), multiplication by \(a\in O\) acts on both terms. Compute the perfect-complex trace and compare it with rational cohomology.

**Solution.** The termwise trace is \(a-a=0\). After tensoring with \(E\), multiplication by \(\ell^2\) is an isomorphism, so the complex is acyclic and its cohomological trace is zero. At finite levels its cohomology can be nonzero and nonprojective; taking an ordinary matrix trace on those cohomology modules would not be a definition of the perfect-complex trace. ∎

## Foundations used by this lesson

The linked preceding lessons supply finite-local-system representability, constructible permanence, torsion dimension bounds and tensor comparisons. Their finite-étale Galois-category equivalence and general finiteness theorems remain explicitly inherited foundations. The examples use the exact projective-space, Kummer, curve-duality and smooth-proper local-constancy arguments linked above, with their stated geometric inputs. The full pro-étale constructible category and local rational lattices are developed in the next lesson. Here the abelian adic category, finite adic cohomology, compatible-perfect-complex recovery, recovery of morphisms and universal coefficients have complete proofs.

## References

- **[Stacks]** The Stacks Project, *Étale Cohomology*, *More on Étale Cohomology* and *The Trace Formula*. Tag links use the [AI Integrated Stacks Project English edition](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/trace.html), an edition with AI-proposed corrections and AI-written additions, not reviewed by the Stacks Project's maintainers. The [official Stacks Project](https://stacks.math.columbia.edu/) remains the upstream reference. Relevant trace labels are [adic sheaves](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/trace.html#trace-definition-l-adic-sheaf), [the abelian category](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/trace.html#trace-lemma-l-adic-abelian), and [compatible perfect complexes](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/trace.html#trace-lemma-piece-together).
- **[Milne, Étale lectures]** J. S. Milne, *Lectures on Étale Cohomology*, version 2.21, 22 March 2013, especially §§18–20. The strict-system recovery and torsion correction are proved above; §19 provides the classical comparison. [Author's notes](https://www.jmilne.org/math/CourseNotes/LEC.pdf).
- **[Deligne, Cohomologie étale]** P. Deligne, *Cohomologie étale*, SGA 4½, Lecture Notes in Mathematics 569, Springer, 1977. We use *Rapport sur la formule des traces* §§2 and 4, and *Théorèmes de finitude en cohomologie ℓ-adique* §1. [Scan at the Institute for Advanced Study](https://publications.ias.edu/sites/default/files/Number32.pdf).
- **[SGA 4]** M. Artin, A. Grothendieck and J.-L. Verdier, *Théorie des topos et cohomologie étale des schémas*, especially Exposés X and XVII. Torsion cohomology, cohomological dimension and derived sheaf operations. [Tome 3 of the re-edition](https://www.normalesup.org/~forgogozo/SGA4/tomes/tome3.pdf).
- **[SGA 5]** A. Grothendieck and collaborators, *Cohomologie ℓ-adique et fonctions L*. J.-P. Jouanolou's Exposé V treats projective adic systems; Exposé VI treats constructible adic sheaves, their cohomology and cycle classes. [English translation](https://github.com/KokunoYumeto/sga-en/releases/download/v2026-10-03-english-edition/06_SGA5_EN_COMPLETE_PUBLISHED_CONTENT_READER.pdf).

- **[Bhatt–Scholze]** B. Bhatt and P. Scholze, [*The pro-étale topology for schemes*](https://arxiv.org/abs/1309.1198), version 2, §§6.5–6.8, for constructible complexes and the distinction between global rationalization and locally defined lattices.
