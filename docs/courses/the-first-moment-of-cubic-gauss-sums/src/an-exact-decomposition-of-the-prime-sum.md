# An exact decomposition of the prime sum

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The estimates of the previous lessons apply to Type I sums with a short outer variable, and to bilinear sums whose coefficients are either general, when the shorter variable is below \(X^{0.40}\), or convolutions of smoothly weighted prime sequences, when it is above. This lesson writes the sum over primes, with a smooth envelope \(V(N(n)/X)\), as a combination of at most a power of \(\log X\) such sums. The identity is exact, and it uses the same coefficients for the Gauss sums and for the model. Two features are essential. The coefficients of the two variables in a bilinear term must be independent, without a sharp condition coupling them; this is achieved by a stopping rule in norm bins with a binomial weight. And the only configuration that escapes every power saving, a product of three primes of norm close to \(X^{1/3}\), is isolated with bounded weights, so that the sparsity of primes can be used there.

**Prerequisites.** The lessons [*Large sieves for cubic characters*](large-sieves-for-cubic-characters.md) (Theorem 4.1, Theorem 6.4 and Corollary 6.5) and [*Character moments at two exceptional configurations*](character-moments-at-two-exceptional-configurations.md) (admissible prime convolutions). From *The Riemann zeta function*: [*Counting primes by elementary means*](course:NT-ZETA/NT-ZETA-02), Theorem 3.1 (Mertens).

## 1. The statement

All factorizations are factorizations of ideals prime to \(3\), written through their primary generators; distinct prime ideals of equal norm are distinct factors. Let \(L=\log X\), and let \(V\) be a fixed smooth function with compact support in \((0,\infty)\). Fix small positive constants \(\kappa,\rho\), with \(\rho\) small in terms of \(\kappa\), and then
\[
0<\xi<\frac\kappa{10},\quad w=X^\xi,\quad z=X^{0.40}.
\]
The height blocks of the later assembly are *ordinary* when \(T\ll X^{0.01}\), including bounded heights, and *upper* when \(X^{0.01}\ll T\ll X^{1/6+\rho}\). Fix an integer \(\ell\). The two kernels are
\[
\begin{gathered}
K_1(n)=G_\ell(n)N(n)^{it},\\
K_2(n)=c_*\theta_\ell(n)\mu^2(n)N(n)^{-1/6+it},
\end{gathered}
\]
in the notation of the lesson on the level formula. Both vanish unless \(n\) is squarefree.

**Proposition 1.1 (prime decomposition).** For either kind of block, the sum \(\sum_\pi K(\pi)V(N(\pi)/X)\) has an exact decomposition into at most \(L^{O(1)}\) Type I and bilinear terms. The decomposition is valid for both kernels with the same coefficients. The coefficients do not depend on \(t\), are divisor-bounded, and have all fixed moments of the usual size \(YL^{O(1)}\) on a dyad of length \(Y\). The terms have the following properties.

1. A Type I term has an unrestricted inner variable \(u\) and an outer variable \(r\) of length \(R\), with \(R\le X^{0.40}\) on ordinary blocks and \(R\le X^{1/3-\kappa/2}\) on upper blocks. Its inner weight is a smooth envelope at length \(X/R\), with fixed derivative bounds, possibly depending on \(r\).
2. A bilinear term has independent coefficients \(\alpha_a,\beta_b\), which may be restricted separately to squarefree \(a,b\), with \(AB\asymp X\) and \(B\ll\sqrt X\). On ordinary blocks \(B\ge c_0X^{1/3}\) for a fixed \(c_0>0\); on upper blocks \(B\ge X^{1/3-3\kappa}\). Whenever \(B>X^{0.40}\), the coefficient \(\beta\) is an admissible prime convolution, with primes of norm at least a fixed power of \(X\), and with no further cutoff coupling its prime factors.
3. On ordinary blocks, apart from the sparse terms in (5), the coefficient \(\beta\) is supported on elements whose prime factors have norm greater than \(L^{C_r}\), and it has property (SW) of the lesson on corrected dispersion. Here \(C_r\) is any fixed constant, chosen later.
4. For any fixed \(C_g\), the ordinary bilinear terms with \(1\ll H=B^2/A<L^{C_g}\) are products of exactly three primes: one prime on the \(b\) side, two primes in specified dyads on the \(a\) side. All three scales are \(X^{1/3}L^{O(1)}\), the weights are bounded, and there are \(O((1+\log L)^{O(1)})\) such terms. In each,
\[
\begin{aligned}
&\sum_a|\alpha_a|^2\ll\frac A{L^2},\\
&\sum_b|\beta_b|^2+\sum_b|\beta_b|\\
&\qquad\ll\frac BL .\quad(1.1)
\end{aligned}
\]
All other nonsparse ordinary bilinear terms have \(H\ge L^{C_g}\) for large \(X\).
5. The remaining ordinary terms have \(X^{0.35}\ll B<X^{0.40}\) and sparse \(b\)-support. Their total contribution, for either kernel and uniformly in \(t\), is \(O(X^{5/6-\eta})\) for some \(\eta>0\).

