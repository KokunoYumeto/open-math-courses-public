# Divisibility of the multiplicative order

*Written by Claude Opus 5.5 (Anthropic) on 23 October 2026. The question was posed by Claude while writing this course and solved by GPT-6 Astra (OpenAI) in ChatGPT's Pro mode; the solution was refereed by Claude Opus 5.5 in a separate session, and this lesson was written from it and refereed and revised by Claude Opus 5.5 in two further sessions. Public domain (CC0).*

This lesson proves two unconditional results on the order of an integer \(a\) with \(|a|>1\) modulo primes. First, for every \(k\ge1\), at least \(x/(2k|a|^{8k}\log x)\) primes \(p\in(x,2x]\) satisfy \(k\mid\operatorname{ord}_p(a)\), once \(x\) is large. Second, every residue class of \(\operatorname{ord}_p(a)\) modulo \(d\) contains infinitely many primes, with an explicit logarithmic lower bound.

The first result reduces to one Frobenius condition in a fixed mixed cyclotomic–Kummer field. A primitive-divisor theorem supplies a witness prime for that condition. Prime-power levels \(K_{\ell^s}\) then control the whole \(\ell\)-part of the index at once.

**Prerequisites.** [*Artin's conjecture and the index of a prime*](artins-conjecture-and-the-index-of-a-prime.md), Section 1 and Lemma 3.1; [*Hilbert's ramification theory in Galois extensions*](course:NT-ANT/hilberts-ramification-theory-in-galois-extensions), Theorem 6.2 and Proposition 6.3; [*Perfect powers: primitive divisors, Catalan and Pillai*](course:TR-BAKER/TR-BAKER-16), Theorem 16.6; [*The Chebotarev density theorem*](course:NT-CFT/the-chebotarev-density-theorem), Theorem 22.4.

## 1. Primitive prime divisors and the sign of the base

Fix \(a\in\mathbb Z\) with \(A=|a|>1\). For \(p\nmid a\) let \(i_p(a)=(p-1)/\operatorname{ord}_p(a)\) be the index. For \(n\ge1\) put \(E_n=\mathbb Q(\mu_n)\) and \(K_n=E_n(\alpha)\) with \(\alpha^n=a\). The field \(K_n\) does not depend on the choice of \(\alpha\), since two choices differ by an element of \(\mu_n\subset E_n\).

**Theorem BV** (Birkhoff and Vandiver [BV, Theorem V]). Let \(u>v\ge1\) be coprime integers and \(N>2\), with \((u,v,N)\ne(2,1,6)\). Then \(u^N-v^N\) has a prime factor that divides no \(u^j-v^j\) with \(j\) a proper divisor of \(N\).

This is the case \(n=N>2\) of Theorem 16.6 of [*Perfect powers: primitive divisors, Catalan and Pillai*](course:TR-BAKER/TR-BAKER-16), which gives a prime that divides \(u^N-v^N\) and none of the numbers \(u^j-v^j\) with \(1\le j<N\).

**Lemma 1.1.** Let \(N\ge3\) with \(N\ne6\). There is a prime \(p\) with
\[
\begin{gathered}\operatorname{ord}_p(A)=N,\qquad p\nmid a,\\ p\equiv1\pmod N,\\ N+1\le p<A^N.\end{gathered}
\]

*Proof.* Apply BV with \((u,v)=(A,1)\), and let \(p\) be the prime it supplies. Then \(p\mid A^N-1\), so \(p\nmid A\), and \(\operatorname{ord}_p(A)\) divides \(N\). A proper divisor \(j\) as the order would give \(p\mid A^j-1\), which BV excludes. So the order is \(N\). It divides \(p-1\), which gives \(p\ge N+1\). Finally \(p\le A^N-1\). \(\square\)

**Lemma 1.2.** Let \(p\) be an odd prime and let \(A\in\mathbb F_p^\times\) have order \(E\). The order of \(-A\) is \(2E\) if \(E\) is odd, \(E/2\) if \(E\equiv2\pmod4\), and \(E\) if \(4\mid E\).

*Proof.* Let \(o\) be the order of \(-A\).

If \(E\) is odd, then \((-A)^2=A^2\) has order \(E\), so \(E\mid o\). Also \(o\mid2E\), and \((-A)^E=-1\ne1\). Hence \(o=2E\).

If \(E\) is even, then \(A^{E/2}\) has order \(2\). The only such element of the cyclic group \(\mathbb F_p^\times\) is \(-1\), so \(-A=A^{E/2+1}\) and \(o=E/\gcd(E,E/2+1)\). The gcd divides \(2(E/2+1)-E=2\). It equals \(2\) if \(E\equiv2\pmod4\) and \(1\) if \(4\mid E\). \(\square\)

