# Trace Hilbert spaces and finite trace expectations

*New exposition: CC0-1.0 to the extent of rights held.*

The measurable-operator construction and trace pairing supply actual closed affiliated operators, their complete measure topology, spectral Fatou estimates and the onto positive isometry \(L^1(N,\sigma)\cong N_*\). This module supplies the \(L^2\) products and trace expectations used in [Invariant states and finite-rank projections](../src/invariant-states-and-finite-rank-projections.md). The trace \(\sigma\) is faithful, normal and semifinite; no separability or finiteness of \(\sigma(1)\) is assumed until stated. Inner products are linear in the second variable.

The preceding trace construction proves that finite-trace projections form a directed net increasing to \(1\). For a measurable \(x=v|x|\), its bounded finite-support spectral approximants
\[
x_n=v|x|1_{[1/n,n]}(|x|)
\]
satisfy
\[
\sigma(|x-x_n|^p)\longrightarrow0
\quad\text{whenever }\sigma(|x|^p)<\infty,\quad p>0.
\tag{TL1}
\]
Here each support has finite trace by the spectral Markov inequality. Spectral Fatou holds for measure convergence, including nets, and multiplication in the measurable algebra is continuous. The products below are these closed measurable products; equality never discards an operator domain.

<a id="trace-l2-completeness"></a>

## TL1. A complete Hilbert space of actual operators

Put
\[
L^2(N,\sigma)=\{x:\sigma(|x|^2)<\infty\},
\qquad \|x\|_2=\sigma(|x|^2)^{1/2}.
\]
The cutoff inequalities in the trace construction first show that this is a vector space and a bounded bimodule. In particular,
\[
\|a x b\|_2\leq\|a\|\|x\|_2\|b\|,
\qquad \|x^*\|_2=\|x\|_2.
\tag{TL2}
\]
These statements use the spectral integrals and do not presuppose a Hilbert-space completion.

For bounded \(x,y\) of finite square trace, their product \(y^*x\) belongs to the bounded finite trace ideal by the finite-domain algebra theorem. Positivity of the trace gives Cauchy–Schwarz, so
\[
|\sigma(y^*x)|\leq\|x\|_2\|y\|_2.
\]
Expanding \(\sigma((x+y)^*(x+y))\) proves the triangle inequality on this bounded square ideal. Apply it to the approximants in (TL1). They converge in measure to \(x,y\); spectral Fatou gives
\[
\|x+y\|_2\leq\|x\|_2+\|y\|_2
\]
for arbitrary \(x,y\in L^2\). Definiteness follows from faithfulness and spectral tails; homogeneity is scalar spectral calculus.

If \((z_n)\) is \(L^2\)-Cauchy, its spectral Markov bound makes it Cauchy in measure. Let \(z\) be its actual measurable limit. For fixed \(n\), Fatou gives
\[
\|z-z_n\|_2^2\leq\liminf_m\|z_m-z_n\|_2^2.
\tag{TL3}
\]
This is finite for a sufficiently large \(n\). Thus \(z\in L^2\), and (TL3) proves \(L^2\)-norm convergence. The space is complete, with the bounded finite-support operators dense by (TL1).

<a id="trace-holder-and-cyclicity"></a>

## TL2. The exact product bound and cyclic trace

For bounded square-integrable \(x,y\), write the bounded polar decomposition \(xy=u|xy|\). The product already belongs to the finite trace ideal. Its trace norm is computed by its polar partial isometry, and trace Cauchy–Schwarz gives
\[
\begin{aligned}
\|xy\|_1
&=\sigma(u^*xy)
=\sigma((x^*u)^*y)\\
&\leq\|x^*u\|_2\|y\|_2
\leq\|x\|_2\|y\|_2.
\end{aligned}
\tag{TL4}
\]
The last inequality follows from (TL2) and \(\|u\|\leq1\). The trace in the first line is a nonnegative real number, so applying the absolute-value Cauchy–Schwarz bound is legitimate.

