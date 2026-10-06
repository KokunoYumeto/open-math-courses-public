# Reduced crossed products and Fell's absorption principle

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The full crossed product records every covariant representation of an action. The reduced crossed product records a regular one: coefficients act differently at each group coordinate, and the group translates those coordinates. This gives a concrete norm on a Hilbert space. Fell's absorption principle explains why tensoring any covariant representation with the left regular representation produces this regular model.

We assume the integrated-form correspondence and universal construction from [C*-dynamical systems and full crossed products](KT-CP-01.md), together with basic Hilbert-space and C*-algebra theory. We develop the Hilbert-module model explicitly. Basic references are [Connes 1994], [Rosenberg 2012], [Blackadar 2006], and [Gomez Aparicio–Julg–Valette 2019]. The earlier chapter *Covariance and crossed products with nonunital coefficients* gives a separate faithful-representation independence proof; *Unitary representations and the two group C* completions* supplies the free-group norm calculation below.

The main distinction is between embeddings and quotients. Reduced crossed products preserve equivariant embeddings without any amenability assumption. Nevertheless, they can fail to preserve the kernel of a quotient map. These statements concern different parts of an exact sequence. We finish by constructing a finitely generated group with an expander placement and an explicit projection that witnesses this failure. The graph, labelling, diagram and operator arguments are all included.

## Coefficients along a group coordinate

Let \(G\) be a locally compact Hausdorff group with left Haar measure \(ds\), and let \(A\) be a possibly nonunital C*-algebra. Let \(\alpha:G\to\operatorname{Aut}(A)\) be a homomorphism with \(s\mapsto\alpha_s(a)\) norm continuous for every \(a\). No separability, second countability, or unimodularity is assumed. The \(L^2\) spaces below can be defined by completing compact continuous sections, so our calculations start on compact supports.

Our modular convention is

\[
\int_G q(ts)\,dt=\Delta(s)^{-1}\int_G q(t)\,dt.
\]

Coefficients precede group operators. On \(C_c(G,A)\) this gives

\[
(f*g)(t)=\int_G f(s)\alpha_s(g(s^{-1}t))\,ds,
\qquad
f^*(t)=\Delta(t)^{-1}\alpha_t(f(t^{-1})^*).
\tag{1}
\]

A covariant pair \((\pi,U)\) consists of a nondegenerate representation \(\pi:A\to B(H)\) and a strongly continuous unitary representation \(U\), with

\[
U_s\pi(a)U_s^*=\pi(\alpha_s(a)).
\tag{2}
\]

Its integrated form is \((\pi\rtimes U)(f)=\int_G\pi(f(s))U_s\,ds\), interpreted on vectors. These conventions agree with the prerequisite and [Connes 1994].

Given any nondegenerate \(\pi\), put, on \(L^2(G,H)\),

\[
(\widetilde\pi(a)\xi)(t)=\pi(\alpha_{t^{-1}}(a))\xi(t),
\qquad
(\lambda_s\xi)(t)=\xi(s^{-1}t).
\tag{3}
\]

The group coordinate tells us which translate of \(a\) to represent. The inverse in that translate is essential.

**Proposition 2.1 (the regular pair).** Equation (3) defines a nondegenerate covariant pair. Its integrated representation \(R_\pi=\widetilde\pi\rtimes\lambda\) satisfies

\[
(R_\pi(f)\xi)(t)
=\int_G\pi(\alpha_{t^{-1}}(f(s)))\xi(s^{-1}t)\,ds,
\qquad
\|R_\pi(f)\|\leq\|f\|_1.
\tag{4}
\]

**Proof.** Coefficient multiplication is bounded by \(\|a\|\), and multiplication and adjoints hold pointwise. Left Haar invariance makes \(\lambda_s\) unitary with inverse \(\lambda_{s^{-1}}\). Translation is strongly continuous on compact continuous sections: near a fixed \(s\), all supports lie in one compact set and the translated functions converge uniformly there. Density extends continuity to all vectors.

Covariance follows from the order of the two inverses:

\[
\begin{aligned}
(\lambda_s\widetilde\pi(a)\lambda_s^*\xi)(t)
&=\pi(\alpha_{(s^{-1}t)^{-1}}(a))\xi(t)\\
&=\pi(\alpha_{t^{-1}}(\alpha_s(a)))\xi(t).
\end{aligned}
\]

For nondegeneracy take a contractive approximate identity \((e_i)\) of \(A\), and test on \(\xi(t)=h(t)\pi(b)v\), with \(h\in C_c(G)\). The family \(\{\alpha_t(b):t\in\operatorname{supp}h\}\) is compact. Hence \(e_i\alpha_t(b)\to\alpha_t(b)\) uniformly there, and

\[
\pi(\alpha_{t^{-1}}(e_i))\pi(b)
=\pi(\alpha_{t^{-1}}(e_i\alpha_t(b)))
\]

converges uniformly on the support to \(\pi(b)\). These test vectors span a dense subspace. Contractivity gives \(\widetilde\pi(e_i)\to1\) strongly. The integrated-form correspondence gives (4), with its bound obtained by integrating vector norms. The displayed formula is first used on compact test sections and then interpreted as an \(L^2\) identity. \(\square\)

*Reference:* [Blackadar 2006] displays \(\alpha_t(a)\) with left translation, although II.10.3.4 uses (2). For \(\alpha_n(b)(k)=b(k-n)\) on \(c_0(\mathbb Z)\), that choice gives \(\alpha_{t-s}(b)\) where covariance requires \(\alpha_{t+s}(b)\). Equation (3) gives the required pair.

For faithful nondegenerate \(\pi\), \(R_\pi\) is faithful on \(C_c(G,A)\), and its norm is independent of \(\pi\). We use these established facts with precise locators under *What this lesson does not prove*. Define

\[
\|f\|_r=\|R_\pi(f)\|,
\qquad
A\rtimes_{\alpha,r}G=\overline{R_\pi(C_c(G,A))}.
\tag{5}
\]

Equivalently, complete \(C_c(G,A)\) in this norm. The bound \(\|f\|_r\leq\|f\|_u\) gives a surjection

\[
q_A:A\rtimes_\alpha G\longrightarrow A\rtimes_{\alpha,r}G.
\tag{6}
\]

Its range is dense by (5) and closed as the range of a C*-homomorphism. Faithfulness on compact coefficient functions does not imply injectivity of (6) after completion.

## A regular model with no chosen Hilbert space

Start with \(C_c(G,A)\), with right action \((\xi a)(t)=\xi(t)a\) and inner product, linear in the second argument,

\[
\langle\xi,\eta\rangle_A=\int_G\xi(t)^*\eta(t)\,dt.
\tag{7}
\]

Its completion for \(\|\xi\|_E=\|\langle\xi,\xi\rangle_A\|^{1/2}\) is the Hilbert \(A\)-module \(E=L^2(G,A)\). Positivity follows by integration of positive elements; definiteness on continuous sections follows by applying a state detecting a nonzero positive value and using full support of Haar measure. Positivity of Gram matrices, followed by norm approximation of these integrals, gives the module Cauchy–Schwarz inequality. Notice that this norm need not be \((\int\|\xi(t)\|^2dt)^{1/2}\).

Finite sums \(t\mapsto h(t)a\) are dense: approximate a continuous coefficient image on its compact support by finitely many values and a partition of unity, using a compact cutoff. An error of uniform size \(\varepsilon\) on a common compact support \(K\) has module norm at most \(\varepsilon\,\mu(K)^{1/2}\). This identifies \(E\) with the standard module \(L^2(G)\otimes A\).

Write \(\mathcal L_A(E)\) for the C*-algebra of bounded adjointable right \(A\)-linear operators. Define

\[
(M(a)\xi)(t)=\alpha_{t^{-1}}(a)\xi(t),
\qquad
(L_s\xi)(t)=\xi(s^{-1}t).
\tag{8}
\]

**Proposition 2.2 (module realization).** Equation (8) is a nondegenerate covariant pair in \(\mathcal L_A(E)\). Its integrated form \(\Lambda_E\) satisfies

\[
\|\Lambda_E(f)\|=\|f\|_r.
\tag{9}
\]

Thus the reduced crossed product is canonically the closure of \(\Lambda_E(C_c(G,A))\).

**Proof.** The inequality \(a^*a\leq\|a\|^2 1\), in the unitization, gives \(\|M(a)\xi\|_E\leq\|a\|\|\xi\|_E\). Equation (7) gives \(M(a)^*=M(a^*)\) and \(L_s^*=L_{s^{-1}}\). The covariance calculation is the one in Proposition 2.1. Continuity on compact sections gives norm continuity of \(s\mapsto L_s\xi\). An approximate identity acts uniformly on the compact family \(\{\alpha_t(\xi(t))\}\), which proves nondegeneracy of \(M\).

The vector integral

\[
\Lambda_E(f)\xi=\int_G M(f(s))L_s\xi\,ds
\]

is bounded by \(\|f\|_1\|\xi\|_E\). Taking inner products under the integral and using covariance and Haar inversion gives \(\Lambda_E(f)^*=\Lambda_E(f^*)\); the convolution computation gives multiplicativity.

Choose faithful nondegenerate \(\pi:A\to B(H)\). The interior tensor product \(E\otimes_\pi H\) balances \(\xi a\otimes v=\xi\otimes\pi(a)v\), with inner product

