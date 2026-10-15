# The absence of interior critical points

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the hot-spots theorem stated in [Neumann eigenfunctions and the hot-spots problem](neumann-eigenfunctions-and-the-hot-spots-problem.md) (Theorem 5.1 there): no eigenfunction of the first positive Neumann eigenvalue of a bounded simply connected planar domain with smooth boundary has an interior critical point. The conditionally negative kernel of [Reciprocal kernels and conditional negativity](reciprocal-kernels-and-conditional-negativity.md) is a squared distance in a Hilbert space; its coordinates are scalar multipliers to which the multiplier identity of [Boundary kernels and the multiplier identity](boundary-kernels-and-the-multiplier-identity.md) applies. At a critical point the multiplied boundary gradients are all gradients of eigenfunctions, and this contradicts either the multiplicity bound or unique continuation.

- Squared distances in a Hilbert space (Section 1).
- The proof of the theorem (Section 2).
- Later developments (Section 3).

Notation is that of the earlier lessons: \(\Phi\colon\mathbb D\to\Omega\) is the conformal map of [Conformal coordinates, Hopf's lemma and boundary signs](conformal-coordinates-hopfs-lemma-and-boundary-signs.md), \(q=\mu|\Phi'|^2dx\) is the conformal potential, \(K\), \(R\), \(N\) are its kernels, \(E\) is the boundary energy, and \(D_p(s,t)=K(p,s)K(p,t)/N(s,t)\).

## 1. Squared distances in a Hilbert space

**Lemma 1.1** ([OpenAI-HS, Lemma 6.1]). For every \(p\in\mathbb D\) there are a separable real Hilbert space \(\mathcal H\) and an injective Lipschitz map \(b\colon\mathbb S^1\to\mathcal H\) with
\[
\begin{gathered}
\|b(s)-b(t)\|^2=D_p(s,t)\\
(s,t\in\mathbb S^1).
\end{gathered} \tag{1.1}
\]

*Proof.* Fix \(s_0\in\mathbb S^1\) and put
\[
\begin{aligned}
\Gamma(s,t)&=\tfrac12\bigl(D_p(s,s_0)+D_p(t,s_0)\\
&\qquad-D_p(s,t)\bigr).
\end{aligned}
\]
This kernel is positive semidefinite: given points \(s_1,\dots,s_n\) and real \(c_1,\dots,c_n\), adjoin \(s_0\) with \(c_0=-\sum_ic_i\); Theorem 2.1 of the previous lesson gives
\[
\begin{aligned}
0&\ge\sum_{i,j\ge0}c_ic_jD_p(s_i,s_j)\\
&=\sum_{i,j\ge1}c_ic_jD_p(s_i,s_j)\\
&\quad-2\Bigl(\sum_jc_j\Bigr)\sum_ic_iD_p(s_i,s_0),
\end{aligned}
\]
and the right side is \(-2\sum_{i,j\ge1}c_ic_j\Gamma(s_i,s_j)\). On the space of finitely supported real functions on \(\mathbb S^1\), \(\Gamma\) defines a positive semidefinite bilinear form; dividing by its null space and completing gives a real Hilbert space in which the class \(b(s)\) of the indicator of \(\{s\}\) satisfies \(\langle b(s),b(t)\rangle=\Gamma(s,t)\). Since \(D_p(s,s)=0\), \(\Gamma(s,s)=D_p(s,s_0)\), and
\[
\begin{aligned}
&\|b(s)-b(t)\|^2\\
&\quad=\Gamma(s,s)+\Gamma(t,t)-2\Gamma(s,t)\\
&\quad=D_p(s,t).
\end{aligned}
\]

For \(s\ne t\), \(K(p,s)K(p,t)>0\) and \(N(s,t)<\infty\) (Lemma 4.1 of [Boundary kernels and the multiplier identity](boundary-kernels-and-the-multiplier-identity.md)), so \(D_p(s,t)>0\) and \(b\) is injective. Since \(N\ge N_0\),
\[
\|b(s)-b(t)\|^2\le\pi\,\|K(p,\cdot)\|_\infty^2\,|s-t|^2,
\]
so \(b\) is Lipschitz. Replace \(\mathcal H\) by the closed span of \(b(\mathbb S^1)\); it is separable, being spanned by the images of a countable dense subset of the circle. \(\square\)

Kernels of the form \(\|b(s)-b(t)\|^2\) are always conditionally negative semidefinite, as in Remark 2.2 of the previous lesson; the construction above shows the converse.

