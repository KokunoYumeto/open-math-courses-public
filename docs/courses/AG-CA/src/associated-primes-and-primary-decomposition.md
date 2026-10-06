# Associated primes and primary decomposition

*Written and self-checked by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. The proofs in this lesson were additionally checked by GPT-6 Astra (OpenAI), Ultra setting. These are AI checks, not human peer review. Public domain (CC0).*

The support of a module tells us where it exists. Associated primes tell us where some individual element is held in place by exactly a prime ideal. They detect every zero divisor, including those caused by nilpotent elements that the underlying space cannot see. Primary decomposition then separates these different causes of annihilation. Its components need not all be unique; we will determine precisely which ones are.

Throughout this lesson, rings are commutative with identity and \(R\) is Noetherian. A finite module means a finitely generated module. We allow arbitrary modules when finiteness is not specified. Primes are proper, and the zero ring has empty spectrum. The zero module has no associated primes. We use the fraction construction, exactness of localization, finite intersections under localization, and the support calculations proved in Localization, local properties and support. We also use the ascending chain condition, its finite-module consequences, and the Artinian structure theorem from Noetherian and Artinian rings. Our references are the Stacks project authors through the AI Integrated Stacks Project, Ravi Vakil’s *The Rising Sea*, and James S. Milne’s *A Primer of Commutative Algebra*. We give all the proofs of primary decomposition below. Weakly associated primes are not needed here.

## 1. Annihilators that are prime

For \(x\in M\), its annihilator is the ideal

\[
\operatorname{Ann}_R(x)=\{a\in R:ax=0\}.
\]

A prime \(\mathfrak p\) is **associated to \(M\)** if it equals \(\operatorname{Ann}_R(x)\) for some nonzero \(x\). Write \(\operatorname{Ass}_R(M)\), or \(\operatorname{Ass}(M)\), for the set of these primes. Equivalently, there is an injection \(R/\mathfrak p\hookrightarrow M\): send the class of \(a\) to \(ax\), and its kernel before passing to the quotient is exactly the annihilator. Conversely an injection supplies such an element by the image of \(1\).

An element \(a\in R\) is a **zero divisor on \(M\)** when multiplication by \(a\) is not injective. Thus it kills a nonzero element of \(M\). With this convention, zero is a zero divisor on every nonzero module, and the zero module has no zero divisors.

**Lemma 1.1 (maximal annihilators).** If \(M\ne0\), a maximal member of the set of annihilators of its nonzero elements is prime. Such a maximal member exists.

**Proof.** The set is nonempty and consists of ideals of the Noetherian ring \(R\), so it has a maximal member \(I=\operatorname{Ann}(x)\). It is proper because \(x\ne0\). Suppose \(ab\in I\) and \(b\notin I\). Then \(bx\ne0\) and \(I\subset\operatorname{Ann}(bx)\). Maximality makes these annihilators equal. Since \(a(bx)=0\), we have \(a\in I\). This proves primality. \(\square\)

**Theorem 1.2 (existence and zero divisors).** For every nonzero \(R\)-module \(M\), the set \(\operatorname{Ass}(M)\) is nonempty. For every \(M\),

\[
\{\text{zero divisors on }M\}
=\bigcup_{\mathfrak p\in\operatorname{Ass}(M)}\mathfrak p.
\]

**Proof.** The first assertion follows from Lemma 1.1. If \(a\) is in the annihilator of a nonzero element, it is a zero divisor. This proves the inclusion from right to left. Conversely, let \(K=\ker(a:M\to M)\ne0\). Apply Lemma 1.1 to \(K\). It contains a nonzero element \(x\) with prime annihilator \(\mathfrak p\). The annihilator is the same whether calculated in \(K\) or in \(M\), and it contains \(a\). Thus \(a\in\mathfrak p\in\operatorname{Ass}(M)\). The empty unions give the assertion for \(M=0\). \(\square\)

This proof uses Noetherianity of the ring, without requiring a finite set of generators of \(M\). It also shows why one should not replace the prime annihilator in the definition by an arbitrary annihilator. For example, the annihilator of \(1\) in \(\mathbb Z/12\mathbb Z\) is \((12)\), which is not prime. The elements \(6\) and \(4\) have prime annihilators \((2)\) and \((3)\).

If \(R\) is a domain, every nonzero element of \(R\), considered as a module over itself, has annihilator zero. Hence \(\operatorname{Ass}(R)=\{(0)\}\). More generally,

\[
\operatorname{Ass}_R(R/\mathfrak p)=\{\mathfrak p\}
\]

for every prime \(\mathfrak p\): a nonzero class has precisely this annihilator because \(R/\mathfrak p\) is a domain.

## 2. Exact sequences and finite control

**Proposition 2.1.** If

\[
0\longrightarrow L\longrightarrow M\longrightarrow Q\longrightarrow0
\]

is exact, then

\[
\operatorname{Ass}(L)\subset\operatorname{Ass}(M)
\subset\operatorname{Ass}(L)\cup\operatorname{Ass}(Q).
\]

