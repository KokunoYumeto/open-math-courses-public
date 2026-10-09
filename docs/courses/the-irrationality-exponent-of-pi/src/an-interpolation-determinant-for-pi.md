# An interpolation determinant for π

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Suppose that \(\pi\) has very good rational approximations \(p_i/q_i\), \(1\le i\le m\). This lesson builds from them a matrix of Taylor coefficients of polynomials along logarithmic curves centred at Gaussian rational points, takes a nonzero maximal minor \(\Delta_H\) (it exists by [Interpolation on logarithmic curves](interpolation-on-logarithmic-curves.md)), and proves two bounds. Arithmetically, clearing denominators shows that \(\Delta_H\) cannot be too small. Analytically, moving the centres to the exact periods \(2\pi\mathrm ij\) of the exponential and expanding in Taylor series shows that \(\Delta_H\) is very small, either because many rows test the same entire functions, or because the approximation errors \(|\pi-p_i/q_i|\) enter to a high power. The last proposition states when the two bounds contradict each other; [The irrationality exponent of π is two](the-irrationality-exponent-of-pi-is-two.md) chooses parameters for which they do.

We use Theorem 1.1 and Lemma 3.1 of the interpolation lesson, Lemma 3.1 (lattice counts) of [The curve inequality](the-curve-inequality.md), Legendre's formula for the exponent of a prime in \(n!\), and Cauchy's estimate for the coefficients of a power series on a disk, from the core course [Complex Analysis (C50)](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C50). The imaginary unit is written \(\mathrm i\); the letter \(i\) is an index. Put \(\omega=2\pi\mathrm i\).

## 1. The data and the matrix

Fix \(\nu>2\), integers \(m,K\ge1\), and positive rationals \(w_0,v_0,\theta\) as in Theorem 1.1 of the interpolation lesson. Suppose that for \(1\le i\le m\) there are integers \(p_i\ne0\), \(q_i\ge2\) with

\[
\Bigl|\pi-\frac{p_i}{q_i}\Bigr|\le q_i^{-\nu},\qquad w_i=\lceil\log q_i\rceil,\qquad r_i=\frac{2\mathrm ip_i}{q_i},
\tag{1.1}
\]

such that the integers \(w_1,\dots,w_m\) exceed the thresholds of that theorem. Put \(w_*=\min_iw_i\ge1\), \(w\alpha=\sum_iw_i\alpha_i\) for \(\alpha\in\mathbb N^m\), and take the centres \(c_{ji}=jr_i\), \(0\le j<K\); they are distinct in \(j\) because \(r_i\ne0\). Fix \(F_0>2/\theta\) and put

\[
T_i=\Bigl\lceil\frac{F_0w_i}{v_0}\Bigr\rceil,\qquad G_i(t)=\sum_{1\le k<T_i}\frac{(-1)^{k+1}t^k}k .
\]

The first omitted term of \(\log(1+t)\) has \(V\)-weight \(v_0T_i\ge F_0w_i>w_i/\theta=v_i\), so by Lemma 3.1 of the interpolation lesson, replacing \(\log(1+t)\) by \(G_i(t)\) in (1.1) of that lesson preserves the surjectivity.

**The matrix.** Its columns are indexed by the monomials \(P=Y^hX^\alpha\) with \(w_0h+w\alpha\le H\), and its rows by the triples \(\rho=(j,s,\beta)\) with \(0\le j<K\), \(s\in\mathbb N\), \(\beta\in\mathbb N^m\) and \(v_0s+w\beta/\theta<H\). The entry is the coefficient of \(t^su^\beta\) in

\[
P\bigl(1+t,\,jr_1+G_1(t)+u_1,\,\dots,\,jr_m+G_m(t)+u_m\bigr).
\tag{1.2}
\]

For \(H\) a sufficiently large multiple of the integer \(R\) of the interpolation theorem, this matrix has independent rows, so it has a nonzero square minor \(\Delta_H\) using all the rows. Let \(M=M_H\) be the number of rows and

\[
\bar b=\bar b_H=\frac1{MH}\sum_{\rho=(j,s,\beta)}w\beta .
\]

By the lattice-count lemma, \(M\sim K\theta^mH^{m+1}/\bigl((m+1)!\,v_0\prod_iw_i\bigr)\) as \(H\to\infty\), and \(0\le\bar b\le\theta\) because every row has \(w\beta<\theta H\). All parameters except \(H\) are fixed in this lesson.

## 2. The arithmetic lower bound

**Lemma 2.1.** For every \(n\ge1\), \(\log\operatorname{lcm}(1,\dots,n)\le4n\log2\).

