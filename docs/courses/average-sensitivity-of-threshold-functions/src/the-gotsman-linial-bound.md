# The Gotsman–Linial bound

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves OpenAI's theorem [OpenAI-G, Sections 5 and 6]:

**Theorem 1.1** (OpenAI). Let \(n\ge1\) and \(1\le d\le n\), let \(p\) be a real polynomial of degree at most \(d\) in \(n\) variables, and \(f=\operatorname{sgn}p\) on \(\Omega=\{-1,1\}^n\), with \(\operatorname{sgn}0=1\). Then \(I(f)\le8d\sqrt n\).

The proof takes the weight \(w=|p|\) in the grading of [A weighted grading of the cube](a-weighted-grading-of-the-cube.md) and the sign function \(h=\chi_{[n]}f\), the product of \(f\) with the parity. Since parity changes sign across every edge, the edges on which \(h\) is constant are exactly the sensitive edges of \(f\), which Lemma 3.1 of that lesson bounds by the anticommutator \(T=MH+HM\). The function \(hw=\chi_{[n]}p\) has Fourier degrees at least \(n-d\). This makes the blocks of \(H\) between low grades vanish, and the squared sizes of the remaining blocks form the joint law of two binomial random variables whose sum is at least \(n-d\). The size of \(T\) is the mean square of that sum minus \(n\), and Lemma 3.1 of [Threshold functions and a one-sided coupling](threshold-functions-and-a-one-sided-coupling.md) bounds it by \(4d\sqrt n\).

We use Lemma 3.1 and the notation of [Threshold functions and a one-sided coupling](threshold-functions-and-a-one-sided-coupling.md), and Lemmas 1.1, 2.1 and 3.1 of [A weighted grading of the cube](a-weighted-grading-of-the-cube.md).

## 1. Proof of the theorem

**Step 1: no zeros.** If \(p\) takes negative values on \(\Omega\), add to \(p\) a positive constant smaller than \(\min\{|p(x)|:p(x)<0\}\); otherwise add any positive constant. Negative values stay negative, and zero and positive values become positive, so \(f\) is unchanged, the degree does not increase, and now \(p(x)\neq0\) for all \(x\in\Omega\).

**Step 2: parity.** Let \(\chi=\chi_{[n]}\), \(w=|p|>0\), \(h=\chi f\) and \(q=\chi p\). Then \(hw=\chi f|p|=\chi p=q\). For adjacent \(x,y\), \(\chi(x)=-\chi(y)\), so \(h(x)=h(y)\) exactly when \(f(x)\neq f(y)\). By (1.1) of [Threshold functions and a one-sided coupling](threshold-functions-and-a-one-sided-coupling.md),
\[
I(f)=\frac{|\mathcal E_h|}N,\qquad N=2^n.\tag{1.1}
\]
Since \(\chi\chi_S=\chi_{[n]\setminus S}\) and \(p\) has Fourier degree at most \(d\), \(q\) is a combination of characters \(\chi_S\) with \(|S|\ge n-d\).

**Step 3: vanishing blocks.** Build the grading of [A weighted grading of the cube](a-weighted-grading-of-the-cube.md) from \(w\), and let \(H\) be multiplication by \(h\). Then
\[
\Pi_sH\Pi_r=0\qquad\text{if }r+s<n-d.\tag{1.2}
\]
Indeed, elements of \(E_r\) and \(E_s\) have the form \(Da\) and \(Db\) with \(a\in V_r\), \(b\in V_s\), and
\[
\langle Db,HDa\rangle=\sum_x\overline{b(x)}a(x)w(x)h(x)=\sum_x\overline{b(x)}a(x)q(x)=0,
\]
because \(\overline b\,a\) has Fourier degree at most \(r+s<n-d\) and the characters are orthogonal.

