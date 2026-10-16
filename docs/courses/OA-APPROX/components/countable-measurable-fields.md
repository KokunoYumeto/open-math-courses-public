# Countably generated measurable fields and their algebras

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Self-checked by the writing AI. New text: CC0.*

The central tracial construction needs measurable Hilbert spaces, decomposable operators, countably generated algebra fields, their centers and uniqueness on a fixed measure space. We prove these statements for a probability space. The operator selections come from compact metric balls and countably many continuous equations. No theorem asserting a standard Borel structure on the space of all von Neumann algebras is an input.

We use the complete [scalar integration proofs, Sections 0–2](../../OA-MOD/notes/analytic-programme/scalar-integration-programme.html), scalar Hilbert-space and bounded operator proofs, and the compact metric facts in [SS2](../../OA-MOD/notes/analytic-programme/spectral-scalar-prerequisites.html#ss2-the-topology-needed-on-a-compact-metric-space). These supply countable additivity, monotone and dominated convergence, scalar Cauchy–Schwarz, completeness, Hilbert representation of bounded functionals and elementary compact metric topology. Bicommutants and bounded density use the full bounded density arguments. Inner products here are linear in the second variable.

## MF1. A countable Gram field

Let \((Y,\Sigma,\mu)\) be a probability space. For each \(y\), let \(H_y\) be a Hilbert space with a sequence \(\xi_j(y)\) whose complex linear span is dense. Suppose
\[
y\longmapsto \langle \xi_i(y),\xi_j(y)\rangle
\]
is measurable for every \(i,j\). A section \(v\), with \(v(y)\in H_y\), is called measurable when every \(\langle \xi_j(y),v(y)\rangle\) is measurable.

Apply Gram–Schmidt in the given order, retaining a zero vector at a dependent step. Explicitly,
\[
r_j=\xi_j-\sum_{i<j}e_i\langle e_i,\xi_j\rangle,\qquad
e_j=\begin{cases}r_j/\|r_j\|,&\|r_j\|>0,\\0,&\|r_j\|=0.\end{cases}
\]
Every coefficient and the test \(\|r_j\|>0\) is measurable. The nonzero \(e_j(y)\) form an orthonormal basis, and their span has the same closure as the original sequence.

A section is measurable exactly when all its coordinates \(\langle e_j,v\rangle\) are measurable. One implication follows from the finite formulas expressing \(e_j\) in the \(\xi_i\). For the other, the orthogonal expansions
\[
v=\lim_{n\to\infty}\sum_{j\le n}e_j\langle e_j,v\rangle
\]
give all pairings with the \(\xi_i\) as pointwise limits of measurable functions. These expansions also show that norms and pairings of measurable sections are measurable. Pointwise norm limits, sums and products by measurable scalar functions preserve measurability. Pairings with every measurable section test exactly the same class, since the \(\xi_j\) themselves are measurable. This proves both existence and uniqueness of the measurable structure containing the fundamental sequence.

Put \(K=\ell^2(\mathbb N)\), with its usual basis \(\epsilon_j\). The map
\[
J_yv=(\langle e_j(y),v\rangle)_j
\]
is an isometry onto \(p(y)K\), where \(p(y)\) is the diagonal projection with \(j\)-th entry \(\|e_j(y)\|^2\in\{0,1\}\). This projection field has measurable matrix entries. A section is measurable exactly when its image under \(J_y\) has measurable coordinates. Conversely, a \(K\)-valued section in \(p(y)K\) with measurable coordinates pulls back to a measurable section. The finite coordinate approximations prove both assertions, without requiring the dimension to be constant.

These statements apply, in particular, to the Hilbert completions of countable positive Gram matrices. On the formal complex span of the countably many symbols, positivity follows by approximating finite complex coefficient lists by Gaussian-rational lists. Quotient by the null seminorm, use scalar Cauchy–Schwarz to see that the pairing descends, and complete by the Hilbert-space completion construction. Positivity and the algebraic identities need hold only outside one measurable null set; replacing the entire field on that set gives a field defined everywhere.

## MF2. The direct integral and localization

Let \(\mathcal H\) be the measurable sections with finite
\[
\|v\|_{\mathcal H}^2=\int_Y\|v(y)\|^2\,d\mu(y),
\]
modulo equality almost everywhere. Integration of the fiber pairing defines its inner product. The integral Cauchy–Schwarz inequality proves that it is well-defined.

This space is complete. From a Cauchy sequence choose a subsequence \(v_{n_k}\) with
\(\|v_{n_{k+1}}-v_{n_k}\|_{\mathcal H}\le2^{-k}\).
Since \(\mu(Y)=1\), scalar Cauchy–Schwarz gives
\[
\int_Y\sum_k\|v_{n_{k+1}}(y)-v_{n_k}(y)\|\,d\mu(y)
\le\sum_k2^{-k}<\infty.
\]
Monotone convergence therefore makes the series of pointwise norms finite outside a measurable null set. Completeness in each fiber gives a limit section there; put it equal to zero on that set. MF1 makes the section measurable. For a finite tail, the triangle inequality in \(\mathcal H\) bounds the tail norm by the sum of the corresponding \(2^{-k}\). Fatou's inequality gives the same bound for its pointwise limit. Thus the subsequence, and then the original Cauchy sequence, converges in \(\mathcal H\).

The sections \(1_E e_j\), \(E\in\Sigma\), have dense linear span. Indeed, truncate any measurable section to its first finitely many orthogonal coordinates. The squared error decreases to zero pointwise and is bounded by \(\|v(y)\|^2\), so dominated convergence gives convergence in \(\mathcal H\). Approximate each of the finitely many scalar \(L^2\) coordinates by simple functions. This proves the assertion.

More generally, any bounded fundamental sequence \(\eta_j\) is total after measurable localization: if \(v\) is orthogonal in \(\mathcal H\) to every \(1_E\eta_j\), its measurable scalar pairing with \(\eta_j\) has integral zero on every \(E\). Testing real and imaginary sign sets shows that this pairing is zero almost everywhere. The common exceptional set is null because \(j\) is countable. Fiber totality gives \(v=0\) almost everywhere.

## MF3. Operator fields and their exact norm

A field \(a(y):H_y\to H_y\) of bounded operators is measurable if it sends every measurable section to a measurable section. It suffices to test the \(\xi_j\), or the \(e_j\). For, the finite orthogonal expansions of a measurable section converge in each fiber, and their images converge there under the bounded operator \(a(y)\). MF1 then proves measurability. No common bound on the fiber norms is needed for this test.

Equivalently, all the entries
\(\langle e_i(y),a(y)e_j(y)\rangle\)
are measurable. The equivalence follows by the same finite expansions and the coordinate characterization in MF1. Adjoint fields are measurable by conjugating entries; sums, products and scalar multiples are measurable by the testing criterion. The same proof works between two such fields.

Enumerate all finite Gaussian-rational combinations of the \(e_j(y)\), and normalize each nonzero combination to norm one, taking zero otherwise. This is a countable family \(u_l(y)\) of measurable sections, dense in each nonzero fiber's unit sphere. Therefore
\[
\|a(y)\|=\sup_l\|a(y)u_l(y)\|
\]
is measurable. If this norm is essentially bounded, the formula
\[
(\widehat a\,v)(y)=a(y)v(y)
\]
defines a bounded operator on \(\mathcal H\). It satisfies
\[
\|\widehat a\|=\operatorname*{ess\,sup}_y\|a(y)\|.
\]
The upper bound follows by integration. For the lower bound, if \(\|a(y)\|>c\) on a set of positive measure, countability provides some \(l\) and a measurable subset \(E\) of positive measure on which \(\|a(y)u_l(y)\|>c\). Testing \(1_Eu_l\) gives \(\|\widehat a\|\ge c\). The case of zero fibers contributes nothing.

The assignment \(a\mapsto\widehat a\) respects sums, products and adjoints. For adjoints, integrate the fiber adjoint identity on two sections. Two fields have the same operator exactly when they agree almost everywhere: apply their difference to the bounded sections \(e_j\), and discard the union of the resulting countably many null sets.

Let \(\mathcal A=\{m_f:f\in L^\infty(Y,\mu)\}\), where \(m_fv=fv\). Every decomposable operator \(\widehat a\) commutes with \(\mathcal A\).

## MF4. The diagonal commutant

Conversely, every \(T\in\mathcal A'\) is decomposable. Choose measurable representatives \(\eta_j\) of \(Te_j\). For every finite Gaussian-rational tuple \(c=(c_j)\) and every \(E\in\Sigma\), commutation with \(m_{1_E}\) gives
\[
\int_E\Big\|\sum_jc_j\eta_j(y)\Big\|^2\,d\mu(y)
\le\|T\|^2\int_E\Big\|\sum_jc_je_j(y)\Big\|^2\,d\mu(y).
\]
Thus the pointwise inequality holds almost everywhere for each \(c\): otherwise its positive-difference set, or a bounded positive level set, contradicts the integral inequality. Outside the union of these countably many exceptional sets it extends to all finite complex tuples by continuity. Consequently \(e_j(y)\mapsto\eta_j(y)\) defines a bounded operator on their span, with norm at most \(\|T\|\), and extends to an operator \(a(y)\) on \(H_y\). Set \(a(y)=0\) on the exceptional set. Its values on the \(e_j\) are measurable, so MF3 applies.

For bounded \(f\), the equality \(T(fe_j)=fTe_j\) follows first for simple functions and then by uniform approximation. MF2 now gives \(T=\widehat a\). This proves
\[
\mathcal A'=\mathcal D,
\]
where \(\mathcal D\) denotes all decomposable operators.

Also \(\mathcal D'=\mathcal A\). Indeed, \(T\in\mathcal D'\) commutes with \(\mathcal A\subset\mathcal D\), hence is \(\widehat a\). It commutes with the countably many measurable rank-one fields
\[
E_{ij}(y)v=e_i(y)\langle e_j(y),v\rangle .
\]
Equality of decomposable fields gives, off one null set, commutation with every \(E_{ij}(y)\). On the nonzero fiber this forces \(a(y)=\lambda(y)1\): commuting with the nonzero diagonal rank-one projections makes it diagonal in that basis, and commuting with the off-diagonal units makes all its diagonal entries equal. Let \(j(y)\) be the first index with \(e_{j(y)}(y)\ne0\). Its level sets are measurable, and
\(\lambda(y)=\langle e_{j(y)}(y),a(y)e_{j(y)}(y)\rangle\)
is measurable there; put it equal to zero on zero fibers. It is essentially bounded, so \(T=m_\lambda\).

Both \(\mathcal A\) and \(\mathcal D\) are consequently von Neumann algebras, being commutants. Diagonal multipliers are identified modulo the null sets on the nonzero-fiber support.

## MF5. Compact metric selections from continuous equations

Let \(K_0\) be a compact metric space, and suppose \(F:Y\times K_0\to[0,\infty)\) has a continuous second-variable function \(F(y,\cdot)\) for every \(y\), and a measurable first-variable function \(F(\cdot,t)\) for every \(t\). Suppose
\[
C_y=\{t\in K_0:F(y,t)=0\}\ne\varnothing .
\]
There are measurable maps \(s_l:Y\to K_0\) such that \(s_l(y)\in C_y\) and \(\{s_l(y):l\ge1\}\) is dense in \(C_y\).

Here are the selection details. A compact metric space has a countable dense subset: for every positive integer \(n\), take a finite subcover of its open \(1/n\)-balls, and collect their centers. Balls with rational radii and these centers form a countable base. The same argument applies to any nonempty compact subset. For any fixed nonempty compact set \(B\subset K_0\), choose such a countable dense subset. Continuity gives
\[
\min_{t\in B}F(y,t)=\inf_{t\in B_0}F(y,t),
\]
which is measurable. Thus the event \(B\cap C_y\ne\varnothing\) is measurable, since the minimum is attained. The empty compact set has empty event.

Take countable finite-radius covers of \(K_0\) by closed balls with radii tending to zero, with interiors covering \(K_0\). Starting with a fixed compact \(B\) for which \(B\cap C_y\ne\varnothing\), choose the first ball at step \(k\) whose intersection with the preceding compact set still meets \(C_y\). Every test is a fixed-compact-set test on each finite choice history. There are countably many such histories, so the selected indices and centers are measurable. The nested nonempty compact intersections have diameters tending to zero. They have one common point in \(C_y\cap B\). Their selected centers converge to this point. The limit map is measurable: its distance to each point of a fixed countable dense subset is the limit of the corresponding measurable distances of the centers. These distances test inverse images of a countable base of open balls and hence of every open set.

Finally take a countable base of open sets \(U_l\) in \(K_0\). Each is a countable union of compact sets: when \(U_l\ne K_0\), use
\(\{t:d(t,K_0\setminus U_l)\ge1/m\}\);
for \(U_l=K_0\), use \(K_0\). On the measurable event \(C_y\cap U_l\ne\varnothing\), choose the first of these compact sets meeting \(C_y\), and apply the nested construction. Off that event use the selector constructed with \(B=K_0\). This gives \(s_l\). Every relatively open neighborhood meeting \(C_y\) contains a base set that meets \(C_y\), so the selectors are dense in \(C_y\). This proves the selection statement without a general measurable-selection theorem.

## MF6. Compact operator balls and commutant selections

The operator unit ball \(\mathcal K\subset B(\ell^2)\) is compact metrizable in its weak operator topology. One metric is the sum of the matrix-entry distances with positive summable weights, for instance
\[
d(S,T)=\sum_{i,j\ge1}2^{-i-j}
|\langle\epsilon_i,(S-T)\epsilon_j\rangle|.
\]
Convergence for this metric is exactly entrywise convergence on the unit ball. To prove compactness, successively select convergent subsequences of the bounded complex matrix entries and take a diagonal subsequence. The limiting matrix defines a form with
\[
\Big|\sum_{i,j}\overline{b_i}t_{ij}c_j\Big|\le\|b\|\,\|c\|
\]
for every finitely supported \(b,c\), by passing the original operator inequality to the limit. Hilbert representation and density give a bounded operator with this matrix and norm at most one. Thus every sequence has a convergent subsequence in the metric.

Here is the open-cover compactness argument. For every \(\varepsilon>0\) there is a finite \(\varepsilon\)-net: otherwise successive choices outside the preceding \(\varepsilon\)-balls give a sequence of mutually separated points, with no convergent subsequence. Any open cover has a radius \(\delta>0\) such that every \(\delta\)-ball is contained in a member of the cover. Otherwise choose, for each \(n\), a point whose \(1/n\)-ball has no such containment. A convergent subsequence has a limit in some open member. A ball about that limit lies in the same member, and for large subsequence indices contains the offending \(1/n\)-ball, a contradiction. A finite \(\delta/2\)-net then gives a finite subcover. This proves compactness. Finite metric nets, taken for each reciprocal integer radius, also supply a countable dense subset.

Let \(x_j(y)\) be countably many measurable contraction fields on the \(H_y\), with the family closed under adjoints. Under MF1 extend \(J_yx_j(y)J_y^*\) by zero to \(K\), and denote these fields by \(X_j(y)\). Their matrix entries are measurable. For \(S\in\mathcal K\), impose all the equations
\[
Sp(y)=S=p(y)S,\qquad SX_j(y)=X_j(y)S\quad(j\ge1).
\]
At each \(y\) these are countably many continuous equations in the weak operator topology, after testing all matrix entries. Multiplication by a fixed bounded operator is weak-operator continuous, so the continuity assertion is exact.

For fixed \(S\), every tested expression is measurable in \(y\). For example, the coordinates of \(X_j(y)\epsilon_l\) are measurable, and finite coordinate truncations show measurability of its pairing with a fixed vector. The same truncation argument works for \(p(y)\) and for \(X_j(y)^*\epsilon_i\). Enumerate the absolute values of all these matrix-entry defects as \(g_k(y,S)\). Then
\[
F(y,S)=\sum_{k\ge1}2^{-k}\min\{1,g_k(y,S)\}
\]
is measurable in \(y\) for fixed \(S\), continuous in \(S\) for fixed \(y\) by uniform convergence, and nonnegative. Its zero set is nonempty, containing zero, and is exactly the unit ball of the supported commutant.

MF5 gives countably many measurable selectors dense in this zero set. Their matrix entries are measurable; finite coordinate expansions make them measurable operator fields on the constant space \(K\), and pulling back under the \(J_y\) gives measurable contraction fields \(s_l(y)\) whose values are weak-operator dense in
\[
\{x_j(y):j\ge1\}'_1\subset B(H_y).
\]
They generate the whole commutant as a von Neumann algebra. Indeed, the generated algebra is weak-operator closed and contains the dense subset of its unit ball, so contains that unit ball and all its scalar multiples.

If the original generating fields are merely pointwise bounded, divide each by the positive measurable scalar \(\max\{1,\|x_j(y)\|\}\) first. At every point this changes neither its commutant nor the generated von Neumann algebra.

## MF7. Generated algebra, commutant and field uniqueness

Let \(M_y=\{x_j(y),x_j(y)^*:j\ge1\}''\), and write \(\int^\oplus M_y\) for all decomposable operators whose fibers belong to \(M_y\) almost everywhere. Let
\[
P=\bigl(\mathcal A\cup\{\widehat{x_j},\widehat{x_j}^*:j\ge1\}\bigr)''.
\]
We prove
\[
P=\int^\oplus M_y,\qquad
P'=\int^\oplus M_y'.
\]
An operator in \(P'\) commutes with \(\mathcal A\), so is decomposable by MF4. Commuting with the countably many generators is equivalent, by MF3, to commuting with their fiber values outside one common null set. This proves the formula for \(P'\).

Apply MF6 to the self-adjoint generator family to obtain measurable contractions \(s_l(y)\) generating \(M_y'\). Their integrals and \(\mathcal A\) belong to \(P'\). If \(T\in P''=P\), it therefore commutes with \(\mathcal A\), is decomposable, and its fibers commute with all \(s_l(y)\) off one null set. Thus its fibers belong to \((M_y')'=M_y\). Conversely, a field with values in \(M_y\) commutes pointwise with every field with values in \(M_y'\), hence its integral belongs to \((P')'=P\). This proves the first formula as well. In particular the direct integral is a von Neumann algebra; closedness has not been assumed beforehand.

Suppose \(L_y\) is another countably generated measurable algebra field on the same Hilbert field, and
\(\int^\oplus M_y=\int^\oplus L_y\).
Take measurable contraction generators \(x_j\) for \(M_y\), as above. Each \(\widehat{x_j}\) belongs to the integral of \(L_y\), so its fibers lie in \(L_y\) almost everywhere. Countability gives \(M_y\subseteq L_y\) off one null set. Apply the same argument to generators of \(L_y\). Therefore \(M_y=L_y\) almost everywhere. The same argument proves the inclusion version. This is uniqueness on a fixed Hilbert field and base, not uniqueness of arbitrary disintegrations under changes of base.

## MF8. Centers and factor fibers

Use MF6 first for \(M_y'\), giving its measurable contraction generators \(s_l(y)\). Then
\[
Z(M_y)=\{x_j(y),x_j(y)^*,s_l(y),s_l(y)^*:j,l\ge1\}'.
\]
The right side is the intersection \(M_y'\cap M_y\). A second application of MF6 gives measurable contractions \(c_l(y)\) weak-operator dense in the unit ball of \(Z(M_y)\). Thus the center field is countably generated and measurable in exactly the sense needed in MF7.

The two identities of MF7 now give
\[
Z(P)=P\cap P'=\int^\oplus Z(M_y).
\]
If almost all nonzero fibers are factors, a central field is scalar there. MF4's first-active-coordinate formula makes that scalar measurable, so \(Z(P)=\mathcal A\).

Conversely suppose \(Z(P)=\mathcal A\). Each integral \(\widehat{c_l}\) is then a diagonal multiplier. Equality of decomposable representatives makes \(c_l(y)\) scalar almost everywhere. Outside the union of the countably many exceptional sets all the \(c_l(y)\) are scalar. Scalars form a weak-operator closed subspace, and these values are dense in the central unit ball. Hence \(Z(M_y)=\mathbb C1\) there. Almost every nonzero fiber is a factor.

The exceptional set can be chosen measurable. To test whether a measurable field \(c(y)\) is scalar on a nonzero fiber, take its pairing with the first active \(e_j(y)\) as \(\lambda(y)\), and test the countably many identities
\[
\langle e_i(y),c(y)e_j(y)\rangle
=\lambda(y)\langle e_i(y),e_j(y)\rangle.
\]
All entries and first-active-index level sets are measurable. Apply this test to every \(c_l\). Its simultaneous validity is exactly scalarity of the full center.

## MF9. Tensoring the field with a countable Hilbert space

The fundamental sections \(\xi_j(y)\otimes\epsilon_k\), with \((j,k)\) countable, give the measurable field \(H_y\otimes\ell^2\) by MF1. The assignment
\[
v\otimes\epsilon_k\longmapsto
\bigl(y\longmapsto v(y)\otimes\epsilon_k\bigr)
\]
extends to a unitary from \(\mathcal H\otimes\ell^2\) onto its direct integral. It preserves inner products on finite sums by direct integration; its range is dense by MF2 applied to the tensor fundamental sequence.

Under this unitary, \(\widehat a\otimes1\) has field \(a(y)\otimes1\), and \(1\otimes E_{kl}\) has its constant matrix-unit field. The spatial algebra \(P\bar\otimes B(\ell^2)\) is generated by these fields and the diagonal algebra. Its fiber generators generate \(M_y\bar\otimes B(\ell^2)\), by the definition of the spatial tensor product and bounded strong approximation in each tensor leg. MF7 therefore gives
\[
P\bar\otimes B(\ell^2)
=\int^\oplus\bigl(M_y\bar\otimes B(\ell^2)\bigr)\,d\mu(y).
\]
If a countable collection of decomposable full matrix units generates the algebra on the left, all their algebraic identities hold simultaneously in the fibers off one null set, by MF3. MF7 then identifies the fiber algebra generated by these units with the displayed stabilized fiber almost everywhere. This proves the precise passage used in the central tracial assembly.

## Mathematical sources

E. G. Effros, [*The Borel space of von Neumann algebras on a separable Hilbert space*](https://msp.org/pjm/1965/15-4/pjm-v15-n4-p07-p.pdf), *Pacific Journal of Mathematics* 15 (1965), 1153–1164, develops Borel choices for weakly closed dual subspaces and the Borel operations on von Neumann algebras. The compact continuous-equation selections above prove only the choices needed for a given countable field. They do not assert the general standard-Borel-space theorem.

The scalar integration, Hilbert-space, compact metric and bounded operator arguments named at the start supply the remaining inputs. All null-set conclusions concern countable construction data or a specified operator; there is no assertion that every element of a direct-integral algebra has a simultaneous pointwise evaluation on one universal conull set.
