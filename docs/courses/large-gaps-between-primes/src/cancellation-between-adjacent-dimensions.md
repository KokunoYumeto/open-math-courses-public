# Cancellation between adjacent dimensions

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

[A square with little prime mass in the next interval](a-square-with-little-prime-mass-in-the-next-interval.md) computed, for every family of test functions \(f_0,\dots,f_k\), the three numbers that govern the weight \(Z^2\): its mass \(w=\sum_j\alpha_j\|f_j\|^2\), its prime mass \(\lambda w\) in the first block, and its prime mass

\[
v=\lambda\sum_{j=0}^k\alpha_j\|f_j+Tf_{j+1}\|^2,\qquad\alpha_j=\frac{\lambda^j}{j!},
\]

in the second block, where \(Tf_{j+1}\) integrates out the last variable of \(f_{j+1}\). With one level, \(v\ge\lambda w\) (Exercise 5.2 there). This lesson constructs families with \(w\to1\) and \(v\to0\). The construction alternates signs over a short range of levels \(j\) near \(k\), using product functions for which \(Tf_{j+1}\) is almost exactly \(-f_j\). This proves Proposition 4.1 of [Prime gaps and adjacent intervals](prime-gaps-and-adjacent-intervals.md), and with it the theorem that a positive proportion of prime gaps exceed \(C\log p\).

Product functions restricted to a simplex, controlled through the moments of their squared density, also underlie Maynard's multidimensional sieve [Maynard]; there they make many shifted integers simultaneously prime, here they are combined with alternating signs to make one block nearly prime-free.

We use Chebyshev's inequality \(\mathbb P(|Y-\mathbb EY|\ge x)\le\operatorname{Var}(Y)/x^2\), which follows from \(\mathbf 1_{\{|Y-\mathbb EY|\ge x\}}\le(Y-\mathbb EY)^2/x^2\).

## 1. A one-dimensional profile

**Lemma 1.1.** For all \(\lambda>0\) and \(\beta>0\) there is a nonnegative \(g\in C_c^\infty((0,\infty))\) with

\[
\int_0^\infty g(u)^2\,du=1,\qquad\int_0^\infty g(u)\,du=\sqrt\lambda,\qquad\mu_g:=\int_0^\infty u\,g(u)^2\,du<\beta .
\]

**Proof.** For \(R\ge2\) choose a smooth function \(\phi_R\) on \((0,\infty)\) with \(\phi_R(u)=1/u\) on \([1,R]\), \(0\le\phi_R(u)\le1/u\) everywhere, and support in \([1/2,2R]\). Put

\[
A_R=\int\phi_R,\qquad B_R=\int u\,\phi_R(u)^2\,du,\qquad N_R^2=\int\phi_R^2 .
\]

Then \(A_R\ge\int_1^Rdu/u=\log R\), \(B_R\le\int_{1/2}^{2R}du/u=\log(4R)\), and \(1/2\le1-1/R\le N_R^2\le\int_{1/2}^\infty u^{-2}du=2\). Let \(g_0=\phi_R/N_R\), so \(\int g_0^2=1\) and \(\int g_0=A_R/N_R\). For \(c>0\) put \(g(u)=c^{-1/2}g_0(u/c)\). The substitution \(u=cx\) gives

\[
\int g^2=1,\qquad\int g=c^{1/2}\int g_0,\qquad\int u\,g(u)^2du=c\int x\,g_0(x)^2dx=\frac{cB_R}{N_R^2}.
\]

The choice \(c=\lambda/(\int g_0)^2=\lambda N_R^2/A_R^2\) gives \(\int g=\sqrt\lambda\) and \(\mu_g=\lambda B_R/A_R^2\le\lambda\log(4R)/(\log R)^2\). This is less than \(\beta\) for \(R\) large. \(\square\)

The profile must be spread over many scales. If \(g\ge0\) is supported in \([a,b]\), Cauchy–Schwarz gives \(\lambda=(\int g)^2\le\int u\,g^2\cdot\int_a^bdu/u=\mu_g\log(b/a)\), so a small \(\mu_g\) forces \(b/a\ge e^{\lambda/\mu_g}\). With the smooth cut-offs of the construction, \(\lambda=2\) gives \(\mu_g=0.137\) for \(R=10^6\) and \(\mu_g=0.070\) for \(R=10^{12}\).

## 2. The cancelling family

Fix \(\lambda>0\) and \(0<\beta<\gamma<\tau=1/8\). Choose \(g\) by Lemma 1.1 and put

