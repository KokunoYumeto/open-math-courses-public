# Local inductive limits of derived non-additive functors without a uniform bound

*Written by Claude Opus 5.5 (Anthropic) on 23 October 2026. The question was posed by Claude while writing this course and solved by GPT-6 Astra (OpenAI) in ChatGPT's Pro mode; the solution was refereed by Claude Opus 5.5 in a separate session, and this lesson was written from it and refereed and revised by Claude Opus 5.5 in two further sessions. Public domain (CC0).*

Theorem 4.4 of [*Non-additive functors of complexes in a ringed topos*](non-additive-functors-of-complexes-in-a-ringed-topos.md) shows that the cohomology sheaves of \(LF\) commute with local inductive limits of complexes. It assumes that all complexes of the system vanish above one common degree. This lesson shows that a bound on the cohomology of each complex separately suffices, whatever the degree of \(F\). The proof truncates at every level \(b\) at once, applies the uniform theorem at each fixed \(b\), exchanges two colimits of sheaves, and only then uses that each complex stabilizes under truncation.

**Prerequisites.** [*Non-additive functors of complexes in a ringed topos*](non-additive-functors-of-complexes-in-a-ringed-topos.md): Section 1, Example 1.3, Section 2.2, Section 3 (Theorem 3.2), Lemma 4.2, Construction 4.3, Theorem 4.4 and its proof, Remark 4.5. [*Homotopy sheaves and the free abelian Whitehead theorem*](homotopy-sheaves-and-the-free-abelian-whitehead-theorem.md): Definition 5.1, Construction 5.2, Propositions 5.3, 5.4, 5.5, 5.7. From the programme lesson [*Sites and sheaves*](course:ag-etale-cohomology/sites-and-sheaves): Theorems 3.2 and 4.1.

## Conventions

The site and the categories:
- \(\mathcal C\) is a small site, \(A\) and \(B\) are sheaves of rings on it, and modules are sheaves of modules.
- \(\operatorname{Mod}(A_U)\) is the category of modules on \(\mathcal C_{/U}\).
- Complexes are cohomological, with \((Y[b])^n=Y^{n+b}\).
- \(D^-\) denotes the complexes with bounded-above cohomology.

Locally filtered systems and local systems are as in Definition 5.1 of the lesson on homotopy sheaves. A local system of complexes assigns to each \(i\in L(U)\) a complex \(X_i\) of \(A_U\)-modules. Its limit \(\varinjlim_LX_i\) is formed degreewise.

\(F\colon\operatorname{Mod}(A)\to\operatorname{Mod}(B)\) is as in Section 4 of the lesson on non-additive functors: reduced, commuting with restriction and with local inductive limits. The totalization \(\operatorname{Tot}\) in \(F(X)=\operatorname{Tot}NF\Gamma\,iX\) is the direct-sum totalization. This is the reading under which the proof of Theorem 4.4 there is valid: the diagonals of a second-quadrant double complex are infinite, and direct sums, unlike products, commute with \(\varinjlim_L\) (Proposition 5.3 of the lesson on homotopy sheaves). For fixed \(q\) put
\[
\begin{aligned}
G&=H^q\circ LF\colon\\
&\quad D^-(A_U)\to\operatorname{Mod}(B_U).
\end{aligned}
\]

## 1. The comparison map

**Lemma 1.1.** Restriction along \(V\to U\) preserves flat modules. For \(Y\in D^-(A_U)\) there is a natural isomorphism
\[
LF(Y)|_V\cong LF(Y|_V),
\]
and hence \(G(Y)|_V\cong G(Y|_V)\).

**Proof.** *Flat modules.* By Theorem 3.2 of the lesson on non-additive functors, a flat module \(M\) is \(\varinjlim_LE_i\) for a local system of finite free modules \(E_i\). Restriction carries this to a local system of finite free modules on the restricted system. Restriction also commutes with sheafification, hence with \(\varinjlim_L\). So \(M|_V\) is flat by the same theorem.

*The isomorphism.* Let \(Y'\to Y\) be a quasi-isomorphism from a bounded-above flat complex. Restriction is exact, so \(Y'|_V\to Y|_V\) is again such a resolution. The functors \(\Gamma\), \(i\), \(N\) and \(\operatorname{Tot}\) use only finite sums, kernels and direct sums, and \(F\) commutes with restriction by hypothesis. Hence \(F(Y')|_V=F(Y'|_V)\). Theorem 4.4 there then gives the isomorphism, which is natural in maps of resolutions. \(\square\)

