# A logarithmic Sobolev inequality on the circle

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The entropy of a function \(h\ge0\) measures how far \(h\) is from a constant, with a logarithmic weight on its large values. A logarithmic Sobolev inequality bounds the entropy of \(f^2\) by the mean square of the derivative of \(f\). This lesson proves such an inequality on the circle with the constant \(\tfrac74\). The constant is not the best one; what matters for the course is that there is no additional term on the right side. The inequality is the input for the next lesson, [Hypercontractivity of the heat operators](hypercontractivity-of-the-heat-operators.md).

- Entropy and Gibbs' inequality (Lemma 1.1).
- The largest value of a function on the circle (Lemma 2.1).
- An inequality with a defect (Lemma 3.1).
- Rothaus's lemma, which removes the defect (Lemma 4.1).
- The logarithmic Sobolev inequality (Theorem 5.1).

The lesson needs calculus and the Lebesgue integral ([core course *Measure and Integration*](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10)). Lemma 4.1 is due to O. S. Rothaus. The inequality with the best constant, which this course does not need, is a theorem of F. Weissler; see [Austin, Section 2] for references.

## 1. Entropy

Let \(\mu\) be a probability measure, and write \(\int h\) for \(\int h\,d\mu\). In this lesson \(\mu\) is the Lebesgue measure on the circle \(\mathbb T=\mathbb R/\mathbb Z\), except in Lemmas 1.1 and 4.1, which hold for every probability measure.

**Definition.** For a bounded Borel function \(h\ge0\), the *entropy* of \(h\) is
\[
\operatorname{Ent}(h)=\int h\log h-\Bigl(\int h\Bigr)\log\Bigl(\int h\Bigr),
\]
with \(0\log0=0\).

**Lemma 1.1.** Let \(h\ge0\) be a bounded Borel function.

