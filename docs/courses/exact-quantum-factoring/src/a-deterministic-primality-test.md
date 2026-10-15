# A deterministic primality test

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The factoring process of [Factoring with verifiable auxiliary data](factoring-with-verifiable-auxiliary-data.md) checks the factorizations that it produces, and for this it needs to decide exactly whether a given number is prime, by a classical algorithm with a polynomial bound on its running time. Agrawal, Kayal and Saxena gave the first such algorithm [AKS 2004]. This lesson proves a variant of their test with simpler bounds [OpenAI-EQF, Appendix A]: the auxiliary modulus is a prime \(s\le n^8\), and the tested residues are \(1\le a\le8s\). The original test uses an auxiliary modulus of size at most about \((\log_2m)^5\) and far fewer congruences, so its running time is a much smaller polynomial; the variant needs only elementary estimates.

- The algorithm (Section 1).
- An auxiliary prime (Section 2).
- Correctness (Section 3).
- Running time (Section 4).

We use from the core course [Abstract Algebra I](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C30) (Judson, *Abstract Algebra: Theory and Applications*) the unique factorization of integers ([Theorem 2.2.7](https://judsonbooks.org/aata-files/aata-html/integers-section-division-algorithm.html)) and Fermat's little theorem ([Theorem 6.3.3](https://judsonbooks.org/aata-files/aata-html/cosets-section-fermat-euler.html)), and from the core course [Abstract Algebra II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C40) that a nonzero polynomial of degree \(d\) over a field has at most \(d\) roots in that field ([Corollary 17.2.4](https://judsonbooks.org/aata-files/aata-html/poly-section-division-algorithm.html)), that every nonconstant polynomial over a field has a root in some extension field ([Theorem 21.1.5](https://judsonbooks.org/aata-files/aata-html/fields-section-extension-fields.html)), and that \((u+v)^p=u^p+v^p\) in an integral domain of prime characteristic \(p\) ([Lemma 22.1.3](https://judsonbooks.org/aata-files/aata-html/finite-section-field.html)).

## 1. The algorithm

Throughout, \(n\ge128\) and \(2\le m<2^n\) are integers. For a prime \(s\) not dividing \(m\), \(\operatorname{ord}_s(m)\) is the least \(j\ge1\) with \(m^j\equiv1\pmod s\). For polynomials \(A,C\in\mathbb Z[X]\) we write \(A\equiv C\pmod{m,X^s-1}\) if \(A-C=mG+(X^s-1)H\) with \(G,H\in\mathbb Z[X]\); equivalently, the images of \(A\) and \(C\) in \((\mathbb Z/m\mathbb Z)[X]\) differ by a multiple of \(X^s-1\).

1. Reject \(m\) if \(m=b^e\) with integers \(b,e\ge2\).
2. Find the least prime \(s\le n^8\) such that \(s\nmid m\) and \(\operatorname{ord}_s(m)>n^2\).
3. If \(m\le8s\), decide whether \(m\) is prime by trial division, and stop. Otherwise, reject \(m\) if some integer \(d\) with \(2\le d\le8s\) divides \(m\).
4. Accept \(m\) if and only if
\[
\begin{gathered}(X+a)^m\equiv X^m+a\\ \pmod{m,X^s-1}\\ \text{for all }1\le a\le8s .\end{gathered}\tag{1.1}
\]

**Theorem 1.1** ([OpenAI-EQF, Lemma A.1]). Step 2 always finds a prime \(s\), the algorithm accepts \(m\) if and only if \(m\) is prime, and its number of bit operations is bounded by a polynomial in \(n\).

The three claims are proved in Lemma 2.1, in Section 3 and in Section 4.

## 2. An auxiliary prime

**Lemma 2.1.** There is a prime \(s\le n^8\) with \(s\nmid m\) and \(\operatorname{ord}_s(m)>n^2\).

*Proof.* Put \(R=2\lfloor n^8/2\rfloor\), so that \(R\) is even and \(n^8-1\le R\le n^8\), and put \(C=\binom{R}{R/2}\). Let \(P_R\) be the product of the primes \(\ell\le R\), and \(\pi(R)\) their number.

*A lower bound for \(C\).* The \(R+1\) numbers \(\binom Rj\) add up to \(2^R\), and \(C\) is the largest of them (Exercise 5.1), so \(C\ge2^R/(R+1)\).

*An upper bound for \(C\).* For a prime \(\ell\) and an integer \(j\ge1\), the exponent of \(\ell\) in \(j!\) is \(\sum_{i\ge1}\lfloor j/\ell^i\rfloor\), since \(\lfloor j/\ell^i\rfloor\) of the numbers \(1,\ldots,j\) are divisible by \(\ell^i\). Hence the exponent of \(\ell\) in \(C=R!/((R/2)!)^2\) is
\[
\sum_{i\ge1}\Bigl(\Bigl\lfloor\frac R{\ell^i}\Bigr\rfloor-2\Bigl\lfloor\frac R{2\ell^i}\Bigr\rfloor\Bigr).
\]
Each summand has the form \(\lfloor2y\rfloor-2\lfloor y\rfloor\in\{0,1\}\) (Exercise 5.2), and it vanishes when \(\ell^i>R\). So the exponent \(e\) of \(\ell\) in \(C\) is at most the number of \(i\ge1\) with \(\ell^i\le R\), and \(\ell^e\le R\). The prime factors of \(C\) divide \(R!\), so they are at most \(R\), and unique factorization gives \(C\le R^{\pi(R)}\). As every prime is at least \(2\), \(\pi(R)\le\log_2P_R\). Together,
\[
\begin{aligned}R-\log_2(R+1)&\le\log_2C\\&\le\log_2P_R\,\log_2R .\end{aligned}
\]

*The estimate.* The function \(x\mapsto x-8\log_2x-1\) is positive at \(x=128\), where it equals \(71\), and increasing for \(x\ge128\), since its derivative is \(1-8/(x\ln2)>0\). So \(8\log_2n+1<n\), which gives \(\log_2R\le8\log_2n<n\) and \(\log_2(R+1)\le\log_2(2n^8)<n\). Therefore
\[
\begin{aligned}\log_2P_R&\ge\frac{R-\log_2(R+1)}{\log_2R}\\&>\frac{n^8-1-n}n>n^6 .\end{aligned}
\]

*The choice of \(s\).* The positive integer \(Y=m\prod_{j=1}^{n^2}(m^j-1)\) satisfies
\[
\begin{aligned}\log_2Y&<n+\sum_{j=1}^{n^2}jn\\&=n\Bigl(1+\frac{n^2(n^2+1)}2\Bigr)\\&\le n^5<n^6 ,\end{aligned}
\]
using \(m<2^n\) and \(1+\frac{n^2(n^2+1)}2\le n^4\) for \(n\ge2\). If every prime \(\ell\le R\) divided \(Y\), then their product \(P_R\) would divide \(Y\) by unique factorization, and \(\log_2P_R\le\log_2Y<n^6\), a contradiction. So some prime \(s\le R\le n^8\) divides neither \(m\) nor any \(m^j-1\) with \(1\le j\le n^2\), which means \(s\nmid m\) and \(\operatorname{ord}_s(m)>n^2\). \(\square\)

## 3. Correctness

**Lemma 3.1.** If \(m\) is prime, the algorithm accepts \(m\).

*Proof.* A prime is not of the form \(b^e\) with \(b,e\ge2\), since \(b\) would be a divisor with \(1<b<m\). Step 2 finds \(s\) by Lemma 2.1. If \(m\le8s\), trial division accepts. Otherwise no integer \(d\) with \(2\le d\le8s<m\) divides \(m\). The ring \((\mathbb Z/m\mathbb Z)[X]\) is an integral domain of characteristic \(m\), so \((X+a)^m=X^m+a^m\) there, and \(a^m=a\) in \(\mathbb Z/m\mathbb Z\) by Fermat's little theorem. So (1.1) holds even without the modulus \(X^s-1\), and the algorithm accepts. \(\square\)

**Proposition 3.2** ([OpenAI-EQF, Lemma A.1]; [AKS 2004, Section 4]). If \(m\) is composite, the algorithm rejects \(m\).

*Proof.* Suppose that a composite \(m\) is accepted. Then \(m\) is not a perfect power; step 2 found a prime \(s\le n^8\) with \(s\nmid m\) and \(\operatorname{ord}_s(m)>n^2\); \(m>8s\), since trial division rejects composite numbers; no integer from \(2\) to \(8s\) divides \(m\); and (1.1) holds. Fix a prime \(p\) dividing \(m\). Then \(p>8s\). Since \(m\) is composite and not a perfect power, it is not a power of \(p\), so it has a prime divisor \(p'\ne p\).

*Introspective exponents.* For \(f\in\mathbb F_p[X]\) and an integer \(k\ge1\), say that \(k\) is *introspective* for \(f\) if
\[
\begin{gathered}f(X)^k\equiv f(X^k)\pmod{X^s-1}\\ \text{in }\mathbb F_p[X],\end{gathered}
\]
following [AKS 2004, Section 4]. Let \(\mathcal P\subseteq\mathbb F_p[X]\) be the set of products of polynomials \(X+a\) with \(1\le a\le8s\), repetitions allowed, including the empty product \(1\). We show that every number \(m^up^v\) with integers \(u,v\ge0\) is introspective for every \(f\in\mathcal P\).

1. Reducing (1.1) modulo \(p\), which divides \(m\), shows that \(m\) is introspective for each \(X+a\), \(1\le a\le8s\).
2. If \(k\) is introspective for \(f\) and for \(g\), then \((fg)^k=f^kg^k\) and \(f^kg^k\equiv f(X^k)g(X^k)=(fg)(X^k)\), so \(k\) is introspective for \(fg\). With (1), \(m\) is introspective for every \(f\in\mathcal P\).
3. For \(f=\sum_ic_iX^i\in\mathbb F_p[X]\), the identity \((u+v)^p=u^p+v^p\) in \(\mathbb F_p[X]\), applied repeatedly, and Fermat's little theorem \(c_i^p=c_i\) give \(f(X)^p=\sum_ic_i^pX^{ip}=f(X^p)\). So \(p\) is introspective for every \(f\).
4. If \(b\) and \(c\) are introspective for \(f\), then so is \(bc\). Indeed \(f(X)^{bc}=(f(X)^b)^c\equiv f(X^b)^c\). Substituting \(X^b\) for \(X\) in \(f(X)^c-f(X^c)=(X^s-1)G(X)\) gives \(f(X^b)^c-f(X^{bc})=(X^{bs}-1)H\) with \(H=G(X^b)\), and \(X^s-1\) divides \(X^{bs}-1\). Hence \(f(X)^{bc}\equiv f(X^{bc})\).

As \(1\) is introspective for every \(f\), (2), (3) and (4) give the claim.

*A root of unity of order \(s\).* By the theorem on extension fields there is a field \(E\supseteq\mathbb F_p\) containing a root \(w\) of \(1+X+\cdots+X^{s-1}\). Since \(X^s-1=(X-1)(1+X+\cdots+X^{s-1})\), \(w^s=1\). The value of \(1+X+\cdots+X^{s-1}\) at \(1\) is \(s\), which is nonzero in \(\mathbb F_p\) because \(p>s\); so \(w\ne1\), and as \(s\) is prime, \(w\) has multiplicative order exactly \(s\). Thus \(w^k\) depends only on \(k\bmod s\), and \(w^0,\ldots,w^{s-1}\) are distinct. Evaluating at \(w\), where \(X^s-1\) vanishes, gives
\[
\begin{gathered}f(w)^k=f(w^k)\\ (f\in\mathcal P,\ k=m^up^v,\\ u,v\ge0).\end{gathered}\tag{3.1}
\]

*The group \(H\).* The residues of \(m\) and \(p\) are units modulo \(s\), because \(s\nmid m\) and \(p\ne s\). Let \(H\subseteq(\mathbb Z/s\mathbb Z)^\times\) be the subgroup they generate and \(h=|H|\). It contains the \(\operatorname{ord}_s(m)\) distinct powers of \(m\), so
\[
n^2<h\le s-1 .
\]
In a finite group the inverse of an element \(x\) is the power \(x^{o-1}\), where \(o\) is the order of \(x\); hence every element of \(H\) is the residue of some \(m^up^v\) with \(u,v\ge0\).

*Many values.* For a set \(A\subseteq\{1,\ldots,8s\}\) with \(h-1\) elements put \(f_A=\prod_{a\in A}(X+a)\in\mathcal P\); this is possible because \(h-1<s\). The numbers \(1,\ldots,8s\) are distinct modulo \(p\), as \(p>8s\), so \(f_A\) has the roots \(-a\), \(a\in A\), and different sets give different polynomials. Suppose \(f_A(w)=f_{A'}(w)\) with \(A\ne A'\). For every \(k=m^up^v\), (3.1) gives \(f_A(w^k)=f_A(w)^k=f_{A'}(w)^k=f_{A'}(w^k)\). As \(k\bmod s\) runs through \(H\), the elements \(w^k\) are \(h\) distinct roots of \(f_A-f_{A'}\), a nonzero polynomial of degree less than \(h-1\), since both are monic of degree \(h-1\). This contradicts the bound on the number of roots. So the values \(f_A(w)\) are distinct, and the set \(\mathcal V=\{f(w):f\in\mathcal P\}\subseteq E\) satisfies
\[
|\mathcal V|\ge\binom{8s}{h-1}\ge\Bigl(\frac{8s}{h-1}\Bigr)^{h-1}\ge8^{h-1}.
\]
Here \(\binom Mt=\prod_{i=0}^{t-1}\frac{M-i}{t-i}\ge(M/t)^t\) for \(1\le t\le M\), since \(\frac{M-i}{t-i}\ge\frac Mt\) is equivalent to \(M\ge t\); and \(8s/(h-1)\ge8\) since \(h-1<s\).

*Few values.* Put \(q=\lfloor\sqrt h\rfloor\). The \((q+1)^2>h\) pairs \((u,v)\) with \(0\le u,v\le q\) give residues \(m^up^v\bmod s\) in \(H\), so two different pairs \((u,v)\ne(u',v')\) give numbers \(k_1=m^up^v\) and \(k_2=m^{u'}p^{v'}\) with \(k_1\equiv k_2\pmod s\). They are different integers: the exponent of \(p'\) in \(k_1\) is \(u\) times its exponent in \(m\), so \(k_1=k_2\) would force \(u=u'\) and then \(p^v=p^{v'}\), \(v=v'\). For every \(f\in\mathcal P\), (3.1) and \(w^{k_1}=w^{k_2}\) give
\[
f(w)^{k_1}=f(w^{k_1})=f(w^{k_2})=f(w)^{k_2},
\]
so every element of \(\mathcal V\) is a root of the nonzero polynomial \(T^{k_1}-T^{k_2}\in E[T]\). Its degree is at most \(\max(k_1,k_2)\), and
\[
\begin{aligned}\max(k_1,k_2)&\le(mp)^q\le m^{2q}\\&<2^{2nq}\le2^{2n\sqrt h}<2^{2h},\end{aligned}
\]
where the last step uses \(n<\sqrt h\). Hence \(|\mathcal V|<2^{2h}\).

*Conclusion.* Since \(h>n^2\ge3\), \(8^{h-1}=2^{3h-3}\ge2^{2h}\), so the two bounds on \(|\mathcal V|\) contradict each other. Therefore no composite \(m\) is accepted. \(\square\)

The lower bound on \(|\mathcal V|\) adapts [AKS 2004, Lemma 4.7], which is credited there to H. W. Lenstra Jr. and was found independently by M. Macaj; the upper bound adapts [AKS 2004, Lemma 4.8], in a formulation credited there to A. Kalai, A. Sahai and M. Sudan.

## 4. Running time

Integers below \(2^n\) have \(n\) bits, and all integers that occur have \(O(n)\) bits.

- Step 1: if \(m=b^e\) with \(b\ge2\), then \(2^e\le m<2^n\), so \(e<n\). For each \(e\) from \(2\) to \(n-1\), a binary search over \(1\le b\le m\) decides whether \(b^e=m\) for some integer \(b\), with \(O(n)\) evaluations of \(b^e\), each stopped as soon as the partial product exceeds \(m\).
- Step 2: for each \(s\le n^8\), trial division by the numbers up to \(\sqrt s\le n^4\) decides whether \(s\) is prime, and \(m\bmod s\) and the residues \(m^j\bmod s\), \(1\le j\le n^2\), are computed by successive multiplication. By Lemma 2.1 a suitable \(s\) is found.
- Step 3: at most \(\max(\sqrt{8s},8s)\le8n^8\) trial divisions of \(n\)-bit numbers.
- Step 4: elements of \((\mathbb Z/m\mathbb Z)[X]/(X^s-1)\) are represented by their \(s\) coefficients, residues modulo \(m\). A product is computed with \(s^2\) multiplications of residues, reducing \(X^{s+i}\) to \(X^i\). Repeated squaring computes \((X+a)^m\) with at most \(2n\) products, and \(X^m+a\) reduces to \(X^{m\bmod s}+a\). With \(8s\le8n^8\) values of \(a\), step 4 uses \(O(n^{25})\) operations on residues.

The prime \(p\), the field \(E\) and the numbers \(k_1,k_2\) occur only in the proof and are never computed. So the number of bit operations is bounded by a polynomial in \(n\), and Theorem 1.1 is proved. \(\square\)

## 5. Exercises

**5.1.** Show that \(\binom R{j+1}\ge\binom Rj\) if and only if \(j<R/2\), and deduce that \(\binom R{R/2}\) is the largest of the numbers \(\binom Rj\) for even \(R\).

**5.2.** Show that \(\lfloor2y\rfloor-2\lfloor y\rfloor\in\{0,1\}\) for every real \(y\).

**5.3.** Let \(s\ge7\) be prime. Show that \((X+1)^6\not\equiv X^6+1\pmod{6,X^s-1}\).

**5.4.** Find the least prime \(s\) with \(s\nmid31\) and \(\operatorname{ord}_s(31)>4\).

**5.5.** In the proof of Proposition 3.2, show that \(f(w)\ne0\) for every \(f\in\mathcal P\).

## 6. Solutions

**5.1.** \(\binom R{j+1}/\binom Rj=\frac{R-j}{j+1}\), which is at least \(1\) exactly when \(R-j\ge j+1\), that is, \(j<R/2\) for even \(R\). So the numbers increase up to \(j=R/2\) and decrease after it.

**5.2.** Write \(y=\lfloor y\rfloor+\theta\) with \(0\le\theta<1\). Then \(\lfloor2y\rfloor=2\lfloor y\rfloor+\lfloor2\theta\rfloor\), and \(\lfloor2\theta\rfloor\in\{0,1\}\).

**5.3.** Modulo \(6\),
\[
\begin{aligned}(X+1)^6&=X^6+6X^5+15X^4\\&\quad+20X^3+15X^2+6X+1\\&\equiv X^6+3X^4\\&\quad+2X^3+3X^2+1 .\end{aligned}
\]
The difference \(3X^4+2X^3+3X^2\) is not a multiple of \(X^s-1\) in \((\mathbb Z/6\mathbb Z)[X]\): reducing modulo \(X^s-1\) does not change a polynomial of degree less than \(s\), and this one is nonzero.

**5.4.** \(31\equiv1\) modulo \(2\), \(3\) and \(5\), so the order is \(1\) for these primes. Modulo \(7\), \(31\equiv3\), with powers \(3,2,6,4,5,1\), so \(\operatorname{ord}_7(31)=6>4\), and \(s=7\).

**5.5.** If \(f(w)=0\), then some factor \(X+a\) of \(f\) vanishes at \(w\), that is, \(w=-a\). By (3.1) for this factor, \(w^k+a=(w+a)^k=0\) for every \(k=m^up^v\), so \(w^k=w\) and \(k\equiv1\pmod s\). Then \(H\) would be trivial, contradicting \(h>n^2\).

## References

- [OpenAI-EQF] OpenAI, *Exact quantum factoring over a fixed finite gate set*, OpenAI Math Release preprint, 25 September 2026, Appendix A. https://github.com/openai/math/tree/main/preprints/Exact-quantum-factoring-over-a-fixed-finite-gate-set-September-25-2026
- [AKS 2004] M. Agrawal, N. Kayal, N. Saxena, *PRIMES is in P*, Ann. of Math. (2) 160 (2004), no. 2, 781–793. https://www.cse.iitk.ac.in/users/manindra/algebra/primality_v6.pdf
