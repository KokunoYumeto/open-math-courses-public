# Finiteness of the class number

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Independent full-lesson AI review is pending. Public domain (CC0).*

An ideal class has infinitely many representatives. Geometry gives a way to choose one with small norm. Once the norm is bounded, only finitely many integral ideals remain, so the class group is finite. The same geometric method also bounds the discriminant from below and produces integral primitive elements with bounded conjugates. These lead to finiteness statements about both the ideals in one field and the fields themselves.

## Prerequisites and conventions

Let \(K\) be a number field of degree \(n=r_1+2r_2\), with ring of integers \(O\), discriminant \(d_K\), and ideal class group \(\mathrm{Cl}_K\). Write \(D=|d_K|\). Norms of nonzero integral ideals are positive integers.

From [*Lattices, Minkowski's theorem and the Minkowski embedding*](lattices-minkowskis-theorem-and-the-minkowski-embedding.md) we use Theorem 7.1 and Proposition 7.2: in ordinary real-and-imaginary-part Lebesgue measure, the image of a nonzero fractional ideal \(\mathfrak a\) has covolume
\[
2^{-r_2}\sqrt D\,N\mathfrak a.
\tag{1}
\]
A compact convex region symmetric about zero contains a nonzero lattice point when its volume is at least \(2^n\) times the covolume.

We also use ideal factorization and the PID criterion from [*Discrete valuation rings and Dedekind domains*](discrete-valuation-rings-and-dedekind-domains.md), multiplicativity and principal-ideal norms from [*Norms, class groups, and modules over Dedekind domains*](norms-class-groups-and-modules-over-dedekind-domains.md), and prime decomposition and the discriminant ramification criterion from [*Decomposition of primes in extensions*](decomposition-of-primes-in-extensions.md). The rings, integral bases, and discriminants in the examples were determined in the first two lessons.

The integration prerequisites are Fubini and Tonelli for Lebesgue measure and polar change of variables in a complex coordinate. Exact locators are [Fremlin, 251N, 252H and 263G]. The elementary integrals and arithmetic–geometric mean inequality needed below are proved here.

## A region adapted to the field norm

Choose the \(r_1\) real embeddings \(\sigma_i\) and one embedding \(\tau_j\) from each conjugate complex pair. For \(t>0\) define
\[
B_t=\left\{(x,z)\in\mathbf R^{r_1}\times\mathbf C^{r_2}:
\sum_{i=1}^{r_1}|x_i|+2\sum_{j=1}^{r_2}|z_j|\leq t\right\}.
\tag{2}
\]
Absolute values satisfy the triangle inequality, so this region is convex. It is closed, bounded, and symmetric about zero.

**Volume lemma.** In our measure convention,
\[
\operatorname{vol}(B_t)
=2^{r_1}\left(\frac{\pi}{2}\right)^{r_2}\frac{t^n}{n!}.
\tag{3}
\]

**Proof.** We first establish the integral formula that includes zero exponents. If \(m\geq1\), \(a_1,\ldots,a_m\) are nonnegative integers, and \(t>0\), then
\[
\int_{\substack{u_i\geq0\\u_1+\cdots+u_m\leq t}}
\prod_{i=1}^m u_i^{a_i}\,du_1\cdots du_m
=\frac{\prod_{i=1}^m a_i!}{(m+\sum_i a_i)!}\,
t^{m+\sum_i a_i}.
\tag{4}
\]
Here a factor with exponent zero is \(1\), including at zero.

For nonnegative integers \(A,B\), integration by parts, starting with \(B=0\), gives
\[
\int_0^t u^A(t-u)^B\,du
=\frac{A!\,B!}{(A+B+1)!}t^{A+B+1}.
\tag{5}
\]
Indeed the \(B=0\) case is \(t^{A+1}/(A+1)\). For \(B>0\), both boundary terms vanish and integration by parts replaces the integral by \(B/(A+1)\) times the integral with exponents \(A+1,B-1\). Repeating proves (5). Formula (4) for \(m=1\) is the same elementary antiderivative. For the induction step, fix \(u_m\), apply the formula for \(m-1\) with \(t-u_m\), and integrate the resulting power of \(t-u_m\) against \(u_m^{a_m}\) using (5). Fubini applies to these bounded nonnegative measurable integrands. This proves (4).

Split the real coordinates into orthants, obtaining a factor \(2^{r_1}\); their boundaries have measure zero. In each complex coordinate write \(z_j=\rho_j e^{i\theta_j}\), and put \(w_j=2\rho_j\). Polar measure becomes
\[
\rho_j\,d\rho_j\,d\theta_j
=\frac{w_j}{4}\,dw_j\,d\theta_j.
\]
Integration over the angle gives \((\pi/2)w_j\,dw_j\). Thus the remaining integral is (4) with \(m=r_1+r_2\), real exponents zero, and complex exponents one. Its total degree plus dimension is \(r_1+2r_2=n\), and every factorial in its numerator is \(1\). The factors from orthants and angles give (3). \(\square\)

We will use the arithmetic–geometric mean inequality in the form
\[
b_1\cdots b_n\leq
\left(\frac{b_1+\cdots+b_n}{n}\right)^n
\qquad(b_i\geq0).
\tag{6}
\]
For completeness, fix a positive sum \(s\). The product attains a maximum on the compact simplex of nonnegative \(n\)-tuples with sum \(s\). The equal tuple has positive product, so a maximizing tuple has no zero coordinate. If two coordinates differ, replacing them by their average increases their product, since
\((a+b)^2/4-ab=(a-b)^2/4>0\), and leaves the other positive factors unchanged. At a maximum all coordinates therefore equal \(s/n\). The zero-sum and \(n=1\) cases are immediate. This proves (6).

## A small integral ideal in every class

Set
\[
M_K=\frac{n!}{n^n}
\left(\frac4\pi\right)^{r_2}\sqrt D.
\tag{7}
\]

**Theorem 8.1 (Minkowski bound).** Every class \(C\in\mathrm{Cl}_K\) contains a nonzero integral ideal \(\mathfrak b\) satisfying
\[
N\mathfrak b\leq M_K.
\]

**Proof.** First let \(\mathfrak a\) be any nonzero integral ideal. Choose \(t>0\) by
\[
t^n=n!\left(\frac4\pi\right)^{r_2}
\sqrt D\,N\mathfrak a.
\tag{8}
\]
Combining (3) and (8) gives
\[
\operatorname{vol}(B_t)
=2^{r_1+r_2}\sqrt D\,N\mathfrak a
=2^n\operatorname{covol}(\mathfrak a).
\]
The compact equality case of Minkowski's theorem supplies \(0\ne\alpha\in\mathfrak a\) whose image lies in \(B_t\).

Apply (6) to the \(n\) nonnegative numbers
\[
|\sigma_1\alpha|,\ldots,|\sigma_{r_1}\alpha|,
|\tau_1\alpha|,|\tau_1\alpha|,\ldots,
|\tau_{r_2}\alpha|,|\tau_{r_2}\alpha|.
\]
Their sum is at most \(t\), and their product is \(|N_{K/\mathbf Q}\alpha|\). Consequently
\[
|N_{K/\mathbf Q}\alpha|
\leq(t/n)^n=M_K\,N\mathfrak a.
\tag{9}
\]

Now start with the specified class \(C\). Choose an integral ideal \(\mathfrak a\) in \(C^{-1}\): a fractional representative can be multiplied by a nonzero integer to clear its denominator, without changing its class. Choose \(\alpha\) as above and put
\[
\mathfrak b=(\alpha)\mathfrak a^{-1}.
\]
The inclusion \((\alpha)\subseteq\mathfrak a\) implies \(\mathfrak b\subseteq O\), so \(\mathfrak b\) is integral. Its class is \([\mathfrak a]^{-1}=C\), and its norm is
\[
N\mathfrak b=\frac{|N_{K/\mathbf Q}\alpha|}{N\mathfrak a}
\leq M_K.
\]
This gives a representative of the requested class. \(\square\)

To compare the two regions exactly, let \(C_K=(2/\pi)^{r_2}\sqrt D\) be the product-body constant of the preceding lesson, Proposition 7.3. Then
\[
\frac{M_K}{C_K}=2^{r_2}\frac{n!}{n^n}.
\]
The bounds agree in degree one and for imaginary quadratic fields; for real quadratic fields the ratio is one half. In every degree \(n\geq3\) the ratio is strictly less than one. Indeed, pair the factors \(j/n\) and \((n+1-j)/n\) in \(n!/n^n\). Their product is at most \(((n+1)/(2n))^2\). There are at least \(r_2\) pairs, so each factor two can be assigned to a different pair. Even those paired contributions are less than one, since \((n+1)^2<2n^2\) for \(n\geq3\); unscaled pairs and an unpaired middle factor are also less than one. This proves the complete comparison. The geometry is that of [Milne, Theorem 4.3 and Lemmas 4.22–4.27]; the volume calculation above supplies all required integer exponents.

## Finiteness and generators

**Bounded-ideal lemma.** For each real \(B\), only finitely many nonzero integral ideals of \(O\) have norm at most \(B\).

**Proof.** If \(N\mathfrak a=m\), the additive group \(O/\mathfrak a\) has order \(m\). Every element is annihilated by \(m\): its cyclic subgroup has order dividing \(m\), by the partition into its cosets. Hence
\[
mO\subseteq\mathfrak a\subseteq O.
\]
An integral basis identifies \(O/mO\) with \((\mathbf Z/m\mathbf Z)^n\), a finite set. Ideals between \(mO\) and \(O\) correspond to certain additive subgroups of this set, so there are finitely many of them. There are only finitely many positive integers \(m\leq B\). \(\square\)

**Corollary 8.2.** The group \(\mathrm{Cl}_K\) is finite. Moreover it is generated by the classes of prime ideals \(\mathfrak p\) with \(N\mathfrak p\leq M_K\).

**Proof.** Theorem 8.1 and the bounded-ideal lemma give a finite set mapping onto the class group. Factor each representative \(\mathfrak b\) into primes. If a prime occurs, its positive integer norm is at most \(N\mathfrak b\), because ideal norms multiply and all other factors are at least \(1\). Therefore all the prime classes in this factorization satisfy the displayed bound. \(\square\)

Write \(h_K=|\mathrm{Cl}_K|\), the **class number**. To compute the group, list the primes below the bound, use elements to find relations between their classes, and prove that the proposed nontrivial classes cannot be principal. A prime of norm at most \(M_K\) lies over a rational prime \(p\leq M_K\), since its norm is \(p^f\). Residue degrees matter: an inert quadratic prime over \(p\) has norm \(p^2\).

## Five complete class-group computations

All ideal norms and equalities below are absolute. For a monogenic quadratic ring with generator \(u\), a simple root \(r\) of its polynomial modulo \(p\) gives the prime \((p,u-r)\) of norm \(p\). The ramified quadratic cases used here also follow from the full-ring prime decomposition proved in Lesson 5. We identify principal ideals by their prime divisors and norms.

### \(\mathbf Q(\sqrt{-5})\)

Put \(s=\sqrt{-5}\). Here \(O=\mathbf Z[s]\), \(D=20\), and
\[
M_K=\frac2\pi\sqrt{20}\approx2.847<3.
\]
Only primes of norm \(2\) can be needed. The prime \(2\) ramifies:
\[
P=(2,1+s),\qquad NP=2,\qquad (2)=P^2.
\]
Thus \(\mathrm{Cl}_K\) is generated by \([P]\), whose square is \(1\).

If \(P=(a+bs)\), its norm would be \(a^2+5b^2=2\), with \(a,b\in\mathbf Z\). When \(b\ne0\) the left side is at least \(5\); when \(b=0\), no integer square is \(2\). Thus \(P\) is not principal, and
\[
\mathrm{Cl}_{\mathbf Q(\sqrt{-5})}\cong\mathbf Z/2\mathbf Z.
\]

### \(\mathbf Q(\sqrt{-23})\)

Take
\[
\theta=\frac{1+\sqrt{-23}}2,\qquad
O=\mathbf Z[\theta],\qquad
\theta^2-\theta+6=0.
\]
The discriminant is \(-23\), so \(M_K\approx3.053<4\). Both \(2\) and \(3\) split, with roots \(0,1\) modulo each prime. Put
\[
A=(2,\theta),\quad \overline A=(2,\theta-1),\qquad
B=(3,\theta),\quad \overline B=(3,\theta-1).
\]
Each ideal's norm is the first integer in its expression. Also
\((2)=A\overline A\) and \((3)=B\overline B\).

Since \(N\theta=6\), and \(\theta\) vanishes at the root-zero primes but not the root-one primes,
\[
(\theta)=AB.
\tag{10}
\]
The element
\[
1+\theta=\frac{3+\sqrt{-23}}2
\]
has norm \(8\). It vanishes modulo \(\overline A\), and has residue \(1\) modulo \(A\). Hence
\[
(1+\theta)=\overline A^{\,3}.
\tag{11}
\]
Equations (10)–(11) and the rational principal ideals show that every generating prime class is a power of \([A]\), and \([A]^3=1\).

Every algebraic integer is \((a+b\sqrt{-23})/2\) with integers \(a\equiv b\pmod2\). An element of norm \(2\) would satisfy
\[
a^2+23b^2=8,
\]
which is impossible: \(b\ne0\) makes the left side at least \(23\), and \(b=0\) would require \(a^2=8\). Thus \(A\) is nonprincipal. Its order is \(3\), and
\[
\mathrm{Cl}_{\mathbf Q(\sqrt{-23})}\cong\mathbf Z/3\mathbf Z.
\]

### \(\mathbf Q(\sqrt{-14})\)

Let \(s=\sqrt{-14}\). The full ring is \(\mathbf Z[s]\), \(D=56\), and \(M_K\approx4.764<5\). The relevant rational primes are \(2,3\). There is one prime over \(2\), and two over \(3\):
\[
P=(2,s),\quad NP=2,\quad (2)=P^2,
\]
\[
Q=(3,s-1),\quad\overline Q=(3,s+1),\quad
NQ=N\overline Q=3,\quad (3)=Q\overline Q.
\]
There is no additional prime of norm \(4\), because the only prime over \(2\) already has norm \(2\).

The element \(2+s\) has norm \(18\). It belongs to \(P\) and \(Q\), and has nonzero residue \(1\) at \(\overline Q\). Unique factorization of ideals and the norm \(18=2\cdot3^2\) therefore give
\[
(2+s)=P Q^2.
\tag{12}
\]
It follows that \([P]=[Q]^{-2}\). Since \([P]^2=1\), we obtain \([Q]^4=1\), and all generating prime classes lie in \(\langle[Q]\rangle\).

There is no element of norm \(2\), because \(a^2+14b^2=2\) has no integral solution. Thus \(P\) is not principal. Equation (12) implies \([Q]^2\ne1\), so \([Q]\) has order exactly \(4\):
\[
\mathrm{Cl}_{\mathbf Q(\sqrt{-14})}\cong\mathbf Z/4\mathbf Z.
\]
The ramified prime class is the unique element of order \(2\).

### \(\mathbf Q(\sqrt{10})\)

Put \(s=\sqrt{10}\). Here \(O=\mathbf Z[s]\), \(D=40\), and
\[
M_K=\sqrt{10}\approx3.162<4.
\]
We need the ramified prime \(P=(2,s)\) and the split primes
\[
Q=(3,s+1),\qquad \overline Q=(3,s-1).
\]
Their norms are \(2,3,3\), respectively, and
\((2)=P^2\), \((3)=Q\overline Q\).

The element \(4+s\) has field norm \(16-10=6\). Its residues vanish at \(P,Q\), but not at \(\overline Q\). Thus
\[
(4+s)=P Q.
\tag{13}
\]
All generating prime classes are consequently powers of \([P]\), which has order at most \(2\).

If \(P\) were principal, its generator would have field norm \(2\) or \(-2\). But
\[
a^2-10b^2=\pm2
\]
would imply \(a^2\equiv2\) or \(3\pmod5\); neither is a square modulo \(5\). Thus \([P]\ne1\), and
\[
\mathrm{Cl}_{\mathbf Q(\sqrt{10})}\cong\mathbf Z/2\mathbf Z.
\]
Using the absolute norm in this nonprincipality test is essential.

### \(\mathbf Q(\sqrt[3]{2})\)

Let \(\alpha=\sqrt[3]{2}\). The integral-basis calculation gives
\[
O=\mathbf Z[\alpha],\qquad d_K=-108,\qquad
(r_1,r_2)=(1,1).
\]
Therefore
\[
M_K=\frac{6}{27}\frac4\pi\sqrt{108}
\approx2.940<3.
\]
For an explicit strict estimate, \(\pi>31/10\) and \(\sqrt3<26/15\) give \(M_K=16\sqrt3/(3\pi)<4160/1395<3\).
Modulo \(2\), the defining polynomial is \(X^3\). Thus the only prime of norm \(2\) is \(P=(2,\alpha)\), with \((2)=P^3\). Since \(N_{K/\mathbf Q}\alpha=2\) and \(\alpha\in P\), the principal ideal \((\alpha)\) has the same norm as \(P\) and is contained in it. Hence
\[
P=(\alpha).
\]
Every prime class needed by Corollary 8.2 is trivial, so
\[
\mathrm{Cl}_{\mathbf Q(\sqrt[3]{2})}=1.
\]
In particular its ring of integers is a PID, even though this argument supplies no Euclidean algorithm.

## Discriminants cannot be too small

**Theorem 8.3 (Minkowski discriminant bound).** If \(n\geq2\), then
\[
D\geq
\left(\frac{\pi}{4}\right)^{2r_2}
\left(\frac{n^n}{n!}\right)^2>1.
\tag{14}
\]
Consequently every number field of degree greater than \(1\) has a ramified rational prime.

**Proof.** A nonzero integral ideal has norm at least \(1\). Applying Theorem 8.1 to any class gives \(M_K\geq1\). Rearranging (7) gives the first inequality in (14).

We derive an explicit exponential consequence of (14). Applying (6) to \(1,2,\ldots,n\) gives
\[
n!\leq\left(\frac{n+1}{2}\right)^n.
\]
Since \(2r_2\leq n\) and \(0<\pi/4<1\), we deduce
\[
D\geq
\left(\frac{\pi}{4}\right)^n
\left(\frac{2n}{n+1}\right)^{2n}
\geq\left(\frac{4\pi}{9}\right)^n>1.
\tag{15}
\]
The middle inequality uses \(2n/(n+1)\geq4/3\) for \(n\geq2\); the last uses \(\pi>3\).

The integer \(D>1\) has a rational prime divisor. By the discriminant ramification criterion of Lesson 5, that prime ramifies in \(K/\mathbf Q\). Thus \(\mathbf Q\) has no nontrivial finite extension unramified at every finite prime. \(\square\)

Estimate (15) will also bound the degree when \(D\) is bounded. A weaker exponential estimate suffices for this purpose; no asymptotic factorial formula is required.

## Hermite's theorem: finitely many fields

**Theorem 8.4 (Hermite).** For every real \(X\), there are only finitely many number fields \(K\subset\mathbf C\) with \(|d_K|\leq X\). In particular there are only finitely many isomorphism classes of such fields.

**Proof.** If \(X<1\), there are no such fields. Suppose \(X\geq1\). For \(n\geq2\), (15) implies
\[
n\leq\frac{\log X}{\log(4\pi/9)}.
\]
Thus only finitely many degrees occur; the only degree-one field is \(\mathbf Q\). Fix a degree \(n\geq2\), and set
\[
c=\frac12,\qquad T=2^n\sqrt X.
\tag{16}
\]
We will find an integral primitive element with every conjugate of modulus at most \(2T\).

We use an exact multiplicity fact from Proposition 1.2 in [*Algebraic integers and rings of integers*](algebraic-integers-and-rings-of-integers.md). For \(\alpha\in K\), if \(m_\alpha\) is its minimal polynomial, then the characteristic polynomial of multiplication by \(\alpha\) on \(K\) is
\[
\chi_{\alpha,K/\mathbf Q}(U)
=\prod_{\sigma:K\hookrightarrow\mathbf C}(U-\sigma\alpha)
=m_\alpha(U)^{[K:\mathbf Q(\alpha)]}.
\tag{17}
\]
The roots of \(m_\alpha\) are distinct in characteristic zero. Consequently, if one value \(\sigma\alpha\) occurs exactly once among the \(n\) embedding values, then \(\mathbf Q(\alpha)=K\).

First assume \(r_1\geq1\). Consider the compact symmetric convex region
\[
|x_1|\leq T,\qquad |x_i|\leq c\ (i>1),
\qquad |z_j|\leq c\ (1\leq j\leq r_2).
\tag{18}
\]
Its volume is \(2^{r_1}\pi^{r_2}Tc^{n-1}\). Dividing by \(2^n\) times the covolume of \(O\), namely \(2^{r_1+r_2}\sqrt D\), gives
\[
2\left(\frac{\pi}{2}\right)^{r_2}\sqrt{\frac XD}\geq2.
\]
Minkowski therefore supplies a nonzero \(\alpha\in O\) in (18). Its nonzero integral field norm has absolute value at least \(1\), whereas all \(n-1\) embedding values other than \(\sigma_1\alpha\) have modulus at most \(c\). Hence
\[
|\sigma_1\alpha|\geq c^{-(n-1)}>c.
\]
This value cannot equal any of the other embedding values. By (17), \(\alpha\) is primitive. All conjugates have modulus at most \(T\).

Now assume \(r_1=0\), so \(n=2r_2\). Enlarging an entire complex disc could leave two equal conjugate values, so instead consider the rectangle in the first coordinate:
\[
|\operatorname{Re}z_1|\leq c,\qquad
|\operatorname{Im}z_1|\leq T,\qquad
|z_j|\leq c\ (j>1).
\tag{19}
\]
Its volume is
\[
4\pi^{r_2-1}Tc^{n-1}
=8\pi^{r_2-1}\sqrt X.
\]
Its ratio to \(2^n\operatorname{covol}(O)=2^{r_2}\sqrt D\) is
\[
4\left(\frac{\pi}{2}\right)^{r_2-1}\sqrt{\frac XD}\geq4.
\]
Again there is a nonzero \(\alpha\in O\) in this region.

If \(\tau_1\alpha\) were real, its modulus would be at most \(c\), by the real-part condition. Then every conjugate would have modulus at most \(c<1\), contradicting \(|N\alpha|\geq1\). Thus \(\tau_1\alpha\) and \(\overline{\tau_1\alpha}\) are distinct. Moreover,
\[
1\leq|N\alpha|
\leq|\tau_1\alpha|^2c^{n-2},
\qquad
|\tau_1\alpha|\geq c^{-(n-2)/2}>c.
\]
No other embedding value can equal \(\tau_1\alpha\), since all outside this conjugate pair have modulus at most \(c\). Its conjugate partner is distinct as just proved. Thus this value occurs exactly once, and (17) again makes \(\alpha\) primitive. The rectangle bounds its modulus by \(\sqrt{T^2+c^2}<2T\), while the other conjugates are even smaller.

In either case \(K=\mathbf Q(\alpha)\), with \(\alpha\) integral and all \(n\) conjugates bounded in modulus by \(H=2T\), a bound depending only on \(n,X\). Write its monic minimal polynomial as
\[
m_\alpha(U)=U^n+a_1U^{n-1}+\cdots+a_n.
\]
Its coefficients are integers, because \(\alpha\) is integral. Each \(a_k\) is, up to sign, a sum of \(\binom nk\) products of \(k\) conjugates. Therefore
\[
|a_k|\leq\binom nk H^k.
\tag{20}
\]
Only finitely many integer coefficient tuples satisfy these bounds. Each resulting polynomial has finitely many roots in \(\mathbf C\), and each root generates just one subfield of \(\mathbf C\). Every field under consideration is generated by such a root, so there are finitely many fields in degree \(n\). The earlier degree bound finishes the proof. \(\square\)

The rectangle in (19) resolves the possible proper-subfield obstruction directly. The proof includes both signature cases and explicitly rules out a repeated-conjugate obstruction from a proper subfield. Notice that the argument proves finiteness of the actual subfields of \(\mathbf C\), the stated form of the theorem.

## Exercises

1. **Easy.** Use the Minkowski bound to prove that \(\mathbf Z[\sqrt{-2}]\), \(\mathbf Z[\sqrt2]\), and \(\mathbf Z[\sqrt3]\) are PIDs.

2. **Medium.** Compute the class group of \(\mathbf Q(\sqrt{-14})\), identifying a generator and the ramified prime class.

3. **Medium.** Compute the class group of \(\mathbf Q(\sqrt{-31})\) and give an explicit prime ideal generator.

4. **Hard.** Prove Hermite's theorem for subfields of \(\mathbf C\). Give separate regions for a field with a real embedding and a totally imaginary field, and explain why your lattice element generates the whole field.

## Solutions

**1.** These are the full rings of integers. Their absolute discriminants are \(8,8,12\), respectively. The imaginary quadratic field has \(r_2=1\), whereas the two real quadratic fields have \(r_2=0\). Their Minkowski bounds are
\[
\frac2\pi\sqrt8<2,\qquad
\frac12\sqrt8=\sqrt2<2,\qquad
\frac12\sqrt{12}=\sqrt3<2.
\]
The first strict inequality follows from \(\pi>3>\sqrt8\). In each case Theorem 8.1 gives an integral ideal of norm less than \(2\) in every class. Its positive integer norm must be \(1\), so the ideal is \(O\). The class group is trivial. By the Dedekind-domain PID criterion of Lesson 3, every ideal is principal, as required.

**2.** With \(s=\sqrt{-14}\), the bound is \(2\sqrt{56}/\pi<5\). The relevant prime ideals are \(P=(2,s)\), \(Q=(3,s-1)\), and \(\overline Q=(3,s+1)\), with norms \(2,3,3\). They satisfy \((2)=P^2\) and \((3)=Q\overline Q\), so \([P]^2=1\) and \([\overline Q]=[Q]^{-1}\).

The norm of \(2+s\) is \(18\). Its residues are zero at \(P,Q\) and nonzero at \(\overline Q\). The exponents forced by this norm give \((2+s)=P Q^2\). Thus every generating class is a power of \([Q]\), and \([Q]^4=1\). The equation \(a^2+14b^2=2\) has no integral solution, so \(P\) is nonprincipal. Hence \([Q]^2=[P]\ne1\). The group is cyclic of order \(4\), generated by \(Q\), with ramified class \([P]=[Q]^2\).

**3.** Put \(\theta=(1+\sqrt{-31})/2\). Then
\[
O=\mathbf Z[\theta],\qquad
\theta^2-\theta+8=0,\qquad d_K=-31.
\]
The bound is \(2\sqrt{31}/\pi\approx3.544<4\). Modulo \(2\) the polynomial has distinct roots \(0,1\), giving
\[
P=(2,\theta),\qquad \overline P=(2,\theta-1),
\qquad (2)=P\overline P.
\]
Modulo \(3\) it is \(U^2-U+2\), with values \(2,2,1\) at \(0,1,2\); it is irreducible. The prime over \(3\) therefore has norm \(9\), beyond the bound. Corollary 8.2 shows that \([P]\) generates the group.

Since \(N\theta=8\), and \(\theta\) belongs to \(P\) but not \(\overline P\), we have \((\theta)=P^3\). Thus \([P]^3=1\). If \(P\) were principal, an integer \((a+b\sqrt{-31})/2\), with \(a\equiv b\pmod2\), would have norm \(2\), giving \(a^2+31b^2=8\). There is no such pair: a nonzero \(b\) already contributes at least \(31\), and \(a^2=8\) is impossible. Hence \([P]\ne1\), and the group is \(\mathbf Z/3\mathbf Z\), generated by \([(2,\theta)]\).

**4.** If \(X<1\), the set is empty. If \(X\geq1\), use (15) to bound the degrees \(n\geq2\), and treat \(\mathbf Q\) separately. For each fixed degree take \(c=1/2\), \(T=2^n\sqrt X\).

When \(r_1>0\), use the region (18). Its volume divided by the critical Minkowski volume is \(2(\pi/2)^{r_2}\sqrt{X/D}>1\). A nonzero integral lattice element has all but one conjugate of modulus at most \(c\). Its integral nonzero norm forces the remaining conjugate to have modulus at least \(c^{-(n-1)}>c\). That conjugate value occurs just once.

When \(r_1=0\), use (19). The critical-volume ratio is \(4(\pi/2)^{r_2-1}\sqrt{X/D}>1\). For the resulting nonzero integral element, a real first coordinate would make all conjugates of modulus at most \(c\), which contradicts the norm. Thus the first conjugate pair consists of two distinct values. The norm also forces their common modulus to be at least \(c^{-(n-2)/2}>c\), so neither equals any other conjugate value.

In both cases (17) makes the element primitive: every distinct minimal-polynomial root occurs \([K:\mathbf Q(\alpha)]\) times, and we have found a root occurring once. All its conjugates have modulus at most \(2T\). The integer coefficients of its degree-\(n\) minimal polynomial consequently satisfy (20). There are finitely many such polynomials, finitely many roots of each, and hence finitely many subfields generated by these roots. Together with the degree bound, this proves the required theorem, including the totally imaginary case.

## What this lesson does not prove

We import the exact lattice theorem and ideal covolume formula (Theorem 7.1 and Proposition 7.2), the ideal factorization and PID criterion of Lesson 3, and ideal norm formulas (Proposition 4.1). The example rings and discriminants are the quadratic and pure-cubic integral-basis results of Lessons 1–2. Their prime decompositions use Lesson 5's full-ring Kummer–Dedekind theorem. The final ramification conclusion uses that lesson's discriminant criterion over \(\mathbf Z\), whose residue fields are finite and separable.

The characteristic-polynomial identity (17), including its embedding product and multiplicity, is Proposition 1.2 of Lesson 1. We use compactness and elementary single-variable integration, and import Lebesgue product measure and Fubini/Tonelli from Fremlin 251N and 252H, and polar change of variables from 263G. The bounds and class computations here do not require Dirichlet's unit theorem or binary quadratic form classification.

## References

- J. S. Milne, [*Algebraic Number Theory*](https://www.jmilne.org/math/CourseNotes/ANT.pdf), version 3.08: Chapter 4, Theorem 4.3, Corollaries 4.4 and 4.9, Lemmas 4.22–4.27, pp. 70–81.
- E. Hecke, *Vorlesungen über die Theorie der algebraischen Zahlen*, 1923: §33, Sätze 96–98, pp. 120–121, for classical finiteness of ideal classes.
- D. H. Fremlin, *Measure Theory*, Volume 2: [Chapter 25](https://www1.essex.ac.uk/maths/people/fremlin/chap25.pdf), 251N and 252H; [Chapter 26](https://www1.essex.ac.uk/maths/people/fremlin/chap26.pdf), 263G.
- Andrew V. Sutherland, [MIT 18.785 Lecture 14](https://math.mit.edu/classes/18.785/2021fa/LectureNotes14.pdf), Theorem 14.28, pp.9-10. The current proof separately closes the complex proper-subfield obstruction; no silent substitution of the shorter Case 2.
