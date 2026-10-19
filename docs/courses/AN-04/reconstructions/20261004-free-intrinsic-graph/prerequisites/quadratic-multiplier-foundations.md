# Quadratic forms, volumes and separation

This companion retains AN03-P001 Sections 4–5 and supplies the connecting
finite-dimensional facts used by the selected metric and multiplier proofs.

This is a separate modified selection from the earlier AN-03 programme.
Original principal author and publisher: AN-03 course-writing task /
AN-03 local course project, 2026. Earlier modification: AN-03 course-writing task and
OpenAI Codex. Selection and the identified connecting proofs: GPT-6 Astra
(OpenAI), Ultra, 4 October 2026; publisher: AN-04 local course project.

Original text: CC0.

## 0. Exact earlier inputs

The [measure companion, M0–M8](measure-and-l2.md) supplies the declared
choice principle, rational enumeration, completed measure and convergence
theorems. The [Fourier companion, L0–L3](fourier-l2.md) supplies the
full \(L^2\) extension and distributional compatibility. The exact
[U001 Schwartz and spectral proofs, Q3–Q5](../../20261004-free-stationary-phase/quadratic-stationary-phase.md#q3-schwartz-estimates-and-the-signs-in-the-fourier-rules)
supply all finite-dimensional Fourier and spectral steps.
The finite-dimensional compactness, algebra and differential inputs are
the exact earlier proofs named in that companion's F0 contract.
Smooth cutoffs are [U001 P14.3](../../20261004-free-stationary-phase/exponential-prerequisite-completions.md#p14-3-exponential-decay-and-the-flat-cutoff-function).
Compact and affine substitution, with every determinant, is
[U001 P21.3–P21.4](../../20261004-free-stationary-phase/change-of-variables-prerequisite-completions.md#p21-3-the-full-compact-jordan-change-of-variables-theorem).
M8 proves compatibility of these integrals with the Lebesgue integrals.

## 1. Positive forms and coordinate maps

Let \(Q(X)=X^{\mathsf T}GX\), where \(G\) is real symmetric positive
definite. U001 Q5 gives \(G=U\operatorname{diag}(\lambda_j)U^{\mathsf T}\),
\(\lambda_j>0\). Put
\(L=U\operatorname{diag}(\lambda_j^{-1/2})\).
Then \(L^{\mathsf T}GL=I\), \(G^{-1}=LL^{\mathsf T}\), and
\(J=|\det L|=(\det G)^{-1/2}>0\), by direct multiplication and the
proved determinant rules. Thus \(Q(Ly)=|y|^2\) and
\(Q^{-1}(\Xi)=\Xi^{\mathsf T}G^{-1}\Xi=|L^{\mathsf T}\Xi|^2\).
The Euclidean Cauchy–Schwarz inequality follows by expanding
\(|v-tv'|^2\geq0\) and minimizing in the real scalar \(t\);
the zero-vector case is immediate. Transfer this inequality by \(L\)
to obtain the triangle inequality for \(Q^{1/2}\).

If \(B\) is another real symmetric matrix, its expression under these
maps is \(L^{-1}BL^{-\mathsf T}\), which is again symmetric and hence
has an orthonormal eigenbasis by Q5. This proves the simultaneous
normalization used in the multiplier companion, without a new
spectral or Gram-matrix theorem. The chain rule gives the corresponding
directional derivative identities. In an orthonormal basis each
coordinate of a unit direction has absolute value at most one;
expansion of a \(k\)-linear form then compares its directional norm
and its maximum coordinate coefficient with factors at most \(d^k\).

## 2. Lebesgue volume of each ellipsoid

Let \(K=\{Q(X)<r^2\}\), \(r>0\). Choose a smooth function
\(b:\mathbb R\to[0,1]\), zero for \(t\leq0\) and one for \(t\geq1\),
using the supplied flat cutoff, and set
\(f_k(X)=b(k(r^2-Q(X)))\).
Each \(f_k\) is compact smooth, is supported in the closed ellipsoid,
and converges pointwise to \(\mathbf1_K\). All supports lie in a
fixed cube: positivity of the eigenvalues bounds \(|X|\) on them.
Compact substitution, followed by M8 and dominated convergence on
that cube and its inverse image, therefore gives
\[
 |K|=J\,|\{y:|y|<r\}|=Jr^d\,|\{y:|y|<1\}|.
 \tag{F1}
\]
The second equality uses the same argument for \(y=rz\).
The unit ball has positive finite measure, since it contains a
positive-volume cube and lies in a bounded cube. Translations have
Jacobian one. Consequently every ellipsoid volume comparison used
in the covering and counting proofs follows from (F1), inclusions,
and countable additivity. No unproved general measure substitution
theorem is being invoked for indicator functions.

## 3. Dual ellipsoids and phase distances

Suppose \(B:E^*\to E\) is symmetric and
\(A(\Xi)=\langle B\Xi,\Xi\rangle\). Use Section 1 to make \(Q\)
Euclidean and \(B=\operatorname{diag}(\beta_j)\). On the range of
\(B\), write
\[
 Q^A(Z)=\sum_{\beta_j\ne0}Z_j^2/\beta_j^2;
 \qquad Q^A(Z)=+\infty\quad(Z\notin\operatorname{ran}B).
 \tag{F2}
\]
This is exactly the supremum defining the phase-dual form: put
\(w_j=\beta_j\Xi_j\), apply Cauchy–Schwarz to
\(\sum Z_jw_j/\beta_j\), and approach the unit vector in that
direction. A nonzero coordinate in \(\ker B\) makes the supremum
infinite by scalar dilation. This proves both directions, including
\(B=0\).

For \(\eta\in E^*\), the support value of
\(\{Z:Q^A(Z)<a^2\}\) is
\[
 a\left(\sum_j\beta_j^2\eta_j^2\right)^{1/2}
       =a\,Q(B\eta)^{1/2}.
 \tag{F3}
\]
Again Cauchy–Schwarz gives the upper bound. When the square root is
positive, take \(Z_j\) proportional to \(\beta_j^2\eta_j\) and
approach the boundary from inside; when it is zero, every pairing
vanishes and both sides are zero. The same calculation with the
ordinary dual form gives support value \(rQ^{-1}(\eta)^{1/2}\)
for \(\{Q<r^2\}\).
For \(Q_1\leq M Q_2\), inclusion of the defining ellipsoids and
scaling gives \(Q_1^A\geq M^{-1}Q_2^A\) on the common finite
domain. Off it both sides are interpreted as infinite.
Sections 4–5 below prove the separation and sum rules needed to
use these support values.

## 4. Strict separation of an open convex set

**Theorem 4.1 (Strict separation).** Let \(V\) be a finite-dimensional real vector space, let \(C\subset V\) be nonempty, open and convex, and let \(x\notin C\). There is a nonzero real covector \(\eta\) such that
\[
\eta(y)<\eta(x)\quad(y\in C),
\qquad \sup_{y\in C}\eta(y)\leq\eta(x).
\]
The second inequality includes \(x\) on the boundary. The supremum need not be attained. The proof uses only finite-dimensional compactness and the inner product.

Choose an auxiliary Euclidean norm, put \(K=\overline C\), and fix \(c\in C\) with \(B(c,r)\subset C\), \(r>0\). First, if \(z\in K\) and \(0\leq t<1\), then
\[
(1-t)c+tz\in C.
\]
For \(t=0\) this is immediate. For \(0<t<1\), choose \(z_j\in C\) tending to \(z\). Convexity gives a ball of radius \((1-t)r\) centered at \((1-t)c+tz_j\) inside \(C\). For sufficiently large \(j\), this ball contains \((1-t)c+tz\), proving the assertion.

For \(\varepsilon>0\), put \(z_\varepsilon=x+\varepsilon(x-c)\). This point lies outside \(K\): if it lay in \(K\), then
\[
x=\frac{\varepsilon}{1+\varepsilon}c
 +\frac{1}{1+\varepsilon}z_\varepsilon
\]
would lie in \(C\) by the preceding assertion. The nonempty closed set \(K\) has a point \(q_\varepsilon\) nearest to \(z_\varepsilon\). To see existence without a compactness assumption on \(K\), take a minimizing sequence. Its distance to \(z_\varepsilon\) is bounded, so it has a convergent subsequence in finite dimensions; closedness places its limit in \(K\).

Write \(v_\varepsilon=z_\varepsilon-q_\varepsilon\ne0\). For \(y\in K\), the segment \(q_\varepsilon+t(y-q_\varepsilon)\), \(0\leq t\leq1\), lies in \(K\). Differentiating the squared distance at its minimum \(t=0\) gives
\[
\langle v_\varepsilon,y-q_\varepsilon\rangle\leq0.
\]
Consequently, for \(u_\varepsilon=v_\varepsilon/|v_\varepsilon|\),
\[
\langle u_\varepsilon,y\rangle
\leq\langle u_\varepsilon,z_\varepsilon\rangle
-|v_\varepsilon|
\leq\langle u_\varepsilon,z_\varepsilon\rangle.
\]
Choose \(\varepsilon=1/k\) and a convergent subsequence of the unit vectors, with limit \(u\), \(|u|=1\). Since \(z_\varepsilon\to x\), the last inequality implies \(\langle u,y\rangle\leq\langle u,x\rangle\) for every \(y\in K\). The same subsequence works for every \(y\): it was selected using only the unit vectors, and the inequality holds for every \(y\) at every index.

Set \(\eta(y)=\langle u,y\rangle\). It is nonzero. For \(y\in C\), openness gives \(y+\delta u\in C\) for some \(\delta>0\), whence
\[
\eta(y)+\delta\leq\eta(x).
\]
This proves strict pointwise separation. The supremum statement follows because \(\eta(C)\) is nonempty and bounded above. In dimension zero the hypotheses cannot occur, since the only nonempty open set is all of \(V\).

## 5. Support functions of Minkowski sums

**Proposition 5.1.** For nonempty \(A,B\subset V\), put
\[
h_A(\eta)=\sup_{a\in A}\eta(a)\in\mathbb R\cup\{+\infty\}.
\]
Then \(h_{A+B}(\eta)=h_A(\eta)+h_B(\eta)\), where \(A+B=\{a+b:a\in A,b\in B\}\). Nonemptiness excludes \(-\infty\), so the right side is unambiguous.

Linearity first gives the inequality \(\leq\). If both right-hand suprema are finite, choose \(a,b\) within \(\varepsilon/2\) of the two suprema. Their sum gives the reverse inequality up to \(\varepsilon\); let \(\varepsilon\downarrow0\). If \(h_A(\eta)=+\infty\), fix \(b_0\in B\). The values \(\eta(a+b_0)\) are unbounded above, so \(h_{A+B}(\eta)=+\infty\). Interchange \(A,B\) for the other case. No boundedness, compactness or convexity is needed for this identity.
