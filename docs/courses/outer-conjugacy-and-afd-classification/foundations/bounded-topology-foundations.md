# Proof companion: bounded topology and faithful states

*Original programme proof excerpts from the OA-MOD course project, with their original CC0 attribution. Selection, integration and checking by GPT-6 Astra (OpenAI), Ultra, October 2026. Cited human texts retain their own rights.*

This companion supplies the complete earlier arguments used by [Bounded topology and tracial representations](../src/bounded-topology-and-tracial-representations.md) for its bounded representation and faithful-state results. It contains the Hilbert, norm-extension, compactness, bounded calculus, predual and density proofs used there, with arbitrary Hilbert dimensions and arbitrary directed nets. The entry assumptions are complete real and complex scalars, inner-product axioms, elementary algebra and topology, and the maximal principle of set theory.

These are copies of existing independently written programme proofs, not extracts from the cited human books or articles. Source locations are recorded in [the provenance manifest](bounded-topology-foundations.provenance.json). Mathematical statements and proofs are retained; local cross-references point within this companion. References in the copied context to later modular or general-weight results do not import those results here.

The source module for the finite-vector commutant argument credits Jacob Lurie's [Math 261y, Lecture 5, Theorem 4 and Proposition 5](https://people.math.harvard.edu/~lurie/261ynotes/lecture5.pdf). The norm-extension module credits Yury Kudryashov and Heather Macbeth's [mathlib Hahn–Banach formulations](https://github.com/leanprover-community/mathlib4/blob/71a80585ee495fc24472fd0eaffc89d94e4fd8d6/Mathlib/Analysis/Normed/Module/HahnBanach.lean#L44). The Kaplansky module compares Jesse Peterson's [Notes on von Neumann algebras, Theorem 2.6.4](https://math.vanderbilt.edu/peters10/teaching/spring2013/vonNeumannAlgebras.pdf). The exact arguments needed below are written in full.

- [Foundation A: Real Hilbert geometry](#foundation-a-real-hilbert-geometry)
- [Foundation B: Norm extension and convex separation](#foundation-b-norm-extension-and-convex-separation)
- [Foundation C: Compact products and dual balls](#foundation-c-compact-products-and-dual-balls)
- [Foundation D: Bernstein continuous calculus](#foundation-d-bernstein-continuous-calculus)
- [Foundation E: Bounded operators and topology](#foundation-e-bounded-operators-and-topology)
- [Foundation F: Concrete preduals](#foundation-f-concrete-preduals)
- [Foundation G: Nonunital bicommutant density](#foundation-g-nonunital-bicommutant-density)
- [Foundation H: Kaplansky density](#foundation-h-kaplansky-density)

## Foundation A: Real Hilbert geometry

A closed real subspace is complete for this real inner product. No complex-linearity, finite dimension, or countability assumption is imposed on it.

## The real Hilbert tools used below

**The inner-product inequalities.** Positivity and definiteness are inner-product axioms. If \(y\ne0\), expansion using the linear-first convention gives
\[
0\leq\left\|x-\frac{\langle x,y\rangle}{\|y\|^2}y\right\|^2
=\|x\|^2-\frac{|\langle x,y\rangle|^2}{\|y\|^2}.
\]
Hence \(|\langle x,y\rangle|\leq\|x\|\|y\|\); the case \(y=0\) is immediate. For a real inner product the same computation uses the real scalar \((x,y)_{\mathbb R}/\|y\|^2\). Expansion and this inequality give
\[
\begin{aligned}
\|x+y\|^2
&=\|x\|^2+2\operatorname{Re}\langle x,y\rangle+\|y\|^2\\
&\leq(\|x\|+\|y\|)^2,
\end{aligned}
\]
so the induced norm satisfies the triangle inequality. Expanding both squares and cancelling the mixed terms also gives the parallelogram identity
\[
\|x+y\|^2+\|x-y\|^2=2\|x\|^2+2\|y\|^2.
\]
These computations apply in arbitrary dimension and to the underlying real Hilbert space.

Let \(E\) be a closed real subspace of a Hilbert space regarded as real. Every \(x\) has a unique closest point \(P_E x\) in \(E\). Indeed, if \(d=\inf_{e\in E}\|x-e\|\) and \(e_n\) is a minimizing sequence, the parallelogram identity gives
\[
\begin{aligned}
&\|e_n-e_m\|^2\\
&\leq 2\|x-e_n\|^2+2\|x-e_m\|^2-4d^2\longrightarrow0.
\end{aligned}
\]
Completeness and closedness give a minimizing limit. Varying that limit by \(t e\), for real \(t\) and \(e\in E\), shows that the residual is real-orthogonal to \(E\). This orthogonality proves uniqueness, real-linearity of \(P_E\), and \(\|P_E x\|\leq\|x\|\).

Every bounded real-linear functional \(\ell\) on a real Hilbert space has a unique vector \(v\) such that \(\ell(z)=(v,z)_{\mathbb R}\), with \(\|v\|=\|\ell\|\). To see this without an additional representation theorem, suppose \(\ell\ne0\), put \(N=\ker\ell\), and choose \(x_0\notin N\). The preceding projection construction gives \(u=x_0-P_Nx_0\ne0\), with \(u\perp_{\mathbb R}N\) and \(\ell(u)=\ell(x_0)\ne0\). Since
\[
z-\frac{\ell(z)}{\ell(u)}u\in N,
\]
one may take \(v=\ell(u)u/\|u\|^2\). The case \(\ell=0\) uses \(v=0\). The norm equality follows from Cauchy–Schwarz and testing at \(v/\|v\|\) when \(v\ne0\). Uniqueness follows by testing the difference of two representing vectors against itself.

## Foundation B: Norm extension and convex separation

**Original mathematical exposition by GPT-6 Astra / Ultra. Self-checked by the writing AI.**

These proofs supply the elementary functional-analysis inputs used in the concrete predual construction. We assume the complete real and complex scalar fields, the inner-product axioms and the set-theoretic maximal principle. Hilbert spaces have arbitrary dimension. Locally convex spaces below need not be Hausdorff or complete, and operator limits may be arbitrary directed nets.

For the norm-extension formulation, the free human source is Yury Kudryashov and Heather Macbeth's [mathlib Hahn–Banach module, `exists_extension_norm_eq` and `exists_dual_vector`](https://github.com/leanprover-community/mathlib4/blob/71a80585ee495fc24472fd0eaffc89d94e4fd8d6/Mathlib/Analysis/Normed/Module/HahnBanach.lean#L44). NP1 writes the real extension argument and its complex conversion in full. No theorem is supplied by that citation in place of a proof. The bounded operator inputs are the written [BK01, BK03, BK04 and BK06](#foundation-e-bounded-operators-and-topology); their free-source reconstruction is separate from this note.

## NP1 — Norm-preserving extension and the norming identity

Let \(p\) be a finite sublinear function on a real vector space \(X\), and let \(f:D\to\mathbb R\) be linear on a subspace with \(f\le p\). For \(x\notin D\), a linear extension assigning value \(a\) to \(x\) is dominated by \(p\) exactly when
\[
\begin{aligned}
&\sup_{d\in D}\{f(d)-p(d-x)\}\le a\\
&\quad\le\inf_{e\in D}\{p(e+x)-f(e)\}.
\end{aligned}
\tag{NP.1}
\]
Each expression on the left is at most each expression on the right, because
\(f(d+e)\le p(d+e)\le p(d-x)+p(e+x)\).
Taking \(d=0\) and \(e=0\) shows that both endpoints of this interval are finite. Real completeness supplies a choice of \(a\). The positive and negative coefficients of \(x\), divided by their absolute values, give precisely the two inequalities in (NP.1); hence the extension is dominated on all of \(D+\mathbb Rx\). The union of a chain of dominated extensions is a dominated extension. The maximal principle and the one-dimensional step therefore give an extension to \(X\).

For a bounded real functional on a subspace of a normed space, apply this with \(p(x)=C\|x\|\), where \(C\) is its norm. Domination at \(x\) and \(-x\) gives an extension bounded by \(C\), and restriction gives the reverse norm inequality.

For a complex-linear functional \(h\) on a complex subspace, extend \(\operatorname{Re}h\) as a real functional \(f\), dominated by \(\|h\|\|x\|\), and set
\[
L(x)=f(x)-if(ix).
\tag{NP.2}
\]
Real linearity and \(L(ix)=iL(x)\) prove complex linearity. On the original subspace, \(f(ix)=\operatorname{Re}(ih(x))=-\operatorname{Im}h(x)\), so \(L=h\). For each \(x\), rotate by a scalar \(\lambda\) of modulus one making \(\lambda L(x)\) nonnegative real. Then
\(|L(x)|=f(\lambda x)\le\|h\|\|x\|\).
Restriction again gives equality of norms. This includes the zero functional and does not require the subspace to be closed.

If \(z\ne0\), the functional \(\lambda z\mapsto\lambda\|z\|\) on its real or complex span has norm one. Extend it by the corresponding result. Testing \(z\), together with the defining bound for a functional, proves
\[
\|z\|=\sup\{|L(z)|:L\in X^*,\ \|L\|\le1\}.
\tag{NP.3}
\]
For \(z=0\) both sides vanish. This is the exact norming identity needed for the quotient predual norm.

Two elementary finite-dimensional steps in that construction can also be made explicit. Given a finite spanning list of Hilbert vectors, successively subtract its projections on the orthonormal vectors already chosen. Skip a zero remainder and normalize a nonzero remainder. Inner-product expansion proves orthogonality at each step, and each discarded or normalized vector remains in the span accumulated so far. After finitely many steps this gives an orthonormal basis of the original span. For a subspace \(W\subset\mathbb C^n\) and \(v\notin W\), successively adding vectors outside the current span constructs a basis of \(W\), then a basis of \(\mathbb C^n\) starting with that basis and \(v\). Assigning values zero on the former basis, one on \(v\), and zero on the remaining basis vectors gives a linear functional annihilating \(W\) but not \(v\). These are the finite coefficient and annihilator tests in CP02 and CP05.

## NP2 — Point separation and equality of convex closures

Let \(X\) be a real locally convex topological vector space, \(C\subset X\) a nonempty closed convex set, and \(x_0\notin C\). The definition of a locally convex topology gives a symmetric open convex neighborhood \(V\) of zero such that \((x_0+V)\cap C=\varnothing\). Symmetry implies \(x_0\notin C+V\). Choose \(c_0\in C\) and put
\[
A=C+V-c_0,\qquad y=x_0-c_0.
\]
The set \(A\) is open and convex, contains zero, and does not contain \(y\). It is absorbing: continuity of \(t\mapsto tx\) at zero places a sufficiently small positive multiple of every \(x\) in \(A\). Its gauge is consequently finite:
\[
p_A(x)=\inf\{t>0:x\in tA\}.
\tag{NP.4}
\]
It is nonnegative and positively homogeneous. If \(s>p_A(x)\) and \(t>p_A(z)\), then \(x\in sA\) and \(z\in tA\). To see the first assertion, choose a smaller admissible dilation and use convexity with zero to enlarge it to \(sA\); the second is identical. Convexity now gives \(x+z\in(s+t)A\). Letting \(s,t\) decrease to their infima proves subadditivity.

Moreover \(A=\{x:p_A(x)<1\}\). An admissible dilation smaller than one lies in \(A\) by convexity. Conversely, if \(x\in A\), openness and continuity of \(t\mapsto tx\) allow a scalar \(t>1\) with \(tx\in A\); then \(p_A(x)\le1/t<1\). Thus \(p_A(y)\ge1\).

On \(\mathbb Ry\), define \(f(ty)=t p_A(y)\). For positive \(t\) this is \(p_A(ty)\); for negative \(t\), domination follows from \(-p_A(y)\le p_A(-y)\), a consequence of subadditivity at zero. NP1 extends \(f\) to a real linear \(\ell\le p_A\). On the open neighborhood \(A\cap(-A)\) we have \(|\ell|<1\), so \(\ell\) is continuous: scaling this neighborhood by any positive \(\varepsilon\) makes \(|\ell|<\varepsilon\).

We have \(\ell(y)=p_A(y)\ge1\). A sufficiently small positive multiple \(v_0\) of \(y\) belongs to \(V\); set \(\delta=\ell(v_0)>0\). For every \(c\in C\), the vector \(c+v_0-c_0\) belongs to \(A\). Therefore
\[
\ell(c)<\ell(c_0)+1-\delta
\le\ell(x_0)-\delta.
\tag{NP.5}
\]
This proves strict point separation with a common positive margin. No Hausdorff assumption entered the proof.

For completeness, the closure of a convex set is convex. If \(a,b\) lie in that closure and \(0\le t\le1\), continuity of \((u,v)\mapsto tu+(1-t)v\) lets points of the original set approximate \(ta+(1-t)b\) in every neighborhood; each approximating convex combination belongs to the set. Applying (NP.5) to its closure shows that the closure of a nonempty convex set is the intersection of all closed half-spaces, defined by continuous real linear functionals, that contain it. The empty set is closed separately. Thus two locally convex topologies with the same continuous real dual have exactly the same closures of convex sets. There is no boundedness, completeness or sequential-closure restriction. CP09–CP10 establish the requisite dual equality for the operator topologies before using this conclusion.

## Foundation C: Compact products and dual balls

*Programme source: OA-MOD, `public/src/banach-second-adjoint.md`, lines 62–98; 128–145.*

## OA-MOD-AB-04 — Filters and compact products

A **proper filter** \(\mathcal F\) on a nonempty set \(S\) is a family of subsets containing \(S\), excluding the empty set, closed under finite intersections and under passage to supersets. An **ultrafilter** is a proper filter maximal for inclusion.

**Extension lemma.** Every proper filter lies in an ultrafilter. An ultrafilter \(\mathcal U\) contains exactly one of \(A,S\setminus A\) for each \(A\subset S\).

**Proof.** Order the proper filters containing \(\mathcal F\) by inclusion. The union of a chain is a proper filter: finitely many chosen members lie in one filter of the chain. Zorn gives a maximal element. If \(A\notin\mathcal U\) and every \(U\in\mathcal U\) met \(A\), the supersets of the sets \(U\cap A\) would generate a larger proper filter. Hence some \(U\) misses \(A\), and \(S\setminus A\in\mathcal U\). Both complementary sets cannot belong to a proper filter. \(\square\)

A filter on a topological space **converges to \(s\)** if it contains every neighborhood of \(s\).

**Compactness criterion.** A space \(S\) is compact if and only if every ultrafilter on \(S\) converges to at least one point. In a Hausdorff space its limit is unique.

**Proof.** The empty space satisfies both assertions. On a nonempty compact space, the closed sets \(\overline U\), \(U\in\mathcal U\), have the finite-intersection property, since their finite intersections contain the corresponding nonempty filter intersections. They therefore have a common point \(s\): otherwise their open complements would cover \(S\) and have a finite subcover. If an open neighborhood \(V\) of \(s\) were absent from \(\mathcal U\), then \(S\setminus V\in\mathcal U\). This closed set would contain \(s\), a contradiction. Thus the filter converges.

Conversely, if an open cover has no finite subcover, its closed complements have the finite-intersection property and generate a proper filter. Extend it to \(\mathcal U\), and suppose \(\mathcal U\to s\). One member \(V\) of the cover contains \(s\), so both \(V\) and its complement belong to \(\mathcal U\), a contradiction. Finally, disjoint neighborhoods of two distinct Hausdorff points cannot both lie in a proper filter. \(\square\)

**Compact product theorem.** An arbitrary product of compact spaces is compact in its product topology.

**Proof.** A product with an empty factor is empty and compact; an empty product is a singleton. Otherwise let \(P=\prod_{i\in I}S_i\), and let \(\mathcal U\) be an ultrafilter on \(P\). For each coordinate projection \(\pi_i\), the family
\[
 \mathcal U_i=\{A\subset S_i:\pi_i^{-1}(A)\in\mathcal U\}
 \tag{AB.6}
\]
is an ultrafilter, as follows directly from inverse images, finite intersections and the complement criterion. Compactness supplies a limit \(s_i\in S_i\). Choose these limits; the same choice principle underlying Zorn is in force. Every basic neighborhood of \(s=(s_i)_{i\in I}\) is a finite intersection of inverse images of coordinate neighborhoods, hence belongs to \(\mathcal U\). Thus \(\mathcal U\to s\), and the criterion proves compactness. No countability of \(I\) has been introduced. \(\square\)

Two elementary consequences will be used below. A closed subset of a compact space is compact: add its open complement to any cover and use a finite subcover. A compact subset of a Hausdorff space is closed: for an outside point, disjoint neighborhoods separating it from each compact-set point have a finite subfamily on the compact side; the intersection of the corresponding outside neighborhoods misses the set. A continuous image of a compact space is compact, by pulling back open covers.

**Scalar and finite-dimensional compactness.** A closed interval \([a,b]\) is compact. For a proof, let \(\mathcal U\) be an ultrafilter on it. Bisect the interval; at least one closed half belongs to \(\mathcal U\), since a finite union in an ultrafilter has a member in the ultrafilter. Repeat within the chosen half. This gives nested intervals \([a_n,b_n]\in\mathcal U\) of lengths at most \(2^{-n}(b-a)\). The supremum \(s=\sup_n a_n\) satisfies \(a_n\le s\le b_n\) for every \(n\). Each neighborhood of \(s\) contains a sufficiently short interval \([a_n,b_n]\), so belongs to \(\mathcal U\). The ultrafilter criterion proves compactness. The degenerate interval is a singleton. The lengths tend to zero because the complete ordered real field is Archimedean: if the integers had a finite supremum \(M\), an integer exceeding \(M-1\) would have its successor exceeding \(M\); and \(2^n\ge n+1\).

Finite real coordinate boxes are compact by the product theorem. The ordinary topology of \(\mathbb C^d\) is the real coordinate topology on \(\mathbb R^{2d}\); the inequalities

\[
\begin{aligned}
\max(|\operatorname{Re}z|,|\operatorname{Im}z|)&\le |z|\\
 &\le |\operatorname{Re}z|+|\operatorname{Im}z|
\end{aligned}
\]

give both neighborhood comparisons. A closed scalar disk is a closed subset of a sufficiently large real box, so is compact. More generally, every closed bounded subset of \(\mathbb F^d\), in the maximum-coordinate norm \(|\alpha|_\infty=\max_j|\alpha_j|\), is compact: it is closed inside such a box.

## OA-MOD-AB-05 — Dual-ball compactness and the bidual criterion

**Banach–Alaoglu theorem.** For any real or complex normed space \(X\) and any \(R\geq0\), the closed ball \(RB_{X^*}\) is compact in \(\sigma(X^*,X)\).

**Proof.** For \(R>0\), consider the product of closed scalar disks
\[
 P_R=\prod_{x\in X}\{z\in\mathbb F:|z|\leq R\|x\|\}.
 \tag{AB.7}
\]
Each disk is compact by the scalar-disk proof in AB-04, and the preceding product theorem makes \(P_R\) compact for arbitrary \(X\). Within this product impose the equations
\[
\begin{gathered}
z_{ax+by}=az_x+bz_y\\
(x,y\in X,\ a,b\in\mathbb F).
\end{gathered}
\tag{AB.8}
\]
Each equation is closed because it involves only three continuous coordinate evaluations and scalar operations. Their simultaneous solution set is closed and compact. A solution defines a linear functional \(f(x)=z_x\) with \(|f(x)|\leq R\|x\|\), hence \(\|f\|\leq R\). Conversely every functional in the ball gives a solution. This identification is a homeomorphism, since both topologies are pointwise convergence on \(X\). If \(R=0\), the ball is the compact singleton \(\{0\}\). \(\square\)

The weak-star topology is Hausdorff, since distinct functionals differ on some vector. Dual balls are also weak-star closed, being the intersections of \(\{|f(x)|\leq R\|x\|\}\).

## Foundation D: Bernstein continuous calculus

## GP0. The bounded calculus used in the proof

Norm limits of bounded operators exist whenever the operator sequence is Cauchy: for each vector \(x\), completeness of \(H\) gives \(Tx=\lim_n T_nx\). Passing to the limit proves linearity and boundedness; a uniform Cauchy estimate \(\|(T_n-T_m)x\|\leq\varepsilon\|x\|\) then proves operator-norm convergence as \(m\to\infty\). In particular an operator series whose norms have finite sum converges in operator norm. This justifies the calculus limits and the geometric inverse below.

We record the tools so that the later cutoff is an actual proof step. Cauchy–Schwarz follows by applying positivity to \(x-ty\) and minimizing over the complex scalar \(t\); the same argument applies to any positive semidefinite sesquilinear form. For a bounded positive operator \(A\), put
\[
m=\sup_{\|x\|=1}\langle Ax,x\rangle.
\]
Form Cauchy–Schwarz and the identity \(\|v\|=\sup_{\|y\|=1}|\langle v,y\rangle|\) give
\[
\|Ax\|^2\leq m\langle Ax,x\rangle\leq m^2\|x\|^2.
\tag{GP0.1}
\]
Thus \(\|A\|=m\). In particular, if \(0\leq A\leq I\), then \(A-A^2\geq0\).

Bounded adjoints require no extra representation theorem here. The real Riesz proof gives a vector representing the real part of a bounded complex-linear functional. Testing also at \(ix\) recovers its imaginary part, and hence its representation as \(x\mapsto\langle x,v\rangle\). Applying this to \(x\mapsto\langle Tx,y\rangle\) defines \(T^*y\); the defining equality proves linearity, the product rule, and \(\|T^*\|=\|T\|\). It also gives \(\|T^*T\|=\|T\|^2\): one inequality is the operator norm bound, and the other follows from \(\|Tx\|^2=\langle T^*Tx,x\rangle\).

Here is continuous calculus for a positive contraction \(A\), in precisely the form we need. For a continuous real function \(f\) on \([0,1]\), its Bernstein polynomial is
\[
B_n f(t)=\sum_{k=0}^n f(k/n){n\choose k}t^k(1-t)^{n-k}.
\tag{GP0.2}
\]
These polynomials converge uniformly to \(f\). Indeed the nonnegative binomial weights sum to one, have mean \(t\), and have variance \(t(1-t)/n\leq1/(4n)\); the mean and variance follow by differentiating \((s+t)^n\) once and twice and then setting \(s=1-t\). Uniform continuity gives, for every \(\varepsilon>0\), a \(\delta>0\) on which the oscillation of \(f\) is at most \(\varepsilon\). The sum of the weights with \(|k/n-t|\geq\delta\) is at most \(1/(4n\delta^2)\), by multiplying each of those weights by the lower bound for its squared deviation. Consequently
\[
|B_nf(t)-f(t)|\leq\varepsilon+\frac{2\|f\|_\infty}{4n\delta^2}.
\tag{GP0.3}
\]
The uniform continuity used here follows from interval compactness: otherwise pairs at distance tending to zero with a fixed positive oscillation have a common convergent subsequence, contradicting continuity. Interval compactness follows by nested bisection and completeness of the real numbers.

Each operator \(A^k(I-A)^{n-k}\) is positive. Remove the even powers as the same polynomial factor on both sides of a quadratic form; the remaining factor is one of \(I,A,I-A,A(I-A)\), all positive by (GP0.1). The operator binomial weights therefore are positive and sum to \(I\). It follows that
\[
\begin{gathered}
-\|f\|_\infty I\leq B_nf(A)\leq\|f\|_\infty I,\\
\|B_nf(A)\|\leq\|f\|_\infty.
\end{gathered}
\tag{GP0.4}
\]
For the last norm estimate, a self-adjoint \(T\) with \(-cI\leq T\leq cI\) has norm at most \(c\): for \(c>0\), apply (GP0.1) to \((T+cI)/(2c)\) to obtain \(T^2\leq c^2I\); the case \(c=0\) follows by polarization.

For a fixed polynomial \(p\), the coefficients of \(B_np\) converge to those of \(p\). One elementary verification for the monomial \(t^j\) is to express \(k^j\) as a linear combination of the falling products \(k(k-1)\cdots(k-r+1)\), \(0\leq r\leq j\), whose highest coefficient is one. Binomial differentiation gives the expectation of that product as \(n(n-1)\cdots(n-r+1)t^r\). After division by \(n^j\), only \(r=j\) survives in the limit. Linearity proves the assertion. Thus (GP0.4) implies \(\|p(A)\|\leq\|p\|_\infty\) for real polynomials. For a complex polynomial use \(p(A)^*p(A)=(\overline p p)(A)\) and the adjoint norm identity.

Uniform polynomial approximation now defines \(f(A)\) for every continuous complex \(f\). The limit is independent of the approximating sequence, preserves sums, products and conjugation, and has norm at most \(\|f\|_\infty\). Positivity follows by using the nonnegative Bernstein weights when \(f\geq0\); hence scalar inequalities are preserved. An operator commuting with \(A\) commutes with every \(f(A)\), by polynomial approximation. In particular square roots of positive contractions are available, and
\[
\langle Ax,x\rangle=\|A^{1/2}x\|^2.
\tag{GP0.5}
\]
Positive operators of arbitrary finite norm are reduced to contractions by scaling. This proves all the continuous calculus needed below. It makes no Borel or unbounded calculus assertion.

## Foundation E: Bounded operators and topology

*Programme source: OA-MOD, `public/src/bounded-operator-kernel.md`, lines 9–81; 87–136; 137–160.*

## OA-MOD-BK-01 — The bounded prerequisite boundary

Inner products are linear in the first variable. A Hilbert space is a complete complex inner-product space; scalar completeness and the inner-product axioms are entry assumptions. For a bounded self-adjoint operator \(a\), write \(a\geq0\) when \(\langle a\xi,\xi\rangle\geq0\) for all \(\xi\). All operators in this lesson have full Hilbert-space domains.

We first discharge the two bounded contracts used in later sections: Hilbert projection, representation and adjoints; and the full continuous calculus for a bounded self-adjoint element in a unital norm-closed *-algebra. The zero Hilbert space satisfies all ensuing operator statements trivially; statements about nonempty spectra below concern nonzero spaces.

**Hilbert representation and bounded operators.** The preceding real Hilbert proof constructs orthogonal projections by a minimizing sequence and the parallelogram identity, and proves the real Riesz representation theorem. Apply it to the real Hilbert space with inner product \(\operatorname{Re}\langle\cdot,\cdot\rangle\). For a complex closed subspace, testing orthogonality against \(\eta\) and \(i\eta\) makes its real projection the complex orthogonal projection. For a bounded complex-linear functional \(L\), represent \(\operatorname{Re}L(\xi)\) as \(\operatorname{Re}\langle\xi,v\rangle\). Evaluation at \(i\xi\) identifies the imaginary parts as well, so \(L(\xi)=\langle\xi,v\rangle\), with the same norm.

If a bounded form \(b(\xi,\eta)\) is linear in \(\xi\) and conjugate-linear in \(\eta\), apply this result to \(\eta\mapsto\overline{b(\xi,\eta)}\), at each fixed \(\xi\). Its representing vector \(T\xi\) satisfies
\(b(\xi,\eta)=\langle T\xi,\eta\rangle\) and \(\|T\xi\|\leq C\|\xi\|\). Uniqueness proves linearity and uniqueness of \(T\). The same argument applied to \(\langle T\xi,\eta\rangle\), for \(T:H\to K\), constructs \(T^*:K\to H\). Testing pairings proves the adjoint sum and product rules and \(\|T^*\|=\|T\|\). Also
\(\|T^*T\|=\|T\|^2\), by \(\|T\xi\|^2=\langle T^*T\xi,\xi\rangle\) and the reverse operator-norm inequality.

Bounded maps on a dense subspace extend uniquely by norm limits: the bound makes images of a Cauchy sequence Cauchy and makes the limit independent of the approximating sequence. If a pre-Hilbert space is initially given, its completion is constructed from Cauchy sequences modulo sequences tending to zero. Termwise addition and scalar multiplication descend; the inner product is the limit of the original pairings, which exists and is representative-independent by Cauchy–Schwarz. Constant sequences embed isometrically and densely. For a Cauchy sequence of classes, choose representatives within \(2^{-n}\) at the \(n\)-th step after taking a subsequence with successive class errors at most \(2^{-n}\); the chosen representative points are Cauchy and give its limit. The original Cauchy sequence converges to that limit as well. This proves completeness.

For later nets, sequential completeness also gives a limit for every Cauchy net: choose increasing indices whose subsequent pairwise errors are at most \(2^{-n}\). Their values form a Cauchy sequence with a limit, and the same tail estimates prove convergence of the original net to that limit. GP0 also proves completeness of \(B(H)\) in operator norm, by taking limits on each vector, and proves Cauchy–Schwarz for positive semidefinite forms. In particular, for bounded positive \(a\),
\(\|a\|=\sup_{\|\xi\|=1}\langle a\xi,\xi\rangle\), and
\[
\|d\xi\|^2\leq C\langle d\xi,\xi\rangle
\quad\hbox{if }0\leq d\leq CI.
\tag{BK.1}
\]
For \(C>0\), this follows from GP0 applied to \(d/C\); for \(C=0\), polarization gives \(d=0\).

**The interval calculus.** GP0 constructs the calculus for a positive contraction from Bernstein polynomials. Its polynomial norm bound, uniform approximation, positivity and commutation proofs are all given there. For self-adjoint \(T\), take \(C=\|T\|>0\) and apply that construction to \((T+CI)/(2C)\). We obtain a unital *-homomorphism
\(f\mapsto f(T)\) from \(C([-C,C])\), with
\(\|f(T)\|\leq\|f\|_\infty\), preservation of order, and polynomial approximation in operator norm. If \(C=0\), use \(f(T)=f(0)I\). Thus every resulting operator belongs to any unital norm-closed *-algebra containing \(T\), and commutes with every operator commuting with \(T\).

For completeness, we now pass from the containing interval to the actual spectrum, rather than assume its norm and inverse properties. Define \(\sigma(T)\) as the complex numbers \(\lambda\) for which \(T-\lambda I\) has no bounded two-sided inverse on \(H\). Norm completeness and the geometric series prove that the resolvent set is open: perturb an invertible operator by an error smaller than the reciprocal inverse norm. The same series excludes \(|\lambda|>C\). For \(\operatorname{Im}\lambda\ne0\), the imaginary part of the quadratic pairing gives
\(\|(T-\lambda)\xi\|\geq|\operatorname{Im}\lambda|\|\xi\|\).
Its range is closed, and its orthogonal complement is
\(\ker(T-\overline\lambda)=0\); hence it is onto and has bounded inverse. Consequently \(\sigma(T)\) is a compact subset of \([-C,C]\).

It is nonempty. Set \(B=T+CI\geq0\) and \(m=\|B\|\). If \(m=0\), \(T=-CI\), whose spectrum is \(\{-C\}\). Otherwise take unit \(\xi_n\) with \(\langle B\xi_n,\xi_n\rangle\to m\). The inequality \(B^2\leq mB\), proved in GP0, gives
\(\|(B-mI)\xi_n\|^2\leq m(m-\langle B\xi_n,\xi_n\rangle)\to0\).
A bounded inverse is therefore impossible, so \(m-C\in\sigma(T)\).
More generally, each real \(\lambda\in\sigma(T)\) has unit approximate eigenvectors. Otherwise \(T-\lambda\) is bounded below, hence injective with closed range; the range-kernel identity for its self-adjoint adjoint makes that range dense, so it would have a bounded inverse.

**Restriction to the spectrum.** If \(h\in C([-C,C])\) vanishes on \(\sigma(T)\), then \(h(T)=0\). First suppose its support is a compact subset of the complement of the spectrum. Around each point \(\lambda\) of that support choose an interval of radius \(\delta\) with
\(\delta\|(T-\lambda)^{-1}\|<1\).
A finite such cover splits \(h\) into finitely many continuous functions \(h_j\) supported in those intervals. Explicitly, choose slightly smaller intervals still covering the support, use their distance-to-complement functions, divide by their positive sum on the support, and multiply by \(h\), extending by zero elsewhere. The extension is continuous because the compact support lies inside the set where the denominator is positive.

For the center \(\lambda_j\) and radius \(\delta_j\), multiplicativity and the interval norm bound give
\
\begin{aligned}
\|h_j(T)\|
&\leq\|(T-\lambda_j)^{-1}\|^n
       \|[(t-\lambda_j)^nh_j(t) (outside these selected proof passages)\|\\
&\leq\bigl(\delta_j\|(T-\lambda_j)^{-1}\|\bigr)^n
       \|h_j\|_\infty .
\end{aligned}
\]
Let \(n\to\infty\); each \(h_j(T)\) is zero. For a general \(h\) vanishing on the spectrum, multiply it by continuous distance cutoffs which vanish within distance \(1/n\) of the spectrum and equal one beyond distance \(2/n\). The products converge uniformly to \(h\), since \(h\) vanishes on that compact set. The preceding case and the norm bound prove \(h(T)=0\).

Every continuous complex \(f\) on \(\sigma(T)\) extends continuously to \([-C,C]\), with the same supremum norm: interpolate linearly across each complementary interval and keep the value constant beyond the extreme spectral points. To check continuity at the spectral set, small complementary intervals have both endpoints close, so uniform continuity of \(f\) controls their interpolates. For intervals longer than a fixed positive length there are only finitely many, and the interpolation is continuous at each endpoint. These two observations give continuity everywhere. Convexity of a closed complex disc gives the norm bound, and a real nonnegative \(f\) has a real nonnegative extension.

The vanishing result makes the value of \(f(T)\) independent of that extension. It yields a unital *-homomorphism on \(C(\sigma(T))\), positive and contractive. For \(\lambda\in\sigma(T)\), let \(\xi_n\) be its unit approximate eigenvectors. Factoring \(p(t)-p(\lambda)\) proves
\(\|(p(T)-p(\lambda))\xi_n\|\to0\) for polynomials. Uniform approximation on the containing interval proves the same assertion for continuous \(f\). Hence
\(\|f(T)\|\geq|f(\lambda)|\), and therefore
\[
\|f(T)\|=\max_{\lambda\in\sigma(T)}|f(\lambda)|.
\]
If \(\mu\notin f(\sigma(T))\), applying the calculus to \(1/(f-\mu)\) gives an inverse for \(f(T)-\mu I\). If \(\mu=f(\lambda)\), the approximate eigenvectors rule out such an inverse. Thus spectral mapping, including complex-valued \(f\), is proved. Inverses produced by the calculus belong to every unital norm-closed *-algebra containing \(T\).

**Positivity, square roots and lower bounds.** A bounded positive \(a\) has no negative spectral value: for \(\lambda<0\),
\(\|(a-\lambda)\xi\|\geq-\lambda\|\xi\|\), and the same closed-range and adjoint argument proves invertibility. Hence \(\sigma(a)\subset[0,\|a\|]\), and the calculus gives \(c=\sqrt a\geq0\), \(c^2=a\).
If another positive \(b\) satisfies \(b^2=a\), it commutes with \(a\), hence with \(c\) by polynomial approximation. Then \((b-c)(b+c)=0\). Positivity and (BK.1) show
\(\ker(b+c)=\ker b\cap\ker c=\ker a\).
The range of the self-adjoint \(b+c\) is dense in \((\ker a)^\perp\), so \(b-c\) vanishes there and also on \(\ker a\). Thus \(b=c\). This proves uniqueness without an unbounded spectral or polar theorem.

The identity \(\langle a\xi,\xi\rangle=\|a^{1/2}\xi\|^2\) gives
\(\ker a=\ker a^{1/2}\). If \(a\geq mI\), \(m>0\), applying the negative-value argument to \(a-mI\) gives \(\sigma(a)\subset[m,\|a\|]\); its continuous inverse and inverse square root are consequently available in the algebra. Finally, for any bounded map \(T:H\to K\),
\(\overline{\operatorname{ran}T}=(\ker T^*)^\perp\):
orthogonality to every \(T\xi\) is equivalent to \(T^*\eta=0\). This is the range-kernel identity used above and below.

## OA-MOD-BK-02 — Finite-vector approximation and the bicommutant

For \(S\subset B(H)\), let \(S'=\{r:rs=sr\ \text{for all }s\in S\}\).
Strong convergence means norm convergence on each fixed Hilbert vector; weak operator convergence means convergence of every matrix coefficient. Cauchy–Schwarz gives strong implies weak. Fixed left and right multiplication are continuous for both topologies: for strong convergence test
\(r(x_i-x)\xi\) and \((x_i-x)r\xi\); for weak convergence move \(r\) to \(r^*\eta\) in the first coefficient and to \(r\xi\) in the second. Thus a commutant is weakly closed. If \(S\) is *-closed, taking adjoints of its commutation equations also makes \(S'\) a unital *-algebra.

**Theorem.** Every unital *-subalgebra \(\mathcal B\subset B(H)\), whether or not norm closed, satisfies
\[
\overline{\mathcal B}^{\mathrm{SOT}}
=\overline{\mathcal B}^{\mathrm{WOT}}=\mathcal B''.
\tag{BK.2}
\]
Only the inclusion from right to left needs proof. Fix \(T\in\mathcal B''\), a finite list \(\xi_1,\ldots,\xi_n\), and an error \(\varepsilon>0\). On \(H^n\), let \(D(b)\) act diagonally and put
\[
\begin{gathered}
\Xi=(\xi_1,\ldots,\xi_n),\\
L=\overline{\{D(b)\Xi:b\in\mathcal B\}}.
\end{gathered}
\]
This is a closed linear subspace invariant under \(D(\mathcal B)\) and their adjoints. Its orthogonal complement is also invariant, by the adjoint pairing; hence its orthogonal projection \(P\) commutes with every \(D(b)\). In block matrix entries this says \(P_{jk}\in\mathcal B'\).
Consequently \(D(T)P=PD(T)\). Unitality puts \(\Xi\) in \(L\), so
\(PD(T)\Xi=D(T)\Xi\). Membership of \(D(T)\Xi\) in \(L\) supplies one \(b\in\mathcal B\) with
\(\sum_j\|(b-T)\xi_j\|^2<\varepsilon^2\).
These simultaneous finite-vector conditions are exactly a neighborhood basis for the strong topology, proving \(T\) belongs to the strong closure. The other inclusions follow from weak closedness of \(\mathcal B''\).

Selecting approximants with finite sets increasing and error decreasing gives a directed net; this argument supplies no uniform norm bound and requires no countable cofinal set. We have explicitly used \(I\in\mathcal B\). Without it, the zero algebra on a nonzero space is already a counterexample to (BK.2).

A concrete von Neumann algebra is therefore equivalently a unital *-algebra \(M=M''\), a strongly closed unital *-algebra, or a weakly closed one. It is norm closed, and the calculus constructed in BK-01 stays inside it.

## OA-MOD-BK-03 — The ultraweak convergence needed by finite cutoffs

The ultraweak topology is defined by the coefficient sums
\[
\begin{gathered}
\omega_{\xi,\eta}(x)=\sum_{n=1}^{\infty}\langle x\xi_n,\eta_n\rangle,\\
\sum_n\|\xi_n\|^2<\infty,\quad
\sum_n\|\eta_n\|^2<\infty .
\end{gathered}
\tag{BK.3}
\]
They converge absolutely by Cauchy–Schwarz, with norm bound
\(\|x\|(\sum\|\xi_n\|^2)^{1/2}(\sum\|\eta_n\|^2)^{1/2}\).
This definition permits nonseparable \(H\); the sequences belong to each individual test, not to a chosen basis.

If \(x_i\to x\) weakly and \(\sup_i\|x_i\|<\infty\), then \(x_i\to x\) ultraweakly. Indeed set \(D=\sup_i\|x_i\|+\|x\|\). The coefficient tail after \(N\), evaluated at \(x_i-x\), is bounded uniformly by
\[
D\left(\sum_{n>N}\|\xi_n\|^2\right)^{1/2}
 \left(\sum_{n>N}\|\eta_n\|^2\right)^{1/2}.
\]
Choose \(N\) for the tail, then a common directed tail for the finitely many leading coefficients. This proves convergence of the whole sum. Bounded strong convergence is a special case.

Fixed multiplication is ultraweakly continuous without a bound on the varying net: testing \(rx\) replaces \(\eta_n\) by \(r^*\eta_n\), while testing \(xr\) replaces \(\xi_n\) by \(r\xi_n\); both replacement sequences are square summable. Single-term sequences show that ultraweak convergence implies weak operator convergence. In particular a weakly closed \(M\) is ultraweakly closed. These arguments do not identify the topologies on unbounded sets or prove a general characterization of normal maps.

## OA-MOD-BK-04 — Bounded increasing positive nets have strong suprema

Let \(a_i\in M_+\) be increasing on a nonempty directed set and \(a_i\leq CI\), \(C<\infty\). Then there is \(a\in M_+\) with
\[
\begin{gathered}
\langle a\xi,\xi\rangle=\sup_i\langle a_i\xi,\xi\rangle,\\
a_i\longrightarrow a\quad\text{strongly and ultraweakly}.
\end{gathered}
\tag{BK.4}
\]
It is the least upper bound even in \(B(H)_{\rm sa}\).

Here is a construction avoiding a representation theorem for an unverified quadratic supremum. The case \(C=0\) is immediate. For \(C>0\), if \(j\geq i\), apply (BK.1) to \(a_j-a_i\):
\[
\|(a_j-a_i)\xi\|^2
 \leq C\bigl(\langle a_j\xi,\xi\rangle-\langle a_i\xi,\xi\rangle\bigr).
\]
The scalar increasing bounded net has a supremum. Given two sufficiently late indices, choose a common upper index and use the displayed estimate twice and the triangle inequality. This proves that \(a_i\xi\) is Cauchy for every \(\xi\). Completeness yields a limit \(a\xi\). Passing to limits proves linearity and \(\|a\|\leq C\); passing to adjoint pairings proves self-adjointness. Its diagonal is the stated supremum, so \(0\leq a\leq CI\) and \(a\geq a_i\). Any self-adjoint upper bound dominates this diagonal, hence dominates \(a\). Strong closedness gives \(a\in M\), and BK-03 gives ultraweak convergence.

If the original upper bound is \(b\in M_+\), use \(C=\|b\|\); leastness gives \(a\leq b\). Applying the result to \(CI-a_i\) proves the decreasing-net version. Also, for fixed \(x\in M\),
\[
a_i\uparrow a\quad\Longrightarrow\quad x^*a_ix\uparrow x^*ax.
\tag{BK.5}
\]
The congruences are positive and increasing, and fixed multiplication preserves their strong limit. The theorem then identifies that limit with their supremum. No commutation between \(x\) and the net is required.

## Foundation F: Concrete preduals

*Programme source: OA-MOD, `public/src/concrete-preduals.md`, lines 8–247.*

## OA-MOD-CP-01 — Conventions and the precise foundations

Inner products are linear in their first variable. Thus the vector coefficient of \(T\in B(H)\) is \(\langle T\xi,\eta\rangle\). The conjugate complex vector space \(\overline H\) has vectors \(\overline\eta\) and scalar action \(\lambda\overline\eta=\overline{\overline\lambda\eta}\). Its inner product is \(\langle\overline\xi,\overline\eta\rangle_{\overline H}=\overline{\langle\xi,\eta\rangle_H}\), and its norm is \(\|\overline\eta\|=\|\eta\|\).

The Hilbert inputs are proved in [BK-01: Hilbert representation and bounded operators](#foundation-e-bounded-operators-and-topology). Every bounded sesquilinear form \(b\), linear in its first variable, has a unique representation \(b(\xi,\eta)=\langle T\xi,\eta\rangle\), and its least bound is \(\|T\|\). These written results apply to arbitrary complex Hilbert spaces, including zero spaces. Its real-to-complex Riesz conversion, bounded-form construction, adjoints and completion proof supply all of these results. The finite orthonormal-basis and linear-annihilator steps used in CP-02 and CP-05 are written at the end of [NP1](#foundation-b-norm-extension-and-convex-separation).

We also use **CP-DEP-HB**, real and complex norm-preserving Hahn–Banach extension, whose full dominated-extension argument, complex conversion and norming consequence are proved in [NP1](#foundation-b-norm-extension-and-convex-separation). For \(z\ne0\), extend the functional \(\lambda z\mapsto\lambda\|z\|\). This gives
\[
\|z\|=\sup_{\|f\|\le1}|f(z)|,\qquad f\in X^*,
\tag{CP.1}
\]
for every real or complex normed space \(X\); for \(z=0\) it is immediate. The one-dimensional extension just proved in NP1 gives this norming identity directly.

Here are the completion facts used below, so no trace-class or tensor-completion theorem is hidden in the construction. For a normed space \(X\), take Cauchy sequences in \(X\), identify two when the norm of their difference tends to zero, and set \(\|[x_n]\|=\lim_n\|x_n\|\). The reverse triangle inequality makes this well-defined, and the finite norm identities pass to limits. Constant sequences embed \(X\) isometrically and densely: \([x_n]\) is approximated by the constant sequences \(x_n\). The resulting space is complete. Indeed, from a Cauchy sequence of classes select a subsequence whose successive distances are at most \(2^{-k}\), and choose a vector of \(X\) within \(2^{-k}\) of its \(k\)-th class. These vectors form a Cauchy sequence in \(X\); its class is the limit of that subsequence, hence of the original Cauchy sequence. A bounded linear map from \(X\) to a Banach space extends uniquely to the completion by taking limits; density preserves its norm.

For reference, \(\ell^2(H)\) consists of sequences \(\xi=(\xi_n)\) with \(\sum_n\|\xi_n\|^2<\infty\), with the sum inner product. Cauchy–Schwarz for finite sums, followed by limits, proves convergence of the inner product and its usual identities. This is a Hilbert space. For a Cauchy sequence in it, take the coordinatewise limits in \(H\). The Cauchy estimates on every finite partial sum pass to those limits and then to their supremum, proving that the limit sequence is square summable and that convergence holds in the sum norm. No basis of \(H\) is used.

Bounded functional calculus and concrete operator topology are proved in **OA-MOD-BK-01**, **OA-MOD-BK-03** and **OA-MOD-BK-04**. The convex-closure corollary uses [NP2: point separation in arbitrary real locally convex spaces](#foundation-b-norm-extension-and-convex-separation); the bounded support theorem uses NP3 and its written BK prerequisites. Weak-star compactness and Krein–Smulian are not assumed or proved in the predual construction.

## OA-MOD-CP-02 — The projective norm is a genuine norm

Let \(V=H\otimes_{\mathbb C}\overline H\) be the algebraic tensor product: the free complex vector space on pairs \((\xi,\overline\eta)\), divided by the bilinearity relations. A bilinear function of those two variables therefore defines a unique linear function on \(V\).

Define
\[
\pi(u)=\inf\left\{\begin{gathered}
 \sum_{j=1}^m\|\xi_j\|\|\eta_j\|:\\
 u=\sum_{j=1}^m\xi_j\otimes\overline{\eta_j}
\end{gathered}\right\}.
\tag{CP.2}
\]
The zero sum is allowed. Every tensor has a finite representation, so this is finite. Rescaling representations proves absolute homogeneity; concatenating representations within any prescribed error of the two infima proves the triangle inequality.

For nondegeneracy, write a given tensor using finite-dimensional spans of its first and second vectors, and choose orthonormal bases \(e_1,\ldots,e_r\) and \(f_1,\ldots,f_s\) for those spans. Expansion gives
\[
u=\sum_{i,j}c_{ij}\,e_i\otimes\overline{f_j}.
\]
The bilinear coefficient test
\[
L_{ij}(\xi\otimes\overline\eta)
  =\langle\xi,e_i\rangle\langle f_j,\eta\rangle
\]
has \(|L_{ij}(u)|\le\pi(u)\), since its value on a pure tensor is at most \(\|\xi\|\|\eta\|\). It reads off \(c_{ij}\). If \(u\ne0\), some coefficient is nonzero: an expansion with all coefficients zero is the zero tensor. Thus \(\pi(u)>0\).

The same test with \(e=\xi/\|\xi\|\) and \(f=\eta/\|\eta\|\), when neither vector is zero, proves
\[
\pi(\xi\otimes\overline\eta)=\|\xi\|\|\eta\|.
\tag{CP.3}
\]
If a factor is zero, both sides vanish. Only finite-dimensional orthonormal bases were used.

Let \(E_H\) be the Banach completion of \((V,\pi)\) constructed in CP-01. We do not identify this completion with a space of trace-class operators.

## OA-MOD-CP-03 — Its dual is exactly \(B(H)\)

For \(T\in B(H)\), define on algebraic tensors
\[
\Phi_T\left(\sum_j\xi_j\otimes\overline{\eta_j}\right)
 =\sum_j\langle T\xi_j,\eta_j\rangle.
\]
Bilinearity makes this independent of the representation. Taking the infimum of the bound over all representations gives
\(|\Phi_T(u)|\le\|T\|\pi(u)\), so \(\Phi_T\) extends to \(E_H\).

Conversely, \(F\in E_H^*\) defines
\(b(\xi,\eta)=F(\xi\otimes\overline\eta)\).
This is sesquilinear with
\(|b(\xi,\eta)|\le\|F\|\|\xi\|\|\eta\|\).
The bounded-form proof in BK-01 supplies a unique \(T\in B(H)\) representing \(b\). Equality on algebraic tensors and density give \(F=\Phi_T\). Finally,
\[
\|\Phi_T\|
\ge\sup_{\|\xi\|\le1,\ \|\eta\|\le1}
 |\langle T\xi,\eta\rangle|
=\|T\|.
\]
Here (CP.3) justifies the test tensors; no norm-attaining vector for \(T\) is presumed. Together with the upper bound this proves a complex-linear onto isometry
\[
B(H)\cong E_H^*,\qquad T\longmapsto\Phi_T.
\tag{CP.4}
\]
All assertions include \(H=\{0\}\). Injectivity of a completed map from \(E_H\) into an operator space is neither assumed nor needed.

## OA-MOD-CP-04 — Every tensor vector is a summable vector series

**Lemma.** Every \(u\in E_H\) has a norm-convergent representation
\[
u=\sum_{n=1}^\infty\xi_n\otimes\overline{\eta_n},
\qquad
\sum_n\|\xi_n\|\|\eta_n\|<\infty.
\tag{CP.5}
\]
The factors can be chosen so that both sequences lie in \(\ell^2(H)\).

**Proof.** Choose algebraic \(v_k\) with \(\|u-v_k\|\le2^{-k}\). Put \(d_1=v_1\) and \(d_k=v_k-v_{k-1}\) for \(k\ge2\). Then \(\sum_k\pi(d_k)<\infty\), since
\(\pi(d_k)\le2^{-k}+2^{-(k-1)}\) for \(k\ge2\).
Represent each \(d_k\) as a finite sum with total cost at most \(\pi(d_k)+2^{-k}\). List those finite sums consecutively. Their total cost is finite; (CP.3) and completeness imply absolute convergence. The partial sums at the block ends are \(v_k\), so the sum is \(u\).

Discard zero terms and replace each remaining pair by
\[
\begin{gathered}
\xi'_n=\left(\frac{\|\eta_n\|}{\|\xi_n\|}\right)^{1/2}\xi_n,\\
\eta'_n=\left(\frac{\|\xi_n\|}{\|\eta_n\|}\right)^{1/2}\eta_n.
\end{gathered}
\]
The positive real multipliers are reciprocal, so the tensor is unchanged. Both new squared norms equal the original product \(\|\xi_n\|\|\eta_n\|\). The two new sequences are square summable. ∎

Conversely, \(\xi,\eta\in\ell^2(H)\) define a vector of \(E_H\) by (CP.5), since scalar Cauchy–Schwarz bounds the sum of the products. Evaluation gives
\[
\Phi_T(u)=\sum_n\langle T\xi_n,\eta_n\rangle.
\tag{CP.6}
\]
Thus \(\sigma(B(H),E_H)\) is exactly the ultraweak topology defined by the vector-series tests in OA-MOD-BK-03. This equality holds on all of \(B(H)\), without a norm-bound restriction.

## OA-MOD-CP-05 — Quotients and annihilators, with the norm checks

Let \(E\) be a Banach space and \(F\subseteq E\) a closed linear subspace. The quotient norm on \(Q=E/F\) is
\[
\|e+F\|_Q=\inf_{f\in F}\|e+f\|.
\]
Norm zero means \(e\) belongs to the closure of \(F\), hence to \(F\); its other norm properties follow by adding and rescaling representatives.

The quotient is complete. Given a Cauchy sequence in \(Q\), select a subsequence \(z_k\) with
\(\|z_{k+1}-z_k\|_Q\le2^{-k}\).
Choose representatives \(d_k\in E\) of those differences with
\(\|d_k\|\le2^{1-k}\), and a representative \(e_1\) of \(z_1\).
The convergent series \(e_1+\sum_kd_k\) represents the limit of the subsequence. The Cauchy property gives convergence of the full sequence.

For the quotient map \(q:E\to Q\), composition gives an onto isometry
\[
q^*:Q^*\longrightarrow F^\perp
 =\{T\in E^*:T|_F=0\}.
\tag{CP.7}
\]
Indeed, a functional annihilating \(F\) defines a functional on \(Q\). Taking the infimum over representatives bounds its quotient norm by its norm on \(E\). The reverse bound follows because \(q\) is contractive. The same bounds prove that composition is isometric.

If a linear subspace \(M\subseteq E^*\) is weak-star closed, then
\[
\begin{gathered}
M=(M_\perp)^\perp,\\
M_\perp=\{e\in E:T(e)=0\ \text{for all }T\in M\}.
\end{gathered}
\tag{CP.8}
\]
For the nontrivial inclusion, take \(T_0\notin M\). A basic weak-star neighborhood disjoint from \(M\) tests finitely many vectors \(e_1,\ldots,e_n\). Let
\(L(T)=(T(e_1),\ldots,T(e_n))\).
Then \(L(T_0)\notin L(M)\), since equality would put an element of \(M\) in that neighborhood. Finite-dimensional linear algebra supplies \(\lambda\) on \(\mathbb C^n\) vanishing on \(L(M)\) but not at \(L(T_0)\). Write \(\lambda(z)=\sum_jc_jz_j\). The vector \(e=\sum_jc_je_j\) belongs to \(M_\perp\), but \(T_0(e)\ne0\). This proves (CP.8) without locally convex separation.

## OA-MOD-CP-06 — The concrete predual and its intrinsic norm

Let \(M\subseteq B(H)\) be a weak operator closed unital *-subalgebra. It is ultraweakly closed by OA-MOD-BK-03. Under (CP.4), define
\[
F=M_\perp\subseteq E_H,\qquad M_*=E_H/F.
\tag{CP.9}
\]
The subspace \(F\) is norm closed, being an intersection of kernels of bounded functionals. Equations (CP.7)–(CP.8) prove that canonical evaluation is an onto isometry
\[
M\cong(M_*)^*.
\tag{CP.10}
\]

Identify \(u+F\) with \(x\mapsto\Phi_x(u)\) on \(M\). This is injective by the definition of \(F\). Its operator norm is exactly the quotient norm: apply the norming identity (CP.1) to \(M_*\), and identify its dual unit ball with the unit ball of \(M\) by (CP.10). Thus \(M_*\) is an isometric Banach subspace of \(M^*\), and is norm closed there.

By CP-04 its elements are exactly the restricted vector-series functionals
\[
f(x)=\sum_n\langle x\xi_n,\eta_n\rangle,\qquad
\xi,\eta\in\ell^2(H).
\tag{CP.11}
\]
The weak-star topology from this pairing is therefore the inherited ultraweak topology.

Moreover \(M_*\) is exactly the space of ultraweakly continuous complex-linear functionals. One inclusion is immediate. For the other, continuity of a linear \(f\) implies that it vanishes whenever finitely many controlling vector-series functionals \(f_1,\ldots,f_r\) all vanish: rescale such a vector and use continuity at zero. Hence \(f\) factors through
\(x\mapsto(f_1(x),\ldots,f_r(x))\).
A linear functional on this finite-dimensional image extends algebraically to \(\mathbb C^r\), so \(f\) is a finite linear combination of the \(f_j\). It belongs to \(M_*\).

This establishes a concrete predual and its topology. It does not prove uniqueness among arbitrary abstract Banach preduals or construct the bidual W* algebra of a general C*-algebra.

## OA-MOD-CP-07 — Positive functionals, closed cones and norm closure

Write \(M_*^+\) for the positive functionals in \(M_*\). For \(\xi\in\ell^2(H)\),
\[
\omega_\xi(x)=\sum_n\langle x\xi_n,\xi_n\rangle
\]
belongs to \(M_*^+\). These functionals separate \(M_+\): if \(a\ge0\) is nonzero, some \(\xi\in H\) satisfies
\(\langle a\xi,\xi\rangle=\|a^{1/2}\xi\|^2>0\).
Single-vector tests also detect positivity of arbitrary operators: nonnegative real diagonal coefficients imply self-adjointness by polarization and then positivity.

Every \(f\in M_*\) is a linear combination of four positive members. Use (CP.11) and put
\[
\begin{gathered}
\omega_k(x)=\sum_n
 \langle x(\xi_n+i^k\eta_n),\,\xi_n+i^k\eta_n\rangle,\\
k=0,1,2,3.
\end{gathered}
\]
Each sequence is square summable. Expansion gives
\[
f=\frac14\sum_{k=0}^3 i^k\omega_k.
\tag{CP.12}
\]
The identity holds for any sesquilinear form; no self-adjointness of \(x\) is required.

For a positive linear functional \(\omega\), positive/negative parts show that it is real on self-adjoint elements and preserves adjoints. Applying positivity to
\(\omega((x+\lambda y)^*(x+\lambda y))\) for every complex \(\lambda\) gives
\[
|\omega(y^*x)|^2\le\omega(x^*x)\omega(y^*y).
\tag{CP.13}
\]
If the second diagonal value is positive, minimize the scalar quadratic polynomial in \(\lambda\); if it is zero, varying the magnitude and argument of \(\lambda\) forces the mixed coefficient to vanish. With \(y=1\) and \(x^*x\le\|x\|^2 1\), this proves boundedness and
\[
|\omega(x)|\le\omega(1)\|x\|,\qquad
\|\omega\|=\omega(1).
\tag{CP.14}
\]
The reverse norm inequality tests \(1\); the zero algebra is immediate. In particular, for \(0\le\psi\le\omega\),
\[
\|\omega-\psi\|=\omega(1)-\psi(1).
\tag{CP.15}
\]

The positive cone of \(M\) is ultraweakly closed, as the intersection of the conditions
\(\langle x\xi,\xi\rangle\in[0,\infty)\).
Every closed norm ball is ultraweakly closed, since
\[
\begin{gathered}
\|x\|\le R
\quad\Longleftrightarrow\\
|\langle x\xi,\eta\rangle|\le R\|\xi\|\|\eta\|\\
(\xi,\eta\in H).
\end{gathered}
\]
The adjoint is conjugate-linear and ultraweakly continuous:
\[
\sum_n\langle x^*\xi_n,\eta_n\rangle
=\overline{\sum_n\langle x\eta_n,\xi_n\rangle}.
\]
Fixed multiplication is ultraweakly continuous by BK-03.

Norm closure of \(M_*\) in CP-06 has a useful concrete interpretation: a norm-Cauchy sequence in the isometric quotient has a limit there; the associated functionals converge in operator norm. Any operator-norm limit in \(M^*\) must be that same predual functional. Positivity survives norm limits by evaluation on each positive element, so \(M_*^+\) is norm closed.

Finally, every \(\omega\in M_*^+\) preserves bounded increasing positive suprema. If \(a_\alpha\uparrow a\), BK-04 supplies ultraweak convergence, whence
\(\omega(a_\alpha)\uparrow\omega(a)\).
This proves the ultraweak-to-order direction without a theorem about weights. The converse is not an input to this unit.

## Foundation G: Nonunital bicommutant density

*Programme source: OA-MOD, `public/src/hilbert-algebra-kernel.md`, lines 102–125.*

**Nonunital density lemma.** If a *-subalgebra \(\mathcal C\subseteq B(H)\) is nondegenerate, then
\[
\overline{\mathcal C}^{\mathrm{SOT}}
=\overline{\mathcal C}^{\mathrm{WOT}}
=\mathcal C''.
\tag{HA.9}
\]
No norm bound is asserted for the approximating nets.

**Proof.** Fix \(T\in\mathcal C''\) and finitely many vectors \(\xi_1,\ldots,\xi_n\). On \(H^n\), write \(D(c)=\operatorname{diag}(c,\ldots,c)\), \(\Xi=(\xi_1,\ldots,\xi_n)\), and let \(P\) project onto
\[
K=\overline{\{D(c)\Xi:c\in\mathcal C\}}.
\]
The set inside closure is linear. Since \(\mathcal C\) is an algebra closed under adjoints, \(K\) is invariant under \(D(c)\) and \(D(c)^*\). Thus \(P\) commutes with every \(D(c)\). For all \(c\in\mathcal C\),
\[
D(c)(I-P)\Xi=(I-P)D(c)\Xi=0.
\]
Nondegeneracy of \(\mathcal C\), applied to each coordinate, gives \((I-P)\Xi=0\). This is the step that replaces a unit.

Every matrix entry \(P_{jk}\) commutes with \(\mathcal C\), so it commutes with \(T\). Consequently \(D(T)P=PD(T)\), and \(D(T)\Xi\in K\). Given \(\varepsilon>0\), the definition of \(K\) therefore supplies \(c\in\mathcal C\) with
\[
\sum_{j=1}^n\|(c-T)\xi_j\|^2<\varepsilon^2.
\]
These conditions characterize membership of \(T\) in the strong closure. The reverse inclusions follow because strong convergence implies weak operator convergence, and \(\mathcal C''\) is weak operator closed by OA-MOD-BK-02. \(\square\)

## Foundation H: Kaplansky density

*Programme source: OA-MOD, `public/src/hilbert-algebra-approximation.md`, lines 127–220.*

## OA-MOD-HAP-04 — Why self-adjoint weak density gives strong density

We need an approximation theorem for the original multiplication algebra, which need not contain an identity or be norm closed. We first prove its topological ingredient.

Let \(\mathcal C\subseteq B(K)\) be a nondegenerate *-subalgebra, and write \(N=\mathcal C''\). [HA03, the nonunital proof](#foundation-g-nonunital-bicommutant-density), gives
\[
\overline{\mathcal C}^{\,\mathrm{WOT}}
=\overline{\mathcal C}^{\,\mathrm{SOT}}=N.
\tag{HAP.12}
\]
Its proof uses nondegeneracy in place of a unit. In particular, it does not put an unproved bound on its approximants.

**Lemma.** The self-adjoint part \(\mathcal C_{\mathrm{sa}}\) is strongly dense in \(N_{\mathrm{sa}}\).

**Proof.** Regard \(V=N_{\mathrm{sa}}\) as a real vector space. A strongly continuous real-linear functional \(\ell\) on \(V\) is bounded by finitely many strong seminorms. More explicitly, continuity at zero and homogeneity give \(\xi_1,\ldots,\xi_n\in K\) and \(C<\infty\) with
\[
|\ell(a)|\leq C\left(\sum_{j=1}^n\|a\xi_j\|^2\right)^{1/2}
\quad(a\in V).
\tag{HAP.13}
\]
If the seminorm on the right vanishes, homogeneity forces \(\ell(a)=0\). Thus \(\ell\) factors through the real-linear map
\[
a\longmapsto(a\xi_1,\ldots,a\xi_n)\in K^n.
\]
The induced bounded real functional on its range extends to the underlying real Hilbert space \(K^n_{\mathbb R}\), by real Hahn–Banach. Real Riesz representation supplies \(\eta_1,\ldots,\eta_n\in K\) such that
\[
\ell(a)=\operatorname{Re}\sum_{j=1}^n\langle a\xi_j,\eta_j\rangle.
\tag{HAP.14}
\]
This is weak-operator continuous. Conversely every weak-operator continuous functional is strongly continuous, since the strong topology is finer.

It follows directly from real locally convex separation that a convex subset of \(V\) has the same strong and weak-operator closures. Indeed, a point outside its strong closed convex closure is separated from that closure by a strongly continuous real functional, which by (HAP.14) is weak-operator continuous. Such a point is also outside its weak closure; the opposite closure inclusion follows from the relative strength of the topologies.

Finally, if \(a=a^*\in N\), (HAP.12) supplies \(c_i\in\mathcal C\) with \(c_i\to a\) weakly. Adjoint is weak-operator continuous, so
\((c_i+c_i^*)/2\to a\) weakly. Hence \(\mathcal C_{\mathrm{sa}}\) is weakly dense in \(V\). It is convex, and the preceding paragraph proves strong density. \(\square\)

## OA-MOD-HAP-05 — Contractive approximation from a nonunital algebra

**Foundation theorem and alternative proof.** The canonical programme statement is Theorem 7.1(1)–(2) of *Kaplansky’s density theorem and its consequences*, in *Foundations of von Neumann algebras*. It allows degenerate as well as nondegenerate subalgebras and does not require norm closure. HAP04 identifies the weak closure in the present nondegenerate setting; the complete proof below is an alternative for that setting. Peterson’s free Theorem 2.6.4 provides a comparison. The proof explicitly returns from the norm closure to the original algebra, which need not contain an identity.

**Theorem.** For the algebra \(\mathcal C\) in HAP-04, every contraction \(x\in N\) is the strong* limit of a net of contractions from \(\mathcal C\). If \(x=x^*\), the approximants may also be chosen self-adjoint.

**Alternative proof for self-adjoint contractions.** Define by bounded continuous functional calculus
\[
\begin{gathered}
y=x\bigl(I+(I-x^2)^{1/2}\bigr)^{-1},\\
f(t)=\frac{2t}{1+t^2}\quad(t\in\mathbb R).
\end{gathered}
\tag{HAP.15}
\]
The inverse exists because its positive denominator is at least \(I\). The operator \(y\) is self-adjoint. The scalar identity
\[
f\left(\frac{t}{1+\sqrt{1-t^2}}\right)=t
\quad(-1\leq t\leq1)
\]
gives \(f(y)=x\). Also \(|f(t)|\leq1\) for every real \(t\).

Choose \(c_i\in\mathcal C_{\mathrm{sa}}\) with \(c_i\to y\) strongly, by HAP-04. For \(z=i\) and \(z=-i\), the resolvent identity is
\[
\begin{aligned}
&(c_i-zI)^{-1}-(y-zI)^{-1}\\
&\quad=(c_i-zI)^{-1}(y-c_i)(y-zI)^{-1}.
\end{aligned}
\tag{HAP.16}
\]
The first factor has norm at most one, by the continuous calculus of the bounded self-adjoint \(c_i\). Applying strong convergence to the fixed vector \((y-zI)^{-1}\xi\) proves strong convergence of these resolvents. Consequently
\[
\begin{gathered}
f(c_i)=(c_i-iI)^{-1}+(c_i+iI)^{-1}\\
\longrightarrow f(y)=x
\quad\hbox{strongly}.
\end{gathered}
\tag{HAP.17}
\]
This argument has not assumed uniform bounds on the \(c_i\).

Each \(d_i=f(c_i)\) is a self-adjoint contraction in the norm closure of \(\mathcal C\). To check the last assertion in the nonunital case, approximate \(f\) by real polynomials \(p_k\) on a compact interval containing \(\sigma(c_i)\) and \(0\). Since \(f(0)=0\), the polynomials \(p_k(t)-p_k(0)\) still approximate \(f\) uniformly and have zero constant term. Their values at \(c_i\) belong to \(\mathcal C_{\mathrm{sa}}\).

For \(0<\varepsilon<1\), choose \(b_{i,\varepsilon}\in\mathcal C_{\mathrm{sa}}\) with
\(\|b_{i,\varepsilon}-d_i\|<\varepsilon\), and set
\[
a_{i,\varepsilon}=(1+\varepsilon)^{-1}b_{i,\varepsilon}.
\tag{HAP.18}
\]
Then \(\|a_{i,\varepsilon}\|\leq1\), and
\(\|a_{i,\varepsilon}-d_i\|<2\varepsilon\).
The product net, directed by increasing \(i\) and decreasing \(\varepsilon\), converges strongly to \(x\). All its terms and its limit are self-adjoint, so it also converges strongly*.

**Alternative proof for arbitrary contractions.** The algebra \(M_2(\mathcal C)\) is nondegenerate on \(K\oplus K\). Its weak closure is \(M_2(N)\): weak operator convergence of these finite matrices is exactly entrywise weak convergence, and (HAP.12) approximates each entry, with the finite product of the indexing sets handling simultaneous approximation. Thus its generated von Neumann algebra is \(M_2(N)\).

Apply the self-adjoint result to
\[
\begin{gathered}
X=\begin{pmatrix}0&x\\x^*&0\end{pmatrix}\in M_2(N),\\
\|X\|=\|x\|\leq1.
\end{gathered}
\tag{HAP.19}
\]
Let \(A_i\in M_2(\mathcal C)\) be self-adjoint contractions converging strongly to \(X\). If \(b_i=(A_i)_{12}\), then \(b_i\in\mathcal C\), \(\|b_i\|\leq1\), and \((A_i)_{21}=b_i^*\). Coordinate-vector tests give both \(b_i\to x\) and \(b_i^*\to x^*\) strongly. \(\square\)

This alternative proves the canonical Kaplansky statement in the present nondegenerate case by bounded functional calculus and real separation. It applies to \(\mathcal C=L(\mathcal A)\), not merely to its norm closure. It requires neither SK-09 nor modular theory. Scaling gives the corresponding approximation bound \(\|b_i\|\leq\|x\|\) for every \(x\in N\), with the zero case handled by the constant zero net.

