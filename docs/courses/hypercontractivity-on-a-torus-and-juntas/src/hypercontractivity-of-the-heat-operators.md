# Hypercontractivity of the heat operators

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The heat operators \(P_t\) do not increase any of the norms \(\|\cdot\|_p\). This lesson proves more: \(P_t\) maps functions with a finite norm \(\|\cdot\|_p\) to functions whose norm \(\|\cdot\|_q\), for an exponent \(q>p\) that depends on \(t\), is not larger, with the constant \(1\). This is *hypercontractivity*. The constant \(1\) is what allows the passage from the circle to a torus of any dimension without a loss. The proof on the circle differentiates the norm along the heat equation and uses the logarithmic Sobolev inequality of the previous lesson; this method is due to L. Gross.

- Hypercontractivity on the circle (Theorem 1.1).
- An inequality for norms in two groups of variables (Lemma 2.1) and hypercontractivity on a torus (Theorem 2.2).
- The form used in the last lesson (Corollary 3.1).

The lesson uses the heat operators and the Fejér means of [Trigonometric polynomials and the heat operators on a torus](trigonometric-polynomials-and-the-heat-operators.md), and Theorem 5.1 of [A logarithmic Sobolev inequality on the circle](a-logarithmic-sobolev-inequality-on-the-circle.md), with its constant \(c_0=\tfrac74\). It needs Hölder's inequality and Fubini's theorem ([core course *Measure and Integration*](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10)). For the place of the inequality in the proof of the main theorem see [Austin, Section 2].

## 1. The circle

**Theorem 1.1.** Let \(1<p\le q<\infty\) and \(t\ge0\) with
\[
\frac{q-1}{p-1}\le e^{4t/c_0} .
\]
Then \(\|P_tf\|_q\le\|f\|_p\) for every real continuous function \(f\) on \(\mathbb T\). In particular
\[
\begin{gathered}
\|P_tf\|_2\le\|f\|_{p(t)},\\
p(t)=1+e^{-4t/c_0} .
\end{gathered}
\]

