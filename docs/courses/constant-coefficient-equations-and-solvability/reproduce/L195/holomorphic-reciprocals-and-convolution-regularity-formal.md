# Holomorphic reciprocals and convolution regularity

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Original exposition: CC0.*

A convolution equation can be inverted microlocally when its Fourier transform has a holomorphic reciprocal with polynomial growth on a complex cone at infinity. The Fourier transform of the kernel may itself be a distribution. The reciprocal identity below is consequently an identity of distributions on the real cone; no pointwise reciprocal of a globally defined function is assumed.

The analytic sequence criterion and localization rules are the available proofs in [Pulling back and combining analytic singularities][P], Section 2. The mixed derivative cutoff bounds are Lemma 1.1 of [Analytic directions of holomorphic boundary values][A]. [Schwartz functions and Fourier inversion][F], Sections F1-F5, supplies the Fourier seminorms, inversion and distributional transpose. The local holomorphic coefficient bounds are the Cauchy estimates in [Cauchy bounds and root counts][C]. [Proper convolution and compact support][U] supplies the tensor pairing and proper support integral. We prove the required microlocal multiplier estimate here rather than assume an analytic pseudodifferential calculus.

## 1. Cutoff estimates with a growing derivative

Fix relatively compact neighborhoods \(U_0\Subset U_1\). The controlled cutoff construction supplies \(\chi_J\in C_c^\infty(U_1)\), equal to one near \(\overline U_0\), whose fixed-order derivative seminorms are bounded independently of \(J\). For each fixed multi-index \(\beta\),
\[
 |D^{\alpha+\beta}\chi_J|
       \le C_\beta^{|\alpha|+1}J^{|\alpha|},
 \qquad |\alpha|\le J.
 \tag{CE1}
\]
All cutoffs have support in the same compact set. Constants may change after the neighborhoods are fixed. They never depend on \(J\) or the growing index.

For every fixed \(\beta\), compact support and integration by parts give
\[
 |\partial_\zeta^\beta\widehat{\partial^\alpha\chi_J}(\zeta)|
 \le C_\beta^{|\alpha|+s+1}J^{|\alpha|+s}
             (1+|\zeta|)^{-s},
 \qquad |\alpha|+s+c_\beta\le J.
 \tag{CE2}
\]
Here \(c_\beta\) is a fixed integer. To check the index, differentiation in \(\zeta\) inserts \(x^\beta\); multiplication by a monomial \(\zeta^\gamma\), \(|\gamma|\le s\), differentiates \(x^\beta\partial^\alpha\chi_J\) at most \(s\) times. The finite product rule uses cutoff derivatives through \(|\alpha|+s\), with only a fixed additional order if a low derivative is kept separate. For \(|\zeta|\ge1\), choose a coordinate with \(|\zeta_j|\ge|\zeta|/\sqrt n\) and integrate by parts \(s\) times in it. On \(|\zeta|\le1\), use the compact \(L^1\) bound. Powers and the finitely many product coefficients are absorbed into the exponential constant in (CE2). This proves the estimate without a second growing factorial.

**Lemma 1.1.** Suppose \(f_K\) have common compact support and distributional order, and for an open real cone \(\Omega\),
\[
 |\widehat f_K(\eta)|\le B(1+|\eta|)^q,\qquad
 |\widehat f_K(\eta)|\le A^{K+1}K^K(1+|\eta|)^{-K}
       \quad(\eta\in\Omega).
 \tag{CE3}
\]
On a fixed smaller cone \(\Omega_0\), for \(J=4K\), \(|\alpha|<K\), and sufficiently large \(K\),
\[
 \left|\widehat{(\partial^\alpha\chi_J)f_K}(\xi)\right|
  \le C^{K+|\alpha|+1}K^{K+|\alpha|+c}
                   (1+|\xi|)^{-K}.
 \tag{CE4}
\]
The fixed integer \(c\) depends on the common polynomial order and dimension.

**Proof.** Use the Fourier convolution formula. In the region
\(|\eta-\xi|\le d|\xi|\), choose \(d>0\) so small that \(\eta\in\Omega\) and \(1+|\eta|\) is comparable to \(1+|\xi|\). The analytic bound in (CE3) applies. The \(L^1\) norm of the cutoff transform in (CE2), with a fixed exponent larger than \(n\), is at most \(C^{|\alpha|+1}K^{|\alpha|+c}\). This proves the contribution claimed in (CE4).

