# The geometry of coefficients and strength

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

An equation can keep its strength while its coefficients vary, then lose it at a particular parameter value. The coefficient space is finite-dimensional, but the strength comparison tests infinitely many frequencies. We show how a compact family of linear forms records all the possible losses. This also proves an exact perturbation criterion: adding every complex multiple of a polynomial preserves strength precisely when that polynomial is dominated by the original one.

Read [Rescaled symbols and stable strength](rescaled-symbols-and-stable-strength.md) and [Operator strength and local inverses](operator-strength-and-local-inverses.md) first. We use compactness in finite-dimensional complex vector spaces and the frequency-window estimates already proved there. Hörmander [HII], Theorem 10.4.7 and Corollary 10.4.8, gives the coefficient-form description and the criterion for all complex multiples. Mantlik [Mantlik] and Malgrange [Malgrange] provide broader parameter-dependent and approximation context.

## Evaluation probes in a finite-dimensional space

Fix a nonzero polynomial \(P\). Let
\[
W=\{Q:Q\prec P\},\qquad W_0=\{Q:Q\ll P\}.
\]
Both are finite-dimensional complex vector spaces. A dominated polynomial is weaker, so \(W_0\subset W\). Write \(\mathscr E\) for the set of polynomials of equal strength to \(P\). Thus \(\mathscr E\subset W\), and \(P\in\mathscr E\).

For each real frequency, define a complex-linear form on \(W\) by
\[
\ell_\xi(Q)=\frac{Q(\xi)}{S_P(\xi)}.
\tag{1}
\]
Let \(Y\) be the closure of these forms in \(W^*\), with its finite-dimensional topology. It is a compact set that does not contain zero. To prove boundedness, fix a basis of \(W\) and use the weak comparison for each basis polynomial in (1). To exclude zero, observe that every \(\partial^\alpha P\) belongs to \(W\), and
\[
\sum_\alpha|\ell_\xi(\partial^\alpha P)|^2=1.
\tag{2}
\]
Equation (2) persists in every limit in \(Y\).

The forms relevant to changes of strength are
\[
Y_0=\{\ell\in Y:\ell(R)=0\text{ for every }R\in W_0\}.
\tag{3}
\]
This is a compact subset of \(Y\), hence it also excludes zero. We shall prove that it is nonempty and that it detects precisely the polynomials outside \(\mathscr E\).

Here is a convenient way of obtaining forms in \(Y_0\).

**Lemma 1.1.** Suppose \(t_j\to\infty\) and the frequencies \(\zeta_j\) satisfy
\[
\frac{S_P(\zeta_j,t_j)}{S_P(\zeta_j,1)}\leq C.
\tag{4}
\]
Every limit of a subsequence of \(\ell_{\zeta_j}\) belongs to \(Y_0\).

**Proof.** For \(R\in W_0\), domination gives
\[
|\ell_{\zeta_j}(R)|
\leq C\frac{S_R(\zeta_j,1)}{S_P(\zeta_j,t_j)}\longrightarrow0.
\]
Thus every limit annihilates \(W_0\). Compactness of \(Y\) ensures convergent subsequences. \(\square\)

The frequency sequence need not be specified in advance. The next argument chooses it by enlarging windows and moving within them to a point where the polynomial is large.

## The exact set where strength is preserved

**Theorem 2.1.** The set \(Y_0\) is nonempty. A polynomial \(Q\in W\) belongs to \(\mathscr E\) exactly when
\[
\ell(Q)\ne0\quad\text{for every }\ell\in Y_0.
\tag{5}
\]
Moreover,
\[
W_0=\bigcap_{\ell\in Y_0}\ker\ell.
\tag{6}
\]

**Proof.** We prove three assertions.

