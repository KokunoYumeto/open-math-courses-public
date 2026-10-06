# Normal positive maps and their preadjoints

**Self-checked by the writing AI.**

For a positive map, preserving increasing suprema is an order property. Ultraweak continuity is a topology property. This unit proves their equivalence and identifies the bounded map on preduals which records both. The proof applies to arbitrary von Neumann algebras and arbitrary bounded increasing nets, without separability, sigma-finiteness, faithfulness or identity preservation.

## Objects and the direction of the proof

Let \(M\subseteq B(H)\) and \(N\subseteq B(K)\) be concrete von Neumann algebras on arbitrary complex Hilbert spaces. Use the preduals constructed in **OA-MOD-CP-06**, so

\[
M=(M_*)^*,\qquad N=(N_*)^*
\]

isometrically, with the concrete ultraweak topologies \(\sigma(M,M_*)\) and \(\sigma(N,N_*)\). Statements transfer along already established concrete von Neumann algebra isomorphisms; no abstract representation theorem is assumed here. Inner products are linear in the first variable. Zero algebras and zero maps are included.

A bounded complex-linear map \(T:M\to N\) is **positive** when \(T(M_+)\subseteq N_+\). Say it is **order normal** when

\[
T(a)=\sup_\alpha T(a_\alpha)
\quad\text{for every bounded increasing net }0\le a_\alpha\uparrow a.
\tag{NP.1}
\]

The domain net is indexed by an arbitrary nonempty directed set. Positivity makes the image increasing, and boundedness makes it norm bounded; BK-04 supplies its supremum.

**Why boundedness is automatic here.** Suppose only that \(T\) is positive and complex linear. Positive/negative parts from BK01 show that \(T(h)\) is self-adjoint for self-adjoint \(h\). Apply \(T\) to \(-\|h\|1_M\le h\le\|h\|1_M\). Since \(T(1_M)\ge0\), this gives

\[
-\|h\|\|T1_M\|1_N\le T(h)\le\|h\|\|T1_M\|1_N,
\qquad \|T(h)\|\le\|T1_M\|\|h\|.
\]

For \(x=h+ik\), with \(h=(x+x^*)/2\) and \(k=(x-x^*)/(2i)\), both self-adjoint parts have norm at most \(\|x\|\). Therefore

\[
\|T(x)\|\le2\|T1_M\|\|x\|.
\tag{NP.0}
\]

This bound suffices to apply the theorems below to every positive complex-linear map between these algebras. It is not asserted to be the optimal norm formula. The zero-domain case gives the zero map directly.

The exact inputs are:

- **The concrete predual and its intrinsic norm and Positive functionals, closed cones and norm closure:** predual duality, identification with the ultraweakly continuous functionals, norm closure of the predual, positive spanning and positivity detection; for a positive functional \(\omega\), \(\|\omega\|=\omega(1)\).
- **The ultraweak convergence needed by finite cutoffs and Bounded increasing positive nets have strong suprema:** concrete ultraweak topology and convergence of bounded increasing positive nets to their suprema.
- **The full characterization:** an arbitrary order-normal weight is recovered pointwise on its positive cone as the supremum of its dominated positive ultraweakly continuous functionals.
- **The sigma-strong seminorms are vector seminorms:** the sigma-strong seminorms \(p_\omega(x)=\omega(x^*x)^{1/2}\), and their comparison with concrete strong topology on explicitly bounded sets.

This ordering is acyclic. The actual proof of NW-11 uses the finite-domain construction **WG-003–006**, not the representation-normality theorem **WG-007**. Its route from increasing-net normality to domination recovery is NW-02, NW-08 and NW-10. The predual and topology facts used there are constructed in CP without the scalar converse below. The written convex inputs are now in CV1–CV4, and NW01 identifies their exact uses. NW11 proves the weight theorem; CP06–CP08 and BK03–BK04 supply the bounded predual and topology facts. These are written programme proofs, not external citations in place of arguments.

## The scalar normality criterion

**Theorem.** A bounded positive linear functional \(\omega:M\to\mathbb C\) preserves bounded increasing positive suprema if and only if \(\omega\in M_*^+\), equivalently if and only if it is ultraweakly continuous.

**Proof.** If \(\omega\in M_*^+\), BK-04 gives \(a_\alpha\to a\) ultraweakly whenever \(0\le a_\alpha\uparrow a\) is bounded. Continuity and positivity give \(\omega(a_\alpha)\uparrow\omega(a)\).

