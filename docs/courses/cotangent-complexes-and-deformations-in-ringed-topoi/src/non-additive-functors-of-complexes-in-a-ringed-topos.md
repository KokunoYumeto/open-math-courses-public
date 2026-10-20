# Non-additive functors of complexes in a ringed topos

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The cotangent complex is built with functors that are not additive: symmetric, exterior and divided powers, and free modules. Such a functor \(F\) cannot be applied term by term to a complex, since \(F(d)\circ F(d)=F(d\circ d)=F(0)\) need not vanish. Dold and Puppe extended non-additive functors to complexes concentrated in nonnegative homological degrees through the Dold–Kan correspondence. Illusie extended them to arbitrary complexes through simplicial–cosimplicial objects, and derived them on bounded-above complexes of modules over a ring of a topos.

This lesson proves the degree bound of Dold and Puppe and Deligne's homotopy invariance of the extension. It proves the theorem of Deligne and Lazard that flat modules over a ring of a topos are local inductive limits of finite free modules. With these it constructs the left derived functor \(LF\) on bounded-above complexes and gives its amplitude bounds and products. Shift formulas such as \(LS^n(E[1])\cong L\Lambda^n(E)[n]\) are proved in the next lesson.

**Prerequisites.** [*Homotopy sheaves and the free abelian Whitehead theorem*](homotopy-sheaves-and-the-free-abelian-whitehead-theorem.md), Section 5 (local inductive limits); [*The cotangent complex*](course:AG-HP/the-cotangent-complex#1-simplicial-algebra-and-the-standard-resolution), Theorems 1.1–1.3 (normalization, the inverse \(\Gamma\) of normalization with \(\Gamma(C)_n=\bigoplus_{[n]\twoheadrightarrow[k]}C_k\), Eilenberg–Zilber); [*Complexes, cones and localization*](course:derived-categories-and-sheaf-operations/complexes-cones-and-localization), Lemmas 1.2, 2.2 and 2.3 and Theorem 4.2. From the AI-integrated Stacks project, which proves them for ringed sites: Dold–Kan in abelian categories and for cosimplicial objects [[Stacks, Tag 019G](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-theorem-dold-kan), [Tag 019H](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-section-dold-kan-cosimplicial)]; homotopies of simplicial objects [[Tag 019L](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-lemma-relations-homotopy), [Tag 019S](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-lemma-homotopy-s-N)]; standard resolutions [[Tag 08ND](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-lemma-standard-simplicial-homotopy), [Tag 08P2](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-lemma-homotopy-equivalence)]; tensor products and flat modules on a ringed site [[Tag 03EK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-modules.html#sites-modules-section-tensor-product), [Tag 03EU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-modules.html#sites-modules-lemma-colimits-flat), [Tag 03EY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-modules.html#sites-modules-lemma-flat-ses), [Tag 08FC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-modules.html#sites-modules-lemma-flat-eq)].

## Conventions

\(\mathcal C\) is a small site, \(T=\operatorname{Sh}(\mathcal C)\), and \(A\), \(B\) are sheaves of rings on \(\mathcal C\). Modules are sheaves of modules. A module is *finitely presented* over \(U\in\mathcal C\) if it is the cokernel of a map \(A_U^m\to A_U^n\) of finite free \(A_U\)-modules. Complexes have differentials of degree \(+1\) unless they are called chain complexes. \(C(\mathcal A)\) is the category of complexes in an abelian category \(\mathcal A\), and \(K(\mathcal A)\) its homotopy category.

## 1. Functors of finite degree

Let \(F\colon\mathcal A\to\mathcal B\) be a functor between abelian categories with \(F(0)=0\), not necessarily additive. Such a functor is called *reduced*. Every functor \(G\) is the direct sum of the constant functor \(G(0)\) and a reduced functor, because \(G(0)\) is a retract of \(G(M)\) through \(0\to M\to0\).

Let \(M=M_1\oplus\cdots\oplus M_r\). For \(S\subseteq\{1,\ldots,r\}\) let \(e_S\colon M\to M\) be the projection onto \(\bigoplus_{s\in S}M_s\). Then \(e_Se_{S'}=e_{S\cap S'}\) and \(F(e_\varnothing)=0\), since \(e_\varnothing\) factors through \(0\). Put
\[
\varepsilon_S=\sum_{R\subseteq S}(-1)^{|S\smallsetminus R|}F(e_R),
\]
an endomorphism of \(F(M)\).

**Lemma 1.1.** The \(\varepsilon_S\), \(S\neq\varnothing\), are orthogonal idempotents with sum \(1_{F(M)}\), and \(\varepsilon_SF(e_R)=\varepsilon_S\) if \(S\subseteq R\), \(0\) otherwise.

**Proof.** If \(S\not\subseteq R\), choose \(s\in S\smallsetminus R\). Pairing each \(R'\subseteq S\) not containing \(s\) with \(R'\cup\{s\}\) gives terms of opposite signs with the same \(F(e_{R'\cap R})\), so \(\varepsilon_SF(e_R)=0\). If \(S\subseteq R\), every \(R'\subseteq S\) satisfies \(R'\cap R=R'\), so \(\varepsilon_SF(e_R)=\varepsilon_S\). Hence
\[
\varepsilon_S\varepsilon_{S'}=\sum_{S\subseteq R'\subseteq S'}(-1)^{|S'\smallsetminus R'|}\varepsilon_S,
\]
which is \(\varepsilon_S\) if \(S=S'\) and \(0\) otherwise. Möbius inversion of the definition gives \(F(e_R)=\sum_{\varnothing\ne S\subseteq R}\varepsilon_S\); take \(R=\{1,\ldots,r\}\). \(\square\)

The image of \(\varepsilon_S\) is the *cross-effect* \(\operatorname{cr}_SF(M_1,\ldots,M_r)\), and \(F(M)=\bigoplus_{S\ne\varnothing}\operatorname{cr}_SF(M_1,\ldots,M_r)\). If \(M_s=0\) for some \(s\in S\), the cross-effect is \(0\), because then \(e_R=e_{R\smallsetminus\{s\}}\) and the terms of \(\varepsilon_S\) cancel in pairs. Maps \(\varphi_i\colon M_i\to N_i\) give \(F(\oplus\varphi_i)\), which commutes with the \(\varepsilon_S\). An injection \(\iota\) of index sets, with the corresponding inclusion of a direct sum into a larger one, carries \(\operatorname{cr}_S\) into \(\operatorname{cr}_{\iota(S)}\). A projection onto a partial sum carries \(\operatorname{cr}_S\) isomorphically onto the corresponding cross-effect of the partial sum when \(S\) lies in the retained indices, and kills it otherwise.

**Definition 1.2.** A reduced functor has *degree \(\le k\)* if \(\operatorname{cr}_SF(M_1,\ldots,M_r)=0\) whenever \(|S|>k\), for all \(r\) and all \(M_i\).

**Example 1.3.** For modules over a sheaf of rings, the symmetric, exterior and divided power algebras \(S_A(M)\), \(\Lambda_A(M)\), \(\Gamma_A(M)\) are the sheaves associated with the corresponding constructions on sections, and they satisfy \(S(M\oplus N)\cong S(M)\otimes S(N)\), and likewise for \(\Lambda\), with the sign rule, and for \(\Gamma\). Hence
\[
\begin{aligned}&S^n(M_1\oplus\cdots\oplus M_r)\\&\quad\cong\bigoplus_{n_1+\cdots+n_r=n}S^{n_1}M_1\otimes\cdots\otimes S^{n_r}M_r,\end{aligned}
\]
and \(\varepsilon_S\) is the projection onto the summands with \(n_s\geq1\) exactly for \(s\in S\). These vanish when \(|S|>n\), so \(S^n\), \(\Lambda^n\) and \(\Gamma^n\) have degree \(\le n\). So has \(M\mapsto M^{\otimes n}\).

## 2. Extension to complexes

### 2.1. Nonnegative chain complexes

For a chain complex \(C\) in \(\mathcal A\) concentrated in degrees \(\ge0\), let \(\Gamma C\) be the simplicial object of Dold–Kan, with \((\Gamma C)_m=\bigoplus_{\sigma\colon[m]\twoheadrightarrow[j]}C_j\). The degeneracy \(s_t\) carries the summand of \(\sigma'\colon[m-1]\twoheadrightarrow[j]\) identically onto the summand of \(\sigma'\circ s^t\), where \(s^t\colon[m]\to[m-1]\) identifies \(t\) and \(t+1\) (Theorem 1.2 of [*The cotangent complex*](course:AG-HP/the-cotangent-complex); its formulas hold in every abelian category [Stacks, Tag 019G](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-theorem-dold-kan)). For a reduced \(F\), put \(F(C)=NF\Gamma C\), with \(N\) the normalized complex, which is the quotient by degenerate elements.

**Proposition 2.1 (Dold–Puppe).** If \(F\) has degree \(\le k\) and \(C_j=0\) for \(j>b\), then \(NF\Gamma C\) vanishes in degrees \(>kb\).

**Proof.** A *jump* of a surjection \(\sigma\colon[m]\twoheadrightarrow[j]\) is a \(t\in\{0,\ldots,m-1\}\) with \(\sigma(t)<\sigma(t+1)\); there are exactly \(j\) jumps. If \(t\) is not a jump, \(\sigma\) factors through \(s^t\). By Lemma 1.1, \(F((\Gamma C)_m)\) is the sum of cross-effects indexed by nonempty sets \(\Sigma\) of surjections, and only those with \(|\Sigma|\le k\) and every \(C_{j(\sigma)}\neq0\) can be nonzero. Such a set has at most \(kb\) jumps in all. If \(m>kb\), some \(t\) is a jump of no \(\sigma\in\Sigma\), so every \(\sigma\in\Sigma\) is \(\sigma'\circ s^t\). The inclusion of summands \(s_t\) then carries the cross-effect indexed by \(\{\sigma'\}\) onto the one indexed by \(\Sigma\). So the cross-effect consists of degenerate elements and is zero in the normalized quotient. \(\square\)

Dually, for a cochain complex \(C\) concentrated in degrees \(\ge0\), let \(\Gamma^\bullet C\) be the cosimplicial object of the cosimplicial Dold–Kan correspondence, which is the simplicial one in the opposite category [Stacks, Tag 019H](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-section-dold-kan-cosimplicial), and put \(F(C)=N^\bullet F\Gamma^\bullet C\). The opposite functor \(F^{\mathrm{op}}\colon\mathcal A^{\mathrm{op}}\to\mathcal B^{\mathrm{op}}\) is reduced of the same degree, because Definition 1.2 only uses finite direct sums, which are self-dual. Hence, by Proposition 2.1 in the opposite categories, \(N^\bullet F\Gamma^\bullet C\) vanishes in degrees \(>kb\) when \(C^q=0\) for \(q>b\).

### 2.2. Arbitrary complexes

A *mixed object* of \(\mathcal A\) is a functor \(\Delta^{\mathrm{op}}\times\Delta\to\mathcal A\): simplicial in a first index \(m\), cosimplicial in a second index \(n\). Normalizing in both directions gives a double complex in the second quadrant. The simplicial normalization projection acts on the first index and the cosimplicial one on the second, so the two commute. Applying \(\Gamma\) in the first direction and \(\Gamma^\bullet\) in the second gives the inverse equivalence between mixed objects and second-quadrant double complexes.

For a complex \(X\), let \(iX\) be the second-quadrant double complex with \((iX)^{p,0}=X^p\) for \(p\le0\), \((iX)^{0,q}=X^q\) for \(q\geq1\), and zero elsewhere. Its horizontal differentials are those of \(X\) in degrees \(<0\), and its vertical ones are those of \(X\) from degree \(0\) on. Its total complex is \(X\). For a reduced \(F\), put
\[
F(X)=\operatorname{Tot}NF\Gamma\,iX,
\]
where \(F\) is applied to each term of the mixed object \(\Gamma\,iX\). Since \(\Gamma\) and \(N\) commute with additive functors and \(N\Gamma=1\), \(F(X)\) is the termwise application when \(F\) is additive. If \(X^q=0\) for \(q>0\) (respectively \(q<0\)), \(\Gamma\,iX\) is constant in the cosimplicial (respectively simplicial) direction, and \(F(X)\) is the construction of Section 2.1.

**Proposition 2.2.** Let \(F\) be reduced of degree \(\le k\), and let \(X\) vanish outside \([a,b]\) with \(a\le0\le b\). Then \(F(X)\) vanishes outside \([ka,kb]\). Without a degree hypothesis, if \(X\) vanishes in degrees \(>b\) (respectively \(<a\)), so does \(F(X)\).

**Proof.** Fix the cosimplicial index \(n\). The row \(m\mapsto(\Gamma\,iX)_m^n\) is \(\Gamma\) of a chain complex concentrated in degrees \([0,-a]\), so after applying \(F\) its normalization vanishes in degrees \(m>-ka\), by Proposition 2.1. Fix \(m\). The column is \(\Gamma^\bullet\) of a cochain complex concentrated in degrees \([0,b]\), and its normalization vanishes for \(n>kb\). The double complex \(NF\Gamma\,iX\) is therefore nonzero only in bidegrees \((-m,n)\) with \(m\le-ka\) and \(n\le kb\), so its total degrees lie in \([ka,kb]\). For the second statement, the row argument uses only that a row is \(\Gamma\) of a chain complex in degrees \(\ge0\), and similarly for columns. \(\square\)

**Proposition 2.3 (Deligne).** If \(u,v\colon X\to Y\) are homotopic maps of complexes, then \(F(u)\) and \(F(v)\) are homotopic.

**Proof.** Let \(v-u=dh+hd\). Write \(h=h^++h^-\), where \(h^+\) agrees with \(h\) on \(X^i\) for \(i>0\) and is zero elsewhere, and \(h^-=h-h^+\). Put \(w=u+dh^++h^+d\), a map of complexes; then \(v-w=dh^-+h^-d\).

The map \(h^+\) consists of maps \(X^i\to Y^{i-1}\) with \(i\geq1\), all inside column \(0\) of \(iX\) and \(iY\). As a map between the columns, it is a chain homotopy from \(iu\) to \(iw\); on the other columns \(iu\) and \(iw\) agree. It commutes with the horizontal differentials, because \(h^+\) vanishes on \((iX)^{0,0}\) and on every column other than \(0\). The dual of the construction at the end of the proof of Theorem 1.3 of [*The cotangent complex*](course:AG-HP/the-cotangent-complex) turns this chain homotopy into a cosimplicial homotopy from \(\Gamma^\bullet iu\) to \(\Gamma^\bullet iw\), compatible with the simplicial structure in the first index. By [Stacks, Tag 019L](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-lemma-relations-homotopy), dualized, such a homotopy is a family of maps of the terms satisfying identities between composites with the structure maps. A functor preserves such a family, so \(F\Gamma\,iu\) and \(F\Gamma\,iw\) are homotopic in the cosimplicial direction. By [Stacks, Tag 019S](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-lemma-homotopy-s-N), dualized and applied row by row, their normalizations are homotopic in the vertical direction, and so are the total complexes. The same argument in the horizontal direction applies to \(h^-\), which consists of the maps \(X^i\to Y^{i-1}\) with \(i\le0\), all inside row \(0\). \(\square\)

So \(F\) induces a functor \(K(\mathcal A)\to K(\mathcal B)\). If a composite \(GF\) is formed, \((GF)(X)\cong G(F(X))\) for \(X\) concentrated in degrees \(\le0\) or \(\ge0\), because \(\Gamma N\cong1\). For complexes with terms of both signs this isomorphism fails in general, because the embedding \(i\) is not compatible with composition.

## 3. Flatness and the Deligne–Lazard theorem

A local system of modules \((E_i)_{i\in L}\) over a locally filtered system \(L\), with \(E_i\) a module over \(\mathcal C_{/U}\) for \(i\in L(U)\), defines the local system of sets \(i\mapsto E_i(U)\). Its local inductive limit in the sense of Section 5 of [*Homotopy sheaves and the free abelian Whitehead theorem*](homotopy-sheaves-and-the-free-abelian-whitehead-theorem.md) is written \(\varinjlim_LE_i\). By Propositions 5.3–5.7 there, it is a module, it is exact, and it commutes with tensor products, finite direct sums, kernels, cokernels and homology.

**Lemma 3.1 (local factorization).** Let \(M\) be a flat \(A\)-module, \(E\) a finitely presented \(A_U\)-module and \(f\colon E\to M|U\). Then there is a covering \(\{U_\alpha\to U\}\) such that each \(f|U_\alpha\) factors through a finite free module.

**Proof.** Write \(E=\operatorname{coker}(A_U^m\xrightarrow{r}A_U^n)\), so \(f\) is given by \(x_1,\ldots,x_n\in M(U)\) satisfying the \(m\) relations \(\sum_ir_{ki}x_i=0\). By the equational criterion [Stacks, Tag 08FC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-modules.html#sites-modules-lemma-flat-eq), the first relation is locally trivial: on a covering, \(x=Cy\) with \(y\in M^{p_1}\) and \(r_1C=0\), where \(r_1\) is the first row of \(r\). The remaining relations become the relations \((r_kC)y=0\) on \(y\). Treating them one at a time, after finitely many refinements \(x=Dz\) with \(z\in M^p\) and \(rD=0\). Then \(e_i\mapsto\sum_jD_{ij}e_j\) defines \(A^n\to A^p\), which kills the image of \(r\) and so factors through \(E\). Followed by \(z\colon A^p\to M\), it gives \(f\). \(\square\)

**Theorem 3.2 (Deligne–Lazard).** An \(A\)-module is flat if and only if it is the local inductive limit of a local system of finite free modules.

**Proof.** Local inductive limits preserve flatness: \(\varinjlim_LE_i\otimes N=\varinjlim_L(E_i\otimes N|U)\), and \(\varinjlim_L\) is exact, so injections are preserved.

Conversely let \(M\) be flat. Let \(L(U)\) be the category of pairs \((F,\varphi)\), where \(F\) is a finite free \(A_U\)-module and \(\varphi\colon F\to M|U\); restriction is restriction. Direct sums give common targets. For parallel arrows \(a,b\) into \((F',\varphi')\), the map \(\varphi'\) kills \(\operatorname{im}(a-b)\). Lemma 3.1, applied to \(F'/\operatorname{im}(a-b)\to M\), gives locally an arrow \(c\colon F'\to F''\) with \(ca=cb\). Together with the zero module this gives (LF0)–(LF2). Every section of \(M\) is the image of \(A\to M\). If \(s\in F\) maps to zero, Lemma 3.1 applied to \(F/As\to M\) gives locally an arrow killing \(s\). Two elements of \(P(U)\) with the same image in \(M(U)\) are represented, locally and by (LF1), at a common object, and their difference is killed locally. So \(\varinjlim_LF\to M\) is locally surjective and injective on local representatives, hence an isomorphism. \(\square\)

**Proposition 3.3.** A bounded-above acyclic complex \(X\) of flat \(A\)-modules is the local inductive limit of a local system of bounded contractible complexes of finite free modules.

**Proof.** Let \(L(U)\) be the category of pairs \((E,f)\) with \(E\) a bounded complex of finitely presented \(A_U\)-modules and \(f\colon E\to X|U\). As in Lemma 6.2 of [*Homotopy sheaves and the free abelian Whitehead theorem*](homotopy-sheaves-and-the-free-abelian-whitehead-theorem.md), using direct sums and cokernels, \(L\) is locally filtered with local inductive limit \(X\). By Proposition 5.6 there, it suffices to show that every such \(f\) factors locally through a bounded contractible complex of finite free modules.

*Bounded case.* Suppose \(X\) is concentrated in \([a,b]\); induct on \(b-a\). If \(a=b\), then \(X=0\). We may take \(E\) zero above \(b\). By Lemma 3.1, \(f^b\colon E^b\to X^b\) factors locally through a finite free \(P\) by maps \(\alpha\colon E^b\to P\) and \(g\colon P\to X^b\). Let \(\widetilde X\) agree with \(X\) below \(b-1\), with \(\widetilde X^{b-1}=X^{b-1}\times_{X^b}P\) and \(\widetilde X^b=P\). The map \(f\) factors through \(\widetilde X\to X\), by \((f^{b-1},\alpha d)\) in degree \(b-1\) and \(\alpha\) in degree \(b\). Since \(X^{b-1}\to X^b\) is surjective (\(X\) is acyclic), so is \(\widetilde X^{b-1}\to P\), and its kernel is \(Z^{b-1}=\ker(X^{b-1}\to X^b)\). This kernel is flat [Stacks, Tag 03EY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-modules.html#sites-modules-lemma-flat-ses). Since \(P\) is finite free, the surjection onto \(P\) splits locally, and locally \(\widetilde X\cong X'\oplus[P\xrightarrow{1}P]\). Here \(X'=(X^a\to\cdots\to X^{b-2}\to Z^{b-1})\) is acyclic with flat terms in \([a,b-1]\). By induction \(E\to X'\) factors locally through a contractible finite free \(Q\) in \([a,b-1]\). Then \(E\to Q\oplus[P\to P]\to\widetilde X\to X\) is the required factorization.

*General case.* Let \(E\) vanish below \(c\). All cycle modules \(Z^q\) of \(X\) are flat, by descending induction from the top with [Stacks, Tag 03EY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-modules.html#sites-modules-lemma-flat-ses). Hence the good truncation \(X_{\ge c-1}=(X^{c-1}/Z^{c-1}\to X^c\to\cdots)\) is bounded, acyclic and flat. By the bounded case, \(E\to X_{\ge c-1}\) factors locally through a contractible finite free \(Q\) concentrated in \([c-1,\ast]\). Lift \(Q^{c-1}\to X^{c-1}/Z^{c-1}\) locally to \(X^{c-1}\), which is possible because \(Q^{c-1}\) is free. The lift is compatible with the differential, because \(X^{c-1}\to X^c\) factors through the quotient. This gives \(E\to Q\to X\). \(\square\)

## 4. The left derived functor

From now on \(F\colon\operatorname{Mod}(A)\to\operatorname{Mod}(B)\) is a reduced functor that commutes with restriction to every \(U\in\mathcal C\) and with local inductive limits. The functors \(S^n\), \(\Lambda^n\), \(\Gamma^n\) (with \(B=A\)) have these properties, because they are sheafified constructions defined by universal properties.

**Lemma 4.1.** \(F\) carries quasi-isomorphisms between bounded-above complexes of flat \(A\)-modules to quasi-isomorphisms.

**Proof.** Let \(u\colon X\to Y\) be such a map. Replace \(Y\) by \(Y\oplus CX\), with \(CX\) the cone of \(1_X\), and \(u\) by \((u,\mathrm{incl})\). The projection \(Y\oplus CX\to Y\) is a homotopy equivalence, so by Proposition 2.3 \(F\) of it is one. So assume \(u\) is a degreewise split injection. Its cokernel \(Z\) is bounded above, flat in each degree, and acyclic (Lemma 1.2 of [*Complexes, cones and localization*](course:derived-categories-and-sheaf-operations/complexes-cones-and-localization)). By Proposition 3.3, \(Z=\varinjlim_LZ_i\) with \(Z_i\) contractible complexes of finite free modules over \(U_i\). Pulling back \(0\to X\to Y\to Z\to0\) along \(Z_i\to Z|U_i\) gives \(0\to X|U_i\xrightarrow{u_i}Y_i\to Z_i\to0\), with \(u=\varinjlim_Lu_i\) by exactness of local inductive limits. Locally on \(U_i\) this sequence splits in each degree, since \(Z_i\) is finite free. A degreewise split sequence is the cone sequence of a map from the shifted quotient (Lemma 2.2 there); when the quotient is contractible, the first map is a homotopy equivalence (Lemma 2.4 there). So, locally, \(F(u_i)\) is a homotopy equivalence by Proposition 2.3, and \(F(u_i)\) is a quasi-isomorphism, because that is a local condition. Since \(F\), \(\Gamma\), \(i\), \(N\) and \(\operatorname{Tot}\) commute with \(\varinjlim_L\), \(F(u)=\varinjlim_LF(u_i)\), which is a quasi-isomorphism by exactness. \(\square\)

**Lemma 4.2 (flat resolutions).**

1. Every complex \(X\) with \(H^n(X)=0\) for \(n>b\) receives a quasi-isomorphism from a complex of flat modules vanishing in degrees \(>b\).
2. Let \(K^-(\mathrm{fl})\subset K^-(A)\) be the full subcategory of bounded-above complexes of flat modules. The inclusion induces an equivalence \(K^-(\mathrm{fl})[\mathrm{qis}^{-1}]\simeq D^-(A)\).

**Proof.** (1) Every module is a quotient of a flat module, for instance of a direct sum of modules \(j_{U!}A_U\) [Stacks, Tag 03EW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-modules.html#sites-modules-lemma-module-quotient-flat), so [Stacks, Tag 05T7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-subcategory-left-resolution) applies. (2) The cone of a map of bounded-above complexes of flat modules is again one, so \(K^-(\mathrm{fl})\) is a full triangulated subcategory. By (1) every object of \(K^-(A)\) receives a quasi-isomorphism from it, and [Stacks, Tag 0GSL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-localization-subcategory) gives the equivalence. \(\square\)

**Construction 4.3 (a resolution commuting with local inductive limits).** Let \(\Phi(M)=A^{(M)}\) be the free module on the underlying sheaf of \(M\), with counit \(\Phi(M)\to M\). Free modules are flat: \(\Phi(M)\otimes N\cong N^{(M)}\), and \(N\mapsto N^{(M)}\) is exact. The standard resolution \(P_\bullet(M)\) of this adjunction, \(P_r(M)=\Phi^{r+1}(M)\), is a simplicial flat module augmented to \(M\). After forgetting module structures, the augmentation is a homotopy equivalence [Stacks, Tag 08ND](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-lemma-standard-simplicial-homotopy), so \(NP_\bullet(M)\to M\) is a quasi-isomorphism on sections [Stacks, Tag 08P2](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-lemma-homotopy-equivalence), hence of sheaves.

For a complex \(Y\) vanishing in degrees \(>0\), regard it as a chain complex in degrees \(\geq0\). Apply \(P_\bullet\) to each term of the simplicial module \(\Gamma Y\), normalize in both simplicial directions, and take the total complex. Call the result \(L_0(Y)\). It is a complex of flat modules vanishing in degrees \(>0\). The augmentation \(L_0(Y)\to N\Gamma Y=Y\) is a quasi-isomorphism: its cone is the total complex of a first-quadrant double complex whose columns are acyclic by the previous paragraph, and such a total complex is acyclic [Stacks, Tag 0132](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/homology.html#homology-lemma-first-quadrant-ss). For a complex \(Y\) vanishing in degrees \(>b\), put \(L_b(Y)=L_0(Y[b])[-b]\). This is a bounded-above flat resolution of \(Y\), functorial among complexes vanishing above \(b\). Since \(\Gamma\), \(\Phi\), \(N\) and \(\operatorname{Tot}\) commute with \(\varinjlim_L\), so does \(L_b\), for local systems of complexes that all vanish above \(b\).

**Theorem 4.4.** The functor \(F\) induces a functor \(LF\colon D^-(A)\to D(B)\), the *left derived functor* of \(F\), with a natural isomorphism \(LF(X)\cong F(X')\) for every quasi-isomorphism \(X'\to X\) from a bounded-above complex of flat modules. If \((X_i)\) is a local system of complexes all vanishing in degrees \(>b\), and \(X=\varinjlim_LX_i\), then \(\varinjlim_LH^qLF(X_i)\cong H^qLF(X)\) for every \(q\).

**Proof.** By Proposition 2.3, \(F\) induces a functor \(K^-(\mathrm{fl})\to K(B)\). By Lemma 4.1 it carries quasi-isomorphisms to quasi-isomorphisms, so it induces a functor on \(K^-(\mathrm{fl})[\mathrm{qis}^{-1}]\), which is \(D^-(A)\) by Lemma 4.2. Under this equivalence \(X\) corresponds to any of its resolutions \(X'\), whence \(LF(X)\cong F(X')\). For the last statement, \(LF(X_i)=F(L_b(X_i))\) and \(LF(X)=F(L_b(X))=\varinjlim_LF(L_b(X_i))\), because \(F\), \(\Gamma\), \(i\), \(N\) and \(\operatorname{Tot}\) commute with \(\varinjlim_L\). Local inductive limits are exact and commute with cohomology. \(\square\)

**Remark 4.5.** The uniform bound in Theorem 4.4 is used only to obtain a resolution that commutes with local inductive limits. A resolution built from the mixed object \(\Gamma\,iY\) of Section 2.2 would not serve without it. Applying a functor of infinite degree in the cosimplicial direction produces complexes that are unbounded above. For instance, let \(C\) be \(\mathbb Z\) placed in degree \(1\) and \(F(M)\) the augmentation ideal of \(\mathbb Z[M]\). Then \((\Gamma^\bullet C)^n=\mathbb Z^n\), with one summand for each surjection \([n]\twoheadrightarrow[1]\). Since \(\mathbb Z[M_0\oplus\cdots\oplus M_{n-1}]=\bigotimes_t\mathbb Z[M_t]\), the cross-effect of all \(n\) summands is \(F(\mathbb Z)^{\otimes n}\neq0\). A summand survives cosimplicial normalization exactly when every \(t\in\{0,\ldots,n-1\}\) is a jump of one of its surjections, so this cross-effect survives in every degree \(n\geq1\).

**Proposition 4.6 (amplitude).** Let \(F\) have degree \(\le k\) and let \([a,b]\ni0\). If \(X\) is quasi-isomorphic to a complex of flat modules concentrated in \([a,b]\), then \(H^qLF(X)=0\) for \(q\notin[ka,kb]\). If \(F\) carries flat modules to flat modules, then \(LF(X)\) is quasi-isomorphic to a complex of flat modules in \([ka,kb]\). If \(F\) carries finite free modules to finite free modules and \(X\) is locally quasi-isomorphic to a complex of finite free modules in \([a,b]\), then \(LF(X)\) is locally quasi-isomorphic to a complex of finite free modules in \([ka,kb]\).

**Proof.** By Theorem 4.4, \(LF(X)=F(X')\) for such a representative \(X'\), and Proposition 2.2 places \(F(X')\) in \([ka,kb]\). Each term of \(F(X')\) is a finite direct sum of cross-effects of \(F\) evaluated on finite direct sums of terms of \(X'\). Each cross-effect is a direct summand of a value of \(F\), so flatness, and local freeness of finite type, pass to it. \(\square\)

**Example 4.7.** \(S^n\), \(\Lambda^n\) and \(\Gamma^n\) carry flat modules to flat modules and finite free modules to finite free modules, and they have degree \(\le n\). So \(LS^n\), \(L\Lambda^n\) and \(L\Gamma^n\) carry complexes of flat amplitude in \([a,b]\) to complexes of flat amplitude in \([na,nb]\), and perfect complexes of amplitude in \([a,b]\) to perfect complexes of amplitude in \([na,nb]\).

## 5. Products

For mixed objects \(P,Q\) of \(A\)-modules, the shuffle map in the simplicial direction and the Alexander–Whitney map in the cosimplicial direction combine into a map of double complexes \(NP\otimes NQ\to N(P\otimes Q)\) (Theorem 1.3 of [*The cotangent complex*](course:AG-HP/the-cotangent-complex) and its dual). On total complexes it gives
\[
\begin{aligned}&\operatorname{Tot}NP\otimes\operatorname{Tot}NQ\\&\quad\to\operatorname{Tot}N(P\otimes Q).\end{aligned}
\tag{5.1}
\]
This map is associative, because the shuffle and Alexander–Whitney maps are associative. It is a homotopy equivalence, because each of the two maps is one.

Let \(\mathbf T=\bigoplus_n\mathbf T^n\) be \(S_A\), \(\Lambda_A\) or \(\Gamma_A\). The multiplication \(\mathbf T^m\otimes\mathbf T^n\to\mathbf T^{m+n}\), applied termwise to \(\Gamma\,iE\) and composed with (5.1), gives maps of complexes \(\mathbf T^m(E)\otimes\mathbf T^n(E)\to\mathbf T^{m+n}(E)\), associative and natural in \(E\). For \(E\in D^-(A)\), compute with a bounded-above flat representative, for which the tensor product of complexes computes the derived tensor product (\(\mathbf T^m\) of a flat complex is flat by Example 4.7). This gives natural products
\[
L\mathbf T^m(E)\otimes^{\mathbf L}L\mathbf T^n(E)\longrightarrow L\mathbf T^{m+n}(E),
\]
and \(\bigoplus_nH^\ast L\mathbf T^n(E)\) is a bigraded algebra.

## 6. Exercises

**Exercise 6.1.** Show that \(M\mapsto M\otimes_AM\) has degree \(2\), and compute its second cross-effect \(\operatorname{cr}_2(M,N)\).

**Exercise 6.2.** Let \(C\) be the chain complex with \(C_1=\mathbb Z\) and all other terms zero. Compute \(NS^2\Gamma C\) and check Proposition 2.1.

**Exercise 6.3.** Show that a finitely presented flat module is, locally, a direct summand of a finite free module.

## 7. Complete solutions

**6.1.** \((M\oplus N)^{\otimes2}\) is the direct sum of \(M^{\otimes2}\), \(M\otimes N\), \(N\otimes M\) and \(N^{\otimes2}\), and \(\varepsilon_{\{1,2\}}\) projects onto \(\operatorname{cr}_2(M,N)=(M\otimes N)\oplus(N\otimes M)\). The cross-effects of three summands vanish, since every term of \((M_1\oplus M_2\oplus M_3)^{\otimes2}\) involves at most two of the summands.

**6.2.** \((\Gamma C)_m=\bigoplus_{\sigma\colon[m]\twoheadrightarrow[1]}\mathbb Z\cong\mathbb Z^m\). By Proposition 2.1, \(NS^2\Gamma C\) vanishes above degree \(2\), and it vanishes in degree \(0\) because \((\Gamma C)_0=0\). In degree \(1\) it is \(S^2(\mathbb Z e)=\mathbb Z e^2\). In degree \(2\), let \(e_a,e_b\) be the basis vectors of the surjections \((0,0,1)\) and \((0,1,1)\), so that \(s_0e=e_a\) and \(s_1e=e_b\). Then \(S^2(\mathbb Z^2)\) has basis \(e_a^2,e_ae_b,e_b^2\), and the degenerate part is spanned by \(e_a^2,e_b^2\), leaving \(\mathbb Z\,e_ae_b\). The faces of \(\Gamma C\), by the rules in Theorem 1.2 of [*The cotangent complex*](course:AG-HP/the-cotangent-complex), are \(d_0e_a=d_1e_a=e\), \(d_2e_a=0\), \(d_0e_b=0\), \(d_1e_b=d_2e_b=e\). Hence \(d_0(e_ae_b)=0\), \(d_1(e_ae_b)=e^2\), \(d_2(e_ae_b)=0\), and the differential sends \(e_ae_b\) to \(-e^2\). The complex \(\mathbb Z\xrightarrow{-1}\mathbb Z\) in degrees \(2,1\) is acyclic: \(LS^2\) of \(\mathbb Z\) placed in homological degree \(1\) is \(0\), in agreement with the shift formula \(LS^2(E[1])\cong L\Lambda^2(E)[2]\) of the next lesson, since \(\Lambda^2\mathbb Z=0\).

**6.3.** By Lemma 3.1 applied to the identity of the module \(E\), locally \(1_E\) factors as \(E\to P\to E\) with \(P\) finite free, so \(E\) is a direct summand of \(P\).

## Sources

The degree of a functor and Proposition 2.1 are due to Dold and Puppe. The extension to arbitrary complexes through mixed objects, its derived functor in a topos and Proposition 4.6 are Illusie's. Proposition 2.3 is Deligne's, as Illusie records, and Theorem 3.2 is the theorem of Deligne and Lazard. Lazard's theorem for modules over a ring is proved in [*Tor and flat modules*](course:AG-CA/tor-and-flat-modules). The flat-module lemmas on ringed sites are those of the AI-integrated Stacks project cited above. A modern treatment of derived functors of non-additive functors is L. Breen and R. Mikhailov, *Derived functors of non-additive functors and homotopy theory*, [arXiv:0910.2817](https://arxiv.org/abs/0910.2817).
