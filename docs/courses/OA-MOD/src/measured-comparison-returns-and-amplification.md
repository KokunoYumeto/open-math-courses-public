# Measured comparison, returns and modular amplification

Orbit matching supplies matrix coordinates, but the matching maps need not preserve the original measure. Their Radon–Nikodym densities determine the amplified weight. A first-return map introduces a different distinction: its corner unitary generally differs from the compression of the original transformation unitary.

Let \(R\) be an ergodic orbitally countable standard Borel principal measured groupoid, with nonzero sigma-finite quasi-invariant unit measure \(\mu\) on \(X\). We identify it with its endpoint relation. 2. Countable presentations and null saturation proves the countable nonsingular Borel presentation and null-saturation criterion. Statements about sets and maps are modulo null sets; countably many exceptional sets and their saturations may be removed together.

## 1. Matching sets and comparing their projections

Write \(A\sim_R B\) when a Borel partial orbit bijection carries \(A\) onto \(B\), and \(A\precsim_R B\) when it carries \(A\) onto a subset of \(B\).

**Comparison and Schröder–Bernstein.** Any two measurable sets are comparable for \(\precsim_R\). If both \(A\precsim_R B\) and \(B\precsim_R A\), then \(A\sim_R B\).

Here is the complete argument of Matching sets and nonsingular dyadic arrays, Lemmas 1.1–1.2, abbreviated **MATCH**. Enumerate Borel partial bijections whose graphs cover \(R\). At each step match all still-unused points of \(A\) whose images under that map are still unused in \(B\). The countable union is a Borel partial bijection with disjoint domains and ranges. If both unmatched remainders had positive measure, ergodicity would make the saturation of either conull. Some presenting map would connect a positive part of one remainder to the other. Those points were available when that map was visited and would have been removed, a contradiction. Thus the matching exhausts at least one side.

For the second assertion take injections \(i:A\to B\) and \(j:B\to A\) along the relation. Set

\[
 D_0=A\setminus j(B),\qquad D_{n+1}=j(i(D_n)),
 \qquad D=\bigcup_{n\geq0}D_n.
 \tag{MRA.1}
\]

Use \(i\) on \(D\) and \(j^{-1}\) on \(A\setminus D\). The identity
\(j(i(D))=D\setminus D_0\) shows that their ranges are disjoint and cover \(B\). The resulting Borel bijection is nonsingular and stays inside \(R\). This proves both assertions, also for sigma-finite measures, since the construction depends only on null sets.

Let \(M=M(R,\mu)\), and put \(e_A=M_{1_A}\). A partial orbit bijection
\(\theta:A\to B\) gives

\[
 (V_\theta\xi)(y,x)=1_B(y)\xi(\theta^{-1}y,x)
 \quad\text{on }L^2(R,\nu_s).
 \tag{MRA.2}
\]

Inside each counted orbit this is a partial permutation of rows. Its norm is at most one, its adjoint is the reverse partial permutation, and

\[
 V_\theta^*V_\theta=e_A,\qquad V_\theta V_\theta^*=e_B.
 \tag{MRA.3}
\]

Its kernel has row and column sums at most one, so it belongs to the relation algebra by 1. Counting arrows and fixing the derivative through 2. The weight model at infinite mass. It carries the diagonal on \(A\) to that on \(B\). Thus measurable matching gives diagonal-normalizing partial isometries, not only abstract equivalence of projections.

## 2. The full type II and type III comparisons

The remaining assertions of Takesaki XIII.3.13 are:

1. For a type II relation and an equivalent sigma-finite invariant measure \(\eta\),

\[
 A\precsim_R B\quad\Longleftrightarrow\quad
 \eta(A)\leq\eta(B).
 \tag{MRA.4}
\]

Equal masses give equivalence, including two infinite masses.
2. For type III, every two positive sets are equivalent inside \(R\).

Both have full earlier proofs in MATCH, at the following precise scope.

A positive atom in an ergodic standard measured relation forces a conull countable orbit: use a countable separating family to locate a point carrying the atom, and then saturate it. Every point of that orbit has positive finite mass. This is MATCH Proposition 5.4 and 2. An expected diagonal in a type I factor is atomic through 4. The complete factor-type classification. Consequently the type II and III cases here are nonatomic; no nonatomic assumption has been silently added to the source.

