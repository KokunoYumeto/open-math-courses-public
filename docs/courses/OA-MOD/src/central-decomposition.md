# Central decomposition from countable operator equations

**Self-checked by the writing AI.**

An abelian central algebra determines the diagonal coordinates of a decomposition. The remaining issue is substantial: fibre commutants need measurable generating families, and the algebra of all bounded fibre sections must equal the original von Neumann algebra. The shared integral, centre, generator and intertwiner statements have the foundation owners identified below. Our retained route codes the unit operator ball as a compact metric space and constructs selectors for explicit countable closed equations. Together with the precise imports, it supplies the existing CENTRAL contract. The five separate SELECTION constructions for Hilbert-algebra graph cores and associated GNS fields remain distinct.

Human antecedents are M. Takesaki, *Theory of Operator Algebras I*, IV.8.18–8.23, printed 273–278 / one-based PDF 280–285. The centre/existence and uniqueness pages 277 and 278, were inspected again for this revision. The proof of existence in Theorem 8.21 is postponed there to representation disintegration. DC06–07 retain a direct realization at the explicit inputs below. DC10–11 separate same-diagonal uniqueness from change of base and its density factor. The exposition is independently written course prose; classical shared statements retain their existing owners.

**Foundation statements.** The shared assertions are proved in the earlier foundation lessons listed below. Their calculations remain as alternative derivations in this lesson.

| Local argument | Exact foundation statement |
| --- | --- |
| DC04, integral and commutant | Theorem 3.2 |
| DC07, whole algebra from countable generators | Lemma 5.1 |
| DC08, centres and factors | Theorem 4.3 |
| DC10, same-diagonal operator field | Proposition 6.1 |

The first three statements belong to *Direct integrals of von Neumann algebras*; the fourth belongs to *Decomposable operators and the diagonal algebra*. They hold over arbitrary sigma-finite measure spaces with separable fibres, without global separability or standardness. DC07 retains global separability for its explicit realization of a specified central abelian algebra. The factor criterion is applied on the nonzero effective support, as permitted by the foundation’s Remark 4.4(2). DC01–03 retain the compact-equation selection and generator construction, DC05 the finite density proof, DC06 the explicit diagonal realization, DC09 the specified common-null localization, DC11 the typed Borel-base and density transport, and DC12 the tests. These are precise statement imports; DC has no dependency on its DI consumer.

Inner products are linear first. The bounded inputs are BK-02's bicommutant theorem, the Hilbert completion/projection/Riesz/adjoint contracts, and SK-02–04's finite regular cyclic spectral representation and bounded Borel calculus. Scalar integration, scalar \(L^2\) completeness and monotone/dominated convergence have their existing course bindings. We prove the finite Radon–Nikodym step in DC-05 rather than importing an unstated measure theorem. DF-01–08 supplies measurable Hilbert fields, exact operator norms, Hilbert integrals and the diagonal-commutant theorem at its declared inputs. The retained alternative proof route uses no central-decomposition theorem or general measurable-selection theorem as an input; its shared statement imports are precisely those in the table above. DC-11 additionally uses a supplied Borel realization of each standard base as a Borel subset of the real unit interval; the general standard-Borel realization theorem is a distinct input whose transitive binding is not supplied by merely naming a standard base.

Von Neumann subalgebras are unital on the displayed Hilbert space. The zero Hilbert space is treated explicitly. Inner-product notation and fibre commutants are taken on the stated fibre Hilbert space, even when its operators are extended by zero in the ambient space. Equality of fibre fields means equality off one null set after specifying the countable data being compared; it never means a universal null set for every measurable representative.

## The unit operator ball is compact in countable weak coordinates

Let \(K\) be a fixed separable complex Hilbert space, realized as a closed subspace of \(\ell^2\) or as \(\ell^2\) itself. Fix a countable dense vector sequence \(v_n\), including the finite rational combinations of a fixed orthonormal basis. On the unit ball \(C\) of \(B(K)\), the weak operator topology is determined by the countable coefficients against basis vectors. If \((r_l,s_l)\) enumerates all basis-index pairs, use

\[
 d(S,T)=\sum_{l=1}^{\infty}2^{-l}
 \min\{1,|\langle(S-T)\delta_{r_l},\delta_{s_l}\rangle|\}.
 \tag{DC.1}
\]

This is a metric: zero distance gives every matrix coefficient zero, hence equality on the dense linear span. Convergence of the matrix coefficients gives weak convergence on arbitrary vector pairs by approximation and the common unit bound. Conversely weak convergence gives convergence in (DC.1), by first controlling a finite sum and then its uniform tail. Thus the metric gives precisely WOT on \(C\).

Every sequence in \(C\) has a subsequence on which all its countably many coefficients converge, by successive subsequences in bounded complex disks and diagonalization. On finite linear combinations \(u,v\) the limiting form \(b(u,v)\) is sesquilinear and satisfies \(|b(u,v)|\leq\|u\|\,\|v\|\). The bound extends it to \(K\). Riesz representation yields a unique \(T\) with norm at most one and \(b(u,v)=\langle Tu,v\rangle\). The selected subsequence converges to \(T\) in (DC.1). Sequential compactness of a metric space implies compactness: if no finite radius-epsilon cover existed, recursively choose an epsilon-separated sequence; completeness follows from convergent subsequences of Cauchy sequences; the usual successive finite-cover construction then proves compactness. This also proves separability by choosing finite \(1/m\) nets and taking their countable union. Consequently

