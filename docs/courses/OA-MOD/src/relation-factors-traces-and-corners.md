# Relation factors, traces and corners

A measured relation determines its factor type through two pieces of information: whether one countable orbit carries the whole measure, and whether the measure class contains a finite or infinite invariant measure. The size of a presenting group does not determine either fact. We prove the precise classification, then compute what happens to traces and modular cocycles in a measurable corner.

Throughout, a countable group acts by nonsingular Borel bijections on a nonzero standard Borel sigma-finite space \((X,\mu)\). Write \(R\) for its principal orbit relation, \(M=\mathcal M(R,\mu)\), \(D=L^\infty(X,\mu)\) for the range-coordinate diagonal, and \(E:M\to D\) for the faithful normal diagonal expectation. The arrows are \((y,x):x\to y\), and \(\nu_s\) counts their ranges over each source. No freeness assumption is made.

## 1. Whole operator fields and exact proof inputs

The complete measurable-field theorem is Relation kernels and modular coordinates, Theorem 4.1 and the sigma-finite transport following Proposition 6.0. It says precisely

\[
 \begin{gathered}
 T\in M\quad\Longleftrightarrow\quad
 (T\xi)(\,\cdot\,,x)=T_x\xi(\,\cdot\,,x),\\
 T_x\in B(\ell^2([x]_R)),\qquad
 \mathop{\rm ess\,sup}_{x}\|T_x\|<\infty,\\
 T_x=T_y\quad(x\sim y)
 \quad\hbox{on an invariant conull set}.
 \end{gathered} \tag{RFT.1}
\]

The field must be measurable: enumerate distinct orbit points by their first occurrence in an enumeration of the acting group and require all matrix coefficients in that enumeration to be measurable. The bases for \(T_x=T_y\) are indexed by the actual points of the same orbit. The theorem also proves
\(\|T\|=\mathop{\rm ess\,sup}_x\|T_x\|\).

Its proof identifies the full commutant with source multiplications and source shifts, realizes the variable fibres inside \(L^2(X;\ell^2(\mathbb N))\), and tests shift commutation on countably many coefficients. The reverse inclusion uses the double commutant theorem. Both directions, and the lower norm bound, are proved there. This is the full assertion of Takesaki XIII.2, Corollary 2.8; it does not require a measurable space parametrizing the orbits.

Here are the other exact earlier inputs.

- Orbits, stabilizers, and relation algebras, Theorem 4.2 and Corollary 4.3 prove that \(D\) is maximal abelian and that \(Z(M)=D^R\). Their probability proof transfers through the source-coordinate unitary of 3. Unitary transport between equivalent measures.
- 4. Every semifinite trace is preserved through 7. Central density and scalar ambiguity prove trace preservation by an expected maximal abelian subalgebra, classify all relation traces by equivalent sigma-finite invariant measures, and prove uniqueness up to a scalar in the ergodic case.
- Projections and types of von Neumann algebras, Theorem 7.2, Corollary 7.3 and Corollary 10.4 prove the factor-type alternatives and the form \(B(K)\) of a type I factor.
- Traces, part A, Corollary 5.12 and Theorem 6.7 prove that a finite factor has a faithful normal tracial state and that a semifinite algebra has a faithful normal semifinite trace. Their full proofs, with their earlier inputs, are the programme trace-existence results also identified in The programme arbitrary-algebra trace-existence theorem through Exact theorem owners and the FT/MB applications.
- 6. The normalized cocycle and modular action through 7. Reduction to a measurable subset give normalized density cocycles and the faithful two-endpoint corner representation.

We use “finite projection” in the Murray–von Neumann sense: a projection is not equivalent inside the algebra to a proper subprojection. “Finite trace” describes a numerical value and is a different condition until its equivalence is proved below.

## 2. An expected diagonal in a type I factor is atomic

We first give a trace argument for the type I obstruction.

**Lemma.** Suppose a standard sigma-finite abelian algebra \(A\) is maximal abelian in \(B(K)\) and admits a normal conditional expectation. Then \(A\) is atomic, and its minimal projections have rank one.

