# Orthogonalizing nearly disjoint projections

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026, with writing-AI self-checking. Original exposition, proof and exercises: CC0.*

Almost orthogonal subspaces can be corrected simultaneously. The useful device is to assemble their inclusion maps into one operator, measure its failure to be an isometry, and correct that failure by its positive square root. This gives a uniform operator-norm estimate, even when the subspaces are infinite dimensional.

Projection orthogonalization is one of the geometric tools in Alain Connes's work on noncommutative Rokhlin towers and outer conjugacy. Here the Gram operator gives a direct proof with an explicit linear bound. Basic preparation is [Hilbert spaces and compact operators](../../foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators.html). The square-root correction needed below is constructed by convergent operator power series, so the proof includes that calculation.

## 1. The simultaneous correction

Let \(M\subset B(H)\) be a von Neumann algebra. Projections are self-adjoint idempotents in \(M\). Their join is the projection onto the closed linear span of their ranges. Two projections \(p,q\) are equivalent if some \(v\in M\) satisfies \(v^*v=p\) and \(vv^*=q\).

**Theorem.** Let \(f_0,\ldots,f_{m-1}\in M\) be projections, where \(m\ge1\), and suppose
\[
 \begin{gathered}
 \|f_if_j\|\le d\quad(i\ne j),\\
 a=(m-1)d<1.
 \end{gathered}
\tag{1.1}
\]
There are orthogonal projections \(e_j\in M\), each equivalent to \(f_j\), such that
\[
 \begin{gathered}
 \sum_j e_j=\bigvee_j f_j,\\
 \|e_j-f_j\|\le 3a.
 \end{gathered}
\tag{1.2}
\]
Neither a trace nor a separability hypothesis is required. A zero projection in the family is allowed.

