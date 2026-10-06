# Fusion over a common spectral point

For an abelian middle algebra, fusion matches the same point in two module fields. It does not integrate over two independent points. On two atoms of measure one, take \(H=K=\mathbb C^2\) with the diagonal action of \(A=\mathbb C^2\). The vectors \(e_1\in H\) and \(e_2\in K\) have ordinary Hilbert tensor norm one, but their fused tensor is zero: their pointwise supports never meet. The pair \(e_1,e_1\) has fused norm one. The proof below determines exactly which pointwise tensors exist for general vectors.

First construct the common measure specified by the reference weight, including both module coordinate transports. Then construct the measurable tensor field and identify the entire fusion quotient with its integral. Finally prove the exact maximal domain for a pair of vectors. Worked examples distinguish a missing tensor, two eligible unbounded vectors, and a change of reference weight.

The source result is Masamichi Takesaki, *Theory of Operator Algebras II*, IX.3.23, whose proof is assigned to the reader. The argument here is complete at its explicitly named prerequisites. The abstract middle algebra has separable predual; its two normal unital module actions are on separable Hilbert spaces. Module kernels, zero and varying-dimensional fibres are allowed. The reference weight is faithful, normal and semifinite. Inner products are linear in the first variable.

The full fusion radical and bounded-vector model, canonical reference-weight comparison, measurable Hilbert fields, abelian diagonal realization, finite scalar density argument, finite-weight cutoffs, and Kaplansky density are used with their stated hypotheses. Scalar measure theory uses countable additivity, nonnegative monotone convergence, completed-measurable representatives and sigma-finite \(L^2\) spaces. No net version of scalar dominated convergence is assumed.

## Construct the weight measure and transport both modules

Let \(A\) be a nonzero abelian von Neumann algebra with separable predual. Let \(H\) and \(K\) be separable Hilbert spaces with normal unital representations of \(A\); since \(A\) is abelian, the action on \(H\) is also its right action. The two representations may have kernels. Let \(\psi\) be a faithful normal semifinite weight on \(A\).

We use the finite-weight cutoff construction in the weight GNS lesson, the abelian diagonal realization in central decomposition, measurable range subfields and the diagonal-commutant theorem in the Hilbert-field lesson, and the finite scalar Radon–Nikodym argument in central decomposition. Their precise statements, rather than a general invocation of disintegration, are the inputs. Inner products are linear in the first variable.

### Obtain a faithful separable representation

Normal positive functionals separate the positive cone of a von Neumann algebra. Its separable predual makes the set of normal positive functionals of norm at most one norm separable. Choose a countable norm-dense family \((\omega_j)\) in that set and positive numbers \(\alpha_j\) with sum one. The normal positive functional \(\omega_0=\sum_j\alpha_j\omega_j\) is faithful. Indeed if \(a\geq0\) has \(\omega_0(a)=0\), every nonnegative summand vanishes. Norm density then gives \(f(a)=0\) for every normal positive functional of norm at most one, hence for every normal positive functional; separation gives \(a=0\). Normalize \(\omega_0\) to a faithful normal state \(\omega\). Its value at one is positive because \(A\ne0\).

The GNS representation \(\pi_\omega\) is faithful and normal. Faithfulness follows from the faithful weight GNS theorem, and normality from the normal weight representation theorem. Its Hilbert space \(L_0\) is separable; the following argument does not assume a norm-separable algebra. The unit ball of \(A\) is weak-star compact and metrizable, by separability of its predual. Choose a countable weak-star dense subset \((a_n)\) of that ball and let \(L_1\) be the closed Hilbert span of \(\pi_\omega(a_n)\Omega\). For \(v\perp L_1\), the functional

\[
 a\longmapsto\langle\pi_\omega(a)\Omega,v\rangle
 \tag{AS.1}
\]

