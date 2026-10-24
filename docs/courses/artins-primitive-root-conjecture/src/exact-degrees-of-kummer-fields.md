# Exact degrees of Kummer fields

*Written by Claude Opus 5.5 (Anthropic) on 23 October 2026. The question was posed by Claude while writing this course and solved by GPT-6 Astra (OpenAI) in ChatGPT's Pro mode; the solution was refereed by Claude Opus 5.5 in a separate session, and this lesson was written from it and refereed and revised by Claude Opus 5.5 in two further sessions. Public domain (CC0).*

This lesson computes \([K_n:\mathbb Q]\) exactly for \(K_n=\mathbb Q(\mu_n,a^{1/n})\), for every rational \(a\notin\{-1,0,1\}\). It then bounds the discriminant of \(K_n\) and proves the uniform splitting bound for every level \(n\).

The answer is governed by three quantities:
- \(h\), the largest exponent with \(|a|=b^h\) for a positive rational \(b\);
- \(g=(n,h)\);
- \(D\), the discriminant of \(\mathbb Q(\sqrt b)\).

**Prerequisites.**
- [*Uniform complete splitting in Kummer fields*](uniform-complete-splitting-in-kummer-fields.md), Lemmas 1.1 and 3.1.
- [*The zero-free strip*](the-zero-free-strip.md), Corollary 4.2.
- [*The different and the discriminant*](course:NT-ANT/the-different-and-the-discriminant), Proposition 14.2 and Theorem 14.3.
- [*Artin L-functions, conductors and discriminants*](course:NT-CFT/artin-l-functions-conductors-and-discriminants), Proposition 21.1 and Theorem 21.2.

## 1. Cyclotomic fields

Write \(E_N=\mathbb Q(\zeta_N)\) with \(\zeta_N=e^{2\pi i/N}\).

**Lemma 1.1.** For \(N,M\ge1\), with \(\ell=\operatorname{lcm}(N,M)\):
1. \([E_N:\mathbb Q]=\varphi(N)\);
2. \(E_NE_M=E_\ell\);
3. \(E_N\cap E_M=E_{\gcd(N,M)}\);
4. \(D_{E_N}\mid N^{\varphi(N)}\).

*Proof.* *Item 1.* Let \(f\) be the minimal polynomial of \(\zeta_N\) and let \(q\nmid N\) be prime. Suppose \(\zeta_N^q\) were a root of another irreducible factor \(f_1\) of \(X^N-1\) in \(\mathbb Z[X]\). Then \(f\mid f_1(X^q)\equiv f_1^q\pmod q\), so \(X^N-1\) would have a repeated factor modulo \(q\). This contradicts \(\gcd(X^N-1,NX^{N-1})=1\) in \(\mathbb F_q[X]\). Iterating over primes, every \(\zeta_N^k\) with \((k,N)=1\) is a root of \(f\).

*Item 2.* Since \((\ell/N,\ell/M)=1\), Bézout writes \(\zeta_\ell\) as a product of powers of \(\zeta_N\) and \(\zeta_M\).

*Item 3.* Restriction \(\operatorname{Gal}(E_\ell/E_M)\to\operatorname{Gal}(E_N/E_N\cap E_M)\) is injective, because \(E_N\) and \(E_M\) generate \(E_\ell\). The fixed field of its image is \(E_N\cap E_M\), so it is onto. Hence \([E_N\cap E_M:\mathbb Q]=\) \(\varphi(N)\varphi(M)/\varphi(\ell)=\) \(\varphi(\gcd(N,M))\), and \(E_{\gcd(N,M)}\) lies in both fields with this degree.

