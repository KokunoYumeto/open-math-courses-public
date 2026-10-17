# Derivative growth and finite-order localization

*Written and self-checked by GPT-6 Astra (OpenAI), Ultra, October 2026. Public domain (CC0).*

A smooth cutoff can destroy analyticity. To measure analytic regularity by Fourier decay, we therefore allow the cutoff to depend on the number of derivatives being tested. The support stays in one compact set, and every fixed derivative remains uniformly bounded. Only the increasing derivative order has a growing cost. We construct these cutoffs and prove a Fourier criterion for an entire family of derivative-growth classes, including analytic and Gevrey functions.

The prerequisites are [Order, positivity and distributional limits](order-positivity-and-limits.md#local-estimates-and-the-meaning-of-order), the [Schwartz and Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), and the integral Taylor formula in [When a kernel is smooth](when-a-kernel-is-smooth.md#taylor-estimates-on-compact-neighborhoods). The [functional foundation](../prerequisites/U011-free-foundations/functional-foundations-U008.md), Section 6 and Sections 14.1–14.2, proves Baire's theorem and completeness of the smooth-function space. The [scalar foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), Section 13.10, supplies smooth bumps. The [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), Sections 15.0–15.1 and 16.1–16.2, supplies Lebesgue measure, dominated convergence, Fubini and affine substitution. All spaces and integrals below use these conventions.

Basic references are Lars Hörmander's *The Analysis of Linear Partial Differential Operators I* and the programme readings just listed. All proofs required here are given below or at those exact earlier locations. The Fourier transform is

\[
 \widehat f(\xi)=\int e^{-ix\cdot\xi}f(x)\,dx,
 \qquad
 f(x)=(2\pi)^{-n}\int e^{ix\cdot\xi}\widehat f(\xi)\,d\xi.
 \tag{1}
\]

Pairings are complex linear, and \(\partial^\alpha\) denotes ordinary differentiation, without a factor of \(1/i\). Throughout, \(n\ge1\).

## Growth scales and a useful shift estimate

Fix a nondecreasing sequence of positive numbers \(L=(L_k)_{k\ge0}\) with

\[
 L_0=1,\qquad k\le L_k,\qquad L_{k+1}\le QL_k
 \quad(k\ge0),\qquad Q\ge1.
 \tag{2}
\]

For an open set \(X\subset\mathbb R^n\), let \(C^L(X)\) consist of the smooth functions such that for every compact \(K\subset X\) there are constants \(A,B\ge1\) with

\[
 \sup_K|\partial^\alpha f|
       \le A(BL_{|\alpha|})^{|\alpha|}
       \quad\hbox{for every multi-index }\alpha.
 \tag{3}
\]

The expression of degree zero is one. Constants in (3) may depend on the compact set, but not on the derivative order.

**Lemma 1.** For fixed nonnegative integers \(a,b\), there are constants \(C,D\ge1\), depending only on \(a,b,Q\), such that

\[
 L_{k+a}^{k+b}\le CD^kL_k^k\qquad(k\ge0).
 \tag{4}
\]

**Proof.** Iterating (2) gives \(L_k\le Q^k\) and \(L_{k+a}\le Q^aL_k\). Hence

\[
 L_{k+a}^{k+b}
 \le Q^{a(k+b)}L_k^{k+b}
 \le Q^{ab}(Q^{a+b})^kL_k^k.
\]

This includes \(k=0\). Thus one may take \(C=Q^{ab}\), \(D=Q^{a+b}\). \(\square\)

In particular, any fixed number of extra derivatives, frequency powers or integration dimensions can be absorbed into the constants in (3). The fixedness of that number matters.

**Proposition 2.** The space \(C^L(X)\) is an algebra and is closed under every fixed partial derivative. If \(L_k\le cM_k\) for all \(k\ge1\), then \(C^L(X)\subset C^M(X)\).

**Proof.** On a common compact set choose constants \(A,B\) that work for both functions. For \(|\alpha|=k\), Leibniz' rule and monotonicity give

\[
 \begin{aligned}
 |\partial^\alpha(fg)|
 &\le A^2\sum_{\beta\le\alpha}\binom\alpha\beta
        (BL_{|\beta|})^{|\beta|}
        (BL_{k-|\beta|})^{k-|\beta|}\\
 &\le A^2(2BL_k)^k.
 \end{aligned}
 \tag{5}
\]

Here \(\sum_{\beta\le\alpha}\binom\alpha\beta=2^k\), obtained by multiplying the ordinary binomial identities in the coordinates. Sums and scalar multiples satisfy (3) by the triangle inequality. A derivative of fixed order \(r\) has bound \(A B^{k+r}L_{k+r}^{k+r}\); apply Lemma 1 with \(a=b=r\). Finally replace \(BL_k\) by \(BcM_k\) in (3). \(\square\)

For \(L_k=(k+1)^s\), \(s\ge1\), condition (2) holds with \(Q=2^s\). These are the Gevrey classes of order \(s\). The case \(s=1\) is exactly real analyticity, as the next argument checks.

**Proposition 3.** A smooth function is real analytic if and only if it satisfies (3) for \(L_k=k+1\). For general \(s\ge1\), the estimate using \((k+1)^{sk}\) is equivalent to an estimate \(A B^k(k!)^s\).

**Proof.** For \(k\ge1\), the exponential series gives

\[
 k!\le(k+1)^k\le e^{k+1}k!\le e^{2k}k!.
 \tag{6}
\]

The middle inequality follows because \(e^{k+1}\) is at least its \(k\)-th term \((k+1)^k/k!\). Raising (6) to \(s\) proves the assertion about Gevrey bounds.

Suppose first that the derivative bound is \(A B^k k!\) on a closed ball inside \(X\). Apply the integral Taylor theorem at an interior point \(x\), along the segment from \(x\) to \(x+h\). Its remainder after degree \(k-1\) is bounded by

\[
 A B^k k!\sum_{|\alpha|=k}\frac{|h^\alpha|}{\alpha!}
       =A(B|h|_1)^k,
 \qquad |h|_1=\sum_j|h_j|.
 \tag{7}
\]

The equality is the multinomial formula. For \(B|h|_1<1\) the remainder tends to zero, and the same bound on the homogeneous Taylor terms proves absolute convergence. Thus the Taylor series represents the function near every point.

Conversely, suppose a power series \(\sum_\alpha a_\alpha(x-c)^\alpha\) represents the function near \(c\) and converges absolutely on a polydisc of radius larger than \(R>0\). Put \(S=\sum_\alpha|a_\alpha|R^{|\alpha|}<\infty\). Then \(|a_\alpha|\le SR^{-|\alpha|}\). On \(|x_j-c_j|\le R/2\), termwise differentiation gives, for \(|\beta|=k\),

\[
 \begin{aligned}
 |\partial^\beta f(x)|
 &\le SR^{-k}\prod_{j=1}^n
       \sum_{m\ge0}\frac{(m+\beta_j)!}{m!}\,2^{-m}\\
 &=SR^{-k}\beta!\,2^{k+n}
 \le S2^n(2/R)^k k!.
 \end{aligned}
 \tag{8}
\]

The one-variable sum is \(r!(1-t)^{-r-1}\) at \(t=1/2\): differentiate the geometric series \(r\) times on a smaller closed interval in \((-1,1)\), where all differentiated series converge by the ratio test. These same bounds justify uniform convergence of the differentiated multivariable series and its termwise differentiation. A finite cover of any compact set by such smaller neighborhoods gives one pair of constants for that compact set. Equations (6)–(8) prove the result. \(\square\)

## Cutoffs with a growing differentiation budget

**Theorem 4.** Given a compact set \(K\subset X\), there are a compact \(K_1\subset X\), an open neighborhood \(V\) of \(K\), and functions \(\chi_N\in C_c^\infty(X)\), \(N\ge1\), such that

\[
 \begin{gathered}
 0\le\chi_N\le1,\qquad \chi_N=1\text{ on }V,
 \qquad \operatorname{supp}\chi_N\subset K_1,\\
 \|\partial^{\alpha+\beta}\chi_N\|_\infty
       \le C_\alpha(BN)^{|\beta|}
       \quad(|\beta|\le N).
 \end{gathered}
 \tag{9}
\]

Here \(B\) is independent of \(N,\alpha,\beta\); \(C_\alpha\) may depend on \(\alpha\), but not on \(N,\beta\).

**Proof.** The empty compact set permits \(\chi_N=0\), so assume \(K\ne\varnothing\). Using finitely many of the scalar foundation's ball cutoffs, choose a smooth compactly supported \(h\), with \(0\le h\le1\), equal to one on a neighborhood of \(K\). Explicitly, if \(b_j\) are cutoffs equal to one on balls covering \(K\), take \(h=1-\prod_j(1-b_j)\). Its support lies in the finite union of their outer closed balls, all inside \(X\).

Choose \(\delta>0\) so small that the closed \(2\delta\)-neighborhood of \(K\) lies where \(h=1\), and the closed \(\delta\)-neighborhood of \(\operatorname{supp}h\) is compactly inside \(X\). Existence follows from compactness and positive distance to the relevant closed complements. Let \(\rho\ge0\) be a smooth function supported in the unit ball with integral one. A nonzero nonnegative ball cutoff divided by its positive integral supplies it after rescaling. Set

\[
 \rho_t(x)=t^{-n}\rho(x/t),\qquad
 \chi_N=h*\underbrace{\rho_{\delta/N}*\cdots*
                      \rho_{\delta/N}}_{N\text{ factors}}.
 \tag{10}
\]

All convolutions here are ordinary compact integrals. Fubini proves associativity. Positivity and integral one preserve the interval \([0,1]\). Every total displacement in (10) has length at most \(\delta\). Consequently \(\chi_N=1\) on the open \(\delta\)-neighborhood of \(K\), and its support lies in the compact closed \(\delta\)-neighborhood of \(\operatorname{supp}h\). These are fixed choices of \(V,K_1\).

Differentiation under the integral and integration by parts permit placing a derivative on any selected smooth factor. Write the \(|\beta|\) coordinate differentiations in any order, and put each on a different one of the \(N\) mollifier factors. Put all \(\alpha\) derivatives on \(h\). No multinomial expansion is involved in this identity. For integrable \(g\), direct integration gives \(\|f*g\|_\infty\le\|f\|_\infty\|g\|_1\). Also

\[
 \|\rho_{\delta/N}\|_1=1,
 \qquad
 \|\partial_j\rho_{\delta/N}\|_1
       =(N/\delta)\|\partial_j\rho\|_1.
 \tag{11}
\]

Apply the convolution bound successively. Equation (9) follows with \(C_\alpha=\|\partial^\alpha h\|_\infty\) and \(B\ge\delta^{-1}\max_j\|\partial_j\rho\|_1\). The differentiated integrals are smooth by compact domination. This also justifies every redistribution of derivatives used above. \(\square\)

Taking \(\beta=0\) shows that the sequence is bounded in every smooth seminorm on its common support. Taking \(\alpha=0\) controls the first \(N\) derivatives by \((BN)^{|\beta|}\), up to a fixed factor. Both conclusions hold for the same sequence. Since \(N\le L_N\), (9) also holds with \(L_N\) in place of \(N\).

## Bounded compact distributions and their transforms

Write \(\mathcal E'(X)\) for the continuous dual of \(C^\infty(X)\). These are compactly supported distributions, acting on smooth functions by inserting a cutoff equal to one near their support. [Convolution as addition of supports](convolution-as-addition-of-supports.md#pairings-parameters-and-tensor-products), B0, proves independence of the cutoff and the finite smooth-seminorm bound for this extension. Conversely, continuity on \(C^\infty(X)\), followed by rescaling a finite seminorm neighborhood, bounds a functional by finitely many derivatives on one compact set. It restricts to a distribution and vanishes on tests outside that compact. This proves the asserted identification.

**Lemma 5.** A sequence \((v_N)\) is bounded in the strong dual \(\mathcal E'(X)\) if and only if there are a compact \(K_1\subset X\), an integer \(m\ge0\) and \(A\ge1\) such that

\[
 |v_N(\phi)|\le A\max_{|\alpha|\le m}\sup_{K_1}
                         |\partial^\alpha\phi|
 \quad(\phi\in C^\infty(X),\ N\ge1).
 \tag{12}
\]

In particular all supports lie in \(K_1\), and the zero extensions to \(\mathbb R^n\) satisfy

\[
 |\widehat v_N(\xi)|\le A'(1+|\xi|)^m
 \quad(\xi\in\mathbb R^n,\ N\ge1).
 \tag{13}
\]

**Proof.** Strong boundedness implies boundedness on each single smooth function. The closed subsets

\[
 F_j=\{\phi\in C^\infty(X):\sup_N|v_N(\phi)|\le j\}
\]

therefore cover \(C^\infty(X)\). By the supplied completeness and Baire proofs, some \(F_j\) has interior. There are a point \(\phi_0\in F_j\), an increasing defining seminorm \(q_l\) from the compact exhaustion, and \(\varepsilon>0\) such that \(q_l(\psi)<\varepsilon\) implies \(\phi_0+\psi\in F_j\). Subtraction yields \(|v_N(\psi)|\le2j\) on that neighborhood. For \(q_l(\psi)>0\), scale \(\psi\) by \(\varepsilon/(2q_l(\psi))\); the resulting estimate is \(4j q_l(\psi)/\varepsilon\). If \(q_l(\psi)=0\), apply the neighborhood bound to every scalar multiple and conclude \(v_N(\psi)=0\). This is (12), for the compact and derivative order defining \(q_l\).

Conversely, the strong dual seminorm associated with a bounded family \(\mathcal B\subset C^\infty(X)\) is \(\sup_{\phi\in\mathcal B}|v(\phi)|\). Its value on every \(v_N\) is bounded by (12), since the indicated smooth seminorm is bounded on \(\mathcal B\). This proves strong boundedness. Tests supported outside \(K_1\) have zero seminorm in (12), proving the support assertion.

For a compact distribution, its Fourier transform is the smooth function \(\widehat v(\xi)=v(e^{-ix\cdot\xi})\). To verify agreement with the distributional transform, insert a fixed compact cutoff in the pairing, express the Fourier transform of a Schwartz test by its integral, and move the functional through that integral. Its finite-order estimate permits this because derivatives through order \(m\) introduce only \(|\xi|^m\), integrable against a Schwartz test. Differentiation in \(\xi\) is justified in the same finite smooth seminorms. Applying (12) to the exponential gives (13). The zero extension is tempered by the same compact estimate and the Schwartz seminorms. \(\square\)

This lemma makes the word “bounded” substantive: both the compact support and the polynomial-growth exponent in (13) are uniform in \(N\).

## A Fourier test for local derivative growth

**Theorem 6.** Let \(u\in\mathcal D'(X)\) and \(x_0\in X\). The following are equivalent.

1. On some neighborhood of \(x_0\), the distribution \(u\) is represented by a function in \(C^L\).
2. There are a neighborhood \(V\) of \(x_0\), a bounded sequence \(v_N\in\mathcal E'(X)\), and constants \(A,B\ge1\), independent of \(N,\xi\), such that \(v_N=u\) on \(V\) and

\[
 |\widehat v_N(\xi)|
       \le A\left(\frac{BL_N}{|\xi|}\right)^N
 \quad(N\ge1,\ \xi\ne0).
 \tag{14}
\]

The estimate is in all real frequency directions. It makes no assertion at \(\xi=0\); (13) supplies the low-frequency control.

**Proof of necessity.** Choose nested compact neighborhoods of \(x_0\) inside a region where \(u=f\in C^L\). Apply Theorem 4 so that the common cutoff support is still in that region, and set \(v_N=\chi_N f\), extended by zero. These functions have uniformly bounded absolute values and one compact support, so they satisfy (12) with \(m=0\).

For \(|\alpha|=N\), Leibniz' rule, \(N\le L_N\), and \(L_j\le L_N\) for \(j\le N\) give

\[
 \|\partial^\alpha(\chi_N f)\|_\infty
        \le C(DL_N)^N,
 \tag{15}
\]

with constants independent of \(N,\alpha\). Indeed a term with \(j\) derivatives on the cutoff has bound \(C(B_1N)^j(B_2L_{N-j})^{N-j}\); summing its binomial coefficients gives \(C((B_1+B_2)L_N)^N\). Integrating (15) over a fixed box containing the support bounds its \(L^1\) norm by another fixed multiple. For any \(\xi\ne0\), choose a coordinate with \(|\xi_j|\ge |\xi|/\sqrt n\). Integration by parts \(N\) times in that coordinate gives

\[
 |\xi_j|^N|\widehat v_N(\xi)|
       \le\|\partial_j^Nv_N\|_1.
\]

The factor \(n^{N/2}\) is absorbed into \(B^N\), proving (14).

**Proof of sufficiency.** Lemma 5 gives (13) with fixed \(m,A'\). For a derivative order \(k\ge0\), choose

\[
 N=k+n+1,\qquad R=L_N\ge1.
 \tag{16}
\]

On \(|\xi|\le R\), estimate (13) and containment in a cube of side \(2R\) give

\[
 \int_{|\xi|\le R}|\xi|^k|\widehat v_N(\xi)|\,d\xi
       \le C R^{k+m+n}.
 \tag{17}
\]

The constant is independent of \(k\): \((1+R)^m\le2^mR^m\). On the annulus \(2^jR<|\xi|\le2^{j+1}R\), \(j\ge0\), use (14). Since \(k-N=-n-1\), the integrand \(|\xi|^k|\widehat v_N(\xi)|\) is at most \(A(BL_N)^N(2^jR)^{-n-1}\). The annulus is contained in a cube of volume \((2^{j+2}R)^n\). Summing the geometric series therefore gives

\[
 \int_{|\xi|>R}|\xi|^k|\widehat v_N(\xi)|\,d\xi
       \le C B^N L_N^{k+n}.
 \tag{18}
\]

For this \(N\), the inverse transform and all its derivatives through order \(k\) converge absolutely. Dominated difference quotients prove that it is \(C^k\). Fourier inversion on tempered distributions, proved in F4–F5 of the supplied Fourier foundation, identifies it with \(v_N\). More explicitly, Fubini pairs the absolutely convergent inverse integral with any Schwartz test to obtain the inverse distributional transform, and the two inverse identities then give \(v_N\).

All these representatives agree as distributions with \(u\) on the same \(V\). Their continuous representatives agree pointwise there: a nonzero continuous difference would, after multiplication by a constant complex phase, have positive real part on a ball; pairing with a nonnegative nonzero bump in that ball contradicts equality of distributions. For arbitrarily large \(k\) this gives one smooth function representing \(u\) on \(V\). Equations (17)–(18), including the inverse factor \((2\pi)^{-n}\), yield

\[
 \sup_V|\partial^\alpha u|
   \le C D^{k+n+1} L_{k+n+1}^{k+m+n},
 \qquad |\alpha|=k,
 \tag{19}
\]

after increasing \(D\ge1\). Apply Lemma 1 with \(a=n+1\), \(b=m+n\), and absorb the fixed factor \(D^{n+1}\). The result is \(C_1(D_1L_k)^k\), which is (3), even uniformly on \(V\). \(\square\)

The proof keeps the extra \(n+1\) derivatives and the distributional order \(m\) until the final shift estimate. No bound on the higher derivatives of one fixed cutoff can replace this argument at the analytic endpoint.

## Worked example and exercises

For \(f(x)=1/(1+x^2)\) on the real line, write

\[
 f(x)=\frac1{2i}\left(\frac1{x-i}-\frac1{x+i}\right).
 \tag{20}
\]

Direct repeated differentiation, and \(|x\pm i|\ge1\) for real \(x\), give \(|f^{(k)}(x)|\le k!\). Thus \(f\) belongs to the analytic class on every real open set. For any compact interval inside that set, Theorem 4 produces \(\chi_N\), and \(v_N=\chi_Nf\) satisfies (14) with \(L_N=N+1\). Each \(v_N\) has compact support, although \(f\) does not. The analytic information is in the uniform sequence estimate, rather than in analyticity of the individual compactly supported functions.

**Exercise 1 — fixed-order control.** Explain why \(\|\partial^\beta\chi_N\|_\infty\le C(BN)^{|\beta|}\), \(|\beta|\le N\), alone does not prove that \((\chi_N)\) is bounded in \(C_c^\infty\). Identify the additional estimate in Theorem 4 that does prove this.

**Solution.** For fixed positive \(|\beta|\), the displayed upper bound grows with \(N\). It therefore supplies no uniform bound for that derivative. In (9), instead take \(\alpha=\beta\) and the second multi-index equal to zero. This gives \(\|\partial^\beta\chi_N\|_\infty\le C_\beta\) for every \(N\). Together with the common compact support, these are precisely the bounded-test-family conditions proved in the earlier distribution lesson. \(\square\)

**Exercise 2 — why a fixed analytic cutoff cannot work.** Prove that a real analytic function on a connected open set which vanishes on a nonempty open subset vanishes everywhere. Deduce that no nonzero real analytic function on \(\mathbb R^n\) has compact support.

**Solution.** Let \(Z\) be the set of points having a neighborhood on which the function vanishes. It is nonempty and open. If \(x\) lies in its relative closure, take points of \(Z\) tending to \(x\). Every derivative is zero at those points, so continuity makes every derivative zero at \(x\). The convergent Taylor expansion near \(x\) is therefore zero, and \(x\in Z\). Thus \(Z\) is also relatively closed. Connectedness forces \(Z\) to be the entire open set. A compactly supported function on \(\mathbb R^n\) vanishes on the nonempty exterior of a large ball; apply the result. Connectedness of \(\mathbb R^n\) follows from its line segments and the intermediate value theorem. \(\square\)

**Exercise 3 — linear changes of variables.** Let \(T:\mathbb R^d\to\mathbb R^n\) be any linear map, \(b\in\mathbb R^n\), and let \(Y=\{y:Ty+b\in X\}\). Show that \(f\in C^L(X)\) implies \(f(Ty+b)\in C^L(Y)\), without assuming that \(T\) is injective or surjective.

**Solution.** A compact \(K\subset Y\) has compact image in \(X\). Let \(A,B\) be its constants in (3), and set \(H=\max_j\sum_i|T_{ij}|\). For each coordinate derivative in \(y_j\), the chain rule applies the constant-coefficient operator \(\sum_iT_{ij}\partial_{x_i}\). A product of \(k\) such operators has sum of absolute coefficient products at most \(H^k\). Every resulting derivative of \(f\) has order \(k\); hence the bound is \(A(BH L_k)^k\). Replace \(H\) by \(\max(1,H)\) to include \(T=0\) and degree zero. This proves the asserted compact estimates. \(\square\)

**Exercise 4 — compare two regularity demands.** For \(1\le s\le t\), prove the inclusion of Gevrey order \(s\) in Gevrey order \(t\), and explain how a sequence witnessing Theorem 6 for the first class also witnesses it for the second.

**Solution.** The weights satisfy \((k+1)^s\le(k+1)^t\). Proposition 2 proves the function-space inclusion. In (14), replacing \(L_N=(N+1)^s\) by the larger \((N+1)^t\) increases the right side. The same distributions, neighborhood, compact support, order, and constants still work. No change to the low-frequency estimate is needed. \(\square\)

## References

- [Schwartz functions and Fourier inversion](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5; [Order, positivity and distributional limits](order-positivity-and-limits.md), Section 1; and [When a kernel is smooth](when-a-kernel-is-smooth.md#taylor-estimates-on-compact-neighborhoods). These programme readings supply the explicitly used distributional, Fourier and Taylor proofs.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, reprint of the second edition (1990), Springer, 2003, [doi:10.1007/978-3-642-61497-2](https://doi.org/10.1007/978-3-642-61497-2). Sections 1.4 and 8.4 treat controlled cutoffs and derivative-growth regularity. The definitions and local Fourier criterion above credit this mathematical source; their proofs and teaching organization are supplied here.
