# Measurable Hilbert fields and their diagonal commutant

**Self-checked by the writing AI.**

A Hilbert field needs a specified measurable structure. Fibrewise isometries alone do not determine one. We construct the structure from countable Gram data, choose measurable orthonormal bases through changing dimensions, and realize the fibres as closed subspaces of one ambient Hilbert space. We then construct the exact Hilbert direct integral and prove that commuting with all scalar multiplication operators is equivalent to being a bounded decomposable operator. The last proof constructs the fibre operators explicitly from countably many localized vectors.

The human antecedent is M. Takesaki, *Theory of Operator Algebras I*, IV.8: Definition 8.9, Lemmas 8.10 and 8.12, Theorem 8.13, Definitions 8.14–8.15, and Corollary 8.16, printed 269–273/PDF 276–280. The governing page images were actually inspected. The calculations below are independently written alternative derivations of the shared foundation statements identified next. They supply every clause of the course's existing FIELD contract; they do not supply central disintegration existence, the other SELECTION coding constructions, or by themselves the compatible GNS representation transport for VIII.4.5. The latter is constructed from these Hilbert-field tools in Two Gram fields before measurability of the involution through Forward and inverse transport by least indices.

**Foundation statements.** Each shared clause below is proved in an existing programme lesson. Measurable fields of Hilbert spaces and their direct integrals supplies the eight HF clauses; Decomposable operators and the diagonal algebra supplies the diagonal-commutant clause. The retained calculations are alternative derivations in our notation.

| Local argument | Exact foundation statement |
| --- | --- |
| DF01–02 | Theorem 3.1 |
| DF03, dimension strata only | Theorem 5.1 |
| DF04, specified subfields | Proposition 4.1 |
| DF04, conjugates and finite sums | Proposition 7.1 |
| DF05 | Theorem 6.2 |
| DF06, completeness and subsequences | Theorem 8.2 |
| DF06, localization and qualified separability | Theorem 9.1 |
| DF07, essentially bounded integration | Theorem 10.1 |
| DF08 | Theorem 5.1 |

These foundation statements are stated over arbitrary sigma-finite measure spaces, with no standardness or global separability requirement. The field-only constructions in DF01–05 work over any measurable base by the proofs retained here. The abstract Gram-quotient construction, the distance-to-projection proof of the Effros criterion, countable sums, nonuniform bounded-fibre integral domains and adjoints, and the examples are retained local mechanisms. The dimension-stratum clause of DF03 imports no Effros converse. This imports precise statements rather than a whole lesson; in particular DF has no dependency on its DI consumer.

Inner products are linear in the first variable. DF-01–05 work over any measurable base \((Y,\Sigma)\). When a measure is used, measurability is with respect to its completion; countably many exceptional sets may be removed together. DF-06 onward assume an arbitrary sigma-finite measure space \((Y,\Sigma,\mu)\). Fibres are separable complex Hilbert spaces, including dimension zero and infinite dimension. The named elementary inputs are Hilbert completion, orthogonal projection and Riesz representation, scalar monotone convergence and scalar \(L^2\) completeness, and, only for global separability, countable generation of the sigma-algebra modulo null sets (as on a standard Borel space). These are the existing OPEN Hilbert/spectral and scalar-integration inputs with their current course statuses. The retained alternative derivations use no direct-integral, central-decomposition or measurable-selection theorem as a proof input; the shared statement imports are exactly the clauses listed above.

## Countable Gram data determines the whole measurable structure

**Alternative derivation of HF Theorem 3.1(3)–(4).** Let \(H_y\) be Hilbert spaces and let \(h_j(y)\), \(j\geq1\), have complex linear span dense in every fibre. Assume each scalar function

\[
 g_{jk}(y)=\langle h_j(y),h_k(y)\rangle
 \tag{DF.1}
\]

is measurable. Define a section \(\xi\) to be measurable when all \(\langle\xi(y),h_j(y)\rangle\) are measurable. This definition has the maximality property: testing against every measurable section, or just against the \(h_j\), gives the same class.