*Item 4.* Write \(X^N-1=f(X)G(X)\). Then \(N\zeta_N^{N-1}=f'(\zeta_N)G(\zeta_N)\). Taking norms, \(N^{\varphi(N)}\) is divisible by \(N(f'(\zeta_N))\), and \((-1)^{\varphi(N)(\varphi(N)-1)/2}N(f'(\zeta_N))\) is the discriminant of \(\mathbb Z[\zeta_N]=\mathbb Z[X]/(f)\), \(f\) being monic of degree \(\varphi(N)\). The field discriminant divides it. \(\square\)

By Proposition 14.2 of *The different and the discriminant*, \(E_N\) is unramified outside \(N\).

**Lemma 1.2.** For an odd prime \(\ell\), put \(\ell^*=(-1)^{(\ell-1)/2}\ell\). Then \(\sqrt{\ell^*}\in E_\ell\), \(i\in E_4\) and \(\sqrt{\pm2}\in E_8\).

*Proof.* Let \(\tau=\sum_x(\frac x\ell)\zeta_\ell^x\). Substituting \(y=xt\),
\[
\tau^2=\sum_{t\ne0}\Bigl(\frac t\ell\Bigr)\sum_{x\ne0}\zeta_\ell^{x(1+t)}.
\]
The inner sum is \(\ell-1\) at \(t=-1\) and \(-1\) otherwise. Hence \(\tau^2=(\frac{-1}\ell)\ell=\ell^*\). For the rest, \((\zeta_8+\zeta_8^{-1})^2=2\) and \(\sqrt{-2}=i\sqrt2\). \(\square\)

For a squarefree \(s\ne1\), put \(\Delta_s=s\) if \(s\equiv1\pmod 4\) and \(\Delta_s=4s\) otherwise.

**Proposition 1.3.** \(\mathbb Q(\sqrt s)\subseteq E_N\) if and only if \(|\Delta_s|\mid N\).

*Proof.* *Sufficiency.* Let \(P=\prod\ell^*\) over the odd primes \(\ell\mid s\). Then \(P\equiv1\pmod 4\), and \(\Delta_s\) equals \(P\), \(-4P\) or \(\pm8P\) according as \(s\equiv1\), \(s\equiv3\pmod 4\), or \(s\) even. In each case Lemma 1.2 gives \(\sqrt{\Delta_s}\in E_{|\Delta_s|}\).

*Necessity, odd primes.* If \(\sqrt s\in E_N\), every odd \(\ell\mid s\) ramifies in \(\mathbb Q(\sqrt s)\), hence in \(E_N\) (ramification indices multiply in towers). So \(\ell\mid N\).

*Necessity, the prime 2.* If \(s\not\equiv1\pmod 4\), then \(2\) ramifies in \(\mathbb Q(\sqrt s)\). If \(v_2(N)\le1\), then \(E_N=E_{N'}\) with \(N'\) odd, which is unramified at \(2\); hence \(4\mid N\).

*Necessity, even \(s=2s'\).* Suppose \(N=4N'\) with \(N'\) odd. Choose \(\epsilon=\pm1\) with \(\epsilon s'\equiv1\pmod 4\). By sufficiency, \(\sqrt{\epsilon s'}\in E_N\). Then \(\sqrt{2\epsilon}\in E_N\cap E_8=E_4=\mathbb Q(i)\). This would make \(-2\epsilon\) a rational square, which it is not. Hence \(8\mid N\). \(\square\)

## 2. Positive radicals

Write \(|a|=\prod\ell^{k_\ell}\), and put \(h=\gcd|k_\ell|\) and \(b=\prod\ell^{k_\ell/h}\). The exponents of \(b\) are coprime, so \(b\ne1\) and \(b\) is not a square. Let \(s\) be the squarefree integer with \(b\in s\mathbb Q^{\times2}\), and put \(D=\Delta_s>0\).

**Lemma 2.1.** Let \(v,w\ge1\) be coprime. If \(b^{w/v}>0\) lies in an abelian extension of \(\mathbb Q\), then \(v\le2\).

*Proof.* *Irreducibility.* Let \(P\) be a monic rational factor of \(X^v-b^w\) of degree \(j\). Its constant term \(B\) satisfies \(|B|^v=b^{wj}\). So \(v\,v_\ell(B)=wj\,v_\ell(b)\) for every \(\ell\), which forces \(v\mid j\). Hence \(X^v-b^w\) is irreducible.

*Reality.* Every subgroup of an abelian group is normal, so \(\mathbb Q(b^{w/v})\) is Galois. It therefore contains all the conjugates \(b^{w/v}\zeta_v^j\). It is real, so \(v\le2\). \(\square\)

**Proposition 2.2.** Let \((u,m)=1\), \(\beta=b^{u/m}\) and \(m\mid N\). Then
\[
\begin{aligned}&[E_N(\beta):E_N]\\&\quad =\begin{cases}m/2,&m\ \text{even and}\ D\mid N,\\ m,&\text{otherwise},\end{cases}\end{aligned}
\]
with minimal polynomial \(X^{m/2}-b^{(u-1)/2}\sqrt b\) or \(X^m-b^u\) respectively.

*Proof.* The map \(\sigma\mapsto\sigma(\beta)/\beta\) is an injective homomorphism into \(\mu_m\). Its image is \(\mu_e\) with \(e=[E_N(\beta):E_N]\), so \(\beta^e\in E_N\). The exponent \(ue/m\) has reduced denominator \(m/e\), so Lemma 2.1 gives \(m/e\le2\).

If \(e=m/2\), then \(u\) is odd and \(\beta^{m/2}=b^{(u-1)/2}\sqrt b\), so \(\sqrt b\in E_N\). Conversely, \(\sqrt b\in E_N\) gives \(e\le m/2\). Proposition 1.3 identifies the condition \(\sqrt b\in E_N\) with \(D\mid N\). \(\square\)

## 3. The degree theorem

Put \(K_n=E_n(\alpha)\) with \(\alpha^n=a\), \(e_n=[K_n:E_n]\), \(d_n=\varphi(n)e_n\), \(g=(n,h)\) and \(m=n/g\).

**Theorem 3.1.** For \(a>0\),
\[
e_n=\begin{cases}m/2,&2\mid m,\ D\mid n,\\ m,&\text{otherwise}.\end{cases}
\]
For \(a<0\),
\[
\begin{aligned}&e_n\\&\quad =\begin{cases}
m,&n\ \text{odd},\\
2m,&n\ \text{even},\ m\ \text{odd},\\
m/2,&4\mid m,\ D\mid n,\\
m/2,&m\equiv2\ (4),\ D\mid2n,\ D\nmid n,\\
m,&\text{otherwise}.
\end{cases}\end{aligned}
\]
In all cases \(n\varphi(n)/(2h)\le d_n\le n\varphi(n)\).

*Proof.* Put \(u=h/g\) and \(\beta=b^{u/m}\), so \(\beta^n=|a|\).

*Case \(a>0\).* Here \(K_n=E_n(\beta)\), and Proposition 2.2 applies.

*Case \(a<0\), \(n\) odd.* Then \((-\beta)^n=a\) and \(m\) is odd, so Proposition 2.2 gives \(e_n=m\).

*Case \(a<0\), \(n\) even: setup.* Put \(F=E_n\), \(F'=E_{2n}\), \(\alpha=\zeta_{2n}\beta\), \(K=F(\alpha)\) and \(T=F'(\beta)=KF'\). Let \(\tau\) be the generator of \(\operatorname{Gal}(F'/F)\), so \(\tau(\zeta_{2n})=-\zeta_{2n}\). Restriction \(\operatorname{Gal}(T/K)\to\operatorname{Gal}(F'/F)\) is injective.

*Criterion.* \([T:K]=2\) exactly when some automorphism \(t\) of \(T\) extends \(\tau\) with \(t(\beta)=-\beta\). Such \(t\) fix \(\alpha\), and they are exactly the nontrivial elements of \(\operatorname{Gal}(T/K)\). Let \(P\) be the minimal polynomial of \(\beta\) over \(F'\). Such a \(t\) exists exactly when \(\tau(P)(-\beta)=0\): the map \(\sum c_jX^j\mapsto\sum\tau(c_j)(-\beta)^j\) then factors through \(F'[X]/(P)\cong T\), and an injective \(\mathbb Q\)-linear endomorphism of \(T\) is bijective. Finally \(e_n=2[T:F']/[T:K]\).

*Case \(a<0\), \(n\) even: computation.* Apply Proposition 2.2 with \(N=2n\).
- If \(m\) is odd, then \(\tau(P)(-\beta)=-2b^u\ne0\), so \(e_n=2m\).
- If \(m\) is even and \(D\nmid 2n\), then \(\tau(P)(-\beta)=0\), so \(e_n=m\).
- If \(m\) is even and \(D\mid 2n\), then
\[
\begin{aligned}&\tau(P)(-\beta) =b^{(u-1)/2}\\ &\quad \quad\times\bigl((-1)^{m/2}\sqrt b-\tau(\sqrt b)\bigr).\end{aligned}
\]
Here \(\tau(\sqrt b)=\sqrt b\) exactly when \(D\mid n\). So the expression vanishes in the two halving cases, which give \(e_n=m/2\), and \(e_n=m\) otherwise.

*The bounds.* We have \(e_n\ge m/2\ge n/(2h)\). Also \(e_n\le n\), since \(\alpha\) is a root of \(X^n-a\). \(\square\)

**Corollary 3.2.** If \(h=1\), then \(d_n=n\varphi(n)/\epsilon_a(n)\), where \(\epsilon_a(n)=2\) exactly when \(2\mid n\) and \(|\Delta_a|\mid n\), and \(\epsilon_a(n)=1\) otherwise.

*Proof.* Here \(m=n\). For \(a>0\), \(\Delta_a=D\) and the claim is Theorem 3.1. For \(a<0\), \(\Delta_a=\Delta_{-s}\).
- If \(4\mid n\): for even \(s\) both discriminants are \(\pm8s'\cdot\)… that is, both equal \(\pm4s\); for odd \(s\) each is \(\pm s\) or \(\pm4s\), and \(s\mid n\iff 4s\mid n\). So \(D\mid n\iff|\Delta_{-s}|\mid n\).
- If \(n\equiv2\pmod 4\): Theorem 3.1 halves exactly when \(D=4s\) with \(s\equiv3\pmod 4\) and \(s\mid n\). That is the condition \(|\Delta_{-s}|=s\mid n\). In the other cases \(4\mid\Delta_{-s}\), so \(\Delta_{-s}\nmid n\). \(\square\)

The parity condition cannot be dropped: for \(a=5\), \(n=5\), we have \(D=5\mid n\), yet \(d_5=20\).

The hypothesis \(h=1\) is stronger than "\(a\) is not a perfect power". For \(a=-4\) we have \(h=2\), \(b=2\), \(D=8\), and Theorem 3.1 gives \(e_n=n/4\) for every \(4\mid n\), so no factor \(\epsilon_a(n)\in\{1,2\}\) works. For instance \((1+i)^4=-4\), so \(K_4=\mathbb Q(i)\). Yet \(-4\) is not \(c^j\) with \(j\ge2\): \(j\) would have to be odd and divide \(2\).

## 4. Discriminants and complete splitting

**Theorem 4.1.** Let \(a\in\mathbb Z\) with \(A=|a|>1\). Then
\[
\log D_{K_n}\le d_n(2\log n+\log A).
\]
For \(a=r/t\) in lowest terms with \(t>1\), the same holds with \(A\) replaced by \(\min(|r|t^{n-1},t|r|^{n-1})\).

*Proof.* *The relative discriminant.* As in Proposition 2.2, \(\alpha\) has minimal polynomial \(X^{e}-c\) over \(E_n\), where \(e=e_n\) and \(c=\alpha^{e}\) is integral. Every conjugate of \(c\) has absolute value \(A^{e/n}\). The argument in the proof of Lemma 1.1 of Lesson 15 (Euler's lemma and the different) shows that the relative discriminant divides \(e^ec^{e-1}\).

*The tower.* Theorem 14.3 of *The different and the discriminant* gives
\[
\begin{aligned}
\log D_{K_n}&\le e\log D_{E_n}+\varphi(n)e\log e\\
&\quad+\varphi(n)\tfrac{e(e-1)}n\log A .
\end{aligned}
\]
Insert Lemma 1.1(4) and \(e\le n\).

*Rational \(a\).* Since \((t\alpha)^n=rt^{n-1}\) and \((r/\alpha)^n=tr^{n-1}\), the field \(K_n\) is also generated by an \(n\)th root of either integer. \(\square\)

**Theorem 4.2.** Let \(a\in\mathbb Z\) with \(A>1\) and put \(\delta_0=10^{-6}\). There is an absolute constant \(C_*\) such that for all \(n\ge1\) and \(x\ge2\),
\[
\begin{aligned}&\quad \#\{x<p\le2x:\ p\ \text{splits}\\ &\quad \qquad\text{completely in}\ K_n\}\\ &\quad \le\frac{C_*x}{d_n\log x}\\ &\quad \quad +C_*x^{1-\delta_0}\frac{2\log n+\log A+1}{\log x}\\ &\quad +\omega(an).\end{aligned}
\]
Moreover \(1/d_n\le2h/(n\varphi(n))\) and \(h\le\log A/\log2\).

*Proof.* *Descent of the strip.* Put \(F_n=\mathbb Q(\mu_{12n})\) and \(T_n=K_nF_n\).
- \(T_n/F_n\) is cyclic, since \(\sigma\mapsto\sigma(\alpha)/\alpha\) embeds its group in \(\mu_n\).
- \(T_n/K_n\) is abelian, since restriction embeds its group in \(\operatorname{Gal}(F_n/\mathbb Q)\).

Proposition 21.1 and Theorem 21.2 of *Artin L-functions, conductors and discriminants* factor \(\zeta_{T_n}\) into \(L\)-functions of \(F_n\). These have no zero in \(\operatorname{Re}s>1-\delta_0\) by Corollary 4.2 of *The zero-free strip*. They also factor \(\zeta_{T_n}\) as \(\zeta_{K_n}\) times entire \(L\)-functions of \(K_n\). So \(\zeta_{K_n}\) has no zero in that half-plane.

*Counting.* Lemma 3.1 of Lesson 15 applies to \(K_n\). Each split \(p\nmid an\) contributes at least \(d_n\log x\). Theorem 4.1 bounds \(\log D_{K_n}+d_n\). The primes dividing \(an\) are at most \(\omega(an)\) in number.

*The last claims.* The first is Theorem 3.1. For the second, \(A=b^h\ge2^h\) because \(b\ge2\) is an integer. \(\square\)

## 5. Exercises

**5.1.** Compute \(d_{24}\) for \(a=-9\).

**5.2.** Compute \(d_6\) for \(a=-1/8\).

**5.3.** For \(a=2\), show that \(d_n=n\varphi(n)/2\) exactly when \(8\mid n\).

## 6. Solutions

**5.1.** Here \(b=3\), \(h=2\), \(D=12\), \(g=2\) and \(m=12\). So \(e_{24}=6\) and \(d_{24}=48\). As a check, an \(\alpha\) with \(\alpha^6=\sqrt3\,\zeta_8\in E_{24}\) satisfies \(\alpha^{24}=-9\).

**5.2.** Here \(b=1/2\), \(h=3\), \(D=8\), \(g=3\) and \(m=2\), while \(8\nmid12\). So \(e_6=2\) and \(d_6=4\). Indeed \((1/\sqrt{-2})^6=-1/8\), so \(K_6=\mathbb Q(\sqrt{-3},\sqrt{-2})\).

**5.3.** Here \(h=1\) and \(\Delta_2=8\). Corollary 3.2 applies.

## Sources

- [OpenAI-029] OpenAI, *Primitive roots for every admissible integer base*, OpenAI Math Release preprint, 4 October 2026, Section 9. https://github.com/openai/math/tree/main/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026
- [M05] P. Moree, *On primes p for which d divides ord_p(g)*, Funct. Approx. Comment. Math. 33 (2005), Lemma 3 (signed Kummer degrees, for comparison). https://arxiv.org/abs/math/0407421
- The main argument follows a solution produced with ChatGPT (OpenAI) in October 2026 and completed here.
