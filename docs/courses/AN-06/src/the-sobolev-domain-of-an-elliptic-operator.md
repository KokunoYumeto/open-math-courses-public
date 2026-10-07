# The Sobolev domain of an elliptic operator

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

**Working question: When does the closure have exactly the expected Sobolev domain?** A graph estimate controls derivatives by the equation, but it must be proved for the actual rough expression before it identifies a closed domain. Approximation then has to preserve symmetry and common constants. Otherwise a smooth approximant can have a correct domain while the limiting operator has not yet been identified.

Changing the highest derivatives of an operator need not change its domain. The difficult point is to prove this when the leading coefficients are merely continuous and the lower coefficients may be unbounded. A symmetric smooth approximation supplies a known domain, but a bound whose constant grows arbitrarily during smoothing would not transfer that domain back to the original expression. We obtain a constant controlled by the fixed coefficient class, its continuity modulus and principal ellipticity. No derivative of an approximating leading coefficient enters that constant.

Read [Admissible differential perturbations](admissible-differential-perturbations.md#admissible-global-mapping) for the local coefficient exponents and the global multiplier estimate. The smooth-reference argument uses the complete programme proof [Finite composition and adjoints with spatial weights](../providers/analysis/finite-weighted-calculus.md#finite-composition). Its hypotheses apply because the reference coefficients are smooth and compactly supported, as checked in Section 4. The high-frequency norm is proved by [the Gaussian-packet norm theorem](../providers/analysis/weighted-positivity.md#high-frequency-norm). Lerner [L] supplies the freely accessible construction correspondence. The uniform estimate for rough coefficients is proved here by local freezing and the coefficient multiplication estimate; it uses no sharp positivity theorem. Fourier inversion and Plancherel are proved in [the Fourier reading](../providers/analysis/finite-derivative-l2.md#fourier-normalization). [Approximation, convolution and integer Sobolev density](../providers/analysis/euclidean-approximation-and-convolution.md) proves the compact smooth density, finite \(L^p\) translation and convolution limits, and the continuous Hilbert-space average used in (15). Hilbert-space adjoint facts are identified in Section 4 below. Teschl [T] provides freely accessible background on adjoints and resolvents.

Throughout, \(n,m\geq1\) are integers, \(D_j=-i\partial_j\), and \(\langle\xi\rangle=(1+|\xi|^2)^{1/2}\). The \(L^2\) inner product is linear in its first variable, and

\[
 \|u\|_{H^s}=\|\langle D\rangle^s u\|_2.
 \tag{1}
\]

All operators below are scalar. Ellipticity means nonvanishing of the principal symbol for every nonzero real covector; it does not require that symbol to be positive.

<a id="domain-theorem"></a>
## 1. The domain theorem and its coefficient hypotheses

Let \(P_0(D)\) have real constant coefficients and elliptic principal polynomial \(p_m(\xi)\), of degree \(m\). Consider

\[
 V=\sum_{|\alpha|\leq m}a_\alpha(x)D^\alpha,
 \qquad P=P_0+V.
 \tag{2}
\]

For \(|\alpha|<m\), with derivative gap \(k=m-|\alpha|\), choose a finite exponent

\[
 p_\alpha=
 \begin{cases}
 n/k,&n>2k,\\
 \text{a fixed number greater than }2,&n=2k,\\
 2,&n<2k.
 \end{cases}
 \tag{3}
\]

**Theorem 1.1.** Assume the following conditions.

- The coefficients \(a_\alpha\) are continuous for \(|\alpha|=m\), and tend to zero as \(|x|\to\infty\).
- For \(|\alpha|<m\), the coefficients belong to \(L^{p_\alpha}_{\mathrm{loc}}\), and

\[
 \|a_\alpha\|_{L^{p_\alpha}(B(y,1))}\longrightarrow0
       \quad\text{as }|y|\to\infty.
 \tag{4}
\]

- \(V\) is symmetric on \(C_c^\infty(\mathbb R^n)\), and the continuous principal symbol

\[
 A_m(x,\xi)=p_m(\xi)+\sum_{|\alpha|=m}a_\alpha(x)\xi^\alpha
 \tag{5}
\]

is elliptic.

Then the differential expression \(P\), with domain \(H^m(\mathbb R^n)\), is self-adjoint in \(L^2(\mathbb R^n)\). Both \(C_c^\infty\) and \(\mathcal S\) are cores. Its graph norm is equivalent to the Sobolev norm:

\[
 c\|u\|_{H^m}\leq \|Pu\|_2+\|u\|_2
       \leq C\|u\|_{H^m},\qquad u\in H^m.
 \tag{6}
\]

The constants in (6) may depend on the operator. No power rate in (4) is needed. In particular the theorem applies to every admissible perturbation in the preceding lesson, even though some of its highest-order terms need not be relatively compact.

The local membership is part of the theorem: an integral that vanishes for all sufficiently distant balls says nothing about its finiteness on balls near the origin. Problem 5 gives a symmetric elliptic expression whose tail integrals vanish but whose action is not defined on all of \(H^m\).

We prove the theorem in stages. Sections 2–3 construct the smooth approximation. Sections 4–5 obtain an imaginary-axis inverse and a graph bound uniform under this approximation. Section 6 transfers the domain.

<a id="domain-coefficient-norm"></a>
## 2. A norm in which symmetry can be approximated

We first make the exponents compatible with localization. Regard a highest-order coefficient as having exponent \(p_\alpha=\infty\). At a critical degree \(m-|\alpha|=n/2\), replace all the given exponents by one common finite exponent greater than 2, no larger than any given exponent at that degree or any exponent at a higher degree. Such a choice exists: every finite exponent at a higher degree is strictly greater than 2, and there are finitely many degrees. Inclusion of \(L^p\) spaces on unit balls preserves both local membership and (4). With this choice,

\[
 \beta\leq\alpha\quad\Longrightarrow\quad p_\beta\leq p_\alpha,
 \tag{7}
\]

where the multiindex inequality is componentwise. Away from the critical degree this follows directly from (3). We keep these fixed compatible exponents throughout the proof.

For any differential expression \(W=\sum b_\alpha D^\alpha\), define

\[
 \|W\|_{\mathrm{coef}}=
 \sum_{|\alpha|=m}\|b_\alpha\|_\infty+
 \sum_{|\alpha|<m}\sup_y
          \|b_\alpha\|_{L^{p_\alpha}(B(y,1))}.
 \tag{8}
\]

The hypotheses imply that \(\|V\|_{\mathrm{coef}}<\infty\). For lower coefficients, local membership bounds the norms at centers in any bounded set by one larger bounded region; (4) bounds the remaining centers. The continuous leading coefficients are bounded by the same compact-region and tail argument.

Proposition 2.1 of [Admissible differential perturbations](admissible-differential-perturbations.md#admissible-global-mapping) gives a fixed constant \(C_0\) such that

\[
 \|Wu\|_2\leq C_0\|W\|_{\mathrm{coef}}\|u\|_{H^m}.
 \tag{9}
\]

It depends on \(n,m\) and the chosen exponents, rather than the coefficients. The extension agrees with the actual coefficient products. Hence \(P:H^m\to L^2\) is bounded, and symmetry extends from compact tests to \(H^m\) by Sobolev density.

<a id="domain-symmetric-smoothing"></a>
**Lemma 2.1.** For every \(\eta>0\), there is a symmetric differential expression \(V_0\) with smooth compactly supported coefficients such that

\[
 \|V-V_0\|_{\mathrm{coef}}<\eta.
 \tag{10}
\]

**Proof.** Choose a real \(\chi\in C_c^\infty\), equal to one on the unit ball and supported in the ball of radius two, and let \(\chi_R(x)=\chi(x/R)\), \(R\geq1\). Set \(W_R=\chi_R V\chi_R\). For compact smooth inputs, multiplication by the real cutoff and symmetry of \(V\) show

\[
 (W_Ru,v)=(V\chi_Ru,\chi_Rv)
              =(\chi_Ru,V\chi_Rv)=(u,W_Rv).
 \tag{11}
\]

The coefficient of \(D^\beta\) in \(W_R\) is

\[
 b_{\beta,R}=\chi_R^2a_\beta+
    \sum_{\substack{\alpha\geq\beta\\\alpha\ne\beta}}
    \binom\alpha\beta\chi_Ra_\alpha
                       D^{\alpha-\beta}\chi_R.
 \tag{12}
\]

Only the cutoff is differentiated. The coefficient of \(D^\beta\) in \(V-W_R\) therefore consists of \((1-\chi_R^2)a_\beta\) and the negatives of the terms in the sum. Every such term is supported where \(|x|\geq R\); the terms with a cutoff derivative are supported in \(R\leq|x|\leq2R\). The derivatives of \(\chi_R\) are uniformly bounded for \(R\geq1\).

For \(p_\beta\leq p_\alpha<\infty\), Hölder on a unit ball gives

\[
 \|a_\alpha\|_{L^{p_\beta}(B(y,1))}
 \leq |B(0,1)|^{1/p_\beta-1/p_\alpha}
          \|a_\alpha\|_{L^{p_\alpha}(B(y,1))}.
 \tag{13}
\]

The corresponding bound for \(p_\alpha=\infty\) uses the factor \(|B(0,1)|^{1/p_\beta}\). A ball meeting the displayed supports has \(|y|\geq R-1\). Equations (4), (7), and the leading coefficient decay now prove

\[
 \|V-W_R\|_{\mathrm{coef}}\longrightarrow0.
 \tag{14}
\]

Fix \(R\) giving an error less than \(\eta/2\). Each lower coefficient of \(W_R\) is compactly supported in its required finite \(L^p\) space; each leading coefficient is continuous and compactly supported.

Let \(\rho_h\geq0\) be a real compact smooth approximate identity of integral one. If \(T_yu(x)=u(x-y)\), define

\[
 V_0u=\int\rho_h(y)T_yW_RT_y^*u\,dy.
 \tag{15}
\]

For compact smooth \(u\), the integral exists in \(L^2\), by (9) and translation continuity; the same formula defines an \(H^m\to L^2\) map. Each translated operator is symmetric, so integrating its inner-product identity proves symmetry of \(V_0\). Its coefficients are exactly \(\rho_h*b_{\beta,R}\), which are smooth and compactly supported. For leading coefficients they converge uniformly; for lower coefficients they converge in global \(L^{p_\beta}\), and hence in the supremum of the local norms in (8). Choosing \(h\) small enough gives \(\|W_R-V_0\|_{\mathrm{coef}}<\eta/2\). Equations (14)–(15) prove (10). \(\square\)

The averaging in (15) explains why coefficient smoothing preserves symmetry here. It smooths the entire localized operator, including every term in (12); it does not impose separate reality conditions on the lower coefficients.

<a id="domain-principal-ellipticity"></a>
## 3. Uniform principal ellipticity

**Lemma 3.1.** The symbol \(A_m\) in (5) is real, and there is \(c_*>0\) such that

\[
 |A_m(x,\xi)|\geq c_*|\xi|^m
         \quad(x\in\mathbb R^n,\ \xi\in\mathbb R^n).
 \tag{16}
\]

For all sufficiently small \(\eta\), any approximation in Lemma 2.1 has principal symbol \(A_{0,m}\) satisfying

\[
 |A_{0,m}(x,\xi)|\geq \tfrac12c_*|\xi|^m.
 \tag{17}
\]

**Proof.** Fix a real covector \(\theta\) and \(\phi\in C_c^\infty\). Symmetry makes the quadratic form of \(P\) on \(e^{iN\theta\cdot x}\phi\) real. Expanding

\[
 D^\alpha(e^{iN\theta\cdot x}\phi)
       =e^{iN\theta\cdot x}(D+N\theta)^\alpha\phi
 \tag{18}
\]

and dividing by \(N^m\) yields, as \(N\to\infty\), the real quantity

\[
 \int A_m(x,\theta)|\phi(x)|^2\,dx.
 \tag{19}
\]

All lower terms tend to zero: their integrals on the fixed compact support are finite by local integrability, and their powers of \(N\) are at most \(m-1\). If the continuous function \(\operatorname{Im}A_m(\cdot,\theta)\) were nonzero at some point, a test supported where it had one strict sign would contradict (19). Thus \(A_m(x,\theta)\) is real for every \(x,\theta\).

The leading coefficient decay makes \(A_m(x,\theta)\to p_m(\theta)\) uniformly on \(|\theta|=1\) as \(|x|\to\infty\). The elliptic polynomial has a positive minimum modulus on that sphere. On the remaining compact set of positions and unit covectors, continuity and ellipticity again give a positive minimum. Homogeneity proves (16).

For an approximation, the finitely many leading coefficient differences each have uniform norm less than \(\eta\). Therefore

\[
 |A_{0,m}-A_m|\leq N_{n,m}\eta|\xi|^m,
 \tag{20}
\]

where \(N_{n,m}\) is the number of multiindices of degree \(m\). Choose \(N_{n,m}\eta\leq c_*/2\). This proves (17); reality follows from the same symmetry argument, or from the smooth formal adjoint. \(\square\)

For example, in one dimension a first-order real elliptic principal symbol has opposite signs at positive and negative frequencies. The estimates use its modulus and retain that case.

## 4. The smooth reference and its imaginary resolvent

Fix an approximation satisfying (17), and write

\[
 A_0=P_0+V_0,\qquad \mathcal D(A_0)=H^m.
 \tag{21}
\]

Its left symbol \(a_0(x,\xi)\) is in the global classical class \(S^m_{1,0}\): all coefficient derivatives are bounded and frequency differentiation lowers polynomial degree. More precisely it belongs to \(S(\langle\xi\rangle^m,G_1)\) in the linked programme calculus proof. Every positive position derivative is supported in the fixed compact coefficient support, where multiplying by any fixed power of \(\langle x\rangle\) changes only its finite bound. The constant-coefficient part has no positive position derivatives. Thus the stronger spatial derivative factors required by \(G_1\) hold for this fixed reference; their constants may depend on that reference. For sufficiently large frequency its modulus is at least \(c\langle\xi\rangle^m\), uniformly in position. The lower coefficients can be complex; this modulus bound follows from (17) by subtracting their order-\(m-1\) bound.

<a id="domain-hilbert-tools"></a>
The Hilbert-space facts used in this domain argument can be proved here. First, in a complete Hilbert space every closed subspace \(N\) has an orthogonal projection. For a fixed \(u\), take \(v_j\in N\) with \(\|u-v_j\|\) tending to its infimum \(d\). The parallelogram identity gives

\[
 \|v_j-v_k\|^2
 \le 2\|u-v_j\|^2+2\|u-v_k\|^2-4d^2\longrightarrow0.
\]

Completeness and closedness give a minimizing \(v\in N\). Varying it by real and imaginary scalar multiples of any \(w\in N\) in the minimizing inequality shows \(u-v\perp N\). The decomposition is unique, since \(N\cap N^\perp=\{0\}\). In particular a closed subspace with zero orthogonal complement is the whole space.

This also proves the representing-vector theorem needed for adjoints. If \(F\) is a nonzero bounded linear functional, apply that projection to its closed kernel and a vector outside the kernel, obtaining \(e\perp\ker F\) with \(F(e)\ne0\). For every \(w\), the vector \(w-F(w)e/F(e)\) is in the kernel. Taking its inner product with \(e\) gives

\[
 F(w)=(w,h),\qquad h=\frac{\overline{F(e)}}{\|e\|^2}e.
\]

The zero functional is represented by zero. Cauchy–Schwarz follows by minimizing \(\|w-ce\|^2\) in the scalar \(c\); it gives \(\|F\|\le\|h\|\), and testing on \(h/\|h\|\) gives equality when \(h\ne0\). Uniqueness follows by testing the difference of two representing vectors against itself.

For a densely defined operator \(A\), its adjoint domain consists of those \(u\) for which \(v\mapsto(Av,u)\) is bounded in the ambient Hilbert norm on \(\mathcal D(A)\). Density extends this functional uniquely, and the representing-vector argument defines \(A^*u\) by \((Av,u)=(v,A^*u)\). Its graph is closed: if \(u_j\to u\) and \(A^*u_j\to f\), pass to the limit in this identity for each fixed \(v\in\mathcal D(A)\). It gives \(u\in\mathcal D(A^*)\) and \(A^*u=f\). A symmetric operator is contained in its adjoint; a self-adjoint operator is therefore closed. The same defining identity proves, for every complex \(z\),

\[
 \operatorname{Ran}(A-z)^\perp=\ker(A^*-\overline z).
\]

Indeed orthogonality says \((Av,u)=z(v,u)=(v,\overline z\,u)\), which is exactly the adjoint-domain condition and displayed kernel equation. These arguments justify all the closed-range and two-sign adjoint steps below.

We will also use the geometric inverse for a bounded operator \(K\) with \(\|K\|<1\). Its finite sums \(\sum_{j=0}^N(-K)^j\) are Cauchy in operator norm by the scalar geometric series. Their values converge on every vector in the complete Hilbert space, defining a bounded operator with the same norm limit. Multiplication by \(I+K\) on either side of the finite sums leaves \(I-(-K)^{N+1}\). Passing to the limit proves the two-sided inverse and the norm bound \((1-\|K\|)^{-1}\). Thus the Neumann step in Section 6 is also a proved input.

<a id="domain-smooth-reference"></a>
**Lemma 4.1.** \(A_0\) is self-adjoint on \(H^m\), and, for every nonzero real \(t\),

\[
 \|(A_0+it)^{-1}\|_{L^2\to L^2}\leq |t|^{-1}.
 \tag{22}
\]

<a id="domain-parametrix"></a>
**Proof.** Here is the smooth parametrix needed for the domain argument. Choose a frequency cutoff equal to one at sufficiently large frequency and zero where the preceding modulus bound has not been established. Its product with \(a_0^{-1}\) is a symbol \(e\in S^{-m}_{1,0}\). The proved finite left product gives

\[
 e(x,D)A_0=I+R,\qquad R\in\operatorname{Op}S^{-1}_{1,0}.
\]

The compact-frequency discrepancy belongs to every negative frequency order. The exact symbols of \((-R)^j e(x,D)\) belong to \(S(\langle\xi\rangle^{-m-j},G_1)\). The reciprocal estimates and composition follow from Sections 1 and 4 of the linked programme proof; the compact-frequency discrepancy belongs to every negative frequency weight for \(G_1\), even though it need not decrease in position. Write these exact symbols as \(b_j\), and choose a smooth frequency cutoff \(\theta\) that is zero on the unit ball and one outside the ball of radius two. For \(j\geq1\), choose \(R_j\geq j\) so large that \(\theta(\xi/R_j)b_j\) has every seminorm of derivative order at most \(j\) in \(S(\langle\xi\rangle^{-m-N},G_1)\) at most \(2^{-j}\), simultaneously for the finitely many integers \(0\leq N<j\). This is possible: the product rule bounds each such seminorm by a fixed constant times \(R_j^{N-j}\); derivatives of the cutoff have the same frequency gains on their annular support. Choose any sufficiently large \(R_0\). For each fixed \(N\), the series with \(j>N\) now converges in every seminorm of \(S(\langle\xi\rangle^{-m-N},G_1)\). The term with \(j=N\) already has that order, and the finitely many differences \((\theta(\xi/R_j)-1)b_j\) with \(j<N\) have compact frequency support and belong to every negative frequency order. Completeness, proved in [the symbol-space argument](../providers/analysis/finite-weighted-calculus.md#symbol-completeness-and-reciprocal), therefore makes \(b=\sum_{j\geq0}\theta(\xi/R_j)b_j\) a symbol of order \(-m\), with \(b-\sum_{j<N}b_j\in S(\langle\xi\rangle^{-m-N},G_1)\) for every \(N\). Multiplying by \(A_0\) puts this error in \(S(\langle\xi\rangle^{-N},G_1)\), while the exact finite product is \(\sum_{j<N}(-R)^j(I+R)=I-(-R)^N\). Uniqueness of the left symbol, proved in Section 5 of that programme reading, makes these all estimates for one exact residual. Thus finite telescoping gives

\[
 BA_0=I+S,\qquad B\in\operatorname{Op}S^{-m}_{1,0},
 \quad S\in\operatorname{Op}S^{-\infty}_{1,0}.
 \tag{23}
\]

Only frequency smoothing is needed here: \(B:L^2\to H^m\), and \(S:L^2\to H^q\) for every fixed real \(q\). These bounds follow by conjugating with the Fourier multipliers and applying the order-zero bound. The finite product and order-zero bounds are proved in Sections 4–6 of the programme calculus reading; frequency cutoff summation above supplies the actual inverse correction. No estimate for the original rough expression is inferred from a smooth-symbol theorem.

If \(u\in\mathcal D(A_0^*)\) and \(f=A_0^*u\in L^2\), the compact-test adjoint identity and smooth formal symmetry give \(A_0u=f\) distributionally. Equation (23) implies

\[
 u=Bf-Su\in H^m.
 \tag{24}
\]

Conversely, symmetry on \(H^m\) puts that space in the adjoint domain. Thus the domains and actions agree. This proves self-adjointness without a positivity assumption on its principal symbol.

For \(u\in H^m\), symmetry gives

\[
 \|(A_0+it)u\|_2^2=\|A_0u\|_2^2+t^2\|u\|_2^2.
 \tag{25}
\]

Its range is closed: Cauchy outputs make both inputs and \(A_0\)-images Cauchy, and a self-adjoint operator is closed. Its orthogonal complement is \(\ker(A_0-it)=0\), again by (25). Hence the range is all of \(L^2\), and (22) follows. \(\square\)

## 5. A fixed bound with an approximation-dependent threshold

For sufficiently large \(|t|\), put

\[
 e_t(x,\xi)=\frac{\langle\xi\rangle^m}{a_0(x,\xi)+it}.
 \tag{26}
\]

The principal symbol is real, but the full left symbol may have complex lower-order terms. We check their effect before using (26).

<a id="domain-parameter-symbol"></a>
**Lemma 5.1.** There are \(c,M>0\), controlled by \(c_*,m\), and thresholds depending on the fixed approximation, such that for both signs of large \(t\),

\[
 |a_0(x,\xi)+it|\geq c(\langle\xi\rangle^m+|t|),
 \qquad \sup_{x,\xi}|e_t(x,\xi)|\leq M.
 \tag{27}
\]

The family \(e_t\) is bounded in \(S^0\) for this approximation. Its derivative seminorm bounds may depend on \(V_0\), whereas \(M\) can be fixed independently of the approximation error \(\eta\).

**Proof.** Since \(a_0-A_{0,m}\in S^{m-1}\), at sufficiently large frequency

\[
 |\operatorname{Re}a_0|\geq \tfrac14c_*|\xi|^m,
 \qquad |\operatorname{Im}a_0|\leq |\xi|^m.
 \tag{28}
\]

The threshold can depend on all the lower coefficients. If \(|t|\geq2|\operatorname{Im}a_0|\), the imaginary part of the denominator has modulus at least \(|t|/2\), and the real part supplies the frequency bound in (28). Their maximum controls their sum. If \(|t|<2|\operatorname{Im}a_0|\), then \(|t|<2|\xi|^m\), and the real part alone controls the sum. On this high-frequency region \(|\xi|^m\) and \(\langle\xi\rangle^m\) are comparable with a fixed constant after making the threshold at least one.

On the remaining bounded-frequency region, take \(|t|\) at least twice the uniform bound for \(|a_0|\), and at least the maximum of \(\langle\xi\rangle^m\) there. Then \(|a_0+it|\geq|t|/2\), proving (27) with a fixed \(c\). In particular \(M=c^{-1}\) works.

For the differentiated estimates, each derivative of \((a_0+it)^{-1}\) is a finite sum of products

\[
 (a_0+it)^{-1-r}\prod_{j=1}^r
             \partial_\xi^{\alpha_j}\partial_x^{\beta_j}a_0,
 \qquad \sum_j\alpha_j=\alpha,\quad\sum_j\beta_j=\beta.
 \tag{29}
\]

Every factor in the product is bounded by \(C\langle\xi\rangle^{m-|\alpha_j|}\). Equation (27) bounds (29) by \(C\langle\xi\rangle^{-m-|\alpha|}\), uniformly in \(t\). The product rule with the numerator in (26) gives all the \(S^0\) bounds. The positive position derivatives are supported in the same fixed compact set as before, so the family also has uniform \(S(1,G_1)\) seminorms. The constants use coefficient derivatives and support bounds of this fixed \(V_0\). \(\square\)

<a id="domain-uniform-operator-norm"></a>
**Lemma 5.2.** There is a constant \(C_1\), independent of small \(\eta\), such that

\[
 \|\operatorname{Op}(e_t)\|_{2\to2}\leq C_1
      \quad(|t|\geq T_{V_0}).
 \tag{30}
\]

**Proof.** Take a smooth \(0\leq\vartheta\leq1\), equal to one on \(|\xi|\leq1\) and zero on \(|\xi|\geq2\). For all \(R\geq1\), split

\[
 e_t=e_t(1-\vartheta(\xi/R))+e_t\vartheta(\xi/R).
 \tag{31}
\]

For the fixed approximation, the first family is bounded in \(S^0\), uniformly in \(R\) and large \(|t|\), and vanishes for \(|\xi|<R\). Cutoff derivatives have size \(R^{-|\alpha|}\) on their annulus, exactly the required frequency weights. Write \(a_{R,t}=e_t(1-\vartheta(\xi/R))\). Since every derivative vanishes for \(|\xi|<R\), its uniform classical bounds imply

\[
 |\partial_x^\alpha\partial_\xi^\beta a_{R,t}|
       \le C_{\alpha\beta,V_0}R^{-|\beta|},
 \qquad \sup|a_{R,t}|\le M.
\]

The complete [Gaussian-packet norm proof, Theorem 4](../providers/analysis/weighted-positivity.md#high-frequency-norm), now gives
\(\|\operatorname{Op}(a_{R,t})\|\le M+C_{V_0}/R\).
Its packet analysis is an isometry, so the compressed multiplication operator has norm at most \(M\), including for complex symbols. With packet width \(r=R^{-1/2}\), the position and frequency Taylor errors are both \(O(R^{-1})\); the left-to-Weyl mixed derivative error has the same bound. The provider proves these estimates and their cutoff limits using its complete bounded-amplitude theorem. No sharp positivity theorem or external finite-composition result enters this step.

Only the finite derivative constant depends on the fixed approximation; \(M\) is still the approximation-independent constant of Lemma 5.1. For \(R\ge1\), \(C_{V_0}/R\le\sqrt{C_{V_0}^2/R}\). Enlarging and renaming that fixed constant proves the originally asserted estimate, for \(R>1\),

\[
 \|\operatorname{Op}(e_t(1-\vartheta(\xi/R)))\|_{2\to2}
       \leq M+\sqrt{C_{V_0}/R}.
 \tag{32}
\]

Choose \(R\), after fixing \(V_0\), to make the last term at most one. For this fixed \(R\), every derivative of the second symbol in (31) through any fixed order is \(O_{V_0,R}(|t|^{-1})\), uniformly in \(x,\xi\). This follows from (29) on its bounded frequency support. The complete programme [finite-derivative operator bound](../providers/analysis/finite-derivative-l2.md#finite-derivative-l2) implies

\[
 \|\operatorname{Op}(e_t\vartheta(\xi/R))\|_{2\to2}
       \longrightarrow0\quad(|t|\to\infty).
 \tag{33}
\]

Make it at most one by increasing the threshold. Thus \(C_1=M+2\) works for every sufficiently accurate approximation. Only the threshold depends on its derivative bounds. \(\square\)

<a id="domain-sobolev-resolvent"></a>
**Proposition 5.3.** A fixed constant \(K\), independent of small \(\eta\), satisfies

\[
 \|(A_0+it)^{-1}\|_{L^2\to H^m}\leq K
       \quad(|t|\geq T'_{V_0}).
 \tag{34}
\]

**Proof.** The finite product in Theorem 4.1 of the programme calculus proof, applied to the \(G_1\) symbols checked above, gives

\[
 \operatorname{Op}(e_t)(A_0+it)=\langle D\rangle^m-R_t,
 \qquad R_t\text{ bounded in }\operatorname{Op}(S^{m-1}).
 \tag{35}
\]

Indeed the pointwise product \(e_t(a_0+it)\) is exactly \(\langle\xi\rangle^m\). Composition with the constant \(it\) is exact. The remainder comes entirely from composition with the fixed symbol \(a_0\), whose order-\(m\) seminorms and the bounded \(S^0\) family from Lemma 5.1 give uniform order-\(m-1\) estimates. The growing constant \(it\) must be separated in this way.

The finite product puts \(R_t\langle D\rangle^{1-m}\) in \(S(1,G_1)\); Section 6 of that same programme proof therefore gives the actual uniform map \(R_t:H^{m-1}\to L^2\) for this fixed approximation. For \(v=(A_0+it)^{-1}g\in H^m\), that map and (30), (35) give

\[
 \|v\|_{H^m}\leq C_1\|g\|_2+L_{V_0}\|v\|_{H^{m-1}}.
 \tag{36}
\]

For every \(\delta>0\) there is \(C_\delta\) with

\[
 \|v\|_{H^{m-1}}\leq\delta\|v\|_{H^m}+C_\delta\|v\|_2.
 \tag{37}
\]

To verify this including \(m=1\), choose a frequency radius beyond which \(\langle\xi\rangle^{-1}\leq\delta\). Split the Fourier norm into the high and low regions and use the triangle inequality; the low region has bounded weight. Choose \(\delta\) so that \(L_{V_0}\delta\leq1/2\). With \(B_{V_0}=L_{V_0}C_\delta\), (22) yields

\[
 \|v\|_{H^m}\leq2C_1\|g\|_2+2B_{V_0}\|v\|_2
       \leq(2C_1+2B_{V_0}/|t|)\|g\|_2.
 \tag{38}
\]

Increase the threshold until \(2B_{V_0}/|t|\leq C_1\). Thus \(K=3C_1\) works for both signs of large \(t\). \(\square\)

The quantifier order in (34) is decisive: first fix \(K\), then choose a sufficiently accurate smooth approximation, and finally take \(|t|\) sufficiently large for that approximation.

### An additional uniform graph bound from coefficient freezing

All constants in this additional argument refer to the fixed original expression \(P\). They are independent of derivatives introduced during smoothing. We prove the estimate for any coefficient approximation \(Q=P_0+\sum q_\alpha D^\alpha\) sufficiently close to \(P\) in (8), whether or not \(Q\) is symmetric.

<a id="domain-lower-part"></a>
**Lower-part estimate.** The original lower-order part \(P_{<m}\), including the lower terms of \(P_0\), satisfies, for every \(a>0\),

\[
 \|P_{<m}v\|_2\leq a\|v\|_{H^m}+C_a\|v\|_2,
 \qquad v\in H^m.
\]

The same estimate holds with \(2a\) and the same lower constant for every sufficiently close \(Q_{<m}\).

**Proof.** Each lower coefficient \(a_\alpha\) can be approximated in its uniform unit-ball \(L^{p_\alpha}\) norm by a bounded smooth compactly supported function \(h_\alpha\). To see this, first cut off where the tail norm in (4) is small; the remaining compactly supported coefficient is in global finite \(L^{p_\alpha}\), and convolution approximates it in that norm. The local supremum is bounded by the global norm. This step includes the finite endpoint \(p_\alpha=n/(m-|\alpha|)>2\).

Choose the finitely many approximations so that their combined multiplier error in (9) is at most \(a/2\). Their bounded coefficients, and the constant lower terms of \(P_0\), give a bound by \(C_h\|v\|_{H^{m-1}}\). Fourier splitting gives, for every \(b>0\),

\[
 \|v\|_{H^{m-1}}\leq b\|v\|_{H^m}+C_b\|v\|_2.
\]

Choose \(C_hb\leq a/2\). This proves the lower-part estimate. Coefficient proximity and (9) add at most \(a\|v\|_{H^m}\) to it. For \(m=1\), the bounded approximating lower part already acts on \(L^2\). \(\square\)

<a id="domain-local-freezing"></a>
**Uniform freezing estimate.** There are \(\eta_0>0\) and \(C_g\), depending only on the fixed coefficients of \(P\), such that

\[
 \|v\|_{H^m}\leq C_g\bigl(\|Qv\|_2+\|v\|_2\bigr),
 \quad v\in H^m,\quad\|Q-P\|_{\mathrm{coef}}<\eta_0.
\]

**Proof.** The leading coefficients are uniformly continuous: they are continuous on compact sets and tend to zero at infinity. Fix a small radius \(r>0\). On a ball \(B(y,r)\), freeze the original principal coefficients at its center, obtaining the homogeneous polynomial \(A_m(y,D)\). Equation (16) and Plancherel give a constant \(C_*\), independent of \(y\), such that

\[
 \|w\|_{H^m}\leq C_*\bigl(\|A_m(y,D)w\|_2+\|w\|_2\bigr).
\]

Indeed \(\langle\xi\rangle^m\leq C(1+|A_m(y,\xi)|)\), with \(C\) controlled by \(c_*\) and \(m\). For \(w\) supported in this ball, the difference between the principal part of \(Q\) and its frozen original part is bounded by

\[
 C\bigl(\omega(r)+\|Q-P\|_{\mathrm{coef}}\bigr)\|w\|_{H^m},
\]

where \(\omega(r)\to0\) is a common modulus of continuity for the finitely many original leading coefficients. Choose the coefficient-error bound and \(r\) so that this term, after multiplication by \(C_*\), is at most \(\|w\|_{H^m}/4\). Use the lower-part estimate with a fixed \(a\) so small that the lower part contributes at most another quarter. Absorption in the frozen-coefficient estimate gives

\[
 \|w\|_{H^m}\leq C_{\mathrm{loc}}
            \bigl(\|Qw\|_2+\|w\|_2\bigr),
 \quad\operatorname{supp}w\subset B(y,r),
\]

with common constants for all centers and all sufficiently close \(Q\).

<a id="domain-global-freezing"></a>
Choose one nonzero real \(\zeta\in C_c^\infty(B(0,r))\), and put \(\zeta_y(x)=\zeta(x-y)\). Integer Sobolev localization gives

\[
 \int\|\zeta_yv\|_{H^m}^2\,dy\asymp\|v\|_{H^m}^2.
\]

For the upper bound expand each derivative by the product rule and integrate in \(y\). For the lower bound start with \(\int\|\zeta_yv\|_2^2dy=\|\zeta\|_2^2\|v\|_2^2\), then use the product rule to express \(\zeta_yD^\alpha v\) through \(D^\alpha(\zeta_yv)\) and derivatives of \(v\) of strictly smaller order. Induction in \(|\alpha|\) bounds those lower terms by the already controlled localized derivative norms. This proves both bounds without differentiating a coefficient.

In the commutator write \(q_\alpha\) for the full coefficients of \(Q\), including the fixed constant coefficients of \(P_0\). The commutator is a finite sum of \(q_\alpha(D^\gamma\zeta_y)D^{\alpha-\gamma}v\), with \(0<\gamma\leq\alpha\). Integrating its squared norm in \(y\) removes the cutoff factor and leaves a constant times \(\|q_\alpha D^{\alpha-\gamma}v\|_2^2\). For a lower coefficient its available gap on \(H^{m-1}\) is

\[
 (m-1)-|\alpha-\gamma|
       =(m-|\alpha|)-1+|\gamma|\geq m-|\alpha|.
\]

Thus the same local coefficient exponent suffices by finite-volume inclusion and the Sobolev multiplication estimate. At a critical gap choose a finite exponent no larger than the given one. Leading coefficients are uniformly bounded and their remaining derivatives have order at most \(m-1\). Consequently

\[
 \int\|[Q,\zeta_y]v\|_2^2dy\leq C_r\|v\|_{H^{m-1}}^2
\]

uniformly over the approximations. For \(m=1\) only bounded first-order coefficients occur in this commutator. Apply the local estimate to \(\zeta_yv\), square, integrate, and use \(Q\zeta_yv=\zeta_yQv+[Q,\zeta_y]v\), the localization identity, and the cutoff commutator bound. The result bounds \(\|v\|_{H^m}\) by a fixed constant times \(\|Qv\|_2+\|v\|_{H^{m-1}}+\|v\|_2\). Absorb the middle norm by the Fourier interpolation inequality. This proves the uniform graph estimate. Compact smooth approximation extends all identities to \(H^m\). \(\square\)

<a id="domain-graph-resolvent"></a>
**Graph-resolvent consequence.** There is a fixed \(K_g\), independent of sufficiently small approximation error, such that

\[
 \|(A_0+it)^{-1}\|_{L^2\to H^m}\leq K_g,
 \qquad |t|\geq1.
\]

**Proof.** The smooth symmetric reference obeys the uniform graph estimate, while (25) gives, for \(v=(A_0+it)^{-1}g\),

\[
 \|A_0v\|_2\leq\|g\|_2,\qquad
 \|v\|_2\leq|t|^{-1}\|g\|_2.
\]

Hence \(\|v\|_{H^m}\leq C_g(1+|t|^{-1})\|g\|_2\). Take \(K_g=2C_g\). Both signs have the same bound. Its constant was obtained before choosing the smoothing accuracy and uses no derivative seminorm of \(V_0\). \(\square\)

The order of choices is now explicit: first obtain \(\eta_0,C_g,K_g\) from the original coefficient class; then choose a symmetric approximation accurate enough for the Neumann factor. The smooth parametrix identifies that reference's domain, and the common graph bound transfers it to the rough expression.

The constant \(K_g\) here may depend on the original continuity modulus and lower coefficients. This additional estimate supplies the fixed threshold \(|t|\geq1\); it is distinct from the principal-ellipticity-controlled constant \(K=3C_1\) in (34), whose threshold may depend on the approximation. Both routes retain independence from the approximation accuracy and both resolvent signs.

<a id="domain-transfer"></a>
## 6. Transferring the domain and finding a core

**Proof of Theorem 1.1.** Choose \(\eta<\eta_0\) small enough for (17) and \(C_0K_g\eta<1/2\). Lemma 2.1 supplies \(V_0\); let \(W=V-V_0\). Equation (9) and the graph-resolvent consequence of the additional freezing argument imply, for both signs and \(|t|\geq1\),

\[
 \|W(A_0+it)^{-1}\|_{2\to2}<\tfrac12.
 \tag{39}
\]

The identity plus this bounded operator has an inverse given by its norm-convergent geometric series. On \(H^m\),

\
 P+it=[I+W(A_0+it)^{-1}.
 \tag{40}
\]

Both factors are onto in their respective spaces. Hence \(P+it:H^m\to L^2\) is onto for both signs of any fixed \(t\) with \(|t|\geq1\).

We already know that \(P\) is densely defined and symmetric on \(H^m\). If \(u\in\mathcal D(P^*)\), choose \(v\in H^m\) solving

\[
 (P-it)v=(P^*-it)u.
 \tag{41}
\]

Then \(u-v\in\ker(P^*-it)\). The adjoint range identity and the opposite surjectivity give

\[
 \ker(P^*-it)=\operatorname{Ran}(P+it)^\perp=\{0\}.
 \tag{42}
\]

Thus \(u=v\in H^m\), proving \(\mathcal D(P^*)=H^m\) and \(P=P^*\).

<a id="domain-graph-core"></a>
Equation (40) also provides a bounded inverse from \(L^2\) to \(H^m\) at this fixed \(t\). Applied to \((P+it)u\), it bounds \(\|u\|_{H^m}\) by a constant times \(\|Pu\|_2+\|u\|_2\). The reverse bound follows from (9) and the constant-coefficient multiplier bound. This proves (6).

For \(u\in H^m\), take \(u_j\in C_c^\infty\) converging in \(H^m\). Boundedness \(P:H^m\to L^2\) gives \(Pu_j\to Pu\) in \(L^2\), so the convergence is in graph norm. Therefore \(C_c^\infty\) is a core. The intermediate domain \(\mathcal S\subset H^m\), which contains that core, is a core too. \(\square\)

This argument uses elementary imaginary-axis inverses rather than a spectral representation. It also distinguishes the \(H^m\to L^2\) size of the perturbation from its \(L^2\to L^2\) size: the latter need not be finite.

### Use the conclusion

Trace the fixed graph bound through smoothing, the core closure and both deficiency signs. Keep ellipticity distinct from positivity: the principal symbol need not be positive for the stated realization theorem.

## 7. Problems

**Exercise 1. Which constant must be chosen first? — Basic.** Suppose a smoothing construction gives \(\|V-V_\eta\|_{H^m\to L^2}\leq C_0\eta\), while a resolvent estimate gives \(\|(P_0+V_\eta+it)^{-1}\|_{L^2\to H^m}\leq C_\eta\) for large \(t\). Explain why taking \(\eta\) small need not make their product smaller than one. State the sufficient quantifier order and the bound on the inverse factor in (40).

**Exercise 2. A cutoff creates a critical coefficient — Intermediate.** Let \(n=4,m=2\). A first-order coefficient has exponent 4; a zeroth-order critical coefficient has been assigned exponent 100. Show why localization cannot demand exponent 100 of a zeroth-order term created from the first-order coefficient. Give a compatible choice and a compact singular function that distinguishes \(L^4\) from \(L^{100}\).

**Exercise 3. Smoothing the whole expression — Intermediate.** In one dimension let \(b_0,b_1\in C_c^\infty\), and suppose \(B=b_1D+b_0\) is symmetric. Prove that coefficient convolution with a real approximate identity preserves symmetry. Compute the relation between \(b_0,b_1\), including any allowed real zeroth-order term, and show that this relation is preserved by convolution.

**Exercise 4. A continuous leading coefficient with a singular derivative — Advanced.** Choose a nonnegative compact smooth cutoff \(\chi\), equal to one near zero, and put \(f(x)=1+\chi(x)|x|^{3/4}\). Consider

\[
 P=fD-\frac i2 f',\qquad \mathcal D(P)=H^1(\mathbb R).
 \tag{43}
\]

Check the coefficient hypotheses of Theorem 1.1 and prove symmetry on compact tests. Conclude its domain and core statements. Explain why omitting the zeroth-order term generally destroys symmetry.

**Exercise 5. Tail decay without local finiteness — Advanced.** In \(\mathbb R^5\), let \(0\leq\chi\in C_c^\infty\) equal one near zero, and define, away from the origin,

\[
 a(x)=\chi(x)|x|^{-11/5},\qquad
 u(x)=\chi(x)|x|^{-2/5}.
 \tag{44}
\]

Assign arbitrary values at zero. Prove that \(-\Delta+a\) is symmetric and maps compact smooth tests into \(L^2\), and that the translated coefficient integrals of exponent \(5/2\) vanish for all sufficiently distant centers. Nevertheless show that \(u\in H^2\) and \(au\notin L^2\). Include justification of the weak derivatives at the origin. What fails in the hypotheses of Theorem 1.1?

<a id="domain-solutions"></a>
## 8. Complete solutions

**Solution 1.** The bound on the perturbation factor is only \(C_0\eta C_\eta\). For example, the permitted estimates could have \(C_\eta=\eta^{-2}\), making this bound \(C_0/\eta\). It cannot certify invertibility as \(\eta\to0\). The sufficient statement is: there exists \(K\) independent of \(\eta\), and for each sufficiently small \(\eta\) there exists a threshold \(T_\eta\) such that the Sobolev resolvent norm is at most \(K\) for both signs of \(|t|\geq T_\eta\). Choose \(C_0K\eta<1/2\) first, then the approximation, then \(t\). With \(Q=W(A_0+it)^{-1}\),

\[
 (I+Q)^{-1}=\sum_{j=0}^\infty(-Q)^j,
 \qquad \|(I+Q)^{-1}\|\leq(1-\|Q\|)^{-1}<2.
 \tag{45}
\]

The example concerns failure of the proposed estimate to prove smallness, rather than proving failure of the actual inverse. Lemmas 5.1–5.2 and Proposition 5.3 obtain the principal-ellipticity-controlled fixed bound \(K\), with an approximation-dependent threshold. The additional freezing argument obtains the coefficient-dependent bound \(K_g\) with the common threshold 1, which is the bound used in the domain transfer.

**Solution 2.** Multiplying on the right by a cutoff produces \(aD_j\chi\) among the zeroth-order coefficients. A bounded smooth factor does not generally improve local integrability. Taking a cutoff supported near zero, the radial coefficient \(a=\chi(x)|x|^{-9/10}\) in four dimensions belongs to \(L^p\) near zero precisely when

\[
 \int_0^1 r^{3-9p/10}\,dr<\infty,
       \quad\text{equivalently }p<40/9.
 \tag{46}
\]

Thus it belongs to \(L^4\) but not \(L^{100}\). A localization cutoff with a derivative nonzero at the singular point leaves this distinction in the created coefficient. The allowed critical choice \(p=3\) satisfies \(2<3\leq4\), so (13) controls that created term. Every original zeroth-order \(L^{100}_{\mathrm{loc}}\) coefficient also belongs to \(L^3_{\mathrm{loc}}\); its translated norm decay persists by finite-volume Hölder. This change of critical exponent fixes the proof without strengthening any coefficient hypothesis.

**Solution 3.** The formal adjoint is

\[
 B^*=\overline{b_1}D-i\overline{b_1}' +\overline{b_0}.
 \tag{47}
\]

Equality with \(B\) gives \(b_1=\overline{b_1}\) and \(b_0-\overline{b_0}=-ib_1'\). Hence

\[
 b_0=c-\frac i2 b_1',\qquad c\text{ real}.
 \tag{48}
\]

Convolving with a real kernel preserves reality and commutes with differentiation, so the new coefficients satisfy the same relation. This gives the direct coefficient proof. Alternatively write the convolved operator as \(\int\rho_h(y)T_yBT_y^*dy\); every integrand is symmetric, and integrating the inner-product identity proves symmetry. The second argument also works with the rough localized coefficients of Lemma 2.1, where their formal derivatives need not be coefficient functions.

**Solution 4.** The function \(f-1\) is continuous and compactly supported, \(f\geq1\), and its weak derivative is

\[
 f'=\chi'|x|^{3/4}+\tfrac34\chi\operatorname{sgn}(x)|x|^{-1/4}
 \tag{49}
\]

almost everywhere. The singular term is locally square integrable, since \(\int_0^1 x^{-1/2}dx<\infty\). It is the weak derivative: \(f\) is locally absolutely continuous, and integrating its displayed derivative across zero recovers \(f\). Both perturbation coefficients \(f-1\) and \(-if'/2\) have zero tails. For \(n=m=1\), the lower coefficient exponent in (3) is 2, so every coefficient hypothesis holds. The principal symbol \(f(x)\xi\) is elliptic.

For compact smooth \(u,v\), integration by parts with the locally absolutely continuous \(f\) gives

\[
 (fDu,v)=(u,fDv-if'v).
 \tag{50}
\]

The adjoint of multiplication by \(-if'/2\) is multiplication by \(if'/2\). Combining the two terms leaves exactly \(fD-if'/2\) on the right. Thus \(P\) is symmetric, and Theorem 1.1 makes it self-adjoint on \(H^1\), with both stated cores and graph norm equivalence. For \(fD\) alone, the extra term \(-if'\) remains in (50), and \(f'\) is not zero. Its leading coefficient's reality by itself does not give symmetry.

**Solution 5.** In five dimensions a radial power \(r^{-s}\) belongs locally to \(L^p\) exactly when \(sp<5\), since its integral has radial exponent \(4-sp>-1\). For \(a\), \(2(11/5)=22/5<5\), so \(a\in L^2_{\mathrm{loc}}\). Multiplication by \(a\) therefore maps compact smooth tests into \(L^2\); it is symmetric because \(a\) is real. Adding \(-\Delta\) preserves these properties, and the principal symbol remains \(|\xi|^2\). For all balls disjoint from the compact support of \(\chi\), the coefficient integral is zero, including at exponent \(5/2\). But

\[
 (11/5)(5/2)=11/2>5,
 \tag{51}
\]

so \(a\notin L^{5/2}_{\mathrm{loc}}\).

For the punctured radial function \(u\), derivatives of order \(j\leq2\) are bounded by \(C_jr^{-2/5-j}\) near zero. The worst squared radial exponent is

\[
 4-2(2/5+2)=-4/5>-1.
 \tag{52}
\]

Thus these classical derivatives, including the function itself, are locally square integrable, and cutoff differentiation is harmless away from zero. They are also its distributional derivatives. Integrate by parts outside the radius-\(\varepsilon\) ball. For a first derivative the boundary integral is bounded by \(C\varepsilon^{4-2/5}\); for the derivative of a first derivative it is bounded by \(C\varepsilon^{4-7/5}\). Both tend to zero. The locally integrable interior terms converge as \(\varepsilon\downarrow0\), proving both successive weak derivative identities. Hence \(u\in H^2\).

Near zero \(au=r^{-13/5}\), whose squared radial exponent is

\[
 4-26/5=-6/5<-1.
 \tag{53}
\]

It is not in \(L^2\), while \(-\Delta u\in L^2\). Their sum cannot belong to \(L^2\), for otherwise subtraction would put \(au\) in \(L^2\). The missing condition is local \(L^{5/2}\) membership of the zeroth coefficient, not ellipticity, symmetry on tests, or tail decay. Infinity-only conditions cannot justify the whole \(H^2\) operator domain.

## 9. Reading and further directions


[L] Nicolas Lerner, [*Metrics on the Phase Space and Non-Selfadjoint Pseudo-Differential Operators*, Chapter 2](https://webusers.imj-prg.fr/~nicolas.lerner/ch2booklerner.pdf), Theorems 2.3.7, 2.3.18–2.3.19 and 2.5.1, gives the broader finite calculus and order-zero bounds. The linked programme calculus proof supplies all such steps used in Sections 4–5 for the actual smooth compact-coefficient reference. Definition 2.4.1 and Proposition 2.4.3 give the freely accessible Gaussian-packet construction; the programme packet proof derives the high-frequency norm used in Lemma 5.2 directly, including complex symbols. The additional freezing proof retains its separate coefficient-dependent constant.

[ALNV] Bernd Ammann, Robert Lauter, Victor Nistor and András Vasy, [*Complex powers and non-compact manifolds*, arXiv:math/0211305v1](https://arxiv.org/abs/math/0211305v1), Proposition 2.2(iii) and Proposition 3.1, gives the smooth elliptic self-adjointness and Sobolev-domain route in extended Weyl algebras. The rough-coefficient transfer in Sections 2, 5 and 6 is additional to that result.

[HJS] Andrew Hassell, Qiuye Jia and Ethan Sussman, [*Lecture notes on non-elliptic Fredholm theory*, arXiv:2604.18956v1](https://arxiv.org/abs/2604.18956v1), Lemma 2.7, relates essential self-adjointness to the vanishing of two distributional nullspaces by invoking abstract deficiency theory; Proposition 2.8 applies it to a Laplacian with a smooth decaying potential. The Hilbert-space and two-sign range arguments used here are proved in Sections 4–6. That smooth example does not replace the present domain theorem for arbitrary real scalar elliptic polynomials and rough differential coefficients, whose proof uses modulus ellipticity rather than positivity.

[T] Gerald Teschl, [*Mathematical Methods in Quantum Mechanics*](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf), §§2.2 and 2.4, provides adjoint and resolvent background; §6.1 treats relative operator bounds and the Kato–Rellich theorem. That abstract theorem is useful once a relative bound smaller than one is known. Here the small bound is produced against a suitably chosen smooth reference, with ellipticity controlling the constant.

For practice, compare the compactly supported leading perturbation from [Admissible differential perturbations](admissible-differential-perturbations.md#admissible-global-mapping), Problem 3, with the domain theorem: failure of relative compactness does not prevent the \(H^m\) domain conclusion. A further question is whether less leading regularity or a different lower-coefficient endpoint can be handled. Such changes require additional estimates; neither the smooth parametrix nor the critical finite-\(p\) multiplier statement alone proves them. Weighted resolvent estimates and boundary values require further analysis after the domain has been identified.
