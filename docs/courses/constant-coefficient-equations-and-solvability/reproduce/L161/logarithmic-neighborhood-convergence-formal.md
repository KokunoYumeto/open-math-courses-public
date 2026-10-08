# Changing centers in logarithmic Fourier windows

Original exposition and proofs: GPT-6.1 Sol (OpenAI), Ultra. CC0 1.0. Self-checked by the writing AI; independent mathematical review is not claimed.

Moving a real Fourier center by a bounded multiple of its logarithm translates the limiting profile in a real direction. Its indicator does not change. More widely, a profile controls a suitable union of growing logarithmic neighborhoods around the original centers. We prove both facts, including collapsed profiles and a uniform comparison that permits the complex parameter to move.

Basic references are Tao's *246B, Notes 2*, Hörmander's *The Analysis of Linear Partial Differential Operators I*, and its second volume. The precise earlier inputs are Joint logarithmic-frequency limits, Theorem 2.1; Local compactness and Hartogs bounds; and Plurisubharmonic envelopes and support functions. These provide profile compactness, canonical uniqueness, continuous Hartogs ceilings, and the indicator increment bound.

## 1. The exact change of parameters

For a compact distribution on \(\mathbb R^n\), use

\[
 F(\zeta)=\langle u(x),e^{-ix\cdot\zeta}\rangle,\qquad
 L_u(z,c)=\frac{\log|F(c+z\log|c|)|}{\log|c|},
 \quad c\in\mathbb R^n,\quad |c|>2. \tag{1.1}
\]

Logarithms at transform zeros have value \(-\infty\). A proper profile means a canonical PSH local \(L^1\) limit. A collapsed profile means convergence to \(-\infty\) uniformly on every compact parameter set. A proper profile has a finite continuous support function \(h\); a collapsed profile has \(h\equiv-\infty\).

Fix two real centers \(c,d\), both of norm greater than two. Put

\[
 Q=|c|,\quad \ell=\log Q,\quad
 a=\frac{d-c}{\ell},\quad
 \kappa=\frac{\log|d|}{\ell}>0,\quad
 T(z)=a+\kappa z. \tag{1.2}
\]

Thus \(a\in\mathbb R^n\), and \(T:\mathbb C^n\to\mathbb C^n\) is an invertible complex affine map.

**Lemma 1.1 (no asymptotic replacement in the identity).**

\[
 L_u(z,d)=\kappa^{-1}L_u(T(z),c),\qquad
 \operatorname{Im}T(z)=\kappa\operatorname{Im}z. \tag{1.3}
\]

*Proof.* The entire Fourier argument on the right is
\(c+(a+\kappa z)\ell=d+z\log|d|\), exactly. Dividing its logarithmic modulus by the two different logarithms gives the first equality. Both \(c,d\) are real, so \(a\) is real and contributes no imaginary part. The identities hold at zeros with the extended convention as well. \(\square\)

**Lemma 1.2 (uniform logarithmic-ratio control).** If \(Q>e\) and
\(|d-c|\leq\delta Q\), with \(0\leq\delta\leq1/4\), then

\[
 \frac12\leq\kappa\leq\frac32,\qquad
 |\kappa-1|\leq\frac{2\delta}{\log Q},\qquad
 |\kappa^{-1}-1|\leq\frac{4\delta}{\log Q}. \tag{1.4}
\]

*Proof.* The triangle inequality gives
\(1-\delta\leq |d|/Q\leq1+\delta\).
For \(0\leq\delta\leq1/4\), integration of \(1/(1-t)\) gives
\(-\log(1-\delta)\leq\delta/(1-\delta)\leq2\delta\);
also \(\log(1+\delta)\leq\delta\).
Consequently
\(|\log|d|-\log Q|\leq2\delta\).
Divide by \(\log Q>1\). The resulting error is at most \(1/2\), proving the bounds for \(\kappa\). Finally
\(|\kappa^{-1}-1|=|\kappa-1|/\kappa\leq2|\kappa-1|\).
All these bounds are uniform over the indicated real neighborhood. \(\square\)

## 2. Bounded logarithmic shifts translate proper profiles

**Lemma 2.1 (affine pullbacks of PSH limits).** Suppose proper PSH functions \(f_j\) are locally uniformly bounded above on \(\mathbb C^n\) and converge to a proper PSH function \(v\) in local \(L^1\). Let \(a_j\to a\) in \(\mathbb R^n\), and \(\kappa_j\to1\) be positive. Then

