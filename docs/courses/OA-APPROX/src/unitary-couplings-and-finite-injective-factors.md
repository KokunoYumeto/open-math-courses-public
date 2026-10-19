# Unitary couplings and finite injective factors

*AI-generated exposition by OpenAI GPT models. CC0-1.0 to the extent of rights held.*

A balanced family can approximately intertwine two tuples of unitaries without containing a single unitary. We will first sample finitely many intertwiners, bound their operator norms without increasing their errors, and pass to an ultrapower. Exact intertwiners there equate two corner dimensions. Projection comparison gives a unitary, and a unitary representative returns the desired approximation to the original algebra.

We use the full [balanced coupling construction](balancing-kraus-families-and-unitary-couplings.md), the [von Neumann multiplier ultrapower](multiplier-ultraproducts-and-normal-embeddings.md#theorem-3-2), and the complete [center-valued trace comparison and finite polar-decomposition proofs](../components/central-finite-trace-inputs.md). In a faithfully tracial algebra every bounded sequence is a multiplier: \(\|axb\|_2\le\|a\|\|b\|\|x\|_2\). Thus its ultrapower is the quotient of all bounded sequences by those with vanishing ultralimit \(2\)-norm, and its faithful normal state is a trace: the coordinate traces of \(xy\) and \(yx\) agree before taking the scalar ultralimit. Factoriality of the ultrapower is unnecessary for the proof below. [NT2](../components/central-sequence-foundations.md#nt2-faithful-state-topology) proves the bounded faithful-state topology and the normal-state countability facts; [TL1–3](../components/invariant-state-trace-hilbert-inputs.md) supplies the complete finite trace Hilbert-space and expectation proofs.

The coupling, lifting, clipping and sampling arguments allow every finite von Neumann algebra \(M\) with a faithful normal tracial state \(\tau\); separability is unnecessary. The final application to injectivity uses a \(\mathrm{II}_1\) factor. Separable predual is assumed only for a generating sequence and the identification with \(R\).

The central corner comparison first explains the unitary-conjugacy conclusion. We then establish its unitary lift, bounded clipping and finite sampling mechanisms. Radial projection onto an operator-norm ball proves clipping directly; the complete self-adjoint matrix argument gives a second proof.

<a id="4-small-coupling-energy-gives-unitary-conjugation"></a>

## Central corner comparison and unitary conjugacy

**Theorem 4.1.** For a fixed faithfully tracial finite algebra \(M\), every integer \(n\ge1\) and \(\varepsilon>0\), there is \(\delta>0\) such that any \(\delta\)-related tuples \((u_k)\), \((v_k)\) in \(M\) have a unitary \(w\in M\) with
\[
\|u_k-wv_kw^*\|_2<\varepsilon\qquad(1\le k\le n).
\tag{18}
\]
The modulus need not be specified explicitly. Neither factoriality nor separability is assumed.

**Proof.** The proof uses bounded clipping in Lemma 2.2 and unitary lifting in Lemma 3.1, both proved below. If the assertion fails, choose \(\delta_j\downarrow0\) and \(\delta_j\)-related tuples \((u_k(j))\), \((v_k(j))\) such that
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

<a id="3-unitary-representatives-in-a-finite-ultrapower"></a>

## Lifting the implementing unitary

**Lemma 3.1.** Every unitary of \(M^\omega\) has a representative consisting of unitaries of \(M\).

**Proof.** Take a bounded representative \((x_j)\). Unitarity in the quotient implies \(\|x_j^*x_j-1\|_2\to_\omega0\). Extend each polar partial isometry to a unitary \(w_j\in M\), so \(x_j=w_j|x_j|\). This extension is possible in a finite algebra: the two support projections are equivalent, hence have equal center-valued traces, and their complements are equivalent by projection comparison. Add a partial isometry between those complements.

For \(t\ge0\), \(|t-1|\le|t^2-1|\). Thus
\[
\|x_j-w_j\|_2=\||x_j|-1\|_2
\le\|x_j^*x_j-1\|_2\longrightarrow_\omega0.
\tag{17}
\]
The sequence \((w_j)\) represents the same unitary. \(\square\)

<a id="2-clipping-without-increasing-intertwining-errors"></a>

## Bounded clipping by radial projection

<a id="radial-operator-ball-projection"></a>

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

**Proof by projection onto an operator-norm ball.** The sampling lemma below supplies the \(b_i\)'s; we first prove directly why clipping their singular values cannot increase an intertwining error.

For \(R>0\) and the polar decomposition \(b=v|b|\), put
\[
\Pi_R(b)=v\min(|b|,R),\qquad q=(|b|-R)_+.
\tag{RC1}
\]
The formula gives an element \(c=\Pi_R(b)\in M\) with \(\|c\|\le R\), even when \(b\) has a kernel. Its polar support \(p=v^*v\) satisfies \(pq=q\), and \(b-c=vq\). For any \(a\in M\) with \(\|a\|\le R\),
\[
\begin{aligned}
\operatorname{Re}\tau((b-c)^*(a-c))
 &=\operatorname{Re}\tau(qv^*a)-R\tau(q)\\
 &=\tau\!\left(q^{1/2}\operatorname{Re}(v^*a)q^{1/2}\right)-R\tau(q)
 \le0.
\end{aligned}
\tag{RC2}
\]
Indeed \(qv^*c=q\min(|b|,R)=Rq\), and \(\operatorname{Re}(v^*a)\le R1\) follows from \(\|v^*a\|\le R\). Expanding the trace square gives
\[
\|b-a\|_2^2
\ge\|b-c\|_2^2+\|a-c\|_2^2.
\tag{RC3}
\]
Thus \(c\) is the unique nearest element to \(b\), in trace \(2\)-norm, among the operators of norm at most \(R\). Faithfulness of the trace proves uniqueness. The explicit formula supplies existence; no additional projection theorem is being assumed.

Apply (RC2) to \(b,d\), with their images \(c=\Pi_R(b)\), \(e=\Pi_R(d)\), using \(a=e\) and \(a=c\), respectively. Adding the resulting inequalities yields
\[
\|c-e\|_2^2
\le\operatorname{Re}\tau((b-d)^*(c-e))
\le\|b-d\|_2\|c-e\|_2.
\]
Dividing when \(c\ne e\), and treating equality separately, proves
\[
\|\Pi_R(b)-\Pi_R(d)\|_2\le\|b-d\|_2.
\tag{RC4}
\]
Left and right multiplication by unitaries preserve the operator-norm ball and the trace \(2\)-distance. Uniqueness in (RC3) therefore gives
\[
\Pi_R(ubv)=u\Pi_R(b)v\qquad(u,v\in\mathcal U(M)).
\tag{RC5}
\]
Taking \(d=v_kb\) and applying (RC4) to \(bu_k,d\), we obtain
\[
\|\Pi_R(b)u_k-v_k\Pi_R(b)\|_2
\le\|bu_k-v_kb\|_2.
\tag{RC6}
\]

We now verify every assertion in (8). For \(r=1\), choose \(c_1=0\): each squared positive-sum defect equals \(1<18\), and the coupling energies are zero. For \(r\ge2\), choose \(b_1,\ldots,b_r\) from Lemma 1.1 and set
\[
R=\sqrt r,\qquad c_i=\Pi_R(b_i),\qquad
A=\sum_i b_i^*b_i,\quad C=\sum_i c_i^*c_i.
\]
Functional calculus gives \(c_i^*c_i=\min(b_i^*b_i,r)\), \(c_ic_i^*=\min(b_ib_i^*,r)\), and \(C\le A\). In particular \(\|c_i\|\le\sqrt r\).

For \(t\ge0\),
\[
0\le t-\min(t,r)\le\frac{(t-1)_+^2}{2r}.
\tag{RC7}
\]
For \(t\le r\) the left side vanishes. For \(t>r\), subtracting \(2r(t-r)\) from \((t-1)^2\) gives \((t-r-1)^2+r(r-2)\ge0\).
The trace inequality
\[
0\le X\le Y\quad\Longrightarrow\quad
\tau((X-1)_+^2)\le\tau((Y-1)_+^2)
\tag{RC8}
\]
does not require operator monotonicity of the positive-part square. To see this, put \(D=(X-1)_+\). For \(z\ge0\),
\[
2\tau(z(X-1))-\tau(z^2)
\le2\tau(zD)-\tau(z^2)
=\tau(D^2)-\tau((z-D)^2)\le\tau(D^2).
\]
Equality holds for \(z=D\). Hence \(\tau((X-1)_+^2)\) is the supremum of the left expression over \(z\ge0\). Replacing \(X\) by the larger \(Y\) increases each expression, since \(\tau(z(Y-X))\ge0\), proving (RC8).

Since \(b_i^*b_i\le A\), (RC7)--(RC8) imply
\[
\begin{aligned}
\tau(A-C)
 &\le\frac1{2r}\sum_{i=1}^r\tau((b_i^*b_i-1)_+^2)\\
 &\le\tfrac12\tau((A-1)_+^2)
 \le\tfrac12\|A-1\|_2^2.
\end{aligned}
\tag{RC9}
\]
Also \(\tau(A^2-C^2)=\tau((A-C)(A+C))\ge0\). Expanding both squared distances from the identity therefore gives
\[
\|C-1\|_2^2
\le\|A-1\|_2^2+2\tau(A-C)
\le2\|A-1\|_2^2<18/r.
\tag{RC10}
\]
Applying the same argument to \(b_i^*\), for which \(\Pi_R(b_i^*)=c_i^*\), proves the reversed-product bound. Finally (RC6) preserves each individual intertwining error. Their sum is less than \(3n\delta\) by Lemma 1.1. This proves all of (8), including its original constants, in an arbitrary faithfully tracial finite algebra. \(\square\)

**Second proof, by self-adjoint matrix clipping.** For \(r=1\), take \(c_1=0\). Now let \(r\ge2\), choose the \(b_i\)'s from Lemma 1.1 and put
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

## Trace-Hilbert Lipschitz calculus

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

<a id="1-sampling-a-countable-coupling"></a>

## Finite sampling of a countable coupling

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
Their scalar traces agree. The continuous notation \(\Omega=\mathbb T^p\), with coordinate phases \(s_i\), has a finite realization for all the moments used here: take the \(s_i\) independently and uniformly from \(\{1,\mathrm i,-1,-\mathrm i\}\). Every phase exponent occurring in a second or fourth moment lies between \(-2\) and \(2\); the average of each nonzero such power is zero, just as for uniform circle phases. All expectations below can therefore be finite averages on the \(4^p\) phase choices and their finite products. Put \(b(s)=\sum_{i=1}^p s_i a_i\). Orthogonality of the phases gives
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

<a id="5-injective-finite-factors-are-locally-afd"></a>

## Finite and semifinite injective factors

**Theorem 5.1.** Every injective \(\mathrm{II}_1\) factor is locally approximately finite dimensional. If its predual is separable, it has a generating increasing dyadic sequence and is isomorphic to the tracial infinite product \(R\).

**Proof.** Fix a finite tuple of unitaries \(u_k\) and an error \(\varepsilon>0\). Theorem 4.1 gives a coupling threshold \(\delta\). [Balanced reconstruction](balancing-kraus-families-and-unitary-couplings.md#corollary-4-2) supplies a matrix subfactor \(D\subset M\) and unitary models \(v_k\in D\) which are \(\delta\)-related to \(u_k\). Equation (18) approximates every \(u_k\) inside the actual finite-dimensional subalgebra \(wDw^*\).

Every element is a finite linear combination of at most four unitaries, as shown in the trace-preserving model lesson. Apply the tuple argument to all unitary summands in a finite set with an error budget divided by their coefficient sums. The resulting approximants have an operator-norm bound independent of the shrinking budget. Bounded \(2\)-norm convergence for a faithful normal trace is \(\sigma\)-strong* convergence; thus this is local AFD in the von Neumann sense.

For separable predual, the [finite-factor exact containment and uniqueness theorem](hyperfinite-finite-factors.md#theorem-5-1) converts local approximation into a generating increasing dyadic matrix sequence. Its compatible trace-GNS identification gives \(M\cong R\). No uniqueness theorem for injective factors was assumed in obtaining the local approximation. \(\square\)

**Corollary 5.2.** Every separable injective \(\mathrm{II}_\infty\) factor is isomorphic to \(R\bar\otimes B(\ell^2)\).

**Proof.** We first construct \(M\cong eMe\bar\otimes B(\ell^2)\) for a nonzero finite projection \(e\). The type II∞ hypothesis supplies such a projection. Its corner is a finite factor and has no minimal projections, because a minimal projection there would also be minimal in \(M\). Thus it is of type \(\mathrm{II}_1\), and the full center-trace construction gives its faithful normal normalized trace. Separable predual gives a faithful normal state on \(M\), by NT2.

Choose a maximal orthogonal family \((e_i)\) of projections equivalent to \(e\). Zorn's lemma applies because unions of chains remain orthogonal families. The family is countable: under the faithful normal state every member has positive value, while every finite sum of those values is at most one. The finite threshold sets with values at least \(1/r\), \(r\ge1\), exhaust it. Write \(S=\sum_i e_i\) and \(r_0=1-S\). Factor projection comparison and maximality imply \(r_0\precsim e\): if \(e\precsim r_0\), another copy could be added.

There must be infinitely many \(e_i\). Otherwise, connecting the finitely many copies and the residual subprojection of \(e\) identifies \(M\) with a corner of a finite matrix algebra over \(eMe\). That matrix algebra is finite: summing its diagonal entries under the faithful corner trace gives a faithful normal finite trace. This would make the identity of \(M\) finite, contrary to type II∞.

If \(r_0=0\), put \(V=1\). If \(r_0\ne0\), choose \(r_i\le e_i\) equivalent to \(r_0\), and partial isometries \(t_i\) with \(t_i^*t_i=r_0\), \(t_it_i^*=r_i\), for \(i\ge1\). Put \(t_0=r_0\) and \(q=\sum_{i\ge1}r_i\). Orthogonality of the initial and final supports makes
\[
V=\sum_{i\ge0}t_{i+1}t_i^*+(S-q)
\]
a strong sum in \(M\), with
\[
V^*V=r_0+q+(S-q)=1,\qquad VV^*=q+(S-q)=S.
\]
Thus the residual projection is absorbed without changing the size of a finite corner. The projections \(f_i=V^*e_iV\) sum to one, and each is equivalent to \(e\); the partial isometry \(e_iV\) identifies \(f_i\) with \(e_i\).

For completeness, the countable matrix coordinates give the entire spatial tensor product. Choose \(v_i\) with \(v_i^*v_i=f_1\), \(v_iv_i^*=f_i\), and \(v_1=f_1\). In a faithful representation of \(M\) on \(H\), the map
\[
W:H\longrightarrow\ell^2\otimes f_1H,\qquad W\xi=(v_i^*\xi)_i
\]
is a unitary: the squared coordinate norms sum to \(\|\xi\|^2\), and every finitely supported tuple has preimage \(\sum_i v_i\eta_i\). It sends \(v_iv_j^*\) to the scalar matrix units. For \(a\in f_1Mf_1\), the bounded strong sum \(\sum_i v_iav_i^*\) becomes \(1\otimes a\). Conversely, every finite block compression of \(x\in M\) has entries \(v_i^*xv_j\in f_1Mf_1\). Those compressions converge strongly to \(x\), because their support projections increase to one. This proves equality with \(B(\ell^2)\bar\otimes f_1Mf_1\), rather than only an embedding. Flipping the tensor legs and identifying the equivalent corners gives the asserted decomposition.

Corner permanence of injectivity now makes \(eMe\) injective, and it is a \(\mathrm{II}_1\) factor with separable predual. Theorem 5.1 identifies it with \(R\). The matrix decomposition uses countable projection comparison, independently of the finite injective-to-AFD result. \(\square\)

This also supplies the finite-corner input for the AFD \(\mathrm{II}_\infty\) MASA regularity branch: AFD implies injective, an injective finite corner is AFD by Theorem 5.1, and the finite regularity construction applies. The nonfactor construction is treated in [Central disintegration and measurable matrix assembly](central-disintegration-and-measurable-matrix-assembly.md) and [Injective algebras and separable tracial envelopes](injective-algebras-and-separable-tracial-envelopes.md). The separate [second finite proof](small-corners-and-the-second-injective-proof.md) develops the finite-rank model approach, using [Repairing small matrix corners](repairing-small-matrix-corners.md).

## 6. Problems with complete solutions

### Corner comparison and the AFD conclusion

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

### Clipping and finite phase averages

**Exercise 3.** Verify (10) when \(r=2\).

*Solution.* For \(t\le2\), its left side is zero. For \(t>2\), the inequality is \(t-2\le(t-1)^2/4\). Subtracting \(4(t-2)\) from \((t-1)^2\) gives \((t-3)^2\ge0\). Equality occurs at \(t=3\); the bound is valid without changing its constant.

**Exercise 4.** Why may (11) be used although \(t\mapsto(t-1)_+^2\) is not assumed operator monotone?

*Solution.* Equation (12) proves monotonicity of its scalar trace value. If \(X\le Y\), then \(\tau(z(X-1))\le\tau(z(Y-1))\) for every \(z\ge0\), because the trace of \(z(Y-X)\) is nonnegative. Taking suprema gives (11). It asserts no operator inequality between the two functional-calculus values.

**Exercise 5.** Why are the weights in (7) nonnegative even when \(p_i,q_j\) do not commute?

*Solution.* Traciality gives \(\tau(p_iq_j)=\tau(q_jp_iq_j)\). The sandwich \(q_jp_iq_j\) is positive, so its trace is nonnegative. Expanding the two finite spectral squares uses these weights and the trace, without multiplying the projection partitions as if they commuted.

**Exercise 1.** Explain the subtraction term in the phase moment (5).

*Solution.* The index conditions \(i=j,\ell=t\) and \(i=t,\ell=j\) each yield a surviving phase average. When all four indices agree, both conditions count the same term. Subtracting \(\sum_i(a_i^*a_i)^2\) removes the second copy and leaves every surviving term counted exactly once. Noncommuting operator products retain their original order.

**Exercise 2.** Check why the simultaneous good-sample set has positive measure.

*Solution.* The two positive-sum failures each have probability strictly below \(1/3\). The \(n\) energy failures each have probability strictly below \(1/(3n)\). The union bound therefore gives total failure probability strictly below \(2/3+n/(3n)=1\). Its complement has positive measure and contains a sample realizing all inequalities in (2).

## References and proof scope

Uffe Haagerup, [*A new proof of the equivalence of injectivity and hyperfiniteness for factors on a separable Hilbert space*](https://doi.org/10.1016/0022-1236(85)90002-3), *Journal of Functional Analysis* 62 (1985), 160–201. Section 4 develops phase sampling, spectral clipping and ultrapower corner comparison; Theorem 5.3 applies coupling to injective finite factors. The sampling construction here uses finite fourth-root phase choices, with all noncommuting moments and simultaneous probability bounds supplied.

The radial clipping proof constructs the nearest point of an operator-norm ball in trace \(2\)-norm, proves its contraction and two-sided unitary covariance, and gives every squared-defect estimate. The self-adjoint matrix proof is also complete: the trace-Hilbert Lipschitz inequality and scalar trace monotonicity are proved here. The ultrapower proof includes a finite polar unitary lift and the \(6/\sqrt r\) central-pairing bound. Neither factoriality of the ultrapower nor an external Lipschitz or unitary-lifting theorem is needed.

Claire Anantharaman and Sorin Popa, [*An introduction to II₁ factors*](https://www.math.ucla.edu/~popa/Books/IIun.pdf), Proposition 4.2.5, p.63, gives finite matrix coordinates. Exercise 8.1, p.135, states the infinite finite-corner decomposition. Corollary 11.2.4, p.188, uses that exercise to classify separable AFD type II∞ factors. The full proof above constructs countably many orthogonal copies, absorbs the residual projection and proves the spatial matrix decomposition before applying the finite injective result. The exercise statement is not used as an unproved prerequisite.

The injective application retains the factor hypothesis of balanced reconstruction. Separable predual enters the generating dyadic sequence and identification with \(R\), and the countable II∞ decomposition. The programme lemma *Uniqueness of the injective II₁ factor*, Lemma 2.3, uses the same polar unitary-lifting mechanism at factor generality; its flip/McDuff route is a different proof. [Central disintegration and measurable matrix assembly](central-disintegration-and-measurable-matrix-assembly.md) treats the nonfactor application.