**Proof.** Let \(\psi(N)=\log\operatorname{lcm}(1,\dots,N)=\sum_{p^k\le N}\log p\). For \(\ell\ge1\), Legendre's formula gives \(v_p\binom{2\ell}\ell=\sum_{k\ge1}\bigl(\lfloor2\ell/p^k\rfloor-2\lfloor\ell/p^k\rfloor\bigr)\), a sum of terms equal to \(0\) or \(1\), and the term is \(1\) whenever \(\ell<p^k\le2\ell\). So \(\psi(2\ell)-\psi(\ell)\le\log\binom{2\ell}\ell\le2\ell\log2\). Summing over \(\ell=2^0,\dots,2^{r-1}\) gives \(\psi(2^r)\le2^{r+1}\log2\). For \(2^{r-1}<n\le2^r\), \(\psi(n)\le\psi(2^r)\le2^{r+1}\log2<4n\log2\). \(\square\)

**Proposition 2.2** (arithmetic lower bound). With \(\Lambda=4\log2\) and

\[
E_{\mathrm{ar}}=\frac{\Lambda F_0m}{v_0}+\Lambda\sum_{i=1}^m\frac1{w_i}+\frac\theta{w_*},
\]

every minor \(\Delta_H\) chosen above satisfies

\[
\frac{\log|\Delta_H|}{MH}\ge-(1-\bar b)-E_{\mathrm{ar}} .
\]

**Proof.** Let \(L_i=\operatorname{lcm}(1,\dots,T_i-1)\) (\(L_i=1\) if \(T_i=1\)) and \(D_H=\prod_iL_i^{\lfloor H/w_i\rfloor}\). Multiply the column of \(Y^hX^\alpha\) by \(\prod_iq_i^{\alpha_i}\) and the row of \((j,s,\beta)\) by \(\prod_iq_i^{-\beta_i}\). Expanding (1.2), the scaled entry is \(0\) unless \(\alpha\ge\beta\) componentwise, and then equals

\[
\prod_i\binom{\alpha_i}{\beta_i}\ [t^s]\,(1+t)^h\prod_i\bigl(q_i(jr_i+G_i(t))\bigr)^{\alpha_i-\beta_i}.
\]

Here \(q_ijr_i=2\mathrm ijp_i\in\mathbb Z[\mathrm i]\) and \(q_iG_i(t)\) has coefficients in \(L_i^{-1}\mathbb Z\). So the denominator of the entry divides \(\prod_iL_i^{\alpha_i}\), which divides \(D_H\) because \(w_i\alpha_i\le H\). Multiplying the scaled square submatrix by \(D_H\) gives a matrix over \(\mathbb Z[\mathrm i]\) with nonzero determinant, of absolute value at least \(1\). Therefore

\[
\log|\Delta_H|\ge-M\log D_H-\sum_{\text{columns}}\sum_i\alpha_i\log q_i+\sum_{\text{rows}}\sum_i\beta_i\log q_i .
\]

Since \(\log q_i\le w_i\), each column has \(\sum_i\alpha_i\log q_i\le w\alpha\le H\). Since \(\log q_i>w_i-1\) and \(\sum_i\beta_i\le w\beta/w_*<\theta H/w_*\), the row sum is at least \(MH\bar b-MH\theta/w_*\). Finally, by Lemma 2.1 and \(T_i\le F_0w_i/v_0+1\),

\[
\frac{\log D_H}H\le\sum_i\frac{\Lambda T_i}{w_i}\le\frac{\Lambda F_0m}{v_0}+\Lambda\sum_i\frac1{w_i}.
\]

Dividing by \(MH\) gives the claim. \(\square\)

## 3. Translation to the exact periods

For \(a\in\mathbb N^m\) and a column \(P\) define the entire function

\[
f_{a,P}(z)=[u^a]\,P(e^z,z+u_1,\dots,z+u_m),\qquad
f_{a,Y^hX^\alpha}(z)=\binom\alpha a\,e^{hz}z^{|\alpha|-|a|}\ \ (a\le\alpha),\ \ 0\ \text{otherwise}.
\]

Only indices with \(wa\le H\) occur.

**Lemma 3.1** (row translation). Each row \(\rho=(j,s,\beta)\) of the matrix is a linear combination, with coefficients independent of the column, of at most

\[
Q_H=(\lfloor H\rfloor+1)^{2m}(\lfloor H/v_0\rfloor+1)
\]

