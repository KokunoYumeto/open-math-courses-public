# Weil's positivity criterion

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The explicit formula becomes a quadratic form when its test function is a convolution square. On the critical line that quadratic form is a sum of absolute squares. Away from the line, reflection couples two different evaluations and can give a negative value. Weil's criterion says that this distinction detects RH even if the test functions have compact support and their Mellin transforms satisfy any prescribed finite set of vanishing conditions.

The compact-support requirement has an arithmetic consequence: each individual test uses only finitely many primes. It does not give one fixed finite set of primes sufficient for all tests. Our proof of the converse constructs a test with the required values, controls its values at all other zeros, and preserves exact vanishing when a Gaussian auxiliary function is cut off.

After the positivity criterion and its character versions, we prove Connes's semilocal trace formula. For finitely many places, two cutoffs make the scaling operator trace class. Mellin transformation separates its trace into the length of a cutoff interval and the logarithmic derivative of a Fourier phase. Tate's local functional equations identify that derivative with the local distributions already calculated in the second lesson.

## 1. Convolution squares and the sign convention

On \(\mathbb R_+^\times\), with measure \(d^*x=dx/x\), set

\[
(g*h)(x)=\int_0^\infty g(y)h(x/y)\,\frac{dy}{y},
\qquad g^\sharp(x)=x^{-1}g(x^{-1}),
\qquad G(s)=\widetilde g(s).
\tag{1.1}
\]

Changing variables and applying Fubini gives

\[
\widetilde{g*h}(s)=\widetilde g(s)\widetilde h(s),
\qquad
\widetilde{\bar g^\sharp}(s)=\overline{G(1-\bar s)}.
\tag{1.2}
\]

For \(g\in C_c^\infty(\mathbb R_+^\times)\) put \(f=g*\bar g^\sharp\). It is again smooth with compact support, and

\[
\widetilde f(s)=G(s)\overline{G(1-\bar s)}.
\tag{1.3}
\]

The explicit formula in the first lesson therefore reads

\[
\mathcal W(g):=\sum_v W_v(g*\bar g^\sharp)
=G(0)\overline{G(1)}+G(1)\overline{G(0)}-Q(g),
\tag{1.4}
\]

where

\[
Q(g)=\sum_\rho G(\rho)\overline{G(1-\bar\rho)}.
\tag{1.5}
\]

The sum is absolutely convergent, as the Mellin bound below proves. The zero multiset is preserved by \(\tau(\rho)=1-\bar\rho\), including multiplicities. Thus changing \(\rho\) to \(\tau(\rho)\) conjugates (1.5); \(Q(g)\) is real. In particular, when \(G(0)=G(1)=0\), our arithmetic sign convention is

\[
\mathcal W(g)=-Q(g). \tag{1.6}
\]

Weil's positive zero form and the nonpositive arithmetic form used here are the same criterion with this minus sign.

## 2. Compact support and Mellin decay

**Lemma 2.1.** If \(\operatorname{supp}g\subset[a,b]\), with \(0<a<b\), then

\[
\operatorname{supp}(g*\bar g^\sharp)
\subset\operatorname{supp}g\cdot(\operatorname{supp}g)^{-1}
\subset[a/b,b/a].
\tag{2.1}
\]

Consequently \(W_p(f)=0\) if \(\operatorname{supp}f\subset(p^{-1},p)\).

*Proof.* A nonzero integrand in (1.1) requires \(y\in\operatorname{supp}g\) and \(y/x\in\operatorname{supp}g\); hence \(x\) is a ratio of two support points. Taking closures proves (2.1). A local prime term evaluates only \(f(p^m)\) and \(p^{-m}f(p^{-m})\). Neither argument meets the given open support interval, so every summand is zero. ∎

For support in \([A^{-1/2},A^{1/2}]\), only primes \(p<A\) can contribute. At the boundary \(p=A\), if it is prime, smooth compact support forces \(f(A)=f(A^{-1})=0\) as well. Thus the strict inequality is valid also when the containing support interval is closed.

**Lemma 2.2 (Mellin Paley–Wiener bound).** For \(g\in C_c^\infty([a,b])\), \(G\) is entire and, for every integer \(N\geq0\),

\[
|G(\sigma+it)|
\leq C_{N,g}\max(a^\sigma,b^\sigma)(1+|t|)^{-N}.
\tag{2.2}
\]

The constant is independent of \(\sigma,t\).

*Proof.* Put \(A=\log a\), \(B=\log b\), and \(h(u)=g(e^u)\). Then
\(G(s)=\int_A^B h(u)e^{su}\,du\).
Differentiation under this finite integral proves that \(G\) is entire and has exponential type. All derivatives of \(h\) vanish at the endpoints of any containing compact interval. For \(s\ne0\), integration by parts \(N\) times gives

\[
G(s)=\frac{(-1)^N}{s^N}\int_A^B h^{(N)}(u)e^{su}\,du.
\]

Its absolute value is at most
\(|s|^{-N}\|h^{(N)}\|_1\max(e^{A\sigma},e^{B\sigma})\).
For \(|t|\geq1\), use \(|s|\geq|t|\); for \(|t|<1\), use the original integral and absorb \(2^N\) into the constant. This proves (2.2). ∎

With \(0\leq\Re\rho\leq1\), the factor involving \(a,b\) is bounded. Since the zeta zero count is \(O(T\log(T+2))\), (2.2) makes (1.5) absolutely convergent. The zero count, functional equation and gamma inputs are supplied by the same existing planned internal zeta lessons identified in the first lesson; their public proof completion is not asserted here.

## 3. A compact test with one prescribed zero value

An exponential-type bound alone is not a proof that arbitrary interpolation is possible. We construct the function explicitly.

**Lemma 3.1 (isolation with exact vanishing).** Let \(Z\) be a locally finite multiset in \(0\leq\Re s\leq1\), with \(O(T\log(T+2))\) points of height at most \(T\), counted with multiplicity. Fix a distinct point \(\rho_0\in Z\), and a finite set \(F\) not containing \(\rho_0\). Fix \(R>2\). There exists \(g\in C_c^\infty(\mathbb R_+^\times)\) such that

\[
G(\rho_0)=1,\qquad G|_F=0,\qquad
G(\rho)=0
\quad\text{for every other distinct }\rho\in Z
\text{ with }|\Im\rho-\Im\rho_0|\leq R,
\tag{3.1}
\]

provided \(F\) does not contain the target. The squared sum of \(|G(\rho)|\), with multiplicity, over zeros outside that band can be made arbitrarily small.

*Proof.* The band contains finitely many distinct points. Let \(E\) be their union with \(F\), omitting \(\rho_0\), and put \(P(s)=\prod_{z\in E}(s-z)\). Then \(P(\rho_0)\ne0\). Consider first the auxiliary entire function