**Proof.** Give \(B(K)\) its usual faithful normal semifinite operator trace \(\operatorname{Tr}\). Its full construction, including arbitrary-cardinality sums, is the example in 8. Tests of the hypotheses and conventions. By EDT-04, its restriction to \(A\) is semifinite and its finite-trace projections increase to \(1\).

For a nonzero projection \(e\in A\), some finite-trace projection \(q\in A\) has \(eq\ne0\). The projection \(f=eq\) has finite trace. A projection of finite operator trace has finite rank: each finite orthonormal family in its range contributes its cardinality to the trace sum. Thus \(fAf\) is a finite-dimensional abelian algebra and contains a minimal nonzero projection \(p\). One can see the latter directly by taking a nonzero projection of least rank in \(fAf\); a proper nonzero subprojection would have smaller rank. Since every \(A\)-subprojection of \(p\) also lies under \(f\), \(p\) is minimal in \(A\).

We have shown that every nonzero \(e\in A\) majorizes an atom. A maximal orthogonal family of these atoms has sum \(1\), since a nonzero complement would contain another atom. Finally, for an atom \(p\), \(pAp=\mathbb Cp\): a nonscalar self-adjoint element would have a proper nonzero spectral projection. Every \(T\in pB(K)p\) then commutes with \(A\), because \(A\) is block diagonal relative to \(p\) and scalar on that block. Maximal abelianness puts \(T\) in \(pAp\). Hence

\[
 pB(K)p=\mathbb Cp,
 \tag{RFT.2}
\]

which forces \(\dim pK=1\). \(\square\)

An atom of a standard sigma-finite measure algebra is represented by a point of positive finite mass. Here is the measure-theoretic detail. A finite-measure cover meets an atom in a set representing the same atom and of positive finite measure. For each member of a countable Borel separating family, choose the side containing that atom modulo null sets. Their intersection retains its positive mass, and contains at most one point. The point has finite mass by sigma-finiteness.

Consequently, if \(M\) is a type I factor, transfer its expected diagonal through a normal isomorphism \(M\cong B(K)\). The lemma gives a point atom \(x\). Its countable saturation \([x]_R\) is measurable, invariant and of positive measure. Ergodicity makes it conull. This proves the difficult direction of the type I criterion using the whole-trace preservation theorem.

## 3. A conull orbit is a full matrix algebra

Suppose the measure is concentrated on one orbit \(O\). Countability implies that some point has positive mass, and nonsingularity propagates positive mass to every point of \(O\). Put \(p_x=\mu(\{x\})\); each \(p_x\) is finite and nonzero.

The unitary

\[
 (U\xi)_{yx}=\sqrt{p_x}\,\xi(y,x)
 \tag{RFT.3}
\]

identifies \(L^2(R,\nu_s)\) with the Hilbert–Schmidt matrix space on \(\ell^2(O)\). The relation algebra acts by multiplication on rows. For each \(i,j\in O\), restrict a group element carrying \(j\) to \(i\) to the singleton \(\{j\}\). Its partial orbit operator becomes the matrix unit \(E_{ij}\). Finite matrix blocks converge strongly to every operator in \(B(\ell^2(O))\): if \(P_n\uparrow1\) are finite-coordinate projections, then \(P_nTP_n\to T\) strongly, with norm bounded by \(\|T\|\). Conversely every relation generator acts on rows by an operator on \(\ell^2(O)\). Therefore

\[
 M=B(\ell^2(O)),\qquad
 D=\ell^\infty(O),\qquad E(T)_x=T_{xx}.
 \tag{RFT.4}
\]

The Hilbert–Schmidt realization retains a source-coordinate multiplicity; it does not identify the represented Hilbert space with \(\ell^2(O)\).

Every invariant sigma-finite measure equivalent to \(\mu\) has equal positive mass \(c\) at all points, because singleton partial orbit maps preserve it. It is \(c\) times counting measure. Thus