In particular, for a finite direct sum,

\[
\operatorname{Ass}(M_1\oplus\cdots\oplus M_r)
=\bigcup_{i=1}^r\operatorname{Ass}(M_i).
\]

**Proof.** An element of the submodule \(L\) has the same annihilator in \(M\), proving the first inclusion. For the second, take \(x\in M\) with annihilator \(\mathfrak p\). If \(Rx\cap L=0\), the map \(Rx\to Q\) is injective, so \(\mathfrak p\in\operatorname{Ass}(Q)\). If this intersection is nonzero, choose \(ax\ne0\) in it. Necessarily \(a\notin\mathfrak p\). Then

\[
bax=0\quad\Longleftrightarrow\quad ba\in\mathfrak p
\quad\Longleftrightarrow\quad b\in\mathfrak p,
\]

so \(ax\in L\) has annihilator \(\mathfrak p\). Thus \(\mathfrak p\in\operatorname{Ass}(L)\). For direct sums, apply the inclusions repeatedly to the split exact sequences. The reverse inclusion follows by putting each summand into the direct sum. \(\square\)

Equality with the union in a nonsplit exact sequence need not hold. In

\[
0\longrightarrow\mathbb Z\xrightarrow{\,2\,}\mathbb Z
\longrightarrow\mathbb Z/2\mathbb Z\longrightarrow0,
\]

the middle module has just the associated prime \((0)\), while the last module has \((2)\).

**Theorem 2.2 (prime filtrations and finiteness).** A finite module \(M\) has a finite filtration

\[
0=M_0\subsetneq M_1\subsetneq\cdots\subsetneq M_t=M,
\qquad M_i/M_{i-1}\cong R/\mathfrak p_i
\]

with prime ideals \(\mathfrak p_i\). For \(M=0\), take the empty filtration. Moreover,

\[
\operatorname{Ass}(M)\subset\{\mathfrak p_1,\ldots,\mathfrak p_t\},
\]

so \(\operatorname{Ass}(M)\) is finite.

**Proof.** Suppose \(M_i\ne M\) has been constructed. Theorem 1.2 gives an associated prime of the nonzero quotient \(M/M_i\), and thus a cyclic submodule isomorphic to \(R/\mathfrak p_{i+1}\). Its inverse image is \(M_{i+1}\), strictly larger than \(M_i\). A finite module over \(R\) is Noetherian, so this construction must reach \(M\) after finitely many steps: otherwise it would give an infinite strictly increasing chain. Apply Proposition 2.1 along the filtration. Each factor has just the associated prime \(\mathfrak p_i\), so every associated prime of \(M\) occurs among them. \(\square\)

Some primes in a filtration can fail to be associated to the whole module. For instance, the filtration \(0\subset2\mathbb Z\subset\mathbb Z\) has factors isomorphic to \(\mathbb Z\) and \(\mathbb Z/2\mathbb Z\), although \((2)\) is not associated to \(\mathbb Z\). A prime filtration supplies a finite upper bound, and its prime list can depend on the filtration.

For \(n\ge2\), integer prime-power factorization and the Chinese remainder theorem give

\[
\mathbb Z/n\mathbb Z\cong
\bigoplus_{p\mid n}\mathbb Z/p^{v_p(n)}\mathbb Z.
\]

In \(\mathbb Z/p^e\mathbb Z\), an element killed by a prime number other than \(p\) must be zero, since that number is a unit modulo \(p^e\). The class of \(p^{e-1}\) has annihilator \((p)\); the prime \((0)\) cannot annihilate a nonzero element because \(p^e\) already annihilates every element. Consequently

\[
\operatorname{Ass}_{\mathbb Z}(\mathbb Z/n\mathbb Z)
=\{(p):p\mid n\}.
\]

The same formula gives the empty set for \(n=1\); for \(n=0\) the module is \(\mathbb Z\) and its associated set is \(\{(0)\}\). Proposition 2.1 also gives

\[
\operatorname{Ass}_{\mathbb Z}(\mathbb Z\oplus\mathbb Z/p\mathbb Z)
=\{(0),(p)\}.
\]

## 3. Localizing the associated points

**Theorem 3.1 (localization).** For any multiplicative set \(S\subset R\) and any module \(M\),

\[
\operatorname{Ass}_{S^{-1}R}(S^{-1}M)
=\{S^{-1}\mathfrak p:
\mathfrak p\in\operatorname{Ass}_R(M),\ \mathfrak p\cap S=\varnothing\}.
\]

**Proof.** If \(\mathfrak p=\operatorname{Ann}(x)\) avoids \(S\), localize the injection \(R/\mathfrak p\to M\). Exactness gives an injection

\[
S^{-1}R/S^{-1}\mathfrak p\longrightarrow S^{-1}M.
\]

The source is nonzero because \(\mathfrak p\) avoids \(S\). Its image of \(1\) therefore witnesses the associated prime \(S^{-1}\mathfrak p\).

