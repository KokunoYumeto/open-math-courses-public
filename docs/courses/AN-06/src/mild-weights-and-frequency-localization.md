# Mild weights and frequency localization

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*


**Working question: Can localization preserve a weight that is not a power?** The useful test is the ratio of weights on adjacent dyadic shells. A weight may include logarithmic factors and still have controlled adjacent ratios. Localization must respect that actual norm when the energy graph is straightened; replacing it by a convenient power would lose the stated range of forcing terms.

Resolvent estimates are first proved near one piece of an energy surface. To combine those estimates, we need to cut Fourier space into pieces, change its local coordinates, and keep control of a spatial endpoint norm. This lesson proves those operations for weights whose size changes by at most a fixed factor between adjacent shells.

Use the shells \(A_j\) and radii \(R_j=2^j\) from [Endpoint spaces and flat energy shells](endpoint-spaces-and-flat-energy-shells.md). The two weighted Hilbert bounds will give the shell-block estimate directly in Section 2, for scalar and Hilbert-valued outputs together. We then treat non-power weights and a continuous family of Fourier cutoffs. The freely readable Agmon lectures [A], Section 1, state the power-weight transfer as Proposition 1.A; the complete argument below supplies the more general adjacent-shell transfer. Teschl [T], Chapter 12, gives freely accessible scattering background.

