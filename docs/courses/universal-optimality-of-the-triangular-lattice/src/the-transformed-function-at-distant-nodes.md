# The transformed function at distant nodes

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

[Gaussian damping and Fourier pairs](gaussian-damping-and-fourier-pairs.md) attaches to every cardinal function \(p\) a transformed function \(K_p\), shows that \(K_p\) decays like \(e^{-qs}\) with \(q\approx0.188\), and that the jet operator \(S\) has norm less than \(4000\). This lesson sharpens these bounds. The slow rate \(0.187\) comes only from the frequencies \(t\) near \(\pm1\); all other frequencies decay at the rate \(0.70\), and the part with the slow rate carries an additional factor \(1/s\), apart from the multiple of the sine product.

- The kernel \(\lambda(t)e^{i\pi z(t)s}\) is estimated separately for \(|t|\le5/6\) and for \(5/6\le|t|\le1\) (Lemma 1.1).
- The spectral density of a cardinal function is bounded on \(5/6<|t|<1\) by \(\pi\) times the sum of the absolute values of the pole coefficients (Lemma 2.1).
- This gives a bound for \(K_p\) and its derivatives with two terms (Theorem 3.1), and a bound \(U_r\) for the part of the list \(S\mathbf a\) at the nodes \(n\ge r\) (Theorem 3.2).

The bound \(U_r\) is what controls the infinitely many distant nodes when the interpolation system is solved. The lesson follows [OpenAI-T, Section 2, the lemma on kernel and tail bounds].

## 1. The kernel on two frequency ranges

Recall \(b=\sqrt3/2\), \(h=2/5\), \(B=4/3\), and for real \(t\)
\[
\begin{gathered}
\lambda(t)=\frac1{b(h-it)},\\
z(t)=\frac{iB}{h-it}-ih .
\end{gathered}
\]
By Lemma 2.1(4) of the lesson on Gaussian damping, with \(r=t^2+h^2\),
\[
\begin{gathered}
|\lambda(t)|=\frac1{b\sqrt r},\\
\operatorname{Im}z(t)=h\Bigl(\frac Br-1\Bigr),\\
|z(t)|^2=h^2+\frac{304}{225\,r}.
\end{gathered}
\]
All three are even functions of \(t\) and decrease when \(|t|\) increases. Let
\[
q(t)=\pi\operatorname{Im}z(t).
\]
Then \(|e^{i\pi z(t)s}|=e^{-q(t)s}\) for real \(s\).

**Lemma 1.1.**

1. For \(|t|\le5/6\): \(|\lambda(t)|<3\), \(|z(t)|<3\) and \(q(t)>0.70\).
2. For \(5/6\le|t|\le1\): \(|\lambda(t)|<1.25\), \(|z(t)|<1.32\) and
\[
q(t)>0.187+2.48\,(1-|t|).
\]

**Proof.** It is enough to consider \(t\ge0\).

(1) The largest values of \(|\lambda|\) and \(|z|\) are those at \(t=0\), which are \(5/\sqrt3<3\) and \(44/15<3\). The smallest value of \(q\) on \([0,5/6]\) is \(q(5/6)\). At \(t=5/6\) we have \(r=\tfrac{25}{36}+\tfrac4{25}=\tfrac{769}{900}\) and \(B/r=\tfrac{1200}{769}\), so
\[
q(5/6)=\pi\cdot\frac25\cdot\frac{431}{769}=\frac{862\pi}{3845},
\]
which is more than \(862\cdot3.14/3845>0.703\).

(2) On \([5/6,1]\) the largest values of \(|\lambda|\) and \(|z|\) are those at \(5/6\). There
\[
|\lambda|=\frac{30}{b\sqrt{769}}=\frac{60}{\sqrt{2307}}<\frac54,
\]
because \(3600\cdot16=57600<57675=25\cdot2307\). Further
\[
|z|^2=\frac4{25}+\frac{1216}{769}=\frac{33476}{19225},
\]
and this is less than \((33/25)^2=1.32^2\), because \(33476\cdot625=20922500\) is less than \(1089\cdot19225=20936025\).

