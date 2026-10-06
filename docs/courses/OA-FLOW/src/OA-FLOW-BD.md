# Norm-controlled density on arbitrary Hilbert spaces

*Fresh local proof by GPT-6 Astra (OpenAI), Ultra, 2026-10-04. CC0-1.0 to the extent of rights in this new exposition.*

This proof supplies the bounded-density input used by WH-02 and the positive contraction net used by WH-04. The algebra need not be norm closed or unital, and the Hilbert space is arbitrary. The only analytic inputs are the elementary Hilbert facts and the exact spectral calculus in [SF-0 and SB-1–SB-6](OA-FLOW-SF.md#oa-flow.shared-foundations.sf-0). The scalar compact approximation used below is proved explicitly. The earlier Hilbert facts are [SF-0](OA-FLOW-SF.md#oa-flow.shared-foundations.sf-0) and [SB-0](OA-FLOW-SF.md#OA-FLOW.SF.SB0); the full spectral-domain proof is [SB-1–SB-6](OA-FLOW-SF.md#OA-FLOW.SF.SB1). Scalar spectral convergence uses [SC-04–05](OA-FLOW-SC.md#sc-04).

For human mathematical context see [Jones's author notes, Theorem 5.2.1, printed pp.32–33](https://math.berkeley.edu/~vfr/MATH20909/VonNeumann2009.pdf#page=32). The following proof supplies the arbitrary-Hilbert and nonclosed-algebra details, using finite-vector separation and a direct resolvent identity.

<a id="oa-flow.bd.1"></a>

## BD-1. The correct support corner and bicommutant density

Let \(\mathcal A\subseteq B(H)\) be a complex \*-subalgebra. Set \(H_0=\overline{\mathcal A H}\), with projection \(p\). This subspace reduces \(\mathcal A\), and \(\mathcal A\) is zero on \(H_0^\perp\): orthogonality to every \(a^*v\) forces \(a w=0\). Work first on \(H_0\), where the representation is nondegenerate. Let \(M=(\mathcal A|_{H_0})''\).

For vectors \(u_1,\ldots,u_n\), let \(Q\) be the projection onto the closure of
\(\{(au_1,\ldots,au_n):a\in\mathcal A\}\subseteq H_0^n\).
The subspace reduces every diagonal \(a\), so \(Q\) commutes with them, and its entries \(Q_{ij}\) lie in \(\mathcal A'\). The vector \(u=(u_j)\) belongs to its range even without a unit in \(\mathcal A\). Indeed
\(a(I-Q)u=(I-Q)au=0\) for every \(a\); the common kernel is zero by nondegeneracy in each coordinate. A diagonal \(x\in M\) commutes with \(Q\), so \(xu\) is in the same closed orbit. Thus \(\mathcal A\) is strongly dense in \(M\), hence weakly dense as well. Conversely \(M\) is strongly and weakly closed, since commutation with each fixed bounded operator is closed for both topologies. Therefore the closures agree with \(M\). On the original space the closure is \(M\oplus0\), with identity \(p\), not necessarily \(I_H\).

Write \(B=\overline{\mathcal A}^{\|\cdot\|}\) on \(H_0\). The self-adjoint part \(B_{\rm sa}\) is weakly dense in \(M_{\rm sa}\): take a weakly convergent algebra net and symmetrize it; adjoint is weakly continuous.

It is also strongly dense. If \(x=x^*\) could not be approximated on a finite tuple \((u_j)\), project its image \((xu_j)\) onto the real closed linear span of \(\{(bu_j):b\in B_{\rm sa}\}\) in the real Hilbert space underlying \(H_0^n\). The nonzero orthogonal difference supplies a functional
\(\operatorname{Re}\sum_j\langle bu_j,v_j\rangle\)
vanishing on \(B_{\rm sa}\) but not at \(x\). This is weakly continuous, contradicting the preceding weak density. The real orthogonal projection is proved by the same parallelogram argument as SF-0; no locally convex separation theorem is used.

<a id="oa-flow.bd.2"></a>

## BD-2. Continuous scalar functions stay in the algebra

Here is the precise elementary polynomial approximation needed. For continuous \(f\) on \([0,1]\), the Bernstein polynomials
\[
B_nf(t)=\sum_{k=0}^n f(k/n){n\choose k}t^k(1-t)^{n-k}
\tag{BD1}
\]
converge uniformly to \(f\). The nonnegative coefficients at each \(t\) sum to one; their weighted second moment about \(t\) is \(t(1-t)/n\), as follows by differentiating the binomial identity twice. For fixed \(\delta>0\), the approximation error is at most
\[
\sup_{|s-t|\leq\delta}|f(s)-f(t)|
+\frac{2\|f\|_\infty}{4n\delta^2}.
\tag{BD2}
\]
This follows by bounding the mass of \(|k/n-t|>\delta\) by the second moment divided by \(\delta^2\). First use uniform continuity to choose \(\delta\), then let \(n\) grow. Affine rescaling proves the result on any compact interval.

If that interval contains zero and \(f(0)=0\), subtract each approximating polynomial's value at zero to obtain polynomials with zero constant term, still converging uniformly. Hence for \(b=b^*\in B\) and continuous \(f\) on a real interval containing its spectrum and zero, with \(f(0)=0\), spectral norm estimates give \(f(b)\in B\). This includes the nonunital case. Real \(f\) can be approximated by real polynomials.

<a id="oa-flow.bd.3"></a>

## BD-3. Self-adjoint and positive contraction density

Suppose \(x=x^*\in M\) and \(\|x\|\leq1\). The scalar function
\[
f(t)=\frac{2t}{1+t^2}
\]
maps \([-1,1]\) bijectively onto itself. Its continuous inverse there is
\(g(s)=s/(1+\sqrt{1-s^2})\), with \(g(0)=0\). Set \(X=g(x)\). Then \(X=X^*\in M\), \(\|X\|\leq1\), and \(f(X)=x\). BD-1 gives self-adjoint \(Y_\alpha\in B\) with \(Y_\alpha\to X\) strongly; no bound on \(\|Y_\alpha\|\) is assumed.

For either sign, the bounded resolvent identity is
\[
(Y_\alpha\pm i)^{-1}-(X\pm i)^{-1}
=(Y_\alpha\pm i)^{-1}(X-Y_\alpha)(X\pm i)^{-1}.
\tag{BD3}
\]
Each left resolvent factor has norm at most one. The right side tends strongly to zero, by testing the strong convergence on the fixed vector \((X\pm i)^{-1}v\). Since
\[
f(Y_\alpha)=(Y_\alpha-i)^{-1}+(Y_\alpha+i)^{-1},
\tag{BD4}
\]
we get \(f(Y_\alpha)\to x\) strongly. These approximants are self-adjoint contractions and belong to \(B\), by BD-2 and \(f(0)=0\). This proves self-adjoint contraction density without bounding the original net.

For \(0\leq x\leq I\), apply that result to \(x^{1/2}\). The resulting self-adjoint contractions \(c_\alpha\in B\) satisfy \(c_\alpha^2\to x\) strongly: expand the difference and use the common bound. Each square is a positive contraction.

Now return to the original algebra \(\mathcal A\). A self-adjoint contraction \(c\in B\) can be approximated in norm within \(\delta>0\) by a self-adjoint \(d\in\mathcal A\), by symmetrizing a norm approximant. Then \(d/(1+\delta)\) is a self-adjoint contraction in \(\mathcal A\), converging in norm to \(c\) as the error decreases. For positive approximation use
\[
\frac{d^2}{(1+\delta)^2}\in\mathcal A_+,\qquad
0\leq\frac{d^2}{(1+\delta)^2}\leq I,
\tag{BD5}
\]
which converges in norm to \(c^2\). Given any finite-vector neighborhood and tolerance, first choose the \(B\) approximant and then the norm approximant. Ordering these neighborhoods by refinement produces the required nets in \(\mathcal A\). In particular positive contractions of \(\mathcal A\) converge strongly to \(I_{H_0}\), and therefore to \(p\) on \(H\).

<a id="oa-flow.bd.4"></a>

## BD-4. Arbitrary contractions and bounded strong-star approximation

For \(x\in M\) with \(\|x\|\leq1\), the operator
\[
Z=\begin{pmatrix}0&x\\x^*&0\end{pmatrix}
\tag{BD6}
\]
is a self-adjoint contraction on \(H_0\oplus H_0\). Entrywise approximation shows that the matrix algebra \(M_2(\mathcal A)\) is weakly dense in \(M_2(M)\). The proof of BD-1–3 therefore gives self-adjoint contraction matrices \(Z_\alpha\in M_2(\mathcal A)\) converging strongly to \(Z\). Let \(a_\alpha\) be their upper-right entries. Compression between the two summands gives \(\|a_\alpha\|\leq1\), \(a_\alpha\to x\) strongly, and, from the lower-left entries, \(a_\alpha^*\to x^*\) strongly. Thus the unit ball of \(\mathcal A\) is strong-star dense in the unit ball of \(M\).

All constructions use finite tuples and arbitrary directed neighborhood sets. No separability or sequential density is assumed. Degenerate representations are handled by \(p\); when \(\mathcal A=0\), \(H_0=0\), and the zero net gives all assertions.

<a id="oa-flow.bd.5"></a>

## BD-5. What this supplies to the modular route

For WH-02, apply BD-4 to its represented C\* algebra on the identity corner: every contraction in its bicommutant has a uniformly bounded strong, hence concrete ultraweak, approximating net. For WH-04, apply BD-3 to its nonunital represented right algebra once its nondegeneracy has been proved by the separate Hilbert-algebra density theorem. The net lies in that actual algebra, rather than only in its norm closure.

Here the concrete ultraweak assertion uses only its defining vector series. Suppose \(a_\alpha\to a\) strongly and \(\sup_\alpha\|a_\alpha\|,\|a\|\leq C\). For square-summable vector sequences \((u_n),(v_n)\), Cauchy–Schwarz gives
\[
\left|\sum_{n>N}\langle(a_\alpha-a)u_n,v_n\rangle\right|
\leq2C\left(\sum_{n>N}\|u_n\|^2\right)^{1/2}
\left(\sum_{n>N}\|v_n\|^2\right)^{1/2}.
\tag{BD7}
\]
The bound tends to zero uniformly in \(\alpha\). The finite initial sum tends to zero by strong convergence. Thus every defining vector-series functional tends to zero on \(a_\alpha-a\), for arbitrary nets, which is exactly concrete ultraweak convergence.

The construction supplies precisely the contraction and positive-contraction conclusions used from OA-FND-KD-07 Theorem 7.1. It does not prove normal-positive-map criteria, predual duality, compactness of dual balls, or Hilbert-algebra right-density. Those remain distinct inputs.
