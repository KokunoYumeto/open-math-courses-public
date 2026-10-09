# Linear Fourier coefficients and degree

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A Boolean function \(f:\{-1,1\}^n\to\{-1,1\}\) correlates with the sum of its inputs by \(\sum_i\widehat f(\{i\})=\mathbb E[f(X)(X_1+\dots+X_n)]\), the sum of its linear Fourier coefficients. By Cauchy–Schwarz this is at most \(\sqrt n\), with equality for majority. Gopalan and Servedio conjectured, around 2009, that \(\sqrt n\) can be replaced by \(\sqrt{\deg f}\), where \(\deg f\) is the degree of the multilinear polynomial representing \(f\); the conjecture is listed in O'Donnell's problem list [OD] and appears as a conjecture in the work of Filmus, Hatami, Keller and Lifshitz [FHKL]. A sharper proposal compares with majority on \(\deg f\) bits; Jha gave reformulations [Jha], Wang proved the cases \(\deg f=1\) and \(\deg f=n-1\) [Wan], and Kudin and Pašalić proved the cases of degree \(2\) and \(3\) and refuted this sharper form in degree \(4\). This course presents OpenAI's disproof of the square-root conjecture, even up to any constant factor [OpenAI-SR]:

**Theorem** (OpenAI 2026; Theorem 4.3 of [A tagged report](a-tagged-report.md)). For every real \(C>0\) there are \(n\) and a nonconstant \(f:\{-1,1\}^n\to\{-1,1\}\) with
\[
\sum_{i=1}^n\widehat f(\{i\})>C\sqrt{\deg f}.
\]

The proof does not build \(f\) directly. It builds finite *observations* of independent signs that retain much of the variance of their sum while every observation cell has low degree, and amplifies the ratio of retained variance to degree by grouping many independent copies. This first lesson sets up the Fourier expansion, proves the linear bound \(\sum_i|\widehat f(\{i\})|\le\deg f\) of Nisan and Szegedy, and develops the calculus of observations. [Asymptotically normal scores](asymptotically-normal-scores.md) proves the probability tools; [A tagged report](a-tagged-report.md) gives the main construction and two variants; [Average degree costs](average-degree-costs.md) gives an amplification that only needs a saving on average, with two further constructions.

## 1. Fourier expansion on the cube

Let \(X\) be uniform on \(\{-1,1\}^n\). For \(S\subseteq[n]=\{1,\dots,n\}\) the *character* \(\chi_S(x)=\prod_{i\in S}x_i\) has \(\chi_\varnothing=1\). For \(f:\{-1,1\}^n\to\mathbb R\) put
\[
\widehat f(S)=\mathbb E[f(X)\chi_S(X)],\qquad\deg f=\max\{|S|:\widehat f(S)\ne0\},
\]
with \(\deg f=0\) for constants.

**Lemma 1.1.** (a) \(\mathbb E[\chi_S\chi_T]=1\) if \(S=T\) and \(0\) otherwise.

(b) Every \(f\) satisfies \(f=\sum_S\widehat f(S)\chi_S\) and \(\mathbb E[fg]=\sum_S\widehat f(S)\widehat g(S)\); in particular \(\mathbb E[f^2]=\sum_S\widehat f(S)^2\).

(c) \(\deg(fg)\le\deg f+\deg g\), and \(\deg\) of a linear combination is at most the largest degree of its terms.

*Proof.* (a) \(\chi_S\chi_T=\chi_{S\triangle T}\), and \(\mathbb E\chi_U=\prod_{i\in U}\mathbb EX_i=0\) for \(U\ne\varnothing\). (b) The \(2^n\) characters are orthonormal in the \(2^n\)-dimensional space of functions on the cube, so they form a basis, and the coefficients are the inner products. (c) Expand both factors; each product \(\chi_S\chi_T=\chi_{S\triangle T}\) has \(|S\triangle T|\le|S|+|T|\). \(\square\)

So \(\deg f\) is the degree of the unique multilinear polynomial representing \(f\). The degree is invariant under the coordinate changes \(x_i\mapsto-x_i\), which change the sign of \(\widehat f(\{i\})\) and of no other linear coefficient. Hence the conjecture with \(\sum_i\widehat f(\{i\})\) and the version with \(\sum_i|\widehat f(\{i\})|\) are equivalent.

## 2. The linear bound

