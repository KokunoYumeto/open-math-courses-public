# Dirichlet characters

*Written by GPT-6.1 Sol (OpenAI) in Codex at Ultra, October 2026. Self-checked by the writing AI, GPT-6.1 Sol, at Ultra. Public domain (CC0).*

An arithmetic progression is easy to recognize under addition, whereas prime factorization is multiplicative. Dirichlet characters connect these two structures. They express the indicator of a reduced residue class as a finite sum of multiplicative functions. Their conductors then tell us which modulus actually carries the information.

We assume the elementary language of groups and fields and the Chinese remainder theorem. The finite group, primitive-root and quadratic-reciprocity arguments needed here are proved below. Basic references are Koukoulopoulos's *The Distribution of Prime Numbers* and Sutherland's lectures on Dirichlet characters.

## 1. Detecting a residue class

A character of a finite abelian group \(G\) is a homomorphism \(G\to\mathbb C^\times\). Its values are roots of unity, because \(\chi(g)^{|G|}=1\). In particular, \(\overline{\chi(g)}=\chi(g)^{-1}\). The characters form a group \(\widehat G\) under pointwise multiplication.

**Lemma 1.1 (extension).** A character of a subgroup \(H\subset G\) extends to a character of \(G\). There are exactly \([G:H]\) extensions.

**Proof.** Suppose first that we adjoin one element \(g\). Let \(m\) be the least positive integer for which \(g^m\in H\). Choose a root \(z\) of \(z^m=\chi(g^m)\), and define

\[
\widetilde\chi(hg^j)=\chi(h)z^j.
\]

If \(hg^j=h'g^{j'}\), then \(j-j'=km\) and \(h'=hg^{km}\). The displayed value is therefore independent of the representation. It is multiplicative, extends \(\chi\), and has value \(z\) at \(g\). Conversely every extension has one of the \(m\) possible values of \(z\). Since \([\langle H,g\rangle:H]=m\), adjoining finitely many elements gives the assertion, with the extension counts multiplying. \(\square\)

Starting with the trivial subgroup shows that \(|\widehat G|=|G|\). Moreover, characters separate points: for \(g\ne1\), choose on \(\langle g\rangle\) the character taking \(g\) to a primitive root of order \(\operatorname{ord}(g)\), and extend it.

**Theorem 1.2 (orthogonality).** For \(\chi\in\widehat G\) and \(g\in G\),

\[
\sum_{h\in G}\chi(h)=|G|\,1_{\chi=1},
\qquad
\sum_{\chi\in\widehat G}\chi(g)=|G|\,1_{g=1}.
\]

**Proof.** If \(\chi\ne1\), choose \(u\) with \(\chi(u)\ne1\). Multiplication by \(u\) permutes \(G\), so the first sum equals \(\chi(u)\) times itself and must vanish. For \(g\ne1\), choose \(\psi\) with \(\psi(g)\ne1\). Multiplication by \(\psi\) permutes \(\widehat G\), giving the same argument for the second sum. In the two remaining cases every summand is 1. \(\square\)

A **Dirichlet character modulo \(q\)** is a character of

\[
U_q=(\mathbb Z/q\mathbb Z)^\times
\]

extended to all integers by setting \(\chi(n)=0\) when \((n,q)>1\). Thus it is periodic and completely multiplicative. The principal character \(\chi_0\) is 1 on the units and 0 elsewhere. For \(q=1\), the unique character is the constant 1, including at 0.

If \((b,q)=1\), orthogonality gives the progression detector

\[
1_{n\equiv b\pmod q}
=\frac1{\varphi(q)}\sum_{\chi\bmod q}\overline{\chi(b)}\chi(n).
\tag{1.1}
\]

For a unit \(n\), apply Theorem 1.2 to \(nb^{-1}\). For a nonunit, both sides are zero. The condition on \(b\) is essential: characters vanish on nonunits and cannot detect their individual classes.

For any finite sequence \(a_n\), multiplying (1.1) by \(a_n\) and summing yields

\[
\sum_{n\equiv b\pmod q}a_n
=\frac1{\varphi(q)}\sum_{\chi\bmod q}\overline{\chi(b)}\sum_n a_n\chi(n).
\]