\[
d=\beta-\mu_g>0,\qquad s_g^2=\int_0^\infty(u-\mu_g)^2g(u)^2\,du,
\]

and let \(B_g\) be an upper bound for the support of \(g\). Fix a smooth \(\chi:[0,\infty)\to[0,1]\) equal to \(1\) on \([0,\beta]\) and to \(0\) on \([\gamma,\infty)\). These are fixed once and for all; only the integer \(k\) below varies.

For an integer \(k\ge4\) put \(r=\lfloor\sqrt k\rfloor\) and \(a=k-r+1\), so that the \(r\) levels \(a\le j\le k\) are the active ones. For \(0\le j\le k\) let

\[
Q_j(t)=k^{j/2}\prod_{i=1}^jg(kt_i),\qquad S_j(t)=t_1+\dots+t_j,\qquad Q_0=1,\ S_0=0,
\]

and define the family

\[
f_j=\frac{(-1)^j}{\sqrt r\sqrt{\alpha_j}}\,Q_j\,\chi(S_j)\quad(a\le j\le k),\qquad f_j=0\quad(0\le j<a).
\]

**Lemma 2.1.**

1. Each \(f_j\) is a real symmetric function in \(C_c^\infty(\Omega_j)\), \(\Omega_j=\{t\in(0,\infty)^j:\sum t_i<\tau\}\), so the family is admissible in the sense of the previous lesson.
2. \(\|Q_j\|=1\), and \(TQ_{j+1}=\sqrt{\lambda/k}\,Q_j\) for \(0\le j<k\).
3. Under the probability density \(Q_j^2\) on \((0,\infty)^j\), the variables \(kt_1,\dots,kt_j\) are independent with density \(g^2\). Hence \(\mathbb E_jS_j=j\mu_g/k\le\mu_g\) and \(\operatorname{Var}_jS_j=js_g^2/k^2\le s_g^2/k\).

**Proof.** (1) If \(g\) is supported in \([b_0,B_g]\) with \(b_0>0\), every coordinate on the support of \(Q_j\) lies in \([b_0/k,B_g/k]\), and \(\chi(S_j)=0\) unless \(S_j<\gamma<\tau\). So the support of \(f_j\) is a compact subset of \(\Omega_j\). Smoothness, reality and symmetry are clear. (2) \(\int Q_j^2=\prod_i\int k\,g(kt_i)^2dt_i=1\), and \(\int_0^\infty Q_{j+1}(t,u)\,du=Q_j(t)\,k^{1/2}\int_0^\infty g(ku)\,du=Q_j(t)k^{-1/2}\sqrt\lambda\). (3) \(Q_j^2(t)\,dt=\prod_ik\,g(kt_i)^2dt_i\) is a product of probability densities, and \(kt_i\) has density \(g^2\), mean \(\mu_g\) and variance \(s_g^2\). Then \(S_j=k^{-1}\sum_i(kt_i)\), and \(j\le k\). \(\square\)

Since \(\alpha_j/\alpha_{j+1}=(j+1)/\lambda\), part (2) gives for the unrestricted products

\[
\sqrt{\alpha_j}\,T\Bigl(\frac{(-1)^{j+1}Q_{j+1}}{\sqrt{\alpha_{j+1}}}\Bigr)=-\sqrt{\frac{j+1}k}\,(-1)^jQ_j .
\]

For \(j\) close to \(k\) the factor \(\sqrt{(j+1)/k}\) is close to \(1\), so the level \(j+1\) almost cancels the level \(j\) in \(v\). The cut-off \(\chi\) is needed to keep the supports inside \(\Omega_j\); it equals \(1\) on most of the mass because \(S_j\) concentrates near \(j\mu_g/k\le\mu_g<\beta\).

**Proposition 2.2.** The family satisfies

\[
1-\frac{s_g^2}{kd^2}\le w\le1,
\]

and, for \(k\ge2B_g/d\),

\[
0\le\frac v\lambda\le\frac2r+\Bigl(\frac rk\Bigr)^2+\frac{4s_g^2}{kd^2}.
\]

In particular \(w\to1\) and \(v\to0\) as \(k\to\infty\).

**Proof.** *The mass.* \(\alpha_j\|f_j\|^2=r^{-1}\mathbb E_j[\chi(S_j)^2]\) for the \(r\) active levels, so \(w=r^{-1}\sum_{j=a}^k\mathbb E_j[\chi(S_j)^2]\le1\). Since \(\chi(S_j)=1\) when \(S_j\le\beta\), and \(S_j>\beta\) implies \(S_j-\mathbb E_jS_j\ge\beta-\mu_g=d\), Chebyshev's inequality gives \(\mathbb E_j[\chi(S_j)^2]\ge1-s_g^2/(kd^2)\).

