# Morphisms of fibred topoi and modules on total topoi

*Written by Claude Opus 5.5 (Anthropic) on 20 October 2026. Self-checked by the writing AI. Public domain (CC0).*

A morphism of fibred topoi changes the index category and maps each level to a level. It induces inverse images on the total topoi, levelwise. Their right adjoints, the direct images, are limits over comma categories of the index categories. Global sections of the total topos are the limit of the global sections of the levels. A ring in a total topos is a compatible family of rings on the levels, and so are its modules. Tensor products are computed levelwise, and internal Homs are computed levelwise from a cartesian source. This lesson proves these facts. They are the formal basis of the cohomology of diagrams of ringed topoi.

**Prerequisites.** [*Fibred topoi and their total topoi*](fibred-topoi-and-their-total-topoi.md); modules on ringed topoi and their inverse images [[Stacks, Tag 03D5](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-modules.html#sites-modules-section-functoriality-modules)]; tensor products and pullback [[Stacks, Tag 03EL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-modules.html#sites-modules-lemma-tensor-product-pullback)].

Notation is that of the lesson on fibred topoi. In particular, the transitivity isomorphisms of a fibred topos are not written.

## 1. Morphisms of fibred topoi

**Definition 1.1.** Let \(X\) be a topos fibred over \(I\) and \(Y\) one fibred over \(J\). A *morphism* \(m=(u,v)\colon X\to Y\) consists of a functor \(v\colon I\to J\), morphisms of topoi \(u_i\colon X_i\to Y_{v(i)}\), and isomorphisms
\[
\theta_f\colon f^*u_j^*\xrightarrow{\ \sim\ }u_i^*v(f)^*\qquad(f\colon i\to j),
\]
compatible with composites and identities through the transitivity isomorphisms of \(X\) and \(Y\). When \(I=J\) and \(v=\mathrm{id}\), \(m\) is an *\(I\)-morphism*.

**Proposition 1.2.** The functors
\[
\begin{gathered}m^*\colon\operatorname{Top}(Y)\to\operatorname{Top}(X),\\m^*(F)_i=u_i^*F_{v(i)},\\m^*(F)_f=u_i^*(F_{v(f)})\circ\theta_f,\end{gathered}
\]
\[
\begin{gathered}m^{\mathrm o*}\colon\operatorname{Top}^{\mathrm o}(Y)\to\operatorname{Top}^{\mathrm o}(X),\\m^{\mathrm o*}(G)_i=u_i^*G_{v(i)},\\m^{\mathrm o*}(G)_f=\theta_f^{-1}\circ u_i^*(G_{v(f)}),\end{gathered}
\]
are well defined and preserve colimits and finite limits.

**Proof.** The conditions on composites follow from those of \(F\) and \(G\) and the compatibility of \(\theta\) with composites. Colimits and finite limits are computed levelwise (Proposition 2.2 of the lesson on fibred topoi), and each \(u_i^*\) preserves them. \(\square\)

## 2. Direct images on the total topoi

For \(j\in J\), let \(I/j\) be the category of pairs \((i,f)\) with \(f\colon v(i)\to j\); a morphism \((i,f)\to(i',f')\) is an arrow \(g\colon i\to i'\) with \(f'\circ v(g)=f\). For \(F\in\operatorname{Top}(X)\) and such a \(g\), let
\[
f'_*u_{i'*}F_{i'}\longrightarrow f_*u_{i*}F_i
\]
be \(f'_*u_{i'*}\) applied to the adjoint \(F_{i'}\to g_*F_i\) of \(F_g\), followed by \(u_{i'*}g_*=v(g)_*u_{i*}\) (the isomorphism adjoint to \(\theta_g\)) and by \(f'_*v(g)_*=f_*\). This makes \((i,f)\mapsto f_*u_{i*}F_i\) a contravariant functor on \(I/j\) with values in \(Y_j\). Put
\[
(m_*F)_j=\varprojlim_{(i,f)\in I/j}f_*u_{i*}F_i.
\]
For \(h\colon j\to k\), the functor \((i,f)\mapsto(i,hf)\) from \(I/j\) to \(I/k\) gives a map
\[
\begin{aligned}(m_*F)_k&\longrightarrow\varprojlim_{(i,f)\in I/j}(hf)_*u_{i*}F_i\\&=h_*(m_*F)_j,\end{aligned}
\]
since \(h_*\) preserves limits. Its adjoint is \((m_*F)_h\colon h^*(m_*F)_k\to(m_*F)_j\).

**Proposition 2.1.** \(m_*\) is right adjoint to \(m^*\). Hence \((m^*,m_*)\) is a morphism of topoi \(\operatorname{Top}(X)\to\operatorname{Top}(Y)\).

**Proof.** Let \(G\in\operatorname{Top}(Y)\). A morphism \(\beta\colon m^*G\to F\) is a family \(\beta_i\colon u_i^*G_{v(i)}\to F_i\) such that \(\beta_i\circ m^*(G)_g=F_g\circ g^*(\beta_{i'})\) for every \(g\colon i\to i'\). Write \(\beta^\sharp_i\colon G_{v(i)}\to u_{i*}F_i\) for the adjoint map. For \(j\in J\) and \((i,f)\in I/j\), let \(\gamma_{j,(i,f)}\colon G_j\to f_*u_{i*}F_i\) be the adjoint of \(\beta^\sharp_i\circ G_f\colon f^*G_j\to G_{v(i)}\to u_{i*}F_i\). The compatibility of \(\beta\) with \(g\), together with \(G_{f'v(g)}=G_{v(g)}\circ v(g)^*(G_{f'})\), says that the \(\gamma_{j,(i,f)}\) form a cone over the functor defining \((m_*F)_j\). So they define \(\gamma_j\colon G_j\to(m_*F)_j\). The relation \(G_{hf}=G_f\circ f^*(G_h)\) says that the \(\gamma_j\) form a morphism \(G\to m_*F\).

Conversely, given \(\gamma\colon G\to m_*F\), let \(\beta^\sharp_i\) be the component of \(\gamma_{v(i)}\) at the object \((i,\mathrm{id}_{v(i)})\) of \(I/v(i)\). The compatibility of \(\gamma\) with the map \((m_*F)_f\), for \(f\colon v(i)\to j\), shows that \(\gamma_j\) is determined by these components, by the formula above. The cone condition at \(g\colon(i,\mathrm{id})\to(i',v(g))\) gives the compatibility of the corresponding \(\beta\) with \(g\). The two constructions are inverse to each other. By Proposition 1.2, \(m^*\) is exact, so \((m^*,m_*)\) is a morphism of topoi. \(\square\)

**Corollary 2.2.** (a) If \(J\) is the category with one object and one arrow, so that \(Y\) is a single topos, then \(m_*F=\varprojlim_{i\in I}u_{i*}F_i\). In particular, for the punctual topos,
\[
\Gamma(\operatorname{Top}(X),F)=\varprojlim_{i\in I}\Gamma(X_i,F_i).
\]
(b) If \(m\) is an \(I\)-morphism, then \((m_*F)_j=u_{j*}F_j\): direct images commute with restriction to the levels. For the constant fibred topos \(Y\) over \(I\) with value the punctual topos, \(\operatorname{Top}(Y)\) is the category of presheaves of sets on \(I\), and \(m_*F\) is the presheaf \(i\mapsto\Gamma(X_i,F_i)\).
(c) For a level \(i\), viewed as the morphism from the fibred topos over the one-point category to \(X\), one recovers \(i_*\).

**Proof.** (a) Here \(I/j=I\). (b) For an \(I\)-morphism, \(I/j\) has the final object \((j,\mathrm{id}_j)\), and the limit of a contravariant functor is its value at a final object. The description of \(\operatorname{Top}(Y)\) is Example 5.2 (c) of the lesson on fibred topoi. (c) The category \(\{i\}/j\) is the discrete set \(\operatorname{Hom}(i,j)\). \(\square\)

## 3. Direct images for the second total category

Let \(X\) and \(Y\) be good. For \(g\colon i_0\to i_1\), the *base change map*
\[
\mathrm{bc}_g\colon v(g)^*u_{i_1*}\longrightarrow u_{i_0*}g^*
\]
is the composite of the unit of \(u_{i_0}\), the isomorphism \(\theta_g^{-1}\colon u_{i_0}^*v(g)^*\to g^*u_{i_1}^*\), and the counit of \(u_{i_1}\). Its adjoint \(u_{i_0}^*v(g)^*u_{i_1*}\to g^*\) is \(g^*(\text{counit})\circ\theta_g^{-1}\).

For \(j\in J\), let \(j/I\) be the category of pairs \((i,f)\) with \(f\colon j\to v(i)\); a morphism \((i_0,f_0)\to(i_1,f_1)\) is a \(g\colon i_0\to i_1\) with \(v(g)f_0=f_1\). For \(G\in\operatorname{Top}^{\mathrm o}(X)\), let \((m^{\mathrm o}_*G)_j\) be the equalizer of the two maps
\[
\begin{aligned}&\prod_{(i,f)\in j/I}f^*u_{i*}G_i\\&\quad\rightrightarrows\prod_{g\colon(i_0,f_0)\to(i_1,f_1)}f_0^*u_{i_0*}g^*G_{i_1}.\end{aligned}
\]
The component at \(g\) of the first map is the projection to \(f_1^*u_{i_1*}G_{i_1}=f_0^*v(g)^*u_{i_1*}G_{i_1}\) followed by \(f_0^*(\mathrm{bc}_g)\). The component of the second is the projection to \(f_0^*u_{i_0*}G_{i_0}\) followed by \(f_0^*u_{i_0*}(G_g)\). For \(h\colon k\to j\), the functor \((i,f)\mapsto(i,fh)\) from \(j/I\) to \(k/I\) gives the map \((m^{\mathrm o}_*G)_h\colon(m^{\mathrm o}_*G)_k\to h^*(m^{\mathrm o}_*G)_j\). Here \(h^*\) preserves the products and the equalizer, because \(Y\) is good.

**Proposition 3.1.** If \(X\) and \(Y\) are good, \(m^{\mathrm o}_*\) is right adjoint to \(m^{\mathrm o*}\). If moreover \(\operatorname{Top}^{\mathrm o}(X)\) and \(\operatorname{Top}^{\mathrm o}(Y)\) are topoi, for example under the hypothesis of Theorem 4.3 of the lesson on fibred topoi, then \((m^{\mathrm o*},m^{\mathrm o}_*)\) is a morphism of topoi.

**Proof.** Let \(H\in\operatorname{Top}^{\mathrm o}(Y)\). A morphism \(\beta\colon m^{\mathrm o*}H\to G\) is a family \(\beta_i\colon u_i^*H_{v(i)}\to G_i\) such that, for \(g\colon i_0\to i_1\),
\[
\begin{aligned}G_g\circ\beta_{i_0}&=g^*(\beta_{i_1})\circ\theta_g^{-1}\\&\quad\circ u_{i_0}^*(H_{v(g)})\end{aligned}
\tag{3.1}
\]
as maps \(u_{i_0}^*H_{v(i_0)}\to g^*G_{i_1}\). Let \(\beta^\sharp_i\colon H_{v(i)}\to u_{i*}G_i\) be adjoint to \(\beta_i\). For \((i,f)\in j/I\), put \(\gamma_{j,(i,f)}=f^*(\beta^\sharp_i)\circ H_f\colon H_j\to f^*u_{i*}G_i\). For \(g\colon(i_0,f_0)\to(i_1,f_1)\), we have \(H_{f_1}=f_0^*(H_{v(g)})\circ H_{f_0}\). So the two maps of the equalizer agree on the family \((\gamma_{j,(i,f)})\) exactly when
\[
\begin{aligned}&\mathrm{bc}_g\circ v(g)^*(\beta^\sharp_{i_1})\circ H_{v(g)}\\&\quad=u_{i_0*}(G_g)\circ\beta^\sharp_{i_0}\\&\quad\colon H_{v(i_0)}\to u_{i_0*}g^*G_{i_1}\end{aligned}
\]
holds after applying \(f_0^*\) and composing with \(H_{f_0}\). The adjoints of the two sides of this equation are the two sides of (3.1). So \(\gamma_j\) factors through \((m^{\mathrm o}_*G)_j\), and the relation \(H_{fh}=h^*(H_f)\circ H_h\) shows that the \(\gamma_j\) form a morphism \(H\to m^{\mathrm o}_*G\). Conversely, given \(\gamma\), let \(\beta^\sharp_i\) be the component of \(\gamma_{v(i)}\) at \((i,\mathrm{id})\). The compatibility of \(\gamma\) with the transition maps shows that \(\gamma\) is recovered from these components by the formula above, and the equalizer condition at \(g\colon(i_0,\mathrm{id})\to(i_1,v(g))\) gives (3.1). The last assertion follows from Proposition 1.2. \(\square\)

**Corollary 3.2.** Suppose that every base change map \(\mathrm{bc}_g\) is an isomorphism on the \(G_{i_1}\). Then \((i,f)\mapsto f^*u_{i*}G_i\) is a covariant functor on \(j/I\), and \((m^{\mathrm o}_*G)_j=\varprojlim_{j/I}f^*u_{i*}G_i\). If moreover \(m\) is an \(I\)-morphism, then \((m^{\mathrm o}_*G)_j=u_{j*}G_j\).

**Proof.** With \(\mathrm{bc}_g\) invertible, the maps \(\mathrm{bc}_g^{-1}\circ u_{i_0*}(G_g)\) make the family a functor, and the equalizer is its limit. For an \(I\)-morphism, \(j/I\) has the initial object \((j,\mathrm{id}_j)\), and the limit of a covariant functor is its value at an initial object. \(\square\)

## 4. Rings and modules

**4.1. Rings and modules in \(\operatorname{Top}(X)\).** Inverse images preserve finite products. So a ring \(A\) of \(\operatorname{Top}(X)\) is a family of rings \(A_i\) of \(X_i\) with ring maps \(f^{-1}A_j\to A_i\), where \(f^{-1}\) denotes the inverse image of sheaves. Then \(X\), with the rings \(A_i\), is a *ringed fibred topos*. For an \(A_i\)-module \(L\) and \(f\colon k\to i\), write \(f^*L=A_k\otimes_{f^{-1}A_i}f^{-1}L\) for the inverse image of modules.

**Proposition 4.2.** (a) A left \(A\)-module \(M\) of \(\operatorname{Top}(X)\) is the same as a family of left \(A_i\)-modules \(M_i\) with \(A_i\)-linear maps \(M_f\colon f^*M_j\to M_i\) satisfying \(M_{gf}=M_f\circ f^*(M_g)\) and \(M_{\mathrm{id}}=\mathrm{id}\).
(b) The restriction \(i^*\colon\operatorname{Mod}(A)\to\operatorname{Mod}(A_i)\) has the left adjoint \(i_!\), with \(i_!(L)_j=\bigoplus_{f\colon j\to i}f^*L\).
(c) For a right \(A\)-module \(L\) and a left \(A\)-module \(M\), \(i^*(L\otimes_AM)\cong L_i\otimes_{A_i}M_i\).
(d) For left \(A\)-modules \(L,M\) there is a canonical map
\[
i^*\,\mathcal{H}om_A(L,M)\longrightarrow\mathcal{H}om_{A_i}(L_i,M_i),
\]
which is an isomorphism when \(L\) is cartesian, that is, when every \(L_f\) is an isomorphism.

**Proof.** (a) A module structure \(A\times M\to M\) in \(\operatorname{Top}(X)\) is a family of module structures \(A_i\times M_i\to M_i\), compatible with the maps \(f^{-1}M_j\to M_i\) and \(f^{-1}A_j\to A_i\). Such a compatible map \(f^{-1}M_j\to M_i\) of \(f^{-1}A_j\)-modules is the same as an \(A_i\)-linear map \(f^*M_j\to M_i\).

(b) This is the proof of Proposition 3.1 of the lesson on fibred topoi, with module inverse images and direct sums of modules.

(c) The pair \((i^*,i_*)\) is a morphism of topoi \(X_i\to\operatorname{Top}(X)\) (Theorem 4.2 there), and \(i^*A=A_i\). So it is a morphism of ringed topoi whose module inverse image is \(i^*\) itself. Inverse images of ringed topoi commute with tensor products [Stacks, Tag 03EL].

(d) For an \(A_i\)-module \(N\), the adjunctions give
\[
\begin{aligned}&\operatorname{Hom}_{A_i}\bigl(N,i^*\mathcal Hom_A(L,M)\bigr)\\&\quad=\operatorname{Hom}_A(i_!N\otimes_AL,M).\end{aligned}
\]
There is a canonical map \(i_!(N\otimes_{A_i}L_i)\to i_!N\otimes_AL\): on the summand \(f^*(N\otimes L_i)=f^*N\otimes f^*L_i\) of level \(j\), it is \(1\otimes L_f\). It induces the canonical map of (d), through the identifications
\[
\begin{aligned}&\operatorname{Hom}_A(i_!(N\otimes L_i),M)\\&\quad=\operatorname{Hom}_{A_i}(N\otimes L_i,M_i)\\&\quad=\operatorname{Hom}_{A_i}(N,\mathcal Hom_{A_i}(L_i,M_i))\end{aligned}
\]
and the Yoneda lemma. If \(L\) is cartesian, every \(L_f\) is an isomorphism, so this map is an isomorphism for every \(N\), and hence so is the map of (d). \(\square\)

**4.3. Rings and modules in \(\operatorname{Top}^{\mathrm o}(X)\).** Let \(X\) be good. A ring \(A\) of \(\operatorname{Top}^{\mathrm o}(X)\) is a family of rings \(A_i\) with ring maps \(A_i\to f^{-1}A_j\). For \(f\colon i\to j\), let \(f^*\colon\operatorname{Mod}(A_j)\to\operatorname{Mod}(A_i)\) be \(f^{-1}\) followed by restriction of scalars along \(A_i\to f^{-1}A_j\). As in Proposition 4.2 (a), a left \(A\)-module is a family of \(A_i\)-modules \(M_i\) with \(A_i\)-linear maps \(M_i\to f^*M_j\), compatible with composites.

**Proposition 4.4.** (a) The functor \(f^*\colon\operatorname{Mod}(A_j)\to\operatorname{Mod}(A_i)\) has a left adjoint \(f^A_!\), with \(f^A_!(A_i^{(E)})=A_j^{(f_!E)}\) for the free module on an object \(E\) of \(X_i\). So an \(A\)-module is the same as a family \(M_i\) with \(A_j\)-linear maps \(f^A_!M_i\to M_j\) compatible with composites.
(b) The restriction \(i^{\mathrm o*}\colon\operatorname{Mod}(A)\to\operatorname{Mod}(A_i)\) has the left adjoint \(i^{\mathrm o}_!\), with \(i^{\mathrm o}_!(L)_j=\bigoplus_{f\colon i\to j}f^A_!L\).

**Proof.** (a) For \(E\in X_i\) and an \(A_j\)-module \(M\),
\[
\begin{aligned}&\operatorname{Hom}_{A_j}(A_j^{(f_!E)},M)\\&\quad=\operatorname{Hom}_{X_j}(f_!E,M)\\&\quad=\operatorname{Hom}_{X_i}(E,f^{-1}M)\\&\quad=\operatorname{Hom}_{A_i}(A_i^{(E)},f^*M).\end{aligned}
\]
So the left adjoint is defined on free modules and on the maps between them, by Yoneda. Every \(A_i\)-module \(L\) has a presentation \(L_1\to L_0\to L\to0\) by free modules. Put \(f^A_!L=\operatorname{coker}(f^A_!L_1\to f^A_!L_0)\). Then
\[
\begin{aligned}&\operatorname{Hom}(f^A_!L,M)\\&\quad=\ker\bigl(\operatorname{Hom}(L_0,f^*M)\\&\qquad\qquad\to\operatorname{Hom}(L_1,f^*M)\bigr)\\&\quad=\operatorname{Hom}(L,f^*M).\end{aligned}
\]
So \(f^A_!L\) represents the functor \(M\mapsto\operatorname{Hom}(L,f^*M)\), and it is independent of the presentation up to unique isomorphism. (b) As in Proposition 3.1 (2) of the lesson on fibred topoi, with \(f^A_!\) in place of \(f_!\). \(\square\)

When \(\operatorname{Top}^{\mathrm o}(X)\) is a topos, \(i^{\mathrm o*}\) is the inverse image of a morphism of ringed topoi, and \(i^{\mathrm o*}(L\otimes_AM)=L_i\otimes_{A_i}M_i\) as in Proposition 4.2 (c). For example, for the constant simplicial object at the final object of a topos \(T\), \(\operatorname{Top}^{\mathrm o}\) is the category of simplicial objects of \(T\). A ring is then a simplicial ring of \(T\), and its modules are the simplicial modules.

## 5. Exercises

**Exercise 5.1.** Let \(X\) be the fibred topos over \(\{0\to1\}\) defined by a morphism of topoi \(X_0\to X_1\). Show that \(\Gamma(\operatorname{Top}(X),F)=\Gamma(X_1,F_1)\).

**Exercise 5.2.** Let \(m\) be an \(I\)-morphism such that every \(u_i\) is an equivalence of topoi. Show that \(m^*\colon\operatorname{Top}(Y)\to\operatorname{Top}(X)\) is an equivalence.

**Exercise 5.3.** Let \(X\) be the constant fibred topos over \(\{0\to1\}\) with value the category of sets, and \(A\) the constant ring \(\mathbb Z\). Let \(L=(L_0,L_1)=(0,\mathbb Z)\) and \(M=(\mathbb Z,\mathbb Z)\) with identity transition map. Show that the map of Proposition 4.2 (d) for \(i=1\) is not an isomorphism.

## 6. Complete solutions

**5.1.** By Corollary 2.2 (a), \(\Gamma(\operatorname{Top}(X),F)=\varprojlim_{i\in I}\Gamma(X_i,F_i)\), the limit of the contravariant functor with the map \(\Gamma(X_1,F_1)\to\Gamma(X_0,F_0)\) induced by \(F_f\). The object \(1\) is final in \(I=\{0\to1\}\), and the limit of a contravariant functor is its value at a final object. So the limit is \(\Gamma(X_1,F_1)\).

**5.2.** Choose quasi-inverses \(w_i^*\) of the \(u_i^*\), with isomorphisms \(u_i^*w_i^*\cong\mathrm{id}\) and \(w_i^*u_i^*\cong\mathrm{id}\). Composing \(w_i^*\theta_fw_j^*\colon w_i^*f^*u_j^*w_j^*\to w_i^*u_i^*f^*w_j^*\) with these isomorphisms gives isomorphisms \(\theta'_f\colon w_i^*f^*\to f^*w_j^*\), compatible with composites because the \(\theta_f\) are. Define \(w^*\colon\operatorname{Top}(X)\to\operatorname{Top}(Y)\) by \(w^*(E)_i=w_i^*E_i\) and \(w^*(E)_f=w_i^*(E_f)\circ\theta'^{-1}_f\), the composite \(f^*w_j^*E_j\to w_i^*f^*E_j\to w_i^*E_i\). The isomorphisms \(u_i^*w_i^*E_i\cong E_i\) and \(w_i^*u_i^*F_i\cong F_i\) are compatible with the transition maps, by the definition of \(\theta'\) and the naturality of the chosen isomorphisms. So they give isomorphisms \(m^*w^*\cong\mathrm{id}\) and \(w^*m^*\cong\mathrm{id}\), and \(m^*\) is an equivalence.

**5.3.** Here \(f^*=\mathrm{id}\), \(A_0=A_1=\mathbb Z\), and \(L_f\colon\mathbb Z\to0\). By Proposition 4.2 (d) and its proof, the level-1 value of \(\mathcal Hom_A(L,M)\) is \(\operatorname{Hom}_A(1_!(\mathbb Z)\otimes_AL,M)\), where \(1_!(\mathbb Z)=(\mathbb Z,\mathbb Z)\) with identity transition map. Then \(1_!(\mathbb Z)\otimes_AL=L\). A morphism \(L\to M\) is a pair \((u_0\colon0\to\mathbb Z,u_1\colon\mathbb Z\to\mathbb Z)\) with \(u_0\circ L_f=M_f\circ u_1\). The left side is \(0\), so \(u_1=0\). Hence the level-1 value is \(0\), while \(\operatorname{Hom}(L_1,M_1)=\mathbb Z\).

## Sources

Morphisms of fibred topoi and the inverse image on total topoi are in SGA 4, Exposé VI, introduced by Grothendieck and Verdier. The formulas for direct images on \(\operatorname{Top}^{\mathrm o}\), modules on \(\operatorname{Top}^{\mathrm o}\) and the enveloping functors \(f^A_!\) are in Illusie's work on the cotangent complex. The results on modules used here are in the Stacks project, Chapter *Modules on Sites*.