The principal character measures the average; the other characters measure departures from that average. This identity will be used with \(a_n=\Lambda(n)\) in the lessons on primes in progressions.

## 2. Constructing the characters locally

For an odd prime \(p\), choose a primitive root \(g\) modulo \(p^k\). Put \(h=\varphi(p^k)\). Every character is uniquely of the form

\[
\chi_j(g^r)=\exp(2\pi i jr/h),\qquad 0\le j<h.
\]

Here is the existence argument needed for this construction. A finite subgroup of the multiplicative group of a field is cyclic. Indeed, let \(m\) be the least common multiple of its element orders. For each prime dividing \(m\), take an element whose order contains the maximal power of that prime, and raise it to remove the other prime factors. Multiplying the resulting elements gives an element of order \(m\), because their orders are coprime. Every group element is a root of \(X^m-1\), so the polynomial root bound gives \(|G|\le m\). Lagrange's theorem gives \(m\mid|G|\), hence equality. Applied to \(\mathbb F_p^\times\), this supplies a generator \(g\) modulo \(p\).

Choose its integer lift so that \(g^{p-1}\not\equiv1\pmod {p^2}\). Such a lift exists among \(g\) and \(g+p\): their \((p-1)\)-st powers differ modulo \(p^2\) by \((p-1)g^{p-2}p\), a nonzero multiple of \(p\). For odd \(p\), the binomial theorem shows

\[
v_p\bigl((1+p^rc)^p-1\bigr)=r+1
\quad(r\ge1,\ p\nmid c).
\]

The first term has valuation \(r+1\), while every later term has larger valuation. Iteration gives \(v_p(g^{(p-1)p^j}-1)=j+1\). The order of \(g\) modulo \(p^k\) is a multiple of \(p-1\) and divides \((p-1)p^{k-1}\); the valuation formula forces it to equal the latter. This proves the primitive-root assertion for every odd prime power.

For powers of 2, \(U_2\) is trivial and \(U_4=\{1,-1\}\). If \(k\ge3\), every odd residue is uniquely

\[
(-1)^\epsilon5^r\pmod {2^k},\qquad
\epsilon\in\{0,1\},\quad r\in\mathbb Z/2^{k-2}\mathbb Z.
\]

Consequently the characters have independent parameters

\[
\chi((-1)^\epsilon5^r)
=(-1)^{a\epsilon}\exp(2\pi i jr/2^{k-2}),
\quad a\in\{0,1\},\quad 0\le j<2^{k-2}.
\]

Here is a short verification of the group description at 2. Induction by squaring gives

\[
v_2(5^{2^r}-1)=r+2\qquad(r\ge0).
\]

For the induction step, \(5^{2^r}+1\) has valuation 1, so factoring the next difference raises the valuation by 1. Hence 5 has order \(2^{k-2}\) modulo \(2^k\). Its powers are all 1 modulo 4, and their number equals the number of such units. Their negatives give exactly the remaining odd residues.

The Chinese remainder theorem gives

\[
U_q\simeq\prod_{p^k\parallel q}U_{p^k}.
\]

A character of a product restricts to a character on each factor, and its value on a tuple is the product of those restrictions. Conversely that product defines a character. Thus the local constructions list every character modulo every \(q\).

**Example 2.1 (modulo 5).** In the order \(1,2,3,4\), the four rows are

\[
\begin{array}{c|rrrr|c}
j&1&2&3&4&\text{conductor}\\\hline
0&1&1&1&1&1\\
1&1&i&-i&-1&5\\
2&1&-1&-1&1&5\\
3&1&-i&i&-1&5
\end{array}
\]

The entries use \(2^0,2^1,2^3,2^2\) for the four columns. At \(n=2\), the four character values sum to 0; at \(n=1\), they sum to 4. This is the detector (1.1) with \(b=1\).

![Two complex-plane diagrams: all four characters modulo 5 have value 1 at n equals 1, while their values at n equals 2 are 1, i, minus 1 and minus i, which cancel.](assets/orthogonality.png)

*Figure 1. The exact character values in Example 2.1. Dividing the sum by 4 detects the class 1 modulo 5. The coincident point in the left panel represents four values. The arrows in the right panel show their cancellation in Theorem 1.2.*

