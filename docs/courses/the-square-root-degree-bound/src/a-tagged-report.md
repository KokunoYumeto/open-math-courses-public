# A tagged report

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the main theorem of [Linear Fourier coefficients and degree](linear-fourier-coefficients-and-degree.md). Section 1 reduces it to a single *reporting rule* on \(m+1\) real inputs that retains more than \(m\) units of variance of their sum while each of its output cells is a combination of functions of only \(m\) inputs. Section 2 gives such a rule, the *refined report*: one input selects one of the other \(m\) inputs, and on the exceptional event where only the selected input fails a short interval test, the rule reports a single tag. Section 3 chooses the intervals for Gaussian inputs, and Section 4 transfers the Gaussian gain to finite scores with the tools of [Asymptotically normal scores](asymptotically-normal-scores.md). Section 5 gives two variants of the rule. Notation for observations, scores \(T_F\), retained variance \(v(F)\) and cell degree bounds is that of the first lesson.

## 1. Amplification

**Lemma 1.1** (Boolean readout). If there are finite observations with positive cell degree bounds \(D\) and arbitrarily large ratios \(v(F)/D\), the theorem holds.

*Proof.* Fix \(C>0\) and choose \(F\) with \(v=v(F)>4C^2D\). Take \(M\) independent copies on disjoint blocks, with scores \(T_1,\dots,T_M\), and \(f=\operatorname{sign}(T_1+\dots+T_M)\). By Lemma 3.1 of the first lesson, \(\deg f\le MD\) and \(\sum_i\widehat f(\{i\})=\mathbb E|T_1+\dots+T_M|=\sqrt{Mv}\,\mathbb E|Z_M|\) with \(Z_M=(T_1+\dots+T_M)/\sqrt{Mv}\). By Theorem 1.1 and Lemma 2.1 of [Asymptotically normal scores](asymptotically-normal-scores.md), \(\mathbb E|Z_M|\to\sqrt{2/\pi}>1/2\), so for large \(M\) the sum exceeds \(\frac12\sqrt{Mv}>C\sqrt{MD}\ge C\sqrt{\deg f}\); it is positive, so \(f\) is not constant. \(\square\)

A *rule* on \(r\) real inputs is a measurable map \(\mathcal W\) from \(\mathbb R^r\) to some set of output labels. Its *coordinate cost* is at most \(d\) if, on every product of finite subsets of \(\mathbb R\), the indicator of each output label is a finite linear combination of functions each depending on at most \(d\) coordinates.

**Proposition 1.2** (Amplification criterion). Let \(1\le d<r\), and let \(\mathcal W\) be a rule on \(r\) inputs with coordinate cost at most \(d\). Suppose there is \(\eta>0\) such that for every sequence \(Z_n\) of centered, variance-one, asymptotically standard normal random variables taking finitely many values, independent copies \(\mathbf Z_n=(Z_{n,1},\dots,Z_{n,r})\) satisfy, for all large \(n\),
\[
\operatorname{Var}\Bigl(\mathbb E\Bigl[\sum_{i=1}^rZ_{n,i}\Bigm|\mathcal W(\mathbf Z_n)\Bigr]\Bigr)\ge d+\eta .
\]
Then finite observations have arbitrarily large ratios \(v(F)/D\), and the theorem holds.