1. (Gibbs' inequality.) If \(p\ge0\) is a bounded Borel function with \(\int p=1\), then
\[
\int h\log p\le\operatorname{Ent}(h),
\]
where \(h\log p\) is read as \(0\) at the points with \(h=0\), and the left side may be \(-\infty\).
2. \(\operatorname{Ent}(h)\ge0\), and \(\operatorname{Ent}(c\,h)=c\operatorname{Ent}(h)\) for every number \(c\ge0\).

**Proof.** (1) Let \(m=\int h\). If \(m=0\), both sides are \(0\). Let \(m>0\). At a point with \(h>0\), the inequality \(\log v\le v-1\), for \(v=pm/h\ge0\) (with \(\log0=-\infty\)), gives
\[
h\log p+h\log m-h\log h\le pm-h .
\]
Integrate over the set where \(h>0\): the right side gives at most \(m\int p-m=0\). (2) The first statement is (1) with \(p=1\). The second follows from \(\log(ch)=\log c+\log h\). \(\blacksquare\)

**Example 1.2.** Let \(h\) be \(1\) on a set of measure \(\alpha\in(0,1]\) and \(0\) elsewhere. Then \(\operatorname{Ent}(h)=\alpha\log\tfrac1\alpha\). A constant function has the entropy \(0\).

## 2. The largest value of a function on the circle

A function on \(\mathbb T\) is *continuously differentiable* if it is so as a function on \(\mathbb R\) with the period \(1\).

**Lemma 2.1.** Let \(f\) be a real continuously differentiable function on \(\mathbb T\).

1. \(\sup f^2\le\|f\|_2^2+2\,\|f\|_2\,\|f'\|_2\).
2. If \(\int f=0\), then \(\sup|f|\le\tfrac12\|f'\|_1\le\tfrac12\|f'\|_2\). In particular \(\|f\|_2\le\tfrac12\|f'\|_2\).

**Proof.** (1) The continuous function \(f^2\) takes its mean value: there is \(y\) with \(f(y)^2=\|f\|_2^2\). For every \(x\in[y,y+1]\),
\[
\begin{aligned}
f(x)^2-f(y)^2&=\int_y^x2ff'\le2\int_0^1|ff'|\\
&\le2\,\|f\|_2\|f'\|_2 ,
\end{aligned}
\]
by the Cauchy–Schwarz inequality. (2) Since \(\int f=0\), there is \(y\) with \(f(y)=0\). Let \(x\in[y,y+1]\). Then \(|f(x)|=|f(x)-f(y)|\le\int_y^x|f'|\), and also \(|f(x)|=|f(y+1)-f(x)|\le\int_x^{y+1}|f'|\). The two integrals add up to \(\|f'\|_1\), so one of them is at most \(\tfrac12\|f'\|_1\). \(\blacksquare\)

## 3. An inequality with a defect

**Lemma 3.1.** For every real continuously differentiable function \(f\) on \(\mathbb T\),
\[
\operatorname{Ent}(f^2)\le\|f'\|_2^2+\|f\|_2^2 .
\]

**Proof.** If \(f=0\) there is nothing to prove. Both sides are multiplied by \(c^2\) if \(f\) is multiplied by \(c\) (Lemma 1.1(2)), so we may assume \(\|f\|_2=1\). Then \(\int f^2=1\) and
\[
\begin{aligned}
\operatorname{Ent}(f^2)&=\int f^2\log f^2\\
&\le\log\bigl(\sup f^2\bigr)\int f^2\\
&=\log\sup f^2 .
\end{aligned}
\]
By Lemma 2.1(1), \(\sup f^2\le1+2\|f'\|_2\). With \(\log(1+v)\le v\) and \(2v\le v^2+1\),
\[
\operatorname{Ent}(f^2)\le2\|f'\|_2\le\|f'\|_2^2+1 .
\]
\(\blacksquare\)

The term \(\|f\|_2^2\) on the right is the *defect*. With it, the inequality says nothing for a constant function, whose entropy is \(0\) and whose derivative is \(0\). The next section shows how to pass from \(f\) to \(f\) minus its mean, for which the defect can be bounded by the derivative.

## 4. Rothaus's lemma

**Lemma 4.1** (Rothaus). Let \(\mu\) be a probability measure, \(g\) a bounded real Borel function and \(a\) a real number. Then
\[
\operatorname{Ent}\bigl((a+g)^2\bigr)\le\operatorname{Ent}(g^2)+2\int g^2 .
\]

**Proof.** *Reduction.* For \(a=0\) the statement is clear. For \(a\ne0\), \((a+g)^2=a^2(1+g/a)^2\), and both sides are multiplied by \(a^2\) when \(g/a\) is put in place of \(g\) and \(1\) in place of \(a\). So it is enough to prove \(F(t)\le0\) for every bounded \(g\) and every real \(t\), where
\[
\begin{aligned}
F(t)={}&\operatorname{Ent}\bigl((1+tg)^2\bigr)\\
&-t^2\Bigl(\operatorname{Ent}(g^2)+2\int g^2\Bigr).
\end{aligned}
\]
If \(\int g^2=0\), then \(g=0\) almost everywhere and \(F=0\). If \(1+t_0g=0\) almost everywhere for some \(t_0\), then \(g\) is almost everywhere a constant, the first term of \(F\) is \(0\) for all \(t\), and \(F\le0\). Exclude these cases. Then, for all \(t\),
\[
\begin{aligned}
m(t)&=\int(1+tg)^2\\
&=1+2t\int g+t^2\int g^2>0 .
\end{aligned}
\]

*The function \(\phi\).* Let \(\phi(u)=u^2\log(u^2)\) for \(u\ne0\) and \(\phi(0)=0\). It is continuously differentiable on \(\mathbb R\), with \(\phi'(u)=2u\log(u^2)+2u\) for \(u\ne0\) and \(\phi'(0)=0\). For \(u\ne0\), \(\phi''(u)=2\log(u^2)+6\). This function is integrable over every bounded interval, and \(\phi'(v)-\phi'(u)=\int_u^v\phi''\) for all \(u<v\).

*First derivative.* Let \(A(t)=\int\phi(1+tg)\), so that \(\operatorname{Ent}((1+tg)^2)=A(t)-m(t)\log m(t)\). Since \(g\) is bounded and \(\phi'\) is continuous, \(A\) is differentiable with \(A'(t)=\int g\,\phi'(1+tg)\). Hence \(F\) is differentiable, with
\[
\begin{aligned}
F(0)&=\phi(1)-1\cdot\log1=0,\\
F'(0)&=\int g\,\phi'(1)\\
&\quad-m'(0)\bigl(\log m(0)+1\bigr)\\
&=2\int g-2\int g=0 .
\end{aligned}
\]

*\(F'\) does not increase.* Let \(t_1<t_2\). At a point with \(g\ne0\),
\[
\begin{aligned}
g\,\phi'(1+t_2g)&-g\,\phi'(1+t_1g)\\
&=\int_{t_1}^{t_2}g^2\,\phi''(1+sg)\,ds ,
\end{aligned}
\]
and \(\int_{t_1}^{t_2}|g|\,|\phi''(1+sg)|\,ds\) is the integral of \(|\phi''|\) over the interval between \(1+t_1g\) and \(1+t_2g\), which is bounded by a constant \(C\) that depends only on \(t_1,t_2\) and \(\sup|g|\). So \(g^2|\phi''(1+sg)|\) is integrable in both variables, and Fubini's theorem gives
\[
\begin{aligned}
A'(t_2)&-A'(t_1)\\
&=\int_{t_1}^{t_2}\Bigl(\int g^2\,\phi''(1+sg)\Bigr)ds .
\end{aligned}
\]
The function \(m\log m\) has the second derivative \(m''(\log m+1)+m'^2/m\), with \(m''=2\int g^2\). Together,
\[
F'(t_2)-F'(t_1)=\int_{t_1}^{t_2}G(s)\,ds ,
\]
where, after collecting the terms with \(\int g^2\), and with \(p_s=(1+sg)^2/m(s)\),
\[
\begin{aligned}
G(s)={}&2\Bigl(\int g^2\log p_s-\operatorname{Ent}(g^2)\Bigr)\\
&-\frac{m'(s)^2}{m(s)} .
\end{aligned}
\]
The function \(p_s\) is bounded, \(p_s\ge0\) and \(\int p_s=1\). By Gibbs' inequality (Lemma 1.1) with \(h=g^2\) and \(p=p_s\), the bracket is \(\le0\). So \(G\le0\), and \(F'(t_2)\le F'(t_1)\).

*Conclusion.* \(F'\) does not increase and \(F'(0)=0\). So \(F'\ge0\) on \((-\infty,0]\) and \(F'\le0\) on \([0,\infty)\), and \(F(t)\le F(0)=0\) for all \(t\). \(\blacksquare\)

Here is the computation of \(G\) in detail. The second derivative of \(A\) contributes \(\int g^2(2\log(1+sg)^2+6)\), the second derivative of \(m\log m\) contributes \(-2\int g^2(\log m+1)-m'^2/m\), and the last term of \(F\) contributes \(-2\operatorname{Ent}(g^2)-4\int g^2\). The terms \(6\int g^2\), \(-2\int g^2\) and \(-4\int g^2\) cancel.

## 5. The inequality

**Theorem 5.1** (a logarithmic Sobolev inequality on the circle). For every real continuously differentiable function \(f\) on \(\mathbb T\),
\[
\operatorname{Ent}(f^2)\le\frac74\,\|f'\|_2^2 .
\]

**Proof.** Let \(a=\int f\) and \(g=f-a\). Then \(g\) is continuously differentiable, \(\int g=0\) and \(g'=f'\). By Lemma 4.1, Lemma 3.1 for \(g\), and Lemma 2.1(2) for \(g\),
\[
\begin{aligned}
\operatorname{Ent}(f^2)&\le\operatorname{Ent}(g^2)+2\|g\|_2^2\\
&\le\|g'\|_2^2+3\|g\|_2^2\\
&\le\|f'\|_2^2+\tfrac34\|f'\|_2^2 .
\end{aligned}
\]
\(\blacksquare\)

Throughout the course we write
\[
c_0=\tfrac74
\]
for the constant of this theorem. The following lessons use only the statement of the theorem, so a better constant would improve all later bounds.

## 6. Exercises

**6.1.** Compute \(\operatorname{Ent}(h)\) for \(h(u)=1+\cos(2\pi u)\) on \(\mathbb T\). (Use \(\int_0^1\log(1+\cos2\pi u)\,du=-\log2\) and \(\int_0^1\cos(2\pi u)\log(1+\cos2\pi u)\,du=1\).)

**6.2.** Show that an inequality \(\operatorname{Ent}(f^2)\le c\,\|f'\|_2^2\) for all continuously differentiable \(f\) on \(\mathbb T\) implies \(\|g\|_2^2\le\tfrac c2\|g'\|_2^2\) for all continuously differentiable \(g\) with \(\int g=0\). Conclude that \(c\ge\tfrac1{2\pi^2}\).

**6.3.** Check Rothaus's lemma directly for \(g\) with the two values \(1\) and \(-1\), each on a set of measure \(\tfrac12\), and \(a=1\).

**6.4.** Let \(f\) be continuously differentiable on \(\mathbb T\) with \(f>0\), and \(q>1\). Show that \(v=f^{q/2}\) is continuously differentiable and
\[
\operatorname{Ent}(f^q)\le\frac{c_0\,q^2}{4}\int f^{q-2}f'^2 .
\]

**6.5.** Let \(f\) be a bounded Borel function on a probability space with \(\int f^2=1\) and \(\sup f^2=M\). Show that \(\operatorname{Ent}(f^2)\le\log M\), and that equality holds if \(f^2\) has only the values \(M\) and \(0\). (This is the first step of the proof of Lemma 3.1.)

## 7. Solutions

**6.1.** \(\int h=1\), so \(\operatorname{Ent}(h)=\int h\log h\). With \(c=\cos(2\pi u)\) this is \(\int\log(1+c)+\int c\log(1+c)\), which is \(-\log2+1\approx0.307\).

**6.2.** Apply the inequality to \(f=1+\epsilon g\) with a small \(\epsilon\). Since \(g\) is bounded, for small \(\epsilon\)
\[
\begin{aligned}
(1+\epsilon g)^2&\log(1+\epsilon g)^2\\
&=2\epsilon g+3\epsilon^2g^2+O(\epsilon^3)
\end{aligned}
\]
uniformly, so \(\int f^2\log f^2=3\epsilon^2\int g^2+O(\epsilon^3)\). Also \(\int f^2=1+\epsilon^2\int g^2\), whose product with its logarithm is \(\epsilon^2\int g^2+O(\epsilon^4)\). So \(\operatorname{Ent}(f^2)=2\epsilon^2\int g^2+O(\epsilon^3)\), while the right side is \(c\,\epsilon^2\|g'\|_2^2\). Divide by \(\epsilon^2\) and let \(\epsilon\to0\). For \(g(u)=\cos(2\pi u)\): \(\|g\|_2^2=\tfrac12\) and \(\|g'\|_2^2=2\pi^2\), so \(\tfrac12\le\tfrac c2\cdot2\pi^2\).

**6.3.** \((1+g)^2\) is \(4\) or \(0\), each with measure \(\tfrac12\). Its integral is \(2\), and \(\int(1+g)^2\log(1+g)^2\) is \(\tfrac12\cdot4\log4=4\log2\). So the entropy is \(4\log2-2\log2=2\log2\approx1.39\). On the right, \(g^2=1\), so \(\operatorname{Ent}(g^2)=0\) and \(2\int g^2=2\). Indeed \(2\log2\le2\).

**6.4.** \(v=f^{q/2}\) is a composition of continuously differentiable functions because \(f>0\), with \(v'=\tfrac q2f^{q/2-1}f'\). So \(v^2=f^q\) and \(v'^2=\tfrac{q^2}4f^{q-2}f'^2\). Apply Theorem 5.1 to \(v\).

**6.5.** Since \(\int f^2=1\), \(\operatorname{Ent}(f^2)=\int f^2\log f^2\), and \(\log f^2\le\log M\) wherever \(f\ne0\). So \(\operatorname{Ent}(f^2)\le\log M\int f^2=\log M\). If \(f^2\) has only the values \(M\) and \(0\), it is \(M\) on a set of measure \(\tfrac1M\), and \(\int f^2\log f^2=\tfrac1M\cdot M\log M\).

## References

- [Austin] T. Austin, *On the failure of concentration for the \(\ell_\infty\)-ball*, arXiv:1309.3315, version 4, Section 2. https://arxiv.org/abs/1309.3315
