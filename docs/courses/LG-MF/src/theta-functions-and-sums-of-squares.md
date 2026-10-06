# Theta functions and sums of squares

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A theta series records lattice points in its coefficients. A transformation law puts a power of that series into a small space of modular forms. Once a basis of that space is known, a few coefficients determine every coefficient. We will carry out this argument for four squares, then for eight and two squares.

We use the valence formula proved in Dimension formulas for congruence subgroups, Theorem 3.1, to prove directly the three small dimensions needed here. We prove the real Poisson and Gaussian identities, then the transformation on the whole half-plane, the generators of the level-four group, and regularity at all its cusps.

## 1. One normalization for each theta function

Throughout, \(z\in\mathfrak H\), \(q=e^{2\pi iz}\), and
\[
\theta(z)=\sum_{n\in\mathbb Z}q^{n^2}
=1+2q+2q^4+2q^9+\cdots.
\tag{1.1}
\]
For the real theta function and Jacobi's theta constant, the dictionary is
\[
\Theta_{\text{real}}(t)=\sum_{n\in\mathbb Z}e^{-\pi tn^2}
=\theta(it/2),\qquad
\vartheta(\tau)=\sum_{n\in\mathbb Z}e^{\pi in^2\tau}
=\theta(\tau/2).
\tag{1.2}
\]
Here \(t>0\), and \(\tau=2z\) when comparing the two holomorphic conventions. The two-variable product used in Solution 5 will have parameter \(z\) itself; it is defined explicitly there.

The Fourier convention and Poisson formula we shall prove are
\[
\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-2\pi ix\xi}\,dx,
\qquad
\sum_{n\in\mathbb Z}f(n)=\sum_{n\in\mathbb Z}\widehat f(n)
\quad(f\in\mathcal S(\mathbb R)).
\tag{1.3}
\]
Both sums are absolutely convergent. The Gaussian transform is
\[
\widehat{e^{-\pi t x^2}}(\xi)
=t^{-1/2}e^{-\pi\xi^2/t}.
\tag{1.4}
\]
The resulting real theta identity is
\[
\Theta_{\text{real}}(1/t)=\sqrt t\,\Theta_{\text{real}}(t).
\tag{1.5}
\]
**Theorem 1.1 (Schwartz Poisson summation and the Gaussian).** Equations (1.3)–(1.5) hold. More generally, with Fourier kernel \(e^{-2\pi ix\cdot\xi}\),
\[
\begin{gathered}
\sum_{m\in\mathbb Z^d}f(m)=\sum_{m\in\mathbb Z^d}\widehat f(m),\\
f\in\mathcal S(\mathbb R^d),\quad d\ge1.
\end{gathered}
\tag{1.3a}
\]
Both sums converge absolutely.

**Proof.** A Schwartz function and each of its derivatives are bounded by \(C_A(1+|x|)^{-A}\) for every \(A\). For \(A>d\), counting the integer points in dyadic shells proves summability of this majorant. Consequently
\(P(x)=\sum_{m\in\mathbb Z^d}f(x+m)\) and all its derivatives converge uniformly on the unit cube. It is a smooth periodic function. Absolute integration and translation of the cubes give its Fourier coefficients
\[
\begin{gathered}
\int_{[0,1]^d}P(x)e^{-2\pi in\cdot x}\,dx\\
=\int_{\mathbb R^d}f(x)e^{-2\pi in\cdot x}\,dx\\
=\widehat f(n).
\end{gathered}
\]
Integration by parts gives
\((1+4\pi^2|\xi|^2)^A\widehat f(\xi)
=\widehat{(1-\sum_j\partial_j^2)^Af}(\xi)\).
The right side is bounded by the integrable absolute value of its input. Thus the coefficients are absolutely summable when \(2A>d\), and their Fourier series converges uniformly to a continuous periodic function \(Q\).

We justify Fourier uniqueness as well. The kernel
\[
K_M(u)=\frac1M\left|\sum_{j=0}^{M-1}e^{2\pi iju}\right|^2
\]
is a nonnegative trigonometric polynomial of integral one. At distance at least \(\delta>0\) from an integer, the geometric-sum formula bounds it by \(1/(M\sin^2(\pi\delta))\). The product of these kernels in the \(d\) coordinates has integral one and mass outside the coordinate \(\delta\)-neighbourhood of zero at most \(d/(M\sin^2(\pi\delta))\). Uniform continuity therefore proves that convolution with the product kernel converges uniformly to any continuous periodic function. If all its Fourier coefficients are zero, every such convolution is zero, so the function is zero. Apply this to \(P-Q\), then evaluate at zero. This proves (1.3a) and (1.3).

For (1.4), put \(g_t(x)=e^{-\pi tx^2}\) and \(G_t(\xi)=\widehat g_t(\xi)\). Differentiation under the integral is justified by the integrable majorant \(2\pi|x|g_t(x)\). Since \(g_t'=-2\pi txg_t\), integration by parts, with zero boundary term, gives
\[
G_t'(\xi)=-\frac{2\pi\xi}{t}G_t(\xi).
\]
Hence \(G_t(\xi)=G_t(0)e^{-\pi\xi^2/t}\). The Gaussian integral is evaluated without an imported transform: if \(I=\int_{\mathbb R}e^{-\pi x^2}dx\), positivity and polar coordinates give
\(I^2=2\pi\int_0^\infty e^{-\pi r^2}r\,dr=1\), so \(I=1\). Scaling gives \(G_t(0)=t^{-1/2}\). This proves (1.4). Apply (1.3) to \(g_t\) and multiply by \(\sqrt t\) to obtain (1.5). \(\square\)

The freely accessible original lecture notes of Sutherland, Theorem 17.8 and Lemma 17.9, provide the one-variable comparison source. The proof above also establishes the higher-dimensional formula and the Fourier uniqueness needed later. The zeta functional equation is not used.

The constant term matters: \(\Theta_{\text{real}}(t)\to1\), while its nonconstant part decays exponentially. For example, since \(n^2\ge1+3(n-1)\) for \(n\ge1\),
\[
0\le\Theta_{\text{real}}(t)-1
\le\frac{2e^{-\pi t}}{1-e^{-3\pi t}}.
\tag{1.6}
\]
In particular it is \(\Theta_{\text{real}}-1\) that is rapidly decreasing as \(t\to\infty\).

For \(m\ge1\), define the number of ordered, signed representations
\[
r_m(n)=\#\{(x_1,\ldots,x_m)\in\mathbb Z^m:
 x_1^2+\cdots+x_m^2=n\}.
\tag{1.7}
\]
Thus \(r_m(0)=1\). Absolute convergence gives
\[
\theta(z)^m=\sum_{n\ge0}r_m(n)q^n.
\tag{1.8}
\]
Indeed multiplying the \(m\) absolutely convergent series sums over all integer tuples; grouping by their squared length gives (1.8). Each individual coefficient counts a finite set.

