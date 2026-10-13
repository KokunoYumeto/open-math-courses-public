# The sum over type words and the lower bound

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The second trace of the map \(F_f\) for \(f=\operatorname{IMM}_{n,n}\) was bounded by a sum of numbers \(W(\tau)\) over all words \(\tau\) of length \(n\) in the two letters \(\mathcal N\) and \(\mathcal D\). This lesson shows that the sum is at most \(e^{3\sqrt n}\). It follows that the measure of \(f\) is at least \(D\,e^{-6\sqrt n}\), and the comparison with the bound for circuits proves the theorem of the course.

- The \(V\) layers are evenly spread (Lemma 1.1).
- Isolated positions are removed (Lemma 2.1).
- The sum over the runs of the letter \(\mathcal D\) (Lemma 3.1).
- \(R(\operatorname{IMM}_{n,n})\ge D\,e^{-6\sqrt n}\) (Proposition 4.1).
- The theorem over \(\mathbb C\) and over every field of characteristic zero (Section 5).
- What the constants of the proof give (Section 6).

The lesson follows [OpenAI-D, Sections 5 and 6]. It continues [Trace moments and paths](trace-moments-and-paths.md) and uses its notation: the division of the layers into the chunks \(V\,U^{l_i}\), the numbers \(w(\tau)\), \(d_V(\tau)\), \(d_U(\tau)\), \(h_t\), the set \(N_V(\tau)\), and
\[
\begin{aligned}
W(\tau)={}&n^{-w(\tau)}\,\alpha^{-d_V(\tau)}\,\beta^{d_U(\tau)}\\
&\cdot\prod_{t\in N_V(\tau)}\bigl(1+\alpha^{-1}n^{-h_t}\bigr).
\end{aligned}
\]
The numbers \(\alpha,\beta,\rho\) and their estimates are those of [A rank measure from differentiation and multiplication](a-rank-measure-from-differentiation-and-multiplication.md). Throughout, \(n\) is large.

## 1. The \(V\) layers are evenly spread

For a set \(I\) of consecutive layers (an *interval*) let \(V(I)\) and \(U(I)\) be the numbers of its \(V\) layers and of its \(U\) layers, and
\[
\operatorname{disc}(I)=V(I)-\rho\,U(I).
\]
Since \(\rho=k/m\), the interval of all layers has \(\operatorname{disc}=k-\rho m=0\). The number \(\rho\) is the proportion of the \(V\) layers to the \(U\) layers in the whole, and \(\operatorname{disc}(I)\) says by how much the interval \(I\) has more \(V\) layers than its proportion.

**Lemma 1.1.** For every interval \(I\), \(\operatorname{disc}(I)\le1+\rho\).

**Proof.** *Complete chunks.* Let \(I\) consist of the chunks \(j+1,\dots,j+c\), with \(c\ge0\). It has \(c\) layers of \(V\), and the number of its \(U\) layers is \(\sum_{i=j+1}^{j+c}l_i=c+E\) with
\[
E=\Bigl\lfloor\frac{(j+c)s}k\Bigr\rfloor-\Bigl\lfloor\frac{js}k\Bigr\rfloor .
\]
Here \(E>\tfrac{cs}k-1\), because \(\lfloor x\rfloor-\lfloor y\rfloor>x-y-1\) for all real \(x,y\).
From \(m=k+s\) we get \(1-\rho=\tfrac sm=\rho\,\tfrac sk\), and so
\[
\begin{aligned}
\operatorname{disc}(I)&=c(1-\rho)-\rho E\\
&=\rho\Bigl(\frac{cs}k-E\Bigr)<\rho .
\end{aligned}
\]

*The general case.* An interval that lies in one chunk contains at most one \(V\) layer, so its \(\operatorname{disc}\) is at most \(1\). Every other interval consists of an end part of a chunk, then complete chunks (possibly none), then a beginning part of a chunk. The end part, if it is not a complete chunk, contains only \(U\) layers: \(\operatorname{disc}\le0\). The beginning part contains one \(V\) layer: \(\operatorname{disc}\le1\). The function \(\operatorname{disc}\) is additive, so \(\operatorname{disc}(I)\le0+\rho+1\). \(\blacksquare\)