Conversely, suppose \(\omega\) preserves these suprema. Its restriction to \(M_+\) is a finite-valued normal weight. By NW-11,

\[
\omega(a)=\sup\{\psi(a):\psi\in M_*^+,\ 
                   \psi(b)\le\omega(b)\text{ for all }b\in M_+\}.
\tag{NP.2}
\]

If \(\omega(1)=0\), the positive norm formula gives \(\omega=0\). Otherwise, use (NP.2) only at \(a=1\) to choose \(\psi_n\in M_*^+\) with \(\psi_n\le\omega\) and

\[
0\le\omega(1)-\psi_n(1)<1/n.
\]

The difference is positive, so CP-07 gives

\[
\|\omega-\psi_n\|=\omega(1)-\psi_n(1)\longrightarrow0.
\tag{NP.3}
\]

By norm closure from CP-06, \(\omega\in M_*\), and it is positive by hypothesis. ∎

Neither the family of dominated functionals nor the chosen sequence is asserted to be increasing. A sequence suffices here because it approximates one finite scalar supremum. This does not replace the arbitrary nets in the definition of normality.

## Ultraweak continuity is exactly existence of a preadjoint

This statement does not require positivity.

**Theorem.** A bounded complex-linear \(T:M\to N\) is ultraweakly continuous if and only if there is a bounded complex-linear map

\[
T_*:N_*\longrightarrow M_*
\]

such that

\[
(T_*\psi)(x)=\psi(Tx)\qquad(\psi\in N_*,\ x\in M).
\tag{NP.4}
\]

The map is unique, its Banach adjoint is \(T\) under the predual identifications, and

\[
\|T_*\|=\|T\|.
\tag{NP.5}
\]

**Proof.** If \(T\) is ultraweakly continuous, \(\psi T\) is an ultraweakly continuous functional on \(M\), hence belongs to \(M_*\) by CP-06. Define \(T_*\psi=\psi T\). This is linear and

\[
\|T_*\psi\|\le\|T\|\|\psi\|.
\]

Evaluation proves that \(T_*^*=T\).

Conversely, if (NP.4) holds and \(x_\alpha\to x\) ultraweakly, then

\[
\psi(Tx_\alpha)=(T_*\psi)(x_\alpha)
 \longrightarrow(T_*\psi)(x)=\psi(Tx)
\]

for every \(\psi\in N_*\). These are exactly the tests for ultraweak convergence in \(N\). There is no norm-bound requirement on this net.

Two preadjoints agree on evaluation at every \(x\in M\), so they are equal. Finally, isometric duality for \(N\) gives

\[
\|Tx\|=\sup_{\psi\in N_*,\,\|\psi\|\le1}|\psi(Tx)|
 \le\|T_*\|\|x\|.
\]

This proves \(\|T\|\le\|T_*\|\), completing the norm equality, including zero cases. ∎

The map \(T_*\) is the **preadjoint**. It acts on the specified preduals, not on the entire bounded duals \(N^*\) and \(M^*\).

## The positive-map equivalence

**Theorem.** For a bounded positive complex-linear \(T:M\to N\), the following are equivalent:

1. \(T\) preserves every bounded increasing positive-net supremum.
2. \(T\) is ultraweakly continuous.
3. \(T\) has the bounded preadjoint of NP-03.

The preadjoint is positive and has the same norm as \(T\). Any of these equivalent properties is called **normality**.

**Proof of 1 ⇒ 2.** Let \(\psi\in N_*^+\). CP-07 shows that \(\psi\) preserves bounded increasing positive suprema. If \(a_\alpha\uparrow a\), assumption 1 and this scalar fact give

\[
\psi(Ta)=\sup_\alpha\psi(Ta_\alpha).
\]

Thus \(\psi T\) is a bounded positive order-normal functional. NP-02 puts it in \(M_*^+\).

Positive predual functionals span \(N_*\) by CP-07. It follows that \(\psi T\in M_*\) for every \(\psi\in N_*\). Every defining ultraweak test on the target therefore pulls back to an ultraweakly continuous test on the source. This proves continuity.

**Proof of 2 ⇒ 1.** Let \(0\le a_\alpha\uparrow a\) be bounded. BK-04 and continuity give
\(T(a_\alpha)\to T(a)\) ultraweakly. Positivity makes \(T(a)\) an upper bound. If \(y=y^*\in N\) is another upper bound, then
\(y-T(a_\alpha)\ge0\) for every \(\alpha\).
The ultraweakly closed positive cone from CP-07 gives
\(y-T(a)\ge0\). Thus \(T(a)\) is the least upper bound.

