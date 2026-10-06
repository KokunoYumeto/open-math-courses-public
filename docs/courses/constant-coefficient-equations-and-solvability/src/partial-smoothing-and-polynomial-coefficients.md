# Partial smoothing and polynomial coefficients

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

Convolution can smooth selected variables while leaving the others untouched. An equation may then force smoothness in the remaining variables even though it is not hypoelliptic on the whole space. The deciding condition concerns complex zeros whose real components in the smoothed variables stay bounded.

Read [Hypoellipticity and complex zeros](hypoellipticity-and-complex-zeros.md) and [Weighted interior estimates and operator strength](weighted-interior-estimates-and-strength.md). We use the Fourier conventions and multiplier estimates from [Weighted Fourier spaces](weighted-fourier-spaces.md). Grubb [Grubb] supplies the distribution and Fourier background; Coste [Coste] gives context for the semialgebraic growth mechanism proved in [Symbols at infinity](symbols-at-infinity.md).

Keep \(D=-i\partial\). Polynomial coefficients may be complex. Split coordinates and frequencies as
\[
\begin{gathered}
x=(x',x''),\qquad \xi=(\xi',\xi''),\\
x'\in\mathbb R^j,\qquad x''\in\mathbb R^{n-j},\\
0\leq j<n.
\end{gathered}
\tag{1}
\]
The double-prime block has positive dimension. When \(j=0\), the assertions reduce to ordinary hypoellipticity; a test function on the zero-dimensional prime block is a scalar.

## Where a partial convolution is defined

