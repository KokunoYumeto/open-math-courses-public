# From partial regularity to smooth solutions

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

An equation can convert arbitrarily high regularity in selected variables into full smoothness. The mechanism is a weighted interior estimate: regularity in the prime variables pays for the prime-frequency factor in the partial-hypoellipticity bound. This also characterizes when partial convolution smooths every homogeneous solution.

Read [Partial smoothing and polynomial coefficients](partial-smoothing-and-polynomial-coefficients.md) and [Weighted interior estimates and operator strength](weighted-interior-estimates-and-strength.md). We use the local spaces, smooth embeddings, and Fréchet topologies from [Local regularity, sharp embeddings, and compactness](local-regularity-and-compactness.md). Grubb [Grubb] gives further Fourier and distribution background. For one remaining variable we reuse the ordinary-differential-equation regularity result from *Weak equations and classical functions* [ODE], with its precise contract stated below.

Keep \(D=-i\partial\), \(x=(x',x'')\), and \(0\leq j<n\), where \(x'\in\mathbb R^j\). All polynomials may have complex coefficients. All weights are positive and moderate, and \(1\leq p\leq\infty\). A nonzero constant operator is handled directly whenever a positive-order derivative norm occurs.

## Spending regularity in the prime variables

For a polynomial \(P\) of positive degree use
\[
\begin{gathered}
S_P^2=\sum_\alpha|\partial^\alpha P|^2,\\
J_P^2=\sum_{|\alpha|\geq1}|\partial^\alpha P|^2,\\
r_P=S_P/J_P\geq1.
\end{gathered}
\tag{1}
\]
The sums are finite. These are moderate weights. Partial hypoellipticity gives constants \(a,C>0\) such that
\[
\begin{gathered}
\frac{J_P(\xi)}{S_P(\xi)}
\leq C\langle\xi'\rangle\langle\xi\rangle^{-a},\\
r_P(\xi)\geq C^{-1}
\frac{\langle\xi\rangle^a}{\langle\xi'\rangle}.
\end{gathered}
\tag{2}
\]

**Theorem 1.1.** Suppose \(P\) is partially hypoelliptic in the double-prime frequencies, \(X\) is open, and \(P(D)u\in C^\infty(X)\). If one moderate weight \(k_0\) satisfies
\[
u\in\bigcap_{v=0}^{\infty}
B_{p,k_0\langle\xi'\rangle^v}^{\mathrm{loc}}(X),
\tag{3}
\]
then \(u\in C^\infty(X)\).

**Proof.** Take any moderate target weight \(k\). Moderateness of \(k\) and \(k_0^{-1}\) gives a finite \(L\geq0\) with
\[
k(\xi)/k_0(\xi)\leq C\langle\xi\rangle^L.
\tag{4}
\]
Choose an integer \(N\geq0\) with \(aN\geq L\), and set \(k_1=k_0\langle\xi'\rangle^N\). Equation (2) yields
\[
k\leq C k_1r_P^N.
\tag{5}
\]
The data are locally in every moderate weighted space because they are smooth. In particular use \(k_2=k/S_P\); this is moderate, and
\[
k\leq k_1+S_Pk_2.
\tag{6}
\]
Theorem 1.1 of the weighted-interior lesson now gives \(u\in B_{p,k}^{\mathrm{loc}}(X)\). We may take \(k=\langle\xi\rangle^s\) with arbitrarily large \(s\). The sharp embedding into \(C^l\) holds when \(s>l+n/p'\), so every finite derivative order is continuous. Hence \(u\) is smooth. A nonzero constant \(P\) gives \(u=P^{-1}P(D)u\) immediately. \(\square\)

The initial weight may allow roughness of any fixed local order. The assumption supplies all prime-frequency gains from that one initial weight; it does not require smoothness at the outset.

## Smoothing a distributional solution

For \(\psi\in C_c^\infty(\mathbb R^j)\), retain the domain and convolution
\[
\begin{gathered}
X_\psi=\{x:x-(\operatorname{supp}\psi\times\{0\})\subset X\},\\
u*'\psi=u*(\psi\otimes\delta_0).
\end{gathered}
\tag{7}
\]

**Theorem 2.1.** If \(P\) is partially hypoelliptic and \(u\in\mathcal D'(X)\) satisfies \(P(D)u=f\in C^\infty(X)\), then
\[
u*'\psi\in C^\infty(X_\psi)
\tag{8}
\]
for every compact smooth \(\psi\).

**Proof.** Let \(K\) be a compact subset of \(X_\psi\). The compact source set \(K-(\operatorname{supp}\psi\times\{0\})\) lies in \(X\). Choose a source cutoff \(\chi\) equal to one on a neighborhood of this set. Near \(K\) the output is the global partial convolution of \(\chi u\).

The compact distribution \(\chi u\) has finite order, so its Fourier transform has a polynomial upper bound. Choose \(M\) large enough that
\[
\chi u\in B_{p,\langle\xi\rangle^{-M}}.
\tag{9}
\]
For finite \(p\), increase \(M\) enough to make the resulting power integrable; for \(p=\infty\) a bounded power suffices. Multiplication by \(\widehat\psi(\xi')\) then gives, for every integer \(v\geq0\), membership of the convolution in
\[
B_{p,\langle\xi\rangle^{-M}\langle\xi'\rangle^v}.
\tag{10}
\]
Indeed \(\langle\xi'\rangle^v\widehat\psi(\xi')\) is bounded. Output cutoffs preserve these memberships. Thus (3) holds on a neighborhood of \(K\), with the same \(M\) for all \(v\).

Constant-coefficient differentiation commutes with the partial convolution on \(X_\psi\), so \(P(D)(u*'\psi)=f*'\psi\). The latter is smooth: on every compact output neighborhood its derivatives are integrals of smooth derivatives of \(f\) over a fixed compact set of prime translations. Theorem 1.1 gives smoothness near \(K\). These neighborhoods cover \(X_\psi\), proving (8). No uniform order for \(u\) on the whole of \(X\) was required. The zero kernel gives the zero smooth function on all of \(\mathbb R^n\). \(\square\)

Define the homogeneous solution space
\[
\begin{aligned}
&\mathcal N_{p,k}(X)\\
&\quad=\{u\in B_{p,k}^{\mathrm{loc}}(X):P(D)u=0\},
\end{aligned}
\tag{11}
\]
with the induced local weighted topology. It is a closed Fréchet subspace: the inclusion into distributions is continuous and the equation is closed there.

**Theorem 2.2.** For a partially hypoelliptic \(P\), partial convolution is a continuous linear map
\[
\mathcal N_{p,k}(X)\longrightarrow C^\infty(X_\psi).
\tag{12}
\]
It maps bounded sets to relatively compact sets in every \(B_{q,h}^{\mathrm{loc}}(X_\psi)\), where \(1\leq q\leq\infty\) and \(h\) is any moderate weight.

**Proof.** Theorem 2.1 gives the range. If \(u_l\to u\) in the solution space and \(u_l*'\psi\to v\) smoothly, distributional continuity of partial convolution gives \(v=u*'\psi\). Thus the graph of (12) is closed. The Fréchet closed graph theorem proves continuity.

A bounded input set therefore has bounded image in \(C^\infty(X_\psi)\). On a countable compact exhaustion, all derivative bounds give subsequences convergent in each derivative order by Ascoli; diagonal selection gives convergence in \(C^\infty(X_\psi)\). Thus the image is relatively compact there. The inclusion \(C^\infty\to B_{q,h}^{\mathrm{loc}}\) is continuous, including \(q=\infty\), by the local weighted-space estimates. Its image is relatively compact in each stated output space. \(\square\)

In particular the conclusion holds with \(q=p,h=k\). We use **compactness on bounded sets** to mean this property. It does not assert that one neighborhood of zero has relatively compact image.

## Two tests in one solution space

**Theorem 3.1.** For a nonzero \(P\), the following are equivalent.

1. \(P\) is partially hypoelliptic in the double-prime frequencies.
2. For some nonempty open \(X\), some \(p,k\), and every compact smooth \(\psi\), all \(u\in\mathcal N_{p,k}(X)\) have \(u*'\psi\in C^\infty(X_\psi)\).
3. For some nonempty open \(X\) and some \(p,k\), every such partial convolution maps bounded subsets of \(\mathcal N_{p,k}(X)\) to relatively compact subsets of \(B_{p,k}^{\mathrm{loc}}(X_\psi)\).

If either test holds once, both conclusions hold for every nonempty open set and every \(p,k\).

**Proof: a kernel that detects bounded prime frequencies.** Theorems 2.1 and 2.2 show that condition 1 implies both tests for every \(X,p,k\). To prove the converses, suppose the complex-zero escape condition fails. There are zeros
\[
\begin{gathered}
\zeta_l=\xi_l+i\eta_l,\qquad |\xi_l|\to\infty,\\
|\eta_l|+|\xi_l'|\leq A.
\end{gathered}
\tag{13}
\]
The entire prime components \(\zeta_l'\) stay in a fixed bounded complex set.

For \(j>0\), choose a nonnegative \(\psi_0\in C_c^\infty(\mathbb R^j)\) with integral one, and put \(\psi_\varepsilon(y)=\varepsilon^{-j}\psi_0(y/\varepsilon)\). Its entire Fourier transform satisfies
\[
\begin{aligned}
&\widehat\psi_\varepsilon(z)-1\\
&\quad=\int\psi_0(y)(e^{-i\varepsilon y\cdot z}-1)\,dy.
\end{aligned}
\tag{14}
\]
On a bounded complex set the absolute value tends uniformly to zero, since
\[
|e^{-i\varepsilon y\cdot z}-1|
\leq\varepsilon|y||z|e^{\varepsilon|y||z|}.
\tag{15}
\]
Choose \(\varepsilon\) so small that \(X_{\psi_\varepsilon}\) is nonempty and
\[
c_l=\widehat\psi_\varepsilon(\zeta_l'),
\qquad 1/2\leq|c_l|\leq3/2.
\tag{16}
\]
Nonemptiness follows by taking a ball inside \(X\) and making the prime support smaller than its radius. For \(j=0\), take the scalar kernel one, with \(c_l=1\) and \(X_\psi=X\).

The normalized solutions
\[
u_l(x)=\frac{e^{ix\cdot\zeta_l}}{k(\xi_l)}
\tag{17}
\]
are bounded in \(\mathcal N_{p,k}(X)\). This is exactly the modulation estimate (18) of [Hypoellipticity and complex zeros](hypoellipticity-and-complex-zeros.md): for a compact cutoff their Fourier transforms are translates of \(\widehat{\phi e^{-x\cdot\eta_l}}/k(\xi_l)\), and moderate weight shifts give a uniform bound at every \(p\). They also tend to zero strongly in distributions. Fourier decay of compact tests is uniform for bounded imaginary parts and bounded test sets, while \(k(\xi_l)^{-1}\) has at most polynomial growth. Direct compact convolution gives
\[
u_l*'\psi_\varepsilon=c_lu_l.
\tag{18}
\]

**Proof: the smoothness test.** Under condition 2 the map from the solution space to \(C^\infty(X_{\psi_\varepsilon})\) has a closed graph, by the distributional continuity used in Theorem 2.2. It is therefore continuous. The sequence \(c_lu_l\) is bounded in every smooth seminorm.

Fix \(x_0\in X_{\psi_\varepsilon}\). For each integer \(r\), bound all \(D_\nu^r(c_lu_l)(x_0)\). Some coordinate of \(\zeta_l\) has modulus at least \(|\zeta_l|/\sqrt n\), while (13) bounds \(e^{-x_0\cdot\eta_l}\) below by a positive constant. Equations (16) and (17) imply
\[
|\xi_l|^r\leq C_r k(\xi_l).
\tag{19}
\]
The weight has a polynomial upper bound \(k(\xi)\leq C\langle\xi\rangle^L\). An integer \(r>L\) contradicts (19).

**Proof: the compactness test.** Under condition 3 the sequence \(c_lu_l\) is relatively compact in the output local weighted space. Its distributional limit is zero, since the \(c_l\) are bounded. Every convergent subsequence must therefore converge to zero. If the full sequence failed to tend to zero in some seminorm, the offending subsequence would have a further convergent subsequence by relative compactness, a contradiction. Thus compactness would force convergence to zero in every weighted seminorm.

Take a nonzero \(\phi\in C_c^\infty(X_{\psi_\varepsilon})\). For the polynomial moderate shift bound \(M_k\), the reverse shift inequality yields
\[
\begin{aligned}
\|\phi(c_lu_l)\|_{p,k}
&\geq |c_l|(2\pi)^{-n/p}\\
&\quad{}\cdot
\left\|\frac{\widehat{\phi e^{-x\cdot\eta_l}}}
{M_k(-\cdot)}\right\|_p.
\end{aligned}
\tag{20}
\]
This is the lower bound (20) of the complex-zeros lesson, multiplied by \(|c_l|\). Pass to a subsequence with \(\eta_l\to\eta\). The transforms converge in the Schwartz topology, and their quotients by \(M_k(-\cdot)\) converge in the displayed norm, also when \(p=\infty\). The limiting norm is positive, because \(\phi e^{-x\cdot\eta}\ne0\) and the Fourier transform is injective. In conjunction with \(|c_l|\geq1/2\), this contradicts convergence to zero.

Either test rules out (13). The zero-escape criterion of the preceding lesson gives condition 1, finishing all implications. A nonzero constant already satisfies condition 1 and has only the zero homogeneous solution. \(\square\)

The small kernel was needed because a general compact smooth function can have zeros in its entire Fourier transform. Its multiplier must stay away from zero on the bounded complex prime frequencies used in the test.

## One remaining variable

Now let \(x''\) have dimension one, with frequency \(t\). We use the following precise ordinary-differential-equation input [ODE]: on an open subset of \(\mathbb R\), a distribution satisfying an order-\(m\) scalar equation with smooth coefficients, nonvanishing leading coefficient, and continuous right-hand side belongs to \(C^m\). Corollary 3.2 of *Weak equations and classical functions* proves it by reduction to a first-order system.

Consequently every nonzero constant-coefficient one-variable operator \(R(D)\) is hypoelliptic. For positive degree \(m\), if \(R(D)u=f\) is smooth, apply that input also to each distributional derivative \(u^{(r)}\):
\[
R(D)u^{(r)}=f^{(r)}.
\tag{21}
\]
Every \(u^{(r)}\) belongs to \(C^m\), so \(u\) is smooth. Degree zero is direct multiplication. This reuses the one-variable result for one-variable distributions.

**Theorem 4.1.** Write a nonzero polynomial as
\[
P(\xi',t)=\sum_{l=0}^m a_l(\xi')t^l,
\qquad a_m\not\equiv0.
\tag{22}
\]
It is partially hypoelliptic in \(t\) if and only if \(a_m\) is a nonzero constant, independent of \(\xi'\).

**Proof.** Expand also as \(P=\sum_\gamma P_\gamma(t)(\xi')^\gamma\). The coefficient criterion in the preceding lesson requires a nonzero hypoelliptic \(P_0\) and \(P_\gamma/P_0\to0\) on the real line for every \(\gamma\ne0\). A nonzero one-variable \(P_0\) is hypoelliptic by the input just explained, or by its finite complex zero set. Quotient decay between one-variable polynomials is exactly
\[
\deg P_\gamma<\deg P_0\qquad(\gamma\ne0),
\tag{23}
\]
with zero coefficients omitted. This follows by comparing their leading powers as \(|t|\to\infty\).

If \(a_m\) is a nonzero constant, \(P_0\) has degree \(m\) and each other \(P_\gamma\) has smaller degree. Conversely, (23) makes \(P_0\) carry the highest power of \(t\); every other prime coefficient has smaller \(t\)-degree, so that highest coefficient is a nonzero constant. If \(m=0\), the criterion forces every other \(P_\gamma\) to vanish, hence forces \(P\) itself to be constant. \(\square\)

For example \(t^3+(1+i\xi_1')t^2+(\xi_1')^4\) qualifies, although its lower normal-order coefficients depend on prime frequencies. The conclusion permits arbitrary complex lower-order coefficients.

## Rapid decay in a curved frequency region

There is a useful Fourier conclusion even before choosing a partial split.

**Proposition 5.1.** Let \(P\) have positive degree, \(u\in\mathcal D'(X)\), and \(P(D)u\in C^\infty(X)\). Suppose a subset \(A\) of real frequency space satisfies
\[
J_P(\xi)/S_P(\xi)\leq C\langle\xi\rangle^{-c},
\qquad \xi\in A,
\tag{24}
\]
for some \(c>0\). For every \(\phi\in C_c^\infty(X)\) and every \(b\geq0\),
\[
\sup_{\xi\in A}
\langle\xi\rangle^b|\widehat{\phi u}(\xi)|<\infty.
\tag{25}
\]

**Proof.** On a relatively compact neighborhood of \(\operatorname{supp}\phi\), finite local order gives \(u\in B_{\infty,k_0}^{\mathrm{loc}}\) for a weight \(k_0=\langle\xi\rangle^{-M}\). For any integer \(N\geq0\) use the moderate target \(k_N=k_0r_P^N\) and data weight \(k_N/S_P\). The two inequalities in the weighted interior theorem hold, with the first an equality and the second immediate from the data term. Smooth data belong to the required space, so
\[
u\in B_{\infty,k_N}^{\mathrm{loc}}.
\tag{26}
\]
On \(A\), (24) makes \(r_P\geq C^{-1}\langle\xi\rangle^c\). Thus
\[
|\widehat{\phi u}(\xi)|
\leq C_{\phi,N}\langle\xi\rangle^{M-cN},
\qquad \xi\in A.
\tag{27}
\]
The weighted supremum bound is pointwise here: the compact distribution has a continuous Fourier transform, and \(k_N\) is continuous. Choose \(N\) so that \(cN\geq M+b\). This proves (25). The argument uses moderate weights \(k_N\) on the full frequency space and makes no regularity assumption on the boundary of \(A\). \(\square\)

For a partially hypoelliptic polynomial, (2) applies on the curved region
\[
\begin{gathered}
A_{\varepsilon,A_0}
=\{\xi:|\xi'|\leq A_0|\xi''|^\varepsilon\},\\
0<\varepsilon<\min(a,1).
\end{gathered}
\tag{28}
\]
On this region \(\langle\xi\rangle\) and \(\langle\xi''\rangle\) are comparable, and
\[
J_P/S_P\leq C\langle\xi\rangle^{-(a-\varepsilon)}.
\tag{29}
\]
Proposition 5.1 proves rapid decrease there for every compact localization of a solution with smooth data. This region narrows towards the double-prime directions as the frequency grows. It is not a fixed angular cone; an ordinary wavefront exclusion requires uniform decay on an open cone.

## Exercises with complete solutions

**Exercise 1. Smoothing the wrong transport variable.** In coordinates \((y,z)\in\mathbb R^2\), smooth in \(y\). For \(P(s,t)=s\), exhibit a homogeneous distribution whose partial convolution is not smooth.

**Solution.** Take \(u=1_y\otimes\delta_0(z)\). It is independent of \(y\), so \(D_yu=0\). For any compact \(\psi\) with integral one, \(u*'\psi=1_y\otimes\delta_0(z)\), still singular. The complex zeros \((0,t)\) with real \(t\to\infty\) have bounded prime component and zero imaginary part. The geometric criterion fails at exactly the frequencies left untouched by smoothing.

**Exercise 2. Transport in the remaining variable.** On \(Y\times I\), where \(I\) is an open interval, let \(D_tu=0\) and let \(y\in Y\) be the prime variables. Explain explicitly why partial convolution is smooth.

**Solution.** Theorem 2.1 of *Weak equations and classical functions* [ODE] states and proves that \(\partial_tu=0\) implies \(u=w\otimes1_I\) for one \(w\in\mathcal D'(Y)\); it constructs \(w\) by pairing against a unit-integral test in \(I\) and uses a test primitive for the remainder. Since \(D_t=-i\partial_t\), that result applies here. On its translated source domain,
\[
u*'\psi=(w*\psi)\otimes1_I.
\]
The distribution convolved with a compact smooth kernel is smooth in \(y\), and the second factor is constant. Hence the result is smooth in all variables. When the prime block is nonempty, the original solution can be singular, for example with \(w=\delta_0\); this operator is partially hypoelliptic but not fully hypoelliptic.

**Exercise 3. Paying for a prescribed isotropic power.** Suppose \(J_P/S_P\leq C\langle\xi'\rangle\langle\xi\rangle^{-1/3}\), \(k_0=\langle\xi\rangle^{-5}\), and the data are smooth. To obtain \(u\in B_{p,\langle\xi\rangle^s}^{\mathrm{loc}}\), \(s\geq0\), which prime gain in (3) suffices?

**Solution.** Choose an integer \(N\geq3(s+5)\). Then
\[
k_0\langle\xi'\rangle^N r_P^N
\geq C_N\langle\xi\rangle^{-5+N/3}
\geq C_N\langle\xi\rangle^s.
\]
Thus the single membership with prime gain \(v=N\) pays for the first inequality of the weighted theorem. Use the smooth-data weight \(\langle\xi\rangle^s/S_P\) for its second inequality. The argument works for every \(p\), including infinity. Taking all prime gains gives every \(s\), and therefore full smoothness.

**Exercise 4. Compactness on bounded sets.** For a nonempty open \(X\subset\mathbb R^n\), \(n\geq1\), the identity on \(C^\infty(X)\) maps bounded sets to relatively compact sets. Show why it need not map any neighborhood of zero to a relatively compact set.

**Solution.** Relative compactness of bounded sets follows from Ascoli for each derivative order and diagonal selection on a compact exhaustion. A neighborhood of zero, however, restricts only finitely many seminorms up to some order \(r\). Take a compact smooth cutoff \(\chi\) supported in a ball inside \(X\), with \(\chi=1\) on a smaller ball, and consider
\[
f_\lambda(x)=c\lambda^{-r}\chi(x)e^{i\lambda x_1},
\qquad \lambda\geq1.
\]
Every derivative up to order \(r\) is uniformly bounded by a constant times \(c\); choose \(c>0\) small enough to place all these functions in a basic neighborhood contained in the given neighborhood. On the smaller ball the derivative of order \(r+1\) in \(x_1\) has modulus \(c\lambda\), which is unbounded. A relatively compact set is bounded in every continuous seminorm, so this neighborhood cannot have relatively compact image. This explains the bounded-set meaning used in Theorems 2.2 and 3.1.

**Exercise 5. The strict exponent margin.** In (28), explain the role of \(\varepsilon<a\). What happens to the estimate when \(\varepsilon=a<1\)?

**Solution.** For \(\varepsilon<1\), the two full and double-prime frequency brackets are comparable on the region. The prime factor in (2) then contributes at most \(C\langle\xi\rangle^\varepsilon\), leaving decay exponent \(a-\varepsilon\). Its strict positivity lets arbitrarily high powers \(r_P^N\) overwhelm any initial loss in (27). At \(\varepsilon=a<1\), these particular estimates give only a uniform bound for \(J_P/S_P\), with no positive decay exponent. They do not imply rapid decrease on that larger region. A particular operator may have better estimates, but those would require additional information.

**Exercise 6. A leading coefficient without real zeros.** Consider
\[
P(s,t)=(1+s^2)t^3+t+1,
\]
where \(s\) is prime. Although \(1+s^2\) never vanishes for real \(s\), show that \(P\) is not partially hypoelliptic in \(t\). Give complex zeros witnessing the failure.

**Solution.** Here \(P_0=t^3+t+1\) is a nonzero one-variable polynomial, but \(P_2=t^3\) and \(P_2/P_0\to1\) at real infinity. The coefficient criterion fails. For real \(T>0\), set
\[
t=T,\qquad s=i\sqrt{1+T^{-2}+T^{-3}}.
\]
Then \(1+s^2=-T^{-2}-T^{-3}\), so \(P(s,T)=-T-1+T+1=0\). As \(T\to\infty\), the full imaginary part stays bounded and the prime real part equals zero. These are precisely the prohibited complex zeros. Nonvanishing of the leading coefficient on real prime frequency space does not suffice.

## References

- **[Grubb]** Gerd Grubb, *Distributions and Operators*, open lectures, sections on Fourier transformation and local regularity. [Lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- **[ODE]** Open mathematics courses, AN-01, *Weak equations and classical functions*, “Independence of one coordinate,” Theorem 2.1, and “First-order systems without commuting matrices,” Corollary 3.2 (higher-order scalar equations). The first gives \(t\)-independent distributions on a product; the second gives \(C^m\) regularity for an order-\(m\) scalar ordinary differential equation with smooth coefficients and continuous data.