**Corollary 1.3.** For every \(k\ge1\) there is a prime \(p_0\) with \(\operatorname{ord}_{p_0}(a)=4k\). Every such prime satisfies \(p_0\nmid ak\), \(4k\mid p_0-1\) and \(p_0\le A^{4k}-1\).

*Proof.* Lemma 1.1 with \(N=4k\) gives \(p_0>4k\) with \(\operatorname{ord}_{p_0}(A)=4k\). In particular \(p_0\) is odd and \(p_0\nmid k\). For \(a<0\), Lemma 1.2 with \(4\mid E\) gives \(\operatorname{ord}_{p_0}(-A)=4k\). The other claims follow from \(p_0\mid A^{4k}-1\) and \(\operatorname{ord}_{p_0}(a)\mid p_0-1\). \(\square\)

Throughout, \(p_0\) is the least prime with \(\operatorname{ord}_{p_0}(a)=4k\). It depends only on \(a\) and \(k\).

## 2. A Frobenius witness in a fixed field

For each prime \(\ell\mid k\) put \(e_\ell=v_\ell(k)\), \(t_\ell=v_\ell(p_0-1)\) and \(s_\ell=t_\ell-e_\ell+1\). Since \(4k\mid p_0-1\), we have \(1\le s_\ell\le t_\ell\). Define
\[
\begin{gathered}
R=\prod_{\ell\mid k}\ell^{t_\ell},\qquad H=\prod_{\ell\mid k}\ell^{t_\ell+1},\\
E=\mathbb Q(\zeta_H,\beta),\qquad\beta^R=a,
\end{gathered}
\]
with empty products equal to \(1\). Since \(R\mid H\), the field \(E\) contains all roots \(\zeta_H^{jH/R}\beta\) of \(X^R-a\). So \(E\) is the splitting field of \((X^H-1)(X^R-a)\), and it is Galois over \(\mathbb Q\). Put \(G=\operatorname{Gal}(E/\mathbb Q)\).

The field \(E\) contains \(E_H\). For each \(\ell\mid k\) it also contains \(K_{\ell^{s_\ell}}\), which is generated by \(\zeta_H^{H/\ell^{s_\ell}}\) and by the root \(\beta^{R/\ell^{s_\ell}}\) of \(X^{\ell^{s_\ell}}-a\).

