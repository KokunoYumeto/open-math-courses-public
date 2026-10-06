# Measurable weight fields and their direct integrals

**Self-checked by the writing AI.**

A measurable weight field must control the finite adjoint domain, rather than only assign measurable values to a few positive operators. This unit separates that field comparison from two further questions: how to evaluate every positive field, including infinite values, and how to recover measurable GNS vectors when an input is finite. The resulting integral has an exact finite domain and decomposes its full modular operators.

The antecedents are Takesaki, *Theory of Operator Algebras II*, VIII.4, Definition 4.4, Lemma 4.5, Definition 4.6 and Theorems 4.7–4.8. Definitions and proofs are independently written. Lemma 4.5's compatible associated-field comparison has original arguments in Exact data, conclusion and prerequisite boundary through The reverse comparison and the realization obstruction, including construction of the actual GNS field and both typed representation transports. The FIELD, CENTRAL and SELECTION contracts of the earlier lesson Recovering algebras from measurable fibres, and the prerequisites they rest on, are not proved here.

## The pointwise finite-adjoint core and compatible comparison

Fix a standard sigma-finite measure space \((Y,\mu)\) and a measurable field of von Neumann algebras \(M_y\). Measurability is understood relative to the completed measure when representatives are changed on null sets. Fibres may have variable dimensions, including the zero algebra. Let \(\varphi_y\) be faithful normal semifinite weights. Write

\[

\mathfrak a_y=\mathfrak n_{\varphi_y}\cap\mathfrak n_{\varphi_y}^*,\qquad

\|x\|_{\varphi_y,\sharp}^2=\varphi_y(x^*x)+\varphi_y(xx^*).

\tag{MW.1}

\]

At the pointwise scope of Definition VIII.4.4, the weight field is measurable when there are countably many measurable operator fields \(x_j(y)\) such that:

1. \(x_j(y)\in\mathfrak a_y\) for every fibre in the chosen realization.

2. Both \(\varphi_y(x_j(y)^*x_k(y))\) and \(\varphi_y(x_j(y)x_k(y)^*)\) are measurable scalar functions for every \(j,k\), using the linear extension to the finite definition algebra.

3. The set \(\{x_j(y):j\geq1\}\) is dense in \(\mathfrak a_y\) for (MW.1), for each \(y\).

No global square-integrability of these fields is part of this definition. The countable core makes the GNS Hilbert space separable: its Hilbert closure contains the finite-star GNS domain, which is dense by WG-009. Faithfulness identifies \(x\) with \(\Lambda_y(x)\). WH-09–11 make

\[

\mathcal A_y=\Lambda_y(\mathfrak a_y),\qquad

\|\Lambda_y(x)\|_S^2=\|x\|_{\varphi_y,\sharp}^2

\tag{MW.2}

\]

the full left Hilbert algebra and its sharp graph norm.

The source and the current DI-00 both require density of the countable set itself for the graph norm. If only its linear span is initially graph dense, adjoining all finite \(\mathbb Q(i)\)-linear combinations gives the required set: approximate the finitely many complex coefficients while controlling the sum of the corresponding graph norms. Scalar products, sharp images and products remain measurable by finite sums. A merely Hilbert-total sequence need not satisfy this stronger density. The same enlargement applies to the right algebra.

**MW-DEP-GNS-FIELD** has complete original author arguments at its named inputs in Exact data, conclusion and prerequisite boundary through The reverse comparison and the realization obstruction. GFR-02 constructs the actual GNS Hilbert field from the first Gram matrix and an intrinsic closed graph field from both Gram orders. GFR-04–05 uses concrete block resolvents and completed analytic selection to recover measurable sharp and product vectors without assuming the missing mixed coefficients. GFR-06 gives the full associated algebra field; GFR-07–08 proves measurable forward and inverse canonical operator transports; GFR-10 proves the reverse comparison with its typed inverse hypothesis. The compatible realization is constructed from the concrete test fields. The abstract frame counterexample A full finite-dimensional field with a nonmeasurable concrete frame through The exact operator transport that fails remains valid, and MC-05 remains a conditional reverse theorem.

All subsequent assertions use these precise GFR clauses and the actual DF, DC and SCF inputs of DI. Operators are transported into the constructed measurable GNS Hilbert field. DI-05 uses the explicit closed multiplier core SCF-03 to supply countable measurable graph-dense right-algebra sections \(\eta_j(y)\), their closed involution images and right multipliers. Rational enlargement makes the set itself graph dense. No proper-original-algebra defect selector or unrestricted DI-08 converse is used in this construction.

