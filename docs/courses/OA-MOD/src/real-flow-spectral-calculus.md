# Spectral localization and products for real flows

Fourier filters isolate the frequencies of an orbit without requiring that the orbit be norm continuous. This lesson proves the real-action results used in the lacunary centralizer argument. The spaces and von Neumann algebras may be nonseparable.

## Predual continuity and normal Fourier filters

Let \(E\) be a complex Banach space, \(X=E^*\), and let \((\alpha_t)_{t\in\mathbb R}\) be a group of weak-star continuous linear maps on \(X\). Assume that every orbit is weak-star continuous and
\[
C=\sup_t\|\alpha_t\|<\infty.
\tag{RSF.1}
\]
Write \(\beta_t\eta=\eta\circ\alpha_t\) for the preadjoint. This lies in \(E\): a weak-star continuous linear functional is bounded by finitely many evaluation seminorms, hence factors through their finite-dimensional coordinate map and is a linear combination of those evaluations. Thus \(\|\beta_t\|\leq C\). Every \(\beta\)-orbit is weakly continuous, because its pairing with each \(x\in E^*\) is continuous by hypothesis. We first prove that it is norm continuous.

**Measurability and integration of a single orbit.** For fixed \(\eta\), let \(E_\eta\) be the norm-closed linear span of \(\{\beta_q\eta:q\in\mathbb Q\}\). This space is separable. It is weakly closed: a point outside a norm-closed subspace is separated by a bounded linear functional, by the Hahn–Banach and annihilator proofs in CP-01 and CP-05. Approximating a real parameter by rationals therefore puts its entire orbit in \(E_\eta\).

There is a countable norming family on \(E_\eta\). Choose a dense sequence in its unit sphere, choose a norm-one supporting functional at each vector by Hahn–Banach, and extend those functionals to \(E\). If \(v\) is a unit vector and a selected vector is within \(\varepsilon\) of it, the corresponding functional has absolute value at least \(1-\varepsilon\) on \(v\). Consequently the supremum of the absolute values of this family is exactly the norm. Distances from the orbit to a fixed vector of \(E_\eta\) are therefore suprema of countably many continuous scalar functions, hence measurable. The zero-space case needs no family.

Choose a countable dense set in \(E_\eta\). Assign each parameter to the first vector of that set within \(1/n\) of its orbit value. The resulting countably valued measurable function approximates the orbit uniformly within \(1/n\). On a bounded interval its values have norm at most \(C\|\eta\|+1\). Replacing all but finitely many of its disjoint measurable pieces by zero gives finite simple functions converging in integral norm: the omitted sets decrease to the empty set, so their measures tend to zero. Completeness of \(E\) now defines the integral of the orbit times a continuous compactly supported scalar function. Approximation in \(L^1\) extends this construction to every scalar \(a\in L^1(\mathbb R)\), with
\[
\begin{gathered}
\eta_a=\int a(t)\beta_t\eta\,dt,\\
\|\eta_a\|\leq C\|a\|_1\|\eta\|.
\end{gathered}
\tag{RSF.2}
\]
The simple-function construction also proves interchange with bounded linear maps and translations of the real variable. Scalar integration and its convergence statements are the ones proved in BI-02.

**Smoothing gives continuity and a dense span.** The group law gives
\[
\begin{aligned}
\|\beta_s\eta_a-\eta_a\|
&\leq C\|\eta\|\,
 \|a(\,\cdot-s)-a\|_1\\
&\longrightarrow0.
\end{aligned}
\tag{RSF.3}
\]
Here translation continuity is proved in BI-03. The span of all \(\eta_a\), for all \(\eta\in E\) and \(a\in C_c(\mathbb R)\), is norm dense in \(E\). Indeed, if \(x\in E^*\) annihilates that span, then the continuous scalar function \(t\mapsto x(\beta_t\eta)\) has integral zero against every continuous compact test function. It vanishes everywhere: a nonzero value, after a scalar rotation and restriction to a small interval, would have positive real part against a nonnegative bump. Its value at zero gives \(x(\eta)=0\). Hahn–Banach separation of a proper closed subspace proves the asserted density. Finally the norm-continuous vectors form a norm-closed subspace, since approximation of \(\eta\) by \(\zeta\) incurs the uniform error \((C+1)\|\eta-\zeta\|\). Thus every predual orbit is norm continuous.

