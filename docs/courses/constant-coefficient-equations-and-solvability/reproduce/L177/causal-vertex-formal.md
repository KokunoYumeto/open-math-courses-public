# Causal inverses and stability at a cone's vertex

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by the writing AI GPT-6.1 Sol (OpenAI). Public domain (CC0 1.0).*

A causal inverse can grow rapidly and still act on every compactly supported test. Its support, rather than a growth estimate, makes convolution possible. We prove that changing a kernel away from the first point of its support preserves such an inverse. A second argument allows a change that is only sufficiently differentiable near that point. We then connect the support geometry to directional hyperbolicity and to the existing Fourier criteria.

Basic references are Richard Melrose's [Differential Analysis](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/), Gerd Grubb's [Fourier transformation of distributions](https://web.math.ku.dk/~grubb/dist5.pdf), and Lars Hörmander's *The Analysis of Linear Partial Differential Operators*, volumes I and II. The proofs used in this chapter are given here or in the following preceding lessons:

- Convolution as addition of supports, Theorems 1.1, 2.1, 3.1 and 3.2, and Proposition 3.3: proper-support convolution, finite-regularity smoothing, associativity, continuity with fixed supports, and the algebra of distributions in a cone containing no line.
- Support cones force reciprocal bounds, Theorem 1.1: the exact translated support cone and its reciprocal estimate.
- Logarithmic Fourier graphs construct a cone-supported inverse, Theorem 1.1: one common inverse from the stated estimates on a nonempty open convex cone that excludes zero.

All distributions and pairings are complex-linear. We work in real dimension \(n\ge1\). A closed convex cone \(C\) is nonempty, closed, convex, and invariant under multiplication by nonnegative scalars. In this chapter it is **pointed** when
\[
C\cap(-C)=\{0\}.
\tag{1.1}
\]
The cone \(\{0\}\) is allowed. We impose no growth or temperedness hypothesis on a cone-supported distribution.

## 1. A positive clock on a pointed cone

**Lemma 1.1 (a quantitative clock).** If \(C\ne\{0\}\) satisfies (1.1), there are a unit vector \(\tau\) and \(\kappa>0\) such that
\[
\tau\cdot x\ge\kappa|x|\quad(x\in C).
\tag{1.2}
\]
For \(C=\{0\}\), any unit vector and \(\kappa=1\) give the same inequality.

**Proof.** Let \(A=C\cap\{|x|=1\}\). This set is compact. Its convex hull is compact: every finite convex combination can be reduced to at most \(n+1\) points. Indeed, if there are more points, their augmented vectors \((x_j,1)\) are linearly dependent. Change the weights along a nonzero dependence, choosing its sign and increasing its magnitude until one positive weight becomes zero. The sum of the weights and the represented point stay fixed. Repeating gives at most \(n+1\) points. The convex hull is therefore the continuous image of the compact product of \(A^{n+1}\) and the closed simplex of weights.

Zero is not in this convex hull. If \(\sum_j\alpha_jx_j=0\) with positive weights and unit vectors \(x_j\in C\), then for any index \(j\) with positive weight,
\[
-x_j=\sum_{\ell\ne j}(\alpha_\ell/\alpha_j)x_\ell\in C.
\]
This contradicts (1.1). Choose a point \(q\) of least norm in the compact convex hull. Its norm is positive. For every \(x\) in that hull, differentiating \(|q+s(x-q)|^2\) at \(s=0+\) gives
\[
q\cdot x\ge |q|^2.
\]
Set \(\tau=q/|q|\) and \(\kappa=|q|\), and apply this inequality to \(x/|x|\) for every nonzero \(x\in C\). The zero case is immediate. \(\square\)

The clock makes the locality of addition explicit. If \(u_j\in C\), \(1\le j\le r\), and \(z=b+\sum_j u_j\), then
\[
\kappa\sum_j|u_j|
\le\sum_j\tau\cdot u_j=\tau\cdot(z-b).
\tag{1.3}
\]
For outputs in a fixed compact set, all the contributing coordinates are bounded. They form a closed set and hence a compact set. This proves the properness needed for any fixed number of factors supported in translates of \(C\). The convolution, commutativity, support inclusion, associativity and fixed-support continuity now follow from the exact preceding foundation theorems. We will use those theorems at these proper support sets, including for noncompact factors.

Write
\[
\mathcal A_C=\{T\in\mathcal D'(\mathbb R^n):
\operatorname{supp}T\subset C\}.
\tag{1.4}
\]
This is the commutative algebra of Proposition 3.3 of the preceding convolution lesson. Its identity is \(\delta_0\).

If \(T\in\mathcal A_C\) vanishes near zero, its closed support misses some ball of radius \(r>0\). Thus (1.2) gives
\[
\operatorname{supp}T\subset\{x\in C:\tau\cdot x\ge b\},
\qquad b=\kappa r>0.
\tag{1.5}
\]
If its support is empty, \(T=0\), and any \(b>0\) works.

## 2. An error with a delay has a locally finite inverse

**Theorem 2.1 (delayed Neumann series).** Let \(R\in\mathcal A_C\) vanish on a neighborhood of zero. Put \(R^{*0}=\delta_0\). Then
\[
S=\sum_{j=0}^{\infty}R^{*j}
\quad\text{is a distribution in }\mathcal A_C,
\qquad
(\delta_0-R)*S=\delta_0.
\tag{2.1}
\]
The series is locally finite on every compact set. It defines the unique inverse of \(\delta_0-R\) in \(\mathcal A_C\).

**Proof.** Choose \(b\) in (1.5). The support inclusion for proper convolution gives
\[
\operatorname{supp}R^{*j}\subset
\{x\in C:\tau\cdot x\ge jb\}\quad(j\ge1).
\tag{2.2}
\]
The inclusion follows by induction, since the clock adds. For a compact test support \(L\), let \(M_L=\max_{x\in L}\tau\cdot x\). Every term with \(jb>M_L\) vanishes on tests supported in \(L\). The sum is therefore finite on that support space, with a finite distributional order and bound. These finite definitions agree when the test support is enlarged. They define a distribution supported in the closed set \(C\).

For \(S_N=\sum_{j=0}^N R^{*j}\), associativity gives
\[
(\delta_0-R)*S_N=\delta_0-R^{*(N+1)}.
\tag{2.3}
\]
One can take the limit on each fixed test. Convolution is continuous for the fixed proper support pair \(C,C\), by Theorem 3.2 of the foundation lesson; \(S_N\to S\) distributionally, and the remainder vanishes eventually on that test by (2.2). This proves (2.1). Since the algebra is commutative, it is also a right inverse. If \(S'\) is another inverse in this algebra, then
\[
S'=S'*(\delta_0-R)*S=S.
\]
Every convolution in this identity is permitted by (1.3). \(\square\)

**Theorem 2.2 (stability away from the first support point).** Let \(a\in\mathbb R^n\). Suppose that
\[
\begin{gathered}
\mu,v\in\mathcal D'(\mathbb R^n),\qquad
\operatorname{supp}\mu,\operatorname{supp}v\subset a+C,\\
\operatorname{supp}E\subset C-a,\qquad
\mu*E=\delta_0,
\end{gathered}
\tag{2.4}
\]
and \(v-\mu\) vanishes near \(a\). There is a unique \(F\), supported in \(C-a\), satisfying
\[
v*F=\delta_0.
\tag{2.5}
\]
In particular, \(\mu\) need not be compactly supported.

**Proof.** Translate the kernel to the vertex and the inverse in the opposite direction:
\[
\mu_0=\tau_{-a}\mu,\quad v_0=\tau_{-a}v,\quad
E_0=\tau_a E.
\tag{2.6}
\]
All three supports lie in \(C\), and \(\mu_0*E_0=\delta_0\). Translation follows directly from the addition pairing in the foundation lesson. The distribution \(w_0=v_0-\mu_0\) vanishes near zero. Set
\[
R=(\mu_0-v_0)*E_0=-w_0*E_0.
\tag{2.7}
\]
Its support is in \(C\). Moreover, \(\operatorname{supp}w_0\) satisfies a positive clock bound (1.5), and \(\tau\cdot x\ge0\) on \(\operatorname{supp}E_0\). Their sum satisfies the same positive bound. Hence \(R\) vanishes near zero.

Theorem 2.1 provides \(S\) with \((\delta_0-R)*S=\delta_0\). Since
\[
v_0*E_0=\delta_0-R,
\qquad
F_0=E_0*S,
\tag{2.8}
\]
we have \(v_0*F_0=\delta_0\) and \(\operatorname{supp}F_0\subset C\). Set \(F=\tau_{-a}F_0\). This gives (2.5) and the required support. For uniqueness, translate any other such inverse into \(\mathcal A_C\) and use the uniqueness of an inverse in a commutative algebra. \(\square\)

The series in this theorem needs no convergence estimate at infinity. Its terms simply stop contributing on each bounded output region. Lower dimensional pointed cones are included.

## 3. A continuous error at the vertex also has an inverse

**Theorem 3.1 (locally continuous causal errors).** Suppose \(R\in\mathcal A_C\) is represented by a continuous function on some neighborhood of zero. Then \(\delta_0-R\) has an inverse in \(\mathcal A_C\).

**Proof.** Choose a compact smooth cutoff \(\chi\) supported inside that neighborhood, equal to one near zero, and with \(0\le\chi\le1\). Shrink its support until
\[
r_0=\chi R\in C_c^0,\qquad
\operatorname{supp}r_0\subset C,\qquad
\|r_0\|_{L^1}=q<1.
\tag{3.1}
\]
This is possible because the continuous representative is bounded on a fixed small closed ball, while the volume of a shrinking ball tends to zero. Multiplication by the cutoff gives a globally continuous compact function. The support inclusion follows because its distribution is \(\chi R\).

Ordinary integration and Fubini give \(\|f*g\|_1\le\|f\|_1\|g\|_1\) for integrable functions. Consequently
\[
T=\delta_0+\sum_{j=1}^{\infty}r_0^{*j}
\tag{3.2}
\]
converges in \(L^1\) after the delta term. Its support is in \(C\), since every partial sum has that support. The function terms are continuous: convolution with a compact continuous function is continuous by uniform continuity and dominated integration. Also
\[
\|r_0^{*j}\|_\infty
\le\|r_0\|_\infty q^{j-1}.
\tag{3.3}
\]
Thus their sum converges uniformly to a bounded continuous function. Telescoping the finite sums and using the \(L^1\) remainder bound \(q^{N+1}\) proves
\[
(\delta_0-r_0)*T=\delta_0.
\tag{3.4}
\]
This identity is also an identity in the cone algebra: its convolution agrees with ordinary integration for the function terms, by the foundation addition pairing, and convergence can be passed through the fixed proper supports.

Put \(R_1=R-r_0\). It vanishes near zero and is supported in \(C\). Define \(Q=T*R_1\). All factors lie in \(\mathcal A_C\), so this convolution exists even if \(R_1\) is not compact. Its support satisfies a positive clock bound, inherited from \(R_1\) because \(T\) has nonnegative clock. Therefore \(Q\) vanishes near zero. Theorem 2.1 gives \(S_1=(\delta_0-Q)^{-1}\) in the cone algebra.

The factorization is exact:
\[
\begin{aligned}
(\delta_0-r_0)*(\delta_0-Q)
&=\delta_0-r_0-(\delta_0-r_0)*T*R_1\\
&=\delta_0-r_0-R_1=\delta_0-R.
\end{aligned}
\tag{3.5}
\]
Its inverse is \(S=T*S_1\). Proper-support associativity justifies every product. This proves the theorem. \(\square\)

**Theorem 3.2 (a finite differentiability threshold).** Fix \(\mu,E,a,C\) as in (2.4). There is an integer \(m\ge0\), depending on \(E\) near \(-a\), with the following property. If \(v\) has support in \(a+C\) and \(v-\mu\) is represented by a \(C^m\) function on a neighborhood of \(a\), then \(v\) has a unique inverse supported in \(C-a\).

**Proof.** Use (2.6), and choose \(m\) to be a finite local order of \(E_0\) on the closed unit ball about zero, with a slightly larger compact neighborhood for its controlling test bound. The local finite-order property of a distribution supplies such an \(m\).

Let \(w_0=v_0-\mu_0\). It is \(C^m\) near zero. Choose a ball of radius \(r<1\) inside that neighborhood. Formula (1.3), for two cone coordinates with sum \(z\), implies
\[
|x|+|y|\le |z|/\kappa
\quad(x,y\in C,\ x+y=z).
\tag{3.6}
\]
For \(z\) sufficiently near zero, all contributing coordinates therefore lie well inside that ball. Choose compact smooth cutoffs \(\alpha,\beta\), supported in the ball and equal to one on a smaller ball containing all these coordinates. On a neighborhood of zero,
\[
w_0*E_0=(\alpha w_0)*(\beta E_0).
\tag{3.7}
\]
To verify the localization, take a test with sufficiently small support. On every contributing pair in the support of \(w_0\otimes E_0\), both cutoffs are one by (3.6). The difference of the two addition pairings is zero.

The first factor on the right is compactly supported and \(C^m\). The second is a compact distribution of order at most \(m\): multiplication by a fixed smooth cutoff preserves that order. The finite-regularity part of Theorem 2.1 of the foundation convolution lesson, with \(j=m\) and \(k=0\), makes (3.7) a continuous function. Thus \(R=-w_0*E_0\) is continuous near zero and belongs to \(\mathcal A_C\).

Theorem 3.1 provides \(S=(\delta_0-R)^{-1}\). Now \(F_0=E_0*S\) is a cone-supported inverse of \(v_0\), as in (2.8). Translate back. Uniqueness is the same cone-algebra argument as before. For \(C=\{0\}\), a function distribution supported in \(C\) is zero; the proof still applies, and the perturbation in this case is zero. \(\square\)

The differentiability requirement is a sufficient condition with an actual finite integer. It is not a claim that every less regular perturbation fails. No global derivative bound is imposed on the perturbation, and no compactness is imposed on \(v\) or on the inverse.

## 4. Three equivalent ways to see directional support

For a closed convex set \(K\subset\mathbb R^n\), let
\[
H_K(\eta)=\sup_{x\in K}x\cdot\eta.
\tag{4.1}
\]
The empty set has support value \(-\infty\). We allow \(+\infty\) for nonempty sets.

**Lemma 4.1 (support values, compact slices, and a translated cone).** Let \(\theta\ne0\). The following conditions are equivalent:

1. \(H_K(\eta)<+\infty\) for every \(\eta\) in some neighborhood of \(\theta\).
2. For every real \(c\), \(K\cap\{x:x\cdot\theta\ge c\}\) is compact, possibly empty.
3. There are \(x_0\in\mathbb R^n\) and \(A>0\) such that
\[
|x-x_0|\le A(x_0-x)\cdot\theta
\quad(x\in K).
\tag{4.2}
\]

**Proof.** The empty set satisfies all three conditions. Suppose \(K\) is nonempty.

For \(1\Rightarrow2\), choose \(h>0\) for which every \(\theta\pm h e_\ell\) has finite support value. For a point of the slice,
\[
\pm h x_\ell
\le H_K(\theta\pm h e_\ell)-c.
\tag{4.3}
\]
These finitely many bounds control every coordinate. The slice is closed and bounded and therefore compact. This is also the exact argument of Lemma 2.1 of the preceding support-cone lesson.

For \(2\Rightarrow3\), translate a point \(p\in K\) to zero, writing \(L=K-p\). Let
\[
L_{-1}=L\cap\{y:y\cdot\theta\ge-1\},\qquad
B=\max\{1,\max_{y\in L_{-1}}|y|\},\qquad
M=\max_{y\in L_{-1}}y\cdot\theta.
\tag{4.4}
\]
The set is compact and contains zero, so \(M\ge0\). If \(y\in L\) has \(y\cdot\theta<-1\), then \(s=-1/(y\cdot\theta)\) belongs to \((0,1)\). Convexity and \(0\in L\) give \(sy\in L\), and \(sy\cdot\theta=-1\). Hence
\[
|y|\le B(-y\cdot\theta).
\tag{4.5}
\]
Put \(d=M+1\), \(x_0=p+d\theta/|\theta|^2\), and choose
\[
A=\max\{B,\ 1/|\theta|,\ B+d/|\theta|\}.
\tag{4.6}
\]
For \(y\in L_{-1}\), the right side of (4.2) is \(A(d-y\cdot\theta)\ge A\), while the left side is at most \(B+d/|\theta|\le A\). For the remaining \(y\), (4.5) gives
\[
\left|y-\frac{d\theta}{|\theta|^2}\right|
\le B(-y\cdot\theta)+d/|\theta|
\le A(d-y\cdot\theta).
\]
Thus (4.2) holds in both cases.

For \(3\Rightarrow1\), let \(z=x-x_0\). Then \(z\cdot\theta\le-|z|/A\). If \(|\eta-\theta|<1/(2A)\), it follows that
\[
z\cdot\eta
\le-|z|/A+|z||\eta-\theta|\le0.
\tag{4.7}
\]
Therefore \(H_K(\eta)\le x_0\cdot\eta<\infty\) on that neighborhood. \(\square\)

The minus sign in (4.2) says the unbounded part of \(K\) goes in directions with negative \(\theta\)-pairing.

**Definition 4.2 (directional hyperbolicity).** A compact kernel \(\mu\) is hyperbolic in a nonzero direction \(\theta\) if it has a distributional inverse \(E\) supported in a convex set whose support function is finite near \(-\theta\). The inverse belongs to \(\mathcal D'\); it need not be tempered.

Taking the closed convex hull of its support preserves the condition. Indeed the support function is unchanged by taking that hull, since linear functions preserve convex combinations and are continuous under limits. With \(-\theta\) in Lemma 4.1, every low-time set
\[
K\cap\{x:x\cdot\theta\le T\}
\tag{4.8}
\]
is compact. Also \(K\) lies in a translated pointed cone facing the positive \(\theta\) direction. The cone defined by \(|z|\le A z\cdot\theta\) is closed and convex, since it is the sublevel set of the convex function \(|z|-A z\cdot\theta\); it contains no nonzero line.

The same directional support condition can be applied to the noncompact kernels of Theorems 2.2 and 3.2 whenever their convolution is defined by these proper cone supports.

## 5. Connecting the support picture to complex frequency

The analytic criteria already have complete preceding proofs. Here are their exact roles.

**Theorem 5.1 (the forward criterion).** Suppose \(\mu\in\mathcal E'\), \(E\in\mathcal D'\), and \(\mu*E=\delta_0\). Let \(K\) be the closed convex hull of \(\operatorname{supp}E\), and suppose
\[
\Gamma=\operatorname{int}\{\eta:H_K(\eta)<\infty\}\ne\varnothing.
\tag{5.1}
\]
There is a unique real vector \(a\) such that
\[
H_\mu(\eta)=-H_K(\eta)=a\cdot\eta\quad(\eta\in\Gamma).
\tag{5.2}
\]
With the negative polar
\[
C=\{x:x\cdot\eta\le0\text{ for all }\eta\in\Gamma\},
\tag{5.3}
\]
one has \(K=C-a\) and \(\operatorname{supp}\mu\subset C+a\). For every closed cone \(\Gamma_1\subset\Gamma\cup\{0\}\), there are constants \(D>0\) and an integer \(N\ge0\) such that
\[
\left|\widehat\mu(\zeta)^{-1}\right|
\le D(1+|\zeta|)^N e^{-a\cdot\operatorname{Im}\zeta}
\tag{5.4}
\]
whenever \(\operatorname{Im}\zeta\in\Gamma_1\) and
\[
|\operatorname{Im}\zeta|>D\log(|\zeta|+2).
\tag{5.5}
\]
The transform is nonzero in this region. The cone \(\Gamma=\mathbb R^n\) is allowed in this forward assertion.

**Proof.** This is Theorem 1.1 of Support cones force reciprocal bounds, with the same compact kernel, arbitrary distributional inverse, closed convex support hull, negative polar, translation, closed angular cones and logarithmic barrier. Rename its constants \(C_1,M\) as \(D,N\). No hypothesis on the growth or Fourier transform of \(E\) is added. \(\square\)

**Theorem 5.2 (the converse at an explicit cone convention).** Let \(\Gamma\) be nonempty, open in \(\mathbb R^n\), ordinarily convex, invariant under positive dilations, and exclude zero. Let \(\mu\in\mathcal E'\). Suppose that on each closed cone \(\Gamma_1\subset\Gamma\cup\{0\}\), its transform is nonzero beyond a logarithmic barrier and satisfies
\[
\left|\widehat\mu(\zeta)^{-1}\right|
\le D(1+|\zeta|)^N e^{A|\operatorname{Im}\zeta|}
\tag{5.6}
\]
there, with constants \(D\ge1\), \(A\ge0\), \(N\ge0\) that can depend on \(\Gamma_1\). Then one common \(E\in\mathcal D'\) satisfies \(\mu*E=\delta_0\) and \(H_K(\eta)<\infty\) for every \(\eta\in\Gamma\).

**Proof.** These are exactly the hypotheses and conclusion of Theorem 1.1 of Logarithmic Fourier graphs construct a cone-supported inverse. Its construction uses one distribution for all directions. Its support bound \(H_K(\eta)\le A|\eta|\) for each corresponding angular cone gives the assertion here. The closure of \(\Gamma\) is not required to be pointed. \(\square\)

These two criteria use different zero-containing cases. The following direct calculation explains why the distinction is mathematical.

**Example 5.3 (all directions cannot be inserted in the converse).** On \(\mathbb R\), let \(\mu=\delta'_0\). Then \(\widehat\mu(\zeta)=i\zeta\). On the whole imaginary-direction space \(\Gamma=\mathbb R\), the reciprocal bound with \(D=1\), \(N=0\), \(A=0\) holds whenever
\[
|\operatorname{Im}\zeta|>\log(|\zeta|+2).
\tag{5.7}
\]
In fact this inequality forces \(|\zeta|>1\): for \(0\le r\le1\), \(\log(r+2)-r\) decreases and has positive value \(\log3-1\) at one. Thus \(|\zeta|^{-1}<1\). The transform has no zero in (5.7).

There is nevertheless no inverse whose support function is finite in both directions. If its support hull \(K\) had finite values at \(1\) and \(-1\), it would be bounded, making the inverse compact. A compact solution of \(E'=\delta_0\) is impossible: choose a compact smooth test equal to one on a neighborhood of \(\operatorname{supp}E\cup\{0\}\). Then \(\langle E',\phi\rangle=-\langle E,\phi'\rangle=0\), while \(\langle\delta_0,\phi\rangle=1\).

An empty direction set also cannot give a converse: its estimates are vacuous, even for the zero kernel. These examples establish necessary qualifications. They make no attribution about an unspecified convention in another work.

## References

- Richard B. Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course materials](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Gerd Grubb, *Fourier transformation of distributions*. [Author-hosted chapter](https://web.math.ku.dk/~grubb/dist5.pdf).
- Convolution as addition of supports, Theorems 1.1, 2.1, 3.1 and 3.2, and Proposition 3.3.
- Support cones force reciprocal bounds, Theorem 1.1 and Lemma 2.1.
- Logarithmic Fourier graphs construct a cone-supported inverse, Theorem 1.1.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators*, volumes I and II, Springer. Background reference; the required proofs are the explicit internal ones cited above and those given in this chapter.