Enumerate the finite \(\mathbb Q(i)\)-linear combinations of the \(h_j\) as \(d_l\). Their values are fibrewise dense. For any \(\xi(y)\),

\[
 \|\xi(y)\|=
 \sup_l\frac{|\langle\xi(y),d_l(y)\rangle|}{\|d_l(y)\|},
 \qquad \frac00:=0.
 \tag{DF.2}
\]

The upper bound is Cauchy–Schwarz. For a nonzero \(\xi\), approximate \(\xi\) by the dense \(d_l\); the displayed quotients tend to \(\|\xi\|\). Thus measurable sections have measurable norms. They are closed under addition, measurable scalar multiplication, countable measurable pasting, and fibrewise norm limits: the defining scalar tests have these properties. Polarization of their measurable squared norms proves that the scalar product of any two measurable sections is measurable. Consequently a section whose scalar products against all measurable sections are measurable belongs to the class, because the fundamental \(h_j\) belong to it. This proves the field axioms and the stated maximality.

There is also a construction when the fibres are not given beforehand. Suppose measurable functions \(g_{jk}\) are Hermitian and every finite matrix \((g_{jk}(y))\) is positive semidefinite. On finitely supported complex sequences set

\[
 \langle c,d\rangle_y=
 \sum_{j,k}c_j\overline{d_k}g_{jk}(y).
 \tag{DF.3}
\]

Quotient by its zero-norm subspace and complete. Positivity and Cauchy–Schwarz make the quotient well defined. The images of the standard coordinate vectors are the \(h_j(y)\); their rational span is dense, so the completion is separable. Equation (DF.1) and the preceding argument provide its measurable structure. A zero Gram matrix produces the zero fibre. This is the complete Gram construction; no uniform positive lower bound on the matrices is assumed. \(\square\)

## Compact orthonormal frames and measurable dimension

**Alternative derivation of HF Theorem 3.1(1)–(2).** We construct sections \(e_n\) whose nonzero values form the first \(\dim H_y\) members of an orthonormal basis. This avoids leaving zeros in the middle of a basis when an early input becomes dependent.

Assume \(e_1,\ldots,e_{n-1}\) have been constructed. Define

\[
 r_{nj}(y)=h_j(y)-\sum_{i<n}
       \langle h_j(y),e_i(y)\rangle e_i(y),
 \quad
 E_n=\bigcup_{j\geq1}\{y:\|r_{nj}(y)\|>0\}.
 \tag{DF.4}
\]

Residuals and their norms are measurable by DF-01. On \(E_n\), let \(j_n(y)\) be the least index with positive residual norm, and put

\[
 e_n(y)=\frac{r_{n,j_n(y)}(y)}{\|r_{n,j_n(y)}(y)\|};
 \qquad e_n(y)=0\quad(y\notin E_n).
 \tag{DF.5}
\]

The event \(\{j_n=j\}\) is the positive-norm event minus the union of the earlier such events, a finite measurable union. Countable measurable pasting proves that \(e_n\) is measurable. It has norm one on \(E_n\), and is orthogonal to all earlier nonzero outputs. Density of the \(h_j\) gives

\[
 E_n=\{y:\dim H_y\geq n\},\qquad
 E_{n+1}\subseteq E_n.
 \tag{DF.6}
\]

If the process stops after \(n\) steps, all \(h_j(y)\) lie in their span, which is therefore the whole fibre. If it does not stop, each original \(h_j(y)\) is eventually included in the span: before that happens the least remaining eligible index is at most \(j\), so only finitely many smaller indices can precede it. Thus the infinite outputs are total as well. Dimension-zero fibres lie outside \(E_1\). Finite dimension \(n\) is the measurable stratum \(E_n\setminus E_{n+1}\); infinite dimension is \(\bigcap_n E_n\).

Every vector has the expansion

\[
 \xi(y)=\sum_{n\geq1}\xi_n(y)e_n(y),
 \qquad \xi_n(y)=\langle\xi(y),e_n(y)\rangle,
 \qquad \|\xi(y)\|^2=\sum_n|\xi_n(y)|^2.
 \tag{DF.7}
\]