## 3. The smallest modulus that carries a character

If \(d\mid q\), the reduction map \(U_q\to U_d\) is onto. This follows locally for prime powers, and then from the Chinese remainder theorem. A character \(\psi\) modulo \(d\) **induces** the character modulo \(q\) defined by

\[
\chi(n)=\begin{cases}\psi(n),&(n,q)=1,\\0,&(n,q)>1.\end{cases}
\]

This formula does not assert equality on every integer: the extra prime divisors of \(q\) introduce extra zeros.

**Theorem 3.1 (conductor).** Every character modulo \(q\) is induced by a unique primitive character modulo a divisor \(q^*\) of \(q\). It is primitive precisely when, for every proper divisor \(d\mid q\), some unit \(u\equiv1\pmod d\) satisfies \(\chi(u)\ne1\).

**Proof.** A character descends to \(U_d\) exactly when it is trivial on the kernel of \(U_q\to U_d\). Surjectivity then makes the descended character unique. Write \(q=\prod p^{k_p}\) and decompose \(\chi\) into local characters. For each \(p\), the kernels of reduction to \(U_{p^c}\), \(0\le c\le k_p\), are nested. Let \(c_p\) be the least exponent through which the local character factors; \(c_p=0\) means the local character is trivial. The character factors through \(d=\prod p^{e_p}\) if and only if \(e_p\ge c_p\) for every \(p\). Therefore its unique least inducing modulus is \(q^*=\prod p^{c_p}\), and the descended character cannot descend further. The kernel criterion gives exactly the stated test for primitivity. \(\square\)

The sign at \(-1\) is unchanged by induction. We write \(a(\chi)\in\{0,1\}\) for the parity determined by \(\chi(-1)=(-1)^{a(\chi)}\).

The principal character has conductor 1, and is primitive only at modulus 1. This includes it in the conductor classification.

For \(\Re s>1\), absolute convergence and complete multiplicativity give an Euler product. Removing the primes newly excluded by \(q\) yields

\[
L(s,\chi)=L(s,\chi^*)
\prod_{p\mid q}\bigl(1-\chi^*(p)p^{-s}\bigr).
\tag{3.1}
\]

Primes dividing \(q^*\) contribute the factor 1. The full analytic justification is developed in Dirichlet's theorem on primes in arithmetic progressions.

**Example 3.2 (an extra zero).** The nonprincipal character modulo 3 has values 1 and \(-1\) on 1 and 2. Its lift modulo 6 has conductor 3 and vanishes also on the even integers. Since \(\chi_{-3}(2)=-1\),

\[
L(s,\chi\bmod6)=(1+2^{-s})L(s,\chi_{-3}).
\]

### Counting primitive characters

Let \(\varphi^*(q)\) denote the number of primitive characters modulo \(q\). Theorem 3.1 partitions all characters by conductor, so

\[
\varphi(q)=\sum_{d\mid q}\varphi^*(d).
\]

Möbius inversion, or multiplication by \(\mu\) in this divisor sum, gives

\[
\boxed{\varphi^*(q)=\sum_{d\mid q}\mu(q/d)\varphi(d).}
\tag{3.2}
\]

Both \(\mu\) and \(\varphi\) are multiplicative, so their convolution is multiplicative. Its local values are

\[
\varphi^*(1)=1,\qquad
\varphi^*(p)=p-2,\qquad
\varphi^*(p^k)=p^{k-2}(p-1)^2\quad(k\ge2).
\]

Every factor is positive except \(\varphi^*(2)=0\). Thus

\[
\varphi^*(q)=0\quad\Longleftrightarrow\quad q\equiv2\pmod4.
\]

## 4. Real characters and quadratic discriminants

A real character takes values \(\pm1\) on units. Equivalently it has square equal to the principal character. We first classify it locally, then identify the resulting characters with quadratic symbols.

### Quadratic signs and reciprocity

For an odd prime \(p\), the Legendre symbol \((a/p)\) is 0 when \(p\mid a\), 1 for a nonzero square modulo \(p\), and \(-1\) otherwise. The cyclic group construction in Section 2 shows it is multiplicative, and gives Euler's criterion \((a/p)\equiv a^{(p-1)/2}\pmod p\).

