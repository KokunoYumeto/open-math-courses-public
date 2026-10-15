# Finite quotients and the comparison theorem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the first of the two statements of [Cohomological and geometric dimension](cohomological-and-geometric-dimension.md), Section 4: a two-dimensional classifying space would force every labelling of the edges by unit quaternions close to \(1\) that has product \(1\) around the chosen cycle basis to have product \(1\) around every closed path [OpenAI-EG, Theorem 3.1].

**Theorem 4.1** (comparison theorem; [OpenAI-EG, Theorem 3.1]). Let \(\Gamma\) be a residually finite group with a finite generating alphabet \(S\), and \(\mathcal D\) a finite list of words on \(S\) of value \(1\) whose chains form a \(\mathbb Z\Gamma\)-basis of the cycle module of the generator graph of \(S\), as in (4.1) of [Aligned presentations of the cycle module](aligned-presentations-of-the-cycle-module.md). If \(\Gamma\) has a classifying space of dimension at most two, there is \(\eta>0\) with the following property. Let \(a\) be a labelling of the edges of the generator graph of \(S\) over \(\Gamma\) by unit quaternions with \(|a(g,s)-1|<\eta\) for every edge \((g,s)\). If \(L(z,g)=1\) for every \(z\in\mathcal D\) and \(g\in\Gamma\), then \(L(w,g)=1\) for every word \(w\) on \(S\) of value \(1\) and every \(g\in\Gamma\).

The labels are given on the infinite graph over \(\Gamma\), and the proof cannot solve infinitely many equations directly. It solves finite systems on finite quotients of \(\Gamma\) with the localized degree, keeping the products along the distinguished relators small by the forbidden value of the previous lesson, and then passes to \(\Gamma\) by compactness of a product of copies of the unit quaternions.

- Equations on a finite quotient (Section 1).
- Solving finite systems by degree (Section 2).
- Compactness (Section 3).
- The comparison theorem (Section 4).

We use: from [Aligned presentations of the cycle module](aligned-presentations-of-the-cycle-module.md), Lemma 4.1 (the aligned presentation); from [Exact counts and a quadratic estimate](exact-counts-and-a-quadratic-estimate.md), its notation and the choices of its Section 2, Lemma 1.1, Lemma 3.1, the numbers \(C\), \(\delta\), \(\eta\) of (4.1) there, and Corollary 4.1; from [Word maps on unit quaternions and degree](word-maps-on-unit-quaternions-and-degree.md), the exponential map of Section 1, word maps (Definition 2.1), the degree and its properties (DEG) of Section 3, and Lemma 5.1 (the localized degree). Tychonoff's theorem is [Theorem 2.3 of the weak topologies lesson](course:foundations-of-von-neumann-algebras/weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian#OA-FND-WT-02).

Throughout, the hypotheses of Theorem 4.1 hold, the presentation \(\langle S,\mathcal T\mid(\rho_z)_{z\in\mathcal D},(r)_{r\in\mathcal R}\rangle\) is the aligned presentation of Lemma 4.1 of the lesson on aligned presentations, and the expressions (2.1) and (2.3), the set \(\mathcal T_0\) and the finite set \(\mathcal A\subseteq\mathcal R\) are the choices of Section 2 of the lesson on exact counts.

## 1. Equations on a finite quotient

For \(r\in\mathcal R\) and \(t\in\mathcal T\) let \(c_{r,t}\in\Lambda=\mathbb Z\Gamma\) be the coefficient of \(e_t\) in the chain \([r]\). By Lemma 4.1 (3) of the lesson on aligned presentations, the map
\[
\Phi\colon\Lambda^{(\mathcal R)}\to\Lambda^{(\mathcal T)},\qquad e_r\mapsto\sum_tc_{r,t}e_t,
\]
is an isomorphism of left \(\Lambda\)-modules. For each \(r\) only finitely many \(c_{r,t}\) are nonzero.