## 2. The transformation on the half-plane

**Theorem 2.1.** The series \(\theta\) is holomorphic on \(\mathfrak H\) and satisfies
\[
\theta(z+1)=\theta(z),\qquad
\theta\left(-\frac1{4z}\right)=\sqrt{-2iz}\,\theta(z).
\tag{2.1}
\]
The square root is the principal branch on the right half-plane.

**Proof.** On a compact subset with \(\operatorname{Im}z\ge y_0>0\), the absolute values of the summands are bounded by \(e^{-2\pi y_0n^2}\). This sequence is summable. The same argument works after any fixed number of derivatives, because the additional factor is a fixed power of \(n^2\). The series and its derivatives converge locally uniformly, proving holomorphy. Since \(n^2\) is an integer, each summand is unchanged by \(z\mapsto z+1\).

The map \(z\mapsto-1/(4z)\) preserves \(\mathfrak H\), and \(\operatorname{Re}(-2iz)=2\operatorname{Im}z>0\). Both sides of the second identity are therefore holomorphic with the stated branch. At \(z=it/2\), its two sides are
\[
\theta\left(\frac{i}{2t}\right)
=\Theta_{\text{real}}(1/t),\qquad
\sqrt t\,\theta(it/2)=\sqrt t\,\Theta_{\text{real}}(t).
\]
They agree by (1.5). The positive imaginary axis has accumulation points inside the domain, so the identity theorem proves equality throughout \(\mathfrak H\). \(\square\)

We will use the integral-weight slash operator
\[
(f|_k\gamma)(z)=(cz+d)^{-k}f(\gamma z)
\quad
\left(\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}
\in\mathrm{SL}_2(\mathbb Z)\right).
\tag{2.2}
\]
Only the integer powers \(\theta^2,\theta^4,\theta^8\) will be treated as modular forms. Formula (2.1) is enough for this purpose; a general half-integral-weight slash operator is not required.

## 3. Generators of the level-four group

Put
\[
T=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
U=\begin{pmatrix}1&0\\4&1\end{pmatrix}.
\tag{3.1}
\]

**Theorem 3.1.** One has
\[
\Gamma_0(4)=\langle-I,T,U\rangle.
\tag{3.2}
\]

**Proof.** These three matrices belong to \(\Gamma_0(4)\). Conjugate by \(D=\operatorname{diag}(2,1)\). A matrix in that group has the form
\[
D\begin{pmatrix}a&b\\4c&d\end{pmatrix}D^{-1}
=\begin{pmatrix}a&2b\\2c&d\end{pmatrix}
\in\Gamma(2),
\tag{3.3}
\]
and this gives every matrix of \(\Gamma(2)\). The conjugates of \(T,U\) are
\[
A=\begin{pmatrix}1&2\\0&1\end{pmatrix},\qquad
B=\begin{pmatrix}1&0\\2&1\end{pmatrix}.
\]
We prove that \(-I,A,B\) generate \(\Gamma(2)\).

Let its first column be \((a,C)^t\). Then \(a\) is odd, \(C\) is even, and \(\gcd(a,C)=1\). If \(C\ne0\) and \(|a|>|C|\), left multiplication by \(A^n\) replaces \(a\) by \(a+2nC\). Choose \(n\) nearest to \(-a/(2C)\); the new absolute value is at most \(|C|\). It is strictly smaller because an odd number cannot have the same absolute value as an even number.

If \(|C|>|a|\), left multiplication by \(B^n\), with \(n\) nearest to \(-C/(2a)\), makes \(|C+2na|<|a|\), by the same parity argument. The case \(|a|=|C|\) is impossible. Thus whenever \(C\ne0\), a step strictly lowers the positive integer \(\max(|a|,|C|)\). The first entry remains odd and hence nonzero. The process must reach \(C=0\).

The determinant then forces the two diagonal entries to be equal and to be \(1\) or \(-1\). The upper-right entry is even. The reduced matrix is therefore \(\pm A^j\) for an integer \(j\). Undoing the finitely many left multiplications writes the original matrix as a word in \(-I,A,B\). Conjugating back proves (3.2). \(\square\)

For later character calculations define
\[
\chi_{-4}(d)=
\begin{cases}
0,&d\text{ even},\\
1,&d\equiv1\pmod4,\\
-1,&d\equiv3\pmod4.
\end{cases}
\tag{3.4}
\]
The two unit residues modulo four multiply with these signs, so this is a Dirichlet character of modulus four. Every lower-right entry of a matrix in \(\Gamma_0(4)\) is odd. If \(\gamma_1,\gamma_2\) belong to that group, their product has lower-right entry congruent to \(d_1d_2\pmod4\). Consequently \(\gamma\mapsto\chi_{-4}(d)\) is a character of the group.

## 4. Modularity and all three cusps

Write \(G=\theta^2\). Squaring (2.1) removes the square root:
\[
G\left(-\frac1{4z}\right)=-2iz\,G(z).
\tag{4.1}
\]
Set \(Wz=-1/(4z)\), and let \(u=Wz-1=-(4z+1)/(4z)\). Since \(W(u)=z/(4z+1)\), applying (4.1) twice and periodicity once gives
\[
G\left(\frac z{4z+1}\right)
=-2iu\,G(u)=(-2iu)(-2iz)G(z)
=(4z+1)G(z).
\tag{4.2}
\]
Thus \(G|_1T=G\), \(G|_1U=G\), and \(G|_1(-I)=-G\). Their values match (3.4). The right slash composition law and Theorem 3.1 now imply
\[
G|_1\gamma=\chi_{-4}(d)G
\quad(\gamma\in\Gamma_0(4)).
\tag{4.3}
\]
The square and fourth power of this identity give the usual weight-two and weight-four laws for \(\theta^4\) and \(\theta^8\).

