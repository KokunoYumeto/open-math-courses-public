# The rank of a depth-five circuit

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A syntactically homogeneous circuit with five layers computes a sum of products \(Q_1\cdots Q_r\) of homogeneous polynomials. The measure \(R\) of such a product is at most \(2D\prod_jH_{e_j}\), where \(e_j\) is the degree of \(Q_j\) and \(H_e=\sum_{i=0}^eq^{|i-\lambda e|}\). This lesson estimates the numbers \(H_e\) and proves that \(R(g)\) is much smaller than \(D\) for every polynomial \(g\) that a small circuit computes.

- \(H_e\) is governed by the distance from \(\lambda e\) to the integers (Lemma 1.1).
- Degrees below \(n/(4s)\): the distance is known exactly (Lemmas 2.1 and 2.2).
- The bound \(R(g)\le2S^2D\,\exp(11\sqrt n)\,n^{-\sqrt n/100}\) for a circuit of size \(S\) (Proposition 3.1).

The lesson follows [OpenAI-D, Sections 3.2 and 3.3]. It uses the measure \(R\), the numbers \(s,k,m,\lambda,q,D\) and the product bound (Proposition 5.1) from [A rank measure from differentiation and multiplication](a-rank-measure-from-differentiation-and-multiplication.md), and the description of a circuit from [Iterated matrix multiplication and depth-five circuits](iterated-matrix-multiplication-and-depth-five-circuits.md). Of the estimates of the numbers (Lemma 4.1 of the lesson on the rank measure) the following are used, for large \(n\):
\[
\begin{gathered}
\tfrac12\sqrt n\le s\le\sqrt n,\\
\lambda=\tfrac12-\tfrac s{2n}\ge\tfrac38,\\
n^{-1/2}\le q\le n^{-2/5},\\
q\le\tfrac2{\sqrt n},\qquad q\le\tfrac12,\\
q\le n^{-1/2}\exp\Bigl(\frac{\log n}{\sqrt n}+\frac4{n^{5/2}}\Bigr).
\end{gathered}
\]

Throughout, \(n\ge n_0\), and \(n_0\) is enlarged finitely many times. The division of the \(n\) layers into \(k\) layers for \(V\) and \(m\) layers for \(U\) is arbitrary in this lesson.

## 1. The sums \(H_e\)

For an integer \(e\ge1\) let
\[
d_e=\operatorname{dist}(\lambda e,\mathbb Z)
\]
be the distance from \(\lambda e\) to the nearest integer. So \(0\le d_e\le\tfrac12\).

**Lemma 1.1.** For every integer \(e\ge1\),
\[
H_e\le q^{d_e}\bigl(1+4q^{1-2d_e}\bigr)\le5 .
\]

**Proof.** Let \(i_0\) be an integer with \(|i_0-\lambda e|=d_e\). Every other integer is \(i_0+j\) with \(j\ne0\), and \(|i_0+j-\lambda e|\ge|j|-d_e\). The sum that defines \(H_e\) runs over some of the integers, so
\[
\begin{aligned}
H_e&\le q^{d_e}+2\sum_{j\ge1}q^{j-d_e}\\
&=q^{d_e}+\frac{2q^{1-d_e}}{1-q}\\
&\le q^{d_e}+4q^{1-d_e},
\end{aligned}
\]
because \(q\le\tfrac12\). This is the first inequality. The second holds because \(0<q<1\) and \(0\le d_e\le\tfrac12\). \(\blacksquare\)

So \(H_e\) is about \(q^{d_e}\), and \(q\) is about \(n^{-1/2}\). A factor \(Q_j\) of the degree \(e\) lowers the bound for the rank by about \(n^{-d_e/2}\). If \(\lambda e\) is an integer, it lowers nothing.

## 2. Small degrees

Put
\[
t_0=\frac n{4s}.
\]
By \(\tfrac12\sqrt n\le s\le\sqrt n\) we have \(\tfrac14\sqrt n\le t_0\le\tfrac12\sqrt n\), and \(t_0>2\) for large \(n\).

**Lemma 2.1.** Let \(1\le e<t_0\). Then
\[
\begin{gathered}
d_e=\frac{se}{2n}\ \text{ if }e\text{ is even},\\
d_e=\frac12-\frac{se}{2n}\ \text{ if }e\text{ is odd},
\end{gathered}
\]
and \(d_e\ge\tfrac{se}{2n}\) in both cases. Moreover:

- if \(e\) is odd, then \(d_e\ge\tfrac38\) and \(H_e\le q^{d_e/2}\);
- if \(e\) is even, then \(H_e\le q^{d_e}\exp\bigl(4q^{1-se/n}\bigr)\).

