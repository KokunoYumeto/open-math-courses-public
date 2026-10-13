# Lipschitz functions are close to juntas

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A *junta* is a function of many variables that depends only on a few of them. This lesson proves a theorem of T. Austin [Austin]: a function on the cube \([0,1]^N\) with values in \([-1,1]\) that is Lipschitz for the sup distance is close, in the mean square, to a junta on a set of coordinates whose size is bounded in terms of the Lipschitz constant and the allowed error only. The number \(N\) of the variables does not enter.

The proof takes the coordinates in which the function has a large derivative, in the mean. That the other coordinates can be averaged out follows from the three inequalities of the earlier lessons: the heat operator \(P_{2t}\) changes the function little, the Poincaré inequality bounds the error of averaging by derivatives, and hypercontractivity makes the derivatives of \(P_{2t}f\) in the coordinates with a small derivative small in the mean square.

- The theorem for trigonometric polynomials on a torus (Theorem 1.1), with its key estimate (Lemma 2.1).
- Lipschitz functions on a torus (Theorem 3.2).
- Lipschitz functions on a cube (Theorem 4.1).
- The size of the bound (Section 5).

The lesson follows [Austin, Section 2]. It uses all three earlier lessons of the course: [Trigonometric polynomials and the heat operators on a torus](trigonometric-polynomials-and-the-heat-operators.md), [A logarithmic Sobolev inequality on the circle](a-logarithmic-sobolev-inequality-on-the-circle.md) for the constant \(c_0=\tfrac74\), and [Hypercontractivity of the heat operators](hypercontractivity-of-the-heat-operators.md).

## 1. The theorem on a torus

Recall that \(E_S\) is the mean over the coordinates outside \(S\), and that \(E_Sf\) is a junta on \(S\).

For \(0<\varepsilon\le1\) define
\[
\begin{gathered}
t=\frac{\varepsilon^2}{100},\qquad b=\tanh\frac{2t}{c_0},\\
a=1-b,\qquad \eta=\Bigl(\frac\varepsilon2\,(2e\,t)^{a/2}\Bigr)^{2/b},\\
q(\varepsilon)=\Bigl\lfloor\frac1\eta\Bigr\rfloor .
\end{gathered}
\]
Then \(0<b<1\), and \(0<\eta<1\) because \(\tfrac\varepsilon2<1\) and \(2et<1\). These numbers depend only on \(\varepsilon\).

**Theorem 1.1.** Let \(0<\varepsilon\le1\) and \(N\ge1\). Let \(f\) be a real trigonometric polynomial on \(\mathbb T^N\) with
\[
\begin{gathered}
\sum_{n=1}^N\|\partial_nf\|_1\le1,\\
\Bigl\|f-\int f\Bigr\|_2\le1 .
\end{gathered}
\]
Then the set \(S=\{n:\ \|\partial_nf\|_1\ge\eta\}\) has at most \(q(\varepsilon)\) elements, and
\[
\|f-E_Sf\|_1<\varepsilon .
\]

The first condition bounds the sum of the mean sizes of the partial derivatives. For a function that is \(1\)-Lipschitz for the sup distance it holds (Lemma 3.1). It does not hold for functions that are only Lipschitz for the Euclidean distance.

## 2. Proof of Theorem 1.1

**Lemma 2.1** (the key estimate). Let \(f\) be a real trigonometric polynomial on \(\mathbb T^N\) with \(\sum_n\|\partial_nf\|_1\le1\) and \(\|f\|_2\le1\). Let \(t>0\), \(b=\tanh(2t/c_0)\), \(a=1-b\), \(\eta>0\) and \(S=\{n:\|\partial_nf\|_1\ge\eta\}\). Then
\[
\|P_{2t}f-E_SP_{2t}f\|_2\le(2e\,t)^{-a/2}\,\eta^{\,b/2} .
\]

