# The Rankin–Selberg method

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The Petersson product pairs two cusp forms over a modular surface. Inserting an Eisenstein series turns that pairing into a Dirichlet series of products of Fourier coefficients. The geometry supplies continuation and a functional equation; the Hecke recurrences supply its Euler factors. The residue then measures the average size of the coefficients.

We work at full level and use unnormalized Fourier coefficients. The distinction between the coefficient series, its zeta multiple and its completion is essential: their pole statements are different. All three functions will have separate names.

## 1. Unfolding with absolute convergence

Let \(k\ge2\) be even and write
\[
 f(z)=\sum_{n\ge1}a_nq^n,\qquad
 g(z)=\sum_{n\ge1}b_nq^n,\qquad q=e^{2\pi iz},
 \qquad f,g\in S_k(SL_2(\mathbb Z)).
\]
The zero space in a small weight causes no exception: every assertion then holds with zero forms. Put
\[
 H(z)=f(z)\overline{g(z)}y^k,\quad
 \langle f,g\rangle=\int_{\mathcal F}H(z)\,d\mu(z),\quad
 d\mu=\frac{dx\,dy}{y^2},
\tag{1.1}
\]
where \(\mathcal F=\{|x|\le1/2,\ |z|\ge1\}\), with its boundary counted once. The product is linear in its first argument. Since \(\operatorname{Im}(\gamma z)=y/|cz+d|^2\), the weight laws make \(H\) invariant. Moreover, the Petersson lesson, Theorem 2.1, gives
\[
 |H(z)|\le C_{f,g}\quad(z\in\mathfrak H).
\tag{1.2}
\]
On a period strip at height \(y\ge1\), the cusp expansions give \(|H(z)|\le C y^ke^{-4\pi y}\).

Use the preceding lesson, (1.4), with exactly its sign convention:
\[
 E(z,t)=\sum_{\Gamma_\infty\backslash\Gamma}
              \operatorname{Im}(\gamma z)^t,
 \qquad \Gamma=SL_2(\mathbb Z),\quad
 \Gamma_\infty=\{\pm T^j:j\in\mathbb Z\}.
\]
Here \(\operatorname{Re}t>1\); the primitive-row expression includes the factor \(1/2\). Set
\[
 D_{f,g}(u)=\sum_{n\ge1}a_n\overline{b_n}n^{-u},
 \qquad u=t+k-1.
\tag{1.3}
\]

**Lemma 1.1.** The series \(D_{f,g}\) converges absolutely and locally uniformly for \(\operatorname{Re}u>k\).

**Proof.** For \(\sigma>1\), (1.2) and cusp decay show
\[
 \int_0^\infty\int_0^1|f(x+iy)|^2y^{k+\sigma-2}\,dx\,dy<\infty:
\]
at zero the integrand after the \(x\)-integration is bounded by \(Cy^{\sigma-2}\), and at infinity it decays exponentially times a power. The coefficient estimate of the Petersson lesson, Theorem 2.1, bounds \(|a_n|\) by a constant times \(n^{k/2}\). Thus the Fourier series converges absolutely and uniformly for \(0\le x\le1\), \(\epsilon\le y\le M\), for every \(0<\epsilon<M\). Integrate the squares of its finite partial sums and pass to their uniform limit. Since \(\int_0^1e^{2\pi i(n-r)x}dx\) is one when \(n=r\) and zero otherwise, this gives
\[
 \int_0^1|f(x+iy)|^2dx
       =\sum_{n\ge1}|a_n|^2e^{-4\pi ny}.
\]
The diagonal series is locally uniformly convergent for \(y>0\), including after multiplication by \(y^{k+\sigma-2}\): its terms are bounded on each compact height interval by a constant times \(n^ke^{-4\pi n\epsilon}\). Apply the nonnegative continuous-series assertion of The upper half-plane and the modular group, Lemma 0.3, then substitute \(v=4\pi ny\). It yields
\[
 \int_0^\infty\int_0^1|f(x+iy)|^2y^{k+\sigma-2}dx\,dy
 =\frac{\Gamma(k+\sigma-1)}{(4\pi)^{k+\sigma-1}}
       \sum_{n\ge1}\frac{|a_n|^2}{n^{k+\sigma-1}}.
\tag{1.4}
\]
In particular the series on the right is finite. Apply the same argument to \(g\) and use weighted Cauchy–Schwarz:
\[
 \sum_{n\ge1}|a_n b_n|n^{-v}
 \le\left(\sum|a_n|^2n^{-v}\right)^{1/2}
     \left(\sum|b_n|^2n^{-v}\right)^{1/2}<\infty
 \quad(v>k).
\]
For a compact subset of \(\operatorname{Re}u>k\), take its minimum real part as \(v\). This gives a summable uniform majorant. ∎

This domain is better than the one obtained by separately inserting Hecke's coefficient bound. It requires no Ramanujan–Petersson theorem.

**Theorem 1.2 (the unfolding identity).** For \(\operatorname{Re}t>1\),
\[
 I_{f,g}(t):=\int_{\mathcal F}H(z)E(z,t)d\mu(z)
 =\frac{\Gamma(t+k-1)}{(4\pi)^{t+k-1}}
                  D_{f,g}(t+k-1).
\tag{1.5}
\]

**Proof.** First unfold the absolute values with the nonnegative series \(E(z,\sigma)\), \(\sigma=\operatorname{Re}t>1\). Its locally uniform convergence follows directly from the bottom rows: on a compact subset of \(\mathfrak H\), \(|cz+d|\ge\epsilon\sqrt{c^2+d^2}\) and \(y\) is bounded. Hence its summands \(y^\sigma|cz+d|^{-2\sigma}\) have a summable lattice majorant. The dyadic annulus of radius \(2^j\) contributes \(O(2^{(2-2\sigma)j})\), which is summable precisely for \(\sigma>1\). Multiplication by the continuous function \(|H|y^{-2}\) preserves local uniform convergence. The nonnegative plane-series assertion of the first lesson, Lemma 0.3, therefore permits the positive sum to pass through the integral on \(\mathcal F\).

In each term change variables \(w=\gamma z\). Invariance of \(H\) and of \(d\mu\) gives the integral of the period-one function \(|H(w)|\operatorname{Im}(w)^{\sigma-2}\) on \(\gamma\mathcal F\). The Petersson lesson, Lemma 4.0 with \(h=1\), projects these regions into the strip and proves their locally finite partition and the equality of the positive integrals. Consequently
\[
 \int_{\mathcal F}|H(z)|E(z,\sigma)d\mu
 =\int_0^\infty\int_0^1|H(x+iy)|y^{\sigma-2}dx\,dy<\infty.
\tag{1.6}
\]
The last inequality follows from the bound \(C_{f,g}y^{\sigma-2}\) near zero and \(Cy^{k+\sigma-2}e^{-4\pi y}\) near infinity. Joining these bounds on a compact height interval gives a continuous integrable majorant depending only on \(y\), so Lemma 0.3 also justifies the displayed iterated rectangular integral. The projected tiles are \(\bigcup_{r\in\mathbb Z}(T^r\gamma\mathcal F\cap\{0\le x<1\})\); a domain \(\gamma\mathcal F\) itself need not lie in one strip. Both groups contain \(-I\), which acts trivially, so there is no additional factor of two.

