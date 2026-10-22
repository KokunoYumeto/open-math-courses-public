# Equivariant sheaves on simplicial topoi

*Written by Claude Opus 5.5 (Anthropic) on 20 October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(X\) be a simplicial topos, for instance the slices \(T/N_n\) of a topos \(T\) over the nerve of a groupoid or of a category of \(T\). An *equivariant sheaf* on \(X\) is a sheaf \(L\) on \(X_0\) with a map from its inverse image along the source map \(X_1\to X_0\) to its inverse image along the target map, subject to a unit condition and a cocycle condition on \(X_2\). For a monoid acting on an object \(Y\) of a topos, equivariant sheaves are the objects over \(Y\) with a compatible action, and for an internal category they are its internal diagrams. This lesson studies the category \(BX\) of equivariant sheaves. Two fully faithful functors, the nerves, embed \(BX\) into the two total categories of \(X\), and their images are described by a décalage condition. When \(X\) satisfies a base change condition, called being a pseudo-category, the forgetful functor from \(BX\) to sheaves on \(X_0\) has a right adjoint, coinduction, and, when the inverse images have left adjoints, also a left adjoint, induction. It follows that the modules of \(BX\) form an abelian category with enough injectives, and that the induced sheaves generate \(BX\). These are the tools from which the cohomology of \(BX\) is computed by the cohomology of the levels of \(X\).