A section is measurable exactly when these coordinates are measurable. The forward direction follows from DF-01. In the reverse direction, the finite sums are measurable and converge in each fibre. Each coordinate vanishes off \(E_n\). Conversely, any sequence of measurable coordinates with that support property and pointwise finite squared sum defines a measurable section. This also proves uniqueness of the measurable structure generated by the given fundamental family. \(\square\)

## Ambient realization and the Effros closed-subspace condition

**The dimension-stratum clause of HF Theorem 5.1.** Let \(\ell^2\) have fixed basis \(\delta_n\), and define the fibre isometry

\[
 U_y:H_y\longrightarrow\ell^2,
 \qquad U_y\xi=\sum_n\xi_n(y)\delta_n.
 \tag{DF.8}
\]

Its range is the closed subspace \(F_y\) spanned by the \(\delta_n\) with \(y\in E_n\). The projection onto it has coordinates \(P_y\delta_n=\mathbf1_{E_n}(y)\delta_n\); hence it sends every fixed vector to a measurable \(\ell^2\)-valued section. A section \(\xi\) is measurable exactly when \(U_y\xi(y)\) is measurable in the fixed ambient space, by DF-02.

We prove the general closed-subspace measurability criterion, including its reverse direction. The Effros sigma-algebra on closed subspaces of a separable Hilbert space \(K\) is generated by the events

\[
 \{F:F\cap O\ne\varnothing\},\qquad O\subseteq K\text{ open}.
 \tag{DF.9}
\]

For a field \(F_y\), the following conditions are equivalent: its subspace map is Effros measurable; each distance \(d(v,F_y)\), for fixed \(v\in K\), is measurable; and each projection vector \(P_yv\) is measurable. For the first implication, \(d(v,F_y)<r\) is precisely the event that \(F_y\) meets the ball of radius \(r\) about \(v\). Conversely, every open set is a union of countably many balls from a fixed countable rational-ball base. Its hit event is the corresponding union of events \(d(q,F_y)<r\). This proves equivalence of the first two conditions.

To construct the projection from distances, fix a countable dense sequence \(q_j\) in \(K\) and \(\varepsilon_m=1/m\). For fixed \(v\), set \(d_y=d(v,F_y)\), and choose the least \(j=j_m(y)\) satisfying

\[
 d(q_j,F_y)<\varepsilon_m,
 \qquad \|q_j-v\|^2<d_y^2+\varepsilon_m.
 \tag{DF.10}
\]

Such indices exist: approximate the actual projection \(P_yv\) closely by a \(q_j\). Both tests are measurable, so the least-index choice is a measurable function. For estimating its error, choose a point \(z\in F_y\) with \(\|z-q_{j_m}\|<2\varepsilon_m\). This point is used only in the fibrewise estimate; no measurable selection of it is asserted. Orthogonal projection gives

\[
 \begin{split}
 \|z-P_yv\|^2
 &=\|z-v\|^2-d_y^2\\
 &<\varepsilon_m+4\varepsilon_m\sqrt{d_y^2+\varepsilon_m}
                  +4\varepsilon_m^2.
 \end{split}
 \tag{DF.11}
\]

Since \(d_y\leq\|v\|\), it follows that \(q_{j_m(y)}\to P_yv\) in norm, even with a bound depending only on \(\|v\|\) and \(m\). The approximants are countably pasted fixed vectors, so the projection vector is measurable. Conversely, a measurable projection gives measurable distances by \(d(v,F_y)=\|v-P_yv\|\).

If a field of closed subspaces \(F_y\subset K\) is Effros measurable, take \(P_y\delta_n\) for a fixed orthonormal basis of \(K\). These are measurable and total in each subspace. They define its Hilbert field by DF-01; a vector field in the subspaces is measurable exactly when it is measurable as a \(K\)-valued field. Indeed ambient measurability tests its scalar products against the \(P_y\delta_n\), while the reverse follows from the coordinate expansions of DF-02 in the ambient space.

This proves both directions of the full ambient-realization statement of source Theorem IV.8.13. Its field-level argument does not require sigma-finiteness. A different fixed infinite-dimensional separable ambient Hilbert space is obtained by a fixed unitary identification. The proof uses countable rational approximants, not a measurable-selection theorem. \(\square\)

