# Faber polynomials and a positive kernel

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

On the unit circle, a polynomial in \(\lambda\) is determined by its Fourier coefficients, and Parseval's identity computes its \(L^2\) norm from them. On the boundary of a smooth convex domain \(\Omega\) the role of the powers \(\lambda^k\) is played by the *Faber polynomials* \(b_k\): in the exterior coordinate \(h\) of [An exterior conformal coordinate](an-exterior-conformal-coordinate.md), \(b_k(h(\mu))\) is \(\mu^k\) plus a series in negative powers of \(\mu\). This lesson defines the Faber polynomials, proves that their negative parts are given by coefficients \(s_{kj}\) of a function \(s(\lambda,\mu)\) holomorphic near \(\mathbf T\times\mathbf T\), shows that convexity of \(\Omega\) makes the kernel \(K=1+s+\bar s\) nonnegative with both marginals equal to one, and deduces a two-sided estimate of boundary norms by coefficients (Proposition 4.6). The kernel and the estimate are due to OpenAI [OpenAI-DC, Section 2]; Faber polynomials of a convex domain evaluated at a matrix were studied by Beckermann and Crouzeix [BC]. In classical terms, the \(s_{kj}\) are differentiated Grunsky coefficients of \(h\).

**Setting.** \(\Omega\) is a smooth convex domain, and \(h(\lambda)=c\lambda+\kappa(1/\lambda)\), \(r_0\) and \(\kappa\) are as in Theorem 3.7 of [An exterior conformal coordinate](an-exterior-conformal-coordinate.md): \(c>0\), \(\kappa\) is holomorphic on \(\{|u|<R_0\}\) with \(R_0=1/r_0>1\), \(h\) is injective with \(h'\ne0\) on \(\{|\lambda|>r_0\}\), and for \(\lambda\in\mathbf T\), \(q(\lambda)=\lambda h'(\lambda)\) satisfies the support inequality
\[
\operatorname{Re}\Bigl(\overline{q(\lambda)}\bigl(h(\lambda)-z\bigr)\Bigr)\ge0\qquad(z\in\overline\Omega).
\]
Write \(\kappa(u)=\sum_{j\ge0}\kappa_ju^j\). Integrals over \(\mathbf T\) use \(d\tau(e^{it})=dt/2\pi\). For a matrix \(C\), \(\|C\|\) is the operator norm and \(\|C\|_2=(\operatorname{tr}C^*C)^{1/2}\) the Hilbert–Schmidt norm, which makes \(M_m(\mathbf C)\) a Hilbert space with inner product \(\operatorname{tr}(D^*C)\). Results of complex analysis are cited by number from Lebl's guide in the core course [Complex Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C50).

## 1. Faber polynomials

