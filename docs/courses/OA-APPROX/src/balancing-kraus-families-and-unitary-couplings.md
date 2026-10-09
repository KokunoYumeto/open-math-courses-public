# Balancing Kraus families and unitary couplings

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Self-checked by the writing AI. New original text: public domain (CC0).*

A unital Kraus family has \(\sum b_i^*b_i=1\). To turn its reconstruction map into an approximate unitary intertwiner, we also need \(\sum b_i b_i^*=1\). We will average the second sum, scale down slightly, and fill both remaining defects exactly. The repaired map changes arbitrarily little on the matrix algebra being modeled.

The inputs are the trace-preserving finite models, the [internal matrix Kraus formula](properly-infinite-injective-algebras-and-dyadic-approximation.md#lemma-4-1), and canonical center-valued trace and projection comparison. The [central trace cuts](central-traces-and-afd-finite-algebras.md#lemma-1-1) provide projections of arbitrary prescribed scalar trace in a \(\mathrm{II}_1\) factor. General tracial expectations retain the exact OA-MOD prerequisite used earlier. We prove the norm-averaging step here.

## 1. Filling two positive defects

Let \(M\) be a finite von Neumann algebra with a faithful normal tracial state \(\tau\), and let \(\mathcal T:M\to Z(M)\) be its canonical center-valued trace. Separability and factoriality are unnecessary in this section.

**Lemma 1.1.** If \(h,k\in M_+\) and \(\mathcal T(h)=\mathcal T(k)\), there is a finite or countable family \((a_i)\) such that
\[
h=\sum_i a_i^*a_i,\qquad k=\sum_i a_i a_i^*,
\tag{1}
\]
with strong convergence of the positive sums.

**Proof.** First suppose \(h\ne0\). Some nonzero spectral projection \(e\) satisfies \(h\ge\lambda e\) for \(\lambda>0\). Put \(z=c(e)\), its central support. Then
\(z\mathcal T(k)=z\mathcal T(h)\ge\lambda\mathcal T(e)\ne0\), so \(zk\ne0\). Choose a nonzero spectral projection \(f\le z\) with \(zk\ge\mu f\), \(\mu>0\). There are nonzero equivalent subprojections of \(e\) and \(f\): otherwise \(fMe=0\), which would force \(f\) to be orthogonal to the central support of \(e\). The polar decomposition of a nonzero element of \(fMe\) gives a partial isometry \(v\) with \(v^*v\le e\), \(vv^*\le f\). Thus
\[
a=\sqrt{\min(\lambda,\mu)}\,v
\quad\hbox{satisfies}\quad 0\ne a^*a\le h,\quad aa^*\le k.
\tag{2}
\]

Take a maximal collection of nonzero operators for which every finite sum of their \(a_i^*a_i\)'s is at most \(h\), and every finite sum of their \(a_i a_i^*\)'s is at most \(k\). A chain has its union as an upper bound, so Zorn's lemma applies. This collection is countable: all \(\tau(a_i^*a_i)>0\), while the finite sums are bounded by \(\tau(h)\). For each positive integer \(r\), only finitely many members can have trace at least \(1/r\), and these finite sets exhaust the collection.

The positive partial sums have strong limits \(H\le h\), \(K\le k\). Normality and traciality of \(\mathcal T\) give
\[
\mathcal T(h-H)=\mathcal T(k-K).
\tag{3}
\]
If the first remainder is nonzero, (2) supplies an operator that can be appended. Multiplying it by a scalar in \((0,1)\), if necessary, gives a new member distinct from every member of the countable collection, preserving both bounds. This contradicts maximality. Thus \(H=h\). Equation (3) and faithfulness of \(\mathcal T\) give \(K=k\). If \(h=0\) initially, faithfulness also gives \(k=0\), and the empty family suffices. \(\square\)

## 2. Simultaneous averaging in operator norm

**Lemma 2.1.** Let \(Q\) be a \(\mathrm{II}_1\) factor with its normalized trace. For any finite list \(x_1,\ldots,x_s\in Q\) and \(\varepsilon>0\), there is a finite convex combination of unitary conjugations
\[
P(x)=\sum_{j=1}^r\alpha_j w_jxw_j^*,\qquad
\alpha_j\ge0,\quad\sum_j\alpha_j=1,
\tag{4}
\]
such that \(\|P(x_i)-\tau(x_i)1\|<\varepsilon\) for every \(i\). No separable-predual hypothesis is needed.

**Proof.** First take one self-adjoint \(x\). Uniform spectral approximation gives
\(x_0=\sum_{j=1}^d\lambda_j p_j\), with a projection partition \((p_j)\) and \(\|x-x_0\|<\delta\). For a large integer \(N\), put
\[
k_j=\lfloor N\tau(p_j)\rfloor,
\qquad L=N-\sum_jk_j<d.
\tag{5}
\]
Cut \(q_j\le p_j\) of trace \(k_j/N\) and split it into \(k_j\) projections of trace \(1/N\). The residual projection \(r=1-\sum_jq_j\) has trace \(L/N\); split it into \(L\) such projections. Zero ranks require no projections. Together these give \(N\) equivalent projections summing to \(1\), hence a full matrix system in \(Q\). Its cyclic permutation unitary \(w\) defines
\[
P_N=\frac1N\sum_{\ell=0}^{N-1}\operatorname{Ad}(w^\ell),
\quad P_N(q_j)=\frac{k_j}{N}1,
\quad P_N(r)=\frac LN1.
\tag{6}
\]
The projection \(r\) commutes with \(x_0\). Write
\(x_0=\sum_j\lambda_jq_j+x_0r\). Since
\(-\|x_0\|r\le x_0r\le\|x_0\|r\), positivity of \(P_N\) gives
\(\|P_N(x_0r)\|\le\|x_0\|L/N\). Its scalar trace has the same absolute bound. Consequently
\[
\|P_N(x)-\tau(x)1\|
\le2\delta+2\|x_0\|\frac LN
\le2\delta+2\|x_0\|\frac dN.
\tag{7}
\]
First choose \(\delta\), then \(N\), to make this as small as desired.

For several self-adjoint elements, apply this one-element result successively to the current image of the next element. Every averaging map fixes scalars, preserves trace and is contractive; thus it preserves the error bounds already obtained. A finite composition of maps (4) is again a finite convex combination of unitary conjugations, by expanding the products of their unitaries and weights. For complex elements, include their real and imaginary parts with half the requested error. This proves the simultaneous assertion. \(\square\)

The residual projection in (5) records the dimension lost by rounding. Its cyclic average has norm \(L/N\), which is the reason this argument proves operator-norm approximation rather than only a trace-norm estimate.

### A second proof by spectral contraction

There is a second proof that uses spectral contraction rather than rounding projection dimensions. It also works in every finite factor, including a matrix algebra. For a nonscalar self-adjoint \(x\), write \(c=\min\operatorname{Sp}(x)\), \(C=\max\operatorname{Sp}(x)\), and \(t=(c+C)/2\). Its spectral projection \(p=1_{(-\infty,t]}(x)\) satisfies \(0<p<1\). Factor projection comparison puts either \(p\) or \(1-p\) below an equivalent subprojection of the other. First suppose \(p\precsim1-p\). Choose \(v\) with \(v^*v=p\), \(vv^*=p'\le1-p\), and set
\[
w=v+v^*+1-p-p',\qquad Q_w(x)=\tfrac12(x+wxw^*).
\]
The orthogonal initial and final projections show that \(w\) is a self-adjoint unitary interchanging \(p,p'\). Functional calculus gives \(x\ge cp+t(1-p)\). Conjugating this lower bound by \(w\) and adding gives
\[
\begin{aligned}
x+wxw^*&\ge(c+t)(p+p')+2t(1-p-p')\\
&\ge(c+t)1.
\end{aligned}
\]
The upper bound is \(x+wxw^*\le2C1\). Thus
\[
\operatorname{diam}\operatorname{Sp}(Q_w(x))
\le C-\frac{c+t}{2}=\frac34(C-c).
\]
If \(1-p\precsim p\), apply the same calculation to \(-x\) with lower projection \(q=1-p\), endpoints \(-C,-c\), and midpoint \(-t\). The inequalities \(-x\ge-Cq-t(1-q)\) and \(-x\le-c1\) give the same diameter bound. This uses the original complementary projection, so eigenvalues exactly at the midpoint cause no ambiguity.

Repeat the construction on the current averaged operator. After \(N\) steps its spectral diameter is at most \((3/4)^N(C-c)\); if an intermediate operator is scalar, stop. Each step preserves trace and is a convex average of two unitary conjugations. Their composite \(P\) is a finite convex average of unitary conjugations. The number \(\tau(P(x))=\tau(x)\) lies between the minimum and maximum of its spectrum, so
\[
\|P(x)-\tau(x)1\|\le(3/4)^N(C-c).
\]
This proves the one-element assertion without choosing rational projection dimensions. For a finite list, average the current real and imaginary parts successively, using half the requested tolerance for each part. Trace preservation and contractivity keep every previous bound, and composition remains a finite convex average. This proves the same simultaneous conclusion as Lemma 2.1. The spectral-contraction method is developed in Anantharaman–Popa, Section 6.4.

## 3. Balanced reconstruction on a matrix subfactor

**Theorem 3.1.** Let \(M\) be a \(\mathrm{II}_1\) factor, let \(D\subset M\) be a unital copy of \(M_m\), and let \(T:D\to M\) be ucp with \(\tau T=\tau|_D\). For every \(\varepsilon>0\), there is a finite or countable family \((a_i)\subset M\) such that
\[
\sum_i a_i^*a_i=\sum_i a_i a_i^*=1,
\qquad
\left\|T(x)-\sum_i a_i^*xa_i\right\|\le\varepsilon\|x\|
\quad(x\in D).
\tag{8}
\]
The sums of positive operators converge strongly. The family defines a normal trace-preserving ucp map on all of \(M\).

**Proof.** The internal Kraus lemma gives \(m^2\) operators \(b_i\in M\) such that
\[
T(x)=\sum_i b_i^*xb_i\quad(x\in D),\qquad
\sum_i b_i^*b_i=1.
\tag{9}
\]
Put \(c=\sum_i b_i b_i^*\). The trace-preserving expectation \(E_D\) satisfies, for every \(x\in D\),
\[
\tau(xE_D(c))=\tau(xc)=\tau(T(x))=\tau(x).
\tag{10}
\]
Nondegeneracy of the trace pairing on \(D\) gives \(E_D(c)=1\).

Matrix coordinates identify \(M\) with \(D\bar\otimes Q\), where \(Q=D'\cap M\) is a \(\mathrm{II}_1\) factor. The product normalized trace is the ambient trace. Write \(c=\sum_{i,j}e_{ij}c_{ij}\), with \(c_{ij}\in Q\). Equation (10) says \(\tau(c_{ij})=\delta_{ij}\). Lemma 2.1 gives one averaging map on \(Q\) bringing every coefficient within \(\alpha\) of its scalar trace. Its unitaries \(w_\ell\) commute with \(D\). Replacing the family in (9) by
\[
\widetilde b_{i\ell}=\sqrt{\alpha_\ell}\,w_\ell b_i
\tag{11}
\]
leaves \(T|_D\) unchanged and leaves the first positive sum equal to \(1\). Its second sum \(c'\) satisfies
\[
\|c'-1\|\le\sum_{i,j}\|P(c_{ij})-\delta_{ij}1\|<m^2\alpha.
\tag{12}
\]
Choose \(0<\eta<\min(1,\varepsilon/2)\) and then \(m^2\alpha<\eta\). Relabel the finite family as \(b_1,\ldots,b_p\) and put \(a_i=\sqrt{1-\eta}\,b_i\) for \(i\le p\). Its two sums are
\[
\sum_{i\le p}a_i^*a_i=(1-\eta)1,
\qquad \sum_{i\le p}a_i a_i^*=(1-\eta)c'\le(1-\eta)(1+\eta)1\le1.
\tag{13}
\]
The positive residuals
\[
h=\eta1,\qquad k=1-(1-\eta)c'
\tag{14}
\]
have equal scalar traces. In a factor this is equality of center-valued traces. Lemma 1.1 fills them with operators \(a_{p+1},a_{p+2},\ldots\).

Let \(B(x)=\sum_{i>p}a_i^*xa_i\). For \(x\ge0\), its partial sums increase and are bounded by \(\|x\|h\), so they converge strongly. Linear combinations of positive elements define the map for every \(x\); the same argument at each matrix level gives complete positivity. Increasing positive nets can be interchanged with these positive sums in each normal positive functional, proving normality. Its norm is \(\|B(1)\|=\eta\). On \(D\), the completed map is \((1-\eta)T+B\), so its distance from \(T\) is at most \(2\eta<\varepsilon\).

The completed map on \(M\) is ucp by its first sum. For \(x\ge0\), normality and traciality give
\(\tau(\sum_i a_i^*xa_i)=\tau(x^{1/2}(\sum_i a_i a_i^*)x^{1/2})=\tau(x)\). Thus it preserves trace by its second sum. This proves every assertion. \(\square\)

Factoriality is used in (14): scalar trace equality suffices there because the center is scalar. Lemma 1.1 itself retains the full nonfactor center-valued condition.

## 4. Approximation becomes a unitary coupling

Call two \(n\)-tuples of unitaries \((u_k)\), \((v_k)\) in a faithfully tracial finite algebra **\(\delta\)-related** if a countable family satisfies
\[
\sum_i a_i^*a_i=\sum_i a_i a_i^*=1,
\qquad
\sum_i\|a_i u_k-v_k a_i\|_2^2<\delta\quad(1\le k\le n).
\tag{15}
\]

**Proposition 4.1.** For a family with the two balanced sums, put \(\Psi(x)=\sum_i a_i^*xa_i\). Then
\[
\sum_i\|a_i u-v a_i\|_2^2
=2-2\operatorname{Re}\tau(u^*\Psi(v))
\le2\|u-\Psi(v)\|_2
\tag{16}
\]
for any two unitaries \(u,v\).

**Proof.** Expand the squared norms of finite partial sums. The two positive terms tend to \(1\) each, because \(\sum a_i^*a_i=1\), and the cross term converges to the displayed trace pairing. Strong convergence of the cp series and normality of \(\tau\) justify that limit. Since \(\tau(u^*u)=1\), the middle expression equals \(2\operatorname{Re}\tau(u^*(u-\Psi(v)))\). Cauchy–Schwarz gives its upper bound in (16). \(\square\)

**Corollary 4.2.** In an injective \(\mathrm{II}_1\) factor, every finite tuple \((u_k)\) is \(\delta\)-related to a tuple of unitaries in some unital matrix subfactor, for every \(\delta>0\).

**Proof.** The preceding lesson gives a trace-preserving ucp reconstruction from \(M_m\) with unitary input models. Projection cuts and comparison embed \(M_m\) unitally as a subfactor \(D\subset M\), preserving its normalized trace. Choose its reconstruction errors below \(\delta/4\). Apply Theorem 3.1 with operator-norm map error below \(\delta/4\). On each unitary model the two errors add to less than \(\delta/2\) in \(2\)-norm. Equation (16) proves (15). \(\square\)

## 5. Problems with complete solutions

**Exercise 1.** Why is scalar trace equality insufficient for Lemma 1.1 off factors?

*Solution.* In \(M=\mathbb C\oplus\mathbb C\) with its equal-weight faithful trace, take \(h=(1,0)\) and \(k=(0,1)\). They have the same scalar trace. However every \(a\) has \(a^*a=aa^*\) coordinate by coordinate, so the two sums in (1) must be identical. Here the center-valued trace is the identity and the necessary equality fails.

**Exercise 2.** Prove the countability assertion used in the maximal-family argument.

*Solution.* If each of \(r_0\) distinct positive numbers \(\tau(a_i^*a_i)\) is at least \(1/r\), their finite sum is at least \(r_0/r\). The bound by \(\tau(h)\) therefore limits their number to \(\lfloor r\tau(h)\rfloor\). Every positive number is at least \(1/r\) for some positive integer \(r\). Thus the nonzero family is a countable union of finite sets.

**Exercise 3.** Compute the rounding loss in (5) for a projection partition of traces \(1/3,1/3,1/3\) and \(N=8\).

*Solution.* Each \(k_j=2\), so \(L=8-6=2\). Each residual piece has trace \(1/3-1/4=1/12\); their sum has trace \(1/4=L/N\). Split that sum into two projections of trace \(1/8\). These complete the eight equivalent diagonal projections, even though the individual residual traces are not multiples of \(1/8\).

**Exercise 4.** Why does later averaging preserve earlier scalar approximation errors?

*Solution.* Any convex combination of unitary conjugations fixes \(\lambda1\) and is norm contractive. If \(\|y-\lambda1\|<\varepsilon\), its image satisfies \(\|P(y)-\lambda1\|=\|P(y-\lambda1)\|<\varepsilon\). Trace preservation ensures that the desired scalar for each next image is still the trace of the original element.

**Exercise 5.** Explain the direction of multiplication in (11).

*Solution.* The unitary multiplies \(b_i\) on the left. Then \((w b_i)^*x(w b_i)=b_i^*w^*xw b_i=b_i^*xb_i\) for \(x\in D\), because \(w\in D'\cap M\). The first sum is unchanged, while the second becomes \(w(\sum_i b_i b_i^*)w^*\), which is precisely the sum that needs averaging.

**Exercise 6.** Verify positivity and trace equality of the defects (14).

*Solution.* The bound \(c'\le(1+\eta)1\) implies \(k\ge\eta^2 1\ge0\). Also \(h=\eta1\ge0\). Traciality and the first sum give \(\tau(c')=\sum_i\tau(b_i b_i^*)=\sum_i\tau(b_i^*b_i)=1\). Hence \(\tau(k)=1-(1-\eta)=\eta=\tau(h)\).

**Exercise 7.** Why does the tail map in Theorem 3.1 have norm exactly \(\eta\)?

*Solution.* Its positive series is cp and sends \(1\) to \(h=\eta1\). For a cp map on a unital algebra, its operator norm is the norm of its value at \(1\), as proved in the finite CP preparation. Thus \(\|B\|=\eta\). The equality also follows by evaluating the norm at the unit, after the cp upper bound is established.

**Exercise 8.** Give a balanced family in \(M_2\) defining the depolarizing map.

*Solution.* Take \(a_{ij}=e_{ij}/\sqrt2\), for \(1\le i,j\le2\). Both \(\sum a_{ij}^*a_{ij}\) and \(\sum a_{ij}a_{ij}^*\) equal \(1\). Moreover \(\sum a_{ij}^*xa_{ij}=\frac12\sum_{i,j}x_{ii}e_{jj}=\tau_2(x)1\). This checks both balance conventions and the reconstruction orientation.

**Exercise 9.** For that family, take \(u=v=\operatorname{diag}(1,-1)\). Compute the coupling energy.

*Solution.* The diagonal terms commute with \(u\) and contribute zero. Each off-diagonal term has commutator \(\pm\sqrt2 e_{ij}\), whose normalized squared \(2\)-norm is \(1\). Their total energy is \(2\). Equation (16) gives the same result because \(\Psi(v)=0\), so \(2-2\operatorname{Re}\tau_2(u^*\Psi(v))=2\).

**Exercise 10.** Show that the relation in (15) is symmetric.

*Solution.* Replace each \(a_i\) by \(a_i^*\). The two balanced sums exchange roles. The adjoint of \(a_i u_k-v_k a_i\) is \(u_k^*a_i^*-a_i^*v_k^*\). Multiplying this on the left by \(u_k\) and on the right by \(v_k\) gives \(a_i^*v_k-u_k a_i^*\). Unitary multiplication and adjoints preserve the tracial \(2\)-norm, so every coupling energy is unchanged.

## References and proof scope

Uffe Haagerup, [*A new proof of the equivalence of injectivity and hyperfiniteness for factors on a separable Hilbert space*](https://doi.org/10.1016/0022-1236(85)90002-3), *Journal of Functional Analysis* 62 (1985), 160–201. Lemma 5.1 and Proposition 5.2 give the defect-filling and balanced reconstruction method. The two-defect lemma here retains nonfactor center-valued traces and a faithful normal tracial state; scalar trace equality is used only in the factor application. The balanced reconstruction theorem and its injective application retain the factor hypothesis, without separability.

Claire Anantharaman and Sorin Popa, [*An introduction to II₁ factors*, author draft](https://idpoisson.fr/anantharaman/publications/IIun.pdf), Theorem 6.4.1 and Corollary 6.4.2. Section 2 above supplies both a finite-cut averaging proof and a complete spectral-contraction proof of the required simultaneous operator-norm averaging. The next lesson turns small coupling energy into a single unitary conjugation.