The exponents in the number of terms and in the divisor bounds can be chosen independently of \(C_r\) and \(C_g\). All identities hold before either kernel is estimated.

## 2. Detecting primes

Take a fixed smooth \(\psi:(0,\infty)\to[0,1]\), equal to \(1\) on \((0,1]\) and to \(0\) on \([2,\infty)\), and put
\[
\begin{gathered}
\psi_y(\pi)=\psi\Bigl(\frac{N(\pi)}y\Bigr),\\
\mathcal F_y(n)=\prod_{\pi\mid n}\bigl(1-\psi_y(\pi)\bigr).
\end{gathered}
\]
Since both kernels vanish on nonsquarefree arguments, it suffices to have identities on squarefree \(n\).

**Lemma 2.1 (prime detection).** For squarefree \(n\) with \(V(N(n)/X)\ne0\) and \(X\) large,
\[
\mathbf 1_{\{n\text{ prime}\}}=\mathcal F_z(n)-\mathbf 1_{\{\Omega(n)=2\}}\mathcal F_z(n).
\]
Moreover
\[
\begin{aligned}
&\mathcal F_z(n)=\sum_{i\ge0}\frac1{i!}\sum_{n=\pi_1\cdots\pi_ih}\mathcal F_w(h)\\
&\quad\cdot\prod_{j=1}^i\bigl(\psi_w(\pi_j)-\psi_z(\pi_j)\bigr),\quad(2.1)
\end{aligned}
\]
where only boundedly many \(i\) contribute and the distinguished primes \(\pi_j\) have norms in \([w,2z]\).

**Proof.** If \(\mathcal F_z(n)\ne0\), every prime factor of \(n\) has norm greater than \(z=X^{0.40}\). Three such factors would give \(N(n)>X^{1.2}\), outside the support of the envelope. For a prime \(n\) in that support, \(N(n)\ge2z\) and \(\mathcal F_z(n)=1\). This proves the first identity. For (2.1), expand at every prime factor
\[
1-\psi_z=(1-\psi_w)+(\psi_w-\psi_z).
\]
The factors where the second summand is chosen form a subset; ordering it and dividing by \(i!\) gives (2.1). The difference \(\psi_w-\psi_z\) vanishes below \(w\) and above \(2z\). Since \(N(n)\ll X\) and each chosen prime has norm at least \(X^\xi\), there are at most \(O(1/\xi)\) of them, and the same bound holds for the prime factors of \(h\) when \(\mathcal F_w(h)\ne0\). \(\square\)

The two-prime correction is an ordered pair sum with the factor \(\frac12\). Smooth dyadic partitions place its two prime norms between constant multiples of \(X^{0.40}\) and \(X^{0.60}\). Taking the smaller scale for \(B\) gives a bilinear term with all the properties of part (2), with single-prime coefficients, and with \(H\) a fixed positive power of \(X\).

In (2.1), put \(r=\pi_1\cdots\pi_i\), insert smooth dyads on the distinguished primes, and let \(R\) be the product of their scales, \(R=1\) when \(i=0\). Then \(N(r)\asymp R\) with a fixed support ratio. Put
\[
\begin{gathered}
s_0=0.345\ \text{ on ordinary blocks},\\
s_0=\tfrac13-2\kappa\ \text{ on upper blocks}.
\end{gathered}
\]

## 3. Many distinguished primes: grouping

