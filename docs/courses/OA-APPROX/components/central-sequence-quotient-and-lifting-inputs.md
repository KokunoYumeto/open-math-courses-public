# Quotient norms, trace completions and exact coordinate relations

*Original programme exposition: CC0-1.0 to the extent of rights held.*

An exact relation in a quotient is an approximation statement for its coordinate representatives. The construction of the quotient must first justify its norm, positivity and Hilbert representation. The [central-sequence lesson](../src/central-sequence-algebras-and-exact-lifts.md) uses those constructions before repairing projections and matrix units.

We use the complete CF1–10 calculus and Hilbert arguments, concrete preduals CP1–6, and bounded density BD1–5. These are exact earlier programme proofs. Inner products are linear in the second variable.

<a id="cq1-complete-cstar-quotient"></a>

## CQ1. The complete C* quotient construction

Let \(A\) be a unital C* algebra and \(I\subset A\) a norm-closed two-sided star ideal. Define
\[
\|x+I\|_q=\inf_{i\in I}\|x-i\|.
\]
This is a norm on the vector quotient: zero distance is membership in \(I\) because \(I\) is closed; homogeneity and the triangle inequality follow from their counterparts in \(A\). Products and adjoints are well defined because \(I\) is two-sided and star closed. Taking representatives arbitrarily close to their infimal norms proves submultiplicativity, and taking adjoints in the infimum proves that the involution is isometric.

The quotient is complete. From a Cauchy sequence of classes, choose a subsequence \(X_r\) with consecutive distances less than \(2^{-r}\). Lift the first class arbitrarily. At step \(r\), choose a representative \(d_r\) of \(X_{r+1}-X_r\) with norm less than \(2^{1-r}\). The representatives
\[
a_{r+1}=a_r+d_r
\]
are norm Cauchy in \(A\). Their norm limit represents the quotient limit of the subsequence. The original Cauchy sequence converges to it by the triangle inequality.

We prove the C* norm identity rather than presuming it for this quotient. For a finite set \(F\subset I\) and \(t>0\), put
\[
b_F=\sum_{i\in F}(i^*i+ii^*),\qquad
e_{F,t}=b_F(b_F+t1)^{-1}.
\tag{CQ1.1}
\]
The inverse exists by the complete continuous positive calculus. The element \(e_{F,t}\) belongs to \(I\), is positive, and has norm at most one. When \(F\) is empty it is zero. For \(i\in F\), positive order and that calculus give
\[
\begin{aligned}
\|i(1-e_{F,t})\|^2
&\leq\|(1-e_{F,t})b_F(1-e_{F,t})\|\\
&=\left\|\frac{t^2b_F}{(b_F+t1)^2}\right\|
\leq\frac t4.
\end{aligned}
\tag{CQ1.2}
\]
The same bound for \((1-e_{F,t})i\) uses \(ii^*\) in place of \(i^*i\). The scalar estimate is
\(t^2s/(s+t)^2\leq t/4\), \(s\geq0\), obtained from \((s-t)^2\geq0\).
Order the indices by enlarging \(F\) and decreasing \(t\). For every fixed \(i\in I\), eventually \(F\) contains \(i\), so both errors tend to zero. This is a complete two-sided approximate identity for \(I\), including \(I=0\).

For fixed \(x\in A\), it follows that
\[
\|x(1-e_{F,t})\|\longrightarrow\|x+I\|_q.
\tag{CQ1.3}
\]
The lower bound holds at each index because \(xe_{F,t}\in I\). For the upper bound, any \(i\in I\) gives
\[
\|x(1-e_{F,t})\|
\leq\|x-i\|+\|i(1-e_{F,t})\|.
\]
Take its limiting upper bound, then the infimum over \(i\).

The difference \(x^*x-(x-i)^*(x-i)\) belongs to \(I\), so
\[
\|x^*x+I\|_q\leq\|x+I\|_q^2.
\]
Conversely, for any \(j\in I\),
\[
\begin{aligned}
\|x(1-e_{F,t})\|^2
&=\|(1-e_{F,t})x^*x(1-e_{F,t})\|\\
&\leq\|x^*x-j\|+\|(1-e_{F,t})j(1-e_{F,t})\|.
\end{aligned}
\]
Use (CQ1.2) for \(j\), and (CQ1.3) for \(x\), to pass to the limit. Infimizing over \(j\) proves the reverse bound. Hence
\[
\|x^*x+I\|_q=\|x+I\|_q^2.
\tag{CQ1.4}
\]
Thus \(A/I\) is a C* algebra, with its inherited products and adjoints. Its quotient map is contractive. If \(I=A\), this is the zero algebra; otherwise its unit is \(1+I\) and has norm one, by the C* norm identity. CF's complete continuous calculus now applies in the quotient itself.

