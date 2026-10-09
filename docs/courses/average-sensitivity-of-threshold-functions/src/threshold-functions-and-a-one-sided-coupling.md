# Threshold functions and a one-sided coupling

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

On the cube \(\Omega=\{-1,1\}^n\), the *average sensitivity* (or *total influence*) of \(f\colon\Omega\to\{-1,1\}\) is
\[
I(f)=\sum_{i=1}^n\mathbb P\bigl(f(X)\neq f(X^{\oplus i})\bigr),
\]
where \(X\) is uniform on \(\Omega\) and \(x^{\oplus i}\) is \(x\) with the \(i\)-th coordinate reversed. It is the average over \(x\) of the sensitivity \(s(f,x)\) of [Sensitivity, block sensitivity and composition](course:sensitivity-and-block-sensitivity/sensitivity-block-sensitivity-and-composition), written for the values \(\pm1\) instead of \(0,1\). A *polynomial threshold function of degree at most \(d\)* is \(f=\operatorname{sgn}p\) for a real polynomial \(p\) of degree at most \(d\), with \(\operatorname{sgn}t=1\) for \(t\ge0\) and \(-1\) for \(t<0\). Gotsman and Linial proposed in 1994 that a certain symmetric function maximizes \(I(f)\) among such functions; this exact form is false, as shown by Chapman [Chapman] and independently by Kim, Maldonado and Wellens [KMW]. The asymptotic form, \(I(f)=O(d\sqrt n)\), remained open: Harsha, Klivans and Meka proved \(I(f)\le2^{O(d)}n^{1-1/(4d+6)}\), Diakonikolas, Raghavendra, Servedio and Tan independently proved \(I(f)\le2^{O(d)}(\log n)\,n^{1-1/(4d+2)}\) [DRST], and Kane proved \(\sqrt n(\log n)^{O(d\log d)}2^{O(d^2\log d)}\) [Kane]. OpenAI proved it in September 2026 with an absolute constant [OpenAI-G]:

**Theorem** (OpenAI). If \(n\ge1\), \(1\le d\le n\), and \(p\) is a real polynomial of degree at most \(d\) in \(n\) variables, then \(f=\operatorname{sgn}p\) on \(\{-1,1\}^n\) satisfies \(I(f)\le8d\sqrt n\).

This course proves it. The present lesson sets up the cube and shows that the order \(d\sqrt n\) is attained by symmetric examples (Proposition 2.2), and proves a probability estimate, the *one-sided coupling* (Lemma 3.1): random variables with the same law whose difference is bounded in one direction only are close in mean square. The lessons [A weighted grading of the cube](a-weighted-grading-of-the-cube.md) and [The Gotsman–Linial bound](the-gotsman-linial-bound.md) build an operator on functions on the cube, weighted by \(|p|\), whose matrix entries count the sensitive edges of \(f\), and turn the degree bound into a one-sided constraint on a pair of binomial random variables.

## 1. The cube

For \(S\subseteq[n]=\{1,\dots,n\}\), the *character* \(\chi_S(x)=\prod_{i\in S}x_i\) is a function \(\Omega\to\{-1,1\}\), with \(\chi_\varnothing=1\), \(\chi_S\chi_T=\chi_{S\triangle T}\) and \(\sum_{x\in\Omega}\chi_S(x)=0\) for \(S\neq\varnothing\) (pair \(x\) with \(x^{\oplus i}\) for some \(i\in S\)). Hence the \(2^n\) characters are orthogonal for \(\langle a,b\rangle=\sum_x\overline{a(x)}b(x)\), with \(\langle\chi_S,\chi_T\rangle=2^n\mathbf 1_{S=T}\), and form a basis of the functions on \(\Omega\). Since \(x_i^2=1\) on \(\Omega\), every monomial agrees on \(\Omega\) with a character of no larger degree; so a real polynomial of degree at most \(d\) agrees on \(\Omega\) with a combination of characters \(\chi_S\), \(|S|\le d\). We say that a function on \(\Omega\) has *Fourier degree at most \(d\)* if it is such a combination.

Counting ordered pairs \((x,x^{\oplus i})\),
\[
I(f)=\frac{|\{(x,y)\in\Omega^2:\ x,y\text{ adjacent},\ f(x)\neq f(y)\}|}{2^n}=\frac1{2^n}\sum_{x\in\Omega}s(f,x),\tag{1.1}
\]
where \(x,y\) are *adjacent* if they differ in exactly one coordinate. In particular \(I(f)\le n\).

## 2. Symmetric examples

Let \(t(x)=\frac12(n+x_1+\dots+x_n)\), the number of coordinates equal to \(1\).

**Proposition 2.1.** Let \(J\subseteq\{0,\dots,n-1\}\) and \(p_J(x)=\prod_{j\in J}\bigl(t(x)-j-\frac12\bigr)\), a polynomial of degree \(|J|\). Then
\[
I(\operatorname{sgn}p_J)=\frac n{2^{n-1}}\sum_{j\in J}\binom{n-1}j.
\]