is normal: \(v\) is approximated in Hilbert norm by GNS vectors, their coefficient functionals are normal by normality of \(\pi_\omega\), and the coefficient-functional norm error is at most the Hilbert norm error times \(\|\Omega\|\). The predual is norm closed. This normal functional vanishes on the weak-star dense subset, hence on the entire unit ball, and therefore on \(A\). Cyclicity gives \(v=0\). Thus \(L_1=L_0\), proving separability.

Before using diagonalization, verify that a faithful normal representation \(\pi\) of \(A\) has a von Neumann image. First prove isometry. Positivity and the self-adjoint order bound make a unital star representation contractive on self-adjoint elements; applying this to \(a^*a\) and the C-star identity gives contractivity on every \(a\). If \(\|\pi(a)\|<\|a\|\), put \(b=a^*a\). The top point \(\|b\|\) belongs to its positive spectrum. Choose a continuous nonnegative function \(f\) on \([0,\|b\|]\) that vanishes on \([0,\|\pi(b)\|]\) and is nonzero at \(\|b\|\). Continuous functional calculus and polynomial approximation give \(f(b)\ne0\) but \(\pi(f(b))=f(\pi(b))=0\), contradicting injectivity. Thus \(\pi\) is isometric and its C-star image is norm closed.

The unit ball of \(\pi(A)\) is consequently precisely the image of the unit ball of \(A\). Normality makes this image map weak-star to ultraweak continuous. Banach–Alaoglu therefore makes the represented unit ball ultraweak compact and hence ultraweak closed. Let \(N=\pi(A)''\). The bicommutant theorem and Kaplansky density for the unital C-star algebra \(\pi(A)\) make its unit ball strongly dense in the unit ball of \(N\). The approximating operators are uniformly bounded, so their strong convergence is also ultraweak convergence. Ultraweak closedness of the represented unit ball gives \(N_1=\pi(A)_1\). Scaling gives \(N=\pi(A)\). This proves the image assertion at continuous functional calculus, weak-star compactness, bicommutant theorem and Kaplansky density; it does not infer image closure from the statement of normality alone.

Apply this argument and then the abelian diagonal realization to the faithful normal representation

\[
 a\longmapsto\pi_\omega(a)\oplus\rho_H(a)\oplus\rho_K(a)
 \quad\hbox{on }L_0\oplus H\oplus K .
 \tag{AS.2}
\]

It gives a compact metric Borel base \(Y\), a finite measure \(\mu_0\), a measurable field \(V_y\) of separable nonzero Hilbert spaces, and a unitary identifying \(A\) with the full diagonal algebra \(L^\infty(Y,\mu_0)\). In particular all completed-measurable bounded functions have Borel representatives modulo null sets. The abelian realization proof includes the onto assertion for this scalar algebra; merely representing the continuous functions would not suffice.

The three block projections in (AS.2) commute with that diagonal algebra. The diagonal-commutant theorem gives measurable bounded projection fields \(P_0(y),P_H(y),P_K(y)\). Take one common conull set for their adjoint, idempotent, pairwise orthogonality and sum identities. Their ranges are measurable subfields: projecting a countable fundamental family and applying zero-padded Gram–Schmidt gives a countable fundamental family in each range. Write these ranges as \(L_{0,y},H_y,K_y\). Restricting the unitary to the two module blocks gives

\[
 H\cong\int_Y^\oplus H_y\,d\mu_0(y),\qquad
 K\cong\int_Y^\oplus K_y\,d\mu_0(y).
 \tag{AS.3}
\]

The scalar action is the given action of \(A\) in both spaces. Individual zero fibres and varying dimensions are allowed, even though the combined faithful field \(V_y\) is nonzero almost everywhere. If \(H\) or \(K\) is zero its projection field and its entire range field are zero. No faithful action on either specified module has been assumed.

### Make the weight into a sigma-finite measure

In the identified diagonal algebra define

\[
 \nu(E)=\psi(1_E)
 \quad\hbox{for completed-measurable }E\subseteq Y.
 \tag{AS.4}
\]

This depends only on the \(\mu_0\)-equivalence class. For disjoint \(E_j\), the finite sums of their projections increase strongly to \(1_{\bigcup_jE_j}\). Additivity and normality of \(\psi\) give countable additivity of \(\nu\), including infinite values. Faithfulness gives

