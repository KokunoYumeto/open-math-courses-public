# Diagonal growth and the bound on characters

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The profile \(P(a,b)\) of a character, defined in [Two inequalities for polynomial multiplication](two-inequalities-for-polynomial-multiplication.md), is symmetric, equals \(b\) at \(a=1\), is discretely concave in each argument and satisfies shifted tripling. This lesson shows that these four properties alone force \(P(a,a)\ge a^{4/3}\) (Lemma 5.1). Since the rank of polynomial multiplication gives \(P(a,a)\le(2a-1)^{1/t}\), every character satisfies \(t\le\frac34\), that is, \(\lambda(T_d)\le d^{9/4}\) (Theorem 5.2). The argument is OpenAI's [OpenAI-MM, Section 5].

## 1. Diagonal growth

**Lemma 5.1.** Let \(P\) be a function from pairs of positive integers to positive reals such that, for all positive integers \(a,b,h\),

1. \(P(a,b)=P(b,a)\) and \(P(1,b)=b\);
2. if \(b\ge2\), then \(2P(a,b)\) is at least \(P(a,b+1)+P(a,b-1)\);
3. \(P(a,3h+a-1)\ge3P(a,h)\).

Then \(P(a,a)\ge a^{4/3}\) for every \(a\ge1\).

**Proof.** For fixed \(a\) put \(\Delta_{a,h}=P(a,h+1)-P(a,h)\) for \(h\ge1\). Condition 2 says that \(\Delta_{a,h}\) is nonincreasing in \(h\). Put \(D_a=P(a,a)\) and \(H_a=2D_a/(3a-1)\).

*Step 1.* Condition 3 with \(h=a\) gives \(P(a,4a-1)\ge3D_a\). Hence
\[
\begin{aligned}
2D_a&\le P(a,4a-1)-D_a\\
&=\sum_{h=a}^{4a-2}\Delta_{a,h}\le(3a-1)\Delta_{a,a},
\end{aligned}
\]
because the sum has \(3a-1\) terms, each at most \(\Delta_{a,a}\). So \(\Delta_{a,a}\ge H_a\).

*Step 2.* Let \(a\ge2\). By symmetry, \(P(a-1,a)=P(a,a-1)\), so
\[
D_a-D_{a-1}=\Delta_{a-1,a-1}+\Delta_{a,a-1}.
\]
Step 1 for \(a-1\) gives \(\Delta_{a-1,a-1}\ge H_{a-1}\), and monotonicity with Step 1 gives \(\Delta_{a,a-1}\ge\Delta_{a,a}\ge H_a\). Hence \(D_a-D_{a-1}\ge H_{a-1}+H_a\). Substituting \(D_a=\frac12(3a-1)H_a\) and \(D_{a-1}=\frac12(3a-4)H_{a-1}\) and rearranging,
\[
\tfrac12(3a-3)\,H_a\ge\tfrac12(3a-2)\,H_{a-1},
\]
that is,
\[
H_a\ge\Bigl(1+\frac1{3(a-1)}\Bigr)H_{a-1}.
\]

*Step 3.* Since \(H_1=D_1=P(1,1)=1\), induction gives
\[
H_a\ge\prod_{m=1}^{a-1}\Bigl(1+\frac1{3m}\Bigr)\qquad(a\ge1),
\]
the empty product being \(1\). For \(m\ge1\), \((1+\frac1{3m})^3\ge1+\frac1m\) (expand the cube). The product \(\prod_{m=1}^{a-1}(1+\frac1m)\) telescopes to \(a\), so \(H_a^3\ge a\). Finally \(\frac12(3a-1)\ge a\), so
\[
\begin{aligned}
D_a&=\tfrac12(3a-1)H_a\\
&\ge a\cdot a^{1/3}=a^{4/3}.
\end{aligned}
\]
\(\square\)

## 2. The bound on characters

**Theorem 5.2.** Every character \(\lambda\) satisfies \(t(\lambda)\le\frac34\). Equivalently, \(\lambda(T_d)\le d^{9/4}\) for every \(d\ge1\).

