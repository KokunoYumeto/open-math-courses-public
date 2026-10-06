# The L-function of a cusp form

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A modular transformation becomes a functional equation of a Mellin transform. The vanishing of a cusp form supplies decay at both ends of the integral, so its completed L-function is entire. We first prove this for an arbitrary cusp form. The eigenform hypothesis enters when we ask for an Euler product.

Throughout, \(k\ge2\) is even, \(q=e^{2\pi iz}\), and
\[
f(z)=\sum_{n\ge1}a_nq^n\in S_k(SL_2(\mathbb Z)).
\]
A zero space at a particular weight causes no exception. We use Euler's Gamma integral
\(\Gamma(s)=\int_0^\infty e^{-u}u^{s-1}\,du\) for \(\operatorname{Re}s>0\), its meromorphic continuation, and the fact that \(1/\Gamma\) is entire. Their proofs are in The Gamma function and Stirling's formula, Theorems 1.1–1.2. The coefficient bound comes from lesson 7, Theorem 2.1. The transformation law was developed in lesson 4. The recurrences and normalized Hecke eigenbasis come from lesson 8, Theorems 2.1 and 4.2.

## 1. The initial Dirichlet series

Define
\[
L(f,s)=\sum_{n\ge1}a_nn^{-s},\qquad n^{-s}=\exp(-s\log n).
\]

**Theorem 1.1 (absolute convergence).** This series converges absolutely for \(\operatorname{Re}s>k/2+1\), and locally uniformly there. It defines a holomorphic function on that half-plane.

**Proof.** The elementary cusp-form estimate is \(|a_n|\le C_fn^{k/2}\). If \(\operatorname{Re}s\ge k/2+1+\delta\), where \(\delta>0\), then
\[
|a_nn^{-s}|\le C_fn^{-1-\delta}.
\]
This summable numerical majorant is independent of the imaginary part. It gives uniform convergence on the entire closed half-plane. Each term is entire, so local uniform convergence proves holomorphy. \(\square\)

This domain suffices for the integral argument. A sharper coefficient estimate will improve it without changing the continuation proof.

## 2. Decay, completion and reflection

Put \(F(y)=f(iy)\) and \(\epsilon=i^k=(-1)^{k/2}\). The earlier coefficient estimate gives, for \(y\ge1\),
\[
|F(y)|\le C_f\sum_{n\ge1}n^{k/2}e^{-2\pi ny}\le A_fe^{-\pi y}.
\tag{2.1}
\]
The last inequality follows from \(2ny\ge n+y\). For each nonnegative integer \(j\), termwise differentiation of the normally convergent Fourier series similarly gives
\[
|(y\partial_y)^jF(y)|\le A_j(1+y)^j e^{-\pi y}.
\]
Indeed this derivative is a finite sum of terms \(y^h\partial_y^hF\), with \(0\le h\le j\); each is bounded by \((2\pi y)^h\sum n^{k/2+h}e^{-2\pi ny}\), and the same inequality extracts \(e^{-\pi y}\) from the summable series in \(n\).

The defining transformation under \(S\), evaluated at \(iy\), gives
\[
\begin{gathered}
F(1/y)=\epsilon y^kF(y),\\
F(y)=\epsilon y^{-k}F(1/y).
\end{gathered}
\tag{2.2}
\]
Differentiating this identity with \(y\partial_y\) gives a finite linear combination of \(y^{-k}((t\partial_t)^hF)(t)\), with \(t=1/y\). Thus every such derivative at zero has an exponential factor \(e^{-\pi/y}\) times a fixed power of \(1/y\). These estimates establish both ends of
\[
\begin{aligned}
I_f(s)&=\int_0^\infty F(y)y^{s-1}\,dy\\
&=\int_{\mathbb R}F(e^x)e^{sx}\,dx.
\end{aligned}
\tag{2.3}
\]
For \(\sigma\) in a bounded real interval, the function \(e^{\sigma x}F(e^x)\), all its derivatives in \(x\), and all their products by powers of \(x\) are integrable and tend to zero at both ends, with bounds uniform in \(\sigma\). At positive infinity this follows from \(e^{-\pi e^x}\); at negative infinity it follows from \(e^{-\pi e^{-x}}\). Each dominates every fixed exponential and polynomial in \(x\). In particular the integral and its derivatives in \(s\) converge locally uniformly, proving entireness.

**Theorem 2.1 (continuation and functional equation).** The completion
\[
\Lambda(f,s)=(2\pi)^{-s}\Gamma(s)L(f,s)
\]
extends from the half-plane of Theorem 1.1 to the entire function \(I_f(s)\). It is bounded on every closed vertical strip and satisfies
\[
\Lambda(f,s)=\epsilon\Lambda(f,k-s).
\tag{2.4}
\]
In fact it decreases to every polynomial order as \(|\operatorname{Im}s|\to\infty\), uniformly on a fixed strip. The uncompleted function \(L(f,s)\) is entire as well.

**Proof.** On \(\sigma>k/2+1\), the finite absolute majorant
\[
\begin{gathered}
\sum_{n\ge1}|a_n|\int_0^\infty e^{-2\pi ny}y^{\sigma-1}\,dy\\
=\Gamma(\sigma)(2\pi)^{-\sigma}\sum_{n\ge1}|a_n|n^{-\sigma}.
\end{gathered}
\]
permits termwise integration by lesson 01, Lemma 0.3(1). Euler's integral then identifies \(I_f(s)\) with the stated completion. Its entire extension has already been proved by the explicit estimates for (2.3).

Reflect \(x\mapsto-x\) in the absolutely convergent logarithmic integral. Equation (2.2) gives
\(F(e^{-x})e^{-sx}=\epsilon F(e^x)e^{(k-s)x}\).
This proves (2.4) for every \(s\) directly. Keeping only the positive half of that same integral also gives the useful split formula
\[
\Lambda(f,s)=A_f(s)+\epsilon A_f(k-s),\qquad
A_f(s)=\int_1^\infty F(y)y^{s-1}\,dy.
\tag{2.5}
\]
For real \(a\le\operatorname{Re}s\le b\), it follows that
\[
\begin{gathered}
B(y)=|F(y)|\bigl(y^{b-1}+y^{k-a-1}\bigr),\\
|\Lambda(f,s)|\le\int_1^\infty B(y)\,dy<\infty.
\end{gathered}
\tag{2.6}
\]
For the stronger decay, integrate \(e^{\sigma x}F(e^x)e^{itx}\) by parts \(M\) times. The boundary terms vanish by the estimates above, and the \(L^1\) norm of the \(M\)-th derivative is uniformly bounded for \(a\le\sigma\le b\). Therefore \(\Lambda(f,\sigma+it)=O_M(|t|^{-M})\) for \(|t|\ge1\). Finally \((2\pi)^s\Lambda(f,s)/\Gamma(s)\) is entire by the earlier reciprocal-Gamma proof and agrees with the initial \(L\)-series. \(\square\)

At each nonpositive integer, the reciprocal Gamma zero forces a zero of \(L(f,s)\). A different zero is forced at the centre when \(\epsilon=-1\).

**Corollary 2.2 (central vanishing).** If \(k\equiv2\pmod4\), then \(\Lambda(f,k/2)=L(f,k/2)=0\).

**Proof.** Equation (2.4) at \(s=k/2\) equates the completed value to its negative. Euler's integral gives \(\Gamma(k/2)>0\), and the other completion factor is nonzero, so the uncompleted value is zero too. \(\square\)

For \(\epsilon=+1\), the central equation is an identity and supplies no nonvanishing assertion. The proof above applies to every cusp form, independently of an Euler product or an optimal coefficient estimate.

## 3. Eisenstein series and the constant term

For even \(k\ge4\), use the constant-one normalization from lesson 4:
\[
E_k(z)=1+c_k\sum_{n\ge1}\sigma_{k-1}(n)q^n,\qquad c_k=-\frac{2k}{B_k}.
\]
Set \(h_k(y)=E_k(iy)-1\).

**Theorem 3.1 (Eisenstein Dirichlet series).** The series of positive Fourier coefficients is
\[
L(E_k,s)=\sum_{n\ge1}a_n(E_k)n^{-s}
=c_k\zeta(s)\zeta(s-k+1)\qquad(\operatorname{Re}s>k).
\tag{3.1}
\]

**Proof.** For \(\sigma>k\),
\[
\sum_{d,m\ge1}d^{k-1}(dm)^{-\sigma}
=\left(\sum_{m\ge1}m^{-\sigma}\right)
 \left(\sum_{d\ge1}d^{-(\sigma-k+1)}\right)<\infty.
\]
Absolute convergence permits regrouping by \(n=dm\). For a fixed \(n\), the sum over \(d\mid n\) is \(\sigma_{k-1}(n)\). Multiply by \(c_k\) to obtain (3.1). \(\square\)

Removing a constant Fourier coefficient does not produce a cusp form. The Mellin integral of \(h_k\) initially converges only for \(\operatorname{Re}s>k\); its continuation retains an explicit contribution from that constant.

**Proposition 3.2 (regularized Eisenstein completion).** Put \(\epsilon=i^k\) and
\[
A_k(s)=\int_1^\infty h_k(y)y^{s-1}\,dy.
\]
Then
\[
\Lambda(E_k,s)=A_k(s)+\epsilon A_k(k-s)+\frac{\epsilon}{s-k}-\frac1s.
\tag{3.2}
\]
It has exactly two simple poles, at \(0,k\), of residues \(-1,\epsilon\), and satisfies \(\Lambda(E_k,s)=\epsilon\Lambda(E_k,k-s)\) meromorphically.

**Proof.** The divisor formula gives polynomial coefficient growth, so \(h_k\) and its derivatives decay exponentially at infinity. Hence \(A_k\) is entire. Modularity gives
\[
h_k(1/y)=\epsilon y^kh_k(y)+\epsilon y^k-1.
\]
For \(\operatorname{Re}s>k\), the substitution \(y=1/t\) below one therefore gives
\[
\int_0^1h_k(y)y^{s-1}\,dy
=\epsilon A_k(k-s)+\epsilon\int_1^\infty y^{k-s-1}\,dy
-\int_1^\infty y^{-s-1}\,dy
=\epsilon A_k(k-s)+\frac{\epsilon}{s-k}-\frac1s.
\]
Absolute termwise integration, justified by Theorem 3.1 and Euler's integral, identifies the full initial Mellin integral with \((2\pi)^{-s}\Gamma(s)L(E_k,s)\). This proves (3.2). Its integral terms are entire, and \(k\ne0\), so neither displayed pole can cancel. Replacing \(s\) by \(k-s\), multiplying by \(\epsilon\), and using \(\epsilon^2=1\) verifies the functional equation, including its rational terms. \(\square\)

### 3.1. The full weight-four calculation

Since \(B_4=-1/30\), \(c_4=240\). The divisor sums at \(1,2,3,4\) are \(1,9,28,73\), so
\[
E_4=1+240q+2160q^2+6720q^3+17520q^4+\cdots,
\]
\[
L(E_4,s)=240\zeta(s)\zeta(s-3),\qquad
\Lambda(E_4,s)=A_4(s)+A_4(4-s)+\frac1{s-4}-\frac1s.
\tag{3.3}
\]
The uncompleted product has possible poles at \(1,4\). The zero \(\zeta(-2)=0\) cancels the pole at one, so its only pole is at four. Its residue there is \(240\zeta(4)=8\pi^4/3\). The completion also has a pole at zero. Using \(\Gamma(4)=6\), \(\zeta(4)=\pi^4/90\), \(\zeta(0)=-1/2\), and \(\zeta(-3)=1/120\), we check
\[
\operatorname*{Res}_{s=4}\Lambda(E_4,s)
=240(2\pi)^{-4}\Gamma(4)\zeta(4)=1,
\]
\[
\operatorname*{Res}_{s=0}\Lambda(E_4,s)=240\zeta(0)\zeta(-3)=-1.
\]
Both calculations agree with the integral formula. In particular, \(\int_0^\infty(E_4(iy)-1)y^{s-1}\,dy\) is not an entire Mellin integral: the constant term at the opposite cusp survives in its small-\(y\) asymptotic.

The zeta facts just used have complete programme proofs in Poisson summation, theta, and the functional equation: Corollary 3.2 gives the pole and \(\zeta(0)\), Theorem 3.3 gives the negative even zeros, and Theorem 4.2 and Example 4.3 give the integer values. Its completed zeta is \(\pi^{-s/2}\Gamma(s/2)\zeta(s)\); this differs from the modular-form completion \((2\pi)^{-s}\Gamma(s)L(f,s)\) used here.

## 4. Euler factors and the centre

Assume now that \(f\) is a simultaneous Hecke eigenform, normalized by \(a_1=1\). The coefficient-of-\(q\) identity gives \(T_nf=a_nf\). Lesson 8 proves
\[
a_{mn}=a_ma_n\quad((m,n)=1),\qquad
a_{p^{r+1}}=a_pa_{p^r}-p^{k-1}a_{p^{r-1}}\quad(r\ge1).
\tag{4.1}
\]

**Proposition 4.1 (Euler product).** In the half-plane of Theorem 1.1,
\[
L(f,s)=\prod_p\frac1{1-a_pp^{-s}+p^{k-1-2s}}.
\tag{4.2}
\]
If \(\alpha_p,\beta_p\) are the roots of \(X^2-a_pX+p^{k-1}\), its local factor is \((1-\alpha_pp^{-s})^{-1}(1-\beta_pp^{-s})^{-1}\).

**Proof.** Set \(a_{p^0}=1\). Multiplying coefficient by coefficient and using (4.1) gives
\[
(1-a_pX+p^{k-1}X^2)\sum_{r\ge0}a_{p^r}X^r=1.
\tag{4.3}
\]
This formal identity is also analytic at \(X=p^{-s}\) in our initial domain, because the coefficient bound makes the series absolutely convergent. In particular, the denominator is nonzero there.

For any finite set of primes, multiply these absolutely convergent series and use coprime multiplicativity. The result is the sum of \(a_nn^{-s}\) over integers supported on those primes. As the sets increase to all primes, the omitted tail tends to zero by absolute convergence of the full Dirichlet series. This proves (4.2). Moreover
\(\sum_p(|a_p|p^{-\sigma}+p^{k-1-2\sigma})<\infty\) for \(\sigma>k/2+1\). Thus the product converges absolutely. Factoring its denominator proves the last assertion. \(\square\)

An arbitrary cusp form has the continuation above but need not have this product. For example, a sum of two normalized eigenforms has first coefficient two; a product whose coefficient at \(n=1\) is one cannot equal that series.

The unitary normalization is
\[
L_{\mathrm u}(f,s)=L\bigl(f,s+(k-1)/2\bigr),\qquad
\Lambda_{\mathrm u}(f,s)=\Lambda\bigl(f,s+(k-1)/2\bigr).
\]
Then
\[
\Lambda_{\mathrm u}(f,s)=\epsilon\Lambda_{\mathrm u}(f,1-s).
\tag{4.4}
\]
The classical centre \(k/2\) becomes \(1/2\). The local parameters become \(\alpha_pp^{-(k-1)/2},\beta_pp^{-(k-1)/2}\), whose product is one.

## 5. The Ramanujan–Petersson input

We state the deep theorem with its hypotheses. If \(f\) is a normalized primitive holomorphic cusp form of integer weight \(k\ge2\) on \(\Gamma_0(N)\) with Dirichlet character \(\chi\), then, for \(p\nmid N\), both roots of
\[
X^2-a_p(f)X+\chi(p)p^{k-1}
\]
have modulus \(p^{(k-1)/2}\). In particular,
\[
|a_p(f)|\le2p^{(k-1)/2}.
\tag{5.1}
\]
This is Deligne, *La conjecture de Weil I*, Theorem (8.2). It is stated here, not proved. The source writes the transformation character as \(\chi(a)^{-1}\); this equals our \(\chi(d)\), because \(ad\equiv1\pmod N\). The written Deligne construction lesson, Lemma 4.1 and Proposition 4.2, proves the passage from projective purity to parabolic cohomology under its stated Leray, multiplication, and compactification hypotheses; Theorem 4.3 then proves the coefficient bound from the root statement. Its Theorem 1.1 still states the representation construction, and Section 4 imports the projective Weil theorem. These are the exact geometric inputs retained here.

At level one no smaller positive level exists, so every normalized eigenform is primitive and the theorem applies at every prime. Self-adjointness also makes \(a_p\) real. Here the bound and the root assertion are equivalent: a real quadratic with constant \(p^{k-1}>0\) and \(|a_p|\le2p^{(k-1)/2}\) has conjugate roots of that modulus, or repeated real roots at the endpoints. For a general character we retain the full root statement; a numerical bound on a complex trace alone does not establish it.

Expanding a local factor gives
\[
a_{p^r}=\sum_{j=0}^r\alpha_p^j\beta_p^{r-j},\qquad
|a_{p^r}|\le(r+1)p^{r(k-1)/2}.
\]
Multiplicativity yields \(|a_n|\le d(n)n^{(k-1)/2}\), where \(d(n)\) counts divisors. Thus, for \(\sigma>(k+1)/2\),
\[
\sum_{n\ge1}|a_n|n^{-\sigma}
\le\sum_{n\ge1}d(n)n^{-(\sigma-(k-1)/2)}
=\zeta\bigl(\sigma-(k-1)/2\bigr)^2<\infty.
\]
The improved domain is \(\operatorname{Re}s>(k+1)/2\), or \(\operatorname{Re}s>1\) in unitary normalization. The earlier continuation and functional equation needed only the elementary coefficient bound.

Theorem (8.2) assumes \(k\ge2\). Deligne's following Remark (8.3) records the weight-one bound by a different argument with Serre. This does not extend the stated cohomological proof to weight one, nor supply a Ramanujan assertion for Maass forms.


**Frobenius convention in the original proof.** For readers following the geometric input, let \(q\) be the size of the finite field. A Tate twist must retain its sign. Deligne's original §§1.15 and 2.2 distinguish arithmetic Frobenius from its inverse, geometric Frobenius. Arithmetic Frobenius acts by \(q\) on the roots-of-unity line, so geometric Frobenius acts on \(\mathbf Q_\ell(r)\) by \(q^{-r}\).