**Prerequisites.** [*Fibred topoi and their total topoi*](fibred-topoi-and-their-total-topoi.md) and [*Morphisms of fibred topoi and modules on total topoi*](morphisms-of-fibred-topoi-and-modules-on-total-topoi.md); Proposition 3.1 of [*Cohomology of the second total topos and local systems*](cohomology-of-the-second-total-topos-and-local-systems.md); Sections 2.3–2.5 of [*Décalage, nerves and the homotopy type of a category*](decalage-nerves-and-the-homotopy-type-of-a-category.md); a functor with an exact left adjoint preserves injectives [[Stacks, Tag 015Z](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/homology.html#homology-lemma-adjoint-preserve-injectives)].

**Notation.** A simplicial topos is a topos \(X\) fibred over \(\Delta^{\mathrm{op}}\). For an increasing map \(\alpha\colon[m]\to[n]\), the corresponding morphism of topoi is \(X(\alpha)\colon X_n\to X_m\), and \(X(\beta)\circ X(\alpha)=X(\alpha\beta)\). As in the lesson on fibred topoi, the transitivity isomorphisms \(X(\beta)^*X(\alpha)^*\cong X(\alpha\beta)^*\) are not written. For \(0\leq k\leq l\leq n\), let \(v_k\colon[0]\to[n]\) be the vertex \(k\) and \(e_{kl}\colon[1]\to[n]\) the edge \(0\mapsto k\), \(1\mapsto l\); the integer \(n\) will be clear from the context. On \(X_1\) we write
\[
s=X(v_0),\qquad t=X(v_1)
\]
for the *source* and the *target* \(X_1\to X_0\), and \(\sigma\colon[1]\to[0]\) for the surjection, so that \(s\,X(\sigma)=t\,X(\sigma)=\mathrm{id}\). The faces are \(d_k=X(\delta^k)\), where \(\delta^k\colon[n-1]\to[n]\) omits \(k\); on \(X_2\), \(d_2=X(e_{01})\), \(d_0=X(e_{12})\) and \(d_1=X(e_{02})\). A sheaf on \(X_n\) means an object of \(X_n\).

## 1. Equivariant sheaves

**Definition 1.1.** An *\(X\)-structure* on a sheaf \(L\) on \(X_0\) is a morphism \(a\colon s^*L\to t^*L\) of \(X_1\) such that

1. \(X(\sigma)^*(a)=\mathrm{id}_L\);
2. on \(X_2\), as maps \(X(v_0)^*L\to X(v_2)^*L\),
\[
\begin{gathered}X(e_{12})^*(a)\circ X(e_{01})^*(a)\\=X(e_{02})^*(a).\end{gathered}
\]

An *\(X\)-sheaf*, or *equivariant sheaf*, is a pair \((L,a)\). A morphism \((L,a)\to(M,b)\) is a morphism \(u\colon L\to M\) of \(X_0\) such that \(b\circ s^*(u)=t^*(u)\circ a\). The \(X\)-sheaves form a category \(BX\), with the forgetful functor \(U\colon BX\to X_0\). Let \(B'X\) be its full subcategory of the \(X\)-sheaves whose structure \(a\) is an isomorphism.

In condition 2, \(X(e_{01})^*t^*=X(v_1)^*=X(e_{12})^*s^*\), so the composite is defined. The definition involves only \(X_0\), \(X_1\), \(X_2\) and the morphisms between them.

**Lemma 1.2.** Let \((L,a)\) be an \(X\)-sheaf. For \(k\leq l\) in \([n]\), put
\[
a_{kl}=X(e_{kl})^*(a)\colon X(v_k)^*L\to X(v_l)^*L
\]
on \(X_n\). Then \(a_{kk}=\mathrm{id}\), \(a_{lm}\circ a_{kl}=a_{km}\) for \(k\leq l\leq m\), and \(X(\beta)^*(a_{kl})=a_{\beta(k)\beta(l)}\) for every \(\beta\colon[n]\to[p]\). A morphism \(u\colon(L,a)\to(M,b)\) satisfies \(b_{kl}\circ X(v_k)^*(u)=X(v_l)^*(u)\circ a_{kl}\).

**Proof.** The relation \(X(\beta)^*X(e_{kl})^*=X(\beta e_{kl})^*\) and \(\beta e_{kl}=e_{\beta(k)\beta(l)}\) give the third assertion. Next, \(e_{kk}=v_k\sigma\), so \(a_{kk}=X(v_k)^*X(\sigma)^*(a)=\mathrm{id}\) by condition 1. For \(k\leq l\leq m\), let \(\tau\colon[2]\to[n]\) send \(0,1,2\) to \(k,l,m\). Then \(\tau e_{01}=e_{kl}\), \(\tau e_{12}=e_{lm}\) and \(\tau e_{02}=e_{km}\), and \(X(\tau)^*\) of condition 2 is the second assertion. The last assertion is \(X(e_{kl})^*\) of the condition \(b\circ s^*(u)=t^*(u)\circ a\). \(\square\)

**Remark 1.3.** If \(a\) is an isomorphism, condition 1 follows from condition 2. Indeed, for the map \(\rho\colon[2]\to[0]\), every \(\rho e_{kl}\) equals \(\sigma\). So \(X(\rho)^*\) of condition 2 says that \(X(\sigma)^*(a)\) is idempotent, and an invertible idempotent is the identity.

**Examples 1.4.** (a) If \(X\) is constant with value a topos \(T\), every \(X(\alpha)\) is the identity, and condition 1 says \(a=\mathrm{id}\). So \(BX=T\).

(b) Let \(C\) be an internal category of a topos \(T\), with objects \(C_0\), arrows \(C_1\), source \(d_1\) and target \(d_0\) (Section 2.3 of the lesson on décalage), and let \(X\) be the simplicial topos \(n\mapsto T/N_n(C)\) of its nerve (Examples 1.2 (c) of the lesson on fibred topoi). A sheaf on \(X_0\) is an object \(p\colon L\to C_0\). The inverse image \(s^*L\) is \(C_1\times_{C_0}L\), formed with the source, and \(t^*L\) is formed with the target. A morphism \(a\colon s^*L\to t^*L\) over \(C_1\) is a morphism \(C_1\times_{C_0}L\to L\), \((g,x)\mapsto g\cdot x\), with \(p(g\cdot x)\) the target of \(g\). Condition 1 says \(1\cdot x=x\). On points \((g,h)\) of \(N_2(C)\), with \(h\) composable after \(g\), condition 2 says \(h\cdot(g\cdot x)=(hg)\cdot x\). So \(BX\) is the category of objects over \(C_0\) with an action of \(C_1\), that is, of internal functors from \(C\) to \(T\), and its morphisms are the equivariant morphisms over \(C_0\). If \(C\) is a groupoid, every structure is invertible and \(BX=B'X\).

(c) For a monoid \(G\) of \(T\) acting on an object \(Y\) (Section 2.5 of the lesson on décalage), take \(C=[G,Y]\). Then \(BX\) is the category of objects \(L\to Y\) with an action of \(G\) on \(L\) for which \(L\to Y\) is equivariant. For \(Y\) the final object, \(BX\) is the category \(BG\) of \(G\)-objects of \(T\).

## 2. Nerves

**Definition 2.1.** Let \((L,a)\) be an \(X\)-sheaf. Its *nerve* \(\operatorname{ner}(L)\) is the object of \(\operatorname{Top}(X)\) with levels \(\operatorname{ner}(L)_n=X(v_n)^*L\) and, for \(\alpha\colon[m]\to[n]\), the map
\[
\begin{aligned}\operatorname{ner}(L)_\alpha=a_{\alpha(m)\,n}\colon\ &X(v_{\alpha(m)})^*L\\&\longrightarrow X(v_n)^*L,\end{aligned}
\]
where \(X(\alpha)^*\operatorname{ner}(L)_m=X(v_{\alpha(m)})^*L\). Its *second nerve* \(\operatorname{ner}^{\mathrm o}(L)\) is the object of \(\operatorname{Top}^{\mathrm o}(X)\) with levels \(\operatorname{ner}^{\mathrm o}(L)_n=X(v_0)^*L\) and maps
\[
\begin{aligned}\operatorname{ner}^{\mathrm o}(L)_\alpha=a_{0\,\alpha(0)}\colon\ &X(v_0)^*L\\&\longrightarrow X(v_{\alpha(0)})^*L .\end{aligned}
\]

In \(\operatorname{Top}(X)\), the condition on composites reads \(E_{\alpha\beta}=E_\alpha\circ X(\alpha)^*(E_\beta)\) for \(\beta\colon[p]\to[m]\); for \(\operatorname{ner}(L)\) it is \(a_{\alpha\beta(p)\,n}=a_{\alpha(m)\,n}\circ a_{\alpha\beta(p)\,\alpha(m)}\), which holds by Lemma 1.2. In \(\operatorname{Top}^{\mathrm o}(X)\) it reads \(E_{\alpha\beta}=X(\alpha)^*(E_\beta)\circ E_\alpha\), and for \(\operatorname{ner}^{\mathrm o}(L)\) it is \(a_{0\,\alpha\beta(0)}=a_{\alpha(0)\,\alpha\beta(0)}\circ a_{0\,\alpha(0)}\). The identities hold because \(a_{kk}=\mathrm{id}\). A morphism \(u\) of \(X\)-sheaves gives the morphisms \(\operatorname{ner}(u)=(X(v_n)^*u)_n\) and \(\operatorname{ner}^{\mathrm o}(u)=(X(v_0)^*u)_n\), by the last part of Lemma 1.2.

For an internal category as in Examples 1.4 (b), the level \(n\) of \(\operatorname{ner}(L)\) is the pullback of \(L\) to the strings of \(n\) arrows along their last object, and that of \(\operatorname{ner}^{\mathrm o}(L)\) along their first object.

**Proposition 2.2.**

1. \(BX\) has all colimits and finite limits, and \(U\) creates them: they are computed in \(X_0\). If \(X\) is good, \(BX\) has all limits, computed in \(X_0\). The same holds for \(B'X\).
2. The functors \(\operatorname{ner}\colon BX\to\operatorname{Top}(X)\) and \(\operatorname{ner}^{\mathrm o}\colon BX\to\operatorname{Top}^{\mathrm o}(X)\) are fully faithful and preserve colimits and finite limits, and all limits when \(X\) is good.

**Proof.** (1) Let \((L_\lambda,a_\lambda)\) be a diagram in \(BX\) and \(L=\varinjlim L_\lambda\) in \(X_0\). Since \(s^*\) and \(t^*\) preserve colimits, the \(a_\lambda\) induce a morphism \(a\colon s^*L\to t^*L\). The functors \(X(\sigma)^*\) and \(X(e_{kl})^*\) also preserve colimits, so conditions 1 and 2 for \(a\) hold after composition with the coprojections, which are jointly epimorphic; hence they hold. A family of morphisms of \(X\)-sheaves \(L_\lambda\to M\) compatible with the diagram induces \(L\to M\) in \(X_0\), and it is a morphism of \(X\)-sheaves, again because the maps \(s^*L_\lambda\to s^*L\) are jointly epimorphic. The same argument, with projections in place of coprojections, applies to finite limits, and to all limits when every inverse image has a left adjoint and so preserves limits. If all \(a_\lambda\) are invertible, so is their colimit or limit \(a\).

(2) Colimits and finite limits in the total categories are computed levelwise (Proposition 2.2 of the lesson on fibred topoi), and every \(X(v_n)^*\) preserves them. The maps \(a_{kl}\) of a colimit or limit are those induced by the \(a_{\lambda,kl}\). This gives the preservation statements. Let \(w\colon\operatorname{ner}(L)\to\operatorname{ner}(M)\) be a morphism of \(\operatorname{Top}(X)\). Compatibility with the vertex \(v_n\colon[0]\to[n]\), for which \(\operatorname{ner}(L)_{v_n}=a_{nn}=\mathrm{id}\), gives \(w_n=X(v_n)^*(w_0)\). Compatibility with \(v_0\colon[0]\to[1]\) gives \(w_1\circ a=b\circ s^*(w_0)\), that is, \(t^*(w_0)\circ a=b\circ s^*(w_0)\). So \(w_0\) is a morphism of \(X\)-sheaves and \(w=\operatorname{ner}(w_0)\). Hence \(\operatorname{ner}\) is fully faithful. For \(w\colon\operatorname{ner}^{\mathrm o}(L)\to\operatorname{ner}^{\mathrm o}(M)\), the condition for \(\alpha\) is \(X(\alpha)^*(w_m)\circ a_{0\,\alpha(0)}=b_{0\,\alpha(0)}\circ w_n\). For \(\alpha=v_0\colon[0]\to[n]\) it gives \(w_n=X(v_0)^*(w_0)\), and for \(\alpha=v_1\colon[0]\to[1]\) it gives \(t^*(w_0)\circ a=b\circ s^*(w_0)\). \(\square\)

**Proposition 2.3 (images of the nerves).**

1. An object \(E\) of \(\operatorname{Top}(X)\) is isomorphic to some \(\operatorname{ner}(L)\) if and only if \(E_\alpha\) is an isomorphism for every \(\alpha\colon[m]\to[n]\) with \(\alpha(m)=n\).
2. An object \(E\) of \(\operatorname{Top}^{\mathrm o}(X)\) is isomorphic to some \(\operatorname{ner}^{\mathrm o}(L)\) if and only if \(E_\alpha\) is an isomorphism for every \(\alpha\) with \(\alpha(0)=0\).

The maps \(\alpha\) with \(\alpha(m)=n\) are those of the form \(\alpha'\sqcup\mathrm{id}_{[0]}\), allowing \(\alpha'\colon\varnothing\to[n-1]\). So condition 1 says that the décalage \(\operatorname{Dec}^1(E)\), which forgets the last face (Definition 4.3 of the lesson on derived left adjoints), together with its augmentation to the level \(0\), is cartesian. Condition 2 says the same for \(\operatorname{Dec}_1(E)\), which forgets the first face.

**Proof.** (1) The maps \(\operatorname{ner}(L)_\alpha=a_{\alpha(m)\,n}\) with \(\alpha(m)=n\) are identities. Conversely, let \(E\) satisfy the condition. For \(\alpha\colon[m]\to[n]\) and \(\gamma\colon[l]\to[m]\), the condition on composites is \(E_{\alpha\gamma}=E_\alpha\circ X(\alpha)^*(E_\gamma)\). For a vertex \(v_k\colon[0]\to[n]\) write \(E^{(n)}_k=E_{v_k}\colon X(v_k)^*E_0\to E_n\); it is invertible for \(k=n\). Put \(L=E_0\) and
\[
a=(E^{(1)}_1)^{-1}\circ E^{(1)}_0\colon s^*L\to t^*L .
\]
For an edge \(e=e_{kn}\) of \([n]\), \(e(1)=n\), so \(E_e\) is invertible, and \(E_e\circ X(e)^*(E^{(1)}_j)=E^{(n)}_{e(j)}\). Hence
\[
\begin{gathered}X(e_{kn})^*(a)\\=(E^{(n)}_n)^{-1}\circ E^{(n)}_k .\end{gathered}
\tag{2.1}
\]
Condition 1: \(\sigma\colon[1]\to[0]\) has \(\sigma(1)=0\), so \(E_\sigma\) is invertible, and \(E_\sigma\circ X(\sigma)^*(E^{(1)}_j)=E_{\mathrm{id}}=\mathrm{id}\) for \(j=0,1\). So \(X(\sigma)^*(E^{(1)}_0)=X(\sigma)^*(E^{(1)}_1)\), and \(X(\sigma)^*(a)=\mathrm{id}\). Condition 2: by (2.1), \(X(e_{02})^*(a)=(E^{(2)}_2)^{-1}E^{(2)}_0\) and \(X(e_{12})^*(a)=(E^{(2)}_2)^{-1}E^{(2)}_1\). The edge \(e_{01}\) of \([2]\) satisfies \(E_{e_{01}}\circ X(e_{01})^*(E^{(1)}_j)=E^{(2)}_j\), so
\[
\begin{aligned}&X(e_{12})^*(a)\circ X(e_{01})^*(a)\\&\quad=(E^{(2)}_2)^{-1}E_{e_{01}}\\&\qquad\circ X(e_{01})^*\bigl(E^{(1)}_1(E^{(1)}_1)^{-1}E^{(1)}_0\bigr)\\&\quad=(E^{(2)}_2)^{-1}E^{(2)}_0=X(e_{02})^*(a).\end{aligned}
\]
Finally, the isomorphisms \(E^{(n)}_n\colon X(v_n)^*L\to E_n\) form an isomorphism \(\operatorname{ner}(L)\to E\): for \(\alpha\colon[m]\to[n]\), by (2.1) and \(E_\alpha\circ X(\alpha)^*(E^{(m)}_m)=E^{(n)}_{\alpha(m)}\),
\[
\begin{aligned}E^{(n)}_n\circ a_{\alpha(m)\,n}&=E^{(n)}_{\alpha(m)}\\&=E_\alpha\circ X(\alpha)^*(E^{(m)}_m).\end{aligned}
\]

(2) The same proof applies with the first vertex in place of the last. Write \(E^{(n)}_k=E_{v_k}\colon E_n\to X(v_k)^*E_0\), invertible for \(k=0\), and put \(a=E^{(1)}_1\circ(E^{(1)}_0)^{-1}\). For an edge \(e=e_{0k}\), \(E_e\) is invertible and \(X(e)^*(E^{(1)}_j)\circ E_e=E^{(n)}_{e(j)}\), so \(X(e_{0k})^*(a)=E^{(n)}_k(E^{(n)}_0)^{-1}\). Conditions 1 and 2 follow as in (1), now using \(X(e_{12})^*(E^{(1)}_j)\circ E_{e_{12}}=E^{(2)}_{j+1}\) on \(X_2\). The maps \(E^{(n)}_0\colon E_n\to X(v_0)^*L\) form an isomorphism \(E\to\operatorname{ner}^{\mathrm o}(L)\). \(\square\)

**Proposition 2.4 (local systems).** Let \((L,a)\) be an \(X\)-sheaf with \(a\) invertible. Then \(\operatorname{ner}(L)\) and \(\operatorname{ner}^{\mathrm o}(L)\) are cartesian, and the maps
\[
a_{0n}\colon\operatorname{ner}^{\mathrm o}(L)_n\longrightarrow\overline{\operatorname{ner}(L)}_n
\]
form an isomorphism \(\operatorname{ner}^{\mathrm o}(L)\cong\overline{\operatorname{ner}(L)}\), where the bar is the equivalence of Proposition 3.1 of the lesson on the second total topos. The nerves restrict to equivalences of \(B'X\) with the cartesian objects of \(\operatorname{Top}(X)\) and of \(\operatorname{Top}^{\mathrm o}(X)\).

**Proof.** All \(a_{kl}\) are invertible, so both nerves are cartesian. In \(\overline{\operatorname{ner}(L)}\), the map for \(\alpha\) is \((a_{\alpha(m)\,n})^{-1}\). The compatibility of the maps \(a_{0n}\) with \(\alpha\colon[m]\to[n]\) reads
\[
X(\alpha)^*(a_{0m})\circ a_{0\,\alpha(0)}=(a_{\alpha(m)\,n})^{-1}\circ a_{0n},
\]
and both sides equal \(a_{0\,\alpha(m)}\) by Lemma 1.2. A cartesian object satisfies the conditions of Proposition 2.3, and the structure \(a\) constructed there is then invertible. With Proposition 2.2 (2), this gives the equivalences. \(\square\)

## 3. Pseudo-categories

**3.1. Base change maps.** Consider a square of morphisms of topoi
\[
\begin{array}{ccc}X'&\xrightarrow{\ g\ }&X\\ \downarrow{\scriptstyle f'}&&\downarrow{\scriptstyle f}\\ Y'&\xrightarrow{\ h\ }&Y\end{array}
\]
with an isomorphism \(\theta\colon f'^*h^*\cong g^*f^*\). Its *base change map* \(c\colon h^*f_*\to f'_*g^*\) is adjoint to \(f'^*h^*f_*\cong g^*f^*f_*\to g^*\), the second map being the counit of \(f\). If \(g^*\) and \(h^*\) have left adjoints \(g_!\) and \(h_!\), its *left base change map* \(c'\colon g_!f'^*\to f^*h_!\) is adjoint to \(f'^*\to f'^*h^*h_!\cong g^*f^*h_!\), the first map being the unit of \(h\).

**Lemma 3.1.** In this situation, for \(E\) on \(Y'\) and \(F\) on \(X\), the adjunction bijections
\[
\begin{gathered}\operatorname{Hom}(f^*h_!E,F)\cong\operatorname{Hom}(E,h^*f_*F),\\ \operatorname{Hom}(g_!f'^*E,F)\cong\operatorname{Hom}(E,f'_*g^*F)\end{gathered}
\]
carry composition with \(c'_E\) to composition with \(c_F\). Hence \(c\) is an isomorphism if and only if \(c'\) is.

**Proof.** Let \(\varphi\colon f^*h_!E\to F\), with adjoint \(\varphi^\sharp=h^*f_*(\varphi)\circ h^*(\eta^f)\circ\eta^h\), where \(\eta^f\) and \(\eta^h\) are the units. We compare the maps \(f'^*E\to g^*F\) adjoint to \(\varphi\circ c'_E\) and to \(c_F\circ\varphi^\sharp\). The first is \(g^*(\varphi)\circ\theta\circ f'^*(\eta^h_E)\), by the definition of \(c'\). The second is \(g^*(\epsilon^f_F)\circ\theta\circ f'^*(\varphi^\sharp)\), by the definition of \(c\). By naturality of \(\theta\), it equals
\[
g^*\bigl(\epsilon^f_F\circ f^*f_*(\varphi)\circ f^*(\eta^f)\bigr)\circ\theta\circ f'^*(\eta^h_E),
\]
and \(\epsilon^f_F\circ f^*f_*(\varphi)\circ f^*(\eta^f)=\varphi\) by naturality of \(\epsilon^f\) and a triangle identity. So the two maps agree. Now \(c'_E\) is an isomorphism exactly when composition with it is bijective for every \(F\), and \(c_F\) exactly when composition with it is bijective for every \(E\). \(\square\)

**Definition 3.2.** A simplicial topos \(X\) is a *pseudo-category* if, for every \(n\geq1\), the base change map of the square
\[
\begin{array}{ccc}X_{n+1}&\xrightarrow{X(e_{n,n+1})}&X_1\\ \downarrow{\scriptstyle d_{n+1}}&&\downarrow{\scriptstyle s}\\ X_n&\xrightarrow{\ X(v_n)\ }&X_0\end{array}
\]
is an isomorphism \(X(v_n)^*s_*\cong d_{n+1*}X(e_{n,n+1})^*\). It is a *two-sided pseudo-category* if moreover, for every \(n\geq1\), the base change map of the square
\[
\begin{array}{ccc}X_{n+1}&\xrightarrow{\ \ d_0\ \ }&X_n\\ \downarrow{\scriptstyle X(e_{01})}&&\downarrow{\scriptstyle X(v_0)}\\ X_1&\xrightarrow{\ \ t\ \ }&X_0\end{array}
\]
is an isomorphism \(t^*X(v_0)_*\cong X(e_{01})_*d_0^*\).

The squares commute: \(s\circ X(e_{n,n+1})\) and \(X(v_n)\circ d_{n+1}\) are both \(X(v_n)\) on \(X_{n+1}\), and \(t\circ X(e_{01})\) and \(X(v_0)\circ d_0\) are both \(X(v_1)\). For \(n=1\) the two conditions coincide. Heuristically, the first condition says that an \((n+1)\)-simplex is an \(n\)-simplex together with an arrow out of its last vertex, and the second that it is an arrow into the first vertex of an \(n\)-simplex. This lesson uses only the first condition. The second is needed to compare the nerves of induced sheaves with direct images along the décalage.

**Lemma 3.3 (localizations).** Let \(T\) be a topos and \(U'=U\times_VV'\) a cartesian square of \(T\). Then the square of localization morphisms \(T/U'\to T/U\), \(T/U'\to T/V'\), \(T/U\to T/V\), \(T/V'\to T/V\) has an invertible base change map.

**Proof.** In the notation of 3.1 with \(X=T/U\), \(Y'=T/V'\), \(Y=T/V\), the left adjoints are given by composition, and \(c'\) is the canonical map \(E\times_{V'}U'\to E\times_VU\) over \(U\), for \(E\) over \(V'\). It is an isomorphism because \(U'=V'\times_VU\). By Lemma 3.1, \(c\) is an isomorphism. \(\square\)

**Proposition 3.4.** Let \(C\) be an internal category of a topos \(T\). The simplicial topos \(n\mapsto T/N_n(C)\) of its nerve is a good two-sided pseudo-category.

**Proof.** Localization morphisms have left adjoints, so \(X\) is good. By Proposition 2.4 (4) of the lesson on décalage, the map \(N_{n+1}(C)\to N_n(C)\times_{C_0}C_1\), given by \(d_{n+1}\) and the last edge, is an isomorphism; the fibre product is formed with the last vertex and the source. So the first square of Definition 3.2 is the square of localizations of a cartesian square, and Lemma 3.3 applies. By condition (2) of the same proposition, with \(a=1\), \(b=n\), \(k=0\), the map \(N_{n+1}(C)\to C_1\times_{C_0}N_n(C)\), given by the first edge and \(d_0\), is an isomorphism; the fibre product is formed with the target and the first vertex. So the second square of Definition 3.2 is also the square of localizations of a cartesian square, and Lemma 3.3 gives the second condition. \(\square\)

**Lemma 3.5.** Let \(X\) be a pseudo-category, \(n\geq0\), \(P\) a sheaf on \(X_n\) and \(Q\) a sheaf on \(X_1\). Let \(\epsilon_Q\colon s^*s_*Q\to Q\) be the counit. Then
\[
\begin{gathered}\operatorname{Hom}\bigl(P,X(v_n)^*s_*Q\bigr)\\ \longrightarrow\operatorname{Hom}\bigl(d_{n+1}^*P,X(e_{n,n+1})^*Q\bigr),\\ \varphi\longmapsto X(e_{n,n+1})^*(\epsilon_Q)\circ d_{n+1}^*(\varphi)\end{gathered}
\]
is bijective. Here \(d_{n+1}^*X(v_n)^*=X(e_{n,n+1})^*s^*\).

**Proof.** For \(n=0\), \(d_1=s\) and \(e_{01}=\mathrm{id}\), and the map is the adjunction bijection of \(s^*\) and \(s_*\). For \(n\geq1\), it is composition with the base change isomorphism followed by the adjunction bijection of \(d_{n+1}^*\) and \(d_{n+1*}\), because the adjoint of the base change map is \(X(e_{n,n+1})^*(\epsilon_Q)\). \(\square\)

**Lemma 3.6.** Let \(X\) be a good pseudo-category, and let \(\eta\colon\mathrm{id}\to t^*t_!\) be the unit of the left adjoint \(t_!\) of \(t^*\). For sheaves \(P\) and \(Q\) on \(X_1\),
\[
\begin{gathered}\operatorname{Hom}\bigl(s^*t_!P,Q\bigr)\\ \longrightarrow\operatorname{Hom}\bigl(X(e_{01})^*P,X(e_{12})^*Q\bigr),\\ \varphi\longmapsto X(e_{12})^*(\varphi)\circ X(e_{01})^*(\eta_P)\end{gathered}
\]
is bijective. Here \(X(e_{01})^*t^*=X(v_1)^*=X(e_{12})^*s^*\).

**Proof.** In the first square of Definition 3.2 for \(n=1\), \(g=X(e_{12})\), \(f'=d_2=X(e_{01})\), \(f=s\) and \(h=X(v_1)=t\). Its base change map is invertible, so by Lemma 3.1 its left base change map \(c'\colon X(e_{12})_!X(e_{01})^*\to s^*t_!\) is invertible. The map of the statement is composition with \(c'_P\) followed by the adjunction bijection of \(X(e_{12})_!\) and \(X(e_{12})^*\), because the adjoint of \(c'_P\) is \(X(e_{01})^*(\eta_P)\). \(\square\)

## 4. Coinduced sheaves

**Proposition 4.1.** Let \(X\) be a pseudo-category and \(L\) a sheaf on \(X_0\). Put \(\operatorname{coind}(L)=s_*t^*L\), and let \(\epsilon\colon s^*\operatorname{coind}(L)\to t^*L\) be the counit. There is a unique morphism \(a^{\mathrm c}\colon s^*\operatorname{coind}(L)\to t^*\operatorname{coind}(L)\) such that
\[
\begin{gathered}X(e_{12})^*(\epsilon)\circ X(e_{01})^*(a^{\mathrm c})\\ =X(e_{02})^*(\epsilon)\end{gathered}
\tag{4.1}
\]
as maps \(X(v_0)^*\operatorname{coind}(L)\to X(v_2)^*L\) on \(X_2\). The pair \((\operatorname{coind}(L),a^{\mathrm c})\) is an \(X\)-sheaf, the *coinduced sheaf* of \(L\), and \(\operatorname{coind}\) is a functor \(X_0\to BX\).

For an internal category as in Examples 1.4 (b), \(\operatorname{coind}(L)\) has, over an object \(x\), the families \((\lambda_h)\) indexed by the arrows \(h\) out of \(x\), with \(\lambda_h\) in the fibre of \(L\) over the target of \(h\). An arrow \(g\colon x\to x'\) sends \((\lambda_h)\) to \((\lambda_{h'g})_{h'}\). Identity (4.1) says that evaluating the transported family at \(h'\) is evaluating the original one at \(h'g\).

**Proof.** *Existence and uniqueness.* Apply Lemma 3.5 with \(n=1\), \(P=s^*\operatorname{coind}(L)\) and \(Q=t^*L\). Then \(X(v_1)^*s_*Q=t^*\operatorname{coind}(L)\), \(d_2^*P=X(v_0)^*\operatorname{coind}(L)\) and \(X(e_{12})^*Q=X(v_2)^*L\), and \(X(e_{02})^*(\epsilon)\) is a map between the last two.

*Condition 1.* By Lemma 3.5 with \(n=0\), a map \(\psi\colon\operatorname{coind}(L)\to\operatorname{coind}(L)\) is determined by \(\epsilon\circ s^*(\psi)\). Since \(X(\sigma)\circ s=X(v_0\sigma)\) and \(v_0\sigma=e_{00}\colon[1]\to[1]\), we have \(s^*X(\sigma)^*(a^{\mathrm c})=X(e_{00})^*(a^{\mathrm c})\). Apply \(X(\tau)^*\) to (4.1), where \(\tau\colon[2]\to[1]\) sends \(0,1,2\) to \(0,0,1\): then \(\tau e_{01}=e_{00}\) and \(\tau e_{12}=\tau e_{02}=\mathrm{id}\). This gives \(\epsilon\circ X(e_{00})^*(a^{\mathrm c})=\epsilon\), so \(X(\sigma)^*(a^{\mathrm c})=\mathrm{id}\).

*Condition 2.* Both sides of condition 2 are maps into \(X(v_2)^*\operatorname{coind}(L)\) on \(X_2\). By Lemma 3.5 with \(n=2\), such a map \(\psi\) is determined by \(X(e_{23})^*(\epsilon)\circ d_3^*(\psi)\), and \(d_3^*X(e_{kl})^*=X(e_{kl})^*\) on \(X_3\). Applying \(X(\tau)^*\) to (4.1) for the maps \(\tau\colon[2]\to[3]\) with images \(\{1,2,3\}\), \(\{0,1,3\}\) and \(\{0,2,3\}\) gives
\[
\begin{aligned}X(e_{23})^*(\epsilon)\,X(e_{12})^*(a^{\mathrm c})&=X(e_{13})^*(\epsilon),\\ X(e_{13})^*(\epsilon)\,X(e_{01})^*(a^{\mathrm c})&=X(e_{03})^*(\epsilon),\\ X(e_{23})^*(\epsilon)\,X(e_{02})^*(a^{\mathrm c})&=X(e_{03})^*(\epsilon).\end{aligned}
\]
The first two show that
\[
\begin{gathered}X(e_{23})^*(\epsilon)\circ X(e_{12})^*(a^{\mathrm c})\\ \circ X(e_{01})^*(a^{\mathrm c})=X(e_{03})^*(\epsilon),\end{gathered}
\]
and the third gives the same value for \(X(e_{02})^*(a^{\mathrm c})\). So the two sides of condition 2 agree.

*Functoriality.* For \(u\colon L\to L'\), the maps \(a'^{\mathrm c}\circ s^*\operatorname{coind}(u)\) and \(t^*\operatorname{coind}(u)\circ a^{\mathrm c}\) into \(t^*\operatorname{coind}(L')\) both have image \(X(v_2)^*(u)\circ X(e_{02})^*(\epsilon)\) under the bijection of Lemma 3.5 for \(n=1\). This follows from (4.1) for \(L\) and \(L'\) and from \(\epsilon'\circ s^*\operatorname{coind}(u)=t^*(u)\circ\epsilon\). So \(\operatorname{coind}(u)\) is a morphism of \(X\)-sheaves. \(\square\)

**Proposition 4.2 (coinduction is right adjoint to the forgetful functor).** Let \(X\) be a pseudo-category, \((M,m)\) an \(X\)-sheaf and \(L\) a sheaf on \(X_0\). The map
\[
\begin{gathered}\operatorname{Hom}_{BX}\bigl(M,\operatorname{coind}(L)\bigr)\\ \longrightarrow\operatorname{Hom}_{X_0}(M,L),\\ v\longmapsto X(\sigma)^*\bigl(\epsilon\circ s^*(v)\bigr)\end{gathered}
\]
is bijective and natural in \(M\) and \(L\). Its inverse sends \(u\colon M\to L\) to the morphism \(\tilde u\colon M\to s_*t^*L\) adjoint to \(t^*(u)\circ m\colon s^*M\to t^*L\). So \(\operatorname{coind}\) is right adjoint to \(U\), with unit \(M\to\operatorname{coind}(M)\) the adjoint of \(m\), and counit \(X(\sigma)^*(\epsilon)\colon\operatorname{coind}(L)\to L\).

**Proof.** Here \(X(\sigma)^*s^*=X(\sigma)^*t^*=\mathrm{id}\). *\(\tilde u\) is a morphism of \(X\)-sheaves.* By Lemma 3.5 with \(n=1\), it suffices to compare the images of \(a^{\mathrm c}\circ s^*(\tilde u)\) and \(t^*(\tilde u)\circ m\) under \(X(e_{12})^*(\epsilon)\circ X(e_{01})^*(-)\). We use \(\epsilon\circ s^*(\tilde u)=t^*(u)\circ m\) and \(X(e_{01})^*t^*=X(e_{12})^*s^*\). By (4.1), the first image is
\[
\begin{aligned}&X(e_{02})^*(\epsilon)\circ X(v_0)^*(\tilde u)\\&\quad=X(e_{02})^*\bigl(t^*(u)\circ m\bigr)\\&\quad=X(v_2)^*(u)\circ X(e_{02})^*(m).\end{aligned}
\]
The second is
\[
\begin{aligned}&X(e_{12})^*\bigl(\epsilon\circ s^*(\tilde u)\bigr)\circ X(e_{01})^*(m)\\&\quad=X(v_2)^*(u)\circ X(e_{12})^*(m)\\&\qquad\circ X(e_{01})^*(m),\end{aligned}
\]
which is the same by condition 2 for \(M\).

*The two maps are inverse.* First,
\[
\begin{aligned}X(\sigma)^*(\epsilon\circ s^*\tilde u)&=X(\sigma)^*(t^*(u)\circ m)\\&=u\circ X(\sigma)^*(m)=u.\end{aligned}
\]
Next let \(v\) be a morphism of \(X\)-sheaves and \(u=X(\sigma)^*(\epsilon\circ s^*v)\). We show \(\tilde u=v\) by comparing adjoints, that is, \(t^*(u)\circ m=\epsilon\circ s^*(v)\). Since \(X(\sigma)\circ t=X(v_1\sigma)\) and \(v_1\sigma=e_{11}\), \(t^*(u)=X(e_{11})^*(\epsilon\circ s^*v)\), which is \(X(e_{11})^*(\epsilon)\circ t^*(v)\). Applying \(X(\tau)^*\) to (4.1) for \(\tau\colon[2]\to[1]\) with values \(0,1,1\) gives \(X(e_{11})^*(\epsilon)\circ a^{\mathrm c}=\epsilon\). Hence
\[
\begin{aligned}t^*(u)\circ m&=X(e_{11})^*(\epsilon)\circ t^*(v)\circ m\\&=X(e_{11})^*(\epsilon)\circ a^{\mathrm c}\circ s^*(v)\\&=\epsilon\circ s^*(v).\end{aligned}
\]
Naturality is clear from the formulas. \(\square\)

## 5. Induced sheaves

**Proposition 5.1 (induced sheaves).** Let \(X\) be a good pseudo-category and \(L\) a sheaf on \(X_0\). Put \(\operatorname{ind}(L)=t_!s^*L\), and let \(\eta\colon s^*L\to t^*\operatorname{ind}(L)\) be the unit. There is a unique morphism \(b\colon s^*\operatorname{ind}(L)\to t^*\operatorname{ind}(L)\) such that
\[
\begin{gathered}X(e_{12})^*(b)\circ X(e_{01})^*(\eta)\\ =X(e_{02})^*(\eta)\end{gathered}
\tag{5.1}
\]
as maps \(X(v_0)^*L\to X(v_2)^*\operatorname{ind}(L)\) on \(X_2\). The pair \((\operatorname{ind}(L),b)\) is an \(X\)-sheaf, the *induced sheaf* of \(L\). For every \(X\)-sheaf \((M,m)\), the map
\[
\begin{gathered}\operatorname{Hom}_{BX}\bigl(\operatorname{ind}(L),M\bigr)\\ \to\operatorname{Hom}_{X_0}(L,M),\quad v\mapsto v\circ\iota_L,\end{gathered}
\]
with \(\iota_L=X(\sigma)^*(\eta)\colon L\to\operatorname{ind}(L)\), is bijective. Its inverse sends \(u\) to the map \(\tilde u\colon t_!s^*L\to M\) adjoint to \(m\circ s^*(u)\). So \(\operatorname{ind}\) is left adjoint to \(U\).

For an internal category, \(\operatorname{ind}(L)\) has, over an object \(y\), the pairs of an arrow \(h\colon x\to y\) and a point of \(L\) over \(x\); an arrow \(g\colon y\to y'\) sends \((h,\xi)\) to \((gh,\xi)\).

**Proof.** *Existence and uniqueness of \(b\).* Apply Lemma 3.6 with \(P=s^*L\) and \(Q=t^*\operatorname{ind}(L)\); then \(X(e_{01})^*P=X(v_0)^*L\), and \(X(e_{02})^*(\eta)\) is a map to \(X(e_{12})^*Q=X(v_2)^*\operatorname{ind}(L)\).

*Condition 1.* A map out of \(\operatorname{ind}(L)=t_!(s^*L)\) is determined by its composite with \(\eta\) after applying \(t^*\). Since \(X(\sigma)\circ t=X(e_{11})\), we have \(t^*X(\sigma)^*(b)=X(e_{11})^*(b)\). Applying \(X(\tau)^*\) to (5.1) for \(\tau\colon[2]\to[1]\) with values \(0,1,1\) gives \(X(e_{11})^*(b)\circ\eta=\eta\). So \(X(\sigma)^*(b)=\mathrm{id}\).

*Morphisms out of \(\operatorname{ind}(L)\).* Let \((M,m)\) be an \(X\)-sheaf and \(u\colon L\to M\). We show \(t^*(\tilde u)\circ b=m\circ s^*(\tilde u)\), using Lemma 3.6 with \(P=s^*L\) and \(Q=t^*M\). We use \(t^*(\tilde u)\circ\eta=m\circ s^*(u)\) and \(X(e_{12})^*s^*=X(e_{01})^*t^*\). By (5.1), the image of the left side is
\[
\begin{aligned}&X(v_2)^*(\tilde u)\circ X(e_{02})^*(\eta)\\&\quad=X(e_{02})^*\bigl(m\circ s^*(u)\bigr).\end{aligned}
\]
The image of the right side is
\[
\begin{aligned}&X(e_{12})^*(m)\circ X(e_{01})^*\bigl(t^*(\tilde u)\circ\eta\bigr)\\&\quad=X(e_{12})^*(m)\circ X(e_{01})^*(m)\\&\qquad\circ X(v_0)^*(u),\end{aligned}
\]
which is the same by condition 2 for \(M\).

*Condition 2.* Apply the previous step to the \(X\)-sheaf \(\operatorname{coind}(\operatorname{ind}(L))\) of Proposition 4.1 and to the map \(\psi\colon L\to s_*t^*\operatorname{ind}(L)\) adjoint to \(\eta\). It gives a map \(j=\tilde\psi\colon\operatorname{ind}(L)\to\operatorname{coind}(\operatorname{ind}(L))\) with
\[
t^*(j)\circ b=a^{\mathrm c}\circ s^*(j).
\tag{5.2}
\]
The map \(j\) has a left inverse, the counit \(r=X(\sigma)^*(\epsilon)\) of Proposition 4.2. Indeed, \(r\circ j\) is determined by \(t^*(r\circ j)\circ\eta\), which is \(X(e_{11})^*(\epsilon)\circ a^{\mathrm c}\circ s^*(\psi)\) by the definition of \(j\). As in the proof of Proposition 4.2, \(X(e_{11})^*(\epsilon)\circ a^{\mathrm c}=\epsilon\), and \(\epsilon\circ s^*(\psi)=\eta\). So \(t^*(r\circ j)\circ\eta=\eta\) and \(r\circ j=\mathrm{id}\). Hence \(j\) and all its inverse images are monomorphisms. Applying \(X(e_{01})^*\) and \(X(e_{12})^*\) to (5.2) and using condition 2 for \(a^{\mathrm c}\),
\[
\begin{aligned}&X(v_2)^*(j)\circ X(e_{12})^*(b)\\&\qquad\circ X(e_{01})^*(b)\\&\quad=X(e_{12})^*(a^{\mathrm c})\circ X(e_{01})^*(a^{\mathrm c})\\&\qquad\circ X(v_0)^*(j)\\&\quad=X(e_{02})^*(a^{\mathrm c})\circ X(v_0)^*(j)\\&\quad=X(v_2)^*(j)\circ X(e_{02})^*(b).\end{aligned}
\]
Cancelling the monomorphism \(X(v_2)^*(j)\) gives condition 2 for \(b\).

*The adjunction.* Since \(X(\sigma)^*t^*\) and \(X(\sigma)^*s^*\) are the identity,
\[
\begin{aligned}\tilde u\circ\iota_L&=X(\sigma)^*\bigl(t^*(\tilde u)\circ\eta\bigr)\\&=X(\sigma)^*(m\circ s^*u)=u.\end{aligned}
\]
Conversely let \(v\colon\operatorname{ind}(L)\to M\) be a morphism of \(X\)-sheaves and \(u=v\circ\iota_L\). Since \(X(\sigma)\circ s=X(e_{00})\), \(s^*(\iota_L)=X(e_{00})^*(\eta)\), and applying \(X(\tau)^*\) to (5.1) for \(\tau\) with values \(0,0,1\) gives \(b\circ X(e_{00})^*(\eta)=\eta\). Hence
\[
\begin{aligned}m\circ s^*(u)&=m\circ s^*(v)\circ s^*(\iota_L)\\&=t^*(v)\circ b\circ X(e_{00})^*(\eta)\\&=t^*(v)\circ\eta,\end{aligned}
\]
so \(v\) is adjoint to \(m\circ s^*(u)\), that is, \(v=\tilde u\). \(\square\)

## 6. Modules

**6.1. Rings and modules.** A *ring of \(B'X\)* is a ring \(\mathcal O_0\) of \(X_0\) with a ring isomorphism \(a_{\mathcal O}\colon s^*\mathcal O_0\to t^*\mathcal O_0\) satisfying conditions 1 and 2. By Proposition 2.4, it is the same as a cartesian ring of \(\operatorname{Top}(X)\), or of \(\operatorname{Top}^{\mathrm o}(X)\), with levels \(\mathcal O_n=X(v_n)^*\mathcal O_0\). Fix such a ring. Because it is cartesian, the module inverse image along each \(X(\alpha)\) is the inverse image of sheaves; and the module direct image is the direct image of sheaves with its module structure. An *\(\mathcal O\)-module of \(BX\)* is an \(X\)-sheaf \((M,m)\) together with an \(\mathcal O_0\)-module structure on \(M\) such that \(m\colon s^*M\to t^*M\) is linear, where \(a_{\mathcal O}\) identifies the rings of \(s^*M\) and \(t^*M\). These modules and the linear morphisms of \(X\)-sheaves form the category \(\operatorname{Mod}(BX)\), with the forgetful functor \(U\colon\operatorname{Mod}(BX)\to\operatorname{Mod}(\mathcal O_0)\).

Sections 1–5 hold for modules with the same proofs, with module categories in place of the levels, module inverse and direct images in place of those of sheaves, and the left adjoints of the module inverse images (Proposition 4.4 (a) of the lesson on morphisms of fibred topoi) in place of those of sheaves. The base change maps of modules are those of the underlying sheaves, so a pseudo-category satisfies the module version of Definition 3.2, and Lemma 3.1 holds in the module categories. In particular, the coinduced module \(\operatorname{coind}(L)=s_*t^*L\) and, for good \(X\), the induced module \(\operatorname{ind}(L)=t_!s^*L\), formed with the left adjoint of \(t^*\) on modules, are right and left adjoint to \(U\).

**Proposition 6.2.** Let \(X\) be a pseudo-category with a ring \(\mathcal O\) of \(B'X\).

1. \(\operatorname{Mod}(BX)\) is an abelian category, in which kernels, cokernels, colimits and finite limits are computed in \(\operatorname{Mod}(\mathcal O_0)\). The functor \(U\) is exact, faithful and conservative.
2. The functor \(\operatorname{coind}\) carries injective modules to injective modules. Every module of \(BX\) embeds into \(\operatorname{coind}(J)\) for an injective \(\mathcal O_0\)-module \(J\). So \(\operatorname{Mod}(BX)\) has enough injectives, and every injective module of \(BX\) is a direct summand of such a \(\operatorname{coind}(J)\).
3. If \(X\) is good, every module of \(BX\) is a quotient of \(\operatorname{ind}(P)\) for a free \(\mathcal O_0\)-module \(P\). If moreover \(t^*\colon\operatorname{Mod}(\mathcal O_0)\to\operatorname{Mod}(\mathcal O_1)\) carries injectives to injectives, then \(\operatorname{ind}\) is exact and \(U\) carries injectives to injectives.

**Proof.** (1) This is Proposition 2.2 (1) for modules: kernels and cokernels are finite limits and colimits, and \(s^*\), \(t^*\) are exact. A morphism whose image under \(U\) is invertible is invertible, its inverse being a morphism of \(X\)-sheaves.

(2) The left adjoint \(U\) of \(\operatorname{coind}\) is exact, so \(\operatorname{coind}\) preserves injectives [Stacks, Tag 015Z]. The unit \(M\to\operatorname{coind}(UM)\) is a monomorphism, because its composite with the counit \(U\operatorname{coind}(UM)\to UM\) is the identity of \(UM\). Choose a monomorphism \(UM\to J\) into an injective module; \(\operatorname{coind}\) is left exact, so \(M\to\operatorname{coind}(J)\) is a monomorphism. An injective module that embeds into \(\operatorname{coind}(J)\) is a direct summand of it.

(3) The counit \(\operatorname{ind}(UM)\to M\) is an epimorphism, because its image under \(U\) has the right inverse \(\iota_{UM}\). Choose an epimorphism \(P\to UM\) from a free module; the left adjoint \(\operatorname{ind}\) is right exact, so \(\operatorname{ind}(P)\to M\) is an epimorphism. If \(t^*\) preserves injectives, its left adjoint \(t_!\) is exact: for a monomorphism \(A\to B\) and every injective \(I\), the map
\[
\begin{gathered}\operatorname{Hom}(t_!B,I)=\operatorname{Hom}(B,t^*I)\\ \to\operatorname{Hom}(A,t^*I)=\operatorname{Hom}(t_!A,I)\end{gathered}
\]
is surjective, and \(\operatorname{Mod}(\mathcal O_0)\) has enough injectives. So \(\operatorname{ind}=t_!s^*\) is exact, and its right adjoint \(U\) preserves injectives [Stacks, Tag 015Z]. \(\square\)

**Proposition 6.3.**

1. If \(X\) is a good pseudo-category, the sheaves \(\operatorname{ind}(V)\), for \(V\) in a generating family of \(X_0\), form a generating family of \(BX\).
2. If \(X\) is a pseudo-category, \(\operatorname{ner}\colon BX\to\operatorname{Top}(X)\) has a right adjoint. If \(X\) is a good pseudo-category, \(\operatorname{ner}^{\mathrm o}\colon BX\to\operatorname{Top}^{\mathrm o}(X)\) has a right adjoint.

**Proof.** (1) Two distinct morphisms \(M\to M'\) of \(BX\) are distinct in \(X_0\), so they differ after composition with some map \(V\to M\), and by Proposition 5.1 this map comes from a morphism \(\operatorname{ind}(V)\to M\).

(2) Let \(E\) be an object of \(\operatorname{Top}(X)\). By the proof of Proposition 2.2 (2), a morphism \(w\colon\operatorname{ner}(L)\to E\) is determined by \(w_0\colon L\to E_0\), through \(w_n=E_{v_n}\circ X(v_n)^*(w_0)\). For a general \(\alpha\colon[m]\to[n]\), the compatibility of these maps with \(\alpha\) follows from the case \(\alpha=v_0\colon[0]\to[1]\) by applying \(X(e_{\alpha(m)\,n})^*\) and composing with \(E_{e_{\alpha(m)\,n}}\). So the morphisms \(\operatorname{ner}(L)\to E\) are the maps \(w_0\colon L\to E_0\) with
\[
E_{v_1}\circ t^*(w_0)\circ a=E_{v_0}\circ s^*(w_0)
\]
as maps \(s^*L\to E_1\). By Proposition 4.2, the maps \(L\to E_0\) are the morphisms \(L\to\operatorname{coind}(E_0)\) of \(BX\), and the maps \(s^*L\to E_1\) are the morphisms \(L\to\operatorname{coind}(s_*E_1)\). The two sides of the condition are natural in \(L\in BX\): for a morphism \(u\colon L'\to L\) of \(X\)-sheaves, \(t^*(u)\circ a'=a\circ s^*(u)\). By the Yoneda lemma, they are induced by two morphisms \(\operatorname{coind}(E_0)\rightrightarrows\operatorname{coind}(s_*E_1)\) of \(BX\), and their equalizer represents \(L\mapsto\operatorname{Hom}(\operatorname{ner}(L),E)\).

For \(\operatorname{ner}^{\mathrm o}\), a morphism \(\operatorname{ner}^{\mathrm o}(L)\to E\) is a family of maps \(w_n\colon X(v_0)^*L\to E_n\), that is, of maps \(L\to X(v_0)_*E_n\), with the conditions \(X(\alpha)^*(w_m)\circ a_{0\,\alpha(0)}=E_\alpha\circ w_n\) for all \(\alpha\). As above, both sides of each condition are natural in \(L\in BX\), with values in \(\operatorname{Hom}(X(v_0)^*L,X(\alpha)^*E_m)\). So the morphisms form the equalizer of two morphisms of \(BX\)
\[
\begin{aligned}&\prod_n\operatorname{coind}\bigl(X(v_0)_*E_n\bigr)\\&\quad\rightrightarrows\prod_\alpha\operatorname{coind}\bigl(X(v_0)_*X(\alpha)^*E_m\bigr),\end{aligned}
\]
which exist because \(BX\) has products when \(X\) is good (Proposition 2.2 (1)). \(\square\)

**Remark 6.4 (the classifying topos).** By Proposition 2.2 (1), \(U\) creates colimits and finite limits. So \(BX\) inherits from \(X_0\) the exactness properties of a topos: it has finite limits and small colimits, its coproducts are disjoint and stable under pullback, and its equivalence relations are effective with quotients stable under pullback. If \(X\) is a good pseudo-category, \(BX\) also has a small generating family (Proposition 6.3 (1)). Giraud's characterization of topoi [SGA 4, Exposé IV, Théorème 1.2] then shows that \(BX\) is a topos, the *classifying topos* of \(X\), and Proposition 6.3 (2) shows that \(\operatorname{ner}\) and \(\operatorname{ner}^{\mathrm o}\) are the inverse images of morphisms of topoi \(\operatorname{Top}(X)\to BX\) and \(\operatorname{Top}^{\mathrm o}(X)\to BX\). Giraud's theorem is not proved in this programme. The cohomology of \(BX\) only needs the abelian category \(\operatorname{Mod}(BX)\), its injectives (Proposition 6.2) and the adjoint functors constructed here, which do not depend on it.

## 7. Exercises

**Exercise 7.1.** Let \(G\) be a group and \(Y\) a set with a left action of \(G\), and let \(X\) be the simplicial topos of the nerve of \([G,Y]\) in the topos of sets. For a set \(L\) over \(Y\), with fibres \(L_y\), compute \(\operatorname{coind}(L)\) and \(\operatorname{ind}(L)\) with their actions. For \(Y\) a point, show that \(\operatorname{coind}(L)\) is the set of maps \(G\to L\) with \((g\cdot\varphi)(h)=\varphi(hg)\), and that \(\operatorname{ind}(L)=G\times L\) with \(g\cdot(h,\xi)=(gh,\xi)\). Check the two adjunctions directly.

**Exercise 7.2.** Let \(G\) be a monoid of a topos \(T\) acting on \(Y\), and \(X\) as in Examples 1.4 (c). By Proposition 5.1 of the lesson on fibred topoi, \(\operatorname{Top}^{\mathrm o}(X)\) is the category of simplicial objects of \(T\) over \(N(G,Y)\). Show that \(\operatorname{ner}^{\mathrm o}\) sends an \(X\)-sheaf \(p\colon L\to Y\) to \(N(G,p)\colon N(G,L)\to N(G,Y)\).

**Exercise 7.3.** Let \(X\) be the simplicial topos of the nerve of the ordered set \(\{0<1\}\), viewed as a category of the topos of sets. Show that an \(X\)-sheaf is a map of sets \(\mu\colon L_0\to L_1\), and that it lies in \(B'X\) only if \(\mu\) is bijective. Compute \(\operatorname{coind}(L)\), \(\operatorname{ind}(L)\) and the unit \(L\to\operatorname{coind}(L)\). Describe \(\operatorname{ner}(L)\) and \(\operatorname{ner}^{\mathrm o}(L)\) on the simplices of the nerve.

## 8. Complete solutions

**7.1.** Here \(X_0\) is the category of sets over \(Y\) and \(X_1\) that of sets over \(G\times Y\), with \(s(g,y)=y\) and \(t(g,y)=gy\). For a map of sets \(q\colon A\to B\), the inverse image of a family \((Q_b)\) is \((Q_{q(a)})_a\), the direct image of a family \((Q_a)\) is \(\bigl(\prod_{q(a)=b}Q_a\bigr)_b\), and its left adjoint sends \((Q_a)\) to \(\bigl(\coprod_{q(a)=b}Q_a\bigr)_b\). So \(t^*L\) has the fibre \(L_{gy}\) over \((g,y)\), and
\[
\operatorname{coind}(L)_y=\prod_{g\in G}L_{gy}.
\]
By (4.1), the arrow \((h,y)\colon y\to hy\) sends \((\lambda_g)_g\) to \((\lambda_{gh})_g\), since the composite of \((h,y)\) and \((g,hy)\) is \((gh,y)\). Likewise \(s^*L\) has the fibre \(L_y\) over \((g,y)\), and
\[
\operatorname{ind}(L)_{y'}=\coprod_{(g,y)\,:\,gy=y'}L_y ;
\]
by (5.1), the arrow \((h,y')\) sends the element \(\xi\) of the summand of \((g,y)\) to the element \(\xi\) of the summand of \((hg,y)\). For \(Y\) a point these are the stated actions on \(\operatorname{Map}(G,L)\) and \(G\times L\). A \(G\)-map \(\varphi\colon M\to\operatorname{Map}(G,L)\) satisfies \(\varphi(m)(g)=(g\cdot\varphi(m))(1)=\varphi(gm)(1)\), so it is determined by \(u=\varphi(-)(1)\colon M\to L\); conversely, every map \(u\) gives the \(G\)-map \(m\mapsto(g\mapsto u(gm))\). This is the bijection of Proposition 4.2: \(X(\sigma)^*\) restricts to the identity arrows, so \(v\mapsto X(\sigma)^*(\epsilon\circ s^*v)\) is evaluation at \(1\). A \(G\)-map \(\psi\colon G\times L\to M\) satisfies \(\psi(g,\xi)=g\cdot\psi(1,\xi)\), so it is determined by its restriction along \(\iota_L(\xi)=(1,\xi)\), and every map \(L\to M\) extends in this way.

**7.2.** By Proposition 5.1 of the lesson on fibred topoi, a map \(E_n\to X(\alpha)^*E_m\) over \(N_n(G,Y)\) is a map \(E_n\to E_m\) over \(N(G,Y)(\alpha)\). The level \(n\) of \(\operatorname{ner}^{\mathrm o}(L)\) is the fibre product of \(N_n(G,Y)=G^n\times Y\) and \(L\) over the first vertex \(y\) of \((g_1,\ldots,g_n,y)\), that is, \(G^n\times L=N_n(G,L)\), with the map induced by \(p\). For \(\alpha\colon[m]\to[n]\), the map \(a_{0\,\alpha(0)}\) transports a point \(\xi\) of \(L\) along the arrow from the vertex \(0\) to the vertex \(\alpha(0)\), whose element of \(G\) is \(g_{\alpha(0)}\cdots g_1\). So the map of \(\operatorname{ner}^{\mathrm o}(L)\) for \(\alpha\) is
\[
(g,\xi)\longmapsto\bigl(N(G)(\alpha)(g),\,g_{\alpha(0)}\cdots g_1\xi\bigr),
\]
which is the map \(N(G,L)(\alpha)\) computed in the proof of Proposition 2.8 (b) of the lesson on décalage.

**7.3.** By Examples 1.4 (b), an \(X\)-sheaf is a functor from \(\{0<1\}\) to sets, that is, sets \(L_0\), \(L_1\) and the map \(\mu\) by which the arrow \(f\colon0\to1\) acts. The structure is invertible exactly when every arrow acts bijectively, that is, when \(\mu\) is bijective. The arrows out of \(0\) are \(\mathrm{id}_0\) and \(f\), and out of \(1\) only \(\mathrm{id}_1\). So \(\operatorname{coind}(L)_0=L_0\times L_1\) and \(\operatorname{coind}(L)_1=L_1\), and \(f\) sends \((\lambda_{\mathrm{id}_0},\lambda_f)\) to \(\lambda_f\). The arrows into \(0\) and \(1\) are \(\mathrm{id}_0\), respectively \(f\) and \(\mathrm{id}_1\). So \(\operatorname{ind}(L)_0=L_0\) and \(\operatorname{ind}(L)_1=L_0\sqcup L_1\), and \(f\) is the inclusion of \(L_0\). The unit \(L\to\operatorname{coind}(L)\) sends \(\xi\in L_0\) to \((\xi,\mu(\xi))\) and is the identity on \(L_1\). The simplices of the nerve are the increasing sequences \(x_0\leq\cdots\leq x_n\) in \(\{0,1\}\). The fibre of \(\operatorname{ner}(L)\) over such a simplex is \(L_{x_n}\), and that of \(\operatorname{ner}^{\mathrm o}(L)\) is \(L_{x_0}\). The map of \(\operatorname{ner}(L)\) for \(\alpha\colon[m]\to[n]\) at a simplex \(x\) is \(\mu\) when \(x_{\alpha(m)}=0\) and \(x_n=1\), and the identity otherwise. So \(\operatorname{ner}(L)\) is cartesian only if \(\mu\) is bijective, in accordance with Proposition 2.4.

## Sources

The classifying topos of a group and the topoi \(BG/Y\) are in SGA 4, Exposé IV. Equivariant sheaves on a simplicial topos, their two nerves, pseudo-categories and the induced and coinduced sheaves in this generality are due to Illusie, in his work on the cotangent complex. Giraud's characterization of topoi is in SGA 4, Exposé IV.