\[
 C\text{ is compact metric and has a fixed countable dense set }\{q_j\}.
 \tag{DC.2}
\]

The same proof applies to the self-adjoint unit ball and to any WOT-closed subset of \(C\). This compactness argument uses no central decomposition and makes no assertion of operator-norm compactness. For \(K=0\) the ball is a singleton. \(\square\)

## Measurable selectors for countably many continuous closed equations

Let \((Y,\Sigma)\) be any measurable space and \(C\) any compact metric space with a fixed countable dense set. Suppose \(f_n:Y\times C\to\mathbb C\) is measurable in \(y\) for fixed \(t\) and continuous in \(t\) for fixed \(y\). Write

\[
 F_y=\{t\in C:f_n(y,t)=0\text{ for every }n\},
 \qquad F_y\ne\varnothing.
 \tag{DC.3}
\]

We prove, with explicit measurable tests, that \(F\) has a measurable selector and a countable family of measurable selectors dense in every \(F_y\).

For every fixed nonempty compact subset \(L\) of \(C\), choose a countable dense set in \(L\). Continuity makes the infimum of a continuous function on \(L\) equal its infimum on that dense set, hence makes

\[
 y\longmapsto\inf_{t\in L}\max_{n\leq m}|f_n(y,t)|
 \quad\text{measurable},\qquad
 F_y\cap L\ne\varnothing\iff
 \inf_{t\in L}\max_{n\leq m}|f_n(y,t)|=0\quad(m\geq1).
 \tag{DC.4}
\]

For the reverse implication, each finite family has a zero on \(L\) because its nonnegative maximum attains the zero infimum. These zero sets are nested nonempty compact sets, whose intersection is nonempty. Empty \(L\) has an identically false intersection test. Only countably many compact sets will be used, so the choices of dense sets do not introduce parameter-dependent selections.

Use closed balls with centers in \(\{q_j\}\) and positive rational radii, all relative to \(C\). For each open \(O\) in \(C\), it is the union of those closed balls contained in \(O\). Indeed a point in \(O\) has a positive distance margin inside \(O\); choose a sufficiently close \(q_j\) and a sufficiently small rational radius whose ball contains that point and stays within the margin. Equation (DC.4) therefore makes \(\{y:F_y\cap O\ne\varnothing\}\) measurable, for a countable open basis and hence for every open \(O\).

Here is the selector itself. Set \(L_0=C\). At stage \(m\) choose the least \(j\) for which

\[
 F_y\cap L_{m-1}(y)\cap\overline B(q_j,2^{-m})\ne\varnothing,
 \qquad
 L_m(y)=L_{m-1}(y)\cap\overline B(q_j,2^{-m}).
 \tag{DC.5}
\]

Such a \(j\) exists because the balls cover \(C\). The previous indices take only countably many values; on each such index history, \(L_{m-1}\) is a fixed compact set. Thus (DC.4), followed by countable least-index choice, makes every stage measurable. The nested compact sets \(F_y\cap L_m\) are nonempty and have diameters at most \(2^{1-m}\). Their intersection is one point \(s(y)\in F_y\); the selected centers converge to \(s(y)\), so \(s\) is measurable as a pointwise limit of measurable countably valued maps.

For each member \(O\) of a countable open basis, on the measurable hit event first choose the least closed ball \(L\) contained in \(O\) that meets \(F_y\) and perform the same nested construction starting from \(L\). Outside the hit event use the first selector \(s\). Denote the result by \(s_O\). Every open set meeting \(F_y\) contains a basis member meeting it, and the corresponding \(s_O\) lies inside that member. The countable family consisting of \(s\) and all \(s_O\) is therefore dense in \(F_y\) for every \(y\). This proves the entire compact-equation selection lemma; it is stronger than selection after measure completion because the construction works on the given \(\sigma\text{-algebra}\). It does not assert a selector for an arbitrary analytic relation or an unbounded graph-core condition. \(\square\)

## Countable measurable generators for fibre commutants

Use DF-03 to realize a measurable Hilbert field \(H_y=P_y\ell^2\), with measurable orthogonal projections \(P_y\). Let \(a_j(y)\) be a countable family of measurable bounded operators on \(H_y\), with each fibre operator bounded; the norms need not have one common essential bound. Include adjoints. Extend operators by zero on the complementary ambient subspace. Define

\[
 N_y=\{a_j(y):j\geq1\}'',\qquad
 C_y'=\{T\in B(\ell^2):\|T\|\leq1,
 T=P_yTP_y, [T,a_j(y)]=0\ (j\geq1)\}.
 \tag{DC.6}
\]

