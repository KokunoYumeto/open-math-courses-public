# Besicovitch's covering theorem and the differentiation of Radon measures

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

For Lebesgue measure on \(\mathbb R^r\), the averages of a locally integrable function over the balls \(B(y,\delta)\) converge to its value at almost every \(y\) as \(\delta\to0\). The usual proof uses a covering argument of Vitali type, which needs a bound \(\lambda B(y,2\delta)\le C\lambda B(y,\delta)\) for the measure \(\lambda\). An arbitrary Radon measure on \(\mathbb R^r\) has no such bound. Besicovitch found a covering principle that uses only the geometry of Euclidean balls: from any family of balls centred at the points of a bounded set one can select \(5^r\) disjoint subfamilies that still cover the set (Theorem 3.1). From it follows the differentiation theorem for every Radon measure on \(\mathbb R^r\) (Theorem 5.1) and the density theorem (Corollary 5.2).

The covering principle and the differentiation theorem are due to Besicovitch. The form of the covering lemma with the constant \(5^r\), and the arrangement of the proofs, follow [Fremlin, Volume 4, Section 472], which is free to read.

We use from the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10): Lebesgue measure on \(\mathbb R^r\), which is translation invariant ([Fremlin, Volume 1, 134A](https://www1.essex.ac.uk/maths/people/fremlin/chap13.pdf)) and multiplies by \(|\det T|\) under a linear map \(T\) ([Fremlin, Volume 2, 263A](https://www1.essex.ac.uk/maths/people/fremlin/chap26.pdf)); Radon measures on \(\mathbb R^r\) and their outer regularity ([Fremlin, Volume 2, 256A–256B](https://www1.essex.ac.uk/maths/people/fremlin/chap25.pdf)); and the absolute continuity of the integral ([Fremlin, Volume 2, 225A](https://www1.essex.ac.uk/maths/people/fremlin/chap22.pdf)).

## 1. Radon measures on \(\mathbb R^r\)

Throughout, \(r\ge1\), \(\|\cdot\|\) is the Euclidean norm, and a *ball* is a closed ball \(B(x,\delta)=\{y:\|y-x\|\le\delta\}\) with \(\delta>0\). Write \(\mathcal L\) for Lebesgue measure and \(\beta_r=\mathcal L B(0,1)\), which is positive and finite. Since \(x\mapsto\delta x\) has determinant \(\delta^r\), \(\mathcal LB(x,\delta)=\beta_r\delta^r\).

A *Radon measure* on \(\mathbb R^r\) is a complete measure \(\lambda\), with domain \(\Sigma\), that is defined on all open sets, finite on bounded sets and inner regular with respect to the compact sets: \(\lambda E=\sup\{\lambda K:K\subseteq E\text{ compact}\}\) for \(E\in\Sigma\). It is outer regular: for \(E\in\Sigma\) and \(\varepsilon>0\) there is an open \(G\supseteq E\) with \(\lambda(G\setminus E)\le\varepsilon\). The *outer measure* of \(A\subseteq\mathbb R^r\) is \(\lambda^*A=\inf\{\lambda E:A\subseteq E\in\Sigma\}\). A function is *locally integrable* if it is integrable over every bounded measurable set.

**Lemma 1.1** (Outer measure). Let \(\lambda\) be a Radon measure and \(A\subseteq\mathbb R^r\) with \(\lambda^*A<\infty\).

1. There is \(E\in\Sigma\) with \(A\subseteq E\) and \(\lambda(F\cap E)=\lambda^*(F\cap A)\) for every \(F\in\Sigma\). (An *envelope* of \(A\).)
2. If \(A_0\subseteq A_1\subseteq\cdots\) and \(\lambda^*\bigl(\bigcup_nA_n\bigr)<\infty\), then \(\lambda^*\bigl(\bigcup_nA_n\bigr)=\lim_n\lambda^*A_n\).
3. For \(F\in\Sigma\), \(\lambda^*A=\lambda^*(A\cap F)+\lambda^*(A\setminus F)\).

*Proof.* (1) Choose \(E_n\in\Sigma\) containing \(A\) with \(\lambda E_n\to\lambda^*A\), and put \(E=\bigcap_nE_n\); then \(\lambda E=\lambda^*A\). For \(F\in\Sigma\), \(\lambda(F\cap E)\ge\lambda^*(F\cap A)\) and \(\lambda(E\setminus F)\ge\lambda^*(A\setminus F)\), while the sum of the right sides is at least \(\lambda^*A=\lambda E\), the sum of the left sides. All terms are finite, so both inequalities are equalities.

(2) Let \(E_n\) be envelopes of \(A_n\) and \(E_n'=\bigcap_{m\ge n}E_m\). Then \(A_n\subseteq E_n'\subseteq E_n\), so \(\lambda E_n'=\lambda^*A_n\), and \(E_n'\) increases. Hence \(\lambda^*\bigl(\bigcup_nA_n\bigr)\le\lambda\bigl(\bigcup_nE_n'\bigr)=\lim_n\lambda^*A_n\le\lambda^*\bigl(\bigcup_nA_n\bigr)\).

(3) With an envelope \(E\) of \(A\), apply (1) to \(F\) and to its complement: \(\lambda^*(A\cap F)+\lambda^*(A\setminus F)=\lambda(E\cap F)+\lambda(E\setminus F)=\lambda E=\lambda^*A\). \(\square\)

**Lemma 1.2** (Support). Let \(\lambda\) be a Radon measure and \(Z\) the set of \(y\) with \(\lambda B(y,\delta)>0\) for every \(\delta>0\). Then \(Z\) is closed and \(\lambda(\mathbb R^r\setminus Z)=0\).

*Proof.* If \(\lambda B(y,\delta)=0\), then \(B(y',\delta/2)\subseteq B(y,\delta)\) for \(\|y'-y\|<\delta/2\), so the complement of \(Z\) is open. For such \(y\), choose \(q\in\mathbb Q^r\) with \(\|q-y\|<\delta/4\) and a rational \(s\in(\delta/4,\delta/2)\). Then \(y\in B(q,s)\subseteq B(y,\delta)\), so \(\lambda B(q,s)=0\). The complement of \(Z\) is therefore covered by countably many null balls. \(\square\)

**Lemma 1.3** (Measures from the Riesz theorem). Let \(\mu\) be a measure on the Borel sets of \(\mathbb R^r\) that is finite on compact sets and outer regular: \(\mu E=\inf\{\mu G:G\supseteq E\text{ open}\}\) for every Borel \(E\). Then the completion of \(\mu\) is a Radon measure.

*Proof.* The completion is complete, defined on open sets and finite on bounded sets. Let \(E\) be Borel with \(E\subseteq K=B(0,m)\), and \(\varepsilon>0\). Outer regularity gives an open \(U\supseteq K\setminus E\) with \(\mu U\le\mu(K\setminus E)+\varepsilon\). Then \(C=K\setminus U\) is compact, \(C\subseteq E\), and \(E\setminus C=E\cap U\subseteq U\setminus(K\setminus E)\) has measure at most \(\varepsilon\). For a general Borel set \(E\), \(\mu E=\lim_m\mu(E\cap B(0,m))\), so \(E\) is inner regular too. A set of the completion differs from a Borel set \(E_0\subseteq E\) by a null set, and has the same inner approximations. \(\square\)

## 2. The covering lemma

Fix \(\varepsilon>0\) with
\[
(5^r+1)(1-\varepsilon-\varepsilon^2)^r>(5+\varepsilon)^r ;
\tag{2.1}
\]
it exists because the left side tends to \(5^r+1\) and the right side to \(5^r\) as \(\varepsilon\to0\).

**Lemma 2.1.** Let \(x_0,\dots,x_n\in\mathbb R^r\) and \(\delta_0,\dots,\delta_n>0\) satisfy
\[
\|x_i-x_j\|>\delta_i\quad\text{and}\quad\delta_j\le(1+\varepsilon)\delta_i\qquad\text{whenever }i<j\le n .
\]
Then at most \(5^r\) indices \(i\le n\) satisfy \(\|x_i-x_n\|\le\delta_i+\delta_n\).

*Proof.* Replacing every \(x_i\) by \(x_i/\delta_n\) and every \(\delta_i\) by \(\delta_i/\delta_n\) changes neither the hypotheses nor the conclusion, so let \(\delta_n=1\). Then \(\delta_i\ge1/(1+\varepsilon)\) for all \(i\). Let \(I\) be the set of the indices in question; for \(i\in I\), \(\|x_i-x_n\|\le\delta_i+1\), and \(\|x_i-x_n\|>\delta_i\) if \(i<n\). For \(i\in I\) put \(x_i'=x_i\) if \(\|x_i-x_n\|\le2+\varepsilon\), and otherwise let \(x_i'\) be the point of the segment from \(x_n\) to \(x_i\) at distance \(2+\varepsilon\) from \(x_n\). In the second case \(\|x_i-x_i'\|=\|x_i-x_n\|-(2+\varepsilon)\).

*Claim: \(\|x_i'-x_j'\|\ge1-\varepsilon-\varepsilon^2\) for distinct \(i<j\) in \(I\).* Write \(d_k=\|x_k-x_n\|\).

- If \(d_i,d_j\le2+\varepsilon\): \(\|x_i'-x_j'\|=\|x_i-x_j\|>\delta_i\ge\frac1{1+\varepsilon}\ge1-\varepsilon\).
- If \(d_j\le2+\varepsilon<d_i\): \(\|x_i'-x_j'\|\ge\|x_i-x_j\|-\|x_i-x_i'\|>\delta_i-d_i+2+\varepsilon\ge\delta_i-(\delta_i+1)+2+\varepsilon=1+\varepsilon\).
- If \(d_i\le2+\varepsilon<d_j\) (so \(j\ne n\)): \(\|x_i'-x_j'\|\ge\|x_i-x_j\|-\|x_j-x_j'\|>\delta_i-(\delta_j+1)+2+\varepsilon\ge\delta_i-(1+\varepsilon)\delta_i+1+\varepsilon=1+\varepsilon-\varepsilon\delta_i\), and \(\delta_i<d_i\le2+\varepsilon\) (here \(i<n\)), so this is at least \(1-\varepsilon-\varepsilon^2\).
- If \(2+\varepsilon<d_j\le d_i\): let \(y\) be the point of the segment from \(x_n\) to \(x_i\) with \(\|y-x_n\|=d_j\). Then \(\|y-x_j\|\ge\|x_i-x_j\|-\|x_i-y\|>\delta_i-(d_i-d_j)\ge d_j-1\). The dilation with centre \(x_n\) and ratio \((2+\varepsilon)/d_j\) sends \(y\) to \(x_i'\) and \(x_j\) to \(x_j'\), so \(\|x_i'-x_j'\|=\frac{2+\varepsilon}{d_j}\|y-x_j\|\ge(2+\varepsilon)\bigl(1-\frac1{d_j}\bigr)\ge1+\varepsilon\).
- If \(2+\varepsilon<d_i\le d_j\): let \(y\) be the point of the segment from \(x_n\) to \(x_j\) with \(\|y-x_n\|=d_i\). Then \(\|y-x_i\|\ge\|x_i-x_j\|-(d_j-d_i)>\delta_i-(\delta_j+1)+d_i\ge d_i-1-\varepsilon\delta_i\ge d_i(1-\varepsilon)-1\), using \(\delta_j\le(1+\varepsilon)\delta_i\) and \(\delta_i<d_i\). Dilating as before, \(\|x_i'-x_j'\|=\frac{2+\varepsilon}{d_i}\|y-x_i\|\ge(2+\varepsilon)(1-\varepsilon)-\frac{2+\varepsilon}{d_i}\ge(2+\varepsilon)(1-\varepsilon)-1=1-\varepsilon-\varepsilon^2\).

*Counting.* Put \(\rho=\frac12(1-\varepsilon-\varepsilon^2)\). By the claim the open balls \(U_i=\{z:\|z-x_i'\|<\rho\}\), \(i\in I\), are disjoint. Each contains \(B(x_i',\rho')\) for every \(\rho'<\rho\), so \(\mathcal LU_i\ge\beta_r\rho^r\). Since \(\|x_i'-x_n\|\le2+\varepsilon\) and \(\rho\le\frac12(1-\varepsilon)\), they lie in \(B\bigl(x_n,2+\varepsilon+\frac12(1-\varepsilon)\bigr)=B\bigl(x_n,\frac12(5+\varepsilon)\bigr)\). Comparing measures, \(\#I\,(1-\varepsilon-\varepsilon^2)^r\le(5+\varepsilon)^r\), and (2.1) gives \(\#I<5^r+1\). \(\square\)

## 3. Besicovitch's covering theorem

**Theorem 3.1.** Let \(A\subseteq\mathbb R^r\) be bounded and \(\mathcal I\) a family of balls such that every point of \(A\) is the centre of a member of \(\mathcal I\). Then there are \(5^r\) countable disjoint subfamilies \(\mathcal I_0,\dots,\mathcal I_{5^r-1}\) of \(\mathcal I\) whose union covers \(A\).

*Proof.* For \(x\in A\) choose \(\delta_x\) with \(B(x,\delta_x)\in\mathcal I\). If \(A\) is empty there is nothing to prove. If \(\sup_{x\in A}\delta_x=\infty\), one ball \(B(x,\delta_x)\) with \(\delta_x\ge\operatorname{diam}A\) covers \(A\). So let the radii be bounded; then \(C=\bigcup_{x\in A}B(x,\delta_x)\) is bounded.

*Selection.* Choose balls \(B_0,B_1,\dots\), some possibly empty, as follows. If \(A\subseteq\bigcup_{i<n}B_i\), put \(B_n=\emptyset\). Otherwise let \(\alpha_n=\sup\{\delta_x:x\in A\setminus\bigcup_{i<n}B_i\}\), choose \(x_n\in A\setminus\bigcup_{i<n}B_i\) with \((1+\varepsilon)\delta_{x_n}\ge\alpha_n\), and put \(B_n=B(x_n,\delta_{x_n})\). If \(B_n\neq\emptyset\), then for \(i<j\le n\) we have \(x_j\notin B_i\), that is \(\|x_i-x_j\|>\delta_{x_i}\), and \(\delta_{x_j}\le\alpha_i\le(1+\varepsilon)\delta_{x_i}\). Two balls \(B_i\), \(B_n\) meet exactly when \(\|x_i-x_n\|\le\delta_{x_i}+\delta_{x_n}\). By Lemma 2.1, the set \(I_n\) of the \(i<n\) with \(B_i\cap B_n\neq\emptyset\) has fewer than \(5^r\) elements.

*Colouring.* Define \(f(n)\) inductively as the least \(k<5^r\) that differs from \(f(i)\) for all \(i\in I_n\), and let \(\mathcal I_k\) consist of the non-empty \(B_n\) with \(f(n)=k\). If \(i<n\) and \(f(i)=f(n)\), then \(i\notin I_n\), so \(B_i\cap B_n=\emptyset\): each \(\mathcal I_k\) is disjoint.

*Covering.* The balls of one \(\mathcal I_k\) are disjoint and lie in the bounded set \(C\), so \(\sum_n\mathcal LB_n\le5^r\mathcal L^*C<\infty\). If some \(x\in A\) lay in no \(B_n\), every \(\alpha_n\) would be defined and at least \(\delta_x\), every \(B_n\) would have radius at least \(\delta_x/(1+\varepsilon)\), and \(\sum_n\mathcal LB_n\) would diverge. \(\square\)

## 4. Disjoint covers up to a null set

**Theorem 4.1.** Let \(\lambda\) be a Radon measure on \(\mathbb R^r\), \(A\subseteq\mathbb R^r\), and \(\mathcal I\) a family of balls such that every point of \(A\) is the centre of arbitrarily small members of \(\mathcal I\). Then there is a countable disjoint \(\mathcal I_0\subseteq\mathcal I\) with \(\lambda^*\bigl(A\setminus\bigcup\mathcal I_0\bigr)=0\).

*Proof.* *Step 1.* If \(A'\subseteq A\) is bounded, there is a finite disjoint \(\mathcal J\subseteq\mathcal I\) with \(\lambda^*\bigl(A'\cap\bigcup\mathcal J\bigr)\ge6^{-r}\lambda^*A'\). Indeed, if \(\lambda^*A'=0\) take \(\mathcal J=\emptyset\). Otherwise Theorem 3.1 gives disjoint countable \(\mathcal J_k\), \(k<5^r\), covering \(A'\); since \(\lambda^*A'\le\sum_k\lambda^*(A'\cap\bigcup\mathcal J_k)\), some \(k\) has \(\lambda^*(A'\cap\bigcup\mathcal J_k)\ge5^{-r}\lambda^*A'\). Enumerate \(\mathcal J_k\) as \(B_0,B_1,\dots\). By Lemma 1.1(2), \(\lambda^*\bigl(A'\cap\bigcup_{i\le n}B_i\bigr)\) tends to \(\lambda^*(A'\cap\bigcup\mathcal J_k)\), which is finite, so it exceeds \(6^{-r}\lambda^*A'\) for some \(n\); take \(\mathcal J=\{B_0,\dots,B_n\}\).

*Step 2.* Fix a sequence \((m_n)\) of natural numbers in which every natural number occurs infinitely often. Put \(\mathcal K_0=\emptyset\). Given a finite disjoint \(\mathcal K_n\subseteq\mathcal I\), let \(\mathcal I'\) consist of the members of \(\mathcal I\) disjoint from the closed set \(\bigcup\mathcal K_n\), and \(A_n=A\cap B(0,m_n)\setminus\bigcup\mathcal K_n\). Every point of \(A_n\) is the centre of arbitrarily small members of \(\mathcal I'\). Step 1 gives a finite disjoint \(\mathcal J_n\subseteq\mathcal I'\) with \(\lambda^*(A_n\cap\bigcup\mathcal J_n)\ge6^{-r}\lambda^*A_n\); put \(\mathcal K_{n+1}=\mathcal K_n\cup\mathcal J_n\), again finite and disjoint. By Lemma 1.1(3), applied to the closed set \(\bigcup\mathcal J_n\),
\[
\lambda^*\Bigl(A\cap B(0,m_n)\setminus\bigcup\mathcal K_{n+1}\Bigr)=\lambda^*\Bigl(A_n\setminus\bigcup\mathcal J_n\Bigr)\le(1-6^{-r})\,\lambda^*A_n .
\]
For fixed \(m\), the numbers \(\lambda^*(A\cap B(0,m)\setminus\bigcup\mathcal K_n)\) decrease in \(n\), are finite, and are multiplied by at most \(1-6^{-r}\) at every \(n\) with \(m_n=m\); so they tend to \(0\). With \(\mathcal I_0=\bigcup_n\mathcal K_n\), which is countable and disjoint, \(\lambda^*(A\cap B(0,m)\setminus\bigcup\mathcal I_0)=0\) for every \(m\), and hence \(\lambda^*(A\setminus\bigcup\mathcal I_0)=0\). \(\square\)

## 5. The differentiation theorem

**Theorem 5.1** (Besicovitch). Let \(\lambda\) be a Radon measure on \(\mathbb R^r\) and \(f\) a locally \(\lambda\)-integrable complex function on \(\mathbb R^r\). For \(\lambda\)-almost every \(y\), \(\lambda B(y,\delta)>0\) for all \(\delta>0\) and
\[
\text{(a)}\ \lim_{\delta\downarrow0}\frac1{\lambda B(y,\delta)}\int_{B(y,\delta)}f\,d\lambda=f(y),\qquad
\text{(b)}\ \lim_{\delta\downarrow0}\frac1{\lambda B(y,\delta)}\int_{B(y,\delta)}|f(x)-f(y)|\,\lambda(dx)=0 .
\]

*Proof.* By Lemma 1.2 the support \(Z\) is conegligible, and at its points the averages are defined. It suffices to treat real \(f\).

(a) For \(n\in\mathbb N\) and rationals \(q<q'\) let \(A\) be the set of \(y\in Z\) with \(\|y\|<n\), \(f(y)\le q\) and \(\limsup_{\delta\downarrow0}\frac1{\lambda B(y,\delta)}\int_{B(y,\delta)}f\,d\lambda>q'\). We show \(\lambda^*A=0\). Let \(\varepsilon>0\). Since \(f\) is integrable on \(B(0,n)\), there is \(\eta\in(0,\varepsilon]\) with \(\int_F|f|\,d\lambda\le\varepsilon\) for measurable \(F\subseteq B(0,n)\) with \(\lambda F\le\eta\) ([Fremlin, Volume 2, 225A](https://www1.essex.ac.uk/maths/people/fremlin/chap22.pdf)). Let \(E\) be an envelope of \(A\) (Lemma 1.1(1)); replacing \(E\) by its intersection with the measurable set \(S=\{y\in Z:\|y\|<n,\ f(y)\le q\}\), which contains \(A\), we keep an envelope and get \(f\le q\) on \(E\). Choose an open \(G\) with \(E\subseteq G\subseteq\{\|y\|<n\}\) and \(\lambda(G\setminus E)\le\eta\). Let \(\mathcal I\) be the family of balls \(B\subseteq G\) with \(\int_Bf\,d\lambda\ge q'\lambda B\). Every point of \(A\) is the centre of arbitrarily small members of \(\mathcal I\), so Theorem 4.1 gives a countable disjoint \(\mathcal I_0\subseteq\mathcal I\) with \(\lambda^*(A\setminus\bigcup\mathcal I_0)=0\). Let \(V=\bigcup\mathcal I_0\subseteq G\). By the envelope property \(\lambda(E\setminus V)=\lambda^*(A\setminus V)=0\), and \(\lambda(V\setminus E)\le\eta\). Hence \(|\lambda V-\lambda E|\le\varepsilon\), and
\[
q'\lambda E\le q'\lambda V+|q'|\varepsilon=\sum_{B\in\mathcal I_0}q'\lambda B+|q'|\varepsilon\le\int_Vf\,d\lambda+|q'|\varepsilon\le\int_Ef\,d\lambda+\varepsilon+|q'|\varepsilon\le q\lambda E+(1+|q'|)\varepsilon .
\]
So \((q'-q)\lambda^*A=(q'-q)\lambda E\le(1+|q'|)\varepsilon\) for every \(\varepsilon\), and \(\lambda^*A=0\). Taking the union over \(n\), \(q\), \(q'\): for almost every \(y\), the \(\limsup\) of the averages is at most \(f(y)\). Applying this to \(-f\), the \(\liminf\) is at least \(f(y)\) almost everywhere.

(b) Apply (a) to the functions \(|f-q|\), \(q\in\mathbb Q\), to get a conegligible set \(D\) on which all their averages converge. For \(y\in D\) and \(\varepsilon>0\) choose \(q\) with \(|f(y)-q|\le\varepsilon\); for small \(\delta\) the average of \(|f-q|\) over \(B(y,\delta)\) is at most \(|f(y)-q|+\varepsilon\le2\varepsilon\), and the average of \(|f-f(y)|\) is at most that plus \(|q-f(y)|\), hence at most \(3\varepsilon\). \(\square\)

**Corollary 5.2** (Density theorem). Let \(\lambda\) be a Radon measure on \(\mathbb R^r\) and \(K\in\Sigma\). For \(\lambda\)-almost every \(y\in K\), \(\lambda(K\cap B(y,\delta))/\lambda B(y,\delta)\to1\), and for \(\lambda\)-almost every \(y\notin K\) it tends to \(0\), as \(\delta\downarrow0\).

*Proof.* Theorem 5.1(a) with \(f=1_K\). \(\square\)

## 6. Exercises

**Exercise 6.1.** Show that one disjoint subfamily does not always suffice in Theorem 3.1: take \(r=1\), \(A=\{0,1,2\}\) and the balls \([-\tfrac32,\tfrac32]\), \([0.9,1.1]\) and \([\tfrac12,\tfrac72]\).

*Solution.* The first ball is the only one containing \(0\), and the third the only one containing \(2\). Any subfamily covering \(A\) contains both, and they meet.

**Exercise 6.2.** (a) Let \(\lambda\) be the Dirac measure at \(0\) on \(\mathbb R^r\), defined on all subsets. Check Theorem 5.1 directly. (b) On \(\mathbb R\) let \(\lambda E=\sum\{1/k!:k\ge1,\ 1/k\in E\}\) for all \(E\subseteq\mathbb R\). Show that \(\lambda\) is a Radon measure and that, for \(k\ge4\), \(y=1/k\) and \(\delta=1/(2k(k-1))\), one has \(\lambda B(y,2\delta)\ge k\,\lambda B(y,\delta)\). So no bound \(\lambda B(y,2\delta)\le C\lambda B(y,\delta)\) holds at the points of the support, and Theorem 5.1 is needed.

*Solution.* (a) The support is \(\{0\}\), and every average at \(0\) equals \(f(0)\). (b) Every subset is measurable, so \(\lambda\) is complete and defined on open sets; the total mass is finite; and \(\lambda E\) is the supremum of \(\lambda\) over the finite, hence compact, subsets of \(E\cap\{1/k:k\ge1\}\). The atoms nearest to \(1/k\) are at distances \(\frac1{k(k+1)}\) and \(\frac1{k(k-1)}\). For \(k\ge4\), \(\delta=\frac1{2k(k-1)}<\frac1{k(k+1)}\), so \(B(y,\delta)\) contains only the atom \(1/k\), of mass \(1/k!\), while \(B(y,2\delta)\) contains \(1/(k-1)\), of mass \(1/(k-1)!=k/k!\).

## Where this leads

The lesson [Vector-valued functions, tensor products with \(L^p\), and preduals](vector-valued-functions-tensor-products-with-lp-and-preduals.md) uses Theorem 5.1 and Corollary 5.2 to construct selectors for every Radon measure on \(\mathbb R^n\) (the remark after its Proposition 3.4). The maximal inequality for Radon measures on \(\mathbb R^r\) is in [Fremlin, Volume 4, 472E–472F].

## References

- [Fremlin] D. H. Fremlin, *Measure Theory*, Volumes 1, 2 and 4, Torres Fremlin, Colchester, 2000–2003; [author's site](https://www1.essex.ac.uk/maths/people/fremlin/mt.htm), free, under the Design Science License. Volume 4, Section 472, is in [Chapter 47](https://www1.essex.ac.uk/maths/people/fremlin/chap47.pdf).