**Proof.** Let \(t=t(\lambda)\) and let \(P\) be the profile of \(\lambda\). By Lemmas 4.1, 4.3 and 4.4, \(P\) satisfies the conditions of Lemma 5.1, so for every \(a\ge2\)
\[
a^{4/3}\le P(a,a)\le(2a-1)^{1/t}<(2a)^{1/t},
\]
using Lemma 4.1 for the upper bound. Taking logarithms, \(\frac43\log a<\frac1t(\log2+\log a)\). Divide by \(\log a\) and let \(a\to\infty\): \(\frac43\le\frac1t\), so \(t\le\frac34\). By Lemma 2.5, \(\lambda(T_d)=d^{3t}\le d^{9/4}\). \(\square\)

## 3. What the bound says

The flattening ranks have \(t=\frac23\) and value \(d^2\) on \(T_d\) (Example 2.6). Theorem 7.3 and Exercise 7.1 show that the supremum of \(3t(\lambda)\) over all characters equals \(\nu\). So Theorem 5.2 is equivalent to \(\nu\le9/4\), and \(\nu=2\) would mean that no character has \(t>\frac23\). The hypotheses of Lemma 5.1 use only three properties of the profile: symmetry with its boundary values, discrete concavity, and shifted tripling.

From these hypotheses alone, the bound of Step 3 is the best possible, at least numerically. For every \(a\le16\), linear programming over all functions that satisfy the hypotheses of Lemma 5.1 on the pairs with \(a,b\le64\) gives
\[
\begin{aligned}
\min P(a,a)&=\tfrac12(3a-1)\\
&\quad\times\prod_{m=1}^{a-1}\Bigl(1+\frac1{3m}\Bigr),
\end{aligned}
\]
for example \(10/3\) at \(a=2\) and \(56/9\) at \(a=3\). Since \(1+x\le e^x\) and \(\sum_{m=1}^{a-1}\frac1m\le1+\log a\), this bound is at most \(\frac32e^{1/3}a^{4/3}<2.1\,a^{4/3}\). On this evidence, a bound below \(9/4\) by the same route needs further inequalities valid for all profiles.

The profile of \(\rho_X\) is \(P(a,b)=\sqrt{ab(a+b-1)}\) (Exercise 4.1), so \(P(a,a)=a\sqrt{2a-1}\), which grows like \(a^{3/2}\). For a profile with \(t=\frac23\), the bound of Lemma 4.1 is \((2a-1)^{3/2}\), of the same order.

## 4. Exercises

**5.1** (easy). Check that \((1+\frac1{3m})^3\ge1+\frac1m\) for every \(m\ge1\), and that \(\prod_{m=1}^{a-1}(1+\frac1m)=a\).

**5.2** (easy). Follow the proof of Lemma 5.1 for \(a=2\): show \(H_2\ge\frac43\) and \(D_2\ge\frac{10}3\), and compare with \(2^{4/3}\).

**5.3** (medium). Show that the function \(P(a,b)=a+b-1\) satisfies conditions 1 and 2 of Lemma 5.1 but not condition 3, and that the conclusion of Lemma 5.1 fails for it.

## 5. Solutions

**5.1.** \((1+x)^3=1+3x+3x^2+x^3\ge1+3x\) for \(x\ge0\); take \(x=\frac1{3m}\). The product is \(\prod_{m=1}^{a-1}\frac{m+1}m=a\).

**5.2.** Step 3 gives \(H_2\ge H_1(1+\frac13)=\frac43\), and \(D_2=\frac52H_2\ge\frac{10}3\approx3.33\), larger than \(2^{4/3}\approx2.52\).

**5.3.** \(P\) is symmetric, \(P(1,b)=b\), and \(P\) is affine in \(b\), so condition 2 holds with equality. For condition 3, \(P(a,3h+a-1)=3h+2a-2\) and \(3P(a,h)=3h+3a-3\); the first is smaller as soon as \(a\ge2\). Finally \(P(a,a)=2a-1<a^{4/3}\) for large \(a\), for example \(a=8\): \(15<16\).

## References

- [OpenAI-MM] OpenAI, *An upper bound of 9/4 for the matrix multiplication exponent*, OpenAI Math Release preprint, 2 October 2026, Section 5. https://github.com/openai/math/tree/main/preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026