**Lemma 2.1.** Every prime \(p\nmid aH\) is unramified in \(E\). Let \(\mathfrak P\) be a prime of \(E\) above such a \(p\), and let \(\sigma\in G\) be its Frobenius (Proposition 6.3 of the ramification lesson). Then \(\sigma(\zeta_H)=\zeta_H^p\). For every Galois subfield \(K'\subseteq E\), the restriction \(\sigma|_{K'}\) is the Frobenius of \(\mathfrak P\cap K'\).

*Proof.* The roots of \(X^H-1\) and of \(X^R-a\) are algebraic integers that generate \(E\). The discriminants of these polynomials are \(\pm H^H\) and \(\pm R^Ra^{R-1}\), and both are prime to \(p\). So each set of roots has distinct reductions modulo \(\mathfrak P\).

An inertia element acts trivially on the residue field (Theorem 6.2 there) and permutes each set of roots. It therefore fixes every root, and so it is the identity. Hence \(p\) is unramified.

Since \(\sigma(\zeta_H)\) and \(\zeta_H^p\) lie in \(\mu_H\) and are congruent modulo \(\mathfrak P\), they are equal. The congruence \(\sigma(t)\equiv t^p\) restricts to the integers of \(K'\), which gives the last claim. \(\square\)

The Frobenius elements at the primes above \(p\) form a conjugacy class \(\operatorname{Frob}_p\) of \(G\).

**Lemma 2.2.** Let \(n\ge1\) and let \(p\nmid an\) be a prime. Then \(p\) is unramified in \(K_n\), and its Frobenius there is trivial exactly when \(n\mid i_p(a)\).

*Proof.* The argument of Lemma 2.1, applied to \(X^n-a\) with discriminant \(\pm n^na^{n-1}\), gives unramifiedness and \(\sigma(\zeta_n)=\zeta_n^p\). So \(\sigma\) fixes \(E_n\) exactly when \(p\equiv1\pmod n\).

Assume \(p\equiv1\pmod n\). Then \(\sigma(\alpha)/\alpha\in\mu_n\) and
\[
\frac{\sigma(\alpha)}\alpha\equiv\alpha^{p-1}=a^{(p-1)/n}\pmod{\mathfrak P}.
\]
Reduction is injective on \(\mu_n\), so \(\sigma(\alpha)=\alpha\) exactly when \(a^{(p-1)/n}\equiv1\pmod p\). In the cyclic group \(\mathbb F_p^\times\), the conditions \(n\mid p-1\) and \(a^{(p-1)/n}\equiv1\) together mean \(\operatorname{ord}_p(a)\mid(p-1)/n\), that is, \(n\mid i_p(a)\). \(\square\)

**Proposition 2.3.** Let \(C=\operatorname{Frob}_{p_0}\subseteq G\). Every prime \(p\nmid aH\) with \(\operatorname{Frob}_p=C\) satisfies \(k\mid\operatorname{ord}_p(a)\). Moreover
\[
[E:\mathbb Q]\le\varphi(\operatorname{rad}k)R^2<kA^{8k}.
\]

*Proof.* Every prime factor of \(H\) divides \(k\), and \(p_0\nmid ak\). So \(p_0\nmid aH\) and \(C\) is defined. Let \(\sigma_0\in C\), and let the Frobenius \(\sigma\) of \(p\) at some prime above it be \(\tau\sigma_0\tau^{-1}\).

The group \(\operatorname{Gal}(E_H/\mathbb Q)\) is abelian, since its elements \(\zeta_H\mapsto\zeta_H^u\) commute. Hence \(\sigma|_{E_H}=\sigma_0|_{E_H}\). Lemma 2.1 then gives \(p\equiv p_0\pmod H\). Since \(\ell^{t_\ell+1}\mid H\) and \(v_\ell(p_0-1)=t_\ell\), we get \(v_\ell(p-1)=t_\ell\) for each \(\ell\mid k\).

At \(p_0\), \(v_\ell(i_{p_0}(a))=t_\ell-v_\ell(4k)\le s_\ell-1\). By Lemmas 2.2 and 2.1, \(\sigma_0|_{K_{\ell^{s_\ell}}}\ne1\). Restriction to this Galois subfield is a homomorphism, so \(\sigma|_{K_{\ell^{s_\ell}}}\) is a conjugate of a nontrivial element and is nontrivial. Lemma 2.2 at \(p\) gives \(\ell^{s_\ell}\nmid i_p(a)\), and hence
\[
\begin{aligned}
v_\ell(\operatorname{ord}_p(a))&=t_\ell-v_\ell(i_p(a))\\
&\ge t_\ell-s_\ell+1=e_\ell .
\end{aligned}
\]
This holds for every \(\ell\mid k\), so \(k\mid\operatorname{ord}_p(a)\).

For the degree, \([E:\mathbb Q]\le\varphi(H)R=\varphi(\operatorname{rad}k)R^2\). The integer \(R\) divides \(p_0-1\le A^{4k}-2\), and \(\varphi(\operatorname{rad}k)\le k\). \(\square\)

## 3. The count in dyadic intervals

**Theorem Ch** (Chebotarev, Dirichlet-density form; Theorem 22.4 of [*The Chebotarev density theorem*](course:NT-CFT/the-chebotarev-density-theorem), also [Milne, Theorem 8.31]). Let \(E/\mathbb Q\) be finite Galois with group \(G\) and \(C\) a conjugacy class. The unramified primes with \(\operatorname{Frob}_p=C\) have Dirichlet density \(|C|/|G|\).

**Named result N8** (Wiertelak, as stated by Moree [M05, Theorem 1]). For fixed rational \(g\notin\{-1,0,1\}\) and fixed \(k\ge1\),
\[
\begin{aligned}
&\#\{p\le X:k\mid\operatorname{ord}_p(g)\}=\delta_g(k)\operatorname{Li}(X)\\
&\quad+O_{g,k}\Bigl(\frac{X(\log\log X)^{\omega(k)+1}}{\log^3X}\Bigr),
\end{aligned}
\]
with \(\delta_g(k)\) a positive rational number. Primes dividing the numerator or denominator of \(g\) are excluded from the count.

**Theorem 3.1.** For every integer \(a\) with \(A=|a|>1\) and every \(k\ge1\), there is \(X_0(a,k)\) such that for \(x\ge X_0(a,k)\), with \(L=\log x\),
\[
\begin{aligned}
&\#\{x<p\le2x:p\nmid a,\ k\mid\operatorname{ord}_p(a)\}\\
&\qquad\ge\frac{x}{2kA^{8k}L}.
\end{aligned}
\]

*Proof.* Let \(T\) be the set of primes counted in N8, with \(g=a\). By N8, \(\pi_T(X)=\delta\pi(X)+o(\pi(X))\) with \(\delta=\delta_a(k)\). Partial summation then gives \(\sum_{p\in T}p^{-s}\sim\delta\sum_pp^{-s}\) as \(s\to1^+\), so \(T\) has Dirichlet density \(\delta\).

By Proposition 2.3, the primes \(p\nmid aH\) with \(\operatorname{Frob}_p=C\) lie in \(T\). Removing finitely many primes does not change a Dirichlet density. So Ch gives
\[
\delta\ge\frac{|C|}{|G|}\ge\frac1{[E:\mathbb Q]}>\frac1{kA^{8k}}.
\]

Subtracting N8 at \(2x\) and at \(x\), and using \(\operatorname{Li}(2x)-\operatorname{Li}(x)\ge x/\log(2x)\), the count is at least \((\delta-o(1))\,x/(L+\log2)\). For large \(x\) this exceeds \(\delta x/(2L)\). The threshold depends only on \(a\) and \(k\). \(\square\)

## 4. Every residue class of the order

**Theorem 4.1.** Fix integers \(d\ge1\) and \(r\). Put \(\lambda=1\) if \(a>0\) and \(\lambda=2\) if \(a<0\). For every \(x\ge2\),
\[
\begin{aligned}
&\#\{p\le x\mid p\nmid a,\ \operatorname{ord}_p(a)\equiv r\ (d)\}\\
&\qquad\ge\frac{\log x}{\lambda d\log A}-\frac{16}d-1 .
\end{aligned}
\]

*Proof.* For \(N\ge16\) define \(E(N)\) as follows: \(E(N)=N\) if \(a>0\) or \(4\mid N\); \(E(N)=2N\) if \(a<0\) and \(N\) is odd; \(E(N)=N/2\) if \(a<0\) and \(N\equiv2\pmod4\). In every case \(8\le E(N)\le\lambda N\).

Lemma 1.1 gives a prime \(p_N\) with \(\operatorname{ord}_{p_N}(A)=E(N)\) and \(p_N<A^{E(N)}\le A^{\lambda N}\). This prime is odd, since \(p_N\ge9\). By Lemma 1.2, \(\operatorname{ord}_{p_N}(a)=N\) for both signs of \(a\). Distinct \(N\) therefore give distinct primes.

Put \(T=\log x/(\lambda\log A)\). Each \(N\equiv r\pmod d\) with \(16\le N\le T\) gives a counted prime \(p_N<A^{\lambda T}=x\). There are at least \((T-16)/d-1\) such \(N\). If \(T<16\), the right side is negative and the bound holds trivially. \(\square\)

This bound counts primes up to \(x\). It gives no lower bound of order \(x/(\log x)^2\) in dyadic intervals for a general residue class.

## 5. Exercises

**5.1.** Show that no prime \(p\) has \(\operatorname{ord}_p(2)=6\), so that the exception in BV is necessary.

**5.2.** For \(a=2\) and \(k=3\), find \(p_0\), \(R\), \(H\) and \(E\), and give congruence conditions satisfied by the primes of Proposition 2.3.

**5.3.** Check Lemma 1.2 for \(p=13\) and \(A=2\).

## 6. Solutions

**5.1.** Such a prime divides \(63=3^2\cdot7\). But \(\operatorname{ord}_3(2)=2\) and \(\operatorname{ord}_7(2)=3\).

**5.2.** We have \(2^{12}-1=3^2\cdot5\cdot7\cdot13\), with \(\operatorname{ord}_3(2)=2\), \(\operatorname{ord}_5(2)=4\) and \(\operatorname{ord}_7(2)=3\). Also \(2^6\equiv-1\) and \(2^4\equiv3\pmod{13}\), so \(\operatorname{ord}_{13}(2)=12\) and \(p_0=13\).

Then \(t_3=e_3=s_3=1\), so \(R=3\), \(H=9\) and \(E=\mathbb Q(\zeta_9,2^{1/3})\). The primes of Proposition 2.3 satisfy \(p\equiv4\pmod9\). Their Frobenius in \(K_3\) is nontrivial, so by Lemma 2.2 the integer \(2\) is not a cube modulo \(p\). Hence \(3\nmid i_p(2)\), \(v_3(p-1)=1\) and \(3\mid\operatorname{ord}_p(2)\).

**5.3.** We have \(-2\equiv11\pmod{13}\), with \(11^2\equiv4\), \(11^3\equiv5\), \(11^4\equiv3\) and \(11^6\equiv-1\). So the order of \(11\) is \(12=E\), as Lemma 1.2 predicts for \(4\mid E\).

## Sources

- [BV] G. D. Birkhoff and H. S. Vandiver, *On the integral divisors of \(a^n-b^n\)*, Annals of Mathematics (2) 5 (1904), 173–180, Theorem V. https://nonagon.org/ExLibris/sites/default/files/pdf/Integral-Divisors-Birkhoff-Vandiver-1904.pdf
- [Milne] J. S. Milne, *Algebraic Number Theory*, version 3.08 (2020), Theorem 8.31. https://www.jmilne.org/math/CourseNotes/ANT.pdf
- [M05] P. Moree, *On primes \(p\) for which \(d\) divides \(\operatorname{ord}_p(g)\)*, Functiones et Approximatio 33 (2005), 85–95, Theorem 1. https://arxiv.org/abs/math/0407421
- The main argument follows a solution produced with ChatGPT (OpenAI) in October 2026 and is completed here.
