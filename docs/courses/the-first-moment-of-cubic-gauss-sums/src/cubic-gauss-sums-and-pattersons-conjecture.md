# Cubic Gauss sums and Patterson's conjecture

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

For a prime \(p\equiv1\pmod3\) the cubic exponential sum
\[
S_p=\sum_{x\bmod p}e\Bigl(\frac{x^3}{p}\Bigr)
\]
is a real number of absolute value at most \(2\sqrt p\). In 1846 Kummer tabulated \(S_p/(2\sqrt p)\) for \(p<500\) and found values in \([\frac12,1]\) about three times as often as values in \([-1,-\frac12]\). Heath-Brown and Patterson proved in 1979 that the angles of these sums are equidistributed, so that the normalized sums have mean zero at the scale of the number of primes. Patterson predicted in 1978 that a bias survives as a secondary term: summed over the primes up to \(X\), the normalized sums grow like \(X^{5/6}/\log X\). This course proves that prediction without any unproved hypothesis, following the proof found by OpenAI in 2026 [OpenAI-023].

Sections 1 and 2 set up the arithmetic of the Eisenstein integers and the cubic residue symbols. Section 3 introduces the cubic Gauss sums and proves their basic identities, including the evaluation of their cubes. Section 4 states the theorem with its equivalent forms, and Section 5 describes the route through the course.

**Prerequisites.** From *Class field theory*: [*Power residue symbols and reciprocity laws*](course:NT-CFT/power-residue-symbols-and-reciprocity-laws), Proposition 23.1 and the cubic reciprocity law (12). From *Dirichlet L-functions and primes in progressions*: [*Gauss sums*](course:NT-DIRL/NT-DIRL-03), Theorem 2.1; [*The prime number theorem for arithmetic progressions*](course:NT-DIRL/NT-DIRL-09), Theorem 3.1.

**Conventions.** \(e(x)=e^{2\pi ix}\), \(\omega=e^{2\pi i/3}\), \(K=\mathbb Q(\omega)\) and \(\mathcal O=\mathbb Z[\omega]\). For \(z\in K\), \(N(z)=z\bar z=|z|^2\) and \(\operatorname{Tr}(z)=z+\bar z\). We put \(\lambda=\sqrt{-3}=1+2\omega\). The letter \(\pi\) always denotes a prime, \(p\) and \(q\) denote rational primes, and \(\mu\) is the Möbius function on the nonzero ideals of \(\mathcal O\).

## 1. The Eisenstein integers

The ring \(\mathcal O\) is the ring of integers of \(K\). For \(z=a+b\omega\) with \(a,b\in\mathbb Q\),
\[
\begin{gathered}
N(z)=a^2-ab+b^2,\\
\operatorname{Tr}(z)=2a-b .
\end{gathered}
\]
The points of \(\mathcal O\) form a lattice of equilateral triangles with side \(1\), so every point of the plane lies at distance at most \(1/\sqrt3\) from \(\mathcal O\). Hence for \(x,y\in\mathcal O\) with \(y\ne0\) there is \(q\in\mathcal O\) with \(N(x/y-q)\le1/3\), and \(\mathcal O\) is Euclidean for the norm: it is a principal ideal domain with unique factorization. Its units are the six elements of norm one, \(\pm1,\pm\omega,\pm\omega^2\). The element \(\lambda\) satisfies \(\lambda^2=-3\) and \(\lambda=\omega(1-\omega)\); it is prime, since \(N(\lambda)=3\).

An element of \(\mathcal O\) is *prime to \(3\)* if \(\lambda\) does not divide it, and *primary* if it is congruent to \(1\) modulo \(3\).

**Lemma 1.1.** The six units are pairwise incongruent modulo \(3\). Every element prime to \(3\) has exactly one primary associate, and products and complex conjugates of primary elements are primary.

**Proof.** A nonzero element of \(3\mathcal O\) has norm at least \(9\), while two distinct units differ by an element of norm at most \(4\). The quotient \(\mathcal O/3\mathcal O\) has nine elements, three of which are multiples of \(\lambda\); the six units are prime to \(3\), so they represent the six remaining classes. If \(x\) is prime to \(3\), its class is the class of a unique unit \(u\), and \(u^{-1}x\equiv1\pmod 3\). If \(ux\equiv u'x\equiv1\), then \(3\) divides \((u-u')x\), hence \(u-u'\), and \(u=u'\). The set \(1+3\mathcal O\) is closed under multiplication and under complex conjugation. \(\square\)

By Lemma 1.1 and unique factorization, every nonzero ideal prime to \(3\) has exactly one primary generator. In all sums of this course, a variable denoted by one of the letters \(a,b,c,d,r,u\), or by \(\pi\), runs over primary elements, that is, over the ideals prime to \(3\), unless a different range is stated.

**Lemma 1.2 (the primary primes).** Up to units, the primes of \(\mathcal O\) are \(\lambda\) and the following primary primes:

- for each rational prime \(p\equiv1\pmod3\), two primary primes \(\pi\) and \(\bar\pi\), not associate, with \(\pi\bar\pi=p\);
- for each rational prime \(q\equiv2\pmod3\), the prime \(-q\), of norm \(q^2\).

