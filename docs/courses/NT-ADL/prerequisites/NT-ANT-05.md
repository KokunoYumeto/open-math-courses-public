# Decomposition of primes in extensions

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Independent full-lesson AI review is pending. Public domain (CC0).*

A prime ideal of a smaller ring can become several prime ideals in a larger ring. Each resulting prime has a multiplicity and a residue field. These two pieces of information account for the whole degree of a finite extension. Polynomial factorization often reveals them, but only when the chosen generator describes the ring correctly at the prime in question.

## What this lesson assumes

We use the ideal factorization theorem, invertibility of fractional ideals, discrete valuation localizations, and Chinese remainders from *Discrete valuation rings and Dedekind domains*. We also use projectivity of finite torsion-free modules over a Dedekind domain and the diagonalization of matrices over a discrete valuation ring from *Norms of ideals, the ideal class group, and modules over Dedekind domains*. The determinant definitions of trace and norm, integrality, and integral bases come from the first two lessons.

Throughout the general part, \(A\) is a Dedekind domain, \(F=\operatorname{Frac}(A)\), \(L/F\) is finite and separable of degree \(n\), and \(B\) is the integral closure of \(A\) in \(L\). Dedekind domains here are not fields. If fields are included in that convention, the closure assertion below reduces to \(B=L\); the assertions about nonzero primes have no instances.

We use two general algebra results with precise locators. A short exact sequence of modules of finite length has additive lengths [Stacks, Tag 00IV]. For a finite field extension \(E/k\), the pairing \((x,y)\mapsto\operatorname{Tr}_{E/k}(xy)\) is nondegenerate exactly when \(E/k\) is separable [Stacks, Tag 0BIL]. Neither assertion requires characteristic zero.

## The larger ring is still Dedekind

**Theorem 5.1.** The ring \(B\) is a finite \(A\)-module and a Dedekind domain. Its fraction field is \(L\), and its rank over \(A\) is \(n\).

**Proof.** Any algebraic element \(u\in L\) can be multiplied by a nonzero element \(d\in A\) to become integral over \(A\): choose \(d\) clearing all coefficients of a monic polynomial for \(u\) over \(F\). If that polynomial has coefficients \(c_j\), the polynomial for \(du\) has coefficients \(d^jc_j\in A\). Scale an \(F\)-basis in this way to obtain a basis \(b_1,\ldots,b_n\) contained in \(B\).

The trace pairing on \(L/F\) is nondegenerate. Let
\[
G=(\operatorname{Tr}_{L/F}(b_i b_j))_{i,j}.
\]
Its entries belong to \(A\). Indeed, the conjugates of an integral element are integral, their sum is integral, and the trace lies in \(F\); the integral closedness of \(A\) puts it in \(A\). For \(x=\sum_i x_i b_i\in B\), every \(\operatorname{Tr}(xb_j)\) also belongs to \(A\). Consequently its coordinate column lies in \(G^{-1}A^n\). This is a finite \(A\)-module, isomorphic to \(A^n\), and \(B\) is an \(A\)-submodule of it. Since \(A\) is Noetherian, \(B\) is a finite \(A\)-module.

Every ideal of \(B\) is now finite as an \(A\)-module. The same generators generate it as a \(B\)-ideal, so \(B\) is Noetherian. Integrality is transitive: an element of \(L\) integral over \(B\) is integral over \(A\), and hence lies in \(B\). Thus \(B\) is integrally closed. The denominator argument at the start gives \(F B=L\), and also gives \(\operatorname{Frac}(B)=L\).

Let \(\mathfrak Q\ne0\) be a prime of \(B\), and choose \(0\ne b\in\mathfrak Q\). The monic minimal polynomial of \(b\) over \(F\) has coefficients in \(A\), because \(A\) is integrally closed and \(b\) is integral. Its constant coefficient \(c\) is nonzero and belongs to \(bB\). Therefore \(0\ne c\in\mathfrak Q\cap A\). This contraction is a maximal ideal \(\mathfrak p\) of \(A\). The domain \(B/\mathfrak Q\) is finite dimensional over \(A/\mathfrak p\). Multiplication by any nonzero element is injective and therefore surjective, so this domain is a field. Every nonzero prime of \(B\) is maximal.

Finally \(B\) is not a field. Otherwise \(1/a\in B\) for every \(a\in A\setminus\{0\}\); since \(1/a\in F\) is integral over \(A\), normality would put it in \(A\), making \(A\) a field. The proved properties characterize a Dedekind domain. Tensoring with \(F\) gives \(L\), so the rank is \(n\). \(\square\)

