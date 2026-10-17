# Separating a shared leg

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A full direct sum requires disjoint variables on all three legs. Often the useful pieces of a tensor have disjoint variables on two legs but share the third. This lesson separates \(M\) such pieces, at the cost of \(5M\) copies of the tensor, by a Fourier projection followed by a degeneration whose weight is the square of a label mismatch (Proposition 3.2); each separated piece carries a dot product of length \(M\). Counting words of a given composition then turns the construction into an entropy inequality for characters (Corollary 3.4). The construction is OpenAI's [OpenAI-MM, Section 3]. Notation from [Tensors, rank and the exponent](tensors-rank-and-the-exponent.md) and [Characters and degenerations](characters-and-degenerations.md) is used throughout.

## 1. Roots of unity

**Lemma 3.1.** Let \(L\ge1\) and let \(\zeta\in F\) be a primitive \(L\)-th root of unity. For every integer \(n\),
\[
\frac1L\sum_{r=0}^{L-1}\zeta^{rn}=\begin{cases}1&\text{if }L\mid n,\\0&\text{otherwise.}\end{cases}
\]

**Proof.** If \(L\mid n\), every term is \(1\). Otherwise \(\zeta^n\ne1\), and the geometric sum equals \((\zeta^{nL}-1)/(\zeta^n-1)=0\). \(\square\)

## 2. Finite separation

**Definition.** Let \(A_1,\dots,A_M\) be tensors that have the same \(X\)-variables, pairwise disjoint sets of \(Y\)-variables and pairwise disjoint sets of \(Z\)-variables. The sum of forms \(A=A_1+\dots+A_M\) is called a *sum with a shared \(X\)-leg and matched sectors*, and the \(A_h\) are its *sectors*. Thus every term of \(A\) contains a \(Y\)-variable and a \(Z\)-variable of the same sector.

**Proposition 3.2** (finite separation). Let \(A=A_1+\dots+A_M\) be a sum with a shared \(X\)-leg and matched sectors. Then
\[
5M\cdot A\;\rightsquigarrow\;\bigoplus_{h=1}^M\bigl(A_h\otimes B_X(M)\bigr),
\]
where on the right the summands have disjoint variables on all three legs; in particular each \(A_h\) has its own copy of the \(X\)-variables.

**Proof.** Write the \(X\)-variables as \(x_a\), the \(Y\)-variables of \(A_h\) as \(y_{h,b}\) and its \(Z\)-variables as \(z_{h,c}\), so that
\[
A=\sum_{h,a,b,c}c_{h,a,b,c}\,x_a\,y_{h,b}\,z_{h,c}.
\]
Put \(L=5M\) and let \(\zeta\in F\) be a primitive \(L\)-th root of unity. The tensor \(5M\cdot A\) is the direct sum of \(L\) copies of \(A\); give the variables of the copy number \(r\in\{0,\dots,L-1\}\) the superscript \((r)\). Introduce new variables \(X_{a,g}\), \(Y_{h,b,u}\), \(Z_{h,c,v}\) with \(g,u,v\in\{1,\dots,M\}\), and substitute, for every \(r\),
\[
\begin{aligned}
x_a^{(r)}&=\sum_{g=1}^M\zeta^{2rg}X_{a,g},\\
y_{h,b}^{(r)}&=\sum_{u=1}^M\zeta^{r(u-h)}Y_{h,b,u},\\
z_{h,c}^{(r)}&=\frac1L\sum_{v=1}^M\zeta^{-r(v+h)}Z_{h,c,v}.
\end{aligned}
\]
All copies are mapped into the same new variables, so the result \(A''\) is a restriction of \(5M\cdot A\). The term \(c_{h,a,b,c}x_a^{(r)}y_{h,b}^{(r)}z_{h,c}^{(r)}\) contributes \(\frac1Lc_{h,a,b,c}\zeta^{r(u-v+2(g-h))}\) to the coefficient of \(X_{a,g}Y_{h,b,u}Z_{h,c,v}\). Summing over \(r\) and using Lemma 3.1,
\[
A''=\sum c_{h,a,b,c}\,X_{a,g}\,Y_{h,b,u}\,Z_{h,c,v},
\]
the sum over all \(h,a,b,c\) and over the \(g,u,v\) with \(L\mid u-v+2(g-h)\). Since \(|u-v+2(g-h)|\le3(M-1)<L\), the condition is
\[
u-v+2(g-h)=0. \tag{3.1}
\]