**Step 4: the anticommutator as a second moment.** Let \(T=MH+HM\). Since \(M=\sum_k(k-\frac n2)\Pi_k\),
\[
\Pi_sT\Pi_r=(s+r-n)\,\Pi_sH\Pi_r,
\]
and by Lemma 1.1(c) of that lesson
\[
\frac1N\|T\|_{\rm HS}^2=\sum_{r,s=0}^n(s+r-n)^2\,\frac{\|\Pi_sH\Pi_r\|_{\rm HS}^2}N.\tag{1.3}
\]
The weights in (1.3) form a probability distribution with binomial marginals: since \(H\) is unitary, by Lemma 1.1(a),(c) there,
\[
\sum_s\|\Pi_sH\Pi_r\|_{\rm HS}^2=\|H\Pi_r\|_{\rm HS}^2=\|\Pi_r\|_{\rm HS}^2=\binom nr,\qquad\sum_r\|\Pi_sH\Pi_r\|_{\rm HS}^2=\|\Pi_sH\|_{\rm HS}^2=\|H^*\Pi_s\|_{\rm HS}^2=\binom ns,
\]
using \(\|B\|_{\rm HS}=\|B^*\|_{\rm HS}\) and \(\dim E_k=\binom nk\). Let \((R,S)\) be random with \(\mathbb P(R=r,S=s)=\|\Pi_sH\Pi_r\|_{\rm HS}^2/N\). Both \(R\) and \(S\) have the binomial distribution \(\operatorname{Bin}(n,\frac12)\), and (1.3) reads \(\frac1N\|T\|_{\rm HS}^2=\mathbb E(R+S-n)^2\).

**Step 5: the coupling.** Put \(U=S\) and \(V=n-R\). By the symmetry \(\binom nr=\binom n{n-r}\), \(U\) and \(V\) have the same distribution, with mean \(\frac n2\) and variance \(\frac n4\). By (1.2), \(R+S\ge n-d\) with probability one, that is \(V-U\le d\). Lemma 3.1 of [Threshold functions and a one-sided coupling](threshold-functions-and-a-one-sided-coupling.md), with \(a=d\) and \(\sigma=\frac{\sqrt n}2\), gives
\[
\frac1N\|T\|_{\rm HS}^2=\mathbb E(U-V)^2\le4d\sqrt n.
\]

**Step 6: conclusion.** By (1.1) and Lemma 3.1 of [A weighted grading of the cube](a-weighted-grading-of-the-cube.md),
\[
I(f)=\frac{|\mathcal E_h|}N\le\frac2N\|T\|_{\rm HS}^2\le8d\sqrt n.\qquad\square
\]

The proof never looks at individual edges of the cube: the weight \(|p|\) enters only through the grading, and the degree of \(p\) only through the vanishing blocks (1.2). In terms of [Sensitivity, block sensitivity and composition](course:sensitivity-and-block-sensitivity/sensitivity-block-sensitivity-and-composition), the theorem says that the average of the sensitivity \(s(f,x)\) over \(x\) is at most \(8d\sqrt n\), while the largest value \(s(f)\) can be \(n\) already for \(d=1\) (Exercise 3.1).

## 2. Noise sensitivity

For \(0\le\eta\le\frac12\), let \(X\) be uniform on \(\Omega\) and let \(Y\) be obtained from \(X\) by reversing each coordinate independently with probability \(\eta\). The *noise sensitivity* of \(f\) is \(\operatorname{NS}_\eta(f)=\mathbb P(f(X)\neq f(Y))\).

**Lemma 2.1.** With \(\widehat f(S)=2^{-n}\langle\chi_S,f\rangle\),
\[
\operatorname{NS}_\eta(f)=\frac12\sum_{S\subseteq[n]}\bigl(1-(1-2\eta)^{|S|}\bigr)\widehat f(S)^2,
\]
which is nondecreasing in \(\eta\in[0,\frac12]\).