The equivalence of 2 and 3 and the norm assertion are NP-03. For \(\psi\in N_*^+\), composition \(\psi T\) is positive, proving positivity of \(T_*\). ∎

This proves **OA-MOD-DEP-NORMAL-MAPS**, relative to the exact prerequisites in NP-01. The order clause is about arbitrary directed nets, and does not require a unit-preserving map or a faithful normal state.

## Composition and the converse construction

If \(T:M\to N\) and \(R:N\to P\) are normal bounded positive maps, their composite is positive and ultraweakly continuous, hence normal. Evaluation gives

\[
(RT)_*=T_*R_*,
\qquad
(\operatorname{id}_M)_*=\operatorname{id}_{M_*}.
\tag{NP.6}
\]

Indeed, for \(\rho\in P_*\) and \(x\in M\),
\((T_*R_*\rho)(x)=\rho(R(Tx))\).
Uniqueness in NP-03 proves the identity. The arrows reverse, and only
\(\|RT\|\le\|R\|\|T\|\) is automatic.

Conversely, a bounded positive linear \(S:N_*\to M_*\), where positivity means preservation of the predual positive cones, determines a unique normal positive map \(T:M\to N\). For \(x\in M\), the functional
\(\psi\mapsto(S\psi)(x)\) on \(N_*\) has norm at most \(\|S\|\|x\|\). Duality for \(N\) defines \(Tx\) by

\[
\psi(Tx)=(S\psi)(x).
\]

This defines a bounded linear map, and NP-03 gives ultraweak continuity, \(T_*=S\), and equality of norms. If \(x\ge0\) and \(\psi\in N_*^+\), the right side is nonnegative. Positivity detection by the predual gives \(Tx\ge0\), so NP-04 makes \(T\) normal.

This is a correspondence between bounded normal positive maps of the algebras and bounded positive maps in the reverse direction on their preduals. No order-completeness structure on the predual itself is being asserted.

## Normal representations and sigma-strong continuity

Let \(\pi:M\to N\) be a complex-linear *-homomorphism. It need not preserve the ambient identity. The element \(e=\pi(1_M)\) is a projection and
\(\pi(x)=e\pi(x)e\).
Positive square-root factorization proves that \(\pi\) is positive. Applying it to \(x^*x\le\|x\|^2 1_M\) gives

\[
0\le\pi(x)^*\pi(x)=\pi(x^*x)\le\|x\|^2e.
\]

Thus \(\pi\) is contractive. It has norm one if nonzero, since then \(e\) is a nonzero projection; otherwise its norm is zero.

NP-04 applies: preserving increasing positive suprema, ultraweak continuity and existence of a preadjoint are equivalent for \(\pi\). If these hold, then for every \(\psi\in N_*^+\),

\[
p_\psi(\pi(x))^2
=\psi(\pi(x)^*\pi(x))
=(\pi_*\psi)(x^*x)
=p_{\pi_*\psi}(x)^2.
\tag{NP.7}
\]

Since \(\pi_*\psi\in M_*^+\), this proves sigma-strong continuity on the entire algebra. Applying the same equality to \(x^*\) proves sigma-strong* continuity. No norm-bound restriction is needed for these two assertions.

In concrete representations, CP-08 consequently gives strong and strong* continuity on norm-bounded sets. It does not replace the preceding assertions by unrestricted strong-operator continuity. Also,

\[
\|\pi_*\psi\|=\psi(e)\qquad(\psi\in N_*^+).
\]

A normal state may therefore pull back to a functional of norm less than one, or zero, when \(e\ne1_N\).

**Isomorphisms of already established von Neumann algebras.** If \(\pi\) is a bijective *-homomorphism, both it and its inverse are positive and contractive. They are order isomorphisms on the self-adjoint parts, so they preserve every existing positive supremum: transport any competing upper bound through the inverse. By NP-04 they are ultraweakly continuous, and by (NP.7) they are sigma-strong and sigma-strong* continuous. Their preadjoints are inverse isometries, as follows from (NP.6) and contractivity in both directions. Thus these concrete topologies and preduals agree under such an isomorphism.

This statement assumes both algebras are already von Neumann algebras. It does not prove that the image of a faithful normal representation is weak operator closed. In particular it is not a substitute for the separate normal-representation image theorem. WG-007's order-net proof for a normal weight's GNS representation may now use NP-04 for its final normality step; WG-007 is a consumer of this theorem, not an input to NP-02.

