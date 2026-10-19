# Homotopy exact squares

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The axiom (Der4) says that two particular squares of small categories, built from comma categories, induce invertible base change morphisms in a derivator. Many other squares share this property, and recognizing them is the main computational tool of the theory: a square is *homotopy exact* when its base change morphism is invertible in every derivator. This lesson proves that base change is compatible with pasting squares side by side and on top of each other, that a right adjoint does not change homotopy colimits, that homotopy Kan extensions along fully faithful functors are fully faithful, and that extensions along sieves and cosieves are extensions by terminal and initial objects.

**Prerequisites.** The lesson [*Kan extensions and the derivator axioms*](kan-extensions-and-the-derivator-axioms.md): base change morphisms (Section 3, with Lemma 3.1), the axioms (Definition 4.1), Proposition 5.1 and Proposition 6.1.

Throughout, \(\mathbb D\) is a prederivator that admits the Kan extensions mentioned, with chosen adjoints, units \(\eta\) and counits \(\varepsilon\). For a square with a natural transformation \(\alpha:u'v\to wu\), as in Section 3 of the preceding lesson, the base change morphism is

\[
\alpha_!=\varepsilon\cdot u_!\alpha^*u'_!\cdot u_!v^*\eta':
\]
\[
u_!v^*\longrightarrow w^*u'_!.
\]

Here \(\cdot\) is vertical composition, read from right to left, and juxtaposition is whiskering.

## 1. Pasting

**Lemma 1.1 (horizontal pasting).** Consider two adjacent squares

\[
\begin{array}{ccccc}
J_1&\xrightarrow{v_1}&J_2&\xrightarrow{v_2}&J_3\\
{\scriptstyle u_1}\downarrow&&{\scriptstyle u_2}\downarrow&&\downarrow{\scriptstyle u_3}\\
K_1&\xrightarrow{w_1}&K_2&\xrightarrow{w_2}&K_3
\end{array}
\]

with \(\alpha_1:u_2v_1\to w_1u_1\) and \(\alpha_2:u_3v_2\to w_2u_2\), and let

\[
\alpha=w_2\alpha_1\cdot\alpha_2v_1:\;u_3v_2v_1\to w_2w_1u_1
\]

be the pasted transformation. Then

\[
\alpha_!=w_1^*\alpha_{2!}\cdot\alpha_{1!}v_2^*.
\]

**Proof.** The 2-functor \(\mathbb D\) turns the pasting into

\[
\alpha^*=\alpha_1^*w_2^*\cdot v_1^*\alpha_2^*:\;
v_1^*v_2^*u_3^*\to u_1^*w_1^*w_2^*,
\]

by the whiskering rules \((w\beta)^*=\beta^*w^*\) and \((\beta t)^*=t^*\beta^*\). Expand the right side of the claim, with \(\Phi=\alpha_{2!}\):

\[
w_1^*\Phi\cdot\varepsilon_1w_1^*u_{2!}v_2^*
\cdot u_{1!}\alpha_1^*u_{2!}v_2^*\cdot u_{1!}v_1^*\eta_2v_2^*.
\]

Naturality of \(\varepsilon_1\) moves \(w_1^*\Phi\) to the right of it, where it appears as \(u_{1!}u_1^*w_1^*\Phi\); naturality of \(\alpha_1^*\) then moves it past \(\alpha_1^*\), where it appears as \(u_{1!}v_1^*u_2^*\Phi\). The expression becomes

\[
\varepsilon_1\cdot u_{1!}\alpha_1^*w_2^*u_{3!}
\cdot u_{1!}v_1^*\bigl(u_2^*\Phi\cdot\eta_2v_2^*\bigr).
\]

Expanding \(\Phi=\varepsilon_2w_2^*u_{3!}\cdot u_{2!}\alpha_2^*u_{3!}\cdot u_{2!}v_2^*\eta_3\) and moving \(\eta_2\) to the left by naturality,

\[
\begin{aligned}
u_2^*\Phi\cdot\eta_2v_2^*
&=u_2^*\varepsilon_2w_2^*u_{3!}\cdot\eta_2u_2^*w_2^*u_{3!}\\
&\qquad\cdot\alpha_2^*u_{3!}\cdot v_2^*\eta_3.
\end{aligned}
\]

By the triangle identity \(u_2^*\varepsilon_2\cdot\eta_2u_2^*=1\) this is \(\alpha_2^*u_{3!}\cdot v_2^*\eta_3\). Substituting,

\[
\varepsilon_1\cdot u_{1!}\bigl(\alpha_1^*w_2^*\cdot v_1^*\alpha_2^*\bigr)u_{3!}
\cdot u_{1!}v_1^*v_2^*\eta_3,
\]

which is \(\alpha_!\) by the formula for \(\alpha^*\). \(\square\)

**Lemma 1.2 (vertical pasting).** Consider two squares stacked vertically,

\[
\begin{array}{ccc}
J&\xrightarrow{v}&J'\\
{\scriptstyle u}\downarrow&&\downarrow{\scriptstyle u'}\\
K&\xrightarrow{w}&K'\\
{\scriptstyle x}\downarrow&&\downarrow{\scriptstyle x'}\\
L&\xrightarrow{y}&L'
\end{array}
\]

with \(\alpha:u'v\to wu\) and \(\beta:x'w\to yx\). Give \((xu)_!=x_!u_!\) the composite adjunction, with unit \(u^*\eta_xu_!\cdot\eta_u\) and counit \(\varepsilon_x\cdot x_!\varepsilon_ux^*\). Then the pasted transformation \(\gamma=\beta u\cdot x'\alpha:x'u'v\to yxu\) has

\[
\gamma_!=\beta_!u'_!\cdot x_!\alpha_!.
\]

**Proof.** Here \(\gamma^*=u^*\beta^*\cdot\alpha^*x'^*\). The right side is

\[
\begin{aligned}
&\varepsilon_x y^*x'_!u'_!\cdot x_!\beta^*x'_!u'_!\\
&\quad\cdot x_!w^*\eta_{x'}u'_!\cdot x_!\varepsilon_uw^*u'_!\\
&\quad\cdot x_!u_!\alpha^*u'_!\cdot x_!u_!v^*\eta_{u'}.
\end{aligned}
\]

Move \(x_!\varepsilon_uw^*u'_!\) to the left past \(x_!w^*\eta_{x'}u'_!\) and \(x_!\beta^*x'_!u'_!\) by naturality of \(\varepsilon_u\); it becomes \(x_!\varepsilon_ux^*y^*x'_!u'_!\), next to \(\varepsilon_x\), and the two maps it passed become \(x_!u_!u^*w^*\eta_{x'}u'_!\) and \(x_!u_!u^*\beta^*x'_!u'_!\). By naturality of \(\alpha^*\), the pair \(x_!u_!u^*w^*\eta_{x'}u'_!\cdot x_!u_!\alpha^*u'_!\) equals \(x_!u_!\alpha^*x'^*x'_!u'_!\cdot x_!u_!v^*u'^*\eta_{x'}u'_!\). The result is

\[
\begin{aligned}
&(\varepsilon_x\cdot x_!\varepsilon_ux^*)y^*x'_!u'_!\\
&\quad\cdot x_!u_!(u^*\beta^*\cdot\alpha^*x'^*)x'_!u'_!\\
&\quad\cdot x_!u_!v^*(u'^*\eta_{x'}u'_!\cdot\eta_{u'}),
\end{aligned}
\]

which is \(\gamma_!\) computed with the composite adjunctions. \(\square\)

The dual statements for \(\alpha_*\) hold with the dual proofs.

## 2. Exact squares

**Definition 2.1.** A square with \(\alpha:u'v\to wu\) is *\(\mathbb D\)-exact* if \(\alpha_!\) is an isomorphism. It is *homotopy exact* if it is \(\mathbb D\)-exact for every derivator \(\mathbb D\).

By Lemma 3.1 of the preceding lesson this does not depend on the chosen adjoints. By Lemmas 1.1 and 1.2, a square pasted from two \(\mathbb D\)-exact squares is \(\mathbb D\)-exact. Axiom (Der4) states that the comma square

\[
\begin{array}{ccc}
J_{/k}&\xrightarrow{\mathrm{pr}}&J\\
{\scriptstyle p}\downarrow&&\downarrow{\scriptstyle u}\\
e&\xrightarrow{k}&K
\end{array}
\]

with the transformation \(\alpha^{/k}:u\,\mathrm{pr}\to kp\) is homotopy exact, together with the dual statement for \(J_{k/}\).

The definition depends on the direction of the transformation. A commutative square, regarded with its identity transformation, need not be exact: Exercise 6.4 gives an example in the represented derivator of sets.

**Lemma 2.2 (adjunctions).** Let \(L:K\to J\) be left adjoint to \(R:J\to K\), with unit \(\eta:1\to RL\) and counit \(\varepsilon:LR\to1\). For every prederivator \(\mathbb D\), the functor \(R^*:\mathbb D(K)\to\mathbb D(J)\) is left adjoint to \(L^*\), with unit \(\eta^*\) and counit \(\varepsilon^*\). If \(L\) is fully faithful, so is \(R^*\).

**Proof.** \(\eta^*:1\to(RL)^*=L^*R^*\) and \(\varepsilon^*:R^*L^*=(LR)^*\to1\). The triangle identities \(R\varepsilon\cdot\eta R=1\) and \(\varepsilon L\cdot L\eta=1\) become, by the whiskering rules, \(\varepsilon^*R^*\cdot R^*\eta^*=1\) and \(L^*\varepsilon^*\cdot\eta^*L^*=1\), which are the triangle identities for \(R^*\dashv L^*\). If \(L\) is fully faithful, \(\eta\) is invertible, hence so is \(\eta^*\), and a left adjoint with invertible unit is fully faithful. \(\square\)

**Proposition 2.3 (right adjoints are homotopy final).** Let \(R:J\to K\) be a right adjoint. The square

\[
\begin{array}{ccc}
J&\xrightarrow{R}&K\\
{\scriptstyle p_J}\downarrow&&\downarrow{\scriptstyle p_K}\\
e&\xrightarrow{1}&e
\end{array}
\]

with the identity transformation \(p_KR=p_J\) is homotopy exact. Thus

\[
\operatorname{hocolim}_JR^*X\cong\operatorname{hocolim}_KX
\]

for every derivator \(\mathbb D\) and \(X\) in \(\mathbb D(K)\). Dually, if \(L:J\to K\) is a left adjoint, then \(\operatorname{holim}_KX\to\operatorname{holim}_JL^*X\) is invertible for \(X\) in \(\mathbb D(K)\).

**Proof.** Let \(L\) be a left adjoint of \(R\). By Lemma 2.2, \(R^*\dashv L^*\), so \(p_{J!}R^*\) is left adjoint to \(L^*p_J^*=(p_JL)^*=p_K^*\), with counit

\[
p_{J!}R^*L^*p_J^*\xrightarrow{\;p_{J!}\varepsilon^*p_J^*\;}p_{J!}p_J^*\xrightarrow{\;\varepsilon_J\;}1.
\]

The transformation \(\varepsilon^*p_J^*=(p_J\varepsilon)^*\) is the identity, because \(p_J\varepsilon\) is a transformation between functors to \(e\). So this counit is \(\varepsilon_J\). The base change morphism is

\[
\begin{aligned}
p_{J!}R^*&\xrightarrow{\;p_{J!}R^*\eta_K\;}p_{J!}R^*p_K^*p_{K!}\\
&\;=\;p_{J!}p_J^*p_{K!}\xrightarrow{\;\varepsilon_Jp_{K!}\;}p_{K!},
\end{aligned}
\]

and this is the canonical comparison between two left adjoints of \(p_K^*\): for left adjoints \(F,G\) of the same functor \(U\), the composite \(F\to FUG\to G\) of the unit of \(G\) and the counit of \(F\) is an isomorphism, with inverse the analogous composite \(G\to GUF\to F\). The dual statement follows by duality. \(\square\)

**Corollary 2.4.** If \(K\) has a terminal object \(t\), then \(X_t\cong\operatorname{hocolim}_KX\). If \(K\) has an initial object \(i\), then \(\operatorname{holim}_KX\cong X_i\).

**Proof.** \(t:e\to K\) is right adjoint to \(p_K\), and \(t^*X=X_t\) while \(\operatorname{hocolim}_e=1\). Apply Proposition 2.3. \(\square\)

## 3. Fully faithful functors

The preceding lesson (Proposition 6.1) showed that for a fully faithful \(u:J\to K\) the unit \(X\to u^*u_!X\) and the counit \(u^*u_*X\to X\) are invertible, so \(u_!\) and \(u_*\) are fully faithful. The next lemma describes their essential images.

**Lemma 3.1.** Let \(\mathbb D\) be a derivator, \(u:J\to K\) fully faithful and \(X\) in \(\mathbb D(K)\).

1. \(X\) is in the essential image of \(u_!\) if and only if the counit \(\varepsilon:u_!u^*X\to X\) is invertible at every object \(k\) of \(K\) outside \(u(J)\).
2. \(X\) is in the essential image of \(u_*\) if and only if the unit \(\eta:X\to u_*u^*X\) is invertible at every object \(k\) outside \(u(J)\).

**Proof.** We prove 2. Since \(u_*\) is fully faithful, \(X\) is in its essential image if and only if \(\eta_X\) is invertible: if \(X\cong u_*Y\), naturality of \(\eta\) and the triangle identity \(u_*\varepsilon\cdot\eta u_*=1\), with \(\varepsilon\) invertible, show that \(\eta_{u_*Y}\) is invertible. By (Der2), \(\eta_X\) is invertible if and only if its components are. At objects \(u(j)\), the triangle identity \(\varepsilon u^*\cdot u^*\eta=1\) and invertibility of \(\varepsilon\) show that \(u^*\eta\) is invertible. So only the components at objects outside \(u(J)\) need to be checked. Statement 1 is dual. \(\square\)

**Definition 3.2.** A fully faithful functor \(u:J\to K\) that is injective on objects is a *cosieve* if every object \(k\) that receives a morphism \(u(j)\to k\) lies in \(u(J)\), and a *sieve* if every object \(k\) with a morphism \(k\to u(j)\) lies in \(u(J)\).

For example, the inclusion of \(1\) into \([1]\) is a cosieve, and the inclusion of \(0\) is a sieve.

**Proposition 3.3 (extension by initial and terminal objects).** Let \(\mathbb D\) be a derivator.

1. If \(u:J\to K\) is a cosieve, \(u_!\) is fully faithful, and \(X\) is in its essential image if and only if \(X_k\) is an initial object of \(\mathbb D(e)\) for every \(k\) outside \(u(J)\).
2. If \(u\) is a sieve, \(u_*\) is fully faithful, and \(X\) is in its essential image if and only if \(X_k\) is a terminal object for every \(k\) outside \(u(J)\).

**Proof.** We prove 1. For \(k\) outside \(u(J)\), the category \(J_{/k}\) is empty: an object \((j,f:u(j)\to k)\) would put \(k\) in \(u(J)\). By (Der4),

\[
(u_!u^*X)_k\cong\operatorname{hocolim}_{\emptyset}(\mathrm{pr}^*u^*X),
\]

and a homotopy colimit over the empty category is an initial object: \(\operatorname{hocolim}_\emptyset\) is left adjoint to \(\mathbb D(e)\to\mathbb D(\emptyset)\simeq e\) (Proposition 5.1 of the preceding lesson). So \((u_!u^*X)_k\) is initial, and \(\varepsilon_k\) is invertible exactly when \(X_k\) is initial. Lemma 3.1 concludes. \(\square\)

## 4. Two examples in shapes of size two and three

Write \([1]=(0\to1)\) and \([2]=(0\to1\to2)\).

- The inclusion \(i_1:\{1\}\to[1]\) is a cosieve. By Proposition 3.3, \(i_{1!}\) identifies \(\mathbb D(e)\) with the objects \(X\) of \(\mathbb D([1])\) with \(X_0\) initial: these are the arrows "from the initial object".
- The inclusion \(i_0:\{0\}\to[1]\) is a sieve, and \(i_{0*}\) identifies \(\mathbb D(e)\) with the arrows "to the terminal object".
- The functor \(d:[1]\to[2]\), \(0\mapsto0\), \(1\mapsto2\), is fully faithful but neither a sieve nor a cosieve. It is left adjoint to \(r:[2]\to[1]\), \(r(0)=r(1)=0\), \(r(2)=1\): both \(\operatorname{Hom}(d(j),k)\) and \(\operatorname{Hom}(j,r(k))\) have one element exactly when \(j=0\) or \(k=2\). By Lemma 2.2, \(r^*\) is left adjoint to \(d^*\), so \(d_!\cong r^*\). The underlying diagram of \(r^*X\) is \(X_0\xrightarrow{1}X_0\to X_1\): the arrow \(X_0\to X_1\) with its source repeated.

These elementary extensions are the building blocks of the cofibre and fibre constructions of the lesson on pointed derivators.

## 5. Where homotopy exactness fails

Homotopy exactness depends on the derivator only through the axioms, so a single derivator can refute it. In the represented derivator of a complete and cocomplete category, base change morphisms are computed by Kan's formulas, and Exercise 6.4 shows that the square

\[
\begin{array}{ccc}
e&\xrightarrow{0}&[1]\\
\downarrow&&\downarrow{\scriptstyle p}\\
e&\xrightarrow{1}&e
\end{array}
\]

with the identity transformation is not homotopy exact, while the same square with \(1\) in place of \(0\) is, by Corollary 2.4. The object \(0\) is a left adjoint of \(p\), not a right adjoint, and Proposition 2.3 does not apply to it.

## 6. Exercises

**6.1** (easy). Show that a square pasted horizontally from two homotopy exact squares is homotopy exact.

**6.2** (easy). Show that in any derivator, \(\operatorname{holim}_{[1]}X\cong X_0\) and \(\operatorname{hocolim}_{[1]}X\cong X_1\).

**6.3** (medium). Let \(u:J\to K\) be fully faithful. Show that \(u_!X\) and \(u_*X\) restrict to \(X\) along \(u\), and give an example, in the represented derivator of sets, with \(u_!X\not\cong u_*X\).

**6.4** (medium). In the represented derivator of sets, compute the base change morphism of the square in Section 5 and show that it is the arrow \(X_0\to X_1\) of \(X\). Deduce that the square is not homotopy exact.

**6.5** (hard). Give a functor \(u:J\to K\) and an object \(k\) such that the projection \(J_{/k}\to J\) has neither a left nor a right adjoint. Show that \(J_{/k}\) has a terminal object whenever \(k=u(j)\) and \(u\) is fully faithful, and use this to give a second proof of Proposition 6.1 of the preceding lesson, through Corollary 2.4.

## 7. Solutions

**6.1.** By Lemma 1.1 the pasted base change is \(w_1^*\alpha_{2!}\cdot\alpha_{1!}v_2^*\), a composite of two isomorphisms.

**6.2.** \(0\) is initial and \(1\) terminal in \([1]\); apply Corollary 2.4.

**6.3.** Proposition 6.1 of the preceding lesson gives \(u^*u_!X\cong X\cong u^*u_*X\). For \(u=i_1:\{1\}\to[1]\) and a set \(S\), \(u_!S=(\emptyset\to S)\) and \(u_*S=(S\to S)\), by Kan's formulas: \(\{1\}_{/0}\) is empty, \(\{1\}_{0/}=\{(1,0\to1)\}\). These differ when \(S\) is not empty.

**6.4.** Write the square as \(u=1_e\), \(v=0:e\to[1]\), \(u'=p\), \(w=1\). The unit of \(p_!\dashv p^*\) at \(X\) is the diagram map \(X\to p^*X_1\) with components \(X_0\to X_1\) and \(1_{X_1}\), since \(p_!X=X_1\) with the injections of Kan's formula. The base change morphism \(\alpha_!:v^*X=X_0\to p_!X=X_1\) is the component of this unit at \(0\), followed by identities: the arrow \(X_0\to X_1\). For \(X=(\emptyset\to\{*\})\) it is not invertible.

**6.5.** Let \(J\) have two objects \(a,b\) and two parallel morphisms \(a\rightrightarrows b\) besides the identities, let \(u:J\to[1]\) send \(a\) to \(0\), \(b\) to \(1\) and both morphisms to \(0\to1\), and take \(k=0\). Then \(J_{/0}\) has the single object \((a,1_0)\), and \(\mathrm{pr}\) picks out \(a\). A right adjoint \(R\) would give \(\operatorname{Hom}_J(a,j)\cong\operatorname{Hom}(*,R(j))\), a one-element set for every \(j\); but \(\operatorname{Hom}_J(a,b)\) has two elements. A left adjoint \(L\) would give \(\operatorname{Hom}_J(j,a)\cong\operatorname{Hom}(L(j),*)\), again one element; but \(\operatorname{Hom}_J(b,a)\) is empty.

For the second part: if \(u\) is fully faithful and \(k=u(j)\), then \(t=(j,1_k)\) is terminal in \(J_{/k}\), by the proof of Corollary 2.3 of the preceding lesson. By (Der4) and Corollary 2.4,
\[
\begin{aligned}
(u_!X)_{u(j)}&\cong\operatorname{hocolim}_{J_{/k}}\mathrm{pr}^*X\\
&\cong(\mathrm{pr}^*X)_t=X_j,
\end{aligned}
\]
and the composite is the component of the unit at \(j\), as in the proof of Proposition 6.1 of the preceding lesson. By (Der2) the unit is invertible.

## Sources

- [Gr] M. Groth, *Derivators, pointed derivators and stable derivators*, Algebraic & Geometric Topology 13 (2013), 313–374; arXiv:1112.3840. https://arxiv.org/abs/1112.3840 — Section 1.2 develops the base change calculus; the pasting lemmas, the finality of right adjoints and the extension by initial and terminal objects appear there.
- [PS] A. Grothendieck, *Pursuing Stacks*, §69, arXiv:2111.01000. https://arxiv.org/abs/2111.01000
