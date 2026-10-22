# Polynomial reciprocals and tempered fundamental solutions

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026.  Public domain (CC0).*

The Fourier transform turns a constant-coefficient differential equation into multiplication by a polynomial. Away from the zeros, division is ordinary division. At a zero, a reciprocal may have to be a distribution. This lesson constructs a tempered reciprocal for every nonzero complex polynomial and hence a tempered fundamental solution for every constant-coefficient polynomial operator.

Read [Schwartz Fourier foundations](../../prerequisites/schwartz-fourier-foundations.html), [Fundamental solutions and the directions an equation uses](../../src/fundamental-solutions-and-active-directions.md), and [Regularity and tempered growth](../../src/regularity-and-tempered-growth.md). The last lesson distinguishes local Fourier regularity from growth at infinity. Basic references are Bernstein [B] for the polynomial functional equation, Grubb [G] for tempered Fourier analysis, and Hörmander [H] for constant-coefficient equations. The [complete proof](polynomial-reciprocals-and-tempered-fundamental-solutions-formal.md) includes the algebraic finiteness argument, the continuation of distributions, and every step of the construction.

## 1. A reciprocal of the constant one

**Theorem 1.1.** Let \(P\) be any nonzero polynomial with complex coefficients on \(\mathbb R^n\). There is \(U\in\mathcal S'(\mathbb R^n)\) with
\[
                              P U=1. \tag{1}
\]
Therefore \(E=\mathcal F^{-1}U\) is tempered and
\[
                              P(D)E=\delta_0. \tag{2}
\]
The Fourier convention is \(\widehat f(\xi)=\int e^{-ix\cdot\xi}f(x)\,dx\), with \(D=-i\partial\).

The theorem includes repeated real zeros, nonreal coefficients, and polynomials independent of some variables. The polynomial \(P=0\) is excluded because its product with any distribution is zero. For a nonzero constant \(a\), take \(U=1/a\) and \(E=\delta_0/a\).

The construction uses polynomial differential operators acting on a parameter family. It never requires multiplying two singular distributions. Its consequence for compact data is also useful: if \(f\) is a compactly supported distribution, \(E*f\) is tempered and solves \(P(D)(E*f)=f\). The complete-proof Corollary 7.1 proves the required continuity on Schwartz tests.

## 2. Continuing a polynomial power

Conjugate the coefficients of \(P\) to obtain \(P^\#\), and put
\[
                             F=P P^\#.
\]
On real space, \(F=|P|^2\). For \(\operatorname{Re}s>0\), the function \(F^s\), set to zero on its zero set, has polynomial growth and defines a tempered distribution \(T(s)\). It depends holomorphically on \(s\). The complete-proof Lemmas 2.1 and 2.2 prove this with a common Schwartz seminorm on each compact parameter set.

Bernstein's functional equation supplies a nonzero scalar polynomial \(b(s)\) and a differential operator \(B(s)\), polynomial in \(s\) and in the real variables, such that
\[
                         b(s)F^s=B(s)F^{s+1}. \tag{3}
\]
Thus the family at \(s\) can be obtained from the family at \(s+1\). Each step can introduce finite-order poles from zeros of \(b\). Repeating the step continues \(T(s)\) meromorphically to every finite complex parameter.

At zero the continuation is holomorphic and equals one. Indeed \(F^s\to1\) almost everywhere as real \(s\downarrow0\), the zero set is null, and \(F^s\leq1+F\) for \(0<s\leq1\). Dominated convergence gives a finite limit on every Schwartz test. A finite-order pole would contradict that limit.

At \(s=-1\), take the constant Laurent coefficient:
\[
                T(s)=\sum_{\ell=-L}^{\infty}A_\ell(s+1)^\ell.
 \tag{4}
\]
The identity \(F T(s)=T(s+1)\) gives \(F A_0=1\), because the right side is holomorphic there with value one. Therefore
\[
                             U=P^\# A_0 \tag{5}
\]
proves (1). Every coefficient in (4) is tempered. This follows from the locally uniform Schwartz-seminorm bounds and the Cauchy formula for the parameter coefficients, as proved in the complete-proof Lemma 2.2.

## 3. Why the functional equation exists

Here is the finite algebraic mechanism behind (3). The full argument is in complete-proof Sections 3–6.

Work over the field \(\mathbb C(s)\), where the parameter is an indeterminate. Polynomial multiplication and ordinary differentiation generate the Weyl algebra. Its operators of total degree at most \(k\) have dimension
\[
                              \binom{k+2n}{2n}. \tag{6}
\]
The noncommutativity has the simple rule \([\partial_i,x_j]=\delta_{ij}\).

A nonzero finitely generated module over this algebra cannot have growth degree below \(n\). To see the key point, an operator of degree at most \(k\) which killed the degree-\(k\) part of a module would, after at most \(k\) commutators, give a nonzero scalar killing a nonzero generator. The complete-proof Theorem 5.2 expands those commutators and proves
\[
              \binom{k+2n}{2n}\leq(\dim M_k)(\dim M_{2k}). \tag{7}
\]
This forces growth degree at least \(n\).

For the cyclic module generated by the formal symbol \(F^s\), the degree is at most \(n\). If \(d=\deg F\), putting the derivatives over a common denominator \(F^k\) bounds the numerator degree by \((d+1)k\). Hence
\[
                         \dim M_k\leq\binom{(d+1)k+n}{n}. \tag{8}
\]
The degree is exactly \(n\). Its leading coefficient, multiplied by \(n!\), is a positive integer called its multiplicity.

Now the cyclic submodules generated by
\[
                             F^s,\ F^{s+1},\ F^{s+2},\ldots
\]
form a descending chain. Every strict inclusion consumes at least one unit of multiplicity, so the chain must have two consecutive equal terms. That equality expresses one power as a polynomial differential operator applied to the next power, with rational dependence on \(s\). Change the parameter back and clear its scalar denominators. The result is (3).

The complete proof supplies the monomial counting, finite-generation and exact-sequence arguments that justify these multiplicities. Thus the chain argument has no assumed finiteness theorem hidden inside it.

## 4. Three reciprocals at real zeros

### Example 1: a simple real zero

For \(P(\xi)=\xi\) on the line, define
\[
 \left\langle\operatorname{pv}\frac1\xi,\phi\right\rangle
       =\int_0^\infty\frac{\phi(t)-\phi(-t)}t\,dt. \tag{9}
\]
The numerator is \(O(t)\) near zero by the mean value theorem, and both tests decrease rapidly at infinity. These bounds also give continuity in a finite set of Schwartz seminorms. Substituting \(\xi\phi\) gives
\[
 \left\langle \xi\,\operatorname{pv}\frac1\xi,\phi\right\rangle
       =\int_0^\infty(\phi(t)+\phi(-t))\,dt
       =\int_{\mathbb R}\phi(t)\,dt.
\]
Thus (9) is a tempered reciprocal. In physical space, \(E(x)=\frac i2\operatorname{sgn}x\) is a tempered fundamental solution of \(D=-i\partial_x\), because \(\partial_x\operatorname{sgn}x=2\delta_0\).

### Example 2: a repeated real zero

For \(P(\xi)=\xi^2\), define the finite part by
\[
 \left\langle\operatorname{fp}\frac1{\xi^2},\phi\right\rangle
    =\lim_{\epsilon\downarrow0}
       \left(\int_{|\xi|>\epsilon}\frac{\phi(\xi)}{\xi^2}\,d\xi
                         -\frac{2\phi(0)}\epsilon\right). \tag{10}
\]
Taylor subtraction shows that the limit exists. More precisely it equals
\[
 \begin{aligned}
 &\int_{|\xi|<1}
       \frac{\phi(\xi)-\phi(0)-\xi\phi'(0)}{\xi^2}\,d\xi\\
 &\qquad+\int_{|\xi|\geq1}\frac{\phi(\xi)}{\xi^2}\,d\xi-2\phi(0).
 \end{aligned}
 \tag{11}
\]
The first integral is bounded by \(\sup_{[-1,1]}|\phi''|\), and the second by \(2\sup|\phi|\). This proves tempered continuity. Replacing \(\phi\) by \(\xi^2\phi\) in (10) gives exactly \(\int\phi\), so the finite part is a reciprocal of \(\xi^2\).

![For the Gaussian test, subtracting its value at zero removes the quadratic reciprocal singularity; the quotient has limit minus one at zero.](figures/finite-part-test-subtraction.png)

*Figure 1. The test is \(\phi(\xi)=e^{-\xi^2}\). The three panels show \(\phi\), the subtracted test \(\phi-1\), and \((\phi-1)/\xi^2\), extended at zero by \(-1\). These are ordinary functions illustrating (11), not a graph of a distribution. Integration by parts gives the exact pairing \(\langle\operatorname{fp}(1/\xi^2),e^{-\xi^2}\rangle=-2\sqrt\pi\).*

To verify the last value, the odd linear Taylor term vanishes and (10) equals the integral of \((e^{-\xi^2}-1)/\xi^2\). Its boundary terms in integration by parts vanish at both zero and infinity. Differentiating the numerator gives \(-2\xi e^{-\xi^2}\), so the integral is \(-2\int e^{-\xi^2}\,d\xi=-2\sqrt\pi\). The Gaussian integral follows by squaring the positive integral and using polar coordinates in the plane.

### Example 3: a complex linear zero

For \(P(\xi_1,\xi_2)=\xi_1+i\xi_2\), the ordinary function
\[
                     U(\xi)=\frac{\xi_1-i\xi_2}{\xi_1^2+\xi_2^2}
 \tag{12}
\]
is locally integrable: its modulus is \(1/|\xi|\), and polar area measure cancels that singular power near zero. It decreases at infinity, so it is tempered. Its product with \(P\) is one almost everywhere, hence distributionally.

Here \(F=|\xi|^2\). Its power family has a pole at \(s=-1\), but multiplication by \(P^\#\) removes that pole. Solution 8 computes the residue and verifies that (5) gives exactly (12).

## 5. What existence does and does not select

If \(U_1,U_2\) solve (1), their difference \(W\) satisfies \(P W=0\), and it is supported on the real zero set of \(P\). This follows by smooth division on every open set where \(P\ne0\). Support on the zero set alone is insufficient: multiplication can detect normal delta derivatives.

If \(P\) has no real zeros, the tempered reciprocal is unique. For example \(P=1+|\xi|^2\) has the smooth reciprocal \((1+|\xi|^2)^{-1}\). When real zeros are present, choosing boundary conditions or support can select a particular inverse.

The theorem supplies tempered growth. The regular inverse construction supplies the local weight \(S_P\). These are distinct conclusions. The degenerate diffusion example in [Regularity and tempered growth](../../src/regularity-and-tempered-growth.md) has no inverse with both properties, even though each existence theorem applies.

## 6. Exercises with complete solutions

### Exercise 1: constants and the Fourier normalization — 5 points

For \(P=a\ne0\), determine both inverses in (1) and (2). State the convention in zero dimensions.

### Solution 1

The frequency distribution is the constant \(U=1/a\), so \(\mathcal F^{-1}U=\delta_0/a\). There is no factor of \(2\pi\), since the inverse transform already contains \((2\pi)^{-n}\) and sends the constant one to delta. In zero dimensions integration and Fourier transformation are the identity on scalars, and the same answer is scalar division.

### Exercise 2: ambiguity at a simple zero — 10 points

Show that every distribution \(W\) on the line with \(\xi W=0\) equals \(c\delta_0\). Deduce all tempered reciprocals of \(P(\xi)=\xi\).

### Solution 2

Choose \(\chi\in C_c^\infty\) equal to one near zero. For every compact test \(\phi\), the function \(\phi-\phi(0)\chi\) vanishes at zero and equals \(\xi\psi\) for a compact smooth \(\psi\); smoothness at zero follows from the integral Taylor formula. Therefore
\[
 \langle W,\phi\rangle=\phi(0)\langle W,\chi\rangle+\langle\xi W,\psi\rangle
                        =c\phi(0).
\]
Thus \(W=c\delta_0\). The difference of two tempered reciprocals has this form. Conversely \(\xi\delta_0=0\), so they are exactly \(\operatorname{pv}(1/\xi)+c\delta_0\). The equality first established on compact tests is equality of tempered distributions because compact smooth functions are dense in the Schwartz topology, as proved in the Fourier foundation reading.

### Exercise 3: a repeated zero in physical space — 15 points

Prove directly that \(E(x)=-|x|/2\) is a tempered fundamental solution of \(D^2\). Also show that \(\delta'_0\) is annihilated by \(\xi^2\), whereas \(\delta''_0\) is not.

### Solution 3

The locally integrable function \(|x|\) has linear growth and is tempered. Integration by parts on the positive and negative half-lines gives \(\partial_x|x|=\operatorname{sgn}x\), and one more integration gives \(\partial_x^2|x|=2\delta_0\). Since \(D^2=-\partial_x^2\), (2) follows. For compact tests,
\[
 \langle \xi^2\delta'_0,\phi\rangle=-(\xi^2\phi)'(0)=0,\qquad
 \langle \xi^2\delta''_0,\phi\rangle=(\xi^2\phi)''(0)=2\phi(0).
\]
Thus \(\xi^2\delta''_0=2\delta_0\). All three delta derivatives are supported at the same point, which illustrates why support alone does not characterize the ambiguity.

### Exercise 4: finding the scalar by commutators — 10 points

In one variable put \(Q=x^2\partial+3x\partial^2+5\). Compute \((\operatorname{ad}\partial)^2(\operatorname{ad}x)Q\), and explain its role in the dimension inequality.

### Solution 4

Using \([x,\partial]=-1\),
\[
 [x,Q]=-x^2-6x\partial,\quad
 [\partial,[x,Q]]=-2x-6\partial,\quad
 [\partial,[\partial,[x,Q]]]=-2.
\]
If this degree-three operator killed the degree-three part of a nonzero module with a generator \(m\), expand the three commutators on \(m\). Every term contains \(Q\) applied to a word of length at most three acting on \(m\), so every term is zero. But their sum is \(-2m\ne0\), a contradiction. This is the scalar-detection step of complete-proof Theorem 5.2.

### Exercise 5: a module of the smallest possible growth — 10 points

Let the one-variable Weyl algebra act on \(K[x]\) by multiplication and differentiation. Use the generator \(1\) to compute the growth degree and multiplicity, and show that the module has no proper nonzero submodule.

### Solution 5

Its degree-\(k\) filtered part is the polynomials of degree at most \(k\), with dimension \(k+1\). Thus \(d=1\) and \(e=1\). A nonzero submodule contains a nonzero polynomial. Differentiating as many times as its degree yields a nonzero constant, since the field has characteristic zero. Scalar division gives \(1\), and multiplication by powers of \(x\) gives every polynomial. The chain therefore has length one, agreeing with the multiplicity bound.

### Exercise 6: a functional equation with repeated factors — 15 points

For \(F(x)=x^d\), \(d\geq1\), find a scalar polynomial \(b(s)\) for which \(\partial_x^d F^{s+1}=b(s)F^s\) holds formally. For \(d=2\), explain why a zero of \(b\) need not be an actual pole of \(T(s)\).

### Solution 6

Differentiating \(x^{d(s+1)}\) \(d\) times gives
\[
 b(s)=\prod_{j=1}^d(ds+j),\qquad
                    \partial_x^d F^{s+1}=b(s)F^s. \tag{13}
\]
This is a formal differential identity, or an ordinary identity after choosing a local logarithm off zero. For \(d=2\), \(b(s)=(2s+1)(2s+2)\). The apparent singularity at \(s=-1\) is removable for \(T(s)=|x|^{2s}\). To see this, subtract \(\phi(0)+x\phi'(0)\) on \(|x|<1\). The remaining integral is holomorphic for \(\operatorname{Re}s>-3/2\), while the subtracted constant contributes \(2\phi(0)/(2s+1)\), and the odd term contributes zero. The outer integral is holomorphic on every bounded parameter set by Schwartz decay. Thus the only pole in this strip is at \(-1/2\); at \(-1\) the expression equals (11). Scalar factors in the recurrence give possible poles, with cancellations permitted.

### Exercise 7: why the value at zero is enough — 15 points

Suppose a meromorphic tempered family \(T(s)\) continues \(F^s\), for a nonzero nonnegative polynomial \(F\), and satisfies \(F T(s)=T(s+1)\). Prove \(T(0)=1\) and \(F A_\ell=0\) for every negative Laurent coefficient at \(-1\).

### Solution 7

The zero set of \(F\) is null. For real \(s\downarrow0\), dominated convergence with \(|F^s|\leq1+F\) gives the weak limit one on every Schwartz test. If a most negative Laurent coefficient at zero were nonzero, choose a test on which it is nonzero. Its scalar pairing would diverge on this real approach. There is therefore no pole at zero, and its value is one. The right side of \(F T(s)=T(s+1)\) is now holomorphic near \(-1\), so every negative coefficient on the left is zero: \(F A_\ell=0\) for \(\ell<0\). The constant coefficient is \(F A_0=1\). No assertion that the individual negative coefficients vanish is required.

### Exercise 8: the residue at a complex linear zero — 20 points

In two dimensions take \(F(\xi)=|\xi|^2\). Compute the residue of \(T(s)=F^s\) at \(s=-1\). Show that multiplication by \(\xi_1-i\xi_2\) removes the pole and gives (12).

### Solution 8

For a Schwartz test put \(g(r)=\int_0^{2\pi}\phi(r\cos\theta,r\sin\theta)\,d\theta\). Taylor expansion and the vanishing angular integral of the linear term give \(g(r)=2\pi\phi(0)+O(r^2)\), with the remainder controlled by the second derivatives on the unit ball. The inner radial integral is
\[
 \int_0^1 r^{2s+1}(g(r)-2\pi\phi(0))\,dr
                         +\frac{\pi\phi(0)}{s+1}. \tag{14}
\]
Its first term is holomorphic for \(\operatorname{Re}s>-2\). The radial integral over \(r\geq1\) is holomorphic on bounded parameter sets by Schwartz decay. Thus
\[
                         \operatorname{Res}_{s=-1}T(s)=\pi\delta_0.
\]
Multiplication by \(\xi_1-i\xi_2\) kills this residue. More directly the function \((\xi_1-i\xi_2)|\xi|^{2s}\) has modulus \(r^{2\operatorname{Re}s+1}\); with area measure it is locally integrable for \(\operatorname{Re}s>-3/2\), including a neighborhood of \(-1\), and its parameter derivatives are dominated there. Hence this multiplied family is holomorphic at \(-1\) and takes the value \((\xi_1-i\xi_2)/|\xi|^2\). Its constant Laurent coefficient is exactly the \(U\) in (5), proving (12).

## References

- **[G]** Gerd Grubb, *Distributions and Operators*, freely readable lecture chapters, especially Chapter 5 on Fourier transformation. [Author's lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm). The Fourier proofs used here are also supplied in the linked foundation reading.
- **[B]** I. N. Bernstein, “The analytic continuation of generalized functions with respect to a parameter,” *Functional Analysis and Its Applications* **6** (1972), 273–285. [Author-hosted article](https://www.math.tau.ac.il/~bernstei/Publication_list/publication_texts/Bern-a-cont-FAN.pdf); [bibliographic record](https://www.mathnet.ru/php/archive.phtml?jrnid=faa&option_lang=eng&paperid=2532&wshow=paper).
- **[H]** Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983; 2005 reprint.