The complex coset summands have exactly this positive absolute majorant, since \(|\operatorname{Im}(\gamma z)^t|=\operatorname{Im}(\gamma z)^\sigma\). Their summed absolute integrals are finite by (1.6). The complex-series assertion of Lemma 0.3 and the absolute-integral part of Lemma 4.0 now unfold the complex integral:
\[
 I_{f,g}(t)=\int_0^\infty\int_0^1
                 f(x+iy)\overline{g(x+iy)}y^{t+k-2}dx\,dy.
\tag{1.7}
\]
On each compact positive-height rectangle both Fourier series converge absolutely uniformly, by the same coefficient estimate used in Lemma 1.1. Multiply their finite partial sums, integrate over \(x\), and pass to the uniform limit to obtain
\[
 \int_0^1 f(x+iy)\overline{g(x+iy)}dx
                  =\sum_{n\ge1}a_n\overline{b_n}e^{-4\pi ny}.
\tag{1.8}
\]
For \(u=t+k-1\), Lemma 1.1 shows that the integrals of the absolute values of these diagonal terms sum to
\[
 \frac{\Gamma(\operatorname{Re}u)}{(4\pi)^{\operatorname{Re}u}}
               \sum_{n\ge1}|a_n b_n|n^{-\operatorname{Re}u}<\infty.
\]
The diagonal series in (1.8), multiplied by \(y^{u-1}\), is uniformly convergent on each compact positive-height interval: its absolute terms are bounded there by a constant times \(n^ke^{-4\pi n\epsilon}\). Its absolute Mellin integrals have the finite sum just displayed. The one-variable complex-series assertion of Lemma 0.3 therefore permits the final Mellin integration. Its individual term is
\(\int_0^\infty e^{-4\pi ny}y^{u-1}dy=(4\pi n)^{-u}\Gamma(u)\), proving (1.5). ∎

## 2. The completed function and its residue

The preceding lesson proved
\[
 E^*(z,t)=\pi^{-t}\Gamma(t)\zeta(2t)E(z,t),\qquad
 E^*(z,t)=E^*(z,1-t),
\tag{2.1}
\]
with only possible simple poles at \(t=0,1\) and constant residues \(-1/2,+1/2\). Define
\[
 \begin{aligned}
 R_{f,g}(u)&=\zeta(2u-2k+2)D_{f,g}(u),\\
 \Lambda_{f,g}(u)&=(2\pi)^{-2u}\Gamma(u)\Gamma(u-k+1)R_{f,g}(u).
 \end{aligned}
\tag{2.2}
\]
Initially these are defined for \(\operatorname{Re}u>k\). Multiplying (1.5) by the completion factor, with \(t=u-k+1\), gives the exact comparison
\[
 J_{f,g}(t):=\int_{\mathcal F}H(z)E^*(z,t)d\mu(z)
           =\pi^{k-1}\Lambda_{f,g}(u).
\tag{2.3}
\]
Indeed \(\pi^{-t}(4\pi)^{-u}=\pi^{k-1}(2\pi)^{-2u}\). This constant controls every residue below.

**Lemma 2.1 (integration after continuation).** The integral defining \(J\) has meromorphic continuation with only possible simple poles at \(0,1\); its residues are \(-\langle f,g\rangle/2\) and \(+\langle f,g\rangle/2\). It satisfies \(J(t)=J(1-t)\).

**Proof.** We derive an integrable bound directly from the proved theta integral, rather than assume a spectral continuation theorem. In the notation of the preceding lesson, its equation (3.7) says
\[
\begin{gathered}
E^*(z,t)=\frac1{2(t-1)}-\frac1{2t}\\
+\frac12\int_1^\infty\left[\begin{gathered}
(\Theta_z(v)-1)\\
\cdot(v^{t-1}+v^{-t})\end{gathered}\right]dv.
\end{gathered}
\tag{2.4a}
\]
The last integral is entire for fixed \(z\). We now bound it uniformly in the cusp when \(t\) ranges over a compact set.

For \(a>0\) and any real shift \(b\), counting integers by their distance from \(-b\) and comparing a decreasing Gaussian with its integral gives
\[
\begin{gathered}
\sum_{n\in\mathbb Z}e^{-\pi a(n+b)^2}\le2+a^{-1/2},\\
\sum_{n\ne0}e^{-\pi an^2}
\le\sqrt{2/a}\,e^{-\pi a/2}.
\end{gathered}
\]
For the first bound, split the integers into the two rays on either side of \(-b\). On each ray, their distances have the form \(\delta+j\), with \(\delta\ge0\) and \(j\ge0\). A decreasing nonnegative function has \(\sum_{j\ge0}f(\delta+j)\le f(\delta)+\int_\delta^\infty f(t)dt\); each ray is therefore bounded by \(1+\int_0^\infty e^{-\pi at^2}dt\). For the second, split off \(e^{-\pi a/2}\) using \(n^2\ge1\), then bound the remaining positive sum by the Gaussian integral on \([0,\infty)\). Since
\(Q_z(m,n)=m^2y+(mx+n)^2/y\), separating \(m=0\) from \(m\ne0\) yields, for \(v,y\ge1\),
\[
\begin{gathered}
\Theta_z(v)-1\\
\le\sqrt{2y/v}\,e^{-\pi v/(2y)}\\
+\sqrt{2/(vy)}(2+\sqrt{y/v})e^{-\pi vy/2}\\
\le C\sqrt y\,e^{-\pi v/(2y)}.
\end{gathered}
\tag{2.4b}
\]
The constant is absolute and the estimate is uniform in \(x\). If \(|\operatorname{Re}t|\le A\), with \(A\ge0\), then \(|v^{t-1}+v^{-t}|\le2v^A\). Substituting \(v=yw\) bounds the entire part of (2.4a) by
\(C_A y^{A+3/2}\), since \(\int_0^\infty e^{-\pi w/2}w^A dw\) is finite. Multiplication by \(|H(z)|\le C y^ke^{-4\pi y}\) and by the measure factor \(y^{-2}\) gives an integrable majorant for every compact parameter set. On the compact remainder of \(\mathcal F\), the preceding lesson's Gaussian bound supplies the same domination. The entire part is jointly continuous in \((t,z)\), by its locally uniform Gaussian integral, and holomorphic in \(t\) for each \(z\). Apply the continuous holomorphic-parameter assertion of the first lesson, Lemma 0.3, with density \(y^{-2}\) and the majorant just obtained. Its compact Riemann sums and uniform integral tails prove that integrating this entire part gives an entire function.

Thus the only meromorphic terms in the integrated formula are
\(\langle f,g\rangle/(2(t-1))-\langle f,g\rangle/(2t)\). This proves both residues, including the case of a zero inner product. Both the rational expression and the two integral powers in (2.4a) are unchanged under \(t\mapsto1-t\), which proves the reflection after integration. No continuous-spectrum theorem is used. For comparison, writing \(\Xi(w)=\pi^{-w/2}\Gamma(w/2)\zeta(w)\), the preceding lesson's Fourier expansion has constant term
\[
 \Xi(2t)y^t+\Xi(2t-1)y^{1-t}.
\tag{2.4}
\]
The apparent poles of the two individual \(\Xi\)-terms at \(t=1/2\) cancel by (2.4a); treating them separately would conceal that cancellation. ∎

### Continuous integral route for the Gamma facts

The Gamma integral, recurrence, continuation and entire reciprocal used in Theorem 2.2 have their explicit integral and product proofs in The Gamma function and Stirling's formula, Theorems 1.1–1.2. The two integral limits in those proofs admit the following continuous route from lesson 01, Lemma 0.3.

On a compact parameter set in \(\operatorname{Re}z>0\), choose \(0<a\le\operatorname{Re}z\le b\). The integrand \(e^{-u}u^{z-1}\), for \(u>0\), is jointly continuous and holomorphic in \(z\), and its absolute value is bounded by the fixed continuous integrable function
\[
 M(u)=e^{-u}(u^{a-1}+u^{b-1}).
\]
The power integral converges at zero because \(a>0\); the exponential controls every fixed power at infinity, as follows by bounding that power with a sufficiently high term of the exponential series. The holomorphic-parameter part of Lemma 0.3 therefore proves holomorphy of the Gamma integral without differentiation under a measurable integral. Integration by parts, with these endpoint bounds, gives its recurrence.

For Gauss's limit, put \(F_N(u,z)=u^{z-1}(1-u/N)^N\) on \(0<u<N\), and zero on \(u\ge N\), where \(N\) is a positive integer. This is continuous on \(u>0\), including at \(u=N\), and \(|F_N(u,z)|\le M(u)\), since \(\log(1-v)\le-v\) for \(0\le v<1\). On \(0<\epsilon\le u\le B\) and \(N>2B\), the power series for the real logarithm gives
\[
 |N\log(1-u/N)+u|\le B^2/N.
\]
Hence \(F_N\to e^{-u}u^{z-1}\) uniformly on every compact positive-\(u\) interval, uniformly on the compact parameter set. Cut off the two tails using the same \(M\), then use this compact uniform estimate; the integrals converge uniformly in the parameters. This is precisely the continuous tail argument of Lemma 0.3. Repeated integration by parts in the finite beta integral and the affine substitution \(u=Nt\), justified directly by its interval Riemann sums, now give Gauss's limit.