<a id="cq2-faithful-trace-hilbert-representation"></a>

## CQ2. A faithful trace gives an isometric Hilbert representation

Let \(A\) be a nonzero unital C* algebra with a faithful tracial state \(\tau\). The form
\[
\langle x,y\rangle=\tau(x^*y)
\]
is an inner product: positivity and scalar Schwarz follow from the positive-functional proof in CF, and faithfulness makes its null space zero. Complete this space to \(H_\tau\), with \(\Omega=1\).

Left multiplication \(L_a x=ax\) and right multiplication \(R_a x=xa\) are bounded. Positivity gives
\[
\|ax\|_2\leq\|a\|\|x\|_2,
\]
and traciality gives the right bound
\[
\|xa\|_2^2=\tau(a^*x^*xa)=\tau(x^*xaa^*)\leq\|a\|^2\|x\|_2^2.
\]
They extend to the Hilbert completion. Pairing local vectors gives
\(L_a^*=L_{a^*}\), \(R_a^*=R_{a^*}\).
The left action is a unital star representation; the right action is an action of the opposite multiplication. They commute on the dense local vectors and hence everywhere.

The left representation is isometric. We already proved \(\|L_a\|\leq\|a\|\). If \(a\ne0\), let \(h=a^*a\), whose spectral maximum is \(\lambda=\|a\|^2>0\) by CF. For \(0<\varepsilon<\lambda\), choose a continuous function \(f\), nonzero at \(\lambda\), with support in \([\lambda-\varepsilon,\lambda]\) on that spectrum. The calculus makes \(f(h)\ne0\), so faithfulness gives \(\|f(h)\|_2>0\). Moreover
\[
\|L_a f(h)\|_2^2
=\tau(f(h)^*h f(h))
\geq(\lambda-\varepsilon)\|f(h)\|_2^2.
\]
Thus \(\|L_a\|^2\geq\lambda-\varepsilon\). Letting \(\varepsilon\) decrease to zero proves the lower bound. The zero case is immediate. The image \(B=L(A)\) is consequently a norm-closed unital C* algebra.

Put \(N=B''\). The vector state
\[
\widetilde\tau(T)=\langle\Omega,T\Omega\rangle,\qquad T\in N,
\tag{CQ2.1}
\]
is normal by the complete CP single-vector test. It is faithful. If \(T\Omega=0\), then
\(T R_a\Omega=R_aT\Omega=0\)
for every \(a\in A\), because the right multipliers commute with \(N\). These vectors are dense, so \(T=0\).

It is also tracial on \(N\), not merely on the local algebra \(B\). BD1–5 supplies bounded strong approximation by \(B\), and CP's vector-series bound makes it ultraweak approximation. Hence \(B\) is ultraweakly dense in \(N\). For a fixed \(b\in B\), the two normal functionals
\(T\mapsto\widetilde\tau(Tb)\) and \(T\mapsto\widetilde\tau(bT)\)
agree on \(B\), and thus on \(N\). Next fix arbitrary \(T\in N\). The two corresponding normal functionals of a second variable agree on \(B\), by the first step, and therefore on \(N\). This proves the trace law for all pairs in \(N\). A vector state has value one at the unit, and its restriction is \(\tau\).

In particular \(N\) is finite: if \(V^*V=1\), the trace law gives
\(\widetilde\tau(1-VV^*)=0\);
faithfulness forces \(VV^*=1\). No separability of \(H_\tau\), a normality assertion about an abstract state before representation, or a classification of finite factors was assumed.

<a id="cq3-complete-trace-ball-and-normal-maps"></a>

## CQ3. A complete trace-metric unit ball is already von Neumann

Assume, in addition to CQ2, that the operator-norm unit ball of \(A\) is complete for the metric
\[
d_2(a,b)=\tau((a-b)^*(a-b))^{1/2}.
\]
Then the isometric image \(B=L(A)\) equals its bicommutant \(N\).