Conversely, suppose \(P=\operatorname{Ann}_{S^{-1}R}(x/s)\) is prime, and let \(\mathfrak p\) be its contraction. The prime correspondence gives \(P=S^{-1}\mathfrak p\) and \(\mathfrak p\cap S=\varnothing\). Write \(\mathfrak p=(a_1,\ldots,a_r)\). For every \(i\), the equality \((a_i/1)(x/s)=0\) gives \(t_i\in S\) with \(t_i a_i x=0\). Set \(t=\prod_i t_i\), taking \(t=1\) if \(r=0\). Then \(\mathfrak p\subset\operatorname{Ann}_R(tx)\). Also \(tx\ne0\), since otherwise the nonzero element \(x/s\) would be killed by a unit. If \(btx=0\), localization and cancellation of the unit \(t/1\) show \((b/1)(x/s)=0\), hence \(b\in\mathfrak p\). We have obtained \(\operatorname{Ann}_R(tx)=\mathfrak p\). This proves the reverse inclusion. If \(0\in S\), both sides are empty. \(\square\)

The finite list of generators here is for an ideal of \(R\). There is no finite-generation assumption on \(M\).

**Theorem 3.2 (support and its minimal points).** For every \(R\)-module \(M\),

\[
\operatorname{Ass}(M)\subset\operatorname{Supp}(M),
\qquad
\operatorname{Supp}(M)=
\bigcup_{\mathfrak p\in\operatorname{Ass}(M)}V(\mathfrak p).
\]

If \(M\) is finite, the minimal elements of its support are exactly the minimal elements of \(\operatorname{Ass}(M)\). They are the primes minimal over \(\operatorname{Ann}(M)\).

**Proof.** If \(\operatorname{Ann}(x)=\mathfrak p\), no denominator outside \(\mathfrak p\) kills \(x\), so \(x/1\ne0\) in \(M_{\mathfrak p}\). More generally, for every \(\mathfrak q\supset\mathfrak p\) the localized injection \((R/\mathfrak p)_{\mathfrak q}\to M_{\mathfrak q}\) has a nonzero source. This proves that the displayed union lies in the support.

For the other inclusion, take \(\mathfrak q\in\operatorname{Supp}(M)\). The ring \(R_{\mathfrak q}\) is Noetherian and \(M_{\mathfrak q}\ne0\). Theorem 1.2 gives an associated prime of this localized module. Theorem 3.1 identifies it with an associated prime \(\mathfrak p\) of \(M\) contained in \(\mathfrak q\). Hence \(\mathfrak q\in V(\mathfrak p)\).

Now suppose \(M\) is finite. Its associated set is finite by Theorem 2.2. Each prime in that set contains a minimal member of that finite set. Therefore the union just obtained has as its minimal elements exactly those minimal members: every point of the union contains one, and a strictly smaller point below a minimal member would itself contain a smaller associated prime. Finally the support of a finite module is \(V(\operatorname{Ann}(M))\), by the preceding localization lesson. Its minimal elements are the primes minimal over that ideal. \(\square\)

The finite-module assertion identifies generic points of the irreducible components of the support. An associated prime which is not minimal among the associated primes is called an **embedded prime**. It contributes no new irreducible component to the support: its closure lies in the closure of a smaller associated prime. It can nevertheless detect additional zero divisors.

For \(M=\mathbb Z\oplus\mathbb Z/p\mathbb Z\), the support is the whole spectrum of \(\mathbb Z\), its minimal associated prime is \((0)\), and \((p)\) is embedded. A module can have an embedded associated prime even when its coefficient ring is a domain.

## 4. Primary pieces

A proper submodule \(N\subset M\) is **\(\mathfrak p\)-primary** if

\[
\operatorname{Ass}(M/N)=\{\mathfrak p\}.
\]

When \(M\) is finite, this definition has a useful operational form.

**Proposition 4.1.** Let \(Q\ne0\) be a finite module and \(\mathfrak p\) a prime. The following conditions are equivalent:

1. \(\operatorname{Ass}(Q)=\{\mathfrak p\}\).
2. \(\sqrt{\operatorname{Ann}(Q)}=\mathfrak p\), and multiplication by every \(a\notin\mathfrak p\) is injective on \(Q\).

Under these conditions each \(a\in\mathfrak p\) has a power which annihilates all of \(Q\), and some power of the ideal \(\mathfrak p\) annihilates \(Q\).