**Definition 1.2.** Let \(X=\varinjlim_LX_i\), let \(c_i\colon X_i\to X|_U\) be the cocone maps, and assume that every \(X_i\) and \(X\) lies in \(D^-\). The maps
\[
G([c_i])\colon G(X_i)\to G(X)|_U
\]
are compatible with the arrows of \(L\) and with restriction, by functoriality and Lemma 1.1. By Proposition 5.3 of the lesson on homotopy sheaves they define
\[
\alpha^q_X\colon\varinjlim_LG(X_i)\to G(X).
\]
This map is \(B\)-linear. Indeed, \(\varinjlim_L\) commutes with the finite products that define the module operations (Proposition 5.5 there), and \(\alpha^q_X\) is linear on local representatives (Proposition 5.4 there).

**Lemma 1.3.** If every \(X_i\) vanishes in degrees \(>b\), then \(\alpha^q_X\) is an isomorphism.

**Proof.** Let \(L_b\) and \(\eta\colon L_bY\to Y\) be as in Construction 4.3 of the lesson on non-additive functors. The isomorphisms \(LF(Y)\cong F(L_bY)\) of Theorem 4.4 there are natural. They carry \(LF([f])\) to \(F(L_bf)\) for every chain map \(f\) between complexes vanishing above \(b\). So \(\alpha^q_X\) becomes the map
\[
\varinjlim_LH^qF(L_bX_i)\to H^qF(L_bX)
\]
induced by the maps \(F(L_bc_i)\).

Each functor in \(F\circ L_b\) commutes with \(\varinjlim_L\), through the map induced by the cocone:
- \(\Gamma\) and \(i\) use finite sums;
- the free module functor commutes by Proposition 5.7 (2) of the lesson on homotopy sheaves;
- \(N\) uses kernels (Proposition 5.7 (3), (4));
- \(\operatorname{Tot}\) uses direct sums (Proposition 5.3);
- \(F\) commutes by hypothesis.

Hence the maps \(F(L_bc_i)\) induce an isomorphism of complexes \(\varinjlim_LF(L_bX_i)\to F(L_bX)\). Finally, \(\varinjlim_L\) commutes with cohomology (Proposition 5.7 (4)). \(\square\)

## 2. Exchanging two colimits

**Lemma 2.1.** Let \(M_{i,b}\), for \(b\in\mathbb N\), be local systems of \(B\)-modules on \(L\), with maps \(M_{i,b}\to M_{i,b+1}\) compatible with \(L\) and with restriction. Put \(M_{i,\infty}=\varinjlim_bM_{i,b}\), a colimit in \(\operatorname{Mod}(B_U)\). The maps \(M_{i,b}\to M_{i,\infty}\to(\varinjlim_LM_{i,\infty})|_U\) induce an isomorphism
\[
\kappa\colon\varinjlim_b\varinjlim_LM_{i,b}\to\varinjlim_LM_{i,\infty}.
\]

**Proof.** Restriction commutes with colimits of sheaves, so \(i\mapsto M_{i,\infty}\) is a local system, and \(\kappa\) is defined. Let \(E\) be a \(B\)-module. By Proposition 5.3 of the lesson on homotopy sheaves and the universal property of sequential colimits, a linear map from either side to \(E\) is the same datum: maps \(M_{i,b}\to E|_U\), compatible in \(b\), in \(i\) and with restriction. Precomposition with \(\kappa\) induces this identification, naturally in \(E\). So \(\kappa\) is an isomorphism by Yoneda. \(\square\)

## 3. Good truncations

For a complex \(Y\), the good truncation \(T_bY\) is
\[
\begin{aligned}
&\cdots\to Y^{b-1}\\
&\quad\to\ker(d^b)\to0\to\cdots
\end{aligned}
\]
It comes with the inclusions \(j_b\colon T_bY\to Y\) and \(u_b\colon T_bY\to T_{b+1}Y\), which satisfy \(j_{b+1}u_b=j_b\). For a chain map \(f\colon Y\to Z\),
\[
\begin{aligned}&f j_b =j_bT_bf,\quad T_{b+1}f\,u_b\\&\quad =u_bT_bf.\end{aligned} \tag{3.1}
\]
Restriction is exact, so \(T_b(Y|_V)=(T_bY)|_V\).

**Lemma 3.1.**
1. \(H^n(j_b)\) is an isomorphism for \(n\le b\), and \(H^n(T_bY)=0\) for \(n>b\). In particular \(T_b\) preserves quasi-isomorphisms.
2. The maps \(T_bc_i\) induce an isomorphism of complexes \(\chi_b\colon\varinjlim_LT_bX_i\to T_bX\), compatible with the maps \(u_b\).