**Proof.** Write \(Y_i=X_i\varepsilon_i\) with independent \(\varepsilon_i\), \(\mathbb P(\varepsilon_i=-1)=\eta\), independent of \(X\). Then \(\mathbb E[\chi_S(X)\chi_T(Y)]=\mathbb E[\chi_{S\triangle T}(X)]\,\mathbb E[\chi_T(\varepsilon)]=\mathbf 1_{S=T}(1-2\eta)^{|S|}\). Expanding \(f=\sum_S\widehat f(S)\chi_S\), \(\mathbb E f(X)f(Y)=\sum_S(1-2\eta)^{|S|}\widehat f(S)^2\), and \(\sum_S\widehat f(S)^2=\mathbb Ef(X)^2=1\). Since \(f(X)f(Y)=1-2\cdot\mathbf 1_{f(X)\neq f(Y)}\), the formula follows. Each \(1-(1-2\eta)^{|S|}\) is nondecreasing in \(\eta\). \(\square\)

**Corollary 2.2** (noise sensitivity of threshold functions; OpenAI). If \(f=\operatorname{sgn}p\) with \(\deg p\le d\), then \(\operatorname{NS}_\eta(f)\le8\sqrt2\,d\sqrt\eta\) for \(0<\eta\le\frac12\).

**Proof.** Constant functions have noise sensitivity \(0\), so let \(d\ge1\). Fix an integer \(q\ge2\). Choose independent uniform signs \(a_1,\dots,a_n\in\{-1,1\}\) and independent uniform buckets \(b(1),\dots,b(n)\in[q]\), and let
\[
g(z)=f\bigl(a_1z_{b(1)},\dots,a_nz_{b(n)}\bigr)\qquad(z\in\{-1,1\}^q).
\]
The polynomial \(p(a_1z_{b(1)},\dots)\) has degree at most \(d\) in \(z\) and agrees on \(\{-1,1\}^q\), zeros included, with a multilinear polynomial of degree at most \(\min\{d,q\}\), so Theorem 1.1 gives \(I(g)\le8d\sqrt q\) (and \(I(g)=0\) if that polynomial is constant).

Now choose, independently of \(a\) and \(b\), a uniform \(z\in\{-1,1\}^q\) and a uniform \(J\in[q]\), and let \(X_i=a_iz_{b(i)}\) and \(Y_i=X_i\cdot(-1)^{\mathbf 1_{b(i)=J}}\). Given \(J\), the indicators \(\mathbf 1_{b(i)=J}\) are independent with mean \(\frac1q\); given \(b\), \(J\) and \(z\), the signs \(a_i\) make \(X\) uniform. So \(X\) is uniform and independent of the reversal indicators, and \((X,Y)\) has the law in the definition of \(\operatorname{NS}_{1/q}\). Moreover \(Y\) is the input of \(f\) corresponding to \(z^{\oplus J}\), so \(f(X)\neq f(Y)\) exactly when \(g(z)\neq g(z^{\oplus J})\). Averaging over \(z\) and \(J\) first,
\[
\operatorname{NS}_{1/q}(f)=\mathbb E_{a,b}\Bigl[\frac1q\sum_{j=1}^q\mathbb P_z\bigl(g(z)\neq g(z^{\oplus j})\bigr)\Bigr]=\frac{\mathbb E_{a,b}I(g)}q\le\frac{8d}{\sqrt q}.
\]
For \(0<\eta\le\frac12\), let \(q=\lfloor1/\eta\rfloor\ge2\). Then \(\eta\le\frac1q\le\frac12\) and \(q\ge\frac1{2\eta}\), so by Lemma 2.1, \(\operatorname{NS}_\eta(f)\le\operatorname{NS}_{1/q}(f)\le8d\sqrt{2\eta}\). \(\square\)

The reduction by random buckets is due to Diakonikolas, Raghavendra, Servedio and Tan [DRST, Section 7.1]. Kane proved the analogous bound \(O(d\sqrt\varepsilon)\) for Gaussian noise [Kane-G].