We can now use the real-line Fourier algebra proved in UW-03:
\[
\begin{gathered}
A=\mathcal F L^1(\mathbb R),\qquad
\|\mathcal Fa\|_A=\|a\|_1,\\
(\mathcal Fa)(p)=\int a(t)e^{ipt}\,dt.
\end{gathered}
\tag{RSF.4}
\]
That proof establishes Fourier injectivity, completeness, the product law, smooth compact cutoffs, norm density of \(A_c=A\cap C_c(\mathbb R)\), local inversion in the actual \(A\) norm, and the compact-support ideal lemma. In particular, if \(J\) is a closed ideal and \(f\in A_c\) has support disjoint from its hull \(h(J)\), then \(f\in J\). This assertion does not require synthesis of an arbitrary closed set.

For \(f=\mathcal Fa\), take the adjoint of \(\eta\mapsto\eta_a\). This is the normal filter \(\alpha_f\); UW-03 proves
\[
\begin{gathered}
\alpha_fx=\int a(t)\alpha_t x\,dt,\qquad
\|\alpha_f\|\leq C\|f\|_A,\\
\alpha_f\alpha_g=\alpha_{fg},\qquad
\alpha_t\alpha_f=\alpha_f\alpha_t.
\end{gathered}
\tag{RSF.5}
\]
The displayed operator integral is weak-star. Every filtered vector has a norm-continuous orbit, because the difference of its translated kernels has \(L^1\) norm tending to zero, with the bound \(C\|x\|\) times that norm.

Fix \(\chi\in C_c^\infty(\mathbb R)\) with \(\chi(0)=1\), and put \(\chi_n(p)=\chi(p/n)\). Its inverse Fourier kernel is \(n k(nt)\), where \(k\) is Schwartz and \(\int k=1\). Predual norm continuity, followed by dominated convergence, gives
\[
\alpha_{\chi_n}x\longrightarrow x
\quad\text{weak-star}.
\tag{RSF.6}
\]
Indeed the predual error is at most \(\int|k(s)|\|\beta_{s/n}\eta-\eta\|\,ds\). No positivity of \(k\) is required. Compactly supported Fourier functions are norm dense in \(A\); the corresponding filtered vectors are asserted here to be weak-star dense in \(X\). RSF-04 explains why these two statements must be distinguished.

## Hull spectra, cutoffs and open localization

Define
\[
\begin{gathered}
I_\alpha(x)=\{f\in A:\alpha_fx=0\},\\
\operatorname{Sp}_\alpha(x)=h(I_\alpha(x)),\\
X^\alpha(D)=\{x:\operatorname{Sp}_\alpha(x)\subseteq D\}.
\end{gathered}
\tag{RSF.7}
\]
The filter bound and product law make \(I_\alpha(x)\) a closed ideal. The local ideal lemma, density of \(A_c\), and (RSF.6) show that an empty spectrum forces \(x=0\); the converse follows by taking a smooth cutoff nonzero at each specified real point. Moreover,
\[
\operatorname{Sp}_\alpha(\alpha_fx)
\subseteq\operatorname{Sp}_\alpha(x)
\cap\operatorname{supp}f.
\tag{RSF.8}
\]
For the first inclusion, every annihilator of \(x\) also annihilates \(\alpha_fx\). For the second, a smooth function supported off \(\operatorname{supp}f\) annihilates it and can be chosen nonzero at any prescribed point of that complement. These arguments also work for noncompact \(\operatorname{supp}f\).