\[
 \kappa_j^{-1}f_j(a_j+\kappa_j z)
 \longrightarrow v(z+a)\quad\text{in local }L^1. \tag{2.1}
\]

*Proof.* The affine pullbacks are proper PSH functions. Every compact observation region has its affine images inside one fixed compact region for large \(j\). Positivity and boundedness of \(\kappa_j^{-1}\), together with the upper bound for \(f_j\), give local uniform upper bounds for the pullbacks.

For a smooth compactly supported test function \(\phi\) on \(\mathbb C^n\), use real volume in dimension \(2n\). The exact change of variables \(w=a_j+\kappa_j z\) gives

\[
 \begin{split}
 &\int_{\mathbb C^n}\kappa_j^{-1}f_j(a_j+\kappa_j z)\phi(z)\,dV(z)\\
 &\quad=\kappa_j^{-1-2n}
       \int_{\mathbb C^n}f_j(w)\phi((w-a_j)/\kappa_j)\,dV(w)
 \longrightarrow
       \int_{\mathbb C^n}v(w)\phi(w-a)\,dV(w).
 \end{split} \tag{2.2}
\]

Here is the full justification with moving tests. The transformed tests have a common compact support and converge uniformly there to \(\phi(w-a)\); the same holds for every derivative. The local \(L^1\) norms of \(f_j\) on that support are bounded because \(f_j\to v\) in \(L^1\). The integral against the difference of the tests is therefore bounded by that \(L^1\) bound times a supremum tending to zero. The remaining difference against the fixed limiting test tends to zero by \(L^1\) convergence. The scalar factor tends to one. This proves (2.2) without assuming strong continuity of affine pullbacks on arbitrary locally integrable functions.

Apply PSH compactness to any subsequence of the pullbacks. Uniform local collapse would make the pairing with a nonnegative test of positive integral tend to \(-\infty\), contrary to the finite limit in (2.2). A proper further local \(L^1\) limit must equal \(v(z+a)\) as a distribution, hence almost everywhere, and then everywhere as the canonical PSH representative. If convergence to that limit failed in an \(L^1\) norm on a compact set, select a subsequence whose norm-distance is bounded below by a positive number; compactness gives a further subsequence with precisely that limit, a contradiction. Thus the entire sequence converges in local \(L^1\). \(\square\)

**Theorem 2.2 (logarithmic-center translation).** Let \(|c_j|\to\infty\), and suppose \(L_u(\cdot,c_j)\) has a proper or collapsed profile \(v\). If real \(d_j\) satisfy

\[
 |d_j-c_j|\leq A\log|c_j|\quad\text{for a fixed }A,\qquad
 a_j=\frac{d_j-c_j}{\log|c_j|}, \tag{2.3}
\]

then:

- If \(v\) is proper and \(a_j\to a\), the new profiles converge in local \(L^1\) to \(v(z+a)\).
- If \(v\) is proper and \(a_j\) is only bounded, every limiting profile of the new sequence is a real translate of \(v\), corresponding to a cluster point of \(a_j\). Every such cluster point gives that translate on its subsequence. No new collapsed limit occurs.
- If \(v\) is collapsed, the new sequence collapses uniformly locally, whether or not \(a_j\) converges.

*Proof.* Set \(Q_j=|c_j|\). The relative displacement is bounded by
\(\delta_j=A\log Q_j/Q_j\to0\).
Lemma 1.2 gives \(\kappa_j=\log|d_j|/\log Q_j\to1\), and \(d_j\) still escapes. Lemma 1.1 and Lemma 2.1 give the first assertion.

For bounded \(a_j\), every subsequence has a further subsequence on which \(a_j\to a\). Apply the first assertion. A proposed proper or collapsed limiting profile of the full subsequence is unchanged by this further extraction, so it must be the asserted proper translate. Conversely, extract a subsequence for each cluster point \(a\); the first assertion gives its translate. This proves the second assertion without claiming convergence when the translates differ.

In the collapsed case, the images \(a_j+\kappa_j B\) of a fixed compact set \(B\) lie inside a fixed compact set \(B'\). For every \(M>0\), the old normalized logarithms are eventually at most \(-M\) on \(B'\). Since \(\kappa_j^{-1}\geq1/2\) for large \(j\), their pullbacks are at most \(-M/2\). The arbitrary choice of \(M\) proves uniform collapse. \(\square\)

**Corollary 2.3 (indicators do not see the real translation).** All proper profiles in Theorem 2.2 have the same indicator and compact convex carrier as \(v\).

*Proof.* For a real vector \(a\), the imaginary-height envelope satisfies