**Proof.** From \(\lambda=\tfrac12-\tfrac s{2n}\),
\[
\begin{gathered}
\lambda e=\frac e2-\frac{se}{2n},\\
0<\frac{se}{2n}<\frac{st_0}{2n}=\frac18 .
\end{gathered}
\]
For even \(e\) the nearest integer is \(\tfrac e2\). For odd \(e\) it is \(\tfrac{e-1}2\), at the distance \(\tfrac12-\tfrac{se}{2n}>\tfrac38\). This gives the formula, and \(d_e\ge\tfrac{se}{2n}\) in both cases because \(\tfrac38>\tfrac18\).

Let \(e\) be odd. By \(q\le n^{-2/5}\),
\[
q^{-d_e/2}\ge n^{d_e/5}\ge n^{3/40}\ge5
\]
for large \(n\). With Lemma 1.1, \(H_e\le5q^{d_e}\le q^{d_e/2}\).

Let \(e\) be even. Then \(1-2d_e=1-\tfrac{se}n\), and Lemma 1.1 with \(1+x\le\exp(x)\) gives the bound. \(\blacksquare\)

For an odd degree the share \(\lambda e\) is close to a half-integer, and the factor gains a fixed power of \(q\). For an even degree \(\lambda e\) is close to the integer \(\tfrac e2\); the gain \(q^{se/(2n)}\) is small, and it exists only because \(\lambda\) is not exactly \(\tfrac12\). The difference \(m-k=s\) was introduced for this. For these factors the correction \(\exp(4q^{1-se/n})\) cannot be estimated by a constant for each factor, since there may be \(\tfrac n2\) factors. The corrections are estimated together.

**Lemma 2.2.** For large \(n\) and every finite list of integers \(e_1,\dots,e_r\ge1\) with \(e_1+\dots+e_r\le n\),
\[
\sum_{\substack{j:\ e_j<t_0\\ e_j\ \mathrm{even}}}q^{1-se_j/n}\le\sqrt n .
\]

**Proof.** We show \(q^{1-se/n}\le\tfrac e{\sqrt n}\) for every even \(e\) with \(2\le e<t_0\); the sum of the \(e_j\) is at most \(n\). For real \(z\) with \(2\le z\le t_0\) put
\[
\begin{gathered}
f(z)=\frac{q^{1-sz/n}}z,\\
\log f(z)=\Bigl(1-\frac{sz}n\Bigr)\log q-\log z .
\end{gathered}
\]
The second derivative of \(\log f\) is \(z^{-2}>0\). So \(\log f\) is convex, and \(f(z)\le\max\{f(2),f(t_0)\}\).

*At \(z=2\).* By \(q^{-1}\le\sqrt n\) and \(s\le\sqrt n\) we have \(q^{-2s/n}\le n^{s/n}\le \exp(\log n/\sqrt n)\). With the upper bound for \(q\),
\[
\begin{aligned}
f(2)&\le\frac1{2\sqrt n}\exp\Bigl(\frac{2\log n}{\sqrt n}+\frac4{n^{5/2}}\Bigr)\\
&\le\frac1{\sqrt n}
\end{aligned}
\]
for large \(n\).

*At \(z=t_0\).* Here \(1-\tfrac{st_0}n=\tfrac34\), and \(q\le\tfrac2{\sqrt n}\):
\[
f(t_0)=\frac{4s}n\,q^{3/4}\le\frac4{\sqrt n}\cdot\frac2{n^{3/8}}\le\frac1{\sqrt n}
\]
for \(n\ge8^{8/3}=256\). \(\blacksquare\)

## 3. The bound for a circuit

**Proposition 3.1** ([OpenAI-D]). There is a number \(n_0\) with the following property. Let \(n\ge n_0\), with the numbers of the lesson on the rank measure and any division of the layers into \(k\) layers for \(V\) and \(m\) layers for \(U\). Let \(K\) be a field, and let \(g\in K[V,U]\) be \(0\) or homogeneous of degree \(n\). If \(g\) is computed by a syntactically homogeneous \(\Sigma\Pi\Sigma\Pi\Sigma\) circuit of size \(S\), then
\[
R(g)\le2S^2D\,\exp(11\sqrt n)\,n^{-\sqrt n/100}.
\]

