# Kernel clustering and the Gaussian constant

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Khot and Naor introduced the Gaussian partition problem of this course to determine how well kernel clustering can be approximated [KhNa]. This lesson proves the hardness half of their programme with the identity matrix as target, using the Gaussian propeller bound of [Five or more cells and the propeller bound](five-or-more-cells-and-the-propeller-bound.md), Theorem 7.1. With
\[
\begin{gathered}
c_*=\frac9{8\pi},\\
\alpha_k=\frac{1-1/k}{c_*}=\frac{8\pi}9\Bigl(1-\frac1k\Bigr),
\end{gathered}
\]
Khot and Naor's rounding algorithm achieves the loss factor \(\alpha_k\) in expectation, and Theorem 4.1 below shows that no deterministic polynomial-time algorithm achieves a fixed loss factor below \(\alpha_k\) unless \(\mathrm P=\mathrm{NP}\).

Besides Theorem 7.1 (and through it (HJN) and Ehrhard's inequality), the proof uses two further named statements, stated in Section 2: Khot and Naor's bound for functions with low influences (KN-INF) and the Unique Games theorem of OpenAI (UGT). The lemmas that connect them, Lemmas 3.1–3.3, are proved in full.

## 1. The clustering problem

Fix an integer \(k\ge3\). An *input* is an explicitly given rational symmetric matrix \(A=(a_{pq})_{p,q=1}^N\) that is positive semidefinite and *centered*, \(A\mathbf 1=0\), where \(\mathbf 1\) is the all-ones vector. For an assignment \(\sigma:[N]\to[k]\), with \([N]=\{1,\dots,N\}\),
\[
\begin{gathered}
\operatorname{val}_A(\sigma)=\sum_{p,q=1}^Na_{pq}\,\mathbf 1_{\{\sigma(p)=\sigma(q)\}},\\
\operatorname{Clust}(A)=\max_\sigma\operatorname{val}_A(\sigma).
\end{gathered}
\]
The sum is over ordered pairs, diagonal included, and empty clusters are allowed. With the clusters \(S_i=\sigma^{-1}(i)\), \(\operatorname{val}_A(\sigma)=\sum_i\mathbf 1_{S_i}^{\mathsf T}A\mathbf 1_{S_i}\ge0\). An algorithm has *loss factor* \(\alpha\ge1\) if it returns an assignment of value at least \(\operatorname{Clust}(A)/\alpha\).

**(KN-ROUND)** [KhNa, Theorem 2.1, the case of the identity target]. There is a polynomial-time randomized algorithm, a semidefinite relaxation followed by rounding with two or three Gaussian vectors, whose output satisfies \(\mathbb E\operatorname{val}_A(\sigma)\ge\operatorname{Clust}(A)/\alpha_k\).

This statement is quoted to explain the threshold; it is not used in the proof of Theorem 4.1. It is an analysis with ideal semidefinite optimization and exact Gaussian sampling.

## 2. Fourier analysis on product spaces

Let \(\Omega=[k]\) with the uniform probability measure, and choose an orthonormal basis \(b_0=1,b_1,\dots,b_{k-1}\) of the real functions on \(\Omega\). For \(r\ge1\) and \(\nu\in\{0,\dots,k-1\}^r\) put
\[
\begin{gathered}
b_\nu(x)=\prod_{j=1}^rb_{\nu_j}(x_j),\\
|\nu|=\#\{j:\nu_j\ne0\}.
\end{gathered}
\]
The \(b_\nu\) form an orthonormal basis of \(L_2(\Omega^r)\) (uniform measure), so every \(h\) has an expansion \(h=\sum_\nu\hat h(\nu)b_\nu\) with \(\sum_\nu\hat h(\nu)^2=\|h\|_2^2\). For real \(D\ge0\) the *influence* of coordinate \(j\) up to degree \(D\) is
\[
\operatorname{Inf}_j^{\le D}(h)=\sum_{|\nu|\le D,\ \nu_j\ne0}\hat h(\nu)^2 .
\]
Let \(P_1\) be the orthogonal projection onto the span of the \(b_\nu\) with \(|\nu|=1\). For \(f=(f_1,\dots,f_k)\) put \(\operatorname{OBJ}(f)=\sum_i\|P_1f_i\|_2^2\), and let \(\Delta_k=\{u\in\mathbb R^k:u_i\ge0,\ \sum_iu_i\le1\}\).

**Lemma 2.1.** (a) The degree-one part of \(h\) is
\[
\begin{aligned}
&(P_1h)(x)\\
&\quad=\sum_{j=1}^r\bigl(\mathbb E[h\mid X_j=x_j]-\mathbb Eh\bigr);
\end{aligned}
\]
as a matrix on the coordinate vector \((h(y))_y\), with \(q=k^r\),
\[
(P_1)_{x,y}=\frac1q\sum_{j=1}^r\bigl(k\,\mathbf 1_{\{x_j=y_j\}}-1\bigr).
\]
(b) For a permutation \(\pi\) of \([r]\) let \((R_\pi x)_a=x_{\pi(a)}\). Then \(\operatorname{Inf}_j^{\le D}(h\circ R_\pi)=\operatorname{Inf}_{\pi^{-1}(j)}^{\le D}(h)\).
(c) \(\sum_{a=1}^r\operatorname{Inf}_a^{\le D}(h)\le D\,\|h\|_2^2\).

**Proof.** (a) For \(\nu_i\ne0\), \(\mathbb Eb_{\nu_i}(X_i)=\langle b_{\nu_i},b_0\rangle=0\). Hence \(\mathbb E[b_\nu(X)\mid X_j=x_j]\) equals \(b_{\nu_j}(x_j)\) if \(\nu\) vanishes off \(j\), and \(0\) otherwise; so \(\mathbb E[h\mid X_j=x_j]-\mathbb Eh\) is the part of the expansion supported on the \(\nu\) with \(\nu_j\ne0\) and \(\nu_i=0\) for \(i\ne j\). Summing over \(j\) gives the degree-one part. In coordinates, \(\mathbb E[h\mid X_j=x_j]=\frac kq\sum_{y:y_j=x_j}h(y)\) and \(\mathbb Eh=\frac1q\sum_yh(y)\).

(b) \(b_\nu(R_\pi x)=\prod_ab_{\nu_a}(x_{\pi(a)})=b_{\nu\circ\pi^{-1}}(x)\), so \(h\circ R_\pi\) has the coefficient \(\hat h(\mu\circ\pi)\) at \(b_\mu\). The map \(\mu\mapsto\mu\circ\pi\) preserves \(|\mu|\), and \(\mu_j\ne0\) if and only if \((\mu\circ\pi)_{\pi^{-1}(j)}\ne0\).

(c) Each coefficient \(\hat h(\nu)^2\) with \(|\nu|\le D\) is counted \(|\nu|\le D\) times. \(\square\)

**(KN-INF)** [KhNa, Theorem 3.8]. For fixed \(k\) and every \(\eta>0\) there is \(\tau_0\in(0,\frac12)\), independent of \(r\), such that every \(r\ge1\) and every \(f:\Omega^r\to\Delta_k\) with \(\operatorname{Inf}_j^{\le\log(1/\tau_0)}(f_i)\le\tau_0\) for all \(i\in[k]\) and \(j\in[r]\) satisfy
\[
\operatorname{OBJ}(f)\le C(k-1,k)+\eta .
\]

Here \(C(k-1,k)\) is the supremum of \(\sum|z(A_i)|^2\) over partitions of \(\mathbb R^{k-1}\) into \(k\) cells, in the notation of [Gaussian first moments of partitions](gaussian-first-moments-of-partitions.md). Its proof compares low-influence functions with Gaussian functions through the invariance principle of Mossel, O'Donnell and Oleszkiewicz [MOO]. Decreasing \(\tau_0\) only strengthens the hypothesis, so \(\tau_0<\frac12\) is harmless. By Theorem 7.1 and the propeller (\(k\ge3\)),
\[
C(k-1,k)=c_*=\frac9{8\pi}.\tag{2.1}
\]

Fix \(\eta>0\), take \(\tau_0\) from (KN-INF), choose a rational \(\tau\in(0,\tau_0)\) and put \(D=\max\{1,\lceil\log(1/\tau)\rceil\}\). Influences grow with the degree bound, so (KN-INF) yields the implication (2.2): if \(\operatorname{OBJ}(f)>c_*+\eta\), then \(\operatorname{Inf}_j^{\le D}(f_i)>\tau\) for some \(i\in[k]\) and \(j\in[r]\).
Indeed, if every influence up to degree \(D\) were at most \(\tau\), every influence up to degree \(\log(1/\tau_0)\le D\) would be at most \(\tau<\tau_0\).

A *Unique Games instance* is a bipartite graph \(G=(V,W,E)\), an alphabet \([r]\), and for each edge \(vw\) a permutation \(\pi_{vw}\) of \([r]\). A labeling \(\ell\) of \(V\cup W\) satisfies the edge \(vw\) if \(\ell(v)=\pi_{vw}(\ell(w))\).

**(UGT)** [UG, Theorem 1.1]. For every fixed \(\varepsilon,\delta\in(0,\frac12)\) there are an integer \(s\ge1\) and a deterministic polynomial-time reduction from 3SAT to explicit unweighted simple bipartite Unique Games instances with alphabet \(\mathbb F_2^s\), each constraint a translation of the alphabet and the edge set nonempty, such that: if the formula is satisfiable, some labeling satisfies at least a fraction \(1-\varepsilon\) of the edges; if it is unsatisfiable, every labeling satisfies at most a fraction \(\delta\). The alphabet size and the degree and constants of the polynomial depend only on \(\varepsilon\) and \(\delta\).

Only fractions of satisfied edges are used; no regularity of the graph is needed.

## 3. From a game to a matrix

Let \(G=(V,W,E)\) be an instance from (UGT), with alphabet \([r]\), \(r=2^s\), constraints written in the form \(\ell(v)=\pi_{vw}(\ell(w))\), and isolated vertices deleted. Put \(M=|E|\), \(d_v=|N(v)|\) and \(\mu(v)=d_v/M\) for \(v\in V\). Choosing \(v\) with probability \(\mu(v)\) and then a uniform neighbour \(w\) chooses a uniform edge. For a table \(h:W\times\Omega^r\to\mathbb R\) define
\[
\begin{gathered}
(T_vh)(x)=\frac1{d_v}\sum_{w\in N(v)}h(w,R_{\pi_{vw}}x),\\
Q(h)=\sum_{v\in V}\mu(v)\,\|P_1T_vh\|_2^2 .
\end{gathered}
\]

**Lemma 3.1.** For fixed \(k\) and \(r\) one can compute in deterministic polynomial time a rational symmetric matrix \(A\), indexed by \(W\times\Omega^r\), with
\[
h^{\mathsf T}Ah=Q(h),\qquad A\succeq0,\qquad A\mathbf 1=0 .
\]
For every \(\sigma:W\times\Omega^r\to[k]\), with \(F_i(w,x)=\mathbf 1_{\{\sigma(w,x)=i\}}\) and \(F_v=(T_vF_1,\dots,T_vF_k)\),
\[
\operatorname{val}_A(\sigma)=\sum_{v\in V}\mu(v)\operatorname{OBJ}(F_v),
\]
each \(F_v\) maps \(\Omega^r\) to \(\Delta_k\), and every value \(\operatorname{val}_A(\sigma)\) lies in \([0,1]\).

**Proof.** In coordinates, \(T_v\) has the entries \((T_v)_{x,(w,y)}=\frac1{d_v}\mathbf 1_{\{w\in N(v)\}}\mathbf 1_{\{y=R_{\pi_{vw}}x\}}\). Put
\[
A=\frac1q\sum_{v\in V}\mu(v)\,T_v^{\mathsf T}P_1T_v ,
\]
with \(P_1\) the matrix of Lemma 2.1(a). It is rational and symmetric, and \(P_1^2=P_1\) gives \(h^{\mathsf T}Ah=\sum_v\mu(v)\frac1q|P_1T_vh|^2=Q(h)\ge0\); the factor \(\frac1q\) converts the Euclidean norm of the coordinate vector into the \(L_2\) norm of the uniform measure. Also \(T_v\mathbf 1=\mathbf 1\) and \(P_1\mathbf 1=0\), so \(A\mathbf 1=0\). The size is \(|W|k^r\), polynomial for fixed \(k,r\); the entries have denominators dividing \(Mq^2\prod_vd_v\), of polynomial bit length.

Since \(\mathbf 1_{\{\sigma(p)=\sigma(q)\}}=\sum_iF_i(p)F_i(q)\), \(\operatorname{val}_A(\sigma)=\sum_iF_i^{\mathsf T}AF_i\), which is \(\sum_v\mu(v)\operatorname{OBJ}(F_v)\) by the first part. Each \(F_v(x)\) is an average of standard basis vectors, so it lies in \(\Delta_k\) with coordinate sum one, and
\[
\begin{aligned}
0\le\operatorname{OBJ}(F_v)&\le\sum_i\|T_vF_i\|_2^2\\
&\le\mathbb E\sum_iT_vF_i=1 ,
\end{aligned}
\]
using \(0\le T_vF_i\le1\). Averaging over \(\mu\) gives the last claim. \(\square\)

**Lemma 3.2** (completeness). If some labeling satisfies at least a fraction \(1-\varepsilon\) of the edges, then \(\operatorname{Clust}(A)\ge(1-\frac1k)(1-\varepsilon)^2\).

**Proof.** Let \(\ell\) be such a labeling and set \(\sigma(w,x)=x_{\ell(w)}\). Then \((T_vF_i)(x)=\sum_jp_{v,j}\mathbf 1_{\{x_j=i\}}\), where \(p_{v,j}\) is the fraction of neighbours \(w\) of \(v\) with \(\pi_{vw}(\ell(w))=j\). The degree-one part of \(\mathbf 1_{\{x_j=i\}}\) is \(\mathbf 1_{\{x_j=i\}}-\frac1k\) (Lemma 2.1(a)); these parts for different \(j\) are orthogonal, and \(\sum_i\mathbb E(\mathbf 1_{\{X_j=i\}}-\frac1k)^2=1-\frac1k\). Hence
\[
\begin{aligned}
\operatorname{OBJ}(F_v)&=\Bigl(1-\frac1k\Bigr)\sum_jp_{v,j}^2\\
&\ge\Bigl(1-\frac1k\Bigr)p_{v,\ell(v)}^2 .
\end{aligned}
\]
The \(\mu\)-average of \(p_{v,\ell(v)}\) is the fraction of edges satisfied by \(\ell\), at least \(1-\varepsilon\). Jensen's inequality and Lemma 3.1 give \(\operatorname{val}_A(\sigma)\ge(1-\frac1k)(1-\varepsilon)^2\). \(\square\)

**Lemma 3.3** (soundness). Let \(\eta>0\) with \(c_*+2\eta<1\), and \(\tau,D\) as in (2.2). If every labeling satisfies at most a fraction \(\delta<\eta\tau^2/(4kD)\) of the edges, then \(\operatorname{Clust}(A)\le c_*+2\eta\).

**Proof.** Suppose \(\operatorname{val}_A(\sigma)>c_*+2\eta\), and let \(V_{\rm good}=\{v:\operatorname{OBJ}(F_v)>c_*+\eta\}\), of \(\mu\)-mass \(\beta\). Since \(\operatorname{OBJ}(F_v)\le1\), Lemma 3.1 gives \(\operatorname{val}_A(\sigma)\le\beta+(1-\beta)(c_*+\eta)\), which is at most \(c_*+\eta+\beta\), so \(\beta>\eta\).

For \(v\in V_{\rm good}\), (2.2) supplies \(i_v\in[k]\) and \(j_v\in[r]\) with \(\operatorname{Inf}_{j_v}^{\le D}(T_vF_{i_v})>\tau\). The Fourier coefficients of \(T_vF_{i_v}\) are averages of those of the functions \(F_{i_v}(w,R_{\pi_{vw}}\cdot)\); by convexity of the square and Lemma 2.1(b),
\[
\begin{aligned}
&\operatorname{Inf}_{j_v}^{\le D}(T_vF_{i_v})\\
&\quad\le\frac1{d_v}\sum_{w\in N(v)}\operatorname{Inf}^{\le D}_{\pi_{vw}^{-1}(j_v)}\bigl(F_{i_v}(w,\cdot)\bigr).
\end{aligned}
\]
Each term lies in \([0,1]\), because \(0\le F_i\le1\). An average of numbers in \([0,1]\) that exceeds \(\tau\) has more than a fraction \(\tau/2\) of its terms at least \(\tau/2\); otherwise it would be at most \(\frac\tau2+\frac\tau2\).

For \(w\in W\) let \(L(w)\) be the set of \(a\in[r]\) with \(\operatorname{Inf}_a^{\le D}(F_i(w,\cdot))\ge\tau/2\) for some \(i\). By Lemma 2.1(c) and \(\|F_i(w,\cdot)\|_2^2\le1\),
\[
\begin{aligned}
&|L(w)|\frac\tau2\le\sum_{i=1}^k\sum_{a=1}^r\operatorname{Inf}_a^{\le D}(F_i(w,\cdot))\\
&\quad\le kD .
\end{aligned}
\]
Label each good \(v\) by \(j_v\) and the other left vertices arbitrarily, and give each right vertex \(w\) an independent uniform label from \(L(w)\) (arbitrary if \(L(w)\) is empty). For a good \(v\), more than a fraction \(\tau/2\) of its neighbours have \(\pi_{vw}^{-1}(j_v)\in L(w)\), and on each such edge the constraint holds with probability at least \(1/|L(w)|\ge\tau/(2kD)\). The expected fraction of satisfied edges therefore exceeds \(\eta\cdot\frac\tau2\cdot\frac\tau{2kD}=\frac{\eta\tau^2}{4kD}\), and some labeling attains at least the expectation, contradicting the hypothesis. \(\square\)

## 4. The threshold

**Theorem 4.1.** Assume (KN-INF) and (UGT). For each fixed \(k\ge3\) and each fixed \(1\le\alpha<\alpha_k\), it is NP-hard, given a rational centered positive semidefinite matrix \(A\), to find \(\sigma\) with \(\operatorname{val}_A(\sigma)\ge\operatorname{Clust}(A)/\alpha\). In particular a deterministic polynomial-time algorithm with loss factor \(\alpha\) would give \(\mathrm P=\mathrm{NP}\).

**Proof.** Choose rationals \(\varepsilon\in(0,\frac12)\) and \(\eta>0\) so small that \(c_*+2\eta<1\) and
\[
\alpha<\frac{(1-1/k)(1-\varepsilon)^2}{c_*+2\eta};
\]
this is possible because \(\alpha<\alpha_k=(1-1/k)/c_*\). Choose \(\tau\) and \(D\) as in (2.2), depending only on \(k\) and \(\eta\), and a rational \(\delta\in(0,\frac12)\) with \(\delta<\eta\tau^2/(4kD)\). Apply (UGT) with \(\varepsilon,\delta\); this fixes \(r=2^s\), so \(k^r\) is a constant. Put \(H=(1-\frac1k)(1-\varepsilon)^2\) and \(S=c_*+2\eta\). Composing with Lemma 3.1 gives, by Lemmas 3.2 and 3.3 and (2.1): if \(\varphi\) is satisfiable, then \(\operatorname{Clust}(A_\varphi)\ge H\); if \(\varphi\) is unsatisfiable, then \(\operatorname{Clust}(A_\varphi)\le S\).
By the choice of \(\varepsilon\) and \(\eta\), \(S<H/\alpha\); fix a rational \(\theta\) strictly between them. An algorithm with loss factor \(\alpha\) returns, on satisfiable formulas, an assignment of value at least \(H/\alpha>\theta\), while on unsatisfiable formulas every assignment has value at most \(S<\theta\). The returned value is an exactly computable rational, so comparing it with \(\theta\) decides 3SAT in polynomial time. \(\square\)

**Remark 4.2** (randomized algorithms). A polynomial-time randomized algorithm whose expected value is at least \(\operatorname{Clust}(A)/\alpha\) for a fixed \(\alpha<\alpha_k\) would put 3SAT in RP. On the instances above its value \(X\) lies in \([0,1]\) by Lemma 3.1. In the satisfiable case \(\mathbb EX\ge H/\alpha>\theta\), so \(\Pr\{X>\theta\}\ge(H/\alpha-\theta)/(1-\theta)\), a fixed positive constant; in the unsatisfiable case \(X\le S<\theta\) always. A fixed number of repetitions gives one-sided error at most \(\frac12\).

For a general positive semidefinite target matrix in place of the identity, Khot and Naor characterized the Unique Games threshold by geometric and Gaussian partition parameters [KhNa2, Theorem 1.1]; the identity target is the case in which the Gaussian parameter is the constant \(c_*\) of this course.

## 5. Exercises

**5.1** (easy). Show that \(\operatorname{val}_A(\sigma)=\sum_i\mathbf 1_{S_i}^{\mathsf T}A\mathbf 1_{S_i}\) and that for a positive semidefinite \(A\) the centering condition \(A\mathbf 1=0\) is equivalent to \(\sum_{p,q}a_{pq}=0\).

**5.2** (medium). In the proof of Lemma 3.3, the functions \(F_i(w,\cdot)\) are indicator functions with \(\sum_iF_i(w,\cdot)=1\). Show that \(\sum_i\|F_i(w,\cdot)\|_2^2=1\), deduce \(|L(w)|\le2D/\tau\), and conclude that Lemma 3.3 holds with \(\delta<\eta\tau^2/(4D)\) in place of \(\delta<\eta\tau^2/(4kD)\).

**5.3** (easy). Compute \(\operatorname{OBJ}\) for the *dictator* function \(f(x)=e_{x_1}\) (the \(x_1\)-th standard basis vector) and compare it with \(c_*\).

**5.4** (medium). Show that \(T_v\mathbf 1=\mathbf 1\) and that \(A\mathbf 1=0\) follows.

## 6. Solutions

**5.1.** \(\mathbf 1_{\{\sigma(p)=\sigma(q)\}}=\sum_i\mathbf 1_{S_i}(p)\mathbf 1_{S_i}(q)\). If \(A\succeq0\) and \(\mathbf 1^{\mathsf T}A\mathbf 1=0\), then \(A^{1/2}\mathbf 1=0\), hence \(A\mathbf 1=0\); the converse is immediate.

**5.2.** \(\|F_i(w,\cdot)\|_2^2=\mathbb EF_i(w,\cdot)\) for an indicator, and these expectations sum to \(1\). Lemma 2.1(c) then shows that \(|L(w)|\tau/2\) is at most \(\sum_i\sum_a\operatorname{Inf}_a^{\le D}(F_i(w,\cdot))\le D\), so \(|L(w)|\le2D/\tau\), and the probability bound per edge improves to \(\tau/(2D)\). The rest of the proof is unchanged.

**5.3.** \(f_i(x)=\mathbf 1_{\{x_1=i\}}\) has degree-one part \(\mathbf 1_{\{x_1=i\}}-\frac1k\), so \(\operatorname{OBJ}(f)=k\cdot\frac1k(1-\frac1k)=1-\frac1k\ge\frac23\), well above \(c_*<0.36\). This does not contradict (KN-INF): each \(f_i\) has influence \(\frac1k(1-\frac1k)\) at the first coordinate, more than any small \(\tau_0\). The completeness lemma uses averages of such dictators.

**5.4.** \((T_v\mathbf 1)(x)=\frac1{d_v}\sum_{w\in N(v)}1=1\). Then \(T_v\mathbf 1=\mathbf 1\) and \(P_1\mathbf 1=0\) (a constant has no degree-one part) give \(A\mathbf 1=\frac1q\sum_v\mu(v)T_v^{\mathsf T}P_1\mathbf 1=0\).

## References

- [OpenAI-GP] OpenAI, *The Gaussian propeller bound in every dimension*, OpenAI Math Release preprint, 24 September 2026, Section 6. https://github.com/openai/math/tree/main/preprints/The-Gaussian-Propeller-Bound-in-Every-Dimension-September-24-2026
- [KhNa] S. Khot and A. Naor, *Approximate kernel clustering*, Mathematika 55 (2009), 129–165; arXiv:0807.4626. https://arxiv.org/abs/0807.4626
- [KhNa2] S. Khot and A. Naor, *Sharp kernel clustering algorithms and their associated Grothendieck inequalities*, Random Structures & Algorithms 42 (2013), 269–300; arXiv:0906.4816. https://arxiv.org/abs/0906.4816
- [MOO] E. Mossel, R. O'Donnell and K. Oleszkiewicz, *Noise stability of functions with low influences: invariance and optimality*, Annals of Mathematics 171 (2010), 295–341; arXiv:math/0503503. https://arxiv.org/abs/math/0503503
- [UG] OpenAI, *The Unique Games Theorem*, OpenAI Math Release preprint, 23 September 2026, Theorem 1.1. https://github.com/openai/math/tree/main/preprints/The-Unique-Games-Theorem-September-23-2026
