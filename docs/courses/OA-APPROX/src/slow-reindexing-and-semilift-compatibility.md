# Slow reindexing and semi-lift compatibility

*Written by GPT-6.1 Sol (OpenAI), Ultra. Course exposition: CC0-1.0 to the extent of rights held. Earlier programme and human-source notices retain their own terms.*

Fast reindexing makes a centralizing input commute with a prescribed separable algebra. Slow reindexing reverses which sequences are held fixed during the selection: its entire image commutes with the centralizing part of that prescribed algebra. It also makes a semi-lift agree on the image with its constant limit lift. That compatibility survives the counterexample to unrestricted fast equivariance.

Let \(M\ne0\) have separable predual and a faithful normal state \(\varphi\). Use \(M^\omega=N_\omega/I_\omega\), the normal subalgebra \(M_\omega=C_\omega/I_\omega\), and \(E_\omega:M^\omega\to M\) from the [multiplier](multiplier-ultraproducts-and-normal-embeddings.md) and [expectation](ultraproduct-expectations-and-semilift-ambiguity.md) lessons. Write \(\|\cdot\|_\#=\|\cdot\|_{\varphi,\#}\).

Subalgebras in this lesson contain the ambient unit. This is the common-unit convention for the unital target in Theorem 1.1. The normal quotient state is \(\rho=\varphi\circ E_\omega\); it is faithful even when neither \(M\) nor its centralizing algebra is a factor. The [general chosen-family construction](ultraproduct-expectations-and-semilift-ambiguity.md#general-convergent-lift-inputs) proves that (1) is a normal automorphism, preserves the centralizing subalgebra and restricts to \(\beta_\gamma\) on constants. These facts require no invariant state for the family.

## 1. The action condition and the theorem

A semi-lift \(\gamma\) is an actual automorphism of \(M^\omega\), represented by a family \(\gamma_k\to\beta_\gamma\) in the \(u\)-topology:
\[
\gamma(\pi(x_k))=\pi(\gamma_k(x_k)).
\tag{1}
\]
Although \(\beta_\gamma\) does not determine \(\gamma\), the given \(\gamma\) determines \(\beta_\gamma\): it is the restriction of \(\gamma\) to the constant copy of \(M\). Thus
\(\gamma\mapsto\beta_\gamma\) respects composition. Write \(b_\gamma=\beta_\gamma^\omega\) for the constant lift.

In particular, if two chosen families induce the same actual \(\gamma\), then for each constant \(a\) their images both equal the constant \(\gamma(a)\); faithfulness of the constant embedding makes their limits equal on every \(a\). For two actual semi-lifts \(\gamma,\eta\), restriction of their composition to constants is \(\beta_\gamma\beta_\eta\). A constant lift of that restriction need not be the original semi-lift. In (5) we only compare a constant lift with the representative of its actual domain image.

**Theorem 1.1.** Let \(P,Q\subset M^\omega\) have separable predual. Let \(H\) be a countable group of semi-lifts preserving \(P\). Assume that \(b_\gamma\in H\) for every \(\gamma\in H\). There is a normal unital injective *-homomorphism \(\Phi:P\to M^\omega\) with
\[
\begin{aligned}
\Phi(x)&=x&&(x\in P\cap M),\\
\Phi(P\cap M_\omega)&\subset M_\omega,\\
\Phi(P)&\subset (Q\cap M_\omega)'\cap M^\omega,\\
E_\omega(a\Phi(x))&=E_\omega(a)E_\omega(x)
&&(x\in P,\ a\in Q),\\
\gamma\Phi(x)&=b_\gamma\Phi(x)=\Phi(b_\gamma(x))
&&(x\in P,\ \gamma\in H).
\end{aligned}
\tag{2}
\]
No factor or trace hypothesis on \(M\) is needed.

The final line concerns \(b_\gamma(x)\) in the domain. It does not require \(\Phi(\gamma(x))=\gamma(\Phi(x))\). The associated constant lifts belong to \(H\), so \(b_\gamma(P)=P\), making the stated expression meaningful.

<a id="2-countable-data-and-the-first-selection"></a>

## 2. Error arrays and admissible rows

The selection mechanism can be separated from the operator algebra. Suppose that \(S_n\in\omega\) is an acceptable set of columns for row \(n\). On row \(n\), an increasing finite list of demands has error at most \(1/n\) whenever the column belongs to \(S_n\), and every demand eventually enters that list. A demand is allowed to enter at a later row; after it enters it must be tested at every subsequent row.

Define a column's depth to be the largest \(n\le k\) for which \(k\) belongs to every \(S_i\) with \(i\le n\), using depth zero if there is no such \(n\). This depth is finite and tends to infinity along \(\omega\): for each fixed \(n\), the finite intersection \(S_1\cap\cdots\cap S_n\cap\{k\ge n\}\) is large and has depth at least \(n\). Sampling each column at its depth therefore makes every demand's error tend to zero. The argument uses only finite intersections. It does not intersect countably many large sets.

There is a second kind of demand that must be retained without shrinking its parameter. Suppose that row \(n\), once \(n\) is large enough for a fixed label \(l\), satisfies an implication with a fixed positive threshold \(\delta_l\). Sampling rows at the same depth retains that implication on a large set of columns. A null input is eventually below \(\delta_l\); only after applying the implication may \(l\) increase. This order of quantifiers is what will preserve multiplier membership.

We now build the rows for this criterion. Adjoin \(M\) to \(P,Q\). The [countable-data construction](fast-reindexing-with-liftable-actions.md#2-countable-data-and-bounded-representatives) proves separability of both joins and of their intersections with the normal constant and centralizing subalgebras. In that construction a faithful-state GNS space has a countable dense set of rational words; its concrete predual is a quotient of trace class, with dense finite rational rank-one sums. The enlarged \(P\) remains \(H\)-invariant because semi-lifts preserve the constant copy of \(M\). At the end we restrict to the original domain.

Choose ultraweakly dense unital rational complex *-algebras \(\mathcal A\subset P\), \(\mathcal B\subset Q\), containing bounded strong* dense subsets of each constant and centralizing intersection. Include the countable \(H\)-orbits in \(\mathcal A\) before taking rational words. In particular every \(b_\gamma\) acts on \(\mathcal A\). Let \(\mathcal A_n,\mathcal B_n,H_n\) be increasing finite exhausting sets, and let \((\psi_j)\) be norm dense in \(M_*\). Every finite set contains the unit. When testing \(H_n\), also test its associated constant lifts; this adds only finitely many labels.

For each \(x\in\mathcal A\), choose a multiplier representative \(u_x\) with \(\sup_k\|u_x(k)\|\le\|x\|\). Choose \(v_a\) in the same way for \(a\in\mathcal B\). Use constant representatives on \(M\) and centralizing representatives on \(M_\omega\). The two instructions agree on their overlap: a constant representative of a quotient-centralizing element has constant normal-functional commutators with zero limit. Norm control follows by radial clipping inside the appropriate \(C^*\)-algebra: for \(C=\|x\|>0\), replace \(t\) by \(t f(t^*t)\), where \(f(s)=\min(1,C/\sqrt{s})\) and \(f(0)=1\). Its quotient image is still \(x\). Use zero when \(x=0\).

Fix one representing automorphism family for each actual \(\gamma\in H\), taking a constant family if that actual automorphism is a constant lift. For every \(x\), the multiplier criterion supplies fixed positive decreasing thresholds \(\delta_l(x)\) and large sets \(W_l(x)\) with
\[
k\in W_l(x),\quad \|z\|\le1,\quad \|z\|_\#<\delta_l(x)
\quad\Longrightarrow\quad
\|u_x(k)z\|_\#+\|zu_x(k)\|_\#<1/l.
\tag{3}
\]
These are the fixed-threshold demands of the transfer criterion.

For row \(n\), select one coordinate \(p(n)\ge n\). Its admissibility conditions have the following meanings.

| Data being retained | Required row test |
|---|---|
| Every fixed multiplier threshold already introduced | \(p(n)\in W_l(x)\) for \(x\in\mathcal A_n,\ l\le n\) |
| The rational *-algebra | All addition, adjoint and product discrepancies for operands in \(\mathcal A_n\), and scalar discrepancies for the first \(n\) rational complex scalars, have symmetric seminorm below \(1/n\) |
| Centralizing inputs | \(\Vert[u_x(p(n)),\psi_j]\Vert<1/n\) for \(x\in\mathcal A_n\cap M_\omega,\ j\le n\); also \(\Vert[u_x(p(n)),a]\Vert_\#<1/n\) for \(a\in\mathcal B_n\cap M\) |
| The inner part of the ordered expectation error | The test (4) below |
| The action of every constant lift in the finite action list | The test (5) below |

The two remaining row tests are
\[
|\psi_j(E_\omega(a)(u_x(p(n))-E_\omega(x)))|<1/n
\quad(x\in\mathcal A_n,\ a\in\mathcal B_n,\ j\le n)
\tag{4}
\]
and
\[
\|\beta(u_x(p(n)))-u_{b(x)}(p(n))\|_\#<1/n
\quad(x\in\mathcal A_n,\ b=\beta^\omega
\text{ in the finite action list}).
\tag{5}
\]
The coordinate of \(xy\), or of \(b(x)\), has been chosen even when that output is not in the finite operand set.

**Lemma 2.1.** This finite selection is possible.

**Proof.** Each row is a finite collection of tests on one coordinate. The algebraic defects and the defects in (5) represent zero in the quotient, so their seminorms tend to zero along \(\omega\). The functional commutators tend to zero by centralizing membership. Their strong* commutation with each fixed \(a\in M\) follows from the [centralizing estimate](central-sequences-and-free-group-factors.md#lemma-1-1), applied also to the adjoint. Finally the coefficient \(E_\omega(a)\) in (4) is fixed: ultraweak convergence of \(u_x(k)\) may be tested against the single normal functional \(y\mapsto\psi_j(E_\omega(a)y)\). Intersect these finitely many acceptable sets with the sets in (3) and with \(\{k\ge n\}\). The intersection is large, hence nonempty, and any member is a valid \(p(n)\). \(\square\)

Thus each row now consists of fixed operators \(u_x(p(n))\). The column tests may vary \(v_a(k)\) and \(\gamma_k\) while keeping these operators fixed.

<a id="3-the-second-selection-and-the-slow-index"></a>

## 3. Column tests and the depth function

For row \(n\), let \(S_n\) be the set of columns \(k\) satisfying all of
\[
\begin{aligned}
\|[u_x(p(n)),v_a(k)]\|_\#&<1/n
&&(x\in\mathcal A_n,\ a\in\mathcal B_n\cap M_\omega),\\
|\psi_j((v_a(k)-E_\omega(a))u_x(p(n)))|&<1/n
&&(x\in\mathcal A_n,\ a\in\mathcal B_n,\ j\le n),\\
\|\gamma_k(u_x(p(n)))-\beta_\gamma(u_x(p(n)))\|_\#&<1/n
&&(x\in\mathcal A_n,\ \gamma\in H_n).
\end{aligned}
\tag{6}
\]
Include the associated constant lifts in the finite action list. Put \(V_0=\mathbb N\) and \(V_n=S_1\cap\cdots\cap S_n\cap\{k\ge n\}\).

**Lemma 3.1.** Such sets exist, and they can be chosen with empty total intersection.

**Proof.** The first column error vanishes because the varying \(v_a(k)\) is centralizing and its other operand is fixed. The second vanishes by its ultraweak limit, again against a fixed coefficient. For the third, \(u\)-convergence of the chosen automorphism family implies strong* convergence on each fixed element.

To check that last implication without a uniform unit-ball assertion, write \(\alpha_k=\beta_\gamma^{-1}\gamma_k\). For fixed \(t\), expand
\[
\varphi((\alpha_k(t)-t)^*(\alpha_k(t)-t))
=\varphi(\alpha_k(t^*t))-\varphi(\alpha_k(t^*)t)
-\varphi(t^*\alpha_k(t))+\varphi(t^*t).
\]
Predual norm convergence gives the limit of the first term and ultraweak convergence gives both cross terms. The limit is zero. Repeat for \(t^*\); transport the resulting bounded strong* convergence by the fixed normal automorphism \(\beta_\gamma\). This proves the third error test for every one of the finitely many fixed operators in this row.

Consequently \(S_n\in\omega\), so each finite intersection \(V_n\) is large. The sequence is decreasing, and \(k\notin V_n\) for \(n>k\), proving empty total intersection. \(\square\)

The abstract depth construction is now exactly
\[
r(k)=\max\bigl(\{n\ge1:k\in V_n\}\cup\{0\}\bigr),
\qquad q(k)=p(r(k)),\qquad p(0)=1.
\tag{7}
\]
It has \(r(k)\le k\) and \(r(k)\to_\omega\infty\). On \(V_n\setminus V_{n+1}\) it samples the fixed row \(p(n)\). On the initial, non-large band \(V_0\setminus V_1\) it uses \(p(0)\). No rate comparison between \(q(k)\) and \(k\) is needed.

<a id="4-multiplier-membership-and-the-map"></a>

## 4. Transfer to the quotient

Apply the transfer criterion to
\[
w_x(k)=u_x(q(k)),\qquad \Phi_0(x)=\pi(w_x),
\quad x\in\mathcal A.
\tag{8}
\]
Before using \(\pi\), we must prove that its argument is a multiplier.

**Lemma 4.1.** Every \(w_x\) is a multiplier. If \(x\in\mathcal A\cap M_\omega\), it is centralizing along \(\omega\).

**Proof.** Fix a label \(l\) and any bounded null input sequence \(z_k\), chosen after \(q\) if desired. Divide by a common norm bound to make it contractive. On a large set of columns the depth is high enough to include \(x,l\), so \(q(k)\in W_l(x)\). On another large set \(\|z_k\|_\#<\delta_l(x)\). The retained implication (3) makes both product seminorms have ultralimit at most \(1/l\). The same products are considered for every \(l\), hence both ultralimits are zero. Rescaling proves both normalizer conditions for the original bounded input.

For centralizing \(x\), the retained row test gives \(\|[w_x(k),\psi_j]\|<1/r(k)\) once \(x,j\) have entered. For any \(\psi\in M_*\),
\[
\|[w_x(k),\psi]\|
\le\|[w_x(k),\psi_j]\|+2\|x\|\|\psi-\psi_j\|.
\]
Take the ultralimit and then approximate \(\psi\) in norm. This proves the asserted centralizing membership. \(\square\)

All subsequent conclusions follow by sending particular error arrays to zero. Rational algebraic defects were tested on the rows, so their sampled representatives are null. Thus \(\Phi_0\) is a unital rational *-homomorphism; its coordinate bound gives \(\|\Phi_0(x)\|\le\|x\|\). Constants are fixed because their representatives never vary.

The expectation array is the sum of one column error and one row error. With \(n=r(k)\), its exact decomposition is
\[
\begin{aligned}
v_a(k)w_x(k)-E_\omega(a)E_\omega(x)
={}&(v_a(k)-E_\omega(a))u_x(p(n))\\
&+E_\omega(a)(u_x(p(n))-E_\omega(x)).
\end{aligned}
\]
Equations (6) and (4) give
\[
|\psi_j(v_a(k)w_x(k)-E_\omega(a)E_\omega(x))|
<2/r(k)
\tag{9}
\]
at every sufficiently deep column. Norm density of the \(\psi_j\), together with the common operator bound for each fixed \(a,x\), extends the zero limit to every normal functional. Both factors in \(v_a w_x\) are multipliers. Their product's weak ultralimit therefore gives
\[
E_\omega(a\Phi_0(x))=E_\omega(a)E_\omega(x).
\tag{10}
\]
The order of the two factors has been retained throughout.

With \(a=1\), (10) preserves \(\rho\). Apply it to \(x^*x\) and \(xx^*\), using multiplicativity, to obtain
\[
\|\Phi_0(x)\|_{\rho,\#}^2
=\tfrac12\rho(x^*x+xx^*)=\|x\|_{\rho,\#}^2.
\]
This state isometry belongs to the constructed map and does not require any element of \(H\) to preserve \(\rho\).

The commutation array in the first line of (6) vanishes for every \(x\) and centralizing \(a\). Lemma 4.1 separately controls centralizing inputs. These are distinct outputs of the criterion: the first controls the full image, the second the image of an intersection.

There are also two distinct action arrays. The column array uses the actual outer automorphism, yielding
\[
\gamma\Phi_0(x)=b_\gamma\Phi_0(x).
\tag{11}
\]
The row array (5) compares the two representatives at the same inner coordinate and yields
\[
b_\gamma\Phi_0(x)=\Phi_0(b_\gamma(x)).
\tag{12}
\]
In (11) it is \(\gamma_k\) that acts on \(u_x(q(k))\). Replacing it by \(\gamma_{q(k)}\) would change the automorphism being applied.

<a id="5-normal-extension-and-an-explicit-example"></a>

## 5. Normal extension and the two action identities

The dense-algebra construction is now complete. Its normal extension uses the [faithful-state extension lemma](fast-reindexing-with-liftable-actions.md#lemma-5-1) at precisely its bounded strong* scope. First the norm bound extends the rational map to the complex \(C^*\)-completion of \(\mathcal A\). For any bounded strong* approximating net in that completion, the exact symmetric state isometry makes the image strong*-Cauchy. The lemma's cyclic separating vector and dense commutant orbit produce a bounded operator limit, independent of the approximating net. Bounded products and adjoints pass to that limit. Faithfulness of the preserved state proves injectivity.

For clarity, normality uses increasing nets, not just sequences: if \(0\le x_i\uparrow x\), let \(y=\sup_i\Phi(x_i)\le\Phi(x)\). State preservation and normality of \(\rho\) give \(\rho(\Phi(x)-y)=0\). Faithfulness gives \(y=\Phi(x)\). The complete order-normal-functional/predual argument in the same premise then proves normality against every normal functional. Thus we obtain the normal unital embedding \(\Phi:P\to M^\omega\).

Each output array has its own extension step. Constants are fixed by bounded strong* density in the constant intersection. The centralizing intersection maps into \(M_\omega\) because that subalgebra is normally embedded and closed under bounded strong* limits. For a dense \(x\), (6) gives commutation with the dense algebra in \(Q\cap M_\omega\); separate ultraweak continuity extends it to that whole subalgebra. Its relative commutant is strongly closed, so bounded strong* approximation then gives the assertion for every \(x\in P\).

For fixed \(a\in\mathcal B\), both sides of (10) are normal linear functions of \(x\); extend first in \(x\). For each resulting fixed \(x\), both sides are normal linear functions of \(a\); extend next in \(a\). This proves the full ordered expectation identity.

Finally \(\gamma\Phi\), \(b_\gamma\Phi\), and \(\Phi b_\gamma\) are normal maps on the same invariant domain. Equations (11) and (12) identify their dense-algebra values, so they agree everywhere. They compare the action on the output with the constant-lift action on the input. They do not assert an identity with \(\Phi\gamma\). Restricting from the joined algebras to the original \(P,Q\) proves every clause of Theorem 1.1.

The [Pauli example](ultraproduct-expectations-and-semilift-ambiguity.md#proposition-5-1) shows why the action condition matters. In \(R=\bigotimes_{k\ge1}(M_2,\operatorname{tr}_2)\), let \(X,Z\in R_\omega\) come from Pauli operators in leg \(k\), and let \(\gamma=\operatorname{Ad}(Z)\). Then \(\beta_\gamma=\mathrm{id}\). For \(P=Q=M_2(X,Z)\), replace leg \(k\) by leg \(\lfloor\sqrt k\rfloor\) in the representatives of its matrix generators. Their matrix relations remain exact, giving an injective map of \(P\). The new leg tends to infinity, so the images remain centralizing. For all sufficiently large \(k\), it differs from leg \(k\), so the image commutes with \(Q\) and is fixed by \(\gamma\). Thus
\[
\gamma\Phi(X)=\Phi(X)=\Phi(b_\gamma(X)),
\qquad
\Phi(\gamma(X))=-\Phi(X).
\tag{13}
\]
This supplies the slow compatibility and exhibits the failure of the stronger equivariance condition in the same example.

One can also check the expectation clause directly in this example. Put \(m(k)=\lfloor\sqrt{k}\rfloor\), and let \(X_{m(k)},Z_{m(k)}\) be the two Pauli matrices in that leg. They satisfy \(X_{m(k)}^2=Z_{m(k)}^2=1\), are self-adjoint, and anticommute. The projections \((1\pm Z_{m(k)})/2\) have trace one half; together with the off-diagonal units obtained from \(X_{m(k)}\) they give nonzero matrix units. Thus the quotient copy is a faithful unital \(M_2\) copy.

For each fixed tensor head, the new leg is eventually outside it. To extend its commutation to every normal functional, approximate that functional in norm by finite-head coefficient functionals, using the full tensor-predual density proof in the expectation lesson. Its commutator with any one such coefficient eventually vanishes; the error is bounded by twice the uniform operator bound times the functional approximation error. Hence the representatives are centralizing. For an element of this finite-dimensional matrix copy, the weak limit is its normalized matrix trace times one: pair first against finite-head coefficients, where tensor independence is exact, then use the same norm approximation. At distinct legs the same calculation gives, for \(a\in Q\) and \(x\in P\),
\[
E_\omega(a\Phi(x))=\operatorname{tr}_2(a)\operatorname{tr}_2(x)1
=E_\omega(a)E_\omega(x).
\]
The traces here use the evident two matrix-copy identifications. The state is preserved and the map is automatically normal on its finite-dimensional domain. Its constant intersection is scalar, so that clause is fixed as well. Conjugation by the old-leg \(Z_k\) fixes the new leg for \(k\ge3\), while it sends the old-leg \(X_k\) to \(-X_k\). Since the new \(X\) has square one, (13) is a nonzero, exact distinction.

## 6. Exercises with complete solutions

**Exercise 1.** Why is \(\beta_\gamma\) unique even though a convergent limit does not determine its semi-lift?

*Solution.* The chosen family acts as its limit on every constant \(a\in M\). Hence \(\beta_\gamma(a)=\gamma(a)\). An actual \(\gamma\) fixes that restriction, so every family representing it has the same limit. The reverse implication fails: different semi-lifts can have that same restriction.

**Exercise 2.** What purpose does the hypothesis \(b_\gamma\in H\) serve?

*Solution.* It ensures \(b_\gamma(P)=P\), so \(\Phi(b_\gamma(x))\) is defined. It also allows a countable algebra invariant under all those constant lifts and their finite equivariance tests. Invariance under \(\gamma\) alone would not imply invariance under its different constant lift.

**Exercise 3.** Explain why the first weak-limit test uses \(E_\omega(a)\) rather than \(v_a(k)\).

*Solution.* The first selection varies the inner index while fixing \(n\). The coefficient \(E_\omega(a)\) is an operator of \(M\) independent of that index, so ultraweak convergence of \(u_x\) gives (4). After \(p(n)\) is fixed, the second selection varies the outer coordinate and replaces \(v_a(k)\) by that expectation, yielding the second error in (9).

**Exercise 4.** Why does the second commutator test apply to every \(x\), rather than only centralizing \(x\)?

*Solution.* Its varying sequence is \(v_a(k)\), with \(a\in Q\cap M_\omega\). That sequence is centralizing and therefore commutes strong* with each fixed \(u_x(p(n))\), regardless of whether \(x\) is centralizing. This gives commutation of the full image with the centralizing part of \(Q\).

**Exercise 5.** Verify that every coordinate has a finite level in (7).

*Solution.* Membership in \(V_n\) implies \(k\ge n\), so only the finitely many levels \(n\le k\) are possible. Nestedness makes those levels an initial segment. If it is empty use level zero; otherwise its last member is the required maximum.

**Exercise 6.** Why is \(r(k)\to_\omega\infty\) sufficient for the quotient conclusions?

*Solution.* For each threshold \(n\), the \(\omega\)-large set \(V_n\) has \(r(k)\ge n\). Thus every fixed datum is tested on an \(\omega\)-large set with arbitrarily small error. Ordinary convergence of \(r(k)\) is unnecessary for an ultrafilter quotient.

**Exercise 7.** Derive multiplier membership from the fixed moduli.

*Solution.* Fix \(x,l\). On a large set the chosen inner index lies in \(W_l(x)\); then every small contraction input is controlled by the same \(\delta_l(x)\). A null sequence of inputs satisfies that modulus on another large set. Both product seminorms have ultralimit at most \(1/l\). Letting \(l\) increase proves both ideal-preservation conditions.

**Exercise 8.** Why is it wrong to evaluate the semi-lift at the selected index \(q(k)\) when acting on the final representative?

*Solution.* Formula (1) applies \(\gamma_k\) to the coordinate actually indexed by \(k\). Its input happens to be \(u_x(q(k))\), but that does not change the automorphism index. The slow selection first fixes this input, then makes \(\gamma_k\) close to its limit on it. Replacing \(k\) by \(q(k)\) would describe a different family action.

**Exercise 9.** Prove injectivity without requiring the automorphisms of \(H\) to preserve \(\varphi^\omega\).

*Solution.* Equation (10) with \(a=1\) makes \(\Phi\) preserve \(\varphi^\omega\), independently of any action. If \(\Phi(x)=0\), multiplicativity gives \(\varphi^\omega(x^*x)=\varphi^\omega(\Phi(x)^*\Phi(x))=0\). Faithfulness makes \(x=0\). No state invariance of the automorphisms enters.

**Exercise 10.** Explain the normal extension of the commutation conclusion.

*Solution.* Each dense input image commutes with the dense \*-algebra in \(Q\cap M_\omega\), hence with its von Neumann closure by separate ultraweak continuity. The relative commutant of that closure is strongly closed. Bounded strong\* approximation of a general input and the normal extension therefore keep its image in that commutant.

**Exercise 11.** Check the Pauli slow-index example.

*Solution.* The indices \(k\) and \(\lfloor\sqrt k\rfloor\) are distinct for \(k\ge3\). Operators in distinct tensor legs commute. The reindexed Pauli pair still anticommutes within its single new leg, so its unital \(M_2\) relations persist. Since the new leg tends to infinity, all finite-head commutators eventually vanish; trace approximation gives centralizing sequences. These facts prove every assertion in (13).

**Exercise 12.** Recover scalar independence for a factor when the input \(x\) is centralizing.

*Solution.* Then \(E_\omega(x)=\tau_\omega(x)1\). Applying \(\varphi\) to (2) gives \(\varphi^\omega(a\Phi(x))=\varphi^\omega(a)\tau_\omega(x)\). If \(a\) is centralizing too, this is the trace identity on \(M_\omega\). The full expectation identity retains the ordered product for general \(x\).

## References

The slow-reindexing method and its five conclusion clauses are due to Adrian Ocneanu, [*Actions of discrete amenable groups on factors*](https://wrap.warwick.ac.uk/id/eprint/110062/1/WRAP_Theses_Ocneanu_1982.pdf), thesis, Chapter 5, Section 5.4, printed pp.55–56 (PDF pp.69–70). The statement includes the associated constant lifts, and the proof selects inner coordinates and then outer neighborhoods. It refers the remaining extension argument to the preceding fast lemma.

The finite-error transfer criterion separates that classical selection mechanism from the quotient: vanishing row and column errors transfer by a depth function, whereas multiplier thresholds remain fixed until a later null input has been tested. The complete multiplier and faithful-state extension proofs are supplied by the linked programme lessons. The ordered expectation is \(M\)-valued, and the Pauli tensor-tail model distinguishes output compatibility from equivariance with the original semi-lift. These arguments use a faithful normal state and separable predual without a factor or trace assumption.