**Proof.** A prime \(\pi\) divides \(\pi\bar\pi=N(\pi)\), hence a rational prime. Since \(\mathcal O\simeq\mathbb Z[x]/(x^2+x+1)\), for a rational prime \(p\) we have \(\mathcal O/p\mathcal O\simeq\mathbb F_p[x]/(x^2+x+1)\). If \(p\equiv1\pmod3\), the cyclic group \(\mathbb F_p^\times\) contains an element of order \(3\); it is a root of \(x^2+x+1\), whose other root is its square and differs from it. Then \(\mathcal O/p\mathcal O\simeq\mathbb F_p\times\mathbb F_p\), and \(p\) is the product of two different prime ideals of norm \(p\). For a prime \(\rho\) above \(p\), the equation \(\rho\bar\rho=p\) shows that \(\bar\rho\) generates the other prime ideal, so \(\rho\) and \(\bar\rho\) are not associate. Taking the primary associate \(\pi\) of \(\rho\), its conjugate \(\bar\pi\) is primary by Lemma 1.1. If \(q\equiv2\pmod3\), a root of \(x^2+x+1\) in \(\mathbb F_q\) would have order \(3\) in \(\mathbb F_q^\times\), whose order \(q-1\) is prime to \(3\); so \(\mathcal O/q\mathcal O\) is a field, \(q\) is prime in \(\mathcal O\), and its primary associate is \(-q\). Finally \(3=-\lambda^2\). \(\square\)

**Lemma 1.3 (the trace form).** (a) \(\operatorname{Tr}(\mathcal O)\subseteq\mathbb Z\), and the set of \(z\in K\) with \(\operatorname{Tr}(z\mathcal O)\subseteq\mathbb Z\) is \(\lambda^{-1}\mathcal O\).

(b) Let \(b\in\mathcal O\) be nonzero and prime to \(3\), and let \(h\in\mathcal O\). Then
\[
\sum_{v\bmod b}e\Bigl(\operatorname{Tr}\frac{hv}{b}\Bigr)
=\begin{cases}N(b),& b\mid h,\\ 0,& b\nmid h.\end{cases}
\]

**Proof.** (a) The first assertion is the formula for the trace. Since \(\lambda^{-1}=-(1+2\omega)/3\), a direct computation gives
\[
\begin{gathered}
\operatorname{Tr}(\lambda^{-1})=0,\quad
\operatorname{Tr}(\lambda^{-1}\omega)=1,\\
\operatorname{Tr}(\lambda^{-1}\omega^2)=-1 .
\end{gathered}
\]
Every \(z\in K\) can be written \(z=\lambda^{-1}(u+v\omega)\) with \(u,v\in\mathbb Q\), and then \(\operatorname{Tr}(z)=v\) and \(\operatorname{Tr}(z\omega)=u-v\). Since \(\mathcal O=\mathbb Z+\mathbb Z\omega\), the condition \(\operatorname{Tr}(z\mathcal O)\subseteq\mathbb Z\) holds exactly when \(u,v\in\mathbb Z\).

(b) The group \(\mathcal O/b\mathcal O\) has \(N(b)\) elements, the absolute value of the determinant of multiplication by \(b\) on \(\mathbb Z^2\). By (a) the map \(v\mapsto e(\operatorname{Tr}(hv/b))\) is a well-defined character of this group, so the sum is \(N(b)\) if the character is trivial and \(0\) otherwise. It is trivial exactly when \(h/b\in\lambda^{-1}\mathcal O\), that is, when \(b\) divides \(\lambda h\). As \(b\) is prime to \(\lambda\), this means \(b\mid h\). \(\square\)

## 2. Cubic residue symbols

Let \(\pi\) be a primary prime. The residue field \(\mathcal O/\pi\mathcal O\) has \(N(\pi)\) elements, and \(N(\pi)\equiv1\pmod3\) by Lemma 1.2. The cube roots of unity \(1,\omega,\omega^2\) are pairwise incongruent modulo \(\pi\), because their differences are associates of \(\lambda\). For \(v\) prime to \(\pi\), the power \(v^{(N(\pi)-1)/3}\) is a root of \(X^3-1\) in the residue field, hence congruent to exactly one of \(1,\omega,\omega^2\). This cube root of unity is \(\chi_\pi(v)\), and \(\chi_\pi(v)=0\) when \(\pi\mid v\).

By Proposition 23.1 of the reciprocity lesson, \(\chi_\pi(v)\) depends only on \(v\) modulo \(\pi\), is multiplicative in \(v\), and equals \(1\) exactly when \(v\) is a nonzero cube modulo \(\pi\). The group \((\mathcal O/\pi\mathcal O)^\times\) is cyclic of order divisible by \(3\), so it contains noncubes, and \(\chi_\pi\) is a character of order exactly \(3\).

For a primary element \(b=\prod\pi^{e_\pi}\) put
\[
\chi_b(v)=\prod_\pi\chi_\pi(v)^{e_\pi},\qquad \chi_1(v)=1 .
\]
Then \(\chi_b(v)\) depends only on the residue of \(v\) modulo the product of the distinct primes dividing \(b\). It vanishes exactly when \(v\) and \(b\) have a common prime factor, and \(\chi_{bb'}=\chi_b\chi_{b'}\).

**Lemma 2.1.** Let \(a,b\) be primary and \(v\in\mathcal O\).

- (a) \(\chi_{\bar b}(\bar v)=\overline{\chi_b(v)}\).
- (b) \(\chi_b(-1)=1\) and \(\chi_b(\omega)=\omega^{(N(b)-1)/3}\).
- (c) If \(a\) and \(b\) are coprime, then \(\chi_a(b)=\chi_b(a)\).

