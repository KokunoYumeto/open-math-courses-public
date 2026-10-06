# Infinitesimal lifting and the invariance of étale morphisms under thickenings

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Independent local AI review found corrections in the preceding version; this revision awaits independent correction verification. Public domain (CC0).*

A square-zero ideal records a first infinitesimal displacement. Multiplication of two displacements vanishes, so the difference between two possible lifts obeys the Leibniz rule. This explains the roles of differentials: smoothness permits lifts, unramifiedness forces uniqueness, and étaleness supplies both. The resulting rigidity goes further than a single lifting problem. An étale scheme can be reconstructed from its restriction to a thickening, including a thickening whose nilpotents have no common exponent.

We use **Smooth morphisms** and **Étale morphisms and their local structure**, the algebraic lesson **Formally smooth, unramified and étale ring maps**, and **Cohomology of affine schemes and Serre's criterion**. Two auxiliary facts from **Quasi-coherent sheaves on schemes** and **Limits of schemes and Noetherian approximation** will be specified where needed. Schemes and bases are arbitrary unless a hypothesis is stated. A lift always respects the given base map.

## 1. How much nilpotence is available?

A **thickening** is a closed immersion \(i:T\hookrightarrow T'\) inducing a homeomorphism on underlying spaces. Its defining quasi-coherent ideal \(\mathcal J\) has locally nilpotent sections. A **first-order thickening** has \(\mathcal J^2=0\); a **finite-order thickening** has \(\mathcal J^{N+1}=0\) for one integer \(N\). The latter bound is an additional condition [Stacks, Tag [04EX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-definition-thickening)].

On an affine chart the distinction is between a nil ideal and a nilpotent ideal. For example, in

\[
A=k[z_1,z_2,\ldots]/(z_1^2,z_2^2,\ldots),\qquad I=(z_1,z_2,\ldots),
\tag{1.1}
\]

every element of \(I\) involves finitely many variables and is nilpotent. However \(z_1\cdots z_m\ne0\) for every \(m\), by the basis of monomials with each exponent zero or one. Thus \(I\) is not nilpotent. The morphism \(\operatorname{Spec}k\hookrightarrow\operatorname{Spec}A\) is still a thickening.

**Lemma 1.1 (base change).** The base change of a thickening is a thickening. Square-zero and finite-order bounds are preserved.

**Proof.** On rings, base change replaces \(I\subset A\) by \(IB\subset B\). If \(I^m=0\), then \((IB)^m=0\). If \(I\) is only nil, each element of \(IB\) is a finite sum \(\sum i_jb_j\). The finitely many nilpotent \(i_j\) generate a nilpotent ideal: if \(i_j^{n_j}=0\), every product of more than \(\sum(n_j-1)\) generators vanishes. Consequently that sum is nilpotent. Every prime of \(B\) contains \(IB\), so \(\operatorname{Spec}(B/IB)\to\operatorname{Spec}B\) is a homeomorphism. These assertions agree on affine overlaps. ∎ [Stacks, Tag [09ZU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-base-change-thickening)]

**Proposition 1.2 (affineness).** A scheme is affine if and only if any thickening of it is affine.

**Proof.** A closed subscheme of an affine scheme is affine. For the converse write \(T\hookrightarrow T'\), with \(T\) affine. The common topology makes \(T'\) quasi-compact and quasi-separated: the intersection of two affine opens of \(T'\) is the intersection of their quasi-compact reductions in the affine scheme \(T\), hence is quasi-compact.

First assume \(\mathcal J^{N+1}=0\). For any quasi-coherent \(\mathcal F\) on \(T'\), the filtration \(\mathcal J^a\mathcal F\) has successive quotients annihilated by \(\mathcal J\). They are pushforwards of quasi-coherent modules on \(T\), and therefore have zero positive cohomology. The long exact sequences of this finite filtration give \(H^1(T',\mathcal F)=0\). Serre's criterion makes \(T'\) affine. Both cohomological facts are the precise prerequisites in **Cohomology of affine schemes and Serre's criterion** [Stacks, Tags [01XB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-quasi-coherent-affine-cohomology-zero), [01XG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-quasi-separated-h1-zero-covering)].

