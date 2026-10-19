# Kan extensions and the derivator axioms

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A prederivator \(\mathbb D\) assigns to each small category \(J\) a category \(\mathbb D(J)\) of "diagrams of shape \(J\)" and to each functor \(u:J\to K\) a restriction \(u^*\). For the represented prederivator of a category \(\mathcal C\), restriction along \(u\) has a left adjoint and a right adjoint whenever \(\mathcal C\) has enough colimits and limits: these are the left and right Kan extensions, and they are computed at each object by a colimit or a limit over a comma category (Kan's formulas). *Pursuing Stacks* (§69) names the existence of both adjoints as the main property to demand of the system \(I\mapsto D(I)\). The derivator axioms demand it, together with Kan's formulas, without asking for any actual colimits in the categories \(\mathbb D(J)\).

This lesson proves Kan's formulas, constructs the comparison maps that the axioms require to be invertible, states the axioms, and shows that a represented prederivator is a derivator exactly when its category is complete and cocomplete. Sections 5 and 6 derive the first consequences of the axioms.

**Prerequisites.** The lesson [*Diagrams up to weak equivalence*](diagrams-up-to-weak-equivalence.md) (prederivators, Definition 4.1; underlying diagrams, Section 5). Limits, colimits and adjoint functors, with the description of an adjunction by a unit and a counit satisfying the two triangle identities.

## 1. Comma categories

Let \(u:J\to K\) be a functor and \(k\) an object of \(K\).

- The category \(J_{/k}\) has as objects the pairs \((j,f)\) with \(j\) in \(J\) and \(f:u(j)\to k\). A morphism \((j,f)\to(j',f')\) is a morphism \(g:j\to j'\) with \(f'\,u(g)=f\).
- The category \(J_{k/}\) has as objects the pairs \((j,f)\) with \(f:k\to u(j)\). A morphism \((j,f)\to(j',f')\) is a morphism \(g:j\to j'\) with \(u(g)\,f=f'\).

Both have a projection \(\mathrm{pr}\) to \(J\) forgetting \(f\), and a unique functor \(p\) to \(e\). Viewing \(k\) as a functor \(e\to K\), the morphisms \(f\) are the components of two natural transformations

\[
\alpha^{/k}:u\circ\mathrm{pr}\to k\circ p
\quad\text{on }J_{/k},
\]
\[
\alpha^{k/}:k\circ p\to u\circ\mathrm{pr}
\quad\text{on }J_{k/}.
\]

A morphism \(h:k\to k'\) of \(K\) induces functors \(h_\sharp:J_{/k}\to J_{/k'}\), \((j,f)\mapsto(j,hf)\), and \(h^\sharp:J_{k'/}\to J_{k/}\), \((j,f)\mapsto(j,fh)\), compatible with the projections. For \(u=1_K\) we write \(K_{/k}\) and \(K_{k/}\); the object \((k,1_k)\) is terminal in \(K_{/k}\) and initial in \(K_{k/}\).

## 2. Kan's formulas

**Theorem 2.1 (left Kan extension).** Let \(u:J\to K\) be a functor between small categories and \(\mathcal C\) a category with colimits of all small diagrams. For \(X:J\to\mathcal C\) and \(k\) in \(K\) put

\[
(u_!X)(k)=\operatorname{colim}_{J_{/k}}X\circ\mathrm{pr},
\]

with colimit injections \(\iota_{(j,f)}:X(j)\to(u_!X)(k)\), and for \(h:k\to k'\) let \((u_!X)(h)\) be the map with

\[
(u_!X)(h)\,\iota_{(j,f)}=\iota_{(j,hf)}.
\]

Then \(u_!X\) is a functor \(K\to\mathcal C\), \(u_!\) is a functor \(\mathcal C^J\to\mathcal C^K\), and \(u_!\) is left adjoint to \(u^*\). The unit \(\eta_X:X\to u^*u_!X\) has components \(\eta_{X,j}=\iota_{(j,1_{u(j)})}\).

**Proof.** The maps \(\iota_{(j,hf)}\), indexed by \(J_{/k}\), form a cocone on \(X\circ\mathrm{pr}\): a morphism \(g:(j,f)\to(j',f')\) of \(J_{/k}\) is also a morphism \((j,hf)\to(j',hf')\) of \(J_{/k'}\), so \(\iota_{(j',hf')}X(g)=\iota_{(j,hf)}\). This defines \((u_!X)(h)\) uniquely. Comparing on injections gives \((u_!X)(1)=1\) and \((u_!X)(h'h)=(u_!X)(h')(u_!X)(h)\). A natural transformation \(\xi:X\to X'\) induces maps of colimits \((u_!\xi)_k\) with \((u_!\xi)_k\iota_{(j,f)}=\iota'_{(j,f)}\xi_j\), natural in \(k\) and functorial in \(\xi\), again by comparing on injections.

For \(Y:K\to\mathcal C\), define

\[
\Phi:\operatorname{Hom}(u_!X,Y)\to\operatorname{Hom}(X,u^*Y),
\]
\[
\Phi(\varphi)_j=\varphi_{u(j)}\,\iota_{(j,1_{u(j)})}.
\]

\(\Phi(\varphi)\) is natural: for \(g:j\to j'\), the map \(g\) is a morphism \((j,u(g))\to(j',1)\) in \(J_{/u(j')}\), so

\[
\varphi_{u(j')}\iota_{(j',1)}X(g)=\varphi_{u(j')}\iota_{(j,u(g))},
\]

and \(\iota_{(j,u(g))}=(u_!X)(u(g))\iota_{(j,1)}\); naturality of \(\varphi\) turns the right side into \(Y(u(g))\varphi_{u(j)}\iota_{(j,1)}\).

Conversely, for \(\psi:X\to u^*Y\) and \(k\) in \(K\), the maps

\[
Y(f)\,\psi_j:X(j)\to Y(k),\quad (j,f)\in J_{/k},
\]

form a cocone: for \(g:(j,f)\to(j',f')\) we have \(Y(f')\psi_{j'}X(g)=Y(f')Y(u(g))\psi_j\), which equals \(Y(f)\psi_j\). Let \(\Psi(\psi)_k\) be the induced map out of the colimit. Comparing on injections shows that \(\Psi(\psi)\) is natural in \(k\), that \(\Phi\Psi(\psi)=\psi\) (use \(f=1\)), and that \(\Psi\Phi(\varphi)=\varphi\): on \(\iota_{(j,f)}\) the right side is \(\varphi_k\iota_{(j,f)}=\varphi_k(u_!X)(f)\iota_{(j,1)}\), which equals \(Y(f)\varphi_{u(j)}\iota_{(j,1)}\). Both \(\Phi\) and \(\Psi\) are natural in \(X\) and \(Y\), by the same comparison. So \(u_!\dashv u^*\), and the unit, which is \(\Phi(1_{u_!X})\), has the stated components. \(\square\)

The dual statement is proved by the dual argument, with \(J_{k/}\) in place of \(J_{/k}\).

**Theorem 2.2 (right Kan extension).** If \(\mathcal C\) has limits of all small diagrams, then

\[
(u_*X)(k)=\lim_{J_{k/}}X\circ\mathrm{pr}
\]

defines a right adjoint \(u_*\) of \(u^*\). The counit \(u^*u_*X\to X\) has components the limit projections at \((j,1_{u(j)})\).

**Corollary 2.3.** If \(u\) is fully faithful, the unit \(X\to u^*u_!X\) and the counit \(u^*u_*X\to X\) are isomorphisms.

**Proof.** For an object \(j\), the object \((j,1_{u(j)})\) is terminal in \(J_{/u(j)}\): a morphism \((j',f)\to(j,1)\) is a \(g:j'\to j\) with \(u(g)=f\), and full faithfulness gives exactly one. A colimit over a category with a terminal object is the value at that object, with the injection at the terminal object as the isomorphism. Hence \(\eta_{X,j}=\iota_{(j,1)}\) is invertible. The counit is dual. \(\square\)

Without full faithfulness the unit need not be invertible; Exercise 7.2 gives an example.

## 3. Base change morphisms

Let \(\mathbb D\) be a prederivator. We say that \(\mathbb D\) *admits left Kan extensions along* \(u:J\to K\) if \(u^*:\mathbb D(K)\to\mathbb D(J)\) has a left adjoint, written \(u_!\), and *right Kan extensions* if it has a right adjoint \(u_*\). For \(p_J:J\to e\) these adjoints are written \(\operatorname{colim}_J\) and \(\lim_J\) when \(\mathbb D\) is represented, and \(\operatorname{hocolim}_J\), \(\operatorname{holim}_J\) in general; they are the *homotopy colimit* and *homotopy limit* of shape \(J\). We fix the chosen adjoints with their units \(\eta\) and counits \(\varepsilon\).

Consider a square of small categories with a natural transformation

\[
\begin{array}{ccc}
J & \xrightarrow{\;v\;} & J'\\
{\scriptstyle u}\downarrow & & \downarrow{\scriptstyle u'}\\
K & \xrightarrow{\;w\;} & K'
\end{array}
\qquad \alpha:u'v\to wu .
\]

Applying \(\mathbb D\) gives \(\alpha^*:v^*u'^*\to u^*w^*\). If \(\mathbb D\) admits left Kan extensions along \(u\) and \(u'\), the *base change morphism* \(\alpha_!:u_!v^*\to w^*u'_!\) is the composite

\[
\begin{aligned}
u_!v^*&\xrightarrow{\;\eta'\;}u_!v^*u'^*u'_!
\xrightarrow{\;\alpha^*\;}u_!u^*w^*u'_!\\
&\xrightarrow{\;\varepsilon\;}w^*u'_!,
\end{aligned}
\]

where \(\eta'\) is the unit of \(u'_!\dashv u'^*\) and \(\varepsilon\) the counit of \(u_!\dashv u^*\). Dually, for a transformation \(\beta:wu\to u'v\) and right Kan extensions along \(u,u'\), the base change morphism \(\beta_*:w^*u'_*\to u_*v^*\) is

\[
\begin{aligned}
w^*u'_*&\xrightarrow{\;\eta\;}u_*u^*w^*u'_*
\xrightarrow{\;\beta^*\;}u_*v^*u'^*u'_*\\
&\xrightarrow{\;\varepsilon'\;}u_*v^*.
\end{aligned}
\]

**Lemma 3.1.** A different choice of adjoints changes \(\alpha_!\) and \(\beta_*\) by composition with the canonical isomorphisms between the chosen adjoints. In particular, whether \(\alpha_!\) or \(\beta_*\) is invertible does not depend on the choices.

**Proof.** If \(\tilde u_!\) is another left adjoint of \(u^*\), there is a unique isomorphism \(\theta:u_!\to\tilde u_!\) with \(\tilde\varepsilon\,\theta u^*=\varepsilon\) and \(\tilde\eta=u^*\theta\,\eta\); it is the image of the identity under the two adjunction bijections. Substituting these equations into the composite defining \(\tilde\alpha_!\) gives \(\tilde\alpha_!\,\theta v^*=\alpha_!\), and similarly for the choice of \(u'_!\), where \(\tilde\alpha_!=w^*\theta'\,\alpha_!\). The case of \(\beta_*\) is dual. \(\square\)

For the comma squares of Section 1 the base change morphisms compare a Kan extension evaluated at \(k\) with a colimit or limit over the comma category:

\[
(\alpha^{/k})_!:\operatorname{hocolim}_{J_{/k}}\mathrm{pr}^*X\longrightarrow k^*u_!X,
\]
\[
(\alpha^{k/})_*:k^*u_*X\longrightarrow\operatorname{holim}_{J_{k/}}\mathrm{pr}^*X.
\]

## 4. The axioms

**Definition 4.1.** A prederivator \(\mathbb D\) is a *derivator* if it satisfies:

- **(Der1)** For small categories \(J_1,J_2\), the functor \(\mathbb D(J_1\sqcup J_2)\to\mathbb D(J_1)\times\mathbb D(J_2)\) given by restriction along the two inclusions is an equivalence of categories, and \(\mathbb D(\emptyset)\) is not empty.
- **(Der2)** A morphism \(f\) of \(\mathbb D(J)\) is an isomorphism if every component \(f_j=j^*f\), \(j\in J\), is an isomorphism of \(\mathbb D(e)\).
- **(Der3)** For every functor \(u\) between small categories, \(\mathbb D\) admits left and right Kan extensions along \(u\).
- **(Der4)** For every functor \(u:J\to K\) and every object \(k\) of \(K\), the base change morphisms \((\alpha^{/k})_!\) and \((\alpha^{k/})_*\) are isomorphisms.

(Der4) is the form that Kan's formulas take in a derivator: the value of \(u_!X\) at \(k\) is the homotopy colimit of \(X\) restricted to \(J_{/k}\), and the value of \(u_*X\) at \(k\) is the homotopy limit over \(J_{k/}\). Every axiom asks for a property of the given prederivator; no further structure is chosen.

**Theorem 4.2.** The represented prederivator \(y(\mathcal C)\) of a category \(\mathcal C\) is a derivator if and only if \(\mathcal C\) has all small limits and colimits.

**Proof.** Suppose \(\mathcal C\) complete and cocomplete. (Der1): a functor on \(J_1\sqcup J_2\) is the same as a pair of functors, so restriction is an isomorphism of categories; and \(\mathcal C^{\emptyset}\) has one object, the empty functor. (Der2): a natural transformation is invertible when its components are. (Der3): Theorems 2.1 and 2.2.

(Der4) for left Kan extensions: take \(u_!\) as in Theorem 2.1 and \(\operatorname{colim}_{J_{/k}}\) as the chosen colimit, with injections \(\iota_{(j,f)}\). We compute \((\alpha^{/k})_!\) on the injection of \(X(j)\) at \((j,f)\). The unit of \(u_!\dashv u^*\) sends it to \(\iota_{(j,1_{u(j)})}:X(j)\to(u_!X)(u(j))\). The transformation \((\alpha^{/k})^*\) is induced by the maps \((u_!X)(f):(u_!X)(u(j))\to(u_!X)(k)\), and \((u_!X)(f)\iota_{(j,1)}=\iota_{(j,f)}\). The counit of \(\operatorname{colim}\dashv\) (constant diagram) maps the colimit of the constant diagram with value \((u_!X)(k)\) to \((u_!X)(k)\) by the identity on each injection. So \((\alpha^{/k})_!\) sends the injection at \((j,f)\) of \(\operatorname{colim}_{J_{/k}}X\mathrm{pr}\) to the injection \(\iota_{(j,f)}\) of \((u_!X)(k)\), which is the same colimit. Hence \((\alpha^{/k})_!\) is the identity for these choices, and by Lemma 3.1 an isomorphism for all choices. Right Kan extensions are dual.

Conversely, if \(y(\mathcal C)\) is a derivator, (Der3) for \(p_J:J\to e\) gives a left and a right adjoint of the constant-diagram functor \(\mathcal C\to\mathcal C^J\), that is, colimits and limits of shape \(J\) for every small \(J\). \(\square\)

**Remark 4.3 (duality).** For a prederivator \(\mathbb D\), the *dual* prederivator has \(\mathbb D^{\mathrm{op}}(J)=\mathbb D(J^{\mathrm{op}})^{\mathrm{op}}\), with \(u^*\) and \(\alpha^*\) induced through \(u^{\mathrm{op}}\) and \(\alpha^{\mathrm{op}}\); the variance works out because \(\alpha^{\mathrm{op}}:v^{\mathrm{op}}\to u^{\mathrm{op}}\) reverses direction and passing to opposite categories reverses it again. Left adjoints of \(\mathbb D^{\mathrm{op}}\) are opposites of right adjoints of \(\mathbb D\), and \((J^{\mathrm{op}})_{/k}=(J_{k/})^{\mathrm{op}}\). So the axioms for \(\mathbb D^{\mathrm{op}}\) are those for \(\mathbb D\) with left and right exchanged, and \(\mathbb D\) is a derivator if and only if \(\mathbb D^{\mathrm{op}}\) is. Statements about left Kan extensions in an arbitrary derivator therefore imply the dual statements about right Kan extensions.

## 5. First consequences

**Proposition 5.1.** Let \(\mathbb D\) be a derivator and \(J\) a small category.

1. \(\mathbb D(\emptyset)\) is equivalent to the category \(e\).
2. \(\mathbb D(J)\) has an initial object and a terminal object.
3. \(\mathbb D(J)\) has finite coproducts and finite products.

**Proof.** (1) By (Der1) for \(\emptyset=\emptyset\sqcup\emptyset\), the diagonal functor \(\mathbb D(\emptyset)\to\mathbb D(\emptyset)\times\mathbb D(\emptyset)\) is an equivalence. Full faithfulness says that the diagonal \(\operatorname{Hom}(x,y)\to\operatorname{Hom}(x,y)^2\) is bijective for all \(x,y\), so each \(\operatorname{Hom}(x,y)\) has at most one element. Essential surjectivity applied to a pair \((x,y)\) gives an object \(z\) with \(z\cong x\) and \(z\cong y\), so \(\operatorname{Hom}(x,y)\) is not empty. So every hom-set of the nonempty category \(\mathbb D(\emptyset)\) has exactly one element, and \(\mathbb D(\emptyset)\simeq e\).

(2) Let \(\emptyset_J:\emptyset\to J\) be the empty functor. Its left adjoint \((\emptyset_J)_!\) sends the object \(0\) of \(\mathbb D(\emptyset)\) to an initial object: \(\operatorname{Hom}((\emptyset_J)_!0,X)\cong\operatorname{Hom}(0,\emptyset_J^*X)\) has exactly one element by (1). Dually \((\emptyset_J)_*0\) is terminal.

(3) Let \(\nabla:J\sqcup J\to J\) be the fold functor and \(i_1,i_2\) the inclusions. Choose a quasi-inverse \(s\) of the equivalence \((i_1^*,i_2^*)\) of (Der1). For \(X_1,X_2\) in \(\mathbb D(J)\), put \(X_1\sqcup X_2=\nabla_!\,s(X_1,X_2)\). Then

\[
\begin{aligned}
&\operatorname{Hom}(\nabla_!s(X_1,X_2),Y)\\
&\quad\cong\operatorname{Hom}(s(X_1,X_2),\nabla^*Y)
\end{aligned}
\]
\[
\cong\operatorname{Hom}(X_1,Y)\times\operatorname{Hom}(X_2,Y),
\]

because \(i_1^*\nabla^*=i_2^*\nabla^*=1\) and \(s\) is an equivalence. So \(\nabla_!s(X_1,X_2)\) is a coproduct; together with (2) this gives all finite coproducts. Products use \(\nabla_*\). \(\square\)

Apart from these, the axioms give no limits or colimits inside the categories \(\mathbb D(J)\). Their role is taken by homotopy limits and colimits, which live one level up: a diagram of shape \(J\) is an object of \(\mathbb D(J)\), not a functor \(J\to\mathbb D(e)\). The cases singled out in *Pursuing Stacks* are the two shapes

\[
\ulcorner=(b\leftarrow a\rightarrow c),
\]
\[
\lrcorner=(b\rightarrow a\leftarrow c).
\]

For \(X\) in \(\mathbb D(\ulcorner)\), \(\operatorname{hocolim}_\ulcorner X\) is the *homotopy pushout*; for \(X\) in \(\mathbb D(\lrcorner)\), \(\operatorname{holim}_\lrcorner X\) is the *homotopy pullback*. In the represented derivator of a complete and cocomplete category they are the ordinary pushout and pullback. Cofibres and fibres of morphisms are homotopy pushouts and pullbacks along a terminal or an initial object; they are studied in the lesson on pointed derivators.

## 6. Kan extensions along fully faithful functors

The first consequence of (Der4) that has no analogue in the axioms themselves is the derivator version of Corollary 2.3.

**Proposition 6.1.** Let \(\mathbb D\) be a derivator and \(u:J\to K\) a fully faithful functor. Then the unit \(X\to u^*u_!X\) and the counit \(u^*u_*X\to X\) are isomorphisms for all \(X\) in \(\mathbb D(J)\). Hence \(u_!\) and \(u_*\) are fully faithful.

**Proof.** By (Der2) it suffices to show that \(j^*\eta_X\) is invertible for each \(j\) in \(J\). Put \(k=u(j)\). In \(J_{/k}\) the object \(t=(j,1_k)\) is terminal (proof of Corollary 2.3). Write \(c:e\to J_{/k}\) for this object, so \(\mathrm{pr}\,c=j\). The functor \(p:J_{/k}\to e\) is left adjoint to \(c\): there is exactly one morphism from every object to \(t\). Restriction along a right adjoint is left adjoint to restriction along its left adjoint: the unit \(1\to cp\) and the counit \(pc=1\) of \(p\dashv c\) give, by applying \(\mathbb D\), transformations \(1\to p^*c^*\) and \(c^*p^*=1\) satisfying the triangle identities, so \(c^*\) is left adjoint to \(p^*\), with identity counit.

By Lemma 3.1 we may compute \((\alpha^{/k})_!\) with \(c^*\) as the chosen left adjoint of \(p^*\). The three maps in its definition become: \(c^*\mathrm{pr}^*\eta_X=j^*\eta_X\), because \(\mathrm{pr}\,c=j\); then \((\alpha^{/k}c)^*\), where \(\alpha^{/k}c\) is the component of \(\alpha^{/k}\) at \(t\), namely \(1_k\), so this map is the identity; and the identity counit. Hence \((\alpha^{/k})_!=j^*\eta_X\), a map \(X_j\to(u_!X)_k=(u^*u_!X)_j\). Since \((\alpha^{/k})_!\) is invertible by (Der4), so is \(j^*\eta_X\). The counit is dual. A left adjoint whose unit is invertible is fully faithful. \(\square\)

## 7. Exercises

**7.1** (easy). For the represented derivator of \(\mathrm{Set}\) and \(u:[1]\to e\), compute \(u_!\) and \(u_*\) on an object \(X=(X_0\to X_1)\).

**7.2** (easy). Let \(J=\{0,1\}\) be the discrete category with two objects and \(u:J\to e\). For the represented derivator of abelian groups, show that the unit \(X\to u^*u_!X\) is not an isomorphism unless \(X_0=X_1=0\).

**7.3** (medium). For the represented derivator of a complete and cocomplete category \(\mathcal C\), let \(i:\{0\}\to[1]\) be the inclusion of the object \(0\). Show that \(i_!x=(x\xrightarrow{1}x)\) and \(i_*x=(x\to *)\), where \(*\) is a terminal object.

**7.4** (medium). Let \(\mathbb D\) be a derivator and \(J\) a small category with a terminal object \(t\). Show that \(\operatorname{hocolim}_J\cong t^*\).

**7.5** (hard). Let \(\mathcal A\) be an abelian category. Show that the prederivator \(\mathbb D_{\mathcal A}\), \(J\mapsto D(\mathcal A^J)\), satisfies (Der1) and (Der2).

## 8. Solutions

**7.1.** Here \(J_{/*}=[1]\) and \(J_{*/}=[1]\). The colimit of \(X_0\to X_1\) is \(X_1\) and its limit is \(X_0\), because \(1\) is terminal and \(0\) initial in \([1]\). So \(u_!X=X_1\) and \(u_*X=X_0\).

**7.2.** \(u_!X=X_0\oplus X_1\), and the unit at \(0\) is the inclusion \(X_0\to X_0\oplus X_1\), which is invertible only if \(X_1=0\); symmetrically at \(1\).

**7.3.** For \(k=0\), \(\{0\}_{/0}\) has one object, so \((i_!x)_0=x\); for \(k=1\), \(\{0\}_{/1}\) has the single object \((0,0\to1)\), so \((i_!x)_1=x\), and the map \((i_!x)(0\to1)\) is the identity on injections. For \(i_*\), \(\{0\}_{0/}\) has one object and \(\{0\}_{1/}\) is empty, so \((i_*x)_1\) is the limit of the empty diagram, a terminal object.

**7.4.** The functor \(t:e\to J\) is right adjoint to \(p_J:J\to e\), with counit \(p_Jt=1_e\) and unit \(1_J\to tp_J\) given by the unique maps \(j\to t\). As in the proof of Proposition 6.1, restriction along this adjunction gives \(t^*\dashv p_J^*\). Uniqueness of left adjoints gives \(\operatorname{hocolim}_J\cong t^*\).

**7.5.** (Der1): complexes and chain maps on \(J_1\sqcup J_2\) are pairs of complexes and chain maps, and homotopies and quasi-isomorphisms are pairs as well, so \(K(\mathcal A^{J_1\sqcup J_2})=K(\mathcal A^{J_1})\times K(\mathcal A^{J_2})\) with the quasi-isomorphisms of the product being the pairs of quasi-isomorphisms. A roof in the product is a pair of roofs, and refinements are pairs of refinements, so the roof category of the product is the product of the roof categories. Hence restriction is an isomorphism \(D(\mathcal A^{J_1\sqcup J_2})\to D(\mathcal A^{J_1})\times D(\mathcal A^{J_2})\). The category \(D(\mathcal A^{\emptyset})\) has the zero complex. (Der2): let \(\varphi\) be a morphism of \(D(\mathcal A^J)\), represented by a roof \(X\xleftarrow{s}M\xrightarrow{f}Y\). It is invertible exactly when \(f\) is a quasi-isomorphism, since \(Q(s)\) is invertible and the functors \(H^n\) descend to \(D(\mathcal A^J)\) (Theorem 5.1 of *Complexes, cones and localization*). The component \(\varphi_j\) is represented by the roof of the \(j\)-components. If every \(\varphi_j\) is invertible, every \(f_j\) is a quasi-isomorphism; cohomology in \(\mathcal A^J\) is computed objectwise, so \(f\) is a quasi-isomorphism and \(\varphi\) is invertible.

## Sources

- [PS] A. Grothendieck, *Pursuing Stacks (À la poursuite des champs). First episode: the modelizing story* (typescript, 1983), §69; public-domain edition by the scrivener (2015), extended by M. Carmona with U. Buchholtz. arXiv:2111.01000. https://arxiv.org/abs/2111.01000
- [Gr] M. Groth, *Derivators, pointed derivators and stable derivators*, Algebraic & Geometric Topology 13 (2013), 313–374; arXiv:1112.3840. https://arxiv.org/abs/1112.3840 — the axioms are stated there in the form used here, with the base change morphisms of Section 3.