Read the earlier [Schwartz transform and its distributional dual](../providers/analysis/finite-derivative-l2.md#tempered-fourier-duality), [integer Sobolev density](../providers/analysis/euclidean-approximation-and-convolution.md#integer-sobolev-density), [strong measurability and norm limits](../providers/analysis/hilbert-valued-integration.md#strong-measurability), [Hilbert projection and representation](../providers/analysis/finite-trace-ideals.md#elementary-hilbert-tools), and [logarithms and real powers](../providers/analysis/elementary-functions-and-cutoffs.md#logarithm-and-real-powers). The endpoint lesson supplies the shell duality proof; the details below verify its use with the present weights and Hilbert-valued outputs.

<a id="mild-shell-spaces"></a>

## 1. Adjacent-shell weights

Let \(c_j>0\) and suppose that, for a fixed \(M\geq1\),

\[
 M^{-1}\leq c_{j+1}/c_j\leq M\quad(j\geq0).
\]

Define

\[
 \|u\|_{B_c}=\sum_{j\geq0}c_j\|u\|_{L^2(A_j)},
 \qquad
 \|v\|_{B_c^*}=\sup_{j\geq0}c_j^{-1}\|v\|_{L^2(A_j)}.
\]

The componentwise Banach-space and duality proofs in the endpoint lesson apply after changing the component weights. In particular \(B_c\) is Banach, its integral dual is \(B_c^*\), and \(C_c^\infty\) is dense in \(B_c\). Both spaces embed continuously in tempered distributions: \(c_0M^{-j}\leq c_j\leq c_0M^j\), and rapid decrease of a Schwartz test function makes its pairings with these shell components summable. This also proves that convergence in either norm implies distributional convergence.

Here are explicit comparisons behind these facts. The map taking \(u\) to \((c_j1_{A_j}u)_j\) is an isometric bijection from \(B_c\) to \(\ell^1(L^2(A_j))\); the reciprocal scaling identifies \(B_c^*\) with \(\ell^\infty(L^2(A_j))\). The complete component, duality and representation proofs from the endpoint lesson therefore apply exactly, including the conjugations for complex pairings. Truncating the shell sum and then approximating in \(L^2\) by compact smooth functions supported in one fixed larger ball proves density: on that ball Cauchy–Schwarz bounds the finite weighted shell sum by a constant times the \(L^2\) norm.

For the distribution estimates choose an integer \(l\) so large that \(\rho=M2^{n/2-l}<1\), and put \(p_l(\phi)=\sup_x\langle x\rangle^l|\phi(x)|\). Shell volume and weight comparison give \(\|1_{A_j}\phi\|_2\le C_{n,l}2^{j(n/2-l)}p_l(\phi)\). Thus

\[
 \begin{gathered}
 \left|\int u\phi\right|
 \le C_{n,l}c_0^{-1}\|u\|_{B_c}p_l(\phi),\\
 \left|\int v\phi\right|
 \le \frac{C_{n,l}c_0}{1-\rho}
          \|v\|_{B_c^*}p_l(\phi).
 \end{gathered}
\]

Both spatial integrals are absolutely convergent: the first uses the supremum of \(c_j^{-1}\|1_{A_j}\phi\|_2\), and the second its counterpart summed with \(c_j\). These estimates prove continuity in \(\mathcal S'\). They also show that sufficiently rapid Schwartz convergence implies convergence in either shell norm. Each shell function is locally square integrable; injectivity as a distribution follows by compact smooth \(L^2\) tests on bounded sets.

Write \(\|u\|_s=\|\langle x\rangle^s u\|_2\). Choose an integer \(N\geq1\) such that \(2^N>M\), and put \(q=M2^{-N}<1\).

**Lemma 1.1.** For each \(k\geq0\),

\[
 \|u\|_{B_c}\leq\frac{2^N}{1-q}\,c_k
       \big(R_k^N\|u\|_{-N}+R_k^{-N}\|u\|_N\big).
\]

The statement includes the possibility that a norm on the right is infinite.

**Proof.** On \(A_j\), including \(j=0\),

\[
 R_j/2\leq\langle x\rangle\leq\sqrt2R_j.
\]

Thus \(\|u\|_{L^2(A_j)}\leq2^NR_j^N\|u\|_{-N}\), and also \(\|u\|_{L^2(A_j)}\leq2^NR_j^{-N}\|u\|_N\). Use the first estimate for \(j\leq k\), the second for \(j>k\), and \(c_j/c_k\leq M^{|j-k|}\). The resulting coefficients are bounded by

\[
 \sum_{j\leq k}c_jR_j^N\leq\frac{c_kR_k^N}{1-q},
 \qquad
 \sum_{j>k}c_jR_j^{-N}\leq\frac{q\,c_kR_k^{-N}}{1-q}.
\]

Discarding \(q\) in the second bound proves the result. \(\square\)

<a id="mild-hilbert-values"></a>

For the vector-valued assertion below, \(L^2(\Omega;H)\) means strongly measurable functions with square-integrable norm, where \(H\) is any Hilbert space. It is complete. Indeed choose from a Cauchy sequence a subsequence whose consecutive \(L^2\) distances are at most \(2^{-j}\). The finite sums of their pointwise norm differences have \(L^2\) norm at most \(\sum_j2^{-j}\), by the scalar triangle inequality. Monotone convergence of their squares gives an \(L^2\) majorant, finite almost everywhere. Completeness of \(H\) gives the pointwise vector limit; the earlier strong-measurability closure proof makes it strongly measurable. Applying the same bound to each tail proves \(L^2\) convergence, and the Cauchy property gives convergence of the original sequence. Pointwise inner products are integrable by Cauchy–Schwarz, so this complete norm is the Hilbert norm of their integral. No separability of the ambient \(H\) was assumed. The norm-completeness argument uses only completeness of the target, so it also proves completeness of \(L^2(\Omega;B)\) for any Banach space \(B\).

Weighted \(L^2(\Omega;H)\) is isometric to this space by multiplication by the positive weight. Weighted shell spaces with values in \(H\) are complete by the same component argument as above. When \(H=L^2_\eta\), these are the usual scalar product integrals in \((x,\eta)\): finite sums of products identify the two \(L^2\) norms by Tonelli, and are dense on both sides. On the joint scalar space this density is the earlier approximation by rectangles. On the vector space, first truncate the support and vector norm, then approximate the strongly measurable function by finite-valued functions; dominated convergence in squared norm gives density. This proves the identification by completion and supplies the product-space interpretation used in Section 4.

<a id="mild-weighted-transfer"></a>

## 2. Consistent weighted bounds imply shell bounds

**Theorem 2.1.** Suppose a linear operator \(T\) is bounded on \(L^2_{-N}\), restricts to a bounded operator on \(L^2_N\), and both norms are at most \(A\). Then

\[
 \|Tu\|_{B_c}\leq C_N A\,\frac{1+q}{1-q}\,\|u\|_{B_c}.
\]

The constant \(C_N\) depends on \(N\), not on the individual \(c_j\). The conclusion also holds from scalar-valued inputs to Hilbert-valued outputs, using the corresponding weighted Hilbert norms and shell norms.

**Proof.** On \(A_j\), the weight satisfies \(R_j/2\leq\langle x\rangle\leq\sqrt2R_j\). The positive weighted bound therefore gives, for a one-shell input,

\[
 \|1_{A_k}T1_{A_j}u\|_2
 \leq 2^NR_k^{-N}\|T1_{A_j}u\|_N
 \leq 2^{3N/2}A(R_j/R_k)^N\|1_{A_j}u\|_2.
\]

The negative weighted bound gives the opposite ratio:

\[
 \|1_{A_k}T1_{A_j}u\|_2
 \leq 2^{N/2}R_k^N\|T1_{A_j}u\|_{-N}
 \leq 2^{3N/2}A(R_k/R_j)^N\|1_{A_j}u\|_2.
\]

Taking the smaller bound yields

\[
 \|1_{A_k}T1_{A_j}u\|_2
     \leq C_NA\,2^{-N|k-j|}\|1_{A_j}u\|_2.
\]

Here one may take \(C_N=2^{3N/2}\). The calculation uses only multiplication by a scalar weight and its Hilbert norm; it applies unchanged to a Hilbert-valued output, without a dimension factor.

Multiply this estimate by \(c_k\). Since \(c_k/c_j\leq M^{|k-j|}\), it follows that

\[
 c_k\|1_{A_k}Tu\|_2
 \leq C_NA\sum_j q^{|k-j|}c_j\|1_{A_j}u\|_2.
\]

For finite shell sums, sum in \(k\) and use \(\sum_{\ell\in\mathbb Z}q^{|\ell|}=(1+q)/(1-q)\). General shell sums converge in \(B_c\). They also converge in \(L^2_{-N}\), because

\[
 \|1_{A_j}u\|_{-N}
 \leq C_NR_j^{-N}c_j^{-1}\,c_j\|1_{A_j}u\|_2
 \leq C_Nc_0^{-1}q^j c_j\|1_{A_j}u\|_2.
\]

Thus the extension from finite sums agrees with the already defined endpoint operator. Taking the norm limit proves the assertion. \(\square\)

For power weights \(c_j=2^{js}\), this gives the familiar weighted interpolation implication. The ratio formulation also permits changing powers or oscillating weights. The strict inequality \(q<1\) is the summability condition that allows the output to spread between shells.

<a id="mild-multipliers"></a>

## 3. Multipliers and Fourier coordinates

The Fourier inversion, Plancherel and weighted differentiation identities used here are proved in the earlier [Fourier prerequisite](../providers/analysis/finite-derivative-l2.md#fourier-normalization), with its transform multiplied by \((2\pi)^{-n/2}\) for our unitary convention. The complete [change-of-variables proof (CI4)](../providers/analysis/coordinate-inverses-and-integration.md#coordinate-integration) applies to all the measurable integrands below, not merely continuous test functions.

We will use weighted duality with its consistency made explicit. The dual of \(L^2_N(H)\) under the unweighted integral pairing is \(L^2_{-N}(H)\), with equal norms: multiply a test by \(\langle x\rangle^N\), apply the earlier Hilbert representation proof in ordinary \(L^2(H)\), and multiply its representing vector by \(\langle x\rangle^N\). This proves both representation and the exact norm. Compact smooth scalar tests are dense in both scalar weighted spaces by truncation and the earlier mollification proof, since weights are bounded above and below on each fixed ball. Finite products of such tests are dense in the product spaces just described.

In particular, suppose \(S\) is bounded on ordinary \(L^2\), and its ordinary adjoint \(S^*\) has a bounded action on \(L^2_N\). The pairing \((f,S^*g)\) for \(f\in L^2_{-N}\), \(g\in L^2_N\), defines a unique output in \(L^2_{-N}\) with norm at most \(\|S^*\|_{L^2_N\to L^2_N}\|f\|_{-N}\). This is the negative weighted extension of \(S\). On ordinary \(L^2\) it agrees with \(S\), first by the adjoint identity on compact tests and then by density. More explicitly, compact smooth approximants converge in ordinary \(L^2\) and hence in \(L^2_{-N}\); the two output limits agree as distributions. If \(S\) also preserves \(L^2_N\), that restriction agrees with the negative extension for the same reason. The identical argument applies between distinct Hilbert-valued \(L^2\) spaces. Thus the two endpoint bounds below define one operator on their intersection, as required in Theorem 2.1.

**Corollary 3.1.** If \(r\in C^N(\mathbb R^n)\) and every derivative through order \(N\) is bounded, then the Fourier multiplier \(r(D)\) is bounded on \(B_c\), with

\[
 \|r(D)u\|_{B_c}\leq C_{N,M}
       \sum_{|\alpha|\leq N}\|\partial^\alpha r\|_\infty\,
       \|u\|_{B_c}.
\]

Here \(r(D)\) on \(B_c\) is the continuous extension of its action on test functions.

**Proof.** Plancherel and the expansion of \((1+|x|^2)^N\) identify \(\|u\|_N\), up to constants depending on \(N,n\), with the sum of the \(L^2\) norms of \(\partial_\xi^\alpha\widehat u\) for \(|\alpha|\leq N\). Leibniz's rule for \(r\widehat u\) gives the positive weighted bound. This remains valid for the stated finite regularity \(r\in C^N\). For a compact smooth frequency input the product is \(C^N\), and repeated classical integration by parts against compact tests identifies its weak derivatives through order \(N\) with the Leibniz formula. Its terms are \(L^2\) by the bounded coefficient derivatives. Approximate a general \(H^N\) frequency input by the compact smooth core proved in the earlier Sobolev reading. The product bounds make all derivative sequences Cauchy in \(L^2\); testing their limits proves the same weak identities. The zeroth bound identifies the resulting function as \(r\widehat u\). This proves the positive estimate on its whole domain without multiplying an arbitrary distribution by a merely \(C^N\) coefficient. The conjugate multiplier \(\overline r(D)\) has the same bound. Duality between \(L^2_N\) and \(L^2_{-N}\), together with the Fourier adjoint identity, gives the negative weighted bound for \(r(D)\). Theorem 2.1 now applies. This construction agrees with the ordinary bounded \(L^2\) multiplier on their common domain, by test-function density. \(\square\)

<a id="mild-fourier-coordinates"></a>

**Theorem 3.2.** Let \(X_1,X_2\subset\mathbb R^n\) be open, \(\psi:X_1\to X_2\) a \(C^{N+1}\) diffeomorphism, and \(\chi\in C_c^\infty(X_1)\). The operator

\[
 Tu=\mathcal F^{-1}\big(\chi\, (\widehat u\circ\psi)\big)
\]

initially on test functions extends boundedly to \(B_c\). Its norm is controlled by the derivatives of \(\chi\) through order \(N\), those of \(\psi,\psi^{-1}\) through order \(N+1\) on neighborhoods of the relevant compact supports, and the size of those neighborhoods. The adjoint also maps \(B_c\) boundedly, so \(T\) has a bounded extension to \(B_c^*\) by duality.

**Proof.** Change of variables \(\eta=\psi(\xi)\) gives the exact Fourier-side adjoint

\[
 \widehat{T^*v}(\eta)
 =\overline{\chi(\psi^{-1}(\eta))}
       |\det D\psi^{-1}(\eta)|\,
       \widehat v(\psi^{-1}(\eta)).
\]

The amplitude is extended by zero outside \(X_2\); its support is compact inside \(X_2\). On \(L^2\), the formula for \(T\) is well defined because a \(C^1\) diffeomorphism and its inverse locally preserve null sets, as proved with (CI4). That formula and its adjoint are bounded on \(L^2\) by the same compact Jacobian bounds. The adjoint amplitude is \(C^N\): the determinant never vanishes, its sign is locally constant, and its derivatives through order \(N\) use only derivatives of the inverse through order \(N+1\). Compact interior support makes its zero extension \(C^N\) too. A positive weighted estimate for \(T\) follows by differentiating \(\chi(\widehat u\circ\psi)\) through order \(N\). Every chain-rule term contains a derivative of \(\widehat u\) of order at most \(N\), composed with \(\psi\), times bounded products of derivatives of \(\psi\) and \(\chi\). Change of variables bounds its \(L^2\) norm, because \(|\det D\psi^{-1}|\) is bounded on the compact image.

For a compact smooth frequency input all these derivatives are classical through order \(N\), are compactly supported, and are also weak derivatives by integration by parts. The earlier \(H^N\) core and the ordinary \(L^2\) bound extend the estimates to all positive weighted inputs, exactly as for the finite-regularity multiplier. The same argument applies to \(T^*\). Differentiating its Jacobian amplitude \(N\) times uses derivatives of \(\psi^{-1}\) through order \(N+1\); this explains the extra derivative in the hypothesis. Duality therefore supplies the negative weighted bounds for both operators. Their formulas agree on the intersection of the weighted spaces by density and the \(L^2\) adjoint calculation. Apply Theorem 2.1 to each. Finally define the action on \(B_c^*\) by \((Tu,v)=(u,T^*v)\); the representation of the dual of \(B_c\) makes this a bounded operator with the same adjoint norm. \(\square\)

For \(c_j=R_j^{1/2}\), both operators also preserve \(B^*_0\). Indeed their \(L^2\) formulas are bounded on \(L^2\), and \(L^2\subset B^*_0\). Approximate any \(B^*_0\) input in \(B^*\) by compactly supported smooth functions. Boundedness on \(B^*\) and closedness of \(B^*_0\) give the assertion. The same argument applies to the multipliers in Corollary 3.1.

**Example 3.3.** Near a compact part of \(p(\xi)=\xi_1+\beta\xi_2^2\), use the inverse energy coordinates

\[
 \psi(\tau,\eta)=(\tau-\beta\eta^2,\eta).
\]

Their Jacobian determinant is one. A compact cutoff in \((\tau,\eta)\) makes the transformed operator bounded on \(B\) and \(B^*\), even though the derivatives of \(\psi\) are not bounded on all of \(\mathbb R^2\). The compact-support restriction in Theorem 3.2 is exactly what supplies the necessary local bounds. In these coordinates \(p\circ\psi=\tau\).

<a id="mild-cutoff-family"></a>

## 4. A square-integrated family of cutoffs

Let \(\chi\in C_c^\infty(\mathbb R^n)\) and

\[
 Q_\eta u=\chi(D-\eta)u
       =\mathcal F^{-1}\big(\chi(\xi-\eta)\widehat u(\xi)\big).
\]

The parameter \(\eta\) translates the frequency window; it does not translate the physical shells.

**Theorem 4.1.** There is a finite constant \(C_{N,M,\chi}\) such that

\[
 \left(\int_{\mathbb R^n}\|Q_\eta u\|_{B_c}^2\,d\eta\right)^{1/2}
       \leq C_{N,M,\chi}\|u\|_{B_c}.
\]

**Proof.** First show that \(Q:u\mapsto(\eta\mapsto Q_\eta u)\) maps \(L^2_{\pm N}\) into \(L^2_\eta(L^2_{\pm N,x})\) boundedly. For the positive weight, Fourier differentiation and Leibniz give finitely many terms of the form

\[
 (\partial^\beta\chi)(\xi-\eta)
                     \partial^{\alpha-\beta}\widehat u(\xi).
\]

Integrate their squared absolute values first in \(\eta\). Translation invariance gives the factor \(\|\partial^\beta\chi\|_2^2\), independent of \(\xi\). The remaining \(\xi\) integrals are bounded by \(C\|u\|_N^2\). Finite-sum Cauchy–Schwarz controls the cross terms.

For the negative weight, compute the adjoint on test functions:

\[
 \widehat{Q^*v}(\xi)
      =\int\overline{\chi(\xi-\eta)}\widehat v(\xi,\eta)\,d\eta.
\]

After differentiating through order \(N\), Cauchy–Schwarz in \(\eta\) bounds each term by \(\|\partial^\beta\chi\|_2\) times the \(L^2_\eta\) norm of the relevant \(\xi\) derivative of \(\widehat v\). Integration in \(\xi\) proves \(Q^*:L^2_\eta(L^2_{N,x})\to L^2_{N,x}\). Weighted duality proves the required negative bound for \(Q\).

Apply the Hilbert-valued part of Theorem 2.1 with output Hilbert space \(L^2_\eta\). It yields the stronger estimate

\[
 \sum_k c_k
      \left(\int\|1_{A_k}Q_\eta u\|_2^2\,d\eta\right)^{1/2}
       \leq C_{N,M,\chi}\|u\|_{B_c}.
\]

For a finite number of shells, the scalar \(L^2_\eta\) triangle inequality moves their nonnegative sum outside the norm. Monotone convergence of the squared partial sums passes to all shells, proving the stated Minkowski step.

Here are the family and density details. The positive and negative weighted bounds are first proved on finite products of compact smooth parameter functions and Schwartz spatial inputs; their density in the weighted product spaces was proved above. The ordinary \(L^2\) bound for \(Q\) is already the zeroth-derivative calculation above: integration in \(\eta\) gives the factor \(\|\chi\|_2^2\), and Plancherel gives \(\|u\|_2^2\). Its adjoint has the same ordinary norm by Hilbert duality. Consequently weighted duality constructs consistent endpoint operators, and Theorem 2.1 applies to them.

For the pointwise family on \(B_c\), Corollary 3.1 gives a bound uniform in \(\eta\). It also proves norm continuity: the scalar segment formula gives

\[
 \|Q_\eta-Q_\zeta\|_{B_c\to B_c}
       \le C_{N,M,\chi}|\eta-\zeta|,
\]

because every derivative of \(\chi(\cdot-\eta)-\chi(\cdot-\zeta)\) through order \(N\) is bounded by \(|\eta-\zeta|\) times a fixed derivative bound of order at most \(N+1\). Thus \(\eta\mapsto Q_\eta u\) is a continuous Banach-valued function and is strongly measurable by the earlier continuous-map measurability proof. Choose compact smooth inputs converging to \(u\) in \(B_c\). Uniform multiplier boundedness gives convergence in \(B_c\) at every parameter, hence in each shell \(L^2\) norm. Fatou in \(\eta\), followed by the nonnegative sum version of Fatou over shells, passes the stronger displayed estimate to this pointwise family. The finite-sum triangle argument then gives the claimed estimate for \(u\). This family agrees almost everywhere with the integrated Hilbert-valued extension: approximating inputs converge to both in \(L^2_\eta(B_c)\), and the same Fatou estimate applied to their differences identifies the limits. \(\square\)

<a id="mild-distribution-detection"></a>

**Theorem 4.2 (detecting a function from a distribution).** Suppose \(\|\chi\|_2=1\), and let \(u\in\mathcal S'(\mathbb R^n)\) be any tempered distribution. Each \(Q_\eta u\) is a smooth function with at most polynomial growth. The extended nonnegative quantity

\[
 A(u)=\left(\int_{\mathbb R^n}
                    \|Q_\eta u\|_{B_c^*}^2\,d\eta\right)^{1/2}
\]

is well defined. If \(A(u)<\infty\), then \(u\) is represented by a unique function \(w\in B_c^*\), and

\[
 \|w\|_{B_c^*}\leq C_{N,M,\chi} A(u).
\]

In particular the distribution is locally square integrable as a consequence of the estimate. For an input already represented by a locally square-integrable function, the same inequality for its norm includes the case of an infinite right side.

**Proof.** Multiplication of \(\widehat u\) by \(\chi(\xi-\eta)\) gives a distribution with compact support. Here is the finite-order fact used in this step. Continuity of a distribution on tests supported in a fixed compact set gives a bound by finitely many defining seminorms: a basic neighborhood of zero bounds finitely many derivative suprema, and rescaling any test into that neighborhood gives \(|V(\varphi)|\le C\max_{|\alpha|\le m}\|\partial^\alpha\varphi\|_\infty\). If \(V\) has compact support, choose a smooth cutoff \(\theta=1\) near it and put \(V(h)=V(\theta h)\) for any smooth \(h\). This is independent of the cutoff: a compact test vanishing near the support is covered by finitely many open sets where \(V\) vanishes, and the finite bump partition proved in the coordinate prerequisite makes its value zero. The bound for \(\theta h\) is the required finite-order bound on a fixed compact neighborhood.

Its inverse Fourier transform is consequently smooth with polynomial growth: evaluate the compact distribution on \((2\pi)^{-n/2}e^{ix\cdot\xi}\), with the cutoff just constructed. Taylor difference quotients converge in every test seminorm on that fixed compact support, so differentiation in \(x\) passes through \(V\). The finite-order bound bounds each resulting exponential derivative by a polynomial in \(x\). Pairing with a Schwartz test and approximating its Fourier integral by compact Riemann sums proves that this function is the distributional inverse transform. To justify passing the compact distribution through that integral, let \(m\) be its finite order and let \(\theta\) be its fixed cutoff. The \(C^m\) norm in frequency of the part integrated over \(|x|>R\) is bounded by \(C_\theta\int_{|x|>R}(1+|x|)^m|v(x)|\,dx\), which tends to zero for a Schwartz test \(v\). On each compact \(x\) box, the integrand and its first \(m\) frequency derivatives are uniformly continuous, so the Riemann sums converge in that same norm. The finite-order bound therefore permits the passage, with the stated Fourier constant. For \(\eta\) in a fixed compact set, one may use the same compact frequency support and cutoff. Differentiating the translated \(\chi\) proves continuity of \(Q_\eta u\) and all its spatial derivatives, uniformly on compact spatial sets. In particular \(\eta\mapsto Q_\eta u\) is continuous into \(L^2(A_j)\) for each shell. The supremum of the countably many continuous shell norms is measurable, possibly infinite. This establishes the meaning of \(A(u)\).

For a Schwartz function \(v\) with compactly supported Fourier transform,

\[
 \int|\chi(\xi-\eta)|^2\widehat v(\xi)\,d\eta
       =\widehat v(\xi),
 \qquad
 (u,v)=\int(Q_\eta u,Q_\eta v)\,d\eta.
\]

Here the inner product is linear in its first entry, and its distributional extension has the same convention. Only the compact difference of the supports of \(\widehat v\) and \(\chi\) contributes to the parameter integral. The first identity holds in the topology of smooth functions on that fixed compact frequency support: every derivative may be taken under the integral, with a uniform integrable bound. Applying the Fourier distribution proves the second identity. Also \(Q_\eta u\) has polynomial growth and \(Q_\eta v\) is Schwartz, so the pairing on the right is the ordinary absolutely convergent spatial integral.

Suppose now \(A(u)<\infty\). For almost every \(\eta\), shell duality bounds that spatial integral; Cauchy–Schwarz in \(\eta\) and Theorem 4.1 then give

\[
 \begin{aligned}
 |(u,v)|
 &\leq A(u)
       \left(\int\|Q_\eta v\|_{B_c}^2\,d\eta\right)^{1/2}\\
 &\leq C_{N,M,\chi}A(u)\|v\|_{B_c}.
 \end{aligned}
\]

Compact-frequency Schwartz functions are dense in \(B_c\). Indeed compactly supported smooth functions, hence Schwartz functions, are dense there by the shell argument in Section 1. Cutting the Fourier transform of a Schwartz function off on growing balls converges in all Schwartz seminorms. The bound \(c_j\leq c_0 M^j\) converts sufficiently rapid spatial decrease into convergence of the shell sum, so this also gives \(B_c\) convergence.

Extend the conjugate-linear functional \(v\mapsto(u,v)\) by this density. The integral duality of \(B_c\), with the conjugate convention just specified, represents it by a unique \(w\in B_c^*\) with the displayed norm bound. Both \(w\) and \(u\) are tempered distributions. Compact-frequency Schwartz tests are also dense in the Schwartz topology, by the same Fourier cutoffs; equality on those tests therefore gives \(u=w\) in \(\mathcal S'\). Finally a \(B_c^*\) function is square integrable on each shell, and any compact set meets only finitely many shells. This proves the asserted local square integrability. \(\square\)

<a id="mild-radial-weights"></a>

## 5. Radial weights with controlled growth

Let \(\mu:[0,\infty)\to(0,\infty)\) be \(C^1\), and assume

\[
 (1+t)|\mu'(t)|\leq a\mu(t)\quad(t\geq0),
 \qquad a\geq0.
\]

Integration of \(|(\log\mu)'|\leq a/(1+t)\) proves, for \(0\leq s\leq t\),

\[
 \left(\frac{1+s}{1+t}\right)^a
 \leq\frac{\mu(s)}{\mu(t)}
 \leq\left(\frac{1+t}{1+s}\right)^a.
\]

Set \(\widetilde\mu(x)=\mu(|x|)\). No differentiability of this radial function at the origin is needed; it is used only as a positive multiplication weight. On each shell, \(\mu(|x|)\) and \(\mu(R_j)\) are comparable within a factor \(2^a\). This includes \(A_0\), since \((1+R_0)/(1+|x|)\leq2\).

**Corollary 5.1.** For \(\chi\in C_c^\infty\) with \(\|\chi\|_2=1\),

\[
 \int\|\widetilde\mu Q_\eta u\|_B^2\,d\eta
       \leq C_{a,\chi}\|\widetilde\mu u\|_B^2,
\]

whenever the input weighted norm is finite. For any \(u\in\mathcal S'\), finiteness of the integral in the following display first implies that \(u\) has a locally square-integrable representative. For that representative,

\[
 \|\widetilde\mu u\|_{B^*}^2
       \leq C_{a,\chi}
              \int\|\widetilde\mu Q_\eta u\|_{B^*}^2\,d\eta.
\]

Multiplication by \(\widetilde\mu\) in this conclusion is performed on the detected function. For an input already locally square integrable, the second inequality also includes infinite norms.

**Proof.** For the first assertion use \(c_j=R_j^{1/2}\mu(R_j)\). Its adjacent ratios lie between \(2^{-a-1/2}\) and \(2^{a+1/2}\); its shell norm is equivalent to \(\|\widetilde\mu u\|_B\). Choose any integer \(N\) with \(2^N>2^{a+1/2}\), and apply Theorem 4.1. For the second assertion use instead \(c_j=R_j^{1/2}/\mu(R_j)\), with the same ratio bound. For each localized smooth function its dual norm is equivalent to \(\|\widetilde\mu Q_\eta u\|_{B^*}\). A finite parameter integral therefore satisfies the hypothesis of Theorem 4.2, which detects a function \(w=u\) and bounds its \(B_c^*\) norm. Only then multiply \(w\) by the positive radial weight; the same shell comparison gives the claimed estimate. No product of a general distribution with the merely \(C^1\) radial weight is needed. The comparison constants depend on \(a\), while \(\mu(0)\) cancels from both sides. \(\square\)

For example \(\mu(t)=(1+t)^s\) works with \(a=|s|\). Products with powers of \(\log(e+t)\) also work: their logarithmic derivatives have an additional bounded contribution to \((1+t)|(\log\mu)'|\). These weights are useful when polynomial powers alone do not describe the desired far-field condition.

### Use the conclusion

For the graph-coordinate example, list the change-of-variables derivatives and the weight ratio used by each map. Then follow reconstruction back to one global norm; a family of local estimates is not yet that norm.

<a id="mild-exercises"></a>

## 6. Exercises

**Exercise 6.1 (foundation).** Let \(c_j=2^{sj}(1+j)^b\), with \(s,b\in\mathbb R\). Find a valid adjacent-ratio constant \(M\), and an integer condition on \(N\) sufficient for Theorem 2.1.

**Exercise 6.2 (foundation).** For a unit \(L^2\) vector supported in \(A_k\), compare \(c_k(R_k^N\|u\|_{-N}+R_k^{-N}\|u\|_N)\) with \(\|u\|_{B_c}\). Explain why Lemma 1.1 is useful for a one-shell input but not an exact norm formula for an arbitrary input.

**Exercise 6.3 (intermediate).** Derive the Fourier-side adjoint for the map \(\psi(\tau,\eta)=(\tau-\beta\eta^2,\eta)\) in Example 3.3. Then replace \(\psi\) by the dilation \(\psi(\xi)=b\xi\), \(b>0\), and retain its Jacobian factor.

**Exercise 6.4 (intermediate).** On \(L^2\), prove the exact identity \(\int\|Q_\eta u\|_2^2\,d\eta=\|\chi\|_2^2\|u\|_2^2\). Explain why it does not by itself prove Theorem 4.1. For \(u=\delta_0\) and nonzero \(\chi\), compute \(Q_\eta u\) and show that \(A(u)=\infty\) for every adjacent-shell weight from Section 1.

**Exercise 6.5 (advanced).** Prove that \(\mu(t)=(1+t)^s[\log(e+t)]^b\) satisfies the hypothesis of Corollary 5.1 with \(a=|s|+|b|\). Use the two different shell weights in that proof to state the resulting upper \(B\) estimate and lower \(B^*\) estimate. Explain why the same \(c_j\) cannot be used for both unless \(\mu\) is constant up to fixed factors.

<a id="mild-solutions"></a>

## 7. Complete solutions

**Solution 6.1.** The ratio is \(2^s((j+2)/(j+1))^b\), where the fraction lies in \([1,2]\). Thus both the ratio and its reciprocal are at most \(M=2^{|s|+|b|}\). Any integer \(N\geq1\) with \(N>|s|+|b|\) gives \(2^N>M\). This is a sufficient bound, not always the smallest possible choice.

**Solution 6.2.** On \(A_k\), \(R_k/2\leq\langle x\rangle\leq\sqrt2R_k\). Consequently \(R_k^N\|u\|_{-N}\) lies between \(2^{-N/2}\) and \(2^N\), and \(R_k^{-N}\|u\|_N\) lies between \(2^{-N}\) and \(2^{N/2}\). The whole expression is therefore bounded above and below by positive constants depending only on \(N\) times \(c_k=\|u\|_{B_c}\). For a general input, the two global weighted Hilbert norms combine shell contributions in squares; \(B_c\) combines them in an absolute sum. A chosen \(k\) balances those two global weights but does not recover all shell amplitudes exactly.

**Solution 6.3.** The inverse map is \(\psi^{-1}(\xi_1,\xi_2)=(\xi_1+\beta\xi_2^2,\xi_2)\), with determinant one. Thus

\[
 \widehat{T^*v}(\xi_1,\xi_2)
 =\overline{\chi(\xi_1+\beta\xi_2^2,\xi_2)}
       \widehat v(\xi_1+\beta\xi_2^2,\xi_2).
\]

For the dilation, \(\psi^{-1}(\eta)=\eta/b\) and \(|\det D\psi^{-1}|=b^{-n}\). The adjoint is therefore

\[
 \widehat{T^*v}(\eta)=b^{-n}\overline{\chi(\eta/b)}\widehat v(\eta/b).
\]

Without \(b^{-n}\), the formula fails the \(L^2\) change-of-variables identity even when \(\chi\) is supported in a small ball.

**Solution 6.4.** Plancherel and Tonelli give

\[
 \int\|Q_\eta u\|_2^2\,d\eta
 =\iint|\chi(\xi-\eta)|^2|\widehat u(\xi)|^2\,d\xi\,d\eta
 =\|\chi\|_2^2\|u\|_2^2.
\]

The \(B_c\) norm contains spatial shell weights and a sum before squaring. Plancherel alone does not control spreading of a shell input into other physical shells. The weighted endpoint estimates and their off-diagonal consequence supply that missing information.

For the Dirac distribution, the unitary Fourier convention gives

\[
 \widehat{\delta_0}=(2\pi)^{-n/2},
 \qquad
 Q_\eta\delta_0(x)=(2\pi)^{-n/2}
                   e^{i\eta\cdot x}(\mathcal F^{-1}\chi)(x).
\]

The \(B_c^*\) norm is independent of \(\eta\), since the exponential has modulus one. It is positive because \(\chi\ne0\), and finite because \(\mathcal F^{-1}\chi\) is Schwartz and \(c_j^{-1}\leq c_0^{-1}M^j\). Its squared integral over all of \(\mathbb R^n\) is infinite. Thus the detection theorem imposes a substantive finite-integral condition; it does not turn every tempered distribution into a function.

**Solution 6.5.** Direct logarithmic differentiation gives

\[
 (\log\mu)'(t)=\frac{s}{1+t}
                    +\frac{b}{(e+t)\log(e+t)}.
\]

Since \((1+t)/((e+t)\log(e+t))\leq1\), the required bound holds with \(a=|s|+|b|\). Taking \(c_j=R_j^{1/2}\mu(R_j)\) gives

\[
 \int\|\mu(|x|)Q_\eta u\|_B^2\,d\eta
       \leq C\|\mu(|x|)u\|_B^2.
\]

Taking \(c_j=R_j^{1/2}/\mu(R_j)\) gives instead

\[
 \|\mu(|x|)u\|_{B^*}^2
       \leq C\int\|\mu(|x|)Q_\eta u\|_{B^*}^2\,d\eta.
\]

The dual shell norm divides by \(c_j\). Using the first choice in that dual norm would therefore weight \(u\) by \(\mu^{-1}\), rather than \(\mu\). When \(\mu\) varies without uniform upper and lower bounds, those are different conditions. For example \(\mu(t)=1+t\) strengthens the weighted \(B^*\) norm, while its reciprocal weakens it.

## References


- [T] Gerald Teschl, *Mathematical Methods in Quantum Mechanics: With Applications to Schrödinger Operators*, second edition, American Mathematical Society, 2014. [Freely readable author's edition](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf).
- [A] Shmuel Agmon, *Limiting Absorption Principle for Long Range Potentials*, lectures of 17–21 July 1978, based on notes by Karl Gustafson and reworked by Michael Taylor. [Author-hosted notes](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2020/08/AGMON.pdf), Section 1, Proposition 1.A. That proposition is stated there; the full adjacent-shell proof used here is Section 2 above.