## Subfields, projections, conjugates and direct sums

**Alternative derivations of HF Proposition 4.1 and Proposition 7.1(1)–(2).** Suppose measurable sections \(b_j(y)\in H_y\) have closed span \(K_y\). Apply DF-02 to their span; denote its compact orthonormal frame by \(f_n\). For any measurable \(\xi\),

\[
 Q_y\xi(y)=\sum_n\langle\xi(y),f_n(y)\rangle f_n(y)
 \tag{DF.12}
\]

is measurable by finite sums and fibrewise limits. The usual orthonormal expansion proves that \(Q_y\) is precisely the orthogonal projection onto \(K_y\), and \(\|Q_y\|\leq1\). The measurable structure intrinsic to the subfield agrees with that induced from \(H_y\): a section in \(K_y\) is measurable if and only if its frame coordinates are measurable, which is also equivalent to the ambient scalar tests. The orthogonal complements form a measurable field with fundamental family \((1-Q_y)h_j(y)\). This proves the projection clause for all subspaces with specified measurable fundamental sections, including changing ranks.

The conjugate space \(\overline H_y\) is defined by conjugating scalar multiplication and setting

\[
 \langle\overline\xi,\overline\eta\rangle_{\overline H_y}
   =\overline{\langle\xi,\eta\rangle_{H_y}}.
 \tag{DF.13}
\]

Its fundamental family is \(\overline{h_j}\). The canonical conjugation \(\kappa_y:\xi\mapsto\overline\xi\) is antiunitary and preserves measurable sections in both directions, by the conjugate scalar tests. A conjugate-linear operator becomes a linear map \(\overline H_y\to K_y\) by composition with \(\kappa_y^{-1}\); the domain and measurability tests remain typed between these two fields.

For two fields, \(H_y\oplus K_y\) has fundamental family \((h_j,0),(0,k_j)\). Its measurable sections are exactly pairs of measurable sections, since testing each of these families tests the two components separately. The same construction works for countable Hilbert direct sums: test the countably many component fundamental vectors, and require the pointwise sum of squared component norms to be finite. Scalar products, coordinate projections and inclusions are measurable. These are fibre Hilbert sums, prior to integration over the base. \(\square\)

## Pointwise bounded operator fields, adjoints and exact norm tests

**Alternative derivation of HF Theorem 6.2.** Let \(T_y:H_y\to K_y\) be bounded on each fibre. The bound may depend on \(y\) and may have infinite essential supremum. The operator field is measurable exactly when \(T_yh_j(y)\) is measurable for every fundamental \(h_j\). Equivalently, it suffices to test a compact orthonormal frame \(e_n\) of the domain. To prove sufficiency, write any measurable input in the expansion (DF.7); the images of its finite sums are measurable. On a fixed fibre, boundedness of \(T_y\) makes these images converge to \(T_y\xi(y)\). DF-01 makes their limit measurable. No common bound was used.

For compact orthonormal frames \(e_n\) and \(f_m\), a measurable field has measurable matrix coefficients. Its adjoint is measurable, because for every \(m\),

\[
 T_y^*f_m(y)=\sum_n
    \langle f_m(y),T_ye_n(y)\rangle e_n(y).
 \tag{DF.14}
\]

Each finite sum is measurable. Fibrewise Riesz representation and Parseval give norm convergence to the displayed adjoint vector. The inner-product order in (DF.14) is dictated by the first-variable-linear convention. Testing the \(f_m\) now proves measurability of \(T_y^*\).

Let \(v_l(y)\) enumerate all finite \(\mathbb Q(i)\)-linear combinations of the \(e_n(y)\). Then

\[
 \|T_y\|=\sup_l
  \frac{\|T_yv_l(y)\|}{\|v_l(y)\|},
 \quad\text{with the ratio zero when }v_l(y)=0.
 \tag{DF.15}
\]