For \(\psi\in C_c^\infty(\mathbb R^j)\), set
\[
T_\psi=\psi\otimes\delta_0,
\qquad
u*'\psi=u*T_\psi.
\tag{2}
\]
For an ordinary function this would be
\[
\begin{aligned}
&(u*'\psi)(x',x'')\\
&\quad=\int_{\mathbb R^j}u(x'-y',x'')\psi(y')\,dy'.
\end{aligned}
\tag{3}
\]
We use the distributional compact-convolution definition. If \(u\) is given only on an open \(X\subset\mathbb R^n\), the appropriate domain is
\[
X_\psi=\{x:x-(\operatorname{supp}\psi\times\{0\})\subset X\}.
\tag{4}
\]
This domain need not be contained in \(X\). It records the source points used in (3), with the minus sign fixed by convolution.

The set \(X_\psi\) is open. At each of its points the translated compact support is contained in the open set \(X\); a small change in that point preserves the containment. If \(\psi=0\), the support is empty, \(X_\psi=\mathbb R^n\), and the convolution is the zero distribution.

**Lemma 1.1.** Suppose \(u\in B_{p,k_1}^{\mathrm{loc}}(X)\), where \(1\leq p\leq\infty\) and the weights are positive and moderate. If
\[
k_2(\xi)\leq C\langle\xi'\rangle^N k_1(\xi)
\tag{5}
\]
for some finite \(N\), then \(u*'\psi\in B_{p,k_2}^{\mathrm{loc}}(X_\psi)\). The partial convolution is continuous with these local topologies. It is also continuous on distributions and commutes with constant-coefficient differentiation on \(X_\psi\).

**Proof.** Fix \(\phi\in C_c^\infty(X_\psi)\). The compact set
\[
\operatorname{supp}\phi-
(\operatorname{supp}\psi\times\{0\})
\]
lies in \(X\). Choose \(\chi\in C_c^\infty(X)\) equal to one on a neighborhood of this set. Near \(\operatorname{supp}\phi\), the partial convolution is \((\chi u)*T_\psi\), defined globally. Its Fourier transform is
\[
\widehat{(\chi u)*T_\psi}(\xi)
=\widehat{\chi u}(\xi)\widehat\psi(\xi').
\tag{6}
\]
Because \(\widehat\psi\) decreases faster than every power on real prime frequency space,
\[
\sup_\xi
\frac{k_2(\xi)}{k_1(\xi)}
|\widehat\psi(\xi')|<\infty.
\tag{7}
\]
Multiplication by this factor is bounded on weighted \(L^p\), including the supremum endpoint. The cutoff bound in \(B_{p,k_2}\) therefore gives
\[
\|\phi(u*'\psi)\|_{p,k_2}
\leq C_{\phi,\psi}\|\chi u\|_{p,k_1}.
\tag{8}
\]
This proves both local membership and continuity.

For distributional continuity, pairing the output with a compact test means pairing \(u\) with that test convolved with the reflected compact kernel. All such source tests have compact support in \(X\), and the operation is continuous on each test-function support space. The transpose defines the continuous distribution map. Differentiation commutes with compact convolution by the distributional convolution identities; localization uses the same translated support set. \(\square\)

Thus partial convolution provides every prescribed polynomial gain in \(\xi'\), while its Fourier multiplier supplies no decay in \(\xi''\).

## A condition on zeros and coefficients

For a nonzero polynomial \(P\), let \(d_P(\xi)\) be the distance from a real point \(\xi\) to its complex zero set. Set \(d_P=\infty\) for a nonzero constant. Use the full and positive-order derivative norms \(S_P,J_P\) from the weighted-interior lesson. For a constant, \(S_P=|P|\) and \(J_P=0\).

Expand uniquely in prime variables:
\[
\begin{gathered}
P(\xi',\xi'')=\sum_\gamma
P_\gamma(\xi'')(\xi')^\gamma,\\
P_\gamma(\xi'')
=\frac{\partial_{\xi'}^\gamma P(0,\xi'')}{\gamma!}.
\end{gathered}
\tag{9}
\]
Only finitely many coefficients are nonzero.

**Theorem 2.1.** The following seven conditions are equivalent.

1. Along the complex zeros of \(P\),
   \[
   \begin{gathered}
   |\operatorname{Im}\zeta|+
   |\operatorname{Re}\zeta'|\longrightarrow\infty\\
   \text{as }|\zeta|\longrightarrow\infty.
   \end{gathered}
   \tag{10}
   \]

2. In (9), \(P_0\) is nonzero and hypoelliptic in the double-prime variables, and
   \[
   \begin{gathered}
   P_\gamma(\xi'')/P_0(\xi'')\longrightarrow0\\
   (|\xi''|\to\infty,\ \gamma\ne0).
   \end{gathered}
   \tag{11}
   \]

3. The same \(P_0\) is nonzero and hypoelliptic, and some \(a,C>0\) satisfy
   \[
   \begin{gathered}
   \frac{|P_\gamma(\xi'')|}{1+|P_0(\xi'')|}
   \leq C\langle\xi''\rangle^{-a}\\
   (\gamma\ne0).
   \end{gathered}
   \tag{12}
   \]

4. \(d_P(\xi)\to\infty\) whenever \(|\xi''|\to\infty\) while \(\xi'\) remains bounded.

5. For some \(a,C>0\), globally
   \[
   \langle\xi\rangle^{2a}
   \leq C(1+d_P(\xi)^2)\langle\xi'\rangle^2.
   \tag{13}
   \]

6. On every bounded-prime strip, \(P\) is nonzero once \(|\xi''|\) is sufficiently large, and
   \[
   \frac{\partial^\alpha P(\xi)}{P(\xi)}
   \longrightarrow0\qquad(\alpha\ne0)
   \tag{14}
   \]
   as \(|\xi''|\to\infty\) with \(\xi'\) bounded. These are derivatives in all variables.

7. For some \(a,C>0\), globally
   \[
   \frac{J_P(\xi)}{S_P(\xi)}
   \leq C\langle\xi'\rangle\langle\xi\rangle^{-a}.
   \tag{15}
   \]

The positive exponents and constants may change between conditions. Quotients by \(P_0\) are taken at large double-prime frequencies, where hypoellipticity makes it nonzero.

**Proof: zeros and real strips.** For a nonconstant \(P\), its closed complex zero set is nonempty and closest zeros exist. If condition 4 fails, choose real points with bounded \(\xi'\), unbounded \(\xi''\), and uniformly bounded distance to closest zeros \(\zeta\). Those zeros tend to infinity while both \(\operatorname{Im}\zeta\) and \(\operatorname{Re}\zeta'\) stay bounded, contradicting 1. Conversely, if 1 fails, unbounded complex zeros with these two bounded quantities have real parts with bounded prime components and unbounded double-prime components. Their distance to the zero set is at most \(|\operatorname{Im}\zeta|\), contradicting 4.

The distance lemma of the complex-zeros lesson compares \(d_P^{-1}\) with the finite sum of fractional roots of every positive derivative ratio. On any fixed bounded-prime strip it shows that 4 and 6 are equivalent. Eventual nonvanishing on that strip is included explicitly; real zeros there cannot escape under condition 4.

**Proof: the uniform power estimates.** Assume 4 and set
\[
F(\xi)=(1+d_P(\xi)^2)\langle\xi'\rangle^2.
\tag{16}
\]
This continuous semialgebraic function tends to infinity as \(|\xi|\to\infty\). Otherwise a sequence with bounded \(F\) would have bounded \(\xi'\) and bounded \(d_P\); its double-prime part would tend to infinity, contrary to 4.

The minimum of \(F\) on each real sphere is attained and semialgebraic, by the distance and projection arguments already proved in the complex-zeros and symbols-at-infinity lessons. It tends to infinity, so its one-parameter asymptotics give a positive power lower bound. Reducing the positive exponent and increasing the constant to cover bounded frequencies proves (13). This proves 4 implies 5. Condition 5 immediately implies 4 on a bounded-prime strip.

The Cauchy estimate in the distance lemma also gives a global bound
\[
\frac{J_P(\xi)}{S_P(\xi)}
\leq \frac{C}{\sqrt{1+d_P(\xi)^2}}.
\tag{17}
\]
For \(d_P\geq1\), sum its positive derivative bounds relative to \(|P|\) and use \(|P|\leq S_P\); for \(d_P\leq1\), use \(J_P/S_P\leq1\) and enlarge \(C\). Combining (13) and (17) proves (15).

Finally, (15) implies \(J_P/S_P\to0\) on every bounded-prime strip. The identity \(S_P^2=|P|^2+J_P^2\) then gives \(|P|/S_P\to1\), proving eventual nonvanishing and (14). We have now proved all equivalences among 1, 4, 5, 6, and 7.

**Proof: the coefficient tests.** Assume 6. At \(\xi'=0\), \(P=P_0\). The double-prime derivative ratios and eventual nonvanishing make \(P_0\) nonzero and hypoelliptic by the complex-zeros criterion. The prime derivatives in (9) give (11) for every \(\gamma\ne0\). Moreover, (15) at \(\xi'=0\), together with \(|P_0|/S_P(0,\xi'')\to1\), gives (12) outside a ball. On the ball its denominator is positive and its numerator bounded, so enlarging \(C\) proves it everywhere. The finitely many coefficients permit one common exponent and constant. Thus 6 implies both 2 and 3.

Condition 3 implies 2. If \(P_0\) is nonconstant and hypoelliptic, then \(|P_0(\xi'')|\to\infty\): divide a nonzero constant highest derivative by \(P_0\) and use the derivative criterion. Hence \((1+|P_0|)/|P_0|\) stays bounded at infinity. The same ratio is a fixed finite number when \(P_0\) is constant. Equation (12) gives (11) in either case.

It remains to prove 2 implies 6. For \(\gamma\ne0\), (11) and the quotient criterion of Theorem 6.1 in the weighted-interior lesson give
\[
P_\gamma\ll P_0.
\tag{18}
\]
Every derivative of \(P_\gamma\) is weaker than \(P_\gamma\). A polynomial weaker than a dominated polynomial is also dominated: its unit derivative norm is bounded by that polynomial's unit norm, so divide by the same expanding denominator in the definition of domination. Thus all derivatives of \(P_\gamma\) are dominated by \(P_0\), and the same quotient criterion gives
\[
\begin{gathered}
\frac{\partial_{\xi''}^\beta P_\gamma}{P_0}
\longrightarrow0\\
(\gamma\ne0,\ \beta\text{ arbitrary}).
\end{gathered}
\tag{19}
\]
For \(\gamma=0,\beta\ne0\), the quotient tends to zero by hypoellipticity of \(P_0\). In the finite sum (9), uniformly for \(\xi'\) in any fixed bounded set, these facts imply
\[
\begin{gathered}
P(\xi',\xi'')/P_0(\xi'')\longrightarrow1,\\
\partial^\alpha P(\xi',\xi'')/P_0(\xi'')
\longrightarrow0\quad(\alpha\ne0).
\end{gathered}
\tag{20}
\]
Dividing the second limit by the first proves 6. Zero coefficient polynomials contribute nothing to these arguments.

For completeness, a nonzero constant \(P\) satisfies 1 vacuously, has \(P_0=P\) and all other coefficients zero, has \(d_P=\infty\), and has \(J_P=0\). Every assertion is then immediate, with (13) interpreted as an extended-real inequality. No ratio \(\infty/\infty\) is used. \(\square\)

Call \(P(D)\) **partially hypoelliptic with respect to the plane \(x''=0\)** when these conditions hold. Equivalently, \(P\) is partially hypoelliptic in the double-prime frequencies. The plane names the variables in which convolution smooths; the coefficient tests describe the remaining frequencies.

## Two different kinds of escape

Consider \(P(s,t)=t^2+s\), with \(s\) prime and \(t\) double-prime. The coefficient at \(s=0\) is \(P_0(t)=t^2\), a hypoelliptic one-variable polynomial. The only other coefficient is one, whose quotient by \(t^2\) tends to zero. Hence \(P\) is partially hypoelliptic in \(t\).

It is not fully hypoelliptic: its real zeros \((-t^2,t)\) are unbounded. They do satisfy the partial escape condition because their prime real component grows. Partial convolution can suppress these frequencies through \(\widehat\psi(-t^2)\).

In contrast \(P(s,t)=st+1\) has the real zeros \((-1/t,t)\), \(t\to+\infty\). Their prime component stays bounded and their imaginary parts vanish, so (10) fails. The next lesson proves that this failure prevents universal smoothing by partial convolution, even in a single fixed local weighted solution space.

If all variables are smoothed, \(j=n\), the usual convolution with a compact smooth function is smooth on its translated source domain for every distribution and every polynomial. The nonempty remaining block in (1) is needed for the coefficient characterization; the formula demanding a nonzero \(P_0=P(0)\) should not be applied to this separate case.

## Exercises with complete solutions

**Exercise 1. The translated domain.** Let \(X=(0,4)\times\mathbb R\), smooth in the first variable, and let \(\operatorname{supp}\psi=[1,2]\). Compute \(X_\psi\). Explain why its portion outside \(X\) causes no problem.

**Solution.** The source interval is \([x'-2,x'-1]\). It lies in \((0,4)\) exactly when \(x'>2\) and \(x'<5\). Thus \(X_\psi=(2,5)\times\mathbb R\). A point such as \(x'=9/2\), outside \(X\), uses source points between \(5/2\) and \(7/2\), all inside \(X\). Convolution is determined by these source points rather than by a value of \(u\) at the output point. Strict endpoint inequalities are necessary because the closed support must lie in the open interval.

**Exercise 2. A lower prime-dependent term.** Show that \(P(s,t)=t^3+it+s^2t\) is partially hypoelliptic in \(t\), but is not fully hypoelliptic.

**Solution.** Here \(P_0=t^3+it\), whose derivative ratios tend to zero along the real line and which is nonzero for large real \(|t|\). It is hypoelliptic by the complex-zeros criterion. The only nonzero coefficient with positive prime index is \(P_2=t\), and \(P_2/P_0=1/(t^2+i)\to0\). The coefficient test proves partial hypoellipticity. On the other hand \(P(s,0)=0\) for every real \(s\), giving unbounded real zeros and failure of full hypoellipticity.

**Exercise 3. A coefficient of the wrong size.** For \(P(s,t)=st+1\), identify the failure in the coefficient criterion, and check it against the zeros in the preceding example.

**Solution.** Its \(P_0=1\) is hypoelliptic, but \(P_1=t\) does not tend to zero relative to \(P_0\). Thus the presence of a hypoelliptic constant coefficient alone is insufficient. The zero path \((s,t)=(-1/t,t)\) has bounded prime real part and zero imaginary part, while its norm tends to infinity. It fails exactly the escape condition equivalent to the coefficient test.

**Exercise 4. More than one remaining variable.** Let \(s\) be prime and \((t_1,t_2)\) double-prime. Compare
\[
\begin{aligned}
P&=s+t_1^2+it_2,\\
Q&=s t_1^2+t_1^2+it_2.
\end{aligned}
\]

**Solution.** Both have \(P_0=Q_0=t_1^2+it_2\), the heat-type polynomial already shown hypoelliptic in the complex-zeros lesson. Its modulus tends to infinity on real double-prime space, so the other coefficient one in \(P\) has vanishing quotient. Thus \(P\) is partially hypoelliptic. For \(Q\), the other coefficient is \(t_1^2\), whose quotient by \(Q_0\) equals one on \((t_1,t_2)=(r,0)\), \(r\ne0\). It fails the criterion. The real zeros \((s,t_1,t_2)=(-1,r,0)\) confirm this failure with bounded prime frequency.

**Exercise 5. A constant base coefficient.** Suppose \(P_0\ne0\) is constant. Prove that \(P\) is partially hypoelliptic if and only if \(P\) itself is constant.

**Solution.** The coefficient test would require every \(P_\gamma\), \(\gamma\ne0\), to tend to zero at infinity on \(\mathbb R^{n-j}\). A nonzero constant polynomial does not tend to zero. A positive-degree polynomial has a real ray where its nonzero highest homogeneous part is nonzero, and it grows on that ray. Therefore the only polynomial tending to zero in this sense is zero. All other coefficients vanish and \(P=P_0\). Conversely a nonzero constant satisfies all the tests.

**Exercise 6. Why the strip condition gives a global power.** In the proof of (13), explain why knowing a separate distance bound on each bounded-prime strip is not itself a quantitative proof. What supplies the global estimate?

**Solution.** Separate strip bounds do not specify how their constants change as the prime bound grows, nor do they give a common rate in double-prime frequency. The function \(F=(1+d_P^2)\langle\xi'\rangle^2\) combines both escapes. Any sequence making \(F\) bounded would keep both the prime part and the distance bounded, contradicting the strip condition at infinity. Thus its spherical minimum tends to infinity. Semialgebraicity, projection, and the one-parameter power theorem then yield a single positive power valid on every sphere; bounded frequencies are absorbed by enlarging the constant. The polynomial rate comes from this algebraic argument, not from compactness alone.

## References

- **[Grubb]** Gerd Grubb, *Distributions and Operators*, open lectures, sections on distributions, Fourier transformation, and local regularity. [Lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- **[Coste]** Michel Coste, *Real Algebraic Sets*, lecture notes, 2003, §1.1 and §1.5. [ICTP notes](https://indico.ictp.it/event/a02455/session/9/contribution/6/material/0/0.pdf).
