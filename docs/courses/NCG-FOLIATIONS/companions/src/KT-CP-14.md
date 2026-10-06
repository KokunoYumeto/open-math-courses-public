# Groupoid C*-algebras: full and reduced

*Written by GPT-6.1 Sol (OpenAI), October 2026. Public domain (CC0).*

The Haar system integrates composable arrows. The reduced norm then measures the resulting operators on individual source fibres; the full norm allows all continuous representations. Their comparison is the groupoid counterpart of the crossed-product comparison in Lessons 1–4. We construct the measurable disintegration of dense-domain representations, then prove the amenable norm equality by Haar smoothing and compression into amplified regular representations, and construct the cutoff that applies it to proper Hausdorff groupoids. A finite-quotient group bundle supplies explicit counterexamples to the converse and to reduced restriction exactness.

Throughout, \(\mathcal G\rightrightarrows X\) is second countable and locally compact, its arrow space is locally Hausdorff, its unit space is Hausdorff, and it has a full-support left Haar system \(\lambda^x\) on \(\mathcal G^x\). Fibres are Hausdorff. In the Hausdorff case \(C_c(\mathcal G)\) has its usual meaning; otherwise it is the patch span of Lesson 13. Functions in that span vanish outside a compact set, although their support closure in the whole arrow space need not be compact. We explicitly require Hausdorff arrows for the conditional expectation onto \(C_0(X)\).

## Integrating compositions

Scalar and Hilbert-module inner products are conjugate-linear in the first entry and linear in the second.

Put \(\lambda_x=\mathrm{inv}_*\lambda^x\), a measure on \(\mathcal G_x\). Left invariance becomes right invariance for this family. Our operations and norm are
\[
 \begin{gathered}
 (f*g)(\gamma)=\int_{\mathcal G^{r(\gamma)}}
                    f(\eta)g(\eta^{-1}\gamma)\,d\lambda^{r(\gamma)}(\eta),\\
 f^*(\gamma)=\overline{f(\gamma^{-1})},\\
 R(f)=\sup_x\int |f|\,d\lambda^x,\qquad
 S(f)=\sup_x\int |f|\,d\lambda_x,\\
 \|f\|_I=\max\{R(f),S(f)\}.
 \end{gathered}
 \tag{14.1}
\]
There is no modular factor in this involution. A modular factor reappears when we identify these kernels with group crossed-product kernels.

All these integrals are finite and uniformly bounded. For a Hausdorff compact support choose a nonnegative compact bump dominating \(|f|\). For a patch sum use the sum of the absolute values of its individual patch terms; this is a positive patch function dominating \(|f|\). Haar continuity bounds its fibre integrals. Applying inversion gives the source bound. The modulus of the entire patch sum need not itself belong to the patch space.

We use a compact integration observation. If \(Y\) is locally compact Hausdorff, \(p:Y\to X\) is continuous, \(U\) is a Hausdorff arrow patch, and
\(F\in C_c(Y\times_{p,r}U)\), then
\[
 y\longmapsto\int_{\mathcal G^{p(y)}} F(y,\eta)\,d\lambda^{p(y)}(\eta)
 \tag{14.2}
\]
is continuous, interpreting \(F\) as zero off the patch. To prove it, extend the compactly supported function from the closed fibre product to a compactly supported function on \(Y\times U\). Compact-support extension is the ordinary Hausdorff extension theorem, with cutoffs. Finite sums \(a(y)b(\eta)\) approximate that extension uniformly, with their supports in one compact rectangle, by the Stone–Weierstrass theorem. The integral of a product is \(a(y)\lambda(b)(p(y))\), which is continuous. A nonnegative patch bump equal to one on the fixed arrow-coordinate compact set bounds the integration error by its uniform fibre integral times the uniform approximation error. This proves (14.2).

**Theorem 14.1.** The operations (14.1) make \(C_c(\mathcal G)\) a normed *-algebra, with
\[
 \|f*g\|_I\leq\|f\|_I\|g\|_I,\qquad \|f^*\|_I=\|f\|_I.
 \tag{14.3}
\]

**Proof.** First assume the arrow space is Hausdorff. The convolution integrand is continuous on \(\{(\gamma,\eta):r(\gamma)=r(\eta)\}\). It vanishes outside a compact subset: the pairs which matter come from the compact composable part of \(\operatorname{supp}f\times\operatorname{supp}g\), through \((\eta,\zeta)\mapsto(\eta\zeta,\eta)\). Observation (14.2), with finitely many patches if needed, proves continuity. Its support is contained in the compact product of the two supports.

Here is the additional argument for patch kernels. Multiplication is an open map. Indeed \((\eta,\zeta)\mapsto(\eta\zeta,\zeta)\) identifies its domain with \(\{(\alpha,\zeta):s(\alpha)=s(\zeta)\}\); projection onto \(\alpha\) is open because it is the base change of the open map \(s\). Explicitly the image of a product of two open sets is the first open set intersected with the inverse image of the second set's open source image.

Let \(f\) be one patch term on a Hausdorff open \(U\). Choose an open \(U_0\) and a compact \(K\subset U\) with \(\operatorname{supp}_U f\subset U_0\subset K\). Near any point \(\zeta\) of the support of a patch term \(g\), choose a compact Hausdorff neighborhood \(L\) inside its patch, sufficiently small that
\[
 KLL^{-1}\subset U,
 \tag{14.4}
\]
where only composable products are included. Such a choice exists: otherwise shrinking neighborhoods of \(\zeta\) give composable triples \(k_j,l_j,l'_j\), with \(k_j\) in the compact Hausdorff \(K\) and \(l_j,l'_j\to\zeta\), whose products stay outside \(U\). A convergent subnet of the \(k_j\) makes these products converge to a point of \(K\subset U\), a contradiction.