It remains to check the cusps. The cusp computation in [Congruence subgroups, cusps and elliptic points, Proposition 4.1], together with [Modular curves and their genus, Section 4], gives the representatives \(\infty,0,1/2\), of projective widths \(1,4,1\). We use
\[
S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
\sigma=\begin{pmatrix}1&0\\2&1\end{pmatrix}
\tag{4.4}
\]
as cusp matrices for \(0,1/2\).

At infinity, (1.1) is a holomorphic \(q\)-series. At zero, substituting \(z/4\) into (4.1) gives
\[
G|_1S=-\frac i2\theta(z/4)^2,\qquad
\theta^4|_2S=-\frac14\theta(z/4)^4.
\tag{4.5}
\]
These are holomorphic series in \(q_0=e^{2\pi iz/4}\), as required by width four. Their constant terms are \(-i/2\) and \(-1/4\).

For the third cusp first separate even and odd integers in (1.1). Since \((-1)^{n^2}=(-1)^n\),
\[
\theta(z+1/2)=2\theta(4z)-\theta(z).
\tag{4.6}
\]
Let \(w=z+1/2\). Then \(\sigma z=1/2-1/(4w)\). Apply (4.6) and (2.1):
\[
\begin{aligned}
\theta(\sigma z)
&=2\theta(-1/w)-\theta(-1/(4w))\\
&=2\sqrt{-iw/2}\,\theta(w/4)
 -\sqrt{-2iw}\,\theta(w)\\
&=\sqrt{-2iw}\,[\theta(w/4)-\theta(w)].
\end{aligned}
\tag{4.7}
\]
The last equality respects the branch: \(-iw\) lies in the right half-plane, and multiplication by a positive real number scales its principal square root by the positive square root of that number.

The difference in brackets is the odd-integer part of \(\theta(w/4)\). Define
\[
C(q)=\sum_{j\ge0}q^{j(j+1)}=1+q^2+q^6+q^{12}+\cdots.
\tag{4.8}
\]
Each odd square is congruent to one modulo eight. Pairing the positive and negative odd integers therefore gives
\[
\theta(w/4)-\theta(w)=2e^{\pi i/4}q^{1/4}C(q).
\tag{4.9}
\]
Here \(q^a\) always means \(e^{2\pi iaz}\) on the half-plane. Since \(-2iw=-i(2z+1)\), equations (4.7)–(4.9) yield
\[
\boxed{
G|_1\sigma=4q^{1/2}C(q)^2,\qquad
\theta^4|_2\sigma=16qC(q)^4,\qquad
\theta^8|_4\sigma=256q^2C(q)^8.
}
\tag{4.10}
\]
All exponents are positive. The half-power in the first series is precisely the character condition, because
\[
\sigma T\sigma^{-1}
=\begin{pmatrix}-1&1\\-4&3\end{pmatrix}
\in\Gamma_0(4),\qquad \chi_{-4}(3)=-1.
\tag{4.11}
\]
Thus \(G|_1\sigma\) is antiperiodic under \(z\mapsto z+1\). Holomorphy here allows the nonnegative exponents \(m+1/2\); it does not require integral powers in this character space.

**Theorem 4.1.** With all cusp conditions included,
\[
\theta^2\in M_1(\Gamma_0(4),\chi_{-4}),\qquad
\theta^4\in M_2(\Gamma_0(4)),\qquad
\theta^8\in M_4(\Gamma_0(4)).
\tag{4.12}
\]

**Proof.** Holomorphy on the half-plane follows from Theorem 2.1. Equations (4.2)–(4.3) prove the group laws, and (4.5), (4.10), and the expansion at infinity prove holomorphy at every cusp. For \(\theta^8\), its expansion at zero is the square of that for \(\theta^4\). \(\square\)

None of these forms is a cusp form, because its constant term at infinity is one. Vanishing at \(1/2\) is only one of the three cusp conditions.

## 5. Jacobi's four-square theorem

Use the constant-one normalization
\[
E_2(z)=1-24\sum_{n\ge1}\sigma_1(n)q^n,
\qquad \sigma_j(n)=\sum_{d\mid n}d^j.
\tag{5.1}
\]
Its weight-two transformation law was proved in [Modular forms, lattice functions and Eisenstein series, Theorem 5.2]. The holomorphic combinations
\[
A(z)=E_2(z)-2E_2(2z),\qquad
B(z)=E_2(z)-4E_2(4z)
\tag{5.2}
\]
belong to \(M_2(\Gamma_0(4))\): use the level-two inclusion for \(A\), and the level-four statement for \(B\). The exact combination theorem is [Hecke operators for \(\Gamma_0(N)\) and \(\Gamma_1(N)\), equation (7.3)], with its normalization factor \(-1/24\) removed.

Here is a direct dimension bound. The level-four group has index six, so the earlier valence formula, Theorem 3.1 of the dimension lesson, gives total weighted order \(2\cdot6/12=1\) for a nonzero holomorphic weight-two form. If its constant and first coefficients were both zero, its order at infinity would be at least two, exceeding that total. Thus those two coefficients give an injective map to \(\mathbb C^2\), and the dimension is at most two. The constant and first coefficients of \(A,B\) are
\[
\begin{array}{c|rr}
 &1&q\\\hline
A&-1&-24\\
B&-3&-24
\end{array}
\tag{5.3}
\]
and their determinant is \(-48\). Hence \(A,B\) form a basis. Since \(\theta^4=1+8q+O(q^2)\), writing \(\theta^4=aA+bB\) gives
\[
-a-3b=1,\qquad -24a-24b=8.
\]
The second equation gives \(a+b=-1/3\); the first gives \(a+3b=-1\). Thus \(b=-1/3\), \(a=0\), and
\[
\theta(z)^4=\frac{4E_2(4z)-E_2(z)}3.
\tag{5.4}
\]

**Theorem 5.1 (Jacobi).** For every positive integer \(n\),
\[
\boxed{r_4(n)=8\sum_{\substack{d\mid n\\ 4\nmid d}}d.}
\tag{5.5}
\]

**Proof.** The coefficient of \(q^n\) in (5.4) is
\[
8\bigl(\sigma_1(n)-4\sigma_1(n/4)\bigr),
\tag{5.6}
\]
where \(\sigma_1(n/4)=0\) unless \(4\mid n\). The divisors of \(n\) divisible by four are exactly \(4e\) with \(e\mid n/4\). Their sum is \(4\sigma_1(n/4)\). Subtracting them gives (5.5), and (1.8) identifies this coefficient with \(r_4(n)\). \(\square\)

