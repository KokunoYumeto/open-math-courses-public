# Finite defects under perturbation

A parametrix converts an analytic estimate into a statement about finitely many missing or redundant directions. This lesson develops that conversion for bounded maps between complex Banach spaces. The range need not have a closed complement. In the upper semi-Fredholm case its codimension may be infinite. For parameter families we distinguish operator norm continuity from strong continuity and identify the additional compactness that makes the latter useful.

The organization is by the mechanisms used later for elliptic operators: compactness of approximate solutions, finite-dimensional enlargement, cancellation of defects, and compactness across a parameter space. No Hilbert-space orthogonal projection or adjoint theorem is used.

## 1. Contracts, defects, and closed ranges

Throughout, \(X,Y,Z\) are complex Banach spaces and every operator displayed between them is bounded and complex linear. The notation \(\mathcal L(X,Y)\) means the operator norm space. The cokernel \(Y/TX\) is initially an **algebraic** quotient; it becomes a Banach quotient when \(TX\) is closed.

The following facts are used with the precise scopes stated here. Their proofs and related examples appear in [Banach estimates, quotient spaces and compact parameter arguments](banach-foundation-bridges.md).

* **Finite-dimensional linear algebra.** Finite-dimensional linear algebra over \(\mathbb C\); every norm on a finite-dimensional vector space is equivalent to its coordinate norm; its closed bounded sets are compact and its subspaces in a normed space are closed; rank-nullity and dimension addition for finite-dimensional exact sequences.
* **Banach quotients.** If \(M\) is a closed linear subspace of a Banach space \(X\), then \(X/M\), with \(\|x+M\|=\inf_{m\in M}\|x+m\|\), is Banach. Finite products of Banach spaces are Banach.
* **Complex Hahn–Banach extension.** A continuous complex linear functional on a linear subspace of a normed complex space has a continuous complex linear extension to the whole space. Only extensions from finite-dimensional subspaces are needed here.
* **Bounded inverse theorem.** A bounded bijection between Banach spaces has a bounded inverse. Its use below always follows verification that both spaces are Banach.
* **Uniform boundedness.** If a family \(\mathcal A\subset\mathcal L(X,Y)\), with \(X\) Banach, satisfies \(\sup_{A\in\mathcal A}\|Ax\|<\infty\) for every \(x\in X\), then \(\sup_{A\in\mathcal A}\|A\|<\infty\). The family may be uncountable.
* **Compact-space facts.** Metric compactness is equivalent to sequential compactness; finite products and continuous images of compact spaces are compact; every net in a compact space has a convergent subnet; a norm-convergent net is bounded on a final segment. We also use the elementary neighborhood characterization of continuity and closed sets. No sequential compactness of the parameter space is assumed.
* **Square-summable sequences (examples only).** The square-summable complex sequences form the Banach space \(\ell^2(\mathbb N)\), with norm \((\sum_k|x_k|^2)^{1/2}\). Coordinate truncations converge to the original vector, and the coordinate vectors have norm one and pairwise distance \(\sqrt2\).

Write \(n(T)=\dim\ker T\) and \(d(T)=\dim(Y/TX)\). An **upper semi-Fredholm** map has closed range and \(n(T)<\infty\). Its index is

\[
\operatorname{ind}T=n(T)-d(T),\qquad
\operatorname{ind}T=-\infty\text{ if }d(T)\text{ is infinite}.       \tag{F1}
\]

Here all infinite algebraic dimensions are assigned the same extended value; we never subtract one infinite dimension from another. A **Fredholm** map has both defects finite and hence an integer index. When \(X,Y\) themselves are finite-dimensional, rank-nullity gives

\[
\operatorname{ind}T=\dim X-\dim Y.                              \tag{F2}
\]

Two elementary constructions will be used repeatedly.

**Finite-dimensional kernel complements.** A finite-dimensional subspace \(N\subset X\) has a bounded projection \(P:X\to N\). Choose a basis \(e_1,\ldots,e_n\) of \(N\); its coordinate functionals are continuous by the finite-dimensional facts above. Extend them using complex Hahn–Banach to \(\ell_j\in X^*\). Then \(Px=\sum_j\ell_j(x)e_j\) satisfies \(P^2=P\). Thus \(X=N\oplus M\), where \(M=\ker P\) is closed. For \(N=\{0\}\) use \(P=0\).

**Finite algebraic defect forces closed range.** If \(d(T)<\infty\), then \(TX\) is closed, even if this was not assumed. The kernel is closed because it is the inverse image of \(\{0\}\) under a continuous map. Set \(E=X/\ker T\), which is Banach by the Banach quotient fact above, and let \(\widetilde T:E\to Y\) be the induced bounded injection. Boundedness follows from \(\|Tx\|\leq\|T\|\|x+m\|\) for every \(m\in\ker T\), followed by the infimum. Choose \(y_1,\ldots,y_d\) whose classes form a basis of \(Y/TX\). The map

\[
F:E\oplus\mathbb C^d\longrightarrow Y,\qquad
F(u,a)=\widetilde Tu+\sum_{j=1}^d a_jy_j                         \tag{F3}
\]

is bounded and bijective. Both its domain and codomain are Banach, so the bounded inverse theorem makes it a homeomorphism. Its image of the closed subspace \(E\oplus\{0\}\) is \(TX\), proving the assertion. In particular, the closed-range clause in the Fredholm definition follows from finiteness of the two algebraic defects. This argument does not apply an open mapping theorem to an image whose completeness is still unknown.

We will also use: if \(R\subset Y\) is closed and \(V\subset Y\) is finite-dimensional, then \(R+V\) is closed. Indeed its image in the Banach quotient \(Y/R\) is finite-dimensional and therefore closed; \(R+V\) is the inverse image of that image under the quotient map. An arbitrary closed subspace of infinite codimension need not have a bounded projection onto it. Nothing below requires such a projection.

### Start with the two errors of an inverse {#AN03-FRE-TWO-ERRORS}

The first question is concrete: if an approximate inverse loses information on both sides, can it lose infinitely many independent directions? Keep bounded complex linear maps \(T:X\to Y\) and \(L,R:Y\to X\) between the Banach spaces above, and suppose that

\[
 LT=I_X+K_X,\qquad TR=I_Y+K_Y,\qquad K_X,\ K_Y\text{ compact}.
 \tag{F25}
\]

Here compact means that the closure of the image of the closed unit ball is compact. Write \(B_Y=\{y\in Y:\|y\|\leq1\}\) for that ball in \(Y\). Then \(T\) has closed range and both defects are finite. Here is a direct proof before studying how these defects change under perturbation.

On the closed subspace \(N=\ker T\), the first identity gives \(K_Xx=-x\). The unit ball of \(N\) is therefore compact: it is closed and is contained in the compact closure of the negative \(K_X\)-image of the unit ball of \(X\). A normed space with compact unit ball is finite dimensional. To see the needed converse explicitly, in an infinite-dimensional space choose successive unit vectors at distance at least one from the preceding finite span. Given a vector outside that span, its distance to the span has a positive minimum, attained inside a bounded finite-dimensional ball; subtract a minimizing vector and divide by the distance. The resulting vectors are pairwise separated and have no convergent subsequence. Thus \(N\) is finite dimensional.