Indeed let \(T\) be any contraction in \(N\). BD gives a net of contractions \(L_{a_i}\) converging strongly to \(T\). Their values on \(\Omega\) are Cauchy, so the net \(a_i\) is \(d_2\)-Cauchy in that unit ball. Sequential metric completeness suffices for the net as well. To see this explicitly, choose increasing indices \(i_m\) beyond a Cauchy threshold for distance \(2^{-m}\); directedness permits each to dominate the previous choices. The selected sequence has a limit \(a\) in the complete ball. Any sufficiently late net element is close to a sufficiently late selected element and hence to \(a\), by the triangle inequality. No countable cofinal subset of the directed set is presumed.

For every local vector \(b\Omega\), the right multiplier bound gives
\[
\|(L_{a_i}-L_a)b\Omega\|
=\|(a_i-a)b\|_2
\leq\|b\|\,d_2(a_i,a)\longrightarrow0.
\tag{CQ3.1}
\]
The common norm bound extends this to the whole Hilbert space. Uniqueness of the strong limit gives \(T=L_a\). Thus every contraction of \(N\) belongs to \(B\); scaling proves \(N=B\). CQ2 supplies its faithful normal normalized trace, and finiteness.

There is a useful whole-domain normality statement. If \(\alpha\) is a trace-preserving star automorphism of \(A\), the rule
\[
U_\alpha(a\Omega)=\alpha(a)\Omega
\]
preserves inner products by the trace law. Its inverse is the analogous rule for \(\alpha^{-1}\), so it extends to a unitary of \(H_\tau\). On the dense local vectors,
\[
U_\alpha L_aU_\alpha^*=L_{\alpha(a)}.
\]
Consequently the automorphism of the represented von Neumann algebra is conjugation by this unitary. It is normal on its entire ultraweak domain: pulling back any CP square-summable vector-pair series replaces both vector sequences by their \(U_\alpha^*\)-images and preserves their sums of squared norms. The same argument treats the inverse. This proves normality without extrapolating bounded strong continuity to arbitrary ultraweak nets.

<a id="cq4-finite-subpiece-cancellation"></a>

## CQ4. Cancel a finite subpiece even when the endpoints are infinite

Suppose \(e\sim f\) are projections of a von Neumann algebra, \(p\leq e\) is finite, \(q\leq f\), and \(w^*w=p,\ ww^*=q\). Then
\[
e-p\sim f-q.
\tag{CQ4.1}
\]
The endpoints \(e,f\) themselves need not be finite.