Give the new variables the weights
\[
\begin{aligned}
w(X_{a,g})&=g^2,\\
w(Y_{h,b,u})&=hu-h^2,\\
w(Z_{h,c,v})&=-hv.
\end{aligned}
\]
By (3.1), \(v=u+2(g-h)\) on every term of \(A''\), and the weight of the term is
\[
\begin{aligned}
&g^2+hu-h^2-h\bigl(u+2(g-h)\bigr)\\
&\qquad=(g-h)^2\ge0.
\end{aligned}
\]
The terms of weight zero are those with \(g=h\), and then \(v=u\). So the degeneration is
\[
A'=\sum_{h,a,b,c,u}c_{h,a,b,c}\,X_{a,h}\,Y_{h,b,u}\,Z_{h,c,u}.
\]
For fixed \(h\), the part of \(A'\) with this \(h\) is \(A_h\otimes B_X(M)\), with \(X_{a,h}\) for \(x_a\otimes x\), \(Y_{h,b,u}\) for \(y_{h,b}\otimes y_u\) and \(Z_{h,c,u}\) for \(z_{h,c}\otimes z_u\). Parts with different \(h\) have disjoint variables on all three legs, so \(A'\) is the direct sum in the statement. \(\square\)

The construction uses two different multiplicities: the right side has \(M\) direct summands, and each carries a dot product of length \(M\). The dot products do not label additional direct summands; their value under a character, \(M^{p_X}\), is the gain that Corollary 3.4 exploits.

## 3. Counting words

For a probability vector \(q=(q_1,\dots,q_s)\) write \(H(q)=-\sum_iq_i\log q_i\), with natural logarithms and \(0\log0=0\).

**Lemma 3.3.** Let \(q\) be a probability vector and \(N\ge1\) an integer such that all \(Nq_i\) are integers. Then the multinomial coefficient \(M=N!/\prod_i(Nq_i)!\) satisfies
\[
(N+1)^{-s}e^{NH(q)}\le M\le e^{NH(q)}.
\]

**Proof.** For integers \(n_1,\dots,n_s\ge0\) with \(\sum_in_i=N\) put
\[
\Pi(n)=\frac{N!}{\prod_in_i!}\prod_iq_i^{n_i}.
\]
By the multinomial theorem, \(\sum_n\Pi(n)=(q_1+\dots+q_s)^N=1\). For integers \(m,k\ge0\) one has \(m!/k!\ge k^{m-k}\): for \(m\ge k\) the quotient is a product of \(m-k\) factors greater than \(k\), and for \(m<k\) it is the reciprocal of a product of \(k-m\) factors at most \(k\). Let \(n^*=(Nq_i)_i\). If \(\Pi(n)>0\), then \(n_i=0\) whenever \(q_i=0\), and
\[
\begin{aligned}
\frac{\Pi(n^*)}{\Pi(n)}&=\prod_{q_i>0}\frac{n_i!}{(Nq_i)!}\,q_i^{Nq_i-n_i}\\
&\ge\prod_{q_i>0}N^{n_i-Nq_i}=1.
\end{aligned}
\]
So \(\Pi(n^*)\) is the largest of at most \((N+1)^s\) numbers with sum \(1\), whence \((N+1)^{-s}\le\Pi(n^*)\le1\). Finally \(\Pi(n^*)=M\prod_iq_i^{Nq_i}=Me^{-NH(q)}\). \(\square\)

## 4. The shared-leg entropy inequality

**Corollary 3.4.** Let \(T=T_1+\dots+T_s\) be a sum with a shared \(X\)-leg and matched sectors, with all \(T_i\ne0\). For every character \(\lambda\) and every probability vector \(q=(q_1,\dots,q_s)\),
\[
\lambda(T)\ge e^{p_X(\lambda)H(q)}\prod_{i=1}^s\lambda(T_i)^{q_i}.
\]

**Proof.** First let \(q\) be rational, and let \(N\) run through the multiples of a common denominator of the \(q_i\). The tensor power \(T^{\otimes N}\) is the sum of the tensors \(T_\mathbf w=T_{w_1}\otimes\dots\otimes T_{w_N}\) over all words \(\mathbf w=(w_1,\dots,w_N)\in\{1,\dots,s\}^N\). Every \(Y\)-variable of \(T^{\otimes N}\) is an \(N\)-tuple of \(Y\)-variables of \(T\), each belonging to one sector, so it has a word in \(\{1,\dots,s\}^N\); the same holds for the \(Z\)-variables, and a term of \(T_\mathbf w\) has \(Y\)- and \(Z\)-variables of word \(\mathbf w\). Substitute \(0\) for every \(Y\)-variable whose word does not contain each letter \(i\) exactly \(Nq_i\) times. The result
\[
A=\sum_{\mathbf w\text{ of type }q}T_\mathbf w
\]
is a restriction of \(T^{\otimes N}\), and it is a sum with a shared \(X\)-leg and matched sectors, the \(T_\mathbf w\), whose number is the multinomial coefficient \(M\) of Lemma 3.3. Reordering the factors shows \(T_\mathbf w\cong\prod_iT_i^{\otimes Nq_i}\), so \(\lambda(T_\mathbf w)=\prod_i\lambda(T_i)^{Nq_i}=:c_N\) for each of these words. By Proposition 3.2 and Lemma 2.9,
\[
\begin{aligned}
5M\,\lambda(T)^N&\ge5M\,\lambda(A)\\
&\ge\sum_\mathbf w\lambda(T_\mathbf w)\,\lambda(B_X(M))\\
&=M^{1+p_X}c_N.
\end{aligned}
\]
Hence \(\lambda(T)\ge5^{-1/N}M^{p_X/N}\prod_i\lambda(T_i)^{q_i}\). By Lemma 3.3, \(M^{1/N}\ge(N+1)^{-s/N}e^{H(q)}\); letting \(N\to\infty\) proves the inequality for rational \(q\). Since \(\lambda(T_i)\ge1\), the right side is a continuous function of \(q\) on the set of probability vectors, in which the rational ones are dense. \(\square\)