**Proof.** Under condition 1, Theorem 3.2 gives \(\operatorname{Supp}(Q)=V(\mathfrak p)\). Since \(Q\) is finite, this is also \(V(\operatorname{Ann}(Q))\). The radical-ideal correspondence gives the asserted equality of radicals. Theorem 1.2 says that every element outside \(\mathfrak p\) acts injectively. Conversely, every associated prime \(\mathfrak q\) contains \(\operatorname{Ann}(Q)\), so contains its radical \(\mathfrak p\). All elements of \(\mathfrak q\) are zero divisors, and condition 2 puts them in \(\mathfrak p\). Thus \(\mathfrak q=\mathfrak p\); existence follows from \(Q\ne0\). The individual powers follow from the definition of radical. To obtain an ideal power, choose generators \(a_1,\ldots,a_r\) of \(\mathfrak p\) and exponents \(e_i\ge1\) with \(a_i^{e_i}Q=0\). If \(r>0\), every monomial of total degree \(1+\sum_i(e_i-1)\) contains one of these powers. That power of \(\mathfrak p\) kills \(Q\). If \(\mathfrak p=0\), its first power already kills \(Q\). \(\square\)

For an ideal \(\mathfrak q\), the familiar definition says that it is proper and

\[
ab\in\mathfrak q,\quad b\notin\mathfrak q
\quad\Longrightarrow\quad a^n\in\mathfrak q
\text{ for some }n\ge1.
\]

Equivalently, every zero divisor of \(R/\mathfrak q\) is nilpotent: the nonzero class of \(b\) witnesses that the class of \(a\) is a zero divisor, and every zero divisor has such a witness.

**Theorem 4.2 (primary ideals).** A proper ideal \(\mathfrak q\) is primary if and only if \(\operatorname{Ass}_R(R/\mathfrak q)\) consists of a single prime \(\mathfrak p\). In that case \(\sqrt{\mathfrak q}=\mathfrak p\).

**Proof.** A single associated prime gives the radical equality and the zero-divisor description by Proposition 4.1 and Theorem 1.2. Each zero divisor is therefore nilpotent modulo \(\mathfrak q\).

Conversely, let \(A=R/\mathfrak q\ne0\), and suppose every zero divisor in \(A\) is nilpotent. Its nilradical \(J\) is prime. Indeed, if \(uv\) is nilpotent and \(u\) is not nilpotent, then \(u\) is not a zero divisor. From \(u^nv^n=0\), injectivity of multiplication by \(u^n\) gives \(v^n=0\). Now let \(\mathfrak p\) be the inverse image of \(J\) in \(R\), namely \(\sqrt{\mathfrak q}\). Every associated prime \(\mathfrak r\) of \(A\) contains \(\mathfrak q\), hence contains \(\mathfrak p\). On the other hand, its elements kill a nonzero class in \(A\) and so are nilpotent modulo \(\mathfrak q\). Thus \(\mathfrak r\subset\mathfrak p\). Existence of an associated prime gives \(\operatorname{Ass}_R(A)=\{\mathfrak p\}\). \(\square\)

A maximal ideal power \(\mathfrak m^n\), for \(n\ge1\), is always \(\mathfrak m\)-primary. We prove this in Solution 8.2. The analogous assertion for a nonmaximal prime is false. In

\[
A=k[x,y,z]/(xy-z^2),\qquad \mathfrak p=(x,z),
\]

the quotient \(A/\mathfrak p=k[y]\) proves primality, and \(\sqrt{\mathfrak p^2}=\mathfrak p\). But \(yx=z^2\in\mathfrak p^2\), whereas \(x\notin\mathfrak p^2\) and \(y\notin\mathfrak p\). For the middle assertion, give all three variables degree one. The relation is homogeneous of degree two, so the quotient has the grading induced from the polynomial ring, with a nonzero degree-one class \(x\). The ideal \(\mathfrak p^2\) is generated by degree-two homogeneous elements; its degree-one part is zero. Thus it cannot contain \(x\). The element \(y\) is a zero divisor on \(A/\mathfrak p^2\) with no power zero there. This is the required failure of primaryness, with the nonmembership explicitly established.

## 5. Existence of primary decomposition

A proper submodule \(N\) is **irreducible** if an equality \(N=A\cap B\), for submodules \(A,B\) containing \(N\), forces \(N=A\) or \(N=B\). This is a property in the lattice of submodules. It is different from irreducibility of a closed subset of the spectrum.

**Lemma 5.1.** In a Noetherian module every proper submodule is a finite intersection of irreducible submodules.

**Proof.** Suppose there are counterexamples, and choose a maximal one \(N\) using the ascending chain condition. It is not irreducible, since an irreducible submodule is its own one-term intersection. Hence \(N=A\cap B\) with both \(A\) and \(B\) strictly larger than \(N\). Neither can be the whole module: that would make the intersection equal to the other one, which is strictly larger than \(N\). By maximality both have finite irreducible decompositions. Intersecting these decompositions gives one for \(N\), a contradiction. \(\square\)

**Lemma 5.2.** An irreducible proper submodule of a finite \(R\)-module is primary.

**Proof.** Put \(Q=M/N\ne0\). Irreducibility means that two nonzero submodules of \(Q\) cannot have zero intersection. Suppose \(\mathfrak p\) and \(\mathfrak q\) are distinct associated primes of \(Q\), witnessed by \(x,y\). Every nonzero element of \(Rx\cong R/\mathfrak p\) has annihilator \(\mathfrak p\); every nonzero element of \(Ry\cong R/\mathfrak q\) has annihilator \(\mathfrak q\). Therefore \(Rx\cap Ry=0\): a nonzero element of the intersection would have both annihilators. This contradicts irreducibility. Theorem 1.2 supplies at least one associated prime, so \(Q\) has exactly one. \(\square\)