For a general thickening use the quasi-coherent extension theorem: on a quasi-compact quasi-separated scheme, a quasi-coherent module is the directed union of its finite type quasi-coherent submodules [Stacks, Tag [01PG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/properties.html#properties-lemma-quasi-coherent-colimit-finite-type)]. Apply it to \(\mathcal J\), writing \(\mathcal J=\bigcup_\lambda\mathcal J_\lambda\). Each submodule is an ideal. On a finite affine cover, finitely many nilpotent generators of \(\mathcal J_\lambda\) give a common nilpotence exponent; taking the largest exponent over the cover gives \(\mathcal J_\lambda^{n_\lambda}=0\).

Put \(T_\lambda=V(\mathcal J_\lambda)\). These are quasi-compact quasi-separated schemes, their transition maps are closed immersions and hence affine, and \(T=\varprojlim T_\lambda\), as is checked on rings by taking the union of the ideals. The affine-limit criterion says that an affine limit of such a system has affine members at every sufficiently large stage [Stacks, Tag [01Z6](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-limit-affine)]. Choose one affine \(T_\lambda\). Its immersion into \(T'\) is a finite-order thickening, so the case just proved makes \(T'\) affine. This argument uses no common exponent for \(\mathcal J\). ∎ [Stacks, Tag [06AD](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-thickening-affine-scheme)]

When \(\mathcal J^2=0\), its conormal sheaf \(\mathcal C_{T/T'}=\mathcal J/\mathcal J^2\) is simply \(\mathcal J\), regarded as an \(\mathcal O_T\)-module. A finite-order thickening is a succession of first-order thickenings: use the quotients by \(\mathcal J,\mathcal J^2,\ldots,\mathcal J^{N+1}\), since \((\mathcal J^a/\mathcal J^{a+1})^2=0\) for \(a\ge1\).

## 2. The space of possible lifts

Consider a square-zero surjection of \(R\)-algebras \(C\twoheadrightarrow C/J\) and an \(R\)-map \(a:B\to C/J\). A **lift** is an \(R\)-map \(\alpha:B\to C\) reducing to \(a\). The \(B\)-action on \(J\) is well-defined through \(a\): two representatives in \(C\) differ by an element of \(J\), which kills \(J\).

**Proposition 2.1 (differences and actions).** If a lift exists, the set of lifts is a simply transitive set for

\[
\operatorname{Der}_R(B,J)
=\operatorname{Hom}_B(\Omega_{B/R},J).
\tag{2.1}
\]

**Proof.** For two lifts \(\alpha,\beta\), put \(\delta=\beta-\alpha\). Its values lie in \(J\). Additivity and triviality on \(R\) are immediate, and

\[
\begin{aligned}
\delta(bb')
&=\alpha(b)\delta(b')+\alpha(b')\delta(b)+\delta(b)\delta(b')\\
&=a(b)\delta(b')+a(b')\delta(b).
\end{aligned}
\tag{2.2}
\]

The last product vanishes because \(J^2=0\). Thus \(\delta\) is a derivation. Conversely, given a derivation \(\delta\), the same expansion proves that \(\alpha+\delta\) is multiplicative. It fixes \(R\), sends \(1\) to \(1\) because \(\delta(1)=0\), and reduces to \(a\). Every lift arises in this way, with a unique difference. The equality in (2.1) is the universal property of differentials. ∎ This affine computation is also [Formally smooth, unramified and étale ring maps](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/AG-CA-17.html), Proposition 2.1; it is included here to develop the sheaf and gluing statements that follow.

For a first-order thickening \(T\hookrightarrow T'\), an \(S\)-scheme \(X\), and \(a:T\to X\), this computation globalizes to the sheaf

\[
\mathcal H=\mathcal{H}om_{\mathcal O_T}(a^*\Omega_{X/S},\mathcal J).
\tag{2.3}
\]

The underlying map of any lift is already prescribed by \(a\), since \(|T|=|T'|\). Differences of the structure-sheaf maps therefore give derivations on the same underlying map. On affine charts Proposition 2.1 supplies both the difference and the action; compatibility with restriction glues them. Adding a derivation preserves locality of the stalk maps, since a unit modulo a square-zero ideal is a unit. The local lifts form a sheaf of sets \(\mathcal L\), because morphisms glue. On every open where \(\mathcal L\) has a section, \(\mathcal H\) acts freely and transitively. This is a **pseudo-torsor**; it is a torsor when it is locally nonempty [Stacks, Tags [02H5](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-action-by-derivations), [04FJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-action-sheaf), [04FL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-omega-deformation)].

There is a useful extension to a diagram of first-order thickenings \((T\subset T')\to(X\subset X')\). Fix both \(a:T\to X\) and the induced conormal map \(a^*\mathcal C_{X/X'}\to\mathcal C_{T/T'}\). Two lifts with these fixed data agree on the ideal of \(X\) in \(X'\), so their difference factors through \(\mathcal O_X\). The proof of (2.2) then gives the same pseudo-torsor (2.3). Conversely a derivation of \(\mathcal O_X\) composed with \(\mathcal O_{X'}\to\mathcal O_X\) adjusts a lift without changing its conormal map. If that map is not fixed, the derivation is instead taken on \(X'\), restricted to \(X\); this distinction prevents an incorrect substitution of reduced-target differentials.

If lifts \(\ell_i\) exist on an open cover, define \(d_{ij}=\ell_j-\ell_i\). Then \(d_{ij}+d_{jk}=d_{ik}\). They glue after adjustments \(\ell_i+c_i\) precisely when

\[
d_{ij}=c_i-c_j.
\tag{2.4}
\]

Thus the obstruction to gluing lies in the degree-one cohomology class of this torsor. It need not vanish on a non-affine scheme.

## 3. Formal lifting and its locality

For a morphism \(f:X\to S\), test every first-order thickening of affine schemes \(T\hookrightarrow T'\), every \(S\)-map \(T'\to S\), and every compatible \(a:T\to X\). Equivalently, test the restriction map

\[
\operatorname{Mor}_S(T',X)\longrightarrow\operatorname{Mor}_S(T,X).
\tag{3.1}
\]

The formal conditions are as follows.

| Condition on \(f\) | Requirement in every affine test |
|---|---|
| Formally smooth | (3.1) is surjective |
| Formally unramified | (3.1) is injective |
| Formally étale | (3.1) is bijective |

Finite type or finite presentation is not part of these definitions [Stacks, Tags [02H0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-definition-formally-smooth), [02HG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-definition-formally-etale)]. It follows directly that formally étale means formally smooth and formally unramified [Stacks, Tag [02HH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-formally-etale-unramified-smooth)]. Repeated square-zero tests also handle every finite-order affine thickening.

The formal conditions restrict to open source and target charts: a lift supplied in \(X\) lands in the chosen source open because its topological image is that of \(a\). For affine \(X=\operatorname{Spec}B\) and \(S=\operatorname{Spec}R\), maps from affine tests correspond to ring maps, so these definitions are exactly the algebraic formal conditions [Stacks, Tags [02H3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-formally-smooth-on-opens), [02H4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-affine-formally-smooth), [02HK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-formally-etale-on-opens), [02HL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-affine-formally-etale)].

**Proposition 3.1 (formal unramifiedness).** A morphism is formally unramified if and only if \(\Omega_{X/S}=0\), without a finiteness assumption.

**Proof.** If the differentials vanish, Proposition 2.1 makes two lifts equal locally, and hence globally. Conversely restrict a formally unramified morphism to affine charts \(R\to B\). For any \(B\)-module \(M\), the split square-zero algebra \(B\oplus M\) has two lifts of the identity for each derivation: \(b\mapsto(b,0)\) and \(b\mapsto(b,\delta(b))\). Uniqueness forces every derivation to vanish. Taking \(M=\Omega_{B/R}\) and the universal derivation shows that every \(db\) is zero, hence \(\Omega_{B/R}=0\). These charts cover \(X\). ∎

**Lemma 3.2 (the affine gluing calculation).** Let \(T\) be affine, \(\mathcal J\) quasi-coherent, and \(\mathcal P\) locally projective. Then every Čech one-cocycle for \(\mathcal{H}om(\mathcal P,\mathcal J)\) on a finite principal-open cover is a coboundary. If \(\mathcal P\) is finite locally free, this Hom sheaf is quasi-coherent and its entire positive cohomology vanishes.

Here **locally projective** means quasi-coherent with projective module of sections on every affine open; no finite-rank condition is imposed.

**Proof.** Write \(T=\operatorname{Spec}C\) and \(\mathcal P=\widetilde P\), with \(P\) projective. Choose a module \(Q\) with \(P\oplus Q=C^{(E)}\). Hence the Hom sheaf is a direct summand of \(\prod_{e\in E}\mathcal J\). On a finite principal cover its Čech complex is a corresponding direct summand of the product of the Čech complexes for \(\mathcal J\). Each of the latter is exact in positive degree by affine quasi-coherent cohomology. Products of exact complexes of modules are exact: preimages of coordinates can be chosen coordinate by coordinate. The degree-one summand is therefore exact. In finite rank, Hom from a vector bundle is its dual tensor \(\mathcal J\), so affine quasi-coherent vanishing applies directly. ∎ [Stacks, Tag [0D0E](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-h1-is-zero)]

**Theorem 3.3 (locality).** Each formal condition is local on source and target. Equivalently, it holds globally if it holds on compatible affine charts covering the source over an affine cover of the target.

**Proof.** Restriction and the affine case were established above. For the converse take an affine test \(T\subset T'\). A finite principal-open cover of \(T'\) can be chosen so that the corresponding opens of \(T\) map into charts of \(X\) over charts of \(S\). Formal smoothness of the chart rings supplies local lifts.

The algebraic prerequisite says that the module of differentials of any formally smooth algebra is projective. Projectivity of a quasi-coherent module on affine charts is local: refine a cover of an arbitrary affine open to finitely many principal opens; the map \(C\to\prod C_{g_i}\) is faithfully flat, and projectivity of the localized modules descends to \(C\). This uses the exact algebraic descent theorem for arbitrary projective modules [Stacks, Tags [05A9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-theorem-ffdescent-projectivity), [05JQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/properties.html#properties-lemma-locally-projective)]. Pullback preserves this local projectivity [Stacks, Tag [060M](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/properties.html#properties-lemma-locally-projective-pullback)]. Thus \(a^*\Omega_{X/S}\) on \(T\) meets Lemma 3.2. Equation (2.4) adjusts and glues the local lifts, proving formal smoothness.

Formal unramifiedness follows from local vanishing of \(\Omega\) and Proposition 3.1. For formal étaleness, the local lifts exist and are unique; on every overlap uniqueness makes them agree, so they glue uniquely. This also proves locality directly in that case. ∎ [Stacks, Tags [0D0F](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-formally-smooth), [0HAM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-formally-etale)]

The arbitrary-rank step matters. Hom from an infinitely generated projective module need not be quasi-coherent; the product Čech calculation replaces an unjustified appeal to quasi-coherent vanishing.

## 4. Recovering smoothness and étaleness

**Theorem 4.1 (infinitesimal criteria).** For any scheme morphism \(f:X\to S\),

\[
\begin{aligned}
f\text{ smooth}&\Longleftrightarrow
f\text{ locally of finite presentation and formally smooth},\\
f\text{ étale}&\Longleftrightarrow
f\text{ locally of finite presentation and formally étale}.
\end{aligned}
\tag{4.1}
\]

**Proof.** In the reverse direction restriction to affine charts turns the formal property into the ring-map property. Together with finite presentation on those charts, the algebraic smooth or étale criterion gives the desired morphism property.

For the smooth forward direction take an affine test \(T\subset T'\) and cover it by finitely many principal opens whose reductions map into smooth affine charts. The algebraic lifting criterion gives local lifts. The differential sheaf of a smooth morphism is finite locally free, by **Smooth morphisms**. Consequently \(\mathcal H\) in (2.3) is quasi-coherent on the affine scheme \(T\). Its Čech one-cocycle is a coboundary, so (2.4) gives compatible lifts and a global morphism \(T'\to X\). This is the complete gluing step, beyond the affine ring criterion.

For an étale map the affine lifts are unique. They agree on overlaps by Proposition 3.1, since étale maps have zero differentials, and glue uniquely. Smooth and étale maps are locally of finite presentation by their definitions. ∎ [Stacks, Tags [02H6](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-smooth-formally-smooth), [02HM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-etale-formally-etale), [025K](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-theorem-formally-etale)]

**Proposition 4.2.** A flat unramified morphism is formally étale, even when it is not locally of finite presentation.

**Proof.** The unramified quotient construction in **Étale morphisms and their local structure**, Lemma 1.2, gives local rings of affine neighbourhoods in the form \(A\to D\twoheadrightarrow B\), with \(D\) an étale \(A\)-algebra. The quotient ideal \(K\) need not be finitely generated. Flatness of the original morphism says that \(B\) is \(A\)-flat on these neighbourhoods.

The graph of \(\operatorname{Spec}B\to\operatorname{Spec}D\) is an open immersion into \(\operatorname{Spec}B\times_{\operatorname{Spec}A}\operatorname{Spec}D\): it is a section of the projection to \(\operatorname{Spec}B\), whose unramifiedness comes from \(D/A\). The other projection, to \(\operatorname{Spec}D\), is flat by base change from \(B/A\). Their composite is therefore flat. Thus \(B\) is \(D\)-flat.

Tensor \(0\to K\to D\to B\to0\) over \(D\) with \(B\). Flatness injects \(K\otimes_D B=K/K^2\) into \(B\); that map is zero, so \(K=K^2\). Now take a square-zero extension \(C\twoheadrightarrow C/J\) and an \(A\)-map \(B\to C/J\). First lift its composite \(D\to C/J\) uniquely to \(u:D\to C\), using formal étaleness of \(D/A\). Since \(u(K)\subset J\) and \(K=K^2\),

\[
u(K)=u(K^2)\subset J^2=0.
\]

Thus \(u\) factors through a lift \(B\to C\). Any other lift has the same composite with \(D\), so is equal. This proves formal étaleness on these charts, and Theorem 3.3 globalizes it. ∎ [Stacks, Tag [04FF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-unramified-flat-formally-etale)]

Finite presentation cannot be dropped from (4.1). The localization \(\mathbf Z\to\mathbf Q\) is formally étale: in a square-zero extension, every element that is a unit modulo the ideal is already a unit, and the localization property gives a unique lift. It is not finite type. Finitely many rational generators have denominators divisible by only finitely many primes, so cannot generate \(1/p\) for every prime \(p\). Hence \(\operatorname{Spec}\mathbf Q\to\operatorname{Spec}\mathbf Z\) is not étale.

## 5. Étale maps through every thickening

**Lemma 5.1 (a nil ideal suffices).** Let \(B\) be an étale \(A\)-algebra and \(I\) a nil ideal in an \(A\)-algebra \(C\). Every \(A\)-map \(B\to C/I\) lifts uniquely to \(C\).

**Proof.** Present \(B=A[X_1,\ldots,X_n]/(F_1,\ldots,F_m)\). Choose representatives \(c_i\in C\) of the generator images. The relation errors \(F_j(c)\) lie in \(I\). Their finitely generated ideal \(J\) is nilpotent, by the exponent argument in Lemma 1.1. Thus \(X_i\mapsto c_i\) gives \(B\to C/J\), reducing to the prescribed map modulo \(I\). Formal étaleness successively lifts it through the powers of \(J\) to \(C\).

If two maps \(B\to C\) agree modulo \(I\), their finitely many generator differences generate a nilpotent ideal \(J'\). They agree modulo \(J'\), and repeated formal étale uniqueness makes them equal in \(C\). No exponent for all of \(I\) was used. ∎

**Theorem 5.2 (morphism lifting).** Let \(S_0\hookrightarrow S\) be a thickening and \(X\to S\) étale. For every \(S\)-scheme \(Y\), put \(Y_0=Y\times_S S_0\) and \(X_0=X\times_S S_0\). Restriction gives a bijection

\[
\operatorname{Mor}_S(Y,X)
\xrightarrow{\ \sim\ }
\operatorname{Mor}_{S_0}(Y_0,X_0).
\tag{5.1}
\]

**Proof.** Start with a morphism on the right. Cover \(Y\) by affine opens whose reductions map into étale affine charts of \(X\) over affine charts of \(S\). The reductions are defined by nil ideals, by Lemma 1.1. Lemma 5.1 gives a unique lift on each such open. The local uniqueness also holds after restricting to affine opens in every overlap. Consequently the lifts agree on overlaps and glue. The same argument proves that two global lifts are equal. No affineness, quasi-compactness or finiteness condition on \(Y\) is needed. ∎ [Stacks, Tag [025H](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-theorem-etale-topological)]

**Theorem 5.3 (the remarkable equivalence).** Base change induces an equivalence

\[
\operatorname{Et}(S)\xrightarrow{\ \sim\ }\operatorname{Et}(S_0)
\tag{5.2}
\]

between the categories of all étale schemes over a scheme and over any thickening of it.

**Proof.** Theorem 5.2, with \(Y\) also étale, gives full faithfulness. To construct a lift of an étale \(X_0\to S_0\), cover \(S\) by affines \(V=\operatorname{Spec}A\), with \(V_0=\operatorname{Spec}(A/I)\). By the monic local structure theorem, \(X_0\) has an open cover over these bases by standard étale algebras

\[
B_0=((A/I)[t]/(f_0))_{g_0},
\qquad f_0\text{ monic},\quad f_0'\text{ invertible in }B_0.
\tag{5.3}
\]

Lift the coefficients to \(A\), keeping \(f\) monic, and form \(B=(A[t]/(f))_g\). The ideal \(IB\) is nil. Since \(f'\) is a unit modulo it, \(f'\) is a unit in \(B\): lift an inverse and invert \(1+r\) for the resulting nilpotent error \(r\). Thus \(B\) is étale and reduces to \(B_0\).

Let \(U_i\) denote the local lifts. Their reductions have intersections \(U_{0,ij}\). Since each reduction is a homeomorphism, these intersections determine open subschemes \(U_{ij}\subset U_i\). The identity identification on the reduced overlap lifts uniquely to an \(S\)-map \(U_{ij}\to U_{ji}\), by Theorem 5.2. Its inverse lifts too; the composites are identities by uniqueness. On triple overlaps the two composites have the same reduction, so uniqueness gives the cocycle condition. Glue the schemes \(U_i\) along these isomorphisms. Their structure maps glue to an étale \(X\to S\) with the required reduction. This proves essential surjectivity, for arbitrarily large covers as well as finite ones. ∎ [Stacks, Tag [039R](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-theorem-remarkable-equivalence)]

The uniqueness has a precise meaning: given a specified identification of the reduction with \(X_0\), any two lifts admit exactly one isomorphism respecting it. The unmarked objects can have automorphisms; (5.2) preserves their automorphism groups.

## 6. Keeping the lift finite

We give an algebraic construction so that finiteness of the lift is established, rather than assumed from the common topology.

**Lemma 6.1 (one square presentation).** Every étale \(R\)-algebra \(B\) has a finite presentation with equally many variables and equations and an invertible square Jacobian determinant on all of \(\operatorname{Spec}B\).

**Proof.** Write \(B=P/K\), with \(P=R[x_1,\ldots,x_n]\) and \(K\) finitely generated. The formally étale conormal criterion identifies

\[
K/K^2\xrightarrow{d}B^n
\tag{6.1}
\]

as an isomorphism. Choose \(f_1,\ldots,f_n\in K\) mapping to a basis, and put \(L=(f_1,\ldots,f_n)\). Then \(K=L+K^2\), so the finite \(P\)-module \(K/L\) equals \(K(K/L)\).

For completeness, the determinant trick applies as follows. With generators \(m_1,\ldots,m_r\) of \(K/L\), write \(m_i=\sum a_{ij}m_j\), with \(a_{ij}\in K\). Multiplying \((1-a)m=0\) by its adjugate gives \(q m=0\), where \(q=\det(1-a)\in1+K\). Thus \(qK\subset L\), and \(K_q=L_q\). Since \(q\) maps to \(1\) in \(B\),

\[
B\simeq P_q/(f_1,\ldots,f_n)
\simeq R[x_1,\ldots,x_n,z]/(f_1,\ldots,f_n,qz-1).
\tag{6.2}
\]

The upper-left Jacobian block is invertible in \(B\) by (6.1). The \(z\)-column is zero in the first \(n\) rows, and its last entry is \(q=1\) in \(B\). The full determinant is therefore a unit. ∎

**Theorem 6.2 (finite étale invariance).** The equivalence (5.2) restricts to

\[
\operatorname{F\acute Et}(S)\xrightarrow{\ \sim\ }\operatorname{F\acute Et}(S_0).
\tag{6.3}
\]

**Proof.** First let \(S=\operatorname{Spec}A\), \(S_0=\operatorname{Spec}(A/I)\), with \(I\) nil, and let \(B_0\) be finite étale over \(A/I\). Use Lemma 6.1 to present \(B_0\) by a square system. Lift the finitely many coefficients to \(A\) and let \(B\) be the resulting quotient algebra. It is finitely presented, \(B/IB=B_0\), and its Jacobian determinant is a unit modulo the nil ideal \(IB\), hence a unit in \(B\). The standard smooth criterion with relative rank zero makes \(B\) étale over \(A\).

Let \(b_1,\ldots,b_r\) be its algebra generators. Each reduction \(\bar b_j\) is integral over \(A/I\), so satisfies a monic polynomial \(\bar P_j\). Lift its coefficients to a monic \(P_j\in A[T]\). Then \(P_j(b_j)\in IB\) is nilpotent. For some \(N_j\), the monic polynomial \(P_j^{N_j}\) annihilates \(b_j\). Thus every generator is integral over \(A\); successive monic reductions show that finitely many bounded-degree monomials span \(B\) as an \(A\)-module. In particular \(B\) is finite.

For a general base, construct these finite étale lifts on an affine cover of \(S\). Theorem 5.2 uniquely lifts the prescribed overlap identifications, and forces their cocycles. The glued morphism is finite, since finiteness is local on the target. This constructs every object on the right of (6.3). Full faithfulness comes from Theorem 5.2. Finally, any étale lift of a finite étale reduction is uniquely isomorphic, with its marked reduction, to this finite lift, so it too is finite. ∎ [Stacks, Tag [0BQB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-thickening)]

A finite étale algebra is finite locally free: finite presentation as an algebra together with finiteness gives finite presentation as a module, and a finitely presented flat module is finite projective [Stacks, Tags [0564](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-finite-finitely-presented-extension), [00NX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-finite-projective)]. The proof above establishes finiteness before invoking this module criterion. It also proves (6.3) for every nil thickening, not only finite-order thickenings.

## 7. Tangents, obstructions and arithmetic

**Tangent vectors.** Let \(x:\operatorname{Spec}k\to X\) be a rational point of a \(k\)-scheme. The constant map supplies a distinguished lift to \(k[\epsilon]/(\epsilon^2)\). Proposition 2.1 identifies the other lifts with

\[
\operatorname{Hom}_k(x^*\Omega_{X/k},k).
\tag{7.1}
\]

For \(X=\operatorname{Spec}k[u,v]/(uv)\) at the origin, \(x^*\Omega\) has basis \(du,dv\): the relation \(v\,du+u\,dv=0\) becomes zero there. The tangent space has dimension two. For a point with a larger residue field \(K\), use \(K[\epsilon]\) and \(\operatorname{Hom}_K(\Omega_{X/k}\otimes K,K)\), rather than silently replacing \(K\) by \(k\).

**An affine obstruction.** On that same crossing, the map \(u\mapsto t,v\mapsto t\) into \(k[t]/(t^2)\) respects \(uv=0\). Every candidate lift to \(k[t]/(t^3)\) has images \(t+at^2,t+bt^2\). Their product is \(t^2\ne0\), in every characteristic. Thus the crossing is not formally smooth. The kernel \((t^2)/(t^3)\) is square-zero, so this is precisely an allowed test.

**A non-affine gluing obstruction.** Let \(T\) be the line with doubled origin: glue two copies \(U,V\) of \(\operatorname{Spec}k[t]\) along \(D(t)\) by the identity. The coordinate \(t\) is a global function on \(T\), defining \(a:T\to\mathbf A^1_k\). Construct \(T'\) by gluing two copies of \(\operatorname{Spec}k[t,\epsilon]/(\epsilon^2)\), with transition

\[
t_V\longmapsto t_U+\epsilon/t_U,\qquad
\epsilon\longmapsto\epsilon
\tag{7.2}
\]

on \(D(t)\). This is an isomorphism; its inverse substitutes \(t\mapsto t-\epsilon/t\). It reduces to the identity and gives a first-order thickening with ideal \(\mathcal O_T\epsilon\).

A lift of \(a\) on the two charts must have coordinate functions \(t_U+\epsilon h_U(t_U)\) and \(t_V+\epsilon h_V(t_V)\), with \(h_U,h_V\in k[t]\). Equation (7.2) makes compatibility equivalent to

\[
h_U(t)-h_V(t)=1/t.
\tag{7.3}
\]

No two polynomials satisfy this. The obstruction is the nonzero class of \(1/t\) in \(k[t,t^{-1}]/k[t]=H^1(T,\mathcal O_T)\), computed from this affine cover with affine overlap. Thus the smooth target \(\mathbf A^1_k\) does not have a global lift for this non-affine test. The affine condition in the definition was essential.

**Finite étale rings over \(\mathbf Z/p^n\).** Over \(\mathbf F_p\), finite étale algebras are finite products of finite fields. For each degree \(r\), choose a monic irreducible \(\bar f\in\mathbf F_p[T]\) defining \(\mathbf F_{p^r}\), and lift it to a monic \(f\in(\mathbf Z/p^n)[T]\). In

\[
B_r=(\mathbf Z/p^n)[T]/(f),
\tag{7.4}
\]

the derivative is a unit modulo \(p\), because finite fields are perfect, and hence a unit in \(B_r\). The algebra is finite free of rank \(r\) and étale. Theorem 6.2 makes it the unique marked lift of \(\mathbf F_{p^r}\), independent of the chosen polynomial. These unramified lifts are the rings customarily denoted \(W_n(\mathbf F_{p^r})\), the truncated Witt rings of finite fields. The naming uses the identification of \(W(k)\) with the unramified valuation ring of residue field \(k\) and \(W_n(k)=W(k)/(p^n)\); see Brinon and Conrad, [*CMI Summer School Notes on p-adic Hodge Theory*, §4.2, p. 48](https://math.stanford.edu/~conrad/papers/notes.pdf#page=48). Thus every finite étale \(\mathbf Z/p^n\)-algebra is

\[
\prod_{j=1}^m W_n(\mathbf F_{p^{r_j}}).
\tag{7.5}
\]

The empty product allows the zero algebra. Isomorphism classes are determined by the multiset of positive degrees \(r_j\). Automorphisms of each factor include the unique lifts of the \(r_j\) Frobenius automorphisms of its residue field; equal factors can also be permuted. Consequently unmarked uniqueness never means that the automorphism group is trivial.

## 8. Exercises

1. **Easy — the first failed extension.** For the crossing \(uv=0\), consider the map \(u,v\mapsto t\) to \(k[t]/(t^2)\). Show that it has no lift to \(k[t]/(t^3)\), and identify both the square-zero ideal and the relation obstruction.

2. **Medium — all differences.** Given \(a:B\to C/J\), with \(J^2=0\), prove directly that two \(R\)-algebra lifts differ by a derivation. Prove that adding every such derivation gives a lift, and explain the meaning when no lift exists.

3. **Medium — marked finite étale lifts.** Let \(I\subset A\) be nilpotent and \(B_0\) finite étale over \(A/I\). Construct a finite étale lift over \(A\), and prove uniqueness of an isomorphism that induces a specified reduction identification. What changes if the ideal is only nil?

4. **Medium — arithmetic classification.** Classify the finite étale algebras over \(\mathbf Z/p^n\). Compute the automorphisms of a connected rank-\(r\) algebra and explain why the word “unique” in Exercise 3 needs its marking.

5. **Hard — glue a smooth lift.** Let \(X\to S\) be smooth and \(T\subset T'\) a first-order affine thickening. Starting from local algebraic lifts of a given \(T\to X\), construct the Čech cocycle, remove it and glue a global lift. Account for the sign of the correcting zero-cochain and for the quasi-coherence of its coefficient sheaf.

## 9. Solutions

**1.** The quotient \(k[t]/(t^3)\to k[t]/(t^2)\) has kernel generated by \(t^2\); its square is zero modulo \(t^3\). Images lifting \(t\) have the form \(t+at^2\) and \(t+bt^2\). Their product is \(t^2\), because terms of degree at least three vanish. The class of \(t^2\) is nonzero in \(k[t]/(t^3)\). The relation \(uv=0\) cannot be respected, so no ring-map lift exists. This is an affine first-order test and disproves formal smoothness.

**2.** Set \(\delta=\beta-\alpha\). Reduction shows \(\delta(B)\subset J\); expansion of the product gives (2.2), with its quadratic term zero. Thus \(\delta\) is \(R\)-linear and obeys Leibniz for the \(B\)-module structure on \(J\) induced by \(a\). Conversely for any derivation \(\delta\), \(\alpha+\delta\) fixes \(R\), is additive and multiplicative, and sends \(1\) to \(1\); it reduces to \(a\). Different derivations give different lifts, and every lift has exactly one difference from \(\alpha\). The universal property of \(\Omega_{B/R}\) identifies these derivations with Hom in (2.1). Without a lift the set is empty; it is a pseudo-torsor, not a torsor with a chosen origin.

**3.** Present \(B_0\) by Lemma 6.1 and lift its square system to an algebra \(B\) over \(A\). The determinant is invertible modulo \(IB\); since that ideal is nilpotent, lifting its inverse gives an inverse by a finite geometric series. Hence \(B\) is étale and has the desired marked reduction. For each algebra generator lift a monic integral equation from \(B_0\); its value in \(B\) lies in \(IB\), so a power of the equation is a monic annihilator. The bounded monomials in the finitely many generators span \(B\), proving it finite.

Given two marked lifts, their specified reduction isomorphism lifts uniquely by Lemma 5.1, applied to a map from one étale algebra into the quotient of the other. Its inverse lifts too. Both composites reduce to identities, so uniqueness makes them identities. This proves existence and uniqueness of the marked isomorphism. For an ideal that is only nil, the determinant argument still works, each individual relation value is still nilpotent, and Lemma 5.1 still gives uniqueness. Thus the whole conclusion persists; no uniform exponent is necessary.

**4.** Reduce an algebra modulo \(p\). It becomes a finite product of finite separable extensions of \(\mathbf F_p\), which are exactly \(\mathbf F_{p^r}\). Conversely the monic presentations (7.4) give finite étale lifts of each factor; their products lift every reduced algebra. Theorem 6.2 and its full faithfulness identify all possibilities with (7.5). The reduction and the lift have the same underlying topological space, so a connected nonzero algebra corresponds to one field factor, of degree \(r\). Its automorphism group is that of \(\mathbf F_{p^r}/\mathbf F_p\), cyclic of order \(r\), generated by \(x\mapsto x^p\); every automorphism lifts uniquely. An isomorphism of marked lifts must reduce to the identity under their markings. Full faithfulness makes that isomorphism unique, while the unmarked algebra retains these Frobenius symmetries.

**5.** Choose a finite principal cover \(W_i'\) of the affine \(T'\) whose reductions \(W_i\) map into smooth affine charts of \(X\) over affine charts of \(S\). The algebraic criterion provides lifts \(\ell_i\) on \(W_i'\). Their differences \(d_{ij}=\ell_j-\ell_i\), interpreted as differences of ring maps, are derivations by Proposition 2.1. They are sections on \(W_i\cap W_j\) of

\[
\mathcal H=\mathcal{H}om_{\mathcal O_T}(a^*\Omega_{X/S},\mathcal J).
\]

On triple overlaps, cancellation gives \(d_{ij}+d_{jk}=d_{ik}\). Smoothness makes \(a^*\Omega_{X/S}\) finite locally free; hence \(\mathcal H=(a^*\Omega_{X/S})^\vee\otimes\mathcal J\) is quasi-coherent. All intersections of this principal cover are affine, and affine quasi-coherent vanishing makes its Čech complex exact in positive degree. Choose \(c_i\) so that \(d_{ij}=c_i-c_j\). The action of Proposition 2.1 replaces \(\ell_i\) by \(\ell_i+c_i\). Their new difference is \(d_{ij}+c_j-c_i=0\). Thus they agree and glue to an \(S\)-morphism \(T'\to X\) reducing to \(a\). Existence is global on the affine test, while uniqueness is not claimed: its possible differences are the global sections of \(\mathcal H\).

## What this lesson does not prove

The algebraic prerequisites are the split conormal criterion for formally smooth ring maps [Stacks, Tag [031I](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-characterize-formally-smooth-again)], its formally étale isomorphism case, and the finitely presented smooth and étale criteria, from **Formally smooth, unramified and étale ring maps**. Section 4 supplies the additional scheme gluing proof. We also use affine quasi-coherent vanishing and Serre's affineness criterion from **Cohomology of affine schemes and Serre's criterion** [Stacks, Tags [01XB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-quasi-coherent-affine-cohomology-zero), [01XG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-quasi-separated-h1-zero-covering)]; finite type quasi-coherent approximation from **Quasi-coherent sheaves on schemes** [Stacks, Tag [01PG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/properties.html#properties-lemma-quasi-coherent-colimit-finite-type)]; and the affine-limit criterion from **Limits of schemes and Noetherian approximation** [Stacks, Tag [01Z6](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-limit-affine)]. The auxiliary faithfully flat descent of arbitrary projective modules is [Stacks, Tag [05A9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-theorem-ffdescent-projectivity)]. Finite module criteria are [Stacks, Tags [0564](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-finite-finitely-presented-extension), [00NX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-finite-projective)]. None replaces the lifting or equivalence proofs.

The written scheme-theoretic providers are **Cohomology of affine schemes and Serre’s criterion**, Theorems 2.2 and 5.2 (the quasi-coherent-cohomology course, lesson 3; its public reader is pending), [Quasi-coherent sheaves on schemes](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-SS/quasi-coherent-sheaves-on-schemes.html), Theorem 4.2, for finite-type approximation on qcqs schemes, and [Limits of schemes and Noetherian approximation](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-MO/AG-MO-03.html) for the affine-transition limit criterion. The split conormal and projective-differentials statements are the written Theorem 3.1 of [Formally smooth, unramified and étale ring maps](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/AG-CA-17.html). Arbitrary-rank projectivity descent is a planned algebraic bridge in [Faithful flatness and the local criterion for flatness](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/AG-CA-08.html): for a faithfully flat map \(R\to S\), projectivity of \(M\otimes_R S\) implies projectivity of \(M\), without finite generation of \(M\). The written finite-projectivity case is Corollary 3.2; the infinite-rank bridge is required for the unrestricted formal-locality argument in Section 3.

The next lesson extends this equivalence from thickenings to every universal homeomorphism: see Étale neighbourhoods, henselization and quasi-finite morphisms, Theorem 5.7. Its proof constructs the canonical descent datum, invokes the exact internal integral-descent theorem and glues arbitrary étale objects; it also proves preservation of the site coverings. The topoi and their cohomology are treated in **Pushforward, pullback and finite morphisms**, Section 6, Theorem 6.2 (the étale-cohomology course, lesson 7; written, with public publication pending). The classification above uses the unramified characterization of \(W_n(\mathbf F_q)\); the Witt polynomial construction and its general functor are outside this lesson.

Our references are the Stacks Project at the cited tags and Vakil's *The Rising Sea*, §21.2 for differentials and §24.8 for infinitesimal lifting. The next lesson uses étale neighbourhoods to construct henselizations and to describe quasi-finite maps locally on the base.