For each fixed \(N\) the proof uses one degeneration; nothing is required about how the weights of these degenerations grow with \(N\), because Lemma 2.9 is applied separately for each \(N\).

## 5. A maximum

**Lemma 3.5.** Let \(\alpha_1,\dots,\alpha_s>0\). For every probability vector \(q\),
\[
e^{H(q)}\prod_i\alpha_i^{q_i}\le\sum_i\alpha_i,
\]
with equality for \(q_i=\alpha_i/\sum_j\alpha_j\).

**Proof.** By the concavity of the logarithm (the weighted inequality between the arithmetic and the geometric mean),
\[
\begin{aligned}
\sum_{q_i>0}q_i\log\frac{\alpha_i}{q_i}&\le\log\sum_{q_i>0}q_i\frac{\alpha_i}{q_i}\\
&\le\log\sum_i\alpha_i,
\end{aligned}
\]
and the left side is the logarithm of \(e^{H(q)}\prod_i\alpha_i^{q_i}\). For \(q_i=\alpha_i/\sum_j\alpha_j\), every quotient \(\alpha_i/q_i\) equals \(\sum_j\alpha_j\), and both inequalities are equalities. \(\square\)

## 6. Exercises

**3.1** (easy). Let \(T=B_X(s)\), the sum of the sectors \(T_i=xy_iz_i\). Show that Corollary 3.4 with the uniform vector \(q\) is an equality.

**3.2** (medium). In the setting of Corollary 3.4, show that \(\lambda(T)\ge\bigl(\sum_i\lambda(T_i)^{1/p}\bigr)^p\) if \(p=p_X(\lambda)>0\), and \(\lambda(T)\ge\max_i\lambda(T_i)\) if \(p_X(\lambda)=0\).

**3.3** (easy). Check Lemma 3.3 for \(s=2\), \(q=(\frac12,\frac12)\) and \(N=2,4,6\).

**3.4** (medium). Show that Proposition 3.2 remains true with \(5M\) replaced by any integer \(L>3(M-1)\), and find a sum with a shared \(X\)-leg and matched sectors for which the substitution of the proof with \(M=2\) and \(L=3\) produces a term of weight zero with \(g\ne h\).

## 7. Solutions

**3.1.** Here \(\lambda(T_i)=1\), \(H(q)=\log s\), and the right side is \(e^{p_X\log s}=s^{p_X}=\lambda(B_X(s))\) by Lemma 2.4.

**3.2.** If \(p>0\), the right side of Corollary 3.4 is \(\bigl(e^{H(q)}\prod_i(\lambda(T_i)^{1/p})^{q_i}\bigr)^p\); choose \(q_i\) proportional to \(\lambda(T_i)^{1/p}\) and apply the equality case of Lemma 3.5. If \(p=0\), take for \(q\) the unit vector at an index \(i\) with the largest \(\lambda(T_i)\). (This case also follows from \(T\ge T_i\).)

**3.3.** The coefficients are \(M=2,6,20\); the lower bounds \(9^{-1}\cdot4\), \(25^{-1}\cdot16\), \(49^{-1}\cdot64\) are below \(2\); the upper bounds are \(e^{N\log2}=4,16,64\).

**3.4.** The proof uses \(L=5M\) only through \(|u-v+2(g-h)|\le3(M-1)<L\), which holds for every \(L>3(M-1)\); the weight computation does not involve \(L\). For \(M=2\) and \(L=3\), take \(A_1=xy_1z_1\) and \(A_2=xy_2z_2\), so \(A=B_X(2)\). With \(g=1\), \(h=2\), \(u=1\) and \(v=2\) one has \(u-v+2(g-h)=-3\), which is divisible by \(3\), so the term \(X_{1,1}Y_{2,1,1}Z_{2,1,2}\) occurs in \(A''\) with coefficient \(1\) (here the indices \(a,b,c\) take the single value \(1\)). Its weight is \(1+(2-4)-4=-5\), smaller than the weight zero of the intended terms; so the least weight is negative and the degeneration is not the intended direct sum.

## References

- [OpenAI-MM] OpenAI, *An upper bound of 9/4 for the matrix multiplication exponent*, OpenAI Math Release preprint, 2 October 2026, Section 3. https://github.com/openai/math/tree/main/preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026
- [LG] F. Le Gall, *Powers of tensors and fast matrix multiplication*, in Proceedings of the 39th International Symposium on Symbolic and Algebraic Computation (2014), 296–303; full version arXiv:1401.7714, Appendix A (counting words of a fixed composition in tensor-power arguments). https://arxiv.org/abs/1401.7714