For \(f:\{-1,1\}^n\to\{-1,1\}\) and \(i\in[n]\), let \(x^{i\to\pm1}\) be \(x\) with the \(i\)-th coordinate set to \(\pm1\), and define the derivative \(D_if(x)=\frac12\bigl(f(x^{i\to1})-f(x^{i\to-1})\bigr)\in\{-1,0,1\}\). The *influence* \(\operatorname{Inf}_i(f)=\Pr(D_if(X)\ne0)\) is the probability that flipping the \(i\)-th coordinate changes \(f\), and \(I(f)=\sum_i\operatorname{Inf}_i(f)\) is the total influence.

**Proposition 2.1** (Nisan–Szegedy). For every \(f:\{-1,1\}^n\to\{-1,1\}\),
\[
\sum_{i=1}^n|\widehat f(\{i\})|\le I(f)=\sum_S|S|\,\widehat f(S)^2\le\deg f .
\]

*Proof.* From the expansion, \(D_if=\sum_{S\ni i}\widehat f(S)\chi_{S\setminus\{i\}}\), so \(\mathbb E[D_if]=\widehat f(\{i\})\) and, by Parseval, \(\mathbb E[(D_if)^2]=\sum_{S\ni i}\widehat f(S)^2\). Since \(D_if\in\{-1,0,1\}\), \(|\widehat f(\{i\})|\le\mathbb E|D_if|=\mathbb E[(D_if)^2]=\operatorname{Inf}_i(f)\). Summing over \(i\) gives \(I(f)=\sum_S|S|\widehat f(S)^2\le\deg f\sum_S\widehat f(S)^2=\deg f\), as \(\mathbb E f^2=1\). \(\square\)

So the correlation with the input sum is always at most linear in the degree; the theorem shows that the square root is not the right scale.

## 3. Observations and their scores

Throughout the course \(H_N=X_1+\dots+X_N\) is the sum of \(N\) independent uniform signs. An *observation* is a function \(F\) on \(\{-1,1\}^N\) with finitely many values. Its *score* and *retained variance* are
\[
T_F=\mathbb E[H_N\mid F],\qquad v(F)=\mathbb E[T_F^2];
\]
here conditional expectation is the elementary one on the finite partition of the cube into the level sets of \(F\). A positive real number \(D\) is a *cell degree bound* for \(F\) if \(\deg\mathbf 1_{\{F=a\}}\le D\) for every value \(a\).

**Lemma 3.1** (Calculus of observations). (a) If \(D\) is a cell degree bound for \(F\), every real function of \(F\) has degree at most \(D\).

(b) Let \(F_1,\dots,F_r\) be observations of disjoint blocks of independent signs, with cell degree bounds \(D_1,\dots,D_r\) and scores \(T_1,\dots,T_r\). Every function of the tuple \((F_1,\dots,F_r)\) has degree at most \(D_1+\dots+D_r\); the conditional expectation of the total sum \(H_{\mathrm{tot}}\) given the tuple is \(T_1+\dots+T_r\); and for every function \(Q\) of the tuple, \(\mathbb E[H_{\mathrm{tot}}\mid Q]=\mathbb E[T_1+\dots+T_r\mid Q]\).

(c) For an observation \(F\), the Boolean function \(f=\operatorname{sign}(T_F)\), with \(\operatorname{sign}0=1\), satisfies \(\deg f\le D\) and \(\sum_i\widehat f(\{i\})=\mathbb E|T_F|\).

*Proof.* (a) A function of \(F\) is \(\sum_ag(a)\mathbf 1_{\{F=a\}}\), a finite combination; use Lemma 1.1(c). (b) A function of the tuple is a combination of products \(\prod_k\mathbf 1_{\{F_k=a_k\}}\), whose degree is at most \(\sum_kD_k\) by Lemma 1.1(c). The block sum \(H_k\) and \(F_k\) are independent of the other blocks, so \(\mathbb E[H_k\mid F_1,\dots,F_r]=\mathbb E[H_k\mid F_k]=T_k\). For a function \(Q\) of the tuple, the level sets of \(Q\) are unions of those of the tuple, and averaging over a union (the tower property) gives the last identity. (c) \(f\) is a function of \(F\), and \(\sum_i\widehat f(\{i\})=\mathbb E[fH_N]=\mathbb E[f\,\mathbb E[H_N\mid F]]=\mathbb E[\operatorname{sign}(T_F)T_F]=\mathbb E|T_F|\). \(\square\)

