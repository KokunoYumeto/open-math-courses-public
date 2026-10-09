# The mapping torus

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

*Independently authored CC0 lesson; self-checked by the writing AI.*

A mapping torus carries an algebra once around an interval and glues its endpoints by an automorphism. Its K-theory measures the classes fixed by that automorphism and the classes left after quotienting by its change. The endpoint extension determines the connecting maps, including their signs. This also gives the torsion class in the K-theory of the Klein bottle.

All algebras are complex C*-algebras, with external unitizations for nonunital constructions. Fix an automorphism \(\alpha\) of \(A\). We import the natural six-term sequence and positive exponential boundary from [Lesson 11, Theorems 1.1 and 2.1](KT-OPK-11.md). Our two suspension identifications are

\[
\begin{aligned}
\theta_A &:K_1(A)\longrightarrow K_0(SA),\\
\beta_A &:K_0(A)\longrightarrow K_1(SA).
\end{aligned}
\tag{0.1}
\]

They are the isomorphisms proved in [Lesson 8, Theorem 2.1](KT-OPK-08.md#2-the-idempotent-loop-of-an-invertible) and [Lesson 10, Theorem 4.1](KT-OPK-10.md#4-the-boundary-proves-periodicity-and-fixes-its-sign). The first is the index boundary for the cone vanishing at 0, evaluated at 1. The second sends a projection \(p\) in a unital algebra to the positive loop \(t\mapsto e^{2\pi itp}\). These conventions will give \(\alpha_*-1\) in both degrees.

## 1. An extension obtained by gluing endpoints

Define

\[
\begin{aligned}
M_\alpha&=\{f\in C([0,1],A):\\
&\qquad f(1)=\alpha(f(0))\},\\
SA&=\{f\in C([0,1],A):\\
&\qquad f(0)=f(1)=0\}.
\end{aligned}
\tag{1.1}
\]

The endpoint condition is preserved by sums, products and adjoints, and is closed under uniform limits. Thus \(M_\alpha\) is a C*-algebra in the supremum norm. An equivalent description uses continuous functions on \(\mathbb R\) satisfying \(f(t+1)=\alpha(f(t))\): extend from the interval by \(f(n+t)=\alpha^n(f(t))\). The endpoint condition makes this extension continuous at every integer, and automorphisms are isometric.

**Proposition 1.1.** Evaluation at 0 gives an extension

\[
0\longrightarrow SA\xrightarrow{j}M_\alpha
\xrightarrow{q=\operatorname{ev}_0}A\longrightarrow0.
\tag{1.2}
\]

*Proof.* Evaluation is a *-homomorphism. Given \(a\in A\), the continuous function

\[
b_a(t)=(1-t)a+t\alpha(a)
\tag{1.3}
\]

belongs to \(M_\alpha\) and has value \(a\) at 0, so evaluation is onto. This is a bounded linear lift, sufficient for surjectivity; it is generally not multiplicative. If \(q(f)=0\), the endpoint condition gives \(f(1)=0\), so its kernel is exactly \(SA\). \(\square\)

For nonunital \(A\), \((M_\alpha)^+\) consists of \(A^+\)-valued continuous functions whose scalar part is constant and whose endpoints satisfy \(f(1)=\alpha^+(f(0))\). Indeed, subtracting that constant scalar leaves a function in \(M_\alpha\). This is smaller than allowing an arbitrary scalar function around the circle.

## 2. Both connecting maps, with their signs

Write \(\varepsilon_\alpha:K_0(A)\to K_1(SA)\) for the exponential boundary of (1.2), and \(\delta_\alpha:K_1(A)\to K_0(SA)\) for its index boundary.

**Theorem 2.1.** Under the identifications (0.1),

\[
\begin{aligned}
\varepsilon_\alpha&=\beta_A(\alpha_{*,0}-1),\\
\delta_\alpha&=\theta_A(\alpha_{*,1}-1).
\end{aligned}
\tag{2.1}
\]

*Proof.* First consider the endpoint extension

\[
\begin{gathered}
\begin{aligned}
0&\longrightarrow SA\longrightarrow C([0,1],A)\\
&\xrightarrow{r}A\oplus A\longrightarrow0,
\end{aligned}\\
r(f)=(f(0),f(1)).
\end{gathered}
\tag{2.2}
\]

The quotient is onto by linear interpolation. Let its exponential and index boundaries be \(E_0\) and \(E_1\), respectively. We use the canonical coordinate identification \(K_i(A\oplus A)=K_i(A)\oplus K_i(A)\); taking coordinate projections or invertibles gives this identification, including scalar kernels in the nonunital case.

The right cone \(CA=\{f:f(0)=0\}\) includes into the middle algebra of (2.2). This gives a morphism from its cone extension to (2.2), with identity ideal map and quotient map \(a\mapsto(0,a)\). By index-boundary naturality and the definition of \(\theta_A\),

\[
E_1(0,y)=\theta_A(y).
\tag{2.3}
\]

Its exponential boundary is \(\beta_A\). For a projection \(p\) in a unital algebra, the self-adjoint cone lift \(t p\) gives the unitary \(e^{2\pi itp}\), exactly the positive Bott loop. Projection differences generate \(K_0\), so this proves the equality for unital algebras. For arbitrary \(A\), include into \(A^+\). The split extension \(0\to A\to A^+\to\mathbb C\to0\), and its suspension, make the ideal K-group inclusions injective. Naturality and the restriction defining \(\beta_A\) therefore prove the same equality on \(K_0(A)\). Consequently

\[
E_0(0,x)=\beta_A(x).
\tag{2.4}
\]

The diagonal map \(a\mapsto(a,a)\) lifts multiplicatively by constant functions. Exactness therefore says \(E_i(x,x)=0\) in each degree. Additivity, using \((x_0,x_1)=(x_0,x_0)+(0,x_1-x_0)\), now gives

\[
\begin{aligned}
E_0(x_0,x_1)&=\beta_A(x_1-x_0),\\
E_1(y_0,y_1)&=\theta_A(y_1-y_0).
\end{aligned}
\tag{2.5}
\]

Finally, inclusion \(M_\alpha\to C([0,1],A)\) gives a morphism of extensions from (1.2) to (2.2). Its ideal map is identity and its quotient map is

\[
a\longmapsto(a,\alpha(a)).
\tag{2.6}
\]

Applying boundary naturality and (2.5) proves both assertions in (2.1). This proof determines the index sign directly from the cone, without appealing to an unspecified suspended sign convention. \(\square\)

**An explicit exponential check.** For unital \(A\), lift a projection \(p\) by \(b_p(t)=(1-t)p+t\alpha(p)\). Its endpoints are projections, so \(e^{2\pi ib_p(t)}\) is a based unitary loop and represents \(\varepsilon_\alpha[p]\). For a relative projection \(p\in M_n(A^+)\) with scalar projection \(P\), use the same lift with \(\alpha^+\). Its scalar part is \(P\), hence its exponential has scalar part identity; Lesson 11 gives

\[
\begin{gathered}
b_p(t)=(1-t)p+t\alpha^+(p),\\
\varepsilon_\alpha([p]-[P])=[e^{2\pi i b_p}].
\end{gathered}
\tag{2.7}
\]

No commutativity between these projections is assumed. Subtracting \(P\) inside this exponential, or replacing it by the exponential of a difference of projections, does not in general preserve its endpoint values.

For example, let \(p=e_{11}\) in \(M_2(\mathbb C)\), and let \(q=\alpha(p)=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix}\) under a unitary conjugation. Direct multiplication gives \((p-q)^2=\frac12 I_2\), so \(p-q\) has eigenvalues \(\pm1/\sqrt2\). Therefore \(e^{2\pi i(p-q)}\ne I_2\). The path \(e^{2\pi it(p-q)}\) is not a based loop, whereas (2.7) has identity at both endpoints. A difference of projections can represent a K-group difference without being a projection or having integral spectrum as an operator.

