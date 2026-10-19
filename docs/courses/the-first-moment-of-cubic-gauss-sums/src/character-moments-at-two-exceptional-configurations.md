# Character moments at two exceptional configurations

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

In the dispersion argument of the next lesson, after Poisson summation, one has to bound sums of squares
\[
\sum_{p,q}\Bigl|\sum_b\beta(b)\,\chi_b(pq^2)\Bigr|^2
\]
over coprime squarefree \(p,q\) of lengths \(P,Q\), with a coefficient \(\beta\) of length \(Y\). The cubic large sieve and the ordinary character large sieve both give \(Y^{7/3}\) at two configurations, \((P,Q)=(Y,1)\) and \(P=Q=Y^{1/3}\), and this bound is too weak by a power. This lesson shows that a fixed power can be saved near both configurations when \(\beta\) is a convolution of a bounded number of smoothly weighted prime sequences. The decomposition of the prime sum in a later lesson produces coefficients of exactly this kind.

The proof argues by contradiction with limiting exponents. A Heath-Brown type identity writes the prime sequences through truncated Möbius functions and full smooth sums. A full factor of maximal length is dualized by the functional equation. Otherwise the large values of the factors are compared at several lengths. One configuration is ruled out at once. In the other, the values are forced into a rigid pattern, which a Gram matrix estimate for the characters \(\chi_p\) contradicts.

