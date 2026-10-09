# Correlations of smooth divisor sums

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

[Divisor sums and primes in progressions](divisor-sums-and-primes-in-progressions.md) reduced every moment of smooth divisor sums, with or without a prime factor \(\vartheta(m+a_0)\), to a finite density sum \(\mathcal A_\delta\). This lesson evaluates the density sum. The answer separates into three parts: a power \(L^{-t}\), where \(t\) is the number of distinct shifts carrying divisor coordinates; the singular series of the shifts, from [The singular series and its average](the-singular-series-and-its-average.md); and a constant \(\mathcal C\) that depends only on the test functions and on which coordinates share a shift. When no shift is shared by more than two coordinates, \(\mathcal C\) is an integral of products of complete mixed derivatives of the test functions. This is the form in which divisor-sum correlations were computed by Goldston and Yıldırım, and, with smooth weights and a Fourier transform, in the work of Maynard and Tao [Maynard]; the version here allows several coupled test functions, arbitrary patterns of equal shifts, one prime mark, and shifts of size up to a power of \(\log X\).

The method: each test function is written as a Fourier integral of exponentials \(e^{-(1+iu)v}\). Substituting \(v=\log d/L\) turns \(F(\log d/L)\) into a combination of powers \(d^{-z}\) with \(\operatorname{Re}z=1/L\), and the density sum into an integral of an Euler product. The Euler product factors into values of the Riemann zeta function near \(1\), which produce \(L^{-t}\), times a product converging to the singular series.

