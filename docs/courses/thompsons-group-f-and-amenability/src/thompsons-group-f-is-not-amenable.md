# Thompson's group F is not amenable

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Ross Geoghegan asked in 1979 whether Thompson's group \(F\) is amenable; the survey [Gu, Section 1] records the question and the work on it. OpenAI answered it in September 2026 [OpenAI-F]; the same release contains a Lean formalization of the theorem [OpenAI-Lean].

**Theorem 5.1** (OpenAI). Thompson's group \(F\) is not amenable.

An amenable countable group has finite sets whose translates by any prescribed finite set of elements almost coincide with the set itself (Følner sets). The proof exhibits one finite set \(S\subseteq F\) and a constant \(\eta_0>0\) such that every nonempty finite \(A\subseteq F\) has \(|hA\triangle A|\ge\eta_0|A|\) for some \(h\in S\) (Proposition 4.1). To do this it attaches to every dyadic partition of \([0,1]\) a *color*, a vector in the closed unit ball \(B\) of a Hilbert space, defined recursively by applying the map \(f:B\to B\) of [A Lipschitz map of the Hilbert ball that moves every point](a-lipschitz-map-of-the-hilbert-ball-that-moves-every-point.md), which moves every point by at least \(\frac12\), to the average of the colors of \(D\) rescaled sub-partitions. Group elements act on partitions, and the covariance of rescaled restrictions turns approximate invariance of \(A\) into approximate equality of averaged inner products of colors. Averaging over \(A\) then forces the colors to be nearly fixed by \(f\) on average, which \(f\) does not allow once \(D\) is large.

We use the following results.

