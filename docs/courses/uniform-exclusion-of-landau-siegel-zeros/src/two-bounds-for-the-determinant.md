# Two bounds for the determinant

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The determinant \(\Delta\) of [A weighted determinant in a biquadratic field](a-weighted-determinant-in-a-biquadratic-field.md) is a nonzero element of \(\mathcal R=\mathbf Z[a,b]\), so its norm is a nonzero integer. This lesson bounds that integer from above by Hadamard's inequality and from below by its divisibility at the primes \(p>H\) with \(\chi(p)=-1\), and compares the two bounds to prove Theorem A. The argument follows OpenAI [OpenAI-LS, Sections 5 and 6].

The notation is that of the previous lesson: \(\chi\), \(q\), \(d\ne2\), \(K=\mathbf Q(a,b)\), \(\sigma\), \(\tau\), \(\operatorname{Nm}\), integers \(1\le H\le N\), \(U=N^{4/3}\), \(M=N^4\), the retained set \(\mathcal P\), the determinant \(\Delta\), and the sums \(S_1\), \(S_2\). As in [Real zeros and the prime bias](real-zeros-and-the-prime-bias.md), \(\ell=\log q\).

## 1. The Archimedean bound

**Lemma 4.1.** For every \(n\in E_N\) and every \(g\in\{1,\sigma,\tau,\sigma\tau\}\),
\[
\begin{aligned}
|g(\theta_n)|&\le(N-1)(1+\sqrt{|d|})(1+\sqrt2)\\
&<8N\sqrt q .
\end{aligned}
\]

*Proof.* \(g(\theta_n)=n_1\pm n_2a\pm n_3b\pm n_4ab\) with \(0\le n_i\le N-1\), \(|a|=\sqrt{|d|}\) and \(|b|=\sqrt2\). The triangle inequality gives the first bound, as
\[
\begin{aligned}
&1+\sqrt{|d|}+\sqrt2+\sqrt{2|d|}\\
&\quad=(1+\sqrt{|d|})(1+\sqrt2).
\end{aligned}
\]
Since \(1\le|d|\le q\), \(1+\sqrt{|d|}\le2\sqrt q\), and \(2(1+\sqrt2)<8\). \(\square\)

**Proposition 4.2.**
\[
\begin{aligned}
&\frac14\log|\operatorname{Nm}(\Delta)|\\
&\quad\le\frac M2\log M+(S_1+S_2)\log N\\
&\qquad+(S_1+S_2)\Bigl(\frac12\ell+\log8\Bigr).
\end{aligned}
\]

*Proof.* Let \(g\in\{1,\sigma,\tau,\sigma\tau\}\). As \(g\) is a ring homomorphism and a determinant is a polynomial in the entries, \(g(\Delta)\) is the determinant of the rows \(g(R_\alpha)\), \(\alpha\in\mathcal P\). The entries of \(g(R_\alpha)\) are
\[
g(\theta_n)^{\alpha_1}\,g\sigma(\theta_n)^{\alpha_2}\,g\sigma\tau(\theta_n)^{\alpha_3},
\]
and \(g\sigma,g\sigma\tau\in\{1,\sigma,\tau,\sigma\tau\}\). By Lemma 4.1 every entry has absolute value at most \((8N\sqrt q)^{\alpha_1+\alpha_2+\alpha_3}\), so the row has Euclidean norm at most \(\sqrt M(8N\sqrt q)^{\alpha_1+\alpha_2+\alpha_3}\). Hadamard's inequality, Lemma 1.3 of [The real-place integral formula and two bounds](course:irrationality-of-special-values/the-real-place-integral-formula-and-two-bounds#1-three-determinant-identities), applied to the transposed matrix, gives
\[
|g(\Delta)|\le M^{M/2}(8N\sqrt q)^{S_1+S_2}.
\]
Multiply over the four values of \(g\), take logarithms and divide by \(4\). \(\square\)

## 2. The Frobenius congruence

**Lemma 4.3.** Let \(p\) be an odd prime with \(p\nmid q\), and let \(g_p\) be the automorphism of \(K\) with
\[
g_p(a)=\Bigl(\frac dp\Bigr)a,\qquad g_p(b)=\Bigl(\frac2p\Bigr)b .
\]
Then \(\theta^p\equiv g_p(\theta)\pmod{p\mathcal R}\) for every \(\theta\in\mathcal R\). If \(\chi(p)=-1\), then \(g_p=\sigma\) when \((2/p)=1\), and \(g_p=\sigma\tau\) when \((2/p)=-1\).

