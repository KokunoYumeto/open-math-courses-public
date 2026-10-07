# Singular values and the Dixmier trace

*Written by GPT-6.1 Sol (OpenAI), September–October 2026, at Ultra; Proposition 4.4 and its discussion by Claude Opus 5.5 (Anthropic); editorial revision with OpenAI Codex, 3 October 2026. AI-written mathematical draft; not formally verified. Original text: CC0.*

What can we learn about an operator by observing only its first \(N\) singular values? A divergent sum may still have a stable logarithmic coefficient. To turn that coefficient into an integral, we must answer three different questions: which tails are too small to detect, how changing a spectral cutoff affects addition, and when the eventual answer is independent of a choice of limit.

We first study the finite observations themselves and test them on a direct sum. We then identify the tails that disappear in the logarithmic ideal norm, before using a scale average to repair additivity. The resulting traces lead to two further tests: whether their value is canonical, and whether they preserve monotone convergence. Finally, the zeta and heat calculations show how to obtain an actual number without selecting a generalized limit.

For the logarithmic-trace construction the human sources are [Dixmier 1966] and [Connes–Moscovici 1995]; [Carey–Rennie–Sedaev–Sukochev 2006] studies the connection with zeta asymptotics. [Lord–Sukochev 2010] discusses the normality of the functionals these traces define.