- From [Thompson's group F and dyadic partitions](thompsons-group-f-and-dyadic-partitions.md): Proposition 1.3 (\(F\) is a countable group), Lemma 2.4 (normalized restrictions; in particular \((T_I)_J=T_{I\cdot J}\)), Lemma 3.1 (images of fine uniform partitions are dyadic partitions respecting any finite family of dyadic intervals), Lemma 4.1 (moving pairs of separated internal dyadic intervals), Lemma 4.2 (covariance) and formula (5.1) there. We keep its notation: dyadic intervals and partitions, \(T^{(n)}\), \(gT\), \(s_I\), \(I\cdot J\), \(T_I\), \(I<J\), internal intervals.
- From [A Lipschitz map of the Hilbert ball that moves every point](a-lipschitz-map-of-the-hilbert-ball-that-moves-every-point.md): Theorem 5.1.
- From [Means, Følner sets, and regular representations](course:OA-ERGODIC/reader/means-folner-sets-and-regular-representations#3-a-level-set-with-a-small-boundary): the definition of amenability in its Section 1 and its Theorem 3.1, that a countable discrete group is amenable exactly when it has a Følner sequence; Remark 1 in Section 5 also uses its Theorem 2.1.

## 1. Amenability and finite averages

Let \(\Gamma\) be a countable discrete group. A *mean* on \(\ell^\infty(\Gamma)\) is a positive linear functional \(m\) with \(m(1)=1\); it is *left invariant* if \(m(L_sf)=m(f)\) for all \(s\in\Gamma\) and \(f\in\ell^\infty(\Gamma)\), where \((L_sf)(t)=f(s^{-1}t)\). The group is *amenable* if a left invariant mean exists. A *Følner sequence* is a sequence of nonempty finite sets \(F_n\subseteq\Gamma\) with \(|sF_n\triangle F_n|/|F_n|\to0\) for every \(s\in\Gamma\); such sets go back to Følner [Fø]. Theorem 3.1 of the lesson on means and Følner sets says that \(\Gamma\) is amenable exactly when it has a Følner sequence. We use one direction, in the following form.

**Corollary 1.1.** If \(\Gamma\) is a countable amenable group, then for every finite \(S\subseteq\Gamma\) and every \(\varepsilon>0\) there is a nonempty finite \(A\subseteq\Gamma\) with \(|hA\triangle A|<\varepsilon|A|\) for all \(h\in S\).

**Proof.** Take a Følner sequence \((F_n)\). For each of the finitely many \(h\in S\) the ratio \(|hF_n\triangle F_n|/|F_n|\) tends to \(0\); choose \(n\) so large that all of them are below \(\varepsilon\), and put \(A=F_n\). \(\square\)

For a nonempty finite \(A\subseteq\Gamma\) and \(\psi:\Gamma\to\mathbb R\) write \(\mathbb E_A\psi=\frac1{|A|}\sum_{g\in A}\psi(g)\).

**Lemma 1.2** (finite translation). Let \(A\subseteq\Gamma\) be nonempty and finite, \(h\in\Gamma\), and \(\varphi:\Gamma\to[-1,1]\). Then
\[
\Bigl|\frac1{|A|}\sum_{g\in A}\varphi(hg)-\mathbb E_A\varphi\Bigr|\le\frac{|hA\triangle A|}{|A|}.
\]

**Proof.** \(\sum_{g\in A}\varphi(hg)=\sum_{k\in hA}\varphi(k)\). The terms with \(k\in hA\cap A\) cancel against those of \(\sum_{k\in A}\varphi(k)\), so the difference of the two sums is \(\sum_{k\in hA\setminus A}\varphi(k)-\sum_{k\in A\setminus hA}\varphi(k)\), of absolute value at most \(|hA\setminus A|+|A\setminus hA|=|hA\triangle A|\). \(\square\)

## 2. Colors of dyadic partitions

Let \(H=L^2([0,1];\mathbb R^2)\), with closed unit ball \(B\), and let \(f:B\to B\) be the map of Theorem 5.1 of the lesson on the Hilbert ball. Let \(L>0\) be a Lipschitz constant for \(f\) and \(\delta=\frac12\), so that
\[
\|f(x)-f(y)\|\le L\|x-y\|,\qquad\|f(x)-x\|\ge\delta\qquad(x,y\in B).\tag{2.1}
\]
Only these two properties of \(f\) and \(H\) are used below. Fix an integer \(D\ge2\) with
\[
D>\frac{4L^2}{\delta^2},\tag{2.2}
\]
and an integer \(r\) with \(2^r>2D\). For \(j=1,\dots,D\) let
\[
I_j=\bigl[(2j-1)2^{-r},\,2j\,2^{-r}\bigr].
\]
These are dyadic intervals of level \(r\), since \(0\le2j-1<2^r\); they are internal, since \(\min I_1=2^{-r}>0\) and \(\max I_D=2D\,2^{-r}<1\); and \(I_1<I_2<\dots<I_D\), with gaps of length \(2^{-r}\). We call them the *parent intervals*.

**Definition 2.1** (colors). For every dyadic partition \(T\) define \(p(T)\in B\) by recursion on the number of cells \(|T|\):
\[
p(T)=\begin{cases}\displaystyle f\Bigl(\frac1D\sum_{j=1}^Dp\bigl(T_{I_j}\bigr)\Bigr),&\text{if \(T\) respects every \(I_j\)},\\ 0,&\text{otherwise.}\end{cases}\tag{2.3}
\]

The recursion is well founded. Suppose \(p\) has been defined, with values in \(B\), on all dyadic partitions with fewer than \(N\) cells, and let \(|T|=N\). If \(T\) respects every \(I_j\), then each \(T_{I_j}\) is a dyadic partition with fewer than \(N\) cells, by Lemma 2.4(b) of the lesson on dyadic partitions, because \(I_j\neq[0,1]\). So the colors \(p(T_{I_j})\) are defined and lie in \(B\); their average lies in the convex set \(B\), \(f\) can be applied, and \(p(T)\in B\). In particular the one-cell partition \(T^{(0)}\) respects no internal interval and has color \(0\).

For the uniform partitions, formula (5.1) of the lesson on dyadic partitions gives \((T^{(n)})_{I_j}=T^{(n-r)}\) for \(n\ge r\), while \(T^{(n)}\) respects no \(I_j\) for \(n<r\). Hence \(p(T^{(n)})=f\bigl(p(T^{(n-r)})\bigr)\) for \(n\ge r\), and \(p(T^{(n)})=f^{\lfloor n/r\rfloor}(0)\) for all \(n\) (Exercise 6.1). In general the color of a partition records, through \(f\), how the partition looks inside the parents \(I_j\), inside the intervals \(I_j\cdot I_k\), and so on down.

## 3. Colors along the group

Let
\[
\mathcal I=\{I_i:1\le i\le D\}\cup\{I_i\cdot I_j:1\le i,j\le D\}.
\]
We call \(I_i\cdot I_j\) the *descendants* of \(I_i\). By Lemma 2.4(a) of the lesson on dyadic partitions they are dyadic intervals contained in \(I_i\), so every member of \(\mathcal I\) is internal. Call two intervals *separated* if one lies to the left of the other, \(I<J\) or \(J<I\).

**Lemma 3.1.** (a) \(I_i\) and \(I_k\) are separated for \(i\neq k\).

(b) \(I_i\cdot I_j\) and \(I_i\cdot I_{j'}\) are separated for \(j\neq j'\).

(c) \(I_i\cdot I_j\) and \(I_k\) are separated for \(k\neq i\) and every \(j\).

**Proof.** (a) holds by construction. (b) The chart \(s_{I_i}\) is increasing and affine with positive slope, so it carries separated intervals to separated intervals. (c) \(I_i\cdot I_j\subseteq I_i\), and \(I_i\) and \(I_k\) are separated. \(\square\)

The only pairs of distinct members of \(\mathcal I\) that are not separated are the pairs consisting of a parent and one of its own descendants.

Call a pair \((n,g)\in\mathbb Z_{\ge0}\times F\) *admissible* if \(gT^{(n)}\) is a dyadic partition that respects every member of \(\mathcal I\). For \(I\in\mathcal I\), \(n\ge0\) and \(g\in F\) put
\[
X^{(n)}_I(g)=\begin{cases}p\bigl((gT^{(n)})_I\bigr),&\text{if \((n,g)\) is admissible},\\ 0,&\text{otherwise.}\end{cases}
\]
Each \(X^{(n)}_I\) is a map \(F\to B\). By Lemma 3.1 of the lesson on dyadic partitions, applied to \(\mathcal J=\mathcal I\), every finite subset \(K\subseteq F\) has a level \(n\) such that \((n,g)\) is admissible for all \(g\in K\).

**Lemma 3.2** (the recursion along the group). If \((n,g)\) is admissible, then for each \(i\)
\[
X^{(n)}_{I_i}(g)=f\Bigl(\frac1D\sum_{j=1}^DX^{(n)}_{I_i\cdot I_j}(g)\Bigr).
\]

**Proof.** Put \(T=gT^{(n)}\). It respects \(I_i\) and every \(I_i\cdot I_j\). By Lemma 2.4(c) of the lesson on dyadic partitions, \(T_{I_i}\) respects every \(I_j\) and \((T_{I_i})_{I_j}=T_{I_i\cdot I_j}\). So the first case of (2.3) applies to \(T_{I_i}\):
\[
p(T_{I_i})=f\Bigl(\frac1D\sum_jp\bigl((T_{I_i})_{I_j}\bigr)\Bigr)=f\Bigl(\frac1D\sum_jp(T_{I_i\cdot I_j})\Bigr).\qquad\square
\]

**Lemma 3.3** (transport of colors). Let \(I<J\) be members of \(\mathcal I\) and \(h\in F\) with \(h\circ s_I=s_{I_1}\) and \(h\circ s_J=s_{I_2}\). If \((n,g)\) and \((n,hg)\) are admissible, then
\[
X^{(n)}_I(g)=X^{(n)}_{I_1}(hg),\qquad X^{(n)}_J(g)=X^{(n)}_{I_2}(hg).
\]

**Proof.** Admissibility says that \(gT^{(n)}\) respects \(I\) and \(J\) and that \((hg)T^{(n)}\) respects \(I_1\) and \(I_2\). Lemma 4.2 of the lesson on dyadic partitions gives \(((hg)T^{(n)})_{I_1}=(gT^{(n)})_I\) and \(((hg)T^{(n)})_{I_2}=(gT^{(n)})_J\). Apply \(p\). \(\square\)

## 4. The uniform boundary bound

For every ordered pair \(I<J\) of members of \(\mathcal I\), choose by Lemma 4.1 of the lesson on dyadic partitions an element \(h_{I,J}\in F\) with
\[
h_{I,J}\circ s_I=s_{I_1},\qquad h_{I,J}\circ s_J=s_{I_2};
\]
this is possible because all members of \(\mathcal I\) are internal and \(I_1<I_2\). Let \(S\) be the finite set of these elements. It depends only on \(D\), \(r\) and the choices of the \(h_{I,J}\), not on any of the finite sets tested below.

**Proposition 4.1.** For every nonempty finite \(A\subseteq F\),
\[
\max_{h\in S}\frac{|hA\triangle A|}{|A|}\ \ge\ \frac{\delta^2/L^2-4/D}{4(1-1/D)}\ >0.\tag{4.1}
\]

**Proof.** Let \(\eta\) be the left side of (4.1). The set \(A\cup SA\), where \(SA=\{hg:h\in S,\ g\in A\}\), is finite; fix a level \(n\) such that \((n,g)\) is admissible for every \(g\in A\cup SA\), and omit the superscript \(n\). For \(I,J\in\mathcal I\) put \(\varphi_{I,J}(g)=\langle X_I(g),X_J(g)\rangle\), a function \(F\to[-1,1]\), and let \(\alpha=\mathbb E_A\varphi_{I_1,I_2}\).

*Step 1: separated correlations are nearly equal.* We claim
\[
\bigl|\mathbb E_A\varphi_{I,J}-\alpha\bigr|\le\eta\qquad\text{for all separated }I,J\in\mathcal I.\tag{4.2}
\]
Since \(\varphi_{I,J}=\varphi_{J,I}\), we may assume \(I<J\). Let \(h=h_{I,J}\). For \(g\in A\), both \(g\) and \(hg\) lie in \(A\cup SA\), so \((n,g)\) and \((n,hg)\) are admissible, and Lemma 3.3 gives \(\varphi_{I,J}(g)=\varphi_{I_1,I_2}(hg)\). Therefore
\[
\mathbb E_A\varphi_{I,J}=\frac1{|A|}\sum_{g\in A}\varphi_{I_1,I_2}(hg),
\]
and Lemma 1.2, applied to \(\varphi_{I_1,I_2}\), bounds its distance from \(\alpha\) by \(|hA\triangle A|/|A|\le\eta\).

*Step 2: a pointwise lower bound.* For \(g\in A\) put
\[
m(g)=\frac1D\sum_{k=1}^DX_{I_k}(g),\qquad z_i(g)=\frac1D\sum_{j=1}^DX_{I_i\cdot I_j}(g)\quad(1\le i\le D).
\]
These are averages of vectors in \(B\), so they lie in \(B\). By Lemma 3.2, \(X_{I_i}(g)=f(z_i(g))\), hence \(m(g)=\frac1D\sum_if(z_i(g))\). Using (2.1), the inequality \(\|\frac1D\sum_iy_i\|^2\le\frac1D\sum_i\|y_i\|^2\) (the triangle inequality followed by the Cauchy–Schwarz inequality in \(\mathbb R^D\)), and (2.1) again,
\[
\delta^2\le\|m-f(m)\|^2=\Bigl\|\frac1D\sum_{i=1}^D\bigl(f(z_i)-f(m)\bigr)\Bigr\|^2\le\frac1D\sum_{i=1}^D\|f(z_i)-f(m)\|^2\le\frac{L^2}D\sum_{i=1}^D\|z_i-m\|^2,\tag{4.3}
\]
everything evaluated at \(g\).

*Step 3: the variance bound.* We show that for each \(i\)
\[
\mathbb E_A\|z_i-m\|^2\le\frac4D+4\Bigl(1-\frac1D\Bigr)\eta.\tag{4.4}
\]
Expand \(\|m\|^2=\frac1{D^2}\sum_{k,l}\langle X_{I_k},X_{I_l}\rangle\). The \(D\) diagonal terms are at most \(1\), since colors lie in \(B\). The \(D(D-1)\) terms with \(k\neq l\) pair separated intervals (Lemma 3.1(a)), so by (4.2) their averages over \(A\) are at most \(\alpha+\eta\). Hence
\[
\mathbb E_A\|m\|^2\le\frac1D+\Bigl(1-\frac1D\Bigr)(\alpha+\eta),
\]
and by Lemma 3.1(b) the same bound holds for \(\mathbb E_A\|z_i\|^2\). Next, \(\langle z_i,m\rangle=\frac1{D^2}\sum_{j,k}\langle X_{I_i\cdot I_j},X_{I_k}\rangle\). The \(D(D-1)\) terms with \(k\neq i\) pair separated intervals (Lemma 3.1(c)) and have averages at least \(\alpha-\eta\). The remaining \(D\) terms pair a descendant of \(I_i\) with \(I_i\) itself; nothing is known about them except that they are at least \(-1\). Hence
\[
\mathbb E_A\langle z_i,m\rangle\ge\Bigl(1-\frac1D\Bigr)(\alpha-\eta)-\frac1D.
\]
Combining the three bounds in \(\|z_i-m\|^2=\|z_i\|^2+\|m\|^2-2\langle z_i,m\rangle\), the terms in \(\alpha\) cancel and (4.4) follows. No information on the sign or size of \(\alpha\) is needed.

*Step 4: conclusion.* Average (4.3) over \(g\in A\) and apply (4.4):
\[
\delta^2\le\frac{L^2}D\sum_{i=1}^D\mathbb E_A\|z_i-m\|^2\le L^2\Bigl(\frac4D+4\Bigl(1-\frac1D\Bigr)\eta\Bigr).
\]
Solving for \(\eta\) gives (4.1). The right side of (4.1) is positive by (2.2) and does not depend on \(A\). \(\square\)

## 5. The theorem

**Proof of Theorem 5.1.** By Proposition 1.3 of the lesson on dyadic partitions, \(F\) is a countable group. If it were amenable, Corollary 1.1, applied to the finite set \(S\) of Section 4 and to \(\varepsilon\) equal to the right side of (4.1), would give a nonempty finite \(A\subseteq F\) with \(|hA\triangle A|<\varepsilon|A|\) for all \(h\in S\), contradicting Proposition 4.1. \(\square\)

**Remarks.** (1) Proposition 4.1 is quantitative: one explicit finite set \(S\) and one constant work for all finite subsets of \(F\). By Theorem 2.1 of the lesson on means and Følner sets, \(F\) also admits no sequence of finitely supported probability measures that is asymptotically invariant in \(\ell^1\) under left translations.

(2) The argument rests on three exact identities, the recursion along the group (Lemma 3.2), the transport of colors (Lemma 3.3) and the cancellation in Lemma 1.2, and on the inequality \(\delta^2\le\|m-f(m)\|^2\). Step 1 says nothing about a parent and its own descendants (Exercise 6.3); the large parameter \(D\) makes these pairs a fraction \(\frac1D\) of the terms in Step 3.

(3) Brin and Squier showed that \(F\) has no free subgroup of rank two, and \(F\) is finitely presented; see [Gu, Section 1]. Theorem 5.1 therefore makes \(F\) a finitely presented nonamenable group without free subgroups of rank two. The first finitely presented groups of this kind were constructed by Ol'shanskii and Sapir [Gu, Section 1].

(4) Theorem 5.1 combines with two companion theorems of OpenAI about nonamenable groups. The first [OpenAI-U, Theorem 1.1] says that a discrete group is amenable if and only if every uniformly bounded representation of it on a complex Hilbert space is similar to a unitary representation, which answers Dixmier's unitarizability question for discrete groups. Applied to \(F\), it gives for every \(\varepsilon>0\) a separable complex Hilbert space and a representation \(\pi\) of \(F\) on it by bounded invertible operators with \(\sup_{g\in F}\|\pi(g)\|\le1+\varepsilon\) such that no bounded invertible \(T\) makes every \(T\pi(g)T^{-1}\) unitary. The second [OpenAI-P, Corollary 1.2] concerns Cayley graphs of nonamenable finitely generated groups. Applied to \(F\), which is finitely generated, it says that for every finite symmetric generating set, Bernoulli bond percolation on the corresponding Cayley graph has \(p_c<p_u\), and for each fixed \(p\) strictly between them there are almost surely infinitely many infinite clusters. The first companion theorem is proved in the course [Amenability and unitarizability](course:amenability-and-unitarizability/unitarizability-implies-amenability#4-all-discrete-groups), whose Corollary 5.1 is the statement for \(F\); the proof of the second is not part of the programme's courses.

## 6. Exercises

**Exercise 6.1** (easy). Prove that \(p(T^{(n)})=f^{\lfloor n/r\rfloor}(0)\) for every \(n\ge0\), where \(f^k\) is the \(k\)-fold composite and \(f^0\) the identity.

**Exercise 6.2** (easy). Show that equality can hold in Lemma 1.2: for nonempty finite \(A\) and \(h\in\Gamma\), find \(\varphi:\Gamma\to[-1,1]\) with \(\frac1{|A|}\sum_{g\in A}\varphi(hg)-\mathbb E_A\varphi=\frac{|hA\triangle A|}{|A|}\).

**Exercise 6.3** (easy). Show that no \(h\in F\) satisfies \(h(I_1)=I_1\) and \(h(I_1\cdot I_1)=I_2\). This is why Step 1 of Proposition 4.1 says nothing about a parent and its own descendants.

**Exercise 6.4** (medium). Let \(\Gamma\) be a countable group and \(\Lambda\subseteq\Gamma\) a subgroup. Show that if \(\Gamma\) is amenable, then so is \(\Lambda\). Conclude that every countable group containing a subgroup isomorphic to \(F\) is not amenable.

**Exercise 6.5** (medium). In the proof of Proposition 4.1, suppose that the colors \(X_I(g)\), \(I\in\mathcal I\), were all equal to one vector \(x_g\in B\) for each \(g\in A\). Show directly from (2.1) and Lemma 3.2 that this is impossible, and compare with Step 3: which terms of the variance bound does this special case make vanish?

## 7. Solutions

**6.1.** For \(n<r\), \(T^{(n)}\) respects no \(I_j\), since every cell is longer than \(I_j\); so \(p(T^{(n)})=0=f^0(0)\). For \(n\ge r\), \(T^{(n)}\) respects every \(I_j\) and \((T^{(n)})_{I_j}=T^{(n-r)}\) by formula (5.1) of the lesson on dyadic partitions, so all \(D\) colors in (2.3) equal \(p(T^{(n-r)})\) and \(p(T^{(n)})=f(p(T^{(n-r)}))\). Induction on \(n\) gives \(p(T^{(n)})=f(f^{\lfloor(n-r)/r\rfloor}(0))=f^{\lfloor n/r\rfloor}(0)\).

**6.2.** Take \(\varphi=1\) on \(hA\setminus A\), \(\varphi=-1\) on \(A\setminus hA\), and \(\varphi=0\) elsewhere. Then \(\sum_{g\in A}\varphi(hg)=\sum_{k\in hA}\varphi(k)=|hA\setminus A|\) and \(\sum_{g\in A}\varphi(g)=-|A\setminus hA|\); the difference is \(|hA\triangle A|\).

**6.3.** \(I_1\cdot I_1\subseteq I_1\), so \(h(I_1\cdot I_1)\subseteq h(I_1)=I_1\), which is disjoint from \(I_2\).

**6.4.** Choose a set \(R\) of representatives of the right cosets \(\Lambda\rho\), so that every \(g\in\Gamma\) is uniquely \(g=\lambda\rho\) with \(\lambda\in\Lambda\), \(\rho\in R\). For \(\phi\in\ell^\infty(\Lambda)\) define \(\tilde\phi\in\ell^\infty(\Gamma)\) by \(\tilde\phi(\lambda\rho)=\phi(\lambda)\). If \(m\) is a left invariant mean on \(\Gamma\), then \(m_\Lambda(\phi)=m(\tilde\phi)\) is positive, linear and \(m_\Lambda(1)=1\). For \(\mu\in\Lambda\), \((L_\mu\tilde\phi)(\lambda\rho)=\tilde\phi(\mu^{-1}\lambda\rho)=\phi(\mu^{-1}\lambda)=\widetilde{L_\mu\phi}(\lambda\rho)\), so \(m_\Lambda(L_\mu\phi)=m(L_\mu\tilde\phi)=m(\tilde\phi)=m_\Lambda(\phi)\). An isomorphism carries invariant means to invariant means, so a group containing a copy of \(F\) would make \(F\) amenable, contradicting Theorem 5.1.

**6.5.** If \(X_I(g)=x_g\) for all \(I\in\mathcal I\), then \(z_i(g)=x_g\), and Lemma 3.2 gives \(x_g=X_{I_i}(g)=f(z_i(g))=f(x_g)\), contradicting \(\|f(x_g)-x_g\|\ge\delta\). In this special case \(z_i=m=x_g\), so \(\|z_i-m\|^2=0\): all the terms in Step 3, including the parent–descendant terms, vanish. In general nothing forces the parent–descendant correlations to match the others, and Step 3 pays \(\frac4D\) for them.

## References

- [Gu] V. Guba, *Amenability problem for Thompson's group F: state of the art*, arXiv:2305.07113. https://arxiv.org/abs/2305.07113. Section 1.
- [OpenAI-F] OpenAI, *Thompson's group F is nonamenable*, OpenAI Math Release preprint, 23 September 2026, Sections 1–3. https://github.com/openai/math/blob/main/preprints/Thompsons-group-F-is-nonamenable-September-23-2026
- [OpenAI-Lean] OpenAI Math Release, *Thompson's group F is nonamenable*, scope of the Lean formalization. https://github.com/openai/math/blob/main/lean/docs/248.md
- [OpenAI-P] OpenAI, *Nonuniqueness of percolation on nonamenable quasi-transitive graphs*, OpenAI Math Release preprint, 24 September 2026, Corollary 1.2. https://github.com/openai/math/blob/main/preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026
- [OpenAI-U] OpenAI, *Unitarizability implies amenability for countable groups*, OpenAI Math Release preprint, 23 September 2026, Theorem 1.1. https://github.com/openai/math/blob/main/preprints/Unitarizability-Implies-Amenability-for-Countable-Groups-September-23-2026
- [Fø] E. Følner, *On groups with full Banach mean value*, Math. Scand. 3 (1955), 243–254. https://doi.org/10.7146/math.scand.a-10442