For arbitrary \(x,y\in L^2\), choose the bounded spectral approximants \(x_n,y_n\). Their products are \(L^1\)-Cauchy, because
\[
\|x_ny_n-x_my_m\|_1
\leq\|x_n\|_2\|y_n-y_m\|_2
 +\|x_n-x_m\|_2\|y_m\|_2.
\]
Let their \(L^1\) limit be \(w\). Norm convergence in \(L^1\) implies measure convergence. Continuity of measurable multiplication also gives \(x_ny_n\to xy\) in measure. Uniqueness of the measure limit identifies \(w\) with the actual closed product \(xy\). Passing to the norm limit proves
\[
xy\in L^1,\qquad \|xy\|_1\leq\|x\|_2\|y\|_2.
\tag{TL5}
\]
Bounded trace cyclicity, first for \(x_n,y_n\) and then by (TL5), proves
\[
\sigma(xy)=\sigma(yx)\qquad(x,y\in L^2).
\tag{TL6}
\]
Thus
\[
\langle x,y\rangle=\sigma(x^*y)
\]
is a well-defined inner product with its stated norm; TL1 proves its completeness. Involution is isometric and the star identity for the trace proves conjugate symmetry. Linearity follows from the actual \(L^1\) pairing.

If \(h,k\in L^2_+\), choose positive bounded finite-support approximants \(h_n,k_n\). Their products have
\[
\sigma(h_nk_n)
=\sigma(k_n^{1/2}h_nk_n^{1/2})\geq0.
\]
The products converge in \(L^1\) by (TL5), so \(\sigma(hk)\geq0\). This does not assert that the noncommuting operator product \(hk\) is positive.

For a normal positive functional, the onto trace pairing supplies a unique \(a\in L^1_+\), and \(h=a^{1/2}\) is an actual positive \(L^2\) element with \(\|h\|_2^2=\sigma(a)\). A unitary conjugation has density \(u^*au\), by bounded \(L^1\) cyclicity and uniqueness. Spectral projections transform by the same conjugation. These are the density and domain facts used in the spectral-level selection proof.

<a id="finite-trace-expectation"></a>

## TL3. Expectations for a finite trace

Suppose now that \(M\) has a faithful normal tracial state \(\tau\), and \(B\subset M\) is a unital von Neumann subalgebra. Its restricted trace is again faithful and normal. For \(a\in M_+\), the functional
\[
b\longmapsto\tau(ab)=\tau(a^{1/2}ba^{1/2}),\qquad b\in B,
\]
is positive and normal, and is bounded above by \(\|a\|\tau\) on \(B_+\). The onto positive trace pairing gives its unique density \(E_B(a)\in L^1(B,\tau)_+\). This density is bounded by \(\|a\|1\). Indeed, a nonzero spectral projection \(e\) of the density above \(\|a\|+\delta\) would give
\[
(\|a\|+\delta)\tau(e)
\leq\tau(E_B(a)e)=\tau(ae)\leq\|a\|\tau(e),
\]
contradicting faithfulness. Thus \(E_B(a)\in B_+\).

Uniqueness of the density proves additivity and nonnegative homogeneity. Linear extension from positive elements is well-defined, since two positive decompositions giving the same element have the same trace pairings against every member of \(B\). It defines \(E_B:M\to B\), characterized by
\[
\tau(bE_B(a))=\tau(ba)\qquad(b\in B,\ a\in M).
\tag{TL7}
\]
It is unital, fixes \(B\), preserves the trace, and is bimodular. For example, for \(b,c,n\in B\), cyclicity gives
\[
\tau(nE_B(bac))
=\tau(nbac)
=\tau(cnb\,a)
=\tau(cnb\,E_B(a))
=\tau(nbE_B(a)c),
\]
so (TL7) and its injectivity give \(E_B(bac)=bE_B(a)c\).

This map is completely positive. If \([a_{ij}]\geq0\) and \(b_1,\ldots,b_r\in B\), positivity and bimodularity give
\[
\sum_{i,j}b_i^*E_B(a_{ij})b_j
=E_B\!\left(\sum_{i,j}b_i^*a_{ij}b_j\right)\geq0.
\]
The column test implies positivity of \([E_B(a_{ij})]\) in \(M_r(B)\). To justify the test, if a self-adjoint matrix \(C\) had a nonzero spectral band below \(-\delta\), choose a nonzero column of its negative-band projection. That column would satisfy \(b^*Cb\leq-\delta b^*b,\qquad b^*b\ne0\), contradicting all the column inequalities. Matrix continuous calculus and the matrix \(C^*\)-norm give this argument for every finite \(r\).