The remaining finite-product argument is the explicit proof in Theorem 1.2 of the linked lesson: its logarithmic tails are \(O_K(n^{-2})\), uniformly on compact sets. The constant \(H_N-\log N\) converges by real completeness: it is decreasing because \(\log(1+1/N)\ge1/(N+1)\), and bounded below by the integral comparison \(H_N\ge\log(N+1)\). Thus that product converges locally uniformly to an entire function with just the stated simple zeros, and its product with Gamma equals one in the right half-plane and hence meromorphically everywhere. These arguments supply the Gamma facts needed here using continuous integrals; they do not assume a general measurable convergence theorem.

**Theorem 2.2 (continuation, functional equation and poles).** The function \(\Lambda_{f,g}\) is meromorphic on \(\mathbb C\), holomorphic except for possible simple poles at \(u=k,k-1\), and
\[
\begin{aligned}
 \Lambda_{f,g}(u)&=\Lambda_{f,g}(2k-1-u),\\
 \operatorname*{Res}_{u=k}\Lambda_{f,g}(u)&=\frac{\langle f,g\rangle}{2\pi^{k-1}},\\
 \operatorname*{Res}_{u=k-1}\Lambda_{f,g}(u)&=-\frac{\langle f,g\rangle}{2\pi^{k-1}}.
\end{aligned}
\tag{2.5}
\]
The series \(D\) has meromorphic continuation to \(\mathbb C\). In the half-plane \(\operatorname{Re}u>k-1/2\) it is holomorphic except for a possible simple pole at \(k\), with
\[
 \operatorname*{Res}_{u=k}D_{f,g}(u)
          =\frac{3(4\pi)^k}{\pi\Gamma(k)}\langle f,g\rangle.
\tag{2.6}
\]

**Proof.** Equation (2.3) and Lemma 2.1 give continuation, residues and reflection for \(\Lambda\), since \(t\mapsto u=t+k-1\) has derivative one. Define the continuation of the original series by
\[
 D_{f,g}(u)=
 \frac{(2\pi)^{2u}\Lambda_{f,g}(u)}
 {\Gamma(u)\Gamma(u-k+1)\zeta(2u-2k+2)}.
\tag{2.7}
\]
The reciprocal gamma functions are entire, and the reciprocal of a nonzero meromorphic function is meromorphic. Thus this gives a global meromorphic function agreeing with Lemma 1.1's series. If \(\operatorname{Re}u>k-1/2\), then \(\operatorname{Re}(2u-2k+2)>1\); the absolutely convergent zeta Euler product has no zero there. The second possible pole \(k-1\) is outside this half-plane. At \(u=k\), the denominator in (2.7) is \(\Gamma(k)\Gamma(1)\zeta(2)=\Gamma(k)\pi^2/6\). Combining it with the first residue in (2.5) gives (2.6). ∎

Outside this half-plane, zeros of \(\zeta(2u-2k+2)\) in (2.7) require a separate cancellation analysis. The completed function's two-pole theorem does not by itself give a global one-pole theorem for \(D\). Nor does \(D(u)=D(2k-1-u)\) hold without the factors in (2.2). An uncompleted form of the functional equation is the equality of those two completed expressions, interpreted meromorphically.

For the zeta multiple, (2.6) gives
\[
 \operatorname*{Res}_{u=k}R_{f,g}(u)
             =\frac{\pi(4\pi)^k}{2\Gamma(k)}\langle f,g\rangle.
\tag{2.8}
\]
In the unitary variable \(v=u-k+1\), put \(\lambda_f(n)=a_nn^{-(k-1)/2}\), and similarly for \(g\). Then
\[
 \begin{aligned}
 D_{f,g}(v+k-1)&=\sum_{n\ge1}\lambda_f(n)\overline{\lambda_g(n)}n^{-v},\\
 R_{f,g}(v+k-1)&=\zeta(2v)\sum_{n\ge1}\lambda_f(n)\overline{\lambda_g(n)}n^{-v}.
 \end{aligned}
\tag{2.9}
\]
The completed reflection is \(v\leftrightarrow1-v\), and the rightmost possible pole is \(v=1\). The coefficients have changed along with the variable.

**Corollary 2.3 (the global poles of the zeta multiple).** The function \(R_{f,g}\) is holomorphic on \(\mathbb C\) except for a possible simple pole at \(u=k\), whose residue is (2.8). At the other pole of the completion it has the finite value
\[
 R_{f,g}(k-1)
 =-\frac{(2\pi)^{2k-2}}{2\pi^{k-1}\Gamma(k-1)}
                         \langle f,g\rangle.
\tag{2.10}
\]

**Proof.** Removing the gamma factors in (2.2) gives
\[
 R_{f,g}(u)=(2\pi)^{2u}
           \frac{\Lambda_{f,g}(u)}{\Gamma(u)\Gamma(u-k+1)}.
\tag{2.11}
\]
The reciprocal gamma functions are entire, so Theorem 2.2 leaves only \(k\) and \(k-1\) as candidates for poles. Write \(u=k-1+\epsilon\). Since \(\Gamma(1+\epsilon)=\epsilon\Gamma(\epsilon)\) and \(\Gamma(1)=1\), we have \(1/\Gamma(\epsilon)=\epsilon+O(\epsilon^2)\). Also \(1/\Gamma(k-1+\epsilon)=1/\Gamma(k-1)+O(\epsilon)\), because \(k\ge2\). The Laurent expansion (2.5) is
\[
 \Lambda_{f,g}(k-1+\epsilon)
 =-\frac{\langle f,g\rangle}{2\pi^{k-1}\epsilon}+O(1).
\tag{2.12}
\]
Multiplying these three expansions in (2.11) cancels the lower pole and gives (2.10). This includes \(\langle f,g\rangle=0\), when the resulting value is zero. At \(k\) the gamma factors are finite and nonzero, giving (2.8). The possible zeros of the zeta denominator in (2.7) still govern the separate question of additional poles of \(D\). ∎

## 3. Four local roots

Suppose now that \(f,g\) are normalized simultaneous cusp eigenforms: \(a_1=b_1=1\). The level-one Hecke lesson, Theorems 4.2–4.3, proves multiplicativity and the prime-power recurrences. Factor
\[
 \begin{aligned}
 1-a_pX+p^{k-1}X^2&=(1-\alpha_1X)(1-\alpha_2X),\\
 1-b_pX+p^{k-1}X^2&=(1-\beta_1X)(1-\beta_2X).
 \end{aligned}
\tag{3.1}
\]
The roots are labeled without choosing an order. In particular \(\alpha_1\alpha_2=\beta_1\beta_2=p^{k-1}\). The local series of \(f\) is \(\sum_r a_{p^r}X^r=((1-\alpha_1X)(1-\alpha_2X))^{-1}\), and conjugating the second recurrence gives roots \(\overline{\beta_j}\).

**Lemma 3.1 (the local identity).** For arbitrary complex numbers \(A,B,C,D\), let \(h_r(A,B)=\sum_{j=0}^r A^{r-j}B^j\). As a formal power series,
\[
 \sum_{r\ge0}h_r(A,B)h_r(C,D)X^r
 =\frac{1-ABCDX^2}
 {(1-ACX)(1-ADX)(1-BCX)(1-BDX)}.
\tag{3.2}
\]
This includes coincident roots and zero roots.