## A model with arbitrarily many normal observations

For an arbitrary set \(I\), represent \(\ell^\infty(I)\) diagonally on \(\ell^2(I)\). The diagonal algebra is weak operator closed: a weak operator limit has zero off-diagonal coefficients, and its diagonal entries are bounded by the norm of the limiting operator.

Its concrete predual is \(\ell^1(I)\), with pairing

\[
\langle a,b\rangle=\sum_{i\in I}b_i a_i,
\qquad a\in\ell^\infty(I),\ b\in\ell^1(I).
\tag{NP.8}
\]

Here an absolutely summable family means that the supremum of its finite absolute subsums is finite; its support is countable, because for each positive integer \(m\) only finitely many coefficients can have magnitude at least \(1/m\).

To verify the predual assertion from CP, restrict a vector-series functional to diagonal operators. Its coefficients are

\[
b_i=\sum_n \xi_{n,i}\overline{\eta_{n,i}},
\qquad
\sum_i|b_i|
\le\sum_n\|\xi_n\|\|\eta_n\|<\infty.
\]

The absolute bound justifies interchanging the sums. To make this explicit, for finite \(F\subseteq I\) and finite \(E\subseteq\mathbb N\), Cauchy–Schwarz gives

\[
\sum_{n\in E}\sum_{i\in F}|\xi_{n,i}\overline{\eta_{n,i}}|
\le\sum_{n\in E}\|\xi_n\|\|\eta_n\|.
\]

Taking finite-subsum suprema proves absolute summability on \(\mathbb N\times I\). A finite subset with absolute sum within \(\varepsilon\) of the total makes every disjoint finite tail smaller than \(\varepsilon\); the same estimate controls tails in either order of summation. Thus both iterated sums converge to the same scalar sum. No countability of \(I\) is used. Conversely, given \(b\in\ell^1(I)\), choose
\(\xi_i=b_i/\sqrt{|b_i|}\), \(\eta_i=\sqrt{|b_i|}\) where \(b_i\ne0\), and set both to zero otherwise. These are square-summable vectors and give (NP.8) as one vector coefficient. The functional norm is \(\sum_i|b_i|\): the upper bound is immediate, and the reverse bound tests the bounded phases \(a_i=\overline{b_i}/|b_i|\), with arbitrary bounded values at zero coefficients. CP-06 now supplies exactly the claimed predual identification.

Let \((\omega_i)_{i\in I}\subseteq M_*^+\) satisfy
\(C=\sup_i\|\omega_i\|<\infty\), with the empty supremum interpreted as zero. Define

\[
T:M\to\ell^\infty(I),\qquad (Tx)_i=\omega_i(x).
\]

It is bounded and positive, with \(\|T\|=\sup_i\|\omega_i\|\), by taking the two independent suprema over \(i\) and the unit ball of \(M\). Increasing bounded positive suprema in the diagonal algebra are coordinatewise, so the scalar normality of each \(\omega_i\) proves that \(T\) is normal. Its preadjoint is

\[
T_*b=\sum_{i\in I}b_i\omega_i,
\tag{NP.9}
\]

where the sum converges absolutely in the Banach space \(M_*\), since
\(\sum_i\|b_i\omega_i\|\le C\sum_i|b_i|\).
Evaluation proves the formula.

If every \(\omega_i\) is a state, \(T\) preserves the identity. There is no requirement that one of them be faithful, that \(I\) be countable, or that their family be norm separable. For nonempty \(I\), the identity map of \(\ell^\infty(I)\) is obtained by taking the coordinate states, even when \(I\) is uncountable.

## Three exercises with complete solutions

**1. Detecting the identity on the predual.** For normal bounded positive \(T:M\to N\), prove

\[
T(1_M)=1_N
\quad\Longleftrightarrow\quad
\|T_*\psi\|=\|\psi\|\quad(\psi\in N_*^+).
\]

Give also the corresponding inequality criterion for \(T(1_M)\le1_N\), and explain the proper-identity case.

**Solution.** Positivity and the scalar norm formula give

\[
\|T_*\psi\|=\psi(T1_M),\qquad \|\psi\|=\psi(1_N).
\]

Unitality proves equality. Conversely, equality makes every positive predual functional vanish on the self-adjoint element \(T1_M-1_N\). Vector tests and polarization force it to be zero. The same positivity-detection argument gives

\[
T1_M\le1_N
\quad\Longleftrightarrow\quad
\|T_*\psi\|\le\|\psi\|\quad(\psi\in N_*^+).
\]

