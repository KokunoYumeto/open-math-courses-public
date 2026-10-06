# Completing the elementary inputs actually used

Private prerequisite companion. The source is Jiří Lebl's freely accessible
*Basic Analysis*, version 6.3, [author edition](https://www.jirka.org/ra/).
This is an attributed adaptation and extension under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
It fills particular omitted proofs in §§1.2, 2.1–2.4, 7.2–7.6 and 8.2.
The complete human proofs already in the programme are retained through exact
bindings; they are not replaced by a fresh treatment of those chapters.
The one short reproduced route, the Archimedean argument, permits the needed
proof to be carried separately from unrelated material on its source page.

The underlying definitions are those of an ordered field of real numbers with
the least-upper-bound axiom, natural-number induction, finite sums, functions,
sets and sequences. These are the declared axioms and definitions of the
arguments, rather than additional theorems asserted without proof. No claim
about constructing or uniquely characterizing that field is used here.
For a nonempty set bounded below, its infimum exists by applying the supremum
axiom to its negative: if \(u=\sup(-A)\), then \(-u\) is a lower bound of
\(A\), and every lower bound \(b\) satisfies \(-b\geq u\), hence
\(b\leq-u\).

## P6. The short omissions in the compactness and contraction chain

### P6.0. The Archimedean argument used by these proofs

This is the argument of Lebl's Theorem 1.2.4(i), adapted with its hypothesis
explicit. The natural numbers are not bounded above in the ordered complete
field. Otherwise \(b=\sup\mathbb N\) would exist. Since \(b-1<b\),
\(b-1\) is not an upper bound, so some \(m\in\mathbb N\) satisfies
\(m>b-1\). Then \(m+1\in\mathbb N\) and \(m+1>b\), a contradiction.
Consequently, for \(x>0\) and any \(y\), some \(n\) satisfies
\(n>y/x\), or \(nx>y\). In particular \(1/n\to0\): given
\(\varepsilon>0\), choose \(N>1/\varepsilon\); every \(n\geq N\)
satisfies \(0<1/n<\varepsilon\). \(\square\)

### P6.1. Subsequence indices, metric limits and tails

If \(n_{k+1}>n_k\) are positive integers, then \(n_k\geq k\).
Indeed \(n_1\geq1\); if \(n_k\geq k\), the integer inequality gives
\(n_{k+1}\geq n_k+1\geq k+1\). Thus, if \(x_n\to p\) in a
metric space, every subsequence converges to \(p\): a bound
\(d(x_n,p)<\varepsilon\) for \(n\geq N\) also holds at \(n_k\)
for \(k\geq N\). If a tail converges, take the larger of its threshold
and its initial index to obtain the same bound for the original sequence.
These statements complete the metric version left as Proposition 7.3.6.

For Proposition 7.3.5, if \(d(x_n,p)\leq a_n\to0\), then, for
every \(\varepsilon>0\), eventually \(d(x_n,p)\leq a_n<\varepsilon\),
so \(x_n\to p\). Conversely take \(a_n=d(x_n,p)\); the definition
of convergence says exactly that this nonnegative real sequence tends to
zero. A convergent metric sequence is bounded (Proposition 7.3.4): eventually
its distance from \(p\) is less than 1, and the maximum of 1 and the
finitely many earlier distances bounds every term. \(\square\)

### P6.2. Decreasing limits and approximation to an extremum

For the decreasing half of Theorem 2.1.10, let \(x_n\) decrease and be
bounded below, and set \(l=\inf\{x_n:n\geq1\}\). Given
\(\varepsilon>0\), \(l+\varepsilon\) cannot be a lower bound,
so there is an \(N\) with \(x_N<l+\varepsilon\). Then
\(l\leq x_n\leq x_N<l+\varepsilon\) for every \(n\geq N\),
proving \(x_n\to l\). The increasing proof is already written in the
programme source.

If \(S\ne\varnothing\) is bounded above and \(s=\sup S\), for
every \(\varepsilon>0\) there is an \(a\in S\) with
\(s-\varepsilon<a\leq s\): otherwise \(s-\varepsilon\) would be
an upper bound smaller than the least one. This proves Proposition 1.2.8.
Choose \(a_n\in S\) with \(s-1/n<a_n\leq s\), and put
\(u_n=\max(a_1,\ldots,a_n)\). Each \(u_n\) is an element of
\(S\), the sequence is increasing, and \(0\leq s-u_n<1/n\).
P6.0 implies \(u_n\to s\). For an infimum \(t\), choose
\(b_n\in S\) with \(t\leq b_n<t+1/n\), using the same
greatest-lower-bound argument, and take the finite minima. This supplies
both monotone sequences in Proposition 2.1.13, used by the extreme-value
proof of Theorem 7.5.6. \(\square\)

### P6.3. The omitted lower-limit steps in the real Cauchy proof

For a bounded sequence, choose \(L\leq x_j\leq U\) for every
\(j\). Each tail is nonempty, so its infimum \(b_n\) and supremum
\(a_n\) satisfy
\(L\leq b_n\leq a_n\leq U\). Passing to a smaller tail cannot
decrease its infimum: any lower bound of the old tail is a lower bound
of the new one. Hence \(b_{n+1}\geq b_n\). These are the omitted
boundedness and monotonicity steps of Proposition 2.3.2.

The liminf half of Theorem 2.3.4 follows from its fully written limsup
half with all signs justified as follows. The number \(-b_n\) is
the supremum of \(\{-x_j:j\geq n\}\), by the definition of an
infimum. If \(v_n\to v\), then \(-v_n\to-v\) because
\(|(-v_n)-(-v)|=|v_n-v|\). Applying the proved limsup subsequence
theorem to \(-x_j\) therefore gives indices \(m_k\) such that
\(-x_{m_k}\to-\lim b_n\), hence
\(x_{m_k}\to\lim b_n=\liminf x_n\). This completes the input
used in the existing full proof of Theorem 2.4.5; that Cauchy proof is
retained, including its comparison of the two subsequential limits.

The subtraction case omitted in Proposition 2.2.5 uses
\[
 |(x_n-y_n)-(x-y)|\leq|x_n-x|+|y_n-y|.
\]
Choose both terms smaller than \(\varepsilon/2\). Its addition,
product and reciprocal proofs are already complete in the source.
\(\square\)

### P6.4. Closed balls and closed complete subspaces

To complete Proposition 7.2.9, if \(y\notin C(p,r)\), then
\(\delta=d(p,y)-r>0\). For \(d(y,z)<\delta\), the triangle
inequality implies
\(d(p,z)\geq d(p,y)-d(y,z)>r\). Thus a ball about every point
of the complement stays in the complement, proving that \(C(p,r)\)
is closed. The proof that open balls are open is already in §7.2.

To complete Proposition 7.4.6, let \(E\) be a closed subset of a
complete metric space \(X\). A Cauchy sequence in \(E\) is Cauchy
in \(X\), since its distances are unchanged. It has a limit \(p\)
in \(X\). The already proved Proposition 7.3.12 says \(p\in E\).
The same distance inequalities then prove convergence in \(E\).
In particular a closed Euclidean ball is complete, using the complete
coordinatewise proof for \(\mathbb R^n\) in Proposition 7.4.4.
\(\square\)

### P6.5. The geometric bound inside the contraction proof

In Theorem 7.6.2 the contraction constant can be taken with
\(0\leq k<1\): replacing any negative constant by zero only weakens
the distance bound. For \(0<k<1\) and a positive integer \(q\),
expanding and cancelling finite sums gives
\[
 (1-k)\sum_{j=0}^{q-1}k^j=1-k^q,
 \qquad
 0\leq\sum_{j=0}^{q-1}k^j\leq\frac1{1-k}.
\]
Consequently the existing iteration estimate can use a finite sum directly:
\[
 d(x_m,x_n)\leq\frac{k^n}{1-k}d(x_1,x_0),\qquad m>n.
\]
Proposition 2.2.11 has a complete proof that \(k^n\to0\), after
the decreasing-limit step is supplied by P6.2. Given \(\varepsilon>0\),
choose \(N\) so that the right side at \(n=N\) is smaller than
\(\varepsilon\). It then stays smaller for every \(n\geq N\),
independently of \(m>n\); interchanging the indices covers \(n>m\),
and equal indices have zero distance. This proves precisely the Cauchy
claim used in the source. If \(k=0\), the image of the map is a single
point, and the iteration is constant after its first step.

The limiting fixed-point step needs only the same Lipschitz estimate:
\[
 d(\varphi(x),x)\leq
 k\,d(x,x_n)+d(x_{n+1},x)\longrightarrow0.
\]
Thus it does not require a separate unproved continuity theorem. The
existence and uniqueness argument of the source remains unchanged.
\(\square\)

### P6.6. Closed-set operations used by the closure argument

Lebl's Proposition 7.2.8 leaves the closed-set version of the topology
rules as an exercise. It follows from the proved open-set rules of
Proposition 7.2.6 and the following identities, verified by membership:
\[
 X\setminus\bigcap_{\lambda}F_\lambda
    =\bigcup_{\lambda}(X\setminus F_\lambda),\qquad
 X\setminus\bigcup_{j=1}^m F_j
    =\bigcap_{j=1}^m(X\setminus F_j).
\]
If the \(F\)'s are closed, their complements are open by definition.
The first right side is open by the union rule, and the second by the
finite-intersection rule. Hence arbitrary intersections and finite unions
of closed sets are closed. The empty set and the whole space are closed
because their complements are open. These steps complete the input of the
existing proofs that a closure is closed and that every ball about a point
of the closure meets the set (Propositions 7.2.19 and 7.2.22).

The empty-set case in the compactness arguments is immediate from the
definition: an empty family of members of any cover already covers the
empty set. Proofs that begin by choosing a point apply to the nonempty
case. This convention also removes an implicit nonemptiness step in
Theorem 7.4.11.

That theorem also refers to Proposition 7.3.5. Here is the complete metric
majorant argument. A sequence \(x_n\) in a metric space converges to \(p\)
if and only if there are real numbers \(a_n\to0\) with
\(d(x_n,p)\leq a_n\) for every \(n\). For the forward implication take
\(a_n=d(x_n,p)\); the real limit assertion is exactly the metric
convergence definition. Conversely, given \(\varepsilon>0\), choose
\(N\) such that \(|a_n|<\varepsilon\) for \(n\geq N\). Then
\(0\leq d(x_n,p)\leq a_n\leq|a_n|<\varepsilon\), which is metric
convergence. In the compactness proof \(a_j=1/j\) tends to zero by
the Archimedean argument P6.0. Thus that source cross-reference uses
the full proof here, including both directions, rather than an
unproved external result. \(\square\)

## P7. Why permutation parity in the determinant is well defined

This completes the parity exercise preceding Lebl's determinant formula in
§8.2.3. For indeterminates \(t_1,\ldots,t_n\), put
\[
 V(t)=\prod_{i<j}(t_j-t_i).
\]
Interchanging two adjacent variables reverses their mutual factor and
permutes all the other factors in pairs, so it multiplies \(V\) by
\(-1\). Interchanging positions \(i<j\) can be performed by
moving position \(i\) to \(j\) in \(j-i\) adjacent steps and then
moving the old position \(j\) back to \(i\) in \(j-i-1\) steps.
It therefore also changes \(V\) by \(-1\).

Every permutation is a product of adjacent interchanges: move the entry
1 to the first position, then the entry 2 to the second without changing
the first, and continue. Each step moves a specified entry through only
finitely many positions; after \(n\) stages the order is the identity.
Thus a permutation \(\sigma\) transforms \(V(t)\) into
\(\epsilon_\sigma V(t)\), where \(\epsilon_\sigma\in\{1,-1\}\).
This sign is independent of the chosen decomposition, since evaluation at
\((t_1,\ldots,t_n)=(1,\ldots,n)\) gives the fixed nonzero quotient
\[
 \epsilon_\sigma=
 \frac{\prod_{i<j}(\sigma(j)-\sigma(i))}
      {\prod_{i<j}(j-i)}.
\]
Applying two permutations successively shows
\(\epsilon_{\sigma\tau}=\epsilon_\sigma\epsilon_\tau\): both
sides are the factor by which the same substitution changes \(V\).
Any decomposition into \(r\) arbitrary interchanges changes \(V\)
by \((-1)^r\), so \((-1)^r=\epsilon_\sigma\). Its parity is
therefore intrinsic. These facts supply exactly the signs used in the
programme determinant proofs and the cofactor calculation P2.
For \(n=1\), the empty product is 1 and the same conclusions hold.
\(\square\)

## P8. Positive square roots without a smooth-inverse circularity

The existence argument generalizes the actually read square-root example
in Lebl §1.2; the general root there is left as an exercise. Fix \(r>0\)
and let \(A=\{x\geq0:x^2\leq r\}\). This set is nonempty and
bounded above by \(r+1\). It contains a positive point, for example
\(\min(r,1)/2\). Therefore \(s=\sup A>0\) exists.

If \(s^2<r\), choose
\[
 0<h\leq\min\left(1,\frac{r-s^2}{2(2s+1)}\right).
\]
Then \((s+h)^2-s^2=h(2s+h)\leq(r-s^2)/2<r-s^2\),
so \(s+h\in A\), contradicting that \(s\) is an upper bound.
If \(s^2>r\), choose
\[
 0<h\leq\min\left(\frac s2,\frac{s^2-r}{4s}\right).
\]
Then \(s-h>0\), and
\((s-h)^2\geq s^2-2sh\geq(s^2+r)/2>r\).
Every nonnegative \(x\geq s-h\) has \(x^2>r\), so \(s-h\)
is an upper bound for \(A\), contradicting minimality of \(s\).
Hence \(s^2=r\). Positive squaring is strictly increasing, since
\(u^2-v^2=(u-v)(u+v)>0\) when \(u>v\geq0\); this also proves
uniqueness. Write this root as \(\sqrt r\), and set \(\sqrt0=0\).
The same comparison proves monotonicity of the square root.

For \(r>0\) and \(t\geq0\),
\[
 |\sqrt t-\sqrt r|=
 \frac{|t-r|}{\sqrt t+\sqrt r}\leq\frac{|t-r|}{\sqrt r}.
\]
This proves continuity at positive \(r\). At zero, \(0\leq t<\varepsilon^2\)
implies \(\sqrt t<\varepsilon\), proving one-sided continuity there.
For \(r+h>0\) and \(h\ne0\), rationalizing gives
\[
 \frac{\sqrt{r+h}-\sqrt r}{h}
   =\frac1{\sqrt{r+h}+\sqrt r}\longrightarrow\frac1{2\sqrt r}.
\]
So the positive square root is \(C^1\) on \((0,\infty)\). If it
is \(C^k\), the reciprocal calculation in P2 and the chain rule show
that its displayed derivative is \(C^k\); hence it is \(C^{k+1}\).
Induction proves smoothness without invoking the inverse function theorem
whose proof later uses these roots. The derivative step inherits the
declared elementary product and chain rules; it does not close all of F0-CALC.
\(\square\)

## Remaining proof review

The exact existing programme files, anchors and these local completions form one dependency chain. Their mathematical arguments must be distinguished from the eligibility of whole source pages or whole-book downloads. The selected dimension and differential-calculus inputs, including P8's smoothness, are now bound in `differential-proof-chain.json`. The compact integral, fundamental theorem and Taylor inputs are bound separately in `integration-proof-chain.json`. Global integration, exponentials, multidimensional change of variables and the final assembled lesson remain under review.