**Closed-space criterion.** For closed \(D\subseteq\mathbb R\),
\[
\begin{aligned}
X^\alpha(D)=\bigcap\{\ker\alpha_g:
&\ g\in A_c,\\
&\ \operatorname{supp}g\cap D=\varnothing\}.
\end{aligned}
\tag{RSF.9}
\]
One inclusion follows from the compact-support ideal lemma applied to \(I_\alpha(x)\). For the other, each point outside \(D\) has a smooth compact cutoff supported outside \(D\) and nonzero at that point. If all such filters annihilate \(x\), that point is excluded from its hull. Since the filters are normal, (RSF.9) makes this space weak-star closed and linear. It is invariant under every \(\alpha_t\), by filter commutation. In fact \(I_\alpha(\alpha_tx)=I_\alpha(x)\), by applying the inverse \(\alpha_{-t}\).

**A compact cutoff fixes its vector.** If \(K=\operatorname{Sp}_\alpha(x)\) is compact and \(f\in A\) equals one on a neighborhood of \(K\), then
\[
\alpha_fx=x.
\tag{RSF.10}
\]
For each \(g\in A_c\), the function \((f-1)g=fg-g\) lies in \(A_c\), has support disjoint from \(K\), and hence annihilates \(x\). Thus \(\alpha_f\alpha_gx=\alpha_gx\). Use \(g=\chi_n\), then (RSF.6) and normality of \(\alpha_f\). This proof uses no unit in \(A\).

For open \(U\), define the open localization space
\[
X_0^\alpha(U)=
\overline{\operatorname{span}}^{\,w^*}
\{\alpha_fx:f\in A_c,\ \operatorname{supp}f\subset U,\ x\in X\}.
\tag{RSF.11}
\]
Using all \(f\in A\) with support in \(U\) gives the same space, because \(f\chi_n\to f\) in \(A\). If \(U\subseteq D\subseteq V\), with \(D\) closed and \(U,V\) open, then
\[
X_0^\alpha(U)\subseteq X^\alpha(D)
\subseteq X_0^\alpha(V).
\tag{RSF.12}
\]
The first inclusion follows from (RSF.8) and weak-star closedness. For the second, take \(x\in X^\alpha(D)\) and \(g\in A_c\). Choose \(c\in C_c^\infty(V)\) equal to one near the compact set \(D\cap\operatorname{supp}g\); if this set is empty use \(c=0\). The support of \((1-c)g\) misses \(D\): every point of \(D\cap\operatorname{supp}g\) has a neighborhood where it vanishes, and every remaining point of \(D\) is outside \(\operatorname{supp}g\). Equation (RSF.9) gives \(\alpha_gx=\alpha_{cg}x\in X_0^\alpha(V)\). Now take \(g=\chi_n\) and use (RSF.6).

The spectrum of the action itself can be defined as the hull of \(J_\alpha=\{f:\alpha_f=0\}\). It is exactly
\[
h(J_\alpha)=
\overline{\bigcup_{x\in X}\operatorname{Sp}_\alpha(x)}.
\tag{RSF.13}
\]
The inclusion from right to left follows from \(J_\alpha\subseteq I_\alpha(x)\). Outside the closure on the right choose a smooth compact \(g\), nonzero at the selected point, whose support avoids that closure. Equation (RSF.9) makes \(\alpha_gx=0\) for every \(x\), so \(g\in J_\alpha\) excludes the point from the left side. This proves the reverse inclusion.

## Adjoint reflection and the product theorem

Now let \(X=M\), a von Neumann algebra with its predual, and assume each \(\alpha_t\) is a normal star automorphism. The bound in (RSF.1) is one unless \(M=0\). The concrete predual construction CP-04–06 shows that left and right multiplication by a fixed element are normal: apply either operation to a summable vector-functional expansion and retain its summable norm bound. Involution is conjugate-linear weak-star continuous by the same expansion. These assertions hold on any Hilbert space.

For \(f=\mathcal Fa\), set \(f^\sharp(p)=\overline{f(-p)}\). Its inverse kernel is \(\overline a\), so taking adjoints in the weak-star integral proves
\[
\begin{gathered}
(\alpha_fx)^*=\alpha_{f^\sharp}(x^*),\\
\operatorname{Sp}_\alpha(x^*)
=-\operatorname{Sp}_\alpha(x).
\end{gathered}
\tag{RSF.14}
\]
Indeed \(f\in I_\alpha(x)\) if and only if \(f^\sharp\in I_\alpha(x^*)\); taking hulls gives the stated reflection, including zero elements.