\[
 \tau_c(T)=c\sum_{x\in O}T_{xx},\qquad T\geq0.
 \tag{RFT.5}
\]

The sum is the increasing supremum over finite subsets and may be infinite. It is finite at \(1\) exactly when \(O\) is finite.

Together with Section 2, this proves

\[
 M\text{ is type I}
 \quad\Longleftrightarrow\quad
 \text{one orbit is conull}.
 \tag{RFT.6}
\]

A conull orbit of \(n\) points gives type \(I_n\); an infinite conull orbit gives type \(I_\infty\).

## 4. The complete factor-type classification

The center formula in Section 1 first gives

\[
 M\text{ is a factor}
 \quad\Longleftrightarrow\quad R\text{ is ergodic}.
 \tag{RFT.7}
\]

Indeed an invariant set gives a central projection. Conversely rational level sets make every bounded invariant real function constant in an ergodic relation; applying this to real and imaginary parts leaves only scalar central elements.

Assume now that \(R\) is ergodic. The complete alternatives are:

| Measured relation | Equivalent invariant measure | Factor type |
| --- | --- | --- |
| One conull orbit, with \(n<\infty\) points | A positive multiple of counting measure | \(I_n\) |
| One conull infinite orbit | A positive multiple of counting measure | \(I_\infty\) |
| No conull orbit | A finite invariant measure exists | \(II_1\) |
| No conull orbit | An infinite sigma-finite invariant measure exists | \(II_\infty\) |
| No equivalent sigma-finite invariant measure | None in that category | \(III\) |

Here and below an invariant measure has the same null sets as \(\mu\), and is nonzero.

**Proof of the type II and III rows.** An equivalent finite invariant measure \(\eta\) gives, by EDT-05, the faithful normal tracial state

\[
 t(T)=\frac1{\eta(X)}\int_X E(T)\,d\eta.
 \tag{RFT.8}
\]

If \(v^*v=1\), the trace identity gives \(t(1-vv^*)=0\), so faithfulness implies \(vv^*=1\). Thus \(M\) is finite. Excluding a conull orbit excludes type I by (RFT.6), so the factor alternatives give type \(II_1\). Conversely, a type \(II_1\) factor has the faithful normal tracial state supplied by Traces, Corollary 5.12. EDT-05 produces a finite invariant \(\eta\); (RFT.6) rules out a conull orbit.

An infinite sigma-finite invariant measure gives a faithful normal semifinite trace. Absence of a conull orbit excludes type I. The factor cannot be type \(II_1\): that case would also give a finite equivalent invariant measure, whereas EDT-07 makes any two invariant measures positive scalar multiples. A finite nonzero scalar cannot turn infinite total mass into finite mass. The remaining semifinite alternative is \(II_\infty\). Conversely a type \(II_\infty\) factor has a faithful normal semifinite trace by Traces, Theorem 6.7. EDT-05 gives an invariant sigma-finite measure, and it must be infinite by the type \(II_1\) implication just proved.

Finally EDT-06 equates existence of an equivalent sigma-finite invariant measure with existence of a faithful normal semifinite trace. By the factor alternatives and Traces, Theorem 6.7, its failure is precisely type III. \(\square\)

These prove all five clauses of Takesaki XIII.2, Theorem 2.10, with “transitive” understood modulo null sets and with its finite-factor clause corrected. The earlier proof and correction appear in Diagonal expectations and invariant measures, Theorems 4.1, 5.1, 5.2, 5.4 and Example 5.3.

The printed condition “the group is infinite” cannot replace absence of a conull orbit. Let \(\mathbb Z\) act on five points by a five-cycle, with uniform measure. It is ergodic, its group is infinite and its measure is finite and invariant. Every stabilizer is \(5\mathbb Z\), and (RFT.4) gives \(M_5(\mathbb C)\). This is the existing counterexample, not a new source correction.

Sigma-finiteness is also essential. For any nonsingular action,

