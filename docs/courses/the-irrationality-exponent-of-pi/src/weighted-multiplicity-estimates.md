# Weighted multiplicity estimates

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A zero estimate converts the vanishing of many derivatives of a polynomial into geometric information. This lesson proves the local estimate behind the zero estimate of this course. Polynomials of weighted degree at most \(N\) whose derivatives along a commuting frame of vector fields vanish on a subvariety \(Z\), up to a weighted order proportional to \(N\), force an inequality between the degree weights of the coordinate directions transverse to \(Z\) and the costs of the vector fields transverse to \(Z\). The vanishing of derivatives gives a lower bound for a local multiplicity on a transverse slice; Bézout's inequality gives an upper bound by degrees. Neither bound depends on the polynomials, on \(Z\), or on \(N\).

We use the weighted Bézout inequality, Corollary 3.2 of [Bézout's inequality for isolated zeros](course:intersection-numbers-and-positivity/bezouts-inequality-for-isolated-zeros#3-the-inequality-for-isolated-zeros); Krull's height theorem, Theorem 3.1 of [Dimension theory of Noetherian local rings](course:AG-CA/dimension-theory-of-noetherian-local-rings#3-how-much-can-one-equation-cut); that the local ring at a smooth point of a complex variety of dimension \(e\) is regular, [Smooth algebras over a field and the Jacobian criterion](course:AG-CA/smooth-algebras-over-a-field-and-the-jacobian-criterion#2-the-criterion-and-its-open-locus), so that its completion is a power series ring in \(e\) variables, by [Coefficient rings and the Cohen structure theorem](course:AG-CA/coefficient-rings-and-cohen-structure). Varieties are over \(\mathbb C\); "general point of \(Z\)" means a point of a dense open subset of \(Z\). For a point \(x\) of a variety, \(\widehat{\mathcal O}_x\) is the completed local ring and \(\mathfrak m_x\) its maximal ideal. Multi-indices have nonnegative integer entries.

## 1. Formal coordinates

**Lemma 1.1** (formal inverse function theorem). Let \(\varphi:\mathbb C[[y_1,\dots,y_n]]\to\mathbb C[[w_1,\dots,w_n]]\) be a homomorphism of \(\mathbb C\)-algebras with \(\varphi(y_i)\in(w_1,\dots,w_n)\), such that the matrix of linear coefficients of the \(\varphi(y_i)\) is invertible. Then \(\varphi\) is an isomorphism.

**Proof.** After composing with a linear change of the \(y_i\), we may assume \(\varphi(y_i)=w_i+(\text{terms of order}\ge2)\). Then \(\varphi\) maps \(\mathfrak m^j\) into \(\mathfrak m^j\), and the induced map \(\mathfrak m^j/\mathfrak m^{j+1}\to\mathfrak m^j/\mathfrak m^{j+1}\) is the identity on homogeneous polynomials of degree \(j\). It is injective: a nonzero series of order \(j\) has an image of order exactly \(j\). It is surjective: given \(s\), choose \(s_0\) with \(s-\varphi(s_0)\in\mathfrak m\), then \(s_1\in\mathfrak m\) with \(s-\varphi(s_0+s_1)\in\mathfrak m^2\), and so on; the series \(s_0+s_1+\dots\) converges in the \(\mathfrak m\)-adic topology, and \(\varphi\) is continuous, so its image is \(s\). \(\square\)

**Lemma 1.2** (exponential of commuting derivations). Let \(R\) be a \(\mathbb Q\)-algebra and \(D_1,\dots,D_k\) pairwise commuting derivations of \(R\). Then

\[
E(f)=\sum_\alpha\frac{D^\alpha f}{\alpha!}\,b^\alpha\in R[[b_1,\dots,b_k]],\qquad D^\alpha=D_1^{\alpha_1}\cdots D_k^{\alpha_k},
\]

is a ring homomorphism \(R\to R[[b]]\).

**Proof.** Additivity is clear. By the Leibniz rule and commutativity, \(D^\alpha(fg)=\sum_{\beta\le\alpha}\binom\alpha\beta D^\beta f\,D^{\alpha-\beta}g\), so the coefficient of \(b^\alpha\) in \(E(fg)\) is \(\sum_{\beta\le\alpha}\frac{D^\beta f}{\beta!}\frac{D^{\alpha-\beta}g}{(\alpha-\beta)!}\), which is the coefficient of \(b^\alpha\) in \(E(f)E(g)\). \(\square\)

For the frame used in this course, \(E\) is the substitution into an explicit flow. On \(\{Y\ne0\}\subset\mathbb C^{m+1}\), with coordinates \(Y,X_1,\dots,X_m\), let

\[
D_0=Y\partial_Y+\sum_{i=1}^m\partial_{X_i},\qquad D_i=\partial_{X_i}\quad(1\le i\le m).
\tag{1.1}
\]

These fields commute and are linearly independent at every point, and for a polynomial \(f\), \(E(f)=f\bigl(Ye^{b_0},X_1+b_0+b_1,\dots,X_m+b_0+b_m\bigr)\), expanded in the \(b\)'s.

## 2. Flow coordinates along a subvariety

Let \(U\subseteq\mathbb C^d\) be a Zariski open subset and \(D_1,\dots,D_d\) pairwise commuting regular vector fields on \(U\) forming a frame: linearly independent at every point. For \(B\subseteq\{1,\dots,d\}\) write \(E_B\) for the exponential of Lemma 1.2 in the variables \(b_\beta\), \(\beta\in B\); it extends to the completed local rings, since the \(D_\beta\) do.

**Definition 2.1.** Let \(Z\subseteq U\) be an irreducible closed subvariety of codimension \(k\ge1\). A set \(A\) of \(k\) coordinate indices is a *coordinate normal basis* of \(Z\) if at a general point \(x\) of \(Z\), \(Z\) is smooth and the vectors \(\partial_{x_a}\), \(a\in A\), span a complement of \(T_xZ\). A set \(B\) of \(k\) frame indices is a *frame normal basis* if the same holds for the vectors \(D_\beta(x)\), \(\beta\in B\).

Both conditions are given by the nonvanishing of determinants on the smooth locus of \(Z\); if they hold at one smooth point, they hold on a dense open subset.

**Lemma 2.2** (flow coordinates). Let \(x\) be a smooth point of \(Z\) at which \(B\) is a frame normal basis. Then

\[
\Psi:\widehat{\mathcal O}_{U,x}\to\widehat{\mathcal O}_{Z,x}[[b_\beta:\beta\in B]],\qquad f\mapsto(E_Bf)|_Z,
\]

where \(|_Z\) restricts each coefficient to \(Z\), is an isomorphism of complete local rings. For each multi-index \(\alpha\) the coefficient of \(b^\alpha\) in \(\Psi(f)\) is \((D_B^\alpha f)|_Z/\alpha!\).

**Proof.** Both sides are power series rings in \(d\) variables: \(\widehat{\mathcal O}_{Z,x}\cong\mathbb C[[z_1,\dots,z_{d-k}]]\) at the smooth point. The map \(\Psi\) is a local homomorphism, and on cotangent spaces it sends the class of \(f\in\mathfrak m_x\) to the pair consisting of \(df|_{T_xZ}\) and the numbers \((D_\beta f)(x)\), \(\beta\in B\). This is the transpose of the linear map \(T_xZ\oplus\mathbb C^B\to T_xU\), \((v,c)\mapsto v+\sum_\beta c_\beta D_\beta(x)\), which is an isomorphism by the normal-basis condition. Lemma 1.1 applies. The formula for the coefficients is the definition of \(E_B\). \(\square\)

## 3. The multiplicity estimate

Give the coordinates \(x_1,\dots,x_d\) positive rational *degree weights* \(\rho_1,\dots,\rho_d\); the weighted degree of \(x^\alpha\) is \(\sum_a\rho_a\alpha_a\). Give the frame fields positive rational *costs* \(\kappa_1,\dots,\kappa_d\); the cost of \(D^\gamma\) is \(\sum_\beta\kappa_\beta\gamma_\beta\).

**Theorem 3.1** (weighted transverse multiplicity). Fix \(\varepsilon>0\). Let \(N>0\), let \(f_1,\dots,f_r\) be polynomials of weighted degree at most \(N\), and let \(Z\) be an irreducible component of \(V(f_1,\dots,f_r)\cap U\) of codimension \(k\ge1\). Suppose that

\[
D^\gamma f_\ell\big|_Z=0\qquad\text{for all }\ell\text{ and all }\gamma\text{ of cost }<\varepsilon N .
\tag{3.1}
\]

Then for every coordinate normal basis \(A\) and every frame normal basis \(B\) of \(Z\),

\[
\prod_{a\in A}\rho_a\le k!\,\varepsilon^{-k}\prod_{\beta\in B}\kappa_\beta .
\tag{3.2}
\]

The bound does not depend on the polynomials, on \(Z\), on \(N\) or on the frame beyond the costs.

**Proof.** Choose a point \(x\in Z\) such that \(Z\) is smooth at \(x\), \(A\) and \(B\) are normal bases at \(x\), and \(x\) lies on no other irreducible component of \(V(f)\cap U\); all three are dense open conditions on \(Z\).

*Step 1: the equations in flow coordinates.* By Lemma 2.2 and (3.1), with \(\gamma\) supported on \(B\), every \(\Psi(f_\ell)\) lies in the ideal of \(\widehat{\mathcal O}_{Z,x}[[b]]\) generated by the monomials \(b^\alpha\) with \(\sum_{\beta\in B}\kappa_\beta\alpha_\beta\ge\varepsilon N\). Let \(\beta_\beta=\Psi^{-1}(b_\beta)\in\widehat{\mathcal O}_{U,x}\). Applying \(\Psi^{-1}\), every \(f_\ell\) lies in the ideal of \(\widehat{\mathcal O}_{U,x}\) generated by the monomials \(\boldsymbol\beta^\alpha\) of cost at least \(\varepsilon N\).

*Step 2: the slice.* Let \(S\subseteq\mathbb C^d\) be the affine subspace through \(x\) on which the coordinates \(x_c\), \(c\notin A\), are fixed; it has dimension \(k\) and coordinates \(x_a\), \(a\in A\), and \(T_xS\) is a complement of \(T_xZ\). The differential of \(\beta_\beta\) at \(x\) is the linear form on \(T_xU=T_xZ\oplus\operatorname{span}(D_B(x))\) that vanishes on \(T_xZ\) and takes the \(D_\beta\)-component. Restricted to \(T_xS\), which maps isomorphically onto \(T_xU/T_xZ\), these \(k\) forms are linearly independent. So the restrictions of the \(\beta_\beta\) form a regular system of parameters of \(\widehat{\mathcal O}_{S,x}\), and by Lemma 1.1, \(\widehat{\mathcal O}_{S,x}=\mathbb C[[\beta_\beta:\beta\in B]]\).

*Step 3: the lower bound.* Let \(J\subseteq\mathcal O_{S,x}\) be the ideal generated by the restrictions \(f_\ell|_S\). By Step 1, \(J\widehat{\mathcal O}_{S,x}\) is contained in the monomial ideal \(\mathfrak M\) generated by the \(\boldsymbol\beta^\alpha\) of cost at least \(\varepsilon N\). Hence

\[
\dim_{\mathbb C}\widehat{\mathcal O}_{S,x}/J\widehat{\mathcal O}_{S,x}\ge\dim_{\mathbb C}\mathbb C[[\boldsymbol\beta]]/\mathfrak M=\#\Bigl\{\alpha\in\mathbb N^B:\sum_\beta\kappa_\beta\alpha_\beta<\varepsilon N\Bigr\}\ge\frac{(\varepsilon N)^k}{k!\prod_{\beta\in B}\kappa_\beta}.
\]

For the last inequality, the simplex \(\{s\in\mathbb R_{\ge0}^B:\sum\kappa_\beta s_\beta<\varepsilon N\}\) is covered by the disjoint unit cubes \(\alpha+[0,1)^B\) over the multi-indices \(\alpha=\lfloor s\rfloor\) it contains, and its volume is \((\varepsilon N)^k/(k!\prod\kappa_\beta)\).

*Step 4: \(x\) is an isolated zero on the slice.* Near \(x\), the zero set \(V(f)\cap U\) coincides with \(Z\). The \(d-k\) functions \(x_c-x_c(x)\), \(c\notin A\), cut out \(S\); restricted to \(Z\), their differentials at \(x\) are independent because \(T_xZ\cap T_xS=0\), so they form a regular system of parameters of \(\mathcal O_{Z,x}\) and \(Z\cap S\) is the reduced point \(x\) near \(x\). Hence \(x\) is an isolated point of \(V(J)\subseteq S\), \(J\) is \(\mathfrak m_x\)-primary, and \(\dim\mathcal O_{S,x}/J=\dim\widehat{\mathcal O}_{S,x}/J\widehat{\mathcal O}_{S,x}\) is finite.

*Step 5: the upper bound.* Let \(W\) be the span of the \(f_\ell|_S\). We choose \(g_1,\dots,g_k\in W\) such that \((g_1,\dots,g_k)\mathcal O_{S,x}\) is \(\mathfrak m_x\)-primary. Suppose \(g_1,\dots,g_i\) chosen, \(i<k\), with all minimal primes of \((g_1,\dots,g_i)\) in the \(k\)-dimensional regular local ring \(\mathcal O_{S,x}\) of height \(i\). None of these finitely many primes \(P\) contains \(J\), since \(J\) is \(\mathfrak m_x\)-primary and \(P\ne\mathfrak m_x\); so \(W\cap P\) is a proper subspace of \(W\), and a general \(g_{i+1}\in W\) lies in none of them. Every minimal prime of \((g_1,\dots,g_{i+1})\) contains a minimal prime of \((g_1,\dots,g_i)\), properly since \(g_{i+1}\) is not in it, so has height at least \(i+1\), and at most \(i+1\) by Krull's height theorem. For \(i+1=k\) the only prime of height \(k\) is \(\mathfrak m_x\).

The \(g_j\) are polynomials in the \(k\) coordinates of \(S\) of weighted degree at most \(N\) (fixing the other coordinates does not raise the weighted degree), and \(x\) is an isolated zero of them. Since \((g)\subseteq J\), Corollary 3.2 of the Bézout lesson gives

\[
\dim\mathcal O_{S,x}/J\le\dim\mathcal O_{S,x}/(g_1,\dots,g_k)\le\frac{N^k}{\prod_{a\in A}\rho_a}.
\]

*Step 6.* Comparing with Step 3, \((\varepsilon N)^k/(k!\prod\kappa_\beta)\le N^k/\prod\rho_a\), which is (3.2). \(\square\)

The proof uses only the derivatives along the fields of \(B\); the hypothesis (3.1) for all \(\gamma\) is convenient because \(B\) is not known in advance.

## 4. Exercises

**Exercise 4.1.** For the frame (1.1), verify that \(D_0\) and \(D_i\) commute, and that \(E(f)=f(Ye^{b_0},X+b_0\mathbf1+b)\).

**Exercise 4.2.** In \(\mathbb C^2\) with coordinates \(x,y\), unit degree weights and the frame \(\partial_x,\partial_y\) with costs \(\kappa_x,\kappa_y\), let \(Z=\{y=0\}\) and \(f=y^N\). For which \(\varepsilon\) does (3.1) hold? Compare with (3.2) and show that (3.2) is sharp in this example.

**Exercise 4.3.** Show that the lattice count in Step 3 is asymptotic to the volume: \(\#\{\alpha:\sum\kappa_\beta\alpha_\beta<T\}\sim T^k/(k!\prod\kappa_\beta)\) as \(T\to\infty\).

**Exercise 4.4.** Explain why Theorem 3.1 would fail without the assumption that \(Z\) is a component of \(V(f)\cap U\) (and not merely contained in it). Give an example with \(Z\) a point on a curve of zeros.

## 5. Solutions

**4.1.** \([D_0,\partial_{X_i}]=-\partial_{X_i}(Y)\partial_Y-\sum_j\partial_{X_i}(1)\partial_{X_j}=0\), and the \(\partial_{X_i}\) commute. The map \(b\mapsto(Ye^{b_0},X+b_0\mathbf1+b)\) satisfies \(\partial_{b_0}f(\cdots)=(D_0f)(\cdots)\) and \(\partial_{b_i}f(\cdots)=(\partial_{X_i}f)(\cdots)\), so its Taylor expansion in \(b\) is \(\sum_\alpha D^\alpha f\,b^\alpha/\alpha!\).

**4.2.** If \(\gamma_1\ge1\), then \(\partial_x^{\gamma_1}\partial_y^{\gamma_2}y^N=0\). If \(\gamma_1=0\), then \(\partial_y^{\gamma_2}y^N\) is a multiple of \(y^{N-\gamma_2}\) for \(\gamma_2\le N\), and \(0\) for \(\gamma_2>N\); it vanishes on \(y=0\) unless \(\gamma_2=N\). So the only derivative not vanishing on \(Z\) is \(\partial_y^Nf=N!\), of cost \(N\kappa_y\), and (3.1) holds if and only if \(N\kappa_y\ge\varepsilon N\), that is, \(\varepsilon\le\kappa_y\). Here \(Z\) is the only component of \(V(f)\), \(k=1\), \(A=\{y\}\), \(B=\{\partial_y\}\), and (3.2) reads \(1\le\kappa_y/\varepsilon\): the same condition. So (3.2) is sharp.

**4.3.** The cubes \(\alpha+[0,1)^k\) with \(\sum\kappa_\beta\alpha_\beta<T\) are contained in the simplex of size \(T+\sum\kappa_\beta\) and cover the simplex of size \(T\); both volumes are \(T^k/(k!\prod\kappa_\beta)(1+O(1/T))\).

**4.4.** If \(Z\) is not a component, a component of larger dimension can contain \(Z\), and Step 4 fails: \(x\) is not isolated on the slice. Take \(f=y\) in \(\mathbb C^2\) with unit degree weights, \(N=1\), and \(Z=\{0\}\), so \(k=2\) and \(A=\{x,y\}\), \(B=\{\partial_x,\partial_y\}\). The only derivative of \(f\) not vanishing at \(0\) is \(\partial_yf=1\), of cost \(\kappa_y\). With \(\kappa_y=\varepsilon=1\) and \(\kappa_x=10^{-6}\), (3.1) holds, but (3.2) would say \(1\le2\cdot10^{-6}\). The slice is the whole plane, on which \(V(f)\) is a line through \(0\).

## References

- [OpenAI-Pi] OpenAI, The irrationality exponent of π is 2, preprint, 24 September 2026. https://github.com/openai/math/tree/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026
- [Philippon] P. Philippon, Lemmes de zéros dans les groupes algébriques commutatifs, Bulletin de la Société Mathématique de France 114 (1986). https://www.numdam.org/articles/10.24033/bsmf.2060/
- [Farhi] B. Farhi, Un lemme de Roth sur les groupes algébriques commutatifs, arXiv:math/0603257 (2006). https://arxiv.org/abs/math/0603257
- [Mondal] P. Mondal, How many zeroes? Counting the number of solutions of systems of polynomials via geometry at infinity, arXiv:1806.05346. https://arxiv.org/abs/1806.05346