Put \(m=(p-1)/2\). For \(p\nmid a\), reduce \(a,2a,\ldots,ma\) to their unique signed representatives in \([-m,m]\), and let \(\nu\) count the negative ones. The absolute values of these representatives are a permutation of \(1,\ldots,m\): an equality of absolute values would give \(aj\equiv\pm ak\pmod p\), which forces \(j=k\) in this range. Taking their product and cancelling \(m!\) gives

\[
a^m\equiv(-1)^\nu\pmod p,
\qquad \left(\frac ap\right)=(-1)^\nu.
\tag{4.1}
\]

This is Gauss's lemma. At \(a=-1\), all \(m\) representatives are negative, so \((-1/p)=(-1)^m\). At \(a=2\), exactly \(m-\lfloor p/4\rfloor\) are negative. Checking \(p\equiv1,3,5,7\pmod8\) gives

\[
\left(\frac2p\right)=(-1)^{(p^2-1)/8}.
\]

To obtain reciprocity, let \(r\) be a distinct odd prime. If \(t_j\) is the least positive residue of \(rj\), then \(t_j=rj-p\lfloor rj/p\rfloor\). Replacing a residue above \(p/2\) by its absolute signed representative \(p-t_j\) changes its parity. The sum of all absolute representatives equals \(1+\cdots+m\). Since \(p\) and \(r\) are odd, comparison of these sums modulo 2 shows

\[
\nu\equiv\sum_{j=1}^m\left\lfloor\frac{rj}{p}\right\rfloor\pmod2.
\]

Now count the integer pairs \((j,k)\) in the rectangle \(1\le j\le(p-1)/2\), \(1\le k\le(r-1)/2\). The line \(rj=pk\) contains no such pair. The number below it is \(\sum_j\lfloor rj/p\rfloor\); the number above it is \(\sum_k\lfloor pk/r\rfloor\). Their sum is the size of the rectangle. Applying Gauss's lemma to both primes therefore proves

\[
\left(\frac rp\right)\left(\frac pr\right)
=(-1)^{(p-1)(r-1)/4}.
\tag{4.2}
\]

These three sign laws supply exactly the reciprocity input for the character classification that follows.

### Local real characters

At an odd prime power \(p^k\), the cyclic group has exactly two real characters. The nontrivial one takes a primitive root to \(-1\). Its kernel is the squares, and its value is \((n/p)\), the Legendre symbol. Reduction modulo \(p\) preserves whether a unit is a square, so this character has conductor \(p\).

At 2 the complete nontrivial possibilities have conductors 4 or 8. On odd integers they are

\[
\chi_{-4}(n)=(-1)^{(n-1)/2},\qquad
\chi_8(n)=(-1)^{(n^2-1)/8},\qquad
\chi_{-8}(n)=\chi_{-4}(n)\chi_8(n).
\tag{4.3}
\]

Indeed, a real character in the description of \(U_{2^k}\) is determined by its two signs at \(-1\) and 5. It is trivial on \(\langle5^2\rangle\), hence factors through 8 when \(k\ge3\). The four sign choices are exactly the principal character and (4.3); their least moduli follow from their values on residues.

Define a **fundamental discriminant** to be either a squarefree integer \(d\equiv1\pmod4\), or \(d=4m\) with squarefree \(m\equiv2,3\pmod4\). We include \(d=1\) for the trivial character. For a prime \(p\), put \(p^*=(-1)^{(p-1)/2}p\). Every such \(d\) has a unique expression

\[
d=d_2\prod_{p\in S}p^*,\qquad
d_2\in\{1,-4,8,-8\},
\tag{4.4}
\]

where \(S\) is a finite set of odd primes. To check existence directly, set \(P=\prod_{p\mid d,\ p\text{ odd}}p^*\). Then \(P\equiv1\pmod4\), \(|P|\) is the odd squarefree part of \(d\), and the defining congruence for a discriminant forces \(d/P\) to be exactly the indicated factor. The same argument proves uniqueness.