The formula also proves that every positive integer is a sum of four squares: the divisor \(1\) contributes, so \(r_4(n)\ge8\). It does not say that every representation has four nonzero coordinates.

## 6. Two complete examples

### 6.1. Counting four squares through ten

For direct counting list the nonnegative absolute values in decreasing order. If a pattern contains \(s\) nonzero entries and the value \(j\) occurs \(m_j\) times, it accounts for
\[
\frac{4!}{\prod_j m_j!}\,2^s
\tag{6.1}
\]
ordered, signed tuples. The permutation factor includes the repeated zeros; zeros have no sign choice.

For \(1\le n\le10\), the square of an entry is \(0,1,4\), or \(9\). If \(n<9\), enumerate the solutions of \(4a+b=n\) with \(a+b\le4\), where \(a\) entries have absolute value two and \(b\) have absolute value one. For \(n=9,10\), either use this same enumeration or include one entry of absolute value three and distribute the remaining \(0\) or \(1\). This proves the list below is exhaustive.

| \(n\) | Absolute-value patterns and their counts | Direct total | \(\sum_{d\mid n,\,4\nmid d}d\) | Formula \(8\sum d\) |
|---:|:---|---:|---:|---:|
| 1 | \((1,0,0,0):\ 4\cdot2=8\) | 8 | \(1\) | 8 |
| 2 | \((1,1,0,0):\ 6\cdot4=24\) | 24 | \(1+2=3\) | 24 |
| 3 | \((1,1,1,0):\ 4\cdot8=32\) | 32 | \(1+3=4\) | 32 |
| 4 | \((2,0,0,0):\ 8;\ (1,1,1,1):\ 16\) | 24 | \(1+2=3\) | 24 |
| 5 | \((2,1,0,0):\ 12\cdot4=48\) | 48 | \(1+5=6\) | 48 |
| 6 | \((2,1,1,0):\ 12\cdot8=96\) | 96 | \(1+2+3+6=12\) | 96 |
| 7 | \((2,1,1,1):\ 4\cdot16=64\) | 64 | \(1+7=8\) | 64 |
| 8 | \((2,2,0,0):\ 6\cdot4=24\) | 24 | \(1+2=3\) | 24 |
| 9 | \((3,0,0,0):\ 8;\ (2,2,1,0):\ 12\cdot8=96\) | 104 | \(1+3+9=13\) | 104 |
| 10 | \((3,1,0,0):\ 48;\ (2,2,1,1):\ 6\cdot16=96\) | 144 | \(1+2+5+10=18\) | 144 |

At \(n=0\), the only tuple is \((0,0,0,0)\), so \(r_4(0)=1\). Formula (5.5) is stated for positive \(n\).

### 6.2. The expansion at one half

Equation (4.6) is obtained by adding the even terms and subtracting the odd terms of \(\theta\); it holds for every \(z\in\mathfrak H\). Its use in (4.7) changes the cusp \(1/2\) to infinity. From \(C(q)=1+q^2+q^6+O(q^{12})\),
\[
C(q)^4=1+4q^2+6q^4+8q^6+O(q^8).
\]
The coefficient of \(q^6\) is \(4\) from choosing one \(q^6\), and \(\binom43=4\) from choosing three \(q^2\)'s. Hence
\[
\theta^4|_2\sigma
=16q+64q^3+96q^5+128q^7+O(q^9).
\tag{6.2}
\]
This is a holomorphic series in the width-one cusp coordinate, with order exactly one. The companion expansions begin
\[
G|_1\sigma=4q^{1/2}+8q^{5/2}+4q^{9/2}+O(q^{13/2}),
\qquad
\theta^8|_4\sigma=256q^2+2048q^4+O(q^6).
\tag{6.3}
\]
The first has the antiperiodicity in (4.11); the second has integral exponents and order two. These different leading orders reflect their different weights and characters.

## 7. The other two counting spaces

### 7.1. Eight squares

The modularity of \(\theta^8\) was proved in Theorem 4.1. The same valence formula gives total order \(4\cdot6/12=2\) for a nonzero form in \(M_4(\Gamma_0(4))\). Its constant, first and second coefficients cannot all vanish, since that would give order at least three at infinity. They give an injective map to \(\mathbb C^3\), so the dimension is at most three. Use
\[
E_4(z)=1+240\sum_{n\ge1}\sigma_3(n)q^n.
\tag{7.1}
\]
The dilations \(E_4(2z),E_4(4z)\) belong to the same level-four space, by the following direct dilation argument. The constant, \(q\), and \(q^2\) coefficients make these three series linearly independent: the \(q\) coefficient detects \(E_4(z)\), the \(q^2\) coefficient then detects \(E_4(2z)\), and the constant detects \(E_4(4z)\). They therefore form a basis.

Their level-four modularity can also be checked directly, including for these noncuspidal forms. Put \(f_d(z)=E_4(dz)\), \(d=2,4\). For \(\gamma=\begin{pmatrix}a&b\\c&e\end{pmatrix}\in\Gamma_0(4)\), the conjugate \(\operatorname{diag}(d,1)\gamma\operatorname{diag}(d,1)^{-1}\) is integral of determinant one, with the same automorphy denominator \(cz+e\). The level-one law proves the weight-four law for \(f_d\).

At an arbitrary cusp matrix \(\alpha=\begin{pmatrix}a&b\\c&e\end{pmatrix}\in\mathrm{SL}_2(\mathbb Z)\), put \(h=\gcd(da,c)>0\). Choose \(\beta\in\mathrm{SL}_2(\mathbb Z)\) with first column \((da/h,c/h)^t\). Then
\[
\operatorname{diag}(d,1)\alpha
=\beta\begin{pmatrix}h&v\\0&d/h\end{pmatrix}
\quad\hbox{for an integer }v.
\tag{7.1a}
\]
The lower diagonal entry follows from the determinant and is positive. The slash denominator identity and invariance of \(E_4\) give
\[
(f_d|_4\alpha)(z)
=\left(\frac hd\right)^4
 E_4\left(\frac{h^2}{d}z+\frac{hv}{d}\right).
\tag{7.1b}
\]
Its affine argument has positive slope, so the Fourier series is bounded as \(\operatorname{Im}z\to\infty\). Periodicity at the cusp then gives a holomorphic expansion, by the cusp criterion in the Eisenstein lesson, Section 1. This proves every cusp condition for both dilations.