*test rows* \(\bigl([t^\ell]f_{a,P}(j\omega+\log(1+t))\bigr)_P\) with \(a\ge\beta\), \(wa\le H\) and \(0\le\ell\le s\). Each coefficient \(\xi\) attached to an index \(a\) satisfies

\[
\log|\xi|\le-\nu\,w(a-\beta)+HE_{\mathrm{tr}},\qquad E_{\mathrm{tr}}=\frac\nu{F_0}+\frac{\log2}{v_0}+\frac{\log4+\log(2K)+\nu}{w_*}.
\]

**Proof.** Put \(\epsilon_i=jr_i-j\omega=2\mathrm ij(p_i/q_i-\pi)\) and \(\tau_i(t)=G_i(t)-\log(1+t)\). With \(z=j\omega+\log(1+t)\) we have \(e^z=1+t\) and \(jr_i+G_i(t)+u_i=z+u_i+\epsilon_i+\tau_i(t)\). Expanding \(P(e^z,z+v)=\sum_af_{a,P}(z)v^a\) with \(v=u+\epsilon+\tau(t)\), and \(v^a\) by the binomial theorem, the coefficient of \(t^su^\beta\) is

\[
\sum_{a\ge\beta}\binom a\beta\sum_{0\le d\le a-\beta}\binom{a-\beta}d\epsilon^{a-\beta-d}\sum_{k=0}^s\Bigl([t^k]\prod_i\tau_i(t)^{d_i}\Bigr)\,[t^{s-k}]f_{a,P}\bigl(j\omega+\log(1+t)\bigr),
\]

with multi-index notation. The scalars do not depend on \(P\).

The series \(\prod_i\tau_i^{d_i}\) has order at least \(\sum_id_iT_i\); so a nonzero term has \(\sum d_iT_i\le k\le s\), and then

\[
\sum_id_iw_i\le\frac{v_0}{F_0}\sum_id_iT_i\le\frac{v_0s}{F_0}<\frac H{F_0}.
\]

On \(|t|=1/2\), \(|\tau_i(t)|\le\sum_{k\ge T_i}2^{-k}/k\le1\), so Cauchy's estimate bounds the coefficient \([t^k]\prod\tau_i^{d_i}\) by \(2^k\le2^s<2^{H/v_0}\). From (1.1), \(|\epsilon_i|\le2Kq_i^{-\nu}\le2Ke^\nu e^{-\nu w_i}\), since \(q_i>e^{w_i-1}\). So

\[
|\epsilon^{a-\beta-d}|\le(2Ke^\nu)^{|a|}e^{-\nu w(a-\beta)}e^{\nu wd}\le e^{H(\log(2K)+\nu)/w_*}\,e^{-\nu w(a-\beta)}\,e^{\nu H/F_0},
\]

using \(|a|\le wa/w_*\le H/w_*\). Moreover \(\binom a\beta\binom{a-\beta}d\le4^{|a|}\le e^{H\log4/w_*}\). Multiplying these bounds gives the estimate for \(\xi\). For the count: every coordinate of \(a\) and of \(d\) is at most \(H\) (as \(w_i\ge1\)), and \(0\le k\le s<H/v_0\). \(\square\)

## 4. Repeated Taylor degrees

**Lemma 4.1** (collision estimate). Choose one test row from the expansion of each row of \(\Delta_H\), and let \(T\) be the resulting \(M\times M\) matrix (same columns as \(\Delta_H\)). Let \(n_a\) be the number of its rows with index \(a\). With \(c=(\log2)/4\) and

\[
E_{\mathrm{hol}}=\frac{100K}{w_0}+\frac{\log2}{v_0}+\frac{\log(200K)}{w_*},
\]

there is \(\rho_H\to0\), independent of the choices, with

\[
|\det T|\le\exp\Bigl\{-c\sum_an_a^2+MH(E_{\mathrm{hol}}+\rho_H)\Bigr\}.
\]

**Proof.** Put \(R_0=100K\). For a column \(P=Y^hX^\alpha\) and \(|z|\le R_0\), \(|f_{a,P}(z)|\le2^{|\alpha|}e^{hR_0}R_0^{|\alpha|}\le\mathcal D_H:=\exp\{H(R_0/w_0+\log(2R_0)/w_*)\}\), because \(h\le H/w_0\) and \(|\alpha|\le H/w_*\). Expand \(f_{a,P}(z)=\sum_{e\ge0}c_{a,e,P}(z/R_0)^e\); Cauchy's estimate gives \(|c_{a,e,P}|\le\mathcal D_H\). A test row with centre \(j\) and order \(\ell\) evaluates \(P\mapsto[t^\ell]f_{a,P}(j\omega+\log(1+t))\). On \(|t|=1/2\), \(|j\omega+\log(1+t)|\le2\pi(K-1)+\log2<50K=R_0/2\), so