**Corollary 3.2.** If for some observation \(\mathbb E|T_F|>C\sqrt D\), where \(D\) is a cell degree bound, then the theorem holds for \(C\) with \(f=\operatorname{sign}(T_F)\), which is nonconstant because its signed correlation \(\mathbb E|T_F|\) is positive.

By Cauchy–Schwarz, \(\mathbb E|T_F|\le\sqrt{v(F)}\); the strategy is to make \(v(F)/D\) large while keeping \(T_F/\sqrt{v(F)}\) close to a standard normal variable, for which \(\mathbb E|G|=\sqrt{2/\pi}>1/2\).

**Example 3.3.** Revealing \(m\) of the bits, \(F=(X_1,\dots,X_m)\), has \(T_F=X_1+\dots+X_m\), \(v(F)=m\), and cell degree bound \(m\): the ratio \(v/D\) is \(1\). Revealing the sum \(H_N\) itself has \(v=N\) and cell degree bound \(N\). Ratios larger than one require observations whose cells have small degree because of cancellation, not because they ignore coordinates.

## 4. Exercises

**4.1.** Compute the Fourier expansion of majority on three bits, \(\operatorname{maj}_3(x)=\operatorname{sign}(x_1+x_2+x_3)\), its degree, and \(\sum_i\widehat{\operatorname{maj}_3}(\{i\})\). Compare with \(\sqrt3\) and \(\sqrt{\deg}\).

**4.2.** Show that \(\sum_i\widehat f(\{i\})\le\sqrt n\) for every Boolean \(f\) on \(n\) bits, and that equality is possible only for \(n=1\).

**4.3.** For the parity \(\chi_{[n]}\), compute both sides of Proposition 2.1.

**4.4.** Show that the identity \(\mathbb E[H_{\mathrm{tot}}\mid F_1,\dots,F_r]=T_1+\dots+T_r\) of Lemma 3.1(b) can fail for observations of overlapping blocks, and explain why the degree bound needs no disjointness.

## 5. Solutions

**4.1.** \(\operatorname{maj}_3=\frac12(x_1+x_2+x_3)-\frac12x_1x_2x_3\): this agrees with the sign of \(x_1+x_2+x_3\) on all eight points. The degree is \(3\) and \(\sum_i\widehat{\operatorname{maj}_3}(\{i\})=3/2\), below \(\sqrt3\approx1.73=\sqrt{\deg}\).

**4.2.** \(\sum_i\widehat f(\{i\})=\mathbb E[fH_n]\le(\mathbb Ef^2)^{1/2}(\mathbb EH_n^2)^{1/2}=\sqrt n\). Equality in Cauchy–Schwarz would need \(f\) proportional to \(H_n\), which takes values in \(\{-1,1\}\) only for \(n=1\).

**4.3.** The only nonzero coefficient is \(\widehat f([n])=1\), so the linear sum is \(0\), \(I(f)=n\) (every flip changes the parity) and \(\deg f=n\).

**4.4.** Take one bit and \(F_1=F_2=X_1\), both observing the same block. Then \(\mathbb E[X_1\mid F_1,F_2]=X_1\), while \(T_1+T_2=2X_1\). The degree bound only uses Lemma 1.1(c), which holds for all products, overlapping or not; disjointness and independence are needed for the conditional expectation.

## References

- [OpenAI-SR] OpenAI, *Unbounded violations of the square-root degree bound*, OpenAI Math Release preprint, 26 September 2026. https://github.com/openai/math/blob/main/preprints/Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026/paper.pdf
- [OD] R. O'Donnell, *Open problems in analysis of Boolean functions*, 2012. https://arxiv.org/abs/1204.6447
- [FHKL] Y. Filmus, H. Hatami, N. Keller and N. Lifshitz, *On the sum of the L1 influences of bounded functions*, Israel Journal of Mathematics 214 (2016); preprint 2014. https://arxiv.org/abs/1404.3396
- [Jha] S. K. Jha, *On the sum of linear coefficients of a Boolean valued function*, 2016. https://arxiv.org/abs/1611.01029
- [Wan] Q. Wang, *On a conjecture of O'Donnell*, IACR Cryptology ePrint Archive 2020/002. https://eprint.iacr.org/2020/002