In the variable \(u=1/\lambda\), \(h(\lambda)=c/u+\kappa(u)\) and \(q(\lambda)=c/u-u\kappa'(u)\), so for \(z\in\mathbf C\)
\[
\frac{q(\lambda)}{h(\lambda)-z}=\frac{c-u^2\kappa'(u)}{c+u\bigl(\kappa(u)-z\bigr)} .
\]
The right side is holomorphic on a disc \(|u|<\epsilon_z\), \(\epsilon_z\le R_0\), on which the denominator does not vanish, and equals \(1\) at \(u=0\).

**Proposition 4.1** (Faber polynomials). Define \(b_k(z)\), for \(|\lambda|>1/\epsilon_z\), by the expansion
\[
\frac{q(\lambda)}{h(\lambda)-z}=\sum_{k\ge0}b_k(z)\lambda^{-k}.
\]
Then \(b_0=1\), and for \(n\ge1\)
\[
\begin{aligned}
cb_n(z)={}&(z-\kappa_0)b_{n-1}(z)-(n-1)\kappa_{n-1}\\
&-\sum_{j=1}^{n-1}\kappa_jb_{n-1-j}(z).
\end{aligned}
\]
So \(b_k\) is a polynomial of degree \(k\) with leading coefficient \(c^{-k}\). Every polynomial of degree at most \(N\) with coefficients in \(M_m(\mathbf C)\) is \(\sum_{k=0}^Nb_kC_k\) for unique \(C_0,\dots,C_N\in M_m(\mathbf C)\).

*Proof.* Multiply the expansion by the denominator:
\[
c-u^2\kappa'(u)=D_z(u)\sum_{k\ge0}b_k(z)u^k,
\]
where
\[
\begin{aligned}
D_z(u)&=c+u\bigl(\kappa(u)-z\bigr)\\
&=c+(\kappa_0-z)u+\sum_{j\ge1}\kappa_ju^{j+1}.
\end{aligned}
\]
The coefficient of \(u^n\) on the left is \(c\) for \(n=0\) and \(-(n-1)\kappa_{n-1}\) for \(n\ge1\); on the right it is \(cb_n+(\kappa_0-z)b_{n-1}+\sum_{j=1}^{n-1}\kappa_jb_{n-1-j}\) (with \(b_{-1}=0\)). Comparing gives \(b_0=1\) and the recursion. By induction on \(n\), the term \((z-\kappa_0)b_{n-1}/c\) has degree \(n\) and leading coefficient \(c^{-n}\), and the other terms have degree less than \(n\). A matrix polynomial \(\sum_{i\le N}D_iz^i\) is then expanded by subtracting \(b_NC_N\) with \(C_N=c^ND_N\) and proceeding downwards; uniqueness holds because \(b_0,\dots,b_N\) are linearly independent. \(\square\)

For the disc \(h(\lambda)=z_0+R\lambda\) the recursion gives \(b_k(z)=((z-z_0)/R)^k\). For the ellipse \(h(\lambda)=\lambda+a/\lambda\) of the example in [An exterior conformal coordinate](an-exterior-conformal-coordinate.md), it gives \(b_1=z\), \(b_2=z^2-2a\), \(b_3=z^3-3az\).

## 2. Separately holomorphic functions on a bidisc

**Lemma 4.2.** Let \(R>0\), \(\Delta=\{|u|<R\}\), and let \(S:\Delta\times\Delta\to\mathbf C\) be continuous and holomorphic in each variable when the other is fixed. Then there are numbers \(\sigma_{kj}\) (\(k,j\ge0\)) with
\[
S(u,v)=\sum_{k,j\ge0}\sigma_{kj}u^kv^j\qquad(u,v\in\Delta),
\]
and for \(0<t<R\), \(|\sigma_{kj}|\le M_tt^{-k-j}\) with \(M_t=\max_{|u|=|v|=t}|S(u,v)|\). The series converges absolutely and uniformly on \(\{|u|,|v|\le t'\}\) for every \(t'<R\).

*Proof.* Let \(0<t'<t<R\) and \(|u|,|v|\le t'\). Let \(C_t\) be the circle of radius \(t\) about \(0\). The Cauchy integral formula in a disc (Theorem 3.2.15), applied in \(v\) and then in \(u\), gives
\[
\begin{aligned}
S(u,v)&=\frac1{2\pi i}\oint_{C_t}\frac{S(u,\eta)}{\eta-v}\,d\eta,\\
S(u,\eta)&=\frac1{2\pi i}\oint_{C_t}\frac{S(\xi,\eta)}{\xi-u}\,d\xi .
\end{aligned}
\]
So \(S(u,v)\) is the iterated integral over \(C_t\times C_t\) of \(S(\xi,\eta)k_{u,v}(\xi,\eta)/(2\pi i)^2\), where \(k_{u,v}(\xi,\eta)=1/((\xi-u)(\eta-v))\). On the circles, \(k_{u,v}=\sum_{k,j}u^kv^j\xi^{-k-1}\eta^{-j-1}\), absolutely and uniformly convergent. Integrating term by term gives the expansion with
\[
\sigma_{kj}=\frac1{(2\pi i)^2}\oint_{C_t}\oint_{C_t}\frac{S(\xi,\eta)\,d\xi\,d\eta}{\xi^{k+1}\eta^{j+1}},
\]
so \(|\sigma_{kj}|\le M_tt^{-k-j}\), and \(|\sigma_{kj}u^kv^j|\le M_t(t'/t)^{k+j}\). The \(\sigma_{kj}\) do not depend on \(t\): for fixed \(v\), \(\sum_j\sigma_{kj}v^j\) is the \(k\)th Taylor coefficient of \(S(\cdot,v)\) at \(0\), and \(\sigma_{kj}\) is the \(j\)th Taylor coefficient of this function of \(v\). \(\square\)

## 3. The mixed coefficients

For \(|\lambda|,|\mu|>r_0\) with \(\lambda\ne\mu\) put
\[
s(\lambda,\mu)=\frac{q(\lambda)}{h(\lambda)-h(\mu)}-\frac\lambda{\lambda-\mu} .
\]
It is defined because \(h\) is injective.

**Theorem 4.3** (OpenAI). There are numbers \(s_{kj}\) (\(k,j\ge1\)) with the following properties.

1. \(s(\lambda,\mu)=\sum_{k,j\ge1}s_{kj}\lambda^{-k}\mu^{-j}\) for \(|\lambda|,|\mu|>r_0\), \(\lambda\ne\mu\); the series converges absolutely and uniformly on \(\{|\lambda|,|\mu|\ge r\}\) for every \(r>r_0\), and so defines \(s\) continuously on the diagonal as well.
2. For every \(\rho\in(r_0,1)\) there is \(C_\rho\) with \(|s_{kj}|\le C_\rho\rho^{k+j}\).
3. For \(k\ge1\) and \(|\mu|>r_0\),
\[
b_k(h(\mu))=\mu^k+\sum_{j\ge1}s_{kj}\mu^{-j}.
\]

*Proof.* Let \(\Delta=\{|u|<R_0\}\). The divided difference
\[
\kappa^{[1]}(u,v)=\int_0^1\kappa'\bigl(v+x(u-v)\bigr)\,dx
\]
is continuous on \(\Delta\times\Delta\) and holomorphic in each variable (by Morera's theorem, as in the proof of Proposition 2.3 of [Smooth convex neighbourhoods](smooth-convex-neighbourhoods.md)); it equals \((\kappa(u)-\kappa(v))/(u-v)\) for \(u\ne v\) and \(\kappa'(u)\) for \(u=v\). So does \(\partial_u\kappa^{[1]}(u,v)=\int_0^1x\,\kappa''(v+x(u-v))\,dx\). Put
\[
\tilde H(u,v)=c-uv\,\kappa^{[1]}(u,v).
\]
For \(u=1/\lambda\) and \(v=1/\mu\) nonzero,
\[
\begin{aligned}
h(\lambda)-h(\mu)&=\frac{c(v-u)}{uv}+\kappa(u)-\kappa(v),\\
\lambda-\mu&=\frac{v-u}{uv},
\end{aligned}
\]
so
\[
\begin{aligned}
\tilde H(u,v)&=\frac{h(\lambda)-h(\mu)}{\lambda-\mu}\quad(u\ne v),\\
\tilde H(u,u)&=h'(\lambda).
\end{aligned}
\]
Hence \(\tilde H\) has no zeros on \(\Delta\times\Delta\): for \(u\ne v\), both nonzero, by injectivity of \(h\); on the diagonal because \(h'\ne0\); and \(\tilde H=c\) where \(u=0\) or \(v=0\).

For \(\lambda\ne\mu\), the function \(H(\lambda,\mu)=(h(\lambda)-h(\mu))/(\lambda-\mu)\) satisfies
\[
\lambda\partial_\lambda H=\frac{q(\lambda)}{\lambda-\mu}-\frac{\lambda H}{\lambda-\mu},
\]
so \(\lambda\partial_\lambda H/H=s\). As \(\lambda\partial_\lambda=-u\partial_u\), \(s(\lambda,\mu)=S(u,v)\) with
\[
S=\frac{uv\bigl(\kappa^{[1]}+u\,\partial_u\kappa^{[1]}\bigr)}{\tilde H}.
\]
The function \(S\) is continuous on \(\Delta\times\Delta\), holomorphic in each variable, and vanishes where \(u=0\) or \(v=0\). By Lemma 4.2, \(S=\sum\sigma_{kj}u^kv^j\); since \(S(0,v)=0=S(u,0)\), \(\sigma_{0j}=\sigma_{k0}=0\). Put \(s_{kj}=\sigma_{kj}\) for \(k,j\ge1\). This gives (1), with uniform convergence on \(\{|u|,|v|\le1/r\}\), and (2) with \(t=1/\rho\) and \(C_\rho=M_{1/\rho}\).

For (3) fix \(\mu\) with \(|\mu|>r_0\) and put \(z=h(\mu)\). For \(|\lambda|\) large,
\[
\begin{aligned}
\frac{q(\lambda)}{h(\lambda)-z}&=\frac\lambda{\lambda-\mu}+s(\lambda,\mu)\\
&=\sum_{k\ge0}\mu^k\lambda^{-k}\\
&\quad+\sum_{k\ge1}\Bigl(\sum_{j\ge1}s_{kj}\mu^{-j}\Bigr)\lambda^{-k},
\end{aligned}
\]
the double series being rearranged by absolute convergence. Both sides are power series in \(1/\lambda\), and comparing coefficients with Proposition 4.1 gives (3). \(\square\)

Statement (3) identifies \(b_k\): if \(\Phi=h^{-1}\) on \(\mathbf C\setminus\overline\Omega\), then \(b_k(z)-\Phi(z)^k\to0\) as \(z\to\infty\), so \(b_k\) is the polynomial part of the Laurent expansion of \(\Phi^k\) at infinity. This is Faber's classical definition.

## 4. The kernel

**Theorem 4.4** (OpenAI). The function on \(\mathbf T\times\mathbf T\)
\[
K(\lambda,\mu)=1+s(\lambda,\mu)+\overline{s(\lambda,\mu)}
\]
is continuous and nonnegative, and for all \(\lambda,\mu\in\mathbf T\)
\[
\begin{aligned}
\int_{\mathbf T}K(\lambda',\mu)\,d\tau(\lambda')&=1,\\
\int_{\mathbf T}K(\lambda,\mu')\,d\tau(\mu')&=1.
\end{aligned}
\]

*Proof.* Continuity follows from Theorem 4.3(1). For distinct \(\lambda,\mu\in\mathbf T\), \(w=\mu/\lambda\ne1\) has modulus one, and
\[
\begin{aligned}
2\operatorname{Re}\frac\lambda{\lambda-\mu}&=\frac1{1-w}+\frac1{1-\bar w}\\
&=\frac{2-w-\bar w}{|1-w|^2}=1.
\end{aligned}
\]
Hence
\[
\begin{aligned}
K(\lambda,\mu)&=2\operatorname{Re}\frac{q(\lambda)}{h(\lambda)-h(\mu)}\\
&=\frac{2\operatorname{Re}\bigl(\overline{q(\lambda)}(h(\lambda)-h(\mu))\bigr)}{|h(\lambda)-h(\mu)|^2},
\end{aligned}
\]
which is nonnegative by the support inequality with \(z=h(\mu)\in\partial\Omega\). By continuity, \(K\ge0\) on the diagonal too. Every term of the absolutely and uniformly convergent series for \(s\) and \(\bar s\) on \(\mathbf T\times\mathbf T\) contains a nonzero power of each variable, so its integral in either variable vanishes, and integrating term by term gives both identities. \(\square\)

Convexity enters only through the support inequality, that is, through \(K\ge0\).

## 5. The coefficient estimate

**Lemma 4.5** (Parseval). Let \(\mathcal H\) be a finite-dimensional complex inner product space, and let \(a_n\in\mathcal H\) (\(n\in\mathbf Z\)) with \(\sum_n\|a_n\|<\infty\). Then \(f(\mu)=\sum_na_n\mu^n\) satisfies \(\int_{\mathbf T}\|f\|^2\,d\tau=\sum_n\|a_n\|^2\).

*Proof.* \(\|f(\mu)\|^2=\sum_{n,n'}\langle a_n,a_{n'}\rangle\mu^n\bar\mu^{n'}\), an absolutely and uniformly convergent double series, and \(\int_{\mathbf T}\mu^n\bar\mu^{n'}d\tau\) is \(1\) for \(n=n'\) and \(0\) otherwise. \(\square\)

**Proposition 4.6** (OpenAI, coefficient estimate). For every \(m\ge1\) and every \(G=\sum_{k=0}^Nb_kC_k\) with \(C_k\in M_m(\mathbf C)\),
\[
\begin{aligned}
\sum_{k=0}^N\|C_k\|_2^2&\le\int_{\mathbf T}\|G(h(\mu))\|_2^2\,d\tau(\mu)\\
&\le\|C_0\|_2^2+2\sum_{k=1}^N\|C_k\|_2^2 .
\end{aligned}
\]

*Proof.* For a continuous \(f:\mathbf T\to M_m(\mathbf C)\) put
\[
(Tf)(\mu)=\int_{\mathbf T}K(\lambda,\mu)f(\lambda)\,d\tau(\lambda).
\]
Since \(K(\cdot,\mu)\,d\tau\) is a probability measure (Theorem 4.4), the Cauchy–Schwarz inequality gives
\[
\|(Tf)(\mu)\|_2^2\le\int_{\mathbf T}K(\lambda,\mu)\|f(\lambda)\|_2^2\,d\tau(\lambda),
\]
and integrating in \(\mu\), with the other marginal,
\[
\int_{\mathbf T}\|Tf\|_2^2\,d\tau\le\int_{\mathbf T}\|f\|_2^2\,d\tau .
\]
Take \(f(\lambda)=\sum_{k=1}^NC_k\lambda^k\). In \(\int K(\lambda,\mu)f(\lambda)\,d\tau(\lambda)\), the term \(1\) contributes \(0\), each term \(\overline{s_{k'j}}\lambda^{k'}\mu^j\) of \(\bar s\) contributes \(0\) because \(k'+k\ge2\), and the terms of \(s\) give
\[
(Tf)(\mu)=\sum_{j\ge1}\Bigl(\sum_{k=1}^Ns_{kj}C_k\Bigr)\mu^{-j}.
\]
By Lemma 4.5 on both sides of the contraction inequality,
\[
\sum_{j\ge1}\Bigl\|\sum_{k=1}^Ns_{kj}C_k\Bigr\|_2^2\le\sum_{k=1}^N\|C_k\|_2^2 .
\]
By Theorem 4.3(3),
\[
\begin{aligned}
G(h(\mu))={}&C_0+\sum_{k=1}^NC_k\mu^k\\
&+\sum_{j\ge1}\Bigl(\sum_{k=1}^Ns_{kj}C_k\Bigr)\mu^{-j},
\end{aligned}
\]
and Lemma 4.5 gives
\[
\begin{aligned}
\int_{\mathbf T}\|G\circ h\|_2^2\,d\tau={}&\|C_0\|_2^2+\sum_{k=1}^N\|C_k\|_2^2\\
&+\sum_{j\ge1}\Bigl\|\sum_{k=1}^Ns_{kj}C_k\Bigr\|_2^2 .
\end{aligned}
\]
The last sum lies between \(0\) and \(\sum_{k\ge1}\|C_k\|_2^2\). \(\square\)

**Example (ellipses).** For \(h(\lambda)=\lambda+a/\lambda\) with \(0\le a<1\),
\[
s(\lambda,\mu)=\frac{a/(\lambda\mu)}{1-a/(\lambda\mu)}=\sum_{k\ge1}a^k(\lambda\mu)^{-k},
\]
so \(s_{kj}=a^k\) for \(j=k\) and \(0\) otherwise, \(b_k(h(\mu))=\mu^k+a^k\mu^{-k}\), and \(K\) is a Poisson kernel (Exercise 4.3). The middle term of Proposition 4.6 is \(\|C_0\|_2^2+\sum_{k\ge1}(1+a^{2k})\|C_k\|_2^2\), which approaches the upper bound when \(a\) is close to \(1\), that is, when the ellipse is close to the segment \([-2,2]\).

## 6. Exercises

**4.1** (easy). Show that \(b_1(z)=(z-\kappa_0)/c\) and \(b_2(z)=(z-\kappa_0)^2/c^2-2\kappa_1/c\).

**4.2** (easy). Show that \(\sum_{j\ge1}|s_{kj}|^2\le1\) for every \(k\ge1\).

**4.3** (medium). For \(h(\lambda)=\lambda+a/\lambda\) with \(0<a<1\), verify the formula for \(s\) in the example, show that
\[
K(\lambda,\mu)=\frac{1-a^2}{|1-a\bar\lambda\bar\mu|^2}\qquad(\lambda,\mu\in\mathbf T),
\]
and show that \(b_k(2\sqrt a\,x)=2a^{k/2}T_k(x)\) for \(k\ge1\), where \(T_k\) is the Chebyshev polynomial with \(T_k(\cos\theta)=\cos k\theta\).

**4.4** (medium). Show that the lower inequality in Proposition 4.6 is an equality for every \(G\) if and only if \(s=0\), and that this happens exactly when \(\Omega\) is a disc.

## 7. Solutions

**4.1.** The recursion with \(n=1\) gives \(cb_1=z-\kappa_0\). With \(n=2\) it gives \(cb_2=(z-\kappa_0)b_1-\kappa_1-\kappa_1b_0\), which is \((z-\kappa_0)^2/c-2\kappa_1\).

**4.2.** Take \(m=1\), \(C_k=1\) and all other coefficients \(0\) in the inequality \(\sum_j|\sum_ks_{kj}C_k|^2\le\sum_k|C_k|^2\) from the proof of Proposition 4.6.

**4.3.** \(h(\lambda)-h(\mu)=(\lambda-\mu)(1-a/(\lambda\mu))\) and \(q(\lambda)=\lambda-a/\lambda\), so
\[
\begin{aligned}
s&=\frac{\lambda-a/\lambda-\lambda+a/\mu}{(\lambda-\mu)(1-a/(\lambda\mu))}\\
&=\frac{a/(\lambda\mu)}{1-a/(\lambda\mu)} .
\end{aligned}
\]
On \(\mathbf T\), \(1/(\lambda\mu)=\bar\lambda\bar\mu\); with \(w=a\bar\lambda\bar\mu\),
\[
\begin{aligned}
K&=1+2\operatorname{Re}\sum_{k\ge1}w^k\\
&=\operatorname{Re}\frac{1+w}{1-w}=\frac{1-|w|^2}{|1-w|^2}.
\end{aligned}
\]
The identity \(b_k(h(\mu))=\mu^k+a^k\mu^{-k}\) holds for \(|\mu|>r_0\), and both sides are holomorphic on \(\mathbf C\setminus\{0\}\), so it holds there by the identity theorem. At \(\mu=\sqrt ae^{i\theta}\), \(h(\mu)=2\sqrt a\cos\theta\) and the right side is \(2a^{k/2}\cos k\theta\). So the two polynomials \(b_k(2\sqrt a\,x)\) and \(2a^{k/2}T_k(x)\) agree on \([-1,1]\), hence everywhere.

**4.4.** By the last formula in the proof of Proposition 4.6, equality for all \(G\) means \(\sum_ks_{kj}C_k=0\) for all \(j\) and all choices of \(C_k\), that is, \(s_{kj}=0\) for all \(k,j\). If \(s=0\), Theorem 4.3(3) gives \(b_1(h(\mu))=\mu\), so \(h(\mu)=c\mu+\kappa_0\) and \(\Omega\) is the disc \(\{|z-\kappa_0|<c\}\). Conversely, for a disc \(\{|z-z_0|<R\}\), the map \(z_0+R\lambda\) satisfies (1) and (2) of Theorem 3.7 in [An exterior conformal coordinate](an-exterior-conformal-coordinate.md), so by the uniqueness in Exercise 3.3 there it equals \(h\) on \(\{|\lambda|>1\}\), and on the whole collar by the identity theorem. For this \(h\), \(s=R\lambda/(R\lambda-R\mu)-\lambda/(\lambda-\mu)=0\).

## References

- [OpenAI-DC] OpenAI, *A direct proof of the complete Crouzeix inequality*, OpenAI Math Release preprint, 26 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026
- [BC] B. Beckermann and M. Crouzeix, *Faber polynomials of matrices for non-convex sets*, Jaen Journal on Approximation 6 (2014), 219–231; arXiv:1310.1356. https://arxiv.org/abs/1310.1356
- J. Lebl, *Guide to Cultivating Complex Analysis: Working the Complex Field*, version 1.9, in the core course [Complex Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C50).