**Proof.** \(p_J\) never vanishes on \(\Omega\), and its sign changes between adjacent \(x,y\) exactly when \(\{t(x),t(y)\}=\{j,j+1\}\) for some \(j\in J\). There are \((n-j)\binom nj=n\binom{n-1}j\) unordered adjacent pairs with weights \(j\) and \(j+1\), hence twice as many ordered pairs; divide by \(2^n\) as in (1.1). \(\square\)

**Proposition 2.2** (sharpness). Let \(n\ge17\), \(m=n-1\), \(c=\lceil m/2\rceil\), and \(1\le d\le1+\sqrt m/3\). For \(J=\{c,c+1,\dots,c+d-1\}\),
\[
I(\operatorname{sgn}p_J)\ge\tfrac16\,d\sqrt n.
\]

**Proof.** *The central coefficient.* Put \(a_k=\binom{2k}k4^{-k}\). Then \(a_1=\frac12\) and \(a_{k+1}=a_k\frac{2k+1}{2k+2}\), and by induction \(a_k^2\ge\frac1{4k}\): indeed \((2k+1)^2(k+1)\ge k(2k+2)^2\) reduces to \(k+1\ge0\). So \(\binom{2k}k\ge4^k/(2\sqrt k)\). If \(m=2k\), this is \(\binom mc\ge2^m/\sqrt{2m}\); if \(m=2k+1\), then \(c=k+1\) and \(\binom m{k+1}=\binom{2k}k\frac{2k+1}{k+1}\ge4^k/(2\sqrt k)\ge2^m/(2\sqrt{2m})\). In both cases \(\binom mc\ge2^m/(3\sqrt m)\).

*Nearby coefficients.* For \(j=c+u\) with \(u\ge0\), \(\binom m{j+1}/\binom mj=\frac{m-j}{j+1}\ge\frac{(m-1)/2-u}{(m+3)/2+u}\ge1-\frac{4u+4}m\). For \(0\le T\le\sqrt m/3\), using \(\prod(1-\epsilon_u)\ge1-\sum\epsilon_u\) for \(\epsilon_u\in[0,1]\),
\[
\binom m{c+T}\ge\binom mc\Bigl(1-\sum_{u=0}^{T-1}\frac{4u+4}m\Bigr)=\binom mc\Bigl(1-\frac{2T^2+2T}m\Bigr)\ge\frac12\binom mc,
\]
because \(2T^2\le\frac29m\) and \(2T\le\frac23\sqrt m\le\frac16m\) for \(m\ge16\). The numbers \(\epsilon_u=(4u+4)/m\) lie in \([0,1]\), since \(u\le T-1\) gives \(4u+4\le\frac43\sqrt m\le m\).

*Conclusion.* Each \(j\in J\) is \(c+T\) with \(0\le T\le d-1\le\sqrt m/3\), and \(c+d-1\le\frac{m+1}2+\frac{\sqrt m}3\le m\), so each \(\binom mj\ge2^m/(6\sqrt m)\), and by Proposition 2.1
\[
I(\operatorname{sgn}p_J)\ge\frac n{2^m}\cdot d\cdot\frac{2^m}{6\sqrt m}=\frac{nd}{6\sqrt{n-1}}\ge\frac{d\sqrt n}6.\qquad\square
\]

So the bound \(8d\sqrt n\) of the theorem is attained up to a constant factor for \(d\) up to about \(\sqrt n/3\). For \(d\ge\sqrt n/8\) the theorem gives nothing beyond \(I(f)\le n\).

## 3. A one-sided coupling

**Lemma 3.1** (one-sided coupling; OpenAI). Let \(U,V\) be real random variables taking finitely many values, with the same distribution, mean \(\mu\) and variance \(\sigma^2\). If \(V-U\le a\) always, where \(a\ge0\), then
\[
\mathbb E(U-V)^2\le8a\sigma.
\]

**Proof.** Let \(g(t)=\int_\mu^t|z-\mu|\,dz=\frac12(t-\mu)|t-\mu|\), a strictly increasing function. For \(u<v\),
\[
\frac{(v-u)^2}4\le g(v)-g(u)\le\frac{v-u}2\bigl(|u-\mu|+|v-\mu|\bigr).\tag{3.1}
\]
For the lower bound: if \(u\le\mu\le v\), the integral is \(\frac12((\mu-u)^2+(v-\mu)^2)\ge\frac14(v-u)^2\); if, say, \(\mu\le u<v\), it is \(\frac12(v-u)(v+u-2\mu)\ge\frac12(v-u)^2\), and similarly if \(u<v\le\mu\). For the upper bound, \(|z-\mu|\) is convex, so it lies below its chord on \([u,v]\), whose integral is the right-hand side.