The finiteness argument uses separability in an essential place: the invertible trace matrix bounds every integral element in one finite module. No global relative integral basis was assumed.

## Multiplicity, residue degree, and the fundamental identity

Fix a nonzero prime \(\mathfrak p\) of \(A\). Put \(\kappa=A/\mathfrak p\) and \(R=A_{\mathfrak p}\). Since \(B\) is finite and torsion-free over \(A\), \(B_{\mathfrak p}=B\otimes_A R\) is free over the discrete valuation ring \(R\), of rank \(n\). Thus
\[
B/\mathfrak pB \cong B_{\mathfrak p}/\mathfrak pB_{\mathfrak p},
\qquad
\dim_\kappa(B/\mathfrak pB)=n. \tag{1}
\]
The first isomorphism holds because every element of \(A\setminus\mathfrak p\) already acts invertibly on the \(\kappa\)-vector space on the left. In particular \(\mathfrak pB\) is proper.

Write its ideal factorization as
\[
\mathfrak pB=\prod_{i=1}^g\mathfrak P_i^{e_i}.
\]
Its prime divisors are exactly the primes of \(B\) over \(\mathfrak p\): a prime containing \(\mathfrak pB\) has contraction \(\mathfrak p\), and the reverse containment is immediate. Define
\[
e_i=e(\mathfrak P_i\mid\mathfrak p),
\qquad
f_i=f(\mathfrak P_i\mid\mathfrak p)
=[B/\mathfrak P_i:\kappa].
\]
The integer \(e_i\) is the **ramification index**, \(f_i\) the **residue degree**, and \(g\) the number of primes above \(\mathfrak p\).

**Theorem 5.2 (fundamental identity).** With these definitions,
\[
\sum_{i=1}^g e_i f_i=n. \tag{2}
\]
The relative norm of fractional ideals is the multiplicative homomorphism defined on prime ideals by
\[
N_{L/F}(\mathfrak P)=
(\mathfrak P\cap A)^{f(\mathfrak P\mid\mathfrak P\cap A)}.
\]
For every nonzero fractional ideal \(\mathfrak a\) of \(A\),
\[
N_{L/F}(\mathfrak aB)=\mathfrak a^n. \tag{3}
\]
For every \(\beta\in L^\times\), it also satisfies
\[
N_{L/F}(\beta B)=N_{L/F}(\beta)A, \tag{4}
\]
where the norm on the right is the field norm.

**Proof.** Chinese remainders give
\[
B/\mathfrak pB\cong\prod_i B/\mathfrak P_i^{e_i}.
\]
Each quotient on the right has a filtration with factors
\(\mathfrak P_i^j/\mathfrak P_i^{j+1}\), for \(0\leq j<e_i\).
Such a factor is killed by \(\mathfrak P_i\); localizing at \(\mathfrak P_i\) does not change it. In the discrete valuation ring \(B_{\mathfrak P_i}\), it is one dimensional over \(B/\mathfrak P_i\). Its dimension over \(\kappa\) is therefore \(f_i\). Adding the dimensions of the factors and using (1) proves (2).

Every nonzero prime of \(B\) contracts to a nonzero prime of \(A\), by Theorem 5.1. Unique factorization of fractional ideals consequently makes the displayed prime assignment extend uniquely to a multiplicative homomorphism. Applying it to \(\mathfrak pB\) gives \(\mathfrak p^{\sum e_i f_i}=\mathfrak p^n\). Factoring \(\mathfrak a\), with arbitrary integer exponents, proves (3).

For (4), first take \(0\ne\beta\in B\). Multiplication by \(\beta\) on the free \(R\)-module \(B_{\mathfrak p}\) has determinant \(N_{L/F}(\beta)\). Diagonalization over the discrete valuation ring gives
\[
v_{\mathfrak p}(N_{L/F}(\beta))
=\operatorname{length}_R(B_{\mathfrak p}/\beta B_{\mathfrak p}).
\]
Indeed, a diagonal entry \(u\pi^m\), with \(u\) a unit, contributes \(m\) to both sides. On the other hand, factorization of \(\beta B\), localization at \(A\setminus\mathfrak p\), and Chinese remainders decompose this quotient into the prime-power factors at the \(\mathfrak P\) over \(\mathfrak p\). Each of their successive factors is \(B/\mathfrak P\), whose length as an \(R\)-module is its \(\kappa\)-dimension \(f(\mathfrak P\mid\mathfrak p)\). Additivity of length yields
\[
v_{\mathfrak p}(N_{L/F}(\beta))
=\sum_{\mathfrak P\mid\mathfrak p}
 f(\mathfrak P\mid\mathfrak p)\,v_{\mathfrak P}(\beta). \tag{5}
\]
These are precisely the prime exponents of \(N_{L/F}(\beta B)\). Equality at every prime of \(A\) proves (4) for integral \(\beta\).