\[
 \eta_\infty(B)=
 \begin{cases}
 0,&\mu(B)=0,\\
 \infty,&\mu(B)>0
 \end{cases}
 \tag{RFT.9}
\]

is an invariant measure with the same null sets. For a disjoint countable union, either every member is null, or one has positive measure; these two cases prove countable additivity. Nonsingularity proves invariance. Every finite-measure set for \(\eta_\infty\) is null, so it is neither sigma-finite nor semifinite on a nonzero space. It supplies none of the traces in the table.

## 5. Ergodicity and trace normalization after restriction

Let \(B\subset X\) have positive measure and let \(e=M_{1_B}\). The reduced relation is \(R_B=R\cap(B\times B)\). Its faithful standard representation of \(eMe\) is

\[
 H_B=eJeJH=L^2(R_B,\nu_s|_{R_B}),
 \tag{RFT.10}
\]

by RWT-07. Both endpoints are cut down; \(eH\) alone is larger.

If \(R\) is ergodic, so is \(R_B\). To prove this, take a reduced-invariant measurable \(C\subset B\). After removing null exceptional sets, its full saturation \([C]_R\) satisfies
\([C]_R\cap B=C\). For invariance modulo null sets, first discard the countably many exceptional sets for the restricted partial group maps and their saturations; nonsingularity keeps them null. The set \([C]_R\) is a countable union of group translates and is invariant in \(X\). It is null or conull, making \(C\) null or conull in \(B\). This proves the assertion without requiring \(B\) itself to be invariant.

Suppose \(\eta=q\mu\) is an equivalent sigma-finite invariant measure and
\(0<\eta(B)<\infty\). On the entire positive cone of \(eMe\), its normalized trace is

\[
 t_B(T)=\frac{\tau_\eta(T)}{\eta(B)}
       =\int_B E(T)\,\frac{q}{\eta(B)}\,d\mu.
 \tag{RFT.11}
\]

The restricted expectation is the diagonal expectation of \(R_B\); the formula follows from EDT-05 and its corner representation. Invariance of \(\eta|_B\) under every partial \(R_B\)-map proves traciality. Its value at \(e\) is one.

Let \(\varphi_B=\varphi_\mu|_{eMe}\), which is faithful normal semifinite even when \(\mu(B)=\infty\). RWT-06–07 give the normalized cocycle

\[
 [Dt_B:D\varphi_B]_t
   =eM_{(q/\eta(B))^{it}}e .
 \tag{RFT.12}
\]

If \(0<\mu(B)<\infty\), set \(\psi_B=\varphi_B/\mu(B)\). Then

\[
 [Dt_B:D\psi_B]_t
   =eM_{(\mu(B)q/\eta(B))^{it}}e.
 \tag{RFT.13}
\]

Thus normalizing the reference weight contributes a scalar character. It cannot be discarded merely because it does not affect conjugation. Both formulas are fixed by the relative-operator construction of the earlier lesson, not only by the induced modular automorphisms.

## 6. Finite projections and the types of diagonal corners

Assume \(R\) is ergodic and admits an equivalent sigma-finite invariant measure \(\eta\). For \(e=M_{1_B}\ne0\),

\[
 e\text{ is finite in }M
 \quad\Longleftrightarrow\quad
 \eta(B)<\infty.
 \tag{RFT.14}
\]


**Proof.** If \(\eta(B)<\infty\), then \(\tau_\eta(e)<\infty\). For \(v^*v=e\) and \(vv^*=f\leq e\), the trace identity and finite subtraction give
\(\tau_\eta(e-f)=0\). Faithfulness gives \(e=f\), proving finiteness.

Conversely, if \(e\) is finite in \(M\), its corner \(eMe\) is a finite factor. Finiteness is exactly the same partial-isometry test in the corner, and factoriality follows from Section 5 and the center formula for \(R_B\). Traces, Corollary 5.12, gives it a faithful normal tracial state. Applying EDT-05 to \(R_B\) produces an equivalent finite invariant measure \(\zeta\) on \(B\). The measure \(\eta|_B\) is also invariant and sigma-finite. Since \(R_B\) is ergodic, EDT-07 gives
\(\eta|_B=c\zeta\) for a positive finite scalar \(c\). Hence \(\eta(B)<\infty\). \(\square\)

