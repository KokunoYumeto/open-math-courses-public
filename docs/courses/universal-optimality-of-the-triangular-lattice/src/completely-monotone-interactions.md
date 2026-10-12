# Completely monotone interactions

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

[Energy, density and the linear programming bound](energy-density-and-the-linear-programming-bound.md) shows how the triangular lattice \(A\) can be proved optimal for one Gaussian interaction \(e^{-\pi\alpha t}\) at a time. The interactions of interest are more general: inverse power laws \(t^{-s/2}\), sums of exponentials, and others. This lesson treats all interactions that are *completely monotone* functions of the squared distance, the class for which H. Cohn and A. Kumar conjectured the triangular lattice to be optimal [Cohn–Kumar]. The results:

- a completely monotone function that is finite at \(0\) is a mixture of the functions \(t\mapsto v^t\), \(0<v\le1\), with a positive measure as weights (Theorem 3.1); this is the theorem of Hausdorff, Bernstein and Widder in the form needed here, and it is proved through the moment problem on \([0,1]\) (Theorem 2.3);
- if a configuration has at least the energy of \(A\) for every Gaussian interaction, it has at least the energy of \(A\) for every completely monotone interaction, including interactions that are infinite at distance zero and lattice sums that diverge (Theorem 4.1);
- hence: if sharp pairs exist for all Gaussians, the triangular lattice is universally optimal (Theorem 5.1).

The lesson follows [OpenAI-T, Section 7]. The representation theorem is proved here by a different route: the measure is obtained from the Riesz representation theorem and identified through the uniqueness of the moment problem, which avoids limits of measures.

