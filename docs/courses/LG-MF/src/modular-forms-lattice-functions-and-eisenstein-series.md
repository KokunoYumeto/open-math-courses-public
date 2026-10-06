# Modular forms, lattice functions and Eisenstein series

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A modular form changes predictably when a lattice basis changes. Summing inverse powers of the nonzero lattice points produces the first examples. Their Fourier coefficients turn out to be divisor sums. Weight two is the boundary case: the lattice sum loses absolute convergence, and the correction needed to recover its transformation law depends on the height in the upper half-plane.

We use Modular curves and their genus and elementary complex analysis. The convergence, lattice reindexing, cotangent residues, Bernoulli recurrence and weight-two continuation below form the mathematical derivation. Freely accessible comparison sources are [Voight open book, §§40.1–40.3] and [Stein author PDF, §2.1 and Chapter 5]. No source comparison substitutes for a local proof.

**Lemma 0.1 (analytic consequences used in the series arguments).** Using the Cauchy formula and theorem proved in lesson 01, Lemma 0.2, a locally uniform limit of holomorphic functions is holomorphic, a bounded isolated puncture is removable, and a normally convergent holomorphic series can be differentiated term by term.

*Proof.* On a closed disc strictly inside the domain, uniform convergence on its boundary permits passage to the limit in Cauchy's formula. The resulting integral is holomorphic in its interior, as differentiating the kernel \((\zeta-z)^{-1}\) on smaller discs is uniformly justified. This also gives convergence of every derivative on smaller discs and proves the differentiation assertion. At a puncture, Cauchy's theorem on an annulus gives the Laurent coefficients
\[
a_n=\frac1{2\pi i}\int_{|\zeta|=r}
F(\zeta)\zeta^{-n-1}\,d\zeta,
\]
independent of the circle radius. The Laurent expansion itself follows by expanding the two Cauchy kernels on the bounding circles into geometric series. If \(|F|\le M\) near zero, then for \(j\ge1\), \(|a_{-j}|\le Mr^j\); let \(r\downarrow0\). All negative coefficients vanish, so the Taylor expansion extends \(F\) across zero. The same circle formula gives uniqueness of the Taylor and Laurent coefficients used below. \(\square\)

Throughout,
\[
z=x+iy\in\mathfrak H,\qquad q=e^{2\pi iz},\qquad
T=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
S=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]
Weights are integers. A sum marked with a prime omits the zero pair or the zero lattice point.

## 1. The slash operator and the cusp condition

For a real matrix \(\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\) of positive determinant, set
\[
j(\gamma,z)=cz+d.
\]
It does not vanish on \(\mathfrak H\). On \(\mathrm{SL}_2(\mathbb R)\) define
\[
(f|_k\gamma)(z)=j(\gamma,z)^{-k}f(\gamma z).
\]

**Proposition 1.1 (the right slash action).** For \(\gamma,\delta\in\mathrm{SL}_2(\mathbb R)\),
\[
j(\gamma\delta,z)=j(\gamma,\delta z)j(\delta,z),\qquad
(f|_k\gamma)|_k\delta=f|_k(\gamma\delta).
\]
The slash operators preserve holomorphic functions and act linearly.

**Proof.** Write the bottom row of \(\gamma\) as \((c,d)\) and
\(\delta=\begin{pmatrix}a'&b'\\c'&d'\end{pmatrix}\). Then
\[
j(\gamma,\delta z)j(\delta,z)
=\left(c\frac{a'z+b'}{c'z+d'}+d\right)(c'z+d')
=(ca'+dc')z+cb'+dd',
\]
which is the bottom-row expression for \(\gamma\delta\). Substituting this identity into
\[
((f|_k\gamma)|_k\delta)(z)
=j(\delta,z)^{-k}j(\gamma,\delta z)^{-k}f(\gamma\delta z)
\]
proves the action law. The identity matrix acts trivially. Composition with a holomorphic fractional linear map and multiplication by a nowhere vanishing holomorphic factor preserve holomorphy. Linearity follows directly. \(\square\)

For later Hecke operators, we fix the extension to \(\mathrm{GL}_2^+(\mathbb Q)\):
\[
(f|_k\gamma)(z)=\det(\gamma)^{\,k-1}j(\gamma,z)^{-k}f(\gamma z).
\tag{1.1}
\]
The same computation, together with multiplicativity of the determinant, proves the right action law. This normalization gives
\(f|_k(\lambda I)=\lambda^{k-2}f\) for positive rational \(\lambda\). It agrees with the preceding definition on determinant-one matrices.

Let \(\Gamma\) be any subgroup of finite index in \(\mathrm{SL}_2(\mathbb Z)\); we do not require \(-I\in\Gamma\).

**Definition.** A modular form of weight \(k\) for \(\Gamma\) is a holomorphic function \(f:\mathfrak H\to\mathbb C\) such that

1. \(f|_k\gamma=f\) for every \(\gamma\in\Gamma\);
2. for every \(\alpha\in\mathrm{SL}_2(\mathbb Z)\), \(f|_k\alpha\) is bounded on \(y\ge1\).

The second condition is holomorphy at the cusps. A cusp form satisfies the stronger condition
\((f|_k\alpha)(x+iy)\to0\), uniformly in \(x\), as \(y\to\infty\), for every \(\alpha\).
We write \(M_k(\Gamma)\) and \(S_k(\Gamma)\) for these vector spaces.

Here is the exact connection with Fourier expansions, including odd weights at irregular cusps.

**Proposition 1.2 (Fourier coordinates at a cusp).** Let \(\alpha\in\mathrm{SL}_2(\mathbb Z)\), and let \(h\) be the projective width of the cusp \(\alpha\infty\). Choose a lift \(\varepsilon T^h\in\alpha^{-1}\Gamma\alpha\), where \(\varepsilon\in\{1,-1\}\). For a \(\Gamma\)-invariant function of weight \(k\), put \(F=f|_k\alpha\). Then
\[
F(z+h)=\varepsilon^k F(z).
\tag{1.2}
\]
If \(\varepsilon^k=1\), use \(W=h\); if \(\varepsilon^k=-1\), use \(W=2h\). The cusp condition is equivalent to an expansion
\[
F(z)=\sum_{n\ge0}a_n e^{2\pi inz/W}.
\tag{1.3}
\]
The cusp-form condition is equivalent to \(a_0=0\). In the second case, all even-index coefficients vanish, so (1.3) consists of positive half-integral powers of \(q_h=e^{2\pi iz/h}\).

