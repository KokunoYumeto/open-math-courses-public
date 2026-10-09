# Fréchet spaces of sections and Schwartz's theorem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Sections of a coherent analytic sheaf over an open set form a Fréchet space, and restriction to a relatively compact open subset is a compact operator, by Montel's theorem. L. Schwartz's perturbation theorem turns this compactness into finiteness: if a compact morphism of Fréchet complexes is surjective in cohomology, the target cohomology is finite-dimensional. This lesson builds the topological framework: Fréchet spaces and the open mapping theorem, compact perturbations, an abstract Mittag-Leffler theorem for inverse limits of complexes, the Krull topology on finitely generated modules over \(\mathcal O_n\), and the canonical Fréchet topology on sections of coherent sheaves.

We use Holomorphic functions of several variables (Weierstrass convergence and Montel's theorem), [Coherent sheaves and Oka's coherence theorem](coherent-sheaves-and-okas-theorem.md), Cartan's coherence theorem and complex spaces and [Stein domains in complex space](stein-domains-in-complex-space.md). The Baire category theorem is [Hahn–Banach, Baire and the basic theorems on Banach spaces, Theorem 3.1](course:foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces#OA-FND-HB-03); the Artin–Rees lemma and Krull's intersection theorem are [Stacks, Tags 00IN and 00IP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-Artin-Rees).

Basic references are [Demailly] and [Cartan–Serre 1953].

## 1. Fréchet spaces

A **Fréchet space** is a complete metrizable locally convex topological vector space. Its topology is given by an increasing sequence of seminorms \(p_1\leq p_2\leq\cdots\) and the translation-invariant metric \(d(x,y)=\sum_k2^{-k}\min(1,p_k(x-y))\). Closed subspaces, countable products, and quotients by closed subspaces of Fréchet spaces are Fréchet spaces. Examples: \(\mathcal O(U)\) with uniform convergence on compact sets (Holomorphic functions of several variables, Section 3), and \(\mathcal O(U)^p\).

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

**Proof.** If \(U'=A\cap V'\) with \(V'\subset V\) a smaller Stein domain, restriction \(\mathcal O(V)^{p_0}\to\mathcal O(V')^{p_0}\) is continuous, so \(\mathcal S(U)\to\mathcal S(U')\) is continuous. A covering of \(U\) by countably many such \(U'_\alpha\) gives an injection of \(\mathcal S(U)\) onto the closed subspace of compatible families in \(\prod\mathcal S(U'_\alpha)\); the induced topology is coarser than the quotient topology and Fréchet, so by Theorem 1.1 the two coincide. Other generators \(H_1,\ldots,H_{p'}\) of \(i_*\mathcal S\) near a point are expressed in terms of the first ones and conversely, on small standard sets, giving continuous maps \(\mathcal O^{p'}\to\mathcal O^{p_0}\) and back compatible with the surjections onto \(\mathcal S\); so the quotient topologies agree there. A change of local embedding is reduced, near each point, to comparing an embedding with its composite with \(\Omega'\hookrightarrow\Omega'\times\mathbf C^{N-d}\), for which the quotient maps correspond under the open restriction \(\mathcal O(V'\times\mathbf C^{N-d})\to\mathcal O(V')\) to the slice. Covering by small standard sets and the closed-subspace argument above then give independence in general. For arbitrary \(W\), the image of \(\mathcal S(W)\) in a countable product is closed (sheaf axiom and continuity of restrictions), hence Fréchet; two coverings have a common refinement, and Theorem 1.1 shows that the topologies coincide. \(\square\)

**Proposition 5.2.** Let \(\mathcal S\) be coherent on \(X\).

1. For every \(x\in W\), the map \(\mathcal S(W)\to\mathcal S_x\) is continuous for the Krull topology of the finitely generated \(\mathcal O_{X,x}\)-module \(\mathcal S_x\).
2. If \(\mathcal S'\subset\mathcal S\) is a coherent subsheaf, \(\mathcal S'(W)\) is closed in \(\mathcal S(W)\). A morphism of coherent sheaves induces continuous maps on sections, and restriction maps are continuous.
3. If \(W'\subset W\) is open with compact closure \(\overline{W'}\subset W\), the restriction \(\mathcal S(W)\to\mathcal S(W')\) is compact.

**Proof.** (1) On a standard \(U=A\cap V\ni x\), the composite \(\mathcal O(V)^{p_0}\to\mathcal O_x^{p_0}\to\mathcal S_x\) is continuous for the Krull topologies (Section 4), and \(\mathcal S(U)\) carries the quotient topology. (2) The first claim follows from (1) and Proposition 4.1 applied to \(\mathcal S'_x\subset\mathcal S_x\). For a morphism \(\mathcal S\to\mathcal S'\), near each point choose generators of \(\mathcal S'\) extending the images of generators of \(\mathcal S\); on small standard sets the morphism is induced by the inclusion \(\mathcal O^{p_0}\to\mathcal O^{p'_0}\). Continuity of restriction was shown in Proposition 5.1. (3) For standard \(U'=A\cap V'\subset U=A\cap V\) with \(\overline{V'}\) compact in \(V\), restriction \(\mathcal O(V)^{p_0}\to\mathcal O(V')^{p_0}\) is compact by Montel's theorem, hence so is \(\mathcal S(U)\to\mathcal S(U')\). In general cover \(\overline{W'}\) by finitely many standard \(U'_\alpha\) with closures in standard \(U_\alpha\subset W\); then \(\mathcal S(W)\to\mathcal S(W')\) factors as \(\mathcal S(W)\to\prod\mathcal S(U_\alpha)\to\prod\mathcal S(U'_\alpha)\) followed by the topological embedding of \(\mathcal S(W')\) into the product of the \(\mathcal S(W'\cap U'_\alpha)\), and the middle arrow is compact. \(\square\)

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
