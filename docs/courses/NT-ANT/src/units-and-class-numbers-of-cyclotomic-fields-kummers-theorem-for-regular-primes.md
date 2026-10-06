# Units and class numbers of cyclotomic fields; Kummer's theorem for regular primes

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Independent full-lesson AI review is pending. Public domain (CC0).*

Factoring an equation into algebraic integers is useful only when the factors can be controlled. In a prime cyclotomic field, two facts provide that control: distinct factors of a first-case Fermat equation generate relatively prime ideals, and every unit is a power of the cyclotomic root times a real unit. Regularity then turns an ideal power into an element power. The remaining obstruction appears in a short congruence in the integral basis.

Throughout, \(p\) is an odd prime and
\[
\zeta=e^{2\pi i/p},\qquad K=\mathbf Q(\zeta),\qquad
K^+=\mathbf Q(\zeta+\zeta^{-1}),\qquad \lambda=1-\zeta.
\tag{1}
\]
Write \(E=\mathcal O_K^\times\), \(E^+=\mathcal O_{K^+}^\times\), and \(h=h(K)\), \(h^+=h(K^+)\). A bar denotes complex conjugation. From [*Cyclotomic fields*](cyclotomic-fields.md), we use
\[
\mathcal O_K=\mathbf Z[\zeta],\qquad
\mathcal O_K/(\lambda)=\mathbf F_p,\qquad
(p)=(\lambda)^{p-1},\qquad [K^+:\mathbf Q]=(p-1)/2.
\tag{2}
\]
The last ideal identity suppresses a unit in the corresponding element identity. The same lesson supplies cyclotomic field intersections and the unit geometric-series ratios. We use Kronecker's lemma and the unit theorem from [*Dirichlet's unit theorem*](dirichlets-unit-theorem.md), together with unique ideal factorization and the finite class group from the earlier ideal and class-number lessons.

## Roots of unity and real units

First identify all roots of unity in \(K\):
\[
\mu(K)=\{\pm\zeta^j: j\in\mathbf Z/p\mathbf Z\}.
\tag{3}
\]
Indeed, if a root of unity of order \(N\) belongs to \(K\), then \(K_N\subseteq K_p\). The intersection theorem gives \(K_N=K_{\gcd(N,p)}\). If \(p\nmid N\), its degree is one, so \(N=1\) or \(2\). If \(p\mid N\), write \(N=p^r m\) with \(p\nmid m\). Now \(K_N=K_p\), and the degree formula yields \(p^{r-1}\varphi(m)=1\). Hence \(r=1\) and \(m=1\) or \(2\). This proves (3), since every root of order \(p\) or \(2p\) is among those displayed.