First, let \(Q\in W\) fail to have equal strength to \(P\). The reverse comparison fails, so there are frequencies \(\xi_j\) with \(S_Q(\xi_j,1)/S_P(\xi_j,1)\to0\). Let \(m\geq\max(1,\deg P)\). By passing to a more rapidly approaching sequence, choose \(t_j\to\infty\) with
\[
\frac{S_Q(\xi_j,t_j)}{S_P(\xi_j,t_j)}
\leq t_j^m\frac{S_Q(\xi_j,1)}{S_P(\xi_j,1)}\longrightarrow0.
\tag{7}
\]
For \(Q=0\), any \(t_j\to\infty\) and frequencies will do. Use the frequency-window norm equivalence to find \(h_j\), \(|h_j|\leq t_j\), with
\[
|P(\xi_j+h_j)|\geq c S_P(\xi_j,t_j).
\]
Put \(\zeta_j=\xi_j+h_j\). The window estimate for \(Q\) and the displayed lower bound give
\[
\frac{|Q(\zeta_j)|}{S_P(\zeta_j,1)}
\leq C\frac{S_Q(\xi_j,t_j)}{S_P(\xi_j,t_j)}\longrightarrow0.
\tag{8}
\]
The scaled shift estimate gives
\[
S_P(\zeta_j,t_j)\leq C'S_P(\xi_j,t_j)
\leq C''|P(\zeta_j)|\leq C''S_P(\zeta_j,1).
\]
Thus (4) holds. Take a limit of the forms \(\ell_{\zeta_j}\). Lemma 1.1 puts it in \(Y_0\), and (8) says that it annihilates \(Q\). Taking \(Q=0\) in this construction already proves that \(Y_0\) is nonempty.

Second, suppose \(Q\in W\) is annihilated by some \(\ell\in Y_0\). Choose \(\xi_j\) with \(\ell_{\xi_j}\to\ell\). Every positive-order derivative \(\partial^\alpha Q\) is dominated by \(P\), because \(Q\prec P\). Hence \(\ell(\partial^\alpha Q)=0\) for all \(|\alpha|\geq1\). Together with \(\ell(Q)=0\), this gives
\[
\frac{S_Q(\xi_j,1)}{S_P(\xi_j,1)}
=\left(\sum_\alpha|\ell_{\xi_j}(\partial^\alpha Q)|^2\right)^{1/2}
\longrightarrow0.
\]
The reverse comparison is impossible, so \(Q\notin\mathscr E\). This proves (5) in both directions.

Third, (3) immediately shows that \(W_0\) is contained in the intersection in (6). Suppose \(Q\in W\setminus W_0\). The symbol characterization of domination gives a number \(c>0\), scales \(t_j\to\infty\), and frequencies \(\xi_j\) with
\[
|Q(\xi_j)|\geq cS_P(\xi_j,t_j).
\tag{9}
\]
Weak comparison supplies \(|Q(\xi_j)|\leq C_Q S_P(\xi_j,1)\). Thus (9) implies (4) with \(\zeta_j=\xi_j\). A subsequential limit lies in \(Y_0\). Also
\[
|\ell_{\xi_j}(Q)|\geq c\frac{S_P(\xi_j,t_j)}{S_P(\xi_j,1)}\geq c.
\]
Its limit therefore does not annihilate \(Q\). This proves the other inclusion in (6). \(\square\)

The coefficient set \(\mathscr E\) is consequently open in \(W\). For a fixed \(Q\in\mathscr E\), compactness gives
\(\min_{\ell\in Y_0}|\ell(Q)|>0\).
The forms in \(Y_0\) have uniformly bounded norms, so small coefficient changes keep this minimum positive. Its complement is a union of complex hyperplanes, one for each \(\ell\in Y_0\).

The forms act on polynomial coefficients. They do not assert that the same single real frequency witnesses every strength loss. Some are limits along frequencies that escape to infinity.

## Perturbations by every complex multiple

**Theorem 3.1.** For a polynomial \(R\), the following are equivalent:

1. \(R\ll P\).
2. \(P+aR\) has equal strength to \(P\) for every \(a\in\mathbb C\).