**Proof.** The conjugation action and Proposition 1.1 give
\(F|_k(\varepsilon T^h)=F\). Since
\(j(\varepsilon T^h,z)=\varepsilon\), this is (1.2). In either case \(F\) has period \(W\). Consequently it descends, by the map \(q_W=e^{2\pi iz/W}\), to a holomorphic function on the punctured unit disc. Boundedness for sufficiently large \(y\) is boundedness near its puncture. The removable singularity theorem gives precisely the Taylor series (1.3). Conversely that series is bounded near the puncture. Periodicity and continuity on the compact rectangle \(0\le x\le W,\ 1\le y\le Y\) extend the bound to all \(y\ge1\).

A Taylor series with \(a_0=0\) tends uniformly to zero as \(q_W\to0\); the converse follows by taking its limit. When \(W=2h\), translation by \(h\) sends \(q_W\) to \(-q_W\). Equation (1.2) then says the Taylor series is odd, proving the last assertion. \(\square\)

Changing a cusp representative replaces \(F(z)\) by \((\pm1)^{-k}F(z+r)\) for an integer \(r\), after a transformation in \(\Gamma\). Thus boundedness and vanishing of the constant term are independent of the choice. Finite index also means that only finitely many slash translates must be checked: if \(\alpha=\gamma\beta\), with \(\gamma\in\Gamma\), then \(f|_k\alpha=f|_k\beta\).

If \(-I\in\Gamma\), invariance gives \(f=(-1)^k f\). Hence all odd-weight forms vanish. When \(-I\notin\Gamma\), one must retain the sign in (1.2). For example, the irregular cusp \(1/2\) of \(\Gamma_1(4)\) has projective width one and negative lift; an odd-weight form there has only odd powers of \(e^{\pi iz}\), rather than arbitrary integral powers of \(e^{2\pi iz}\).

Products of forms of weights \(k\) and \(\ell\) have weight \(k+\ell\). A product is a cusp form if either factor is a cusp form. These statements follow from the transformation law and from boundedness, or vanishing, of each slash translate.

## 2. Functions on lattices

A lattice in \(\mathbb C\) is a subgroup
\(\Lambda=\mathbb Z\omega_1+\mathbb Z\omega_2\) with \(\omega_1,\omega_2\) linearly independent over \(\mathbb R\). We can choose the order of the basis so that \(\operatorname{Im}(\omega_1/\omega_2)>0\).

**Theorem 2.1 (the lattice dictionary).** Functions \(f:\mathfrak H\to\mathbb C\) satisfying
\[
f(\gamma z)=j(\gamma,z)^k f(z)\quad
(\gamma\in\mathrm{SL}_2(\mathbb Z))
\tag{2.1}
\]
correspond bijectively to functions \(\Phi\) on lattices satisfying
\[
\Phi(\lambda\Lambda)=\lambda^{-k}\Phi(\Lambda)
\quad(\lambda\in\mathbb C^\times).
\tag{2.2}
\]
The two constructions are
\[
f(z)=\Phi(\mathbb Zz+\mathbb Z),\qquad
\Phi(\Lambda)=\omega_2^{-k}f(\omega_1/\omega_2).
\tag{2.3}
\]

