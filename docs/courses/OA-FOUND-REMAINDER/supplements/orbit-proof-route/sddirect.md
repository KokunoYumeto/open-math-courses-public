<span id="spatial-comparison-on-an-arbitrary-representation"></span>
# Spatial comparison on an arbitrary representation

<a id="OA-MOD-SD-01"></a>
<span id="oa-mod-sd-01-spaces-weights-and-dependency-contracts"></span>
<span id="oa-mod-sd-01"></span>
## OA-MOD-SD-01. Spaces, weights and dependency contracts

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

The following are exact dependencies, with their current status visible.

* **SD-DEP-GNS:** [OA-MOD-WG-003 through OA-MOD-WG-010](../../reader/orbit-proof-route/wg.html#OA-MOD-WG-003), for finite ideals, the linear extension of a weight, the semicyclic triple, its normal representation and semifinite cutoffs. Their proofs are given on the linked page.
* **SD-DEP-BOUNDED:** arbitrary Hilbert-space completions, bounded adjoints, positivity, continuous functional calculus, and the bicommutant theorem. These foundational results are used here without proof.


The bounded-vector proofs below use only SD-DEP-GNS and SD-DEP-BOUNDED. They do not assume SD-DEP-STANDARD or any spatial derivative already exists. References to OA-MOD-SC record downstream proofs of later contracts: SC uses SD-02, SD-04 and SD-05, while those three proofs have no SC premise. The direct construction does not use SD-DEP-STANDARD or SD-DEP-RELATIVE; those contracts govern the separate convention dictionary and relative modular identification.

<a id="OA-MOD-SD-02"></a>
<span id="oa-mod-sd-02-which-vectors-define-bounded-intertwiners"></span>
<span id="oa-mod-sd-02"></span>
## OA-MOD-SD-02. Which vectors define bounded intertwiners?

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

<a id="OA-MOD-SD-03"></a>
<span id="oa-mod-sd-03-a-useful-complete-norm-on-the-bounded-vectors"></span>
<span id="oa-mod-sd-03"></span>
## OA-MOD-SD-03. A useful complete norm on the bounded vectors

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

<a id="OA-MOD-SD-04"></a>
<span id="oa-mod-sd-04-coefficients-matrices-and-the-coefficient-ideal"></span>
<span id="oa-mod-sd-04"></span>
## OA-MOD-SD-04. Coefficients, matrices and the coefficient ideal

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

The proof has not asserted ultraweak density of \(\mathcal J_{\psi'}\). [OA-MOD-SC-04](../../reader/orbit-proof-route/scdirect.html#OA-MOD-SC-04) proves that density and supplies increasing positive approximants, using this algebraic ideal result.

<a id="OA-MOD-SD-05"></a>
<span id="oa-mod-sd-05-the-energy-formula-before-closure"></span>
<span id="oa-mod-sd-05"></span>
## OA-MOD-SD-05. The energy formula before closure

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

The preceding algebraic argument alone does not prove density of \(\mathcal E_{\varphi,\psi'}\), closability of \(q_0\), or completeness in its form norm. [OA-MOD-SC-05 through OA-MOD-SC-07](../../reader/orbit-proof-route/scdirect.html#OA-MOD-SC-05) prove density and closability and construct the closed completion. The representation theorem applies to that completion; the initial form need not itself be closed.

Although \(\mathcal D_{\psi'}(H)\) is invariant under \(M\), no such invariance of \(\mathcal E_{\varphi,\psi'}\) is asserted. A general weight does not satisfy \(\varphi(a z a^*)\leq\|a\|^2\varphi(z)\).

