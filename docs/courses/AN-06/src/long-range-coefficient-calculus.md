# Regularizing long-range coefficients

*Written by GPT-6.1 Sol (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

**Working question: How much smoothing can a slowly varying coefficient tolerate?** At distance \(R\), an averaging radius \(R^\rho\), with \(0<\rho<1\), grows but has relative size \(R^{\rho-1}\to0\). Thus a derivative can be improved without averaging across a macroscopic part of the escaping ray. Moment cancellation decides the size of the remainder; a positive kernel alone cannot cancel every even moment.

A slowly decaying coefficient changes a classical trajectory over a long time. Constructing that trajectory requires differentiating the coefficient repeatedly, even if the original equation assumes only finitely many derivatives. The useful remedy is to separate a smooth long-range part from an integrable short-range remainder. The smoothing scale must grow with distance but remain small compared with that distance.

The derivative rules and Taylor remainder are proved in Section 1, and Section 4 gives the local inverse argument. We use the earlier [finite linear algebra and compact scalar calculus](../providers/analysis/coordinate-inverses-and-integration.md#coordinate-linear-algebra), [smooth cutoffs](../providers/analysis/elementary-functions-and-cutoffs.md#smooth-flat-cutoffs), and [convolution differentiation](../providers/analysis/euclidean-approximation-and-convolution.md#mollification). [Endpoint spaces and flat energy shells](endpoint-spaces-and-flat-energy-shells.md) explains the spatial scale of a short-range remainder. Hörmander [HW], Lemma 3.3, pp. 77–78, gives the dyadic regularization method; Yafaev [Y], Section 3, discusses the long-range scattering setting. We construct the signed moment kernel, prove the vanishing normalization and track the derivative bounds below.

## 1. A kernel that cancels Taylor terms

A positive averaging kernel cannot cancel all even moments. We instead use a smooth signed kernel. This causes no difficulty: only bounded integral norms and moment identities will enter the proof.

<a id="coefficient-taylor"></a>
Here are the calculus identities needed in the construction. A differentiable real function with equal endpoint values has an interior extremum unless it is constant; the two one-sided difference quotients at that extremum give derivative zero. Subtracting the affine secant function proves the mean value theorem. For a continuously differentiable real function, apply this on each subinterval of a partition. Its increment differs from the derivative at the left endpoint times the length by at most that length times the modulus of continuity of the derivative. Summing and sending the mesh to zero proves the fundamental theorem of calculus. For complex or vector functions apply this componentwise. Repeated integration gives, along a segment,

\[
 f(x+h)=\sum_{r=0}^{K-1}\frac{(h\cdot\nabla)^r f(x)}{r!}
 +\frac1{(K-1)!}\int_0^1(1-t)^{K-1}
                  (h\cdot\nabla)^K f(x+th)\,dt.
\]

Indeed, substitute the fundamental theorem successively for each derivative; interchanging the continuous integrals on the compact simplex leaves a section of volume \((1-t)^{K-1}/(K-1)!\), as follows by induction by integrating its preceding power. The multinomial expansion gives \((h\cdot\nabla)^r=\sum_{|\alpha|=r}(r!/\alpha!)h^\alpha\partial^\alpha\). Thus the remainder is bounded by \(C_{n,K}|h|^K\max_{|\alpha|=K,\,0\le t\le1}|\partial^\alpha f(x+th)|\). The product and chain rules follow by substituting the first-order increment expressions for the factors or the inner and outer maps; induction gives the multi-index product formula used below. These arguments apply through the stated finite differentiability order.

<a id="coefficient-moments"></a>
**Lemma 1.1.** For every integer \(K\geq1\), there is a real \(\eta\in C_c^\infty(\mathbb R^n)\) such that

\[
 \int\eta=1,\qquad
 \int y^\alpha\eta(y)\,dy=0\quad(1\leq|\alpha|<K).
\]

**Proof.** Choose a real smooth compactly supported \(\theta\) with integral one, and distinct positive numbers \(\lambda_0,\ldots,\lambda_{K-1}\). Define \(\theta_\ell(y)=\lambda_\ell^{-n}\theta(y/\lambda_\ell)\). Its moment of total degree \(r\) is \(\lambda_\ell^r\) times that of \(\theta\). The Vandermonde matrix \((\lambda_\ell^r)_{0\leq r,\ell<K}\) is invertible, because its determinant is \(\prod_{\ell<j}(\lambda_j-\lambda_\ell)\ne0\). Alternatively, nonsingularity follows without the determinant formula: a polynomial of degree less than \(K\) vanishing at all \(K\) distinct points is zero, since division by each root removes one linear factor. Thus the transpose has zero kernel and the square matrix is invertible. Solve

\[
 \sum_{\ell=0}^{K-1}c_\ell\lambda_\ell^r
 =\begin{cases}1,&r=0,\\0,&1\leq r<K.\end{cases}
\]

Then \(\eta=\sum c_\ell\theta_\ell\) has the required moments, simultaneously for every multiindex of each total degree. \(\square\)

For \(s>0\), put \(\eta_s(y)=s^{-n}\eta(y/s)\). Its \(L^1\) norm is independent of \(s\), while

\[
 \|\partial^\alpha\eta_s\|_1=s^{-|\alpha|}\|\partial^\alpha\eta\|_1.
\]

These identities explain precisely where high derivatives in a smoothed function will come from.

<a id="coefficient-lower-derivatives"></a>
**Proposition 1.2 (recovering the lower derivatives).** Let \(f\in C^K(\mathbb R^n)\), \(K\geq1\), and \(\varepsilon>0\). If \(f(x)\to0\) as \(|x|\to\infty\) and

\[
 |\partial^\alpha f(x)|\leq C_\alpha\langle x\rangle^{-K-\varepsilon}
 \qquad(|\alpha|=K),
\]

then every derivative of order \(r\leq K\) satisfies

\[
 |\partial^\alpha f(x)|\leq C'_\alpha\langle x\rangle^{-r-\varepsilon}
 \qquad(|\alpha|=r).
\]

**Proof.** First show that each lower positive-order derivative tends to zero. The function \(f\) is bounded, since it tends to zero outside large balls and is continuous on compact sets. For \(|x|\geq2\), set \(R=|x|/2\) and \(F_x(z)=f(x+Rz)\), \(|z|\leq1\). Taylor's theorem at zero gives a polynomial \(P_x\) of degree at most \(K-1\) with

\[
 \sup_{|z|\leq1}|F_x(z)-P_x(z)|\leq C|x|^{-\varepsilon}.
\]

Indeed every point on the Taylor segment has distance at least \(|x|/2\) from the origin, and the rescaled order-\(K\) derivatives are bounded by \(CR^K|x|^{-K-\varepsilon}\). Thus \(P_x\) is uniformly bounded on the unit ball. Its coefficients are uniformly bounded as well: choose \(K\) distinct coordinates in \([-1/(2\sqrt n),1/(2\sqrt n)]\) in each variable, and evaluate the polynomial on their tensor grid. The grid lies in the unit ball. The tensor product of the invertible Vandermonde matrices recovers every coefficient of a polynomial with degree at most \(K-1\) in each variable from those finitely many values, with a fixed constant. It applies in particular to \(P_x\).

The coefficient of \(z^\alpha\) in \(P_x\) is \(R^{|\alpha|}\partial^\alpha f(x)/\alpha!\). Consequently
\(|\partial^\alpha f(x)|\leq C_\alpha|x|^{-|\alpha|}\)
for \(1\leq|\alpha|<K\), proving their vanishing. When \(K=1\), this preliminary range is empty. Vanishing of the zeroth derivative is a hypothesis.

Now descend from order \(K\). Suppose the sharper estimate is known at order \(r+1\). For \(|\alpha|=r\), the just established vanishing, or the given vanishing when \(r=0\), allows integration to infinity along the ray through \(x\):

\[
 \partial^\alpha f(x)
 =-\int_1^\infty\sum_{j=1}^n x_j
                      \partial^{\alpha+e_j}f(tx)\,dt.
\]

The integral converges absolutely and has bound

\[
 C|x|\int_1^\infty |tx|^{-r-1-\varepsilon}\,dt
 =\frac{C}{r+\varepsilon}|x|^{-r-\varepsilon}.
\]

Induction gives all orders through zero outside the fixed ball. Their continuity on that ball enlarges the constants to the stated global bounds. \(\square\)

**Example 1.3.** Vanishing of \(f\) is a real normalization condition. On the line, \(f(x)=\arctan x\) has \(f'(x)=(1+x^2)^{-1}\), so the order-one hypothesis holds for every \(0<\varepsilon<1\). Its two limiting constants are \(\pi/2\) and \(-\pi/2\). No single polynomial can make both tails tend to zero: boundedness forces that polynomial to be constant, and the two constants differ. Proposition 1.2 proves exactly the vanishing normalization needed for long-range coefficients, including dimension one.

## 2. Choosing a scale from the available regularity

<a id="coefficient-dyadic-regularization"></a>
**Theorem 2.1.** Let \(K\geq1\), \(0<\varepsilon<1\), and \(f\in C^K(\mathbb R^n)\) satisfy

\[
 |\partial^\alpha f(x)|\leq C_\alpha\langle x\rangle^{-\varepsilon-|\alpha|}
 \qquad(|\alpha|\leq K).
\]

For each \(0<b<\varepsilon\), there is a decomposition \(f=f_S+f_L\) with \(f_L\in C^\infty\),

\[
 |f_S(x)|\leq C\langle x\rangle^{-1-\varepsilon+b},
 \qquad
 |\partial^\alpha f_L(x)|\leq C'_\alpha\langle x\rangle^{-M(|\alpha|)},
\]

where

\[
 M(q)=\begin{cases}
 b+q,&0\leq q\leq K,\\
 1+\rho q,&q\geq K,
 \end{cases}
 \qquad \rho=\frac{K-1+b}{K}\in(0,1).
\]

The two formulas agree at \(q=K\). The sequence \(M\) is increasing and concave. For real \(f\), both parts can be chosen real.

**Proof.** Choose a smooth radial cutoff \(\chi\) equal to one on the unit ball and zero outside the ball of radius two. Set

\[
 \varphi_0(x)=\chi(x),\qquad
 \varphi_j(x)=\chi(2^{-j}x)-\chi(2^{1-j}x)\quad(j\geq1).
\]

The sum is one, by telescoping. For \(j\geq1\), \(\varphi_j\) is supported where \(2^{j-1}\leq|x|\leq2^{j+1}\), and \(|\partial^\alpha\varphi_j|\leq C_\alpha2^{-j|\alpha|}\). Put \(g_j=\varphi_jf\), \(R_j=2^j\), and \(s_j=R_j^\rho\). The product rule gives

\[
 \|\partial^\alpha g_j\|_\infty
 \leq C_\alpha R_j^{-\varepsilon-|\alpha|}\quad(|\alpha|\leq K).
\]

The same bound for \(j=0\) holds with a different finite constant. Take \(\eta\) from Lemma 1.1 and define

\[
 h_j=\eta_{s_j}*g_j,\qquad f_L=\sum_{j\geq0}h_j.
\]

If \(\eta\) is supported in a ball of radius \(C_\eta\), the support of \(h_j\) lies within distance \(C_\eta s_j\) of the support of \(g_j\). Since \(s_j/R_j\to0\), for all sufficiently large \(j\) this support lies in \(R_j/4\leq|x|\leq4R_j\). Thus only a uniformly bounded number of large-index terms can be nonzero at a given point. The remaining terms have compact support. The sum is locally finite and smooth.

For \(q=|\alpha|\leq K\), move all derivatives onto \(g_j\) in the convolution, obtaining

\[
 \|\partial^\alpha h_j\|_\infty
 \leq C_\alpha R_j^{-\varepsilon-q}.
\]

For \(q>K\), choose \(\gamma\leq\alpha\) with \(|\gamma|=K\) and move the remaining derivatives onto the kernel. Then

\[
 \|\partial^\alpha h_j\|_\infty
 \leq C_\alpha R_j^{-\varepsilon-K}s_j^{K-q}
 =C_\alpha R_j^{-1-\varepsilon+b-\rho q}.
\]

These bounds are stronger than the asserted ones: \(\varepsilon>b\) in the low-order range, and \(1+\varepsilon-b+\rho q>1+\rho q\) in the high-order range. Finite overlap and \(R_j\asymp\langle x\rangle\) on the large supports give the global bounds.

Set \(f_S=\sum_j(g_j-h_j)\). Taylor-expand \(g_j(x-s_jy)\) at \(x\) through degree \(K-1\). Every positive-degree term disappears after integration against \(\eta\), and the constant term cancels \(g_j(x)\). The integral remainder is bounded by

\[
 C s_j^K\max_{|\alpha|=K}\|\partial^\alpha g_j\|_\infty
 \leq C R_j^{\rho K-K-\varepsilon}
 =C R_j^{-1-\varepsilon+b}.
\]

The finitely many small indices satisfy the same conclusion with a larger constant, because their differences have compact support. Finite overlap proves the bound for \(f_S\). The partition identity gives \(f_S+f_L=f\). Real cutoffs and a real kernel preserve reality. Finally the slopes of \(M\) are one up to \(K\) and \(\rho<1\) afterwards, proving concavity and monotonicity. \(\square\)

This theorem controls the remainder itself. It does not assert all-derivative estimates on \(f_S\), which still has only the original \(C^K\) regularity. For a differential perturbation it is applied to each coefficient separately.

**Example 2.2.** Let \(K=2\), \(\varepsilon=3/5\), and choose \(b=1/3\). Then \(\rho=2/3\), the remainder is \(O(\langle x\rangle^{-19/15})\), and the smooth part satisfies orders \(M(0)=1/3\), \(M(1)=4/3\), \(M(2)=7/3\), \(M(3)=3\), and \(M(4)=11/3\). The decrease in slope after the second derivative records the finite number of derivatives originally available. It cannot be replaced without proof by the bound \(b+q\) at every order.

<a id="coefficient-extra-derivative"></a>
**Corollary 2.3 (one more derivative with full decay).** Suppose the hypotheses of Theorem 2.1 hold and \(\varepsilon>1/(K+1)\). Choose

\[
 \frac1{K+1}<b<\varepsilon,
 \qquad
 \sigma=\frac{(K+1)b-1}{K}>0,
 \qquad \varepsilon_1=\min(b,\sigma)>0.
\]

The resulting smooth part satisfies

\[
 |\partial^\alpha f_L(x)|
 \leq C_\alpha\langle x\rangle^{-|\alpha|-\varepsilon_1}
 \qquad(|\alpha|\leq K+1).
\]

Thus it belongs to the same finite-regularity class with \(K\) replaced by \(K+1\), allowing a smaller positive decay exponent. The short-range remainder retains the exponent \(\varepsilon-b>0\).

**Proof.** For \(q\leq K\), Theorem 2.1 gives \(M(q)=q+b\geq q+\varepsilon_1\). At the new order,

\[
 M(K+1)-(K+1)
 =1+\frac{K-1+b}{K}(K+1)-(K+1)
 =\sigma\geq\varepsilon_1.
\]

These are exactly all the claimed estimates. The theorem's remainder bound is unchanged. If a later argument needs the regime \(\varepsilon\leq1/(K+1)\), one may simply lower the chosen positive exponent to that threshold; the original inequalities remain true. If it needs an extra controlled derivative, the promotion above supplies it with its explicitly stated exponent. These are two separate permissible uses of the estimate. \(\square\)

**Example 2.4.** Take \(K=2\), \(\varepsilon=3/5\), and now \(b=1/2\). Then \(\rho=3/4\), \(M(3)=13/4\), and \(\varepsilon_1=1/4\). The smooth part has full decay through order three, while the remainder is \(O(\langle x\rangle^{-11/10})\). The choice \(b=1/3\) in Example 2.2 sits at the threshold and gives \(M(3)=3\), so it does not establish a positive extra decay exponent at order three.

## 3. Products with a derivative budget

The next estimates use a parameter \(T\geq1\). A sequence \(a(0),a(1),\ldots\) is convex if its successive differences are nondecreasing. Linear interpolation makes it a convex function between integer arguments.

<a id="coefficient-product-budget"></a>
**Lemma 3.1.** Suppose, at a fixed point, that

\[
 |\partial^\alpha f|\leq A_\alpha T^{a(|\alpha|)},\qquad
 |\partial^\alpha g|\leq B_\alpha T^{b(|\alpha|)},
\]

where \(a,b\) are convex sequences. Then

\[
 |\partial^\gamma(fg)|\leq C_\gamma T^{c(|\gamma|)},\qquad
 c(q)=\max\{a(q)+b(0),a(0)+b(q)\}.
\]

One can take \(C_\gamma=2^{|\gamma|}\max_{\alpha\leq\gamma}A_\alpha B_{\gamma-\alpha}\).

**Proof.** The product rule has binomial coefficients whose sum is \(2^{|\gamma|}\). A term with \(|\alpha|=r\) has exponent \(a(r)+b(q-r)\), a convex function of \(r\in[0,q]\). Its maximum is at an endpoint. Since \(T\geq1\), replacing each exponent by that maximum increases its bound. Sum the coefficients. \(\square\)

Applied to powers of distance, the exponents are often negative. Convexity still applies; the sign does not reverse the endpoint rule because the base \(T\) is at least one.

## 4. Compositions and their inverses

Let \(\psi:\mathbb R^{n'}\to\mathbb R^n\) be smooth near a point \(x\). Bounds on its derivatives begin at order one; \(\psi(x)\) itself need not be bounded. The convex-exponent composition estimate and inverse estimate are discussed in [HW], Lemma 3.6 and the following remark, pp. 79–80.

<a id="coefficient-local-inverse"></a>
The local inverse fact needed when the dimensions agree has the following proof. Suppose \(B=\psi'(x_0)\) is invertible. By continuity choose a closed ball of radius \(r>0\) about \(x_0\), contained in the domain, on which \(\|I-B^{-1}\psi'(x)\|\le1/2\). If \(\|B^{-1}(y-\psi(x_0))\|<r/2\), the map \(F_y(x)=x+B^{-1}(y-\psi(x))\) sends the ball into itself and has Lipschitz constant at most \(1/2\), by integrating its derivative along segments. Starting at \(x_0\), its iterates have successive differences bounded by a geometric series. Completeness of the closed ball gives a fixed point, and the same Lipschitz estimate gives uniqueness. For two target points, subtract the fixed-point equations to obtain \(\|\phi(y)-\phi(z)\|\le2\|B^{-1}\|\|y-z\|\).

All nearby derivative matrices are invertible: the finite sums of powers of \(I-B^{-1}\psi'(x)\) converge geometrically, and multiplying the finite sums by \(B^{-1}\psi'(x)\) leaves the identity minus a power tending to zero. The preceding Lipschitz bound and the first-order expansion at \(x=\phi(y)\) now give

\[
 \phi(y+k)-\phi(y)=\psi'(\phi(y))^{-1}k+o(|k|).
\]

Thus the inverse is \(C^1\). Matrix inversion is smooth on the set of invertible matrices, directly from the cofactor formula with its nonzero determinant denominator. Induction in \(\phi'= (\psi'\circ\phi)^{-1}\) proves smoothness of the inverse whenever \(\psi\) is smooth. This proves the local inverse assertion used in the theorem and exercises, without a separate inverse-function prerequisite.

<a id="coefficient-composition-budget"></a>
**Theorem 4.1.** Suppose

\[
 |\partial^\alpha\psi(x)|\leq A_\alpha T^{a(|\alpha|)}\quad(|\alpha|\geq1),
\]

with a convex sequence \(a\). In the chain-rule expansion

\[
 \partial^\gamma(f\circ\psi)(x)
 =\sum_{1\leq|\beta|\leq q}
      (\partial^\beta f)(\psi(x))\,P_{\gamma,\beta}(x),
 \qquad q=|\gamma|>0,
\]

the coefficients satisfy

\[
 |P_{\gamma,\beta}(x)|
 \leq C_\gamma T^{(|\beta|-1)a(1)+a(q-|\beta|+1)}.
\]

If additionally \(|\partial^\beta f(\psi(x))|\leq B_\beta T^{b(|\beta|)}\) for a convex sequence \(b\), then

\[
 |\partial^\gamma(f\circ\psi)(x)|
 \leq C'_\gamma T^{\max\{b(q)+qa(1),\ b(1)+a(q)\}}.
\]

**Proof.** Repeated chain rules express a coefficient with \(|\beta|=j\) as a finite sum of products of \(j\) derivatives of components of \(\psi\). Their orders \(k_1,\ldots,k_j\) are positive integers with sum \(q\). For any two orders greater than one, shifting one unit from the smaller to the larger cannot decrease the sum of a convex sequence. Repetition puts \(j-1\) orders at one and the remaining order at \(q-j+1\). Thus

\[
 \sum_{\ell=1}^ja(k_\ell)\leq(j-1)a(1)+a(q-j+1).
\]

The finite number of chain-rule coefficients depends only on \(\gamma\), the dimensions and the derivative constants through order \(q\). This proves the first bound. After multiplying by the \(f\) derivative, the exponent is

\[
 b(j)+(j-1)a(1)+a(q-j+1).
\]

It is convex in \(j\in[1,q]\). Its endpoint values are \(b(1)+a(q)\) and \(b(q)+qa(1)\). Summing the finitely many terms proves the second estimate. \(\square\)

**Corollary 4.2.** If \(a(1)\leq0\) and \(a(q)\leq b(q)-b(1)\) for \(q\geq1\), then the composition has the same order-\(q\) bound \(T^{b(q)}\).

**Proof.** Both endpoint exponents in Theorem 4.1 are at most \(b(q)\). \(\square\)

<a id="coefficient-inverse-budget"></a>
**Theorem 4.3.** Assume the forward derivative bounds \(|\partial^\alpha\psi(x)|\leq A_\alpha T^{a(|\alpha|)}\), \(|\alpha|\geq1\), from Theorem 4.1, with \(a\) convex and \(a(1)=0\). Let \(\psi\) be a local diffeomorphism at \(x\). Suppose its derivative inverse has norm at most \(L\). For \(\phi=\psi^{-1}\), at \(y=\psi(x)\),

\[
 |\partial^\gamma\phi(y)|\leq C_\gamma T^{a(|\gamma|)}\qquad(|\gamma|\geq1),
\]

with constants depending only on \(L\), the dimensions and the derivative bounds for \(\psi\) through the indicated order.

**Proof.** At first order \(\phi'(y)=\psi'(x)^{-1}\), giving the assertion because \(T^{a(1)}=1\). Suppose it has been proved below order \(q\). Differentiate \(\psi\circ\phi=\operatorname{id}\) to order \(q\). One term is \(\psi'(x)\partial^\gamma\phi(y)\). Every other term contains a derivative of \(\psi\) of order \(j\geq2\), and \(j\) derivatives of \(\phi\) of positive orders \(k_1,\ldots,k_j<q\) whose sum is \(q\).

The exponent is bounded by \(a(j)+\sum a(k_\ell)\). The preceding convexity argument gives \(\sum a(k_\ell)\leq a(q-j+1)\), since \(a(1)=0\). Also

\[
 a(j)+a(q-j+1)\leq a(q).
\]

To verify the last inequality without a sign assumption, write \(d_r=a(r+1)-a(r)\). Then \(a(j)=\sum_{r=1}^{j-1}d_r\), whereas \(a(q)-a(q-j+1)=\sum_{r=q-j+1}^{q-1}d_r\). The second sum has the same number of terms, each with an index at least as large, so convexity bounds the first by the second. Multiplying the differentiated identity by \(\psi'(x)^{-1}\) finishes the induction. \(\square\)

The bound on the inverse first derivative is necessary. For the map \(\psi_T(x)=T^{-1}x\), the derivative of the inverse is \(T\). Even perfect bounds on the higher derivatives of \(\psi_T\) cannot replace that missing hypothesis.

<a id="coefficient-integrable-remainder"></a>
## 5. Why the remainder is short range

The elementary coefficient condition \(|f_S(x)|\leq C\langle x\rangle^{-1-\delta}\), \(\delta=\varepsilon-b>0\), has a direct dynamical consequence. Along a straight ray \(x=tv\), \(v\ne0\), its absolute value is integrable for \(t\geq1\):

\[
 \int_1^\infty|f_S(tv)|\,dt
 \leq C\int_1^\infty\langle tv\rangle^{-1-\delta}\,dt<\infty.
\]

The original coefficient need not have that property. For example \(\langle tv\rangle^{-\varepsilon}\), \(0<\varepsilon<1\), has an integral growing like \(t^{1-\varepsilon}\). This is why the smooth part contributes to the modifier in a long-range wave operator while the remainder is estimated as an integrable error. Constructing such a modifier requires additional Hamiltonian and operator estimates; the coefficient decomposition alone is not an existence theorem for wave operators.

### Use the conclusion

Track one Taylor remainder through the chosen smoothing radius, then check the joining derivative index in the final bounds. Use the resulting split when reading the coefficient hypotheses of Admissible differential perturbations.

<a id="coefficient-exercises"></a>
## 6. Exercises

**Exercise 6.1 (foundation).** With \(K=1\), \(\varepsilon=3/4\), \(b=1/4\), compute the smoothing scale, the remainder decay and the first four values of \(M\). Explain why \(s_j/R_j\to0\). Then choose \(b=5/8\) instead and compute the promoted order-two decay exponent and the new remainder decay.

**Exercise 6.2 (intermediate).** In dimension one, start from a smooth kernel \(\theta\) of integral one with nonzero first and second moments. Construct a kernel with zero moments of orders one and two using scales \(1,2,3\).

**Exercise 6.3 (intermediate).** For \(a(q)=q^2\) and \(b(q)=2q^2-3\), compute the exponent in Lemma 3.1 for \(q=4\). Compare it with the exponents for each split \(r=0,1,2,3,4\).

**Exercise 6.4 (advanced).** Let \(\psi_T(x)=x+T^{-1}\sin x\) on \(\mathbb R\), \(T\geq2\). Show that its inverse has uniformly bounded derivatives of every fixed order. Specify an exponent sequence to which Theorem 4.3 applies.

**Exercise 6.5 (advanced).** A proposed smoothing uses a fixed scale \(s_j=1\). Determine the remainder decay from the same Taylor argument. Explain why this does not give the high-derivative decay of Theorem 2.1.

## 7. Complete solutions

**Solution 6.1.** Here \(\rho=b=1/4\), so \(s_j=R_j^{1/4}\). The remainder is \(O(\langle x\rangle^{-3/2})\). The sequence is \(M(0)=1/4\), \(M(1)=5/4\), \(M(2)=3/2\), \(M(3)=7/4\). The two formulas at order one both give \(5/4\). The ratio \(s_j/R_j=R_j^{-3/4}\) tends to zero, giving the support overlap used in the proof. With \(b=5/8\), the new slope is \(\rho=5/8\), the remainder exponent is \(1+3/4-5/8=9/8\), and \(M(2)=1+2(5/8)=9/4\). Corollary 2.3 gives \(\sigma=2b-1=1/4\) and \(\varepsilon_1=1/4\), proving full decay through order two with that exponent.

**Solution 6.2.** Solve \(c_1+c_2+c_3=1\), \(c_1+2c_2+3c_3=0\), \(c_1+4c_2+9c_3=0\). The answer is \((3,-3,1)\). Thus

\[
 \eta(y)=3\theta(y)-\tfrac32\theta(y/2)+\tfrac13\theta(y/3).
\]

Each scaled term has the stated total mass after including its scaling factor. The first moment is multiplied by \(3-6+3=0\), and the second by \(3-12+9=0\). The mass is \(3-3+1=1\). The kernel may change sign, which is expected.

**Solution 6.3.** The endpoint exponents are \(a(4)+b(0)=16-3=13\) and \(a(0)+b(4)=32-3=29\), so the bound uses \(T^{29}\). For splits \(r=0,1,2,3,4\), the values of \(r^2+2(4-r)^2-3\) are \(29,16,9,8,13\). Their maximum is indeed the endpoint 29. Negative zeroth-order exponents cause no problem.

**Solution 6.4.** The first derivative is \(1+T^{-1}\cos x\in[1/2,3/2]\); hence the map is strictly increasing, tends to both infinities at the corresponding ends and has an inverse with derivative bounded by two. All its derivatives of order at least two are bounded by \(1/T\leq1/2\). Use the constant sequence \(a(q)=0\) for \(q\geq1\), which is convex with \(a(1)=0\). Theorem 4.3 gives a bound independent of \(T\) and the point for each fixed order. The constants can depend on that order. This also proves smoothness of the inverse globally by overlapping local inverse charts.

**Solution 6.5.** Taylor cancellation would give \(g_j-h_j=O(R_j^{-K-\varepsilon})\), which is a faster remainder. For \(q>K\), however, all remaining derivatives fall on a kernel at scale one, giving only \(\partial^\alpha h_j=O(R_j^{-K-\varepsilon})\), independent of \(q\). The growing scale in Theorem 2.1 deliberately weakens the remainder to gain an additional factor \(R_j^{-\rho(q-K)}\) for high derivatives. It is the balance between those two requirements that fixes \(\rho\).

## References

- [Y] Dmitri Yafaev, notes prepared by Andrew Hassell, *Lectures on scattering theory*, 2004, [arXiv:math/0403213](https://arxiv.org/abs/math/0403213), Section 3, pp. 12–13, for the long-range scattering setting. The coefficient regularization used here is proved in Section 2 above.

- [HW] Lars Hörmander, *The existence of wave operators in scattering theory*, Mathematische Zeitschrift **146** (1976), 69–91. [Freely readable journal scan](https://gdz.sub.uni-goettingen.de/download/pdf/PPN266833020_0146/LOG_0012.pdf), Lemmas 3.2–3.3, pp. 76–78, and Lemma 3.6 with its inverse-function remark, pp. 79–80, for regularization and convex-exponent derivative estimates.