**Proof.** *Step 1: a trigonometric polynomial with \(f\ge\delta>0\), and equality in the condition.* Let \(T\ge0\) be the number with \(q-1=(p-1)e^{4T/c_0}\), and for \(0\le t\le T\) put
\[
q(t)=1+(p-1)\,e^{4t/c_0} .
\]
Then \(q'(t)=4\,(q(t)-1)/c_0\).
Let \(u(t,x)=P_tf(x)\). By Corollary 3.3 of the first lesson, \(u\) is infinitely differentiable in \((t,x)\) and \(\partial_tu=\partial_x^2u\); and \(u\ge\delta\), because \(P_t(f-\delta)\ge0\). Hence \((t,x)\mapsto u(t,x)^{q(t)}\) is continuously differentiable, and
\[
\Lambda(t)=\int_0^1u(t,x)^{q(t)}\,dx
\]
can be differentiated under the integral. Write \(q,q',u\) for \(q(t),q'(t),u(t,\cdot)\). Then
\[
\Lambda'=q'\int u^q\log u+q\int u^{q-1}\,\partial_tu .
\]
With the heat equation and an integration by parts over a period,
\[
\int u^{q-1}\partial_x^2u=-(q-1)\int u^{q-2}(\partial_xu)^2 .
\]
Let \(v=u^{q/2}\), a continuously differentiable positive function with \(v^2=u^q\) and \((\partial_xv)^2=\tfrac{q^2}4u^{q-2}(\partial_xu)^2\). So
\[
\begin{aligned}
q\,\Lambda'={}&q'\int v^2\log v^2\\
&-4(q-1)\int(\partial_xv)^2 .
\end{aligned}
\]
Now let \(\mathcal N(t)=\Lambda(t)^{1/q(t)}=\|P_tf\|_{q(t)}\). From \(\log\mathcal N=\tfrac1q\log\Lambda\),
\[
\begin{aligned}
&q^2\Lambda\,\frac{\mathcal N'}{\mathcal N}=q\Lambda'-q'\Lambda\log\Lambda\\
&\quad=q'\operatorname{Ent}(v^2)-4(q-1)\int(\partial_xv)^2 ,
\end{aligned}
\]
since \(\Lambda=\int v^2\). By the logarithmic Sobolev inequality, \(\operatorname{Ent}(v^2)\le c_0\int(\partial_xv)^2\), and \(q'\ge0\). So the right side is at most
\[
\bigl(q'c_0-4(q-1)\bigr)\int(\partial_xv)^2=0 .
\]
Hence \(\mathcal N'\le0\) on \([0,T]\), and \(\|P_Tf\|_q=\mathcal N(T)\le\mathcal N(0)=\|f\|_p\).

*Step 2: the same \(f\), and \(t\ge T\).* By Step 1 and since \(P_{t-T}\) does not increase the norm \(\|\cdot\|_q\) (Lemma 3.1 and Corollary 3.3 of the first lesson), \(\|P_tf\|_q=\|P_{t-T}P_Tf\|_q\le\|P_Tf\|_q\), and this is at most \(\|f\|_p\). So the theorem holds for trigonometric polynomials \(f\ge\delta>0\).

*Step 3: a continuous function \(f\ge0\).* Let \(f_m\) be the Fejér means of \(f\). By Lemma 2.2 of the first lesson, \(f_m\) is a real trigonometric polynomial with \(f_m\ge0\), and \(f_m\to f\) uniformly. For \(\delta>0\), Step 2 gives \(\|P_t(f_m+\delta)\|_q\le\|f_m+\delta\|_p\). Since \(\sup|P_th|\le\sup|h|\), also \(P_tf_m\to P_tf\) uniformly. Let \(m\to\infty\) and then \(\delta\to0\): \(\|P_tf\|_q\le\|f\|_p\).

*Step 4: a real continuous function.* \(|P_tf|\le P_t|f|\), and \(|f|\) is continuous and \(\ge0\). So \(\|P_tf\|_q\le\|P_t|f|\|_q\le\|f\|_p\).

The last statement is the case \(q=2\): then \((q-1)/(p-1)=e^{4t/c_0}\) for \(p=p(t)\). \(\blacksquare\)

The condition of the theorem is not the best possible one. Exercise 4.2 shows that \((q-1)/(p-1)\le e^{8\pi^2t}\) is necessary.

## 2. Several coordinates

**Lemma 2.1.** Let \(1\le p\le2\), and let \(h\) be a real continuous function on \(\mathbb T^a\times\mathbb T^b\), with the points \((x,y)\). Then
\[
\begin{aligned}
&\int\Bigl(\int|h(x,y)|^p\,dx\Bigr)^{2/p}dy\\
&\qquad\le\Bigl(\int\Bigl(\int|h(x,y)|^2\,dy\Bigr)^{p/2}dx\Bigr)^{2/p} .
\end{aligned}
\]

**Proof.** Let \(r=2/p\ge1\), \(k=|h|^p\) and \(G(y)=\int k(x,y)\,dx\). The claim is
\[
\|G\|_r\le\int\|k(x,\cdot)\|_r\,dx ,
\]
with the norms of functions of \(y\): the left side of the lemma is \(\|G\|_r^r\), and \(\|k(x,\cdot)\|_r=(\int|h(x,y)|^2dy)^{p/2}\). For \(r=1\) the claim is Fubini's theorem. Let \(r>1\) and \(r'=r/(r-1)\). If \(\|G\|_r=0\) there is nothing to prove. Otherwise let \(\psi=G^{r-1}/\|G\|_r^{r-1}\). Then \(\psi\ge0\), \(\int\psi^{r'}=1\) and \(\int G\psi=\|G\|_r\). By Fubini's theorem and Hölder's inequality,
\[
\begin{aligned}
\|G\|_r&=\int\!\!\int k(x,y)\,\psi(y)\,dy\,dx\\
&\le\int\|k(x,\cdot)\|_r\,\|\psi\|_{r'}\,dx\\
&=\int\|k(x,\cdot)\|_r\,dx .
\end{aligned}
\]
\(\blacksquare\)

**Theorem 2.2** (hypercontractivity on a torus). Let \(N\ge1\), \(t\ge0\) and \(p=1+e^{-4t/c_0}\). Then for every real continuous function \(f\) on \(\mathbb T^N\)
\[
\|P_tf\|_2\le\|f\|_p .
\]

**Proof.** By induction on \(N\); the case \(N=1\) is Theorem 1.1. Let \(N\ge2\), and write the points of \(\mathbb T^N\) as \((x,y)\) with \(x\in\mathbb T\) and \(y\in\mathbb T^{N-1}\). By Lemma 3.1(4) of the first lesson, \(P_t=P_t'P_t''\), where \(P_t'\) acts on \(x\) and \(P_t''\) on \(y\). Let \(h=P_t''f\), a continuous function.

For every fixed \(y\), \(P_tf(\cdot,y)=P_t'\bigl(h(\cdot,y)\bigr)\), and Theorem 1.1 gives
\[
\begin{aligned}
\int|P_tf(x,y)|^2&\,dx\\
&\le\Bigl(\int|h(x,y)|^p\,dx\Bigr)^{2/p} .
\end{aligned}
\]
Integrate over \(y\) and apply Lemma 2.1:
\[
\begin{aligned}
&\|P_tf\|_2^2\\
&\quad\le\Bigl(\int\Bigl(\int|h(x,y)|^2\,dy\Bigr)^{p/2}dx\Bigr)^{2/p} .
\end{aligned}
\]
For every fixed \(x\), \(h(x,\cdot)=P_t''\bigl(f(x,\cdot)\bigr)\) with the heat operator on \(\mathbb T^{N-1}\), and the induction hypothesis gives
\[
\Bigl(\int|h(x,y)|^2\,dy\Bigr)^{p/2}\le\int|f(x,y)|^p\,dy .
\]
So \(\|P_tf\|_2^2\le\bigl(\int\!\!\int|f|^p\,dy\,dx\bigr)^{2/p}=\|f\|_p^2\). \(\blacksquare\)

The induction works because the constant in Theorem 1.1 is \(1\): a constant \(C>1\) on the circle would become \(C^N\) on \(\mathbb T^N\). The exponent \(p\) does not depend on \(N\).

## 3. The form used in the last lesson

**Corollary 3.1.** Let \(t>0\), and
\[
b=\tanh\frac{2t}{c_0},\qquad a=1-b .
\]
Then \(0<b<1\), and for every real continuous function \(f\) on \(\mathbb T^N\)
\[
\|P_tf\|_2\le\|f\|_1^{\,b}\,\|f\|_2^{\,a} .
\]

**Proof.** Let \(p=1+e^{-4t/c_0}\), so \(1<p<2\). Then
\[
\begin{gathered}
\frac{2-p}p=\frac{1-e^{-4t/c_0}}{1+e^{-4t/c_0}}=\tanh\frac{2t}{c_0}=b,\\
\frac{2(p-1)}p=1-b=a .
\end{gathered}
\]
Write \(|f|^p=|f|^{pb}\,|f|^{pa}\). Since \(pb+\tfrac{pa}2=(2-p)+(p-1)=1\), Hölder's inequality with the exponents \(\tfrac1{pb}\) and \(\tfrac2{pa}\) gives
\[
\int|f|^p\le\Bigl(\int|f|\Bigr)^{pb}\Bigl(\int|f|^2\Bigr)^{pa/2} ,
\]
that is, \(\|f\|_p\le\|f\|_1^b\|f\|_2^a\). Now apply Theorem 2.2. \(\blacksquare\)

For a function with a small norm \(\|f\|_1\) and a norm \(\|f\|_2\) of ordinary size, the corollary says that \(P_tf\) is small in the norm \(\|\cdot\|_2\). Without the heat operator there is no such statement: a function that is large on a small set has a small norm \(\|\cdot\|_1\) and a large norm \(\|\cdot\|_2\).

## 4. Exercises

**4.1.** For which \(t\) does Theorem 1.1 give \(\|P_tf\|_4\le\|f\|_2\)? For which \(t\) does it give \(\|P_tf\|_2\le\|f\|_{3/2}\)?

**4.2.** Let \(f=1+\epsilon\cos(2\pi x)\) on \(\mathbb T\). Show that \(\|f\|_p^2=1+\tfrac{p-1}2\epsilon^2+O(\epsilon^3)\) for every \(p>1\), and conclude that an inequality \(\|P_tf\|_q\le\|f\|_p\) for all continuous \(f\) implies \((q-1)e^{-8\pi^2t}\le p-1\).

**4.3.** Show that for no \(t>0\) the inequality \(\|P_tf\|_2\le\|f\|_1\) holds for all continuous \(f\ge0\) on \(\mathbb T\). So the exponent \(p\) in Theorem 1.1 cannot be \(1\).

**4.4.** Let \(f(x,y)=\phi(x)\chi(y)\) on \(\mathbb T^2\) with continuous \(\phi,\chi\). Show directly that Theorem 2.2 for \(f\) follows from Theorem 1.1.

**4.5.** In the proof of Lemma 2.1, check that \(\int\psi^{r'}=1\) and \(\int G\psi=\|G\|_r\).

## 5. Solutions

**4.1.** With \(p=2\), \(q=4\): \(3\le e^{4t/c_0}\), that is \(t\ge\tfrac{c_0}4\log3=\tfrac7{16}\log3\approx0.48\). With \(p=\tfrac32\), \(q=2\): \(2\le e^{4t/c_0}\), that is \(t\ge\tfrac7{16}\log2\approx0.30\).

**4.2.** For small \(\epsilon\),
\[
\begin{aligned}
(1+\epsilon c)^p={}&1+p\epsilon c+\tfrac{p(p-1)}2\epsilon^2c^2\\
&+O(\epsilon^3)
\end{aligned}
\]
uniformly for \(|c|\le1\). With \(c=\cos(2\pi x)\), \(\int c=0\) and \(\int c^2=\tfrac12\): \(\int f^p=1+\tfrac{p(p-1)}4\epsilon^2+O(\epsilon^3)\), and the power \(\tfrac2p\) of this is \(1+\tfrac{p-1}2\epsilon^2+O(\epsilon^3)\). By Corollary 3.3 of the first lesson, \(P_tf=1+\epsilon e^{-4\pi^2t}\cos(2\pi x)\), so \(\|P_tf\|_q^2=1+\tfrac{q-1}2\epsilon^2e^{-8\pi^2t}+O(\epsilon^3)\). The inequality for all small \(\epsilon\) gives \((q-1)e^{-8\pi^2t}\le p-1\).

**4.3.** Let \(f=1+\cos(2\pi x)\ge0\). Then \(\|f\|_1=\int f=1\). By Corollary 3.3 of the first lesson, \(P_tf=1+e^{-4\pi^2t}\cos(2\pi x)\), and \(\|P_tf\|_2^2=1+\tfrac12e^{-8\pi^2t}>1\).

**4.4.** \(P_tf(x,y)=(P_t'\phi)(x)\,(P_t''\chi)(y)\), so \(\|P_tf\|_2=\|P_t\phi\|_2\|P_t\chi\|_2\) with the heat operators on the circle, and this is at most \(\|\phi\|_p\|\chi\|_p=\|f\|_p\).

**4.5.** \(\psi^{r'}=G^{(r-1)r'}/\|G\|_r^{(r-1)r'}=G^r/\|G\|_r^r\), whose integral is \(1\). And \(G\psi=G^r/\|G\|_r^{r-1}\), whose integral is \(\|G\|_r^r/\|G\|_r^{r-1}\).

## References

- [Austin] T. Austin, *On the failure of concentration for the \(\ell_\infty\)-ball*, arXiv:1309.3315, version 4, Section 2. https://arxiv.org/abs/1309.3315
