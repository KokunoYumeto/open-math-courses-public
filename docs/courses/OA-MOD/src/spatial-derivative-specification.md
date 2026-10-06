# Spatial comparison on an arbitrary representation

A spatial derivative compares a weight on an algebra with a weight on its commutant. The resulting operator acts on the given representation space. Its existence is an analytic assertion: a formula for finite energies must first be shown to have a dense domain and a closable form. This unit proves the bounded-vector and coefficient calculations needed for that assertion. The direct construction is now supplied by Constructing spatial energy from finite observations; the contracts below distinguish its proved consequences from the remaining modular and reconstruction assertions.

The construction in OA-MOD-SD-07, the support equality in OA-MOD-SD-08, and the order and invertible-transport assertions in OA-MOD-SD-09 have proofs in OA-MOD-SC relative to its stated prerequisites. The full spatial sum theorem and its joint core supplies finite addition, and Increasing weights, finite energy and resolvents supplies the increasing-weight form, resolvent and spectral-power assertions. Spatial energy and modular time supplies the relative closed graph, modular identification, reciprocity, faithful cocycle formula and predual topology of the increasing-weight modular automorphisms. Recovering a weight from spatial energy supplies the corrected all-energy reconstruction criterion and covariance characterization, using the converse cocycle theorem Reconstructing a weight from a modular cocycle. The elementary results in OA-MOD-SD-02 through OA-MOD-SD-06 have complete proofs relative to the stated foundation contracts. Those foundation contracts are not proved here. No separability, sigma-finiteness, cyclic vector, or finite-weight assumption is imposed unless expressly stated.

Mathematical antecedents: M. Takesaki, *Theory of Operator Algebras II* (2003), Chapter IX, Section 3, pp. 186–198, in particular Lemma 3.3, Theorem 3.8, Lemma 3.9, Proposition 3.10, Theorem 3.11, Lemma 3.12 and Corollary 3.13. The present organization uses a direct commutant-GNS convention. These references identify antecedents; their prose and proofs are not imported.

## Spaces, weights and dependency contracts