We use: Fourier inversion on the Schwartz space, Theorem 1.1 of [Fourier transforms, finite spectra and convex separation](course:elliptic-operators-and-boundary-problems/prerequisite-bridges#fourier-inversion-on-the-schwartz-space); the Euler product of \(\zeta\) and the formula \(\zeta(s)=s/(s-1)-s\int_1^\infty\{u\}u^{-s-1}du\) for \(\operatorname{Re}s>0\), Theorems 2.2 and 5.1 of [Dirichlet series and Euler products](course:NT-ZETA/NT-ZETA-01#5-subtracting-the-pole-of-zeta); Mertens's estimates \(\sum_{p\le x}1/p=\log\log x+O(1)\) and \(\sum_{p\le x}\log p/p=\log x+O(1)\), Theorem 3.1 of [Counting primes by elementary means](course:NT-ZETA/NT-ZETA-02#3-factorials-determine-reciprocal-prime-averages); and Fubini's theorem.

## 1. The setting and the theorem

We keep the setting of Section 4 of the divisor-sums lesson: fixed test functions \(F_r\) of dimensions \(j_r\) and budgets \(\rho_r\) (\(1\le r\le R\)), the coordinate set \(\Gamma=\{(r,\ell)\}\) with \(M=|\Gamma|\), \(\sigma=\sum_r\rho_r\), and \(\delta\in\{0,1\}\) with \(\sigma<1\) if \(\delta=0\) and \(\sigma<1/2\) if \(\delta=1\). In addition we fix a surjection \(\kappa:\Gamma\to\{1,\dots,t\}\), the *pattern*, and write \(\mathcal M_i=\kappa^{-1}(i)\) for its fibres. The shifts are

\[
b_\gamma=a_{\kappa(\gamma)},\qquad a_1,\dots,a_t\ \text{distinct integers},\qquad |a_i|\le DL^B,
\]

with fixed \(D>0\), \(B\ge0\). If \(\delta=1\), the mark \(a_0\) is a further integer, different from \(a_1,\dots,a_t\), with \(|a_0|\le DL^B\). Let

\[
\mathcal H=\{a_1,\dots,a_t\}\ \ (\delta=0),\qquad\mathcal H=\{a_0,a_1,\dots,a_t\}\ \ (\delta=1).
\]

So \(t\) counts the distinct shifts that carry divisor coordinates, while \(M\) counts the coordinates with repetition. Coordinates of one factor may share a shift.

**Theorem 1.1** (correlations of smooth divisor sums). There is a real constant \(\mathcal C\), depending only on the test functions \(F_r\) and the pattern \(\kappa\), and a number \(A\) depending only on \(M\), such that, uniformly in the shifts,

\[
\mathbb E_X\Bigl[\chi_\delta(m)\prod_{r=1}^RD_{F_r}(m;\mathbf b^{(r)})\Bigr]=L^{-t}\Bigl\{\mathfrak S(\mathcal H)\,\mathcal C+O\bigl(L^{-1/2}(\log L)^A\bigr)\Bigr\}.
\]

If \(\Gamma=\varnothing\), then \(t=0\) and \(\mathcal C=\prod_rF_r\). If every fibre \(\mathcal M_i\) has at most two elements, then

\[
\mathcal C=\int_{[0,\infty)^{P}}\ \prod_{r=1}^Rf_r\bigl(y_{\kappa(r,1)},\dots,y_{\kappa(r,j_r)}\bigr)\prod_{i\in P}dy_i,\qquad f_r=(-1)^{j_r}\partial_1\cdots\partial_{j_r}F_r,
\tag{1.1}
\]

where \(P\) is the set of \(i\) with \(|\mathcal M_i|=2\), the variable \(y_i\) is set to \(0\) when \(|\mathcal M_i|=1\), and \(f_r=F_r\) for a scalar factor.

The error term is additive: it remains valid when \(\mathfrak S(\mathcal H)=0\).

Two special cases show the shape of (1.1). For one test function \(F\) of dimension \(1\) and one shift \(b\),

\[
\mathbb E_X D_F(m;b)^2=\frac1L\Bigl\{\int_0^\infty F'(y)^2\,dy+O\bigl(L^{-1/2}(\log L)^A\bigr)\Bigr\},
\]

the fibre being \(\{(1,1),(2,1)\}\). For two different shifts \(b_1\ne b_2\), each fibre is a singleton and

\[
\mathbb E_X D_F(m;b_1)D_F(m;b_2)=\frac1{L^2}\Bigl\{\mathfrak S(\{b_1,b_2\})F'(0)^2+O\bigl(L^{-1/2}(\log L)^A\bigr)\Bigr\}.
\]

By Proposition 4.2 of the divisor-sums lesson, the left side of Theorem 1.1 equals the density sum \(\mathcal A_\delta\) up to \(O(L^{-A'})\) for every \(A'\). It therefore suffices to prove the formula for \(\mathcal A_\delta\), which is done in Sections 2–6.

## 2. A Fourier representation of test functions

**Lemma 2.1.** Let \(F\) be a test function of dimension \(j\ge1\), and let \(\widetilde F\) be a smooth compactly supported extension of \(F\) to \(\mathbb R^j\). Put

\[
\Phi(u)=(2\pi)^{-j}\int_{\mathbb R^j}e^{v_1+\dots+v_j}\,\widetilde F(v)\,e^{iu\cdot v}\,dv\qquad(u\in\mathbb R^j).
\]

Then \(\Phi\) is a Schwartz function, and for all \(v\in\mathbb R^j\)

\[
\widetilde F(v)=\int_{\mathbb R^j}\Phi(u)\,e^{-\sum_\ell(1+iu_\ell)v_\ell}\,du,\qquad
(-1)^j\partial_1\cdots\partial_j\widetilde F(v)=\int_{\mathbb R^j}\Phi(u)\prod_{\ell=1}^j(1+iu_\ell)\,e^{-\sum_\ell(1+iu_\ell)v_\ell}\,du .
\]

**Proof.** The function \(g(v)=e^{\sum_\ell v_\ell}\widetilde F(v)\) is smooth with compact support, hence Schwartz. In the conventions of the Fourier-inversion theorem cited above, \(\Phi=Gg\), and since the Fourier transform \(F\!f(\xi)=\int e^{-ix\cdot\xi}f(x)\,dx\) is an automorphism of the Schwartz space with inverse \(G\), \(\Phi\) is Schwartz and \(g=F\!\Phi\), that is, \(g(v)=\int e^{-iu\cdot v}\Phi(u)\,du\). Multiplying by \(e^{-\sum v_\ell}\) gives the first formula. Every function \(u\mapsto\Phi(u)\prod_\ell(1+iu_\ell)\) is integrable, so differentiation under the integral sign is allowed; each \(\partial_\ell\) brings down the factor \(-(1+iu_\ell)\). \(\square\)

For each positive-dimensional \(F_r\) fix such an extension and its \(\Phi_r\). For \(u=(u_\gamma)_{\gamma\in\Gamma}\in\mathbb R^\Gamma\) put

\[
w_\gamma=1+iu_\gamma,\qquad z_\gamma=\frac{w_\gamma}L,\qquad z_S=\sum_{\gamma\in S}z_\gamma\ \ (S\subseteq\Gamma),\qquad\Phi(u)=\prod_{r:\,j_r\ge1}\Phi_r\bigl((u_{r,\ell})_\ell\bigr)\prod_{r:\,j_r=0}F_r .
\]

For squarefree positive integers the first formula of Lemma 2.1 at \(v_\ell=\log d_{r,\ell}/L\ge0\) reads

\[
F_r\Bigl(\Bigl(\frac{\log d_{r,\ell}}L\Bigr)_\ell\Bigr)=\int\Phi_r(u^{(r)})\prod_\ell d_{r,\ell}^{-z_{r,\ell}}\,du^{(r)} .
\tag{2.1}
\]

## 3. The density sum as an integral of an Euler product

A tuple \(\mathbf d=(d_\gamma)\) of squarefree positive integers is the same as a family \((S_p)_p\), indexed by the primes, of subsets \(S_p=\{\gamma:p\mid d_\gamma\}\subseteq\Gamma\), with only finitely many \(S_p\) nonempty. Compatibility (Definition 4.1 of the divisor-sums lesson) is a condition on each \(S_p\) separately. Call a nonempty \(S\subseteq\Gamma\) *allowed at \(p\)* if the shifts \(b_\gamma\), \(\gamma\in S\), are congruent modulo \(p\) and, when \(\delta=1\), their common residue is not \(a_0\bmod p\). Then \(\mathbf d\) is compatible exactly when every nonempty \(S_p\) is allowed at \(p\), and in that case

\[
\rho_\delta(\mathbf d)\prod_\gamma\mu(d_\gamma)d_\gamma^{-z_\gamma}=\prod_{p:\,S_p\ne\varnothing}\frac{(-1)^{|S_p|}p^{-z_{S_p}}}{p-\delta}.
\tag{3.1}
\]

**Lemma 3.1.** With \(C_M=2(2^M-1)\),

\[
\sum_{\mathbf d}\rho_\delta(\mathbf d)\prod_\gamma d_\gamma^{-1/L}\le\prod_p\Bigl(1+\frac{C_M}{p^{1+1/L}}\Bigr)\le(1+L)^{C_M}.
\]

**Proof.** By (3.1) with absolute values, the sum is a sum of products of local terms over finitely supported families \((S_p)\). For nonnegative terms such a sum equals the product over \(p\) of the local sums \(1+\sum_{S\text{ allowed}}p^{-|S|/L}/(p-\delta)\): the partial product over \(p\le P\) is the sum over families supported on the primes \(p\le P\), and both sides increase to their limits as \(P\to\infty\). There are at most \(2^M-1\) allowed sets, each contributing at most \(p^{-1/L}\cdot2/p\), since \(1/(p-\delta)\le2/p\). Finally, \(\log\prod_p(1+C_Mp^{-1-1/L})\le C_M\sum_pp^{-1-1/L}\le C_M\log\zeta(1+1/L)\), because \(\log\zeta(s)=\sum_p\sum_{k\ge1}p^{-ks}/k\ge\sum_pp^{-s}\) for real \(s>1\), and \(\zeta(1+x)\le1+\int_1^\infty y^{-1-x}dy=1+1/x\) for \(x>0\). \(\square\)

**Lemma 3.2.** For every \(u\in\mathbb R^\Gamma\), with absolutely convergent sum and product,

\[
\sum_{\mathbf d}\rho_\delta(\mathbf d)\prod_\gamma\mu(d_\gamma)d_\gamma^{-z_\gamma}=\prod_pP_p(z),\qquad P_p(z)=1+\frac1{p-\delta}\sum_{S\text{ allowed at }p}(-1)^{|S|}p^{-z_S},
\]

and

\[
\mathcal A_\delta=\int_{\mathbb R^\Gamma}\Phi(u)\prod_pP_p(z)\,du .
\tag{3.2}
\]

**Proof.** Since \(|d^{-z_\gamma}|=d^{-1/L}\), Lemma 3.1 gives absolute convergence of the sum, and of the product in the sense \(\sum_p|P_p(z)-1|<\infty\). The partial product over \(p\le P\) equals, by (3.1), the sum over tuples whose prime factors are all at most \(P\); dominated convergence (with Lemma 3.1) lets \(P\to\infty\). For (3.2), insert (2.1) for each factor into the definition of \(\mathcal A_\delta\); the result is a sum over \(\mathbf d\) of integrals over \(u\). The absolute values have finite total \(\int|\Phi|\cdot(1+L)^{C_M}\), so Fubini's theorem allows the sum to be taken inside. \(\square\)

## 4. Local factors

Separate from \(P_p\) the part that would be present if all shifts were incongruent modulo \(p\):

\[
B_p(z)=\prod_{i=1}^t\ \prod_{\varnothing\ne S\subseteq\mathcal M_i}\bigl(1-p^{-1-z_S}\bigr)^{-(-1)^{|S|}},\qquad H_p(z)=\frac{P_p(z)}{B_p(z)} .
\]

For \(\operatorname{Re}z_\gamma\ge0\) we have \(|p^{-1-z_S}|\le1/p\le1/2\), so \(B_p(z)\ne0\).

**Lemma 4.1.** There is \(C\), depending only on \(M\), such that for every prime \(p\) and every \(z\) with all \(\operatorname{Re}z_\gamma\ge0\):

1. \(|P_p(z)|\), \(|B_p(z)|^{\pm1}\) and \(|H_p(z)|\) are at most \(e^{C/p}\);
2. if the elements of \(\mathcal H\) are pairwise incongruent modulo \(p\), then \(|H_p(z)-1|\le C/p^2\);
3. \(P_p(0)=\dfrac{p-\nu_p(\mathcal H)}{p-\delta}\), \(B_p(0)=(1-1/p)^t\), and \(H_p(0)=\bigl(1-\nu_p(\mathcal H)/p\bigr)(1-1/p)^{-|\mathcal H|}\) is the factor at \(p\) of \(\mathfrak S(\mathcal H)\);
4. \(|H_p(z)-H_p(0)|\le C\,\dfrac{\log p}p\,\max_\gamma|z_\gamma|\).

**Proof.** (1) \(|P_p(z)|\le1+2^{M+1}/p\le e^{2^{M+1}/p}\). Each of the at most \(2^M\) factors of \(B_p\) has the form \((1-x)^{\pm1}\) with \(|x|\le1/p\le1/2\), and \(|1-x|\le e^{1/p}\), \(|1-x|^{-1}\le(1-1/p)^{-1}\le e^{2/p}\).

(2) If the elements of \(\mathcal H\) are incongruent modulo \(p\), two coordinates have congruent shifts only when they lie in the same fibre, and no shift \(a_i\) is congruent to \(a_0\). So the allowed sets are exactly the nonempty subsets of the fibres, and

\[
P_p(z)=1+\frac1{p-\delta}\sum_{i=1}^t\sum_{\varnothing\ne S\subseteq\mathcal M_i}(-1)^{|S|}p^{-z_S}.
\]

On the other hand \((1-x)^{-(-1)^{|S|}}=1+(-1)^{|S|}x+O(|x|^2)\) for \(|x|\le1/2\), so \(B_p(z)=1+p^{-1}\sum_i\sum_S(-1)^{|S|}p^{-z_S}+O_M(p^{-2})\). Since \(1/(p-\delta)=1/p+O(p^{-2})\), \(P_p-B_p=O_M(p^{-2})\), and dividing by \(B_p\) (part 1) gives the claim.

(3) At \(z=0\) the allowed sets are grouped by the residue class \(c\) of their shifts: for each class \(c\) met by the \(b_\gamma\) (and, if \(\delta=1\), different from the class of \(a_0\)), they are the nonempty subsets of \(\{\gamma:b_\gamma\equiv c\}\), with \(\sum_{S\ne\varnothing}(-1)^{|S|}=-1\). The number of such classes is \(\nu_p(\mathcal H)\) if \(\delta=0\), and \(\nu_p(\mathcal H)-1\) if \(\delta=1\), because then \(\mathcal H\) contains \(a_0\), whose class is excluded. Hence \(P_p(0)=1-(\nu_p(\mathcal H)-\delta)/(p-\delta)\). For \(B_p(0)\), each fibre gives \((1-1/p)^{-\sum_{S\ne\varnothing}(-1)^{|S|}}=1-1/p\). Then \(H_p(0)=(p-\nu_p)\big/\bigl((p-\delta)(1-1/p)^t\bigr)\), which is \((1-\nu_p/p)(1-1/p)^{-t}\) for \(\delta=0\) and \((1-\nu_p/p)(1-1/p)^{-t-1}\) for \(\delta=1\); in both cases the exponent is \(|\mathcal H|\).

(4) For \(\operatorname{Re}w\ge0\), \(|e^{-w}-1|=|\int_0^1we^{-sw}ds|\le|w|\); hence \(|p^{-z_S}-1|\le M\max_\gamma|z_\gamma|\log p\). This gives \(|P_p(z)-P_p(0)|\le2^{M+1}M\max|z_\gamma|\log p/p\). The factors \(x=p^{-1-z_S}\) of \(B_p\) move by at most \(p^{-1}M\max|z_\gamma|\log p\), and \(|(1-x)^{-1}-(1-x')^{-1}|\le4|x-x'|\) for \(|x|,|x'|\le1/2\). Changing the factors of \(B_p^{-1}\) one at a time, each partial product being bounded by part 1, gives \(|B_p(z)^{-1}-B_p(0)^{-1}|\le C\max|z_\gamma|\log p/p\). Finally \(H_p(z)-H_p(0)=(P_p(z)-P_p(0))B_p(z)^{-1}+P_p(0)(B_p(z)^{-1}-B_p(0)^{-1})\). \(\square\)

## 5. Comparison with the singular series

**Lemma 5.1.** Put \(Y=2DL^B+L\). There is \(A\), depending only on \(M\), such that uniformly for \(u\in\mathbb R^\Gamma\) with \(\max_\gamma|u_\gamma|\le\sqrt L\),

\[
\prod_pH_p(z)=\mathfrak S(\mathcal H)+O\bigl(L^{-1/2}(\log L)^A\bigr),\qquad\mathfrak S(\mathcal H)\ll(\log L)^A .
\]

**Proof.** In this range \(|z_\gamma|\le(1+\sqrt L)/L\le2L^{-1/2}\).

*Large primes.* Two elements of \(\mathcal H\) differ by a nonzero integer of absolute value at most \(2DL^B<Y\). So for \(p>Y\) they are pairwise incongruent modulo \(p\), and Lemma 4.1(2) applies to \(H_p(z)\) and to \(H_p(0)\). For \(p>Y\ge2C\), \(|\log H_p|\le2C/p^2\), hence \(\prod_{p>Y}H_p(z)\) and \(\prod_{p>Y}H_p(0)\) both equal \(1+O(1/Y)=1+O(1/L)\).

*Small primes.* By Lemma 4.1(1) and Mertens's estimate, every product of the numbers \(H_p(z)\) or \(H_p(0)\) over a set of primes \(p\le Y\) is at most \(\exp(C\sum_{p\le Y}1/p)\ll(\log Y)^C\). Listing the primes \(p_1<p_2<\dots\le Y\) and changing one factor at a time,

\[
\prod_{p\le Y}H_p(z)-\prod_{p\le Y}H_p(0)=\sum_k\Bigl(\prod_{p<p_k}H_p(0)\Bigr)\bigl(H_{p_k}(z)-H_{p_k}(0)\bigr)\Bigl(\prod_{p_k<p\le Y}H_p(z)\Bigr).
\]

By Lemma 4.1(4) and Mertens's estimate \(\sum_{p\le Y}\log p/p\ll\log Y\), this is \(O\bigl((\log Y)^{2C+1}L^{-1/2}\bigr)\). Since \(Y\ll L^{\max(B,1)}\), \(\log Y\ll\log L\).

*Together.* By Lemma 4.1(3), \(\mathfrak S(\mathcal H)=\prod_pH_p(0)\), and

\[
\prod_pH_p(z)-\mathfrak S(\mathcal H)=\Bigl[\prod_{p\le Y}H_p(z)-\prod_{p\le Y}H_p(0)\Bigr]\prod_{p>Y}H_p(z)+\prod_{p\le Y}H_p(0)\Bigl[\prod_{p>Y}H_p(z)-\prod_{p>Y}H_p(0)\Bigr],
\]

which is \(O(L^{-1/2}(\log L)^{2C+1})+O((\log L)^C/L)\). The bound for \(\mathfrak S(\mathcal H)\) follows from the same estimates at \(z=0\). \(\square\)

No division by a local factor of \(\mathfrak S(\mathcal H)\) occurs, so the lemma holds also when some of these factors vanish.

## 6. The zeta factors and the proof of Theorem 1.1

**Lemma 6.1.** For \(\operatorname{Re}z>0\) and \(|z|\le1\), \(|\zeta(1+z)-1/z|\le3\). Consequently, for \(|z|\le1/12\), \(\zeta(1+z)=z^{-1}(1+\eta)\) and \(\zeta(1+z)^{-1}=z(1+\eta')\) with \(|\eta|\le3|z|\) and \(|\eta'|\le6|z|\).

**Proof.** By Theorem 5.1 of the zeta lesson with \(s=1+z\), \(\zeta(1+z)-1/z=1-(1+z)\int_1^\infty\{u\}u^{-2-z}du\), and the integral is at most \(\int_1^\infty u^{-2}du=1\) in absolute value. Then \(\eta=z(\zeta(1+z)-1/z)\), \(|\eta|\le3|z|\le1/4\), and \(\eta'=(1+\eta)^{-1}-1\) has \(|\eta'|\le|\eta|/(1-|\eta|)\le2|\eta|\). \(\square\)

For a fibre \(\mathcal M_i\) define

\[
K_i(u)=\prod_{\varnothing\ne S\subseteq\mathcal M_i}\Bigl(\sum_{\gamma\in S}w_\gamma\Bigr)^{(-1)^{|S|+1}} .
\]

Every sum \(\sum_{\gamma\in S}w_\gamma\) has real part \(|S|\ge1\), so \(|K_i(u)|\le(M(1+\max|u_\gamma|))^{2^M}\): the product \(\prod_iK_i\) grows at most polynomially.

**Lemma 6.2.** There is \(L_0\), depending only on \(M\), such that for \(L\ge L_0\) and \(\max_\gamma|u_\gamma|\le\sqrt L\),

\[
\prod_pB_p(z)=L^{-t}\prod_{i=1}^tK_i(u)\,\bigl(1+O_M(L^{-1/2})\bigr).
\]

**Proof.** Each \(z_S\) has real part \(|S|/L>0\), so \(\prod_p(1-p^{-1-z_S})^{-1}=\zeta(1+z_S)\) by the Euler product, with absolute convergence. Hence

\[
\prod_pB_p(z)=\prod_{i=1}^t\prod_{\varnothing\ne S\subseteq\mathcal M_i}\zeta(1+z_S)^{(-1)^{|S|}} .
\]

Here \(|z_S|\le2ML^{-1/2}\le1/12\) for \(L\ge L_0\), and by Lemma 6.1 each factor equals \(z_S^{-(-1)^{|S|}}(1+O(ML^{-1/2}))\). Since \(z_S=L^{-1}\sum_{\gamma\in S}w_\gamma\) and \(\sum_{\varnothing\ne S\subseteq\mathcal M_i}(-1)^{|S|+1}=1\), the product over the subsets of one fibre is \(L^{-1}K_i(u)(1+O(L^{-1/2}))\). There are at most \(2^M\) factors in all. \(\square\)

**Proof of Theorem 1.1.** If \(\Gamma=\varnothing\), the only tuple is the empty one, with \(q=1\) and \(\rho_\delta=1\), so \(\mathcal A_\delta=\prod_rF_r\); also \(t=0\), and \(\mathcal H\) is empty or a single point, so \(\mathfrak S(\mathcal H)=1\). Assume \(M\ge1\) and start from (3.2).

*Large frequencies.* By Lemma 3.1, \(|\prod_pP_p(z)|\le(1+L)^{C_M}\) for every \(u\). Since \(\Phi\) is Schwartz, \(\int_{\max|u_\gamma|>\sqrt L}|\Phi(u)|\,du\ll_NL^{-N}\) for every \(N\). This part of (3.2) is negligible.

*Small frequencies.* For \(\max|u_\gamma|\le\sqrt L\), the products \(\prod_pB_p(z)\) and \(\prod_pH_p(z)\) converge (Lemma 6.2 and Lemma 4.1(2) for large \(p\)), and their product is \(\prod_pP_p(z)\). Lemmas 5.1 and 6.2 give

\[
\prod_pP_p(z)=L^{-t}\prod_iK_i(u)\Bigl\{\mathfrak S(\mathcal H)+O\bigl(L^{-1/2}(\log L)^A\bigr)\Bigr\},
\]

using \(\mathfrak S(\mathcal H)\ll(\log L)^A\) to absorb the factor \(1+O(L^{-1/2})\). Integrating against \(\Phi\), and using that \(\Phi\prod_iK_i\) is integrable with tails \(\int_{\max|u_\gamma|>\sqrt L}|\Phi\prod K_i|\ll_NL^{-N}\),

\[
\mathcal A_\delta=L^{-t}\Bigl\{\mathfrak S(\mathcal H)\,\mathcal C+O\bigl(L^{-1/2}(\log L)^A\bigr)\Bigr\},\qquad\mathcal C=\int_{\mathbb R^\Gamma}\Phi(u)\prod_{i=1}^tK_i(u)\,du .
\]

The constant is real: the \(F_r\) are real, so \(\Phi_r(-u)=\overline{\Phi_r(u)}\), and \(K_i(-u)=\overline{K_i(u)}\). It does not depend on the shifts. It does not depend on the chosen extensions either: for any admissible set of \(t\) shifts (Exercise 5.2 of the singular-series lesson), \(\mathcal C=\lim_{L\to\infty}L^t\mathcal A_\delta/\mathfrak S(\mathcal H)\), and \(\mathcal A_\delta\) involves only the values of the \(F_r\) on the orthant.

*Fibres of size at most two.* A singleton fibre \(\{\gamma\}\) has \(K_i=w_\gamma\). A fibre \(\{\gamma,\gamma'\}\) has

\[
K_i=\frac{w_\gamma w_{\gamma'}}{w_\gamma+w_{\gamma'}}=w_\gamma w_{\gamma'}\int_0^\infty e^{-(w_\gamma+w_{\gamma'})y}\,dy,
\]

since \(\operatorname{Re}(w_\gamma+w_{\gamma'})=2\). Hence, with \(y_i=0\) for singleton fibres,

\[
\mathcal C=\int_{\mathbb R^\Gamma}\int_{[0,\infty)^P}\Phi(u)\prod_{\gamma\in\Gamma}w_\gamma e^{-w_\gamma y_{\kappa(\gamma)}}\,dy\,du .
\]

The absolute value of the integrand is \(|\Phi(u)|\prod_\gamma|w_\gamma|\,e^{-2\sum_{i\in P}y_i}\), which is integrable. By Fubini's theorem we may integrate over \(u\) first. The \(u\)-integral factors over \(r\), and by Lemma 2.1 the factor of \(r\) is \((-1)^{j_r}\partial_1\cdots\partial_{j_r}\widetilde F_r\) at the point \((y_{\kappa(r,\ell)})_\ell\) of the orthant, where it equals \(f_r\). This is (1.1).

Finally, Proposition 4.2 of the divisor-sums lesson replaces \(\mathcal A_\delta\) by the average with an error \(O(L^{-t-1})\). \(\square\)

The convergence is slow but visible numerically. Take \(F(v)=(\rho-v)^3\) for \(0\le v\le\rho\), extended by zero. (It is only twice continuously differentiable, which does not matter for the density sums.) The ratios of the exact density sums to the main terms of Theorem 1.1 are:

| \(L\) | 8 | 12 | 16 | 20 |
|---|---|---|---|---|
| \(D_F(m;0)^2\), \(\rho=0.4\) | 0.861 | 0.899 | 0.922 | 0.938 |
| \(D_F(m;0)D_F(m;2)\), \(\rho=0.4\) | 0.398 | 0.554 | 0.659 | 0.729 |
| \(\vartheta(m+2)D_F(m;0)^2\), \(\rho=0.24\) | 0.746 | 0.903 | 0.956 | 0.973 |

For \(X=2\cdot10^6\) the direct average \(\mathbb E_X D_F(m;0)D_F(m;2)\) and its density sum agree to within \(4\cdot10^{-10}\), and the marked average \(\mathbb E_X\vartheta(m+2)D_F(m;0)^2\) is within \(0.1\%\) of its density sum.

## 7. Exercises

**Exercise 7.1** (Selberg's upper bound). Let \(0<\rho<1/2\) and let \(F\) be a one-dimensional test function of budget \(\rho\) with \(F(0)=1\). Show that

\[
\#\{X<p\le2X:p\text{ prime}\}\le\frac XL\Bigl(\int_0^\infty F'(y)^2dy+o(1)\Bigr).
\]

Deduce that the number of primes in \((X,2X]\) is at most \((2+\varepsilon)X/\log X\) for every \(\varepsilon>0\) and large \(X\).

**Exercise 7.2.** Compute \(K_i\) for a fibre with three elements and check that it is homogeneous of degree \(1\) in \((w_1,w_2,w_3)\).

**Exercise 7.3.** Suppose a shift \(a_i\) occurs in exactly one coordinate \(\gamma=(r,\ell)\), and \(f_r\) vanishes whenever its \(\ell\)-th argument is \(0\). Show from (1.1) that \(\mathcal C=0\) when all fibres have at most two elements.

**Exercise 7.4.** Use Theorem 1.1 to find the main term of \(\mathbb E_X\vartheta(m+a)D_F(m;b)^2\) for a one-dimensional \(F\) of budget \(\rho<1/4\) and \(a\ne b\), and explain why it vanishes when \(a-b\) is odd.

**Exercise 7.5.** Show that \(\prod_iK_i(u)\) is unchanged if the coordinates inside a fibre are permuted, and that (1.1) does not depend on the order in which the coordinates of each factor are listed, as long as the same order is used for the pattern.

## 8. Solutions

**7.1.** Every prime \(m\in(X,2X]\) exceeds \(X^\rho\), so \(D_F(m;0)=F(0)=1\) by Exercise 5.1 of the divisor-sums lesson. Since \(D_F^2\ge0\), the number of primes in \((X,2X]\) is at most \(X\,\mathbb E_XD_F(m;0)^2\). The first special case of Theorem 1.1 gives \(\mathbb E_XD_F(m;0)^2=L^{-1}(\int F'^2+o(1))\). Among functions with \(F(0)=1\), \(F(\rho)=0\), Cauchy–Schwarz gives \(\int_0^\rho F'^2\ge(\int_0^\rho F')^2/\rho=1/\rho\), with near-equality for smooth approximations of \(1-v/\rho\). Choosing \(\rho\) close to \(1/2\) and such an \(F\) gives \((2+\varepsilon)X/\log X\).

**7.2.** For \(\mathcal M_i=\{1,2,3\}\), the subsets of odd size give factors \(w_1,w_2,w_3,w_1+w_2+w_3\) in the numerator, and those of even size give \(w_1+w_2,w_1+w_3,w_2+w_3\) in the denominator:

\[
K_i=\frac{w_1w_2w_3(w_1+w_2+w_3)}{(w_1+w_2)(w_1+w_3)(w_2+w_3)},
\]

of degree \(4-3=1\). In general the degree is \(\sum_{S\ne\varnothing}(-1)^{|S|+1}=1\).

**7.3.** In (1.1) the variable at the singleton fibre of \(a_i\) is \(y_i=0\), so the factor \(f_r\) is evaluated with \(\ell\)-th argument \(0\) and vanishes; the integrand is identically zero.

**7.4.** Here \(t=1\) (one shift \(b\), carried by two coordinates), \(\delta=1\), and \(\mathcal H=\{a,b\}\). The fibre has two elements, so \(\mathcal C=\int_0^\infty F'(y)^2dy\) and the main term is \(L^{-1}\mathfrak S(\{a,b\})\int_0^\infty F'^2\). For odd \(a-b\), \(\mathfrak S(\{a,b\})=0\) (Lemma 1.3 of the singular-series lesson). Indeed \(D_F(m;b)^2\) favours \(m\) with \(m+b\) odd, and then \(m+a\) is even.

**7.5.** The factors of \(K_i\) are indexed by the subsets of the fibre, and a permutation of the fibre permutes these subsets. In (1.1), reordering the coordinates of a factor \(r\) permutes the arguments of \(F_r\) and of \(f_r\) consistently; the integral over the fibre variables is unchanged.

## References

- [OpenAI-Gaps] OpenAI, Positive lower density of large prime gaps, preprint, 25 September 2026. https://github.com/openai/math/tree/main/preprints/Positive-lower-density-of-large-prime-gaps-September-25-2026
- [GY] D. A. Goldston, C. Y. Yıldırım, Higher correlations of divisor sums related to primes I: triple correlations, Integers 3 (2003), A5. https://math.colgate.edu/~integers/d5/d5.pdf
- [Maynard] J. Maynard, Small gaps between primes, Annals of Mathematics 181 (2015), 383–413. https://arxiv.org/abs/1311.4600
- [Soundararajan] K. Soundararajan, Small gaps between prime numbers: the work of Goldston–Pintz–Yıldırım, Bulletin of the American Mathematical Society 44 (2007), 1–18. https://arxiv.org/abs/math/0605696