\[
H_\varepsilon(s)=\frac{P(s)}{P(\rho_0)}
\exp\left(\frac{(s-\rho_0)^2}{\varepsilon^2}\right),
\qquad0<\varepsilon\leq1.
\tag{3.2}
\]

It has the values in (3.1). Write \(v=\Im\rho-\Im\rho_0\). Since the real parts differ by at most \(1\), outside the band

\[
|H_\varepsilon(\rho)|^2
\leq C(1+|\rho|)^{2\deg P}
\exp\left(\frac{2(1-v^2)}{\varepsilon^2}\right)
\leq C e^{-(R^2-2)/\varepsilon^2}
(1+|\rho|)^{2\deg P}e^{-v^2}.
\tag{3.3}
\]

The last inequality uses \(|v|>R\) and \(\varepsilon\leq1\). The sum of the last factor over \(Z\) is finite by the zero count. Thus the squared tail tends to zero as \(\varepsilon\downarrow0\).

Function (3.2) is not itself a compact-support Mellin transform. Fix \(\varepsilon\) after making its tail small, and use the Gaussian bilateral Laplace transform

\[
b_\varepsilon(u)=\frac{\varepsilon}{2\sqrt\pi}
e^{-\varepsilon^2u^2/4-\rho_0u},
\qquad
\int_\mathbb R b_\varepsilon(u)e^{su}\,du
=e^{(s-\rho_0)^2/\varepsilon^2}.
\tag{3.4}
\]

Choose \(\chi\in C_c^\infty(\mathbb R)\), equal to \(1\) on \([-1,1]\) and zero outside \([-2,2]\). The transforms
\(B_L(s)=\int\chi(u/L)b_\varepsilon(u)e^{su}\,du\)
converge to the right side of (3.4), with every polynomial vertical weight, uniformly for \(0\leq\Re s\leq1\). Indeed all derivatives of the Gaussian tail, multiplied by \(e^{\sigma u}\), have \(L^1\) norms tending to zero uniformly in this strip. Derivatives of \(\chi(u/L)\) are supported in the same tail and carry bounded factors \(L^{-j}\). Integration by parts \(N\) times therefore gives

\[
\sup_{0\leq\sigma\leq1,\ t\in\mathbb R}
(1+|t|)^N|B_L(\sigma+it)-B(\sigma+it)|\longrightarrow0.
\tag{3.5}
\]

Apply \(P(-d/du)\) to \(\chi(u/L)b_\varepsilon(u)\). Its transform is \(P(s)B_L(s)\); this function vanishes **exactly** on \(E\) for every \(L\). Its value at \(\rho_0\) tends to \(P(\rho_0)\), so it is nonzero for large \(L\). Divide by that value. Finally set \(g(e^u)\) equal to this normalized compactly supported smooth function.

The resulting transforms converge to \(H_\varepsilon\) with weight \((1+|t|)^2\), by choosing \(N>\deg P+2\) in (3.5). Since
\(\sum_{\rho\in Z}(1+|\Im\rho|)^{-4}<\infty\),
they converge in squared-sum norm on \(Z\). Their tail is therefore as small as desired, while every condition in (3.1) remains exact. ∎

The same proof gives the frequently useful pointwise formulation: for any prescribed \(\eta>0\), the nontarget values can be bounded by \(\eta|\rho-\rho_0|^{-2}\), outside a fixed sufficiently large disk, and can be set to zero at the other zeros inside it. In (3.3), multiply by \(|\rho-\rho_0|^4\); the Gaussian still dominates every polynomial. In (3.5), retain the same weighted uniform bound. A band may contain extra points beyond the disk; their values are simply set to zero too.

The support radius \(L\) is chosen after the auxiliary Gaussian width. It can be very large. Compactness gives a finite witness, not a uniform small-support witness.

## 4. The full converse with finitely many vanishing conditions