Fix a concrete unital von Neumann algebra \(M\subseteq B(H)\), with commutant \(M'\). The Hilbert space \(H\) is arbitrary. Fix a **normal semifinite faithful** weight \(\psi'\) on \(M'\). A numerator \(\varphi\), when present, is **normal and semifinite** on \(M\); it need not be faithful.

Inner products are linear in the first variable. Use the semicyclic triple

\[
(H_{\psi'},\pi_{\psi'},\Lambda_{\psi'}),\qquad
\mathfrak n_{\psi'}=\{x'\in M':\psi'(x'^*x')<\infty\}.
\]

Thus \(\Lambda_{\psi'}\) maps the finite left ideal into its Hilbert completion, and

\[
\pi_{\psi'}(y')\Lambda_{\psi'}(x')
=\Lambda_{\psi'}(y'x'),\qquad
\|\Lambda_{\psi'}(x')\|^2=\psi'(x'^*x').
\]

The following are exact dependencies.

* **SD-DEP-GNS:** Domain algebra and its positive cone through Faithfulness and the finite-weight specialization, for finite ideals, the linear extension of a weight, the semicyclic triple, its normal representation and semifinite cutoffs.
* **SD-DEP-BOUNDED:** arbitrary Hilbert-space completions, bounded adjoints, positivity, continuous functional calculus, and the bicommutant theorem.
* **SD-DEP-FORM:** A form includes its domain through Logarithms and imaginary powers, especially the exact representation of a densely defined closed positive form and the finite-energy condition for monotone limits; and The completion test and canonical closure through When a form sum equals an operator sum, for the closability completion test, lower semicontinuity, exact cores, the converse form-order theorem and the operator/form-sum comparison. Their arbitrary-dimensional spectral calculus is provided by Bounded Borel functions and the spectral measure through Convergence and cutoffs, relative to its exact scalar, Hilbert-space and bounded-calculus inputs. Finite energy and its Hilbert-space closure through Completion gives the exact core and energy formula verify density, closability and the exact core for the particular spatial form, using the earlier coefficient results of this unit.
* **SD-DEP-SUPPORT:** for a normal semifinite weight, its support \(p=s(\varphi)\in M\), the identity \(\varphi(x)=\varphi(pxp)\) for \(x\in M_+\), and the faithful normal semifinite restriction to \(pMp\). This contract is proved in The faithful semifinite support corner, relative to its WG/BK bounded-operator prerequisites, whose foundations are not proved here.
* **SD-DEP-STANDARD:** The positive cone of a standard representation constructs the natural cone, its positive-functional vectors and the weight standard form; Recovering a representation from its positive cone proves the supported corner and abstract comparison theorems. Both rely on their stated prerequisites. The complete weight-Hilbert-algebra correspondence is supplied by Completing the two multiplication domains through Fullness and recovery of the original weight; it alone does not prove the cone results. SI-11 proves the opposite-module dictionary below using the actual modular conjugation and transported GNS graphs, without a natural-cone premise.
* **SD-DEP-RELATIVE:** Every finite rectangular intertwiner has a vector through Ordinary relative GNS maps are a specialization supplies the finite rectangular inverse correspondence, linking weight, closed relative map, full graph core, support reduction and polar factor. The nonfaithful zero part and the distinct source and target spaces are retained. The inputs of these proofs are not proved here.
* **SD-DEP-MODULAR:** The modular fundamental theorem supplies the modular automorphism group for a faithful normal semifinite weight, its sigma-strong* continuity, finite-domain covariance and invariance of the whole weight. The KMS boundary condition determines the modular group supplies the KMS characterization and uniqueness at its stated analytic inputs. SI-08 through SI-09 separately identifies spatial powers with the numerator and negative-time commutant actions; MF alone does not provide that identification.
* **SD-DEP-COCYCLE:** SI-14 supplies the reference-independent balanced-matrix cocycle, with the convention \([D\varphi_2:D\varphi_1]_t\). Existence, uniqueness and the prescribed cocycle supplies the converse for arbitrary strongly continuous unitary cocycles of an NSF weight. SX-07 applies it on the actual support corner in the characterization below. That application retains the converse as a substantive prerequisite; it is not an independent shortcut that proves it.

The bounded-vector proofs below use only SD-DEP-GNS and SD-DEP-BOUNDED. They do not assume SD-DEP-STANDARD or any spatial derivative already exists. References to OA-MOD-SC record downstream proofs of later contracts: SC uses SD-02, SD-04 and SD-05, while those three proofs have no SC premise. The direct construction does not use SD-DEP-STANDARD or SD-DEP-RELATIVE; those contracts govern the separate convention dictionary and relative modular identification.

## Which vectors define bounded intertwiners?

Define

\[
\begin{aligned}
\mathcal D_{\psi'}(H)=\{\xi\in H:\ &\text{there is }C\geq0\text{ such that}\\
&\|x'\xi\|\leq C\,\psi'(x'^*x')^{1/2}
\quad(x'\in\mathfrak n_{\psi'})\}.
\end{aligned}
\]

For \(\xi\) in this set, define on \(\Lambda_{\psi'}(\mathfrak n_{\psi'})\)

\[
R_{\psi'}(\xi)\Lambda_{\psi'}(x')=x'\xi.
\]

**Proposition.** This formula extends uniquely to a bounded linear map

\[
R_{\psi'}(\xi):H_{\psi'}\longrightarrow H.
\]

Its norm is the least permissible \(C\). The space \(\mathcal D_{\psi'}(H)\) is linear, \(\xi\mapsto R_{\psi'}(\xi)\) is linear and injective, and

\[
R_{\psi'}(\xi)\pi_{\psi'}(y')=y'R_{\psi'}(\xi)
\quad(y'\in M').
\]

For \(a\in M\), the vector \(a\xi\) belongs to \(\mathcal D_{\psi'}(H)\), and

\[
R_{\psi'}(a\xi)=aR_{\psi'}(\xi),\qquad
\|R_{\psi'}(a\xi)\|\leq\|a\|\,\|R_{\psi'}(\xi)\|.
\]

**Proof.** The defining estimate says exactly that the displayed rule is bounded for the GNS norm. If two representatives have the same GNS vector, their difference has GNS norm zero, so the estimate makes their images equal. The rule is therefore well-defined, and extension from a dense subspace proves existence, uniqueness and the norm assertion. The triangle inequality proves linearity of the bounded-vector domain, and uniqueness of bounded extension proves linearity of \(R_{\psi'}\).

For \(x'\in\mathfrak n_{\psi'}\) and \(y'\in M'\), the left-ideal property gives \(y'x'\in\mathfrak n_{\psi'}\). On the dense GNS domain,

\[
R_{\psi'}(\xi)\pi_{\psi'}(y')\Lambda_{\psi'}(x')
=y'x'\xi
=y'R_{\psi'}(\xi)\Lambda_{\psi'}(x').
\]

Both sides are bounded operators, proving the intertwining identity. If \(a\in M\), then \(x'a\xi=ax'\xi\), so the defining estimate holds for \(a\xi\) with constant \(\|a\|\|R_{\psi'}(\xi)\|\). The same dense-domain computation proves the formula for \(R_{\psi'}(a\xi)\).

Finally, suppose \(R_{\psi'}(\xi)=0\). The finite positive contractions \(e_i'\) supplied by OA-MOD-WG-008 converge strongly to \(1\). They belong to \(\mathfrak n_{\psi'}\), because \((e_i')^2\leq e_i'\) and \(\psi'(e_i')<\infty\). Hence

\[
e_i'\xi=R_{\psi'}(\xi)\Lambda_{\psi'}(e_i')=0.
\]

Strong convergence gives \(\xi=0\). \(\square\)

This proposition does **not** prove that \(\mathcal D_{\psi'}(H)\) is dense in \(H\). The finite cutoffs act on a bounded vector to detect it; the argument does not show that applying a cutoff to an arbitrary vector makes that vector bounded.

## A useful complete norm on the bounded vectors

**Proposition.** The formula

\[
\|\xi\|_{\mathrm b}
=\bigl(\|\xi\|^2+\|R_{\psi'}(\xi)\|^2\bigr)^{1/2}
\]

makes \(\mathcal D_{\psi'}(H)\) a Banach space. For \(a\in M\), multiplication by \(a\) has norm at most \(\|a\|\) on this space.

**Proof.** This is the norm induced by the linear graph embedding

\[
\xi\longmapsto (\xi,R_{\psi'}(\xi))
\in H\oplus B(H_{\psi'},H),
\]

where the direct sum has the square-sum Banach norm. Let \((\xi_n)\) be Cauchy in that norm. There are \(\xi\in H\) and \(T\in B(H_{\psi'},H)\) with \(\xi_n\to\xi\) in Hilbert norm and \(R_{\psi'}(\xi_n)\to T\) in operator norm. For every \(x'\in\mathfrak n_{\psi'}\),

\[
T\Lambda_{\psi'}(x')
=\lim_n x'\xi_n=x'\xi.
\]

Thus \(\xi\) satisfies the bounded-vector estimate with constant \(\|T\|\), and uniqueness gives \(R_{\psi'}(\xi)=T\). The graph is closed, proving completeness. The multiplication estimate follows by applying the two bounds in OA-MOD-SD-02 to the two terms of the norm. \(\square\)

Completeness here concerns the bounded-vector norm, not the Hilbert norm. It gives no assertion that this domain is Hilbert-norm closed or dense.

## Coefficients, matrices and the coefficient ideal

For bounded vectors define

\[
\theta_{\psi'}(\xi,\eta)
=R_{\psi'}(\xi)R_{\psi'}(\eta)^*\in B(H).
\]

**Proposition.** These coefficients belong to \(M\), are linear in \(\xi\) and conjugate-linear in \(\eta\), and satisfy

\[
\begin{gathered}
\theta(\xi,\eta)^*=\theta(\eta,\xi),\qquad
\theta(a\xi,b\eta)=a\theta(\xi,\eta)b^*,\\
\theta(\xi,\xi)\geq0,\qquad
\|\theta(\xi,\eta)\|\leq\|R(\xi)\|\,\|R(\eta)\|.
\end{gathered}
\]

For every finite family \(\xi_1,\ldots,\xi_n\), the matrix

\[
[\theta(\xi_i,\xi_j)]_{i,j=1}^n
\]

is positive in \(M_n(M)\). Consequently

\[
\mathcal J_{\psi'}=
\operatorname{span}\{\theta(\xi,\eta):\xi,\eta\in\mathcal D_{\psi'}(H)\}
\]

is an algebraic two-sided *-ideal of \(M\), and its positive cone is exactly

\[
\mathcal J_{\psi'}\cap M_+
=\left\{\sum_{j=1}^n\theta(\xi_j,\xi_j):
n\geq1,\ \xi_j\in\mathcal D_{\psi'}(H)\right\}.
\]

The zero operator is included by taking a zero vector.

**Proof.** Taking adjoints of the intertwining formula with \(y'^*\) gives

\[
\pi_{\psi'}(y')R(\eta)^*=R(\eta)^*y'.
\]

Therefore \(y'R(\xi)R(\eta)^*=R(\xi)R(\eta)^*y'\) for every \(y'\in M'\), and the bicommutant theorem puts the coefficient in \(M\). All scalar, adjoint and covariance identities follow from the corresponding identities for \(R\).

For \(v_1,\ldots,v_n\in H\),

\[
\sum_{i,j}\langle\theta(\xi_i,\xi_j)v_j,v_i\rangle
=\left\|\sum_j R(\xi_j)^*v_j\right\|^2\geq0.
\]

This proves matrix positivity. Covariance under \(a,b\in M\) and the adjoint identity make \(\mathcal J_{\psi'}\) a two-sided *-ideal.

It remains to prove the assertion about its positive cone; polarization alone does not prove positivity of the coefficients in a chosen linear expansion. Let \(z\in\mathcal J_{\psi'}\cap M_+\). Absorb scalar coefficients into the first vectors and write \(z=\sum_{j=1}^n\theta(\xi_j,\eta_j)\). Since \(z=z^*\), positivity of \(\theta(\xi_j-\eta_j,\xi_j-\eta_j)\) gives

\[
0\leq z\leq
P:=\frac12\sum_{j=1}^n
\bigl(\theta(\xi_j,\xi_j)+\theta(\eta_j,\eta_j)\bigr).
\]

Define a contraction on \(\operatorname{ran}P^{1/2}\) by

\[
T(P^{1/2}v)=z^{1/2}v.
\]

The inequality \(z\leq P\) proves that this is well-defined and contractive. Extend it continuously to \(\overline{\operatorname{ran}P}\) and set it to zero on \(\ker P\). For every unitary \(u'\in M'\), both \(P^{1/2}\) and \(z^{1/2}\) commute with \(u'\). On \(\operatorname{ran}P^{1/2}\), this implies \(Tu'=u'T\); the range closure and kernel of \(P\) are also \(u'\)-invariant. Thus the identity holds on all of \(H\). Every element of \(M'\) is a linear combination of unitaries, so \(T\in M\).

We have \(TP^{1/2}=z^{1/2}\), hence \(TPT^*=z\). Substituting the definition of \(P\) and using covariance gives

\[
z=\sum_{j=1}^n
\left[
\theta\left(\frac{T\xi_j}{\sqrt2},\frac{T\xi_j}{\sqrt2}\right)
+\theta\left(\frac{T\eta_j}{\sqrt2},\frac{T\eta_j}{\sqrt2}\right)
\right].
\]

All new vectors are bounded by OA-MOD-SD-02. This proves the nontrivial inclusion; the other inclusion follows from positivity. \(\square\)

The proof has not asserted ultraweak density of \(\mathcal J_{\psi'}\). A coefficient ideal with an explicit approximate identity proves that density and supplies increasing positive approximants, using this algebraic ideal result.

## The energy formula before closure

Let \(\varphi\) be the numerator weight. Define the finite initial domain

\[
\mathcal E_{\varphi,\psi'}
=\{\xi\in\mathcal D_{\psi'}(H):
\varphi(\theta_{\psi'}(\xi,\xi))<\infty\}.
\]

**Proposition.** This is a linear subspace. For \(\xi,\eta\) in it, \(\theta_{\psi'}(\xi,\eta)\) belongs to \(\mathfrak m_\varphi\), and

\[
q_0(\xi,\eta)
=\widetilde\varphi(\theta_{\psi'}(\xi,\eta))
\]

is a nonnegative sesquilinear form, with

\[
q_0[\xi]=\varphi(\theta_{\psi'}(\xi,\xi)).
\]

Here \(\widetilde\varphi\) is the finite linear extension proved in OA-MOD-WG-004. No infinite subtraction occurs.

**Proof.** Expanding the positive operator \((R(\xi)-R(\eta))(R(\xi)-R(\eta))^*\) gives

\[
\theta(\xi+\eta,\xi+\eta)
\leq2\theta(\xi,\xi)+2\theta(\eta,\eta).
\]

Monotonicity and additivity of the weight prove closure of the finite domain under sums; scalar closure follows from homogeneity. Polarization, with the first-variable-linear convention, gives

\[
\theta(\xi,\eta)
=\frac14\sum_{k=0}^3 i^k
\theta(\xi+i^k\eta,\xi+i^k\eta).
\]

Every diagonal on the right is finite for \(\varphi\). It therefore belongs to the finite positive cone of \(\mathfrak m_\varphi\). Its linear span is \(\mathfrak m_\varphi\), proving membership of the cross coefficient. Composing its sesquilinearity with the linear extension of \(\varphi\) proves sesquilinearity of \(q_0\); the diagonal is visibly nonnegative. \(\square\)

The preceding algebraic argument alone does not prove density of \(\mathcal E_{\varphi,\psi'}\), closability of \(q_0\), or completeness in its form norm. Finite energy and its Hilbert-space closure through Completion gives the exact core and energy formula prove density and closability and construct the closed completion. The representation theorem applies to that completion; the initial form need not itself be closed.

Although \(\mathcal D_{\psi'}(H)\) is invariant under \(M\), no such invariance of \(\mathcal E_{\varphi,\psi'}\) is asserted. A general weight does not satisfy \(\varphi(a z a^*)\leq\|a\|^2\varphi(z)\).

## A conditional density consequence and a null-support check

**Lemma.** If \(\mathcal D_{\psi'}(H)\) is dense in \(H\), then the coefficient ideal acts nondegenerately: a vector \(v\) annihilated by every member of \(\mathcal J_{\psi'}\) is zero.

**Proof.** For each bounded \(\xi\), the assumption \(\theta(\xi,\xi)v=0\) gives

\[
\|R(\xi)^*v\|^2
=\langle\theta(\xi,\xi)v,v\rangle=0.
\]

Hence \(v\) is orthogonal to \(R(\xi)\Lambda_{\psi'}(e_i')=e_i'\xi\), where \(e_i'\) are the finite cutoffs used in OA-MOD-SD-02. Passing to their strong limit shows \(v\perp\xi\). Density of the bounded vectors yields \(v=0\). \(\square\)

One possible route from nondegeneracy to ultraweak density would use the separate foundation fact that an ultraweakly closed two-sided ideal of a von Neumann algebra has the form \(Mz\) for a central projection \(z\). The direct proof in A coefficient ideal with an explicit approximate identity supplies an increasing positive approximate identity using bounded functional calculus and the density proved in SC-03. Thus this construction has no prerequisite requiring classification of closed ideals.

**Support check, conditional on SD-DEP-SUPPORT.** Put \(p=s(\varphi)\). For \(\xi\in\mathcal D_{\psi'}(H)\), the vector \((1-p)\xi\) lies in \(\mathcal E_{\varphi,\psi'}\) and has zero energy.

**Proof.** Covariance of the coefficient gives

\[
\theta((1-p)\xi,(1-p)\xi)
=(1-p)\theta(\xi,\xi)(1-p).
\]

Compressing this positive operator by \(p\) gives zero. The support identity for \(\varphi\) therefore gives weight zero. \(\square\)

This proves one elementary part of the kernel computation. The exclusion of additional null directions is proved separately in All and only the null directions survive at zero energy through The representing operator and its domains.

## The full spatial construction contract

**Construction theorem; proof supplied by OA-MOD-SC relative to its stated prerequisites.** With exactly the hypotheses of OA-MOD-SD-01, the following assertions hold.

1. \(\mathcal D_{\psi'}(H)\) is dense in \(H\), and \(\mathcal J_{\psi'}\) is ultraweakly dense in \(M\).
2. \(\mathcal E_{\varphi,\psi'}\) is dense in \(H\). The form \(q_0\) of OA-MOD-SD-05 is closable. Explicitly, if \(\xi_n\in\mathcal E_{\varphi,\psi'}\), \(\xi_n\to0\) in \(H\), and \(q_0[\xi_n-\xi_m]\to0\) as \(n,m\to\infty\), then \(q_0[\xi_n]\to0\). Write \(\overline q_0\) for its closed form extension obtained by completion in the form norm, whose injection into \(H\) is then justified by OA-MOD-FC-02.
3. There is a unique nonnegative self-adjoint operator \(A\) on \(H\) with

\[
\begin{gathered}
D(A^{1/2})=D(\overline q_0),\\
\overline q_0(\xi,\eta)
=\langle A^{1/2}\xi,A^{1/2}\eta\rangle.
\end{gathered}
\]

4. The initial domain is exactly

\[
\mathcal E_{\varphi,\psi'}
=\mathcal D_{\psi'}(H)\cap D(A^{1/2}),
\]

and it is a core for \(A^{1/2}\): for every \(\xi\in D(A^{1/2})\), a sequence \(\xi_n\in\mathcal E_{\varphi,\psi'}\) satisfies \(\xi_n\to\xi\) and \(A^{1/2}\xi_n\to A^{1/2}\xi\) in Hilbert norm. This is a graph-norm sequence, not a separability assumption on \(H\).
5. Equivalently, for every \(\xi\in\mathcal D_{\psi'}(H)\),

\[
\varphi(\theta_{\psi'}(\xi,\xi))
=\begin{cases}
\|A^{1/2}\xi\|^2,&\xi\in D(A^{1/2}),\\
+\infty,&\xi\notin D(A^{1/2}).
\end{cases}
\]

The operator is denoted \(A=d\varphi/d\psi'\). Its operator domain, distinguished from its square-root domain, is

\[
D(A)=\{\xi\in D(\overline q_0):
\text{there is }\zeta\in H\text{ with }
\overline q_0(\xi,\eta)=\langle\zeta,\eta\rangle
\text{ for all }\eta\in D(\overline q_0)\},
\]

and then \(A\xi=\zeta\). This last description follows from SD-DEP-FORM once the preceding spatial assertions have been established.

The exact closure of bounded vectors through A coefficient ideal with an explicit approximate identity prove assertion 1. Finite energy and its Hilbert-space closure through Completion gives the exact core and energy formula prove assertion 2 and the exact core and energy identities in assertions 4 and 5. The representing operator and its domains supplies assertion 3 and the operator-domain description using the form representation theorem. These direct proofs use normal positive functionals and form completion. The relative map has exactly the coefficient form separately identifies the resulting operator with the positive square of the rectangular closed relative map by proving equality of their whole graph completions. That identification is downstream of these construction assertions.

**Conditional convention dictionary.** Assume the standard-form part of SD-DEP-STANDARD. Put \(N=(M')^{\mathrm{op}}\), denote the element corresponding to \(y'\in M'\) by \(n=(y')^{\mathrm{op}}\), and transport the weight by \(\psi(n)=\psi'(y')\) on positive elements. Give \(H\) the right \(N\)-action \(\xi n=y'\xi\). Let \(J_\psi\) be the standard conjugation on \(H_\psi\). There is a unitary

\[
W:H_{\psi'}\longrightarrow H_\psi,\qquad
W\Lambda_{\psi'}(y')=J_\psi\Lambda_\psi(n^*)
\quad(y'\in\mathfrak n_{\psi'}).
\]

To prove this, observe that \(y'\in\mathfrak n_{\psi'}\) is equivalent to \(n^*\in\mathfrak n_\psi\), since \((nn^*)\) corresponds to \(y'^*y'\). The rule is linear: the adjoint and \(J_\psi\) each reverse scalar conjugation. Its norm is

\[
\|J_\psi\Lambda_\psi(n^*)\|^2
=\psi(nn^*)=\psi'(y'^*y').
\]

The range contains \(J_\psi\Lambda_\psi(\mathfrak n_\psi)\), a dense subspace. Extension therefore gives the claimed unitary. In the module convention, \(L_\psi(\xi)\) is the bounded extension of

\[
L_\psi(\xi)J_\psi\Lambda_\psi(n^*)=\xi n.
\]

The two bounded-vector estimates are equivalent through \(W\), and the defining formulas give

\[
R_{\psi'}(\xi)=L_\psi(\xi)W,
\qquad
\theta_{\psi'}(\xi,\eta)=L_\psi(\xi)L_\psi(\eta)^*.
\]

This proves the displayed dictionary from the modular conjugation. SI-11 additionally transports its full linking GNS map and relative graph, and SI-04 proves the inverse finite rectangular correspondence. The analytic right-action formula for entire elements is supplied by CX-03. Extension to every element of the source's closed complex-time domains remains the distinct obligation in SD-OPEN-03.

## Support, modular time and change of numerator

**Support, modular actions, reciprocity and faithful cocycle supplied at their stated prerequisites.** The support equality is supplied by All and only the null directions survive at zero energy through The representing operator and its domains. SI-08 through SI-10 supplies the supported modular actions, SI-13 supplies reciprocity for two NSF weights with its inverse domain, and SI-14 supplies the faithful cocycle formula and reference independence. Let \(A=d\varphi/d\psi'\) and \(p=s(\varphi)\). Then

\[
s(A)=p,\qquad \ker A=(1-p)H.
\]

Let \(A_p\) denote its injective part on \(pH\). Its imaginary powers are unitary on \(pH\). For \(x\in pMp\),

\[
A_p^{it}xA_p^{-it}=\sigma_t^{\varphi|_{pMp}}(x).
\]

For \(y'\in M'\), write \(y'|_{pH}\) for its restriction; this is well-defined because \(p\in M\). Then

\[
A_p^{it}(y'|_{pH})A_p^{-it}
=\sigma_{-t}^{\psi'}(y')|_{pH}.
\]

SI-09 proves that the right side depends only on \(y'|_{pH}\), including invariance of the restriction kernel. It does not rename the restriction of \(\psi'\) to an unspecified reduced algebra.

One equivalent formulation avoids restricted notation. Define \(U_t\) on \(H\) to equal \(A_p^{it}\) on \(pH\) and zero on \((1-p)H\). Then

\[
U_t\sigma_t^{\psi'}(y')=y'U_t
\quad(y'\in M',\ t\in\mathbb R).
\]

Here \(U_0=p\), and \(U_t^*U_t=U_tU_t^*=p\). These are unitaries on the support space, not generally on \(H\).

If the numerator is faithful, then \(p=1\) and the symmetry is reciprocal:

\[
\frac{d\psi'}{d\varphi}
=\left(\frac{d\varphi}{d\psi'}\right)^{-1}.
\]

The inverse is defined by the spectral calculus on its actual dense domain \(\operatorname{ran}A\). No bounded inverse is asserted.

For two **faithful** normal semifinite numerator weights \(\varphi_1,\varphi_2\), put \(A_j=d\varphi_j/d\psi'\). The spatial formula for the weight cocycle is

\[
[D\varphi_2:D\varphi_1]_t=A_2^{it}A_1^{-it}\in M.
\]

It is independent of the faithful commutant reference weight. The products here are bounded products of unitaries on the same \(H\); they require no unbounded-product closure. In this convention,

\[
\begin{gathered}
u_{s+t}=u_s\sigma_s^{\varphi_1}(u_t),\\
\sigma_t^{\varphi_2}=\operatorname{Ad}(u_t)\circ\sigma_t^{\varphi_1}.
\end{gathered}
\]

The first identity uses the first numerator as the reference weight. Reversing that reference or replacing the commutant time \(-t\) by \(t\) changes the assertion. Nonfaithful numerator cocycles need additional support and partial-isometry statements and are not supplied by this faithful formula.

## Order, finite addition and invertible transport

**Order, finite addition and invertible transport proved relative to the stated prerequisites.** One approximation works for every normal weight through The full spatial sum theorem and its joint core supplies the finite-functional addition theorem with its joint form core. Weight order is exactly closed-form order proves the order equivalence, and Bounded invertible change of the numerator proves invertible transport with the stated domains, relative to their prerequisites. Keep the denominator \(\psi'\) fixed.

For normal semifinite numerators,

\[
\varphi_1\leq\varphi_2
\quad\Longleftrightarrow\quad
\frac{d\varphi_1}{d\psi'}\leq\frac{d\varphi_2}{d\psi'}.
\]

The order on the right is **closed-form order**: if the derivatives are \(A_1,A_2\), it means

\[
D(A_2^{1/2})\subseteq D(A_1^{1/2}),\qquad
\|A_1^{1/2}\xi\|^2\leq\|A_2^{1/2}\xi\|^2
\quad(\xi\in D(A_2^{1/2})).
\]

When both numerators are **finite normal positive functionals**,

\[
\frac{d(\varphi_1+\varphi_2)}{d\psi'}
=\frac{d\varphi_1}{d\psi'}\mathbin{\dot+}\frac{d\varphi_2}{d\psi'}.
\]

The symbol \(\dot+\) means the operator associated with the sum of the two closed forms, whose domain is \(D(A_1^{1/2})\cap D(A_2^{1/2})\). Density of that domain and the common-core argument belong to the proof. This source-range assertion is not an unrestricted addition theorem for arbitrary semifinite weights.

Let \(a\in M\) be bounded and invertible. Define the transported weight without a notation ambiguity by

\[
\varphi_a(x)=\varphi(a^*xa)\quad(x\in M_+).
\]

Then \(\varphi_a\) is normal and semifinite, and

\[
\frac{d\varphi_a}{d\psi'}=aAa^*,\qquad A=\frac{d\varphi}{d\psi'}.
\]

The right side has operator domain

\[
\{\xi\in H:a^*\xi\in D(A)\}
\]

and form domain

\[
\{\xi\in H:a^*\xi\in D(A^{1/2})\}.
\]

Its form energy there is \(\|A^{1/2}a^*\xi\|^2\). Invertibility is retained: it is used to transport the core and to obtain this self-adjoint operator product with its stated domain.

## Recognizing an operator that comes from a weight

**Covariance characterization specified; finite-only source condition corrected.** Fix \(M\), \(H\) and \(\psi'\) as above. Let \(A\) be any nonnegative self-adjoint operator on \(H\), put \(p=s(A)\), and define \(U_t\) by imaginary powers on \(pH\), extended by zero. Conditions 1 and 2 are equivalent. Condition 3 is necessary but is not sufficient: the finite-only assertion printed in the source admits a verified counterexample. The valid coefficient characterization must compare all extended energies, including infinity.

1. There exists a normal semifinite weight \(\varphi\) on \(M\) with \(A=d\varphi/d\psi'\). Such a weight is unique.
2. For every \(y'\in M'\) and \(t\in\mathbb R\),

\[
U_t\sigma_t^{\psi'}(y')=y'U_t.
\]

At \(t=0\), this condition implies \(p\in M\); it does not presuppose a support projection in \(M\).

3. The domain

\[
\mathcal F=\mathcal D_{\psi'}(H)\cap D(A^{1/2})
\]

is a core for \(A^{1/2}\), and finite sums of energies depend only on their coefficient sum. Explicitly, if \(\xi_1,\ldots,\xi_r,\eta_1,\ldots,\eta_s\in\mathcal F\) and

\[
\sum_{i=1}^r\theta(\xi_i,\xi_i)
=\sum_{j=1}^s\theta(\eta_j,\eta_j),
\]

then

\[
\sum_{i=1}^r\|A^{1/2}\xi_i\|^2
=\sum_{j=1}^s\|A^{1/2}\eta_j\|^2.
\]

Condition 3 does not imply a reconstruction theorem on \(\mathcal J_{\psi'}\). A corrected reconstruction route must first impose consistency of all extended coefficient energies. Its exact ideal-weight requirement is as follows. There must be a weight \(w\) on \(\mathcal J_{\psi'}\cap M_+\) such that

\[
w(\theta(\xi,\xi))
=\begin{cases}
\|A^{1/2}\xi\|^2,&\xi\in D(A^{1/2}),\\
+\infty,&\xi\notin D(A^{1/2}),
\end{cases}
\quad \xi\in\mathcal D_{\psi'}(H).
\]

This weight must satisfy, for each \(z\in\mathcal J_{\psi'}\cap M_+\) and every net \(b_i\in M\) converging strongly to \(1\),

\[
w(z)\leq\liminf_i w(b_i z b_i^*).
\]

SX-02 through SX-04 proves that

\[
\varphi(x)=\sup\{w(z):z\in\mathcal J_{\psi'}\cap M_+,\ z\leq x\}
\quad(x\in M_+)
\]

is a normal additive weight extending \(w\). SX-04 proves semifiniteness from the dense finite-energy core; the ideal-extension theorem alone does not assert it. Positivity of a supremum alone does not establish these properties. The finite-energy condition above does not guarantee a well-defined extended rule. The corrected condition compares every finite family of denominator-bounded vectors, with infinity assigned outside the square-root domain, and requires equal coefficient sums to have equal extended energy sums. Together with the stated core condition, this is the valid reconstruction criterion proved in SX-04.

The implication from condition 2 is proved in SX-07 using CX-10 on the actual support corner and the supported ratio lemma SX-06; it retains that converse weight-cocycle theorem as a dependency. The finite-only implication from condition 3 is false; SX-08 through SX-10 proves the counterexample, and SX-04 supplies the all-energy replacement. For an already constructed derivative, condition 1 implies condition 3 by Completion gives the exact core and energy formula through The representing operator and its domains: the finite-energy domain is the exact square-root core, and weight additivity makes equal coefficient sums have equal finite energy sums. Uniqueness of an existing normal numerator follows from Weight order is exactly closed-form order, or directly from the positive coefficient approximants in SC-04 as proved in SC-13, Problem 4.

## Increasing weights and the convergence obligation

**Form, resolvent, compact-time spectral-power and modular-automorphism convergence supplied at their stated prerequisites.** Increasing weights, finite energy and resolvents proves the analytic assertions below, and SI-15 proves convergence in pointwise predual norm for automorphisms and their inverses. Let \((\varphi_n)_{n\geq1}\) be an increasing **sequence** of faithful normal semifinite weights on \(M\), and suppose

\[
\varphi(x)=\sup_n\varphi_n(x),\qquad x\in M_+,
\]

is semifinite. It is then faithful and normal. With \(\psi'\) fixed, the closed forms of \(A_n=d\varphi_n/d\psi'\) increase to the closed form of \(A=d\varphi/d\psi'\), and \(A_n\to A\) in strong resolvent sense.

The required domain identification is

\[
D(A^{1/2})=
\left\{\xi\in\bigcap_nD(A_n^{1/2}):
\sup_n\|A_n^{1/2}\xi\|^2<\infty\right\}.
\]

The supremum-energy bound cannot be deleted. Faithfulness makes all these operators injective. The spectral consequence of SS-09, using QF-08 and its SK calculus inputs, gives strong convergence of \(A_n^{it}\) to \(A^{it}\), uniformly for \(t\) in each compact real interval. Using SI-08's spatial modular identification, for a fixed \(x\in M\) and \(\xi\in H\), this yields

\[
\sup_{|t|\leq T}
\|(\sigma_t^{\varphi_n}(x)-\sigma_t^\varphi(x))\xi\|
\longrightarrow0,
\]

and the same assertion with \(x^*\). To prove this consequence from unitary convergence, use uniform convergence on the compact vector orbit \(\{A^{-it}\xi:|t|\leq T\}\), not an unjustified replacement of a varying vector by a fixed one.

The antecedent's topology on \(\operatorname{Aut}(M)\), defined in IX.1 immediately before Theorem 1.15, is pointwise norm convergence on the predual for automorphisms and their inverses. SF-12 and SE-11 prove its equivalence to the strong topology of the standard implementing unitaries. SI-15 proves the full compact-time predual convergence by absolutely summable vector-pair series in the given representation. This specification retains the source sequence hypothesis; SS-09 and SI-15 also prove their stated conclusions for arbitrary directed nets with a semifinite supremum. Those proofs depend on the prerequisites stated with them.

## A worked sign and support check

This finite-dimensional model verifies the conventions by a complete calculation. It supplies neither the general density theorem nor the general spatial-closure proof.

Let \(K=\mathbb C^d\), \(H=B(K)\) with Hilbert-Schmidt inner product \(\langle\xi,\eta\rangle=\operatorname{Tr}(\eta^*\xi)\), and represent \(M=B(K)\) by left multiplication \(L_a\xi=a\xi\). Its commutant consists of right multiplications \(R_b\xi=\xi b\), with \(R_bR_c=R_{cb}\).

Choose \(h\geq0\) and \(k>0\) in \(B(K)\), and set

\[
\varphi(L_a)=\operatorname{Tr}(ha),\qquad
\psi'(R_b)=\operatorname{Tr}(kb)\quad(a,b\geq0).
\]

The numerator is faithful exactly when \(h\) is invertible. The denominator is faithful. A GNS identification for it is

\[
\Lambda_{\psi'}(R_b)=k^{1/2}b\in H.
\]

Indeed,

\[
\psi'(R_b^*R_b)=\operatorname{Tr}(kbb^*)
=\|k^{1/2}b\|_{\mathrm{HS}}^2,
\]

and left GNS multiplication by \(R_c\) becomes right multiplication by \(c\). Since \(k\) is invertible, every \(\xi\in H\) is bounded and

\[
R_{\psi'}(\xi)=L_{\xi k^{-1/2}},\qquad
\theta_{\psi'}(\xi,\eta)=L_{\xi k^{-1}\eta^*}.
\]

Thus

\[
q_0[\xi]=\operatorname{Tr}(h\xi k^{-1}\xi^*)
=\|h^{1/2}\xi k^{-1/2}\|_{\mathrm{HS}}^2.
\]

The form is everywhere defined and closed, so its representing operator is

\[
A\xi=h\xi k^{-1}.
\]

Its support is left multiplication by \(s(h)\). In particular, if \(h\) has a kernel, \(A^{it}\) defined to vanish there is not a unitary on all of \(H\).

When \(h>0\), the imaginary powers act by

\[
A^{it}\xi=h^{it}\xi k^{-it}.
\]

The denominator's GNS Tomita operator has initial formula \(k^{1/2}b\mapsto k^{1/2}b^*\). Its squared norm is represented by \(L_{k^{-1}}R_k\): on \(\zeta=k^{1/2}b\),

\[
\|k^{1/2}b^*\|_{\mathrm{HS}}^2
=\operatorname{Tr}(k b^*b)
=\langle L_{k^{-1}}R_k\zeta,\zeta\rangle.
\]

Consequently its modular automorphism action on right multipliers is

\[
\sigma_t^{\psi'}(R_b)=R_{k^{-it}bk^{it}}.
\]

Direct multiplication now gives

\[
A^{it}R_bA^{-it}=R_{k^{it}bk^{-it}}
=\sigma_{-t}^{\psi'}(R_b).
\]

For two positive definite numerators \(h_1,h_2\),

\[
A_2^{it}A_1^{-it}=L_{h_2^{it}h_1^{-it}},
\]

which also checks the numerator order in the cocycle formula and cancellation of the reference matrix \(k\). No commutation of \(h_1\) with \(h_2\) is needed.

**Exercise 1.** In dimension two, take \(h=\operatorname{diag}(3,0)\) and \(k=\operatorname{diag}(2,5)\). Compute the four eigenvalues of \(A\), its support, and the vectors of zero energy.

**Solution.** For the matrix units \(E_{ij}\), \(AE_{ij}=h_{ii}k_{jj}^{-1}E_{ij}\). The eigenvalues on \(E_{11},E_{12},E_{21},E_{22}\) are \(3/2,3/5,0,0\). The support is the projection onto the first-row matrices, and the zero-energy vectors are exactly the second-row matrices. The imaginary powers on the first-row space are unitary there; their zero extensions annihilate the entire second-row space.

**Exercise 2.** For \(c>0\), derive how replacing \(\psi'\) by \(c\psi'\) changes the energy form, using the general bounded-vector definition.

**Solution.** The map \(V:H_{c\psi'}\to H_{\psi'}\) given by \(V\Lambda_{c\psi'}(x')=c^{1/2}\Lambda_{\psi'}(x')\) is unitary, as follows directly from the two GNS norms and their dense domains. The bounded-vector sets are equal and

\[
R_{c\psi'}(\xi)=c^{-1/2}R_{\psi'}(\xi)V.
\]

Thus \(\theta_{c\psi'}(\xi,\eta)=c^{-1}\theta_{\psi'}(\xi,\eta)\), the finite initial form domains agree, and \(q_0^{(c\psi')}=c^{-1}q_0^{(\psi')}\). The required spatial closures are supplied by The representing operator and its domains under the hypotheses of this unit; uniqueness of form representation then gives \(d\varphi/d(c\psi')=c^{-1}d\varphi/d\psi'\). The coefficient and initial-form assertions are proved here without assuming the general construction theorem.

## Exact remaining proof obligations

Each item below names a proof obligation of this specification and the results that address it.

* **SD-OPEN-01:** direct commutant-GNS bounded-vector density at arbitrary representation size is proved in Positive observations can be implemented by vector sums through The exact closure of bounded vectors, using concrete positive vector-series implementation. SI-11 supplies its source right-module dictionary. SF and SE separately supply the weight standard form and abstract comparison; the vector-series argument alone does not do so.
* **SD-OPEN-02:** SI-04 through SI-07 supplies the linking algebra, diagonal weights, finite rectangular inverse map, all four GNS corners and their graph cores. SI-09 through SI-10 supplies the nonfaithful supported corner and zero-domain identification without assuming symmetry of the weights.
* **SD-OPEN-03:** SI-11 supplies the actual commutant-GNS/opposite-module unitary, corner weight and GNS-map transport; SI-04 supplies the inverse finite-intertwiner correspondence. CX-03 supplies the analytic right-action identities for entire elements with the negative imaginary half-time sign. Their extension to all elements in the antecedent's closed complex-time domains is not proved here. The prerequisites of SF, SE and these providers are not proved here.
* **SD-OPEN-04:** SI-07 identifies the full rectangular closed relative graph with the completed coefficient form; SI-10 retains its nonfaithful zero part and proves independence of the auxiliary faithful completion; SI-12 specializes to the ordinary mixed two-weight GNS graph. SC-05 through SC-09 remains the direct form-construction provider, without a relative-map premise.
* **SD-OPEN-05:** both inclusions in the support equality, including zero numerators and noncentral supports, are proved in All and only the null directions survive at zero energy through The representing operator and its domains. SI-08 through SI-09 supplies the supported modular implementations and the restriction-kernel invariance; SI-13 supplies NSF reciprocity and its actual inverse domain.
* **SD-OPEN-06:** coefficient-ideal ultraweak density and positive approximation are proved in A coefficient ideal with an explicit approximate identity, both directions of derivative order in Weight order is exactly closed-form order, and invertible covariance with its actual operator and form domains in Bounded invertible change of the numerator. One approximation works for every normal weight through The full spatial sum theorem and its joint core supplies finite-functionals addition with its common form core. SX-02 supplies the normal additive extension of an ideal weight satisfying its strong-net lower-semicontinuity condition; semifiniteness is a separate core consequence in SX-04.
* **SD-OPEN-07:** SX-02 through SX-04 supplies all-energy consistency, ideal lower semicontinuity, normal additive extension and semifiniteness from the exact core. SX-08 through SX-10 refutes the finite-only source condition. SX-07 supplies covariance reconstruction on the actual support corner, using CX-10's NSF converse and SX-06's supported ratio. These are distinct exact dependencies; their prerequisites are not proved here.
* **SD-OPEN-08:** SI-14 supplies reference-weight independence, the faithful spatial cocycle formula and the balanced-matrix definition. SX-06 supplies the ratio for two weights with the same support. Distinct-support partial-isometry variants and their exact clauses remain separate obligations. General action cocycle/cohomology applications belong to OA-FLOW.
* **SD-OPEN-09:** Scalar multiples and pointwise suprema through Increasing weights, finite energy and resolvents supplies increasing extended energies, the exact finite-energy limit domain and the resolvents, identifying the pointwise supremum weight. Under the semifinite limit and faithful-tail hypotheses, SS-09 also supplies logarithm and compact-time imaginary powers through QF-08. SI-15 supplies the modular-automorphism conclusion in the source predual topology. A nonsemifinite supremum retains only the stated generalized form and resolvent conclusions.
* **SD-OPEN-10:** the source topology is defined in IX.1 before Theorem 1.15. SF-12 and SE-11 supply its standard-implementation interpretation; SI-15 proves compact-time pointwise predual-norm convergence for the automorphisms and their inverses.
* **SD-OPEN-11:** cover the finite algebra/finite commutant coupling-operator theorem with faithful normal tracial states agreeing on the center, including the definition of the coupling operator and all center-valued-trace prerequisites. The general course has not replaced this source item by the matrix model.

The bounded-vector/coefficient part, direct form construction, relative graph identification, supported modular transport, NSF reciprocity, faithful cocycle formula, corrected characterization and stated convergence proofs can be used with their precise hypotheses as named dependencies. The remaining complex-time domain extensions, distinct-support variants and coupling theorem listed above are not proved here.