For arbitrary \(\beta\in L^\times\), choose \(0\ne a\in A\) with \(a\beta\in B\). Apply the integral case to \(a\beta\), use (3) for \(aA\), and cancel \(a^n\). The field identity \(N_{L/F}(a\beta)=a^nN_{L/F}(\beta)\) gives (4). \(\square\)

In a tower \(F\subseteq L\subseteq M\) of finite separable extensions, ideal norms are transitive. For a prime of the top integral closure, the residue degrees multiply by the field degree formula. The two successive prime-ideal assignments therefore equal the direct one, and multiplicativity extends this equality to every fractional ideal. For number fields over \(\mathbf Q\), this relative ideal norm recovers the absolute norm: a prime over \(p\) has absolute norm \(p^f\).

## Reading primes from a polynomial

Let \(\alpha\in B\) generate \(L\) over \(F\), and let \(f(X)\in A[X]\) be its monic minimal polynomial. The correct local condition is
\[
B_{\mathfrak p}=R[\alpha]. \tag{6}
\]
Equivalently, \((B/A[\alpha])_{\mathfrak p}=0\). Over \(A=\mathbf Z\) this says that the rational prime \(p\) does not divide the integer index \([B:\mathbf Z[\alpha]]\). Over a general ring of integers, the quotient is a torsion \(A\)-module; its vanishing at \(\mathfrak p\), rather than divisibility of an unspecified integer index, is the condition to use.

**Theorem 5.3 (Kummer–Dedekind).** Suppose (6) holds and
\[
\overline f=\prod_{i=1}^g \overline g_i^{\,m_i}
\quad\text{in }\kappa[X],
\]
where the \(\overline g_i\) are distinct monic irreducible polynomials. Choose monic lifts \(g_i\in A[X]\). Then
\[
\mathfrak pB=\prod_i\mathfrak P_i^{m_i},
\qquad
\mathfrak P_i=\mathfrak pB+g_i(\alpha)B,
\qquad
f(\mathfrak P_i\mid\mathfrak p)=\deg\overline g_i. \tag{7}
\]

**Proof.** Polynomial division by the monic \(f\) shows that \(R[\alpha]\cong R[X]/(f)\): a remainder of degree less than \(n\) vanishing at \(\alpha\) is zero over \(F\), and hence over \(R\). Reducing (6) gives
\[
C:=B/\mathfrak pB\cong\kappa[X]/(\overline f)
\cong\prod_i\kappa[X]/(\overline g_i^{\,m_i}). \tag{8}
\]
The maximal ideals of \(C\) are the inverse images of the ideals generated by \(\overline g_i\) in these factors. In \(B\), these inverse images are exactly the displayed \(\mathfrak P_i\), and their residue fields are \(\kappa[X]/(\overline g_i)\). This proves primality, completeness of the list, and the residue degree.

It remains to identify the exponents, rather than just their sum. The local factor \(\kappa[X]/(\overline g_i^{\,m_i})\) has maximal ideal generated by \(\overline g_i\). Its nilpotency index is exactly \(m_i\): its \(m_i\)-th power is zero and its \((m_i-1)\)-st power is nonzero. From the ideal factorization in Theorem 5.2, the same local factor is \(B/\mathfrak P_i^{e_i}\). Localizing at \(\mathfrak P_i\), its maximal ideal is generated by a uniformizer and has nilpotency index exactly \(e_i\). Thus \(e_i=m_i\). \(\square\)

The notation \((\mathfrak p,g_i(\alpha))\) in this theorem denotes an ideal of the full ring \(B\). A repeated factor of a polynomial is evidence of ramification only after the local condition (6) has been checked.

## Discriminants detect ramification