**Proof.** (1) Below degree \(b\), nothing changes. In degree \(b\), both cohomologies are \(\ker d^b/\operatorname{im}d^{b-1}\).

(2) Below degree \(b\), \(\chi_b\) is the identity of \(X^n\). In degree \(b\) it is the map \(\varinjlim_L\ker d_i^b\to\ker\varinjlim_Ld_i^b\), which is bijective by Proposition 5.7 (4) of the lesson on homotopy sheaves. The compatibility with \(u_b\) follows from (3.1). \(\square\)

**Lemma 3.2.** For \(Y\in D^-(A_U)\), the maps \(G([j_b])\) induce an isomorphism
\[
s_Y\colon\varinjlim_bG(T_bY)\to G(Y).
\]
It is natural in \(Y\) and compatible with restriction.

**Proof.** The maps \(G([j_b])\) form a cocone over the transition maps \(G([u_b])\), because \(j_{b+1}u_b=j_b\). Choose \(h\ge0\) with \(H^n(Y)=0\) for \(n>h\). For \(b\ge h\), \(j_b\) and \(u_b\) are quasi-isomorphisms by Lemma 3.1, so \(G([j_b])\) and \(G([u_b])\) are isomorphisms. A sequence that is eventually a sequence of isomorphisms has its colimit mapped isomorphically by such a cocone.

Naturality is (3.1), and the compatibility with restriction is Lemma 1.1. The integer \(h\) enters only the proof of invertibility, not the definition of \(s_Y\). \(\square\)

## 4. The theorem

**Theorem 4.1.** Let \(X=\varinjlim_LX_i\), and suppose that every \(X_i\) and \(X\) has bounded-above cohomology, with bounds that may depend on \(i\). Then for every \(q\) the map
\[
\alpha^q_X\colon\varinjlim_LH^qLF(X_i)\to H^qLF(X)
\]
is an isomorphism. No hypothesis on the degree of \(F\) is needed.

**Proof.** *Fixed \(b\).* Fix \(b\in\mathbb N\). Lemma 1.3, applied to the system \(T_bX_i\) and followed by \(G([\chi_b])\), gives an isomorphism
\[
\beta_b\colon\varinjlim_LG(T_bX_i)\to G(T_bX).
\]
On the cocone from \(G(T_bX_i)\), \(\beta_b\) is \(G([T_bc_i])\). By (3.1), the maps \(\beta_b\) commute with the transition maps \(G([u_b])\): precomposed with the cocone, both composites are \(G\) of the same chain map \(u_bT_bc_i=T_{b+1}c_i\,u_b\).

*Two routes.* Put \(P=\varinjlim_b\varinjlim_LG(T_bX_i)\). There are two maps \(P\to G(X)\):
- route (a) is \(s_X\circ\varinjlim_b\beta_b\);
- route (b) is \(\alpha^q_X\circ\varinjlim_Ls_{X_i}\circ\kappa\), where \(\kappa\) is the map of Lemma 2.1 for \(M_{i,b}=G(T_bX_i)\).

The factors are isomorphisms for the following reasons:
- \(\varinjlim_b\beta_b\), because every \(\beta_b\) is one;
- \(s_X\), by Lemma 3.2, because \(X\in D^-\);
- \(\kappa\), by Lemma 2.1;
- \(\varinjlim_Ls_{X_i}\), because each \(s_{X_i}\) is an isomorphism by Lemma 3.2 applied to the single complex \(X_i\), and the \(s_{X_i}\) form a map of local systems by naturality.

*The routes agree.* By the universal properties, it suffices to compare the two routes on the map from \(G(T_bX_i)\), restricted to \(U\). There they are \(G([j_b])G([T_bc_i])\) and \(G([c_i])G([j_b])\). These are equal by (3.1), since \(j_bT_bc_i=c_ij_b\) as chain maps \(T_bX_i\to X|_U\).

Hence \(\alpha^q_X\) is the composite of route (a) with the inverses of the other three factors of route (b), all isomorphisms. So \(\alpha^q_X\) is an isomorphism. \(\square\)

In particular, there is no counterexample, even in the punctual topos with \(L\) a directed set. No truncation degree is chosen as a function of \(i\). A common bound \(H^n(X_i)=0\) for \(n>b\) implies \(X\in D^-\), by Proposition 5.7 (4) of the lesson on homotopy sheaves, so such a bound is sufficient but not necessary.