**Proof.** If \(R\ll P\), then \(aR\ll P\) for every scalar \(a\), and the stable-strength lemma gives assertion 2. Conversely, assertion 2 at \(a=1\) implies \(R\in W\), by subtracting \(P\) from a polynomial weaker than \(P\). If \(R\notin W_0\), Theorem 2.1 gives \(\ell\in Y_0\) with \(\ell(R)\ne0\). Since \(P\in\mathscr E\), \(\ell(P)\ne0\). Set
\[
a=-\frac{\ell(P)}{\ell(R)}.
\]
Then \(\ell(P+aR)=0\), so \(P+aR\notin\mathscr E\) by (5), contradicting assertion 2. Thus \(R\in W_0\). \(\square\)

This theorem explains the role of dominated corrections in the formal transpose and composition formulas. Their coefficients can have arbitrary complex values at a point, and domination preserves strength for all those values. Weak comparison alone does not give that guarantee.

**Example 3.2.** Let \(P(\xi)=\xi\) in one variable and \(R=i\xi\). For every real \(t\), \(P+tR=(1+it)\xi\) has the same strength as \(P\). Yet \(R\) is not dominated by \(P\), since they have the same degree. The complex value \(a=i\) makes \(P+aR=0\). Requiring only real multiples would therefore be a different condition.

## Two coefficient geometries

For the elliptic linear polynomial \(P(\xi_1,\xi_2)=\xi_1+i\xi_2\), the weaker space consists of all affine linear polynomials
\[
Q=a\xi_1+b\xi_2+c.
\]
Its dominated subspace consists of the constants. By the elliptic classification, \(Q\) has equal strength to \(P\) exactly when its linear part has no nonzero real zero. In coefficient coordinates this means
\[
\operatorname{Im}(\overline a b)\ne0.
\tag{10}
\]
Indeed the real matrix sending \((\xi_1,\xi_2)\) to the real and imaginary parts of the linear form has determinant \(\operatorname{Im}(\overline a b)\). The constant coefficient \(c\) does not affect strength. Along a continuous equal-strength path the sign of this determinant cannot change.

For \(P(\xi_1,\xi_2)=\xi_1\xi_2\), which is of principal type, the weaker space is
\[
Q=a\xi_1\xi_2+b\xi_1+c\xi_2+d.
\tag{11}
\]
To see this, the top-homogeneous comparison forces a quadratic part to vanish on both coordinate axes; it must therefore be a multiple of \(\xi_1\xi_2\). All lower-degree terms are dominated. A polynomial in (11) has equal strength exactly when \(a\ne0\). If \(a\ne0\), divide by \(a\) and apply the stable dominated-perturbation lemma. If \(a=0\), a lower-degree polynomial cannot be as strong as the quadratic \(P\). Here the set where strength is lost is the single coefficient hyperplane \(a=0\).

## Uniform estimates on compact coefficient families

**Proposition 5.1.** If \(K\) is a compact subset of \(\mathscr E\), there is a constant \(C_K\) such that
\[
C_K^{-1}S_P(\xi,t)\leq S_Q(\xi,t)\leq C_K S_P(\xi,t)
\qquad(Q\in K,\ \xi\in\mathbb R^n,\ t\geq1).
\tag{12}
\]