A prime \(\mathfrak P\) above \(\mathfrak p\) is **unramified** when
\[
e(\mathfrak P\mid\mathfrak p)=1
\quad\text{and}\quad
B/\mathfrak P\text{ is separable over }\kappa.
\]
The prime \(\mathfrak p\) is unramified in \(B\) when all primes above it are unramified. Otherwise it ramifies. Over finite residue fields the separability condition is automatic; over imperfect fields it is part of the definition.

For completeness, a finite field of characteristic \(p\) has bijective Frobenius \(x\mapsto x^p\). If an irreducible polynomial over it had derivative zero, all its exponents would be divisible by \(p\); taking \(p\)-th roots of its coefficients would express it as a \(p\)-th power, a contradiction. Thus its finite field extensions are separable.

For an \(F\)-basis \(c_1,\ldots,c_n\) contained in \(B\), put
\[
\operatorname{disc}(c_1,\ldots,c_n)
=\det(\operatorname{Tr}_{L/F}(c_i c_j)).
\]
These nonzero elements lie in \(A\). The **relative discriminant ideal**
\(\mathfrak d_{B/A}\) is the ideal they generate. This definition works even when \(B\) has no basis over \(A\).

At \(\mathfrak p\), choose an \(R\)-basis \(u_1,\ldots,u_n\) of \(B_{\mathfrak p}\). Then
\[
\mathfrak d_{B/A}R
=\operatorname{disc}(u_1,\ldots,u_n)R. \tag{9}
\]
Every tuple from \(B\) has coordinates in \(R\); the change of basis formula multiplies the discriminant by the square of its determinant in \(R\). This proves one containment. Conversely, multiply each \(u_i\) by a denominator in \(A\setminus\mathfrak p\) to obtain elements of \(B\). They form an \(F\)-basis, and their discriminant differs from that of the \(u_i\) by a unit of \(R\). This proves the other containment.

We need the following elementary bridge between algebras and trace forms.

**Trace lemma.** If \(C\) is a finite dimensional commutative algebra over a field \(k\), the pairing
\[
(x,y)\longmapsto\operatorname{Tr}_k(m_{xy})
\]
is nondegenerate exactly when \(C\) is a product of finite separable field extensions of \(k\). Here \(m_z\) means multiplication by \(z\) on \(C\).

**Proof.** A nilpotent \(z\in C\) satisfies \((zx)^r=0\) for every \(x\) and some \(r\). Thus \(m_{zx}\) is nilpotent and has trace zero. If the pairing is nondegenerate, \(z=0\), so \(C\) is reduced.

Every prime ideal of \(C\) is maximal: its quotient is a finite dimensional domain over \(k\), hence a field. There are only finitely many maximal ideals. Indeed, Chinese remainders for any finite list of distinct ones give a surjection onto the product of their residue fields; the length of such a list is at most \(\dim_k C\).

Their intersection is the nilradical. To see the nontrivial direction, if \(z\) is not nilpotent, \(C[1/z]\ne0\). A maximal ideal of this ring pulls back to a prime ideal of \(C\) avoiding \(z\), which is a maximal ideal by the preceding paragraph. For reduced \(C\), the intersection is therefore zero. Chinese remainders identify \(C\) with the product of its residue fields.

On a product of fields, multiplication matrices and trace pairings are block diagonal. A block is nondegenerate exactly when its field extension is separable [Stacks, Tag 0BIL]. This proves both directions. \(\square\)

**Theorem 5.4 (discriminant criterion).** The following are equivalent:

1. \(\mathfrak p\) is unramified in \(B\).
2. \(B/\mathfrak pB\) is a product of finite separable extensions of \(\kappa\).
3. The trace pairing of the \(\kappa\)-algebra \(B/\mathfrak pB\) is nondegenerate.
4. \(\mathfrak p\) does not divide \(\mathfrak d_{B/A}\).

Only finitely many primes of \(A\) ramify in \(B\).

**Proof.** Chinese remainders express \(B/\mathfrak pB\) as the product of \(B/\mathfrak P_i^{e_i}\). A factor is reduced exactly when \(e_i=1\). For \(e_i>1\), its localization at \(\mathfrak P_i\) has a nonzero nilpotent uniformizer class; the quotient is unchanged by this localization. For \(e_i=1\), it is the field \(B/\mathfrak P_i\). Hence conditions 1 and 2 are equivalent. The trace lemma proves the equivalence of 2 and 3.