**Proof.** If \(g=0\), then \(R(g)=0\). Let \(g\ne0\). The polynomial of the output is \(0\) or homogeneous of the formal degree of the output, so this formal degree is \(n\). By Lemma 4.1 of the first lesson, \(g\) is a sum of at most \(S\) polynomials \(c\,G\) with \(c\in K\) and
\[
\begin{gathered}
G=Q_1\cdots Q_r,\\
\deg Q_j=e_j\ge1,\qquad e_1+\dots+e_r=n,
\end{gathered}
\]
where every \(Q_j\) is a sum of at most \(S\) polynomials, each an element of \(K\) times a product of \(e_j\) linear forms. Since \(R(cG)\le R(G)\) and \(R\) of a sum is at most the sum, it is enough to show
\[
R(G)\le2SD\exp(11\sqrt n)\,n^{-\sqrt n/100}
\]
for every such \(G\). We refer to this inequality as (3.1). There are two cases.

*Case 1: every \(e_j\) is smaller than \(t_0\).* Put \(\Delta=\sum_jd_{e_j}\), and let \(\Sigma\) be the sum of the numbers \(q^{1-se_j/n}\) over the \(j\) with even \(e_j\). By the product bound and Lemma 2.1, where for even degrees \(q^{d_e}\le q^{d_e/2}\) is used,
\[
\begin{aligned}
R(G)&\le2D\prod_jH_{e_j}\\
&\le2D\,q^{\Delta/2}\exp(4\Sigma).
\end{aligned}
\]
By Lemma 2.1, \(\Delta\ge\tfrac s{2n}\sum_je_j=\tfrac s2\). By Lemma 2.2, \(\Sigma\le\sqrt n\). With \(q\le n^{-2/5}\) and \(s\ge\tfrac12\sqrt n\),
\[
\begin{aligned}
R(G)&\le2D\exp(4\sqrt n)\,q^{s/4}\\
&\le2D\exp(4\sqrt n)\,n^{-\sqrt n/20}.
\end{aligned}
\]

*Case 2: one factor, say \(Q_{j_0}\), has a degree \(e=e_{j_0}\ge t_0\).* By Lemma 4.2 of the first lesson, \(G\) is a sum of at most \(S\) polynomials
\[
c'\,\ell_1\ell_2\cdots\ell_e\prod_{j\ne j_0}Q_j
\]
with \(c'\in K\) and linear forms \(\ell_1,\dots,\ell_e\). If one of the \(\ell_i\) is \(0\), the term is \(0\). Otherwise it is \(c'\) times a product of \(e\) polynomials of degree \(1\) and of the \(Q_j\) with \(j\ne j_0\), and the degrees add up to \(n\). The product bound gives for its measure at most
\[
2D\,H_1^{\,e}\prod_{j\ne j_0}H_{e_j}.
\]
We estimate the factors.

- *The linear forms.* Since \(1<t_0\) and \(1\) is odd, Lemma 2.1 gives \(d_1=\tfrac12-\tfrac s{2n}=\lambda\) and \(H_1\le q^{\lambda/2}\). So \(H_1^{\,e}\le q^{\lambda e/2}\le q^{\lambda t_0/2}\).
- *Other factors of a degree \(\ge t_0\).* The degrees add up to \(n\), so there are at most \(n/t_0=4s\) of them. Each has \(H_{e_j}\le5\) by Lemma 1.1.
- *Factors of an odd degree \(<t_0\).* \(H_{e_j}\le q^{d_{e_j}/2}\le1\).
- *Factors of an even degree \(<t_0\).* \(H_{e_j}\le\exp(4q^{1-se_j/n})\), and by Lemma 2.2 the product of these numbers is at most \(\exp(4\sqrt n)\).

With \(q\le n^{-2/5}\), \(\lambda\ge\tfrac38\) and \(t_0\ge\tfrac14\sqrt n\) we get \(q^{\lambda t_0/2}\le n^{-\lambda t_0/5}\le n^{-3\sqrt n/160}\). Adding over the at most \(S\) terms,
\[
R(G)\le2SD\cdot5^{4s}\exp(4\sqrt n)\,n^{-3\sqrt n/160},
\]
and \(5^{4s}\le\exp(4\log5\cdot\sqrt n)\).

In both cases (3.1) holds, because \(4+4\log5<11\), \(\tfrac1{20}>\tfrac1{100}\) and \(\tfrac3{160}>\tfrac1{100}\). \(\blacksquare\)

## 4. Remarks on the proof

**Which properties of the circuit are used.** Only the description of Lemma 4.1 of the first lesson: \(g\) is a sum of at most \(S\) products, and every factor is a sum of at most \(S\) products of linear forms. The linear forms may contain any number of variables, and the number of the edges plays no role. The number \(S\) enters twice: once for the terms of the output, once for the terms of the one factor that is expanded. This is the exponent \(2\) of \(S\).

