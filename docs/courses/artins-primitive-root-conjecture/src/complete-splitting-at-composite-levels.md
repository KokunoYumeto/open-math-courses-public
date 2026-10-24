# Complete splitting at composite levels

*Written by Claude Opus 5.5 (Anthropic) on 23 October 2026. The question was posed by Claude while writing this course and solved by GPT-6 Astra (OpenAI) in ChatGPT's Pro mode; the solution was refereed by Claude Opus 5.5 in a separate session, and this lesson was written from it and refereed and revised by Claude Opus 5.5 in two further sessions. Public domain (CC0).*

This lesson extends Proposition 5.2 of [*Artin's conjecture and the index of a prime*](artins-conjecture-and-the-index-of-a-prime.md) from prime levels \(q\) to every integer level \(n\), with no lower threshold on \(n\). The Kummer field at level \(n\) is \(K_n=\mathbb Q(\mu_n,a^{1/n})\).

- Section 1 bounds the degree of \(K_n\) from both sides, and Section 2 bounds its discriminant.
- Section 3 shows that the zero-free strip descends to \(\zeta_{K_n}\) for every \(n\), and Section 4 proves the uniform count of completely split primes.
- Section 5 proves a deletion theorem. It turns a supply of primes with prescribed index at finitely many small primes into primes with \(i_p(a)=m\). It also shows that the required Frobenius condition is nonempty whenever one prime with index \(m\) exists.

**Prerequisites.**
- [*Artin's conjecture and the index of a prime*](artins-conjecture-and-the-index-of-a-prime.md), Lemmas 1.1, 3.1 and 4.1, Theorem 2.1 and Proposition 5.1.
- [*Uniform complete splitting in Kummer fields*](uniform-complete-splitting-in-kummer-fields.md), Lemmas 1.1 and 3.1 and Section 4.
- [*The zero-free strip*](the-zero-free-strip.md), Corollary 4.2.
- [*Primes with controlled predecessors*](primes-with-controlled-predecessors.md), Theorem 6.1.
- [*Hilbert's ramification theory in Galois extensions*](course:NT-ANT/hilberts-ramification-theory-in-galois-extensions), Corollary 6.5.
- [*The different and the discriminant*](course:NT-ANT/the-different-and-the-discriminant), (1)–(4), Proposition 14.2 and Theorem 14.3.
- [*Discriminants and integral bases*](course:NT-ANT/discriminants-and-integral-bases), Proposition 2.2.
- [*Artin L-functions, conductors and discriminants*](course:NT-CFT/artin-l-functions-conductors-and-discriminants), Proposition 21.1 and Theorem 21.2.

## 1. Degrees

Fix \(a\in\mathbb Z\) with \(A=|a|>1\). Put \(E_n=\mathbb Q(\mu_n)\) and \(K_n=E_n(\alpha)\), where \(\alpha^n=a\). The field \(K_n\) is the splitting field of \(T^n-a\), so it is Galois over \(\mathbb Q\). Write \(d_n=[K_n:\mathbb Q]\) and \(D_n\) for its absolute discriminant.

Write \(A=b^h\), where \(h\) is the greatest common divisor of the exponents in the prime factorization of \(A\). Then \(b>1\), and the exponents of \(b\) have greatest common divisor \(1\).

**Lemma 1.1.** Let \(v,w\ge1\) be coprime integers. If the positive real number \(b^{w/v}\) lies in an abelian extension of \(\mathbb Q\), then \(v\le2\).

*Proof.* We first show that \(X^v-b^w\) is irreducible over \(\mathbb Q\). Let \(P\) be a monic factor of degree \(j\) with \(1\le j\le v\). By Gauss's lemma, \(P\) has integer coefficients. All roots of \(X^v-b^w\) have absolute value \(b^{w/v}\), so the constant term of \(P\) is an integer \(B\) with \(|B|=b^{wj/v}\). Then \(|B|^v=b^{wj}\), so \(v\mid wj\,v_\ell(b)\) for every prime \(\ell\mid b\). Since the \(v_\ell(b)\) have greatest common divisor \(1\) and \((v,w)=1\), we get \(v\mid j\), hence \(j=v\).

Every subgroup of an abelian group is normal, so the field \(\mathbb Q(b^{w/v})\) is Galois over \(\mathbb Q\). It is a real field. By irreducibility, it contains all the conjugates \(b^{w/v}\zeta_v^j\). These are all real only if \(v\le2\). \(\square\)

**Proposition 1.2.** Put \(g=(n,h)\). Then
\[
\frac{n\varphi(n)}{2g}\le d_n\le n\varphi(n).
\]
For every prime \(q>\max(h,2)\) one has \(d_q=q(q-1)\).

*Proof.* Put \(m=n/g\) and \(u=h/g\), so that \((u,m)=1\). Let \(\beta=b^{u/m}>0\); then \(\beta^n=A\). Let \(F\) be a cyclotomic field containing \(\mu_m\), and put \(e=[F(\beta):F]\).

Since \(\beta^m\in\mathbb Q\), the map \(\sigma\mapsto\sigma(\beta)/\beta\) is an injective homomorphism from \(\operatorname{Gal}(F(\beta)/F)\) into \(\mu_m\). Its image is \(\mu_e\). So \(\beta^e=b^{ue/m}\) is fixed by the whole Galois group and lies in \(F\). In lowest terms, \(ue/m\) has denominator \(m/e\), and Lemma 1.1 gives \(m/e\le2\).

If \(a>0\), take \(\alpha=\beta\) and \(F=E_n\). If \(a<0\), take \(\alpha=\zeta_{2n}\beta\), so that \(\alpha^n=a\), and \(F=E_{2n}\). Since \(\zeta_{2n}\in F\), we have \(K_nF=F(\beta)\), and
\[
\begin{aligned}
[K_n:E_n]&\ge[K_nF:F]\\
&=[F(\beta):F]\ge m/2 .
\end{aligned}
\]
In both cases \(d_n\ge\varphi(n)n/(2g)\). The upper bound holds because \(\alpha\) is a root of \(T^n-a\) over \(E_n\).

For a prime \(q>\max(h,2)\) we have \(g=1\), so \(e_q=[K_q:E_q]\ge q/2\). Moreover \(e_q\mid q\), so \(e_q=q\). \(\square\)

**Example 1.3.** Take \(a=-4\). If \(c^j=-4\) with \(c\in\mathbb Z\) and \(j\ge2\), then \(j\) is odd and divides \(v_2(4)=2\), which is impossible. So \(-4\) is not a perfect power of an integer.

Let \(n=4k\), and choose \(\alpha\) with \(\alpha^k=1+i\). Then \(\alpha^n=(1+i)^4=-4\). Since \(1+i\in E_n\), this gives \([K_n:E_n]\le k\). Here \(h=2\) and \(g=2\), so Proposition 1.2 gives the reverse inequality, and
\[
d_n=\frac{n\varphi(n)}4\qquad(4\mid n).
\]
For instance, \(T^4+4=(T^2-2T+2)(T^2+2T+2)\) has the roots \(\pm1\pm i\), so \(K_4=\mathbb Q(i)\). Consequently, no formula \(d_n=n\varphi(n)/\epsilon\) with \(\epsilon\in\{1,2\}\) holds for all integers that are not perfect powers.

## 2. The discriminant

**Proposition 2.1.** For all \(n\ge1\),
\[
\begin{aligned}
\log D_n&\le d_n(2\log n+\log A),\\
\log D_n+d_n&\le C_A\,d_n\log(2n),
\end{aligned}
\]
where \(C_A=3+\log A/\log2\).

*Proof.* *The cyclotomic field.* Write \(T^n-1=\Phi_n(T)G(T)\) with \(G\in\mathbb Z[T]\). Differentiating at \(\zeta_n\) gives
\[
n\zeta_n^{n-1}=\Phi_n'(\zeta_n)G(\zeta_n).
\]
By Proposition 2.2 of [*Discriminants and integral bases*](course:NT-ANT/discriminants-and-integral-bases), \(\pm N(\Phi_n'(\zeta_n))\) is the discriminant of \(\mathbb Z[\zeta_n]\), and the field discriminant divides it. The integer \(N(G(\zeta_n))\) is nonzero, so this norm divides \(N(n\zeta_n^{n-1})=\pm n^{\varphi(n)}\). Hence \(D_{E_n}\mid n^{\varphi(n)}\).

*The relative step.* Let \(e=[K_n:E_n]\). The map \(\sigma\mapsto\sigma(\alpha)/\alpha\) embeds \(\operatorname{Gal}(K_n/E_n)\) in \(\mu_n\), with image \(\mu_e\). The conjugates of \(\alpha\) are therefore \(\alpha\mu_e\), and its minimal polynomial is \(f=T^e-c\) with \(c=\alpha^e\). The element \(c\) is integral, and \(|c|=A^{e/n}\) at every embedding.

The argument of Lemma 1.1 of [*Uniform complete splitting in Kummer fields*](uniform-complete-splitting-in-kummer-fields.md) applies to \(f\). It uses Euler's lemma and (1), (4) and (15) of [*The different and the discriminant*](course:NT-ANT/the-different-and-the-discriminant). It shows that \(f'(\alpha)\in\mathfrak D_{K_n/E_n}\), so the relative discriminant divides \(N_{K_n/E_n}(e\alpha^{e-1})=\pm e^ec^{e-1}\). Its absolute norm is at most
\[
e^{e\varphi(n)}A^{(e-1)e\varphi(n)/n}.
\]

*The tower.* The tower formula (16) there gives
\[
\begin{aligned}
\log D_n&\le e\varphi(n)\log n\\
&\quad+e\varphi(n)(\log e+\log A),
\end{aligned}
\]
using \((e-1)/n\le1\). Since \(e\le n\) and \(d_n=e\varphi(n)\), this is the first bound.

For the second bound, \(1-2\log2<0\) and \(\log(2n)\ge\log 2\) give
\[
\begin{aligned}
&2\log n+\log A+1\\
&\le2\log(2n)+\tfrac{\log A}{\log2}\log(2n)\\
&\le C_A\log(2n). \qquad\square
\end{aligned}
\]

## 3. Splitting and the descent of the strip

**Lemma 3.1.** Let \(p\nmid an\). The following are equivalent:

1. \(n\mid i_p(a)\);
2. \(p\) splits completely in \(K_n\);
3. \(p\equiv1\pmod n\) and \(a^{(p-1)/n}\equiv1\pmod p\).

*Proof.* Conditions 1 and 3 are equivalent by the proof of Lemma 1.1 of Lesson 1 with \(q\) replaced by \(n\).

For the equivalence of 2 and 3, follow the proof of Lemma 3.1 of Lesson 1 with \(q\) replaced by \(n\). The discriminant \(\pm n^na^{n-1}\) of \(T^n-a\) is prime to \(p\), so the roots of \(T^n-a\) have distinct reductions and \(p\) is unramified. The identity \(\prod_{i=1}^{n-1}(1-\zeta_n^i)=n\) makes reduction injective on \(\mu_n\). The Frobenius \(\sigma\) therefore fixes \(\zeta_n\) exactly when \(p\equiv1\pmod n\). Under that condition, \(\sigma(\alpha)=\alpha\) exactly when \(a^{(p-1)/n}\equiv1\pmod p\).

By Corollary 6.5 of [*Hilbert's ramification theory in Galois extensions*](course:NT-ANT/hilberts-ramification-theory-in-galois-extensions), an unramified prime splits completely exactly when its Frobenius is trivial. \(\square\)

**Proposition 3.2.** For every \(n\ge1\), \(\zeta_{K_n}(s)\ne0\) in \(\operatorname{Re}s>1-10^{-6}\).

*Proof.* Let \(F_n=\mathbb Q(\mu_{12n})\) and \(T_n=K_nF_n=F_n(\alpha)\).

- The extension \(T_n/F_n\) is Galois, and \(\sigma\mapsto\sigma(\alpha)/\alpha\) embeds its group in \(\mu_n\). So the group is cyclic.
- The extension \(T_n/K_n\) is Galois, and restriction to \(F_n\) embeds its group in the abelian group \(\operatorname{Gal}(F_n/\mathbb Q)\). So it is abelian.

By (4) of Proposition 21.1 and Theorem 21.2 of [*Artin L-functions, conductors and discriminants*](course:NT-CFT/artin-l-functions-conductors-and-discriminants),
\[
\begin{gathered}
\zeta_{T_n}(s)=\prod_\eta L_{F_n}(s,\eta),\\
\frac{\zeta_{T_n}(s)}{\zeta_{K_n}(s)}=\prod_{\eta'\ne1}L_{K_n}(s,\eta').
\end{gathered}
\]
Here \(\eta\) runs over the characters of \(\operatorname{Gal}(T_n/F_n)\), and \(\eta'\) over the nontrivial characters of \(\operatorname{Gal}(T_n/K_n)\).

Since \(F_n\supseteq\mu_{12}\), Corollary 4.2 of [*The zero-free strip*](the-zero-free-strip.md) makes every \(L_{F_n}(s,\eta)\), and hence \(\zeta_{T_n}\), zero-free in the half-plane. Each \(L_{K_n}(s,\eta')\) is entire. A zero of \(\zeta_{K_n}\) in the half-plane would therefore be a zero of \(\zeta_{T_n}\), which is impossible. \(\square\)

## 4. The bound at every level

**Theorem 4.1.** Put \(L=\log x\) and \(\delta_0=10^{-6}\). There is an absolute constant \(C_*\) such that, for all \(n\ge1\) and \(x\ge\max(A,n,2)+1\),
\[
\begin{aligned}
&\#\{x<p\le2x:\ p\ \text{splits}\\
&\qquad\text{completely in}\ K_n\}\\
&\le\frac{C_*x}{d_nL}\\
&\quad+C_*x^{1-\delta_0}\,\frac{2\log n+\log A+1}{L}.
\end{aligned}
\]
For \(n\le\exp(L^{0.3})\) and \(L\ge1\), the count is at most
\[
C_*\Bigl(\frac{x}{d_nL}+(4+\log A)x^{1-\delta_0}\Bigr).
\]

*Proof.* Since \(x>\max(A,n)\), no prime in \((x,2x]\) divides \(an\). Fix \(\phi\) as in Section 4 of Lesson 15. Proposition 3.2 allows us to apply Lemma 3.1 of Lesson 15 to \(K_n\) with \(\delta=\delta_0\). Each split prime contributes at least \(d_nL\) to the nonnegative sum \(\Theta_{K_n,\phi}(x)\). Inserting Proposition 2.1 gives the first bound.

For \(n\le\exp(L^{0.3})\) we have \(2\log n/L\le2\), and \((\log A+1)/L\le\log A+1\). This gives the second bound. \(\square\)

## 5. Deletion and seeds

Put \(y=\exp(L^{0.1})\) and \(z=\exp(L^{0.3})\).

**Theorem 5.1.** Fix an even integer \(C\), a divisor \(m\mid C\) and \(\kappa>0\). Suppose that, for large \(x\), there is a set \(\mathcal T(x)\) of at least \(\kappa x/L^2\) primes \(p\in(x,2x)\) with the following two properties:

- \(p-1=CrQ\), where \(Q>x^{0.9}\) is prime and every prime factor of \(r\) lies in \((y,z)\);
- \(v_\ell(i_p(a))=v_\ell(m)\) for every prime \(\ell\mid C\).

Then, for large \(x\), at least \(\frac\kappa2x/L^2\) primes of \(\mathcal T(x)\) satisfy \(i_p(a)=m\).

*Proof.* Take \(x\) so large that \(x>A\), \(y>\max(h,2)\) and \(z<x\). The second property and \(m\mid C\) give \(m\mid i_p(a)\).

Suppose \(i_p(a)>m\), and let \(q\) be a prime factor of \(i_p(a)/m\). By the second property, \(q\nmid C\). Since \(q\mid p-1=CrQ\), either \(q=Q\) or \(q\mid r\).

*The case \(q=Q\).* Then \(\operatorname{ord}_p(a)\le Cr<2x^{0.1}\), so \(p\) divides \(B_a(x)\) as in the proof of Theorem 2.1 of Lesson 1. There are \(O_a(x^{0.2}/L)\) such primes.

*The case \(q\mid r\).* Then \(y<q<z\). Since \(q>h\), Proposition 1.2 gives \(d_q=q(q-1)\). By Lemma 3.1, \(p\) splits completely in \(K_q\), and \(p\nmid aq\). Summing Theorem 4.1 over \(q\), using \(\sum_{j>y}1/(j(j-1))\le2/y\), bounds these primes by
\[
C_a\Bigl(\frac{2x}{Ly}+zx^{1-\delta_0}\Bigr).
\]
Both exceptional counts are \(o(x/L^2)\), so for large \(x\) together they are at most \(\frac\kappa2x/L^2\). \(\square\)

**Lemma 5.2.** Suppose \(i_{p_1}(a)=m\) for some prime \(p_1\nmid a\). Put
\[
C=\prod_{\ell\mid2m}\ell^{\,v_\ell(p_1-1)}.
\]
Then \(C\) is even, \(m\mid C\) and \(p_1\nmid aC\). Let \(\Sigma\) be the set of \(\sigma\in\operatorname{Gal}(K_C/\mathbb Q)\) whose restriction to \(K_m\) is trivial and whose restriction to \(K_{m\ell}\) is nontrivial for every prime \(\ell\mid C\) with \(m\ell\mid C\). Then \(\Sigma\) is stable under conjugation and contains the Frobenius class of \(p_1\).

*Proof.* The integer \(p_1-1\) is even and divisible by \(m\), so \(C\) is even and \(m\mid C\). Also \(C\mid p_1-1\), hence \(p_1\nmid C\).

For \(t\mid C\), the field \(K_t\) is a Galois subfield of \(K_C\), via \(\zeta_t=\zeta_C^{C/t}\) and \(\alpha_t=\alpha^{C/t}\). Restriction to \(K_t\) is a homomorphism, so \((\tau\sigma\tau^{-1})|_{K_t}\) is the conjugate of \(\sigma|_{K_t}\) by \(\tau|_{K_t}\). A conjugate of an element is trivial exactly when the element is, so \(\Sigma\) is stable under conjugation.

Finally, \(m\mid i_{p_1}(a)\) and \(m\ell\nmid i_{p_1}(a)\). Lemma 3.1 converts these into \(\operatorname{Frob}_{p_1}\in\Sigma\). \(\square\)

Proposition 5.1 of Lesson 1, proved as Theorem 6.1 of [*Primes with controlled predecessors*](primes-with-controlled-predecessors.md), holds for every triple \((M,c,u)\) satisfying (4.1) there, with no reference to \(a\).

*An index-2 instance.* Take \((M,c,u)=(8,2,7)\) and \(a=2\); (4.1) holds since \((7,8)=1\), \(2\mid6\) and \((3,4)=1\). Then \(\bigl(\tfrac2p\bigr)=1\) and \(v_2(p-1)=1\), so \(v_2(i_p(2))=1\). Theorem 5.1 with \(C=m=2\) gives at least a constant times \(x/L^2\) primes with \(i_p(2)=2\).

*What that proposition cannot reach.* Its primes satisfy \(3\nmid p-1\) once \(y>3\), so none of them satisfies \(i_p(2)=3\). A lower bound for the sieve with the Frobenius condition \(\Sigma\) inserted is not provided by that proposition.

## 6. Exercises

**6.1.** Show that \(d_6=4\) for \(a=-8\).

**6.2.** Deduce Theorem 2.1 of Lesson 1 from Theorem 5.1.

**6.3.** Show that \(K_n\) is unramified outside the primes dividing \(an\).

## 7. Solutions

**6.1.** We have \((\sqrt{-2})^6=(-2)^3=-8\), so \(K_6=E_6(\sqrt{-2})=\mathbb Q(\sqrt{-3},\sqrt{-2})\). The two quadratic fields are distinct, so the degree is \(4\).

**6.2.** Let \(a\) be admissible and take the triple \((M,c,u)\) of Lemma 4.1 of Lesson 1. Proposition 5.1 there supplies the first property with \(C=c\). Put \(m=1\). Since \(\bigl(\tfrac ap\bigr)=-1\), the index \(i_p(a)\) is odd, so \(v_2(i_p(a))=0\), which is the second property. Theorem 5.1 gives the conclusion.

**6.3.** The proof of Proposition 2.1 shows two things:
- the relative discriminant of \(K_n/E_n\) divides \(e^ec^{e-1}\), with \(e\mid n\), so it is supported on the primes dividing \(an\);
- \(D_{E_n}\) divides \(n^{\varphi(n)}\).

By the tower formula, \(D_n\) is divisible only by primes dividing \(an\). A prime ramifies exactly when it divides the discriminant (Proposition 14.2 of [*The different and the discriminant*](course:NT-ANT/the-different-and-the-discriminant)).

## Sources

- [OpenAI-029] OpenAI, *Primitive roots for every admissible integer base*, OpenAI Math Release preprint, 4 October 2026, Section 9. https://github.com/openai/math/tree/main/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026
- [HSW] E. Hasanalizade, Q. Shen and P.-J. Wong, *Counting zeros of Dedekind zeta functions*, Math. Comp. 91 (2022), Corollary 1.2. https://arxiv.org/abs/2102.04663
- The main argument follows a solution produced with ChatGPT (OpenAI) in October 2026 and is completed here.