Choose \(v^*v=e,\ vv^*=f\), and transport \(q\) into \(eMe\):
\[
q'=v^*qv,\qquad (v^*w)^*(v^*w)=p,\qquad
(v^*w)(v^*w)^*=q'.
\]
Both \(p,q'\) are finite by [PC5](central-finite-trace-inputs.md#oa-flow.projection.pc5). Their join \(j=p\vee q'\) is finite by the complete [PC6 finite-join proof](central-finite-trace-inputs.md#oa-flow.projection.pc6). Apply [FCT2's unitary completion](central-finite-trace-inputs.md#oa-flow.fct.2) inside the finite corner \(jMj\), extending the prescribed partial isometry \(v^*w\) to a unitary \(u_j\). Its orthogonal extension
\[
u=u_j+(e-j)
\]
is unitary in \(eMe\) and satisfies \(upu^*=q'\). Thus \(vu(e-p)\) has initial projection \(e-p\) and final projection \(f-q\), proving (CQ4.1). When \(p=q=0\), use \(u=e\). This route never cancels an infinite subpiece.

<a id="cq5-small-infinite-pieces"></a>

## CQ5. Infinite pieces small for several normal states

Let \(M\) be a factor with a faithful normal state. Every nonzero infinite projection \(p\) is properly infinite, and any two such projections are equivalent. Here is the full route from the earlier projection proofs. [PC4](central-finite-trace-inputs.md#oa-flow.projection.pc4) identifies \(Z(pMp)\) with \(Z(M)p=\mathbb Cp\). Its central finite/properly-infinite split in [PC5](central-finite-trace-inputs.md#oa-flow.projection.pc5) therefore has only the two scalar possibilities; an infinite \(p\) cannot have the finite one. A faithful normal state assigns strictly positive mass to each nonzero member of any orthogonal family. Since their finite sums have mass at most one, only finitely many have mass at least \(1/k\), for each \(k\). Every such family is countable. [PC7](central-finite-trace-inputs.md#oa-flow.projection.pc7) consequently gives mutual subequivalence between two properly infinite projections with central support \(1\); [PC3](central-finite-trace-inputs.md#oa-flow.projection.pc3) turns this into equivalence.

More precisely, let \(\psi_1,\ldots,\psi_s\) be positive normal functionals, and let \(\varepsilon>0\). PC5 constructs a filling orthogonal family
\[
p=\sum_{k\geq0}p_k,\qquad p_k\sim p.
\tag{CQ5.1}
\]
Normality gives
\(\sum_k\sum_{a=1}^s\psi_a(p_k)=\sum_a\psi_a(p)<\infty\).
For any specified finite integer \(h\geq1\), select \(h\) distinct sufficiently late members with total mass less than \(\varepsilon\), leaving at least one member unselected. All selected members are infinite, and their complementary remainder in \(p\) is infinite because it contains an unselected infinite member. This proves the asserted small-piece construction for one or finitely many pieces.

For the partial-isometry repair use \(\psi_1=\varphi\) and
\(\psi_2(a)=\varphi(waw^*)\), where \(w^*w=p\). The second functional is positive and normal by [NT1's fixed-multiplier predual proof](central-sequence-foundations.md#nt1-normal-functional-decomposition). Selecting a single \(r\leq p\) gives
\[
p-r\text{ infinite},\qquad
\varphi(r)+\varphi(wrw^*)<\varepsilon.
\tag{CQ5.2}
\]
The operator \(wr\) has the exact two square seminorms
\[
\varphi((wr)^*(wr))=\varphi(r),\qquad
\varphi((wr)(wr)^*)=\varphi(wrw^*).
\]
Thus choosing \(\varepsilon_n=1/n^2\) makes both sides small, rather than estimating only the initial projection. Its removal leaves infinite complementary endpoint projections on both sides of \(w(p-r)\).

Deleting a finite projection from an infinite one also leaves an infinite projection: otherwise the original projection would be the join of two finite projections, contradicting PC6. This includes a finite zero subpiece. All these statements concern infinite projections in a countably decomposable factor; no assertion about arbitrary properly infinite projections with different central supports is made.

<a id="cq6-minimal-projections-test-centrality"></a>

## CQ6. Minimal projections force a scalar centralizing quotient

Suppose the factor \(M\) has a nonzero minimal projection \(p\). There is a finite or countable orthogonal family \((p_i)\) of projections equivalent to \(p\) whose sum is \(1\). To construct it, extend \(\{p\}\) to a maximal such family by the choice argument of PC0. If its remainder \(q\) were nonzero, \(qMp\ne0\): otherwise the central support of \(p\), which is \(1\) by PC2, would be orthogonal to \(q\). Polar decomposition of a nonzero \(qxp\) supplies an initial nonzero subprojection of \(p\), hence all of \(p\), and a final projection in \(q\) equivalent to \(p\). This contradicts maximality. The filling sum is the PC1 strong sum. Countability follows from the faithful-state mass argument in CQ5. Equivalence transfers minimality to every \(p_i\).

Each corner is scalar, \(p_iMp_i=\mathbb Cp_i\). Indeed a nonscalar self-adjoint element in that corner would have a nontrivial spectral projection by the complete bounded spectral calculus; minimality excludes one. Real and imaginary parts treat all elements.

Let \((x_n)\) be bounded, with scalar ultraweak ultralimit \(\lambda1\), and suppose
\[
[x_n,a]\longrightarrow_\omega0\text{ strongly*}\quad(a\in M).
\tag{CQ6.1}
\]
Write \(p_i x_n p_i=\alpha_i(n)p_i\). Evaluating on any unit vector of \(p_iH\) shows \(\alpha_i(n)\to_\omega\lambda\), since that vector functional is normal. For \(\xi\in p_iH\),
\[
(x_n-\lambda)\xi=[x_n,p_i]\xi+
(\alpha_i(n)-\lambda)\xi\longrightarrow_\omega0.
\tag{CQ6.2}
\]
Apply the same reasoning to \(x_n^*\), whose ultraweak limit is \(\overline\lambda1\). Finite sums of \(p_iH\) are dense because the projections fill \(1\). The uniform bound on \(x_n-\lambda\), approximation by one such finite sum, and then a finite intersection of its ultrafilter convergence sets prove strong convergence on every vector; adjoints give strong*. CP's square-summable vector-series test makes this the intrinsic strong* assertion.

Consequently every such sequence is scalar modulo the strong*-zero ideal. This treats every type I factor without assuming a classification \(M=B(H)\): by the definition of type I it has a nonzero abelian projection, whose corner center is scalar by PC4, so that projection is minimal. Finite-dimensional and infinite-dimensional cases both occur in the argument; no separability of an ambient faithful Hilbert representation was needed.

<a id="cq7-balance-finite-partitions"></a>

## CQ7. Balancing a whole finite partition with a quantitative error

Fix a finite integer \(m\geq1\) and projection partitions
\[
q_n=\sum_{j=1}^m e_j(n),\qquad e_j(n)e_k(n)=0\quad(j\ne k).
\]
In a type \(\mathrm{II}_1\) factor with normalized trace \(\tau\), put
\(d_n=\tau(q_n)/m\). The full [AF2 trace-cut proof](central-afd-uniqueness-inputs.md#af2-trace-cuts-and-projection-repair) constructs a cut of any prescribed trace between zero and the trace of its containing projection. Cut each overfull cell to trace \(d_n\). The removed projections are orthogonal; their sum \(D_n\) has trace equal to the sum of the deficits in the underfull cells, since the total trace of the partition is \(md_n\).

Successive cuts of \(D_n\) supply orthogonal pieces of those deficits, including zero deficits, using the final exact remainder for the last one. Add them to the respective underfull cells. The result is a partition \(q_n=\sum_j e'_j(n)\) with all traces \(d_n\). Overfull cells were only decreased and underfull cells only increased, so in both cases the difference has square equal to the projection that was removed or added. Hence
\[
\|e'_j(n)-e_j(n)\|_{2,\tau}^2
=|\tau(e_j(n))-d_n|.
\tag{CQ7.1}
\]
FCT7's scalar trace comparison proves equivalence of the corrected cells. If each right side tends to zero along \(\omega\), [NT2](central-sequence-foundations.md#nt2-faithful-state-topology) transports their bounded trace convergence to intrinsic strong* convergence, and hence to either square seminorm of any faithful normal state. If \(q_n=0\), every cell and every correction is zero; otherwise \(d_n>0\) makes every corrected cell nonzero.

For an infinite factor, suppose \(q_n\ne0\) at each coordinate. When \(q_n\) is finite, its complement is infinite by CQ5. Add to it an infinite subprojection \(r_n\) of \(\varphi\)-mass less than \(1/n^2\), using CQ5, and add the same projection to the first cell. If \(q_n\) was already infinite, do nothing. The support is now infinite. At least one of its finitely many cells is infinite, since PC6 makes a finite join of finite cells finite.

If the original \(q_n\) was finite, choose \(m-1\) orthogonal infinite pieces inside the newly added \(r_n\), leaving an infinite remainder inside \(r_n\), by CQ5. Give one piece to each cell other than the first; the first retains that remainder along with its original cell. Every corrected cell is therefore its original projection plus an orthogonal subprojection of \(r_n\). Its difference from the original is a projection of \(\varphi\)-mass below \(1/n^2\). In particular there is no estimate for the difference of two unrelated small projections hidden in this step.

If the original \(q_n\) was already infinite, choose an infinite original cell and remove \(m-1\) orthogonal infinite pieces of total \(\varphi\)-mass less than \(1/n^2\), leaving an infinite remainder, by CQ5. Give one to each other cell. The donor is only decreased and the recipients only increased, so each change is a signed projection with square mass below \(1/n^2\). In both cases all resulting cells are infinite and equivalent. The stated bound \(2/n^2\) holds for every support and cell square mass, and their changes vanish strongly* ordinarily by NT2 and along the free ultrafilter. For \(m=1\) there are no pieces to transfer.

If the original support is \(1\), it is already infinite in an infinite factor; the support stays exactly \(1\). In a nonunital application the invisible change to a finite support is permitted and the new support remains its quotient representative. A zero quotient support is treated separately by the identically zero system. CQ6 covers factors with a minimal projection; in their scalar quotient there is no nonzero equivalent orthogonal partition of size greater than one. Thus no finite matrix case or smaller-than-unit support is lost.

## Proof routes used here

CQ1 uses only the complete C* positive and continuous calculus, norm completeness and finite-set approximate-identity estimates. CQ2–3 uses CF's Hilbert completion, the exact CP predual/vector-series proofs and BD's bounded-density proof. The central-sequence quotient's separate diagonal construction supplies the trace-metric completeness hypothesis of CQ3; this module does not assume that an arbitrary traced C* unit ball is complete in that weaker metric.

CQ4–7 use the complete retained PC0–7/FCT0–7 projection and center-trace arguments, AF2's full scalar-cut construction, and NT1–2's normal-functional and faithful-state topology proofs. These are programme proofs retained under their existing notices. The displayed balancing hypotheses are conditional estimates on coordinate partitions; this module does not infer them from equivalence in a quotient before that quotient and its trace have been constructed.