**Proposition 13.1 (Kummer's unit lemma).** Every \(\varepsilon\in E\) has the form
\[
\varepsilon=\zeta^k v,\qquad v\in E^+.
\tag{4}
\]
In particular, the unit index \([E:\mu(K)E^+]\) equals one.

**Proof.** The quotient \(\varepsilon/\overline\varepsilon\) is an algebraic integer because both factors are units. Cyclotomic automorphisms commute with conjugation, so every conjugate of this quotient has absolute value one. Kronecker's lemma makes it a root of unity. By (3), it is \(\pm\zeta^j\).

Reduction modulo \(\lambda\) sends \(\zeta\) and \(\zeta^{-1}\) to \(1\). Thus \(\varepsilon\) and \(\overline\varepsilon\) have the same nonzero residue, and their quotient reduces to \(1\). A root \(-\zeta^j\) reduces to \(-1\), which differs from \(1\) because \(p\) is odd. Therefore
\[
\varepsilon/\overline\varepsilon=\zeta^j.
\]
Choose \(k\) with \(2k\equiv j\pmod p\) and put \(v=\zeta^{-k}\varepsilon\). Then \(v/\overline v=\zeta^{j-2k}=1\). Both \(v\) and its inverse are integral and real, hence belong to \(\mathcal O_{K^+}\). This proves (4). The possible minus sign in a root of unity has been absorbed into the real unit. \(\square\)

The residue congruence supplies the extra information beyond the general CM-field argument. The latter gives a root of unity; the congruence removes its negative coset.

## Constructing cyclotomic units

For \(p\nmid a\), define
\[
u_a=\frac{1-\zeta^a}{1-\zeta}.
\tag{5}
\]
Only the residue of \(a\) modulo \(p\) matters.

**Proposition 13.2.** The element \(u_a\) is a unit of \(\mathbf Z[\zeta]\).

**Proof.** Represent \(a\) by an integer between \(1\) and \(p-1\). Then
\[
u_a=1+\zeta+\cdots+\zeta^{a-1}\in\mathbf Z[\zeta].
\]
Choose a positive integer \(b\) with \(ab\equiv1\pmod p\). The reverse ratio is also a geometric sum:
\[
u_a^{-1}=\frac{1-(\zeta^a)^b}{1-\zeta^a}
=1+\zeta^a+\cdots+(\zeta^a)^{b-1}.
\]
Multiplication proves that these two algebraic integers are inverses. \(\square\)

The ratios themselves need not be real. Direct conjugation gives
\[
\overline u_a=\zeta^{1-a}u_a.
\]
Let \(r_a\in\mathbf Z/p\mathbf Z\) satisfy \(2r_a\equiv1-a\pmod p\), and put
\[
c_a=\zeta^{r_a}u_a\in E^+.
\tag{6}
\]
Indeed, \(c_a/\overline c_a=\zeta^{2r_a+a-1}=1\). Moreover \(c_1=1\) and \(c_{p-a}=-c_a\): the latter follows from \(u_{p-a}=-\zeta^{-a}u_a\) and \(r_{p-a}-r_a\equiv a\pmod p\). Thus the real cyclotomic-unit subgroup can be written
\[
C^+=\langle-1,c_2,c_3,\ldots,c_{(p-1)/2}\rangle\subseteq E^+.
\tag{7}
\]
For \(p=3\) this means \(C^+=\{1,-1\}\). Its displayed nontorsion generators number \((p-3)/2\), the rank of \(E^+\).

### The index of the real cyclotomic units

**Theorem (real cyclotomic-unit index).** For every odd prime \(p\), the subgroup in (7) has finite index
\[
[E^+:C^+]=h(K^+)=h^+.
\tag{8}
\]

The proof uses the unit theorem already established in [*Dirichlet's unit theorem*](dirichlets-unit-theorem.md). Its analytic inputs are proved later in [*The Dedekind zeta function and the analytic class number formula*](the-dedekind-zeta-function-and-the-analytic-class-number-formula.md), Theorem 16.2, and [*Abelian number fields and Dirichlet L-functions at \(s=1\)*](abelian-number-fields-and-dirichlet-l-functions-at-s-1.md), Theorem 17.1, Proposition 17.2 and Theorem 17.3. These give the residue, the cyclotomic Euler-factor product, and convergence and nonvanishing at one. Their proofs use the ordinary class group and the full unit lattice, not this index theorem.

**Proof.** If \(p=3\), then \(\zeta+\zeta^{-1}=-1\), so \(K^+=\mathbf Q\), \(E^+=C^+=\{1,-1\}\), and \(h^+=1\). The regulator is \(1\), by the rank-zero convention. This proves the theorem in that case.

Assume henceforth that \(p\geq5\). Set
\[
n=\frac{p-1}{2},\qquad F=K^+,\qquad
t=\zeta+\zeta^{-1},\qquad
G=(\mathbf Z/p\mathbf Z)^\times/\{1,-1\}.
\]
Use \(1,2,\ldots,n\) as representatives for \(G\), with \(1\) its identity. Its elements index the real embeddings \(\sigma_a:F\to\mathbf R\), obtained by restricting \(\zeta\mapsto\zeta^a\). Write \(R^+\) for the ordinary, deleted-row regulator of \(F\).

**The real integral basis and discriminant.** Multiplication by the unit \(\zeta\) takes the integral basis \(1,\zeta,\ldots,\zeta^{p-2}\) of \(K\) to the integral basis
\[
\zeta,\zeta^2,\ldots,\zeta^{p-1}.
\]
Conjugation permutes this basis by \(a\mapsto p-a\). Uniqueness of integral coordinates shows that its fixed lattice has basis
\[
s_a=\zeta^a+\zeta^{-a}\qquad(1\leq a\leq n).
\]
The algebraic integers of \(F\) are exactly \(\mathcal O_K\cap F\), so this fixed lattice is \(\mathcal O_F\). Set \(s_0=2\) and \(s_1=t\). The identity
\[
s_{a+1}=t s_a-s_{a-1}
\]
puts every \(s_a\) in \(\mathbf Z[t]\). Conversely \(t\) is a real algebraic integer, hence \(\mathbf Z[t]\subseteq\mathcal O_F\). We have proved
\[
\mathcal O_F=\mathbf Z[t].
\tag{CU1}
\]
In particular \(1,t,\ldots,t^{n-1}\) is an integral basis: the monic minimal polynomial of \(t\) has degree \(n\), and division by it describes all of \(\mathbf Z[t]\).

Let \(P(T)\) be that minimal polynomial. The numbers \(\zeta^a+\zeta^{-a}\), indexed by \(G\), are distinct: two equal sums give the same polynomial \(X^2-t_aX+1\), and hence the same unordered pair of roots \(\{\zeta^a,\zeta^{-a}\}\). Pairing the roots of \(\Phi_p\) therefore gives
\[
\Phi_p(X)=\prod_{a\in G}(X^2-t_aX+1)
=X^nP(X+X^{-1}).
\]
Differentiate this identity and evaluate at \(\zeta\). Since \(P(t)=0\), the term differentiating \(X^n\) vanishes, leaving
\[
\Phi_p'(\zeta)
=\zeta^{n-1}(\zeta-\zeta^{-1})P'(t).
\tag{CU2}
\]

For a monogenic integral basis with minimal polynomial \(Q\), the discriminant has absolute value \(|N(Q'(\alpha))|\). Indeed, if the roots are \(\alpha_i\), then \(Q'(\alpha_i)=\prod_{j\ne i}(\alpha_i-\alpha_j)\). Multiplying over \(i\) gives, up to the sign \((-1)^{m(m-1)/2}\), the squared Vandermonde determinant, which is the trace discriminant of \(1,\alpha,\ldots,\alpha^{m-1}\).

The cyclotomic discriminant calculation from *Cyclotomic fields* gives \(|d_K|=p^{p-2}\). Also
\[
|N_{K/\mathbf Q}(\zeta-\zeta^{-1})|
=|N_{K/\mathbf Q}(\zeta^{-1}(\zeta^2-1))|=p.
\]
Here \(\zeta^{-1}\) is a root of unity, and \(\zeta^2\) is again a primitive \(p\)-th root, so the last norm is \(\Phi_p(1)=p\) in absolute value. Each real embedding of \(F\) has two extensions to \(K\), giving
\[
|N_{K/\mathbf Q}(P'(t))|
=|N_{F/\mathbf Q}(P'(t))|^2=d_F^2.
\]
The last equality uses (CU1); \(d_F>0\) because all embeddings are real. Taking absolute norms in (CU2) now yields
\[
p^{p-2}=p\,d_F^2,\qquad d_F=p^{n-1}.
\tag{CU3}
\]

**The augmentation determinant.** We first prove a finite linear-algebra identity. Let \(H\) be a finite abelian group with identity \(1\), and let \(q:H\to\mathbf C\) be any function. Form the matrix
\[
D_{a,b}=q(ab)-q(a)\qquad(a,b\in H\setminus\{1\}).
\]
Then
\[
|\det D|
=\prod_{\substack{\chi\in\widehat H\\\chi\ne1}}
\left|\sum_{a\in H}\chi(a)q(a)\right|.
\tag{CU4}
\]
This also includes the trivial group, with both sides equal to \(1\).

To prove it, take the vector space with basis \(e_a\), and put
\[
T(e_b)=\sum_{a\in H}q(ab^{-1})e_a,\qquad
W=\left\{\sum_a x_ae_a:\sum_a x_a=0\right\}.
\]
Every column of \(T\) has sum \(\sum_aq(a)\), so \(T(W)\subseteq W\). The integral augmentation lattice \(W\cap\mathbf Z[H]\) has basis \(u_b=e_b-e_1\), \(b\ne1\): a vector with coefficient sum zero is uniquely \(\sum_{b\ne1}x_bu_b\). In that same basis for both domain and range, the matrix of \(T|_W\) is
\[
M_{a,b}=q(ab^{-1})-q(a)\qquad(a,b\ne1).
\]
Replacing each column index \(b\) by \(b^{-1}\) changes the determinant only by a sign and turns \(M\) into \(D\).

Finite abelian group decomposition gives exactly \(|H|\) complex characters. Their orthogonality can be checked directly: if \(\chi\ne\psi\), choose \(h\) with \(\chi(h)\overline{\psi(h)}\ne1\); translation by \(h\) multiplies \(\sum_a\chi(a)\overline{\psi(a)}\) by this value, forcing the sum to be zero. For \(\chi=\psi\) the sum is \(|H|\), because character values are roots of unity. Consequently the vectors
\[
v_\chi=\sum_{a\in H}\chi(a)e_a
\]
form a basis. The nontrivial ones have coefficient sum zero and form a basis of \(W\). Substitution \(c=ab^{-1}\) shows
\[
T v_\chi=
\left(\sum_{c\in H}q(c)\chi(c)^{-1}\right)v_\chi.
\]
The determinant of \(T|_W\) is the product of these eigenvalues. Reindexing the nontrivial characters by inversion, and taking absolute values, proves (CU4). No factor \(|H|\) appears: we computed the actual restricted operator in one augmentation basis, not a cofactor of its full matrix.

Apply this with \(H=G\) and
\[
\ell(a)=\log|1-\zeta^a|.
\]
The function is well-defined on \(G\) since \(|1-\zeta^{-a}|=|1-\zeta^a|\). The real units \(c_b\) constructed in (6) satisfy
\[
\log|\sigma_a(c_b)|=\ell(ab)-\ell(a),
\]
because their root-of-unity phases have absolute value one. Thus the deleted-row logarithmic matrix for \(c_2,\ldots,c_n\) is
\[
B=(\ell(ab)-\ell(a))_{a,b\in G\setminus\{1\}},
\]
where the omitted embedding is \(a=1\). Define \(R_C=|\det B|\), without yet assuming that the units are independent. Formula (CU4) gives
\[
R_C=\prod_{\substack{\chi\in\widehat G\\\chi\ne1}}|S_\chi|,
\qquad S_\chi=\sum_{a\in G}\chi(a)\ell(a).
\tag{CU5}
\]

**The even-character logarithm formula.** Characters of \(G\) are exactly the even Dirichlet characters modulo \(p\). Extend them by zero at multiples of \(p\). Every nontrivial one is primitive, since its conductor divides the prime \(p\) and cannot be \(1\). We now prove, for all such characters, including nonreal ones,
\[
L(1,\chi)=-\frac{2}{\tau(\overline\chi)}S_{\overline\chi},
\qquad
\tau(\chi)=\sum_{a=1}^{p-1}\chi(a)\zeta^a,
\qquad |\tau(\chi)|=\sqrt p.
\tag{CU6}
\]

A nontrivial character has \(\sum_{a=1}^{p-1}\chi(a)=0\), by multiplying the residues by a unit on which it is not \(1\). Character values on units have absolute value one. In the squared Gauss-sum magnitude, substitute \(a=ub\):
\[
\begin{aligned}
|\tau(\chi)|^2
&=\sum_{u=1}^{p-1}\chi(u)
  \sum_{b=1}^{p-1}\zeta^{(u-1)b}\\
&=(p-1)-\sum_{u\ne1}\chi(u)=p.
\end{aligned}
\]
The inner geometric sum is \(p-1\) at \(u=1\) and \(-1\) otherwise. This proves the magnitude and nonvanishing of the Gauss sum without a choice of phase.

For every positive integer \(m\), change variables \(b=am\) if \(p\nmid m\). If \(p\mid m\), use the zero character sum. The two cases give
\[
\sum_{a=1}^{p-1}\overline\chi(a)\zeta^{am}
=\tau(\overline\chi)\chi(m).
\]
For \(0<r<1\), absolute convergence of \(\sum r^m/m\) therefore permits interchange with the finite sum:
\[
\sum_{m\geq1}\frac{\chi(m)r^m}{m}
=-\frac1{\tau(\overline\chi)}
 \sum_{a=1}^{p-1}\overline\chi(a)\log(1-r\zeta^a).
\tag{CU7}
\]
The logarithm is the branch starting at zero when \(r=0\). Its argument has positive real part throughout \(0\leq r\leq1\), so this is also the principal branch.

The undamped series \(\sum\chi(m)/m\) converges: periodicity and the zero period sum bound the partial sums of \(\chi(m)\), and summation by parts gives a tail tending to zero. Its limit is \(L=L(1,\chi)\), as in Proposition 17.2. If \(U_N=\sum_{m=1}^N\chi(m)/m\), then
\[
\sum_{m\geq1}\frac{\chi(m)r^m}{m}
=(1-r)\sum_{N\geq1}U_Nr^N
=Lr+(1-r)\sum_{N\geq1}(U_N-L)r^N.
\]
For any \(\delta>0\), choose \(N_0\) so that \(|U_N-L|<\delta\) for \(N\geq N_0\). The finite initial part of the last sum tends to zero after multiplication by \(1-r\); the remaining part has absolute value at most \(\delta r\). This proves the Abel limit as \(r\uparrow1\).

Each logarithm on the finite right side of (CU7) has a limit, since \(\zeta^a\ne1\). The terms at \(a\) and \(p-a\) have equal character coefficients, because \(\chi\) is even, and conjugate logarithms. Their logarithms sum to \(2\log|1-\zeta^a|\). Taking the limit of (CU7) proves (CU6).

Applying (CU6) to \(\overline\chi\) gives
\[
|S_\chi|=\frac{\sqrt p}{2}|L(1,\overline\chi)|.
\]
Complex conjugation permutes the nontrivial characters of \(G\). Thus (CU5) becomes
\[
R_C=\left(\frac{\sqrt p}{2}\right)^{n-1}
 \prod_{\substack{\chi\in\widehat G\\\chi\ne1}}|L(1,\chi)|.
\tag{CU8}
\]
Theorem 17.3 proves that every factor is nonzero. In particular \(\det B\ne0\); independence of the displayed cyclotomic units follows from this calculation rather than being assumed at the start.

**The analytic class-number product.** The field \(F\) is already a specified cyclotomic subfield, with character group \(\widehat G\). The Euler-factor proof of Theorem 17.1 gives, for \(\Re s>1\),
\[
\zeta_F(s)=\zeta(s)
 \prod_{\substack{\chi\in\widehat G\\\chi\ne1}}L(s,\chi).
\]
The trivial character here is taken at its primitive conductor \(1\), so its factor is \(\zeta(s)\), including the Euler factor at \(p\). It is not the imprimitive principal character modulo \(p\).

Every other factor is holomorphic at \(1\) by Proposition 17.2. Divide by \(\zeta(s)\) and let real \(s\) decrease to \(1\). Theorem 16.2 gives the residue of \(\zeta_F\), while the residue of \(\zeta\) is \(1\). The field \(F\) has \(n\) real places, no complex places, exactly two roots of unity, and discriminant (CU3). Therefore
\[
\prod_{\substack{\chi\in\widehat G\\\chi\ne1}}L(1,\chi)
=\frac{2^{n-1}h^+R^+}{p^{(n-1)/2}}>0.
\tag{CU9}
\]
The product of the absolute values is the absolute value of this product, hence the same positive number. Substitution into (CU8) cancels every factor \(2\) and \(\sqrt p\), giving
\[
R_C=h^+R^+.
\tag{CU10}
\]

**From logarithmic determinants to the integer index.** By the unit theorem choose units \(\varepsilon_1,\ldots,\varepsilon_{n-1}\) whose classes form a basis of \(E^+/\{1,-1\}\). These are its only torsion units because \(F\) is real. Let
\[
U=(\log|\sigma_a(\varepsilon_j)|)_{a\ne1,\,1\leq j\leq n-1},
\qquad |\det U|=R^+.
\]
The unit theorem makes \(U\) nonsingular. Each \(c_b\) has a unique expression
\[
c_b=(-1)^{\delta_b}\prod_{j=1}^{n-1}\varepsilon_j^{m_{j,b}},
\qquad m_{j,b}\in\mathbf Z,
\]
up to the written sign. With \(M=(m_{j,b})\), logarithms give \(B=UM\). Since \(B\) is nonsingular, \(\det M\ne0\). The subgroup \(C^+\) contains both torsion units, so
\[
E^+/C^+\cong\mathbf Z^{n-1}/M\mathbf Z^{n-1}.
\]

For completeness, a nonsingular square integer matrix \(M\) has quotient of order \(|\det M|\). Integer row and column swaps, sign changes, and addition of an integer multiple of one row or column to another preserve both this quotient's order and the absolute determinant. Row operations change the ambient lattice basis; column operations change the chosen generators of its sublattice. The Euclidean algorithm diagonalizes \(M\): move a nonzero entry to the first pivot; division in its row and column either permits clearing an entry or produces a smaller positive pivot after a swap. Positive pivot sizes cannot decrease indefinitely. Eventually clear the first row and column, and continue on the remaining nonsingular block. No divisibility ordering of the final diagonal entries is needed. For the resulting diagonal matrix \(\operatorname{diag}(d_1,\ldots,d_{n-1})\), the quotient is \(\prod_j\mathbf Z/d_j\mathbf Z\), of order \(\prod_j|d_j|=|\det M|\).

Consequently the index is finite and
\[
[E^+:C^+]=|\det M|
=\frac{|\det B|}{|\det U|}
=\frac{R_C}{R^+}=h^+,
\]
as asserted. \(\square\)

For the classical theorem and its regulator approach, see Romyar Sharifi, [*Iwasawa Theory*, Chapter 4, Theorem 4.3.3](https://math.ucla.edu/~sharifi/notes/iwasawa-ch04.html), together with the even-character formula in Theorem 4.2.14 and the class-number product in Theorem 4.2.20. The proof above explicitly supplies the real integral basis, discriminant, augmentation determinant, Abel limit, independence, and regulator-index calculation in the prime-conductor case.

For example, if \(h^+=1\), these cyclotomic units generate all real units. Together with (4), they then generate \(E\) after adjoining \(\zeta\). Equation (8) concerns the real class number, whereas regularity below concerns the full class number.

### The golden ratio in the fifth cyclotomic field

Let \(p=5\), and set \(t=\zeta+\zeta^{-1}\). Since \(1+\zeta+\zeta^2+\zeta^3+\zeta^4=0\),
\[
t^2+t-1=0.
\]
Here \(t=2\cos(2\pi/5)>0\), so \(t=(\sqrt5-1)/2\). With \(\phi=(1+\sqrt5)/2=t+1\), we obtain
\[
\zeta^2+\zeta^3=-1-t=-\phi,
\qquad \zeta^2(1+\zeta)=-\phi.
\]
Consequently
\[
1+\zeta=-\zeta^3\phi.
\tag{9}
\]
The real factor \(-\phi\) is a unit: \(\phi^2=\phi+1\) gives \(\phi^{-1}=\phi-1\). Its quadratic norm is \(-1\). Thus (9) exhibits precisely the root-of-unity and real-unit factors of Proposition 13.1. The fundamental-unit calculation for \(\mathbf Q(\sqrt5)\) was given in *Dirichlet's unit theorem*.

## Regular primes and their class numbers

An odd prime \(p\) is **regular** if
\[
p\nmid h(\mathbf Q(\zeta_p)).
\tag{10}
\]
Equivalently, the class group of \(K\) has no nontrivial element killed by \(p\). One direction follows from Lagrange's theorem; the converse follows from Cauchy's theorem for a finite group.

Define the Bernoulli numbers by the formal power series
\[
\frac{T}{e^T-1}=\sum_{n\geq0}B_n\frac{T^n}{n!}.
\tag{11}
\]
In this convention \(B_1=-1/2\).

### Kummer's Bernoulli criterion

**Theorem (Kummer's criterion).** With the convention (11), an odd prime \(p\) is regular if and only if it divides none of the numerators, in lowest terms, of
\[
B_2,B_4,\ldots,B_{p-3}.
\tag{12}
\]
For \(p=3\), this list is empty.

All class numbers in this proof are ordinary ideal class numbers. Put

\[
F=K^+,\qquad n=\frac{p-1}{2},\qquad h_F=h^+,\qquad H=\frac{h_K}{h_F}.
\]

Initially \(H\) is a positive rational ratio; the proof does not assume that it is an integer. Its \(p\)-adic valuation will be identified with the order of the minus \(p\)-primary class group.

The proof uses the following proved programme results, with their hypotheses and normalizations:

1. *Cyclotomic fields*, Theorems 12.1–12.3, gives cyclotomic degrees, integral bases and discriminants, prime decomposition, and total ramification of \(\mathbf Q(\zeta_{p^r})\) at \(p\). In particular, \(|d_K|=p^{p-2}\), and every prime over \(p\) in \(\mathbf Q(\zeta_{p-1})\) has ramification and residue degrees both one.
2. Proposition 13.1 and the preceding root-of-unity calculation give
   \(E_K=\mu(K)E_F\), \(\mu(K)=\{\pm\zeta_p^a\}\), and \(\mu(F)=\{1,-1\}\). Their proof precedes this criterion and is independent of the cyclotomic-unit index formula.
3. *The Dedekind zeta function and the analytic class number formula*, Theorem 16.4, imports *Hecke L-functions and the Dedekind zeta function*, Theorem 10.2 and Corollary 10.4, with Proposition 10.3. For every number field \(T\),
   \[
   \zeta_T(s)=-\frac{h_TR_T}{w_T}s^{r_1(T)+r_2(T)-1}
   +O\!\left(s^{r_1(T)+r_2(T)}\right)
   \]
   near zero. The regulator is the weighted deleted-row regulator and equals one in rank zero. *Tate's local theory at the infinite places*, equations (5)–(6), in “Mellin continuation without a functional equation,” proves that \(1/\Gamma(s)\) is entire and equals \(s+O(s^2)\) at zero.
4. *Abelian number fields and Dirichlet L-functions at \(s=1\)*, Theorem 17.1, proves the primitive-character factorization for every cyclotomic subfield, including the ramified Euler factors. Its proof precedes its Gauss-sign, Kronecker–Weber and conductor–discriminant imports. Its first section supplies the finite character facts used here.
5. *Hilbert and ring class fields and quadratic prime forms*, Theorem 19.1, gives the **ordinary Hilbert class field**: for every number field \(T\), there is an abelian extension \(H_T/T\), unramified at every place including real places, with \(\operatorname{Gal}(H_T/T)\cong\operatorname{Cl}_T\). Its written proof, §1, uses the preceding class-field conductor and existence lesson, Theorem 18.4 and Proposition 18.3, and the earlier reciprocity and existence theorems.
6. *Hilbert's ramification theory in Galois extensions*, Theorem 6.2 and its tower arguments, identify inertia as the kernel of the residue action, give its projection to a Galois subfield, and characterize unramified finite primes by trivial inertia.
7. *Finiteness of the class number*, Theorem 8.1, supplies the Minkowski ideal-class bound. Unique fractional-ideal factorization and finiteness of the ordinary class group are earlier NT-ANT results.

The analytic inputs in items 3–4 and the class-field input in item 5 are forward programme dependencies of this proof. The Bernoulli congruence, special \(L\)-value computation, and plus-to-minus implication needed for the criterion are proved below.

#### A. The relative class-number product

Every embedding of \(F\) is real, and its two extensions to \(K\) form one complex-conjugate pair. The unit decomposition identifies

\[
E_F/\{1,-1\}\cong E_K/\mu(K):
\]

surjectivity follows from \(E_K=\mu(K)E_F\), and \(E_F\cap\mu(K)=\{1,-1\}\). A fundamental real-unit basis is therefore also a basis modulo roots of unity in \(K\). Each weighted logarithm at a complex place is twice its corresponding real-place logarithm in \(F\). Deleting one of the \(n\) corresponding rows multiplies the regulator determinant by \(2^{n-1}\). Thus

\[
R_K=2^{n-1}R_F,\qquad w_K=2p,\qquad w_F=2.
\]

This includes \(n=1\), when the regulator determinants are empty and equal one. Both zeta functions have order \(n-1\) at zero. Their leading terms give

\[
\lim_{s\to0}\frac{\zeta_K(s)}{\zeta_F(s)}
=H\frac{2^{n-1}}p. \tag{A1}
\]

The characters of \(\operatorname{Gal}(K/\mathbf Q)\) are the characters modulo \(p\). Those of \(F\) are exactly the even characters, since they kill complex conjugation, the residue \(-1\). The primitive-character factorization gives

\[
\frac{\zeta_K(s)}{\zeta_F(s)}
=\prod_{\substack{\chi\bmod p\\\chi(-1)=-1}}L(s,\chi)
\]

initially for \(\Re s>1\). Every odd character is nontrivial. We now prove that each factor is holomorphic at zero and evaluate it there.

For a nontrivial character \(\chi\) modulo \(p\), put

\[
F_\chi(t)=\frac{\sum_{a=1}^{p-1}\chi(a)e^{-at}}{1-e^{-pt}},
\qquad C_\chi=-\frac1p\sum_{a=1}^{p-1}a\chi(a).
\]

The character sum vanishes: multiplication of the nonzero residues by a unit whose character value is not one multiplies the sum by that value. Expanding the numerator and denominator at zero therefore gives \(F_\chi(t)=C_\chi+O(t)\), with an analytic expansion near zero. At infinity, \(F_\chi(t)=O(e^{-t})\). Expanding its denominator for \(t>0\) gives the absolutely convergent identity

\[
F_\chi(t)=\sum_{r\geq1}\chi(r)e^{-rt}.
\]

For \(\Re s>1\), absolute summability permits termwise integration and gives

\[
\Gamma(s)L(s,\chi)=\int_0^\infty F_\chi(t)t^{s-1}\,dt
=\frac{C_\chi}s+A_\chi(s),
\]

where

\[
A_\chi(s)=\int_0^1\bigl(F_\chi(t)-C_\chi\bigr)t^{s-1}\,dt
+\int_1^\infty F_\chi(t)t^{s-1}\,dt.
\]

The first integral is holomorphic on \(\Re s>-1\). On a compact subset, choose a lower real-part bound greater than \(-1\); the estimate \(F_\chi(t)-C_\chi=O(t)\) dominates every parameter derivative by an integrable power of \(t\) times a power of \(|\log t|\). Exponential decay makes the second integral entire by the same compact differentiation argument. Since \(1/\Gamma(s)=s+O(s^2)\), division continues \(L(s,\chi)\) holomorphically near zero and proves

\[
L(0,\chi)=C_\chi=-B_{1,\chi},\qquad
B_{1,\chi}:=\frac1p\sum_{a=1}^{p-1}a\chi(a). \tag{A2}
\]

This convention also equals \(\sum_a\chi(a)(a/p-1/2)\), since \(\sum_a\chi(a)=0\). No conjugate character is inserted in the definition.

The meromorphic identity theorem extends the product identity to this neighborhood of zero. The limit in (A1) is nonzero, so every odd-character value in (A2) is nonzero, and

\[
H=\frac p{2^{n-1}}
\prod_{\substack{\chi\bmod p\\\chi(-1)=-1}}L(0,\chi). \tag{A3}
\]

Thus the product formula also supplies the nonvanishing of its individual factors.

#### B. Bernoulli denominators and permutation congruences

Until part E, assume \(p\geq5\). Let \(v_p\) be the rational \(p\)-adic valuation normalized by \(v_p(p)=1\). A rational number is \(p\)-integral when its reduced denominator is prime to \(p\); write \(\mathbf Z_{(p)}\) for this ring.

The generating series gives \(B_0=1\) and \(B_1=-1/2\). Also \(B_m=0\) for odd \(m>1\): replacing \(t\) by \(-t\) shows that \(t/(e^t-1)+t/2\) is even.

For \(m\geq1\), put \(S_m=\sum_{a=1}^{p-1}a^m\). The finite geometric identity

\[
\frac{te^{pt}}{e^t-1}-\frac t{e^t-1}
=t\sum_{a=0}^{p-1}e^{at}
\]

and comparison of the coefficient of \(t^{m+1}\) give

\[
S_m=\frac1{m+1}\sum_{j=0}^m\binom{m+1}{j}B_jp^{m+1-j}.
\]

Isolating its final term and putting \(d=m-j\) yields

\[
B_m=\frac{S_m}p
-\sum_{d=1}^m\binom md B_{m-d}\frac{p^d}{d+1}. \tag{B1}
\]

This formula is used only for \(m\geq1\); \(B_0\) is the separate induction base. We claim that

\[
v_p(B_m)\geq-1\qquad(m\geq0). \tag{B2}
\]

Induct on \(m\). The term \(S_m/p\) has valuation at least \(-1\). By the induction hypothesis, each remaining summand in (B1) has valuation at least

\[
d-v_p(d+1)-1.
\]

For \(d=1\), this is zero, since \(p\geq5\). For \(d\geq2\), it is at least one: indeed \(v_p(d+1)\leq d-2\), because

\[
p^{d-1}\geq5^{d-1}>d+1.
\]

The last inequality follows by induction from \(5>3\). Every other term is therefore \(p\)-integral, proving (B2). A zero Bernoulli number satisfies the bound as well.

For even \(m\geq4\), the \(d=1\) term vanishes because \(B_{m-1}=0\). For \(m=2\), that summand is \(pB_1=-p/2\), whose contribution to \(B_m-S_m/p\) is \(+p/2\). Each \(d\geq2\) summand has valuation at least one. Consequently

\[
B_m-\frac{S_m}p\in p\mathbf Z_{(p)}
\qquad(m\geq2\text{ even}). \tag{B3}
\]

If \(p-1\nmid m\), then \(S_m\equiv0\pmod p\). Reduce \(m\) modulo \(p-1\) to \(r\in\{1,\ldots,p-2\}\). The polynomial \(X^r-1\) cannot vanish at all \(p-1\) nonzero residues, so some \(c\) satisfies \(c^m\not\equiv1\pmod p\). Multiplication by \(c\) permutes those residues and gives \(S_m\equiv c^mS_m\pmod p\). The assertion follows, and (B3) proves

\[
B_m\in\mathbf Z_{(p)}
\quad\text{if }m\geq2\text{ is even and }p-1\nmid m. \tag{B4}
\]

Now let \(m\geq2\) be even, with \(p\nmid m\) and \(p-1\nmid m\). Choose \(1\leq c\leq p-1\), and put \(q_a=\lfloor ca/p\rfloor\). The residues \(r_a=ca-pq_a\) permute \(1,\ldots,p-1\). The binomial expansion gives

\[
S_m=\sum_a r_a^m
\equiv c^mS_m-mp c^{m-1}\sum_a a^{m-1}q_a\pmod{p^2}.
\]

Divide by \(p\), replace \(S_m/p\) by \(B_m\) using (B3), and divide by the \(p\)-adic unit \(m\). This yields a congruence between \(p\)-integral rationals:

\[
(1-c^m)\frac{B_m}m
\equiv-c^{m-1}\sum_{a=1}^{p-1}a^{m-1}
\left\lfloor\frac{ca}p\right\rfloor\pmod p. \tag{B5}
\]

For odd \(k\in\{1,3,\ldots,p-4\}\), put \(m=1+pk\) and \(r=k+1\). Both are even, prime to \(p\), and not divisible by \(p-1\). They agree modulo \(p-1\), and \(2\leq r\leq p-3\). Choose \(c\) with \(c^r\not\equiv1\pmod p\), using the polynomial root bound. In (B5) for \(m\) and \(r\), the factors \(1-c^m\) and \(1-c^r\) have the same nonzero residue. The right sides agree because \(m-1\equiv r-1\pmod{p-1}\). Cancelling their common unit proves

\[
\frac{B_{1+pk}}{1+pk}
\equiv\frac{B_{k+1}}{k+1}\pmod p. \tag{B6}
\]

This is the exact Bernoulli congruence needed below, proved directly from the generating series and a permutation of residues.

#### C. Character values at one prime over \(p\)

Let \(T=\mathbf Q(\zeta_{p-1})\), choose a prime \(\mathfrak P\) over \(p\), and put \(R=\mathcal O_{T,\mathfrak P}\). By *Cyclotomic fields*, Theorem 12.3, this is a discrete valuation ring with maximal ideal \(pR\) and residue field \(\mathbf F_p\): \(p\nmid p-1\), and the order of \(p\) modulo \(p-1\) is one. Its normalized valuation \(v\) restricts to \(v_p\) on rational numbers. All subsequent congruences are in \(R\) or \(R/p^2R\); every \(p\)-integral rational belongs to \(R\).

Reduction identifies \(\mu_{p-1}\) with \(\mathbf F_p^\times\). To prove uniqueness, suppose two \((p-1)\)st roots \(x,y\) have the same nonzero residue \(a\). Then

\[
0=x^{p-1}-y^{p-1}
=(x-y)(x^{p-2}+x^{p-3}y+\cdots+y^{p-2}).
\]

The bracket reduces to \((p-1)a^{p-2}\neq0\), so it is a unit and \(x=y\). There are \(p-1\) roots and \(p-1\) nonzero residues, proving that reduction is a bijective group map. Its inverse defines the character

\[
\omega:\mathbf F_p^\times\longrightarrow\mu_{p-1},
\qquad\omega(a)\equiv a\pmod{pR}.
\]

Here “inverse” means the inverse of the reduction map. It does not mean the inverse character.

The same derivative argument proves uniqueness modulo \(p^2R\) of a \((p-1)\)st-root lift of a nonzero residue. If \(x-y=pd\), then

\[
x^{p-1}-y^{p-1}
\equiv pd(p-1)a^{p-2}\pmod{p^2R},
\]

which forces \(d\equiv0\pmod{pR}\). In particular,

\[
\omega(a)\equiv a^p\pmod{p^2R}. \tag{C1}
\]

Indeed, write \(\omega(a)=a+pt\), with \(t\in R\). Since \(\omega(a)^p=\omega(a)\), expanding \((a+pt)^p\) modulo \(p^2R\) gives (C1).

The character \(\omega\) has order \(p-1\), and its powers are all characters modulo \(p\). Its values run through the cyclic group \(\mu_{p-1}\), so the inverse image of a generator also shows that \(\mathbf F_p^\times\) is cyclic. The characters of a cyclic group are exactly these powers. Since \(\omega(-1)=-1\), the odd characters are \(\omega^k\) for \(k=1,3,\ldots,p-2\).

For such \(k\), equation (C1) implies

\[
\sum_{a=1}^{p-1}a\omega(a)^k
\equiv S_{1+pk}\pmod{p^2R}. \tag{C2}
\]

For \(k\leq p-4\), this numerator is zero modulo \(pR\): its residue is \(\sum_a a^{k+1}\), and \(p-1\nmid k+1\). Thus \(B_{1,\omega^k}\in R\). Divide (C2) by \(p\) and use (B3), then (B6), to obtain

\[
B_{1,\omega^k}
\equiv\frac{S_{1+pk}}p
\equiv B_{1+pk}
\equiv\frac{B_{k+1}}{k+1}\pmod{pR}. \tag{C3}
\]

The last equality also uses \(1+pk\equiv1\pmod p\). Each \(B_{k+1}\) is \(p\)-integral by (B4), and \(k+1\) is a \(p\)-adic unit. Therefore

\[
v(B_{1,\omega^k})\geq1
\quad\Longleftrightarrow\quad
p\text{ divides the reduced numerator of }B_{k+1},
\quad k=1,3,\ldots,p-4. \tag{C4}
\]

For the remaining character, \(k=p-2\), the numerator in (C2) reduces to
\(\sum_a a^{p-1}=p-1\equiv-1\pmod{pR}\). It is therefore a unit, and

\[
v(B_{1,\omega^{p-2}})=-1. \tag{C5}
\]

Every factor in (A3) is nonzero by part A. Taking its valuation, recalling \(L(0,\chi)=-B_{1,\chi}\) and that \(2\) is a unit, gives

\[
\begin{aligned}
v_p(H)
&=1+\sum_{\substack{1\leq k\leq p-2\\ k\text{ odd}}}v(B_{1,\omega^k})\\
&=\sum_{\substack{1\leq k\leq p-4\\ k\text{ odd}}}v(B_{1,\omega^k}).
\end{aligned} \tag{C6}
\]

All terms on the last line are nonnegative integers. In particular, \(v_p(H)\geq0\), and

\[
v_p(H)>0
\quad\Longleftrightarrow\quad
\text{some }B_2,B_4,\ldots,B_{p-3}
\text{ has numerator divisible by }p. \tag{C7}
\]

#### D. Passing from the relative to the full class number

Write \(A=\operatorname{Cl}_K[p^\infty]\) and \(A_F=\operatorname{Cl}_F[p^\infty]\) for the \(p\)-primary subgroups, using additive notation. A finite abelian group splits into its \(p\)-primary and prime-to-\(p\) parts: if its order is \(p^rd\) with \((p,d)=1\), a Bézout identity supplies complementary projections. Multiplication by two is an automorphism on \(A\) and \(A_F\).

Complex conjugation \(j\) acts on \(A\). The maps \((1+j)/2\) and \((1-j)/2\), with division by two interpreted as the inverse of multiplication by two, are complementary projections. Hence

\[
A=A^+\oplus A^-,\qquad
A^+=\{x:jx=x\},\quad A^-=\{x:jx=-x\}. \tag{D1}
\]

Let \(i:\operatorname{Cl}_F\to\operatorname{Cl}_K\) extend ideals, and let \(N:\operatorname{Cl}_K\to\operatorname{Cl}_F\) be the ideal norm. For the quadratic Galois extension \(K/F\), prime factorization gives

\[
Ni=2,\qquad iN=1+j. \tag{D2}
\]

Extending a prime and then taking its norm multiplies its exponent by \(\sum ef=[K:F]=2\), proving the first identity. For the second, extension of the norm of an ideal gives its product with its conjugate. This follows by checking a prime in each of the split, inert and ramified quadratic cases; multiplicativity proves it for every fractional ideal. Both maps take principal ideals to principal ideals, so the identities descend to class groups.

On the \(p\)-primary subgroups, \(i\) is injective because \(Ni=2\) is invertible. Its image lies in \(A^+\). Conversely, if \(x\in A^+\), then \(iN(x/2)=x\) by (D2). Consequently

\[
i:A_F\xrightarrow{\sim}A^+,\qquad
v_p(H)=\log_p|A^-|. \tag{D3}
\]

Thus (C7) tests whether the minus \(p\)-primary class group is nonzero. We must still exclude a nonzero plus group with zero minus group. We prove

\[
p\mid h_F\quad\Longrightarrow\quad A^-\neq0. \tag{D4}
\]

Suppose \(p\mid h_F\). The finite abelian class group has a quotient of order \(p\). Here is an elementary justification. An element of order \(p\) exists by induction on group order: choose a nontrivial cyclic subgroup; if its order is divisible by \(p\), it contains such an element. Otherwise pass to the smaller quotient and lift an order-\(p\) element, correcting its \(p\)th multiple inside the cyclic subgroup, where multiplication by \(p\) is invertible. Multiplication by \(p\) on the finite group therefore has nonzero kernel and cannot be onto. The quotient by its \(p\) multiples is a nonzero finite \(\mathbf F_p\)-vector space, and a nonzero linear functional gives a quotient of order \(p\).

By *Hilbert and ring class fields and quadratic prime forms*, Theorem 19.1, this quotient corresponds to a cyclic extension \(L/F\) of degree \(p\), unramified at every place. Since \(F\) is totally real and its real places do not ramify, \(L\) is totally real. The coprime degrees \(p\) and two give \(L\cap K=F\), so \(M=LK\) is Galois over \(F\) with

\[
\operatorname{Gal}(M/F)
\cong\operatorname{Gal}(L/F)\times\operatorname{Gal}(K/F).
\]

Extend \(j\) to \(M\) by fixing \(L\) and conjugating \(K\). This is complex conjugation and commutes with the first factor.

To prove that \(M/K\) is unramified at finite primes, fix a prime of \(M\) over \(F\). Its inertia group projects trivially to \(\operatorname{Gal}(L/F)\), because \(L/F\) is unramified. Thus inertia lies in the order-two factor. The relative inertia for \(M/K\) is its intersection with \(\operatorname{Gal}(M/K)\), the order-\(p\) factor, and is trivial. *Hilbert's ramification theory in Galois extensions*, Theorem 6.2, gives ramification index one. There is no real place of \(K\) to introduce infinite ramification.

Let \(\sigma\) generate \(\operatorname{Gal}(M/K)\). As a \(K\)-linear operator on \(M\), it satisfies \(X^p-1\), which splits over \(K\) with distinct roots. It is diagonalizable. Since \(\sigma\neq1\), a nonzero eigenvector has eigenvalue \(\zeta_p^t\), with \(t\not\equiv0\pmod p\). Raising it to a positive power inverse to \(t\) modulo \(p\) gives \(u\neq0\) with \(\sigma(u)=\zeta_pu\). Then \(u^p=a\in K\), \(u\notin K\), and the prime degree implies \(M=K(u)\).

Commutation of \(\sigma\) and \(j\), together with \(j(\zeta_p)=\zeta_p^{-1}\), gives \(\sigma(j(u))=\zeta_p^{-1}j(u)\). The element \(j(u)u\) is fixed by \(\sigma\); write it as \(b\in K^\times\). Then

\[
j(u)=\frac bu,\qquad a j(a)=b^p. \tag{D5}
\]

For each finite prime of \(K\), choose a prime of \(M\) above it and normalize both valuations to take integer values. Unramifiedness gives \(v_M(a)=v_K(a)\), whereas \(u^p=a\) gives \(v_M(a)=p v_M(u)\). Every exponent in the fractional ideal \((a)\) is therefore divisible by \(p\). Unique fractional-ideal factorization defines an ideal \(\mathfrak B\) with \((a)=\mathfrak B^p\). Equation (D5) gives

\[
(\mathfrak B j(\mathfrak B))^p=(b)^p,
\]

and hence \(\mathfrak B j(\mathfrak B)=(b)\), since the fractional-ideal group is free abelian on prime ideals. Thus \([\mathfrak B]\) is killed by \(p\) and satisfies \(j[\mathfrak B]=-[\mathfrak B]\): it belongs to \(A^-\).

Assume for contradiction that \(A^-=0\). Then \(\mathfrak B=(c)\), and \(a=c^p\varepsilon\) for a unit \(\varepsilon\in E_K\). Equation (D5) implies

\[
\varepsilon j(\varepsilon)
=\left(\frac b{c j(c)}\right)^p.
\]

The expression inside parentheses is a unit, because its \(p\)th power is a unit and therefore all its prime valuations are zero. In \(E_K/E_K^p\), the class of \(\varepsilon\) is consequently anti-invariant under \(j\).

The proved unit decomposition gives \(\varepsilon=\zeta_p^rv\), with \(v\in E_F\); the sign can be absorbed into \(v\). Then \(\varepsilon j(\varepsilon)=v^2\) is a \(p\)th power in \(E_K\). Multiplication by two is invertible in the exponent-\(p\) group \(E_K/E_K^p\), so \(v=d^p\) for some \(d\in E_K\). It follows that

\[
a=(cd)^p\zeta_p^r.
\]

If \(r\equiv0\pmod p\), then \(a\in K^{\times p}\), and \(X^p-a\) splits over \(K\). This forces \(u\in K\), contrary to \([M:K]=p\). If \(r\not\equiv0\pmod p\), then \(u/(cd)\) is a \(p\)th root of \(\zeta_p^r\), hence a primitive \(p^2\)nd root of unity. Thus

\[
M=K(\zeta_{p^2}).
\]

By *Cyclotomic fields*, Theorem 12.3, this extension is totally ramified of degree \(p\) at the prime over \(p\): the absolute ramification indices are \(p(p-1)\) and \(p-1\). This contradicts the unramifiedness of \(M/K\). Both cases are impossible, proving (D4).

The order of \(\operatorname{Cl}_K\) is \(|A^+||A^-|\) times a number prime to \(p\), and \(A^+\cong A_F\). Therefore, if \(p\mid h_K\), either \(A^-\neq0\) already, or \(p\mid h_F\), in which case (D4) again gives \(A^-\neq0\). Conversely, \(A^-\neq0\) implies \(p\mid h_K\). Equations (D3) and (C7) now prove the stated criterion for \(p\geq5\).

The obstruction has a concrete form: a nonzero plus class produces an ordinary unramified cyclic \(p\)-extension, whose Kummer radical defines an anti-invariant \(p\)-torsion ideal class. If that minus class vanished, the unit decomposition would reduce the radical to a \(p\)th root of \(\zeta_p\), which gives a ramified extension. This contradiction excludes a plus-only obstruction.

#### E. The empty-list case \(p=3\)

Here \(K=\mathbf Q(\zeta_3)\) is the imaginary quadratic field of discriminant \(-3\), by *Cyclotomic fields*. Its Minkowski bound, from *Finiteness of the class number*, Theorem 8.1, is

\[
\frac{2!}{2^2}\frac4\pi\sqrt3
=\frac{2\sqrt3}\pi<2.
\]

For example, \(\sqrt3<2\) and \(\pi>3\) give a bound below \(4/3\). Every ideal class has an integral representative of norm less than two, hence of norm one. That ideal is \(\mathcal O_K\), so \(h_K=1\) and \(3\nmid h_K\). This is exactly the vacuous Bernoulli condition for the empty list. \(\square\)

For an exact example,
\[
B_{32}=-\frac{7709321041217}{510},\qquad
7709321041217=37\cdot208360028141.
\tag{13}
\]
The denominator is prime to \(37\), so the criterion makes \(37\) irregular. These rational numbers can be calculated directly from (11), using \(B_0=1\) and
\[
\sum_{j=0}^{n}\binom{n+1}{j}B_j=0\quad(n\geq1).
\tag{14}
\]
Thus the numerical divisibility in (13) does not require a floating-point approximation.

### Exact class numbers for the eight small prime conductors

We now prove the full values
\[
h(\mathbf Q(\zeta_p))=1\quad(p=3,5,7,11,13,17,19),
\qquad h(\mathbf Q(\zeta_{23}))=3.
\tag{15}
\]
The calculation has two parts: a finite Minkowski certificate for \(h^+=1\), and an integer determinant for the ratio \(h/h^+\). Both parts are unconditional.

**The real class numbers.** Retain \(n=(p-1)/2\), \(t=\zeta+\zeta^{-1}\), and define
\[
S_0(T)=2,\quad S_1(T)=T,\quad
S_{j+1}(T)=T S_j(T)-S_{j-1}(T),\qquad
F_p(T)=1+\sum_{j=1}^{n}S_j(T).
\]
The integral-basis argument in (CU1) gives \(\mathcal O_{K^+}=\mathbf Z[t]\). Moreover
\(F_p(t)=1+\sum_{j=1}^n(\zeta^j+\zeta^{-j})=0\), and its monic degree is \(n=[K^+:\mathbf Q]\), so \(F_p\) is the minimal polynomial. The elements \(b_0=1\), \(b_j=S_j(t)\), \(1\le j<n\), form an integral basis: each \(S_j\) is monic of degree \(j\), so their change from the power basis is triangular with diagonal one.

By (CU3), the discriminant is \(D=p^{n-1}\). The proved Minkowski bound in *Finiteness of the class number*, Theorem 8.1, says that prime ideals of norm at most
\[
M=\frac{n!}{n^n}\sqrt{D}
\]
generate the class group. To see the prime version directly, take an integral ideal of norm at most \(M\) representing any class, and factor it; each prime factor has norm at most that ideal's norm. Put
\[
N=(n!)^2D,\qquad E=n^{2n},\qquad
B=\operatorname{isqrt}(\lfloor N/E\rfloor).
\]
Thus \(B^2 E\le N<(B+1)^2 E\), so \(B=\lfloor M\rfloor\) by integer comparisons. The following table lists every orbit of prime ideals with norm at most \(B\). Its entries \((q,f)\) give rational prime and residue degree; all primes in an orbit have norm \(q^f\).

| \(p\) | \(n\) | \(B\) | Required prime orbits \((q,f)\) |
|---:|---:|---:|:---|
| 3 | 1 | 1 | none |
| 5 | 2 | 1 | none |
| 7 | 3 | 1 | none |
| 11 | 5 | 4 | none |
| 13 | 6 | 9 | none |
| 17 | 8 | 48 | \(2,4\), \(17,1\) |
| 19 | 9 | 122 | \(19,1\), \(37,1\), \(113,1\) |
| 23 | 11 | 900 | \(23,1\), \(47,1\), \(137,1\), \(139,1\), \(229,1\), \(277,1\), \(367,1\), \(461,1\), \(599,1\), \(643,1\), \(691,1\), \(827,1\), \(829,1\) |

Here is a complete finite way to obtain that list. Enumerate the rational primes \(2\le q\le B\) by trial division. For \(q\ne p\), the cyclotomic Frobenius is the class of \(q\) in \((\mathbf Z/p\mathbf Z)^\times/\{\pm1\}\), so \(f\) is the first positive integer with \(q^f\equiv\pm1\pmod p\). Retain the orbit exactly when \(q^f\le B\). At \(q=p\), there is one totally ramified prime of norm \(p\). These rules follow from the proved cyclotomic splitting and Frobenius theorems. For \(p=23\), the real Galois group has prime order \(11\); all non-split unramified primes have norm at least \(2^{11}=2048>900\). The split primes at most \(900\) are precisely the twelve listed above. For the smaller conductors the same bounded enumeration gives the displayed rows.

The following integral elements prove that all the required orbits are principal. The table records signed field norms, not approximate absolute values.

| \(p\) | Generator \(\alpha\) in the \(b_j\) basis | \(N_{K^+/\mathbf Q}(\alpha)\) |
|---:|:---|---:|
| 17 | \(1 -b_{1} -b_{4}\) | 16 |
| 17 | \(2 -b_{1}\) | 17 |
| 19 | \(2 -b_{1}\) | 19 |
| 19 | \(1 -b_{1} +b_{3}\) | -37 |
| 19 | \(1 +b_{1} -b_{2}\) | -113 |
| 23 | \(2 -b_{1}\) | 23 |
| 23 | \(1 +b_{1} -b_{3}\) | 47 |
| 23 | \(1 -b_{1} +b_{7}\) | -137 |
| 23 | \(1 -b_{1} +b_{3}\) | 139 |
| 23 | \(b_{1} +b_{2} -b_{3}\) | -229 |
| 23 | \(1 -b_{1} -b_{2}\) | -277 |
| 23 | \(b_{1} +b_{3} -b_{4}\) | -367 |
| 23 | \(b_{1} -b_{3} -b_{8}\) | -461 |
| 23 | \(1 -b_{1} -b_{2} +b_{3}\) | -599 |
| 23 | \(b_{1} +b_{2} -b_{5}\) | -643 |
| 23 | \(b_{1} -b_{3} +b_{4}\) | 691 |
| 23 | \(b_{1} +b_{4} +b_{5}\) | -827 |
| 23 | \(1 -b_{1} -b_{3} +b_{8}\) | -829 |

Every norm in this table can be checked from the stated recurrence and integer matrices. Express \(\alpha=g(t)\). Reduce \(g(T)T^j\), \(0\le j<n\), by monic division by \(F_p(T)\); its coefficients give column \(j\) of the multiplication matrix. Its determinant is the norm by definition. Thus no integral-basis guess, floating-point root, class-number table or unproved unit calculation enters the check. For instance, the \(p=17\) element is \(1-b_1-b_4=-t^4+4t^2-t-1\), and its matrix determinant is \(16\). In every ramified row, the uniform formula gives \(N(2-t)=F_p(2)=p\).

If \(|N(\alpha)|=q^f\), ideal-norm multiplicativity shows that \((\alpha)\) is one prime over \(q\), with exponent one: all prime divisors lie over \(q\), and every prime over \(q\) already has norm \(q^f\). This includes the norm \(16\) row, where the two primes above \(2\) both have residue degree four. Galois transitivity then proves every other prime in that orbit principal, by conjugating \(\alpha\). All Minkowski generators are therefore trivial, proving
\[
h^+=1\qquad(p=3,5,7,11,13,17,19,23).
\tag{CN1}
\]

The integer certificate includes every polynomial, exact bound, prime orbit and norm matrix. Its standard-library Python verifier recomputes all of them from the recurrence and exact determinants.

**The relative class numbers.** The already proved special-value formula (A3) gives
\[
\frac h{h^+}=\frac p{2^{n-1}}\prod_{\chi(-1)=-1}L(0,\chi),
\qquad L(0,\chi)=-\frac1p\sum_{a=1}^{p-1}a\chi(a).
\]
We turn this into one integer determinant. Write \(r(x)\) for the representative of a nonzero residue \(x\) in \(\{1,\ldots,p-1\}\), and form
\[
H_{a,b}=2r(ab^{-1})-p\qquad(1\le a,b\le n).
\tag{CN2}
\]
On the vector space with basis \(e_a\), indexed by \(G=(\mathbf Z/p\mathbf Z)^\times\), let
\(T(e_b)=\sum_a r(ab^{-1})e_a\).
Its anti-invariant subspace for \(e_a\mapsto e_{-a}\) has basis \(u_b=e_b-e_{-b}\), \(1\le b\le n\). The coefficient at \(e_a\) of \(T(u_b)\) is
\(r(ab^{-1})-r(-ab^{-1})=2r(ab^{-1})-p\), and the coefficient at \(e_{-a}\) is its negative. Hence its matrix is exactly \(H\).

The character eigenvectors in the augmentation proof form a full basis; exactly the odd characters lie in this anti-invariant subspace. The eigenvalues are \(\sum_a r(a)\chi(a)^{-1}\). Inversion permutes odd characters, so
\[
\det H=\prod_{\chi(-1)=-1}\sum_{a=1}^{p-1}a\chi(a),\qquad
\frac h{h^+}=\frac{(-1)^n\det H}{(2p)^{n-1}}.
\tag{CN3}
\]
This argument also works for \(p=3\), where \(H=(-1)\). Exact integer determinants give:

| \(p\) | \(\det H\) | \(h/h^+\) |
|---:|---:|---:|
| 3 | -1 | 1 |
| 5 | 10 | 1 |
| 7 | -196 | 1 |
| 11 | -234256 | 1 |
| 13 | 11881376 | 1 |
| 17 | 52523350144 | 1 |
| 19 | -4347792138496 | 1 |
| 23 | -127262242448329728 | 3 |

For reproducibility, the relative determinant verifier constructs (CN2) from modular inverses and uses exact rational Gaussian elimination; each determinant is an integer. Together with (CN1), (CN3) proves (15), including the full value at \(23\). In particular \(23\) is regular even though its class group has order three. \(\square\)

## The first case of Fermat's equation

**Theorem 13.3 (Kummer).** If \(p\geq5\) is regular, there are no integers \(x,y,z\) satisfying
\[
x^p+y^p=z^p,\qquad p\nmid xyz.
\tag{16}
\]

We prove two algebraic congruence facts before assembling the argument. Congruences modulo \(p\) below mean membership in the ideal \(p\mathcal O_K\), rather than merely in \(\lambda\mathcal O_K\).

**Power congruence.** For every \(\alpha\in\mathcal O_K\), there is an integer \(a\) such that
\[
\alpha^p\equiv a\pmod{p\mathcal O_K},
\qquad \overline\alpha^{\,p}\equiv a\pmod{p\mathcal O_K}.
\tag{17}
\]
To prove this, write \(\alpha=\sum_{j=0}^{p-2}a_j\zeta^j\) in the integral basis. In any commutative ring of characteristic \(p\), raising to the \(p\)-th power is additive. Since \(\zeta^{jp}=1\) and \(a_j^p\equiv a_j\pmod p\), its \(p\)-th power is congruent to \(a=\sum a_j\). The same calculation for the conjugate has the same integer \(a\). This does not require the quotient ring to be reduced; indeed (2) shows that it is not reduced.

**Coefficient congruence.** If \(b_0,\ldots,b_{p-1}\in\mathbf Z\), then
\[
\sum_{j=0}^{p-1}b_j\zeta^j\in p\mathcal O_K
\quad\Longleftrightarrow\quad
b_0\equiv b_1\equiv\cdots\equiv b_{p-1}\pmod p.
\tag{18}
\]
Eliminate \(\zeta^{p-1}\) using \(\sum_{j=0}^{p-1}\zeta^j=0\). The result is
\(\sum_{j=0}^{p-2}(b_j-b_{p-1})\zeta^j\).
Because these \(p-1\) powers are an integral basis, membership in \(p\mathcal O_K\) means exactly that each coefficient is divisible by \(p\). This proves both directions of (18).

**Proof of Theorem 13.3.** Suppose (16) holds. Divide by the common greatest positive divisor of \(x,y,z\). Since \(p\nmid xyz\), this division preserves the first-case condition. The resulting triple is pairwise coprime: a prime dividing two entries also divides the third by the equation.

We may also arrange
\[
x\not\equiv y\pmod p.
\tag{19}
\]
For this, put \(u=x,v=y,w=-z\). Their nonzero residues satisfy \(u+v+w=0\) in \(\mathbf F_p\). If all three residues were equal, we would have \(3u=0\), impossible for \(p\geq5\). Choose two unequal residues, call the corresponding integers \(x,y\), and negate the remaining integer to obtain the new \(z\). Since \(p\) is odd, the equation, pairwise coprimality and \(p\nmid xyz\) all persist.

Factor the equation in \(\mathcal O_K\):
\[
\prod_{i=0}^{p-1}(x+\zeta^i y)=z^p.
\tag{20}
\]
The principal ideals generated by its factors are pairwise relatively prime. To check this, suppose a prime ideal \(\mathfrak q\) divides the \(i\)-th and \(j\)-th factors, with \(i\ne j\). Their difference is \((\zeta^i-\zeta^j)y\). Proposition 13.2 shows that \(\zeta^i-\zeta^j\) is \(\lambda\) times a unit. If \(\mathfrak q\nmid(p)\), it follows that \(y\in\mathfrak q\), and then \(x\in\mathfrak q\). Bezout's identity for the coprime integers \(x,y\) would put \(1\) in \(\mathfrak q\), a contradiction. If \(\mathfrak q\mid(p)\), (2) gives \(\mathfrak q=(\lambda)\). Reduction of either factor yields \(p\mid x+y\). But (16) modulo \(p\) gives \(z\equiv x+y\pmod p\), contradicting \(p\nmid z\).

Unique factorization of ideals applied to (20) now gives
\[
(x+\zeta y)=\mathfrak a^p
\tag{21}
\]
for an integral ideal \(\mathfrak a\): every prime occurs in only one factor, and its exponent in the product is divisible by \(p\). The class of \(\mathfrak a\) is killed by \(p\). Regularity and finiteness of the class group make this class trivial. Write \(\mathfrak a=(\alpha)\), where \(\alpha\in\mathcal O_K\), since \(\mathfrak a\) is integral. Equality (21) then says
\[
x+\zeta y=\varepsilon\alpha^p=\zeta^r v\alpha^p,
\qquad v\in E^+.
\tag{22}
\]
Here equal nonzero principal ideals differ by a unit, and the last equality uses Proposition 13.1.

Conjugating (22) and applying (17) gives, for the same integer \(a\),
\[
x+\zeta y\equiv\zeta^r va,
\qquad x+\zeta^{-1}y\equiv\zeta^{-r}va
\pmod{p\mathcal O_K}.
\]
No division by \(a\) is needed. Multiply the second congruence by \(\zeta^{2r}\) and subtract. If \(s\equiv2r\pmod p\), then
\[
x+y\zeta-x\zeta^s-y\zeta^{s-1}\equiv0
\pmod{p\mathcal O_K}.
\tag{23}
\]
Reduce all exponents modulo \(p\). The left side has coefficients in at most four positions among \(0,\ldots,p-1\). Because \(p\geq5\), at least one position has coefficient zero. Equation (18) consequently forces every coefficient to be zero modulo \(p\).

If the four positions \(0,1,s,s-1\) are distinct, this would force \(p\mid x\) and \(p\mid y\). A coincidence is possible only for \(s=0,1,2\). Their polynomials, with exponents reduced modulo \(p\), are respectively
\[
\begin{array}{c|c|c}
s&x+yX-xX^s-yX^{s-1}&\text{consequence}\\
0&y(X-X^{p-1})&p\mid y\\
1&(x-y)(1-X)&x\equiv y\pmod p\\
2&x(1-X^2)&p\mid x.
\end{array}
\tag{24}
\]
The relevant two exponents in each row are distinct for \(p\geq5\). The first and third conclusions contradict \(p\nmid xyz\); the middle contradicts (19). This proves the theorem, including \(p=5\). \(\square\)

Regularity was used exactly once, when (21) had to become an element power. The proof does not require the class number to equal one. The first-case restriction was used to keep the factors coprime at the unique ramified prime. If \(p\mid z\), the factors acquire the common ramified prime; when another coordinate is divisible by \(p\), the later nonzero-residue argument requires a different treatment. The proof above supplies no second-case conclusion.

## Exercises and complete solutions

**Exercise 1.** Show that \(1+\zeta_5\) is a unit, and express it as a power of \(\zeta_5\) times a real unit.

**Solution 1.** It is \(u_2\). The inverse exponent \(b=3\) gives the explicit inverse \(1+\zeta^2+\zeta^4\), because \(2\cdot3\equiv1\pmod5\). Multiplying yields \(1\) after using \(1+\zeta+\cdots+\zeta^4=0\). Equation (9) gives \(1+\zeta=\zeta^3(-\phi)\). The real factor lies in \(\mathbf Q(\sqrt5)\) and has inverse \(-\phi^{-1}=1-\phi\). Thus both the inverse and the real-unit decomposition are explicit.

**Exercise 2.** Under (16) and pairwise coprimality of \(x,y,z\), prove that the ideals \((x+\zeta^i y)\), \(0\leq i<p\), are pairwise coprime. Identify the role of the first-case hypothesis.

**Solution 2.** A common prime \(\mathfrak q\) for two factors divides \((\zeta^i-\zeta^j)y\). The first factor of this product is a unit times \(\lambda\). Away from \(\lambda\), this forces \(\mathfrak q\mid(y)\), then \(\mathfrak q\mid(x)\), contrary to the integer Bezout identity. At \(\lambda\), every factor reduces to \(x+y\in\mathbf F_p\). A common divisor there requires \(x+y\equiv0\pmod p\); the equation gives \(z\equiv x+y\pmod p\), impossible in the first case. Therefore no common prime exists. The restriction \(p\nmid z\) is exactly what excludes the common ramified prime; without it, many factors can acquire that divisor.

**Exercise 3.** Prove that every \(\alpha\in\mathbf Z[\zeta_p]\) has \(\alpha^p\equiv a\pmod{p\mathbf Z[\zeta_p]}\) for a rational integer \(a\). Show that the same \(a\) works for its conjugate.

**Solution 3.** In the integral basis, write \(\alpha=\sum_{j=0}^{p-2}a_j\zeta^j\). The binomial coefficients between the endpoints are divisible by \(p\), so repeated binomial expansion gives \(\alpha^p\equiv\sum a_j^p\zeta^{jp}\equiv\sum a_j\). Replacing \(j\) by \(-j\) gives the same sum for the conjugate. This establishes the full congruence modulo \(p\mathcal O_K\), including its nilpotent elements, and proves (17).

**Exercise 4.** Complete the final congruence argument from (23). Explain why its normalization and the assumption \(p\geq5\) are necessary.

**Solution 4.** Relation (18) says that all \(p\) coefficients of the polynomial in (23) are equal modulo \(p\). Its support has at most four positions; \(p\geq5\) leaves a zero coefficient, forcing them all to vanish. If its positions are distinct, the coefficient at \(0\) is \(x\), a contradiction. Otherwise comparing \(0,1,s,s-1\) gives exactly \(s=0,1,2\), with the three reductions in (24). The middle case only forces \(x\equiv y\), which is why we first choose unequal residues. That choice is possible because a triple of equal nonzero residues with sum zero would give \(3x=0\), impossible for \(p\geq5\). For \(p=3\), the support need not leave a zero position and this normalization also fails. The theorem as proved therefore starts at \(5\). The separate first-case assertion for exponent \(3\) follows from cubes modulo \(9\): a number prime to \(3\) has cube \(1\) or \(-1\), and three such cubes cannot sum to zero modulo \(9\).

## What this lesson does not prove

The unit-index theorem (8), Bernoulli criterion (12), and full class numbers (15) have complete receiving proofs above. The analytic continuation and zero-leading-term proof are the exact later-course analytic inputs recorded in the criterion; the ordinary Hilbert-class-field theorem supplies the indicated class-field input. These arguments make no claim about the second case of Fermat's equation, irregular exponents, or cyclotomic-unit indices at general composite conductors. The earlier elementary field, ideal, unit and Minkowski results are used with the precise hypotheses stated above.

## References

- J. S. Milne, [*Algebraic Number Theory*, v3.08](https://www.jmilne.org/math/CourseNotes/ANT.pdf), Chapter 6, “Class numbers of cyclotomic fields,” printed p.101; “Units in cyclotomic fields,” Proposition 6.7, pp.101–102; “The first case of Fermat's last theorem for regular primes,” Theorem 6.8 and Lemmas 6.9–6.11, pp.102–104.
- Romyar Sharifi, [*Iwasawa Theory*, Chapter 4](https://math.ucla.edu/~sharifi/notes/iwasawa-ch04.html), §4.3, Definition 4.3.1 and Theorem 4.3.3, for the real cyclotomic-unit subgroup and its class-number index.
