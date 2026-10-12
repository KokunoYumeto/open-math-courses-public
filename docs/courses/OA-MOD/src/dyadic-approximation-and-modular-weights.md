# Dyadic approximation and modular weights

Finite orbit relations approximate arrows. Compatible arrays do something stronger: they approximate the diagonal as well and yield increasing ordinary matrix algebras. The modular flow of the original weight need not preserve those scalar matrix algebras. It does preserve the larger algebras of measurable matrix fields.

Let \(R\) be an ergodic countable standard Borel principal relation with nonzero sigma-finite quasi-invariant measure \(\mu\). Choose an equivalent probability \(\rho\), and write \(\mu=h\rho\), where \(0<h<\infty\) almost everywhere. This choice is possible by weighting a disjoint finite-measure exhaustion with positive summable coefficients. Finite approximation will use \(\rho\); all modular formulas below retain \(h\), and therefore the original weight. Countable presentations and invariant conull restrictions are proved in 2. Countable presentations and null saturation.

We use the complete earlier programme proofs in Matching sets and nonsingular dyadic arrays, abbreviated **MATCH**; Balanced arrays and the hyperfinite finite factor, abbreviated **BAL**; and Towers and odometer orbits, abbreviated **TOWER**. Their precise proof roles are identified below.

## 1. What finite approximation means

For a partial orbit bijection \(T:D\to E\) and full-unit Borel subrelation \(F\), put

\[
 e_\rho(T,F)=\rho\{x\in D:(Tx,x)\notin F\}.
 \tag{AFM.1}
\]

This is the source-counting measure of the missing graph. Restricting \(T\) to its good set produces a partial map in \(F\) with exactly this error. Conversely, agreement with any map in \(F\) forces the corresponding arrow to belong to \(F\). Undefined values count as disagreements; no extension to all of \(D\) is required.

A finite relation has finite classes; a **bounded finite** relation has one finite bound for all class sizes. A **constant-size** relation has exactly \(q\) points per class. These are different conditions. Adding the missing diagonal to a partially supported finite relation preserves its bound, but can introduce singleton classes.

Call \(R\) hyperfinite when an increasing sequence of full-unit finite subrelations exhausts its arrows modulo source-counting null sets. Call (AFM.1) **finite local approximation** when every finite family of partial maps has arbitrarily small errors in one bounded finite subrelation.

These notions depend only on the measure class. For the local property, equivalent probabilities are uniformly absolutely continuous with respect to one another, so an error small in either probability is small in the other. For arrow-null exhaustion use

\[
 d\nu_s^\mu=(h\circ s)\,d\nu_s^\rho.
 \tag{AFM.2}
\]

The source's AF convention allows constant finite class size on each stage's own unit space. Adding the missing diagonal gives a hyperfinite exhaustion. Section 4 proves the converse in the ergodic setting, including the separate atomic cases. Thus the distinction between stage conventions is resolved by a theorem.

If \(F_n\) is a finite exhaustion, monotone convergence makes the errors of finitely many graphs small at one stage. On that stage replace classes larger than \(N\) by singletons. The discarded object sets decrease to the empty set, so taking \(N\) large adds arbitrarily small source errors. This proves hyperfiniteness implies finite local approximation, without a uniform bound on the original stages.

## 2. Arrays, balancing and exact refinement

An array on a positive support \(Z\) consists of disjoint positive cells \(Z_a\), indexed by a finite set, and orbit bijections

\[
 U_{ab}:Z_b\longrightarrow Z_a,\qquad
 U_{aa}=\mathrm{id},\qquad U_{ab}U_{bc}=U_{ac}.
 \tag{AFM.3}
\]