Use an \(R\)-basis of \(B_{\mathfrak p}\). Multiplication by each element has a matrix over \(R\), and reduction modulo its maximal ideal gives its multiplication matrix on \(B/\mathfrak pB\). Taking traces commutes with this reduction. Thus the Gram matrix of the residue trace pairing is the reduction of the Gram matrix in (9). It is nonsingular exactly when its determinant is a unit in \(R\), which is condition 4.

Finally, separability of \(L/F\) supplies a nonzero basis discriminant, so \(\mathfrak d_{B/A}\ne0\). A nonzero ideal in a Dedekind domain has only finitely many prime divisors. \(\square\)

For a number field \(K\), \(A=\mathbf Z\) and \(B=\mathcal O_K\) have an integral basis, so \(\mathfrak d_{B/A}=d_K\mathbf Z\). The theorem says that \(p\) ramifies in \(K\) exactly when \(p\mid d_K\). More generally it applies to \(\mathcal O_L/\mathcal O_K\) without a relative integral basis. Indeed, the integral closure of \(\mathcal O_K\) in \(L\) is \(\mathcal O_L\), by transitivity of integrality over \(\mathbf Z\). The field extension \(L/F\) being separable does not by itself make its residue field extensions separable; this is why that hypothesis remains visible in condition 1.

## The quadratic decomposition law

Let \(d\ne1\) be a nonzero squarefree integer, of either sign, let \(K=\mathbf Q(\sqrt d)\), and write \(s=\sqrt d\). The integral basis theorem gives
\[
\mathcal O_K=
\begin{cases}
\mathbf Z[(1+s)/2],&d\equiv1\pmod4,\\
\mathbf Z[s],&d\equiv2,3\pmod4,
\end{cases}
\qquad
D=d_K=
\begin{cases}
d,&d\equiv1\pmod4,\\
4d,&d\equiv2,3\pmod4.
\end{cases}
\]
A rational prime **splits** if there are two primes with \(e=f=1\); it is **inert** if there is one prime with \(e=1,f=2\); it **ramifies** here if there is one prime with \(e=2,f=1\).

**Corollary 5.5.** For an odd prime \(p\), the decomposition is
\[
\begin{array}{c|c}
\text{condition}&\text{decomposition}\\ \hline
p\mid D&\text{ramified}\\
p\nmid D,\ (d/p)=1&\text{split}\\
p\nmid D,\ (d/p)=-1&\text{inert}.
\end{array}
\]
Here \((d/p)\) is the Legendre symbol. At \(2\) the law is
\[
\begin{array}{c|c}
d\equiv2,3\pmod4&\text{ramified}\\
d\equiv1\pmod8&\text{split}\\
d\equiv5\pmod8&\text{inert}.
\end{array}
\]

**Proof.** At odd \(p\), the ring of integers localized at \(p\) is \(\mathbf Z_{(p)}[s]\), because \(2\) is invertible there. Apply Theorem 5.3 to \(X^2-d\). If \(p\mid d\), its reduction is \(X^2\), giving
\[
(p)=(p,s)^2.
\]
If \(d\) is a nonzero square modulo \(p\), choose \(a\) with \(a^2\equiv d\); the two distinct linear factors give
\[
(p)=(p,s-a)(p,s+a).
\]
If \(d\) is a nonsquare, the polynomial is irreducible and \((p)\) is prime, of residue degree two. For odd \(p\), divisibility of \(D\) is the same as divisibility of \(d\).

At \(2\), if \(d\equiv2\pmod4\), the integral generator is \(s\) and its polynomial reduces to \(X^2\). If \(d\equiv3\pmod4\), it reduces to \((X+1)^2\). Thus respectively
\[
(2)=(2,s)^2,\qquad (2)=(2,1+s)^2.
\]
If \(d\equiv1\pmod4\), use \(\omega=(1+s)/2\), whose polynomial is
\[
X^2-X+\frac{1-d}{4}.
\]
For \(d\equiv1\pmod8\) its reduction is \(X(X+1)\), giving
\((2)=(2,\omega)(2,\omega-1)\). For \(d\equiv5\pmod8\) its reduction is \(X^2+X+1\), which has no root in \(\mathbf F_2\), and \((2)\) is inert. Every case satisfies \(ef=2\) or \(1+1=2\). \(\square\)

## Three fields, with their actual prime ideals