Our entry prerequisites are complex Hilbert spaces, elementary finite-dimensional linear algebra, real and complex calculus, and integration with monotone and dominated convergence. The supporting proofs are collected in Section 9, with links at their points of use: [compact decomposition](#compact-positive-operators), [compact-resolvent domains](#compact-resolvent-spectral-core), [Schatten estimates](#schatten-holder), and [positive extensions of limits](#extension-used-to-construct-a-state). The bounded positive functional calculus and scalar measure construction have complete proofs in [Positive spectral calculus](../../elliptic-boundary-reduction/lower-bounded-spectral-calculus.html#the-full-calculus-of-a-bounded-positive-contraction), AN03-SPC-001–003; the trace-class facts are proved in [Traces that survive passage to cohomology](../../elliptic-boundary-reduction/traces-and-complexes.html#the-trace-ideal-from-paired-orthonormal-systems), AN03-TRC-002–003. These are referenced proofs with their own licenses. In the sections on limits we use finite measures and polynomial approximation on a compact interval. Basic references are [Dixmier 1966], [Connes–Moscovici 1995], and [Carey–Rennie–Sedaev–Sukochev 2006]. Our trace class is on a separable complex Hilbert space \(H\), and \(\operatorname{Tr}\) denotes its ordinary trace.

## 1. A finite spectral budget

A finite observation is a sum of the largest singular values, not the trace of a fixed compression. The choice of the leading subspace depends on the operator. This is why the variational formulas below will give inequalities for sums rather than exact additivity.

The compact spectral decomposition and polar decomposition used here are proved in [Lemma 9.1](#compact-positive-operators), independently of this section. Start with that proof if these decompositions are not yet available.

For compact \(T\), let

\[
\mu_0(T)\geq\mu_1(T)\geq\cdots\geq0
\]

be the eigenvalues of \(|T|=(T^*T)^{1/2}\), counted with multiplicity and padded by zeros. An equivalent description is

\[
\mu_j(T)=\inf_{\operatorname{rank}R\leq j}\|T-R\|.
\tag{1.1}
\]

Indeed, truncate the polar spectral decomposition after \(j\) terms for the upper bound. For the lower bound, the restriction of a rank-\(j\) operator to the span of the first \(j+1\) eigenvectors has a nonzero kernel vector \(v\). On that span \(\|Tv\|\geq\mu_j(T)\|v\|\). This also proves the minimax description using restrictions to orthogonal complements of \(j\)-dimensional subspaces.

For \(N\geq1\) write \(S_N(T)=\sum_{j<N}\mu_j(T)\). The trace-class prerequisite gives the ideal inequality and \(|\operatorname{Tr}A|\leq\|A\|_1\). Specializing these facts gives

\[
\|T\|_1=\sup_{\|X\|\leq1}|\operatorname{Tr}(TX)|
\quad(T\text{ trace class}).
\tag{1.2}
\]

For the reverse inequality in (1.2), write \(T=U|T|\) and use \(X=U^*\). Ordinary trace cyclicity gives \(\operatorname{Tr}(TU^*)=\operatorname{Tr}|T|\). For compact \(T\) of infinite trace norm, the same supremum over **finite-rank** contractions is infinite: choose \(X=E_NU^*\), with \(E_N\) the leading spectral projection of \(|T|\). Restricting the supremum in this way avoids assigning an ordinary trace to a product outside the trace class.

**Theorem 1.1 (Ky Fan variational formulas).** For compact \(T\),

\[
S_N(T)=\sup_{\substack{E=E^*=E^2\\\operatorname{rank}E\leq N}}\|TE\|_1
=\sup_{\substack{\|X\|\leq1\\\operatorname{rank}X\leq N}}|\operatorname{Tr}(TX)|.
\tag{1.3}
\]

For positive \(T\), one also has

\[
S_N(T)=\sup_{\substack{E=E^*=E^2\\\operatorname{rank}E\leq N}}\operatorname{Tr}(TE).
\tag{1.4}
\]

**Proof.** Formula (1.1) implies \(\mu_j(TE)\leq\mu_j(T)\), since multiplication by a contraction does not increase the distance to the corresponding rank class. As \(TE\) has rank at most \(N\), its trace norm is at most \(S_N(T)\). Taking \(E=E_N\) gives equality. If \(X\) is a contraction of rank at most \(N\), its range projection \(E\) has rank at most \(N\), \(TX=TEX\), and \(|\operatorname{Tr}(TX)|\leq\|TE\|_1\). The choice \(X=E_NU^*\) gives equality. For positive \(T\), \(\operatorname{Tr}(TE)\leq\|TE\|_1\), and \(E_N\) again attains the bound. \(\square\)

Thus \(S_N\) is a norm. Formula (1.3) makes its triangle inequality visible, and (1.1) gives

\[
S_N(ATB)\leq\|A\|\|B\|S_N(T).
\tag{1.5}
\]

## 2. Allowing a fractional budget

A sum of two operators brings two potentially different leading subspaces into play. We will compare a fixed budget with the combined budget, so it is useful to allow a real cutoff. The following formula also makes the interpolation completely explicit. Define

\[
S_t(T)=\inf_{T=X+Y}\bigl(\|X\|_1+t\|Y\|\bigr),\qquad t>0,
\tag{2.1}
\]

where \(X\) is trace class and \(Y\) is compact. Put \(N=\lfloor t\rfloor\), \(\theta=t-N\).

**Theorem 2.1.** One has

\[
S_t(T)=\sum_{j<N}\mu_j(T)+\theta\mu_N(T).
\tag{2.2}
\]

In particular \(S_t\) is increasing and concave in \(t\), is affine between integers, and is a norm in \(T\) for each \(t>0\).

**Proof.** For \(T=X+Y\), (1.3) and the triangle inequality give \(S_m(T)\leq\|X\|_1+m\|Y\|\) at every integer \(m\geq1\), also at \(m=0\) with \(S_0=0\). Taking the convex combination of \(m=N,N+1\) gives the lower bound in (2.1). For the reverse inequality put \(c=\mu_N(T)\) and use the polar decomposition to set

\[
X=U(|T|-c)_+,\qquad Y=U\min(|T|,c).
\]

The first operator has finite rank, \(\|Y\|=c\) unless both sides are zero, and

\[
\|X\|_1+t\|Y\|=\sum_{j<N}(\mu_j-c)+tc.
\]

This is (2.2), including ties among the eigenvalues. At \(0<t<1\) it reduces to \(t\|T\|\). The decreasing slopes are precisely \(\mu_N(T)\), proving concavity. The infimum description proves homogeneity and subadditivity; positivity follows from \(S_t(T)\geq\min(1,t)\|T\|\). \(\square\)

For positive compact \(A,B\), the two estimates we need are

\[
S_t(A+B)\leq S_t(A)+S_t(B),
\qquad S_{s+t}(A+B)\geq S_s(A)+S_t(B).
\tag{2.3}
\]

**Proof of the second estimate.** For integers \(s,t\), choose their leading spectral subspaces and let \(E\) project onto the sum of those subspaces. Its rank is at most \(s+t\). Positivity gives \(\operatorname{Tr}(AE)\geq S_s(A)\) and \(\operatorname{Tr}(BE)\geq S_t(B)\); apply (1.4). For real \(s,t\), divide the quadrant into triangles whose vertices have integral coordinates and whose edges lie on integral lines for \(s,t,s+t\). On each triangle every term of the desired inequality is affine, by (2.2). The integral-vertex inequalities imply the inequality throughout the triangle. \(\square\)

**Exercise 1 (basic).** Let \(T=\operatorname{diag}(5,2,1,0,\ldots)\). Compute \(S_{1/2}(T)\), \(S_{3/2}(T)\), and \(S_{7/2}(T)\), and exhibit minimizing decompositions in (2.1).

**Solution.** Formula (2.2) gives \(5/2,6,8\). At \(t=1/2\), take \(X=0,Y=T\). At \(t=3/2\), use \(c=2\), so \(X=\operatorname{diag}(3,0,0,\ldots)\) and \(Y=\operatorname{diag}(2,2,1,0,\ldots)\), yielding \(3+(3/2)2=6\). At \(t=7/2\), take \(X=T,Y=0\). Theorem 2.1 proves each lower bound, so these are minima.

The next test isolates the obstruction that the logarithmic average must remove.

**Exercise 3 (intermediate).** On \(H\oplus H\), let \(A=T\oplus0\) and \(B=0\oplus T\), with \(T\geq0\). Prove \(S_{2N}(A+B)=2S_N(T)\). Use \(T\) with eigenvalues \(1/(j+1)\) to explain why \(S_N\) is not additive even on positive operators.

**Solution.** The singular values of \(A+B=T\oplus T\) repeat every singular value of \(T\) twice, proving the identity. But \(S_N(A)+S_N(B)=2S_N(T)\), while \(S_N(A+B)=2S_{N/2}(T)\) by (2.2). For \(N=2\) these are three and two, respectively. Exact additivity fails before the averaging and quotient steps.

## 3. Logarithmic size and the additivity defect

Fix \(a>e\). The ideal of logarithmic size is

\[
\mathcal M_{1,\infty}=\left\{T\text{ compact}:\|T\|_{\mathcal M}:=
\sup_{t\geq a}\frac{S_t(T)}{\log t}<\infty\right\}.
\tag{3.1}
\]

This ideal is also denoted \(\mathcal L^{(1,\infty)}\). We keep \(\mathcal L_{1,\infty}\) for the potentially smaller condition \(\mu_j(T)=O((j+1)^{-1})\); the two conditions are not definitions of the same normed space.

The norms (2.1) prove the triangle inequality in (3.1), and \(\|T\|\leq(S_a(T)/\log a)\log a\) proves that it dominates the operator norm up to a fixed constant. The ideal estimate (1.5) extends to real \(t\) by (2.1). This is a Banach ideal: a Cauchy sequence converges in operator norm to a compact \(T\); (1.1) implies continuity of each \(S_t\), and taking the supremum in (3.1) shows convergence in \(\|\cdot\|_{\mathcal M}\).

### First question: which tails can finite-rank approximation remove?

Before constructing a trace, we can decide when the entire logarithmic observation is negligible. This is a statement about the ideal norm, not about any choice of state.

**Proposition 3.1 (vanishing logarithmic tails).** The norm closure of finite-rank operators is exactly

\[
\mathcal M_0=\{T\in\mathcal M_{1,\infty}:S_t(T)=o(\log t)\}.
\tag{3.2}
\]

In particular, \(\mu_j(T)=o((j+1)^{-1})\) implies \(T\in\mathcal M_0\).

**Proof.** A finite-rank operator has bounded \(S_t\). Norm approximation and the triangle inequality show the forward implication in (3.2). Conversely, truncate the polar spectral decomposition at \(N\), writing its tail as \(R_N\). For fixed \(b\geq a\), (2.2) gives \(S_t(R_N)\leq t\mu_N(T)\) when \(a\leq t\leq b\), and \(S_t(R_N)\leq S_t(T)\) for all \(t\). First choose \(b\) so the latter ratio is small for \(t\geq b\), then let \(N\to\infty\) to control the bounded interval. This proves norm approximation. Finally split the sum of singular values into a finite initial segment and a tail bounded by \(\epsilon\sum_{j\leq t}(j+1)^{-1}\), then let \(\epsilon\to0\). \(\square\)

The approximation statement does not say that a nonzero logarithmic coefficient exists for every other operator. To obtain an additive observation even when no ordinary coefficient exists, we must address the cutoff discrepancy seen in Exercise 3.

### Second question: can a change of scale be averaged away?

In the coordinate \(x=\log u\), doubling the cutoff shifts \(x\) by the fixed amount \(\log2\). This suggests averaging \(S_{e^x}(T)/x\) over \(x\); the estimate below controls both the shifted endpoints and the change in its denominator. For \(T\geq0\) define the averaged logarithmic mean

\[
C_\lambda(T)=\frac1{\log\lambda}\int_a^\lambda
\frac{S_u(T)}{\log u}\,\frac{du}{u},\qquad\lambda\geq a.
\tag{3.3}
\]

This is a bounded continuous function with \(0\leq C_\lambda(T)\leq\|T\|_{\mathcal M}\).

**Theorem 3.2 (averaged additivity).** If \(A,B\geq0\) and \(S_u(A)\leq C_A\log u, S_u(B)\leq C_B\log u\) for \(u\geq a\), then

\[
0\leq C_\lambda(A)+C_\lambda(B)-C_\lambda(A+B)
\leq(C_A+C_B)\frac{(\log\log\lambda+2)\log2}{\log\lambda}.
\tag{3.4}
\]

**Proof.** The first estimate in (2.3) gives the lower bound. For the upper bound use \(S_{2u}(A+B)\geq S_u(A)+S_u(B)\). After changing variable \(v=2u\), the sum of the two means is bounded by

\[
\frac1{\log\lambda}\int_{2a}^{2\lambda}
\frac{S_v(A+B)}{\log(v/2)}\,\frac{dv}{v}.
\]

Replacing \(\log(v/2)\) by \(\log v\) changes this by at most

\[
\frac{(C_A+C_B)\log2}{\log\lambda}
\int_{2a}^{2\lambda}\frac{dv}{v\log(v/2)}
=\frac{(C_A+C_B)\log2}{\log\lambda}
(\log\log\lambda-\log\log a).
\]

Moving the integration interval from \([2a,2\lambda]\) to \([a,\lambda]\) changes the integral with denominator \(\log v\) by at most \(2(C_A+C_B)\log2/\log\lambda\). Since \(\log\log a>0\), these estimates imply (3.4). They hold also when the two intervals overlap only partially. \(\square\)

Thus (3.4) answers the direct-sum obstruction quantitatively: the averaged observations are additive up to a function tending to zero. The denominator correction contributes \(\log\log\lambda/\log\lambda\), and the endpoint intervals contribute \(2/\log\lambda\), both with the stated factor \((C_A+C_B)\log2\). No ordinary limit of \(S_u(T)/\log u\) has been assumed.

## 4. From means to traces

The estimate just proved has a natural target: regard two bounded continuous observations as the same when their difference tends to zero. This retains a possibly nonconvergent observation while making its trace identities exact.

Let \(\mathcal Q=C_b([a,\infty))/C_0([a,\infty))\). Taking the class of (3.3), Theorem 3.2 gives an additive homogeneous map on the positive cone. Every selfadjoint element \(T\) of the ideal has \(T=T_+-T_-\) with \(T_\pm\geq0\) in the ideal. Define

\[
\Theta(T)=[C(T_+)]-[C(T_-)],
\]

and then extend complex linearly. This does not depend on the positive decomposition: \(A-B=A'-B'\) implies \(A+B'=A'+B\), and additivity in the quotient proves equality.

**Theorem 4.1.** The map \(\Theta:\mathcal M_{1,\infty}\to\mathcal Q\) is positive, complex linear, and satisfies

\[
\Theta(ST)=\Theta(TS)\qquad(S\in B(H),\ T\in\mathcal M_{1,\infty}).
\tag{4.1}
\]

It vanishes on trace-class operators.

**Proof.** A unitary conjugation preserves every singular value, hence preserves \(\Theta\) first on positive operators and then on the whole ideal. For unitary \(U\), apply this invariance to \(TU\) to obtain \(\Theta(UT)=\Theta(TU)\). A selfadjoint contraction \(S\) is \((V+V^*)/2\), where \(V=S+i(1-S^2)^{1/2}\) is unitary. Splitting a general bounded operator into real and imaginary selfadjoint parts and rescaling therefore proves (4.1). For positive trace-class \(T\),

\[
0\leq C_\lambda(T)\leq\|T\|_1
\frac{\log\log\lambda-\log\log a}{\log\lambda}\longrightarrow0.
\]

Linearity gives the assertion for all trace-class operators. \(\square\)

A **generalized limit** here is a state \(\omega\) on \(\mathcal Q\). Passing from a quotient-valued observation to a number requires such a state.

**Lemma 4.2 (existence of generalized limits).** The quotient \(\mathcal Q\) has states obtained by evaluation along any sequence \(\lambda_j\to\infty\) followed by a positive extension of the ordinary sequence limit.

**Proof.** On convergent real sequences, the ordinary limit is a norm-one functional. [Lemma 9.4](#extension-used-to-construct-a-state) extends it to all bounded sequences, proves positivity, and then complexifies it. Evaluation along \(\lambda_j\) followed by this extension annihilates \(C_0\), since every function in \(C_0\) evaluates to a sequence with limit zero. It therefore gives a positive unital functional on \(\mathcal Q\). \(\square\)

A countable version of the choice of state is sometimes enough. For a separable unital C*-subalgebra of \(\mathcal Q\), choose representatives \(f_1,f_2,\ldots\) of a dense countable set. Successive subsequences of evaluations at \(\lambda=n+a\), followed by a diagonal subsequence, make every \(f_j\) converge. The limits extend by continuity to a positive unital functional on the subalgebra: the evaluation estimates are bounded by the quotient norm \(\limsup_{\lambda\to\infty}|f(\lambda)|\), and positive quotient classes have representatives whose negative parts tend to zero. This uses countably many subsequence choices and does not require simultaneous choices for all bounded functions.

Define

\[
\operatorname{Tr}_\omega(T)=\omega(\Theta(T)).
\tag{4.2}
\]

**Theorem 4.3.** Each \(\operatorname{Tr}_\omega\) is a positive bounded trace on \(\mathcal M_{1,\infty}\), invariant under bounded similarity and zero on the norm closure of finite-rank operators.

**Proof.** Positivity and cyclicity follow from Theorem 4.1. On positive operators its value lies between zero and \(\|T\|_{\mathcal M}\). For selfadjoint \(T\), positivity and \(-|T|\leq T\leq |T|\) give the same bound in absolute value. For general \(T\), the ideal norm triangle inequality gives \(\|\operatorname{Re}T\|_{\mathcal M},\|\operatorname{Im}T\|_{\mathcal M}\leq\|T\|_{\mathcal M}\), yielding a bound \(2\|T\|_{\mathcal M}\). This sufficient continuity bound, together with vanishing on finite rank, proves vanishing on its closure. Similarity follows from cyclicity. \(\square\)

This construction uses arbitrary states **after** logarithmic averaging. If one applies a generalized limit directly to \(S_t(T)/\log t\), an invariance hypothesis on that generalized limit is needed for the additivity argument. The convention (4.2) specifies exactly which family of traces is under discussion.

### A singular integral need not satisfy monotone convergence

A positive element of the logarithmic ideal can serve as a weight: pairing it with bounded operators through a trace (4.2) gives a positive functional on all of \(B(H)\). The next proposition shows that such a functional vanishes on compact operators, and that this property is incompatible with monotone convergence as soon as the weight has positive trace.

**Proposition 4.4.** Suppose that \(H\) is separable and infinite dimensional, and let \(T\in\mathcal M_{1,\infty}\) be positive. The functional
\[
\Phi_\omega(A)=\operatorname{Tr}_\omega(AT),\qquad A\in B(H),
\]
has the following properties.

(i) \(\Phi_\omega(K)=0\) for every compact operator \(K\).

(ii) \(\Phi_\omega\) is a positive linear functional on \(B(H)\), and \(\|\Phi_\omega\|=\Phi_\omega(I)=\operatorname{Tr}_\omega(T)\). In particular \(\Phi_\omega=0\) when \(\operatorname{Tr}_\omega(T)=0\).

(iii) If \(\operatorname{Tr}_\omega(T)>0\), then \(\Phi_\omega\) fails monotone convergence on \(B(H)\). There are finite-rank projections \(P_1\leq P_2\leq\cdots\) converging strongly to \(I\), and every such sequence satisfies
\[
\Phi_\omega(P_N)=0\quad\text{for every }N,\qquad\Phi_\omega(I)>0.
\]
Consequently \(\Phi_\omega\) is not normal, where normality means \(\Phi_\omega(\sup_\alpha X_\alpha)=\sup_\alpha\Phi_\omega(X_\alpha)\) for every bounded increasing family \((X_\alpha)\) of positive operators.

**Proof.** Multiplication by a bounded operator is bounded on the ideal. Multiplying a decomposition \(X=X_1+X_2\) as in (2.1) by \(A\) on either side, and using \(\|AX_1\|_1,\|X_1A\|_1\leq\|A\|\,\|X_1\|_1\), gives the real-cutoff form of (1.5): \(S_t(AX)\) and \(S_t(XA)\) are at most \(\|A\|S_t(X)\) for bounded \(A\), compact \(X\) and \(t>0\). For \(X\in\mathcal M_{1,\infty}\), dividing by \(\log t\) and taking the supremum over \(t\geq a\) yields
\[
\|AX\|_{\mathcal M}\leq\|A\|\,\|X\|_{\mathcal M},\qquad\|XA\|_{\mathcal M}\leq\|A\|\,\|X\|_{\mathcal M}.
\]
Hence \(AT\in\mathcal M_{1,\infty}\), and \(\Phi_\omega\) is linear because \(\operatorname{Tr}_\omega\) is.

For (i), Lemma 9.1 applied to \(K^*K\) shows \(\mu_j(K)\to0\). By (1.1), for each \(j\geq1\) there is an operator \(R_j\) of rank at most \(j\) with \(\|K-R_j\|\leq\mu_j(K)+1/j\). Every \(R_jT\) has finite rank, and
\[
\|KT-R_jT\|_{\mathcal M}\leq\|K-R_j\|\,\|T\|_{\mathcal M}\longrightarrow0.
\]
Thus \(KT\) lies in the closure of the finite-rank operators in \(\|\cdot\|_{\mathcal M}\), on which \(\operatorname{Tr}_\omega\) vanishes by Theorem 4.3.

For (ii), let \(A\geq0\), and let \(R=A^{1/2}\) be its positive square root, given by the bounded positive functional calculus listed among the prerequisites. Formula (4.1), applied to the bounded operator \(R\) and the ideal element \(RT\), moves the left factor \(R\) to the right:
\[
\Phi_\omega(A)=\operatorname{Tr}_\omega(R\,RT)=\operatorname{Tr}_\omega(RTR)\geq0,
\]
because \(\langle RTR\xi,\xi\rangle=\langle TR\xi,R\xi\rangle\geq0\) and \(\operatorname{Tr}_\omega\) is positive. For selfadjoint \(B\), the operators \(\|B\|I+B\) and \(\|B\|I-B\) are positive; applying \(\Phi_\omega\) to both shows that \(\Phi_\omega(B)\) is real and \(|\Phi_\omega(B)|\leq\|B\|\Phi_\omega(I)\). For arbitrary \(A\), choose \(c\in\mathbb C\) with \(|c|=1\) and \(c\Phi_\omega(A)=|\Phi_\omega(A)|\), and split \(cA=B_1+iB_2\) with selfadjoint \(B_1=(cA+(cA)^*)/2\) and \(B_2=(cA-(cA)^*)/(2i)\). The numbers \(\Phi_\omega(B_1)\) and \(\Phi_\omega(B_2)\) are real, and \(\Phi_\omega(B_1)+i\Phi_\omega(B_2)=|\Phi_\omega(A)|\) is real, so \(\Phi_\omega(B_2)=0\) and
\[
|\Phi_\omega(A)|=\Phi_\omega(B_1)\leq\|B_1\|\,\Phi_\omega(I)\leq\|A\|\,\Phi_\omega(I).
\]
Equality at \(A=I\) shows \(\|\Phi_\omega\|=\Phi_\omega(I)=\operatorname{Tr}_\omega(T)\).

For (iii), Gram–Schmidt applied to a dense sequence gives an orthonormal basis \((e_k)_{k\geq1}\) of \(H\). The orthogonal projections \(P_N\) onto \(\operatorname{span}\{e_1,\ldots,e_N\}\) have finite rank, increase with \(N\), and converge strongly to \(I\), since Parseval gives \(\|\xi-P_N\xi\|^2=\sum_{k>N}|\langle\xi,e_k\rangle|^2\). Now let \((P_N)\) be any increasing sequence of finite-rank projections with strong limit \(I\). Part (i) gives \(\Phi_\omega(P_N)=0\) for every \(N\), whereas \(\Phi_\omega(I)=\operatorname{Tr}_\omega(T)>0\). The supremum of the sequence is \(I\): the numbers \(\langle P_N\xi,\xi\rangle\) increase to \(\|\xi\|^2\), so \(P_N\leq I\), and every selfadjoint \(B\) with \(B\geq P_N\) for all \(N\) satisfies \(\langle B\xi,\xi\rangle\geq\|\xi\|^2\). Normality would force \(\Phi_\omega(I)=\sup_N\Phi_\omega(P_N)=0\). \(\square\)

Part (i) is the mechanism behind (iii). Operators that differ by a compact operator have the same value, so the complementary projections \(I-P_N\), which decrease strongly to zero, all have the value \(\operatorname{Tr}_\omega(T)\). For the same reason, the values of \(\Phi_\omega\) on a strongly dense subalgebra need not determine it. The finite-rank operators form such a subalgebra, since for bounded \(A\)
\[
P_NAP_N\xi-A\xi=P_NA(P_N\xi-\xi)+(P_N-I)A\xi\longrightarrow0,
\]
and \(\Phi_\omega\) vanishes on all of them, although \(\Phi_\omega(I)>0\) in the situation of (iii). Norm continuity, in contrast, determines \(\Phi_\omega\) on the norm closure of a subalgebra from its values on the subalgebra.

Normality of a restriction is a separate question for each algebra of coefficients, because it involves only increasing families inside that algebra. If a unital subalgebra \(\mathcal N\subseteq B(H)\) contains an increasing sequence of compact positive operators with strong limit \(I\), the argument for (iii) runs inside \(\mathcal N\), and the restriction of \(\Phi_\omega\) to \(\mathcal N\) is not normal when \(\operatorname{Tr}_\omega(T)>0\). If \(\mathcal N\) contains no nonzero compact operator, part (i) gives no information about \(\Phi_\omega\) on \(\mathcal N\).

Positivity and boundedness pass from \(\operatorname{Tr}_\omega\) to \(\Phi_\omega\); the trace property is a separate matter. Cyclicity (4.1) moves a bounded factor past the ideal element \(AT\), so \(\Phi_\omega(BA)=\operatorname{Tr}_\omega(B\,AT)=\operatorname{Tr}_\omega(ATB)\) and
\[
\Phi_\omega(AB)-\Phi_\omega(BA)=\operatorname{Tr}_\omega(A[B,T]),\qquad A,B\in B(H).
\]
The right side vanishes for every \(A\) when \([B,T]\) lies in the closure of the finite-rank operators in \(\|\cdot\|_{\mathcal M}\), for example when \(B\) commutes with \(T\): by the estimate at the start of the proof, left multiplication by \(A\) maps that closure into itself, and \(\operatorname{Tr}_\omega\) vanishes on it by Theorem 4.3. Whether \(\Phi_\omega\) is a trace on a given algebra of coefficients is decided by these commutators.

The failure of normality for functionals defined by Dixmier traces, and the separate question of normality on a smaller von Neumann algebra, are also discussed in S. Lord and F. Sukochev, *Measure Theory in Noncommutative Spaces*, [arXiv:1009.3095v1](https://arxiv.org/abs/1009.3095v1), Introduction.

## 5. When the choice disappears

There are two distinct independence questions. First, does every generalized limit assign the same number? Second, does the quotient-valued observation depend on a choice of equivalent Hilbert norm? The first is a scalar limiting question; the second follows from cyclicity.

### Agreement of all scalar observations

**Lemma 5.1.** For \(f\in C_b([a,\infty))\), all states on \(\mathcal Q\) give the same value on \([f]\) if and only if \(f\) has an ordinary limit at infinity.

**Proof.** If \(f\to L\), its quotient class is the constant \(L\). If \(f\) has no limit, boundedness gives two sequences escaping to infinity on which \(f\) converges to distinct complex numbers. The sequence-evaluation states constructed above have those two values. \(\square\)

For \(T\geq0\), **measurability for the family (4.2)** therefore means exactly that \(C_\lambda(T)\) converges. For general \(T\), choose the bounded continuous representative

\[
C_\lambda((\operatorname{Re}T)_+)-C_\lambda((\operatorname{Re}T)_-)
+iC_\lambda((\operatorname{Im}T)_+)-iC_\lambda((\operatorname{Im}T)_-).
\]

Lemma 5.1 gives the same criterion for this representative. A different positive decomposition changes it by a function tending to zero.

### Error rates and equivalent Hilbert norms

The construction also records more than a limiting number. The error bound in Theorem 3.2 allows a finer comparison of asymptotic observations.

The cyclic observation in Theorem 4.1 has a finer algebraic version. Put \(\rho(\lambda)=\log\log\lambda/\log\lambda\), and quotient bounded continuous functions by those that are \(O(\rho)\). This is an algebraic quotient, not asserted to be a C*-algebra. The bound (3.4) proves additivity already in that quotient; the same unitary argument proves (4.1) there as well. The trace-class bound is also \(O(\rho)\). Thus we retain the rate at which the trace identities become exact, before passing to the larger ideal of all functions tending to zero.

**Corollary 5.2 (equivalent Hilbert norms).** If two Hilbert inner products give the same norm topology, the two resulting maps \(\Theta\) agree after identifying their underlying vector spaces. The same holds for the finer algebraic quotient.

**Proof.** Equivalent Hilbert norms give a bounded positive invertible change of metric. Its square root identifies the new Hilbert space isometrically with the old one, transporting \(T\) to \(STS^{-1}\) for a bounded invertible \(S\). Formula (4.1) applied to \(ST\) and \(S^{-1}\) gives \(\Theta(STS^{-1})=\Theta(T)\). \(\square\)

**Example 5.3 (the harmonic boundary).** On \(\ell^2(\mathbb N)\), let \(Te_j=\frac{3}{j+1}e_j\), indexing from zero. The integral comparison for the harmonic series gives \(S_N(T)=3\log N+O(1)\), so every trace (4.2) gives three. The operator \(T^2\) is trace class and every such trace gives zero. These values distinguish ordinary summability from its logarithmic boundary.

**Exercise 2 (intermediate).** Show that a positive compact operator with eigenvalues \((j+2)^{-1}(\log(j+2))^{-1}\) belongs to \(\mathcal M_0\), although its ordinary trace is infinite.

**Solution.** The eigenvalues decrease. Integral comparison with \(1/(x\log x)\) gives \(S_N=\log\log N+O(1)\). This diverges, but \(S_N/\log N\to0\). Real interpolation and Proposition 3.1 give membership in \(\mathcal M_0\), hence zero value for every trace (4.2).

These calculations separate a nonzero logarithmic coefficient from an infinite ordinary trace that is nevertheless invisible to every trace in (4.2). Proposition 3.1 identifies the ideal-norm approximation behind the second conclusion.

## 6. Recovering the coefficient from a zeta function

The criterion in Section 5 asks for a limit of spectral observations. In applications, a zeta function or a heat trace may be easier to compute. We now connect these data in two steps: a Tauberian argument converts a Laplace asymptotic into an eigenvalue threshold, and a singular-value bound converts that threshold into a rank cutoff. Keeping these steps separate makes the extra hypothesis visible.

**Theorem 6.1 (a Tauberian equivalence).** Suppose \(T\geq0\) and \(\mu_j(T)\leq C/(j+1)\). Write \(\zeta_T(s)=\operatorname{Tr}(T^s)\) for real \(s>1\). For \(L\geq0\), the following are equivalent:

\[
\lim_{s\downarrow1}(s-1)\zeta_T(s)=L,
\qquad
\lim_{N\to\infty}\frac1{\log N}\sum_{j<N}\mu_j(T)=L.
\tag{6.1}
\]

In either case every trace (4.2) takes the value \(L\) on \(T\).

**Proof.** Rescale \(T\), if necessary, so \(\|T\|\leq1\). Both limits scale by the same factor, since \(c^{1+\epsilon}\to c\). Zero eigenvalues contribute nothing. Define the positive measure

\[
dU(t)=\sum_{\mu_j>0}\mu_j\delta_{-\log\mu_j}(dt),\quad t\geq0.
\]

It is finite on bounded intervals, and

\[
\zeta_T(1+\epsilon)=\int_0^\infty e^{-\epsilon t}\,dU(t).
\tag{6.2}
\]

We first prove that \(\epsilon\) times this Laplace transform tends to \(L\) exactly when \(U([0,R])/R\to L\). The reverse direction follows from Tonelli:

\[
\epsilon\int e^{-\epsilon t}\,dU(t)
=\epsilon^2\int_0^\infty e^{-\epsilon t}U([0,t])\,dt.
\]

If \(U([0,t])=Lt+o(t)\), divide the integral at a fixed large threshold. The bounded initial part tends to zero, and the tail error is bounded by \(\epsilon^2\int e^{-\epsilon t}\epsilon_0t\,dt=\epsilon_0\). The main integral is \(L\).

For the forward direction, let \(d\nu_R(u)=R^{-1}dU(Ru)\). The assumed limit gives, for every integer \(k\geq1\),

\[
\int e^{-ku}\,d\nu_R(u)=R^{-1}\zeta_T(1+k/R)\longrightarrow L/k.
\]

Push \(e^{-u}d\nu_R(u)\) to \([0,1]\) by \(x=e^{-u}\). Its \(m\)-th moment tends to \(L/(m+1)\) for every integer \(m\geq0\), precisely the moments of \(L\,dx\). Polynomial approximation and the bounded zeroth moments imply convergence against every continuous function on \([0,1]\). Continuous upper and lower approximations to \(x^{-1}1_{[e^{-1},1]}(x)\), with arbitrarily short transition intervals, then show

\[
\nu_R([0,1])\longrightarrow L\int_{e^{-1}}^1\frac{dx}{x}=L.
\]

The limiting Lebesgue measure gives zero mass to the endpoints, so those transitions add no persistent error. This is the desired Tauberian direction.

It remains to compare an eigenvalue threshold with a rank threshold. The difference between \(U([0,\log N])\) and \(S_N(T)\) is uniformly bounded: omitted terms among the first \(N\) are each below \(1/N\), with total at most one; included terms beyond \(N\) must have \(j+1\leq CN\), and their sum is bounded by \(C\sum_{N<j+1\leq CN}(j+1)^{-1}\). This harmonic sum is bounded independently of \(N\). Taking \(N=\lfloor e^R\rfloor\), the interval between \(e^{-R}\) and \(1/N\) contains at most \(Ce^R\) terms, each at most \(1/N\); their total is at most \(2C\) for large \(R\). This proves equivalence with the second limit in (6.1). Formula (2.2) passes it to real cutoffs. An ordinary Cesàro average preserves a limit, so (3.3) also tends to \(L\). \(\square\)

The upper bound on singular values is a hypothesis of this theorem. It has not been deduced merely from membership in \(\mathcal M_{1,\infty}\).

For the heat application, the eigenbasis and graph-domain assertions are supplied by [Lemma 9.2](#compact-resolvent-spectral-core), whose proof uses only the compact spectral decomposition and selfadjointness. No trace construction is used in that spectral argument.

**Corollary 6.2 (heat normalization).** Let \(Q\geq cI>0\) have compact resolvent, and suppose

\[
\operatorname{Tr}(e^{-tQ})\sim A\,t^{-p},\qquad t\downarrow0,\quad p>0,\quad A>0.
\]

Then \(Q^{-p}\) satisfies the hypothesis of Theorem 6.1 and

\[
\operatorname{Tr}_\omega(Q^{-p})=\frac{A}{\Gamma(p+1)}.
\tag{6.3}
\]

**Proof.** If \(N_Q(R)\) counts eigenvalues at most \(R\), then \(e^{-1}N_Q(R)\leq\operatorname{Tr}(e^{-Q/R})=O(R^p)\). Thus the eigenvalues of \(Q^{-p}\) are \(O((j+1)^{-1})\). Functional calculus and Tonelli give

\[
\operatorname{Tr}(Q^{-p(1+\epsilon)})=
\frac1{\Gamma(p+p\epsilon)}\int_0^\infty
\operatorname{Tr}(e^{-tQ})t^{p+p\epsilon}\,\frac{dt}{t}.
\]

For \(t\geq1\), exponential decay follows from \(Q\geq cI\) and the finite heat trace at \(t=1/2\). That part disappears after multiplication by \(\epsilon\). On a sufficiently small interval the heat trace differs from \(At^{-p}\) by at most \(\eta t^{-p}\). Its main integral is \(A/(p\epsilon)\); the error is bounded by \(\eta/(p\epsilon)\). Let \(\epsilon\downarrow0\), then \(\eta\downarrow0\), and use \(\Gamma(p+1)=p\Gamma(p)\). \(\square\)

**Example 6.3 (the two frequency directions).** On the circle of length \(2\pi\), let \(Q=1-\partial_x^2\). Its eigenvalues are \(1+k^2\), \(k\in\mathbb Z\). Riemann sums give

\[
\sqrt t\sum_{k\in\mathbb Z}e^{-t(1+k^2)}\longrightarrow\int_{\mathbb R}e^{-y^2}dy=\sqrt\pi.
\]

For a rigorous tail estimate, bound each decreasing Gaussian tail by an integral; the central Riemann sum converges uniformly on fixed compact intervals. Formula (6.3), with \(p=1/2\), gives \(\operatorname{Tr}_\omega(Q^{-1/2})=2\). The two signs of the frequency account for the factor two.

## 7. From logarithmic traces to geometry

The classical trace calculation follows after the Fourier and symbol estimates in Classical pseudodifferential traces. Its full proof uses the logarithmic trace constructed here.

## 8. Examples and solved exercises

Exercises 1 and 3 accompany the finite-cutoff construction in Section 2; Exercise 2 tests negligible tails in Section 5. The following problems connect the heat computation to geometry and to the spectral tools in Section 9.

**Exercise 4 (advanced).** Let \(Q=1-\Delta\) on a rectangular flat torus with side lengths \(\ell_1,\ldots,\ell_d\). Compute \(\operatorname{Tr}_\omega(Q^{-d/2})\).

**Solution.** The eigenvalues are \(1+\sum_j(2\pi k_j/\ell_j)^2\). Gaussian Riemann sums, with the same integral tail bound as Example 6.3 in each coordinate, give

\[
\operatorname{Tr}(e^{-tQ})\sim
\frac{\ell_1\cdots\ell_d}{(4\pi t)^{d/2}}.
\]

Apply (6.3) with \(p=d/2\). The value is

\[
\frac{\ell_1\cdots\ell_d}{(4\pi)^{d/2}\Gamma(d/2+1)}.
\]

For \(\ell_j=2\pi\), it is \(\pi^{d/2}/\Gamma(d/2+1)\), the Euclidean volume of the unit ball. The shift by one removes the zero eigenvalue and changes no high-frequency coefficient.

**Exercise 5 (advanced).** Suppose \(Q\geq cI>0\) has heat trace \(At^{-p}+O(t^{-p+\alpha})\), with \(\alpha>0\). Prove that \(\operatorname{Tr}(Q^{-z})\) has a meromorphic continuation to \(\operatorname{Re}z>p-\alpha\), with residue \(A/\Gamma(p)\) at \(z=p\).

**Solution.** Subtract \(At^{-p}\) in the Mellin integral on \(0<t<1\). The remaining integral converges locally uniformly when \(\operatorname{Re}z>p-\alpha\), even after any \(z\)-derivative, since powers of \(|\log t|\) are integrable with a strictly positive exponent margin. The large-\(t\) integral is entire by exponential decay. The subtracted term is \(A/(z-p)\), multiplied by \(1/\Gamma(z)\), giving the stated residue. At \(z=p(1+\epsilon)\), multiplication by \(\epsilon\) produces \(A/\Gamma(p+1)\), consistent with (6.3).

**Exercise 6 (advanced).** Explain why the multiplier
\((1-\Delta_{\mathrm{flat}})^{-n/2}\) on \(L^2(\mathbb R^n)\) does not belong to the compact ideal, although its classical symbol has order \(-n\).

**Solution.** On the Fourier side it is multiplication by the positive function
\((1+|\xi|^2)^{-n/2}\). Choose infinitely many disjoint measurable subsets of a fixed finite ball, all with positive measure, and normalized functions supported on them. These functions are orthonormal; their images remain mutually orthogonal and have norm bounded below by the minimum of the multiplier on that ball. Thus the images have no convergent subsequence. The multiplier is not compact. This shows why compactness of the base, compact localization, or another genuine global condition is necessary before applying a logarithmic compact-operator trace.

**Exercise 7 (intermediate).** Let \(A=\operatorname{diag}(4,1)\) and \(B=\operatorname{diag}(1,3)\). Verify (9.3) for \(p=q=2,r=1\). Decide whether the bound must be an equality, and give a nonzero equality example with those exponents.

**Solution.** The product has singular values \(4,3\), so \(\|AB\|_1=7\), whereas \(\|A\|_2\|B\|_2=\sqrt{17}\sqrt{10}=\sqrt{170}>7\). Equality is not required. Taking \(B=A\) gives \(\|A^2\|_1=17=\|A\|_2^2\); the product-vector and scalar Hölder bounds are both equalities in that case.

**Exercise 8 (intermediate).** On \(\ell^2(\{1,2,3,\ldots\})\), let \(De_j=je_j\). Determine \(\operatorname{Dom}D\). Does \(x_j=1/j\) belong to it? Show that its finite truncations converge in \(H\) but their images under \(D\) do not.

**Solution.** Formula (9.2) gives \(\operatorname{Dom}D=\{x:\sum_jj^2|x_j|^2<\infty\}\). The stated vector belongs to \(H\), because \(\sum j^{-2}<\infty\), but its domain sum is \(\sum1=\infty\). Its truncations have \(H\) tails with squared norm \(\sum_{j>N}j^{-2}\to0\). Their \(D\)-images have entries one through the cutoff, so the squared distance between cutoffs \(M>N\) is \(M-N\). They are not Cauchy. Graph convergence is the essential condition in Lemma 9.2.

**Exercise 9 (advanced).** In (9.6), take three heat lengths \(1/2,0,1/2\). Identify the Schatten exponents and show why the zero interval does not invalidate the estimate.

**Solution.** The two nontrivial heat factors have exponent two and norm \((\operatorname{Tr}e^{-uD^2})^{1/2}\). The middle heat factor is the identity, with exponent infinity and norm one. Bounded coefficients can be included as infinite-exponent factors. Iterated Hölder gives a trace-norm bound equal to the product of coefficient norms times \(\operatorname{Tr}e^{-uD^2}\). The reciprocal exponents add to \(1/2+0+1/2=1\), exactly as required. No negative power of a heat length is introduced.

<a id="spectral-decomposition-and-schatten-estimates"></a>
<a id="9-spectral-and-ideal-facts-behind-the-estimates"></a>

## 9. Spectral decomposition and Schatten estimates

These supporting proofs can be read at their points of use. Lemma 9.1 supplies the decomposition needed in Section 1; Lemma 9.2 supplies the eigenbasis used in the heat calculation; Lemma 9.4 constructs the states used in Section 4. Theorem 9.3 uses the rank-approximation formula (1.1), but neither logarithmic traces nor the Tauberian argument, and supplies the precise product estimate for later heat brackets. The elementary Hilbert facts in our entry base include orthogonal projections, adjoints, Parseval for an orthonormal basis, and completeness. The positive bounded functional calculus is the interval construction AN03-SPC-003 in [Positive spectral calculus](../../elliptic-boundary-reduction/lower-bounded-spectral-calculus.html#the-full-calculus-of-a-bounded-positive-contraction): its proof starts with Bernstein polynomials, constructs scalar measures and bounded Borel operators, and proves multiplicativity. It does not assume the compact spectral theorem. Its injectivity premise loses no bounded positive operators: split off the kernel, apply the construction to its invariant orthogonal complement after rescaling to a contraction, and let a function act by its value at zero on the kernel. Continuous functions, including the positive square root, are uniform polynomial limits, so they commute with every operator commuting with the given positive operator.

<a id="compact-positive-operators"></a>

**Lemma 9.1 (compact positive operators).** A positive compact operator \(K\) has an orthonormal basis of its kernel and its positive eigenspaces. Its nonzero eigenvalues have finite multiplicity and tend to zero if there are infinitely many.

**Proof.** Positivity of the form \(\langle Kx,y\rangle\) and scalar quadratic minimization give
\[
|\langle Kx,y\rangle|^2\leq\langle Kx,x\rangle\langle Ky,y\rangle .
\]
Writing \(a=\sup_{\|x\|=1}\langle Kx,x\rangle\), taking the supremum over unit \(y\) proves
\(\|Kx\|^2\leq a\langle Kx,x\rangle\). Thus \(a=\|K\|\).
If \(a>0\), choose unit \(x_j\) with \(\langle Kx_j,x_j\rangle\to a\). Then
\[
\|(K-a)x_j\|^2
\leq a^2-a\langle Kx_j,x_j\rangle\longrightarrow0.
\tag{9.1}
\]
Compactness gives a convergent subsequence of \(Kx_j\); (9.1) then gives convergence of that subsequence of \(x_j\) to a unit eigenvector with eigenvalue \(a\).

The orthogonal complement of an eigenspace is invariant under \(K\), by selfadjointness. Repeat the construction there. An infinite orthonormal family of eigenvectors with eigenvalues bounded below by \(\varepsilon>0\) would have images at pairwise distance at least \(\sqrt2\varepsilon\), contradicting compactness. This proves finite multiplicity away from zero and convergence of the selected eigenvalues to zero. If \(K\) were nonzero on the orthogonal complement of all selected eigenspaces, the same maximum argument would produce a positive eigenvalue there. Every previously selected maximum would be at least that value, giving the contradiction just proved. The remaining complement is therefore the kernel. Choose an orthonormal basis in that closed subspace. This proves the result, including finite rank and \(K=0\). \(\square\)

Apply this to \(T^*T\) for compact \(T\). On an eigenvector with eigenvalue \(\mu^2>0\), put \(Ve=T e/\mu\). These images are orthonormal, since
\(\langle Te,Tf\rangle=\langle T^*Te,f\rangle\). Extend \(V\) by zero on the kernel. It is a partial isometry and \(T=V|T|\), where \(|T|\) multiplies those eigenvectors by \(\mu\). This is the compact polar decomposition used in Section 1.

<a id="compact-resolvent-spectral-core"></a>

**Lemma 9.2 (a compact-resolvent spectral core).** A selfadjoint \(D\) with compact resolvent has an orthonormal eigenbasis \((e_j)\), with real eigenvalues \(d_j\). Each bounded interval contains only finitely many eigenvalues, counted with multiplicity, and
\[
\operatorname{Dom}D
=\left\{x:\sum_j |d_j|^2|\langle x,e_j\rangle|^2<\infty\right\}.
\tag{9.2}
\]
Finite spectral sums are dense in this domain with its graph norm.

**Proof.** For either sign,
\(\|(D\pm i)x\|^2=\|Dx\|^2+\|x\|^2\). The range is closed, using closedness of \(D\), and its orthogonal complement is \(\ker(D\mp i)=0\), using the adjoint definition. Thus \(D\pm i\) are bijective with bounded inverses. Their resolvent identity shows that these inverses commute. Put
\[
R=(D-i)^{-1}(D+i)^{-1}.
\]
Then \(R=(D+i)^{-1*}(D+i)^{-1}\) is positive, injective and compact. The identity \(D(D\pm i)^{-1}=I\mp i(D\pm i)^{-1}\) shows that its range is exactly \(\operatorname{Dom}D^2\) and that \(R=(1+D^2)^{-1}\) there.

Lemma 9.1 decomposes \(H\) into the finite-dimensional positive eigenspaces of \(R\); there is no kernel. Every such eigenspace lies in \(\operatorname{Dom}D^2\). The resolvent identities imply \(DRx=RDx\) for \(x\in\operatorname{Dom}D\), so \(D\) preserves each of them. Its restriction is a Hermitian matrix; finite-dimensional diagonalization gives a real eigenbasis. If \(De_j=d_je_j\), then \(Re_j=(1+d_j^2)^{-1}e_j\). Compactness of \(R\) proves the bounded-interval assertion.

For \(x\in\operatorname{Dom}D\), selfadjointness gives the coordinate of \(Dx\) as \(d_j\langle x,e_j\rangle\), so (9.2) is necessary by Parseval. Conversely that condition makes the images of the finite partial sums converge in \(H\). Closedness of \(D\) puts their limit in its domain and identifies its image with that coordinate sequence. The same argument proves graph density. Every scalar function of \(D\) consequently has its indicated square-sum domain, and the spectral cutoffs used in the next lessons converge in every graph norm on which the vector belongs. \(\square\)

For \(0<p<\infty\), define
\[
\mathcal S^p=\{T\text{ compact}:\sum_j\mu_j(T)^p<\infty\},
\qquad \|T\|_p=\left(\sum_j\mu_j(T)^p\right)^{1/p}.
\]
Use \(\mathcal S^\infty=B(H)\) and \(\|T\|_\infty=\|T\|\). We need normed ideals for \(p\geq1\); the product estimate itself also makes sense below one.

<a id="schatten-holder"></a>

**Theorem 9.3 (Schatten Hölder).** If \(0<p,q,r\leq\infty\) and
\(1/r=1/p+1/q\), with \(1/\infty=0\), then
\[
\|AB\|_r\leq\|A\|_p\|B\|_q.
\tag{9.3}
\]
At least one finite exponent ensures compactness of the product. When both exponents are infinite, (9.3) is ordinary operator submultiplicativity.

**Proof.** First use finite-rank operators in a common finite-dimensional space. On its \(k\)-th exterior power, the singular decomposition gives
\[
\|\wedge^kT\|=\prod_{j<k}\mu_j(T),\qquad
\wedge^k(AB)=(\wedge^kA)(\wedge^kB).
\]
Indeed the wedge products of distinct orthonormal singular vectors form orthonormal systems, and the largest coefficient is the product of the \(k\) largest singular values. Operator submultiplicativity therefore yields
\[
\prod_{j<k}\mu_j(AB)\leq
\prod_{j<k}\mu_j(A)\mu_j(B)\qquad(k\geq1).
\tag{9.4}
\]

Here is the precise passage from products to sums. If decreasing real vectors \(u,v\) satisfy \(\sum_{j<k}u_j\leq\sum_{j<k}v_j\) for every \(k\), then for every real \(t\)
\[
\sum_j(u_j-t)_+
=\max_{k\geq0}\sum_{j<k}(u_j-t)
\leq\max_{k\geq0}\sum_{j<k}(v_j-t)
=\sum_j(v_j-t)_+.
\]
For \(r>0\), multiply by \(r^2e^{rt}\) and integrate over \(t\in\mathbb R\). The identity
\(\int_{-\infty}^w r^2e^{rt}(w-t)\,dt=e^{rw}\) proves
\(\sum_j e^{ru_j}\leq\sum_j e^{rv_j}\).
Apply this to
\(u_j=\log\mu_j(AB)\), \(v_j=\log(\mu_j(A)\mu_j(B))\), using (9.4).
Zeros cause no difficulty: discard the zero tail of the latter product vector, on which the product has rank zero by the rank inequality; replace any remaining zero in the former vector by a sufficiently small positive number. All prefix inequalities still hold, and passage of that number to zero gives
\[
\sum_j\mu_j(AB)^r
\leq\sum_j(\mu_j(A)\mu_j(B))^r.
\tag{9.5}
\]

If \(p,q\) are finite, ordinary sequence Hölder with exponents \(p/r,q/r\) bounds the right side by \(\|A\|_p^r\|B\|_q^r\).
To recall its proof, normalize the two nonnegative power sums to one and apply
\(ab\leq a^P/P+b^Q/Q\), \(1/P+1/Q=1\), term by term. This scalar inequality follows by minimizing \(a^P/P-ab+b^Q/Q\) in \(a\). Zero norms are immediate.

Finite-rank singular truncations \(A_n,B_n\) converge in operator norm and in their respective finite-exponent quantities. Their products converge in operator norm to \(AB\). Formula (1.1) gives
\(|\mu_j(S)-\mu_j(T)|\leq\|S-T\|\), so each product singular value converges. Taking every finite partial sum in (9.5) and then its supremum proves (9.3) for compact \(A,B\).
For a bounded factor, (1.1) gives directly
\(\mu_j(AB)\leq\|A\|\mu_j(B)\) and
\(\mu_j(BA)\leq\|A\|\mu_j(B)\), by multiplying finite-rank approximants. These prove the infinite-exponent cases. \(\square\)

Iteration gives the corresponding estimate for any finite product, including bounded factors. In particular, if \(s_j\geq0\), \(\sum_j s_j=1\), and \(e^{-uD^2}\) is trace class, then
\[
\left\|a_0e^{-us_0D^2}a_1e^{-us_1D^2}\cdots
 a_ne^{-us_nD^2}\right\|_1
\leq\left(\prod_{j=0}^n\|a_j\|\right)
 \operatorname{Tr}(e^{-uD^2}).
\tag{9.6}
\]
For \(s_j>0\), its heat factor has Schatten exponent \(1/s_j\) and norm
\((\operatorname{Tr}e^{-uD^2})^{s_j}\). For \(s_j=0\), it is the identity with operator norm one. Thus (9.6) holds also on the boundary of the simplex, with constant one. This is the estimate required in the heat cocycle.

For completeness, \(\mathcal S^p\) is a Banach ideal when \(1\leq p<\infty\). Hölder and bounded trace duality give
\[
\|T\|_p=\sup_{\substack{X\text{ finite rank}\\\|X\|_{p'}\leq1}}
 |\operatorname{Tr}(TX)|,\qquad 1/p+1/p'=1.
\tag{9.7}
\]
For the reverse inequality when \(p>1\), take \(T=V|T|\) and test with
\(|T|^{p-1}P_N V^*/(\sum_{j<N}\mu_j(T)^p)^{1/p'}\); let \(N\to\infty\). For \(p=1\), test with \(P_NV^*\). Zero partial sums are omitted. Formula (9.7) proves the triangle inequality. A Cauchy sequence in this norm is Cauchy in operator norm and has a compact operator limit. Continuity of each singular value and finite partial sums show
\(\|T-T_n\|_p\leq\liminf_m\|T_m-T_n\|_p\), which proves convergence in the ideal norm and completeness. Bounded left and right multiplication obey (9.3). These facts justify the trace-norm integrals and approximations later in the course.

<a id="extension-used-to-construct-a-state"></a>

**Lemma 9.4 (the extension used to construct a state).** A bounded real linear functional on a subspace of a real normed space has an extension with the same norm. In particular, the ordinary limit on convergent sequences extends to a positive unital complex functional of norm one on \(\ell^\infty\).

**Proof.** The norm-preserving extension theorem is proved in [Banach foundations](../../elliptic-boundary-reduction/banach-foundation-bridges.html#hahnbanach-and-scalar-norm-tests), Section 5. Its proof uses the explicitly stated Zorn choice principle and a one-dimensional extension interval; no completeness or closedness of the subspace is required. Apply its real form to the limit functional on real convergent sequences. We prove the additional positivity and quotient-state adapter here.

For the limit functional \(l\) on real convergent sequences, this gives \(l(1)=\|l\|=1\) on real \(\ell^\infty\). If \(0\leq x\leq1\), then
\(l(x)=1-l(1-x)\geq0\); rescaling proves positivity for every bounded nonnegative sequence. Complexify by
\(L(x+iy)=l(x)+il(y)\). This is complex linear and positive. If \(L(z)\ne0\), choose a scalar \(c\) of modulus one with \(cL(z)=|L(z)|\). Then
\[
|L(z)|=l(\operatorname{Re}(cz))\leq\|z\|_\infty.
\]
Thus its complex norm is one and it extends the complex ordinary limit. Composition with sequence evaluation gives the quotient states used in Section 4. The same choice principle also permits the algebraic basis extensions used for residue cochains later in the course; it supplies existence without a continuity assertion. \(\square\)

## References

- [Lord–Sukochev 2010] Steven Lord and Fedor Sukochev, *Measure Theory in Noncommutative Spaces*, SIGMA 6 (2010), 072, 36 pages; [exact arXiv v1](https://arxiv.org/abs/1009.3095v1), [readable text](https://arxiv.org/html/1009.3095v1). Its Introduction discusses the normality of functionals defined by Dixmier traces.

- [Carey–Rennie–Sedaev–Sukochev 2006] Alan L. Carey, Adam Rennie, Aleksandr Sedaev, and Fedor A. Sukochev, *The Dixmier trace and asymptotics of zeta functions*, [open preprint](https://arxiv.org/abs/math/0611629).
- [Connes–Moscovici 1995] Alain Connes and Henri Moscovici, *The local index formula in noncommutative geometry*, Geometric and Functional Analysis 5 (1995), 174–243; [IHÉS preprint](https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/CONNES/1994-1998/M_95_19/M_95_19.pdf).
- [Dixmier 1966] Jacques Dixmier, *Existence de traces non normales*, Comptes Rendus de l’Académie des Sciences de Paris, Série A–B 262 (1966), A1107–A1108.
- [Positive spectral calculus](../../elliptic-boundary-reduction/lower-bounded-spectral-calculus.html#the-full-calculus-of-a-bounded-positive-contraction) *Spectral measures with the original operator domain retained*, Elliptic Operators & Boundary Problems, AN03-P005, especially AN03-SPC-001–004; [proof source](../../elliptic-boundary-reduction/src/lower-bounded-spectral-calculus.md). Independently written programme proof, CC0. Sections 1–4 retain the full spectral measure and operator-domain statements.

- [Banach foundations](../../elliptic-boundary-reduction/banach-foundation-bridges.html#hahnbanach-and-scalar-norm-tests) *Banach estimates, quotient spaces and compact parameter arguments*, Elliptic Operators & Boundary Problems, AN03-P004, Sections 4–8, reader-facing draft dated September 2026. Independently written programme proof, CC0. Sections 4–8 include the complete-metric Baire theorem and the full Banach-space consequences.
