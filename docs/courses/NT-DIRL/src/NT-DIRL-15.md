# The Bombieri–Vinogradov theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A bound for one progression can be weak while a sum of such bounds is strong. The Bombieri–Vinogradov theorem makes this distinction precise: primes have the expected distribution, on average over moduli, almost as far as the square-root range suggested by the generalized Riemann hypothesis. The proof combines three kinds of cancellation. Short character sums control the smallest variable in Vaughan's identity; the multiplicative large sieve controls two long variables; Siegel–Walfisz handles small conductors.

We use *The Siegel–Walfisz theorem*, *The multiplicative large sieve and bilinear forms with characters*, and *Vaughan's identity and sums over primes*. The primitive Pólya–Vinogradov estimate is Theorem 1.1 of *Character sums: the Pólya–Vinogradov inequality*. The application also uses the arithmetic sieve inequality, already proved in Section 6 of *The large sieve inequality*. Only that proved inequality is needed, not its deeper discussion of the exact Brun–Titchmarsh constant.

Write \(L=\log(2x)\), \(\sum_\chi^*\) for primitive characters, and

\[
\begin{aligned}
E_\psi(x,q)&=\max_{0\le y\le x}\max_{(b,q)=1}
\left|\psi(y;q,b)-\frac y{\varphi(q)}\right|,\\
E_\theta(x,q)&=\max_{0\le y\le x}\max_{(b,q)=1}
\left|\theta(y;q,b)-\frac y{\varphi(q)}\right|,\\
E_\pi(x,q)&=\max_{2\le y\le x}\max_{(b,q)=1}
\left|\pi(y;q,b)-\frac{\operatorname{li}(y)}{\varphi(q)}\right|.
\end{aligned}
\tag{0.1}
\]

Here \(x\ge2\), \(\operatorname{li}(y)=\int_2^ydu/\log u\), and \(b\) ranges over reduced residue classes. Maxima over real cutoffs mean suprema; a supremum can occur at the left limit of a prime-power jump. For character sums without a continuous subtracted main term, the cutoff can be restricted to integers and the maximum is attained. Changing the additive normalization of \(\operatorname{li}\) changes the later estimates by \(O(\sum_{q\le Q}1/\varphi(q))\), which is harmless. Constants are effective until Siegel–Walfisz is used.

## 1. Conductors and the principal character

Two elementary totient estimates will also supply the constant in the application. Put

\[
\mathcal C=\prod_p\left(1+\frac1{p(p-1)}\right)
=\frac{\zeta(2)\zeta(3)}{\zeta(6)}.
\tag{1.1}
\]

The product converges absolutely. The equality follows by checking each local factor:

\[
1+\frac1{p(p-1)}=
\frac{1-p^{-6}}{(1-p^{-2})(1-p^{-3})}.
\]

**Lemma 1.1.** Uniformly for \(z\ge1\),

\[
\sum_{n\le z}\frac1{\varphi(n)}=\mathcal C\log z+O(1),
\qquad
\sum_{n\le z}\frac n{\varphi(n)}\ll z.
\tag{1.2}
\]

Consequently \(q/\varphi(q)\ll\log(2q)\), and, for \(d\le Q\),

\[
\sum_{\substack{q\le Q\\d\mid q}}\frac1{\varphi(q)}
\ll\frac{\log(2Q/d)}{\varphi(d)}.
\tag{1.3}
\]

**Proof.** Multiplication of the prime-power factors gives

\[
\frac n{\varphi(n)}=\sum_{d\mid n}\frac{\mu^2(d)}{\varphi(d)}.
\tag{1.4}
\]

Set \(a(d)=\mu^2(d)/(d\varphi(d))\). Its sum is \(\mathcal C\), and \(\sum_da(d)\log(2d)<\infty\). For the latter assertion, the logarithmic contribution of a prime in the absolutely convergent product is at most a constant times \(\log p/[p(p-1)]\); its sum converges by comparison with \(\sum_{n\ge2}\log n/n^2\). Rearranging the finite sum in (1.4) gives

\[
\sum_{n\le z}\frac1{\varphi(n)}
=\sum_{d\le z}a(d)H_{\lfloor z/d\rfloor},
\qquad H_k=\sum_{m\le k}\frac1m.
\]

Since \(H_{\lfloor t\rfloor}=\log t+O(1)\) for \(t\ge1\), the difference from \(\mathcal C\log z\) is bounded by a constant times \(\sum_da(d)\log(2d)\). In particular, the omitted tail satisfies \(\log z\sum_{d>z}a(d)\le\sum_{d>z}a(d)\log d\). This proves the first estimate. Summing (1.4) without the factor \(1/n\) proves the second, since \(\lfloor z/d\rfloor\le z/d\). Also \(q/\varphi(q)\le\sum_{d\le q}1/\varphi(d)\), which gives the pointwise consequence.

Finally \(\varphi(dm)\ge\varphi(d)\varphi(m)\), as is checked at every prime: equality holds for disjoint prime factors, and the ratio is \(p/(p-1)\) when the prime occurs in both. Apply the first estimate to \(m\le Q/d\). \(\square\)

For a character \(\chi\), define

\[
\psi'(y,\chi)=\psi(y,\chi)-\mathbf1_{\chi=\chi_0}y.
\tag{1.5}
\]

Character orthogonality gives the exact identity

\[
\psi(y;q,b)-\frac y{\varphi(q)}
=\frac1{\varphi(q)}\sum_{\chi\bmod q}
\overline{\chi(b)}\psi'(y,\chi).
\tag{1.6}
\]

