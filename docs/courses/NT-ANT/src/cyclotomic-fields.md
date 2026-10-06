# Cyclotomic fields

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Independent full-lesson AI review is pending. Public domain (CC0).*

The roots of unity give number fields whose automorphisms and prime decomposition can be read from congruences. Their integral bases also have a particularly simple form: powers of a single root generate the full ring of integers. Inside these fields, quadratic Gauss sums connect two descriptions of Frobenius and prove quadratic reciprocity.

Fix the complex embedding and write
\[
\zeta_n=e^{2\pi i/n},\qquad K_n=\mathbf Q(\zeta_n),\qquad
U_n=(\mathbf Z/n\mathbf Z)^\times.
\tag{1}
\]
We take \(U_1\) to be the trivial group and \(\varphi(1)=1\). Both \(K_1\) and \(K_2\) are \(\mathbf Q\).

We use integral lattices and the discriminant–index identity from [*Discriminants and integral bases*](discriminants-and-integral-bases.md); the local membership test and DVR characterization from [*Discrete valuation rings and Dedekind domains*](discrete-valuation-rings-and-dedekind-domains.md); the quadratic splitting law and discriminant ramification criterion from [*Decomposition of primes in extensions*](decomposition-of-primes-in-extensions.md); and inertia, arithmetic Frobenius, and unramified composita and Galois closures from [*Hilbert's ramification theory in Galois extensions*](hilberts-ramification-theory-in-galois-extensions.md), Corollary 6.6. We also use the consequence of Minkowski's bound in [*Finiteness of the class number*](finiteness-of-the-class-number.md): a number field unramified at every finite prime of \(\mathbf Q\) is \(\mathbf Q\).

## Cyclotomic polynomials and their automorphisms

Define
\[
\Phi_n(X)=\prod_{\substack{1\leq a\leq n\\(a,n)=1}}(X-\zeta_n^a).
\]
Grouping roots by their exact orders gives
\[
X^n-1=\prod_{d\mid n}\Phi_d(X).
\tag{2}
\]
Inductively, every \(\Phi_n\) is monic and integral. Indeed, divide \(X^n-1\) by the product of the already integral monic factors for proper divisors. Monic division has integer quotient and remainder; the identity over \(\mathbf C\) makes that remainder zero.

**Theorem 12.1.** The polynomial \(\Phi_n\) is irreducible over \(\mathbf Q\). Its degree is \(\varphi(n)\), and the map
\[
U_n\xrightarrow{\sim}\operatorname{Gal}(K_n/\mathbf Q),
\qquad a\longmapsto\sigma_a,\quad \sigma_a(\zeta_n)=\zeta_n^a
\tag{3}
\]
is an isomorphism.

**Proof.** Let \(f\) be the monic minimal polynomial of \(\zeta_n\). Its coefficients are integers by integrality, and it divides \(\Phi_n\). Suppose \(p\nmid n\) is prime and \(\zeta_n^p\) is not a root of \(f\). Let \(g\) be its monic minimal polynomial, a distinct irreducible factor of \(\Phi_n\). Since \(g(\zeta_n^p)=0\), we have \(f(X)\mid g(X^p)\) in \(\mathbf Z[X]\).

Reduce modulo \(p\). The identity \(g(X^p)=g(X)^p\) there shows that any irreducible factor of \(\overline f\) also divides \(\overline g\). Since \(fg\mid X^n-1\), the latter polynomial would have a repeated factor modulo \(p\). Its derivative \(nX^{n-1}\) is relatively prime to it, which is a contradiction.

The same argument works for any primitive root that is already a root of \(f\). Every positive integer \(a\) coprime to \(n\) is a product of primes not dividing \(n\). Repeated application therefore puts every \(\zeta_n^a\) among the roots of \(f\). Thus \(f=\Phi_n\). All these roots lie in \(K_n\); sending \(\zeta_n\) to any one of them defines an automorphism. Composition multiplies exponents, proving (3). The cases \(n=1,2\) are linear polynomials and trivial groups. \(\square\)

The isomorphism (3) follows from the action on roots of unity. Throughout this lesson Frobenius means the **arithmetic** automorphism acting on residue fields by \(x\mapsto x^p\).

## Prime powers and integral bases

Let \(n=p^r\), \(r\geq1\), put \(\zeta=\zeta_n\), and set \(t=\varphi(n)=p^{r-1}(p-1)\). Then
\[
\Phi_{p^r}(X)=\frac{X^{p^r}-1}{X^{p^{r-1}}-1}
=\sum_{j=0}^{p-1}X^{jp^{r-1}}.
\tag{4}
\]
Modulo \(p\) this is \((X-1)^t\). Consequently \(\Phi_{p^r}(X+1)\) has all nonleading coefficients divisible by \(p\), while its constant term is \(\Phi_{p^r}(1)=p\). It is Eisenstein at \(p\).

We prove the full integral-basis assertion, rather than infer it merely from Eisenstein irreducibility. In \(R=\mathbf Z[\zeta]\), put \(\pi=1-\zeta\). Equation (4) gives
\[
N_{K_n/\mathbf Q}\pi=p,\qquad
p=\prod_{a\in U_n}(1-\zeta^a)=u\pi^t,\quad u\in R^\times.
\tag{5}
\]
For the unit assertion, each ratio \((1-\zeta^a)/(1-\zeta)\) is a geometric sum in \(R\). Choose a positive \(c\) with \(ac\equiv1\pmod n\); the reverse ratio is the geometric sum \((1-(\zeta^a)^c)/(1-\zeta^a)\). These two sums are inverses.

There is exactly one prime of \(R\) over \(p\), because
\[
R/pR\simeq\mathbf F_p[X]/((X-1)^t).
\]
It is \(P=(p,\pi)=(\pi)\), and \(R/P=\mathbf F_p\). An order is Noetherian of dimension one, as proved in [*Orders in number fields and their Picard groups*](orders-in-number-fields-and-their-picard-groups.md), “Orders and their conductors.” Thus \(R_P\) is a one-dimensional Noetherian local domain with principal maximal ideal. The DVR characterization makes it integrally closed.

The power-basis discriminant is supported only at \(p\). To calculate it, differentiation of (4) at \(\zeta\) gives
\[
\Phi_{p^r}'(\zeta)=\frac{p^r\zeta^{p^r-1}}{\zeta^{p^{r-1}}-1}.
\]
The denominator has absolute norm \(p^{p^{r-1}}\): its value belongs to \(K_p\), has norm \(p\) there, and \([K_{p^r}:K_p]=p^{r-1}\). The discriminant formula using the derivative therefore gives
\[
|\operatorname{disc}(1,\zeta,\ldots,\zeta^{t-1})|
=p^{rt-p^{r-1}}
=p^{p^{r-1}(rp-r-1)}.
\tag{6}
\]

The discriminant–index identity excludes every prime other than \(p\) from \([O_{K_n}:R]\). Nor can \(p\) divide that index: at the only maximal ideal of \(R\) over \(p\), every element of \(O_{K_n}\), being integral over \(R_P\), belongs to the normal ring \(R_P\). The quotient \(O_{K_n}/R\) consequently vanishes after localization there; a nonzero \(p\)-primary quotient would survive at some maximal ideal over \(p\), by the local membership test. Hence
\[
O_{K_{p^r}}=\mathbf Z[\zeta_{p^r}],\qquad
(p)=(1-\zeta_{p^r})^{\varphi(p^r)}.
\tag{7}
\]
Here the last expression is an equality of ideals; the prime is \((1-\zeta_{p^r})\), of residue degree one. For \(p=2,r=1\), it is simply \((2)\) in \(\mathbf Z\), with ramification index one.

## Combining fields with coprime discriminants

**Coprime-discriminant lemma.** Let \(K,L\) be number fields with relatively prime absolute discriminants \(d_K,d_L\). Then
\[
[KL:\mathbf Q]=[K:\mathbf Q][L:\mathbf Q],\quad
O_{KL}=O_KO_L,\quad
d_{KL}=d_K^{[L:\mathbf Q]}d_L^{[K:\mathbf Q]}.
\tag{8}
\]
The product \(O_KO_L\) means the ring of finite sums of products.

**Proof.** Let \(E,F\) be the Galois closures of \(K,L\). A prime not dividing \(d_K\) is unramified in \(K\) and in its Galois closure, by the unramified-closure result of the ramification lesson. The analogous assertion holds for \(F\). At every rational prime, at least one of \(E,F\) is therefore unramified. Their intersection is unramified there by multiplicativity of ramification indices in towers. The discriminant ramification criterion and Minkowski's discriminant bound imply \(E\cap F=\mathbf Q\).

For completeness, Galois fields with this intersection have full product degree. Restrict \(\operatorname{Gal}(EF/F)\) to \(E\), obtaining a subgroup \(H\). An element of \(E\) fixed by \(H\) is fixed by \(\operatorname{Gal}(EF/F)\), so belongs to \(F\). Thus \(E^H=E\cap F=\mathbf Q\). Galois correspondence gives \(H=\operatorname{Gal}(E/\mathbf Q)\) and \([EF:F]=[E:\mathbf Q]\). The multiplication map \(E\otimes_{\mathbf Q}F\to EF\) is an isomorphism; its restriction to \(K\otimes_{\mathbf Q}L\) is injective. Its image is \(KL\), since that image is a finite-dimensional domain and therefore a field. This proves the first assertion in (8).

Take integral bases \(e_1,\ldots,e_a\) of \(K\) and \(f_1,\ldots,f_b\) of \(L\), and put \(S=O_KO_L\). Their products are a \(\mathbf Z\)-basis of \(S\). For \(\alpha\in O_{KL}\), expand
\[
\alpha=\sum_i e_i\beta_i,\qquad \beta_i\in L.
\]
Every relative trace \(\operatorname{Tr}_{KL/L}(e_j\alpha)\) is integral and belongs to \(L\), hence lies in \(O_L\). Full product degree makes the relative embeddings precisely the embeddings of \(K\), so these traces give the linear system
\[
\sum_i\operatorname{Tr}_{K/\mathbf Q}(e_je_i)\beta_i\in O_L.
\]
Its integral coefficient matrix has determinant \(d_K\). Its adjugate shows \(d_K\beta_i\in O_L\), and therefore \(d_K\alpha\in S\). Interchanging the fields gives \(d_L\alpha\in S\). Bézout's identity now gives \(\alpha\in S\). The opposite inclusion follows from integrality of products and sums, proving the second assertion.

Finally the trace matrix in the product basis is the tensor product of the two trace matrices, since full product degree pairs the embeddings independently. Its determinant is \(d_K^b d_L^a\); the tensor determinant identity follows, for example, by triangularizing the two matrices over \(\mathbf C\) and multiplying their diagonal entries. This proves the last assertion. \(\square\)

The lemma supplies full product degree even when neither field is Galois. An intersection computation by itself would not supply that conclusion for arbitrary fields.

**Theorem 12.2.** For every \(n\geq1\),
\[
O_{K_n}=\mathbf Z[\zeta_n].
\tag{9}
\]
For \(n>2\) its discriminant is
\[
d_{K_n}=(-1)^{\varphi(n)/2}
\frac{n^{\varphi(n)}}{\displaystyle\prod_{p\mid n}p^{\varphi(n)/(p-1)}}.
\tag{10}
\]
For \(n=1,2\), it is \(1\).

**Proof.** Write \(n=\prod_i q_i\) with \(q_i\) distinct prime powers. Their fields have coprime discriminants by (6). Repeated application of (8) gives the full ring as the product of the rings \(\mathbf Z[\zeta_{q_i}]\). Inside \(K_n\), \(\zeta_{q_i}=\zeta_n^{n/q_i}\). The integers \(n/q_i\) have gcd one, so integer powers of these roots also generate \(\zeta_n\). This proves (9); \(n=1\) is immediate.

Here is a direct derivation of the discriminant formula. Möbius inversion in (2) gives
\[
\Phi_n(X)=\prod_{d\mid n}(X^d-1)^{\mu(n/d)}.
\]
At a primitive root \(\zeta=\zeta_n\), differentiation after removing the factor \(X^n-1\) yields
\[
\Phi_n'(\zeta)=n\zeta^{n-1}
\prod_{\substack{d\mid n\\d<n}}(\zeta^d-1)^{\mu(n/d)}.
\tag{11}
\]
For \(m>1\), taking the limit at \(1\) in the same product gives
\[
\Phi_m(1)=\prod_{d\mid m}d^{\mu(m/d)}=
\begin{cases}
p,&m\text{ is a power of the prime }p,\\
1,&m\text{ has at least two prime divisors}.
\end{cases}
\tag{12}
\]
To verify the last equality, take the valuation at a prime \(q\). In \(\sum_{d\mid m}\mu(m/d)v_q(d)\), summation over any other prime divisor cancels the terms in pairs. If \(m=q^k\), just the terms \(d=q^k,q^{k-1}\) survive, with difference one.

For \(m=n/d\), the root \(\zeta^d\) is primitive of order \(m\), so
\[
|N_{K_n/\mathbf Q}(1-\zeta^d)|
=\Phi_m(1)^{\varphi(n)/\varphi(m)}.
\]
In (11), all \(m\) other than prime powers contribute one, and \(\mu(p^k)=0\) for \(k\geq2\). The terms \(m=p\) contribute \(p^{-\varphi(n)/(p-1)}\). Taking the derivative norm proves the absolute value in (10). For \(n>2\), no embedding is real: a primitive root of order greater than two is nonreal. Thus \(r_2=\varphi(n)/2\), and the signature sign of the discriminant gives (10). The two degree-one cases have integral basis \(1\) and discriminant \(1\). \(\square\)

## Decomposition of primes

For \(p\nmid m\), write \(\operatorname{ord}_m(p)\) for the order of \(p\) in \(U_m\), with \(\operatorname{ord}_1(p)=1\).

**Theorem 12.3.** Let \(p\) be any rational prime and write \(n=p^r m\), with \(r\geq0\) and \(p\nmid m\). In \(K_n\), every prime over \(p\) has
\[
e=\varphi(p^r),\qquad f=\operatorname{ord}_m(p),\qquad
g=\frac{\varphi(m)}{f}
\tag{13}
\]
as ramification index, residue degree, and number of primes, respectively. Here \(p^0=1\). For \(p\nmid n\), arithmetic Frobenius is \(\sigma_p\).

**Proof.** First suppose \(p\nmid n\). Formula (10), with the degree-one cases treated separately, shows that \(p\) is unramified. At a prime \(P\) over \(p\), the reduction of \(\zeta_n\) still has order \(n\). Indeed, the factors \(\overline\Phi_d\), \(d\mid n\), of \(X^n-1\) are pairwise coprime because that polynomial is squarefree. A root of \(\overline\Phi_n\) cannot also have a proper divisor of \(n\) as its order.

The arithmetic Frobenius \(F_P\) satisfies \(F_P(\zeta_n)\equiv\zeta_n^p\pmod P\). Both are powers of \(\zeta_n\), and the exact order of its reduction makes the two powers equal already in \(K_n\). Thus \(F_P=\sigma_p\). The decomposition group is the cyclic group it generates, of order \(\operatorname{ord}_n(p)\); the unramified decomposition theorem gives \(f\) equal to this order and \(g=\varphi(n)/f\).

For \(r>0\), the prime-power field \(K_{p^r}\) is totally ramified at \(p\), with residue field \(\mathbf F_p\), by (7). The field \(K_m\) is unramified there by the first part. Coprime discriminants and (3) identify
\[
\operatorname{Gal}(K_n/\mathbf Q)=U_{p^r}\times U_m.
\]
Restriction of inertia to a Galois subfield is onto its inertia group. Hence inertia maps onto \(U_{p^r}\) and has trivial image in \(U_m\). It is exactly \(U_{p^r}\times1\). Restriction of decomposition groups is likewise onto, so the decomposition group has projection \(\langle p\bmod m\rangle\) in \(U_m\). Since it contains \(U_{p^r}\times1\), it is
\[
D=U_{p^r}\times\langle p\bmod m\rangle,\qquad
I=U_{p^r}\times1.
\tag{14}
\]
The formulas \(e=|I|\), \(f=|D/I|\), and \(g=|G/D|\) give (13). \(\square\)

In particular, a prime ramifies exactly when \(\varphi(p^r)>1\). If \(n>2\) and \(n\not\equiv2\pmod4\), this means exactly the primes dividing \(n\). If \(n=2m\) with \(m\) odd, then
\[
\zeta_{2m}=-\zeta_m^{(m+1)/2},\qquad K_{2m}=K_m;
\tag{15}
\]
the factor \(2\) contributes no ramification. The fields \(K_1,K_2\) have no ramified primes.

For \(p\nmid n\), complete splitting means \(p\equiv1\pmod n\). More generally, the finite-field factorization of \(\Phi_n\) consists of \(g\) distinct irreducible factors, each of degree \(f\): its roots are primitive roots of order \(n\), whose Frobenius orbits all have length \(\operatorname{ord}_n(p)\). The full-ring factorization theorem identifies the primes with those factors.

**Examples.** In \(K_5\), the residues of \(11,19,2,3\) modulo \(5\) have orders \(1,2,4,4\). Thus \(11\) splits into four primes of norm \(11\); \(19\) into two primes of norm \(19^2\); and \(2,3\) are inert, with norms \(2^4,3^4\). The prime \(5\) is totally ramified. Formula (10) gives \(d_{K_5}=5^3\).

In \(K_{12}\), put \(\zeta=\zeta_{12}\). Then \(i=\zeta^3\) and \(\sqrt3=\zeta+\zeta^{-1}\). Conversely \(\zeta=(\sqrt3+i)/2\), so
\[
K_{12}=\mathbf Q(i,\sqrt3).
\]
Its degree is four, and its Galois group is \(U_{12}\simeq(\mathbf Z/2\mathbf Z)^2\). The three index-two subgroups give exactly the three quadratic subfields \(\mathbf Q(i),\mathbf Q(\sqrt3),\mathbf Q(\sqrt{-3})\). Its discriminant is \(144\).

For \(K_7\), the signature has three complex pairs, and (10) gives \(d_{K_7}=-7^5\).

## A Gauss sum and quadratic reciprocity

For an odd prime \(p\), let \(\chi(a)=(a/p)\) be the Legendre symbol, extended by \(\chi(0)=0\). The cyclic group \(\mathbf F_p^\times\) has a subgroup of squares of index two; thus \(\chi\) is multiplicative, its sum over \(\mathbf F_p\) is zero, and
\[
\chi(-1)=(-1)^{(p-1)/2}.
\tag{16}
\]
Define
\[
G_p=\sum_{a\bmod p}\chi(a)\zeta_p^a,\qquad
p^*=(-1)^{(p-1)/2}p.
\tag{17}
\]

**Proposition 12.4.** For every odd prime \(p\),
\[
G_p^2=p^*,\qquad
\mathbf Q(G_p)=\mathbf Q(\sqrt{p^*}),
\tag{18}
\]
and this is the unique quadratic subfield of \(K_p\).

**Proof.** Reindexing the sum gives
\[
\sigma_b(G_p)=\chi(b)G_p,\qquad
\overline{G_p}=\chi(-1)G_p.
\tag{19}
\]
The norm square is computed without choosing a sign for a square root. With \(a=tb\) and \(b\ne0\),
\[
G_p\overline{G_p}
=\sum_{t\bmod p}\chi(t)\sum_{b\ne0}\zeta_p^{(t-1)b}
=(p-1)-\sum_{t\ne1}\chi(t)=p.
\tag{20}
\]
The inner sum is \(p-1\) for \(t=1\) and \(-1\) otherwise, by the finite geometric sum; the total character sum is zero. Equations (19)–(20) prove (18). The rational number \(p^*\) is not a rational square, so this field is quadratic. Finally \(U_p\) is cyclic, and a cyclic group of even order has exactly one index-two subgroup. Galois correspondence proves uniqueness. \(\square\)

**Theorem 12.5 (quadratic reciprocity).** For distinct odd primes \(p,q\),
\[
\left(\frac pq\right)\left(\frac qp\right)
=(-1)^{(p-1)(q-1)/4}.
\tag{21}
\]
The supplements, for odd \(p\), are
\[
\left(\frac{-1}{p}\right)=(-1)^{(p-1)/2},\qquad
\left(\frac2p\right)=(-1)^{(p^2-1)/8}.
\tag{22}
\]

**Proof.** The first supplement is (16). The quadratic field \(E=\mathbf Q(\sqrt{p^*})\) has fundamental discriminant \(p^*\). The prime \(q\) is unramified in \(K_p\), so its Frobenius restricts to the Frobenius in \(E\). By (19), its action on \(G_p\) is multiplication by \((q/p)\). By the quadratic splitting law, that same action is multiplication by \((p^*/q)\): Frobenius is the identity when the prime splits and the conjugation when it is inert. Thus
\[
\left(\frac qp\right)=\left(\frac{p^*}{q}\right)
=\left(\frac pq\right)
(-1)^{(p-1)(q-1)/4},
\tag{23}
\]
which is (21). No reciprocity statement has been used in deriving (23).

For the second supplement, in \(K_8\) set \(s=\zeta_8+\zeta_8^{-1}=\sqrt2\). For odd \(q\), the automorphism \(\sigma_q\) sends \(s\) to \(s\) for \(q\equiv1,7\pmod8\) and to \(-s\) for \(q\equiv3,5\pmod8\). The prime \(q\) is unramified in \(K_8\), and restricting its Frobenius to \(\mathbf Q(\sqrt2)\) identifies this sign with \((2/q)\), by the quadratic splitting law. The four signs are exactly \((-1)^{(q^2-1)/8}\). \(\square\)

## Quadratic fields inside cyclotomic fields

For an odd prime put \(d_p=p^*\), and use these three even discriminants:
\[
\chi_{-4}(a)=(-1)^{(a-1)/2},\quad
\chi_8(a)=(-1)^{(a^2-1)/8},\quad
\chi_{-8}(a)=\chi_{-4}(a)\chi_8(a)
\tag{24}
\]
for odd \(a\), with value zero for even \(a\). These are multiplicative functions on the units modulo \(4,8,8\), respectively. For the first this follows by multiplying signs modulo four. For the second it follows from the four unit residues modulo eight: the kernel is \(\{1,7\}\). For \(d_p\), let \(\chi_{d_p}(a)=(a/p)\).

Every quadratic fundamental discriminant \(D\) factors uniquely as
\[
D=\delta\prod_{p\mid D,\ p>2}p^*,
\qquad \delta\in\{1,-4,8,-8\},
\tag{25}
\]
where the absolute values of the displayed factors are pairwise coprime. To check this directly, an odd fundamental \(D\equiv1\pmod4\) equals the product of its \(p^*\), since that product is \(1\pmod4\) and has the same absolute value. If \(D=4d\) with odd squarefree \(d\equiv3\pmod4\), the odd product is \(-d\), so \(\delta=-4\). If \(D=8u\) with odd squarefree \(u\), the odd product is \(u\) for \(u\equiv1\pmod4\) and \(-u\) for \(u\equiv3\pmod4\), giving \(\delta=8\) or \(-8\).

For a factor \(d_i\) in (25), set \(f_i=|d_i|\) and
\[
\tau_i=\sum_{a\bmod f_i}\chi_{d_i}(a)\zeta_{f_i}^a.
\]
The odd factors satisfy \(\tau_i^2=d_i\) by Proposition 12.4. Direct sums of the four or eight residues give
\[
\tau_{-4}=2i,\qquad \tau_8=2\sqrt2,\qquad
\tau_{-8}=2i\sqrt2,
\tag{26}
\]
so the same square identity holds for the even factors.

Put \(f=|D|=\prod_i f_i\) and \(\chi_D(a)=\prod_i\chi_{d_i}(a)\), with the factors evaluated modulo their respective moduli. The Chinese remainder theorem makes this a quadratic character modulo \(f\). Write \(M_i=f/f_i\) and choose \(t_iM_i\equiv1\pmod{f_i}\). A residue is \(a=\sum_i a_iM_it_i\), and \(\zeta_f^a=\prod_i\zeta_{f_i}^{a_it_i}\). Therefore
\[
\tau_D:=\sum_{a\bmod f}\chi_D(a)\zeta_f^a
=\prod_i\left(\sum_{a_i\bmod f_i}
 \chi_{d_i}(a_i)\zeta_{f_i}^{t_i a_i}\right)
=\left(\prod_i\chi_{d_i}(M_i)\right)\prod_i\tau_i.
\tag{27}
\]
The substitution \(b=t_i a_i\) gives the last equality; for a quadratic character the value at an inverse equals the value at the element. The prefactor is \(1\) or \(-1\). Thus
\[
\tau_D^2=D,\qquad \tau_D\in K_{|D|}.
\tag{28}
\]

**Proposition 12.6.** If \(E\) is a quadratic number field of discriminant \(D\), then
\[
E=\mathbf Q(\tau_D)\subseteq K_{|D|}.
\tag{29}
\]

**Proof.** Its integral basis identifies \(E=\mathbf Q(\sqrt D)\). Equation (28) gives a nonzero square root of \(D\) in the indicated cyclotomic field. Since a quadratic discriminant is not a rational square, \(\tau_D\) generates \(E\). \(\square\)

This is an explicit algebraic inclusion. Determining which of the two complex square roots equals a general Gauss sum requires additional information; (28) does not select that sign.

For example, \(12=(-4)(-3)\); the factors \(2i\) and \(i\sqrt3\) in (26) and (18) already give a square root of \(12\) inside \(K_{12}\), with the CRT sign in (27) fixing the resulting Gauss sum.

**Real subfield.** For \(n>2\), put \(K_n^+=\mathbf Q(\zeta_n+\zeta_n^{-1})\). This field is real, and \(\zeta_n\) satisfies
\[
X^2-(\zeta_n+\zeta_n^{-1})X+1=0.
\]
It is nonreal, so \([K_n:K_n^+]=2\). Complex conjugation is \(\sigma_{-1}\); its fixed field also has index two, and hence is exactly \(K_n^+\). Thus \([K_n^+:\mathbf Q]=\varphi(n)/2\). For \(n=1,2\), the real subfield is \(\mathbf Q\), of degree one.

## Exercises

1. Compute the decomposition of \(2,3,5,7,11\) in \(K_8\), including the norms of the primes.
2. Prove the coprime-discriminant lemma (8) for arbitrary number fields; explain where full product degree enters the integral-basis proof.
3. Prove \(K_n\cap K_m=K_{\gcd(n,m)}\), including the cases with a factor \(2\) occurring to the first power.
4. Compute quadratic Gauss sums up to sign for composite moduli. Treat primitive characters and characters induced to a larger modulus separately, and deduce (29) explicitly.

## Solutions

**1.** At \(2\), formula (7) gives
\[
(2)=(1-\zeta_8)^4,\qquad e=4,\ f=1,\ g=1,\ N(1-\zeta_8)=2.
\]
For each of \(3,5,7,11\), its residue modulo \(8\) is nonidentity and has order two in \(U_8\). Thus it is unramified and splits into two distinct primes, each of residue degree two and norm \(p^2\). Their norms are \(9,25,49,121\), respectively. None is inert: \(U_8\) has no element of order four.

**2.** The first part of the proof of (8) establishes full product degree before any trace expansion: the intersection of the Galois closures is unramified everywhere and hence trivial, and restriction of Galois groups then proves linear disjointness. Restricting the tensor multiplication map to the original fields gives degree \([K:\mathbf Q][L:\mathbf Q]\).

With integral bases \(e_i,f_j\), the products \(e_if_j\) are therefore linearly independent. Their span is closed under multiplication, because each original integral basis has integer multiplication coefficients. It is exactly the product ring \(S\).

An integer \(\alpha\in KL\) has a unique expansion \(\sum_i e_i\beta_i\), \(\beta_i\in L\). Full product degree identifies the relative trace coefficients with the rational trace matrix of \(K\). Its adjugate gives \(d_K\alpha\in S\); reversing \(K,L\) gives \(d_L\alpha\in S\). For integers \(u,v\) with \(ud_K+vd_L=1\),
\[
\alpha=u(d_K\alpha)+v(d_L\alpha)\in S.
\]
Thus \(O_{KL}=S\), with no Galois hypothesis on \(K,L\). The trace tensor determinant proves the discriminant formula. The full degree was needed both for uniqueness of the expansion and for the identification of its relative traces.

**3.** Put \(l=\operatorname{lcm}(n,m)\), \(d=\gcd(n,m)\). All the fields lie in \(K_l\). For any divisor \(a\mid l\), the subgroup fixing \(K_a\) is
\[
H_a=\ker(U_l\longrightarrow U_a).
\tag{30}
\]
Indeed, \(\zeta_a=\zeta_l^{l/a}\) is fixed precisely when the exponent is \(1\pmod a\).

The reduction map is onto. To lift a unit modulo \(a\), retain its specified residue at primes dividing \(a\), and impose a unit residue, for instance \(1\), at primes dividing \(l\) but not \(a\); the Chinese remainder theorem supplies the lift. Consequently its fixed field has degree \(|U_a|=\varphi(a)\), confirming it is \(K_a\).

Factor \(l=\prod_p p^{c_p}\), and write the exponents in \(n,m\) as \(a_p,b_p\), allowing zero. The Chinese remainder theorem decomposes \(U_l\) as the product of the groups \(U_{p^{c_p}}\). In each component the kernels of reduction to \(U_{p^{a_p}}\) and \(U_{p^{b_p}}\) are nested. Their generated subgroup is the kernel of reduction to exponent \(\min(a_p,b_p)\). Thus
\[
\langle H_n,H_m\rangle=H_d.
\]
An element belongs to both fixed fields exactly when it is fixed by both groups, hence by the group they generate. Galois correspondence yields \(K_n\cap K_m=K_d\). The trivial groups \(U_1,U_2\) make this argument valid without any exception for \(n\equiv2\pmod4\).

**4.** First, the characters in (25) are primitive at their displayed moduli. A nontrivial Legendre character modulo a prime cannot have a smaller conductor. The character \(\chi_{-4}\) distinguishes \(1,3\pmod4\). Each of \(\chi_8,\chi_{-8}\) distinguishes \(1,5\pmod8\), and so cannot come from modulus four. Their CRT product cannot lose any prime-power component: a hypothetical smaller conductor would make one of these component characters factor through a smaller modulus. Hence \(\chi_D\) is primitive of conductor \(f=|D|\).

These describe all nontrivial primitive quadratic characters. For an odd prime power \(p^r\), the kernel of \(U_{p^r}\to U_p\) has odd order \(p^{r-1}\), so any homomorphism to \(\{1,-1\}\) kills it. The only nontrivial quadratic character on the cyclic group \(U_p\) is the Legendre character.

For \(2^r\), \(r\geq3\), the group of units is generated by \(-1\) and \(5\). To see this, induction using
\[
5^{2^{k+1}}-1=(5^{2^k}-1)(5^{2^k}+1)
\]
gives \(v_2(5^{2^k}-1)=k+2\). Thus \(5\) has order \(2^{r-2}\) modulo \(2^r\), and its powers give all residues \(1\pmod4\); their negatives give the other odd residues. A quadratic character kills \(5^2\), whose powers are all residues \(1\pmod8\). It therefore factors through modulus eight. The three nontrivial characters there have primitive conductors \(4,8,8\) and are exactly (24). The cases \(r=1,2\) are immediate. CRT now gives precisely the factorization (25), with its sign determined by the selected local characters. The trivial primitive character has conductor \(1\); set \(D=1,\tau_1=1\) for it.

For a primitive nontrivial character \(\chi_D\), (27) is the requested composite calculation:
\[
\tau_D=\epsilon_D\prod_i\tau_i,\qquad
\epsilon_D=\prod_i\chi_{d_i}(f/f_i)\in\{1,-1\},\qquad
\tau_D^2=D.
\tag{31}
\]
In particular \(\tau_D=\pm\sqrt D\), and its value is explicitly a product of the odd-prime sums (17) and the three known even sums (26), with the specified CRT sign. This proves the quadratic-field inclusion directly.

Now induce this character to a modulus \(M\) divisible by \(f\): let \(\chi(a)=\chi_D(a)\) when \((a,M)=1\), and zero otherwise. Its Gauss sum need not have absolute value \(\sqrt M\). The exact formula is
\[
\tau_M(\chi)
=\mu(M/f)\chi_D(M/f)\tau_D.
\tag{32}
\]
Here \(\chi_D\) is zero on integers not coprime to \(f\).

To prove (32), let \(S\) be the product of the distinct primes dividing \(M\) but not \(f\). The zeros already imposed by \(\chi_D\) handle primes dividing \(f\); exclusion of the remaining primes gives
\[
\tau_M(\chi)
=\sum_{d\mid S}\mu(d)\chi_D(d)
\sum_{b\bmod M/d}\chi_D(b)\zeta_{M/d}^b.
\tag{33}
\]
Since \(d\) is coprime to \(f\), the integer \(M/d\) is still divisible by \(f\). Put \(M/d=fh\) and write \(b=c+kf\), \(0\leq c<f,\ 0\leq k<h\). The inner sum contains the factor
\[
\sum_{k=0}^{h-1}e^{2\pi i k/h},
\]
which is zero unless \(h=1\). The only possible surviving term in (33) is consequently \(d=M/f\). Such a term exists exactly when \(M/f\) is squarefree and coprime to \(f\). It is then the right side of (32); otherwise either the Möbius value or the character value there is zero. This also proves the formula for the conductor-one trivial character.

For example, the Jacobi symbol modulo an odd squarefree \(M\) is primitive and corresponds to \(D=(-1)^{(M-1)/2}M\), so its sum squares to that \(D\). For an odd nonsquarefree \(M\), its primitive conductor is the product of primes occurring to odd exponent. The quotient \(M/f\) contains a square or shares a prime with \(f\), so (32) makes its Gauss sum zero. This includes square moduli, where the induced character is principal. Thus a blanket square formula for imprimitive quadratic characters would be false.

## What this lesson does not prove

- The integral-lattice and discriminant–index results, the DVR characterization and local membership test, and the finite-field cyclicity used above are the precise prerequisites in lessons 2, 3, and 5.
- Prime factorization, the discriminant ramification criterion, and the full quadratic splitting law including the prime \(2\) come from *Decomposition of primes in extensions*. Inertia restriction, Frobenius restriction, and preservation of unramifiedness under composita and Galois closure come from *Hilbert's ramification theory in Galois extensions*.
- The discriminant lower bound excluding a nontrivial everywhere-unramified extension of \(\mathbf Q\) comes from *Finiteness of the class number*, Theorem 8.3, “Discriminants cannot be too small.”
- The exact analytic choice of sign of general primitive Gauss sums, the full Kronecker–Weber theorem for abelian extensions, and the class-field-theory reciprocity convention are outside this lesson. The square identities and the explicit quadratic inclusions require none of them.

The next lesson studies cyclotomic units and class numbers. The canonical action (3) also supplies the cyclotomic Galois input used in the Bost–Connes system and in the arithmetic of the field with one element.

## References

- J. S. Milne, *Algebraic Number Theory*, version 3.08, 2020, Chapter 6, “The basic results,” Propositions 6.1–6.5 and Remark 6.6, pp. 95–100.
- J. S. Milne, *Fields and Galois Theory*, version 5.10, 2022, Chapter 5, “Cyclotomic extensions,” Lemma 5.8, Proposition 5.9, and Theorem 5.10, pp. 64–66.
- Erich Hecke, *Vorlesungen über die Theorie der algebraischen Zahlen*, 1923, Chapter V, §30, Satz 91–92, pp. 110–113, for the historical cyclotomic decomposition argument; Chapter VI, §43, Satz 126–131, pp. 165–172, with the cyclotomic degree conclusion on p. 170.