**Proof.** For every \(n\) let \(g_n=\partial_nP_tf=P_t\partial_nf\), a real trigonometric polynomial (Corollary 3.3 of the first lesson). Then
\[
\partial_nP_{2t}f=\partial_nP_tP_tf=P_tg_n .
\]
By the Poincaré inequality (Lemma 1.1 of the first lesson) for the trigonometric polynomial \(P_{2t}f\), and by hypercontractivity in the form of Corollary 3.1 of the third lesson,
\[
\begin{aligned}
&\|P_{2t}f-E_SP_{2t}f\|_2^2\le\sum_{n\notin S}\|P_tg_n\|_2^2\\
&\quad\le\sum_{n\notin S}\bigl(\|g_n\|_1^2\bigr)^b\bigl(\|g_n\|_2^2\bigr)^a .
\end{aligned}
\]
By Hölder's inequality for sums with the exponents \(\tfrac1b\) and \(\tfrac1a\), the right side is at most
\[
\Bigl(\sum_{n\notin S}\|g_n\|_1^2\Bigr)^b\Bigl(\sum_{n\notin S}\|g_n\|_2^2\Bigr)^a .
\]
*The first factor.* \(\|g_n\|_1=\|P_t\partial_nf\|_1\le\|\partial_nf\|_1\), and this is less than \(\eta\) for \(n\notin S\). So
\[
\sum_{n\notin S}\|g_n\|_1^2\le\eta\sum_n\|\partial_nf\|_1\le\eta .
\]
*The second factor.* By Lemma 4.2 of the first lesson,
\[
\begin{aligned}
\sum_n\|g_n\|_2^2&=\sum_n\|\partial_nP_tf\|_2^2\\
&\le\frac{\|f\|_2^2}{2et}\le\frac1{2et} .
\end{aligned}
\]
Together, \(\|P_{2t}f-E_SP_{2t}f\|_2^2\le\eta^b(2et)^{-a}\). \(\blacksquare\)

The lemma is where the three tools meet. The derivatives in the coordinates outside \(S\) are small in the norm \(\|\cdot\|_1\), by the choice of \(S\). All derivatives of \(P_tf\) together are bounded in the norm \(\|\cdot\|_2\). Hypercontractivity turns the two facts into a bound in the norm \(\|\cdot\|_2\) that is small for small \(\eta\).

**Proof of Theorem 1.1.** Since \(\eta\,|S|\le\sum_n\|\partial_nf\|_1\le1\), the set \(S\) has at most \(1/\eta\) elements.

Subtracting the constant \(\int f\) from \(f\) changes neither the derivatives nor \(f-E_Sf\). So we may assume \(\int f=0\) and \(\|f\|_2\le1\). With the number \(t\) of Section 1,
\[
\begin{aligned}
f-E_Sf={}&(f-P_{2t}f)\\
&+(P_{2t}f-E_SP_{2t}f)\\
&+E_S(P_{2t}f-f) .
\end{aligned}
\]
The operator \(E_S\) does not increase the norm \(\|\cdot\|_1\), and \(\|\cdot\|_1\le\|\cdot\|_2\). So
\[
\begin{aligned}
\|f-E_Sf\|_1\le{}&2\,\|f-P_{2t}f\|_1\\
&+\|P_{2t}f-E_SP_{2t}f\|_2 .
\end{aligned}
\]
By Lemma 4.1 of the first lesson, \(\|f-P_{2t}f\|_1\le\sqrt{4t}=2\sqrt t\). By Lemma 2.1 and the definition of \(\eta\),
\[
\|P_{2t}f-E_SP_{2t}f\|_2\le(2et)^{-a/2}\eta^{b/2}=\frac\varepsilon2 .
\]
Since \(4\sqrt t=\tfrac4{10}\varepsilon\), this gives \(\|f-E_Sf\|_1\le\tfrac4{10}\varepsilon+\tfrac12\varepsilon<\varepsilon\). \(\blacksquare\)

## 3. Lipschitz functions on a torus

**Lemma 3.1.** Let \(f\) be a real trigonometric polynomial on \(\mathbb T^N\) that is \(L\)-Lipschitz for the sup distance. Then \(\sum_n|\partial_nf(x)|\le L\) for every \(x\), and so \(\sum_n\|\partial_nf\|_1\le L\).