**Proof.** (a) Complex conjugation is a ring automorphism of \(\mathcal O\). Applied to the congruence \(v^{(N(\pi)-1)/3}\equiv\chi_\pi(v)\pmod\pi\), it gives \(\bar v^{(N(\pi)-1)/3}\equiv\overline{\chi_\pi(v)}\pmod{\bar\pi}\), and \(N(\bar\pi)=N(\pi)\). Multiply over the primes dividing \(b\).

(b) The element \(-1=(-1)^3\) is a cube. For a primary prime \(\pi\), the power \(\omega^{(N(\pi)-1)/3}\) is itself a cube root of unity, so \(\chi_\pi(\omega)=\omega^{(N(\pi)-1)/3}\). If \(N(\pi_i)=1+3k_i\), then \(\prod_i(1+3k_i)\equiv1+3\sum_ik_i\pmod9\), so \(\sum_ik_i\equiv(N(b)-1)/3\pmod3\), and the formula for \(b\) follows by multiplicativity.

(c) The reciprocity law (12) of the reciprocity lesson concerns coprime elements congruent to \(-1\) modulo \(3\), and \(-a,-b\) are such elements. The symbols depend on their lower entries only through the ideals \((-a)=(a)\) and \((-b)=(b)\), and \(\chi_b(-a)=\chi_b(a)\), \(\chi_a(-b)=\chi_a(b)\) by (b). \(\square\)

## 3. Cubic Gauss sums

For a primary element \(b\) define
\[
\begin{gathered}
g(b)=\sum_{v\bmod b}\chi_b(v)\,e\Bigl(\operatorname{Tr}\frac vb\Bigr),\\
G(b)=\frac{g(b)}{\sqrt{N(b)}} .
\end{gathered}
\]
Both factors of the summand depend only on \(v\) modulo \(b\), by Lemma 1.3(a).

**Proposition 3.1.** (a) \(G(1)=1\), and \(G(a)=0\) when \(a\) is divisible by the square of a prime.

(b) \(|G(\pi)|=1\) for every primary prime \(\pi\).

(c) If \(a,b\) are coprime and primary, then
\[
G(ab)=\overline{\chi_b(a)}\,G(a)\,G(b).
\]

(d) For every primary \(a\), \(|G(a)|=\mu^2(a)\) and \(G(\bar a)=\overline{G(a)}\).