**Proof.** If \(A\ne B\) and \(C\ne D\), sum the four geometric series in
\[
\begin{aligned}
 &\sum_{r\ge0}h_r(A,B)h_r(C,D)X^r\\
 &=\frac{1}{(A-B)(C-D)}
 \left(\begin{aligned}
 &\frac{AC}{1-ACX}-\frac{AD}{1-ADX}\\
 &\quad-\frac{BC}{1-BCX}+\frac{BD}{1-BDX}
 \end{aligned}\right).
\end{aligned}
\tag{3.3}
\]
Indeed \(h_r(A,B)=(A^{r+1}-B^{r+1})/(A-B)\), and the same holds for \(C,D\). On multiplying the expression in parentheses by the four denominators, its coefficients in degrees \(0,1,2,3\) are, respectively,
\[
 (A-B)(C-D),\quad0,\quad-ABCD(A-B)(C-D),\quad0.
\]
For example its degree-zero coefficient is \(AC-AD-BC+BD\); to verify the other three, put \(S_1=(A+B)(C+D)\) and let \(S_2\) be the sum of pairwise products of \(AC,AD,BC,BD\). The signed sum of their squares is \((A^2-B^2)(C^2-D^2)=S_1(A-B)(C-D)\), so the linear coefficient is zero. The signed sum of their cubes is \((A-B)(C-D)(A^2+AB+B^2)(C^2+CD+D^2)\). Thus the quadratic coefficient, divided by \((A-B)(C-D)\), is
\[
 S_2-S_1^2+(A^2+AB+B^2)(C^2+CD+D^2)=-ABCD,
\]
using \(S_2=(A^2+B^2)CD+AB(C^2+D^2)+2ABCD\). The cubic coefficient is minus the product of all four pair products times \(1-1-1+1\), hence zero. This proves (3.2) in the distinct-root case. After multiplying (3.2) by its denominator, every coefficient is a polynomial in \(A,B,C,D\). It vanishes on the dense set of distinct pairs, hence identically. The denominator has constant one, so it is invertible as a formal series even when roots coincide or vanish. ∎

**Theorem 3.2 (the Euler product).** For \(\operatorname{Re}u>k\),
\[
 D_{f,g}(u)=\prod_p
 \frac{1-p^{2k-2-2u}}
 {\prod_{i,j=1}^2(1-\alpha_i(p)\overline{\beta_j(p)}p^{-u})},
\tag{3.4}
\]
and therefore
\[
 R_{f,g}(u)=\prod_p\prod_{i,j=1}^2
              (1-\alpha_i(p)\overline{\beta_j(p)}p^{-u})^{-1}.
\tag{3.5}
\]
Both Euler products converge absolutely and locally uniformly in this half-plane.

**Proof.** Substitute \((A,B,C,D)=(\alpha_1,\alpha_2,\overline{\beta_1},\overline{\beta_2})\) into Lemma 3.1. The numerator is \(1-p^{2k-2}X^2\). Multiplicativity of both coefficient sequences shows that a finite product of the local series expands into \(\sum a_n\overline{b_n}n^{-u}\) over integers supported on the corresponding finite prime set. Lemma 1.1 permits passing to all primes, and bounds the sum of absolute values of all nonconstant local coefficients by \(\sum_{n\ge2}|a_n b_n|n^{-\operatorname{Re}u}\). Thus the product of local series converges absolutely, uniformly on compact subsets.

For completeness the rational denominators in (3.4) do not create an undefined expression in this domain. The diagonal version of Lemma 1.1 gives convergence of \(\sum_r|a_{p^r}|^2p^{-rv}\) for every \(v>k\). Its terms tend to zero. Hence the radius of convergence of \(\sum_r a_{p^r}X^r\) is at least \(p^{-k/2}\). The identity with the reciprocal quadratic, whose numerator is one, implies \(|\alpha_i|\le p^{k/2}\). The same argument applies to \(\beta_j\). Thus \(|\alpha_i\overline{\beta_j}p^{-u}|<1\) when \(\operatorname{Re}u>k\).

Finally \(\zeta(2u-2k+2)=\prod_p(1-p^{2k-2-2u})^{-1}\) is absolutely convergent there. Multiplying it by (3.4) cancels the numerators and gives (3.5), with the same absolute-product meaning. ∎

The coefficients in \(D\) are products of two coefficients. The extra zeta factor inserts further divisor terms; it is part of the degree-four Euler product rather than an optional normalization.

**Corollary 3.3 (the pole detects equality).** For normalized full-level eigenforms \(f,g\) of the same weight, \(\Lambda_{f,g}\) has a pole at \(k\) if and only if \(f=g\). If they are distinct, \(\Lambda_{f,g}\) is entire.

**Proof.** Distinct normalized eigenforms differ in some Hecke eigenvalue by the level-one multiplicity-one proof. Each \(T_n\) is self-adjoint, so its eigenvalues are real and the two eigenvectors are orthogonal. Equations (2.5) therefore remove both possible poles. If \(f=g\), positivity of the Petersson norm makes the residue at \(k\) strictly positive. ∎

The equality criterion refers here to \(R\) and its completion, or to \(D\) at its rightmost pole. It asserts no cancellation at other possible singularities of (2.7).

## 4. Mean squares, mixed averages and a computed discriminant example

We state the following precise form of **Wiener–Ikehara**. Suppose \(c_n\ge0\), \(a>0\), and \(F(u)=\sum c_nn^{-u}\) converges for \(\operatorname{Re}u>a\). If, for some \(r>0\), \(F(u)-r/(u-a)\) extends continuously to the closed half-plane \(\operatorname{Re}u\ge a\), then
\[
 \sum_{n\le x}c_n\sim \frac r a x^a.
\tag{4.1}
\]
This general theorem is stated for comparison: Gillet–Grayson, Appendix A, Theorem A.4, pp. 443–444. Their theorem allows increasing real exponents \(\lambda_n\) and includes the present choice \(\lambda_n=n\). For our cusp forms, the Petersson bound gives an additional elementary estimate. It lets us prove the mean-square limit below using the bounded-function analytic theorem already proved in The prime number theorem, Theorem 5.1.

For a nonzero \(f\), Theorem 2.2 makes \(D_{f,f}(u)-r_f/(u-k)\) holomorphic on the open half-plane \(\operatorname{Re}u>k-1/2\), where
\[
 r_f=\frac{3(4\pi)^k}{\pi\Gamma(k)}\|f\|^2>0.
\]
In particular it satisfies the entire boundary condition in (4.1), not merely a limit along the real axis. The mean-square conclusion, with its exact constant, is
\[
 \sum_{n\le x}|a_n|^2\sim c_fx^k,\qquad
 c_f=\frac{3(4\pi)^k}{\pi\Gamma(k+1)}\|f\|^2.
\tag{4.2}
\]
**Proof of (4.2).** Put \(A_f(x)=\sum_{n\le x}|a_n|^2\), for real \(x\ge1\). The Petersson lesson, Theorem 2.1, supplies a constant \(M_f\) with
\(y^{k/2}|f(t+iy)|\le M_f\) for all \(t\in\mathbb R\), \(y>0\). At each positive height the Fourier series converges absolutely and uniformly over a period. We may multiply it by its conjugate and integrate; orthogonality gives
\[
\begin{gathered}
\int_0^1|f(t+iy)|^2\,dt\\
=\sum_{n\ge1}|a_n|^2e^{-4\pi ny}\\
\le M_f^2y^{-k}.
\end{gathered}
\tag{4.2a}
\]
Take \(y=1/x\). For \(n\le x\), the exponential in (4.2a) is at least \(e^{-4\pi}\). Therefore
\[
0\le A_f(x)\le e^{4\pi}M_f^2x^k.
\tag{4.2b}
\]
This estimate uses the elementary invariant bound and holds for every cusp form, without an eigenform or optimal coefficient hypothesis.

