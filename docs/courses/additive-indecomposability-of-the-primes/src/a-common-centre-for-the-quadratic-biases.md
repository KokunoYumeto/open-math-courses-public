# A common centre for the quadratic biases

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The translates \(t_p\) chosen in Lesson 3 were arbitrary, one residue at each prime of the block \(\mathcal P\). This lesson proves that a large subset \(\mathcal P_0\subseteq\mathcal P\) shares a single rational centre: there are integers \(h\) and \(m\ge1\), with \(m\) tiny and \(|h|\) not much larger than \(X\), such that \(t_p\equiv h/m\pmod p\) for every \(p\in\mathcal P_0\) (Proposition 4.2). The route has three steps. On the event \(\mathcal E\) of Lesson 4, one quadratic exponential sum is large, and an inverse theorem for quadratic Weyl sums turns this into a rational approximation to \(\theta=t_M/M\) (Lemma 1.1 and Proposition 2.1). Clearing denominators gives an integer \(n\), not much larger than \(X\), with \(n\equiv at_p\pmod p\) for all \(p\mid M\). Counting such integers over many tuples then shows that one of them fits a large set of primes.

**Prerequisites.** [*Hypercontractive moments and a small-kernel witness*](hypercontractive-moments-and-a-small-kernel-witness.md), Sections 5 and 6.

The notation of Lessons 3 and 4 is in force.

## 1. An inverse theorem for quadratic Weyl sums

For real \(x\), \(\|x\|\) denotes the distance from \(x\) to the nearest integer.

**Lemma 1.1.** Let \(c_1\in(0,1]\). There is \(K_1=K_1(c_1)\) with the following property. Let \(K\ge K_1\) and \(Y\ge2\) satisfy
\[
Y\ge e^{4K},\qquad\log(2Y)\le e^K,
\]
let \(I\) be an interval of at most \(Y/c_1\) integers, and let \(\alpha,\beta\) be real with
\[
\Bigl|\sum_{j\in I}e(\alpha j^2+\beta j)\Bigr|\ge c_1Ye^{-K}.
\]
Then there is an integer \(q\) with \(1\le q\le2e^{8K}\) and \(\|q\alpha\|\le2e^{8K}Y^{-2}\).

*Proof.* *A rational approximation.* Put \(Q_1=\lfloor Y^2e^{-8K}\rfloor\ge1\). By Dirichlet's theorem there is an integer \(1\le r\le Q_1\) with \(\|2r\alpha\|\le1/Q_1\); let \(b\) be the integer nearest to \(2r\alpha\). Dividing \(b\) and \(r\) by their greatest common divisor keeps \(r\le Q_1\) and \(|2r\alpha-b|\le1/Q_1\), so we may assume \((b,r)=1\). Then \(|2\alpha-b/r|\le1/(rQ_1)\le1/r^2\).