## A countable contractive family detects every positive value

Fix one fibre temporarily. Let \(\mathcal A_r\) be its full right algebra, \(F\) its closed involution, and \(r_j=R_{\eta_j}\). A graph-dense family may have unbounded multiplication norms. We produce a countable family of right contractions without losing the density needed for the variational formula.

Define

\[

g(t)=\begin{cases}1,&|t|\leq1,\\|t|^{-1},&|t|>1,\end{cases}\qquad

B_j=\begin{pmatrix}0&r_j^*\\r_j&0\end{pmatrix},\qquad

g(B_j)=\begin{pmatrix}b'_j&0\\0&b_j\end{pmatrix}.

\tag{MW.3}

\]

Here \(b_j=\min(1,(r_jr_j^*)^{-1/2})\), with value one on the zero spectral subspace; \(b'_j\) uses \(r_j^*r_j\). Both are bounded positive contractions. Put

\[

\beta_j=b_j\eta_j,\qquad

R_{\beta_j}=b_jr_j,\qquad

F\beta_j=b'_jF\eta_j,\qquad \|R_{\beta_j}\|\leq1.

\tag{MW.4}

\]

For the domain assertion, covariance first makes \(\beta_j\) right bounded. Both \(r_j\) and \(r_j^*\) belong to the finite right ideal. Its left-ideal property puts \(b_jr_j\) and \((b_jr_j)^*=r_j^*b_j=b'_jr_j^*\) there. The full ideal-intersection theorem RD-07/WH-03, applied to the opposite right algebra, gives \(\beta_j\in\mathcal A_r\); its adjoint multiplier and injectivity give the stated \(F\)-image. Thus the formula includes the actual involution domain.

This family is graph dense in the set of right-algebra vectors with multiplier norm at most one. To prove it, let such a vector \(\eta\) be given, and choose \(\eta_{j_k}\to\eta\), \(F\eta_{j_k}\to F\eta\). For every \(a\in\mathcal A_l\), mixed multiplication gives

\[

r_{j_k}a=L_a\eta_{j_k}\longrightarrow L_a\eta=R_\eta a,\qquad

r_{j_k}^*a=L_aF\eta_{j_k}\longrightarrow R_\eta^*a.

\tag{MW.5}

\]

Let \(B\) be the self-adjoint matrix in (MW.3) for \(R_\eta\). Its norm is at most one. Equation (MW.5) gives \(B_{j_k}u\to Bu\) on the dense subspace \(\mathcal A_l\oplus\mathcal A_l\). For \(w=(B+i)u\) on this subspace,

\[

(B_{j_k}+i)^{-1}w-u=(B_{j_k}+i)^{-1}(B-B_{j_k})u\longrightarrow0.

\tag{MW.6}

\]

The resolvents have norm at most one, and these \(w\)'s are dense because \(B+i\) is boundedly invertible. Thus the resolvents converge strongly on the whole space; the same argument works at \(-i\). Their Cayley unitaries and adjoints converge strongly. Continuous functional calculus on the circle therefore gives \(f(B_{j_k})\to f(B)\) strongly for every \(f\in C_0(\mathbb R)\): the corresponding circle function has value zero at the missing point, and Laurent-polynomial approximation proves the assertion. Apply this to the continuous function \(g\) in (MW.3). Since \(g(B)=I\), both diagonal blocks converge strongly to \(I\). Equations (MW.4) now give

\[

\beta_{j_k}\to\eta,\qquad F\beta_{j_k}\to F\eta.

\tag{MW.7}

\]

This proves the promised density without pretending that a graph approximation controls operator norms directly.

Return to the field. DI's bounded field calculus, with localization when \(\|r_j(y)\|\) has no common bound, makes both blocks in (MW.3) measurable. Consequently \(\beta_j(y)\) and \(F_y\beta_j(y)\) are measurable. The full variational theorem WH-12 and (MW.7) imply, for every positive bounded operator in a fibre,

\[

\varphi_y(a)=\sup_j\langle\pi_y(a)\beta_j(y),\beta_j(y)\rangle.

\tag{MW.8}

\]

Continuity of the quadratic form for each fixed bounded \(\pi_y(a)\) justifies restriction to this dense countable family. The supremum may be infinite. WH-12 itself uses all dominated normal positive functionals and NW-11, so (MW.8) is not an assertion based only on agreement on the finite cone.

For a measurable positive operator field \(a(y)\in M_y^+\), each coefficient in (MW.8) is measurable by the proved forward representation transport GFR-08. No uniform essential bound on \(\|a(y)\|\) is needed: it is bounded on each fibre and its action is measurable. The countable supremum proves measurability of \(y\mapsto\varphi_y(a(y))\), including the set where its value is infinity. This is the entire assertion (i) of Theorem VIII.4.7.

The source's finite-subset cutoff argument can also be made explicit with this family. Adjoin all integer multiples of the \(\beta_j\); (MW.7) makes this enlarged set graph dense in \(\mathcal A_r\). In a finite subset containing \(k\beta_j\), its sum \(h\) of right-multiplier-star products satisfies \(h\geq k^2R_{\beta_j}^*R_{\beta_j}\). For \(z=h(1+h)^{-1}\), inverse order and scalar calculus give

\[

R_{\beta_j}^*R_{\beta_j}\leq(1+k^{-2})z.

\tag{MW.9}

\]

Indeed \(0\leq R_{\beta_j}^*R_{\beta_j}\leq I\), and the inequality holds on its scalar spectrum after replacing \(h\) by \(k^2R_{\beta_j}^*R_{\beta_j}\). The sum \(h\) belongs to the positive finite definition ideal of the right weight. Since \(0\leq z\leq h\), \(z\) belongs to that ideal too. The positive map \(\Theta_r\) of Completely positive maps from the finite algebras, on that exact finite domain, transfers (MW.9) to normal positive functionals on the left represented algebra. Its square formula gives \(\Theta_r(R_{\beta_j}^*R_{\beta_j})(a)=\langle\pi_y(a)\beta_j,\beta_j\rangle\). Letting \(k\to\infty\) and then taking the supremum over \(j\) recovers (MW.8) on all positive inputs. This specifies the scaling present in a dense enlarged family and the step needed for infinite values. A merely total sequence such as \(2^{-j}\) in the scalar right algebra would instead give \(h=1/3\) and \(z=1/4\); it is not the graph-dense set required by the printed definition.

## Recovering measurable GNS vectors by an injective equation

Let \(b(y)\) be a measurable operator field with \(\varphi_y(b(y)^*b(y))<\infty\) on a measurable set \(E\). We prove that \(\Lambda_y(b(y))\) is a measurable vector field there. In particular this supplies the inverse-GNS step for square roots in the integral theorem. Its finite set is measurable by MW-02.

Use the unnormalized right graph-dense family from MW-01 and write \(r_j(y)=R_{\eta_j(y)}\). Its common kernel is zero. If \(r_j\xi=0\) for every \(j\), then

\(\xi\perp r_j^*a=L_aF\eta_j\) for all \(a\in\mathcal A_l\). The vectors \(F\eta_j\) are Hilbert total by graph density and the dense range of the closed involution. Hence \(\xi\perp L_aH\) for every \(a\). Nondegeneracy of the left Hilbert algebra gives \(\xi=0\).

GFR-08 makes the represented operator \(\pi_y(b(y))\) measurable. All following coefficients are consequently measurable and finite on each fibre. Define

\[

c_j(y)=\frac{2^{-j}}{1+\|r_j(y)\|^2+\|\pi_y(b(y))\eta_j(y)\|^2},\quad

K_y=\sum_{j\geq1}c_j(y)r_j(y)^*r_j(y),

\tag{MW.10}

\]

and

\[

u_y=\sum_{j\geq1}c_j(y)r_j(y)^*\pi_y(b(y))\eta_j(y).

\tag{MW.11}

\]

The operator series converges in norm, with tails bounded by the corresponding geometric tails. The vector series is absolutely convergent: \(c_j\|r_j\|\|\pi_y(b)\eta_j\|\leq2^{-j}/2\). Thus \(K_y\) and \(u_y\) are measurable fields. Moreover \(0\leq K_y\leq I\), and the strictly positive coefficients and common-kernel argument give \(\ker K_y=0\).

On \(E\), the existing finite GNS vector \(\xi_y=\Lambda_y(b(y))\) satisfies, by WH-04,

\[

r_j(y)\xi_y=\pi_y(b(y))\eta_j(y),\qquad K_y\xi_y=u_y.

\tag{MW.12}

\]

Consequently the explicit measurable fields

\[

\xi_{y,n}=(K_y+n^{-1}I)^{-1}u_y

=K_y(K_y+n^{-1}I)^{-1}\xi_y

\longrightarrow\xi_y

\tag{MW.13}

\]

converge in norm on every fibre of \(E\). The inverse in (MW.13) has the global bound \(n\), so bounded field calculus applies. Injectivity of \(K_y\) and spectral bounded convergence prove the limit. Extending by zero outside \(E\) yields a measurable section.

This is an inverse on the known finite domain. We have not inferred finiteness from solvability of a weighted normal equation: such an equation alone need not solve every original multiplication equation. Finiteness came from (MW.8), while (MW.12) identifies the unique existing GNS vector. No selector for uncountably many unknown vectors, and no assertion that a measurable multiplier automatically has a measurable inverse vector, was used.

## Constructing the integral weight and its full operators

GFR-02–06 constructs the actual measurable full left Hilbert-algebra field \(\mathcal A_y\subseteq H_{\varphi_y}\). DI-06–09 gives its integrated algebra on \(H=\int_Y^\oplus H_{\varphi_y}\,d\mu(y)\). Fullness uses only DI-08's unconditional implication from full fibres to a full integral. Its represented left von Neumann algebra is \(N=\int_Y^\oplus\pi_y(M_y)\,d\mu(y)\); the prescribed concrete algebra \(M_K=\int_Y^\oplus M_y\,d\mu(y)\) initially acts on the different integral of the \(K_y\).

There is an actual global identification. GFR-08 in both directions preserves measurable operator sections, and each \(\pi_y\) preserves the operator norm. Hence \(\Pi(a)_y=\pi_y(a_y)\) defines a bijective isometric star-isomorphism \(M_K\to N\) on the essentially bounded fields. Both are von Neumann algebras by the actual decomposition constructions. This isomorphism and its inverse are normal: they preserve all suprema of bounded increasing nets by their order isomorphism, as in NP-06. We identify the prescribed algebra through \(\Pi\), rather than assuming the two Hilbert fields are identical, and write

\[
 M=\int_Y^\oplus M_y\,d\mu(y)
 \quad\text{represented on }H\text{ through }\Pi .
 \tag{MW.14}
\]

The associated weight on \(N\) is pulled back by \(\Pi\). This normal identification preserves faithfulness, semifiniteness and the full weight domain.

The algebra sections have square-integrable vectors and sharp images, fibrewise algebra membership, and essentially bounded left multipliers. Completion of their closed sharp graph does not retain that multiplier bound as an extra restriction on its operator domain. WH-05–08 define the associated faithful normal semifinite weight \(\Phi\) on \(M\). This is Definition VIII.4.6:

\[

\Phi=\int_Y^\oplus\varphi_y\,d\mu(y).

\tag{MW.15}

\]

The Tomita integral used in the source is equivalent to this left integral after full completion by DI-10–12; WH-08 and the full recovery in WH-11 identify their associated weights. In this comparison DI-11 uses its corrected complex-power membership and product-density argument at the exact existing inputs. That author correction does not close its independent or transitive review; those obligations remain inputs here as well. We are therefore specifying the full source construction, rather than choosing a smaller algebra of convenient simple sections.

Here are the actual modular domains. DI-02/03/06 give

\[

S=\int_Y^\oplus S_y\,d\mu(y),\qquad

D(S)=\left\{\xi:\xi_y\in D(S_y)\text{ a.e.},\ \int_Y\|S_y\xi_y\|^2d\mu<\infty\right\},

\tag{MW.16}

\]

where membership in \(H\) already means \(\int\|\xi_y\|^2<\infty\). The adjoint is the integral of the \(F_y=S_y^*\), with its own full square-integrability domain. Linearization through conjugate Hilbert fields handles the antilinear maps. Their polar operators satisfy

\[

J=\int_Y^\oplus J_y\,d\mu(y),\quad

\Delta=\int_Y^\oplus\Delta_y\,d\mu(y),\quad

D(\Delta)=\left\{\xi:\xi_y\in D(\Delta_y)\text{ a.e.},\ \int_Y\|\Delta_y\xi_y\|^2d\mu<\infty\right\}.

\tag{MW.17}

\]

For completeness, the integral closed form \(\|S\xi\|^2=\int\|\Delta_y^{1/2}\xi_y\|^2\) identifies its representing positive operator with the displayed \(\Delta\), by QF-03 and the full integral resolvent/domain theorem DI-02. The integral of the polar antiunitaries is an everywhere defined antiunitary, and \(S=J\Delta^{1/2}\) on its entire form domain. Polar uniqueness identifies it with the GNS modular conjugation.

The bounded resolvent \((1+\Delta)^{-1}\) is the integral of the fibre resolvents. Polynomial, continuous and bounded Borel spectral convergence, as in SK-04/05 and DI-01, show that the same is true of bounded Borel functions of \(\Delta\). Each \(\Delta_y\) is injective, so \(\Delta\) is injective. In particular

\[

\Delta^{it}=\int_Y^\oplus\Delta_y^{it}\,d\mu(y),\qquad

\sigma_t^\Phi(x)_y=\sigma_t^{\varphi_y}(x_y).

\tag{MW.18}

\]

The fibre imaginary powers have norm one; dominated convergence proves strong continuity of the integrated unitaries. The operator fields on the right are measurable and have the same essential bound as \(x\). MF-06's implementation proves equality on the whole integral algebra. These full GNS and modular descriptions are elaborations of the construction, not additional numbered assertions being attributed to the source's Theorem 4.7.

## Every positive value and the exact finite left ideal

For \(x\in M_+\), represented by the essentially bounded positive field \(x_y\), we prove

\[

\Phi(x)=\int_Y\varphi_y(x_y)\,d\mu(y)

\tag{MW.19}

\]

with extended nonnegative values. MW-02 has already established measurability of the integrand. It remains to justify both finite directions.

If \(\Phi(x)<\infty\), the full weight/Hilbert-algebra correspondence supplies a vector \(\xi\in\mathcal A\) with \(L_\xi=x^{1/2}\), \(S\xi=\xi\), and \(\|\xi\|^2=\Phi(x)\). DI-04 and DI-09 identify its multiplier field. Uniqueness of direct-integral operator fields gives \(L_{\xi_y}=x_y^{1/2}\) a.e. The fibre weight correspondence then gives \(\varphi_y(x_y)=\|\xi_y\|^2\). Integrating proves (MW.19) in this direction.

Conversely, suppose the right side of (MW.19) is finite. On the conull finite set put \(\xi_y=\Lambda_y(x_y^{1/2})\). MW-03 proves its measurability. Its squared norm is precisely the integrand, so it is an integrated Hilbert vector. Moreover \(\xi_y\in\mathcal A_y\), \(S_y\xi_y=\xi_y\), and \(L_{\xi_y}=x_y^{1/2}\). Its sharp image is square integrable, and these multipliers have the common essential bound \(\|x\|^{1/2}\). Thus \(\xi\in\mathcal A\), \(L_\xi=x^{1/2}\), and WH's defining weight formula gives (MW.19). If one of the two sides is infinite and the other finite, the corresponding finite direction just proved is contradicted. Therefore both infinite values also agree. This is the entire assertion (ii) of Theorem VIII.4.7.

In particular the complete finite left ideal is

\[

\mathfrak n_\Phi=\left\{a\in M:\int_Y\varphi_y(a_y^*a_y)\,d\mu(y)<\infty\right\},\qquad

\Lambda_\Phi(a)_y=\Lambda_y(a_y).

\tag{MW.20}

\]

The first equality follows by applying (MW.19) to \(a^*a\). For the vector identity, MW-03 supplies the measurable field on its finite set, and (MW.20)'s integral makes it square integrable. For every section of the global right algebra, mixed multiplication holds fibrewise. The essentially bounded operator field \(a_y\) therefore acts on that right-algebra vector by the bounded operator \(a\); equivalently the integrated vector has left multiplier \(a\). WH-08's GNS identification and uniqueness prove the second equality. This argument includes finite left-ideal elements whose adjoints are not finite; it does not replace \(\mathfrak n_\Phi\) by the smaller finite-star algebra.

The positive formula alone now verifies all weight axioms as well: additivity and scalar multiplication hold pointwise and pass through nonnegative integration; normality for arbitrary bounded increasing nets is already supplied by the associated-weight construction, so it does not rely on a sequential interchange of an arbitrary uncountable supremum with a scalar integral. Faithfulness and semifiniteness likewise come from the full Hilbert algebra. This order of proof preserves the general net scope.

## Scalar examples and the cutoff convention

On \(Y=\mathbb R\) with Lebesgue measure, take \(M_y=\mathbb C\) and \(\varphi_y(z)=z\) for \(z\geq0\). Enumerate \(\mathbb Q(i)\) as the constant fields \(x_j\). They form the required pointwise finite-adjoint core, with measurable coefficients, while each nonzero constant has infinite global squared GNS norm. The weight field is nonetheless measurable, and \(\Phi(f)=\int_{\mathbb R}f(y)\,dy\). Finite-measure localizations give actual integrated algebra sections; the definition never required the original test fields to be globally square integrable.

On \(Y=(0,1]\), let \(\varphi_y(z)=y^{-2}z\) on \(\mathbb C_+\). The fields \(q_jy^2\), with \(q_j\) enumerating \(\mathbb Q(i)\), form a pointwise graph-dense finite-star core. Identify \(H_{\varphi_y}=\mathbb C\) by \(\Lambda_y(z)=z/y\). For the bounded positive field \(x_y=y^\alpha\), \(\alpha\geq0\),

\[

\varphi_y(x_y)=y^{\alpha-2},\qquad

\Lambda_y(x_y^{1/2})=y^{\alpha/2-1},\qquad

\Phi(x)=\begin{cases}(\alpha-1)^{-1},&\alpha>1,\\\infty,&0\leq\alpha\leq1.\end{cases}

\tag{MW.21}

\]

All fibre values are finite. Global finiteness is exactly square-integrability of the displayed GNS field. In particular \(\alpha=1\) is a genuine boundary value with logarithmic divergence; \(\alpha=2\) gives value one and \(\alpha=3\) gives one half. The sharp is conjugation and all modular operators and automorphisms are the identity in this commutative example.

The exact truncated integral is

\[

\int_\varepsilon^1 y^{\alpha-2}dy

=\begin{cases}
(1-\varepsilon^{\alpha-1})/(\alpha-1),&\alpha\ne1,\\
-\log\varepsilon,&\alpha=1.
\end{cases}

\tag{MW.22}

\]

**Problem: does an arbitrary total right sequence justify the printed identity cutoff?** No. In the scalar right algebra, \(\eta_j=2^{-j}\) is total by linear span, but the finite-subset sums tend to \(1/3\), and \(h(1+h)^{-1}\) tends to \(1/4\). This family is not dense as a set in the graph norm. Adjoin rational combinations or the explicitly dense contraction family and its integer multiples as in MW-02. The resulting countable data meet the stronger density, and (MW.9) explains the all-positive recovery. This is a convention repair, not a refutation of Theorem VIII.4.7 under its full printed hypotheses.

**Problem: why is measurable operator inversion insufficient for GNS inversion?** The GNS map is not the operator-field map \(x\mapsto x^{-1}\), and its domain is an unbounded finite ideal. A fibrewise existence assertion does not produce a measurable vector. MW-03 instead uses the measurable injective operator \(K_y\), its uniformly bounded regularized inverses at each fixed \(n\), and a norm limit on the previously verified finite set. This retains the complete finite left ideal.

## Central disintegration of a separable weighted algebra

Let \(M\) be a separably acting von Neumann algebra with a faithful normal semifinite weight \(\varphi\), and let \(D\subseteq Z(M)\) be any unital von Neumann subalgebra. We prove Theorem VIII.4.8 at the exact field-comparison and central/selection prerequisites already declared. At a fixed actual measure its fibre weights are unique up to the specified almost-everywhere algebra identifications. Under equivalent changes of base measure, weighted uniqueness includes the inverse Radon–Nikodym rescaling proved below, with the prescribed diagonal algebra retained.

For the zero algebra use the empty base and zero Hilbert space. Otherwise, first the GNS space of \(\varphi\) is separable. In a faithful concrete representation on a separable Hilbert space \(K\), choose a countable total unit-vector family and strictly positive summable coefficients of total one. Their vector-state sum is a faithful normal state \(\omega\). On the unit ball of \(M\), the strong topology embeds into a countable product of separable Hilbert spaces, so it has a countable dense set. Strong approximation on this bounded ball gives approximation in the \(\omega\)-GNS norm, by the defining summable vector series and its uniform tail bound. Integer rescalings give a countable dense set in \(H_\omega\). SF's canonical GNS standard forms and SE-10's comparison for the identity of \(M\) now give a unitary from \(H_\varphi\) to \(H_\omega\). Thus \(H_\varphi\) is separable; this does not assume \(\varphi(1)<\infty\).

Apply DI-13 to the full left Hilbert algebra of \(\varphi\) and the specified central subalgebra \(D\). At its exact CENTRAL and SELECTION contracts, this gives a standard sigma-finite base and a measurable field of full left Hilbert algebras \(\mathcal A_y\), with

\[

\mathcal A_\varphi=\int_Y^\oplus\mathcal A_y\,d\mu(y),\qquad

M=\int_Y^\oplus M_y\,d\mu(y),\qquad D=L^\infty(Y,\mu)\text{ diagonally}.

\tag{MW.23}

\]

Associate the faithful normal semifinite weights \(\varphi_y\) by WH-05–08. Their reverse comparison requires a constructed compatible GNS realization. Here \(M_y=L(\mathcal A_y)''\) acts on the already specified measurable field \(H_y\). The canonical WH-08 unitary \(U_y:H_{\varphi_y}\to H_y\) is characterized by \(U_y\Lambda_{\varphi_y}(L_a)=a\), for \(a\in\mathcal A_y\). Pull the actual GNS field structure back along these maps: if \(h_j\) is a known fundamental Hilbert family, the vectors \(U_y^{-1}h_j\) have its measurable Gram matrix, so DF-01 defines a measurable structure on the actual \(H_{\varphi_y}\). DF-05 then proves that \(U_y\) and \(U_y^{-1}\) are measurable by their actions on these fundamental families. This construction does not infer measurability of an arbitrary fibrewise unitary.

The canonical representation satisfies \(\pi_y(c)=U_y^{-1}cU_y\), since that equality holds on the dense algebra vectors. Conjugation by these measurable unitaries makes the inverse operator transport \(B_y\mapsto U_yB_yU_y^{-1}\) measurable by DF-05, even with varying fibre bounds. The pulled-back algebra fundamental family \(U_y^{-1}a_j\) has measurable sharp images and products and is a set dense in the sharp graph norm, because WH-08 intertwines the actual full algebra and its closed involution. Thus every hypothesis of GFR-10 is supplied, and its reverse argument proves that \(\varphi_y\) is a measurable weight field on the represented \(M_y\). The integrated full algebra is the original one; WH-08 and WH-11 recover the original weight, giving

\[

(M,\varphi)=\int_Y^\oplus(M_y,\varphi_y)\,d\mu(y).

\tag{MW.24}

\]

MW-05 determines every positive value and the whole finite left ideal of this equality. MW-04 also supplies the full GNS and modular decompositions.

**Uniqueness over a fixed actual measure.** First compare two decompositions on the same standard sigma-finite space \((Y,\mu)\), with the same specified diagonal identification. Their canonical global GNS map preserves the full Hilbert-algebra product, sharp and inner product, by WH-08/11 and (MW.20). It intertwines multiplication by every \(f\in L^\infty(Y,\mu)\). DC-10, proved by applying DF-08 to the off-diagonal block on the sum field, therefore disintegrates this given map into measurable fibre unitaries. Pull the second full algebra field back along those unitaries. Its integral is literally the first full algebra in the same Hilbert integral, so DI-14(1) identifies the two full fibre algebras almost everywhere. The induced normal star-isomorphisms of their left von Neumann algebras preserve multiplication-vector norms. WH's associated-weight construction consequently preserves the finite positive cone and every finite value; the other positive values are infinity in both weights. This proves weighted uniqueness at the fixed measure, including all positive inputs. It uses the reconstructed global GNS map, rather than a selection of arbitrary abstract fibre isomorphisms.

**Changing the measure requires changing the fibre weights.** After transporting the bases through the specified measure-class identification of DC-11, write both fields on \(Y\). If \(\nu\) and \(\mu\) are equivalent sigma-finite measures, their Radon–Nikodym derivative \(r\) satisfies \(0<r(y)<\infty\) almost everywhere. For a given decomposition with weights \(\varphi_y\) over \(\mu\), the corresponding weights over \(\nu\) are

\[
 \begin{gathered}
 d\nu=r\,d\mu,\\
 \psi_y=r(y)^{-1}\varphi_y.
 \end{gathered}
 \tag{MW.25}
\]

This rescaling preserves faithfulness, normality and semifiniteness in each fibre. It leaves both finite ideals unchanged. The graph norm in (MW.1) is multiplied by \(r(y)^{-1/2}\), and both Gram matrices of any original countable core are multiplied by \(r(y)^{-1}\). That core remains a measurable set dense for the rescaled graph norm on every fibre. MW-01 and the compatible GNS construction therefore give the actual measurable field for \(\psi_y\), including varying dimensions and zero fibres. Neither a uniform bound on \(r\) nor one on its reciprocal is needed.

On the common finite left ideal define \(I_y\Lambda_{\varphi_y}(a)=\Lambda_{\psi_y}(a)\). Its exact norm is \(r(y)^{-1/2}\) on nonzero fibres; it extends to an invertible bounded map on each fibre. Its restriction to the common finite-adjoint algebra preserves multiplication and sharp. The maps and their inverses are measurable by their actions on the two fundamental GNS families and DF-05. The fibre map \(V_y=r(y)^{1/2}I_y\) is unitary. For vectors in that finite-adjoint algebra it is generally not multiplicative: \(V_y(\xi\eta)=r(y)^{1/2}I_y(\xi\eta)\), whereas \((V_y\xi)(V_y\eta)=r(y)I_y(\xi\eta)\). Thus this unitary cannot be used as a Hilbert-algebra isomorphism without the measure compensation.

That compensation occurs in the actual global map \((U\xi)_y=I_y\xi_y\), from the \(\varphi\)-GNS integral over \(\mu\) to the \(\psi\)-GNS integral over \(\nu\). With \(g(y)=\|\xi_y\|^2\), its norm identity is

\[
 \begin{gathered}
 \|U\xi\|_{\nu}^{2}\\
 =\int_Y r^{-1}g\,d\nu\\
 =\int_Y g\,d\mu\\
 =\|\xi\|_{\mu}^{2}.
 \end{gathered}
 \tag{MW.26}
\]

The inverse maps give surjectivity. The same identity applies to sharp images. Conjugation by \(I_y\), equivalently by the unitary \(V_y\), preserves each left-multiplier norm. Thus all three integral-algebra conditions of DI-06 are preserved, and \(U\) is a global unitary Hilbert-algebra isomorphism. MW-05 also gives \(\int_Y\psi_y(x_y)\,d\nu=\int_Y\varphi_y(x_y)\,d\mu\) for every positive field, including infinite values. The integral weight and its complete finite left ideal are unchanged.

For two initially given decompositions with weights \(\varphi_y\) over \(\mu\) and \(\psi_y\) over \(\nu\), normalize the second one to weights \(\widehat\psi_y=r(y)\psi_y\) over \(\mu\). The preceding construction, in the inverse direction, preserves its global full algebra and weight. Apply fixed-measure uniqueness to \(\varphi_y\) and \(\widehat\psi_y\). The resulting measurable algebra identifications \(\beta_y:M_y\to N_y\) satisfy

\[
 \begin{gathered}
 \psi_y(\beta_y(a))\\
 =r(y)^{-1}\varphi_y(a),\\
 a\in M_y^+.
 \end{gathered}
 \tag{MW.27}
\]

almost everywhere, with equality also for infinite values. The full associated-weight identification establishes this for the whole positive cone on the same conull fibres; it does not take an uncountable union of exceptional sets. This proves uniqueness under simultaneous base transport and inverse-density rescaling, retaining the general measure-class scope of the decomposition theorem. DI-14 is applied only after the two actual measures have been made equal.

**One-point check.** Let \(M=D=\mathbb C\) and let the global weight be \(\Phi(z)=z\) for \(z\geq0\). The base of mass one with fibre weight \(\varphi(z)=z\), and the base of mass two with fibre weight \(\psi(z)=z/2\), have the same diagonal algebra, measure class and integrated weight. Here \(r=2\), as in (MW.25). The only complex unital star-automorphism of \(\mathbb C\) is the identity, so the two unrescaled fibre weights are not weight-preservingly isomorphic. The unitary between their weighted fibre Hilbert spaces is \(a\mapsto\sqrt2\,a\), whose value on \(1\cdot1\) is \(\sqrt2\), while the product of its values on the two factors is \(2\). It is not multiplicative. The globally multiplicative map is the identity on algebra vectors with the compensated base measure, as in (MW.26). This example detects the omitted normalization convention; it does not refute the intended source disintegration theorem.

The source map is exact: MW-01 states Definition VIII.4.4 and uses the full compatible comparison in GFR-01–10; MW-04 constructs Definition 4.6 with the explicit global representation \(\Pi\); MW-02/03/05 proves both clauses of Theorem 4.7, including all infinite values and the complete finite left ideal; MW-07 proves Theorem 4.8 at the precise central-decomposition inputs and constructs its compatible GNS realization. The source pages are printed 134–137/PDF 154–157, with set graph density checked on VI.3.1, printed 28/PDF 48. DF, DC and corrected SCF supply original author arguments for their actual DI consumers. No unrestricted DI-08 converse is used or proved.