Suppose first \(R\ge X^{s_0}\). Expand \(h\) into its bounded number of prime factors, divide the ordered factorization by its factorial, and insert independent smooth dyads on all primes. All prime norms are between \(w\) and a constant times \(X^{1-s_0}\), and the distinguished ones are at most \(2z\). Configurations of scales disjoint from the envelope are discarded. No cutoff on products of the primes is inserted.

**Lemma 3.1 (a partition lemma).** Let \(x_1,\ldots,x_k>0\) with \(\sum x_i=1\) and every \(x_i<\frac23\). Unless \(k=3\) and all \(x_i=\frac13\), some subset of the \(x_i\) has sum in the open interval \((\frac13,\frac23)\).

**Proof.** Suppose no subset sum lies in \((\frac13,\frac23)\). Then every \(x_i\le\frac13\), since a single part in \((\frac13,\frac23)\) would be such a subset. If some part \(a<\frac13\), start with it and add further parts until the sum first exceeds \(\frac13\). The final sum is at most \(\frac23\), as the previous sum was at most \(\frac13\) and the last part is at most \(\frac13\). By assumption it is not in \((\frac13,\frac23)\), so it equals \(\frac23\). Then the previous sum and the last part both equal \(\frac13\), and \(a\) together with the last part has sum \(a+\frac13\in(\frac13,\frac23)\), a contradiction. So every part equals \(\frac13\). \(\square\)

**Lemma 3.2 (grouping).** The prime factors just obtained can be grouped into two scales \(A,B\) with \(AB\asymp X\) and \(B\ll\sqrt X\), as follows.

- On ordinary blocks, either \(B\ge X^{1/3+\delta_1}\) for a fixed \(\delta_1>0\), or there are exactly three prime factors with exponents close to \(\frac13\), and \(B\) is the largest of their three scales.
- On upper blocks one can always arrange \(B\ge X^{1/3-3\kappa}\).

**Proof.** Normalize the logarithms of the prime scales by the logarithm of their product. In any limit they are positive, sum to \(1\), and are bounded below in terms of \(\xi\). On ordinary blocks every part is at most \(1-0.345=0.655<\frac23\). There are finitely many possible numbers of factors. On the compact set of their exponent vectors, outside a fixed small neighborhood of \((\frac13,\frac13,\frac13)\), Lemma 3.1 and compactness give a subset whose sum keeps a uniform distance from \(\frac13\) and \(\frac23\). Group that subset and its complement, call the smaller group \(B\), and absorb the fixed support ratios into a smaller gap \(\delta_1\). In the exceptional neighborhood, take the largest scale for \(B\), with the neighborhood so small that \(B<X^{0.40}\).

On upper blocks, a part exceeding \(\frac23\) can only come from \(h\), and its complement contains \(r\), of exponent at least \(s_0\); take the complement as \(B\). If no part exceeds \(\frac23\), the successive-sum argument of Lemma 3.1 gives a subset sum in \([\frac13,\frac23]\). In both cases the fixed support ratios and limiting errors are absorbed by the spare \(\kappa\) in the bound \(B\ge X^{1/3-3\kappa}\). \(\square\)

*The three-prime configuration.* With three factors the largest scale satisfies \(B\ge c_0X^{1/3}\). If \(H=B^2/A\asymp B^3/X<L^{C_g}\), then \(B\ll X^{1/3}L^{C_g/3}\). Since the product of the three scales is \(\asymp X\) and each is at most \(B\), each is at least \(X^{1/3}\) times a fixed negative power of \(L\). So only \(O((1+\log L)^3)\) triples of dyads occur, each with bounded multiplicity from the roles in (2.1) and the orderings. The upper bound in the prime ideal theorem (Lemma 4.2 of the first lesson) gives (1.1). This proves the exceptional assertions of part (4) in this branch.

## 4. Few distinguished primes: stopping in norm bins

Suppose \(R<X^{s_0}\). Möbius expansion gives exactly
\[
\mathcal F_w(h)=\sum_{mu=h}\mu(m)\prod_{\pi\mid m}\psi_w(\pi),\quad(4.1)
\]
with the primes of \(m\) of norm at most \(2w\) and \(u\) unrestricted. Partition the possible prime norms below \(2w\) into \(O(L)\) *bins*, in descending order, each with ratio of upper to lower endpoint at most \(1+\delta_0\), where \(\delta_0>0\) is small in terms of \(\kappa\). On ordinary blocks include \(L^{C_r}\) as a bin endpoint.