The finite-dimensional kernel projection constructed above gives \(X=N\oplus M\), with \(M\) closed. If \(T|_M\) had no positive lower bound, there would be \(m_j\in M\) with \(\|m_j\|=1\) and \(Tm_j\to0\). Compactness gives a subsequence on which \(K_Xm_j\) converges, while

\[
                 m_j=LTm_j-K_Xm_j                              \tag{F26}
\]

then gives convergence of \(m_j\) itself. Its limit belongs to \(M\cap\ker T\), has norm one, and is therefore impossible. Consequently \(\|Tm\|\geq a\|m\|\) on \(M\) for some \(a>0\). If \(Tx_j\) converges, write \(x_j=n_j+m_j\); this lower bound makes \(m_j\) Cauchy. Its limit in the closed Banach space \(M\) maps to the proposed range limit. This proves that \(TX\) is closed.

Let \(Q:Y\to Y/TX\) be the actual Banach quotient map. The second identity gives

\[
                QK_Yy=-Qy\quad(y\in Y).                         \tag{F27}
\]

In particular \(K_Y(TX)\subset TX\), so the map induced by \(K_Y\) on the quotient is well-defined and equals minus the identity. Every quotient vector of norm at most one has a representative \(y\) with \(\|y\|<2\), by the infimum defining the quotient norm. Formula (F27) puts the entire quotient unit ball in the compact set \(Q(\overline{K_Y(2B_Y)})\), with a minus sign on that set. The quotient unit ball is closed, hence compact. The separated-vector argument just given makes \(Y/TX\) finite dimensional. This proves both finite defects without choosing a complement to an infinite-codimension range.

The two approximate inverses also agree up to a compact operator. Associativity, with every ordered factor retained, gives

\[
 \begin{split}
 LTR&=L+LK_Y=R+K_XR,\\
 R-L&=LK_Y-K_XR .
 \end{split}                                                     \tag{F28}
\]

The last two products are compact because they compose a compact map with a bounded map. Section 4 will prove how indices add under composition; Section 5 applies that rule to obtain the indices of \(L\) and \(R\). The direct argument here already explains why both error terms matter. The shift example in Section 8 shows exactly what a one-sided identity can miss.

## 2. Compactness of approximate solutions

**Lemma: a separated sequence.** In every infinite-dimensional normed space one can find unit vectors \(u_j\) with \(\|u_j-u_k\|\geq1\) for \(j\ne k\).

**Proof.** Suppose \(u_1,\ldots,u_{j-1}\) have been chosen and let \(L\) be their span. Choose \(v\notin L\). The function \(w\mapsto\|v-w\|\) on \(L\) attains its positive minimum: outside a sufficiently large ball it exceeds \(\|v\|+1\), and inside that ball compactness gives a minimum. If \(w_0\) minimizes it, put \(u_j=(v-w_0)/\|v-w_0\|\). For every \(w\in L\), minimality gives \(\|u_j-w\|\geq1\). This establishes the induction and the separation. Thus the unit ball is not norm compact. Conversely, in finite dimension its closure is compact by the finite-dimensional facts above. \(\square\)

**Theorem: the compactness test.** For \(T\in\mathcal L(X,Y)\) the following are equivalent:

1. \(T\) is upper semi-Fredholm.
2. Every bounded sequence \((x_j)\) for which \((Tx_j)\) converges has a norm-convergent subsequence.
3. There are a finite-dimensional \(N=\ker T\), a closed complement \(X=N\oplus M\), and a constant \(a>0\) such that

\[
\|Tm\|\geq a\|m\|\qquad(m\in M).                              \tag{F4}
\]

**Proof.** If 1 holds, construct \(M\) as above. The restriction \(T:M\to TX\) is a bounded bijection between Banach spaces. Its bounded inverse gives (F4). If \(M=\{0\}\), any \(a>0\) works.

Assume 3. Write a bounded sequence as \(x_j=n_j+m_j\) using the bounded projections of this direct sum. If \(Tx_j\) converges, then

\[
\|m_j-m_k\|\leq a^{-1}\|Tx_j-Tx_k\|.
\]

The sequence \(m_j\) is Cauchy and converges in the closed Banach subspace \(M\). A subsequence of the bounded sequence \(n_j\) converges in \(N\). Their sums give 2. The same lower bound shows directly that \(TM\) is closed: for a convergent sequence \(Tm_j\), the vectors \(m_j\) are Cauchy and their limit maps to the proposed range limit. Hence 3 also implies 1.

Finally assume 2. Every sequence in the closed unit ball of \(\ker T\) has a convergent subsequence, so that ball is compact and the preceding lemma makes \(\ker T\) finite-dimensional. Choose its closed complement \(M\). If no \(a>0\) satisfies (F4), there are unit vectors \(m_j\in M\) with \(\|Tm_j\|<1/j\). Condition 2 gives a convergent subsequence. Its limit lies in \(M\cap\ker T=\{0\}\) and has norm one, a contradiction. This proves 3. \(\square\)

The test concerns bounded approximate solutions. It asserts compactness after choosing a subsequence, not compactness of an inverse on all of \(Y\).

## 3. Stability without a range complement

We first isolate the part of perturbation theory where the infinite defect matters.

**Lemma: bounded-below maps retain their defect locally.** Let \(M\) be a Banach space and let \(A:M\to Y\) be bounded below: \(\|Am\|\geq a\|m\|\) for some \(a>0\). There exists an operator norm neighborhood of \(A\) consisting of injections with closed range and with the same cokernel dimension as \(A\), where “same” means either the same nonnegative integer or both infinite.

**Proof.** Every \(B\) with \(\|B-A\|<a/2\) is bounded below by \(a/2\); its range is closed by completeness of \(M\). Denote this convex, hence connected, ball of operators by \(\mathcal U\).

Suppose first that a particular \(B\in\mathcal U\) has \(d(B)=q<\infty\). Choose a \(q\)-dimensional complement \(W\) to \(BM\) in \(Y\). The map

\[
F_B:M\oplus W\longrightarrow Y,\qquad F_B(m,w)=Bm+w             \tag{F5}
\]

is a bounded bijection of Banach spaces, using the sum norm on \(M\oplus W\). If \(C\) is sufficiently close to \(B\), then \(F_C=F_B+(F_C-F_B)\) remains bijective. In detail, when \(\|F_B^{-1}(F_C-F_B)\|<1\), the series \(\sum_{j\geq0}[-F_B^{-1}(F_C-F_B)]^j\) converges in operator norm. The operator space is complete: a norm-Cauchy sequence has pointwise limits in the Banach target, these limits form a bounded linear map, and the original sequence converges to it in operator norm. Multiplication of the geometric partial sums then proves that the series is the inverse of \(I+F_B^{-1}(F_C-F_B)\). Therefore \(Y=CM\oplus W\), so \(d(C)=q\). No complement of an infinite-codimension range has been chosen.