**Theorem 5.3 (Lasker–Noether).** Let \(M\) be a finite module over the Noetherian ring \(R\), and let \(N\subset M\). There is a finite decomposition

\[
N=N_1\cap\cdots\cap N_r,
\qquad \operatorname{Ass}(M/N_i)=\{\mathfrak p_i\},
\]

in which the primes \(\mathfrak p_i\) are distinct and no component is redundant. For \(N=M\), the decomposition is empty, with intersection \(M\).

**Proof.** For proper \(N\), combine Lemmas 5.1 and 5.2 to obtain a finite primary decomposition. Components with the same associated prime may be merged by intersection. To justify this, if \(A\) and \(B\) are \(\mathfrak p\)-primary, the map

\[
M/(A\cap B)\longrightarrow M/A\oplus M/B,
\qquad x+(A\cap B)\longmapsto(x+A,x+B),
\]

is injective. Proposition 2.1 gives an associated set contained in \(\{\mathfrak p\}\). The quotient is nonzero because \(A\cap B\) is proper, so Theorem 1.2 makes this set exactly \(\{\mathfrak p\}\). Repeated merging leaves distinct primes. Finally delete any component containing the intersection of all the others. There are finitely many components, so deletion stops with an irredundant decomposition, and it preserves distinctness. \(\square\)

This argument proves the module theorem directly; the ideal theorem is the case \(M=R\). It requires Noetherianity of \(M\) for the finite intersection and Noetherianity of \(R\) for the associated-prime arguments. A finite module over a Noetherian ring supplies both.

## 6. Exactly what is unique

**Theorem 6.1 (first uniqueness theorem).** In an irredundant primary decomposition

\[
N=\bigcap_{i=1}^rN_i,
\qquad \operatorname{Ass}(M/N_i)=\{\mathfrak p_i\},
\]

the set of primes is

\[
\{\mathfrak p_1,\ldots,\mathfrak p_r\}
=\operatorname{Ass}(M/N).
\]

In particular this set is independent of the decomposition.

**Proof.** The natural injection \(M/N\to\bigoplus_i M/N_i\) and Proposition 2.1 give the inclusion from right to left. Fix \(i\), and set

\[
K_i=\left(\bigcap_{j\ne i}N_j\right)/N\subset M/N.
\]

The intersection over no indices means \(M\). Irredundancy makes \(K_i\ne0\). Its map to \(M/N_i\) is injective, since the kernel before quotienting is \(N\). Hence \(\operatorname{Ass}(K_i)\subset\{\mathfrak p_i\}\). Theorem 1.2 makes this set nonempty, so it contains \(\mathfrak p_i\). The submodule inclusion \(K_i\subset M/N\) puts \(\mathfrak p_i\) in \(\operatorname{Ass}(M/N)\). This proves the other inclusion. The empty decomposition for \(N=M\) also gives the empty associated set. \(\square\)

**Theorem 6.2 (second uniqueness theorem).** Suppose the decomposition in Theorem 6.1 has distinct primes. If \(\mathfrak p_i\) is minimal in \(\operatorname{Ass}(M/N)\), then

\[
N_i=\ker\left(M\longrightarrow(M/N)_{\mathfrak p_i}\right).
\]

Thus the primary component belonging to a minimal associated prime is determined by \(M,N\) and that prime.

**Proof.** For \(j\ne i\), distinctness and minimality imply \(\mathfrak p_j\not\subset\mathfrak p_i\). By Theorem 3.2, \(\operatorname{Supp}(M/N_j)=V(\mathfrak p_j)\), so \((M/N_j)_{\mathfrak p_i}=0\). Therefore \((N_j)_{\mathfrak p_i}=M_{\mathfrak p_i}\). Localization preserves finite intersections of submodules, and consequently

\[
N_{\mathfrak p_i}=\bigcap_j(N_j)_{\mathfrak p_i}
=(N_i)_{\mathfrak p_i}.
\]

The inverse image of \((N_i)_{\mathfrak p_i}\) under \(M\to M_{\mathfrak p_i}\) is exactly \(N_i\). Indeed, if \(x/1\) lies in that localized submodule, some \(s\notin\mathfrak p_i\) satisfies \(sx\in N_i\). Theorem 1.2 says that \(s\) acts injectively on \(M/N_i\), so \(x\in N_i\). The inverse image of \(N_{\mathfrak p_i}\) is the kernel of \(M\to(M/N)_{\mathfrak p_i}\) by exactness. Combining these facts proves the formula. \(\square\)

For ideals, the formula is often written

\[
\mathfrak q_i=\{a\in R:a/1\in IR_{\mathfrak p_i}\}
\]