**Proof.** If \(z'=\gamma z\), then
\[
\mathbb Zz'+\mathbb Z
=(cz+d)^{-1}\bigl(\mathbb Z(az+b)+\mathbb Z(cz+d)\bigr)
=(cz+d)^{-1}(\mathbb Zz+\mathbb Z).
\]
The last equality uses the invertibility of \(\gamma\) over \(\mathbb Z\).
Homogeneity therefore gives (2.1).

Conversely, two bases of the same lattice are related by an integral matrix of determinant \(\pm1\). If both ratios lie in \(\mathfrak H\), the identity
\[
\operatorname{Im}\frac{a\omega_1+b\omega_2}{c\omega_1+d\omega_2}
=\frac{\det(\gamma)\operatorname{Im}(\omega_1/\omega_2)}
 {|c(\omega_1/\omega_2)+d|^2}
\]
forces determinant \(+1\). For \(z=\omega_1/\omega_2\), the new second basis vector is \(\omega'_2=(cz+d)\omega_2\). Equation (2.1) gives
\[
(\omega'_2)^{-k}f(\omega'_1/\omega'_2)
=\omega_2^{-k}(cz+d)^{-k}f(\gamma z)
=\omega_2^{-k}f(z).
\]
Thus (2.3) is well-defined. Scaling both basis vectors proves (2.2), and the two formulas plainly undo one another. \(\square\)

No analytic condition is hidden in this set-theoretic dictionary. The associated function must still be holomorphic on \(\mathfrak H\) and bounded at the cusp to be a modular form. Also, a bare lattice forgets level structure: for a proper subgroup \(\Gamma\), one retains a basis modulo the changes allowed by \(\Gamma\). An arbitrary \(\Gamma\)-invariant function need not descend to a function on unmarked lattices.

Since \(-\Lambda=\Lambda\), an odd-degree homogeneous function on bare lattices is zero. The lattice description recovers the odd-weight obstruction for the full modular group.

## 3. Convergence and the cotangent identity

**Lemma 3.1 (lattice sums).** For real \(s>2\),
\[
\sum_{(m,n)\ne(0,0)}|mz+n|^{-s}
\tag{3.1}
\]
converges locally uniformly for \(z\in\mathfrak H\). For each fixed \(z\), it diverges when \(s=2\).

**Proof.** The real linear map \((m,n)\mapsto mz+n\) is invertible because \(y>0\). Its inverse varies continuously with \(z\). On a compact set \(K\subset\mathfrak H\), there is therefore \(a_K>0\) such that
\[
|mz+n|\ge a_K\max(|m|,|n|).
\]
The square shell \(\max(|m|,|n|)=r\) contains
\((2r+1)^2-(2r-1)^2=8r\) integer pairs. Its contribution is at most
\(8a_K^{-s}r^{1-s}\), a summable bound when \(s>2\).
For fixed \(z\), the reverse bound
\[
|mz+n|\le (|z|+1)\max(|m|,|n|)
\]
makes the shell contribution for \(s=2\) at least
\(8(|z|+1)^{-2}/r\). The harmonic series diverges. \(\square\)

For an integer \(k>2\), it follows that
\[
G_k(\Lambda)=\sum_{\omega\in\Lambda\setminus\{0\}}\omega^{-k},
\qquad
G_k(z)=\sum_{(m,n)\ne(0,0)}(mz+n)^{-k}
\tag{3.2}
\]
are absolutely convergent. The second is holomorphic by local uniform convergence. Reindexing the first gives \(G_k(\lambda\Lambda)=\lambda^{-k}G_k(\Lambda)\), so Theorem 2.1 proves its transformation law. Pairing \(\omega\) and \(-\omega\) shows that \(G_k=0\) for odd \(k\).

We next compute its Fourier expansion without importing a sine product.

**Lemma 3.2 (partial fractions of the cotangent).** For \(z\notin\mathbb Z\),
\[
\pi\cot(\pi z)=\frac1z+
\sum_{n\ge1}\left(\frac1{z-n}+\frac1{z+n}\right)
=\frac1z+\sum_{n\ge1}\frac{2z}{z^2-n^2}.
\tag{3.3}
\]
The paired series converges normally away from the integers.

**Proof.** First take \(z\ne0\) fixed. Integrate
\(\pi\cot(\pi w)/(w^2-z^2)\) around the square with real and imaginary coordinates between \(-R\) and \(R\), where \(R=M+1/2\). On its vertical sides \(\cot(\pi w)\) is bounded by one in absolute value; on its horizontal sides it is bounded uniformly as \(M\to\infty\), using its exponential expression. The denominator has absolute value at least \(R^2-|z|^2\), and the perimeter is \(8R\). The integral therefore tends to zero.

At an integer \(n\), the residue is \(1/(n^2-z^2)\). At \(z\) and \(-z\), the two residues sum to \(\pi\cot(\pi z)/z\). The residue theorem gives
\[
0=-\frac1{z^2}+\sum_{n\ge1}\frac{2}{n^2-z^2}
+\frac{\pi\cot(\pi z)}z,
\]
which rearranges to (3.3). The terms \(2z/(z^2-n^2)\) are bounded by \(C_K/n^2\) on every compact set avoiding the poles. This proves normal convergence and allows termwise differentiation. \(\square\)

**Theorem 3.3 (Lipschitz formula).** For every integer \(k\ge2\) and \(z\in\mathfrak H\),
\[
\sum_{n\in\mathbb Z}(z+n)^{-k}
=\frac{(-2\pi i)^k}{(k-1)!}
 \sum_{r\ge1}r^{k-1}e^{2\pi irz}.
\tag{3.4}
\]

**Proof.** On \(\mathfrak H\), \(|q|<1\) and
\[
\pi\cot(\pi z)=\pi i\frac{q+1}{q-1}
=-\pi i-2\pi i\sum_{r\ge1}q^r.
\]
Differentiate this equality and (3.3) exactly \(k-1\) times. Both series can be differentiated locally uniformly. The left side becomes
\((-1)^{k-1}(k-1)!\sum_{n\in\mathbb Z}(z+n)^{-k}\);
the right becomes
\(-(2\pi i)^k\sum_{r\ge1}r^{k-1}q^r\).
Dividing gives (3.4), including its sign for odd \(k\). \(\square\)

## 4. Bernoulli numbers and the Fourier expansion

Define the Bernoulli numbers by
\[
\frac{t}{e^t-1}=\sum_{n\ge0}B_n\frac{t^n}{n!}.
\tag{4.1}
\]
The apparent singularity at zero is removable, and the function is holomorphic for \(|t|<2\pi\).

**Proposition 4.1 (recurrence and zeta values).** We have \(B_0=1\), \(B_1=-1/2\), \(B_n=0\) for odd \(n>1\), and
\[
B_n=-\frac1{n+1}\sum_{j=0}^{n-1}\binom{n+1}{j}B_j
\quad(n\ge1).
\tag{4.2}
\]
For every even integer \(k\ge2\),
\[
\zeta(k)=-\frac{(2\pi i)^k B_k}{2k!}.
\tag{4.3}
\]

**Proof.** Multiplying (4.1) by \(e^t-1\) and comparing coefficients first gives \(B_0=1\), and then
\(\sum_{j=0}^n\binom{n+1}{j}B_j=0\) for \(n\ge1\).
This proves (4.2) and the rationality of all \(B_n\). The function
\[
\frac{t}{e^t-1}+\frac t2=\frac t2\frac{e^t+1}{e^t-1}
\]
is even. Thus \(B_1=-1/2\) and the remaining odd coefficients vanish.

For \(0<|z|<1\), substitute \(t=2\pi iz\) into (4.1):
\[
\pi\cot(\pi z)
=\pi i+\frac1z\sum_{n\ge0}B_n\frac{(2\pi iz)^n}{n!}
=\frac1z+\sum_{m\ge1}
 \frac{B_{2m}(2\pi i)^{2m}}{(2m)!}z^{2m-1}.
\]
On the other hand, (3.3) and the geometric series give
\[
\pi\cot(\pi z)=\frac1z-2\sum_{m\ge1}\zeta(2m)z^{2m-1}.
\]
The double sum is absolutely convergent on \(|z|\le r<1\), because it is bounded by
\(2\sum_{n\ge1}r/[n^2(1-r^2/n^2)]\).
Comparing coefficients proves (4.3). \(\square\)

In particular, \(B_2=1/6\) and \(B_4=-1/30\) give
\[
\zeta(2)=-\frac{(2\pi i)^2}{2\cdot2!}\frac16=\frac{\pi^2}{6},
\qquad
\zeta(4)=-\frac{(2\pi i)^4}{2\cdot4!}\left(-\frac1{30}\right)
=\frac{\pi^4}{90}.
\]

For positive \(n\), write
\(\sigma_r(n)=\sum_{d\mid n,\ d>0}d^r\).

**Theorem 4.2 (the normalized Eisenstein series).** For every even \(k\ge4\),
\[
G_k(z)=2\zeta(k)+
\frac{2(2\pi i)^k}{(k-1)!}\sum_{n\ge1}\sigma_{k-1}(n)q^n,
\tag{4.4}
\]
and
\[
E_k(z):=\frac{G_k(z)}{2\zeta(k)}
=1-\frac{2k}{B_k}\sum_{n\ge1}\sigma_{k-1}(n)q^n
\in M_k(\mathrm{SL}_2(\mathbb Z)).
\tag{4.5}
\]

**Proof.** The row \(m=0\) of (3.2) contributes \(2\zeta(k)\).
Rows \(m\) and \(-m\) agree, since \(k\) is even. Apply (3.4) to each positive row:
\[
G_k(z)=2\zeta(k)+
\frac{2(2\pi i)^k}{(k-1)!}
\sum_{m\ge1}\sum_{r\ge1}r^{k-1}q^{mr}.
\]
Grouping by \(n=mr\) gives the divisor sum in (4.4). The grouping is justified by absolute convergence: if \(|q|\le R<1\),
\[
\sum_{r,m\ge1}r^{k-1}R^{mr}
\le\frac1{1-R}\sum_{r\ge1}r^{k-1}R^r<\infty.
\]
Division by \(2\zeta(k)\), followed by (4.3), proves (4.5). We already proved holomorphy and the transformation law. The Fourier series is bounded at infinity, with constant term one. All cusps of the full modular group are equivalent, and every slash translate of \(E_k\) equals \(E_k\), so the cusp condition holds at every cusp. \(\square\)

A useful second description is
\[
E_k(z)=\frac12
\sum_{\substack{c,d\in\mathbb Z\\\gcd(c,d)=1}}(cz+d)^{-k}.
\tag{4.6}
\]
Indeed every nonzero pair is uniquely \(r(c,d)\), where \(r>0\) and \((c,d)\) is primitive; consequently \(G_k=2\zeta(k)E_k\). The factor \(1/2\) in (4.6) identifies the two signs of a primitive pair.

Our \(E_k\) has constant term one. The coefficient-one normalization used in the free [Stein author PDF, §2.1] is obtained by a direct scalar calculation:
\[
E_k^{\mathrm{Stein}}=-\frac{B_k}{2k}E_k.
\]
Indeed the coefficient of \(q\) in \(E_k\) is \(-2k/B_k\), because \(\sigma_{k-1}(1)=1\); multiplying by \(-B_k/(2k)\) therefore makes that coefficient one. Throughout this lesson \(B_n\) means the signed coefficient in (4.1), with \(B_1=-1/2\). Both the constant and the sign of every Fourier prefactor follow from that defining series and Proposition 4.1.

## 5. The boundary case: weight two

The holomorphic series
\[
E_2(z)=1-24\sum_{n\ge1}\sigma_1(n)q^n
\tag{5.1}
\]
converges locally uniformly, since \(\sigma_1(n)\le n^2\). It is periodic, but it is not a modular form of weight two.

We will prove its transformation law by introducing a convergent lattice sum, continuing the convergence parameter to zero, and keeping track of the constant Fourier coefficient. This also avoids using the discriminant before its construction in the next lesson.

**Lemma 5.1 (Hecke's convergence factor).** For \(\operatorname{Re}s>0\), define
\[
H(z,s)=y^s\sum_{(m,n)\ne(0,0)}
(mz+n)^{-2}|mz+n|^{-2s}.
\tag{5.2}
\]
For each \(z\), it extends holomorphically in \(s\) to a neighbourhood of zero. Its value there is
\[
H(z,0)=\frac{\pi^2}{3}
-8\pi^2\sum_{n\ge1}\sigma_1(n)q^n-\frac{\pi}{y}.
\tag{5.3}
\]
For every \(\gamma\in\mathrm{SL}_2(\mathbb Z)\),
\[
H(\gamma z,0)=j(\gamma,z)^2H(z,0).
\tag{5.4}
\]

**Proof.** The absolute value of a summand in (5.2) is
\(y^{\operatorname{Re}s}|mz+n|^{-2-2\operatorname{Re}s}\).
Lemma 3.1 proves convergence, locally uniformly in \(z\) and \(s\) in the stated domain. For \(\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\), reindex by
\((m,n)\mapsto(ma+nc,mb+nd)\). The identity
\(\operatorname{Im}(\gamma z)=y/|cz+d|^2\) gives
\[
H(\gamma z,s)=(cz+d)^2H(z,s).
\tag{5.5}
\]
The factors \(|cz+d|^{2s}\) from the summands and \(|cz+d|^{-2s}\) from the height cancel.

We now construct the continuation explicitly. The row \(m=0\) contributes
\(2\zeta(2+2s)y^s\). The rows \(m\) and \(-m\) agree. For \(v>0\), periodize
\[
F_{s,v}(t)=(t+iv)^{-2}(t^2+v^2)^{-s}.
\]
For \(\operatorname{Re}s>0\), its periodization has Fourier coefficients
\[
I_r(s,v)=\int_{\mathbb R}F_{s,v}(t)e^{-2\pi irt}\,dt,
\quad r\in\mathbb Z.
\tag{5.6}
\]
Indeed termwise integration on a period interval unfolds the integral on \(\mathbb R\). The periodization and all its derivatives converge uniformly, so two integrations by parts give absolutely summable Fourier coefficients. To see that the Fourier series equals the function, one may use
\[
K_M(t)=\frac1M\left|\sum_{j=0}^{M-1}e^{2\pi ijt}\right|^2.
\]
This kernel is nonnegative, has integral one on a period, and has mass tending to zero outside every neighbourhood of the integers. Uniform continuity therefore makes its convolution with any continuous periodic function tend uniformly to that function. These convolutions are the arithmetic means of its Fourier partial sums. For an absolutely convergent Fourier series the same means tend to its sum, proving the assertion without any additional summation theorem.

First compute the constant coefficient. The odd part of the integrand integrates to zero, and integration of the derivative of
\(t(t^2+v^2)^{-s-1}\) gives
\[
I_0(s,v)=
\int_{\mathbb R}\frac{t^2-v^2}{(t^2+v^2)^{s+2}}\,dt
=-\frac{s}{s+1}J(s)v^{-1-2s},
\quad
J(s)=\int_{\mathbb R}(1+u^2)^{-s-1}\,du.
\tag{5.7}
\]
For clarity, if \(A=\int(t^2+v^2)^{-s-1}dt\), the integrated derivative says
\(\int t^2(t^2+v^2)^{-s-2}dt=A/(2s+2)\).
Subtracting the complementary \(v^2\) term gives (5.7).
The boundary term vanishes for \(\operatorname{Re}s>-1/2\).
The integral defining \(J\) is holomorphic in that half-plane, and \(J(0)=\pi\).

After summing (5.7) over positive \(m\), both signs contribute
\[
-\frac{2sJ(s)}{s+1}\zeta(1+2s)y^{-1-s}.
\tag{5.8}
\]
The pole in this expression cancels. Here is the needed local zeta calculation:
\[
\zeta(1+u)-\frac1u
=\sum_{n\ge1}\left(n^{-1-u}
-\int_n^{n+1}t^{-1-u}\,dt\right).
\tag{5.9}
\]
It holds initially for \(\operatorname{Re}u>0\), by summing the integrals from one to infinity. On compact subsets of \(\operatorname{Re}u>-1\), the summands are bounded by a constant times \(n^{-2-\operatorname{Re}u}\), using the derivative of \(t^{-1-u}\). Thus the right side is holomorphic there. In particular \(u\zeta(1+u)\to1\). Expression (5.8) consequently has value \(-\pi/y\) at zero.

It remains to continue the nonconstant coefficients, with estimates strong enough to sum them. Define
\(\Gamma(a)=\int_0^\infty e^{-t}t^{a-1}dt\) for \(\operatorname{Re}a>0\).
Integration by parts proves
\(\Gamma(a+1)=a\Gamma(a)\), and \(\Gamma(1)=1\).
Near \(s=0\) we use \(1/\Gamma(s)=s/\Gamma(s+1)\), which is holomorphic and has a simple zero. We take a sufficiently small \(0<\delta<1/4\) so that \(\Gamma(s+1)\) and \(\Gamma(s+2)\) do not vanish for \(|s|\le\delta\); this follows from their continuity and their values at zero.

For \(\operatorname{Re}s>0\), the elementary Laplace identity
\[
\lambda^{-a}=\frac1{\Gamma(a)}
\int_0^\infty t^{a-1}e^{-\lambda t}\,dt
\quad(\operatorname{Re}\lambda>0)
\]
follows first for real positive \(\lambda\) by substitution, then for complex \(\lambda\) by holomorphy. Since \(t+iv=i(v-it)\), it yields
\[
F_{s,v}(t)=
-\frac1{\Gamma(s+2)\Gamma(s)}
\int_0^\infty\int_0^\infty
a^{s+1}b^{s-1}e^{-v(a+b)}e^{it(a-b)}\,da\,db.
\tag{5.10}
\]
The complex powers in these formulas use the real logarithm on positive integration variables and the branch on the right half-plane for \(\lambda\).

For \(r>0\), put \(Q=2\pi r\). Formula (5.10) gives
\[
I_r(s,v)=
-\frac{2\pi e^{-vQ}}{\Gamma(s+2)\Gamma(s)}
\int_0^\infty(b+Q)^{s+1}b^{s-1}e^{-2vb}\,db.
\tag{5.11}
\]
For \(r<0\), put \(Q=2\pi|r|\). It gives
\[
I_r(s,v)=
-\frac{2\pi e^{-vQ}}{\Gamma(s+2)\Gamma(s)}
\int_0^\infty a^{s+1}(a+Q)^{s-1}e^{-2va}\,da.
\tag{5.12}
\]

We justify this Fourier calculation rather than integrating an oscillatory exponential formally. Insert \(e^{-\eta t^2}\), \(\eta>0\), into (5.6) before using (5.10). All three integrals are now absolutely convergent, so Fubini applies. The \(t\)-integral is
\[
\sqrt{\frac{\pi}{\eta}}\,
\exp\!\left(-\frac{(a-b-2\pi r)^2}{4\eta}\right).
\]
This Gaussian identity follows by differentiating its Fourier transform in the frequency and integrating by parts; the value at frequency zero is the Gaussian integral, whose square is evaluated in polar coordinates. As \(\eta\downarrow0\), the displayed kernels have total mass \(2\pi\) and concentrate at \(a-b=2\pi r\). The convolution of the two one-sided densities in (5.10) is continuous and bounded: the \(a\)-density, extended by zero, is bounded and uniformly continuous, and the \(b\)-density is integrable. Consequently the approximate-identity limit evaluates that convolution at \(2\pi r\). On the original side, dominated convergence removes \(e^{-\eta t^2}\) because \(F_{s,v}\) is integrable. Solving \(a=b+Q\) or \(b=a+Q\) proves (5.11) and (5.12).

In (5.11), write the integral as
\[
\frac{Q^{s+1}}s+R(s,Q,v),
\tag{5.13}
\]
where
\[
R=\int_0^1
 \bigl((b+Q)^{s+1}e^{-2vb}-Q^{s+1}\bigr)b^{s-1}\,db
+\int_1^\infty(b+Q)^{s+1}b^{s-1}e^{-2vb}\,db.
\]
The subtraction in the first integral removes its singularity at \(b=0\), so \(R\) is holomorphic for \(|s|<\delta\). Multiplication by \(1/\Gamma(s)\) cancels the pole in (5.13). At zero its surviving value is \(Q\), giving
\[
I_r(0,v)=-4\pi^2r e^{-2\pi rv}\quad(r>0).
\tag{5.14}
\]
The integral in (5.12) is already holomorphic near zero, since its small-\(a\) behaviour is bounded by a constant times \(a^{1-\delta}\). Thus
\[
I_r(0,v)=0\quad(r<0).
\tag{5.15}
\]

Here are uniform bounds for the continuation. Fix \(v_0>0\), let \(v\ge v_0\), and recall \(Q\ge2\pi\). For \(0\le b\le1\), differentiation in \(b\) gives
\[
\left|(b+Q)^{s+1}e^{-2vb}-Q^{s+1}\right|
\le C Q^{1+\delta}(1+v)b
\quad(|s|\le\delta).
\]
Its integral against \(|b^{s-1}|\) is at most
\(C Q^{1+\delta}(1+v)/(1-\delta)\).
For \(b\ge1\), use
\((b+Q)^{1+\delta}\le C Q^{1+\delta}(1+b)^{1+\delta}\) and \(e^{-2vb}\le e^{-2v_0b}\).
The second integral in \(R\) is at most \(C_{v_0}Q^{1+\delta}\).
Likewise the integral in (5.12) is bounded by
\[
Q^{\delta-1}\int_0^\infty
 (a^{1-\delta}+a^{1+\delta})e^{-2v_0a}\,da.
\]
The gamma factors after pole cancellation are bounded on \(|s|\le\delta\). Together these estimates give, for every nonzero \(r\),
\[
|I_r(s,v)|\le C_{v_0}|r|^{1+\delta}(1+v)e^{-2\pi|r|v}.
\tag{5.16}
\]

The row with positive \(m\) is
\(\sum_r I_r(s,my)e^{2\pi irmx}\).
On a compact subset of \(\mathfrak H\), \(y\) is bounded above and bounded below by a positive number. The bound (5.16) makes the double sum over \(m\ge1,\ r\ne0\) locally uniformly convergent, even at \(s=0\): a polynomial in \(m,r\) times \(e^{-2\pi y_0mr}\) is summable. Thus the Fourier expression, consisting of the \(m=0\) term, (5.8), and these nonzero coefficients, gives a holomorphic continuation in \(s\). It agrees with (5.2) for \(0<\operatorname{Re}s<\delta\), where the periodizations and the sums were justified.

Now \(2\zeta(2)=\pi^2/3\), the constant-row contribution is \(-\pi/y\), and (5.14) gives
\[
2\sum_{m,r\ge1}(-4\pi^2r)e^{2\pi irmz}
=-8\pi^2\sum_{n\ge1}\sigma_1(n)q^n.
\]
This proves (5.3). Finally continue the identity (5.5) in \(s\) and evaluate it at zero. This gives (5.4). \(\square\)

**Theorem 5.2 (the transformation law of \(E_2\)).** The real analytic function
\[
E_2^*(z)=E_2(z)-\frac3{\pi y}
\tag{5.17}
\]
satisfies
\[
E_2^*(\gamma z)=(cz+d)^2E_2^*(z)
\quad(\gamma\in\mathrm{SL}_2(\mathbb Z)).
\]
The holomorphic function \(E_2\) satisfies
\[
E_2(\gamma z)=(cz+d)^2E_2(z)+\frac{6c(cz+d)}{\pi i}.
\tag{5.18}
\]
In particular,
\[
E_2(-1/z)=z^2E_2(z)+\frac{12z}{2\pi i},
\qquad E_2(z+1)=E_2(z).
\tag{5.19}
\]

**Proof.** Equation (5.3) says \(H(z,0)=(\pi^2/3)E_2^*(z)\), so Lemma 5.1 proves the first statement. Put \(j=cz+d\). Since
\(\operatorname{Im}(\gamma z)=y/|j|^2\), the first statement rearranges to
\[
E_2(\gamma z)=j^2E_2(z)+\frac3{\pi y}(|j|^2-j^2).
\]
But \(\overline j-j=c(\overline z-z)=-2icy\), whence
\(|j|^2-j^2=-2icyj\). The correction is \(-6icj/\pi=6cj/(\pi i)\), proving (5.18). Substitute \(S\) and \(T\) to obtain (5.19). The nonzero correction for \(S\) proves that \(E_2\notin M_2(\mathrm{SL}_2(\mathbb Z))\). \(\square\)

There are two distinct constructions at weight two. The row-by-row sum
\[
G_2^{\mathrm{row}}(z)=
\sum_{n\ne0}n^{-2}
+\sum_{m\ne0}\left(\sum_{n\in\mathbb Z}(mz+n)^{-2}\right)
\]
converges in the displayed order. By the \(k=2\) Lipschitz formula it equals
\((\pi^2/3)E_2(z)\). The invariantly regularized value is
\(H(z,0)=G_2^{\mathrm{row}}(z)-\pi/y\).
The absolute lattice sum diverges by Lemma 3.1, so its terms cannot be rearranged as at higher weights. The surviving constant coefficient in (5.8) explains the difference.

## 6. Worked examples

### 6.1. Ten coefficients of \(E_4\) and \(E_6\)

The Bernoulli recurrence, computed explicitly in Solution 4, gives
\(B_4=-1/30\) and \(B_6=1/42\). Thus
\[
E_4=1+240\sum_{n\ge1}\sigma_3(n)q^n,\qquad
E_6=1-504\sum_{n\ge1}\sigma_5(n)q^n.
\]
Here are all divisors used to compute their first ten positive-index coefficients. Each divisor is cubed or raised to the fifth power and the results are added.

| \(n\) | Positive divisors | \(\sigma_3(n)\) | Coefficient in \(E_4\) | \(\sigma_5(n)\) | Coefficient in \(E_6\) |
|---:|:---|---:|---:|---:|---:|
| 1 | 1 | 1 | 240 | 1 | \(-504\) |
| 2 | 1, 2 | 9 | 2160 | 33 | \(-16632\) |
| 3 | 1, 3 | 28 | 6720 | 244 | \(-122976\) |
| 4 | 1, 2, 4 | 73 | 17520 | 1057 | \(-532728\) |
| 5 | 1, 5 | 126 | 30240 | 3126 | \(-1575504\) |
| 6 | 1, 2, 3, 6 | 252 | 60480 | 8052 | \(-4058208\) |
| 7 | 1, 7 | 344 | 82560 | 16808 | \(-8471232\) |
| 8 | 1, 2, 4, 8 | 585 | 140400 | 33825 | \(-17047800\) |
| 9 | 1, 3, 9 | 757 | 181680 | 59293 | \(-29883672\) |
| 10 | 1, 2, 5, 10 | 1134 | 272160 | 103158 | \(-51991632\) |

For instance,
\(\sigma_3(6)=1+8+27+216=252\), while
\(\sigma_5(6)=1+32+243+7776=8052\). Multiplication by \(240\) and \(-504\), respectively, gives the row for \(q^6\).

### 6.2. Rotation of the square and hexagonal lattices

Let \(\rho=(-1+i\sqrt3)/2\). Multiplication by \(i\) preserves the square lattice \(\mathbb Z[i]\), so homogeneity gives
\[
G_k(\mathbb Z[i])=i^{-k}G_k(\mathbb Z[i]).
\]
For \(k=6\), the multiplier is \(-1\), hence \(G_6(\mathbb Z[i])=0\).
It does not force \(G_4\) to vanish. In fact \(q(i)=e^{-2\pi}>0\), and every positive-index coefficient of \(E_4\) is positive. Thus
\(E_4(i)>1\), proving \(G_4(\mathbb Z[i])\ne0\).

Multiplication by \(\lambda=1+\rho=e^{\pi i/3}\) preserves
\(\mathbb Z+\mathbb Z\rho\): it sends \(1\) to \(1+\rho\) and \(\rho\) to \(-1\), using \(\rho^2+\rho+1=0\). Its sixth power is one. For \(k=4\), \(\lambda^{-4}\ne1\), so
\[
G_4(\mathbb Z+\mathbb Z\rho)=0.
\]
For \(k=6\), the multiplier is one.

We can also prove that the remaining value \(G_6\) is nonzero without the valence formula. Put \(r=e^{-\pi\sqrt3}\), so \(q(\rho)=-r\).
We have \(r<1/100\): indeed \(\pi>3,\ \sqrt3>5/3\), and the first seven terms of the exponential series give \(e^5>100\).
Since
\[
\sigma_5(n)=n^5\sum_{d\mid n}d^{-5}\le\zeta(5)n^5,
\qquad
\zeta(5)<1+\frac1{32}+\int_2^\infty t^{-5}dt=\frac{67}{64},
\]
and, for \(n\ge2\),
\[
\frac{(n+1)^5r^{n+1}}{n^5r^n}
\le(3/2)^5r<8r,
\]
the terms from \(n=2\) onwards obey
\[
\left|E_6(\rho)-(1+504r)\right|
\le504\,\frac{67}{64}\frac{32r^2}{1-8r}
<504r\,\frac{67}{184}<504r.
\]
The value is real, because \(q(\rho)\) and the coefficients are real. Therefore \(E_6(\rho)>1\), and \(G_6(\mathbb Z+\mathbb Z\rho)\ne0\).
The symmetry-forced zeros are exactly the two asserted above; the other two values do not vanish.

### 6.3. A weight-two value at the square lattice

At the fixed point \(S(i)=i\), equation (5.19) gives
\[
E_2(i)=-E_2(i)+\frac6\pi,\qquad E_2(i)=\frac3\pi,
\qquad E_2^*(i)=0.
\]
This produces the convergent identity
\[
\sum_{n\ge1}\frac{n}{e^{2\pi n}-1}
=\sum_{n\ge1}\sigma_1(n)e^{-2\pi n}
=\frac1{24}-\frac1{8\pi}.
\]
To verify the first equality, expand \(1/(e^{2\pi n}-1)\) as
\(\sum_{m\ge1}e^{-2\pi mn}\) and group the positive terms by the product \(mn\). The second follows from (5.1) and the computed value of \(E_2(i)\).

## 7. Exercises

1. **Easy.** Prove \(M_k(\Gamma)=0\) for odd \(k\) if \(-I\in\Gamma\). Explain why this argument does not force odd-weight forms for \(\Gamma_1(4)\) to vanish.
2. **Easy.** Derive the Lipschitz formula for every integer \(k\ge2\) from the cotangent partial fractions, including the sign when \(k\) is odd.
3. **Medium.** Prove local uniform absolute convergence of (3.1) for \(s>2\), and divergence for \(s=2\). Explain which part of the proof prevents an unrestricted rearrangement at weight two.
4. **Medium.** Compute \(B_k\) and \(E_k\) for \(k=4,6,8,10,14\), using the defining recurrence rather than a table of Bernoulli numbers.
5. **Hard.** Starting from the convergent family \(H(z,s)\), prove that \(E_2^*\) transforms with weight two. Deduce the transformation law of \(E_2\) for a general matrix and for \(S,T\). Identify the contribution that survives when \(s\to0\).

## 8. Full solutions

### Solution 1

For \(\gamma=-I\), the point \(\gamma z\) is \(z\), while \(j(\gamma,z)=-1\).
Thus invariance reads \(f(z)=(-1)^{-k}f(z)\). If \(k\) is odd, this is \(f(z)=-f(z)\), hence \(f=0\) over \(\mathbb C\).
The matrix \(-I\) is absent from \(\Gamma_1(4)\), since its diagonal entries are \(3\), rather than \(1\), modulo \(4\).
There is therefore no such global vanishing argument. At its irregular cusp, Proposition 1.2 instead imposes an odd Taylor series in \(e^{\pi iz}\); this local condition allows nonzero series.

### Solution 2

The normally convergent expression
\[
\frac1z+\sum_{n\ge1}\left(\frac1{z-n}+\frac1{z+n}\right)
\]
equals \(\pi\cot(\pi z)\) by Lemma 3.2. After \(k-1\) derivatives, its value is
\((-1)^{k-1}(k-1)!\sum_{n\in\mathbb Z}(z+n)^{-k}\).
For \(y>0\), the geometric-series expression for the same cotangent is
\(-\pi i-2\pi i\sum_{r\ge1}e^{2\pi irz}\).
Its \(k-1\) derivatives equal
\(-(2\pi i)^k\sum_{r\ge1}r^{k-1}e^{2\pi irz}\).
Both differentiations are justified on compact subsets, by normal convergence. Division by \((-1)^{k-1}(k-1)!\) gives the coefficient
\((-1)^k(2\pi i)^k/(k-1)!=(-2\pi i)^k/(k-1)!\).
This proves the formula for even and odd \(k\).

### Solution 3

On compact \(K\subset\mathfrak H\), the least expansion factor of the invertible real linear map
\((m,n)\mapsto mz+n\), measured with the maximum norm on \(\mathbb R^2\), has a positive lower bound \(a_K\).
For the shell \(\max(|m|,|n|)=r\), there are \(8r\) terms, each at most
\(a_K^{-s}r^{-s}\). The sum is bounded by
\(8a_K^{-s}\sum_{r\ge1}r^{1-s}\), proving uniform convergence when \(s>2\).
At fixed \(z\), each shell instead contributes at least
\(8(|z|+1)^{-2}/r\) to the absolute sum at \(s=2\), by the upper bound on \(|mz+n|\).
Summing these lower bounds proves divergence.
Consequently the weight-two complex terms are not absolutely summable. A convergent row-by-row prescription does not authorize arbitrary permutations of all lattice terms.

### Solution 4

First \(B_0=1\). Recurrence (4.2) gives \(B_1=-1/2\), then
\(B_2=-(1+3B_1)/3=1/6\). All subsequent odd entries vanish by the parity proved in Proposition 4.1.
For even \(n\), denote the sum in the numerator of (4.2) by \(A_n\).
Successive substitution of the already computed entries gives
\[
\begin{aligned}
A_4&=1-\frac52+\frac{10}{6}=\frac16,\\
A_6&=1-\frac72+\frac{21}{6}-\frac{35}{30}=-\frac16,\\
A_8&=1-\frac92+\frac{36}{6}-\frac{126}{30}+\frac{84}{42}=\frac3{10},\\
A_{10}&=1-\frac{11}{2}+\frac{55}{6}-\frac{330}{30}
 +\frac{462}{42}-\frac{165}{30}=-\frac56,\\
A_{12}&=1-\frac{13}{2}+\frac{78}{6}-\frac{715}{30}
 +\frac{1716}{42}-\frac{1287}{30}+\frac{286\cdot5}{66}
 =\frac{691}{210},\\
A_{14}&=1-\frac{15}{2}+\frac{105}{6}-\frac{1365}{30}
 +\frac{5005}{42}-\frac{6435}{30}+\frac{3003\cdot5}{66}
 -\frac{455\cdot691}{2730}=-\frac{35}{2}.
\end{aligned}
\]
For example, the coefficient \(455\) in the last line is \(\binom{15}{12}\).
Dividing each \(A_n\) by \(-(n+1)\) gives

| \(n\) | \(B_n\) | \(-2n/B_n\) |
|---:|:---:|:---:|
| 4 | \(-1/30\) | \(240\) |
| 6 | \(1/42\) | \(-504\) |
| 8 | \(-1/30\) | \(480\) |
| 10 | \(5/66\) | \(-264\) |
| 12 | \(-691/2730\) | \(65520/691\) |
| 14 | \(7/6\) | \(-24\) |

The intermediate weight twelve is necessary for computing \(B_{14}\).
Substitution into Theorem 4.2 now gives all five requested series:
\[
\begin{aligned}
E_4&=1+240\sum_{n\ge1}\sigma_3(n)q^n,\\
E_6&=1-504\sum_{n\ge1}\sigma_5(n)q^n,\\
E_8&=1+480\sum_{n\ge1}\sigma_7(n)q^n,\\
E_{10}&=1-264\sum_{n\ge1}\sigma_9(n)q^n,\\
E_{14}&=1-24\sum_{n\ge1}\sigma_{13}(n)q^n.
\end{aligned}
\]
In the last line the divisor exponent is thirteen; the equality of its prefactor with that of \(E_2\) does not make the two series equal.

### Solution 5

For \(\operatorname{Re}s>0\), all terms of \(H(z,s)\) are absolutely summable. Reindexing the integer pairs under \(\gamma\) multiplies its complex-power factor by \(j(\gamma,z)^2\), while the absolute-power factor is cancelled by
\(\operatorname{Im}(\gamma z)^s=y^s|j(\gamma,z)|^{-2s}\).
Thus \(H(\gamma z,s)=j(\gamma,z)^2H(z,s)\).

Lemma 5.1 proves the continuation, including the termwise limits of its nonconstant Fourier coefficients. Its constant-row term is
\[
-\frac{2sJ(s)}{s+1}\zeta(1+2s)y^{-1-s}.
\]
Since \(J(0)=\pi\) and \(2s\zeta(1+2s)\to1\), this term tends to \(-\pi/y\); it cannot be discarded merely because of the visible factor \(s\).
The remaining terms give
\(H(z,0)=(\pi^2/3)E_2(z)-\pi/y=(\pi^2/3)E_2^*(z)\).
Continuation of the covariance identity proves weight-two covariance for \(E_2^*\).

Writing \(j=cz+d\), solve that identity for \(E_2(\gamma z)\):
\[
E_2(\gamma z)=j^2E_2(z)+\frac3{\pi y}j(\overline j-j)
=j^2E_2(z)-\frac{6icj}{\pi}
=j^2E_2(z)+\frac{6cj}{\pi i}.
\]
For \(S\), this is \(E_2(-1/z)=z^2E_2(z)+12z/(2\pi i)\).
For \(T\), \(c=0,d=1\), so \(E_2(z+1)=E_2(z)\).
This proves every transformation asserted, with the correction traced to the pole cancellation.

## What this lesson does not prove

The modular-form arguments are written out, including the cotangent partial fractions, the Bernoulli recurrence and the analytic continuation needed for weight two. Lemma 0.1 supplies the elementary series and puncture consequences of Cauchy's formula. Their derivation is conditional on the analytic foundations named next, so this is not a claim that every theorem dependency has been closed.

The needed Cauchy, identity, rectangle residue, maximum and power-series facts have an earlier local proof in lesson 01, Lemma 0.2; its local inverse consequence supplies branching coordinates. General parameter-dependent dominated integration remains a foundational prerequisite without a verified earlier programme proof locator here. Taylor and Laurent expansions, removable punctures and locally uniform holomorphy are derived from Cauchy's formula in Lemma 0.1. Elementary real integration, linear algebra and compactness also remain foundations. The missing exact proof locators are recorded as residual gaps; free source availability alone does not close them.

The transformation of the imaginary part is proved in The upper half-plane and the modular group, Proposition 1.1. Cusp widths and the irregular cusp of \(\Gamma_1(4)\) are established in Congruence subgroups, cusps and elliptic points, Section 2 and Proposition 4.1. We use those results as prerequisites. No assertion that \(E_2\) is modular, no valence formula, and no product formula for the discriminant is imported into the proofs here.

## References

- **Voight open book.** J. Voight, *Quaternion Algebras*, freely distributed stable post-publication version 1.0.5 (10 January 2024), §§40.1–40.3, especially Lemmas 40.1.3, 40.1.7 and 40.2.16. [Author's stable free PDF](https://jvoight.github.io/quat-book-v1.0.5.pdf).
- **Stein author PDF.** W. Stein, *Modular Forms: A Computational Approach*, freely distributed PDF on the author's website, §2.1 and Chapter 5. [Free author PDF](https://wstein.org/books/modform/stein-modform.pdf).
- **Teleman 2003.** C. Teleman, *Riemann Surfaces*, Lectures 8–9, for lattice and elliptic-function background. [Author's notes](https://math.berkeley.edu/~teleman/math/Riemann.pdf).
