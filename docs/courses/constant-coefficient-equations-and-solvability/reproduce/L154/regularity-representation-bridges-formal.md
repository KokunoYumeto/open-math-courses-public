# From complex solution representations to real regularity estimates

*Original proof exposition by GPT-6.1 Sol (OpenAI), Ultra, October 2026. CC0 1.0.*

We solve the two separate exercise targets on printed page 291 of Hörmander's Chapter 15. The first identifies the exact real polynomial-strength criterion with the complex characteristic growth criterion. The second derives the high directional derivative bound from the tube representation. The arbitrary-distribution representation exercises on printed page 300 remain separate active targets.

Use \(D=-i\partial\) and the bilinear Fourier convention of [L150](../../AN02-L150.html#nv1-the-exact-representation-theorem). Physical regularity weights here are denoted \(k,k_1\); the reflected reciprocal required when applying the representation theorem is supplied explicitly below. The actual general weighted theorem being compared is [L022 Theorem1.1](../../AN02-L022.html#the-weight-that-pays-for-a-commutator), and the hypoellipticity criterion used in the heat example is [L021 Theorems2.1–3.1](../../AN02-L021.html#retreat-from-real-space-has-a-polynomial-rate). Finite complex root factorization and coefficient extraction also use the complete [L045 Cauchy/root-count proofs](../../AN02-L045.html#cauchy-estimates-and-parameter-contours).

## EB1. Full polynomial strength versus distance to complex zeros

Let \(P\) be a nonconstant complex polynomial of degree \(m\ge1\) on \(\mathbb C^n\). For real \(\xi\), define
\[
A(\xi)=\left(\sum_\alpha|\partial^\alpha P(\xi)|^2\right)^{1/2},
\quad B(\xi)=\left(\sum_{|\alpha|>0}|\partial^\alpha P(\xi)|^2\right)^{1/2},
\quad r_P(\xi)=A(\xi)/B(\xi),
\quad d_P(\xi)=\operatorname{dist}(\xi,\{P=0\}).
\tag{EB1}
\]
All derivatives are ordinary derivatives, without factorial normalization. A top-order derivative is a nonzero constant, so \(B>0\), \(A>0\), and \(r_P\ge1\). The nonempty zero set is closed; a nearest zero exists by compactness of a closed bounded distance-minimizing sequence.

We prove constants depending only on \(n,m\) such that
\[
c_{n,m}(1+d_P(\xi))\le r_P(\xi)
\le C_{n,m}(1+d_P(\xi))^m.
\tag{EB2}
\]
For the upper bound choose a nearest zero \(z\), \(|z-\xi|=d\), and Taylor-expand:
\[
|P(\xi)|
\le\sum_{1\le|\alpha|\le m}
       \frac{|\partial^\alpha P(\xi)|}{\alpha!}|z-\xi|^{|\alpha|}
\le C_{n,m}B(\xi)(1+d)^m.
\tag{EB3}
\]
Since \(A^2=|P|^2+B^2\), EB3 proves the upper bound.

For the lower bound, first let \(d\ge1\). Then \(P(\xi)\ne0\). For every complex unit vector \(\omega\), the one-variable polynomial \(q_\omega(t)=P(\xi+t\omega)\) has no zero in \(|t|<d\). Factor its at most \(m\) roots:
\[
q_\omega(t)=P(\xi)\prod_{\nu=1}^{l}(1-t/a_\nu),
\quad |a_\nu|\ge d,\quad
\left|[t^a]q_\omega(t)\right|
\le\binom ma d^{-a}|P(\xi)|.
\tag{EB4}
\]
A constant polynomial has \(l=0\), satisfying the same inequalities. The homogeneous Taylor coefficient
\(T_a(\omega)=\sum_{|\alpha|=a}\partial^\alpha P(\xi)\omega^\alpha/\alpha!\)
is therefore bounded on the complex unit sphere by the last expression. Evaluate it on
\(\omega_j=n^{-1/2}e^{i\theta_j}\), which has unit norm. Multiplication by \(e^{-i\alpha\cdot\theta}\) and integration over the \(n\)-torus extracts its coefficient; orthogonality of the integer exponentials gives
\[
|\partial^\alpha P(\xi)|
\le \alpha!n^{|\alpha|/2}\binom m{|\alpha|}
           d^{-|\alpha|}|P(\xi)|.
\tag{EB5}
\]
There are finitely many derivatives, so for \(d\ge1\),
\(B\le C_{n,m}|P(\xi)|/d\). Thus \(r_P\ge |P|/B\ge c_{n,m}d\).
For \(d<1\), \(r_P\ge1\) gives the remaining part of EB2 after decreasing the constant. This proves the full two-sided polynomial comparison, without hypoellipticity.

## EB2. The exact first exercise equivalence

A positive shift weight satisfies \(k(\xi+h)\le(1+C|h|)^N k(\xi)\). Reflection and reciprocal preserve this property by applying it in reverse, and products preserve it by multiplying the inequalities. Thus \(a=k/k_1\) is also a shift weight.

We prove equivalence of the following two conditions, with possibly different constants and nonnegative powers:
\[
\begin{aligned}
k(\xi)&\le C k_1(\xi)r_P(\xi)^N &&(\xi\in\mathbb R^n),\\
k(\operatorname{Re}z)&\le C'k_1(\operatorname{Re}z)
              (1+|\operatorname{Im}z|)^{N'} &&(P(z)=0).
\end{aligned}
\tag{EB6}
\]
The first is exactly source formula 11.1.7, and the second exactly formula 15.3.8.

First EB2 shows that the first line is equivalent, up to changing the exponent, to
\[
a(\xi)\le C(1+d_P(\xi))^L.
\tag{EB7}
\]
For a zero \(z=\xi+i\eta\), \(d_P(\xi)\le|\eta|\), so EB7 immediately gives the second line of EB6.
Conversely suppose that line holds. For any real \(\xi\), choose a nearest zero \(z\). Shift moderation of \(a\) gives
\[
a(\xi)\le (1+C_a|\xi-\operatorname{Re}z|)^{M_a}
                   a(\operatorname{Re}z)
\le C(1+d_P(\xi))^{M_a+N'}.
\tag{EB8}
\]
Here both the real displacement and the imaginary part of \(z\) are at most its distance from \(\xi\). EB2 then bounds this by a power of \(r_P\), proving the first line. All constants are uniform in \(\xi\); exponent changes are allowed by the two source conditions.

For homogeneous solutions the additional datum condition 11.1.8 creates no extra restriction. Choose \(k_2=k/A\); then \(f=0\) belongs to its local weighted space and
\(k\le k_1+A k_2\). The weight \(A\) is itself a shift weight: finite Taylor expansion of each derivative bounds its strength at \(\xi+h\) by \(C_m(1+|h|)^mA(\xi)\). To remove the harmless prefactor near \(h=0\), the vector of all jets has derivative norm at most a fixed multiple of its own norm, giving a bounded gradient of \(\log A\); combine this local Lipschitz estimate with the polynomial estimate at \(|h|\ge1\) to obtain a bound of the required form \((1+C|h|)^{N_A}\). The reciprocal and product rules therefore make \(k/A\) a shift weight too.

Consequently the homogeneous \(p=2\) regularity conclusion of Theorem11.1.7, \(u\in B_{2,k_1}^{\mathrm{loc}}\), \(P(D)u=0\Rightarrow u\in B_{2,k}^{\mathrm{loc}}\), has exactly the same admissible weight criterion as [L150 NV10, Corollary15.3.2](../../AN02-L150.html#nv10-transfer-of-weights-on-the-characteristic-set). This solves the first exercise with the positive-order derivative strength retained. A nonzero constant polynomial has no homogeneous solutions except zero, and its \(B\) is zero; the ratio comparison is stated only for nonconstant \(P\). For \(P=0\), the complex condition reduces to a bounded weight ratio on the real plane; the indeterminate strength ratio is not used.

## EB3. The directional geometric bridge needed for the second exercise

Let \(P\) be nonconstant and hypoelliptic, \(\gamma\in\mathbb R^n\), and suppose
\[
|\gamma\cdot\xi|\le C(1+d_P(\xi))^\rho
\quad(\xi\in\mathbb R^n).
\tag{EB9}
\]
If \(\gamma=0\), every positive directional derivative is zero. Otherwise \(\rho\ge1\): choose one zero \(z_0\) and put \(\xi=t\gamma\). Then \(d_P(t\gamma)\le|t\gamma-z_0|\le t|\gamma|+|z_0|\), while the left side is \(t|\gamma|^2\), excluding every \(\rho<1\).

At a zero \(z=\xi+i\eta\), \(d_P(\xi)\le|\eta|\), so
\[
|\gamma\cdot z|
\le|\gamma\cdot\xi|+|\gamma||\eta|
\le C_1(1+|\eta|)^\rho.
\tag{EB10}
\]
Conversely EB10 and a nearest zero give EB9, by the triangle inequality and \(\rho\ge1\). This is the precise prescribed-exponent bridge of Theorem11.4.8, whose full higher-dimensional strip-growth proof is [L030 Theorem1.1](../../AN02-L030.html#strip-maxima-and-their-optimal-powers). The elementary bridge just given also works in dimension one for \(\rho\ge1\).

The same inequality holds on the unit tube \(\mathcal N_P(1)\). Choose a zero \(\theta\) within distance one of any tube point \(z\); its imaginary part is at most \(1+|\operatorname{Im}z|\), and \(|\gamma\cdot(z-\theta)|\le|\gamma|\). Thus
\[
|\gamma\cdot z|\le C_2(1+|\operatorname{Im}z|)^\rho
\quad(z\in\mathcal N_P(1)).
\tag{EB11}
\]

## EB4. Full high-derivative estimate from the tube integral

Let \(P(D)u=0\) in a neighborhood of a compact \(K\). Hypoellipticity makes \(u\) smooth there, since its datum is the smooth zero function. On a convex ball compact in that neighborhood, choose the test weight
\[
\kappa(\xi)=\langle\xi\rangle^{-s},\quad
\langle\xi\rangle=(1+|\xi|^2)^{1/2},\quad s=n+1.
\tag{EB12}
\]
Its reflected reciprocal is \(\langle\xi\rangle^s\); compact cutoffs of a smooth \(u\) have rapidly decreasing Fourier transforms and therefore belong to this local physical space. The shift inequality for \(\kappa\) follows from
\(\langle\xi\rangle\le\langle\xi+h\rangle+|h|\le(1+|h|)\langle\xi+h\rangle\).

Apply the complete tube theorem [L150 NV1–NV8](../../AN02-L150.html#nv1-the-exact-representation-theorem), with radius one. It gives a measurable \(U\) and four-condition \(\Phi\) for which
\[
u(x)=\int_{\mathcal N_P(1)}U(z)e^{ix\cdot z}\,dV(z)
\quad\hbox{weakly},\qquad
A_U^2:=\int_{\mathcal N_P(1)}|U(z)|^2e^{2\Phi(-z)}dV(z)<\infty.
\tag{EB13}
\]
Take a smaller compact convex \(K'\) in this ball and \(L=K'+\delta\overline B\) still compact inside it, \(\delta>0\). The actual compact growth of \(\Phi\) gives
\[
e^{-2\Phi(-\xi-i\eta)}|e^{ix\cdot(\xi+i\eta)}|^2
\le C_L\langle\xi\rangle^{-2s}e^{-2\delta|\eta|}
\quad(x\in K').
\tag{EB14}
\]
Indeed \(H_L(-\eta)\ge-x\cdot\eta+\delta|\eta|\); the Fourier reflection and the sign of the exponential are both needed for this inequality.

Cauchy–Schwarz, EB11 and EB14 imply
\[
\sup_{x\in K'}\left|
\int_{\mathcal N_P(1)}U(z)(\gamma\cdot z)^j e^{ix\cdot z}dV(z)\right|
\le C A_U C_2^j
\left(\int_{\mathbb R^n}\langle\xi\rangle^{-2s}d\xi
\int_{\mathbb R^n}(1+|\eta|)^{2\rho j}e^{-2\delta|\eta|}d\eta
\right)^{1/2}.
\tag{EB15}
\]
The real-frequency integral is finite because \(2s>n\). Its decay was supplied by the chosen test weight, so no unproved volume bound on the tube is needed.

For \(q=2\rho j\), calculus bounds
\(\sup_{r\ge0}(1+r)^q e^{-\delta r}\le C_\delta^q(1+q)^q\).
One verifies this by differentiating \(q\log(1+r)-\delta r\); its maximum is at \(r=q/\delta-1\) when this is nonnegative, and at zero otherwise. Keep a remaining factor \(e^{-\delta|\eta|}\), whose integral is finite, to obtain from EB15
\[
\sup_{x\in K'}|( \gamma\cdot D)^j u(x)|
\le C_3^{\,j}j^{\rho j},\qquad j\ge1.
\tag{EB16}
\]
The fixed prefactors, \(A_U\), \(2\rho\) and the remaining exponential integral are absorbed in \(C_3^j\); \(C_3\) is independent of \(j\).

Here is the justification for using the integral pointwise and differentiating it. EB15 at \(j=0\) gives absolute convergence uniformly on each smaller compact, so the weak integral represents a continuous function equal to the given smooth solution. For every finite positive \(j\), the same bound, applied on a slightly larger compact inside the ball, dominates the differentiated kernels along real \(\gamma\)-segments. Dominated convergence differentiates them and yields the directional derivative integral. Thus every estimate in EB16 is an estimate of the actual solution derivatives, rather than of formal kernels.

Cover the original \(K\) by finitely many such smaller convex neighborhoods. Take the largest of their constants, enlarged if necessary to absorb each fixed prefactor for \(j\ge1\). This proves EB16 uniformly on all of \(K\), for an arbitrary open solution neighborhood. It is exactly Theorem11.4.1 derived from15.3.1 and the11.4.8 geometric bridge, solving the second page291 exercise. The zero direction and the nonzero constant-polynomial zero-solution case are immediate endpoints.

## Remaining exercise scope

The two page300 exercises require an actual weak integral for every distribution, and an actual surface representation for every distributional homogeneous solution. Their test orders may vary over a compact exhaustion. They are not consequences of choosing one fixed global moderate weight class. Those full targets, their learner materials, all chapter notes and the rest of the assigned course remain active.

The classical human source is Lars Hörmander, *The Analysis of Linear Partial Differential Operators II*, two unnumbered exercises on printed p.291, with exact cross-references Theorems11.1.7,11.4.1,11.4.8 on printed pp.65,85,90. Approved current-edition source statement pixels were read before comparison; the source's older native-page offsets are not used for this edition. This is original proof exposition and includes no protected book body or page image.