The principal term cannot simply be deleted: \(\psi(y,\chi_0)\) is not exactly \(y\). Defining \(\psi'\) incorporates its error.

Suppose \(\chi\pmod q\) is induced by primitive \(\chi^*\pmod d\), \(d\mid q\). The difference consists precisely of the omitted prime powers:

\[
\psi'(y,\chi^*)-\psi'(y,\chi)
=\sum_{\substack{p\mid q\\ p\nmid d}}\sum_{p^k\le y}
\chi^*(p)^k\log p.
\tag{1.7}
\]

The subtracted main terms agree, including \(d=1\). Each prime contributes at most \(\log(2x)\), so for \(q\le Q\le\sqrt x\) the absolute difference is \(O(L^2)\), uniformly over \(0\le y\le x\). Each primitive character induces exactly one character modulo each multiple of its conductor. The triangle inequality, (1.3), and (1.6) therefore give

\[
\sum_{q\le Q}E_\psi(x,q)
\ll QL^2+
\sum_{d\le Q}\frac{\log(2Q/d)}{\varphi(d)}
\sum_{\chi\bmod d}^{*}\max_{y\le x}|\psi'(y,\chi)|.
\tag{1.8}
\]

The initial error is \(QL^2\), not a sum of \(Q^2\) errors: for each modulus the factor \(1/\varphi(q)\) cancels its number of characters before summation.

## 2. A maximal first moment over primitive characters

Define

\[
\mathcal T(x,Q)=\sum_{q\le Q}\frac q{\varphi(q)}
\sum_{\chi\bmod q}^{*}\max_{0\le y\le x}|\psi(y,\chi)|.
\]

**Theorem 2.1.** For every \(x\ge2\) and \(Q\ge1\),

\[
\mathcal T(x,Q)\ll
\left(x+Qx^{5/6}+Q^2\sqrt x\right)L^3.
\tag{2.1}
\]

The conductor-one character is included. The constants in this theorem are effective.

**Proof.** First suppose \(Q\le\sqrt x\). Apply Vaughan's identity with \(1\le U,V\le x\):

\[
\Lambda=\Lambda_{\le U}+\mu_{\le V}*\log-c*\mathbf1+\alpha*\beta,
\tag{2.2}
\]

where \(c=\Lambda_{\le U}*\mu_{\le V}\), \(\alpha=\Lambda_{>U}*\mathbf1\), and \(\beta=\mu_{>V}\). Thus \(c(t)=0\) for \(t>UV\), \(|c(t)|\le\log t\), \(\alpha(m)=0\) for \(m\le U\), \(0\le\alpha(m)\le\log m\), and \(|\beta(n)|\le1\), with \(\beta(n)=0\) for \(n\le V\). Every estimate below has a majorant independent of \(y\).

For primitive nonprincipal \(\chi\pmod q\), Pólya–Vinogradov gives

\[
\max_{Y\ge0}\left|\sum_{n\le Y}\chi(n)\right|
\ll\sqrt q\log(2q).
\tag{2.3}
\]

The term \(c*\mathbf1\), restricted to \(t\le U\), is consequently bounded by \(U\sqrt q\,L^2\). Summing over the primitive family with weight \(q/\varphi(q)\) gives \(O(Q^{5/2}UL^2)\), since the weighted number at modulus \(q\) is at most \(q\). At conductor 1, use instead

\[
\sum_{t\le U}|c(t)|\left\lfloor\frac xt\right\rfloor
\ll xL^2.
\]

For \(\mu_{\le V}*\log\), partial summation in the second variable multiplies (2.3) by at most \(2L\). The same argument bounds its weighted maximum by \(O((x+Q^{5/2}V)L^2)\). Its conductor-one contribution is bounded by \(xL\sum_{d\le V}1/d\ll xL^2\). Finally \(\Lambda_{\le U}\) contributes \(O(Q^2U)\), by the elementary Chebyshev estimate.

The two remaining pieces have two variables. To see the estimates explicitly, restrict \(m\) to a dyadic block \((M,2M]\), clip its support as necessary, and let \(n\le x/M\). The maximal bilinear estimate in Theorem 3.1 of the preceding lesson gives

\[
\begin{aligned}
&\sum_{q\le Q}\frac q{\varphi(q)}\sum_\chi^*
\max_{y\le x}\left|\sum_{\substack{M<m\le2M\\mn\le y}}
a_m b_n\chi(mn)\right|\\
&\hspace{12mm}\ll
\left(x+Q\sqrt{xM}+\frac{Qx}{\sqrt M}+Q^2\sqrt x\right)L^2,
\end{aligned}
\tag{2.4}
\]

provided \(|a_m|\le L\), \(|b_n|\le1\). Indeed, the coefficient norms have product \(O(\sqrt x\,L)\), and expanding \(\sqrt{(2M+Q^2)(x/M+Q^2)}\) gives the four displayed terms. This argument retains the product cutoff and the maximum; the maximizing \(y\) may vary with \(\chi\).

For \(\alpha*\beta\), the block parameter satisfies \(U/2\le M\le x/V\). Summing \(O(L)\) blocks in (2.4) gives

\[
\ll\left(x+\frac{Qx}{\sqrt U}+\frac{Qx}{\sqrt V}+Q^2\sqrt x\right)L^3.
\tag{2.5}
\]

This is also Corollary 11.1 of the preceding lesson. For the part of \(c*\mathbf1\) with \(U<t\le UV\), the first variable satisfies \(U/2\le M\le UV\), while the second has no lower cutoff. Its corresponding bound is

\[
\ll\left(x+\frac{Qx}{\sqrt U}+Q\sqrt{xUV}+Q^2\sqrt x\right)L^3.
\tag{2.6}
\]

If a range is empty, its contribution is zero. Real cutoffs and rounded supports change only absolute constants. Combining all pieces proves

\[
\begin{aligned}
\mathcal T(x,Q)\ll\bigg(&x+\frac{Qx}{\sqrt U}+\frac{Qx}{\sqrt V}
+Q\sqrt{xUV}+Q^2\sqrt x\\
&+Q^{5/2}(U+V)+Q^2U\bigg)L^3.
\end{aligned}
\tag{2.7}
\]

Here logarithms of the parameters are \(O(L)\), since \(U,V\le x\) and \(Q\le\sqrt x\).

Take \(U=V=W\). For \(Q\le x^{1/3}\), choose \(W=x^{1/3}\). Then \(Qx/\sqrt W=Qx^{5/6}\), \(Q\sqrt x\,W=Qx^{5/6}\), and \(Q^{5/2}W\le Qx^{5/6}\). Also \(Q^2W\le Q^2\sqrt x\). For \(x^{1/3}<Q\le\sqrt x\), choose \(W=x^{2/3}/Q\). In this range

\[
Qx/\sqrt W=Q^{3/2}x^{2/3}\le Q^2\sqrt x,
\quad Q\sqrt x\,W=x^{7/6}\le Q^2\sqrt x,
\]

and \(Q^{5/2}W=Q^{3/2}x^{2/3}\le Q^2\sqrt x\). The remaining \(Q^2W\) is smaller as well. These substitutions prove (2.1) for \(Q\le\sqrt x\).

If \(Q>\sqrt x\), apply the same maximal bilinear theorem directly with \(a_1=1\) and \(b_n=\Lambda(n)\), \(n\le x\). Chebyshev gives \(\sum_{n\le x}\Lambda(n)^2\le L\psi(x)\ll xL\). Hence

\[
\mathcal T(x,Q)\ll
\sqrt{(1+Q^2)(x+Q^2)}\sqrt{xL}\,L
\ll Q^2\sqrt x\,L^{3/2},
\]

which implies (2.1). \(\square\)

The square-root boundary in this estimate is visible in \(Q^2\sqrt x\). Passing from the weight \(q/\varphi(q)\) to \(1/\varphi(q)\) on a conductor block of size \(Q\) turns this into \(Q\sqrt x\), precisely the scale in Bombieri–Vinogradov.

### Direct progression estimates

There is another useful organization of Vaughan's identity. Its Type I part is well distributed in progressions by direct counting, and its Type II part has cancellation at small conductors even after an additional coprimality restriction. We prove both facts, so that this alternative organization does not conceal an extra input.

For an arithmetic function \(f\), put

\[
\Delta_f(t;q,b)=\sum_{\substack{n\le t\\n\equiv b\pmod q}}f(n)
-\frac1{\varphi(q)}\sum_{\substack{n\le t\\(n,q)=1}}f(n).
\tag{2.8}
\]

**Lemma 2.2 (Type I distribution).** If \(f\) is supported on \(1\le n\le Z\), \(v\ge0\), \(t\ge2\), and \((b,q)=1\), then

\[
|\Delta_{f*(\log)^v}(t;q,b)|
\le2(\log t)^v\sum_{k\le Z}|f(k)|.
\tag{2.9}
\]

For \(v=0\), the function \((\log)^0\) means \(\mathbf1\), including at 1.

**Proof.** Each reduced residue class contains either \(\lfloor u/q\rfloor\) or \(\lfloor u/q\rfloor+1\) positive integers up to \(u\). Its count differs from the average over reduced classes by at most 1. Thus \(|\Delta_{\mathbf1}(u;q,j)|\le1\). If \(v>0\), partial summation and monotonicity of \((\log u)^v\) give

\[
|\Delta_{(\log)^v}(u;q,j)|
\le(\log u)^v+\int_1^u d(\log s)^v=2(\log u)^v.
\]

For \(v=0\) the stronger constant 1 suffices. Open the convolution in (2.8). Only \(k\) coprime to \(q\) contribute, and the inner discrepancy is
\(\Delta_{(\log)^v}(t/k;q,bk^{-1})\), with its average divided by \(\varphi(q)\). Bound it as above and sum the absolute coefficients. Terms \(k>t\) are empty. This proves (2.9). \(\square\)

In particular, for \(\Lambda^\sharp=\mu_{\le V}*\log-c*\mathbf1\),

\[
\max_{y\le x}\max_{(b,q)=1}|\Delta_{\Lambda^\sharp}(y;q,b)|
\ll UVL.
\tag{2.10}
\]

The two coefficient sums are at most \(V\) and \(UV\log(UV)\), with the latter interpreted as zero when \(UV=1\). They are bounded by \(O(UVL)\) after the logarithmic factor for the first term is included.

**Lemma 2.3 (small conductors with a selector).** Fix \(A,C\ge1\). Suppose \(x\ge3\), \(1\le U\le x\), \(e^{\sqrt{\log x}}\le V\le x\), \(r\le x\) is a positive integer, and \(\chi\) has modulus \(q\le(\log x)^C\). Then

\[
\max_{0\le y\le x}\left|
\sum_{n\le y}\Lambda^\flat(n)\chi(n)\mathbf1_{(n,r)=1}
\right|\ll_{A,C}xL^{-A},
\qquad \Lambda^\flat=\alpha*\beta.
\tag{2.11}
\]

The constant is ineffective. The principal character is allowed.

**Proof.** Write \(M(t,\chi)=\sum_{n\le t}\mu(n)\chi(n)\). The earlier Möbius form of Siegel–Walfisz proves
\(|M(t,\chi)|\ll_C t e^{-c\sqrt{\log t}}\) whenever the modulus is a fixed power of \(\log t\). We first transfer this estimate to

\[
M_r(t,\chi)=\sum_{\substack{n\le t\\(n,r)=1}}\mu(n)\chi(n),
\qquad V\le t\le x.
\]

Let \(\mathcal R_r\) be the positive integers all of whose prime factors divide \(r\), including 1. A local prime-power check gives

\[
M_r(t,\chi)=\sum_{\substack{d\le t\\d\in\mathcal R_r}}
\chi(d)M(t/d,\chi).
\tag{2.12}
\]

At a prime dividing \(r\), convolution of \(1-\chi(p)z\) with \((1-\chi(p)z)^{-1}\) leaves 1. At other primes the Möbius factor is unchanged. This proves (2.12) also when \(\chi(p)=0\).

For \(d\le\sqrt t\), one has \(\log(t/d)\ge\frac12\sqrt{\log x}\). Consequently \(q\le(\log(t/d))^{3C}\) for sufficiently large \(x\). Siegel–Walfisz at this fixed exponent bounds that part of (2.12) by

\[
\ll_C t e^{-c'(\log x)^{1/4}}
\sum_{d\in\mathcal R_r}\frac1d
=t e^{-c'(\log x)^{1/4}}\,O_C(r/\varphi(r))
\ll_C tL e^{-c'(\log x)^{1/4}}.
\tag{2.13}
\]

For the remaining \(d\), the trivial bound for \(M\) gives \(t\sum_{d>\sqrt t,\ d\in\mathcal R_r}1/d\). Put \(\eta=1/[4\log(2L)]\). Then

\[
\sum_{\substack{d>\sqrt t\\d\in\mathcal R_r}}\frac1d
\le t^{-\eta/2}\prod_{p\mid r}(1-p^{-1+\eta})^{-1}
\ll(\log(2L))^K\exp\left(-\frac{\log t}{8\log(2L)}\right)
\tag{2.14}
\]

for an absolute effective \(K\). To justify the product bound, split its primes at \(L^2\). At smaller primes \(p^\eta\le e^{1/2}\), and
\(-\log(1-p^{-1+\eta})\ll1/p\). The reciprocal-prime estimate
\(\sum_{p\le w}1/p=\log\log w+O(1)\), proved in *Dirichlet's theorem on primes in arithmetic progressions* (or the principal case of the Mertens results in *The Siegel–Walfisz theorem*), bounds the product there by a power of \(\log(2L)\). At larger primes each \(p^{-1+\eta}\le e^{1/2}/L^2\), and there are at most \(\log r/\log2\le L/\log2\) of them. Their product is bounded absolutely. This proves (2.14).

Since \(\log t\ge\sqrt{\log x}\), both (2.13) and \(t\) times (2.14) are \(O_{H,C}(tL^{-H})\) for every fixed \(H>0\), uniformly over \(V\le t\le x\) and \(r\le x\). Therefore

\[
|M_r(t,\chi)|\ll_{H,C}tL^{-H}.
\tag{2.15}
\]

Finally open the convolution \(\alpha*\beta\). For a fixed \(m\le y/V\), the inner sum over \(V<n\le y/m\), including the coprimality selector, is
\(M_r(y/m,\chi)-M_r(V,\chi)\). Its modulus is at most
\(O_{H,C}((y/m)L^{-H})\) because \(y/m\ge V\). Since \(|\alpha(m)|\le\log m\) and \((mn,r)=1\) splits into its two selectors, the total is at most

\[
O_{H,C}\left(yL^{-H}\sum_{m\le y/V}\frac{\log m}{m}\right)
\ll_{H,C}xL^{2-H}.
\]

Take \(H=A+2\). Empty ranges contribute zero; enlarging the ineffective constant covers the bounded initial range of \(x\). This proves (2.11). \(\square\)

Thus direct progression counting, small-conductor Möbius cancellation and the maximal Type II estimate are compatible approaches to the same prime-sum decomposition. In the proof that follows, Theorem 2.1 packages the large-conductor estimates into one first moment.

## 3. Small and large conductors

**Theorem 3.1 (Bombieri–Vinogradov).** Fix \(D>0\). Uniformly for

\[
\sqrt x\,L^{-D}\le Q\le\sqrt x,\qquad x\ge2,
\]

we have

\[
\sum_{q\le Q}E_\psi(x,q)\ll_D Q\sqrt x\,L^3.
\tag{3.1}
\]

In particular, for every \(A>0\), the choice

\[
\boxed{B(A)=A+3}
\tag{3.2}
\]

gives

\[
\sum_{q\le Q}E_\psi(x,q)\ll_A\frac{x}{(\log x)^A}
\quad\left(1\le Q\le\frac{\sqrt x}{(\log x)^{A+3}}\right).
\tag{3.3}
\]

The constants in these assertions are ineffective.

**Proof.** Let \(R=L^{D+1}\). First handle conductors \(d\le R\) in (1.8). The character form of Siegel–Walfisz, proved along with the progression form in the earlier lesson, gives

\[
\max_{0\le y\le x}|\psi'(y,\chi)|
\ll_D xe^{-c\sqrt{\log x}}\quad(d\le R).
\tag{3.4}
\]

To verify its uniformity in the cutoff, split at \(\sqrt x\). Below that point use \(|\psi'(y,\chi)|\le\psi(y)+y\ll\sqrt x\). Above it, \(d\le L^{D+1}\le(\log y)^{2(D+1)}\) for sufficiently large \(x\), so the earlier theorem applies with that fixed parameter. A smaller absolute \(c>0\) absorbs both pieces. The initial threshold and the resulting implied constant are ineffective. Since there are at most \(\varphi(d)\) primitive characters at \(d\), their total contribution to (1.8) is

\[
\ll_D RLxe^{-c\sqrt{\log x}}.
\tag{3.5}
\]

For the remaining conductors partition \(R<d\le Q\) into blocks \(r<d\le2r\), \(r=2^jR\), clipping the last one. They are all greater than 1, so \(\psi'=\psi\). Theorem 2.1 gives

\[
\begin{aligned}
&\sum_{r<d\le\min(2r,Q)}\frac{\log(2Q/d)}{\varphi(d)}
\sum_\chi^*\max_{y\le x}|\psi(y,\chi)|\\
&\quad\ll
\left(\frac xr+x^{5/6}+r\sqrt x\right)L^3\log(2Q/r).
\end{aligned}
\tag{3.6}
\]

The factor \(1/r\) here is the conversion from the large-sieve weight. The three sums over \(r\) behave differently:

\[
\begin{aligned}
\sum_r\frac{\log(2Q/r)}r&\ll L/R,\\
\sum_r\log(2Q/r)&\ll L^2,\\
\sum_r r\log(2Q/r)&\ll Q.
\end{aligned}
\tag{3.7}
\]

For the first bound use \(r\ge2^jR\) and \(\log(2Q/r)\le L\). For the second there are \(O(L)\) blocks, each with logarithm \(O(L)\). For the third count backwards from the largest block: the terms are bounded by constant multiples of \(Q2^{-k}(k+1)\), whose sum converges. Retaining this last geometric estimate avoids an unnecessary logarithmic loss.

The large-conductor part of (1.8) is therefore at most

\[
\ll\frac xR L^4+x^{5/6}L^5+Q\sqrt x\,L^3.
\tag{3.8}
\]

Because \(Q\ge\sqrt x\,L^{-D}\) and \(R=L^{D+1}\), the first term is at most \(Q\sqrt x\,L^3\). For fixed \(D\), the second has the same upper bound for all sufficiently large \(x\), since \(x^{-1/6}L^{D+2}\to0\). The term (3.5) and the initial \(QL^2\) in (1.8) are also absorbed. Enlarging the constant on the bounded initial range proves (3.1).

For (3.3), apply (3.1) with \(D=A+3\) at \(Q_0=\sqrt x/(\log x)^{A+3}\), then use monotonicity of the sum for \(Q\le Q_0\). For \(x\ge3\), \(Q_0\le\sqrt x\), \(Q_0\ge\sqrt x\,L^{-D}\), and \(L/\log x\) is bounded. Thus \(Q_0\sqrt x\,L^3\ll_A x(\log x)^{-A}\). If \(Q_0<1\) there is no admissible \(Q\); the remaining bounded values \(2\le x<3\) are handled by enlarging the constant. \(\square\)

All estimates after (3.4) are effective. The ineffectivity of Bombieri–Vinogradov in this proof comes solely from the small-conductor theorem. It does not arise from the large sieve or from the maximal cutoff.

An alternative treatment applies the elementary progression estimate directly to the Type I part of Vaughan's identity and the large sieve only to the Type II part. The maximal character argument above has the advantage that the conductor reduction and the exceptional principal term remain explicit throughout.

## 4. Prime weights, prime counts and exceptional moduli

**Corollary 4.1.** In the range of Theorem 3.1,

\[
\sum_{q\le Q}E_\theta(x,q)\ll_D Q\sqrt x\,L^3,
\qquad
\sum_{q\le Q}E_\pi(x,q)\ll_D Q\sqrt x\,L^2.
\tag{4.1}
\]

Consequently the range in (3.3), with the same \(B(A)=A+3\), gives

\[
\sum_{q\le Q}E_\theta(x,q)\ll_A x(\log x)^{-A},
\qquad
\sum_{q\le Q}E_\pi(x,q)\ll_A x(\log x)^{-A-1}.
\tag{4.2}
\]

**Proof.** The total weight of proper prime powers is \(O(\sqrt x)\). Indeed, it is bounded by \(\sum_{2\le k\le\log_2x}\theta(x^{1/k})\). The \(k=2\) term is \(O(\sqrt x)\) by Chebyshev, and the others are \(O(x^{1/3}L)=O(\sqrt x)\), after treating a bounded initial interval. This uniform bound proves \(E_\theta(x,q)\le E_\psi(x,q)+O(\sqrt x)\), and hence the first assertion.

For prime counts we prove the useful maximal estimate

\[
E_\pi(x,q)\ll\frac{E_\theta(x,q)+\sqrt x}{L}.
\tag{4.3}
\]

For \(x\ge16\), put \(z=\sqrt x\). When \(2\le y\le z\), Chebyshev's prime bound and \(|\operatorname{li}(y)|\ll z/\log z\) give \(O(\sqrt x/L)\) for the prime-count error, uniformly in \(q,b\). For \(z\le y\le x\), exact partial summation between \(z\) and \(y\) gives

\[
\begin{aligned}
\pi(y;q,b)-\frac{\operatorname{li}(y)}{\varphi(q)}
={}&\pi(z;q,b)-\frac{\operatorname{li}(z)}{\varphi(q)}\\
&+\frac{E_\theta(y;q,b)}{\log y}
-\frac{E_\theta(z;q,b)}{\log z}
+\int_z^y\frac{E_\theta(u;q,b)}{u\log^2u}\,du,
\end{aligned}
\tag{4.4}
\]

where \(E_\theta(u;q,b)=\theta(u;q,b)-u/\varphi(q)\). The lower endpoint is \(O(\sqrt x/L)\); the remaining terms are bounded by \(O(E_\theta(x,q)/L)\), because \(\log z\) is comparable to \(L\) and \(\int_z^xdu/(u\log^2u)\ll1/L\). This proves (4.3). The bounded range \(2\le x<16\) is absorbed into an absolute constant. Summing (4.3) and the theta estimate proves (4.1); monotonicity gives (4.2). \(\square\)

The lower-argument split is essential to the extra factor \(1/\log x\). Applying partial summation from 2 and bounding every error by its maximum would only give a constant multiple of that maximum.

There is also a useful consequence with squared maxima.

**Corollary 4.2.** Under the same hypotheses,

\[
\begin{aligned}
\sum_{q\le Q}qE_\psi(x,q)^2&\ll_D x^{3/2}QL^4,\\
\sum_{q\le Q}qE_\theta(x,q)^2&\ll_D x^{3/2}QL^4,\\
\sum_{q\le Q}qE_\pi(x,q)^2&\ll_D x^{3/2}QL^2.
\end{aligned}
\tag{4.5}
\]

**Proof.** There are at most \(x/q+1\) integers in a residue class up to \(x\). By Lemma 1.1, \(q/\varphi(q)\ll L\) for \(q\le\sqrt x\). It follows that \(qE_\psi(x,q)\ll xL\) and \(qE_\theta(x,q)\ll xL\), including small cutoffs \(y<q\). For \(\pi\), the counting term contributes \(O(x)\), while \(q|\operatorname{li}(y)|/\varphi(q)\ll x\), so \(qE_\pi(x,q)\ll x\). Multiply these bounds by the respective errors and sum using (3.1) or (4.1). \(\square\)

These are squares of maxima, not the sharper mean over all residue classes in the Barban–Davenport–Halberstam theorem. That distinction is the subject of the next lesson.

For a fixed \(0<\varepsilon<1/2\), set \(X=x^{1/2-\varepsilon}\). Applying (4.2) with \(A=4\) gives, for large \(x\),

\[
\begin{aligned}
\#\bigg\{q\le X:\ 
&\max_{(b,q)=1}\left|\pi(x;q,b)-\frac{\operatorname{li}(x)}{\varphi(q)}\right|\\
&>\frac{\operatorname{li}(x)}{\varphi(q)\log x}
\bigg\}\ll\frac X{(\log x)^3}=o(X).
\end{aligned}
\tag{4.6}
\]

Every exceptional modulus contributes at least a constant times \(x/[X(\log x)^2]\) to the error sum, since \(\varphi(q)\le X\) and \(\operatorname{li}(x)\sim x/\log x\). Outside this one exceptional set the relative asymptotic holds uniformly for every reduced class. The theorem does not assert that every modulus in the square-root range has a small error.

## 5. Divisors of a prime minus one

We will prove the Titchmarsh divisor asymptotic, in its usual unweighted normalization:

\[
\boxed{\sum_{p\le x}d(p-1)=\mathcal Cx+
O\left(\frac{x\log\log(3x)}{\log x}\right),\qquad
\mathcal C=\frac{\zeta(2)\zeta(3)}{\zeta(6)}.}
\tag{5.1}
\]

Here \(d(m)\) counts the positive divisors of \(m\). The error constant is ineffective. This is an application that really needs moduli approaching the square-root range.

First we prove the upper bound for progressions used to discard the middle divisors. No optimal constant is required.

**Lemma 5.1.** There is an effective absolute constant \(K\) such that

\[
\pi(t;q,b)\le K\frac{t}{\varphi(q)\log(t/q)}
\quad(t\ge3,\ 1\le q\le\sqrt t,\ (b,q)=1).
\tag{5.2}
\]

**Proof.** Put \(R=\sqrt{t/q}\). Represent the positive integers congruent to \(b\) by \(qk+b\), with \(1\le b\le q\), and a block of at most \(t/q+1\) integer values of \(k\). For each prime \(\ell\nmid q\), a prime \(qk+b>R\) avoids the single class \(k\equiv-bq^{-1}\pmod\ell\). When \(\ell\mid q\), no class is excluded, since \((b,q)=1\).

The arithmetic large sieve, with these forbidden classes, bounds their number by

\[
\frac{2t/q}{L_q(R)},\qquad
L_q(R)=\sum_{\substack{d\le R\\(d,q)=1}}\frac{\mu^2(d)}{\varphi(d)}.
\tag{5.3}
\]

Indeed its numerator is the block length minus 1 plus \(R^2\), at most \(t/q+R^2=2t/q\). This is precisely the proved selector form of the arithmetic sieve inequality. Primes at most \(R\) add at most \(R\).

We need a lower bound for this denominator uniform in \(q\). For squarefree \(d\), the product of the geometric series at its primes gives

\[
\frac1{\varphi(d)}=\sum_{\operatorname{rad}(m)=d}\frac1m.
\]

All terms are nonnegative. Thus

\[
L_q(R)\ge H_q(R):=
\sum_{\substack{m\le R\\(m,q)=1}}\frac1m.
\tag{5.4}
\]

Möbius inclusion–exclusion gives

\[
H_q(R)=\sum_{\substack{d\mid\operatorname{rad}(q)\\d\le R}}
\frac{\mu(d)}d H_{\lfloor R/d\rfloor}.
\]

Using \(H_{\lfloor u\rfloor}=\log u+\gamma+O(1/u)\) for \(u\ge1\), and inserting the omitted divisors \(d>R\), yields

\[
\begin{aligned}
H_q(R)={}&\frac{\varphi(q)}q
\left(\log R+\gamma+
\sum_{\ell\mid q}\frac{\log\ell}{\ell-1}\right)\\
&+O\left(\frac{2^{\omega(q)}\log(2q)}R\right).
\end{aligned}
\tag{5.5}
\]

The coefficient of \(\log R+\gamma\) is \(\sum_{d\mid\operatorname{rad}(q)}\mu(d)/d=\varphi(q)/q\). Differentiating that finite product with respect to the exponents, or expanding one prime at a time, gives
\(-\sum_{d\mid\operatorname{rad}(q)}\mu(d)\log d/d=
(\varphi(q)/q)\sum_{\ell\mid q}\log\ell/(\ell-1)\).
The harmonic-number errors sum to \(O(2^{\omega(q)}/R)\); each inserted divisor is at most \(q\) and contributes at most \(O(\log(2q)/R)\). This proves (5.5). The standard harmonic estimate follows directly by comparing \(1/m\) with \(\int_m^{m+1}du/u\); the tail difference is \(O(1/m)\). The limit \(\gamma=\lim(H_m-\log m)\) lies in \([0,1]\).

For any fixed \(\eta>0\), the elementary product estimates

\[
2^{\omega(q)}\ll_\eta q^\eta,\qquad
q/\varphi(q)\ll_\eta q^\eta
\tag{5.6}
\]

are effective. To prove them, choose a finite bound for the primes below which \(2>\ell^\eta\), or \(\ell/(\ell-1)>\ell^\eta\); multiply their finitely many exceptional factors into the constant. At all larger prime factors the desired local inequality holds, and \(\operatorname{rad}(q)\le q\).

Here \(q\le\sqrt t\), \(R\ge t^{1/4}\). With \(\eta=1/16\), the error in (5.5), after division by \(\varphi(q)/q\), is \(O(t^{-3/16}\log(2t))\). The nonnegative terms involving \(\gamma\) and \(\log\ell\) may be discarded, while \(\log R\ge(\log t)/4\). Therefore, beyond an effective absolute threshold,

\[
H_q(R)\ge\frac{\varphi(q)}{2q}\log R.
\tag{5.7}
\]

Equations (5.3)–(5.7) bound \(\pi(t;q,b)\) by \(R+O(t/[\varphi(q)\log(t/q)])\). The first term is absorbed because \(\log u\ll\sqrt u\) for \(u=t/q\ge1\). Enlarge \(K\) for the bounded initial range, in which \(\log(t/q)>0\). This proves the lemma. \(\square\)

**Proof of (5.1).** Put \(Y=\lfloor\sqrt{x-1}\rfloor\). Pairing divisors about \(\sqrt m\) gives the exact hyperbola identity

\[
\sum_{p\le x}d(p-1)=
2\sum_{d\le Y}\bigl(\pi(x;d,1)-\pi(d^2;d,1)\bigr)
-\#\{p\le x\mid p-1\text{ is a square}\}.
\tag{5.8}
\]

A divisor \(d\) enters the smaller half exactly when \(p-1\ge d^2\), which is the condition \(p>d^2\). The last term corrects the double count of the square root.

For sufficiently large \(x\), choose \(Q=\lfloor\sqrt x/(\log x)^4\rfloor\). This tends to infinity and is at most \(Y\). For the terms \(d\le Q\), the trivial estimate \(\pi(d^2;d,1)\le d+1\) gives a total \(O(Q^2)\). The square correction is \(O(\sqrt x)\). For the terms \(Q<d\le Y\), Lemma 5.1, applied at \(t=x\), gives

\[
\begin{aligned}
\sum_{Q<d\le Y}\pi(x;d,1)
&\ll\frac{x}{\log x}\sum_{Q<d\le Y}\frac1{\varphi(d)}\\
&\ll\frac{x}{\log x}\bigl(\log(Y/Q)+1\bigr)
\ll\frac{x\log\log(3x)}{\log x}.
\end{aligned}
\tag{5.9}
\]

The second inequality is Lemma 1.1 applied at the two endpoints. Since all differences in (5.8) are nonnegative, these bounds show

\[
\sum_{p\le x}d(p-1)=2\sum_{d\le Q}\pi(x;d,1)
+O\left(Q^2+\sqrt x+\frac{x\log\log(3x)}{\log x}\right).
\tag{5.10}
\]

Corollary 4.1 with \(A=1\) is applicable at this \(Q\); its prime-count error is \(O(x/(\log x)^2)\). Hence

\[
\sum_{d\le Q}\pi(x;d,1)
=\operatorname{li}(x)\sum_{d\le Q}\frac1{\varphi(d)}
+O\left(\frac{x}{(\log x)^2}\right).
\tag{5.11}
\]

Use \(\operatorname{li}(x)=x/\log x+O(x/(\log x)^2)\), which follows by one integration by parts and a split at \(\sqrt x\), together with

\[
\sum_{d\le Q}\frac1{\varphi(d)}=\mathcal C\log Q+O(1),
\qquad
\log Q=\tfrac12\log x-4\log\log x+o(1).
\]

The factor 2 in (5.10) cancels the factor \(1/2\) in \(\log Q\). All other terms have the size allowed in (5.1), proving the asserted normalization and error. \(\square\)

For comparison with the asymptotic, exact divisor enumeration gives:

| \(x\) | \(\sum_{p\le x}d(p-1)\) | Sum divided by \(x\) |
|---:|---:|---:|
| 100 | 160 | 1.60000 |
| 1,000 | 1,804 | 1.80400 |
| 10,000 | 19,069 | 1.90690 |
| 100,000 | 191,593 | 1.91593 |

The limiting constant is \(\mathcal C=1.943596436820759\ldots\). These finite values illustrate the normalization; the proof of the limit is (5.8)–(5.11), not the numerical trend.

## 6. The square-root barrier and Elliott–Halberstam

On GRH, the explicit-formula estimate from *Counting zeros and the explicit formula for character sums over prime powers* gives

\[
E_\psi(x,q)\ll\sqrt x\,\log^2(2qx).
\tag{6.1}
\]

For \(Q\le\sqrt x\), summing this yields \(O(Q\sqrt x\,L^2)\). At \(Q=\sqrt x\), the bound is \(O(xL^2)\), so it provides no negative power of the logarithm. For \(Q=\sqrt x(\log x)^{-A-2}\), it does give \(O_A(x(\log x)^{-A})\). The unconditional proof loses only one additional logarithm in this comparison, using \(B=A+3\).

The comparison concerns error estimates, not a deduction of GRH from an average theorem. Exceptional individual moduli may remain in that average.

**Elliott–Halberstam conjecture.** For every \(A>0\) and every fixed \(0<\varepsilon<1\),

\[
\sum_{q\le x^{1-\varepsilon}}E_\psi(x,q)
\ll_{A,\varepsilon}x(\log x)^{-A}.
\tag{6.2}
\]

This remains a conjecture. It asks for distribution up to every exponent below 1, whereas Bombieri–Vinogradov supplies every exponent below \(1/2\). The individual GRH bound (6.1) alone does not imply (6.2).

To see why the modulus range matters for prime gaps, fix distinct shifts \(h_1,\ldots,h_k\) and nonnegative weights \(w_n\), supported on a finite interval. If

\[
\sum_n w_n\sum_{j=1}^k\mathbf1_{\mathbb P}(n+h_j)
>(m-1)\sum_n w_n,
\tag{6.3}
\]

then some \(n\) with \(w_n>0\) has at least \(m\) prime values among its shifts. Otherwise every inner sum is at most \(m-1\), contradicting (6.3). Thus a suitably evaluated weighted prime sum can produce clusters of primes.

For example, expanding weights of the form

\[
w_n=\left(\sum_{\substack{d\mid\prod_j(n+h_j)\\d\le R}}\lambda_d\right)^2
\]

creates simultaneous divisibility conditions with moduli \([d,e]\le R^2\). Counting prime values among these conditions leads to primes in progressions. A larger range of distribution permits longer divisor sums in such weights. The full argument also needs estimates for their coefficients and an optimization that makes (6.3) positive; the range of distribution by itself is not a prime-gap theorem.

For historical context, Zhang proved in 2013 that bounded gaps between primes recur infinitely often, by obtaining a stronger distribution estimate for restricted moduli; the Polymath project's *New equidistribution estimates of Zhang type* describes his argument in its introduction and proves a strengthened form of the estimate as its Theorem 1.1. Maynard's *Small gaps between primes*, Theorems 1.1 and 1.3, establishes bounded clusters of any fixed number of primes using a different sieve argument with Bombieri–Vinogradov; its Theorem 1.4 explains the further improvement under Elliott–Halberstam. These prime-gap results are mentioned here as applications beyond this lesson, and are not inputs to any proof above. [The Polymath paper](https://arxiv.org/pdf/1402.0811v3), [Maynard's paper](https://arxiv.org/pdf/1311.4600v3).

## 7. Exercises

1. **Easy.** Fix \(0<\varepsilon<1/2\). Show that, outside \(o(x^{1/2-\varepsilon})\) moduli \(q\le x^{1/2-\varepsilon}\), the asymptotic
   \(\pi(x;q,b)\sim\operatorname{li}(x)/\varphi(q)\) holds uniformly for all reduced classes \(b\).
2. **Medium.** Deduce the theta and prime-count versions from the theorem for \(\psi\). Retain the maximum over the cutoff, and obtain the additional factor \(1/\log x\) for prime counts.
3. **Medium.** Assuming GRH, prove the \(\psi\) theorem with \(Q=\sqrt x(\log x)^{-A-2}\). Give the corresponding prime-count saving.
4. **Hard.** Prove the Titchmarsh divisor asymptotic, including its constant. Explain why a modulus cutoff consisting only of a fixed power of \(\log x\) would not suffice for the main term.

## 8. Solutions

**Solution 1.** Put \(X=x^{1/2-\varepsilon}\), and declare a modulus exceptional when the maximum relative error at \(x\) exceeds \(1/\log x\). With \(A=4\), Corollary 4.1 bounds the sum of the absolute prime-count errors by \(O(x/(\log x)^5)\); its allowable cutoff is \(\sqrt x/(\log x)^7\), which exceeds \(X\) for sufficiently large \(x\). Since \(\varphi(q)\le X\) and \(\operatorname{li}(x)\ge c x/\log x\) eventually, every exceptional modulus contributes at least \(c x/[X(\log x)^2]\). Hence there are \(O(X/(\log x)^3)=o(X)\) of them. For all other moduli the relative error is at most \(1/\log x\), simultaneously for every reduced class. This proves the required uniform asymptotic. If \(\varepsilon\ge1/2\), the modulus range is bounded or empty and the fixed-modulus prime theorem gives the corresponding assertion.

**Solution 2.** The exact difference \(\psi(y;q,b)-\theta(y;q,b)\) consists of proper prime powers in that class. Its weight is at most the global \(O(\sqrt x)\) proved in Corollary 4.1, independently of \(y\). Thus the sum of maximal theta errors differs by at most \(O(Q\sqrt x)\), which is absorbed by the asserted bound.

For prime counts set \(z=\sqrt x\). Below \(z\), global Chebyshev bounds give an error \(O(\sqrt x/\log x)\). Above \(z\), apply the exact formula (4.4), and use \(E_\theta(x,q)\) as the common majorant for all its upper-interval errors. The denominators and the integral each supply a factor \(O(1/\log x)\). This proves (4.3) with the maximum still inside the modulus sum. It follows that

\[
\sum_{q\le Q}E_\pi(x,q)
\ll\frac1{\log x}\left(\sum_{q\le Q}E_\theta(x,q)+Q\sqrt x\right).
\]

At the cutoff \(Q=\sqrt x(\log x)^{-A-3}\), the right side is \(O_A(x(\log x)^{-A-1})\). Monotonicity gives the same result at every smaller cutoff. A bounded initial range of \(x\) changes only the constant.

**Solution 3.** The GRH character estimate, including the subtracted principal main term, is
\(|\psi'(y,\chi)|\ll\sqrt y\,\log^2(2qy)\) for \(y\ge2\). Average it in (1.6). Division by \(\varphi(q)\) cancels the number of characters, so for \(q\le\sqrt x\) the maximal progression error is \(O(\sqrt x\,L^2)\). Cutoffs below 2 contribute at most an absolute constant. Therefore

\[
\sum_{q\le Q}E_\psi(x,q)\ll Q\sqrt x\,L^2
\ll_A x(\log x)^{-A}
\]

at \(Q=\sqrt x(\log x)^{-A-2}\). The prime-power argument gives the same theta bound. Then (4.3) gives \(E_\pi(x,q)\ll\sqrt x\,L\) and, at the same cutoff, a total \(O_A(x(\log x)^{-A-1})\). This uses the individual GRH estimate; it does not prove a larger power range.

**Solution 4.** The divisor pairing gives (5.8) exactly. Choose \(Q=\lfloor\sqrt x/(\log x)^4\rfloor\). The lower-end subtraction for \(d\le Q\) is \(O(Q^2)\), and the square correction is \(O(\sqrt x)\). For \(Q<d\le\sqrt{x-1}\), Lemma 5.1 and Lemma 1.1 give a total \(O(x\log\log(3x)/\log x)\), because \(\log(\sqrt x/Q)=O(\log\log x)\). Bombieri–Vinogradov then evaluates the small-divisor term as \(2\operatorname{li}(x)(\mathcal C\log Q+O(1))+O(x/(\log x)^2)\). Using \(\log Q=\frac12\log x-4\log\log x+o(1)\) and \(\operatorname{li}(x)=x/\log x+O(x/(\log x)^2)\) gives (5.1).

For the constant, the exact identity (1.4) makes \(\mathcal C=\sum_d\mu^2(d)/(d\varphi(d))\), and its absolutely convergent Euler product is (1.1). Thus there is no extra factor 2 in the final answer. If instead \(Q=(\log x)^C\), then the evaluated small-divisor contribution would be only \(O(x\log\log x/\log x)=o(x)\); the remaining divisor range would contain the main term. Siegel–Walfisz alone therefore cannot close this argument.

## 9. Proof scope and references

The maximal primitive-character first moment, both complementary Type I/II estimates, the conductor reduction including its principal term, Bombieri–Vinogradov with \(B(A)=A+3\), both prime versions, the three squared-maximum corollaries, the exceptional-set assertion and the Titchmarsh divisor asymptotic are proved here. The inputs from preceding lessons are their proved character identities, primitive Pólya–Vinogradov estimate, multiplicative maximal bilinear inequality, Siegel–Walfisz estimates for both \(\Lambda\) and \(\mu\), Chebyshev bounds, Mertens estimate and arithmetic sieve inequality.

The Elliott–Halberstam conjecture is unproved. The bounded-gap results mentioned for context in Section 6, Zhang's theorem and Maynard's Theorems 1.1, 1.3 and 1.4, are not proved here. Neither replaces a proof step in this lesson.

- D. Koukoulopoulos, [*The Distribution of Prime Numbers*](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf), AMS, 2019, author's preliminary version, Chapter 26, Lemma 26.1, Theorems 26.2, 26.4 and 26.6, and Corollary 26.7: the direct progression organization and its complementary small-conductor estimate.
- D. H. J. Polymath, [*New equidistribution estimates of Zhang type*](https://arxiv.org/pdf/1402.0811v3), arXiv:1402.0811v3, 2014, introduction and Theorem 1.1: Zhang's bounded-gap theorem and a strengthened form of his restricted-modulus distribution estimate.
- J. Maynard, [*Small gaps between primes*](https://arxiv.org/pdf/1311.4600v3), arXiv:1311.4600v3; Annals of Mathematics 181 (2015), 383–413, introduction and Theorems 1.1, 1.3 and 1.4: the prime-cluster context and the role of Elliott–Halberstam.