In \(\mathbf Z[i]\),
\[
2=-i(1+i)^2,\qquad (2)=(1+i)^2.
\]
The residue field of \((1+i)\) is \(\mathbf F_2\), so \(e=2,f=1\). For an odd prime, \(-1\) is a square modulo \(p\) exactly when \(p\equiv1\pmod4\): the cyclic group \(\mathbf F_p^\times\) contains an element of order four exactly in that case. Such a prime splits as \((p,i-a)(p,i+a)\), where \(a^2\equiv-1\); a prime congruent to \(3\pmod4\) is inert. The degree checks are \(1+1=2\) and \(1\cdot2=2\).

Here is the elementary cyclicity argument used in this example. If \(G\) is a finite subgroup of a field's multiplicative group, let \(m\) be the least common multiple of its element orders. For each prime power dividing \(m\), some element has an order divisible by that prime power; raising that element to a suitable power gives an element of exactly that order. The product of these elements has order \(m\), because their orders are relatively prime and they commute. Every member of \(G\) is a root of \(X^m-1\), so \(\#G\leq m\). The element of order \(m\) gives the reverse inequality. Thus \(G\) is generated by that element. Applying this to \(\mathbf F_p^\times\) proves the assertion: an element of order four has square \(-1\), the unique element of order two, and a square root of \(-1\) has order four.

For \(K=\mathbf Q(\alpha)\), \(\alpha^3=2\), the integral basis calculation in *Discriminants and integral bases* proves \(\mathcal O_K=\mathbf Z[\alpha]\). Thus Theorem 5.3 applies at every prime.

| \(p\) | Factorization of \(X^3-2\) over \(\mathbf F_p\) | Factorization of \((p)\) in \(\mathcal O_K\) | \(\sum ef\) |
|---|---|---|---|
| \(2\) | \(X^3\) | \((2,\alpha)^3\) | \(3\cdot1=3\) |
| \(3\) | \((X+1)^3\) | \((3,\alpha+1)^3\) | \(3\cdot1=3\) |
| \(5\) | \((X-3)(X^2+3X+4)\) | \((5,\alpha-3)(5,\alpha^2+3\alpha+4)\) | \(1+2=3\) |
| \(7\) | irreducible | \((7)\), prime | \(1\cdot3=3\) |
| \(31\) | \((X-4)(X-7)(X-20)\) | \((31,\alpha-4)(31,\alpha-7)(31,\alpha-20)\) | \(1+1+1=3\) |

At \(5\), the quadratic factor has discriminant \(3\), a nonsquare modulo \(5\). At \(7\), the possible cubes are \(0,1,6\), so the cubic has no root and is irreducible. At \(31\), direct cubing gives \(4^3\equiv7^3\equiv20^3\equiv2\); these are three distinct roots. These observations verify every irreducibility assertion in the table. The first two primes are totally ramified: there is a single prime, with ramification index equal to the field degree.

For \(K=\mathbf Q(\sqrt{-5})\), put \(s=\sqrt{-5}\). Here \(\mathcal O_K=\mathbf Z[s]\) and \(D=-20\). The primes \(2\) and \(5\) ramify. The squares \(1\) modulo \(3\) and \(9\equiv2\) modulo \(7\) give
\[
(3)=(3,s-1)(3,s+1),
\qquad
(7)=(7,s-3)(7,s+3).
\]
At \(11\), \(-5\equiv6\) is not among the nonzero squares \(1,3,4,5,9\). At \(13\), \(-5\equiv8\) is not among \(1,3,4,9,10,12\). Hence \((11)\) and \((13)\) are inert primes. Each ramified prime has \(ef=2\), each split pair contributes \(1+1=2\), and each inert prime has \(ef=2\). Inert prime ideals have absolute norms \(11^2\) and \(13^2\), rather than \(11\) and \(13\).

## Exercises

1. **Easy.** Factor \(2,3,5,7\) in \(\mathcal O_{\mathbf Q(\sqrt{-5})}\), giving the prime ideals and their \(e,f\).
2. **Medium.** Let \(\alpha^3-\alpha-1=0\). Factor \(3,5,7\) in \(\mathbf Z[\alpha]\), and verify \(\sum ef=3\) in each case.
3. **Medium.** Derive the entire quadratic law at \(2\), using \(\omega=(1+\sqrt d)/2\) when \(d\equiv1\pmod4\). Explain why reducing \(X^2-d\) at \(2\) is insufficient in that case.
4. **Hard.** Let \(\alpha\) be a root of \(h(X)=X^3+X^2-2X+8\), and \(K=\mathbf Q(\alpha)\). Prove that \(2\) splits completely in \(\mathcal O_K\), and that \(\mathcal O_K\ne\mathbf Z[\theta]\) for every \(\theta\in\mathcal O_K\).