\[
\langle\xi\otimes v,\eta\otimes w\rangle
=\langle v,\pi(\langle\xi,\eta\rangle_A)w\rangle.
\]

The map

\[
J(\xi\otimes v)(t)=\pi(\xi(t))v
\tag{10}
\]

preserves inner products and has dense range: it contains \(h(t)\pi(a)v\). Hence it is unitary onto \(L^2(G,H)\). It carries \(M(a)\otimes1\) to \(\widetilde\pi(a)\), \(L_s\otimes1\) to \(\lambda_s\), and \(\Lambda_E(f)\otimes1\) to \(R_\pi(f)\).

The homomorphism \(T\mapsto T\otimes1\) on \(\mathcal L_A(E)\) is faithful. Indeed, if \(T\xi\ne0\), then \(b=\langle T\xi,T\xi\rangle_A\ne0\) is positive. Faithfulness of \(\pi\) supplies \(v\) with \(\langle v,\pi(b)v\rangle>0\), and

\[
\|(T\otimes1)(\xi\otimes v)\|^2=\langle v,\pi(b)v\rangle>0.
\]

An injective C*-homomorphism is isometric. Applying this to \(\Lambda_E(f)\) proves (9). \(\square\)

This explains faithful-representation independence from the module viewpoint: every faithful \(\pi\) measures the norm of the same \(\Lambda_E(f)\). It complements the earlier finite matrix compression proof without requiring that argument again.

If a coefficient representation \(\sigma:A\to B(K)\) is not faithful, the tensor construction is still contractive. If it is degenerate, restrict to \(K_0=\overline{\sigma(A)K}\); it is zero on \(K_0^\perp\). The regular integrated representation is zero on \(L^2(G,K_0^\perp)\) as well. Consequently

\[
\|R_\sigma(f)\|\leq\|f\|_r
\quad\text{for every representation }\sigma.
\tag{11}
\]

## Absorbing a unitary representation

Identify \(H\otimes L^2(G)\) with \(L^2(G,H)\) by \(v\otimes h\mapsto[t\mapsto h(t)v]\). The pair \((\pi\otimes1,U\otimes\lambda)\) then becomes

\[
(P(a)\xi)(t)=\pi(a)\xi(t),
\qquad
(V_s\xi)(t)=U_s\xi(s^{-1}t).
\tag{12}
\]

It is covariant by (2).