Next, if \(d(B)>q\), choose a subspace \(W\subset Y\) of dimension \(q+1\) whose classes modulo \(BM\) are linearly independent. Then \(BM\cap W=\{0\}\). The range \(BM+W\) is closed by Section 1, and (F5), now with codomain \(BM+W\), is a bounded bijection of Banach spaces. Thus \(F_B\) is bounded below. For all sufficiently close \(C\), so is \(F_C\). In particular \(CM\cap W=\{0\}\), and \(d(C)\geq q+1\).

It follows that, on \(\mathcal U\), both the set \(\{B:d(B)=q\}\) and its complement are open: points of the complement either have another finite defect, for which the first argument applies, or have defect larger than \(q\), for which the second applies. Hence every finite-defect level is both open and closed. Connectedness of \(\mathcal U\) now completes the proof. If \(A\) has finite defect \(q\), that level is all of \(\mathcal U\). If \(A\) has infinite defect, no finite level can be nonempty, since it would be a nonempty proper open-and-closed subset. Thus every \(B\in\mathcal U\) has infinite defect. \(\square\)

The connectedness step is essential: for each fixed finite-dimensional transverse space one gets a perturbation radius, but those radii need not have a positive lower bound as its dimension increases.

**Theorem: upper semi-Fredholm perturbations.** If \(T:X\to Y\) is upper semi-Fredholm, there is \(\varepsilon>0\) such that \(\|E\|<\varepsilon\) implies

\[
T+E\text{ is upper semi-Fredholm},\quad
n(T+E)\leq n(T),\quad
\operatorname{ind}(T+E)=\operatorname{ind}T.                    \tag{F6}
\]

The assertion includes index \(-\infty\).

**Proof.** Put \(N=\ker T\), \(n=\dim N\), and choose \(X=N\oplus M\) with \(M\) closed. The operator \(A=T|_M\) is bounded below. For sufficiently small \(E\), the preceding lemma applies to \(B=(T+E)|_M\). Thus \(B\) is injective with closed range and \(d(B)=d(T)\) in the finite/infinite convention of the lemma.

Let \(Q:Y\to Y/BM\) be the quotient map and consider the finite-dimensional-domain map

\[
D:N\longrightarrow Y/BM,\qquad Dn=Q((T+E)n).                   \tag{F7}
\]

If \(v\in\ker D\), there is a unique \(m\in M\) with \(Bm=-(T+E)v\). Consequently \(m+v\in\ker(T+E)\), and projection onto \(N\) gives a linear isomorphism \(\ker(T+E)\cong\ker D\). If \(k=\dim\ker D\), then \(k\leq n\) and \(\dim DN=n-k\). The range

\[
(T+E)X=BM+(T+E)N
\]

is closed as a finite-dimensional enlargement of a closed subspace. Its cokernel is naturally \((Y/BM)/DN\). If \(d(T)=r<\infty\), its dimension is \(r-(n-k)\); hence \(\operatorname{ind}(T+E)=k-r+n-k=n-r\). If \(d(T)\) is infinite, quotienting \(Y/BM\) by the finite-dimensional \(DN\) leaves it infinite-dimensional, giving index \(-\infty\). This proves every assertion. \(\square\)

**Corollary.** The Fredholm locus in \(\mathcal L(X,Y)\) is open; its kernel dimension is upper semicontinuous and its index is locally constant, hence constant on each connected component. The upper semi-Fredholm locus has the same statements with the extended index. Here upper semicontinuity of kernel dimension means that near \(T_0\), \(n(T)\leq n(T_0)\). No assertion is made that the kernel subspaces themselves vary continuously at a dimension jump.

## 4. Adding and cancelling defects

**Theorem: composition.** If \(A:X\to Y\) and \(B:Y\to Z\) are Fredholm, then \(BA\) is Fredholm and

\[
\operatorname{ind}(BA)=\operatorname{ind}A+\operatorname{ind}B.  \tag{F8}
\]

**Proof.** There is an exact sequence of algebraic vector spaces

\[
0\longrightarrow\ker A\longrightarrow\ker BA
\mathop{\longrightarrow}^{A}\ker B
\longrightarrow Y/AX
\mathop{\longrightarrow}^{B} Z/BAX
\longrightarrow Z/BY\longrightarrow0.                         \tag{F9}
\]

The first arrow is inclusion. The arrow from \(\ker B\) takes \(y\) to its class modulo \(AX\); the next takes \([y]\) to \([By]\), and the last takes \([z]\) modulo \(BAX\) to \([z]\) modulo \(BY\). These are well-defined. Exactness at \(\ker BA\) is the definition of \(\ker A\); exactness at \(\ker B\) says \(y\in\ker B\cap AX\) exactly when \(y=Ax\) with \(BAx=0\). At \(Y/AX\), the condition \(By\in BAX\) means \(y-Ax\in\ker B\) for some \(x\). At \(Z/BAX\), a class dies modulo \(BY\) exactly when it has representative \(By\). The last map is surjective.

This also proves finiteness before we use any index formula. The map \(\ker BA\to\ker B\) has finite-dimensional kernel \(\ker A\) and finite-dimensional image, so \(\ker BA\) is finite-dimensional. The kernel of \(Z/BAX\to Z/BY\) is an image of the finite-dimensional \(Y/AX\), and its target is finite-dimensional. Thus \(Z/BAX\) is finite-dimensional. Section 1 then proves that \(BAX\) is closed. All spaces in (F9) are now finite-dimensional, so the alternating sum of their dimensions is zero, which is (F8). For completeness, that alternating-sum rule follows by splitting each dimension into the dimensions of the incoming and outgoing images; each image occurs twice with opposite signs. \(\square\)

Finite direct sums of Fredholm maps are Fredholm, and their indices add, since their kernels and cokernels are the corresponding direct sums. A bounded isomorphism has index zero. These facts will be useful for changing a system's domain by adding finitely many variables or equations.

## 5. Compact errors and approximate inverses

An operator \(K:X\to Y\) is **compact** if the closure of the image of its closed unit ball is compact in \(Y\). Since \(Y\) is a metric space, this is equivalent to every bounded sequence \((x_j)\) having a subsequence on which \(Kx_j\) converges. Multiplication on either side by a bounded operator preserves compactness: on the right a bounded ball maps into a multiple of a bounded ball, and on the left the continuous image of a compact set is compact. Sums of compact maps are compact by compactness of the product of the two compact image closures. Finite-rank maps are compact by finite-dimensional compactness.

**Theorem: compact perturbations.** If \(T\) is upper semi-Fredholm and \(K:X\to Y\) is compact, then \(T+K\) is upper semi-Fredholm and

\[
\operatorname{ind}(T+K)=\operatorname{ind}T.                    \tag{F10}
\]

In particular a compact perturbation of a Fredholm map is Fredholm with the same integer index.

**Proof.** For a bounded sequence \((x_j)\) with \((T+K)x_j\) convergent, pass to a subsequence on which \(Kx_j\) converges. Then \(Tx_j\) converges, and Section 2 supplies a further convergent subsequence. The compactness test proves that \(T+K\) is upper semi-Fredholm. The same reasoning applies to every \(T+sK\), \(0\leq s\leq1\). This is an operator norm continuous path entirely in that locus. The local constancy from Section 3 and connectedness of \([0,1]\) imply (F10), including its infinite-index case. \(\square\)