For a type II relation factor, the base has no point atoms: one such atom would have a conull orbit by ergodicity, contradicting (RFT.6). Every countable orbit in \(B\) therefore has measure zero. Apply the table to \(R_B\):

\[
 eMe\text{ is }
 \begin{cases}
 II_1,&0<\eta(B)<\infty,\\
 II_\infty,&\eta(B)=\infty.
 \end{cases}
 \tag{RFT.15}
\]

This includes finite corners of a type \(II_\infty\) factor and all nonzero diagonal corners of a type \(II_1\) factor.

For a type I factor supported on \(O\), the corner is
\(B(\ell^2(O\cap B))\), by the matrix units of Section 3. Its rank is the number of surviving points. For a type III factor, every nonzero diagonal corner is type III: a nonzero finite projection in that corner would satisfy the same finiteness test in \(M\), since every partial isometry with initial and final projections below it already lies in the corner.

The number \(\mu(B)\) measures the original weight, whereas \(\eta(B)\) detects finiteness in (RFT.14). Confusing these numbers loses information even when \(\mu\) is a probability.

## 7. Atomic cores and a finite weight on an infinite factor

Return to a conull countable orbit \(O\), with masses \(p_i>0\). Let \(q_i>0\) be finite, so the equivalent diagonal weight has masses \(p_iq_i\). In the height lift, the quantity

\[
 w=p_x\lambda=p_y\lambda_y
 \tag{RFT.16}
\]

is constant on each lifted orbit. The onto unitary

\[
 (V\eta)_{yx}(w)=\eta(y,x;w/p_x)
 \tag{RFT.17}
\]

identifies the lifted Hilbert space with
\(L^2((0,\infty),dw;\operatorname{HS}(\ell^2(O)))\).
Indeed source counting gives \(\sum_{x,y}p_x\int|\eta(y,x;\lambda)|^2d\lambda\), and \(dw=p_xd\lambda\) converts it to the displayed norm. The inverse substitutes \(w=p_x\lambda\). Tonelli handles the countably infinite orbit.

Bounded lifted diagonal functions give all bounded diagonal matrix fields in \(w\). Singleton partial orbit maps give the constant matrix units. Finite-coordinate compression shows that these generate every bounded measurable operator field. Each generator already has this form, so, using 1. The lifted relation and the exact core theorem through 2. Why the Fourier, trace and product conventions matter,

\[
 \begin{gathered}
 N=B(\ell^2(O))\overline\otimes L^\infty((0,\infty),dw),\\
 \tau_{\rm core}(T)=\frac1{2\pi}\int_0^\infty
                       \operatorname{Tr}(T(w))\,dw,\\
 A_q(w)=\operatorname{diag}_{i\in O}(p_iq_i/w).
 \end{gathered} \tag{RFT.18}
\]

The trace is the full basepoint formula after the same substitution, with its canonical constant from RCS. Its positive values may be infinite.

For all \(z\in\mathbb C\), the exact domain is

\[
 D(A_q^z)=
 \left\{\eta:
 \sum_{x,y\in O}\int_0^\infty
       (p_yq_y/w)^{2\operatorname{Re}z}
       |\eta_{yx}(w)|^2\,dw<\infty\right\}.
 \tag{RFT.19}
\]

Here \(\eta\) is already in the Hilbert space. The formula follows from the maximal multiplication domain proved in RCS-05. A diagonal corner cuts both indices to \(O\cap B\), as in (RFT.10), and retains that full domain formula on the cutdown.

For a concrete distinction between finite weight and finite projection, take
\(O=\mathbb N_{\geq1}\), the complete relation, and \(p_i=2^{-i}\). Finite permutations give a countable presentation. Then