*Interior levels.* Let \(a\le j\le k-1\). By the definition of \(T\) and the substitution \(u'=ku\),

\[
\sqrt{\alpha_j}\,(f_j+Tf_{j+1})(t)=\frac{(-1)^jQ_j(t)}{\sqrt r}\Bigl[\chi(S_j)-\sqrt{\frac{j+1}{\lambda k}}\int_0^\infty g(u)\,\chi\Bigl(S_j+\frac uk\Bigr)du\Bigr].
\tag{2.1}
\]

Both terms in the bracket lie in \([0,1]\): the first because \(0\le\chi\le1\), the second because it is at most \(\sqrt{(j+1)/(\lambda k)}\int g=\sqrt{(j+1)/k}\le1\). So the bracket has absolute value at most \(1\) everywhere. On the event \(S_j\le\beta-B_g/k\), every cut-off in (2.1) equals \(1\): \(S_j\le\beta\), and \(S_j+u/k\le\beta\) for every \(u\) in the support of \(g\). There the bracket equals \(1-\sqrt{(j+1)/k}\). As \(j+1\ge a+1>k-r\), we have \(0\le1-\sqrt{(j+1)/k}\le1-\sqrt{1-r/k}\le r/k\). For \(k\ge2B_g/d\), the complementary event \(S_j>\beta-B_g/k\) implies \(S_j-\mathbb E_jS_j\ge d-B_g/k\ge d/2\), and has \(\mathbb P_j\)-probability at most \(4s_g^2/(kd^2)\). Hence

\[
\alpha_j\|f_j+Tf_{j+1}\|^2=\frac1r\,\mathbb E_j[\text{bracket}^2]\le\frac1r\Bigl(\Bigl(\frac rk\Bigr)^2+\frac{4s_g^2}{kd^2}\Bigr),
\]

and the \(r-1\) interior levels contribute at most \((r/k)^2+4s_g^2/(kd^2)\) to \(v/\lambda\).

The comparison of the two measures in (2.1) needs no estimate: the probability is taken for \(Q_j^2\), and on the good event the inner integral has its cut-off equal to \(1\) at every point.

*The two ends.* At the top level \(j=k\), \(f_{k+1}=0\) and \(\alpha_k\|f_k\|^2\le1/r\). At \(j=a-1\), \(f_{a-1}=0\) and

\[
\sqrt{\alpha_{a-1}}\,Tf_a=\frac{(-1)^aQ_{a-1}}{\sqrt r}\sqrt{\frac a{\lambda k}}\int_0^\infty g(u)\,\chi\Bigl(S_{a-1}+\frac uk\Bigr)du,
\]

whose squared norm is at most \(\frac1r\cdot\frac a{\lambda k}\cdot\lambda\le\frac1r\). For \(j<a-1\) both \(f_j\) and \(f_{j+1}\) vanish. Adding the contributions proves the bound for \(v/\lambda\). As \(k\to\infty\), \(r\to\infty\) and \(r/k\to0\). \(\square\)

When \(\lambda<\beta\) one may take \(g\) supported in \((0,\beta)\); then all cut-offs equal \(1\) on the supports, \(w=1\), and \(v/\lambda=r^{-1}\bigl(\sum_{j=a}^{k-1}(1-\sqrt{(j+1)/k})^2+1+a/k\bigr)\) exactly (Exercise 6.3). For \(k=10^4\) this is \(0.0199\), against the bound \(2/r+(r/k)^2=0.0201\); for \(k=10^6\) it is \(0.001999\).

## 3. Proof of the weights proposition and of the theorem

**Proof of Proposition 4.1 of the first lesson.** Fix \(\lambda>0\) and a function \(G\) as in Section 2 of the previous lesson, and put

\[
K_\lambda=C_*=\lambda+\lambda^2c_G^2 .
\]

This depends only on \(\lambda\) (through the fixed choice of \(G\)), not on \(\varepsilon\). Let \(\varepsilon>0\). Choose \(\beta\), \(\gamma\), \(g\) and \(\chi\) as in Section 2. By Proposition 2.2 there is a single integer \(k\) for which the family satisfies \(w\ge1/2\) and \(v/w\le\varepsilon\). Fix this family and define

\[
W_X(m)=\frac{Z(m)^2}w\ge0 .
\]

Proposition 2.1 of the previous lesson, applied to this fixed family, gives as \(X\to\infty\):

\[
\mathbb E_XW_X\to1,\quad\mathbb E_X(W_XV_J)\to\lambda,\quad\limsup\mathbb E_X(W_XV_I)\le\frac vw\le\varepsilon,\quad\limsup\mathbb E_X(W_XV_J^2)\le C_*=K_\lambda,
\]

and \(\mathbb E_XW_X^2=\mathbb E_XZ^4/w^2=O_{\lambda,\varepsilon}(1)\). \(\square\)

**Theorem 3.1** (OpenAI, 2026). For every \(C>0\) there are \(c(C)>0\) and \(N_0(C)\) such that \(\#\{1\le n\le N:p_{n+1}-p_n>C\log p_n\}\ge c(C)N\) for all \(N\ge N_0(C)\). Consequently the indices at which \(p_n/n\) increases have positive lower density.

**Proof.** Section 4 of the first lesson deduces the theorem and its corollary from its Proposition 4.1, proved above. \(\square\)

## 4. The order of the choices

The proof fixes its parameters in this order:

1. the threshold \(C\), then \(\lambda=C+1\);
2. the function \(G\), hence \(K_\lambda\);
3. the suppression level \(\varepsilon=\lambda^2/(2K_\lambda)\);
4. \(\beta\), \(\gamma\), \(g\), \(\chi\), and then the number of levels \(k\), so that \(v/w\le\varepsilon\);
5. only then \(X\to\infty\).

The moment asymptotics of the previous lesson hold for each fixed family; their error terms depend on \(k\) and on the functions. No uniformity in \(k\) is needed, because \(k\) is chosen before \(X\). The detector constant \(K_\lambda\) is fixed in step 2, before \(\varepsilon\); this is what allows \(\varepsilon\) to be chosen in terms of \(K_\lambda\). The bound \(M\) for \(\mathbb E_XW_X^2\) is chosen after step 4, and may be very large.

In principle every constant before the limit \(X\to\infty\) can be computed, so \(c(C)\) is explicit up to these computations. The threshold \(N_0(C)\) is not effective: it depends on the rate in the Bombieri–Vinogradov theorem, whose constants come from the Siegel–Walfisz theorem.

## 5. Where this leads

The theorem gives a positive proportion \(c(C)\) of gaps exceeding \(C\log p\), with no useful numerical value. Cramér's model, and Gallagher's work under a uniform form of the Hardy–Littlewood prime-tuple conjecture [Montgomery–Soundararajan], predict the proportion \(e^{-C}\): the gaps, normalized by \(\log p\), should be exponentially distributed.

Earlier unconditional results counted intervals rather than gaps, or reached only thresholds below the average spacing for prime-start counts [BLZ]. Tao showed that thresholds below \(1/4\) can be reached with known results, and that the question for a threshold is equivalent to a definite drop in the density of prime-free intervals between two lengths [Tao-MO]. The adjacent-interval method of the first lesson supplies such a drop through the weights.

The extreme end of the distribution is the subject of the work of Ford, Green, Konyagin, Maynard and Tao [FGKMT], which produces single gaps of size at least a constant times \(\log p\,\log\log p\,\log\log\log\log p/\log\log\log p\). The small end is the subject of the Goldston–Pintz–Yıldırım and Maynard–Tao theorems on bounded gaps, whose weights detect many primes at once, where the weights here suppress them.

## 6. Exercises

**Exercise 6.1.** Let \(g\ge0\) be supported in \([a,b]\subset(0,\infty)\) with \(\int g^2=1\) and \(\int g=\sqrt\lambda\). Prove \(\mu_g\ge\lambda/\log(b/a)\).

**Exercise 6.2.** Show that the bound \(2/r+(r/k)^2\) is minimized, up to constant factors, by \(r\asymp k^{2/3}\), where it is of order \(k^{-2/3}\), and that the proof of Proposition 2.2 works for any choice \(r=r(k)\) with \(r\to\infty\) and \(r/k\to0\).

**Exercise 6.3.** Assume \(\lambda<\beta\). Construct \(g\in C_c^\infty((0,\beta))\) with \(\int g^2=1\) and \(\int g=\sqrt\lambda\). For the family of Section 2 built from this \(g\), show that \(w=1\) and

\[
\frac v\lambda=\frac1r\Bigl(\sum_{j=a}^{k-1}\Bigl(1-\sqrt{\tfrac{j+1}k}\Bigr)^2+1+\frac ak\Bigr).
\]

**Exercise 6.4.** In the family of Section 2, \(f_0=0\) and \(f_j=0\) for \(j<a\). Show that the levels below \(a-1\) contribute nothing to \(v\), and that the scalar level would contribute \(\lambda f_0^2\) if \(f_0\ne0\) and \(a\ge2\).

**Exercise 6.5.** Explain why Proposition 2.1 of the previous lesson cannot simply be applied with \(k=k(X)\to\infty\), and why the proof does not need to.

## 7. Solutions

**6.1.** Write \(g=\bigl(g\sqrt u\bigr)\cdot u^{-1/2}\). Cauchy–Schwarz gives \(\lambda=(\int_a^bg)^2\le\int_a^bu\,g^2\cdot\int_a^bu^{-1}du=\mu_g\log(b/a)\).

**6.2.** The function \(x\mapsto2/x+x^2/k^2\) has derivative \(-2/x^2+2x/k^2\), which vanishes at \(x=k^{2/3}\), where the value is \(3k^{-2/3}\). In the proof, \(r\) enters only through the two end levels (each at most \(1/r\)) and through \(1-\sqrt{(j+1)/k}\le r/k\); both tend to \(0\) when \(r\to\infty\) and \(r/k\to0\).

**6.3.** Fix \(b\) with \(\lambda<b<\beta\), and a smooth nonnegative \(\psi\) supported in \((0,1)\) with \(\kappa=\int\psi/(\int\psi^2)^{1/2}>(\lambda/b)^{1/2}\); this is possible because \(\kappa\) can be made as close to \(1\) as desired by taking \(\psi\) close to the indicator of \((0,1)\). Put \(s=\lambda/\kappa^2<b\) and \(g(u)=s^{-1/2}\psi(u/s)/(\int\psi^2)^{1/2}\). Then \(\int g^2=1\), \(\int g=s^{1/2}\kappa=\sqrt\lambda\), and \(g\) is supported in \((0,s)\), so \(\mu_g<s<\beta\). On the support of \(Q_j\), \(S_j\le js/k\le s<\beta\), and \(S_j+u/k\le(j+1)s/k\le s<\beta\) for \(j<k\), so every cut-off equals \(1\). Hence \(\mathbb E_j[\chi(S_j)^2]=1\) and \(w=1\); the interior brackets equal \(1-\sqrt{(j+1)/k}\) exactly; the top level gives \(1/r\); the bottom level gives \(\frac1r\cdot\frac a{\lambda k}(\int g)^2=\frac a{kr}\).

**6.4.** The \(j\)-th term of \(v\) involves only \(f_j\) and \(f_{j+1}\); both vanish for \(j<a-1\). If \(f_0\ne0\) and \(a\ge2\), then \(f_1=0\), so the \(j=0\) term is \(\lambda\alpha_0|f_0+Tf_1|^2=\lambda f_0^2\).

**6.5.** The error terms in Theorem 1.1 of the correlations lesson, and hence in Proposition 2.1 of the previous lesson, depend on the dimensions, the test functions and the number of shapes, all of which grow with \(k\); nothing controls them uniformly. The proof chooses one finite \(k\) from \(\varepsilon\), before \(X\), so the limit \(X\to\infty\) is taken for a fixed family.

## References

- [OpenAI-Gaps] OpenAI, Positive lower density of large prime gaps, preprint, 25 September 2026. https://github.com/openai/math/tree/main/preprints/Positive-lower-density-of-large-prime-gaps-September-25-2026
- [Maynard] J. Maynard, Small gaps between primes, Annals of Mathematics 181 (2015), 383–413. https://arxiv.org/abs/1311.4600
- [FGKMT] K. Ford, B. Green, S. Konyagin, J. Maynard, T. Tao, Long gaps between primes, Journal of the American Mathematical Society 31 (2018), 65–105. https://arxiv.org/abs/1412.5029
- [BLZ] D. Bazzanella, A. Languasco, A. Zaccagnini, Prime numbers in logarithmic intervals, Transactions of the American Mathematical Society 362 (2010), 2667–2684. https://arxiv.org/abs/0809.2967
- [Tao-MO] T. Tao, answer to "Positive proportion of logarithmic gaps between consecutive primes", MathOverflow, May 2019. https://mathoverflow.net/a/332888
- [Montgomery–Soundararajan] H. L. Montgomery, K. Soundararajan, Primes in short intervals, Communications in Mathematical Physics 252 (2004), 589–617. https://arxiv.org/abs/math/0409258
