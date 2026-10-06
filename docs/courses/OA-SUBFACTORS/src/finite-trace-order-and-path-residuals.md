# Finite trace order and the remaining support

A residual trace can be positive while its formal matrix ranks are negative. Lesson 78 resolves this at finite depth by primitive matrix convergence. Here we prove the corresponding order test for every sequence of finite-dimensional unital inclusions. It identifies exactly which other traces can obstruct promotion. We then compute two infinite path cases: the critical trace has every dyadic projection trace it needs, whereas a transcendental noncritical trace can fail subtraction closure even though its von Neumann algebra is a factor.

The inputs are the [finite matrix decomposition in 8.1](finite-dimensional-markov-calculus.md), the [actual path algebras and weights in 9.1–9.2](path-models.md), their [factoriality in 10.5](path-trace-factoriality.md), and the [placement and residual-extension theorems 78.1–78.3](trace-certificates-and-exact-finite-partitions.md). The compactness and integer arguments below are proved directly; no dimension-group classification theorem is used. The final applications to an actual tunnel state their precise trace hypotheses. The unrestricted partition in Popa's Theorem 4.4.1(1) remains assigned.

## Rank vectors and all compatible traces

Let the actual finite-dimensional unital inclusions be

\[
\begin{gathered}
F_j=\bigoplus_{\ell=1}^{s_j}\operatorname{Mat}_{n_{j\ell}},\\
F_j\subset F_{j+1},\qquad n_{j\ell}>0,\\
n_{j+1}=D_jn_j,\\
D_j\geq0\text{ integer}.
\end{gathered}
\tag{79.1}
\]

Rows of \(D_j\) are target blocks; columns are source blocks. Write \(D_{j,k}=D_{k-1}\cdots D_j\) for \(k>j\), and \(D_{j,j}=I\). A tracial state on \(F_j\) is specified by its minimal-projection weights, so its simplex is

\[
\begin{gathered}
W_j=\{w\in\mathbb R_+^{s_j}:w\cdot n_j=1\},\\
w_j=D_j^{\mathsf T}w_{j+1},\\
K_{j,k}=D_{j,k}^{\mathsf T}W_k.
\end{gathered}
\tag{79.2}
\]

Weights here may be zero. Although the inherited ambient trace is faithful, the order test must include other, possibly nonfaithful, traces on the norm closure. Every \(W_j\) is a nonempty compact simplex, and \(K_{j,k+1}\subset K_{j,k}\).

**Lemma 79.1 — compatible-trace compactness.** For \(F=\overline{\bigcup_jF_j}^{\|\cdot\|}\), the restrictions to \(F_j\) of all tracial states on \(F\) form exactly \(K_j=\bigcap_{k\geq j}K_{j,k}\). Compatible sequences of weights are precisely the tracial states on \(F\).

**Proof.** Trace restriction across the embedding gives 79.2: each source minimal projection appears with multiplicity \(D_{j,\ell a}\) in target block \(\ell\). A compatible sequence therefore defines a positive normalized trace on the algebraic union. Each finite-stage state has norm one, so the resulting functional is bounded by the operator norm and extends to \(F\). Positivity, normalization and the trace identity pass to the norm closure. Conversely, restriction of a tracial state supplies just such a sequence.

A global trace restricts to every \(K_{j,k}\). For the reverse implication fix \(w\in K_j\). At each arbitrarily late \(k\), choose a trace on \(F_k\) whose restriction to \(F_j\) is \(w\), and restrict it to every earlier level. Compactness of each finite-dimensional simplex permits successively extracting convergent subsequences at levels \(0,1,2,\ldots\). A diagonal subsequence converges at every fixed level. The finite linear restriction maps preserve these limits, producing a compatible sequence with its \(j\)-th entry \(w\). The previous paragraph extends it to a tracial state on \(F\). The same construction, starting with arbitrary late traces, supplies existence without presupposing a global trace. The set of compatible sequences is closed in the countable product of compact simplexes; the diagonal argument proves its sequential compactness, which suffices for every minimum below. \(\square\)

Fix a signed integer rank vector \(v\in\mathbb Z^{s_j}\). For a trace \(\sigma\) with weight \(w_j\), its evaluation on this formal vector means \(\sigma(v)=w_j\cdot v\). No projection with rank \(v\) is asserted. Set