Density of those vectors in the fibre proves equality; testing single basis vectors alone would not in general give the operator norm. Thus \(y\mapsto\|T_y\|\) is measurable. Sums, scalar multiples and composable products of measurable fields are measurable by their actions on sections. Fibrewise strong limits of pointwise bounded operators are measurable when the limits exist as bounded operators on every fibre under consideration. These assertions also hold between two different fields and at zero fibres. \(\square\)

## The Hilbert direct integral, localization and subsequences

**Alternative derivations of HF Theorems 8.2 and 9.1.** Now let \(\mu\) be sigma-finite. Define \(H=\int_Y^\oplus H_y\,d\mu(y)\) to consist of equivalence classes, modulo equality almost everywhere, of measurable sections with finite squared-norm integral. Its inner product is

\[
 \langle\xi,\eta\rangle_H
   =\int_Y\langle\xi(y),\eta(y)\rangle\,d\mu(y),
 \qquad \|\xi\|_H^2=\int_Y\|\xi(y)\|^2\,d\mu(y).
 \tag{DF.16}
\]

Scalar Cauchy–Schwarz makes the inner-product integral absolutely convergent. The coordinate map (DF.7) gives an isometric identification

\[
 H\cong\bigoplus_{n\geq1}L^2(E_n,\mu),
 \qquad \xi\longmapsto(\xi_n)_n.
 \tag{DF.17}
\]

Here \(L^2(E_n)\) is understood as the subspace of \(L^2(Y)\) vanishing off \(E_n\). Monotone convergence identifies the integral of the coordinate squared sum with the sum of their integrals. Conversely, a family with finite total \(L^2\) squared norm has pointwise finite squared sum off one null set, again by monotone convergence. Choose measurable representatives, form the fibre expansions there, and set the section zero on the exceptional set. Altering countably many representatives changes the section only on their common null union. This proves surjectivity of (DF.17). Completeness follows from completeness of scalar \(L^2\) and its Hilbert countable sum, so (DF.16) constructs the actual Hilbert space.

Choose measurable finite-measure sets \(F_k\uparrow Y\). For any measurable section, each truncation

\[
 \mathbf1_{F_k\cap\{\|\xi(y)\|\leq m\}}\xi(y)
 \tag{DF.18}
\]

belongs to the direct integral, whether or not the original section does. These supports exhaust the points where the section is defined and finite. If \(\xi\in H\), dominated convergence gives norm convergence of successive such truncations to \(\xi\). Bounded measurable scalar multiplication with finite-measure support therefore provides the localization used below.

If the sigma-algebra is countably generated modulo null sets, the direct integral is separable. In particular this holds for a standard base. Choose a countable algebra generating the sigma-algebra modulo null sets and adjoin a countable finite-measure exhaustion. The finite-measure sets in this algebra, intersected with each \(E_n\), and rational complex coefficients give a countable dense family of scalar simple functions in \(L^2(E_n)\). To verify density, on each finite-measure exhaustion set the collection of sets whose indicators can be approximated is closed under complements and monotone countable unions, by scalar \(L^2\) convergence. It contains the generating algebra; the monotone-class theorem gives the sigma-algebra. Every measurable set agrees modulo a null set with a set in the generated sigma-algebra, by the countable-generation hypothesis. Exhausting the base and truncating functions finishes the scalar density proof. Finite coordinate sums in (DF.17) are then a countable dense family in \(H\). Countable generation is used only for this global separability assertion. No such condition is used for completeness, localization, subsequences, operator integration or the diagonal commutant.

Finally, if \(\xi_l\to\xi\) in \(H\), choose a subsequence \(l_j\) such that

\[
 \sum_j\|\xi_{l_j}-\xi\|_H^2<\infty.
 \tag{DF.19}
\]

Monotone convergence shows that the pointwise sum of the corresponding squared errors is finite almost everywhere. Those errors tend to zero in the fibre norms, so the subsequence converges fibrewise almost everywhere. A whole norm-convergent sequence need not converge pointwise; the chosen subsequence is the conclusion. The same proof applies to finitely many components by taking their Hilbert direct sum. \(\square\)

## Integrating operator fields: norm, domains and adjoints

**Alternative derivation of HF Theorem 10.1 for essentially bounded fields.** For a measurable \(T_y:H_y\to K_y\) with \(C=\operatorname*{ess\,sup}_y\|T_y\|<\infty\), set