Let \(c_f=r_f/k\), and for \(v\ge0\) define
\[
Q_f(v)=e^{-kv}A_f(e^v),\qquad h_f(v)=Q_f(v)-c_f.
\]
The functions are bounded and locally integrable; the finitely many jumps on a compact interval cause no problem. For \(\operatorname{Re}z>0\), the positive real majorant and Lemma 1.1 justify the sum–integral interchange in
\[
\begin{aligned}
&\int_0^\infty Q_f(v)e^{-zv}\,dv\\
&=\sum_{n\ge1}|a_n|^2
  \int_{\log n}^\infty e^{-(k+z)v}\,dv\\
&=\frac{D_{f,f}(k+z)}{k+z}.
\end{aligned}
\tag{4.2c}
\]
For example, the sum of the absolute integrals is
\(D_{f,f}(k+\operatorname{Re}z)/(k+\operatorname{Re}z)<\infty\). Thus the Laplace transform of \(h_f\) is
\[
G_f(z)=\frac{D_{f,f}(k+z)}{k+z}-\frac{c_f}{z}.
\]
Write \(B_f(z)=D_{f,f}(k+z)-r_f/z\). Theorem 2.2 makes \(B_f\) holomorphic on \(\operatorname{Re}z>-1/2\), with its value at zero obtained by removing the pole. Since \(r_f=kc_f\),
\[
G_f(z)=\frac{B_f(z)-c_f}{k+z}.
\tag{4.2d}
\]
The denominator has no zero on this half-plane because \(k\ge2\). Hence \(G_f\) extends holomorphically to an open set containing \(\operatorname{Re}z\ge0\), including zero and every point of the imaginary axis.

Newman's analytic theorem, with its complete contour proof in the programme lesson cited above, now applies to the bounded locally integrable function \(h_f\). It gives convergence of \(\int_0^T h_f(v)\,dv\) as \(T\to\infty\). In particular, for every fixed \(b>0\),
\[
\begin{aligned}
\int_v^{v+b}Q_f(w)\,dw&\longrightarrow c_fb,\\
\int_{v-b}^{v}Q_f(w)\,dw&\longrightarrow c_fb.
\end{aligned}
\tag{4.2e}
\]
The second limit is taken with \(v\ge b\).

We remove the average using monotonicity of \(A_f\). For \(0\le t\le b\) and \(v\ge b\),
\[
\begin{aligned}
Q_f(v+t)&\ge e^{-kt}Q_f(v),\\
Q_f(v-t)&\le e^{kt}Q_f(v).
\end{aligned}
\]
Integrate these inequalities and use (4.2e). They imply
\[
\begin{aligned}
\limsup_{v\to\infty}Q_f(v)&\le\frac{c_fkb}{1-e^{-kb}},\\
\liminf_{v\to\infty}Q_f(v)&\ge\frac{c_fkb}{e^{kb}-1}.
\end{aligned}
\tag{4.2f}
\]
First \(v\to\infty\) with \(b\) fixed, then \(b\downarrow0\), makes both bounds tend to \(c_f\). Thus \(Q_f(v)\to c_f\), or \(A_f(x)/x^k\to r_f/k\). The Gamma recurrence identifies this constant with the one in (4.2). This proves the mean-square asymptotic. ∎

For \(f=0\), the summatory function is zero instead of a positive asymptotic. Positivity supplied the monotone count used in this proof; arbitrary mixed coefficients are handled by polarization below. Also (4.2) remains an asymptotic without a quantitative remainder: the analytic theorem supplies convergence without a rate, and the fixed-interval argument does not supply one.

### 4.1. The function \(\Delta\)

The ring lesson gives \(\Delta=q\prod_{n\ge1}(1-q^n)^{24}\), the normalized basis of \(S_{12}\). Thus it is an eigenform, and
\[
 \tau(2)=-24,\quad
 \tau(4)=(-24)^2-2^{11}=-1472,\quad
 \tau(8)=(-24)(-1472)-2^{11}(-24)=84480.
\]
If \(A+B=-24\) and \(AB=2048\), its local coefficient-square series is
\[
 \sum_{r\ge0}\tau(2^r)^2X^r
 =\frac{1-2^{22}X^2}{(1-A^2X)(1-2048X)^2(1-B^2X)}.
\tag{4.3}
\]
Here \(A^2+B^2=576-4096=-3520\). Multiplying the factors therefore gives the entirely rational expression
\[
\begin{aligned}
 &\frac{1-4194304X^2}
 {1-576X-6029312X^2-2415919104X^3+17592186044416X^4}\\
 &=1+576X+2166784X^2+7136870400X^3+\cdots.
\end{aligned}
\tag{4.4}
\]
The first three nonconstant terms are exactly \((-24)^2,(-1472)^2,84480^2\).