\[
 \varphi_\mu(1)=1,\qquad
 M=B(\ell^2(\mathbb N)),\qquad
 \tau_{\rm counting}(1)=\infty.
 \tag{RFT.20}
\]

The unilateral shift is an isometry with proper range projection, so \(1\) is infinite. A faithful normal state has not made this algebra finite.

For \(B_N=\{1,\ldots,N\}\), its corner is \(M_N(\mathbb C)\),
\(\eta(B_N)=N\), and \(\mu(B_N)=1-2^{-N}\). The normalized trace and normalized diagonal state have density ratio

\[
 \frac{\mu(B_N)}{\eta(B_N)p_i}
       =\frac{(1-2^{-N})\,2^i}{N}
 \qquad(1\leq i\leq N).
 \tag{RFT.21}
\]

Its imaginary powers are exactly the diagonal cocycle in (RFT.13).

## 8. Problems with complete solutions

**Problem 1.** Does an infinite equivalent invariant measure force type \(II_\infty\)?

**Solution.** No. Translation of \(\mathbb Z\) on itself preserves counting measure and has one orbit. Section 3 gives \(B(\ell^2(\mathbb Z))\), of type \(I_\infty\). The type \(II_\infty\) row excludes a conull orbit. Conversely, the five-cycle example in Section 4 has an infinite presenting group and a finite invariant measure, but gives type \(I_5\).

**Problem 2.** If \(R\) is ergodic and one orbit has positive measure, must that orbit be conull? Can an ergodic nonatomic relation have any such orbit?

**Solution.** The orbit is a countable Borel set, invariant under the action. Ergodicity makes a positive-measure orbit conull. A nonatomic measure gives each point mass zero, hence every countable orbit mass zero. Thus no such orbit exists in the nonatomic case.

**Problem 3.** For a type II relation factor with invariant \(\eta\), can a finite original weight \(\varphi_\mu(M_{1_B})\) certify that \(M_{1_B}\) is finite?

**Solution.** The criterion is \(\eta(B)<\infty\), by (RFT.14). An equivalent probability \(\mu\) can always be chosen even when \(\eta(X)=\infty\), using the finite-measure partition and positive summable densities of EDT-05. Then \(\varphi_\mu(1)=1\) while \(1\) is infinite in a type \(II_\infty\) factor. The correct finite corner state is (RFT.11), when its hypothesis on \(\eta(B)\) holds.

**Problem 4.** Check the two-point case of (RFT.21), including the scalar normalization.

**Solution.** The original masses on \(B_2\) are \(1/2,1/4\), with total \(3/4\). The normalized state has diagonal weights \(2/3,1/3\), and the normalized trace has weights \(1/2,1/2\). Their ratios are \(3/4,3/2\), agreeing with (RFT.21). Thus

\[
 [Dt_{B_2}:D\psi_{B_2}]_t
      =\operatorname{diag}((3/4)^{it},(3/2)^{it}).
 \tag{RFT.22}
\]

Relative to the unnormalized restricted weight the ratios would instead be \(1,2\). The factor \((3/4)^{it}\) is necessary when the reference state is normalized.

**Problem 5.** Does (RFT.1) assert that all measurable fields on the orbit fibres belong to \(M\)?

**Solution.** It also requires essential boundedness and constancy across base points on the same orbit. On the full relation of two points, the field \(T_x=xI\), after labeling the points \(1,2\), is measurable and bounded but has different values at the two base points. It acts on the source-coordinate multiplicity and fails the constancy requirement. It belongs to the source multiplication algebra in the commutant, and is not in the factor \(M_2(\mathbb C)\).

## References

Masamichi Takesaki, *Theory of Operator Algebras III*, Chapter XIII, Section 2, Corollary 2.8 and Theorem 2.10, pp. 21–23, provides the source statements. [Publisher record](https://doi.org/10.1007/978-3-662-10453-8). The complete earlier programme proofs are identified in Section 1; the existing correction to the finite-factor condition is credited in Section 4. The trace proof of atomicity, corner calculations and countable atomic core model above are independently written exposition. New text is released under CC0.