**Corollary 4.2.** For any complex \(Y\) of \(A_U\)-modules put
\[
\widehat G(Y)=\varinjlim_bH^qLF(T_bY).
\]
1. \(\widehat G\) is a functor on \(D(A_U)\), compatible with restriction, and \(s_Y\) identifies it with \(G\) on \(D^-\).
2. For every local system of arbitrary complexes, the maps \(\widehat G([c_i])\) induce an isomorphism \(\varinjlim_L\widehat G(X_i)\to\widehat G(X)\).
3. Let \(J\) be a functor with the properties of (1) and (2) and an identification \(\theta\colon J|_{D^-}\cong G\). Then \(J\cong\widehat G\) by a unique isomorphism extending \(\theta\).

**Proof.** (1) Each \(T_b\) preserves quasi-isomorphisms (Lemma 3.1), so \(\widehat G\) inverts quasi-isomorphisms and factors through \(D(A_U)\). The identification on \(D^-\) is Lemma 3.2.

(2) The map is \((\varinjlim_b\beta_b)\circ\kappa^{-1}\), which is defined for every \(b\) without any bound on the cohomology of the \(X_i\) or of \(X\). It is the stated map by the comparison of cocones in the proof of Theorem 4.1.

(3) Regard \(b\mapsto T_bY\) as a local system over the constant locally filtered system \(\mathbb N\). Its limit is \(Y\) through the maps \(j_b\): in each degree \(n\) the terms are constant for \(b>n\). By (2) for \(J\), the maps \(J([j_b])\) give
\[
\begin{aligned}&J(Y) \cong\varinjlim_bJ(T_bY)\\&\quad \cong\varinjlim_bG(T_bY) =\widehat G(Y),\end{aligned}
\]
the middle isomorphism being \(\theta\). This isomorphism is natural by (3.1). Conversely, any isomorphism extending \(\theta\) is compatible with the maps \(J([j_b])\), so it equals this one by the universal property of the colimit. \(\square\)

## 5. The functors covered

**Proposition 5.1.** For a commutative sheaf of rings \(A\) and \(n\ge1\), the functors \(S^n_A\), \(\Lambda^n_A\), \(\Gamma^n_A\) and \(M\mapsto M^{\otimes n}\) satisfy the hypotheses on \(F\).

**Proof.** These functors are reduced. Write \(V(M)\) for the underlying sheaf of \(M\); then \(V(\varinjlim_LM_i)=\varinjlim_LV(M_i)\).

*A presentation of \(\Gamma^n_A(M)\).* It is the weight-\(n\) part of the quotient of the polynomial algebra on symbols \(x^{[k]}\), for \(k\ge1\), by the relations
\[
\begin{gathered}
x^{[k]}x^{[l]}-\tbinom{k+l}{k}x^{[k+l]},\\
(ax)^{[k]}-a^kx^{[k]},\\
(x+y)^{[k]}-\textstyle\sum_lx^{[l]}y^{[k-l]},
\end{gathered}
\]
where \(x^{[0]}=1\). So \(\Gamma^n_A(M)\) is the cokernel of a map \(A^{(R_n(M))}\to A^{(W_n(M))}\) built from finitely many module operations. Here:
- \(W_n(M)\), the weight-\(n\) monomials, is a finite coproduct of quotients of sheaves \(V(M)^r\) by finite groups;
- \(R_n(M)\), the relations times monomials of total weight \(n\), is a finite coproduct of quotients of sheaves \(V(M)^r\times V(A)\) and \(V(M)^r\).

*Commutation with \(\varinjlim_L\).* The functor \(\varinjlim_L\) commutes with each step of this presentation:
- with finite products (Proposition 5.5 of the lesson on homotopy sheaves);
- with colimits (Proposition 5.3 there);
- with free modules (Proposition 5.7 (2) there);
- with cokernels (Proposition 5.7 (4) there).

Every step also commutes with restriction.

*The other functors.* The same argument applies to \(S^n_A\) and \(M^{\otimes n}\), with the relations of multilinearity, and of commutativity for \(S^n_A\). It applies to \(\Lambda^n_A\) with the relations \(x\wedge x\wedge y_3\wedge\cdots\wedge y_n\) added. \(\square\)

**Example 5.2.** Let \(I(M)\) be the kernel of the augmentation \(A^{(V(M))}\to A\), \([m]\mapsto1\). Then \(I\) satisfies the hypotheses on \(F\), by Proposition 5.7 (2), (4) of the lesson on homotopy sheaves.