For completeness, the **Kronecker symbol** \((d/n)\) is multiplicative in the denominator. On odd positive primes it is the Legendre symbol, with value zero at divisors of \(d\); at \(-1\) it is \(\operatorname{sgn}(d)\); at 2 it is zero for even \(d\), and for odd \(d\) it equals \((-1)^{(d^2-1)/8}\). Put \((d/1)=1\) and \((d/0)=1\) for \(d=1\), zero for the other fundamental discriminants. Prime factorization then defines it on every integer.

**Theorem 4.1.** The real primitive Dirichlet characters are exactly

\[
\chi_d(n)=\left(\frac d n\right),
\]

for fundamental discriminants \(d\). Their conductor is \(|d|\), and \(\chi_d(-1)=\operatorname{sgn}(d)\).

**Proof.** Quadratic reciprocity and its supplementary laws give

\[
\left(\frac{p^*}{n}\right)=\left(\frac n p\right)
\]

for every integer \(n\), with zero values included. For positive odd primes in the denominator this is quadratic reciprocity with the sign absorbed into \(p^*\). For the denominator 2 it is the law for \((2/p)\); for \(-1\) both sides equal \((-1)^{(p-1)/2}\). Multiplicativity gives the assertion for general denominators. Likewise the symbols for \(-4,8,-8\) have exactly the values in (4.3), by the two supplementary laws.

It follows that the symbol for (4.4) is the product of the local characters just classified. Each nontrivial odd component has conductor \(p\), and the 2-component has conductor \(|d_2|\). Since these moduli are coprime, Theorem 3.1 gives conductor \(|d|\). Conversely, a real primitive character has precisely these local possibilities and hence gives a unique expression (4.4). The sign at \(-1\) is the defining Kronecker value. \(\square\)

**Example 4.2 (modulo 8).** All four characters vanish on even integers. On the odd classes they are

\[
\begin{array}{c|rrrr|c}
&1&3&5&7&\text{conductor}\\\hline
\chi_0&1&1&1&1&1\\
\chi_{-4}&1&-1&1&-1&4\\
\chi_8&1&-1&-1&1&8\\
\chi_{-8}&1&1&-1&-1&8
\end{array}
\]

Thus the primitive characters *modulo 8* are \(\chi_8\) and \(\chi_{-8}\). The character labelled \(\chi_{-4}\) in this table is its lift from modulus 4. Notice that \(\chi_8\) is even and \(\chi_{-8}\) is odd.

**Example 4.3 (modulo 12).** On \(1,5,7,11\), the rows are

\[
\begin{array}{c|rrrr|c}
&1&5&7&11&\text{conductor}\\\hline
\chi_0&1&1&1&1&1\\
\chi_{-3}&1&-1&1&-1&3\\
\chi_{-4}&1&1&-1&-1&4\\
\chi_{12}&1&-1&-1&1&12
\end{array}
\]

Only the last character is primitive modulo 12. Here \(\chi_{12}=\chi_{-3}\chi_{-4}\) on the units. Products can lose conductor: the square of any real primitive character is principal and has conductor 1, despite being represented at the original modulus.

## 5. Exercises

**Exercise 5.1 (easy).** Reconstruct the character table modulo 8 from the independent choices of values at \(-1\) and 5. Determine the conductor and parity of each row.

**Exercise 5.2 (medium).** Give a group-theoretic reason that no character modulo \(2m\), with \(m\) odd, is primitive. Do not use formula (3.2).

**Exercise 5.3 (medium).** Verify that 2 and 44 generate \(U_{45}\) as \(C_{12}\times C_2\). Define \(\chi(2)=i\) and \(\chi(44)=1\). Determine its conductor and the primitive character inducing it.

**Exercise 5.4 (medium).** Derive (3.2) from the partition by conductor, then compute the numbers of primitive characters modulo 9, 15, 16 and 18.

**Exercise 5.5 (hard).** Starting from a real primitive character, reconstruct its discriminant from its local factors. Explain why no squared odd prime divides its conductor and why the exponent of 2 is 0, 2 or 3.

### Solutions