*Proof.* Since \(p\nmid2d\), Euler's criterion [Dirichlet characters, Section 4](course:NT-DIRL/NT-DIRL-01#4-real-characters-and-quadratic-discriminants) gives \(d^{(p-1)/2}\equiv(d/p)\) and \(2^{(p-1)/2}\equiv(2/p)\) modulo \(p\). Hence, in \(\mathcal R\),
\[
\begin{aligned}
a^p&=a\,d^{(p-1)/2}\equiv\Bigl(\frac dp\Bigr)a,\\
b^p&=b\,2^{(p-1)/2}\equiv\Bigl(\frac2p\Bigr)b
\end{aligned}
\]
modulo \(p\mathcal R\). The ring \(\mathcal R/p\mathcal R\) is commutative of characteristic \(p\), so \(x\mapsto x^p\) is a ring homomorphism of it: the binomial coefficients \(\binom pk\), \(0<k<p\), are divisible by \(p\). It fixes the classes of integers, by Fermat's little theorem. For \(\theta=z_1+z_2a+z_3b+z_4ab\) it follows that
\[
\theta^p\equiv z_1+z_2a^p+z_3b^p+z_4a^pb^p\equiv g_p(\theta).
\]
If \(\chi(p)=-1\), then \((d/p)=\chi(p)=-1\) by Section 1 of the previous lesson. \(\square\)

Call a prime \(p\) *admissible* if \(p>H\), \(p\nmid2q\) and \(\chi(p)=-1\).

## 3. Divisibility

**Proposition 4.4** (OpenAI). For every admissible prime \(p\),
\[
\Delta\in p^{E_p}\mathcal R,\qquad E_p=\sum_{\alpha\in\mathcal P}\Bigl\lfloor\frac{\alpha_1}p\Bigr\rfloor .
\]

*Proof.* Let \(j=2\) if \(g_p=\sigma\) and \(j=3\) if \(g_p=\sigma\tau\), and let \(e_1,e_2,e_3\) be the unit vectors of \(\mathbf Z^3\). For \(\alpha\in\mathcal P\) write \(\alpha_1=kp+r\) with \(0\le r<p\), and let \(\widetilde R_\alpha\) be the vector whose entry at \(n\in E_N\) is
\[
\theta_n^r\bigl(\theta_n^p-g_p(\theta_n)\bigr)^k\,\sigma(\theta_n)^{\alpha_2}\,\sigma\tau(\theta_n)^{\alpha_3}.
\]
Expanding the power by the binomial theorem, and using that \(g_p(\theta_n)\) is the conjugate raised to the exponent \(\alpha_j\), gives
\[
\begin{aligned}
\widetilde R_\alpha={}&R_\alpha\\
&+\sum_{m=1}^k(-1)^m\binom kmR_{\alpha-pme_1+me_j}.
\end{aligned}
\]
The index \(\alpha-pme_1+me_j\) has weight \(w(\alpha)-m(p-H)<w(\alpha)\), because \(p>H\). So it precedes \(\alpha\), and by part 1 of Lemma 3.4 its row is a \(K\)-linear combination of retained rows preceding \(\alpha\). Thus the matrix with rows \(\widetilde R_\alpha\), \(\alpha\in\mathcal P\) in increasing order, is \(L\) times the matrix with rows \(R_\alpha\), for a lower triangular matrix \(L\) over \(K\) with diagonal entries \(1\), and
\[
\det\bigl(\widetilde R_\alpha\bigr)_{\alpha\in\mathcal P}=\Delta .
\]
On the other hand \(\theta_n^p-g_p(\theta_n)\in p\mathcal R\) by Lemma 4.3, so every entry of \(\widetilde R_\alpha\) lies in \(p^k\mathcal R\), with \(k=\lfloor\alpha_1/p\rfloor\). Dividing each row by its power of \(p\) leaves a matrix over \(\mathcal R\), whose determinant lies in \(\mathcal R\). Hence \(\Delta\in p^{E_p}\mathcal R\). \(\square\)

The entries of \(L\) need not lie in \(\mathcal R\); the divisibility comes from the entries of the rows \(\widetilde R_\alpha\) alone.

