# A duality formula for diagrams in a topos

*Written by Claude Opus 5.5 (Anthropic) on 20 October 2026. Self-checked by the writing AI. Public domain (CC0).*

For a diagram \(X\) of objects of a topos \(T\), a module \(E\) of the first total topos and a module \(F\) of the second have an internal Hom with values in the second total topos: on each level it is the internal Hom of the levels, and the maps of \(E\), which go from \(f^*E_j\) to \(E_i\), combine with those of \(F\), which go from \(F_i\) to \(f^*F_j\), to make these internal Homs a module of the second total topos. For a module \(M\) of \(T\), pulled back to every level, this lesson proves the duality formula
\[
\begin{gathered}R\operatorname{Hom}_{\operatorname{Top}(X)}(L,M_X)\\ \cong R\Gamma\bigl(\operatorname{Top}^{\mathrm o}(X),R\underline{\operatorname{Hom}}^{\mathrm o}(L,M_X)\bigr),\end{gathered}
\]
which computes the Ext groups of a module of the first total topos into a pulled back module by the cohomology of the second total topos. It follows from a relative form for a morphism of diagrams. The main step is that the internal Hom of the standard generators into a pulled back injective module is an injective module of the second total topos.

**Prerequisites.** Examples 1.2 (c) and Proposition 5.1 of [*Fibred topoi and their total topoi*](fibred-topoi-and-their-total-topoi.md); Proposition 4.2 of [*Morphisms of fibred topoi and modules on total topoi*](morphisms-of-fibred-topoi-and-modules-on-total-topoi.md); Proposition 1.2 of [*Cohomology of the second total topos and local systems*](cohomology-of-the-second-total-topos-and-local-systems.md); Lemma 1.2 and Theorem 3.2 of [*Left derived functors of left adjoints on total topoi*](left-derived-functors-of-left-adjoints-on-total-topoi.md); internal Hom of modules, its adjunction with the tensor product [[Stacks, Tag 03EO](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-modules.html#sites-modules-lemma-internal-hom-adjoint-tensor)] and its restriction to a localization [[Stacks, Tag 0E8H](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-modules.html#sites-modules-lemma-internal-hom-restriction)]; extension by zero [[Stacks, Tag 03DJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-modules.html#sites-modules-lemma-extension-by-zero-exact), [Tag 0E8I](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-modules.html#sites-modules-lemma-j-shriek-and-tensor), [Tag 03EV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-modules.html#sites-modules-lemma-j-shriek-flat)]; right adjoints of exact functors preserve injectives [[Stacks, Tag 015Z](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/homology.html#homology-lemma-adjoint-preserve-injectives)]; bounded below complexes of injectives [[Stacks, Tags 070J](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-bounded-below-injectives-K-injective), [05TG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-morphisms-into-injective-complex)]; resolutions by a generating subcategory [[Stacks, Tag 05T7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-subcategory-left-resolution)].

**Setting.** \(T\) is a topos with a commutative ring \(\mathcal O\), \(I\) a small category and \(X\colon I\to T\) a functor, a *diagram* in \(T\). As in Examples 1.2 (c) of the lesson on fibred topoi, \(X\) defines a good fibred topos with levels \(X_i=T/X(i)\); for \(f\colon i\to j\), \(f^*\) is the restriction along \(X(f)\colon X(i)\to X(j)\), and its left adjoint \(f_!\) composes with \(X(f)\). Both total topoi \(\operatorname{Top}(X)\) and \(\operatorname{Top}^{\mathrm o}(X)\) are topoi (Proposition 5.1 there). The levels carry the rings \(\mathcal O|_{X(i)}\), which form cartesian rings of both total topoi, and the module inverse images \(f^*\) are restrictions: they are exact, with the exact left adjoints \(f_!\), extension by zero [Stacks, Tag 03DJ], so they carry injective modules to injective modules [Stacks, Tag 015Z]. A module \(E\) of \(\operatorname{Top}(X)\) has maps \(E_f\colon f^*E_j\to E_i\), a module \(F\) of \(\operatorname{Top}^{\mathrm o}(X)\) has maps \(F_f\colon F_i\to f^*F_j\). For a module \(M\) of \(T\), \(M_X\) denotes the module with the levels \(M|_{X(i)}\) and the identity maps, a module of either total topos. Internal Homs are taken over the rings \(\mathcal O|_{X(i)}\).

## 1. The internal mixed Hom

**Definition 1.1.** For a module \(E\) of \(\operatorname{Top}(X)\) and a module \(F\) of \(\operatorname{Top}^{\mathrm o}(X)\), the module \(\underline{\operatorname{Hom}}^{\mathrm o}(E,F)\) of \(\operatorname{Top}^{\mathrm o}(X)\) has the levels \(\underline{\operatorname{Hom}}(E_i,F_i)\), and for \(f\colon i\to j\) the map
\[
\begin{aligned}&\underline{\operatorname{Hom}}(E_i,F_i)\longrightarrow\underline{\operatorname{Hom}}(f^*E_j,f^*F_j)\\&\quad\cong f^*\underline{\operatorname{Hom}}(E_j,F_j),\end{aligned}
\]
which sends a local section \(\varphi\) to \(F_f\circ\varphi\circ E_f\); the isomorphism is the restriction of internal Hom to a localization [Stacks, Tag 0E8H]. For complexes, \(\underline{\operatorname{Hom}}^{\mathrm o}(E,F)\) is the complex with the levels \(\underline{\operatorname{Hom}}^\bullet(E_i,F_i)\).

For \(i\xrightarrow{f}j\xrightarrow{g}k\), the identities \(E_{gf}=E_f\circ f^*(E_g)\) and \(F_{gf}=f^*(F_g)\circ F_f\) give \(F_{gf}\circ\varphi\circ E_{gf}=\) \(f^*(F_g)\circ\bigl(F_f\circ\varphi\circ E_f\bigr)\circ f^*(E_g)\), and the isomorphisms of [Stacks, Tag 0E8H] are compatible with composites of restrictions. So the maps satisfy the condition on composites of \(\operatorname{Top}^{\mathrm o}(X)\). The construction is contravariant in \(E\) and covariant in \(F\).

**Lemma 1.2.** Let \(E\) be a module of \(\operatorname{Top}(X)\) and \(N\) a module of \(T\). Then
\[
\begin{aligned}&\Gamma\bigl(\operatorname{Top}^{\mathrm o}(X),\underline{\operatorname{Hom}}^{\mathrm o}(E,N_X)\bigr)\\&\quad =\operatorname{Hom}_{\operatorname{Top}(X)}(E,N_X).\end{aligned}
\]

**Proof.** A global section of a module \(G\) of \(\operatorname{Top}^{\mathrm o}(X)\) is a family of global sections \(s_i\) of \(G_i\) with \(G_f(s_i)=f^*(s_j)\) for every \(f\colon i\to j\). For \(G=\underline{\operatorname{Hom}}^{\mathrm o}(E,N_X)\), the \(s_i\) are maps \(\varphi_i\colon E_i\to N|_{X(i)}\), and the condition reads \(\varphi_i\circ E_f=f^*(\varphi_j)\), the maps of \(N_X\) being identities. This is the condition for \((\varphi_i)\) to be a morphism \(E\to N_X\) of \(\operatorname{Top}(X)\). \(\square\)

**Lemma 1.3.** Every module of \(\operatorname{Top}^{\mathrm o}(X)\) is a submodule of an injective module whose levels are injective, and the levels of every injective module of \(\operatorname{Top}^{\mathrm o}(X)\) are injective.

**Proof.** The first assertion is Proposition 1.2 (4) of the lesson on the second total topos, whose proof applies to modules: the inverse images \(f^*\) carry injective modules to injective modules (Setting). An injective module is a direct summand of such a module, so its levels are direct summands of injective modules. \(\square\)

**Definition 1.4.** For \(E\in D(\operatorname{Top}(X))\) and \(F\in D^+(\operatorname{Top}^{\mathrm o}(X))\), put \(R\underline{\operatorname{Hom}}^{\mathrm o}(E,F)=\underline{\operatorname{Hom}}^{\mathrm o}(E,J)\), where \(F\to J\) is a quasi-isomorphism to a bounded below complex of injective modules of \(\operatorname{Top}^{\mathrm o}(X)\).

**Lemma 1.5.** \(R\underline{\operatorname{Hom}}^{\mathrm o}\) is a well defined functor \(D(\operatorname{Top}(X))^{\mathrm{op}}\times D^+(\operatorname{Top}^{\mathrm o}(X))\to\) \(D(\operatorname{Top}^{\mathrm o}(X))\). Its level \(i\) is \(R\underline{\operatorname{Hom}}(E_i,F_i)\). If \(F\to F'\) is a quasi-isomorphism to a bounded below complex with injective levels, then \(R\underline{\operatorname{Hom}}^{\mathrm o}(E,F)\cong\underline{\operatorname{Hom}}^{\mathrm o}(E,F')\). In particular, if \(M\to J\) is a quasi-isomorphism from \(M\in D^+(T)\) to a bounded below complex of injective modules of \(T\), then \(R\underline{\operatorname{Hom}}^{\mathrm o}(E,M_X)\cong\underline{\operatorname{Hom}}^{\mathrm o}(E,J_X)\).

**Proof.** Exactness in \(\operatorname{Top}^{\mathrm o}(X)\) is checked on the levels. On the level \(i\), a bounded below complex \(J_i\) of injective modules is K-injective [Stacks, Tag 070J], so \(\underline{\operatorname{Hom}}^\bullet(A,J_i)\) is exact for an exact complex \(A\): its sections over an object \(V\) of \(X_i\) form the complex \(\operatorname{Hom}^\bullet(A\otimes\mathcal O_V,J_i)\) [Stacks, Tag 03EO], and \(A\otimes\mathcal O_V\), the extension by zero of the restriction of \(A\) to \(V\), is exact. And a quasi-isomorphism \(w\colon J\to J'\) between bounded below complexes with injective levels is a homotopy equivalence on every level, its cone being a bounded below exact complex of injectives and hence contractible [Stacks, Tag 05TG]; so \(\underline{\operatorname{Hom}}^{\mathrm o}(E,w)\) is a quasi-isomorphism. For a quasi-isomorphism \(v\colon E'\to E\), the cone of \(\underline{\operatorname{Hom}}^{\mathrm o}(v,J)\) has the levels \(\underline{\operatorname{Hom}}^\bullet(\operatorname{cone}(v_i),J_i)\), exact by the first fact. Hence \(\underline{\operatorname{Hom}}^{\mathrm o}(E,J)\) does not depend on the choice of \(J\) up to canonical isomorphism and defines a functor on derived categories. If \(F\to F'\) is a quasi-isomorphism to a bounded below complex with injective levels, the map \(F\to J\) extends to a map \(F'\to J\) in the derived category, represented by a map of complexes [Stacks, Tag 05TG]; it is a quasi-isomorphism, so \(F'\) may replace \(J\). By Lemma 1.3, \(J\) has injective levels, so the level \(i\) is \(\underline{\operatorname{Hom}}^\bullet(E_i,J_i)=R\underline{\operatorname{Hom}}(E_i,F_i)\). The last assertion holds because \(J_X\) has the injective levels \(J|_{X(i)}\) [Stacks, Tag 015Z]. \(\square\)

## 2. The duality formula

For an object \(i\) of \(I\), the level functor \(i^*\colon\operatorname{Mod}(\operatorname{Top}(X))\to\operatorname{Mod}(X_i)\) has the exact left adjoint \(i_!\), with \((i_!Q)_k=\bigoplus_{f\colon k\to i}f^*Q\) (Proposition 4.2 (b) of the lesson on morphisms of fibred topoi), and the level functor \(i^{\mathrm o*}\) of \(\operatorname{Top}^{\mathrm o}(X)\) has the right adjoint \(i^{\mathrm o}_*\), with \((i^{\mathrm o}_*G)_k=\prod_{f\colon k\to i}f^*G\) (Proposition 1.2 (2) of the lesson on the second total topos, with \(n=1\)). Since \(i^{\mathrm o*}\) is exact, \(i^{\mathrm o}_*\) carries injective modules to injective modules [Stacks, Tag 015Z].

**Lemma 2.1.** Let \(Q\) be a flat module of \(X_i\) and \(J\) an injective module of \(T\). Then \(\underline{\operatorname{Hom}}(Q,J|_{X(i)})\) is an injective module of \(X_i\), and
\[
\begin{gathered}\underline{\operatorname{Hom}}^{\mathrm o}(i_!Q,J_X)\\ \cong i^{\mathrm o}_*\underline{\operatorname{Hom}}(Q,J|_{X(i)})\end{gathered}
\]
is an injective module of \(\operatorname{Top}^{\mathrm o}(X)\).

**Proof.** For a module \(A\) of \(X_i\), \(\operatorname{Hom}\bigl(A,\underline{\operatorname{Hom}}(Q,J|_{X(i)})\bigr)=\) \(\operatorname{Hom}(A\otimes Q,J|_{X(i)})\) [Stacks, Tag 03EO]. This is exact in \(A\), because \(Q\) is flat and \(J|_{X(i)}\) is injective. So \(\underline{\operatorname{Hom}}(Q,J|_{X(i)})\) is injective. On the level \(k\),
\[
\begin{aligned}&\underline{\operatorname{Hom}}\Bigl(\bigoplus_{f\colon k\to i}f^*Q,J|_{X(k)}\Bigr)\\&\quad =\prod_f\underline{\operatorname{Hom}}\bigl(f^*Q,f^*(J|_{X(i)})\bigr)\\&\quad \cong\prod_ff^*\underline{\operatorname{Hom}}(Q,J|_{X(i)}),\end{aligned}
\]
using \(J|_{X(k)}=f^*(J|_{X(i)})\) and [Stacks, Tag 0E8H]. For \(g\colon k\to l\), the map of \(i_!Q\) sends the summand \(g^*f'^*Q\) of \(g^*(i_!Q)_l\), for \(f'\colon l\to i\), to the summand of \(f=f'g\), and the map of \(\underline{\operatorname{Hom}}^{\mathrm o}(i_!Q,J_X)\) is precomposition with it; the map of \(i^{\mathrm o}_*G\) projects the factor of \(f'g\) to the factor \(g^*f'^*G\). The two agree under the displayed isomorphisms. The last assertion follows from the first, as \(i^{\mathrm o}_*\) preserves injectives. \(\square\)

**Lemma 2.2.** Let \(\mathcal A\) be an abelian category, \(L\) a bounded above complex and \(N\) a bounded below complex of objects of \(\mathcal A\) such that \(\operatorname{Ext}^k(L^p,N^q)=0\) for all \(p\), \(q\) and \(k\geq1\). If \(\mathcal A\) has enough injectives, \(\operatorname{Hom}^\bullet(L,N)\) represents \(R\operatorname{Hom}(L,N)\).

**Proof.** Let \(N\to I\) be a quasi-isomorphism to a bounded below complex of injectives and \(C\) its cone, a bounded below exact complex with \(\operatorname{Ext}^k(L^p,C^q)=0\) for \(k\geq1\). Let \(Z^q\) be the kernel of \(C^q\to C^{q+1}\). The exact sequences \(0\to Z^q\to C^q\to Z^{q+1}\to0\), with \(Z^q=0\) for small \(q\), show by induction that \(\operatorname{Ext}^k(L^p,Z^q)=0\) for \(k\geq1\), and then that \(\operatorname{Hom}(L^p,C^\bullet)\) is exact. In each degree \(\operatorname{Hom}^\bullet(L,C)\) is a finite product of these groups, and filtering by \(p\) shows that it is exact. So \(\operatorname{Hom}^\bullet(L,N)\to\operatorname{Hom}^\bullet(L,I)\) is a quasi-isomorphism, and the target represents \(R\operatorname{Hom}(L,N)\) [Stacks, Tag 070J]. \(\square\)

**Theorem 2.3.** For \(L\in D^-(\operatorname{Top}(X))\) and \(M\in D^+(T)\), there is a canonical isomorphism, functorial in \(L\) and \(M\),
\[
\begin{gathered}R\operatorname{Hom}_{\operatorname{Top}(X)}(L,M_X)\\ \cong R\Gamma\bigl(\operatorname{Top}^{\mathrm o}(X),R\underline{\operatorname{Hom}}^{\mathrm o}(L,M_X)\bigr).\end{gathered}
\]

**Proof.** Every module of \(\operatorname{Top}(X)\) is a quotient of a sum of modules \(i_!Q\) with \(Q\) free: if \(Q_i\to E_i\) are epimorphisms from free modules, the adjoint map \(\bigoplus_ii_!Q_i\to E\) is an epimorphism on every level. By [Stacks, Tag 05T7], \(L\) is represented by a bounded above complex whose terms are sums of modules \(i_!Q\) with \(Q\) flat. Represent \(M\) by a bounded below complex \(J\) of injective modules of \(T\).

The left side. For a sum \(P=\bigoplus_\alpha i_{\alpha!}Q_\alpha\) of such modules,
\[
\begin{aligned}&\operatorname{Ext}^k_{\operatorname{Top}(X)}(P,J^q_X)\\&\quad =\prod_\alpha\operatorname{Ext}^k(i_{\alpha!}Q_\alpha,J^q_X)\\&\quad =\prod_\alpha\operatorname{Ext}^k_{X_{i_\alpha}}(Q_\alpha,J^q|_{X(i_\alpha)})\\&\quad =0\end{aligned}
\]
for \(k\geq1\), because \(i_{\alpha!}\) is an exact left adjoint of the exact functor \(i_\alpha^*\), so that the adjunction passes to derived categories, and \(J^q|_{X(i_\alpha)}\) is injective. By Lemma 2.2, \(\operatorname{Hom}^\bullet_{\operatorname{Top}(X)}(L,J_X)\) represents \(R\operatorname{Hom}(L,M_X)\).

The right side. By Lemma 1.5, \(R\underline{\operatorname{Hom}}^{\mathrm o}(L,M_X)\) is represented by \(\underline{\operatorname{Hom}}^{\mathrm o}(L,J_X)\). Its terms are products of the modules \(\underline{\operatorname{Hom}}^{\mathrm o}(i_{\alpha!}Q_\alpha,J^q_X)\), which are injective by Lemma 2.1. So it is a bounded below complex of injective modules of \(\operatorname{Top}^{\mathrm o}(X)\), and \(R\Gamma\) of it is \(\Gamma\) of it.

By Lemma 1.2, applied in each degree, \(\Gamma\bigl(\operatorname{Top}^{\mathrm o}(X),\underline{\operatorname{Hom}}^{\mathrm o}(L,J_X)\bigr)=\) \(\operatorname{Hom}^\bullet_{\operatorname{Top}(X)}(L,J_X)\). This identification of the two sides does not depend on the choices: two choices are related by homotopy equivalences, compatibly with Lemma 1.2. \(\square\)

## 3. Morphisms of diagrams

Let \(Y\colon I'\to T\) be a second diagram and \(u\colon X\to Y\) a morphism of diagrams: a functor \(v\colon I\to I'\) and maps \(u_i\colon X(i)\to Y(v(i))\) natural in \(i\). On levels, \(u_i\) defines the localization morphism \(T/X(i)\to T/Y(v(i))\), whose module inverse image is the restriction along \(u_i\), exact with the exact left adjoint \(u_{i!}\). As in the lesson on morphisms of fibred topoi, \(u\) induces inverse images \(u^*\) and \(u^{\mathrm o*}\) on the modules of both total topoi, with the levels \(u_i^*E_{v(i)}\), and their right adjoints \(u_*\), \(u^{\mathrm o}_*\). The conditions (L) and (H) of the lesson on left derived functors hold, because the \(u_{i!}\) and the \(f_!\) are extensions by zero, which are exact. So \(u^*\) has a left adjoint \(u_!\) with a left derived functor \(Lu_!\colon D^-(\operatorname{Top}(X))\to D^-(\operatorname{Top}(Y))\), and \(R\operatorname{Hom}(Lu_!E,F)\cong R\operatorname{Hom}(E,u^*F)\) (Theorem 3.2 there).

**Lemma 3.1.** For \(A\in D(\operatorname{Top}(Y))\) and \(F\in D^+(\operatorname{Top}^{\mathrm o}(Y))\), \(u^{\mathrm o*}R\underline{\operatorname{Hom}}^{\mathrm o}(A,F)\cong R\underline{\operatorname{Hom}}^{\mathrm o}(u^*A,u^{\mathrm o*}F)\), canonically.

**Proof.** Represent \(F\) by a bounded below complex \(J\) of injective modules. Its levels are injective (Lemma 1.3), and so are the levels \(u_i^*J_{v(i)}\) of \(u^{\mathrm o*}J\), restriction to a localization preserving injectives. On the level \(i\), \(u_i^*\underline{\operatorname{Hom}}^\bullet(A_{v(i)},J_{v(i)})\cong\) \(\underline{\operatorname{Hom}}^\bullet(u_i^*A_{v(i)},u_i^*J_{v(i)})\) [Stacks, Tag 0E8H], compatibly with the maps of both sides. Lemma 1.5 identifies the two sides with these complexes. \(\square\)

**Theorem 3.2.** For \(E\in D^-(\operatorname{Top}(X))\) and \(F\in D^+(\operatorname{Top}^{\mathrm o}(Y))\) there is a canonical map
\[
\begin{gathered}R\underline{\operatorname{Hom}}^{\mathrm o}(Lu_!E,F)\\ \longrightarrow Ru^{\mathrm o}_*R\underline{\operatorname{Hom}}^{\mathrm o}(E,u^{\mathrm o*}F),\end{gathered}
\tag{3.1}
\]
functorial in \(E\) and \(F\). It is an isomorphism when \(F=M_Y\) for some \(M\in D^+(T)\).

**Proof.** *The map.* By adjunction, (3.1) corresponds to a map \(u^{\mathrm o*}R\underline{\operatorname{Hom}}^{\mathrm o}(Lu_!E,F)\to\) \(R\underline{\operatorname{Hom}}^{\mathrm o}(E,u^{\mathrm o*}F)\). We take the isomorphism of Lemma 3.1, to \(R\underline{\operatorname{Hom}}^{\mathrm o}(u^*Lu_!E,u^{\mathrm o*}F)\), followed by the map induced by the adjunction map \(E\to u^*Lu_!E\).

*The case \(F=M_Y\).* Represent \(E\) as in the proof of Theorem 2.3 by a bounded above complex whose terms are sums of modules \(i_!Q\) with \(Q\) flat, and \(M\) by a bounded below complex \(J\) of injective modules of \(T\). Then \(Lu_!E\) is represented by \(u_!E\) (Theorem 3.2 (1) of the lesson on left derived functors), and \(u^{\mathrm o*}J_Y=J_X\). For \(j=v(i)\), \(u_!i_!=j_!u_{i!}\), both being left adjoint to \(u_i^*j^*=i^*u^*\), and \(Q'=u_{i!}Q\) is flat [Stacks, Tag 03EV]. By Lemma 2.1, applied to \(Y\) and to \(X\),
\[
\begin{aligned}\underline{\operatorname{Hom}}^{\mathrm o}(u_!i_!Q,J^q_Y)&\cong j^{\mathrm o}_*\underline{\operatorname{Hom}}(Q',J^q|_{Y(j)}),\\ \underline{\operatorname{Hom}}^{\mathrm o}(i_!Q,J^q_X)&\cong i^{\mathrm o}_*\underline{\operatorname{Hom}}(Q,J^q|_{X(i)}),\end{aligned}
\]
and both are injective. So both sides of (3.1) are represented by complexes built termwise from these modules: the left side by \(\underline{\operatorname{Hom}}^{\mathrm o}(u_!E,J_Y)\) (Lemma 1.5), the right side by \(u^{\mathrm o}_*\underline{\operatorname{Hom}}^{\mathrm o}(E,J_X)\), since \(\underline{\operatorname{Hom}}^{\mathrm o}(E,J_X)\) is a bounded below complex of injectives. Now \(u^{\mathrm o}_*i^{\mathrm o}_*=j^{\mathrm o}_*u_{i*}\), both being right adjoint to \(u_i^*j^{\mathrm o*}=i^{\mathrm o*}u^{\mathrm o*}\), and
\[
\begin{gathered}u_{i*}\underline{\operatorname{Hom}}(Q,J^q|_{X(i)})\\ \cong\underline{\operatorname{Hom}}(u_{i!}Q,J^q|_{Y(j)}),\end{gathered}
\]
since for every module \(A\) of \(Y_j\), \(\operatorname{Hom}(u_i^*A\otimes Q,J^q|_{X(i)})=\) \(\operatorname{Hom}\bigl(u_{i!}(u_i^*A\otimes Q),J^q|_{Y(j)}\bigr)=\) \(\operatorname{Hom}(A\otimes u_{i!}Q,J^q|_{Y(j)})\) [Stacks, Tags 03EO, 0E8I]. So the two sides have the same terms. The map (3.1) is built from the adjunction maps of \(u_{i!}\) and \(u_i^*\), and so are these identifications; on each term, (3.1) is therefore the identification just described, and it is an isomorphism of complexes. \(\square\)

For the final object \(e\) of \(T\), viewed as a diagram of type the one-point category, and the morphism \(u\colon X\to e\), Theorem 3.2 gives \(R\underline{\operatorname{Hom}}(Lu_!L,M)\cong\) \(Ru^{\mathrm o}_*R\underline{\operatorname{Hom}}^{\mathrm o}(L,M_X)\) in \(D(\mathcal O)\). Applying \(R\Gamma(T,-)\), and using that \(u^{\mathrm o}_*\) preserves injectives, gives \(R\operatorname{Hom}(Lu_!L,M)\cong\) \(R\Gamma\bigl(\operatorname{Top}^{\mathrm o}(X),R\underline{\operatorname{Hom}}^{\mathrm o}(L,M_X)\bigr)\); with the adjunction \(R\operatorname{Hom}(Lu_!L,M)\cong R\operatorname{Hom}(L,M_X)\) this is Theorem 2.3 again.

## 4. Examples

**4.1. The structure ring.** For \(L=\mathcal O_X\), the ring of \(\operatorname{Top}(X)\), \(\underline{\operatorname{Hom}}^{\mathrm o}(\mathcal O_X,M_X)=M_X\), and Theorem 2.3 reads \(R\Gamma(\operatorname{Top}(X),M_X)\cong R\Gamma(\operatorname{Top}^{\mathrm o}(X),M_X)\): for a module pulled back from \(T\), the two total topoi have the same cohomology.

**4.2. A map of objects.** Let \(I=\{0\to1\}\) and \(X\) the map \(g\colon X(0)\to X(1)\) of \(T\). A module \(E\) of \(\operatorname{Top}(X)\) is a pair of modules \(E_0\) on \(X(0)\) and \(E_1\) on \(X(1)\) with a map \(E_g\colon g^*E_1\to E_0\), where \(g^*\) is the restriction along \(g\). The module \(\underline{\operatorname{Hom}}^{\mathrm o}(E,M_X)\) of \(\operatorname{Top}^{\mathrm o}(X)\) has the levels \(\underline{\operatorname{Hom}}(E_0,M|_{X(0)})\) and \(\underline{\operatorname{Hom}}(E_1,M|_{X(1)})\), and the map \(\underline{\operatorname{Hom}}(E_0,M|_{X(0)})\to\) \(g^*\underline{\operatorname{Hom}}(E_1,M|_{X(1)})=\) \(\underline{\operatorname{Hom}}(g^*E_1,M|_{X(0)})\) is precomposition with \(E_g\). Exercise 5.2 describes \(R\Gamma\) on \(\operatorname{Top}^{\mathrm o}(X)\) in this case, and Exercise 5.3 uses it to compute an Ext group of \(\operatorname{Top}(X)\) that does not vanish.

## 5. Exercises

**Exercise 5.1.** Let \(I\) be a category with an initial object \(o\) and \(X\) the constant diagram with value the final object of \(T\), so that every level is \(T\) and every \(f^*\) is the identity. Show that \(\Gamma(\operatorname{Top}^{\mathrm o}(X),G)=\Gamma(T,G_o)\) and \(R\Gamma(\operatorname{Top}^{\mathrm o}(X),G)\cong R\Gamma(T,G_o)\) for every module \(G\) of \(\operatorname{Top}^{\mathrm o}(X)\). Deduce from Theorem 2.3 that \(R\operatorname{Hom}_{\operatorname{Top}(X)}(L,M_X)\cong\) \(R\operatorname{Hom}_T(L_o,M)\), and explain this isomorphism in degree \(0\) directly.

**Exercise 5.2.** In Example 4.2, let \(G\) be a module of \(\operatorname{Top}^{\mathrm o}(X)\), with the map \(G_g\colon G_0\to g^*G_1\). Show that \(R\Gamma(\operatorname{Top}^{\mathrm o}(X),G)\) is represented by the cone, shifted by \(-1\), of the map
\[
\begin{gathered}R\Gamma(X(0),G_0)\oplus R\Gamma(X(1),G_1)\\ \longrightarrow R\Gamma(X(0),g^*G_1),\end{gathered}
\]
\((s_0,s_1)\mapsto G_g(s_0)-g^*(s_1)\).

**Exercise 5.3.** In Example 4.2, let \(T\) be the topos of sets, \(\mathcal O=k\) a field, \(X(0)=\{a,b\}\), \(X(1)=\{c\}\) and \(g\) the constant map. Let \(E\) be the module of \(\operatorname{Top}(X)\) with \(E_0=0\) and \(E_1=k\). Compute \(\operatorname{Ext}^n_{\operatorname{Top}(X)}(E,k_X)\) with Theorem 2.3 and Exercise 5.2.

## 6. Complete solutions

**5.1.** A global section of \(G\) is a family of global sections \(s_i\) of \(G_i\) with \(G_f(s_i)=s_j\) for every \(f\colon i\to j\). For the unique arrows \(f_j\colon o\to j\), such a family satisfies \(s_j=G_{f_j}(s_o)\), and conversely every \(s_o\) defines a compatible family by this formula, since \(f\circ f_i=f_j\). So \(\Gamma(\operatorname{Top}^{\mathrm o}(X),G)=\Gamma(T,G_o)\). The level functor \(o^{\mathrm o*}\) is exact and has the exact left adjoint \(o^{\mathrm o}_!\), with \((o^{\mathrm o}_!N)_k=\bigoplus_{f\colon o\to k}f_!N=N\); so it carries injective modules to injective modules [Stacks, Tag 015Z], and \(R\Gamma(\operatorname{Top}^{\mathrm o}(X),-)=R\Gamma(T,-)\circ o^{\mathrm o*}\). Theorem 2.3 and the level \(o\) of \(R\underline{\operatorname{Hom}}^{\mathrm o}(L,M_X)\), which is \(R\underline{\operatorname{Hom}}(L_o,M)\) by Lemma 1.5, give \(R\operatorname{Hom}_{\operatorname{Top}(X)}(L,M_X)\cong\) \(R\Gamma\bigl(T,R\underline{\operatorname{Hom}}(L_o,M)\bigr)=\) \(R\operatorname{Hom}_T(L_o,M)\). In degree \(0\): a module of \(\operatorname{Top}(X)\) is a functor \(L\colon I^{\mathrm{op}}\to\operatorname{Mod}(T)\), the object \(o\) is final in \(I^{\mathrm{op}}\), so \(\varinjlim L=L_o\), and a morphism \(L\to M_X\) into the constant functor is a morphism \(\varinjlim L=L_o\to M\).

**5.2.** Let \(G\to J\) be an injective resolution in \(\operatorname{Top}^{\mathrm o}(X)\). By Lemma 1.3, \(J_0\) and \(J_1\) are complexes of injective modules, and so is \(g^*J_1\) (Setting); they compute \(R\Gamma\) of \(G_0\), \(G_1\) and \(g^*G_1\). As in the proof of Lemma 1.2, \(\Gamma(\operatorname{Top}^{\mathrm o}(X),J^q)\) is the kernel of the map \(\Gamma(J^q_0)\oplus\Gamma(J^q_1)\to\Gamma(g^*J^q_1)\), \((s_0,s_1)\mapsto J_g(s_0)-g^*(s_1)\). This map is surjective. Indeed, by the proof of Lemma 1.3, \(J^q\) is a direct summand of a module \(e^{\mathrm o}_*N\) with \(N\) injective on the discrete topos, and for \(e^{\mathrm o}_*N\), with the levels \(N_0\times g^*N_1\) and \(N_1\) (Section 2), the map to \(g^*N_1\) is the projection on the second factor of the first level. So there is an exact sequence of complexes
\[
\begin{aligned}0&\to\Gamma(\operatorname{Top}^{\mathrm o}(X),J)\to\Gamma(J_0)\oplus\Gamma(J_1)\\&\to\Gamma(g^*J_1)\to0,\end{aligned}
\]
and the first term is quasi-isomorphic to the cone of the last map, shifted by \(-1\).

**5.3.** The modules of \(T/X(0)\) are pairs of vector spaces indexed by \(a\) and \(b\), those of \(T/X(1)\) are vector spaces, and \(g^*\) sends \(V\) to \((V,V)\). All these modules are injective and have no higher cohomology. By Lemma 1.5, \(R\underline{\operatorname{Hom}}^{\mathrm o}(E,k_X)=\underline{\operatorname{Hom}}^{\mathrm o}(E,k_X)=G\), with \(G_0=0\), \(G_1=k\), and \(G_g=0\). By Exercise 5.2, \(R\Gamma(\operatorname{Top}^{\mathrm o}(X),G)\) is the cone, shifted by \(-1\), of the map \(0\oplus k\to k^2\), \(s\mapsto(-s,-s)\). Its cohomology is \(0\) in degree \(0\), \(k^2/\{(s,s)\}\cong k\) in degree \(1\) and \(0\) above. By Theorem 2.3, \(\operatorname{Hom}(E,k_X)=0\), \(\operatorname{Ext}^1(E,k_X)\cong k\) and \(\operatorname{Ext}^n(E,k_X)=0\) for \(n\geq2\). Directly: a module of \(\operatorname{Top}(X)\) is a representation of the quiver with the two arrows \(c\to a\) and \(c\to b\), given by the two components of \(E_g\); \(E\) is the simple representation at \(c\), and the nonsplit extensions of \(E\) by \(k_X\) are classified, up to the action of \(\operatorname{Hom}(E_c,(k_X)_c)\), by the pairs of maps \(E_c\to k\) at \(a\) and \(b\), which gives \(k^2/k\).

## Sources

The internal Hom with values in the second total topos and the duality formula are due to Illusie, in his work on the cotangent complex and the cohomology of diagrams, where they are stated for diagrams of diagrams of any depth. The proof given here, through the injectivity of the internal Hom of the standard generators, treats diagrams in a topos.