**5.1.** Write each unit as \((-1)^\epsilon5^r\), with \(\epsilon,r\in\{0,1\}\). The residues \(1,3,5,7\) have pairs \((0,0),(1,1),(0,1),(1,0)\). If the chosen values at \(-1\) and 5 are \(u,v\), their row is \((1,uv,v,u)\). The choices \((1,1),(-1,1),(1,-1),(-1,-1)\) give the four rows of Example 4.2. Their conductors are 1, 4, 8, 8. The first and third are even; the second and fourth are odd. The row of conductor 4 is induced, so it is not primitive modulo 8.

**5.2.** Reduction \(U_{2m}\to U_m\) is an isomorphism: every unit modulo \(m\) has exactly one odd lift modulo \(2m\). Every character therefore descends to \(m\), a proper divisor. This also covers \(m=1\).

**5.3.** Modulo 9, 2 has order 6; modulo 5 it has order 4. It therefore has order 12 modulo 45. An exponent giving \(-1\) modulo 9 must be 3 modulo 6, whereas one giving \(-1\) modulo 5 must be 2 modulo 4; these parity conditions are incompatible. Thus 44, which is \(-1\), is not in \(\langle2\rangle\). Since \(|U_{45}|=24\), the two cyclic subgroups give the whole group and have trivial intersection. The prescribed values respect their orders, so they define a character.

Let \(\alpha\) and \(\beta\) be its local values at 2 modulo 9 and modulo 5. Then \(\alpha^6=\beta^4=1\), \(\alpha\beta=i\), and \(\alpha^3\beta^2=1\). The first two conditions force \(\alpha\in\{1,-1\}\); the last excludes \(\alpha=1,\beta=i\) and gives \(\alpha=-1,\beta=-i\). The modulo 9 factor is the lift of \((n/3)\), of conductor 3. The modulo 5 factor \(\psi\), defined by \(\psi(2)=-i\), has conductor 5. Hence \(\chi\) has conductor 15 and is induced by \((n/3)\psi(n)\) modulo 15. Its parity is even, as prescribed.

**5.4.** If \(F(q)=\sum_{d\mid q}f(d)\), then

\[
\sum_{d\mid q}\mu(q/d)F(d)
=\sum_{e\mid q}f(e)\sum_{e\mid d\mid q}\mu(q/d)=f(q),
\]

because the inner sum is 1 for \(e=q\) and 0 otherwise. Apply this with \(F=\varphi\) and \(f=\varphi^*\). The local formulas give \(\varphi^*(9)=4\), \(\varphi^*(15)=(3-2)(5-2)=3\), \(\varphi^*(16)=4\), and \(\varphi^*(18)=\varphi^*(2)\varphi^*(9)=0\).

**5.5.** On an odd prime-power factor a real nontrivial character sends a primitive root to \(-1\), so it is the Legendre character and descends to that prime. Primitivity excludes every higher odd exponent and every trivial local factor. At 2 a real character kills \(5^2\), so it descends to 8; the nontrivial possibilities are exactly (4.3). Modulus 2 adds no information. Choose \(d_2\) from their labels, or 1 if the 2-component is absent, and set \(d=d_2\prod p^*\) over the odd components. The verification following (4.4) shows this is fundamental. Reciprocity identifies its Kronecker character with the given character, and the local conductor product proves \(|d|\) is the conductor. The uniqueness of the local factors proves uniqueness of \(d\).

## What this lesson does not prove

The elementary group and field language and the Chinese remainder theorem are prerequisites. For pairwise coprime moduli, the latter follows from Bézout's identity by choosing coefficients that are 1 at one modulus and 0 at the others; their weighted sum gives every tuple of residues, and divisibility by the product gives uniqueness. All character extension, orthogonality, primitive-root, reciprocity, conductor, counting and real-character classification arguments needed here have been proved above.

## References

- Dimitris Koukoulopoulos, [*The Distribution of Prime Numbers*](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf), Graduate Studies in Mathematics 203, American Mathematical Society, 2019; Chapters 9 and 10.
- Andrew V. Sutherland, [*Dirichlet L-functions, primes in arithmetic progressions*](https://math.mit.edu/classes/18.785/2019fa/LectureNotes18.pdf), MIT 18.785, 2019; the sections on characters and conductors.