when \(I=\bigcap_i\mathfrak q_i\) and \(\mathfrak p_i\) is minimal over \(I\). The braces mean inverse image under localization; the map \(R\to R_{\mathfrak p_i}\) need not be injective. The distinction matters in rings with zero divisors.

## 7. A line and its embedded point

Let \(R=k[x,y]\) and \(I=(x^2,xy)\). Every class in \(B=R/I\) has a unique expression

\[
f(y)+c\bar x,\qquad f(y)\in k[y],\ c\in k.
\]

To see uniqueness, the monomials not divisible by \(x^2\) or \(xy\) are exactly the powers of \(y\) and \(x\). The monomials divisible by either generator span the ideal as a vector space, so these remaining monomials form a basis for the quotient. Multiplication is determined by \(\bar x^2=\bar x\bar y=0\). The ideal \(k\bar x\) is a nonzero square-zero piece killed by both variables, while quotienting it out leaves \(k[y]\).

Every prime of \(B\) contains \(\bar x\), because it is nilpotent. The underlying spectrum is therefore the line \(\operatorname{Spec}k[y]\). But as an \(R\)-module, \(B\) has the associated primes \((x)\) and \((x,y)\). The annihilator of \(\bar y\) is \((x)\), since multiplying \(f(y)+c\bar x\) by \(\bar y\) gives \(yf(y)\). The annihilator of \(\bar x\) is \((x,y)\), since multiplication by it retains just the constant term of a polynomial. These computations show both primes explicitly. They are all the associated primes by Proposition 2.1 applied to

\[
0\longrightarrow k\bar x\longrightarrow B\longrightarrow k[y]\longrightarrow0.
\]

The prime \((x)\) is the generic point of the line. The embedded prime \((x,y)\) is the origin. It records the additional element \(\bar x\) supported only there: its cyclic module is \(R/(x,y)\). Thus “embedded point” here describes an algebraic contribution supported at a point already on the line; it does not add another point to the underlying space.

There are two decompositions

\[
I=(x)\cap(x^2,y)
=(x)\cap(x^2,xy,y^2).
\]

The last ideal is \((x,y)^2\). Both displayed intersections can be checked using their monomials: in each, a monomial is divisible by \(x\) and by one of the generators of the other component exactly when it is divisible by \(x^2\) or \(xy\). The component \((x)\) is prime. The other components have radical \((x,y)\) and are primary: the first quotient is \(k[x]/(x^2)\), whose zero divisors are precisely the multiples of \(x\), all nilpotent; the second is a maximal-ideal power. Each decomposition is irredundant. Indeed \(x\notin I\), while \(y\) belongs to the first embedded component and \(y^2\) to the second, and neither belongs to \(I\). Yet the embedded components differ: \(y\in(x^2,y)\) and \(y\notin(x,y)^2\).

The minimal component agrees in both decompositions, as Theorem 6.2 requires. Localization at \((x)\) makes \(y\) a unit, so \(IR_{(x)}=(x)R_{(x)}\), whose inverse image is \((x)\). At \((x,y)\), both components survive; localization cannot single out the embedded component by the same argument.

Over \(\mathbb Z\), primary decomposition has a simpler shape. If \(n\ge2\), write \(n=\prod_i p_i^{e_i}\). Then

\[
(n)=\bigcap_i(p_i^{e_i}).
\]

An integer belongs to this intersection exactly when each prime power divides it, equivalently when their product divides it. Each factor is \((p_i)\)-primary: if \(p_i^{e_i}\mid ab\) and \(a\) is not divisible by \(p_i\), then \(p_i^{e_i}\mid b\). The intersection is irredundant, since \(n/p_i^{e_i}\) lies in all the other components and not in this one. All the associated primes are maximal and pairwise incomparable, so all components are minimal and unique. The ideal \((1)\) has the empty decomposition, and \((0)\) is itself prime.

## 8. Exercises

The first two exercises develop the definitions. The next three combine structural results, and the last asks for an explicit comparison of decompositions.

**Exercise 8.1 (first steps).** Compute \(\operatorname{Ass}_{\mathbb Z}(\mathbb Z/12\mathbb Z)\), give elements witnessing its primes, and write an irredundant primary decomposition of \(12\mathbb Z\). Identify the minimal and embedded primes.

**Exercise 8.2 (first steps).** Prove that \(\mathfrak m^n\) is \(\mathfrak m\)-primary for every maximal ideal \(\mathfrak m\) and \(n\ge1\). Show that this fact does not require Noetherianity.

**Exercise 8.3 (structural).** Verify the failure of primaryness of \(\mathfrak p^2\) in \(A=k[x,y,z]/(xy-z^2)\), with \(\mathfrak p=(x,z)\). Prove all the nonmembership assertions, including \(x\notin\mathfrak p^2\). Use the zero-divisor theorem to show that \(A/\mathfrak p^2\) has an embedded associated prime.

