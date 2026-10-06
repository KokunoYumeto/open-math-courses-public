# The gamma integral and its entire reciprocal

*A modified selection from “Causal kernels, initial data, and short-time geometry”, AN03-U021, prepared by GPT-6 Astra (OpenAI), Ultra reasoning effort, 4 October 2026. The selected proof (W4a)–(W4e) retains its CC0 1.0 licence. The accompanying title page, history, rights and licence remain part of this selection.*

We retain only the complete scalar gamma proof. The wave kernels, polar masses, beta duplication, Fourier transforms and pullbacks in the original lesson are not inputs here. The following preliminary arguments supply every analytic limit used by the selection. The [scalar foundations](metric-foundation-bridges.md), Sections 13.1–13.5 and 13.7–13.9, prove the calculus, complex exponential series, real logarithm and uniform differentiation used here. The [integration foundations](banach-foundation-bridges.md), Sections 15.0–15.4 and 16.1–16.2, prove Lebesgue convergence and affine substitution. [Cauchy kernels and distributional boundary limits](../../src/cauchy-kernels-and-boundary-limits.md), Corollary 2.2, and [Gluing holomorphic sides](../../src/gluing-holomorphic-sides.md), Lemma 3.2, prove the circle power-series and identity results.

## G0. Complex powers and parameter integrals

Write \(E(z)=\sum_{j\ge0}z^j/j!\). The scalar foundation proves its entire differentiability and \(E(z+w)=E(z)E(w)\), \(E(z)E(-z)=1\). Its real coefficients give \(\overline{E(z)}=E(\bar z)\), first on partial sums and then on their limits. Thus \(|E(ib)|^2=E(ib)E(-ib)=1\) for real \(b\), and \(|E(a+ib)|=e^a\). For \(x>0\) and \(z\in\mathbb C\), define \(x^z=E(z\log x)\). The already proved product and chain rules give

\[
 |x^z|=x^{\operatorname{Re}z},\qquad
 \partial_x x^z=zx^{z-1},\qquad
 \partial_z^j x^z=(\log x)^j x^z.
 \tag{G0}
\]