## Complete solutions

**1.** With \(s=\sqrt{-5}\), the integral generator \(s\) has polynomial \(X^2+5\). Its reductions at \(2,3,5,7\) are respectively
\[
(X+1)^2,\quad (X-1)(X+1),\quad X^2,\quad (X-3)(X+3).
\]
Consequently
\[
\begin{aligned}
(2)&=(2,1+s)^2,\\
(3)&=(3,s-1)(3,s+1),\\
(5)&=(5,s)^2,\\
(7)&=(7,s-3)(7,s+3).
\end{aligned}
\]
Each displayed prime has residue field \(\mathbf F_p\), so \(f=1\). The exponents are two at the ramified primes and one at both primes of a split pair. Thus the sum is two in all four cases. Primality and equality of the ideals follow from Theorem 5.3, not merely from matching their norms.

**2.** The cubic is irreducible over \(\mathbf Q\): neither possible rational root \(1\) nor \(-1\) is a root. Its discriminant is \(-23\), so the squarefree-discriminant criterion of *Discriminants and integral bases* gives \(\mathcal O_K=\mathbf Z[\alpha]\).

Modulo \(3\), evaluation at \(0,1,2\) always gives \(2\). Thus \(X^3-X-1\) has no root, is irreducible, and \((3)\) is prime with \(e=1,f=3\).

Modulo \(5\) and \(7\), respectively,
\[
\begin{aligned}
X^3-X-1&=(X-2)(X^2+2X+3)&&\text{over }\mathbf F_5,\\
X^3-X-1&=(X+2)(X^2+5X+3)&&\text{over }\mathbf F_7.
\end{aligned}
\]
The quadratic discriminants are \(2\) modulo \(5\) and \(6\) modulo \(7\), both nonsquares. Hence
\[
\begin{aligned}
(5)&=(5,\alpha-2)(5,\alpha^2+2\alpha+3),\\
(7)&=(7,\alpha+2)(7,\alpha^2+5\alpha+3).
\end{aligned}
\]
At each of these primes the two residue degrees are \(1,2\), and both exponents are one. The checks are \(1\cdot3=3\), \(1+2=3\), and \(1+2=3\).

**3.** For \(d\equiv2,3\pmod4\), the ring of integers is \(\mathbf Z[s]\). Reduction gives \(X^2\) in the first case and \((X+1)^2\) in the second. Theorem 5.3 gives \((2)=(2,s)^2\) or \((2)=(2,s+1)^2\), both with \(e=2,f=1\).

For \(d\equiv1\pmod4\), the full ring is \(\mathbf Z[\omega]\), and the polynomial of \(\omega\) is \(X^2-X+(1-d)/4\). If \(d\equiv1\pmod8\), its constant coefficient is even, so its reduction is \(X(X+1)\); the distinct factors give \((2)=(2,\omega)(2,\omega-1)\), with \(e=f=1\) at both primes. If \(d\equiv5\pmod8\), the constant coefficient is odd, so the reduction is the irreducible \(X^2+X+1\); now \((2)\) is prime with \(e=1,f=2\). The order \(\mathbf Z[s]\) has index two in \(\mathbf Z[\omega]\), so it fails the local hypothesis at \(2\); its polynomial cannot determine this decomposition.

**4.** None of the possible rational roots \(\pm1,\pm2,\pm4,\pm8\) is a root of \(h\); hence \(h\) is irreducible. Define
\[
\beta=\frac{\alpha^2+\alpha}{2}.
\]
Using \(h(\alpha)=0\) gives the three relations
\[
\alpha^2=2\beta-\alpha,\qquad
\alpha\beta=\alpha-4,\qquad
\beta^2=\beta-2\alpha-2. \tag{10}
\]
Thus the lattice \(C=\mathbf Z+\mathbf Z\alpha+\mathbf Z\beta\) is a ring. The multiplication matrix of \(\beta\) on the basis \(1,\alpha,\beta\) is
\[
\begin{pmatrix}
0&-4&-2\\
0&1&-2\\
1&0&1
\end{pmatrix}.
\]
Its characteristic polynomial is \(T^3-2T^2+3T-10\). By Cayley–Hamilton, applied to \(1\), this monic polynomial annihilates \(\beta\), so \(\beta\) is integral and \(C\subseteq\mathcal O_K\).