**Exercise 8.4 (structural).** Prove that a Noetherian ring is reduced if and only if it has no embedded associated primes and \(R_{\mathfrak p}\) is a field for every minimal prime \(\mathfrak p\). Include the zero ring using the usual vacuous conventions.

**Exercise 8.5 (structural).** Prove finite prime avoidance: if an ideal \(J\) lies in a finite union of prime ideals, it lies in one of them. Deduce that an ideal all of whose elements are zero divisors in a nonzero Noetherian ring is contained in one associated prime.

**Exercise 8.6 (synthesis).** Give two different irredundant primary decompositions of \((x^2,xy)\subset k[x,y]\), determine every associated prime, and prove that their embedded components differ. Recover the unique minimal component by localization.

## 9. Solutions

**Solution 8.1.** The classes of \(6\) and \(4\) have annihilators \((2)\) and \((3)\), respectively. Every annihilator contains \((12)\), so a prime annihilator must be a prime containing \((12)\). The only such primes of \(\mathbb Z\) are \((2)\) and \((3)\). Hence these are exactly the associated primes. We have

\[
(12)=(4)\cap(3),
\]

since simultaneous divisibility by \(4\) and \(3\) is divisibility by \(12\). The ideal \((4)\) is \((2)\)-primary: if an odd integer multiplies another into \((4)\), that other integer is already divisible by \(4\). The ideal \((3)\) is prime, hence primary. The elements \(3\) and \(4\) show that neither component is redundant. Both associated primes are minimal over \((12)\), as neither contains the other. There are no embedded primes.

**Solution 8.2.** Set \(B=R/\mathfrak m^n\). Primes of \(B\) correspond to primes containing \(\mathfrak m^n\), which must contain \(\mathfrak m\) and hence equal \(\mathfrak m\). Thus \(B\) has just one prime, the maximal ideal \(\mathfrak m/\mathfrak m^n\). Every element outside this ideal is a unit: a nonunit would generate a proper ideal and belong to a maximal ideal. A unit cannot be a zero divisor. Every element inside this ideal has its \(n\)-th power zero. Consequently every zero divisor is nilpotent, and \(\mathfrak m^n\) is proper because it is contained in \(\mathfrak m\). These facts prove primaryness and radical \(\mathfrak m\). None of this uses Noetherianity or associated-prime existence.

**Solution 8.3.** The quotient by \((x,z)\) is \(k[y]\), so \(\mathfrak p\) is prime. For any prime ideal, \(\sqrt{\mathfrak p^2}=\mathfrak p\): containment of \(\mathfrak p^2\) in \(\mathfrak p\) gives one inclusion, and \(a^2\in\mathfrak p^2\) for every \(a\in\mathfrak p\) gives the other. The relation gives \(yx=z^2\in\mathfrak p^2\). The degree-one part of \(A\) has basis \(x,y,z\), since the homogeneous defining ideal has no degree-one part. The ideal \(\mathfrak p^2=(x^2,xz,z^2)\) has no degree-one part, so \(x\notin\mathfrak p^2\). Also \(y\notin\mathfrak p\), as its image in \(k[y]\) is nonzero; indeed no positive power of \(y\) lies in \(\mathfrak p\) or \(\mathfrak p^2\). Thus \(y\) kills a nonzero class in \(A/\mathfrak p^2\) without being nilpotent there, disproving primaryness. Since \(A\) is a Noetherian quotient of a polynomial ring, Theorem 1.2 puts \(y\) in an associated prime \(\mathfrak q\) of this module. Every such prime contains \(\sqrt{\mathfrak p^2}=\mathfrak p\), and \(y\notin\mathfrak p\) forces \(\mathfrak q\supsetneq\mathfrak p\). Theorem 3.2 identifies \(\mathfrak p\) as the unique minimal associated prime. Hence \(\mathfrak q\) is embedded.

**Solution 8.4.** First suppose \(R\ne0\) is reduced. Its finitely many minimal primes \(\mathfrak p_1,\ldots,\mathfrak p_r\) have intersection equal to the nilradical, hence to zero. This intersection is irredundant. For a fixed \(i\), choose \(a_j\in\mathfrak p_j\setminus\mathfrak p_i\) for every \(j\ne i\), possible by incomparability, and multiply them. The product is in all the other primes and not in \(\mathfrak p_i\). When \(r=1\), use \(1\) as the empty product. Thus the primes themselves form an irredundant primary decomposition of zero. Theorem 6.1 gives \(\operatorname{Ass}(R)=\{\mathfrak p_1,\ldots,\mathfrak p_r\}\), so there are no embedded primes.

For any minimal prime \(\mathfrak p\), the only prime of \(R_{\mathfrak p}\) is its maximal ideal \(\mathfrak p R_{\mathfrak p}\). This localization is reduced: if \((a/s)^n=0\), some \(t\notin\mathfrak p\) satisfies \(ta^n=0\), so \((ta)^n=t^na^n=0\) and reducedness gives \(ta=0\), hence \(a/s=0\). The intersection of its primes is therefore zero, so its unique maximal ideal is zero. A nonzero ring whose maximal ideal is zero is a field.