\[
\begin{gathered}
v_k=D_{j,k}v,\qquad n_k=D_{j,k}n_j,\\
a_k(v)=\min_\ell\frac{v_{k\ell}}{n_{k\ell}},\\
b_k(v)=\max_\ell\frac{v_{k\ell}}{n_{k\ell}}.
\end{gathered}
\tag{79.3}
\]

**Theorem 79.2 — the finite order test.** The numbers \(a_k(v)\) increase and \(b_k(v)\) decrease as \(k\) increases. Their exact limits are

\[
\begin{gathered}
a=\min_{\sigma\in T(F)}\sigma(v),\\
b=\max_{\sigma\in T(F)}\sigma(v),\\
a_k(v)\longrightarrow a,\qquad b_k(v)\longrightarrow b,\\
0\leq v_k\leq n_k
\iff\begin{cases}a_k(v)\geq0,\\b_k(v)\leq1.\end{cases}
\end{gathered}
\tag{79.4}
\]

Here \(T(F)\) denotes all tracial states on the norm closure. In particular, if every such trace has \(0<\sigma(v)<1\), the promoted vector is a valid projection-rank vector at some finite level. Its value under any chosen inherited trace is preserved exactly.

**Proof.** A trace on \(F_k\) assigns normalized block masses \(m_\ell=n_{k\ell}w_{k\ell}\), with \(m_\ell\geq0\) and \(\sum m_\ell=1\). Hence

\[
w_k\cdot v_k
=\sum_\ell m_\ell\frac{v_{k\ell}}{n_{k\ell}}.
\tag{79.5}
\]

Every vertex mass concentrated on one block is allowed. The minimum and maximum on \(W_k\) are therefore exactly 79.3. By restriction they are also the extrema of \(w\cdot v\) on \(K_{j,k}\). The nesting of these compact sets proves monotonicity. They are bounded because \(K_{j,k}\subset W_j\).

Choose a minimizer in each \(K_{j,k}\). A subsequence converges in \(W_j\). Its limit belongs to every fixed \(K_{j,h}\), because all sufficiently late minimizers belong to that closed set. Thus the limit belongs to \(K_j\), and its evaluation equals \(\lim a_k(v)\). Lemma 79.1 identifies it with the restriction of a global trace. Since every point of \(K_j\) lies in every \(K_{j,k}\), the opposite inequality is automatic. This proves the minimum formula; maximizing proves the maximum formula.

The finite inequalities in 79.4 are simply the coordinatewise rank bounds. If all global trace values lie strictly inside \((0,1)\), compactness gives attained extrema \(a>0\) and \(b<1\). The two limits imply \(a_k>0\) and \(b_k<1\) for all sufficiently late \(k\). The ranks remain integers. Diagonal projections with those ranks then exist in \(F_k\). Trace compatibility gives

\[
w_k\cdot D_{j,k}v=w_j\cdot v
\tag{79.6}
\]

for each inherited compatible weight system. This is an exact equality, with no tolerance or limiting replacement of the trace. \(\square\)

If no finite promotion of this particular vector is valid, the contrapositive gives a trace with value at most zero or at least one. A limiting value equal to zero or one need not obstruct a different vector with the same ambient trace. Nor does nonnegative evaluation at every trace by itself supply the strict hypothesis.

**Corollary 79.3 — unique norm trace.** If \(F\) has a unique tracial state \(\tau\), its finite projection traces are exactly the elements of the additive group generated by those traces that lie in \([0,1]\).

**Proof.** Represent any group element by a finite signed sum of finite projection ranks and move them to one level. If its trace lies strictly between zero and one, Theorem 79.2 realizes it. The scalar endpoints use zero and the identity, regardless of the signed representative. The converse follows from the definition of the group. \(\square\)