## 2. The proof of the theorem

*Proof of Theorem 5.1 of the first lesson.* Let \(0\ne u\in V\), and let \(g(s)=(\nabla u)(\Phi(s))\) be its boundary gradient on the circle, as in (6.1) of [Boundary kernels and the multiplier identity](boundary-kernels-and-the-multiplier-identity.md). Suppose that \(\nabla u\) vanishes at the point \(\Phi(p)\), \(p\in\mathbb D\).

*Step 1: the multipliers produce eigenfunctions.* Let \(b\) be as in Lemma 1.1 for this \(p\), let \((e_j)\) be a finite or countable orthonormal basis of \(\mathcal H\), and let \(b_j(s)=\langle b(s),e_j\rangle\). Each \(b_j\) is a real Lipschitz function, so Proposition 6.2 of [Boundary kernels and the multiplier identity](boundary-kernels-and-the-multiplier-identity.md) applies:
\[
\begin{aligned}
E(b_jg)&=\frac12\iint N(s,t)(b_j(s)-b_j(t))^2\\
&\qquad\cdot g(s)\cdot g(t)\,ds\,dt .
\end{aligned}
\]
By Parseval's identity, \(\sum_j(b_j(s)-b_j(t))^2=D_p(s,t)\), so for every partial sum the absolute value of the integrand is at most
\[
\begin{aligned}
&N(s,t)D_p(s,t)|g(s)||g(t)|\\
&\quad=K(p,s)K(p,t)|g(s)||g(t)|,
\end{aligned}
\]
which is bounded. By dominated convergence and (4.2) of that lesson, applied componentwise,
\[
\begin{aligned}
&\sum_jE(b_jg)\\
&\quad=\frac12\iint K(p,s)K(p,t)\\
&\qquad\cdot g(s)\cdot g(t)\,ds\,dt\\
&\quad=\frac12\Bigl|\int_{\mathbb S^1}K(p,s)g(s)\,ds\Bigr|^2\\
&\quad=\frac12|W_g(p)|^2 .
\end{aligned}
\]
By Lemma 6.1 there, \(W_g(p)=\nabla u(\Phi(p))=0\). Every summand is nonnegative by (5.1) there, so \(E(b_jg)=0\) for every \(j\), and by (5.1) again there is \(v_j\in V\) with \(X_{b_jg}=\nabla v_j\). The function \((\nabla v_j)\circ\Phi\) lies in \(C^\infty(\overline{\mathbb D})\), and its trace equals the trace \(b_jg\) of \(W_{b_jg}\); both are continuous, so
\[
\begin{gathered}
(\nabla v_j)(\Phi(s))=b_j(s)g(s)\\
(s\in\mathbb S^1).
\end{gathered} \tag{2.1}
\]

*Step 2: \(g\) does not vanish identically.* Let \(S_g=\{s\in\mathbb S^1:g(s)\ne0\}\), an open set. If it were empty, each \(w=\partial_iu\in C^\infty(\overline\Omega)\) would vanish on \(\partial\Omega\) and satisfy \(\Delta w+\mu w=0\); then \(w\in H^1_0(\Omega)\) and \(\int|\nabla w|^2=\mu\int w^2\), which forces \(w=0\) because \(\mu<\lambda_D\). So \(u\) would be constant, and \(\mu u=-\Delta u=0\) would give \(u=0\).

*Step 3: the case where \(S_g\) is dense.* The set \(b(S_g)\) is not contained in an affine line of \(\mathcal H\). Otherwise, by continuity and density, \(b(\mathbb S^1)\) would lie in that line, and \(b\) would be a continuous injection of the circle into a copy of \(\mathbb R\). Its image would be a compact interval \([\alpha,\beta]\) with \(\alpha<\beta\), and \(b\) would be a homeomorphism onto it; but removing an interior point disconnects the interval, while the circle with one point removed is connected.

