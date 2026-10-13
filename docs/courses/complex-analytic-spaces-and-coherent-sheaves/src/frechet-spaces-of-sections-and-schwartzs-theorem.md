# Fréchet spaces of sections and Schwartz's theorem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

*Section 5 comparison and compact-restriction proofs completed by GPT-6 Astra (OpenAI), Ultra, 12 October 2026. Author self-check; independent review not claimed. CC0.*

Sections of a coherent analytic sheaf over an open set form a Fréchet space, and restriction to a relatively compact open subset is a compact operator, by Montel's theorem. L. Schwartz's perturbation theorem turns this compactness into finiteness: if a compact morphism of Fréchet complexes is surjective in cohomology, the target cohomology is finite-dimensional. This lesson builds the topological framework: Fréchet spaces and the open mapping theorem, compact perturbations, an abstract Mittag-Leffler theorem for inverse limits of complexes, the Krull topology on finitely generated modules over \(\mathcal O_n\), and the canonical Fréchet topology on sections of coherent sheaves.

We use [Holomorphic functions of several variables](holomorphic-functions-of-several-variables.md) (Weierstrass convergence and Montel's theorem), [Coherent sheaves and Oka's coherence theorem](coherent-sheaves-and-okas-theorem.md), [Cartan's coherence theorem and complex spaces](cartans-coherence-theorem-and-complex-spaces.md) and [Stein domains in complex space](stein-domains-in-complex-space.md). The Baire category theorem is [Hahn–Banach, Baire and the basic theorems on Banach spaces, Theorem 3.1](course:foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces#OA-FND-HB-03); the Artin–Rees lemma and Krull's intersection theorem are [Stacks, Tags 00IN and 00IP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-Artin-Rees).

Basic references are [Demailly] and [Cartan–Serre 1953].

## 1. Fréchet spaces

A **Fréchet space** is a complete metrizable locally convex topological vector space. Its topology is given by an increasing sequence of seminorms \(p_1\leq p_2\leq\cdots\) and the translation-invariant metric \(d(x,y)=\sum_k2^{-k}\min(1,p_k(x-y))\). Closed subspaces, countable products, and quotients by closed subspaces of Fréchet spaces are Fréchet spaces. Examples: \(\mathcal O(U)\) with uniform convergence on compact sets ([Holomorphic functions of several variables, Section 3](holomorphic-functions-of-several-variables.md#3-limits-the-space-of-holomorphic-functions-and-montel-s-theorem)), and \(\mathcal O(U)^p\).

**Theorem 1.1 (open mapping theorem).** A continuous linear surjection \(A:E\to F\) between Fréchet spaces is open. A continuous linear bijection between Fréchet spaces is a topological isomorphism.

**Proof.** Let \(B_r=\{x:\ d(x,0)<r\}\); these are balanced, \(B_r+B_r\subset B_{2r}\), and \(d(\sum x_k,0)\leq\sum d(x_k,0)\). Fix \(r>0\). Since \(F=\bigcup_mm\,A(B_{r})\) and \(F\) is complete, the Baire category theorem shows that some \(m\,\overline{A(B_r)}\), hence \(\overline{A(B_r)}\), has interior points; since \(\overline{A(B_r)}-\overline{A(B_r)}\subset\overline{A(B_{2r})}\), the set \(\overline{A(B_{2r})}\) is a neighbourhood of \(0\). Applying this with \(r=2^{-k-1}\varepsilon\), choose neighbourhoods \(W_k\subset\overline{A(B_{2^{-k}\varepsilon})}\) of \(0\), shrinking to \(0\). Let \(y\in W_0\). Choose \(x_0\in B_\varepsilon\) with \(y-Ax_0\in W_1\), then \(x_1\in B_{\varepsilon/2}\) with \(y-Ax_0-Ax_1\in W_2\), and so on. The series \(\sum x_k\) converges, by completeness, to some \(x\) with \(d(x,0)<2\varepsilon\), and \(Ax=y\) by continuity. So \(A(B_{2\varepsilon})\supset W_0\), and \(A\) is open. \(\square\)

**Definition 1.2.** Let \(E,F\) be Fréchet spaces and \(g:E\to F\) continuous and linear. Then \(g\) is a **quasi-epimorphism** if \(g(E)\) is closed of finite codimension, and \(g\) is **compact** if some neighbourhood of \(0\) in \(E\) has relatively compact image.

**Lemma 1.3.** \(g:E\to F\) is a quasi-epimorphism as soon as \(g(E)\) has finite codimension, and \(g\) is then open onto \(g(E)\).

**Proof.** Let \(S\) be a finite-dimensional complement of \(g(E)\). The map \(E/\ker g\oplus S\to F\), \((\tilde x,y)\mapsto g(x)+y\), is a continuous linear bijection of Fréchet spaces (\(\ker g\) is closed), hence a topological isomorphism by Theorem 1.1. So \(g(E)\), the image of the closed subspace \(E/\ker g\oplus0\), is closed, and \(g\) is open onto it. \(\square\)

## 2. Schwartz's theorem

**Theorem 2.1 (L. Schwartz).** Let \(E,F\) be Fréchet spaces, \(g:E\to F\) a quasi-epimorphism and \(h:E\to F\) compact. Then \(g+h\) is a quasi-epimorphism.

**Proof.** Let \(U\) be an open convex balanced neighbourhood of \(0\) with \(K=\overline{h(U)}\) compact. Replacing \(F\) by \(F/S\) for a finite-dimensional complement \(S\) of \(g(E)\), we may assume \(g\) surjective; then \(V=g(U)\) is an open convex neighbourhood of \(0\) (Theorem 1.1). By compactness, \(K\subset\bigcup_{j\leq N}(b_j+\tfrac12V)\) for some \(b_j\in K\); replacing \(F\) by its quotient by the span of the \(b_j\), we may assume \(K\subset\tfrac12V\). It suffices to show that \(f=g+h\) is now surjective, since then the original \(g+h\) has image of finite codimension and Lemma 1.3 applies.

Let \(y_0\in V\). Choose \(x_0\in U\) with \(g(x_0)=y_0\); then \(y_1=y_0-f(x_0)=-h(x_0)\in K\subset\tfrac12V\). Inductively choose \(x_\nu\in2^{-\nu}U\) with \(g(x_\nu)=y_\nu\) and set \(y_{\nu+1}=y_\nu-f(x_\nu)=-h(x_\nu)\in2^{-\nu}K\subset2^{-\nu-1}V\). Then \(y_0-f(x_0+\cdots+x_\nu)=y_{\nu+1}\to0\). The choice of the \(x_\nu\) can be made so that \(\sum x_\nu\) converges: let \(U_p\) be a basis of convex neighbourhoods of \(0\) with \(U_{p+1}\subset\tfrac12U_p\). For each \(p\), the compact set \(K\) is covered by the increasing open sets \(g(2^nU_p\cap\tfrac12U)\), \(n\in\mathbf N\), whose union is \(g(\tfrac12U)=\tfrac12V\); so there are \(N(p)\), which we take increasing, with \(K\subset g(2^{N(p)}U_p\cap\tfrac12U)\), hence \(2^{1-\nu}K\subset g(2^{N(p)+1-\nu}U_p\cap2^{-\nu}U)\). Since \(y_\nu\in2^{1-\nu}K\), for \(N(p)<\nu\leq N(p+1)\) we may choose \(x_\nu\in2^{N(p)+1-\nu}U_p\cap2^{-\nu}U\). Then \(x_{N(p)+1}+\cdots+x_{N(p+1)}\in(1+\tfrac12+\cdots)U_p\subset2U_p\), so the series converges to \(x\) with \(f(x)=y_0\). Hence \(f(E)\supset V\), and \(f\) is surjective. \(\square\)

**Theorem 2.2 (finiteness criterion).** Let \(\rho:(E^\bullet,d)\to(F^\bullet,\delta)\) be a morphism of complexes of Fréchet spaces with continuous differentials. If \(\rho^q\) is compact and \(H^q(\rho):H^q(E^\bullet)\to H^q(F^\bullet)\) is surjective, then \(H^q(F^\bullet)\) is finite-dimensional and \(\delta(F^{q-1})\) is closed in \(F^q\).

**Proof.** Consider \(g,h:Z^q(E^\bullet)\oplus F^{q-1}\to Z^q(F^\bullet)\), \(g(x,y)=\rho^q(x)+\delta y\), \(h(x,y)=-\rho^q(x)\), between Fréchet spaces (cocycle spaces are closed). Surjectivity of \(H^q(\rho)\) means that \(g\) is surjective, and \(h\) is compact. By Theorem 2.1, \(g+h=(x,y)\mapsto\delta y\) is a quasi-epimorphism, so \(\delta(F^{q-1})\) is closed and of finite codimension in \(Z^q(F^\bullet)\). \(\square\)

**Remark 2.3.** In the situation of Theorem 2.2 without compactness, if \(H^q(\rho)\) is surjective then the map \(g\) is open by Theorem 1.1, so \(H^q(\rho)\) is open for the quotient topologies; if \(H^q(\rho)\) is bijective it is a homeomorphism.

## 3. An abstract Mittag-Leffler theorem

**Proposition 3.1.** Let \((E^\bullet_\nu)_{\nu\in\mathbf N}\) be complexes of Fréchet spaces with continuous differentials and continuous morphisms \(E^\bullet_{\nu+1}\to E^\bullet_\nu\) with dense image in each degree, and let \(E^\bullet=\varprojlim E^\bullet_\nu\).

1. If all \(H^q(E^\bullet_{\nu+1})\to H^q(E^\bullet_\nu)\) are surjective, then \(H^q(E^\bullet)\to H^q(E^\bullet_0)\) is surjective.
2. If all \(H^q(E^\bullet_{\nu+1})\to H^q(E^\bullet_\nu)\) have dense image, then \(H^q(E^\bullet)\to H^q(E^\bullet_0)\) has dense image.
3. If all \(H^{q-1}(E^\bullet_{\nu+1})\to H^{q-1}(E^\bullet_\nu)\) have dense image and all \(H^q(E^\bullet_{\nu+1})\to H^q(E^\bullet_\nu)\) are injective, then \(H^q(E^\bullet)\to H^q(E^\bullet_0)\) is injective.
4. If \(\phi:F^\bullet\to E^\bullet\) is a morphism of Fréchet complexes with dense image in each degree and every \(H^q(F^\bullet)\to H^q(E^\bullet_\nu)\) has dense image, then \(H^q(F^\bullet)\to H^q(E^\bullet)\) has dense image.

Here density in cohomology refers to the quotient topology on cocycles modulo coboundaries.

**Proof.** For \(x\) in \(E^\bullet\) or in \(E^\bullet_\mu\), \(\mu\geq\nu\), write \(x^\nu\) for its image in \(E^\bullet_\nu\). Choose translation-invariant metrics \(d_\nu\) defining the topologies, replaced by \(\max_{\mu\leq\nu}d_\mu(x^\mu,y^\mu)\), so that all maps \(E_{\nu+1}\to E_\nu\) have Lipschitz constant \(1\). Elements of \(E^\bullet\) are sequences \((x_\nu)\) with \(x_{\nu+1}^\nu=x_\nu\), and a sequence \((\xi_\nu)\) with \(\xi_\nu\in E_\nu\) and \(d_\nu(\xi_{\nu+1}^\nu,\xi_\nu)\leq2^{-\nu}\) defines an element of \(E^\bullet\) as the limit of the images of the \(\xi_\mu\), by completeness.

(1) Let \(x_0\in Z^q(E_0)\). Inductively choose \(x_{\nu+1}\in Z^q(E_{\nu+1})\) with \(x^\nu_{\nu+1}=x_\nu+\delta y_\nu\), \(y_\nu\in E^{q-1}_\nu\). Using density, replace \(x_{\nu+1}\) by \(x_{\nu+1}-\delta\tilde y_{\nu+1}\), where \(\tilde y_{\nu+1}\in E^{q-1}_{\nu+1}\) has image close to \(y_\nu\); so we may assume \(d_\nu(y_\nu,0)\) and \(d_\nu(\delta y_\nu,0)\) are at most \(2^{-\nu}\). Then \((x_\nu)\) defines \(\xi\in Z^q(E^\bullet)\) with \(\xi^0=x_0+\delta\sum_\nu y_\nu^0\).

(2) The density assumption implies that \(Z^q(E_{\nu+1})\to Z^q(E_\nu)\) has dense image: given \(x\in Z^q(E_\nu)\), approximate its class by the class of some \(x'^\nu\), \(x'\in Z^q(E_{\nu+1})\), so \(x\approx x'^\nu+\delta y\) with \(y\in E^{q-1}_\nu\), and approximate \(y\) by an image. Then build a sequence as above converging within \(\varepsilon\) of a given \(x_0\).

(3) Let \(x\in Z^q(E^\bullet)\) with \(x^0\) exact. By injectivity each \(x^\nu\) is exact, \(x^\nu=\delta y_\nu\) with \(y_\nu\in E^{q-1}_\nu\). Then \(z_\nu=y^\nu_{\nu+1}-y_\nu\) is a cocycle of \(E_\nu\). By the density assumption in degree \(q-1\) there are \(z'\in Z^{q-1}(E_{\nu+1})\) and \(w\in E^{q-2}_\nu\) with \(z'^\nu\) close to \(z_\nu+\delta w\); choose \(\tilde w\in E^{q-2}_{\nu+1}\) with \(\tilde w^\nu\) close to \(w\), and replace \(y_{\nu+1}\) by \(y_{\nu+1}-z'+\delta\tilde w\). This does not change \(\delta y_{\nu+1}=x^{\nu+1}\), and makes \(d_\nu(y^\nu_{\nu+1},y_\nu)\leq2^{-\nu}\). Proceeding inductively, the \(y_\nu\) define \(y\in E^{q-1}\) with \(\delta y=x\).

(4) For a class in \(H^q(E^\bullet)\) represented by \(\xi\), there are \(x_\nu\in Z^q(F^\bullet)\) and \(z_\nu\in E^{q-1}_\nu\) with \(d_\nu(\xi^\nu,\phi(x_\nu)^\nu+\delta z_\nu)\to0\). Approximate \(z_\nu\) by \(\phi(w_\nu)^\nu\), \(w_\nu\in F^{q-1}\), and replace \(x_\nu\) by \(x_\nu+\delta w_\nu\); then \(\phi(x_\nu)\to\xi\) in \(E^\bullet\). \(\square\)

*Reference:* the arrangement of Sections 1–3 follows [Demailly], who credits Theorem 2.1 to L. Schwartz and Theorem 2.2 to H. Cartan and J.-P. Serre [Cartan–Serre 1953].

## 4. The Krull topology on modules over \(\mathcal O_n\)

Let \(E\) be a finitely generated \(\mathcal O_n\)-module, \(\mathfrak m=\mathfrak m_n\). Each \(E/\mathfrak m^kE\) is a finite-dimensional vector space, and by Krull's intersection theorem \(\bigcap_k\mathfrak m^kE=0\) [Stacks, Tag 00IP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-intersect-powers-ideal-module-zero). So \(E\) embeds into \(\prod_kE/\mathfrak m^kE\); the induced topology is the **Krull topology**. On \(\mathcal O_n\) it is the topology of convergence of each Taylor coefficient. Module homomorphisms are continuous for it, since they induce linear maps on the finite-dimensional quotients.

**Exact programme inputs.** Complete proofs are provided by [Noetherian and Artinian rings, Theorem 5.1 (Artin–Rees)](course:AG-CA/AG-CA-03#5-intersecting-a-filtration-with-a-submodule) and [Theorem 6.1 (Krull intersection)](course:AG-CA/AG-CA-03#6-what-can-survive-every-power). Their finite-generation and polynomial-ring inputs are proved in Sections 1–2 of that lesson. The determinant argument and Nakayama's lemma are proved in [Localization, local properties and support, Lemma 4.1 and Theorem 4.2](course:AG-CA/AG-CA-02#4-finite-generators-near-a-point). The Stacks references above remain the human-source comparisons.

**Application to possibly nonreduced spaces.** For an analytic space and a point \(x\), its local ring \(R=\mathcal O_{X,x}\) is a quotient of a Noetherian local ring of holomorphic germs, and the stalk \(M=\mathcal F_x\) of a coherent sheaf is a finite \(R\)-module. Use the local-ring case of Theorem 6.1 with \(I=\mathfrak m_x=\operatorname{Jac}(R)\): it gives \(\bigcap_{k\geq1}\mathfrak m_x^kM=0\). No reducedness, domain, torsion-freeness or freeness assumption is needed. The same conclusion applies to a finite quotient stalk, as used in Proposition 4.1. In local coordinates, \(R/\mathfrak m_x^k\) is a quotient of the finite-dimensional space of polynomials of degree less than \(k\), so \(M/\mathfrak m_x^kM\) is finite-dimensional too. This proves the finite-jet separation used in Section 5; it does not assert that the module is complete for its ideal-adic topology.

**Proposition 4.1.** If \(E\subset F\) are finitely generated \(\mathcal O_n\)-modules, then \(E\) is closed in \(F\) for the Krull topology of \(F\).

**Proof.** The image of the closure \(\overline E\) in the finite-dimensional space \(F/\mathfrak m^kF\) lies in the closure of the image of \(E\), which is the image itself; so \(\overline E\subset E+\mathfrak m^kF\) for every \(k\). By Krull's intersection theorem applied to \(F/E\), \(\bigcap_k(E+\mathfrak m^kF)=E\). \(\square\)

A sequence \(f_\nu\in\mathcal O(U)\) converging uniformly on compact sets converges at each \(x\in U\) in the Krull topology of \(\mathcal O_x\), because the Taylor coefficients converge by the Cauchy estimates. Consequently, for a coherent subsheaf \(\mathcal Z\subset\mathcal O^p_U\), the space \(\mathcal Z(U)\) is closed in \(\mathcal O(U)^p\): a uniform limit on compact sets of sections of \(\mathcal Z\) has germs in the Krull-closed submodules \(\mathcal Z_x\subset\mathcal O_x^p\).

## 5. The topology on sections of coherent sheaves

Let \(X\) be a complex space and \(\mathcal S\) a coherent \(\mathcal O_X\)-module. Call an open set \(U\subset X\) **standard** if it is of the form \(U=A\cap V\), where \(A\subset\Omega\subset\mathbf C^N\) is a distinguished patch for \(\mathcal S\) (Definition 4.2 of the previous lesson) with resolution beginning \(\mathcal O_\Omega^{p_0}\to i_*\mathcal S\to0\), and \(V\subset\Omega\) is a Stein domain. By Proposition 4.3 of the previous lesson, the sequence

\[
0\longrightarrow\mathcal Z_0(V)\longrightarrow\mathcal O(V)^{p_0}\longrightarrow\mathcal S(U)\longrightarrow0
\tag{5.1}
\]

is exact, and \(\mathcal Z_0(V)\) is closed by Section 4. Give \(\mathcal S(U)\) the quotient Fréchet topology.

**Proposition 5.1.** This topology does not depend on the choices. For an arbitrary open set \(W\subset X\), the topology on \(\mathcal S(W)\) induced by the injection \(\mathcal S(W)\to\prod_\alpha\mathcal S(U_\alpha)\), for any countable covering of \(W\) by standard open sets, is a Fréchet topology independent of the covering, and it agrees with the previous one when \(W\) is standard.

**Proof.** We first make the maps between different presentations explicit. We then use finite jets to prove closedness and independence without presupposing continuity of restriction on arbitrary intersections.

**Intrinsic finite jets.** For a standard model \(U=A\cap V\), write \(q_V:\mathcal O(V)^p\twoheadrightarrow\mathcal S(U)\) for (5.1). At \(x\in U\), let \(\mathfrak m_x\) be the maximal ideal of \(\mathcal O_{X,x}\). For every \(k\geq1\), the map
\[
j_{x,k}:\mathcal S(U)\longrightarrow
\mathcal S_x/\mathfrak m_x^k\mathcal S_x,\qquad
s\longmapsto s_x\bmod\mathfrak m_x^k\mathcal S_x
\]
is continuous. Indeed, after composition with \(q_V\), it depends only on the Taylor coefficients of order less than \(k\) of the \(p\) ambient holomorphic functions at the point representing \(x\). The ambient maximal ideal maps onto \(\mathfrak m_x\); multiplication by the chosen section generators therefore gives a well-defined linear map from the finite-dimensional ambient jet space to this quotient. Taylor coefficients are continuous by the Cauchy estimates, and continuity descends through the quotient map \(q_V\). These intrinsic jets separate germs: \(\bigcap_k\mathfrak m_x^k\mathcal S_x=0\) by Krull's intersection theorem, since the analytic local ring is Noetherian and the stalk is finite over it. This argument does not require \(X\) to be reduced.

**Explicit local comparison.** Suppose \(i:U_i\hookrightarrow\Omega\subset\mathbf C^N\) and \(j:U_j\hookrightarrow\Xi\subset\mathbf C^M\) are two closed analytic models around \(x\), equipped with finite generators \(s_1,\ldots,s_p\) and \(t_1,\ldots,t_r\) of \(\mathcal S\). Choose a Stein neighbourhood \(V_j\subset\Xi\) of \(j(x)\) on which the second quotient presentation is valid. Each coordinate section \(j_\ell\) on the common complex-space neighbourhood has, near \(i(x)\), a holomorphic lift \(F_\ell\), by the quotient description of the structure sheaf. Shrink the ambient neighbourhood so that
\[
F=(F_1,\ldots,F_M):\Omega_0\longrightarrow V_j
\]
is holomorphic and \(A\cap\Omega_0\) lies in the common neighbourhood. The restriction of \(F\) to that complex subspace is the transition morphism \(j\circ i^{-1}\), not just its map on points. To check this on a holomorphic germ \(f\), use its Taylor polynomial of each finite order at \(j(x)\). Both pullbacks agree on the coordinate germs and hence on that polynomial; the remaining difference belongs to every power of \(\mathfrak m_x\), so vanishes by Krull intersection. The same argument at every point after shrinking establishes the sheaf identity.

At \(x\), write \(t_b=\sum_a c_{ab}s_a\) in \(\mathcal S_x\). The finitely many coefficient germs and these finitely many identities extend to a common neighbourhood. Lift the coefficients to holomorphic functions \(\widetilde c_{ab}\) in the first ambient model and choose a sufficiently small Stein ball \(D\subset\Omega_0\) on which all of them are defined. The comparison on presenting spaces is
\[
T:\mathcal O(V_j)^r\longrightarrow\mathcal O(D)^p,\qquad
(Tf)_a=\sum_{b=1}^r\widetilde c_{ab}(f_b\circ F).
\tag{5.2}
\]
This map is continuous: for every compact \(K\subset D\), \(F(K)\) is compact in \(V_j\), and
\[
\sup_K |(Tf)_a|
\leq\sum_{b=1}^r\sup_K|\widetilde c_{ab}|\,
                  \sup_{F(K)}|f_b|.
\]
Let \(U_D=A\cap D\) and let \(R:\mathcal S(j^{-1}(V_j))\to\mathcal S(U_D)\) be restriction, identifying the common models by their actual complex-space morphism. The square commutes in the precise sense
\[
q_D T=R q_{V_j}.
\tag{5.3}
\]
The equality follows from the generator identities and the structure-sheaf pullback just proved. Since \(q_{V_j}\) is a quotient surjection, (5.3) proves continuity of \(R\) for the two displayed quotient topologies. Reversing the roles of the embeddings gives the comparison in the other direction on smaller neighbourhoods. Neither equal ambient dimensions nor an invertible ambient map is required. Taking \(F\) to be the identity gives the change-of-generators comparison and nested same-chart restriction as special cases.

The sheaf qualification matters. On the one-point complex space with local ring \(\mathbf C[\varepsilon]/(\varepsilon^2)\), the embeddings given by the coordinate images \(\varepsilon\) and \((\varepsilon,\varepsilon)\) have comparison \(F(z)=(z,z)\). The map \((z,0)\) agrees with it on the underlying point but not on the second coordinate in the structure sheaf. Such a map would not satisfy (5.3).

**Closed compatible families.** Choose a countable standard cover \((U_\alpha)\) of an arbitrary \(W\), with any of the quotient presentations above. In the Fréchet product \(P=\prod_\alpha\mathcal S(U_\alpha)\), define
\[
C=\left\{(s_\alpha)\in P:
 j_{x,k}(s_\alpha)-j_{x,k}(s_\beta)=0
 \text{ for all }\alpha,\beta,\ x\in U_\alpha\cap U_\beta,\ k\geq1\right\}.
\]
Each difference is a continuous linear map to a finite-dimensional Hausdorff space, so \(C\) is an intersection of closed kernels. It is therefore a closed Fréchet subspace of \(P\). The jet-separation statement implies that its families agree as germs on every overlap, hence agree as sections there. The sheaf gluing and uniqueness axioms give a linear bijection \(\mathcal S(W)\to C\). Transport the topology of \(C\) to \(\mathcal S(W)\). This proves completeness and metrizability without any assumption about the topology of the overlaps.

For clarity, the closed-graph consequence of Theorem 1.1 used next needs no extra functional-analytic input. If \(L:E\to F\) is a linear map of Fréchet spaces with closed graph \(G\subset E\times F\), then \(G\) is Fréchet and its first projection \(G\to E\) is a continuous linear bijection. Its inverse is continuous by Theorem 1.1, and composition with the second projection proves that \(L\) is continuous.

Now take two countable standard covers of \(W\), producing spaces \(C\) and \(C'\). They are linearly identified by their glued sections. The graph of this identification is closed: for every member of each cover, every point of their intersection, and every positive jet order, impose equality of the two intrinsic jets. These are closed linear conditions; jet separation and sheaf uniqueness identify their joint solution set with the graph. The preceding closed-graph argument makes the identification continuous, and Theorem 1.1 makes its inverse continuous. If \(W\) itself is standard, apply exactly this argument to its single quotient space and the family space \(C\). It proves agreement with the quotient topology, including when two different models present the same standard open set.

Finally, for any open inclusion \(W'\subset W\), restriction \(\mathcal S(W)\to\mathcal S(W')\) has closed graph by the same jet test, now only at points of \(W'\). Both section spaces are Fréchet by the construction, so restriction is continuous. Countability is used only for the chosen products; the test for closedness may use arbitrarily many closed kernels. The countable-atlas convention for complex spaces in this course supplies these covers. \(\square\)

**Proposition 5.2.** Let \(\mathcal S\) be coherent on \(X\).

1. For every \(x\in W\), the map \(\mathcal S(W)\to\mathcal S_x\) is continuous for the Krull topology of the finitely generated \(\mathcal O_{X,x}\)-module \(\mathcal S_x\).
2. If \(\mathcal S'\subset\mathcal S\) is a coherent subsheaf, \(\mathcal S'(W)\) is closed in \(\mathcal S(W)\). A morphism of coherent sheaves induces continuous maps on sections, and restriction maps are continuous.
3. If \(W'\subset W\) is open with compact closure \(\overline{W'}\subset W\), the restriction \(\mathcal S(W)\to\mathcal S(W')\) is compact.

**Proof.** (1) The intrinsic finite-jet maps constructed in Proposition 5.1 are continuous on standard opens. Restricting from \(W\) to one of them proves continuity of every \(\mathcal S(W)\to\mathcal S_x/\mathfrak m_x^k\mathcal S_x\), hence of the map to the stalk with its Krull topology.

(2) Proposition 4.1 applied over the analytic local ring shows that \(\mathcal S'_x\subset\mathcal S_x\) is Krull-closed; equivalently apply its proof to the finite module \(\mathcal S_x/\mathcal S'_x\). The space \(\mathcal S'(W)\) is the intersection, over \(x\in W\), of the inverse images of these closed submodules under the continuous germ maps. It is therefore closed. For a coherent-sheaf morphism \(\phi:\mathcal S\to\mathcal T\), its stalk map induces continuous linear maps on all finite jets. The graph of \(\phi_W:\mathcal S(W)\to\mathcal T(W)\) is the intersection of the conditions
\[
t_x-\phi_x(s_x)=0
   \quad\hbox{in }\mathcal T_x/\mathfrak m_x^k\mathcal T_x
   \qquad(x\in W,\ k\geq1).
\]
It is closed by jet continuity and Krull intersection, so \(\phi_W\) is continuous by the closed-graph argument in Proposition 5.1. More concretely, on a sufficiently small common model write the images of the finitely many generators of \(\mathcal S\) as linear combinations of generators of \(\mathcal T\); lifting the coefficients gives a holomorphic matrix between the two presenting free modules, compatible with the quotient maps. Arbitrary restrictions were proved continuous at the end of Proposition 5.1.

(3) First take \(U=A\cap V\) and \(U'=A\cap V'\), where \(V,V'\) are Stein, \(\overline{V'}\) is compact in \(V\), and both use the same finite presentation. The ambient restriction
\[
T:\mathcal O(V)^p\longrightarrow\mathcal O(V')^p
\]
is compact: choose a compact neighbourhood of \(\overline{V'}\) in \(V\). A uniform bound there defines a zero-neighbourhood in \(\mathcal O(V)^p\), whose image is locally bounded on \(V'\); Montel's theorem gives compact closure of that image in \(\mathcal O(V')^p\). Write \(q\) and \(q'\) for the two quotient maps and \(R:\mathcal S(U)\to\mathcal S(U')\) for restriction. Then \(Rq=q'T\). If \(N\) is a zero-neighbourhood whose \(T\)-image has compact closure, the open quotient map \(q\) makes \(q(N)\) a zero-neighbourhood and
\[
R(q(N))\subset q'\bigl(\overline{T(N)}\bigr).
\]
The set on the right is compact, and the target is Hausdorff, so \(R\) is compact. No continuous right inverse or bounded lifting of the quotient map is being assumed.

For general \(W'\Subset W\), choose finitely many nested same-chart standard opens \(U'_\alpha\subset U_\alpha\subset W\), whose ambient Stein domains are relatively compact as above, such that the \(U'_\alpha\) cover \(\overline{W'}\). Such pairs are obtained from nested small balls in distinguished patches at each point of that compact set. Put \(B_\alpha=W'\cap U'_\alpha\). The \(B_\alpha\) need not be standard; their section spaces already have the topology of Proposition 5.1. Define
\[
K:\mathcal S(W)\longrightarrow\prod_{\alpha=1}^m\mathcal S(U'_\alpha),
\qquad K(s)=(s|_{U'_\alpha})_\alpha,
\]
and
\[
L:\prod_{\alpha=1}^m\mathcal S(U'_\alpha)
       \longrightarrow P=\prod_{\alpha=1}^m\mathcal S(B_\alpha),
\qquad L((t_\alpha))=(t_\alpha|_{B_\alpha})_\alpha.
\]
Each component of \(K\) factors through the continuous restriction to \(\mathcal S(U_\alpha)\) and the compact restriction to \(\mathcal S(U'_\alpha)\); it is compact. The finite intersection of the resulting zero-neighbourhoods shows that \(K\) is compact, since the product of their finitely many compact image closures is compact. The map \(L\) is continuous.

The compatible-family image \(C\) of
\(J:\mathcal S(W')\to P\) is closed by the intrinsic jet conditions. The map \(J\) is a continuous bijection onto the Fréchet space \(C\), hence a topological isomorphism by Theorem 1.1. For the desired restriction \(R_W:\mathcal S(W)\to\mathcal S(W')\) we have the correctly directed identity
\[
J R_W=L K.
\tag{5.4}
\]
Choose a zero-neighbourhood \(N_W\) whose image under \(LK\) has compact closure in \(P\). Since \(LK(N_W)\subset C\) and \(C\) is closed, that closure is a compact subset of \(C\). Its image under the continuous inverse \(J^{-1}:C\to\mathcal S(W')\) contains \(R_W(N_W)\) and is compact. This proves the asserted compactness. \(\square\)

**The comparison used here.** Theorem 3.2 of [Čech cohomology](course:AG-QC/cech-cohomology#3-comparing-overlaps-with-derived-cohomology) proves the acyclic-cover comparison for sheaves of modules on any ringed space: if every nonempty finite intersection has vanishing higher cohomology, its Čech complex computes sheaf cohomology. The proof uses the injective-resolution double complex and applies to countable covers as well as finite ones. Refinement acts on that double complex by restriction and commutes with its augmentation from global sections of the injective resolution. Consequently the comparison intertwines refinement with the identity on sheaf cohomology. [Theorem 2.1 of the same lesson](course:AG-QC/cech-cohomology#2-a-smaller-complex-without-repeated-indices) identifies the full complex with the ordered complex, without division by factorials. Thus either convention gives the comparison below. Continuity of the component restrictions gives continuity of the Čech maps in the product topologies; the separate open-mapping argument in Remark 2.3 supplies the topological conclusion. The Stacks reference below remains a source comparison, alongside these programme proofs.

**Cohomology on manifolds.** Let \(X\) be a complex manifold. A **Leray covering** for \(\mathcal S\) is a countable open covering \(\mathcal W=(W_\alpha)\) of an open set by standard sets, each in a coordinate chart with a finite free resolution of \(\mathcal S\) on the chart. Each finite intersection \(W_{\alpha_0\ldots\alpha_k}\) is a Stein open subset of \(X\) (Proposition 2.2(4) of the lesson on Stein manifolds) contained in the chart of \(W_{\alpha_0}\), hence a Stein domain there, so \(H^j(W_{\alpha_0\ldots\alpha_k},\mathcal S)=0\) for \(j\geq1\) by Theorem 4.1 of the previous lesson. By [Stacks, Tag 01ET](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-lemma-cech-spectral-sequence-application), the Čech complex \(C^\bullet(\mathcal W,\mathcal S)\), a complex of Fréchet spaces (countable products of Fréchet spaces) with continuous differentials, computes \(H^\bullet(W,\mathcal S)\). The quotient topology on \(H^q(W,\mathcal S)\) does not depend on the Leray covering, by Remark 2.3 applied to refinement maps, which induce bijections in cohomology. These groups need not be Hausdorff.

## 6. Exercises

**Exercise 6.1.** Show that the restriction map \(\mathcal O(\Delta(0;1))\to\mathcal O(\Delta(0;\tfrac12))\) on the unit disc is compact but not surjective, and that its image is dense.

*Solution.* Compactness is Montel's theorem: the neighbourhood \(\{f:\ \sup_{|z|\leq3/4}|f|<1\}\) maps to a locally bounded set on the smaller disc. The function \(1/(z-\tfrac34)\) is holomorphic on the smaller disc but not the restriction of a holomorphic function on the unit disc. The Taylor polynomials of any \(f\) on the smaller disc are restrictions of entire functions and converge to \(f\) uniformly on compact subsets, so the image is dense.

**Exercise 6.2.** Show that the submodule \(\mathcal O_1\cdot z\subset\mathcal O_1\) is closed for the Krull topology but that \(\mathcal O_1\) is not complete for it.

*Solution.* \(\mathcal O_1\cdot z\) is the set of germs with zero constant term, closed since evaluation of the constant coefficient is continuous; this is also Proposition 4.1. The sequence of polynomials \(\sum_{k\leq\nu}k!\,z^k\) is Cauchy for the Krull topology, each coefficient being eventually constant, but its only possible limit is the divergent series \(\sum k!z^k\), which is not a convergent power series.

**Exercise 6.3.** Let \(g:E\to F\) be a quasi-epimorphism and \(h=-g\). Is \(g+h=0\) a quasi-epimorphism, and is \(h\) compact? Reconcile with Theorem 2.1.

*Solution.* \(0\) is a quasi-epimorphism only if \(F\) is finite-dimensional. And \(h=-g\) is compact only if a neighbourhood of \(0\) has relatively compact image under \(g\); if \(g\) is open onto a closed subspace of finite codimension, that subspace would be locally compact, hence finite-dimensional. So when \(F\) is infinite-dimensional, \(h\) is not compact, and there is no contradiction.

## References

- [Demailly] J.-P. Demailly, *Complex Analytic and Differential Geometry*, version of 21 June 2012, freely available from the author with permission to copy, modify and redistribute with credit. <https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf>
- [Cartan–Serre 1953] H. Cartan and J.-P. Serre, Un théorème de finitude concernant les variétés analytiques compactes, *Comptes Rendus de l'Académie des Sciences de Paris* 237 (1953), 128–130.
- [Stacks] The Stacks project, cited by tag; each tag links to the same result in the AI Integrated Stacks Project. <https://stacks.math.columbia.edu/>
