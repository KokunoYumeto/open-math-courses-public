# Admissible differential perturbations

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

**Working question: How can a rough full-order perturbation be split without losing symmetry?** The differential order of a coefficient and its decay at infinity play different roles. A full-order term needs controlled derivatives, while lower-order coefficients can be measured by local integral norms. Smoothing individual coefficients without respecting the formal adjoint can change the operator's symmetry, so the split is made at the expression level.

A differential perturbation can change the highest derivatives, contain unbounded lower-order coefficients, and still become small far from the origin. The appropriate size of a lower-order coefficient depends on the number of derivatives available to multiply it. A long-range splitting introduces a second issue: real coefficients give a real classical symbol, whereas symmetry of the differential operator depends on its ordering.

This lesson gives the coefficient conditions, proves their global mapping consequences, and constructs both the real-symbol and symmetric splittings. Read [Polynomial localizations and rough coefficients](polynomial-localizations-and-rough-coefficients.md) for the exact Sobolev estimates, and [Regularizing long-range coefficients](long-range-coefficient-calculus.md) for the smoothing theorem. The free primary coefficient-smoothing proof is Hörmander [HW], Lemma 3.3. The expression-level adjoint calculation is proved below. [Approximation, convolution and integer Sobolev density](../providers/analysis/euclidean-approximation-and-convolution.md) supplies the exact Hölder, density, convolution and translation facts used with those proofs; its [Proposition 5.1](../providers/analysis/euclidean-approximation-and-convolution.md#oscillatory-integrals-and-averages) proves the oscillatory-integral limit in Solution 6.3.

Throughout, \(n,m\geq1\) are integers,
\(D_j=-i\partial_j\), and \(\langle x\rangle=(1+|x|^2)^{1/2}\).
The \(H^m(\mathbb R^n)\) norm is
\(\|\langle D\rangle^m u\|_2\), using the unitary Fourier transform.
Our \(L^2\) inner product is linear in the first variable.

## 1. Choosing a coefficient exponent

For a term \(a(x)D^\alpha\) of order \(|\alpha|<m\), put
\(k=m-|\alpha|>0\). Choose the finite coefficient exponent \(p_\alpha\) by

\[
 p_\alpha=
 \begin{cases}
 n/k,&n>2k,\\
 \text{any fixed }p>2,&n=2k,\\
 2,&n<2k.
 \end{cases}
 \tag{1}
\]

The corresponding exponent for the differentiated function is

\[
 q_\alpha=
 \begin{cases}
 2n/(n-2k),&n>2k,\\
 2p_\alpha/(p_\alpha-2),&n=2k,\\
 \infty,&n<2k.
 \end{cases}
 \qquad
 \frac12=\frac1{p_\alpha}+\frac1{q_\alpha}.
 \tag{2}
\]

Different critical terms may use different fixed exponents. An essentially bounded coefficient satisfies every finite local exponent on a unit ball.

<a id="admissible-local-multiplier"></a>
**Lemma 1.1.** For every measurable \(a\), every \(y\in\mathbb R^n\), and every \(u\in C_c^\infty(B(y,1))\),

\[
 \|aD^\alpha u\|_2
 \leq C_{\alpha,n,m,p_\alpha}
       \|a\|_{L^{p_\alpha}(B(y,1))}\|u\|_{H^m}.
 \tag{3}
\]

The constant is independent of \(a,y,u\). An infinite coefficient norm makes the assertion vacuous.

**Proof.** Apply equation (13) of [Polynomial localizations and rough coefficients](polynomial-localizations-and-rough-coefficients.md#localization-sobolev) to \(D^\alpha u\), with derivative gap \(k\). Translation leaves its constant unchanged. The Fourier inequality
\(|\xi^\alpha|\langle\xi\rangle^k\leq\langle\xi\rangle^m\) gives

\[
 \|D^\alpha u\|_{L^{q_\alpha}(B(y,1))}
       \leq C\|D^\alpha u\|_{H^k}
       \leq C\|u\|_{H^m}.
 \tag{4}
\]

Hölder's inequality with (2) proves (3). The product vanishes outside the ball, since \(D^\alpha u\) does. \(\square\)

The finite endpoint \(p_\alpha=n/k>2\) is included. At \(n=2k\), the Sobolev estimate gives every fixed finite \(q_\alpha\), which explains the strict condition \(p_\alpha>2\). The critical \(L^2\) multiplication obstruction has the complete compactly supported proof in [The critical two-dimensional multiplication obstruction](../providers/analysis/critical-multiplication.md#critical-multiplication).

For highest-order terms the bound is instead immediate:

\[
 \|aD^\alpha u\|_2
       \leq\|a\|_{L^\infty(B(y,1))}\|u\|_{H^m},
       \qquad |\alpha|=m.
 \tag{5}
\]

## 2. Local norms and a global operator

Define the translated coefficient size by

\[
 A_\alpha(y)=
 \begin{cases}
 \displaystyle\sup_{x\in B(y,1)}|a_\alpha(x)|,
                                      &|\alpha|=m,\\
 \|a_\alpha\|_{L^{p_\alpha}(B(y,1))},
                                      &|\alpha|<m.
 \end{cases}
 \tag{6}
\]

For the first row we assume continuity. Thus its supremum agrees with its essential supremum.

<a id="admissible-global-mapping"></a>
**Proposition 2.1.** Suppose
\(V=\sum_{|\alpha|\leq m}a_\alpha D^\alpha\), the highest-order coefficients are continuous, the lower-order coefficients have the local integrability in (1), and every \(A_\alpha\) is bounded. Then \(V\) extends uniquely to a bounded map \(H^m\to L^2\), and

\[
 \|Vu\|_2
       \leq C\Bigl(\sum_{|\alpha|\leq m}\sup_y A_\alpha(y)\Bigr)
             \|u\|_{H^m}.
 \tag{7}
\]

Moreover, for \(R\geq2\),

\[
 \|1_{\{|x|>R\}}Vu\|_2
 \leq C\Bigl(\sum_{|\alpha|\leq m}
                   \sup_{|y|>R-1/2}A_\alpha(y)\Bigr)\|u\|_{H^m}.
 \tag{8}
\]

**Proof.** Choose a fixed real \(\chi\in C_c^\infty(B(0,1))\) that equals one on \(B(0,1/2)\), and set \(\chi_y(x)=\chi(x-y)\). For an integer Sobolev order, Plancherel makes the norm equivalent to the square sum of derivative norms through order \(m\). The product rule and Fubini therefore give

\[
 \int_{\mathbb R^n}\|\chi_yu\|_{H^m}^2\,dy
       \leq C_\chi\|u\|_{H^m}^2.
 \tag{9}
\]

Indeed, each product-rule term is
\((D^\beta\chi)(x-y)D^\gamma u(x)\), with
\(|\beta|+|\gamma|\leq m\). Its squared integral in \(x,y\) is
\(\|D^\beta\chi\|_2^2\|D^\gamma u\|_2^2\). The finite sum bounds (9).

On \(B(y,1/2)\), the derivatives of \(\chi_yu\) equal those of \(u\). Equations (3) and (5) imply

\[
 \int_{B(y,1/2)}|a_\alpha D^\alpha u|^2\,dx
       \leq C A_\alpha(y)^2\|\chi_yu\|_{H^m}^2.
 \tag{10}
\]

Integrate in \(y\). Each \(x\) belongs to a set of centers of volume
\(|B(0,1/2)|\); (9) proves the bound for one term. Sum its norms over the finite family of multiindices to obtain (7).

For (8), restrict the left integral of (10) to \(|x|>R\). A contributing center satisfies \(|y|>R-1/2\). Fubini, followed by (9), gives the stated tail bound by the same argument.

These estimates initially apply to compact smooth inputs. Such inputs are dense in \(H^m\), so (7) gives a unique bounded extension and (8) persists. Its value is the actual coefficient product: after multiplying an approximating sequence by a fixed cutoff, (4) gives convergence of each lower derivative in its required local \(L^{q_\alpha}\) norm. Hölder then identifies its product with \(a_\alpha\) in local \(L^2\). For highest derivatives, local boundedness of the continuous coefficient gives the same identification. Thus the extension has its claimed differential expression. \(\square\)

The useful extra information in (8) is smallness of the **output** at infinity. This conclusion also holds without a power rate whenever \(A_\alpha(y)\to0\).

## 3. The admissible class

Let \(P_0(D)\) be a scalar, formally self-adjoint, constant-coefficient elliptic operator of order \(m\). Its polynomial \(P_0(\xi)\) is real for real \(\xi\).

<a id="admissible-coefficient-class"></a>
**Definition 3.1.** A differential operator

\[
 V(x,D)=\sum_{|\alpha|\leq m}a_\alpha(x)D^\alpha
 \tag{11}
\]

has coefficient short range if its coefficients are measurable, continuous when \(|\alpha|=m\), and, for some \(\delta>0\),

\[
 \begin{aligned}
 |a_\alpha(x)|&\leq C\langle x\rangle^{-1-\delta},
                                  &&|\alpha|=m,\\
 \|a_\alpha\|_{L^{p_\alpha}(B(y,1))}
              &\leq C\langle y\rangle^{-1-\delta},
                                  &&|\alpha|<m.
 \end{aligned}
 \tag{12}
\]

This definition concerns the differential coefficients through order \(m\). The earlier compact endpoint condition in [Short-range compactness and local tests](short-range-compactness-and-local-tests.md) is a separate operator condition.

For an integer \(K\geq1\), call \(V\) **\(K\)-admissible relative to \(P_0\)** if:

- its full differential expression is symmetric on \(C_c^\infty\);
- \(P_0+V\) is elliptic;
- it has a splitting \(V=V_S+L\), where \(V_S\) has coefficient short range and
  \(L=\sum_{|\alpha|\leq m}\ell_\alpha D^\alpha\) has real \(C^K\) coefficients satisfying, for some \(\varepsilon>0\),

\[
 |D^\beta\ell_\alpha(x)|
       \leq C_{\alpha,\beta}\langle x\rangle^{-\varepsilon-|\beta|},
       \qquad |\beta|\leq K.
 \tag{13}
\]

Symmetry means
\((Vu,v)=(u,Vv)\) for all compact smooth \(u,v\). It is a condition on the whole expression; neither summand of this real-coefficient splitting is required to be symmetric.

**Corollary 3.2.** Every coefficient-short-range operator is bounded \(H^m\to L^2\), with

\[
 \|1_{\{|x|>R\}}Vu\|_2
       \leq C R^{-1-\delta}\|u\|_{H^m},
       \qquad R\geq2.
 \tag{14}
\]

Every \(K\)-admissible \(V\) is also bounded \(H^m\to L^2\). If \(V\) is symmetric on compact smooth functions, then \(P_0+V\), with domain \(H^m\), is a densely defined symmetric operator.

**Proof.** Points in a unit ball about \(y\) have
\(\langle x\rangle\) comparable with \(\langle y\rangle\), uniformly in \(y\). Thus (12) bounds all sizes (6), including highest-order ones, by \(C\langle y\rangle^{-1-\delta}\). Apply Proposition 2.1. A long-range coefficient in (13) is bounded and belongs to every required local finite \(L^p\) space with a bounded translated norm, so Proposition 2.1 also applies to \(L\). Finally \(P_0:H^m\to L^2\) is bounded. Approximation by compact smooth inputs passes symmetry to its full domain, which is dense in \(L^2\). \(\square\)

Identifying the adjoint domain with \(H^m\) requires an elliptic domain argument beyond this mapping result.

**Example 3.3.** In three dimensions, a zeroth-order term in an order-two problem uses \(p_0=2\), whereas a first-order term uses \(p_\alpha=3\). Consequently, a locally \(L^2\) potential may be unbounded and still satisfy (12). Exercise 6.2 constructs a real short-range potential whose peak heights tend to infinity.

A highest-order short-range coefficient can also alter the local principal symbol. It must retain ellipticity in the admissible class. Its compact support alone does not make the map \(H^m\to L^2\) compact; Exercise 6.3 displays the high-frequency obstruction.

## 4. A smooth real-symbol splitting

The regularization theorem allows all derivatives of the long-range coefficients to be used, with a precise loss at high orders.

<a id="admissible-regularization"></a>
**Theorem 4.1.** Suppose \(V\) is \(K\)-admissible and has the splitting above. After replacing \(\varepsilon\), if necessary, by a smaller number in \((0,1)\), choose \(0<b<\varepsilon\). Then

\[
 V=\widetilde V_S+\widetilde L
 \tag{15}
\]

where \(\widetilde V_S\) has coefficient short range,
\(\widetilde L=\sum\widetilde\ell_\alpha D^\alpha\) has real smooth coefficients, and

\[
 \begin{aligned}
 |D^\beta\widetilde\ell_\alpha(x)|
       &\leq C_{\alpha,\beta}\langle x\rangle^{-M(|\beta|)},\\
 M(q)&=
 \begin{cases}
 b+q,&0\leq q\leq K,\\
 1+\rho q,&q\geq K,
 \end{cases}
 \qquad
 \rho=\frac{K-1+b}{K}\in(0,1).
 \end{aligned}
 \tag{16}
\]

One may take the new short-range decay exponent
\(\min(\delta,\varepsilon-b)>0\).

**Proof.** Apply Theorem 2.1 of [Regularizing long-range coefficients](long-range-coefficient-calculus.md#coefficient-dyadic-regularization) separately to each real \(\ell_\alpha\). It supplies real smooth \(\widetilde\ell_\alpha\) with (16), and

\[
 |\ell_\alpha(x)-\widetilde\ell_\alpha(x)|
       \leq C_\alpha\langle x\rangle^{-1-\varepsilon+b}.
 \tag{17}
\]

Add \(\sum(\ell_\alpha-\widetilde\ell_\alpha)D^\alpha\) to \(V_S\). For a highest-order coefficient (17) is the required pointwise bound, and its continuity persists. For a lower-order coefficient, unit-ball comparability and the ball's fixed volume turn (17) into the required local \(L^{p_\alpha}\) bound. Adding it to (12) gives the minimum exponent. The differential expression itself is unchanged, hence its symmetry and ellipticity persist. \(\square\)

The sequence \(M\) is increasing, \(M(1)=1+b\), and
\(M(q)\geq1+b\) for every integer \(q\geq1\). These facts will make every ordering correction short range.

The real polynomial
\(\sum\widetilde\ell_\alpha(x)\xi^\alpha\) is convenient for Hamiltonian equations. Its left-ordered differential operator can still fail to be symmetric.

## 5. A symmetric splitting with the same decay budget

<a id="admissible-formal-adjoint"></a>
For smooth coefficients, integration by parts on compact tests gives the following identities, where the star denotes the formal adjoint

\[
 \left(\sum_\alpha \widetilde\ell_\alpha D^\alpha\right)^*
   =\sum_\alpha D^\alpha\overline{\widetilde\ell_\alpha}
   =\sum_\alpha\sum_{\beta\leq\alpha}
       {\alpha\choose\beta}
       (D^{\alpha-\beta}\overline{\widetilde\ell_\alpha})D^\beta.
 \tag{18}
\]

In the middle expression \(D^\alpha\overline{\widetilde\ell_\alpha}\) denotes operator composition with multiplication; the last expression is its coefficient expansion.

<a id="admissible-symmetric-split"></a>
**Theorem 5.1.** With the real smooth splitting of Theorem 4.1, put

\[
 L_{\mathrm{sym}}=\frac{\widetilde L+\widetilde L^*}{2},
 \qquad
 S_{\mathrm{sym}}=\widetilde V_S+
                         \frac{\widetilde L-\widetilde L^*}{2}.
 \tag{19}
\]

Then \(V=L_{\mathrm{sym}}+S_{\mathrm{sym}}\), both summands are symmetric on compact tests, \(S_{\mathrm{sym}}\) has coefficient short range, and the coefficients of \(L_{\mathrm{sym}}\) satisfy every bound in (16). The highest-order coefficients of \(L_{\mathrm{sym}}\) are exactly those of \(\widetilde L\); lower-order coefficients may be complex. The short-range exponent can be chosen as

\[
 \delta_{\mathrm{sym}}
       =\min(\delta,\varepsilon-b,b)>0.
 \tag{20}
\]

**Proof.** Since the coefficients of \(\widetilde L\) are real, the terms with \(\beta=\alpha\) in (18) cancel in
\(\widetilde L^*-\widetilde L\). Every remaining coefficient contains at least one derivative of a long-range coefficient. It therefore has order at most \(m-1\) and obeys

\[
 |D^{\alpha-\beta}\widetilde\ell_\alpha(x)|
       \leq C\langle x\rangle^{-M(|\alpha-\beta|)}
       \leq C\langle x\rangle^{-1-b},
       \qquad \beta<\alpha.
 \tag{21}
\]

Finite sums preserve the bound. Unit-ball comparability proves the short-range local norms for every such coefficient. Combining this with Theorem 4.1 gives (20).

A derivative of order \(q\) of an added coefficient involves a derivative of order \(q+|\alpha-\beta|\) of \(\widetilde\ell_\alpha\). Monotonicity of \(M\) gives

\[
 M(q+|\alpha-\beta|)\geq M(q).
 \tag{22}
\]

Thus the coefficients in the average \(L_{\mathrm{sym}}\) retain (16). The cancellation already observed shows its highest-order coefficients are unchanged.

The formal adjoint of \(L_{\mathrm{sym}}\) equals itself. Since \(V\) is symmetric and \(S_{\mathrm{sym}}=V-L_{\mathrm{sym}}\), subtraction of the compact-test inner-product identities proves symmetry of \(S_{\mathrm{sym}}\). This reasoning applies even when its other coefficients are merely measurable. Equation (19) proves the exact sum. \(\square\)

For a concrete ordering correction in one dimension,

\[
 (fD)^*=fD-i f',
 \qquad
 \frac{fD+(fD)^*}{2}=fD-\frac{i}{2}f',
 \tag{23}
\]

when \(f\) is real and smooth. The imaginary zeroth-order term ensures symmetry. Its extra derivative supplies the short-range decay.

<a id="admissible-weyl-split"></a>
**Theorem 5.2 (the Weyl alternative).** Let
\(\ell(x,\xi)=\sum_{|\alpha|\leq m}\widetilde\ell_\alpha(x)\xi^\alpha\)
be the real smooth polynomial from Theorem 4.1. Its Weyl operator \(L_w=\operatorname{Op}_{1/2}(\ell)\) is a differential operator, with exact expression

\[
 L_w=\sum_{|\alpha|\leq m}\sum_{\beta\leq\alpha}
       {\alpha\choose\beta}2^{-|\beta|}
       (D^\beta\widetilde\ell_\alpha)D^{\alpha-\beta}.
\]

It is symmetric on compact smooth tests, has the same highest-order coefficients as \(\widetilde L\), and all its coefficients retain (16). The splitting

\[
 V=L_w+S_w,\qquad
 S_w=\widetilde V_S+\widetilde L-L_w
\]

has symmetric summands; \(S_w\) has coefficient short range with exponent (20). It gives the same admissible operator with a real Weyl symbol for its long-range part.

**Proof.** We can verify the polynomial conversion directly. The Weyl kernel for one monomial is the distributional oscillatory integral

\[
 (2\pi)^{-n}\int e^{i(x-y)\cdot\xi}
       \widetilde\ell_\alpha((x+y)/2)\xi^\alpha\,d\xi.
\]

Use \(\xi^\alpha e^{i(x-y)\cdot\xi}=(-D_y)^\alpha e^{i(x-y)\cdot\xi}\), then integrate by parts against the input. The product rule differentiates the input \(\alpha-\beta\) times and the midpoint coefficient \(\beta\) times. Each midpoint derivative costs the factor \(2^{-1}\). Fourier inversion gives exactly

\[
 \sum_{\beta\leq\alpha}{\alpha\choose\beta}
        2^{-|\beta|}(D^\beta\widetilde\ell_\alpha)(x)
        D^{\alpha-\beta}u(x).
\]

This is a finite distribution identity, not a formal infinite expansion. It can first be tested on compact smooth inputs; the bounded smooth coefficients and their derivatives extend its action to Schwartz inputs. Summing over \(\alpha\) gives the stated exact differential expression. For comparison, [Lerner’s freely readable author chapter](https://webusers.imj-prg.fr/~nicolas.lerner/ch2booklerner.pdf), Theorems 2.3.18–2.3.19, printed p. 100, treats general changes of quantization and composition. Its kernel uses \(e^{2\pi i(x-y)\cdot\eta}\); the substitution \(\xi=2\pi\eta\) gives our convention. The finite polynomial kernel identity needed here was proved directly above, without using that general metric calculus as a prerequisite.

Reality of \(\ell\) makes the Weyl kernel equal to the complex conjugate of its transpose. Testing that distributional identity on two Schwartz inputs gives \(L_w^*=L_w\) on those tests. In the difference \(L_w-\widetilde L\), every term has \(|\beta|\geq1\), hence differential order at most \(m-1\). Its coefficient is bounded by
\(C\langle x\rangle^{-M(|\beta|)}\leq C\langle x\rangle^{-1-b}\).
The local \(L^{p_\alpha}\) short-range bounds follow from unit-ball comparability, exactly as in Theorem 5.1. After \(q\) extra coefficient derivatives, monotonicity gives \(M(q+|\beta|)\geq M(q)\), so all bounds (16) persist in \(L_w\). The terms with \(\beta=0\) show that the highest-order coefficients are unchanged. Combining the two short-range parts gives (20). Finally \(S_w=V-L_w\) is symmetric on compact tests by subtraction. Proposition 2.1 supplies the actual bounded \(H^m\)-to-\(L^2\) actions and density extends these symmetry identities to that domain. \(\square\)

For the order-two example in Solution 6.5, Weyl quantization gives

\[
 \operatorname{Op}_{1/2}(f(x)\xi^2)
 =fD^2-i f'D-\tfrac14 f'',
 \qquad
 DfD-\operatorname{Op}_{1/2}(f(x)\xi^2)=\tfrac14 f''.
\]

The symmetric-average splitting there instead has remainder \(f''/2\). Both remainders are short range; their different constants record the two ordering choices.

<a id="admissible-exterior-ellipticity"></a>
**Corollary 5.3 (an elliptic smooth part outside a large ball).** In the splitting of Theorem 4.1, the smooth long-range part can first be made zero on a large ball and then symmetrized so that \(P_0+L_{\mathrm{ext}}\) is uniformly elliptic. All coefficient bounds (16) remain valid, and

\[
 V=L_{\mathrm{ext}}+S_{\mathrm{ext}}
\]

still has symmetric summands, with coefficient-short-range \(S_{\mathrm{ext}}\). For \(K=1\), writing \(\delta=b\in(0,1)\), the smooth coefficients satisfy

\[
 |c_\alpha(x)|\leq C_\alpha\langle x\rangle^{-\delta},
 \qquad
 |D^\gamma c_\alpha(x)|\leq C_{\alpha\gamma}
                   \langle x\rangle^{-1-\delta|\gamma|}
 \quad(|\gamma|\geq1).
\]

**Proof.** Choose a real smooth \(\vartheta_R\) with \(0\leq\vartheta_R\leq1\), zero on \(|x|\leq R\), one on \(|x|\geq2R\), and with derivatives of order \(j\) bounded by \(C_jR^{-j}\), for \(R\geq1\). Put \(L_R=\vartheta_R\widetilde L\). The coefficient difference \(\widetilde L-L_R\) is smooth and compactly supported, hence coefficient short range with any fixed positive exponent, with constants allowed to depend on \(R\).

The product coefficients retain every bound (16). A term with \(j>0\) derivatives on the cutoff is supported in \(R\leq|x|\leq2R\) and has decay exponent \(j+M(q-j)\) at total derivative order \(q\). Both slopes of \(M\) lie between zero and one, so \(M(q)-M(q-j)\leq j\). Thus \(j+M(q-j)\geq M(q)\). Terms with no cutoff derivative use (16) directly. These estimates may be chosen uniformly for \(R\geq1\).

Now set \(L_{\mathrm{ext}}=(L_R+L_R^*)/2\). The coefficient-adjoint calculation of Theorem 5.1 applies unchanged: every added coefficient contains at least one derivative, decays at least as \(\langle x\rangle^{-1-b}\), and its further derivatives retain (16) by monotonicity of \(M\). The highest coefficients are precisely \(\vartheta_R\widetilde\ell_\alpha\), since these coefficients are real. The operator is symmetric, and \(S_{\mathrm{ext}}=V-L_{\mathrm{ext}}\) is symmetric by subtraction. Its three coefficient-short-range pieces are the remainder in Theorem 4.1, the compact coefficient difference just identified, and the adjoint correction. Their minimum positive exponent is (20). The bounded \(H^m\)-to-\(L^2\) actions and symmetry identities follow from Proposition 2.1 and density as before.

Let \(c_0=\min_{|\xi|=1}|p_m(\xi)|>0\). The finitely many highest \(\widetilde\ell_\alpha\) tend to zero at infinity. Choose \(R\) so large that

\[
 \sum_{|\alpha|=m}\sup_{|x|\geq R}
                 |\widetilde\ell_\alpha(x)|<c_0/2.
\]

On unit covectors the perturbation of \(p_m\) then has modulus less than \(c_0/2\) at every position; it is zero inside the ball and small outside. Homogeneity gives
\(|(P_0+L_{\mathrm{ext}})_m(x,\xi)|\geq(c_0/2)|\xi|^m\).
No positivity or fixed sign of \(p_m\) is required. Finally for \(K=1\), formula (16) is exactly \(M(0)=b\) and \(M(q)=1+bq\) for \(q\geq1\), giving the last displayed estimates. \(\square\)

### Use the conclusion

Check the top-derivative recovery and the joining regularity threshold, then verify the symmetric long-range/short-range decomposition. Retain the local exponent and every allowed differential order in the operator-domain application.

<a id="admissible-exercises"></a>
## 6. Exercises

**Exercise 6.1 (foundation).** For \(n=3,m=2\), give the coefficient and function exponents for zeroth- and first-order terms. Let \(\chi\) be smooth, equal to one near zero and supported in \(B(0,1/2)\). For \(s>0\), determine when \(\chi(x)|x|^{-s}\) belongs to each required coefficient space. At \(s=3/p\), determine the condition on \(\gamma>0\) for
\(\chi(x)|x|^{-3/p}(\log(e/|x|))^{-\gamma}\) to belong to \(L^p\).

**Exercise 6.2 (intermediate).** In \(\mathbb R^3\), fix a nonnegative nonzero
\(\phi\in C_c^\infty(B(0,1))\) with \(\phi(0)=1\). Put
\(R_j=4^j\), \(x_j=R_je_1\), \(r_j=R_j^{-2}\), and

\[
 a(x)=\sum_{j\geq1}R_j\,
                     \phi\bigl((x-x_j)/r_j\bigr).
 \tag{24}
\]

Show that \(a\) is smooth, is unbounded, and satisfies
\(\|a\|_{L^2(B(y,1))}\leq C\langle y\rangle^{-2}\).
Deduce that multiplication by \(a\) is a coefficient-short-range, \(K\)-admissible perturbation of \(-\Delta\) for every \(K\geq1\).

**Exercise 6.3 (advanced).** Let \(a\) be a nonzero smooth compactly supported function, and choose \(\phi\in C_c^\infty\) with \(a\phi\ne0\). For

\[
 u_N(x)=N^{-m}\phi(x)e^{iNx_1},
       \qquad N=1,2,\ldots,
 \tag{25}
\]

show that the sequence is bounded in \(H^m\), while
\(aD_1^m u_N\) has no strongly convergent subsequence in \(L^2\).
Explain the consequence for highest-order coefficient short range.

**Exercise 6.4 (intermediate).** In one dimension let
\(f(x)=\langle x\rangle^{-\varepsilon}\), \(0<\varepsilon<1\), and
\(P_0=D\). Prove that
\(V=fD-i f'/2\) is \(K\)-admissible for every \(K\geq1\).
Give its real-coefficient long-range splitting and check ellipticity of \(P_0+V\).

**Exercise 6.5 (advanced).** With the same \(f\), now take
\(P_0=D^2\), \(V=D f D\), and the real left-ordered long-range part \(L=fD^2\). Compute \(L^*\), its symmetric average, and the remaining short-range operator \(V-(L+L^*)/2\). Verify the signs and decay of every coefficient. For the general budget (16) with \(K=2,b=1/3\), give the first five values of \(M\) and the decay available for a correction involving three derivatives.

<a id="admissible-solutions"></a>
## 7. Complete solutions

**Solution 6.1.** A zeroth-order term has gap two. Since \(3<4\), its pair is
\(p_0=2,q_0=\infty\). A first-order term has gap one, and \(3>2\), so its pair is \(p_\alpha=3,q_\alpha=6\). Near zero, polar integration gives

\[
 \int_{|x|<c}|x|^{-sp}\,dx
       =|\mathbb S^2|\int_0^c r^{2-sp}\,dr.
 \tag{26}
\]

It is finite exactly when \(sp<3\). Thus the zeroth-order coefficient permits \(s<3/2\), and the first-order coefficient permits \(s<1\). At equality, the logarithmic example gives
\(\int_0^c r^{-1}(\log(e/r))^{-\gamma p}\,dr\).
Substitute \(t=\log(e/r)\); its convergence is exactly
\(\gamma p>1\). Hence the conditions are \(\gamma>1/2\) and \(\gamma>1/3\), respectively. These are local integrability conclusions; symmetry of a whole differential expression is an additional condition.

**Solution 6.2.** The supports escape every compact set, so the sum is locally finite and smooth. They are disjoint, and \(a(x_j)=R_j\to\infty\). A unit ball meets at most one support: the smallest gap between successive centers is twelve, whereas the support radii are at most \(1/16\). When the ball meets the \(j\)-th support, its center satisfies
\(|y-x_j|<1+r_j\), so \(\langle y\rangle\) is comparable with \(R_j\). A change of variables gives

\[
 \|R_j\phi((\,\cdot-x_j)/r_j)\|_2
       =R_j r_j^{3/2}\|\phi\|_2
       =R_j^{-2}\|\phi\|_2.
 \tag{27}
\]

This bounds the norm on that unit ball. If the ball meets no support, the norm is zero. Thus (12) holds with \(\delta=1\) for the sole zeroth-order coefficient in the order-two problem. Its required exponent is two, as in Solution 6.1.

Multiplication by the real \(a\) is symmetric on compact tests. It leaves the principal symbol \(|\xi|^2\) unchanged. Take \(V_S=a\) and \(L=0\); all long-range derivative conditions hold for every \(K\). Proposition 2.1 also proves the map \(H^2\to L^2\) is bounded despite the growing peaks.

<a id="admissible-high-frequency-obstruction"></a>
**Solution 6.3.** Differentiating (25) \(r\leq m\) times produces a finite sum with factors \(N^{j-m}\), \(j\leq r\). The other factors are fixed derivatives of \(\phi\) times a unit-modulus exponential. Every such norm is bounded, proving the \(H^m\) bound. More precisely,

\[
 aD_1^m u_N=a\phi e^{iNx_1}+e_N,
       \qquad \|e_N\|_2\leq C/N.
 \tag{28}
\]

The principal term converges weakly to zero: for any \(h\in L^2\), its pairing is a Fourier oscillatory integral of the \(L^1\) function \(a\phi\overline h\), which tends to zero by the Riemann–Lebesgue lemma. Its norm is the positive constant \(\|a\phi\|_2\). Hence the full sequence in (28) has weak limit zero and norms tending to that positive constant. Any strongly convergent subsequence would have limit zero by weak convergence, contradicting its norms.

The coefficient \(a\) has compact support and satisfies every power decay at infinity, yet \(aD_1^m:H^m\to L^2\) is not compact. Thus (12), when highest-order terms are permitted, cannot by itself be interpreted as a compactness assertion in this Sobolev graph norm. To put the same example inside an elliptic symmetric perturbation class, in dimension one and order two take a small nonnegative \(a\) and \(V=D a D\). Its leading symbol is \(a(x)\xi^2\); the lower-order term in \(V\) applied to \(u_N\) tends to zero, so the obstruction persists, while \(D^2+V\) remains elliptic.

**Solution 6.4.** Formula (23) makes \(V\) symmetric. Each derivative of \(f\) satisfies
\(|f^{(r)}(x)|\leq C_r\langle x\rangle^{-\varepsilon-r}\).
For completeness, write \(f=(1+x^2)^{-\varepsilon/2}\). Differentiation gives a finite sum of terms
\(c x^j(1+x^2)^{-\varepsilon/2-\ell}\) with
\(2\ell-j=r\). Differentiating either factor preserves the identity with \(r\) increased by one; the displayed decay follows from \(|x|\leq\langle x\rangle\).

Use the real long-range part \(L=fD\) and
\(V_S=-i f'/2\). In dimension one with \(m=1\), the lower coefficient exponent is two. The derivative bound and unit-ball comparability give its local \(L^2\) norm at most \(C\langle y\rangle^{-1-\varepsilon}\). Thus it is short range with \(\delta=\varepsilon\), and \(L\) satisfies (13) for every finite \(K\).

The principal symbol of \(D+V\) is
\((1+f(x))\xi\). Since \(f>0\), its absolute value is at least \(|\xi|\); ellipticity holds. The operator is therefore \(K\)-admissible for every \(K\). Its left-ordered long-range coefficient is real, while the imaginary short-range coefficient is required by symmetry.

**Solution 6.5.** The product rule gives

\[
 \begin{aligned}
 V&=fD^2+(Df)D=fD^2-i f'D,\\
 L^*&=D^2 f=fD^2+2(Df)D+D^2f,\\
 \frac{L+L^*}{2}
       &=fD^2-i f'D-\frac12 f'',\\
 V-\frac{L+L^*}{2}&=\frac12 f''.
 \end{aligned}
 \tag{29}
\]

The expression \(D^2 f\) in the second line denotes composition; its final expansion contains \(D^2f=-f''\). This fixes both signs in the last two lines. On compact tests
\((Vu,v)=(fDu,Dv)\), so \(V\) is symmetric. In the real-symbol splitting \(L=fD^2\), the remainder is
\((Df)D=-i f'D\), whose coefficient decays as
\(\langle x\rangle^{-1-\varepsilon}\). Both lower coefficient exponents here are two. The principal coefficient of \(D^2+V\) is \(1+f>0\), proving ellipticity.

Direct differentiation yields

\[
 f''(x)=\varepsilon\bigl((\varepsilon+1)x^2-1\bigr)
                      \langle x\rangle^{-\varepsilon-4}.
 \tag{30}
\]

Consequently the symmetric remainder \(f''/2\) decays as
\(\langle x\rangle^{-2-\varepsilon}\) and has the required local \(L^2\) short-range bound. The symmetric long-range expression has real coefficients at order two and zero, and a purely imaginary first-order coefficient, in accordance with Theorem 5.1.

For \(K=2,b=1/3\), the slope is \(\rho=2/3\).
Thus \(M(0),\ldots,M(4)\) are
\(1/3,4/3,7/3,3,11/3\). A correction containing three derivatives is bounded by \(C\langle x\rangle^{-3}\). It is short range; after \(q\) further derivatives its bound uses \(M(q+3)\geq M(q)\), which preserves the general long-range budget.

## References

[HW] Lars Hörmander, [*The existence of wave operators in scattering theory*](https://gdz.sub.uni-goettingen.de/download/pdf/PPN266833020_0146/LOG_0012.pdf), *Mathematische Zeitschrift* **146** (1976), 69–91, Lemma 3.3 and Definition 3.4 with its adjoint remark, pp. 77–78. Its wave-operator admissibility requires additional decay inequalities; it does not assert our complete stationary class. The present local multiplier and symmetric-splitting proofs state their own hypotheses.

[AT] Shmuel Agmon, notes by Karl Gustafson, reworked by Michael Taylor, [*Limiting Absorption Principle for Long Range Potentials*](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2020/08/AGMON.pdf), §1, conditions (1.1)–(1.4), sets out a smooth differential long-range model. The finite local integrability and restricted leading-coefficient regularity allowed here require the multiplication and approximation proofs above; they are not inferred from those smooth assumptions.


- [Y] Dmitri Yafaev, notes prepared by Andrew Hassell, *Lectures on scattering theory*, 2004. [Author's paper](https://arxiv.org/abs/math/0403213).
