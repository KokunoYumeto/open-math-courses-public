# Entropy of finite random variables

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The proof of the uniform component bound for Gaussian primes measures how widely the residues of a randomly sampled walk position are spread, and how much a short word of later steps reveals about them. The measure is Shannon entropy. This lesson develops the finite theory that the course uses: entropy, conditional entropy and mutual information with their chain rules; relative entropy, Pinsker's inequality and a continuity bound; an entropy bound for short lists of candidates, in the spirit of Fano's inequality; and averages of entropies over random sets of coordinates, which are concave in the number of coordinates.

All random variables in this lesson take finitely many values. We assume finite probability, as in the core course [Probability (B90)](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-B90), and Jensen's inequality for concave functions of one real variable. The problem that motivates the lesson is described in [Walks through Gaussian primes](walks-through-gaussian-primes.md).

Basic references are [Polyanskiy–Wu] and [MacKay].

## 1. Entropy

Throughout, random variables are defined on a probability space \((\Omega,\mathbb P)\), and each takes finitely many values. The **law** of \(X\) is the function \(p(x)=\mathbb P(X=x)\) on its set of values. Logarithms are natural, and \(0\log0=0\).

**Definition 1.1.** The **entropy** of \(X\), with law \(p\), is

\[
H(X)=-\sum_xp(x)\log p(x).
\]

It depends only on the law, so we also write \(H(p)\). Each term is nonnegative, so \(H(X)\ge0\), with equality exactly when \(X\) is almost surely constant. If \(f\) is injective on the values of \(X\), then \(H(f(X))=H(X)\).

**Lemma 1.2** (Gibbs' inequality). Let \(p\) and \(q\) be probability laws on a finite set with \(q(x)>0\) wherever \(p(x)>0\). Then

\[
\sum_xp(x)\log\frac{p(x)}{q(x)}\ge0,
\]

with equality exactly when \(p=q\).

**Proof.** Use \(\log t\le t-1\), with equality only at \(t=1\). Summing over \(x\) with \(p(x)>0\),

\[
\sum_xp(x)\log\frac{q(x)}{p(x)}\le\sum_{p(x)>0}\bigl(q(x)-p(x)\bigr)\le1-1=0.
\]

Equality forces \(q(x)=p(x)\) wherever \(p(x)>0\); since both laws have total mass one, \(q\) then vanishes elsewhere. \(\square\)

**Corollary 1.3.** If \(X\) takes at most \(a\) values, then \(H(X)\le\log a\), with equality exactly when \(X\) is uniformly distributed on \(a\) values.

**Proof.** Apply Lemma 1.2 with \(q\) uniform on a set of \(a\) values containing those of \(X\): the sum equals \(\log a-H(X)\). \(\square\)

## 2. Conditional entropy

For finite random variables \(X\) and \(Y\), the pair \((X,Y)\) is again a finite random variable, with entropy \(H(X,Y)\). For a value \(y\) with \(\mathbb P(Y=y)>0\), write \(H(X\mid Y=y)\) for the entropy of the conditional law \(x\mapsto\mathbb P(X=x\mid Y=y)\).

**Definition 2.1.** The **conditional entropy** of \(X\) given \(Y\) is

\[
H(X\mid Y)=\sum_y\mathbb P(Y=y)\,H(X\mid Y=y),
\]

summed over the values of positive probability. Conditioning on several variables means conditioning on the tuple they form.

**Proposition 2.2** (chain rule). \(H(X,Y)=H(Y)+H(X\mid Y)\). More generally,

\[
H(X_1,\dots,X_n\mid Z)=\sum_{j=1}^nH(X_j\mid X_1,\dots,X_{j-1},Z).
\]

**Proof.** With \(p(x,y)=\mathbb P(X=x,Y=y)\) and \(p(y)=\mathbb P(Y=y)\), we have \(\log p(x,y)=\log p(y)+\log\bigl(p(x,y)/p(y)\bigr)\); multiply by \(-p(x,y)\) and sum. The general form follows by applying the first one conditionally on each value of \(Z\) and inducting on \(n\). \(\square\)

**Proposition 2.3** (conditioning does not increase entropy). \(H(X\mid Y,Z)\le H(X\mid Z)\). In particular \(H(X\mid Y)\le H(X)\), with equality exactly when \(X\) and \(Y\) are independent.

**Proof.** Fix \(Z=z\) and work in the conditional probability space; it suffices to treat the case without \(Z\). With \(p(x)\) the law of \(X\),

\[
H(X)-H(X\mid Y)=\sum_{x,y}p(x,y)\log\frac{p(x,y)}{p(x)p(y)},
\]

which is nonnegative by Lemma 1.2, applied to the joint law and the product law \(p(x)p(y)\). Equality holds exactly when these laws agree. \(\square\)

**Corollary 2.4.** The following hold for finite random variables.

1. (Subadditivity) \(H(X_1,\dots,X_n\mid Z)\le\sum_jH(X_j\mid Z)\).
2. (Determined variables) If \(X=f(Y)\) almost surely, then \(H(X\mid Y)=0\) and \(H(X\mid W)\le H(Y\mid W)\) for every \(W\). If \(X\) is determined by \((Y,Z)\), then \(H(X)\le H(Y)+H(Z)\).
3. (Cost of conditioning) \(H(X\mid Y)\ge H(X)-H(Y)\), and more generally \(H(X\mid Y,Z)\ge H(X\mid Z)-H(Y\mid Z)\).
4. (Equivalent conditions) If \(Y\) and \(Y'\) determine each other, then \(H(X\mid Y)=H(X\mid Y')\). If \(Y'\) is determined by \(Y\), then \(H(X\mid Y)\le H(X\mid Y')\).