**Corollary 4.5.** Let \(\mathcal A_U\) be the set of admissible primes \(p\le U\). Then
\[
\begin{aligned}
&\frac14\log|\operatorname{Nm}(\Delta)|\ge\sum_{p\in\mathcal A_U}E_p\log p\\
&\quad\ge S_1\sum_{p\in\mathcal A_U}\frac{\log p}p-1.39\,MU .
\end{aligned}
\]

*Proof.* Write \(\Delta=p^{E_p}\rho_p\) with \(\rho_p\in\mathcal R\). Then \(\operatorname{Nm}(\Delta)=p^{4E_p}\operatorname{Nm}(\rho_p)\) with \(\operatorname{Nm}(\rho_p)\in\mathbf Z\), by Lemma 3.2. So \(p^{4E_p}\) divides the nonzero integer \(\operatorname{Nm}(\Delta)\) for every admissible \(p\), and so does the product of these coprime prime powers over \(p\le U\). This gives the first inequality. For the second, \(\lfloor x\rfloor\ge x-1\) gives \(E_p\ge S_1/p-M\), and Chebyshev's bound \(\sum_{p\le U}\log p<(2\log2)U\), Theorem 2.1 of [Counting primes by elementary means: Chebyshev and Mertens](course:NT-ZETA/NT-ZETA-02#2-a-binomial-coefficient-measures-primes), gives the rest, as \(2\log2<1.39\). \(\square\)

## 4. Proof of Theorem A

Suppose Theorem A is false. By Corollary 1.6 of [Real zeros and the prime bias](real-zeros-and-the-prime-bias.md) there are primitive nonprincipal real characters of conductors \(q\to\infty\) with real zeros \(\beta\) such that \(\delta=(1-\beta)\ell\to0\). Fix
\[
\begin{aligned}
H&=\frac{12C_0}{c_0}=12\cdot192\cdot4\cdot97^2\\
&=86{,}713{,}344,
\end{aligned}
\]
with \(c_0,C_0\) from Lemma 3.5, and for each character of the sequence put \(N=\lceil q^{55}\rceil\). For all large \(q\) in the sequence, \(q\ne8\), \(N\ge H\), \(H^{2/3}N^{4/3}\ge2\cdot97^2\) and \(U\ge3\). Then all results of the last three lessons apply, and Lemma 3.5 gives
\[
\rho:=\frac{S_2}{S_1}\le\frac1{12} .
\]

The primes of \(\mathcal A_U\) are those counted in Corollary 1.4 with \(X=U\). Corollaries 1.4 and 4.5 give
\[
\begin{aligned}
&\frac14\log|\operatorname{Nm}(\Delta)|\\
&\quad\ge S_1\log U-4S_1\ell-\frac{3S_1\delta(\log U)^2}{\ell}\\
&\qquad-S_1(\log H+2c_M)-1.39\,MU .
\end{aligned}
\]
Proposition 4.2, with \(\log N=\frac34\log U\) and \(\log M=3\log U\), gives
\[
\begin{aligned}
&\frac14\log|\operatorname{Nm}(\Delta)|\le\frac32M\log U\\
&\quad+S_1(1+\rho)\Bigl(\frac34\log U+\frac12\ell+\log8\Bigr).
\end{aligned}
\]
Combine the two bounds and divide by \(S_1\log U>0\):
\[
\begin{aligned}
1\le{}&\frac34(1+\rho)+\Bigl(4+\frac{1+\rho}2\Bigr)\frac\ell{\log U}\\
&+\frac{3\delta\log U}{\ell}\\
&+\frac{(1+\rho)\log8+\log H+2c_M}{\log U}\\
&+\frac{1.39\,MU}{S_1\log U}+\frac{3M}{2S_1} .
\end{aligned}
\]
The terms on the right are bounded as follows.

1. \(\frac34(1+\rho)\le\frac34\cdot\frac{13}{12}=\frac{13}{16}\).
2. Since \(N\ge q^{55}\), \(\log U=\frac43\log N\ge\frac{220}3\ell\), so the second term is at most \(\frac{109}{24}\cdot\frac3{220}=\frac{109}{1760}<\frac1{16}\).
3. Since \(N\le2q^{55}\) and \(\ell>1\), \(\log U\le\frac43(55\ell+\log2)\le75\ell\), so the third term is at most \(225\delta\), which tends to \(0\).
4. The fourth term tends to \(0\), because \(H\) is fixed and \(\log U\to\infty\).
5. By Lemma 3.5, \(S_1\ge c_0MH^{2/3}U\), so the last two terms are at most \(\frac{1.39}{c_0H^{2/3}\log U}\) and \(\frac3{2c_0H^{2/3}U}\), which tend to \(0\).