## 2. Isolated positions

Let
\[
\begin{gathered}
W_0(\tau)=n^{-w(\tau)}\,\alpha^{-d_V(\tau)}\,\beta^{d_U(\tau)},\\
Z=\sum_\tau W_0(\tau),
\end{gathered}
\]
where the sum runs over all words \(\tau\in\{\mathcal N,\mathcal D\}^n\).
So \(W(\tau)\) is \(W_0(\tau)\) times the factors \(1+\alpha^{-1}n^{-h_t}\) of the \(V\) layers of the type \(\mathcal N\). Such a factor is harmless if \(h_t\ge1\): then it is at most \(1+n^{-1/2}\), because \(\alpha^{-1}\le\sqrt n\). It is large, about \(\sqrt n\), if \(h_t=0\). For a \(V\) layer \(t\ge2\) this happens exactly if both neighbours \(t-1\) and \(t+1\) have the type \(\mathcal D\). (The layer \(n\) is a \(U\) layer, so a \(V\) layer \(t\ge2\) has two neighbours, and both are \(U\) layers.)

**Definition.** A position \(t\) is *isolated* in \(\tau\) if \(t\ge2\) is a \(V\) layer, \(\tau_t=\mathcal N\), and \(\tau_{t-1}=\tau_{t+1}=\mathcal D\).

**Lemma 2.1.** For large \(n\),
\[
\sum_\tau W(\tau)\le e^{\sqrt n}\,Z .
\]

**Proof.** *The map \(\Phi\).* For a word \(\tau\) let \(\Phi(\tau)\) be the word in which all isolated positions of \(\tau\) are changed to \(\mathcal D\). The neighbours of a \(V\) layer are \(U\) layers and are not changed. So \(\Phi(\tau)\) has no isolated position, and for the \(V\) layers of the type \(\mathcal N\) in \(\Phi(\tau)\) the numbers \(h_t\) are the same as in \(\tau\).

*The ratio.* Suppose \(j\) positions are changed. At each of them, the two switches at its two sides disappear; switches at different positions are different. Its factor \(1+\alpha^{-1}\) (here \(h_t=0\)) disappears, and \(d_V\) increases by \(1\). So
\[
\begin{aligned}
\frac{W(\tau)}{W(\Phi(\tau))}&=\Bigl(\frac{n^{-2}(1+\alpha^{-1})}{\alpha^{-1}}\Bigr)^j\\
&=\Bigl(\frac{1+\alpha}{n^2}\Bigr)^j .
\end{aligned}
\]

*The words with a given image.* Let \(y\) be a word without isolated positions, and let \(E(y)\) be the set of the \(V\) layers \(t\ge2\) with \(y_{t-1}=y_t=y_{t+1}=\mathcal D\). The words \(\tau\) with \(\Phi(\tau)=y\) are exactly the words obtained from \(y\) by changing the positions of a subset \(X\) of \(E(y)\) to \(\mathcal N\). Indeed, such a word has the isolated positions \(X\) and no others, because a further isolated position would be isolated in \(y\); and conversely the isolated positions of a word \(\tau\) with \(\Phi(\tau)=y\) lie in \(E(y)\). Hence
\[
\begin{aligned}
\sum_{\tau:\ \Phi(\tau)=y}W(\tau)&=W(y)\Bigl(1+\frac{1+\alpha}{n^2}\Bigr)^{|E(y)|}\\
&\le W(y)\Bigl(1+\frac2{n^2}\Bigr)^k .
\end{aligned}
\]

*Words without isolated positions.* In such a word \(y\), every \(V\) layer \(t\ge2\) of the type \(\mathcal N\) has a neighbour of the type \(\mathcal N\), and the position between them is an inner position; so \(h_t\ge1\). For the layer \(1\) only \(h_1\ge0\) is known. So
\[
W(y)\le W_0(y)\,(1+\alpha^{-1})\Bigl(1+\frac{\alpha^{-1}}n\Bigr)^k .
\]

