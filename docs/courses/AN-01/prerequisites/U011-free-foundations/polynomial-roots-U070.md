# Polynomial division and all complex roots

*Selected AN-03 programme proof; CC0 1.0. Original ownership is retained. See [licence](https://creativecommons.org/publicdomain/zero/1.0/), [rights](notices/RIGHTS.md), and [selection history](notices/U070_SELECTION_HISTORY.md).*

The [scalar calculus and topology](metric-foundation-bridges.md), §§12–13, [finite algebra](stable-prerequisite-bridges.md), §§10.1–10.6, and [integration proofs](banach-foundation-bridges.md), §§15.0–15.1 and 16, supply the stated foundational inputs.

## Scalar polynomial division

For a field \(F\), every \(f,g\in F[z]\) with \(g\ne0\) has unique \(f=gq+r\), where \(r=0\) or \(\deg r<\deg g\).

**Proof of division.** Let \(e=\deg g\) and let \(b\ne0\) be its leading coefficient. If \(f=0\) or \(\deg f<e\), take \(q=0\) and \(r=f\). Otherwise let \(d=\deg f\), with leading coefficient \(a\ne0\), and subtract \((a/b)z^{d-e}g\) from \(f\). The leading terms cancel, so the difference is zero or has degree strictly below \(d\). Repeating this step terminates because the degree of a nonzero remainder decreases at every step. The sum of the subtracted monomials is \(q\), and the final difference is the required \(r\). This includes a constant divisor and the zero dividend. If \(f=gq+r=gq'+r'\) with both remainders zero or of degree below \(e\), then \(g(q-q')=r'-r\). A nonzero left side has degree at least \(e\), whereas the right side is zero or has degree below \(e\). Therefore \(q=q'\) and \(r=r'\).

## 9. Complex roots with all original coefficients retained

This selection proves the complex-root fact and full factorization, retaining every coefficient, leading factor and translated remainder. The original source’s later spectral and Bézout applications are outside this selection.

The scalar entry bases are real completeness, field arithmetic, finite polynomial arithmetic and degree induction, real differentiation and integration on compact intervals, and the finite-dimensional definitions in the supplied finite-algebra foundation. Absolute convergence and the required exponential differentiation are justified directly below. No root theorem, primary decomposition or general Cauchy integral theorem is used to prove its own prerequisite.

### 9.1. The actual exponential and a direction with any prescribed integer power

Define \(E(t)=\sum_{k=0}^{\infty}(it)^k/k!\) for real \(t\). On \(|t|\leq T\) the absolute series and its first derivative are uniformly convergent: once \(k+1>2T\), the ratio of successive absolute majorants is less than \(1/2\); finitely many earlier terms and the resulting geometric tail are included. To justify the derivative rule directly, finite partial sums obey their integral derivative formula. Uniform limits of the functions and derivatives let that formula pass to the limit on every compact interval, proving \(E'=iE\). Absolute convergence, finite binomial expansion and regrouping of the double series give
\[
 E(s)E(t)=\sum_{m\geq0}i^m
       \sum_{k=0}^m\frac{s^kt^{m-k}}{k!(m-k)!}
       =\sum_{m\geq0}\frac{i^m(s+t)^m}{m!}=E(s+t).              \tag{CR1}
\]
Conjugation of the actual series gives \(\overline{E(t)}=E(-t)\); hence \(E(t)\overline{E(t)}=E(0)=1\). Put \(C(t)=\operatorname{Re}E(t)\), \(S(t)=\operatorname{Im}E(t)\). Thus
\[
 C'=-S,\quad S'=C,\quad C(0)=1,\quad S(0)=0,\quad
                         C(t)^2+S(t)^2=1.                    \tag{CR2}
\]
There is a first positive zero \(t_0\) of \(C\), and \(0<t_0<2\). For existence, its actual series gives
\(C(2)=1-2+2/3+\sum_{k\geq3}(-1)^k2^{2k}/(2k)!\leq-1/3<0\):
the remaining terms are decreasing in absolute value, and each consecutive negative/positive pair has nonpositive sum. Continuity and the intermediate value property supply a zero in \((0,2)\). The intermediate value property follows directly from real completeness. For a continuous real function \(f\) with \(f(a)>0>f(b)\), let \(c=\sup\{x\in[a,b]:f(x)>0\}\). Positivity near \(a\) and negativity near \(b\) give \(a<c<b\). Points of that set approach \(c\), so continuity gives \(f(c)\geq0\). If \(f(c)>0\), continuity supplies a point of the set strictly to its right, a contradiction. Thus \(f(c)=0\). Reversing the signs covers the other case, and subtracting a requested intermediate value covers arbitrary endpoint values. Since \(C>0\) near zero, the closed nonempty zero set in a compact subinterval has a positive infimum that belongs to it by continuity. This gives \(t_0\); another change of sign before it would have supplied an earlier zero. Therefore \(C>0\) on \([0,t_0)\).

The integral \(S(t)=\int_0^t C(s)\,ds\) is strictly positive for \(0<t\leq t_0\). Formula (CR2) gives \(S(t_0)=1\). Also \(C\) decreases from one to zero there, because \(C'=-S<0\) on the interior. For any unit complex number \(a+ib\) in the first quadrant, the intermediate value property supplies \(t\in[0,t_0]\) with \(C(t)=a\), and positivity plus (CR2) gives \(S(t)=b\). Any unit complex number can be multiplied by one of \(1,-i,-1,i\) to lie in that quadrant. Since \(E(t_0)=i\), (CR1) then shows that it is \(E(t+j t_0)\) for some \(j\in\{0,1,2,3\}\). Thus every prescribed unit number \(d\) is \(E(\theta)\) for a real \(\theta\). For any positive integer \(q\),
\[
             c=E(\theta/q),\qquad |c|=1,\qquad c^q=d.           \tag{CR3}
\]
This proves the needed direction without assuming a root theorem for an arbitrary complex polynomial. The parameter \(t_0\) serves only this proof; no original circle, contour or Fourier constant is being changed.

For any positive real \(r\), there is a unique positive \(q\)-th root of \(r\). The continuous function \(x\mapsto x^q\) increases strictly on \([0,\infty)\), since for \(y>x\geq0\) its difference is
\((y-x)\sum_{j=0}^{q-1}y^{q-1-j}x^j>0\).
It is zero at zero and exceeds \(r\) at \(r+1\). The same intermediate value argument gives existence and the strict inequality gives uniqueness. These are the real roots used in the bounds below.

### 9.2. A minimum of the original polynomial modulus

Let the original nonconstant polynomial be
\[
       p(z)=\sum_{k=0}^N a_k z^k,\qquad
              N\geq1,\quad a_N\ne0,\quad
       A_0=\sum_{k=0}^{N-1}|a_k| .                            \tag{CR4}
\]
Its actual leading coefficient remains \(a_N\). For \(r=|z|\geq1\), the full reverse triangle inequality gives
\[
 |p(z)|\geq |a_N|r^N-\sum_{k=0}^{N-1}|a_k|r^k
            \geq r^{N-1}(|a_N|r-A_0).                         \tag{CR5}
\]
Choose
\[
 R=1+\frac{2A_0}{|a_N|}
              +\left(\frac{2(|a_0|+1)}{|a_N|}\right)^{1/N}.
                                                               \tag{CR6}
\]
For \(r\geq R\), (CR5) is at least \(|a_N|r^N/2\) and exceeds \(|a_0|+1\). Thus the global infimum is attained inside the original disk \(|z|\leq R\).

Here is the existence argument for the attained minimum. The nonempty set of values on that disk is bounded below by zero; real completeness defines its infimum \(b\). Choose original points \(z_j\) in the disk with \(|p(z_j)|<b+1/j\). A bounded sequence in a closed complex square has a convergent subsequence: repeatedly divide the square into four closed subsquares, retain one with infinitely many original points, and choose increasing original indices in the nested squares. Their diameters tend to zero, so completeness in each real coordinate gives a common limit. The disk is closed, hence its subsequence limit \(z_0\) belongs to it. Polynomial continuity follows directly from the full identity
\[
 p(z)-p(w)=(z-w)\sum_{k=1}^N a_k
                    \sum_{j=0}^{k-1}z^{k-1-j}w^j .             \tag{CR7}
\]
On any fixed disk its finite sum is bounded; thus the difference tends to zero with \(z-w\). Consequently \(|p(z_0)|=b\). By the strict outside bound and the available value \(|p(0)|=|a_0|\), this is a global minimum.

### 9.3. The exact translated coefficients force a zero

Suppose \(b_0=p(z_0)\ne0\). The complete finite binomial formula is
\[
 p(z_0+w)=\sum_{r=0}^N b_r w^r,\qquad
 b_r=\sum_{k=r}^N a_k\binom{k}{r}z_0^{\,k-r},\qquad b_N=a_N.
                                                               \tag{CR8}
\]
Let \(q\) be the smallest positive index with \(b_q\ne0\). It exists because \(b_N\ne0\); every intervening coefficient is exactly zero. Define the unit direction
\[
 d=-\frac{|b_q|b_0}{|b_0|b_q},\qquad
 c^q=d,\quad |c|=1,\qquad H=\sum_{r=q+1}^N|b_r|.                \tag{CR9}
\]
Existence of \(c\) is (CR3), with all original factors in \(d\). Put \(w=tc\). Choose \(t>0\), \(t<1\), with
\(|b_q|t^q<|b_0|\) and, if \(H>0\), \(tH<|b_q|/2\).
Such a choice follows from the proved positive real roots; for example take half of the minimum of \(1\), \((|b_0|/|b_q|)^{1/q}\) and \(|b_q|/(2H)\), omitting only the last bound when its actual denominator \(H\) is zero. Then
\[
 \begin{split}
 |p(z_0+tc)|
 &\leq |b_0+b_qt^qc^q|+\sum_{r=q+1}^N|b_r|t^r\\
 &= |b_0|-|b_q|t^q+\sum_{r=q+1}^N|b_r|t^r\\
 &\leq |b_0|-|b_q|t^q+Ht^{q+1}<|b_0| .                       
 \end{split} \tag{CR10}
\]
The middle equality uses \(b_qc^q=-|b_q|b_0/|b_0|\) and the strict bound on \(t^q\). The last inequality also holds when \(H=0\), since the full higher sum is then zero. This contradicts the global minimum. Hence \(p(z_0)=0\). Every nonconstant original complex polynomial has a root, with all its original coefficients and full translated remainder retained. \(\square\)

### 9.4. Full factorization, leading coefficient and multiplicities

For an arbitrary \(\alpha\in\mathbb C\), the full division identity is
\[
 p(z)=p(\alpha)+(z-\alpha)q_\alpha(z),\qquad
 q_\alpha(z)=\sum_{k=1}^N a_k
                    \sum_{j=0}^{k-1}z^{k-1-j}\alpha^j .         \tag{CR11}
\]
It follows from (CR7) with \(w=\alpha\). When \(p(\alpha)=0\), the quotient has degree \(N-1\) and exactly the same leading coefficient \(a_N\); its original finite coefficient sums are shown in (CR11). Applying the proved root theorem to each successive nonconstant quotient, and retaining every zero remainder, yields
\[
 p(z)=a_N\prod_{\ell=1}^N(z-\alpha_\ell)
      =a_N\prod_{\lambda\in Z(p)}(z-\lambda)^{m_\lambda},
 \qquad \sum_{\lambda\in Z(p)}m_\lambda=N .                    \tag{CR12}
\]
Here \(Z(p)\) is the finite set of distinct roots of the original polynomial, and \(m_\lambda\) counts its occurrences in the list, including repetitions. These multiplicities are intrinsic: in (CR8) centered at a root, the least index \(r\) with nonzero coefficient is exactly the largest power of \(z-\lambda\) dividing \(p\), since division at that power leaves a quotient with nonzero value at the root. The derivative identity \(p^{(r)}(\lambda)=r!b_r\), obtained by differentiating every finite term, gives the same characterization with its full factorial. Thus distinct factorizations have the same root set and multiplicities. A nonzero constant has no roots and is its original leading constant times the empty product. The zero polynomial has every complex number as a root and no finite multiplicity at any point; it is excluded from the degree-\(N\), \(a_N\ne0\) theorem. \(\square\)