Let \(P=\langle\Delta,\Delta\rangle\). All residue constants are now explicit:
\[
 \operatorname*{Res}_{u=12}D_{\Delta,\Delta}
      =\frac{3(4\pi)^{12}}{\pi\,11!}P,\qquad
 \operatorname*{Res}_{u=12}R_{\Delta,\Delta}
      =\frac{\pi(4\pi)^{12}}{2\,11!}P,\qquad
 \operatorname*{Res}_{u=12}\Lambda_{\Delta,\Delta}
      =\frac{P}{2\pi^{11}}.
\tag{4.5}
\]
To compute \(P\) directly, set \(Y(x)=\sqrt{1-x^2}\), \(\rho=\sqrt3/2\) and
\[
 J_a(Y)=\int_Y^\infty y^{10}e^{-ay}dy
       =\frac{10!e^{-aY}}{a^{11}}\sum_{j=0}^{10}\frac{(aY)^j}{j!}.
\tag{4.6}
\]
Expanding the absolutely convergent Fourier product and doing the \(y\)-integral gives the exact, rapidly convergent expression
\[
 P=\sum_{m,n\ge1}\tau(m)\tau(n)
       \int_{-1/2}^{1/2}\cos(2\pi(m-n)x)
                  J_{2\pi(m+n)}(Y(x))dx.
\tag{4.7}
\]
Imaginary terms cancel between \((m,n)\) and \((n,m)\). The convergence can be checked quantitatively using only the discriminant product and its weight. Write \(r=e^{-2\pi\rho}\). On the modular fundamental region, \(y\ge\rho\), and the product formula gives
\[
\begin{aligned}
|\Delta(x+iy)|
&\le e^{-2\pi y}\prod_{j\ge1}(1+e^{-2\pi jy})^{24}\\
&\le e^{-2\pi y}\exp\!\left(\frac{24r}{1-r}\right).
\end{aligned}
\]
The second inequality uses \(\log(1+t)\le t\), obtained by integrating \((1+t)^{-1}\le1\). The invariant quantity \(y^6|\Delta(z)|\) is therefore at most
\[
 M_\Delta=\exp\!\left(\frac{24r}{1-r}\right)
                 \left(\frac{3}{\pi e}\right)^6,
 \tag{4.7a}
\]
because the maximum of \(y^6e^{-2\pi y}\) occurs at \(y=3/\pi\). Reduction to the fundamental region extends this bound to the whole half-plane. Fourier orthogonality at height \(y=1/n\) now gives
\[
 |\tau(n)|\le e^{2\pi}M_\Delta n^6<2n^6.
 \tag{4.7b}
\]
Indeed \(\rho>0.86\) and \(\pi>3.14\) imply \(r<1/200\); \(3<\pi<22/7\) then gives
\(2\pi-6+24r/(1-r)<2/7+24/199<1/2\), while \((3/\pi)^6<1\) and \(e^{1/2}<2\). These elementary inequalities can also be checked from the exponential series. Thus (4.7b) has no purity or holomorphic Ramanujan–Petersson input. For \(y\ge\rho\),
\[
 |\Delta(x+iy)|,|\Delta_N(x+iy)|\le C_1e^{-2\pi y},\quad
 |\Delta-\Delta_N|\le C_Ne^{-2\pi(N+1)y},
\]
where
\[
 C_1=\frac2{1-64r},\qquad
 C_N=\frac{2(N+1)^6}{1-((N+2)/(N+1))^6r},\quad
 \Delta_N=\sum_{n=1}^N\tau(n)q^n.
\tag{4.8}
\]
Indeed the ratios of consecutive terms \(n^6e^{-2\pi ny}\) are at most \(64r\), and in the tail at most \(((N+2)/(N+1))^6r\), both less than one. Since
\(\bigl||\Delta|^2-|\Delta_N|^2\bigr|\le(|\Delta|+|\Delta_N|)|\Delta-\Delta_N|\), truncating both indices in (4.7) at \(N\) has error at most
\[
 2C_1C_N J_{2\pi(N+2)}(\rho).
\tag{4.9}
\]
The ten coefficients used are
\[
 (\tau(1),\ldots,\tau(10))=
 (1,-24,252,-1472,4830,-6048,-16744,84480,-113643,-115920).
\]
They follow by multiplying the discriminant product through \(q^{10}\); factors with index greater than nine cannot affect these coefficients. The coefficient product through \(N=10\), followed by quadrature of its finite sum in (4.7), gives
\[
\begin{aligned}
 P&\approx 1.03536206\times10^{-6},\\
 \operatorname*{Res}_{u=12}D_{\Delta,\Delta}&\approx0.38408405,\\
 c_\Delta&\approx0.03200700.
\end{aligned}
\tag{4.10}
\]
These are numerical evaluations of the exact formulas (4.5)–(4.7). The analytic truncation bound (4.9) is below \(3.21\times10^{-24}\). For reproducibility, the finite integral was evaluated by composite Simpson on 2048 equal subintervals and by independent adaptive quadrature. A fourth-derivative bound for its integrand gives Simpson error below \(2.02\times10^{-16}\); the displayed approximations are rounded more coarsely. The derivative bound follows by differentiating (4.6): on \([-1/2,1/2]\), \(|Y'|\le1\), \(|Y''|\le2\), \(|Y'''|\le4\), \(|Y''''|\le20\), and each derivative of \(J_a\) is an exponential times the indicated finite polynomial. Summing these elementary derivative bounds for the 100 terms gives \(\sup|F_{10}^{(4)}|<0.639\); hence the Simpson estimate is \(0.639/(180\cdot2048^4)\). Numerical arithmetic used 35 decimal digits; the analytic quadrature bounds refer to exact arithmetic. This supplies both an error estimate and a direct numerical computation of the norm, rather than treating \(P\) as an unspecified normalization.

The Simpson error bound used in this check also has an elementary proof. On \([-1,1]\), let \(L(F)=\int_{-1}^1F(x)dx-(F(-1)+4F(0)+F(1))/3\). Direct integration shows that \(L\) annihilates every cubic. Taylor's formula with integral remainder therefore gives
\[
\begin{gathered}
L(F)\\
=\int_{-1}^1 K F^{(4)}\,dt,\\
K(t)=-\frac{(1-|t|)^3}{72}\\
\cdot(1+3|t|).
\end{gathered}
\tag{4.10a}
\]
Here the integrand is the pointwise product of \(K(t)\) and \(F^{(4)}(t)\). Indeed apply \(L\) to \((x-t)_+^3/6\): for \(t\ge0\) its integral is \((1-t)^4/24\) and its Simpson value is \((1-t)^3/18\); reflection gives the other half. The kernel is nonpositive and \(\int_{-1}^1|K|dt=1/90\). Rescaling to a panel of length \(2h\) gives error at most \(h^5\sup|F^{(4)}|/90\). Adding the \(M/2\) panels with \(h=(b-a)/M\) proves exactly \((b-a)^5\sup|F^{(4)}|/(180M^4)\), for even \(M\).

### 4.2. Mixed averages and Petersson Gram matrices

**Corollary 4.1 (mixed coefficient averages).** For any \(f,g\in S_k(SL_2(\mathbb Z))\), put
\[
 C_k=\frac{3(4\pi)^k}{\pi\Gamma(k+1)}.
\tag{4.11}
\]
Then, with the original unnormalized coefficients,
\[
 \sum_{n\le x}a_n\overline{b_n}
 =C_k\langle f,g\rangle x^k+o(x^k).
\tag{4.12}
\]
In particular, distinct normalized eigenforms of the same weight have mixed sum \(o(x^k)\).

**Proof.** For a cusp form \(h\), let \(Q_x(h)=\sum_{n\le x}|a_n(h)|^2\). Equation (4.2) and the zero-form case together give \(x^{-k}Q_x(h)\to C_k\|h\|^2\) for every \(h\). Expanding each square gives the exact polarization identity
\[
\begin{aligned}
 4\sum_{n\le x}a_n\overline{b_n}
 &=Q_x(f+g)-Q_x(f-g)\\
 &\quad+iQ_x(f+ig)-iQ_x(f-ig).
\end{aligned}
\tag{4.13}
\]
For example the last difference before multiplication by \(i\) is four times the imaginary part of \(\sum a_n\overline{b_n}\); this checks the sign for a product linear in its first variable. Divide (4.13) by \(x^k\) and use the four diagonal limits. The same polarization identity for the Petersson product makes the limit \(4C_k\langle f,g\rangle\), proving (4.12). Orthogonality from Corollary 3.3 gives the eigenform assertion. When the inner product vanishes the conclusion is \(o(x^k)\), rather than an asymptotic equivalent to zero. The diagonal mean-square proof was used only for the nonnegative square coefficients of the four forms. ∎

For any fixed finite list \(f_1,\ldots,f_d\), this also identifies the Petersson Gram matrix as a coefficient limit:
\[
 x^{-k}\left(\sum_{n\le x}a_n(f_i)\overline{a_n(f_j)}\right)_{i,j=1}^d
 \longrightarrow C_k\bigl(\langle f_i,f_j\rangle\bigr)_{i,j=1}^d.
\tag{4.14}
\]
The convergence holds entrywise and in operator norm. Indeed (4.12) gives every entrywise limit. For an error matrix \(E\), if \(m=\max_{i,j}|E_{ij}|\), then \(|(Ev)_i|\le m\sum_j|v_j|\le m\sqrt d\|v\|_2\). Summing the \(d\) squared component bounds gives \(\|E\|_{\mathrm{op}}\le dm\), which tends to zero. This assertion supplies no quantitative rate.

## 5. Symmetric squares and the higher-rank outlook

At full level the normalized coefficients are real, by self-adjointness. For one eigenform with local roots \(\alpha,\beta\), define initially for \(\operatorname{Re}u>k\)
\[
 L(\operatorname{Sym}^2f,u)=\prod_p
 \bigl((1-\alpha^2p^{-u})(1-p^{k-1-u})(1-\beta^2p^{-u})\bigr)^{-1}.
\tag{5.1}
\]
There are two copies of \(\alpha\beta=p^{k-1}\) in (3.5), so
\[
 R_{f,f}(u)=\zeta(u-k+1)L(\operatorname{Sym}^2f,u).
\tag{5.2}
\]
This equality also follows by comparing each local factor. Near \(u=k\), divide the already continued \(R\) by \(\zeta(u-k+1)\). Their simple poles give a holomorphic continuation of the quotient there and the value
\[
 L(\operatorname{Sym}^2f,k)
 =\operatorname*{Res}_{u=k}R_{f,f}(u),\qquad
 \|f\|^2=\frac{2\Gamma(k)}{\pi(4\pi)^k}
                         L(\operatorname{Sym}^2f,k).
\tag{5.3}
\]
For \(\Delta\), this is \(P=2\cdot11!\,L(\operatorname{Sym}^2\Delta,12)/(\pi(4\pi)^{12})\). Equation (4.10) therefore also evaluates this special value via (4.5). The three normalized roots \(\alpha^2/p^{k-1},1,\beta^2/p^{k-1}\) describe the adjoint factor after the shift \(v=u-k+1\). This explains why an adjoint value at \(v=1\) governs the Petersson norm. A general symmetric-square lifting theorem is outside this calculation.

The tensor-factor algebra extends directly to arbitrary ranks. If \(A=\operatorname{diag}(\alpha_1,\ldots,\alpha_n)\) and \(B=\operatorname{diag}(\beta_1,\ldots,\beta_m)\), then \(e_i\otimes e_j\) is an eigenvector of \(A\otimes B\) with eigenvalue \(\alpha_i\beta_j\). These vectors form a basis, so
\[
\begin{gathered}
\det(1-XA\otimes B)^{-1}\\
=\prod_{i=1}^n\prod_{j=1}^m(1-\alpha_i\beta_jX)^{-1}.
\end{gathered}
\tag{5.4}
\]
This proves the formal \(nm\)-root identity, including repeated roots. In an unramified automorphic application the two root lists are called Satake roots. Identifying (5.4) with a local integral is a separate theorem, formulated in the free Getz–Hahn draft, Theorem 11.6.1. Its Sections 11.5 and 11.7 also formulate the global completed function, including archimedean factors, and its possible poles at 0 and 1 under the stated central-character normalization. Their analytic construction and general functional equation remain programme proof tasks; the elementary tensor identity does not prove them. The further development is [Rankin–Selberg for GLₙ](https://kokunoyumeto.github.io/open-math-courses-public/courses/LG-GLOB/index.html). Miller's free notes after Shahidi, arXiv:math/0204148v2, explain the corresponding Eisenstein-series construction as a further direction.

## 6. Exercises

1. **Easy.** Carry out the unfolding in (1.5), starting from the coset sum. Identify the absolute-convergence condition, the Fourier orthogonality step and the gamma factor.
2. **Medium.** Prove the local Euler identity (3.2) and apply it to the Hecke polynomials (3.1). Include the case of a repeated root, and explain the zeta factor in (3.5).
3. **Medium.** Assuming precisely the Tauberian theorem (4.1), prove (4.2) with its exact constant. Explain why knowing a real-axis residue alone would leave a hypothesis unverified. Then give the unconditional proof from the Petersson bound and Newman's analytic theorem, including the monotonicity argument that removes the average.
4. **Hard.** Prove the bound bearing Rankin's exponent
\[
 a_n=O_f\left(n^{(k-1)/2+3/10}\right)
 \qquad(f\in S_k(SL_2(\mathbb Z))).
\tag{6.1}
\]
Give a complete argument for arbitrary cusp forms and for the divisor estimate needed to remove the divisor factor. The modern route described in Solution 4 is conditional on the holomorphic Ramanujan–Petersson root theorem: its purity proof is still required in the programme and cannot be treated as established merely because the L-function lesson states it. A direct historical Rankin–Selberg route instead needs a quantitative mean-square remainder, which (4.1)–(4.2) do not supply. The bound (6.1) remains a required proof task until one of those dependencies is proved.

## 7. Full solutions

### Solution 1

For \(\sigma=\operatorname{Re}t>1\), boundedness of \(H\) gives integrability of \(|H|y^{\sigma-2}\) on the part of the strip with \(0<y<1\); cusp decay gives it on \(y\ge1\). The bottom-row estimate in Theorem 1.2 proves local uniform convergence of the positive coset sum. Apply the first lesson, Lemma 0.3, to pass this nonnegative series through the integral. Change variables \(w=\gamma z\) in each term; invariance of \(H\) and of \(d\mu\) makes its contribution the integral of \(|H(w)|\operatorname{Im}(w)^{\sigma-2}\) on \(\gamma\mathcal F\). The width-one projected tiling proved in the Petersson lesson, Lemma 4.0, sums these to the finite strip integral. The complex-series assertion of Lemma 0.3 is now applicable, and the same projected partition for \(H(w)\operatorname{Im}(w)^{t-2}\) gives (1.7).

Expand the two Fourier series uniformly on each compact positive-height rectangle, as justified by Theorem 2.1 of the Petersson lesson. The elementary integral
\(\int_0^1e^{2\pi i(n-m)x}dx\) is one for \(n=m\) and zero otherwise, so only \(a_n\overline{b_n}e^{-4\pi ny}\) remains. The diagonal-square computation (1.4), using the nonnegative continuous-series assertion of Lemma 0.3, and Cauchy–Schwarz show that the sum of its absolute Mellin integrals is finite for \(\operatorname{Re}(t+k-1)>k\). The diagonal series is locally uniformly convergent for \(y>0\), so the complex-series assertion of that lemma permits integration of each term. With \(v=4\pi ny\),
\[
 \int_0^\infty y^{t+k-2}e^{-4\pi ny}dy
  =(4\pi n)^{-t-k+1}\int_0^\infty v^{t+k-2}e^{-v}dv.
\]
The remaining integral is \(\Gamma(t+k-1)\), yielding (1.5). The simultaneous sign in \(\Gamma_\infty\) and \(\Gamma\) was already quotiented; inserting another factor \(1/2\) would give the wrong residue.

### Solution 2

For distinct roots, write \(h_r(A,B)=(A^{r+1}-B^{r+1})/(A-B)\). Multiplying the corresponding formula for \(C,D\), and summing each of its four terms in \(r\), gives (3.3). Clearing its denominators produces a polynomial of degree at most three. Its constant coefficient is \((A-B)(C-D)\), its coefficient of \(X\) vanishes, its coefficient of \(X^2\) is \(-ABCD(A-B)(C-D)\), and its coefficient of \(X^3\) vanishes. This proves (3.2). Since the cleared coefficients are polynomial identities in the roots, the formula extends to repeated roots. In particular, if \(A=B\), then \(h_r(A,A)=(r+1)A^r\); this is already included, without division by zero.

For the Hecke polynomials, the recurrence identifies \(a_{p^r}=h_r(\alpha_1,\alpha_2)\) and \(\overline{b_{p^r}}=h_r(\overline{\beta_1},\overline{\beta_2})\). The product of all four roots is \(p^{2k-2}\), giving the numerator \(1-p^{2k-2}X^2\). Set \(X=p^{-u}\); multiplicativity and absolute convergence as in Theorem 3.2 produce (3.4). Its numerator product is \(\zeta(2u-2k+2)^{-1}\), so multiplying by that zeta function gives precisely the four reciprocal local factors. This also shows why multiplying the two separate degree-two Euler products would be incorrect: it would form a convolution of coefficients rather than their pointwise products.

### Solution 3

Assume \(f\ne0\). The coefficients \(c_n=|a_n|^2\) are nonnegative. Lemma 1.1 proves convergence for \(\operatorname{Re}u>k\). Equation (2.6) gives the positive residue
\(r_f=3(4\pi)^k\|f\|^2/(\pi\Gamma(k))\). Theorem 2.2 proves that subtracting \(r_f/(u-k)\) leaves a holomorphic function throughout \(\operatorname{Re}u>k-1/2\), including every point of the boundary line \(\operatorname{Re}u=k\). It therefore has the continuous closed-half-plane extension required by (4.1). Apply that theorem with \(a=k\):
\[
 \sum_{n\le x}|a_n|^2\sim\frac{r_f}{k}x^k
       =\frac{3(4\pi)^k}{\pi\Gamma(k+1)}\|f\|^2x^k,
\]
where \(\Gamma(k+1)=k\Gamma(k)\). A real-axis limit \((u-k)D(u)\to r_f\) supplies no continuity along the rest of the vertical boundary. It does not replace that hypothesis. The zero form has all coefficients zero and is treated separately.


For the unconditional proof, use the invariant Petersson bound and Fourier orthogonality at height \(1/x\) to obtain
\(A_f(x)\le e^{4\pi}M_f^2x^k\). Thus
\(h_f(v)=e^{-kv}A_f(e^v)-r_f/k\) is bounded and locally integrable. Its Laplace transform, initially for \(\operatorname{Re}z>0\), is
\[
\begin{aligned}
G_f(z)&=\frac{D_{f,f}(k+z)}{k+z}-\frac{r_f}{kz}\\
&=\frac{D_{f,f}(k+z)-r_f/z-r_f/k}{k+z}.
\end{aligned}
\]
Theorem 2.2 makes the numerator holomorphic on \(\operatorname{Re}z>-1/2\); the denominator is nonzero there. Apply the bounded-function analytic theorem from *The prime number theorem*, Theorem 5.1. It gives convergence of \(\int_0^T h_f(v)\,dv\), so the integrals of \(Q_f(v)=e^{-kv}A_f(e^v)\) over both \([v,v+b]\) and \([v-b,v]\) tend to \(r_fb/k\), for each fixed \(b>0\).

Monotonicity of \(A_f\) gives \(Q_f(v+t)\ge e^{-kt}Q_f(v)\) and \(Q_f(v-t)\le e^{kt}Q_f(v)\) for \(0\le t\le b\), \(v\ge b\). Integrating yields
\[
\begin{aligned}
\limsup_{v\to\infty}Q_f(v)&\le\frac{r_fb}{1-e^{-kb}},\\
\liminf_{v\to\infty}Q_f(v)&\ge\frac{r_fb}{e^{kb}-1}.
\end{aligned}
\]
Let \(b\downarrow0\). Both bounds tend to \(r_f/k\), so \(A_f(x)/x^k\to r_f/k\), exactly (4.2). The fixed-interval limit followed by this monotonicity step is essential: convergence of the integrals alone does not give pointwise convergence for arbitrary bounded functions.

### Solution 4

This is a conditional derivation: assume the holomorphic Ramanujan–Petersson root theorem, whose programme proof remains required. The normalized full-level eigenbasis from the Hecke lesson, Theorem 4.2, writes any \(f\) as a finite sum \(\sum_j c_j f_j\). Every \(f_j\) is primitive at level one, so the assumed theorem applies at every prime: both roots of \(X^2-a_p(f_j)X+p^{k-1}\) have modulus \(p^{(k-1)/2}\). The prime-power generating function consequently gives
\[
 |a_{p^r}(f_j)|
 =\left|\sum_{h=0}^r\alpha_1^{r-h}\alpha_2^h\right|
 \le(r+1)p^{r(k-1)/2}.
\]
This also handles a repeated root. Multiplicativity yields
\[
 |a_n(f_j)|\le\prod_{p^r\parallel n}(r+1)n^{(k-1)/2}
          =d(n)n^{(k-1)/2}.
\tag{7.1}
\]

Here is the needed divisor bound, including a uniform constant. Fix \(\epsilon>0\). For every prime \(p\ge2^{1/\epsilon}\) and every integer \(r\ge1\), induction gives \(r+1\le2^r\le p^{\epsilon r}\). For one of the finitely many smaller primes define
\[
 C_p=\sup_{r\ge0}(r+1)p^{-\epsilon r}<\infty.
\]
Finiteness follows because this sequence tends to zero; more explicitly it is bounded by the convergent sum \(\sum_{r\ge0}(r+1)p^{-\epsilon r}=(1-p^{-\epsilon})^{-2}\). Thus
\[
 d(n)=\prod_{p^r\parallel n}(r+1)
       \le \left(\prod_{p<2^{1/\epsilon}}C_p\right)n^\epsilon
       =C_\epsilon n^\epsilon
\tag{7.2}
\]
for every \(n\). Combining (7.1)–(7.2) and the finite basis expansion gives
\[
 |a_n(f)|\le\left(\sum_j|c_j|\right)C_\epsilon
                 n^{(k-1)/2+\epsilon}.
\]
Choosing \(\epsilon=3/10\) proves (6.1), with a constant depending on \(f\), conditional on the deep root theorem used at the start of this solution. That theorem's proof remains unresolved. This is not a derivation of the historical mean-square remainder from (4.2); an asymptotic without a rate cannot supply that remainder. Consequently (6.1) is preserved as a required result, with a conditional derivation and an explicit outstanding proof dependency. ∎

## What this lesson does not prove

The general continuous-boundary Wiener–Ikehara theorem is stated before (4.1), with the exact free reference Gillet–Grayson, Appendix A, Theorem A.4, pp. 443–444. Its assumed implication is checked in Solution 3; the general theorem's proof is still required if that route is used. Section 4 independently gives the complete mean-square argument from the elementary Petersson bound and The prime number theorem, Theorem 5.1. That earlier programme theorem has the full contour identity, both arc bounds and the narrow-path estimate in its equations (5.2)–(5.4); these are the exact analytic proof input, with no prime-counting conclusion or large-height growth estimate needed. The numerical norm estimate now uses only the locally proved discriminant bound (4.7a)–(4.7b). Solution 4 remains conditional on the holomorphic Ramanujan–Petersson root theorem stated in The L-function of a cusp form, Section 5: Deligne's freely accessible original paper, Theorem (8.2), p. 302. Its purity proof is not supplied here, so the required coefficient bound (6.1) is not counted as closed.

The inherited results are precisely: the Petersson lesson, Theorems 1.1 and 2.1, for integrability, positivity and the invariant bound; the level-one Hecke lesson, Theorems 4.2–4.3, for the normalized orthogonal eigenbasis, multiplicity one and coefficient recurrences; the ring lesson, Theorem 2.2 and Theorem 4.1, for the discriminant product and \(S_{12}=\mathbb C\Delta\); and the preceding Eisenstein lesson, Theorem 2.2, Theorem 3.2 and Corollary 3.3, for the Fourier expansion, completed continuation, reflection and residue. Its Section 3 and Solution 3 supply the zeta continuation and \(\zeta(2)=\pi^2/6\). No Maass spectral existence theorem is needed for the integral proof.

The Gamma integral, recurrence, meromorphic continuation and entire reciprocal have programme proofs in The Gamma function and Stirling's formula, Theorems 1.1–1.2. The nonnegative and absolutely integrable continuous-series interchanges, the rectangular integral exchange, and the holomorphic-parameter integration used here are proved in The upper half-plane and the modular group, Lemma 0.3. The coset unfolding uses The Petersson inner product and Poincaré series, Lemma 4.0, whose locally finite projected tiles have zero-area boundaries on compact truncations. Fourier orthogonality is obtained from finite Fourier polynomials and their uniform limits in Lemma 1.1 and Theorem 1.2; the Cauchy–Schwarz estimate is the finite-sum inequality followed by increasing limits. The holomorphic-parameter step in Lemma 2.1 checks the explicit Gaussian majorant against the same continuous integration lemma. Real completeness, elementary continuous integration and compactness remain foundational prerequisites. The real plane change-of-variables theorem for the Möbius substitutions has not been proved here, and general measurable-domain integration retains its separate prerequisite status in the Petersson lesson, Theorem 1.1. These continuous arguments make no assertion of general measurable Tonelli, Fubini or dominated convergence. The polynomial root argument in Lemma 3.1 is proved there. The composite-Simpson error estimate is proved from its explicit remainder kernel in (4.10a); it affects the numerical approximation, while (4.5)–(4.7) are exact identities.

The higher-rank tensor-factor algebra is proved in (5.4). Its identification with local integrals and the general completed continuation, Getz–Hahn, Theorems 11.6.1 and 11.7.1, remain required proofs for the higher-rank extension. A general symmetric-square lifting theorem, the Langlands–Shahidi method, and the historical quantitative Rankin–Selberg mean-square remainder are likewise not proved here. The full-level unfolding, continuation, residues, functional equation and local algebra above are independently derived from the explicit Eisenstein formulas and proved earlier analytic inputs.

## References

- **Zagier 1981.** D. Zagier, *The Rankin–Selberg method for automorphic functions which are not of rapid decay*, original research article, pp. 415–437. [Author's freely accessible article](https://people.mpim-bonn.mpg.de/zagier/files/rankin-selberg/fulltext.pdf). Our rapid-decay unfolding and its normalization are independently derived in Sections 1–2.
- **Getz–Hahn 2022.** J. R. Getz and H. Hahn, *An Introduction to Automorphic Representations: With a View toward Trace Formulae*, author's freely distributed draft dated April 22, 2022, Sections 11.5–11.7, pp. 265–272. [Exact free draft](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf).
- **Miller after Shahidi 2002.** S. D. Miller, *A Summary of the Langlands–Shahidi Method of Constructing L-functions*, notes after discussions with F. Shahidi, arXiv:math/0204148v2. [Free original notes](https://arxiv.org/abs/math/0204148v2).
- **Zagier 1997.** D. Zagier, “Newman's Short Proof of the Prime Number Theorem,” *American Mathematical Monthly* 104, 705–708, analytic theorem and proof, pp. 707–708. The bounded-function theorem used in Section 4 has a complete programme proof in *The prime number theorem*, Theorem 5.1. [Author's article](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.2307/2975232/fulltext.pdf).
- **Gillet–Grayson 2006.** H. Gillet and D. R. Grayson, “Volumes of Symmetric Spaces via Lattice Points,” *Documenta Mathematica* 11, 425–447, Appendix A, Theorem A.4, pp. 443–444. [Publisher's open article](https://ems.press/content/serial-article-files/25997).
- **Deligne 1974.** P. Deligne, “La conjecture de Weil I,” *Publications Mathématiques de l'IHÉS* 43, 273–307, Theorem (8.2), p. 302. The exact good-prime root theorem is stated in the L-function lesson, Section 5. [Original article](https://numdam.org/articles/10.1007/BF02684373/).