*Proof.* Put \(K=\bigoplus_{j=0}^{m-1}f_jH\), and define
\[
 \begin{gathered}
 T:K\longrightarrow H,\\
 T(\xi_0,\ldots,\xi_{m-1})=\sum_j\xi_j.
 \end{gathered}
\tag{1.3}
\]
The Gram operator \(G=T^*T\) has identity diagonal and off-diagonal entries given by the restrictions of \(f_if_j\). For \(\xi=(\xi_j)\in K\),
\[
 \begin{gathered}
 \|((G-I_K)\xi)_i\|
 \le d\sum_{j\ne i}\|\xi_j\|,\\
 \sum_i\left(\sum_{j\ne i}b_j\right)^2
 \le(m-1)^2\sum_j b_j^2,\\
 b_j\ge0.
 \end{gathered}
\tag{1.4}
\]
The second inequality follows by Cauchy–Schwarz in each row and then counting each \(b_j^2\) exactly \(m-1\) times. Consequently
\[
 \begin{gathered}
 \|G-I_K\|\le a,\\
 (1-a)I_K\le G\le(1+a)I_K.
 \end{gathered}
\tag{1.5}
\]
The lower bound shows that \(T\) has closed range: if \(T\xi_n\) is Cauchy, then \(\xi_n\) is Cauchy. Its range is the finite sum of the \(f_jH\), whose closure defines their join. We next construct the square-root correction directly. Set
\[
 \begin{gathered}
 B=I_K-G,\\
 c_n=4^{-n}\binom{2n}{n},\\
 F(z)=\sum_{n\ge0}c_nz^n=(1-z)^{-1/2}.
 \end{gathered}
\tag{1.6}
\]
For completeness, \(c_0=1\) and \((n+1)c_{n+1}=(n+1/2)c_n\). Since \(0<c_n\le1\), the series and its termwise derivative converge for \(|z|<1\). The recurrence gives \((1-z)F'(z)=F(z)/2\), so differentiating \((1-z)F(z)^2\) makes it constant, with value one at zero. This proves the indicated identity, choosing the value positive on \(0\le z<1\).

Because \(\|B\|\le a<1\), the following series converge absolutely in operator norm:
\[
 \begin{gathered}
 R=\sum_{n\ge0}c_nB^n,\\
 S=(I_K-B)R,\\
 S=I_K-\sum_{n\ge1}\frac{c_n}{2n-1}B^n.
 \end{gathered}
\tag{1.7}
\]
The last identity follows from \(c_n-c_{n-1}=-c_n/(2n-1)\). Products of these absolutely convergent series obey the scalar coefficient identities. Hence \(R^2G=I_K\), \(RS=SR=I_K\) and \(S^2=G\). Both \(R\) and \(S\) are self-adjoint and commute with \(G\). The nonnegative coefficients in the last series give
\[
 \begin{aligned}
 \|I_K-S\|&\le\sum_{n\ge1}\frac{c_n a^n}{2n-1}\\
 &=1-\sqrt{1-a}<1.
 \end{aligned}
\tag{1.8}
\]
In particular \(S\) is positive and invertible: for every \(\xi\), its quadratic form is at least \((1-\|I_K-S\|)\|\xi\|^2\), and \(R\) is its inverse. Thus these are precisely a positive square root and its inverse, constructed without a further spectral approximation theorem. Define
\[
 W=TR.
\tag{1.9}
\]
Then \(W^*W=I_K\), and \(W\) maps \(K\) onto the range of \(T\). If \(P_j\) is the coordinate projection of \(K\), put
\[
 e_j=WP_jW^*.
\tag{1.10}
\]
These are orthogonal projections and sum to the range projection of \(T\).

To check that the construction stays inside \(M\), view \(K\) as the range of \(Q=\operatorname{diag}(f_0,\ldots,f_{m-1})\) in \(H^m\). The row operator \((f_0,\ldots,f_{m-1})\) belongs to \(M_{1,m}(M)\); its Gram operator belongs to the corner \(QM_m(M)Q\). Every term of (1.7), and its norm limit, belongs to this corner, which is a norm-closed algebra with identity \(Q\). Hence every entry of \(W\) belongs to the corresponding matrix algebra over \(M\). Therefore \(e_j\in M\). The \(j\)-th entry \(v_j\) of \(W\) satisfies \(v_j^*v_j=f_j\) and \(v_jv_j^*=e_j\), proving equivalence.

Since \(T=WS\), the power-series bound (1.8) gives
\[
 \begin{aligned}
 \|W-T\|&=\|I_K-S\|\\
 &\le \frac{a}{1+\sqrt{1-a}}\le a.
 \end{aligned}
\tag{1.11}
\]
Here \(1-\sqrt{1-a}=a/(1+\sqrt{1-a})\). Also \(TP_jT^*=f_j\) and \(\|T\|\le\sqrt{1+a}\). Expanding the difference of these two products gives
\[
 \begin{aligned}
 \|e_j-f_j\|
 &\le(1+\sqrt{1+a})\|W-T\|\\
 &\le\frac{1+\sqrt{1+a}}{1+\sqrt{1-a}}a
 \le3a.
 \end{aligned}
\tag{1.12}
\]
For \(m=1\), the same formulas give \(e_0=f_0\) and zero error. If every \(f_j=0\), all assertions hold with every \(e_j=0\); the preceding argument can otherwise be carried out on the nonzero corner \(Q\). This proves the theorem. \(\square\)

## 2. A factorial version and useful examples

**Corollary.** If \(0<d<1/m!\), the same construction gives
\[
 \|e_j-f_j\|<m!d.
\tag{2.1}
\]

*Proof.* For \(m=1\), the error is zero. For \(m=2\), \(a=d<1/2\), and (1.12) gives
\[
 \|e_j-f_j\|
 \le\frac{1+\sqrt{1+d}}{1+\sqrt{1-d}}d<2d.
\tag{2.2}
\]
For the last strict inequality,
\[
 \begin{aligned}
 1+\sqrt{1+d}&<1+\sqrt{3/2}\\
 &<2(1+1/\sqrt2)\\
 &<2(1+\sqrt{1-d}).
 \end{aligned}
\]
For \(m\ge3\), the coefficient \(1+\sqrt{1+a}\) is strictly below \(3\). Thus the error is strictly below \(3(m-1)d\), and \(3(m-1)\le m!\). The hypothesis also ensures \((m-1)d<1\), so the theorem applies. \(\square\)

**Example 1: five projections.** If every pairwise product has norm at most \(10^{-4}\), then \(a=4\cdot10^{-4}\). The error bound in (1.2) is \(0.0012\). The factorial estimate is \(0.012\), so the Gram bound is substantially sharper in this example.

**Example 2: two lines.** In \(\mathbb C^2\), take unit vectors \(x_0=(1,0)\) and \(x_1=(c,\sqrt{1-c^2})\), where \(0\le c<1\), and let \(f_j\) project onto their spans. Then \(\|f_0f_1\|=c\) and, in their coordinate Hilbert space,
\[
 \begin{gathered}
 G=\begin{pmatrix}1&c\\c&1\end{pmatrix},\\
 \operatorname{spec}(G)=\{1-c,1+c\}.
 \end{gathered}
\tag{2.3}
\]
Multiplying the two-column inclusion matrix by \(G^{-1/2}\) produces orthonormal columns. Their rank-one projections are the corrected family. As \(c\) approaches one, the smallest eigenvalue approaches zero; this explains the strict threshold in (1.1).

**Example 3: the threshold can fail.** For two identical nonzero rank-one projections, \(d=1\) and \(a=1\). Their join has rank one. Two orthogonal nonzero equivalent rank-one projections would have a rank-two sum, so the theorem's conclusion is impossible for this family. A strict lower spectral bound is essential.

## 3. Exercises with solutions

**Exercise 1.** For seven projections with \(d=10^{-3}\), compute \(a\), the Gram bound and the factorial bound. Is the factorial corollary applicable?

*Solution.* We have \(a=0.006<1\), so the theorem gives an error at most \(0.018\). The numerical factorial expression is \(7!d=5.04\), but the corollary is inapplicable because \(10^{-3}>1/5040\). The theorem still applies.

**Exercise 2.** Explain why replacing the finite sum of ranges by its closure does not enlarge the range of \(T\) under (1.1).

*Solution.* Equation (1.5) gives \(\|T\xi\|\ge\sqrt{1-a}\|\xi\|\). A convergent sequence \(T\xi_n\) therefore comes from a Cauchy sequence \(\xi_n\), which converges because \(K\) is complete. Its image is the given limit. Thus the range of \(T\) is closed and already equals the closed span used in the join.

**Exercise 3.** Show that (1.5) bounds the condition number of \(T\) on its range, and compute the bound for the two-line example with \(c=1/2\).

*Solution.* The upper bound is \(\|T\|\le\sqrt{1+a}\), and the inverse on its range has norm at most \((1-a)^{-1/2}\). The condition number is at most \(\sqrt{(1+a)/(1-a)}\). For \(a=c=1/2\), this is \(\sqrt3\). The two eigenvalues in (2.3) show that the bound is attained in that example.

**Exercise 4.** Why does the construction preserve each projection's equivalence class rather than merely its rank in a Hilbert-space representation?

*Solution.* The column \(v_j\) of \(W\) belongs to the original algebra \(M\), by the matrix-corner power-series argument. Its initial projection is exactly \(f_j\), and its final projection is exactly \(e_j\). It is therefore an equivalence inside \(M\). Equality of Hilbert-space dimensions alone would not establish this algebraic conclusion.

## References

Alain Connes, *Outer conjugacy classes of automorphisms of factors*, Annales scientifiques de l'École Normale Supérieure 8 (1975), 383–419, Lemma 1.2.6. [Freely readable article](https://numdam.org/articles/10.24033/asens.1295/). Its projection-orthogonalization argument provides the mathematical context; the simultaneous Gram-operator treatment and exercises above are independently written.