\[
 T=\int_Y^\oplus T_y\,d\mu(y),\qquad
 (T\xi)(y)=T_y\xi(y).
 \tag{DF.20}
\]

Measurability is DF-05; the inequality \(\|T_y\xi(y)\|\leq C\|\xi(y)\|\) gives square integrability and \(\|T\|\leq C\). In fact

\[
 \|T\|=\operatorname*{ess\,sup}_y\|T_y\|,
 \qquad T^*=\int_Y^\oplus T_y^*\,d\mu(y).
 \tag{DF.21}
\]

For the lower bound, choose \(c<C\) with \(c\geq0\). By (DF.15), the positive-measure event \(\{\|T_y\|>c\}\) is a countable union of events on which a particular rational vector \(v_l\ne0\) has \(\|T_yv_l\|>c\|v_l\|\). Some such event has positive measure. Sigma-finiteness gives within it a measurable set \(A\) of finite positive measure. Use \(\xi(y)=\mathbf1_A(y)v_l(y)/\|v_l(y)\|\). Then \(\xi\in H\), and \(\|T\xi\|>c\|\xi\|\), since the squared pointwise inequality is strict on a positive-measure set. Taking \(c\uparrow C\) proves the norm equality. If \(C=0\), both norms are zero. For the adjoint, integrate \(\langle T_y\xi,\eta\rangle=\langle\xi,T_y^*\eta\rangle\); both integrals are absolutely convergent by scalar Cauchy–Schwarz. This gives the adjoint equality. Pointwise products and this identity also show that integration respects multiplication and adjoints for bounded decomposable fields of the appropriate types.

**Retained extension to nonuniform bounded-fibre fields.** If the essential supremum is infinite, define instead

\[
 \begin{split}
 D(T)&=\{\xi\in H:\int_Y\|T_y\xi(y)\|^2\,d\mu(y)<\infty\},\\
 (T\xi)(y)&=T_y\xi(y).
 \end{split}
 \tag{DF.22}
\]

Each fibre operator is still bounded on its own fibre. The domain is dense: for \(\xi\in H\), multiply it by \(\mathbf1_{\{\|T_y\|\leq m\}}\); the resulting vectors are in the domain and converge to \(\xi\). For closedness, if \(\xi_l\to\xi\) and \(T\xi_l\to\eta\) in the two global Hilbert spaces, DF-06 gives one subsequence converging to both limits fibrewise off a common null set. Boundedness of each \(T_y\) gives \(T_y\xi(y)=\eta(y)\). Hence \(\xi\in D(T)\) and \(T\xi=\eta\), proving closedness.

The adjoint of (DF.22) is the integral of the pointwise adjoints with its own exact domain:

\[
 D(T^*)=\{\eta\in K:\int_Y\|T_y^*\eta(y)\|^2\,d\mu(y)<\infty\}.
 \tag{DF.23}
\]

The displayed condition is sufficient by the integrated inner-product identity. For necessity, let \(T^*\eta=v\in H\). Test against \(\xi=\mathbf1_A e_n\), where \(A\subset F_k\cap\{\|T_y\|\leq m\}\). Such inputs belong to the domain. Localization of the integrated identity gives \(\langle e_n(y),T_y^*\eta(y)\rangle=\langle e_n(y),v(y)\rangle\) almost everywhere there. The scalar functions are integrable on these finite-measure sets by Cauchy–Schwarz and the local norm bound. One may obtain the pointwise equality by testing all measurable subsets, or by applying the identity to its positive and negative real and imaginary parts. Taking the countable union over \(k,m,n\) gives \(T_y^*\eta(y)=v(y)\) almost everywhere, because the frame is total. Since \(v\in H\), the displayed squared integral is finite. This proves (DF.23). No bounded global operator is inferred when the norm function has infinite essential supremum. \(\square\)

## The diagonal commutant is exactly the decomposable algebra

On \(H=\int_Y^\oplus H_y\,d\mu(y)\), let

