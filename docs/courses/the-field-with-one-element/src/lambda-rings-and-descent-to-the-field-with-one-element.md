# Λ-rings and descent to the field with one element

*Written by Claude Opus 5.5 (Anthropic), September 2026, revised October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session; the October revision links the AI Integrated Stacks Project citations and is self-checked by the writing AI. The October revision also corrects points found by GPT-6 Astra (OpenAI), Ultra, in a separate review session. Public domain (CC0).*

## Introduction

Let \(M\) be a monoid in the sense of *Commutative monoids and their spectra*: commutative, with \(1\) and with
\(0\). In the simplest geometry over the field with one element, \(M\) is an algebra over \(\mathbb F_1\), and the
monoid ring \(\mathbb Z[M]\) is its base change to the integers. For every prime \(p\) the map \(m\mapsto m^p\) is an
endomorphism of \(M\). So \(\mathbb Z[M]\) carries a ring endomorphism \(\psi_p\) for every prime \(p\), and these
endomorphisms commute. Modulo \(p\), the endomorphism \(\psi_p\) is the Frobenius map \(f\mapsto f^p\) of
\(\mathbb F_p[M]\). A ring that comes from a monoid therefore carries a commuting family of lifts of the Frobenius
maps.

[Borger 2009] turns this observation into a definition. The proposal is that such a family of Frobenius lifts,
defined in the right way for all rings, *is* the descent datum from \(\mathbb Z\) to \(\mathbb F_1\). An algebra
over \(\mathbb F_1\) is then a ring with this extra structure, and base change from \(\mathbb F_1\) to \(\mathbb Z\)
is the functor that forgets the structure. The right definition is that of a Λ-ring. [Borger 2009] describes it as
the notion of Λ-ring of Grothendieck's Riemann–Roch theory. It is tied to the ring of big Witt vectors.

The lesson has four parts.

1. Sections 1 and 2 introduce Frobenius lifts and construct the ring \(W(A)\) of big Witt vectors of a ring \(A\),
   with its Frobenius maps and its comonad structure. All proofs are given.
2. Section 3 defines a Λ-ring as a ring \(A\) with a compatible map \(A\to W(A)\). It proves that on a ring without
   torsion a Λ-structure is the same as a commuting family of Frobenius lifts (Theorem 3.5), that a non-zero Λ-ring
   has characteristic zero and a reduced Λ-ring has no torsion (Proposition 3.7), and that \(W\) is right adjoint to
   the forgetful functor from Λ-rings to rings (Theorem 3.11). Section 4 shows that Λ-rings are the λ-rings defined
   by λ-operations (Theorem 4.5).
3. Section 5 explains the dictionary of [Borger 2009] and tests it on \(\mathbb Z\), on monoid rings and on
   cyclotomic rings.
4. Section 6 shows how monoid schemes give Λ-schemes. It then proves, by elementary means, that a non-zero Λ-ring
   that is finite over \(\mathbb Z\) has a point over \(\mathbb F_1\) (Theorem 6.6) and that a Λ-ring of finite type
   has only finitely many such points (Proposition 6.10). It also proves that \(GL_n\) is not a group scheme over \(\mathbb F_1\) for \(n\ge2\) (Proposition 6.12). Section 7 lists, with exact locators, what is known about
   Λ-schemes of finite type and is not proved here.

**What is assumed.** Commutative rings, polynomial rings, quotients and localization; categories, functors and
adjoint functors. Section 5 uses monoids, their prime ideals and the monoid ring from *Commutative monoids and their
spectra*, and the Galois theory of cyclotomic fields. Section 6 uses schemes [Stacks], monoid schemes and their base
change from *Monoid schemes*, and three facts about number fields that are quoted from [Milne 2020]. The lesson
*Counting over finite fields and the limit q → 1* explains why the symmetric group should be the general linear
group over \(\mathbb F_1\); Example 5.6 returns to this.

Basic references are [Borger 2009], [Borger 2011] and, for the structure at a single prime,
[Bhatt–Scholze 2019, Section 2]. Result numbers of [Borger 2009] refer to the first arXiv version.

**Conventions.** Rings are commutative with \(1\). We write \(\mathbb N_+=\{1,2,3,\dots\}\). The letters \(p\) and
\(\ell\) denote prime numbers, and \(v_p(n)\) is the exponent of \(p\) in \(n\in\mathbb N_+\). For a ring
\(A\), \(A^{\mathbb N_+}\) is the ring of all sequences \((b_1,b_2,\dots)\) in \(A\), with componentwise operations.
A ring \(A\) is *torsion-free* if \(na=0\) with \(n\in\mathbb N_+\) and \(a\in A\) implies \(a=0\); this holds if and
only if \(A\) has no \(p\)-torsion for every prime \(p\). "Monoid" has the meaning above, morphisms of monoids
preserve \(0\) and \(1\), \(\operatorname{Hom}(M,N)\) is the set of morphisms of monoids, \(\mathbb F_1=\{0,1\}\) and
\(\mathbb F_{1^n}=\{0\}\cup\mu_n\). The monoid ring \(\mathbb Z[M]\) is the free abelian group on \(M\setminus\{0\}\)
with the product of \(M\); the zero of \(M\) is the zero of the ring.

## 1. Frobenius lifts

**Definition 1.1.** Let \(A\) be a ring and \(p\) a prime. A *Frobenius lift at \(p\)* on \(A\) is a ring
endomorphism \(\psi\colon A\to A\) such that \(\psi(x)-x^p\in pA\) for all \(x\in A\).

The ring \(A/pA\) has characteristic \(p\) or is zero, so \(x\mapsto x^p\) is a ring endomorphism of \(A/pA\), the
*Frobenius map*. The definition says that \(\psi\) induces the Frobenius map on \(A/pA\). If \(p\) is invertible in
\(A\), then \(pA=A\) and every endomorphism of \(A\) is a Frobenius lift at \(p\).

**Lemma 1.2 (generators suffice).** Let \(\psi\) be a ring endomorphism of \(A\), and let \(S\subseteq A\) generate
\(A\) as a ring. If \(\psi(s)-s^p\in pA\) for all \(s\in S\), then \(\psi\) is a Frobenius lift at \(p\).

*Proof.* The maps \(x\mapsto\psi(x)+pA\) and \(x\mapsto x^p+pA\) are ring homomorphisms \(A\to A/pA\); the second one
is, because the Frobenius map of \(A/pA\) is a ring homomorphism. The set on which two ring homomorphisms agree is a
subring. It contains \(S\), so it is \(A\). \(\square\)

**Example 1.3 (the integers).** The identity is the only ring endomorphism of \(\mathbb Z\). By Fermat's little
theorem \(x^p\equiv x\) modulo \(p\) for all integers \(x\), so the identity is a Frobenius lift at every prime. The
same holds for \(\mathbb Z[1/N]\) with \(N\in\mathbb N_+\) and for \(\mathbb Q\): the identity is the only
endomorphism, and \(\mathbb Z[1/N]/p\,\mathbb Z[1/N]\) is \(\mathbb F_p\) or \(0\).

**Example 1.4 (monoid rings).** Let \(M\) be a monoid. For \(n\in\mathbb N_+\) the map \(m\mapsto m^n\) is a
morphism of monoids \(M\to M\), because \(M\) is commutative. It induces a ring endomorphism
\[
\psi_n\colon\mathbb Z[M]\to\mathbb Z[M],\qquad \psi_n\Big(\sum_m c_m\,m\Big)=\sum_m c_m\,m^n .
\]
Clearly \(\psi_1=\mathrm{id}\) and \(\psi_m\psi_n=\psi_{mn}\). By Lemma 1.2, applied to the generating set \(M\),
the endomorphism \(\psi_p\) is a Frobenius lift at \(p\). Three cases to keep in mind:

- \(M=\mathbb F_1[x_1,\dots,x_r]\), the free monoid. Then \(\mathbb Z[M]=\mathbb Z[x_1,\dots,x_r]\) and
  \(\psi_n(x_i)=x_i^n\).
- \(M=\mathbb F_1[x^{\pm1}]\), the infinite cyclic group with a zero. Then \(\mathbb Z[M]=\mathbb Z[x,x^{-1}]\).
- \(M=\mathbb F_{1^n}\). Then \(\mathbb Z[M]=\mathbb Z[x]/(x^n-1)\), the group ring of \(\mu_n\).

**Example 1.5 (two extremes).** If \(A\) is a \(\mathbb Q\)-algebra, then \(pA=A\) for every \(p\), and every ring
endomorphism of \(A\) is a Frobenius lift at every prime. If \(A\) is an \(\mathbb F_p\)-algebra, then \(pA=0\) and
\(\ell A=A\) for \(\ell\neq p\). Then the only Frobenius lift at \(p\) is the Frobenius map itself, and every
endomorphism is a Frobenius lift at \(\ell\). For example, on \(A=\mathbb F_p\) the identity is a Frobenius lift at
every prime.

**Lemma 1.6 (quotients and subrings).** Let \(\psi\) be a Frobenius lift at \(p\) on \(A\).

(a) If \(I\) is an ideal with \(\psi(I)\subseteq I\), the endomorphism of \(A/I\) induced by \(\psi\) is a Frobenius
lift at \(p\).

(b) Let \(B\subseteq A\) be a subring with \(\psi(B)\subseteq B\). If \(pA\cap B=pB\), then the restriction of
\(\psi\) to \(B\) is a Frobenius lift at \(p\) on \(B\).

(c) The condition \(pA\cap B=pB\) holds in the following two cases. First: \(B\) is the set of all \(a\in A\) with
\(u(a)=v(a)\), for two ring homomorphisms \(u,v\colon A\to C\) into a ring \(C\) without \(p\)-torsion. Second:
\(A\) has no \(p\)-torsion and \(B=A^G\) is the ring of invariants of a group \(G\) that acts on \(A\) by ring
automorphisms.

*Proof.* (a) is clear. (b) For \(b\in B\) the element \(\psi(b)-b^p\) lies in \(pA\cap B=pB\). (c) Let \(a\in A\)
with \(pa\in B\). In the first case \(p\,(u(a)-v(a))=0\), so \(u(a)=v(a)\) and \(a\in B\). In the second case
\(p\,(ga-a)=0\) for all \(g\in G\), so \(ga=a\) and \(a\in B\). \(\square\)

**Example 1.7 (a stable subring on which the lift fails).** Let \(A=\mathbb Z[x]\) with \(\psi_n(x)=x^n\) as in
Example 1.4, and let \(B=\mathbb Z+2\,\mathbb Z[x]\), the subring of polynomials whose non-constant coefficients are
even. Then \(\psi_n(B)\subseteq B\) for all \(n\). But
\[
\psi_2(2x)-(2x)^2=-2x^2\notin 2B=2\,\mathbb Z+4\,\mathbb Z[x].
\]
So \(\psi_2\) restricted to \(B\) is not a Frobenius lift at \(2\). Here \(2x\in B\) and \(x\notin B\), so the
condition of Lemma 1.6(b) fails. A subring that is stable under the \(\psi_p\) need not inherit the Frobenius lifts.

**Example 1.8 (the Chebyshev lifts).** Let \(A=\mathbb Z[t,t^{-1}]\) with \(\psi_n(t)=t^n\), and let \(\sigma\) be
the automorphism with \(\sigma(t)=t^{-1}\). It commutes with all \(\psi_n\). We claim that the ring of invariants is
the polynomial ring \(\mathbb Z[x]\) in \(x=t+t^{-1}\). An element \(\sum_kc_kt^k\) is invariant if and only if
\(c_k=c_{-k}\) for all \(k\), so the invariants are spanned by \(1\) and the elements \(s_k=t^k+t^{-k}\), \(k\ge1\).
Put \(s_0=2\). Then \(s_1=x\) and \(s_{k+1}=x\,s_k-s_{k-1}\), so all \(s_k\) lie in \(\mathbb Z[x]\). The powers of
\(x\) are linearly independent, because \(x^k\) has highest term \(t^k\).

By Lemma 1.6, \(\psi_p\) restricts to a Frobenius lift at \(p\) on \(\mathbb Z[x]\), for every prime \(p\). These
lifts commute. They are given by \(\psi_n(x)=t^n+t^{-n}=D_n(x)\), where the polynomials \(D_n\) satisfy \(D_1=x\),
\(D_2=x^2-2\) and \(D_{n+1}=x\,D_n-D_{n-1}\). For example
\[
D_3=x^3-3x,\qquad D_5=x^5-5x^3+5x .
\]
So the ring \(\mathbb Z[x]\) carries two different commuting families of Frobenius lifts: \(x\mapsto x^p\) and
\(x\mapsto D_p(x)\). The second family is the Chebyshev family of [Borger 2009, §2.5].

**Example 1.9 (the Gaussian integers have no Frobenius lift at 2).** The ring endomorphisms of \(\mathbb Z[i]\) are
the identity and complex conjugation. Both induce the identity on \(\mathbb Z[i]/2\,\mathbb Z[i]\), because
\(\bar\imath-i=-2i\). The Frobenius map of \(\mathbb Z[i]/2\,\mathbb Z[i]\) sends \(i\) to \(i^2=-1\), and
\(-1\not\equiv i\) modulo \(2\,\mathbb Z[i]\). So \(\mathbb Z[i]\) has no Frobenius lift at \(2\). Corollary 6.7
shows that among the subrings of number fields that are finitely generated as \(\mathbb Z\)-modules, only
\(\mathbb Z\) has a Frobenius lift at every prime.

**Example 1.10 (lifts that do not commute).** On \(\mathbb Z[x]\) let \(\psi_2(x)=x^2\) and \(\psi_3(x)=x^3-3x\). By
Lemma 1.2 these are Frobenius lifts at \(2\) and at \(3\). They do not commute:
\[
\psi_2\psi_3(x)=x^6-3x^2,\qquad \psi_3\psi_2(x)=(x^3-3x)^2=x^6-6x^4+9x^2 .
\]
So commutation is a condition of its own.

A first guess for the structure that a ring over \(\mathbb F_1\) should carry is a commuting family of Frobenius
lifts, one for each prime. Example 1.5 shows that this guess cannot be right for rings with torsion: on an
\(\mathbb F_p\)-algebra the condition at the prime \(p\) carries no information, because the lift must be the
Frobenius map itself. The congruence \(\psi(x)\equiv x^p\) modulo \(p\)
says that \(\psi(x)-x^p=p\,y\) for some \(y\), and when \(A\) has \(p\)-torsion the element \(y\) is not determined.
The definition that works for all rings makes the elements \(y\) part of the structure. The tool for this is the
ring of Witt vectors.

## 2. The big Witt vectors

### Witt vectors and ghost components

**Definition 2.1.** For \(n\in\mathbb N_+\) the *\(n\)-th Witt polynomial* is
\[
w_n=\sum_{d\mid n}d\,x_d^{\,n/d},
\]
a polynomial with integer coefficients in the variables \(x_d\), \(d\mid n\). So
\[
w_1=x_1,\quad w_2=x_1^2+2x_2,\quad w_3=x_1^3+3x_3,\quad w_4=x_1^4+2x_2^2+4x_4,\quad w_p=x_1^p+p\,x_p .
\]
For a ring \(A\) let \(W(A)\) be the set \(A^{\mathbb N_+}\) of sequences \(a=(a_1,a_2,\dots)\). Its elements are
called *Witt vectors* (more precisely, big Witt vectors), and \(a_n\) is the *\(n\)-th Witt component* of \(a\). The
*ghost map* is
\[
w\colon W(A)\to A^{\mathbb N_+},\qquad w(a)=(w_1(a),w_2(a),\dots),
\]
and \(w_n(a)\) is the *\(n\)-th ghost component* of \(a\). A ring homomorphism \(f\colon A\to B\) induces the map
\(W(f)\colon W(A)\to W(B)\) that applies \(f\) to every Witt component. Since the \(w_n\) have integer coefficients,
\(w_n(W(f)(a))=f(w_n(a))\).

As a set, \(W(A)\) is just the set of sequences. The point of the construction is a ring structure on \(W(A)\),
different from the componentwise one, for which the ghost map is a ring homomorphism.

**Lemma 2.2.** If \(A\) is torsion-free, the ghost map is injective. If \(A\) is a \(\mathbb Q\)-algebra, it is
bijective.

*Proof.* We have \(w_n(a)=n\,a_n+r_n\), where \(r_n\) is a polynomial in the components \(a_d\) with \(d\mid n\) and
\(d < n\). So \(w(a)\) determines \(a_1,a_2,\dots\) one after the other when multiplication by \(n\) is injective on
\(A\) for all \(n\), and every sequence of ghost components is reached when every \(n\) is invertible in \(A\).
\(\square\)

**Lemma 2.3.** Let \(x,y\in A\) and \(k\ge1\). If \(x\equiv y\) modulo \(p^kA\), then \(x^p\equiv y^p\) modulo
\(p^{k+1}A\). Hence \(x\equiv y\) modulo \(pA\) implies \(x^{p^j}\equiv y^{p^j}\) modulo \(p^{j+1}A\) for all
\(j\ge0\).

*Proof.* Write \(x=y+p^kz\) and expand \((y+p^kz)^p-y^p\) by the binomial theorem. The terms with \(1\le i\le p-1\)
are \(\binom pi\,y^{p-i}p^{ki}z^i\); they are divisible by \(p\cdot p^k\). The last term is \(p^{kp}z^p\), and
\(kp\ge k+1\). \(\square\)

The next lemma, Dwork's lemma, describes the image of the ghost map.