\[
 \nu(E)=0\quad\Longleftrightarrow\quad\mu_0(E)=0.
 \tag{AS.5}
\]

The forward direction says that a zero-weight projection is zero. The reverse direction says that a zero equivalence class is the zero projection.

Semifiniteness supplies an increasing net of finite-weight positive contractions \(e_i\) converging strongly to one. Normality of the faithful state \(\omega\) implies \(\omega(1-e_i)\to0\). Choose indices \(i_n\) with \(\omega(1-e_{i_n})<2^{-n}\); these chosen contractions need not themselves form an increasing sequence. Their spectral projections

\[
 q_n=1_{(1/2,1]}(e_{i_n}),\qquad
 Q_n=q_1\vee\cdots\vee q_n
 \tag{AS.6}
\]

do form increasing finite joins. The scalar spectral inequalities \(q_n\leq2e_{i_n}\) and \(1-q_n\leq2(1-e_{i_n})\) give \(\psi(q_n)<\infty\) and \(\omega(1-q_n)<2^{1-n}\). Because the algebra is abelian, \(Q_n\leq\sum_{j\leq n}q_j\), so additivity and monotonicity give \(\psi(Q_n)<\infty\). Moreover \(\omega(1-Q_n)\leq\omega(1-q_n)\to0\). If \(Q=\bigvee_nQ_n\), normality gives \(\omega(1-Q)=0\), and faithfulness gives \(Q=1\).

Choose nested Borel representatives \(F_n\) of the \(Q_n\). One can first choose representatives individually, then replace the \(n\)-th by their finite union. Their union is conull for \(\mu_0\), and therefore for \(\nu\), and

\[
 \nu(F_n)=\psi(Q_n)<\infty .
 \tag{AS.7}
\]

Remove the common null complement of their union. This proves sigma-finiteness of \(\nu\) without assuming \(\psi(1)<\infty\), and without assuming that all finite-weight projections in an arbitrary nonabelian algebra are directed.

For every bounded nonnegative measurable function \(a\), choose nonnegative simple functions increasing to \(a\). They give increasing elements of \(A_+\) with supremum \(a\). The projection definition and additivity give the integral formula on each simple function. Normality and scalar monotone convergence then give

\[
 \psi(a)=\int_Y a(y)\,d\nu(y)\quad(a\in A_+).
 \tag{AS.8}
\]

This is the desired weight representation on the entire positive cone, including infinite weight values.

### Change both module coordinates to that measure

Let \(B_1=F_1\) and \(B_n=F_n\setminus F_{n-1}\) for \(n>1\). Both \(\mu_0|_{B_n}\) and \(\nu|_{B_n}\) are finite, and the second is absolutely continuous with respect to the first. The finite scalar Radon–Nikodym proof supplies a nonnegative finite density \(w_n\) on \(B_n\). Glue these countably many densities to a measurable \(w\). Formula (AS.5) shows that \(w>0\) almost everywhere: the measurable zero set of a density has zero \(\nu\)-measure and therefore zero \(\mu_0\)-measure. The densities are finite almost everywhere because they have finite integrals on each \(B_n\). Thus

\[
 0<w(y)<\infty\ \hbox{a.e.},\qquad
 d\nu=w\,d\mu_0 .
 \tag{AS.9}
\]

All integral identities extend from the disjoint finite pieces by nonnegative monotone convergence. The measures have the same null sets and the same completed Borel measurable structure. Put \(\mu=\nu\). The base is still standard and is now sigma-finite for the weight measure.

For any of the subfields \(E_y=H_y,K_y,L_{0,y}\), define the coordinate transport

\[
 \begin{gathered}
 C_w:\int^\oplus E_y\,d\mu_0\\
 \longrightarrow\int^\oplus E_y\,d\mu,\\
 (C_w\xi)(y)=w(y)^{-1/2}\xi(y).
 \end{gathered}
 \tag{AS.10}
\]