For \(\pi(x)=\operatorname{diag}(x,0)\), a vector state supported in the second summand pulls back to zero; the normal homomorphism preserves the identity of its own image, not that of the full target.

**2. Why multiplicativity was needed for sigma-strong continuity.** On \(H=\ell^2(\mathbb N)\), let \(J\) be coordinate conjugation and set
\(\tau(x)=Jx^*J\). Prove that \(\tau\) is normal and positive, but is not sigma-strong continuous.

**Solution.** Taking an adjoint and conjugating by \(J\) each reverses complex scalars, so their combination is complex linear. The map is isometric. For \(x\ge0\),

\[
\langle\tau(x)\xi,\xi\rangle
=\overline{\langle xJ\xi,J\xi\rangle}\ge0,
\]

proving positivity. More generally,

\[
\langle\tau(x)\xi,\eta\rangle=\langle xJ\eta,J\xi\rangle.
\]

This turns each square-summable vector-series test into another such test, proving ultraweak continuity and hence normality.

For \(n\ge2\), let \(x_n=e_{1n}\), so \(x_n\xi=\langle\xi,e_n\rangle e_1\). This norm-one sequence converges strongly to zero, hence sigma-strongly by CP-08. Its transpose is \(e_{n1}\), which sends \(e_1\) to \(e_n\) and is not strongly null. Thus \(\tau\) is not sigma-strong continuous. It reverses products; it is not a *-homomorphism. NP-06 therefore cannot be extended to all normal positive maps by dropping multiplicativity.

**3. A normal positive map with nonclosed range.** Define
\(T:\ell^\infty(\mathbb N)\to\ell^\infty(\mathbb N)\) by
\((Ta)_n=a_n/n\). Determine its preadjoint and whether its range is norm closed or ultraweakly closed.

**Solution.** Coordinatewise suprema show that \(T\) is order normal, and it is positive. Its norm is one by the coordinate \(n=1\). Under (NP.8),

\[
(T_*b)_n=b_n/n,\qquad \|T_*\|=1.
\]

The range contains every finitely supported sequence. Truncations of any bounded sequence converge ultraweakly by absolute summability of every \(\ell^1\) test, so this range is ultraweakly dense. It is proper, since the constant sequence \(1\) has no bounded preimage; hence it is not ultraweakly closed.

It is not norm closed either. The finite truncations of \(c_n=n^{-1/2}\) lie in the range and converge in supremum norm to \(c\). Its necessary preimage is \(n^{1/2}\), which is unbounded. This example is a positive map, not a representation, and makes no assertion about the separate faithful-normal representation image theorem.

## Exact exports and boundaries

NP-02 closes the bounded scalar order-normal/ultraweak equivalence. NP-03 proves the preadjoint characterization and exact norm for arbitrary bounded linear maps. NP-04 supplies **OA-MOD-DEP-NORMAL-MAPS** and the positive normal-map clause of **OA-MOD-DEP-PREDUAL**. NP-05 proves composition and the converse positive-predual construction. NP-06 gives the representation specialization, sigma-strong(+*) continuity, and transport under isomorphisms between already established concrete von Neumann algebras.

The proofs use the written CP, BK and NW prerequisites identified in NP01. No universal \(C^*\)-bidual theorem, normal-representation image-closure theorem, predual uniqueness theorem or spectral theorem is supplied by this unit.

**Related literature.** Uffe Haagerup's [*Normal weights on \(W^*\)-algebras*](https://doi.org/10.1016/0022-1236(75)90060-9), Corollary 1.9, identifies the scalar order and ultraweak notions. NP02 proves this consequence from the full weight theorem NW11 using approximation at the identity and norm closure of the concrete predual.

Abraham A. Westerbaan's [*The Category of Von Neumann Algebras*, version 2](https://arxiv.org/abs/1804.02203v2), Exercise 44 XV and Exercise 45 I, PDF p. 85, give the positive-map equivalence and the transpose phenomenon. His Definition 42 II–III, p. 79, starts with order-normal positive functionals and uses them to define the ultraweak topology. Our CP lessons instead construct the concrete predual from vector-series functionals. The scalar bridge NP02 is therefore proved explicitly here; Exercise 44 XV alone would not supply it under our starting definitions. NP08 develops the transpose hint with the full coefficient calculation and matrix-unit sequence. The preadjoint proofs, arbitrary-index model and three worked solutions are written in full above; these classical results and examples are not claimed as new discoveries.
