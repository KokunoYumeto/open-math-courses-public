# Frequency cutoffs and compact scattering remainders

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

**Working question: How can a full-order perturbation become compact after a frequency cutoff?** The localized derivative example in the guide is noncompact on its natural graph space, yet a smooth compact frequency cutoff turns it into a square-integrable kernel. For rough coefficients one still needs local multiplication control and a decaying tail. This compactness is used to make the forcing term continuous in energy; it does not retroactively make the original perturbation compact.

A perturbation of the highest derivatives need not be compact, even when its coefficients vanish outside a ball. A frequency cutoff changes this conclusion. It turns the localized perturbation into an integral operator, while decay of the coefficients controls the part at infinity. This is the mechanism that makes the forcing in a stationary first-order scattering equation continuous in energy.

We begin with integral kernels and rough coefficients. We then obtain an exact energy-factor remainder, prove every derivative estimate for its symbol, and apply the compactness result to a boundary resolvent. Read [Endpoint spaces and flat energy shells](endpoint-spaces-and-flat-energy-shells.md) for integral duality, [Admissible differential perturbations](admissible-differential-perturbations.md), Sections 1–3, for the local Sobolev multiplication estimate, and [Energy-shell factors and outgoing equations](energy-shell-factors-and-outgoing-equations.md) for the real energy root and outgoing evolution. The final application uses Theorem 1.1 and Section 6 of [Limiting absorption for long-range differential perturbations](limiting-absorption-for-long-range-differential-perturbations.md). Freely accessible background references are Yafaev [Y] and Teschl [T]. The kernel and remainder constructions below use finite differentiation, integration by parts and the explicit annular estimates.