**Theorem 2.3 (Fell's absorption principle).** For every nondegenerate covariant pair \((\pi,U)\), the pair (12) is unitarily equivalent to \((\widetilde\pi,\lambda)\). An intertwining unitary is

\[
(W\xi)(t)=U_{t^{-1}}\xi(t),
\qquad
(W^*\eta)(t)=U_t\eta(t).
\tag{13}
\]

**Proof.** Strong continuity of \(U\) makes (13) a compact continuous section when \(\xi\) is one. Continuity follows by first bounding the change in \(\xi(t)\), then applying strong continuity to its fixed value. Unitarity gives

\[
\|W\xi\|_2^2=\int_G\|U_{t^{-1}}\xi(t)\|^2dt=\|\xi\|_2^2.
\]

The formula using \(U_t\) also preserves compact continuous sections and is the inverse there. Both extend isometrically, so \(W\) is surjective and its adjoint has the displayed formula. There is no change of the group variable, hence no modular factor.

For coefficients, covariance gives

\[
(WP(a)W^*\eta)(t)
=U_{t^{-1}}\pi(a)U_t\eta(t)
=\pi(\alpha_{t^{-1}}(a))\eta(t).
\]

For the group operators,

\[
(WV_sW^*\eta)(t)
=U_{t^{-1}}U_sU_{s^{-1}t}\eta(s^{-1}t)
=\eta(s^{-1}t).
\]

These identities extend from a dense subspace. They give \(WP(a)W^*=\widetilde\pi(a)\), \(WV_sW^*=\lambda_s\), and, on integrating,

\[
W(P\rtimes V)(f)W^*=R_\pi(f).
\tag{14}
\]

This proves the assertion. \(\square\)

**Corollary 2.4 (a faithful covariant formula for the reduced norm).** If \(\pi\) is faithful, then

\[
\|f\|_r
=\|((\pi\otimes1)\rtimes(U\otimes\lambda))(f)\|.
\tag{15}
\]

The integrated representation extends faithfully to \(A\rtimes_{\alpha,r}G\).

**Proof.** Equation (14) and the definition give (15). An isometry on the dense coefficient algebra extends isometrically to its completion. \(\square\)

Such pairs exist: start with a faithful coefficient representation and form its regular pair. Its coefficient representation is faithful, since a nonzero positive element gives a nonzero operator at the identity coordinate; continuity on a suitable test vector makes it nonzero on an open set of positive Haar measure.

Without faithfulness, absorption still holds and (11) gives a representation of the reduced algebra. This does not say that the original, untensored \(\pi\rtimes U\) factors through that algebra.

For \(A=\mathbb C\), coefficients are scalar. Thus every strongly continuous unitary representation \(U\) satisfies

\[
U\otimes\lambda\simeq1_H\otimes\lambda,
\qquad
\lambda\otimes U\simeq\lambda\otimes1_H,
\tag{16}
\]

where the second equivalence uses the tensor flip. This is the group version of Fell absorption. It is an equivalence implemented by a unitary, not equality of the original formulas.

## Equivariant maps and their norms

Let \(\varphi:(A,\alpha)\to(B,\beta)\) be an equivariant C*-homomorphism, so \(\varphi\alpha_s=\beta_s\varphi\). It need not be unital or nondegenerate. On compact functions it acts by

\[
(\varphi_c f)(s)=\varphi(f(s)).
\tag{17}
\]

**Theorem 2.5 (reduced functoriality and embeddings).** Equation (17) extends to a homomorphism

\[
\varphi\rtimes_rG:A\rtimes_{\alpha,r}G\longrightarrow B\rtimes_{\beta,r}G.
\]

It is injective if \(\varphi\) is injective and surjective if \(\varphi\) is surjective. These maps preserve identities and composition.

**Proof.** Equation (1) and equivariance show that \(\varphi_c\) preserves products and adjoints. Choose faithful nondegenerate \(\rho:B\to B(K)\). Formula (4) gives

\[
R_\rho^B(\varphi_c f)=R_{\rho\varphi}^A(f).
\tag{18}
\]

By (11) the right side has norm at most \(\|f\|_{r,A}\). This proves contractivity and extension.

Suppose \(\varphi\) is injective. Set \(K_A=\overline{\rho(\varphi(A))K}\). The restriction \(\sigma=(\rho\varphi)|_{K_A}\) is nondegenerate and faithful: \(\rho\varphi\) is faithful on \(K\), and zero on \(K_A^\perp\), so restriction cannot erase a nonzero represented element. Both summands reduce the coefficient operators, and translations preserve their \(L^2\) spaces. Thus (18) decomposes as \(R_\sigma^A(f)\oplus0\), giving

\[
\|\varphi_c f\|_{r,B}=\|R_\sigma^A(f)\|=\|f\|_{r,A}.
\tag{19}
\]

The extension is isometric and injective. This essential-space step handles embeddings that act degenerately on \(K\).

The identity and composition laws hold on compact functions and hence on completions. For surjectivity, finite sums \(s\mapsto h(s)b\) are \(L^1\)-dense on compact supports in \(C_c(G,B)\). Each has a lift \(s\mapsto h(s)a\) if \(\varphi(a)=b\). The image of the completed map is therefore dense and, as a C*-homomorphism's range, closed. \(\square\)

Full crossed products are also functorial. Precompose a covariant pair of \(B\) with \(\varphi\) and restrict to its essential coefficient space if needed. Equivariance makes that space invariant under the group operators. Its orthogonal complement has zero coefficients, so the integrated representation there is zero. The full universal norm therefore gives \(\|\varphi_c f\|_u\leq\|f\|_u\), proving existence of \(\varphi\rtimes G\). This argument does not give isometry for an embedding: the full norm of \(A\) also tests covariant pairs that need not arise by restricting pairs of \(B\).

## A trivial action gives a spatial tensor product

Write \(C_r^*(G)=\overline{\lambda(C_c(G))}\subseteq B(L^2(G))\), where \(\lambda(h)=\int h(s)\lambda_s\,ds\). For nondiscrete groups, individual group unitaries are generally multipliers rather than elements of this algebra. The minimal tensor product is the closure of the algebraic tensor product in faithful spatial representations.

**Theorem 2.6 (trivial action).** There is a canonical isomorphism

\[
A\rtimes_{\mathrm{id},r}G\cong A\otimes_{\min}C_r^*(G),
\tag{20}
\]

sending \(f(s)=h(s)a\) to \(a\otimes\lambda(h)\).

**Proof.** For faithful nondegenerate \(\pi:A\to B(H)\), triviality of the action gives \(\widetilde\pi(a)=\pi(a)\otimes1\) on \(H\otimes L^2(G)\). Hence

\[
R_\pi(h(\cdot)a)=\pi(a)\otimes\lambda(h).
\]

The span of these coefficient functions is \(L^1\)-dense on compact supports and therefore dense for the reduced norm. Its operator closure is exactly the spatial tensor product of \(\pi(A)\) and \(C_r^*(G)\), which faithfully realizes the minimal tensor product. This proves (20). The formula on the dense span uniquely specifies the map, independently of the auxiliary representation. \(\square\)

For the full construction the corresponding algebra is \(A\otimes_{\max}C^*(G)\), by [Blackadar 2006]. A trivial action requires the coefficient and group representations to commute, precisely the universal requirement of the maximal tensor product.

## Two examples and the failure of full injectivity

**Discrete coordinates.** With counting Haar measure on a discrete group \(\Gamma\), \(E\) is \(\ell^2(\Gamma,A)\), the completion of finitely supported sequences with

\[
\|\xi\|_E^2=\left\|\sum_{t\in\Gamma}\xi(t)^*\xi(t)\right\|.
\]

For a general element, these positive sums converge in norm, with finite subsets directed by inclusion. For finitely supported \(f\),

\[
(\Lambda_E(f)\xi)(t)=\sum_s\alpha_{t^{-1}}(f(s))\xi(s^{-1}t).
\tag{21}
\]

The matrix entry at row \(t\), column \(r\), is left multiplication by \(\alpha_{t^{-1}}(f(tr^{-1}))\). For example, let \(\Gamma=\mathbb Z\), \(A=M_2(\mathbb C)\), and \(\alpha_n=\operatorname{Ad}(v^n)\) for \(v=\operatorname{diag}(1,i)\). A coefficient \(f(1)=a\) contributes \(v^{-t}av^t\xi(t-1)\), exhibiting both the shift and the varying matrix coefficient.

**A strict norm difference.** Let \(\Gamma=F_2=\langle x,y\rangle\), and set

\[
h=\delta_x+\delta_{x^{-1}}+\delta_y+\delta_{y^{-1}}.
\]

The calculation in *Unitary representations and the two group C* completions*, section *A strict gap: the free group on two generators*, gives

\[
\|h\|_{C^*(F_2)}=4,
\qquad
\|h\|_{C_r^*(F_2)}=2\sqrt3.
\tag{22}
\]

The first norm is attained by the trivial representation. The second is the adjacency norm of the four-neighbor tree. We use the exact calculation from that chapter rather than repeat its tree proof. Equation (22) proves that \(C^*(F_2)\to C_r^*(F_2)\) has nonzero kernel. For any nonzero \(A\) with trivial action, choose norm-one positive \(a\in A\). The maximal tensor product has \(\|a\otimes h\|=4\), whereas (20) gives reduced norm \(2\sqrt3\). Thus the full and reduced norms differ with these coefficients as well.

The untensored trivial representation of \(F_2\) cannot factor through \(C_r^*(F_2)\): it would send an element of norm \(2\sqrt3\) to the scalar \(4\), contradicting contractivity. Tensoring it with \(\lambda\), as in (16), yields the regular representation.

## Geodesic probabilities on the free-group boundary

The strict norm difference also gives a coefficient embedding that full crossed products fail to preserve. We construct the action and prove the required norm equality explicitly.

Let \(T\) be the Cayley tree of \(F_2=\langle x,y\rangle\), with edges joining \(g\) to \(ga\) for \(a\in\{x,x^{-1},y,y^{-1}\}\). Its boundary \(X=\partial T\) consists of infinite reduced words. A cylinder specifies a finite initial word; these clopen cylinders give a compact Hausdorff topology, since \(X\) is the closed subset of the product of four-letter alphabets obtained by forbidding adjacent inverse letters. Left multiplication, followed by cancellation, gives a continuous action of \(F_2\) on \(X\). For fixed \(s\), cancellation removes at most \(|s|\) initial letters, so the inverse image of a cylinder is a finite union of cylinders. The inverse map is multiplication by \(s^{-1}\).

For \(\omega\in X\), let \(v_j(\omega)\) be the vertex at distance \(j\) on the ray from \(e\) to \(\omega\), including \(v_0=e\), and put
\[
m_n(\omega)=\frac1n\sum_{j=0}^{n-1}\delta_{v_j(\omega)}.
\tag{2A.1}
\]
This is a continuous map into \(\ell^1(F_2)\): each coordinate is a cylinder function, and the union of its supports is the finite ball of radius \(n-1\). The rays from \(e\) and \(s\) to the same end coalesce. Their portions before the common ray have lengths whose sum is \(|s|\). Consequently their first \(n\) vertices share at least \(n-|s|\) vertices when \(n>|s|\). Applied to the ray from \(s\) to \(\omega\), which is the translate of the ray from \(e\) to \(s^{-1}\omega\), this gives
\[
\sup_{\omega\in X}
\|s m_n(s^{-1}\omega)-m_n(\omega)\|_1
\leq \min\{2,2|s|/n\}.
\tag{2A.2}
\]
Here \((sp)(g)=p(s^{-1}g)\). Thus the boundary action is topologically amenable, with a concrete sequence of finitely supported probability maps.

The same ray calculation proves **property A** for the word metric on \(F_2\). Fix one end of the tree. At a vertex \(g\), put equal mass on the first \(n\) vertices of the ray from \(g\) to that end. The resulting probability \(p_n^g\) is supported within distance \(n-1\) of \(g\), and
\(\|p_n^g-p_n^h\|_1\leq\min\{2,2d(g,h)/n\}\).
These are precisely the uniformly bounded support and small-variation probability conditions defining property A. This proof uses only the tree geometry.

**Proposition (the boundary crossed-product norm).** For the boundary action,
\[
C(X)\rtimes F_2\longrightarrow C(X)\rtimes_r F_2
\quad\text{is an isomorphism}.
\tag{2A.3}
\]

**Proof.** Write \(\alpha_s(a)(\omega)=a(s^{-1}\omega)\). Set
\(\xi_{n,g}(\omega)=\sqrt{m_n(\omega)(g)}\).
These are continuous real functions, only finitely many are nonzero, and
\(\sum_g\xi_{n,g}^2=1\).
For an arbitrary nondegenerate covariant representation \((\pi,U)\) on \(H\), define the isometry
\[
J_n v=\sum_g\pi(\xi_{n,g})v\otimes\delta_g
\quad:H\longrightarrow H\otimes\ell^2(F_2).
\tag{2A.4}
\]
It intertwines coefficients exactly, since \(C(X)\) is commutative. Covariance shows that the \(g\)-coordinate of \((U_s\otimes\lambda_s)J_n-J_nU_s\) is
\(\pi(\alpha_s(\xi_{n,s^{-1}g})-\xi_{n,g})U_s\).
The squared operator norm is therefore bounded by the supremum of the sum of the squared coordinate functions. The scalar inequality
\(|\sqrt a-\sqrt b|^2\leq|a-b|\), for \(a,b\geq0\), and (2A.2) give
\[
\|(U_s\otimes\lambda_s)J_n-J_nU_s\|
\leq \min\{2,2|s|/n\}^{1/2}.
\tag{2A.5}
\]
For a finite crossed-product polynomial \(f=\sum_s a_su_s\), exact coefficient intertwining and (2A.5) imply
\[
J_n^*\big((\pi\otimes1)\rtimes(U\otimes\lambda)\big)(f)J_n
\longrightarrow (\pi\rtimes U)(f)
\quad\text{in operator norm}.
\tag{2A.6}
\]
Indeed, the norm of the error is at most the finite sum of \(\|a_s\|\) times the bound in (2A.5). Fell absorption identifies the amplified pair with the regular pair induced from \(\pi\), whose norm is bounded by the reduced norm even if \(\pi\) is not faithful. Compression is contractive, so (2A.6) gives
\(\|(\pi\rtimes U)(f)\|\leq\|f\|_r\).
Take the supremum over covariant pairs and then complete the polynomial algebra. This proves (2A.3). ∎

The constants give an equivariant embedding \(\mathbb C\hookrightarrow C(X)\). Its full crossed-product map starts at \(C^*(F_2)\). In the regular model of the target, the image of the element \(h\) in (22) is \(1\otimes\lambda(h)\), of norm \(2\sqrt3\), whereas its source norm is \(4\). By (2A.3) the target full norm is this reduced norm. The full map is therefore not injective. The reduced map for the same coefficient embedding is injective by Theorem 2.5. This gives the asserted functorial distinction for a specific nonzero compact action.

Gomez Aparicio–Julg–Valette, §9.3.1 and §9.3.3, Theorem 9.9, discuss free-group property A and boundary amenability in the general theory. Blackadar, II.10.3.15, records the amenable-action norm theorem. The construction and the norm proof required for this example have been supplied above.

## Where exactness can fail

For an invariant closed ideal \(I\subseteq A\), give \(I\) the restricted action and \(A/I\) the quotient action. Theorem 2.5 gives

\[
0\longrightarrow I\rtimes_rG
\xrightarrow{\iota_r}A\rtimes_rG
\xrightarrow{p_r}(A/I)\rtimes_rG
\longrightarrow0
\tag{23}
\]

with injectivity on the left and surjectivity on the right. The image of \(\iota_r\) is an ideal: products of compact coefficient functions in \(I\) with those in \(A\) have coefficients in \(I\), by (1) and invariance; continuity extends this property to the completions. Also \(p_r\iota_r=0\). What can fail is equality in

\[
\iota_r(I\rtimes_rG)\subseteq\ker p_r.
\tag{24}
\]

An **exact group**, in the crossed-product sense, is a locally compact group for which (23) is exact for every equivariant short exact sequence. A C*-algebra \(C\) is **exact** if minimal tensoring with \(C\) preserves every short exact sequence. Theorem 2.6 shows that exactness of \(G\) implies exactness of \(C_r^*(G)\), by using trivial actions. No converse for general locally compact groups is assumed here.

There are finitely generated discrete groups \(\Gamma\), constructed using families of expanders in their Cayley graphs, for which \(C_r^*(\Gamma)\) is not exact. These examples are called Gromov monster groups. A precise instance is failure of middle exactness in

\[
0\longrightarrow J\otimes_{\min}C_r^*(\Gamma)
\longrightarrow M\otimes_{\min}C_r^*(\Gamma)
\longrightarrow(M/J)\otimes_{\min}C_r^*(\Gamma)
\longrightarrow0,
\tag{25}
\]

where \(M=\prod_kM_{n_k}(\mathbb C)\) and \(J=\bigoplus_kM_{n_k}(\mathbb C)\), the norm-vanishing direct sum. We construct a bounded-degree expander family, label it with finitely many generators, prove that its vertices survive in the presented group, and then exhibit the kernel projection. The mathematical constructions are credited below; their proofs are supplied here. By (20), trivial \(\Gamma\)-actions turn (25) into a failure of equality in (24).

### Expanding graphs with increasing girth

We first construct the finite graphs that will supply the obstruction. This avoids assuming a family of Ramanujan graphs. The constants below are deliberately generous. A graph's **girth** is the length of its shortest cycle, and its **diameter** is the largest distance between two vertices. During the random construction we allow loops and parallel edges; loops count twice toward degree and do not cross a cut.

**Graph construction.** There are finite connected simple graphs \(X_k\), with \(n_k\to\infty\), whose degrees lie between \(998\) and \(1000\), whose girths tend to infinity, and for which
\[
 \begin{gathered}
 |\partial U|\ge8\min\{|U|,|X_k\setminus U|\},\\
 \operatorname{diam}(X_k)\le A\operatorname{girth}(X_k),\qquad
 A=\frac{64\log(2000)}{\log(1+8/1000)}.
 \end{gathered}
 \tag{2G.1}
\]
Here \(\partial U\) is the set of edges with exactly one endpoint in \(U\). Their normalized Laplacians have a common positive spectral gap.

**Proof: obtaining expansion.** Put \(d=1000\). Give each of \(n\) vertices \(d\) distinct half-edges, and choose a uniformly random perfect matching of the \(N=dn\) half-edges. A matched pair is an edge. After revealing any collection of pairs, the matching of the remaining half-edges is still uniform: every possible remaining matching has the same number of completions.

Fix \(U\) with \(k\le n/2\) vertices, and write \(D=dk\), \(x=k/n\) and \(\delta=1/100\). Explore its half-edges by taking the first unmatched one in a fixed order and revealing its partner. An internal partner removes two half-edges of \(U\); an external partner removes one and creates a cut edge. If the completed exploration has at most \(B=\delta D=10k\) external partners, every prefix has at most \(B\). After \(i\) internal and \(b\) external steps, the conditional probability of an internal partner is
\[
 \frac{D-2i-b-1}{N-2i-2b-1}
 \le\frac{D}{N-2B}
 \le\frac{x}{1-\delta}.
 \tag{2G.2}
\]
For the first inequality, first increase the numerator by one and the denominator by one: this increases a ratio at most one. The ratio \((D-2i-b)/(N-2i-2b)\) decreases as \(i\) increases, since \(D+b\le N\). Bound its numerator by \(D\) and its denominator, at \(i=0\), by \(N-2B\).

Such an exploration has at least \((1-\delta)D/2\) internal steps. For a specified internal/external pattern, multiply the conditional bounds (2G.2), and bound external-step probabilities by one. A pattern with \(b\) external steps has length \((D+b)/2\); its external positions identify it uniquely. Thus there are at most \(\sum_{b=0}^B\binom Db\) possible bad patterns. The elementary binomial estimate
\[
 \sum_{b=0}^{\delta D}\binom Db
 \le \exp(DH(\delta))\le(e/\delta)^{\delta D},
 \quad
 H(t)=-t\log t-(1-t)\log(1-t),
 \tag{2G.3}
\]
follows by expanding \((1+z)^D\) at \(z=\delta/(1-\delta)<1\): for \(b\le B\), \(z^b\ge z^B\). The last inequality uses \(-(1-\delta)\log(1-\delta)\le\delta\).

Consequently the probability that some \(k\)-element set has at most \(10k\) cut edges is bounded by
\[
 \begin{aligned}
 \binom nk
 \left[(e/\delta)^\delta
       \left(\frac{k}{n(1-\delta)}\right)^{(1-\delta)/2}\right]^{dk}
 &\le \left[C_0(k/n)^{494}\right]^k,\\
 C_0&=e(e/\delta)^{10}(1-\delta)^{-495}.
 \end{aligned}
 \tag{2G.4}
\]
Indeed \(\binom nk\le(en/k)^k\). For these constants \(C_0 2^{-494}<e^{-280}\). Sum (2G.4) over \(k\le\sqrt n\) using \(k/n\le n^{-1/2}\); this sum tends to zero as a geometric series with ratio \(C_0n^{-247}\). For \(\sqrt n<k\le n/2\), the total is at most \(n e^{-280\sqrt n}\). With probability tending to one, every nonempty set of at most half the vertices therefore has more than \(10|U|\) cut edges.

**Proof: separating the short cycles.** Set
\[
 g=\left\lfloor\frac{\log n}{8\log(2d)}\right\rfloor.
 \tag{2G.5}
\]
With probability tending to one, distinct cycles of length at most \(g\) have disjoint vertex sets. To see this without an independence assumption, two distinct intersecting cycles contain either two cycles meeting at one vertex, or three internally disjoint paths between two vertices. In the second case, take one cycle and a segment of the other outside it with endpoints on it. Their union contains the three paths. These two possible configurations have at most \(2g\) edges, \(v=e-1\) vertices, and are specified, up to the two types, by at most three path lengths. This also includes loops and pairs of parallel edges as cycles of length one and two.

For each configuration with \(e\) edges, choose its vertices in at most \(n^v\) ways and its half-edges in at most \(d^{2e}\) ways. The probability that its specified pairs occur in the random matching is
\[
 \frac1{(N-1)(N-3)\cdots(N-2e+1)}
 \le(N-4g)^{-e}.
 \tag{2G.6}
\]
For large \(n\), its expected number of occurrences is therefore at most \(n^{-1}(2d)^e\). Summing over the two types and the path lengths gives, for example, the upper bound \(3(2g)^4(2d)^{2g}/n\). By (2G.5) this tends to zero. The probability of any such configuration is at most its expected number: for a nonnegative integer-valued variable \(Z\), \(1_{Z>0}\le Z\).

Both required events hold simultaneously for all sufficiently large \(n\), since their failure probabilities have sum tending to zero. Choose a matching with those properties. Delete one edge from every cycle of length at most \(g\). Since these cycles have disjoint vertex sets, a vertex loses at most two half-edges; the factor two allows for a deleted loop. The remaining graph is simple, has degrees in \([d-2,d]\), and has girth greater than \(g\). At most \(2|U|\) cut edges were deleted from any set \(U\), so its boundary still has at least \(8|U|\) edges when \(|U|\le n/2\). Taking complements proves the first line of (2G.1), and also proves connectedness.

Every vertex outside a set meets at most \(d\) of its boundary edges. A ball with at most \(n/2\) vertices therefore grows by a factor at least \(1+8/d\) on enlarging its radius by one. A radius \(t\le\log n/\log(1+8/d)+2\) suffices for every ball to have more than half the vertices. Any two such balls intersect, so the diameter is at most \(2t\). For sufficiently large \(n\), (2G.5) gives \(g\ge\log n/(16\log(2d))\), while \(2t\le4\log n/\log(1+8/d)\). These estimates imply (2G.1). Choose an increasing sequence of these \(n\)'s; its girths tend to infinity.

**Proof: converting a cut estimate to a spectral gap.** For a vertex \(v\), write \(d_v\) for its degree, and put \(\operatorname{vol}(U)=\sum_{v\in U}d_v\). If \(\operatorname{vol}(U)\) is at most half the total volume, both \(|U|\) and \(|U^c|\) are at least \(\operatorname{vol}(U)/d\). Thus (2G.1) gives \(|\partial U|\ge h\operatorname{vol}(U)\), where \(h=8/d\).

For a nonnegative real function \(f\) supported on such a set, sum the boundary inequality over the superlevel sets of \(f^2\). Integrating the indicators gives
\[
 \begin{aligned}
 h\sum_v d_v f(v)^2
 &\le\sum_{\{v,w\}\in E}|f(v)^2-f(w)^2|\\
 &\le\left(2\sum_vd_vf(v)^2
             \sum_{\{v,w\}\in E}|f(v)-f(w)|^2\right)^{1/2}.
 \end{aligned}
 \tag{2G.7}
\]
The second inequality is Cauchy–Schwarz followed by
\(\sum_E(f(v)+f(w))^2\le2\sum_vd_v f(v)^2\).

Given a real function \(u\) with \(\sum_vd_vu(v)=0\), choose a weighted median \(m\): each strict side of \(m\) has at most half the total volume. Apply (2G.7) to \((u-m)_+\) and \((m-u)_+\). On each edge the energy of \(u\) dominates the sum of their energies, including an edge crossing the two sides. Also
\(\sum_vd_v(u(v)-m)^2\ge\sum_vd_vu(v)^2\), by the zero-mean condition. It follows that
\[
 \sum_E|u(v)-u(w)|^2
 \ge\frac{h^2}{2}\sum_vd_vu(v)^2.
 \tag{2G.8}
\]
Apply the same argument to real and imaginary parts for complex functions. Under the isometry \(u(v)\mapsto\sqrt{d_v}u(v)\), the quadratic form on the left is that of
\(1-D^{-1/2}A_XD^{-1/2}\). Its kernel is the span of \((\sqrt{d_v})_v\); connectedness proves this from the energy formula. Its spectrum lies in \([0,2]\), since \(|u(v)-u(w)|^2\le2|u(v)|^2+2|u(w)|^2\). Equation (2G.8) proves the common gap \(\varepsilon=h^2/2\). \(\square\)

This is the configuration-model method for producing sparse expanding graphs, followed by a bounded deletion of separated short cycles. For the spectral viewpoint and the cut-to-energy method compare Daniel A. Spielman, *Spectral and Algebraic Graph Theory*, draft of 2 April 2025, Chapter 21, Theorem 21.1.3 and its proof, pp.176–180. The argument above supplies the graph family and every estimate needed here; it does not assume a Ramanujan construction or a sharp random-graph eigenvalue theorem.

### Labelling the entire family with finitely many letters

A label alphabet \(\mathcal S\) consists of finitely many letters paired by a formal inverse \(a\mapsto\bar a\), with \(a\ne\bar a\). Orient the edges of a graph arbitrarily; an oriented edge receives a letter, and traversal in the reverse direction reads its inverse. A labelling is **reduced** when distinct edges leaving a vertex read distinct letters. Equivalently, a path without backtracking reads a freely reduced word.

Fix \(\lambda=1/12\). By passing to a subsequence of the graphs in (2G.1), we can arrange that
\(\ell_k=\lfloor\lambda\operatorname{girth}(X_k)\rfloor\) are strictly increasing integers greater than one. We will label the whole family so that two distinct paths reading the same word have length less than \(\ell_i\) in every component \(X_i\) in which they occur. In particular, every repeated path is shorter than \(\lambda\) times every simple cycle containing it. This is the **graphical small cancellation condition** used below.

Here is the finite counting argument, following the method of Louis Esperet and Ugo Giocanti, *Optimization in graphical small cancellation theory*, Theorem 3.1 and Claim 3.3 (arXiv:2306.03474v2). The argument includes the reconstruction step for overlapping paths, which is essential to the counting.

Put \(D=1000\), and choose an even integer \(L\) such that
\[
 \alpha=2(D-1)^{2A/\lambda+2},\qquad
 L\ge2(D-1)+13\alpha.
 \tag{2L.1}
\]
Use an alphabet of \(L\) letters. Suppose the earlier components \(X_i\), \(i<k\), have already been labelled. A partial labelling of an edge set \(F\subseteq E(X_k)\) is called valid if it is reduced, contains no word of length \(\ell_i\) already occurring in \(X_i\) for \(i<k\), and contains no two distinct paths with the same word of length \(\ell_k\). Let \(c(F)\) count valid labellings and set \(c(\varnothing)=1\). We prove by induction on \(|F|\) that
\[
 c(F)\ge\alpha c(F\setminus\{e\})\qquad(e\in F).
 \tag{2L.2}
\]
This gives at least one valid labelling of the entire component and allows induction over the components.

For one edge all \(L\) choices are valid. For the induction step, extend a valid labelling of \(F\setminus\{e\}\) by one of its \(L\) possible edge labels. A failure of reducedness has at most \(2(D-1)\) causes: another edge at one of the two endpoints determines the forbidden label. Thus these extensions number at most \(2(D-1)c(F\setminus\{e\})\).

Every other failure gives a path \(P\) containing \(e\), with length \(\ell_i\), that reads the same word as a path \(Q\) in \(X_i\), for some \(i\le k\); for \(i=k\), the paths are distinct. The edge \(e\) must occur in one of the two paths, since its deletion leaves a valid labelling. Name that path \(P\). Delete every edge label on \(P\). Repeated use of the induction hypothesis on smaller edge sets gives
\[
 c(F\setminus E(P))
 \le\alpha^{1-\ell_i}c(F\setminus\{e\}).
 \tag{2L.3}
\]
The path has \(\ell_i\) distinct edges, because its length is less than the girth of \(X_k\).

We claim that its erased labels are uniquely determined by \(P,Q\) and the remaining labelling. When \(i<k\), all of \(Q\) lies in an earlier, fixed component; its word determines the word on \(P\). The same conclusion holds if \(i=k\) and the two paths share no edge.

If they share an edge, their common edges form one subpath. Two separate common subpaths would create a cycle of length at most \(2\ell_k\), contradicting \(\operatorname{girth}(X_k)\ge12\ell_k\). Number each path's edges from zero to \(\ell_k-1\). For a common subpath traversed in the same direction, suppose its initial positions are \(p\) in \(P\) and \(q\) in \(Q\). They cannot be equal: reducedness and the common word would extend the coincidence forward and backward until both paths were identical. Reverse both paths, if needed, to arrange \(q>p\). Write \(h=q-p\). The letters on \(Q\) outside the common subpath remain known. In particular the word positions \(p,\ldots,q-1\) are known. On the common subpath, equality of its labels says that a letter at position \(j\ge q\) equals the letter at position \(j-h\). This recurrence, together with all the known positions outside that interval, determines the entire common word. Hence it restores every edge of \(P\).

If the common subpath is traversed in opposite directions, its index intervals in the two paths are disjoint. Otherwise two walkers following the equal words at equal speed would meet on that common subpath: either at a vertex at an integer time, or in the middle of an edge at a half-integer time. Meeting at a vertex forces the paths to coincide by reducedness. Meeting inside an edge forces a letter to equal its formal inverse. Both are impossible. The letters at the indices of \(P\)'s common subpath can consequently be read on the un-erased part of \(Q\). They determine that subpath's labels; its reverse determines the erased part of \(Q\), and the common word then restores all of \(P\). This proves the reconstruction claim.

There are at most \(2\ell_i(D-1)^{\ell_i-1}\) oriented paths \(P\) of length \(\ell_i\) containing a fixed edge: choose its position and direction, then extend without backtracking. A graph of maximum degree \(D\) and diameter \(b\) has at most
\(1+D\sum_{j=0}^{b-1}(D-1)^j\) vertices, by exploring a ball about one vertex. Its number of edges is at most \(\tfrac32(D-1)^{b+2}\). Since
\(b\le A\operatorname{girth}(X_i)\le2A\ell_i/\lambda\), the number of oriented paths \(Q\) of length \(\ell_i\), counted from their initial edge, is at most
\[
 3(D-1)^{(2A/\lambda+1)\ell_i+1}.
 \tag{2L.4}
\]
Combine this with (2L.3) and the unique reconstruction. The number of bad extensions belonging to the index \(i\) is at most
\[
 \begin{aligned}
 &6\ell_i(D-1)^{(2A/\lambda+2)\ell_i}
          \alpha^{1-\ell_i}c(F\setminus\{e\})\\
 &\hspace{20mm}=6\alpha\ell_i2^{-\ell_i}c(F\setminus\{e\}).
 \end{aligned}
 \tag{2L.5}
\]
The \(\ell_i\)'s are distinct positive integers, so their sum \(\sum_i\ell_i2^{-\ell_i}\) is at most \(\sum_{j\ge1}j2^{-j}=2\). All bad extensions together therefore number at most
\((2(D-1)+12\alpha)c(F\setminus\{e\})\). Subtract them from the \(L c(F\setminus\{e\})\) extensions, and use (2L.1) to obtain (2L.2).

Choose a valid full labelling at every stage. A repeated longer word contains a repeated word of one of the forbidden lengths, so the labellings have the stated small cancellation property for all paths. Although the alphabet in (2L.1) is large, it is fixed once and for all: it does not increase with \(k\). \(\square\)

### The quotient group retains the graph vertices

Let \(\mathcal X=\bigsqcup_kX_k\) carry the preceding labellings. Choose one generator from each inverse pair of letters, and define
\[
 \Gamma=\langle a_1,\ldots,a_{L/2}\mid
       \text{words read on all simple cycles of }\mathcal X\rangle.
 \tag{2M.1}
\]
This is a finitely generated discrete group; infinitely many relators are allowed. A closed walk in a graph is a product of conjugates of simple cycles, after deleting backtracking: split a walk whenever a vertex is repeated. Its word therefore becomes the identity in \(\Gamma\). For a chosen base vertex \(o_k\), assign to \(v\in X_k\) the element \(g_v\) read along any path from \(o_k\) to \(v\). The closed-walk observation makes this independent of the path. An edge from \(v\) to \(w\), with letter \(a\), gives \(g_v^{-1}g_w=a\). We now prove that each vertex map is injective.

We supply the diagram facts used in that proof. The graphical reduction argument is due to Yann Ollivier and Dominik Gruber; compare Gruber, *Groups with graphical C(6) and C(7) small cancellation presentations*, Lemmas 2.10 and 2.13. A **piece** is a nonbacktracking path whose word has two distinct lifts to \(\mathcal X\). Our labellings make a piece in any simple cycle shorter than \(1/12\) of that cycle.

**Diagrams and reduction.** A diagram is a finite simply connected planar complex with oriented, labelled edges and polygonal faces. Its exterior boundary can pass through a vertex more than once. A face boundary is labelled by a closed walk in \(\mathcal X\); we initially allow all nontrivial closed walks as relators. A word is the identity in (2M.1) precisely when it bounds such a diagram. In one direction, successively removing faces expresses the boundary word as a product of conjugated relators. In the other, express a word in the normal closure as a finite product \(\prod_j t_jr_j^{\pm1}t_j^{-1}\). Draw the relator polygons attached by the paths \(t_j\) to a common basepoint in a planar arrangement. Consecutive inverse letters in the remaining boundary can be identified by folding. This constructs the required diagram. Conversely the same cutting procedure, with paths from the basepoint to each face, recovers that product. These operations prove the diagram criterion, including freely reducible boundary words.

An interior edge **originates from the graph** if the two incident face-boundary lifts traverse the same edge of \(\mathcal X\). If this holds for one edge in an interior arc, reducedness extends the agreement along the arc. Every other interior arc is a piece. A nontrivial closed walk has a unique lift once its cyclic word and a lifted point are specified. Two distinct full cycle lifts would give a repeated path containing a simple cycle, which is excluded by the small cancellation bound. This ensures that the origin condition is independent of the face descriptions.

Among diagrams for a given boundary word choose one with as few edges as possible, and then as few vertices as possible. We claim that it has no originating interior edge and that every face lifts to a simple cycle. Here are the planar reduction details, including the possible holes when several faces merge.

Erase all originating interior edges and merge incident faces. The face lifts agree at each erased edge, so the boundary walks of each merged region still lift to \(\mathcal X\). First exclude a merged region with freely trivial boundary. Choose an innermost such boundary, and take the disk subdiagram it encloses in the original diagram. Its interior edges connecting the merged faces originate from the graph. Replace this subdiagram by one face with the same boundary word. Identify consecutive inverse boundary edges, then repeat until this face has become a labelled tree. The exterior boundary walk is preserved, while at least one edge has been removed. Edge minimality excludes this alternative. Thus every remaining merged face carries a freely nontrivial closed walk in the graph.

Two further obstructions must be considered: a merged region can enclose a hole, or its closure can fail to be simply connected. Choose an innermost such enclosure. The region it encloses, denoted \(D_0\), has at least one face, has no interior spur, and has simply connected faces. Its interior arcs are pieces. After suppressing degree-two vertices, every face of \(D_0\), including its boundary faces, has at least six edges: its entire boundary consists of pieces, since it faces the surrounding merged region, and a nontrivial cycle cannot be covered by fewer than six pieces. There is at most one vertex of \(D_0\) incident to an edge outside \(D_0\); all its other vertices have degree at least three after suppression.

Such an enclosure is impossible. Indeed, a planar diagram whose faces have at least six edges and whose interior vertices have degree at least three satisfies
\[
 \sum_{v\in\partial D_0}\bigl(5/2-\deg(v)\bigr)\ge3.
 \tag{2M.2}
\]
Here is a calculation that also covers cut vertices and connecting tree edges. Let \(b\) be the length of the exterior boundary walk, counting a bridge twice, and let \(B\) be its set of distinct vertices. Each such vertex is visited, so \(b\ge|B|\). Euler's formula and face incidences give \(V-E+F=1\), \(\sum_v\deg(v)=2E\), and \(6F\le2E-b\). Consequently
\[
 6\le\sum_v(6-2\deg(v))-b
   \le\sum_{v\in B}(5-2\deg(v)).
\]
The second inequality uses the nonpositive interior-vertex terms and \(b\ge|B|\). Dividing by two proves (2M.2), with no assumption that the boundary embeds. In the enclosure above, at most one summand is positive, and even a vertex of degree one contributes only \(3/2\). This contradicts (2M.2).

The erased-edge construction therefore gives an actual diagram with nontrivial closed-walk faces. Any erased edge would contradict its minimal number of edges. There are consequently no originating edges in the minimal diagram.

Its faces are simply connected, with no spur ending inside a face. If a face lift repeated a graph vertex, pinch the two corresponding boundary vertices together through that face. The two resulting boundary walks are closed walks in \(\mathcal X\). Freely trivial ones can be folded as above. If folding removes edges, edge minimality fails; otherwise the pinch reduces the number of vertices with the same edges, contrary to the second minimality condition. Every remaining face therefore lifts to a simple cycle. We have proved that any trivial word has a diagram with simple-cycle faces and with every interior arc a piece.

**A boundary face with a long exterior segment.** Consider a disk component of such a diagram, with at least two faces. Suppress vertices of degree two. Write \(i(f)\) for the number of interior arcs of a face and \(e(f)\) for its exterior arcs. Directly from Euler's formula,
\[
 6=2\sum_v(3-\deg(v))
            +\sum_f\bigl(6-2e(f)-i(f)\bigr).
 \tag{2M.3}
\]
The total degrees count each edge twice; face incidences count each interior edge twice and each exterior edge once, which gives the displayed identity. There are no degree-one vertices when the boundary is cyclically reduced, so the vertex sum is nonpositive. An interior face has at least thirteen arcs because each piece is shorter than a twelfth of its perimeter. A face with \(e(f)\ge2\) has \(i(f)\ge e(f)\), since the exterior components are separated by interior arcs; its contribution is nonpositive. A face with \(e(f)=1\) also contributes nonpositively if \(i(f)\ge4\). Thus (2M.3) requires boundary faces with
\(e(f)=1\) and \(i(f)\le3\). In a diagram with at least two faces each such face has an interior arc, so it contributes at most three. There are at least two such faces. The unique exterior segment of either one has length greater than \(3/4\) of its perimeter, since its at most three interior pieces together have length less than one quarter.

**Injectivity.** Suppose some two distinct graph vertices have the same image, and choose a shortest nonempty graph geodesic \(p\) whose word is trivial. Its word is freely reduced. It is also cyclically reduced: deleting inverse first and last letters would leave a shorter trivial subpath, and a nonempty subpath of a geodesic has distinct endpoints. Take a reduced diagram for its word. If there are no faces, the nonempty freely reduced word would be freely trivial. If there is a cut vertex, choose a leaf disk component not crossing the boundary basepoint. Its boundary is a shorter contiguous subword of \(p\), again contradicting minimality. Thus the diagram is a disk.

If there is just one face, a contiguous subpath of \(p\) longer than half its perimeter is a subpath of that simple cycle. Its lift along \(p\) must agree with the cycle lift: otherwise it is a piece, contradicting the twelfth-perimeter bound. But a graph geodesic cannot follow more than half a simple cycle, since the complementary segment is shorter.

If there are at least two faces, use the two faces furnished by (2M.3). At least one of their exterior segments does not cross the boundary basepoint, so it is a contiguous subpath of \(p\). It is longer than \(3/4\) of its face perimeter. Again its two lifts must agree, and the complementary cycle segment shortens a geodesic subpath. This final contradiction proves injectivity. \(\square\)

### An explicit projection in the tensor kernel

We first give the projection argument for regular graphs, where the constant-vector formula is simplest, and then apply its weighted version to the constructed graphs. A finite connected simple \(d\)-regular graph \(V_k\), with \(n_k\) vertices, has normalized Laplacian \(\Delta_k=1-A_k/d\). We require \(n_k\to\infty\) and one \(\varepsilon>0\) such that
\[
 \operatorname{spec}(\Delta_k)\subset\{0\}\cup[\varepsilon,2]
                         \quad\text{for every }k.
 \tag{2T.1}
\]
This is the spectral expander condition used in the calculation. Suppose there are injective vertex maps \(v\mapsto g_v\in\Gamma\) and a fixed finite symmetric subset \(S\subset\Gamma\) with
\(g_v^{-1}g_w\in S\) whenever \(v,w\) are adjacent. Isometric copies in a finitely generated Cayley graph satisfy this hypothesis. We allow extra Cayley edges between the embedded vertices; the graph's own edges determine its Laplacian.

For \(s\in S\), let \(a_{s,k}\in M_{n_k}\) have entry \(1/d\) at \((v,w)\) if \(v,w\) are adjacent and \(g_v^{-1}g_w=s\), and zero otherwise. Injectivity makes this a scaled partial permutation matrix, so its norm is at most \(1/d\). The bounded sequence \(a_s=(a_{s,k})_k\) belongs to \(M\). In the spatial tensor product form
\[
 \Delta=1\otimes1-\sum_{s\in S}a_s\otimes\lambda_s.
 \tag{2T.2}
\]
The symmetry of the graph gives \(a_{s^{-1}}=a_s^*\), hence \(\Delta\) is self-adjoint. Its \(k\)-th coordinate acts on \(\ell^2(V_k)\otimes\ell^2(\Gamma)\). The diagonal unitary
\(W_k=\operatorname{diag}_{v\in V_k}\lambda_{g_v^{-1}}\) gives exactly
\[
 \Delta^{(k)}=W_k(\Delta_k\otimes1)W_k^*.
 \tag{2T.3}
\]
Indeed its \((v,w)\) entry is the scalar Laplacian entry times \(\lambda_{g_v^{-1}g_w}\). The direct sum of all matrix-coordinate representations is faithful on \(M\), so its spatial tensor product with the faithful regular representation is faithful as well. Thus \(\Delta\) is positive and has spectrum in the set in (2T.1).

Choose \(\varphi(t)=\max\{0,1-t/\varepsilon\}\) on \([0,2]\). Functional calculus gives a projection \(P=\varphi(\Delta)\in M\otimes_{\min}C_r^*(\Gamma)\). Connectedness makes the zero eigenspace of each \(\Delta_k\) exactly the constants: its quadratic form is a positive multiple of \(\sum_{v\sim w}|\xi(v)-\xi(w)|^2\). If \(p_k\) is the rank-one projection onto the normalized constant vector, then
\[
 \begin{gathered}
 P^{(k)}=W_k(p_k\otimes1)W_k^*,\qquad\|P^{(k)}\|=1,\\
 (P^{(k)})_{v,w}=\frac1{n_k}\lambda_{g_v^{-1}g_w}.
 \end{gathered}
 \tag{2T.4}
\]
In particular \(P\) is a nonzero projection of norm one.

Let \(\omega_t(z)=\langle\delta_t,z\delta_e\rangle\) be the bounded Fourier functional on \(C_r^*(\Gamma)\), so \(\omega_t(\lambda_s)=1\) for \(s=t\) and zero otherwise. Formula (2T.4) gives
\[
 \left\|\big((\operatorname{id}_M\otimes\omega_t)(P)\big)_k\right\|
                              \leq \frac1{n_k}.
 \tag{2T.5}
\]
For a fixed \(t\), the entry \(1/n_k\) can occur at most once in any row or column, since \(g_w=g_vt\) uniquely determines \(w\) from \(v\), and conversely. This is why injectivity of the vertex maps matters. Every Fourier coefficient of \(P\) therefore belongs to \(J\).

Put \(q:M\to M/J\). Every coefficient of \((q\otimes\operatorname{id})(P)\) is zero. These coefficients separate elements of the spatial tensor product, with no exactness assumption. To verify that fact for any C*-algebra \(B\), represent \(B\) faithfully on \(H\) and use the regular representation in the other factor. The matrix block of an element \(z\in B\otimes_{\min}C_r^*(\Gamma)\), from column \(v\) to row \(u\) of \(\ell^2(\Gamma)\), is
\(\rho((\operatorname{id}_B\otimes\omega_{uv^{-1}})(z))\). The identity holds on finite tensors and extends by norm continuity. If every coefficient vanishes, every matrix block vanishes, and the finite-coordinate vectors show that the faithfully represented operator is zero. Consequently
\[
 (q\otimes\operatorname{id})(P)=0.
 \tag{2T.6}
\]

On the other hand, every element of \(J\otimes_{\min}C_r^*(\Gamma)\) has coordinate norms tending to zero. For finite sums \(\sum j_i\otimes c_i\), bound the \(k\)-th norm by \(\sum\|(j_i)_k\|\|c_i\|\), then use uniform approximation by those sums. Equation (2T.4) proves that \(P\) is outside this ideal. We have explicitly obtained
\[
 P\in\ker(q\otimes\operatorname{id})
                 \setminus\big(J\otimes_{\min}C_r^*(\Gamma)\big).
 \tag{2T.7}
\]
Thus the expander-embedding hypothesis implies nonexactness of the reduced group algebra and, by the trivial-action isomorphism, failure of middle exactness for reduced crossed products. The graph and diagram arguments above supply the required finitely generated group; the weighted calculation below applies the obstruction to its bounded-degree graphs.

The same calculation works for weak vertex maps whose largest fibre size \(m_k\) satisfies \(m_k/n_k\to0\), provided edge differences still belong to one finite \(S\). The \(a_{s,k}\)'s now need not be partial permutation matrices, but their absolute row and column sums are at most one, so they still give bounded sequences in \(M\). The matrices in (2T.5) are sums of disjoint all-ones rectangular blocks, one for each pair of group-value fibres related by \(t\). Their norm is at most \(m_k/n_k\). Formula (2T.3) does not require injectivity, so all the remaining arguments are unchanged. This includes the weaker type of expander placement used in the original Gromov construction.

The construction is the expander projection argument described in [Gomez Aparicio–Julg–Valette 2019, §9.3.3, proof of Theorem 9.12]. The formulas above specify the element, its Fourier coefficients, and the exact kernel and ideal in (25).

### The tensor obstruction for the constructed graphs

The constructed graphs have bounded, rather than identical, degrees. Here is the corresponding version of the projection calculation. For one graph, let \(D_k=\operatorname{diag}(d_v)\) and \(\operatorname{vol}(X_k)=\sum_vd_v\). Replace the regular graph Laplacian in (2T.1) by
\[
 \Delta_k=1-D_k^{-1/2}A_kD_k^{-1/2}.
 \tag{2M.4}
\]
Its uniform gap was proved in (2G.8). For \(s\) in the fixed label set, the matrix \(a_{s,k}\) now has entry \(1/\sqrt{d_vd_w}\) when the edge from \(v\) to \(w\) reads \(s\). Injectivity gives at most one entry in each row and column. Its norm is at most \(1/998\), so \(a_s=(a_{s,k})_k\) belongs to the same product algebra \(M\). Equations (2T.2)–(2T.3) still hold exactly with these matrices.

The normalized kernel vector of \(\Delta_k\) is
\(v\mapsto\sqrt{d_v/\operatorname{vol}(X_k)}\). Thus its gauged constant-space projection has entries
\[
 (P^{(k)})_{v,w}
 =\frac{\sqrt{d_vd_w}}{\operatorname{vol}(X_k)}
                   \lambda_{g_v^{-1}g_w},\qquad
 \|P^{(k)}\|=1.
 \tag{2M.5}
\]
Each fixed Fourier coefficient is a weighted partial permutation matrix of norm at most
\(1000/(998n_k)\), which tends to zero. The separating-coefficient argument (2T.6) and the norm-vanishing ideal argument (2T.7) therefore apply without change. We have constructed both the finitely generated group and a concrete projection witnessing nonexactness of \(C_r^*(\Gamma)\). Through the trivial-action identity, it is also a counterexample to exactness of the reduced crossed-product functor.

The original monster construction is due to Mikhail Gromov. The finite graphical labelling approach is due to Damian Osajda; the counting improvement used here is due to Louis Esperet and Ugo Giocanti, and the diagram reduction to Ollivier and Gruber. The final analytic projection is the obstruction described by Gomez Aparicio–Julg–Valette.

The ideal representation-extension argument in Lesson 1 proves that full crossed products preserve equivariant short exact sequences; Connes, Chapter II, Appendix C, Proposition 2(b), records this theorem. Their preservation of ideal inclusions is consistent with the preceding failure for a general embedding: an ideal has additional representation-extension properties. Likewise, reduced preservation of embeddings does not settle the middle kernel in (23).

## Exercises

**Exercise 1 (basic).** Starting from (3), verify covariance, both adjoint formulas, and why left translation has no modular factor. Explain where a modular factor does appear.

**Solution.** Pointwise adjointing gives \(\widetilde\pi(a)^*=\widetilde\pi(a^*)\). In the \(L^2\) integral put \(t=sr\). Left Haar invariance gives \(\|\lambda_s\xi\|_2=\|\xi\|_2\), so \(\lambda_s^*=\lambda_{s^{-1}}\). Applying the three operators in order gives \(\pi(\alpha_{t^{-1}s}(a))\xi(t)\). Since \(\alpha_{t^{-1}s}=\alpha_{t^{-1}}\alpha_s\), this is \(\widetilde\pi(\alpha_s(a))\xi(t)\). The modular function is needed for Haar inversion in the integrated adjoint formula, producing \(\Delta(t)^{-1}\) in (1); it is absent from a left-translation change of variables.

**Exercise 2 (intermediate).** Prove Fell absorption by constructing \(W\) on compact continuous sections. Include surjectivity, both intertwining identities, and the scalar case with the tensor factors reversed.

**Solution.** Define \(W\xi(t)=U_{t^{-1}}\xi(t)\). Strong continuity makes this a compact continuous section. Its norm is \(\|\xi\|_2\), since every \(U_{t^{-1}}\) is unitary. The inverse \(Z\eta(t)=U_t\eta(t)\) preserves the same dense subspace and satisfies \(WZ=ZW=1\) there. Both maps extend isometrically, giving \(Z=W^*\) and surjectivity. Covariance gives \(WP(a)W^*\eta(t)=\pi(\alpha_{t^{-1}}(a))\eta(t)\). The other identity is

\[
WV_sW^*\eta(t)=U_{t^{-1}}U_sU_{s^{-1}t}\eta(s^{-1}t)=\eta(s^{-1}t).
\]

Thus the conjugated pair is regular, and integration preserves conjugation. Scalar coefficients give \(U\otimes\lambda\simeq1\otimes\lambda\). Composing with the tensor flip gives \(\lambda\otimes U\simeq\lambda\otimes1\).

**Exercise 3 (intermediate).** Let \(\varphi:A\hookrightarrow B\) be equivariant. Prove that its reduced crossed-product map is isometric, allowing a faithful representation of \(B\) to restrict degenerately to \(A\).

**Solution.** Choose faithful nondegenerate \(\rho\) on \(K\), and set \(K_A=\overline{\rho(\varphi(A))K}\). This space reduces \(\rho\varphi\), whose complementary summand is zero. Its restriction \(\sigma\) is faithful: if it kills \(a\), the full representation kills \(a\) too, whence \(a=0\). It is nondegenerate by construction. Equivariance gives \(R_\rho^B(\varphi_c f)=R_{\rho\varphi}^A(f)\). On \(L^2(G,K_A)\oplus L^2(G,K_A^\perp)\), this integrated operator is \(R_\sigma^A(f)\oplus0\), because translations preserve the decomposition. Its norm is \(\|f\|_{r,A}\). Completion preserves this equality, proving isometry without requiring a nondegenerate embedding into \(B\).

**Exercise 4 (advanced).** For any C*-algebra \(B\) with trivial \(G\)-action, prove the canonical isomorphism

\[
(A\otimes_{\min}B)\rtimes_{\alpha\otimes\mathrm{id},r}G
\cong(A\rtimes_{\alpha,r}G)\otimes_{\min}B.
\tag{26}
\]

Specify its dense formula. No nuclearity or exactness hypothesis on \(B\) is allowed.

**Solution.** If either algebra is zero, both sides are zero. Otherwise take faithful nondegenerate \(\pi_A\) on \(H_A\) and \(\pi_B\) on \(H_B\). Their spatial tensor product is faithful on \(A\otimes_{\min}B\). Use the unitary identification

\[
L^2(G,H_A\otimes H_B)\cong L^2(G,H_A)\otimes H_B,
\quad
[t\mapsto\xi(t)\otimes w]\longleftrightarrow\xi\otimes w.
\]

In the left regular model, \(a\otimes b\) acts at coordinate \(t\) as \(\pi_A(\alpha_{t^{-1}}(a))\otimes\pi_B(b)\); translation acts as \(\lambda_s\otimes1\). Hence \(F(s)=f(s)\otimes b\) has integrated operator \(R_{\pi_A}(f)\otimes\pi_B(b)\). The dense formula is

\[
\sum_j f_j(\cdot)\otimes b_j
\longmapsto\sum_j R_{\pi_A}(f_j)\otimes\pi_B(b_j).
\]

Such functions form a *-subalgebra by (1) and triviality of the second action. They are \(L^1\)-dense on compact supports: approximate a compact coefficient image by finite tensor sums, then use a partition of unity and cutoff. The common regular model makes the map isometric for the reduced norm. Its image is dense in the right side, because \(R_{\pi_A}(C_c(G,A))\) is dense in the first factor and \(\pi_B(B)\) realizes the second faithfully. Completion gives (26), with the formula making it independent of the auxiliary representations. All norms here are spatial, so neither nuclearity nor exactness is needed.

**Exercise 5 (advanced).** Let a connected finite graph have vertex degrees \(d_v\), and suppose its vertices map injectively to a group, with every edge difference in a fixed finite set. Find the kernel vector of its normalized Laplacian and the entries of the gauged kernel projection. Prove a bound for every fixed Fourier coefficient in terms of \(n\), the minimum degree and the maximum degree. Explain why a lower degree bound and a uniform spectral gap suffice for the nonexactness argument.

**Solution.** The normalized Laplacian is \(1-D^{-1/2}AD^{-1/2}\). Its quadratic form on \(D^{1/2}u\) is \(\sum_E|u(v)-u(w)|^2\), so connectedness makes its kernel the span of \((\sqrt{d_v})_v\). Normalize by \(\operatorname{vol}(X)^{1/2}\). Diagonal conjugation by \(\lambda_{g_v^{-1}}\) gives entries \(\sqrt{d_vd_w}\lambda_{g_v^{-1}g_w}/\operatorname{vol}(X)\). For one Fourier index, injectivity permits at most one nonzero entry in each row and column; its norm is therefore the largest weight, at most \(d_{\max}/(d_{\min}n)\). A uniform gap isolates the kernel by one continuous functional-calculus function for every graph. The projection has norm one in each coordinate, while these Fourier coefficients tend to zero when the degree ratio is bounded and \(n\to\infty\). Equations (2T.6)–(2T.7) give the required quotient kernel and exclusion from the norm-vanishing tensor ideal.

## Proofs and prerequisites

We use the following exact prerequisite proofs and distinguish them from the results constructed in this lesson.

- Nondegenerate covariant pairs correspond to nondegenerate representations of the full crossed product, with integrated operator \(\int\pi(f(s))U_sds\). See [Connes 1994] and [Blackadar 2006]. This is the prerequisite result of the chapter “C*-dynamical systems and full crossed products”.
- For faithful nondegenerate coefficient representations, regular representations are faithful on \(L^1(G,A)\) and give the same norm there. See *Covariance and crossed products with nonunital coefficients*, sections *The regular pair and its two faithfulness assertions*, *Why the reduced norm does not depend on the faithful coefficient representation*, and *Full and reduced crossed products and their canonical actions*, Theorems 4.2, 5.1 and 6.1, equations (4.3)–(6.3); compare [Blackadar 2006]. Proposition 2.2 provides the module interpretation.
- The free-group element in (22) has full norm \(4\) and reduced norm \(2\sqrt3\). See *Unitary representations and the two group C* completions*, section *A strict gap: the free group on two generators*, Proposition 13.1 and equations (13.2)–(13.5).
- For trivial actions the full crossed product is \(A\otimes_{\max}C^*(G)\). This is proved by the commuting universal representations in Lesson 1; Blackadar, II.10.3.16(i), gives the literature statement.
- Free-group property A, the amenable boundary action and its full-to-reduced norm equality are proved in the geodesic-probability section. The example does not require the general equivalence between property A and boundary amenability.
- Equations (2G.1)–(2G.8) construct expanding graphs of increasing girth; (2L.1)–(2L.5) label the entire family with a fixed alphabet; the diagram proof after (2M.1) embeds every vertex set in the finitely generated group. The projection in (2T.2)–(2T.7), with the weighted version (2M.4)–(2M.5), proves the matrix-product failure of middle exactness. These proofs supply the complete nonexact-group example used here; compare [Gomez Aparicio–Julg–Valette 2019, §9.3.3, Theorem 9.12].
- Full crossed products preserve every equivariant short exact sequence by the ideal representation-extension proof of Lesson 1; compare Connes, Chapter II, Appendix C, Proposition 2(b).

We also assume foundational C*-facts: faithful nondegenerate Hilbert-space representations exist; injective C*-homomorphisms are isometric and C*-homomorphisms have closed range; minimal spatial tensor norms are independent of faithful representations. These are ordinary C*-algebra prerequisites. Amenability criteria for general actions, discrete conditional expectations, and characterizations of exact groups require further results; the embedding and tensor-product proofs here do not assume them.

## References

- **[Spielman 2025]** Daniel A. Spielman, *Spectral and Algebraic Graph Theory*, draft of 2 April 2025, Chapter 21, Theorem 21.1.3 and proof, pp.176–180. [Author's book project](https://www.cs.yale.edu/homes/spielman/sagt/).
- **[Esperet–Giocanti 2024]** Louis Esperet and Ugo Giocanti, *Optimization in graphical small cancellation theory*, [arXiv:2306.03474v2](https://arxiv.org/abs/2306.03474v2), Theorem 3.1 and Claim 3.3.
- **[Gruber 2014]** Dominik Gruber, *Groups with graphical C(6) and C(7) small cancellation presentations*, [arXiv:1210.0178v2](https://arxiv.org/abs/1210.0178v2), Lemmas 2.10 and 2.13 and §4. The graphical reduction originates in Yann Ollivier's small cancellation method.
- **[Gomez Aparicio–Julg–Valette 2019]** Maria Paula Gomez Aparicio, Pierre Julg, and Alain Valette, *The Baum-Connes conjecture: an extended survey*, [arXiv:1905.10081](https://arxiv.org/abs/1905.10081). Relevant sections: *Full and reduced C*-algebras*; *Yu's property A: a polymorphous property*, especially *Exactness*.
- **[Connes 1994]** Alain Connes, *Noncommutative Geometry*, Academic Press, 1994. Chapter II, Appendix C, *Crossed Products of C\*-algebras and the Thom Isomorphism*. [Author's electronic edition](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf).
- **[Rosenberg 2012]** Jonathan Rosenberg, *Examples and applications of noncommutative geometry and K-theory*, in Guillermo Cortiñas (ed.), *Topics in Noncommutative Geometry*, Clay Mathematics Proceedings 16, American Mathematical Society and Clay Mathematics Institute, 2012, §2.2, *Basic properties of crossed products*. [Electronic volume](https://www.claymath.org/wp-content/uploads/2022/03/cmip016c.pdf).
- **[Blackadar 2006]** Bruce Blackadar, *Operator Algebras: Theory of C\*-Algebras and von Neumann Algebras*, Encyclopaedia of Mathematical Sciences 122, Springer, 2006, II.10.3.13–16. [Author's revised edition, 2017](https://bruceblackadar.com/Mathematics/Cycr.pdf).
- **[Covariance and crossed products with nonunital coefficients](../prerequisites/src/OA-FLOW/repaired-20261004/covariance-and-crossed-products.md)** Chapter in *Crossed Products & Flow of Weights*, sections *The regular pair and its two faithfulness assertions*, *Why the reduced norm does not depend on the faithful coefficient representation*, and *Full and reduced crossed products and their canonical actions*.
- **[Unitary representations and the two group C* completions](../prerequisites/src/OA-FLOW/repaired-20261004/group-representations-and-completions.md)** Chapter in *Crossed Products & Flow of Weights*, section *A strict gap: the free group on two generators*.