\[
 \sup_{x\in\mathbb R^n}v(x+a+i\eta)
 =\sup_{x\in\mathbb R^n}v(x+i\eta). \tag{2.4}
\]

The real translation permutes the whole real space. Thus the envelopes and their recession support functions coincide. Compact convex carrier uniqueness gives the same carrier. In the collapsed case both indicators are \(-\infty\) and both carriers are empty. \(\square\)

## 3. One profile controls expanding logarithmic neighborhoods

Choose an integer \(N\geq0\) which is an ordinary compact Fourier growth order for \(u\). For a proper normalized profile, the earlier increment theorem gives

\[
 v(z)\leq N+h(\operatorname{Im}z). \tag{3.1}
\]

This exact inequality follows from the real-axis ceiling \(v\leq N\) and the indicator increment bound in Plurisubharmonic envelopes and support functions. It also occurs in Joint logarithmic-frequency limits, Theorem 2.1. The support function \(h\) is finite, continuous and positively homogeneous; it is allowed to have negative values.

**Theorem 3.1 (uniform expanding-neighborhood bound).** Suppose
\(L_u(\cdot,c_j)\to v\) properly in local \(L^1\), or by uniform local collapse. There are positive numbers \(r_j\to\infty\) with

\[
 \frac{r_j\log|c_j|}{|c_j|}\longrightarrow0 \tag{3.2}
\]

such that, for

\[
 E=\bigcup_j
 \{d\in\mathbb R^n:|d-c_j|<r_j\log|c_j|\}, \tag{3.3}
\]

the following holds. In the proper case, every compact \(B\subset\mathbb C^n\) and every \(\varepsilon>0\) have a threshold \(T\) for which

\[
 L_u(z,d)\leq N+h(\operatorname{Im}z)+\varepsilon
 \quad(z\in B,\ d\in E,\ |d|>T). \tag{3.4}
\]

In particular,

\[
 \limsup_{\substack{d\in E,\ |d|\to\infty\\w\to z}}
 L_u(w,d)\leq N+h(\operatorname{Im}z). \tag{3.5}
\]

In the collapsed case, \(L_u(\cdot,d)\to-\infty\) uniformly on every compact set as \(d\in E\) escapes. Formula (3.5) then has right side \(-\infty\). The conclusion therefore includes the regularized upper limit, not only the value at a fixed parameter point.

The constant \(N\) in (3.4) is an available real Fourier growth order. The existence of a finite constant is enough for the neighborhood statement; the shrinking-error diagonal below retains \(N\) itself.

**Lemma 3.2 (a quantified diagonal).** In the proper case one can choose integers \(s_j\to\infty\) such that, for all large \(j\),

\[
 L_u(w,c_j)\leq N+h(\operatorname{Im}w)+1/s_j
 \quad(|w|\leq2s_j). \tag{3.6}
\]

In the collapsed case one can instead choose such integers with

\[
 L_u(w,c_j)\leq-s_j\quad(|w|\leq2s_j). \tag{3.7}
\]

*Proof.* For each fixed positive integer \(k\), Hartogs comparison against the continuous ceiling in (3.1), on the closed ball of radius \(2k\) inside a slightly larger ball, gives a threshold \(J_k\) such that
\(L_u\leq N+h+1/k\) there for all \(j\geq J_k\).
For collapse, uniform convergence on that ball gives the analogous bound \(-k\).
Increase the thresholds so that \(J_k\geq k\) and they are strictly increasing. For \(j\geq J_1\), define

\[
 s_j=\max\{k\leq j:J_k\leq j\}. \tag{3.8}
\]

This finite set is nonempty. For every fixed \(k\), all \(j\geq J_k\) have \(s_j\geq k\), so \(s_j\to\infty\). The chosen maximum itself satisfies \(J_{s_j}\leq j\), giving (3.6) or (3.7) with \(k=s_j\). Assign any positive integer to the finitely many earlier indices. \(\square\)

*Proof of Theorem 3.1.* Write \(Q_j=|c_j|\), and ignore a finite prefix until \(Q_j>e\). It can be added back with arbitrary finite positive radii, because finitely many bounded frequency neighborhoods do not affect the limit at infinity. For the remaining indices use Lemma 3.2 and put

\[
 r_j=\min\left\{
 s_j,\sqrt{\frac{Q_j}{\log Q_j}},
 \frac{Q_j}{4\log Q_j}
 \right\}. \tag{3.9}
\]