**Proof.** (1) Combine the chain rule with Proposition 2.3. (2) Given \(Y=y\), the variable \(X\) is constant. By the chain rule \(H(X\mid W)\le H(X,Y\mid W)=H(Y\mid W)+H(X\mid Y,W)=H(Y\mid W)\). If \(X\) is determined by \((Y,Z)\), then \(H(X)\le H(Y,Z)\le H(Y)+H(Z)\). (3) \(H(X\mid Z)\le H(X,Y\mid Z)=H(Y\mid Z)+H(X\mid Y,Z)\). (4) The events \(\{Y=y\}\) and \(\{Y'=y'\}\) coincide for corresponding values, so the conditional laws agree. If \(Y'=g(Y)\), then \(H(X\mid Y)=H(X\mid Y,Y')\le H(X\mid Y')\) by the first part and Proposition 2.3. \(\square\)

**Proposition 2.5** (independent blocks). If \(X_1,\dots,X_n\) are conditionally independent given \(Z\), then \(H(X_1,\dots,X_n\mid Z)=\sum_jH(X_j\mid Z)\).

**Proof.** Given \(Z=z\), the joint law is the product of the marginal laws, and the logarithm of a product is the sum of the logarithms. \(\square\)

## 3. Mutual information

**Definition 3.1.** The **mutual information** of \(X\) and \(Y\) given \(Z\) is

\[
I(X;Y\mid Z)=H(X\mid Z)-H(X\mid Y,Z).
\]

Without \(Z\) we write \(I(X;Y)=H(X)-H(X\mid Y)\).

By Proposition 2.3 it is nonnegative. The chain rule gives the symmetric form \(I(X;Y\mid Z)=H(X\mid Z)+H(Y\mid Z)-H(X,Y\mid Z)\), so \(I(X;Y\mid Z)=I(Y;X\mid Z)\le\min\{H(X\mid Z),H(Y\mid Z)\}\).

**Proposition 3.2** (chain rule for information). \(I(X;Y,W\mid Z)=I(X;Y\mid Z)+I(X;W\mid Y,Z)\).

**Proof.** Both sides equal \(H(X\mid Z)-H(X\mid Y,W,Z)\): add and subtract \(H(X\mid Y,Z)\). \(\square\)

**Lemma 3.3** (removing a condition). For finite random variables \(A,B,C,S\),

\[
I(A;B\mid C,S)\le I(A;B\mid C)+H(S).
\]

**Proof.** Expand \(I(A;B,S\mid C)\) by Proposition 3.2 in the two possible orders:

\[
I(A;S\mid C)+I(A;B\mid C,S)=I(A;B\mid C)+I(A;S\mid B,C).
\]

Hence \(I(A;B\mid C,S)\le I(A;B\mid C)+I(A;S\mid B,C)\), and \(I(A;S\mid B,C)\le H(S\mid B,C)\le H(S)\). \(\square\)

**Lemma 3.4** (repeated observations). Let \(X,O,P\) be finite random variables, and let \(P_1,\dots,P_m\) be random variables that are conditionally independent given \((X,O)\), such that each triple \((X,O,P_a)\) has the same law as \((X,O,P)\). Then

\[
I(X;P_1,\dots,P_m\mid O)\le m\,I(X;P\mid O).
\]

**Proof.** By Definition 3.1 in its symmetric form, Proposition 2.5 and subadditivity,

\[
I(X;P_1,\dots,P_m\mid O)=H(P_1,\dots,P_m\mid O)-\sum_{a=1}^mH(P_a\mid X,O)
\le\sum_{a=1}^m\bigl(H(P_a\mid O)-H(P_a\mid X,O)\bigr).
\]

Each summand equals \(I(X;P\mid O)\), because it depends only on the law of \((X,O,P_a)\). \(\square\)

## 4. Mixtures and the binary entropy

The **binary entropy** is

\[
h(u)=-u\log u-(1-u)\log(1-u)\qquad(0\le u\le1),
\]

the entropy of a variable taking two values with probabilities \(u\) and \(1-u\). It is continuous, symmetric about \(\tfrac12\), and concave, since \(h''(u)=-1/(u(1-u))<0\) on \((0,1)\). It increases on \([0,\tfrac12]\), where \(h'(u)=\log((1-u)/u)\ge0\). Moreover

\[
h(u)\le u\log\frac eu,
\tag{4.1}
\]

because \(-(1-u)\log(1-u)\le u\): indeed \(-\log(1-u)\le u/(1-u)\), by the inequality \(\log t\le t-1\) applied to \(t=1/(1-u)\).

**Lemma 4.1** (mixtures). Let \(X\) and \(Y\) be finite random variables with values in the same set, and let \(\xi\) be an independent fair coin. Let \(V=X\) if \(\xi=0\) and \(V=Y\) if \(\xi=1\). Then for every function \(F\),

\[
H(F(V))\ge\tfrac12H(F(X))+\tfrac12H(F(Y)).
\]

**Proof.** By Proposition 2.3, \(H(F(V))\ge H(F(V)\mid\xi)\). Given \(\xi=0\), the variable \(F(V)\) is \(F(X)\), whose conditional law equals its law because \(\xi\) is independent of \((X,Y)\); likewise for \(\xi=1\). \(\square\)

## 5. Relative entropy, total variation and continuity

**Definition 5.1.** For probability laws \(p,q\) on a finite set, the **relative entropy** is

\[
D(p\Vert q)=\sum_xp(x)\log\frac{p(x)}{q(x)},
\]

with the value \(+\infty\) if \(q(x)=0<p(x)\) for some \(x\). The **total variation distance** is

\[
\operatorname{TV}(p,q)=\frac12\sum_x|p(x)-q(x)|=\max_A\bigl(p(A)-q(A)\bigr),
\]

the maximum being attained at \(A=\{x:p(x)>q(x)\}\).

By Lemma 1.2, \(D(p\Vert q)\ge0\). If \(u\) is the uniform law on a set of \(a\) elements containing the support of \(p\), then

\[
D(p\Vert u)=\log a-H(p).
\tag{5.1}
\]

If \(f\) is a map, the image laws satisfy \(\operatorname{TV}(f_*p,f_*q)\le\operatorname{TV}(p,q)\), because \(f_*p(A)-f_*q(A)=p(f^{-1}A)-q(f^{-1}A)\). For mixtures with the same weights, the triangle inequality gives \(\operatorname{TV}\bigl(\sum_j\lambda_jp_j,\sum_j\lambda_jq_j\bigr)\le\sum_j\lambda_j\operatorname{TV}(p_j,q_j)\).

**Lemma 5.2** (log-sum inequality). For nonnegative numbers \(a_1,\dots,a_n\) and \(b_1,\dots,b_n\) with \(b_j>0\) wherever \(a_j>0\), and \(a=\sum a_j\), \(b=\sum b_j>0\),

\[
\sum_ja_j\log\frac{a_j}{b_j}\ge a\log\frac ab.
\]

**Proof.** If \(a=0\) both sides vanish. Otherwise apply Lemma 1.2 to the laws \(a_j/a\) and \(b_j/b\): \(\sum_j(a_j/a)\log\bigl((a_j/a)(b/b_j)\bigr)\ge0\). \(\square\)

**Theorem 5.3** (Pinsker's inequality). For probability laws \(p,q\) on a finite set,

\[
D(p\Vert q)\ge2\operatorname{TV}(p,q)^2.
\]

**Proof.** We may assume \(D(p\Vert q)<\infty\). Let \(A=\{x:p(x)>q(x)\}\), \(u=p(A)\) and \(v=q(A)\), so that \(\operatorname{TV}(p,q)=u-v\). Lemma 5.2, applied separately to the terms with \(x\in A\) and with \(x\notin A\), gives

\[
D(p\Vert q)\ge u\log\frac uv+(1-u)\log\frac{1-u}{1-v}=:d(u,v).
\]

If \(v\in\{0,1\}\), finiteness forces \(u=v\) and there is nothing to prove. For fixed \(v\in(0,1)\), put \(\varphi(u)=d(u,v)-2(u-v)^2\) on \([0,1]\). Then \(\varphi(v)=0\), \(\varphi'(u)=\log\frac uv-\log\frac{1-u}{1-v}-4(u-v)\) vanishes at \(u=v\), and

\[
\varphi''(u)=\frac1{u(1-u)}-4\ge0\qquad(0<u<1).
\]

So \(\varphi\) is convex on \((0,1)\) with a critical point at \(v\), hence \(\varphi\ge0\) there, and by continuity on \([0,1]\). \(\square\)

*Reference:* [Polyanskiy–Wu, Theorem 7.10].

**Lemma 5.4** (maximal coupling). Let \(p,q\) be probability laws on a finite set \(\mathcal X\) with \(\operatorname{TV}(p,q)=\varepsilon\). There is a pair \((U,\widetilde U)\) of random variables with laws \(p\) and \(q\) such that \(\mathbb P(U\ne\widetilde U)=\varepsilon\).

**Proof.** If \(\varepsilon=0\), take \(U=\widetilde U\). Otherwise put \(m=\min(p,q)\), \(r=(p-q)_+\) and \(r'=(q-p)_+\), pointwise. Then \(m+r=p\), \(m+r'=q\), \(\sum r=\sum r'=\varepsilon\), and \(\sum m=1-\varepsilon\); also \(r\) and \(r'\) have disjoint supports. With probability \(1-\varepsilon\) draw one point from the law \(m/(1-\varepsilon)\) and let \(U=\widetilde U\) be that point (if \(\varepsilon=1\), this case does not occur). With probability \(\varepsilon\) draw \(U\) from \(r/\varepsilon\) and, independently, \(\widetilde U\) from \(r'/\varepsilon\); then \(U\ne\widetilde U\). The laws are \(m+r=p\) and \(m+r'=q\). \(\square\)

**Lemma 5.5** (continuity of entropy). Let \(p,q\) be laws on a set of at most \(a\) elements with \(\operatorname{TV}(p,q)\le\varepsilon\le\frac12\). Then

\[
|H(p)-H(q)|\le h(\varepsilon)+\varepsilon\log a.
\]

**Proof.** Let \(\varepsilon'=\operatorname{TV}(p,q)\), take the coupling of Lemma 5.4, and let \(\beta\) indicate the event \(U\ne\widetilde U\). By the chain rule,

\[
H(U)\le H(U,\widetilde U)=H(\widetilde U)+H(U\mid\widetilde U)\le H(\widetilde U)+H(\beta)+H(U\mid\widetilde U,\beta).
\]

Given \(\beta=0\), \(U\) is determined by \(\widetilde U\); given \(\beta=1\), its conditional entropy is at most \(\log a\). So \(H(U\mid\widetilde U,\beta)\le\varepsilon'\log a\), and \(H(\beta)=h(\varepsilon')\le h(\varepsilon)\), since \(h\) increases on \([0,\frac12]\). Exchange the roles of \(p\) and \(q\). \(\square\)

**Corollary 5.6** (continuity of conditional entropy). Let \((X,Y)\) and \((\widetilde X,\widetilde Y)\) be pairs whose joint laws, on a product set with at most \(a\) elements, have total variation at most \(\varepsilon\le\frac12\). Then

\[
|H(X\mid Y)-H(\widetilde X\mid\widetilde Y)|\le2h(\varepsilon)+2\varepsilon\log a.
\]

**Proof.** Write \(H(X\mid Y)=H(X,Y)-H(Y)\). The laws of \(Y\) and \(\widetilde Y\) are images of the joint laws, so their total variation is at most \(\varepsilon\); they live on a set with at most \(a\) elements. Apply Lemma 5.5 twice. \(\square\)

## 6. Short lists of candidates

When a variable \(Y\) narrows the possible values of \(X\) to a short list, the conditional entropy of \(X\) drops. The following bound quantifies this even when the list is short only some of the time, and when it contains \(X\) only some of the time.

**Lemma 6.1** (short lists). Let \(X\) take at most \(a\) values, let \(Y\) be a finite random variable, and for each value \(y\) let \(\mathcal L(y)\) be a set of possible values of \(X\). Let \(1\le b\le a\) be real, and

\[
\rho=\mathbb P\bigl(X\in\mathcal L(Y)\text{ and }|\mathcal L(Y)|\le b\bigr).
\]

Then

\[
\log a-H(X\mid Y)\ge\rho\log\frac ab-h(\rho).
\]

**Proof.** Let \(\beta\) indicate the event in the definition of \(\rho\). It is a function of \((X,Y)\), so

\[
H(X\mid Y)\le H(X,\beta\mid Y)=H(\beta\mid Y)+H(X\mid\beta,Y)\le h(\rho)+\rho\log b+(1-\rho)\log a.
\]

Indeed \(H(\beta\mid Y)\le H(\beta)=h(\rho)\). On the event \(\beta=1\), with \(Y\) known, \(X\) lies in the set \(\mathcal L(Y)\) with at most \(b\) elements, so the part of \(H(X\mid\beta,Y)\) coming from \(\beta=1\) is at most \(\rho\log b\); the part from \(\beta=0\) is at most \((1-\rho)\log a\). Rearrange. \(\square\)

With \(b=1\) and a single guess \(\mathcal L(y)=\{g(y)\}\), this is Fano's inequality in the form \(H(X\mid Y)\le h(\varepsilon)+\varepsilon\log a\), where \(\varepsilon=\mathbb P(X\ne g(Y))\) (Exercise 8.5); compare [Polyanskiy–Wu, Theorem 3.12].

## 7. Averages over random coordinates

In the course, a random point \(Z\) of \(\mathbb Z[i]\) is reduced modulo many prime factors at once, and the factors used are themselves chosen at random. Such auxiliary choices are never part of the measured data. We fix the choices, compute entropies in the experiment that samples \(Z\), and only then average over the choices.

**Convention 7.1** (averaged entropies). Let \(\mathcal C\) be an auxiliary random variable, with finitely many values, independent of the variables whose entropy is measured. For an entropy expression \(\Phi(\mathcal C)\) that depends on the value of \(\mathcal C\), such as \(H(\psi_{\mathcal C}(Z))\) for a family of functions \(\psi_c\), we write

\[
\mathbb E_{\mathcal C}\,\Phi(\mathcal C)=\sum_c\mathbb P(\mathcal C=c)\,\Phi(c),
\]

where each \(\Phi(c)\) is computed in the original experiment. This is an average of entropies; it is not the entropy of a mixture.

Let \(Y\) be a finite random variable, let \(\mathcal I\) be a finite index set, and for each \(c\in\mathcal I\) let \(\psi_c\) be a function on the values of \(Y\), with values in a set \(G_c\) of \(a_c\) elements. Let \(c_1,\dots,c_N\) be auxiliary random indices in \(\mathcal I\), independent of \(Y\), and put

\[
f(s)=\mathbb E\,H\bigl(\psi_{c_1}(Y),\dots,\psi_{c_s}(Y)\bigr)\qquad(0\le s\le N),
\]

in the sense of Convention 7.1, with \(f(0)=0\). The sequence of indices is **exchangeable** if the law of \((c_{\sigma(1)},\dots,c_{\sigma(N)})\) is the same for every permutation \(\sigma\) of \(\{1,\dots,N\}\).

**Proposition 7.2** (concavity in the number of coordinates). If the index sequence is exchangeable, then

\[
f(s+1)-f(s)=\mathbb E\,H\bigl(\psi_{c_{s+1}}(Y)\mid\psi_{c_1}(Y),\dots,\psi_{c_s}(Y)\bigr),
\]

and these increments do not increase with \(s\). Consequently, for \(1\le s\le N\),

\[
f(s+1)-f(s)\le\frac{f(s)}s\quad(s<N),\qquad f(1)\ge\frac{f(s)}s.
\]

**Proof.** The formula for the increment is the chain rule, applied for fixed indices and then averaged. Write \(\Psi_s\) for the tuple \((\psi_{c_1}(Y),\dots,\psi_{c_s}(Y))\). For fixed indices, Proposition 2.3 gives

\[
H\bigl(\psi_{c_{s+2}}(Y)\mid\Psi_{s+1}\bigr)\le H\bigl(\psi_{c_{s+2}}(Y)\mid\Psi_s\bigr).
\]

By exchangeability, \((c_1,\dots,c_s,c_{s+2})\) has the same law as \((c_1,\dots,c_s,c_{s+1})\), so the average of the right side is \(f(s+1)-f(s)\); the average of the left side is \(f(s+2)-f(s+1)\). For the consequences, \(f(s)\) is the sum of the first \(s\) increments, each at least \(f(s+1)-f(s)\) and at most \(f(1)\). \(\square\)

For uniformly chosen subsets of coordinates this is a form of Han's inequality; see [Polyanskiy–Wu, Theorem 1.7].

**Proposition 7.3** (one shared conditioning cost). Suppose that each index \(c_j\) is uniformly distributed on \(\mathcal I\), and put \(\overline L=\frac1{|\mathcal I|}\sum_{c\in\mathcal I}\log a_c\). Let \(1\le s\le N\), and let \(\mathcal H\) be a finite random variable, defined on the same space as \(Y\) and independent of the indices. If

\[
f(s)\ge(1-\varepsilon)\,s\,\overline L\qquad\text{and}\qquad H(\mathcal H)\le\kappa\,s\,\overline L,
\]

then

\[
\frac1{|\mathcal I|}\sum_{c\in\mathcal I}\bigl[\log a_c-H(\psi_c(Y)\mid\mathcal H)\bigr]\le(\varepsilon+\kappa)\,\overline L.
\]

No independence between \(Y\) and \(\mathcal H\) is assumed.

**Proof.** For fixed indices, Corollary 2.4(3) and subadditivity give

\[
H(\Psi_s)-H(\mathcal H)\le H(\Psi_s\mid\mathcal H)\le\sum_{j=1}^sH\bigl(\psi_{c_j}(Y)\mid\mathcal H\bigr).
\]

Average over the indices. Since each \(c_j\) is uniform on \(\mathcal I\), the right side averages to \(s\) times the mean of \(H(\psi_c(Y)\mid\mathcal H)\) over \(c\in\mathcal I\). The left side averages to at least \((1-\varepsilon-\kappa)s\overline L\). Divide by \(s\) and subtract from \(\overline L\), the mean of \(\log a_c\). \(\square\)

The point of Proposition 7.3 is the single payment \(H(\mathcal H)\). If separate data were used for each coordinate, their cost would be paid once per coordinate; a single shared vector is paid for once, in the joint entropy, and then distributed over all coordinates.

**Example 7.4** (signed coordinates). The course uses the following index sequence. Let \(\mathcal B\) be a finite set of rational primes congruent to \(1\) modulo \(4\), with \(k\) elements, and for each \(p\in\mathcal B\) fix its two conjugate factors \(\pi_{p,+}\) and \(\pi_{p,-}\) (Proposition 2.3 of [Walks through Gaussian primes](walks-through-gaussian-primes.md)). The index set \(\mathcal I\) consists of the \(2k\) **signed coordinates** \((p,\pm)\). Let \(p_1,\dots,p_k\) be a uniformly random ordering of \(\mathcal B\), let \(\sigma_1,\dots,\sigma_k\) be independent fair signs, independent of the ordering, and put \(c_j=(p_j,\sigma_j)\). This sequence is exchangeable, and each \(c_j\) is uniform on \(\mathcal I\). Its first \(s\) terms form a **uniform signed subset of size \(s\)**: \(s\) distinct primes, chosen uniformly, each with one of its two factors chosen by a fair coin. With \(\psi_c(z)=z\bmod\pi_c\), each \(G_c\) has \(a_c=p\) elements, and \(\overline L\) is the mean of \(\log p\) over \(\mathcal B\).

## 8. Exercises

**Exercise 8.1 (easy).** Compute \(h(\frac14)\) and \(H(X)\) for \(X\) uniform on \(a\) values. Show that \(h(u)\ge2u\log2\) for \(0\le u\le\frac12\).

**Exercise 8.2 (easy).** Show that \(H(X\mid Y)=0\) if and only if \(X\) is almost surely a function of \(Y\).

**Exercise 8.3 (easy).** Show that \(I(X;Y)=D(p_{XY}\Vert p_X\otimes p_Y)\), where \(p_X\otimes p_Y\) is the product of the marginal laws.

**Exercise 8.4 (medium).** Give an example of finite random variables with \(H(X\mid Y=y)>H(X)\) for some value \(y\). Why does this not contradict Proposition 2.3?

**Exercise 8.5 (medium).** Deduce Fano's inequality from Lemma 6.1: if \(X\) takes at most \(a\) values and \(\varepsilon=\mathbb P(X\ne g(Y))\) for some function \(g\), then \(H(X\mid Y)\le h(\varepsilon)+\varepsilon\log a\).

**Exercise 8.6 (medium).** Let \(Y\) be uniform on \(\mathbf F_p^2\) and let the three coordinates be \(\psi_1(y)=y_1\), \(\psi_2(y)=y_2\) and \(\psi_3(y)=y_1+y_2\). For a uniformly random ordering \(c_1,c_2,c_3\) of the indices, compute \(f(0),\dots,f(3)\) and check Proposition 7.2.

**Exercise 8.7 (hard).** Show that the constant \(2\) in Pinsker's inequality cannot be improved: compute \(D(\mathrm{Ber}(\frac12+t)\Vert\mathrm{Ber}(\frac12))\) to second order in \(t\).

## 9. Solutions

**8.1.** \(h(\frac14)=\frac14\log4+\frac34\log\frac43=\log4-\frac34\log3\approx0.562\). The uniform law on \(a\) values has entropy \(\log a\). The function \(h\) is concave with \(h(0)=0\) and \(h(\frac12)=\log2\), so on \([0,\frac12]\) it lies above the chord \(u\mapsto2u\log2\).

**8.2.** \(H(X\mid Y)=0\) exactly when each conditional law \(\mathbb P(X=\cdot\mid Y=y)\) of positive weight is a point mass, that is, when \(X=g(Y)\) almost surely for the function \(g\) assigning to \(y\) that point.

**8.3.** Both sides equal \(\sum_{x,y}p(x,y)\log\bigl(p(x,y)/(p(x)p(y))\bigr)\), as in the proof of Proposition 2.3.

**8.4.** Let \(Y\) be a fair coin, and let \(X=0\) if \(Y=0\), while \(X\) is a fair coin if \(Y=1\). Then \(\mathbb P(X=0)=\frac34\), so \(H(X)=h(\frac14)\approx0.562<\log2=H(X\mid Y=1)\). Proposition 2.3 concerns the average \(H(X\mid Y)=\frac12\log2\approx0.347\), which is smaller than \(H(X)\).

**8.5.** Take \(\mathcal L(y)=\{g(y)\}\) and \(b=1\). Then \(\rho=1-\varepsilon\), and Lemma 6.1 gives \(H(X\mid Y)\le\log a-(1-\varepsilon)\log a+h(1-\varepsilon)=\varepsilon\log a+h(\varepsilon)\).

**8.6.** Any one coordinate is uniform on \(\mathbf F_p\), and any two determine \(y\) and are jointly uniform on \(\mathbf F_p^2\); all three together still determine only \(y\). So \(f(0)=0\), \(f(1)=\log p\), \(f(2)=f(3)=2\log p\). The increments \(\log p,\log p,0\) do not increase.

**8.7.** With \(u=\frac12+t\),

\[
d(u,\tfrac12)=\log2-h(u)=u\log(2u)+(1-u)\log(2(1-u))=\tfrac12\bigl[(1+2t)\log(1+2t)+(1-2t)\log(1-2t)\bigr].
\]

Since \((1+x)\log(1+x)+(1-x)\log(1-x)=x^2+O(x^4)\), this is \(2t^2+O(t^4)\), while \(\operatorname{TV}=t\). So no constant larger than \(2\) works for small \(t\).

## References

- [Polyanskiy–Wu] Y. Polyanskiy, Y. Wu, Information Theory: From Coding to Learning, prepublication version, 2024. https://people.lids.mit.edu/yp/homepage/data/itbook-export.pdf
- [MacKay] D. J. C. MacKay, Information Theory, Inference, and Learning Algorithms, Cambridge University Press, 2003; free online edition. https://www.inference.org.uk/itprnn/book.pdf