In the remaining region, \(|\xi-\eta|\) is bounded below by a fixed positive multiple of both \(|\xi|\) and \(|\eta|\), with an inessential adjustment for bounded frequencies. More precisely their sum is at most a fixed multiple of \(|\xi-\eta|\), since \(|\xi-\eta|>d|\xi|\) and \(|\eta|\le|\xi-\eta|+|\xi|\). Use the global polynomial bound in (CE3) and (CE2) with \(s=K+q+n+1\). The integral is bounded by a constant to the \(K+|\alpha|+1\) power times
\(K^{K+|\alpha|+q+n+1}(1+|\xi|)^{-K}\).
All derivative orders are below \(2K+q+n+1\), hence below \(4K\) for sufficiently large \(K\). A fixed shift handles the finitely many smaller \(K\). This proves the lemma. \(\square\)

## 2. An analytic symbol is microlocally local

Let \(a\in C^\infty(\mathbb R^n)\) satisfy the symbol estimates
\[
 |\partial^\beta a(\eta)|
       \le C_\beta(1+|\eta|)^{m-|\beta|}
       \quad\hbox{for every fixed }\beta,
 \tag{CE5}
\]
where \(m\ge0\) is an integer. Assume that for \(\xi\) in an open cone \(\Gamma\), at sufficiently large radius, \(a\) extends holomorphically to balls of radius \(d|\xi|\) and is bounded there by \(C(1+|\xi|)^m\), with one \(d>0\). The Cauchy formula on smaller polydisks gives
\[
 \frac{|\partial^\alpha a(\xi)|}{\alpha!}
       \le C^{|\alpha|+1}|\xi|^{m-|\alpha|}.
 \tag{CE6}
\]
The smooth extension elsewhere has no analyticity requirement.

Define \(T_af=\mathcal F^{-1}(a\widehat f)\) on tempered distributions. Estimates (CE5) make multiplication by \(a\) a continuous map on Schwartz tests, so this definition is meaningful.