**Proof.** Fix \(x\), and let \(\sigma_n\) be \(1\) if \(\partial_nf(x)\ge0\) and \(-1\) otherwise. For \(0<h<\tfrac12\) the point \(x+h\sigma\) has the sup distance \(h\) from \(x\), so \(f(x+h\sigma)-f(x)\le Lh\). Divide by \(h\) and let \(h\to0\): the left side tends to \(\sum_n\sigma_n\partial_nf(x)=\sum_n|\partial_nf(x)|\). Integrate over \(x\). \(\blacksquare\)

For \(L\ge0\) and \(\tau>0\) put
\[
\begin{gathered}
\varepsilon_{L,\tau}=\min\Bigl\{1,\frac{\tau^2}{8\max\{L,1\}}\Bigr\},\\
J_{\mathbb T}(L,\tau)=q(\varepsilon_{L,\tau}) .
\end{gathered}
\]
This is an integer \(\ge1\).

**Theorem 3.2.** Let \(L\ge0\), \(\tau>0\) and \(N\ge1\). Let \(H:\mathbb T^N\to[-1,1]\) be \(L\)-Lipschitz for the sup distance. Then there is a set \(S\) of at most \(J_{\mathbb T}(L,\tau)\) coordinates with
\[
\|H-E_SH\|_2<\tau .
\]

**Proof.** Let \(L'=\max\{L,1\}\) and \(\varepsilon=\varepsilon_{L,\tau}\), so that \(\varepsilon\le\tau^2/(8L')\).