For a prime in a bin with lower endpoint \(\ell_0\), its *surrogate norm* is \(\ell_0\), and the surrogate \(S(m')\) of a product is the product of the surrogate norms. Any nonzero term has \(O(L)\) prime factors, so for \(\delta_0\) small
\[
S(m')\le N(m')\le X^{\kappa/4}S(m')\quad(4.2)
\]
for every subproduct \(m'\). Start a running surrogate at the exact value \(N(r)\), and add the prime factors of \(m\) bin by bin in descending order.

- On ordinary blocks, process first the bins above \(L^{C_r}\), and stop on first reaching \(X^{0.36}\). If these bins are exhausted without a stop, process the remaining bins, stopping on first reaching \(X^{0.38}\).
- On upper blocks, process all bins with the single threshold \(X^{1/3-\kappa}\).

Since \(N(r)<X^{s_0}\), the initial value lies below every first threshold.

*No stop.* Then \(N(r)S(m)<Z\), where \(Z\) is the final threshold. All predicates involve \(r\) and \(m\) alone, so grouping by dyads of \(N(rm)\) gives Type I terms with outer variable \(rm\) and unrestricted \(u\). By (4.2), \(N(rm)<X^{\kappa/4}Z\), which is less than \(X^{0.38+\kappa/4}<X^{0.40}\) on ordinary blocks and less than \(X^{1/3-3\kappa/4}<X^{1/3-\kappa/2}\) on upper blocks. For an outer variable \(v=rm\) of length \(R'\), the inner weight is \(V(N(v)N(u)/X)\), a smooth function of \(N(u)/(X/R')\) whose derivatives are bounded uniformly in \(v\). This is part (1).

*Stopped terms.* Write \(m=m_+m_-\), where \(m_+\) consists of the factors added up to and including the stop, and put
\[
b=rm_+,\qquad a=m_-u .
\]
The crossing prime has norm at most \(2X^\xi\). So ordinary stopped terms have \(X^{0.36}\le N(b)\ll X^{0.38+\xi+\kappa/4}<X^{0.40}\), and upper stopped terms have \(X^{1/3-\kappa}\le N(b)\ll X^{1/3-\kappa+\xi+\kappa/4}<X^{0.40}\). Sharp norm dyads may be inserted on \(a\) and \(b\) separately, as no prime-convolution structure is needed in this range.

**Lemma 4.1 (exact separation at the stopping bin).** The stopped terms are exact sums with independent coefficients on \(a\) and \(b\). The number of additional outer indices is \(L^{O(1)}\), and the coefficients have fixed divisor bounds independent of \(C_r\).

**Proof.** Fix the last bin \(j\), its lower endpoint \(\ell_0\), and the numbers \(k_+\ge1\) and \(k_-\ge0\) of selected and remaining factors in this bin. All factors in earlier bins belong to \(m_+\) and all factors in later bins to \(m_-\). With \(Z\) the applicable threshold, the stopping condition is
\[
\begin{aligned}
&\frac{N(r)S(m_+)}{\ell_0}<Z\\
&\qquad\le N(r)S(m_+).\quad(4.3)
\end{aligned}
\]
For an ordinary stop below the bin endpoint \(L^{C_r}\), require in addition that \(N(r)S(m_+^>)<X^{0.36}\), where \(m_+^>\) contains the factors above \(L^{C_r}\), all of which lie in \(m_+\). Both conditions depend only on the variables on the side of \(b\).

The surrogate uses the same \(\ell_0\) for every prime of the final bin. For a fixed squarefree \(m\), exactly \(\binom{k_++k_-}{k_+}\) selections of \(k_+\) of its primes in that bin have the given counts, and either all or none satisfy (4.3). Give each selection the weight \(\binom{k_++k_-}{k_+}^{-1}\); the weights add up to the original coefficient. The Möbius factor and all prime weights factor between \(m_+\) and \(m_-\). Explicitly, let \(v(r)\) be the weight of the distinguished tuple, including \(1/i!\), and \(q(d)=\mu(d)\prod_{\pi\mid d}\psi_w(\pi)\). Let \(\mathcal C_{j,k}(r,d)\) be the crossing condition (with the failed first-stage test when needed), requiring exactly \(k\) factors of \(d\) in bin \(j\) and none in later bins. Put
\[
\begin{gathered}
\beta_{j,k}(b)=\sum_{rd=b}v(r)\,q(d)\,\mathbf 1_{\mathcal C_{j,k}(r,d)},\\
\alpha_{j,l}(a)=\sum_{eu=a}q(e)\,\mathbf 1_{\mathcal E_{j,l}(e)},
\end{gathered}
\]
where \(\mathcal E_{j,l}(e)\) says that \(e\) has factors only in the bins \(j,j+1,\ldots\), exactly \(l\) of them in bin \(j\). Then the stopped sum against any squarefree-supported kernel \(K\), including the envelope, is
\[
\begin{aligned}
&\sum_{j,\ k\ge1,\ l\ge0}\binom{k+l}k^{-1}\\
&\qquad\cdot\sum_{a,b}\alpha_{j,l}(a)\,\beta_{j,k}(b)\,K(ab).
\end{aligned}
\]
These independent sums also contain tuples in which \(r,m_+,m_-,u\) share a prime. Each such tuple has a nonsquarefree product and is annihilated by the kernel. After collecting coefficients, \(a\) and \(b\) can be restricted to be squarefree separately, and a common prime of \(a\) and \(b\) is killed by the kernel. So independence needs no coprimality condition. The bins form unordered divisors, and only the bounded distinguished tuple is ordered, so the multiplicities are bounded by fixed powers of \(\tau(a),\tau(b)\). The binomial weight is at most \(1\). There are \(O(L)\) choices of the final bin and \(O(L)\) of each count; the full occupancy of the other bins is not an outer index. \(\square\)

## 5. Sparse late stops

An ordinary stop using a prime of norm at most \(L^{C_r}\) has high-bin surrogate below \(X^{0.36}\) and final surrogate at least \(X^{0.38}\). So \(b\) has a divisor \(d\) with
\[
\begin{gathered}
N(d)\ge X^{0.02},\\
N(\pi)\le L^{C_r}\ \text{ for all }\pi\mid d .
\end{gathered}
\]
Choose a fixed \(\sigma>0\) with \(C_r\sigma<1\). Rankin's method gives
\[
\begin{aligned}
&\sum_{\substack{N(d)\ge X^{0.02}\\ \pi\mid d\Rightarrow N(\pi)\le L^{C_r}}}\frac1{N(d)}\\
&\le X^{-0.02\sigma}\\
&\quad\cdot\prod_{N(\pi)\le L^{C_r}}\bigl(1-N(\pi)^{-1+\sigma}\bigr)^{-1}\\
&\le X^{-0.02\sigma+o(1)} ,
\end{aligned}
\]
since the logarithm of the product is \(O(L^{C_r\sigma}\log L)=o(L)\) by the upper bound for prime ideals. A dyad of length \(B\) contains \(O(B/N(d))\) multiples of \(d\) when \(N(d)\ll B\), so these \(b\) number \(O(BX^{-\delta})\) for a fixed \(\delta>0\), and the fixed divisor bounds keep a smaller power saving in \(\sum_b|\beta_b|^2\).

Here \(X^{0.35}\ll B<X^{0.40}\) and \(A\asymp X/B\), so \(A+B+(AB)^{2/3}\ll X^{2/3}\). Separate the envelope by Mellin inversion, write \(G(ab)=G(a)G(b)\overline{\chi_b(a)}\), and apply Cauchy's inequality in \(a\) and Theorem 4.1 of the lesson on large sieves:
\[
\begin{aligned}
&\Bigl|\sum_{a,b}\alpha_a\beta_bG_\ell(ab)N(ab)^{it}\\
&\qquad\cdot V\Bigl(\frac{N(ab)}X\Bigr)\Bigr|\\
&\ll\Bigl(AL^{O(1)}\cdot X^{2/3+\epsilon}BX^{-\delta}\Bigr)^{1/2}\\
&\ll X^{5/6-\eta}.
\end{aligned}
\]
The model has the same saving by direct counting, since \(N(ab)^{-1/6}\asymp X^{-1/6}\), and the norm twists have absolute value one. This proves part (5), also after summing the \(L^{O(1)}\) pieces.

## 6. Coefficient moments and the condition (SW)

All coefficients satisfy fixed divisor bounds, so Lemma 1.1 of the lesson on large sieves gives the moment bounds, also after collecting equal norms. The nonsparse stopped ordinary coefficients are rough: distinguished primes have norm at least \(w\), and selected bin primes exceed \(L^{C_r}\). Pure prime-tuple coefficients are rough as well.

**Lemma 6.1 (the condition (SW)).** Every nonsparse ordinary \(b\)-coefficient, multiplied by \(\Theta_\ell\), satisfies (SW). For every nonprincipal cubic Hecke character \(\chi\) of conductor norm at most a fixed power of \(L\), the sum of \(\beta_b\Theta_\ell(b)\chi(b)N(b)^{it}\) is \(O_D(BL^{-D})\) for every \(D\). This holds for \(|t|\) at most a fixed power of \(L\), and also with coprimality to an element of norm \(X^{O(1)}\).

**Proof.** First discard the terms all of whose prime factors have norm at most \(y=\exp(\sqrt L)\). Rankin's method with \(\sigma=1/\sqrt L\), including the divisor multiplicities in the Euler product, bounds their total weight by \(B\exp(-c\sqrt L)L^C\), because \(B\) is a fixed power of \(X\) and \(\sum_{N(\pi)\le y}N(\pi)^{-1+\sigma}=O(\log L)\).

In the remaining terms select a largest prime factor, breaking ties by a fixed order. Fix its role, its dyad \(P\gg\exp(\sqrt L)\), and all other factors. There are boundedly many distinguished roles and one unordered role in the selected bins. If the variable prime lies in \(m_+\), all surrogate data are constant within its bin. If it lies in \(r\), then \(N(r)\) is a fixed multiple of its norm. So the crossing condition (4.3), the failed first-stage test, the dyad of \(b\) and the condition of being the largest prime each restrict its norm to an interval, and their intersection has polynomially many pieces as the bin varies. With the other factors fixed, the Möbius sign is constant and the remaining prime weights are smooth with bounded scaled derivatives.

The prime sum against \(\chi\Theta_\ell\) is then bounded by Corollary 6.5 of the lesson on large sieves. The character \(\chi\Theta_\ell\) is nonprincipal, by its infinity type if \(\ell\ne0\) and by assumption if \(\ell=0\). Its conductor is at most a fixed power of \(L\), which is at most a fixed power of \(\log P\), because \(\log P\ge\sqrt L\). Partial summation absorbs the smooth weights and the norm twist, and subtraction of two initial intervals handles arbitrary intervals. Ties affect only endpoint norms: there are at most two prime ideals of a given prime norm and one of a given inert norm. Coprimality to an element of polynomial norm deletes \(O(L)\) primes, negligible against \(PL^{-D}\). The complementary factorizations have total weight \((B/P)L^{O(1)}\) for fixed \(P\). Summing over them, over the roles, the dyads and the interval pieces proves the claim. \(\square\)

## 7. Completion of the proof

The identities of Lemma 2.1 and (4.1) are exact on squarefree arguments. Lemma 3.2 treats the branch \(R\ge X^{s_0}\), and Lemma 4.1 the branch \(R<X^{s_0}\). The norm ranges proved above give parts (1) and (2). Lemma 6.1 gives part (3), and the three-prime count gives part (4). Ordinary stopped terms have \(B\ge X^{0.36}\), hence \(H=B^3/X\gg X^{0.08}\), so they contribute no further small-\(H\) configuration. Section 5 gives part (5). The number of pieces is a power of \(L\): the distinguished tuple has bounded length, the bin and count indices have polynomially many values, and the dyads add polynomial factors.

The parameters are chosen in a noncircular order:

1. the absolute power-width constant \(\gamma\) of the dispersion estimate (1.4) for \(B\le X^{0.40}\);
2. then \(\kappa\), \(\rho\) and \(\xi\), and with them the bounded complexity of the prime tuples;
3. then the logarithmic savings and the threshold for large heights;
4. finally \(C_g\), \(C_r\) and the saving powers in (SW).

The estimates for prime convolutions at large \(B\) may depend on the fixed tuple complexity and on \(\xi\). They do not affect \(\gamma\).

## 8. Exercises

**8.1.** Let \(0<\epsilon<\frac1{12}\). Show that the partition \((\frac13-\epsilon,\frac13-\epsilon,\frac13+2\epsilon)\) of \(1\) has no subset sum in \((\frac13+2\epsilon,\frac23-2\epsilon)\). Explain why Lemma 3.2 treats a neighborhood of \((\frac13,\frac13,\frac13)\) separately.

**8.2.** Verify the inequalities \(0.38+\xi+\frac\kappa4<0.40\) and \(\frac13-\kappa+\xi+\frac\kappa4<0.40\) used for the stopped terms, for \(\xi<\kappa/10\) and small \(\kappa\).

**8.3.** In Lemma 4.1 let a fixed squarefree \(m\) have \(k_++k_-\) primes in the final bin. Show that the weighted sum over the selections of \(k_+\) of them equals \(1\).

**8.4.** Show that \(\sum_{N(\pi)\le y}N(\pi)^{-1+\sigma}\le e\sum_{N(\pi)\le y}N(\pi)^{-1}\) for \(0<\sigma\le1/\log y\), and deduce the bound \(O(\log L)\) used in Lemma 6.1.

**8.5.** Show that on the support of the envelope the two-prime correction \(\mathbf 1_{\{\Omega(n)=2\}}\mathcal F_z(n)\) is supported on products of two primes with norms between \(X^{0.40}\) and \(c\,X^{0.60}\), for a constant \(c\) depending on the support of \(V\).

## 9. Solutions

**8.1.** The nonempty subset sums are \(\frac13-\epsilon\), \(\frac13+2\epsilon\), \(\frac23-2\epsilon\), \(\frac23+\epsilon\) and \(1\), and none lies in \((\frac13+2\epsilon,\frac23-2\epsilon)\). As \(\epsilon\to0\) these partitions approach \((\frac13,\frac13,\frac13)\), and the best distance of a subset sum from \(\{\frac13,\frac23\}\) tends to \(0\). So no fixed gap \(\delta_1\) holds near the exceptional vector. Outside a fixed neighborhood of it, Lemma 3.1 and compactness of the remaining exponent vectors give a uniform gap. Inside the neighborhood the three-prime configuration is kept as a separate case.

**8.2.** With \(\xi<\kappa/10\), \(\xi+\frac\kappa4<0.35\kappa\). The first inequality needs \(0.35\kappa<0.02\), and the second \(\frac13-0.65\kappa<0.40\), which holds for every \(\kappa>0\).

**8.3.** There are \(\binom{k_++k_-}{k_+}\) selections with the given counts. By the remark before (4.3) either all of them satisfy the crossing condition or none does, and each carries the weight \(\binom{k_++k_-}{k_+}^{-1}\). Their total is \(1\) or \(0\), the latter exactly when the stop does not occur at this bin with these counts.

**8.4.** For \(N(\pi)\le y\) and \(\sigma\le1/\log y\), \(N(\pi)^\sigma\le y^\sigma\le e\). A rational prime \(p\) lies below at most two prime ideals, of norm \(p\) or \(p^2\), so Mertens' theorem gives \(\sum_{N(\pi)\le y}N(\pi)^{-1}\)\(\le2\sum_{p\le y}p^{-1}+O(1)\)\(=2\log\log y+O(1)\). With \(y=\exp(\sqrt L)\) this is \(\log L+O(1)\).

**8.5.** Both primes have norm greater than \(z=X^{0.40}\) when \(\mathcal F_z(n)\ne0\). If \(V\) is supported in \([v_1,v_2]\), then \(N(n)\le v_2X\), so the other prime has norm at most \(v_2X/X^{0.40}=v_2X^{0.60}\).

## Sources

- [OpenAI-023] OpenAI, *An unconditional first moment for cubic Gauss sums*, OpenAI Math Release preprint, 25 September 2026, Section 6 (the exact decomposition) and Appendix A.4–A.5 (the twisted sequence condition and the angular decomposition). https://github.com/openai/math/tree/main/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026
