# Trigonometric polynomials and the heat operators on a torus

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This course proves a theorem of T. Austin [Austin]: a function of many variables that is Lipschitz for the sup distance is close to a function of a bounded number of the variables, and the bound does not depend on the number of the variables. The proof uses the heat operators on a torus and one inequality for them, hypercontractivity, which the course proves from a logarithmic Sobolev inequality on the circle.

This first lesson collects the tools: trigonometric polynomials on a torus, their approximation of continuous functions, the heat operators, and three inequalities for the heat operators that are proved with Fourier coefficients.

- Trigonometric polynomials, means over coordinates, and the Poincaré inequality (Lemma 1.1).
- Fejér means: approximation that keeps bounds and Lipschitz constants (Lemma 2.2).
- The heat operators \(P_t\) (Lemmas 3.1, 3.2 and Corollary 3.3).
- \(P_t\) moves a function slowly (Lemma 4.1) and makes it smooth (Lemma 4.2).

The lesson needs the Lebesgue integral with Fubini's theorem and Jensen's inequality ([core course *Measure and Integration*](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10)) and calculus. The plan of the proof and the two lemmas of Section 4 follow [Austin, Section 2].

## 1. Functions on a torus

Let \(\mathbb T=\mathbb R/\mathbb Z\) and \(N\ge1\). A function on \(\mathbb T^N\) is the same as a function on \(\mathbb R^N\) that has the period \(1\) in every coordinate. Its integral \(\int f\) is the integral over the cube \([0,1)^N\); it does not change if \(f\) is translated: \(\int f(x+y)\,dx=\int f(x)\,dx\). For \(1\le p<\infty\) put
\[
\begin{gathered}
\|f\|_p=\Bigl(\int|f|^p\Bigr)^{1/p},\\
\langle f,h\rangle=\int f\,\overline h .
\end{gathered}
\]
Since the total mass is \(1\), \(\|f\|_p\le\|f\|_q\) for \(p\le q\). The *sup distance* of two points of \(\mathbb T^N\) is \(d_\infty(x,y)=\max_n\|x_n-y_n\|\), where \(\|u\|\) is the distance of a real number \(u\) to the nearest integer.

**Characters.** For \(k\in\mathbb Z^N\) let
\[
e_k(x)=e^{2\pi i(k_1x_1+\dots+k_Nx_N)} .
\]
Then \(e_ke_l=e_{k+l}\), \(\overline{e_k}=e_{-k}\), and \(\int e_k\) is \(1\) for \(k=0\) and \(0\) otherwise. So \(\langle e_k,e_l\rangle\) is \(1\) for \(k=l\) and \(0\) otherwise.

A *trigonometric polynomial* is a finite sum \(f=\sum_kc_ke_k\) with complex numbers \(c_k\). The coefficients are determined by \(f\): \(c_k=\langle f,e_k\rangle\). The function \(f\) is real if and only if \(c_{-k}=\overline{c_k}\) for all \(k\). Moreover
\[
\begin{gathered}
\|f\|_2^2=\sum_k|c_k|^2,\\
\partial_nf=\sum_k2\pi i\,k_n\,c_k\,e_k ,
\end{gathered}
\]
where \(\partial_n\) is the partial derivative in the coordinate \(x_n\). The derivatives of a real trigonometric polynomial are real trigonometric polynomials.

**Means over coordinates.** For a bounded Borel function \(f\) and a coordinate \(n\) let \(E_nf\) be the mean of \(f\) over the coordinate \(x_n\): with \(x^{w}\) for the point \(x\) with \(w\) in place of \(x_n\),
\[
(E_nf)(x)=\int_0^1f(x^{w})\,dw .
\]
For a set \(S\subset\{1,\dots,N\}\) let \(E_S\) be the product of the operators \(E_n\) with \(n\notin S\), in any order. The function \(E_Sf\) depends only on the coordinates in \(S\); a function with this property is a *junta on \(S\)*. By Jensen's inequality and Fubini's theorem, \(\|E_nf\|_p\le\|f\|_p\), and so \(\|E_Sf\|_p\le\|f\|_p\).

For a character, \(E_ne_k=e_k\) if \(k_n=0\), and \(E_ne_k=0\) otherwise. So for a trigonometric polynomial
\[
E_Sf=\sum_{k:\ k_n=0\text{ for all }n\notin S}c_ke_k .
\]