We will prove the full product inclusion
\[
\operatorname{Sp}_\alpha(xy)
\subseteq
\overline{\operatorname{Sp}_\alpha(x)+
\operatorname{Sp}_\alpha(y)}.
\tag{RSF.15}
\]
The bar is retained for arbitrary closed, possibly unbounded spectra.

**Two-variable Fourier injectivity.** If \(K\in L^1(\mathbb R^2)\) has zero Fourier transform, then \(K=0\) almost everywhere. To see this using the one-variable injectivity proved in UW-03, fix rational \(q\). Scalar Fubini makes
\(u\mapsto\int K(u,v)e^{iqv}\,dv\) an \(L^1\) function with zero Fourier transform in \(u\), hence zero almost everywhere. Discard the union of these countably many null sets, and the null set where the section in \(v\) is not integrable. For each remaining \(u\), its section's transform vanishes at every rational \(q\). Continuity of that transform extends the equality to every real \(q\). One-variable injectivity in \(v\), and Fubini once more, prove the claim.

**Filtered products.** Let \(f=\mathcal Fa\), \(g=\mathcal Fb\) and \(h=\mathcal Fc\), with \(a,b,c\in L^1(\mathbb R)\). Define
\[
\begin{gathered}
K(u,v)=\int c(t)a(u-t)b(v-t)\,dt,\\
\|K\|_1\leq\|a\|_1\|b\|_1\|c\|_1.
\end{gathered}
\tag{RSF.16}
\]
Scalar Fubini and translation substitutions give
\[
(\mathcal F_2K)(p,q)=f(p)g(q)h(p+q).
\tag{RSF.17}
\]
All substitutions are justified by the product of the three \(L^1\) norms. Pairing a filtered product with \(\phi\in M_*\) gives, by separate normality of multiplication,
\[
\begin{aligned}
\phi\bigl(\alpha_h((\alpha_fx)(\alpha_gy))\bigr)
&=\int_{\mathbb R^2}K(u,v)\\
&\quad\cdot\phi(\alpha_u(x)\alpha_v(y))\,du\,dv.
\end{aligned}
\tag{RSF.18}
\]
For completeness, the untransformed triple integral has integrand
\(c(t)a(s)b(r)\phi(\alpha_{t+s}(x)\alpha_{t+r}(y))\). Its absolute value is bounded by \(\|\phi\|\|x\|\|y\||c(t)a(s)b(r)|\). Its coefficient is jointly continuous: write it as
\[
\phi(\alpha_u(x)\alpha_v(y))
=(\beta_u\phi)(x\alpha_{v-u}(y)).
\]
Norm continuity of \(\beta_u\phi\), the boundedness of the product, and weak-star continuity of the other orbit prove the assertion. Thus scalar Fubini applies; set \(u=t+s\), \(v=t+r\) to obtain (RSF.18). If \(\operatorname{supp}h\) misses \(\operatorname{supp}f+\operatorname{supp}g\), (RSF.17) is zero. Two-variable injectivity and (RSF.18) then prove
\[
\alpha_h((\alpha_fx)(\alpha_gy))=0.
\tag{RSF.19}
\]

**Passage to closed spectral spaces.** Let \(D,F\) be closed and let \(x\in M^\alpha(D)\), \(y\in M^\alpha(F)\). If either set is empty its vector is zero. Otherwise take \(h\in A_c\) with compact support \(K\) disjoint from \(\overline{D+F}\). The case \(h=0\) is immediate. For nonzero \(h\), the distance of \(K\) from that closed set is positive. Choose \(\varepsilon>0\) with twice that radius smaller than this distance, and put
\[
U=D+(-\varepsilon,\varepsilon),\qquad
V=F+(-\varepsilon,\varepsilon).
\]
Then \(K\cap(U+V)=\varnothing\). By (RSF.12), \(x\in M_0^\alpha(U)\) and \(y\in M_0^\alpha(V)\). Equation (RSF.19) annihilates the product of every pair of filtered generators for these two spaces, and therefore of every pair of their finite linear combinations. Fix one such first factor. Normality of left multiplication by it, followed by normality of \(\alpha_h\), allows the weak-star limit in the second factor. Now fix the resulting second factor \(y\); normality of right multiplication by \(y\) allows the weak-star limit in the first factor. Hence \(\alpha_h(xy)=0\). These are two separate limits; no joint weak-star continuity of multiplication is asserted. Applying (RSF.9) with the closed set \(\overline{D+F}\), and then taking the actual spectra for \(D,F\), proves (RSF.15).