Their graphs form a constant-size relation on \(Z\). A refinement has cells \(Z'_{a,i}\) partitioning every old cell, and its equal-second-index maps restrict the old maps. A subarray is supported on one old cell.

For \(v_a=U_{a0}\), a subarray with cells \(Y_i\subset Z_0\) and maps \(W_{ij}\) gives the refinement

\[
 Z'_{a,i}=v_aY_i,\qquad
 U'_{(a,i),(b,j)}=v_aW_{ij}v_b^{-1}.
 \tag{AFM.4}
\]

The middle factors cancel under composition. Equal indices \(i=j\) give the restriction of \(v_av_b^{-1}=U_{ab}\), and their disjoint union recovers the old map. This proves the full supported-array assertion, including all domain and range requirements; it is MATCH Lemma 4.0.

**Balancing theorem.** On a nonatomic ergodic probability space, given a bounded finite \(F\subset R\), a finite partition and \(\varepsilon>0\), there is a full-support array of order \(2^k\) whose relation \(H\) satisfies

\[
 \nu_s^\rho(F\setminus H)<\varepsilon,
 \tag{AFM.5}
\]

and whose cell unions approximate every prescribed partition member in \(\rho\)-measure to within \(\varepsilon\).

The complete proof is MATCH Theorem 4.1, with precisely these three cases. First sort \(F\) into finitely many base pieces and their at-most-\(N\) sheets, also recording the partition membership of every sheet.

* If a finite invariant measure exists, normalize it to \(\eta(X)=1\). BAL Lemma 2.1 cuts every base piece into chunks of invariant mass \(2^{-k}\), transports each chunk to all its sheets, and puts the remainders together. With \(L\) base pieces, their total remainder has \(\eta\)-mass at most \(LN2^{-k}\). Fill it with the remaining equal-mass cells and match all cells using BAL Lemma 1.1. Common base matches cancel within each retained block, preserving its original arrows. Absolute continuity transfers a sufficiently small remainder to \(\rho\); at most \(N\) arrows are lost per source. No finite exhaustion is assumed in this balancing proof.
* In type III, remove a positive small part of each base so that the union of all its transported sheets has \(\rho\)-mass below \(\varepsilon/N\). Absolute continuity of the finitely many transported measures permits this. Keep the remaining sheets. Split the small remainder along the prescribed partition and then into enough positive pieces to make the total cell count a power of two. Every two positive cells are equivalent by the full type III matching proof in MATCH Theorem 3.1, also used in 2. The full type II and type III comparisons. Choose common matches on each retained block and arbitrary matches on the remainder. Only remainder sources lose arrows.
* With an equivalent infinite invariant measure \(\eta\), first retain finite-\(\eta\) subsets of each base whose sheets cover all but \(\rho\)-mass \(\varepsilon/N\). The remainder has infinite \(\eta\)-mass. Divide it into \(2^k\) infinite-mass pieces and pad every retained sheet with one of them; use the spare pieces as additional cells. In a reference cell choose disjoint finite pieces with the masses of the retained bases. Prescribe their matches to those bases and transport to the old sheets. The remaining domains and targets have infinite invariant mass and can be matched by MRA-02. These extensions retain the old arrows on the finite pieces. The padded remainder bounds both arrow and partition errors.

These are all possibilities by the invariant-measure/type criterion 4. The complete factor-type classification. Type II and III are nonatomic; the atomic case is treated in Section 4. In type III, equal probability masses are not needed, and transported cells need not keep their probability masses.

**Exact refinement with approximation.** Suppose finite local approximation holds and an old full-support array has order \(q=2^m\). Reduce each prescribed partial map to the old base:

\[
 T_j^{b,a}=v_b^{-1}T_jv_a.
 \tag{AFM.6}
\]

Finite local approximation passes to this positive reduction by restriction and normalization of the base probability. The finitely many measures \(B\mapsto\rho(v_aB)\) are absolutely continuous relative to that base probability. Choose a base error \(\delta\) so that each transported error has mass below \(\varepsilon/q^2\), and the transported union of all partition-error sets has mass below \(\varepsilon\).

Approximate the finitely many maps (AFM.6) by one bounded finite relation to error \(\delta/2\). Apply balancing on the base with missing-arrow error \(\delta/2\), and with partition errors whose union is smaller than \(\delta\). Lift its array by (AFM.4). Exact refinement is already proved. An original graph error is contained in the union of its \(q^2\) transported reduced errors, and the same transport controls the partition errors. This proves MATCH Lemma 5.1 and the complete refinement assertion of Takesaki XIII.3.21.

## 3. Towers and the correct cyclic boundary

Let \(T\) be ergodic, nonsingular and properly ergodic for \(\rho\). The recurrence proof 6. Recurrence and the induced transformation gives finite forward waiting times to every positive set on an invariant conull space.

Given height \(n\) and \(\varepsilon>0\), choose a positive set \(A\) so small that
\(\rho(T^{-j}A)<\varepsilon/n\) for \(0\leq j<n\). Nonatomicity and absolute continuity of these finitely many measures allow this choice. Put

\[
 \begin{aligned}
 r(x)&=\min\{k\geq0:T^kx\in A\},& A_k&=\{r=k\},\\
 F&=\bigcup_{l\geq1}A_{ln},& E&=T^{-(n-1)}F.
 \end{aligned}
 \tag{AFM.7}
\]

If \(x\in A_{ln}\) and \(0<j<n\), then \(r(T^jx)=ln-j\), so \(T^jx\notin F\). Hence \(F,T^{-1}F,\ldots,T^{-(n-1)}F\) are disjoint. If \(r(x)=ln+j\geq n\), \(0\leq j<n\), then \(T^jx\in F\). Therefore the tower with base \(E\) covers the complement of \(\bigcup_{j<n}T^{-j}A\), and has measure greater than \(1-\varepsilon\). This is the full nonsingular tower proof of TOWER Theorem 2.1 and Takesaki XIII.3.23.

To approximate powers \(|j|\leq m\), choose \(q\) large and a tower of height \(n=qm\). Its complement \(C\) can be made so small that

\[
 \rho(T^kC)<\varepsilon/2\quad(0\leq k\leq(q-1)m).
 \tag{AFM.8}
\]

Set \(F_i=\bigcup_{l<m}T^{im+l}E\). The \(F_i\)'s are disjoint, and their translates \(T^{n-m}F_i\) are separately disjoint. Thus

\[
 \sum_{i<q}\bigl(\rho(F_i)+\rho(T^{n-m}F_i)\bigr)\leq2.
 \tag{AFM.9}
\]

Choose a summand at most \(2/q\), translate the entire tower by \(T^{im}\), and close it into an \(n\)-cycle. Namely, follow \(T\) below the top, send the top to the base by \(T^{-(n-1)}\), and fix the translated complement. The resulting \(S\) is Borel, nonsingular, satisfies \(S^n=1\), and has orbits within \(R_T\). For \(|j|\leq m\), disagreement lies in the complement and its bottom and top \(m\)-bands. Hence

\[
 \rho\{S^j\ne T^j\}\leq\varepsilon/2+2/q<\varepsilon
 \tag{AFM.10}
\]

after choosing \(q>4/\varepsilon\). The top band is translated by \(n-m\), not \(n-m-1\). Both terms in (AFM.9) are essential. This is TOWER Theorem 3.1.

Every partial \(R_T\)-map is a countable disjoint union of restrictions of powers of \(T\). Keep finitely many pieces to lose arbitrarily little source probability, then apply (AFM.10) to their powers. The finite relation of \(S\) proves finite local approximation.

There is also a direct increasing exhaustion, TOWER Corollary 3.2. Choose finite relations \(H_k\) so that the union of power graphs \(|j|\leq k\) misses \(H_k\) in source measure below \(2^{-k}\), and put

\[
 R_n=\bigcap_{k\geq n}H_k.
 \tag{AFM.11}
\]

Each is bounded finite, and they increase. For fixed \(j\) and \(n\geq|j|\), its missing graph has measure at most \(\sum_{k\geq n}2^{-k}\), tending to zero. Removing the countable union of exceptional source sets and its null saturation makes \(\bigcup_nR_n=R_T\) exactly. No monotonicity of the original cyclic approximants was assumed.

## 4. The dyadic criterion and the whole measured model

On a nonatomic ergodic standard probability space the following are equivalent:

1. Hyperfiniteness, or the source constant-size AF convention.
2. Finite local approximation.
3. An increasing full-unit exhaustion \(F_k\) with every class of size \(2^k\).
4. Generation by one ergodic nonsingular transformation.

Here is the complete proof route of MATCH Theorem 5.2. Section 1 proves the first implication to local approximation. Starting from the identity array, apply Section 2 repeatedly to the first \(n\) presenting maps and the first \(n\) members \(B_j\) of a countable separating Borel generating family. Make the graph and partition errors below \(2^{-n}\), and choose strictly increasing dyadic orders \(2^{m_n}\). Exact refinement preserves every previous arrow. The increasing union misses no presenting graph except on a null set; delete all its null source exceptions and their saturation.

Label successive refinements by binary words. Every point acquires an infinite address \(\Phi(x)\). For each fixed \(B_j\), the errors of its cell-union approximations are summable. The union bound for the tails of these error sets shows that their indicators eventually agree with \(\mathbf1_{B_j}\) almost everywhere. On a common invariant conull set, equal addresses therefore imply equal membership in every \(B_j\), hence equal points. Apply the countable-section Borel image theorem used in GMB-02 to the graph of this injection, and to its restrictions to Borel sets. Its image and inverse are Borel. This supplies the realization step in MATCH Theorem 5.2.

An old array map changes its prefix and preserves later labels by (AFM.4). Conversely any finite prefix change occurs at a sufficiently long stage. Thus the address image is saturated for tail equivalence, and \(\Phi\) identifies the whole relation with that relation on its image. Extend the pushforward probability \(\nu=\Phi_*\rho\) by zero to all of \(\{0,1\}^{\mathbb N}\). It is nonatomic, ergodic and quasi-invariant under finite coordinate changes. Interpolate a jump of \(d\) binary digits by grouping the fine cells according to their first \(i\) new digits and summing the transports that preserve the remaining \(d-i\) digits. This yields exactly the old stage at \(i=0\), the fine stage at \(i=d\), and every intermediate class size. Thus (3) holds. It plainly implies either finite-exhaustion convention.

For (4), remove both eventually-zero and eventually-one sequences. These are countable invariant tail classes, hence \(\nu\)-null. Addition by one uses the first zero, resets preceding ones, and preserves all later digits; borrowing uses the first one. On the retained space both operations stop and are inverse Borel maps. If two sequences agree past \(N\), subtracting the integers represented by their first \(N\) digits gives the iterate taking one to the other: addition modulo \(2^L\) verifies this for every \(L\geq N\). Thus the orbits are precisely the tail classes. Its countable carry partition proves nonsingularity, and the equality of relations gives ergodicity. This is TOWER Theorem 4.1, proving the implication to (4); Section 3 proves the converse. This transformation is the **dyadic odometer**.

If an invariant probability exists, perform balancing using that probability. Every prefix of length \(k\) then has mass \(2^{-k}\), so \(\nu\) is the fair product probability. It is also the Haar probability of the compact binary group: coordinate translations permute cylinders of the same length, and invariance forces their equal masses. Cylinders determine the measure. This proves uniqueness in the invariant finite case, including the measured relation and its diagonal. For invariant infinite measure, partition into equal finite-mass sheets, reduce to one, apply the fair model and then the product splitting 3. Splitting into countably many equivalent sheets through 4. The algebra and the amplified weight. This is the complete infinite-measure proof of BAL Proposition 6.1. General type III laws are only quasi-invariant; they need not be fair.

The atomic alternatives are part of the theorem's scope. MATCH Proposition 5.4 proves that an atom forces a conull countable orbit. On \(n\) points the complete relation is AF and cyclically generated, but cannot have classes of size \(2^k>n\). On a countably infinite orbit, enumerate by \(\mathbb N\); blocks with equal \(\lfloor a/2^k\rfloor\) give the dyadic exhaustion. Finite binary expansions identify this with the tail class of zero, with arbitrary positive summable point masses. A separate enumeration by \(\mathbb Z\) supplies a bilateral generator. Finite-carry addition on the eventually-zero class is not onto and is not the generator used there.

## 5. Scalar matrices and modular matrix fields

Take the compatible arrays constructed in Section 4, of orders \(q_n=2^{m_n}\). Let \(F_n\) be their relations and \(e_{ab}^{(n)}=V_{U_{ab}^{(n)}}\) their orbit operators. Row counting gives the ordinary matrix-unit identities and

\[
 \mathcal D_n=\operatorname{span}\{e_{ab}^{(n)}\}\cong M_{q_n}(\mathbb C),
 \qquad
 e_{ab}^{(n)}=\sum_i e_{(a,i),(b,i)}^{(n+1)}.
 \tag{AFM.12}
\]

These are unital increasing scalar matrix algebras.

They generate \(M=M(R,\rho)\). Indeed, the cell partitions approximate every \(B_j\). For any \(\xi\in L^2(R,\nu_s^\rho)\), the finite measure

\[
 \lambda_\xi(B)=
 \int_X\sum_{yRx}1_B(y)|\xi(y,x)|^2\,d\rho(x)
 \tag{AFM.13}
\]

is absolutely continuous relative to \(\rho\), because null sets have null saturations. Thus small symmetric-difference errors give strong convergence of the corresponding diagonal projections. The generated algebra contains the full diagonal. For a presenting partial map \(g\), restrict to
\(D_{g,n}=\{x:(gx,x)\in F_n\}\). On each source/target cell pair this restriction is the unique array map restricted to a measurable subdomain. Its operator is a finite sum of matrix units times diagonal projections. The domains increase to the whole domain of \(g\), so these restricted operators converge strongly to \(V_g\). This proves

\[
 M=\left(\bigcup_n\mathcal D_n\right)''.
 \tag{AFM.14}
\]

The multiplying diagonal projections belong to the limiting algebra; they need not belong to \(\mathcal D_n\). This is the full argument of MATCH Corollary 5.3.

Fix one stage, suppress \(n\), and let \(B=Z_0\) be its base, \(v_a:B\to Z_a\) its sheets. Let \(\nu\) be the pushforward of \(\rho\) by the class selector. The finite-sheet proof 4. Finite sheets without a probability assumption through 5. The matrix weight and its analytic cutoffs supplies measurable functions

\[
 p_a>0,\qquad \sum_{a<q}p_a=1,\qquad
 \rho(v_aA)=\int_Ap_a\,d\nu.
 \tag{AFM.15}
\]

The larger algebra \(\mathcal N_F\), generated by all diagonal functions and these matrix units, is
\(L^\infty(B,\nu)\bar\otimes M_q\). Central functions are the diagonal functions constant on each \(F\)-class; expanding entries in matrix units proves the assertion. For each source \(x\), its counted \(R\)-orbit is the disjoint union of \(F\)-classes, and the field acts as the corresponding \(q\)-dimensional block on each class. Its norm is therefore the essential supremum of the field norms, as in the faithful restriction to \(L^2(F,\nu_s^\rho)\). Increasing bounded positive fields converge blockwise and hence strongly by dominated convergence. Thus this ambient representation is faithful and normal, with the same matrix-field algebra on the restricted space.

Write \(h_a(b)=h(v_ab)\), \(w_a=h_ap_a\), and \(D_h(b)=\operatorname{diag}(w_a)\). The restricted original weight and its modular action are

\[
 \begin{split}
 \varphi_\mu(A)&=\int_B\sum_a w_a(b)A_{aa}(b)\,d\nu(b),\\
 \sigma_t^{\varphi_\mu}(A)(b)&=D_h(b)^{it}A(b)D_h(b)^{-it}.
 \end{split}\tag{AFM.16}
\]

This follows from the diagonal weight and the arrow modulus
\(h_ap_a/(h_bp_b)\), by 2. The weight model at infinite mass. It retains infinite values and does not replace \(\mu\) by \(\rho\). In particular \(\mathcal N_F\) is invariant.

The scalar matrix algebra \(\mathcal D_F\) is invariant exactly when there are constants \(c_a>0\), \(\sum_ac_a=1\), and a positive finite measurable \(r\) such that

\[
 w_a(b)=r(b)c_a\quad\text{for every }a,\ \nu\text{-almost everywhere}.
 \tag{AFM.17}
\]

Sufficiency follows by cancelling \(r\). For necessity, the \(ab\)-entry of
\(\sigma_t(e_{ab})\) is \((w_a/w_b)^{it}\). Membership in the scalar matrix algebra forces this entry to be constant over \(B\), for every rational \(t\). Delete the common exceptional null set. Comparing two remaining points and using \(t=1/l\) for all positive integers \(l\) forces their logarithmic ratios to agree. Thus all \(w_a/w_b\) are constant. Dividing by \(r=\sum_aw_a\) gives (AFM.17).

If \(0<\mu(X)<\infty\), the normalized restriction to \(\mathcal D_F\) has diagonal masses \(\mu(Z_a)/\mu(X)\). Under (AFM.17) they are \(c_a\), and its modular group agrees with the ambient restriction. Without (AFM.17) that assertion is false. If \(\mu(X)=\infty\), even a modular-invariant \(\mathcal D_F\) need not have a semifinite restricted weight: under (AFM.17), every nonzero positive scalar matrix has infinite weight. Each matrix field still has a faithful normal semifinite weight, since the finite positive \(w_a\)'s can be bounded above and below on a finite-measure exhaustion of the base.

## 6. Expectations that retain every diagonal weight

For any full-unit finite subrelation \(F\), let

\[
 H_F=L^2(F,\nu_s^\rho),\qquad P_F=m_{1_F}
 \tag{AFM.18}
\]

inside \(H_\rho=L^2(R,\nu_s^\rho)\). This is a Hilbert-space projection on arrows, not a corner projection obtained from an object subset.

There is a faithful normal conditional expectation

\[
 E_F:M\longrightarrow\mathcal N_F
 \tag{AFM.19}
\]

which restricts each convolution kernel to \(F\). Here is a construction without presupposing an expectation theorem. The diagonal and partial orbit operators have a unital star algebra as their linear span, since products are again partial orbit maps with diagonal coefficients. If \(g\) is such a map, then compression to \(H_F\) keeps exactly the sources with \((gx,x)\in F\):

\[
 P_FV_gP_F\big|_{H_F}
   =V_{g|D_g}\big|_{H_F},\qquad
 D_g=\{x\in\operatorname{dom}g:(gx,x)\in F\}.
 \tag{AFM.20}
\]

Indeed, if \(yFx\), the additional condition \(gyFx\) is equivalent to \(gyFy\). On diagonal coefficients compression simply restricts the representation.

The compressed operators therefore belong to the standard matrix-field algebra on \(H_F\). Bounded strong density of the generating star algebra, followed by normal compression, proves the same for every \(x\in M\). Compose this compression with the inverse of the faithful normal representation of \(\mathcal N_F\) on \(H_F\). This defines a normal unital completely positive map into \(\mathcal N_F\) fixing that algebra. Left multiplication by \(\mathcal N_F\) preserves both \(H_F\) and its orthogonal complement, so \(P_F\) commutes with it. This proves the bimodule identity and hence (AFM.19).

Let \(\Omega=1_{\{(x,x):x\in X\}}\), the reference probability GNS vector. Since \(P_F\Omega=\Omega\), compression preserves the reference state. It also preserves its diagonal expectation:

\[
 E_{\mathrm{diag}}E_F=E_{\mathrm{diag}}.
 \tag{AFM.21}
\]

The equality holds on the generating kernels because every diagonal arrow is in \(F\), and extends by normality. Consequently \(E_F\) preserves every diagonal weight \(\varphi_{k\rho}\), \(0<k<\infty\) almost everywhere, including \(\varphi_\mu\) and weights of infinite total mass. Faithfulness follows already from preservation of the faithful reference state.

For increasing stages \(F_n\), kernel restriction and normality give

\[
 E_nE_l=E_{\min(n,l)},\qquad
 \Lambda_\rho(E_nx)=P_n\Lambda_\rho(x).
 \tag{AFM.22}
\]

Since \(P_n\uparrow1\), the GNS vectors converge. This implies strong convergence of \(E_nx\) to \(x\): on the dense vectors \(a'\Omega\), \(a'\in M'\),

\[
 \|(E_nx-x)a'\Omega\|
 \leq\|a'\|\,\|(E_nx-x)\Omega\|\longrightarrow0.
\]

The common bound \(\|E_nx-x\|\leq2\|x\|\) extends it to all vectors. Apply the same argument to \(x^*\) to obtain strong* convergence. For the density used here, RWT-05 gives \(J_\rho M J_\rho=M'\), and \(J_\rho\Omega=\Omega\) since the diagonal modulus is one. Applying \(J_\rho\) to the dense GNS set \(M\Omega\) gives the density of \(M'\Omega\).

All these expectations commute with the original modular group: on a kernel, both sides multiply by its modulus to the power \(it\) and by \(1_{F_n}\), in either order. Normality again extends the identity. Thus the matrix-field exhaustion, unlike a general scalar matrix exhaustion, retains the original modular dynamics exactly.

## 7. Relative domains through finite stages

Let \(\psi=\varphi_{k\rho}\) and \(\varphi=\varphi_{h\rho}\), where \(h,k\) are arbitrary positive finite measurable functions. Use the common reference Hilbert space \(H_\rho\) and the canonical source-coordinate GNS transports of 3. Unitary transport between equivalent measures through 6. The normalized cocycle and modular action. With \(\delta_\rho\) in the range-over-source convention, put

\[
 \kappa(y,x)=\frac{k(y)}{h(x)}\delta_\rho(y,x).
 \tag{AFM.23}
\]

The complete earlier relative-operator proof gives

\[
 \begin{split}
 \Delta_{\psi,\varphi}&=m_\kappa,\\
 (A_{k,h}\xi)(y,x)&=
       \left(\frac{k(x)}{h(y)}\right)^{1/2}\overline{\xi(x,y)},\\
 A_{k,h}&=J_\rho m_\kappa^{1/2}.
 \end{split}\tag{AFM.24}
\]

The maximal domains, for every \(z\in\mathbb C\), are

\[
 \begin{split}
 D(A_{k,h})&=\{\xi\in H_\rho:\int_R\kappa|\xi|^2\,d\nu_s^\rho<\infty\},\\
 D(\Delta_{\psi,\varphi}^{\,z})
 &=\{\xi\in H_\rho:\int_R\kappa^{2\operatorname{Re}z}|\xi|^2\,d\nu_s^\rho<\infty\}.
 \end{split}\tag{AFM.25}
\]

These are genuine domains; finite class size does not make an unbounded measurable coefficient bounded over its base.

Since each \(F_n\) is symmetric under reversing arrows, \(P_n\) commutes with \(J_\rho\) as well as all multiplication powers. It reduces both operators and their maximal domains. Their restrictions to \(H_{F_n}\) are precisely the relative operators of the restricted weights on \(\mathcal N_{F_n}\): the kernel and GNS-core calculation is the same one on \(F_n\), and the graph-core proof RWT-04 identifies its closure.

For example, denote the base point by \(\beta\) and use matrix indices \(i,j\). In the coordinates \(\eta_{ij}(\beta)=\sqrt{p_j(\beta)}\xi(v_i\beta,v_j\beta)\), write \(h_i(\beta)=h(v_i\beta)\), \(k_i(\beta)=k(v_i\beta)\). Then

\[
 \begin{split}
 (\Delta_{\psi,\varphi}\eta)_{ij}
     &=\frac{k_ip_i}{h_jp_j}\eta_{ij},\\
 (A_{k,h}\eta)_{ij}
     &=\left(\frac{k_jp_j}{h_ip_i}\right)^{1/2}\overline{\eta_{ji}}.
 \end{split}\tag{AFM.26}
\]

All functions in (AFM.26) are evaluated at the same base point. These are the full matrix-field formulas of GMB-06, with both weights retained.

For every \(\xi\in D(\Delta_{\psi,\varphi}^{\,z})\),

\[
 \|P_n\xi-\xi\|^2+
 \|\Delta_{\psi,\varphi}^{\,z}(P_n\xi-\xi)\|^2
 =
 \int_{R\setminus F_n}(1+\kappa^{2\operatorname{Re}z})|\xi|^2\,d\nu_s^\rho
 \longrightarrow0.
 \tag{AFM.27}
\]

Dominated convergence proves the assertion because the displayed integrand is integrable on the full domain. With \(z=1/2\), \(J_\rho\)'s isometry gives the analogous graph convergence for \(A_{k,h}\). Thus the union of the finite-stage maximal domains is a graph core for every displayed power and mixed operator.

Within each stage, further restrict to a finite-measure part of the base, bounds on all \(p_a,h_a,k_a\) and their reciprocals, and bounded matrix entries. These cutoffs are graph-dense by the same dominated-convergence argument, and the GNS kernels on them are bounded and square integrable for both weights. This proves the concrete core assertion without treating an infinite weight's identity as a GNS vector.

The exact normalized Connes cocycle is

\[
 [D\psi:D\varphi]_t=M_{(k/h)^{it}}.
 \tag{AFM.28}
\]

It belongs to the common diagonal, hence to every \(\mathcal N_{F_n}\), and is the cocycle of both restricted weights there. The quotient of the two relative imaginary powers cancels the source density and \(\delta_\rho\), proving the formula with its actual weight normalization. This compatibility does not imply membership in the smaller \(\mathcal D_n\).

## 8. Examples and complete solutions

**Problem 1: a finite matrix stage that the flow leaves.** Use the fair binary tail relation and its first-digit array. Write \(a\in\{0,1\}\) for the first digit and \(s\) for the second, and change the fair measure by

\[
 h_{0,0}=h_{0,1}=h_{1,0}=1,\qquad h_{1,1}=3.
\]

Normalize the resulting measure to a probability.

**Solution.** The unnormalized total is \(3/2\), so multiply \(h\) by \(2/3\). This common factor does not affect the modular flow. For the first-digit matrix unit,

\[
 \sigma_t(e_{01})=
 \begin{cases}
 e_{01},&s=0,\\
 3^{-it}e_{01},&s=1.
 \end{cases}
 \tag{AFM.29}
\]

For example at \(t=1\) these two coefficients differ, so the image is not in the scalar first-digit algebra. Its two state masses are instead \(1/3,2/3\), so its own restricted-state modular group multiplies \(e_{01}\) by \(2^{-it}\). At the two-digit stage the four density values are constants on each prefix cell, and the scalar stage is invariant. Hyperfiniteness alone made no assertion about invariance of every chosen stage.

**Problem 2: an invariant stage with an infinite restricted weight.** On the same first-digit array, let \(r\) be a positive finite function of the remaining tail with infinite integral, and put \(h(a,\text{tail})=r(\text{tail})\).

**Solution.** Such an \(r\) exists: partition the nonatomic tail into positive sets \(B_j\) and set \(r=1/\rho_{\mathrm{tail}}(B_j)\) on \(B_j\). It is finite at every point of the partition and its integral is infinite. Here \(w_0=w_1=r/2\), so the first-digit scalar algebra is fixed pointwise by the modular flow. Nevertheless every nonzero positive scalar matrix has infinite weight. The ambient and matrix-field weights remain semifinite, by bounded-density cutoffs. The restricted scalar weight is not semifinite.

**Problem 3: a proper domain already at one dyadic stage.** Let \(b\) be a uniform \((0,1)\) coordinate of the fair tail, obtained by binary expansion after discarding the null ambiguity set. Put \(h(0,b)=2b\), \(h(1,b)=2(1-b)\). This gives a probability equivalent to the original fair law.

**Solution.** In the two-sheet field, the weight densities are \(w_0=b\), \(w_1=1-b\). The vector with the \(01\)-entry identically one and other entries zero is in \(L^2((0,1);\mathrm{HS}_2)\). Its squared square-root modular norm is

\[
 \int_0^1\frac{b}{1-b}\,db=\infty.
 \tag{AFM.30}
\]

Thus it is outside \(D(\Delta^{1/2})\), even at this finite stage. Bounds on class size cannot replace the maximal-domain conditions.

**Problem 4: which approximation is an expectation?** In a finite complete relation, split the objects into disjoint blocks and let \(F\) retain exactly the within-block arrows.

**Solution.** On matrices \(E_F\) deletes the off-block entries:

\[
 E_F(A)=\sum_C P_CA P_C,
 \tag{AFM.31}
\]

where \(C\) runs over the blocks. The orthogonal block projections sum to one, so this map is unital, completely positive and bimodular over the block algebra. It preserves every diagonal weighted trace because no diagonal entry is removed. A general approximation by scalar array matrices does not have this kernel-cutting formula. In the measured construction, (AFM.20) is the corresponding compression on arrow space, and (AFM.27) controls unbounded relative operators as well as bounded elements.

## References

Masamichi Takesaki, *Theory of Operator Algebras III*, Chapter XIII, Definitions 3.15–3.16, 3.18–3.19 and 3.24, Theorems 3.17 and 3.22, and Lemmas 3.20–3.21 and 3.23, printed pp. 38–47. [Publisher record](https://doi.org/10.1007/978-3-662-10453-8).

The earlier programme proofs named above include the nonsingular balancing cases, full recurrence and tower arguments, binary coding, atomic qualifications and matrix-field modular domains. The missing-graph estimate uses set difference; retained sheet counts include every base chunk; the upper boundary in the cyclic construction uses \(n-m\); and the odometer domain removes both exceptional tail classes. The modular-stage, expectation and graph-convergence arguments here are independently written course exposition. New text is released under CC0.