\[
 D=\{M_f:f\in L^\infty(Y,\mu)\},\qquad
 (M_f\xi)(y)=f(y)\xi(y).
 \tag{DF.24}
\]

If zero fibres occur on a positive-measure set, this representation of \(L^\infty\) has a kernel there. The theorem concerns its represented image \(D\); no faithfulness on those zero fibres is assumed.

**Imported statement: DG Theorem 5.1.** A bounded operator \(B\in B(H)\) commutes with \(D\) if and only if there is a measurable field \(B_y\in B(H_y)\) with essentially bounded norm such that \(B=\int_Y^\oplus B_y\,d\mu(y)\). The field is unique almost everywhere, and its essential norm supremum is \(\|B\|\).

**Alternative proof by localized frame images.** A decomposable operator commutes with each scalar field pointwise, so first consider the converse. Partition the base into countably many measurable sets \(A_k\) of finite measure. The vectors \(\mathbf1_{A_k}e_n\) belong to \(H\). Commutation with \(M_{\mathbf1_{A_k}}\) makes their images under \(B\) supported on \(A_k\). Choose measurable representatives of these countably many images and paste them over the partition to obtain sections

\[
 b_n(y)=\bigl(B(\mathbf1_{A_k}e_n)\bigr)(y)
       \quad(y\in A_k).
 \tag{DF.25}
\]

Countable changes of representatives are harmless off one common null set.

Let \(a=(a_1,\ldots,a_N)\) have rational complex coordinates. Set \(u_a(y)=\sum_{n\leq N}a_ne_n(y)\) and \(w_a(y)=\sum_{n\leq N}a_nb_n(y)\). For every measurable \(E\subseteq A_k\), commutation with its characteristic multiplication operator gives

\[
 \int_E\|w_a(y)\|^2\,d\mu(y)
   =\|B(\mathbf1_Eu_a)\|^2
   \leq\|B\|^2\int_E\|u_a(y)\|^2\,d\mu(y).
 \tag{DF.26}
\]

Both integrands are integrable on \(A_k\): the first is the squared norm of a finite linear combination of the localized image vectors. If the pointwise inequality failed on a positive-measure subset, using that measurable subset for \(E\) would contradict (DF.26). Thus it holds almost everywhere for fixed \(a,k\). There are countably many rational finite vectors and partition sets. Remove their null union. On the remaining single conull set,

\[
 \Bigl\|\sum_n a_nb_n(y)\Bigr\|
       \leq\|B\|\Bigl\|\sum_n a_ne_n(y)\Bigr\|
       \quad\text{for every finite }a\in\mathbb Q(i)^{(\mathbb N)}.
 \tag{DF.27}
\]

This includes relations caused by zero frame vectors. Hence the assignment \(e_n(y)\mapsto b_n(y)\) is well defined on their rational span and extends continuously to a complex-linear operator \(B_y:H_y\to H_y\), with \(\|B_y\|\leq\|B\|\). Complex linearity follows by approximating arbitrary complex coefficients by rational ones before extension. Define \(B_y=0\) on the exceptional set. The fields \(B_ye_n=b_n\) are measurable there and off it; DF-05 therefore makes the operator field measurable.

For a bounded measurable scalar \(f\) supported on \(A_k\), commutation gives

\[
 B(fe_n)=fB(\mathbf1_{A_k}e_n)
         =\Bigl(\int_Y^\oplus B_y\,d\mu(y)\Bigr)(fe_n).
 \tag{DF.28}
\]

Finite sums of these inputs are dense in \(H\), by coordinate truncation and bounded scalar-function truncation in (DF.17). Both operators are bounded, so they agree on all of \(H\).

For uniqueness, if two essentially bounded measurable fields have the same integral, apply their difference to \(\mathbf1_{A_k}e_n\). Its global squared norm is zero, so their values on each frame vector agree almost everywhere on \(A_k\). The countable common null union over \(k,n\), followed by fibrewise density, makes the fields equal almost everywhere. The exact norm assertion is DF-07. This alternative proof verifies DG Theorem 5.1, and hence the conclusion of source Corollary IV.8.16, over an arbitrary sigma-finite base. Its proof route uses neither a commutant theorem nor a fibre-selector theorem as an input. \(\square\)