**Proof.** (a) For \(a=1\) the sum has the single term \(v=0\), with \(\chi_1(0)=1\). Suppose \(\pi^2\mid a\) and put \(a'=a/\pi\). Every prime dividing \(a\) divides \(a'\), so \(\chi_a(v+a't)=\chi_a(v)\) for all \(v,t\in\mathcal O\). If \(v\) runs over representatives of \(\mathcal O/a'\mathcal O\) and \(t\) over \(\mathcal O/\pi\mathcal O\), then \(v+a't\) runs over \(\mathcal O/a\mathcal O\), each class once, and
\[
e\Bigl(\operatorname{Tr}\frac{v+a't}a\Bigr)
=e\Bigl(\operatorname{Tr}\frac va\Bigr)e\Bigl(\operatorname{Tr}\frac t\pi\Bigr).
\]
The sum over \(t\) of the last factor vanishes by Lemma 1.3(b) with \(h=1\), so \(g(a)=0\).

(b) Expanding the square,
\[
\begin{aligned}
|g(\pi)|^2&=\sum_{v,w\bmod\pi}\chi_\pi(v)\overline{\chi_\pi(w)}\\
&\qquad\cdot e\Bigl(\operatorname{Tr}\frac{v-w}\pi\Bigr).
\end{aligned}
\]
Only \(w\) prime to \(\pi\) contribute. Substituting \(v=wx\), the sum becomes
\[
\sum_{x\bmod\pi}\chi_\pi(x)\sum_{w\not\equiv0}
e\Bigl(\operatorname{Tr}\frac{w(x-1)}\pi\Bigr).
\]
By Lemma 1.3(b) the inner sum is \(N(\pi)-1\) for \(x\equiv1\) and \(-1\) otherwise. Since \(\chi_\pi\) is a nontrivial character, \(\sum_x\chi_\pi(x)=0\), and \(|g(\pi)|^2=N(\pi)\).

(c) By the Chinese remainder theorem, \((x,y)\mapsto bx+ay\) is a bijection from \(\mathcal O/a\mathcal O\times\mathcal O/b\mathcal O\) onto \(\mathcal O/ab\mathcal O\), and \((bx+ay)/(ab)=x/a+y/b\). Moreover
\[
\begin{gathered}
\chi_a(bx+ay)=\chi_a(b)\chi_a(x),\\
\chi_b(bx+ay)=\chi_b(a)\chi_b(y),
\end{gathered}
\]
so \(g(ab)=\chi_a(b)\chi_b(a)g(a)g(b)\). By Lemma 2.1(c), \(\chi_a(b)\chi_b(a)=\chi_b(a)^2\), and \(\zeta^2=\bar\zeta\) for a cube root of unity \(\zeta\). Divide by \(\sqrt{N(ab)}=\sqrt{N(a)}\sqrt{N(b)}\).

(d) For squarefree \(a\), apply (c) to its prime factorization and use (b); for the other \(a\), use (a). For the conjugate, Lemma 2.1(a) and \(\operatorname{Tr}(\bar w/\bar a)=\operatorname{Tr}(w/a)\) give
\[
g(\bar a)=\sum_{w\bmod a}\overline{\chi_a(w)}\,e\Bigl(\operatorname{Tr}\frac wa\Bigr).
\]
Replacing \(w\) by \(-w\) in \(\overline{g(a)}\) and using \(\chi_a(-1)=1\) gives the same sum, so \(g(\bar a)=\overline{g(a)}\). \(\square\)

**Proposition 3.2 (Kummer's sums).** Let \(p\equiv1\pmod3\) be prime and let \(\pi\) be a primary prime with \(\pi\bar\pi=p\). Then
\[
\begin{gathered}
G(\pi)+G(\bar\pi)=\frac{S_p}{\sqrt p},\\
\text{so}\quad\frac{S_p}{2\sqrt p}=\operatorname{Re}G(\pi).
\end{gathered}
\]

**Proof.** The residue field \(\mathcal O/\pi\mathcal O\) has \(p\) elements, so the rational integers \(0,1,\ldots,p-1\) represent it. For such \(v\),
\[
\begin{gathered}
\operatorname{Tr}\frac v\pi=v\operatorname{Tr}\frac{\bar\pi}p=\frac{vt}p,\\
t=\pi+\bar\pi\in\mathbb Z .
\end{gathered}
\]
The prime \(p\) does not divide \(t\), since otherwise \(\pi\) would divide \(\bar\pi\). On rational integers \(\chi_\pi\) restricts to a character \(\psi\) of \(\mathbb F_p^\times\) of order \(3\), and \(\chi_{\bar\pi}(v)=\overline{\psi(v)}\) for \(v\in\mathbb Z\) by Lemma 2.1(a). With \(\tau(\psi)=\sum_{v\bmod p}\psi(v)e(v/p)\), the substitution \(v\mapsto t^{-1}v\) gives
\[
g(\pi)=\overline{\psi(t)}\,\tau(\psi),\qquad
g(\bar\pi)=\psi(t)\,\tau(\bar\psi).
\]
Since \(t\equiv\bar\pi\pmod\pi\), we have \(\psi(t)=\chi_\pi(\bar\pi)\). By Lemma 2.1(c) and (a), \(\chi_\pi(\bar\pi)=\chi_{\bar\pi}(\pi)=\overline{\chi_\pi(\bar\pi)}\), so this cube root of unity is real, and \(\psi(t)=1\). Finally,
\[
\begin{aligned}
&\tau(\psi)+\tau(\bar\psi)\\
&=\sum_{v\bmod p}\bigl(1+\psi(v)+\bar\psi(v)\bigr)e\Bigl(\frac vp\Bigr)\\
&=S_p ,
\end{aligned}
\]
because \(\sum_ve(v/p)=0\), and \(1+\psi(v)+\bar\psi(v)\) is the number of solutions of \(y^3\equiv v\pmod p\): three for a nonzero cube, none for a nonzero noncube, and one for \(v\equiv0\). The second formula follows from Proposition 3.1(d). \(\square\)

**Theorem 3.3 (the cube of a Gauss sum).** For every primary prime \(\pi\),
\[
G(\pi)^3=-\frac{\pi}{|\pi|} .
\]
If \(\pi=-q\) with a rational prime \(q\equiv2\pmod3\), then \(G(\pi)=\chi_\pi(\lambda)\).

**Proof.** First let \(N(\pi)=p\equiv1\pmod3\), with \(\psi\) as in the proof of Proposition 3.2, so that \(g(\pi)=\tau(\psi)\). Let
\[
J=\sum_{x\bmod p}\psi(x)\psi(1-x)
\]
be the Jacobi sum.

1. *\(\tau(\psi)^2=J\,\tau(\psi^2)\).* Grouping the pairs \((x,y)\) by \(s=x+y\),
\[
\begin{aligned}
\tau(\psi)^2&=\sum_{s\bmod p}e\Bigl(\frac sp\Bigr)\\
&\qquad\cdot\sum_{x+y=s}\psi(x)\psi(y).
\end{aligned}
\]
For \(s\not\equiv0\), the substitution \(x=sx'\) shows that the inner sum is \(\psi^2(s)J\). For \(s\equiv0\) it is \(\psi(-1)\sum_x\psi^2(x)=0\), as \(\psi^2\) is nontrivial.
2. *\(\tau(\psi)^3=pJ\).* We have \(\psi^2=\bar\psi\). The value \(\psi(-1)\) is a cube root of unity with square \(1\), so \(\psi(-1)=1\), and Theorem 2.1 of the lesson on Gauss sums gives \(\tau(\psi)\tau(\bar\psi)=p\). Multiply step 1 by \(\tau(\psi)\).
3. *\(|J|^2=p\),* because \(|\tau(\psi)|^2=p\) by the same theorem.
4. *\(\pi\) divides \(J\).* Put \(m=(p-1)/3\). Since \(\psi(x)\equiv x^m\pmod\pi\),
\[
J\equiv\sum_{x=0}^{p-1}x^m(1-x)^m\pmod\pi .
\]
Expanding \((1-x)^m\) expresses the right side through power sums \(\sum_xx^k\) with \(m\le k\le2m<p-1\). Each is divisible by \(p\): for \(1\le k\le p-2\) there is \(y\in\mathbb F_p^\times\) with \(y^k\ne1\), and \(x\mapsto yx\) permutes \(\mathbb F_p\) while multiplying the sum by \(y^k\). Since \(p\in\pi\mathcal O\), \(J\equiv0\pmod\pi\).
5. *\(J\equiv-1\pmod3\).* Cubing is additive modulo \(3\) in any commutative ring. In \(\mathbb Z[\omega,e(1/p)]\) this gives
\[
\begin{aligned}
\tau(\psi)^3&\equiv\sum_x\psi(x)^3e\Bigl(\frac{3x}p\Bigr)\\
&=\sum_{x\not\equiv0}e\Bigl(\frac{3x}p\Bigr)\\
&=-1\pmod 3 .
\end{aligned}
\]
The ring \(\mathbb Z[\omega,e(1/p)]\) is a free \(\mathbb Z[\omega]\)-module with basis \(1,e(1/p),\ldots,e((p-2)/p)\), because the cyclotomic polynomial of degree \(p-1\) remains irreducible over \(K\) (the field \(\mathbb Q(\omega,e(1/p))\) has degree \(2(p-1)\)). Comparing coordinates, an element of \(\mathbb Z[\omega]\) that lies in \(3\mathbb Z[\omega,e(1/p)]\) lies in \(3\mathbb Z[\omega]\). So \(pJ\equiv-1\pmod 3\) in \(\mathbb Z[\omega]\), and \(J\equiv-1\pmod3\) as \(p\equiv1\pmod3\).

By steps 3 and 4, \(J=u\pi\) for a unit \(u\). By step 5 and \(\pi\equiv1\pmod 3\), \(u\equiv-1\pmod3\), so \(u=-1\) by Lemma 1.1. Hence \(g(\pi)^3=\tau(\psi)^3=-p\pi\), and \(G(\pi)^3=-p\pi/p^{3/2}=-\pi/|\pi|\).

In the remaining case \(\pi=-q\) with \(q\equiv2\pmod3\), so that \(\mathcal O/q\mathcal O=\mathbb F_{q^2}\) and \(N(\pi)=q^2\). For \(v\in\mathbb F_q^\times\),
\[
v^{(q^2-1)/3}=\bigl(v^{q-1}\bigr)^{(q+1)/3}=1,
\]
so \(\chi_\pi\) is a nontrivial character of \(\mathbb F_{q^2}^\times/\mathbb F_q^\times\). Complex conjugation induces the nontrivial automorphism of \(\mathbb F_{q^2}\), so \(\operatorname{Tr}(v)\) reduces modulo \(q\) to the trace from \(\mathbb F_{q^2}\) to \(\mathbb F_q\), and \(\operatorname{Tr}(v/\pi)=-\operatorname{Tr}(v)/q\). Decompose \(\mathbb F_{q^2}^\times\) into cosets \(c\,\mathbb F_q^\times\):
\[
g(\pi)=\sum_c\chi_\pi(c)\sum_{x\in\mathbb F_q^\times}e\Bigl(-\frac{x\operatorname{Tr}(c)}q\Bigr).
\]
The inner sum is \(q-1\) if \(\operatorname{Tr}(c)\equiv0\) and \(-1\) otherwise. The trace is a nonzero \(\mathbb F_q\)-linear form, as \(\operatorname{Tr}(1)=2\) and \(\operatorname{Tr}(\omega)=-1\) are not both divisible by \(q\). Its kernel is therefore a line, spanned by \(\lambda\), since \(\operatorname{Tr}(\lambda)=0\) and \(\lambda\not\equiv0\pmod q\). So exactly one coset, \(\lambda\mathbb F_q^\times\), has trace zero, and
\[
g(\pi)=q\,\chi_\pi(\lambda)-\sum_c\chi_\pi(c)=q\,\chi_\pi(\lambda).
\]
Thus \(G(\pi)=\chi_\pi(\lambda)\) and \(G(\pi)^3=1=-\pi/|\pi|\). \(\square\)

**Remark 3.4.** For a split prime, Proposition 3.1(d) and Theorem 3.3 determine \(G(\pi)\) up to the choice of one of the three cube roots of \(-\pi/|\pi|\). Writing \(G(\pi)=e(\theta_\pi)\), we get \(S_p/(2\sqrt p)=\cos2\pi\theta_\pi\). Heath-Brown and Patterson proved that the angles \(\theta_\pi\) are equidistributed modulo \(1\). Consequently \(\sum_{N(\pi)\le X}G(\pi)=o(X/\log X)\), and the first moment of this course is a term of lower order.

## 4. The theorem

Put
\[
c_*=\frac{(2\pi)^{2/3}}{3\,\Gamma(2/3)}=0.83818\ldots
\]

**Theorem 4.1.** As \(X\to\infty\),
\[
\begin{aligned}
\sum_{N(\pi)\le X}G(\pi)&=\frac65\,c_*\,\frac{X^{5/6}}{\log X}\\
&\quad+o\Bigl(\frac{X^{5/6}}{\log X}\Bigr),
\end{aligned}
\]
the sum running over all primary primes, including both conjugates above every split rational prime.

**Lemma 4.2 (the prime ideal theorem for \(K\)).** The number \(P(y)\) of primary primes \(\pi\) with \(N(\pi)\le y\) satisfies \(P(y)=y/\log y+o(y/\log y)\), and \(P(y)\ll y/\log y\) for \(y\ge2\).

**Proof.** By Lemma 1.2, \(P(y)=2\pi(y;3,1)+\pi(\sqrt y;3,2)\). Theorem 3.1 of the lesson on primes in progressions, for the fixed modulus \(3\), gives \(\theta(y;3,1)=y/2+o(y)\): its possible exceptional term involves \(y^{\beta_1}\) with a fixed \(\beta_1<1\). Partial summation gives \(\pi(y;3,1)=y/(2\log y)+o(y/\log y)\), and \(\pi(\sqrt y;3,2)\le\sqrt y\). \(\square\)

**Proposition 4.3 (the model).**
\[
\begin{aligned}
\sum_{N(\pi)\le X}N(\pi)^{-1/6}&=\frac65\,\frac{X^{5/6}}{\log X}\\
&\quad+o\Bigl(\frac{X^{5/6}}{\log X}\Bigr).
\end{aligned}
\]

**Proof.** By partial summation,
\[
\begin{aligned}
&\sum_{N(\pi)\le X}N(\pi)^{-1/6}\\
&=\frac{P(X)}{X^{1/6}}+\frac16\int_2^XP(y)\,y^{-7/6}\,dy .
\end{aligned}
\]
The first term is \(X^{5/6}/\log X+o(X^{5/6}/\log X)\) by Lemma 4.2. In the integral, Lemma 4.2 replaces \(P(y)\) by \(y/\log y\) with an error \(o(X^{5/6}/\log X)\) in total, and integration by parts gives
\[
\begin{aligned}
\int_2^X\frac{y^{-1/6}}{\log y}\,dy&=\frac65\,\frac{X^{5/6}}{\log X}\\
&\quad+O\Bigl(\frac{X^{5/6}}{\log^2X}\Bigr).
\end{aligned}
\]
The two contributions add up to \((1+\tfrac15)X^{5/6}/\log X\). \(\square\)

So Theorem 4.1 is equivalent to the comparison
\[
\begin{aligned}
&\sum_{N(\pi)\le X}\Bigl(G(\pi)-\frac{c_*}{N(\pi)^{1/6}}\Bigr)\\
&\qquad=o\Bigl(\frac{X^{5/6}}{\log X}\Bigr).\qquad(4.1)
\end{aligned}
\]
The function \(c_*N(\pi)^{-1/6}\) is the *model* for \(G(\pi)\). The course proves (4.1), on dyadic ranges \(X<N(\pi)\le2X\).

**Corollary 4.4.** (a)
\[
\begin{aligned}
&\sum_{N(\pi)\le X}G(\pi)\log N(\pi)\\
&\qquad=\frac65\,c_*X^{5/6}+o(X^{5/6}).
\end{aligned}
\]

(b) Summing over all rational primes,
\[
\sum_{p\le X}\frac{S_p}{2\sqrt p}=\frac35\,c_*\,\frac{X^{5/6}}{\log X}
+o\Bigl(\frac{X^{5/6}}{\log X}\Bigr),
\]
where \(\frac35c_*=(2\pi)^{2/3}/(5\,\Gamma(2/3))\).

**Proof.** (a) Let \(A(y)\) be the sum in Theorem 4.1. Partial summation gives
\[
\begin{aligned}
&\sum_{N(\pi)\le X}G(\pi)\log N(\pi)\\
&\qquad=A(X)\log X-\int_2^XA(y)\,\frac{dy}y .
\end{aligned}
\]
By Theorem 4.1, \(A(X)\log X=\frac65c_*X^{5/6}+o(X^{5/6})\) and \(|A(y)|\ll y^{5/6}/\log y\) for \(y\ge2\), so the integral is \(O(X^{5/6}/\log X)\).

(b) If \(p\not\equiv1\pmod3\), cubing permutes \(\mathbb F_p\) and \(S_p=\sum_xe(x/p)=0\). For \(p\equiv1\pmod3\), Proposition 3.2 gives \(S_p/(2\sqrt p)=(G(\pi)+G(\bar\pi))/2\). The primes \(-q\) with \(q^2\le X\) number at most \(\sqrt X\), and \(|G|=1\) at each of them. Hence the left side equals \(\frac12A(X)+O(\sqrt X)\). \(\square\)

**Remark 4.5 (normalizations).** The factor \(\frac12\) between the coefficients in Theorem 4.1 and Corollary 4.4(b) comes from the two primary primes above each split rational prime. In the paper of Dunn and Radziwiłł [DR], the asymptotic for the sum over primary primes, displayed after their equation (1.8), carries the coefficient \(\frac65c_*\), in agreement with Theorem 4.1. Their statement of Patterson's conjecture in Section 1.1 and their Theorem 1.1 attach that same coefficient to the rational sums of \(S_p/(2\sqrt p)\). For those sums the coefficient is half as large: the constant \(2(2\pi)^{2/3}/(5\Gamma(2/3))\) of their conjecture should be \((2\pi)^{2/3}/(5\Gamma(2/3))\), and the factor \(c_*\int W(x)x^{-1/6}dx\) in their Theorem 1.1 should be \(\frac12c_*\int W(x)x^{-1/6}dx\). Direct computation agrees with Corollary 4.4(b). Let \(R(X)\) be the sum of \(S_p/(2\sqrt p)\) over \(p\le X\), and let \(M(X)=c_*\sum p^{-1/6}\) over the primes \(p\le X\) with \(p\equiv1\pmod3\), the model behind Corollary 4.4(b). Computing \(S_p\) directly from its definition gives

- \(X=10^4\): \(R=122.9\), \(M=135.9\);
- \(X=10^5\): \(R=718.1\), \(M=722.9\);
- \(X=2\cdot10^5\): \(R=1160.2\), \(M=1208.2\).

At \(X=2\cdot10^5\) the square root of the number of primes \(p\equiv1\pmod3\) below \(X\), the size of a random fluctuation, is about \(95\). The doubled coefficient would predict \(R\approx2M\), about \(2416\) there.

**Theorem 4.6 (angular modes).** For every fixed integer \(\ell\),
\[
\begin{aligned}
&\sum_{N(\pi)\le X}\Bigl(\frac\pi{|\pi|}\Bigr)^{\ell}\Bigl(G(\pi)-\frac{c_*}{N(\pi)^{1/6}}\Bigr)\\
&\qquad=o_\ell\Bigl(\frac{X^{5/6}}{\log X}\Bigr),
\end{aligned}
\]
and for \(\ell\ne0\) the sum of \((\pi/|\pi|)^\ell G(\pi)\) over \(N(\pi)\le X\) is \(o_\ell(X^{5/6}/\log X)\).

**Corollary 4.7 (powers).** For every fixed integer \(k\) not divisible by \(3\),
\[
\begin{aligned}
\sum_{N(\pi)\le X}G(\pi)^k
&=\mathbf 1_{k=\pm1}\,\frac65\,c_*\,\frac{X^{5/6}}{\log X}\\
&\quad+o_k\Bigl(\frac{X^{5/6}}{\log X}\Bigr).
\end{aligned}
\]

Theorem 4.6 and Corollary 4.7 are proved in the last lesson, [*Angular modes and powers of Gauss sums*](angular-modes-and-powers-of-gauss-sums.md). Patterson also conjectured the bound \(o(X^{5/6}/\log X)\) for every fixed power \(k\notin\{0,\pm1\}\). Corollary 4.7 proves the cases \(3\nmid k\). For \(k=3m\) with \(m\ne0\), Theorem 3.3 gives \(G(\pi)^k=(-1)^m(\pi/|\pi|)^m\). The conjecture then concerns the angles of the primes themselves at the scale \(X^{5/6}/\log X\), which is beyond the methods of this course.

## 5. The route through the course

The comparison (4.1) is proved on the dyadic ranges \(X<N(\pi)\le2X\).

- *Large sieves for cubic characters* (lesson 2) collects the tools: lattice Poisson summation, the ordinary character large sieve, Heath-Brown's cubic large sieve, and Hecke \(L\)-functions of \(K\).
- *The level formula and Type I sums* (lesson 3) evaluates sums \(\sum_ra_r\sum_uG(ru)W(N(u)/U)\) with short \(r\) by the level Voronoi formula of Dunn and Radziwiłł. Its main term is exactly that of the model.
- *Character moments at two exceptional configurations* (lesson 4) and *Corrected dispersion* (lesson 5) bound bilinear sums \(\sum\alpha_a\beta_bG(ab)\). The square is opened and Poisson summation is applied; the frequencies that are cubes reproduce the square of the model and cancel against it.
- *An exact decomposition of the prime sum* (lesson 6) writes the prime sum as a combination of Type I and bilinear sums with independent coefficients. One configuration, a product of three primes of norm close to \(X^{1/3}\), admits no power saving and is controlled by the sparsity of the primes.
- *Bilinear sums and the sharp cutoff* (lesson 7) assembles the estimates, at Mellin heights up to \(X^{1/6+\rho}\), and proves Theorem 4.1.
- *Angular modes and powers of Gauss sums* (lesson 8) proves Theorem 4.6 and Corollary 4.7.

Three published theorems are used without proof in the programme. Each is stated in full where it is used:

- (N1) Heath-Brown's cubic large sieve, in the form of [DR], Theorem 9.1;
- (N2) the level Voronoi formula of Dunn and Radziwiłł, [DR], Proposition 5.3;
- (N3) prime number theorems for Hecke characters of \(K\) whose conductor is at most a power of \(\log x\), from the work of Thorner and Zaman and of Kaneko and Thorner.

## 6. Exercises

**6.1.** Compute \(G(-2)\) from the definition, and compare with Theorem 3.3.

**6.2.** Show that \(1+3\omega\) and \(-2-3\omega\) are the primary primes of norm \(7\). For \(\pi=1+3\omega\), find the residue of \(\omega\) modulo \(\pi\) in \(\{0,\ldots,6\}\), the values of the character \(\psi\) of Proposition 3.2 on \(\mathbb F_7^\times\), and the Jacobi sum \(J\). Check that \(J=-\pi\).

**6.3.** For \(p=7\) and \(\pi=1+3\omega\), compute \(S_7\), and determine which of the three cube roots of \(-\pi/|\pi|\) is \(G(\pi)\).

**6.4.** Let \(b\) be primary and squarefree, and \(h\in\mathcal O\). Prove that
\[
\sum_{v\bmod b}\chi_b(v)\,e\Bigl(\operatorname{Tr}\frac{hv}b\Bigr)=\overline{\chi_b(h)}\,g(b).
\]

**6.5.** Prove the identity \(P(y)=2\pi(y;3,1)+\pi(\sqrt y;3,2)\) used in Lemma 4.2, including the treatment of the prime above \(3\).

## 7. Solutions

**6.1.** Here \(\mathcal O/2\mathcal O=\mathbb F_4=\{0,1,\omega,\omega^2\}\) and \(N(-2)=4\), so \(\chi_{-2}(v)\equiv v\pmod2\): the character sends \(1,\omega,\omega^2\) to themselves. Since \(\operatorname{Tr}(v/(-2))=-\operatorname{Tr}(v)/2\) with \(\operatorname{Tr}(1)=2\) and \(\operatorname{Tr}(\omega)=\operatorname{Tr}(\omega^2)=-1\),
\[
\begin{aligned}
g(-2)&=1\cdot e(-1)+\omega\, e\bigl(\tfrac12\bigr)\\
&\quad+\omega^2e\bigl(\tfrac12\bigr)\\
&=1-\omega-\omega^2=2,
\end{aligned}
\]
so \(G(-2)=1\). Theorem 3.3 gives \(G(-2)=\chi_{-2}(\lambda)\), and \(\lambda=1+2\omega\equiv1\pmod2\), so again \(G(-2)=1\); also \(-(-2)/|-2|=1=G(-2)^3\).

**6.2.** An element \(a+b\omega\) is primary when \(a\equiv1\) and \(b\equiv0\pmod3\). Then \(a^2-ab+b^2=7\) forces \(|b|\le3\), and the solutions are \(1+3\omega\) and \(-2-3\omega=\overline{1+3\omega}\). From \(1+3\omega\equiv0\) we get \(\omega\equiv-3^{-1}\equiv-5\equiv2\pmod\pi\); indeed \(2^2+2+1=7\). The character is \(\psi(x)\equiv x^2\pmod 7\), read as a cube root of unity through \(1\mapsto1\), \(2\mapsto\omega\), \(4\mapsto\omega^2\):
\[
\begin{gathered}
\psi(1)=\psi(6)=1,\\
\psi(3)=\psi(4)=\omega,\\
\psi(2)=\psi(5)=\omega^2 .
\end{gathered}
\]
The terms \(\psi(x)\psi(1-x)\) for \(x=2,3,4,5,6\) are \(\omega^2,1,\omega^2,1,\omega^2\), so
\[
\begin{aligned}
J&=2+3\omega^2=2-3-3\omega\\
&=-(1+3\omega).
\end{aligned}
\]

**6.3.** The cubes modulo \(7\) of \(1,\ldots,6\) are \(1,1,6,1,6,6\), so \(S_7=1+6\cos(2\pi/7)=4.74094\ldots\) and \(\operatorname{Re}G(\pi)=S_7/(2\sqrt7)=0.89595\ldots\). The number \(-\pi/|\pi|=(\frac12-\frac{3\sqrt3}2i)/\sqrt7\) has argument \(-1.38067\ldots\). Its cube roots have arguments \(-0.46022\ldots\) and \(-0.46022\ldots\pm2\pi/3\), with cosines \(0.89595\ldots\), \(-0.06333\ldots\) and \(-0.83262\ldots\). So
\[
\begin{aligned}
&G(1+3\omega)=e^{-0.46022\ldots i}\\
&\qquad=0.89595\ldots-0.44414\ldots i .
\end{aligned}
\]

**6.4.** First let \(b=\pi\) be prime. If \(\pi\mid h\), the left side is \(\sum_v\chi_\pi(v)=0\), as is the right side. Otherwise the substitution \(v\mapsto h^{-1}v\) multiplies the sum by \(\chi_\pi(h^{-1})=\overline{\chi_\pi(h)}\) and turns it into \(g(\pi)\). For \(b=ac\) with coprime \(a,c\), write \(v=cx+ay\) as in Proposition 3.1(c). The left side becomes
\[
\begin{aligned}
&\chi_a(c)\chi_c(a)\sum_x\chi_a(x)e\Bigl(\operatorname{Tr}\frac{hx}a\Bigr)\\
&\qquad\cdot\sum_y\chi_c(y)e\Bigl(\operatorname{Tr}\frac{hy}c\Bigr).
\end{aligned}
\]
By induction this is \(\chi_a(c)\chi_c(a)\overline{\chi_a(h)\chi_c(h)}g(a)g(c)\), which equals \(\overline{\chi_b(h)}g(b)\) by the identity \(g(ac)=\chi_a(c)\chi_c(a)g(a)g(c)\) from the proof of Proposition 3.1(c).

**6.5.** Primary primes correspond to the prime ideals prime to \(3\), and \(N(\pi)\le y\) is a condition on the ideal. By Lemma 1.2, each prime \(p\equiv1\pmod3\) with \(p\le y\) gives two ideals of norm \(p\), and each prime \(q\equiv2\pmod3\) with \(q^2\le y\) gives one ideal of norm \(q^2\). The ideal \((\lambda)\) is not prime to \(3\) and is not counted, and there are no other prime ideals.

## Sources

- [OpenAI-023] OpenAI, *An unconditional first moment for cubic Gauss sums*, OpenAI Math Release preprint, 25 September 2026, Section 1 (the theorem, the conversion to rational primes, the history and the plan of proof), Section 2 (the Gauss-sum identities at its beginning) and Appendix A (the angular theorem and the powers). https://github.com/openai/math/tree/main/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026
- [DR] A. Dunn and M. Radziwiłł, *Bias in cubic Gauss sums: Patterson's conjecture*, arXiv:2109.07463v3 (2024), published in Ann. of Math. 200 (2024). Section 1 surveys the history from Kummer to Heath-Brown, and equation (1.8) is the cube identity of Theorem 3.3. https://arxiv.org/abs/2109.07463v3