**Why one factor is expanded.** A factor of a degree \(e\ge t_0\) may lie exactly on its share: \(\lambda e\) may be an integer, and then \(H_e\ge1\) (Exercise 5.2). Such a factor gives no gain in the product bound. But a factor of a large degree consists of many linear forms, and each linear form is as far from its share as possible, \(d_1=\lambda\). Its \(e\ge\tfrac14\sqrt n\) linear forms together gain \(q^{\lambda e/2}\). The other factors of large degree are not expanded; they are few, and each costs at most the factor \(5\).

**Why all factors may be small.** If no factor has a degree \(\ge t_0\), the gain comes from all factors together: the distances \(d_{e_j}\) add up to at least \(\tfrac s2\), whatever the degrees are, because \(d_e\ge\tfrac{se}{2n}\) and the degrees add up to \(n\).

**The fifth layer.** With more layers, a factor of large degree would be a sum of products of polynomials of unknown degrees, and the expansion would not lead to linear forms. The argument uses that below the middle sums there is only one layer of products.

## 5. Exercises

**5.1.** Let \(n=100\). Find \(s,k,m,\lambda\) and \(t_0\), and compute \(d_e\) for \(e=1,2,3,4,5,10,20\).

**5.2.** Show \(H_e\ge q^{d_e}\) for every \(e\ge1\). Conclude that \(H_e\ge1\) if \(\lambda e\) is an integer, and that this happens for \(e=n\).

**5.3.** Let \(G=\ell_1\cdots\ell_n\) be a product of \(n\) linear forms. Which bound for \(R(G)\) follows from the product bound and Lemma 2.1?

**5.4.** Let \(F\) be a positive function on an interval \([x_0,x_1]\) whose logarithm is convex. Show \(F(x)\le\max\{F(x_0),F(x_1)\}\) for all \(x\) in the interval.

**5.5.** In Case 2 of the proof the degree \(e\) of the expanded factor may be as large as \(n\). What are then the other factors, and which bound does the proof give?

## 6. Solutions

**5.1.** \(s\) is the largest integer \(\le10\) with \(100-s\) even: \(s=10\). So \(k=45\), \(m=55\), \(\lambda=0.45\), \(t_0=2.5\). The numbers \(\lambda e\) are \(0.45,\ 0.9,\ 1.35,\ 1.8,\ 2.25,\ 4.5,\ 9\). So \(d_1=0.45\), \(d_2=0.1\), \(d_3=0.35\), \(d_4=0.2\), \(d_5=0.25\), \(d_{10}=0.5\), \(d_{20}=0\). For \(e=1,2\) (the degrees below \(t_0\)) these are the values \(\tfrac12-\tfrac{se}{2n}\) and \(\tfrac{se}{2n}\) of Lemma 2.1.

**5.2.** \(0\le\lambda e\le e\), so an integer \(i_0\) nearest to \(\lambda e\) lies in \(\{0,\dots,e\}\), and its term \(q^{d_e}\) is one of the terms of \(H_e\). If \(\lambda e\) is an integer, \(d_e=0\) and \(H_e\ge1\). For \(e=n\): \(\lambda n=k\).

**5.3.** All degrees are \(1<t_0\), so \(R(G)\le2DH_1^{\,n}\le2D\,q^{\lambda n/2}=2D\,q^{k/2}\). With \(q\le n^{-2/5}\) and \(k\ge\tfrac n4\) this is at most \(2D\,n^{-n/20}\). A product of linear forms has a very small measure.

**5.4.** Every \(x\) in the interval is \((1-\theta)x_0+\theta x_1\) with \(0\le\theta\le1\). Put \(L=\log F\). By convexity,
\[
\begin{aligned}
L(x)&\le(1-\theta)L(x_0)+\theta L(x_1)\\
&\le\max\{L(x_0),L(x_1)\}.
\end{aligned}
\]

**5.5.** Then \(r=1\) and \(G=Q_1\) is one middle sum of the degree \(n\): there are no other factors. The proof expands it into at most \(S\) products of \(n\) linear forms, and by Exercise 5.3 gives \(R(G)\le2SD\,q^{k/2}\).

## References

- [OpenAI-D] OpenAI, *Homogeneous depth-five lower bounds for iterated matrix multiplication*, OpenAI Math Release preprint, 25 September 2026, Sections 3.2 and 3.3. https://github.com/openai/math/tree/main/preprints/Homogeneous-depth-five-lower-bounds-for-iterated-matrix-multiplication-September-25-2026
