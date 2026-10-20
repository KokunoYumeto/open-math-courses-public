# Zero detection for the frequency characters

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

After the Euler product of [*The Euler product of the probe*](the-euler-product-of-the-probe.md), the frequency \(u\) enters the probe through \(1/L^S(\xi,\eta\overline{\chi_\bullet(u)})\). Lesson 14 moves the \(\xi\)-contour of every nonprincipal frequency from \(\operatorname{Re}\xi>1\) to \(\operatorname{Re}\xi=0.998\), which is only possible where this reciprocal is under control. This lesson shows that it is under control for all but \(O(U^{1/2})\) of the frequencies of norm about \(U\). A zero of \(L_F(s,\omega_u)\) close to \(\operatorname{Re}s=1\) forces a long Dirichlet polynomial to be large; a large sieve over the frequency characters, ordered by conductor, shows that this happens rarely; and away from the exceptional characters the Borel–Carathéodory theorem and the three circles theorem bound the reciprocal by \(U^\epsilon\).

**Prerequisites.** [*S-integers and sixth-power classes*](s-integers-and-sixth-power-classes.md), Lemma 2.1 and Lemma 4.1; [*Sextic reciprocity and Kummer characters*](sextic-reciprocity-and-kummer-characters.md), Lemmas 3.1, 3.2 and 4.1; [*The quadratic large sieve and the reflected moment*](the-quadratic-large-sieve-and-the-reflected-moment.md), Lemma 3.1; [*The Poisson probe*](the-poisson-probe.md), Lemma 3.1; [*The Gamma function and Stirling's formula*](course:NT-ZETA/NT-ZETA-03), Corollary 4.1; [*Entire functions of order one and the Hadamard product of xi*](course:NT-ZETA/NT-ZETA-05), Theorem 2.1; [*Growth in the critical strip: convexity and the Lindelöf hypothesis*](course:NT-ZETA/NT-ZETA-06), Theorem 2.1; [*The Riemann hypothesis implies the Lindelöf hypothesis*](course:NT-ZETA/NT-ZETA-18), Theorem 2.1; [*Tate's global theory: continuation and functional equation*](course:NT-ADL/NT-ADL-09), Theorem 9.2; [*Hecke L-functions and the Dedekind zeta function*](course:NT-ADL/NT-ADL-10), (1)–(3) and Theorem 10.1; [*Dirichlet series and Euler products*](course:NT-ZETA/NT-ZETA-01), Lemma A.3; [*Schwartz functions and Fourier inversion*](course:AN-01/prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017), Section F4.

## 1. The frequency characters

For \(u\in\mathcal U\) (Lemma 3.2 of Lesson 3) let \(\omega_u\) be the Hecke character \(\eta\,\overline{\kappa_u}\), with \(\kappa_u\) the Kummer character of Lemma 3.1 of Lesson 3; as an idèle class character of finite order it has a well-defined conductor, and its ideal function, extended by zero on the primes of the conductor, is the primitive character inducing \(\eta\overline{\chi_\bullet(u)}\). Write \(L_F(s,\omega)\) for the complete finite \(L\)-function of a primitive character, a sum over all nonzero integral ideals of \(\mathcal O_F\).

**Lemma 1.1** (the family [OpenAI-029, (8.1)]). For \(U\ge1\):