For (MRA.4), invariance gives necessity. For finite equal masses, the greedy matching of Section 1 removes equal invariant masses at every step. The two unused finite masses remain equal, so the exhausted side forces both to be exhausted. Nonatomicity allows a set of any prescribed smaller finite mass to be cut from the target. One explicit cut embeds a finite-measure piece Borelly into \([0,1]\) and uses its continuous cumulative distribution; combine successive finite-measure pieces if necessary. Two infinite sets have countable partitions into pieces of mass one: accumulate a sigma-finite finite-measure cover in order, making the final fractional cut by this same procedure, and discard only a null remainder. Match corresponding unit pieces and take their disjoint union. This proves the infinite case too. These are the complete steps of MATCH Proposition 3.2.

For type III the substantial ingredient is MATCH Theorem 2.3: a positive set finite for orbit matching produces an equivalent sigma-finite invariant measure. Its proof is part of the programme, not a cited external theorem. Lemmas 2.1–2.2 first prove halving and finiteness of finite unions of matching-finite sets. Compatible dyadic partitions then define a dimension on subsets of such a finite set. Theorem 2.3 proves both finite additivity and faithfulness. Its decreasing-set argument, equations (2.4)–(2.5), proves countable additivity: a positive limiting dimension would allow the successive disjoint differences to be embedded into a target omitting a fixed positive cell, compressing a finite set. Finally equation (2.6) extends this invariant measure over countably many injective orbit charts and verifies invariance on every chart intersection. This provides a genuine sigma-finite measure.

Thus a type III positive set \(A\) admits a compression
\(\theta:A\to A\setminus C\) with \(C\) positive. The sets \(\theta^jC\) are disjoint. Partition \(X\), modulo null sets, into Borel pieces \(D_j\) with injective orbit maps \(\pi_j:D_j\to C\), using the first presenting graph that reaches \(C\). Then

\[
 x\in D_j\longmapsto\theta^j\pi_j(x)
 \tag{MRA.5}
\]

embeds \(X\) into \(A\), because the target pieces are disjoint. Inclusion gives the reverse embedding, and Section 1 gives \(A\sim_R X\). Applying this twice proves the type III assertion. This is MATCH Theorem 3.1. Its atomic exclusion is the one just verified.

For completeness, measurable comparison exactly detects Murray–von Neumann comparison of these diagonal projections:

\[
 A\precsim_R B\quad\Longleftrightarrow\quad
 e_A\precsim_M e_B.
 \tag{MRA.6}
\]

One direction is (MRA.3). In type I, RFT-02–03 identifies \(M\) with the full matrix algebra on its conull countable orbit; comparison of diagonal projections compares their finite or countable ranks, and a corresponding injection of points is an orbit map. In type II, 5. All traces of a measured relation and RFT-04 give the faithful normal semifinite trace
\(\tau(e_A)=\eta(A)\). A partial isometry into \(e_B\) implies
\(\eta(A)\leq\eta(B)\), by the trace identity and positivity; use (MRA.4). In type III, every two nonzero diagonal projections already have a matching by (MRA.5), and the zero cases are immediate.

Equation (MRA.6) asserts existence of a diagonal-normalizing implementer. It does not say that every partial isometry implementing the same comparison normalizes the diagonal. A nonpermutation unitary in \(M_2\), for instance, need not preserve the diagonal.

## 3. Splitting into countably many equivalent sheets

Assume there is a countable partition

\[
 X=\bigsqcup_{n\geq0}E_n,\qquad E_n\sim_R E_0.
 \tag{MRA.7}
\]

All sheets are positive, since otherwise nonsingularity and equivalence would make the whole countable union null. Put \(E=E_0\), and choose Borel partial orbit bijections \(v_n:E\to E_n\), with \(v_0=\mathrm{id}\). Define

\[
 W:E\times\mathbb N\longrightarrow X,\qquad W(x,n)=v_nx.
 \tag{MRA.8}
\]

This is a Borel bijection, with Borel inverse on the countable partition. Moreover,

\[
 v_nx\ R\ v_my\quad\Longleftrightarrow\quad x\ R|_E\ y.
 \tag{MRA.9}
\]