For the actual smaller tunnel algebras \(B_j=N_j'\cap N\), each selected support in 76.4 has a canonical finite trace certificate by 78.1. Thus uniqueness of the tracial state on \(\overline{\bigcup_jB_j}^{\|\cdot\|}\) makes the residual trace a finite certificate and 78.3 gives an exact finite full partition. This implication requires neither stationarity nor finite depth. Uniqueness of the normal trace on a factorial von Neumann closure does not assert this norm-trace hypothesis.

## A changing system and the strict endpoints

**Example 79.4 — a nonstationary promotion.** Take two blocks, \(n_0=(1,1)^{\mathsf T}\), and

\[
\begin{gathered}
D_j=\begin{pmatrix}j+2&1\\1&j+2\end{pmatrix},\\
R_k=\prod_{j=0}^{k-1}(j+3)=\frac{(k+2)!}{2},\\
S_k=\prod_{j=0}^{k-1}(j+1)=k!,\\
n_k=R_k(1,1)^{\mathsf T}.
\end{gathered}
\tag{79.7}
\]

The empty products are one. The symmetric and antisymmetric vectors are simultaneous eigenvectors of all \(D_j\), with respective product eigenvalues \(R_k,S_k\). For \(v=(-2,3)^{\mathsf T}\),

\[
\begin{gathered}
v_k=\frac{R_k}{2}(1,1)^{\mathsf T}
 +\frac{5S_k}{2}(-1,1)^{\mathsf T},\\
a_k(v)=\frac12-\frac{5}{(k+1)(k+2)},\\
b_k(v)=\frac12+\frac{5}{(k+1)(k+2)}.
\end{gathered}
\tag{79.8}
\]

In particular,

\[
\begin{gathered}
v_0=(-2,3),\qquad n_0=(1,1),\\
v_1=(-1,4),\qquad n_1=(3,3),\\
v_2=(1,11),\qquad n_2=(12,12).
\end{gathered}
\tag{79.9}
\]

The inherited minimal weights are \((1/(2R_k),1/(2R_k))\), so the trace is one half at every level. The norm trace is unique: at any fixed starting level, the product of the antisymmetric-to-symmetric ratios tends to zero. The restriction of every later normalized weight simplex therefore contracts to the symmetric ray, whose scale is fixed by \(n_j\). Lemma 79.1 then leaves exactly that one compatible trace. The matrices themselves continue to change; no stationary tail is being claimed.

For a separate endpoint test use the stationary matrix \(C=\left(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right)\), capacities \(3^k(1,1)\), and \(v=(1,-1)\). The unique trace evaluates \(v\) at zero, but

\[
\begin{gathered}
C^kv=(1,-1),\\
a_k(v)=-3^{-k}\longrightarrow0.
\end{gathered}
\tag{79.10}
\]

A negative coordinate persists forever. The zero projection nevertheless realizes the scalar trace zero. The order of one specified signed vector and existence of some projection with its ambient trace are different questions.

## The critical infinite path has every dyadic trace

In the fixed abstract path system \(P_n\) of 9.4–9.5 for \(A_\infty\), let \(\tau_2\) be the compatible trace with \(\delta=2\). At the cofinal even level \(n=2k\), the reachable vertices are \(2r\), \(0\leq r\leq k\). The path counts and minimal weights are

\[
\begin{gathered}
\begin{aligned}
c_{k,r}&=\binom{2k}{k-r}\\
&\quad-\binom{2k}{k-r-1},
\end{aligned}\\
\omega_{k,r}=\frac{2r+1}{4^k},\\
c_{k,r}\geq1,\\
c_{k,0}\geq2\ (k\geq2),\\
\sum_{r=0}^k(2r+1)c_{k,r}=4^k.
\end{gathered}
\tag{79.11}
\]

A binomial coefficient with a negative lower index is zero. The count formula follows from reflection at the first visit to \(-1\): all unconstrained paths ending at \(2r\) number \(\binom{2k}{k-r}\), and reflecting the prefix through that visit bijects the excluded paths with paths counted by \(\binom{2k}{k-r-1}\). Each reachable vertex has at least the path making its required initial backtracks and then moving upward. For \(k\geq2\), concatenate either of the two distinct length-four loops at zero with \(k-2\) length-two loops to obtain two root paths. The trace weights and normalization are exactly 9.6–9.7 at \(\delta=2\).

**Lemma 79.5 — bounded integer coins.** Suppose available integer coins of values \(a_0<a_1<\cdots<a_m\) have positive integer capacities \(c_i\). If \(a_0=1\) and \(a_i\leq1+\sum_{h<i}a_hc_h\) for every \(i>0\), then every integer between zero and \(\sum_i a_ic_i\) is represented with each coin used at most its capacity.

**Proof.** The first coin represents \(0,1,\ldots,c_0\). Suppose earlier coins represent every integer \(0\leq x\leq L\). Using exactly \(q\) copies of the next coin of value \(a\) gives the full interval of integers \([qa,qa+L]\), for \(0\leq q\leq c\). Consecutive intervals leave no integer gap because \(a\leq L+1\). Their union is every integer from zero through \(ca+L\). Induction proves the assertion and gives a finite algorithm: choose one such \(q\) and recurse on the earlier coins. \(\square\)

**Theorem 79.6 — the exact critical trace set.** For \(k\geq2\), the projection traces in \(P_{2k}\) under \(\tau_2\) are precisely

\[
\begin{gathered}
T_{2k}(\tau_2)=\{m/4^k\},\\
0\leq m\leq4^k,\qquad m\in\mathbb Z,\\
T(\tau_2)=\mathbb Z[1/2]\cap[0,1].
\end{gathered}
\tag{79.12}
\]

**Proof.** At the even level the available rank contributions are coins \(a_r=2r+1\), of capacities \(c_{k,r}\). For \(r\geq1\), the earlier capacity sum is at least

\[
2+\sum_{h=1}^{r-1}(2h+1)=r^2+1.
\tag{79.13}
\]

Thus \(2r+1\leq r^2+2\) for every \(r\geq1\). Lemma 79.5 and the normalization in 79.11 give all numerators between zero and \(4^k\), with valid integer ranks in each block. Conversely, all traces at this level have that denominator. Every level, including odd levels, has weights \((v+1)/2^n\), so every finite projection trace is dyadic. Every dyadic scalar in \([0,1]\) has denominator dividing \(4^k\) at a sufficiently late even level. This proves both claims. \(\square\)

Consequently, if the actual smaller tunnel system has this critical path system as a cofinal trace-preserving finite-algebra system, the selected supports of 76.4 have dyadic traces. Their residual is dyadic, Theorem 79.6 gives its finite certificate, and 78.3 supplies the exact finite full whole-tunnel partition. This is an infinite-path trace calculation, with no unique norm-trace assumption. The hypothesis is an identification of the actual \(B_j\) and their inherited traces; a generic factor realization of path relations alone does not establish it.

## A factor does not force scalar subtraction closure

The abstract path inclusions 9.5 do not depend on the parameter \(\delta\). They have a character \(\chi\): at level \(n\), read the scalar block of the unique path \((0,1,\ldots,n)\). Restriction of the next outermost block reads exactly this earlier block, so these characters are compatible and extend by norm continuity to \(P=\overline{\bigcup_nP_n}\). In particular \(\chi(e_1)=0\), whereas \(\tau_\delta(e_1)=\delta^{-2}>0\). Every \(\tau_\delta\), \(\delta\geq2\), has a factorial II₁ closure by 10.5, and still \(P\) has these distinct tracial states. The character cannot extend to a normal tracial state on that factor: its unique normalized normal trace restricts to \(\tau_\delta\).

For an exact subtraction diagnostic put \(t=\delta^{-2}\) and choose a transcendental \(t\in(1/5,1/4)\). Such numbers exist because the algebraic real numbers are countable and this interval is uncountable. The recurrence \(\mu(v+1)=\delta\mu(v)-\mu(v-1)\) gives

\[
\begin{gathered}
\mu(2r)=\delta^{2r}Q_r(t),\\
\omega_{k,r}(t)=t^{k-r}Q_r(t),\\
Q_r(t)=\sum_{h=0}^r a_{r,h}t^h,\\
a_{r,h}=(-1)^h\binom{2r-h}{h},\\
Q_r(0)=1.
\end{gathered}
\tag{79.14}
\]

The finite formula follows by induction from the same recurrence, or from the binomial identity applied to its neighboring terms. In particular every finite projection trace is an integer polynomial in \(t\) after moving to an even level:

\[
\begin{gathered}
H_q(t)=\sum_{r=0}^k h_rt^{k-r}Q_r(t),\\
0\leq h_r\leq c_{k,r},\qquad h_r\in\mathbb Z,\\
H_q(0)=h_k=\chi(q)\in\{0,1\}.
\end{gathered}
\tag{79.15}
\]

The last capacity is one because the outermost path is unique. Evaluation at zero in 79.15 is a polynomial operation agreeing with the character; zero is not a permitted finite Markov parameter in 9.3.

**Proposition 79.7 — exact failure inside a factorial path representation.** There are two disjoint physical projections in \(M=\pi_{\tau_\delta}(P)''\), each unitarily conjugate in \(M\) to a finite path projection, whose residual trace is not the trace of any finite path projection.

**Proof.** At level four take the outermost projection \(p\); its rank vector is \((0,0,1)\), with capacities \((2,3,1)\). By 79.14,

\[
\begin{gathered}
\tau_\delta(p)=1-3t+t^2,\\
\chi(p)=1,\\
0<\tau_\delta(p)<11/25<1/2,\\
R(t)=1-2\tau_\delta(p),\\
R(t)=-1+6t-2t^2,\\
0<R(t)<1.
\end{gathered}
\tag{79.16}
\]

Indeed \(1-3t+t^2\) decreases on \((1/5,1/4)\), and its upper endpoint at \(t=1/5\) is \(11/25\). The II₁ factor has two disjoint projections of this trace; factor comparison carries \(p\) onto each by a unitary. Write them \(r_1,r_2\), and set \(f=1-r_1-r_2\). Then \(\tau(f)=R(t)\).

If a finite path projection \(q\) had this trace, 79.15 would give the equality \(H_q(t)=R(t)\). Since the chosen \(t\) is transcendental, the integer polynomial \(H_q-R\) must be identically zero. Evaluation at zero would give \(\chi(q)=-1\), contradicting positivity. Thus no such finite certificate exists. Equivalently, the canonical signed level-four vector is

\[
\begin{gathered}
v=(2,3,-1),\\
\chi(v)=-1.
\end{gathered}
\tag{79.17}
\]

Its negative outermost coordinate persists in every continuation, because that new scalar block receives only the preceding outermost scalar block. The polynomial argument additionally rules out all other rank vectors with the same ambient trace. \(\square\)

This is a concrete faithful factorial path-AF diagnostic. It is not a counterexample to Popa's amenable-inclusion theorem: neither the needed actual smaller-relative-commutant identification nor relative amenability of a corresponding inclusion has been supplied. It disproves the proposed shortcut from factoriality of an AF representation to automatic residual trace certificates.

At the critical parameter \(t=1/4\), the same formal vector has trace \(3/8\) and still has negative character value. Yet the valid rank vector \((0,2,0)\) at level four has precisely that trace. Their polynomial difference is

\[
\begin{gathered}
2t(1-t)-R(t)=1-4t,\\
(1-4t)|_{t=1/4}=0.
\end{gathered}
\tag{79.18}
\]

A nonzero ambient-trace kernel has repaired the certificate. The all-trace strict condition tests a specified vector, whereas the scalar placement criterion 78.2 permits another vector in its ambient-trace fiber.

![All compatible traces control finite promotion; the critical and transcendental path traces behave differently.](figures/finite-trace-order-and-path-residuals.svg)

*Figure 79.1. The top panel records the exact nested-simplex order test 79.2–79.6. The changing two-block example is 79.7–79.9. The critical level-four ranks use weights \((1,3,5)/16\); they certify \(3/8\) despite the old signed vector's negative character. At transcendental \(t\in(1/5,1/4)\), polynomial equality forces the impossible character value \(-1\). These are exact algebraic tests; a plot of sampled parameter values would not prove the transcendental exclusion. [Editable figure source](figures/finite-trace-order-and-path-residuals.py).*

## Exercises

**Exercise 79.1 — normalized block masses (basic).** Let \(F_j=M_2\oplus M_3\) and \(v=(-1,4)\). Compute the extrema over all normalized traces. Explain why the arithmetic mean of the two ranks is irrelevant.

**Solution.** The block masses are \(m_0=2w_0,m_1=3w_1\), with \(m_0+m_1=1\). The value is \(-m_0/2+4m_1/3\); its minimum is \(-1/2\) and its maximum is \(4/3\). They are attained by the normalized trace concentrated on the respective block. A rank must be divided by its block capacity before taking convex combinations. Here the signed vector fails both finite bounds.

**Exercise 79.2 — a complete changing-system check (intermediate).** Verify the two promotions in 79.9, their complements, and their exact trace. Determine the first valid level.

**Solution.** Multiplying by \(D_0=\left(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right)\) gives \((-1,4)\) and capacities \((3,3)\). Multiplying by \(D_1=\left(\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\right)\) gives \((1,11)\) and capacities \((12,12)\). The complements are respectively \((3,-2)\), \((4,-1)\), and \((11,1)\). The first two levels fail, while level two has both vectors nonnegative. Their inherited weights are \((1/2,1/2)\), \((1/6,1/6)\), and \((1/24,1/24)\), yielding one half each time. Thus level two is the first valid promotion.

**Exercise 79.3 — every critical level-four numerator (intermediate).** Use capacities \((2,3,1)\) and weights \((1,3,5)/16\) to realize \(11/16\), \(3/8\), and \(15/16\). Explain why the coin argument includes all other numerators.

**Solution.** Valid ranks \((2,3,0)\), \((0,2,0)\), and \((1,3,1)\) give numerators \(11,6,15\), respectively. Two coins of value one give \(0,1,2\); adding up to three coins of value three gives every integer through eleven, since consecutive translates leave no gap. Adding the optional coin of value five extends the covered interval to sixteen. These are exactly the matrix-rank capacities, so each integer representation corresponds to a projection.

**Exercise 79.4 — the limiting trace obstruction (advanced).** Suppose at every sufficiently late level a promoted vector has a negative coordinate. Construct a global trace with nonpositive value. Why does this argument not prove that every scalar-equivalent vector fails?

**Solution.** At each such level choose the normalized trace concentrated on a negative block. Restrict these traces to all earlier levels and extract the diagonal subsequence used in Lemma 79.1. At the fixed original level the evaluations are negative, so their limit is at most zero. The compatible limits extend to a global tracial state. This trace evaluates the specified signed rank class; an alternative vector with the same ambient trace can differ by an element of the ambient trace's kernel but not of the newly constructed trace's kernel. Equation 79.18 gives an exact example of that distinction.

**Exercise 79.5 — why transcendence is used (advanced).** For the level-four path projection in 79.16, prove that the scalar residual is positive throughout the prescribed interval. Explain the two distinct roles of the character and transcendence.

**Solution.** At \(t=1/5\), \(R(t)=3/25\), and \(R'(t)=6-4t>0\) on the interval, so \(R(t)>3/25>0\). At \(t=1/4\), \(R(t)=3/8<1\), so throughout the open interval it lies between those two endpoint values. The character first proves that the original vector cannot promote: its value remains \(-1\). Transcendence then makes equality of scalar traces imply equality of their integer polynomials. That stronger step transfers the negative value to any alleged scalar-equivalent finite projection. At the algebraic critical parameter the stronger inference fails, as the polynomial \(1-4t\) shows.

**Exercise 79.6 — the actual residual and the remaining hypothesis (advanced).** Assume the actual smaller tunnel norm algebra has a unique tracial state. Use 76.4 and this lesson to give the exact finite full partition while retaining the old square. State what must still be proved to use that argument for an arbitrary amenable inclusion.

**Solution.** Finite alignment 78.1 represents each physically selected \(r_i\) by a projection in the fixed \(B_j\) system. Move finitely many such representatives to one level. Subtract their rank vectors from its identity vector to represent \(t=1-\sum_i\tau(r_i)=\tau(f)\). If \(0<t<1\), the unique norm trace supplies the strict hypothesis of 79.2, so a finite promotion gives a canonical projection of trace \(t\). For \(t=0\) or \(1\), use the corresponding endpoint projection. Theorem 78.2 moves the certificate to the physical \(f\) by an \(N\)-unitary conjugation of only its new finite tunnel. Theorem 78.3 retains all selected blocks and \(fA_0\), preserves both expectation orders, and improves the approximation. The finite supports sum exactly to one. For an arbitrary amenable inclusion one must still justify an actual finite residual trace certificate or another full finite family. Factoriality alone does not prove norm-trace uniqueness; alternatively one could establish the needed canonical trace-fiber order property or choose the local supports with additional compatible-trace control. No higher-prefix alignment or generating conclusion follows from this exercise alone.

## Source and scope

The precise source endpoint is Sorin Popa, [*Classification of amenable subfactors of type II*](https://doi.org/10.1007/BF02392646), Theorem 4.4.1(1), printed p.222. The finite endpoint permits a separate actual continuation for each supported summand. This lesson proves the nonstationary all-trace order criterion and exact critical-path trace computation; it does not assume the unrestricted theorem it is intended to help prove.

For the broader trace context, Stephen T. Moore's [*Limits of traces of Temperley–Lieb algebras*](https://arxiv.org/abs/2212.11592) studies positive extremal traces, and David Handelman's [*Good measures for non-simple dimension groups*](https://arxiv.org/abs/1309.7424) studies trace goodness beyond the simple case. Neither paper's classification or goodness criteria are imported here. All mathematical tests used in this lesson have their complete proofs above.

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Public domain (CC0).*