**Lemma 1.1** (the ordinary relators on a quotient). Let \(F\) be a finite quotient of \(\Gamma\), with quotient map \(\pi\). Then
\[
\begin{gathered}
\Phi_F\colon(\mathbb ZF)^{(\mathcal R)}\to(\mathbb ZF)^{(\mathcal T)},\\
e_r\mapsto\sum_t\pi(c_{r,t})e_t,
\end{gathered}
\]
is an isomorphism, where \(\pi\) also denotes the ring homomorphism \(\mathbb Z\Gamma\to\mathbb ZF\). In particular the vectors \(f\,\Phi_F(e_r)\), \((f,r)\in F\times\mathcal R\), are linearly independent over \(\mathbb Q\) in the rational vector space with basis \(F\times\mathcal T\).

*Proof.* Let \(\Psi(e_t)=\sum_rd_{t,r}e_r\) be the inverse of \(\Phi\); again only finitely many \(d_{t,r}\) are nonzero for each \(t\). The identities \(\Psi\Phi=1\) and \(\Phi\Psi=1\) read \(\sum_tc_{r,t}d_{t,r'}=[r=r']\) and \(\sum_rd_{t,r}c_{r,t'}=[t=t']\), all sums finite. Applying the ring homomorphism \(\pi\) gives the same identities for \(\pi(c_{r,t})\) and \(\pi(d_{t,r})\), so \(e_t\mapsto\sum_r\pi(d_{t,r})e_r\) is inverse to \(\Phi_F\). The vectors \(fe_r\) form a \(\mathbb Z\)-basis of \((\mathbb ZF)^{(\mathcal R)}\), so their images under the injective map \(\Phi_F\) are linearly independent over \(\mathbb Z\), and hence over \(\mathbb Q\). \(\square\)

On the generator graph over \(F\) the edges of the letters of \(\mathcal T\) are loops. Fix the labels of the \(S\)-edges and regard the labels \(x_{g,t}=\ell(g,t)\) of the \(\mathcal T\)-edges as unknowns. For \(r\in\mathcal R\) and \(f\in F\), the equation \(L(r,f)=1\) is then an equation "a word in the unknowns and their inverses, with coefficients in \(H\), equals \(1\)": the path that reads \(r\) from \(f\) is determined by the values of the letters, every occurrence of a letter \(t\in\mathcal T\) traverses the loop \((g,t)\) at the current vertex \(g\), and every occurrence of a letter of \(S\) contributes a fixed coefficient.

**Lemma 1.2** (exponent sums). The total exponent of the unknown \(x_{g,t}\) in the equation \(L(r,f)=1\) is the coefficient of \(ge_t\) in \(f\,\Phi_F(e_r)\).