For \(t>0\) the derivative of \(q\) is
\[
q'(t)=-\frac{2\pi hB\,t}{(t^2+h^2)^2}.
\]
The function \(t/(t^2+h^2)^2\) has the derivative \((h^2-3t^2)/(t^2+h^2)^3\), which is negative for \(t>h/\sqrt3\), in particular on \([5/6,1]\). So on this interval \(-q'(t)\) is at least its value at \(t=1\),
\[
\begin{aligned}
\frac{2\pi hB}{(1+h^2)^2}&=2\pi\cdot\frac8{15}\cdot\frac{625}{841}\\
&=\frac{2000\pi}{2523},
\end{aligned}
\]
which is more than \(2000\cdot3.14/2523>2.48\). Hence for \(5/6\le t\le1\)
\[
\begin{aligned}
q(t)&=q(1)+\int_t^1(-q'(\tau))\,d\tau\\
&\ge q(1)+2.48\,(1-t),
\end{aligned}
\]
and \(q(1)=26\pi/435>0.187\). \(\blacksquare\)

So the exponential \(e^{i\pi z(t)s}\) decays at the rate \(0.70\) or faster unless \(|t|\) is close to \(1\), and near \(|t|=1\) the rate improves linearly with the distance from \(1\).

## 2. The density near the highest frequencies

Let \(\mathbf a\) be a coefficient list with entries \(C,c_n,d_n\), let \(W=\sum_n(|c_n|+|d_n|)\), and let \(p\) be its cardinal function. The proof of Theorem 2.2 in [The sine product and cardinal functions](the-sine-product-and-cardinal-functions.md) gives the function \(m\) with \(p(s)=CP(s)+\int_{-1}^1m(t)e^{i\pi ts}\,dt\) explicitly. For a node \(n\) let \(\pi_l=P_le^{i\pi t_ln}\), where \(t_l=l/6\), and \(u=s-n\). The identities proved there are
\[
\begin{aligned}
&\frac{P(s)}{s-n}=i\pi\sum_l\pi_l\int_0^{t_l}e^{i\pi tu}\,dt,\\
&\frac{P(s)}{(s-n)^2}\\
&\quad=-\pi^2\sum_l\pi_l\int_0^{t_l}(t_l-t)\,e^{i\pi tu}\,dt ,
\end{aligned}
\]
and \(e^{i\pi tu}=e^{-i\pi tn}e^{i\pi ts}\).
A frequency \(t\) with \(0<t<1\) occurs in the integral with index \(l\) exactly when \(t_l>t\). So the right sides are \(\int_{-1}^1m_n'(t)e^{i\pi ts}\,dt\) and \(\int_{-1}^1m_n''(t)e^{i\pi ts}\,dt\) with, for \(0<t<1\),
\[
\begin{aligned}
m_n'(t)&=i\pi\,e^{-i\pi tn}\sum_{l:\,t_l>t}\pi_l,\\
m_n''(t)&=-\pi^2e^{-i\pi tn}\sum_{l:\,t_l>t}\pi_l\,(t_l-t),
\end{aligned}
\]
and for \(-1<t<0\) with the sums over the indices \(l\) with \(t_l<t\) and the opposite sign. The function \(m\) is the sum of the series \(\sum_n(c_nm_n''+d_nm_n')\), which converges in the space of integrable functions.

**Lemma 2.1.** For \(5/6<|t|<1\),
\[
|m(t)|\le\pi\,W .
\]

**Proof.** Let \(5/6<t<1\). The only index \(l\) with \(t_l>t\) is \(l=6\), and \(|\pi_6|=|P_6|=1\). So \(|m_n'(t)|=\pi\) and \(|m_n''(t)|=\pi^2(1-t)\le\pi^2/6<\pi\). For \(-1<t<-5/6\) the same holds with \(l=-6\). Hence, for every node \(n\),
\[
|c_nm_n''(t)+d_nm_n'(t)|\le\pi\,(|c_n|+|d_n|).
\]
So at these \(t\) the series converges absolutely, to a function bounded by \(\pi W\), and this function agrees almost everywhere with the limit in the space of integrable functions. \(\blacksquare\)

The point is that \(\pi W\) is much smaller than what the bound \(\int|m|\le36W\) would allow on a short interval, and that it holds at every frequency of the interval, not only on average.

## 3. Refined bounds

Let \(K=K_p\) be the transformed function of the lesson on Gaussian damping,
\[
\begin{aligned}
K(s)={}&C\sum_{l=-6}^6P_l\,\lambda(t_l)\,e^{i\pi z(t_l)s}\\
&+\int_{-1}^1m(t)\,\lambda(t)\,e^{i\pi z(t)s}\,dt .
\end{aligned}
\]

**Theorem 3.1.** Let \(w\ge W\) and \(c\ge|C|\). For every integer \(j\ge0\) and every real \(s>0\),
\[
\begin{aligned}
&|K^{(j)}(s)|\le3\,(3\pi)^j\,(36w+25c)\,e^{-0.70s}\\
&\quad+1.25\,(1.32\pi)^j\Bigl(\frac{2.54\,w}s+2c\Bigr)e^{-0.187s}.
\end{aligned}
\]

**Proof.** Write \(K=K_0+K_1\). The function \(K_0\) consists of the terms of the sum with \(|l|\le5\) and the integral over \(|t|\le5/6\); the function \(K_1\) consists of the two terms with \(l=\pm6\), that is \(t_l=\pm1\), and the integral over \(5/6<|t|<1\). By Lemma 3.1 of the lesson on Gaussian damping, the derivatives are obtained by inserting the factor \((i\pi z(t))^j\).

*The part \(K_0\).* By Lemma 1.1(1) every term has a kernel of absolute value at most \(3(3\pi)^je^{-0.70s}\). The total weight is at most
\[
|C|\sum_{|l|\le5}|P_l|+\int|m|\le23|C|+36W,
\]
which is at most \(36w+25c\).

*The part \(K_1\).* By Lemma 1.1(2), for \(5/6\le|t|\le1\) the kernel has absolute value at most
\[
1.25\,(1.32\pi)^j\,e^{-0.187s}\,e^{-2.48s(1-|t|)}.
\]
The two terms with \(t_l=\pm1\) have the total weight \(|C|(|P_6|+|P_{-6}|)=2|C|\), and for them the last factor is \(1\). For the integral, Lemma 2.1 gives
\[
\begin{aligned}
&\int_{5/6<|t|<1}|m(t)|\,e^{-2.48s(1-|t|)}\,dt\\
&\quad\le2\pi W\int_{5/6}^1e^{-2.48s(1-t)}\,dt\\
&\quad\le\frac{2\pi W}{2.48\,s},
\end{aligned}
\]
and \(2\pi/2.48<2.54\). \(\blacksquare\)

**Theorem 3.2.** Let \(w\ge W\) and \(c\ge|C|\). For every integer \(r\ge1\),
\[
\begin{gathered}
\sum_{n\in\mathcal N,\ n\ge r}\bigl(|(S\mathbf a)_{c,n}|+|(S\mathbf a)_{d,n}|\bigr)\\
\le U_r(w,c),
\end{gathered}
\]
where
\[
\begin{aligned}
&U_r(w,c)=800\,(w+c)\,\frac{e^{-0.70r}}{1-e^{-0.70}}\\
&\quad+5.3\Bigl(\frac{2.54\,w}r+2c\Bigr)\frac{e^{-0.187r}}{1-e^{-0.187}}.
\end{aligned}
\]

**Proof.** As in the proof of Proposition 4.1 of the lesson on Gaussian damping, with \(Q_n>7/4\) and \(|D_n|<2.12\),
\[
\begin{aligned}
&|(S\mathbf a)_{c,n}|+|(S\mathbf a)_{d,n}|\\
&\quad\le\frac{(1+|D_n|)\,|K(n)|+|K'(n)|}{Q_n}.
\end{aligned}
\]
Apply the bounds of the proof of Theorem 3.1 for \(j=0\) and \(j=1\) to \(K_0\) and \(K_1\) separately. The part \(K_0\) contributes at most
\[
\begin{aligned}
&\frac{3\,(1+2.12+3\pi)}{1.75}\\
&\quad\cdot(36w+25c)\,e^{-0.70n}.
\end{aligned}
\]
The first factor is less than \(3\cdot12.55/1.75<22\), and \(22(36w+25c)\le800(w+c)\). The part \(K_1\) contributes at most
\[
\begin{aligned}
&\frac{1.25\,(1+2.12+1.32\pi)}{1.75}\\
&\quad\cdot\Bigl(\frac{2.54\,w}n+2c\Bigr)e^{-0.187n},
\end{aligned}
\]
and the first factor is less than \(1.25\cdot7.27/1.75<5.3\). Now sum over all integers \(n\ge r\), using \(1/n\le1/r\) and \(\sum_{n\ge r}e^{-an}=e^{-ar}/(1-e^{-a})\). \(\blacksquare\)

The bound \(U_r(w,c)\) is a sum of a multiple of \(w\) and a multiple of \(c\). So for several lists the sum of their tails is bounded by \(U_r\) of the sums of their numbers \(w\) and \(c\). For large \(r\) the second term of \(U_r\) is the larger one: a list without the entry \(C\) has a tail of the order \(e^{-0.187r}/r\).

## 4. Exercises

**4.1.** Compute \(q(0)\) and compare it with \(\pi|z(0)|\). Which frequencies of \(p\) give the fastest decaying parts of \(K_p\)?

**4.2.** Show that \(U_{169}(w,c)<2\cdot10^{-12}\,(w+c)\). A calculator may be used for the exponentials.

**4.3.** Let \(\mathbf a\) be a list with \(C=0\). Show that \(|K_p(s)|\le81\,W\,e^{-0.187s}/s\) for all \(s>0\).

## 5. Solutions

**4.1.** At \(t=0\), \(r=h^2\) and \(q(0)=\pi h(B/h^2-1)\), which is \(\pi(B/h-h)=44\pi/15\), about \(9.2\). This equals \(\pi|z(0)|\), because \(z(0)=i(B/h-h)\) is purely imaginary. Since \(q\) decreases in \(|t|\), the low frequencies of \(p\) give the fastest decaying parts of \(K_p\), and the frequencies near \(\pm1\) the slowest.

**4.2.** For the first term, \(e^{-0.70\cdot169}<10^{-51}\) and \(1-e^{-0.70}>0.5\), so it is less than \(10^{-47}(w+c)\). For the second term, \(0.187\cdot169=31.603\), \(e^{-31.603}<1.9\cdot10^{-14}\) and \(1-e^{-0.187}>0.17\). Since \(2.54w/169+2c\le2(w+c)\), the second term is less than \(5.3\cdot2\cdot1.9\cdot10^{-14}/0.17\) times \(w+c\), and this factor is less than \(1.2\cdot10^{-12}\). Together, \(U_{169}(w,c)<2\cdot10^{-12}(w+c)\).

**4.3.** Theorem 3.1 with \(j=0\), \(w=W\) and \(c=0\) gives
\[
\begin{aligned}
|K_p(s)|\le{}&108\,W\,e^{-0.70s}\\
&+\frac{3.175\,W}s\,e^{-0.187s}.
\end{aligned}
\]
The first term is \(108\,W\,(s\,e^{-0.513s})\,e^{-0.187s}/s\). The function \(s\,e^{-0.513s}\) has its maximum at \(s=1/0.513\), where it is \(1/(0.513\,e)<0.718\). Since \(108\cdot0.718+3.175<81\), the bound follows.

## References

- [OpenAI-T] OpenAI, *Universal optimality of the triangular lattice*, OpenAI Math Release preprint, 23 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/Universal-optimality-of-the-triangular-lattice-September-23-2026