For \(|w|<1\), the series \(\ell(w)=\sum_{j\ge1}(-1)^{j+1}w^j/j\) and each of its fixed derivative series converge uniformly on smaller closed disks, by polynomial times geometric bounds. Passing the fundamental identity along real and imaginary segments proves \(\ell'(w)=1/(1+w)\). The derivative of \(E(\ell(w))/(1+w)\) is zero, so integrating along a straight segment from zero makes this quotient constantly one. Hence \(E(\ell(w))=1+w\). This proves the local logarithm used for the infinite-product tail. It asserts no logarithm across an initial factor's zero.

For \(\sigma>0\) and integer \(j\ge0\), ordinary positive-interval substitution and \(j\) integrations by parts give

\[
 \int_0^1 x^{\sigma-1}|\log x|^j\,dx
 =\int_0^\infty v^j e^{-\sigma v}\,dv
 =\frac{j!}{\sigma^{j+1}}.
 \tag{G1}
\]

Perform substitutions on truncated intervals first, and pass by monotone convergence. Every boundary term at infinity vanishes: choose an integer \(m>j\), and use \(e^{\sigma v/2}\ge(\sigma v/2)^m/m!\). This also supplies an exponential integrable envelope at infinity for every finite real power times every logarithmic power; on \(x\ge1\), use \(\log x\le x\) and increase \(m\). The endpoint zero in each integration by parts is its actual polynomial endpoint, including the final constant integral \(1/\sigma\).

Here is the parameter-differentiation justification used below. If \(H(z,x)=w(x)x^{z+c}\), then for a complex increment \(h\) its difference quotient is

\[
 \frac{H(z+h,x)-H(z,x)}h
 =\int_0^1 w(x)x^{z+th+c}\log x\,dt.
 \tag{G2}
\]

The identity follows by the real fundamental theorem in \(t\). On a small parameter disk, a common integrable envelope for the right side permits dominated convergence as the complex number \(h\to0\). Thus the integral of \(H\) is complex differentiable, with the derivative obtained inside the integral. Repeating with additional \(\log x\) factors proves all derivatives. Formula (G1) gives exactly these envelopes near zero whenever the least exponent is greater than \(-1\). At infinity either the integration is over a compact interval or a factor \(e^{-x}\) gives the preceding exponential envelope. This proves holomorphy of the Euler integral before using its product construction. The same argument proves all Taylor-subtracted power integrals later used in U016.

## The complete earlier gamma proof

The following proof is retained from the earlier programme lesson, with its original formula numbers. In its final sentence, the “normalizations below” and “Section 3” refer to that original lesson; their results are not assumed in this selection.

**Proof.** We first justify the gamma normalization for complex parameters. For \(\operatorname{Re}z>0\), let \(\Gamma(z)=\int_0^\infty e^{-u}u^{z-1}\,du\), using the real logarithm for positive \(u\). For an integer \(N\geq1\), repeated integration by parts in the beta integral gives
\[
 B(z,N+1)=\int_0^1 t^{z-1}(1-t)^N\,dt
 =\frac{N!}{z(z+1)\cdots(z+N)},\qquad
 N^zB(z,N+1)\longrightarrow\Gamma(z).
 \tag{W4a}
\]
For the rational identity, one integration replaces the integral by \(N/z\) times the integral with parameters \(z+1,N\); the final integral is \(1/(z+N)\). No gamma division is used. For the limit put \(u=Nt\). On a compact subset of the right half-plane choose \(0<\sigma\leq\operatorname{Re}z\leq M\). The resulting integrands are bounded in absolute value by \((u^{\sigma-1}+u^{M-1})e^{-u}\), since \((1-u/N)^N\leq e^{-u}\) for \(0<u<N\). Pointwise convergence is uniform for \(z\) in that compact set, and the integrable bound makes the integral convergence locally uniform.

Define \(H_N=\sum_{k=1}^N k^{-1}\). The numbers \(H_N-\log N\) decrease and are bounded below: the decrease follows from \(\log(1+1/N)>1/(N+1)\), and comparison with the integral of \(1/t\) gives the lower bound. Write their limit as \(\gamma\). The exact reciprocal of the scaled beta expression in (W4a) is the entire finite product
\[
 P_N(z)=zN^{-z}\prod_{k=1}^N(1+z/k)
 =z\exp\bigl(z(H_N-\log N)\bigr)
       \prod_{k=1}^N(1+z/k)e^{-z/k}.
 \tag{W4b}
\]
Its limit exists locally uniformly on the whole plane. Indeed, on \(|z|\leq R\) choose an integer \(K>2R\). For \(k>K\), use the logarithm defined by its power series at one; then
\[
 \log(1+z/k)-z/k
 =\sum_{j=2}^{\infty}\frac{(-1)^{j+1}}{j}(z/k)^j,
 \qquad
 \bigl|\log(1+z/k)-z/k\bigr|\leq 2R^2/k^2.
 \tag{W4c}
\]
Thus the sum of these tail logarithms converges uniformly on this disk. The derivative of each tail logarithm is \(-z/[k(k+z)]\), uniformly \(O_R(k^{-2})\); uniform convergence of this derivative series also proves that the tail sum is holomorphic. Exponentiating it, and retaining the first \(K\) factors as polynomials times exponentials, proves local uniform convergence to an entire function
\[
 G(z)=z e^{\gamma z}\prod_{k=1}^{\infty}(1+z/k)e^{-z/k}.
 \tag{W4d}
\]
The exponential of the tail sum never vanishes. Consequently the finite initial factors show that the only zeros are \(0,-1,-2,\ldots\), each simple: near any of these points precisely one polynomial factor has a simple zero and all the others are nonzero. This argument uses logarithms only for the tail factors close to one, including when the disk contains zeros of the full product.

For \(\operatorname{Re}z>0\), the product of \(P_N(z)\) and \(N^zB(z,N+1)\) is exactly one. Passing to the two locally uniform limits gives \(G(z)\Gamma(z)=1\); in particular the gamma integral has no zero there. This identifies \(G\) as the entire reciprocal of the meromorphic continuation of gamma, with the constant fixed by the original integral, rather than only up to a nonzero factor. Explicitly \(P_N(1)=(N+1)/N\), so \(G(1)=1\). Integration by parts in the gamma integral gives \(\Gamma(z+1)=z\Gamma(z)\) in the right half-plane. It follows that \(G(z)=zG(z+1)\) there, hence everywhere by the identity theorem. Iterating at \(z=-m\), for an integer \(m\geq0\), gives
\[
 G'(-m)=(-1)^m m!,\qquad
 \operatorname*{Res}_{z=-m}\Gamma(z)=\frac{(-1)^m}{m!}.
 \tag{W4e}
\]
For this derivative, differentiate \(G(z)=z(z+1)\cdots(z+m)G(z+m+1)\) at \(-m\) and use \(G(1)=1\); its reciprocal has the stated residue. These facts justify both complex gamma normalizations below and the pole cancellation in Section 3.

## Consequences and exact proof scope

The elementary comparisons used in the selected proof follow directly from the supplied calculus. On \(0<v<1\), integrating \(1/(1-t)\ge1\) from zero to \(v\) gives \(\log(1-v)\le-v\). Integrating \(1/t>1/(N+1)\) on \([N,N+1]\) gives \(\log(1+1/N)>1/(N+1)\). On each \([k,k+1]\), \(1/t\le1/k\), so \(H_N\ge\log(N+1)>\log N\). Thus the harmonic-log sequence decreases and is bounded below, proving its stated limit by completeness. Finally, for \(k\ge2\), \(k^{-2}\le[k(k-1)]^{-1}=1/(k-1)-1/k\). Its telescoping tail proves convergence of the logarithm and derivative majorants in (W4c).

For clarity, the limit in (W4a) is uniform on each compact parameter set because its error is bounded by the integral of

\[
 (u^{\sigma-1}+u^{M-1})\left|\boldsymbol1_{(0,N)}(u)(1-u/N)^N-e^{-u}\right|.
\]

The first term inside the absolute value is defined as zero for \(u\ge N\). The integral tends to zero by the displayed integrable envelope and pointwise convergence. The latter follows from \(\ell(-u/N)=-u/N+O_u(N^{-2})\) at fixed \(u\), whose error follows from G0. The logarithm at positive real arguments agrees with the earlier real logarithm: both have derivative \(1/x\) and value zero at one. For each compact disk, the sum in (W4c) and its first derivative converge uniformly. The coordinate fundamental identity makes their limit complex differentiable. Exponentiation and finite initial factors therefore produce an entire \(G\), including at those factors' zeros. An inverse exists locally away from the zeros by the quotient rule. At a simple zero, factor its convergent power series as \((z-z_0)h(z)\), \(h(z_0)\ne0\); the quotient \(1/h\) has a convergent series by the circle theorem. This proves the meromorphic assertion and the residue used in (W4e).

The identity theorem here is the complete one-variable result in the supplied gluing lesson. A locally uniform limit theorem for arbitrary holomorphic functions is not required: the differentiated logarithm series and fundamental identity prove holomorphy directly. The scalar beta integral with integer second parameter is proved by the displayed integrations; no general beta identity or multidimensional change of variables is an input.

## Sources and licence

- NIST, [DLMF 5.2, Gamma definition and Euler constant](https://dlmf.nist.gov/5.2), [5.5.1, recurrence](https://dlmf.nist.gov/5.5.E1), and [5.8.2, reciprocal product](https://dlmf.nist.gov/5.8.E2), provide freely accessible formula comparisons. The full proof required here is supplied above. No text from their cited books is used or included.
- *Causal kernels, initial data, and short-time geometry*, AN03-U021, complete scalar proof (W4a)–(W4e), exact source version 00536d84a8ffc35c4a7055b081ef1193ea222cac51c65a916e6940553bddbd30, original lines 51–89. This selection supplies its complete relevant proof locally.

This independently written programme selection is dedicated under CC0 1.0 Universal, to the extent rights are held. The original [title page](notices/TITLE_PAGE.md), [history](notices/HISTORY.md), [rights notice](notices/U016_ORIGINAL_RIGHTS.md), [selection history](notices/U016_SELECTION_HISTORY.md) and full [licence](https://creativecommons.org/publicdomain/zero/1.0/) accompany it. The additional preliminary and closure arguments in this modified selection are distributed under the same licence.