There is a transposed twist on [the original printed page 300](https://www.numdam.org/item/PMIHES_1974__43__273_0/), equations (7.1.5) and (7.1.5'). There \(n=2m+1\) and \(d=n+1\); the displayed \(\mathbf Q_\ell(n-m)\) would have eigenvalue \(q^{-d/2}\), whereas the next sentence needs \(q^{d/2}\). The consistent twist is
\[
\mathbf Q_\ell(m-n),\qquad q^{n-m}=q^{d/2}.
\]
Its type can also be checked directly. A nonzero vanishing cycle fixed by geometric Frobenius in \(H^n(m)\) determines an untwisted line \(L\cong\mathbf Q_\ell(-m)\) in \(H^n\). Pairing with that line in the intersection pairing \(H^n\otimes H^n\to\mathbf Q_\ell(-n)\) takes values in
\[
L^\vee\otimes\mathbf Q_\ell(-n)
\cong\mathbf Q_\ell(m-n).
\]
The local specialization sequence identifies this line as the boundary quotient used at that step. Thus the corrected twist supplies the claimed eigenvalue. This convention check retains the local specialization and duality inputs; it does not prove those geometric results or replace the Weil theorem stated above.

**Specialization and the zero-cycle case.** The twist can also be checked in the full specialization sequence. Work in the one-node situation of Deligne's Section 4: a proper flat morphism over a strictly henselian trait, with a smooth geometric generic fibre, a special fibre smooth except at one ordinary quadratic singularity, and pure relative dimension \(n=2m+1\). Assume \(\ell\) is invertible on the trait. Write \(A^i=H^i(X_s,\mathbf Q_\ell)\) and \(B^i=H^i(X_{\bar\eta},\mathbf Q_\ell)\). Use the geometric specialization theorem as an input. With the global vanishing cycle \(\delta\in B^n(m)\), it gives the following sequence, continued from the first line to the second:

\[
\begin{gathered}
0\longrightarrow A^n\xrightarrow{\mathrm{sp}}B^n
\xrightarrow{b}\mathbf Q_\ell(m-n),\\
\mathbf Q_\ell(m-n)\xrightarrow{\partial}A^{n+1}
\xrightarrow{\mathrm{sp}}B^{n+1}\longrightarrow0.
\end{gathered}
\]

Here \(b(v)=\langle v,\delta\rangle\). Indeed, pairing an element of \(B^n\) with an element of \(B^n(m)\) takes values in \(\mathbf Q_\ell(-n)(m)=\mathbf Q_\ell(m-n)\). This agrees with Deligne's equation (4.3.3). The corresponding summary in [SGA7 II, Exposé XV, Theorem 3.4(ii), printed page 196](https://publications.ias.edu/sites/default/files/Number12.pdf#page=204) prints \(\Lambda(n-m)\); its own cycle and duality calculations require \(\Lambda(m-n)\) in that pairing target.

Exactness now gives two distinct cases. If \(\delta\ne0\), the nondegenerate Poincaré pairing supplies a vector with \(b(v)\ne0\). Since the target is one-dimensional, \(b\) is surjective. Hence \(\partial=0\), the next specialization map is an isomorphism, and the image of the first one is exactly \(\delta^\perp\). If \(\delta=0\), then \(b=0\): the first specialization map is an isomorphism, while \(\partial\) injects the Tate line as the kernel of the next specialization map. The local vanishing-cycle space still has dimension one; its image in global cohomology may vanish. Thus the local rank-one calculation alone does not exclude the second case. These deductions use exactness and Poincaré duality; the geometric construction of the sequence remains the stated input.

**Monodromy and the specialization image.** Assume, in addition, that the total space is regular at the node. The odd-dimensional Picard–Lefschetz formula in SGA7 II, XV, Theorem 3.4(iii), supplies a nonzero local character \(\varepsilon_x:I\to\mathbf Q_\ell(1)\), where \(I\) is inertia. We use that geometric formula as an input. On \(W=B^n(m)\), the Poincaré pairing takes values in \(\mathbf Q_\ell(2m-n)=\mathbf Q_\ell(-1)\). Choose a nonzero \(e\in\mathbf Q_\ell(1)\) and put \(\beta(v,w)=e\langle v,w\rangle\). This scalar pairing is nondegenerate and alternating: graded commutativity in odd degree gives \(2\langle v,v\rangle=0\), and \(2\) is invertible in \(\mathbf Q_\ell\), including when \(\ell=2\). Define

\[
\begin{gathered}
N(v)=\beta(v,\delta)\delta,\\
c_\sigma=\varepsilon_x(\sigma)/e,\\
T_\sigma=1+(-1)^{m+1}c_\sigma N.
\end{gathered}
\]

Here \(T_\sigma\) is the inertia action. Alternation gives the complete nilpotence calculation

\[
N^2(v)=\beta(v,\delta)\beta(\delta,\delta)\delta=0.
\]

Consequently \((T_\sigma-1)^2=0\); every inertia operator is unipotent. If \(\delta\ne0\), nondegeneracy makes \(N\) have rank one, with image \(\mathbf Q_\ell\delta\) and kernel \(\delta^\perp\). Some \(c_\sigma\) is nonzero, so a vector is fixed by all of inertia exactly when it lies in that kernel. Twisting the preceding specialization sequence by \(m\) therefore proves

\[
W^I=\ker N=\delta^\perp
=\operatorname{im}(\mathrm{sp}(m)).
\]

If \(\delta=0\), then \(N=0\), inertia acts trivially, and the first specialization map is onto, so the same equality holds with \(W^I=W\). Rescaling \(e\) rescales \(N\) and \(c_\sigma\) inversely, leaving the action and its fixed subspace unchanged. Thus the invariant-space conclusion follows completely from the stated Picard–Lefschetz and specialization inputs; it does not supply their geometric proofs.

### 5.1. The character phase and the local roots

The character changes the direction of a good Hecke eigenvalue in the complex plane. The adjoint formula determines that direction before the optimal bound determines its size.

**Proposition 5.1 (phase normalization).** Let \(f\) be a normalized cuspidal Hecke eigenform of weight \(k\ge2\), level \(N\), and character \(\chi\). At a prime \(p\nmid N\), put \(R=p^{(k-1)/2}\), and choose either square root \(\eta\) of \(\chi(p)\). Then
\[
\begin{gathered}
\overline{a_p}=\chi(p)^{-1}a_p,\\
x=\frac{a_p}{\eta R}\in\mathbb R.
\end{gathered}
\tag{5.1a}
\]
For this eigenvalue, the bound \(|a_p|\le2R\) is equivalent to both roots of
\[
X^2-a_pX+\chi(p)R^2
\tag{5.1b}
\]
having modulus \(R\). Under these equivalent conditions there is a real \(\theta\in[0,\pi]\) such that, as an unordered pair,
\[
\begin{gathered}
x=2\cos\theta,\\
\{\alpha_p,\beta_p\}
=\{\eta R e^{i\theta},\eta R e^{-i\theta}\}.
\end{gathered}
\tag{5.1c}
\]
For every \(r\ge0\), the good-prime recurrence consequently gives
\[
\begin{aligned}
a_{p^r}
&=\eta^rR^r\sum_{j=0}^r e^{i(2j-r)\theta},\\
|a_{p^r}|&\le(r+1)R^r.
\end{aligned}
\tag{5.1d}
\]
The finite sum remains valid when the two roots coincide.

**Proof.** On the character space, the level Hecke lesson, Theorem 4.2, proves
\(T_p^*=\chi(p)^{-1}T_p\). Its coefficient formula identifies the eigenvalue of a normalized eigenform with \(a_p\). Since the Petersson product is linear in its first argument, the adjoint identity gives
\[
\begin{aligned}
a_p\langle f,f\rangle
&=\langle T_pf,f\rangle
=\langle f,T_p^*f\rangle\\
&=\chi(p)\overline{a_p}\langle f,f\rangle.
\end{aligned}
\tag{5.1e}
\]
Positivity permits cancellation. The character has finite order, so \(|\chi(p)|=|\eta|=1\). Therefore
\[
\overline{\eta^{-1}a_p}
=\eta\overline{a_p}
=\eta\chi(p)^{-1}a_p
=\eta^{-1}a_p.
\]
This proves (5.1a), without a purity theorem.

Set \(X=\eta R Z\) in (5.1b) and divide by \(\eta^2R^2\). The resulting polynomial is
\[
Z^2-xZ+1.
\tag{5.1f}
\]
If \(|a_p|\le2R\), then the real number \(x\) lies in \([-2,2]\). Choose \(\theta\in[0,\pi]\) with \(x=2\cos\theta\); multiplication shows that its roots are \(e^{i\theta},e^{-i\theta}\). Rescaling proves (5.1c), including the repeated roots at \(x=\pm2\). Conversely, two roots of modulus \(R\) have sum of modulus at most \(2R\), proving the equivalence. Replacing \(\eta\) by \(-\eta\) changes \(x\) to \(-x\); it leaves the original polynomial and its unordered roots unchanged.

The coefficient of \(T^r\) in
\[
\frac1{(1-\alpha_pT)(1-\beta_pT)}
\]
is \(\sum_{j=0}^r\alpha_p^j\beta_p^{r-j}\), by multiplying two geometric series. These coefficients start with \(1,a_p\) and satisfy the Hecke recurrence with constant \(\chi(p)p^{k-1}\), so they equal \(a_{p^r}\). Substitution of (5.1c) proves (5.1d); each of the \(r+1\) summands has modulus one. At \(\theta=0\) the sum is \(r+1\), and at \(\theta=\pi\) it is \((r+1)(-1)^r\). Thus no division by \(\alpha_p-\beta_p\) or limiting argument is needed. \(\square\)

For a polynomial example, take \(k=2\), \(p=5\), \(\chi(p)=-1\), and \(a_p=i\sqrt5\). This illustrates compatible local data, without asserting the existence of a particular newform with these data. Choose \(\eta=i\); then \(x=1\) and \(\theta=\pi/3\). The polynomial and roots are
\[
\begin{gathered}
X^2-i\sqrt5X-5,\\
\alpha,\beta=\frac{i\sqrt5\pm\sqrt{15}}2,\\
|\alpha|=|\beta|=\sqrt5.
\end{gathered}
\tag{5.1g}
\]
The first two recurrence checks are
\[
\begin{gathered}
a_{25}=(i\sqrt5)^2+5=0,\\
a_{125}=5i\sqrt5.
\end{gathered}
\tag{5.1h}
\]
The trace is imaginary, while its phase-normalized value is real. Proposition 5.1 is the additional reason that the coefficient and root formulations of the bound agree for a general character. It does not prove the optimal coefficient bound.

At arbitrary level, multiplicativity and (5.1d) give the precise good-index consequence
\[
\begin{gathered}
|a_n|\le d(n)n^{(k-1)/2}\\
\bigl((n,N)=1\bigr).
\end{gathered}
\tag{5.1i}
\]
Indeed, write \(n=\prod p^{r_p}\), multiply the prime-power bounds, and use \(d(n)=\prod(r_p+1)\). The primes dividing the primitive level require their separate local factors. At level one every index is good, which is the situation used in the preceding convergence argument. In the level-eleven numerical example of the next lesson, the factor \(a_{11^r}=1\) supplies the missing bad-prime information explicitly.

### 5.2. Parity in the split quadratic model

The geometric source uses quadratic forms to describe vanishing cycles. The following algebra calculation supplies the exterior-algebra step in [SGA7 II, Exposé XII, §§1.4 and 1.9–1.10, printed pages 65–69](https://publications.ias.edu/sites/default/files/Number12.pdf#page=73). Its tensor compatibility is left to the reader there.

**Lemma 5.2 (split Clifford algebra and parity).** Let \(A\) be a commutative ring, let \(W\) be free of rank \(m\ge1\), and give \(V=W\oplus W^*\) the quadratic form \(Q(w,f)=f(w)\). Define the Clifford algebra by the relations \(x^2=Q(x)\). Then
\[
C(Q)\cong\operatorname{End}_A(\Lambda W)
\tag{5.2a}
\]
as algebras graded by degree modulo two. Its even part has centre \(A\times A\), with the two factors corresponding to even and odd exterior degree. For two such forms, with \(W=W_1\oplus W_2\), the graded tensor identification preserves the Clifford actions. If \(e_i\) projects onto even degree in \(\Lambda W_i\), the total even-degree idempotent is
\[
\begin{aligned}
e&=e_1\otimes e_2\\
&\quad+(1-e_1)\otimes(1-e_2).
\end{aligned}
\tag{5.2b}
\]
All assertions hold in characteristic two.

**Proof.** Write \(L_w\alpha=w\wedge\alpha\). For \(f\in W^*\), contraction is
\[
\begin{gathered}
I_f(w_1\wedge\cdots\wedge w_r)\\
=\sum_{j=1}^r(-1)^{j-1}f(w_j)\alpha_j,\\
\alpha_j=w_1\wedge\cdots\widehat w_j\cdots\wedge w_r.
\end{gathered}
\tag{5.2c}
\]
The alternating relation gives \(L_w^2=0\). In \(I_f^2\), the two orders of removing any pair of entries have opposite signs, so they cancel. The same formula, applied to \(w\wedge\alpha\), gives
\[
I_fL_w+L_wI_f=f(w)\,1.
\]
Thus \((L_w+I_f)^2=f(w)\,1\), and the defining Clifford relations give a homomorphism to the endomorphisms in (5.2a). Each generator changes parity.

We prove that it is an isomorphism. Choose a basis \(e_1,\ldots,e_m\), its dual basis, and write \(L_i,I_i\) for their operators. The exterior basis is \(e_J\), indexed by subsets \(J\subseteq\{1,\ldots,m\}\), with entries in increasing order. The operator \(L_iI_i\) fixes \(e_J\) if \(i\in J\) and kills it otherwise; \(I_iL_i\) does the reverse. These diagonal operators commute. Hence
\[
P_J=\prod_{i\in J}L_iI_i\prod_{i\notin J}I_iL_i
\]
projects onto \(Ae_J\). Following \(P_J\) by contractions that remove \(J\setminus K\), and then wedges that add \(K\setminus J\), sends \(e_J\) to \(\pm e_K\) and kills every other basis vector. Multiplying by that sign gives each matrix unit. The homomorphism is therefore surjective.

The Clifford relations also span \(C(Q)\) by the \(2^{2m}=4^m\) ordered monomials in its \(2m\) basis generators, each used at most once. Indeed, their squares are zero, and interchanging adjacent generators introduces their negative and, for a dual pair, the scalar one. Repeating these operations orders each word and shortens every scalar remainder. There is consequently a surjection \(A^{4^m}\to C(Q)\). Its composite with the surjection to \(\operatorname{End}(\Lambda W)\cong A^{4^m}\) is a surjective square matrix. Lifting the target basis gives a right inverse, so its determinant is a unit and it is invertible. The first surjection and the Clifford representation must both be injective. This proves (5.2a), including its grading.

The even endomorphisms are
\[
\operatorname{End}(\Lambda^{\mathrm{even}}W)
\times\operatorname{End}(\Lambda^{\mathrm{odd}}W).
\]
Both modules are free of positive rank \(2^{m-1}\). A matrix commuting with every diagonal matrix unit is diagonal; commuting with every remaining matrix unit makes its diagonal entries equal. Thus each matrix algebra has centre \(A\), proving the stated centre and its two idempotents.

For the tensor assertion, the exterior identification is
\[
\begin{gathered}
\Phi:\Lambda W_1\otimes\Lambda W_2
\longrightarrow\Lambda(W_1\oplus W_2),\\
\Phi(\alpha\otimes\beta)=\alpha\wedge\beta.
\end{gathered}
\]
For homogeneous operators and vectors, the graded tensor action is
\[
\begin{gathered}
(a\otimes b)(\alpha\otimes\beta)\\
=(-1)^{\deg b\deg\alpha}a\alpha\otimes b\beta.
\end{gathered}
\tag{5.2d}
\]
Wedge and contraction from the first summand act on the first factor. Those from the second act on the second factor with the sign \((-1)^{\deg\alpha}\): for wedges this follows by moving past \(\alpha\), and for contractions it follows by splitting the sum (5.2c), since the functional vanishes on \(W_1\). Thus \(\Phi\) intertwines every Clifford generator.

The graded tensor product of the two Clifford algebras has multiplication
\[
(a\otimes b)(a'\otimes b')
=(-1)^{\deg b\deg a'}aa'\otimes bb'.
\]
Generators in different summands anticommute, exactly as required by the orthogonal sum. The maps determined by these generators in both directions are inverse, giving \(C(Q_1\perp Q_2)\cong C(Q_1)\widehat\otimes C(Q_2)\). Formula (5.2d) likewise gives the endomorphism-algebra identification: a tensor of homogeneous matrix units acts as a matrix unit with coefficient \(1\) or \(-1\), so these tensors form a basis. This verifies the whole tensor diagram.

Finally, total even degree consists of even–even and odd–odd tensors. The right side of (5.2b) fixes exactly these and kills the other two possibilities. Faithfulness of (5.2a) proves the idempotent identity inside the Clifford algebra. No step divided by two. The two centre labels therefore combine by addition modulo two when even is labelled zero. This supplies the split parity calculation; the geometric descent and vanishing-cycle theorems remain the inputs described above. \(\square\)

#### Finite projective modules

**Corollary 5.2.1 (the projective hyperbolic module).** A finite projective module means a direct summand of some finite free module. Let \(W\) be such a module over a commutative ring \(A\), and put \(H(W)=W\oplus W^*\), with \(Q(w,f)=f(w)\). The same operators give a canonical graded isomorphism
\[
\begin{gathered}
\rho_W:C(H(W))\\
\longrightarrow\operatorname{End}_A(\Lambda W),\\
\rho_W(w,f)=L_w+I_f.
\end{gathered}
\tag{5.2e}
\]
It commutes with arbitrary scalar extension \(A\to B\) and with the graded tensor identification for \(W_1\oplus W_2\). If \(W\) has positive rank at every prime of \(A\), the centre of its even Clifford algebra is \(A\times A\). The representation itself also holds at rank zero.

**Proof.** First record a test we will use repeatedly. If a module \(M\) has zero localization at every prime, then \(M=0\). Indeed, a nonzero element \(x\) has a proper annihilator contained in a maximal ideal \(\mathfrak m\). If \(x/1=0\) in \(M_{\mathfrak m}\), some element outside \(\mathfrak m\) annihilates \(x\), a contradiction. Exactness of localization consequently detects whether a module homomorphism is an isomorphism.

A finite projective module over a local ring \((R,\mathfrak m)\) is free. Here are the needed details. For any finitely generated \(M\) with \(M=\mathfrak mM\), write its generators as linear combinations of themselves with coefficients in \(\mathfrak m\). The resulting matrix \(1-T\) has determinant congruent to one modulo \(\mathfrak m\), hence a unit. Its adjugate shows that all generators vanish. Now lift a basis of \(W/\mathfrak mW\). The cokernel of the resulting map \(R^r\to W\) is finitely generated with zero reduction, so the preceding argument makes the map surjective. Projectivity splits it. Its kernel is a finitely generated direct summand, and the split reduction shows that its reduction is zero. The same argument kills the kernel.

Choose split maps \(W\to A^N\to W\) whose composite is the identity. Applying each exterior power gives a retraction from the finite free module \(\Lambda^j A^N\) onto \(\Lambda^j W\). Thus these powers are finite projective and vanish for \(j>N\). In particular \(E=\Lambda W\), and both its parity summands, are finite projective. Tensor powers and their alternating quotients commute with localization. Hence \(E_{\mathfrak p}=\Lambda(W_{\mathfrak p})\).

We also need the endomorphisms to commute with localization. For any finite projective \(P\), the split finite free presentation gives elements \(p_i\) and functionals \(\phi_i\) with
\[
x=\sum_i\phi_i(x)p_i.
\]
Evaluation is an isomorphism
\[
\begin{gathered}
P^*\otimes P\longrightarrow\operatorname{End}(P),\\
\phi\otimes p\longmapsto\bigl(x\mapsto\phi(x)p\bigr),
\end{gathered}
\]
whose inverse sends \(h\) to \(\sum_i\phi_i\otimes h(p_i)\). The dual-basis identity verifies both composites. The same identity proves \(P^*\otimes B\cong(P\otimes B)^*\) for every \(A\)-algebra \(B\). These formulas prove the required endomorphism localization and, later, arbitrary base change.

Contraction (5.2c) is defined without a basis. It respects the alternating relations: after localization at any prime this is the already verified free-module operator, so every relation has zero image by our test. The identities \(L_w^2=I_f^2=0\) and \(I_fL_w+L_wI_f=f(w)\) follow in the same way. They define \(\rho_W\).

The Clifford algebra localizes too. Its tensor algebra localizes degree by degree, and its defining ideal localizes to the quadratic relations on \(H(W)_{\mathfrak p}\). Every localized vector has the form \(x/s\); its relation is \(s^{-2}(x^2-Q(x))\), so there are no additional relations. Together with the dual and exterior identifications, the localized map \(\rho_W\) is exactly the free representation of Lemma 5.2. At rank zero both sides are the local ring itself. Its kernel and cokernel therefore vanish at every prime. Our test proves (5.2e) globally. Since the map preserves parity and is injective, the opposite parity component of any preimage must vanish; its inverse also preserves parity.

Consequently the even part is
\[
\begin{aligned}
C(H(W))^0&\cong\operatorname{End}(E^{\mathrm{even}})\\
&\quad\times\operatorname{End}(E^{\mathrm{odd}}).
\end{aligned}
\tag{5.2f}
\]
To identify the centres, let \(P\) be finite projective of positive rank at every prime and put \(D=\operatorname{End}(P)\). Its centre is the kernel of the linear commutator map
\[
\begin{gathered}
D\longrightarrow\operatorname{Hom}_A(D,D),\\
T\longmapsto\bigl(S\mapsto TS-ST\bigr).
\end{gathered}
\]
The domain of this Hom is finite projective, so the same dual-basis argument makes Hom commute with localization. Exactness then makes this kernel commute with localization. The scalar map \(A\to Z(\operatorname{End}(P))\) is an isomorphism at every prime, by the positive-size matrix calculation in Lemma 5.2, and is therefore an isomorphism globally. For positive local rank \(r\) of \(W\), each parity summand has rank \(2^{r-1}>0\). Applying this argument to (5.2f) proves the two-factor centre. At rank zero, the odd summand vanishes; the even algebra and its centre there are just the base ring.

The exterior map \(\Phi\) and its intertwining calculation (5.2d) use no chosen global basis. Localizing shows that \(\Phi\) is an isomorphism. The maps on Clifford generators for the orthogonal direct sum and the graded tensor product are inverse just as in Lemma 5.2. Thus its tensor diagram and the total projector (5.2b) remain valid for finite projective modules, including variable rank. Only the total projector is asserted central in the total even algebra.

Finally consider arbitrary \(A\to B\), without assuming flatness. Exterior powers commute with base change because tensor powers and their alternating quotients do. The Clifford tensor algebra and its relation quotient also commute with base change. To check the latter explicitly, expand the square of a \(B\)-linear combination of vectors. The individual relations \(x^2=Q(x)\), together with
\[
xy+yx=Q(x+y)-Q(x)-Q(y),
\]
supply every cross term of its quadratic relation. Thus all relations after scalar extension are generated by the original ones. The dual-basis formulas identify the extended duals and endomorphisms. Under these identifications, evaluation, wedge and contraction are exactly their original formulas with scalars extended. Parity projections likewise extend. This proves all claimed base-change compatibilities, with no division by two. \(\square\)

This gives the construction for a globally split hyperbolic bundle: the formulas agree on overlaps because they are defined by wedge, evaluation and contraction. An arbitrary unsplit quadratic bundle, independence of a chosen complement and the geometric vanishing-cycle theorem still require their separate inputs.

#### The centre at variable rank

The representation above needs no constant-rank hypothesis. We can also describe its centre on every rank component at once.

**Corollary 5.2.2 (including the rank-zero component).** Let \(W\) be any finite projective module over a commutative ring \(A\). Define its evaluation ideal by
\[
J=(f(w):w\in W,\ f\in W^*).
\]
There is a unique idempotent \(e\in A\) with \(J=eA\). It satisfies \(eW=W\), and the canonical centre identification is
\[
Z\bigl(C_A(H(W))^0\bigr)\cong A\times eA.
\tag{5.2g}
\]
Here \(e\) is a scalar in the base ring; it is distinct from the even projection on the exterior module. Under (5.2g), the two scalar actions have the exact form
\[
\begin{gathered}
A\times A\longrightarrow A\times eA,\\
(a,b)\longmapsto(a,eb),\\
\ker=\{0\}\times(1-e)A.
\end{gathered}
\tag{5.2h}
\]
These identifications commute with arbitrary \(A\to B\), including nonflat maps: if \(e_B\) is the image of \(e\), the new centre is \(B\times e_BB\).

**Proof.** Choose split maps \(i:W\to A^N\) and \(r:A^N\to W\), with \(ri=1_W\). Write \(P=ir\), so \(P^2=P\). For the standard basis vector \(v_j\), the entry \(P_{ij}\) is the value on \(r(v_j)\) of the \(i\)-th coordinate functional restricted to \(W\). Thus every entry belongs to \(J\). Conversely, \(f(w)=(fr)(i(w))\) and \(i(w)=Pi(w)\) express each evaluation as a linear combination of those entries. Consequently \(J\) is their finitely generated ideal. The equation
\[
P_{ij}=\sum_kP_{ik}P_{kj}
\]
puts every generator in \(J^2\). The reverse inclusion holds for any ideal, so \(J=J^2\).

We prove the idempotent-generator assertion directly. If \(J=0\), take \(e=0\). Otherwise choose finite generators \(a_1,\ldots,a_t\). The identity \(J=J^2\) gives \(a_i=\sum_jT_{ij}a_j\) with every \(T_{ij}\in J\). Applying the adjugate of \(1-T\) to this generator vector gives
\[
\begin{gathered}
dJ=0,\qquad d=\det(1-T),\\
d\equiv1\pmod J.
\end{gathered}
\]
Put \(e=1-d\). Then \(e\in J\) and \(ex=x\) for every \(x\in J\). In particular \(e^2=e\), and these two facts give \(J=eA\). If another idempotent \(e'\) generates the same ideal, its membership in \(eA\) gives \(ee'=e'\); the membership of \(e\) in \(e'A\) gives \(ee'=e\). Hence \(e'=e\).

Each coordinate of \(i(w)=Pi(w)\) lies in \(J\), so \(ei(w)=i(w)\). Injectivity of \(i\) proves \(ew=w\). This yields the decomposition
\[
A\cong eA\times(1-e)A,
\]
under which \(W\) vanishes on the second factor. The algebra \(eA\) has identity \(e\). On any of its prime localizations, the evaluation ideal is the whole local ring. Indeed, the dual-basis and localization formulas of Corollary 5.2.1 identify that ideal with the localization of \(J=eA\). A free module of rank zero would have zero evaluation ideal, so the local rank of \(W\) on this factor is positive. Conversely, a positive free rank has a basis vector and its coordinate functional evaluating to one. Thus \(e\) is one exactly at the prime localizations where \(W\) has positive rank, and zero at the rank-zero ones. No global constant rank is assumed.

Set \(E^{\mathrm{even}}=\Lambda^{\mathrm{even}}W\) and \(E^{\mathrm{odd}}=\Lambda^{\mathrm{odd}}W\). Both are finite projective by the preceding corollary. The even module contains the direct summand \(\Lambda^0W=A\), so it has positive local rank at every prime of \(A\). The proved endomorphism-centre argument therefore gives
\[
Z\bigl(\operatorname{End}_A(E^{\mathrm{even}})\bigr)=A.
\]
On every positive exterior power, \(e\) acts as the identity: this follows first on tensor products from \(eW=W\), then on their alternating quotients. Hence \(E^{\mathrm{odd}}\) is killed by \(1-e\). Restricting a finite free retraction by \(e\) shows that it is finite projective over \(eA\). At a prime of \(eA\), write \(r>0\) for the local rank of \(W\). Toggling the first basis vector pairs the even and odd exterior basis subsets; each parity has rank \(2^{r-1}>0\). The same centre argument, now over \(eA\), gives
\[
Z\bigl(\operatorname{End}_A(E^{\mathrm{odd}})\bigr)=eA.
\]
Here the \(A\)-linear and \(eA\)-linear endomorphisms coincide because \(e\) acts as the identity. If \(e=0\), the odd module and its endomorphism ring are zero, and the displayed conclusion still holds.

By (5.2f), the even Clifford algebra is the product of these two endomorphism algebras. An element of a product commutes with every pair exactly when each component commutes with every element of its factor. Taking their centres proves (5.2g). On the even module the scalar \(a\) acts faithfully; on the odd module the scalar \(b\) acts through \(eb\). This gives (5.2h). Every element of \(eA\) is of that form, and \(eb=0\) holds exactly when \(b=(1-e)b\), proving both surjectivity and the asserted kernel.

Finally extend scalars to any \(B\). The matrix \(P_B\) remains idempotent and presents \(W\otimes_A B\) as a finite free summand. The same entry argument shows that its evaluation ideal is
\[
J_B=JB=e_BB.
\]
The uniqueness just proved identifies its idempotent with \(e_B\). The exterior representation and parity projections extend by Corollary 5.2.1. Applying our centre formula over \(B\) gives \(B\times e_BB\), precisely the base change of \(A\times eA\); the scalar map and its displayed kernel extend as well. This uses no flatness. It proves base change for these hyperbolic projective Clifford centres, rather than assuming a general base-change rule for centres. \(\square\)

For \(e=1\), the result recovers the positive-rank centre \(A\times A\). For \(W=0\), it gives \(e=0\) and the centre \(A\times0\cong A\). Exercise 9 computes both components together over a product ring.

### 5.3. Two derived steps in the duality input

The Poincaré pairing used in Section 5 comes from a trace in a derived category. This optional section supplies two algebraic steps in that construction. Readers may take the geometric pairing as the stated input without using this section.

We use cohomological grading: \(H^j(K[r])=H^{j+r}(K)\). For an abelian category \(\mathcal A\), write \(D^b(\mathcal A)\) for its bounded derived category and \(\tau_{\ge a}\) for canonical truncation. We assume the truncation triangles, their functoriality, and the exact Hom sequences obtained from a distinguished triangle.

**Lemma 5.3 (factorization through top cohomology).** Fix an integer \(k\ge0\). Let
\[
K_0\xrightarrow{f_0}K_1\longrightarrow\cdots
\xrightarrow{f_{2k-1}}K_{2k}
\]
be a chain in \(D^b(\mathcal A)\), with each \(K_i\) having cohomology only in degrees \(0,\ldots,k\). Suppose \(H^j(f_i)=0\) for every \(j<k\). Its composite factors through the canonical projection
\[
K_0\xrightarrow{p}H^k(K_0)[-k].
\tag{5.3a}
\]
The bound \(2k\) is sufficient; no sharpness is asserted.

**Proof.** If \(k=0\), then \(p\) is an isomorphism and the empty composite is the identity. Suppose \(k\ge1\) and use induction. Put
\[
\begin{gathered}
A=H^k(K_0)[-k],\qquad L=K_{2k-2},\\
M=K_{2k-1},\qquad N=K_{2k},
\end{gathered}
\]
and write \(g:K_0\to L\) for the first \(2k-2\) maps, followed by \(a:L\to M\) and \(b:M\to N\). The complexes \(\tau_{\ge1}K_i[1]\) have cohomology in \(0,\ldots,k-1\), and their induced maps kill cohomology below \(k-1\). Applying induction to their first \(2k-2\) maps, then shifting back, gives
\[
\begin{gathered}
\beta:A\longrightarrow\tau_{\ge1}L,\\
r_Lg=\beta p,
\end{gathered}
\tag{5.3b}
\]
where \(r_P:P\to\tau_{\ge1}P\) is the natural projection. Here the projection from \(K_0\) to its top cohomology agrees with the one obtained after truncation, by functoriality.

For any of these nonnegative complexes \(P\), its bottom truncation triangle is
\[
\begin{gathered}
H^0(P)\xrightarrow{i_P}P\xrightarrow{r_P}\tau_{\ge1}P,\\
\tau_{\ge1}P\xrightarrow{\partial_P}H^0(P)[1].
\end{gathered}
\tag{5.3c}
\]
Naturality of its connecting map gives
\[
\begin{aligned}
\partial_M(\tau_{\ge1}a)\beta
&=H^0(a)[1]\partial_L\beta\\
&=0.
\end{aligned}
\tag{5.3d}
\]
The last equality uses \(H^0(a)=0\). Exactness of \(\operatorname{Hom}(A,-)\) applied to (5.3c) therefore supplies \(h:A\to M\) such that
\[
r_Mh=(\tau_{\ge1}a)\beta.
\]
Using (5.3b) and naturality of \(r\), we get \(r_M(ag-hp)=0\). Exactness of \(\operatorname{Hom}(K_0,-)\) supplies a map \(v:K_0\to H^0(M)\) with
\[
ag-hp=i_Mv.
\]
Finally, naturality of the bottom inclusion and \(H^0(b)=0\) give
\[
bi_M=i_NH^0(b)=0.
\]
Thus \(bag=(bh)p\), which is the desired factorization. The two last maps have separate roles: the first removes the obstruction to lifting \(\beta\), and the second removes the difference between that lift and the original composite. \(\square\)

For the geometric application, let \(f:X\to S\) be smooth and compactifiable of pure relative dimension \(d\ge1\), and let \(\Lambda=\mathbf Z/n\) with \(n>1\) invertible on \(S\). The compact-support dimension bound places \(Rf_!\Lambda(d)\) in cohomological degrees \(0,\ldots,2d\). SGA4 XVIII, Theorem 2.14, supplies successive étale neighborhoods whose transition maps kill the groups below \(2d\), with an isomorphism from top cohomology to \(\Lambda\) given by trace. After base change to one common étale neighborhood of the base, Lemma 5.3, with \(k=2d\), shows that after \(4d\) such transitions the derived map factors through
\[
Rf'_!\Lambda(d)\xrightarrow{\mathrm{Tr}}
\Lambda[-2d].
\tag{5.3e}
\]
This proves the algebraic passage in XVIII, Corollary 2.14.4. The compact-support bound and the geometric neighborhood theorem remain its inputs. This factorization feeds the local criterion XVIII, Proposition 3.1.17, used to prove Poincaré duality.

The compatibility between trace and the adjunction has a separate formal proof.

**Lemma 5.4 (the trace and its adjoint).** Let \(F:\mathcal C\to\mathcal D\) have right adjoint \(G\), with unit \(\eta\) and counit \(\varepsilon\). For a functor \(T:\mathcal D\to\mathcal C\) and a natural transformation \(t:FT\to\operatorname{Id}_{\mathcal D}\), define
\[
u_L=G(t_L)\eta_{T L}:T L\longrightarrow G L.
\tag{5.3f}
\]
Then \(\varepsilon_LF(u_L)=t_L\). Conversely this identity determines \(u\) uniquely.

**Proof.** Naturality of \(\varepsilon\), followed by the triangle identity, gives
\[
\begin{aligned}
\varepsilon_LF(u_L)
&=\varepsilon_LFG(t_L)F(\eta_{T L})\\
&=t_L\varepsilon_{FT L}F(\eta_{T L})\\
&=t_L.
\end{aligned}
\tag{5.3g}
\]
Conversely, for any \(u:T\to G\), naturality of \(\eta\) and the other triangle identity give
\[
\begin{aligned}
G\bigl(\varepsilon_LF(u_L)\bigr)\eta_{T L}
&=G(\varepsilon_L)GF(u_L)\eta_{T L}\\
&=G(\varepsilon_L)\eta_{G L}u_L\\
&=u_L.
\end{aligned}
\]
These two formulas prove the claimed inverse correspondence. \(\square\)

For a smooth map in the preceding setting, take \(F=Rf_!\), \(G=Rf^!\), and \(T(L)=f^*L(d)[2d]\), on the bounded-below categories where the adjunction is constructed. The trace defines \(t\); its adjoint \(u\) therefore satisfies the exact trace diagram of SGA4 XVIII, Lemma 3.2.3. Identifying this adjoint with an isomorphism is the geometric duality theorem, XVIII, Theorem 3.2.5. The formal trace identity just proved does not supply that isomorphism. Cohomology maps alone need not determine a derived morphism, as the next exercise shows.

#### A shorter truncation bound

The \(2k\) count in Lemma 5.3 is sufficient. Using lower truncations gives a stronger bound, which we prove separately.

**Corollary 5.3.1 (one degree per transition).** Let \(a\le b\) be integers and set \(m=b-a\). Suppose
\[
K_0\xrightarrow{f_0}K_1\longrightarrow\cdots
\xrightarrow{f_{m-1}}K_m
\]
is a chain in \(D^b(\mathcal A)\), with every \(K_i\) having cohomology only in degrees \(a,\ldots,b\). If \(H^r(f_i)=0\) for every \(r<b\), the composite factors through the canonical projection
\[
p:K_0\longrightarrow H^b(K_0)[-b].
\tag{5.3h}
\]
The factor need not be unique. If \(a=b\), this projection is an isomorphism and the empty composite factors through it.

**Proof.** Write \(j_{P,r}:\tau_{\le r}P\to P\) for the canonical inclusion. The top projection of a lower truncation fits into the triangle
\[
\begin{gathered}
\tau_{\le r-1}Q\xrightarrow{c_{Q,r}}\tau_{\le r}Q,\\
\tau_{\le r}Q\xrightarrow{q_{Q,r}}H^r(Q)[-r],\\
H^r(Q)[-r]\longrightarrow(\tau_{\le r-1}Q)[1].
\end{gathered}
\tag{5.3i}
\]
If \(f:P\to Q\) has \(H^r(f)=0\), naturality gives
\[
\begin{aligned}
q_{Q,r}(\tau_{\le r}f)
&=H^r(f)[-r]q_{P,r}\\
&=0.
\end{aligned}
\]
The exact sequence obtained by applying \(\operatorname{Hom}(\tau_{\le r}P,-)\) to (5.3i) therefore supplies a lift
\[
\begin{gathered}
\lambda_{f,r}:\tau_{\le r}P\longrightarrow\tau_{\le r-1}Q,\\
c_{Q,r}\lambda_{f,r}=\tau_{\le r}f.
\end{gathered}
\]
Composing with the canonical inclusion into \(Q\) yields the actual morphism identity
\[
j_{Q,r-1}\lambda_{f,r}=f j_{P,r}.
\tag{5.3j}
\]
This is not an inference that zero cohomology maps imply a zero morphism.

Assume \(m\ge1\), and put \(T=\tau_{\le b-1}K_0\). Starting with its identity map, we construct
\[
\begin{gathered}
g_i:T\longrightarrow\tau_{\le b-1-i}K_i,\\
j_{K_i,b-1-i}g_i\\
=(f_{i-1}\cdots f_0)j_{K_0,b-1},
\end{gathered}
\tag{5.3k}
\]
where the empty composite for \(i=0\) is the identity. At step \(i<m\), let \(r=b-1-i<b\). Since \(H^r(f_i)=0\), the preceding lift exists. Define \(g_{i+1}=\lambda_{f_i,r}g_i\). Equation (5.3j) proves (5.3k) at the next step, with the order of the maps unchanged. For \(i=m\), its target is \(\tau_{\le a-1}K_m=0\). Thus the complete composite vanishes on the actual inclusion of \(T\) into \(K_0\).

Finally apply \(\operatorname{Hom}(-,K_m)\) to the source triangle
\[
\begin{gathered}
T\longrightarrow K_0\xrightarrow{p}H^b(K_0)[-b],\\
H^b(K_0)[-b]\longrightarrow T[1].
\end{gathered}
\]
Exactness supplies \(h:H^b(K_0)[-b]\to K_m\) such that \(f_{m-1}\cdots f_0=hp\), proving the assertion. \(\square\)

Taking \(a=0,b=k\) shows that \(k\) transitions suffice. The original \(2k\) assertion still follows: factor the first \(k\) maps and then postcompose with the remaining \(k\). Its proof and source formulation above remain valid.

With the same retained geometric inputs as before, the complexes have amplitude \([0,2d]\) after passage to one common étale base. Hence \(2d\) transitions killing the groups below \(2d\) suffice. The top-cohomology trace isomorphism identifies the projection (5.3h) with the trace map (5.3e), so the factorization still has target \(\Lambda[-2d]\), with the same twist and coefficients. This improves only the algebraic transition count; it does not prove the geometric neighborhood theorem, dimension bound, base change or duality.

**Corollary 5.3.2 (a bounded chain of cohomologically zero maps).** Suppose every object in a chain has amplitude \([a,b]\), and every transition induces zero on all cohomology groups. A composite of \(b-a+1\) such transitions is zero.

**Proof.** Start with \(\tau_{\le b}K_0\cong K_0\). The same one-step lift (5.3j) lowers the target truncation degree once per transition. After \(b-a+1\) steps the composite factors through \(\tau_{\le a-1}K_{b-a+1}=0\). This proves its actual vanishing. \(\square\)

#### Sharpness at every amplitude width

**Proposition 5.3.3 (both bounds are attained).** For every pair of integers \(a\le b\), put \(m=b-a\). In the bounded derived category of modules over \(R=\mathbf F_2[\varepsilon]/(\varepsilon^2)\), there is an object \(K\) with nonzero cohomology exactly in degrees \(a,\ldots,b\), and an endomorphism \(\gamma\) inducing zero on every cohomology group, such that
\[
\begin{gathered}
\gamma^q\ne0\quad(0\le q\le m),\\
\gamma^{m+1}=0.
\end{gathered}
\tag{5.3l}
\]
For a nonnegative integer \(q\), the power \(\gamma^q\) factors through the canonical top projection \(K\to H^b(K)[-b]\) exactly when \(q\ge m\). Powers with exponent zero mean the identity, including when \(m=0\).

**Proof.** Let \(B=R/(\varepsilon)\). We first check all extension powers as actual compositions. Write \(P^i=R\) for \(i\le0\) and zero for \(i>0\), with differential multiplication by \(\varepsilon\) in negative degrees and zero in degree zero. Its augmentation \(\pi:P\to B\) is reduction modulo \(\varepsilon\). For \(x=u+v\varepsilon\), multiplication gives \(\varepsilon x=u\varepsilon\), so the kernel and image are both \(\varepsilon R\). This proves exactness in negative degrees and identifies the degree-zero quotient with \(B\); thus \(P\) is a free resolution.

Every differential in \(\operatorname{Hom}_R(P,B)\) is zero, and its term in each nonnegative degree is \(B\). The projective-resolution identification with derived morphisms consequently gives
\[
\operatorname{Hom}_{D^b(R\text{-}\mathrm{Mod})}(B,B[q])
\cong B\qquad(q\ge0).
\]
To determine multiplication as well, define \(D:P\to P[1]\) by \(D^i=1_R\) for \(i\le-1\), and zero otherwise. Below degree minus one, the chain-map equation has multiplication by \(\varepsilon\) on both sides; the shifted differential sign disappears in characteristic two. In degree minus one both composites are zero, and the higher degrees are zero too. Hence \(D\) is a chain map. Let \(\delta:B\to B[1]\) be the class characterized by \(\delta\pi=\pi[1]D\).

Set \(D^{(0)}=1_P\), \(\delta^{(0)}=1_B\), and, for \(q\ge1\), set
\[
\begin{aligned}
D^{(q)}&=D[q-1]\cdots D[1]D,\\
\delta^{(q)}&=\delta[q-1]\cdots\delta[1]\delta.
\end{aligned}
\tag{5.3m}
\]
The map \(D^{(q)}:P\to P[q]\) is the identity in degrees \(i\le-q\), since precisely there all \(q\) identity components are available; its other components are zero. Shifting \(\delta\pi=\pi[1]D\) and composing in the displayed order gives
\[
\delta^{(q)}\pi=\pi[q]D^{(q)}.
\tag{5.3n}
\]
The right side is the cocycle with value \(1\in B\) in resolution degree \(-q\). Since the Hom differentials vanish, it cannot be a boundary. Thus every \(\delta^{(q)}\) is nonzero, including \(q=0\). This proves the required multiplication directly; the dimensions of the Ext groups alone would not prove it.

Now take the finite ordered sum
\[
K=\bigoplus_{r=0}^{m}B[-a-r],
\tag{5.3o}
\]
and write \(i_r,p_r\) for its inclusions and projections. With the convention \(H^j(L[s])=H^{j+s}(L)\), the \(r\)-th summand has cohomology \(B\) in degree \(a+r\) only. Define
\[
\gamma=\sum_{r=1}^{m}i_{r-1}\delta[-a-r]p_r.
\tag{5.3p}
\]
The middle map goes from \(B[-a-r]\) to \(B[1-a-r]=B[-a-(r-1)]\). It connects distinct cohomological degrees, so it induces zero in every degree. Consequently \(H^j(\gamma)=0\) for all \(j\).

The identities \(p_r i_s=0\) for \(r\ne s\) and \(p_r i_r=1\) give the complete power formula
\[
\begin{gathered}
\gamma^q=\sum_{r=q}^{m}
 i_{r-q}\delta^{(q)}[-a-r]p_r,\\
0\le q\le m.
\end{gathered}
\tag{5.3q}
\]
For \(q=0\), this is the direct-sum identity. If the formula holds for \(q<m\), multiplying on the left by \(\gamma\) leaves only the adjacent entry indexed by \(r-q\), for \(r\ge q+1\). Its middle composite is
\[
\begin{aligned}
&\delta[-a-r+q]\delta^{(q)}[-a-r]\\
&\hspace{1em}=\delta^{(q+1)}[-a-r],
\end{aligned}
\]
by (5.3m). This proves the induction without commuting any maps. Projecting one entry gives
\[
\begin{gathered}
p_0\gamma^q i_q=\delta^{(q)}[-a-q]\ne0,\\
0\le q\le m.
\end{gathered}
\tag{5.3r}
\]
Thus all these powers are nonzero. The next power vanishes because (5.3q) at \(q=m\) lands in the first summand and \(\gamma i_0=0\). This proves (5.3l). When \(m=0\), the defining sum for \(\gamma\) is empty and zero, while \(K=B[-a]\ne0\); the same argument includes this endpoint.

The lower truncation \(\tau_{\le b-1}K\) is the sum of the terms with \(r<m\). Its quotient is the last summand, so the canonical top projection is precisely \(p_m:K\to B[-b]\). The last nonzero power satisfies
\[
\gamma^m=i_0\delta^{(m)}[-b]p_m.
\tag{5.3s}
\]
For \(q>m\), the zero power factors as well. If \(0\le q<m\) and \(\gamma^q=h p_m\), then \(p_m i_q=0\) would give \(p_0\gamma^q i_q=0\), contradicting (5.3r). This proves the exact factorization threshold. \(\square\)

The constant chain with object \(K\) and transition \(\gamma\) meets even the stronger condition of zero maps in every cohomology degree. Hence the universal \(b-a\) top-factorization count in Corollary 5.3.1 and the \(b-a+1\) vanishing count in Corollary 5.3.2 cannot be reduced. This is sharpness over the class of derived module categories; it asserts neither optimality in every particular category nor an optimal number of geometric neighborhood refinements. The case \(a=0,m=2\) recovers the ordered three-term computation in Solution 10.

The nonzero map in Solution 8 has amplitude \([0,1]\) and square zero. The following three-term example tests both the improved factorization and the longer nilpotence bound.

### 5.4. A finite choice in the curve-duality programme

The original curve-duality construction in SGA4 XVIII, 1.5.9–1.5.12, includes a general-position choice of sections after a residue-field extension. We isolate its elementary avoidance step here. The lemma concerns vector spaces and their scalar extensions; applying it to relative divisors still requires the geometric restriction, section-lifting and neighbourhood arguments.

**Lemma 5.5 (exact criterion and finite-field count).** Let \(V\) have dimension \(d\ge1\) over a field \(k\), let \(\ell:V\to k\) be nonzero, and put \(A=\ell^{-1}(1)\). For finitely many indices \(i\), let \(q_i:V\to U_i\) be linear and \(S_i\subset U_i\) a linear subspace. Define
\[
\begin{aligned}
L_i&=q_i^{-1}(S_i),\\
c_i&=\operatorname{codim}_V L_i\\
&=\dim_k\left(\frac{q_i(V)}{q_i(V)\cap S_i}\right).
\end{aligned}
\tag{5.4a}
\]
There is a point \(v\in A(K)\) over some finite separable extension \(K/k\), avoiding every \(L_i\otimes_k K\), if and only if every \(c_i>0\). For infinite \(k\), one can take \(K=k\).

Suppose these conditions hold and \(K\) is finite of cardinality \(Q\). Let \(I\) be the indices for which \(\ell|_{L_i}\ne0\). Then
\[
\begin{gathered}
\#\bigl(A(K)\setminus\textstyle\bigcup_i(L_i\otimes K)\bigr)\\
\ge Q^{d-1}-\sum_{i\in I}Q^{d-c_i-1}.
\end{gathered}
\tag{5.4b}
\]
In particular, avoidance is possible if
\[
\sum_{i\in I}Q^{-c_i}<1.
\tag{5.4c}
\]
With \(N=\#I\), the inequality \(Q>N\) suffices. In the particular case \(d=4\), injective \(q_i\), and \(\dim S_i\le2\), there are at least \(Q^3-NQ\) allowed points, so \(Q^2>N\) suffices.

**Proof.** The kernel of \(V\to U_i/S_i\) is \(L_i\). The first isomorphism theorem gives (5.4a). Choose a basis of this kernel and extend it to a basis of \(V\); the images of the added vectors in \(U_i/S_i\) are linearly independent. After any field extension they stay independent. Thus the kernel after extension is exactly \(L_i\otimes K\), with the same codimension. In particular, an index with \(c_i=0\) prevents avoidance over every extension.

Choose \(a\in V\) with \(\ell(a)=1\). We have \(A=a+\ker\ell\). This affine slice spans \(V\): it contains \(a\), and every \(w\in\ker\ell\) is the difference \((a+w)-a\) of two points of \(A\). A proper \(L_i\) therefore cannot contain \(A\).

If \(\ell|_{L_i}=0\), its intersection with \(A\) is empty. Otherwise choose \(a_i\in L_i\) with \(\ell(a_i)=1\). The intersection after extension is
\[
\begin{gathered}
A(K)\cap(L_i\otimes K)\\
=a_i+\ker(\ell|_{L_i})\otimes K.
\end{gathered}
\tag{5.4d}
\]
Its translation space has dimension \(d-c_i-1\). When \(K\) is finite, a basis identifies its points with \(K^{d-c_i-1}\), so there are exactly \(Q^{d-c_i-1}\) points. The entire slice has \(Q^{d-1}\) points. Subtracting the upper bound on the size of a finite union proves (5.4b), and dividing its right side by \(Q^{d-1}\) gives (5.4c). Every \(c_i\ge1\), so the sum is at most \(N/Q\). When \(d=1\), every proper \(L_i\) is zero and \(I\) is empty: the slice's unique point already works. No negative exponent is used for a nonempty intersection.

If \(k\) is finite of size \(q\), arbitrarily large finite separable extensions can be constructed explicitly. For an integer \(r\ge1\), take the roots of \(X^{q^r}-X\) in an algebraic closure. Its derivative is \(-1\), so it has exactly \(q^r\) distinct roots. Frobenius identities show that addition, subtraction, multiplication and nonzero inversion preserve the root equation. The roots form a field containing \(k\); its size is \(Q=q^r\), and it is separable since its elements satisfy this separable polynomial. Choose \(Q>N\) and apply (5.4c). This proves sufficiency over finite \(k\).

For infinite \(k\), put affine coordinates on \(A\). Each nonempty forbidden intersection is a proper affine subspace. Choose a nonzero linear functional annihilating its translation space and subtract its value at one point; the resulting nonzero affine polynomial vanishes on that subspace. The product of these finitely many polynomials is nonzero, because a polynomial ring over a field has no zero divisors. This product has a nonzero value at some \(k\)-point. Indeed, induct on the number of variables: first choose earlier coordinates making one nonzero coefficient polynomial nonzero, then choose the last coordinate outside the finitely many roots of the resulting nonzero one-variable polynomial. In zero variables a nonzero constant suffices. The point so obtained avoids every intersection. This completes the existence criterion.

Finally, in the stated four-dimensional case injectivity gives \(\dim L_i\le\dim S_i\le2\), hence \(c_i\ge2\). Each nonempty intersection consequently has at most \(Q\) points. Formula (5.4b) becomes the claimed lower bound \(Q^3-NQ\), which is positive when \(Q^2>N\). \(\square\)

The criterion is \(q_i(V)\not\subset S_i\); injectivity is one sufficient way to check it in the original four-dimensional setup. A chosen point outside the span of a nonzero prescribed value \(m\) gives a good interpolating pair: \(\lambda m+(1-\lambda)q_i(v)\ne0\) for every scalar over every further extension, since the two vectors are independent.

For a triple, suppose an old pair \(m,n\) is already good over all further field extensions, and choose \(q_i(v)\notin\operatorname{span}(m,n)\). If
\[
\lambda m+\mu n+(1-\lambda-\mu)q_i(v)=0,
\]
then avoidance of that span forces \(1-\lambda-\mu=0\). The remaining equality is a prohibited zero of the old good pair. This proves the triple condition even if the old vectors are dependent. These are the formal pair and triple consequences of the lemma. They establish neither the geometric hypotheses on the restriction maps nor the relative-divisor conditions over the whole interpolation parameter space. The numerical threshold is attained in Solution 11.

### 5.5. Affine torsor morphisms on a projective bundle

The projective-torsor programme in SGA4 XVIII, Section 1.2, separates the determination of morphisms from the existence of a classification. The following calculation proves the affine morphism statement. Its proof permits any commutative affine group scheme, including groups that are not flat or not of finite presentation. Those conclusions concern full faithfulness alone; the nonaffine and existence parts of the programme retain their own hypotheses.

**Lemma 5.6 (affine full faithfulness).** Let \(S\) be a scheme, let \(E\) be a vector bundle whose locally finite rank is everywhere at least two, and let \(G\) be a commutative affine group scheme over \(S\). Write \(p:P=\mathbb P(E)\to S\), with projectivization parametrizing lines. Thus \(U=E\setminus0_S\) is the frame bundle of \(\mathcal O_P(-1)\). Torsors here are sheaves locally trivial for the fppf topology; no representability or finite-presentation claim about all torsors is part of the definition.

Consider pairs \((T,\phi)\), where \(T\) is a \(G\)-torsor on \(S\) and \(\phi:\mathbb G_{m,S}\to G\) is a group-scheme morphism. Between pairs with the same character the morphisms are the equivariant base-torsor maps; between unequal characters there are no morphisms. Define
\[
F(T,\phi)=p^*T+\phi\mathcal O_P(1).
\tag{5.5a}
\]
Here the sum is the contracted sum of commutative torsors. The character torsor is the pushout of the frame torsor of \(\mathcal O_P(1)\), with convention
\[
[s\lambda,g]=[s,\phi(\lambda)+g].
\tag{5.5b}
\]
The functor \(F\) is fully faithful: every equivariant map between its images forces equality of their characters and comes from exactly one base-torsor map. The statement and its proof persist after arbitrary base change.

**Proof, first step: extending coordinates.** Work over an arbitrary ring \(A\), with \(E\) free of rank \(r\ge2\). Put \(R=A[x_1,\ldots,x_r]\), so \(U=\bigcup_iD(x_i)\). All the coordinate and overlap rings inject into
\[
L=A[x_1^{\pm1},\ldots,x_r^{\pm1}].
\]
Indeed, multiplication by a coordinate shifts the monomial basis of a free \(A\)-module and is injective, even if \(A\) has zero divisors. Localizing other coordinates gives the same argument with a Laurent monomial basis. Compatible functions on the charts therefore become one common Laurent polynomial. In \(R_{x_1}\) only the first exponent may be negative; in \(R_{x_2}\) only the second may be negative. Uniqueness of Laurent coefficients gives
\[
\begin{gathered}
R_{x_1}\cap R_{x_2}=R,\\
\Gamma(U,\mathcal O_U)=R.
\end{gathered}
\tag{5.5c}
\]
The remaining chart functions equal that polynomial because their injections into \(L\) agree. Conversely every polynomial gives a compatible family.

For any affine \(A\)-scheme \(H=\operatorname{Spec}C\), the coordinate homomorphisms of a map \(\psi:U\to H\) consequently combine into a homomorphism \(C\to R\). Its restriction on every chart is the given map, so it extends \(\psi\) uniquely to \(\bar\psi:E\to H\). No finite generating set of \(C\) is needed: each coordinate has its own polynomial image, and the ring identities hold by restriction and injectivity.

Suppose \(H\) is an affine group scheme and, in multiplicative group notation, a character \(\chi:\mathbb G_m\to H\) satisfies
\[
\psi(\lambda v)=\chi(\lambda)\psi(v).
\tag{5.5d}
\]
Apply the same injection argument over \(A[t,t^{-1}]\). The two maps in (5.5d) agree on the punctured bundle, and hence on the entire bundle. At the zero section their equality becomes \(\chi(t)g=g\), where \(g=\bar\psi(0)\). Cancellation proves that \(\chi\) is the neutral character as a group-scheme map. It follows that \(\bar\psi(tv)=\bar\psi(v)\).

For a coordinate of \(H\), let its polynomial image be \(\sum_\alpha a_\alpha x^\alpha\). Invariance says
\[
\begin{gathered}
\sum_\alpha a_\alpha t^{|\alpha|}x^\alpha\\
=\sum_\alpha a_\alpha x^\alpha.
\end{gathered}
\tag{5.5e}
\]
For every \(|\alpha|>0\), comparison of the coefficient of \(t^{|\alpha|}x^\alpha\) makes \(a_\alpha=0\). Thus every coordinate is constant, and \(\psi\) is the pullback of \(g\). This coefficient argument uses neither differentiation nor reducedness. On affine trivializations of a general bundle the same conclusion holds. The base sections agree on overlaps: after trivializing \(E\), its punctured bundle has the section \((1,0,\ldots,0)\), so pullback of sections is injective there. They therefore glue uniquely.

**Second step: the morphism and its descent.** Trivialize both base torsors on fppf covers, trivialize \(E\) on open covers, and refine to affine pieces. These torsor covers exist by the chosen sheaf-torsor definition, without a flatness assumption on \(G\). For \(v\in U\), the dual frame \(s(v)\) of \(\mathcal O(1)\) is characterized by \(s(v)(v)=1\). Hence
\[
\begin{aligned}
s(\lambda v)&=\lambda^{-1}s(v),\\
t_\phi(\lambda v)&=t_\phi(v)-\phi(\lambda),
\end{aligned}
\tag{5.5f}
\]
where \(t_\phi(v)=[s(v),0]\) in the character torsor. Include the chosen origin of the base torsor in this notation. An equivariant map \(\beta:F(T,\phi)\to F(T',\phi')\) now determines a unique section \(\psi\in G(U)\) by
\[
\beta(t_\phi(v))=t_{\phi'}(v)+\psi(v).
\]
Since \(G\) is affine, that section is an actual scheme map \(U\to G\). Evaluating the same equation at \(\lambda v\) and using (5.5f) and equivariance yields
\[
\begin{gathered}
\psi(\lambda v)\\
=\psi(v)+(\phi'-\phi)(\lambda).
\end{gathered}
\tag{5.5g}
\]
Commutativity makes the difference of characters a character. The first step, now in additive notation, proves \(\phi'=\phi\) and \(\psi=p_U^*g\) for a unique base section \(g\). Translation by \(g\) is precisely the base-torsor map inducing \(\beta\) on this piece.

These local base maps agree on overlaps. Both induce the given \(\beta\); their uniqueness, or the local section of the punctured bundle just used, makes them equal. Maps between sheaf torsors glue on covers, so they give a unique global base map. Equality of the characters on that cover is equality on \(S\), by the sheaf condition for their maps into \(G\). Conversely a base map pulls back and adds the identity of the fixed character torsor, producing a map of the images. The two procedures are inverse on each trivializing piece and therefore globally. Every equivariant torsor map is an isomorphism: locally it is translation, whose inverse is translation by the negative section. This proves the asserted full faithfulness. All polynomial, frame, translation and gluing formulas remain the same under base change, proving the last assertion. \(\square\)

**A nonflat group covered by the lemma.** For a field \(k\), take \(A=k[s]\) and
\[
C=A[t]/(st),\qquad G=\operatorname{Spec}C.
\]
The additive-group maps descend to this quotient: \(\Delta(t)=t\otimes1+1\otimes t\), the identity sends \(t\) to zero, and the inverse sends it to \(-t\). In \(C\otimes_A C\), the image of \(st\) is \(st\otimes1+1\otimes st=0\); the other maps also kill the relation. The associative addition and inverse identities are the ordinary polynomial identities, so \(G\) is a commutative affine group scheme.

It is not flat over \(A\). Multiplication by \(s\) is injective on \(A\), but tensoring this injection with \(C\) gives multiplication by \(s\) on \(C\), which kills \(t\). The class of \(t\) is nonzero because specializing \(s=0\) sends it to the nonzero polynomial \(t\in k[t]\). Flatness would preserve the injection, a contradiction. The fibre at \(s=0\) is \(\mathbb G_a\); after inverting \(s\), the relation forces \(t=0\), so the group is trivial. Lemma 5.6 still determines the torsor morphisms on every projective bundle of the specified rank.

**A group without finite presentation.** Over \(k\), the algebra \(k[t_1,t_2,\ldots]\), with each \(t_i\) primitive under the same additive comultiplication, defines a commutative affine group. It is not of finite type: a finite collection of polynomials uses only finitely many variables and generates an algebra in those variables. An omitted variable cannot belong to that algebra, by uniqueness of polynomial coefficients. In particular the group is not of finite presentation. The coordinate extension in the proof handles each coordinate separately, so this example also satisfies the lemma.

**Why the rank hypothesis remains.** Take \(S=\operatorname{Spec}k\), \(E=\mathcal O_S\), \(G=\mathbb G_m\), and trivial base torsors. Here \(P=S\) and the standard frame trivializes \(\mathcal O(1)\). Both the neutral character and the identity character therefore give trivial image torsors, although the characters are unequal. A target isomorphism exists and the source Hom set is empty, so the functor fails to be full. At the coordinate level the obstruction is already visible: on the rank-one punctured line, \(\psi(v)=v\) satisfies \(\psi(\lambda v)=\lambda\psi(v)\) with a nonneutral character and does not extend as a map into \(\mathbb G_m\) across zero.

These examples show exactly which hypotheses the affine morphism proof uses. They supply no essential-surjectivity proof, no classification for nonaffine groups, and no removal of hypotheses from the complete geometric theorem.


### 5.6. Norms when divisors meet

The trace construction in SGA4 XVII, Section 6.3, includes finite families with ramification and repeated points. For line bundles its concrete form is a determinant norm. The following proof establishes the tensor and divisor compatibilities in this case over arbitrary rings. It uses neither a separation of the points nor a passage to cohomology classes.

**Lemma 5.7 (line-bundle norm and divisor interchange).** Let \(p:T\to S\) be finite locally free. There is a functor \(N_p\) from line bundles and their isomorphisms on \(T\) to line bundles and their isomorphisms on \(S\). It has canonical tensor, unit and arbitrary-base-change isomorphisms. Locally where \(p\) has rank \(n\),

\[
\begin{aligned}
N_p(L)&=\det(p_*L)\\
&\quad\otimes\det(p_*\mathcal O_T)^{-1},\\
N_p(p^*M)&\simeq M^{\otimes n}.
\end{aligned} \tag{5.6a}
\]

Let \(D,E\) be effective Cartier divisors on an \(S\)-scheme \(X\), and assume \(D,E,D+E\) are finite locally free over \(S\). For a line bundle \(L\) on \(X\), write \(N_D(L)=N_{D/S}(L|_D)\). Then there is a canonical isomorphism \(\beta_L\)

\[
\begin{aligned}
N_{D+E}(L)&\longrightarrow\\
&N_D(L)\otimes N_E(L).
\end{aligned} \tag{5.6b}
\]

These maps commute with tensor products of line bundles, associativity, ordinary symmetry, units and base change whenever the stated Cartier and finite-local-freeness hypotheses persist. The divisors may meet and may be nonreduced.

**Proof, first step: frames over the base.** On an affine open of \(S\), put \(T=\operatorname{Spec}B\) and \(S=\operatorname{Spec}A\), with \(B\) a finite locally free \(A\)-algebra. An invertible \(B\)-module \(L\) becomes free of rank one after a Zariski covering of \(\operatorname{Spec}A\). Here is the required argument, including the absence of a noetherian hypothesis.

Localize at a prime of \(A\), so \(A\) is local with maximal ideal \(\mathfrak m\). A finite algebra is integral: write multiplication by any element using finitely many module generators including \(1\), and apply the adjugate determinant identity to obtain a monic annihilating polynomial. Consequently every maximal ideal of \(B\) lies over \(\mathfrak m\). Indeed a domain integral inside a field which is integral over it is a field: the monic equation for the inverse of a nonzero element, multiplied by a suitable power of that element, expresses its inverse in the domain. Apply this to the residue extension at a maximal ideal of \(B\). The maximal ideals of \(B\) are therefore those of the finite-dimensional algebra \(B/\mathfrak mB\), and there are finitely many.

At each such maximal ideal choose a nonzero vector in the one-dimensional residue fibre of \(L\). The Chinese remainder identity for these pairwise comaximal ideals, applied to the module \(L\), lifts the finitely many choices to one element \(\ell\in L\). At every maximal localization \(L\) is free of rank one and \(\ell\) has unit coefficient. Thus \(B\to L\), \(b\mapsto b\ell\), is an isomorphism at every maximal ideal, and hence an isomorphism. To justify the last implication, a nonzero kernel or cokernel element would have a proper annihilator contained in a maximal ideal and would remain nonzero at a suitable maximal localization.

This frame spreads to a neighbourhood of the chosen prime of \(A\). The module \(L\) is finite projective over \(A\), since it is a direct summand of a finite sum of copies of the finite projective module \(B\). Clear the denominator of a local frame; after shrinking, both \(B\) and \(L\) are free over \(A\) of the same rank. The determinant of the resulting map \(B\to L\) is a unit at the chosen prime. Inverting it makes the map an isomorphism on a neighbourhood. This argument uses no finiteness assumption on the kernel of a matrix. For a rank-zero component \(T\) is empty and the norm is the unit line.

**Second step: the norm and its actual maps.** For \(u\in B\), define \(N_{B/A}(u)=\det_A(m_u)\), where \(m_u\) is multiplication by \(u\) on \(B\). Determinants are independent of the chosen basis, and

\[
\begin{aligned}
N_{B/A}(uv)&=N_{B/A}(u)N_{B/A}(v),\\
N_{B/A}(a)&=a^n\quad(a\in A).
\end{aligned} \tag{5.6c}
\]

The first equality follows from \(m_{uv}=m_um_v\), and the second from the scalar matrix. In particular a unit has unit norm, with the norm of its inverse as inverse.

A frame \(\ell:B\simeq L\) defines a frame \(\nu_L(\ell)\) of the determinant line in (5.6a): take \(\det(\ell)\) and tensor with the inverse identity of \(\det(B)\). Replacing \(\ell\) by \(u\ell\), for \(u\in B^\times\), gives

\[
\nu_L(u\ell)=N_{B/A}(u)\nu_L(\ell). \tag{5.6d}
\]

This proves that these local frames glue to the displayed determinant line. If an isomorphism \(f:L\to L'\) sends \(\ell\) to \(u\ell'\), its norm sends \(\nu_L(\ell)\) to \(N_{B/A}(u)\nu_{L'}(\ell')\). Formula (5.6d) makes this prescription independent of both frames. Multiplicativity proves preservation of identities and composition.

Define the tensor map \(\alpha_{L,M}\) from \(N_p(L)\otimes N_p(M)\) to \(N_p(L\otimes M)\) by

\[
\begin{aligned}
\nu_L(\ell)\otimes\nu_M(m)&\longmapsto\\
&\nu_{L\otimes M}(\ell\otimes m).
\end{aligned} \tag{5.6e}
\]

Changing the two frames by \(u,v\) multiplies both sides by \(N(u)N(v)=N(uv)\), so the map is intrinsic. It is an isomorphism because it sends a local frame to a local frame. The frame \(1\) gives the unit identification. Every associativity pentagon sends the tensor of the original norm frames to the norm of the same tensor of original frames. The triangle has the same description with \(1\) inserted. Both symmetry hexagons implement the same permutation of those frames. The flip on the tensor square of one line is identity locally, since both factors can use one frame; hence the diagonal symmetry is identity. These statements prove equality of actual maps, since equality of line-bundle maps is local. They also prove naturality using the explicit \(N(u)\) formula for morphisms. All tensor products here are ordinary tensor products of lines; no graded determinant sign is introduced.

For \(A\to A'\) the multiplication matrix becomes the same matrix with its entries mapped to \(A'\), and its determinant maps to the same determinant. The frame formulas therefore give the canonical base-change isomorphism and show that every preceding map pulls back to its counterpart. No flatness of \(A'\) is needed. A frame of \(M\) pulls back to a frame of \(p^*M\); its transition \(a\) has norm \(a^n\), proving the second assertion of (5.6a).

**Third step: intersecting divisors.** There is an exact sequence on \(X\)

\[
\begin{aligned}
0\longrightarrow\mathcal O_D(-E)&\longrightarrow\mathcal O_{D+E}\\
&\longrightarrow\mathcal O_E\longrightarrow0.
\end{aligned} \tag{5.6f}
\]

To check it, use local equations \(f,g\) for \(D,E\). The first map sends a class modulo \(f\), with the local frame of \(\mathcal O(-E)\), to its product by \(g\) modulo \(fg\). If \(gx\in(fg)\), cancellation of the nonzerodivisor \(g\) gives \(x\in(f)\), proving injectivity. Its image is exactly the kernel of reduction modulo \(g\). This does not require the supports to be disjoint.

Push (5.6f) to \(S\). It remains exact: locally the sheaves are modules supported on the finite affine scheme \(D+E\), and restriction of scalars is exact. The first and last modules are finite locally free over \(S\); for the first this follows by applying the frame argument to the invertible \(\mathcal O_D\)-module \(\mathcal O_D(-E)\). Locally on \(S\) the sequence splits as a sequence of modules, because the quotient is projective.

If \(u\) is a unit on \(D+E\), multiplication by \(u\) preserves this sequence. In an adapted basis its matrix is block triangular. Expanding its determinant gives the product of the two diagonal-block determinants: a permutation term using an entry in the zero off-diagonal block vanishes, and every remaining term is a product of a permutation term in each diagonal block. On \(\mathcal O_D(-E)\) the determinant equals the determinant on \(\mathcal O_D\), since a local frame over \(D\) intertwines the two multiplication maps. We obtain

\[
\begin{aligned}
N_{D+E/S}(u)&=N_{D/S}(u|_D)\\
&\quad\cdot N_{E/S}(u|_E).
\end{aligned} \tag{5.6g}
\]

Now trivialize \(L\) on the entire finite scheme \(D+E\) after a base covering, and define \(\beta_L\) by

\[
\begin{aligned}
\nu_{L|_{D+E}}(\ell)&\longmapsto\\
&\nu_{L|_D}(\ell|_D)\\
&\quad\otimes\nu_{L|_E}(\ell|_E).
\end{aligned} \tag{5.6h}
\]

A frame change by \(u\) multiplies the source by the left side of (5.6g) and the target by its right side. Thus the maps glue, are intrinsic and are isomorphisms. The same calculation proves naturality for isomorphisms of \(L\).

For two line bundles \(L,M\), the route first using the tensor map on \(D+E\) and then (5.6b), and the route first using (5.6b) separately and then the two tensor maps, both send the original frames to

\[
\begin{aligned}
&\nu_{(L\otimes M)|_D}(\ell|_D\otimes m|_D)\\
&\quad\otimes\nu_{(L\otimes M)|_E}(\ell|_E\otimes m|_E).
\end{aligned} \tag{5.6i}
\]

In the second route one uses the ordinary flip to put the two \(D\) factors together and the two \(E\) factors together. This proves the full tensor/divisor interchange square as actual maps. For three or more divisors, provided their sums satisfy the stated hypotheses, trivialize on the total sum. Each parenthesized route sends the same frame to the ordered tensor of its restrictions. Reordering the divisors uses ordinary flips. Therefore all divisor associativity, symmetry and unit diagrams commute. The empty divisor contributes the unit line. Base change preserves the determinant and restriction formulas, proving the remaining compatibility. \(\square\)

**A collision which is not a disjoint union.** Let \(A\) be any ring, \(c\in A\), and

\[
B=A[t]/\bigl(t(t-c)\bigr).
\]

The divisors \(t=0\) and \(t=c\) on \(\mathbb A^1_A\) are effective Cartier divisors of degree one, with finite locally free sum of degree two. They collide when \(c=0\). In the basis \((1,t)\), multiplication by \(a+bt\) is

\[
\begin{aligned}
m_{a+bt}&=\begin{pmatrix}a&0\\b&a+bc\end{pmatrix},\\
N_{B/A}(a+bt)&=a(a+bc).
\end{aligned} \tag{5.6j}
\]

This is exactly the product of the restrictions to the two divisors, even when \(c\) is not invertible and no Chinese remainder decomposition exists. At \(c=0\) the fibre is \(A[t]/(t^2)\) and the norm is \(a^2\). The double point contributes its multiplicity two; replacing it by one reduced point would incorrectly give \(a\).

For the frame torsor of a line bundle, (5.6d) is the equivariance rule for pushout along the determinant norm \(p_*\mathbb G_{m,T}\to\mathbb G_{m,S}\). Thus the lemma gives the concrete multiplicative-group trace and its ramified divisor interchange. It does not establish symmetric-power descent or trace compatibility for every abelian sheaf or every other group in the original programme.


### 5.7. Norms through a tower

A trace also has to commute with a composite of finite maps. SGA4 XVII, Proposition 6.3.15(v), original printed pages 445–446, states this compatibility; Example 6.3.18 identifies its multiplicative-group case with the usual norm. We prove that case directly, including the actual maps on line bundles. The middle map need not have one rank on all components. Ramification, nilpotents and rank-zero components are allowed.

**Lemma 5.8 (norm transitivity).** Let \(p:T\to S\) and \(q:U\to T\) be finite locally free. Their composite is finite locally free. For every line bundle \(L\) on \(U\), there is a canonical natural isomorphism

\[
\begin{aligned}
\theta_{p,q,L}:N_{pq}(L)&\longrightarrow\\
&N_p\bigl(N_q(L)\bigr).
\end{aligned} \tag{5.7a}
\]

It commutes with the tensor and unit maps of Lemma 5.7 and with arbitrary base change. The two routes for three composable maps agree; consequently all parenthesizations for a longer tower agree. Disjoint-union norm maps also commute with these maps. On affine pieces \(A\to B\to C\), the underlying scalar identity is

\[
\begin{aligned}
N_{C/A}(u)&=\\
&N_{B/A}\bigl(N_{C/B}(u)\bigr)
\end{aligned} \tag{5.7b}
\]

for every \(u\in C\), including nonunits.

**Proof, first step: the variable ranks.** A finite projective module over a local ring is free. To recall the argument, lift a basis of its residue fibre to a map from a finite free module. Nakayama's lemma makes the map surjective. Projectivity splits it; its kernel is then finite projective with zero residue fibre, so Nakayama makes the kernel zero. Here the needed form of Nakayama itself follows from the determinant trick: if finitely many generators are linear combinations of themselves with coefficients in the maximal ideal, the adjugate of the resulting matrix shows that a determinant congruent to one annihilates them. That determinant is a unit.

A local basis spreads to a neighbourhood. A finite projective module and its dual are direct summands of finite free modules. Thus the finitely many basis vectors and coordinate maps over a localization can be lifted after clearing denominators. Their two inverse identities need only be checked on finitely many generators; clearing their remaining denominators gives inverse maps on an open neighbourhood. In particular its rank is locally constant and has finitely many values.

We will use the corresponding idempotents without a henselian assumption. For completeness, let a rank stratum in \(\operatorname{Spec}B\) be the clopen set \(V\), with complement \(W\). Quasicompactness gives finite principal-open covers of both sets. Let \(I,J\) be the ideals generated by their respective covering elements. Then \(I+J=B\). Every product of a chosen generator of \(I\) and one of \(J\) belongs to every prime, and hence is nilpotent. There are finitely many products, so \((IJ)^r=0\) for some \(r\). Also \(I^r+J^r=B\): expand \((x+y)^{2r-1}=1\) after choosing \(x\in I,y\in J,x+y=1\). Choose

\[
e\in I^r,\qquad 1-e\in J^r. \tag{5.7c}
\]

Their product is zero, so \(e^2=e\). At every point of \(V\), \(1-e\) is in the prime and \(e\) is not; on \(W\), \(e\) is in the prime. Thus \(D(e)=V\). Idempotents with the same support are equal: the idempotents \(e(1-e')\) and \(e'(1-e)\) have empty support, hence are nilpotent, hence zero. It follows that the idempotents of the different rank strata are orthogonal and sum to one.

Now localize \(A\) at a prime. As in Lemma 5.7, the finite algebra \(B\) is semilocal. Apply the rank-stratum decomposition to the finite projective \(B\)-module \(C\), obtaining

\[
B=\prod_j B_j,\qquad C=\prod_j C_j. \tag{5.7d}
\]

The \(B_j\)-rank of \(C_j\) is constant, say \(m_j\). A projective module of constant finite rank over a semilocal ring is free: choose a basis in each of its finitely many residue fibres; the module Chinese remainder map lifts the choices to one common list. At every maximal localization the resulting square matrix has invertible determinant, so the list is a basis there. The kernel and cokernel of the common map vanish because their maximal localizations vanish. Thus \(C_j\) is free over \(B_j\) of rank \(m_j\).

Each \(B_j\) is a direct summand of the finite projective \(A\)-module \(B\), so it is free over the local ring \(A\), say of rank \(n_j\). Also \(C\) is finite projective over \(A\): it is a direct summand of a finite sum of copies of \(B\). This proves finite local freeness of the composite. Its rank here is \(\sum_j n_jm_j\). A zero value of \(m_j\) gives the empty component and contributes the unit norm.

**Second step: restriction of scalars and determinants.** Let \(D\) be a semilocal algebra free of rank \(n\) over a local ring \(R\). For an \(m\)-by-\(m\) matrix \(M\) over \(D\), write \(\rho(M)\) for its \(R\)-linear matrix on \(D^m\). We prove

\[
\det_R\rho(M)=N_{D/R}(\det_D M). \tag{5.7e}
\]

First suppose \(M\) is invertible. Its first column \((a_1,\ldots,a_m)\) is unimodular. At each maximal residue field choose \(c_2,\ldots,c_m\) so that \(a_1+\sum_{i>1}c_i a_i\) is nonzero. If all the other entries vanish, unimodularity already makes \(a_1\) nonzero; otherwise one can prescribe the sum to be one. Chinese remaindering lifts all these coefficients simultaneously. The resulting sum is outside every maximal ideal, so it is a unit.

Add the chosen multiples of the other rows to the first row. Clear the rest of the first column using that unit pivot, and then clear the rest of the first row by column operations. The result is the pivot together with an invertible \((m-1)\)-by-\((m-1)\) block. Induction reduces \(M\) to a diagonal matrix using elementary row and column additions. No row interchange is needed.

An elementary addition has determinant one over \(D\). Its restricted matrix over \(R\) also has determinant one: in block form it has identity diagonal blocks and one off-diagonal multiplication block, and is triangular after ordering the two relevant blocks. A diagonal multiplication by a unit \(v\) in one coordinate has restricted determinant \(N_{D/R}(v)\). Determinant multiplicativity now proves (5.7e) for every invertible matrix. For \(m=0\), both sides are one by the empty-determinant convention.

To include all matrices, use a formal variable \(z\). The ring \(D[[z]]\) is semilocal: \(1-zb\) is invertible for every power series \(b\), so every maximal ideal contains \(z\), and the maximal ideals correspond to those of \(D\). It is free of rank \(n\) over the local ring \(R[[z]]\). The matrix \(1+zM\) is invertible, with inverse the formal geometric series. Apply the identity just proved to this matrix. Both sides are polynomials in \(z\). The coefficient of \(z^{mn}\) on the left is \(\det_R\rho(M)\). On the right, \(\det_D(1+zM)\) has highest possible coefficient \(\det_D M\) in degree \(m\); its multiplication matrix therefore has highest possible coefficient \(m_{\det_D M}\). Expanding its determinant gives \(N_{D/R}(\det_D M)\) in degree \(mn\). Equality of coefficients proves (5.7e), even if some leading coefficients are zero. No cancellation, domain hypothesis or generic-point argument is used.

Apply (5.7e) to multiplication by the component \(u_j\) of \(u\) on \(C_j\), and put \(v_j=N_{C_j/B_j}(u_j)\). A direct-sum multiplication matrix has determinant the product of its block determinants. Hence

\[
\begin{aligned}
N_{C/A}(u)&=\prod_j N_{C_j/A}(u_j),\\
&=\prod_j N_{B_j/A}(v_j),\\
&=N_{B/A}\bigl((v_j)_j\bigr).
\end{aligned} \tag{5.7f}
\]

Since \((v_j)_j=N_{C/B}(u)\), this proves (5.7b) after every localization of \(A\), hence over \(A\). The product decomposition came from rank strata of a finite projective module; it did not assume that arbitrary residue points lift to separate components.

**Third step: the actual tower maps.** Lemma 5.7 supplies a frame \(\ell\) of \(L\) over an open covering of the base \(S\), since \(U\to S\) is finite locally free. To distinguish its norms, write \(\nu_q(\ell)\), \(\nu_{pq}(\ell)\) and \(\nu_p(-)\) for the normalized determinant frames. Define (5.7a) by

\[
\nu_{pq}(\ell)\longmapsto\nu_p\bigl(\nu_q(\ell)\bigr). \tag{5.7g}
\]

Replacing \(\ell\) by \(u\ell\), with \(u\) a unit, multiplies the left frame by \(N_{C/A}(u)\) and the right by \(N_{B/A}(N_{C/B}(u))\). They are equal by (5.7b). Thus the prescription is independent of the frame and glues to an isomorphism. The same coefficient identity for an isomorphism between two line bundles proves naturality.

For tensor products, each route sends the tensor of two input norm frames to \(\nu_p(\nu_q(\ell\otimes h))\). For the unit, each sends the frame obtained from \(1\) to the frame obtained from \(1\). The ordinary symmetry interchanges the same two frames along both routes. This proves the tensor, unit and symmetry diagrams as actual maps.

For a third finite locally free map \(r:V\to U\), choose a frame over the full composite. Both routes from \(N_{pqr}(L)\) to \(N_pN_qN_r(L)\) send that frame to \(\nu_p(\nu_q(\nu_r(\ell)))\). Therefore the two maps are equal. The same description for any number of maps proves agreement of all parenthesizations, including the associativity pentagon. An identity map gives the same frame on both sides, proving the identity-tower triangles.

For a disjoint union \(U=U_1\amalg U_2\), the direct-sum determinant calculation gives the norm map to \(N(L|_{U_1})\otimes N(L|_{U_2})\): it sends a normalized frame to the tensor of its restrictions. Apply it either before or after (5.7g). With the outer tensor map of Lemma 5.7, both routes give the tensor of the same two iterated frames. Hence this diagram commutes too; the argument applies to any finite disjoint union, including the empty one. Ordinary lines are being tensored, so no uncancelled graded sign is inserted.

Finally, multiplication matrices, determinants and normalized frames commute with arbitrary ring base change. Formula (5.7g) is consequently the same formula after any base change. Since all the maps were characterized by these local frame prescriptions, the base-change diagrams commute without requiring that the chosen rank decomposition be chosen again on the new base. This proves every assertion. \(\square\)

**A tower with two different fibre lengths.** Let \(A\) be any commutative ring, and take

\[
\begin{aligned}
B&=A\times A,\\
C&=A[t]/(t^2)\times A[s]/(s^3).
\end{aligned} \tag{5.7h}
\]

The map to \(B\) has ranks two and three on its two components. Its composite to \(A\) has rank five. For \(u=(a+bt,c+ds+hs^2)\), multiplication on the first component has matrix

\[
\begin{pmatrix}a&0\\b&a\end{pmatrix},
\]

and on the second it has matrix

\[
\begin{pmatrix}c&0&0\\d&c&0\\h&d&c\end{pmatrix}.
\]

Thus the intermediate norm is \((a^2,c^3)\), the outer norm multiplies its two entries, and the direct norm is \(a^2c^3\). Both fibres are nonreduced, and their different lengths are essential. For a scalar \(w\in A\), this gives \(w^5\), exactly the degree law for the composite. The example concerns a genuine tower, not a disjoint enumeration of five geometric points.

## 6. Two cusp-form examples

### 6.1. The discriminant form

The form \(\Delta=\sum_{n\ge1}\tau(n)q^n\) spans \(S_{12}\), by the ring and dimension results of lesson 5. The coefficient at one is one, so \(\Delta\) is a normalized eigenform.

For completeness, let \(P(q)=\prod_{m\ge1}(1-q^m)^{24}=\sum_{r\ge0}b_rq^r\), so \(\tau(n)=b_{n-1}\). Its logarithmic derivative is
\[
qP'(q)=-24P(q)\sum_{j\ge1}\sigma_1(j)q^j,\qquad
rb_r=-24\sum_{j=1}^r\sigma_1(j)b_{r-j},\quad b_0=1.
\]
The divisor sums through five are \(1,3,4,7,6\). Successive substitution gives
\[
\begin{aligned}
b_1&=-24,\\
2b_2&=-24(-24+3)=504,\\
3b_3&=-24(252-72+4)=-4416,\\
4b_4&=-24(-1472+756-96+7)=19320,\\
5b_5&=-24(4830-4416+1008-168+6)=-30240.
\end{aligned}
\]
Hence
\[
\Delta=q-24q^2+252q^3-1472q^4+4830q^5-6048q^6+\cdots,
\]
\[
L(\Delta,s)=1-\frac{24}{2^s}+\frac{252}{3^s}-\frac{1472}{4^s}
+\frac{4830}{5^s}-\frac{6048}{6^s}+\cdots.
\]
The first two local denominators are
\[
1+24\,2^{-s}+2^{11-2s},\qquad 1-252\,3^{-s}+3^{11-2s}.
\]
The Hecke checks are \(\tau(4)=(-24)^2-2^{11}=-1472\) and \(\tau(6)=(-24)252=-6048\). At each prime the local roots have modulus \(p^{11/2}\), giving \(|\tau(p)|\le2p^{11/2}\).

Here \(\epsilon=i^{12}=1\), so \(\Lambda(\Delta,s)=\Lambda(\Delta,12-s)\). The classical centre is six and the unitary centre is \(1/2\). The positive sign does not itself force a zero there.

### 6.2. A forced zero in weight eighteen

The ring calculation identifies \(S_{18}=\Delta M_6\) and \(M_6=\mathbb CE_6\). Therefore \(f=\Delta E_6\) spans \(S_{18}\) and is a normalized eigenform. The divisor sums \(\sigma_5(n)\), for \(n=1,\ldots,5\), are \(1,33,244,1057,3126\). Thus
\[
E_6=1-504q-16632q^2-122976q^3-532728q^4-1575504q^5+\cdots.
\]
The complete coefficient multiplication through six is
\[
\begin{aligned}
a_1&=1,\\
a_2&=-24-504=-528,\\
a_3&=252+(-24)(-504)-16632=-4284,\\
a_4&=-1472+252(-504)+(-24)(-16632)-122976=147712,\\
a_5&=4830+(-1472)(-504)+252(-16632)+(-24)(-122976)-532728\\
&=-1025850,\\
a_6&=-6048+4830(-504)+(-1472)(-16632)+252(-122976)\\
&\quad+(-24)(-532728)-1575504=2261952.
\end{aligned}
\]
Hence
\[
f=q-528q^2-4284q^3+147712q^4-1025850q^5+2261952q^6+\cdots.
\]
The independent Hecke checks are
\[
a_4=(-528)^2-2^{17}=147712,\qquad a_6=(-528)(-4284)=2261952.
\]
The prime-two denominator is \(1+528\,2^{-s}+2^{17-2s}\). Since \(i^{18}=-1\),
\[
\Lambda(f,s)=-\Lambda(f,18-s),\qquad L(f,9)=0.
\]
Equivalently, \(L_{\mathrm u}(f,1/2)=0\). The coefficient calculations identify the form; the functional equation proves its central vanishing.

## 7. Exercises

1. **Easy.** Prove (3.1), specifying the domain of absolute convergence that permits rearrangement of the divisor sum.
2. **Medium.** Prove that \(\Lambda(f,s)\) is bounded on every vertical strip.
3. **Medium.** Prove the central vanishing for every level-one cusp form of weight \(k\equiv2\pmod4\).
4. **Hard.** Let \(k\ge2\) be even, and let \(a_n=O(n^c)\). Suppose
\[
\Lambda(s)=(2\pi)^{-s}\Gamma(s)\sum_{n\ge1}a_nn^{-s}
\]
initially defined for \(\operatorname{Re}s>\max(c+1,0)\), extends to an entire function bounded on every vertical strip and satisfies \(\Lambda(s)=i^k\Lambda(k-s)\). Prove that \(\sum_{n\ge1}a_nq^n\) is a cusp form of weight \(k\) for the full modular group. Justify Mellin inversion and the contour shift.

5. **Medium.** For a good-prime eigenform with character \(\chi\), prove that the coefficient bound \(|a_p|\le2p^{(k-1)/2}\) and the equal-modulus root assertion are equivalent. Identify the adjoint input needed for this implication, treat both repeated-root endpoints, and derive the bound for every index prime to the level. Explain why a bound on a complex trace alone would not suffice, using \(X^2-(i/2)X+1\).

6. **Medium.** Work over \(\mathbf Q_\ell\), including \(\ell=2\). Let \(W=\mathbf Q_\ell u\oplus\mathbf Q_\ell v\) have the alternating pairing \(\beta(u,v)=1\), let \(c:I\to\mathbf Q_\ell\) be a nonzero additive character, and put \(s=(-1)^{m+1}\). For \(\delta=u\), define \(N(w)=\beta(w,\delta)\delta\) and \(T_\sigma=1+s c(\sigma)N\). Compute the matrices, prove that the operators form an action preserving \(\beta\), and determine the invariant space. Show that the fixed line and its quotient are trivial representations but have no invariant complementary line. Explain what changes when \(\delta=0\). This is a linear-algebra model of the formula in Section 5.

7. **Medium.** For the split hyperbolic plane over \(\mathbf Z\), compute the wedge and contraction matrices on the ordered basis \((1,e)\), and verify the relation for \(e+f\), where \(f(e)=1\). For two planes, compute the total even projection on \((1,e_1,e_2,e_1\wedge e_2)\). Show why using an ordinary tensor action for both wedge operators fails the Clifford relation over \(\mathbf Z\). Explain why the correct construction still works over \(\mathbf F_2\).

8. **Hard.** In \(D^b(\mathbf Z\text{-}\mathrm{Mod})\), let \(B=\mathbf Z/2\) and let \(\delta:B\to B[1]\) be the connecting morphism of the extension \(0\to B\to\mathbf Z/4\to B\to0\), whose first map sends \(1\) to \(2\). Prove that \(\delta\ne0\). On \(K=B\oplus B[-1]\), use \(\delta[-1]\) to construct a nonzero endomorphism \(\gamma\) that induces zero on every cohomology group, and compute \(\gamma^2\). Explain the distinction between an isomorphism criterion based on cohomology and an equality criterion for morphisms.

9. **Medium.** Let \(A=R\times S\), where \(R,S\) are nonzero commutative rings, and let \(e=(1,0)\). For the finite projective module \(W=eA\), compute \(W^*\), both parity summands of \(\Lambda W\), the full Clifford algebra of \(H(W)\), and the centre of its even part. Write its two parity projections and the kernel of the natural scalar map \(A\times A\to Z(C(H(W))^0)\). Check the representation after each projection \(A\to R,S\), and explain why the positivity hypothesis in Corollary 5.2.1 cannot be dropped.

10. **Hard.** Let \(R=\mathbf F_2[\varepsilon]/(\varepsilon^2)\), let \(B=R/(\varepsilon)\), and work in \(D^b(R\text{-}\mathrm{Mod})\). Use the resolution with \(R\) in every nonpositive degree and differential multiplication by \(\varepsilon\) to compute \(\operatorname{Ext}_R^j(B,B)\). Let \(\delta:B\to B[1]\) be the class represented by \(1\) in degree one. By explicitly lifting it to a map of resolutions, prove \(\delta[1]\delta\ne0\). On \(K=B\oplus B[-1]\oplus B[-2]\), construct an endomorphism \(\gamma\) inducing zero on all cohomology, with \(\gamma^2\ne0\) and \(\gamma^3=0\). Show that \(\gamma^2\) factors through the canonical top projection while \(\gamma\) does not.


11. **Medium.** In \(V=\mathbf F_3^4\), with ordered coordinates \((t,x,y,z)\), let \(\ell=t\). For each \((a,b)\in\mathbf F_3^2\) other than \((2,2)\), take the identity map \(q_{a,b}:V\to V\) and the subspace
\[
S_{a,b}=\{(t,at,bt,z):t,z\in\mathbf F_3\}.
\]
Compute all points of \(\ell^{-1}(1)\) avoiding these eight subspaces. Then include the ninth subspace and explain why no point remains. Over a general finite field of size \(Q\), use the same construction to show that \(N<Q^2\) in the four-dimensional count cannot be weakened to \(N\le Q^2\) as a guarantee depending only on the number of obstructions.

12. **Medium.** Let \(A=\mathbf F_2[\varepsilon]/(\varepsilon^2)\), \(G=\mathbb G_{a,A}\), and \(E=A^2\). By comparing Laurent coefficients, prove that every character \(\mathbb G_{m,A}\to G\) is zero. Compute all equivariant automorphisms of the trivial \(G\)-torsor on \(\mathbb P^1_A\), listing them as translations. Explain why the coefficient calculation remains valid despite the nonzero nilpotent \(\varepsilon\).

13. **Medium.** Let \(A=\mathbf F_2[\varepsilon]/(\varepsilon^2)\), \(B=A[t]/\bigl(t(t-\varepsilon)\bigr)\), \(u=1+t\) and \(v=1+\varepsilon t\). Compute their norms, their product and the inverse of \(u\). Show that \(v\) is a nonidentity unit of norm one. Specialize \(\varepsilon\) to zero and explain how the norm still accounts for the two coincident divisors.

14. **Medium.** In the tower (5.7h), take \(A=\mathbf F_2[\varepsilon]/(\varepsilon^2)\) and put \(a=1+\varepsilon\). For
\[
\begin{aligned}
u&=(a+t,a+s),\\
v&=(1+\varepsilon t,1+\varepsilon s),
\end{aligned}
\]
compute the intermediate and direct norms, the product \(uv\), and both inverses. Show that \(v\) is a nonidentity unit of direct norm one. Compare the direct norm of \(u\) with the product of its two constant terms, and then specialize \(\varepsilon\) to zero. Explain the effect of the fibre lengths two and three.

## 8. Full solutions

### Solution 1

For \(\sigma>k\), the absolute sum of the proposed rearrangement is
\[
|c_k|\sum_{d,m\ge1}d^{k-1}(dm)^{-\sigma}
=|c_k|\zeta(\sigma)\zeta(\sigma-k+1)<\infty.
\]
Using \(a_n(E_k)=c_k\sum_{d\mid n}d^{k-1}\), and then \(n=dm\), gives
\[
\sum_{n\ge1}a_n(E_k)n^{-s}
=c_k\sum_{d,m\ge1}d^{k-1}(dm)^{-s}
=c_k\zeta(s)\zeta(s-k+1).
\]
The constant coefficient one is excluded from this Dirichlet series. Its Mellin contribution appears separately in (3.2).

### Solution 2

Fix real \(a\le b\). Split at one and apply the modular transformation below one:
\[
\Lambda(f,s)=\int_1^\infty f(iy)\bigl(y^{s-1}+i^ky^{k-s-1}\bigr)\,dy.
\]
For \(a\le\operatorname{Re}s\le b\), its absolute value is at most
\[
\int_1^\infty |f(iy)|\bigl(y^{b-1}+y^{k-a-1}\bigr)\,dy.
\]
Exponential decay makes this finite. The majorant contains no imaginary part, so it bounds the whole infinite strip.

### Solution 3

The transformation by \(S\) gives \(i^k=-1\), hence \(\Lambda(f,s)=-\Lambda(f,k-s)\). At \(s=k/2\), the value equals its negative and is zero. Since \(k/2>0\), Euler's integral gives \(\Gamma(k/2)>0\). Divide by the nonzero completion factor to get \(L(f,k/2)=0\). This applies to every cusp form of that weight, including arbitrary linear combinations of eigenforms.

### A Mellin inversion lemma

**Lemma 8.0 (the complex-analysis steps used in the Mellin arguments).** A holomorphic function has a convergent power series on every sufficiently small disk. On a connected open set it is determined by its values on a set with an interior accumulation point. A holomorphic function on a neighborhood of a closed rectangle has modulus at most its maximum on the boundary. If it is instead meromorphic there, has no pole on the boundary, and has finitely many simple poles in the interior, its positively oriented boundary integral is \(2\pi i\) times the sum of its residues. Locally uniform limits of holomorphic functions are holomorphic.

**Proof.** We include the contour foundations. For a closed triangle contained in the open set, subdivide into four similar triangles by joining side midpoints. The interior edges cancel in the sum of the oriented boundary integrals. If the original integral has modulus \(J\), some subtriangle has integral modulus at least \(J/4\). Iterating gives nested triangles \(D_n\), with diameters and perimeters respectively \(2^{-n}d\) and \(2^{-n}l\), and integral modulus at least \(4^{-n}J\). Their intersection is a single point \(z_0\). Complex differentiability gives
\[
\begin{gathered}
f(z)=f(z_0)+f'(z_0)(z-z_0)+r(z),\\
|r(z)|\le\eta|z-z_0|.
\end{gathered}
\]
on sufficiently small triangles, for every \(\eta>0\). The integrals of the constant and linear terms vanish, by their explicit polynomial primitives. The remaining integral is at most \(\eta ld\,4^{-n}\). Thus \(J\le\eta ld\) for every \(\eta\), forcing \(J=0\). Triangulating a polygon proves the same assertion for it. Shared edges cancel, including across a finite polygonal decomposition of a region with holes.

On a disk, the triangle assertion gives a primitive of any holomorphic function: integrate from a fixed point along a line segment, and compare neighboring segments using their triangle. The change along the small joining segment, divided by its increment, tends to the value of the function by continuity. This proves the primitive derivative directly. The same construction on small disks shows that a contour integral is invariant under a homotopy avoiding singularities: subdivide the parameter square into sufficiently small rectangles whose images lie in disks with such primitives; their integrals cancel. Such a finite subdivision exists by uniform continuity and a finite disk cover of the compact homotopy image. This applies to piecewise smooth contour homotopies.

Choose a closed filled disk contained in the open set, a point \(z\) in its interior, and apply this invariance to \(f(\zeta)/(\zeta-z)\) on the annulus between the circle and a small circle about \(z\). The latter integral tends to \(2\pi i f(z)\): its constant part integrates to that value under \(\zeta=z+re^{it}\), and continuity bounds the remaining integral by \(2\pi\sup_{|\zeta-z|=r}|f(\zeta)-f(z)|\to0\). Hence
\[
\begin{gathered}
f(z)=\frac1{2\pi i}\int_{|\zeta-p|=R}
\frac{f(\zeta)}{\zeta-z}\,d\zeta,\\
|z-p|<R.
\end{gathered}
\]
For \(|z-p|\le r<R\), expand the denominator as the uniformly convergent geometric series in \((z-p)/(\zeta-p)\). Integration gives
\[
\begin{gathered}
f(z)=\sum_{j\ge0}c_j(z-p)^j,\\
c_j=\frac1{2\pi i}\int_{|\zeta-p|=R}
\frac{f(\zeta)}{(\zeta-p)^{j+1}}\,d\zeta,\\
|c_j|\le R^{-j}\max_{|\zeta-p|=R}|f(\zeta)|.
\end{gathered}
\]
These bounds also justify termwise differentiation on smaller disks. A nonzero series whose constant term is zero factors as \((z-p)^h\) times a series with a nonzero constant, so its zero at \(p\) is isolated. If zeros accumulate, every coefficient at that limit point is zero and the function vanishes on a disk. The set of points with a vanishing neighborhood is then open and closed in the connected domain: at a limit point, an accumulating sequence of zeros forces the same conclusion. This proves the identity assertion, including equality of two functions by applying it to their difference.

At an interior local maximum, rotate the function by a constant phase to make \(f(p)=M\ge0\). The circle formula at its centre says \(f(p)\) is the mean of \(f\) on every sufficiently small circle. There \(\operatorname{Re}f\le|f|\le M\), and the mean is \(M\). The nonnegative continuous function \(M-\operatorname{Re}f\) therefore has zero integral and is zero everywhere on that circle. Since \(|f|\le M\), its imaginary part is also zero. This holds on every such circle, giving constancy on a disk and then on the connected domain. If \(M=0\), the same conclusion is immediate. Compactness supplies a maximum on a closed rectangle; an interior maximum forces constancy, so in either case the boundary maximum bounds it.

For the residue assertion, a simple pole at \(p\) means precisely that \(f(z)-c_p/(z-p)\) extends holomorphically near \(p\), where \(c_p\) is its residue. Subtract all these principal parts. The remainder is holomorphic on a neighborhood of the rectangle, so its boundary integral is zero by the triangle proof. The integral of \(1/(z-p)\) on the boundary is \(2\pi i\): shrink the rectangle around its interior point through contours avoiding \(p\), and evaluate on a small circle as above. Adding the principal parts proves the claimed formula with its positive orientation.

Finally a locally uniform limit may be passed through the circle formula, since its circle is compact. The resulting integral of the continuous limit has a convergent power series on every smaller disk by the same geometric expansion. Thus the limit is holomorphic. This also applies to integrals obtained as locally uniform limits of holomorphic finite integrals. \(\square\)

The freely available text of Lebl, Sections 2.4 and 3.2–3.3, provides background for these classical steps. The proofs needed for the rectangle shifts, strip bound and identity arguments have been written here.

**Lemma 8.1 (smooth Mellin inversion).** Let \(b\in\mathbb R\) and \(\phi\in C^2((0,\infty))\). Suppose, for \(j=0,1,2\),
\[
\int_0^\infty |\phi^{(j)}(y)|y^{b+j}\,\frac{dy}{y}<\infty.
\tag{8.3}
\]
Then \(\mathcal M\phi(b+it)=\int_0^\infty\phi(y)y^{b+it}\,dy/y\) is \(O((1+|t|)^{-2})\), and, for every \(y>0\),
\[
\phi(y)=\frac{y^{-b}}{2\pi}\int_{\mathbb R}
\mathcal M\phi(b+it)y^{-it}\,dt.
\tag{8.4}
\]
The integral is absolutely convergent.

**Proof.** Write \(y=e^x\) and \(H(x)=e^{bx}\phi(e^x)\). Direct differentiation gives
\[
\begin{aligned}
H'(x)&=bH(x)+e^{(b+1)x}\phi'(e^x),\\
H''(x)&=b^2H(x)\\
&\quad+(2b+1)e^{(b+1)x}\phi'(e^x)\\
&\quad+e^{(b+2)x}\phi''(e^x).
\end{aligned}
\tag{8.5}
\]
Thus \(H,H',H''\in L^1(\mathbb R)\). Since \(H'\) is integrable, the fundamental theorem of calculus makes \(H\) have finite limits at both ends of the real line. Its integrability makes both limits zero. Apply the same argument to \(H'\), using \(H''\in L^1\), to get \(H'(x)\to0\) at both ends. In particular, \(H\) is bounded and continuous.

Set \(M(t)=\int_{\mathbb R}H(x)e^{itx}\,dx\), which is the stated Mellin transform. Twice integrating by parts on finite intervals and then letting the endpoints tend to infinity gives, for \(t\ne0\),
\[
M(t)=-\frac1{t^2}\int_{\mathbb R}H''(x)e^{itx}\,dx.
\]
The endpoint terms vanish by the preceding limits. Consequently \(|M(t)|\le\|H\|_1\) for all \(t\), and \(|M(t)|\le |t|^{-2}\|H''\|_1\) for \(t\ne0\). These bounds prove the claimed decay and \(M\in L^1(\mathbb R)\).

We now prove the inversion step. The Gaussian transform proved in Poisson summation, theta, and the functional equation, Lemma 2.1, gives, for \(\varepsilon>0\),
\[
\begin{aligned}
K_\varepsilon(v)&=\frac1{2\pi}\int_{\mathbb R}
e^{-\varepsilon t^2}e^{itv}\,dt\\
&=\frac{e^{-v^2/(4\varepsilon)}}{\sqrt{4\pi\varepsilon}}.
\end{aligned}
\tag{8.6}
\]
Indeed that lemma uses \(e^{-2\pi iu\xi}\); take its Gaussian parameter to be \(\varepsilon/\pi\) and \(\xi=-v/(2\pi)\). The resulting \(K_\varepsilon\) is nonnegative and has integral one. The continuous double-integral interchange in lesson 01, Lemma 0.3(2), is justified by
\(\|H\|_1\int_{\mathbb R}e^{-\varepsilon t^2}\,dt<\infty\), so
\[
\begin{gathered}
\frac1{2\pi}\int_{\mathbb R}e^{-\varepsilon t^2}M(t)e^{-itx}\,dt\\
=\int_{\mathbb R}H(u)K_\varepsilon(u-x)\,du\\
=\int_{\mathbb R}H(x+v)K_\varepsilon(v)\,dv.
\end{gathered}
\tag{8.7}
\]
For a fixed \(x\), continuity makes \(|H(x+v)-H(x)|\) arbitrarily small when \(|v|<\delta\). The integral over that interval is bounded by the same small number. On its complement, boundedness gives the upper bound
\(2\|H\|_\infty\int_{|v|\ge\delta}K_\varepsilon(v)\,dv\), which tends to zero after the substitution \(v=2\sqrt\varepsilon\,w\). Hence the right side of (8.7) tends to \(H(x)\). On the left side, \(M\in L^1\), the common continuous majorant \(|M(t)|\), and uniform convergence of the Gaussian multiplier on compact intervals permit the limit as \(\varepsilon\downarrow0\), by lesson 01, Lemma 0.3(2). This proves
\(H(x)=(2\pi)^{-1}\int M(t)e^{-itx}\,dt\). Multiply by \(e^{-bx}\) and substitute \(y=e^x\) to obtain (8.4). No general Fourier-inversion theorem is needed. \(\square\)

### Solution 4: Hecke's converse, with the contour estimate

Put \(\epsilon=i^k\). Choose a nonnegative integer \(C\ge c\), enlarge the coefficient constant so that \(|a_n|\le An^C\), and define
\[
f(z)=\sum_{n\ge1}a_ne^{2\pi inz},\qquad g(y)=f(iy).
\]
An exponential dominates every polynomial, so the series and every fixed derivative converge normally on compact subsets of the upper half-plane. Thus \(f\) is holomorphic, has period one, and decays exponentially as \(\operatorname{Im}z\to\infty\), uniformly in \(\operatorname{Re}z\).

For \(j=0,1,2\),
\[
g^{(j)}(y)=\sum_{n\ge1}a_n(-2\pi n)^je^{-2\pi ny}.
\]
For \(0<y\le1\), this is \(O(y^{-C-j-1})\). To justify that bound explicitly, dominate the summand \(n^{C+j}e^{-2\pi ny}\) on \([n-1,n]\) by \((x+1)^{C+j}e^{-2\pi xy}\) and sum the integrals. After \(u=xy\), the resulting integral is
\[
y^{-C-j-1}\int_0^\infty(u+y)^{C+j}e^{-2\pi u}\,du
\le y^{-C-j-1}\int_0^\infty(u+1)^{C+j}e^{-2\pi u}\,du.
\]
At \(y\ge1\), the same series give exponential decay. Therefore, for \(b>C+1\), all three functions
\[
y^bg(y),\qquad y^{b+1}g'(y),\qquad y^{b+2}g''(y)
\]
are integrable for \(dy/y\).

Lemma 8.1 now applies with \(\phi=g\). It proves the decay \(\mathcal Mg(b+it)=O((1+|t|)^{-2})\) and the absolutely convergent inversion
\[
g(y)=\frac1{2\pi i}\int_{b-i\infty}^{b+i\infty}\mathcal Mg(s)y^{-s}\,ds.
\tag{8.1}
\]
The finite absolute majorant
\(\Gamma(b)(2\pi)^{-b}\sum_n|a_n|n^{-b}\) permits termwise integration and identifies \(\mathcal Mg(s)=\Lambda(s)\) on that line.

We need decay throughout a strip to move the contour. Boundedness alone does not imply that its horizontal integrals vanish. We supply the additional estimate.

**Boundary estimate.** For fixed \(b>0\), Euler's integral with \(u=e^x\) is
\[
\Gamma(b+it)=\int_{\mathbb R}H_b(x)e^{itx}\,dx,\qquad H_b(x)=e^{bx-e^x}.
\]
Every derivative of \(H_b\) is a polynomial in \(e^x\) times \(H_b\). At minus infinity these derivatives decay like \(e^{bx}\); at plus infinity the factor \(e^{-e^x}\) dominates each such polynomial. They are integrable and tend to zero at both ends. Four integrations by parts give
\[
|\Gamma(b+it)|\le |t|^{-4}\|H_b^{(4)}\|_1\qquad(|t|\ge1).
\]
For \(|t|\le1\), Euler's integral bounds its modulus by \(\Gamma(b)\). The Dirichlet series is uniformly bounded on \(b>C+1\) by its absolute numerical sum. Hence
\(\Lambda(b+it)=O((1+|t|)^{-4})\). The functional equation gives the same bound on \(a=k-b\).

**Strip estimate.** Suppose \(G\) is holomorphic on a neighborhood of the closed strip \(a\le\operatorname{Re}s\le b\), has polynomial growth in \(|\operatorname{Im}s|\) uniformly there, and has modulus at most \(K\) on its two boundary lines. We prove that \(|G|\le K\) throughout the strip.

Put \(h=(a+b)/2\), choose \(0<\kappa<\pi/(b-a)\), and, for \(\delta>0\), multiply \(G(s)\) by
\[
\exp\bigl(-\delta\cos(\kappa(s-h))\bigr).
\]
If \(s=\sigma+it\) lies in the strip, then
\[
\operatorname{Re}\cos(\kappa(s-h))
=\cos(\kappa(\sigma-h))\cosh(\kappa t)
\ge c_\kappa\cosh(\kappa t)>0,
\]
where \(c_\kappa=\cos(\kappa(b-a)/2)>0\). The multiplier has modulus at most one on the vertical edges. On the horizontal edges at heights \(\pm T\), its decay dominates the polynomial growth of \(G\). For any \(\eta>0\), these horizontal values are eventually at most \(K+\eta\). On a compact rectangle a continuous modulus attains its maximum. If this occurs in the interior, the maximum modulus principle makes the function constant and transfers the value to the boundary. Thus the boundary bound makes the product at most \(K+\eta\). Let the rectangles exhaust the strip, then \(\eta\downarrow0\), and finally \(\delta\downarrow0\). This proves the asserted bound, also when \(K=0\).

Choose now \(b>\max(C+1,k/2,0)\), let \(a=k-b<b\), and choose \(R>1-a\). The assumed boundedness of \(\Lambda\) on this strip makes
\(G(s)=(s+R)^2\Lambda(s)\) of polynomial growth there. The boundary estimate bounds \(G\) on both edges. The proved strip estimate bounds it everywhere. Since \(\operatorname{Re}(s+R)>1\),
\[
|\Lambda(\sigma+it)|\le\frac{K'}{1+t^2}
\qquad(a\le\sigma\le b).
\tag{8.2}
\]

For fixed \(y>0\), apply Cauchy–Goursat to the two triangles of a rectangle; their common edge cancels. Use the entire function \(\Lambda(s)y^{-s}\) on the rectangle with vertical sides \(a,b\) and horizontal sides at \(\pm T\). On the horizontal sides, \(|y^{-s}|=y^{-\sigma}\) is bounded independently of \(T\), and (8.2) makes their integrals tend to zero. Both vertical integrals converge absolutely. Thus (8.1) shifts to \(a=k-b\) without any residue. The functional equation and the substitution \(w=k-s\), with its reversed orientation, give
\[
\begin{aligned}
g(y)&=\frac1{2\pi i}\int_{a-i\infty}^{a+i\infty}\Lambda(s)y^{-s}\,ds\\
&=\frac{\epsilon y^{-k}}{2\pi i}\int_{b-i\infty}^{b+i\infty}\Lambda(w)y^w\,dw
=\epsilon y^{-k}g(1/y).
\end{aligned}
\]
Because \(\epsilon^2=1\), this is \(f(i/y)=(iy)^kf(iy)\). The holomorphic functions \(f(-1/z)\) and \(z^kf(z)\) agree on the positive imaginary axis, which has limit points in the upper half-plane. The identity theorem extends their equality throughout it. Period one gives the transformation by \(T\); these two transformations give modularity for the generators \(S,T\), hence for \(SL_2(\mathbb Z)\).

The Fourier series has no constant term and decays at infinity. The full modular group has a single cusp orbit, so modularity transports this cusp condition to every cusp. Therefore \(f\in S_k(SL_2(\mathbb Z))\). Its prescribed coefficients give the original Dirichlet series; uniqueness follows from the uniqueness of a Fourier expansion. This proves the converse with its bounded-strip hypothesis and its complete contour justification. \(\square\)

### Solution 5

Theorem 4.2 of the level Hecke lesson gives \(T_p^*=\chi(p)^{-1}T_p\). Apply the adjoint identity to \(f,f\) and cancel the positive Petersson norm; with the product linear in its first variable this gives \(a_p=\chi(p)\overline{a_p}\). Choose \(\eta^2=\chi(p)\), put \(R=p^{(k-1)/2}\), and set \(x=a_p/(\eta R)\). Since \(\overline\eta=\eta^{-1}\), the preceding identity makes \(x\) real. Substituting \(X=\eta R Z\) changes the local polynomial into \(Z^2-xZ+1\).

The coefficient bound is now \(|x|\le2\). Write \(x=2\cos\theta\); the normalized roots are \(e^{\pm i\theta}\) and have modulus one. Rescale to obtain modulus \(R\). Conversely, if both original roots have modulus \(R\), their sum has modulus at most \(2R\). At \(x=2\) the two normalized roots are \(1\); at \(x=-2\) both are \(-1\). Their inverse Euler factors are respectively \((1-T)^{-2}\) and \((1+T)^{-2}\), whose degree-\(r\) coefficients are \(r+1\) and \((-1)^r(r+1)\). Restoring the factor \(\eta^rR^r\) agrees with the finite-sum formula (5.1d) at both endpoints.

At each good prime this gives \(|a_{p^r}|\le(r+1)p^{r(k-1)/2}\). For \((n,N)=1\), multiplicativity over its prime factorization gives (5.1i). This proof makes no assertion about a bad-prime factor.

For the proposed counterexample, the trace has modulus \(1/2\le2\) and the constant coefficient is one, but the roots are
\[
\frac{i(1+\sqrt{17})}4,
\qquad \frac{i(1-\sqrt{17})}4.
\tag{8.8}
\]
Their moduli are \((1+\sqrt{17})/4>1\) and \((\sqrt{17}-1)/4<1\). Thus the bound on an arbitrary complex trace does not force equal root moduli. This polynomial fails the adjoint phase condition: for character value one, that condition requires a real trace. The modular implication uses that condition as well as the bound. \(\square\)

### Solution 6

Alternation gives \(\beta(u,u)=\beta(v,v)=0\) and \(\beta(v,u)=-1\). Thus \(N(u)=0\), \(N(v)=-u\), and, in the ordered basis \((u,v)\),
\[
N=\begin{pmatrix}0&-1\\0&0\end{pmatrix},
\qquad
T_\sigma=\begin{pmatrix}1&-s c(\sigma)\\0&1\end{pmatrix}.
\]
In particular \(N^2=0\). Since \(c(\sigma\tau)=c(\sigma)+c(\tau)\), multiplication gives
\[
\begin{aligned}
T_\sigma T_\tau
&=1+s\bigl(c(\sigma)+c(\tau)\bigr)N\\
&=T_{\sigma\tau}.
\end{aligned}
\]
Also \(T_1=1\) and \(T_\sigma^{-1}=T_{\sigma^{-1}}\), so this is an action. Its vectors satisfy \(T_\sigma u=u\) and \(T_\sigma v=v-s c(\sigma)u\). Their pairing remains one, and each self-pairing remains zero. Bilinearity therefore proves preservation of \(\beta\) on all of \(W\).

For \(a,b\in\mathbf Q_\ell\),
\[
T_\sigma(au+bv)-(au+bv)=-s c(\sigma)b u.
\]
Some \(c(\sigma)\ne0\), so this vanishes for every \(\sigma\) exactly when \(b=0\). Hence \(W^I=\mathbf Q_\ell u=\ker N\). The line \(\mathbf Q_\ell u\) is fixed, and the class of \(v\) is fixed in the quotient. Suppose an invariant complementary line existed. Its projection onto \(W/\mathbf Q_\ell u\) would be an equivariant isomorphism, so every vector on that line would be fixed. This contradicts the computed invariant space. Equivalently, an operator with \(c(\sigma)\ne0\) has characteristic polynomial \((X-1)^2\) but only one eigenline, and is not diagonalizable.

If \(\delta=0\), then \(N=0\), every \(T_\sigma=1\), and \(W^I=W\); every complementary line is now invariant. These calculations take place in characteristic zero also when \(\ell=2\), so the sign and alternation arguments remain valid. \(\square\)

### Solution 7

In the basis \((1,e)\),
\[
L=\begin{pmatrix}0&0\\1&0\end{pmatrix},\qquad
I=\begin{pmatrix}0&1\\0&0\end{pmatrix}.
\]
Thus \(L^2=I^2=0\), \(LI+IL=1\), and \((L+I)^2=1\), as required by \(Q(e+f)=1\). The even projection is \(IL=\operatorname{diag}(1,0)\).

For two planes, even–even and odd–odd give the basis elements \(1\) and \(e_1\wedge e_2\). Hence (5.2b) gives
\[
e=\operatorname{diag}(1,0,0,1).
\]
With the ordinary tensor action, \(L_1\otimes1\) and \(1\otimes L_2\) commute. Their sum has square \(2L_1\otimes L_2\), which sends the vacuum \(1\otimes1\) to \(2e_1\otimes e_2\ne0\). But \(Q(e_1+e_2)=0\), so this is not a Clifford action over \(\mathbf Z\). The graded action (5.2d) makes the two cross terms cancel instead. Over \(\mathbf F_2\), their signs coincide and their sum is still zero. Exterior squares remain zero, the matrix-unit proof still applies, and even and odd degree remain distinct grading components. Thus the correct construction and its two centre projections survive characteristic two.

### Solution 8

The extension does not split: an element of \(\mathbf Z/4\) mapping to \(1\in B\) is odd and has order four. It cannot be the image of \(1\) under a homomorphism from the group \(B\) of order two. More explicitly, the projective resolution
\[
0\longrightarrow\mathbf Z\xrightarrow{2}\mathbf Z
\longrightarrow B\longrightarrow0
\]
becomes a two-term complex with zero differential after applying \(\operatorname{Hom}_{\mathbf Z}(-,B)\). Hence
\[
\operatorname{Ext}^1_{\mathbf Z}(B,B)=B.
\]
Lift the generator of the quotient \(B\) to \(1\in\mathbf Z/4\). Twice this lift is the image of \(1\) in the kernel, so the extension class is the nonzero generator of this Ext group. Under its identification with \(\operatorname{Hom}_{D^b}(B,B[1])\), that class is \(\delta\).

Let \(p:K\to B[-1]\) be the second projection and \(i:B\to K\) the first inclusion. Define
\[
\gamma=i\delta[-1]p.
\]
Its component from the second summand to the first is \(\delta[-1]\ne0\), so \(\gamma\ne0\). The first summand has cohomology only in degree zero, and the second only in degree one. In each degree the cross-component therefore induces the zero map. Thus \(H^j(\gamma)=0\) for every \(j\). Nevertheless, since \(pi=0\),
\
\gamma^2=i\delta[-1\delta[-1]p=0.
\]
This is an exact example, with no numerical approximation.

A morphism of complexes is an isomorphism in the derived category exactly when its cone has zero cohomology. Consequently isomorphisms can be detected on all cohomology groups. Equality of two derived maps requires their difference itself to be zero; the computed \(\gamma\) proves that zero cohomology maps alone do not ensure this. Lemma 5.3 uses truncation triangles to prove an actual factorization, and Lemma 5.4 proves an actual identity through the adjunction formulas.

### Solution 9

The decomposition \(A=eA\oplus(1-e)A\) makes \(W\) finite projective. A functional on \(eA\) is determined by its value on \(e\); that value must lie in \(eA\), since \(f(e)=ef(e)\). Conversely every such value defines an \(A\)-linear functional. Thus \(W^*\cong eA\). The module is cyclic, so all exterior powers above degree one vanish. We obtain
\[
E^{\mathrm{even}}=A,\qquad E^{\mathrm{odd}}=eA.
\]
Over the \(R\) component \(E\) is \(R^2\), with ordered basis \((1,e)\); over the \(S\) component it is \(S\). The corollary therefore gives
\[
\begin{gathered}
C(H(W))\cong M_2(R)\times S,\\
C(H(W))^0\cong R\times R\times S.
\end{gathered}
\]
The latter algebra is commutative, so it is already its centre. Its coordinates represent the even \(R\) line, the odd \(R\) line and the even \(S\) line. The parity projections are respectively
\[
e_{\mathrm{even}}=(1,0,1),\qquad
 e_{\mathrm{odd}}=(0,1,0).
\]
For \(a=(a_R,a_S)\), \(b=(b_R,b_S)\), the two scalar actions give
\[
\begin{gathered}
(a,b)\longmapsto(a_R,b_R,a_S),\\
\ker=\{((0,0),(0,s)):s\in S\}.
\end{gathered}
\]
This nonzero kernel shows precisely why the canonical two-factor scalar-centre statement fails here. The actual centre is also \(A\times R\), by rearranging its three coordinates.

Under \(A\to R\), \(W\) becomes the free rank-one module. Wedge by \(e\) and contraction by its dual have the matrices of Solution 7 and generate \(M_2(R)\). Under \(A\to S\), \(W\) becomes zero, so the exterior module and Clifford algebra both become \(S\), with identity representation and no odd part. These are exactly the base changes of the displayed decomposition. The example works over characteristic two as well. The representation has no positive-rank restriction; its centre has two scalar factors only when both parity modules have positive local rank everywhere.

The evaluation ideal in this example is exactly \(eA\): all values lie there, and the functional determined by \(f(e)=e\) attains its generator. Thus Corollary 5.2.2 gives \(A\times eA\cong A\times R\), and its scalar map is exactly the one computed above. Under the two component maps, the evaluation idempotent becomes respectively one and zero. This identifies both base changes and the kernel as instances of the general variable-rank formula.

### Solution 10

Every element of \(R\) has a unique expression \(a+b\varepsilon\), with \(a,b\in\mathbf F_2\). Multiplication by \(\varepsilon\) sends it to \(a\varepsilon\), so its kernel and image are both \(\varepsilon R\). The augmented complex
\[
\begin{gathered}
\cdots\xrightarrow{\varepsilon}R\xrightarrow{\varepsilon}R,\\
R\xrightarrow{\varepsilon}R\longrightarrow B\longrightarrow0.
\end{gathered}
\]
is therefore a projective resolution. Write it as \(P^{-j}=R\) for \(j\ge0\), with \(d^{-j}=\varepsilon\) for \(j\ge1\) and \(d^0=0\). After applying \(\operatorname{Hom}_R(-,B)\), every differential is zero because \(\varepsilon B=0\). Hence
\[
\operatorname{Ext}_R^j(B,B)\cong B
\qquad(j\ge0).
\]
We use the usual projective-resolution computation and its identification with derived morphisms, as in Solution 8.

Define a map \(D:P\to P[1]\) by the identity from \(P^{-j}\) to \(P[1]^{-j}=P^{-j+1}\) when \(j\ge1\), and by zero in degree zero. Below degree minus one, the differentials on both sides are multiplication by \(\varepsilon\): the sign in a shifted complex disappears in characteristic two. At degree minus one, both composites in the chain-map identity are zero. Thus \(D\) is a chain map. Composing it with the shifted augmentation \(P[1]\to B[1]\) gives the cocycle \(1\) in degree one, so it represents \(\delta\).

The composite \(D[1]D:P\to P[2]\) is the identity in each degree at most minus two and zero in the remaining degrees. After the augmentation to \(B[2]\), it is the cocycle \(1\) in degree two. The Hom complex has zero differentials, so this class is nonzero. Therefore
\[
\delta[1]\delta\ne0
\quad\text{in }\operatorname{Hom}(B,B[2]).
\]
This checks the composition itself, rather than deducing it merely from the sizes of the Ext groups.

In the ordered summands \((B,B[-1],B[-2])\), define
\[
\gamma=
\begin{pmatrix}
0&\delta[-1]&0\\
0&0&\delta[-2]\\
0&0&0
\end{pmatrix}.
\]
Each summand has cohomology only in its corresponding degree \(0,1,2\). Every nonzero component of \(\gamma\) goes to a summand in a different degree, so \(H^j(\gamma)=0\) for all \(j\). Its square has only the component from \(B[-2]\) to \(B\), namely
\[
(\gamma^2)_{0,2}=(\delta[1]\delta)[-2]\ne0.
\]
A third application is zero because \(\gamma\) kills the first summand. Thus \(\gamma^2\ne0\) and \(\gamma^3=0\).

Let \(p_2:K\to B[-2]\) be the third projection and \(i_0:B\to K\) the first inclusion. Then
\[
\gamma^2=i_0(\delta[1]\delta)[-2]p_2,
\]
which is the top-cohomology factorization promised by Corollary 5.3.1 for two transitions and amplitude \([0,2]\). In contrast, if \(\gamma=hp_2\), its restriction to the second summand would be zero. That restriction is \(i_0\delta[-1]\), and projecting it back to \(B\) recovers the nonzero \(\delta[-1]\). This contradiction proves that one transition does not suffice in this example. Its nonzero square and zero cube also attain the three-transition nilpotence bound of Corollary 5.3.2 for this amplitude.

### Solution 11

The vectors \((1,a,b,0)\) and \((0,0,0,1)\) form a basis of \(S_{a,b}\): their first and fourth coordinates prove independence, and their linear combinations give exactly its definition. Thus every subspace has dimension two and codimension two in \(V\). On the slice \(t=1\), its points are precisely
\[
S_{a,b}\cap\ell^{-1}(1)
=\{(1,a,b,z):z\in\mathbf F_3\}.
\]
Different indices \((a,b)\) give disjoint sets because the second and third coordinates recover the index. The slice has \(3^3=27\) points, and each of the eight forbidden sets has three. A point avoids them exactly when \((x,y)=(2,2)\), so all allowed points are
\[
(1,2,2,0),\quad(1,2,2,1),\quad(1,2,2,2).
\]
Their number is \(27-8\cdot3=3\), attaining the lower bound \(Q^3-NQ\) at \(Q=3,N=8\). Adding \(S_{2,2}\) removes exactly these three points and leaves none.

Over \(\mathbf F_Q\), the same two basis vectors prove \(\dim S_{a,b}=2\). The \(Q^2\) distinct indices give disjoint sets of \(Q\) slice points, covering all \(Q^3\) points. Every restriction map is still the identity and hence injective. Therefore the original four-dimensional hypotheses hold at \(N=Q^2\), yet avoidance fails. This proves sharpness of the strict count-only sufficient threshold, without an optimality assertion about any particular geometric section problem.

### Solution 12

A scheme map \(\mathbb G_{m,A}\to\mathbb G_{a,A}\) is a Laurent polynomial \(f(T)=\sum_n a_nT^n\), with finitely many nonzero coefficients. It is a group homomorphism precisely when
\[
f(TU)=f(T)+f(U)
\]
in \(A[T^{\pm1},U^{\pm1}]\). For each \(n\ne0\), the coefficient of \(T^nU^n\) on the left is \(a_n\), whereas it is zero on the right: neither exponent there can be simultaneously nonzero. Hence all such \(a_n\) vanish. Comparison of the constant coefficients gives \(a_0=2a_0\), so \(a_0=0\) by subtraction, over any coefficient ring. Thus the character is zero.

The trivial base torsor and zero character have image the trivial torsor on \(\mathbb P^1_A\). Lemma 5.6 identifies every equivariant automorphism with a unique base translation by an element of \(A\). Its elements are exactly \(0,1,\varepsilon,1+\varepsilon\), so the four maps are
\[
\begin{gathered}
x\mapsto x,\quad x\mapsto x+1,\\
x\mapsto x+\varepsilon,\quad x\mapsto x+1+\varepsilon.
\end{gathered}
\]
Their composition adds the translating elements; in characteristic two each is its own inverse. The four maps are distinct, as evaluation at the zero section gives their distinct translating elements. Finally, Laurent monomials are a free \(A\)-module basis, so coefficient comparison detects even nilpotent coefficients. The argument never cancels \(\varepsilon\) and never treats \(A\) as a domain.

### Solution 13

The basis \((1,t)\) and relation \(t^2=\varepsilon t\) give

\[
\begin{aligned}
N(u)&=1+\varepsilon,\qquad N(v)=1,\\
uv&=1+(1+\varepsilon)t.
\end{aligned} \tag{8.11}
\]

For the product, the term \(\varepsilon t^2=\varepsilon^2t\) vanishes. Direct multiplication gives

\[
\begin{aligned}
u^{-1}&=1+(1+\varepsilon)t,\\
v^2&=1.
\end{aligned} \tag{8.12}
\]

Indeed the coefficient of \(t\) in \(u\,u^{-1}\) is \(1+(1+\varepsilon)+(1+\varepsilon)\varepsilon=0\). Thus both are units, and multiplicativity also gives \(N(uv)=1+\varepsilon=N(u)N(v)\). The element \(v\) differs from \(1\) because \(B\) is free over \(A\) on \((1,t)\) and its \(t\) coefficient \(\varepsilon\) is nonzero. Its norm is nevertheless one, so the norm on units need not be injective.

After \(\varepsilon\mapsto0\), the algebra becomes \(\mathbf F_2[t]/(t^2)\), \(u\) becomes the nonidentity unit \(1+t\), and \(v\) becomes \(1\). The multiplication matrix for \(a+bt\) now has both diagonal entries \(a\), so its norm is \(a^2\). The two divisor restrictions both take the value \(a\), and their product is \(a^2\) even though the supports coincide. Every calculation used the free polynomial basis; no nilpotent was cancelled.


### Solution 14

In characteristic two, \(a^2=1\), \(a^3=a\), and \(a\varepsilon=\varepsilon\). The triangular multiplication matrices give

\[
\begin{aligned}
N_{C/B}(u)&=(1,a),\\
N_{C/A}(u)&=a,\\
N_{C/B}(v)&=(1,1),\\
N_{C/A}(v)&=1.
\end{aligned} \tag{8.13}
\]

Direct multiplication, using \(t^2=0\) and \(s^3=0\), gives

\[
\begin{aligned}
(uv)_1&=a+(1+\varepsilon)t,\\
(uv)_2&=a+(1+\varepsilon)s+\varepsilon s^2.
\end{aligned} \tag{8.14}
\]

The constant terms are still \(a,a\), so the intermediate norm of the product is \((1,a)\) and its direct norm is \(a\), in agreement with norm multiplicativity. Explicit inverses are

\[
\begin{aligned}
(u^{-1})_1&=a+t,\\
(u^{-1})_2&=a+s+a s^2,\\
v^{-1}&=v.
\end{aligned} \tag{8.15}
\]

Indeed \((a+t)^2=a^2+t^2=1\). Multiplying the two second-component polynomials gives

\[
(a+s)(a+s+a s^2)=1:
\]

the linear terms cancel, the quadratic coefficient is \(a^2+1=0\), and the cubic term vanishes. Each component of \(v\) squares to one because \(\varepsilon^2=0\). The element \(v\) is nonidentity: its first-component coefficient of \(t\) is the nonzero element \(\varepsilon\) in the free basis \((1,t)\). Norm one therefore does not imply that a unit is identity.

The product of the two constant terms of \(u\) is \(a^2=1\). Its actual direct norm is \(a^2a^3=a^5=a=1+\varepsilon\), which differs from one. Taking each constant term only once discards the fibre lengths. The tower computation retains lengths two and three even though both fibres have one underlying point.

After \(\varepsilon\mapsto0\), the unit \(u\) becomes \((1+t,1+s)\), with inverse \((1+t,1+s+s^2)\), and remains nonidentity. The unit \(v\) becomes identity. Both intermediate norms become \((1,1)\) and both direct norms become one. This is the same base-change computation as in Lemma 5.8. All identities follow from free polynomial bases and the displayed relations; no nilpotent is cancelled.

## What this lesson does not prove

* Euler's Gamma integral, meromorphic continuation and entire reciprocal are proved in The Gamma function and Stirling's formula, Theorems 1.1–1.2. The Gamma recurrence used at integer arguments is part of Theorem 1.1. Solution 4 proves the vertical-line decay needed here directly.
* The continuation of \(\zeta\), its sole pole at one of residue one, its negative even zeros and the special values in Section 3.1 are proved in Poisson summation, theta, and the functional equation, Corollary 3.2, Theorems 3.3 and 4.2, and Example 4.3. The Eisenstein product and its regularized Mellin continuation are proved here.
* The Gaussian transform used in Lemma 8.1 is proved in that same programme lesson, Lemma 2.1. Lemma 8.1 proves smooth Mellin inversion from it, including the vanishing boundary terms, absolute integrability of the transform and the limiting convolution argument. Solution 4 checks all three weighted hypotheses.
* Lemma 8.0 proves the identity theorem, rectangle Cauchy/residue formula, maximum modulus principle, and locally uniform holomorphic limit needed here. Its proof supplies the triangle, circle and power-series steps from complex differentiability. The strip estimate itself is proved in Solution 4.
* The continuous series, Gaussian double-integral and holomorphic-parameter interchanges used in the Mellin arguments have earlier proofs in lesson 01, Lemma 0.3. Each use has the compact-uniform convergence and explicit integrable majorants supplied above. General measurable Fubini/Tonelli is not supplied by this lemma.
* Ramanujan–Petersson in the primitive holomorphic good-prime root formulation: Deligne, *La conjecture de Weil I*, Theorem (8.2). The written Deligne construction lesson, Lemma 4.1, Proposition 4.2, and Theorem 4.3, supplies the conditional parabolic-cohomology and triangle-inequality deductions. Its construction theorem, projective Weil purity, and stated geometric hypotheses remain inputs. Section 5 and the optimal discriminant bound use the root theorem. Proposition 5.1 and Solution 5 independently prove the phase normalization and root/coefficient equivalence from the level Hecke lesson, Theorem 4.2. Continuation, central vanishing, and the converse do not depend on the optimal bound.

## References

* J. S. Milne, *Modular Functions and Modular Forms*, author lecture notes, version 1.31 (2017), Section 9, Theorems 9.2–9.3, for the Mellin correspondence. [Free author text](https://www.jmilne.org/math/CourseNotes/MF.pdf). Sections 1–4 and Lemma 8.1 above give the written coefficient, continuation, constant-term and inversion arguments in the conventions used here.

* P. Deligne, “La conjecture de Weil I,” *Publications Mathématiques de l'IHÉS* 43 (1974), 273–307, Theorem (8.2) and Remark (8.3). [Free original article at NUMDAM](https://www.numdam.org/item/PMIHES_1974__43__273_0/).
* J. Lebl, *A Guide to Cultivating Complex Analysis*, version 1.9, Sections 2.4 and 3.2–3.3. [Author text](https://www.jirka.org/ca/).
* D. H. Fremlin, *Measure Theory*, Volume 2, Chapter 25, Section 252. [Author's volumes](https://www1.essex.ac.uk/maths/people/fremlin/mt.htm).
* *NIST Digital Library of Mathematical Functions*, Sections 5.2, 25.2 and 25.6, for the exact Gamma and zeta reference statements.
* P. Deligne, SGA4, Exposé XVIII, Lemma 2.14.2, Corollary 2.14.4, Proposition 3.1.17 and Lemma 3.2.3–Theorem 3.2.5, original printed pages 561–563 and 580–586. [Original XVII–XVIII scan](https://publications.ias.edu/sites/default/files/Number4.pdf).