*A trigonometric polynomial.* First let \(H\) be, in addition, a trigonometric polynomial, and \(f=H/L'\). By Lemma 3.1, \(\sum_n\|\partial_nf\|_1\le L/L'\le1\). The constant \(\int f\) is the constant nearest to \(f\) in the norm \(\|\cdot\|_2\), so \(\|f-\int f\|_2\le\|f\|_2\le1\). Theorem 1.1 gives a set \(S\) with at most \(q(\varepsilon)\) elements and \(\|f-E_Sf\|_1<\varepsilon\), that is, \(\|H-E_SH\|_1<L'\varepsilon\). The function \(H-E_SH\) has absolute values of at most \(2\), so
\[
\begin{aligned}
\|H-E_SH\|_2^2&\le2\,\|H-E_SH\|_1\\
&<2L'\varepsilon\le\frac{\tau^2}4 .
\end{aligned}
\]
So \(\|H-E_SH\|_2<\tau/2\).

*The general case.* \(H\) is continuous. Let \(H_m\) be its Fejér means. By Lemma 2.2 of the first lesson, \(H_m\) is a real trigonometric polynomial with values in \([-1,1]\) that is \(L\)-Lipschitz for the sup distance, and \(H_m\to H\) uniformly. Take \(m\) with \(\sup|H-H_m|\le\tau/4\), and the set \(S\) of the first part for \(H_m\). Since \(E_S\) does not increase the norm,
\[
\begin{aligned}
\|H-E_SH\|_2\le{}&\|H-H_m\|_2\\
&+\|H_m-E_SH_m\|_2\\
&+\|E_S(H_m-H)\|_2\\
<{}&\frac\tau4+\frac\tau2+\frac\tau4 .
\end{aligned}
\]
\(\blacksquare\)

## 4. Lipschitz functions on a cube

For a bounded Borel function \(f\) on the cube \([0,1]^N\), the means \(E_nf\) and \(E_Sf\) and the norms are defined as on the torus, with the Lebesgue measure of the cube.

**Theorem 4.1** (T. Austin). For every \(L\ge0\) and every \(\tau>0\) there is an integer \(J(L,\tau)\ge1\) with the following property. Let \(N\ge1\), and let \(f:[0,1]^N\to[-1,1]\) satisfy, for all \(x,y\in[0,1]^N\),
\[
|f(x)-f(y)|\le L\max_{1\le k\le N}|x_k-y_k| .
\]
Then there is a set \(S\subset\{1,\dots,N\}\) with at most \(J(L,\tau)\) elements such that
\[
\|f-E_Sf\|_2<\tau .
\]
One can take \(J(L,\tau)=J_{\mathbb T}(2L,\tau)\).

**Proof.** *The fold.* For a real number \(\theta\) let \(\|\theta\|\) be its distance to the nearest integer. The function \(\theta\mapsto2\|\theta\|\) has the period \(1\) and values in \([0,1]\); on \([0,\tfrac12]\) it is \(2\theta\), and on \([\tfrac12,1]\) it is \(2-2\theta\). It satisfies \(|2\|\theta\|-2\|\theta'\||\le2\|\theta-\theta'\|\). For a bounded Borel function \(\varphi\) on \([0,1]\),
\[
\begin{aligned}
\int_0^1\varphi(2\|\theta\|)\,d\theta&=\int_0^{1/2}\varphi(2\theta)\,d\theta\\
&\quad+\int_{1/2}^1\varphi(2-2\theta)\,d\theta\\
&=\int_0^1\varphi .
\end{aligned}
\]
Let \(\Phi:\mathbb T^N\to[0,1]^N\) be the map \(\Phi(x)=(2\|x_1\|,\dots,2\|x_N\|)\). Applying the last formula in one coordinate, and then in all, gives for every bounded Borel function \(k\) on the cube
\[
\begin{gathered}
E_n(k\circ\Phi)=(E_nk)\circ\Phi,\\
\int_{\mathbb T^N}k\circ\Phi=\int_{[0,1]^N}k .
\end{gathered}
\]

*The function on the torus.* Let \(H=f\circ\Phi\). It has values in \([-1,1]\), and
\[
\begin{aligned}
|H(x)&-H(x')|\\
&\le L\max_n\bigl|2\|x_n\|-2\|x'_n\|\bigr|\\
&\le2L\,d_\infty(x,x') .
\end{aligned}
\]
By Theorem 3.2 there is a set \(S\) with at most \(J_{\mathbb T}(2L,\tau)\) elements and \(\|H-E_SH\|_2<\tau\). By the two formulas for \(\Phi\), \(E_SH=(E_Sf)\circ\Phi\) and
\[
\begin{aligned}
\|f-E_Sf\|_2&=\|(f-E_Sf)\circ\Phi\|_2\\
&=\|H-E_SH\|_2<\tau .
\end{aligned}
\]
\(\blacksquare\)

Theorem 4.1 is the case of the interval \([0,1]\) with the Lebesgue measure, and of functions with a Lipschitz condition, of [Austin, Theorem 1.1]. That theorem holds for products of a compact metric space whose measure has a connected and locally connected support, and for functions with any given modulus of continuity; this generality is not proved here.

## 5. The size of the bound

The proof gives the bound \(q(\varepsilon)=\lfloor1/\eta\rfloor\) with
\[
\log\frac1\eta=\frac2b\Bigl(\log\frac2\varepsilon+\frac a2\log\frac1{2et}\Bigr),
\]
where \(t=\varepsilon^2/100\), \(b=\tanh(2t/c_0)\) and \(a=1-b\) as in Section 1.
For small \(\varepsilon\), \(b\) is about \(2t/c_0=\varepsilon^2/(50c_0)\). So \(\log q(\varepsilon)\) grows like \(\varepsilon^{-2}\log\tfrac1\varepsilon\): the bound is finite and explicit, and very large. For \(\varepsilon=1\) the number \(q(\varepsilon)\) has \(163\) decimal digits, and for \(\varepsilon=\tfrac1{10}\) about \(51{,}000\). In Theorem 4.1, \(\varepsilon\) is \(\tau^2/(8\max\{2L,1\})\) for small \(\tau\).

A better constant \(c_0\) in the logarithmic Sobolev inequality improves the bound, but not its form. For particular functions far fewer coordinates suffice (Exercises 6.1 and 6.4).

## 6. Exercises

**6.1.** Let \(f(x)=\tfrac1{4N}\sum_{n=1}^N\cos(2\pi x_n)\) on \(\mathbb T^N\). Show that \(f\) satisfies the conditions of Theorem 1.1, find the set \(S\) for a given \(\eta\), and compute \(\|f-E_Sf\|_2\).

**6.2.** In the proof of Theorem 1.1, where is each of the two conditions on \(f\) used?

**6.3.** For \(N=1\) and \(k(w)=w\), compute \(k\circ\Phi\) and check \(\int_{\mathbb T}k\circ\Phi=\int_0^1k\).

**6.4.** Let \(f(x)=\max_nx_n\) on \([0,1]^N\). Show that \(f\) satisfies the condition of Theorem 4.1 with \(L=1\), that \(\|f-1\|_2^2=\tfrac2{(N+1)(N+2)}\), and that for \(\tau=\tfrac1{10}\) and every \(N\) there is a set \(S\) of at most \(12\) coordinates with \(\|f-E_Sf\|_2<\tau\).

**6.5.** Let \(M>0\). Derive from Theorem 4.1: a function \(f:[0,1]^N\to[-M,M]\) with the Lipschitz condition of the theorem has a set \(S\) of at most \(J(L/M,\tau/M)\) coordinates with \(\|f-E_Sf\|_2<\tau\).

## 7. Solutions

**6.1.** \(\partial_nf=-\tfrac{2\pi}{4N}\sin(2\pi x_n)\), and \(\int_0^1|\sin2\pi u|\,du=\tfrac2\pi\). So \(\|\partial_nf\|_1=\tfrac1N\), and the sum over \(n\) is \(1\). Also \(\int f=0\) and \(\|f\|_2^2=\tfrac1{16N^2}\cdot N\cdot\tfrac12\le1\). If \(\eta\le\tfrac1N\), then \(S\) is the set of all coordinates and \(f-E_Sf=0\). If \(\eta>\tfrac1N\), then \(S\) is empty, \(E_Sf=0\), and \(\|f-E_Sf\|_2=\|f\|_2=(32N)^{-1/2}\), which is small because \(N>1/\eta\) is large.

**6.2.** The condition on the derivatives is used three times: for the number of the elements of \(S\); in Lemma 4.1 of the first lesson, for \(\|f-P_{2t}f\|_1\le2\sqrt t\); and in the first factor of Lemma 2.1. The condition on the norm is used in the second factor of Lemma 2.1, through Lemma 4.2 of the first lesson.

**6.3.** \(k\circ\Phi(x)=2\|x\|\), which is \(2x\) on \([0,\tfrac12]\) and \(2-2x\) on \([\tfrac12,1]\). Its integral is \(\tfrac14+\tfrac14=\tfrac12=\int_0^1w\,dw\).

**6.4.** If \(|x_n-y_n|\le\epsilon\) for all \(n\), then \(\max_nx_n\le\max_ny_n+\epsilon\), and the same with \(x\) and \(y\) exchanged. The largest coordinate \(V\) of a uniform point has \(\Pr(V\le u)=u^N\), so
\[
\begin{aligned}
\|f-1\|_2^2&=\int_0^1(1-u)^2Nu^{N-1}\,du\\
&=\frac{2}{(N+1)(N+2)} .
\end{aligned}
\]
For \(N\ge13\) this is at most \(\tfrac2{210}<\tfrac1{100}\); since \(E_\varnothing f=\int f\) is the constant nearest to \(f\), the empty set does it. For \(N\le12\) take all coordinates.

**6.5.** The function \(f/M\) has values in \([-1,1]\) and satisfies the condition with \(L/M\). Theorem 4.1 for \(f/M\) with \(\tau/M\) gives \(S\) with \(\|f/M-E_S(f/M)\|_2<\tau/M\).

## References

- [Austin] T. Austin, *On the failure of concentration for the \(\ell_\infty\)-ball*, arXiv:1309.3315, version 4, Theorems 1.1, 1.2 and 2.1 and Section 2. https://arxiv.org/abs/1309.3315
