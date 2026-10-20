# The major term and the theorem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

On a major arc \(\theta=h/k+\lambda/Y\), the phase \(e(\theta(bmn-ars-b+a))\) depends on the six variables through their residues modulo the small integer \(k\) and through a slowly varying factor. Characters modulo \(k\) separate the residues, and a Mellin transform separates the slowly varying factor, so the major sum \(\mathcal Q_Y^{\rm maj}\) of [*Cauchy's inequality and the determinant equation*](cauchys-inequality-and-the-determinant-equation.md) becomes an integral of products of Dirichlet polynomials. Here the twisted cancellation of \(\alpha\) is finally used. It does not suffice by itself, because the frequencies range over an interval of length comparable to \(X\), where the mean square of the other polynomial is large. One group prime is therefore isolated from the marking product: where its polynomial is small, a mean value bound suffices, and where it is large, the frequencies are so sparse that the polynomial of \(\beta\) has small energy there. The lesson ends with the proof of Theorems 2.2 and 2.3 of [*The marked Type II estimate*](the-marked-type-ii-estimate.md).

**Prerequisites.** [*Cauchy's inequality and the determinant equation*](cauchys-inequality-and-the-determinant-equation.md), Sections 5 and 7; [*Primes, divisors, mean squares and rough numbers*](primes-divisors-mean-squares-and-rough-numbers.md), Lemmas 2.1, 3.1 and 3.2; [*Logarithmic phases at polynomial scales*](logarithmic-phases-at-polynomial-scales.md), Corollary 4.1; [*Birth distinctness and the minor moment*](birth-distinctness-and-the-minor-moment.md), Theorem 4.2; [*Long prime polynomials*](long-prime-polynomials.md), Corollary 2.2; [*Schwartz functions and Fourier inversion*](course:AN-01/prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017), Section F4; [*Lebesgue integration and smoothing — selected programme proofs*](course:AN-01/prerequisites/U011-free-foundations/banach-foundation-bridges), Sections 15.1 and 15.2.

The hypotheses of Theorem 2.2 of Lesson 1 hold, \(A_0\) is fixed, and \(Y\) lies in the range (2.1) of Lesson 7. Implied constants may depend on all fixed data, including \(K\), \(A_0\) and the constants of twisted cancellation.

## 1. Characters and the Mellin separation

**Proposition 1.1 (the major sum).** For every fixed \(D>0\), \(|\mathcal Q_Y^{\rm maj}|\ll XY\,L^{-D}\).

The proof occupies Sections 1–3.

*Arcs.* On the arc around \(h/k\) write \(\theta=h/k+\lambda/Y\) with \(|\lambda|\le2L^{A_0}\), so \(d\theta=d\lambda/Y\). There are at most \(L^{2A_0}\) arcs. Every variable of (5.5) of Lesson 7 is coprime to \(k\le L^{A_0}\): the group primes exceed \(e^{L^{0.1}}\), and \(m,n,r,s\) are rough. The function \((a,b,m,n,r,s)\)\(\mapsto e(h(bmn-ars-b+a)/k)\) on \(((\mathbb Z/k\mathbb Z)^\times)^6\) has modulus \(1\), so its expansion in products \(\chi_a(a)\chi_b(b)\chi_m(m)\chi_n(n)\chi_r(r)\chi_s(s)\) of characters modulo \(k\) has coefficients of modulus at most \(1\), at most \(\varphi(k)^6\le L^{6A_0}\) of them. It suffices to bound each arc and each character term by \(XYL^{-D-8A_0}\).

*The archimedean factor.* With \(t=bmn-ars\), the remaining factor is \(\psi(t/Y)e(\lambda(t-b+a)/Y)\)\(=\psi_\lambda(t/Y)e(-\lambda b/Y)e(\lambda a/Y)\), where \(\psi_\lambda(y)=\psi(y)e(\lambda y)\). Put \(w=bmn/(YX)\) and \(w'=ars/(YX)\); both lie in \([1,16]\) on the support of the coefficients, and \(t/Y=X(w-w')\). Fix a smooth \(\kappa\) with compact support, equal to \(1\) on \([0,\log16]\), and define

\[
\begin{gathered}
\Phi_\lambda(\zeta,z)=\psi_\lambda\bigl(Xe^z(e^{\zeta/X}-1)\bigr)\kappa(z).
\end{gathered}
\]

On the support of \(\psi\), \(|e^{\zeta/X}-1|\le5e^{-z}/X\), so \(\Phi_\lambda\) has compact support in a set independent of \(x\); each derivative in \(\zeta\) or \(z\) costs a factor \(O(1+|\lambda|)\). By Fourier inversion on \(\mathbb R^2\) (Section F4 of [*Schwartz functions and Fourier inversion*](course:AN-01/prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017)) and integration by parts, \(\Phi_\lambda(\zeta,z)=\iint F_\lambda(v,s')e^{i(v\zeta+s'z)}dv\,ds'\) with

\[
\begin{aligned}
|F_\lambda(v,s')|&\ll_j\Bigl(1+\frac{|v|}{L^{A_0+1}}\Bigr)^{-j}\\
&\quad\times\Bigl(1+\frac{|s'|}{L^{A_0+1}}\Bigr)^{-j}\quad(1.1)
\end{aligned}
\]

for every \(j\). At \(\zeta=X\log(w/w')\), \(z=\log w'\), and after the substitution \(v=t'/X\),

\[
\begin{aligned}
&\psi_\lambda\bigl(X(w-w')\bigr)=\frac1X\iint F_\lambda\Bigl(\frac{t'}X,s'\Bigr)\\
&\quad\times w^{it'}(w')^{i(s'-t')}dt'\,ds'.\quad(1.2)
\end{aligned}
\]

*The polynomials.* For real \(u\) define

\[
\begin{aligned}
B_\lambda(u)&=\frac1Y\sum_b\eta\Bigl(\frac bY\Bigr)e\Bigl(-\frac{\lambda b}Y\Bigr)\\
&\quad\times\frac{\chi_b(b)b^{iu}}{V_1\cdots V_K},\\
M_\alpha(u)&=\frac1{H_m}\sum_m\alpha_m\chi_m(m)m^{iu},\\
N_\beta(u)&=\frac1{H_n}\sum_n\beta_n\chi_n(n)n^{iu},
\end{aligned}
\]

and \(Q=B_\lambda M_\alpha N_\beta\); let \(Q'\) be the analogous product for \(a,r,s\), with \(e(+\lambda a/Y)\), \(\overline{\alpha_r}\), \(\overline{\beta_s}\) and the characters \(\chi_a,\chi_r,\chi_s\). Inserting (1.2) into the character term and summing over the six variables, the factors \((YX)^{-it'}\) and \((YX)^{-i(s'-t')}\) combine to \((YX)^{-is'}\), of modulus one, and the normalizations combine to \(Y^{-1}X^{-1}(YH_mH_n)^2=XY\). So the character term is \(XY\) times

\[
\begin{aligned}
&\int_{|\lambda|\le2L^{A_0}}\iint F_\lambda\Bigl(\frac{t'}X,s'\Bigr)(YX)^{-is'}\\
&\quad\times Q(t')\,Q'(s'-t')\,dt'\,ds'\,d\lambda .\quad(1.3)
\end{aligned}
\]

## 2. Mean squares and the energy

**Lemma 2.1.** \(|B_\lambda(u)|\le4\), and for every interval \(I\) of length \(Z\ge1\) and every translate,

\[
\begin{gathered}
\int_I|M_\alpha N_\beta|^2\le L^{C_4}\Bigl(1+\frac ZX\Bigr),\\
C_4=4C+5,\quad(2.1)
\end{gathered}
\]

and the same for the primed polynomials.

**Proof.** Since \(b\le4Y\) on the support, \(|B_\lambda|\le4\sum_bb^{-1}\prod_iV_i^{-1}\)\(=4\prod_i(V_i^{-1}\sum_{p\in\mathcal P_i}p^{-1})=4\). The product \(M_\alpha N_\beta\) is a Dirichlet polynomial over \(u=mn\le4X\) with coefficients of modulus at most \(L^{2C}\tau(u)/X\), so by Lemma 2.1 of Lesson 2 their squares sum to \(O(L^{4C+4}/X)\). Lemma 3.1 of Lesson 2 gives (2.1); a translate of \(I\) only twists the coefficients by unimodular factors. \(\square\)

*Truncation.* Put \(B_1=A_0+2\). For fixed \(s'\), split the \(t'\)-integral of \(|F_\lambda Q(t')Q'(s'-t')|\) into dyadic ranges \(|t'|\in[Z,2Z]\). By Cauchy's inequality and (2.1), each range contributes at most \(16L^{C_4}(1+2Z/X)\) times \(\sup|F_\lambda|\) there. For \(Z\ge XL^{B_1}\), (1.1) makes the sum of these contributions \(O(L^{-A'})\) for every \(A'\), uniformly in \(s'\); and the integral over \(|t'|\le XL^{B_1}\) is \(O(L^{C_4+B_1})\) uniformly in \(s'\). By (1.1) in \(s'\), the part with \(|s'|>L^{B_1}\) is \(O(L^{-A'})\) as well. On the remaining rectangle, Cauchy's inequality in \(t'\) and (2.1) for \(Q'\) bound the integral by \(O(L^{B_1}L^{(C_4+B_1)/2})\) times \(E^{1/2}\), where

\[
\begin{aligned}
&E=\int_{|t'|\le2XL^{B_1}}\bigl|B_\lambda(t')M_\alpha(t')\\
&\qquad\times N_\beta(t')\bigr|^2\,dt' .\quad(2.2)
\end{aligned}
\]

Hence Proposition 1.1 follows once \(E\ll L^{-A''}\) for every fixed \(A''\), uniformly in \(\lambda\) and the characters.

*Isolating one prime.* Write \(b=pb'\) with \(p\in\mathcal P_1\) and \(b'\) the product of the primes of the other groups, and split \(p\) into dyadic ranges \([P,2P)\); there are at most \(2L^{0.2}\) of them, and \(\log P\ge L^{0.1}-1\). Let \(f_\lambda(y)=\eta(y)e(-\lambda y)\). Fourier inversion (Section F4 of [*Schwartz functions and Fourier inversion*](course:AN-01/prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017)) for the smooth compactly supported function \(u\mapsto f_\lambda(e^u)\) gives \(f_\lambda(y)=\int\widehat f_\lambda(\xi)y^{i\xi}d\xi\) for \(y>0\), and two integrations by parts give \(\int|\widehat f_\lambda|\,d\xi\ll(1+|\lambda|)^2\ll L^{2A_0}\). Since \(f_\lambda(pb'/Y)=0\) unless \(pb'\in[Y,4Y]\), for \(p\in[P,2P)\) we may restrict \(b'\) to \((Y/(2P),4Y/P]\), and then

\[
\begin{gathered}
B_\lambda^{(P)}(u)=V_1^{-1}\int\widehat f_\lambda(\xi)Y^{-i\xi}\\
\times P_s(u+\xi)\,Q_P(u+\xi)\,d\xi,\\
P_s(u)=\frac1P\sum_{\substack{p\in\mathcal P_1\\ P\le p<2P}}\chi_b(p)p^{iu},\\
Q_P(u)=\frac PY\sum_{Y/(2P)<b'\le4Y/P}\frac{\chi_b(b')b'^{iu}}{V_2\cdots V_K}.
\end{gathered}
\]

As for \(B_\lambda\), \(|Q_P|\le4\). Put \(\Lambda=\int|\widehat f_\lambda(\xi)|\,d\xi\ll L^{2A_0}\). Cauchy's inequality over the at most \(2L^{0.2}\) dyadic ranges gives \(|B_\lambda(t')|^2\le2L^{0.2}\sum_P|B^{(P)}_\lambda(t')|^2\), and Cauchy's inequality for the \(\xi\)-integral with the weight \(|\widehat f_\lambda(\xi)|\), together with \(V_1\ge\frac12\), gives \(|B^{(P)}_\lambda(t')|^2\)\(\le64\Lambda\int|\widehat f_\lambda(\xi)|\,|P_s(t'+\xi)|^2d\xi\). Multiply by \(|M_\alpha(t')N_\beta(t')|^2\), integrate over \(|t'|\le2XL^{B_1}\) and interchange the two integrals of the nonnegative integrand (Tonelli's theorem; Sections 15.1 and 15.2 of [*Lebesgue integration and smoothing — selected programme proofs*](course:AN-01/prerequisites/U011-free-foundations/banach-foundation-bridges) prove it and Cauchy's inequality for integrals). Then \(E\le256L^{0.4}\Lambda^2\) times the supremum over \(P\) and \(\xi\) of the \(t'\)-integral below, so

\[
\begin{aligned}
&E^{1/2}\ll L^{0.2+2A_0}\\
&\quad\times\sup_{P,\xi}\Bigl(\int_{|t'|\le2XL^{B_1}}\bigl|P_s(t'+\xi)\\
&\qquad\times M_\alpha(t')N_\beta(t')\bigr|^2dt'\Bigr)^{1/2}.
\end{aligned}
\]

It remains to bound the last integral by \(L^{-A'''}\) for arbitrary \(A'''\), uniformly in \(\xi\in\mathbb R\) and in \(P\). Replacing the prime set by its translate in the frequency, we write \(P_s(t)\) for \(P_s(t+\xi)\); its coefficients still have modulus \(P^{-1}\).

## 3. Sparse frequencies

**Lemma 3.1 (sparse frequencies).** Let \(A_s>0\) be fixed, and let \(\mathcal I\) be the set of unit intervals \([l,l+1]\), \(l\in\mathbb Z\), that meet \(\{t:|t|\le2XL^{B_1},\ |P_s(t)|>L^{-A_s}\}\). Then

\[
\begin{gathered}
|\mathcal I|\le\exp\bigl(O(L^{0.91})\bigr),\\
\sum_{I\in\mathcal I}\sup_I|N_\beta|^2\ll L^{2C+1},\quad(3.1)
\end{gathered}
\]

uniformly in \(\xi\) and \(P\).

**Proof.** *The count.* Let \(Z=4XL^{B_1}\) and \(j=\lfloor\log Z/\log(2P)\rfloor\). Then \(P_s(t)^j=\sum_nc_nn^{it}\) over \(n\le(2P)^j\le Z\), where \(c_n\) is \(P^{-j}\) times a sum over the ordered \(j\)-tuples of primes with product \(n\) of unimodular numbers. An integer has at most \(j!\) such tuples, so

\[
\begin{gathered}
\sum_n|c_n|^2\le P^{-2j}j!\sum_n\#\{\text{tuples}\}\\
\le j!\,P^{-j},
\end{gathered}
\]

since there are at most \(P\) primes in \([P,2P)\). This bound uses the actual degree \(j\), which grows with \(x\). Choose in every \(I\in\mathcal I\) a point where \(|P_s|>L^{-A_s}\), and split these points into three classes according to \(l\bmod3\); each class is \(1\)-separated. Lemma 3.2 of Lesson 2, whose constant does not depend on the coefficients, gives for each class

\[
\begin{gathered}
L^{-2A_sj}\cdot\#\text{class}\le\sum|P_s^j|^2\\
\ll Z\,L^2\,j!\,P^{-j}.
\end{gathered}
\]

Here \(\log Z-j\log P\le\log(2P)+j\log2\), \(j\le\log Z/\log P\le3L^{0.9}\), \(\log j!\le j\log j\), and \(\log(2P)\le3L^{0.2}\). So the logarithm of the right side divided by \(L^{-2A_sj}\) is \(O(L^{0.9}\log L)\), which proves the first bound.

*The energy.* Choose in the closure of each \(I\in\mathcal I\) a point \(t_I\) where \(|N_\beta|\) attains its maximum, and split into the same three classes. Within a class, consider the map \(e\mapsto(\sum_ne_nn^{it_I})_I\) on sequences \(e\) supported on the integers of \([H_n,2H_n]\). The square of its norm is at most the largest absolute row sum of the matrix \(G_{IJ}=\sum_{H_n\le n\le2H_n}n^{i(t_I-t_J)}\). The diagonal entries are at most \(H_n+1\). For \(I\ne J\), \(1\le|t_I-t_J|\le Z+2\le x^2\), and Corollary 4.1 of [*Logarithmic phases at polynomial scales*](logarithmic-phases-at-polynomial-scales.md), with \(q=1\) and \(N=H_n\in[x^\delta,c_*x]\), gives \(|G_{IJ}|\ll H_n/|t_I-t_J|+H_nx^{-c}\). In a row, the points are \(1\)-separated, so \(\sum_J1/|t_I-t_J|\)\(\le4\sum_{1\le m\le Z+2}1/m\ll L\), and \(|\mathcal I|H_nx^{-c}=o(H_n)\) by the first part. So the row sums are \(O(H_nL)\). Applying the map to \(e_n=\beta_n\chi_n(n)/H_n\), whose squared norm is at most \(2L^{2C}/H_n\), gives \(\sum_I|N_\beta(t_I)|^2\ll L^{2C+1}\) for each class. \(\square\)

*Conclusion of the proof of Proposition 1.1.* Split the integral at the end of Section 2 according to \(|P_s(t)|\le L^{-A_s}\) or not. On the first set, (2.1) bounds it by \(L^{-2A_s}L^{C_4}(1+4L^{B_1})\). On the second set, which is contained in the union of the intervals of \(\mathcal I\), use \(|P_s|\le1\) and the twisted cancellation of \(\alpha\) (Definition 2.1 of Lesson 1, with the modulus bound \(L^{A_0}\), \(B=B_1\) and precision \(A\)): \(|M_\alpha(t)|\le C_{\rm tc}L^{-A}\) for all \(|t|\le2XL^{B_1}\). With Lemma 3.1 this part is at most \(C_{\rm tc}^2L^{-2A}\sum_{I\in\mathcal I}\sup_I|N_\beta|^2\ll L^{-2A+2C+1}\). Choosing \(A_s\) and \(A\) large proves the required bound for every \(A'''\), hence \(E\ll L^{-A''}\), and Proposition 1.1 follows from Section 2 and the count of arcs and characters. \(\square\)

Only \(M_\alpha\), not its primed counterpart, needs cancellation: the polynomial \(Q'\) enters through its mean square alone.

## 4. Proof of the theorems

**Proof of Theorem 2.2 of Lesson 1.** Let \(D_*\) and \(C\) be given, and put

\[
\begin{aligned}
D_1&=2D_*+2,\\
E_0&=D_1+4C+2,\\
A_0&=E_0+7,\\
K_0&=200(E_0+7)\\
&=200(2D_*+4C+11).
\end{aligned}
\]

Let \(K\ge K_0\) and let the band exponents be arbitrary in \((0.1,0.2)\). Define the major arcs with this \(A_0\). Theorem 4.2 of [*Birth distinctness and the minor moment*](birth-distinctness-and-the-minor-moment.md) gives \(|\mathcal Q_Y^{\rm min}|\ll XYL^{-D_1}\), and Proposition 1.1 with \(D=D_1\) gives \(|\mathcal Q_Y^{\rm maj}|\ll XYL^{-D_1}\), uniformly for \(Y\) in (2.1) of Lesson 7. By Proposition 7.1 of Lesson 7, \(|\mathfrak B|\le C'XL^{-D_*}\). The number \(K_0\) depends only on \(C\) and \(D_*\); all other dependence, including that on \(\delta\), \(c_*\), \(q\), \(K\), the \(a_i\) and the constants of twisted cancellation, enters only the constant \(C'\) and the threshold for \(x\). \(\square\)

**Proof of Theorem 2.3 of Lesson 1.** By Corollary 2.2 of [*Long prime polynomials*](long-prime-polynomials.md), the coefficient (2.5) of Lesson 1 satisfies the hypotheses of Theorem 2.2, with twisted cancellation constants depending only on \(\delta,c_*,C\) and \(A_0,B,A\), uniformly in the interval \(I\) and in \(v\). \(\square\)

The order of choices matches Section 4 of Lesson 1. The precision \(D_1\) of the Cauchy square is fixed by \(D_*\); the moment precision \(E_0\) adds the logarithmic size \(4C\) of the endpoint vectors; the contraction exponent \(G=E_0+4\) of a single step determines \(A_0\) through the clean edges and \(K\) through the dirty edges; and \(x\) is taken large last. The analytic precisions of Proposition 1.1, the depth of the Bonferroni truncations and the rank cutoff are internal to their lessons and impose no condition on \(K\).

## 5. Exercises

**17.1.** Let \(f\) be a function of modulus at most \(1\) on a finite abelian group \(\Gamma\). Show that its Fourier coefficients with respect to the characters of \(\Gamma\) have modulus at most \(1\), and that there are \(|\Gamma|\) of them.

**17.2.** Show that a product of \(j\) primes arises from at most \(j!\) ordered \(j\)-tuples of primes.

**17.3.** Verify the normalization \(Y^{-1}X^{-1}(YH_mH_n)^2=XY\) in (1.3).

**17.4.** Show that \(\int_{|t|\le XL^{B_1}}|N_\beta(t)|^2dt\) can be as large as \(L^{2C+B_1}H_m\) in order of magnitude, and explain why twisted cancellation of \(\alpha\) alone does not bound (2.2).

**17.5.** Check that \(K_0=200(2D_*+4C+11)\) satisfies the conditions \(A_0\ge E_0+7\) and \(K\ge200(E_0+7)\) of Theorem 4.2 of Lesson 16 when \(E_0=2D_*+4C+4\).

## 6. Solutions

**17.1.** \(f=\sum_\chi\widehat f(\chi)\chi\) with \(\widehat f(\chi)=|\Gamma|^{-1}\sum_xf(x)\overline{\chi(x)}\), whose modulus is at most the average of \(|f|\), hence at most \(1\). The characters of a finite abelian group are \(|\Gamma|\) in number. For \(\Gamma=((\mathbb Z/k\mathbb Z)^\times)^6\) this gives \(\varphi(k)^6\) coefficients.

**17.2.** By unique factorization the product determines the multiset of the primes, and a multiset of size \(j\) has at most \(j!\) orderings.

**17.3.** The sums over \(b,m,n\) and over \(a,r,s\) are \(YH_mH_n\) times the normalized polynomials, the arc measure is \(d\lambda/Y\), and (1.2) contributes \(1/X\). Since \(H_mH_n=X\), the product is \(Y^{-1}X^{-1}Y^2X^2=XY\).

**17.4.** By (3.1) of Lesson 2, the mean square over an interval of length \(2XL^{B_1}\) is about \(2XL^{B_1}\sum_n|\beta_n|^2/H_n^2\), which for \(|\beta_n|\asymp L^C\) on \(\asymp H_n\) integers is of order \(XL^{B_1+2C}/H_n=H_mL^{B_1+2C}\). Twisted cancellation gives \(|M_\alpha|^2\le C_{\rm tc}^2L^{-2A}\), and \(L^{-2A}H_m\) is still a power of \(x\). The isolated prime reduces the measure of the relevant frequencies from about \(X\) to \(x^{o(1)}\) unit intervals, where a pointwise count of the energy of \(N_\beta\) is possible.

**17.5.** \(A_0=E_0+7\) by definition, and \(K_0=200(E_0+7)\) with \(E_0+7=2D_*+4C+11\).

## References

- [PD] OpenAI, *The Poisson–Dirichlet law for prime predecessors*, OpenAI Math Release preprint, 24 September 2026, Section 5. https://github.com/openai/math/tree/main/preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026