Now \(\theta^8=1+16q+112q^2+O(q^3)\). There are eight ways to place a single \(\pm1\), giving \(16\), and \(\binom82\) ways to place two, with four sign choices, giving \(112\). Matching the three coefficients gives
\[
\theta(z)^8
=\frac{E_4(z)-2E_4(2z)+16E_4(4z)}{15}.
\tag{7.2}
\]
Solution 3 completes the conversion of this identity into
\[
\boxed{r_8(n)=16\sum_{d\mid n}(-1)^{n+d}d^3
\quad(n\ge1).}
\tag{7.3}
\]

### 7.2. The weight-one dimension

**Proposition 7.1.** One has
\[
\dim M_1(\Gamma_0(4),\chi_{-4})=1.
\tag{7.4}
\]

**Proof.** Let \(V\) be the subspace of \(M_2(\Gamma_0(4))\) consisting of forms vanishing at the cusp \(P_*=1/2\). Every nonzero element has total weighted order one, by the earlier valence formula just used. If it also had zero constant term at infinity, its orders at these two distinct cusps would be at least one each, a contradiction. Thus its constant term is an injective functional on \(V\), giving \(\dim V\le1\). By (4.10), \(\theta^4\) belongs to \(V\) and has constant term one. Therefore \(V=\mathbb C\theta^4\). This argument does not use Riemann–Roch or an analytic/topological genus comparison.

For any \(g\in M_1(\Gamma_0(4),\chi_{-4})\), its square is in \(M_2(\Gamma_0(4))\). At \(P_*\), (4.11) makes \(g|_1\sigma\) antiperiodic. Its holomorphic expansion has exponents \(m+1/2\), \(m\ge0\), so \(g^2|_2\sigma\) has order at least one. Therefore \(g^2=c\theta^4\) for a constant \(c\).

If \(c=0\), then \(g=0\). Otherwise choose a complex number \(b\) with \(b^2=c\). On the connected half-plane,
\[
(g-b\theta^2)(g+b\theta^2)=0.
\]
If the first factor is not identically zero, it is nonzero on an open set; the second vanishes there and therefore everywhere by the identity theorem. Hence \(g=b\theta^2\) or \(g=-b\theta^2\). This proves the dimension is at most one, and Theorem 4.1 supplies the nonzero form \(\theta^2\). \(\square\)

The irregular-cusp conventions agree with the dimension lesson, Section 7.4: \(\Gamma_0(4)=\{\pm\gamma:\gamma\in\Gamma_1(4)\}\), and weight one on the latter group extends with precisely the character (3.4). The direct valence proof above supplies the required dimension independently of that lesson's general dimension machinery.

To turn (7.4) into a divisor formula, we still need a form with the desired coefficients. Solution 5 constructs, proves modular, and checks all cusps of
\[
E(z)=\frac14+\sum_{n\ge1}
 \left(\sum_{d\mid n}\chi_{-4}(d)\right)q^n.
\tag{7.5}
\]
Comparing its constant term with \(\theta^2\) in the one-dimensional space then gives
\[
\boxed{r_2(n)=4\sum_{d\mid n}\chi_{-4}(d)
\quad(n\ge1).}
\tag{7.6}
\]
The dimension statement alone cannot justify (7.6) without proving that (7.5) belongs to the space.

## 8. Exercises

1. **Easy.** For \(t>0\) and \(a\in\mathbb R\), deduce from Poisson summation that
   \[
   \sum_{n\in\mathbb Z}e^{-\pi t(n+a)^2}
   =t^{-1/2}\sum_{n\in\mathbb Z}e^{-\pi n^2/t}e^{2\pi ina}.
   \]
   Justify the translation factor and convergence.
2. **Medium.** Prove the generator theorem (3.2) by a terminating reduction. As a worked reduction, express \(\begin{pmatrix}3&1\\8&3\end{pmatrix}\) in the generators.
3. **Medium.** Derive (7.3) from the modularity of \(\theta^8\) and the three-dimensional Eisenstein basis. Include both odd and even \(n\).
4. **Medium.** Prove (4.6) and use the inversion formula, with the branch checked, to prove holomorphy of \(\theta^4\) at \(1/2\). Compute the first four nonzero coefficients there.
5. **Hard.** Deduce (7.6) from the weight-one modularity of \(\theta^2\) and dimension (7.4). Supply a modularity and cusp proof for the coefficient series (7.5), rather than assume it from its Fourier expansion. You may use the product construction in the solution.

## 9. Full solutions

### Solution 1

Let \(f_t(x)=e^{-\pi tx^2}\) and \(g(x)=f_t(x+a)\). Translation preserves the Schwartz class. With \(u=x+a\),
\[
\widehat g(\xi)
=\int_{\mathbb R}f_t(u)e^{-2\pi i(u-a)\xi}\,du
=e^{2\pi ia\xi}t^{-1/2}e^{-\pi\xi^2/t}.
\tag{9.1}
\]
Apply (1.3) to \(g\), and evaluate (9.1) at integer \(\xi=n\). This gives the requested formula, with the positive translation phase. Both sides converge absolutely: the original is a shifted Gaussian sum, and the phase on the other side has absolute value one. No conditional rearrangement occurs.

### Solution 2

Conjugation by \(D\) in (3.3) takes the problem to \(\Gamma(2)\), with upper and lower even shears \(A,B\). The determinant makes the first column primitive, with its first entry odd and its second even. If the lower entry is nonzero, reduce the larger absolute entry by the nearest multiple of twice the smaller one. The new entry has absolute value at most that of the smaller; opposite parity rules out equality. Thus the maximum strictly decreases at each step, and it cannot decrease indefinitely among positive integers. The odd first entry never becomes zero, so the terminal lower entry is zero. The determinant and parity then give the terminal matrix \(\pm A^j\). Reversing these shears expresses every matrix in the claimed generators, proving the theorem in both directions.

For the requested level-four example, the left reductions are explicitly
\[
\begin{pmatrix}3&1\\8&3\end{pmatrix}
\xrightarrow{U^{-1}}
\begin{pmatrix}3&1\\-4&-1\end{pmatrix}
\xrightarrow{T}
\begin{pmatrix}-1&0\\-4&-1\end{pmatrix}
\xrightarrow{U^{-1}}-I.
\tag{9.2}
\]
Therefore \(U^{-1}TU^{-1}\gamma=-I\), or
\[
\gamma=-UT^{-1}U.
\tag{9.3}
\]
Multiplying the right side gives \(\begin{pmatrix}3&1\\8&3\end{pmatrix}\), confirming the signs.