**Theorem: two possibly different parametrices.** Suppose \(L,R:Y\to X\) satisfy

\[
LT=I_X+K_X,\qquad TR=I_Y+K_Y,                                 \tag{F11}
\]

with \(K_X,K_Y\) compact. Then \(T,L,R\) are Fredholm,

\[
\operatorname{ind}L=\operatorname{ind}R=-\operatorname{ind}T,
\qquad R-L\text{ is compact}.                                 \tag{F12}
\]

**Proof.** The preceding theorem applied to the identity makes \(I_X+K_X\) and \(I_Y+K_Y\) Fredholm of index zero. Since \(\ker T\subset\ker(LT)\), the kernel of \(T\) is finite-dimensional. Since \((TR)Y\subset TX\), the quotient \(Y/TX\) is a quotient of the finite-dimensional \(Y/(TR)Y\). It is finite-dimensional, so \(TX\) is closed by Section 1. Thus \(T\) is Fredholm.

Associativity gives \(LTR=L+LK_Y=R+K_XR\), hence

\[
R-L=LK_Y-K_XR.                                                \tag{F13}
\]

Both terms are compact. Therefore \(TL-I_Y=(TR-I_Y)+T(L-R)\) and \(RT-I_X=(LT-I_X)+(R-L)T\) are compact too. Apply the same finite-kernel/finite-cokernel argument to \(L\), using \(T\) on both sides, and then to \(R\); this proves they are Fredholm without presupposing their indices. Finally, composition and (F11) yield \(\operatorname{ind}L+\operatorname{ind}T=0\) and \(\operatorname{ind}T+\operatorname{ind}R=0\). \(\square\)

There is also a converse useful for constructions. If \(T\) is Fredholm, choose \(X=N\oplus M\) as before and \(Y=TX\oplus W\), with \(W\) finite-dimensional. The inverse of \(T|_M\), extended by zero on \(W\), is a bounded \(S:Y\to X\). To verify boundedness of the projection along \(W\), apply the bounded inverse theorem to the bounded bijection \(TX\oplus W\to Y\). Then \(ST-I_X\) and \(TS-I_Y\) are negatives of the projections onto \(N\) and \(W\), respectively. They have finite rank. This construction uses a range complement only in the finite-codimension Fredholm case.

## 6. Strong families: the compactness mechanism

Let \(I\) be a compact topological space. The proofs below do not require it to be metrizable; they also do not require a Hausdorff assumption on \(I\). A family \(t\mapsto T_t\in\mathcal L(X,Y)\) is **strongly continuous** if \(t\mapsto T_tx\) is norm continuous for each fixed \(x\in X\). A family \(\{K_t:X\to X\}_{t\in I}\) is **collectively compact** if

\[
\overline{\{K_tx:t\in I,\ \|x\|\leq1\}}\quad
\text{is compact in }X.                                      \tag{F14}
\]

The operators \(K_t\) need not be continuous in operator norm. Individual compactness says less than (F14).

Three compactness observations will control the family.

**Uniform boundedness and joint continuity.** For each \(x\), the image \(\{T_tx:t\in I\}\) is compact, hence bounded. Uniform boundedness gives \(C_T=\sup_t\|T_t\|<\infty\). If \(t_\alpha\to t\) and \(x_\alpha\to x\), then

\[
\|T_{t_\alpha}x_\alpha-T_tx\|
\leq C_T\|x_\alpha-x\|+\|(T_{t_\alpha}-T_t)x\|\longrightarrow0. \tag{F15}
\]

Thus \((t,x)\mapsto T_tx\) is jointly continuous. The same conclusions hold for a strongly continuous family \(S_t:Y\to X\).

**A closed-projection fact.** If \(C\) is compact and \(F\subset I\times C\) is closed, its projection onto \(I\) is closed. Indeed, for \(t_0\) outside that projection, every \(c\in C\) has a product neighborhood \(U_c\times V_c\) of \((t_0,c)\) disjoint from \(F\). A finite subcover of the \(V_c\)'s gives a neighborhood \(\bigcap U_c\) disjoint from the projection. This proves the fact even when \(I\) is not Hausdorff.

**Compactness of normalized vectors with constrained images.** Suppose \(T_t,S_t\) are strongly continuous, and \(S_tT_t-I_X=K_t\) is collectively compact. If \(W\subset Y\) is finite-dimensional, then all vectors \(x\) satisfying

\[
\|x\|=1,\qquad T_tx\in W\quad\text{for some }t\in I             \tag{F16}
\]

lie in a single compact subset of \(X\). To see this, put

\[
D_W=\{w\in W:\|w\|\leq C_T\},\quad
C_K=\overline{\{K_tx:t\in I,\|x\|\leq1\}}.
\]

The set \(D_W\) is compact. Joint continuity of \(S\) makes \(C_S=\{S_tw:t\in I,w\in D_W\}\) compact as the image of \(I\times D_W\). The identity

\[
x=S_tT_tx-K_tx                                                \tag{F17}
\]

places every vector in (F16) in the compact difference set \(C_S-C_K\). This is the step where collective compactness is used, and it controls moving vectors as well as moving parameters.

**Local transversality lemma.** Under the hypotheses of the preceding observation, fix \(t_0\in I\), a closed subspace \(M\subset X\), and a finite-dimensional subspace \(W\subset Y\). Suppose \(T_{t_0}|_M\) is injective and \(T_{t_0}M\cap W=\{0\}\). Then on some neighborhood \(U\) of \(t_0\), \(T_t|_M\) is injective and \(T_tM\cap W=\{0\}\).

**Proof.** A failure at \(t\) is exactly the existence of a unit vector \(x\in M\) with \(T_tx\in W\): any nonzero witness can be normalized, including a kernel vector. All witnesses lie in the single compact set \(C=C_S-C_K\). By joint continuity, the subset

\[
F=\{(t,x)\in I\times C:x\in M,\ \|x\|=1,\ T_tx\in W\}
\]

is closed: \(M\), the unit sphere, and \(W\) are closed. Its projection is therefore closed by the closed-projection fact. The assumptions exclude \(t_0\) from the projection; its complement is the required neighborhood. Equivalently, one could argue with a net of failures approaching \(t_0\), extract a convergent subnet of their unit vectors in \(C\), and get a nonzero vector in \(M\) mapped into \(W\) at \(t_0\). A sequence would not suffice for an arbitrary parameter space. \(\square\)

## 7. Index stability for collectively compact families

**Theorem.** Let \(I\) be compact, and let \(T_t:X\to Y\), \(S_t:Y\to X\) be strongly continuous. Assume both error families

\[
K_{X,t}=S_tT_t-I_X,\qquad K_{Y,t}=T_tS_t-I_Y                   \tag{F18}
\]

are collectively compact on their respective spaces. Then:

1. Each \(T_t,S_t\) is Fredholm, and \(\operatorname{ind}S_t=-\operatorname{ind}T_t\).
2. Both functions \(t\mapsto\dim\ker T_t\) and \(t\mapsto\dim\ker S_t\) are upper semicontinuous.
3. \(t\mapsto\operatorname{ind}T_t\) is locally constant, hence constant if \(I\) is connected.