Since \(U\) and \(V\) have the same distribution, \(\mathbb Eg(U)=\mathbb Eg(V)\). Let \(Y=g(V)-g(U)\); then \(\mathbb EY=0\), so \(\mathbb E|Y|=2\mathbb E\max\{Y,0\}\), and \(Y>0\) exactly when \(V>U\). On that event \(0<V-U\le a\), so by (3.1)
\[
\mathbb E|Y|=2\,\mathbb E\bigl[\mathbf 1_{V>U}Y\bigr]\le a\,\mathbb E\bigl(|U-\mu|+|V-\mu|\bigr)\le2a\sigma,
\]
using \(\mathbb E|U-\mu|\le(\mathbb E(U-\mu)^2)^{1/2}=\sigma\). By the lower bound in (3.1), \((U-V)^2\le4|g(U)-g(V)|=4|Y|\) always. Taking expectations, \(\mathbb E(U-V)^2\le8a\sigma\). \(\square\)

Nothing is assumed about the joint distribution of \(U\) and \(V\), and \(V-U\) may be very negative on rare events. Equality of the marginals is what balances the two directions, through the cancellation \(\mathbb E[g(V)-g(U)]=0\). Exercise 4.4 shows that the bound has the right order.

## 4. Exercises

**Exercise 4.1** (easy). Compute \(I(f)\) for \(f(x)=x_1\), for \(f=\chi_{[n]}\), and for the majority function \(\operatorname{sgn}(x_1+\dots+x_n)\) with \(n\) odd.

**Exercise 4.2** (easy). Show that \(I(f)=\sum_{S}|S|\,\widehat f(S)^2\), where \(\widehat f(S)=2^{-n}\langle\chi_S,f\rangle\). *Hint:* \(\mathbb P(f(X)\neq f(X^{\oplus i}))=\frac14\mathbb E(f(X)-f(X^{\oplus i}))^2\).

**Exercise 4.3** (medium). Show that the conclusion of Lemma 3.1 fails if \(U\) and \(V\) are not assumed to have the same distribution.

**Exercise 4.4** (medium). Let \(U\) be uniform on \(\{0,1,\dots,L\}\) and \(V=U+1\) if \(U<L\), \(V=0\) if \(U=L\). Show that \(U,V\) have the same distribution, \(V-U\le1\), and \(\mathbb E(U-V)^2=L\), while \(\sigma^2=L(L+2)/12\). Conclude that \(\mathbb E(U-V)^2/(a\sigma)\) can approach \(\sqrt{12}\).

## 5. Solutions

**4.1.** For \(x_1\), only \(i=1\) is sensitive: \(I=1\). For parity every coordinate is sensitive everywhere: \(I=n\). For majority with \(n=2k+1\), coordinate \(i\) is sensitive exactly when the other \(2k\) coordinates are balanced, with probability \(\binom{2k}k4^{-k}\); so \(I=n\binom{2k}k4^{-k}\ge n/(2\sqrt k)\ge\sqrt{n/2}\). This is Proposition 2.1 with \(J=\{k\}\).

**4.2.** \(f(x)-f(x^{\oplus i})=2\sum_{S\ni i}\widehat f(S)\chi_S(x)\), because \(\chi_S(x^{\oplus i})=-\chi_S(x)\) for \(i\in S\) and \(=\chi_S(x)\) otherwise. By orthogonality \(\mathbb E(f(X)-f(X^{\oplus i}))^2=4\sum_{S\ni i}\widehat f(S)^2\), and \((f(x)-f(x^{\oplus i}))^2\) is \(4\) or \(0\). Sum over \(i\).

**4.3.** \(U=0\) and \(V=-L\) satisfy \(V-U\le0\), have variance \(0\), and \(\mathbb E(U-V)^2=L^2\).

**4.4.** \(V\) is a cyclic shift of \(U\), hence uniform. \(U-V=-1\) with probability \(\frac L{L+1}\) and \(U-V=L\) with probability \(\frac1{L+1}\), so \(\mathbb E(U-V)^2=\frac{L+L^2}{L+1}=L\). The variance of the uniform distribution on \(\{0,\dots,L\}\) is \(((L+1)^2-1)/12\). With \(a=1\), \(L/\sqrt{L(L+2)/12}\to\sqrt{12}\approx3.46\), compared with \(8\) in Lemma 3.1.

## References

- [Chapman] B. Chapman, *The Gotsman–Linial conjecture is false*, SODA 2018; arXiv:2108.02288. https://arxiv.org/abs/2108.02288
- [DRST] I. Diakonikolas, P. Raghavendra, R. A. Servedio and L.-Y. Tan, *Average sensitivity and noise sensitivity of polynomial threshold functions*, SIAM J. Comput. 43 (2014); arXiv:0909.5011. https://arxiv.org/abs/0909.5011
- [Kane] D. M. Kane, *The correct exponent for the Gotsman–Linial conjecture*, Comput. Complexity 23 (2014); arXiv:1210.1283. https://arxiv.org/abs/1210.1283
- [KMW] H. W. Kim, C. Maldonado and J. Wellens, *On graphs and the Gotsman–Linial conjecture for d = 2*, arXiv:1709.06650 (2017). https://arxiv.org/abs/1709.06650
- [OpenAI-G] OpenAI, *Average sensitivity of polynomial threshold functions*, OpenAI Math Release preprint, 25 September 2026, Sections 1 and 2. https://github.com/openai/math/tree/main/preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026