*Differencing.* Write \(S=\sum_{j\in I}e(\alpha j^2+\beta j)\) and \(H=|I|\le Y/c_1\). Expanding \(|S|^2\) and putting \(j=j'+h\),
\[
|S|^2=\sum_{|h|<H}e(\alpha h^2+\beta h)\sum_{\substack{j'\in I\\j'+h\in I}}e(2\alpha hj'),
\]
so, by the geometric-sum bound \(|\sum_{j'\in J'}e(\gamma j')|\le\min(|J'|,1/(2\|\gamma\|))\),
\[
\begin{aligned}
|S|^2&\le H+2\sum_{1\le h<H}\min\Bigl(H,\\
&\quad \frac1{\|2h\alpha\|}\Bigr).\quad(1.1)
\end{aligned}
\]
The linear coefficient \(\beta\) and the position of \(I\) do not affect this bound.

*Counting near-integers.* Split \(1\le h<H\) into blocks of consecutive integers, each a single integer or of length less than \(r/2\); with blocks of length \(\max(1,\lceil r/2\rceil-1)\ge r/4\) there are at most \(4H/r+1\) of them. If \(h\ne h'\) lie in one block, then \(0<|h-h'|<r/2<r\), so \(r\nmid(h-h')b\) and \(\|(h-h')b/r\|\ge1/r\), while \(|(h-h')(2\alpha-b/r)|\le\frac r2\cdot\frac1{r^2}=\frac1{2r}\). Hence the numbers \(2h\alpha\) in one block are \(\frac1{2r}\)-separated modulo \(1\). For \(i\ge1\), the open arc of length \(i/(2r)\) centred at \(0\) contains at most \(i\) points of a \(\frac1{2r}\)-separated set; so if the points of a block are ordered by their distance to \(0\), the \((i+1)\)-th has distance at least \(i/(4r)\). Each block has fewer than \(r\) points, so it contributes at most \(H+\sum_{i<r}4r/i\le H+4r(1+\log r)\) to the sum in (1.1). Therefore
\[
\begin{aligned}
|S|^2&\le H+2\Bigl(\frac{4H}r+1\Bigr)\bigl(H\\
&\quad +4r(1+\log r)\bigr).\quad(1.2)
\end{aligned}
\]

*Small denominator.* Suppose \(r>e^{8K}\). Then \(H/r\le Y/(c_1e^{8K})\), \(r\le Q_1\le Y^2e^{-8K}\), and \(1+\log r\le3\log(2Y)\le3e^K\). Expanding (1.2), every term is at most a constant depending on \(c_1\) times \(Y^2e^{-7K}\) or \(Ye^{K}\), and \(Ye^K\le Y^2e^{-3K}\) because \(Y\ge e^{4K}\). So \(|S|^2\le C(c_1)Y^2e^{-3K}\), which contradicts \(|S|^2\ge c_1^2Y^2e^{-2K}\) once \(e^K>C(c_1)/c_1^2\). Hence \(r\le e^{8K}\) for \(K\ge K_1(c_1)\). Take \(q=2r\le2e^{8K}\). Then \(\|q\alpha\|\le|2r\alpha-b|\le1/Q_1\le2e^{8K}Y^{-2}\), using \(Q_1\ge\frac12Y^2e^{-8K}\). \(\square\)

The conclusion is necessary up to the size of the losses: if \(\alpha=b/q\) with small \(q\), the sum over a long interval is of size about \(Y/\sqrt q\) for suitable \(\beta\) (Exercise 6.1).

## 2. From the witness to an integer lift

Fix a tuple in the event \(\mathcal E\) of Lesson 4, and a witness: \(s\in\mathcal S\) with \(s<\mathcal L^4\) and \(v,d\mid\mathcal L\) with
\[
|G_d(s,v)|\ge2^{\omega(d)/2}e^{-K}.
\]
Put \(Y_0=N_{dsv}/d\). By (5.1) of Lesson 4, \(Y_0\ge Z^{4.9}\); also \(Y_0\le\sqrt R\le Z^{7}\), so \(\log Y_0\asymp\log Z\asymp T\).

**Proposition 2.1** ([OpenAI-013, (3.23) and (3.24)]). For large \(T\), there are integers \(a\) and \(n\) with
\[
\begin{gathered}
1\le a\le Z^{0.12+o(1)},\\
|n|\le XZ^{0.12+o(1)},\\
n\equiv at_p\pmod p\\
\text{for every }p\mid M.\quad(2.1)
\end{gathered}
\]

*Proof.* *Splitting into progressions.* In the definition (6.1) of Lesson 3 of \(G_d(s,v)=G_d^{(1)}(s,v)\), write \(w=x+dj\) with \(x\) running over a residue system modulo \(d\). The factor \(g_d(-svw^2\overline M)\) and the phase \(e(h_0svw^2/d)\) depend only on \(x\). The remaining phase is
\[
\begin{gathered}
\begin{aligned}
&e\Bigl(\frac{\theta sv(x+dj)^2}d\Bigr)\\
&\quad =e\Bigl(\frac{\theta svx^2}d\Bigr)\,e(\alpha j^2+\beta_xj),
\end{aligned}\\
\alpha=svd\,\theta,\\
\beta_x=2\theta svx,
\end{gathered}
\]
and, because \(Y_0^2=R/(svd)\), the smooth factor is
\[
\widehat\psi\Bigl(\frac{sv(x+dj)^2}{Rd}\Bigr)=\widehat\psi\Bigl(\Bigl(\frac{j+x/d}{Y_0}\Bigr)^2\Bigr).
\]
As in the proof of Lemma 5.1 of Lesson 4, \(\sum_{x\bmod d}|g_d(-svx^2\overline M)|\le d\,2^{\omega(d)/2}\). Since \(N_{dsv}=dY_0\), the witness inequality forces some \(x\) with
\[
\begin{aligned}
&\Bigl|\sum_je(\alpha j^2+\beta_xj)\\
&\qquad \,\widehat\psi\Bigl(\Bigl(\frac{j+x/d}{Y_0}\Bigr)^2\Bigr)\Bigr|\ge Y_0e^{-K}.
\end{aligned}
\]
The weight vanishes unless \(|j+x/d|\le Y_0/2\), and as a function of \(j\) it has supremum and total variation bounded in terms of \(\widehat\psi\) alone. By partial summation there is an interval \(I\) of at most \(Y_0+1\) integers with \(|\sum_{j\in I}e(\alpha j^2+\beta_xj)|\ge c_1Y_0e^{-K}\), where \(c_1>0\) depends only on \(\widehat\psi\).

*Approximation.* By (2.2) of Lesson 3, \(K\asymp T^{1-\gamma}\), so \(Y_0\ge Z^{4.9}\ge e^{4K}\) and \(\log(2Y_0)\ll T\le e^K\) for large \(T\). Lemma 1.1 gives \(1\le q\le2e^{8K}\) with
\[
\|q\alpha\|\le2e^{8K}Y_0^{-2}=2e^{8K}\frac{svd}R.
\]

*The lift.* Put \(a=qsvd\). Then \(1\le a\le2e^{8K}\mathcal L^6\le Z^{0.12+o(1)}\), since \(e^{O(K)}=Z^{o(1)}\) and \(\mathcal L\le Z^{0.02}\). Let \(b'\) be the integer nearest to \(a\theta=q\alpha\) and put \(n=at_M-b'M\). Then \(n\equiv at_M\equiv at_p\pmod p\) for \(p\mid M\), and
\[
\begin{aligned}
|n|&=M\,\|q\alpha\|\le2e^{8K}\,svd\,\frac MR\\
&=2e^{8K}svd\,X\\
&\le XZ^{0.12+o(1)}.
\end{aligned}
\]
\(\square\)

**Fixing the multiplier.** There are at most \(Z^{0.12+o(1)}\) possible values of \(a\). By Proposition 6.1 of Lesson 4, at least \(e^{-O(K)}(J)_k\) ordered tuples lie in \(\mathcal E\), and \((J)_k=(1-o(1))J^k\), \(e^{O(K)}=Z^{o(1)}\). Choosing one lift for each such tuple and pigeonholing over \(a\):

**Corollary 2.2.** For large \(T\) there is a fixed integer \(1\le a\le Z^{0.12+o(1)}\) such that at least \(J^kZ^{-0.13}\) ordered tuples of distinct primes of \(\mathcal P\) admit an integer \(n\) with \(|n|\le XZ^{0.12+o(1)}\) and \(n\equiv at_p\pmod p\) for all primes \(p\) of the tuple. \(\square\)

## 3. Counting lifts

Fix \(a\) as in Corollary 2.2 and put \(H_0=XZ^{0.15}\). Since \(X\le Z^{k-10}\), \(H_0\le Z^{k-9.85}\). For integers \(|n|\le H_0\) let
\[
\begin{gathered}
\mathcal P_n=\{p\in\mathcal P:n\equiv at_p\pmod p\},\\
r(n)=|\mathcal P_n|,
\end{gathered}
\]
and write \((x)_j=x(x-1)\cdots(x-j+1)\).

**Lemma 3.1.** For large \(T\),
\[
\begin{gathered}
\sum_{|n|\le H_0}(r(n))_k\ge J^kZ^{-0.13},\\
\sum_{|n|\le H_0}(r(n))_{k-10}\ll Z^{0.15}J^{k-10}.\quad(3.1)
\end{gathered}
\]

*Proof.* The number \((r(n))_k\) counts the ordered \(k\)-tuples of distinct primes of \(\mathcal P_n\). Each tuple of Corollary 2.2 is such a tuple for its lift \(n\), and \(|n|\le H_0\); this gives the first bound. For the second, exchange the order of counting: for an ordered \((k-10)\)-tuple of distinct primes of \(\mathcal P\), the congruences \(n\equiv at_p\pmod p\) fix \(n\) modulo the product of the tuple, which is at least \(Z^{k-10}\). So at most \(2H_0/Z^{k-10}+1\le3Z^{0.15}\) integers \(|n|\le H_0\) fit the tuple, and there are at most \(J^{k-10}\) tuples. \(\square\)

**Low multiplicities are negligible.** If \(r(n)<Z^{0.6}\), then \((r(n))_k\le r(n)^{10}(r(n))_{k-10}\)\(\le Z^6(r(n))_{k-10}\). By (3.1) these \(n\) contribute \(O(Z^{6.15}J^{k-10})\) to the first sum, which is \(o(J^kZ^{-0.13})\) because \(J^{10}\gg(Z/\log Z)^{10}\). Call \(n\) *high* if \(r(n)\ge Z^{0.6}\).

## 4. One centre for many primes

**Lemma 4.1.** Two different integers \(n\ne n'\) with \(|n|,|n'|\le H_0\) satisfy \(|\mathcal P_n\cap\mathcal P_{n'}|\le k\).

*Proof.* A prime \(p\) in both sets satisfies \(n\equiv at_p\equiv n'\pmod p\), so \(p\mid n-n'\). The product of \(k+1\) such primes is at least \(Z^{k+1}\), whereas \(0<|n-n'|\le2H_0<Z^{k+1}\). \(\square\)

**Proposition 4.2** (a common centre [OpenAI-013, (3.27)]). For large \(T\) there are a set \(\mathcal P_0\subseteq\mathcal P\) and integers \(h,m\) with \(m\ge1\) and \((h,m)=1\) such that
\[
\begin{gathered}
J_0:=|\mathcal P_0|\ge JZ^{-O(1/k)},\\
t_p\equiv h\,\overline m\pmod p\quad(p\in\mathcal P_0),\\
m\le Z^{0.13}=X^{o(1)},\\
|h|\le XZ^{0.15}.\quad(4.1)
\end{gathered}
\]

*Proof.* *The total size of the high sets.* Let \(b\) be the number of high \(n\), \(R_0=\sum_{n\ \mathrm{high}}r(n)\), and for \(p\in\mathcal P\) let \(d_p\) be the number of high \(n\) with \(p\in\mathcal P_n\). Then \(\sum_pd_p=R_0\), and by Lemma 4.1
\[
\sum_pd_p^2=\sum_{n,n'\ \mathrm{high}}|\mathcal P_n\cap\mathcal P_{n'}|\le R_0+kb^2 .
\]
By Cauchy–Schwarz, \(R_0^2\le J\sum_pd_p^2\le JR_0+kJb^2\). Since \(b\le R_0/Z^{0.6}\), this gives \(R_0\bigl(1-kJZ^{-1.2}\bigr)\le J\), and \(kJZ^{-1.2}=o(1)\) because \(J\le2Z\). So \(R_0\le2J\) for large \(T\).

*A large set.* Let \(J_0\) be the largest \(r(n)\) over high \(n\). By Lemma 3.1 and the preceding paragraph,
\[
\begin{aligned}
\tfrac12J^kZ^{-0.13}&\le\sum_{n\ \mathrm{high}}(r(n))_k\\
&\le J_0^{k-1}\sum_{n\ \mathrm{high}}r(n)\\
&\le2J\,J_0^{k-1},
\end{aligned}
\]
so \(J_0^{k-1}\ge\frac14J^{k-1}Z^{-0.13}\) and \(J_0\ge JZ^{-O(1/k)}\). Let \(n\) attain the maximum and \(\mathcal P_0=\mathcal P_n\).

*The centre.* Write \(n/a=h/m\) in lowest terms with \(m\ge1\). Then \(m\mid a\), so \(m\le a\le Z^{0.13}\), and \(|h|\le|n|\le H_0\). Every \(p\in\mathcal P_0\) satisfies \(p\ge Z>a\), so \(p\nmid a\) and \(p\nmid m\). From \(nm=ah\) and \(n\equiv at_p\pmod p\) we get \(ah\equiv at_pm\pmod p\), and dividing by \(a\), \(h\equiv t_pm\pmod p\). Finally \(\log Z/\log X\asymp T^{-0.6}\), so \(Z^{0.13}=X^{o(1)}\). \(\square\)

This is the first point at which the initially unrelated translates are tied together. The quadratic characters \(\chi_p(x-t_p)\), \(p\in\mathcal P_0\), all become \(\chi_p(m)\chi_p(mx-h)\): the bias of Lemma 2.1 of Lesson 3 is a bias of the single integer sequence \(mx-h\), \(x\in A_X\), against many quadratic characters at once. Lesson 6 shows that this forces the numbers \(mx-h\) to have few squarefree parts, and derives a contradiction.

## 5. Why a common centre is needed

If the translates were known in advance to be reductions of one integer, \(t_p\equiv t\pmod p\), the bias of Lemma 2.1 of Lesson 3 would directly be a statement about the integers \(x-t\), and Proposition 4.2 would be empty. The difficulty is that the residue supports \(S_p\) are chosen independently at each prime, so the maximizing translates have no a priori relation. The amplified moment over products of \(k\) primes, the Poisson dual, and Lemma 1.1 extract the relation from the size of a moment alone. The cost is the loss \(Z^{-O(1/k)}\) in the size of \(\mathcal P_0\), which is harmless because \(k\) tends to infinity.

## 6. Exercises

**6.1.** Let \(q\ge3\) be an odd prime and \(Y\) a multiple of \(q\). Show that \(\bigl|\sum_{j=1}^{Y}e(j^2/q)\bigr|=Y/\sqrt q\), and compare with Lemma 1.1.

**6.2.** Let \(\mathcal Q_1,\dots,\mathcal Q_b\) be subsets of a set of \(J\) elements, each of size at least \(t\), with \(|\mathcal Q_i\cap\mathcal Q_j|\le k\) for \(i\ne j\). Show that \(\sum_i|\mathcal Q_i|\le2J\) whenever \(t^2\ge2kJ\).

**6.3.** In the proof of Lemma 1.1, show that for \(i\ge1\) an open arc of length \(i/(2r)\) contains at most \(i\) points of a \(\frac1{2r}\)-separated subset of \(\mathbb R/\mathbb Z\), and deduce that the \((i+1)\)-th point in order of distance to \(0\) has distance at least \(i/(4r)\).

**6.4.** Suppose all translates satisfy \(t_p\equiv t\pmod p\) for one integer \(t\) with \(0\le t\le X\). Show that the conclusion of Proposition 2.1 holds with \(a=1\) and \(n=t\), for every tuple.

## 7. Solutions

**6.1.** The function \(j\mapsto e(j^2/q)\) has period \(q\), so the sum is \(Y/q\) times the quadratic Gauss sum \(\sum_{j\bmod q}e(j^2/q)\), whose modulus is \(\sqrt q\) ([*Gauss sums*](course:NT-DIRL/NT-DIRL-03)). With \(\alpha=1/q\), \(\|q\alpha\|=0\): the lemma's conclusion holds with \(q\) itself, and the sum has size \(Ye^{-K}\) for \(e^K=\sqrt q\). So a denominator of size \(e^{2K}\) can occur, and the lemma's bound \(e^{8K}\) is of the right form.

**6.2.** Let \(d_x\) be the number of sets containing \(x\), and \(R_0=\sum_i|\mathcal Q_i|=\sum_xd_x\). Cauchy–Schwarz gives \(R_0^2\le J\sum_xd_x^2\)\(=J\sum_{i,j}|\mathcal Q_i\cap\mathcal Q_j|\)\(\le J(R_0+kb^2)\). Since \(b\le R_0/t\), \(R_0^2(1-kJ/t^2)\le JR_0\), so \(R_0\le J/(1-kJ/t^2)\le2J\).

**6.3.** If \(i+1\) points of the set lay in an open arc of length \(i/(2r)\), two consecutive ones among them would be closer than \(\frac1{2r}\), since \(i\) gaps of at least \(\frac1{2r}\) would span at least \(i/(2r)\). The points at distance less than \(i/(4r)\) from \(0\) form the intersection with the open arc of length \(i/(2r)\) centred at \(0\), so there are at most \(i\) of them, and the \((i+1)\)-th point in order of distance is at distance at least \(i/(4r)\).

**6.4.** With \(n=t\) and \(a=1\): \(n\equiv t\equiv t_p\pmod p\) for every \(p\), and \(|n|\le X\).

## Sources

- [OpenAI-013] OpenAI, *The additive indecomposability of the primes*, OpenAI Math Release preprint, 24 September 2026, Section 3: recovering a rational approximation from the witness, (3.23), the integer lift, and one common centre for many primes. https://github.com/openai/math/tree/main/preprints/the-additive-indecomposability-of-the-primes-September-24-2026