Conversely, assume there are no embedded associated primes and every localization at a minimal prime is a field. Theorem 3.2, applied to \(M=R\), says that the minimal associated primes are precisely the minimal primes. Thus all associated primes are minimal. The map

\[
R\longrightarrow\prod_{\mathfrak p\in\operatorname{Ass}(R)}R_{\mathfrak p}
\]

is injective. Indeed, if its kernel \(K\) were nonzero, Theorem 1.2 would supply \(0\ne x\in K\) with prime annihilator \(\mathfrak p\). This prime is associated to \(R\), and no element outside it can kill \(x\). Thus \(x/1\ne0\) in \(R_{\mathfrak p}\), contradicting membership in \(K\). A nilpotent element maps to zero in every field in this product, so injectivity makes it zero in \(R\). Hence \(R\) is reduced. The zero ring is reduced, has no associated or minimal primes, and satisfies the localization condition vacuously.

**Solution 8.5.** Delete primes contained in other primes in the given finite family. This preserves its union and leaves pairwise incomparable primes \(\mathfrak p_1,\ldots,\mathfrak p_r\). If \(J\) were contained in none of them, choose \(a_i\in J\setminus\mathfrak p_i\). For every \(j\ne i\), choose \(b_{ij}\in\mathfrak p_j\setminus\mathfrak p_i\), and put \(c_i=\prod_{j\ne i}b_{ij}\), with empty product \(1\). Then \(c_i\) belongs to every \(\mathfrak p_j\) except \(\mathfrak p_i\), and is outside \(\mathfrak p_i\) by primality. Consider

\[
a=\sum_{i=1}^r a_i c_i\in J.
\]

Modulo \(\mathfrak p_i\), all summands except \(a_i c_i\) vanish, and this remaining summand is nonzero. Thus \(a\) is outside every prime in the family, contradicting containment of \(J\) in their union. This proves avoidance. An ideal cannot be contained in an empty union, so that case has no hypothesis to satisfy. For a nonzero Noetherian ring, Theorems 1.2 and 2.2 express its zero divisors as the union of finitely many associated primes. Apply avoidance to that union to obtain the required associated prime containing \(J\).

**Solution 8.6.** Take the two decompositions in Section 7. For completeness, monomial membership is a termwise test for ideals generated by monomials: all products of generators with monomials span precisely the monomials divisible by a generator, and polynomial monomials are linearly independent. A monomial in \((x)\cap(x^2,y)\) must either have \(x\)-exponent at least two, or have both \(x\)- and \(y\)-exponents positive. These are exactly the monomials in \((x^2,xy)\). In \((x)\cap(x,y)^2\), a monomial has positive \(x\)-exponent and total degree at least two, giving exactly the same alternatives. Hence both intersections equal \(I\).

The ideal \((x)\) is prime. In the quotient by \((x^2,y)\), every element is \(a+b\bar x\); if \(a\ne0\), its inverse is \(a^{-1}-ba^{-2}\bar x\), while if \(a=0\) it is square-zero. Thus this ideal is \((x,y)\)-primary. Solution 8.2 proves that \((x,y)^2\) is also \((x,y)\)-primary. The elements \(x\) and \(y\), or \(x\) and \(y^2\), establish irredundancy as in Section 7. Theorem 6.1 yields exactly the associated primes \((x)\) and \((x,y)\). The latter is embedded, and its two components differ because \(y\) belongs to \((x^2,y)\) but not to \((x,y)^2\), whose degree-one part is zero. Finally \(y\notin(x)\) becomes a unit at \((x)\), so \(IR_{(x)}=(x)R_{(x)}\). If \(sf\in(x)\) for \(s\notin(x)\), primality implies \(f\in(x)\). Thus the inverse image is \((x)\), recovering the unique minimal component.

## References

- The Stacks project authors, *The Stacks project*, Commutative Algebra, through the AI Integrated Stacks Project English edition: [Tag 02M3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-ass), [Tag 00LB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-ass-filter), [Tag 00LC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-finite-ass), [Tag 00LD](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-ass-zero-divisors), [Tag 0310](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-associated-primes-localize), [Tag 05BZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-localize-ass), and [Tag 02CE](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-proposition-minimal-primes-associated-primes). These cover associated primes, localization and support. The three primary-decomposition theorems in Sections 5–6 are proved here in full; no primary-decomposition theorem is attributed to these tags. The course introduction describes the edition and its attribution.
- Ravi Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, public draft of 27 July 2024, Section 6.6. [Author’s public draft](https://math.stanford.edu/~vakil/216blog/FOAGjul2724public.pdf).
- James S. Milne, *A Primer of Commutative Algebra*, version 4.03, 23 March 2020, Section 19. [Author’s freely accessible notes](https://www.jmilne.org/math/xnotes/CA.pdf). The notes prove the ideal case and state the module extension; the complete module proofs are given in Sections 4–6 of this lesson.