**Lemma 1.1** (Poincaré inequality). For a trigonometric polynomial \(f\) on \(\mathbb T^N\) and a set \(S\) of coordinates,
\[
\|f-E_Sf\|_2^2\le\frac1{4\pi^2}\sum_{n\notin S}\|\partial_nf\|_2^2 .
\]

**Proof.** \(f-E_Sf\) is the sum of the terms \(c_ke_k\) over the set \(Z\) of the \(k\) with \(k_n\ne0\) for some \(n\notin S\). For \(k\in Z\), \(\sum_{n\notin S}k_n^2\ge1\). So
\[
\begin{aligned}
\|f-E_Sf\|_2^2&=\sum_{k\in Z}|c_k|^2\\
&\le\sum_k\sum_{n\notin S}k_n^2|c_k|^2 ,
\end{aligned}
\]
and \(\|\partial_nf\|_2^2=\sum_k4\pi^2k_n^2|c_k|^2\). \(\blacksquare\)

## 2. Approximation by trigonometric polynomials

For \(m\ge1\) and \(u\in\mathbb T\) the *Fejér kernel* is
\[
F_m(u)=\sum_{|k|<m}\Bigl(1-\frac{|k|}m\Bigr)e_k(u) .
\]

**Lemma 2.1.** (1) \(F_m(u)=\tfrac1m\bigl|\sum_{j=0}^{m-1}e_j(u)\bigr|^2\ge0\). (2) \(\int F_m=1\). (3) If \(0<\delta\le\tfrac12\) and \(\|u\|\ge\delta\), then \(F_m(u)\le\dfrac1{m\sin^2(\pi\delta)}\).

**Proof.** (1) \(\bigl|\sum_{j<m}e_j\bigr|^2=\sum_{j,l<m}e_{j-l}\), and \(k=j-l\) occurs \(m-|k|\) times. (2) The coefficient of \(e_0\) is \(1\). (3) For \(u\notin\mathbb Z\), the sum of the geometric progression is
\[
\Bigl|\sum_{j=0}^{m-1}e^{2\pi iju}\Bigr|=\frac{|e^{2\pi imu}-1|}{|e^{2\pi iu}-1|}\le\frac{2}{2|\sin\pi u|} ,
\]
and \(|\sin\pi u|\ge\sin\pi\delta\) for \(\|u\|\ge\delta\). \(\blacksquare\)

On \(\mathbb T^N\) let \(K_m(y)=F_m(y_1)\cdots F_m(y_N)\). For a bounded Borel function \(f\) on \(\mathbb T^N\), its *\(m\)-th Fejér mean* is
\[
f_m(x)=\int f(x-y)\,K_m(y)\,dy .
\]

**Lemma 2.2.** Let \(f\) be a bounded Borel function on \(\mathbb T^N\).

1. \(f_m\) is a trigonometric polynomial; it is real if \(f\) is real.
2. If \(a\le f\le b\) for real numbers \(a,b\), then \(a\le f_m\le b\).
3. If \(f\) is \(L\)-Lipschitz for the sup distance, so is \(f_m\).
4. \((E_Sf)_m=E_S(f_m)\) for every set \(S\) of coordinates.
5. If \(f\) is continuous, then \(f_m\to f\) uniformly as \(m\to\infty\).