For a sign check, take \(A=\mathbb C^2\), let \(\alpha\) exchange the coordinates, and put \(p=(1,0)\). Formula (2.7) is

\[
t\longmapsto(e^{-2\pi it},e^{2\pi it}),
\tag{2.8}
\]

which has winding pair \((-1,1)=\alpha_*[p]-[p]\). The reversed lift \(tp+(1-t)\alpha(p)\) has endpoints \(\alpha(p),p\). It belongs to \(M_\alpha\) only when \(\alpha^2(p)=p\); a cyclic permutation of three coordinate projections shows the general failure.

The conventional expression \(1-\alpha_*\) has the same kernels and images as \(\alpha_*-1\). Replacing each suspension identification by its negative converts (2.1) to that expression. For this course's positive identifications we retain (2.1), because naturality and explicit representatives require the actual map.

**Reversing the interval.** The map \(Rf(t)=f(1-t)\) is an isometric *-isomorphism from \(M_\alpha\) onto \(M_{\alpha^{-1}}\). Indeed, its last value is \(f(0)=\alpha^{-1}(f(1))\), and applying reversal again is its inverse. Its quotient map at 0 is \(\alpha\), since \(q_0 Rf=f(1)=\alpha(q_0 f)\). Its ideal map is the suspension reversal \(\rho(g)(t)=g(1-t)\).

