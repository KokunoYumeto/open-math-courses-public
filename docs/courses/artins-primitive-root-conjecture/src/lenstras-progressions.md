# Lenstra's progressions

*Written by Claude Opus 5.5 (Anthropic) on 23 October 2026. The question was posed by Claude while writing this course and solved by GPT-6 Astra (OpenAI) in ChatGPT's Pro mode; the solution was refereed by Claude Opus 5.5 in a separate session, and this lesson was written from it and refereed and revised by Claude Opus 5.5 in two further sessions. Public domain (CC0).*

This lesson studies primes \(p\equiv r\pmod f\) at which \(a\) has a prescribed index \(i_p(a)=m\), a question going back to Lenstra. It proves three things.

- The bound of [*Complete splitting at composite levels*](complete-splitting-at-composite-levels.md) extends to the fields \(K_n\mathbb Q(\mu_f)\), uniformly in \(n\) and \(f\).
- The congruence sieve yields the indices \(m\in\{1,2\}\) in progressions, through a finite certificate. For general \((m,f,r)\), the problem reduces to one Frobenius-restricted lower bound, Hypothesis F, whose Frobenius condition is nonempty.
- In \(\mathbb Q(\mu_3,2^{1/3})\), no congruence condition forces splitting or nonsplitting.

**Prerequisites.**
- [*Artin's conjecture and the index of a prime*](artins-conjecture-and-the-index-of-a-prime.md), Lemma 1.1, (4.1) and Proposition 5.1.
- [*Complete splitting at composite levels*](complete-splitting-at-composite-levels.md), Propositions 1.2, 2.1 and 3.2, Lemma 3.1, Theorems 4.1 and 5.1, and Lemma 5.2.
- [*Uniform complete splitting in Kummer fields*](uniform-complete-splitting-in-kummer-fields.md), Lemma 3.1 and Section 4.
- [*The zero-free strip*](the-zero-free-strip.md), Corollary 4.2.
- [*Primes with controlled predecessors*](primes-with-controlled-predecessors.md), Theorem 6.1.
- [*Hilbert's ramification theory in Galois extensions*](course:NT-ANT/hilberts-ramification-theory-in-galois-extensions), Corollary 6.5.
- [*The different and the discriminant*](course:NT-ANT/the-different-and-the-discriminant), Proposition 14.2 and Theorem 14.3.
- [*Artin L-functions, conductors and discriminants*](course:NT-CFT/artin-l-functions-conductors-and-discriminants), Proposition 21.1 and Theorem 21.2.
- [*The Chebotarev density theorem*](course:NT-CFT/the-chebotarev-density-theorem), Theorem 22.4.

## 1. Splitting in the fields \(K_n\mathbb Q(\mu_f)\)

Fix \(a\in\mathbb Z\) with \(A=|a|>1\), and write \(A=b^h\) as in Section 1 of the composite-levels lesson. Put \(E_n=\mathbb Q(\mu_n)\) and \(K_n=E_n(\alpha_n)\) with \(\alpha_n^n=a\). For \(n,f\ge1\) put
\[
\begin{gathered}
N=\operatorname{lcm}(n,f),\\
K_n^{(f)}=K_nE_f,\qquad d_n^{(f)}=[K_n^{(f)}:\mathbb Q].
\end{gathered}
\]
For \(\sigma\in\operatorname{Gal}(E_f/\mathbb Q)\) and \(r\) prime to \(f\), write \(\sigma=\sigma_r\) when \(\sigma(\zeta_f)=\zeta_f^r\). Throughout, \(L=\log x\), \(\delta_0=10^{-6}\), \(y=\exp(L^{0.1})\) and \(z=\exp(L^{0.3})\).

**Lemma 1.1.** The field \(K_n^{(f)}\) has the following properties.

1. It is Galois over \(\mathbb Q\), it equals \(E_N(\alpha_n)\), and it is contained in \(K_N\).
2. Every prime \(p\nmid aN\) is unramified in it.
3. For such \(p\), the prime \(p\) splits completely in \(K_n^{(f)}\) exactly when \(p\equiv1\pmod f\) and \(n\mid i_p(a)\).

*Proof.* *Part 1.* The field is a compositum of Galois fields, so it is Galois over \(\mathbb Q\). Since \((N/n,N/f)=1\), Bézout's identity writes \(\zeta_N\) as a product of powers of \(\zeta_n=\zeta_N^{N/n}\) and \(\zeta_f=\zeta_N^{N/f}\). Hence \(E_nE_f=E_N\), and \(K_n^{(f)}=E_N(\alpha_n)\). The element \(\alpha_N^{N/n}\) is an \(n\)th root of \(a\). Any two \(n\)th roots of \(a\) differ by an element of \(\mu_n\subset E_N\), so \(E_N(\alpha_n)\subseteq K_N\).

*Part 2.* By Lemma 3.1 of the composite-levels lesson at level \(N\), the prime \(p\) is unramified in \(K_N\). It is therefore unramified in every subfield of \(K_N\).

*Part 3.* The Frobenius of \(p\) in the compositum is trivial exactly when its restrictions to \(E_f\) and to \(K_n\) are trivial. The restriction to \(E_f\) is \(\sigma_p\). By Lemma 3.1 of the composite-levels lesson, the restriction to \(K_n\) is trivial exactly when \(n\mid i_p(a)\). Corollary 6.5 of [*Hilbert's ramification theory in Galois extensions*](course:NT-ANT/hilberts-ramification-theory-in-galois-extensions) identifies complete splitting of an unramified prime with trivial Frobenius. \(\square\)

**Proposition 1.2.** For all \(n,f\ge1\), \(\zeta_{K_n^{(f)}}\) has no zero in \(\operatorname{Re}s>1-\delta_0\). Moreover,
\[
\frac{\log D_n^{(f)}}{d_n^{(f)}}\le2\log N+\log A .
\]

*Proof.* *The zero-free strip.* Put \(K'=K_n^{(f)}\), \(F=\mathbb Q(\mu_{12N})\) and \(T=K'F=F(\alpha_n)\).
- The extension \(T/F\) is cyclic, because \(\sigma\mapsto\sigma(\alpha_n)/\alpha_n\) embeds its group in \(\mu_n\).
- The extension \(T/K'\) is abelian, because restriction embeds its group in \(\operatorname{Gal}(F/\mathbb Q)\).

By (4) of Proposition 21.1 and Theorem 21.2 of [*Artin L-functions, conductors and discriminants*](course:NT-CFT/artin-l-functions-conductors-and-discriminants), \(\zeta_T\) is the product of the \(L_F(s,\eta)\) over the characters \(\eta\) of \(\operatorname{Gal}(T/F)\). The same results give \(\zeta_T=\zeta_{K'}\prod_{\eta'\ne1}L_{K'}(s,\eta')\), with \(\eta'\) running over the nontrivial characters of \(\operatorname{Gal}(T/K')\); each such factor is entire. Corollary 4.2 of [*The zero-free strip*](the-zero-free-strip.md) applies to every \(L_F(s,\eta)\), since \(F\supseteq\mu_{12}\), so \(\zeta_T\) has no zero in the half-plane. A zero of \(\zeta_{K'}\) there would be a zero of \(\zeta_T\).

*The discriminant.* By (16) of Theorem 14.3 of [*The different and the discriminant*](course:NT-ANT/the-different-and-the-discriminant), \(D_{K_N}=(D_n^{(f)})^{[K_N:K']}\,\mathrm N(\mathfrak d_{K_N/K'})\), and the norm is a positive integer. Taking logarithms and dividing by \(d_{K_N}=[K_N:K']\,d_n^{(f)}\) gives \(\log D_n^{(f)}/d_n^{(f)}\le\log D_{K_N}/d_{K_N}\). Proposition 2.1 of the composite-levels lesson bounds the right side by \(2\log N+\log A\). \(\square\)

**Theorem 1.3.** There is an absolute constant \(C_*\) such that, for all \(n,f\ge1\) and \(x\ge\max(A,N,2)+1\), the number of primes \(x<p\le2x\) with \(p\equiv1\pmod f\) and \(n\mid i_p(a)\) is at most
\[
\begin{aligned}
&\frac{C_*x}{d_n^{(f)}L}\\
&\quad+C_*x^{1-\delta_0}\frac{2\log N+\log A+1}{L}.
\end{aligned}
\]

*Proof.* Fix \(\phi\) as in Section 4 of [*Uniform complete splitting in Kummer fields*](uniform-complete-splitting-in-kummer-fields.md). No prime in \((x,2x]\) divides \(aN\). By Lemma 1.1, each prime counted splits completely in \(K'\), so it contributes at least \(d_n^{(f)}L\) to \(\Theta_{K',\phi}(x)\). By Proposition 1.2, Lemma 3.1 of that lesson applies with \(\delta=\delta_0\), and \(\log D_n^{(f)}+d_n^{(f)}\le\) \(d_n^{(f)}(2\log N+\log A+1)\). Dividing the resulting bound by \(d_n^{(f)}L\) gives the claim, with \(C_*=C_\phi\). \(\square\)

## 2. Prescribed index in a progression

By Section 5 of the composite-levels lesson, Theorem 6.1 of [*Primes with controlled predecessors*](primes-with-controlled-predecessors.md) holds for every triple \((M,c,u)\) satisfying
\[
\begin{gathered}
8\mid M,\quad c\in\{2,4\},\quad(u,M)=1,\\
c\mid u-1,\quad\bigl(\tfrac{u-1}c,\tfrac Mc\bigr)=1 .
\end{gathered}
\]
It supplies \(\kappa=\kappa(M,c,u)>0\) such that, for large \(x\), at least \(\kappa x/L^2\) primes \(p\in(x,2x)\) satisfy \(p\equiv u\pmod M\) and \(p-1=csQ\). Here \(Q>x^{0.9}\) is prime and every prime factor of \(s\) lies in \((y,z)\).

**Theorem 2.1.** Let \((r,f)=1\) and \(\epsilon\in\{\pm1\}\), and let \((M,c,u)\) be as above, with \(f\mid M\) and \(u\equiv r\pmod f\). Suppose \(\bigl(\frac ap\bigr)=\epsilon\) for every prime \(p\equiv u\pmod M\) with \(p\nmid a\). Put \(m=1\) if \(\epsilon=-1\). Put \(m=2\) if \(\epsilon=+1\), and assume \(c=2\) in that case. Then, for large \(x\), at least \(\frac\kappa2x/L^2\) primes \(x<p<2x\) satisfy \(p\equiv r\pmod f\) and \(i_p(a)=m\).

*Proof.* Take \(x>A\) and \(y>2\). The supplied primes lie in the class \(r\bmod f\). By Euler's criterion, \(i_p(a)\) is even exactly when \(\bigl(\frac ap\bigr)=1\).
- If \(\epsilon=-1\), the index is odd, so \(v_2(i_p(a))=0\).
- If \(\epsilon=+1\), then \(c=2\) and \(sQ\) is odd, so \(v_2(p-1)=1\). The index is even and divides \(p-1\), so \(v_2(i_p(a))=1\).

Theorem 5.1 of the composite-levels lesson with \(C=c\) gives the conclusion. \(\square\)

**Example 2.2.** Take \(a=2\) and \(f=3\).
- The triple \((24,2,11)\) satisfies the conditions, and \(11\equiv3\pmod8\) gives \(\bigl(\frac2p\bigr)=-1\). Hence \(i_p(2)=1\) for \(\gg x/L^2\) primes \(p\equiv2\pmod3\).
- The triple \((24,2,23)\) satisfies the conditions, and \(23\equiv7\pmod8\) gives \(\bigl(\frac2p\bigr)=+1\). Hence \(i_p(2)=2\) for \(\gg x/L^2\) such primes.

**Lemma 2.3.** Let \(m,f\ge1\) and \((r,f)=1\). Suppose some prime \(p_1\nmid af\) has \(p_1\equiv r\pmod f\) and \(i_{p_1}(a)=m\). Put \(C=\prod_{\ell\mid2m}\ell^{v_\ell(p_1-1)}\) and \(J=K_CE_f\). Let \(\Sigma\) be the set of \(\sigma\in\operatorname{Gal}(J/\mathbb Q)\) such that
- \(\sigma|_{K_m}=1\);
- \(\sigma|_{K_{m\ell}}\ne1\) for every prime \(\ell\mid C\) with \(m\ell\mid C\);
- \(\sigma|_{E_f}=\sigma_r\).

Then the following hold.
1. \(C\) is even, \(m\mid C\), \(p_1\nmid a\operatorname{lcm}(C,f)\), and \(\Sigma\) is a nonempty union of conjugacy classes containing \(\operatorname{Frob}_{p_1}\).
2. Let \(p\nmid aCf\) be a prime with \(\operatorname{Frob}_p\subseteq\Sigma\) and \(v_\ell(p-1)=v_\ell(C)\) for every \(\ell\mid C\). Then \(p\equiv r\pmod f\) and \(v_\ell(i_p(a))=v_\ell(m)\) for every \(\ell\mid C\).

*Proof.* *Part 1.* Lemma 5.2 of the composite-levels lesson gives that \(C\) is even, that \(m\mid C\) and that \(C\mid p_1-1\). Hence \(p_1\nmid a\operatorname{lcm}(C,f)\), and \(p_1\) is unramified in \(J\) by Lemma 1.1(2). Restriction to a Galois subfield carries conjugates to conjugates, and \(\operatorname{Gal}(E_f/\mathbb Q)\) is abelian, so \(\Sigma\) is a union of conjugacy classes. The Frobenius of \(p_1\) restricts to \(\sigma_r\) on \(E_f\). Since \(m\mid i_{p_1}(a)\) and \(m\ell\nmid i_{p_1}(a)\), Lemma 3.1 of the composite-levels lesson gives the other two conditions.

*Part 2.* The first and third conditions give \(p\equiv r\pmod f\) and \(m\mid i_p(a)\). Fix \(\ell\mid C\).
- If \(v_\ell(m)<v_\ell(C)\), then \(m\ell\mid C\), and the second condition gives \(m\ell\nmid i_p(a)\). Hence \(v_\ell(i_p(a))=v_\ell(m)\).
- Otherwise \(v_\ell(m)\le\) \(v_\ell(i_p(a))\le\) \(v_\ell(p-1)=\) \(v_\ell(C)=\) \(v_\ell(m)\). \(\square\)

**Hypothesis F**\((a,m,f,r)\). There is \(\kappa>0\) such that, for large \(x\), at least \(\kappa x/L^2\) primes \(p\in(x,2x)\) satisfy three conditions:
- \(p\nmid aCf\);
- \(p-1=CsQ\), with \(Q>x^{0.9}\) prime and every prime factor of \(s\) in \((y,z)\);
- \(\operatorname{Frob}_p(J/\mathbb Q)\subseteq\Sigma\).

**Theorem 2.4.** Under Hypothesis F\((a,m,f,r)\), for large \(x\) at least \(\frac\kappa2x/L^2\) primes \(p\in(x,2x)\) satisfy \(p\equiv r\pmod f\) and \(i_p(a)=m\).

*Proof.* Take \(y\) larger than every prime factor of \(C\). Then \(v_\ell(p-1)=v_\ell(C)\) for \(\ell\mid C\), and Lemma 2.3(2) applies. Theorem 5.1 of the composite-levels lesson gives the conclusion. \(\square\)

In Theorem 2.1, the set \(\Sigma\) is cut out by the value of \(\bigl(\frac ap\bigr)\) and a congruence, which is why a congruence sieve reaches it.

## 3. The obstruction

**Proposition 3.1.** Let \(\ell\) be an odd prime and \(y>\ell\). Every prime supplied by Theorem 6.1 of the controlled-predecessors lesson has \(\ell\nmid p-1\) and \(v_2(p-1)\le2\).

*Proof.* We have \(p-1=csQ\) with \(c\in\{2,4\}\), and every prime factor of \(sQ\) exceeds \(y>\ell\). \(\square\)

**Proposition 3.2.** Let \(K=\mathbb Q(\mu_3,2^{1/3})\), let \(3\mid M\), and let \(u\) be reduced modulo \(M\) with \(u\equiv1\pmod3\). Among the primes \(p\equiv u\pmod M\), those splitting completely in \(K\) have Dirichlet density \(1/(3\varphi(M))\), and the others have Dirichlet density \(2/(3\varphi(M))\).

*Proof.* *The group of \(K\).* By Eisenstein's criterion at \(2\), the field \(\mathbb Q(2^{1/3})\) has degree \(3\). So \(6\mid[K:\mathbb Q]\le6\), and the action on the roots of \(X^3-2\) gives \(\operatorname{Gal}(K/\mathbb Q)\cong S_3\), with \(E_3\) the fixed field of \(A_3\).

*The intersection.* Put \(B=E_M\), \(I=K\cap B\) and \(J=KB\). The field \(I\) is abelian over \(\mathbb Q\), so \(\operatorname{Gal}(K/I)\supseteq A_3\) and \(I\subseteq E_3\). Since \(3\mid M\), also \(E_3\subseteq I\), so \(I=E_3\).

*The group of \(J\).* Restriction \(\rho:\gamma\mapsto(\gamma|_K,\gamma|_B)\) is injective, with image in the set \(P\) of pairs agreeing on \(I\). Restriction maps \(\operatorname{Gal}(J/B)\) injectively onto \(\operatorname{Gal}(K/I)\), since the fixed field of the image is \(K\cap B=I\). Hence \([J:\mathbb Q]=3\varphi(M)=|P|\), and \(\rho\) is an isomorphism onto \(P\).

*The Frobenius classes.* For \(p\nmid6M\) in the progression, \(p\) is unramified in \(K\) by Lemma 3.1 of the composite-levels lesson. It is unramified in \(B\) because \(D_{E_M}\mid M^{\varphi(M)}\) (proof of Proposition 2.1 there) and Proposition 14.2 of [*The different and the discriminant*](course:NT-ANT/the-different-and-the-discriminant). Its Frobenius is \((g,\sigma_u)\) with \(g\in A_3=\{1,\gamma,\gamma^2\}\).
- The element \((1,\sigma_u)\) is central.
- For \(\tau\in G_B\) nontrivial on \(E_3\) and a transposition \(t\), the pair \((t,\tau)\) lies in \(P\), and conjugation by it exchanges \((\gamma,\sigma_u)\) and \((\gamma^2,\sigma_u)\).

The Chebotarev density theorem (Theorem 22.4 of [*The Chebotarev density theorem*](course:NT-CFT/the-chebotarev-density-theorem); also [Milne, Theorem 8.31]) gives the Dirichlet densities \(1/(3\varphi(M))\) and \(2/(3\varphi(M))\). Complete splitting in \(K\) means \(g=1\), by Corollary 6.5 of [*Hilbert's ramification theory in Galois extensions*](course:NT-ANT/hilberts-ramification-theory-in-galois-extensions). \(\square\)

**Corollary 3.3.** Let \(p>3\). If \(i_p(2)=3\), then \(p\equiv1\pmod3\) and \(p\) splits completely in \(K=K_3\). If \(i_p(2)=1\) and \(p\equiv1\pmod3\), then \(p\) does not split completely in \(K\). Every progression as in Proposition 3.2 contains a set of primes of each kind with positive Dirichlet density, so no such congruence implies either conclusion.

*Proof.* Lemma 3.1 of the composite-levels lesson shows that \(p\) splits completely in \(K\) exactly when \(3\mid i_p(2)\). The index divides \(p-1\). The last sentence is Proposition 3.2. \(\square\)

So for \((a,m,f,r)=(2,3,1,0)\) and \((2,1,3,1)\), Hypothesis F requires a sieve lower bound with a non-abelian Frobenius condition inserted. This bound does not follow from Theorem 6.1 of the controlled-predecessors lesson, by Proposition 3.1. Theorem 1.3 gives only upper bounds of size \(x/L\) at each fixed level, and Theorem 5.1 of the composite-levels lesson needs the seed as its input. A set of size \(\kappa x/L^2\) can lie entirely inside, or entirely outside, a set of size \(Bx/L\). So these estimates cannot produce the required intersection.

## 4. Exercises

**4.1.** Check that \((24,2,11)\) and \((24,2,23)\) satisfy the conditions of Section 2.

**4.2.** In Proposition 3.2, take \(u\equiv2\pmod3\) instead. Show that every prime \(p\equiv u\pmod M\) with \(p\nmid6M\) has the same Frobenius class, and that none of them splits completely in \(K\).

**4.3.** Show that \(X^3\equiv2\pmod p\) has exactly one solution for every prime \(p\equiv2\pmod3\).

**4.4.** Fix \(f\). Show that the number of primes \(p\in(x,2x]\) with \(p\equiv1\pmod f\) and \(q\mid i_p(a)\) for some prime \(q\in(y,z)\) is \(o(x/L^2)\).

## 5. Solutions

**4.1.** Both residues are prime to \(24\), and \(2\) divides \(10\) and \(22\). Moreover \((5,12)=(11,12)=1\).

**4.2.** The \(B\)-component \(\sigma_u\) is nontrivial on \(E_3\), so the \(K\)-component is a transposition. The pairs \((\gamma^j,1)\) lie in \(P\), and conjugation by them permutes the three transpositions transitively. So the three possible Frobenius elements form one class, and its \(K\)-component is never trivial.

**4.3.** Since \(3\nmid p-1\), the map \(t\mapsto t^3\) is a bijection of the cyclic group \(\mathbb F_p^\times\).

**4.4.** For \(q>\max(h,2)\), Proposition 1.2 of the composite-levels lesson and \(K_q\subseteq K_q^{(f)}\) give \(q(q-1)=d_q\le d_q^{(f)}\). Summing Theorem 1.3 over \(q\in(y,z)\), with \(\log N\le\log f+L^{0.3}\), bounds the count by
\[
\begin{aligned}
&C_*\frac{2x}{yL}\\
&\quad+C_*zx^{1-\delta_0}(3+\log Af).
\end{aligned}
\]
Both terms are \(o(x/L^2)\).

## Sources

- [OpenAI-029] OpenAI, *Primitive roots for every admissible integer base*, OpenAI Math Release preprint, 4 October 2026, Sections 9 and 12. https://github.com/openai/math/tree/main/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026
- [Milne] J. S. Milne, *Algebraic Number Theory*, version 3.08 (2020), Theorem 8.31. https://www.jmilne.org/math/CourseNotes/ANT.pdf
- [Lenstra] H. W. Lenstra, Jr., *On Artin's conjecture and Euclid's algorithm in global fields*, Invent. Math. 42 (1977), 201–224. https://pub.math.leidenuniv.nl/~lenstrahw/PUBLICATIONS/1977d/art.pdf
- The main argument follows a solution produced with ChatGPT (OpenAI) in October 2026 and is completed here.