## Narrow bands and two worked models

Let \(Y\subseteq X\) be a weak-star closed invariant linear subspace, and fix any \(\varepsilon>0\). Then
\[
Y=\overline{\operatorname{span}}^{\,w^*}
\bigcup_{a\in\mathbb R}
\bigl(Y\cap X^\alpha([a-\varepsilon,a+\varepsilon])\bigr).
\tag{RSF.20}
\]
Every filter preserves \(Y\): predual functionals annihilating \(Y\) annihilate its orbit integral. The weak-star annihilator characterization is the finite-coordinate separation argument of CP-10, or its general locally convex form NP2. For \(y\in Y\), approximate it by \(\alpha_{\chi_n}y\) using (RSF.6). Cover the compact support of \(\chi_n\) by finitely many open intervals of radius \(\varepsilon\). The finite smooth partition construction in BI-03 gives compactly supported \(q_j\) in those intervals whose sum is one near this support. Thus
\[
\alpha_{\chi_n}y=\sum_j\alpha_{\chi_n q_j}y.
\]
Each summand belongs to \(Y\) and has its spectrum in the corresponding closed interval by (RSF.8). This proves the nontrivial inclusion in (RSF.20); the other uses weak-star closedness of \(Y\).

**Matrix frequencies.** On \(M_n(\mathbb C)\), let \(D=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)\) with real entries and set \(\alpha_t(x)=e^{itD}xe^{-itD}\). For a matrix unit,
\[
\begin{gathered}
\alpha_t(e_{ij})=e^{it(\lambda_i-\lambda_j)}e_{ij},\\
\operatorname{Sp}_\alpha(e_{ij})=\{\lambda_i-\lambda_j\}.
\end{gathered}
\tag{RSF.21}
\]
Its filter is \(f(\lambda_i-\lambda_j)e_{ij}\). Smooth cutoffs separate every other point, proving the hull equality. Taking adjoints negates the frequency. If \(j=k\), multiplication of \(e_{ij}\) by \(e_{k\ell}\) adds the two frequencies and produces \(e_{i\ell}\); if \(j\ne k\) the product is zero and has empty spectrum. Thus the product formula is an inclusion and may be strict.

**Weak-star density need not be norm density.** Let \(X=\ell^\infty(\mathbb Z)=\ell^1(\mathbb Z)^*\) and
\[
(\alpha_tx)_n=e^{int}x_n.
\tag{RSF.22}
\]
This is a dual Banach-space action; it is not claimed to be an algebra automorphism action. The predual orbits are norm continuous by a finite-head, small-tail estimate in \(\ell^1\). Its filters satisfy \((\alpha_fx)_n=f(n)x_n\). Every \(f\in A\) vanishes at infinity, as proved in UW-03, so every filtered vector belongs to \(c_0(\mathbb Z)\). Smooth compact cutoffs around individual integers give every finitely supported vector. Their norm closure is exactly \(c_0\), since a uniform limit of sequences vanishing at infinity still vanishes at infinity, while finite truncations converge uniformly to every member of \(c_0\). This closure is proper: it omits the constant sequence one. Those same finite truncations converge weak-star to every bounded sequence, by the \(\ell^1\) tail estimate. Thus the weak-star density in (RSF.6) and (RSF.20) cannot be strengthened to norm density in general.

The Fourier-algebra proofs used here are UW-03, built from BI-02–03. The general programme treatment of spectral localization and spectral sums is in OA-FLOW, lessons 17, 78, 80 and 84. The real-line arguments above supply the exact dual-space and automorphism-flow statements needed for the lacunary centralizer theorem WC-06.