**Lemma 2.4 (Dwork's lemma).** Let \(A\) be a ring, and suppose that for every prime \(p\) a Frobenius lift
\(\varphi_p\) at \(p\) on \(A\) is given. For a sequence \(b=(b_n)\in A^{\mathbb N_+}\) the following are
equivalent.

(i) \(b=w(a)\) for some \(a\in W(A)\).

(ii) \(b_{pn}\equiv\varphi_p(b_n)\) modulo \(p^{v_p(n)+1}A\), for every prime \(p\) and every \(n\in\mathbb N_+\).

Neither torsion-freeness of \(A\) nor commutation of the \(\varphi_p\) is assumed.

*Proof.* We first show that for all \(a\in W(A)\), all primes \(p\) and all \(n\in\mathbb N_+\)
\[
w_{pn}(a)\equiv\varphi_p(w_n(a))\pmod{p^{v_p(n)+1}A}. \tag{2.1}
\]
By definition \(w_{pn}(a)=\sum_{d\mid pn}d\,a_d^{\,pn/d}\). If \(d\) divides \(pn\) but not \(n\), then
\(v_p(d)=v_p(n)+1\), so the term \(d\,a_d^{\,pn/d}\) lies in \(p^{v_p(n)+1}A\). Now let \(d\) divide \(n\), and write
\(n/d=p^jk\) with \(p\nmid k\), so that \(j=v_p(n)-v_p(d)\). Since \(\varphi_p(a_d)\equiv a_d^{\,p}\) modulo \(pA\),
Lemma 2.3 gives \(\varphi_p(a_d)^{p^j}\equiv (a_d^{\,p})^{p^j}\) modulo \(p^{j+1}A\). We raise this to the power
\(k\) and multiply by \(d\), which is divisible by \(p^{v_p(d)}\):
\[
d\,\varphi_p(a_d)^{n/d}\equiv d\,a_d^{\,pn/d}\pmod{p^{v_p(n)+1}A}.
\]
Summing over the divisors \(d\) of \(n\) gives (2.1), because
\(\varphi_p(w_n(a))=\sum_{d\mid n}d\,\varphi_p(a_d)^{n/d}\). With (ii) read for \(b=w(a)\), this proves that (i)
implies (ii).

Conversely let \(b\) satisfy (ii). We construct \(a_1,a_2,\dots\) one after the other so that \(w_n(a)=b_n\) for all
\(n\). Put \(a_1=b_1\). Let \(n>1\) and suppose that \(a_d\) is constructed for all \(d < n\), with \(w_d(a)=b_d\) for
\(d < n\); this makes sense, because \(w_d\) involves only components whose index divides \(d\). Put
\[
c=b_n-\sum_{d\mid n,\ d < n}d\,a_d^{\,n/d}.
\]
We must find \(a_n\) with \(n\,a_n=c\). Let \(p\) be a prime divisor of \(n\) and \(n=pk\). Apply (2.1), with the
index \(k\), to the Witt vector \(a'=(a_1,\dots,a_{n-1},0,0,\dots)\): we get \(w_n(a')\equiv\varphi_p(w_k(a'))\)
modulo \(p^{v_p(n)}A\). Here \(w_n(a')=b_n-c\) and \(w_k(a')=b_k\). By (ii), \(\varphi_p(b_k)\equiv b_n\) modulo
\(p^{v_p(n)}A\). Hence \(c\in p^{v_p(n)}A\), and this holds for every prime divisor \(p\) of \(n\). If \(r\) and
\(s\) are coprime integers and \(c\in rA\cap sA\), then \(c\in rsA\): write \(1=ur+vs\); then \(c=urc+vsc\), and
both terms lie in \(rsA\). So \(c\in nA\), and \(a_n\) exists. \(\square\)

### The ring structure

**Theorem 2.5.** There is exactly one way to define, for every ring \(A\), a ring structure on the set \(W(A)\) such
that

1. \(W(f)\) is a ring homomorphism for every ring homomorphism \(f\colon A\to B\);
2. the ghost map \(w\colon W(A)\to A^{\mathbb N_+}\) is a ring homomorphism for every ring \(A\).

The zero of \(W(A)\) is \((0,0,0,\dots)\) and the one is \((1,0,0,\dots)\).

*Proof.* Let \(R=\mathbb Z[x_n,y_n:n\in\mathbb N_+]\), a polynomial ring in two sequences of variables, and let
\(x=(x_n)\) and \(y=(y_n)\) in \(W(R)\). Let \(\varphi_p\) be the ring endomorphism of \(R\) that raises every
variable to its \(p\)-th power. It is a Frobenius lift at \(p\) by Lemma 1.2.

*Step 1: universal sum, product and negative.* By Dwork's lemma the sequences \(w(x)\) and \(w(y)\) satisfy (ii).
Since \(\varphi_p\) is a ring homomorphism, the sequences \(w(x)+w(y)\), \(w(x)\,w(y)\) and \(-w(x)\) satisfy (ii) as
well. So there are \(s,m,\nu\in W(R)\) with
\[
w(s)=w(x)+w(y),\qquad w(m)=w(x)\,w(y),\qquad w(\nu)=-w(x).
\]
They are unique by Lemma 2.2, because \(R\) is torsion-free. Their components are polynomials with integer
coefficients in the \(x_n\) and \(y_n\).

*Step 2: definition.* Let \(A\) be a ring and \(a,b\in W(A)\). Let \(g\colon R\to A\) be the ring homomorphism with
\(g(x_n)=a_n\) and \(g(y_n)=b_n\). Define
\[
a+b=W(g)(s),\qquad ab=W(g)(m),\qquad -a=W(g)(\nu).
\]
In other words, substitute the components of \(a\) and \(b\) into the polynomials \(s_n\), \(m_n\), \(\nu_n\). These
operations commute with \(W(f)\) for every ring homomorphism \(f\colon A\to B\), because \(f\circ g\) is the
homomorphism that belongs to \(W(f)(a)\) and \(W(f)(b)\). Moreover
\(w(a+b)=g(w(s))=g(w(x)+w(y))=w(a)+w(b)\), where \(g\) is applied to each component, and in the same way
\(w(ab)=w(a)\,w(b)\) and \(w(-a)=-w(a)\).

*Step 3: the ring axioms.* Each axiom is an identity that involves at most three elements \(a,b,c\in W(A)\). Let
\(R'=\mathbb Z[x_n,y_n,z_n:n\in\mathbb N_+]\) and let \(g'\colon R'\to A\) send the three universal vectors
\(x,y,z\) to \(a,b,c\). Since \(W(g')\) commutes with the operations, it is enough to prove the axiom for \(x,y,z\)
in \(W(R')\). The ring \(R'\) is torsion-free, so the ghost map of \(W(R')\) is injective, and by Step 2 it carries
the operations of \(W(R')\) to the componentwise operations of the ring \(R'^{\,\mathbb N_+}\), where the axioms hold.
For example \(w((x+y)+z)=w(x)+w(y)+w(z)=w(x+(y+z))\), hence \((x+y)+z=x+(y+z)\). The neutral elements are as stated,
because \(w(0,0,\dots)=(0,0,\dots)\) and \(w(1,0,0,\dots)=(1,1,\dots)\).

*Step 4: uniqueness.* Let \(\oplus\) and \(\otimes\) be the operations of a second family of ring structures with
properties 1 and 2. Then \(w(x\oplus y)=w(x)+w(y)=w(s)\) in \(R^{\mathbb N_+}\), so \(x\oplus y=s\). For
\(a,b\in W(A)\) and \(g\) as in Step 2 we get \(a\oplus b=W(g)(x\oplus y)=W(g)(s)=a+b\). The same argument applies
to \(\otimes\). \(\square\)

From now on \(W(A)\) denotes this ring, the *ring of big Witt vectors* of \(A\). In a \(p\)-typical form the
construction goes back to Witt; see [Borger 2011, §1.15].

**Example 2.6 (the first components).** The proof finds the components of a sum and of a product by solving the
ghost equations one after the other. From \(w_1\) and \(w_2\) one gets
\[
(a+b)_1=a_1+b_1,\qquad (a+b)_2=a_2+b_2-a_1b_1,
\]
\[
(ab)_1=a_1b_1,\qquad (ab)_2=a_1^2b_2+a_2b_1^2+2a_2b_2,\qquad (-a)_1=-a_1,\qquad (-a)_2=-a_2-a_1^2 .
\]
So addition is not componentwise, and the negative is not the componentwise negative. For a prime \(p\) the
equation \(w_p=x_1^p+p\,x_p\) gives
\[
(a+b)_p=a_p+b_p+\frac{a_1^p+b_1^p-(a_1+b_1)^p}{p},\qquad (ab)_p=a_1^p\,b_p+a_p\,b_1^p+p\,a_p\,b_p . \tag{2.2}
\]
The fraction stands for the polynomial \(-\sum_{i=1}^{p-1}\tfrac1p\binom pi a_1^ib_1^{p-i}\), which has integer
coefficients. These formulas are identities between the polynomials \(s_n\) and \(m_n\) of the proof, so they hold in
\(W(A)\) for every ring \(A\). Over the torsion-free ring \(R\) they follow from \(w_p(s)=w_p(x)+w_p(y)\) and
\(w_p(m)=w_p(x)\,w_p(y)\), together with \(s_1=x_1+y_1\) and \(m_1=x_1y_1\).

The argument of Steps 3 and 4 will be used several times. We record it.

**Lemma 2.7 (the universal case).**

(a) If \(A\) is torsion-free, then the additive group of \(W(A)\) is torsion-free. Hence the rings \(W(W(A))\) and
\(W(W(W(A)))\) are torsion-free too, and all their ghost maps are injective.

(b) Let \(A\) be a ring, \(a^{(1)},\dots,a^{(k)}\in W(A)\) and \(c_1,\dots,c_l\in A\). Let \(R\) be the polynomial
ring over \(\mathbb Z\) in the variables \(x^{(i)}_n\) (\(1\le i\le k\), \(n\in\mathbb N_+\)) and \(X_1,\dots,X_l\),
and let \(x^{(i)}=(x^{(i)}_n)_n\in W(R)\). Then \(R\) is torsion-free, raising every variable to its \(p\)-th power
is a Frobenius lift \(\varphi_p\) at \(p\) on \(R\), and the ring homomorphism \(g\colon R\to A\) with
\(g(x^{(i)}_n)=a^{(i)}_n\) and \(g(X_j)=c_j\) satisfies \(W(g)(x^{(i)})=a^{(i)}\).

*Proof.* (a) The ghost map is an injective homomorphism from the additive group of \(W(A)\) into the torsion-free
group \(A^{\mathbb N_+}\). (b) is clear; the statement on \(\varphi_p\) is Lemma 1.2. \(\square\)

We use the lemma as follows. Suppose that two constructions attach to every ring \(A\), and to every choice of
finitely many elements of \(W(A)\) and of \(A\), an element of \(A\), of \(W(A)\), of \(W(W(A))\) or of
\(W(W(W(A)))\), and that both constructions commute with ring homomorphisms. If the two results agree whenever
\(A\) is torsion-free, they agree for all \(A\): they agree for the universal elements over \(R\), and the map
induced by \(g\) carries the universal results to the results over \(A\). Over a torsion-free ring, two Witt
vectors agree as soon as their ghost components agree. We refer to this as *reduction to ghost components*.

**Lemma 2.8 (Teichmüller representatives).** For \(x\in A\) put \([x]=(x,0,0,\dots)\in W(A)\). Then
\(w_n([x])=x^n\) for all \(n\). For \(x,y\in A\), \(a\in W(A)\) and a ring homomorphism \(f\colon A\to B\):
\[
[x]\,[y]=[xy],\qquad [0]=0,\qquad [1]=1,\qquad (a\cdot[x])_n=a_n\,x^n,\qquad W(f)([x])=[f(x)].
\]

*Proof.* The formula for \(w_n([x])\) and the last formula follow from the definitions. For the others we reduce to
ghost components: \(w_n(a)\,x^n=\sum_{d\mid n}d\,a_d^{\,n/d}x^n=\sum_{d\mid n}d\,(a_dx^d)^{n/d}\) is the \(n\)-th
ghost component of the vector \((a_nx^n)_n\). For \(a=[y]\) this gives \([y]\,[x]=[yx]\). \(\square\)

The map \(x\mapsto[x]\) is multiplicative. It is not additive: \([1]+[1]=2\) has the components
\((2,-1,-2,-4,\dots)\), see Exercise 8.1.

**Example 2.9 (rational algebras, and the integers).** (a) If \(A\) is a \(\mathbb Q\)-algebra, the ghost map is an
isomorphism of rings \(W(A)\to A^{\mathbb N_+}\), by Lemma 2.2. Over \(\mathbb Q\) nothing is gained.

(b) Take \(A=\mathbb Z\) and \(\varphi_p=\mathrm{id}\) in Dwork's lemma. The ghost map identifies \(W(\mathbb Z)\)
with the subring of \(\mathbb Z^{\mathbb N_+}\) of all sequences \(b\) with
\[
b_{pn}\equiv b_n\pmod{p^{v_p(n)+1}}\qquad\text{for all primes }p\text{ and all }n\in\mathbb N_+ .
\]
The constant sequences satisfy this; they are the images of the integers. The sequence \((1,3,1,3,\dots)\) is the
image of \((1,1,0,0,\dots)\), and \((2,4,8,16,\dots)\) is the image of \([2]\). The sequence \((0,1,0,1,\dots)\) is
not in the image, because \(b_2\not\equiv b_1\) modulo \(2\).

### Frobenius maps and the comonad structure

**Theorem 2.10 (Frobenius maps).** For every \(n\in\mathbb N_+\) there is exactly one family of maps
\(F_n\colon W(A)\to W(A)\), one for each ring \(A\), that commutes with the maps \(W(f)\) for all ring homomorphisms
\(f\) and satisfies
\[
w_m(F_n(a))=w_{mn}(a)\qquad(m\in\mathbb N_+,\ a\in W(A)). \tag{2.3}
\]
Each \(F_n\) is a ring homomorphism, \(F_1=\mathrm{id}\), \(F_mF_n=F_{mn}\) and \(F_n([x])=[x^n]\). For every prime
\(p\)
\[
F_p(a)-a^p\in p\,W(A)\qquad(a\in W(A)). \tag{2.4}
\]
So \(F_p\) is a Frobenius lift at \(p\) on the ring \(W(A)\), for every ring \(A\), and these lifts commute.

*Proof.* Let \(R=\mathbb Z[x_1,x_2,\dots]\) with the Frobenius lifts \(\varphi_p\) of Lemma 2.7, and
\(x=(x_1,x_2,\dots)\in W(R)\). Fix \(n\). By (2.1), applied to the index \(mn\), we have
\(w_{pmn}(x)\equiv\varphi_p(w_{mn}(x))\) modulo \(p^{v_p(mn)+1}R\), hence modulo \(p^{v_p(m)+1}R\). So the sequence
\((w_{mn}(x))_m\) satisfies condition (ii) of Dwork's lemma, and there is exactly one \(F_n(x)\in W(R)\) with
\(w_m(F_n(x))=w_{mn}(x)\) for all \(m\). For a ring \(A\) and \(a\in W(A)\) let \(g\colon R\to A\) be the
homomorphism with \(g(x_k)=a_k\), and define \(F_n(a)=W(g)(F_n(x))\). This family commutes with the maps \(W(f)\)
and satisfies (2.3). Any other such family agrees with it on torsion-free rings by Lemma 2.2, and then on all rings
by Lemma 2.7.

The remaining identities commute with ring homomorphisms, so we reduce to ghost components. We have
\(w_m(F_n(a+b))=w_{mn}(a)+w_{mn}(b)=w_m(F_n(a)+F_n(b))\), and in the same way for products and for the element
\(1\). Further \(w_k(F_mF_n(a))=w_{km}(F_n(a))=w_{kmn}(a)=w_k(F_{mn}(a))\), \(w_m(F_1(a))=w_m(a)\), and
\(w_m(F_n([x]))=x^{mn}=w_m([x^n])\).

It remains to prove (2.4). Since \(W(g)\) is a ring homomorphism, it is enough to find \(c\in W(R)\) with
\(F_p(x)-x^p=p\,c\) for the universal vector \(x\). The ghost components of \(F_p(x)-x^p\) are
\(w_{pn}(x)-w_n(x)^p\). By (2.1) and the definition of a Frobenius lift,
\(w_{pn}(x)\equiv\varphi_p(w_n(x))\equiv w_n(x)^p\) modulo \(pR\). As \(R\) is torsion-free, there are unique
\(c_n\in R\) with
\[
p\,c_n=w_{pn}(x)-w_n(x)^p .
\]
We claim that the sequence \((c_n)\) satisfies condition (ii) of Dwork's lemma. Then \((c_n)=w(c)\) for some
\(c\in W(R)\), and the Witt vectors \(p\,c\) and \(F_p(x)-x^p\) have the same ghost components, so they are equal.

Let \(q\) be a prime and \(n\in\mathbb N_+\), and put \(e=v_q(n)+1\). Then
\[
p\,\big(c_{qn}-\varphi_q(c_n)\big)=\big(w_{pqn}(x)-\varphi_q(w_{pn}(x))\big)-\big(w_{qn}(x)^p-\varphi_q(w_n(x))^p\big).
\]
Let \(q\neq p\). The first bracket lies in \(q^eR\) by (2.1) for the prime \(q\) and the index \(pn\), since
\(v_q(pn)=v_q(n)\). The second bracket lies in \(q^eR\), because \(w_{qn}(x)\equiv\varphi_q(w_n(x))\) modulo
\(q^eR\) by (2.1). As \(p\) is invertible modulo \(q^e\), we get \(c_{qn}-\varphi_q(c_n)\in q^eR\). Let \(q=p\). The
first bracket lies in \(p^{e+1}R\) by (2.1) for the index \(pn\). By (2.1) for the index \(n\) we have
\(w_{pn}(x)\equiv\varphi_p(w_n(x))\) modulo \(p^eR\), so the second bracket lies in \(p^{e+1}R\) by Lemma 2.3. Hence
\(p\,(c_{pn}-\varphi_p(c_n))\in p^{e+1}R\), and \(c_{pn}-\varphi_p(c_n)\in p^eR\) because \(R\) is torsion-free. The
lifts \(F_p\) commute because \(F_pF_q=F_{pq}=F_qF_p\). \(\square\)

For example \(F_n(a)_1=w_n(a)\) by (2.3) with \(m=1\): the first Witt component of \(F_n(a)\) is the \(n\)-th ghost
component of \(a\). Further \(F_2(a)_2=2a_4-a_2^2-2a_1^2a_2\), which is congruent to \(a_2^2\) modulo \(2\) but is not
equal to it.

**Theorem 2.11 (the comonad structure).** There is exactly one family of maps
\(\Delta_A\colon W(A)\to W(W(A))\), one for each ring \(A\), that commutes with ring homomorphisms and satisfies
\[
w_n(\Delta_A(a))=F_n(a)\qquad(n\in\mathbb N_+,\ a\in W(A)). \tag{2.5}
\]
Here \(w_n\) is the \(n\)-th ghost component on \(W(W(A))\), with values in \(W(A)\). Each \(\Delta_A\) is a ring
homomorphism, and the following hold.

(a) \(w_1\circ\Delta_A=\mathrm{id}_{W(A)}\) and \(W(w_1)\circ\Delta_A=\mathrm{id}_{W(A)}\), where \(W(w_1)\) is
induced by the ring homomorphism \(w_1\colon W(A)\to A\).

(b) \(W(\Delta_A)\circ\Delta_A=\Delta_{W(A)}\circ\Delta_A\) as maps \(W(A)\to W(W(W(A)))\).

(c) \(\Delta_A([x])=[[x]]\) for \(x\in A\), the Teichmüller representative of \([x]\in W(A)\).

In the language of categories, \((W,w_1,\Delta)\) is a comonad on the category of rings.

*Proof.* Let \(R=\mathbb Z[x_1,x_2,\dots]\) and \(x\in W(R)\) as before. The ring \(W(R)\) is torsion-free by Lemma
2.7, and \(F_p\) is a Frobenius lift at \(p\) on \(W(R)\) by Theorem 2.10. We apply Dwork's lemma to the ring
\(W(R)\), with the lifts \(F_p\), and to the sequence \((F_n(x))_n\) of elements of \(W(R)\). Condition (ii) holds
with equality, because \(F_{pn}(x)=F_p(F_n(x))\). So there is exactly one \(\Delta(x)\in W(W(R))\) with
\(w_n(\Delta(x))=F_n(x)\) for all \(n\). For a ring \(A\) and \(a\in W(A)\), with \(g\colon R\to A\) as in the last
proof, define \(\Delta_A(a)=W(W(g))(\Delta(x))\). This family commutes with ring homomorphisms, and
\(w_n(\Delta_A(a))=W(g)(w_n(\Delta(x)))=W(g)(F_n(x))=F_n(a)\). Uniqueness follows as in Theorem 2.10.

All remaining statements are identities between maps that commute with ring homomorphisms. By Lemma 2.7 we may
assume that \(A\) is torsion-free; then all ghost maps that occur are injective.

\(\Delta_A\) is a ring homomorphism, because \(w\circ\Delta_A=(F_n)_n\) is a ring homomorphism
\(W(A)\to W(A)^{\mathbb N_+}\) and \(w\) is an injective ring homomorphism.

(a) \(w_1\circ\Delta_A=F_1=\mathrm{id}\). For the second identity we compare ghost components. The maps \(w_n\)
commute with the ring homomorphism \(w_1\colon W(A)\to A\), so
\(w_n\circ W(w_1)\circ\Delta_A=w_1\circ w_n\circ\Delta_A=w_1\circ F_n=w_n\), by (2.5) and (2.3).

(b) First, \(\Delta_A\circ F_n=F_n\circ\Delta_A\), where \(F_n\) on the right is the Frobenius map of \(W(W(A))\):
indeed \(w_m\circ\Delta_A\circ F_n=F_m\circ F_n=F_{mn}\) and \(w_m\circ F_n\circ\Delta_A=w_{mn}\circ\Delta_A=F_{mn}\).
Now the maps \(w_n\) commute with the ring homomorphism \(\Delta_A\), so
\(w_n\circ W(\Delta_A)\circ\Delta_A=\Delta_A\circ w_n\circ\Delta_A=\Delta_A\circ F_n\), and
\(w_n\circ\Delta_{W(A)}\circ\Delta_A=F_n\circ\Delta_A\) by (2.5) for the ring \(W(A)\). The two are equal.

(c) \(w_n(\Delta_A([x]))=F_n([x])=[x^n]=[x]^n=w_n([[x]])\). \(\square\)

## 3. Λ-rings

### The definition and the Adams operations

**Definition 3.1.** A *Λ-structure* on a ring \(A\) is a ring homomorphism \(\alpha\colon A\to W(A)\) such that

- (Λ1) \(w_1\circ\alpha=\mathrm{id}_A\), and
- (Λ2) \(W(\alpha)\circ\alpha=\Delta_A\circ\alpha\) as maps \(A\to W(W(A))\).

A *Λ-ring* is a ring with a Λ-structure. A *morphism of Λ-rings*, or *Λ-map*, from \((A,\alpha)\) to \((B,\beta)\)
is a ring homomorphism \(f\colon A\to B\) with \(W(f)\circ\alpha=\beta\circ f\). The set of Λ-maps is written
\(\operatorname{Hom}_\Lambda(A,B)\). For \(n\in\mathbb N_+\) and a prime \(p\) we define two maps \(A\to A\): the map
\(\psi_n=w_n\circ\alpha\), and the map \(\delta_p\) that sends \(x\) to the \(p\)-th Witt component of
\(\alpha(x)\). The \(\psi_n\) are the *Adams operations* of the Λ-ring.

In the language of categories, a Λ-ring is a coalgebra for the comonad \(W\). Condition (Λ1) says that the first
Witt component of \(\alpha(x)\) is \(x\). [Borger 2009, §1.1] defines a Λ-structure on a space as an action of a
Witt vector monad, and notes that for an affine scheme \(\operatorname{Spec}A\) this is a Λ-ring structure on \(A\)
"in the usual sense"; Theorem 4.5 compares Definition 3.1 with the definition by λ-operations.

**Theorem 3.2.** Let \((A,\alpha)\) be a Λ-ring.

(a) Each \(\psi_n\) is a ring endomorphism of \(A\), \(\psi_1=\mathrm{id}\) and \(\psi_m\psi_n=\psi_{mn}\). In
particular the \(\psi_n\) commute with each other.

(b) For every prime \(p\) and every \(x\in A\)
\[
\psi_p(x)=x^p+p\,\delta_p(x). \tag{3.1}
\]
So \(\psi_p\) is a Frobenius lift at \(p\).

(c) A Λ-map \(f\) commutes with the operations: \(f\circ\psi_n=\psi_n\circ f\) and \(f\circ\delta_p=\delta_p\circ f\).

*Proof.* (a) \(\psi_n\) is a composite of ring homomorphisms, and \(\psi_1=\mathrm{id}\) is (Λ1). The maps \(w_n\)
commute with the ring homomorphism \(\alpha\colon A\to W(A)\), that is, \(\alpha\circ w_n=w_n\circ W(\alpha)\) on
\(W(A)\). Hence, by (Λ2), (2.5) and (2.3),
\[
\psi_m\circ\psi_n=w_m\circ\alpha\circ w_n\circ\alpha=w_m\circ w_n\circ W(\alpha)\circ\alpha
=w_m\circ w_n\circ\Delta_A\circ\alpha=w_m\circ F_n\circ\alpha=w_{mn}\circ\alpha=\psi_{mn}.
\]
(b) \(w_p=x_1^p+p\,x_p\), and the first component of \(\alpha(x)\) is \(x\). (c) Apply \(w_n\), or take the \(p\)-th
Witt component, in the equation \(W(f)(\alpha(x))=\beta(f(x))\). \(\square\)

**Proposition 3.3 (rules for \(\delta_p\)).** In a Λ-ring, for all \(x,y\) and every prime \(p\):
\[
\delta_p(0)=\delta_p(1)=0,\qquad \delta_p(x+y)=\delta_p(x)+\delta_p(y)+\frac{x^p+y^p-(x+y)^p}{p},
\]
\[
\delta_p(xy)=x^p\,\delta_p(y)+y^p\,\delta_p(x)+p\,\delta_p(x)\,\delta_p(y).
\]
The fraction is the polynomial with integer coefficients of Example 2.6.

*Proof.* \(\alpha\) is a ring homomorphism, so \(\alpha(x+y)=\alpha(x)+\alpha(y)\),
\(\alpha(xy)=\alpha(x)\,\alpha(y)\), \(\alpha(0)=(0,0,\dots)\) and \(\alpha(1)=(1,0,0,\dots)\). Take \(p\)-th Witt
components and use (2.2) with \(a_1=x\) and \(b_1=y\). \(\square\)

**Remark 3.4 (one prime at a time).** Fix a prime \(p\). A ring with one map \(\delta\) that satisfies the rules of
Proposition 3.3 is called a \(\delta\)-ring. Then \(x\mapsto x^p+p\,\delta(x)\) is a Frobenius lift at \(p\), and on a
ring without \(p\)-torsion every Frobenius lift at \(p\) comes from exactly one such \(\delta\). *Reference:*
[Bhatt–Scholze 2019, Definition 2.1 and Remark 2.2]; the opening of Section 2 there refers to Joyal for the notion. A Λ-ring
carries such a structure for every prime, and by Theorem 3.2(a) the Frobenius lifts for different primes commute.
The maps \(\delta_p\) are the elements \(y\) asked for at the end of Section 1.

### Rings without torsion

**Theorem 3.5 (Frobenius lifts determine the Λ-structure).** Let \(A\) be a torsion-free ring.

(a) The map \(\alpha\mapsto(\psi_p)_p\) is a bijection from the set of Λ-structures on \(A\) onto the set of all
families \((\psi_p)_p\), indexed by the primes, of ring endomorphisms of \(A\) such that \(\psi_p\) is a Frobenius
lift at \(p\) and \(\psi_p\psi_\ell=\psi_\ell\psi_p\) for all primes \(p,\ell\).

(b) Let \(A\) carry a Λ-structure, and let \(B\) be a Λ-ring, not necessarily torsion-free. A ring homomorphism
\(f\colon B\to A\) is a Λ-map if and only if \(f\circ\psi_p=\psi_p\circ f\) for all primes \(p\).

*Proof.* (a) The map is well defined by Theorem 3.2.

*It is injective.* Let \(\alpha\) and \(\alpha'\) be Λ-structures with the same \(\psi_p\) for all primes \(p\). By
Theorem 3.2(a), \(\psi_n\) is the composite of the \(\psi_p\) over the prime factors of \(n\). So \(\alpha\) and
\(\alpha'\) have the same \(\psi_n\) for all \(n\), that is, \(w\circ\alpha=w\circ\alpha'\). Since \(w\) is injective
(Lemma 2.2), \(\alpha=\alpha'\).

*It is surjective.* Let \((\psi_p)_p\) be a commuting family of Frobenius lifts. For \(n=p_1\cdots p_k\), a product
of primes, put \(\psi_n=\psi_{p_1}\circ\dots\circ\psi_{p_k}\), and \(\psi_1=\mathrm{id}\). This does not depend on
the order of the factors, and \(\psi_m\psi_n=\psi_{mn}\). Fix \(x\in A\). The sequence \((\psi_n(x))_n\) satisfies
condition (ii) of Dwork's lemma for the lifts \(\varphi_p=\psi_p\), with equality, because
\(\psi_{pn}(x)=\psi_p(\psi_n(x))\). So there is a Witt vector \(\alpha(x)\) with
\[
w_n(\alpha(x))=\psi_n(x)\qquad\text{for all }n,
\]
and only one. The map \(w\circ\alpha=(\psi_n)_n\colon A\to A^{\mathbb N_+}\) is a ring homomorphism and \(w\) is an
injective ring homomorphism, so \(\alpha\) is a ring homomorphism. (Λ1) holds, because
\(w_1(\alpha(x))=\psi_1(x)=x\). For (Λ2), recall that \(W(A)\) and \(W(W(A))\) are torsion-free (Lemma 2.7). We
compare ghost components twice:
\[
w_m\circ w_n\circ W(\alpha)\circ\alpha=w_m\circ\alpha\circ w_n\circ\alpha=\psi_m\circ\psi_n,\qquad
w_m\circ w_n\circ\Delta_A\circ\alpha=w_m\circ F_n\circ\alpha=w_{mn}\circ\alpha=\psi_{mn}.
\]
These agree. So \(\alpha\) is a Λ-structure, and its Adams operations are the given \(\psi_n\).

(b) "Only if" is Theorem 3.2(c). Conversely, if \(f\) commutes with \(\psi_p\) for all primes \(p\), it commutes
with all \(\psi_n\), and
\(w_n\circ W(f)\circ\beta=f\circ w_n\circ\beta=f\circ\psi_n=\psi_n\circ f=w_n\circ\alpha\circ f\). As \(w\) is
injective on \(W(A)\), we get \(W(f)\circ\beta=\alpha\circ f\). \(\square\)

*Reference:* (a) is due to Wilkerson, in the language of the λ-operations of Section 4; see [Bhatt–Scholze 2019, Remark 2.3] and [Borger 2011, §1.17].

**Examples 3.6.** By Theorem 3.5 the torsion-free examples of Section 1 are Λ-rings.

(a) \(\mathbb Z\), \(\mathbb Z[1/N]\) and \(\mathbb Q\) have exactly one Λ-structure each. All \(\psi_n\) are the
identity.

(b) For a monoid \(M\) the ring \(\mathbb Z[M]\) is torsion-free. With \(\psi_n(m)=m^n\) it is a Λ-ring. This is the
*toric* Λ-structure of [Borger 2009, §2.2].

(c) The polynomial ring \(\mathbb Z[x]\) has, besides the toric Λ-structure, the *Chebyshev* Λ-structure with
\(\psi_n(x)=D_n(x)\) of Example 1.8.

(d) A Λ-structure on a \(\mathbb Q\)-algebra \(A\) is the same as a family of commuting ring endomorphisms of \(A\),
indexed by the primes.

(e) No Λ-structure on \(\mathbb Z[x]\) has the operations \(\psi_2,\psi_3\) of Example 1.10, and \(\mathbb Z[i]\)
has no Λ-structure at all (Example 1.9 and Theorem 3.2(b)).

### Rings with torsion

**Proposition 3.7 (torsion).** Let \(A\) be a Λ-ring, \(p\) a prime and \(x\in A\) with \(px=0\). Then
\(\psi_p(x)=0\) and \(x^{p+1}=0\). Consequently:

(a) if \(A\neq0\), then \(n\cdot1\neq0\) in \(A\) for all \(n\in\mathbb N_+\);

(b) if \(A\) is reduced, then \(A\) is torsion-free.

*Proof.* The unique ring homomorphism \(\iota\colon\mathbb Z\to A\) is a Λ-map for the Λ-structure of \(\mathbb Z\)
from Example 3.6(a): \(W(\iota)\circ\alpha_{\mathbb Z}\) and \(\alpha_A\circ\iota\) are ring homomorphisms
\(\mathbb Z\to W(A)\), so they are equal. On \(\mathbb Z\), formula (3.1) gives
\(\delta_p(p)=(p-p^p)/p=1-p^{p-1}\). By Theorem 3.2(c), \(\delta_p(p\cdot1)=(1-p^{p-1})\cdot1\) in \(A\). The product
rule of Proposition 3.3 now gives, for every \(x\in A\),
\[
\delta_p(px)=p^p\,\delta_p(x)+(1-p^{p-1})\,x^p+p\,(1-p^{p-1})\,\delta_p(x)=\psi_p(x)-p^{p-1}x^p .
\]
Let \(px=0\). Then \(\delta_p(px)=\delta_p(0)=0\), and \(p^{p-1}x^p=0\) because \(p-1\ge1\). So \(\psi_p(x)=0\).
By (3.1) this says \(x^p=-p\,\delta_p(x)\), and therefore \(x^{p+1}=-(px)\,\delta_p(x)=0\).

(a) Suppose \(n\cdot1=0\) for some \(n\in\mathbb N_+\), and take \(n\) minimal. Then \(n>1\), because \(A\neq0\). Let
\(p\) be a prime divisor of \(n\) and \(y=(n/p)\cdot1\). Then \(py=0\), so \(\psi_p(y)=0\). But \(\psi_p(y)=y\),
since \(\psi_p\) is a ring homomorphism. So \((n/p)\cdot1=0\), against the minimality of \(n\).

(b) Let \(nx=0\). We use induction on the number of prime factors of \(n\). If \(n=pm\), then \(p\,(mx)=0\), so
\((mx)^{p+1}=0\), and \(mx=0\) because \(A\) is reduced. By induction \(x=0\). \(\square\)

*Reference:* for a single prime, [Bhatt–Scholze 2019, Lemma 2.28]. [Borger 2009, §1.1] states (b) in the form: a
reduced algebraic space with a Λ-structure is flat over \(\mathbb Z\).

**Example 3.8 (\(\mathbb F_p\) is not a Λ-ring).** By Example 1.5 the ring \(\mathbb F_p\) has a commuting family
of Frobenius lifts. By Proposition 3.7(a) it has no Λ-structure, and neither has any non-zero ring of positive
characteristic. So Theorem 3.5(a) fails without the hypothesis that \(A\) is torsion-free. *Reference:*
[López Peña–Lorscheid 2011a, §1.8] states that a reduced scheme with a commuting family of Frobenius lifts is flat
over \(\mathbb Z\); this fails for \(\operatorname{Spec}\mathbb F_p\) with all lifts equal to the identity. The
statement that holds is Proposition 3.7(b), for Λ-structures.

**Lemma 3.9 (quotients).** Let \((A,\alpha)\) be a Λ-ring and \(I\subseteq A\) an ideal. Write \(W(I)\) for the set
of Witt vectors all of whose components lie in \(I\). If \(\alpha(I)\subseteq W(I)\), then \(A/I\) has exactly one
Λ-structure for which the quotient map \(\pi\colon A\to A/I\) is a Λ-map. The set \(\alpha^{-1}(W(I))\) is an ideal
of \(A\), so it is enough to check \(\alpha(s)\in W(I)\) for the elements \(s\) of a set of generators of \(I\).

*Proof.* \(W(\pi)\colon W(A)\to W(A/I)\) is a surjective ring homomorphism with kernel \(W(I)\). So \(W(I)\) is an
ideal of \(W(A)\), and its preimage under \(\alpha\) is an ideal of \(A\). If \(\alpha(I)\subseteq W(I)\), there is
exactly one ring homomorphism \(\bar\alpha\colon A/I\to W(A/I)\) with \(\bar\alpha\circ\pi=W(\pi)\circ\alpha\). Then
\(w_1\circ\bar\alpha\circ\pi=w_1\circ W(\pi)\circ\alpha=\pi\circ w_1\circ\alpha=\pi\), and
\[
W(\bar\alpha)\circ\bar\alpha\circ\pi=W(\bar\alpha\circ\pi)\circ\alpha=W(W(\pi))\circ W(\alpha)\circ\alpha
=W(W(\pi))\circ\Delta_A\circ\alpha=\Delta_{A/I}\circ W(\pi)\circ\alpha=\Delta_{A/I}\circ\bar\alpha\circ\pi .
\]
As \(\pi\) is surjective, \(\bar\alpha\) satisfies (Λ1) and (Λ2). \(\square\)

**Example 3.10 (a Λ-ring with torsion).** Let \(A=\mathbb Z[x]\) with the toric Λ-structure and \(I=(2x,x^2)\). The
Witt vectors \(\alpha(x)\) and \([x]\) have the same ghost components \(x^n\), so \(\alpha(x)=[x]\). Hence
\(\alpha(x^2)=[x^2]\in W(I)\). By Lemma 2.8, \(\alpha(2x)=\alpha(2)\cdot[x]\) has the components
\(\alpha(2)_n\,x^n\). They lie in \(I\), because \(\alpha(2)_1=2\) and \(x^n\in I\) for \(n\ge2\). By Lemma 3.9,
\[
B=\mathbb Z[x]/(2x,x^2)=\mathbb Z\oplus(\mathbb Z/2)\,\bar x
\]
is a Λ-ring. The element \(\bar x\) is \(2\)-torsion, and \(\psi_2(\bar x)=\bar x^2=0\), as Proposition 3.7
predicts. So Λ-rings with torsion exist, and they are not described by Theorem 3.5.

### The Witt vectors as a right adjoint

**Theorem 3.11 (\(W(A)\) is the cofree Λ-ring on \(A\)).** Let \(A\) be a ring.

(a) \(\Delta_A\) is a Λ-structure on \(W(A)\). Its Adams operations are the Frobenius maps \(F_n\). For a ring
homomorphism \(f\colon A\to A'\) the map \(W(f)\) is a Λ-map.

(b) Let \((B,\beta)\) be a Λ-ring. For every ring homomorphism \(f\colon B\to A\) there is exactly one Λ-map
\(\tilde f\colon B\to W(A)\) with \(w_1\circ\tilde f=f\), namely \(\tilde f=W(f)\circ\beta\). Its ghost components
are \(w_n\circ\tilde f=f\circ\psi_n\).

(c) The functor \(A\mapsto(W(A),\Delta_A)\) from rings to Λ-rings is right adjoint to the forgetful functor \(U\)
from Λ-rings to rings: for every Λ-ring \(B\) and every ring \(A\) the map
\[
\operatorname{Hom}_\Lambda(B,W(A))\longrightarrow\operatorname{Hom}_{\mathrm{rings}}(U(B),A),\qquad h\mapsto w_1\circ h,
\]
is a bijection, and it is natural in \(A\) and \(B\).

*Proof.* (a) Conditions (Λ1) and (Λ2) for \(\Delta_A\) are Theorem 2.11(a) and (b). The Adams operations are
\(w_n\circ\Delta_A=F_n\) by (2.5). \(W(f)\) is a Λ-map, because \(\Delta\) commutes with ring homomorphisms.

(b) Put \(\tilde f=W(f)\circ\beta\). Then \(w_1\circ\tilde f=f\circ w_1\circ\beta=f\). It is a Λ-map:
\[
W(\tilde f)\circ\beta=W(W(f))\circ W(\beta)\circ\beta=W(W(f))\circ\Delta_B\circ\beta=\Delta_A\circ W(f)\circ\beta
=\Delta_A\circ\tilde f .
\]
Let \(h\colon B\to W(A)\) be any Λ-map with \(w_1\circ h=f\). Then, by the second identity of Theorem 2.11(a),
\[
W(f)\circ\beta=W(w_1)\circ W(h)\circ\beta=W(w_1)\circ\Delta_A\circ h=h .
\]
The ghost components are \(w_n\circ W(f)\circ\beta=f\circ w_n\circ\beta=f\circ\psi_n\).

(c) restates (b). Naturality is clear from the formula. \(\square\)

So a Λ-map from a Λ-ring \(B\) into \(W(A)\) is the same as a ring homomorphism from \(B\) to \(A\). For example the
Λ-structure \(\alpha\colon A\to W(A)\) of a Λ-ring is the Λ-map that corresponds to the identity of \(A\). For one
prime at a time, the corresponding statement is [Bhatt–Scholze 2019, Remark 2.7], which attributes it to Joyal.

### Line elements

**Definition 3.12.** Let \((A,\alpha)\) be a Λ-ring. An element \(x\in A\) is a *line element* if
\(\alpha(x)=[x]\). The set of line elements is written \(L(A)\).

**Lemma 3.13.** Let \(A\) be a Λ-ring.

(a) \(L(A)\) contains \(0\) and \(1\) and is closed under multiplication. So it is a monoid.

(b) A Λ-map \(f\colon A\to B\) maps \(L(A)\) into \(L(B)\).

(c) If \(A\) is torsion-free, then \(x\in L(A)\) if and only if \(\psi_p(x)=x^p\) for all primes \(p\).

(d) \(L(W(A))=\{[a]:a\in A\}\) for every ring \(A\), and \(a\mapsto[a]\) is an isomorphism of monoids from
\((A,\cdot)\) onto \(L(W(A))\).

*Proof.* (a) \(\alpha(xy)=\alpha(x)\,\alpha(y)=[x]\,[y]=[xy]\), \(\alpha(0)=[0]\) and \(\alpha(1)=[1]\), by Lemma
2.8. (b) \(\beta(f(x))=W(f)(\alpha(x))=W(f)([x])=[f(x)]\). (c) If \(\alpha(x)=[x]\), then
\(\psi_n(x)=w_n([x])=x^n\). Conversely let \(\psi_p(x)=x^p\) for all primes \(p\). Then \(\psi_n(x)=x^n\) for all
\(n\), by induction on the number of prime factors: \(\psi_{pn}(x)=\psi_p(x^n)=\psi_p(x)^n=x^{pn}\). So \(\alpha(x)\)
and \([x]\) have the same ghost components, and they are equal. (d) \(\Delta_A([a])=[[a]]\) by Theorem 2.11(c), so
\([a]\) is a line element of \(W(A)\). Conversely let \(y\in W(A)\) with \(\Delta_A(y)=[y]\). Apply \(W(w_1)\): by
Theorem 2.11(a) and Lemma 2.8, \(y=W(w_1)(\Delta_A(y))=W(w_1)([y])=[w_1(y)]\). The map \(a\mapsto[a]\) is injective
and multiplicative. \(\square\)

In a monoid ring \(\mathbb Z[M]\) with the toric Λ-structure every \(m\in M\) is a line element. The name comes from
the λ-operations of the next section: \(x\) is a line element if and only if \(\lambda^n(x)=0\) for all \(n\ge2\),
in the same way as the exterior powers of a one-dimensional vector space vanish from the second on.

## 4. λ-operations

A Λ-structure can also be described by operations \(\lambda^n\) that behave like exterior powers. This section
derives these operations from the map \(A\to W(A)\) and shows that the two descriptions agree.

### The series form of a Witt vector

**Proposition 4.1.** For a ring \(A\) and \(a\in W(A)\) put
\[
E(a)=\prod_{n\ge1}\big(1-a_n(-t)^n\big)=(1+a_1t)(1-a_2t^2)(1+a_3t^3)\cdots\ \in 1+tA[[t]].
\]

(a) \(E\colon W(A)\to1+tA[[t]]\) is a bijection, and it commutes with ring homomorphisms. The coefficient of
\(t^n\) in \(E(a)\) is \((-1)^{n-1}a_n\) plus a polynomial with integer coefficients in \(a_1,\dots,a_{n-1}\).

(b) With \('\) for the derivative with respect to \(t\),
\[
-t\,\frac{E(a)'}{E(a)}=\sum_{n\ge1}w_n(a)\,(-t)^n . \tag{4.1}
\]

(c) \(E(a+b)=E(a)\,E(b)\) and \(E([x])=1+xt\). So \(E\) is an isomorphism from the additive group of \(W(A)\) onto
the group \(1+tA[[t]]\) under multiplication of power series.

*Proof.* (a) The factor with index \(n\) is congruent to \(1\) modulo \(t^n\). So the product converges in
\(A[[t]]\), only the factors with index at most \(n\) contribute to the coefficient of \(t^n\), and the factor with
index \(n\) contributes \((-1)^{n-1}a_nt^n\). Hence the coefficients of \(E(a)\) determine \(a_1,a_2,\dots\) one
after the other, and they can be prescribed.

(b) For \(f\in1+tA[[t]]\) write \(D(f)=-tf'/f\). Then \(D(fg)=D(f)+D(g)\), and \(D(f)\) modulo \(t^{N}\) depends
only on \(f\) modulo \(t^{N}\). So \(D\) turns the convergent product into a convergent sum. For a single factor,
\[
D\big(1-c\,(-t)^n\big)=\frac{n\,c\,(-t)^n}{1-c\,(-t)^n}=n\sum_{k\ge1}c^k(-t)^{nk}.
\]
Summing over \(n\), with \(c=a_n\), the coefficient of \((-t)^m\) is \(\sum_{n\mid m}n\,a_n^{\,m/n}=w_m(a)\).

(c) \(E([x])=1+xt\) by definition. Both sides of \(E(a+b)=E(a)E(b)\) commute with ring homomorphisms, so by Lemma
2.7 we may assume that \(A\) is torsion-free. By (4.1) and the additivity of \(w\),
\(D(E(a+b))=D(E(a))+D(E(b))=D(E(a)E(b))\). If \(D(f)=D(g)\), then \(h=f/g\) satisfies \(h'=0\); writing
\(h=1+\sum c_nt^n\) we get \(n\,c_n=0\), so \(c_n=0\) and \(f=g\). \(\square\)

So the additive group of \(W(A)\) is the group of power series with constant term \(1\). The Witt components are
the coefficients in the product expansion of a series, and the ghost components are, up to sign, the coefficients of
its logarithmic derivative.

### λ-operations and Newton's formulas

**Definition 4.2.** Let \((A,\alpha)\) be a Λ-ring. For \(x\in A\) write
\[
\lambda_t(x)=E(\alpha(x))=\sum_{n\ge0}\lambda^n(x)\,t^n .
\]
This defines maps \(\lambda^n\colon A\to A\) for \(n\ge0\), the *λ-operations* of the Λ-ring.

**Proposition 4.3.** Let \(A\) be a Λ-ring and \(x,y\in A\).

(a) \(\lambda^0(x)=1\), \(\lambda^1(x)=x\) and \(\lambda_t(x+y)=\lambda_t(x)\,\lambda_t(y)\), that is,
\(\lambda^n(x+y)=\sum_{i+j=n}\lambda^i(x)\,\lambda^j(y)\).

(b) (Newton's formulas.) \(-t\,\lambda_t(x)'/\lambda_t(x)=\sum_{n\ge1}\psi_n(x)\,(-t)^n\). Equivalently, for all
\(n\ge1\),
\[
n\,\lambda^n(x)=\sum_{k=1}^{n}(-1)^{k-1}\,\psi_k(x)\,\lambda^{n-k}(x). \tag{4.2}
\]

(c) \(x\) is a line element if and only if \(\lambda_t(x)=1+xt\). A Λ-map commutes with all \(\lambda^n\).

*Proof.* (a) follows from Proposition 4.1(a) and (c) and from (Λ1). (b) The first formula is (4.1) for
\(a=\alpha(x)\). Multiply it by \(\lambda_t(x)\) and compare the coefficients of \(t^n\). (c) \(E\) is bijective with
\(E([x])=1+xt\), and \(E\) commutes with ring homomorphisms. \(\square\)

For \(n=2\) and \(n=3\), formula (4.2) gives
\[
2\,\lambda^2(x)=x^2-\psi_2(x),\qquad 6\,\lambda^3(x)=x^3-3x\,\psi_2(x)+2\,\psi_3(x).
\]
In a torsion-free Λ-ring the \(\lambda^n\) are therefore determined by the \(\psi_n\). That the right-hand sides are
divisible by \(2\) and by \(6\) is a consequence of the Frobenius lift property; for \(n=2\) it is exactly the
congruence \(\psi_2(x)\equiv x^2\) modulo \(2\). Read in this way, Theorem 3.5(a) says: for commuting endomorphisms
\(\psi_p\) of a torsion-free ring, the congruences \(\psi_p(x)\equiv x^p\) modulo \(p\) are all that is needed for
the elements \(\lambda^n(x)\), computed from (4.2) with rational coefficients, to lie in \(A\).

### The axioms in terms of λ-operations

The product of \(W(A)\) and the map \(\Delta_A\) can be written in the coefficients of the series \(E(a)\). This
leads to two families of universal polynomials. We write \(e_k(\xi)\) for the \(k\)-th elementary symmetric
polynomial in variables \(\xi_1,\dots,\xi_q\), with \(e_k(\xi)=0\) for \(k>q\).

**Proposition 4.4 (the universal polynomials).** There are unique polynomials with integer coefficients
\[
P_n(s_1,\dots,s_n;\sigma_1,\dots,\sigma_n)\qquad\text{and}\qquad P_{n,m}(s_1,\dots,s_{nm})\qquad(n,m\in\mathbb N_+)
\]
such that for all \(q,r\in\mathbb N_+\) the following identities hold between polynomials in \(t\) with
coefficients in \(\mathbb Z[\xi_1,\dots,\xi_q,\eta_1,\dots,\eta_r]\):
\[
\prod_{i=1}^{q}\prod_{j=1}^{r}(1+\xi_i\eta_jt)=1+\sum_{n\ge1}P_n\big(e_1(\xi),\dots,e_n(\xi);e_1(\eta),\dots,e_n(\eta)\big)\,t^n, \tag{4.3}
\]
\[
\prod_{1\le i_1 < \dots < i_m\le q}(1+\xi_{i_1}\cdots\xi_{i_m}t)=1+\sum_{n\ge1}P_{n,m}\big(e_1(\xi),\dots,e_{nm}(\xi)\big)\,t^n . \tag{4.4}
\]
Moreover, let \(A\) be a ring and \(a,b\in W(A)\), and write \(E(a)=1+\sum a'_nt^n\) and \(E(b)=1+\sum b'_nt^n\).

(i) \(E(ab)=1+\sum_{n\ge1}P_n(a'_1,\dots,a'_n;b'_1,\dots,b'_n)\,t^n\).

(ii) Let \(\lambda^m(a)\in W(A)\) be the λ-operations of the Λ-ring \((W(A),\Delta_A)\) of Theorem 3.11. Then
\(E(\lambda^m(a))=1+\sum_{n\ge1}P_{n,m}(a'_1,\dots,a'_{nm})\,t^n\).

For example
\[
P_1=s_1\sigma_1,\qquad P_2=s_1^2\sigma_2+s_2\sigma_1^2-2s_2\sigma_2,\qquad P_{n,1}=s_n,\qquad P_{1,m}=s_m,\qquad
P_{2,2}=s_1s_3-s_4 .
\]

*Proof.* *Existence.* Let \(R=\mathbb Z[x_n,y_n:n\in\mathbb N_+]\) with the universal Witt vectors \(x,y\), and
write \(E(x)=1+\sum x'_nt^n\), \(E(y)=1+\sum y'_nt^n\). By Proposition 4.1(a), \(x'_n\) is \(\pm x_n\) plus a
polynomial in the earlier variables, so the \(x'_n\) and \(y'_n\) are again free polynomial generators of \(R\).
Hence the coefficient of \(t^n\) in \(E(xy)\) is \(P_n(x'_1,x'_2,\dots;y'_1,y'_2,\dots)\) for exactly one polynomial
\(P_n\) in finitely many variables, and the coefficient of \(t^n\) in \(E(\lambda^m(x))\) is
\(P_{n,m}(x'_1,x'_2,\dots)\) for exactly one polynomial \(P_{n,m}\). Applying \(g\) and \(W(g)\) for the
homomorphism \(g\colon R\to A\) of Lemma 2.7 gives (i) and (ii), for the moment with polynomials that may involve
more variables than stated.

*The identities.* In \(W(\mathbb Z[\xi,\eta])\) let \(a=[\xi_1]+\dots+[\xi_q]\) and \(b=[\eta_1]+\dots+[\eta_r]\). By
Proposition 4.1(c), \(E(a)=\prod_i(1+\xi_it)\), so \(a'_k=e_k(\xi)\), and in the same way \(b'_k=e_k(\eta)\). Since
\([\xi_i]\,[\eta_j]=[\xi_i\eta_j]\), we have \(ab=\sum_{i,j}[\xi_i\eta_j]\) and
\(E(ab)=\prod_{i,j}(1+\xi_i\eta_jt)\). With (i) this is (4.3). Next, \(\Delta(a)=\sum_i[[\xi_i]]\) by Theorem
2.11(c). We apply Proposition 4.1(c) in the ring \(W(\mathbb Z[\xi])\), with the variable \(u\) in place of \(t\):
\[
E(\Delta(a))=\prod_i\big(1+[\xi_i]\,u\big)=1+\sum_{m\ge1}e_m\big([\xi_1],\dots,[\xi_q]\big)\,u^m .
\]
So \(\lambda^m(a)=e_m([\xi_1],\dots,[\xi_q])=\sum_{i_1 < \dots < i_m}[\xi_{i_1}\cdots\xi_{i_m}]\), and
\(E(\lambda^m(a))\) is the left-hand side of (4.4). With (ii) this is (4.4).

*The variables, and uniqueness.* The polynomials \(e_1(\xi),\dots,e_q(\xi)\) are algebraically independent over
\(\mathbb Z\): in the lexicographic order, the largest monomial of \(e_1^{c_1}\cdots e_q^{c_q}\) is
\(\xi_1^{c_1+\dots+c_q}\xi_2^{c_2+\dots+c_q}\cdots\xi_q^{c_q}\); different exponents \((c_k)\) give different largest
monomials, so in a non-trivial integer combination the largest of them does not cancel. The same holds for the
\(e_k(\xi)\) and \(e_k(\eta)\) together. Give \(s_k\) and \(\sigma_k\) the weight \(k\). The coefficient of \(t^n\)
on the left of (4.3) is homogeneous of degree \(n\) in the \(\xi_i\) and of degree \(n\) in the \(\eta_j\). Split
\(P_n\) into its parts of fixed weight in the \(s_k\) and in the \(\sigma_k\). A part whose pair of weights is not
\((n,n)\) becomes, after the substitution, a polynomial of another bidegree, so it becomes zero. Take \(q\) and \(r\)
larger than all indices of the variables in \(P_n\); then algebraic independence shows that this part is zero. So
\(P_n\) has weight \(n\) in each group of variables, and it involves only \(s_k,\sigma_k\) with \(k\le n\). In the
same way \(P_{n,m}\) has weight \(nm\). Two families that satisfy (4.3) and (4.4) agree after substitution of
algebraically independent elements, so they are equal. The examples are computed from (4.3) and (4.4). \(\square\)

**Theorem 4.5 (Λ-rings are λ-rings).** Let \(A\) be a ring, let \(\lambda^n\colon A\to A\) be maps for \(n\ge0\),
and write \(\lambda_t(x)=\sum_n\lambda^n(x)t^n\). The following are equivalent.

(a) There is a Λ-structure \(\alpha\) on \(A\) with \(\lambda_t=E\circ\alpha\). It is then unique.

(b) For all \(x,y\in A\) and all \(n,m\in\mathbb N_+\):

- (L1) \(\lambda^0(x)=1\), \(\lambda^1(x)=x\) and \(\lambda^n(x+y)=\sum_{i+j=n}\lambda^i(x)\,\lambda^j(y)\);
- (L2) \(\lambda_t(1)=1+t\);
- (L3) \(\lambda^n(xy)=P_n\big(\lambda^1(x),\dots,\lambda^n(x);\lambda^1(y),\dots,\lambda^n(y)\big)\);
- (L4) \(\lambda^n(\lambda^m(x))=P_{n,m}\big(\lambda^1(x),\dots,\lambda^{nm}(x)\big)\).

*Proof.* A map \(\lambda_t\colon A\to1+tA[[t]]\) is the same as a map \(\alpha=E^{-1}\circ\lambda_t\colon A\to W(A)\),
because \(E\) is bijective; the condition \(\lambda^0=1\) says that \(\lambda_t\) has values in \(1+tA[[t]]\). By
Proposition 4.1(c), \(\alpha\) is additive if and only if \(\lambda_t(x+y)=\lambda_t(x)\lambda_t(y)\). By
Proposition 4.1(a), (Λ1) holds if and only if \(\lambda^1(x)=x\). Since the one of \(W(A)\) is \([1]\) and
\(E([1])=1+t\), we have \(\alpha(1)=1\) if and only if (L2) holds. By Proposition 4.4(i), \(\alpha\) is
multiplicative if and only if (L3) holds. So \(\alpha\) is a ring homomorphism with (Λ1) if and only if (L1), (L2)
and (L3) hold.

Assume this. We show that (Λ2) is equivalent to (L4). The map \(E\) for the ring \(W(A)\), with variable \(u\), is a
bijection from \(W(W(A))\) onto \(1+uW(A)[[u]]\). Since \(E\) commutes with the ring homomorphism \(\alpha\),
\[
E\big(W(\alpha)(\alpha(x))\big)=\sum_{m\ge0}\alpha(\lambda^m(x))\,u^m,\qquad
E\big(\Delta_A(\alpha(x))\big)=\sum_{m\ge0}\lambda^m(\alpha(x))\,u^m,
\]
where \(\lambda^m(\alpha(x))\) is the λ-operation of the Λ-ring \(W(A)\). So (Λ2) holds if and only if
\(\alpha(\lambda^m(x))=\lambda^m(\alpha(x))\) for all \(x\) and \(m\). Apply the bijection \(E\) to both sides. The
left side becomes \(\lambda_t(\lambda^m(x))\). By Proposition 4.4(ii), with \(a=\alpha(x)\) and
\(a'_k=\lambda^k(x)\), the right side becomes \(1+\sum_nP_{n,m}(\lambda^1(x),\dots,\lambda^{nm}(x))\,t^n\). Comparing
coefficients gives (L4). \(\square\)

In this lesson a ring with operations \(\lambda^n\) that satisfy (L1) to (L4) is called a *λ-ring*, and a ring with
operations that satisfy (L1) only a *pre-λ-ring*. By Theorem 4.5 a λ-ring is the same as a Λ-ring.
[Borger 2009, Introduction] refers to Grothendieck for the notion of Λ-ring. For \(n=2\), (L3) reads
\(\lambda^2(xy)=x^2\lambda^2(y)+y^2\lambda^2(x)-2\lambda^2(x)\lambda^2(y)\), and (L4) for \(n=m=2\) reads
\(\lambda^2(\lambda^2(x))=x\,\lambda^3(x)-\lambda^4(x)\).

The model for \(\lambda^n\) is the \(n\)-th exterior power. For finite-dimensional vector spaces \(V\) and \(V'\)
there is a natural isomorphism between the \(n\)-th exterior power of \(V\oplus V'\) and the direct sum, over
\(i+j=n\), of the tensor products of the \(i\)-th exterior power of \(V\) and the \(j\)-th exterior power of \(V'\).
This has the shape of (L1). A space of dimension one has vanishing exterior powers from the second on, which is the
shape of a line element. In the same way (4.3) and (4.4) have the shape of the exterior powers of a tensor product,
and of an exterior power, for direct sums of one-dimensional spaces, when \(\xi_i\) and \(\eta_j\) stand for the
summands.

**Examples 4.6.** (a) *The integers.* For the Λ-structure of \(\mathbb Z\) we have \(\alpha(1)=[1]\), so
\(\lambda_t(1)=1+t\) and \(\lambda_t(x)=(1+t)^x\) for all \(x\in\mathbb Z\), by Proposition 4.3(a). Hence
\(\lambda^n(x)=\binom xn\), also for negative \(x\). As a check of (L4): \(\lambda^2(\lambda^2(4))=\binom62=15\) and
\(4\binom43-\binom44=15\).

(b) *Monoid rings.* For \(m\in M\) we have \(\lambda_t(m)=1+mt\) in \(\mathbb Z[M]\), and
\(\lambda_t\big(\sum c_m\,m\big)=\prod_m(1+mt)^{c_m}\).

(c) *The Chebyshev Λ-ring.* Here \(\lambda_t(x)=1+xt+t^2\); see Exercise 8.3.

## 5. Borger's proposal

A reference for this section is [Borger 2009, §1 and §2].

### The dictionary

Let \(k\to K\) be a homomorphism of rings. Base change \(B\mapsto K\otimes_kB\) is a functor from \(k\)-algebras to
\(K\)-algebras. It is left adjoint to the functor that regards a \(K\)-algebra as a \(k\)-algebra. Descent theory
asks which extra structure on a \(K\)-algebra \(C\) allows one to recover a \(k\)-algebra \(B\) with
\(C\cong K\otimes_kB\). For a faithfully flat homomorphism such a structure is a *descent datum*; see
[Stacks, Tag [023N](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-proposition-descent-module)] for the case of modules.

[Borger 2009, Introduction and §1.2] proposes to read the forgetful functor \(U\) from Λ-rings to rings in this
way: as the base change functor from a base "\(\mathbb F_1\)" below \(\mathbb Z\). Then a Λ-structure on a ring
plays the role of a
descent datum from \(\mathbb Z\) to \(\mathbb F_1\), and a Λ-ring is an \(\mathbb F_1\)-algebra. No ring
\(\mathbb F_1\) is involved. The category of Λ-rings takes the place of the category of \(\mathbb F_1\)-algebras. The
formal parallel is this.

| A ring homomorphism \(k\to K\) | The proposal |
|---|---|
| \(k\)-algebras | Λ-rings |
| \(K\)-algebras | rings |
| base change \(B\mapsto K\otimes_kB\) | the forgetful functor \(U\) |
| a \(K\)-algebra regarded as a \(k\)-algebra; right adjoint of base change | \(W\); right adjoint of \(U\) (Theorem 3.11) |
| the comonad \(C\mapsto K\otimes_kC\) on \(K\)-algebras | the comonad \(W\) on rings |
| Weil restriction; left adjoint of base change, when it exists | the free Λ-ring on a ring; left adjoint of \(U\) (quoted in Section 7) |
| \(k\) | \(\mathbb Z\) with its Λ-structure (Proposition 5.1) |
| \(K\otimes_kK\) | \(W(\mathbb Z)\) (Example 5.2) |

In the fifth row, the comonad on \(K\)-algebras is base change applied after its right adjoint. A \(K\)-algebra of
the form \(C=K\otimes_kB\) has the homomorphism of \(K\)-algebras \(C\to K\otimes_kC\),
\(c\otimes b\mapsto c\otimes(1\otimes b)\), which makes it a coalgebra for this comonad. In the proposal the
corresponding comonad is \(U\circ W=W\), and by Definition 3.1 a Λ-ring is a ring with a coalgebra structure
\(A\to W(A)\) for it. So \(W(C)\) stands for "\(\mathbb Z\otimes_{\mathbb F_1}C\)", where the ring \(C\) is first
regarded as an \(\mathbb F_1\)-algebra.

The table is about rings. [Borger 2009, §1.2] states it for spaces, that is, for sheaves of sets on the category of
affine schemes with the étale topology. There the arrows are reversed: the functor \(v^*\) that forgets the
Λ-structure has a left adjoint \(v_!\), called base-forgetting, and a right adjoint \(v_*\), called Weil restriction
of scalars. For an affine scheme \(\operatorname{Spec}A\), [Borger 2009, §1.1] describes the first as the colimit of
the spectra of the rings of Witt vectors of finite length of \(A\), and the second as the spectrum of the Λ-ring
freely generated by \(A\).

We use the following names. An *\(\mathbb F_1\)-point* of a Λ-ring \(A\) is a Λ-map \(A\to\mathbb Z\); this is the
\(\mathbb F_1\)-valued point of [Borger 2009, Corollary 3.5]. For \(n\in\mathbb N_+\), an
*\(\mathbb F_{1^n}\)-point* of \(A\) is a Λ-map \(A\to\mathbb Z[\mathbb F_{1^n}]=\mathbb Z[x]/(x^n-1)\), where the
target has the toric Λ-structure. [Borger 2009, §2.2 and Corollary 3.5] considers these maps and recalls that
\(\mathbb Z[x]/(x^n-1)\) has been called the base change of \(\mathbb F_{1^n}\); it does not give the maps a name.

**Proposition 5.1 (the absolute point).** The ring \(\mathbb Z\) has exactly one Λ-structure. For it
\(\psi_n=\mathrm{id}\) and \(\lambda^n(x)=\binom xn\). With this structure \(\mathbb Z\) is an initial object of the
category of Λ-rings: every Λ-ring receives exactly one Λ-map from \(\mathbb Z\).

*Proof.* The first two statements are Examples 3.6(a) and 4.6(a). The unique ring homomorphism from \(\mathbb Z\)
to a Λ-ring is a Λ-map; this was shown in the proof of Proposition 3.7. \(\square\)

[Borger 2009, §2.1] writes \(\mathbb F_1\) for this Λ-ring and calls \(\operatorname{Spec}\mathbb Z\) with this
structure the absolute point.

**Example 5.2 (the ring \(W(\mathbb Z)\)).** In the dictionary \(W(\mathbb Z)\) stands for
"\(\mathbb Z\otimes_{\mathbb F_1}\mathbb Z\)". In [Borger 2009, §1.2] the space
"\(\operatorname{Spec}\mathbb Z\times_{\operatorname{Spec}\mathbb F_1}\operatorname{Spec}\mathbb Z\)" is defined to
be the Witt space of \(\operatorname{Spec}\mathbb Z\), the space that underlies
\(v_!(\operatorname{Spec}\mathbb Z)\). By Example 2.9(b),
\[
W(\mathbb Z)\cong\{\,b\in\mathbb Z^{\mathbb N_+}:\ b_{pn}\equiv b_n \bmod p^{v_p(n)+1}\ \text{for all }p,n\,\},
\]
and by (2.3) the Frobenius map \(F_k\) is the shift \((F_kb)_n=b_{kn}\). So \(W(\mathbb Z)\) consists of one copy of
\(\mathbb Z\) for each \(n\in\mathbb N_+\), the \(n\)-th ghost component, and the copies with indices \(n\) and
\(pn\) are tied together modulo \(p^{v_p(n)+1}\). The ring \(W(\mathbb Z)\) is uncountable, so it is not a finitely
generated ring. The same holds for \(W(A)\) for every non-zero ring \(A\), because \(W(A)\) is the set
\(A^{\mathbb N_+}\). So the Λ-rings of the form \(W(A)\) are far from the Λ-rings of finite type of Section 6. In
*Weil's proof for curves and what is missing over the integers* the product of \(\operatorname{Spec}\mathbb Z\) with
itself over the missing base is one of the missing objects. The ring \(W(\mathbb Z)\) is what this proposal puts in
its place. Section 7 quotes the comparison with function fields that supports this reading.

### Monoid rings

**Theorem 5.3.** Let \(M\) be a monoid.

(a) With \(\psi_n(m)=m^n\) the ring \(\mathbb Z[M]\) is a Λ-ring, and \(\alpha(m)=[m]\) for \(m\in M\). So
\(M\subseteq L(\mathbb Z[M])\). A morphism of monoids \(M\to N\) induces a Λ-map \(\mathbb Z[M]\to\mathbb Z[N]\).

(b) For every Λ-ring \(A\), restriction to \(M\) is a bijection
\[
\operatorname{Hom}_\Lambda(\mathbb Z[M],A)\longrightarrow\operatorname{Hom}(M,L(A)).
\]
So the functor \(M\mapsto\mathbb Z[M]\) from monoids to Λ-rings is left adjoint to the functor \(L\).

(c) The composite of \(L\) with the functor \(W\) of Theorem 3.11 sends a ring \(A\) to the monoid \((A,\cdot)\).

*Proof.* (a) \(\mathbb Z[M]\) is torsion-free, so Example 1.4 and Theorem 3.5(a) give the Λ-structure. The Witt
vectors \(\alpha(m)\) and \([m]\) have the same ghost components \(m^n\), so they are equal. The ring homomorphism
induced by a morphism of monoids commutes with the \(\psi_p\), so it is a Λ-map by Theorem 3.5(b).

(b) A ring homomorphism \(f\colon\mathbb Z[M]\to A\) is the same as a morphism of monoids \(M\to(A,\cdot)\), by
restriction to \(M\); see *Commutative monoids and their spectra*. If \(f\) is a Λ-map, then \(f(M)\subseteq L(A)\)
by Lemma 3.13(b). Conversely let \(f(M)\subseteq L(A)\). The maps \(W(f)\circ\alpha\) and \(\alpha_A\circ f\) are ring
homomorphisms \(\mathbb Z[M]\to W(A)\). At \(m\in M\) they take the values \(W(f)([m])=[f(m)]\) and
\(\alpha_A(f(m))=[f(m)]\). As \(M\) generates the ring \(\mathbb Z[M]\), they are equal.

(c) is Lemma 3.13(d). \(\square\)

So the base change functor of monoid geometry factors through Λ-rings:
\[
\text{monoids}\ \xrightarrow{\ M\mapsto\mathbb Z[M]\ }\ \text{Λ-rings}\ \xrightarrow{\ U\ }\ \text{rings}.
\]
Each functor is a left adjoint. The right adjoints are \(L\) and \(W\), and their composite is the right adjoint
\(A\mapsto(A,\cdot)\) of the base change functor \(M\mapsto\mathbb Z[M]\) from monoids to rings.

How much of \(M\) does the Λ-ring \(\mathbb Z[M]\) remember? This depends on its line elements.

**Proposition 5.4 (line elements of monoid rings).**

(a) Let \(N\) be a cancellative and torsion-free monoid. By *Commutative monoids and their spectra* this means that
\(N\) is a submonoid of \(G_0=G\cup\{0\}\) for a torsion-free abelian group \(G\); examples are
\(\mathbb F_1[x_1,\dots,x_r]\), \(\mathbb F_1[x_1^{\pm1},\dots,x_r^{\pm1}]\) and the monoids of lattice points of
cones. Then \(L(\mathbb Z[N])=N\). More precisely, every \(f\in\mathbb Z[N]\) with \(\psi_2(f)=f^2\) lies in \(N\).

(b) \(L(\mathbb Z[\mathbb F_{1^n}])=\mathbb F_{1^n}\) for every \(n\in\mathbb N_+\).

(c) Let \(E=\{0,e,1\}\) with \(e^2=e\). Then \(L(\mathbb Z[E])=\{0,1,e,1-e\}\), which is larger than \(E\).

*Proof.* (a) \(\mathbb Z[N]\) is a subring of the group ring \(\mathbb Z[G]\). Let \(f\neq0\) with
\(\psi_2(f)=f^2\), and write \(f=\sum_{i=1}^kc_ib_i\) with different elements \(b_i\in N\setminus\{0\}\) and non-zero
integers \(c_i\). The subgroup \(H\) of \(G\) generated by the \(b_i\) is finitely generated and torsion-free, so
\(H\cong\mathbb Z^r\) [Stacks, Tag [0ASV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-modules-PID)]. The lexicographic order makes \(H\) an ordered group: \(b < b'\) implies
\(bb'' < b'b''\). Number the \(b_i\) so that \(b_1 < \dots < b_k\), and suppose \(k\ge2\). The products \(b_ib_j\) with
\(i\le j\) other than \(b_{k-1}b_k\) and \(b_k^2\) are smaller than \(b_{k-1}b_k\). So the coefficient of the group
element \(b_{k-1}b_k\) in \(f^2\) is \(2c_{k-1}c_k\neq0\). In \(\psi_2(f)=\sum c_ib_i^2\) the element \(b_{k-1}b_k\)
does not occur, because \(b_i^2\le b_{k-1}^2 < b_{k-1}b_k < b_k^2\) for \(i\le k-1\). This is a contradiction. Hence
\(k=1\) and \(f=c_1b_1\). Then \(c_1b_1^2=c_1^2b_1^2\) gives \(c_1=1\), and \(f=b_1\in N\). Conversely
\(N\subseteq L(\mathbb Z[N])\) by Theorem 5.3(a), and line elements satisfy \(\psi_2(f)=f^2\).

(b) Let \(g\) be a generator of \(\mu_n\) and \(\zeta\in\mathbb C\) a primitive \(n\)-th root of unity. For
\(k\in\mathbb Z\) let \(\chi_k\colon\mathbb Z[\mathbb F_{1^n}]\to\mathbb C\) be the ring homomorphism with
\(\chi_k(g)=\zeta^k\). An element \(f=\sum_{j=0}^{n-1}c_jg^j\) with \(\chi_k(f)=0\) for \(k=1,\dots,n\) is zero,
because the polynomial \(\sum c_jT^j\) of degree less than \(n\) then has \(n\) roots. We have
\(\chi_k\circ\psi_m=\chi_{km}\). Let \(f\) be a line element and \(z=\chi_1(f)\). Then
\(\chi_m(f)=\chi_1(\psi_m(f))=z^m\) for all \(m\ge1\). For \(m=n\) and \(m=2n\) this gives \(z^n=z^{2n}\), so
\(z^n\) is \(0\) or \(1\). If \(z^n=0\), then \(z=0\), all \(\chi_m(f)\) vanish and \(f=0\). If \(z^n=1\), then
\(z=\zeta^j\) for some \(j\), and \(\chi_m(f)=\zeta^{jm}=\chi_m(g^j)\) for all \(m\), so \(f=g^j\).

(c) \(\mathbb Z[E]\) has the basis \(1,e\), and all \(\psi_n\) are the identity, because \(e^n=e\). By Lemma
3.13(c) the line elements are the \(f\) with \(f^p=f\) for all \(p\); these are the idempotents. Under the
isomorphism \(\mathbb Z[E]\cong\mathbb Z\times\mathbb Z\), \(1\mapsto(1,1)\), \(e\mapsto(0,1)\), the idempotents are
\((0,0),(1,1),(0,1),(1,0)\), that is, \(0,1,e,1-e\). \(\square\)

**Corollary 5.5.** Let \(M\) be a monoid.

(a) If \(N\) is cancellative and torsion-free, every Λ-map \(\mathbb Z[M]\to\mathbb Z[N]\) is induced by exactly
one morphism of monoids \(M\to N\). So the functor \(M\mapsto\mathbb Z[M]\) to Λ-rings is fully faithful on
cancellative torsion-free monoids.

(b) \(\operatorname{Hom}_\Lambda(\mathbb Z[M],\mathbb Z[\mathbb F_{1^n}])=\operatorname{Hom}(M,\mathbb F_{1^n})\)
for all \(n\). In particular the \(\mathbb F_1\)-points of \(\mathbb Z[M]\) are the morphisms \(M\to\mathbb F_1\),
and \(f\mapsto f^{-1}(0)\cap M\) is a bijection from the set of \(\mathbb F_1\)-points onto the set
\(\operatorname{Spec}M\) of prime ideals of \(M\).

(c) On all monoids the functor is faithful, but it is not full: \(\mathbb Z[E]\) has a Λ-automorphism that
exchanges \(e\) and \(1-e\), and it is not induced by a morphism \(E\to E\).

*Proof.* (a) and (b) follow from Theorem 5.3(b) and Proposition 5.4(a), (b), with
\(\mathbb Z=\mathbb Z[\mathbb F_1]\). The bijection between \(\operatorname{Hom}(M,\mathbb F_1)\) and
\(\operatorname{Spec}M\) is proved in *Commutative monoids and their spectra*. (c) The functor is faithful, because
\(N\) is a subset of \(\mathbb Z[N]\). The map \(E\to L(\mathbb Z[E])\) with \(e\mapsto1-e\) is a morphism of
monoids. By Theorem 5.3(b) it gives a Λ-map \(\mathbb Z[E]\to\mathbb Z[E]\), which sends \(e\) to \(1-e\notin E\)
and is its own inverse. \(\square\)

So for the monoids of toric geometry the Λ-ring \(\mathbb Z[M]\) remembers \(M\) and its morphisms. Part (b) says
that the two notions of point agree: the \(\mathbb F_{1^n}\)-points of the Λ-ring \(\mathbb Z[M]\) are the
\(\mathbb F_{1^n}\)-points of \(\operatorname{Spec}M\) that are counted in *Monoid schemes*. For example the toric
affine line \(\mathbb Z[x]\) has the \(n+1\) points \(x\mapsto c\), \(c\in\mathbb F_{1^n}\), and the torus
\(\mathbb Z[x,x^{-1}]\) has the \(n\) points with \(c\in\mu_n\). For \(n=1\) the affine line has the two
\(\mathbb F_1\)-points \(0\) and \(1\), as noted in [Borger 2009, §3.6].

**Example 5.6 (linear maps over \(\mathbb F_1\)).** Let \(A=\mathbb Z[x_1,\dots,x_n]\) with the toric Λ-structure,
the Λ-ring of affine \(n\)-space. A matrix \(C=(c_{ij})\) with integer entries defines the ring endomorphism \(f_C\)
of \(A\) with \(f_C(x_i)=\sum_jc_{ij}x_j\). When is \(f_C\) a Λ-map? By Lemma 3.13(b) and Proposition 5.4(a), the
element \(f_C(x_i)\) must lie in \(L(A)=\mathbb F_1[x_1,\dots,x_n]\), the set of monomials together with \(0\). A
linear form is a monomial or zero only if it is \(0\) or one of the \(x_j\). Conversely, if every row of \(C\) is
zero or a standard basis vector, then \(f_C\) is induced by a morphism of monoids, and it is a Λ-map. So the linear
Λ-endomorphisms of affine \(n\)-space are given by the matrices in which every row is zero or a standard basis
vector. The invertible ones are the permutation matrices. The group of linear Λ-automorphisms of affine
\(n\)-space is the symmetric group \(S_n\). This is the form that the expectation \(GL_n(\mathbb F_1)=S_n\) of
*Counting over finite fields and the limit q → 1* takes here. By Proposition 5.4(a) the operation \(\psi_2\) alone
forces it.

[Borger 2009, Corollary 4.4] states the corresponding result for a space of linear maps that is defined inside the
category of Λ-spaces; see Section 7. The first paragraph of [Borger 2009, §4] states that the group scheme \(GL_n\)
itself does not descend to \(\mathbb F_1\), with a reference to Buium. This needs \(n\ge2\): \(GL_1=\mathbb G_m\)
with its toric Λ-structure \(\psi_p(t)=t^p\) (Example 1.4) is a group scheme over \(\mathbb F_1\), since
\(\psi_p(t\otimes t)=t^p\otimes t^p\) shows that the group law is a morphism of Λ-schemes. For \(n\ge2\)
the statement is Proposition 6.12.

### Cyclotomic rings

Roots of unity enter in three different rings. Their behaviour is different.

**Proposition 5.7.** Let \(n\in\mathbb N_+\), and let \(\zeta\in\mathbb C\) be a primitive \(n\)-th root of unity.

(a) The group ring \(\mathbb Z[\mathbb F_{1^n}]=\mathbb Z[x]/(x^n-1)\) is a Λ-ring with \(\psi_k(x)=x^k\). The
endomorphism \(\psi_p\) is an automorphism if \(p\nmid n\) and is not injective if \(p\mid n\). The Λ-endomorphisms
are the maps \(x\mapsto x^a\) with \(a\in\mathbb Z/n\), so the group of Λ-automorphisms is
\((\mathbb Z/n)^\times\). There is exactly one \(\mathbb F_1\)-point, \(x\mapsto1\).

(b) Let \(n\ge3\). The ring \(\mathbb Z[\zeta]\) of cyclotomic integers has no Λ-structure. For some prime \(p\)
dividing \(n\) it has no Frobenius lift at \(p\).

(c) The ring \(\mathbb Z[\zeta,1/n]\) has exactly \(\varphi(n)^{\omega(n)}\) Λ-structures, where \(\varphi\) is
Euler's function and \(\omega(n)\) is the number of primes that divide \(n\). For \(p\nmid n\), \(\psi_p\) must be
the automorphism \(\sigma_p\) with \(\sigma_p(\zeta)=\zeta^p\). For \(p\mid n\), \(\psi_p\) can be any of the
\(\varphi(n)\) automorphisms \(\sigma_a\) with \(\sigma_a(\zeta)=\zeta^a\), \(a\in(\mathbb Z/n)^\times\). For
\(n\ge3\) this ring has no ring homomorphism to \(\mathbb Q\), and so no \(\mathbb F_1\)-point.

*Proof.* (a) The Λ-structure is that of Theorem 5.3(a). If \(p\nmid n\), choose \(k\in\mathbb N_+\) with
\(pk\equiv1\) modulo \(n\); then \(\psi_k\psi_p=\psi_{pk}=\mathrm{id}\), because \(x^{pk}=x\). If \(p\mid n\), then
\(\psi_p(x^{n/p}-1)=x^n-1=0\), and \(x^{n/p}-1\neq0\) because \(1,x,\dots,x^{n-1}\) is a basis. By Corollary 5.5(b)
the Λ-endomorphisms are the morphisms of monoids \(\mathbb F_{1^n}\to\mathbb F_{1^n}\). Such a morphism sends a
generator \(g\) of \(\mu_n\) to an element whose \(n\)-th power is \(1\), so to some \(g^a\). The
\(\mathbb F_1\)-points are the morphisms \(\mathbb F_{1^n}\to\mathbb F_1\); such a morphism sends the unit \(g\) to
the unit \(1\).

(b) If \(n\equiv2\) modulo \(4\), then \(-\zeta\) is a primitive root of unity of order \(n/2\) and
\(\mathbb Z[\zeta]=\mathbb Z[-\zeta]\). So we may assume that \(n\not\equiv2\) modulo \(4\), and still \(n\ge3\). Put
\(O=\mathbb Z[\zeta]\) and \(K=\mathbb Q(\zeta)\). A ring endomorphism \(\psi\) of \(O\) extends to an endomorphism
of the field \(K\). This is an automorphism of finite order, so \(\psi^k=\mathrm{id}\) for some \(k\), and \(\psi\)
induces an automorphism of \(O/pO\). If \(\psi\) is a Frobenius lift at \(p\), the Frobenius map of \(O/pO\) is
injective, and \(O/pO\) is reduced. It is therefore enough to find a prime \(p\) and an element \(z\in O\) with
\(z\notin pO\) and \(z^k\in pO\) for some \(k\). If \(n\) has an odd prime factor \(p\), let \(\eta=\zeta^{n/p}\), a
primitive \(p\)-th root of unity, and \(z=\eta-1\). Then \(z^p\equiv\eta^p-1=0\) modulo \(pO\). The norm of \(z\)
from \(\mathbb Q(\eta)\) to \(\mathbb Q\) is \(\prod_{j=1}^{p-1}(\eta^j-1)=p\), so \(z/p\) has norm \(p^{2-p}\),
which is not an integer. Hence \(z/p\) is not an algebraic integer and \(z\notin pO\). Otherwise \(n\) is a power of
\(2\) with \(n\ge4\). Let \(i=\zeta^{n/4}\) and \(z=i-1\). Then \(z^2=-2i\in2O\), and \(z/2\) has norm \(1/2\) from
\(\mathbb Q(i)\), so \(z\notin2O\).

(c) Put \(A=\mathbb Z[\zeta,1/n]\) and \(K=\mathbb Q(\zeta)\). The Galois group of \(K\) over \(\mathbb Q\) consists
of the automorphisms \(\sigma_a\), \(a\in(\mathbb Z/n)^\times\), and each of them maps \(A\) onto \(A\). For
\(1\le d < n\) the element \(1-\zeta^d\) divides \(n\) in \(\mathbb Z[\zeta]\), because
\(\prod_{d=1}^{n-1}(1-\zeta^d)=n\); put \(T=1\) in \(\prod_{d=1}^{n-1}(T-\zeta^d)=1+T+\dots+T^{n-1}\). So
\(1-\zeta^d\) is a unit of \(A\). Let \(\psi\) be a ring endomorphism of \(A\). Then \(\psi(\zeta)^n=1\) and
\(1-\psi(\zeta)^d=\psi(1-\zeta^d)\neq0\) for \(1\le d < n\). So \(\psi(\zeta)\) is a primitive \(n\)-th root of unity
in \(K\), that is, \(\psi(\zeta)=\zeta^a\) with \(a\in(\mathbb Z/n)^\times\), and \(\psi=\sigma_a\) on \(A\),
because \(\zeta\) and \(1/n\) generate \(A\). Hence the ring endomorphisms of \(A\) are the \(\sigma_a\), and they
commute.

If \(p\mid n\), then \(pA=A\), and every \(\sigma_a\) is a Frobenius lift at \(p\). Let \(p\nmid n\). The ring \(A\)
is a free module over \(\mathbb Z[1/n]\) with basis \(1,\zeta,\dots,\zeta^{\varphi(n)-1}\), so \(A/pA\neq0\). The
automorphism \(\sigma_p\) is a Frobenius lift at \(p\) by Lemma 1.2: it sends \(\zeta\) to \(\zeta^p\), it fixes
\(1/n\), and \(c^p\equiv c\) modulo \(p\) for \(c\in\mathbb Z[1/n]\). If \(a\not\equiv p\) modulo \(n\), then
\(\zeta^a-\zeta^p=\zeta^p(\zeta^{a-p}-1)\) is a unit of \(A\). So it does not lie in \(pA\), and \(\sigma_a\) is not
a Frobenius lift at \(p\). Now Theorem 3.5(a) gives the count. Finally let \(n\ge3\). By the argument for \(\psi\),
a ring homomorphism \(A\to\mathbb Q\) would send \(\zeta\) to a primitive \(n\)-th root of unity in \(\mathbb Q\),
and there is none. \(\square\)

*Reference:* [Borger 2009, Remark 6.13] states the last sentence of (c) for every \(n>0\). For \(n=1\) and \(n=2\)
the ring is \(\mathbb Z\) or \(\mathbb Z[1/2]\), which is a subring of \(\mathbb Q\), so \(n\ge3\) is needed.

The ring in (a) is the base change of the monoid \(\mathbb F_{1^n}\), and \((\mathbb Z/n)^\times\) acts on it as a
Galois group would. The ring in (b) is what one might first write down as "\(\mathbb Z\) with the \(n\)-th roots of
unity adjoined", and for \(n\ge3\) it is not defined over \(\mathbb F_1\) at all. For \(n\ge3\) the ring in (c) is
an example of a Λ-ring of finite type without \(\mathbb F_1\)-points; it will be compared with Theorem 6.6.

## 6. Λ-schemes

### Flat Λ-schemes

A scheme \(X\) is *flat over \(\mathbb Z\)* if the ring \(\mathcal O_X(U)\) is torsion-free for every affine open
\(U\subseteq X\); a module over \(\mathbb Z\) is flat if and only if it is torsion-free [Stacks, Tag [0AUW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-dedekind-torsion-free-flat)]. For a
prime \(p\) let \(X_p=X\times_{\operatorname{Spec}\mathbb Z}\operatorname{Spec}\mathbb F_p\), the closed subscheme of
\(X\) defined by \(p\). Every endomorphism of \(X\) induces an endomorphism of \(X_p\). The *absolute Frobenius* of
\(X_p\) is the endomorphism that is the identity on points and \(g\mapsto g^p\) on functions [Stacks, Tag [03SM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-definition-absolute-frobenius)].

**Definition 6.1.** Let \(X\) be a scheme that is flat over \(\mathbb Z\). A *Frobenius lift at \(p\)* on \(X\) is
an endomorphism \(\psi\colon X\to X\) that induces the absolute Frobenius on \(X_p\). A *flat Λ-scheme* is a scheme
\(X\), flat over \(\mathbb Z\), with a Frobenius lift \(\psi_p\) at every prime \(p\), such that
\(\psi_p\psi_\ell=\psi_\ell\psi_p\) for all primes \(p,\ell\). A *Λ-morphism* of flat Λ-schemes is a morphism of
schemes that commutes with all \(\psi_p\). An *\(\mathbb F_1\)-point* of \(X\) is a Λ-morphism
\(\operatorname{Spec}\mathbb Z\to X\), where \(\operatorname{Spec}\mathbb Z\) has \(\psi_p=\mathrm{id}\) for all
\(p\).

For \(X=\operatorname{Spec}A\) with \(A\) torsion-free, an endomorphism of \(X\) is a Frobenius lift at \(p\) if and
only if the corresponding endomorphism of \(A\) is one in the sense of Definition 1.1. So by Theorem 3.5 an affine
flat Λ-scheme is the same as a torsion-free Λ-ring, Λ-morphisms are Λ-maps, and the two notions of
\(\mathbb F_1\)-point agree. Definition 6.1 is the definition of [López Peña–Lorscheid 2011a, §1.8]. [Borger 2009,
§1.1] defines Λ-structures on all schemes and algebraic spaces and states that for flat ones the definition reduces
to the one above; see Section 7. We only use flat Λ-schemes.

### Monoid schemes give Λ-schemes

Recall from *Monoid schemes*: a monoid scheme is a topological space \(X\) with a sheaf of monoids
\(\mathcal O_X\) that is locally isomorphic to \(\operatorname{Spec}M\) for monoids \(M\). A morphism is a
continuous map \(f\) together with a morphism of sheaves of monoids \(f^\sharp\) that is local on the stalks. Base
change to \(\mathbb Z\) is a functor \(X\mapsto X_{\mathbb Z}\) from monoid schemes to schemes with
\((\operatorname{Spec}M)_{\mathbb Z}=\operatorname{Spec}\mathbb Z[M]\). For an open subset \(U\subseteq X\) the
scheme \(U_{\mathbb Z}\) is an open subscheme of \(X_{\mathbb Z}\), and
\((U\cap V)_{\mathbb Z}=U_{\mathbb Z}\cap V_{\mathbb Z}\) for open subsets \(U\) and \(V\). The base change of a
restriction is the restriction of the base change, and the \(U_{\mathbb Z}\) cover \(X_{\mathbb Z}\) when the \(U\)
cover \(X\).

**Theorem 6.2 (monoid schemes give Λ-schemes).** Let \(X\) be a monoid scheme.

(a) For \(n\in\mathbb N_+\) the identity of the space \(X\), together with the map \(s\mapsto s^n\) on
\(\mathcal O_X\), is an endomorphism \(\psi_n\) of the monoid scheme \(X\). We have \(\psi_m\psi_n=\psi_{mn}\), and
\(f\circ\psi_n=\psi_n\circ f\) for every morphism \(f\colon X\to Y\) of monoid schemes.

(b) The scheme \(X_{\mathbb Z}\), with the endomorphisms \((\psi_p)_{\mathbb Z}\), is a flat Λ-scheme. For every
morphism \(f\) of monoid schemes, \(f_{\mathbb Z}\) is a Λ-morphism. On an affine open subscheme
\(\operatorname{Spec}\mathbb Z[M]\) of \(X_{\mathbb Z}\) that comes from an affine open subscheme
\(\operatorname{Spec}M\) of \(X\), the Λ-structure is the toric one.

So base change to \(\mathbb Z\) lifts to a functor from monoid schemes to flat Λ-schemes.

*Proof.* (a) The map \(s\mapsto s^n\) is a morphism of sheaves of monoids \(\mathcal O_X\to\mathcal O_X\), because
the monoids \(\mathcal O_X(U)\) are commutative. On a stalk, \(s^n\) is a unit if and only if \(s\) is a unit, so
the morphism is local. The two identities hold because \((s^n)^m=s^{mn}\) and \(f^\sharp(s^n)=f^\sharp(s)^n\). On an
affine open subscheme \(U=\operatorname{Spec}M\) the endomorphism \(\psi_n\) is the one induced by the morphism of
monoids \(m\mapsto m^n\) of \(M\): this morphism pulls a prime ideal back to itself, and on the localizations of
\(M\) it induces \(s\mapsto s^n\).

(b) Let \(U=\operatorname{Spec}M\) be an affine open subscheme of \(X\). By (a) and by the properties of base
change, \((\psi_n)_{\mathbb Z}\) maps \(U_{\mathbb Z}=\operatorname{Spec}\mathbb Z[M]\) into itself, and there it is
given by the ring endomorphism \(\psi_n\) of Example 1.4. The ring \(\mathbb Z[M]\) is torsion-free, and flatness
can be checked on a cover by affine open subschemes [Stacks, Tag [01U5](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-flat-characterize)], so \(X_{\mathbb Z}\) is flat over
\(\mathbb Z\). Let \(p\) be a prime. The endomorphism of \((X_{\mathbb Z})_p\) induced by \((\psi_p)_{\mathbb Z}\)
and the absolute Frobenius both map each open subscheme \(\operatorname{Spec}\mathbb F_p[M]\) into itself, and they
agree there, because \(\psi_p\) induces \(f\mapsto f^p\) on
\(\mathbb F_p[M]=\mathbb Z[M]/p\,\mathbb Z[M]\). These open subschemes cover \((X_{\mathbb Z})_p\), so the two
endomorphisms are equal. The \((\psi_p)_{\mathbb Z}\) commute, and \(f_{\mathbb Z}\) commutes with them, because
base change is a functor. \(\square\)

For example, take a fan. The scheme over \(\mathbb Z\) that is glued from the affine schemes
\(\operatorname{Spec}\mathbb Z[S_\sigma]\), where \(\sigma\) runs through the cones of the fan and \(S_\sigma\) is
the monoid of lattice points of the dual cone of \(\sigma\), is the base change to \(\mathbb Z\) of the monoid scheme
of the fan in *Monoid schemes*; this follows from the properties of base change recalled above. So it is a flat
Λ-scheme. Its base changes to fields are the toric varieties of the fan. Projective space
\(\mathbb P^n_{\mathbb Z}\) is the base change of the monoid scheme \(\mathbb P^n\), and its Frobenius lifts are
\(\psi_p([x_0:\dots:x_n])=[x_0^p: \dots:x_n^p]\). *Reference:* [Borger 2009, §2.4] for toric varieties;
[López Peña–Lorscheid 2011a, §2.7] for the functor.

**Example 6.3 (what the functor forgets).** (a) By Corollary 5.5(c) the functor of Theorem 6.2 is not full.

(b) It sends two monoid schemes that are not isomorphic to isomorphic Λ-schemes. Let \(E=\{0,e,1\}\) as in
Proposition 5.4(c). The space \(\operatorname{Spec}E\) has the two points \(\{0\}\) and \(\{0,e\}\), and the only
open set that contains the point \(\{0,e\}\) is the whole space; so \(\operatorname{Spec}E\) is connected. The
disjoint union \(Y\) of two copies of \(\operatorname{Spec}\mathbb F_1\) is a monoid scheme with two points and the
discrete topology. So \(\operatorname{Spec}E\) and \(Y\) are not isomorphic. But both base changes are the disjoint
union of two copies of \(\operatorname{Spec}\mathbb Z\) with all \(\psi_p\) equal to the identity, because
\(\mathbb Z[E]\cong\mathbb Z\times\mathbb Z\) with \(\psi_p=\mathrm{id}\).

(c) On affine monoid schemes \(\operatorname{Spec}N\) with \(N\) cancellative and torsion-free, in particular on
the affine monoid schemes that belong to the cones of a fan, the functor is fully faithful by Corollary 5.5(a).

*Reference:* [López Peña–Lorscheid 2011a, §2.7], which works with monoids without zero, says that the category of
monoid schemes embeds into the category of Λ-schemes. By (a) and (b), which hold in that setting with the monoid
\(\{e,1\}\) in place of \(E\), the functor is neither full nor injective on isomorphism classes; on affine monoid
schemes it is faithful, and (c) gives a class on which it is fully faithful.

**Proposition 6.4 (a Λ-ring of finite type that is not a monoid ring).** Let \(C\) be the ring \(\mathbb Z[x]\)
with the Chebyshev Λ-structure of Example 3.6(c). Then \(L(C)=\{0,1\}\). Hence \(C\) is not isomorphic, as a
Λ-ring, to \(\mathbb Z[M]\) with its toric Λ-structure for any monoid \(M\).

*Proof.* The inclusion \(C\subseteq\mathbb Z[t,t^{-1}]\), \(x=t+t^{-1}\), commutes with the \(\psi_p\). Both rings
are torsion-free, so by Lemma 3.13(c) and Proposition 5.4(a)
\[
L(C)=C\cap L(\mathbb Z[t,t^{-1}])=C\cap\big(\{0\}\cup\{t^k:k\in\mathbb Z\}\big).
\]
An element \(t^k\) is invariant under \(t\mapsto t^{-1}\) only for \(k=0\). So \(L(C)=\{0,1\}\). If \(C\) were
isomorphic to a Λ-ring \(\mathbb Z[M]\), it would be generated as a ring by line elements, because
\(M\subseteq L(\mathbb Z[M])\). But \(0\) and \(1\) generate the subring \(\mathbb Z\). \(\square\)

So the Chebyshev line \(\operatorname{Spec}C\) is a flat Λ-scheme of finite type that is not the base change of an
affine monoid scheme. [Borger 2009, §2.5] states, with a reference to [Clauwens 1994], that up to isomorphism the
toric and the Chebyshev structure are the only Λ-structures on the affine line; see Section 7.

### Λ-rings that are finite over the integers

**Lemma 6.5.** Let \(C\) be a non-zero ring that is reduced, torsion-free, and finitely generated as a
\(\mathbb Z\)-module. If \(C/pC\) is reduced for every prime \(p\), then \(C\cong\mathbb Z^r\) as a ring, for some
\(r\ge1\).

*Proof.* \(K=C\otimes\mathbb Q\) is a finite-dimensional \(\mathbb Q\)-algebra. It is reduced, because \(C\) is
reduced and torsion-free. A ring of finite length is the product of its localizations at its maximal ideals
[Stacks, Tag [00JB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-artinian-finite-length)], and a reduced local ring of finite length is a field. So \(K=K_1\times\dots\times K_r\) with
number fields \(K_i\). We regard \(C\) as a subring of \(K\). Let
\(\mathcal O=\mathcal O_{K_1}\times\dots\times\mathcal O_{K_r}\) be the product of the rings of integers. Every
element of \(C\) is integral over \(\mathbb Z\), so \(C\subseteq\mathcal O\). The \(\mathbb Z\)-module
\(\mathcal O\) is finitely generated [Milne 2020, Proposition 2.29], and every element of
\(\mathcal O\) has a multiple in \(C\). So \(\mathcal O/C\) is a finite group.

Suppose \(C\neq\mathcal O\). Then there are a prime \(p\) and \(z\in\mathcal O\setminus C\) with \(pz\in C\). Put
\(y=pz\). Then \(y\notin pC\), because \(K\) is torsion-free. The element \(z\) satisfies an equation
\(z^k+c_{k-1}z^{k-1}+\dots+c_0=0\) with \(c_i\in\mathbb Z\) and \(k\ge1\). Multiplying by \(p^k\) we get
\(y^k=-\sum_{i < k}c_i\,p^{k-i}\,y^i\in pC\). So the class of \(y\) is a non-zero nilpotent element of \(C/pC\),
against the assumption. Hence \(C=\mathcal O\).

Now \(\mathcal O_{K_i}/p\,\mathcal O_{K_i}\) is a factor of the product ring \(C/pC\), so it is reduced, for every
\(p\) and \(i\). Write \(p\,\mathcal O_{K_i}=\mathfrak P_1^{e_1}\cdots\mathfrak P_g^{e_g}\) with different prime
ideals \(\mathfrak P_j\) [Milne 2020, Theorem 3.7]. By the Chinese remainder theorem
\(\mathcal O_{K_i}/p\,\mathcal O_{K_i}\) is the product of the rings \(\mathcal O_{K_i}/\mathfrak P_j^{e_j}\). If
\(e_j\ge2\), the ideal \(\mathfrak P_j^{e_j-1}/\mathfrak P_j^{e_j}\) is non-zero and its square is zero. So all
\(e_j\) are \(1\), that is, no prime number ramifies in \(K_i\). By Minkowski's theorem
[Milne 2020, Theorem 4.9] this forces \(K_i=\mathbb Q\). Hence \(C=\mathcal O=\mathbb Z^r\).
\(\square\)

**Theorem 6.6 (non-zero Λ-rings that are finite over \(\mathbb Z\) have \(\mathbb F_1\)-points).** Let \(B\) be a
non-zero Λ-ring that is finitely generated as a \(\mathbb Z\)-module. Then there are \(r\ge1\) and a surjective Λ-map
\(B\to\mathbb Z^r\), where \(\mathbb Z^r\) has the Λ-structure with all \(\psi_n\) equal to the identity. In
particular \(B\) has an \(\mathbb F_1\)-point.

*Proof.* We pass to quotients several times and use the following remark. Let \(B'\) be a Λ-ring and \(I\) an ideal
with \(\psi_p(I)\subseteq I\) for all \(p\), such that \(B'/I\) is torsion-free. Then the \(\psi_p\) induce commuting
Frobenius lifts on \(B'/I\) (Lemma 1.6(a)). By Theorem 3.5(a) they define a Λ-structure on \(B'/I\), and by Theorem
3.5(b) the quotient map is a Λ-map.

*Step 1: torsion.* Let \(T\) be the ideal of torsion elements of \(B\). It is mapped into itself by every ring
endomorphism, and \(B_1=B/T\) is torsion-free. By Proposition 3.7(a), \(1\notin T\), so \(B_1\neq0\).

*Step 2: kernels.* Let \(I_n\) be the kernel of \(\psi_n\) on \(B_1\). Then \(I_n\subseteq I_{nk}\) for all \(n,k\).
The ring \(B_1\) is Noetherian; choose \(N\) such that \(I_N\) is maximal among the ideals \(I_n\). Then
\(I_n\subseteq I_{nN}=I_N\) for all \(n\). The ideal \(I_N\) is stable under the \(\psi_p\), because they commute
with \(\psi_N\). The ring \(B_2=B_1/I_N\) is isomorphic to the subring \(\psi_N(B_1)\) of \(B_1\), so it is
torsion-free and not zero. Every \(\psi_n\) is injective on \(B_2\): if \(\psi_n(b)\in I_N\), then
\(\psi_{nN}(b)=0\), so \(b\in I_{nN}=I_N\).

*Step 3: nilpotent elements.* Let \(B_3\) be the quotient of \(B_2\) by its nilradical. It is reduced and not zero.
It is torsion-free: if \(nb\) is nilpotent, then \(n^kb^k=0\) for some \(k\), so \(b^k=0\). The \(\psi_p\) map
nilpotent elements to nilpotent elements. Every \(\psi_n\) is injective on \(B_3\): if \(\psi_n(b)\) is nilpotent,
then \(\psi_n(b^k)=0\) for some \(k\), so \(b^k=0\) by Step 2.

*Step 4: the fibres are reduced.* \(K=B_3\otimes\mathbb Q\) is a finite-dimensional reduced \(\mathbb Q\)-algebra,
so a product of \(r\) number fields, as in the proof of Lemma 6.5. For a prime \(p\), \(\psi_p\) induces an injective
endomorphism of the \(\mathbb Q\)-algebra \(K\). It is bijective, because \(K\) has finite dimension. The group of
automorphisms of the \(\mathbb Q\)-algebra \(K\) is finite: an automorphism permutes the \(r\) factors and is given
by isomorphisms between number fields. So \(\psi_p^{\,k}=\mathrm{id}\) on \(K\), and hence on \(B_3\), for some
\(k\ge1\). Thus \(\psi_p\) is an automorphism of \(B_3\), and the Frobenius map of \(B_3/pB_3\) is bijective. A ring
of characteristic \(p\) with injective Frobenius map is reduced. So \(B_3/pB_3\) is reduced for every \(p\).

*Step 5: conclusion.* By Lemma 6.5, \(B_3\cong\mathbb Z^r\) with \(r\ge1\). A ring automorphism of \(\mathbb Z^r\)
permutes the idempotents \(e_1,\dots,e_r\) of the standard basis. Since \(\psi_p(e_i)\equiv e_i^{\,p}=e_i\) modulo
\(p\,\mathbb Z^r\), this permutation is the identity, and \(\psi_p=\mathrm{id}\). The composite
\(B\to B_1\to B_2\to B_3\cong\mathbb Z^r\) is a surjective Λ-map by the remark at the beginning, and each projection
\(\mathbb Z^r\to\mathbb Z\) is a Λ-map by Theorem 3.5(b). \(\square\)

**Corollary 6.7.** Let \(O\) be an integral domain of characteristic zero that is finitely generated as a
\(\mathbb Z\)-module. If \(O\) has a Frobenius lift at every prime, then \(O=\mathbb Z\). The lifts are not assumed
to commute. In particular, a subring of a number field that is finitely generated as a \(\mathbb Z\)-module and
different from \(\mathbb Z\) has no Λ-structure. This applies to the ring of integers of every number field other
than \(\mathbb Q\).

*Proof.* The fraction field \(K=O\otimes\mathbb Q\) is a number field. Let \(\psi\) be a Frobenius lift at \(p\). It
extends to an endomorphism of the field \(K\), which is injective and \(\mathbb Q\)-linear, hence bijective. The
automorphism group of \(K\) is finite, so \(\psi^k=\mathrm{id}\) for some \(k\ge1\). Hence \(\psi\) is an
automorphism of \(O\), the Frobenius map of \(O/pO\) is bijective, and \(O/pO\) is reduced. This holds for every
\(p\). By Lemma 6.5, \(O\cong\mathbb Z^r\), and \(r=1\) because \(O\) is a domain. \(\square\)

Theorem 6.6 is the case of affine schemes that are finite over \(\mathbb Z\) of a result stated in
[Borger 2009, Corollary 6.11] for all non-empty Λ-schemes that are proper over \(\mathbb Z\); see Section 7. The
statement of Corollary 6.7 on Λ-structures is noted in the introduction of [Borger–de Smit 2008]: a number field
other than \(\mathbb Q\) has no subring of full rank that is finitely generated as a \(\mathbb Z\)-module and
carries a Λ-structure. It is obtained there from a classification whose proof uses the Kronecker–Weber theorem
and Chebotarev's density theorem. The proof above needs Minkowski's theorem and no class field theory, and it
does not need the lifts to commute.

The Λ-ring \(\mathbb Z[\zeta,1/n]\) of Proposition 5.7(c) is of finite type, but not finitely generated as a
\(\mathbb Z\)-module, and for \(n\ge3\) it has no \(\mathbb F_1\)-point. So finiteness cannot be weakened to finite
type. Corollary 6.7 explains Example 1.9 and Proposition 5.7(b).

### Finiteness of the sets of points

**Lemma 6.8.** Let \(B\) be a finitely generated \(\mathbb F_p\)-algebra and \(m\ge1\) an integer such that
\(b^{p^m}=b\) for all \(b\in B\). Then \(B\) is a finite product of finite fields whose degrees over
\(\mathbb F_p\) divide \(m\). In particular \(B\) is finite.

*Proof.* If \(b_1,\dots,b_k\) generate \(B\), then \(B\) is a quotient of the finite ring
\(\mathbb F_p[x_1,\dots,x_k]/(x_i^{p^m}-x_i)\). The ring \(B\) is reduced: if \(b^j=0\), choose \(i\) with
\(p^{mi}\ge j\); then \(b=b^{p^{mi}}=0\). A finite reduced ring is a finite product of fields [Stacks, Tag [00JB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-artinian-finite-length)].
Let \(F\) be one of them, with \(p^d\) elements. A generator of the cyclic group \(F^\times\) has order \(p^d-1\) and
is a root of \(x^{p^m-1}-1\), so \(p^d-1\) divides \(p^m-1\). Write \(m=ud+v\) with \(0\le v < d\). Then \(p^d-1\)
divides \(p^m-1-p^v(p^{ud}-1)=p^v-1\), which is smaller than \(p^d-1\). So \(v=0\). \(\square\)

**Lemma 6.9.** Let \(B\) be a finitely generated ring such that \(B/pB\) is finite for infinitely many primes
\(p\). Then \(B\otimes\mathbb Q\) is a finite-dimensional \(\mathbb Q\)-vector space.

*Proof.* If \(n\cdot1=0\) in \(B\) for some \(n\in\mathbb N_+\), then \(B\otimes\mathbb Q=0\). Otherwise
\(\mathbb Z\to B\) is injective. By Noether normalization over a domain [Stacks, Tag [07NA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-Noether-normalization-over-a-domain)] there are
\(N\in\mathbb N_+\), an integer \(d\ge0\) and elements \(y_1,\dots,y_d\in B[1/N]\), algebraically independent over
\(\mathbb Z[1/N]\), such that \(B[1/N]\) is a finitely generated module over \(P=\mathbb Z[1/N][y_1,\dots,y_d]\). If
\(d=0\), then \(B\otimes\mathbb Q\) is finite-dimensional. Let \(d\ge1\), and let \(p\) be a prime that does not
divide \(N\). The ring \(P/pP=\mathbb F_p[y_1,\dots,y_d]\) has infinitely many prime ideals, for example those
generated by the irreducible polynomials in \(y_1\). Every prime ideal of \(P\) is the intersection of \(P\) with a
prime ideal of \(B[1/N]\), because \(P\subseteq B[1/N]\) is an integral extension [Stacks, Tag [00GQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-integral-overring-surjective)]. So
\(B[1/N]\) has infinitely many prime ideals that contain \(p\), and the ring \(B[1/N]/pB[1/N]=B/pB\) is infinite.
Hence \(B/pB\) is finite for at most the finitely many primes that divide \(N\), against the assumption. \(\square\)

**Proposition 6.10 (finiteness).** Let \(A\) and \(C\) be Λ-rings that are finitely generated as rings. Call a
prime \(p\) *periodic* for \(C\) if \(\psi_p^{\,m}=\mathrm{id}_C\) for some \(m\ge1\), where \(\psi_p^{\,m}\) is the
\(m\)-fold composite of \(\psi_p\).

(a) If infinitely many primes are periodic for \(C\), then \(C\otimes\mathbb Q\) is a finite-dimensional
\(\mathbb Q\)-vector space.

(b) If moreover \(C\) is reduced, then \(\operatorname{Hom}_\Lambda(A,C)\) is finite.

(c) \(A\) has only finitely many \(\mathbb F_{1^n}\)-points, for every \(n\in\mathbb N_+\). In particular it has
only finitely many \(\mathbb F_1\)-points.

*Proof.* In every Λ-ring, \(\psi_p^{\,m}(x)\equiv x^{p^m}\) modulo \(p\); this follows from Theorem 3.2(b) by
induction on \(m\).

(a) Let \(p\) be periodic for \(C\), with \(\psi_p^{\,m}=\mathrm{id}\). Then \(b^{p^m}=b\) for all \(b\in C/pC\),
and \(C/pC\) is finite by Lemma 6.8. Now apply Lemma 6.9.

(b) Let \(S\) be the set of primes that are periodic for \(C\), and for \(p\in S\) choose \(m_p\) with
\(\psi_p^{\,m_p}=\mathrm{id}_C\). Let \(f\colon A\to C\) be a Λ-map. For \(p\in S\) we have
\(f\circ\psi_p^{\,m_p}=\psi_p^{\,m_p}\circ f=f\). So \(f\) vanishes on the ideal \(J\subseteq A\) generated by the
elements \(\psi_p^{\,m_p}(a)-a\) with \(p\in S\) and \(a\in A\), and \(f\) factors through \(B=A/J\). For \(p\in S\)
and \(b\in B/pB\) we have \(b^{p^{m_p}}=b\). By Lemmas 6.8 and 6.9, \(B\otimes\mathbb Q\) has finite dimension. By
Proposition 3.7(b), \(C\) is torsion-free. So a ring homomorphism \(B\to C\) is determined by the induced
homomorphism of \(\mathbb Q\)-algebras \(B\otimes\mathbb Q\to C\otimes\mathbb Q\). By (a), \(C\otimes\mathbb Q\) is a
finite-dimensional reduced \(\mathbb Q\)-algebra, so a product of fields \(L_1\times\dots\times L_s\). A
homomorphism of \(\mathbb Q\)-algebras \(B\otimes\mathbb Q\to L_j\) has a maximal ideal \(\mathfrak m\) as its
kernel, and it is determined by \(\mathfrak m\) and by an embedding of the field \((B\otimes\mathbb Q)/\mathfrak m\)
into \(L_j\). The algebra \(B\otimes\mathbb Q\) has finitely many maximal ideals, and a finite extension of
\(\mathbb Q\) has finitely many embeddings into \(L_j\). So there are only finitely many homomorphisms.

(c) The ring \(C=\mathbb Z[\mathbb F_{1^n}]=\mathbb Z[x]/(x^n-1)\) is finitely generated, and it is reduced,
because \(x^n-1\) has no multiple root. Every prime \(p\nmid n\) is periodic for \(C\): if \(m\) is the order of
\(p\) in \((\mathbb Z/n)^\times\), then \(\psi_p^{\,m}(x)=x^{p^m}=x\). For \(n=1\) this is the case
\(C=\mathbb Z\). \(\square\)

*Reference:* these are affine cases of [Borger 2009, Proposition 3.2, Proposition 3.4 and Corollary 3.5], which are
stated for separated algebraic spaces of finite type; see Section 7.

### Points and the Euler characteristic

**Example 6.11 (\(\mathbb F_1\)-points and their complements).** Let \(X\) be a flat Λ-scheme and \(U\subseteq X\)
an open subscheme with \(\psi_p(U)\subseteq U\) for all \(p\). Then \(U\), with the restricted maps, is a flat
Λ-scheme. Following [Borger 2009, §3.6], we call an \(\mathbb F_1\)-point with closed image \(Z\subseteq X\)
*complemented* if the open complement of \(Z\) has this property, that is, if \(\psi_p^{-1}(Z)\subseteq Z\) for all
\(p\).

(a) *The toric affine line* \(\operatorname{Spec}\mathbb Z[x]\). By Corollary 5.5(b) its \(\mathbb F_1\)-points are
\(x\mapsto0\) and \(x\mapsto1\), with images \(V(x)\) and \(V(x-1)\). The first is complemented:
\(\psi_p^{-1}(V(x))=V(x^p)=V(x)\), and the complement is the torus \(\operatorname{Spec}\mathbb Z[x,x^{-1}]\). The
second is not: \(\psi_2^{-1}(V(x-1))=V(x^2-1)\) contains the prime ideal \((x+1)\), which does not contain \(x-1\).

(b) *The Chebyshev line* of Proposition 6.4. By Theorem 3.5(b) an \(\mathbb F_1\)-point is a ring homomorphism
\(x\mapsto c\in\mathbb Z\) with \(D_p(c)=c\) for all \(p\). The equation \(D_2(c)=c\) gives \(c\in\{2,-1\}\), and
\(D_3(c)=c\) gives \(c\in\{0,2,-2\}\). For \(c=2\) all equations hold: put \(t=1\) in
\(D_p(t+t^{-1})=t^p+t^{-p}\). So there is exactly one \(\mathbb F_1\)-point, \(x\mapsto2\). It is not complemented,
because \(\psi_2^{-1}(V(x-2))=V(x^2-4)\) contains the prime ideal \((x+2)\).

(c) *The projective line.* A morphism \(\operatorname{Spec}\mathbb Z\to\mathbb P^1_{\mathbb Z}\) is given by a pair
\((a,b)\) of coprime integers, unique up to sign [Stacks, Tags [01NE](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/constructions.html#constructions-lemma-projective-space) and [0BCH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-UFD-Pic-trivial)]. It is an \(\mathbb F_1\)-point if and
only if \((a^p,b^p)=\pm(a,b)\) for all \(p\). For \(p=2\) this leaves, up to sign, the pairs \((1,0)\), \((0,1)\) and
\((1,1)\), and these three are \(\mathbb F_1\)-points. So \(\mathbb P^1\) has the three \(\mathbb F_1\)-points
\(0\), \(\infty\) and \(1\), as many as the monoid scheme \(\mathbb P^1\) of *Monoid schemes* has points. As in (a),
the points \(0\) and \(\infty\) are complemented and the point \(1\) is not.

The numbers of complemented \(\mathbb F_1\)-points in (a), (b), (c) are \(1\), \(0\), \(2\). The Euler
characteristics of the spaces of complex points are \(1\), \(1\), \(2\). For toric varieties the two numbers agree
in general, by a result quoted in Section 7; the Chebyshev line shows that they need not agree for other
Λ-structures, as [Borger 2009, Remark 6.7] points out.

### Group schemes

A group scheme over \(\mathbb F_1\) in the sense of this lesson is a flat Λ-scheme \(G\) with a group law \(\mu\colon G\times G\to G\) that is a Λ-morphism. Here \(G\times G=G\times_{\operatorname{Spec}\mathbb Z}G\) carries the Frobenius lifts \(\psi_p\times\psi_p\). For \(G=\operatorname{Spec}A\) these are the endomorphisms \(\psi_p\otimes\psi_p\) of \(A\otimes A\), which are Frobenius lifts by Lemma 1.2 applied to the generators \(a\otimes1\) and \(1\otimes b\). The torus \(\mathbb G_m\) with its toric Λ-structure is an example (Section 5).

**Proposition 6.12 (the general linear group).** Let \(n\ge2\) and let \(p\) be a prime. Let \(GL_n=\operatorname{Spec}A\) with \(A=\mathbb Z[x_{ij}\mid 1\le i,j\le n][1/\det]\), and let \(\mu\) be its group law. There is no Frobenius lift \(\psi\) at \(p\) on \(GL_n\) with \(\psi\circ\mu=\mu\circ(\psi\times\psi)\). In particular, \(GL_n\) has no structure of a flat Λ-scheme for which \(\mu\) is a Λ-morphism.

*Proof.* Suppose that \(\psi\) is such a Frobenius lift, and let \(\psi^*\) be the corresponding ring endomorphism of \(A\). For a ring \(R\), a point \(g\in GL_n(R)\) is a ring homomorphism \(A\to R\), and \(\psi\) sends it to \(g\circ\psi^*\), which we write \(\psi(g)\). These maps are natural in \(R\), and the condition \(\psi\circ\mu=\mu\circ(\psi\times\psi)\) says that \(\psi(gh)=\psi(g)\,\psi(h)\). So \(\psi\) is a group homomorphism \(GL_n(R)\to GL_n(R)\) for every ring \(R\), and \(\psi(1)=1\).

Let \(E\) be the matrix with entry \(1\) at the place \((1,2)\) and \(0\) elsewhere; this needs \(n\ge2\). Then \(E^2=0\), so \(U(t)=1+tE\) lies in \(GL_n(\mathbb Z[t])\), and \(U(s+t)=U(s)\,U(t)\) in \(GL_n(\mathbb Z[s,t])\). Put \(\varphi(t)=\psi(U(t))\in GL_n(\mathbb Z[t])\), and write \(\varphi(t)=\sum_{k\ge0}a_kt^k\) with integer matrices \(a_k\), almost all zero. Naturality, applied to the ring homomorphisms \(\mathbb Z[t]\to\mathbb Z[s,t]\) that send \(t\) to \(s+t\), to \(s\) and to \(t\), gives
\[ \varphi(s+t)=\psi(U(s)\,U(t))=\varphi(s)\,\varphi(t), \]
and \(a_0=\varphi(0)=\psi(1)=1\). The coefficients of \(st^k\) on the two sides give \((k+1)\,a_{k+1}=a_1a_k\). Hence
\[ k!\,a_k=a_1^k\qquad(k\ge0). \tag{6.1} \]
Now we use that \(\psi\) is a Frobenius lift. The \((i,j)\) entry of \(\varphi(t)\) is the image of \(\psi^*(x_{ij})\) under the ring homomorphism \(A\to\mathbb Z[t]\) that is the point \(U(t)\), and \(\psi^*(x_{ij})-x_{ij}^p\in pA\). So the \((i,j)\) entry of \(\varphi(t)\) is congruent modulo \(p\,\mathbb Z[t]\) to the \(p\)-th power of the \((i,j)\) entry of \(U(t)\), which is \(0\), \(1\) or \(t\). Hence
\[ \varphi(t)\equiv 1+t^pE\pmod{p}. \]
Comparing the coefficients of \(t\) and of \(t^p\) gives \(a_1\equiv0\) and \(a_p\equiv E\) modulo \(p\). By (6.1), \(p!\,a_p=a_1^p\), and every entry of \(a_1^p\) is divisible by \(p^p\). Since \(p!=p\cdot(p-1)!\) and \((p-1)!\) is prime to \(p\), every entry of \(a_p\) is divisible by \(p^{p-1}\), hence by \(p\). This contradicts \(a_p\equiv E\pmod p\).

For the last statement: the Frobenius lift \(\psi_p\) of such a structure would be a \(\psi\) as above. \(\square\)

The proof uses only the matrices \(1+tE\), so it applies without change to \(SL_n\) for \(n\ge2\). For \(n=1\) there is no such matrix, and indeed \(GL_1=\mathbb G_m\) is a group scheme over \(\mathbb F_1\). [Borger 2009, §4] states the result for \(GL_n\) and refers to Buium for it. The \(\mathbb F_1\)-version of \(GL_n\) in [Borger 2009, Corollaries 4.3 and 4.4] is a different Λ-space, built from maps of toric affine space (Example 5.6 and Section 7).

## 7. What this lesson does not prove

The following results are stated here without proof. In [Borger 2009] a Λ-scheme or Λ-space carries a Λ-structure
in the general sense of item 1. For flat schemes this is the structure of Definition 6.1.

**Foundations.**

1. *Λ-structures on schemes and spaces.* [Borger 2009, §1.1] calls a sheaf of sets on the category of affine
   schemes with the étale topology a space, and defines a Λ-structure on a space as an action of a monad built from
   the big Witt vectors. It states two facts. On an algebraic space that is flat over \(\mathbb Z\), a Λ-structure
   is the same as a commuting family of endomorphisms \(\psi_p\), one for each prime, such that \(\psi_p\) agrees
   with the \(p\)-th power Frobenius map on the fibre over \(p\). A reduced algebraic space with a Λ-structure is
   flat over \(\mathbb Z\). The proofs are not in [Borger 2009]; its introduction refers to [Borger 2011] and to a
   sequel for the theory of Λ-structures on schemes. This lesson proves the versions for rings: Theorem 3.5 and
   Proposition 3.7(b).
2. *The left adjoint of the forgetful functor.* [Borger 2009, §1.1, §1.2 and §2.3]: the forgetful functor from
   Λ-rings to rings has a left adjoint, which sends a ring to the Λ-ring freely generated by it. The free Λ-ring on
   one generator is the ring of symmetric functions in infinitely many variables. On spaces, the functor \(v^*\)
   that forgets the Λ-structure has a left adjoint \(v_!\) and a right adjoint \(v_*\).
3. *One prime at a time.* On a ring without \(p\)-torsion, a Frobenius lift at \(p\) comes from exactly one
   \(\delta\)-structure [Bhatt–Scholze 2019, Remark 2.2]. The \(p\)-typical Witt vector functor is right adjoint to
   the forgetful functor from \(\delta\)-rings to rings; [Bhatt–Scholze 2019, Remark 2.7] attributes this to Joyal.
4. *The comparison with function fields.* [Borger 2009, §7.2 and Corollary 7.6]: let \(k\) be a finite field and
   \(S\) a smooth, geometrically connected curve over \(k\). There is a variant of the notion of Λ-structure for
   spaces over \(S\), with one Frobenius lift \(\psi_{\mathfrak m}\) for each closed point \(\mathfrak m\) of \(S\).
   For a space \(T\) over \(k\), the product \(S\times_kT\) carries such a structure, in which
   \(\psi_{\mathfrak m}\) is the identity on \(S\) and the \(q_{\mathfrak m}\)-th power Frobenius map on \(T\), where
   \(q_{\mathfrak m}\) is the number of elements of the residue field at \(\mathfrak m\). The functor
   \(T\mapsto S\times_kT\) is faithful, and it is fully faithful on separated reduced algebraic spaces over \(k\).
   So over a function field, a separated reduced algebraic space over the base field \(k\), and its morphisms, can
   be read off from its base change to \(S\) together with this structure. This is the model for the dictionary of
   Section 5.

**Examples and non-examples.**

5. *The affine line.* [Borger 2009, §2.5], with a reference to [Clauwens 1994]: up to isomorphism, the affine line
   \(\operatorname{Spec}\mathbb Z[x]\) has exactly one Λ-structure besides the toric one, the Chebyshev structure.
6. *Dimension zero.* [Borger 2009, §2.7], with a reference to [Borger–de Smit 2008]: every Λ-ring that is finite
   over \(\mathbb Z\) and reduced is isomorphic to a sub-Λ-ring of a product of Λ-rings of the form
   \(\mathbb Z[x]/(x^n-1)\) with their toric structures. Theorem 6.6 is a first step in this direction.
7. *Flag varieties.* [Borger 2009, §2.8] states, as a consequence of a theorem of Paranjape and Srinivas, that no
   flag variety other than a projective space has a Frobenius lift at any prime. The statement depends on what is
   called a flag variety. If every quotient of a reductive group by a parabolic subgroup is one, it needs a
   restriction. The product \(\mathbb P^1\times\mathbb P^1\) is the quotient of \(SL_2\times SL_2\) by the subgroup
   of pairs of upper triangular matrices, and the endomorphisms \(\psi_p\times\psi_p\) are commuting Frobenius lifts
   on it, where \(\psi_p\) is the lift of \(\mathbb P^1\) from Theorem 6.2; indeed the absolute Frobenius of a
   product of two schemes over \(\mathbb F_p\) is the product of the two absolute Frobenius morphisms. This
   product is not a variety of flags in one vector space, because such a variety of dimension two is a projective
   plane. The lesson does not determine the class of flag varieties for which the statement holds.
8. *Curves.* [Borger 2009, §2.9]: let \(C\) be a connected smooth proper model over \(\mathbb Z[1/M]\) of a
   connected smooth proper curve of genus at least \(1\) over \(\mathbb Q\). Then \(C\) has no Λ-structure.
9. *The general linear group.* (That the group scheme \(GL_n\), \(n\ge2\), does not descend to \(\mathbb F_1\) is
   Proposition 6.12.) [Borger 2009, Corollaries 4.3 and 4.4]: let
   \(M_{n/\mathbb F_1}\) be the Λ-space of maps from toric affine \(n\)-space to itself that commute with scalar
   multiplication by the torus \(\mathbb G_m\), and \(GL_{n/\mathbb F_1}\) the locus of invertible maps. Then
   \(GL_{n/\mathbb F_1}\) is the semidirect product of \(S_n\) and \(\mathbb G_m^n\). The \(\mathbb F_1\)-points of
   \(M_{n/\mathbb F_1}\) are the matrices with entries \(0\) and \(1\) and at most one \(1\) in every row, and the
   \(\mathbb F_1\)-points of \(GL_{n/\mathbb F_1}\) form the group \(S_n\). Example 5.6 is the elementary part.
10. *A Λ-scheme that is not glued from Λ-rings.* [Borger 2009, §2.6] gives an example, attributed there to
    B. Wieland: the quotient of the toric \(\mathbb P^1\) that identifies the points \(0\) and \(\infty\) is a
    Λ-scheme in which the singular point has no affine open neighbourhood that is stable under all \(\psi_p\).

**Λ-schemes of finite type.**

11. *Finiteness.* [Borger 2009, Proposition 3.2]: a separated algebraic Λ-space of finite type over \(\mathbb Z\)
    with infinitely many periodic primes is affine and quasi-finite over \(\mathbb Z\). [Borger 2009, Proposition
    3.4]: if \(X\) and \(Y\) are separated algebraic Λ-spaces of finite type over \(\mathbb Z\), and \(X\) is
    reduced with infinitely many periodic primes, then there are only finitely many Λ-morphisms \(X\to Y\).
    [Borger 2009, Corollary 3.5]: a separated algebraic Λ-space of finite type over \(\mathbb Z\) has only
    finitely many \(\mathbb F_{1^n}\)-points
    for every \(n\), and only finitely many \(\mathbb F_1\)-points. Proposition 6.10 proves the affine cases, except
    for the statement "quasi-finite", of which it proves that the fibre over \(\mathbb Q\) is finite.
12. *Complemented points.* [Borger 2009, Proposition 3.8 and Corollary 3.9]: in a toric variety with its toric
    Λ-structure, a closed sub-Λ-space is complemented if and only if its underlying closed set is a union of
    closures of torus orbits. [Borger 2009, Proposition 3.8] states this for the subspace itself, and its proof
    concerns the underlying closed set. The distinction matters: \(\operatorname{Spec}\mathbb Z[x]/(x^2)\) is a
    closed sub-Λ-space of the toric affine line, with \(\psi_p(\bar x)=0\), and it is complemented, since its
    complement is the torus; but it is not reduced, so it is not a union of closures of torus orbits. The
    complemented \(\mathbb F_1\)-points are the fixed points of the torus action, and their number is the Euler
    characteristic.
13. *Cohomology.* Let \(X\) be a separated Λ-scheme of finite type over \(\mathbb Z\), and let
    \(\overline{\mathbb Q}\) be an algebraic closure of \(\mathbb Q\). [Borger 2009, Theorem 6.1]: for every integer
    \(s>0\) and every \(n\), the action of the Galois group of \(\overline{\mathbb Q}\) over \(\mathbb Q\) on the
    étale cohomology group with compact support of \(X_{\overline{\mathbb Q}}\) with coefficients
    \(\mathbb Z/s\mathbb Z\), in degree \(n\), factors through the largest abelian quotient of the Galois group.
    [Borger 2009, Corollary 6.2]: for every prime \(p\) there is an integer \(N\ge1\) such that, as a
    representation of the Galois group of \(\overline{\mathbb Q}\) over \(\mathbb Q(\zeta_N)\), the cohomology with
    compact support in
    degree \(n\) with coefficients \(\mathbb Q_p\) is isomorphic to the direct sum over \(m\) of \(r_{m,n}\) copies
    of \(\mathbb Q_p(-m)\). Here \(r_{m,n}\) is the Hodge number \(h^{m,m}\) of the mixed Hodge structure on the
    cohomology with compact support in degree \(n\) of the space of complex points of \(X\).
14. *Point counts.* With these numbers put \(H_X(t)=\sum_{m,n}(-1)^n\,r_{m,n}\,t^m\). [Borger 2009, Corollary 6.6]:
    if \(X\) is a Λ-scheme that is smooth and proper over \(\mathbb Z\), then for every prime power \(q>1\) the
    number of \(\mathbb F_q\)-points of \(X\) is \(H_X(q)\). [Borger 2009, Corollary 6.5]: if \(X\) is a Λ-scheme
    that is smooth and proper over \(\mathbb Z[1/M]\), there is an integer \(N\), divisible only by primes that
    divide \(M\), such
    that the number of \(\mathbb F_q\)-points is \(H_X(q)\) for all prime powers \(q>1\) with \(q\equiv1\) modulo
    \(N\). The proofs of items 13 and 14 in [Borger 2009, §5 and §6] use étale cohomology and \(p\)-adic Hodge
    theory. That paper is described by its author as a preliminary version, and some of these proofs are given in
    outline only.
15. *Existence of points.* [Borger 2009, Theorem 6.10]: a non-empty separated Λ-scheme of finite type over
    \(\mathbb Z\) has a non-empty closed Λ-subscheme that is étale over \(\mathbb Z\).
    [Borger 2009, Corollary 6.11]: a non-empty Λ-scheme that is proper over \(\mathbb Z\) has an
    \(\mathbb F_1\)-point. [Borger 2009, Corollary 6.12]: a non-empty open Λ-subscheme of a Λ-scheme that is proper
    over \(\mathbb Z\) has a Λ-morphism from \(\operatorname{Spec}\mathbb Q\). Theorem 6.6 of this lesson proves the
    statement on \(\mathbb F_1\)-points for affine schemes that are finite over \(\mathbb Z\). Proposition 5.7(c)
    shows that properness cannot be dropped.
16. *An expectation.* In the introduction of [Borger 2009] the author expresses the hope to show that all examples
    of finite type come from toric varieties, in a certain precise sense. This is stated there as an aim, not as a
    theorem. Proposition 6.4 shows that, for an affine Λ-scheme, "comes from" cannot mean "is the base change of
    an affine monoid scheme".

**Background.** The lesson uses without proof: the facts on number fields quoted from [Milne 2020] in Lemma 6.5;
the facts from [Stacks] with Tags 00GQ, 00JB, 01NE, 01U5, 07NA, 0ASV, 0AUW and 0BCH; the Galois theory of cyclotomic
fields in Proposition 5.7; from *Commutative monoids and their spectra*, the adjunction between monoids and rings
and the bijection between prime ideals of \(M\) and morphisms \(M\to\mathbb F_1\); and from *Monoid schemes*, the
properties of base change recalled before Theorem 6.2, the monoid scheme of a fan, and the monoid scheme
\(\mathbb P^n\) with its base change and its points.

## 8. Exercises

**Exercise 8.1 (arithmetic in \(W(\mathbb Z)\)).**

(a) Compute the first four Witt components of \(2=[1]+[1]\) in \(W(\mathbb Z)\).

(b) Check Proposition 4.1(c) for this element: \(E(2)\equiv(1+t)^2\) modulo \(t^5\).

(c) Compute \(\delta_2(2)\) and \(\delta_3(2)\) in the Λ-ring \(\mathbb Z\), in two ways.

(d) Which of the sequences \(b_n=n\), \(b_n=(-1)^n\) and \(b_n=1+(-1)^n\) are ghost vectors of elements of
\(W(\mathbb Z)\)? Find the elements.

*Solution.* (a) All ghost components of \(2\) are \(2\), because \(w\) is a ring homomorphism and
\(w(1)=(1,1,\dots)\). So \(a_1=2\). From \(w_2\): \(4+2a_2=2\), so \(a_2=-1\). From \(w_3\): \(8+3a_3=2\), so
\(a_3=-2\). From \(w_4\): \(16+2+4a_4=2\), so \(a_4=-4\). Hence \(2=(2,-1,-2,-4,\dots)\).

(b) \(E(2)=(1+2t)(1+t^2)(1-2t^3)(1+4t^4)\cdots\). The first two factors give \(1+2t+t^2+2t^3\). Multiplying by
\(1-2t^3\) gives \(1+2t+t^2-4t^4\) modulo \(t^5\), and multiplying by \(1+4t^4\) gives \(1+2t+t^2\) modulo \(t^5\).

(c) On \(\mathbb Z\) all \(\psi_n\) are the identity, so \(\alpha(2)\) is the Witt vector with all ghost components
equal to \(2\), which is the element \(2\) of (a). Its components with index \(2\) and \(3\) give
\(\delta_2(2)=-1\) and \(\delta_3(2)=-2\). Formula (3.1) gives the same: \((2-2^2)/2=-1\) and \((2-2^3)/3=-2\).

(d) By Example 2.9(b) a sequence is a ghost vector if and only if \(b_{pn}\equiv b_n\) modulo \(p^{v_p(n)+1}\) for
all \(p\) and \(n\). For \(b_n=n\) this fails already for \(n=1\): \(p\not\equiv1\) modulo \(p\). The sequence
\(b_n=(-1)^n\) is \(w([-1])\). The sequence \(b_n=1+(-1)^n\) is therefore \(w([1]+[-1])\). Solving the ghost
equations gives \(a_1=0\), then \(2a_2=2\), and then \(a_n=0\) for \(n\ge3\), because the vector \((0,1,0,0,\dots)\)
has the ghost components \(2\cdot1^{n/2}=2\) for even \(n\) and \(0\) for odd \(n\). So
\([1]+[-1]=(0,1,0,0,\dots)\), which is not \([0]\): the Teichmüller map is not additive.

**Exercise 8.2 (Λ-structures on \(\mathbb Z[i,1/2]\)).** Prove directly, without Proposition 5.7, that the ring
\(A=\mathbb Z[i,1/2]\) has exactly two Λ-structures, and describe their Adams operations.

*Solution.* A ring endomorphism of \(A\) sends \(i\) to a square root of \(-1\) in the domain \(A\), so to \(\pm i\).
Hence the endomorphisms are the identity and complex conjugation \(c\). They commute. The ring \(A\) is torsion-free,
so by Theorem 3.5(a) we have to find the Frobenius lifts. At \(p=2\) both are Frobenius lifts, because \(2A=A\). Let
\(p\) be odd. Then \(A/pA=\mathbb F_p[x]/(x^2+1)\neq0\). By Lemma 1.2 an endomorphism \(\psi\) is a Frobenius lift
at \(p\) if and only if \(\psi(i)-i^p\in pA\); the generator \(1/2\) is fixed and satisfies
\((1/2)^p\equiv1/2\) modulo \(p\). Now \(i^p=i\) if \(p\equiv1\) modulo \(4\), and \(i^p=-i\) if \(p\equiv3\) modulo
\(4\). The difference of the two candidates \(i\) and \(-i\) is \(2i\), a unit of \(A\), which is not in \(pA\). So
there is exactly one Frobenius lift at \(p\): the identity if \(p\equiv1\) modulo \(4\), and \(c\) if \(p\equiv3\)
modulo \(4\). The two Λ-structures differ in \(\psi_2\), which is the identity or \(c\). This agrees with the count
\(\varphi(4)^{\omega(4)}=2\) of Proposition 5.7(c).

**Exercise 8.3 (λ-operations of the Chebyshev ring).** Let \(C\) be \(\mathbb Z[x]\) with the Chebyshev
Λ-structure. Show that \(\lambda_u(x)=1+xu+u^2\). So \(\lambda^2(x)=1\) and \(\lambda^n(x)=0\) for \(n\ge3\). Check
Newton's formulas (4.2) for \(n=2\) and \(n=3\).

*Solution.* The inclusion \(j\colon C\to\mathbb Z[t,t^{-1}]\), \(x\mapsto t+t^{-1}\), commutes with the \(\psi_p\),
and the target is torsion-free. So \(j\) is a Λ-map by Theorem 3.5(b), and it commutes with the λ-operations by
Proposition 4.3(c). In \(\mathbb Z[t,t^{-1}]\) the elements \(t\) and \(t^{-1}\) are line elements. By Proposition
4.3(a) and (c),
\[
\lambda_u(t+t^{-1})=(1+tu)(1+t^{-1}u)=1+(t+t^{-1})\,u+u^2 .
\]
Since \(j\) is injective, \(\lambda_u(x)=1+xu+u^2\). Newton's formula for \(n=2\):
\(2\lambda^2(x)=x^2-\psi_2(x)=x^2-(x^2-2)=2\). For \(n=3\):
\(3\lambda^3(x)=x\,\lambda^2(x)-\psi_2(x)\,x+\psi_3(x)=x-(x^2-2)\,x+(x^3-3x)=0\).

**Exercise 8.4 (a monoid ring with more line elements than the monoid).** Let \(E=\{0,e,1\}\) with \(e^2=e\).

(a) Show that the ring \(\mathbb Z[E]\cong\mathbb Z\times\mathbb Z\) has exactly one Λ-structure.

(b) Determine all Λ-maps from \(\mathbb Z[x]\), with the toric Λ-structure, to \(\mathbb Z[E]\). Which of them come
from morphisms of monoids \(\mathbb F_1[x]\to E\)?

*Solution.* (a) A ring endomorphism \(f\) of \(\mathbb Z\times\mathbb Z\) is determined by the idempotent
\(\varepsilon=f(1,0)\): \(f(a,b)=a\varepsilon+b(1-\varepsilon)\). The idempotents are \((0,0),(1,1),(1,0),(0,1)\).
So there are four endomorphisms: the identity, the exchange of the factors, \((a,b)\mapsto(b,b)\) and
\((a,b)\mapsto(a,a)\). In \(\mathbb F_p\times\mathbb F_p\) the Frobenius map is the identity. A Frobenius lift at
\(p\) must therefore send \((1,0)\) to an element congruent to \((1,0)\) modulo \(p\), and among the four idempotents
only \((1,0)\) has this property. So the identity is the only Frobenius lift at \(p\), for every \(p\), and by
Theorem 3.5(a) there is exactly one Λ-structure. It is the toric one, since \(e^n=e\).

(b) By Theorem 5.3(b) the Λ-maps \(\mathbb Z[x]\to\mathbb Z[E]\) correspond to the morphisms of monoids
\(\mathbb F_1[x]\to L(\mathbb Z[E])\), that is, to the elements of \(L(\mathbb Z[E])=\{0,1,e,1-e\}\) (Proposition
5.4(c)). So there are four Λ-maps, \(x\mapsto0\), \(x\mapsto1\), \(x\mapsto e\) and \(x\mapsto1-e\). The first
three come from morphisms \(\mathbb F_1[x]\to E\). The fourth does not, because \(1-e\notin E\).

**Exercise 8.5 (points of the affine line and of the torus).** Determine the \(\mathbb F_{1^n}\)-points of the
toric Λ-rings \(\mathbb Z[x]\) and \(\mathbb Z[x,x^{-1}]\), and the \(\mathbb F_1\)-points of
\(\mathbb Z[x_1,\dots,x_d]\). Compare the numbers with the numbers of points over a finite field \(\mathbb F_q\).

*Solution.* By Corollary 5.5(b) the \(\mathbb F_{1^n}\)-points are the morphisms of monoids to
\(\mathbb F_{1^n}\). A morphism \(\mathbb F_1[x]\to\mathbb F_{1^n}\) is given by the image of \(x\), which is any
element of \(\mathbb F_{1^n}\): there are \(n+1\) points. A morphism
\(\mathbb F_1[x^{\pm1}]\to\mathbb F_{1^n}\) sends the unit \(x\) to a unit: there are \(n\) points. A morphism
\(\mathbb F_1[x_1,\dots,x_d]\to\mathbb F_1\) sends each \(x_i\) to \(0\) or \(1\): there are \(2^d\) points, one
for each prime ideal of the free monoid. Over \(\mathbb F_q\) the affine line has \(q\) points and the torus has
\(q-1\) points. The numbers of \(\mathbb F_{1^n}\)-points are the values of these polynomials at \(q=n+1\), and the
\(\mathbb F_1\)-points of affine \(d\)-space are counted by \(q^d\) at \(q=2\). This agrees with the counts of points
with values in \(\mathbb F_{1^n}\) in *Commutative monoids and their spectra* and in *Monoid schemes*.

**Exercise 8.6 (symmetric Laurent polynomials).** Let \(A=\mathbb Z[x_1^{\pm1},x_2^{\pm1}]\) with the toric
Λ-structure, let the group \(S_2\) exchange the variables, and let \(B=A^{S_2}\).

(a) Show that \(B\) is a Λ-ring and that \(B=\mathbb Z[e_1,e_2,e_2^{-1}]\) with \(e_1=x_1+x_2\) and \(e_2=x_1x_2\).

(b) Compute \(\psi_2(e_1)\), \(\psi_3(e_1)\) and \(\lambda_t(e_1)\).

(c) Show that \(L(B)=\{0\}\cup\{e_2^k:k\in\mathbb Z\}\), and conclude that \(B\) is not isomorphic to a monoid ring
with its toric Λ-structure.

*Solution.* (a) The exchange of the variables commutes with the \(\psi_p\), and \(A\) is torsion-free. By Lemma
1.6(b) and (c) the \(\psi_p\) restrict to commuting Frobenius lifts on \(B\), and Theorem 3.5(a) applies. If
\(f\in B\), then \(e_2^kf\) is a symmetric polynomial in \(x_1,x_2\) for large \(k\), hence a polynomial in \(e_1\)
and \(e_2\). So \(B=\mathbb Z[e_1,e_2,e_2^{-1}]\).

(b) \(\psi_2(e_1)=x_1^2+x_2^2=e_1^2-2e_2\) and \(\psi_3(e_1)=x_1^3+x_2^3=e_1^3-3e_1e_2\). As in Exercise 8.3,
\(\lambda_t(e_1)=(1+x_1t)(1+x_2t)=1+e_1t+e_2t^2\). So \(\lambda^2(e_1)=e_2\), in agreement with
\(2\lambda^2(e_1)=e_1^2-\psi_2(e_1)\).

(c) As in the proof of Proposition 6.4, \(L(B)=B\cap L(A)\), and \(L(A)\) consists of \(0\) and the monomials
\(x_1^ax_2^b\) by Proposition 5.4(a). Such a monomial is symmetric only if \(a=b\). So
\(L(B)=\{0\}\cup\{e_2^k\}\). The subring generated by \(L(B)\) is \(\mathbb Z[e_2,e_2^{-1}]\), which does not
contain \(e_1\). A monoid ring with its toric Λ-structure is generated by line elements. So \(B\) is not isomorphic
to one. [Borger 2009, §2.5] mentions this example, for \(n\) variables, as a Λ-structure on the product of an
affine space and a torus that is not toric.

## References

- [Borger 2009] J. Borger, *Λ-rings and the field with one element*, [arXiv:0906.3146](https://arxiv.org/pdf/0906.3146v1). Result numbers refer to the
  first version.
- [Borger 2011] J. Borger, *The basic geometry of Witt vectors, I: The affine case*, Algebra Number Theory 5
  (2011), no. 2, 231–285; [arXiv:0801.1691](https://arxiv.org/pdf/0801.1691v6). Section numbers refer to the sixth arXiv version.
- [Bhatt–Scholze 2019] B. Bhatt, P. Scholze, *Prisms and prismatic cohomology*, [arXiv:1905.08229](https://arxiv.org/pdf/1905.08229).
- [López Peña–Lorscheid 2011a] J. López Peña, O. Lorscheid, *Mapping F_1-land: an overview of geometries over the
  field with one element*, [arXiv:0909.0069](https://arxiv.org/pdf/0909.0069).
- [Stacks] The [Stacks project](https://stacks.math.columbia.edu/), cited by tag. Each tag links to the same place in [AI Integrated Stacks Project](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/), the programme's edition of the Stacks project, which agrees with it modulo corrections made by GPT-6 Astra (OpenAI, Ultra setting) on suggestions of GPT-5.6 Sol (OpenAI, Ultra setting). Of the tags cited in this lesson, Tags 00JB and 0ASV carry such corrections: wording, notation and small precisions in statements and proofs. None of them changes the results used here.
- [Borger–de Smit 2008] J. Borger, B. de Smit, *Galois theory and integral models of Λ-rings*, Bull. Lond. Math.
  Soc. 40 (2008), 439–446; [arXiv:0801.2352](https://arxiv.org/pdf/0801.2352).
- [Clauwens 1994] F. J. B. J. Clauwens, *Commuting polynomials and λ-ring structures on Z[x]*, J. Pure Appl. Algebra
  95 (1994), no. 3, 261–269. Free at https://doi.org/10.1016/0022-4049(94)90061-2
- [Milne 2020] J. S. Milne, *Algebraic Number Theory*, course notes, version 3.08, 2020. Free at https://www.jmilne.org/math/CourseNotes/ANT.pdf