Reversal acts by minus identity under both of our suspension identifications. To verify this without guessing an orientation, reverse the middle functions in the endpoint extension (2.2). This swaps the two quotient coordinates and induces \(\rho\) on the ideal. By naturality, (2.3) and (2.5) give

\[
\begin{aligned}
\rho_*\theta_A(y)&=E_1(y,0)=-\theta_A(y),\\
\rho_*\beta_A(x)&=E_0(x,0)=-\beta_A(x).
\end{aligned}
\tag{2.9}
\]

The morphism of mapping-torus extensions induced by \(R\) therefore intertwines the boundary of \(\alpha\), followed by \(\rho_*\), with the boundary of \(\alpha^{-1}\), preceded by \(\alpha_*\). On coefficient groups the required identity is

\[
(\alpha_*^{-1}-1)\alpha_*=-(\alpha_*-1),
\tag{2.10}
\]

exactly as (2.1) predicts. Thus changing the gluing direction also changes the quotient identification and the suspension orientation. Although \(1-\alpha_*^{-1}\), \(1-\alpha_*\) and \(\alpha_*-1\) have the same kernels and images, their formulas record these different choices. The explicit maps above specify how to compare them and how to transport a representative between the two mapping tori.

## 3. Kernels, cokernels, and the splitting question

The six-term sequence, rewritten using (0.1), runs cyclically as

\[
\begin{gathered}
K_1(A)\xrightarrow{\alpha_{*,1}-1}K_1(A),\\
K_1(A)\xrightarrow{j_*\theta_A}K_0(M_\alpha),\\
K_0(M_\alpha)\xrightarrow{q_*}K_0(A),\\
K_0(A)\xrightarrow{\alpha_{*,0}-1}K_0(A),\\
K_0(A)\xrightarrow{j_*\beta_A}K_1(M_\alpha),\\
K_1(M_\alpha)\xrightarrow{q_*}K_1(A).
\end{gathered}
\tag{3.1}
\]

The final arrow is followed by the first one. For compact notation put \(\sigma_0=\theta_A\) and \(\sigma_1=\beta_A\), so \(\sigma_i:K_{1-i}(A)\to K_i(SA)\).

**Corollary 3.1.** For \(i=0,1\), there is a natural short exact sequence

\[
\begin{gathered}
C_i=\frac{K_{1-i}(A)}{(\alpha_{*,1-i}-1)K_{1-i}(A)},\\
\begin{aligned}
0&\longrightarrow C_i
\xrightarrow{\overline{j_*\sigma_i}}K_i(M_\alpha)\\
&\xrightarrow{q_*}\ker(\alpha_{*,i}-1)\longrightarrow0.
\end{aligned}
\end{gathered}
\tag{3.2}
\]

*Proof.* Exactness of (3.1) says that \(j_*\sigma_i\) has kernel precisely the displayed image of \(\alpha_*-1\), so it induces an injective map from the quotient. Its image equals the kernel of \(q_*\). The image of \(q_*\) equals the displayed kernel, proving surjectivity onto that subgroup. These three statements prove (3.2). If \(\phi:A\to B\) satisfies \(\phi\alpha=\beta\phi\), pointwise application gives \(M_\alpha\to M_\beta\). Together with \(S\phi\) and \(\phi\) it is a morphism of extensions. Boundary naturality and naturality of \(\theta,\beta\) prove the asserted naturality on the kernels and quotients. \(\square\)

A short exact sequence of abelian groups need not split. If its right-hand group is free abelian, choose a basis and a lift of each basis element. Sending each integral linear combination to the same combination of lifts defines a section. This proves a splitting in that case, but it depends on the lifts.

For \(\alpha=1\), constant functions supply a specified section \(c:A\to M_1\) of evaluation. Hence, in the chosen interval coordinate,

\[
\begin{aligned}
K_0(M_1)&\cong K_0(A)\oplus K_1(A),\\
K_1(M_1)&\cong K_1(A)\oplus K_0(A).
\end{aligned}
\tag{3.3}
\]