Our convention is \(D=-i\partial\), with left quantization and the unitary Fourier transform. Fourier inversion and Plancherel with the normalization used here are proved in [Fourier facts](../providers/analysis/finite-derivative-l2.md#fourier-normalization). The same reading supplies the [measure and product proofs](../providers/analysis/finite-derivative-l2.md#euclidean-products). [Approximation and convolution](../providers/analysis/euclidean-approximation-and-convolution.md) proves Hölder, local smooth Sobolev approximation and, in Proposition 5.1, the Riemann–Lebesgue statement used in Solution 3. The endpoint lesson, Theorem 1.1, proves the completeness and duality of \(B,B^*\).

## 1. Frequency localization in the endpoint spaces

Put \(X(x)=(1+|x|^2)^{1/2}\). For \(n\ge1\), define

\[
 \begin{gathered}
 r_j=2^j,\qquad S_0=\{|x|<1\},\\
 S_j=\{2^{j-1}\le |x|<2^j\}\quad(j\ge1),\\
 \|f\|_B=\sum_j r_j^{1/2}\|f\|_{L^2(S_j)},\\
 \|v\|_{B^*}=\sup_j r_j^{-1/2}\|v\|_{L^2(S_j)}.
 \end{gathered}
 \tag{1}
\]

On \(S_j\), \(X\) is comparable to \(r_j\), with constants independent of \(j\). The derivative graph space is

\[
 \begin{gathered}
 \mathcal Y_m=\{u:D^\gamma u\in B^*,\ |\gamma|\le m\},\\
 \|u\|_{\mathcal Y_m}
     =\sum_{|\gamma|\le m}\|D^\gamma u\|_{B^*}.
 \end{gathered}
 \tag{2}
\]

Its derivatives are distributional derivatives of one \(u\). On each fixed ball this norm controls the \(H^m\) norm after multiplication by a fixed smooth cutoff. All its elements are tempered distributions: the shell estimate makes \(X^{-b}u\) square integrable for \(b>1/2\), and Cauchy–Schwarz then bounds its action on Schwartz tests.

Let \(b(x,\xi)\) be smooth, supported in one fixed compact frequency set, with every frequency derivative uniformly bounded. Its kernel is

\[
 \begin{aligned}
 K_b(x,y)&=(2\pi)^{-n}\int
       e^{i(x-y)\cdot\xi}b(x,\xi)\,d\xi,\\
 |K_b(x,y)|&\le C_N(1+|x-y|)^{-N}.
 \end{aligned}
 \tag{3}
\]

Integration by parts in frequency proves the second line for every integer \(N\). Only finitely many frequency derivatives are needed for each such bound.

**Lemma 1.1.** A measurable kernel satisfying the second line of (3) defines a bounded operator \(B\to B\). The bound is uniform when the required finite kernel constants are uniform.

**Proof.** Let \(T_{jk}=1_{S_j}T1_{S_k}\), viewed between the corresponding \(L^2\) spaces. If \(|j-k|\le2\), both absolute kernel integrals are uniformly bounded. The Schur estimate gives \(\|T_{jk}\|\le C\). This estimate follows directly by applying Cauchy–Schwarz with measure \(|K(x,y)|\,dy\), then integrating in \(x\).

If \(|j-k|\ge3\), the distance is at least \(c\max(r_j,r_k)\). The square integral of the kernel gives

\[
 \|T_{jk}\|
 \le C_N r_j^{n/2}r_k^{n/2}
               \max(r_j,r_k)^{-N}.
 \tag{4}
\]

Thus the relevant matrix coefficients are

\[
 d_{jk}=r_j^{1/2}\|T_{jk}\|r_k^{-1/2}.
 \tag{5}
\]

Their sum over \(j\), with \(k\) fixed, is bounded uniformly. There are at most five near terms, and their radius ratios are bounded. For \(j\ge k+3\), the sum of the bound from (4) is at most \(C r_k^{n-N}\), since \(N>(n+1)/2\). For \(j\le k-3\), the geometric sum of \(r_j^{(n+1)/2}\) gives the same bound. Choose \(N>n+2\).

The triangle inequality on each output shell now gives

\[
 \begin{aligned}
 \|Tf\|_B
 &\le \sum_k\left(\sum_j d_{jk}\right)
                   r_k^{1/2}\|f\|_{L^2(S_k)}
 \\
 &\le C\|f\|_B.
 \end{aligned}
 \tag{6}
\]

The annular series is absolutely convergent in \(B\), and defines the operator on every input. \(\square\)

In particular, a compactly supported smooth Fourier multiplier \(\chi(D)\) is bounded on \(B\). Its adjoint is \(\overline\chi(D)\), which has the same property. Integral duality therefore gives boundedness on \(B^*\) as well. On tempered distributions this dual action agrees with Fourier multiplication.

## 2. A decay gap makes an integral kernel compact

**Theorem 2.1.** Suppose \(K\) is continuous and, for some \(\epsilon>0\),

\[
 \begin{gathered}
 |K(x,y)|\le C_N X(x)^{-1-\epsilon}
                    (1+|x-y|)^{-N}\\
 \quad\text{for every }N.
 \end{gathered}
 \tag{7}
\]

Then its integral operator is compact \(B^*\to B\). It sends bounded weak-star convergent sequences in \(B^*\) to norm-convergent sequences in \(B\).

**Proof.** The near-shell Schur estimate and the far-shell square-integral estimate give

\[
 \begin{aligned}
 \|T_{jk}\|&\le C r_j^{-1-\epsilon}
                          \quad(|j-k|\le2),\\
 \|T_{jk}\|&\le C_N r_j^{-1-\epsilon}
       r_j^{n/2}r_k^{n/2}\\
 &\quad\cdot\max(r_j,r_k)^{-N}
                          \quad(|j-k|\ge3).
 \end{aligned}
 \tag{8}
\]

Set

\[
 a_{jk}=r_j^{1/2}\|T_{jk}\|r_k^{1/2}.
 \tag{9}
\]

The double sum of these coefficients is finite. Near the diagonal it is bounded by \(C\sum_j r_j^{-\epsilon}\). For \(j\ge k+3\), first sum over \(k\); the resulting bound is \(C_N r_j^{n-\epsilon-N}\). For \(k\ge j+3\), first sum over \(j\); the bound is

\[
 C_N(1+k)r_k^{(n+1)/2-N}
             \max(1,r_k^{(n-1)/2-\epsilon}).
 \tag{10}
\]

The factor \(1+k\) also covers a zero exponent in the inner geometric sum. Taking \(N>n+2+\epsilon\) makes both remaining sums converge. Consequently

\[
 \|Tv\|_B\le\left(\sum_{j,k}a_{jk}\right)\|v\|_{B^*}.
 \tag{11}
\]

This proves absolute convergence of the annular operator series. Truncating both indices at \(J\) changes its norm by at most the omitted coefficient sum, which tends to zero.

Each finite truncation has a square-integrable kernel on a bounded product of balls. Here is its finite-rank approximation. Extend the kernel by zero to a containing product box. The Euclidean rectangle-density proof approximates it in \(L^2\) by finite linear combinations of indicators of rectangles in \(\mathbb R^{2n}\). Each such rectangle is \(E\times F\) with \(E,F\subset\mathbb R^n\), so its operator has the one-dimensional range spanned by \(1_E\). Cauchy–Schwarz followed by product integration bounds the operator norm of the error by the \(L^2\) norm of the kernel error. Restrict these approximants back to the input and output balls. They still have finite rank and converge in operator norm. Restriction from \(B^*\) to that ball and inclusion from supported \(L^2\) into \(B\) are bounded, so the same approximation holds between the endpoint spaces.

A bounded set in a finite-dimensional range has finite nets at every positive radius, by a grid in its coordinates. Uniform operator-norm approximation transfers such finite nets to the image of the unit ball under the limiting operator. Every sequence in this image has a Cauchy subsequence, by successively taking subsequences in balls of radii tending to zero. Completeness of \(B\) gives a convergent subsequence. This proves compactness of each truncation and of their operator-norm limit with the actual endpoint norms.

Now let \(v_l\rightharpoonup^*v\), with uniformly bounded endpoint norms. On a fixed ball this is weak \(L^2\) convergence, because every supported \(L^2\) test belongs to \(B\). A compact \(L^2\) operator sends such a sequence to a norm-convergent sequence: every convergent subsequence of its image has the weak limit \(Tv\), and compactness excludes any other behavior. Apply this to a finite truncation. Its uniformly small operator-norm error proves the assertion for \(T\). \(\square\)

The positive decay gap is essential. Exercise 2 gives a kernel of weight \(X^{-1}\) whose action does not even map \(B^*\) into \(B\). None of this proof assumes norm density of compact tests in \(B^*\).

## 3. Rough differential coefficients after a frequency cutoff

For a term of order \(|\gamma|<m\), put \(k=m-|\gamma|\) and use

\[
 p_\gamma=
 \begin{cases}
 n/k,&n>2k,\\
 \text{a fixed finite }p>2,&n=2k,\\
 2,&n<2k.
 \end{cases}
 \tag{12}
\]

Let \(p_\gamma=\infty\) at order \(m\). The local multiplication estimate from the prerequisite is

\[
 \begin{gathered}
 \|aD^\gamma w\|_2
 \le C\|a\|_{L^{p_\gamma}(B(y,1))}
                      \|w\|_{H^m},\\
 \quad w\in C_c^\infty(B(y,1)).
 \end{gathered}
 \tag{13}
\]

At order \(m\) this is just bounded multiplication; an essential supremum suffices. At lower orders it is the sharp finite Sobolev estimate followed by Hölder.

**Theorem 3.1.** Suppose

\[
 \begin{gathered}
 V_S=\sum_{|\gamma|\le m}a_\gamma(x)D^\gamma,\\
 \|a_\gamma\|_{L^{p_\gamma}(B(y,1))}
      \le C_\gamma X(y)^{-1-\epsilon},
 \qquad \epsilon>0.
 \end{gathered}
 \tag{14}
\]

The coefficients are measurable. Then \(V_S:\mathcal Y_m\to B\) is bounded, with its actual local coefficient products. If \(T\) has a smooth kernel satisfying (3), then \(TV_S:\mathcal Y_m\to B\) is compact and sends bounded derivative-wise weak-star convergence to norm convergence.

**Proof: the differential action and its tail.** Choose a smooth \(\theta_y(x)=\theta(x-y)\) supported in \(B(y,1)\), equal to one on \(B(y,1/2)\). On the latter ball the derivatives of \(\theta_yu\) equal those of \(u\). Use (13), then integrate over the centers \(y\) whose half-balls meet \(S_j\). Every such center has \(X(y)\) comparable to \(r_j\); the case of the first few shells is absorbed into a fixed constant. The product rule and Fubini give

\[
 \begin{aligned}
 \|V_Su\|_{L^2(S_j)}^2
 &\le C r_j^{-2-2\epsilon}
       \sum_{|\beta|\le m}
       \|D^\beta u\|_{L^2(E_j)}^2,\\
 E_j&=\{x:\operatorname{dist}(x,S_j)<2\}.
 \end{aligned}
 \tag{15}
\]

To see the Fubini step explicitly, each term in
\(D^\beta(\theta_yu)\) is a fixed derivative of \(\theta(x-y)\) times one derivative of \(u(x)\). Its squared integral in \(y\) is bounded by the squared \(L^2\) norm of that derivative of \(\theta\). The smaller-ball integral on the left counts each \(x\in S_j\) for a set of centers of fixed positive volume. This proves (15). The estimates extend to local \(H^m\) inputs by smooth approximation and Hölder.

The enlarged shell \(E_j\) lies in a fixed number of neighboring shells, apart from a fixed bounded set for small \(j\). Its derivative mass is at most \(C r_j\|u\|_{\mathcal Y_m}^2\). Hence

\[
 \begin{aligned}
 \|V_Su\|_B&\le C\sum_j r_j^{-\epsilon}
                                  \|u\|_{\mathcal Y_m},\\
 \|1_{\{|x|\ge r_J\}}V_Su\|_B
     &\le C r_J^{-\epsilon}\|u\|_{\mathcal Y_m}.
 \end{aligned}
 \tag{16}
\]

These products are locally in \(L^2\), so their action is unambiguous.

**Proof: compactness on bounded inputs.** By Lemma 1.1 and (16), it suffices to consider \(T1_{\{|x|<R\}}V_S\). Truncate each lower-order coefficient in value. On this ball the bounded truncations converge in the finite \(L^{p_\gamma}\) norm. A smooth cutoff equal to one on the ball, (13), and a finite cover give

\[
 \begin{gathered}
 a_\gamma^{(M)}
       =a_\gamma1_{\{|a_\gamma|\le M\}},\\
 \|1_{\{|x|<R\}}(a_\gamma-a_\gamma^{(M)})
                    D^\gamma u\|_2
       \le o_M(1)\|u\|_{\mathcal Y_m}.
 \end{gathered}
 \tag{17}
\]

Supported \(L^2\) embeds boundedly in \(B\). Lemma 1.1 therefore also controls the error after \(T\). Highest-order coefficients are already bounded on the ball and need no approximation.

For a bounded, supported coefficient \(a\), the kernel \(K(x,y)a(y)\) defines a compact map \(L^2(B(0,R))\to B\). After restricting the output to a ball it is square integrable. Its remaining output shells have square-integral norm at most \(C_{N,R}r_j^{n/2-N}\), by (3). Their \(B\)-weighted sum tends to zero for \(N>(n+1)/2\). Thus the bounded-output compact operators converge in norm. Compose this map with the bounded component \(u\mapsto D^\gamma u|_{B(0,R)}\), and use (17), then (16). This proves compactness.

For derivative-wise weak-star convergence, each restricted component converges weakly in \(L^2\). The compact operators just constructed give strong convergence. The coefficient and spatial truncation errors are uniform on the bounded graph ball. Taking those errors to zero proves the final assertion. \(\square\)

In particular, no compactness of the unsmoothed highest-order differential term was used. Exercise 3 shows why it would be false.

## 4. The energy-factor cancellation is exact

Write \(x=(s,z)\) and \(\xi=(\xi_1,\eta)\). Let \(P_0\) be a real elliptic polynomial of degree \(m\). In a fixed regular graph collar suppose the smooth real long-range polynomial

\[
 L(x,\xi)=\sum_{|\gamma|\le m}\ell_\gamma(x)\xi^\gamma
 \tag{18}
\]

has the root and quotient from the energy-shell lesson:

\[
 \begin{aligned}
 &P_0(\xi)+L(x,\xi)-\lambda\\
 &\quad=(\xi_1-a(x,\eta,\lambda))Q(x,\xi,\lambda).
 \end{aligned}
 \tag{19}
\]

Choose a fixed \(\chi\in C_c^\infty\) in a smaller collar where \(Q\) never vanishes. Set

\[
 b_\lambda=\chi/Q,\qquad T_\lambda=b_\lambda(x,D).
 \tag{20}
\]

Extend \(a\) by a transverse frequency cutoff equal to one over the projection of \(\operatorname{supp}\chi\); denote the extension by \(\widetilde a\). The coefficient bounds and a sufficiently large region where \(L=0\) guarantee the uniform collar and reciprocal estimates. They are the hypotheses of the root construction, not consequences of a formal division.

Right composition with a constant Fourier multiplier is exact symbol multiplication. Also, left multiplication by \(\ell_\gamma(x)\) is exact multiplication of the left symbol. Equation (19) consequently gives

\[
 \begin{aligned}
 R_\lambda
 &:=(D_s-\widetilde a(x,D_z))\chi(D)\\
 &\quad-T_\lambda(P_0(D)+L(x,D)-\lambda)\\
 &=-\sum_{|\gamma|\le m}
                  [T_\lambda,\ell_\gamma]D^\gamma.
 \end{aligned}
 \tag{21}
\]

The kernel of the operator before \(D^\gamma\) in the last line is

\[
 H_{\gamma,\lambda}(x,y)
   =K_{b_\lambda}(x,y)
                     (\ell_\gamma(x)-\ell_\gamma(y)).
 \tag{22}
\]

In particular, the sign in (21) is fixed by the two different locations of the coefficient in this kernel. No asymptotic series is needed to prove the identity.

Assume the smooth long-range derivative bounds

\[
 \begin{gathered}
 0<\delta<1/3,\qquad r=(1+\delta)/2,\\
 \mu(k)=
 \begin{cases}
 \delta+k,&0\le k\le2,\\
 1+rk,&k\ge2,
 \end{cases}\\
 |\partial^\beta\ell_\gamma(x)|
                \le C_\beta X(x)^{-\mu(|\beta|)}.
 \end{gathered}
 \tag{23}
\]

The two formulas for \(\mu(2)\) coincide. The root and reciprocal estimates imply that every frequency derivative of \(b_\lambda\) is bounded, and, at every positive physical order,

\[
 |\partial_x^\beta\partial_\xi^\alpha b_\lambda|
       \le C_{\alpha\beta}X^{-\mu(|\beta|)}
                  \quad(|\beta|\ge1).
 \tag{24}
\]

If \(|x-y|\le X(x)/2\), the connecting segment has comparable \(X\). The first-derivative bound for \(\ell_\gamma\) gives

\[
 |\ell_\gamma(x)-\ell_\gamma(y)|
       \le C X(x)^{-1-\delta}|x-y|.
 \tag{25}
\]

In the complementary region the coefficients are bounded and \(X(x)\le2|x-y|\). Absorb the required power of \(|x-y|\) into the arbitrarily rapid kernel decay. Thus (22) satisfies (7) with \(\epsilon=\delta\).

**Corollary 4.1.** The exact remainder \(R_\lambda:\mathcal Y_m\to B\) is compact and sends bounded derivative-wise weak-star convergence to strong \(B\) convergence.

**Proof.** Apply Theorem 2.1 to each kernel (22), then compose with \(u\mapsto D^\gamma u\). There are finitely many terms. \(\square\)

The identity holds on all of \(\mathcal Y_m\). One way to verify this extension is distributional transposition. The compact-frequency symbols and all their physical derivatives are bounded; their kernels and their transposes preserve Schwartz space. Multiplication by the present smooth coefficients and polynomial differentiation do so as well. The Schwartz identity (21) therefore extends to tempered distributions. The annular actions in Corollary 4.1 agree with these distributional actions by testing the absolutely convergent kernel series.

## 5. Every derivative of the remainder symbol

Compactness required only (25). We can also prove the full smooth symbol assertion directly.

**Theorem 5.1.** The left symbol \(\rho_\lambda\) of \(R_\lambda\) satisfies, for every \(\alpha,\beta,N\),

\[
 |\partial_x^\beta\partial_\xi^\alpha\rho_\lambda|
       \le C_{\alpha\beta N}
                 X^{-1-\delta-r|\beta|}
                 \langle\xi\rangle^{-N}.
 \tag{26}
\]

It therefore belongs to \(S(X^{-1-\delta},G_\delta)\), where

\[
 G_\delta=X^{-2\delta}|dx|^2
                      +\langle\xi\rangle^{-2}|d\xi|^2.
 \tag{27}
\]

Here membership means the coordinate inequalities with factors
\(X^{-\delta|\beta|}\langle\xi\rangle^{-|\alpha|}\).

**Proof.** Put \(w=x-y\) and

\[
 \begin{aligned}
 k_\lambda(x,w)&=(2\pi)^{-n}
           \int e^{iw\cdot\xi}b_\lambda(x,\xi)\,d\xi,\\
 h_{\gamma,\lambda}(x,w)
      &=k_\lambda(x,w)
                (\ell_\gamma(x)-\ell_\gamma(x-w)).
 \end{aligned}
 \tag{28}
\]

Every \(w\) derivative of \(k_\lambda\) is still rapidly decreasing in \(w\), because it inserts a polynomial in the compact frequency variable. Every positive physical derivative also gains \(X^{-\mu(|\beta|)}\), by (24).

After distributing \(\beta\) between the two factors, let \(q\) be the physical order on the coefficient difference. In \(|w|\le X/2\), with no \(w\) derivative on that difference, the segment formula bounds it by \(C X^{-\mu(q+1)}|w|\). With a positive \(w\) derivative, its order on \(\ell_\gamma(x-w)\) is at least \(q+1\), so its bound is \(C X^{-\mu(q+1)}\). The elementary inequalities

\[
 \begin{aligned}
 \mu(q+1)&\ge1+\delta+rq
                               &&(q\ge0),\\
 \mu(k)&\ge\delta+rk
                               &&(k\ge1)
 \end{aligned}
 \tag{29}
\]

give, for every physical and \(w\) derivative,

\[
 |\partial_x^\beta\partial_w^\nu h_{\gamma,\lambda}|
 \le C_{\beta\nu M}
           X^{-1-\delta-r|\beta|}(1+|w|)^{-M}.
 \tag{30}
\]

For the first inequality in (29), check \(q=0\) directly and use \(1+r(q+1)\ge1+\delta+rq\) for \(q\ge1\). The second follows from \(r\le1\) at \(k=1\), and \(1\ge\delta\) at higher orders. The factor \(|w|\) is absorbed in the rapid kernel bound. If a positive physical order hits \(k_\lambda\), its second bound in (29) provides at least the remaining \(r\) cost.

Outside \(|w|\le X/2\), all coefficient derivatives are bounded. Since \(X\le2|w|\), arbitrarily high kernel decay supplies every fixed power of \(X\) required in (30). This estimates the already differentiated expression in two regions; no derivative of a discontinuous region cutoff is taken.

The exact left symbol of the kernel (22) is

\[
 c_{\gamma,\lambda}(x,\xi)
    =\int e^{-iw\cdot\xi}h_{\gamma,\lambda}(x,w)\,dw.
 \tag{31}
\]

A frequency derivative inserts \(w^\alpha\). Integrate by parts with \((1-\Delta_w)^M\); (30) makes all resulting terms integrable with the same physical weight. This proves arbitrary frequency decay for every derivative of \(c_{\gamma,\lambda}\). Right composition with \(D^\gamma\) multiplies its symbol exactly by \(\xi^\gamma\), so

\[
 \rho_\lambda=\sum_{|\gamma|\le m}
                             c_{\gamma,\lambda}\xi^\gamma.
 \tag{32}
\]

Polynomial multiplication preserves arbitrary frequency decay, proving (26). Finally \(r\ge\delta\), and we may choose \(N\ge|\alpha|\). These observations give the precise coordinate inequalities for (27). \(\square\)

## 6. Continuous forcing for the outgoing equation

Work on a sufficiently small compact energy interval \(I\) around a fixed regular energy. Use one common graph collar and one fixed cutoff \(\chi\). The free root \(E(\eta,\lambda)\) is smooth there. In the contraction proof for \(a-E\), energy is an additional external parameter: derivatives of \(E\) and of the positive divided difference are bounded on the common collar. Differentiating the fixed-point identity isolates the same invertible scalar factor at each order. Every physical derivative still has exactly the decay cost in (23); energy derivatives carry no physical derivative cost. The quotient recurrence and differentiated reciprocal identity have the same property.

It follows that all the kernel bounds above are uniform for \(\lambda\in I\), and the kernels of differences gain a factor \(C|\lambda-\lambda'|\). The finite-seminorm shell estimates therefore imply

\[
 \begin{aligned}
 \|T_\lambda-T_{\lambda'}\|_{B\to B}
       &\le C|\lambda-\lambda'|,\\
 \|R_\lambda-R_{\lambda'}\|_{\mathcal Y_m\to B}
       &\le C|\lambda-\lambda'|.
 \end{aligned}
 \tag{33}
\]

Theorem 3.1 and the first line also make \(T_\lambda V_S\) norm continuous as a compact map \(\mathcal Y_m\to B\).

Now suppose \(H=P_0(D)+L(x,D)+V_S(x,D)\) is the self-adjoint admissible operator of the limiting-absorption theorem. Let \(I\) avoid its eigenvalues and the critical free energies. For \(f\in B\), put

\[
 \begin{aligned}
 u_\lambda&=(H-\lambda-i0)^{-1}f,\\
 v_\lambda&=\chi(D)u_\lambda,\\
 g_\lambda&=T_\lambda f-T_\lambda V_Su_\lambda
                                      +R_\lambda u_\lambda.
 \end{aligned}
 \tag{34}
\]

Choose the frequency collar so that \(\partial_{\xi_1}P_0>0\). The exact equation is

\[
 (D_s-\widetilde a(x,D_z,\lambda))v_\lambda=g_\lambda.
 \tag{35}
\]

**Theorem 6.1.** The forcing in (34) belongs to \(B\), depends continuously on \(\lambda\) in its norm, and satisfies

\[
 \|g_\lambda\|_B\le C_I\|f\|_B.
 \tag{36}
\]

The solution \(v_\lambda\) is the unique outgoing solution and has square-integrable transverse slices with

\[
 \|v_\lambda(s,\cdot)\|_2
     \le C_I\int_{-\infty}^s
                      \|g_\lambda(t,\cdot)\|_2\,dt.
 \tag{37}
\]

The conclusions about continuity and the uniform estimate also hold with strongly varying \(B\) forcing.

**Proof.** Limiting absorption bounds \(u_\lambda\) in \(\mathcal Y_m\) uniformly on \(I\), and gives derivative-wise weak-star continuity, jointly with strong \(B\) forcing. Theorems 2.1 and 3.1 convert this convergence into strong convergence of \(R_\lambda u_\lambda\) and \(T_\lambda V_Su_\lambda\). For example, subtract the two values, first vary the operator with its norm estimate, then apply the fixed compact operator to the weak-star convergent graph. Lemma 1.1 treats \(T_\lambda f\). These statements prove the continuity and (36).

For completeness, the full directional radiation condition implies the particular outgoing condition needed in (37). On the frequency support choose \(\kappa>0\) such that
\(\partial_{\xi_1}P_0/|\nabla P_0|\ge2\kappa\). Take a smooth angular function \(\zeta\) equal to one when \(s/|x|\le\kappa/2\), and zero when \(s/|x|\ge\kappa\). Let \(\vartheta(x)\) be a radial smooth function equal to zero near zero and one outside a ball. Then

\[
 h(x,\xi)=\vartheta(x)\zeta(x/|x|)\chi(\xi)
 \tag{38}
\]

is smooth, belongs to \(S(1,G_1)\), and vanishes on every positive free-velocity ray over the energy surface. The apparent angular expression near zero is removed by \(\vartheta\). Radiation therefore gives \(h(x,D)u_\lambda\in\dot B^*\).

The norm closure \(\dot B^*\) of Schwartz space has vanishing ball mass divided by radius. Indeed the ball/shell bound gives a limsup at most \(C\|w-w_0\|_{B^*}^2\) for any Schwartz approximation \(w_0\); its own normalized ball mass tends to zero, and the error can be made arbitrarily small. For each fixed \(T\), (38) equals \(\chi(D)u_\lambda\) on \(s<T\) outside a sufficiently large ball. The omitted bounded region has finite mass. Consequently

\[
 \lim_{R\to\infty}R^{-1}
     \int_{\substack{|x|<R\\s<T}}|v_\lambda(x)|^2\,dx=0.
 \tag{39}
\]

Also \(v_\lambda\in B^*\), by the Fourier-multiplier consequence of Lemma 1.1. The root-cutoff application of the outgoing evolution theorem now applies to (35), yielding uniqueness and (37). This includes \(n=1\), when the transverse space is \(\mathbb C\). \(\square\)

### Use the conclusion

Check the exact energy-factor cancellation before estimating its remainder symbol. Then verify kernel compactness locally and uniformly small tails separately in the boundary-resolvent application.

## 7. Exercises with complete solutions

**Exercise 1 — Foundation: the exact sign.** In one dimension take \(P_0(\xi)=\xi^2\), \(\lambda=1\), and a real smooth \(\ell(s)\) with \(|\ell|\le1/8\). On a positive-frequency collar set \(a(s)=\sqrt{1-\ell(s)}\), \(Q(s,\xi)=\xi+a(s)\), and \(b=\chi/Q\). Find the exact remainder in (21). What happens when \(\ell\) is constant?

**Solution 1.** The factorization is \(\xi^2+\ell-1=(\xi-a)(\xi+a)\). Since the transverse dimension is zero, \(\widetilde a\) is multiplication by \(a(s)\). We obtain

\[
 \begin{aligned}
 R&=(D_s-a)\chi(D_s)\\
  &\quad-b(s,D_s)(D_s^2+\ell-1),\\
 (Ru)(s)&=\int K_b(s,t)(\ell(s)-\ell(t))u(t)\,dt.
 \end{aligned}
 \tag{40}
\]

Indeed \(b(D_s)(D_s^2-1)\) is exact right Fourier multiplication, whereas \(b(D_s)\ell\) places \(\ell(t)\) at the input. The polynomial identity places \(\ell(s)\) at the output. Their subtraction gives the displayed sign. If \(\ell\) is constant, the difference is zero and the factorization is exact at operator level. This last conclusion is algebraic and requires no decay of a constant coefficient.

**Exercise 2 — Intermediate: the missing decay gap.** Let \(\omega\ge0\) be smooth, supported in a small ball, with integral one. For every \(n\ge1\), consider
\(Tv=X^{-1}(\omega*v)\) and \(v=X^{-(n-1)/2}\). Show that \(v\in B^*\) and \(Tv\notin B\). Explain what changes if \(X^{-1}\) is replaced by \(X^{-1-\epsilon}\).

**Solution 2.** On large shells, \(v^2\) is comparable to \(|x|^{-(n-1)}\). Radial integration gives squared shell mass comparable to \(r_j\), so the normalized \(B^*\) shell norms are bounded above and below. This also holds for \(n=1\), where \(v=1\). Near zero the function is bounded.

For \(x\) large and \(y\) in the support of \(\omega\), \(X(x-y)\) and \(X(x)\) are uniformly comparable. Positivity and integral one give \((\omega*v)(x)\asymp X(x)^{-(n-1)/2}\). Hence \(Tv\asymp X^{-(n+1)/2}\), its shell \(L^2\) norm is comparable to \(r_j^{-1/2}\), and each large shell contributes a positive constant to the \(B\) norm. The sum diverges. Its continuous kernel \(X(x)^{-1}\omega(x-y)\) satisfies every rapid distance bound, with weight \(X^{-1}\). The extra factor \(X^{-\epsilon}\) changes the shell contributions to \(r_j^{-\epsilon}\), whose sum converges, in agreement with Theorem 2.1.

**Exercise 3 — Intermediate: highest-order oscillations.** Choose real \(a,\phi\in C_c^\infty\) with \(a\phi\ne0\), and put
\(u_j=2^{-jm}\phi(x)e^{i2^jx_1}\). Show that this sequence is bounded and converges derivative-wise weak-star to zero in \(\mathcal Y_m\), but \(aD_1^mu_j\) has no norm-convergent subsequence in \(B\). Show that applying \(T=b(x,D)\) as in Theorem 3.1 repairs this.

**Solution 3.** The product rule shows that each derivative through order \(m\) is supported in the same ball and bounded in \(L^2\). At orders below \(m\) its norm tends to zero. At order \(m\), only \(D_1^m\) can have a nonvanishing leading term; it is \(\phi e^{i2^jx_1}\), with an \(L^2\) error tending to zero. Every pairing of this leading term with a supported \(L^2\) test tends to zero by the Riemann–Lebesgue lemma, since the product of the two functions is in \(L^1\). These facts prove derivative-wise weak-star convergence, and fixed support makes the endpoint bounds uniform.

Now \(aD_1^mu_j=a\phi e^{i2^jx_1}+o(1)\) in \(L^2\). The leading terms have one positive constant norm. Their pairwise inner products tend uniformly to zero as the smaller index tends to infinity: every difference of two distinct frequencies past index \(J\) has modulus at least \(2^J\), and the Fourier transform of \(|a\phi|^2\) tends to zero. Thus a tail is separated by a fixed positive \(L^2\) distance. It has no convergent subsequence. Convergence in \(B\) would imply convergence in \(L^2\), since \(\|f\|_2\le\|f\|_B\). Finally \(a\) is a short-range coefficient of every positive gap, and Theorem 3.1 gives \(T(aD_1^mu_j)\to0\) in \(B\).

**Exercise 4 — Intermediate: two singular coefficients.** In dimension four with \(m=2\), choose the critical exponent \(p=3\) for order zero. Give all coefficient and partner exponents. If \(\eta\in C_c^\infty\) equals one near zero, verify that
\(a_0=\eta|x|^{-1}\), \(a_1=\eta|x|^{-1/2}\), and \(a_2=\eta\) satisfy the coefficient hypotheses for terms of orders zero, one and two, respectively.

**Solution 4.** At order zero the derivative gap is two, so \(n=2k\). The chosen \(p_0=3\) has partner \(q_0=6\). At order one, \(k=1\), so \(p_1=4\) and \(q_1=4\). At order two the exponents are \(p_2=\infty\), \(q_2=2\). Each pair satisfies \(1/p+1/q=1/2\).

Near zero the radial integrals for the two finite coefficient norms are constant multiples of
\(\int_0^1 r^{3-3}\,dr\) and \(\int_0^1 r^{3-2}\,dr\), respectively; both converge. The highest coefficient is bounded. The full local norms are uniformly bounded because each finite-norm coefficient has finite global norm and compact support. Unit balls with centers outside a fixed larger ball see zero. On the remaining bounded set, \(X(y)^{-1-\epsilon}\) has a positive lower bound. Increasing the constant gives (14) for every fixed \(\epsilon>0\). Thus the differential products are bounded into \(B\), and their frequency-localized composition is compact, despite both lower coefficients being unbounded.

**Exercise 5 — Advanced: a translated graph with no norm limit.** Let \(\phi\in C_c^\infty(B(0,1/10))\) be nonzero, and set
\(w_j=r_j^{1/2}\phi(x-r_je_1)\). Prove that \(w_j\) is bounded and converges derivative-wise weak-star to zero in \(\mathcal Y_m\), while its norm does not tend to zero. For a kernel satisfying (7), prove \(\|Tw_j\|_B\le C r_j^{-\epsilon}\).

**Solution 5.** Each derivative has \(L^2\) norm \(r_j^{1/2}\|D^\gamma\phi\|_2\). Its support meets only the two shells adjacent to radius \(r_j\). Their radii are comparable to \(r_j\), which proves the upper endpoint bounds. For the zeroth derivative, one of the two shell pieces contains at least half its squared mass, giving a fixed positive lower bound. For a test in \(B\), the pairing with any derivative is bounded by its uniform endpoint norm times the \(B\) norm of the test on those receding shells. This tail tends to zero, proving weak-star convergence.

The shell matrix in (9) has the stronger column estimate

\[
 \sum_l a_{lk}\le C r_k^{-\epsilon}.
 \tag{41}
\]

For the near terms this is (8). For \(l\ge k+3\), summing the far estimate gives \(C r_k^{n-\epsilon-N}\). For \(l\le k-3\), it gives the expression in (10), with \(k\) fixed. Choose \(N>n+3+2\epsilon\); this expression is at most \(C r_k^{-\epsilon}\), including its factor \(1+k\). Applying (41) to the at most two input shells of \(w_j\) proves the requested bound. Thus compact remainders can have strongly vanishing images along graphs that have no norm convergence. This is precisely the convergence mechanism used for the second and third terms in (34).

## References

- [Y] Dmitri Yafaev, [*Lectures on scattering theory*, free author preprint, arXiv:math/0403213v1](https://arxiv.org/pdf/math/0403213v1), 12 March 2004; lecture notes prepared by Andrew Hassell. Section 1 provides scattering context. The endpoint kernel, exact commutator and energy-continuity proofs are written in this lesson.
- [T] Gerald Teschl, [*Mathematical Methods in Quantum Mechanics: With Applications to Schrödinger Operators*, free author's online second edition](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf), 2014, §6.3, equations (6.11)–(6.15), pp. 163–164. These give the square-integrable-kernel comparison. Section 2 above proves the finite-rank approximation and its extension to the endpoint norms, including both spatial tails.