The \(2\)-positive Schwarz inequality follows by applying \(E_B\) to the positive \(2\)-by-\(2\) matrix with entries \(a^*a,a^*,a,1\) and completing the square. It gives
\[
E_B(a)^*E_B(a)\leq E_B(a^*a),\qquad
\|E_B(a)\|\leq\|a\|,\qquad
\|E_B(a)\|_2\leq\|a\|_2.
\tag{TL8}
\]
For \(a_i\uparrow a\) boundedly in \(M_+\), the increasing bounded net \(E_B(a_i)\) has a supremum \(h\in B\). Normality of the finite trace and (TL7), tested against \(b\in B_+\), give \(\tau(bh)=\tau(ba)\). Thus \(h=E_B(a)\). If \(f\in B_*^+\), the bounded positive functional \(f\circ E_B\) therefore preserves increasing positive suprema. The bounded-functional normality proof, NF1–4, puts \(f\circ E_B\) in \(M_*\). Every concrete predual functional is a linear combination of four positive predual functionals: polarize its summable vector series, using the square-summable factors from CP-04. Consequently every predual test composed with \(E_B\) is ultraweakly continuous. This proves ultraweak continuity of \(E_B\), rather than assuming an unproved equivalence for positive maps.

Finally (TL7) says
\[
\langle b,a-E_B(a)\rangle=0\qquad(b\in B).
\]
Together with (TL8), this identifies the continuous \(L^2\) extension of \(E_B\) with the orthogonal projection onto \(L^2(B,\tau)\). This constructs precisely the finite trace expectations needed for pinching, with no general-weight modular invariance premise.

<a id="decreasing-trace-expectations"></a>

## TL4. The intersection of decreasing trace spaces

Let \(B_1\supset B_2\supset\cdots\) be unital von Neumann subalgebras of this finite \(M\), and let \(P_n\) be their \(L^2\) projections. Decreasing orthogonal projections have a strong limit \(P\) onto the intersection of their ranges: for \(m\geq n\),
\[
\|P_n\xi-P_m\xi\|_2^2
=\|P_n\xi\|_2^2-\|P_m\xi\|_2^2.
\]
This proves convergence; the limit belongs to every range and fixes their intersection.

For \(x\in M\), the operators \(E_{B_n}(x)\) have norm at most \(\|x\|\). A subnet has an ultraweak cluster point \(y\) in that bounded ball, by concrete predual compactness. Every tail lies in each fixed \(B_k\), so \(y\in B_\infty=\bigcap_kB_k\). For \(z\in M\), the functional \(a\mapsto\tau(z^*a)\) is normal. Therefore
\[
\langle z,Px\rangle
=\lim_n\tau(z^*E_{B_n}(x))
=\tau(z^*y).
\]
Bounded vectors are \(L^2\)-dense, so \(Px\) is the vector of \(y\in B_\infty\). Density and closedness now imply
\[
\bigcap_nL^2(B_n,\tau)=L^2(B_\infty,\tau).
\tag{TL9}
\]
If \(B_\infty=\mathbb C1\), trace preservation gives \(y=\tau(x)1\) and \(E_{B_n}(x)\to\tau(x)1\) in \(2\)-norm. The proof identifies the Hilbert-space intersection using bounded operators; it does not assume that the intersection commutes with taking \(L^2\) closures.

<a id="finite-factor-trace-cuts"></a>

## TL5. Exact trace cuts and matrix pieces

Let \(N\) be a type \(\mathrm{II}_1\) factor with normalized trace \(\tau\). If \(0\ne e\in N\), the corner \(eNe\) has no minimal projection: a minimal projection in that corner would also be minimal in \(N\). Repeatedly split a nonzero projection into two nonzero pieces and keep a piece of trace at most half the preceding trace. Thus every nonzero corner has nonzero projections of arbitrarily small positive trace.

For \(0\leq t\leq\tau(e)\), order the projections \(p\leq e\) with \(\tau(p)\leq t\) by inclusion. Every chain has its projection supremum as an upper bound, and normality keeps its trace at most \(t\). A maximal member exists by the maximal principle. If \(\tau(p)<t\), its nonzero complement in \(e\) contains a nonzero \(q\) with \(\tau(q)\leq t-\tau(p)\). Then \(p+q\) contradicts maximality. Consequently there is a projection of every prescribed trace \(t\) under \(e\).