Both implications follow by composing the two chosen transport arrows with an arrow between the displayed points. Thus \(W\) identifies \(R\) with
\((R|_E)\times(\mathbb N\times\mathbb N)\).

Give \(E\times\mathbb N\) the reference measure
\(\lambda_0=\mu|_E\times\#\). The measure pulled back from \(X\) is equivalent to it. More precisely, define

\[
 \mu_n(A)=\mu(v_n A),\qquad
 h_n=\frac{d\mu_n}{d(\mu|_E)},\qquad h_0=1.
 \tag{MRA.10}
\]

Each \(\mu_n\) is sigma-finite, by transporting a finite-measure exhaustion of \(E_n\), and is equivalent to \(\mu|_E\). Hence every \(h_n\) is positive and finite almost everywhere. We have

\[
 d(W^*\mu)(x,n)=h_n(x)\,d\lambda_0(x,n).
 \tag{MRA.11}
\]

There is no assertion that these densities are one.

This proves the full product splitting of Takesaki XIII.3.14(i); the earlier proof is MATCH Proposition 3.3. The countably infinite pair relation is the source's type \(I_\infty\) groupoid, whether its points are labelled by \(\mathbb N\) or \(\mathbb Z\).

Write \(\delta_E\) for the modulus of \(R|_E\), in the range-over-source convention. The partial-map derivative theorem RWT-01 gives
\(h_n(x)=\delta(v_nx,x)\). After a common conull restriction the cocycle identity therefore yields

\[
 \delta(v_nx,v_my)=
       \frac{h_n(x)}{h_m(y)}\,\delta_E(x,y).
 \tag{MRA.12}
\]

The density in (MRA.10) measures the image of a set. It is not the inverse-pushforward density at its image, which has the reciprocal value.

A countably infinite partition (MRA.7) cannot exist in the finite invariant-measure case: every sheet would have the same positive invariant mass, contradicting finite total mass. This is a consequence of the hypothesis, not an extra restriction on the splitting theorem.

## 4. The algebra and the amplified weight

Let \(N=e_EMe_E\), identified with \(M(R|_E,\mu|_E)\) by 3. A full reduction is a full modular corner. Put \(V_n=V_{v_n}\). Disjointness of the sheets gives

\[
 V_n^*V_m=1_{\{n=m\}}e_E,\qquad
 \sum_{n\geq0}V_nV_n^*=1
 \quad\text{strongly}.
 \tag{MRA.13}
\]

There is a normal isomorphism

\[
 \Pi:N\bar\otimes B(\ell^2\mathbb N)\longrightarrow M,
 \qquad \Pi(a\otimes E_{nm})=V_naV_m^*.
 \tag{MRA.14}
\]


Here is its concrete representation proof, including the measure factors. Set
\(H_E=L^2(R|_E,\nu_s^E)\). A vector in \(H_\mu\) has the unitary coordinates

\[
 (U\xi)_{nm}(x,y)=
     h_m(y)^{1/2}\xi(v_nx,v_my)
 \tag{MRA.15}
\]

in \(H_E\otimes\mathrm{HS}(\ell^2\mathbb N)\). Indeed its squared norm is obtained by integrating in the source sheet \(v_my\) and counting the range points \(v_nx\); (MRA.11) gives exactly the factor \(h_m(y)\). Division by its square root gives the inverse unitary.

In these coordinates \(V_naV_m^*\) acts by \(a\) on the base range coordinate and by \(E_{nm}\) on the matrix row coordinate. The source multiplier in (MRA.15) commutes with this action. These operators therefore generate the spatial tensor product on the left of (MRA.14), faithfully and normally. Conversely, with \(p_k=\sum_{n<k}V_nV_n^*\), every block of \(p_kTp_k\), \(T\in M\), equals
\(V_n(V_n^*TV_m)V_m^*\), where \(V_n^*TV_m\in N\). Since \(p_kTp_k\to T\) strongly, these blocks generate all of \(M\). This proves surjectivity and (MRA.14).

Let \(\varphi_E\) be the diagonal weight on \(N\). The reference weight on the tensor product is

\[
 \Phi(A)=\sum_{n\geq0}\varphi_E(A_{nn}),\qquad A\geq0;
 \tag{MRA.16}
\]

it is \(\varphi_E\otimes\operatorname{Tr}\). The original weight, transported by \(\Pi\), is instead

\[
 \Psi_h(A)=\sum_{n\geq0}\int_E
                 h_n(x)E_N(A_{nn})(x)\,d\mu(x).
 \tag{MRA.17}
\]

On the sheet \(E_n\), the diagonal expectation of \(\Pi(A)\) at \(v_nx\) equals \(E_N(A_{nn})(x)\). Change variables by (MRA.10) and sum the nonnegative integrals over the disjoint sheets. This proves (MRA.17), including infinite values, for every positive \(A\).

Both are faithful normal semifinite weights by the sigma-finite relation-weight theorem RWT-02, applied respectively to \(\lambda_0\) and \(W^*\mu\). The positive affiliated diagonal

\[
 H=\operatorname{diag}(M_{h_n})
\]

records the density of (MRA.17). Its bounded spectral functions lie in the diagonal centralizer of \(\Phi\). The exact normalized cocycle is

\[
 [D\Psi_h:D\Phi]_t=
       \operatorname{diag}(M_{h_n^{it}}).
 \tag{MRA.18}
\]

This is RWT-05–06 on the product relation with density \(h(x,n)=h_n(x)\). It fixes the weight normalization as well as the modular conjugacy. Strong* continuity follows by dominated convergence in the Hilbert space (MRA.15), since each scalar entry and its conjugate have modulus one.


## 5. Relative operators and normalized finite corners

In the common space \(H_E\otimes\mathrm{HS}(\ell^2\mathbb N)\), also allow a positive finite measurable density \(k_n(x)\) on every sheet. Let \(\Psi_k\) be its weight, defined as in (MRA.17). Both densities give sigma-finite equivalent unit measures: intersect a finite-measure exhaustion of \(E\) with a finite set of sheet labels and bounded-density sets.

The reference modular conjugation is

\[
 (J_0\xi)_{nm}(x,y)=
       \delta_E(x,y)^{1/2}\overline{\xi_{mn}(y,x)}.
 \tag{MRA.19}
\]

The relative positive multiplier is

\[
 \kappa_{k,h}(x,n;y,m)
       =\frac{k_n(x)}{h_m(y)}\,\delta_E(x,y).
 \tag{MRA.20}
\]

Apply the full graph and canonical-standard-form proofs of 4. The mixed graph and its full domain through 5. Canonical standard forms and relative operators to this product relation. They give

\[
 \begin{split}
 (A_{k,h}\xi)_{nm}(x,y)
   &=\left(\frac{k_m(y)}{h_n(x)}\right)^{1/2}
                       \overline{\xi_{mn}(y,x)},\\
 \Delta_{\Psi_k,\Psi_h}&=m_{\kappa_{k,h}},\qquad
 A_{k,h}=J_0m_{\kappa_{k,h}}^{1/2}.
 \end{split} \tag{MRA.21}
\]

The absence of an extra \(\delta_E^{1/2}\) in the first line is deliberate: the two cocycle factors cancel when \(J_0\) flips the coefficient of the square root. Changing variables under that flip gives the domain condition

\[
 D(A_{k,h})=
 \left\{\xi:
 \sum_{n,m}\int_{R|_E}\kappa_{k,h}
                   |\xi_{nm}|^2\,d\nu_s^E<\infty\right\}.
 \tag{MRA.22}
\]

All displayed domains are subsets of the underlying Hilbert space. For every \(z\in\mathbb C\), the exact complex-power domain is

\[
 D(\Delta_{\Psi_k,\Psi_h}^{\,z})=
 \left\{\xi:
 \sum_{n,m}\int_{R|_E}\kappa_{k,h}^{\,2\operatorname{Re}z}
                   |\xi_{nm}|^2\,d\nu_s^E<\infty\right\},
 \tag{MRA.23}
\]

and the power multiplies each entry by \(\kappa_{k,h}^z\). The graph-core proof RWT-04 uses finite-measure restrictions and bounds on both densities and their reciprocals; a finite restriction of the two sheet indices adds the tensor cutoff here. Monotone exhaustion and dominated convergence in the weighted graph norm give exactly (MRA.22)–(MRA.23), with no boundedness assumption on all sheets at once.

In particular, the individual modular multiplier of \(\Psi_h\) is

\[
 \kappa_{h,h}=\frac{h_n(x)}{h_m(y)}\delta_E(x,y),
 \tag{MRA.24}
\]

whereas the relative multiplier of \(\Psi_h\) against \(\Phi\) is
\(h_n(x)\delta_E(x,y)\). Confusing these two loses the source density.

The exact cocycle is

\[
 [D\Psi_k:D\Psi_h]_t=
        \operatorname{diag}(M_{(k_n/h_n)^{it}}),
 \tag{MRA.25}
\]

by RWT-06. For a finite label set \(F\), let
\(p_F=1\otimes\sum_{n\in F}E_{nn}\). This diagonal projection is in both centralizers. Its corner standard form keeps **both** indices \(n,m\) in \(F\), with the coefficients and maximal domains above unchanged, by RWT-07.

If the two masses

\[
 m_h=\sum_{n\in F}\int_E h_n\,d\mu,\qquad
 m_k=\sum_{n\in F}\int_E k_n\,d\mu
\]

are positive and finite, normalize the restricted weights by these masses. Their cocycle is

\[
 [D(\Psi_k|_{p_F}/m_k):D(\Psi_h|_{p_F}/m_h)]_t
   =(m_h/m_k)^{it}
       \sum_{n\in F}M_{(k_n/h_n)^{it}}\otimes E_{nn}.
 \tag{MRA.26}
\]

Indeed the ratio of the two normalized densities is
\((m_h/m_k)k_n/h_n\). This proves the scalar phase and also explains why an algebraic amplification alone cannot determine the normalized weights.

## 6. Recurrence and the induced transformation

Suppose now that \(R=R_T\) for an invertible ergodic nonsingular Borel transformation \(T\), and that the measure is not concentrated on one orbit. Let \(E\subset X\) have positive measure. The atomic argument in Section 2 makes this properly ergodic case nonatomic.

The complete recurrence proof is Towers and odometer orbits, Lemma 1.1. The following version makes both time directions and the original sigma-finite measure explicit.

The set of last visits,

\[
 L=E\setminus\bigcup_{j\geq1}T^{-j}E,
 \tag{MRA.27}
\]

is wandering: two distinct iterates of \(L\) cannot intersect, because a point of \(L\) would then have a later visit to \(E\). If \(L\) were positive, nonatomicity would split it into two positive Borel parts. Their two-sided saturations would be disjoint invariant positive sets, contradicting ergodicity. Thus \(L\) is null.

A point of \(E\) with only finitely many forward visits has a last visit in \(L\), and belongs to a countable union of inverse images of \(L\). Hence almost every point of \(E\) has infinitely many forward visits. Apply the same proof to \(T^{-1}\) for backward visits. Delete the exceptional sets and their two-sided saturations. On the remaining invariant conull space every retained orbit meeting \(E\) has visits to \(E\) in both time directions without bound. The saturation of \(E\) is conull by ergodicity.

Define the positive first-return time and transformation by

\[
 r_E(x)=\min\{j\geq1:T^jx\in E\},\qquad
 T_Ex=T^{r_E(x)}x.
 \tag{MRA.28}
\]

For each \(j\), its level set is
\(E\cap T^{-j}E\cap\bigcap_{1\leq l<j}T^{-l}(X\setminus E)\), so it is Borel. The map is nonsingular on each level, being a restriction of \(T^j\). Its inverse takes the preceding visit, and is Borel and nonsingular by the corresponding backward partition. Thus \(T_E\) is an invertible nonsingular transformation of the reduced space.

Its iterates enumerate all visits of an original orbit to \(E\). More explicitly, between \(x\) and \(T^j x\in E\), \(j>0\), there are only finitely many integer times; successively taking the next visit reaches that point. Negative times use the inverse map. Therefore

\[
 R_{T_E}=R_T|_E.
 \tag{MRA.29}
\]

The reduced relation is ergodic: saturating a positive reduced-invariant subset gives a conull invariant subset of \(X\), whose intersection with \(E\) is the original reduced-invariant set. This proves the full nontrivial assertion of Takesaki XIII.3.14(ii), also proved in MATCH Proposition 3.4. A null \(E\) gives the zero measured corner; no return map is required outside its empty conull representative.

The nontransitivity hypothesis matters. Translation on a single countable orbit with counting measure is ergodic and nonsingular, but a singleton has no positive return. Section 8 separates finite coordinate checks from this recurrence assertion.

## 7. Return unitaries and analytic cutoffs

Let \(e=e_E\), and write \(E_j=\{x\in E:r_E(x)=j\}\) within this section. The first-return unitary in the corner is

\[
 V_{T_E}=\sum_{j\geq1}V_T^jM_{1_{E_j}}.
 \tag{MRA.30}
\]

The source domains \(E_j\) partition \(E\), and the ranges \(T^jE_j=T_EE_j\) also partition \(E\), because \(T_E\) is bijective. Thus the summands have orthogonal initial and final projections. Their partial sums converge strongly, as do their adjoints, to a unitary with identity \(e\). On relation vectors the sum changes a range coordinate \(x\in E_j\) to \(T^jx\); it is exactly the operator of \(T_E\).

By contrast,

\[
 eV_Te=V_TM_{1_{E_1}}.
 \tag{MRA.31}
\]

This compression retains only the one-step returns. It equals the return unitary only when almost every return has time one.

Put \(d_T(x)=\delta(Tx,x)\), so that
\(\mu(TA)=\int_A d_T\,d\mu\). The simultaneous cocycle identity in RWT-01 proves

\[
 d_E(x):=\delta(T_Ex,x)
      =\prod_{l=0}^{r_E(x)-1}d_T(T^lx).
 \tag{MRA.32}
\]

This is a finite positive product for almost every \(x\in E\). It also is the image-measure derivative for \(T_E\), by partitioning \(E\) into the return-time levels and applying change of variables there.

Let \(\varphi_E\) retain the original restricted measure, even if it is infinite. The corner modular formula RWT-02/07 is

\[
 \sigma_t^{\varphi_E}(V_{T_E})
       =V_{T_E}M_{d_E^{it}}
       =M_{(d_E\circ T_E^{-1})^{it}}V_{T_E}.
 \tag{MRA.33}
\]

The positive imaginary power uses the image-measure convention of (MRA.32). If instead one uses the pushforward derivative at the range point, that derivative is
\((d_E\circ T_E^{-1})^{-1}\), and its imaginary power in (MRA.33) has the negative sign.

Return times can be unbounded. Entire elements are obtained directly by

\[
 D_k=\{x\in E:k^{-1}\leq d_E(x)\leq k\},\qquad
 a_k=V_{T_E}M_{1_{D_k}}.
 \tag{MRA.34}
\]

Since \(\log d_E\) is bounded on \(D_k\),

\[
 \sigma_z^{\varphi_E}(a_k)=
       V_{T_E}M_{1_{D_k}\exp(iz\log d_E)},\qquad
 \|\sigma_z^{\varphi_E}(a_k)\|
       \leq k^{|\operatorname{Im}z|}.
 \tag{MRA.35}
\]

The bounded logarithm's exponential series and derivative series converge in norm on bounded complex sets, proving the entire extension. The increasing projections \(M_{1_{D_k}}\) tend strongly to \(e\). Formula (MRA.34) and its adjoint therefore converge strongly to \(V_{T_E}\) and its adjoint.

This proof applies to any partial orbit map \(\theta\), using its derivative \(\delta(\theta x,x)\) on its domain. Cut off the countably many presenting orbit maps in this way. Along with the bounded diagonal multipliers, their products and adjoints form a unital algebra of entire elements whose von Neumann closure is \(M\). Products are entire by continuity of operator multiplication; the adjoint extension is \(z\mapsto\sigma_{\bar z}(a)^*\). Strong convergence of the cutoff maps supplies every presenting generator. This construction keeps the original weight and requires no global derivative bound.

## 8. Examples and complete solutions

**Problem 1: an implementer need not normalize.** In \(M_2(\mathbb C)\), test the diagonal under

\[
 u=2^{-1/2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
\]


**Solution.** The matrix is unitary, so it implements equivalence of \(1\) with itself. But

\[
 uE_{00}u^*=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix}
\]

is not diagonal. Equation (MRA.6) gives existence of a normalizing implementer for diagonal projections; it does not characterize every implementer.

**Problem 2: a finite check of the return formula.** Give \(a,b,c\) masses \(1/2,1/3,1/6\), take the cycle \(Ta=b,Tb=c,Tc=a\), and restrict to \(E=\{a,c\}\).

**Solution.** The return time is two at \(a\) and one at \(c\), so

\[
 V_{T_E}=E_{ca}+E_{ac},\qquad eV_Te=E_{ac}.
\]

Here \(E_{yx}\) sends the basis vector at \(x\) to that at \(y\). The two-step derivative at \(a\) is
\((\mu(b)/\mu(a))(\mu(c)/\mu(b))=(2/3)(1/2)=1/3\); at \(c\) it is \(3\). Consequently

\[
 \sigma_t^{\varphi_E}(V_{T_E})
     =(1/3)^{it}E_{ca}+3^{it}E_{ac}.
 \tag{MRA.36}
\]

Normalizing the corner measure gives masses \(3/4,1/4\) and the same modular group. This is a direct finite computation; the space is transitive and does not fall under the properly ergodic recurrence theorem.

**Problem 3: a state on an infinite amplification.** On \(\mathbb N=\{0,1,\ldots\}\), take the complete relation and point masses \(2^{-n-1}\). Use the singleton \(E=\{0\}\) as the reference sheet.

**Solution.** We have \(N=\mathbb C\), \(\varphi_E(1)=1/2\), and \(h_n=2^{-n}\). Thus

\[
 M=B(\ell^2\mathbb N),\qquad
 \Phi=\tfrac12\operatorname{Tr},\qquad
 \Psi_h(A)=\sum_{n\geq0}2^{-n-1}A_{nn}.
 \tag{MRA.37}
\]

The last weight is a state although the algebra is type \(I_\infty\). On the \(nm\)-matrix coordinate the individual modular multiplier is \(2^{m-n}\), while the relative multiplier against \(\Phi\) is \(2^{-n}\).

The vector with
\(\xi_{0m}=2^{-m/2}/\sqrt{m+1}\), all other entries zero, is square integrable. Its square-root modular norm for \(\Psi_h\) is proportional to
\(\sum_{m\geq0}(m+1)^{-1}\), which diverges. The Hilbert norm is proportional to the convergent sum
\(\sum 2^{-m}/(m+1)\). This verifies that (MRA.22) can be a proper domain even though all imaginary powers are bounded.

For \(F=\{0,\ldots,q-1\}\), the masses are \(q/2\) and \(1-2^{-q}\). The cocycle of the normalized \(\Psi_h\)-corner against the normalized \(\Phi\)-corner is

\[
 \left(\frac{q}{2(1-2^{-q})}\right)^{it}
     \sum_{n<q}2^{-nit}E_{nn}.
 \tag{MRA.38}
\]

Every factor is fixed by the actual normalization of these two states.

**Problem 4: the comparison measure must be invariant.** Let \(\mathbb Q\) act on \(\mathbb R\) by translations. Can equal masses for an equivalent probability replace equal invariant masses in (MRA.4)?

**Solution.** No. 7. Two tests of the topology–measure distinction gives the complete ergodicity and type \(II_\infty\) proof with Lebesgue invariant measure. Set \(A=[0,1)\), \(B=[1,3)\). Start with the positive integrable density
\(r_0(x)=2^{-|j|}/3\) on \([j,j+1)\), \(j\in\mathbb Z\). Replace it by \(1\) on \(A\) and by \(1/2\) on \(B\), retaining \(r_0\) elsewhere, and normalize.

The original masses on \(A\) and \(B\) sum to \(1/3+1/6+1/12=7/12\). The unchanged complement has mass \(5/12\); the new unnormalized total is \(2+5/12=29/12\). Hence the normalized equivalent probability gives both \(A\) and \(B\) mass \(12/29\). Their invariant Lebesgue masses are instead \(1\) and \(2\). Thus \(A\precsim_R B\), but \(B\not\precsim_R A\), and the two sets are not equivalent. The source's comparison criterion uses an invariant measure, not an arbitrary probability in its class.

## References

Masamichi Takesaki, *Theory of Operator Algebras III*, Chapter XIII, Proposition 3.13 and Lemma 3.14, printed pp. 37–38. [Publisher record](https://doi.org/10.1007/978-3-662-10453-8). The complete matching, invariant-measure, splitting and recurrence programme proofs are identified above. The modular amplification, maximal-domain, return-unitary and normalization calculations here are independently written course exposition. New text is released under CC0.