**Proof.** Collective compactness implies compactness of each individual error, so Section 5, with \(L=R=S_t\), gives 1.

Fix \(t_0\). Put \(N=\ker T_{t_0}\), \(n=\dim N\), and choose a closed complement \(X=N\oplus M\). Use the local transversality lemma first with \(W=\{0\}\). On a neighborhood of \(t_0\), \(T_t|_M\) is injective. Projection \(X\to N\) is therefore injective on \(\ker T_t\): if the projection of a kernel vector vanishes, that vector belongs to \(M\cap\ker T_t=\{0\}\). Consequently \(\dim\ker T_t\leq n\). Interchanging \(T\) and \(S\), and \(X\) and \(Y\), proves upper semicontinuity for \(\ker S_t\).

To control the index, choose a finite-dimensional complement \(W\) to \(T_{t_0}X=T_{t_0}M\), and write \(r=\dim W=d(T_{t_0})\). The transversality lemma gives a neighborhood on which \(T_t|_M\) is injective and \(T_tM\cap W=\{0\}\). The inclusion \(J:M\hookrightarrow X\) is Fredholm of index \(-n\), because it is injective, has closed range, and \(X/M\cong N\). Therefore composition gives

\[
\operatorname{ind}(T_tJ)=\operatorname{ind}T_t-n.
\]

Since \(T_tJ\) is injective, this reads

\[
\operatorname{ind}T_t=n-\dim(Y/T_tM).                         \tag{F19}
\]

Transversality makes \(W\to Y/T_tM\) injective, so \(\dim(Y/T_tM)\geq r\). Hence, near \(t_0\),

\[
\operatorname{ind}T_t\leq n-r=\operatorname{ind}T_{t_0}.        \tag{F20}
\]

The same argument applied to \(S_t\) gives \(\operatorname{ind}S_t\leq\operatorname{ind}S_{t_0}\) on another neighborhood. Part 1 turns this into the reverse inequality for \(\operatorname{ind}T_t\). On the intersection both inequalities hold, proving local constancy. A locally constant integer-valued function on a connected space is constant: each value's inverse image is open and its complement is a union of other such open sets. This proves 3. \(\square\)

The argument used the compactness of \(I\) to obtain uniform operator bounds and a compact image of \(I\times D_W\). It used compactness in the Banach-space fibers to exclude bad parameters. It never replaced strong convergence by operator norm convergence.

**Editorial consequence: different approximate inverses and the full local finite-dimensional reduction.** The same strong-family mechanism proves more than local index constancy. Retain the original complex Banach spaces, their norms, the compact parameter space \(I\), and strong continuity. Let the left and right maps now be different:

\[
 T_t:X\longrightarrow Y,\qquad L_t,R_t:Y\longrightarrow X,\qquad
 K_{X,t}=L_tT_t-I_X,\qquad K_{Y,t}=T_tR_t-I_Y.                 \tag{FS1}
\]

Suppose both original error families in (FS1) are collectively compact. Then all three operators are Fredholm at each parameter, their kernel and cokernel dimensions are upper semicontinuous, and

\[
 \operatorname{ind}L_t=\operatorname{ind}R_t=-\operatorname{ind}T_t,
 \qquad \operatorname{ind}T_t\text{ is locally constant}.       \tag{FS2}
\]

There is no Hausdorff or countability assumption on \(I\). If \(I\) is empty there is no parameter and every assertion about a parameter is vacuous. Assume it is nonempty for the proof. Write

\[
 \begin{aligned}
 C_T&=\sup_{t\in I}\|T_t\|,& C_L&=\sup_{t\in I}\|L_t\|,&
 C_R&=\sup_{t\in I}\|R_t\|,\\
 \mathcal C_X&=\overline{\{K_{X,t}x:t\in I,\|x\|_X\leq1\}},&
 \mathcal C_Y&=\overline{\{K_{Y,t}y:t\in I,\|y\|_Y\leq1\}}.
 \end{aligned}                                                \tag{FS3}
\]

Section6 gives all three finite operator bounds and joint continuity of all three evaluation maps. Both compact sets in (FS3) contain zero. Every ordered product in the original identity (F13) remains:

\[
 D_t=R_t-L_t=L_tK_{Y,t}-K_{X,t}R_t.                            \tag{FS4}
\]

The set \(\mathcal C_{LY}=\{L_tz:t\in I,z\in\mathcal C_Y\}\) is compact as the continuous image of \(I\times\mathcal C_Y\). For a unit \(y\), the second term in (FS4) lies in \(C_R\mathcal C_X\): when \(C_R>0\), use the original vector \(R_ty/C_R\); when \(C_R=0\), it is zero. Thus the closure \(\mathcal C_D\) of all \(D_t\)-images of the unit ball is contained in the compact set \(\mathcal C_{LY}-C_R\mathcal C_X\) and is compact. Here compact subsets of the normed target are closed, so a closed subset of that compact set is compact. No operator-norm continuity of \(D_t\) is presumed; it is strongly continuous as \(R_t-L_t\).

The two additional errors have the complete formulas

\[
 T_tL_t-I_Y=K_{Y,t}-T_tD_t,\qquad
 R_tT_t-I_X=K_{X,t}+D_tT_t.                                   \tag{FS5}
\]

The first family is collectively compact because its unit-ball images lie in
\(\mathcal C_Y-\{T_tz:t\in I,z\in\mathcal C_D\}\), a compact set by joint continuity. The second lies in \(\mathcal C_X+C_T\mathcal C_D\), also compact; its zero-bound case is direct. Apply Section7 first to \((T_t,L_t)\), then to \((T_t,R_t)\). Section5 already proves the pointwise Fredholm statements and both opposite indices. Section7 proves local index constancy and upper semicontinuity of all three kernel dimensions. For each of the three operators, the identity
\(d(A_t)=n(A_t)-\operatorname{ind}A_t\) then proves upper semicontinuity of its cokernel dimension on a neighborhood where its index is constant. This proves (FS2) with both defects, using the actual two error families.

Fix \(t_0\in I\). Retain a bounded projection \(P:X\to N=\ker T_{t_0}\), its actual closed complement \(M=\ker P\), and a finite-dimensional subspace \(W\subset Y\) satisfying the original direct sum \(Y=T_{t_0}M\oplus W\). Give \(M,N,W\) their inherited original norms and each displayed finite product its sum norm. Put \(n=\dim N\), \(r=\dim W\). There is a neighborhood \(U\) of \(t_0\) and \(a>0\) such that

\[
 \begin{aligned}
 F_t:M\oplus W&\longrightarrow Y,& F_t(m,w)&=T_tm+w,\\
 G_t=F_t^{-1}:Y&\longrightarrow M\oplus W,&
 \|F_t(m,w)\|_Y&\geq a(\|m\|_X+\|w\|_Y),& \|G_t\|&\leq a^{-1}
 \quad(t\in U).
 \end{aligned}                                                \tag{FS6}
\]