It uses the previous lesson, the core courses [Measure and Integration (D10)](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10) (Fatou's lemma, monotone and dominated convergence, image measures, uniqueness of measures) and [Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20) (the Weierstrass approximation theorem), and the representation of positive functionals by measures from [Finite Radon representation on locally compact spaces](course:HA-LCA/prerequisites/src/finite-radon-representation).

## 1. Completely monotone functions

Let \(J\) be the interval \((0,\infty)\) or \([0,\infty)\). A function \(g\colon J\to[0,\infty)\) is *completely monotone* if it is infinitely differentiable, with one-sided derivatives at \(0\) if \(0\in J\), and
\[
(-1)^r g^{(r)}(t)\ge0\qquad(r\ge0,\ t\in J).
\]
So \(g\ge0\), \(g'\le0\), \(g''\ge0\), and so on: \(g\) is nonincreasing and convex.

**Examples 1.1.** For \(c\ge0\) the function \(e^{-ct}\) is completely monotone on \([0,\infty)\). For \(s>0\) the function \(t^{-s}\) is completely monotone on \((0,\infty)\): its \(r\)-th derivative is \((-1)^rs(s+1)\cdots(s+r-1)\,t^{-s-r}\). Sums and nonnegative multiples of completely monotone functions are completely monotone. If \(g\) is completely monotone on \((0,\infty)\) and \(\varepsilon>0\), then \(F(t)=g(\varepsilon+t)\) is completely monotone on \([0,\infty)\).

For \(0\le v\le1\) and \(t>0\) let \(v^t\) have its usual meaning, with \(0^t=0\); and let \(v^0=1\) for all \(v\in[0,1]\). For fixed \(t>0\), \(v\mapsto v^t\) is continuous on \([0,1]\). With \(v=e^{-c}\), the functions \(t\mapsto v^t\), \(0<v\le1\), are the exponentials \(e^{-ct}\), \(c\ge0\).

## 2. The moment problem on the unit interval

For a sequence \(m=(m_j)_{j\ge0}\) of real numbers let \(\Delta m_j=m_{j+1}-m_j\), and let \(\Delta^r\) be the \(r\)-fold application, \(\Delta^0m=m\). By induction on \(n\),
\[
\Delta^nm_p=\sum_{i=0}^n\binom ni(-1)^{n-i}m_{p+i}.
\]

**Lemma 2.1.** Let \(F\) be completely monotone on \([0,\infty)\), \(d>0\), and \(m_j=F(jd)\). Then \((-1)^r\Delta^rm_j\ge0\) for all \(r,j\ge0\).

**Proof.** For an infinitely differentiable function \(\phi\) on \([0,\infty)\) let \((\Delta_d\phi)(t)=\phi(t+d)-\phi(t)\); this is \(\int_0^d\phi'(t+u)\,du\). By induction on \(r\),
\[
\begin{gathered}
(\Delta_d^r\phi)(t)=\int_{[0,d]^r}\phi^{(r)}(t+u)\,du_1\cdots du_r,\\
u=u_1+\dots+u_r .
\end{gathered}
\]
For \(\phi=F\) and \(t=jd\) the left side is \(\Delta^rm_j\), and \((-1)^rF^{(r)}\ge0\). \(\blacksquare\)

Let \(\beta_{M,p}(x)=\binom Mpx^p(1-x)^{M-p}\) for \(0\le p\le M\). For a polynomial \(P\) let
\[
B_MP=\sum_{p=0}^MP(p/M)\,\beta_{M,p},
\]
the *Bernstein polynomial* of \(P\).

**Lemma 2.2.**

1. \(\sum_{p=0}^M\binom pi\beta_{M,p}=\binom Mix^i\) for \(0\le i\le M\).
2. For every \(j\ge0\) and \(M\ge j\), \(B_M(x^j)=\sum_{i=0}^jc_{M,j,i}x^i\) with numbers \(c_{M,j,i}\) such that, as \(M\to\infty\), \(c_{M,j,j}\to1\) and \(c_{M,j,i}\to0\) for \(i<j\).

**Proof.** (1) Since \(\binom Mp\binom pi=\binom Mi\binom{M-i}{p-i}\), the left side is
\[
\begin{gathered}
\binom Mix^i\sum_{q=0}^{M-i}\binom{M-i}qx^q(1-x)^{M-i-q}\\
=\binom Mix^i .
\end{gathered}
\]
(2) The polynomials \(p(p-1)\cdots(p-i+1)=i!\binom pi\) in the variable \(p\), for \(i=0,\dots,j\), have degrees \(0,\dots,j\) and leading coefficient \(1\). So there are numbers \(s_{j,i}\), with \(s_{j,j}=1\), such that \(p^j=\sum_{i\le j}s_{j,i}\,i!\binom pi\) for all \(p\). By (1),
\[
\begin{gathered}
B_M(x^j)=M^{-j}\sum_{i\le j}s_{j,i}\,i!\binom Mix^i\\
=\sum_{i\le j}s_{j,i}\,q_{M,i}\,x^i,\\
q_{M,i}=\frac{M(M-1)\cdots(M-i+1)}{M^j}.
\end{gathered}
\]
The quotient \(q_{M,i}\) is \(\prod_{r<j}(1-r/M)\to1\) for \(i=j\), and at most \(M^{i-j}\to0\) for \(i<j\). \(\blacksquare\)

**Theorem 2.3** (Hausdorff). Let \((m_j)_{j\ge0}\) be real numbers with \((-1)^r\Delta^rm_j\ge0\) for all \(r,j\ge0\). Then there is exactly one finite positive Borel measure \(\eta\) on \([0,1]\) with
\[
\int_{[0,1]}x^j\,d\eta(x)=m_j\qquad(j\ge0).
\]

**Proof.** Let \(\Lambda\) be the linear map from the polynomials to \(\mathbb R\) with \(\Lambda(x^j)=m_j\).

*Step 1.* Expanding \((1-x)^n\) and using the formula for \(\Delta^n\),
\[
\begin{aligned}
\Lambda\bigl(x^p(1-x)^n\bigr)&=\sum_{i=0}^n\binom ni(-1)^im_{p+i}\\
&=(-1)^n\Delta^nm_p\ge0 .
\end{aligned}
\]
So \(\Lambda(\beta_{M,p})\ge0\) for all \(M,p\).

*Step 2.* For every polynomial \(P\), \(\Lambda(B_MP)\to\Lambda(P)\) as \(M\to\infty\). By linearity it suffices to take \(P=x^j\), and then it follows from Lemma 2.2(2).

*Step 3.* If \(P\ge0\) on \([0,1]\), then \(\Lambda(B_MP)=\sum_pP(p/M)\Lambda(\beta_{M,p})\ge0\), hence \(\Lambda(P)\ge0\) by Step 2. Applied to \(\|P\|\pm P\), where \(\|P\|\) is the largest value of \(|P|\) on \([0,1]\), this gives
\[
|\Lambda(P)|\le m_0\,\|P\| .
\]
*Step 4.* By the Weierstrass approximation theorem the polynomials are dense in the space \(C[0,1]\) of continuous real functions with the norm \(\|\cdot\|\). By Step 3, \(\Lambda\) extends uniquely to a continuous linear functional on \(C[0,1]\), and the extension is positive: a continuous \(\phi\ge0\) is the uniform limit of the polynomials \(P_n+\|P_n-\phi\|\ge0\), where \(P_n\to\phi\).

*Step 5.* By the representation theorem for positive functionals (Theorem 3.1 of the lesson on finite Radon representation, for the compact space \([0,1]\)) there is a finite positive Borel measure \(\eta\) with \(\Lambda(\phi)=\int\phi\,d\eta\) for all \(\phi\in C[0,1]\). In particular \(\int x^j\,d\eta=m_j\).

*Uniqueness.* Let \(\eta'\) be a second such measure. Then \(\int P\,d\eta'=\int P\,d\eta\) for polynomials, hence for all continuous functions, by uniform approximation. For a closed set \(C\subseteq[0,1]\) the continuous functions \(\phi_n(x)=\max(0,1-n\operatorname{dist}(x,C))\) decrease to the indicator function of \(C\), so \(\eta'(C)=\eta(C)\) by dominated convergence. The closed sets are closed under finite intersections and generate the Borel sets, and \(\eta'([0,1])=\eta([0,1])\); so \(\eta'=\eta\). \(\blacksquare\)

## 3. The representation

**Theorem 3.1.** Let \(F\) be completely monotone on \([0,\infty)\). There is a finite positive Borel measure \(\rho\) on \([0,1]\) such that
\[
F(t)=\int_{[0,1]}v^t\,d\rho(v)\qquad(t\ge0).
\]
It has total mass \(F(0)\), and \(\rho(\{0\})=0\).

**Proof.** For an integer \(l\ge1\) the sequence \(m_j=F(j/l)\) satisfies the assumption of Theorem 2.3, by Lemma 2.1. Let \(\eta_l\) be its measure, and \(\rho=\eta_1\). So
\[
\begin{gathered}
\int x^j\,d\eta_l(x)=F(j/l),\\
\int v^j\,d\rho(v)=F(j).
\end{gathered}
\]
*The measures \(\eta_l\) are images of \(\rho\).* Let \(\kappa\) be the image of \(\eta_l\) under the map \(x\mapsto x^l\) of \([0,1]\). Then \(\int v^j\,d\kappa(v)=\int x^{lj}\,d\eta_l(x)=F(j)\). By the uniqueness in Theorem 2.3, \(\kappa=\rho\). The map \(x\mapsto x^l\) is a homeomorphism of \([0,1]\) with inverse \(v\mapsto v^{1/l}\); so \(\eta_l\) is the image of \(\rho\) under \(v\mapsto v^{1/l}\), and
\[
\int v^{j/l}\,d\rho(v)=\int x^j\,d\eta_l(x)=F(j/l).
\]
*All real exponents.* So \(F(t)=\int v^t\,d\rho\) for all rational \(t\ge0\). Let \(t>0\) be real and \(t_n\to t\) rational, \(t_n>0\). Then \(v^{t_n}\to v^t\) for every \(v\in[0,1]\), and these functions are bounded by \(1\). By dominated convergence \(\int v^{t_n}\,d\rho\to\int v^t\,d\rho\), and \(F(t_n)\to F(t)\) because \(F\) is continuous.

*The mass.* For \(t=0\) the formula says \(\rho([0,1])=F(0)\). As \(t\) decreases to \(0\), the functions \(v^t\) increase to the indicator function of \((0,1]\). By monotone convergence \(\rho((0,1])=\lim_{t\to0}F(t)=F(0)\). So \(\rho(\{0\})=0\). \(\blacksquare\)

**Examples 3.2.** For \(F(t)=e^{-ct}\) the measure \(\rho\) is the unit mass at \(v=e^{-c}\). For \(F(t)=1/(1+t)\) it is Lebesgue measure on \([0,1]\), since \(\int_0^1v^t\,dv=1/(t+1)\).

Under the substitution \(v=e^{-c}\) the theorem says that \(F\) is the Laplace transform of a finite positive measure on \([0,\infty)\). A completely monotone function on \((0,\infty)\) that is unbounded near \(0\), such as \(t^{-s}\), has no representation with a finite measure. For such functions the theorem is applied to the shifted functions \(g(\varepsilon+t)\).

## 4. From Gaussians to completely monotone interactions

Let \(A\) be the triangular lattice of covolume one. For a configuration \(\mathcal C\) of density one, the sets \(\mathcal C_R\), the numbers \(N_R\) and the energy \(E_g(\mathcal C)\) are as in the previous lesson.

**Theorem 4.1.** Let \(\mathcal C\) be a configuration of density one such that for every \(\alpha>0\)
\[
\begin{gathered}
\liminf_{R\to\infty}\frac1{N_R}\sum_{\substack{x,y\in\mathcal C_R\\x\ne y}}e^{-\pi\alpha|x-y|^2}\\
\ge\sum_{a\in A\setminus\{0\}}e^{-\pi\alpha|a|^2}.
\end{gathered}
\]
Then for every completely monotone \(g\colon(0,\infty)\to[0,\infty)\)
\[
E_g(\mathcal C)\ \ge\ \sum_{a\in A\setminus\{0\}}g(|a|^2),
\]
where both sides may be \(\infty\).

**Proof.** Fix \(\varepsilon>0\) and let \(F(t)=g(\varepsilon+t)\), completely monotone on \([0,\infty)\). Let \(\rho\) be its measure from Theorem 3.1.

Let \(R_n\to\infty\) be any sequence with \(N_{R_n}>0\). For \(v\in[0,1]\) put
\[
\begin{gathered}
A_n(v)=\frac1{N_{R_n}}\sum_{\substack{x,y\in\mathcal C_{R_n}\\x\ne y}}v^{|x-y|^2},\\
L(v)=\sum_{a\in A\setminus\{0\}}v^{|a|^2}\in[0,\infty].
\end{gathered}
\]
All exponents are positive. The functions \(A_n\) are continuous, and \(L\) is a sum of nonnegative continuous functions, hence measurable.

*\(\liminf_nA_n(v)\ge L(v)\) for every \(v\in[0,1]\).* For \(0<v<1\) this is the assumption with \(\alpha=-\log(v)/\pi\), because \(v^t=e^{-\pi\alpha t}\); a lower limit over all \(R\) is at most the lower limit along a sequence. For \(v=0\) both sides are \(0\). For \(v=1\), \(A_n(1)=N_{R_n}-1\to\infty=L(1)\).

*Integration.* By Theorem 3.1, applied to each term,
\[
\begin{gathered}
\frac1{N_{R_n}}\sum_{\substack{x,y\in\mathcal C_{R_n}\\x\ne y}}F(|x-y|^2)\\
=\int A_n\,d\rho .
\end{gathered}
\]
By Fatou's lemma and the monotone convergence theorem for the series \(L\),
\[
\begin{aligned}
\liminf_n\int A_n\,d\rho&\ge\int\liminf_nA_n\,d\rho\\
&\ge\int L\,d\rho\\
&=\sum_{a\in A\setminus\{0\}}\int v^{|a|^2}\,d\rho\\
&=\sum_{a\in A\setminus\{0\}}F(|a|^2).
\end{aligned}
\]
All integrands are nonnegative, so this holds also when the last sum is infinite. The sequence \((R_n)\) was arbitrary. Hence
\[
E_F(\mathcal C)\ \ge\ \sum_{a\in A\setminus\{0\}}g(\varepsilon+|a|^2),
\]
where \(E_F\) is the energy for the interaction \(t\mapsto F(t)\), \(t>0\).

*Removing the shift.* Since \(g\) is nonincreasing, \(g(t)\ge g(\varepsilon+t)=F(t)\), so \(E_g(\mathcal C)\ge E_F(\mathcal C)\). As \(\varepsilon\) decreases to \(0\), the terms \(g(\varepsilon+|a|^2)\) increase to \(g(|a|^2)\), and the sums increase to \(\sum_{a\ne0}g(|a|^2)\) by monotone convergence. \(\blacksquare\)

The shift is removed after the lattice sum has been formed. At no point is a representing measure for \(g\) itself needed, and no limit in \(\varepsilon\) is exchanged with the lower limit in \(R\).

## 5. The theorem

Let \((\mathrm G)\) be the statement: *for every \(\alpha>0\) there is a sharp pair for \(\alpha\)*, in the sense of Section 4 of the previous lesson.

**Theorem 5.1.** Assume \((\mathrm G)\). Let \(g\colon(0,\infty)\to[0,\infty)\) be completely monotone. Then for every configuration \(\mathcal C\) of density one in the plane
\[
E_g(\mathcal C)\ \ge\ E_g(A)=\sum_{a\in A\setminus\{0\}}g(|a|^2)
\]
in \([0,\infty]\).

**Proof.** By \((\mathrm G)\) and Theorem 4.2 of the previous lesson, \(\mathcal C\) satisfies the assumption of Theorem 4.1. The equality is Lemma 1.1 of the previous lesson. \(\blacksquare\)

The statement \((\mathrm G)\) is a theorem of [OpenAI-T]: its Sections 2 to 5, with two appendices of verified computations, construct the sharp pairs. With it, Theorem 5.1 is the *universal optimality* of the triangular lattice, the main theorem of [OpenAI-T, Section 1]. In this course \((\mathrm G)\) is a hypothesis; everything else in the proof of Theorem 5.1 is proved in these two lessons and the lessons they cite.

The theorem covers inverse power laws \(g(t)=t^{-s/2}\) for all \(s>0\). For \(s\le2\) the lattice sum diverges, and the statement is that every configuration of density one has infinite energy (Exercise 6.3).

## 6. Exercises

**6.1.** Show that the product of two completely monotone functions on \((0,\infty)\) is completely monotone.

**6.2.** Determine the sequence \(m_j=F(j)\) and check the inequalities \((-1)^r\Delta^rm_j\ge0\) directly for \(F(t)=e^{-ct}\), \(c>0\).

**6.3.** Let \(0<s\le2\). Show that \(\sum_{a\in A\setminus\{0\}}|a|^{-s}=\infty\).

**6.4.** Let \(g\) be completely monotone on \((0,\infty)\) with \(g(t_0)=0\) for some \(t_0>0\). Show that \(g=0\).

## 7. Solutions

**6.1.** By the product rule, \((fg)^{(r)}=\sum_i\binom rif^{(i)}g^{(r-i)}\), and \((-1)^rf^{(i)}g^{(r-i)}\) is the product of \((-1)^if^{(i)}\ge0\) and \((-1)^{r-i}g^{(r-i)}\ge0\).

**6.2.** \(m_j=q^j\) with \(q=e^{-c}\in(0,1)\). Then \(\Delta m_j=q^j(q-1)\), and by induction \(\Delta^rm_j=q^j(q-1)^r\). So \((-1)^r\Delta^rm_j=q^j(1-q)^r\ge0\). The measure of Theorem 2.3 is the unit mass at \(q\).

**6.3.** By Lemma 1.1 of the previous lesson, the number of points of \(A\) in the disk \(B_R\) is \(\pi R^2(1+o(1))\). So the number of \(a\in A\) with \(2^k<|a|\le2^{k+1}\) is \(3\pi4^k(1+o(1))\) as \(k\to\infty\), and each of them has \(|a|^{-s}\ge2^{-s(k+1)}\). The sum over this ring is at least a positive constant times \(4^k2^{-sk}=2^{(2-s)k}\ge1\) for large \(k\). So the series diverges.

**6.4.** Let \(0<\varepsilon<t_0\) and \(F(t)=g(\varepsilon+t)\), with measure \(\rho\) by Theorem 3.1. Then \(0=F(t_0-\varepsilon)=\int v^{t_0-\varepsilon}\,d\rho\), and the integrand is positive on \((0,1]\); so \(\rho((0,1])=0\). Since \(\rho(\{0\})=0\), \(\rho=0\) and \(F=0\). Hence \(g=0\) on \([\varepsilon,\infty)\) for every small \(\varepsilon\).

## References

- [OpenAI-T] OpenAI, *Universal optimality of the triangular lattice*, OpenAI Math Release preprint, 23 September 2026, Section 7. https://github.com/openai/math/tree/main/preprints/Universal-optimality-of-the-triangular-lattice-September-23-2026
- [Cohn–Kumar] H. Cohn and A. Kumar, *Universally optimal distribution of points on spheres*, Journal of the American Mathematical Society 20 (2007), Section 9. https://arxiv.org/abs/math/0607446