\(I\) has infinite degree. Take \(A=\mathbb Z\) on the punctual site. From \(\mathbb Z[M\oplus N]=\mathbb Z[M]\otimes\mathbb Z[N]\) and \(\mathbb Z[M]=\mathbb Z\oplus I(M)\),
\[
I\Bigl(\bigoplus_{j=1}^rM_j\Bigr)\cong\bigoplus_{\varnothing\ne S}\bigotimes_{j\in S}I(M_j).
\]
The map \(I(e_R)\) is the identity on the summands with \(S\subseteq R\) and zero on the others. So \(\varepsilon_{\{1,\dots,r\}}\) acts on the summand of \(S\) by \(\sum_{S\subseteq R}(-1)^{r-|R|}=(1-1)^{r-|S|}\). The top cross-effect is therefore \(\bigotimes_jI(M_j)\). For \(M_j=\mathbb Z\) it contains \(([1]-[0])^{\otimes r}\neq0\), because \(I(\mathbb Z)\) is free on the elements \([m]-[0]\) with \(m\neq0\). So all cross-effects are nonzero.

**Proposition 5.3.** Let \(E\colon\operatorname{Mod}(A)\to\operatorname{Mod}(B)\) commute with restriction and with local inductive limits. Put \(K=E(0)\), let \(E_{\mathrm{red}}(M)=\ker E(M\to0)\), and set \(LE=K[0]\oplus LE_{\mathrm{red}}\). Then \(LE(X)\) agrees with \(\operatorname{Tot}NE\Gamma\,iX'\) on flat resolutions \(X'\), and the conclusion of Theorem 4.1 holds for \(LE\).

**Proof.** *The splitting.* The map \((k,x)\mapsto E(0\to M)(k)+x\) is a natural isomorphism \(K\oplus E_{\mathrm{red}}(M)\to E(M)\). The functor \(E_{\mathrm{red}}\) is reduced and has the hypotheses of \(F\), because restriction and \(\varinjlim_L\) are exact.

*The constant part.* The mixed object of the constant functor \(K\) is constant, and its normalization is \(K\) in bidegree \((0,0)\). This gives the agreement with \(\operatorname{Tot}NE\Gamma\,iX'\).

*The comparison.* The constant system \(i\mapsto K|_U\) has limit \(K\). The map to \(K\) is locally surjective by (LF0) and injective on local representatives by (LF1), so it is an isomorphism (Theorem 4.1 of *Sites and sheaves*). So the comparison for \(E\) is the direct sum of the identity of \(K\) and the isomorphism of Theorem 4.1 for \(E_{\mathrm{red}}\). \(\square\)

For example, the free-module functor \(M\mapsto A^{(V(M))}\) has \(K=A\), and \(E_{\mathrm{red}}=I\) is the functor of Example 5.2.

## 6. Exercises

**Exercise 6.1.** On the punctual site, let \(X_b=\mathbb Z[-b]\) for \(b\in\mathbb N\), with zero transition maps. Show that \(\varinjlim_bX_b=0\), and that \(\varinjlim_bH^qLF(X_b)=0\), both directly and by Theorem 4.1.

**Exercise 6.2.** Let \(Y=\bigoplus_{b\ge0}\mathbb Z[-b]\). Show that \(Y\notin D^-\), that no map \(T_bY\to T_{b+1}Y\) is a quasi-isomorphism, and that \(\widehat G(Y)\) is defined.

## 7. Complete solutions

**6.1.** In degree \(n\), the system \(X_b^n\) is \(\mathbb Z\) for \(b=n\) and \(0\) otherwise, with zero maps, so the colimit is \(0\). Theorem 4.1 then gives \(\varinjlim_bH^qLF(X_b)\cong H^qLF(0)=0\), since \(F(0)=0\).

Directly, each transition map is \(LF\) of a zero map. It factors through \(LF(0)=0\), so it is zero, and the colimit of a sequence of zero maps is zero.

**6.2.** \(H^n(Y)=\mathbb Z\) for every \(n\ge0\), so \(Y\notin D^-\). The truncation \(T_bY=\bigoplus_{c\le b}\mathbb Z[-c]\) lies in \(D^-\). The map \(H^{b+1}(u_b)\) is \(0\to\mathbb Z\), so \(u_b\) is not a quasi-isomorphism. The module \(\widehat G(Y)\) is the colimit of a sequence of modules, so it is defined.

## Sources

The proposition that the cohomology of derived non-additive functors commutes with local inductive limits of complexes with bounded-above cohomology is due to Illusie, in his work on the cotangent complex. Local inductive limits and the homotopy invariance used here are Deligne's. The main argument follows a solution produced with ChatGPT (OpenAI) in October 2026 and completed here. For context, see L. Brantner and A. Mathew, *Deformation theory and partition Lie algebras*, [arXiv:1904.07352](https://arxiv.org/abs/1904.07352), Section 3.2, and J. Lurie, *Higher Algebra*, Proposition 6.1.5.4, [author's page](https://people.math.harvard.edu/~lurie/papers/HA.pdf).