**Proof of the full bound and surjectivity.** First prove the bound. If no neighborhood and positive bound existed, for each neighborhood \(V\) of \(t_0\) and each positive integer \(j\), choose \(t_{V,j}\in V\), \(m_{V,j}\in M\), \(w_{V,j}\in W\) with
\(\|m_{V,j}\|_X+\|w_{V,j}\|_Y=1\) and \(\|T_{t_{V,j}}m_{V,j}+w_{V,j}\|_Y<1/j\). Order these pairs by decreasing neighborhoods and increasing integers. This gives a net \(t_\alpha\to t_0\) with \(F_{t_\alpha}(m_\alpha,w_\alpha)\to0\). The unit ball of \(W\) is compact, so pass to a subnet where \(w_\alpha\to w\). Collective compactness of \(K_X\) gives a further subnet where \(K_{X,t_\alpha}m_\alpha\to k\). The original identity, with all terms in their original order, is

\[
 m_\alpha
 =L_{t_\alpha}F_{t_\alpha}(m_\alpha,w_\alpha)
       -L_{t_\alpha}w_\alpha-K_{X,t_\alpha}m_\alpha
 \longrightarrow -L_{t_0}w-k=:m.                             \tag{FS7}
\]

Its first term tends to zero by \(C_L\), and its second by joint continuity. The closedness of \(M\) gives \(m\in M\), and the original norm sum remains \(\|m\|_X+\|w\|_Y=1\). Joint continuity of \(T\) gives \(T_{t_0}m+w=0\), contradicting the original direct sum and injectivity of \(T_{t_0}|_M\). This proves the bound on a neighborhood. If \(M\oplus W=\{0\}\), its bound holds for any \(a>0\) without a unit-vector argument.

The bound makes \(F_t\) injective, \(T_t|_M\) injective and \(T_tM\cap W=\{0\}\). Shrink the neighborhood also to one on which \(\operatorname{ind}T_t=n-r\), already proved in (FS2). The original inclusion \(J:M\hookrightarrow X\) is Fredholm of index \(-n\), so (F8) makes \(T_tJ\) Fredholm of index \(-r\). Since it is injective, \(\dim(Y/T_tM)=r\). The actual map \(W\to Y/T_tM\) is injective, and its domain and target both have dimension \(r\); therefore it is onto. This proves \(Y=T_tM\oplus W\) and surjectivity of \(F_t\). The bound gives the inverse estimate in (FS6). When the domain of \(F_t\) is zero, this dimension argument gives \(Y=0\); the unique zero-space maps are the inverse maps and have norm zero.

Write \(G_ty=(Q_{M,t}y,Q_{W,t}y)\). Both coordinate operators have norm at most \(a^{-1}\). The inverse family is strongly continuous on \(U\). For any fixed \(y\in Y\), and any fixed parameter \(s\in U\), retain the full inverse identity

\[
 (G_t-G_s)y=G_t(F_s-F_t)G_sy,\qquad
 \|(G_t-G_s)y\|_{M\oplus W}
 \leq a^{-1}\|(T_s-T_t)Q_{M,s}y\|_Y\longrightarrow0
 \quad(t\to s).                                               \tag{FS8}
\]

Strong continuity is the conclusion here; this equation does not assert operator-norm continuity on the full infinite-dimensional space.

The actual finite-dimensional receiving operator and its accompanying component are

\[
 A_t=Q_{M,t}T_t|_N:N\longrightarrow M,\qquad
 B_t=Q_{W,t}T_t|_N:N\longrightarrow W,
 \qquad \|A_t\|,\|B_t\|\leq a^{-1}C_T.                       \tag{FS9}
\]

They are operator-norm continuous on \(U\). For a fixed vector of \(N\), this follows from (FS8), strong continuity of \(T\) and the uniform inverse bound. To pass to operator norm, take any actual basis \(f_1,\ldots,f_n\) of \(N\) and its continuous coordinate functionals \(\lambda_1,\ldots,\lambda_n\). For either difference \(E_t\),
\(\|E_t\|\leq\sum_{j=1}^n\|\lambda_j\|\|E_tf_j\|\to0\). For \(N=0\), both operators are zero and the empty sum is zero. No moving infinite-dimensional basis is required.

Define the complete coordinate maps on the original spaces by

\[
 \begin{aligned}
 U_t:X&\longrightarrow M\oplus N,\\
 U_tx&=((I_X-P)x+A_tPx,\ Px),\\
 U_t^{-1}:M\oplus N&\longrightarrow X,\\
 U_t^{-1}(m',n')&=m'-A_tn'+n',\\
 G_tT_tU_t^{-1}(m',n')&=(m',B_tn'),\\
 \|U_t\|&\leq\|I_X-P\|+(1+a^{-1}C_T)\|P\|,\\
 \|U_t^{-1}\|&\leq1+a^{-1}C_T.
 \end{aligned}                                                \tag{FS10}
\]