\[
\Bigl|[t^\ell]\Bigl(\frac{j\omega+\log(1+t)}{R_0}\Bigr)^e\Bigr|\le2^\ell2^{-e}.
\]

Expand \(\det T\) by multilinearity in the rows, writing each test row as \(\sum_e\bigl([t^\ell]{}(\cdots)^e\bigr)\,(c_{a,e,P})_P\). The terms are indexed by a choice of a degree \(e_\rho\) for every row; each is a product of scalars times the determinant of the matrix with rows \((c_{a_\rho,e_\rho,P})_P\), of modulus at most \(M!\,\mathcal D_H^M\). The expansion converges absolutely, by the factors \(2^{-e}\). If two rows have the same pair \((a,e)\), their coefficient rows coincide and the term vanishes. So in a nonzero term the degrees within each group of rows with the same \(a\) are distinct, and \(\sum_\rho e_\rho\ge\sum_a\binom{n_a}2\). Using half of the decay for this and summing the other half freely,

\[
|\det T|\le M!\,\mathcal D_H^M\,2^{\sum_\rho\ell_\rho}\,2^{-\frac12\sum_a\binom{n_a}2}\,(1-2^{-1/2})^{-M}.
\]

Here \(\sum_\rho\ell_\rho\le\sum_\rho s_\rho\le MH/v_0\), and \(\frac12\sum_a\binom{n_a}2=\frac14\sum_an_a^2-\frac M4\). Taking logarithms gives the claim with \(\rho_H=\bigl(\log M+\frac14\log2-\log(1-2^{-1/2})\bigr)/H\), which tends to \(0\) because \(M\) grows polynomially in \(H\). \(\square\)

## 5. Two incompatible bounds

Put \(E_{\mathrm{an}}=E_{\mathrm{tr}}+E_{\mathrm{hol}}\).

**Proposition 5.1** (determinant comparison). Let \(0<A<1\), \(0<\eta<1\), and

\[
g=\nu\bigl(A(1-\eta)-\theta\bigr)-(1-\theta),\qquad\mathcal L=\frac{\eta^2K\theta^m}{(m+1)v_0A^m}.
\]

If

\[
g>0,\qquad E_{\mathrm{ar}}+E_{\mathrm{an}}<g,\qquad c\mathcal L>1+E_{\mathrm{ar}}+E_{\mathrm{an}},
\tag{5.1}
\]

then the approximations (1.1) cannot exist together with the hypotheses of Section 1.

