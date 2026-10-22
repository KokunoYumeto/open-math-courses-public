# Derived left adjoints on the second total topos and local inductive limits

*Written by Claude Opus 5.5 (Anthropic) on 20 October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson continues the study of left adjoints of inverse images of modules on total topoi. For a diagram in a topos whose category of local sections is locally filtered, the left adjoint is Deligne's local inductive limit, which is exact. On the second total topos the left adjoint is a colimit over comma categories, and it is computed level by level for morphisms that fix the index category. Under exactness conditions on flat modules it has a left derived functor, adjoint to the inverse image on derived Hom complexes. Over the opposite of the category of finite ordinals, the derived colimit of a simplicial module is its associated chain complex. This gives the derived left adjoint for simplicial topoi and the triviality of the décalage, in a form dual to the décalage statement for cohomology.

**Prerequisites.** [*Left derived functors of left adjoints on total topoi*](left-derived-functors-of-left-adjoints-on-total-topoi.md) and [*Cohomology of simplicial topoi and cohomological descent*](cohomology-of-simplicial-topoi-and-cohomological-descent.md); Section 5 of [*Homotopy sheaves and the free abelian Whitehead theorem*](homotopy-sheaves-and-the-free-abelian-whitehead-theorem.md); [*Derived colimits over a small category*](derived-colimits-over-a-small-category.md); Proposition 4.4 of [*Morphisms of fibred topoi and modules on total topoi*](morphisms-of-fibred-topoi-and-modules-on-total-topoi.md); composition of derived functors [[Stacks, Tag 015M](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-compose-derived-functors)].

## 1. Local inductive limits

Let \((T,\mathcal O)\) be a ringed topos, the sheaves on a site \(\mathcal C\), and \(I\) a small category. Let \(X\colon I^{\mathrm{op}}\to T\) be a functor, \(i\mapsto X_i\), with \(X(f)\colon X_j\to X_i\) for \(f\colon i\to j\). By Examples 1.2 (c) of the lesson on fibred topoi, the localized topoi \(T/X_i\) form a topos fibred over \(I^{\mathrm{op}}\), the arrow \(f\colon i\to j\) of \(I\) giving the localization \(T/X_j\to T/X_i\) along \(X(f)\). The localizations \(p_i\colon T/X_i\to T\) form a morphism \(u\) to \(T\), and with the rings \(\mathcal O|_{X_i}\), Setting 1.1 of the lesson on left derived functors applies with \(\varphi\) the identity. A module \(M\) on the total topos is a family of \(\mathcal O|_{X_i}\)-modules \(M_i\) with maps \(M_f\colon M_i|_{X_j}\to M_j\) for \(f\colon i\to j\), compatible with composites, and \(u^*E=(E|_{X_i})_i\).

**Definition 1.1.** The *category of local sections* of \(X\) is the system \(L_X\) over \(\mathcal C\) such that \(L_X(U)\) has the objects \((i,x)\), \(x\in X_i(U)\), and the arrows \((i,x)\to(j,y)\) the arrows \(f\colon i\to j\) with \(X(f)\circ y=x\); restriction along \(V\to U\) restricts \(x\). The diagram \(X\) is *locally filtering* if \(L_X\) is locally filtered (Definition 5.1 of the lesson on homotopy sheaves). A module \(M\) gives the local system \(F_M\) on \(L_X\) with \(F_M(i,x)\) the sections of \(M_i\) over \(x\colon U\to X_i\); an arrow \(f\colon(i,x)\to(j,y)\) maps a section over \(x=X(f)\circ y\) to its restriction along \(X(f)\) followed by \(M_f\).

**Proposition 1.2.** Let \(X\) be locally filtering. Then \(u_!M\cong\varinjlim_{L_X}F_M\), naturally in \(M\), and \(u_!\) is exact. Hence \(L_qu_!=0\) for \(q>0\), and \(Lu_!\) is \(u_!\) applied to each term of a complex.