1. \(\#\{u\in\mathcal U:U\le q_u<2U\}\le C\,U\), and \(\operatorname N\mathfrak f_{\omega_u}\le C\,U\) for these \(u\);
2. the characters \(\omega_u\), \(u\in\mathcal U\), are pairwise distinct, and at most one of them is principal;
3. their local components at the places of \(S\) belong to a fixed finite set.

*Proof.* Part 1 is Lemma 4.1 of Lesson 3. For part 2, \(\omega_u=\omega_{u'}\) means \(\kappa_u=\kappa_{u'}\), so \(u=u'\) by Lemma 3.2 of Lesson 3; a principal \(\omega_u\) means \(\kappa_u=\eta\), which by distinctness happens for at most one \(u\). For part 3, the component of \(\kappa_u\) at \(v\in S\) is \(y\mapsto(u,y)_{6,v}\) (Lemma 3.1 of Lesson 3), which depends only on the class of \(u\) in the finite group \(F_v^\times/F_v^{\times6}\). \(\square\)

**Lemma 1.2** (the divisor bound). Let \(\tau_F(\mathfrak n)\) be the number of integral ideals dividing \(\mathfrak n\). For every \(\epsilon>0\), \(\tau_F(\mathfrak n)\le C_{F,\epsilon}(\operatorname N\mathfrak n)^\epsilon\).

*Proof.* \(\tau_F(\mathfrak n)(\operatorname N\mathfrak n)^{-\epsilon}=\prod_{\mathfrak p^a\parallel\mathfrak n}(a+1)q_{\mathfrak p}^{-a\epsilon}\). If \(q_{\mathfrak p}\ge2^{1/\epsilon}\), the factor is at most \((a+1)2^{-a}\le1\). The finitely many primes with \(q_{\mathfrak p}<2^{1/\epsilon}\) give factors at most \(\sup_{a\ge0}(a+1)2^{-a\epsilon}<\infty\). \(\square\)

## 2. A large sieve for primitive characters of bounded conductor

**Lemma 2.1** (primitive conductor large sieve [OpenAI-029, Lemma 8.1]). Let \(C_0>0\), let \(\mathscr L_S\) be a finite set of possible local components at \(S\), and let \(\mathscr X(U)\) be a family of distinct primitive finite-order Hecke characters of \(F\) with conductor norms at most \(C_0U\) and components at \(S\) in \(\mathscr L_S\). For \(N,U\ge2\), complex numbers \(b_{\mathfrak n}\) and \(\epsilon>0\),
\[
\begin{aligned}
&\sum_{\omega\in\mathscr X(U)}\Bigl|\sum_{\operatorname N\mathfrak n\le N}b_{\mathfrak n}\,\omega(\mathfrak n)\Bigr|^2\\
&\quad \le C_{F,S,C_0,\mathscr L_S,\epsilon}\,(N+U^2)(NU)^\epsilon\\
&\qquad \sum_{\operatorname N\mathfrak n\le N}|b_{\mathfrak n}|^2 ,\quad(2.1)
\end{aligned}
\]
the sums running over integral ideals of \(\mathcal O_F\).

*Proof.* *Reduction to exterior ideals.* Write \(\mathfrak n=\mathfrak n_S\mathfrak n^S\) with \(\mathfrak n_S\) supported on the finite places of \(S\) and \(\mathfrak n^S\) prime to them. There are \(O((1+\log N)^{|S|})\) possible \(\mathfrak n_S\) of norm at most \(N\), and for characters with the same components at \(S\) the value \(\omega(\mathfrak n_S)\) is the same (or zero). Partition \(\mathscr X(U)\) according to the components at \(S\), apply Cauchy–Schwarz over the \(\mathfrak n_S\) and over \(O(\log N)\) dyadic ranges of \(\operatorname N\mathfrak n^S\); the losses are powers of \(\log N\), absorbed in \(N^\epsilon\). It remains to prove (2.1) for coefficients on exterior ideals of norm in \((N_1,2N_1]\), \(N_1\le N\), and characters with one fixed set of components at \(S\).

*Values through residue characters.* Let \(\omega\) be such a character and \(\mathfrak q\) the exterior part of its conductor. For an exterior ideal \(\mathfrak n=nR\), with \(n\) its balanced generator (Lemma 4.1 of Lesson 2), evaluate the idèle character at the principal idèle \(n\): its value is \(1\), and the unramified exterior components give \(\omega(\mathfrak n)\) when \(\mathfrak n\) is prime to \(\mathfrak q\). Hence
\[
\begin{gathered}
\omega(\mathfrak n)=\lambda_S(n)\,\lambda_{\mathfrak q}(n),\\
\lambda_S(n)=\prod_{v\in S}\omega_v(n)^{-1},\\
\lambda_{\mathfrak q}(n)=\prod_{v\mid\mathfrak q}\omega_v(n)^{-1},
\end{gathered}
\]
where \(\lambda_S\) is the same unitary function for the whole slice, and \(\lambda_{\mathfrak q}\) is a primitive character of \((R/\mathfrak q)^\times\), extended by zero; both sides vanish when \(\mathfrak n\) meets \(\mathfrak q\). In particular \(\omega\) is determined by \(\lambda_{\mathfrak q}\).

*Gauss sums.* Let \(q\) generate \(\mathfrak q\), and for a primitive \(\lambda\) modulo \(\mathfrak q\) put \(\tau(\overline\lambda)=\sum_{d\bmod\mathfrak q}\overline{\lambda(d)}\,\mathrm e(d/q)\). Then for every \(n\in R\),
\[
\begin{gathered}
\begin{aligned}
\lambda(n)\,\tau(\overline\lambda)&=\sum_{d\bmod\mathfrak q}\overline{\lambda(d)}\,\mathrm e(nd/q),
\end{aligned}\\
|\tau(\overline\lambda)|^2=q_{\mathfrak q}.\quad(2.2)
\end{gathered}
\]
For a unit \(n\) the identity follows from \(d\mapsto n^{-1}d\). If a prime \(\mathfrak p\mid\mathfrak q\) divides \(n\), let \(H\) be the group of units congruent to \(1\) modulo \(\mathfrak q\mathfrak p^{-1}\); for \(h\in H\), \(nd(h-1)\in\mathfrak q\), so \(\mathrm e(ndh/q)=\mathrm e(nd/q)\), while \(\lambda\) is nontrivial on \(H\) by primitivity, so the right side equals \(\overline{\lambda(h)}\) times itself for some \(\lambda(h)\ne1\) and vanishes. Finally, \((n,d)\mapsto\mathrm e(nd/q)\) is a perfect pairing on \(R/\mathfrak q\) (Lemma 2.1 of Lesson 2), so Parseval's identity (expand the square: for \(d\ne d'\) the character \(n\mapsto\mathrm e(n(d-d')/q)\) is nontrivial and sums to zero over \(R/\mathfrak q\)) gives \(\sum_n|\sum_d\overline{\lambda(d)}\mathrm e(nd/q)|^2=q_{\mathfrak q}|(R/\mathfrak q)^\times|\), while by the identity the left side is \(|(R/\mathfrak q)^\times|\,|\tau(\overline\lambda)|^2\).

*The sieve.* Put \(T_{d/q}=\sum_{\mathfrak n}b_{\mathfrak n}\lambda_S(n)\mathrm e(nd/q)\). By (2.2), the sum over the characters of exterior conductor \(\mathfrak q\) is at most
\[
\begin{aligned}
&\frac1{q_{\mathfrak q}}\sum_{\lambda\bmod\mathfrak q}\Bigl|\sum_{d}\overline{\lambda(d)}\,T_{d/q}\Bigr|^2\\
&\quad =\frac{|(R/\mathfrak q)^\times|}{q_{\mathfrak q}}\sum_{d\in(R/\mathfrak q)^\times}|T_{d/q}|^2\\
&\quad \le\sum_{d\in(R/\mathfrak q)^\times}|T_{d/q}|^2 ,
\end{aligned}
\]
by orthogonality of the characters of \((R/\mathfrak q)^\times\). Sum over \(q_{\mathfrak q}\le C_0U\). The fractions \(d/q\) are distinct reduced fractions, and the balanced generators of the ideals on the dyad lie in \(\ell_{2N_1}K\) for a fixed compact \(K\). The exchanged form of Lemma 3.1 of Lesson 11, with \(V=\max(2,C_0U)\), bounds the total by \(C(N+U^2)\sum|b_{\mathfrak n}|^2\), since \(|\lambda_S|=1\). \(\square\)

## 3. A conservative convexity bound

**Lemma 3.1** ([OpenAI-029, (8.3)]). Let \(A_F=[F:\mathbb Q]\). For every \(\epsilon>0\), every nonprincipal primitive finite-order Hecke character \(\omega\) of \(F\) with \(\operatorname N\mathfrak f_\omega\le C_0U\), \(U\ge1\), and all \(0\le\sigma\le4\), \(t\in\mathbb R\),
\[
\begin{aligned}
&|L_F(\sigma+it,\omega)|\\
&\quad \le C_{F,C_0,\epsilon}\,U^{1/2+\epsilon}(2+|t|)^{A_F}.\quad(3.1)
\end{aligned}
\]

*Proof.* Let \(0<\epsilon'\le\min(\epsilon,\frac14)\). Characters of finite order are trivial on \(\mathbb C^\times\), which is divisible, so in the notation of (2) of [*Hecke L-functions and the Dedekind zeta function*](course:NT-ADL/NT-ADL-10) every infinite component is trivial and \(\Gamma_\infty(s,\omega)=\Gamma_{\mathbb C}(s)^{r}\), \(2r=A_F\). On \(\operatorname{Re}s=1+\epsilon'\), the Euler product gives \(|L_F|\le\zeta_F(1+\epsilon')\). On \(\operatorname{Re}s=-\epsilon'\), Theorem 10.1 there gives
\[
\begin{gathered}
\begin{aligned}
|L_F(s,\omega)|&=Q^{1/2+\epsilon'}\Bigl|\frac{\Gamma_{\mathbb C}(1-s)}{\Gamma_{\mathbb C}(s)}\Bigr|^r\\
&\quad\times|L_F(1-s,\overline\omega)|,
\end{aligned}\\
Q=|d_F|\operatorname N\mathfrak f_\omega ,
\end{gathered}
\]
and Corollary 4.1 of [*The Gamma function and Stirling's formula*](course:NT-ZETA/NT-ZETA-03) bounds the Gamma quotient by \(C(2+|t|)^{1+2\epsilon'}\) (for \(|t|\le1\) by continuity, as \(\Gamma\) has no pole at \(-\epsilon'+it\)). So \(|L_F(-\epsilon'+it,\omega)|\)\(\le CU^{1/2+\epsilon'}(2+|t|)^{r(1+2\epsilon')}\). In the strip, \(\omega\) is nontrivial on the norm-one idèle classes (a character of finite order is trivial on the positive reals), so by (19) of Theorem 9.2 of [*Tate's global theory*](course:NT-ADL/NT-ADL-09) the completed function is entire and bounded on vertical strips, each of its two terms being an integral over norms at least one that converges uniformly there; with Stirling for \(1/\Gamma_{\mathbb C}\), this gives \(|L_F(s,\omega)|\le D\exp(D(1+|t|))\) on the strip. Theorem 2.1 of [*Growth in the critical strip*](course:NT-ZETA/NT-ZETA-06), whose proof bounds the constant by a fixed multiple of the larger boundary constant, gives (3.1) for \(-\epsilon'\le\sigma\le1+\epsilon'\), with exponent \(r(1+2\epsilon')\le A_F\); for \(1+\epsilon'\le\sigma\le4\) the Euler product suffices. \(\square\)

The constant in (3.1) is crude but uniform; this is all the argument needs. The same proof gives polynomial bounds in \(|t|\) on fixed strips for \((s-1)\zeta_F(s)\). Omitting the Euler factors at \(S\), or at the primes dividing \(u\), changes such bounds on a line \(\operatorname{Re}s=\sigma_*>0\) by at most \(C_\epsilon q_u^\epsilon\), since \(\prod_{\mathfrak p\mid uR}(1\pm q_{\mathfrak p}^{-\sigma_*})^{\pm1}\le C_{\epsilon,\sigma_*}q_u^\epsilon\) by the argument of Lemma 1.2.

## 4. Zero detection

**Proposition 4.1** (exceptional frequencies [OpenAI-029, Proposition 8.2]). There are \(\rho>0\) and \(U_0\), depending on \(F\), \(S\) and \(\eta\), with the following property. For every \(U\ge U_0\) there is a set \(\mathcal E(U)\subseteq\{u\in\mathcal U:U\le q_u<2U\}\) with
\[
|\mathcal E(U)|\le C\,U^{1/2},
\]
containing every \(u\) for which \(\omega_u\) is principal or \(L_F(s,\omega_u)\) has a zero with \(\operatorname{Re}s\ge0.996\), \(|\operatorname{Im}s|\le4U^\rho\). For \(u\notin\mathcal E(U)\) and \(\epsilon>0\),
\[
\begin{gathered}
\bigl|L^S\bigl(\xi,\eta\overline{\chi_\bullet(u)}\bigr)^{-1}\bigr|\le C_\epsilon\,U^\epsilon\\
(\operatorname{Re}\xi\ge0.998,\ |\operatorname{Im}\xi|\le2U^\rho).\quad(4.1)
\end{gathered}
\]

*Proof.* Put \(\sigma_0=0.996\) and fix \(0<\rho<\min\{\frac1{10},\frac1{A_F+1}\}\).

*The detector.* For a nonprincipal \(\omega=\omega_u\) in the dyad, put
\[
\begin{gathered}
\begin{aligned}
D_U(s,\omega)&=\sum_{\operatorname N\mathfrak d\le U^2}\mu_F(\mathfrak d)\,\omega(\mathfrak d)\,\operatorname N\mathfrak d^{-s},
\end{aligned}\\
\alpha_U(\mathfrak n)=\sum_{\substack{\mathfrak d\mid\mathfrak n\\ \operatorname N\mathfrak d\le U^2}}\mu_F(\mathfrak d),
\end{gathered}
\]
with \(\mu_F\) the Möbius function of integral ideals. By complete multiplicativity of \(\omega\) (with the zero extension), \(L_F(s,\omega)D_U(s,\omega)\)\(=\sum_{\mathfrak n}\alpha_U(\mathfrak n)\omega(\mathfrak n)\operatorname N\mathfrak n^{-s}\) for \(\operatorname{Re}s>1\), and
\[
\begin{gathered}
\alpha_U(\mathcal O_F)=1,\\
\alpha_U(\mathfrak n)=0\quad(1<\operatorname N\mathfrak n\le U^2),\\
|\alpha_U(\mathfrak n)|\le\tau_F(\mathfrak n),\quad(4.2)
\end{gathered}
\]
the middle statement because all divisors of such \(\mathfrak n\) are counted and \(\sum_{\mathfrak d\mid\mathfrak n}\mu_F(\mathfrak d)=0\) for \(\mathfrak n\ne\mathcal O_F\).

Suppose \(L_F(\beta+i\gamma,\omega)=0\) with \(\beta\ge\sigma_0\) and \(|\gamma|\le4U^\rho\); then \(\beta\le1\) by the Euler product. Mellin inversion of \(e^{-x}\) (Fourier inversion, Section F4 of [*Schwartz functions and Fourier inversion*](course:AN-01/prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017), for the Schwartz function \(u\mapsto e^{cu}e^{-e^u}\), whose Fourier transform is \(\tau\mapsto\Gamma(c-i\tau)\)) gives, with \(c>1\) and the sum and the integral interchanged by absolute convergence,
\[
\begin{aligned}
&\sum_{\mathfrak n}\alpha_U(\mathfrak n)\omega(\mathfrak n)\operatorname N\mathfrak n^{-\beta-i\gamma}\\
&\qquad e^{-\operatorname N\mathfrak n/U^{10}}=\frac1{2\pi i}\\
&\qquad \int_{(c)}L_F(\beta+i\gamma+v,\omega)\\
&\qquad \,D_U(\beta+i\gamma+v,\omega)\,\Gamma(v)\,U^{10v}\\
&\qquad \,dv .\quad(4.3)
\end{aligned}
\]
Move the line to \(\operatorname{Re}v=\frac12-\beta\in[-\frac12,-0.496]\) by the residue formula (Lemma A.3 of [*Dirichlet series and Euler products*](course:NT-ZETA/NT-ZETA-01)). The only pole crossed is \(v=0\), with residue \(L_F(\beta+i\gamma,\omega)D_U(\beta+i\gamma,\omega)=0\); \(L_F(\cdot,\omega)\) is entire, and the exponential decay of \(\Gamma\) against the polynomial bound (3.1) removes the horizontal sides. On the new line, \(|D_U|\le\sum_{\operatorname N\mathfrak d\le U^2}\operatorname N\mathfrak d^{-1/2}\le CU\) by Lemma 3.1 of Lesson 10, \(|U^{10v}|=U^{10(1/2-\beta)}\le U^{-4.96}\), and (3.1) at real part \(\frac12\) gives
\[
\begin{aligned}
&\Bigl|\text{right side of (4.3)}\Bigr|\\
&\quad \le C\,U^{-4.96+1/2+1+\epsilon}(2+4U^\rho)^{A_F}\\
&\quad \le C\,U^{-3.46+A_F\rho+\epsilon}=o(1),\quad(4.4)
\end{aligned}
\]
since \(A_F\rho<1\).

On the left of (4.3), the ideal \(\mathcal O_F\) contributes \(e^{-U^{-10}}=1+o(1)\), the ideals with \(1<\operatorname N\mathfrak n\le U^2\) contribute nothing, and those with \(\operatorname N\mathfrak n>U^{11}\) contribute at most a fixed power of \(U\) times \(e^{-U/2}\), by Lemma 1.2 and the ideal count. So the sum over \(U^2<\operatorname N\mathfrak n\le U^{11}\) has absolute value at least \(\frac12\) for large \(U\). Split this range into \(O(\log U)\) dyads \((N,2N]\). On each dyad write the weight as \(\operatorname N\mathfrak n^{-\sigma_0}\) times \(w(\operatorname N\mathfrak n)\), \(w(t)=t^{\sigma_0-\beta}e^{-t/U^{10}}\), which is positive, decreasing and at most \(1\). Order the ideals of the dyad by norm; by summation by parts, the weighted sum is at most twice the largest initial segment (a **prefix**) of the unweighted sums. Hence for some dyad \(U^2/2<N\le U^{11}\) and some prefix,
\[
\begin{aligned}
&\Bigl|\sum_{\mathfrak n\in\text{prefix}}\alpha_U(\mathfrak n)\,\omega(\mathfrak n)\operatorname N\mathfrak n^{-\sigma_0-i\gamma}\Bigr|\\
&\quad \ge\frac c{\log U}.\quad(4.5)
\end{aligned}
\]

*Counting.* A prefix of a dyad is a disjoint union of at most \(1+\log_2M\) dyadic blocks of consecutive indices, \(M\) being the number of ideals in the dyad, one block from each level of the binary subdivision; by Cauchy–Schwarz its square is at most \((1+\log_2M)\) times the sum of the squares over all blocks of all levels. For one block \(I\), let \(P_I(t)=\sum_{\mathfrak n\in I}\alpha_U(\mathfrak n)\omega(\mathfrak n)\operatorname N\mathfrak n^{-\sigma_0-it}\). For a smooth function on an interval of length three, the supremum of its square on the middle unit interval is at most a constant times the integral of \(|P_I|^2+|P_I'|^2\) over the interval, and \(P_I'\) has the coefficients multiplied by \(-i\log\operatorname N\mathfrak n\). Apply Lemma 2.1, with Lemma 1.1, at each \(t\), integrate over \(|t|\le4U^\rho+2\), and sum over blocks and levels. The squared coefficient mass on a dyad is
\[
\sum_{N<\operatorname N\mathfrak n\le2N}\tau_F(\mathfrak n)^2\operatorname N\mathfrak n^{-2\sigma_0}\le C_\epsilon N^{1-2\sigma_0+\epsilon},
\]
and since \(U^2/2<N\le U^{11}\),
\[
\begin{aligned}
&(N+U^2)\,N^{1-2\sigma_0+\epsilon}\le3N^{2-2\sigma_0+\epsilon}\\
&\quad \le3\,U^{11(0.008+\epsilon)}\\
&\quad =3\,U^{0.088+11\epsilon}.\quad(4.6)
\end{aligned}
\]
Altogether the sum over the characters of the dyad of the largest squared prefix over \(|t|\le4U^\rho\) is at most \(C\,U^{0.088+\rho+O(\epsilon)}(\log U)^{C}\). Each character with a zero in the rectangle contributes at least \(c(\log U)^{-2}\) by (4.5), for one of the \(O(\log U)\) dyads. Hence at most \(C\,U^{0.088+\rho+O(\epsilon)}\le U^{1/2}\) characters have such a zero, for \(\epsilon\) small, because \(0.088+\rho<0.19\). Let \(\mathcal E(U)\) consist of the corresponding \(u\), which are distinct by Lemma 1.1, together with the \(u\) (at most one) for which \(\omega_u\) is principal.

*The reciprocal.* Let \(T=U^\rho\), \(u\notin\mathcal E(U)\), \(\omega=\omega_u\), and \(|t|\le2T\). Consider the discs centred at \(2+it\) with radii
\[
\begin{gathered}
R_2=1.0035,\\
r_2=1.003,\\
r_1=1.002,\\
r_0=0.999 .
\end{gathered}
\]
For large \(U\) the disc of radius \(R_2\) lies in \(\operatorname{Re}s>0.996\), \(|\operatorname{Im}s|<4T\), where \(L_F(s,\omega)\) is entire and has no zero; so \(\log L_F(s,\omega)\) has a branch there, equal at the centre to the logarithm of the Euler product. On the disc, \(\operatorname{Re}\log L_F=\log|L_F|\le C\log U\) by (3.1), and \(|\log L_F(2+it,\omega)|\le\log\zeta_F(2)\). Theorem 2.1 of [*Entire functions of order one and the Hadamard product of xi*](course:NT-ZETA/NT-ZETA-05) (Borel–Carathéodory), applied to \(\log L_F(s)-\log L_F(2+it)\), gives \(|\log L_F|\le C\log U\) on the disc of radius \(r_2\). On the disc of radius \(r_0\), the real parts are at least \(1.001\) and \(|\log L_F|\le\log\zeta_F(1.001)\). Hadamard's three circles theorem (Theorem 2.1 of [*The Riemann hypothesis implies the Lindelöf hypothesis*](course:NT-ZETA/NT-ZETA-18)) gives, on the circle of radius \(r_1\),
\[
\begin{gathered}
|\log L_F(s,\omega)|\le C(\log U)^\theta,\\
\theta=\frac{\log(1.002/0.999)}{\log(1.003/0.999)}<1 .
\end{gathered}
\]
These discs reach \(\operatorname{Re}s=0.998\), and absolute convergence covers \(\operatorname{Re}s\ge3\). So \(|L_F(s,\omega)^{-1}|\le\exp(C(\log U)^\theta)\le C_\epsilon U^\epsilon\) for \(\operatorname{Re}s\ge0.998\), \(|\operatorname{Im}s|\le2T\). Finally \(L^S(\xi,\eta\overline{\chi_\bullet(u)})^{-1}\) differs from \(L_F(\xi,\omega_u)^{-1}\) by the Euler factors at \(S\) and at the primes dividing \(u\), which contribute at most \(C_\epsilon q_u^\epsilon\le C_\epsilon'U^\epsilon\) (end of Section 3). \(\square\)

The numbers \(0.996\), \(0.998\) and \(\frac12\) are absolute; \(\rho\), \(U_0\) and the constants depend on the fixed data. Only \(\rho>0\) matters in Lesson 14.

## 5. Exercises

**5.1.** Show that \(\theta=\log(1.002/0.999)/\log(1.003/0.999)\) is about \(0.750\), and explain why \(\theta<1\) is all that is needed.

**5.2.** Prove that a character of \(\mathbb C^\times\) of finite order is trivial.

**5.3.** In (4.4), check the exponent: \(10(\frac12-0.996)+\frac12+1=-3.46\).

**5.4.** In (4.6), check that \(11(2-2\cdot0.996)=0.088\), and that \(0.088+\rho<\frac12\) leaves room for every \(\rho<\frac1{10}\).

**5.5.** Let \(f\) be continuously differentiable on \([j-1,j+2]\). Show that \(\sup_{[j,j+1]}|f|^2\)\(\le\frac13\int_{j-1}^{j+2}|f|^2+2\int_{j-1}^{j+2}|f||f'|\).

## 6. Solutions

**5.1.** \(\log(1.002/0.999)\approx0.0029985\) and \(\log(1.003/0.999)\approx0.0039960\), so \(\theta\approx0.7504\). Any \(\theta<1\) makes \((\log U)^\theta=o(\log U)\), so \(\exp(C(\log U)^\theta)\) is smaller than every positive power of \(U\).

**5.2.** If \(\chi^m=1\) and \(z\in\mathbb C^\times\), choose \(w\) with \(w^m=z\); then \(\chi(z)=\chi(w)^m=1\).

**5.3.** \(10(0.5-0.996)=-4.96\), and \(-4.96+1.5=-3.46\).

**5.4.** \(2-1.992=0.008\) and \(11\cdot0.008=0.088\); \(0.088+0.1=0.188<0.5\).

**5.5.** For \(t\in[j,j+1]\) and \(t'\in[j-1,j+2]\), \(|f(t)|^2\le|f(t')|^2+2\int_{j-1}^{j+2}|f||f'|\); average over \(t'\).

## Sources

- [OpenAI-029] OpenAI, *Primitive roots for every admissible integer base*, OpenAI Math Release preprint, 4 October 2026, Section 8.1. https://github.com/openai/math/tree/main/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026