The proof also localizes any countable family of asserted bounded-operator identities: equality of the corresponding global decomposable operators gives equality on one common conull set by testing the same countable localized frame vectors. This is the countable-core uniqueness mechanism, rather than an uncountable union of fibre exceptional sets.

## Changing dimensions, a norm formula, and a nonuniform field

Let \(Y=(0,1]\) with Lebesgue measure. Put \(H_y=0\) for \(0<y<1/4\), \(H_y=\mathbb C\) for \(1/4\leq y<1/2\), and \(H_y=\mathbb C^2\) for \(1/2\leq y\leq1\). Let \(e_1,e_2\) be their ordinary compact coordinate frames, extended by zero where absent. Thus

\[
 E_1=[1/4,1],\qquad E_2=[1/2,1],\qquad
 \int_Y^\oplus H_y\,dy
  \cong L^2([1/4,1])\oplus L^2([1/2,1]).
 \tag{DF.29}
\]

The measurable fundamental inputs \(h_1=e_1\) and \(h_2=ye_1+e_2\) illustrate why a residual may vanish on the dimension-one stratum. Compact Gram–Schmidt makes \(e_2\) vanish there and leaves an initial nonzero basis segment on each fibre.

Define \(T_y=0\) on the zero fibres, \(T_y=2I\) on the dimension-one stratum, and

\[
 T_y=\begin{pmatrix}1&y\\0&2\end{pmatrix},\qquad
 T_y^*=\begin{pmatrix}1&0\\y&2\end{pmatrix}
       \quad(1/2\leq y\leq1).
 \tag{DF.30}
\]

All frame columns are measurable. On the two-dimensional stratum,

\[
 \|T_y\|^2=
 \frac{5+y^2+\sqrt{(5+y^2)^2-16}}2,
 \qquad \Bigl\|\int_Y^\oplus T_y\,dy\Bigr\|
      =\sqrt{3+\sqrt5}.
 \tag{DF.31}
\]

Indeed \(T_y^*T_y\) has trace \(5+y^2\) and determinant four, so its larger eigenvalue is the displayed root. That root is increasing in \(y>0\); its essential supremum is its limit at one. The dimension-one value two is smaller. This is an essential supremum, not a claim that a norm-maximizing global vector exists on the single endpoint fibre.

For a separate example with constant scalar fibres on \((0,1]\), the measurable field \(S_y=y^{-1}I\) is bounded on every fibre and has infinite essential supremum. Its integral is the closed multiplication operator with exact domain

\[
 D(S)=\{\xi\in L^2(0,1):\int_0^1y^{-2}|\xi(y)|^2\,dy<\infty\}.
 \tag{DF.32}
\]

The vectors \(\xi_n=\sqrt{2n}\,\mathbf1_{(1/(2n),1/n)}\) lie in this domain and satisfy \(\|\xi_n\|=1\), \(\|S\xi_n\|^2=2n^2\). Hence pointwise boundedness does not produce a bounded global integral. For \(\xi(y)=y^\beta\) with \(\beta>0\), membership in the domain is exactly \(\beta>1/2\); the boundary diverges logarithmically.

Finally, on a constant scalar field over \((0,1)\), reflection \((R\xi)(y)=\xi(1-y)\) is a global unitary. It is not decomposable. For \(f(y)=y\),

\[
 ((RM_f-M_fR)\xi)(y)=(1-2y)\xi(1-y).
 \tag{DF.33}
\]

At \(\xi=1\), the output squared norm is \(\int_0^1(1-2y)^2dy=1/3\). This nonzero commutator shows exactly which hypothesis of DF-08 fails: a global unitary moving base points does not commute with all diagonal multiplication operators.

The nine arguments cover the FIELD contract: Gram construction, measurable dimensions and frames, scalar products, specified-subfield projections, operator actions/adjoints/norms, conjugate and sum fields, the exact direct-integral Hilbert space, localization and almost-everywhere subsequences, and the diagonal-commutant characterization. The compatible GNS-field comparison and the CENTRAL and SELECTION contracts are not proved in this lesson.