**Proof.** For an \(\mathcal O\)-module \(E\), a map \(M\to u^*E\) is a family of maps \(M_i\to E|_{X_i}\) compatible with the \(M_f\). On sections it is a family of maps \(F_M(i,x)\to E(U)\), natural in \((i,x)\in L_X(U)\) and compatible with restriction, that is, a map of local systems \(F_M\to E_{L_X}\), and module maps correspond to linear ones. By Proposition 5.3 of the lesson on homotopy sheaves, these are the maps \(\varinjlim_{L_X}F_M\to E\), the module structure of the local inductive limit coming from Proposition 5.5 there. So \(\varinjlim_{L_X}F_{(-)}\) is left adjoint to \(u^*\), hence isomorphic to \(u_!\). The functor \(M\mapsto F_M\) is left exact, and local inductive limits commute with finite limits (Proposition 5.5 there). So \(u_!\) preserves monomorphisms; being a left adjoint, it is right exact. Hence \(u_!\) is exact. An exact functor carries quasi-isomorphisms of bounded above complexes to quasi-isomorphisms, so it is its own left derived functor. \(\square\)

For example, if \(I\) is filtered and \(X\) is constant with value the final object, \(L_X(U)\) is \(I\) for every \(U\), and \(u_!\) is the colimit over \(I\), which is exact.

## 2. The left adjoint on the second total topos