**Proof.** \(K_m\ge0\) and \(\int K_m=1\) by Lemma 2.1. This gives (2). It also gives (3): \(|f(x-y)-f(x'-y)|\le L\,d_\infty(x,x')\) for every \(y\), and \(f_m(x)-f_m(x')\) is the mean of these differences with the weight \(K_m\).
(1) \(K_m=\sum_k\kappa_ke_k\) with \(\kappa_k=\prod_n(1-|k_n|/m)\) for the \(k\) with all \(|k_n|<m\). The substitution \(z=x-y\) gives \(\int f(x-y)e_k(y)\,dy=\langle f,e_k\rangle\,e_k(x)\). So
\[
f_m=\sum_k\kappa_k\,\langle f,e_k\rangle\,e_k .
\]
If \(f\) is real, \(f_m\) is real because \(K_m\) is real. (4) By Fubini's theorem, \(\langle E_nf,e_k\rangle\) is \(\langle f,e_k\rangle\) if \(k_n=0\) and \(0\) otherwise. With the formula in (1) for \(E_Sf\) and the formula for \(E_S\) on trigonometric polynomials, both sides of (4) are \(\sum\kappa_k\langle f,e_k\rangle e_k\) over the \(k\) with \(k_n=0\) for all \(n\notin S\).

(5) Let \(\epsilon>0\). Since \(f\) is uniformly continuous, there is \(\delta\in(0,\tfrac12]\) with \(|f(x-y)-f(x)|\le\epsilon\) whenever \(d_\infty(y,0)\le\delta\). The set of the \(y\) with \(d_\infty(y,0)>\delta\) is contained in the union of the \(N\) sets \(\{\|y_n\|>\delta\}\), and by Lemma 2.1 the integral of \(K_m\) over each of them is at most \(1/(m\sin^2\pi\delta)\). Hence
\[
\begin{aligned}
|f_m(x)&-f(x)|\\
&\le\int|f(x-y)-f(x)|\,K_m(y)\,dy\\
&\le\epsilon+\frac{2N\sup|f|}{m\sin^2(\pi\delta)} ,
\end{aligned}
\]
which is at most \(2\epsilon\) for large \(m\). \(\blacksquare\)

## 3. The heat operators

Let \(g(z)=(2\pi)^{-1/2}e^{-z^2/2}\) be the density of the standard Gaussian law on \(\mathbb R\). It is even, and
\[
\begin{gathered}
\int g=1,\qquad \int z\,g(z)\,dz=0,\\
\int z^2g(z)\,dz=1 .
\end{gathered}
\]
Write \(g_N(z)=g(z_1)\cdots g(z_N)\) for \(z\in\mathbb R^N\).

**Definition.** For \(t\ge0\) and a bounded Borel function \(f\) on \(\mathbb T^N\), put
\[
(P_tf)(x)=\int_{\mathbb R^N}f\bigl(x+\sqrt{2t}\,z\bigr)\,g_N(z)\,dz .
\]
So \(P_tf(x)\) is the mean of \(f\) at a point that is moved away from \(x\) by a Gaussian vector, each coordinate with the variance \(2t\). \(P_0f=f\). The operators \(P_t\) are the *heat operators*.

**Lemma 3.1.** Let \(f,h\) be bounded real Borel functions on \(\mathbb T^N\) and \(t\ge0\).

1. \(P_t\) is linear; \(P_tf\ge0\) if \(f\ge0\); \(P_t1=1\); \(|P_tf|\le P_t|f|\); and \(P_tf\) is continuous if \(f\) is.
2. \(\int P_tf=\int f\), \(\ \|P_tf\|_p\le\|f\|_p\) for \(1\le p<\infty\), and \(\sup|P_tf|\le\sup|f|\).
3. \(\langle P_tf,h\rangle=\langle f,P_th\rangle\).
4. Let \(P_t'\) be the heat operator in the first coordinate alone and \(P_t''\) the heat operator in the other \(N-1\) coordinates, each applied with the remaining coordinates fixed. Then \(P_t=P_t'P_t''=P_t''P_t'\). Also \(P_tE_S=E_SP_t\) for every set \(S\) of coordinates.

**Proof.** (1) is clear from the definition; continuity follows from the theorem on dominated convergence. (2) By Fubini's theorem and the invariance of the integral under translations,
\[
\begin{aligned}
\int P_tf&=\int g_N(z)\int f(x+\sqrt{2t}\,z)\,dx\,dz\\
&=\int f .
\end{aligned}
\]
By Jensen's inequality for the probability density \(g_N\), \(|P_tf|^p\le P_t(|f|^p)\); integrate. (3) By Fubini's theorem and the substitution \(x'=x+\sqrt{2t}\,z\), the left side is \(\int g_N(z)\int f(x')\,h(x'-\sqrt{2t}\,z)\,dx'\,dz\), and \(g_N(-z)=g_N(z)\). (4) is Fubini's theorem. \(\blacksquare\)

**Lemma 3.2.** \(P_te_k=e^{-4\pi^2|k|^2t}\,e_k\) for every \(k\in\mathbb Z^N\), where \(|k|^2=k_1^2+\dots+k_N^2\).

**Proof.** The definition (applied to the real and the imaginary part) gives \(P_te_k(x)=e_k(x)\prod_n\varphi(2\pi k_n\sqrt{2t})\) with
\[
\begin{aligned}
\varphi(\xi)&=\int e^{i\xi z}g(z)\,dz\\
&=\int\cos(\xi z)\,g(z)\,dz ;
\end{aligned}
\]
the part with the sine vanishes because \(g\) is even. Differentiate under the integral, which is allowed since \(|z|g(z)\) is integrable, use \(g'(z)=-z\,g(z)\), and integrate by parts:
\[
\begin{aligned}
\varphi'(\xi)&=-\int z\sin(\xi z)\,g(z)\,dz\\
&=\int\sin(\xi z)\,g'(z)\,dz=-\xi\,\varphi(\xi).
\end{aligned}
\]
With \(\varphi(0)=1\) this gives \(\varphi(\xi)=e^{-\xi^2/2}\), and \(\tfrac12(2\pi k_n)^2\cdot2t=4\pi^2k_n^2t\). \(\blacksquare\)

**Corollary 3.3.** Let \(f=\sum_kc_ke_k\) be a trigonometric polynomial.

1. \(P_tf=\sum_ke^{-4\pi^2|k|^2t}c_ke_k\). It is a trigonometric polynomial, real if \(f\) is real, and \(P_sP_tf=P_{s+t}f\).
2. \(\partial_nP_tf=P_t\partial_nf\) for every coordinate \(n\).
3. The function \(u(t,x)=P_tf(x)\) is infinitely differentiable in \((t,x)\), and it solves the heat equation
\[
\partial_tu=\partial_1^2u+\dots+\partial_N^2u .
\]
4. \(P_tf\to f\) uniformly as \(t\to0\).

**Proof.** (1) is Lemma 3.2 and linearity. The rest is read from the finite sum in (1): \(\partial_n\) multiplies the term of \(e_k\) by \(2\pi ik_n\), and \(\partial_t\) by \(-4\pi^2|k|^2\). \(\blacksquare\)

## 4. Two inequalities

**Lemma 4.1** (\(P_t\) moves a function slowly). For a real trigonometric polynomial \(f\) on \(\mathbb T^N\) and \(t\ge0\),
\[
\|f-P_tf\|_1\le\sqrt{2t}\,\sum_{n=1}^N\|\partial_nf\|_1 .
\]

**Proof.** Let \(c=\sqrt{2t}\), and for \(z\in\mathbb R^N\) let \(d_z=\sum_nz_n\,\partial_nf\), a real trigonometric polynomial. For \(x\) and \(z\),
\[
f(x+cz)-f(x)=c\int_0^1d_z(x+scz)\,ds .
\]
The function \(P_tf-f\) is the mean of the left side over \(z\). For fixed \(z\) and \(s\), the integral of \(|d_z(x+scz)|\) over \(x\) is \(\|d_z\|_1\), because the integral does not change under translations. So
\[
\begin{aligned}
&\|f-P_tf\|_1\le c\int g_N(z)\,\|d_z\|_1\,dz\\
&\quad=c\int\Bigl(\int|d_z(x)|\,g_N(z)\,dz\Bigr)dx .
\end{aligned}
\]
Fix \(x\) and write \(a_n=\partial_nf(x)\), so that \(d_z(x)=\sum_nz_na_n\). By the Cauchy–Schwarz inequality, and because \(\int z_nz_{n'}g_N(z)\,dz\) is \(1\) for \(n=n'\) and \(0\) otherwise,
\[
\begin{aligned}
&\int|d_z(x)|\,g_N(z)\,dz\\
&\quad\le\Bigl(\int d_z(x)^2\,g_N(z)\,dz\Bigr)^{1/2}\\
&\quad=\Bigl(\sum_na_n^2\Bigr)^{1/2}\le\sum_n|a_n| .
\end{aligned}
\]
Integrate over \(x\). \(\blacksquare\)

**Lemma 4.2** (\(P_t\) makes a function smooth). For a trigonometric polynomial \(f\) on \(\mathbb T^N\) and \(t>0\),
\[
\sum_{n=1}^N\|\partial_nP_tf\|_2^2\le\frac{\|f\|_2^2}{2e\,t} .
\]

**Proof.** By Corollary 3.3, the coefficient of \(e_k\) in \(\partial_nP_tf\) is \(2\pi ik_ne^{-4\pi^2|k|^2t}c_k\). So, with \(v_k=4\pi^2|k|^2\), the left side is
\[
\sum_kv_k\,e^{-2tv_k}\,|c_k|^2 .
\]
The function \(v\mapsto ve^{-2tv}\) on \([0,\infty)\) has its largest value at \(v=\tfrac1{2t}\), where it is \(\tfrac1{2et}\). \(\blacksquare\)

The two lemmas work against each other in the proof of the main theorem: for a small \(t\), the function \(P_tf\) is still close to \(f\), and its derivatives are already controlled in the norm \(\|\cdot\|_2\).

## 5. Exercises

**5.1.** Let \(N=1\). Write \(F_2\) and \(F_3\) as real trigonometric polynomials, and compute the Fejér mean \(f_2\) of \(f(u)=\cos(2\pi u)+\cos(4\pi u)\).

**5.2.** Compute \(P_tf\) for \(f(x)=\cos(2\pi x_1)\cos(2\pi x_2)+\sin(6\pi x_1)\) on \(\mathbb T^2\), and \(E_{\{1\}}P_tf\).

**5.3.** Let \(f\) be a trigonometric polynomial. Show that \(\|P_tf-\int f\|_2\le e^{-4\pi^2t}\|f-\int f\|_2\).

**5.4.** Let \(f\) be a real trigonometric polynomial with \(f\ge\delta\) for a number \(\delta\). Show that \(P_tf\ge\delta\) for all \(t\ge0\).

**5.5.** Let \(f\) be a real trigonometric polynomial on \(\mathbb T^N\) that is \(L\)-Lipschitz for the sup distance. Show that \(\sum_n|\partial_nf(x)|\le L\) for every \(x\). (This is used in the last lesson.)

## 6. Solutions

**5.1.** \(F_2=1+\tfrac12(e_1+e_{-1})\), that is \(F_2(u)=1+\cos(2\pi u)\), and \(F_3(u)=1+\tfrac43\cos(2\pi u)+\tfrac23\cos(4\pi u)\). By Lemma 2.2(1), \(f_2\) multiplies the coefficient of \(e_k\) by \(1-|k|/2\) for \(|k|<2\) and removes the others: \(f_2(u)=\tfrac12\cos(2\pi u)\).

**5.2.** \(\cos(2\pi x_1)\cos(2\pi x_2)\) is a sum of the four characters with \(k=(\pm1,\pm1)\), \(|k|^2=2\), and \(\sin(6\pi x_1)\) of the two with \(k=(\pm3,0)\), \(|k|^2=9\). So
\[
\begin{aligned}
P_tf={}&e^{-8\pi^2t}\cos(2\pi x_1)\cos(2\pi x_2)\\
&+e^{-36\pi^2t}\sin(6\pi x_1),
\end{aligned}
\]
and \(E_{\{1\}}\) keeps the characters with \(k_2=0\): \(E_{\{1\}}P_tf=e^{-36\pi^2t}\sin(6\pi x_1)\).

**5.3.** \(P_tf-\int f=\sum_{k\ne0}e^{-4\pi^2|k|^2t}c_ke_k\), and \(|k|^2\ge1\) for \(k\ne0\). So the square of its norm is at most \(e^{-8\pi^2t}\sum_{k\ne0}|c_k|^2\).

**5.4.** \(f-\delta\ge0\), so \(P_t(f-\delta)\ge0\) by Lemma 3.1(1), and \(P_t\delta=\delta\).

**5.5.** Fix \(x\), and let \(\sigma_n\) be \(1\) if \(\partial_nf(x)\ge0\) and \(-1\) otherwise. For \(0<h<\tfrac12\) the point \(x+h\sigma\) has the sup distance \(h\) from \(x\), so \(f(x+h\sigma)-f(x)\le Lh\). Divide by \(h\) and let \(h\to0\): the left side tends to \(\sum_n\sigma_n\partial_nf(x)=\sum_n|\partial_nf(x)|\).

## References

- [Austin] T. Austin, *On the failure of concentration for the \(\ell_\infty\)-ball*, arXiv:1309.3315, version 4, Section 2. https://arxiv.org/abs/1309.3315