Restricted to \(H_y\), \(C_y'\) is exactly the unit ball of \(N_y'\). It is nonempty because it contains zero. Each coefficient of \(T-P_yTP_y\) and of \(Ta_j-a_jT\) is continuous in \(T\) for WOT on the ambient unit ball: multiplication by fixed bounded operators is WOT continuous. For fixed \(T\) it is measurable in \(y\) by DF-05. The projections and \(a_j\) are measurable operator fields, their actions on any measurable vector are measurable, and their adjoints have the same property. Enumerate the real and imaginary parts of all these coefficient equations. DC-02 applies and produces countably many measurable maps \(b_l(y)\) dense in \(C_y'\).

A measurable map into the WOT unit ball gives a measurable operator field. Its coefficients on fixed basis vectors are measurable. For a fixed basis vector, its image is the norm limit of its finite coordinate truncations, whose coordinates are measurable; separability then makes the image a measurable Hilbert vector. For arbitrary measurable vectors, approximate by finite coordinate sections and use the uniform operator bound. Restriction and DF transport give measurable \(b_l\) on \(H_y\). The \(b_l\) are contractions and generate \(N_y'\) as a von Neumann algebra: any operator in its unit ball is in their WOT closure, so any WOT-closed algebra containing them contains the whole unit ball and its scalar multiples.

Apply the same construction to the countable family consisting of \(b_l\) and \(b_l^*\). It supplies measurable contraction generators \(c_k\) for \((N_y')'=N_y\). Thus both the field and its commutant have countable measurable generating families, with the exact bound

\[
 \|b_l(y)\|\leq1,\quad \|c_k(y)\|\leq1,\qquad
 \{b_l(y),b_l(y)^*:l\geq1\}''=N_y',
 \quad\{c_k(y),c_k(y)^*:k\geq1\}''=N_y.
 \tag{DC.7}
\]

Adjoints may already be in the dense families; explicitly adding them prevents any ambiguity. Zero fibres give zero selectors, and variable or infinite dimensions cause no change in the ambient compact coding. This proves the measurable generating-family and commutant assertions without invoking CENTRAL or SELECTION as an input. \(\square\)

## The integral algebra and its exact commutant

**Alternative derivation of VN Theorem 3.2(1)–(3).** Assume an arbitrary sigma-finite base and let \(N_y\) be a field with countable measurable generators, as in DC-03. Set

\[
 \mathcal N=\left\{\int_Y^{\oplus}T_y\,d\mu(y):
 T_y\in N_y\text{ a.e.},\ T\text{ measurable},\
 \operatorname*{ess\,sup}_y\|T_y\|<\infty\right\}.
 \tag{DC.8}
\]

This is a unital *-algebra by DF-05/07. It contains the represented diagonal algebra \(D\) because \(f(y)I_{H_y}\) belongs to every fibre algebra. \(D\) is central in \(\mathcal N\).

Let \(B\) belong to \(\mathcal N'\). Since it commutes with \(D\), DF-08 gives a bounded measurable field \(B_y\). If the given generator \(a_j\) has nonuniform norms, use its measurable cutoffs \(a_{j,m}(y)=1_{\{\|a_j(y)\|\leq m\}}a_j(y)\). Their integrals belong to \(\mathcal N\). Commutation with these countably many operators, followed by DF-07/08 uniqueness, gives

\[
 [B_y,a_{j,m}(y)]=0\quad(j,m\geq1)
 \quad\text{off one null set}.
 \tag{DC.9}
\]

Each \(a_j(y)\) is bounded on its fibre, so one cutoff eventually equals it there. Thus \(B_y\) belongs to \(N_y'\). Conversely, if \(B_y\) belongs to \(N_y'\), it commutes pointwise almost everywhere with each specified bounded measurable \(\mathcal N\)-field, giving commutation after integration. Hence

\[
 \mathcal N'=\int_Y^{\oplus}N_y'\,d\mu(y).
 \tag{DC.10}
\]

This notation means the algebra of all essentially bounded measurable sections, not an assertion that an arbitrary family of operators is measurable. DC-03 supplies countable measurable generators for the commutant field as well. Applying the argument to \(N_y'\) proves \(\mathcal N''=\int_Y^\oplus N_y''\,d\mu(y)=\mathcal N\). BK-02 therefore makes \(\mathcal N\) a von Neumann algebra. Both the exact commutant and bicommutant assertions are proved. No uncountable family of operator identities has been removed in one null union. \(\square\)

## A finite Radon–Nikodym density from Hilbert representation

Let \(\mu\) and \(\nu\) be finite positive measures on the same measurable space, with \(\nu\ll\mu\). Set \(\tau=\mu+\nu\). The functional \(f\longmapsto\int f\,d\nu\) is bounded on complex \(L^2(\tau)\), since

\[
 \left|\int f\,d\nu\right|
 \leq\nu(Y)^{1/2}\left(\int|f|^2\,d\nu\right)^{1/2}
 \leq\nu(Y)^{1/2}\|f\|_{L^2(\tau)}.
 \tag{DC.11}
\]

It is well defined modulo \(\tau\)-null sets. Hilbert Riesz gives \(g\) in \(L^2(\tau)\) with \(\int f\,d\nu=\int fg\,d\tau\); initially the representing vector is conjugated because inner products are linear first. Testing indicators shows that \(g\) is real and \(0\leq g\leq1\) almost everywhere. To see the reality assertion, integrate its imaginary part on the sets where that part is positive or negative; similarly the sets where \(g<0\) or \(g>1\) contradict positivity of \(\nu\) or \(\mu\). Since \(\tau\) is finite, all bounded indicators belong to \(L^2(\tau)\). Consequently \(\nu=g\tau\) and \(\mu=(1-g)\tau\) on every measurable set.

The set \(\{g=1\}\) is \(\mu\)-null and therefore \(\nu\)-null, by absolute continuity, hence \(\tau\)-null. Define \(h=g/(1-g)\) elsewhere and zero on that set. By nonnegative simple approximation and monotone convergence,

\[
 h\geq0,\qquad \nu(E)=\int_E h\,d\mu\quad(E\in\Sigma).
 \tag{DC.12}
\]

The density is unique \(\mu\)-almost everywhere: if two densities differ on a positive-measure set, some bounded-away-from-zero difference on a finite sublevel set has nonzero integral, contrary to equality on every measurable subset. If \(\nu\) is equivalent to \(\mu\), \(h\) is positive \(\mu\)-almost everywhere, as well as finite \(\mu\)-almost everywhere. The construction includes zero measures. This gives the finite density needed below with a full proof at scalar \(L^2\) and Hilbert Riesz inputs. \(\square\)

## Realizing an abelian algebra as the diagonal algebra

Let \(D\) be a unital abelian von Neumann algebra on a separable nonzero Hilbert space \(H\). DC-01 makes its self-adjoint unit ball a compact metric space in WOT. Choose a countable dense family \(h_j\) there. The von Neumann algebra generated by these \(h_j\) contains the WOT closure of that family, so it contains the self-adjoint unit ball, hence all of \(D\). Rational spectral projections of the \(h_j\) form a countable commuting family \(p_n\) generating \(D\): the spectral calculus supplies each \(p_n\) in \(D\), and bounded step approximation reconstructs \(h_j\) from its rational spectral cuts.

We replace the countable family by one positive generator,

\[
 h=\sum_{n=1}^{\infty}3^{-n}p_n,\qquad 0\leq h\leq\tfrac12 I,
 \qquad D=\{h\}''.
 \tag{DC.13}
\]

The series converges in norm. Here is the reverse inclusion. Let \(S\) be the compact set of sums \(\sum_{n=1}^\infty 3^{-n}\varepsilon_n\) with \(\varepsilon_n\in\{0,1\}\). The first differing digit dominates the remaining tail, so the coding map from \(\{0,1\}^{\mathbb N}\) into \(S\) is injective and its inverse digit functions are continuous on \(S\). The spectrum of \(h\) lies in \(S\): its mth partial sum has spectrum in the finite prefix sums, and its norm tail is at most \(\tfrac12 3^{-m}\). Resolvent perturbation bounds the distance of every spectral point of \(h\) from a prefix spectrum by that tail; letting \(m\) grow gives membership in \(S\). The continuous nth digit function on \(S\) applied to \(h\) is \(p_n\). Indeed extend that continuous function to the enclosing interval by linear interpolation across the complementary intervals; evaluating partial sums for \(m\geq n\) gives \(p_n\), and norm continuity of continuous calculus passes to the limit \(h\). Thus every \(p_n\) lies in \(\{h\}''\), proving (DC.13).

Apply SK-02/03 to the continuous calculus of \(h\) on its compact spectrum \(X\). Since \(H\) is separable, its nonzero orthogonal cyclic subspaces are at most countable: pick distinct points from a fixed countable dense family in disjoint balls around their unit vectors. Obtain

\[
 H\cong\bigoplus_{k\in J}L^2(X,\nu_k),\qquad
 h\cong\bigoplus_k M_x,
 \tag{DC.14}
\]

where \(J\) is nonempty and at most countable and the cyclic generators are normalized, so each \(\nu_k\) has mass one. Choose positive numbers \(\alpha_k\) with \(\sum_k\alpha_k=1\) and set \(\mu=\sum_k\alpha_k\nu_k\). This is a finite Borel probability measure on the compact metric subset \(X\) of the real line. Each \(\nu_k\) is absolutely continuous with respect to \(\mu\). DC-05 supplies \(r_k=d\nu_k/d\mu\); put \(E_k=\{r_k>0\}\). Remove the one null set on which any required density identity fails. In particular \(\sum_k\alpha_k r_k=1\) almost everywhere, so the \(E_k\) cover the base almost everywhere.

Define \(H_y\) as the closed span in \(\ell^2(J)\) of \(\delta_k\) for which \(y\) belongs to \(E_k\). The coordinate sections \(1_{E_k}\delta_k\) give its measurable structure by DF. The unitary from (DC.14) to its direct integral is

\[
 (f_k)_k\longmapsto\xi(y)=\sum_k\sqrt{r_k(y)}f_k(y)\delta_k,
 \qquad
 \int\|\xi(y)\|^2\,d\mu=\sum_k\int|f_k|^2\,d\nu_k.
 \tag{DC.15}
\]

The equality follows by monotone convergence. It is onto: from the \(k\)-coordinate of a measurable square-integrable section, divide by \(\sqrt{r_k}\) on \(E_k\) and set zero outside; the same integral identity gives the required \(L^2(\nu_k)\) functions. Representatives can be chosen on one common null set because \(J\) is countable. Denote the resulting unitary \(H\longrightarrow\int_X^\oplus H_y\,d\mu(y)\) by \(V\).

Every bounded Borel \(f\) on \(X\) acts after \(V\) as \(f(y)I_{H_y}\). By SK-04 these operators lie in \(\{h\}''=D\). Conversely, let \(\mathcal A\) be the integral algebra of all measurable essentially bounded \(B(H_y)\)-fields. DC-04 gives \(\mathcal A'=\int^{\oplus}\mathbb CI_{H_y}\,d\mu\). A measurable scalar field here has measurable coefficient, obtained by testing its first compact frame vector; its essential bound is exactly the essential bound of that coefficient. Thus \(\mathcal A'\) is precisely the scalar multiplication algebra, and as a commutant it is a von Neumann algebra. It contains the continuous calculus of \(h\), so it contains \(D\). We have proved

\[
 VDV^*=\{M_f:f\in L^\infty(X,\mu)\},
 \qquad H_y\ne0\text{ for almost every }y.
 \tag{DC.16}
\]

In the stated alternative proof of strong closedness, full \(B(H_y)\) has a countable measurable generating family: the coordinate matrix units \(1_{E_j\cap E_k}\,|\delta_j\rangle\langle\delta_k|\), whose fibre commutant is the scalars on \(H_y\). Thus DC-04 applies without invoking central decomposition. All completed measurable functions have Borel representatives modulo null sets. The base is a compact metric Borel base with finite measure and is therefore standard sigma-finite. If \(H=0\), use the empty base with zero measure and the empty Hilbert integral; both algebras have identity zero. \(\square\)

## Existence over any specified central abelian subalgebra

Let \(M\) be a von Neumann algebra on a separable Hilbert space \(H\) and let \(D\) be a specified unital von Neumann subalgebra of \(Z(M)\). For \(H=0\) use the empty decomposition from DC-06. Otherwise first diagonalize \(D\) by \(V\) from DC-06. Choose a countable WOT-dense family \(a_j\) in the unit ball of \(VMV^*\), and include its adjoints and the identity. This family generates \(VMV^*\) by the same closure argument as DC-06.

Each \(a_j\) commutes with all diagonal multiplications because \(D\) is central in \(M\). DF-08 supplies measurable contraction fields \(a_j(y)\). Choose their representatives and remove one null set on which any adjoint or identity equality for this countable family fails. Define

\[
 M_y=\{a_j(y):j\geq1\}'',\qquad
 \mathcal F=\int_X^{\oplus}M_y\,d\mu(y).
 \tag{DC.17}
\]

DC-03 makes both \(M_y\) and \(M_y'\) fields with countable measurable contraction generators; DC-04 makes \(\mathcal F\) a von Neumann algebra.

**Countable-generator clause: VN Lemma 5.1.** We prove by the retained commutant argument that \(\mathcal F\) is exactly \(VMV^*\), rather than merely an algebra containing its selected generators. Every \(B\) in \((VMV^*)'\) commutes with \(D\) because \(D\) is a subalgebra of \(VMV^*\). DF-08 therefore makes it decomposable. Its commutation with the \(a_j\) is equivalent, after removing their countable common null set, to \(B_y\) commuting with every \(a_j(y)\), that is \(B_y\) in \(M_y'\). Conversely every bounded measurable \(M_y'\)-field commutes with the \(a_j\) after integration and hence with their bicommutant \(VMV^*\). Thus

\[
 (VMV^*)'=\int_X^{\oplus}M_y'\,d\mu(y)
 =\mathcal F',\qquad VMV^*=\mathcal F.
 \tag{DC.18}
\]

The final equality follows by taking commutants and using that both algebras equal their bicommutants. This proves existence at the entire stated CENTRAL scope: the specified \(D\) is diagonal, the base is standard finite (hence sigma-finite), and the original algebra, not just its chosen \(C^*\)-subalgebra, is the integral of its fibres. Faithfulness of the represented diagonal on the effective support follows from (DC.16), so no positive-measure zero-fibre ambiguity is retained in this constructed decomposition. \(\square\)

## Centers and the factor decomposition

**Alternative derivation of VN Theorem 4.3 on an arbitrary sigma-finite base.** For any field \(N_y\) with countable measurable generators, let \(Z_y=N_y\cap N_y'\). Apply the compact-equation construction to the combined generating families for \(N_y\) and \(N_y'\). Their commutant is \(N_y'\cap N_y=Z_y\). Thus the center field has measurable contraction generators. For \(\mathcal N=\int_Y^\oplus N_y\,d\mu(y)\), DC-04 implies

\[
 Z(\mathcal N)=\mathcal N\cap\mathcal N'
 =\int_Y^{\oplus}Z(N_y)\,d\mu(y).
 \tag{DC.19}
\]

The equality includes the common null set for the two memberships of each specified field. Conversely a bounded measurable \(Z_y\)-field belongs to both integral algebras.

On the effective support \(Y_+=\{y:\dim H_y>0\}\), the center equals the represented diagonal algebra if and only if \(N_y\) is a factor almost everywhere. One implication is immediate when \(Z_y=\mathbb CI_{H_y}\). For the other, let \(z_l(y)\) be a countable WOT-dense family in the unit ball of \(Z_y\) and choose the first vector \(e_1(y)\) of the compact DF frame, of norm one on \(Y_+\). Put

\[
 c_l(y)=\langle z_l(y)e_1(y),e_1(y)\rangle,\qquad
 q_l(y)=z_l(y)-c_l(y)I_{H_y}.
 \tag{DC.20}
\]

These are measurable central fields, bounded by two. If a non-scalar center occurs, some \(z_l\) is non-scalar there: scalar multiples of the identity form a WOT-closed subspace, so a dense family consisting entirely of scalars would force the whole center to be scalar. The event that \(q_l\) is nonzero is measurable by DF's exact norm test. If such events have positive measure for any \(l\), the integral of \(q_l\) is a central operator that cannot be diagonal: a scalar field with its first diagonal coefficient zero is zero, whereas this \(q_l\) is nonzero on a positive-measure set. This contradicts \(Z(\mathcal N)=D\). The countable union proves that nonfactor fibres have measure zero.

Apply DC-07 with \(D=Z(M)\). Its fibres are nonzero almost everywhere by construction, so the equivalence proves a decomposition into factors. For an arbitrary field with positive-measure zero fibres, the assertion is expressly restricted to \(Y_+\); neither faithfulness of \(L^\infty\) on the removed set nor the designation of the zero algebra as a factor is assumed. \(\square\)

## Exact common-null-set localization of specified data

Over an arbitrary sigma-finite base, fix any countable list of measurable vectors, bounded measurable operator fields and their stated relations in a decomposition. Localize vectors by the exhaustion \(F_m\) of finite measure and by their norm cutoffs. Such localizations belong to the global Hilbert integral. If two global operators agree, DF-07/08 uniqueness gives equality of their fibre actions on a countable compact frame almost everywhere. If a global vector is zero, its squared integral norm gives a zero fibre vector almost everywhere. Intertwining, products and adjoints of bounded fields are measurable and integrate correctly by DF-05/07.

Each particular relation therefore has a measurable exceptional set of measure zero. Enumerate the specified relations and take the union of these exceptional sets, also including the representative and finite-measure localization exceptional sets. On the complement every enumerated relation holds simultaneously. In particular, for countably many generators \(a_j\) and specified commutant fields \(b_k\),

\[
 [a_j,b_k]=0\text{ globally for all }j,k
 \Longrightarrow
 [a_j(y),b_k(y)]=0\text{ for all }j,k
 \text{ on one conull set}.
 \tag{DC.21}
\]

The converse is immediate after integration. The compact generators from DC-03 then extend these relations to the generated fibre von Neumann algebras by WOT continuity of fixed multiplication. Nonuniformly bounded measurable operators may be included by taking the countably many norm cutoffs used in DC-04. Closed unbounded operator equality requires graph/domain data, not this bounded-operator test; a graph relation can be localized only after its measurable graph and the relevant countable cores are actually supplied. This supplies the countable-core localization in CENTRAL without borrowing an unwritten SELECTION graph-core construction. \(\square\)

## Uniqueness over the same diagonal structure

**Same-diagonal field clause: DG Proposition 6.1.** Let \(H=\int_Y^\oplus H_y\,d\mu(y)\) and \(K=\int_Y^\oplus K_y\,d\mu(y)\) be Hilbert integrals over the same arbitrary sigma-finite base. Suppose \(U:H\longrightarrow K\) is a unitary with

\[
 UM_f^{H}=M_f^{K}U\quad(f\in L^\infty(Y,\mu)).
 \tag{DC.22}
\]

**Alternative block reconstruction.** Apply DF-08 on the sum field \(H_y\oplus K_y\) to the bounded block operator sending \((\xi,\eta)\longmapsto(0,U\xi)\). It commutes with the scalar diagonal. The countably many constant block-projection equations force its reconstructed field to have precisely the same off-diagonal block form. Therefore \(U\) is the integral of a measurable field \(U_y:H_y\longrightarrow K_y\), of norm at most one. DF-07 gives its adjoint field, and uniqueness applied to \(U^*U=I\) and \(UU^*=I\) yields both fibre identities off one null set:

\[
 U_y^*U_y=I_{H_y},\qquad U_yU_y^*=I_{K_y},\qquad
 U=\int_Y^{\oplus}U_y\,d\mu(y).
 \tag{DC.23}
\]

Thus \(U_y\) is unitary, including the zero-to-zero case; the two fibre dimensions agree almost everywhere. No measurable selection of arbitrary fibre isomorphisms is used: the field is reconstructed from the given global \(U\).

Suppose in addition \(\mathcal N=\int_Y^\oplus N_y\,d\mu(y)\) and \(\mathcal Q=\int_Y^\oplus Q_y\,d\mu(y)\) are the algebras of all bounded measurable sections, their fibre algebras having the countable generating families above, and \(U\mathcal NU^*=\mathcal Q\). Use measurable contraction generators \(a_j(y)\) of \(N_y\). Their global integrals belong to \(\mathcal N\), so the fibre fields \(U_ya_j(y)U_y^*\) belong to \(Q_y\) almost everywhere. Take the countable union of these exceptional sets. Fixed multiplication is WOT continuous, so the generator inclusion extends to \(U_yN_yU_y^*\subseteq Q_y\). Applying the same argument to \(U^*\) and contraction generators of \(Q_y\) proves the reverse inclusion. Hence

\[
 U_yN_yU_y^*=Q_y\quad\text{almost everywhere}.
 \tag{DC.24}
\]

This proves full same-diagonal uniqueness, including the specified algebra identification and both directions of unitary transport, at the CENTRAL contract. It does not imply that a family of abstract fibre isomorphisms given without \(U\) is measurable. \(\square\)

## Change of base and the square-root density in general uniqueness

For this section suppose the two standard bases are supplied as Borel subsets \(Y_i\) of \([0,1]\), with completed sigma-finite Borel measures \(\mu_i\), and nonzero fibres almost everywhere. This is the exact standard-Borel-realization input identified above. Write \(\mathcal H_1=\int_{Y_1}^{\oplus}H_x\,d\mu_1(x)\) and \(\mathcal H_2=\int_{Y_2}^{\oplus}K_y\,d\mu_2(y)\), and let \(U:\mathcal H_1\longrightarrow\mathcal H_2\) be a unitary taking the first diagonal algebra onto the second. If these Hilbert spaces are zero, faithfulness forces both measure algebras to be zero. Removing the null bases leaves the empty Borel isomorphism and empty fibre unitary, so all subsequent almost-everywhere assertions are vacuous. Henceforth the Hilbert spaces are nonzero; both measures have positive total mass, and equivalent probability measures can be chosen. The diagonal representations are faithful, so conjugation by \(U\) induces an isomorphism

\[
 \theta:L^\infty(Y_1,\mu_1)\longrightarrow L^\infty(Y_2,\mu_2).
 \tag{DC.25}
\]

This isomorphism preserves suprema of bounded increasing families because it is an order isomorphism; in particular it preserves monotone sequential spectral constructions. Use equivalent finite probability measures first, choosing positive integrable densities on the sigma-finite exhaustions. Equivalent replacement changes neither null sets nor \(L^\infty\). Let \(c_i\) be the coordinate function on \(Y_i\) and choose a measurable representative \(g\) of \(\theta(c_1)\). Order implies \(0\leq g\leq1\) almost everywhere.

Polynomial and uniform continuous approximation give \(\theta(f(c_1))=f(g)\) for every continuous \(f\) on \([0,1]\). Monotone open-set approximations and the Dynkin-class argument from SK-04 extend this identity to every bounded Borel \(f\). In particular \(f=1_{Y_1}\) gives \(g(y)\in Y_1\) almost everywhere. Set \(\Phi(y)=g(y)\) there and choose arbitrary values on the null exceptional set. The same procedure for \(\theta^{-1}\) gives a Borel map \(\Psi:Y_1\longrightarrow Y_2\) modulo null sets. Completed measurable scalar functions have Borel versions. We obtain

\[
 \theta(f)(y)=f(\Phi(y))\quad\text{a.e. on }Y_2,
 \qquad
 \theta^{-1}(g)(x)=g(\Psi(x))\quad\text{a.e. on }Y_1.
 \tag{DC.26}
\]

Here bounded measurable \(f\) can be represented by bounded Borel functions on \(Y_1\), extended by zero to \([0,1]\). Indicator functions show that \(\Phi\) pulls every \(\mu_1\)-null Borel set back to a \(\mu_2\)-null set, and \(\Psi\) has the converse property. Applying the two identities to the coordinate functions and using these nonsingularity facts gives \(\Phi(\Psi(x))=x\) and \(\Psi(\Phi(y))=y\) almost everywhere. Choose Borel conull sets \(G_1,G_2\) where these identities and memberships hold. Restrict to \(X_1=\{x\in G_1:\Psi(x)\in G_2\}\) and \(X_2=\{y\in G_2:\Phi(y)\in G_1\}\). Nonsingularity makes these conull. The identities show that \(\Phi:X_2\longrightarrow X_1\) and \(\Psi:X_1\longrightarrow X_2\) are Borel inverse bijections. Thus the base map is a Borel isomorphism after null removal, not merely a map of measure algebras.

The pushforward \(\lambda=\Phi_*\mu_2\) is equivalent to \(\mu_1\). It is sigma-finite because \(\Phi\) is a Borel isomorphism on the conull sets. The finite density construction DC-05 extends to equivalent sigma-finite measures by choosing one countable partition on which both are finite: intersect and disjointize two finite-measure exhaustions. On each partition piece obtain the finite density and paste. Hence \(w=d\lambda/d\mu_1\) exists and satisfies \(0<w<\infty\) almost everywhere. Its square root is the exact coordinate-change factor:

\[
 (J\eta)(x)=\sqrt{w(x)}\,\eta(\Psi(x)),\qquad
 J:\int_{Y_2}^{\oplus}K_y\,d\mu_2(y)
 \longrightarrow\int_{Y_1}^{\oplus}K_{\Psi(x)}\,d\mu_1(x).
 \tag{DC.27}
\]

The transported field is measurable by its pulled-back fundamental sections. The pushforward identity makes \(J\) isometric and its inverse is division by \(\sqrt w\) followed by \(\Phi\). Thus it is onto. It conjugates \(M_{f\circ\Phi}\) to \(M_f\). If a global \(U\) maps the two diagonal algebras onto each other according to \(\theta\), then \(JU\) intertwines the same scalar diagonal on \(Y_1\). DC-10 supplies a measurable unitary field \(W_x:H_x\longrightarrow K_{\Psi(x)}\). Solving \(JU=\int_{Y_1}^\oplus W_x\,d\mu_1(x)\) gives

\[
 (U\xi)(y)=w(\Phi(y))^{-1/2}W_{\Phi(y)}\xi(\Phi(y))
 \quad\text{for almost every }y\in Y_2.
 \tag{DC.28}
\]

If \(U\) also conjugates the global integral algebras, DC-10 gives \(W_xM_xW_x^*=N_{\Psi(x)}\) almost everywhere. The factor \(w^{-1/2}\) in this direction is required by the exact norm identity; the reciprocal \(\sqrt w\) belongs to \(J\) in the opposite direction. These typed formulas avoid ambiguous expressions that integrate a map into a fibre over the wrong base point. The argument recovers the full change-of-base uniqueness assertion at the explicitly supplied standard-Borel models. The general Borel-realization input is not proved here. Zero-fibre sets, if originally present, must first be removed to make the diagonal faithful. \(\square\)

## Exact finite models and tests that distinguish the hypotheses

On a two-point base \(\{a,b\}\) with masses \(p\) and \(1-p\), \(0<p<1\), let \(H_a=\mathbb C^2\) and \(H_b=\mathbb C^3\). Set \(M_a=B(\mathbb C^2)\), \(M_b=B(\mathbb C^3)\). Their integral acts on \(\mathbb C^2\oplus\mathbb C^3\) with Hilbert norm

\[
 \|(\xi_a,\xi_b)\|^2=p\|\xi_a\|^2+(1-p)\|\xi_b\|^2,
 \quad\mathcal M=B(\mathbb C^2)\oplus B(\mathbb C^3),
 \quad\mathcal M'=\mathbb CI_2\oplus\mathbb CI_3.
 \tag{DC.29}
\]

The center is the full diagonal. Matrix units form contraction generators and their commutation equations force a scalar matrix on each fibre. This is a factor decomposition with changing dimensions.

If instead the specified central algebra is only \(\mathbb CI\) inside this same global \(M\), DC-07 may use a one-point base with fibre \(\mathbb C^5\) and fibre algebra \(B(\mathbb C^2)\oplus B(\mathbb C^3)\). Its center is two-dimensional, so that fibre is not a factor. Existence relative to an arbitrary chosen \(D\) does not require factor fibres; taking \(D=Z(M)\) is the hypothesis that forces them.

For the direction of the density factor, retain the two-point base and fibres but replace the masses \((p,1-p)\) by \((q,1-q)\), \(0<q<1\), with the identity base map. Then

\[
 w(a)=q/p,\quad w(b)=(1-q)/(1-p),\qquad
 U(\xi_a,\xi_b)=
 \left(\sqrt{p/q}\,\xi_a,
 \sqrt{(1-p)/(1-q)}\,\xi_b\right)
 \tag{DC.30}
\]

is unitary from the \(p\)-weighted Hilbert sum to the \(q\)-weighted one and intertwines both diagonal and fibre algebras. Substitution gives \(q(p/q)\|\xi_a\|^2+(1-q)((1-p)/(1-q))\|\xi_b\|^2\) equal to the norm in (DC.29). Multiplication by \(\sqrt{q/p}\) in the same direction generally fails this test. At \(p=1/3\) and \(q=1/2\) the correct multipliers are \(\sqrt{2/3}\) and \(\sqrt{4/3}\).

Finally, on two equal-mass points with equal nonzero fibres, the block swap is unitary and carries the diagonal algebra onto itself, but fails to commute with the characteristic multiplication of the first point. Its base map interchanges \(a\) and \(b\). Thus it belongs to DC-11's general uniqueness setting, while DC-10's same-diagonal intertwining hypothesis is absent. This example distinguishes diagonal normalization from commutation with every individual scalar multiplication.

DC01–10 supplies the existing CENTRAL contract through these exact foundation clauses and retained local mechanisms at the named elementary and DF inputs. DC-11 records the additional general base-change scope and its explicit Borel-model dependency; DC-12 checks the coordinate, commutant, factor and density mechanisms. The separate associated GNS-field and Hilbert-algebra SELECTION constructions are not proved in this lesson.