*Proof.* The path that reads \(r\) from \(1\) in the generator graph over \(\Gamma\) traverses the loop \((\gamma,t)\) with signed multiplicity equal to the coefficient of \(\gamma\) in \(c_{r,t}\), by the definition of the chain. The path that reads \(r\) from \(f\) in the graph over \(F\) is its image under \(\gamma\mapsto f\pi(\gamma)\) on vertices, so the signed multiplicity of the loop \((g,t)\) is the sum of these coefficients over the \(\gamma\) with \(f\pi(\gamma)=g\), which is the coefficient of \(ge_t\) in \(f\sum_{t'}\pi(c_{r,t'})e_{t'}\). A forward traversal contributes \(x_{g,t}\) and a backward one \(x_{g,t}^{-1}\). \(\square\)

## 2. Solving finite systems by degree

**Lemma 2.1** (finite systems; [OpenAI-EG, Lemma 3.5]). Let \(F\) be a finite quotient of \(\Gamma\), prescribe labels \(\ell(f,s)\) of the \(S\)-edges of the generator graph over \(F\) with \(|\ell(f,s)-1|<\eta\), and let \(\mathcal B\subseteq\mathcal R\) be a finite set containing \(\mathcal A\). Then there are labels of the \(\mathcal T\)-edges such that
\[
\begin{gathered}
L(r,v)=1\quad(r\in\mathcal B,\ v\in F),\\
\max_{z\in\mathcal D,\ v\in F}|L(\rho_z,v)-1|<\delta ,
\end{gathered}
\]
the maximum being \(0\) if \(\mathcal D\) is empty.

*Proof.* *Selecting unknowns.* Let \(m=|F|\,|\mathcal B|\). By Lemmas 1.1 and 1.2, the \(m\) equations \(L(r,v)=1\), \((v,r)\in F\times\mathcal B\), have exponent-sum vectors that are linearly independent over \(\mathbb Q\). They involve only finitely many unknowns, so the matrix of these vectors, restricted to the columns of the unknowns that occur, has rank \(m\), and we can choose \(m\) unknowns whose columns form a nonsingular \(m\times m\) integer matrix \(B\). All the other \(\mathcal T\)-labels are set equal to \(1\).

*Moving the coefficients.* Each prescribed label is \(\ell(f,s)=\exp(w_{f,s})\) with \(w_{f,s}\in\operatorname{Im}\mathbb H\), \(|w_{f,s}|<\pi\), since \(\ell(f,s)\ne-1\). For \(\tau\in[0,1]\) put \(\ell_\tau(f,s)=\exp(\tau w_{f,s})\). Since \(|\exp(w)-1|=2\sin(|w|/2)\) for \(|w|<\pi\), we have \(|\ell_\tau(f,s)-1|\le|\ell(f,s)-1|<\eta\) for all \(\tau\) (Exercise 5.3). Let \(f_\tau\colon H^m\to H^m\) send the selected unknowns \(x\in H^m\) to the \(m\) products \(L(r,v)\), \((v,r)\in F\times\mathcal B\), computed with the \(S\)-labels \(\ell_\tau\), the selected \(\mathcal T\)-labels \(x\) and all other \(\mathcal T\)-labels \(1\). It depends continuously on \((\tau,x)\) and is smooth in \(x\). Let
\[
\begin{gathered}
h(\tau,x)=\max_{z\in\mathcal D,\ v\in F}|L(\rho_z,v)-1|,\\
\mathcal O_\tau=\{x\in H^m:h(\tau,x)<\delta\},
\end{gathered}
\]
computed with the same labels. Finitely many products occur, so \(h\) is continuous.

*Roots avoid the value \(\delta\).* If \(f_\tau(x)=\mathbf 1\), all equations \(L(r,v)=1\) with \(r\in\mathcal B\supseteq\mathcal A\) hold, and all \(S\)-labels are within \(\epsilon<\eta\) of \(1\), where \(\epsilon\) is the largest of the finitely many distances. By Corollary 4.1 of the lesson on exact counts,
\[
\begin{aligned}
&f_\tau(x)=\mathbf 1\\
&\quad\Longrightarrow\ h(\tau,x)\ne\delta .
\end{aligned}\tag{2.1}
\]

*The case \(m=0\).* Then \(\mathcal B\) is empty, there are no unknowns, all \(\mathcal T\)-labels are \(1\), and \(h(\tau)\) is a continuous function of \(\tau\) alone, never equal to \(\delta\) by (2.1). At \(\tau=0\) all labels are \(1\) and \(h(0)=0\). By the intermediate value theorem \(h(1)<\delta\), which is the assertion. From now on \(m\ge1\).

*The degree is constant in \(\tau\).* The boundary of \(\mathcal O_\tau\) lies in \(\{h(\tau,\cdot)=\delta\}\), so by (2.1) it contains no root of \(f_\tau\), and \(\deg(f_\tau,\mathcal O_\tau,\mathbf 1)\) is defined. Fix \(\tau_0\). By (2.1) the roots of \(f_{\tau_0}\) in \(\mathcal O_{\tau_0}\) are the roots with \(h(\tau_0,x)\le\delta\), a compact set \(K_0\). Choose an open set \(V\supseteq K_0\) with \(\overline V\subseteq\mathcal O_{\tau_0}\) (if \(K_0=\varnothing\), take \(V=\varnothing\)). By compactness of \(\overline V\) and uniform continuity of \(h\), there is \(\gamma>0\) such that for \(|\tau-\tau_0|<\gamma\):

- \(\overline V\subseteq\mathcal O_\tau\);
- every root \(x\) of \(f_\tau\) with \(h(\tau,x)<\delta\) lies in \(V\): otherwise there are \(\tau_n\to\tau_0\) and such roots \(x_n\notin V\), a subsequence converges to a root \(x\) of \(f_{\tau_0}\) with \(h(\tau_0,x)\le\delta\), so \(x\in K_0\subseteq V\) and \(x_n\in V\) for large \(n\), a contradiction;
- \(f_\tau\) has no root on \(\partial V\): otherwise a limit of such roots would be a root of \(f_{\tau_0}\) on \(\partial V\subseteq\overline V\subseteq\mathcal O_{\tau_0}\), hence in \(K_0\subseteq V\), which is disjoint from \(\partial V\).

For these \(\tau\), excision (DEG 2) gives \(\deg(f_\tau,\mathcal O_\tau,\mathbf 1)=\deg(f_\tau,V,\mathbf 1)\), and homotopy invariance (DEG 3) on the interval \(|\tau-\tau_0|<\gamma\) gives \(\deg(f_\tau,V,\mathbf 1)=\deg(f_{\tau_0},V,\mathbf 1)\). So the degree is locally constant in \(\tau\), hence constant on \([0,1]\).

*The degree at \(\tau=0\).* All labels other than the unknowns are \(1\), so \(f_0\) is a word map in the sense of Definition 2.1 of the lesson on word maps, with exponent-sum matrix \(B\) by Lemma 1.2, and \(\det B\ne0\). Simultaneous conjugation of the unknowns by \(g\in H\) conjugates every product \(L(\rho_z,v)\) by \(g\), so \(h(0,\cdot)\) and \(\mathcal O_0\) are invariant, by \(|gag^{-1}-1|=|a-1|\). The set \(\mathcal O_0\) contains \(\mathbf 1\), where \(h=0\), and its boundary contains no root. By Lemma 5.1 of the lesson on word maps, \(\deg(f_0,\mathcal O_0,\mathbf 1)\ne0\).

So \(\deg(f_1,\mathcal O_1,\mathbf 1)\ne0\), and by (DEG 1) \(f_1\) has a root \(x\in\mathcal O_1\). With the selected labels \(x\) and the other \(\mathcal T\)-labels \(1\), all equations of \(\mathcal B\) hold and \(h(1,x)<\delta\). \(\square\)

## 3. Compactness

A family of closed subsets of a topological space has the *finite intersection property* if every finite subfamily has nonempty intersection. In a compact space such a family has nonempty intersection: otherwise the complements would form an open cover without a finite subcover.

The unit quaternions \(H\) form a closed and bounded subset of \(\mathbb R^4\), hence a compact space. For any set \(I\), the product \(H^I\) is compact in the product topology by Tychonoff's theorem. The set \(I\) may be uncountable; this matters here, since the aligned presentation may have uncountably many letters.

## 4. The comparison theorem

*Proof of Theorem 4.1.* Let \(\eta\) be the number fixed in (4.1) of the lesson on exact counts, and let \(a\) be a labelling as in the theorem. Consider the compact space \(\mathscr P=H^{\Gamma\times\mathcal T}\) of all labellings of the \(\mathcal T\)-edges of the generator graph over \(\Gamma\); together with \(a\) on the \(S\)-edges, every point of \(\mathscr P\) is a labelling of the generator graph of \(A=S\amalg\mathcal T\). Consider the conditions
\[
\begin{aligned}
&L(r,g)=1\\
&\qquad(r\in\mathcal R,\ g\in\Gamma),\\
&|L(\rho_z,g)-1|\le\delta\\
&\qquad(z\in\mathcal D,\ g\in\Gamma).
\end{aligned}\tag{4.1}
\]
Each condition involves the labels of the finitely many edges traversed by one path, and the product along the path is a continuous function of these labels, so each condition defines a closed subset of \(\mathscr P\).

*The finite intersection property.* Let \(\mathscr C\) be a finite set of conditions (4.1). Let \(P\subseteq\Gamma\) be the finite set of the starting points \(g\) of the \(S\)-edges \((g,s)\) traversed, forwards or backwards, by the paths of the conditions in \(\mathscr C\), and let \(\mathcal B\subseteq\mathcal R\) be the union of \(\mathcal A\) and the ordinary relators occurring in \(\mathscr C\). Since \(\Gamma\) is residually finite, for each of the finitely many pairs \(p\ne p'\) in \(P\) there is a normal subgroup of finite index not containing \(p^{-1}p'\); the intersection \(N\) of these subgroups has finite index, and the quotient map \(\pi\colon\Gamma\to F=\Gamma/N\) is injective on \(P\). Label the \(S\)-edges of the graph over \(F\): the edge \((\pi(g),s)\) gets the label \(a(g,s)\) if \((g,s)\) is traversed by a path of \(\mathscr C\), which is consistent since \(\pi\) is injective on \(P\), and every other \(S\)-edge gets the label \(1\). All these labels are within \(\eta\) of \(1\). Lemma 2.1 gives labels \(\ell_F\) of the \(\mathcal T\)-edges over \(F\) with \(L(r,v)=1\) for \(r\in\mathcal B\), \(v\in F\), and \(|L(\rho_z,v)-1|<\delta\) for all \(z\), \(v\). Pull them back: \(x_{g,t}=\ell_F(\pi(g),t)\). For a condition of \(\mathscr C\) at the vertex \(g\), the path over \(\Gamma\) maps to the path over \(F\) from \(\pi(g)\) reading the same word, and every edge it traverses carries the same label as its image, by construction for the \(S\)-edges and by the pullback for the \(\mathcal T\)-edges. So the products agree, and the point \((x_{g,t})\in\mathscr P\) satisfies every condition of \(\mathscr C\).

By Section 3 there is a point of \(\mathscr P\) satisfying all conditions (4.1). With it, the labelling of the graph over \(\Gamma\) satisfies the hypotheses of Lemma 3.1 of the lesson on exact counts, with \(F=\Gamma\) and \(\epsilon=\eta\), and its \(h\) satisfies \(h\le\delta\). By hypothesis \(L(z,g)=1\) for every \(z\in\mathcal D\) and \(g\in\Gamma\). The first inequality of (3.1) there gives \(|1-L(\rho_z,g)|\le C(h+\eta)h\), and taking the supremum,
\[
\begin{aligned}
h&\le C(h+\eta)h\le C(\delta+\eta)h\\
&<\tfrac12h\quad\text{if }h>0 .
\end{aligned}
\]
So \(h=0\): the products along all relators, distinguished and ordinary, are \(1\) from every vertex.

Finally let \(w\) be a word on \(S\) of value \(1\) and \(g\in\Gamma\). Since the aligned presentation presents \(\Gamma\), \(w\) is a product of conjugates \(ur^{\pm1}u^{-1}\) of relators in the free group on \(A\). By Lemma 1.1 (3), (5) and (4) of the lesson on exact counts, \(L(w,g)\) is the product of the conjugates \(L(u,g)L(r,g\bar u)^{\pm1}L(u,g)^{-1}\), each equal to \(1\). The path reading \(w\) traverses only \(S\)-edges, so \(L(w,g)\) is the product computed with the original labelling \(a\). \(\square\)

The proof never assumes that the labelling \(a\) is pulled back from a finite quotient: each finite set of conditions uses its own quotient, and compactness assembles the answers. The finite quotients are needed because the degree argument works on a finite-dimensional torus of unknowns.

## 5. Exercises

**5.1** (easy). Where does the proof of Theorem 4.1 use that \(\Gamma\) is residually finite, and where that \(\mathcal D\) is finite?

**5.2** (easy). Show that in the proof of the finite intersection property, the labels of the \(S\)-edges over \(F\) are well defined: if \((g,s)\) and \((g',s)\) are both traversed by paths of \(\mathscr C\) and \(\pi(g)=\pi(g')\), then \(g=g'\).

**5.3** (medium). Show that \(|\exp(w)-1|=2\sin(|w|/2)\) for \(w\in\operatorname{Im}\mathbb H\) with \(|w|<\pi\), and deduce that \(|\exp(\tau w)-1|\) increases with \(\tau\in[0,1]\).

**5.4** (medium). In Lemma 2.1, suppose \(\mathcal D\) is empty. Show that the conclusion holds with any labels of the \(\mathcal T\)-edges solving the equations of \(\mathcal B\), and show that such labels exist by the degree argument without the sets \(\mathcal O_\tau\), that is, with \(\mathcal O_\tau=H^m\).

**5.5** (medium). Let \(\Gamma=\mathbb Z^2=\langle x,y\rangle\), \(S=\{x,y\}\), and \(\mathcal D=\{xyx^{-1}y^{-1}\}\) (Exercise 5.2 of the lesson on aligned presentations). Show directly, without Theorem 4.1, that a labelling with \(L(xyx^{-1}y^{-1},g)=1\) for every \(g\) has \(L(w,g)=1\) for every word \(w\) of value \(1\). (Hint: \(\langle x,y\mid xyx^{-1}y^{-1}\rangle\) presents \(\mathbb Z^2\).)

## 6. Solutions

**5.1.** Residual finiteness is used once, to find a finite quotient injective on the finite set \(P\) of starting points, so that the prescribed labels descend consistently. Finiteness of \(\mathcal D\) enters through the constant \(C\) of Lemma 3.1 of the lesson on exact counts, which is a maximum over \(z\in\mathcal D\), and through the finitely many products in the function \(h\) on a finite quotient.

**5.2.** Both \(g\) and \(g'\) lie in \(P\), and \(\pi\) is injective on \(P\).

**5.3.** \(\exp(w)=\cos|w|+\frac w{|w|}\sin|w|\), so \(|\exp(w)-1|^2=(1-\cos|w|)^2+\sin^2|w|=2-2\cos|w|=4\sin^2(|w|/2)\). For \(\tau\in[0,1]\), \(\tau|w|/2\in[0,\pi/2)\), where the sine increases.

**5.4.** The second condition of the lemma is vacuous when \(\mathcal D\) is empty, and so is (2.1); then \(h=0\) and \(\mathcal O_\tau=H^m\), which has empty boundary. The degree of \(f_\tau\) on \(H^m\) is constant by (DEG 3) and equals \(\deg(f_0,H^m,\mathbf 1)\ne0\) by Lemma 5.1 of the lesson on word maps, so \(f_1\) has a root.

**5.5.** The word \(w\) is a product of conjugates of \(c=xyx^{-1}y^{-1}\) and \(c^{-1}\) in the free group on \(x,y\). By Lemma 1.1 of the lesson on exact counts (with \(\mathcal T\) empty and \(F=\Gamma\)), \(L(w,g)\) is the product of the elements \(L(u,g)L(c,g\bar u)^{\pm1}L(u,g)^{-1}\), and each is \(1\).

## References

- [OpenAI-EG] OpenAI, *A finitely generated counterexample to the Eilenberg–Ganea conjecture*, OpenAI Math Release preprint, 23 September 2026, Sections 3.3 and 3.4. https://github.com/openai/math/tree/main/preprints/A-finitely-generated-counterexample-to-the-Eilenberg-Ganea-conjecture-September-23-2026