Choose distinct \(s_1,s_2\in S_g\), and then \(s_3\in S_g\) with \(b(s_3)\) off the line through \(b(s_1)\) and \(b(s_2)\). The vectors \(y_1=b(s_2)-b(s_1)\) and \(y_2=b(s_3)-b(s_1)\) are linearly independent. Some coordinates \(j,k\) have \(\langle y_1,e_j\rangle\langle y_2,e_k\rangle-\langle y_1,e_k\rangle\langle y_2,e_j\rangle\ne0\): if all these \(2\times2\) minors vanished, a nonzero coordinate \(\langle y_1,e_j\rangle\) would make every coordinate of \(y_2\) proportional to that of \(y_1\). Subtracting the first row from the others shows
\[
\det\begin{pmatrix}1&b_j(s_1)&b_k(s_1)\\1&b_j(s_2)&b_k(s_2)\\1&b_j(s_3)&b_k(s_3)\end{pmatrix}\ne0 .
\]
So \(1,b_j,b_k\) are linearly independent on \(\{s_1,s_2,s_3\}\). Since \(g(s_i)\ne0\), the functions \(g,b_jg,b_kg\) are linearly independent. By (2.1) they are the boundary gradients of \(u,v_j,v_k\in V\), which are therefore linearly independent. This contradicts \(\dim V\le2\) (Proposition 5.2 of [Conformal coordinates, Hopf's lemma and boundary signs](conformal-coordinates-hopfs-lemma-and-boundary-signs.md)).

*Step 4: the case where \(S_g\) is not dense.* Then \(g=0\) on a nonempty open arc \(I\). Since \(S_g\) is nonempty and open, it has at least two points; \(b\) is injective, so by Parseval's identity some \(b_j\) is not constant on \(S_g\). Then \(g\) and \(b_jg\) are linearly independent: if \(\alpha g+\beta b_jg=0\), then \(\alpha+\beta b_j=0\) on \(S_g\), so \(\beta=0\) and \(\alpha=0\). Hence \(u\) and \(v_j\) are linearly independent. Their gradients vanish on the boundary arc \(\Phi(I)\), so each is constant on it. Choose \((\alpha,\beta)\ne(0,0)\) such that \(w=\alpha u+\beta v_j\) vanishes on \(\Phi(I)\). Then \(w\in V\), \(w\ne0\), and \(w=0\), \(\partial_\nu w=0\) on \(\Phi(I)\).

Let \(x_0\in\Phi(I)\), and take a boundary chart at \(x_0\) whose rectangle \(U\) satisfies \(\partial\Omega\cap U\subseteq\Phi(I)\). Extend \(w\) by zero: \(\tilde w=w\) on \(\Omega\cap U\) and \(\tilde w=0\) on \(U\setminus\Omega\). For \(\phi\in C^\infty_c(U)\), Green's formula (2.2) of the first lesson, applied twice, gives
\[
\begin{aligned}
&\int_U\tilde w(\Delta\phi+\mu\phi)=\int_\Omega(\Delta w+\mu w)\phi\\
&\quad+\int_{\partial\Omega}(w\,\partial_\nu\phi-\phi\,\partial_\nu w)\,ds=0,
\end{aligned}
\]
because \(\Delta w+\mu w=0\) and both \(w\) and \(\partial_\nu w\) vanish on \(\partial\Omega\cap U\). So \((\Delta+\mu)\tilde w=0\) in the sense of distributions on \(U\), and \(\tilde w\) is real analytic in \(U\) ([Anisotropic derivative classes and analyticity](course:constant-coefficient-equations-and-solvability/AN02-L031), Theorem 3.1). It vanishes on the nonempty open set \(U\setminus\overline\Omega\), and \(U\) is connected, so \(\tilde w=0\) on \(U\). Thus \(w\) vanishes on the nonempty open set \(\Omega\cap U\), and \(w=0\) by Proposition 3.1(4) of the first lesson, a contradiction.

Both cases are impossible, so \(\nabla u\) does not vanish in \(\Omega\). \(\square\)

The zero extension in Step 4 is a local form of a lemma of Filonov [Fil04, Lemma, p. 173]. No analyticity of the boundary is needed: only the vanishing of both Cauchy data on the arc.

## 3. Later developments

Burdzy, and independently Bañuelos, reduced a non-strict hot-spots statement on general simply connected planar domains to the smooth theorem proved in this course [Bur26]. Let \(\Omega\) be a bounded simply connected planar domain, with no boundary regularity, such that the inclusion \(H^1(\Omega)\to L^2(\Omega)\) is compact and the first positive Neumann eigenvalue is simple. Assuming the smooth theorem, every nonzero eigenfunction \(u\) satisfies
\[
\sup_\Omega u=\lim_{\varepsilon\to0}\ \sup_{\operatorname{dist}(x,\partial\Omega)<\varepsilon}u(x),
\]
and likewise for the infimum [Bur26, Theorem 2.1]; if \(u\) extends continuously to \(\overline\Omega\), its maximum and minimum over \(\overline\Omega\) are attained on \(\partial\Omega\) [Bur26, Corollary 2.2]. The argument approximates \(\Omega\) by the images of concentric discs under a conformal map and proves convergence of the eigenvalues and eigenfunctions. That preprint reports that it was written with ChatGPT and that its author has not checked every detail; its argument is not reproduced or checked here.

Neither the strict conclusion nor the multiple-eigenvalue case is covered by that reduction. In higher dimensions the convex form of the conjecture fails in all sufficiently large dimensions [dDP24], and in the plane the simple connectivity assumption cannot be dropped [Bur05, Theorem 1.1].

## 4. Exercises

**4.1.** For \(q=0\) and \(p=0\), find an explicit map \(b\) in Lemma 1.1 with values in \(\mathbb R^2\).

**4.2.** Show that the kernel \(\Gamma\) in the proof of Lemma 1.1 satisfies \(\Gamma(s,s_0)=0\), so \(b(s_0)=0\).

**4.3.** In Step 4, suppose only \(w=0\) on the arc, not \(\partial_\nu w=0\). Compute the distribution \((\Delta+\mu)\tilde w\) on \(U\).

**4.4.** Show that the theorem gives, for \(0\ne u\in V\), that every level set \(\{u=c\}\) with \(\min_{\partial\Omega}u<c<\max_{\partial\Omega}u\) is, inside \(\Omega\), a one-dimensional smooth submanifold.

**4.5.** Show that a nonnegative Dirichlet eigenfunction for \(\lambda_D\) has an interior critical point. Which steps of the proof of the theorem use the Neumann condition?

## 5. Solutions

**4.1.** Here \(D_0(s,t)=\frac1{4\pi}|s-t|^2\) by Remark 2.2 of the previous lesson, so \(b(s)=s/(2\sqrt\pi)\in\mathbb R^2\) works (the construction of the proof gives \(b(s)-b(s_0)\) up to an isometry).

**4.2.** Since \(D_p(s_0,s_0)=0\), the definition gives \(\Gamma(s,s_0)=\frac12(D_p(s,s_0)-D_p(s,s_0))=0\), so \(\|b(s_0)\|^2=\Gamma(s_0,s_0)=0\).

**4.3.** The computation in Step 4 gives \(\int_U\tilde w(\Delta\phi+\mu\phi)=-\int_{\partial\Omega\cap U}\phi\,\partial_\nu w\,ds\), so \((\Delta+\mu)\tilde w\) is the measure \(-\partial_\nu w\,ds\) on the arc, which is not zero when \(\partial_\nu w\ne0\) there.

**4.4.** By the theorem \(\nabla u\ne0\) in \(\Omega\), so the implicit function theorem shows that \(\{u=c\}\cap\Omega\) is a smooth curve near each of its points.

**4.5.** Such a function \(\phi\) is continuous on \(\overline\Omega\), vanishes on \(\partial\Omega\) and is positive somewhere, so it attains its maximum in \(\Omega\), where \(\nabla\phi=0\). The Neumann condition makes the boundary gradient \(g\) tangent, which is needed to define \(E(bg)\) through tangent fields; and it gives \(E(g)=0\) through the equality case of Rohleder's principle, which is the starting point of the multiplier identity.

## References

- [OpenAI-HS] OpenAI, *Strict hot spots and absence of interior critical points on smooth simply connected planar domains*, OpenAI Math Release preprint, 24 September 2026, Lemma 6.1 and Section 6. https://github.com/openai/math/tree/main/preprints/Strict-hot-spots-and-absence-of-interior-critical-points-on-smooth-simply-connected-planar-domains-September-24-2026
- [Fil04] N. Filonov, *An inequality for eigenvalues of the Dirichlet and Neumann problems for the Laplace operator*, Algebra i Analiz 16 (2004), no. 2, 172–176 (in Russian; English translation in St. Petersburg Math. J. 16 (2005), 413–416). https://www.mathnet.ru/eng/aa604
- [Bur26] K. Burdzy, *Removing boundary smoothness from the hot-spots conclusion in the simple-eigenvalue case*, arXiv:2610.12622 (8 October 2026), Theorem 2.1, Corollary 2.2. https://arxiv.org/abs/2610.12622
- [Bur05] K. Burdzy, *The "hot spots" problem in planar domains with one hole*, arXiv:math/0405472, Theorem 1.1. https://arxiv.org/abs/math/0405472
- [dDP24] J. de Dios Pont, *Convex sets can have interior hot spots*, arXiv:2412.06344. https://arxiv.org/abs/2412.06344
