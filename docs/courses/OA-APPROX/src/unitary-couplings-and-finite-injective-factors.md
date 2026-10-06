# Unitary couplings and finite injective factors

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Self-checked by the writing AI. New original text: public domain (CC0).*

A balanced family can approximately intertwine two tuples of unitaries without containing a single unitary. We will first sample finitely many intertwiners, bound their operator norms without increasing their errors, and pass to an ultrapower. Exact intertwiners there equate two corner dimensions. Projection comparison gives a unitary, and a unitary representative returns the desired approximation to the original algebra.

We use the [balanced coupling construction](balancing-kraus-families-and-unitary-couplings.md), the [von Neumann multiplier ultrapower](multiplier-ultraproducts-and-normal-embeddings.md#theorem-3-2), canonical center-valued trace comparison and finite polar decomposition. In a faithfully tracial algebra every bounded sequence is a multiplier: \(\|axb\|_2\le\|a\|\|b\|\|x\|_2\). Thus its ultrapower is the quotient of all bounded sequences by those with vanishing ultralimit \(2\)-norm, and its faithful normal state is a trace. Factoriality of the ultrapower is unnecessary for the proof below.

Sections 1–4 allow every finite von Neumann algebra \(M\) with a faithful normal tracial state \(\tau\); separability is unnecessary. The final application to injectivity uses a \(\mathrm{II}_1\) factor. Separable predual is assumed only for a generating sequence and the identification with \(R\).

## 1. Sampling a countable coupling

Suppose \((u_k)_{k=1}^n\) and \((v_k)_{k=1}^n\) are \(\delta\)-related, in the terminology of the preceding lesson, with \(n\ge1\) and \(\delta>0\). Thus
\[
\sum_i a_i^*a_i=\sum_i a_i a_i^*=1,
\qquad \sum_i\|a_i u_k-v_k a_i\|_2^2<\delta.
\tag{1}
\]

**Lemma 1.1.** For every integer \(r\ge1\), there are \(b_1,\ldots,b_r\in M\) such that
\[
\left\|\sum_i b_i^*b_i-1\right\|_2^2<\frac9r,
\qquad
\left\|\sum_i b_i b_i^*-1\right\|_2^2<\frac9r,
\qquad
\sum_i\|b_i u_k-v_k b_i\|_2^2<3n\delta.
\tag{2}
\]

**Proof.** Choose \(p\) with \(\tau(A)>1-1/r\), where
\[
A=\sum_{i=1}^p a_i^*a_i\le1,\qquad
B=\sum_{i=1}^p a_i a_i^*\le1.
\tag{3}
\]
Their scalar traces agree. Give \(\Omega=\mathbb T^p\) its product probability measure, with coordinate phases \(s_i\), and put \(b(s)=\sum_{i=1}^p s_i a_i\). Orthogonality of the phases gives
\[
\mathbb E(b^*b)=A,\qquad \mathbb E(bb^*)=B,
\qquad \mathbb E\|bu_k-v_kb\|_2^2<\delta.
\tag{4}
\]
The fourth moment has an exact noncommuting expansion:
\[
\mathbb E((b^*b)^2)
=A^2+\sum_i a_i^*B a_i-\sum_i(a_i^*a_i)^2\le 2\,1.
\tag{5}
\]
Indeed \(\mathbb E(\overline{s_i}s_j\overline{s_\ell}s_t)\) is nonzero exactly when the two multisets \(\{i,\ell\}\) and \(\{j,t\}\) agree. The two pairings give the first two terms in (5); the all-equal pairing is counted twice and must be subtracted once. The bounds \(A,B\le1\) prove the inequality. Exchanging \(a_i\) with \(a_i^*\) gives \(\mathbb E((bb^*)^2)\le2\,1\) as well.

For \(r\) independent samples, let
\(A_r=r^{-1}\sum_{j=1}^r b(s^{(j)})^*b(s^{(j)})\). Independence and (5) yield
\[
\mathbb E\tau(A_r^2)
=\frac1r\tau(\mathbb E((b^*b)^2))
+\frac{r-1}{r}\tau(A^2)\le1+\frac1r,
\qquad
\mathbb E\tau(A_r)=\tau(A)>1-\frac1r.
\]
Consequently \(\mathbb E\|A_r-1\|_2^2<3/r\). The same estimate holds for the averaged reversed products. Each averaged coupling energy has expectation less than \(\delta\).

Markov's inequality bounds the probabilities of the first two failures in (2) by numbers strictly below \(1/3\) each, and the probability of each energy failure by a number strictly below \(1/(3n)\). Their union has probability less than \(1\). Choose a sample outside it and put \(b_j=r^{-1/2}b(s^{(j)})\). This gives all the inequalities simultaneously. \(\square\)

## 2. Clipping without increasing intertwining errors

We need operator-norm bounds independent of the small coupling parameter. The following trace Hilbert-space fact supplies them.

**Lemma 2.1.** If \(f:\mathbb R\to\mathbb R\) is Lipschitz with constant \(1\), then for bounded self-adjoint \(H,K\) in a faithfully tracial finite algebra,
\[
\|f(H)-f(K)\|_2\le\|H-K\|_2.
\tag{6}
\]

**Proof.** First suppose \(H=\sum_i\lambda_i p_i\), \(K=\sum_j\mu_j q_j\) have finite spectra. The weights \(\tau(p_iq_j)\) are nonnegative, because they equal \(\tau(q_jp_iq_j)\). Expanding squares and using both projection partitions gives
\[
\|f(H)-f(K)\|_2^2
=\sum_{i,j}(f(\lambda_i)-f(\mu_j))^2\tau(p_iq_j)
\le\sum_{i,j}(\lambda_i-\mu_j)^2\tau(p_iq_j)
=\|H-K\|_2^2.
\tag{7}
\]
Uniform spectral approximations to \(H,K\) converge in operator norm, as do their continuous functional calculi on the common bounded spectral interval. Passing to the limit proves (6). The projections from different partitions need not commute. \(\square\)

**Lemma 2.2.** For every \(r\ge1\), the coupled tuples have operators \(c_1,\ldots,c_r\) satisfying
\[
\|c_i\|\le\sqrt r,
\qquad
\left\|\sum_i c_i^*c_i-1\right\|_2^2<\frac{18}{r},
\qquad
\left\|\sum_i c_i c_i^*-1\right\|_2^2<\frac{18}{r},
\qquad
\sum_i\|c_i u_k-v_k c_i\|_2^2<3n\delta.
\tag{8}
\]

**Proof.** For \(r=1\), take \(c_1=0\). Now let \(r\ge2\), choose the \(b_i\)'s from Lemma 1.1 and put
\[
g(t)=\begin{cases}1,&0\le t\le r,\\ \sqrt{r/t},&t>r,\end{cases}
\quad h(t)=tg(t)^2=\min(t,r),
\quad c_i=b_i g(b_i^*b_i)=g(b_i b_i^*)b_i.
\tag{9}
\]
Polar decomposition proves the last equality. Also \(c_i^*c_i=h(b_i^*b_i)\), \(c_i c_i^*=h(b_i b_i^*)\), so \(\|c_i\|\le\sqrt r\).

Set \(A=\sum_i b_i^*b_i\) and \(C=\sum_i c_i^*c_i\le A\). For scalar \(t\ge0\),
\[
0\le t-h(t)\le\frac1{2r}(t-1)_+^2.
\tag{10}
\]
For \(t>r\), the difference between the right numerator and \(2r(t-r)\) is \((t-r-1)^2+r(r-2)\ge0\); for \(t\le r\) the left side is zero.

We also need trace monotonicity: if \(0\le X\le Y\), then
\[
\tau((X-1)_+^2)\le\tau((Y-1)_+^2).
\tag{11}
\]
To prove it without an operator-monotonicity assumption, use
\[
\tau((X-1)_+^2)
=\sup_{z\in M_+}\bigl(2\tau(z(X-1))-\tau(z^2)\bigr).
\tag{12}
\]
The expression is at most \(\tau((X-1)_+^2)\) by \(X-1\le(X-1)_+\) and completing the trace square; equality is attained at \(z=(X-1)_+\). Positivity of the trace of a product of positives proves (11).

Apply (10)–(11) to each \(b_i^*b_i\le A\). Summing gives
\[
\tau(A-C)\le\tfrac12\|A-1\|_2^2.
\tag{13}
\]
Since \(C\le A\), \(\tau(C^2)\le\tau(A^2)\): their difference is \(\tau((A-C)(A+C))\ge0\). Therefore
\[
\|C-1\|_2^2
\le\|A-1\|_2^2+2\tau(A-C)
\le2\|A-1\|_2^2<18/r.
\tag{14}
\]
The reversed products have the same proof.

Finally use the real clipping function \(f(t)=\max(-\sqrt r,\min(t,\sqrt r))\). In \(N=M_2\bar\otimes M\), with its normalized product trace, set
\[
H_i=\begin{pmatrix}0&b_i^*\\b_i&0\end{pmatrix},
\qquad s_k=\begin{pmatrix}u_k&0\\0&v_k\end{pmatrix}.
\tag{15}
\]
Functional calculus gives \(f(H_i)=\left(\begin{smallmatrix}0&c_i^*\\c_i&0\end{smallmatrix}\right)\). Direct computation of the two block entries gives
\[
\|H_i-s_kH_i s_k^*\|_{2,N}^2=\|b_i u_k-v_kb_i\|_2^2.
\tag{16}
\]
The corresponding identity for \(f(H_i)\) has \(c_i\) in place of \(b_i\). Equation (6) and covariance of functional calculus under unitary conjugation show that each clipped error is no larger than its original error. Summing proves the final bound in (8). \(\square\)

## 3. Unitary representatives in a finite ultrapower

**Lemma 3.1.** Every unitary of \(M^\omega\) has a representative consisting of unitaries of \(M\).

**Proof.** Take a bounded representative \((x_j)\). Unitarity in the quotient implies \(\|x_j^*x_j-1\|_2\to_\omega0\). Extend each polar partial isometry to a unitary \(w_j\in M\), so \(x_j=w_j|x_j|\). This extension is possible in a finite algebra: the two support projections are equivalent, hence have equal center-valued traces, and their complements are equivalent by projection comparison. Add a partial isometry between those complements.

For \(t\ge0\), \(|t-1|\le|t^2-1|\). Thus
\[
\|x_j-w_j\|_2=\||x_j|-1\|_2
\le\|x_j^*x_j-1\|_2\longrightarrow_\omega0.
\tag{17}
\]
The sequence \((w_j)\) represents the same unitary. \(\square\)

## 4. Small coupling energy gives unitary conjugation

**Theorem 4.1.** For a fixed faithfully tracial finite algebra \(M\), every integer \(n\ge1\) and \(\varepsilon>0\), there is \(\delta>0\) such that any \(\delta\)-related tuples \((u_k)\), \((v_k)\) in \(M\) have a unitary \(w\in M\) with
\[
\|u_k-wv_kw^*\|_2<\varepsilon\qquad(1\le k\le n).
\tag{18}
\]
The modulus need not be specified explicitly. Neither factoriality nor separability is assumed.

**Proof.** If the assertion fails, choose \(\delta_j\downarrow0\) and \(\delta_j\)-related tuples \((u_k(j))\), \((v_k(j))\) such that
\[
\max_k\|z u_k(j)-v_k(j)z\|_2\ge\varepsilon
\quad\hbox{for every }z\in\mathcal U(M)\hbox{ and every }j.
\tag{19}
\]
Choose a free ultrafilter \(\omega\) and let \(U_k,V_k\) be the corresponding unitary classes in \(M^\omega\). In \(N=M_2\bar\otimes M^\omega\), put
\[
s_k=\begin{pmatrix}U_k&0\\0&V_k\end{pmatrix},
\qquad P=\{s_1,\ldots,s_n\}'\cap N.
\tag{20}
\]
This is a finite von Neumann algebra with the faithful normal restriction of \(\tau_N=\tau_2\otimes\tau^\omega\). The coordinate projections \(E_{11},E_{22}\) belong to \(P\).

For each fixed integer \(r\), Lemma 2.2 gives \(c_1(j),\ldots,c_r(j)\) bounded in operator norm by \(\sqrt r\), for every \(j\). They therefore define classes \(C_i\in M^\omega\). Their coupling errors have ultralimit zero, so \(C_iU_k=V_kC_i\). The operators
\[
D_i=\begin{pmatrix}0&0\\C_i&0\end{pmatrix}
\tag{21}
\]
belong to \(P\), and (8) gives
\[
\left\|\sum_iD_i^*D_i-E_{11}\right\|_{2,N}^2\le9/r,
\qquad
\left\|\sum_iD_iD_i^*-E_{22}\right\|_{2,N}^2\le9/r.
\tag{22}
\]
For any central projection \(z\in P\), traciality and \(zD_i=D_i z\) give
\(\tau_N(z\sum_iD_i^*D_i)=\tau_N(z\sum_iD_iD_i^*)\). Cauchy–Schwarz in (22) consequently yields
\[
|\tau_N(zE_{11})-\tau_N(zE_{22})|\le6/\sqrt r.
\tag{23}
\]
The left side is independent of \(r\), so it is zero. Testing all central projections, and then the positive and negative spectral projections of their center-valued trace difference, proves
\(\mathcal T_P(E_{11})=\mathcal T_P(E_{22})\). Faithfulness of \(\tau_N|_P\) justifies that last implication. Finite projection comparison in \(P\) gives a partial isometry \(W\in P\) with \(W^*W=E_{11}\), \(WW^*=E_{22}\).

These supports force \(W=\left(\begin{smallmatrix}0&0\\w&0\end{smallmatrix}\right)\), with \(w\) unitary in \(M^\omega\). Its membership in \(P\) says \(wU_k=V_kw\). Lemma 3.1 gives unitary representatives \(w_j\in M\), and hence
\[
\|w_j u_k(j)-v_k(j)w_j\|_2\longrightarrow_\omega0
\quad(1\le k\le n).
\tag{24}
\]
There are only finitely many \(k\), so an \(\omega\)-large set satisfies all these errors below \(\varepsilon\). This contradicts (19). Taking the adjoint of the implementing unitary converts the intertwining form into (18). \(\square\)

Equation (22) bounds squared norms. Taking square roots gives (23). The proof uses its decay to zero, not the faster rate that would result from dropping that square root.

## 5. Injective finite factors are locally AFD

**Theorem 5.1.** Every injective \(\mathrm{II}_1\) factor is locally approximately finite dimensional. If its predual is separable, it has a generating increasing dyadic sequence and is isomorphic to the tracial infinite product \(R\).

**Proof.** Fix a finite tuple of unitaries \(u_k\) and an error \(\varepsilon>0\). Theorem 4.1 gives a coupling threshold \(\delta\). The preceding lesson supplies a matrix subfactor \(D\subset M\) and unitary models \(v_k\in D\) which are \(\delta\)-related to \(u_k\). Equation (18) approximates every \(u_k\) inside the actual finite-dimensional subalgebra \(wDw^*\).

Every element is a finite linear combination of at most four unitaries, as shown in the trace-preserving model lesson. Apply the tuple argument to all unitary summands in a finite set with an error budget divided by their coefficient sums. The resulting approximants have an operator-norm bound independent of the shrinking budget. Bounded \(2\)-norm convergence for a faithful normal trace is \(\sigma\)-strong* convergence; thus this is local AFD in the von Neumann sense.

For separable predual, the [finite-factor exact containment and uniqueness theorem](hyperfinite-finite-factors.md#theorem-5-1) converts local approximation into a generating increasing dyadic matrix sequence. Its compatible trace-GNS identification gives \(M\cong R\). No uniqueness theorem for injective factors was assumed in obtaining the local approximation. \(\square\)

**Corollary 5.2.** Every separable injective \(\mathrm{II}_\infty\) factor is isomorphic to \(R\bar\otimes B(\ell^2)\).

**Proof.** The [semifinite matrix decomposition](masas-in-expected-semifinite-subfactors.md#3-splitting-the-semifinite-case) gives \(M\cong eMe\bar\otimes B(\ell^2)\) for a nonzero finite projection \(e\). Corner permanence of injectivity makes \(eMe\) injective, and it is a \(\mathrm{II}_1\) factor with separable predual. Theorem 5.1 identifies it with \(R\). The matrix decomposition uses countable projection comparison, independently of the finite injective-to-AFD result. \(\square\)

This also supplies the finite-corner input for the AFD \(\mathrm{II}_\infty\) MASA regularity branch: AFD implies injective, an injective finite corner is AFD by Theorem 5.1, and the previously proved finite regularity construction applies. The nonfactor conclusion is proved in [Central disintegration and measurable matrix assembly](central-disintegration-and-measurable-matrix-assembly.md) and [Injective algebras and separable tracial envelopes](injective-algebras-and-separable-tracial-envelopes.md). The separate [second finite proof](small-corners-and-the-second-injective-proof.md) reaches the same factor conclusion through finite-rank models and repaired small corners.

## 6. Problems with complete solutions

**Exercise 1.** Explain the subtraction term in the phase moment (5).

*Solution.* The index conditions \(i=j,\ell=t\) and \(i=t,\ell=j\) each yield a surviving phase average. When all four indices agree, both conditions count the same term. Subtracting \(\sum_i(a_i^*a_i)^2\) removes the second copy and leaves every surviving term counted exactly once. Noncommuting operator products retain their original order.

**Exercise 2.** Check why the simultaneous good-sample set has positive measure.

*Solution.* The two positive-sum failures each have probability strictly below \(1/3\). The \(n\) energy failures each have probability strictly below \(1/(3n)\). The union bound therefore gives total failure probability strictly below \(2/3+n/(3n)=1\). Its complement has positive measure and contains a sample realizing all inequalities in (2).

**Exercise 3.** Verify (10) when \(r=2\).

*Solution.* For \(t\le2\), its left side is zero. For \(t>2\), the inequality is \(t-2\le(t-1)^2/4\). Subtracting \(4(t-2)\) from \((t-1)^2\) gives \((t-3)^2\ge0\). Equality occurs at \(t=3\); the bound is valid without changing its constant.

**Exercise 4.** Why may (11) be used although \(t\mapsto(t-1)_+^2\) is not assumed operator monotone?

*Solution.* Equation (12) proves monotonicity of its scalar trace value. If \(X\le Y\), then \(\tau(z(X-1))\le\tau(z(Y-1))\) for every \(z\ge0\), because the trace of \(z(Y-X)\) is nonnegative. Taking suprema gives (11). It asserts no operator inequality between the two functional-calculus values.

**Exercise 5.** Why are the weights in (7) nonnegative even when \(p_i,q_j\) do not commute?

*Solution.* Traciality gives \(\tau(p_iq_j)=\tau(q_jp_iq_j)\). The sandwich \(q_jp_iq_j\) is positive, so its trace is nonnegative. Expanding the two finite spectral squares uses these weights and the trace, without multiplying the projection partitions as if they commuted.

**Exercise 6.** Explain why the bound \(\|c_i(j)\|\le\sqrt r\) is needed in Theorem 4.1.

*Solution.* For fixed \(r\), it makes each coordinate sequence \((c_i(j))_j\) an element of the bounded sequence algebra defining \(M^\omega\). A bound only on its trace \(2\)-norm would not give such an element: operators can have large norms on small projections. Lemma 2.2 retains the small intertwining errors while supplying the required uniform operator bound.

**Exercise 7.** Recover the normalization \(9/r\) in (22).

*Solution.* The initial defect is block diagonal with upper-left entry \(\sum_iC_i^*C_i-1\) and lower-right entry zero. The normalized product trace assigns the upper block weight \(1/2\). Its squared \(2\)-norm is therefore half the corresponding squared norm in \(M^\omega\), at most \((1/2)(18/r)=9/r\). The final defect is the same computation in the lower block.

**Exercise 8.** Derive (23) using both defects in (22).

*Solution.* Each defect has \(2\)-norm at most \(3/\sqrt r\). Pairing it with a central projection \(z\) changes its trace by at most that number, since \(\|z\|_2\le1\). The two middle sums have the same pairing with \(z\) by traciality and centrality. The triangle inequality therefore gives total difference at most \(6/\sqrt r\), which tends to zero.

**Exercise 9.** What is needed to turn equality of all central projection pairings into projection equivalence in \(P\)?

*Solution.* The canonical center-valued trace satisfies \(\tau_N(zE_{ii})=\tau_N(z\mathcal T_P(E_{ii}))\). Its self-adjoint difference has zero pairing with every central projection. Its positive and negative spectral projections and faithfulness of the trace force the difference to vanish. The finite projection comparison theorem then makes \(E_{11}\) and \(E_{22}\) equivalent inside \(P\). Equality of their total scalar traces alone would not suffice in a nonfactor \(P\).

**Exercise 10.** Distinguish the hypotheses of Theorem 5.1's local and sequential conclusions.

*Solution.* Local AFD follows for every injective \(\mathrm{II}_1\) factor, using its faithful normalized trace and finite unitary tests. To choose a countable dense list for a generating matrix sequence, the proof assumes separable predual. That sequence has the tracial dyadic product identification with \(R\). The local conclusion therefore does not supply a countable sequence or an isomorphism with separable \(R\) for a factor with nonseparable predual.

## References and proof scope

Uffe Haagerup, [*A new proof of the equivalence of injectivity and hyperfiniteness for factors on a separable Hilbert space*](https://doi.org/10.1016/0022-1236(85)90002-3), *Journal of Functional Analysis* 62 (1985), 160–201. Section 4 and Theorem 5.3 develop sampling, clipping and the ultrapower comparison method. Sections 1–4 here give complete arguments for arbitrary faithfully tracial finite algebras. They include the trace-Hilbert Lipschitz inequality, the finite unitary lift and the square-root bound in the central trace comparison; factoriality of the ultrapower is unnecessary. The AFD application retains the factor hypothesis of balanced reconstruction, and its generating sequence retains separable predual.

The declared programme lemma *Uniqueness of the injective II₁ factor*, Lemma 2.3, has the same polar unitary lifting argument at factor generality. Its later flip/McDuff route is a different proof. The general nonfactor conclusion is completed in [Central disintegration and measurable matrix assembly](central-disintegration-and-measurable-matrix-assembly.md). [Small corners and the second injective proof](small-corners-and-the-second-injective-proof.md) develops the other finite approach, with Repairing small matrix corners supplying its corner correction.