Each of these three positive quantities tends to infinity, so \(r_j\to\infty\).
If \(d\) is in its \(j\)-th neighborhood, set
\[
 a_{j,d}=\frac{d-c_j}{\log Q_j},\qquad
 \kappa_{j,d}=\frac{\log|d|}{\log Q_j},\qquad
 \delta_j=\frac{r_j\log Q_j}{Q_j}.
 \tag{3.10}
\]
The cap in (3.9) gives \(\delta_j\leq1/4\), and the square-root bound gives
\(\delta_j\leq\sqrt{\log Q_j/Q_j}\to0\).
This proves (3.2), and ensures \(|d|\geq3Q_j/4\) in the tail. Lemma 1.2 gives uniformly throughout the neighborhood

\[
 \frac12\leq\kappa_{j,d}\leq\frac32,\qquad
 |\kappa_{j,d}^{-1}-1|\leq4r_j/Q_j\longrightarrow0. \tag{3.11}
\]

Let \(B\) lie in a ball \(|z|\leq M\). For large \(j\), \(r_j\geq3M\), so the parameter in Lemma 1.1 satisfies

\[
 |a_{j,d}+\kappa_{j,d}z|
 \leq r_j+\tfrac32M
 \leq\tfrac32r_j\leq2s_j
 \quad(z\in B). \tag{3.12}
\]

In the proper case, apply (3.6) at this entire parameter and then (1.3). Positive homogeneity cancels the logarithmic ratio in the support term exactly:

\[
 \begin{split}
 L_u(z,d)
 &\leq\kappa_{j,d}^{-1}(N+1/s_j)
       +\kappa_{j,d}^{-1}h(\kappa_{j,d}\operatorname{Im}z)\\
 &=\kappa_{j,d}^{-1}(N+1/s_j)+h(\operatorname{Im}z)\\
 &\leq N+h(\operatorname{Im}z)+4Nr_j/Q_j+2/s_j.
 \end{split} \tag{3.13}
\]

The last error tends to zero. This exact cancellation remains valid for negative support values; no sign-dependent approximation of \(h\) has been used.

In the collapsed case, (3.7), (3.12) and (1.3) give
\[
 L_u(z,d)\leq-\kappa_{j,d}^{-1}s_j\leq-s_j/2
 \quad(z\in B), \tag{3.14}
\]
which tends uniformly to \(-\infty\).

It remains to pass from individual neighborhoods to their union with the correct quantifiers. For any fixed \(J\), the union of the first \(J\) frequency neighborhoods is bounded: each has a finite center and finite radius. Therefore, as \(d\in E\) tends to infinity, every index witnessing its membership eventually exceeds \(J\). Choose \(J\) so that (3.12) holds and the error in (3.13) is below the prescribed \(\varepsilon\) for all \(j>J\). Then choose \(T\) exceeding the norms of the first \(J\) neighborhoods. This proves (3.4). The same argument with the bound \(-s_j/2\) proves uniform collapse throughout the union.

Finally, for \(w\to z\), place these parameter points in one compact neighborhood and use the continuous support function in (3.4). First let the escaping frequency and parameter approach their limits, and then let \(\varepsilon\downarrow0\). This proves (3.5), including moving parameter points. \(\square\)

**Corollary 3.3 (one neighborhood union for a finite joint profile tuple).** For finitely many compact distributions whose profiles converge properly or collapse on the same \(c_j\), the radii in Theorem 3.1 can be chosen in common. Each proper coordinate has its own order \(N_i\) and indicator \(h_i\); collapsed coordinates collapse uniformly throughout the common union.

*Proof.* For each fixed \(k\), take the maximum of the finitely many thresholds \(J_{i,k}\) needed for its proper ceilings or collapsed bounds. Make these common thresholds strictly increasing, and construct \(s_j\) by (3.8). The same radius (3.9) gives (3.12) for every coordinate. Apply (3.13) or (3.14) coordinatewise. Each prescribed compact set and tolerance then has a common threshold by another finite maximum. \(\square\)

## References

- Terence Tao, [246B, Notes 2: Some connections with the Fourier transform](https://terrytao.wordpress.com/2021/01/23/246b-notes-2-some-connections-with-the-fourier-transform/), for background on entire Fourier transforms and support. Its normalization differs from (1.1).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I*, Springer, 1983, for compact Fourier theory and PSH compactness.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II*, Springer, 1983, Chapter XVI, for logarithmic-frequency center changes and neighborhood bounds. The exact affine identity, moving-test proof, quantified diagonal and proper/collapsed conclusions are proved above.