Explicitly, \((x,y)\mapsto c_*x+j_*\sigma_i y\) is the degree-\(i\) isomorphism. This agrees with the coefficient-circle result of [Lesson 12, Theorem 5.1](KT-OPK-12.md#5-adding-circles-with-arbitrary-coefficients). For a general automorphism, the kernel and cokernel alone do not determine the extension class of (3.2).

## 4. Moving the gluing automorphism continuously

A path of automorphisms is **point-norm continuous** if \(s\mapsto\alpha_s(a)\) is norm continuous for every \(a\in A\).

**Theorem 4.1 (isomorphism under homotopy and conjugacy).** Suppose \(\alpha_s\) is such a path from \(\alpha\) to \(\gamma^{-1}\beta\gamma\), where \(\beta,\gamma\in\operatorname{Aut}(A)\). Then \(M_\alpha\cong M_\beta\) as C*-algebras.

*Proof.* Define

\[
\begin{gathered}
\eta_t=\beta^{-1}\gamma\alpha_t,\\
\eta_0=\beta^{-1}\gamma\alpha,
\qquad\eta_1=\gamma,\\
(\Phi f)(t)=\eta_t(f(t)).
\end{gathered}
\tag{4.1}
\]

This function is continuous. At \(t_0\), use isometry to bound its difference by

\[
\begin{aligned}
&\|f(t)-f(t_0)\|\\
&\quad+\|\eta_t(f(t_0))-\eta_{t_0}(f(t_0))\|,
\end{aligned}
\tag{4.2}
\]

which tends to zero. Its boundary satisfies

\[
\begin{aligned}
\beta((\Phi f)(0))
&=\gamma\alpha(f(0))\\
&=\gamma(f(1))=(\Phi f)(1).
\end{aligned}
\tag{4.3}
\]

Thus \(\Phi\) maps into \(M_\beta\), preserves pointwise algebra operations and adjoints, and is isometric in the supremum norm.

The inverses also form a point-norm continuous path: for fixed \(a\),

\[
\begin{gathered}
\|\eta_t^{-1}(a)-\eta_{t_0}^{-1}(a)\|\\
=\|a-\eta_t\eta_{t_0}^{-1}(a)\|\longrightarrow0.
\end{gathered}
\tag{4.4}
\]

The same continuity estimate as (4.2) therefore applies to \(f(t)=\eta_t^{-1}(g(t))\). For \(g\in M_\beta\), its endpoints obey

\[
\begin{aligned}
f(0)&=\alpha^{-1}\gamma^{-1}\beta(g(0)),\\
f(1)&=\gamma^{-1}(g(1))\\
&=\gamma^{-1}\beta(g(0))=\alpha(f(0)).
\end{aligned}
\tag{4.5}
\]

So this is an inverse into \(M_\alpha\), proving the theorem. \(\square\)

The quotient map at 0 intertwines \(\Phi\) with \(\eta_0\), not generally with \(\gamma\) itself. Their induced K-maps agree because \(\eta_t\) is a homotopy from \(\eta_0\) to \(\gamma\). The proof needs a path of automorphisms: a homotopy through arbitrary homomorphisms does not provide the pointwise inverse used above.

Two useful special cases have simpler formulas. If \(\beta=\gamma\alpha\gamma^{-1}\), constant pointwise application \(f\mapsto\gamma\circ f\) gives the isomorphism. If

\[
\beta=\operatorname{Ad}(u)\alpha,
\qquad u\in U_0(M(A)),
\tag{4.6}
\]

choose a norm-continuous unitary path \(u_t\) from \(1\) to \(u\). Here \(M(A)\) denotes the multiplier algebra, and for unital \(A\) we may use \(A\) itself. Then

\[
(\Psi f)(t)=u_t f(t)u_t^*
\tag{4.7}
\]

is an isomorphism \(M_\alpha\to M_\beta\): its values at 0 and 1 are \(f(0)\) and \(u\alpha(f(0))u^*\). Continuity follows from norm continuity of \(u_t\) and \(f\); conjugation preserves \(A\). Conjugation by \(u_t^*\) gives the inverse, whose endpoint condition follows by reversing the same computation. Membership of \(u\) in the identity component supplies the required path.

### From mapping tori to crossed products

The preceding isomorphism also controls crossed-product K-groups, even when the coefficient groups have torsion. We now use three complete proofs already written in this programme: [*Green's imprimitivity theorem*, Theorem 7.4](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-CP/KT-CP-07.html#completion-in-the-full-crossed-product-norms) and [equations (7.45)–(7.47)](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-CP/KT-CP-07.html#finite-coset-spaces-and-mapping-tori), [*Morita invariance of K-theory and correspondence maps*, Theorem 2.4 and Corollary 2.5](https://kokunoyumeto.github.io/open-math-courses-public/courses/hilbert-c-star-modules-and-morita-equivalence/morita-invariance-of-k-theory-and-correspondence-maps.html#2-full-multiplier-corners), and [*The Connes–Thom isomorphism*, Theorem 11.3](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-CP/KT-CP-11.html#surjectivity-first-unital-and-then-general). Their proofs cover arbitrary C*-algebras. The Morita proof obtains the actual linking-corner maps, first for separable full corners and then by directed continuity; it does not require a countable approximate identity in the present algebra. The Thom proof makes both Wiener–Hopf boundaries bijective. We retain those precise maps and prove their application to our endpoint convention below. All crossed products in this comparison are full crossed products.

**Proposition 4.2 (the crossed-product comparison).** For every C*-algebra \(A\) and every \(\alpha\in\operatorname{Aut}(A)\), there are isomorphisms

\[
\begin{gathered}
\Xi_{\alpha,i}:K_i(A\rtimes_\alpha\mathbb Z)\\
\longrightarrow K_{i-1}(M_\alpha),\\
i=0,1,
\end{gathered}
\tag{4.8}
\]

with degrees read modulo two.

*Proof.* Extend \(F\in M_\alpha\) to the real line as in Section 1 and set

\[
(\tau_rF)(t)=F(t+r).
\tag{4.9}
\]

Since \(F(t+1)=\alpha(F(t))\), the translated function has the same covariance and belongs to \(M_\alpha\). Translation preserves pointwise algebra operations and adjoints, and \(\tau_{-r}\) is its inverse. The continuous function \(t\mapsto\|F(t)\|\) is one-periodic; its supremum on any interval of length one is therefore \(\|F\|\). Thus each \(\tau_r\) is isometric. Uniform continuity of \(F\) on \([-1,2]\) gives \(\|\tau_rF-F\|\to0\) as \(r\to0\). The group law and isometry give continuity at every \(r\), so this is a point-norm continuous real action, with no separability hypothesis.

For Green's theorem choose \(G=\mathbb R\), \(H=\mathbb Z\) and the action \(n\mapsto\alpha^n\). Its induced algebra consists of continuous functions \(f\) such that \(f(t+n)=\alpha^{-n}(f(t))\). The norm on the compact quotient is bounded automatically. Reflection \(F(t)=f(-t)\) identifies it isometrically with \(M_\alpha\): indeed \(F(t+n)=\alpha^n(F(t))\). The inverse is the same reflection after the quasi-periodic extension. Green's left translation \((\operatorname{lt}_rf)(t)=f(t-r)\) becomes exactly (4.9), since

\[
\begin{aligned}
(\operatorname{lt}_rf)(-t)&=f(-t-r)\\
&=F(t+r).
\end{aligned}
\tag{4.10}
\]

Consequently the cited complete imprimitivity proof supplies an equivalence between

\[
\begin{aligned}
B&=A\rtimes_\alpha\mathbb Z,\\
C&=M_\alpha\rtimes_\tau\mathbb R.
\end{aligned}
\tag{4.11}
\]

Orient its bimodule as a \(B\)–\(C\) module \(X\), taking the conjugate Green module if necessary. Its linking algebra is \(L=\mathcal K(X\oplus C)\), with full diagonal corner inclusions \(i_B,i_C\). Corollary 2.5 of the Morita lesson proves that both corner K-maps are invertible and that \(\mu_{X,i}=(i_{C*})^{-1}i_{B*}:K_i(B)\to K_i(C)\) is an isomorphism. Theorem 11.3 of the Thom lesson proves that the degree-\(i\) Wiener–Hopf boundary \(\partial_i^\tau:K_i(C)\to K_{i-1}(M_\alpha)\) is an isomorphism. Define

\[
\Xi_{\alpha,i}=\partial_i^\tau\,\mu_{X,i}.
\tag{4.12}
\]

This is a composition of the two specified isomorphisms. Reflection (4.10) fixes which gluing automorphism and real flow they use; no replacement of \(\alpha\) by its inverse is implicit. This proves (4.8). \(\square\)

**Corollary 4.3 (homotopy of automorphisms).** Under the hypotheses of Theorem 4.1, for both degrees,

\[
\begin{gathered}
K_i(A\rtimes_\alpha\mathbb Z)
\\\cong K_i(A\rtimes_\beta\mathbb Z).
\end{gathered}
\tag{4.13}
\]

*Proof.* Theorem 4.1 gives the actual isomorphism \(\Phi:M_\alpha\to M_\beta\), hence an isomorphism on each mapping-torus K-group. The required isomorphism is the composition \(\Xi_{\beta,i}^{-1}\,\Phi_*\,\Xi_{\alpha,i}\). Every factor has an inverse. No freeness, unitality or countability condition is used. \(\square\)

This conclusion uses a path through automorphisms, including its pointwise inverse in Theorem 4.1. Equality of the induced coefficient K-maps alone does not give that path or split the sequences (3.2). Moreover \(\Phi\) need not intertwine the translation flows. Formula (4.13) compares their K-groups through the mapping tori; it does not apply crossed-product functoriality to a nonequivariant \(\Phi\), or assert an isomorphism of the crossed-product algebras. These distinctions allow the same argument to handle torsion in Lessons 21 and 23.

## 5. Gluing spaces: the torus and the Klein bottle

Let \(X\) be compact Hausdorff and \(\varphi:X\to X\) a homeomorphism. Set \(\alpha=\varphi^*\), meaning \(\alpha(a)(x)=a(\varphi(x))\), and form

\[
\begin{gathered}
X_\varphi=(X\times[0,1])/\!\sim,\\
(x,1)\sim(\varphi(x),0).
\end{gathered}
\tag{5.1}
\]

The equivalence relation is closed: it consists of the diagonal and the two closed endpoint graphs. The quotient is compact Hausdorff. A norm-continuous function \(f:[0,1]\to C(X)\) corresponds to the continuous function \(F(x,t)=f(t)(x)\). Joint continuity follows from uniform norm continuity in \(t\) and continuity in \(x\). Conversely, a continuous function on the compact product is norm continuous as a \(C(X)\)-valued function: continuity near each point of a fixed slice, followed by a finite cover of \(X\), bounds the difference uniformly in \(x\). The gluing condition is exactly

\[
F(x,1)=F(\varphi(x),0).
\tag{5.2}
\]

Such functions descend continuously through the quotient, and all quotient functions pull back this way. Suprema agree and operations are pointwise, proving an isometric *-isomorphism

\[
M_{\varphi^*}\cong C(X_\varphi).
\tag{5.3}
\]

For \(\varphi=1\) and \(X=S^1\), the space is the two-dimensional torus. The identity case (3.3), with \(K_0(C(S^1))=K_1(C(S^1))=\mathbb Z\), gives \(K^0(T^2)=K^1(T^2)=\mathbb Z^2\). Rank and positive winding are the generators of the coefficient groups, by [Lesson 6, Theorem 5.2](KT-OPK-06.md#5-components-detected-by-spectra-winding-and-index).

**Proposition 5.1 (Klein bottle).** For the Klein bottle \(\mathcal K=X_\varphi\), where \(X=S^1\) and \(\varphi(z)=\overline z\),

\[
\begin{aligned}
K^0(\mathcal K)&=\mathbb Z\oplus\mathbb Z/2,\\
K^1(\mathcal K)&=\mathbb Z.
\end{aligned}
\tag{5.4}
\]

*Proof.* On \(K_0(C(S^1))\), \(\alpha_*\) is identity: it fixes the rank-one generator. On \(K_1\), it sends the coordinate unitary \(z\) to \(\overline z=z^{-1}\), which has winding \(-1\). Thus \(\alpha_*-1\) is zero in degree 0 and multiplication by \(-2\) in degree 1. Formula (3.2) becomes

\[
\begin{aligned}
0&\longrightarrow\mathbb Z/2\longrightarrow K_0(M_\alpha)\\
&\xrightarrow{q_*}\mathbb Z\longrightarrow0,\\
0&\longrightarrow\mathbb Z\xrightarrow{j_*\beta_A}K_1(M_\alpha)\\
&\longrightarrow0\longrightarrow0.
\end{aligned}
\tag{5.5}
\]

The first sequence splits by \(n\mapsto n[1_{M_\alpha}]\), since evaluation sends the unit to the coefficient generator. Its injected torsion generator is \(j_*\theta_A[z]\), of exact order 2 because the induced map from the cokernel is injective. The second sequence identifies its group with \(\mathbb Z\), generated by the base-circle unitary

\[
w(t)=e^{2\pi it}1_A.
\tag{5.6}
\]

Its endpoints are identity, so it is a based loop over \(SA\) and its image is in \(M_\alpha\). The rank-one class and the order-two class prove the first isomorphism; the second sequence proves the second. Equation (5.3) and the definition of topological K-theory in [Lesson 12](KT-OPK-12.md) finish the claim. \(\square\)

## 6. Five exercises with complete solutions

**Exercise 17.1 (identity and coefficients).** Identify \(M_1\), and give both coefficient-circle isomorphisms with their maps.

*Solution.* When \(\alpha=1\), (1.1) consists precisely of continuous functions on the interval with equal endpoints. The quotient \([0,1]/\{0,1\}\cong S^1\) identifies this algebra isometrically with \(C(S^1,A)\). Evaluation has the *-homomorphic section of constant functions \(c\), so both boundaries vanish. For degree \(i\), the map \((x,y)\mapsto c_*x+j_*\sigma_i y\) has inverse as follows: send \(h\) to \(q_*h\) in its first coordinate. The difference \(h-c_*q_*h\) lies in \(\ker q_*\), which equals the image of the injective \(j_*\sigma_i\); use its unique preimage as the second coordinate. This proves both maps are mutually inverse and recovers (3.3) without making a splitting choice.

**Exercise 17.2 (Klein bottle generators).** Compute the groups, the evaluation maps and explicit generators of the Klein bottle.

*Solution.* Complex conjugation acts by \(+1\) on rank and \(-1\) on winding, so the two change maps are \(0\) and \(-2\). In degree 0 the cokernel of the winding change is \(\mathbb Z/2\), and the kernel of the rank change is \(\mathbb Z\). The unit supplies a lift of 1 in the latter, so every class is uniquely \(n[1]+e\,j_*\theta[z]\), with \(n\in\mathbb Z\) and \(e\in\{0,1\}\). Evaluation gives \(n\), and the second summand has exact order 2 by injectivity from the cokernel. In degree 1 the cokernel of the rank change is \(\mathbb Z\), while the kernel of multiplication by \(-2\) is zero. Thus \(j_*\beta\) is an isomorphism, every class is an integer multiple of \([w]\) in (5.6), and evaluation in degree 1 is zero. These determine the maps as well as the groups.

**Exercise 17.3 (the automorphism-homotopy theorem).** Prove Blackadar's Proposition 10.5.1, including its conjugacy version and continuity of the inverse.

*Solution.* Let \(\alpha_t\) join \(\alpha\) to \(\gamma^{-1}\beta\gamma\). Put \(\eta_t=\beta^{-1}\gamma\alpha_t\) and \(\Phi(f)(t)=\eta_t(f(t))\). Estimate (4.2) proves continuity using only point-norm continuity. Its endpoints obey \(\beta\eta_0=\gamma\alpha\) and \(\eta_1=\gamma\), hence \(\beta\Phi(f)(0)=\Phi(f)(1)\). It is a pointwise *-homomorphism and an isometry. Formula (4.4) proves point-norm continuity of the inverses, and the same estimate proves continuity of \(\eta_t^{-1}(g(t))\). Equation (4.5) verifies the inverse's endpoint condition. Pointwise composition in both orders is identity. With \(\gamma=1\) this proves the homotopy case; the general construction proves the conjugacy version. No finite-dimensional or unital hypothesis was used.

**Exercise 17.4 (conjugation and an inner perturbation).** Give direct isomorphisms for conjugate automorphisms and for \(\beta=\operatorname{Ad}(u)\alpha\) with \(u\in U_0(M(A))\).

*Solution.* In the conjugate case \(\beta=\gamma\alpha\gamma^{-1}\), use \(\Phi(f)(t)=\gamma(f(t))\). Its last value is \(\gamma\alpha(f(0))=\beta\gamma(f(0))\); applying \(\gamma^{-1}\) pointwise gives the inverse. In the inner case choose a norm-continuous path \(u_t\) from 1 to \(u\) and use (4.7). Its last value is \(u\alpha(f(0))u^*=\beta(f(0))\), and its first is \(f(0)\). For \(g\in M_\beta\), the proposed inverse has first value \(g(0)\) and last value \(u^*\beta(g(0))u=\alpha(g(0))\), so it belongs to \(M_\alpha\). Both maps preserve products and adjoints, are continuous isometries, and compose to identity. The path makes the construction valid in the multiplier algebra because its conjugations preserve the essential ideal \(A\).

**Exercise 17.5 (a two-point circle and the sign).** Let \(A=\mathbb C^2\) and let \(\alpha\) exchange the coordinates. Identify its mapping torus, compute its groups and maps, and verify explicitly that \(j_*\beta([p]-[q])=0\) for \(p=(1,0),q=(0,1)\).

*Solution.* Write \(f(t)=(f_1(t),f_2(t))\). The conditions are \(f_1(1)=f_2(0)\) and \(f_2(1)=f_1(0)\). Concatenate \(f_1\) on \([0,1]\) and \(f_2\) on \([1,2]\); these conditions give a continuous function on the circle \(\mathbb R/2\mathbb Z\). Concatenation and restriction are inverse isometric *-homomorphisms. Therefore both K-groups are \(\mathbb Z\).

In degree 0, evaluation sends rank \(n\) to \((n,n)\). The image of \(\alpha_*-1\) on \(K_0(A)=\mathbb Z^2\) is \(\mathbb Z(1,-1)\), with kernel the diagonal. Its cokernel is identified with \(\mathbb Z\) by the sum of coordinates. Since \(K_1(A)=0\), (3.2) makes evaluation in degree 0 an isomorphism onto that diagonal, and makes \(j_*\beta\) in degree 1 the sum map. Directly, the two based loops for ranks \(a,b\) concatenate with total winding \(a+b\).

For the requested nullhomotopy, put \(h(t)=(t,1-t)\). Its last value is the exchange of its first, so \(h\in M_\alpha\). The unitaries

\[
\begin{gathered}
U_s(t)=\exp(2\pi i s h(t)),\\
0\leq s\leq1,
\end{gathered}
\tag{6.1}
\]

belong to \(M_\alpha\), because functional calculus preserves the endpoint condition. At \(s=0\) they are identity; at \(s=1\) they are \((e^{2\pi it},e^{-2\pi it})\), the representative of \(j_*\beta([p]-[q])\). Thus that nonzero coefficient class dies after inclusion, as also predicted by exactness. Finally the connecting loop for \([p]\) is (2.8), giving \((-1,1)\) and confirming the sign in Theorem 2.1. This example also explains why a subgroup of a suspension K-group cannot automatically be regarded as an injected subgroup of the mapping torus's K-group.

## Sources and precise imports

- B. Blackadar, *K-Theory for Operator Algebras*, second edition (1998), §§10.3–10.5, printed pp. 74–77: mapping-torus definition, Proposition 10.4.1 on its boundary, and Proposition 10.5.1 on homotopy and conjugacy. Both boundary signs, the full mapping-torus homotopy theorem, and the crossed-product K comparison of Corollary 10.5.2 are proved above using exact programme prerequisites. The proposed reversed projection lift in the boundary argument is replaced by (1.3); relative exponentials use (2.7). [Author's corrected second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf).
- J. Rosenberg, “Examples and applications of noncommutative geometry and K-theory,” in *Topics in Noncommutative Geometry* (2012), §2.5, printed p. 108: the mapping-torus sequence and its place in the crossed-product computation. The mapping-torus part is proved directly; Proposition 4.2 uses the complete Green, linking-corner and Wiener–Hopf proofs in the three programme lessons named there.
- The complete programme proofs used in Section 4 were checked at their published source versions: [Green's theorem](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-CP/KT-CP-07.html#completion-in-the-full-crossed-product-norms), [arbitrary Morita invariance](https://kokunoyumeto.github.io/open-math-courses-public/courses/hilbert-c-star-modules-and-morita-equivalence/morita-invariance-of-k-theory-and-correspondence-maps.html#2-full-multiplier-corners), and [the Thom theorem](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-CP/KT-CP-11.html#surjectivity-first-unital-and-then-general). The endpoint reflection, continuous real action and composition of actual K-maps are proved here. This supplies the asserted group comparison; the separate Kasparov-equivalence context in Lesson 21 retains its own proof obligation.
- Lessons 8, 10 and 11 supply the exact suspension maps, positive exponential formula, boundary naturality and six-term exactness. Lessons 6 and 12 supply circle generators and the definition of topological K-theory. These exact imports are used rather than reproved.

The kernel-cokernel sequences describe the possible extension of groups; a splitting is asserted only when a section or basis-lifting argument has been given. The compact-space identification uses the stated pullback convention \(\varphi^*a=a\circ\varphi\). These choices keep endpoint directions, signs and generators consistent throughout.