**Theorem 2.1.** For every \(f\in\mathcal S'\),
\[
 \operatorname{WF}_A(T_af)\cap(\mathbb R^n\times\Gamma)
       \subset\operatorname{WF}_A(f).
 \tag{CE7}
\]
Only directions with the stipulated uniform holomorphic neighborhoods are included.

**Proof.** Fix \((x_0,\xi_0)\notin\operatorname{WF}_A(f)\) with \(\xi_0\in\Gamma\). Take a smaller cone about \(\xi_0\) whose closure stays in both the analytic absence cone and the symbol's holomorphic cone. Choose neighborhoods \(U_0\Subset U_1\) on which a bounded analytic witness sequence \(f_K\) equals \(f\). The witnesses satisfy (CE3) on a larger cone than the one of output directions. Choose the cutoff supports inside \(U_1\).

There are fixed \(M,q_1\) such that the tempered transform of \(f\) satisfies
\[
 |\widehat f(\psi)|
   \le C\max_{|\beta|\le M}\sup_\eta
                    (1+|\eta|)^{q_1}|\partial^\beta\psi(\eta)|.
 \tag{CE8}
\]
Choose a fixed large integer \(B>m+q_1\), also exceeding all the fixed derivative-order losses in (CE2)–(CE4) and the estimates below, and put
\[
 K=N+B,\qquad J=4K,\qquad v_N=\chi_JT_af.
 \tag{CE9}
\]
All those losses depend only on \(m,M,q,q_1,n\) and the fixed cutoff family, not on \(B\) or \(N\), so this is one finite choice. These \(v_N\) have common compact support, common finite distributional order and equal \(T_af\) near \(x_0\). The uniform low derivative bounds on the cutoffs justify that assertion. We will prove their analytic Fourier estimate.

First consider \(|\xi|\ge K\) in the smaller output cone. Set
\[
 P_\xi(\eta)=
       \sum_{|\alpha|<K}
          \frac{\partial^\alpha a(\xi)}{\alpha!}(\eta-\xi)^\alpha,
 \qquad R_\xi(\eta)=a(\eta)-P_\xi(\eta).
 \tag{CE10}
\]
The Fourier pairing for \(v_N\) is
\[
 \widehat v_N(\xi)
   =(2\pi)^{-n}\widehat f_\eta
          \bigl(a(\eta)\widehat\chi_J(\xi-\eta)\bigr).
 \tag{CE11}
\]
All tests here are Schwartz functions, since \(a\) has polynomial symbol bounds.

**The polynomial part.** Each Taylor monomial has the exact pairing identity
\[
 (2\pi)^{-n}\widehat f_\eta
       \bigl((\eta-\xi)^\alpha\widehat\chi_J(\xi-\eta)\bigr)
       =i^{|\alpha|}\widehat{(\partial^\alpha\chi_J)f}(\xi).
 \tag{CE12}
\]
This follows from \(\widehat{\partial^\alpha\chi_J}(\xi-\eta)
=i^{|\alpha|}(\xi-\eta)^\alpha\widehat\chi_J(\xi-\eta)\) and the Fourier convolution formula. The factor \(i^{|\alpha|}\) on the right of (CE12) includes the sign from \(\eta-\xi\).

The local product in (CE12) equals the one with \(f_K\). Equations (CE4) and (CE6) therefore bound the sum by
\[
 C^{K+1}K^{K+c}|\xi|^{m-K}
       \sum_{|\alpha|<K}
                 C^{|\alpha|}(K/|\xi|)^{|\alpha|}
 \le C_1^{K+1}K^{K+c}|\xi|^{m-K}.
 \tag{CE13}
\]
For the last bound, \(K/|\xi|\le1\), the number of multi-indices of each degree is polynomial in \(K\), and a fixed polynomial is absorbed into \(C_1^{K+1}\). No factorial remains from the Taylor coefficients.

**The remainder near the diagonal.** Choose a smooth cutoff in \(h/|\xi|\), where \(h=\eta-\xi\), supported on \(|h|\le2d_0|\xi|\) and one on \(|h|\le d_0|\xi|\). Here \(d_0\) is fixed small enough that the entire larger ball lies in a uniform holomorphic neighborhood and inside its smaller Cauchy radius. The Taylor series and (CE6), differentiated only through the fixed order \(M\), give
\[
 |\partial_\eta^\beta R_\xi(\eta)|
       \le C^{K+1}K^M|\xi|^{m-K}
                         |h|^{K-|\beta|},
 \quad |\beta|\le M,\quad |h|\le2d_0|\xi|.
 \tag{CE14}
\]
To see the uniform tail explicitly, differentiation replaces the coefficients of degree \(\ell\ge K\) by fixed-degree polynomials in \(\ell\), while \(|h|/(d|\xi|)\) stays below a fixed number less than one. The remaining geometric tail is at most \(C^{K+1}K^M\) times its first power. Since \(K>M\), the indicated exponents are nonnegative.

Apply (CE8) after differentiating the product of this near cutoff, \(R_\xi\), and \(\widehat\chi_J(\xi-\eta)\). On this region \(1+|\eta|\le C|\xi|\). Derivatives of the near cutoff cost only fixed powers of \(|\xi|^{-1}\). Estimate (CE2), with moment order at most \(K+c\) and a fixed Fourier derivative, bounds each remaining product of \(|h|^{K-|\beta|}\) and a cutoff-transform derivative by \(C^{K+1}K^{K+c}\). Thus this part of the remainder pairing is at most
\[
 C^{K+1}K^{K+c}|\xi|^{m+q_1-K}.
 \tag{CE15}
\]
Here and below the fixed integer \(c\) may increase; it depends only on the fixed seminorm orders and dimension. Our choice of \(B\) covers all such orders.

**The remainder away from the diagonal.** On the far region,
\[
 |\eta-\xi|\ge d_0|\xi|,
 \qquad 1+|\eta|\le C(1+|\eta-\xi|).
 \tag{CE16}
\]
For the \(a(\eta)\) part use (CE5) through order \(M\), the weight in (CE8), and (CE2) with \(s=K+m+q_1+c\). This gives \(C^{K+1}K^{K+c}|\xi|^{-K}\), after a fixed increase of \(c\).

For each Taylor polynomial term of degree \(|\alpha|<K\), use (CE2) with \(s=K+|\alpha|+q_1+c\). Differentiating that polynomial through order \(M\) costs at most a fixed-degree polynomial in \(K\). Equation (CE6) then gives, with (CE16), a bound by
\[
 C^{K+|\alpha|+1}K^{K+c}|\xi|^{m-K}
                      (K/|\xi|)^{|\alpha|}.
 \tag{CE17}
\]
All cutoff derivative orders used are below \(2K+c\), hence below \(J=4K\). Summing the finitely many terms as in (CE13) proves the same bound, up to increasing the exponential constant. Equations (CE15)–(CE17) bound the entire remainder by the right side of (CE15), since \(m,q_1\ge0\).

Combine the polynomial and remainder estimates. Since \(K=N+B\), \(B>m+q_1\), and
\[
 (N+B)^{N+B+c}\le C_B^{N+1}N^N,
 \tag{CE18}
\]
we obtain
\[
 |\widehat v_N(\xi)|
       \le C^{N+1}N^N(1+|\xi|)^{-N}
       \quad(|\xi|\ge K).
 \tag{CE19}
\]
To justify (CE18), divide by \(N^N\), use
\((1+B/N)^N\le e^B\), and absorb the fixed power
\((N+B)^{B+c}\) into a fixed exponential. Replacing \(|\xi|^{-N}\) by \((1+|\xi|)^{-N}\) costs at most \(2^N\).

For \(|\xi|<K\), the common compact distributional bound gives a fixed polynomial bound for \(\widehat v_N\). Increasing \(C\) makes (CE19) hold there too, because \(K=N+B\), \(N/(N+B)\) has its \(N\)-th power bounded below by a positive constant depending only on \(B\), and a fixed polynomial in \(N+B\) is bounded by a fixed exponential. Thus \(v_N\) is an analytic absence sequence at the chosen point and direction. This proves (CE7). \(\square\)

## 3. A Fourier gap is analytically regular in its interior cone

**Lemma 3.1.** Let \(r\in\mathcal S'\). If \(\widehat r\) vanishes on an open real cone above some radius, then \(r\) has no analytic wavefront in any strictly smaller cone, at any base point.

**Proof.** Choose a smooth frequency cutoff \(b\) equal to one on a neighborhood of \(\operatorname{supp}\widehat r\), zero on a smaller high-frequency cone, and with symbol bounds of order zero. This is possible by angular cutoffs and a cutoff equal to one in a large ball. Then \(\widehat r=b\widehat r\). For \(\xi\) in the still smaller output cone and sufficiently large, every \(\eta\) in the support of \(b\) satisfies
\[
 1+|\xi-\eta|\ge c(1+|\xi|+|\eta|).
 \tag{CE20}
\]
Apply a fixed tempered seminorm estimate for \(\widehat r\) to
\(b(\eta)\widehat\chi_J(\xi-\eta)\). Equation (CE2), with \(s=N+c\), absorbs its fixed weight and derivatives and gives \(C^{N+1}N^N(1+|\xi|)^{-N}\). Use a fixed sufficiently large multiple of \(N+c\) for \(J\), so every required derivative is allowed and the low cutoff derivatives remain uniform. Bounded \(\xi\) are handled by the common compact distributional bound as at the end of Theorem 2.1. The localizations \(\chi_Jr\) are the required sequence. The base neighborhood was arbitrary. \(\square\)

## 4. The reciprocal criterion for a convolution kernel

Let \(\mu\in\mathcal S'(\mathbb R^n)\). Call a real nonzero direction \(\xi_0\) noncharacteristic for \(\mu\) if there are a complex open conic neighborhood \(V\) of \(\xi_0\), a radius \(R\), and a holomorphic \(\Phi\) on \(V\cap\{|\zeta|>R\}\) such that
\[
 |\Phi(\zeta)|\le C(1+|\zeta|)^m,\qquad
 \Phi\,\widehat\mu=1
       \quad\hbox{on }V\cap\mathbb R^n\cap\{|\xi|>R\}.
 \tag{CE21}
\]
Here \(m\) may be enlarged to a nonnegative integer. The second identity means multiplication of a distribution by the smooth real restriction of \(\Phi\). Let \(\operatorname{Char}\mu\) be the complement of these directions in the nonzero real frequency space.

**Theorem 4.1.** For every \(v\in\mathcal E'(\mathbb R^n)\),
\[
 \operatorname{WF}_A(v)
   \subset\operatorname{WF}_A(\mu*v)
                \cup(\mathbb R^n\times\operatorname{Char}\mu).
 \tag{CE22}
\]

**Proof.** Compact support of \(v\) and temperedness of \(\mu\) give \(g=\mu*v\in\mathcal S'\) and
\(\widehat g=\widehat\mu\,\widehat v\). Here is the required test argument. For \(\phi\in\mathcal S\), the function
\(x\mapsto v_y(\phi(x+y))\) is Schwartz. Insert a fixed compact cutoff in \(y\); the finite order of \(v\) bounds its derivatives by finitely many derivatives of \(\phi\). Its weights are controlled by \(1+|x|\le C(1+|x+y|)\) for \(y\) in that compact set. These are continuous Schwartz seminorm bounds, and pairing the result with \(\mu\) defines \(g\in\mathcal S'\), agreeing with the proper convolution integral.

Every fixed derivative of \(\widehat v\) has at most the same polynomial order on real frequencies, with a constant depending on that derivative. Indeed it inserts a power of \(y\) on a fixed compact set before the same finite-order estimate. Thus multiplication by \(\widehat v\) preserves Schwartz tests. Applying Fourier inversion to a test, and passing the compact \(v\)-pairing through its rapidly decreasing integral in each required seminorm, gives
\[
 \begin{aligned}
 (\widehat\mu\,\widehat v)(\psi)
 &=\mu_x\!\left(v_y\!\left(
        \int e^{-i(x+y)\cdot\xi}\psi(\xi)\,d\xi\right)\right)\\
 &=(\mu*v)(\mathcal F\psi)=\widehat g(\psi).
 \end{aligned}
 \tag{CE25}
\]
This establishes the identity even when \(\widehat\mu\) is a distribution.

Fix a direction satisfying (CE21). Inside a smaller real cone choose a smooth angular cutoff, cut off also at bounded radius, and extend
\[
 a(\xi)=\rho(\xi)\Phi(\xi)
 \tag{CE23}
\]
by zero off its real domain. Arrange \(\rho=1\) on a still smaller cone at large radius. The supports of its transitions stay inside the domain of \(\Phi\). Cauchy estimates and homogeneous angular cutoff derivatives prove (CE5). On the smaller cone \(a=\Phi\), and uniform complex balls of radius \(d|\xi|\) stay in \(V\) above a larger radius, by compactness of the smaller unit section. Thus \(a\) satisfies Theorem 2.1 there.

Set \(r=v-T_ag\). On that cone at large frequency,
\[
 \widehat r=\widehat v-a\,\widehat\mu\,\widehat v=0
 \tag{CE24}
\]
by the distributional identity (CE21). Lemma 3.1 excludes analytic wavefront of \(r\) in a smaller cone at every point. If \(g\) is analytically regular at a base point in the chosen direction, Theorem 2.1 makes \(T_ag\) regular there too. Since \(v=T_ag+r\), the analytic absence estimates for the two terms, on common neighborhoods and cones, add to give absence for \(v\). This proves (CE22).

No nonvanishing assumption on the real restriction of \(\Phi\) is needed in this argument. What is used is exactly its holomorphic polynomial bound and the distributional product identity. \(\square\)

**Corollary 4.2.** The same inclusion holds for \(v\in\mathcal D'\), without a growth assumption on \(v\), if addition is proper on \(\operatorname{supp}\mu\times\operatorname{supp}v\).

**Proof.** At a relatively compact output neighborhood \(O\), properness makes the pairs contributing over \(\overline O\) compact. Their input projection, together with \(\overline O\), lies in one compact set. Choose \(\chi\in C_c^\infty\), equal to one near that set, and put \(v_c=\chi v\). Then \(v_c=v\) near \(O\) and \(\mu*v_c=\mu*v\) on \(O\). The latter assertion follows directly by the compact support integral defining proper convolution: the removed input factor vanishes near every contributing pair. Apply Theorem 4.1 to \(v_c\); equality on \(O\) identifies both local wavefront sets with the asserted ones. Cover the output space. \(\square\)

## References

The analytic convolution inclusion and its holomorphic reciprocal criterion are classical; Lars Hörmander, *The Analysis of Linear Partial Differential Operators I*, Theorem 8.6.15 and its following proper-convolution remark give the general context. The argument here proves the needed analytic multiplier estimate by Cauchy bounds, finite Taylor expansion and controlled cutoff moments. Its polynomial-growth condition on the complex neighborhood is part of the theorem. A merely smooth real reciprocal, or a reciprocal with unrestricted exponential growth, does not supply the estimates used above.

[P]: ../../AN02-L188.html#complete-proof
[A]: ../../AN02-L186.html#complete-proof
[F]: ../../prerequisites/schwartz-fourier-foundations.html
[C]: ../../AN02-L045.html
[U]: ../../prerequisites/proper-convolution-and-compact-support.html