**Proof.** Choose any coefficient norm \(\|\cdot\|_W\). The uniform scaled comparison for each basis polynomial of \(W\) gives
\[
S_R(\xi,t)\leq C\|R\|_W S_P(\xi,t),
\qquad R\in W,\ t\geq1.
\]
This proves the upper bound on bounded \(K\). Define
\[
r(Q)=\inf_{\xi,\ t\geq1}\frac{S_Q(\xi,t)}{S_P(\xi,t)}.
\]
The derivative-vector triangle inequality and the displayed bound give
\(|r(Q)-r(Q')|\leq C\|Q-Q'\|_W\).
For \(Q\in\mathscr E\), the reverse uniform scaled comparison gives \(r(Q)>0\). The continuous positive function \(r\) has a positive minimum on \(K\), proving the lower bound in (12). \(\square\)

This is a compact-family estimate. A family approaching the complement of \(\mathscr E\) can have comparison constants tending to infinity, even if no finite parameter has yet reached that complement.

## Exercises with solutions

**Exercise 1 (entry).** Prove that the evaluation probes in (1) cannot converge to zero, even if \(P(\xi_j)\) vanishes at every point of a frequency sequence.

**Solution.** The polynomial \(P\) itself need not detect those points, but its derivative polynomials belong to \(W\). Equation (2) says that at least one of the finitely many derivative evaluations has absolute value at least the reciprocal square root of the number of derivatives in the sum. If the probes converged to zero as linear forms, each such derivative evaluation would tend to zero, contradicting that sum. This is precisely why normalization by the full derivative norm is useful.

**Exercise 2 (intermediate).** For \(P=\xi_1\xi_2\), show that the two limits obtained from \(\xi=(s,s)\) and \(\xi=(s,-s)\), \(s\to\infty\), act on (11) by \(Q\mapsto a\) and \(Q\mapsto-a\). Explain how they give (6) in this example.

**Solution.** The derivative norm is \((\xi_1^2\xi_2^2+\xi_1^2+\xi_2^2+1)^{1/2}\). On either sequence it is asymptotic to \(s^2\). The mixed quadratic term divided by that norm tends to \(a\) on the first sequence and \(-a\) on the second; all linear and constant terms tend to zero. These forms annihilate the dominated lower-degree polynomials. Their common kernel is exactly \(a=0\), which is \(W_0\) here. Both are members of \(Y_0\), so they explicitly detect every polynomial outside \(W_0\).

**Exercise 3 (intermediate).** For \(Q_t=\xi_1+i t\xi_2\), \(t>0\), determine what happens to its strength comparison with \(P=\xi_1+i\xi_2\) as \(t\downarrow0\).

**Solution.** Every \(Q_t\), \(t>0\), is elliptic of order one, hence has equal strength to \(P\). Along \((0,s)\), the ratio \(S_P/S_{Q_t}\) tends to \(1/t\) as \(s\to\infty\). Thus any reverse comparison constant is at least \(1/t\) and cannot remain bounded as \(t\downarrow0\). At zero the linear coefficient determinant in (10) vanishes, and \(Q_0=\xi_1\) loses control of the second direction. Proposition 5.1 applies on a compact parameter interval bounded away from zero.

**Exercise 4 (advanced).** Show that \(\mathscr E+W_0=\mathscr E\), and that its image in \(W/W_0\) is open. What information is discarded by this quotient?

**Solution.** Every form in \(Y_0\) annihilates \(W_0\). Therefore \(\ell(Q+R)=\ell(Q)\) for \(R\in W_0\), and (5) proves the equality. The quotient projection is open: choose a linear complement of \(W_0\), identify the quotient with that finite-dimensional complement, and observe that projections of open product neighborhoods are open. Since \(\mathscr E\) is open and is invariant under \(W_0\), its quotient image is open as well. The quotient discards precisely the dominated changes of the symbol, which preserve strength for arbitrary complex coefficients. It does not discard every lower-degree term for an arbitrary non-principal-type polynomial.

## References

- [Mantlik] Frank Mantlik, *Partial differential operators depending analytically on a parameter*, Annales de l'Institut Fourier **41** (1991), 577–599. [Original article](https://www.numdam.org/item/10.5802/aif.1266/).
- [Malgrange] Bernard Malgrange, *Existence et approximation des solutions des équations aux dérivées partielles et des équations de convolution*, Annales de l'Institut Fourier **6** (1956), 271–355. [Original article](https://aif.centre-mersenne.org/articles/10.5802/aif.65/).
- [HII] Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 2005 (reprint of the 1983 edition), Section 10.4, Theorem 10.4.7 and Corollary 10.4.8, pp. 36–37. [Publisher record](https://link.springer.com/book/10.1007/b138375).
