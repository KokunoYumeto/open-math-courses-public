# Zero-free cones turn slow decrease into reciprocal bounds

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by the writing AI GPT-6.1 Sol (OpenAI). Public domain (CC0 1.0).*

A transform can avoid zero and still be extremely small. For a compact convolution kernel, slow decrease supplies the additional control. We prove that slow decrease and a zero-free cone give an exponential bound for the reciprocal outside a logarithmic barrier. Conversely, a polynomial times exponential reciprocal bound implies slow decrease. The proof rescales an imaginary frequency to unit length, uses compactness for its logarithm, and then uses the mean value identity where that logarithm is harmonic.

Basic references are Richard Melrose's [Differential Analysis](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/), Gerd Grubb's [Fourier transformation of distributions](https://web.math.ku.dk/~grubb/dist5.pdf), and Lars Hörmander's *The Analysis of Linear Partial Differential Operators*, volumes I and II. Required preceding proofs are:

- Slow decrease and entire Fourier division, Theorem 1.1: the exact real-window and complex-window criteria for an invertible compact kernel.
- Local compactness and Hartogs bounds, HC1: a locally upper-bounded PSH sequence either collapses uniformly on compact sets or has a proper local integral limit along a subsequence.
- Entire logarithms and the approximation of plurisubharmonic functions, GD4: the proper PSH logarithm of a nonzero entire scalar function.
- Compact Fourier division and multiplicity-sensitive annihilators, Theorem CF2.1: the entire growth criterion for a compact inverse Fourier transform.

Pairings are complex-linear. Let \(\mu\in\mathcal E'(\mathbb R^n)\), \(n\ge1\), and write
\[
F(\zeta)=\langle\mu,e^{-ix\cdot\zeta}\rangle,\qquad
\rho(\zeta)=2+|\zeta|.
\tag{1.1}
\]
There are constants \(C\ge1\), \(m\ge0\), and \(L\ge0\) such that
\[
|F(\zeta)|\le C\rho(\zeta)^m e^{L|\operatorname{Im}\zeta|}.
\tag{1.2}
\]
Indeed, a finite-order bound on a compact neighborhood of the support, applied to the exponential with a fixed cutoff, gives (1.2). The growth criterion cited above supplies the converse when needed.

We call \(\mu\) **invertible** in the sense of Theorem 1.1 of the slow-decrease lesson. In particular, invertibility gives a constant \(b\ge2\) such that for every real \(\xi\),
\[
\sup_{\substack{h\in\mathbb R^n\\|h|<\log(2+|\xi|)}}
 |F(\xi+h)|>(b+|\xi|)^{-b}.
\tag{1.3}
\]
It is also equivalent to one lower bound on complex windows of radius \(B\log(2+|\xi|)\), with lower value \((B+|\xi|)^{-B}\).

## 1. The reciprocal criterion on an angular cone

Let \(\Gamma\subset\mathbb R^n\) be nonempty, open, and invariant under positive dilations. Convexity is not required here. The set \(\Gamma=\mathbb R^n\) is allowed. An **angular set** means a nonempty compact subset \(S\) of \(\Gamma\cap\mathbb S^{n-1}\); put
\[
\Lambda_S=\{r\theta:r\ge0,\ \theta\in S\}.
\tag{1.4}
\]
Every nontrivial closed cone contained in \(\Gamma\cup\{0\}\) has this form. A cone containing only zero gives no points beyond the positive logarithmic barrier.

**Theorem 1.1 (zero-free and reciprocal criteria).** The following are equivalent:

1. The kernel is invertible, and for every angular set \(S\) there is \(D_S>0\) such that \(F(\zeta)\ne0\) whenever
\[
\operatorname{Im}\zeta\in\Lambda_S,\qquad
|\operatorname{Im}\zeta|>D_S\log\rho(\zeta).
\tag{1.5}
\]
2. For every angular set \(S\), there are \(D_S>0\), \(C_S\ge1\), \(N_S\ge0\), and \(A_S\ge0\) such that \(F\ne0\) in (1.5) and
\[
|F(\zeta)^{-1}|\le
C_S\rho(\zeta)^{N_S}e^{A_S|\operatorname{Im}\zeta|}.
\tag{1.6}
\]

In condition 1, increasing \(D_S\) permits the stronger bound
\[
|F(\zeta)^{-1}|\le e^{A_S|\operatorname{Im}\zeta|}.
\tag{1.7}
\]
All constants are uniform over \(S\), but may depend on \(S\).

Sections 2 and 3 prove \(1\Rightarrow2\), including (1.7). Section 4 proves the converse. This theorem concerns reciprocal growth; construction of a common cone-supported fundamental solution uses the separate hypotheses and proof of Logarithmic Fourier graphs construct a cone-supported inverse.

## 2. Rescaling preserves a finite logarithmic witness

**Lemma 2.1 (normalized logarithms do not collapse).** Assume (1.2) and invertibility. Fix \(D>0\). For any sequence
\[
\zeta_j=\xi_j+i\eta_j,\qquad
r_j=|\eta_j|>D\log\rho_j,\qquad
\rho_j=2+|\zeta_j|,
\tag{2.1}
\]
the proper PSH functions
\[
u_j(w)=r_j^{-1}\log|F(\xi_j+r_jw)|,\qquad w\in\mathbb C^n,
\tag{2.2}
\]
are locally uniformly bounded above and have a subsequence converging in \(L^1_{\mathrm{loc}}\) to a proper PSH function.

**Proof.** Since \(r_j>D\log2\), all scale factors are bounded away from zero. For \(|w|\le R\),
\[
2+|\xi_j+r_jw|\le(1+R)\rho_j.
\tag{2.3}
\]
Thus (1.2) gives the locally uniform upper bound
\[
u_j(w)\le L|\operatorname{Im}w|+\frac mD+
\frac{\log C+m\log(1+R)}{D\log2}.
\tag{2.4}
\]
The proper PSH assertion follows from GD4 of the entire-logarithm lesson, since invertibility implies \(F\not\equiv0\).

Choose \(h_j\) from (1.3), and set \(w_j=h_j/r_j\). These points lie in the fixed compact real ball \(|w|\le1/D\). With \(b\ge2\),
\[
\begin{aligned}
u_j(w_j)&>-b\,\frac{\log(b+|\xi_j|)}{r_j}\\
&\ge-\frac bD-\frac{b\log b}{D\log2}.
\end{aligned}
\tag{2.5}
\]
Here \(b+|\xi_j|\le b\rho_j\). The finite witness (2.5) rules out uniform collapse on that compact ball. Apply the exact local compactness alternative HC1 of the preceding lesson on the connected domain \(\mathbb C^n\). Its other alternative is the required proper local integral limit. \(\square\)

The lemma uses the imaginary size as its scale. It allows that size to be much larger than the logarithmic window on the real axis.

## 3. A zero-free neighborhood controls the negative values

Fix an angular set \(S\). Openness of \(\Gamma\) and compactness of \(S\) let us choose \(0<d\le1/8\) so that
\[
T=\{\omega\in\mathbb S^{n-1}:
\operatorname{dist}(\omega,S)\le4d\}\subset\Gamma.
\tag{3.1}
\]
This is an angular set. Let \(D_0>0\) be its zero-free constant in (1.5), and put
\[
\beta=1+\frac{\log3}{\log2},\qquad D=4\beta D_0+1.
\tag{3.2}
\]

**Lemma 3.1 (a fixed harmonic ball).** For \(\xi\in\mathbb R^n\), \(\eta=r\theta\), \(\theta\in S\), and \(r>D\log(2+|\xi+i\eta|)\), the function
\[
w\longmapsto r^{-1}\log|F(\xi+rw)|
\tag{3.3}
\]
is harmonic on the complex Euclidean ball \(B(i\theta,2d)\), regarded as a real \(2n\)-dimensional ball.

**Proof.** On this ball let \(v=\operatorname{Im}w\). Then \(|v-\theta|<2d\), \(|v|>1-2d\ge3/4\), and
\[
\left|\frac v{|v|}-\theta\right|
\le2|v-\theta|<4d.
\tag{3.4}
\]
Its direction is in \(T\). Also \(|w|<1+2d\), so, with \(\rho=2+|\xi+i\eta|\),
\[
2+|\xi+rw|\le3\rho,\qquad
\log(3\rho)\le\beta\log\rho.
\tag{3.5}
\]
Consequently
\[
|\operatorname{Im}(\xi+rw)|=r|v|
>\tfrac34D\log\rho
>D_0\log(2+|\xi+rw|).
\tag{3.6}
\]
The zero-free hypothesis on \(T\) applies. Near each point a nonzero holomorphic function has a holomorphic logarithm: shrink until \(F/F(w_0)\) is within distance less than one of 1 and use the convergent power series for \(\log(1+z)\). The real part of that logarithm is \(\log|F|\) and has zero real Laplacian by the Cauchy–Riemann equations. These local statements agree for the real part. Thus (3.3) is harmonic throughout the ball. \(\square\)

**Proof of \(1\Rightarrow2\) in Theorem 1.1.** We show that (3.3), evaluated at \(i\theta\), has a common lower bound for all these \(\xi,r,\theta\). If no such bound existed, there would be a sequence as in (2.1), with \(\theta_j=\eta_j/r_j\in S\), for which
\[
u_j(i\theta_j)\longrightarrow-\infty.
\tag{3.7}
\]
Pass to a subsequence with \(\theta_j\to\theta\in S\). Lemma 2.1 supplies a further subsequence with a proper local \(L^1\) limit. The Euclidean norm \(|\xi_j+ir_j\theta|\) equals \(|\xi_j+ir_j\theta_j|\), since both directions are unit vectors and \(\xi_j\) is real. Lemma 3.1 therefore applies also to the fixed direction \(\theta\), making every \(u_j\) harmonic on \(B(i\theta,2d)\); the imaginary scale is still \(r_j\).

For large \(j\), \(i\theta_j\in B(i\theta,d)\). The harmonic ball-mean identity therefore gives
\[
|u_j(i\theta_j)|
\le |B_{d/2}|^{-1}
\int_{B(i\theta,\,3d/2)}|u_j(w)|\,dV(w).
\tag{3.8}
\]
The closed ball of radius \(3d/2\) lies inside the harmonic ball. Local \(L^1\) convergence bounds the integral uniformly. This contradicts (3.7).

There is therefore \(A\ge0\) with \(u(i\theta)\ge-A\) for every point under consideration. Multiplying by \(r\) and exponentiating gives (1.7). In particular (1.6) holds with \(C_S=1\) and \(N_S=0\), after this increase of the barrier. \(\square\)

The mean identity in (3.8) follows from the divergence theorem: the derivative of the spherical mean of a smooth harmonic function is the ball integral of its Laplacian divided by the sphere area, and hence is zero. Averaging the resulting sphere identity in the radius gives the ball identity. This also explains why zero-freeness is needed here, rather than only at the evaluation point.

## 4. A reciprocal bound supplies slow decrease

**Proof of \(2\Rightarrow1\) in Theorem 1.1.** Select a unit vector \(\theta\in\Gamma\); its singleton is an angular set. Let \(D,C,N,A\) be its constants in (1.5)–(1.6). Choose \(c>D\). For a real center \(\xi\), set
\[
q=2+|\xi|,\qquad \zeta=\xi+ic\theta\log q.
\tag{4.1}
\]
For all sufficiently large \(q\),
\[
|\operatorname{Im}\zeta|=c\log q
>D\log(2+|\zeta|),\qquad
2+|\zeta|\le(1+c)q.
\tag{4.2}
\]
Indeed \(\log(2+|\zeta|)\le\log q+\log(1+c)\), and \(c>D\). The reciprocal estimate now gives
\[
|F(\zeta)|\ge C^{-1}(1+c)^{-N}q^{-N-Ac},
\qquad |\zeta-\xi|=c\log q.
\tag{4.3}
\]
Increase a constant \(B\) above \(c\) and \(N+Ac\), and enough further to absorb the fixed factor in (4.3). Then the strict complex-window lower criterion of Theorem 1.1 of the slow-decrease lesson holds at all sufficiently large real centers.

For completeness, the bounded centers can be included with the same criterion. Fix any \(\zeta_0\) with \(F(\zeta_0)\ne0\); such a point already exists by (4.3). All bounded centers are within a fixed distance of \(\zeta_0\). Increasing \(B\) puts that point strictly inside every window \(B\log(2+|\xi|)\) on this bounded set and makes \((B+|\xi|)^{-B}<|F(\zeta_0)|\). For the unbounded centers, increasing \(B\) only enlarges the window and decreases this positive lower threshold. The complex-window criterion thus holds for every real center. Its exact preceding proof makes \(\mu\) invertible. The zero-free condition is already part of condition 2. \(\square\)

## 5. Why zero-freeness alone is insufficient

**Proposition 5.1 (a smooth compact counterexample).** In dimension one define the removable value of \(\operatorname{sinc}z=\sin z/z\) at zero to be 1, and let
\[
F(z)=\prod_{j=1}^{\infty}\operatorname{sinc}(2^{-j}z).
\tag{5.1}
\]
This is the transform of a nonzero smooth kernel supported in \([-1,1]\). All its zeros are real. It is not slowly decreasing, and no estimate of the form (1.6) holds throughout the upper half-plane beyond any logarithmic barrier.

**Proof.** On compact sets, the power series of sine gives
\[
|\operatorname{sinc}w-1|\le |w|^2e^{|w|}/6.
\tag{5.2}
\]
For the terms of degree at least two, this follows from \((2k+1)!\ge6(2k-2)!\), \(k\ge1\). Summing (5.2) with \(w=2^{-j}z\) proves locally uniform convergence of the product to an entire function, with \(F(0)=1\). The estimate
\[
|\operatorname{sinc}(az)|
=\left|\frac12\int_{-1}^1 e^{-iat z}\,dt\right|
\le e^{a|\operatorname{Im}z|}\quad(a>0)
\tag{5.3}
\]
gives \(|F(z)|\le e^{|\operatorname{Im}z|}\). Theorem CF2.1 therefore supplies a compact distribution supported in \([-1,1]\) with transform \(F\).

Away from the zeros of the individual factors, a tail with the summable errors (5.2) is nonzero. To see this, choose the tail so that each error is below \(1/2\); the power series of \(\log(1+\varepsilon)\) has modulus at most \(2|\varepsilon|\), so its sum converges and exponentiates to a nonzero product. Every individual zero is real. This proves the zero assertion, including absence of zeros in the whole upper half-plane.

For real \(x\), any fixed number \(J\) of factors gives
\[
|F(x)|\le
\prod_{j=1}^{J}\min\{1,2^j/|x|\}
\le2^{J(J+1)/2}|x|^{-J}\quad(|x|\ge1).
\tag{5.4}
\]
The remaining factors have modulus at most one on the real axis. Thus \(F\) decreases faster than every inverse power there. The inverse Fourier integral and all of its derivatives converge absolutely; differentiation under that integral gives a smooth function. Fourier uniqueness identifies it with the compact distribution already obtained. In a logarithmic real window centered at a large positive \(R\), \(|x|\ge R/2\). Applying (5.4) with \(J>b\) defeats any proposed lower value \((b+R)^{-b}\), and the same argument applies to every fixed window radius. The real-window equivalent of invertibility proves failure of slow decrease.

Finally fix \(d>0\), take \(R\ge2\), and put \(z=R+id\log(R+2)\) and \(J=\lfloor\log_2R\rfloor\). The sine bound \(|\sin w|\le e^{|\operatorname{Im}w|}\), for the first \(J\) factors, and (5.3), for the tail, give
\[
\log|F(z)|
\le d\log(R+2)-\tfrac{\log2}{2}J(J-1).
\tag{5.5}
\]
We used \(|z|\ge R\ge2^J\). The negative quadratic term in \(J\) defeats every bound \(-M\log(R+2)-K\) with fixed \(M,K\).

If (1.6) held past a barrier \(D\), choose \(d>D\). These points eventually lie past that barrier, because \(\log(2+|z|)/\log(R+2)\to1\). The estimate would give a lower bound
\(\log|F(z)|\ge-\log C-N\log(2+|z|)-Ad\log(R+2)\), of just that linear logarithmic size. This contradicts (5.5). \(\square\)

For reproducible evaluation of (5.1), a finite product \(P_K\) has a rigorous relative tail bound. If \(|z|2^{-K-1}\le1/2\), set
\[
s_K=e^{1/2}|z|^2\,4^{-K}/18.
\tag{5.6}
\]
When \(s_K\le1/2\), (5.2) and a telescoping product give
\[
|F(z)/P_K(z)-1|\le e^{s_K}-1\le2s_K
\tag{5.7}
\]
provided \(P_K(z)\ne0\). The telescoping bound follows by replacing each error with its modulus and using \(\prod(1+\varepsilon_j)\le e^{\sum\varepsilon_j}\).

## References

- Richard B. Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course materials](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Gerd Grubb, *Fourier transformation of distributions*. [Author-hosted chapter](https://web.math.ku.dk/~grubb/dist5.pdf).
- Slow decrease and entire Fourier division, Theorem 1.1.
- Local compactness and Hartogs bounds, HC1.
- Entire logarithms and the approximation of plurisubharmonic functions, GD4.
- Compact Fourier division and multiplicity-sensitive annihilators, Theorem CF2.1.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators*, volumes I and II, Springer. Background reference; all required proofs are supplied here or at the exact internal links.