### Solution 3

The group laws and all cusp expansions for \(\theta^8\) are in Section 4. By dimension three and independence of \(E_4(z),E_4(2z),E_4(4z)\), write \(\theta^8=\alpha E_4+\beta E_4(2z)+\gamma E_4(4z)\). The first three equations are
\[
\alpha+\beta+\gamma=1,\qquad
240\alpha=16,\qquad
2160\alpha+240\beta=112.
\]
Thus \(\alpha=1/15\), \(\beta=-2/15\), \(\gamma=16/15\), proving (7.2). Coefficient comparison yields
\[
r_8(n)=16\left(\sigma_3(n)-2\sigma_3(n/2)
                         +16\sigma_3(n/4)\right),
\tag{9.4}
\]
with nonintegral arguments understood to contribute zero.

For odd \(n\), every divisor is odd, so \((-1)^{n+d}=1\). Both (9.4) and the requested signed sum equal \(16\sigma_3(n)\).

For even \(n\), write \(n=2^am\), \(a\ge1\), \(m\) odd. The geometric sums \(S_a=1+8+\cdots+8^a\), with \(S_{-1}=0\), satisfy \(S_a=9S_{a-1}-8S_{a-2}\). Multiplying by \(\sigma_3(m)\) gives
\[
\sigma_3(n)=9\sigma_3(n/2)-8\sigma_3(n/4).
\tag{9.5}
\]
Use (9.5) in (9.4); its bracket becomes \(16\sigma_3(n/2)-\sigma_3(n)\). On the other hand, the sum of the cubes of the even divisors is \(8\sigma_3(n/2)\). Since \(n\) is even, the signs in the required sum are positive for even divisors and negative for odd divisors. Thus that signed sum is
\[
8\sigma_3(n/2)-\bigl(\sigma_3(n)-8\sigma_3(n/2)\bigr)
=16\sigma_3(n/2)-\sigma_3(n).
\]
This proves (7.3) for every positive integer. For example, the first three values are \(16,112,448\): at \(n=3\), select three of eight positions for \(\pm1\), giving \(\binom83 2^3=448\).

### Solution 4

Splitting the theta sum into its even and odd terms gives
\[
\theta(z+1/2)
=\sum_{n\text{ even}}q^{n^2}-\sum_{n\text{ odd}}q^{n^2}
=2\sum_{m\in\mathbb Z}q^{4m^2}-\theta(z),
\]
which is (4.6). With \(w=z+1/2\), the cusp matrix satisfies \(\sigma z=1/2-1/(4w)\). Inversion at \(w/4\) and \(w\) gives exactly (4.7). The principal-root identity \(2\sqrt{-iw/2}=\sqrt{-2iw}\) holds because its rescaling factor is positive, and both arguments remain in the right half-plane.

The even terms in \(\theta(w/4)\) are \(\theta(w)\). For an odd positive integer \(2j+1\), its paired positive and negative terms contribute
\[
2\exp\left(2\pi i\frac{(2j+1)^2(z+1/2)}4\right)
=2e^{\pi i/4}q^{1/4}q^{j(j+1)}.
\]
The phase is constant because \((2j+1)^2\equiv1\pmod8\). Sum over \(j\ge0\), raise (4.7) to the fourth power, and divide by \((2z+1)^2\). The two minus signs, from \((-i)^2\) and \(e^{\pi i}\), cancel, giving \(16qC(q)^4\).

This convergent power series has no negative powers and hence is holomorphic at the width-one cusp. Expanding \((1+q^2+q^6+\cdots)^4\) gives the four coefficients \(16,64,96,128\) at powers \(q,q^3,q^5,q^7\), respectively, as calculated in Example 6.2. This completes the cusp proof and the coefficient calculation.

### Solution 5

We construct the coefficient series (7.5) as a logarithmic derivative of a convergent product. This proves its modularity before any comparison with the theta square.

**Step 1: the product and its zeros.** For fixed \(z\in\mathfrak H\) and variable \(u\in\mathbb C\), put
\[
P_z(u)=\sin(\pi u)\prod_{n\ge1}
 (1-q^n e^{2\pi iu})(1-q^n e^{-2\pi iu}),
\qquad q=e^{2\pi iz}.
\tag{9.6}
\]
The product converges locally uniformly in \((z,u)\): on a compact set, \(|q|\le r<1\), and the absolute values of \(e^{2\pi iu}\) and its inverse are bounded by some \(K\). The sum of the deviations of the factors from one is at most \(2K\sum_{n\ge1}r^n\). For a sufficiently far tail each deviation has size less than \(1/2\), so its logarithm also has a summable uniform majorant. This proves convergence and shows the tail is nonzero. The finite initial factors are holomorphic, so \(P_z\) is entire in \(u\) and holomorphic in \(z\).

Its zeros are exactly \(u\in\mathbb Z+z\mathbb Z\), and all are simple. The sine accounts for the real integer translates. The factors with \(q^n e^{2\pi iu}\) account for the translates of \(-nz\), and those with \(q^n e^{-2\pi iu}\) for the translates of \(nz\), \(n\ge1\). These points are distinct modulo \(\mathbb Z\), because \(\operatorname{Im}z>0\); at each point just one displayed factor has a simple zero and all the others have nonzero product. Also \(P_z(-u)=-P_z(u)\).

Its quasiperiods are
\[
P_z(u+1)=-P_z(u),\qquad
P_z(u+z)=-e^{-\pi iz-2\pi iu}P_z(u).
\tag{9.7}
\]
The first follows directly from the sine. For the second, set \(v=e^{2\pi iu}\) and write
\[
P_z(u)=-\frac{e^{-\pi iu}}{2i}(1-v)
 \prod_{n\ge1}(1-q^nv)(1-q^nv^{-1}).
\]
Replacing \(u\) by \(u+z\) replaces \(v\) by \(qv\). The first string of factors loses \(1-v\), while the inverse string gains \(1-v^{-1}\). Their ratio, together with the sine factor, is
\[
e^{-\pi iz}\frac{1-v^{-1}}{1-v}
=-e^{-\pi iz}v^{-1}.
\]
This gives (9.7) away from the zeros, hence everywhere by holomorphy.