**Theorem 4.1 (Weil's compact-support criterion).** Let \(F\subset\mathbb C\) be any finite set containing \(0,1\), disjoint from the nontrivial zeta zeros. Then

\[
\boxed{\mathrm{RH}\quad\Longleftrightarrow\quad
\mathcal W(g)\leq0
\text{ for every }g\in C_c^\infty(\mathbb R_+^\times)
\text{ with }G|_F=0.}
\tag{4.1}
\]

*Proof.* Under RH, \(1-\bar\rho=\rho\). Equations (1.5)–(1.6) give
\(\mathcal W(g)=-\sum_\rho|G(\rho)|^2\leq0\).

Conversely suppose \(\rho_0\) is off the critical line. Then
\(\rho_1=1-\bar\rho_0\ne\rho_0\)
is a zero of the same multiplicity \(m\), with the same imaginary part. Select one band of radius \(R>2\) about that imaginary part. Use Lemma 3.1 twice: obtain \(G_0,G_1\) equal to \(1\) at their respective targets, zero at the other target, zero at every remaining band zero and on \(F\), and each with outside squared-sum norm less than \(\eta^2\). Let \(g=g_0-g_1\). Its transform takes the values \(1,-1\) at \(\rho_0,\rho_1\); all other band evaluations vanish.

The pair's contribution to \(Q(g)\) is \(-2m\). Reflection \(\tau\) preserves the outside band and its multiplicities, so Cauchy–Schwarz gives

\[
\left|\sum_{\rho\ {\rm outside}}
G(\rho)\overline{G(\tau\rho)}\right|
\leq\sum_{\rho\ {\rm outside}}|G(\rho)|^2
<4\eta^2.
\tag{4.2}
\]

Choose \(4\eta^2<2m\). Then \(Q(g)<0\), while \(G|_F=0\). Equation (1.6) gives \(\mathcal W(g)>0\), contradicting the proposed sign. Every step uses an actual compactly supported smooth test. ∎

This proves the finite-vanishing extension discussed by Connes and Consani in their appendix *Positivity criterion*, including the compact interpolation step referred there to Yoshida. The disjointness condition on \(F\) is essential to the construction: if a target were also prescribed to vanish, its required value \(1\) would be impossible.

## 5. Two examples of support and spectral localization

If \(g\) is supported in \([2^{-1/2},2^{1/2}]\), then \(f\) is supported in \([1/2,2]\). Smoothness makes both endpoint values zero. No prime term enters, including the prime \(2\). Thus \(\mathcal W(g)=W_{\mathbb R}(f)\) is purely archimedean. The next lesson studies this small-support form in detail.

For a spectral localization example, assume RH and write \(\gamma_1\approx14.1347\) for the first positive ordinate. Let \(b\) be a nonzero real, even, smooth bump supported in \([-1,1]\), with positive integral, and begin with
\(h_L(u)=e^{-u/2}b(u/L)\cos(\gamma_1u)\).
Its Mellin transform on the critical line is

\[
\frac L2\left\{\widehat b(L(t-\gamma_1))
+\widehat b(L(t+\gamma_1))\right\},
\tag{5.1}
\]

where \(\widehat b(t)=\int b(u)e^{itu}\,du\). Apply the polynomial differential operator whose Mellin multiplier is \(s(s-1)\), imposing vanishing at \(0,1\). Normalize so that the resulting \(G_L(1/2+i\gamma_1)=1\). Evenness and reality give the same value at the negative ordinate, because
\(s(s-1)=-(1/4+t^2)\) on the critical line.

Every other distinct zero evaluation tends to zero, while their squared sum tends to zero: rapid decay of \(\widehat b\), the positive distance to the nearest other ordinate, and the zero count give a summable majorant after choosing a power greater than \(4\). Thus

\[
\mathcal W(g_L)\longrightarrow-2m_1,
\tag{5.2}
\]

where \(m_1\) is the multiplicity of the first positive zero. If it is simple, the limit is \(-2\). This explains the approximation by the two first-zero absolute squares. The support expands with \(L\), so this localization example does not simultaneously have fixed small support.

The existing lesson *Weil's proof for curves and what is missing over the integers* in *The field with one element* proves a Gaussian-type criterion in its Theorem 6.4. Theorem 4.1 adds compact support and arbitrary admissible finite vanishing conditions; its proof above does not assume that the Gaussian auxiliary transform itself is of Paley–Wiener type.

## 6. Characters and idèle classes

### All Dirichlet characters modulo one modulus

Let \(B=(\mathbb Z/q\mathbb Z)^\times\), with probability counting measure. For a smooth compactly supported \(g(b,x)\), define the character Mellin coefficient

\[
G_\chi(s)=\frac1{\varphi(q)}
\sum_{b\in B}\int_0^\infty g(b,x)\chi(b)x^s\,\frac{dx}{x}.
\tag{6.1}
\]

Convolution is on \(B\times\mathbb R_+^\times\), and the involution is
\(g^*(b,x)=x^{-1}\overline{g(b^{-1},x^{-1})}\).
The coefficient of \(g*g^*\) is
\(G_\chi(s)\overline{G_\chi(1-\bar s)}\).
This follows by the same substitutions as (1.2), with character orthogonality in the finite group.

Define the combined zero form

\[
Q_q(g)=\sum_{\chi\bmod q}\sum_{\rho\ {\rm of}\ \chi^*}
G_\chi(\rho)\overline{G_\chi(1-\bar\rho)}.
\tag{6.2}
\]

Here each character is reduced to its primitive inducing character. The corresponding arithmetic form is obtained from lesson 2 by using, in each component, \(P_\chi+E_\chi-A_{q_\chi,a_\chi}\); the single conductor-\(1\) component also has the pole pair. On functions with \(G_{\chi_0}(0)=G_{\chi_0}(1)=0\), the total arithmetic form equals \(-Q_q(g)\).

**Proposition 6.1.** GRH for all primitive functions inducing characters modulo \(q\) is equivalent to \(Q_q(g)\geq0\) for all such tests.

*Proof.* Under GRH every summand in (6.2) is an absolute square. Conversely choose a character \(\chi\) and use
\(g(b,x)=\bar\chi(b)k(x)\).
Orthogonality makes the only nonzero coefficient \(G_\chi=\widetilde k\). The zero multiset of this primitive function is invariant under \(s\mapsto1-\bar s\), by its functional equation and conjugation, and has the zero-count bound of lesson 2. If an off-line pair exists, the proof of Theorem 4.1 constructs \(k\) with a negative zero form. For the principal component impose the two additional vanishing conditions; for other components no pole conditions are necessary. This contradicts positivity. ∎

Requiring vanishing at \(0,1\) in **every** component gives an equivalent criterion, since the same construction imposes any finite set disjoint from the completed zeros. The missing Euler factors are retained in the arithmetic form rather than treating their boundary zeros as primitive nontrivial zeros.

### Weil's idèle-class distribution

For a number field \(k\), use the norm splitting and Mellin-character convention of lesson 2, Section 7. Define on \(C_c^\infty(C_k)\)

\[
D(h)=\widehat h(0)+\widehat h(1)-\sum_vW_v(h).
\tag{6.3}
\]

Weil's idèlic explicit formula, proved there, identifies this as

\[
D(h)=\sum_{\chi\in\widehat{C_k^1}}\sum_{\rho\ {\rm of}\ \Lambda_\chi}
\widehat h(\chi,\rho).
\tag{6.4}
\]

With \(g^*(u)=|u|^{-1}\overline{g(u^{-1})}\), its evaluation on \(g*g^*\) is the sum of the character zero forms. The character and zero sums are absolutely convergent by the fixed-level rapid Fourier decay and uniform zero bound proved in that lesson.

**Proposition 6.2 (Weil's idèle criterion).** Every unitary Hecke \(L\)-function of \(k\) satisfies RH if and only if \(D(g*g^*)\geq0\) for every \(g\in C_c^\infty(C_k)\).

*Proof.* The forward direction gives an absolute square in every component of (6.4). For the converse fix a character of \(C_k^1\), and use \(g(u)=\bar\chi(u)k(|u|)\). Character orthogonality isolates its Hecke function. Its zeros lie in the same bounded strip, satisfy the zero count of lesson 2, and are invariant under \(s\mapsto1-\bar s\). Lemma 3.1 and the off-line-pair argument therefore produce a negative form if any such zero exists. The trivial norm component's poles have already been subtracted in the definition (6.3), so no moment restriction is needed for this zero-form criterion. ∎

To express positive type with the usual unitary convolution involution, apply the algebra automorphism \(g(u)\mapsto|u|^{1/2}g(u)\). It changes \(g^*\) into \(\overline{g(u^{-1})}\), and the critical-line Mellin evaluations become Fourier evaluations. This is the Fourier–Mellin dictionary behind Weil's 1952 idèle-class formulation. The ordinary real positivity here is a property of the whole distribution; it does not assert positivity of each individual local term.

## 7. A Hilbert space for finitely many places

Let \(k\) be a global field, and let \(S\) be a nonempty finite set of its places, containing all infinite places in the number-field case. Put

\[
A_S=\prod_{v\in S}k_v,\qquad J_S=\prod_{v\in S}k_v^\times,\qquad
\Gamma=\mathcal O_S^\times
=\{q\in k^\times:|q|_v=1\text{ for }v\notin S\},
\qquad C_S=J_S/\Gamma.
\tag{7.1}
\]

The product norm is \(|x|=\prod_{v\in S}|x_v|_v\). The product formula gives \(|q|=1\) for \(q\in\Gamma\). The norm-one group \(K_S=\ker(|\cdot|:C_S\to\mathbb R_+^\times)\) is compact.

Here are the precise structural inputs and their relation to this setting. For number fields we use finiteness of the ideal class group and Dirichlet's unit lattice, the results used in lesson 3, *Idèles and the idèle class group*, of *Adèles, idèles and Tate's thesis*. These are existing planned internal prerequisites; their public proof completion is not asserted here. They imply the \(S\)-unit statement as follows. For each finite place \(v\in S\), a positive power of its prime ideal is principal. A generator of that power is an \(S\)-unit. Its valuation at \(v\) is nonzero and its valuations at the other finite places are zero. These generators supply all the finite-place directions, up to finite index. The ordinary unit lattice supplies the remaining archimedean directions. Thus

\[
q\longmapsto(\log|q|_v)_{v\in S}
\tag{7.2}
\]

has finite kernel and is a full lattice in \(\sum_v y_v=0\). The kernel consists of roots of unity. The local norm-one unit groups are compact, so a bounded lattice fundamental region and those unit groups give compactness of \(K_S\). In particular \(C_S\simeq K_S\times\mathbb R\), after choosing a splitting and writing the second coordinate as \(r=\log|x|\).

For completeness, the function-field structure needed for the same trace theorem has an elementary adelic proof. Let the constant field have order \(q\). Choose a separating element \(t\), so that \(k/\mathbb F_q(t)\) is finite separable. The additive quotient
\(\mathbb A_{\mathbb F_q(t)}/\mathbb F_q(t)\) is compact: subtract the finitely many principal parts at finite irreducible polynomials by partial fractions, then subtract the polynomial part at infinity. The remaining representative lies in
\(\prod_{p\text{ finite}}\mathcal O_p\times t^{-1}\mathcal O_\infty\), a compact set. It meets the diagonal rational-function field only at zero. A field basis of \(k/\mathbb F_q(t)\) gives a topological additive isomorphism
\(\mathbb A_k\simeq\mathbb A_{\mathbb F_q(t)}^{[k:\mathbb F_q(t)]}\), carrying \(k\) to \(\mathbb F_q(t)^{[k:\mathbb F_q(t)]}\). To check the restricted products in this assertion, away from finitely many primes an integral basis and its inverse have integral coordinates; at the remaining primes either basis gives equivalent finite-dimensional local topologies. Hence \(\mathbb A_k/k\) is compact and \(k\) is discrete.

If a compact open additive box \(B\subset\mathbb A_k\) has volume exceeding the volume of that quotient, two points of \(B\) have the same image in the quotient. Indeed integrate the number of representatives in \(B\) over a fundamental region; if it were at most one, the volume of \(B\) could not exceed that region's volume. Since \(B-B=B\), this gives a nonzero element of \(k\cap B\). For a divisor \(D\), the box
\(B_D=\prod_v\{x:\operatorname{ord}_v x\geq-D_v\}\)
has volume \(c q^{\deg D}\), where \(c>0\) is fixed. Choose one place \(v_0\) and an integer \(N\) with \(c q^{N\deg v_0}\) exceeding the quotient volume. Every divisor \(D\) of degree zero then admits \(0\ne f\in B_{D+Nv_0}\cap k\). Thus \(D+Nv_0+\operatorname{div}(f)\) is effective of the fixed degree \(N\deg v_0\).

There are only finitely many effective divisors of that degree. A place of \(k\) of bounded degree lies above a place of \(\mathbb F_q(t)\) of bounded degree; there are finitely many such base places, and finitely many places above each. This proves finiteness of the degree-zero divisor class group. For \(v\in S\setminus\{v_0\}\), with \(v_0\) now chosen in \(S\), a positive multiple of
\((\deg v_0)v-(\deg v)v_0\) is therefore principal. Its generator is an \(S\)-unit. These generators span, up to finite index, the lattice of integer valuations satisfying \(\sum_v(\deg v)n_v=0\). Its kernel is finite: an element with every valuation zero has all its powers in the compact box \(B_0\); the discrete set \(k\cap B_0\) is finite, so two powers coincide. This proves the \(S\)-unit lattice and compactness of \(K_S\) in this case too. The norm image is \(e^{a\mathbb Z}\), where \(a>0\) is the positive generator of the subgroup of \(\mathbb R\) generated by \((\deg v)\log q\), \(v\in S\). Choosing one element of norm \(e^a\) gives \(C_S\simeq K_S\times a\mathbb Z\).

Normalize multiplicative measure on \(C_S\) by mass one on \(K_S\), and by \(dr\) on the real norm coordinate, or \(a\) times counting measure on \(a\mathbb Z\). This is exactly the normalization for which long norm intervals have volume asymptotic to their logarithmic length. Fix additive characters \(\alpha_v\), self-dual additive measures, and the product Fourier transform \(\mathscr F\) on \(A_S\).

The quotient \(X_S=A_S/\Gamma\) can have a complicated topology. Its required Hilbert space is nevertheless concrete. For a Schwartz–Bruhat function \(\phi\) define

\[
E_0\phi(x)=\sum_{q\in\Gamma}\phi(qx),\qquad
\|\phi\|_{X_S}^2=\int_D|E_0\phi(x)|^2\,dx,
\tag{7.3}
\]

where \(D\subset J_S\) is a fundamental region and \(dx\) is the quotient of the self-dual additive measure. The complement \(A_S\setminus J_S\) has additive measure zero. Multiplication by \(\Gamma\) preserves additive measure. There is a positive constant \(\rho\) with \(dx=\rho|x|\,d^*x\) on \(D\).

**Lemma 7.1.** Formula (7.3) is finite, and

\[
\langle\phi_1,\phi_2\rangle_{X_S}
=\sum_{q\in\Gamma}
\langle\phi_1,U(q)\phi_2\rangle_{L^2(A_S)},\qquad
U(q)\phi(x)=\phi(q^{-1}x).
\tag{7.4}
\]

The series is absolutely convergent. The Fourier transform induces a unitary involution on the separated completion of (7.3), and that completion is unitarily isomorphic to \(L^2(C_S,d^*x)\).

*Proof.* Choose a lattice word length on \(\Gamma\). The sum of the coordinates in (7.2) is zero, so
\[
\sum_v(\log|q|_v)^+=\frac12\sum_v|\log|q|_v|
\geq c\,\operatorname{length}(q)
\]
outside the finite kernel. For two characteristic functions of fixed local boxes, the volume of their intersection after scaling by \(q\) is at most a constant times
\(\prod_v\min(1,|q|_v^{-1})\), which is exponentially small in that length. For Schwartz functions use a sum of such box majorants with coefficients decreasing faster than every power of the box radius. The radii contribute only polynomial factors; summing them leaves the same exponential bound with a fixed constant. Thus the series of absolute inner products in (7.4) converges. Expanding (7.3), unfolding one of its two sums from \(D\) to \(J_S\), and applying this absolute bound proves (7.4).

Fourier transformation preserves the additive inner product and sends \(U(q)\) to \(U(q^{-1})\), since \(|q|=1\). It therefore preserves (7.4). Its square is reflection by \(-1\), which acts trivially on the quotient because \(-1\in\Gamma\). Finally the map
\[
\phi\longmapsto \rho^{1/2}|x|^{1/2}E_0\phi(x)
\tag{7.5}
\]
is isometric into \(L^2(C_S,d^*x)\). Its image is dense. To see this, lift a smooth compactly supported function on \(C_S\) to \(J_S\) using finitely many relatively compact coordinate neighborhoods and a smooth partition of unity. The discreteness of \(\Gamma\) makes each neighborhood an evenly covered set. Multiply the lift by \(\rho^{-1/2}|x|^{-1/2}\) before periodizing. Extended by zero, the resulting function is Schwartz–Bruhat on \(A_S\), because its support is compact and bounded away from every coordinate zero. Its image under (7.5) is the prescribed function. Such functions are dense. ∎

The unnormalized scaling \(U(\lambda)\) has operator norm \(|\lambda|^{1/2}\). Under (7.5) it becomes \(|\lambda|^{1/2}\) times unitary translation on \(C_S\). Thus
\[
U(h)=\int_{C_S}h(\lambda)U(\lambda)\,d^*\lambda
\tag{7.6}
\]
is bounded for smooth compactly supported \(h\).

## 8. Mellin transformation of the two cutoffs

First take a number field, so the norm coordinate is \(r\in\mathbb R\). Expand on the compact group \(K_S\), with characters \(\chi\), extended to be trivial on the chosen norm splitting. Use the unitary transform
\[
\mathcal M_\chi\psi(s)
=\frac1{\sqrt{2\pi}}\int_{K_S}\int_{\mathbb R}
\psi(c,r)\overline{\chi(c)}e^{-isr}\,dr\,dc.
\tag{8.1}
\]
The scaling integral is diagonal in this representation, with multiplier
\[
m_\chi(s)=\int_{C_S}h(\lambda)|\lambda|^{1/2}
\overline{\chi(\lambda)}|\lambda|^{-is}\,d^*\lambda.
\tag{8.2}
\]

We use Tate's local functional equations in lessons 7 and 8 of *Adèles, idèles and Tate's thesis*, already exact planned prerequisites of the second lesson. To fix the convention completely, write their local factor as
\[
Z_v(\mathscr F_v\phi,\omega^{-1},1-z)
=\gamma_v(\omega,z,\alpha_v)Z_v(\phi,\omega,z),\quad
Z_v(\phi,\omega,z)=\int_{k_v^\times}
\phi(x)\omega(x)|x|_v^z\,d^\times x.
\tag{8.3}
\]
Any constant normalization of \(d^\times x\) cancels here. On \(\Re z=1/2\), the factor has modulus one for unitary \(\omega\). Unfold (7.5) in (8.1), first for a product of local Schwartz functions. Equation (8.3) at each place gives
\[
(\mathcal M\mathscr F\psi)_\chi(s)
=u_\chi(s)(\mathcal M\psi)_{\bar\chi}(-s),\qquad
u_\chi(s)=\prod_{v\in S}
\gamma_v(\chi_v,1/2+is,\alpha_v).
\tag{8.4}
\]
The product of local integrals converges absolutely on this line. Finite sums of product Schwartz functions are dense; Lemma 7.1 then extends (8.4) to the whole Hilbert space. In particular no assertion about RH is needed to obtain its Fourier phase.

Let \(V\) be multiplication by \(u_\chi(s)\), and let \(J\) reflect \(s\) and conjugate the character index as in (8.4). Thus \(\mathscr F=VJ\). Put \(L=\log\Lambda\), and let \(P_L\) multiply by \(1_{r\leq L}\). Its Fourier conjugate is
\[
\widehat P_L=\mathscr F P_L\mathscr F^{-1}
=V\,1_{r\geq-L}\,V^*.
\tag{8.5}
\]

At any fixed finite level, \(h\) has only a finite group of nonarchimedean angular variables and finitely many torus directions. Repeated integration by parts in those torus directions and in \(r\) makes \(m_\chi(s)\) rapidly decreasing in both the torus frequency and \(s\). The local factors have a useful uniform bound: every derivative of \(u_\chi\) grows at most polynomially in \(1+|s|+\operatorname{frequency}(\chi)\), at that level. At a finite place the unramified factor is a quotient of \(1-\omega(\varpi)q_v^{-1/2-is}\) and its conjugate, whose denominator has absolute value at least \(1-q_v^{-1/2}\); a ramified factor is a constant phase times an exponential in \(s\). Its conductor is bounded at the fixed level. At the infinite places the factors are gamma quotients with positive real gamma arguments. Differentiated Stirling estimates and the digamma series give logarithmic bounds for their first logarithmic derivatives and polynomial bounds for all higher ones, uniformly as the angular index varies. Hence \(m_\chi u_\chi\) and \(m_\chi\bar u_\chi\) are Schwartz multipliers with seminorms decreasing faster than every power of that index.

## 9. Why the cutoff operator is trace class

We supply the operator argument before calculating a diagonal. On \(L^2(\mathbb R,dr)\), let \(P=1_{r\leq0}\), and let \(B\) be a convolution operator with Schwartz Fourier multiplier \(m\).

**Lemma 9.1.** The commutator \([P,B]\) is trace class. If \(I\) is a bounded interval, \(1_I B\) is trace class as well. Their trace norms are bounded by finitely many Schwartz seminorms of \(m\).

*Proof.* Write the inverse transform kernel of \(B\) as \(b(r-t)\). The commutator has only the two off-diagonal blocks \(r\leq0<t\) and \(t\leq0<r\). Reflecting the negative coordinate turns each block into a kernel \(b(\pm(r+t))\) on \(r,t\geq0\). Choose a smooth function equal to one on \([0,\infty)\) and zero on \((-\infty,-1]\). Multiplying by this function in each variable extends the kernel to a Schwartz function on \(\mathbb R^2\): on its support, \(r+t\) controls the size of both variables except in a bounded region.

A Schwartz-kernel operator \(T\) on the full line is trace class. Set \(A=1+r^2-d^2/dr^2\). The kernel of \(AT\) is square integrable, so \(AT\) is Hilbert–Schmidt. The normalized Hermite functions diagonalize \(A\), with eigenvalues \(2n+2\), making \(A^{-1}\) Hilbert–Schmidt. Their completeness can be checked without a spectral assumption: if \(f\) is orthogonal to every polynomial times \(e^{-r^2/2}\), the entire function \(\int f(r)e^{-r^2/2}e^{zr}\,dr\) has all derivatives zero at zero. It vanishes identically; uniqueness of the Fourier transform then gives \(f=0\). The Hermite eigenvalue calculation follows by differentiating their Rodrigues formula. Thus \(T=A^{-1}(AT)\) is a product of two Hilbert–Schmidt operators. Such a product is trace class: in an orthonormal basis expand it as a sum of rank-one operators and use Cauchy–Schwarz to bound the sum of their norms by the product of the Hilbert–Schmidt norms. Restricting the two variables to half-lines preserves trace class. This proves the first assertion.

For the second assertion choose a smooth compactly supported function equal to one on \(I\). Its product with \(b(r-t)\) is a Schwartz kernel on the full plane, since \(r\) is bounded and \(b\) decreases rapidly in \(r-t\). Restrict its output to \(I\). The same proof applies. All the displayed Hilbert–Schmidt bounds use only finitely many weighted kernel derivatives, giving the stated seminorm estimates. ∎

Suppose \(V\) is a unitary Fourier multiplier \(u\) with the derivative bounds of Section 8. Since \(B\) commutes with \(V\),
\[
[V^*,P]VB=V^*[P,VB]-[P,B].
\tag{9.1}
\]
Both commutators on the right are trace class by Lemma 9.1. On one character component, unitary conjugation by \(V\) changes the cutoff operator
\(R_\Lambda U(h)=\widehat P_LP_L B\) into
\[
1_{r\geq-L}V^*P_LVB
=1_{[-L,L]}B+1_{r\geq-L}[V^*,P_L]VB.
\tag{9.2}
\]
This is trace class by the lemma and (9.1). The same statement holds after summing over characters: the seminorm bounds and rapid angular decrease established in Section 8 make the sums of trace norms finite. Thus (9.2) proves trace class for the actual operator, rather than assuming it from a formal kernel integral.

The first trace in (9.2) is
\[
2L\,\frac1{2\pi}\int_\mathbb R m_\chi(s)\,ds.
\tag{9.3}
\]
For example, its kernel is continuous except at the two output cutoff endpoints. Average the Fourier basis on a finite containing interval with Fejér weights. These positive contraction kernels converge to the diagonal away from those two endpoints; boundedness of the kernel and the approximate-identity bound give dominated convergence. Their traces therefore converge to the diagonal integral. This argument also justifies the diagonal calculation below.

Translate the second term in (9.2) by \(L\). Since convolution operators commute with translation, its trace becomes
\[
\operatorname{Tr}\bigl(
1_{r\geq-2L}[V^*,P]VB\bigr)
\longrightarrow\operatorname{Tr}\bigl((V^*PV-P)B\bigr).
\tag{9.4}
\]
Here strong convergence of the projections suffices: approximate a trace-class operator in trace norm by finite-rank operators, apply strong convergence on their finite-dimensional ranges, and use the uniform norm bound one on the projections.

In the \(s\)-representation the kernel of \(P\) is
\(\tfrac12\delta(s-t)+\tfrac{i}{2\pi}\operatorname{PV}(s-t)^{-1}\).
The delta terms in \(V^*PV-P\) cancel. The remaining continuous kernel, after multiplication by \(B\), is
\[
\frac{i}{2\pi}
\frac{\overline{u_\chi(s)}u_\chi(t)-1}{s-t}\,m_\chi(t).
\tag{9.5}
\]
Its diagonal is \(-i\overline{u_\chi(s)}u_\chi'(s)m_\chi(s)/(2\pi)\).
To verify the trace formula, first restrict both spectral variables to \([-R,R]\). Fejér averages of that interval's orthonormal Fourier basis converge to its identity strongly, while their positive kernels concentrate on the diagonal of the continuous kernel (9.5). Thus the trace of the restricted operator is its diagonal integral. Let \(R\to\infty\). Trace-norm approximation gives convergence of the traces, and the Schwartz multiplier times the polynomial bound on \(u_\chi'\) gives dominated convergence of the integrals. We obtain
\[
\operatorname{Tr}\bigl((V^*PV-P)B\bigr)
=\frac1{2\pi}\int_\mathbb R
m_\chi(s)\bigl(-i\overline{u_\chi(s)}u_\chi'(s)\bigr)\,ds.
\tag{9.6}
\]
The signs in (9.5)–(9.6) use the negative half-line cutoff \(r\leq0\). Replacing it by the positive half-line changes the commutator sign.

## 10. Connes's semilocal trace formula

For each place define the additive-character-normalized distribution
\[
T_v(h)=\int_{k_v^\times}'\frac{h(u^{-1})}{|1-u|_v}\,d^*u.
\tag{10.1}
\]
Here \(k_v^\times\) is mapped to \(C_S\) by inserting \(u\) in its \(v\)-coordinate. To specify the prime, let \(\rho_v>0\) satisfy \(d^*u=\rho_v^{-1}du/|u|_v\), for self-dual \(du\) and the multiplicative normalization of the second lesson. Take the finite-part extension \(L_v\) of \(\rho_v^{-1}du/|1-u|_v\) whose additive Fourier transform vanishes at \(1\), and set
\(T_v(h)=\langle L_v,h(u^{-1})/|u|_v\rangle\).
“Finite part” means that the test function's value at \(1\) is subtracted in a neighborhood of the logarithmic singularity. The remaining ambiguity is a multiple of \(\delta_1\); the Fourier condition fixes it. It excludes extensions with additional derivatives of a point mass. The second lesson's equations (7.2)–(7.5) give equivalent explicit formulas at finite, real and complex places. In particular this principal value retains the different and conductor terms.

Its spectral density is the logarithmic derivative of the local phase:
\[
w_{v,\chi}(s)
=-i\,\overline{\gamma_v(\chi_v,1/2+is,\alpha_v)}
\frac{d}{ds}\gamma_v(\chi_v,1/2+is,\alpha_v).
\tag{10.2}
\]
We check the correspondence, including its constants. At an unramified finite place let \(\beta=\chi_v(\varpi_v)\), and first use an additive character of conductor \(\mathcal O_v\). The phase is
\[
\frac{1-\beta q_v^{-1/2-is}}
{1-\bar\beta q_v^{-1/2+is}},
\quad
w_{v,\chi}(s)
=2\log q_v\sum_{n\geq1}q_v^{-n/2}
\Re\bigl(\beta^ne^{-ins\log q_v}\bigr).
\tag{10.3}
\]
The series converges normally. Fourier inversion of \(m_\chi\) makes its two exponentials evaluate \(h\) at the classes of \(\varpi_v^{-n}\) and \(\varpi_v^n\). The factors \(|\lambda|^{1/2}\) in (8.2), combined with \(q_v^{-n/2}\), give respectively \(1\) and \(q_v^{-n}\). Character factors cancel after angular inversion. This is precisely the nonunit-shell calculation of (10.1).

For a character of conductor exponent \(n\geq1\), the phase is a constant of modulus one times \(q_v^{-ins}\); its density is \(-n\log q_v\). This equals the unit-shell term calculated in the second lesson. Changing an additive character to \(\alpha_v(ax)\) multiplies the phase by a constant of modulus one times \(|a|_v^{is}\); it adds \(\log|a|_v\) to (10.2), exactly the prescribed principal-value correction.

At a real place with parity \(\epsilon\) and norm shift \(\tau\), put \(L_v(z)=\Gamma_{\mathbb R}(z+\epsilon)\). Up to a constant phase the quotient is
\[
\frac{L_v(1/2-i(s+\tau))}
{L_v(1/2+i(s+\tau))},\qquad
w_{v,\chi}(s)
=-2\Re\frac{L_v'}{L_v}(1/2+i(s+\tau)).
\tag{10.4}
\]
The complex formula is the same with
\(L_v(z)=\Gamma_{\mathbb C}(z+|m|/2)\) for angular index \(m\).
The digamma integrals and angular integral in the second lesson, Section 7, identify these densities with its real and complex principal values. This is also a direct way to check the archimedean sign: for the trivial real character, (10.4) is the negative of the positive-frequency density used for \(W_\infty=-W_{\mathbb R}\) in the next lesson.

Since \(u_\chi\) is the product of these local phases,
\(-i\bar u_\chi u_\chi'=\sum_{v\in S}w_{v,\chi}\).
Fourier inversion and (10.2)–(10.4) therefore give
\[
\sum_\chi\frac1{2\pi}\int m_\chi(s)
\bigl(-i\bar u_\chi(s)u_\chi'(s)\bigr)\,ds
=\sum_{v\in S}T_v(h).
\tag{10.5}
\]
All interchanges are justified by the uniform bounds and angular decay of Section 8. Equivalently first check each angular component by the local calculations, then sum the absolutely convergent components. The possible lack of compact support of the restriction of \(h\) to one local group causes no difficulty: its norm support is bounded away from zero and infinity, and at fixed norm its angular variables range over compact sets.

**Theorem 10.1 (Connes's semilocal trace formula).** On the Hilbert space (7.3), let \(P_\Lambda\) be the norm cutoff \(|x|\leq\Lambda\), let \(\widehat P_\Lambda=\mathscr F P_\Lambda\mathscr F^{-1}\), and put \(R_\Lambda=\widehat P_\Lambda P_\Lambda\). For every smooth compactly supported \(h\) on \(C_S\), \(R_\Lambda U(h)\) is trace class, and

\[
\boxed{\operatorname{Tr}(R_\Lambda U(h))
=2h(1)\log'\Lambda+\sum_{v\in S}T_v(h)+o(1),}
\qquad
2\log'\Lambda
=\int_{\Lambda^{-1}\leq|\lambda|\leq\Lambda}d^*\lambda.
\tag{10.6}
\]

In a number field \(\log'\Lambda=\log\Lambda\).

*Proof in the number-field case.* Trace class was proved in (9.2), with a summable bound over all angular components. Sum (9.3) over \(\chi\). Fourier inversion at the identity in (8.2) gives
\(\sum_\chi(2\pi)^{-1}\int m_\chi(s)\,ds=h(1)\).
The second trace tends to (10.5) by (9.4)–(9.6). The trace-norm bound is summable uniformly for \(L\geq0\); it bounds every projection in (9.4) by one. Hence dominated convergence also justifies summing the limits over \(\chi\). This proves (10.6). ∎

For a function field the norm coordinate is \(r=aj\), \(j\in\mathbb Z\). Use the Fourier variable \(\theta\in[0,2\pi]\) and replace (8.2) by
\[
m_\chi(\theta)
=a\sum_{j\in\mathbb Z}\int_{K_S}
h(c,aj)e^{aj/2}\overline{\chi(c)}e^{-ij\theta}\,dc.
\tag{10.7}
\]
This is a trigonometric polynomial. At the finite level of \(h\), there are finitely many angular characters: \(K_S\) is a finite extension of a quotient of local profinite unit groups, and a locally constant function factors through a finite quotient. The phase \(u_\chi(\theta)\) is the same product of local factors as (8.4), evaluated at \(s=\theta/a\). Each local residue logarithm is an integer multiple of \(a\), so this phase is periodic and smooth. Its finite Euler denominators have no zeros on the circle.

Put \(M=\lfloor\log\Lambda/a\rfloor\). The proof of (9.2) now uses \(P_M=1_{j\leq M}\), and the finite overlap is \(-M\leq j\leq M\). The required commutator lemma has a simpler discrete proof. If a smooth multiplier has Fourier coefficients \(b_n\), the commutator of a half-line projection with a shift by \(n\) has rank \(|n|\) and norm one. Thus its trace norm is at most
\(\sum_n|n||b_n|<\infty\). Apply this to \(m_\chi\) and \(m_\chi u_\chi\), using (9.1). The finite overlap term has finite rank, and the second term tends in trace to the full commutator exactly as in (9.4).

The kernel of \(P_0\), away from the diagonal on the circle, is
\((2\pi)^{-1}(1-e^{i(\theta-\eta)})^{-1}\).
In \(V^*P_0V-P_0\) the diagonal singularity cancels, and its diagonal limit is
\(-i\bar u_\chi(\theta)u_\chi'(\theta)/(2\pi)\).
Fejér averaging on the circle gives its trace. Equations (10.3) and their ramified versions identify its pairing with (10.7) with \(\sum_vT_v(h)\): differentiation in \(\theta\) divides the density by \(a\), while the factor \(a\) in (10.7) restores exactly the local shell measure \(\log q_v\).

Finally the main trace is \(a(2M+1)h(1)\), and
\[
2\log'\Lambda=a(2M+1)
\tag{10.8}
\]
by the specified multiplicative measure. This proves (10.6) in the function-field case, including the shell boundary term. It completes the theorem for global fields.

## 11. What the finite-place trace teaches

For \(k=\mathbb Q\) and \(S=\{\infty,2,3\}\), the group of \(S\)-units is
\(\{\pm2^n3^m:n,m\in\mathbb Z\}\). The local terms in (10.6) are the real principal value and the two prime distributions. If \(h\) depends only on the norm, the finite terms are exactly
\[
(\log2)\sum_{n\geq1}\bigl(h(2^n)+2^{-n}h(2^{-n})\bigr)
+(\log3)\sum_{n\geq1}\bigl(h(3^n)+3^{-n}h(3^{-n})\bigr).
\tag{11.1}
\]
Only finitely many terms enter for a compactly supported norm test. If \(h\) is supported in \((1/2,2)\), both prime distributions vanish, so the constant term after subtracting \(2h(1)\log\Lambda\) is purely archimedean.

The function-field boundary in (10.8) matters even for one local field. With residue cardinality \(q_v\), trivial additive conductor, \(h\) equal to \(1\) on the units and zero on all other norm shells, the local principal value is zero by its normalization. For \(\Lambda=q_v^M\), the trace is consequently
\((2M+1)\log q_v+o(1)\).
Using \(2M\log q_v\) would lose the central shell. This agrees with the exact main term obtained from the discrete overlap projection.

We can check that example directly in the trivial angular component. Put \(r=q_v^{-1/2}\) and expand its phase as
\[
\frac{1-re^{-i\theta}}{1-re^{i\theta}}
=\sum_{\ell\in\mathbb Z}c_\ell e^{-i\ell\theta},
\qquad
c_1=-r,\quad c_{-j}=(1-r^2)r^j\ (j\geq0),\quad
c_\ell=0\ (\ell\geq2).
\tag{11.2}
\]
These coefficients have squared sum one and first weighted squared sum zero:
\(\sum_\ell\ell c_\ell^2=r^2-(1-r^2)^2\sum_{j\geq0}jr^{2j}=0\).
For \(M\geq1\), the cutoff diagonal trace is
\[
(\log q_v)\sum_{\ell\leq2M}(2M-\ell+1)c_\ell^2
=(2M+1)\log q_v.
\tag{11.3}
\]
Indeed for each shift \(\ell=j-k\), the constraints \(j\leq M\), \(k\geq-M\) give exactly \(2M-\ell+1\) pairs. Thus this particular example has the stated trace exactly once \(M\geq1\), independently confirming the shell convention.

The theorem concerns each fixed finite \(S\). Its proof uses the product of finitely many local phases and sums over the angular characters of \(K_S\). The global Weil criterion in Section 6 concerns the full idèle class distribution. Establishing an operator limit as all places are included requires further estimates; the finite-\(S\) theorem by itself supplies no global positivity conclusion.

## 12. Exercises with solutions

### 1. The support of the square

Prove the support inclusion for \(g*\bar g^\sharp\).

**Solution.** The integrand can be nonzero only if \(y\) and \(y/x\) belong to the support of \(g\). Their ratio is \(x\). A point outside the closed product of the two compact support sets has a neighborhood where the integrand vanishes, so the convolution vanishes there. This proves (2.1), including support endpoints.

### 2. Which primes can occur?

Prove the local vanishing assertion, and list the possible primes for \(g\) supported in \([1/3,3]\).

**Solution.** The local distribution evaluates only the two points \(p^m,p^{-m}\); neither lies in an open support interval \((p^{-1},p)\). For the stated support, \(f\) is supported in \([1/9,9]\) and is zero at its endpoints. The possible primes are \(2,3,5,7\). Their possible powers below \(9\) are \(2,4,8;3;5;7\), respectively. The power \(9\) has zero endpoint value. A particular test may make further terms vanish.

### 3. Mellin Paley–Wiener decay

Prove (2.2) with a constant independent of the real part.

**Solution.** Integrate against the whole complex exponential \(e^{su}\), not just its oscillatory factor. Moving \(N\) derivatives to \(g(e^u)\) gives \(s^{-N}\), with no powers of \(\sigma\) in the numerator. Bound its derivative's integral by \(\max(e^{A\sigma},e^{B\sigma})\) times its \(L^1\) norm. Use \(|s|\geq|t|\) for \(|t|\geq1\) and the undifferentiated integral otherwise. Compact support permits differentiation in \(s\), proving entire continuation as well.

### 4. The direct positivity implication

Show that RH and \(G(0)=G(1)=0\) give \(\mathcal W(g)=-\sum_\rho|G(\rho)|^2\).

**Solution.** On the critical line, \(1-\bar\rho=\rho\), so each term in (1.5) is \(|G(\rho)|^2\). The two pole products in (1.4) vanish. Equation (2.2) and the zero count justify the absolutely convergent sum. Hence (1.6) is exactly the claimed identity.

### 5. Completing the compact interpolation

Construct the test that contradicts the sign in the presence of an off-line zero, preserving the finite conditions exactly.

**Solution.** Choose the band containing the distinct pair \(\rho_0,1-\bar\rho_0\). For each target, the polynomial \(P\) vanishes at the other target, every remaining band zero, and every point of \(F\). The Gaussian transform (3.2) makes the outside squared tail exponentially small by (3.3). Cut off its inverse transform (3.4), and then apply \(P(-d/du)\); cutting off **after** that polynomial operation would destroy the exact zero conditions. Normalize at the target. Weighted convergence (3.5) proves that the tail remains small. Subtract the two tests, giving values \(1,-1\) at the pair and zero at all other band zeros. Their contribution is \(-2m\), while the outside form has absolute value at most \(4\eta^2\). Taking \(4\eta^2<2m\) gives \(Q<0\), hence \(\mathcal W>0\). This provides the function, its support, its exact vanishing and the bound on the infinite remainder, rather than only formal interpolation data.

## 13. Proof dependencies and references

The compact interpolation, Weil criterion, character reductions and semilocal trace theorem are proved in this lesson. For the positivity statements we use the explicit formulas proved in the preceding two lessons and their exact existing planned zeta and Hecke prerequisites: continuation, reflection, order, zero count and gamma estimates. For the trace theorem we use the local Fourier transforms, self-dual measures and Tate functional equations in lessons 5, 7 and 8 of *Adèles, idèles and Tate's thesis*. In the convention (8.3), those equations are required for every unitary character of a nonarchimedean local field and of \(\mathbb R^\times,\mathbb C^\times\), including the conductor and additive-character dependence. The number-field class and unit structure is supplied by its lesson 3. These providers are actual existing planned assignments; their public full-proof completion is not asserted here. Section 7 gives the needed function-field compactness and \(S\)-unit argument directly.

The sources establish the historical origins and allow comparison of conventions:

- A. Weil, [*Sur les formules explicites de la théorie des nombres*](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&paperid=2289&what=fullt&option_lang=eng) (1972), no. 16, for the explicit formula written as a distribution on the Weil group (on the idèle class group for Hecke characters) and the remark that the positivity of this distribution is equivalent to the Riemann hypothesis together with Artin's conjecture. Weil introduced the positivity criterion and the idèle-class formulation in 1952.
- E. Bombieri, [*Problems of the Millennium: the Riemann Hypothesis*](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf) (2000), Section V, for the quadratic form and its two pole moments.
- A. Connes and C. Consani, [*Weil positivity and trace formula, the archimedean place*](https://arxiv.org/pdf/2006.13771) (2021), Introduction and appendix *Positivity criterion*, for the compact-support formulation with finite vanishing conditions and its attribution to Yoshida.
- A. Connes, [*Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*](https://arxiv.org/pdf/math/9811068) (1999), Section V, Theorem 3, for one place, and Section VII, Theorem 4, for the semilocal formula. The proof here uses the Fourier phase and trace-class commutators to justify the cutoff trace.
- A. Connes, [*The Riemann Hypothesis: Past, Present and a Letter Through Time*](https://arxiv.org/pdf/2602.04022) (2026), subsection *Weil's Positivity Criterion*, for the relation between the form and its geometric interpretations.

The Gaussian criterion in *Weil's proof for curves and what is missing over the integers*, Theorem 6.4, is a related existing internal result. The compact construction above proves the additional support and interpolation assertions used here.