*Proof.* Let \(F\) be a finite observation with \(v=v(F)>0\) and cell degree bound \(D\). Form \(r\) blocks of \(M\) independent copies of \(F\), let \(Z_{M,i}\) be the normalized sum of the scores in block \(i\), and put \(F'=\mathcal W(Z_{M,1},\dots,Z_{M,r})\), an observation with finitely many values. A function of one input \(Z_{M,i}\) is a function of \(M\) copies of \(F\), of degree at most \(MD\); so the coordinate cost gives the cell degree bound \(dMD\) for \(F'\). By Lemma 3.1 of the first lesson, the score of \(F'\) is \(\mathbb E[\sum_i\sqrt{Mv}Z_{M,i}\mid F']\), so \(v(F')=Mv\operatorname{Var}(\mathbb E[\sum_iZ_{M,i}\mid F'])\). The variables \(Z_{M,i}\) are centered, have variance one and are asymptotically standard normal as \(M\to\infty\) (Theorem 1.1 of [Asymptotically normal scores](asymptotically-normal-scores.md)); so for large \(M\), \(v(F')\ge Mv(d+\eta)\), and
\[
\frac{v(F')}{dMD}\ge\frac vD\Bigl(1+\frac\eta d\Bigr).
\]
Start with one revealed sign (\(v=D=1\)) and iterate; each stage uses its own finite \(M\). Finitely many stages exceed any ratio, and Lemma 1.1 applies. \(\square\)

Revealing \(d\) of \(r=d+1\) inputs retains variance exactly \(d\). The criterion asks for a rule that beats this by a fixed margin at the same cost.

## 2. The refined report

Let \(m\ge3\), let \(I_1,\dots,I_m\) be intervals, and let \(\iota:\mathbb R\to\{1,\dots,m\}\) be a *selector* with finitely many cut points, so that each \(U_i=\{t:\iota(t)=i\}\) is a finite union of intervals; all endpoint conventions are fixed. Write the inputs as \((u,z_1,\dots,z_m)\), their sum as \(L=u+\sum_jz_j\), and
\[
B=\{z_j\in I_j\text{ for all }j\},\qquad P=\{z_j\in I_j\text{ for all }j\ne\iota(u)\},\qquad A=P\setminus B .
\]
So \(A\) is the event that the selected input \(z_{\iota(u)}\) alone fails its test, and \(A\), \(B\), \(P^c\) partition the inputs. The *refined report* \(\mathcal W\) reports:

| event | report |
|---|---|
| \(A\) | the tag \(A\) only |
| \(B\) | \((B,z_1,\dots,z_m)\) |
| \(P^c\) | \((P^c,u,\iota(u),(z_j)_{j\ne\iota(u)})\) |

**Lemma 2.1** (Cost of the refined report). On every product of finite input alphabets, \(\mathcal W\) has finitely many values and coordinate cost at most \(m\). The key identity is
\[
\mathbf 1_A=\sum_{i=1}^m\mathbf 1_{U_i}(u)\prod_{j\ne i}\mathbf 1_{I_j}(z_j)-\prod_{j=1}^m\mathbf 1_{I_j}(z_j). \tag{2.1}
\]

*Proof.* The first sum is \(\mathbf 1_P\), as exactly one \(i\) has \(u\in U_i\); subtracting \(\mathbf 1_B\le\mathbf 1_P\) gives \(\mathbf 1_A\). Each product involves \(m\) coordinates: \(u\) and \(m-1\) leaves, or the \(m\) leaves. An attained \(B\) report fixes the \(m\) leaves and is the product of their value tests. An attained \(P^c\) report fixes \(u\), \(i=\iota(u)\) and the other \(m-1\) leaves, one of which fails its test; so it forces \(P^c\) whatever \(z_i\) is, and its indicator depends on these \(m\) coordinates. Unattained labels have zero indicator. \(\square\)

The indicator of \(A\) depends on all \(m+1\) inputs, but (2.1) writes it as a combination of functions of \(m\) inputs: the saving comes from cancellation.

**Lemma 2.2** (Retained variance). Let the inputs be independent, centered, of variance one, each taking finitely many values. For every \(b\in\mathbb R\), with \(\Delta_b=\mathbb E\bigl[\mathbf 1_A(1-(L-b)^2)\bigr]\),
\[
\operatorname{Var}\bigl(\mathbb E[L\mid\mathcal W]\bigr)\ge m+\Delta_b .
\]

*Proof.* Predict \(L\) by \(b\) on \(A\), by \(\sum_jz_j\) on \(B\), and by \(u+\sum_{j\ne\iota(u)}z_j\) on \(P^c\); this is a function of the report. On \(B\) the error is \(u\), and \(B\) is independent of \(u\), so this part contributes \(\mathbb E[\mathbf 1_Bu^2]=\Pr(B)\). For each \(i\), the event \(E_i=P^c\cap\{u\in U_i\}\) depends only on \(u\) and the leaves other than \(z_i\), so the error \(z_i\) contributes \(\mathbb E[\mathbf 1_{E_i}z_i^2]=\Pr(E_i)\). The total squared error is \(\Pr(A^c)+\mathbb E[\mathbf 1_A(L-b)^2]=1-\Delta_b\). The conditional expectation, the orthogonal projection onto functions of the report, has at most this error, so \(\operatorname{Var}(\mathbb E[L\mid\mathcal W])=\operatorname{Var}(L)-\mathbb E(L-\mathbb E[L\mid\mathcal W])^2\ge(m+1)-(1-\Delta_b)\). \(\square\)

## 3. Gaussian intervals

**Lemma 3.1** (Gaussian design). There are an odd \(m\ge3\), closed intervals \(I_1,\dots,I_m\) and a selector \(\iota\) with finitely many cut points such that, for independent standard normal inputs, with \(\beta_j=\Pr(z_j\in I_j)\), conditional means \(\mu_j\) and variances \(s_j^2\) on \(I_j\),
\[
p_*=\prod_j\beta_j>0,\qquad S=\sum_js_j^2<\tfrac14,\qquad b=\sum_j\mu_j-1,
\]
the deficit satisfies
\[
d_A=\mathbb E\bigl[\mathbf 1_A(1-(L-b)^2)\bigr]>\tfrac34p_* .
\]

*Proof.* *An exact identity.* Fix \(u=t\) and \(i=\iota(t)\). Given \(u=t\), the event \(P\) has probability \(p_*/\beta_i\), restricts the leaves \(j\ne i\) to their intervals and leaves \(z_i\) free; then \(L-b\) has mean \(1+t-\mu_i\) and variance \(1+\sum_{j\ne i}s_j^2\). So, with \(\phi\) the normal density,
\[
\mathbb E\bigl[\mathbf 1_P(1-(L-b)^2)\bigr]=-p_*J,\qquad J=\int_{\mathbb R}\Bigl((1+t-\mu_{\iota(t)})^2+\sum_{j\ne\iota(t)}s_j^2\Bigr)\frac{\phi(t)}{\beta_{\iota(t)}}\,dt .
\]
On \(B\), with \(u\) free, \(L-b\) has mean \(1\) and variance \(1+S\), so \(\mathbb E[\mathbf 1_B(1-(L-b)^2)]=-p_*(1+S)\). As \(\mathbf 1_A=\mathbf 1_P-\mathbf 1_B\),
\[
d_A=p_*(1+S-J). \tag{3.1}
\]

*The intervals.* For odd \(m\) put \(R=\sqrt{8\log m}\), \(h=m^{-3/2}\), centres \(a_i=1-R+\frac{2R(i-1)}{m-1}\) and \(I_i=[a_i-h,a_i+h]\). For \(|t|\le R\) let \(\iota(t)\) be the index of a centre nearest to \(1+t\) (the smaller index on ties); for \(|t|>R\), the middle index, whose centre is \(1\). Then \(|\mu_i-a_i|\le h\), \(s_i^2\le h^2\), and \(\beta_i\ge2h\phi(|a_i|+h)\).

For \(|t|\le R\), the spacing gives \(|1+t-\mu_{\iota(t)}|\le\frac R{m-1}+h\) and \(|a_{\iota(t)}|+h\le|t|+2\) for large \(m\), so \(\phi(t)/\beta_{\iota(t)}\le\frac1{2h}e^{2|t|+2}\le\frac{e^2}{2h}e^{2R}\), and the central part of \(J\) is at most
\[
\frac{e^2R}he^{2R}\Bigl(\bigl(\tfrac R{m-1}+h\bigr)^2+mh^2\Bigr)=O\bigl(R(R^2+1)e^{2R}m^{-1/2}\bigr)\longrightarrow0,
\]
since \(e^{2R}=e^{2\sqrt{8\log m}}\) grows more slowly than every power of \(m\). For \(|t|>R\), the selected interval has \(\beta\ge2h\phi(2)\), the numerator is \(O(1+t^2)\), and \(\int_{|t|>R}(1+t^2)\phi(t)\,dt=O((R+1)e^{-R^2/2})=O((R+1)m^{-4})\), so the tail part is \(O((R+1)m^{-5/2})\to0\). Also \(S\le mh^2=m^{-2}\). For large odd \(m\), \(J<\frac14\) and \(S<\frac14\), and (3.1) gives \(d_A>\frac34p_*\). \(\square\)

The limit is reached only for very large \(m\). For \(|t|\le R\), \(\phi(t)/\beta_{\iota(t)}\) is close to \(e^{t+1/2}/(2h)\), the squared mismatch \((1+t-\mu_{\iota(t)})^2\) averages about \(R^2/(3(m-1)^2)\) over a selector cell, and \(S\) is close to \(mh^2/3\). So to leading order \(J\approx(R^2+1)e^{R+1/2}/(6\sqrt m)\), which is below \(\frac14\) only when \(\log m\) exceeds about \(54\).

Since \(d_A=\Pr(A)\bigl(1-\operatorname{Var}(L\mid A)-(\mathbb E[L\mid A]-b)^2\bigr)>0\), the sum varies by less than one unit on \(A\): this is the variance saved by the tag.

## 4. Transfer and the theorem

**Lemma 4.1** (Transfer). Fix the design of Lemma 3.1 and put \(\eta=p_*/2\). If \(Z_n\) are centered, variance-one, asymptotically standard normal random variables with finitely many values, then for independent copies \(\mathbf Z_n\) of \(m+1\) inputs and all large \(n\),
\[
\operatorname{Var}\bigl(\mathbb E[L\mid\mathcal W(\mathbf Z_n)]\bigr)>m+\eta .
\]

*Proof.* Expanding \(\mathbf 1_A\) by (2.1) and \((L-b)^2\) as a polynomial of degree two writes \(g=\mathbf 1_A(1-(L-b)^2)\) as a finite linear combination of functions \(\prod_k\mathbf 1_{J_k}(x_k)x_k^{a_k}\) with finite unions of intervals \(J_k\) (the intervals \(I_j\), the sets \(U_i\), or \(\mathbb R\)) and \(a_k\le2\). By Corollary 2.2 of [Asymptotically normal scores](asymptotically-normal-scores.md), \(\mathbb Eg(\mathbf Z_n)\to d_A>\frac34p_*\), so \(\Delta_b>\eta\) for large \(n\), and Lemma 2.2 applies. \(\square\)

**Theorem 4.2.** The refined report satisfies the amplification criterion (Proposition 1.2) with \((r,d,\eta)=(m+1,m,p_*/2)\).

*Proof.* Lemma 2.1 gives the cost and Lemma 4.1 the variance. \(\square\)

**Theorem 4.3** (OpenAI 2026). For every \(C>0\) there are \(n\) and a nonconstant \(f:\{-1,1\}^n\to\{-1,1\}\) with \(\sum_i\widehat f(\{i\})>C\sqrt{\deg f}\). Consequently \(\sup_f\sum_i|\widehat f(\{i\})|/\sqrt{\deg f}=\infty\) over all nonconstant Boolean functions.

*Proof.* Theorem 4.2 and Proposition 1.2. \(\square\)

The dimension and the number of copies used are finite but grow extremely fast; the proof gives no useful bound on them.

## 5. Two variants

**The coarse report.** Replace the report on \(B\) by a single mark: \(\mathcal O\) reports \(X\) on \(A\), \(Y\) on \(B\), and \((O,u,\iota(u),(z_j)_{j\ne\iota(u)})\) on \(P^c\).

**Proposition 5.1.** \(\mathcal O\) has coordinate cost at most \(m\). For independent centered variance-one inputs with finitely many values and constants \(b_0,b_1\), with \(g_{b_0,b_1}=\mathbf 1_A(1-(L-b_0)^2)+\mathbf 1_B(1-(L-b_1)^2)\),
\[
\operatorname{Var}\bigl(\mathbb E[L\mid\mathcal O]\bigr)\ge m+\mathbb Eg_{b_0,b_1}.
\]
For Gaussian inputs and the design of Lemma 3.1, \(\mathbb Eg_{b,M_\mu}=p_*(1-J)>\frac34p_*\), where \(M_\mu=\sum_j\mu_j\). Hence the coarse report also satisfies the amplification criterion with \((r,d,\eta)=(m+1,m,p_*/2)\).

*Proof.* The cost is as in Lemma 2.1; the \(Y\) indicator depends on the leaves only. Predict by \(b_0\) on \(X\), by \(b_1\) on \(Y\), and by \(u+\sum_{j\ne\iota(u)}z_j\) on ordinary reports; the error is \(\Pr(P^c)+\mathbb E[\mathbf 1_A(L-b_0)^2]+\mathbb E[\mathbf 1_B(L-b_1)^2]=1-\mathbb Eg_{b_0,b_1}\), and the variance bound follows as in Lemma 2.2. For Gaussian inputs, on \(B\) the variable \(L-M_\mu\) has mean \(0\) and variance \(1+S\), so \(\mathbb E[\mathbf 1_B(1-(L-M_\mu)^2)]=-p_*S\), and \(\mathbb Eg_{b,M_\mu}=d_A-p_*S=p_*(1-J)\) by (3.1). The transfer is as in Lemma 4.1. \(\square\)

The coarse report loses \(p_*S\) against the refined one: merging the \(B\) reports leaves the small leaf variance \(S\) unobserved.

**Switching to an independent input.** Keep \(A\) and \(b\), put \(q=m+1\), and add a further independent input \(w\). The rule \(\mathcal O_+\) reports \((\mathrm{off},\mathbf z)\) if \(\mathbf z=(u,z_1,\dots,z_m)\notin A\), and \((\mathrm{on},w)\) if \(\mathbf z\in A\).

**Proposition 5.2.** \(\mathcal O_+\) has \(q+1\) inputs and coordinate cost at most \(q\). For independent centered variance-one inputs with \(p=\Pr(A)>0\) and \(c=\mathbb E[L\mid A]\),
\[
\operatorname{Var}\bigl(\mathbb E[L+w\mid\mathcal O_+]\bigr)=q+p\bigl(1-\operatorname{Var}(L\mid A)\bigr)=q+\Delta_b+p(c-b)^2 .
\]
Hence \(\mathcal O_+\) satisfies the amplification criterion with \((r,d,\eta)=(m+2,m+1,p_*/2)\).

*Proof.* An off output fixes the \(q\) original inputs and ignores \(w\); an on output has indicator \(\mathbf 1_A(\mathbf z)\mathbf 1_{\{w=w_0\}}\), which by (2.1) is a combination of functions of \(m+1=q\) inputs. The conditional mean of \(L+w\) is \(L\) off \(A\) and \(c+w\) on \(A\), so its second moment is \(\mathbb E[\mathbf 1_{A^c}L^2]+p(c^2+1)=q-p\operatorname{Var}(L\mid A)+p\); and \(\Delta_b=p-p\bigl(\operatorname{Var}(L\mid A)+(c-b)^2\bigr)\). For asymptotically normal finite-valued inputs, Lemma 4.1 gives \(\Delta_b>p_*/2\) for large \(n\), hence \(p>0\) and a variance above \(q+p_*/2\). \(\square\)

## 6. Exercises

**6.1.** Verify identity (2.1) at a point where \(u\in U_2\), \(z_2\notin I_2\) and all other leaves pass, and at a point where two leaves fail.

**6.2.** Show that revealing any \(m\) of \(m+1\) independent centered variance-one inputs retains variance exactly \(m\), and that no report can retain more than \(m+1\).

**6.3.** Why must \(\eta\) in Proposition 1.2 be fixed independently of the stage? What would go wrong if the margin \(\eta_k\) at stage \(k\) satisfied \(\sum_k\eta_k/d<\infty\)?

**6.4.** In Lemma 3.1, why is the shift by one in \(b=\sum_j\mu_j-1\) essential? Compute \(d_A\) if \(b\) were \(\sum_j\mu_j\).

## 7. Solutions

**6.1.** At the first point, the sum in (2.1) has the single nonzero term \(i=2\), equal to \(1\) (all leaves \(j\ne2\) pass), and the product over all leaves is \(0\), so \(\mathbf 1_A=1\): only the selected leaf fails. If two leaves fail, every term of the sum and the product vanish: \(P\) fails for every selection.

**6.2.** Revealing all inputs but \(z_k\) gives \(\mathbb E[L\mid\cdot]=L-z_k\), with variance \(m\). Any conditional expectation has variance at most \(\operatorname{Var}L=m+1\).

**6.3.** Each stage multiplies the ratio by \(1+\eta_k/d\); the product of these factors is infinite exactly when \(\sum_k\eta_k=\infty\). With a fixed \(\eta\), finitely many stages exceed any ratio; with summable margins the ratio would stay bounded.

**6.4.** With \(b'=\sum_j\mu_j\), the mean of \(L-b'\) given \(u=t\) and \(P\) is \(t-\mu_i+\sum_{j\ne i}\mu_j-\sum_{j\ne i}\mu_j=t-\mu_{\iota(t)}\), and on \(B\) it is \(0\); the same computation gives \(d_A=p_*(1+S-J')-p_*\) with \(J'\) defined from \(t-\mu_{\iota(t)}\), and the positive constant \(1\) disappears: \(d_A=p_*(S-J')\le p_*S\), too small. The shift makes the mean on \(B\) equal to \(1\), and subtracting the \(B\) term turns its square into the gain.

## References

- [OpenAI-SR] OpenAI, *Unbounded violations of the square-root degree bound*, OpenAI Math Release preprint, 26 September 2026. https://github.com/openai/math/blob/main/preprints/Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026/paper.pdf