Choose an open \(W\) about \(\zeta\) inside \(L\). The open product \(U_0W\) is Hausdorff. If a net of its arrows, written \(\eta_j\zeta_j\), converges to two points \(\alpha,\beta\) in this product, compactness of \(L\) permits a subnet with \(\zeta_j\to\zeta'\in L\). Then \(\eta_j\) converges to both \(\alpha(\zeta')^{-1}\) and \(\beta(\zeta')^{-1}\). Both belong to \(KLL^{-1}\subset U\), by writing \(\alpha,\beta\) as products in \(U_0W\). Hausdorffness of \(U\) makes them equal, hence \(\alpha=\beta\). Endpoints match in these limit products because \(X\) is Hausdorff.

A finite partition of \(g\) within its Hausdorff patch now puts each term in one such \(W\). Its convolution with \(f\) is a continuous compactly supported function on the Hausdorff patch \(U_0W\), by (14.2), and is zero elsewhere. Thus convolution preserves the patch span. Inversion sends a Hausdorff open patch homeomorphically to another, so the involution also preserves it.

For associativity, both bracketings reduce, using Fubini and left invariance, to
\[
 \int_{\mathcal G^{r(\gamma)}}\!
 \int_{\mathcal G^{s(\xi)}}\!
 f(\xi)g(\zeta)h(\zeta^{-1}\xi^{-1}\gamma)
 \,d\lambda^{s(\xi)}(\zeta)\,d\lambda^{r(\gamma)}(\xi).
 \tag{14.5}
\]
The substitution in the other bracketing is \(\eta=\xi\zeta\). Compact positive patch envelopes justify absolute integrability and Fubini. For the involution identity, substitute \(\eta=\gamma\theta\) in \((g^**f^*)(\gamma)\); its integrand becomes
\(\overline{g(\theta^{-1}\gamma^{-1})}\,\overline{f(\theta)}\) integrated against \(\lambda^{s(\gamma)}\), exactly \((f*g)^*(\gamma)\).

Finally integrate the absolute convolution on a range fibre and substitute \(\gamma=\eta\zeta\). The inner \(g\)-integral is at most \(R(g)\), giving \(R(f*g)\leq R(f)R(g)\). Apply this to \(g^**f^*\) to get \(S(f*g)\leq S(g)S(f)\). Inversion exchanges \(R,S\), proving (14.3). Full support, and continuity of the restriction of a patch function to each Hausdorff fibre, imply that \(\|f\|_I=0\) only for \(f=0\). ∎

## Source-fibre representations

On \(H_x=L^2(\mathcal G_x,\lambda_x)\) define
\[
 \begin{aligned}
 (L_x(f)\xi)(\gamma)
 &=\int_{\mathcal G_x} f(\gamma\zeta^{-1})\xi(\zeta)\,d\lambda_x(\zeta)\\
 &=\int_{\mathcal G^{r(\gamma)}}f(\eta)\xi(\eta^{-1}\gamma)
                                      \,d\lambda^{r(\gamma)}(\eta).
 \end{aligned}
 \tag{14.6}
\]
The equality follows by inversion and left multiplication; it does not insert a modular function.

**Proposition 14.2.** These are *-representations, and
\[
 \|L_x(f)\|\leq \sqrt{R(f)S(f)}\leq\|f\|_I.
 \tag{14.7}
\]

**Proof.** The integral kernel is \(K(\gamma,\zeta)=f(\gamma\zeta^{-1})\). Its absolute row integrals are at most \(R(f)\). For a column, right translation \(\gamma\mapsto\gamma\zeta^{-1}\) carries \(\lambda_x\) to \(\lambda_{r(\zeta)}\), so its absolute integral is at most \(S(f)\). Cauchy–Schwarz with the weight \(|K|\), followed by integration in \(\gamma\), gives
\[
 \begin{aligned}
 |L_x(f)\xi(\gamma)|^2
 &\leq R(f)\int |K(\gamma,\zeta)|\,|\xi(\zeta)|^2\,d\lambda_x(\zeta),\\
 \|L_x(f)\xi\|_2^2&\leq R(f)S(f)\|\xi\|_2^2.
 \end{aligned}
 \tag{14.8}
\]
The transposed conjugate kernel is \(f^*(\gamma\zeta^{-1})\), proving the adjoint identity. Kernel composition, with the substitution used in (14.6), is convolution. Positive envelopes justify these calculations first on compactly supported vectors and then on all \(H_x\). ∎

The family detects every nonzero test function. If \(f(\gamma)\ne0\), put \(x=s(\gamma)\), and choose a nonnegative source-fibre bump near \(e(x)\), small enough that \(f(\gamma\zeta^{-1})\) stays in an open complex half-plane after multiplication by one fixed phase. Full support makes its integral against that bump nonzero. The bump can be obtained by restricting a compact Hausdorff-patch function on \(\mathcal G\). Its convolution with \(f\), restricted to \(\mathcal G_x\), is continuous, so the nonzero value persists on a relatively open set of positive measure. Thus \(L_x(f)\ne0\).

Consequently
\[
 \|f\|_r=\sup_{x\in X}\|L_x(f)\|
 \tag{14.9}
\]
is a C*-norm. Its completion is \(C_r^*(\mathcal G)\). The definition uses all units, rather than a chosen invariant measure.

When \(\mathcal G\) is Hausdorff there is also a Hilbert \(C_0(X)\)-module description:
\[
 \langle\xi,\eta\rangle(x)=\int_{\mathcal G_x}\overline{\xi(\gamma)}
                       \eta(\gamma)\,d\lambda_x(\gamma),\qquad
 (\xi b)(\gamma)=\xi(\gamma)b(s(\gamma)).
 \tag{14.10}
\]
Haar continuity after inversion makes the inner product belong to \(C_0(X)\). Completion gives \(E\); convolution is adjointable by (14.7) and the adjoint calculation. Its norm is (14.9). For the reverse of the immediate upper bound, extend a compact source-fibre vector to a compactly supported function on \(\mathcal G\), then multiply by a unit-space cutoff equal to one at that fibre. Continuity of its inner-product norm lets the cutoff make the module norm arbitrarily close to the fibre norm. Such vectors are dense in \(H_x\), proving the reverse bound. This description will help with equivalence in Lesson 15. For non-Hausdorff arrows, pointwise products of patch functions can fail to be patch functions, and (14.10) cannot be assumed to give a \(C_0(X)\)-valued inner product.

## The full norm and disintegration

Let \(\mathcal R_I\) be the *-representations satisfying
\(\|\pi(h)\|\leq\|h\|_I\) for every test function \(h\). Define
\[
 \|f\|_{\max}=\sup_{\pi\in\mathcal R_I}\|\pi(f)\|.
 \tag{14.11}
\]
It satisfies the C*-identity, is finite, and is a norm because it dominates (14.9). Its completion is \(C^*(\mathcal G)\). There is a canonical surjection
\[
 C^*(\mathcal G)\longrightarrow C_r^*(\mathcal G).
 \tag{14.12}
\]
Surjectivity follows because its image is closed and contains the dense test-function algebra.

We now prove Renault's disintegration theorem, with the precise dense-domain hypotheses of [Muhly–Williams 2008, Theorem 7.8, pp. 45–46]. A multiplicative representation on a dense domain in a Hilbert space, with dense essential range, continuous matrix coefficients for uniform convergence on a fixed compact set, and the adjoint identity there, extends to an \(I\)-contractive representation. It is the integrated form of a measurable unitary representation of the groupoid on a Hilbert bundle over \(X\), with a quasi-invariant measure. We use separable Hilbert spaces in this statement. General C*-representations reduce to separable cyclic representations because the present second countable test-function completion is separable; they need not decompose into irreducibles.

More explicitly let \(\mu\) be the unit-space measure, \(\nu=\int\lambda^x\,d\mu(x)\), and \(D=d\nu/d\nu^{-1}\). Quasi-invariance means these two arrow measures are equivalent. The integrated form has weak integral kernel
\[
 (\pi(f)\xi)(x)=\int_{\mathcal G^x}
       f(\gamma)V_\gamma\xi(s(\gamma))D(\gamma)^{-1/2}\,d\lambda^x(\gamma).
 \tag{14.13}
\]
Here \(V_\gamma:H_{s(\gamma)}\to H_{r(\gamma)}\) is unitary and respects products. This measured \(D\) is separate from the group modular function in the next section. The theorem and its integrated-form bound identify (14.11) with the usual universal continuous groupoid norm. The construction below proves both conclusions, including the measurable foundations; [ibid., Proposition 7.6, p. 45] is also the historical locator for the integrated bound.

We will also need the unit-space multipliers. For every nondegenerate full representation \(\pi\) there is a nondegenerate representation \(M:C_0(X)\to B(H)\) satisfying
\[
 M(b)\pi(f)=\pi((b\circ r)f),\qquad
 \pi(f)M(b)=\pi(f(b\circ s)).
 \tag{14.14}
\]
Here is a direct proof of the required bound. For a bounded continuous \(b\), set \(c=\|b\|_\infty\) and \(h=(c^2-|b|^2)^{1/2}\). Endpoint multiplication preserves every patch term. The convolution identities give
\[
 ((b\circ r)f_i)^**((b\circ r)f_j)
 +((h\circ r)f_i)^**((h\circ r)f_j)=c^2 f_i^**f_j.
 \tag{14.15}
\]
Applying \(\pi\) and summing matrix coefficients for any finite family of vectors proves that the rule in (14.14), on their dense span \(\sum\pi(f_i)\xi_i\), is well-defined and bounded by \(c\). The product and adjoint rules follow there. Cutoffs in \(C_c(X)\) equal to one on the finitely many compact range images show nondegeneracy; taking adjoints gives the second formula. In (14.13), \(M(b)\) is multiplication by \(b(x)\).

### Local units for the convolution algebra

We prove the disintegration statement before using it. Write \(\mathscr C\) for the patch test-function algebra and \(H_{00}=\operatorname{span}L(\mathscr C)H_0\). Its dense-domain hypotheses are essential range density, multiplicativity, the adjoint identity, and continuity of each matrix coefficient on every fixed compact patch. No bound on \(L(f)\) is assumed. The square identity (14.15) still applies to these operators on \(H_0\); its right-hand side is a squared Hilbert norm. It therefore constructs the same bounded, nondegenerate unit representation \(M\) on \(H\), before any arrow operator has been shown bounded.

We first need a left approximate identity in the patch inductive-limit topology. For a compact \(K\subset X\) and an open neighborhood \(W\) of the units, choose finitely many nonnegative patch bumps supported in \(W\), positive at units covering \(K\). Their sum \(b\) has \(\lambda(b)>0\) on a neighborhood of \(K\): Haar full support gives positivity, and Haar continuity gives the neighborhood. Choose \(0\leq\chi\in C_c(X)\), equal to one on \(K\), with support in that neighborhood. Define, with zero where the denominator vanishes,
\[
 e(\gamma)=\frac{b(\gamma)\chi(r(\gamma))}{\lambda(b)(r(\gamma))}.
 \qquad \lambda(e)=\chi,\quad
 \sup_x\lambda^x(e)\leq1.
 \tag{14E.1}
\]
This is a nonnegative patch function supported in \(W\).

Here are the compactness details that make shrinking \(W\) useful even with non-Hausdorff arrows. There are arbitrarily small neighborhoods \(N\) of the units such that \(N\cap r^{-1}(K)\) and \(N\cap s^{-1}(K)\) are compact for every compact unit set \(K\). To construct one inside a prescribed neighborhood, take a locally finite cover of \(X\) by compact sets \(K_i\) whose interiors cover \(X\). Choose compact neighborhoods \(N_i'\) of \(K_i\) inside the prescribed arrow neighborhood, using finitely many compact Hausdorff neighborhoods. Put
\(N_i=N_i'\cap r^{-1}(K_i)\cap s^{-1}(K_i)\), and take their union. Over a compact unit set only finitely many pieces occur; their relevant intersections are closed in compact sets. This proves the assertion. Consequently \(N\cdot C\) is compact for compact arrow sets \(C\).

For a compact \(C\) inside an open set \(V\), a sufficiently small unit neighborhood satisfies \(N\cdot C\subset V\). To see this, for each unit \(u\in r(C)\) there is an arrow neighborhood \(U_u\) with \(U_u\cdot C\subset V\). Otherwise arrows approaching \(u\) would act on points of \(C\) to give points outside \(V\); a convergent subnet of those points of \(C\) and continuity of the action would force their products to approach a point of \(C\subset V\), a contradiction. Take the union of finitely many such neighborhoods covering the compact unit image, and include \(s^{-1}(X\setminus r(C))\). The latter arrows cannot act on \(C\). This gives a neighborhood of all units, which may then be shrunk to one of the compact neighborhoods just constructed.

Over a compact unit set \(K\) we can also arrange that this neighborhood is Hausdorff. For each \(x\in K\), take a Hausdorff arrow neighborhood \(V_x\) and a closed unit neighborhood \(C_x\subset V_x\). Intersect finitely many sets
\(V_x\cup r^{-1}(X\setminus C_x)\) with the \(C_x\)'s covering \(K\). Two arrows in the result with different ranges separate in \(X\); with the same range they lie in one of the Hausdorff \(V_x\)'s.

Now let \(f\in C_c(V)\), with compact patch support \(C\). Fix a compact neighborhood \(N\) as above with \(N\cdot C\subset V\); shrink further so that \(N\) over the compact range image of \(N\cdot C\) is Hausdorff. Uniformly for composable \((\eta,\gamma)\), as \(\eta\) approaches the units within these neighborhoods,
\[
 |f(\eta^{-1}\gamma)-f(\gamma)|\longrightarrow0.
 \tag{14E.2}
\]
Only \(\gamma\in N\cdot C\) can contribute. If uniform convergence failed, compactness would give convergent subnets of these \(\gamma\)'s and of \(\eta\)'s. In the Hausdorff restricted neighborhood the latter limit is a unit: any proposed nonunit can be excluded by a smaller compact unit neighborhood, since singletons are closed. Its restriction to the fixed compact range set is compact and therefore closed in the Hausdorff restricted neighborhood; eventual membership forces the limit into it, a contradiction. Multiplication then gives \(\eta^{-1}\gamma\to\gamma\) inside \(V\), contradicting continuity of \(f\). Choosing the compact unit set in (14E.1) to contain \(r(N\cdot C)\), the row-mass bound and (14E.2) give \(e*f\to f\) uniformly, with support in the fixed compact set \(N\cdot C\subset V\). The same argument term by term proves left approximation for every patch sum.

If \(a=\sum L(f_i)\xi_i\in H_{00}\), this approximation gives \(L(e)a\to a\) in Hilbert norm. Expand the square of the difference; every term is a matrix coefficient of either \((e*f_i-f_i)^**(e*f_j-f_j)\) or an equivalent expanded convolution. Convolution is continuous for the fixed patch supports proved above, so coefficient continuity sends every term to zero. In particular, if \(\{\zeta_j\}\subset H_{00}\) is an orthonormal basis of \(H\), then
\[
 \operatorname{span}\{L(f)\zeta_j:f\in\mathscr C,\ j\geq1\}
                  \text{ is dense in }H.
 \tag{14E.3}
\]
Such a basis exists by Gram–Schmidt on a countable dense subset of \(H_{00}\). Notice that this argument does not assume continuity of the possibly unbounded \(L(f)\) in its vector variable.

### Obtaining the measure on the units

For clarity we construct the multiplication representation of \(M\), rather than assuming a direct-integral decomposition. Let \(\{v_n\}\) be an orthonormal basis of \(H\). The positive functionals \(a\mapsto\langle v_n,M(a)v_n\rangle\) have finite Radon measures \(\mu_n\) on \(X\). Put \(\mu=\sum 2^{-n}\mu_n\). The complex matrix measures \(\mu_{ij}(a)=\langle v_i,M(a)v_j\rangle\) are absolutely continuous with respect to \(\mu\), by Cauchy–Schwarz for the spectral measures. One may obtain these spectral measures directly by extending the positive vector functionals from continuous functions to Borel functions using their Radon measures; polarization and multiplicativity on continuous functions give the projection rule, first on open sets by increasing continuous cutoffs and then on Borel sets by the monotone-class theorem.

Let \(h_{ij}=d\mu_{ij}/d\mu\). Off one null set, the matrices \((h_{ij}(x))\) are positive semidefinite: test finite vectors with rational complex coefficients and nonnegative continuous unit cutoffs, then use density of those coefficients. At each such \(x\), complete the formal span of symbols \(v_i(x)\) with Gram matrix \(h_{ij}(x)\), after quotienting the null vectors. Take zero fibres on the exceptional set. Measurable Gram–Schmidt makes this a Borel field: discard zero-length residuals, divide the remaining residuals by their Borel norms, and use their coordinates to identify each fibre with a coordinate subspace of \(\ell^2\). This also proves completeness of its \(L^2\)-space by ordinary coordinatewise \(L^2\) completeness.

The map
\[
 \sum_i M(a_i)v_i\longmapsto \left(x\mapsto\sum_i a_i(x)v_i(x)\right)
 \tag{14E.4}
\]
is isometric, because both inner products are \(\sum_{ij}\int\overline{a_i}a_jh_{ij}\,d\mu\). Its domain is dense by nondegeneracy of \(M\). Its image is dense as well: the \(v_i(x)\)'s are total in every fibre, and continuous scalar functions are dense in \(L^2(\|v_i(x)\|^2\mu)\), a finite Radon measure. Thus (14E.4) extends to a unitary onto this \(L^2\)-space. In this realization \(M(k)\) is multiplication by any bounded Borel \(k\). In particular it is zero when \(k=0\) almost everywhere for \(\mu\). If \(H=0\), take \(\mu=0\) and zero fibres; the rest of the theorem is immediate. Henceforth assume \(H\ne0\).

### Enlarging the test functions without assuming bounded operators

We need Borel indicators, but we cannot insert them into \(L\) without a construction. Let \(\mathscr B\) be the finite span of bounded Borel functions supported in compact subsets of Hausdorff patches. Each coefficient
\(\ell_{\xi,\eta}(f)=\langle\xi,L(f)\eta\rangle\), for \(\xi,\eta\in H_0\), is a complex Radon functional on each patch. Its measures agree on overlaps, since they agree on continuous functions there. A disjoint Borel partition of a countable patch cover glues them. Their total variations are finite on compact patch sets, so their integrals extend \(\ell_{\xi,\eta}\) to \(\mathscr B\).

Convolution and involution preserve \(\mathscr B\). Measurability follows from the Borel Haar kernel described below; the row-mass bounds of positive compact patch envelopes bound convolution uniformly. The product of the compact envelopes is compact and has a finite cover by precompact Hausdorff patches; partitioning it into Borel pieces puts the result back in \(\mathscr B\). If bounded sequences converge pointwise with fixed compact patch envelopes, their convolutions converge pointwise by dominated convergence, with uniform bounds and fixed compact envelopes. The same is true after integrating against any of the coefficient total variations.

On \(\mathscr B\odot H_0\) define
\[
 \langle f\otimes\xi,g\otimes\eta\rangle
       =\ell_{\xi,\eta}(f^**g).
 \tag{14E.5}
\]
This form is positive and its quotient embeds in the original \(H\); we give the limiting argument because positivity for Borel functions is not automatic. On \(\mathscr C\odot H_0\) it is precisely
\(\langle L(f)\xi,L(g)\eta\rangle\), hence its completion is \(H\). Every bounded Borel function with compact patch envelope belongs to the closure of the continuous patch functions under bounded pointwise sequential limits. Indeed on a Hausdorff patch, continuous cutoff exhaustion generates indicators of relatively compact open sets; the bounded monotone-class theorem generates all Borel indicators and then bounded Borel functions. Keep a larger compact cutoff envelope throughout. If desired, this closure can be organized by countable ordinal stages: take bounded sequential limits of earlier stages, and take their union over the countable ordinals. Each Borel function enters some stage, since the Borel sigma-algebra is generated by the countable open basis using countable operations.

At a new stage \(f_n\to f\), the vectors \([f_n\otimes\xi]\) are Cauchy: their squared difference is
\(\ell_{\xi,\xi}((f_n-f_m)^**(f_n-f_m))\), which tends to zero as \(n,m\to\infty\) by the two dominated-convergence statements above. Their limit in \(H\) has the inner products prescribed by (14E.5). Apply this simultaneously to any finite family to preserve positivity, and to two possible approximations to prove independence. Induction through the stages proves the claim for all of \(\mathscr B\). This argument allows arbitrary Borel null sets; it does not assume that a general \(G_\delta\) indicator is a pointwise limit of continuous functions.

Write \(E=\operatorname{span}\{[g\otimes\xi]:g\in\mathscr B,\xi\in H_0\}\subset H\). For \(f\in\mathscr C\), the densely defined operator \(L(f)|_{H_{00}}\) is closable. To check this directly, if \(a_n\to0\) and \(L(f)a_n\to b\), the adjoint identity against every \(c\in H_{00}\) gives \(\langle c,b\rangle=0\), hence \(b=0\). The same limiting induction therefore puts \([g\otimes\xi]\) in its closed domain with image \([f*g\otimes\xi]\). At subsequent stages in the first variable it also proves the implication
\[
 \sum_i[g_i\otimes\xi_i]=0\quad\Longrightarrow\quad
                    \sum_i[f*g_i\otimes\xi_i]=0.
 \tag{14E.6}
\]
For continuous \(f\) use the closed operator just constructed; for a bounded pointwise limit in \(f\), pass to the Hilbert-norm limit of the convolution vectors. Thus
\(L_b(f)[g\otimes\xi]=[f*g\otimes\xi]\) defines an operator on \(E\) for every \(f\in\mathscr B\).

The unit multipliers extend with the expected formula:
\[
 \begin{gathered}
 M(k)[g\otimes\xi]=[(k\circ r)g\otimes\xi],\\
 M(k)L_b(f)=L_b((k\circ r)f)\quad\text{on }E.
 \end{gathered}
 \tag{14E.7}
\]
Prove the first identity for continuous \(k\) using (14.14), and pass through bounded Borel limits. The left side converges strongly in the multiplication realization, while the right side converges by (14E.5). Repeat for Borel \(g\); a cutoff on its compact range image handles a \(k\) without compact support. The second identity follows from the first and \((k\circ r)(f*g)=((k\circ r)f)*g\). The same limiting argument gives, for \(a=[g\otimes\xi]\), \(b=[h\otimes\eta]\) with continuous \(g,h\),
\(\langle a,L_b(f)b\rangle=\ell_{\xi,\eta}(g^**f*h)\). These identities will supply precisely the null-set tests we need.

### Why the unit measure is quasi-invariant

Put \(\nu=\mu\lambda\). On each Hausdorff patch this is a Radon measure: continuity of the Haar kernel gives finiteness on compact envelopes and the usual positive Radon functional. We show \(\nu(A^{-1})=0\) whenever \(\nu(A)=0\). It suffices to treat compact \(A\) in a Hausdorff patch. Indeed the inverse measure is also Radon on every patch; its inner regularity, and a countable patch cover, then give the assertion for every Borel null set.

Let \(b=1_A\). For \(k_1,k_2\in\mathscr C\), the Borel function
\(a(x)=\lambda^x(\overline{k_1}k_2b)\) is zero \(\mu\)-almost everywhere, so \(M(a)=0\). Formula (14E.7) yields, for every \(g_1,g_2\in\mathscr C\) and \(\xi\in H_0\),
\[
 \ell_{\xi,\xi}\big(g_1^**((a\circ r)g_2)\big)=0.
 \tag{14E.8}
\]
To reverse \(A\), introduce the same-range space
\(Y=\{(\alpha,\beta):r(\alpha)=r(\beta)\}\). For compact patch functions \(F_1,F_2\) on \(Y\), set
\[
 K_b(F_1,F_2)(\sigma)=
 \int\!\int \overline{F_1(\alpha,\beta)}
 F_2(\sigma^{-1}\alpha,\sigma^{-1}\beta)
 b(\alpha^{-1}\beta)\,d\lambda^{r(\sigma)}(\alpha)
                         d\lambda^{r(\sigma)}(\beta).
 \tag{14E.9}
\]
This is a bounded Borel function with compact patch envelopes. The bounds follow from the product of the two fibre masses of compact positive envelopes; its possible \(\sigma\)'s lie in a compact difference set of the projections of the supports. For continuous \(b\), product approximation on compact Hausdorff patches gives the usual continuous patch integration lemma. Bounded pointwise limits in \(b\) give the stated Borel version and justify all subsequent integrals.

For \(F_i(\alpha,\beta)=k_i(\alpha^{-1}\beta)g_i(\alpha^{-1})\), left invariance changes the second integral in (14E.9) into
\(K_b(F_1,F_2)=g_1^**((\lambda(\overline{k_1}k_2b)\circ r)g_2)\).
Thus its coefficient is zero by (14E.8), including mixed pairs, not just equal pairs. Such \(F_i\)'s span a dense subspace in the patch inductive-limit topology. To prove this, use the homeomorphism
\((\alpha,\beta)\mapsto(\alpha^{-1},\alpha^{-1}\beta)\) onto the composable-pair space; products of the two coordinates separate points on a compact Hausdorff patch. Extend its compactly supported function to a compact rectangle and approximate by finite products, using ordinary Stone–Weierstrass and cutoffs. Refine to the finitely many Hausdorff patches when required. The fixed-support bounds in (14E.9), followed by coefficient total-variation integration, extend the zero identity to every \(F_1,F_2\).

Interchanging \(\alpha,\beta\) in (14E.9) replaces \(b(\alpha^{-1}\beta)\) by \(b((\alpha^{-1}\beta)^{-1})\). Hence the zero identity holds with \(b^\vee(\gamma)=b(\gamma^{-1})\). Reversing the earlier calculation, for every \(k,g,\xi\),
\(\langle L(g)\xi,M(\lambda(|k|^2b^\vee))L(g)\xi\rangle=0\).
The multiplier is positive. Its square root annihilates the dense essential span, so it is zero. In the multiplication realization this says \(\lambda(|k|^2b^\vee)=0\) \(\mu\)-almost everywhere. Countably many nonnegative patch bumps with positive sets covering \(\mathcal G\) now give \(b^\vee=0\) \(\nu\)-almost everywhere. This proves \(\nu(A^{-1})=0\). Applying inversion twice gives equivalence of \(\nu\) and \(\nu^{-1}\), as required.

### A modular derivative that respects every product

Let \(\mu\) be a finite positive measure on the units and suppose
\(\nu=\mu\lambda\) is equivalent to its inverse measure \(\nu^{-1}\). The Radon–Nikodym theorem initially gives only a positive finite Borel function \(D=d\nu/d\nu^{-1}\), defined almost everywhere. We prove that its representative can be chosen multiplicative on every composable pair. This matters when constructing an actual groupoid representation, rather than identities with separate exceptional sets.

All spaces here have standard Borel structures, including locally Hausdorff arrows. Indeed partition a countable Hausdorff open cover into disjoint Borel pieces; each piece is a Borel subset of a second countable locally compact Hausdorff space. Its countable disjoint union is standard Borel, and its Borel sets are exactly the original Borel sets. The Haar measures form a Borel kernel: this follows first for compact bumps in each chart by Haar continuity, then for indicators of open sets by countable bump exhaustion, and then for Borel sets by the monotone-class theorem.

Choose a strictly positive Borel function \(q\) with \(q\lambda^x\) a probability for every unit. One explicit choice starts with countably many nonnegative patch bumps \(b_j\leq1\) whose positive sets cover the arrows, and puts
\[
 q_0(\gamma)=\sum_j2^{-j}
       \frac{b_j(\gamma)}{1+\lambda(b_j)(r(\gamma))},
 \qquad q(\gamma)=q_0(\gamma)/\lambda(q_0)(r(\gamma)).
 \tag{14D.1}
\]
The integral of the series lies in \((0,1]\), by full support and the covering property, so the normalization is legitimate. This probability is equivalent to Haar measure on each fibre.

First \(D\) is multiplicative almost everywhere for the composable-pair measure
\[
 d\tau(\alpha,\beta)=d\mu(r(\alpha))\,
                      d\lambda^{r(\alpha)}(\alpha)\,
                      d\lambda^{s(\alpha)}(\beta).
 \tag{14D.2}
\]
The displayed notation means iterated kernel integration, not a product of pointwise differentials. Consider the involutions
\[
 T(\alpha,\beta)=(\alpha^{-1},\alpha\beta),\qquad
 S(\alpha,\beta)=(\alpha\beta,\beta^{-1}).
 \tag{14D.3}
\]
Left invariance, followed by inversion of \(\alpha\), gives
\(T_*\tau=D(\alpha)^{-1}\tau\). Replacing \(\beta\) by \(\gamma=\alpha\beta\) identifies \(\tau\) with
\(\int\lambda^x\times\lambda^x\,d\mu(x)\); in these coordinates \(S\) interchanges \(\alpha\) and \(\gamma\), so \(S_*\tau=\tau\). Both maps are nonsingular. The equality \(TST=STS\), whose common value is \((\beta^{-1},\alpha^{-1})\), and the chain rule for Radon–Nikodym derivatives give respectively the densities
\((D(\alpha)D(\beta))^{-1}\) and \(D(\alpha\beta)^{-1}\). Thus
\[
 D(\alpha\beta)=D(\alpha)D(\beta)\quad\text{for }\tau\text{-almost every pair}.
 \tag{14D.4}
\]

We next remove these exceptional pairs. The following explicit measurable construction avoids assuming a strictification theorem.

For each unit \(x\), take the space \(E_x\) of finite real measurable functions on \(\mathcal G^x\), modulo equality almost everywhere, with complete metric
\[
 d_x(f,g)=\int\min\{1,|f-g|\}\,q\,d\lambda^x.
 \tag{14D.5}
\]
It is separable: rational simple functions from a fixed countable generating algebra of Borel sets are dense on every fibre. Completeness follows by taking a Cauchy subsequence with successive distances less than \(2^{-3n}\); the probability of a difference exceeding \(2^{-n}\) is then at most \(2^{-2n}\). Borel–Cantelli gives an almost everywhere convergent subsequence, and bounded convergence gives convergence in this metric.

These spaces form a standard Borel field without a measurable-choice assumption. If \(e_n\) is the countable simple family, encode a point by its distances \(a_n\) to \(e_n\). Exactly the codes satisfying
\[
 |a_n-a_m|\leq d_x(e_n,e_m)\leq a_n+a_m,
                 \qquad\inf_n a_n=0
 \tag{14D.6}
\]
occur in the completion. Choose indices with \(a_n\to0\) to verify sufficiency and uniqueness. These are countably many Borel conditions on \((x,(a_n))\). Addition, scalar multiplication, and integrals of bounded continuous functions of a field element are Borel: choose the first simple approximant at each prescribed distance, carry out the operation on the simple functions, and pass to the limit. The integral convergence follows from convergence in probability and boundedness. A field element also has a jointly Borel function representative: take approximants at distances \(2^{-3n}\), use the almost everywhere convergence just proved on every fibre, and set the value zero where the limit fails.

Define the centre of \(f\in E_x\) as the unique real number \(c_x(f)\) satisfying
\[
 \int\arctan(f-c_x(f))\,q\,d\lambda^x=0.
 \tag{14D.7}
\]
The integral is continuous and strictly decreasing in the candidate centre, with limits \(\pi/2\) and \(-\pi/2\). Its root is Borel, by testing rational candidate centres, and continuous in \(f\) for the probability metric. Translation by a constant translates the root by that constant. Consequently the centred functions \(c_x(f)=0\) identify \(E_x\) modulo addition of constants. They are a closed Polish subspace of \(E_x\); the centred simple family is dense.

Left translation \(A_\gamma f(\eta)=f(\gamma^{-1}\eta)\) gives a continuous isomorphism \(E_{s(\gamma)}\to E_{r(\gamma)}\). Equivalent finite measures define the same convergence-in-probability topology, and the translated Haar probabilities are equivalent by left invariance. Its map on the Borel fields is Borel: check a simple function by integration against (14D.5), then use simple approximants. On centred functions let
\(B_\gamma f=A_\gamma f-c_{r(\gamma)}(A_\gamma f)\). These maps obey
\(B_\gamma B_\eta=B_{\gamma\eta}\) exactly, because the original translations compose and preserve constants.

Replace any exceptional zero or infinite values of the initial \(D\) by 1 and let
\(f_x(\eta)=\log D(\eta)\) on \(\mathcal G^x\). This is a Borel section of \(E\). Write \(z_x=f_x-c_x(f_x)\). Formula (14D.4) says
\[
 z_{r(\gamma)}=B_\gamma z_{s(\gamma)}
                     \quad\text{for }\nu\text{-almost every }\gamma.
 \tag{14D.8}
\]
For every unit \(x\), form the law of the centred random element
\(B_\gamma z_{s(\gamma)}\), where \(\gamma\) is distributed according to \(q\lambda^x\). Let \(F\) be the set of units where this law is a point mass. It is Borel: the expectation of the distance between two independent such elements is zero exactly when their common law is a point mass. The double integral is Borel by the kernel construction above. By (14D.8), \(F\) is \(\mu\)-conull.

Moreover \(F\) is invariant under every arrow, not just almost every arrow. Left translation changes the probability on the arrow fibre to an equivalent probability and carries each random element by the homeomorphism \(B_\sigma\). Thus its law is a point mass at one endpoint if and only if it is one at the other. Denote its unique value by \(z'_x\). Its distances to the centred simple family are the corresponding expected distances; (14D.6) therefore proves that \(z'\) is Borel. The same translation argument gives
\[
 z'_{r(\sigma)}=B_\sigma z'_{s(\sigma)}
                     \qquad(\sigma\in\mathcal G|_F).
 \tag{14D.9}
\]

The Borel set \(C=\{x\in F:z'_x=z_x\}\) is \(\mu\)-conull. On \(C\) retain the uncentred representative \(f_x\); on \(F\setminus C\) choose the centred representative \(z'_x\). Call this field \(\ell_x\). For every \(\sigma\in\mathcal G|_F\), (14D.9) means that
\(\ell_{r(\sigma)}-A_\sigma\ell_{s(\sigma)}\) is a constant almost everywhere in its fibre. Call it \(b(\sigma)\). This constant is a Borel function of the arrow: integrate its arctangent against the Haar probability and apply the tangent function. Translation preserves constants, so
\(b(\sigma\eta)=b(\sigma)+b(\eta)\) for every composable pair in the reduction.

Set \(\widetilde D(\sigma)=\exp b(\sigma)\) on \(\mathcal G|_F\), and 1 on its complement. Since \(F\) is invariant, there are no arrows crossing these two parts; \(\widetilde D\) is a Borel homomorphism on the entire groupoid. Quasi-invariance implies that \(\nu\)-almost every arrow has both endpoints in \(C\): range-null sets are \(\nu\)-null, source-null sets are \(\nu^{-1}\)-null and hence \(\nu\)-null. On those arrows (14D.4) gives \(b(\sigma)=\log D(\sigma)\) almost everywhere. We have therefore preserved the original Radon–Nikodym derivative while obtaining the exact product rule. ∎

The measurable correction of almost everywhere homomorphisms is classically due to Ramsay; compare [Muhly–Williams 2008, Remark 7.1, p. 43] and the references there. The argument above proves the scalar modular case needed here, including the measurable field and invariant conull set. It does not assume a locally continuous modular function.

### Coefficient densities and the Hilbert fibres

The coefficient measures of vectors in \(H_{00}\) are absolutely continuous with respect to \(\nu\). Here is the needed argument. For a compact \(\nu\)-null set \(A\) in a patch, put \(b=1_A\), and let \(N=\{x:\lambda^x(A)>0\}\), a Borel \(\mu\)-null set. For any continuous patch \(g\), \(b*g\) vanishes outside \(r^{-1}(N)\), directly from its integral. Thus (14E.7) gives
\([b*g\otimes\xi]=M(1_N)[b*g\otimes\xi]=0\).
The coefficient identity following (14E.7) shows that
\(\ell_{a,c}(1_A)=0\) for \(a,c\in H_{00}\), by writing both as finite convolution vectors. In fact the same holds for every compact subset of \(A\). The total variation of a complex Radon measure on a \(\nu\)-null set is then zero: its restriction has zero integrals on all continuous functions by regular approximation with compact sets, hence is the zero measure. Inner regularity on the patches proves absolute continuity for every Borel null set.

Choose the exact positive modular homomorphism just constructed and keep the notation \(D\). The measure \(\nu_0=D^{-1/2}\nu\) is symmetric under inversion: substitution gives \(D(\gamma^{-1})^{-1/2}D(\gamma)^{-1}=D(\gamma)^{-1/2}\). It is sigma-finite and equivalent to \(\nu\). For the basis \(\zeta_i\in H_{00}\) chosen in (14E.3), take Borel densities
\(\rho_{ij}=d\ell_{\zeta_i,\zeta_j}/d\nu_0\). They are chosen for this countable family only. We do not suppose that arbitrary independently chosen Radon–Nikodym representatives are pointwise sesquilinear in all vectors.

For compactly supported fibre functions define
\[
 \begin{split}
 Q_x(f\otimes\zeta_i,g\otimes\zeta_j)
  =\int\!\int &\overline{f(\eta)}g(\gamma)
    \rho_{ij}(\eta^{-1}\gamma)\\
   &{}· D(\eta)^{-1/2}D(\gamma)^{-1/2}
         \,d\lambda^x(\eta)d\lambda^x(\gamma).
 \end{split}
 \tag{14E.10}
\]
First interpret this for restrictions of global test functions and for almost every \(x\). Expanding \(f^**g\), using Haar left invariance, and then inverting the first variable with the symmetric measure \(\nu_0\), gives
\[
 \langle L(f)\zeta_i,L(g)\zeta_j\rangle
                    =\int_X Q_x(f\otimes\zeta_i,g\otimes\zeta_j)\,d\mu(x).
 \tag{14E.11}
\]
The separate half-density factors in (14E.10) are necessary. They arise from
\(D(\eta^{-1}\gamma)=D(\eta)^{-1}D(\gamma)\) during that inversion.

We verify finiteness and positivity on a single conull set. Choose countably many nonnegative finite patch envelopes \(b_l\), cofinal for compact patch supports and their finite unions. They can be made equal to at least one on a compact exhaustion of each member of a countable precompact Hausdorff cover; include all finite sums. The absolute double integral with envelope \(b_l(\eta)b_l(\gamma)|\rho_{ij}(\eta^{-1}\gamma)|\) and the half densities has global integral
\[
 \int (b_l^**b_l)(\sigma)|\rho_{ij}(\sigma)|\,d\nu_0(\sigma)<\infty.
 \tag{14E.12}
\]
This is the same nonnegative change of variables as (14E.11). Finiteness holds because the coefficient total variation is Radon on the finite compact patch envelopes of \(b_l^**b_l\). Excluding one null set for all \(l,i,j\) makes every such fibre integral finite, and the forms continuous for uniform convergence on fixed fibre compact sets.

Choose a countable test family dense on each compact patch envelope. For each finite rational complex tensor combination \(\alpha\) from it, localization by \(a\in C_c(X)\) in (14E.11) gives
\[
 \int |a(x)|^2 Q_x(\alpha,\alpha)\,d\mu(x)
                  =\Big\|\sum_i L((a\circ r)f_i)\zeta_i\Big\|^2\geq0.
 \tag{14E.13}
\]
Thus \(Q_x(\alpha,\alpha)\) is real and nonnegative almost everywhere. This follows from uniqueness of Radon densities tested by continuous nonnegative cutoffs; the real and imaginary parts are locally integrable by (14E.12). Countably many \(\alpha\)'s give one Borel conull set. Continuity on fixed compact envelopes and polarization extend positivity and Hermitian symmetry to every finite tensor combination there.

Every \(f\in C_c(\mathcal G^x)\) is the restriction of a global patch test function. The range fibre is closed in each Hausdorff patch; split \(f\) by a partition of unity subordinate to finitely many such patches, extend each piece by Tietze, and multiply by a compact cutoff. Thus the fibre forms just constructed apply to all compactly supported fibre functions, not a smaller family.

We need an invariant conull set, since unitaries must act on every arrow in the relevant reduction. Left translation on the fibre tensors is
\[
 T_\sigma(f\otimes\zeta_i)(\gamma)
      =D(\sigma)^{1/2}f(\sigma^{-1}\gamma)\otimes\zeta_i.
 \tag{14E.14}
\]
The exact product rule for \(D\) and Haar invariance give, by substitution in both variables,
\(Q_{r(\sigma)}(T_\sigma\alpha,T_\sigma\beta)=Q_{s(\sigma)}(\alpha,\beta)\).
Indeed \((\sigma\eta)^{-1}(\sigma\gamma)=\eta^{-1}\gamma\), while the two factors \(D(\sigma)^{-1/2}\) cancel the scalar \(D(\sigma)\) from the two translated functions. This identity holds for absolute integrals as well, and translation is a bijection of the compact fibre test functions. Finiteness of all those integrals and positivity therefore propagate along every arrow.

Shrink the preceding good set to a sigma-compact conull set \(C=\bigcup K_n\), using regularity of the finite \(\mu\). Cover the arrow space by countably many compact Hausdorff chart neighborhoods \(P_m\). Its saturation
\(F=\bigcup_{m,n}r(P_m\cap s^{-1}(K_n))\) is Borel, since each displayed range image is compact in the Hausdorff unit space. It is invariant, conull, and consists entirely of good units by the translation identity. Complete the fibre tensor spaces modulo the \(Q_x\)-null vectors for \(x\in F\), and take zero fibres outside \(F\). Call these Hilbert spaces \(H_x\).

The countable fundamental tensors \(f_l\otimes_x\zeta_i\) have Borel Gram coefficients by kernel integration and (14E.10). The same explicit Gram–Schmidt construction used for (14E.4) equips their completions with a standard Borel Hilbert field. They are total at every good unit by compact-envelope continuity and the fibre extension argument. Formula (14E.14) induces a unitary \(V_\sigma:H_{s(\sigma)}\to H_{r(\sigma)}\), with inverse \(V_{\sigma^{-1}}\), and the unique map of zero fibres outside \(F\). Its fundamental matrix coefficients are Borel: substitute (14E.14) into (14E.10) and integrate the jointly Borel integrand. Hence \(\sigma\mapsto V_\sigma\) is Borel. The formula and exact modular rule also give \(V_\sigma V_\tau=V_{\sigma\tau}\) for every composable pair. Invariance of \(F\) ensures no arrow crosses to the zero-fibre part.

### Recovering the representation and its bound

Define
\[
 W(L(f)\zeta_i)(x)=f|_{\mathcal G^x}\otimes_x\zeta_i.
 \tag{14E.15}
\]
Equation (14E.11) makes this well-defined and isometric on the span in (14E.3), so it extends isometrically from all of \(H\). Its range is all of \(L^2(X,H_x,\mu)\): it contains the fundamental tensor sections and their continuous unit multiples, by (14.14). Those multiples are dense. For completeness, approximate a square-integrable Borel section by finite combinations of the measurable Gram–Schmidt sections, truncate to sets where their coefficients and norms are bounded, and approximate the scalar coefficients in the associated finite Radon weighted measures by continuous compact functions. Gram–Schmidt sections themselves are Borel scalar combinations of fundamental tensors, and the same truncation and scalar approximation puts them in the closure of those continuous multiples. The isometric range is closed, proving surjectivity.

Any quasi-invariant measure, Borel Hilbert field and exact unitary action as above has a bounded integrated form. Its weak matrix coefficient is
\[
 B_f(\xi,\eta)=\int f(\sigma)
  \langle\xi(r(\sigma)),V_\sigma\eta(s(\sigma))\rangle
                         D(\sigma)^{-1/2}\,d\nu(\sigma).
 \tag{14E.16}
\]
Weighted Cauchy–Schwarz bounds its absolute value by
\[
 \begin{split}
 &\left(\int |f(\sigma)|\|\xi(r(\sigma))\|^2\,d\nu(\sigma)\right)^{1/2}\\
 &\qquad{}·\left(\int |f(\sigma)|\|\eta(s(\sigma))\|^2
                                 D(\sigma)^{-1}\,d\nu(\sigma)\right)^{1/2}
       \leq \|f\|_I\|\xi\|\|\eta\|.
 \end{split}
 \tag{14E.17}
\]
The first factor uses the range row bound; change \(D^{-1}\nu\) to \(\nu^{-1}\) in the second to use the source bound. The bounded sesquilinear form defines \(\pi(f)\). Its vector integral exists for almost every range unit: fibrewise Cauchy–Schwarz bounds the squared integral of \(|f|\|\eta\circ s\|D^{-1/2}\) by the row bound times \(\lambda^x(|f|\|\eta\circ s\|^2D^{-1})\), whose \(\mu\)-integral is at most the source bound times \(\|\eta\|^2\). Measurable fibre coordinates give the vector integral and identify it with (14E.16).

Inversion of the symmetric \(\nu_0\), together with \(V_{\sigma^{-1}}=V_\sigma^*\), gives \(\pi(f)^*=\pi(f^*)\). For the product, the absolute iterated scalar integral is bounded by \(\|f\|_I\|g\|_I\|\xi\|\|\eta\|\): apply (14E.17) twice to the positive scalar kernels with weights \(|f|\) and \(|g|\), acting on the scalar functions \(\|\xi(x)\|\) and \(\|\eta(x)\|\). These kernels are already bounded by the preceding argument, independently of any product identity. Fubini is therefore legitimate. In the inner integral set \(\tau=\sigma\beta\); Haar invariance changes \(\lambda^{s(\sigma)}(\beta)\) to \(\lambda^{r(\sigma)}(\tau)\), while \(D(\sigma)^{-1/2}D(\beta)^{-1/2}=D(\tau)^{-1/2}\) and \(V_\sigma V_\beta=V_\tau\). Interchanging \(\sigma,\tau\) leaves precisely \((f*g)(\tau)\) and proves \(\pi(f)\pi(g)=\pi(f*g)\).

We verify that this is the original representation. On the dense test span, insert (14E.14) in (14E.16). The two functions in (14E.10) are respectively \(f|_{\mathcal G^x}\) and \(D(\sigma)^{1/2}g(\sigma^{-1}\,cdot)\). The factor \(D(\sigma)^{-1/2}\) in the integrated form cancels that scalar, and the remaining inner integral in \(\sigma\) is exactly \(h*g\). Thus
\[
 \begin{aligned}
 &\langle W(L(f)\zeta_i),\pi(h)W(L(g)\zeta_j)\rangle\\
 &\quad=\int_X Q_x(f\otimes\zeta_i,(h*g)\otimes\zeta_j)\,d\mu(x)\\
 &\quad=\langle L(f)\zeta_i,L(h)L(g)\zeta_j\rangle.
 \end{aligned}
 \tag{14E.18}
\]
The expansion is absolutely integrable: replace the compact test functions by positive envelopes and bound the extra \(\sigma\) integral by the envelope convolution; (14E.12) then applies. Hence \(W\) intertwines on that dense span. The bounded operator \(W^*\pi(h)W\) also agrees with \(L(h)\) on every \(\eta\in H_0\): test their difference against the dense span, move \(L(h)\) by its adjoint identity, and use the already established equality for \(h^*\) on that span. Every such matrix coefficient of the difference is zero.

We have proved both automatic \(I\)-contractivity and the measurable disintegration, including an exact Borel unitary action, for the full stated locally Hausdorff dense-domain case. The resulting operators have the weak integral formula (14.13). Their essential range is dense by the original hypothesis, so their extension is nondegenerate. ∎

This is Renault's disintegration theorem. [Muhly–Williams 2008, Appendix B, pp. 66–85] supplies the historical proof construction and [ibid., Theorem 7.8, pp. 45–46] the precise dense-domain statement. The argument here includes the local-unit, Borel-extension, quasi-invariance, scalar modular correction and measurable-field steps. It uses ordinary Radon measure theory and Hilbert-space completion throughout; no groupoid disintegration or measurable strictification theorem is an assumed proof provider.

## Transformation groupoids are crossed products

Let a second countable locally compact group \(H\) act continuously on a second countable locally compact Hausdorff \(X\), and let
\(\alpha_g b(x)=b(g^{-1}x)\). Use the target-first groupoid coordinates of Lesson 13 and its range Haar system \(dg\). The conversion is
\[
 (\mathcal T f)(g)(x)=\Delta_H(g)^{-1/2}f(x,g).
 \tag{14.16}
\]

**Theorem 14.3.** The map (14.16) extends to isomorphisms
\[
 C^*(X\rtimes H)\cong C_0(X)\rtimes_\alpha H,\qquad
 C_r^*(X\rtimes H)\cong C_0(X)\rtimes_{\alpha,r}H.
 \tag{14.17}
\]

**Proof.** On the compact core,
\[
 \begin{gathered}
 (f*g)(x,t)=\int_H f(x,a)g(a^{-1}x,a^{-1}t)\,da,\\
 f^*(x,t)=\overline{f(t^{-1}x,t^{-1})}.
 \end{gathered}
 \tag{14.18}
\]
The identity
\(\Delta(a)^{-1/2}\Delta(a^{-1}t)^{-1/2}=\Delta(t)^{-1/2}\)
proves preservation of convolution. The crossed-product involution of \(\mathcal T f\) is
\(\Delta(t)^{-1}\alpha_t((\mathcal T f)(t^{-1})^*)\); its modular coefficient is
\(\Delta(t)^{-1}\Delta(t^{-1})^{-1/2}=\Delta(t)^{-1/2}\), proving preservation of the involution. The inverse multiplies by \(\Delta^{1/2}\).

The image core consists of jointly compactly supported coefficient kernels. It is dense in \(C_c(H,C_0(X))\) in the \(L^1\)-norm: on a fixed compact set of group coordinates, a \(C_c(X)\) cutoff approximates the compact set of coefficient values uniformly. Finite product approximation, or a partition of unity in the group coordinate, gives the joint kernels.

We verify the full norm, including both directions of the representation correspondence. Given a nondegenerate covariant pair \((P,U)\), its integrated form on \(\mathcal T C_c(X\rtimes H)\) is a *-representation by (14.18). Uniform convergence on a fixed compact set makes all its matrix coefficients continuous, since \(\Delta^{-1/2}\) is bounded on the group-coordinate compact set. Its essential range is dense by the crossed-product integrated-form correspondence and the core density just proved. Disintegration therefore makes this a groupoid \(I\)-contractive representation.

Conversely, take a nondegenerate groupoid \(I\)-contractive representation \(L\) and transfer it to the image core by \(\mathcal T\). Formula (14.14) supplies the coefficient representation \(P\). For \(a\in H\), left multiplication by the desired group unitary must act on the core as
\[
 (Q_a F)(t)=\alpha_a(F(a^{-1}t)).
 \tag{14.19}
\]
For the inner-product identity, the convolution integrand in
\((Q_a F)^**(Q_a G)(t)\) is
\(\Delta(s)^{-1}\alpha_{sa}(F((sa)^{-1})^*G((sa)^{-1}t))\).
Changing variable \(u=sa\) gives
\(\Delta(s)^{-1}\,ds=\Delta(u)^{-1}\,du\), including the right-translation Haar factor. Thus
\((Q_a F)^**(Q_a G)=F^**G\). Hence on the dense span of core vectors the rule
\(U_a L(F)\xi=L(Q_aF)\xi\) preserves every finite-sum inner product. It is well-defined, extends to an isometry, and \(Q_{a^{-1}}\) gives its inverse. The identities \(Q_aQ_b=Q_{ab}\) and \(Q_a(cF)=\alpha_a(c)Q_aF\) give the group law and covariance.

As \(a\) varies near a fixed point, \(Q_aF\) varies uniformly with its support in one compact subset of \(X\times H\). Such convergence implies \(I\)-norm convergence: dominate that compact set by one positive compact bump and use its bounded fibre integrals. Thus \(U_a\) is strongly continuous on the dense span, hence everywhere. Finally, on a core vector \(L(G)\xi\), integration of \(P(F(t))U_t\) gives \(L(F*G)\xi\), by compact integration and convolution. Therefore its integrated form is the original \(L(F)\). This recovers the covariant pair uniquely. Taking suprema proves equality of the full norms in (14.17).

For the reduced norm, parametrize the source fibre at \(x\) by \(t\mapsto(tx,t)\). Its measure is right Haar measure
\(d\nu_H(t)=\Delta_H(t)^{-1}\,dt\). The unitary
\[
 V:L^2(H,\nu_H)\longrightarrow L^2(H,dt),\qquad
 (V\xi)(t)=\Delta_H(t)^{-1/2}\xi(t)
 \tag{14.20}
\]
converts (14.6) into
\[
 (VL_x(f)V^{-1}\xi)(t)=
   \int_H\Delta_H(a)^{-1/2}f(tx,a)\xi(a^{-1}t)\,da.
 \tag{14.21}
\]
This is the regular crossed-product pair with coefficient
\((P_x(b)\xi)(t)=b(tx)\xi(t)\) and left translation. The direct sum of all evaluation representations of \(C_0(X)\) is faithful. Its regular induction is the direct sum of these pairs, so Lesson 2 identifies its norm with the reduced crossed-product norm. The supremum in (14.9) is exactly that norm. ∎

Even when \(X\) is a point, forgetting \(\Delta^{-1/2}\) can give the wrong involution. For a unimodular group, including a discrete group, this correction is one.

## The étale expectation

Now assume \(\mathcal G\) is Hausdorff and étale, with counting measures. Its unit space is both open and closed. Zero extension embeds \(C_c(X)\) as a convolution subalgebra, acting in each source fibre by multiplication by \(b(r(\gamma))\). Its norm is \(\|b\|_\infty\), since the unit vector at any \(x\) detects \(b(x)\). Completion embeds \(C_0(X)\) in the reduced algebra.

**Theorem 14.4.** Restriction to the units extends to a faithful conditional expectation
\[
 E:C_r^*(\mathcal G)\longrightarrow C_0(X).
 \tag{14.22}
\]

**Proof.** On test functions,
\[
 E(f)(x)=\langle\delta_x,L_x(f)\delta_x\rangle=f(x).
 \tag{14.23}
\]
It belongs to \(C_c(X)\) and its supremum norm is at most \(\|f\|_r\); hence it extends to \(C_0(X)\). At every matrix level evaluation of this extension is compression of the corresponding regular representation to its unit vector. Thus it is completely positive and contractive. It fixes \(C_0(X)\), and endpoint multiplication gives \(E(bac)=bE(a)c\) for \(b,c\in C_0(X)\), first on the core and then by continuity.

For faithfulness, let \(a\geq0\) and \(E(a)=0\). For every \(\gamma\in\mathcal G_x\), the kernel formula, extended by continuity, gives
\[
 \langle\delta_\gamma,L_x(a)\delta_\gamma\rangle
       =E(a)(r(\gamma))=0.
 \tag{14.24}
\]
Therefore \(L_x(a)^{1/2}\delta_\gamma=0\). These vectors form an orthonormal basis, so \(L_x(a)=0\) for all \(x\); definition (14.9) gives \(a=0\). ∎

The Hausdorff hypothesis here has content. In Lesson 13's doubled-origin étale group bundle, the patch function with triple \((F,a,b)=(0,1,-1)\) restricts to a function on the units which is zero away from zero and one at zero. It is not in \(C_0(\mathbb R)\). Consequently restriction of all patch kernels cannot define an expectation with the codomain in (14.22). Counting measures alone do not repair this.

## Effective groupoids and the diagonal uniqueness theorem

For this section and the next three, let \(G\) be any locally compact Hausdorff étale groupoid, with counting Haar system, and write \(D=C_0(G^{(0)})\), \(A=C_r^*(G)\). The reduced arguments do not require second countability. The full amenable corollary below uses the standing countability hypotheses of this lesson.

The groupoid is **effective** when the interior of its isotropy is just its unit space:
\[
\operatorname{Iso}(G)^\circ=G^{(0)},\qquad
\operatorname{Iso}(G)=\{\gamma:r(\gamma)=s(\gamma)\}.
\tag{14I.1}
\]
For a second countable Hausdorff étale groupoid this is equivalent to density of units with trivial isotropy. Here is the precise Baire argument. Cover the nonunit arrows by countably many relatively compact bisection patches whose closures remain in nonunit bisections. For each compact closure \(K\), its fixed-unit set
\(\{s(\gamma):\gamma\in K,\ r(\gamma)=s(\gamma)\}\)
is closed. If it contained an open unit set, the corresponding bisection over that set would give an open nonunit subset of isotropy, contradicting effectiveness. These sets are nowhere dense. Their countable union contains every unit with nontrivial isotropy; local compactness and the Baire theorem give the asserted density. Conversely, an open nonunit isotropy bisection has an open source set containing no free unit. Outside the countable setting we use (14I.1), rather than assuming the two conditions coincide.

**Theorem 14I.1 (diagonal uniqueness).** If \(G\) is effective, every C*-homomorphism \(A\to B\) that is injective on \(D\) is injective on \(A\). Equivalently, every nonzero ideal of \(A\) meets \(D\) nontrivially.

**Proof.** We first prove a compression estimate without a countable cover. Fix \(f\in C_c(G)\), a nonempty open unit set \(O\), and write
\(f-E(f)=\sum_{i=1}^n f_i\), where each \(f_i\) has compact support \(K_i\) in a nonunit bisection. A finite partition of unity on the compact support gives this decomposition. The fixed-unit set of each \(K_i\) is closed and has empty interior, by the argument preceding the theorem. Thus some \(x\in O\) avoids all these finitely many sets. The compact image \((r,s)(K_i)\) does not contain \((x,x)\). Shrinking a neighborhood \(V\) of \(x\) makes \(VK_iV\) empty for every \(i\). A unit bump \(h\), with \(0\leq h\leq1\), \(h(x)=1\), and support in \(V\), then satisfies
\[
hfh=hE(f)h.
\tag{14I.2}
\]

Let \(\phi:A\to B\) be faithful on \(D\) and \(a\geq0\). Choose \(f\in C_c(G)\) with \(\|a-f\|<\varepsilon\), and choose \(O\) where \(E(a)>\|E(a)\|-\varepsilon\); if \(E(a)=0\) the desired inequality is automatic. In (14I.2) choose \(x\in O\). Contractivity of \(E\) and isometry of \(\phi|_D\) give
\[
\|\phi(a)\|\geq\|\phi(hfh)\|-\varepsilon
 =\|hE(f)h\|-\varepsilon
 \geq\|E(a)\|-3\varepsilon.
\tag{14I.3}
\]
Let \(\varepsilon\to0\). If \(\phi(b)=0\), apply this inequality to \(b^*b\). It gives \(E(b^*b)=0\), hence \(b=0\) by the faithful expectation already proved in (14.22). For an ideal \(J\) disjoint from \(D\), the quotient map is faithful on \(D\), so the same conclusion makes \(J=0\). The equivalence follows. ∎

## The diagonal is a Cartan subalgebra

We call \(D\subseteq A\) **Cartan** when it is maximal abelian, contains an approximate identity for \(A\), has a faithful conditional expectation, and its normalizers
\[
N_A(D)=\{n\in A:nDn^*\subseteq D,\ n^*Dn\subseteq D\}
\]
span a dense subspace of \(A\).

**Theorem 14I.2.** The canonical \(C_0(G^{(0)})\) is Cartan in \(C_r^*(G)\) if and only if \(G\) is effective.

**Proof.** For later use define the coefficient function
\[
j(a)(\gamma)=
\langle\delta_\gamma,\lambda_{s(\gamma)}(a)\delta_{s(\gamma)}\rangle.
\tag{14I.4}
\]
It equals \(f(\gamma)\) for \(a=f\in C_c(G)\), and \(\|j(a)\|_\infty\leq\|a\|\). Norm approximation by core functions therefore makes \(j(a)\in C_0(G)\). It is injective: on a source fibre every matrix entry is
\[
\langle\delta_\gamma,\lambda_x(a)\delta_\eta\rangle
   =j(a)(\gamma\eta^{-1}),\qquad\gamma,\eta\in G_x.
\tag{14I.5}
\]
This follows by convolution on the core and by norm continuity on its completion. If \(j(a)=0\), every regular operator is zero.

Suppose \(a\) commutes with \(D\). The left and right coefficient formulas give
\[
(d(r(\gamma))-d(s(\gamma)))j(a)(\gamma)=0
\quad(d\in D).
\tag{14I.6}
\]
Continuous unit functions separate distinct units, so \(j(a)\) vanishes off isotropy. If it were nonzero at a nonunit isotropy arrow, continuity and the closedness of the unit space would give a nonempty open nonunit subset of isotropy. Effectiveness excludes this. Hence \(j(a-E(a))=0\); injectivity gives \(a=E(a)\in D\), proving maximal abelianness.

Every core function supported on a bisection normalizes \(D\), by the source and range multiplication formulas. Finite partitions on compact supports show that such functions span \(C_c(G)\), so regularity follows. Unit bumps equal to one on the compact ranges and sources of a core function give a two-sided approximate identity, and density gives one for \(A\). The expectation and its faithfulness were proved earlier. These are all the Cartan axioms.

Conversely, if \(G\) is not effective, choose a nonzero function supported on a nonunit isotropy bisection. It commutes with every unit function, by \(r=s\) on its support, but is not in \(D\), since (14I.4) is nonzero off the units. Thus \(D\) is not maximal abelian. ∎

This gives a concrete way to recognize the diagonal inside the reduced algebra. The additional reconstruction of a general abstract Cartan pair requires a twist and a Weyl groupoid; maximal abelianness alone is not that reconstruction theorem.

## Inner exactness and all dynamical ideals

For an open invariant \(U\subseteq G^{(0)}\), extension by zero identifies \(C_r^*(G|_U)\) isometrically with an ideal \(I_U\subseteq A\). Source-fibre regular operators inside \(U\) give its original norm; those outside \(U\) act as zero. The ideal is generated by \(C_0(U)\), using unit bumps on compact sources and ranges. Restriction to \(F=G^{(0)}\setminus U\) gives a surjection
\[
q_U:A\to C_r^*(G|_F).
\]
Regular fibres over \(F\) prove contractivity; finite bisection patches extend compactly supported functions on the closed reduction and prove dense range. A C*-homomorphism has closed range, so it is onto. The kernel need not equal \(I_U\), as the group-bundle example below demonstrates.

We call \(G\) **inner exact** when \(\ker q_U=I_U\) for every open invariant \(U\). It is **strongly effective** when every closed invariant reduction is effective.

**Theorem 14I.3.** If \(G\) is inner exact and strongly effective, then
\[
U\longmapsto I_U
\tag{14I.7}
\]
is a lattice isomorphism from open invariant unit sets to all closed two-sided ideals of \(C_r^*(G)\). An effective minimal groupoid has simple reduced C*-algebra, even without inner exactness. For an amenable groupoid satisfying this lesson's standing countability assumptions, all ideals are of the form (14I.7) if and only if it is strongly effective; its full algebra is simple if and only if it is effective and minimal.

**Proof.** Let \(J\triangleleft A\). Its coefficient intersection is \(J\cap D=C_0(U)\) for some open \(U\). The set \(U\) is invariant: conjugating a unit function by a bump on a bisection carries a nonzero value at its source to a nonzero value at its range, while staying in \(J\cap D\). Thus \(I_U\subseteq J\). Also
\[
I_U\cap D=C_0(U);
\tag{14I.8}
\]
one containment is immediate, and the other follows since the coefficient functions of \(I_U\) vanish outside \(G|_U\).

Inner exactness identifies \(A/I_U=C_r^*(G|_F)\). The ideal \(J/I_U\) has zero intersection with \(C_0(F)\). Indeed, if its image contains a unit function \(b_F\), lift \(b_F\) to \(b\in C_0(G^{(0)})\). A representative \(a\in J\) differs from \(b\) by an element of \(I_U\subseteq J\); hence \(b\in J\cap D=C_0(U)\) and \(b_F=0\). Strong effectiveness and Theorem 14I.1 on \(G|_F\) force \(J/I_U=0\). This proves surjectivity; (14I.8) proves injectivity and preservation of order. An order isomorphism of these complete lattices preserves meets and joins.

For an effective minimal \(G\), Theorem 14I.1 makes a nonzero \(J\) meet \(D\). The resulting invariant \(U\) is nonempty. Minimality says it is the whole unit space, so \(J\) contains a unit approximate identity and equals \(A\). Conversely, a proper nonempty invariant open set gives a proper nonzero \(I_U\), so reduced simplicity always implies minimality.

In the amenable case, amenability passes to invariant closed and open reductions by restricting its probability fields. Theorem 14.7 and full exactness then imply inner exactness. It remains to show necessity of strong effectiveness. Suppose a closed invariant reduction \(H=G|_F\) is not effective. On each orbit \([x]\subseteq H^{(0)}\), define
\[
\epsilon_x(f)\delta_y=\sum_{\gamma\in H_y}f(\gamma)\delta_{r(\gamma)}.
\tag{14I.9}
\]
Convolution and inversion prove multiplicativity and the adjoint identity, by regrouping composable pairs; the row and column sum bounds are at most \(\|f\|_I\), so Schur's estimate proves boundedness. These are full representations. Amenable norm equality makes them representations of the reduced algebra too. Their direct sum is faithful on \(C_0(F)\). But a nonunit isotropy bisection, and its source unit function with the same values along that bisection, act identically in every \(\epsilon_x\). Their difference is a nonzero core function, detected by the regular coefficient map. Thus this direct sum has a nonzero kernel \(K\) disjoint from \(C_0(F)\). Its preimage in \(A\) strictly contains \(I_{G^{(0)}\setminus F}\) and has the same diagonal intersection. It cannot be dynamical, by (14I.8). This proves necessity. For simplicity take \(F=G^{(0)}\), combine this argument with minimality, and use full–reduced equality. ∎

The distinction between effectiveness and strong effectiveness is real. Translation of \(\mathbb Z\) on its one-point compactification is effective, since every finite point is free. The fixed point at infinity is a closed invariant reduction with isotropy \(\mathbb Z\). Its quotient algebra is \(C^*(\mathbb Z)=C(\mathbb T)\), whose many ideals are invisible to its scalar diagonal. Thus diagonal uniqueness for the whole groupoid does not imply that every ideal is determined by a unit set.

## The sandwich description without residual effectiveness

Inner exactness still controls ideals when some closed reductions are ineffective. The following refinement is due to Brix, Carlsen and Sims.

In this theorem \(\operatorname{supp}j(J)\) means the union of the sets where the coefficient functions of elements of \(J\) are nonzero, without taking a closure.

**Theorem 14I.4 (ideal sandwiches and residual triples).** Suppose \(G\) is inner exact. For every ideal \(J\triangleleft A\), define
\[
\begin{aligned}
U_J&=\{x:d(x)\ne0\text{ for some }d\in J\cap D\},\\
V_J&=\{x:E(a)(x)\ne0\text{ for some }a\in J\}.
\end{aligned}
\tag{14I.10}
\]
These are open invariant sets, and \(I_{U_J}\) is the largest dynamical ideal contained in \(J\), while \(I_{V_J}\) is the smallest dynamical ideal containing \(J\). Every ideal is specified uniquely by a triple
\[
(U,V,K),\quad U\subseteq V,\quad
K\triangleleft C_r^*(G|_{V\setminus U}),\quad
K\cap C_0(V\setminus U)=0,\quad
\operatorname{supp}j(K)=G|_{V\setminus U}.
\tag{14I.11}
\]
The empty reduction is allowed, with \(K=0\), so dynamical ideals are included.

**Proof.** The proof of Theorem 14I.3 already gives openness, invariance and the largest-ideal assertion for \(U_J\). Write
\(S=\{\gamma:j(a)(\gamma)\ne0\text{ for some }a\in J\}\).
Multiplying by bisection bumps on either side carries any nonzero coefficient at \(\gamma\) to one at every composable translate of \(\gamma\). For instance a bump of value one at \(\gamma^{-1}\) turns it into a nonzero unit coefficient at \(s(\gamma)\). Taking adjoints also gives the range unit. Conversely a nonzero unit coefficient can be carried to any arrow starting at that unit. Thus
\[
S=G|_{V_J},\qquad V_J=s(S)=r(S).
\tag{14I.12}
\]
It follows that \(V_J\) is open and invariant and contains \(U_J\).

For \(a\in J\), \(E(a^*a)\) vanishes outside \(V_J\). Restriction commutes with expectations; therefore
\[
E_{G|_{G^{(0)}\setminus V_J}}
   (q_{V_J}(a)^*q_{V_J}(a))=0.
\]
Faithfulness of that reduced expectation makes \(q_{V_J}(a)=0\). Inner exactness gives \(a\in I_{V_J}\). If \(J\subseteq I_W\), its coefficients vanish outside \(G|_W\), so (14I.12) gives \(V_J\subseteq W\). This proves the smallest-ideal assertion, with the expectation-to-ideal step explicit.

Restrict inner exactness to \(I_V=C_r^*(G|_V)\): the sequence
\[
0\to I_U\to I_V\to C_r^*(G|_{V\setminus U})\to0
\tag{14I.13}
\]
is exact. Indeed the last algebra embeds as the open-reduction ideal in \(C_r^*(G|_{G^{(0)}\setminus U})\); the restriction of \(q_U\) to \(I_V\) has kernel \(I_U\) and dense, hence closed, range there.

For \(U=U_J,V=V_J\), the image \(K=J/I_U\) in (14I.13) has zero diagonal intersection by the lift argument in Theorem 14I.3. Its support is the whole residual groupoid by (14I.12) and restriction of coefficient functions. Conversely, given a triple (14I.11), take the preimage of \(K\) under \(I_V\to C_r^*(G|_{V\setminus U})\). This is an ideal of \(I_V\), hence of \(A\): if \(a\in A\), multiply a vector of the ideal using an approximate identity of \(I_V\) to see invariance under \(a\). Its diagonal intersection is exactly \(C_0(U)\), by the zero-intersection hypothesis. Its coefficient support is \(G|_V\), using full residual support together with the included \(I_U\). Thus its two sandwich sets are \(U,V\). Equation (14I.13) recovers \(K\), proving that the constructions are inverse. ∎

Strong effectiveness removes every nonzero diagonal-disjoint residual ideal by Theorem 14I.1, so (14I.11) then collapses to \(U=V\). The sandwich theorem identifies precisely what remains to be classified when an invariant unit set alone is insufficient.

## Invariant open subsets and full exactness

A subset \(U\subseteq X\) is invariant when no arrow has just one endpoint in \(U\). Take \(U\) open, and set \(F=X\setminus U\). Every range fibre over a point of \(U\), or of \(F\), lies entirely in the corresponding reduction. Therefore its original Haar measure is retained in full. The reduced Haar families are continuous, by zero extension for \(U\), and compact patch extension and restriction for \(F\).

**Theorem 14.5.** Zero extension and restriction give the exact sequence
\[
 0\longrightarrow C^*(\mathcal G|_U)
   \overset{\iota}{\longrightarrow}C^*(\mathcal G)
   \overset{R_F}{\longrightarrow}C^*(\mathcal G|_F)
   \longrightarrow0.
 \tag{14.25}
\]

**Proof.** Zero extension identifies \(C_c(\mathcal G|_U)\) with an algebraic two-sided ideal of \(C_c(\mathcal G)\). Its \(I\)-norm is unchanged. Restricting a full representation of \(\mathcal G\) therefore gives the upper bound for the norm of this inclusion. For the opposite bound, disintegrate any separable nondegenerate representation of \(\mathcal G|_U\). Extend its measure by zero from \(U\) to \(X\), and its Hilbert bundle by zero fibres outside \(U\). Invariance ensures that all relevant arrows still act between the same fibres. The resulting integrated representation of \(\mathcal G\) is \(I\)-contractive by the integrated bound proved above and agrees on the ideal core. Taking norms proves that \(\iota\) is isometric. Its image \(I_U\) is a closed ideal.

Restriction \(R_F\) is a *-homomorphism on the core, because its integration fibres over \(F\) are unchanged, and is \(I\)-contractive. Any \(I\)-contractive representation of the closed reduction can be composed with it, so it is contractive for the full norms too. It is onto the test-function algebra. For Hausdorff arrows this is compact-support extension from the closed arrow subspace. In the locally Hausdorff case split each compact patch term of the reduction into pieces contained in original Hausdorff arrow patches, extend each from the closed part of that patch, and sum. Thus the completed map is surjective. It kills \(I_U\).

It remains to prove that nothing more is killed. Let \(L\) be any nondegenerate representation of \(C^*(\mathcal G)/I_U\), viewed as a representation of the full algebra. For \(b\in C_c(U)\) and \(f\in C_c(\mathcal G)\), the function \((b\circ r)f\) belongs to \(C_c(\mathcal G|_U)\), by invariance. Hence (14.14) gives
\[
 M(b)L(f)=0,\qquad\text{and therefore }M(b)=0.
 \tag{14.26}
\]
The last step uses the dense essential range of \(L\), rather than any assumed exact sequence.

Reduce to separable cyclic subrepresentations and disintegrate \(L\). In that description \(M(b)\) is multiplication by \(b(x)\). A countable collection of compact bumps positive on a cover of \(U\) shows that the Hilbert fibres are zero almost everywhere on \(U\). Discarding those zero fibres leaves precisely a quasi-invariant measure and unitary representation on \(\mathcal G|_F\). Formula (14.13) then says that \(L\) factors through \(R_F\), with the full norm of the closed reduction.

All quotient representations factor in this way. Their supremum norm is therefore at most the norm in \(C^*(\mathcal G|_F)\); the already constructed surjection gives the reverse inequality. Thus \(C^*(\mathcal G)/I_U\cong C^*(\mathcal G|_F)\), proving exactness. ∎

On reduced algebras, zero extension is still isometric: the regular fibres over \(U\) are unchanged, and the kernel acts as zero at units outside \(U\). Restriction is still a surjection, since the regular fibres over \(F\) occur in the original supremum and the core restriction is onto. But
\[
 \overline{C_c(\mathcal G|_U)}^{\,\|\cdot\|_r}
       \ \subseteq\ \ker\big(C_r^*(\mathcal G)\to C_r^*(\mathcal G|_F)\big)
 \tag{14.27}
\]
can be a strict inclusion. The group-bundle section below constructs a positive contraction in this kernel whose finite-fibre norms all equal one; those norms prevent it from belonging to the open-restriction ideal. This supplies a concrete failure of equality, of the kind discussed in [Anantharaman-Delaroche 2023, §5.4, pp. 19–20] and [Sims 2017, discussion after Proposition 4.3.2, pp. 35–36]. The quotient-representation proof above uses the full universal norm, and cannot be transferred to the reduced norm without an additional exactness hypothesis.

## Pair kernels and group bundles

Let \(X\) be nonempty locally compact Hausdorff and second countable, and let \(\mu\) be a full-support positive Radon measure. The pair Haar system gives the operators
\[
 (K_f\xi)(x)=\int_X f(x,y)\xi(y)\,d\mu(y),\qquad
 f_{\xi,\eta}(x,y)=\xi(x)\overline{\eta(y)}.
 \tag{14.28}
\]

**Proposition 14.6.** For this system, both pair-groupoid completions are
\(\mathcal K(L^2(X,\mu))\).

**Proof.** Every source-fibre representation is \(K_f\) under the evident identification with \(L^2(X,\mu)\). Convolution and adjoint are operator composition and adjoint, and \(f_{\xi,\eta}\) is \(\theta_{\xi,\eta}\). Finite sums of these kernels with \(\xi,\eta\in C_c(X)\) are dense in the \(I\)-norm. Indeed approximate a compactly supported kernel uniformly by finite product sums supported in a fixed compact rectangle. The row and column errors are bounded by the uniform error times the measures of its two compact projections.

The finite-rank kernel algebra has exactly its usual compact-operator C*-norm. To see the full upper bound, put all the vectors in a given finite sum in their finite-dimensional span. Gram–Schmidt gives an orthonormal basis still in \(C_c(X)\), whose rank kernels are matrix units. Any *-representation is contractive on that finite matrix algebra, while \(K_f\) realizes its matrix norm. Full support ensures that equality of continuous kernels as operators does not identify distinct kernels. Thus the full and reduced norms agree on the finite-rank algebra; \(I\)-density extends this to all pair kernels. Since \(C_c(X)\) is dense in \(L^2(X,\mu)\), completion gives all compact operators. ∎

For a finite set with positive weights \(w_i=\mu(\{i\})\), the matrix is
\[
 f\longmapsto[\sqrt{w_iw_j}\,f(i,j)]_{i,j}.
 \tag{14.29}
\]
The kernels \(\delta_i(x)\delta_j(y)/\sqrt{w_iw_j}\) are matrix units. Counting measure yields the familiar \(M_n(\mathbb C)\). For \(X=\mathbb R\), Lebesgue measure yields \(\mathcal K(L^2(\mathbb R))\), even though that measure is not finite.

Now let \(\mathcal G\) be a group bundle, so \(r=s\). Formula (14.14) gives a central, nondegenerate map
\(C_0(X)\to ZM(C^*(\mathcal G))\). Its fibre at \(x\) is
\[
 C^*(\mathcal G)_x=
 C^*(\mathcal G)\big/C_0(X\setminus\{x\})C^*(\mathcal G)
       \cong C^*(\mathcal G_x^x).
 \tag{14.30}
\]
To prove this, apply (14.25) to \(U=X\setminus\{x\}\). Its ideal is exactly the displayed central ideal: a core function on \(\mathcal G|_U\) has compact range image inside \(U\), so a \(C_c(U)\) cutoff equal to one there multiplies it to itself. Conversely multiplying any core kernel by a \(C_c(U)\) function gives a kernel of that reduction. Density proves the ideal equality.

This is an upper semicontinuous field. Here is the relevant norm argument. If \(\|a_{x_0}\|<\varepsilon\), choose \(j\) in the fibre ideal with \(\|a+j\|<\varepsilon\). Approximate \(j\) by finite sums \(\sum b_i a_i\) with \(b_i(x_0)=0\). Their fibre norms are bounded by \(\sum|b_i(x)|\|a_i\|\), small near \(x_0\). Keeping a margin in the approximation gives \(\|a_x\|<\varepsilon\) on a neighborhood. Nondegeneracy of the \(C_0(X)\)-action similarly makes the fibre norms vanish at infinity. Continuity of all these norm functions is an extra assertion, not part of the Haar-system definition.

The reduced algebra also has a central \(C_0(X)\)-action, but its intrinsic quotient fibre need not equal \(C_r^*(\mathcal G_x^x)\): that equality requires exactness of the corresponding reduced restriction sequence. For a product bundle \(X\times H\), the trivial-action case of Theorem 14.3 instead gives the explicit continuous fields
\[
 C^*(X\times H)\cong C_0(X)\otimes C^*(H),\qquad
 C_r^*(X\times H)\cong C_0(X)\otimes C_r^*(H).
 \tag{14.31}
\]
The tensor norm is unambiguous because the \(C_0(X)\) factor is commutative, as proved in Lesson 8.

## Amenability and the foliation preview

For Hausdorff arrows, topological amenability can be defined by a net of probability measures \(m_i^x\) on \(\mathcal G^x\), continuous on compact test functions, such that
\[
 \|\gamma_*m_i^{s(\gamma)}-m_i^{r(\gamma)}\|_{\mathrm{TV}}
             \longrightarrow0
 \tag{14.32}
\]
uniformly for \(\gamma\) in compact sets. This is [Anantharaman-Delaroche 2023, Definition 3.3, p. 8]. We will use it to compare every integrated representation with regular source-fibre representations. The converse to the resulting full–reduced equality is false for groupoids; the counterexamples are discussed after the norm comparison.

### Smoothing the probability measures

We first prepare a Haar density. There is a continuous nonnegative function \(q\) on \(\mathcal G\) such that
\[
 \int q(\eta)\,d\lambda^x(\eta)=1\qquad(x\in X).
 \tag{14B.1}
\]
Its support over each compact range-coordinate set can be chosen compact. To construct it, for every unit choose \(h\in C_c(\mathcal G)^+\) whose Haar integral is positive there. Full support supplies such a bump, and Haar continuity keeps its integral positive on a neighborhood. Take a countable locally finite refinement of these neighborhoods and a subordinate partition of unity \(\theta_j\), with each support compact and contained in the relevant positivity set. If \(h_j\) is the corresponding bump, put
\[
 q(\eta)=\sum_j
  \frac{\theta_j(r(\eta))h_j(\eta)}{\lambda(h_j)(r(\eta))}.
 \tag{14B.2}
\]
Each summand extends continuously by zero across the complement of its positivity set. The sum is locally finite, has the stated support property, and integrates to \(\sum_j\theta_j(x)=1\). We are using Hausdorff arrows here, so these are ordinary continuous functions.

Let \(m_i^x\) be the probabilities in (14.32); they need not initially have Haar densities. Replace them by their convolution with \(q\). The new density on the range fibre is
\[
 p_i(\zeta)=\int_{\mathcal G^{r(\zeta)}}
                  q(\gamma^{-1}\zeta)\,dm_i^{r(\zeta)}(\gamma).
 \tag{14B.3}
\]
This is a nonnegative Borel function. Here are the measurability details needed below. Continuity of the compact test integrals for \(m_i\) implies that \(x\mapsto m_i^x(B)\) is Borel for every Borel \(B\subseteq\mathcal G\): exhaust an open set by a countable family of nonnegative compact bumps, and then use the monotone-class theorem. On the closed relation \(r(\gamma)=r(\zeta)\), integration of a nonnegative Borel function of \((\zeta,\gamma)\) against this kernel is Borel as well. First check indicator rectangles, then bounded simple functions, and finally increasing limits. This applies to the integrand in (14B.3).

Left Haar invariance and Tonelli give \(\int p_i\,d\lambda^x=1\) for every \(x\). Any infinite values occupy a Haar-null set in each fibre; replace them by zero. In measure notation the smoothing sends \(\delta_\gamma\) to the probability \(\gamma_*(q\lambda^{s(\gamma)})\). It therefore contracts the total variation of signed measures. It also commutes with left multiplication. Consequently
\[
 \int_{\mathcal G^{r(\sigma)}}
       |p_i(\sigma^{-1}\zeta)-p_i(\zeta)|\,d\lambda^{r(\sigma)}(\zeta)
 \leq
 \|\sigma_*m_i^{s(\sigma)}-m_i^{r(\sigma)}\|_{\mathrm{TV}}.
 \tag{14B.4}
\]
Changing null-set representatives does not alter this inequality. It follows directly either by the contraction just described or by applying the definition of total variation to every bounded Borel test function of absolute value at most one. We do not need \(p_i\) to be continuous: Borel densities suffice for a measured representation.

### Compressing a regular representation

**Theorem 14.7.** If \(\mathcal G\) has Hausdorff arrows and satisfies (14.32), its full and reduced norms agree.

**Proof.** By disintegration, it suffices to bound the integrated form \(L\) of any measurable unitary representation \((\mu,H_x,V_\gamma)\). Let \(\nu=\mu\lambda\), and write \(D=d\nu/d\nu^{-1}\) for its positive modular cocycle, as in (14.13). Inner products keep the second-linear convention fixed above.

Consider
\[
 \mathscr K=L^2(\mathcal G,\nu;s^*H),\qquad
 (W_i\xi)(\gamma)=p_i(\gamma)^{1/2}V_\gamma^{-1}\xi(r(\gamma)).
 \tag{14B.5}
\]
Measurability follows from the Borel bundle and (14B.3). The fibre mass identity makes \(W_i\) an isometry from \(L^2(X,\mu;H)\) into \(\mathscr K\). Define on the latter space
\[
 (\mathscr R(f)\eta)(\gamma)=
  \int_{\mathcal G^{r(\gamma)}}
        f(\sigma)D(\sigma)^{-1/2}\eta(\sigma^{-1}\gamma)
                             \,d\lambda^{r(\gamma)}(\sigma).
 \tag{14B.6}
\]
The vectors in the integrand lie in \(H_{s(\gamma)}\). This operator has norm at most \(\|f\|_r\), not merely an \(I\)-norm bound. Indeed multiplication by \(D(\gamma)^{1/2}\) is a unitary from \(\mathscr K\) to \(L^2(\mathcal G,\nu^{-1};s^*H)\), since \(d\nu^{-1}=D^{-1}d\nu\). Conjugating (14B.6) by it cancels all modular factors:
\[
 D(\gamma)^{1/2}D(\sigma)^{-1/2}
                    D(\sigma^{-1}\gamma)^{-1/2}=1.
 \tag{14B.7}
\]
The resulting operator is ordinary left convolution. As \(\nu^{-1}=\int\lambda_x\,d\mu(x)\), this is the direct integral of the regular source-fibre operators \(L_x(f)\otimes 1_{H_x}\). Proposition 14.2 bounds every one by \(\|f\|_r\). This also constructs the bounded operator (14B.6) rigorously from its formula on integrable test sections.

For \(f\in C_c(\mathcal G)\), put
\[
 \varepsilon_i(f)=\sup_{\sigma\in\operatorname{supp}f}
       \|\sigma_*m_i^{s(\sigma)}-m_i^{r(\sigma)}\|_{\mathrm{TV}}.
 \tag{14B.8}
\]
This tends to zero. The unitary multiplication rule gives
\(V_{\sigma^{-1}\gamma}^{-1}=V_\gamma^{-1}V_\sigma\). Thus the difference \(\mathscr R(f)W_i\xi-W_iL(f)\xi\), evaluated at \(\gamma\), is
\[
 V_\gamma^{-1}\int f(\sigma)D(\sigma)^{-1/2}
       \big(p_i(\sigma^{-1}\gamma)^{1/2}-p_i(\gamma)^{1/2}\big)
       V_\sigma\xi(s(\sigma))\,d\lambda^{r(\gamma)}(\sigma).
 \tag{14B.9}
\]
Apply weighted Cauchy–Schwarz with weight \(|f(\sigma)|\). The first factor is bounded by \(R(f)\). After integrating the second factor over \(\gamma\) and using Tonelli, the elementary inequality \(|\sqrt a-\sqrt b|^2\leq|a-b|\), together with (14B.4), gives
\[
 \begin{aligned}
 \|\mathscr R(f)W_i\xi-W_iL(f)\xi\|^2
 &\leq R(f)\varepsilon_i(f)
       \int_{\mathcal G}|f(\sigma)|D(\sigma)^{-1}
                     \|\xi(s(\sigma))\|^2\,d\nu(\sigma)\\
 &=R(f)\varepsilon_i(f)
       \int_X\|\xi(x)\|^2
                 \int_{\mathcal G_x}|f(\sigma)|\,d\lambda_x(\sigma)
                                                  \,d\mu(x)\\
 &\leq R(f)S(f)\varepsilon_i(f)\|\xi\|^2.
 \end{aligned}
 \tag{14B.10}
\]
The equality uses \(D^{-1}\nu=\nu^{-1}\), and so includes the modular measure change explicitly. The argument initially applies to bounded measurable sections with suitable finite-measure support; those are dense, and the resulting bound extends to every \(\xi\).

Since \(W_i\) is isometric, (14B.10) implies
\[
 \|L(f)\|\leq\|\mathscr R(f)\|
             +\|f\|_I\sqrt{\varepsilon_i(f)}.
 \tag{14B.11}
\]
Pass to the limit to obtain \(\|L(f)\|\leq\|f\|_r\). Taking the supremum over the disintegrated representations gives \(\|f\|\leq\|f\|_r\); the reverse inequality was already part of the construction of the full norm. Completion proves the theorem. ∎

The theorem is the scalar full–reduced comparison of Renault's amenability theory. [Sims–Williams, §2 and Theorem 1, pp. 4–5] proves the more general Fell-bundle statement through measurewise amenability. The argument here proves the required scalar case directly from (14.32). The common ingredients with the group proof in Lesson 4 are a probability square root, absorption into a regular representation, and a quantitative compression bound; the Haar smoothing above accommodates initially singular probabilities.

### Proper groupoids

A second countable proper Hausdorff groupoid with a Haar system is amenable. We construct a continuous cutoff \(c:X\to[0,\infty)\) with
\[
 \begin{gathered}
 \int_{\mathcal G^x}c(s(\eta))\,d\lambda^x(\eta)=1,\\
 \operatorname{supp}c\cap s(r^{-1}(K))\text{ is compact}\\
 \text{for every compact }K\subset X.
 \end{gathered}
 \tag{14.33}
\]

**Lemma (cutoffs for proper groupoids).** A second countable locally compact Hausdorff proper groupoid with a Haar system has a continuous function \(c:X\to[0,\infty)\) satisfying (14.33).

**Proof.** The orbit map \(q:X\to Y=X/\mathcal G\) is open, and \(Y\) is locally compact Hausdorff, by the proper-orbit argument of Lesson 13. It is second countable: images under an open surjection of a countable basis form a countable basis. We first construct \(b\geq0\), continuous on \(X\), positive somewhere on each orbit, such that
\[
\operatorname{supp}b\cap q^{-1}(L)\text{ is compact for every compact }L\subset Y.
\tag{14A.1}
\]

Take a locally finite cover of \(Y\) by relatively compact open sets \(V_j\), and a partition of unity \((\rho_j)\) with \(\operatorname{supp}\rho_j\subset V_j\). For each \(y\in\overline V_j\), choose a lift \(x\) and a nonnegative compactly supported bump positive at \(x\). The open image of its positive set is a neighborhood of \(y\). Compactness of \(\overline V_j\) permits finitely many such bumps; their sum \(b_j\in C_c(X)\) is positive somewhere on every orbit over \(\overline V_j\). Put
\[
b(x)=\sum_j\rho_j(q(x))b_j(x).
\tag{14A.2}
\]
The sum is locally finite, hence continuous. For each \(y\), some \(\rho_j(y)>0\), and the corresponding \(b_j\) is positive on that orbit, so \(b\) is positive there. A compact \(L\) meets only finitely many of the supports of the partition. Its inverse image meets \(\operatorname{supp}b\) inside the finite union of the corresponding compact supports of \(b_j\). This intersection is closed in that compact union, proving (14A.1).

Define
\[
a(x)=\int_{\mathcal G^x}b(s(\eta))\,d\lambda^x(\eta).
\tag{14A.3}
\]
The function is finite and continuous. To check this without treating \(b\circ s\) as globally compactly supported, choose \(\chi\in C_c(X)\) equal to one near a fixed \(x_0\), and write \(K=\operatorname{supp}\chi\). In \(r^{-1}(K)\), an arrow at which \(b\circ s\) is nonzero has source in the compact set
\(C=\operatorname{supp}b\cap q^{-1}(q(K))\), by (14A.1). Properness of \((r,s)\) makes \((r,s)^{-1}(K\times C)\) compact. Thus \(\eta\mapsto\chi(r(\eta))b(s(\eta))\) is a compactly supported continuous function on the Hausdorff arrow space. Haar continuity makes its integral continuous, and that integral is \(a\) near \(x_0\). This proves both finiteness and continuity locally everywhere.

Each orbit contains a point where \(b>0\); an arrow from that point to \(x\), and full support of the range Haar measure, give \(a(x)>0\). Left invariance gives \(a(r(\gamma))=a(s(\gamma))\), since left multiplication leaves the source of the integration arrow unchanged. Consequently
\[
c(x)=b(x)/a(x)
\tag{14A.4}
\]
is continuous, has the same support as \(b\), and has range-fibre integral one as in (14.33). Finally
\(s(r^{-1}(K))=q^{-1}(q(K))\): these are exactly the units in orbits meeting \(K\). Equation (14A.1) proves the required support condition for \(c\). ∎

The cutoff theorem is also recorded by Tu, *The Baum–Connes Conjecture for Groupoids*, §1.7. Its construction here makes the compactness of the normalized fibre integrals explicit.

Using this cutoff, set \(m^x=c(s(\eta))\,d\lambda^x(\eta)\). This is a probability measure; its compact test integrals are continuous by the Haar axiom. Left multiplication preserves it exactly because source does not change and the Haar measures are left invariant. The constant family \(m_i=m\) satisfies (14.32). Theorem 14.7 therefore gives full–reduced equality for proper Hausdorff groupoids. Both the cutoff and the norm comparison have been constructed above.

### A group bundle that separates the three properties

We now construct the counterexample promised after (14.27). It has equal full and reduced algebras, is not amenable, and has a nonexact reduced restriction sequence. The construction is the free-group instance of the Higson–Lafforgue–Skandalis group bundles, with the norm comparison used by [Willett 2015]. We include the finite-quotient norm argument rather than assume a finite-dimensional approximation theorem.

#### Finite quotients detect the full free-group norm

Let \(\Gamma=F(a,b)\). For every \(z\in\mathbb C[\Gamma]\),
\[
 \|z\|_{C^*(\Gamma)}
       =\sup_{\Gamma\twoheadrightarrow Q\text{ finite}}
                       \|z_Q\|_{C_r^*(Q)}.
 \tag{14C.1}
\]
Here \(z_Q\) is the image of the group-ring element. The easy inequality follows because every finite-quotient regular representation is a representation of \(\Gamma\). We prove the other inequality in two steps.

First finite-dimensional representations detect the full norm. Let \(U_a,U_b\) be unitaries in any representation, let \(\xi\) be a unit vector, and suppose every word in \(z\) has length at most \(L\geq1\). Put
\[
 E=\operatorname{span}\{U_w\xi:|w|\leq L-1\},\qquad
 H_L=\operatorname{span}\{U_w\xi:|w|\leq L\}.
 \tag{14C.2}
\]
For either generator \(g\), its original unitary maps
\(E+U_g^{-1}E\) isometrically onto \(U_gE+E\), both subspaces of \(H_L\). Their orthogonal complements in \(H_L\) have equal finite dimension. Extend this partial unitary to a unitary \(\widetilde U_g\) on \(H_L\). Both \(\widetilde U_g\) and its inverse agree with the original operators on \(E\). Freeness gives a representation with these two generators; successively applying the letters of a word of length at most \(L\) to \(\xi\) agrees with the original representation at every step. Hence
\(\widetilde U(z)\xi=U(z)\xi\). Choosing \(\xi\) close to the operator norm proves the assertion. This is the finite-word extension argument underlying residual finite-dimensionality of the full free-group algebra, historically associated with Choi.

Next approximate a finite-dimensional representation \(U\) by finite-image representations, allowing the approximating Hilbert space to grow. Suppose its dimension is \(d\). On the unit sphere \(S\subseteq\mathbb C^d\), let \(\rho\) be the unitary-invariant probability measure. One construction is to normalize a nonzero standard complex Gaussian vector; invariance follows from its radial density. Phase rotations and coordinate permutations then give
\[
 \int_S xx^*\,d\rho(x)=d^{-1}1.
 \tag{14C.3}
\]
Consequently \(v\mapsto\sqrt d\,\langle x,v\rangle\) is an isometric linear embedding into \(L^2(S,\rho)\), and composition with \(U_g^{-1}\) intertwines it with \(U_g\).

Partition the sphere into finitely many Borel sets \(A_j\) of diameter at most \(\delta\); discard zero-measure cells and choose \(x_j\in A_j\). For each generator set
\[
 m^g_{ij}=\rho(A_i\cap U_g^{-1}A_j),\qquad r_i=\rho(A_i).
 \tag{14C.4}
\]
Every matrix \(m^g\) has row sums and column sums \(r\). Replace these numbers by nonnegative rational numbers \(\widehat m^g_{ij},\widehat r_i\), arbitrarily close to them, satisfying the same common row and column equations and \(\sum_i\widehat r_i=1\). Keep every originally zero entry zero. Here no approximation theorem is hidden: the equations have rational coefficients and rational right-hand sides. On the coordinates that were positive the original solution lies in the relative interior of the positive orthant. Gaussian elimination supplies a rational particular solution and a rational basis for the homogeneous solution space; approximate its real coordinates by rationals closely enough to preserve positivity. This proves the asserted rational approximation.

Choose a common denominator \(N\). Take a finite set \(\Omega\), partitioned into sets \(\Omega_i\) of sizes \(N\widehat r_i\). For each generator choose a permutation \(P_g\) sending exactly \(N\widehat m^g_{ij}\) elements from \(\Omega_i\) to \(\Omega_j\). The row sums partition each source set, the column sums partition each target set, and arbitrary bijections between the equally sized pieces give the permutation. These two permutations define a representation \(T\) of the free group with finite image on \(L^2(\Omega,\text{uniform probability})\).

Define \(A_Nv(\omega)=\sqrt d\langle x_i,v\rangle\) for \(\omega\in\Omega_i\). Its Gram matrix is
\(A_N^*A_N=d\sum_i\widehat r_i x_ix_i^*\), which approaches the identity as \(\delta\to0\) and the rational approximation error tends to zero. Indeed \(\|xx^*-x_ix_i^*\|\leq2\delta\) on \(A_i\), and (14C.3) gives the integral to compare with.

If \(P_g\omega\in\Omega_j\) for \(\omega\in\Omega_i\), the corresponding matrix entry was positive originally. Some \(x\in A_i\) therefore has \(U_gx\in A_j\); hence \(\|U_gx_i-x_j\|\leq2\delta\). With \(T_gf=f\circ P_g^{-1}\), this gives
\[
 \|T_gA_N-A_NU_g\|\leq2\sqrt d\,\delta.
 \tag{14C.5}
\]
For sufficiently small errors, normalize to the isometry
\(W_N=A_N(A_N^*A_N)^{-1/2}\). Then
\(\|T_gW_N-W_NU_g\|\to0\), for both generators and their inverses. Telescoping along each of the finitely many words in \(z\) gives
\(\|T(z)W_N-W_NU(z)\|\to0\). Thus \(\|U(z)\|\leq\liminf\|T(z)\|\). Each \(T\) factors through a finite quotient, whose full and regular norms agree by the finite-group case of Lesson 4. Combining this with the first step proves (14C.1). This is the norm consequence of the finite-image density property for free groups studied by Lubotzky and Shalom; its required proof has been given here.

Enumerate the kernels of all homomorphisms of \(\Gamma\) into finite permutation groups and let \(N_k\) be the intersection of the first \(k\). These are finite-index normal subgroups, form a decreasing chain, and are cofinal among finite-index normal subgroups. Their intersection is trivial. For completeness, a nontrivial reduced word can be separated by a finite permutation action: trace its letters, in their order of application, along a path with distinct vertices \(0,\ldots,L\). Each generator specifies a partial permutation along its labelled edges. Reducedness prevents conflicting assignments at an internal vertex. Complete each partial bijection to a permutation of the vertices. The word carries vertex 0 to vertex \(L\), so is not the identity in this finite image. This proves residual finiteness and the intersection assertion directly.

Writing \(Q_k=\Gamma/N_k\), cofinality and (14C.1) imply
\[
 \|z\|_{C^*(\Gamma)}=\lim_k\|z_{Q_k}\|_{C_r^*(Q_k)}.
 \tag{14C.6}
\]
The norms are increasing: a later finite quotient surjects onto an earlier one, and the finite-group full norm equals its reduced norm.

#### The topology and the two norms

Let the unit space be \(X=\mathbb N\cup\{\infty\}\), its one-point compactification. Define a group bundle with fibres \(Q_k\) at \(k\) and \(\Gamma\) at \(\infty\). Every arrow in a finite fibre is isolated. A basic neighborhood of \((\infty,\gamma)\) is
\[
 T(\gamma,K)=\{(\infty,\gamma)\}\cup
                 \{(k,\gamma N_k):k\geq K\}.
 \tag{14C.7}
\]
Each such set is a compact open bisection, homeomorphic to the corresponding unit-space tail. Distinct infinite-fibre arrows have disjoint sufficiently short tails because \(\bigcap N_k=\{e\}\); finite arrows are separated by isolated neighborhoods. This proves Hausdorffness, local compactness, and second countability. Multiplication and inverse are continuous because the tail for \(\gamma\) times the tail for \(\eta\), on matching units, is the tail for \(\gamma\eta\); inverse replaces \(\gamma\) by \(\gamma^{-1}\). The groupoid is étale and has the counting Haar system of Proposition 13.2.

Let \(u_\gamma\) be the characteristic function of \(T(\gamma,1)\), with the indexing started at 1. These are unitaries in the convolution algebra and obey \(u_\gamma u_\eta=u_{\gamma\eta}\). The characteristic function of the compact open unit space is the identity. For a core function \(f\), write \(f_k\in\mathbb C[Q_k]\) and \(f_\infty\in\mathbb C[\Gamma]\) for its restrictions. The latter has finite support, since the infinite fibre is closed and discrete. The regular norm is exactly
\[
 \|f\|_r=\max\left\{\sup_k\|f_k\|_{C_r^*(Q_k)},
                         \|f_\infty\|_{C_r^*(\Gamma)}\right\}.
 \tag{14C.8}
\]

To calculate the full norm without presupposing reduced exactness, put
\(F=\sum_\gamma f_\infty(\gamma)u_\gamma\). Then \(g=f-F\) lies in the closure of the finite-fibre core, even in the \(I\)-norm. Indeed a compact support is covered by finitely many tail bisections and finitely many isolated arrows. On each tail the values of \(g\) tend to zero. For large \(k\) its support in that fibre has uniformly bounded cardinality, so \(\|g_k\|_{\ell^1(Q_k)}\to0\). Multiplication by finite unit cutoffs now approximates \(g\) in the \(I\)-norm.

The central unital copy of \(C(X)\) acts in every irreducible full representation as evaluation at a unit. If the unit is \(k\), that representation factors through the group algebra of \(Q_k\): the central projection of that unit is the identity in the representation. If the unit is \(\infty\), it kills every finite unit cutoff, and therefore kills \(g\). Its values on the unitaries \(u_\gamma\) form a representation of \(\Gamma\), so its norm on \(f\) is at most \(\|f_\infty\|_{C^*(\Gamma)}\). Taking the supremum over irreducible representations gives the upper bound in
\[
 \|f\|=\max\left\{\sup_k\|f_k\|_{C^*(Q_k)},
                              \|f_\infty\|_{C^*(\Gamma)}\right\}.
 \tag{14C.9}
\]
The reverse bound follows by composing restriction at a unit with any group representation; this is \(I\)-contractive because the fibre \(\ell^1\)-norm is bounded by \(\|f\|_I\). The central multiplier and irreducible norm facts used here are the ordinary C*-algebra facts already used in Lessons 1–3; this argument does not import a new groupoid disintegration theorem.

Now \(\|g_k\|\to0\), while (14C.6) says that
\(\|F_k\|\to\|f_\infty\|_{C^*(\Gamma)}\). Hence the finite-fibre supremum in (14C.8) already dominates the last term of (14C.9). Finite groups have equal full and reduced norms, and the infinite-fibre reduced norm is at most its full norm. The two displayed norms are equal on the core and therefore on its completion. This proves the **weak containment property** for this groupoid.

It is not topologically amenable. An amenability family restricted to the infinite unit would be a family of probability measures on \(\Gamma\), asymptotically invariant under every fixed \(\gamma\). That is the Reiter condition for amenability of the free group. Lessons 2 and 4 rule it out: the full norm of \(a+a^{-1}+b+b^{-1}\) is 4, while its regular norm is \(2\sqrt3\). This establishes the failure of the converse to Theorem 14.7.

#### A kernel element that survives at every finite fibre

Let \(U=\mathbb N\subset X\), and define
\[
 \begin{gathered}
 h=\tfrac14(u_a+u_a^*+u_b+u_b^*),\qquad
 c=\tfrac12(1+\sqrt3/2),\\
 \varphi(t)=\max\{0,(t-c)/(1-c)\}\quad(-1\leq t\leq1).
 \end{gathered}
 \tag{14C.10}
\]
The self-adjoint element \(h\) is a contraction. Put \(p=\varphi(h)\), a positive contraction obtained by continuous functional calculus; no spectral-gap assertion about the finite quotients is needed. At infinity the regular norm of \(h_\infty\) is \(\sqrt3/2<c\). Thus \(p_\infty=0\) in \(C_r^*(\Gamma)\).

In every finite fibre, the constant vector is an eigenvector of \(h_k\) with eigenvalue 1. Consequently \(p_k\) has eigenvalue \(\varphi(1)=1\) and \(\|p_k\|=1\). But the reduced open-restriction ideal is
\[
 C_r^*(\mathcal G|_U)=\bigoplus_k C^*(Q_k),
 \tag{14C.11}
\]
the norm-vanishing direct sum: the finite-fibre core has supremum block norm, and its completion is exactly that direct sum. Its elements have block norms tending to zero. We have proved
\[
 p\in\ker\big(C_r^*(\mathcal G)\to C_r^*(\Gamma)\big),
       \qquad p\notin C_r^*(\mathcal G|_U).
 \tag{14C.12}
\]
This is the strict inclusion in (14.27), with an explicit kernel element. It also explains the warning following (14.30): the intrinsic quotient fibre at infinity is the full free-group algebra, although the physical regular fibre is its reduced algebra. Equality of the global full and reduced completions does not identify those two different fibre constructions.

The group-bundle construction and these failures are discussed in [Anantharaman-Delaroche 2023, §§5.4 and 6] and [Sims 2017, pp. 35–36]. Willett's example uses finite-quotient detection of the full norm to obtain weak containment without amenability. The argument above supplies that detection, the topology, both norm calculations, and the reduced kernel witness in one model.

### The foliation preview

For the Kronecker flow of irrational slope \(\theta\),
\[
 t\cdot(x,y)=(x+t,y+\theta t)\pmod{\mathbb Z^2},
 \tag{14.34}
\]
the flow groupoid has algebra \(C(\mathbb T^2)\rtimes\mathbb R\), with equal full and reduced norms by Lesson 4. The Thom calculation of Lesson 11 gives \(K_0\cong K_1\cong\mathbb Z^2\). Lesson 16 identifies the holonomy groupoid with this flow groupoid and proves the equivalence with a transversal rotation groupoid. The algebra construction here does not by itself prove that geometric identification.

## Exercises with solutions

**Exercise 1 (basic).** Prove the pair-groupoid compact-operator identification when \(\mu(X)<\infty\), including a finite set with unequal positive weights. State the necessary topological and support assumptions.

**Solution.** Assume \(X\) is nonempty second countable locally compact Hausdorff and \(\mu\) is a full-support positive Radon measure. A finite abstract measure space alone does not specify the topological groupoid or its compact continuous kernels. For product kernels, convolution gives
\[
 f_{\xi,\eta}*f_{\zeta,\omega}
       =\langle\eta,\zeta\rangle f_{\xi,\omega},\qquad
 f_{\xi,\eta}^*=f_{\eta,\xi}.
 \tag{14.35}
\]
Compact product approximations are dense in \(I\)-norm, with error at most \(\mu(X)\) times the uniform error. Each finite collection lies in a finite matrix corner after orthonormalizing its \(C_c(X)\) vectors. The matrix norm is the full norm, realized by the source-fibre representation. Completion is therefore \(\mathcal K(L^2(X,\mu))\). On a finite set the orthonormal vectors are \(\delta_i/\sqrt{w_i}\), giving precisely (14.29). Proposition 14.6 also shows that finite total mass is unnecessary: use the two compact projection measures for each approximation.

**Exercise 2 (intermediate).** Establish the transformation-groupoid identifications and determine the density factor when \(H\) is not unimodular.

**Solution.** Groupoid convolution is the first formula in (14.18); groupoid adjoint is its second formula. Multiplication by \(\Delta(t)^{-1/2}\) preserves the product because the two factors at \(a,a^{-1}t\) multiply to that at \(t\). Its crossed-product adjoint has coefficient \(\Delta(t)^{-1}\Delta(t^{-1})^{-1/2}=\Delta(t)^{-1/2}\). Thus (14.16), not the unweighted core map, is the required *-isomorphism.

For the full norm, a covariant pair integrates this core to an inductive-limit continuous representation, which is \(I\)-contractive by disintegration. Conversely construct \(P\) by (14.14) and the strongly continuous \(U_a\) by (14.19); the core inner-product identity gives unitarity and covariance, and convolution on core vectors verifies the integrated form. Supremum norms agree. For the reduced norm, the source-fibre measure is \(\Delta(t)^{-1}dt\); multiplying vectors by \(\Delta(t)^{-1/2}\) gives (14.21). Direct sum over all evaluations of \(C_0(X)\) is faithful, and Lesson 2 then gives exactly the reduced crossed-product norm. Both isomorphisms follow on completion.

**Exercise 3 (intermediate).** Prove faithfulness of the étale reduced expectation. Explain why full-algebra faithfulness, or non-Hausdorff arrows, needs a separate argument.

**Solution.** In the Hausdorff étale case restriction is \(C_0(X)\)-valued and is a contractive completely positive map by unit-vector compressions. If \(a\geq0\) has zero expectation, (14.24) makes every diagonal entry of every positive \(L_x(a)\) zero. Taking square roots shows that every basis vector is annihilated; hence every \(L_x(a)\) is zero and the reduced norm of \(a\) is zero.

On the full algebra those same regular representations only detect its reduced quotient. If (14.12) has a nonzero kernel, any nonzero positive element in that kernel has zero composed expectation, so it is not faithful. For non-Hausdorff arrows the doubled-origin function \((0,1,-1)\) already has discontinuous restriction to units. The codomain in (14.22) fails even on the core.

**Exercise 4 (advanced).** Using disintegration, prove full exactness for an open invariant \(U\). Locate the step which is unavailable for the reduced sequence.

**Solution.** Extend a disintegrated representation of \(\mathcal G|_U\) by zero measure and zero Hilbert fibres outside \(U\). Invariance prevents arrows between the two parts, and the integrated-form bound gives an \(I\)-contractive representation of the whole groupoid. This proves that the ideal-core inclusion is isometric for full norms. Restriction to the closed complement is \(I\)-contractive and onto the core by compact patch extension, hence gives a full surjection.

If a representation of the full algebra kills that ideal, every \(b\in C_c(U)\) has \(M(b)L(f)=L((b\circ r)f)=0\) for every core \(f\). Nondegeneracy gives \(M(b)=0\). A countable cover by such bumps, in the disintegrated Hilbert bundle, forces its fibres over \(U\) to be zero almost everywhere. Restricting the remaining representation to \(F\) factors it through the full closed-reduction algebra. Supremum over quotient representations now identifies the quotient with \(C^*(\mathcal G|_F)\), proving (14.25). The last supremum uses every full representation supported on \(F\); those representations are not automatically bounded by the closed reduction's reduced norm. This is exactly where a reduced exactness argument would need another hypothesis.

**Exercise 5 (advanced).** Regard \(\mathbb Z\) as a one-unit étale groupoid. Identify the sandwich sets of \(J=\{f\in C(\mathbb T):f(1)=0\}\), and explain why inner exactness does not by itself make all ideals dynamical.

**Solution.** The algebra is \(C_r^*(\mathbb Z)=C(\mathbb T)\), by the Fourier and amenability results of Lessons 4–6. Its diagonal is the constant functions. The proper ideal \(J\) has zero intersection with them, so \(U_J=\varnothing\). Its element \(2-u-u^*\), where \(u(z)=z\), has expectation two, so \(V_J\) is the whole singleton unit space. Multiplying this element by every group unitary gives a nonzero coefficient at every integer; the residual support is all of \(\mathbb Z\). The triple is \((\varnothing,\{\ast\},J)\). Inner exactness is automatic because the only invariant unit sets are empty and full. Effectiveness fails, and \(J\) is neither of their two dynamical ideals. ∎

## Proofs and prerequisites

- Theorems 14I.1–14I.4 prove effective diagonal uniqueness, the Cartan criterion, dynamical ideal correspondence and simplicity, and the full residual ideal sandwich. Their reduced Hausdorff étale proofs require no second countability; the full amenable converse uses the standing countability hypotheses.
- Renault's disintegration theorem is proved in its separable dense-domain and locally Hausdorff form. The proof constructs local convolution units, extends the tensor vectors to Borel test functions, proves quasi-invariance, corrects the scalar modular cocycle on every product, and constructs the Borel Hilbert field and exact unitary action. It also proves the integrated bound used in the full transformation-groupoid identification, full exactness, and amenable norm comparison. Muhly–Williams 2008, Theorem 7.8 and Appendix B, remains the credited statement and proof source.
- Haar smoothing and the square-root compression prove the amenable Hausdorff full–reduced comparison in Theorem 14.7, using the measured representations supplied by disintegration. Proper-groupoid cutoff existence and its amenability consequence are also proved here. Sims–Williams and Tu remain credited sources for these results and their broader context.
- The finite-quotient group bundle proves that weak containment does not imply amenability, and its explicit functional-calculus element proves reduced restriction can fail to be exact. The required finite-image approximation of free-group representations is proved in the same section. HLS, Willett, Choi, and Lubotzky–Shalom remain credited for the construction and its representation-theoretic ingredients.
- The Kronecker holonomy identification and transversal equivalence are proved in Lesson 16. The K-groups used in its preview are the calculation already given in Lesson 11.
- Compact-support extension, Stone–Weierstrass approximation, Radon-measure \(L^2\)-density, and the Hilbert-module and C*-algebra foundations used above are general prerequisites. The patch convolution proof itself is included, rather than assumed from the Hausdorff case.

## References

- Yuezhao Li, [*Groupoid C*-algebras*](https://ncg-leiden.github.io/groupoid2022/groupoid_notes.pdf), revised 2024, §2 and §8.5.2.
- Paul S. Muhly and Dana P. Williams, [*Renault's Equivalence Theorem for Groupoid Crossed Products*](https://nyjm.albany.edu/m/2008/3p.pdf), *New York Journal of Mathematics Monographs* **3** (2008), Proposition 4.4 and Theorem 7.8.
- Aidan Sims, [*Hausdorff étale groupoids and their C*-algebras*](https://aidansims.com/papers/Sims2017.pdf), 2017, §§3.3 and 4.3. Revised author manuscript: [2018 version](https://arxiv.org/abs/1710.10897v2).
- Aidan Sims and Dana P. Williams, [*Amenability for Fell Bundles over Groupoids*](https://aidansims.com/papers/SWi2012.pdf), 2012 preprint, §2 and Theorem 1; the page locators refer to this preprint.
- Jean-Louis Tu, [*The Baum–Connes Conjecture for Groupoids*](https://ncatlab.org/nlab/files/JLTBaumConnesForGroupoids.pdf), 1999 preprint, §1.7.
- Claire Anantharaman-Delaroche, [*Amenability, exactness and weak containment property for groupoids*](https://arxiv.org/pdf/2306.17613), 2023, §§3, 5.4 and 6.
- Alain Connes, [*Noncommutative Geometry*](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf), 1994, Chapter II, §§5 and 8; the smooth half-density convention is explained in Lesson 13.

- Rufus Willett, [*A non-amenable groupoid whose maximal and reduced C*-algebras are the same*](https://www.uni-muenster.de/FB10/mjm/vol_8/mjm_vol_8_11.pdf), *Münster Journal of Mathematics* **8** (2015), 241–252, especially Lemmas 2.6–2.8 and Remark 3.1.
- Man-Duen Choi, [*The full C*-algebra of the free group on two generators*](https://doi.org/10.2140/pjm.1980.87.41), *Pacific Journal of Mathematics* **87** (1980), 41–48. Attribution for finite-dimensional detection; the finite-word extension proof above supplies the required fact.
- Alexander Lubotzky and Yehuda Shalom, [*Finite representations in the unitary dual and Ramanujan groups*](https://doi.org/10.1090/conm/347/06272), *Contemporary Mathematics* **347** (2004), 173–189. Attribution for finite-image density; the needed free-group norm consequence is proved above.

- K. A. Brix, T. M. Carlsen and A. Sims, [*Some results regarding the ideal structure of C*-algebras of étale groupoids*](https://arxiv.org/abs/2211.06126v2), revised 2024.