Define the meromorphic function
\[
L_z(u)=\frac{P'_z(u)}{P_z(u)},
\tag{9.8}
\]
where the prime differentiates in \(u\). Differentiating (9.7) and the oddness gives
\[
L_z(u+1)=L_z(u),\qquad
L_z(u+z)=L_z(u)-2\pi i,\qquad
L_z(-u)=-L_z(u).
\tag{9.9}
\]
These identities extend meromorphically through their poles.

**Step 2: the Fourier expansion.** In the strip \(|\operatorname{Im}u|<\operatorname{Im}z\), both \(|q e^{2\pi iu}|\) and \(|q e^{-2\pi iu}|\) are less than one. Logarithmic differentiation of (9.6), followed by the absolutely convergent geometric expansions, gives
\[
L_z(u)=\pi\cot(\pi u)
 +4\pi\sum_{n\ge1}\frac{q^n}{1-q^n}\sin(2\pi nu).
\tag{9.10}
\]
For completeness, the two product factors at index \(m\) contribute
\[
-2\pi i\sum_{n\ge1}q^{mn}e^{2\pi inu}
+2\pi i\sum_{n\ge1}q^{mn}e^{-2\pi inu}.
\]
Their sum is \(4\pi\sum_{n\ge1}q^{mn}\sin(2\pi nu)\). Summing in \(m\) yields (9.10). The compact-substrip bounds justify both differentiation and interchanging the two sums.

Now set
\[
E(z)=\frac{L_z(1/4)}{4\pi}.
\tag{9.11}
\]
The point \(1/4\) is never in \(\mathbb Z+z\mathbb Z\), so this is holomorphic on \(\mathfrak H\). Since \(\cot(\pi/4)=1\) and \(\sin(\pi n/2)=\chi_{-4}(n)\), equation (9.10) gives
\[
E(z)=\frac14+\sum_{d\ge1}\chi_{-4}(d)\frac{q^d}{1-q^d}
=\frac14+\sum_{n\ge1}\left(\sum_{d\mid n}\chi_{-4}(d)\right)q^n.
\tag{9.12}
\]
The last regrouping is absolute: for \(|q|\le r<1\), the sum of the absolute values of the Lambert terms is bounded by \((1-r)^{-1}\sum_{d\ge1}r^d\). This proves the claimed coefficients and the constant term.

**Step 3: the transformation of the logarithmic derivative.** First, \(P_{z+1}(u)=P_z(u)\), because its definition depends on \(z\) through \(q\); hence \(L_{z+1}(u)=L_z(u)\). To prove the inversion law, consider the entire function of \(u\)
\[
Q(u)=e^{-\pi iu^2/z}P_{-1/z}(u/z).
\tag{9.13}
\]
Its zeros are the same simple lattice zeros as those of \(P_z\): \(u/z\in\mathbb Z-z^{-1}\mathbb Z\) is equivalent to \(u\in z\mathbb Z+\mathbb Z\). Formula (9.7), including its inverse-shift version, gives
\[
Q(u+1)=-Q(u),\qquad
Q(u+z)=-e^{-\pi iz-2\pi iu}Q(u).
\]
For the first equality, the quadratic exponential contributes \(e^{-\pi i(2u+1)/z}\), and the shift by \(1/z\) in \(P_{-1/z}\) contributes \(-e^{\pi i/z+2\pi iu/z}\); they multiply to \(-1\). For the second, the argument of that product shifts by one, while the quadratic exponential contributes \(e^{-2\pi iu-\pi iz}\).

The quotient \(Q/P_z\) therefore extends to an entire function, including at the common simple zeros, and has periods \(1,z\). It is bounded on a compact fundamental parallelogram and hence on the whole plane. Liouville's theorem makes it constant. Taking its logarithmic derivative in \(u\) yields
\[
L_{-1/z}(u/z)=zL_z(u)+2\pi iu.
\tag{9.14}
\]
No value of that constant, and no product-normalization or square-root multiplier, is needed.

Since \(S,T\) generate \(\mathrm{SL}_2(\mathbb Z)\), these two identities compose to
\[
L_{\gamma z}\left(\frac{u}{cz+d}\right)
=(cz+d)L_z(u)+2\pi icu
\quad
\left(\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\right).
\tag{9.15}
\]
Here is the composition check for the extra term. If \(\delta\) has lower row \((c',d')\), put \(j_\delta=c'z+d'\) and \(j_\gamma=c(\delta z)+d\). Applying the two identities in succession gives the coefficient
\[
j_\gamma c'+\frac c{j_\delta}=ca'+dc'=c_{\gamma\delta}.
\tag{9.16}
\]
Multiply by \(j_\delta\) to verify this equality using \(a'd'-b'c'=1\). The leading factors multiply to \(j_{\gamma\delta}\). Thus the formula is closed under products. It is also closed under inverses by solving the same formula for the original \(L_z\); equivalently, apply the composition calculation to \(\gamma\gamma^{-1}=I\). This establishes (9.15) for every word in the generators and their inverses.

**Step 4: the level-four character law.** Let \(\gamma\in\Gamma_0(4)\), and write \(c=4C\). Substitute \(u=(cz+d)/4\) into (9.15). Quasiperiodicity and oddness in (9.9) give
\[
L_z(d/4+Cz)=\chi_{-4}(d)L_z(1/4)-2\pi iC.
\tag{9.17}
\]
Indeed \(d/4\) differs by an integer from \(1/4\) when \(d\equiv1\pmod4\), and from \(-1/4\) when \(d\equiv3\pmod4\). The extra term in (9.15) is \(2\pi iC(cz+d)\). It cancels the \(-2\pi iC(cz+d)\) produced by (9.17). Dividing by \(4\pi\) proves
\[
E(\gamma z)=\chi_{-4}(d)(cz+d)E(z).
\tag{9.18}
\]

**Step 5: all cusp expansions are holomorphic.** At infinity this follows from (9.12). For \(0\) and \(1/2\), take \(\gamma=S,\sigma\) in (9.15), respectively, and again make its transformed argument equal to \(1/4\). The result is
\[
E|_1S=\frac{L_z(z/4)+\pi i/2}{4\pi},\qquad
E|_1\sigma=\frac{L_z(z/2+1/4)+\pi i}{4\pi}.
\tag{9.19}
\]
Both points lie in the strip of (9.10), and neither is a lattice zero of \(P_z\).

To see the expansions explicitly, put \(v=e^{2\pi iu}\). For \(\operatorname{Im}u>0\),
\[
\cot(\pi u)=-i\frac{1+v}{1-v}
=-i-2i\sum_{\ell\ge1}v^\ell,
\qquad
\sin(2\pi nu)=\frac{v^n-v^{-n}}{2i}.
\tag{9.20}
\]
In the first expression in (9.19), \(v=q^{1/4}\). The cotangent contributes the constant \(-i\pi\) and positive powers \(q^{\ell/4}\). The sine terms, after expanding \(q^n/(1-q^n)\), have exponents
\[
jn+n/4\quad\hbox{or}\quad jn-n/4,
\qquad j,n\ge1,
\]
all positive integer multiples of \(1/4\). These series converge normally for small \(|q^{1/4}|\). Adding \(\pi i/2\) leaves constant \(-i\pi/2\), so \(E|_1S\) is a holomorphic series in the width-four coordinate with constant \(-i/8\).

In the second expression, \(v=iq^{1/2}\). All nonconstant exponents are again positive, now integer multiples of \(1/2\): those in the sine terms are \(jn\pm n/2\). The cotangent's constant \(-i\pi\) cancels the added \(\pi i\), leaving zero constant. The series is thus bounded and tends to zero. Its antiperiodicity, obtained from (9.18) and (4.11), eliminates the integral powers and allows exactly \(q^{m+1/2}\), \(m\ge0\). This is the required character cusp condition. We have proved
\[
E\in M_1(\Gamma_0(4),\chi_{-4})
\tag{9.21}
\]
with no cusp omitted.

**Step 6: use the dimension.** By Proposition 7.1, \(E\) is a scalar multiple of \(\theta^2\). Its constant term is \(1/4\), while that of \(\theta^2\) is one. Therefore \(\theta^2=4E\). Equations (1.8) and (9.12) now give (7.6). This deduction uses the dimension as requested; modularity of the divisor series was established independently.

For example, at \(n=5\) the divisors \(1,5\) both have character one, giving eight tuples \((\pm1,\pm2)\) and \((\pm2,\pm1)\). At \(n=3\), the characters of \(1,3\) cancel, giving no representation. In general the right side is four times the number of divisors congruent to one modulo four minus four times the number congruent to three. Even divisors contribute zero.

## What this lesson does not prove

The four principal assertions, both examples, and all five exercises are proved here. The weight-one dimension and the modularity of its divisor-coefficient series are also proved here. We use these stated prerequisites:

- **Real Fourier analysis is proved locally.** Theorem 1.1 proves Schwartz Poisson summation in every dimension, Fourier uniqueness, the Gaussian transform and the real theta relation (1.3)–(1.5), with the displayed Fourier kernel. The decay bound is (1.6), and the shifted Gaussian identity is deduced in Solution 1. No proof from another course or from a reference is assumed for these identities.
- **Earlier modular-form results.** The generators \(S,T\) of the full modular group are The upper half-plane and the modular group, Proposition 4.1. The three cusps, their widths, index six, absence of elliptic points and genus zero come from the congruence-subgroup lesson, Proposition 4.1, and the modular-curve lesson, Section 4. Sections 5 and 7 here prove the needed dimensions two, three and one directly from the valence formula proved in the dimension lesson, Theorem 3.1; general Riemann–Roch is not a dependency of those arguments. The Fourier normalizations and transformation of \(E_2\) are the Eisenstein lesson, Sections 4–5. Holomorphic modularity of \(E_2-tE_2(tz)\), \(t=2,4\), is proved in the earlier higher-level Hecke lesson directly after equation (7.3), including every cusp. The dilation needed for \(E_4\) is verified in Section 7.1 below the coefficient normalization.
- **Elementary complex analysis.** The first lesson, Lemma 0.2, proves the identity theorem, the circle formula and holomorphy of locally uniform limits; its coefficient bounds justify differentiation on smaller disks. The earlier Petersson lesson, Lemma 0.1, proves removable singularities and Liouville's theorem. Liouville applies only after the quotient in Solution 5 has been proved entire and bounded. No general theta-series modularity theorem or Jacobi null-value identity is imported into that solution.
- **Foundations still requiring an exact earlier proof.** Basic real integration, change of variables and differentiation under integrable majorants are used in Theorem 1.1. Its Fourier construction is local, but the underlying real-analysis foundations have not been matched to exact earlier programme proofs. The inherited elementary arithmetic and compactness foundations are likewise recorded in the earlier lessons. No claim of complete closure of those foundational dependencies is made.

General theta series of quadratic lattices are developed in the next lesson. Half-integral-weight modular forms and their general multiplier theory are not developed here.

## References

- A. V. Sutherland, *18.785 Number Theory I*, Fall 2021, Lecture 17, Theorem 17.8 and Lemma 17.9, for the Poisson and Gaussian comparison. [Original freely accessible lecture notes](https://ocw.mit.edu/courses/18-785-number-theory-i-fall-2021/mit18_785f21_lec17.pdf). Theorem 1.1 above proves the formulas locally, including the higher-dimensional extension.
- W. Stein, *Modular Forms: A Computational Approach*, Chapters 5–6, especially Section 5.3 for weight-two combinations and Section 6.3 for character-space background. [Freely accessible author-hosted text](https://wstein.org/books/modform/stein-modform.pdf), [free-distribution statement](https://wstein.org/books/modform/README.html). The weight-one dimension and coefficient-series construction have separate proofs in Proposition 7.1 and Solution 5.
- C. Teleman, *Riemann Surfaces*, Lent 2003 lecture notes, Lecture 13, for two-variable theta products and sums of two squares. [Author's freely accessible notes](https://math.berkeley.edu/~teleman/math/Riemann.pdf). The parameter dictionary is (1.2); the auxiliary product (9.6) is specified directly.
- J. Voight, *Quaternion Algebras*, Section 40.4. [Author's open-access edition](https://jvoight.github.io/quat.html). Its general modularity theorem does not replace the level-four proof.
- J. Lebl, *Guide to Cultivating Complex Analysis*, version 1.9, Theorems 2.4.7, 3.3.10 and 5.2.2, and Sections 3.2–3.3. [Author's free text](https://www.jirka.org/ca/ca.pdf).