The [projection-comparison arguments](central-finite-trace-inputs.md) show that two projections in a factor are comparable by a partial isometry. If their finite traces agree, the unmatched complement has trace zero and hence is zero. They are therefore equivalent. Split a projection \(e\) successively into \(q\) pieces of trace \(\tau(e)/q\), using the preceding trace cuts. Choose partial isometries \(v_i\) from the first piece to each piece, with \(v_1\) equal to that first piece. Then
\[
e_{ij}=v_i v_j^*,\qquad
e_{ij}e_{kl}=\delta_{jk}e_{il},\qquad
e_{ij}^*=e_{ji},\qquad
\sum_i e_{ii}=e.
\tag{TL10}
\]
Their initial pieces are the same and their final pieces are orthogonal, which proves the displayed multiplication identities. This supplies equal dyadic atoms and actual matrix units in each nonzero normalized corner.

In the finite tracial instances of the pinching and expected-subfactor constructions, TL3 supplies every required trace-preserving expectation, and TL4 supplies the decreasing-expectation intersection. All the relevant subalgebras lie in the trace centralizer, and their normalized corners again carry faithful tracial states. Thus these finite instances require no general-weight modular construction. Their simultaneous binary cuts, compatible matrix induction, irreducible AFD containment and decreasing-AFD existence remain separate stated constructions; TL3–TL5 do not replace those arguments.

<a id="ordinary-trace-and-rank"></a>

## TL6. Ordinary trace and Hilbert-space rank

For an arbitrary Hilbert space \(H\), the arbitrary matrix trace, with scalar coefficient algebra \(\mathbb C\), constructs the faithful normal semifinite trace \(\operatorname{Tr}\) on \(B(H)\). For an orthonormal basis \((e_j)\) and \(X\geq0\) it is
\[
\operatorname{Tr}(X)=\sum_j\langle e_j,Xe_j\rangle,
\]
where the sum means the supremum of finite subsums. This definition is independent of the basis. If \((f_\alpha)\) is another orthonormal basis, Parseval and interchange of nonnegative finite-subsum suprema give
\[
\sum_j\|X^{1/2}e_j\|^2
=\sum_{j,\alpha}|\langle f_\alpha,X^{1/2}e_j\rangle|^2
=\sum_\alpha\|X^{1/2}f_\alpha\|^2.
\]
For a projection \(p\), choose an orthonormal basis of its range and extend it by one of its kernel. The displayed sum is the number of range basis vectors, with value \(+\infty\) for an infinite range. Hence
\[
0<\operatorname{Tr}(p)<\infty
\quad\Longleftrightarrow\quad
0<\operatorname{rank}(p)<\infty,\qquad
\|p\|_{\mathrm{HS}}^2=\operatorname{Tr}(p)=\operatorname{rank}(p).
\]
The projection selected using this trace therefore has exactly the finite Hilbert-space rank used in the finite-algebra corollary. This trace is distinct from the finite trace on the represented algebra.

## Sources and prerequisites

The full measurable-operator construction, spectral Fatou proof and positive \(L^1\)-predual isometry are in the linked trace module. The exact bounded predual, Hilbert-space and scalar integration foundations are retained there. Finite matrix calculus is supplied by [Scalar GNS and matrix \(C^*\)-norms](scalar-gns-and-matrix-cstar-norms.md). The argument above proves its \(L^2\) completion, sharp product bound, cyclic pairing, finite trace expectation and decreasing-space assertions in their stated scope.

Sorin Popa’s [1986 paper](https://www.theta.ro/jot/archive/1986-016-002/1986-016-002-005.pdf), Section2 and Remark2.3, supplies the freely readable invariant-state/square-root comparison. Anantharaman and Popa’s [author draft](https://www.math.ucla.edu/~popa/Books/IIun.pdf), Sections10.2–10.3 and Lemma11.1.9, supplies the normal-state, spectral-level and decreasing-expectation comparisons. The human sources retain their own distribution terms; their prose and PDFs are not redistributed here.
