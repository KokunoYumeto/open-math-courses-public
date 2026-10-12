# Gaussian damping and Fourier pairs

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

[The sine product and cardinal functions](the-sine-product-and-cardinal-functions.md) constructs entire functions \(p\) with prescribed values and derivatives at the nodes. The normalized statement \((\mathrm N_k)\) of [Shells and Gaussian duality](shells-and-gaussian-duality.md) is about a radial function \(e^{-\pi hs}H_1(s)\) on the plane, with \(s=b|x|^2\), and its Fourier transform \(e^{-\pi hs}H_2(s)\). This lesson computes the Fourier transform of \(e^{-\pi hs}p(s)\) for a cardinal function \(p\), and writes down the equations that the construction has to solve.

- The Fourier transform of the planar Gaussian \(e^{-\pi\gamma|x|^2}\) with a complex parameter \(\gamma\), \(\operatorname{Re}\gamma>0\), is \(\gamma^{-1}e^{-\pi|\xi|^2/\gamma}\) (Proposition 1.2).
- For a cardinal function \(p\) there is an entire function \(K_p\), given by an explicit integral, such that \(e^{-\pi hs}p(s)\) and \(e^{-\pi hs}K_p(s)\) are Fourier transforms of each other (Theorem 3.2). The function \(K_p\) and all its derivatives decay exponentially on \([0,\infty)\).
- For two coefficient lists, \(H_1=p_1+K_{p_2}\) and \(H_2=p_2+K_{p_1}\) give an admissible radial function and its transform. So \((\mathrm N_k)\) holds as soon as two lists are found for which \(H_1\) and \(H_2\) have the required contacts and signs (Corollary 3.3).
- The contact conditions form a linear system for the two lists, written with an operator \(S\) on lists. The operator \(S\) is bounded, with norm less than \(4000\) (Proposition 4.1).

The lesson follows [OpenAI-T, Section 2, the parts on Gaussian damping and on the jet operator]. It uses Fubini's theorem and dominated convergence (core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10)) and power series (core course [Complex Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C50)).

## 1. Gaussians with a complex parameter

**Lemma 1.1.** Let \(U\) be an open interval of \(\mathbb R\) or a convex open subset of \(\mathbb C\), and \(F\colon\mathbb R\times U\to\mathbb C\) a function with these properties: for every \(u\in U\) the function \(x\mapsto F(x,u)\) is integrable; for every \(x\) the function \(u\mapsto F(x,u)\) is differentiable (complex differentiable if \(U\subset\mathbb C\)), with derivative \(F_u(x,u)\); and there is an integrable function \(G\) with \(|F_u(x,u)|\le G(x)\) for all \(x\) and \(u\). Then \(\Phi(u)=\int F(x,u)\,dx\) is differentiable on \(U\) (complex differentiable if \(U\subset\mathbb C\)), and
\[
\Phi'(u)=\int F_u(x,u)\,dx .
\]

