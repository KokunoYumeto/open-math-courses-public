# Universal measurability and strong sequences

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. Original text: CC0 1.0.*

Semicontinuous operators can bound an operator from above and below. Universal measurability asks that the gap between such bounds be arbitrarily small when measured by any given state. This produces a norm-closed real space larger than either semicontinuity cone. It is also closed under strong limits of sequences.

The sequential closure proof has two stages. First we handle increasing sequences by compressing a positive sum with a bounded rational function. Then a rapidly convergent subsequence of an arbitrary strong sequence reduces the problem to positive sums again. The rational compression controls the operator norm even when the uncompressed partial sums have no common bound.

Use [Monotone approximation and semicontinuous operators](../reader/monotone-approximation-and-semicontinuous-operators.html), particularly its positive rational stability, exact unitized class, one-sided resolvent lemma and Jordan algebra. Bounded monotone closure of the norm-closed cones is [Passing to an increasing limit](../reader/open-projections-and-closed-one-sided-ideals.html#passing-to-an-increasing-limit), Corollary 1.2. The complete proof of [Kaplansky's continuity theorem](../../foundations-of-von-neumann-algebras/kaplansky-s-density-theorem-and-its-consequences.html#oa-fnd-kd-05), Theorem 5.2 and Corollary 5.3(4), permits unbounded nets when taking absolute values. The [universal representation](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#oa-fnd-wa-03) is used in its faithful nondegenerate case, with the stated bidual and normal-extension background. [Normal vector expansions](../../foundations-of-von-neumann-algebras/the-double-commutant-theorem.html#oa-fnd-bi-14), Theorem 10.1, handle other faithful normal realizations. Brown’s freely readable paper treats the measurable-space definition and sequential closure. The proofs below establish that closure in full.

## 1. Small gaps for each state

Let \(A\) be a C*-algebra and \(M=A^{**}\). The zero algebra is immediate; assume \(A\ne0\). Write
\[
U=A_{\mathrm{sa}}^\uparrow,\qquad L=A_{\mathrm{sa}}^\downarrow,
\qquad A_1=A+\mathbb C1.
\]
An arrow denotes a norm-bounded monotone strong limit. States of \(A\) are identified with their positive normal extensions to \(M\).

Call \(a\in M_{\mathrm{sa}}\) universally measurable if for every \(\varphi\in S(A)\) and \(\varepsilon>0\) there are \(x\in U\) and \(y\in L\) such that
\[
y\le a\le x,
\qquad \varphi(x-y)<\varepsilon.
\tag{1.1}
\]
Denote the resulting class by \(\mathcal M_u(A)\). The bounding elements may depend on the state and on the tolerance.

**Lemma 1.1 — squeezing with measurable bounds.** An element \(a\in M_{\mathrm{sa}}\) belongs to \(\mathcal M_u(A)\) if and only if (1.1) can be satisfied with \(x,y\) themselves in \(\mathcal M_u(A)\).

**Proof.** First, \(U\subset\mathcal M_u(A)\). If \(a_i\in A_{\mathrm{sa}}\) increase boundedly to \(a\), normality gives \(\varphi(a-a_i)\to0\); use upper bound \(a\in U\) and lower bound \(a_i\in L\), the latter by a constant net. Taking negatives gives \(L\subset\mathcal M_u(A)\). This proves one implication.

Conversely, suppose measurable bounds \(v\le a\le u\) have \(\varphi(u-v)<\varepsilon/3\). Choose original upper and lower bounds \(x\in U\), \(y\in L\), with
\[
x\ge u,\quad y\le v,\qquad
\varphi(x-u)<\varepsilon/3,\quad\varphi(v-y)<\varepsilon/3.
\]
They exist by measurability of \(u\) and \(v\). Then \(y\le a\le x\), and summing the three positive gaps gives \(\varphi(x-y)<\varepsilon\). \(\square\)

**Proposition 1.2.** The class \(\mathcal M_u(A)\) is a norm-closed real vector space. It contains \(1\), \(U\), \(L\), and
\[
J=\overline{U-U}^{\|\cdot\|}.
\tag{1.2}
\]
It is invariant under \(a\mapsto\alpha a+\beta1\), for real \(\alpha,\beta\).

**Proof.** Taking negatives interchanges upper and lower bounds in (1.1), so the class is symmetric. Positive scalar multiplication rescales the gap and preserves both monotone-limit classes. Those classes are closed under addition: use the product directed set for two bounded monotone nets. Adding bounds with tolerance \(\varepsilon/2\) proves closure under addition. Zero is included.

An increasing contractive approximate identity of \(A\) has strong supremum \(1\). Thus \(1\in U\subset\mathcal M_u(A)\), and all real scalar multiples of \(1\) belong to the measurable space. If \(a_n\in\mathcal M_u(A)\) and \(\|a_n-a\|\le\delta\), then
\[
a_n-\delta1\le a\le a_n+\delta1.
\]
The two bounds are measurable, and their state gap is \(2\delta\). Lemma 1.1 proves norm closedness. The inclusions of \(U,L\), followed by linearity and norm closure, give (1.2). Affine invariance follows. \(\square\)

Retain the two norm-closed cones and the exact unitized class
\[
C=\overline U^{\|\cdot\|},\qquad
C_+=\overline{A_+^\uparrow}^{\|\cdot\|}=C\cap M_+,
\qquad
T=(A_1)_{\mathrm{sa}}^\uparrow=\mathbb R1+C.
\tag{1.3}
\]
The preceding proposition gives \(C,T,-T,J\subset\mathcal M_u(A)\). The space \(J\) is the norm-closed Jordan algebra already proved in the monotone-approximation lesson; in particular it contains the continuous real functional calculus of each of its elements. We will apply that fact to elements of \(T\), without assuming that every measurable element already has that calculus closure.

<a id="comparing-the-free-source-definition"></a>

### Equivalent semicontinuous bounds

[Brown] uses bounds in \(C\) and \(-C\) in the small-gap definition. This gives exactly the class in (1.1). Our original bounds lie in those closed cones, which proves one inclusion. Conversely, fix a state \(\varphi\) and a tolerance \(\varepsilon>0\), and choose Brown's bounds \(k\le a\le h\) with \(h\in C\), \(k\in-C\), and \(\varphi(h-k)<\varepsilon/2\). For \(0<\delta<\varepsilon/4\), [the scalar-shift criterion](../reader/monotone-approximation-and-semicontinuous-operators.html#2-lower-semicontinuity-on-the-quasi-state-space), Theorem 2.1(4), gives \(h+\delta1\in U\) and \(k-\delta1\in L\). These still bound \(a\), and their state gap is \(\varphi(h-k)+2\delta<\varepsilon\). This proves the reverse inclusion. No common operator norm bound on all state-dependent choices is imposed.

## 2. One-sided strong approximation

Let \(H_u\) be the universal representation space. Every state \(\varphi\) is a vector state there, with a unit vector \(\xi_\varphi\). This also identifies its quadratic seminorm:
\[
\varphi(b^2)^{1/2}=\|b\xi_\varphi\|
\quad(b=b^*\in M).
\tag{2.1}
\]

**Theorem 2.1.** An element \(a\in M_{\mathrm{sa}}\) is universally measurable if and only if, for every state \(\varphi\) and \(\varepsilon>0\), there are \(x\in T\), \(y\in-T\) with
\[
y\le a\le x,
\qquad
\varphi((x-a)^2)^{1/2}+\varphi((a-y)^2)^{1/2}<\varepsilon.
\tag{2.2}
\]
Equivalently, in \(H_u\), the sum of the two norms in (2.2) can be required to be small at every specified vector. There is also an equivalent formulation in every faithful normal realization: \(a\) is in the strong closure of its upper bounds in \(T\) and of its lower bounds in \(-T\). Here strong closure means approximation on every finite set of vectors simultaneously.

**Proof.** Suppose \(a\) is measurable. Positive affine normalization reduces to \(0\le a\le1\). The definition supplies a net \(x_i\in U\) with \(x_i\ge a\) and \(x_i\to a\) ultraweakly. To construct it, direct finite sets of states and positive tolerances by enlargement and decreasing tolerance; apply (1.1) to the normalized sum of those states. Since all gaps are positive, making that sum sufficiently small makes each required gap small. Every positive normal functional is a scalar multiple of a state, and positive normal functionals span the predual. Hence the net has the asserted ultraweak convergence. Its norms need not have a common bound.

Each \(x_i\) is positive and lies in \(C_+\). For \(\alpha>0\), put
\[
f_\alpha(t)=\frac{t}{1+\alpha t},\qquad
w_{\alpha,i}=(1+\alpha)f_\alpha(x_i).
\tag{2.3}
\]
Positive rational stability gives \(w_{\alpha,i}\in C_+\subset T\). Operator monotonicity gives
\[
w_{\alpha,i}\ge(1+\alpha)f_\alpha(a)\ge a,
\tag{2.4}
\]
where the second inequality follows, on \([0,1]\), from
\[
0\le(1+\alpha)f_\alpha(t)-t
=\frac{\alpha t(1-t)}{1+\alpha t}\le\alpha.
\tag{2.5}
\]
For fixed \(\alpha\), the one-sided resolvent lemma gives
\[
w_{\alpha,i}\longrightarrow(1+\alpha)f_\alpha(a)
\quad\text{strongly},
\qquad 0\le w_{\alpha,i}\le\frac{1+\alpha}{\alpha}1.
\tag{2.6}
\]
This holds in any faithful normal realization: ultraweak convergence implies weak operator convergence there, and the resolvent proof needs only the lower bound \(x_i\ge a\ge0\). The bounded target in (2.6) converges in norm to \(a\) as \(\alpha\downarrow0\). Given a finite set of vectors and a tolerance, first choose \(\alpha\) and then choose an index \(i\) to make both errors small. This proves upper strong approximation. It does not assert convergence on a product index with \(\alpha\) and \(i\) chosen independently. Applying the same argument to \(-a\) and undoing the affine normalizations gives lower approximation. In particular it proves (2.2) and the universal-vector formulation.

Conversely, (2.2) and Cauchy–Schwarz for the normal state give
\[
\varphi(x-y)
\le\varphi((x-a)^2)^{1/2}+\varphi((a-y)^2)^{1/2}<\varepsilon.
\]
Since \(x,y\in\mathcal M_u(A)\), Lemma 1.1 proves measurability. In \(H_u\), (2.1) proves the converse from the vector condition as well. All vectors there give positive normal functionals, while each state has its own universal vector; thus those formulations are equivalent.

Finally suppose the two strong-closure conditions hold in another faithful normal realization. Normalize again to \(0\le a\le1\), and take a net \(x_i\in T\), \(x_i\ge a\), converging strongly to \(a\). The elements \(x_i\) are positive. For fixed \(\alpha>0\), the resolvent identity gives
\[
(1+\alpha x_i)^{-1}-(1+\alpha a)^{-1}
=\alpha(1+\alpha x_i)^{-1}(a-x_i)(1+\alpha a)^{-1}
\longrightarrow0\quad\text{strongly}.
\tag{2.7}
\]
The left inverse factors have norms at most one, so strong convergence on the fixed vectors \((1+\alpha a)^{-1}\xi\) suffices. Thus \(w_{\alpha,i}=(1+\alpha)f_\alpha(x_i)\) converge strongly to \((1+\alpha)f_\alpha(a)\), with the common bound in (2.6). They are measurable: \(x_i\in T\subset J\), and continuous functional calculus in \(J\) contains their rational transforms. They majorize \(a\) by (2.4).

Every normal state has a square-summable vector expansion in this realization. The common bound for fixed \(\alpha\) controls its series tail, and strong convergence handles the finite initial sum. Hence \(\varphi(w_{\alpha,i})\to\varphi((1+\alpha)f_\alpha(a))\). First choose \(\alpha\) small using (2.5), then choose \(i\); this gives measurable upper bounds with arbitrarily small state gap. The lower-closure condition, applied to \(-a\), gives measurable lower bounds. Lemma 1.1 proves measurability, establishing the general strong-closure equivalence. \(\square\)

The state-seminorm formulation is intrinsic. The universal realization makes its quantification by individual vectors exact. In an arbitrary realization, finite sets of vectors specify the equivalent strong-topology formulation. The bounded rational transforms in (2.7) are what allow normal states with several, or infinitely many, vector components to be used in its converse.

## 3. Increasing measurable sequences

**Lemma 3.1.** If \(a_n\in\mathcal M_u(A)\) increase boundedly to \(a\), then \(a\in\mathcal M_u(A)\). The corresponding statement holds for decreasing sequences.

**Proof.** Normalize to \(0\le a_n\le a\le1\), put \(a_0=0\), and set
\[
d_n=a_n-a_{n-1}\ge0.
\]
Fix a state \(\varphi\) and \(\delta>0\). Each \(d_n\) is measurable, so choose \(x_n\in U\) with
\[
x_n\ge d_n,
\qquad\varphi(x_n-d_n)<\delta2^{-n}.
\tag{3.1}
\]
The elements \(x_n\) are positive, hence belong to \(C_+\). Write \(R_n=\sum_{k=1}^n x_k\). They form an increasing positive sequence in \(C_+\), although their operator norms may be unbounded. Their state values satisfy
\[
\varphi(R_n)\le\varphi(a_n)+\delta\le\varphi(a)+\delta.
\tag{3.2}
\]
For fixed \(\alpha>0\), the operators
\[
Y_{\alpha,n}=(1+\alpha)f_\alpha(R_n)
\]
increase, are bounded by \((1+\alpha)/\alpha\), and belong to \(C_+\). Bounded monotone closure of \(C\), together with positivity, places their strong limit \(Y_\alpha\) in \(C_+\subset\mathcal M_u(A)\). Since \(R_n\ge a_n\),
\[
Y_\alpha\ge(1+\alpha)f_\alpha(a)\ge a.
\tag{3.3}
\]
Normality, \(f_\alpha(t)\le t\) for \(t\ge0\), and (3.2) give
\[
\varphi(Y_\alpha-a)
\le\alpha\varphi(a)+(1+\alpha)\delta
\le\alpha+(1+\alpha)\delta.
\tag{3.4}
\]
Choose \(\alpha\) and \(\delta\) so that this is as small as required. On the other side, \(a_n\le a\) are already measurable and \(\varphi(a-a_n)\to0\). Thus \(a\) is squeezed between measurable bounds with arbitrarily small total state gap. Lemma 1.1 proves the assertion. Taking negatives gives decreasing closure. \(\square\)

This proof uses monotone closure of \(C_+\) to establish monotone closure of \(\mathcal M_u(A)\); it does not assume the conclusion in constructing \(Y_\alpha\).

## 4. Arbitrary strongly convergent sequences

**Theorem 4.1.** The space \(\mathcal M_u(A)\) is sequentially strongly closed in every faithful normal realization of \(A^{**}\).

**Proof.** Let \(a_n\in\mathcal M_u(A)\) converge strongly to \(a\). A strongly convergent sequence is norm bounded by uniform boundedness. Its limit is self-adjoint and lies in \(M\). Affine invariance and scaling reduce to
\[
\|a_n\|\le\tfrac12,
\qquad\|a\|\le\tfrac12.
\tag{4.1}
\]
For every positive normal functional,
\(\varphi((a_n-a)^2)\to0\). In the universal realization this is vector convergence. In any other faithful normal realization, use its square-summable normal vector expansion: the bounded norms control the series tail, and strong convergence handles the finitely many leading vectors.

Fix a state \(\varphi\) and \(\delta>0\). Choose and relabel a subsequence so rapidly convergent that
\[
\varphi(|a_1-a|)<\delta,
\qquad
\varphi(|b_n|)<\delta2^{-n},
\quad b_n=a_{n+1}-a_n.
\tag{4.2}
\]
This is possible by choosing the quadratic seminorm errors \(\varphi((a_n-a)^2)^{1/2}\) geometrically small and using Cauchy–Schwarz and the triangle inequality for those seminorms.

Each \(b_n\) is measurable. Theorem 2.1 supplies upper bounds in \(T\) converging strongly to \(b_n\) in \(H_u\). The complete absolute-value continuity theorem gives strong convergence of their absolute values to \(|b_n|\), even if that approximating net is unbounded. At the vector \(\xi_\varphi\), choose an upper bound \(x_n\in T\) with
\[
x_n\ge b_n,
\qquad\varphi(|x_n|)<2\delta2^{-n}.
\tag{4.3}
\]
Because \(T\subset J\), its continuous functional calculus puts \(|x_n|\in J\). Therefore
\[
R_n=\sum_{k=1}^n|x_k|\in J_+,
\qquad\varphi(R_n)<2\delta.
\tag{4.4}
\]
For \(0<\alpha<1\), \(f_\alpha(R_n)\) is an increasing bounded sequence in \(J\subset\mathcal M_u(A)\). By Lemma 3.1 its strong supremum
\[
X_\alpha=\mathop{\mathrm{s}\!\!-\!\!\lim}_{n\to\infty}f_\alpha(R_n)
\tag{4.5}
\]
is measurable. Normality and \(f_\alpha(t)\le t\) give \(\varphi(X_\alpha)\le2\delta\).

Let \(S_n=\sum_{k=1}^n b_k=a_{n+1}-a_1\). By (4.1), \(-1\le S_n\le1\), and
\[
S_n\le\sum_{k=1}^n x_k\le R_n.
\]
Inversion reverses order whenever \(1+\alpha t\) is positive invertible. Hence \(f_\alpha\) is operator monotone throughout the interval \([-1,\infty)\), and all three displayed operators lie in that domain. For \(|t|\le1\),
\[
t-f_\alpha(t)=\frac{\alpha t^2}{1+\alpha t}
\le\frac{\alpha}{1-\alpha}.
\]
Consequently
\[
S_n-\frac{\alpha}{1-\alpha}1
\le f_\alpha(S_n)
\le f_\alpha\left(\sum_{k=1}^n x_k\right)
\le f_\alpha(R_n)\le X_\alpha.
\tag{4.6}
\]
Taking the strong limit of \(S_n\) yields a measurable upper bound
\[
u=a_1+X_\alpha+\frac{\alpha}{1-\alpha}1\ge a,
\qquad
\varphi(u-a)<3\delta+\frac{\alpha}{1-\alpha}.
\tag{4.7}
\]
Here the initial error is \(\varphi(a_1-a)\le\varphi(|a_1-a|)<\delta\); no smallness of \(\varphi(a_1)\) itself is assumed. Choose \(\delta\) and then \(\alpha\) to make (4.7) arbitrarily small. Applying the argument to \(-a_n\) supplies a measurable lower bound with an arbitrarily small gap. Lemma 1.1 proves \(a\in\mathcal M_u(A)\). Undo the normalization. \(\square\)

Uniform boundedness is used for the original convergent sequence. The auxiliary positive sums in (3.2) and (4.4) have only a state bound; rational compression supplies their operator bound before taking a strong supremum.

## 5. Graded exercises with solutions

**Exercise 5.1 — introductory: explicit bounds for a sequence algebra.** Let \(A=c_0(\mathbb N)\) and \(a\in\ell^\infty_{\mathrm{sa}}\). For a state with weights \(\mu_n\ge0\), \(\sum_n\mu_n=1\), give bounds satisfying (1.1). Conclude that \(\mathcal M_u(c_0)=\ell^\infty_{\mathrm{sa}}\).

**Solution.** Put \(R=\|a\|\), and for a finite set \(F\), let \(p_F=1_F\). Define
\[
x_F=p_Fa+R(1-p_F),\qquad
y_F=p_Fa-R(1-p_F).
\]
Then \(y_F\le a\le x_F\). The negative part of \(x_F\) is finitely supported, and its positive part is a bounded positive sequence. Truncating that positive part increasingly and keeping the negative part fixed gives a bounded increasing net from \(c_0\) with limit \(x_F\). Thus \(x_F\in U\). Applying the same argument to \(-y_F\) shows \(y_F\in L\). Their state gap is
\[
\varphi(x_F-y_F)=2R\sum_{n\notin F}\mu_n\longrightarrow0.
\]
Choose \(F\) large enough. Every self-adjoint bidual element is thereby measurable.

**Exercise 5.2 — intermediate: a countable Borel projection.** Use the rational-set projection constructed in [Abelian semicontinuity and multiplier spectra](../reader/abelian-semicontinuity-and-multiplier-spectra.html), Exercise 4.3, to prove that \(\mathcal M_u(C_0(\mathbb R))\) contains an element belonging to neither \(T\) nor \(-T\).

**Solution.** Each point projection \(p_q\) is the decreasing strong limit of the continuous bumps at \(q\), so \(p_q\in L\subset\mathcal M_u(A)\). Enumerate the rationals. The finite sums of their mutually orthogonal point projections are measurable positive contractions and increase strongly to \(r\). Lemma 3.1 puts \(r\) in \(\mathcal M_u(A)\). Its evaluations at finite positive measures are \(\mu(\mathbb Q)\), and its point evaluations are \(1_{\mathbb Q}\). The earlier function-model theorem excludes it from both monotone-limit classes, since the rationals and irrationals are both dense. Thus the measurable space strictly extends their union.

**Exercise 5.3 — advanced: a state bound without an operator bound.** On \(H=\ell^2(\mathbb N)\), let \(p_n\) be the coordinate rank-one projections, \(x_n=np_n\), and
\[
\varphi(T)=\sum_{n=1}^\infty2^{-n}\langle T\delta_n,\delta_n\rangle.
\]
For \(A=\mathcal K(H)\), analyze \(R_N=\sum_{n\le N}x_n\) and the strong limits of \(f_\alpha(R_N)\). Explain their use in the closure proof.

**Solution.** The functional is a faithful normal state, and
\[
\varphi(R_N)=\sum_{n\le N}n2^{-n}\le2,
\qquad\|R_N\|=N.
\]
Thus the state values are bounded while the operator norms diverge. For fixed \(\alpha>0\), the rational transforms increase to the bounded diagonal operator
\[
X_\alpha\delta_n=\frac{n}{1+\alpha n}\delta_n,
\qquad\|X_\alpha\|=\frac1\alpha,
\qquad\varphi(X_\alpha)\le2.
\]
They converge strongly because each fixed diagonal coordinate stabilizes and the transforms have a common bound. Each \(R_N\) is positive finite rank; its transform is also in \(A_+\), so its bounded increasing limit lies in \(U\subset\mathcal M_u(A)\). There is no bounded operator supremum for the original sequence \(R_N\). The proofs above take the strong supremum only after this rational compression and then use the small state gap separately.

## References

[Brown] Lawrence G. Brown, *Large C\*-algebras of universally measurable operators*, [arXiv:1309.6306v1](https://arxiv.org/abs/1309.6306v1), 24 September 2013; *Quarterly Journal of Mathematics* 65 (2014), 851–855.