The field is measurable because it is multiplied by a measurable scalar. Its squared integral norm is unchanged:

\[
 \begin{gathered}
 \int_Y\|w^{-1/2}\xi(y)\|^2\,d\mu(y)\\
 =\int_Y\|\xi(y)\|^2\,d\mu_0(y).
 \end{gathered}
 \tag{AS.11}
\]

The inverse is multiplication by \(w^{1/2}\); the same identity verifies its whole domain and shows that \(C_w\) is onto. These statements require no essential bound on either scalar multiplier. The operators are unitaries between two different integral Hilbert spaces, not necessarily bounded multiplication operators on a fixed one. Scalar \(A\)-actions intertwine because both coordinate multipliers commute pointwise. Composing (AS.3) with \(C_w\) gives the exact common model

\[
 \begin{aligned}
 A&=L^\infty(Y,\mu),\\
 \psi(a)&=\int_Ya\,d\mu,\\
 H&=\int_Y^\oplus H_y\,d\mu,\\
 K&=\int_Y^\oplus K_y\,d\mu .
 \end{aligned}
 \tag{AS.12}
\]

This proves existence of the spectral inputs used by the abelian fusion argument at the stated elementary and course prerequisites.

### A coordinate check and the zero algebra

For a concrete nonfinite weight, take \(\mu_0\) to be Lebesgue measure on \((0,1)\) and \(w(t)=t^{-1}\). The intervals \(F_n=[1/n,1)\), \(n\geq2\), have weight measure \(\log n\) and exhaust the base modulo null sets, but \(\mu(Y)=\infty\). The constant section one belongs to the old scalar \(L^2\) space and not to the new one if left unchanged. The correct new section is \(t^{1/2}\), whose squared norm under \(d\mu=dt/t\) is one. This tests the coordinate factor in (AS.10).

For a constant weight change \(d\mu=c\,d\mu_0\), the coordinate factor for each module is \(c^{-1/2}\). A pointwise tensor of two unchanged abstract module vectors consequently has new coordinate factor \(c^{-1}\). Its canonical fusion comparison instead has coordinate factor \(c^{-1/2}\), as the fusion norm calculation shows. Two module coordinate changes do not by themselves define that canonical comparison.

If \(A=0\) with identity zero, unital module actions force \(H=K=0\). Use the empty measure space and empty fields; every asserted integral and fusion is zero. The construction above handles all nonzero algebras, all zero specified modules, and all module kernels without changing the measure on their complement.

Take the common spectral realizations

\[
 A=L^\infty(Y,\mu),\qquad
 \psi(a)=\int_Y a\,d\mu\quad(a\geq0),\qquad
 H=\int_Y^\oplus H_y\,d\mu(y),\quad
 K=\int_Y^\oplus K_y\,d\mu(y).
 \tag{AF.1}
\]

Here the base is standard and sigma-finite, the module actions are scalar multiplication, and the fields have countable measurable fundamental sections. These are the spectral disintegrations in the proposition, with the same weight measure on both sides. A different measure in the same class requires unitary coordinate transport; one cannot silently leave both the measure and vector coordinates unchanged. The module actions need not be faithful: their kernels are represented by zero fibres.