**Proof.** Fix \(x\) and two points \(u\ne u'\) of \(U\). The function \(\varphi(\tau)=F(x,u+\tau(u'-u))\) on \([0,1]\) is differentiable with \(|\varphi'(\tau)|\le|u'-u|\,G(x)\). Choose a complex number \(\omega\) of absolute value \(1\) with \(\omega(\varphi(1)-\varphi(0))=|\varphi(1)-\varphi(0)|\). The mean value theorem for the real function \(\operatorname{Re}(\omega\varphi)\) gives
\[
|F(x,u')-F(x,u)|\le|u'-u|\,G(x).
\]
So the difference quotients \((F(x,u')-F(x,u))/(u'-u)\) are bounded by \(G(x)\), and they converge to \(F_u(x,u)\) as \(u'\to u\). By dominated convergence \((\Phi(u')-\Phi(u))/(u'-u)\) converges to \(\int F_u(x,u)\,dx\). \(\blacksquare\)

**Proposition 1.2.** Let \(\gamma\) be a complex number with \(\operatorname{Re}\gamma>0\). For every \(\xi\in\mathbb R^2\),
\[
\begin{gathered}
\int_{\mathbb R^2}e^{-\pi\gamma|x|^2}e^{-2\pi ix\cdot\xi}\,dx\\
=\gamma^{-1}e^{-\pi|\xi|^2/\gamma}.
\end{gathered}
\]

**Proof.** Let \(\rho=\operatorname{Re}\gamma\). For real \(\xi\) and \(x\) write \(E_\xi(x)=e^{-2\pi ix\xi}\), and let
\[
F_\gamma(\xi)=\int_{\mathbb R}e^{-\pi\gamma x^2}E_\xi(x)\,dx .
\]
The integrand has absolute value \(e^{-\pi\rho x^2}\).

*Step 1: the dependence on \(\xi\).* By Lemma 1.1 with the parameter \(\xi\) and \(G(x)=2\pi|x|e^{-\pi\rho x^2}\),
\[
F_\gamma'(\xi)=\int(-2\pi ix)\,e^{-\pi\gamma x^2}E_\xi(x)\,dx .
\]
Here \((-2\pi ix)e^{-\pi\gamma x^2}\) is the derivative in \(x\) of \((i/\gamma)e^{-\pi\gamma x^2}\), and the derivative of \(E_\xi\) is \(-2\pi i\xi E_\xi\). Integrate by parts over \([-R,R]\) and let \(R\to\infty\); the boundary terms have absolute value \(e^{-\pi\rho R^2}/|\gamma|\) and tend to \(0\). The result is
\[
\begin{aligned}
F_\gamma'(\xi)&=-\frac i\gamma\int e^{-\pi\gamma x^2}E_\xi'(x)\,dx\\
&=-\frac{2\pi\xi}\gamma\,F_\gamma(\xi).
\end{aligned}
\]
So the derivative of \(F_\gamma(\xi)e^{\pi\xi^2/\gamma}\) is zero, and
\[
\begin{gathered}
F_\gamma(\xi)=I(\gamma)\,e^{-\pi\xi^2/\gamma},\\
I(\gamma)=\int_{\mathbb R}e^{-\pi\gamma x^2}\,dx .
\end{gathered}
\]

*Step 2: \(\gamma I(\gamma)^2=1\).* Let \(\delta>0\). On the half-plane \(\operatorname{Re}\gamma>\delta\), Lemma 1.1 with the parameter \(\gamma\) and \(G(x)=\pi x^2e^{-\pi\delta x^2}\) shows that \(I\) is complex differentiable with
\[
I'(\gamma)=-\pi\int x^2e^{-\pi\gamma x^2}\,dx .
\]
Since \(xe^{-\pi\gamma x^2}\) is the derivative of \(-(2\pi\gamma)^{-1}e^{-\pi\gamma x^2}\), integration by parts gives
\[
\int x\cdot xe^{-\pi\gamma x^2}\,dx=\frac1{2\pi\gamma}\,I(\gamma).
\]
So \(I'(\gamma)=-I(\gamma)/(2\gamma)\), and the derivative of \(\gamma I(\gamma)^2\) is \(I^2+2\gamma II'=0\). Two points of the half-plane \(\operatorname{Re}\gamma>0\) are joined by a segment, which lies in a half-plane \(\operatorname{Re}\gamma>\delta\); along the segment \(\gamma I(\gamma)^2\) has derivative zero. So \(\gamma I(\gamma)^2\) is constant. At \(\gamma=1\) its value is \(1\), because \(\int e^{-\pi x^2}dx=1\) ([Real-variable calculations for the Fourier examples](course:HA-LCA/prerequisites/src/real-variable-calculations), Theorem 2.1, at the frequency \(0\)).

*Step 3: two variables.* The integrand of the planar integral has absolute value \(e^{-\pi\rho|x|^2}\), which is integrable over \(\mathbb R^2\). By Fubini's theorem the integral is
\[
F_\gamma(\xi_1)F_\gamma(\xi_2)=I(\gamma)^2e^{-\pi|\xi|^2/\gamma},
\]
and \(I(\gamma)^2=\gamma^{-1}\). \(\blacksquare\)

Only the square of \(I(\gamma)\) occurs, so no choice of a square root of \(\gamma\) is needed.

## 2. The transform of a damped exponential

The constants of the construction are
\[
b=\frac{\sqrt3}2,\quad h=\frac25,\quad B=\frac1{b^2}=\frac43 .
\]
For real \(t\) let
\[
\begin{gathered}
\gamma_t=b(h-it),\qquad\lambda(t)=\frac1{\gamma_t},\\
z(t)=\frac{iB}{h-it}-ih .
\end{gathered}
\]
The radial coordinate \(s=b|x|^2\) is used for the variable of a function and for the variable of its Fourier transform.

**Lemma 2.1.** Let \(t\) be real.

1. \(e^{-\pi hs}e^{i\pi ts}=e^{-\pi\gamma_t|x|^2}\) for \(x\in\mathbb R^2\), \(s=b|x|^2\).
2. The Fourier transform of \(x\mapsto e^{-\pi hs}e^{i\pi ts}\) is \(x\mapsto e^{-\pi hs}\lambda(t)e^{i\pi z(t)s}\).
3. The Fourier transform of \(x\mapsto e^{-\pi hs}\lambda(t)e^{i\pi z(t)s}\) is \(x\mapsto e^{-\pi hs}e^{i\pi ts}\).
4. With \(r=t^2+h^2\),
\[
\begin{gathered}
\operatorname{Re}\frac1{\gamma_t}=\frac h{br},\qquad|\lambda(t)|=\frac1{b\sqrt r},\\
\operatorname{Im}z(t)=h\Bigl(\frac Br-1\Bigr),\\
|z(t)|^2=h^2+\frac{B^2-2Bh^2}r .
\end{gathered}
\]
For \(|t|\le1\),
\[
\begin{gathered}
|\lambda(t)|\le\frac5{\sqrt3}<3,\qquad|z(t)|\le\frac{44}{15},\\
\operatorname{Im}z(t)\ge\frac{26}{435},\\
\operatorname{Re}\frac1{\gamma_t}\ge\frac{20}{29\sqrt3}.
\end{gathered}
\]

**Proof.** (1) \(\gamma_t|x|^2=(h-it)\,b|x|^2=hs-its\).

(2) By (1) and Proposition 1.2 with \(\gamma=\gamma_t\), whose real part is \(bh>0\), the transform at \(\xi\) is \(\lambda(t)e^{-\pi|\xi|^2/\gamma_t}\). With \(s=b|\xi|^2\),
\[
\frac{|\xi|^2}{\gamma_t}=\frac s{b^2(h-it)}=\frac{Bs}{h-it},
\]
and \(B/(h-it)=h-iz(t)\) by the definition of \(z\). So \(e^{-\pi|\xi|^2/\gamma_t}=e^{-\pi hs}e^{i\pi z(t)s}\).

(3) By the computation in (2) the function is \(x\mapsto\lambda(t)e^{-\pi|x|^2/\gamma_t}\). The real part of \(1/\gamma_t\) is positive. Proposition 1.2 with the parameter \(1/\gamma_t\) gives the transform \(\lambda(t)\gamma_t\,e^{-\pi\gamma_t|\xi|^2}=e^{-\pi\gamma_t|\xi|^2}\), and (1) applies.

(4) Since \(1/(h-it)=(h+it)/r\),
\[
\begin{gathered}
\frac1{\gamma_t}=\frac{h+it}{br},\\
z(t)=-\frac{Bt}r+ih\Bigl(\frac Br-1\Bigr).
\end{gathered}
\]
This gives the first three formulas, and
\[
\begin{aligned}
|z(t)|^2&=\frac{B^2t^2}{r^2}+\frac{B^2h^2}{r^2}-\frac{2Bh^2}r+h^2\\
&=\frac{B^2}r-\frac{2Bh^2}r+h^2 .
\end{aligned}
\]
Here \(B^2-2Bh^2=\tfrac{16}9-\tfrac{32}{75}=\tfrac{304}{225}>0\). So all four quantities decrease when \(|t|\) increases. At \(t=0\), where \(r=h^2\): \(|\lambda|=1/(bh)=5/\sqrt3\), and \(25/3<9\); \(|z|=B/h-h=\tfrac{10}3-\tfrac25=\tfrac{44}{15}\). At \(|t|=1\), where \(r=\tfrac{29}{25}\): \(B/r=\tfrac{100}{87}\), so \(\operatorname{Im}z=\tfrac25\cdot\tfrac{13}{87}=\tfrac{26}{435}\); and \(h/(br)=\tfrac25\cdot\tfrac2{\sqrt3}\cdot\tfrac{25}{29}=\tfrac{20}{29\sqrt3}\). \(\blacksquare\)

So damping the exponential \(e^{i\pi ts}\) by \(e^{-\pi hs}\) gives a Gaussian with a complex parameter, and the transform is again the damping factor times an exponential, with the complex frequency \(z(t)\) in the upper half-plane.

## 3. The transformed function

**Lemma 3.1.** Let \(m\) be an integrable function on \([-1,1]\), and \(v,w\) bounded measurable complex functions on \([-1,1]\). Then
\[
\Phi(s)=\int_{-1}^1m(t)\,v(t)\,e^{i\pi w(t)s}\,dt
\]
is an entire function of \(s\), and for every \(j\ge0\)
\[
\begin{aligned}
\Phi^{(j)}(s)=\int_{-1}^1&m(t)\,v(t)\,(i\pi w(t))^j\\
&\cdot e^{i\pi w(t)s}\,dt .
\end{aligned}
\]

**Proof.** Let \(M\) be a bound for \(|w|\) and \(N\) a bound for \(|v|\). The partial sums of the series \(e^{i\pi w(t)s}=\sum_j(i\pi w(t)s)^j/j!\) are bounded by \(e^{\pi M|s|}\). By dominated convergence
\[
\begin{gathered}
\Phi(s)=\sum_{j\ge0}a_js^j,\\
a_j=\frac{(i\pi)^j}{j!}\int_{-1}^1m(t)\,v(t)\,w(t)^j\,dt,
\end{gathered}
\]
and \(|a_j|\le(\pi M)^jN\int|m|/j!\). So the power series converges for all \(s\), and \(\Phi\) is entire. Differentiating the series \(j\) times term by term gives the power series, obtained in the same way, of the integral with \(v\) replaced by \(v\cdot(i\pi w)^j\). \(\blacksquare\)

Let \(\mathbf a\) be a coefficient list with entries \(C,c_n,d_n\), let \(W=\sum_n(|c_n|+|d_n|)\), and let \(p\) be its cardinal function. By Theorem 2.2 of [The sine product and cardinal functions](the-sine-product-and-cardinal-functions.md) there is an integrable function \(m\) on \([-1,1]\) with
\[
\begin{gathered}
p(s)=C\,P(s)+\int_{-1}^1m(t)\,e^{i\pi ts}\,dt,\\
\int_{-1}^1|m(t)|\,dt\le36\,W .
\end{gathered}
\]
Recall \(P(s)=\sum_{l=-6}^6P_le^{i\pi t_ls}\) with \(t_l=l/6\) and \(\sum_l|P_l|=25\). Define
\[
\begin{aligned}
K(s)={}&C\sum_{l=-6}^6P_l\,\lambda(t_l)\,e^{i\pi z(t_l)s}\\
&+\int_{-1}^1m(t)\,\lambda(t)\,e^{i\pi z(t)s}\,dt .
\end{aligned}
\]
So \(K\) is obtained from \(p\) by replacing every exponential \(e^{i\pi ts}\) by \(\lambda(t)e^{i\pi z(t)s}\). Let
\[
q=\frac{26\pi}{435},\qquad V=25|C|+36\,W .
\]
Since \(\pi>3.14\), \(q>0.187\).

**Theorem 3.2.** With these notations:

1. \(K\) is entire, and for every \(j\ge0\) and every real \(s\ge0\),
\[
|K^{(j)}(s)|\le3\Bigl(\frac{44\pi}{15}\Bigr)^jV\,e^{-qs}.
\]
2. The functions \(f\) and \(g\) on \(\mathbb R^2\) defined, with \(s=b|x|^2\), by
\[
\begin{gathered}
f(x)=e^{-\pi hs}p(s),\\
g(x)=e^{-\pi hs}K(s)
\end{gathered}
\]
are continuous and bounded in absolute value by \(3Ve^{-\pi hb|x|^2}\). Each is the Fourier transform of the other: \(\widehat f=g\) and \(\widehat g=f\).
3. \(K\) is real on the real axis. It is determined by \(p\): another choice of \(C\) and \(m\) representing the same function \(p\) gives the same \(K\).

**Proof.** (1) The integral is entire by Lemma 3.1 with \(v=\lambda\) and \(w=z\), which are continuous on \([-1,1]\); the finite sum is entire. For real \(s\ge0\) and \(|t|\le1\), Lemma 2.1(4) gives
\[
|e^{i\pi z(t)s}|=e^{-\pi s\operatorname{Im}z(t)}\le e^{-qs},
\]
and \(|\lambda(t)|<3\), \(|\pi z(t)|\le44\pi/15\). With the formula for the derivatives in Lemma 3.1, and the same for the finite sum,
\[
\begin{aligned}
|K^{(j)}(s)|\le{}&3\Bigl(\frac{44\pi}{15}\Bigr)^je^{-qs}\\
&\cdot\Bigl(25|C|+\int|m|\Bigr),
\end{aligned}
\]
and \(25|C|+\int|m|\le V\).

(2) The function \(p\) is entire, so \(f\) is continuous, and \(|p(s)|\le25|C|+\int|m|\le V\) for real \(s\). The bound for \(g\) is (1) with \(j=0\). By Lemma 2.1(1),
\[
\begin{aligned}
f(x)={}&C\sum_lP_l\,e^{-\pi\gamma_{t_l}|x|^2}\\
&+\int_{-1}^1m(t)\,e^{-\pi\gamma_t|x|^2}\,dt .
\end{aligned}
\]
For fixed \(\xi\) the function \((t,x)\mapsto m(t)e^{-\pi\gamma_t|x|^2}e^{-2\pi ix\cdot\xi}\) has absolute value \(|m(t)|e^{-\pi bh|x|^2}\), which is integrable over \([-1,1]\times\mathbb R^2\). By Fubini's theorem the Fourier transform of \(f\) is obtained by transforming the Gaussians under the sum and under the integral. By Lemma 2.1(2) the result is \(e^{-\pi hs}K(s)\) with \(s=b|\xi|^2\). So \(\widehat f=g\).

In the same way
\[
\begin{aligned}
g(x)={}&C\sum_lP_l\,\lambda(t_l)\,e^{-\pi|x|^2/\gamma_{t_l}}\\
&+\int_{-1}^1m(t)\,\lambda(t)\,e^{-\pi|x|^2/\gamma_t}\,dt,
\end{aligned}
\]
and the integrand has absolute value at most \(3|m(t)|e^{-\pi\rho|x|^2}\) with \(\rho=20/(29\sqrt3)\), by Lemma 2.1(4). Fubini's theorem and Lemma 2.1(3) give \(\widehat g=f\).

(3) The function \(p\) is real on the real axis, so \(f\) is real, and \(f\) is even. Hence
\[
\overline{\widehat f(\xi)}=\int f(x)\,e^{2\pi ix\cdot\xi}\,dx=\widehat f(-\xi),
\]
and \(\widehat f(-\xi)=\widehat f(\xi)\) because \(g\) depends only on \(|\xi|\). So \(K(s)\) is real for \(s\ge0\). Then all derivatives of \(K\) at the point \(1\) are real. The entire function \(K\) is the sum of its Taylor series at \(1\), so \(K\) is real on the whole real axis.

If \(C',m'\) is another choice with the same \(p\), and \(K'\) the function it defines, then the proof of \(\widehat f=g\) in (2) applies to \(K'\) as well: for \(s=b|\xi|^2\), both \(e^{-\pi hs}K'(s)\) and \(e^{-\pi hs}K(s)\) are equal to \(\widehat f(\xi)\). So \(K'=K\) on \([0,\infty)\); the two entire functions have the same Taylor series at \(1\) and are equal. \(\blacksquare\)

We write \(K_p\) for the function \(K\) of Theorem 3.2. The map \(p\mapsto K_p\) is linear, since \(p\mapsto f\mapsto\widehat f\) is linear.

**Corollary 3.3.** Let \(\mathbf a_1,\mathbf a_2\) be two coefficient lists with cardinal functions \(p_1,p_2\), and
\[
H_1=p_1+K_{p_2},\qquad H_2=p_2+K_{p_1}.
\]
Then \(H_1\) and \(H_2\) are entire and real on the real axis, the function \(f(x)=e^{-\pi hs}H_1(s)\), \(s=b|x|^2\), is an admissible radial function on \(\mathbb R^2\), and \(\widehat f(x)=e^{-\pi hs}H_2(s)\).

Consequently, let \(k>0\). If the lists can be chosen such that, for all \(s\ge0\) and all \(n\in\mathcal N\),
\[
\begin{gathered}
H_1(s)\le T_k(s),\qquad H_2(s)\ge0,\\
H_1(n)=T_k(n),\qquad H_2(n)=0,
\end{gathered}
\]
then the normalized statement \((\mathrm N_k)\) holds.

**Proof.** Let \(f_i(x)=e^{-\pi hs}p_i(s)\) and \(g_i(x)=e^{-\pi hs}K_{p_i}(s)\) for \(i=1,2\). Then \(f=f_1+g_2\), and by Theorem 3.2(2) \(\widehat f=g_1+f_2\), which is \(e^{-\pi hs}H_2(s)\). The function \(f\) is continuous, real and radial, in particular even. Both \(|f|\) and \(|\widehat f|\) are bounded by a constant multiple of \(e^{-\pi hb|x|^2}\), hence by a constant multiple of \((1+|x|)^{-3}\). So \(f\) is admissible. The last statement is the definition of \((\mathrm N_k)\). \(\blacksquare\)

## 4. Jets and the interpolation system

Recall the numbers \(Q_n\) and \(D_n\) that describe the sine product at a node \(n\), with \(Q_n>7/4\) and \(|D_n|<53/25\) (Proposition 1.2 of [The sine product and cardinal functions](the-sine-product-and-cardinal-functions.md)). For a real function \(\psi\) on \([0,\infty)\) that is differentiable at the points of \(\mathcal N\), the *jet list* \(\mathcal J\psi\) consists of the numbers
\[
\begin{gathered}
(\mathcal J\psi)_{c,n}=\frac{\psi(n)}{Q_n},\\
(\mathcal J\psi)_{d,n}=\frac{\psi'(n)-D_n\psi(n)}{Q_n}
\end{gathered}
\]
for \(n\in\mathcal N\). The map \(\mathcal J\) is linear, and two functions have the same jet list exactly when they have the same value and the same derivative at every node.

For a coefficient list \(\mathbf a\) let \(\mathbf a^+\) be its *positive part*, the numbers \(c_n,d_n\) for \(n\in\mathcal N\). The three remaining entries \(C,c_0,d_0\) are the *extra entries*. By Theorem 2.2(3) of the same lesson,
\[
\mathcal Jp_{\mathbf a}=\mathbf a^+ .
\]
Define the list
\[
S\mathbf a=-\mathcal JK_{p_{\mathbf a}} .
\]
It is indexed by \(n\in\mathcal N\) like a positive part, and it depends linearly on \(\mathbf a\).

**Proposition 4.1.** For every coefficient list \(\mathbf a\),
\[
\begin{gathered}
\sum_{n\in\mathcal N}\bigl(|(S\mathbf a)_{c,n}|+|(S\mathbf a)_{d,n}|\bigr)\\
\le4000\,\bigl(|C|+W\bigr).
\end{gathered}
\]

**Proof.** Let \(K=K_{p_{\mathbf a}}\). By Theorem 3.2(1), \(|K(n)|\le3Ve^{-qn}\) and \(|K'(n)|\le3\cdot\tfrac{44\pi}{15}Ve^{-qn}\). So
\[
\begin{aligned}
&|(S\mathbf a)_{c,n}|+|(S\mathbf a)_{d,n}|\\
&\quad\le\frac{(1+|D_n|)\,|K(n)|+|K'(n)|}{Q_n}\\
&\quad\le\frac{3V}{Q_n}\Bigl(1+|D_n|+\frac{44\pi}{15}\Bigr)e^{-qn}.
\end{aligned}
\]
Since \(44\pi/15<9.22\), the factor in front of \(e^{-qn}\) is at most \(3V\cdot12.34/1.75<22\,V\). The sum of \(e^{-qn}\) over all integers \(n\ge1\) is \(1/(e^q-1)\), and \(e^q-1>q+q^2/2\), which is more than \(0.187+0.017=0.204\). Since \(V\le36(|C|+W)\) and \(22\cdot36/0.204<3883\), the sum is less than \(3883\,(|C|+W)\). \(\blacksquare\)

So \(S\) maps coefficient lists to summable lists indexed by \(\mathcal N\), and the bound does not depend on the position of the nonzero entries.

Let \(\mathbf a_1,\mathbf a_2\) and \(H_1,H_2\) be as in Corollary 3.3. Since \(\mathcal J\) is linear,
\[
\begin{gathered}
\mathcal JH_1=\mathbf a_1^+-S\mathbf a_2,\\
\mathcal JH_2=\mathbf a_2^+-S\mathbf a_1 .
\end{gathered}
\]
Suppose the conditions of Corollary 3.3 hold. Then \(T_k-H_1\) and \(H_2\) are nonnegative on \([0,\infty)\) and vanish at every node, so their derivatives vanish there too (Exercise 5.3 of [Shells and Gaussian duality](shells-and-gaussian-duality.md)). Hence \(\mathcal JH_1=\mathcal JT_k\) and \(\mathcal JH_2=0\), that is,
\[
\begin{gathered}
\mathbf a_1^+-S\mathbf a_2=\mathcal JT_k,\\
\mathbf a_2^+-S\mathbf a_1=0 .
\end{gathered}
\]
These two equations between lists are the *interpolation system*. Since \(T_k(s)=k^{-1}e^{-k(s-1)}\) and \(T_k'(s)=-e^{-k(s-1)}\), the right side is
\[
\begin{gathered}
(\mathcal JT_k)_{c,n}=\frac{e^{-k(n-1)}}{kQ_n},\\
(\mathcal JT_k)_{d,n}=-\Bigl(1+\frac{D_n}k\Bigr)\frac{e^{-k(n-1)}}{Q_n}.
\end{gathered}
\]

The interpolation system is a linear system for the two lists. It is necessary for the conditions of Corollary 3.3, and it expresses exactly that \(H_1\) touches \(T_k\) and \(H_2\) touches \(0\) at every node, with equal values and equal first derivatives. It does not contain the two sign conditions between the nodes; these have to be proved separately for a solution. The system has infinitely many equations, two for each node and each list, and the unknowns are the two positive parts and the six extra entries, which enter only through \(S\mathbf a_1\) and \(S\mathbf a_2\).

## 5. Exercises

**5.1.** The formulas \(\lambda(t)=1/(b(h-it))\) and \(z(t)=iB/(h-it)-ih\) make sense for complex \(t\ne-ih\). Show that \(z(t)\ne-ih\), \(z(z(t))=t\) and \(\lambda(t)\lambda(z(t))=1\).

**5.2.** Show that
\[
\begin{gathered}
\int_{\mathbb R^2}e^{-\pi hb|x|^2}P(b|x|^2)\,dx\\
=\sum_{l=-6}^6\frac{P_l}{b(h-it_l)},
\end{gathered}
\]
and that the right side is a real number.

**5.3.** Compute \(\operatorname{Re}(1/\gamma_t)\) for \(t=0\) and for \(t=1\), to three decimals. What does the result say about the Fourier transform of \(e^{-\pi hs}e^{i\pi ts}\)?

**5.4.** Let \(\mathbf a\) be the list with \(C=1\) and all other entries \(0\). Express \((S\mathbf a)_{c,n}\) by the numbers \(P_l\), and show \(|(S\mathbf a)_{c,n}|<43\,e^{-0.187n}\).

## 6. Solutions

**5.1.** Since \(h-it=-i(t+ih)\), we have \(z(t)+ih=-B/(t+ih)\), which is not zero. Applying this twice, \(z(z(t))+ih=-B/(z(t)+ih)=t+ih\). Also \(\lambda(t)=i/(b(t+ih))\), so
\[
\begin{aligned}
\lambda(t)\,\lambda(z(t))&=\frac i{b(t+ih)}\cdot\frac i{b(z(t)+ih)}\\
&=\frac i{b(t+ih)}\cdot\frac{-i(t+ih)}{bB}\\
&=\frac1{b^2B}=1 .
\end{aligned}
\]

**5.2.** The list with \(C=1\) and all other entries \(0\) has the cardinal function \(P\), with \(m=0\), and \(K_P(s)=\sum_lP_l\lambda(t_l)e^{i\pi z(t_l)s}\). The left side is \(\widehat f(0)\) for \(f(x)=e^{-\pi hs}P(s)\), and by Theorem 3.2(2) \(\widehat f(0)=K_P(0)=\sum_lP_l\lambda(t_l)\). The terms with indices \(l\) and \(-l\) are complex conjugates, because \(P_{-l}=\overline{P_l}\) and \(t_{-l}=-t_l\); so the sum is real.

**5.3.** By Lemma 2.1(4), \(\operatorname{Re}(1/\gamma_0)=1/(bh)=5/\sqrt3\), about \(2.887\), and \(\operatorname{Re}(1/\gamma_1)=20/(29\sqrt3)\), about \(0.398\). The transform has absolute value \(|\lambda(t)|e^{-\pi\operatorname{Re}(1/\gamma_t)|\xi|^2}\). So the transform of the damped exponential with the highest frequency \(t=1\) decays much more slowly than that of the pure damping factor \(t=0\): high frequencies in \(p\) become slowly decaying parts of \(K_p\).

**5.4.** The cardinal function of this list is \(P\), and by the solution of Exercise 5.2
\[
\begin{gathered}
(S\mathbf a)_{c,n}=-\frac{K_P(n)}{Q_n},\\
K_P(n)=\sum_{l=-6}^6P_l\,\lambda(t_l)\,e^{i\pi z(t_l)n}.
\end{gathered}
\]
By Theorem 3.2(1) with \(V=25\), \(|K_P(n)|\le75\,e^{-qn}\). With \(Q_n>7/4\) and \(q>0.187\) this gives \(|(S\mathbf a)_{c,n}|<\tfrac{75}{1.75}e^{-0.187n}\), and \(75/1.75<43\).

## References

- [OpenAI-T] OpenAI, *Universal optimality of the triangular lattice*, OpenAI Math Release preprint, 23 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/Universal-optimality-of-the-triangular-lattice-September-23-2026