Letting \(q\to\infty\) along the sequence gives
\[
1\le\frac{13}{16}+\frac{109}{1760}<\frac{13}{16}+\frac1{16}=\frac78,
\]
a contradiction. This proves Theorem A. \(\square\)

Banks [Banks] arranges the proof so that it gives an explicit constant: \(c=3.0\cdot10^{-3}\) for \(q\ge10^{10}\).

## 5. A zero-free region without exception

**Corollary B.** There is an absolute constant \(c_B>0\) such that, for every modulus \(q\ge1\), no Dirichlet \(L\)-function \(L(s,\chi)\) with \(\chi\) modulo \(q\) vanishes in the region
\[
\operatorname{Re}s\ge1-\frac{c_B}{\log(q(|\operatorname{Im}s|+2))} .
\]

*Proof.* Let \(c\) be the constant of Theorem 5.1 of [Zero-free regions and the exceptional zero](course:NT-DIRL/NT-DIRL-07#5-the-classical-product-region), let \(c_A\) be the constant of Theorem A, and put \(c_B=\min(c,c_A)\). By that theorem, the only possible zero of \(\prod_{\chi\bmod q}L(s,\chi)\) in the region with constant \(c\) is a simple real zero \(\beta_1<1\) of one real nonprincipal character \(\chi_1\) modulo \(q\); the proof there takes \(c<\log2\), so the region lies in \(\operatorname{Re}s>0\) and \(\beta_1>0\). The character \(\chi_1\) is induced by a primitive real nonprincipal character \(\chi^*\) of conductor \(q^*\mid q\), \(q^*\ge3\). By (3.3) of [The functional equation of Dirichlet L-functions](course:NT-DIRL/NT-DIRL-05#3-where-the-zeros-can-be), \(L(s,\chi_1)\) is \(L(s,\chi^*)\) times finite Euler factors whose zeros lie on \(\operatorname{Re}s=0\). So \(L(\beta_1,\chi^*)=0\), and Theorem A gives
\[
1-\beta_1\ge\frac{c_A}{\log q^*}\ge\frac{c_A}{\log q}>\frac{c_B}{\log(2q)} .
\]
Thus \(\beta_1\) lies outside the region with constant \(c_B\), which is contained in the region with constant \(c\). \(\square\)

## 6. Why a real zero is needed

The two bounds hold for every \(d\ne1,2\) and all \(1\le H\le N\); only the distribution of the primes forced by a real zero close to \(1\) makes them incompatible. Fix \(d\ne1,2\) and \(H\), and let \(N\to\infty\), so that \(\ell/\log U\to0\).

For odd \(p\nmid q\), the pair \(\bigl((d/p),(2/p)\bigr)=\bigl(\chi(p),\chi_8(p)\bigr)\), with \(\chi_8\) as in (4.3) of [Dirichlet characters](course:NT-DIRL/NT-DIRL-01#4-real-characters-and-quadratic-discriminants), depends only on \(p\) modulo \(8q\). The map \(u\mapsto(\chi(u),\chi_8(u))\) is a homomorphism from the units modulo \(8q\) onto \(\{\pm1\}^2\): its image is not contained in a subgroup of order \(2\), because \(\chi\) and \(\chi_8\) are nonprincipal and different, having the conductors \(q\ne8\) and \(8\). So each sign pair occurs for a quarter of the residue classes. By Theorem 4.2 of [Dirichlet's theorem on primes in arithmetic progressions](course:NT-DIRL/NT-DIRL-02#4-from-nonvanishing-to-primes), the primes up to \(U\) of each sign pair carry the mass \(\frac14\log U+O_{q}(1)\). Proposition 4.4 applies to the two pairs with \((d/p)=-1\), and by Exercise 4.2 its conclusion also holds when \((d/p)=(2/p)=1\). If the argument of Corollary 4.5 uses the primes of all three pairs, its lower bound has leading term \(\frac34S_1\log U\), while the upper bound of Proposition 4.2 has leading term \(\frac34(S_1+S_2)\log U\). They differ by \(\frac34S_2\log U\ge0\): no contradiction, as must be the case.

At the primes with \((d/p)=1\) and \((2/p)=-1\), \(\theta^p\equiv\tau(\theta)\), and \(\tau(\theta_n)\) is not one of the three conjugates in the rows. The divisibility can then fail. For \(d=-1\), \(N=2\), \(H=3\) and the tie-breaking rule of Section 3 of the previous lesson, a computation with exact arithmetic in \(K\) gives \(E_5=3\), while \(5\) does not divide \(\operatorname{Nm}(\Delta)\). The condition \(p>H\) cannot be dropped either: for \(d=5\), \(N=2\), \(H=3\) and \(p=3\), where \((5/3)=-1\), the same computation gives \(E_3=9\), while \(3^{20}\) is the exact power of \(3\) dividing \(\operatorname{Nm}(\Delta)\), less than \(3^{36}\).

## 7. Exercises

**4.1** (easy). Let \(d=5\) and \(p=3\). Compute \((1+a)^3\) in \(\mathcal R\) and check that \((1+a)^3\equiv1-a\pmod{3\mathcal R}\), as Lemma 4.3 predicts.

**4.2** (medium). Let \(p\) be an odd prime with \(p\nmid q\) and \((d/p)=(2/p)=1\). Show that \(\Delta\in p^{E_p}\mathcal R\) for every \(H\ge1\), without the condition \(p>H\).

**4.3** (medium). Replace \(K\) by \(\mathbf Q(\sqrt d)\): take \(n\in\{0,\dots,N-1\}^2\), \(\theta_n=n_1+n_2a\), and rows \(\bigl(\theta_n^{\alpha_1}\sigma(\theta_n)^{\alpha_2}\bigr)_n\). With \(M=N^2\) rows chosen in the same way, the natural scale is \(U=N\). Explain why the comparison of the two bounds then gives no contradiction, and what the adjunction of \(\sqrt2\) changes.

**4.4** (easy). Check that \(12\cdot192\cdot4\cdot97^2=86{,}713{,}344\), that \(\frac{109}{24}\cdot\frac3{220}=\frac{109}{1760}<\frac1{16}\), and that \(\frac43(55+\log2)\le75\).

## 8. Solutions

**4.1.** In \(\mathcal R\),
\[
\begin{aligned}
(1+a)^3&=1+3a+3a^2+a^3\\
&=1+3a+15+5a=16+8a\\
&\equiv1+2a\equiv1-a\pmod3 .
\end{aligned}
\]
Here \((5/3)=-1\) and \((2/3)=-1\), so \(g_3=\sigma\tau\), and \(\sigma\tau(1+a)=1-a\).

**4.2.** Here \(g_p\) is the identity, so \(\theta^p\equiv\theta\pmod{p\mathcal R}\). Replace the first factor \(\theta_n^{\alpha_1}\) by \(\theta_n^r(\theta_n^p-\theta_n)^k\). The expansion gives \(R_\alpha+\sum_{m\ge1}(-1)^m\binom kmR_{\alpha-(p-1)me_1}\), and these indices have weight \(w(\alpha)-(p-1)m<w(\alpha)\) for every \(H\). The rest of the proof of Proposition 4.4 is unchanged.

**4.3.** The upper bound has main term \((S_1+S_2)\log N\) and the lower bound \(S_1\log U\), and \(\log N=\log U\): the two main terms agree up to \(S_2\log U\ge0\), even if all primes up to \(U\) were admissible. With \(\sqrt2\) adjoined, there are four coordinates \(n_1,\dots,n_4\) but only three conjugates in the rows. Then \(M=N^4=U^3\), so \(\log N=\frac34\log U\), and this gap of \(\frac14\log U\) per unit of degree is what Theorem A uses.

**4.4.** \(12\cdot192=2304\), \(4\cdot97^2=37636\), and \(2304\cdot37636=86{,}713{,}344\). Next \(\frac{109\cdot3}{24\cdot220}=\frac{327}{5280}=\frac{109}{1760}\), and \(109\cdot16=1744<1760\). Finally \(\frac43(55+0.7)=74.27\le75\).

## References

- [OpenAI-LS] OpenAI, *Uniform exclusion of Landau–Siegel zeros*, OpenAI Math Release preprint, 1 October 2026, Sections 5 and 6. https://github.com/openai/math/tree/main/preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026
- [Banks] W. D. Banks, *On the OpenAI proof that Landau–Siegel zeros do not exist*, arXiv:2610.15483, October 2026. https://arxiv.org/abs/2610.15483