The standard GNS space is \(L=L^2(Y,\mu)\). On \(L^\infty\cap L^2\), its GNS map is the function itself, its closed Tomita involution is complex conjugation, and its modular operator is one. Indeed bounded functions of finite-measure support are dense in \(L^2\); conjugation is already an everywhere-defined antiunitary, and the initial involution has that closure. Thus the opposite GNS coordinate \(\Lambda'_\psi(x)=J\Lambda_\psi(x^*)\) is also \(x\), and the standard left and right actions are both multiplication.

## Construct a measurable tensor field with its full frame

The ordinary fibre tensor product needs an actual positive inner product. For a finite algebraic sum \(u=\sum_i x_i\otimes y_i\), choose orthonormal bases \((e_a)\) and \((f_b)\) of the finite-dimensional spans of its factors and write \(u=\sum_{a,b}c_{ab}e_a\otimes f_b\). The coefficient formula

\[
 \left\langle\sum_i x_i\otimes y_i,\sum_j z_j\otimes t_j\right\rangle
 =\sum_{i,j}\langle x_i,z_j\rangle\langle y_i,t_j\rangle
 \tag{AF.T1}
\]

is well defined on the algebraic tensor product by its bilinear universal property. In the chosen coordinates its quadratic value is \(\sum_{a,b}|c_{ab}|^2\). The basis tensors are algebraically independent: applying the coordinate functional on each factor recovers each \(c_{ab}\). Thus a zero quadratic value means a zero algebraic tensor. The formula is a positive-definite inner product, and its Hilbert completion is the ordinary complex Hilbert tensor product. The product orthonormal basis is complete because the algebraic tensor span is dense in that completion. For separable factors its index set is countable; a zero factor gives the zero completion.

The tensor-product foundation lesson, Section 5, uses this Hilbert cross norm and proves its uniqueness by complex polarization. Here the coordinate argument supplies the particular construction and total product frame needed for the measurable fibres. No singular-value theorem or trace-duality result is an input.

Apply DF02 to obtain measurable orthonormal frames \(e_i(y)\) for \(H_y\) and \(f_j(y)\) for \(K_y\), extended by zero whenever a coordinate is absent. In

\[
 G_y=H_y\otimes_{\mathbb C}K_y,\qquad
 g_{ij}(y)=e_i(y)\otimes f_j(y),
 \tag{AF.2}
\]

the nonzero \(g_{ij}(y)\) form an orthonormal basis. The Gram functions of the countable family \((g_{ij})\) are measurable: the ordinary tensor coefficient formula multiplies the two frame Gram functions. DF01 therefore defines a unique measurable structure generated by this family. In particular its fibres can have changing dimensions and can vanish.

If \(\xi,\eta\) are measurable sections of the two fields, their pointwise tensor is measurable in this structure. Its coordinates are

\[
 \langle\xi(y)\otimes\eta(y),g_{ij}(y)\rangle
 =\langle\xi(y),e_i(y)\rangle\langle\eta(y),f_j(y)\rangle .
 \tag{AF.3}
\]

These are measurable. The Gram-testing criterion gives the assertion, or equivalently finite coordinate sums converge pointwise to the section. Its squared fibre norm is exactly \(\|\xi(y)\|^2\|\eta(y)\|^2\). Define the actual target Hilbert space, using DF06, by

\[
 G=\int_Y^\oplus G_y\,d\mu(y).
 \tag{AF.4}
\]

This constructs its measurable structure and completion before a fusion symbol is assigned to a section.

## Identify the entire fusion quotient and prove onto

The right-bounded vectors in the weight model are precisely

\[
 D(H,\psi)=\{\xi\in H:\operatorname*{ess\,sup}_y\|\xi(y)\|<\infty\}.
 \tag{AF.5}
\]

For such a section \(L_\psi(\xi):L\to H\) sends \(h(y)\) to \(h(y)\xi(y)\); its norm is the essential supremum in (AF.5). The upper estimate is integration. Conversely the defining bounded-vector inequality, tested on \(x=1_E\) for every measurable finite-measure \(E\), gives
\(\int_E\|\xi(y)\|^2\,d\mu\leq C\mu(E)\). If \(\|\xi(y)\|^2>C\) on a positive-measure set, a finite-measure part of a positive gap set contradicts this inequality. This proves the converse and the exact norm. The same argument describes \(D'(K,\psi)\).

For two right-bounded vectors, the coefficient is multiplication by

\[
 L_\psi(\zeta)^*L_\psi(\xi)
 =M_{\langle\xi(y),\zeta(y)\rangle}.
 \tag{AF.6}
\]

To check the order and conjugations, its scalar inner product against \(k\in L\) is
\(\int h(y)\overline{k(y)}\langle\xi(y),\zeta(y)\rangle\,d\mu\), obtained from the inner product of \(h\xi\) and \(k\zeta\). The scalar coefficient is bounded by the product of the two essential norm bounds.

Consequently the fusion form on two arbitrary finite sums is

\[
 \begin{aligned}
 &\left\langle\sum_i\xi_i\otimes_\psi\eta_i,
                   \sum_j\zeta_j\otimes_\psi\theta_j\right\rangle\\
 &\quad=\int_Y\sum_{i,j}
       \langle\xi_i(y),\zeta_j(y)\rangle
       \langle\eta_i(y),\theta_j(y)\rangle\,d\mu(y)\\
 &\quad=\left\langle\sum_i\xi_i(y)\otimes\eta_i(y),
                       \sum_j\zeta_j(y)\otimes\theta_j(y)\right\rangle_G .
 \end{aligned}
 \tag{AF.7}
\]

Here every first entry is right-bounded and every second entry belongs to \(K\). Each integrand is integrable, by the essential first-entry bounds and scalar Cauchy–Schwarz for the second entries. This is equality of the entire finite-sum form, including all cross terms. Its full radical consists exactly of sums whose target section is zero almost everywhere. Thus the pointwise map descends to an isometry of the full null quotient, not merely of an algebraic quotient by balancing relations. FU03 identifies its completion with the entire fusion space.

The isometry is onto. Let \(a\in L^2(Y,\mu)\) be supported in \(F_n\) and where \(g_{ij}\neq0\). The section \(ag_{ij}\) is the image of
\((1_{F_n}e_i)\otimes_\psi(af_j)\). Its first entry has norm at most one pointwise and finite global norm; its second has finite global norm. Finite sums of these sections are dense in \(G\): expand a target vector in the countable frame, truncate the coordinate set, then restrict each coordinate to \(F_n\). Parseval and monotone convergence make both truncations converge in the Hilbert norm. The range of an isometry from a complete space is closed, so it contains all of \(G\). We have proved the specified unitary

\[
 U_\psi:H\boxtimes_AK\longrightarrow G,\qquad
 U_\psi(\xi\otimes_\psi\eta)(y)=\xi(y)\otimes\eta(y)
 \quad(\xi\in D(H,\psi),\ \eta\in K).
 \tag{AF.8}
\]

Scalar balancing, including either inherited outer \(A\)-action, follows pointwise. If the two modules have disjoint supports, every fibre tensor and the entire fusion space are zero. No faithful-module assumption was used.

## Determine exactly which vector pairs have a tensor

Fix \(\eta\in K\). Pointwise tensoring with \(\eta(y)\) defines a linear multiplication operator from \(H\) to \(G\) with maximal domain

\[
 \mathcal D_\eta=
 \left\{\xi\in H:\int_Y\|\xi(y)\|^2\|\eta(y)\|^2\,d\mu(y)<\infty\right\}.
 \tag{AF.9}
\]

This operator is closed. If \(\xi_n\to\xi\) in \(H\) and their images tend to \(u\) in \(G\), DF06 supplies a common subsequence converging in both fibre norms almost everywhere. Tensoring with the fixed \(\eta(y)\) is continuous on each fibre, so \(u(y)=\xi(y)\otimes\eta(y)\) there. Since \(u\in G\), the integral in (AF.9) is finite; the asserted limit belongs to the graph.

Right-bounded first vectors form a core for this maximal operator. For \(\xi\in\mathcal D_\eta\), put

\[
 E_n=F_n\cap\{\|\xi(y)\|\leq n\},\qquad \xi_n=1_{E_n}\xi .
 \tag{AF.10}
\]

These are right-bounded and converge to \(\xi\) in \(H\). Their tensor images converge in \(G\), because the squared image error is the tail integral of the integrable function in (AF.9). This proves graph-norm convergence. The closedness just proved also shows that any graph-convergent approximating family yields the same section. With \(U_\psi\) we therefore define, for every eligible pair,

\[
 \xi\otimes_\psi\eta
 =U_\psi^{-1}\bigl(y\mapsto\xi(y)\otimes\eta(y)\bigr),\qquad
 \|\xi\otimes_\psi\eta\|^2
 =\int_Y\|\xi(y)\|^2\|\eta(y)\|^2\,d\mu(y).
 \tag{AF.11}
\]

This agrees with (AF.8), is independent of representative changes on null sets, and proves the full vector formula of IX.3.23. Interchanging the roles gives the same extension of the left-bounded model. Neither entry has to be bounded when (AF.9) holds. Conversely failure of the integral means the displayed section is not in \(G\); it cannot be the norm limit prescribed by this formula.

The statement concerns a partially defined bilinear operation. It does not extend tensoring continuously to all of \(H\times K\). In particular convergence of both entries separately in their Hilbert norms does not by itself imply convergence in the fusion norm.

## Test the domain and its topology

**A pair with no tensor.** Let \(H=K=L^2(0,1)\), \(A=L^\infty(0,1)\), and \(\psi\) be Lebesgue integration. Both vectors \(\xi(y)=\eta(y)=y^{-1/3}\) belong to \(L^2\), since \(\int_0^1y^{-2/3}\,dy=3\). But their tensor would have squared norm \(\int_0^1y^{-4/3}\,dy=\infty\). The obstruction occurs even with one-dimensional fibres and faithful module actions.

**Two unbounded eligible vectors.** With \(\xi(y)=\eta(y)=y^{-1/8}\), both entries are unbounded, while their tensor has squared norm \(\int_0^1y^{-1/2}\,dy=2\). Cutoffs at \(y=1/n\) converge in the graph norm of (AF.9), not because either entry becomes globally bounded in the limit.

**Why a Hilbert-norm approximation is insufficient.** Set \(\xi_n=\eta_n=n^{1/2}1_{(0,1/n^2)}\). Both Hilbert norms are \(n^{-1/2}\), so the entries tend to zero, while \(\|\xi_n\otimes_\psi\eta_n\|^2=1\). Every pair is individually eligible. This disproves continuity at the zero pair for the unrestricted product of Hilbert norms.

## Compare the reference weights with the correct coordinates

**A change of reference weight.** Keep the abstract module Hilbert spaces fixed and replace \(\psi\) by \(c\psi\), \(c>0\). Its GNS norm is multiplied by \(\sqrt c\), so the coefficient (AF.6), and therefore the squared fusion norm of an unchanged vector symbol, is divided by \(c\). FU09's canonical comparison sends

\[
 \xi\otimes_\psi\eta
 \longmapsto\sqrt c\,(\xi\otimes_{c\psi}\eta).
 \tag{AF.12}
\]

This preserves the full finite-sum form and extends onto the completed spaces. In coordinates with measure \(c\mu\), each fixed module vector is represented by \(c^{-1/2}\) times its old section. An unchanged pair therefore has target section \(c^{-1}\xi(y)\otimes\eta(y)\), whereas the canonical comparison has section \(c^{-1/2}\xi(y)\otimes\eta(y)\). The target integral norm of the latter equals the source norm. For \(c=9\) the difference is a factor of three. This is precisely the reference-weight warning following the proposition and in Remark 3.22.

For a nonconstant measure change \(d\mu=w\,d\mu_0\), the same distinction is visible before any canonical comparison is made. Each fixed abstract module vector has weight-measure coordinate \(w^{-1/2}\) times its old coordinate. Their pointwise tensor has factor \(w^{-1}\). Formula (AS.11) concerns each module separately; the fusion comparison preserves the entire coefficient form. It cannot be inferred by pretending both modules' coordinates stayed fixed.

### Mathematical sources

Masamichi Takesaki, *Theory of Operator Algebras II*, IX.3.23 gives the abelian fusion statement and the eligible-vector condition. The spectral antecedents are in Volume I, IV.8. The common-weight model and the complete quotient, onto and maximal-domain arguments are independently written classical exposition, OpenAI Codex, Ultra, October 2026, CC0-1.0. The tensor-product foundation lesson supplies the same ordinary Hilbert tensor statement; its broader singular-value results are not used.