**Prerequisites.** The lessons [*Large sieves for cubic characters*](large-sieves-for-cubic-characters.md) and [*The level formula and Type I sums*](the-level-formula-and-type-i-sums.md). From *The Riemann zeta function*: [*The Gamma function and Stirling's formula*](course:NT-ZETA/NT-ZETA-03), Theorem 3.1.

## 1. Admissible prime convolutions

Fix \(c>0\), an integer \(k_0\ge1\), an integer \(\ell\), and bounds for supports and derivatives. An *admissible prime convolution* at length \(Y\) is a function of the form
\[
\begin{aligned}
&\beta(b)=\Theta_\ell(b)\,\mu^2(b)\\
&\quad\cdot\sum_{b=\pi_1\cdots\pi_k}\ \prod_{j=1}^kw_j\Bigl(\frac{N(\pi_j)}{F_j}\Bigr),\\
&\quad 1\le k\le k_0,
\end{aligned}
\]
with \(\prod_jF_j\asymp Y\). Here the sum runs over ordered tuples of primary primes, every prime in the support has norm at least \(Y^c\), and \(\Theta_\ell\) is the angular character of Lemma 6.1 of the lesson on large sieves. The weights \(w_j\) are supported in fixed compact subintervals of \((0,\infty)\), and their derivatives of each fixed order are bounded by a fixed power of \(\log Y\). There is no condition coupling the prime factors, such as a sharp cutoff on their product. These coefficients are divisor-bounded.

For coprime primary squarefree \(p,q\), the character \(b\mapsto\chi_b(pq^2)=\chi_p(b)\overline{\chi_q(b)}\) has conductor \(pq\).

- At \((P,Q)=(Y,1)\), Theorem 4.1 of the lesson on large sieves gives the second moment \(Y(Y+Y+Y^{4/3})\asymp Y^{7/3}\), up to a small power.
- At \(P=Q=Y^{1/3}\), the conductors have norm \(O(Y^{2/3})\), and Lemma 3.3 there gives \(Y(Y+Y^{4/3})\asymp Y^{7/3}\).

**Proposition 1.1 (the exceptional character moments).** There are \(\delta,\eta>0\), depending only on the fixed data, with the following property. Let \(v,e\in\mathcal O\setminus\{0\}\) with \(N(v),N(e)\le Y^\delta\), let \(1+|u|\le Y^{0.36}\), and put
\[
A(p,q)=\sum_{(b,e)=1}\beta(b)\,N(b)^{iu}\,\chi_b(vpq^2).
\]
Let \(p,q\) run over coprime primary squarefree elements of lengths \(P,Q\ge1\), where either
\[
\Bigl|\frac{\log P}{\log Y}-1\Bigr|\le\delta\ \text{ and }\ 0\le\frac{\log Q}{\log Y}\le\delta,
\]
or
\[
\begin{gathered}
\Bigl|\frac{\log P}{\log Y}-\frac13\Bigr|\le\delta\ \text{ and }\\
\Bigl|\frac{\log Q}{\log Y}-\frac13\Bigr|\le\delta .
\end{gathered}
\]
Then
\[
\sum_{p,q}|A(p,q)|^2\ll Y^{7/3-\eta},
\]
uniformly over the admissible prime convolutions with the given fixed data.

## 2. Two analytic lemmas

A *full smooth sum* is a sum \(\sum_{\mathfrak n}\Psi(\mathfrak n)N(\mathfrak n)^{it}W(N(\mathfrak n)/Z)\) over all nonzero ideals, against a primitive Hecke character \(\Psi\).

**Lemma 2.1 (a full smooth sum and its dual).** Let \(\Psi\) be a primitive nonprincipal Hecke character of angular order \(\ell\) and conductor norm \(D\), and let \(W\) be supported in a fixed compact subinterval of \((0,\infty)\), with derivatives of each fixed order bounded by a fixed power of \(\log Y\). Let \(Z\), \(D\) and \(|t|\) be at most fixed powers of \(Y\), and \(\epsilon,A>0\). Then the full smooth sum equals, up to \(O(Y^{-A})\),
\[
\begin{aligned}
&\sum_J\frac1{2\pi}\int_{\mathbb R}\mathcal MW(\tfrac12+i\tau)\,Z^{1/2+i\tau}\\
&\quad\cdot u_\Psi(\tau,t)\sum_{\mathfrak n}\frac{\overline{\Psi(\mathfrak n)}\,N(\mathfrak n)^{i(\tau-t)}}{N(\mathfrak n)^{1/2}}\\
&\quad\cdot\phi\Bigl(\frac{N(\mathfrak n)}J\Bigr)d\tau .
\end{aligned}
\]
Here \(J\) runs over the dyadic numbers with \(J\le Y^\epsilon D(1+|t|)^2/Z\), \(\phi\) is a fixed smooth dyadic partition function, and \(|u_\Psi(\tau,t)|=1\). The factor \(u_\Psi\) depends on \(\Psi\) only through its root number, conductor and angular order, and is a scalar for each character.

**Proof.** Put \(k=|\ell|/2\) and \(C_D=\sqrt{3D}/(2\pi)\). By Lemma 1.2 of the lesson on large sieves, the sum is
\[
\frac1{2\pi i}\int_{(2)}\mathcal MW(s)\,Z^s\,L(s-it,\Psi)\,ds .
\]
The function \(L(s,\Psi)\) is entire by Proposition 6.2 of that lesson, and its functional equation reads
\[
\begin{aligned}
L(s,\Psi)&=\varepsilon_\Psi\,C_D^{1-2s}\,\frac{\Gamma(1-s+k)}{\Gamma(s+k)}\\
&\qquad\cdot L(1-s,\overline\Psi).
\end{aligned}
\]
Move the line to \(\operatorname{Re}s=-B\). There the dual series converges absolutely, and we insert the partition \(\sum_J\phi(N(\mathfrak n)/J)=1\). By Stirling's formula the gamma quotient has size \((1+|\operatorname{Im}s-t|)^{1+2B}\). With the rapid decay of \(\mathcal MW\), the dyad \(J\) contributes
\[
\begin{aligned}
&\ll D^{1/2}(1+|t|)\Bigl(\frac{D(1+|t|)^2}{ZJ}\Bigr)^{B}\\
&\qquad\cdot(\log Y)^{O(B)} .
\end{aligned}
\]
For \(J>Y^\epsilon D(1+|t|)^2/Z\) and \(B\) large in terms of \(\epsilon,A\), the total of these dyads is \(O(Y^{-A})\). This truncation is made before any further step, with the same cutoff for every character that later shares the same \(D\) bound.

Each retained dyad is a finite Dirichlet polynomial, so its integrand is entire, and the line can be moved back to \(\operatorname{Re}s=\frac12\). No pole is crossed: the poles of \(\Gamma(1-s+it+k)\) have real part \(1+k\). With \(s=\frac12+i\tau\), the factor in front of the dual polynomial is
\[
\begin{aligned}
u_\Psi(\tau,t)&=\varepsilon_\Psi\,C_D^{2i(t-\tau)}\\
&\qquad\cdot\frac{\Gamma(\frac12+k-i(\tau-t))}{\Gamma(\frac12+k+i(\tau-t))},
\end{aligned}
\]
which has absolute value one, and the polynomial is \(\sum\overline{\Psi(\mathfrak n)}N(\mathfrak n)^{-1/2+i(\tau-t)}\phi(N(\mathfrak n)/J)\). \(\square\)

So a full smooth sum of length \(Z\) is, after an integral over \(\tau\) against the common majorant \(|\mathcal MW(\frac12+i\tau)|\), a combination of \(O(\log Y)\) polynomials of lengths \(J\le Y^\epsilon D(1+|t|)^2/Z\) in \(\overline\Psi\), with amplitude \(\sqrt{Z/J}\) after the factor \(N(\mathfrak n)^{-1/2}\asymp J^{-1/2}\) is extracted. In an average over a family of characters, the conductor-dependent factors stay outside the polynomials. Minkowski's inequality therefore applies with the same shifts \(\tau\) for every character.

**Lemma 2.2 (an off-diagonal Gram estimate).** Let \(p\) be primary and squarefree with \(N(p)\asymp P\), and let \(W\) be a fixed smooth function with compact support in \((0,\infty)\). For primary squarefree \(p'\) of the same length put
\[
T_{p,p'}=\sum_nW\Bigl(\frac{N(n)}Z\Bigr)\chi_p(n)\overline{\chi_{p'}(n)},
\]
the sum over primary \(n\). For \(Z\ge1\) and \(\epsilon>0\),
\[
\begin{aligned}
&\sum_{p'\ne p}|T_{p,p'}|^2\\
&\qquad\ll_\epsilon(PZ)^\epsilon\,Z\Bigl(P+\Bigl(\frac{P^3}Z\Bigr)^{2/3}\Bigr).
\end{aligned}
\]
The same bound holds for any subset of the \(p'\).

**Proof.** Fix \(k=(p,p')\), put \(K=N(k)\), and write \(p=ka\), \(p'=kb\), with \(a,b\) coprime and squarefree. Then \(\chi_p(n)\overline{\chi_{p'}(n)}=\mathbf 1_{(n,k)=1}\psi(n)\) with \(\psi=\chi_a\overline{\chi_b}\). This character is primitive modulo \(ab\), and nonprincipal because \(p'\ne p\). Remove the condition \((n,k)=1\) by \(\sum_{m\mid(n,k)}\mu(m)\), put \(M=N(m)\) and \(n=mx\). The factor \(\psi(m)\) has absolute value one.

Split \(x\) into its classes modulo \(ab\) and apply Lemma 2.1 of the lesson on large sieves to the classes \(x\equiv x_0\pmod{3ab}\) of primary elements. The transform of \(z\mapsto W(M|z|^2/Z)\) at \(\eta\) is \((Z/M)\widehat{W_0}(\eta\sqrt{Z/M})\), where \(W_0(z)=W(|z|^2)\) is a fixed radial Schwartz function. The frequency zero vanishes, since \(\sum_\beta\psi(\beta)=0\). At a frequency \(h\), the sum over the classes \(\beta\) modulo \(ab\) is a complete Gauss sum. Writing the primary classes as \(x=ab+3s\), with \(s\) modulo \(ab\), Lemma 3.2 of the same lesson evaluates it as
\[
\begin{aligned}
&e\Bigl(\operatorname{Tr}\frac h{3\lambda}\Bigr)\psi(3\lambda)\,\overline{\psi(h)}\,g(\psi)\\
&\qquad=e\Bigl(\operatorname{Tr}\frac h{3\lambda}\Bigr)\overline{\psi(h)}\,g(\psi),
\end{aligned}
\]
since \(3\lambda=(-\lambda)^3\) is a cube. Thus the amplitude is
\[
\begin{gathered}
\frac{Z\,|g(\psi)|}{M\,N(ab)}=\frac{Z}{M\sqrt{N(ab)}}\asymp\frac{ZK}{MP},\\
\text{and}\quad J_0=\frac{N(ab)M}Z\asymp\frac{P^2M}{K^2Z}
\end{gathered}
\]
is the natural dual length, beyond which \(\widehat{W_0}\) decays rapidly. The complete Gauss sums and the factors from the Chinese remainder theorem do not depend on the frequency, so they are scalars for each \(b\). The frequency character is \(\overline{\chi_a(h)}\chi_b(h)\), and the transform depends on \(b\) only through \(N(b)\).

On a dyad \(N(h)\asymp J\), Mellin separation in the variables \(N(h)/J\) and \(N(b)/(P/K)\) gives coefficients independent of \(b\), integrated against a rapidly decreasing common majorant whose mass is \(O_A((1+J/J_0)^{-A})\) for every \(A\). The unit and the exact power of \(\lambda\) in \(h\) are separated first. Their character values are scalars for each \(b\), and there are \(O(\log Z)\) cases. Lemma 4.2(a) of the lesson on large sieves, with unrestricted inner variable \(h\) and squarefree outer variable \(b\), bounds the square sum over \(b\) of this dyad by
\[
\begin{aligned}
&(PZ)^\epsilon\Bigl(\frac{ZK}{MP}\Bigr)^2J\\
&\quad\cdot\Bigl(\frac PK+J+\Bigl(\frac{PJ}K\Bigr)^{2/3}\Bigr)\\
&\quad\cdot\Bigl(1+\frac J{J_0}\Bigr)^{-A}.
\end{aligned}
\]
Summing over the dyads, the three powers \(J,J^2,J^{5/3}\) are bounded by the same powers of \(J_0\), also when \(J_0<1\). Substituting \(J_0\) gives the three terms
\[
\frac{ZP}{MK},\qquad\frac{P^2}{K^2},\qquad\frac{P^2Z^{1/3}}{K^2M^{1/3}} .
\]
Since \(Z,K,M\ge1\), their sum is \(O(ZP+P^2Z^{1/3})\)\(=O(Z(P+(P^3/Z)^{2/3}))\). There are only a divisor-bounded number of choices of \(k\mid p\) and \(m\mid k\), and Cauchy's inequality over them finishes the proof. \(\square\)

## 3. Proof of Proposition 1.1

We argue by contradiction. Suppose that along a sequence \(Y\to\infty\) the norms of \(v\) and \(e\) are \(Y^{o(1)}\), the pair of exponents \((\log P/\log Y,\log Q/\log Y)\) tends to \((1,0)\) or to \((\frac13,\frac13)\), and the moment is at least \(Y^{7/3-o(1)}\). The last step derives the proposition, with uniform \(\delta,\eta\), from the contradiction. A *subpower loss* means a loss of \(Y^{\epsilon}\) with an arbitrarily small fixed \(\epsilon>0\); it is never used as a logarithmic saving.

**Step 1: prime powers and repeated factors.** Remove the squarefree restriction in the definition of \(\beta\), and replace each prime weight \(w_j(N(\pi)/F_j)\) by the smooth weight \(w_j(N(\mathfrak n)/F_j)\Lambda(\mathfrak n)/\log N(\mathfrak n)\) on prime powers. The discrepancy has divisor-bounded coefficients supported on a set of size \(O(Y^{1-\theta})\) for a fixed \(\theta>0\). Indeed, each term of the discrepancy contains a repeated prime of norm at least \(Y^c\), or a prime power \(\pi^j\) with \(j\ge2\) and norm at least \(Y^c\). In both cases \(b\) is divisible by the square of an element of norm at least \(Y^{c/4}\), and summing \(O(Y/N(d)^2)\) over such square divisors \(d^2\) gives \(O(Y^{1-c/4})\). In the factorization \(b=st^2d^3\) with \(s,t\) coprime squarefree, this also gives \(N(s)\le Y^{1-\theta'}\) for a fixed \(\theta'>0\).

In the first configuration fix \(q\), at a subpower cost, and write \(\chi_b(vpq^2)=\chi_b(vq^2)\chi_p(b)\) with the first factor in the coefficients. With \(S,V,C\) the lengths of \(s,t,d\), we have \((VC)^2S\ll Y\) and \(S\ll Y^{1-\theta'}\). The bound (4.1) of the lesson on large sieves then gives the discrepancy moment
\[
Y^{1+o(1)}\bigl(Y+Y^{1-\theta'}+Y^{(4-2\theta')/3}\bigr),
\]
a power saving. In the second configuration, square the discrepancy polynomial. Its support has size at most \(Y^{2-2\theta}\), and its coefficients are divisor-bounded. Lemma 3.3 of the lesson on large sieves, at length \(Y^2\) and conductor norm \(Y^{2/3+o(1)}\), bounds the fourth moment by \(Y^{4-2\theta+o(1)}\). Cauchy's inequality over the \(Y^{2/3+o(1)}\) rows gives a second moment at most \(Y^{7/3-\theta+o(1)}\). The fixed factor \(\chi_b(v)\) and the exclusions are part of the coefficients. So both discrepancies may be discarded.

**Step 2: a short convolution identity.** Write \(*\) for Dirichlet convolution of functions on ideals, \(\mathbf 1\) for the constant function \(1\), and \(\mathbf 1_*\) for the identity of convolution. For a dyad of prime powers with upper endpoint \(F'\), put \(m=\mu\cdot\mathbf 1_{N\le\sqrt{F'}}\). The function \(\mathbf 1_*-m*\mathbf 1\) vanishes on ideals of norm at most \(\sqrt{F'}\), so its convolution square vanishes on ideals of norm at most \(F'\). Expanding the square, convolving with \(\Lambda\) and using \(\mathbf 1*\Lambda=\log N\) gives, on the dyad,
\[
\Lambda=(2m-m*m*\mathbf 1)*\log N.\quad(3.1)
\]
Multiplication by \(\Theta_\ell\) respects Dirichlet convolution, because \(\Theta_\ell\) is completely multiplicative on ideals prime to \(3\). So (3.1) holds with every factor twisted by \(\Theta_\ell\). Apply it to every factor, insert smooth norm dyads, and separate the product weights by Mellin inversion. The number of pieces and the \(L^1\) costs are subpower, and the Mellin shifts may be truncated at \(Y^\epsilon\) with negligible tails. By Minkowski's inequality the same shifts may be fixed across each average over characters. It follows that some product of a bounded number of divisor-bounded character polynomials still has second moment \(Y^{7/3-o(1)}\).

Pass to a subsequence on which the length exponents of these polynomials converge, say to \(a_i\ge0\) with \(\sum_ia_i=1\). The common twists and fixed characters are distributed over the polynomials. Every truncated Möbius factor has length at most \(Y^{1/2+o(1)}\). So if some \(a_i\) equals \(1\), that factor is a full smooth sum, possibly with a logarithmic weight, with twist height at most \(Y^{0.37}\).

**Step 3: a dominant full sum.** Suppose \(a_i=1\). The other factors have trivial size \(Y^{o(1)}\). The character of the full sum, \(\mathfrak n\mapsto\chi_n(vpq^2)\Theta_\ell(\mathfrak n)\), is nonprincipal. Away from the primes dividing \(3ve\), its conductor agrees with \(pq\). Let \(S\) be the set of these primes, fix the parts of \(p,q\) at \(S\), and fix the resulting local characters. There are \(Y^{o(1)}\) choices, since the product of the norms of the primes in \(S\) is \(Y^{o(1)}\). The remaining primitive character has the form \(\psi_S\,\chi_{p_0}\overline{\chi_{q_0}}\,\Theta_\ell\) up to inclusion–exclusion over the missing Euler factors at \(S\), which rescales the length by a subpower divisor. It is nonprincipal: for \(\ell\ne0\) by its infinity type, and for \(\ell=0\) because \(p_0q_0\) has norm a positive power of \(Y\).

Apply Lemma 2.1. In the second configuration the conductor is at most \(Y^{2/3+o(1)}\), the dual length is at most \(Y^{2/3+0.74-1+o(1)}\), and the trivial bound for the full sum is \(\sqrt{ZJ}\le Y^{1/3+0.37+o(1)}\). Summing the squares over the \(Y^{2/3+o(1)}\) rows gives the exponent
\[
\frac23+2\Bigl(\frac13+0.37\Bigr)=2.073\ldots<\frac73 .
\]
In the first configuration fix \(q\) and the parts at \(S\). The variable conductor \(p_0\) is squarefree of length \(Y^{1+o(1)}\), and the dual polynomial has length \(J\le Y^{0.74+o(1)}\), with coefficients of size \(J^{-1/2}\) and amplitude \(\sqrt Z\), \(Z=Y^{1+o(1)}\). Lemma 4.2(a) of the lesson on large sieves gives
\[
Y^{1+o(1)}\bigl(Y+J+(YJ)^{2/3}\bigr)\le Y^{2.16+o(1)} .
\]
Both bounds contradict the assumed moment. The averaging is legitimate because the factors \(u_\Psi\) of Lemma 2.1 stand outside the polynomials.

**Step 4: moments at several lengths.** In the remaining case every \(a_i<1\). Pigeonhole the absolute values of the individual polynomials into \(O(\log Y)\) classes. Values below a large fixed negative power of \(Y\) can be discarded using the trivial bounds for the other factors and the number of rows. Passing to a further subsequence, there is a set of \(Y^{r+o(1)}\) rows on which the \(i\)-th polynomial has absolute value \(Y^{v_i+o(1)}\), where \(v_i\le a_i\), and
\[
r\ge\frac73-2v,\quad v=\sum_iv_i .\qquad(3.2)
\]

*The second configuration.* There are at most \(Y^{2/3+o(1)}\) rows, so \(r\le\frac23\). The full product \(F\) has length \(Y^{1+o(1)}\), and its square is a divisor-bounded polynomial of length \(Y^{2+o(1)}\). Lemma 3.3 of the lesson on large sieves, applied to \(F^2\), gives \(r+4v\le4\). Together with (3.2) this forces \(v=\frac56\) and \(r=\frac23\). Since \(\sum v_i=\frac56\sum a_i\), there is an index with \(0<a_i<1\) and \(v_i\ge\frac56a_i\). Multiply \(F\) by this factor once more, and put \(z=1+a_i\in(1,2)\). The product has length \(Y^{z+o(1)}\) and, on the chosen rows, values at least \(Y^{5z/6+o(1)}\). Lemma 3.3 gives
\[
\begin{aligned}
r&\le\max\Bigl(\frac43,z\Bigr)+z-\frac{5z}3\\
&=\max\Bigl(\frac43,z\Bigr)-\frac{2z}3<\frac23,
\end{aligned}
\]
a contradiction.

*The first configuration.* Fix \(q\) at a subpower cost; (3.2) is unchanged. The rows are distinct squarefree \(p\) of length \(Y^{1+o(1)}\). Put \(d_i=v_i-\frac56a_i\). For nonnegative integers \(k_i\) with \(z=\sum_ik_ia_i\in[\frac12,2]\), the product \(\prod_if_i^{k_i}\) is a divisor-bounded polynomial of length \(Y^{z+o(1)}\). Lemma 4.2(a) of the lesson on large sieves gives
\[
r\le\frac23-2\sum_ik_id_i ,
\tag{3.3}
\]
because \(z+\max\{1,z,\frac23(1+z)\}=\frac23+\frac{5z}3\) for \(\frac12\le z\le2\).

- The vector of ones makes the right side of (3.3) equal to the lower bound in (3.2), so equality holds in (3.2) and (3.3).
- Increasing one multiplicity from \(1\) to \(2\) keeps \(z<2\), and so proves \(d_i\le0\) for every \(i\).
- Decreasing it to \(0\) keeps \(z\ge\frac12\) when \(a_i\le\frac12\), and so proves \(d_i\ge0\) for these \(i\).

So every factor with \(a_i\le\frac12\) has \(d_i=0\), including those with \(a_i=0\). At most one index has \(a_i>\frac12\). If there is one, remove it, and add copies of a positive factor with \(a\le\frac12\) until the length exponent lies in \([\frac12,2]\). Such a factor exists, since no \(a_i\) equals \(1\). Then (3.3) gives \(r\le\frac23\), and the vector of ones gives \(r=\frac23-2d_{i_0}\ge\frac23\). Hence all \(d_i=0\) and \(r=\frac23\).

Choose a positive exponent \(a\le\frac12\) among the \(a_i\). Some fixed multiple of \(a\) lies strictly between \(\frac43\) and \(2\), since that interval is longer than \(a\). Taking that many copies of the factor gives a divisor-bounded polynomial \(\sum_nc_n\chi_p(n)\) of length \(Z=Y^{z+o(1)}\), with \(\frac43<z<2\), whose absolute value is at least \(Y^{5z/6+o(1)}\) on at least \(Y^{2/3-o(1)}\) distinct squarefree rows \(p\). The multiplicity is fixed once the subsequence is chosen, even when \(a\) is small.

**Step 5: near orthogonality.** Let \(\mathcal P\) be this set of rows, with \(|\mathcal P|=R\), and let \(W\ge0\) be a smooth radial weight that is at least \(1\) on the support of \((c_n)\). In the space of functions on primary elements with the inner product \(\langle f,g\rangle=\sum_nf(n)\overline{g(n)}\), take
\[
\begin{gathered}
\xi(n)=\frac{c_n}{\sqrt{W(N(n)/Z)}},\\
\phi_p(n)=\sqrt{W(N(n)/Z)}\;\overline{\chi_p(n)},
\end{gathered}
\]
with \(\xi(n)=0\) off the support of \(c\). Then \(\langle\xi,\phi_p\rangle\) is the polynomial at \(p\), \(\langle\phi_p,\phi_{p'}\rangle=\overline{T_{p,p'}}\), and \(\|\xi\|^2\le Z^{1+o(1)}\). The Bombieri–Halász–Montgomery inequality (Lemma 5.2 of the lesson on large sieves) and Cauchy's inequality give
\[
\begin{aligned}
&R\,Y^{5z/3+o(1)}\le Z^{1+o(1)}\Bigl(O(Z)\\
&\qquad+R^{1/2}\max_p\Bigl(\sum_{p'\ne p}|T_{p,p'}|^2\Bigr)^{1/2}\Bigr).
\end{aligned}
\]
By Lemma 2.2 with \(P=Y^{1+o(1)}\), the inner sum is at most \(Y^{o(1)}Z(Y+(Y^3/Z)^{2/3})\). Divide by \(ZR\), with \(R=Y^{2/3+o(1)}\). The left side has exponent \(\frac{2z}3\). The diagonal term has exponent at most \(z-\frac23\), and the off-diagonal term has exponent at most
\[
\frac{z+\max(1,2-\frac{2z}3)-\frac23}2 .
\]
Both are strictly smaller than \(\frac{2z}3\). The gap for the diagonal is \(\frac{2-z}3\). The gap for the off-diagonal term is \(\frac{3z-4}6\) for \(z\le\frac32\) and \(\frac{z-1}6\) for \(z\ge\frac32\). These fixed gaps absorb every subpower loss, which gives the final contradiction.

**Step 6: uniform neighborhoods.** If the proposition failed for every choice of \(\delta\) and \(\eta\), choose shrinking \(\delta_n,\eta_n\to0\) and counterexamples with \(Y_n\to\infty\). This diagonal sequence has \(N(v),N(e)=Y^{o(1)}\), length exponents tending to one of the two pairs, and moments at least \(Y^{7/3-o(1)}\). There are boundedly many factors, their length exponents lie in a compact simplex, and the pigeonholing confines the value exponents to a compact interval. So Steps 1 to 5 apply to a subsequence. Every multiplicity and every small loss is fixed before the limit is taken. The contradiction proves the existence of \(\delta,\eta>0\) and the uniform bound. \(\square\)

**Remark 3.1.** The angular order \(\ell\) enters only in two places. It enters Lemma 2.1, through the factor \(\Gamma(s+|\ell|/2)\) of the functional equation and the nonprincipality of the dual character. It also enters Step 2, through the multiplicativity of \(\Theta_\ell\). In every moment estimate \(\Theta_\ell\) belongs to the coefficients common to all rows, and in the Gram matrix of Step 5 it cancels against its conjugate. The constants \(\delta,\eta\) may depend on the fixed \(\ell\).

## 4. Exercises

**4.1.** Verify the identity \(z+\max\{1,z,\frac23(1+z)\}=\frac23+\frac{5z}3\) for \(\frac12\le z\le2\), and show that it fails for \(z<\frac12\).

**4.2.** In Step 4, second configuration, derive \(v=\frac56\) and \(r=\frac23\) from \(r\le\frac23\), \(r+4v\le4\) and (3.2).

**4.3.** Check the three terms in the proof of Lemma 2.2 by substituting \(J=J_0\) into \(\bigl(\frac{ZK}{MP}\bigr)^2J\bigl(\frac PK+J+(\frac{PJ}K)^{2/3}\bigr)\).

**4.4.** Show that (3.1) holds on the dyad: for every ideal \(\mathfrak n\) with \(N(\mathfrak n)\le F'\), \(\Lambda(\mathfrak n)=((2m-m*m*\mathbf 1)*\log N)(\mathfrak n)\).

**4.5.** In Step 5, explain why the factor \(N(b)^{iu}\) in \(A(p,q)\), and more generally any factor depending only on the inner variable, causes no difficulty, whereas a factor depending on both the row and the inner variable would.

## 5. Solutions

**4.1.** For \(z\ge\frac12\), \(\frac23(1+z)\ge1\), and \(\frac23(1+z)\ge z\) holds exactly for \(z\le2\). So the maximum is \(\frac23(1+z)\), and \(z+\frac23(1+z)=\frac23+\frac{5z}3\). For \(z<\frac12\) the maximum is \(1\), and \(z+1>\frac23+\frac{5z}3\) since \(z<\frac12\).

**4.2.** From (3.2), \(\frac73-2v\le r\le\frac23\) gives \(v\ge\frac56\). From \(r+4v\le4\) and (3.2), \(\frac73+2v\le r+4v\le4\) gives \(v\le\frac56\). So \(v=\frac56\), and then \(r=\frac23\).

**4.3.** With \(J_0=P^2M/(K^2Z)\), the factor \(\bigl(\frac{ZK}{MP}\bigr)^2J_0=\frac ZM\). Multiplying it by \(\frac PK\), by \(J_0\) and by \((PJ_0/K)^{2/3}\) gives \(\frac{ZP}{MK}\), \(\frac{P^2}{K^2}\) and \(\frac ZM\bigl(\frac{P^3M}{K^3Z}\bigr)^{2/3}=\frac{P^2Z^{1/3}}{K^2M^{1/3}}\).

**4.4.** Let \(h=\mathbf 1_*-m*\mathbf 1\). For \(N(\mathfrak n)\le\sqrt{F'}\), \((m*\mathbf 1)(\mathfrak n)=\sum_{\mathfrak d\mid\mathfrak n}\mu(\mathfrak d)=\mathbf 1_*(\mathfrak n)\), so \(h(\mathfrak n)=0\). If \(N(\mathfrak n)\le F'\) and \(\mathfrak n=\mathfrak n_1\mathfrak n_2\), one of the factors has norm at most \(\sqrt{F'}\), so \((h*h)(\mathfrak n)=0\). Expanding,
\[
h*h=\mathbf 1_*-2m*\mathbf 1+m*m*\mathbf 1*\mathbf 1 .
\]
Convolving with \(\Lambda\) and using \(\mathbf 1*\Lambda=\log N\), the function \(\Lambda-2m*\log N+m*m*\mathbf 1*\log N\) vanishes for \(N(\mathfrak n)\le F'\).

**4.5.** A factor depending only on the inner variable is part of the coefficient vector \(\xi\), which is the same for all rows, so the Gram matrix of the vectors \(\phi_p\) is unchanged. A factor depending on both the row and the inner variable would change the vectors \(\phi_p\) themselves, and their inner products would not be the sums \(T_{p,p'}\) bounded in Lemma 2.2.

## Sources

- [OpenAI-023] OpenAI, *An unconditional first moment for cubic Gauss sums*, OpenAI Math Release preprint, 25 September 2026, Section 4 (the exceptional character moments) and Appendix A.3 (the angular version). https://github.com/openai/math/tree/main/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026