**Remark.** Combined with the polynomial regression method of Kalai, Klivans, Mansour and Servedio, Corollary 2.2 gives an agnostic learning algorithm for polynomial threshold functions under the uniform distribution, with running time polynomial in \((n+1)^k\), \(k=O(d^2\alpha^{-2}\log(1/\alpha))\) [OpenAI-G, Section 6.2]. That consequence needs generalization bounds from learning theory and is not proved in this course.

## 3. Exercises

**Exercise 3.1** (easy). Show that the majority function \(\operatorname{sgn}(x_1+\dots+x_n)\), \(n\) odd, has sensitivity \(s(f)=\frac{n+1}2\), while its average sensitivity is of order \(\sqrt n\); and that \(f=\operatorname{sgn}(x_1+\dots+x_n-n+\frac12)\) (the AND function) has \(s(f)=n\) and \(I(f)=n2^{1-n}\).

**Exercise 3.2** (easy). Check \(\Pi_sT\Pi_r=(s+r-n)\Pi_sH\Pi_r\) from the definition of \(M\).

**Exercise 3.3** (medium). For \(d=n\) the theorem gives \(I(f)\le8n^{3/2}\), weaker than \(I(f)\le n\). Find the largest \(d\), as a function of \(n\), for which \(8d\sqrt n<n\).

**Exercise 3.4** (medium). Where does the proof use that \(f\) is the sign of a polynomial of degree at most \(d\), rather than an arbitrary Boolean function? Show that for \(f=\chi_{[n]}\) (degree \(n\) as a polynomial) the blocks in (1.2) need not vanish for any \(r+s<n\).

## 4. Solutions

**3.1.** For majority with \(n=2k+1\), at an input with \(k+1\) coordinates equal to \(1\) each of these \(k+1\) is sensitive, and no input has more sensitive coordinates; the average was computed in Exercise 4.1 of [Threshold functions and a one-sided coupling](threshold-functions-and-a-one-sided-coupling.md). For AND, the all-ones input has all \(n\) coordinates sensitive, the inputs with exactly one \(-1\) have one, and others none: \(I=(n+n\cdot1)/2^n=n2^{1-n}\).

**3.2.** \(\Pi_sMH\Pi_r=(s-\frac n2)\Pi_sH\Pi_r\) and \(\Pi_sHM\Pi_r=(r-\frac n2)\Pi_sH\Pi_r\), because \(\Pi_sM=(s-\frac n2)\Pi_s\) and \(M\Pi_r=(r-\frac n2)\Pi_r\).

**3.3.** \(8d\sqrt n<n\) means \(d<\sqrt n/8\); the largest such integer is \(\lceil\sqrt n/8\rceil-1\).

**3.4.** Only in Step 3, through the Fourier degrees of \(q=\chi p\). For \(f=\chi_{[n]}\) one may take \(p=\chi_{[n]}\), so \(w=1\) and \(q=\chi_{[n]}^2=1\) has degree \(0\); then \(H\) is multiplication by \(h=1\), the identity, and \(\Pi_sH\Pi_r=\Pi_r\) for \(s=r\), nonzero for every \(r\). Here \(d=n\), and (1.2) asserts nothing. Indeed \(I(\chi_{[n]})=n\).

## References

- [DRST] I. Diakonikolas, P. Raghavendra, R. A. Servedio and L.-Y. Tan, *Average sensitivity and noise sensitivity of polynomial threshold functions*, SIAM J. Comput. 43 (2014); arXiv:0909.5011. https://arxiv.org/abs/0909.5011
- [Kane-G] D. M. Kane, *The Gaussian surface area and noise sensitivity of degree-d polynomial threshold functions*, Comput. Complexity 20 (2011); arXiv:0912.2709, with the title *The Gaussian surface area and noise sensitivity of degree-d polynomials*. https://arxiv.org/abs/0912.2709
- [OpenAI-G] OpenAI, *Average sensitivity of polynomial threshold functions*, OpenAI Math Release preprint, 25 September 2026, Sections 5 and 6. https://github.com/openai/math/tree/main/preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026