*The sum.* Adding over all \(y\) without isolated positions, and then enlarging the sum of the \(W_0(y)\) to all words,
\[
\begin{aligned}
\sum_\tau W(\tau)\le{}&\Bigl(1+\frac2{n^2}\Bigr)^k(1+\alpha^{-1})\\
&\cdot\Bigl(1+\frac{\alpha^{-1}}n\Bigr)^kZ .
\end{aligned}
\]
With \(\alpha^{-1}\le\sqrt n\) and \(k\le\tfrac n2\), the logarithm of the factor before \(Z\) is at most
\[
\frac1n+\log(1+\sqrt n)+\frac{\sqrt n}2\le\sqrt n
\]
for large \(n\). \(\blacksquare\)

## 3. Runs

A *run* of a word is a maximal interval of positions of the type \(\mathcal D\).

**Lemma 3.1.** For large \(n\), \(Z\le e^{2\sqrt n}\).

**Proof.** *The weight of a run.* For a run \(I\), the layers of \(I\) contribute to \(W_0\) the factor
\[
\begin{aligned}
\alpha^{-V(I)}\beta^{U(I)}&\le\alpha^{-V(I)+\rho U(I)}\,e^{2U(I)/b}\\
&=\alpha^{-\operatorname{disc}(I)}\,e^{2U(I)/b},
\end{aligned}
\]
by \(\beta\le\alpha^\rho e^{2/b}\). If \(\operatorname{disc}(I)\le0\), then \(\alpha^{-\operatorname{disc}(I)}\le1\). Otherwise, by Lemma 1.1, \(\alpha^{-1}\le\sqrt n\) and \(\rho<1\),
\[
\alpha^{-\operatorname{disc}(I)}\le\alpha^{-(1+\rho)}\le n^{(1+\rho)/2}\le n .
\]
So every run contributes at most \(n\,e^{2U(I)/b}\). The runs are disjoint, so the factors \(e^{2U(I)/b}\) of all runs multiply to at most \(e^{2m/b}\).

*The two constant words.* The word \(\mathcal N^n\) has \(W_0=1\). The word \(\mathcal D^n\) is one run, the interval of all layers, with \(\operatorname{disc}=0\): \(W_0\le e^{2m/b}\).