Every sum and sign in (FS10) is needed. To check both inverse products, use \(P|_N=I_N\), \(P|_M=0\) and \(A_tN\subset M\). To check the operator identity, expand
\(T_t(m'-A_tn'+n')=T_tm'-T_tA_tn'+T_tn'\), and use
\(G_tT_tn'=(A_tn',B_tn')\) and \(G_tT_tm'=(m',0)\). The two original \(A_tn'\) terms cancel only after their images are displayed. The stated bounds use the inherited original norms and the complete sum norm; no norm of \(X\) or \(Y\) has been changed. Both \(U_t\) and \(U_t^{-1}\) are norm continuous because the only moving term factors through the actual finite-dimensional \(N\).

The exact kernel and cokernel maps are consequently

\[
 \begin{aligned}
 \ker B_t&\longrightarrow\ker T_t,& n'&\longmapsto n'-A_tn',
 & (\text{inverse})\quad x&\longmapsto Px,\\
 Y/T_tX&\longrightarrow W/B_tN,&[y]&\longmapsto[Q_{W,t}y],
 & (\text{inverse})\quad[w]&\longmapsto[w].
 \end{aligned}                                                \tag{FS11}
\]

For the quotient maps, \(Q_{W,t}T_t(n'+m)=B_tn'\), which proves that the first map is well-defined. Conversely, if \(Q_{W,t}y=B_tn'\), write \(y=T_tQ_{M,t}y+B_tn'\) and use
\(B_tn'=T_t(n'-A_tn')\); thus \(y\in T_tX\). Every \(w\in W\) is its own \(W\)-coordinate, giving surjectivity and both inverse products. These are Banach quotient maps: \(T_tX\) is closed by the proved Fredholm property, and \(B_tN\) is finite-dimensional and closed. Their original quotient norms satisfy both comparisons

\[
 \|y+T_tX\|_{Y/T_tX}
 \leq\|Q_{W,t}y+B_tN\|_{W/B_tN}
 \leq a^{-1}\|y+T_tX\|_{Y/T_tX}.                              \tag{FS12}
\]

The right inequality follows by applying \(Q_{W,t}\) to every original representative and taking the infimum. For the left inequality, the class of \(y\) equals that of \(Q_{W,t}y\), and the class of every \(B_tn'\) is zero in \(Y/T_tX\). Take the infimum over those original vectors in \(W\). Thus (FS11) proves actual bounded inverse morphisms, preserving both quotient norms. Finally rank-nullity on the original \(B_t:N\to W\) gives

\[
 n(T_t)=n-\operatorname{rank}B_t,\qquad
 d(T_t)=r-\operatorname{rank}B_t,\qquad
 \operatorname{ind}T_t=n-r.                                   \tag{FS13}
\]

This reduction identifies the precise finite-dimensional object controlling each changing defect. It retains the original infinite-dimensional operators, domains, targets and both compact errors. It neither makes a kernel dimension constant through a rank jump nor upgrades strong continuity of the original operators to operator-norm continuity. In zero-dimensional cases all displayed maps, empty sums, quotients and rank formulas keep their indicated domains and values. These are standard consequences of the chapter's proved mechanisms; no novelty is claimed.

## 8. Four ways defects behave

The examples in this section index their sequence coordinates by
\(\mathbb N=\{1,2,\ldots\}\), so their first vector is \(e_1\). The Banach
prerequisite constructs the space with coordinates indexed by
\(\mathbb N_0=\{0,1,\ldots\}\). Retain both spaces, denoted \(H_1\) and
\(H_0\), and compare them by

\[
 \begin{aligned}
 \mathcal U:H_0&\longrightarrow H_1,&
       (\mathcal Ux)_j&=x_{j-1}\quad(j\geq1),\\
 \mathcal U^{-1}:H_1&\longrightarrow H_0,&
       (\mathcal U^{-1}z)_k&=z_{k+1}\quad(k\geq0),\\
 \|\mathcal Ux\|_{H_1}^2
 &=\sum_{j=1}^{\infty}|x_{j-1}|^2
  =\sum_{k=0}^{\infty}|x_k|^2=\|x\|_{H_0}^2.
 \end{aligned}
 \tag{F20a}
\]

The two formulas compose to the identity in each indicated domain, and the
norm identity proves that both are bounded isometries. Thus completeness and
coordinate-truncation convergence transfer from \(H_0\) to \(H_1\), with
\(\mathcal Ue_k^{(0)}=e_{k+1}^{(1)}\). Every \(H\) below means \(H_1\).
In particular, the backward shift's first zero is at coordinate one; the
formula \(Ve_{k+1}=e_k\) below has \(k\geq1\). This specifies the exact
comparison with the prerequisite and every endpoint of the shift formulas.

**An infinite defect with a stable injection.** On \(H=\ell^2(\mathbb N)\), define \(J:H\to H\) by \(Je_k=e_{2k}\). Then \(\|Jx\|=\|x\|\), its range is the closed even-coordinate subspace, and its cokernel contains all odd coordinates. Thus \(\operatorname{ind}J=-\infty\). Every \(E\) with \(\|E\|<1/2\) gives an injective \(J+E\) with closed range and infinite cokernel by Section 3. This is a genuine part of the theorem; finite-defect matrix reduction alone would not establish it. This particular example has a complemented range, but the proof of the theorem did not use that feature.

**A disappearing kernel with unchanged index.** On \(H=\ell^2(\mathbb N)\), let \(P\) project onto \(\mathbb Ce_1\) and define \(T_z=I-P+zP\), \(z\in\mathbb C\). At \(z=0\), kernel and cokernel each have dimension one. At \(z\ne0\), \(T_z\) is invertible. The family is norm continuous, the kernel dimension can fall when moving away from zero, and the index stays zero.

**A one-sided exact inverse and a defect on the other side.** Let \(U:H\to H\) be the unilateral shift \(Ue_k=e_{k+1}\), and let \(V\) be the backward shift, \(Ve_1=0\), \(Ve_{k+1}=e_k\). Then \(VU=I\) and \(UV=I-P\). Thus \(U\) is Fredholm of index \(-1\), and \(V\) has index \(1\). The identity \(VU=I\) does not imply surjectivity of \(U\); the other error measures its missing direction.

**A strong family whose index changes.** Set \(I=\{0\}\cup\{1/n:n\geq1\}\) with its usual compact topology. Put \(T_0=S_0=I_H\). For \(t=1/n\), let \(T_t\) act as the identity on \(e_1,\ldots,e_n\) and as the unilateral shift on the remaining tail; let \(S_t\) be its tail backward shift. Explicitly,

\[
T_{1/n}e_k=\begin{cases}e_k&k\leq n,\\e_{k+1}&k>n,\end{cases}
\qquad
S_{1/n}e_k=\begin{cases}e_k&k\leq n,\\0&k=n+1,\\e_{k-1}&k>n+1.\end{cases} \tag{F21}
\]

The two families have norms at most one and converge strongly to the identity: their difference from the identity on a vector is bounded by twice the norm of that vector's tail after coordinate \(n\). Yet \(S_{1/n}T_{1/n}=I\), whereas \(T_{1/n}S_{1/n}=I-P_{n+1}\). All errors have finite rank, but \(\{P_{n+1}e_{n+1}\}\) has no convergent subsequence, so the second error family is not collectively compact. The indices are \(-1\) at \(1/n\) and \(0\) at \(0\). Also \(\dim\ker S_{1/n}=1>\dim\ker S_0\). Thus individual compactness of strong-family errors does not imply either conclusion. Here \(\|(T_{1/n}-I)e_{n+1}\|=\sqrt2\), so there is no conflict with norm stability.

## 9. Problems with full solutions

**Problem 1: a quantitative estimate with a finite-dimensional defect.** Given an upper semi-Fredholm \(T\), a bounded projection \(P\) onto its kernel, and a lower bound \(a\) for \(T\) on \(M=\ker P\), prove an estimate valid for every \(x\in X\). Then prove the converse when \(P\) is replaced by any compact operator \(C:X\to Z\) into a Banach space.

**Solution.** Since \(T(x-Px)=Tx\), (F4) gives

\[
\|x\|\leq\|Px\|+a^{-1}\|Tx\|.                                 \tag{F22}
\]

Conversely suppose \(\|x\|\leq A\|Tx\|+B\|Cx\|\) for all \(x\), where \(C\) is compact and \(A,B\geq0\). If \((x_j)\) is bounded and \(Tx_j\) converges, choose a subsequence on which \(Cx_j\) converges. Applying the estimate to \(x_j-x_k\) makes this subsequence Cauchy. Completeness of \(X\) makes it convergent, and Section 2 proves that \(T\) is upper semi-Fredholm. This criterion does not require finite codimension. It is the form frequently produced by an elliptic estimate with a compact lower-order term.

**Problem 2: adding variables and equations.** Let \(T:X\to Y\) be Fredholm, \(E,F\) finite-dimensional, and let

\[
\mathcal T:X\oplus E\to Y\oplus F,\qquad
\mathcal T(x,e)=(Tx+Ae,Bx+De),                                 \tag{F23}
\]

where all displayed maps are bounded. Determine its index without assuming invertibility of \(D\).

**Solution.** Start with \(\mathcal T_0(x,e)=(Tx,0)\). Its kernel is \(\ker T\oplus E\), its range \(TX\oplus\{0\}\) is closed, and its cokernel is \((Y/TX)\oplus F\). Hence \(\operatorname{ind}\mathcal T_0=\operatorname{ind}T+\dim E-\dim F\). The difference \(\mathcal T-\mathcal T_0\) has range contained in \(AE\oplus F\), a finite-dimensional space. It is compact, so Section 5 gives the same index for \(\mathcal T\). No block invertibility is needed.

**Problem 3: a rotation witnessing composition.** For Fredholm \(A:X\to Y\), \(B:Y\to Z\), use a path of block operators to connect \(A\oplus B\) with a direct sum containing \(BA\). Verify the endpoints and the Fredholm property at every parameter.

**Solution.** On \(Y\oplus Y\) let \(R_\theta(u,v)=(u\cos\theta+v\sin\theta,-u\sin\theta+v\cos\theta)\), which is a bounded isomorphism with inverse \(R_{-\theta}\). Define

\[
F_\theta=
\begin{pmatrix}I_Y&0\\0&B\end{pmatrix}
R_\theta
\begin{pmatrix}A&0\\0&I_Y\end{pmatrix}:X\oplus Y\to Y\oplus Z.
                                                                    \tag{F24}
\]

Each outer factor is Fredholm by direct sums and the middle factor is invertible. Section 4 therefore makes every \(F_\theta\) Fredholm. The coefficients depend continuously in norm on \(\theta\). At \(\theta=0\), \(F_0(x,y)=(Ax,By)\); at \(\theta=\pi/2\), \(F_{\pi/2}(x,y)=(y,-BAx)\). Domain exchange and multiplication by \(-1\) are isomorphisms, so the latter has index \(\operatorname{ind}(BA)\). The index is constant along the path. This is a second geometric check on (F8); the exact-sequence proof established composition first, so using it to justify this path is not circular.

**Problem 4: local uniform control of a strong family.** Under the assumptions of Section 7, fix \(t_0\), and a closed complement \(M\) of \(\ker T_{t_0}\). Prove that there are a neighborhood \(U\) of \(t_0\) and \(c>0\) such that \(\|T_tm\|\geq c\|m\|\) for all \(t\in U,m\in M\).

**Solution.** If no such pair existed, for every neighborhood \(U\) of \(t_0\) and every positive integer \(j\) choose \(t_{U,j}\in U\) and a unit \(m_{U,j}\in M\) with \(\|T_{t_{U,j}}m_{U,j}\|<1/j\). Direct the pairs by decreasing neighborhoods and increasing \(j\). This gives a net \(t_\alpha\to t_0\), \(\|m_\alpha\|=1\), \(T_{t_\alpha}m_\alpha\to0\). Uniform boundedness of \(S_t\) implies \(S_{t_\alpha}T_{t_\alpha}m_\alpha\to0\). Collective compactness of \(K_{X,t}\) gives a subnet on which \(K_{X,t_\alpha}m_\alpha\) converges. Identity (F17) then makes \(m_\alpha\) converge along that subnet to a unit vector \(m\in M\). Joint continuity gives \(T_{t_0}m=0\), contradicting \(M\cap\ker T_{t_0}=\{0\}\). This proves the estimate. The parameter net is necessary for this proof at the stated topological generality.

**Problem 5: a usable test for collective compactness.** Suppose \(t\mapsto K_t\in\mathcal L(X,Y)\) is operator norm continuous on compact \(I\), and each \(K_t\) is compact. Prove collective compactness. Explain why the tail-shift errors in (F21) fail the hypothesis.

**Solution.** Given \(\varepsilon>0\), cover \(I\) by finitely many sets on each of which \(\|K_t-K_{t_j}\|<\varepsilon/2\). For each center \(t_j\), compactness of \(K_{t_j}\) provides a finite \(\varepsilon/2\)-net for its image of the unit ball. The union of these finitely many nets is an \(\varepsilon\)-net for all \(K_t\)-images of that ball. Thus the union is totally bounded. Its closure is complete as a closed subset of Banach \(Y\), and complete total boundedness implies compactness: successively choose nested infinite subsequences lying in balls of radii tending to zero to obtain a Cauchy subsequence of every sequence, then use completeness and metric sequential compactness. The closure is totally bounded too, by first using nets of smaller radius for the original set. For (F21), the second error is \(-P_{n+1}\), whose norm is one for every \(n\), whereas its value at zero is the zero operator. It is strongly continuous but fails operator norm continuity there.

## 10. From operator defects to elliptic problems

For an elliptic realization between two Banach or Sobolev spaces, the immediate task is to construct a left and a right approximate inverse with compact remainders on the correct domain and target. Section 5 then supplies the Fredholm property and the relation of indices. The hypotheses do not identify which lower-order terms are compact; that is a separate analytic theorem. Changing the domain can change the operator and its index.

For a family of such realizations, operator norm continuity permits Section 3 directly. If only strong continuity is available, Section 7 asks for collective compactness of both error families. A uniform estimate landing in a fixed compactly embedded auxiliary space is one route to that condition. Pointwise smoothing without a uniform bound is not enough. A subsequent unit must check those embeddings, parameter bounds, and spaces rather than appeal only to the word “elliptic.”

## References

The proofs here use finite-dimensional enlargement, an exact sequence for composition, and a closed-projection argument for strong families.

For prerequisite reading, Paul Garrett's [*Banach Spaces*, 13 November 2017](https://www-users.cse.umn.edu/~garrett/m/fun/notes_2016-17/02_banach.pdf), §6, Theorem 6.1, supplies the arbitrary-family uniform boundedness contract; §7, Theorem 7.1 and Corollary 7.2, supplies bounded inverse. Its Baire dependency is [*Review of metric spaces*, 2 February 2014](https://www-users.cse.umn.edu/~garrett/m/fun/notes_2012-13/01_metric_spaces.pdf), Theorem 4.0.1. These specified readings are covered by the [author's CC BY 3.0 notice](https://www-users.cse.umn.edu/~garrett/m/fun/). In the open mapping proof retain the derived radius \(1+2\varepsilon\); its final change to \(1+\varepsilon\) is obtained by relabeling the arbitrary positive parameter and has no effect on the corollary.

For the complex Hahn–Banach theorem, the pinned mathlib declaration [exists_extension_norm_eq](https://github.com/leanprover-community/mathlib4/blob/71a80585ee495fc24472fd0eaffc89d94e4fd8d6/Mathlib/Analysis/Normed/Module/HahnBanach.lean#L38-L51), commit 71a80585ee495fc24472fd0eaffc89d94e4fd8d6, has the required stronger norm-preserving statement. Taking its scalar field to be \(\mathbb C\) gives complex Hahn–Banach extension; a functional on a finite-dimensional subspace is continuous by norm equivalence. The source is under [Apache 2.0](https://github.com/leanprover-community/mathlib4/blob/71a80585ee495fc24472fd0eaffc89d94e4fd8d6/LICENSE).

Two further comparisons help orient advanced reading. Jochen Glück's [*Functional Analysis 1*, version 23 August 2026](https://fan.uni-wuppertal.de/fileadmin/mathe/reine_mathematik/funktionalanalysis/glueck/Manuskripte/Lecture_Notes__Functional_Analysis_1.pdf), Lemmas 6.1.15–6.1.16, treats infinite-defect norm stability. The proofs above give complete arguments at the stated prerequisites.