**Proof.** Let \(D_A(H)=\#\{a\in\mathbb N^m:wa\le AH\}\) and \(\mathcal L_H=\eta^2M/(HD_A(H))\). The lattice counts give \(D_A(H)\sim(AH)^m/(m!\prod_iw_i)\), and with the asymptotics of \(M\), \(\mathcal L_H\to\mathcal L\).

Expand \(\Delta_H\) by the row translations of Lemma 3.1, using multilinearity: it becomes a sum of at most \(Q_H^M\) terms, each a product of coefficients \(\xi_\rho\) times a determinant \(\det T\) as in Lemma 4.1. For a term with indices \(a_\rho\), the coefficients contribute at most \(\exp\{-\nu\sum_\rho w(a_\rho-\beta_\rho)+MHE_{\mathrm{tr}}\}=\exp\{-\nu\sum_\rho wa_\rho+\nu MH\bar b+MHE_{\mathrm{tr}}\}\).

*If at least \(\eta M\) rows have \(wa_\rho\le AH\):* these rows have at most \(D_A(H)\) distinct indices, so Cauchy–Schwarz gives \(\sum_an_a^2\ge(\eta M)^2/D_A(H)=MH\mathcal L_H\). The coefficient exponent \(-\nu\sum w(a_\rho-\beta_\rho)\) is nonpositive. So the term is at most \(\exp\{MH(-c\mathcal L_H+E_{\mathrm{an}}+\rho_H)\}\).

*Otherwise* more than \((1-\eta)M\) rows have \(wa_\rho>AH\), so \(\sum_\rho wa_\rho\ge(1-\eta)AMH\). Discarding the nonpositive collision term, the term is at most \(\exp\{MH(-\nu(A(1-\eta)-\bar b)+E_{\mathrm{an}}+\rho_H)\}\).

Summing the absolute values of all terms,

\[
\frac{\log|\Delta_H|}{MH}\le E_{\mathrm{an}}+\varepsilon_H+\max\bigl\{-c\mathcal L_H,\,-\nu(A(1-\eta)-\bar b)\bigr\},\qquad\varepsilon_H=\rho_H+\frac{\log Q_H}H\to0 .
\]

Compare with Proposition 2.2. In the first alternative, \(c\mathcal L_H>1+E_{\mathrm{ar}}+E_{\mathrm{an}}+\varepsilon_H\ge(1-\bar b)+E_{\mathrm{ar}}+E_{\mathrm{an}}+\varepsilon_H\) for large \(H\), by (5.1) and \(\mathcal L_H\to\mathcal L\). In the second, since \(\bar b\le\theta\) and \(\nu>1\),

\[
\nu\bigl(A(1-\eta)-\bar b\bigr)-(1-\bar b)=\nu A(1-\eta)-1-(\nu-1)\bar b\ge g>E_{\mathrm{ar}}+E_{\mathrm{an}}+\varepsilon_H
\]

for large \(H\). In both cases \(\log|\Delta_H|/(MH)<-(1-\bar b)-E_{\mathrm{ar}}\), contradicting Proposition 2.2. \(\square\)

The two alternatives explain the two requirements on the parameters. The collision saving \(c\mathcal L\) must beat the trivial arithmetic cost \(1\), which needs many rows per transverse index: \(\mathcal L\) compares the row count in dimension \(m+1\) with the index count in dimension \(m\). The approximation gain \(g\) must beat the cost \(1-\theta\) of the rows, which needs \(\nu(A-\theta)>1-\theta\); this is possible only because \(\nu>2\) allows \(A\) and \(\theta\) close to \(1\) with \(A^2<\theta\).

## 6. Exercises

**Exercise 6.1.** Show that \(\binom{2\ell}\ell\le4^\ell\) and deduce \(\psi(2\ell)-\psi(\ell)\le2\ell\log2\) as in Lemma 2.1.

**Exercise 6.2.** Compute \(f_{a,P}\) for \(m=1\), \(P=YX_1^3\) and \(a=1\), and check the bound \(|f_{a,P}(z)|\le\mathcal D_H\) on \(|z|\le R_0\) for \(H=w_0+3w_1\).

**Exercise 6.3.** Show that if all \(M\) rows of a matrix test the same entire function \(f\) (that is, the rows are \(([t^{\ell_\rho}]f_P(z_\rho+\log(1+t)))_P\) for one index), then the collision estimate gives \(|\det T|\le e^{-cM^2+O(MH)}\), and explain why this is much smaller than \(e^{-MH}\) when \(M\gg H\).

**Exercise 6.4.** In the proof of Proposition 5.1, where is it used that the coefficients \(\xi_\rho\) are independent of the column?

## 7. Solutions

**6.1.** \(\binom{2\ell}\ell\le\sum_k\binom{2\ell}k=4^\ell\). The prime powers \(p^k\in(\ell,2\ell]\) each contribute \(\log p\) to \(\log\binom{2\ell}\ell\), and the other contributions are nonnegative.

**6.2.** \(P(e^z,z+u)=e^z(z+u)^3\), so \(f_{1,P}(z)=3e^zz^2\). On \(|z|\le R_0\), \(|f|\le3e^{R_0}R_0^2\le2^3e^{R_0}R_0^3=\exp\{R_0+3\log(2R_0)\}\le\exp\{H(R_0/w_0+\log(2R_0)/w_1)\}\), since \(H/w_0\ge1\) and \(H/w_1\ge3\).

**6.3.** With one index, \(n_a=M\), so \(\sum n_a^2=M^2\). The bound is \(e^{-cM^2+MH(E_{\mathrm{hol}}+\rho_H)}\), and \(cM^2\) dominates \(MH\) when \(M/H\to\infty\). In the proof, \(M\asymp H^{m+1}\) while the number of indices \(a\) is only \(\asymp H^m\), so the rows must share indices massively.

**6.4.** Multilinearity of the determinant in its rows requires each row to be a linear combination of test rows with scalar coefficients, the same for every column. This is what allows \(\Delta_H\) to be expanded as a sum of products of scalars and determinants of test-row matrices.

## References

- [OpenAI-Pi] OpenAI, The irrationality exponent of π is 2, preprint, 24 September 2026. https://github.com/openai/math/tree/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026
- [Laurent] M. Laurent, Sur quelques résultats récents de transcendance, Astérisque 198–200 (1991). https://www.numdam.org/item/AST_1991__198-199-200__209_0/