The change of basis determinant from \(1,\alpha,\alpha^2\) to \(1,\alpha,\beta\) is \(1/2\). Since \(\operatorname{disc}(h)=-2012=-4\cdot503\), we get
\[
\operatorname{disc}(1,\alpha,\beta)=-503.
\]
For direct verification its trace matrix is
\[
\begin{pmatrix}
3&-1&2\\
-1&5&-13\\
2&-13&-2
\end{pmatrix},
\]
whose determinant is \(-503\). The number \(503\) is prime: trial division by \(2,3,5,7,11,13,17,19\), the primes below \(\sqrt{503}<23\), gives no divisor. The discriminant index formula
\(\operatorname{disc}(C)=[\mathcal O_K:C]^2d_K\) therefore forces \([\mathcal O_K:C]=1\). We have proved
\[
\mathcal O_K=\mathbf Z+\mathbf Z\alpha+\mathbf Z\beta,
\qquad
[\mathcal O_K:\mathbf Z[\alpha]]=2.
\]

Modulo \(2\), (10) becomes
\[
\alpha^2=\alpha,\qquad \beta^2=\beta,\qquad \alpha\beta=\alpha.
\]
There are three evaluation homomorphisms to \(\mathbf F_2\), corresponding to
\[
(\alpha,\beta)=(0,0),\ (0,1),\ (1,1).
\]
Together they give an isomorphism \(\mathcal O_K/2\mathcal O_K\to\mathbf F_2^3\). Indeed, the matrix of this linear map on \(1,\alpha,\beta\) is
\[
\begin{pmatrix}1&0&0\\1&0&1\\1&1&1\end{pmatrix},
\]
which is invertible modulo \(2\). Its three kernels lift to the distinct prime ideals
\[
\begin{aligned}
\mathfrak P_{00}&=(2,\alpha,\beta),\\
\mathfrak P_{01}&=(2,\alpha,\beta-1),\\
\mathfrak P_{11}&=(2,\alpha-1,\beta-1).
\end{aligned}
\]
The quotient is reduced, so all exponents are one. All residue fields are \(\mathbf F_2\), so
\[
(2)=\mathfrak P_{00}\mathfrak P_{01}\mathfrak P_{11},
\qquad
\sum ef=1+1+1=3.
\]

Suppose now that \(\mathcal O_K=\mathbf Z[\theta]\) for some integral \(\theta\). Then its quotient modulo \(2\) would be generated as an \(\mathbf F_2\)-algebra by the image of \(\theta\). In \(\mathbf F_2^3\), any triple has two equal coordinates. Every polynomial in that triple has those same two coordinates equal, so cannot generate the whole product. This contradiction excludes every \(\theta\).

Notice the failure of the tempting calculation with \(h\): modulo \(2\), it is \(X^2(X+1)\), which would suggest two primes, one with exponent two. The index is divisible by \(2\), so Theorem 5.3 does not apply to \(\alpha\) there. The actual decomposition has three unramified primes.

## What this lesson does not prove

For a finite field extension, separability is equivalent to nondegeneracy of its trace pairing; this is [Stacks, Tag 0BIL]. The additivity of finite module length in a short exact sequence is [Stacks, Tag 00IV]. We use the ideal factorization, localization and module theorems proved in the preceding two lessons, and the discriminant index formula and quadratic and pure cubic integral bases proved in *Discriminants and integral bases*.

Hilbert's decomposition and inertia groups are treated in the next lesson. The relation with completions and the scheme interpretation of unramifiedness belong to the courses on local fields and on finite separable and étale morphisms; neither is used as an unproved step here.

## References

- **[Milne ANT]** J. S. Milne, *Algebraic Number Theory*, version 3.08 (2020), Chapter 3, Theorems 3.29, 3.34, 3.35 and 3.41, Proposition 3.44, pp. 57–64; Chapter 4, Proposition 4.1, pp. 68–69. [Lecture notes](https://www.jmilne.org/math/CourseNotes/ANT.pdf).
- **[Hecke 1923]** Erich Hecke, [*Vorlesungen über die Theorie der algebraischen Zahlen*](https://archive.org/details/vorlesungenber00heckuoft), Leipzig, 1923, Chapter V, §29, quadratic decomposition.
- **[Stacks]** The Stacks project, [Tag 00IV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-length-additive), additivity of length, and [Tag 0BIL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/fields.html#fields-lemma-separable-trace-pairing), separability and the trace pairing.