**2.1. Setting.** Let \(X\) be a good topos fibred over \(I\) and \(Y\) a good one fibred over \(J\), and \(u=(u,v)\colon X\to Y\) a morphism. Let \(\mathcal O_X\) be a ring of \(\operatorname{Top}^{\mathrm o}(X)\) and \(\mathcal O_Y\) one of \(\operatorname{Top}^{\mathrm o}(Y)\) (Section 4.3 of the lesson on morphisms of fibred topoi): rings \(\mathcal O_{X,i}\) with ring maps \(\mathcal O_{X,i}\to f^{-1}\mathcal O_{X,i'}\), the module inverse images \(f^*\) being \(f^{-1}\) followed by restriction of scalars, with left adjoints \(f_!\) (Proposition 4.4 there). We are given a ring map \(\varphi\colon\mathcal O_X\to u^{-1}\mathcal O_Y\), and \(u^*M\) is \(u^{-1}M\) regarded as an \(\mathcal O_X\)-module, with levels \(u_i^*M_{v(i)}\). We assume condition (L) of the lesson on left derived functors, so that each \(u_i^*\) has a left adjoint \(u_{i!}\) (Lemma 1.2 (1) there). For an object \(j\) of \(J\), let \(I/j\) be the category of pairs \((i,f)\) with \(f\colon v(i)\to j\).

**Proposition 2.2.** The functor \(u^*\) on modules over the second total topoi has a left adjoint \(u_!\), with
\[
(u_!E)_j=\varinjlim_{(i,f)\in I/j}f_!u_{i!}E_i .
\]
Here an arrow \(g\colon(i,f)\to(i',f')\) of \(I/j\), with \(f'v(g)=f\), induces \(f_!u_{i!}E_i\to f'_!u_{i'!}E_{i'}\) from the adjoint \(g_!E_i\to E_{i'}\) of \(E_g\) and the isomorphism \(u_{i'!}g_!\cong v(g)_!u_{i!}\). For \(h\colon j\to k\), the structure map of \(u_!E\) is adjoint to the map \(h_!(u_!E)_j\to(u_!E)_k\) induced by \((i,f)\mapsto(i,hf)\). In particular:

1. for a module \(L\) on \(X^{\mathrm{dis}}\), \((u_!e^{\mathrm o}_!L)_j=\bigoplus_{(i,f)\in I/j}f_!u_{i!}L_i\);
2. if \(u\) is an \(I\)-morphism, \((u_!E)_i=u_{i!}E_i\) for every \(i\).

**Proof.** The isomorphism \(u_{i'!}g_!\cong v(g)_!u_{i!}\) is the conjugate of the isomorphism \(g^*u_{i'}^*\cong u_i^*v(g)^*\), both functors being \(u_i^{-1}g^{-1}=v(g)^{-1}u_{i'}^{-1}\) followed by restriction of scalars along the compatible ring maps. The formula defines a functor on \(I/j\), and the maps for \(h\) satisfy the conditions on composites because \(I/j\to I/k\to I/l\) is \(I/j\to I/l\). A map \(u_!E\to M\) is a family of maps \(f_!u_{i!}E_i\to M_j\), natural on \(I/j\) and compatible with the \(h\). Compatibility with \(h=f\colon v(i)\to j\) shows that the component at \((i,f)\) is \(f_!\) of the component at \((i,\mathrm{id}_{v(i)})\) followed by the map \(f_!M_{v(i)}\to M_j\) of \(M\). So the family is determined by the maps \(u_{i!}E_i\to M_{v(i)}\), adjoint to maps \(E_i\to u_i^*M_{v(i)}\), and naturality on \(I/v(i')\) at the arrows \(g\colon(i,v(g))\to(i',\mathrm{id})\) is exactly compatibility with \(E_g\) and \(M_{v(g)}\). These families are the maps \(E\to u^*M\). For (1), the left adjoint of \(e^{\mathrm o*}u^*\) is \(L\mapsto\bigoplus_iv(i)^{\mathrm o}_!u_{i!}L_i\), and \(v(i)^{\mathrm o}_!(N)_j=\bigoplus_{f\colon v(i)\to j}f_!N\) by Proposition 4.4 (b) of the lesson on morphisms of fibred topoi. For (2), \(I/i\) has the final object \((i,\mathrm{id}_i)\), and a colimit over a category with a final object is the value there. \(\square\)

## 3. The left derived functor

Call a module on \(\operatorname{Top}^{\mathrm o}(X)\) levelwise flat if all its levels are flat. We assume:

**(H\(^{\mathrm o}\))** for every object \(j\) of \(J\) and every \((i,f)\in I/j\), the functor \(f_!u_{i!}\) carries short exact sequences of flat modules to exact sequences;

**(F)** every left adjoint \(f_!\) of a module inverse image of \(X\) carries flat modules to flat modules and short exact sequences of flat modules to exact sequences.

Condition (F) holds when the transition morphisms of \(X\) are localizations, as for diagrams in a topos, since \(f_!\) is then extension by zero, and when the levels are punctual, since \(f_!\) is then an extension of scalars. Some such condition is needed for the argument below: for the morphism from the topos of sheaves on a circle to the punctual topos, \(f_!\) on abelian sheaves takes coinvariants of local systems, and the short exact sequence \(0\to\mathbb Z\to L\to\mathbb Z\to0\) of free local systems with unipotent monodromy goes to a sequence whose first map is zero.

**Theorem 3.1.** Assume (L), (H\(^{\mathrm o}\)) and (F).

1. The functor \(u_!\) has a left derived functor \(Lu_!\colon D^-(\mathcal O_X)\to D^-(\mathcal O_Y)\), computed by the bounded above complexes of modules \(e^{\mathrm o}_!P\) with \(P\) flat.
2. For a bounded above complex \(M^\bullet\) of levelwise flat modules, \(Lu_!M^\bullet\) is represented by the total complex of \(u_!\bigl((e^{\mathrm o}_!e^{\mathrm o*})^{n+1}M^m\bigr)\).
3. For \(E\in D^-(\mathcal O_X)\) and \(F\in D^+(\mathcal O_Y)\),
\[
\begin{gathered}R\operatorname{Hom}(Lu_!E,F)\\ \cong R\operatorname{Hom}(E,u^*F).\end{gathered}
\]
4. If \(u\) is an \(I\)-morphism, then \((Lu_!M)_i\cong Lu_{i!}(M_i)\) for every \(i\).

**Proof.** The proofs of Proposition 3.1 and Theorem 3.2 of the lesson on left derived functors apply, with \(e^{\mathrm o}_!\) in place of \(e_!\). The only change is the analogue of Lemma 2.1 (1) there: by Proposition 4.4 (b) of the lesson on morphisms of fibred topoi, \((e^{\mathrm o}_!L)_j=\bigoplus_{f\colon i\to j}f_!L_i\), so by (F), \(e^{\mathrm o}_!\) carries flat modules to levelwise flat modules and short exact sequences of flat modules to short exact sequences. The rows \(u_!e^{\mathrm o}_!L\) are exact for exact complexes \(L\) of flat modules by Proposition 2.2 (1) and (H\(^{\mathrm o}\)). For (4), Proposition 2.2 (2) gives \((u_!e^{\mathrm o}_!L)_i=u_{i!}(e^{\mathrm o}_!L)_i\); the levels of a complex in the class of (1) are bounded above complexes of flat modules, which compute \(Lu_{i!}\) by Theorem 3.2 (1) of the lesson on left derived functors for the single level. \(\square\)

**Remark 3.2.** As in Remark 3.3 of the lesson on left derived functors, if the functors \(f_!u_{i!}\) and the functors \(f_!\) of \(X\) are exact, the formula of Theorem 3.1 (2) holds for every bounded above complex.

## 4. Simplicial topoi and décalage

**Lemma 4.1.** Let \(\mathcal A\) be the category of modules over a ring of a topos, and \(N\) a bounded above complex of simplicial objects of \(\mathcal A\). Then \(L\varinjlim_{\Delta^{\mathrm{op}}}N\) is canonically isomorphic to the total complex of the chain complexes \(s(N^q)\), with the alternating sums of the faces as differentials.

**Proof.** For an object \(A\) of \(\mathcal A\) and \(n\geq0\), let \(h_n\otimes A\) be the simplicial object \([m]\mapsto A^{(\Delta([m],[n]))}\), the free simplicial object on \(A\) in degree \(n\). Its colimit over \(\Delta^{\mathrm{op}}\) is \(A\), since \(\Delta[n]\) is connected, and \(s(h_n\otimes A)\) is the chain complex of \(\Delta[n]\) tensored with \(A\), which is homotopy equivalent to \(A\) in degree \(0\) (Lemma 2.2 of the lesson on strict simplicial objects, \([n]\) having an initial object). So the augmentation \(s(P)\to\varinjlim P\), the projection of \(s(P)_0=P_0\) onto the colimit, is a quasi-isomorphism for every direct sum \(P\) of such objects. Evaluation at all objects \([n]\) has the left adjoint \(e_!\), with \(e_!\bigl((A_n)_n\bigr)=\bigoplus_nh_n\otimes A_n\), and the standard resolution \((e_!e^*)^{\bullet+1}N^q\to N^q\) is exact, as in Proposition 2.1 of the lesson on cohomology of total topoi. Its terms are sums of free simplicial objects. Here \(e_!\) and \(\varinjlim\circ\,e_!=\bigoplus\) are exact functors, so the argument of Proposition 3.1 and Theorem 3.2 (1) of the lesson on left derived functors, with every functor exact, shows that bounded above complexes of such sums compute \(L\varinjlim\). Let \(R\) be the total complex of these resolutions. Then
\[
\begin{gathered}s(N)\longleftarrow\operatorname{Tot}s(R)\\ \longrightarrow\operatorname{Tot}\varinjlim R=L\varinjlim N\end{gathered}
\]
are quasi-isomorphisms: the first because \(s\) is exact and the columns are resolutions, the second because it is a quasi-isomorphism on every column [Stacks, Tag 0132]. \(\square\)

Together with Theorem 2.3 of the lesson on derived colimits, which computes \(L\varinjlim_{\Delta^{\mathrm{op}}}\) by the simplicial replacement, Lemma 4.1 shows that the simplicial replacement of a simplicial module is quasi-isomorphic to its chain complex.

**Corollary 4.2.** Let \(J\) be the one-point category, and \(u\colon X\to Y\) as in Setting 2.1 with (L), (H\(^{\mathrm o}\)) and (F). Let \(\underline u_!M\) be the functor \(i\mapsto u_{i!}M_i\) on \(I\), with the maps of Proposition 2.2.

1. For a bounded above complex \(M\) of levelwise flat modules, \(Lu_!M\) is represented by \(L\varinjlim_I(\underline u_!M)\), computed by the simplicial replacement of \(\underline u_!M\).
2. If \(I=\Delta^{\mathrm{op}}\), \(Lu_!M\) is represented by the total complex of the chain complexes \(s(\underline u_!M^q)\).

**Proof.** Write \(u\) as the \(I\)-morphism \(\underline u\colon X\to Y_I\) to the constant fibred topos, followed by \(Y_I\to Y\), whose left adjoint is the colimit over \(I\) of a functor \(I\to\operatorname{Mod}(\mathcal O_Y)\), the second total topos of \(Y_I\) being the category of such functors. By Proposition 2.2 (2), \(u_!=\varinjlim_I\circ\,\underline u_!\), with \(\underline u_!M=(u_{i!}M_i)_i\). The functor \(\underline u_!\) carries the modules \(e^{\mathrm o}_!P\), \(P\) flat, to the induced diagrams \(\bigoplus_i i^{\mathrm o}_!(u_{i!}P_i)\), by Proposition 2.2 (1). Induced diagrams are colimit-acyclic (Lemma 1.1 and Section 2 of the lesson on derived colimits), and \(L\underline u_!M=\underline u_!M\) for levelwise flat \(M\) by Theorem 3.1 (4). So \(Lu_!=L\varinjlim_I\circ L\underline u_!\) [Stacks, Tag 015M], which gives (1) by Theorem 2.3 of the lesson on derived colimits, and (2) by Lemma 4.1. \(\square\)

**Definition 4.3.** For a simplicial topos \(X\), the décalage \(\operatorname{Dec}^1(X)\) has levels \(X_{n+1}=X([n]\sqcup[0])\) and morphisms \(X(\alpha\sqcup\mathrm{id}_{[0]})\): it forgets the last face. Let \(\lambda_n\colon[0]\to[n+1]\) be the inclusion of the last vertex. The morphisms \(d_n=X(\lambda_n)\colon X_{n+1}\to X_0\) form the augmentation \(d\colon\operatorname{Dec}^1(X)\to X_0\), and for a module \(M\) on \(\operatorname{Top}^{\mathrm o}(X)\), \(\operatorname{Dec}^1_+(M)\) has levels \(M_{n+1}\).

**Proposition 4.4.** Let \(X\) be a good simplicial topos with a ring \(\mathcal O_X\) of \(\operatorname{Top}^{\mathrm o}(X)\) satisfying (F), such that every \(d_{n!}\colon\operatorname{Mod}(\mathcal O_{X,n+1})\to\operatorname{Mod}(\mathcal O_{X,0})\) carries short exact sequences of flat modules to exact sequences. Then for \(M\in D^-(\operatorname{Top}^{\mathrm o}(X))\) the canonical map
\[
Ld_!\operatorname{Dec}^1_+(M)\longrightarrow M_0
\]
is an isomorphism.

**Proof.** Represent \(M\) by a bounded above complex of levelwise flat modules. By Corollary 4.2 (2), \(Ld_!\operatorname{Dec}^1_+(M)\) is represented by the chain complexes of the simplicial modules \(A_n=d_{n!}M_{n+1}\), \(n\geq0\). Let \(\Delta_1\subset\Delta\) be the subcategory of the maps preserving the last vertex, and \(\lambda^k\colon[0]\to[k]\) the last vertex. For \(\alpha\colon[k]\to[l]\) in \(\Delta_1\), the adjoint \(X(\alpha)_!M_l\to M_k\) of \(M_\alpha\colon M_l\to X(\alpha)^*M_k\), and \(X(\lambda^l)_!=X(\lambda^k)_!X(\alpha)_!\), give a map \(\Psi(\alpha)\colon X(\lambda^l)_!M_l\to X(\lambda^k)_!M_k\). This makes \(\Psi([k])=X(\lambda^k)_!M_k\) a contravariant functor on \(\Delta_1\), with \(A_n=\Psi([n+1])\) and faces \(\Psi(\delta^k)\colon A_n\to A_{n-1}\) for \(\delta^k\colon[n]\to[n+1]\), \(0\leq k\leq n\): these are the faces \(\delta^k\sqcup\mathrm{id}_{[0]}\) of \(\operatorname{Dec}^1(X)\), and they preserve the last vertex. The augmentation \(A_0\to A_{-1}=M_0\) is \(\Psi(\delta^0)\), with \(\delta^0\colon[0]\to[1]\). Put \(s=\Psi(\sigma^{n+1})\colon A_n\to A_{n+1}\), for the codegeneracy \(\sigma^{n+1}\colon[n+2]\to[n+1]\) repeating the last vertex. The identities \(\sigma^{n+1}\delta^{n+1}=\mathrm{id}\) and \(\sigma^{n+1}\delta^k=\delta^k\sigma^n\) for \(k\leq n\) give \(d_{n+1}s=\mathrm{id}\) and \(d_ks=sd_k\) for \(k\leq n\). With \(\partial=\sum_k(-1)^kd_k\) and \(h=(-1)^{n+1}s\) on \(A_n\),
\[
\begin{aligned}\partial hx&=x+(-1)^{n+1}s\,\partial x,\\ h\partial x&=(-1)^ns\,\partial x,\end{aligned}
\]
so \(\partial h+h\partial=\mathrm{id}\), also on \(A_{-1}\). The augmented chain complex is contractible, and the chain complex of \(A\) is quasi-isomorphic to \(M_0\) through the augmentation. \(\square\)

**Corollary 4.5.** Let \(T\) be a topos, \(Z\) an augmented simplicial object of \(T\) with \(Z_{-1}\) its augmentation, and \(X\) a simplicial topos whose décalage \(\operatorname{Dec}^1(X)\), augmented to \(X_0\), is isomorphic to the simplicial topos \([n]\mapsto T/Z_n\) augmented to \(T/Z_{-1}\). Let \(\mathcal O\) be a ring of \(T/Z_{-1}\). Then for \(E\in D^+(\mathcal O)\) the adjunction map \(E\to Rd_*d^*E\) is an isomorphism.

**Proof.** Represent \(E\) by a bounded below complex of injectives \(I^\bullet\). The levels of \(d^*I^q\) are restrictions of injectives along localizations, hence injective (Lemma 5.1 of the lesson on cohomology of simplicial topoi, for modules). By Theorem 2.1 of that lesson, \(Rd_*d^*E\) is represented by the double complex \(d_{n*}d_n^*I^q\cong\underline{\operatorname{Hom}}_{\mathcal O}(d_{n!}d_n^*\mathcal O,I^q)\), by the module version of the same Lemma 5.1. The adjunction map is \(\underline{\operatorname{Hom}}(-,I^\bullet)\) applied to the augmentation from the chain complex of \([n]\mapsto d_{n!}d_n^*\mathcal O\) to \(\mathcal O\). The proof of Proposition 4.4, applied to the contravariant functor \([k]\mapsto X(\lambda^k)_!X(\lambda^k)^*\mathcal O\) on \(\Delta_1\), whose maps are the counits, shows that this augmentation is a homotopy equivalence; so is its image under \(\underline{\operatorname{Hom}}(-,I^q)\), for each \(q\), and the map of total complexes is a quasi-isomorphism. \(\square\)

## 5. Exercises

**Exercise 5.1.** Let \(I\) be the category with two objects \(0,1\) and one arrow \(0\to1\), \(T\) a topos, and \(X\colon I^{\mathrm{op}}\to T\) the diagram given by a monomorphism \(X_1\to X_0\). Describe \(L_X\) and decide whether \(X\) is locally filtering. Compute \(u_!M\).

**Exercise 5.2.** In Lemma 4.1, check directly that \(\varinjlim_{\Delta^{\mathrm{op}}}N\) is the cokernel of \(d_0-d_1\colon N_1\to N_0\), and that \(H_0\) of the chain complex of \(N\) is the same cokernel.

**Exercise 5.3.** Let \(X\) be the constant simplicial topos with value the punctual topos and the ring \(\mathbb Z\), so that modules on \(\operatorname{Top}^{\mathrm o}(X)\) are simplicial abelian groups. Identify \(\operatorname{Dec}^1_+(M)\), the augmentation \(d\), and the conclusion of Proposition 4.4 with a statement about simplicial abelian groups.

## 6. Complete solutions

**5.1.** An object of \(L_X(U)\) is \((0,x)\) with \(x\in X_0(U)\) or \((1,y)\) with \(y\in X_1(U)\), and an arrow \((0,x)\to(1,y)\) exists exactly when \(x\) is the image of \(y\), and is then unique. Condition (LF1) fails for two objects \((0,x)\), \((0,x')\) with \(x\neq x'\) locally: an object receiving arrows from both is \((1,y)\) with \(y\) mapping to both, impossible, or \((0,x'')\), which receives only identities. So \(X\) is not locally filtering as soon as \(X_0\) has two sections over some object that remain distinct on every covering. To compute \(u_!M\), use the adjunction: a map \(M\to u^*E\) is a pair of maps \(a_0\colon M_0\to E|_{X_0}\) and \(a_1\colon M_1\to E|_{X_1}\) with \(a_1\circ M_f=a_0|_{X_1}\). By the adjunctions of the localizations, these are maps \(p_{0!}M_0\to E\) and \(p_{1!}M_1\to E\) whose composites with the two maps
\[
\begin{gathered}p_{0!}M_0\longleftarrow p_{1!}(M_0|_{X_1})\\ \longrightarrow p_{1!}M_1\end{gathered}
\]
agree; the first map is the counit of the localization along \(X_1\to X_0\), and the second is \(p_{1!}(M_f)\). So \(u_!M\) is the pushout of this diagram.

**5.2.** A cocone from \(N\) to an object \(C\) is a family of maps \(c_n\colon N_n\to C\) compatible with all simplicial operators. Each \(c_n\) is \(c_0\) composed with any vertex map \(N_n\to N_0\), and \(c_1=c_0d_0=c_0d_1\). Conversely, a map \(c_0\) with \(c_0d_0=c_0d_1\) defines a cocone: two vertex maps of \(N_n\), for the vertices \(i<j\), factor through the edge \(N_n\to N_1\) from \(i\) to \(j\) followed by \(d_1\) and \(d_0\), so they have the same composite with \(c_0\). So the colimit is the coequalizer of \(d_0,d_1\colon N_1\rightrightarrows N_0\), the cokernel of \(d_0-d_1\). In the chain complex, \(H_0=N_0/\operatorname{im}(d_0-d_1)\), the same cokernel.

**5.3.** Here \(\operatorname{Dec}^1_+(M)\) is the simplicial abelian group \([n]\mapsto M_{n+1}\) with the faces \(d_0,\ldots,d_n\) and the degeneracies \(s_0,\ldots,s_n\) of \(M\), augmented to \(M_0\) by \(d_0^{n+1}\). Every \(d_{n!}\) is the identity of abelian groups. Proposition 4.4 says that the chain complex of \(\operatorname{Dec}^1_+(M)\), augmented to \(M_0\), is contractible; the contraction is \((-1)^{n+1}s_{n+1}\), the degeneracy of \(M\) that \(\operatorname{Dec}^1\) forgets. This is the statement of Proposition 1.1 of the lesson on décalage for the simplicial object \(M\) of the category of abelian groups.

## Sources

The identification of the left adjoint with local inductive limits, the left adjoints on the second total topoi and their derived functors, and the décalage statements are due to Illusie, in his work on the cotangent complex and the cohomology of diagrams. Local inductive limits are due to Deligne.