*Mixed words.* Let \(\tau\) contain both letters. Let \(c\) be the number of its runs that contain neither the layer \(1\) nor the layer \(n\), and \(c'\in\{0,1,2\}\) the number of its runs that contain one of them; no run contains both. A run of the first kind has a switch at each of its two sides, a run of the second kind at one side, and every switch is at the side of exactly one run. So \(w(\tau)=2c+c'\), and
\[
\begin{aligned}
W_0(\tau)&\le n^{-(2c+c')}\cdot n^{c+c'}\,e^{2m/b}\\
&=n^{-c}\,e^{2m/b}.
\end{aligned}
\]
A run in the interior pays \(n^{-2}\) for its two switches and gains at most \(n\).

*Counting.* A word is determined by its first letter and the set of its switches. So there are \(2\binom{n-1}w\) words with \(w\) switches, and at most \(2\binom{n-1}{2c+c'}\) mixed words with given \(c\) and \(c'\). For each \(c'\in\{0,1,2\}\),
\[
\begin{aligned}
\sum_{c\ge0}\binom{n-1}{2c+c'}n^{-c}&\le\sum_{c\ge0}\frac{n^{c+c'}}{(2c+c')!}\\
&\le n^2\sum_{c\ge0}\frac{(\sqrt n)^{2c}}{(2c)!}\\
&\le n^2e^{\sqrt n}.
\end{aligned}
\]

*Together.*
\[
Z\le e^{2m/b}\bigl(2+6n^2e^{\sqrt n}\bigr).
\]
By \(m\le n\) and \(b\ge\tfrac14n^{5/2}\) we have \(\tfrac{2m}b\le8n^{-3/2}\le1\), and \(e\cdot(2+6n^2e^{\sqrt n})\le e^{2\sqrt n}\) for large \(n\); here \(e\) is Euler's number. \(\blacksquare\)

The even spread of the \(V\) layers is used in the weight of a run. A run with \(i\) more \(V\) layers than its proportion would contribute about \(n^{i/2}\). If the \(V\) layers were bunched together, a single run could gain much more than its two switches cost.

## 4. The lower bound for the measure

**Proposition 4.1** ([OpenAI-D]). Let \(K=\mathbb C\), and let the layers be divided as in the lesson on trace moments. For large \(n\),
\[
R(\operatorname{IMM}_{n,n})\ge D\,e^{-6\sqrt n}.
\]

**Proof.** Put \(f=\operatorname{IMM}_{n,n}\). By Lemmas 2.1 and 3.1, \(\sum_\tau W(\tau)\le e^{3\sqrt n}\). By \(\beta\le\tfrac2{\sqrt n}\) and \(m\le n\), \((1+\beta)^m\le e^{\beta m}\le e^{2\sqrt n}\). So Proposition 7.1 of the lesson on trace moments gives
\[
T_2\le D\,n^{2(n-1)}\,\mu^2\,e^{5\sqrt n},
\]
and Proposition 5.1 there gives \(T\ge D\,n^{n-1}\mu\,e^{-6/\sqrt n}>0\). By the lemma on the two traces,
\[
\begin{aligned}
R(f)=\operatorname{rank}F_f&\ge\frac{T^2}{T_2}\ge D\,e^{-12/\sqrt n-5\sqrt n}\\
&\ge D\,e^{-6\sqrt n}.
\end{aligned}
\]
\(\blacksquare\)

Since \(R(f)\le D\), the map \(F_f\) has almost the full rank on the scale of the proof, on which factors \(e^{O(\sqrt n)}\) do not matter and factors \(n^{\sqrt n/100}\) do.

## 5. The theorem

**Theorem 5.1** ([OpenAI-D]). There is a number \(n_0\) such that for every \(n\ge n_0\) and every field \(K\) of characteristic zero, every syntactically homogeneous \(\Sigma\Pi\Sigma\Pi\Sigma\) circuit over \(K\) that computes \(\operatorname{IMM}_{n,n}\) has a size of at least \(n^{\sqrt n/400}\).

This is Theorem 3.1 of [Iterated matrix multiplication and depth-five circuits](iterated-matrix-multiplication-and-depth-five-circuits.md).

**Proof for \(K=\mathbb C\).** Let a circuit of this kind and of size \(S\) compute \(f=\operatorname{IMM}_{n,n}\). Divide the layers as in the lesson on trace moments. By Proposition 4.1 and by Proposition 3.1 of [The rank of a depth-five circuit](the-rank-of-a-depth-five-circuit.md),
\[
\begin{aligned}
D\,e^{-6\sqrt n}&\le R(f)\\
&\le2S^2D\,e^{11\sqrt n}\,n^{-\sqrt n/100}.
\end{aligned}
\]
Since \(D>0\),
\[
S\ge2^{-1/2}\,e^{-\frac{17}2\sqrt n}\,n^{\sqrt n/200}. \tag{5.1}
\]
The right side is at least \(n^{\sqrt n/400}\) as soon as \(\tfrac{\sqrt n}{400}\log n\ge\tfrac{17}2\sqrt n+\tfrac12\log2\), which holds for \(\log n\ge3401\). \(\blacksquare\)

For the other fields we compare ranks.

**Lemma 5.2.** Let \(A\) be a matrix with entries in \(\mathbb Z\), and let \(K\) be a field of characteristic zero. The rank of \(A\) over \(K\) is equal to its rank over \(\mathbb Q\).

**Proof.** The rank of a matrix over a field is the largest number \(r\) such that some square submatrix with \(r\) rows has a determinant \(\ne0\). The determinants of the submatrices of \(A\) are integers, computed by the same formula over \(\mathbb Q\) and over \(K\). Since \(K\) has the characteristic zero, the image in \(K\) of an integer \(\ne0\) is \(\ne0\). \(\blacksquare\)

**Proof of Theorem 5.1 for a field \(K\) of characteristic zero.** For every field, the monomials are bases of \(\mathcal H(a,b)\) and \(\mathcal H(a-k,b+m)\). A partial derivative maps a monomial to an integer multiple of a monomial or to \(0\), a multiplication by a variable maps a monomial to a monomial, and \(f\) has the coefficients \(0\) and \(1\). So the matrix of \(F_f\) in the monomial bases has entries in \(\mathbb Z\), and it is the same matrix for every field. By Lemma 5.2, used for \(K\) and for \(\mathbb C\), its rank over \(K\) is its rank over \(\mathbb C\). The rank over \(\mathbb C\) does not depend on the bases. So Proposition 4.1 holds over \(K\), with the same number \(D\). Proposition 3.1 on circuits holds over every field. So (5.1) holds over \(K\). \(\blacksquare\)

## 6. What the proof gives

**No outside theorem is used.** The proof uses linear algebra (rank, trace, adjoint, determinants), binomial coefficients and power series, and elementary estimates. Every step is proved in the five lessons of this course.

**The size of \(n_0\).** [OpenAI-D] states the theorem with a number \(n_0\) and gives no value for it. With the constants found in this course, the last step, from (5.1) to the bound \(n^{\sqrt n/400}\), needs \(\log n\ge3401\), that is \(n\ge e^{3401}\), a number with \(1478\) digits. The other conditions on \(n\) in the lessons are far weaker; the course does not compute them. The right side of (5.1) is smaller than \(1\) for \(\log n\le1700\): for such \(n\) the inequality says nothing. The constants \(11\) and \(6\) in the exponents were not optimized here, and better constants would lower these thresholds; but the method compares a gain \(n^{-\sqrt n/100}=e^{-\sqrt n\log n/100}\) with losses \(e^{O(\sqrt n)}\), and such a comparison needs \(\log n\) to be large compared with \(100\) times the constant of the losses. The theorem is a statement about very large \(n\).

**How much the estimates lose.** The sum \(\sum_\tau W(\tau)\) can be computed exactly by a program that goes through the layers and keeps the last two letters. For \(n=10^3,10^4,10^5\) its logarithm is \(7.0\), \(14.3\) and \(32.1\); the bound \(3\sqrt n\) of this lesson is \(95\), \(300\) and \(949\). So the lower bound for the rank is better than \(D\,e^{-6\sqrt n}\) in these cases. The larger losses are in the bound for circuits, in the factors \(5^{4s}\) and \(\exp(4\sqrt n)\).

**Fields of positive characteristic.** Proposition 3.1 on circuits holds over every field. The lower bound for the rank of \(F_f\) was proved over \(\mathbb C\) and transferred by Lemma 5.2, which fails in positive characteristic: the rank of an integer matrix can drop modulo a prime (Exercise 7.4). The course proves nothing for these fields.

**Lower and upper bound.** Proposition 5.1 of the first lesson gives circuits of the size \(n^{\sqrt n+4}\) over every field. So the least size of a syntactically homogeneous \(\Sigma\Pi\Sigma\Pi\Sigma\) circuit for \(\operatorname{IMM}_{n,n}\) over a field of characteristic zero is between \(n^{\sqrt n/400}\) and \(n^{\sqrt n+4}\) for \(n\ge n_0\). The two exponents of \(n\) differ by a factor of about \(400\).

**The choice of \(s\).** The number \(s=m-k\) enters the bound for circuits in two opposite ways. If all factors of a product have degrees below \(t_0=\tfrac n{4s}\), the gain is \(q^{s/4}\), which is about \(n^{-s/8}\). If one factor has a degree of at least \(t_0\), the gain is \(q^{\lambda t_0/2}\), which is about \(n^{-n/(32s)}\). A larger \(s\) improves the first and spoils the second. With \(s\) about \(\sqrt n\) both are \(n^{-c\sqrt n}\) with a fixed \(c>0\). The upper bound of the first lesson has the same form for a similar reason: blocks of the length \(\sqrt n\) balance the cost inside a block against the cost of combining the blocks.

## 7. Exercises

**7.1.** For \(n=12\), \(s=2\), \(k=5\), \(m=7\) the division is \(VU\,VU\,VUU\,VU\,VUU\). Compute \(\operatorname{disc}\) for the intervals of the layers \(1\) to \(3\), \(1\) to \(5\) and \(6\) to \(7\), and compare with \(1+\rho\).

**7.2.** Show that there are exactly \(2\binom{n-1}w\) words of length \(n\) in two letters with \(w\) switches, and check \(\sum_w2\binom{n-1}w=2^n\).

**7.3.** For the division \(VU\,VU\,VUU\) of seven layers and the word \(\tau=\mathcal D\mathcal D\mathcal N\mathcal D\mathcal D\mathcal D\mathcal D\), find the isolated positions, \(W(\tau)\), \(\Phi(\tau)\), \(W(\Phi(\tau))\) and the ratio.

**7.4.** (a) Give a matrix with entries in \(\mathbb Z\) whose rank over the field with two elements is smaller than its rank over \(\mathbb Q\). (b) Let \(V=\{x\}\), \(U=\{y\}\), \(k=2\), \(m=0\), \(a=2\), \(b=0\) and \(g=x^2\). Compute \(R(g)\) over \(\mathbb Q\) and over the field with two elements.

**7.5.** Suppose that Proposition 3.1 on circuits held with \(n^{-\sqrt n/2}\) in place of \(n^{-\sqrt n/100}\), with the same other constants. For which \(n\) would (5.1) then be larger than \(1\)?

## 8. Solutions

**7.1.** \(\rho=\tfrac57\) and \(1+\rho=\tfrac{12}7\). Layers \(1\) to \(3\) are \(VUV\): \(\operatorname{disc}=2-\tfrac57=\tfrac97\). Layers \(1\) to \(5\) are \(VUVUV\): \(3-\tfrac{10}7=\tfrac{11}7\). Layers \(6\) to \(7\) are \(UU\): \(-\tfrac{10}7\). All are at most \(\tfrac{12}7\); the second is the largest value among all intervals of this division.

**7.2.** A word is determined by its first letter (2 choices) and by the set of the positions \(t\in\{1,\dots,n-1\}\) with \(\tau_t\ne\tau_{t+1}\) (\(\binom{n-1}w\) sets with \(w\) elements); every choice gives a word. The sum over \(w\) is \(2\cdot2^{n-1}\).

**7.3.** The \(V\) layers are \(1,3,5\). The position \(3\) is isolated: \(\tau_3=\mathcal N\), \(\tau_2=\tau_4=\mathcal D\). The word has \(w=2\), \(d_V=2\), \(d_U=4\), \(N_V=\{3\}\), \(h_3=0\):
\[
W(\tau)=n^{-2}\alpha^{-2}\beta^4(1+\alpha^{-1}).
\]
\(\Phi(\tau)=\mathcal D^7\) with \(W=\alpha^{-3}\beta^4\). The ratio is \(n^{-2}(1+\alpha^{-1})\alpha=\tfrac{1+\alpha}{n^2}\).

**7.4.** (a) The matrix \((2)\) with one row and one column: rank \(1\) over \(\mathbb Q\), rank \(0\) over the field with two elements. (b) \(\mathcal H(2,0)\) has the basis \(x^2\), and \(\mathcal H(0,0)\) the basis \(1\); \(D=1\). \(F_g=\partial_x^2\) maps \(x^2\) to \(2\). So \(R(g)=1\) over \(\mathbb Q\) and \(R(g)=0\) over the field with two elements. The matrix of \(F_g\) in the monomial bases is the matrix \((2)\) of (a).

**7.5.** Then (5.1) would read \(S\ge2^{-1/2}e^{-\frac{17}2\sqrt n}\,n^{\sqrt n/4}\). The right side is larger than \(1\) if \(\tfrac{\sqrt n}4\log n>\tfrac{17}2\sqrt n+\tfrac12\log2\), which holds for \(\log n\ge35\), that is \(n\ge e^{35}\approx1.6\cdot10^{15}\). The threshold depends strongly on the constant in the exponent of \(n\).

## References

- [OpenAI-D] OpenAI, *Homogeneous depth-five lower bounds for iterated matrix multiplication*, OpenAI Math Release preprint, 25 September 2026, Sections 5 and 6. https://github.com/openai/math/tree/main/preprints/Homogeneous-depth-five-lower-bounds-for-iterated-matrix-multiplication-September-25-2026
