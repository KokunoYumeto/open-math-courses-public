# Finite traces with arbitrary centers

*Retained complete programme arguments PC0–7 and FCT0–7. Original programme exposition: CC0-1.0 to the extent of rights held; the same terms remain in force.*

The projection comparison proof supplies the cancellation, central corners and arbitrary sums used to construct the trace. The construction proves existence, faithfulness and normal uniqueness for every finite von Neumann algebra, including nonseparable algebras and non-countably-decomposable centers. No scalar faithful trace or direct-integral decomposition is a starting assumption.

These complete proof sections come from the programme's [projection comparison](../../OA-FLOW/OA-FLOW-PC.html) and [center-valued trace](../../OA-FLOW/OA-FLOW-FCT.html) lessons. The links to their earlier proofs below use the retained CF/SF/CP/ST foundations. The remaining sections of those larger lessons are outside this selected prerequisite route.

<a id="retained-pc-complete-inputs"></a>

# Projection comparison and the countably decomposable type III case

*Independent exposition and original figure/source: CC0-1.0 to the extent of rights held.*

Let \(M=M''\subseteq B(H)\), where \(H\) is any complex Hilbert space and the identity is \(1_H\). Zero spaces are permitted. A projection is an element \(p=p^*=p^2\). Write \(p\sim q\) if some \(v\in M\) has \(v^*v=p,\ vv^*=q\), and \(p\precsim q\) if the final projection may instead be any subprojection of \(q\). A projection \(p\) is finite if \(p\sim q\leq p\) forces \(q=p\). Proper infiniteness means that \(p\neq0\) and every nonzero central compression of the unit of \(pMp\) is infinite. Type III means absence of nonzero finite projections. A projection is countably decomposable if every orthogonal family of its nonzero subprojections is countable.

The actual earlier mathematical inputs are CF Sections 1, 6–8 and 10, with Sections 2–5 as the continuous-calculus predecessors (choice/maximality, norm series, bounded C\* calculus, Hilbert projection/adjoints/completion), SF-0 and SB-0 (the commutant-unitary test and elementary Hilbert facts), and CP-01–06 (concrete predual and vector-series topology). The polar construction below is the bounded specialization of the reviewed HA-R4 range-isometry argument, written completely here; its unbounded form theorem is not an additional input. No bounded or unbounded spectral representation theorem, weight theorem, trace existence, spectral classification or cardinal-dimension theorem is an input.

Free source comparison: [Jesse Peterson's author notes, 2020, Sections 5.1–5.2, printed 83–90](https://math.vanderbilt.edu/peters10/teaching/spring2020/OperatorAlgebras.pdf#page=83), and [Brent Nelson's author notes, Lemma 5.2.9 and Proposition 5.2.13, printed 49–51](https://users.math.msu.edu/users/banelson/teaching/209/209_notes.pdf#page=50). Every statement used in this proof is proved below or bound to the specified earlier programme proof. In particular the countability condition will concern only the projection to be embedded.

<a id="oa-flow.projection.pc0"></a>
Actual earlier proof ranges: OA-FLOW.CF.1, OA-FLOW.CF.2, OA-FLOW.CF.3, OA-FLOW.CF.4, OA-FLOW.CF.5, OA-FLOW.CF.6, OA-FLOW.CF.7, OA-FLOW.CF.8, OA-FLOW.CF.10, OA-FLOW.SF.SF0, OA-FLOW.SF.SB0, OA-FLOW.CP.1, OA-FLOW.CP.2, OA-FLOW.CP.3, OA-FLOW.CP.4, OA-FLOW.CP.5, OA-FLOW.CP.6. The bounded polar construction in PC1 is proved locally. Its comparison with the later HA-R range-isometry proof is historical development context and adds no unbounded-form premise.

<a id="oa-flow.pc.0"></a><a id="pc-0"></a>

## PC-0. The two set-theoretic operations

We need no unproved infinite-cardinal arithmetic. If \(u:A\to B\) and \(v:B\to A\) are injections, set \(A_0=A\setminus v(B)\) and \(D=\bigcup_{n\geq0}(vu)^nA_0\). The map equal to \(u\) on \(D\) and to \(v^{-1}\) on \(A\setminus D\) is a bijection \(A\to B\). The second inverse is defined since \(A_0\subseteq D\). Their images are disjoint because \(vu(D)\subseteq D\). For surjectivity, if \(v(b)\in D\), then \(v(b)\notin A_0\), so \(v(b)\in vu(D)\) and injectivity gives \(b\in u(D)\); otherwise the inverse branch maps \(v(b)\) to \(b\).

An infinite set \(I\) is in bijection with \(I\setminus\{i_0\}\) for any \(i_0\in I\): choose distinct \(i_0,i_1,\ldots\), shift \(i_n\mapsto i_{n+1}\), and fix all other points.

Every infinite set \(I\) has a partition \(I=I_0\sqcup I_1\) with both pieces in bijection with \(I\). Here are details at the choice convention of CF-1. Well-order \(I\), and identify its cardinal with an infinite initial ordinal \(\kappa\). If any infinite cardinal up to \(\kappa\) failed to have \(|\lambda\times\{0,1\}|=\lambda\), take the least failing one \(\lambda\). Order its pairs first by their ordinal coordinate, then by the second coordinate. The predecessors of any pair have cardinal at most \(2|\beta|+1<\lambda\), by minimality when \(|\beta|\) is infinite and by finiteness otherwise; adjoining one point does not change an infinite cardinal by the preceding shift argument. The order type cannot exceed \(\lambda\): a point at position \(\lambda\) would have \(\lambda\) predecessors. Thus there is an injection of the pairs into \(\lambda\); the converse injection is immediate, and the bijection just proved gives a contradiction. Transport the two images to \(I\).

<a id="oa-flow.projection.pc1"></a>

<a id="oa-flow.pc.1"></a><a id="pc-1"></a>

## PC-1. Corners, supports and arbitrary orthogonal sums

The orthogonal projection onto an intersection of projection ranges commutes with every unitary of \(M'\), since that intersection reduces those unitaries. SF-0 puts the projection in \(M\). This supplies all meets. Complements give joins; equivalently a join projects onto the closed span of the ranges. Orthogonal joins are their strong sums.

For \(e\in M\) a projection, \(eMe\) acting on \(eH\) is a concrete von Neumann algebra. Indeed extend a weak operator limit on \(eH\) by zero on \((1-e)H\); it is a weak operator limit of elements of \(M\), hence lies in \(M\) and is compressed by \(e\). The following finite-vector argument gives its bicommutant characterization locally.

For completeness the latter argument uses only Hilbert projection. For a unital \*-algebra \(A\) and a tuple \((\xi_1,\ldots,\xi_n)\), project onto the closed orbit \(\overline{\{(a\xi_j)_j:a\in A\}}\). Its matrix entries commute with \(A\). Every diagonal \(x\in A''\) therefore preserves this space, which contains the original tuple. Thus \(x\) is a strong limit of elements of \(A\), on arbitrary finite tuples. If \(A\) is weak operator closed the limit belongs to \(A\), proving \(A=A''\).

Given \(x\in M\), put \(h=(x^*x)^{1/2}\). The rule \(h\xi\mapsto x\xi\) is a well-defined isometry, because \(\|h\xi\|=\|x\xi\|\). Extend it to \(\overline{hH}=(\ker x)^\perp\), and set it to zero on \(\ker x\). This gives a partial isometry \(v\), with
\[
x=vh,\qquad v^*v=[x^*H],\qquad vv^*=[xH].
\tag{PC1}
\]
The brackets mean projection onto the closed indicated range. The initial range equality follows from \((x^*H)^\perp=\ker x\). Every unitary of \(M'\) commutes with \(x,h\), preserves their kernels and ranges, and therefore commutes with this isometry and its zero summand. SF-0 gives \(v\in M\); consequently both support projections lie in \(M\). This proves the entire bounded polar input, including zero and noninjective operators.

Suppose \((v_i)_{i\in I}\subset M\) are partial isometries with initial projections \(p_i\) and final projections \(q_i\), each family separately orthogonal. For every finite \(F\subset I\),
\[
\left\|\sum_{i\in F}v_i\xi\right\|^2
=\sum_{i\in F}\|p_i\xi\|^2\leq\|\xi\|^2.
\tag{NP1}
\]
The scalar sum is the supremum of its finite subsums. For any \(\varepsilon>0\) a finite subsum is within \(\varepsilon^2\) of that supremum, so every complementary finite vector sum has norm at most \(\varepsilon\). Completeness gives a strong limit \(v\); applying the same argument to the adjoints gives their strong limit \(v^*\). The limits commute with \(M'\), hence belong to \(M\). Uniformly bounded strong products converge strongly by expanding their differences, so
\[
v^*v=\sum_i p_i,\qquad vv^*=\sum_i q_i.
\tag{PC2}
\]
Thus equivalences or subequivalences can be added over arbitrary orthogonal index sets. More generally uniformly bounded operators supported on separate orthogonal corners have a strong-star diagonal sum, by the same squared-norm tail estimate.

Composition of implementing partial isometries proves transitivity of \(\precsim\): if \(u^*u=p,\ uu^*\leq q=v^*v,\ vv^*\leq r\), then \((vu)^*(vu)=p\) and \((vu)(vu)^*\leq r\). Adjoints give symmetry of \(\sim\); identity projections give reflexivity.

<a id="oa-flow.projection.pc2"></a>

<a id="oa-flow.pc.2"></a><a id="pc-2"></a>

## PC-2. Central supports and comparison

For a projection \(p\), let \(c(p)\) project onto \(\overline{\operatorname{span}}MpH\). This space reduces \(M\), so its projection commutes with \(M\). It also reduces \(M'\), because \(y'xp\xi=xpy'\xi\). SF-0 puts that projection in \(M\); hence \(c(p)\in Z(M)\). It dominates \(p\). Any central projection \(z\geq p\) contains every \(xpH\), so \(c(p)\leq z\). This proves the least-central-projection definition without an imported support theorem.

If \(pMq=\{0\}\), then \(p\) vanishes on \(MqH\), giving \(pc(q)=0\). Since \(c(q)\) is central, minimality gives \(c(p)\leq1-c(q)\). Conversely orthogonal central supports force \(pxq=0\) for every \(x\in M\). We have proved
\[
pMq=\{0\}\quad\Longleftrightarrow\quad c(p)c(q)=0.
\tag{PC3}
\]
When \(pMq\neq0\), polar decomposition of a nonzero \(pxq\) supplies nonzero equivalent projections below \(q\) and \(p\), respectively. Equivalence also preserves central support: every central projection dominating one initial projection dominates the final projection, by commuting through its partial isometry, and conversely.

Take a maximal collection of nonzero partial isometries with separately orthogonal initial projections below \(p\) and final projections below \(q\). Chain unions supply upper bounds, so CF-1 applies. Let \(v\) be its [PC-1](#oa-flow.projection.pc1) strong-star sum and set \(p_0=p-v^*v,\ q_0=q-vv^*\). A nonzero bridge from \(p_0\) to \(q_0\) could be added, so \(c(p_0)c(q_0)=0\). With \(z=c(q_0)\) we have \(zp_0=0\) and \((1-z)q_0=0\). Compressing \(v\) gives
\[
zp\sim z v^*v\precsim zq,\qquad
(1-z)q\sim(1-z)vv^*\precsim(1-z)p.
\tag{NP2}
\]
This is central comparison for arbitrary projections and arbitrary cardinality.

<a id="oa-flow.projection.pc3"></a>

<a id="oa-flow.pc.3"></a><a id="pc-3"></a>

## PC-3. Mutual subequivalence and the join formula

Suppose \(p\precsim q\) and \(q\precsim p\), implemented by \(u^*u=p,\ uu^*\leq q\) and \(v^*v=q,\ vv^*\leq p\). In the corner with unit \(p\), \(T=vu\) is an isometry. Put
\[
a_0=p-vv^*,\quad a_n=T^na_0(T^*)^n,\quad
A=\sum_{n\geq0}a_n,\quad B=uAu^*.
\]
Since \(a_0T=0\), the \(a_n\) are orthogonal: for \(m>n\), their product contains \(a_0T^{m-n}=0\). Also \(v^*a_0v=0\) and \(v^*a_{n+1}v=ua_nu^*\), so \(v^*Av=B\). The projection \(p-A\) is at most \(vv^*\). Therefore \(v^*(p-A)\) has initial projection \(p-A\) and final projection \(q-B\). Its initial and final projections are orthogonal to those of \(uA\). Their sum satisfies
\[
W=uA+v^*(p-A),\qquad W^*W=p,\qquad WW^*=q.
\tag{NP3}
\]
This proves mutual subequivalence implies equivalence, including zero projections.

For \(x=(1-p)q\), its kernel is \((1-q)H\oplus(pH\cap qH)\). Its initial support is therefore \(q-p\wedge q\). Also \(\ker x^*=pH\oplus((1-p)H\cap(1-q)H)\), so its final support is \(p\vee q-p\). [PC-1](#oa-flow.projection.pc1) gives
\[
(p\vee q)-p\sim q-(p\wedge q).
\tag{NP4}
\]

<a id="oa-flow.projection.pc4"></a>

<a id="oa-flow.pc.4"></a><a id="pc-4"></a>

## PC-4. The center of any projection corner

For \(e\neq0\), work in \(Mc(e)\), with identity \(c(e)\). Compression maps \(Z(M)c(e)\) into \(Z(eMe)\). It is injective: a central \(h\) with \(he=0\) annihilates \(MeH\), whose span is dense in \(c(e)H\).

Choose a maximal orthogonal family \((r_i)\) of nonzero projections subequivalent to \(e\), including \(r_0=e\). The residual projection is zero: otherwise PC3 provides a bridge to \(e\) and thus an additional member. Choose \(v_i^*v_i\leq e,\ v_iv_i^*=r_i,\ v_0=e\). For \(h\in Z(eMe)\) define
\[
\widetilde h=\sum_i v_i h v_i^*.
\tag{PC4}
\]
Each summand is supported on \(r_i\) and has norm at most \(\|h\|\); [PC-1](#oa-flow.projection.pc1) supplies the bounded strong-star sum. It compresses to \(h\) at \(e\). For \(x\in Mc(e)\), \(v_i^*xv_j\in eMe\), so it commutes with \(h\). Multiplying this identity by \(v_i,v_j^*\) shows \(r_i\widetilde h x r_j=r_i x\widetilde h r_j\). Since finite sums of \(r_i\) converge strongly to \(c(e)\), all matrix corners determine an operator, and \(\widetilde h\) is central.

Commutation of \(h\) with \(v_i^*v_i\) gives, in each \(r_i\) corner, preservation of products and adjoints; hence extension and compression are inverse unital \*-isomorphisms. Their continuity is also explicit. For vectors \(\xi,\eta\),
\[
\langle\widetilde h\xi,\eta\rangle
=\sum_i\langle h v_i^*\xi,v_i^*\eta\rangle,\qquad
\sum_i\|v_i^*\xi\|^2\leq\|\xi\|^2.
\tag{PC5}
\]
Only countably many coordinates are nonzero: for each integer \(n\), finitely many squared norms exceed \(1/n\). Thus this is a CP vector-series functional on \(eMe\). A square-summable series of ambient vector pairs remains square summable after these substitutions, by the same inequality and the countable union of their supports. Extension is ultraweakly continuous on its entire domain; compression is too by its vector-pair substitutions. In particular central projections of \(eMe\) are precisely \(ez\), \(z\in Z(M)c(e)\), and this identification preserves bounded increasing suprema.

<a id="oa-flow.projection.pc5"></a>

<a id="oa-flow.pc.5"></a><a id="pc-5"></a>

## PC-5. Finite central parts and properly infinite halving

Finiteness passes to subprojections: a partial isometry from \(r\leq p\) onto a strict subprojection of \(r\), added to \(p-r\), would make \(p\) equivalent to a strict subprojection of itself. Finiteness passes through equivalence by conjugating the corner with its implementing partial isometry. The same corner isomorphism preserves proper infiniteness.

In any projection corner with unit \(e\), choose a maximal orthogonal family of finite central projections. Its sum \(z_f\) is finite. Indeed an equivalence from \(z_f\) to a subprojection commutes with each central summand and restricts there to equality; its full final projection must therefore equal \(z_f\). Every finite central projection is below \(z_f\), since its portion outside \(z_f\), if nonzero, could be added. Hence \(e-z_f\), when nonzero, has no nonzero finite central compression and is properly infinite. This decomposition is unique and, by [PC-4](#oa-flow.projection.pc4), arises from an ambient central split on \(c(e)\).

We prove halving in a corner \(A\) whose unit \(e\) is properly infinite. In every nonzero central corner \(zA\), infiniteness gives \(w^*w=z,\ ww^*<z\). Its defect \(d=z-ww^*\neq0\) has orthogonal equivalent translates \(w^nd(w^*)^n\), because \(dw=0\). Let \(h=c_A(d)\leq z\). Equivalence preserves their common central support \(h\), so they lie in \(hA\) and have full support there.

Extend this countable seed to a maximal orthogonal family \((d_i)_{i\in I}\) equivalent to \(d\) inside \(hA\). Let \(Q=\sum_i d_i,\ r=h-Q\), and fix \(i_0\). Comparison in \(hA\) gives a central \(t\leq h\) with \(rt\precsim d_{i_0}t\) and \(d_{i_0}(h-t)\precsim r(h-t)\). If \(t=0\), another copy of \(d\) fits in \(r\), contradicting maximality. Thus \(t\neq0\).

The infinite family absorbs this residual on \(t\). Every \(d_it\) is nonzero because \(c_A(d_i)=h\), and they remain mutually equivalent by central compression of their implementing partial isometries. Map \(rt\) into \(d_{i_0}t\), and use a bijection \(I\to I\setminus\{i_0\}\) to map \(Qt\) into the other summands. Orthogonal addition gives \(t\precsim Qt\); the reverse subequivalence is inclusion. [PC-3](#oa-flow.projection.pc3) gives \(t\sim Qt\). Partition \(I\) into two pieces each in bijection with \(I\), using [PC-0](#oa-flow.projection.pc0). Their sums in \(Qt\) are each equivalent to \(Qt\). Transport them through the equivalence \(t\sim Qt\). We obtain \(t=r_t+s_t\), with \(r_t\sim s_t\sim t\).

This construction works inside every nonzero central portion of \(e\). A maximal orthogonal family of central portions admitting such a halving must therefore fill \(e\). Adding their halves and their equivalences by [PC-1](#oa-flow.projection.pc1) proves
\[
e=r+s,\qquad r\sim s\sim e.
\tag{NP5}
\]
No countability assumption was used. Repeated splitting is consequently legitimate.

There are countably many orthogonal copies of \(e\) inside \(e\): choose an isometry \(w\) from \(e\) onto \(s\), and put \(e_n=w^n r(w^*)^n\). Their orthogonality follows from \(rw=0\); each is equivalent to \(e\). Their sum \(Q\) contains \(e_0\sim e\), so \(e\precsim Q\leq e\) and [PC-3](#oa-flow.projection.pc3) gives \(Q\sim e\). Transport the family through this equivalence to obtain a filling family
\[
e=\sum_{n\geq0}f_n,\qquad f_n\sim e,\qquad f_nf_m=0\ (n\neq m).
\tag{PC6}
\]
This argument does not incorrectly assume that the first shift's original ranges already fill \(e\).

<a id="oa-flow.projection.pc6"></a>

<a id="oa-flow.pc.6"></a><a id="pc-6"></a>

## PC-6. The finite-join consequence

If \(p,q\) are finite, NP4 makes \(p\vee q-p\) finite. Replace \(q\) by this projection and work in the corner with unit \(p+q\). If that unit were infinite, [PC-5](#oa-flow.projection.pc5) would give a nonzero properly infinite central piece; compress to it. We would have a properly infinite unit \(1=p+q\) with both summands finite.

Choose its halving \(1=r+s,\ r\sim s\sim1\). Compare \(p\wedge r\) and \(q\wedge s\), with central \(z\) satisfying \(z(p\wedge r)\precsim z(q\wedge s)\) and the reverse comparison on \(1-z\). On \(z\), NP4 and orthogonal addition give
\[
zr=z(r-p\wedge r)+z(p\wedge r)
\precsim z((p\vee r)-p)+z(q\wedge s)\leq zq.
\tag{NP6}
\]
The target summands are orthogonal: \(q\wedge s\) is orthogonal to both \(p\) and \(r\), thus to their join. Both lie under \(q\). If \(z\neq0\), \(zr\sim z\) is infinite and cannot be subequivalent to finite \(zq\); hence \(z=0\). On \(1-z\) interchange \(p,r\) with \(q,s\) to get the same contradiction unless \(1-z=0\). This is impossible for a nonzero unit. Therefore \(p\vee q\) is finite. Induction also proves every finite orthogonal sum of finite projections finite.

<a id="oa-flow.projection.pc7"></a>

<a id="oa-flow.pc.7"></a><a id="pc-7"></a>

## PC-7. Countability belongs to the source corner

A faithful normal state on \(fMf\) makes \(f\) countably decomposable. Every nonzero orthogonal subprojection has strictly positive state value. Finitely many can have value at least \(1/n\), since their finite sums have value at most one; taking their union over \(n\) proves countability. No state on \(M\) is inferred.

Conversely suppose \(f\neq0\) is countably decomposable. For a unit vector \(\xi\in fH\), let \(r_\xi\) project onto \(\overline{M'\xi}\). SF-0 gives \(r_\xi\in M\), and \(r_\xi\leq f\). The vector functional is faithful on \(r_\xi Mr_\xi\): if a positive \(a\) there has zero value, then \(a^{1/2}\xi=0\), so commutation makes \(a^{1/2}\) zero on the dense orbit \(M'\xi\).

A maximal orthogonal collection of such nonzero \(r_{\xi_j}\leq f\) fills \(f\); a nonzero remainder would contain a vector providing an additional one. It is finite or countable by assumption. With strictly positive \(c_j\) summing to one,
\[
\omega(x)=\sum_j c_j\langle x\xi_j,\xi_j\rangle,\qquad x\in fMf,
\tag{PC7}
\]
is normal by CP's square-summable vector-series description. It is a state. Zero value on positive \(x\) forces \(x^{1/2}\) to vanish on every commutant orbit, hence on their filling sum, proving faithfulness. This proves the exact equivalence of the two corner conventions.

Now let \(e\) be properly infinite and let \(f\) be countably decomposable, with \(c(f)\leq c(e)\). A maximal orthogonal family of nonzero \(q_i\leq f\) with \(q_i\precsim e\) fills \(f\): a nonzero residual \(a\) has \(c(a)c(e)=c(a)\neq0\), so PC3 supplies another subprojection. The family is countable by the hypothesis on \(f\). Use distinct copies \(e_i\sim e\) from [PC-5](#oa-flow.projection.pc5) to place each \(q_i\) under \(e_i\), then add the implementing partial isometries. We have proved
\[
c(f)\leq c(e),\quad e\text{ properly infinite},\quad
f\text{ countably decomposable}\quad\Longrightarrow\quad f\precsim e.
\tag{PC8}
\]
The zero source case is immediate. In particular two countably decomposable properly infinite projections with the same central support are equivalent by applying PC8 twice and [PC-3](#oa-flow.projection.pc3). The whole ambient algebra need not be countably decomposable.



<a id="retained-fct-complete-inputs"></a>


<a id="oa-flow.fct.setting"></a>

# The normalized trace with its full center retained

Let \(M\subseteq B(H)\) be a finite von Neumann algebra on an arbitrary complex Hilbert space, and put \(Z=Z(M)\). Finiteness means that an isometry in every projection corner has full final projection. Equivalently, the identity is a finite projection, since finiteness passes to subprojections by PC5. No countability, factor, separability or scalar-trace assumption is made.

We construct a unique normal positive linear map \(T:M\to Z\) such that

<a id="equation-fct1"></a>

\[
 T(1)=1,\qquad T(zx)=zT(x),\qquad T(xy)=T(yx)
 \quad(z\in Z,\ x,y\in M).
 \tag{FCT1}
\]
It is faithful, has norm one when \(M\ne0\), and preserves all bounded increasing positive suprema. Normal here means continuous on the entire concrete ultraweak space, not just on bounded sets. For the zero algebra the map is zero; its norm is zero and its normalization is \(T(0)=0\).

The construction is quantitative: maps with trace distortion tending to one converge in operator norm. We prove that stability first, under an explicit tiling condition. We then supply the tilings, normal center-valued states and two local balancing arguments needed to produce those maps.

The earlier complete proofs used are CF1/3–8, SF0 and SB1–6, CP1–6, ST1–2, and [PC1–7](#oa-flow.projection.pc1). Only the last automorphism corollary additionally uses the order-normal positive-map criterion NF6. Each use is located below. Scalar trace existence, type-I classification, direct integrals and a fixed-point theorem are not premises.

*Original exposition and illustration: CC0-1.0 to the extent of rights held.*

<a id="fct-0"></a>

<a id="oa-flow.fct.0"></a>

## FCT0. Three analytic operations

For a positive functional \(f\) on a unital C-star algebra, the positive/negative decomposition of a self-adjoint element shows that \(f\) is real on self-adjoint elements, hence \(f(x^*)=\overline{f(x)}\). Positivity of \(f((x+ty)^*(x+ty))\) for all complex \(t\) proves

<a id="equation-fct2"></a>

\[
 |f(y^*x)|^2\le f(x^*x)f(y^*y).
 \tag{FCT2}
\]
Indeed the diagonal values are nonnegative and the mixed terms are conjugates. If \(f(y^*y)>0\), minimize the scalar quadratic. If that diagonal is zero, a nonzero mixed term would make the quadratic negative by a sufficiently large scalar of the opposite phase. This also proves the zero-diagonal case. Setting \(y=1\) and using \(x^*x\le\|x\|^2 1\), from CF7, gives \(\|f\|=f(1)\), including \(f=0\).

Suppose \(F:M\to Z\) is positive and linear. Every character \(\chi\) of the commutative unital C-star algebra \(Z\) is positive, by CF6 and positive square roots. Thus \(\chi\circ F\) is positive and
\[
 |\chi(F(x))|\le \chi(F(1))\|x\|\le\|F(1)\|\|x\|.
\]
CF6 proves \(\|z\|=\sup_\chi|\chi(z)|\) for every complex \(z\in Z\). Consequently

<a id="equation-fct3"></a>

\[
 \|F\|=\|F(1)\|.
 \tag{FCT3}
\]
This proves boundedness as well as the exact norm. It does not identify a complex image with its real part. The same argument works in a nonzero central corner, using its identity.

For completeness, a bounded increasing net \(a_j\ge0\) has its supremum as a strong limit in \(M\). Its limiting quadratic values define a bounded positive form: homogeneity and the parallelogram identity pass to the scalar limits along the directed net. Polarization and CF8's Hilbert representation theorem give a positive operator \(a\). We have \(0\le a-a_j\le C1\) for a common bound \(C\), so CF6–7 give

<a id="equation-fct4"></a>

\[
 \|(a-a_j)\xi\|^2\le C\langle(a-a_j)\xi,\xi\rangle\longrightarrow0.
 \tag{FCT4}
\]
Strong closedness puts \(a\) in \(M\), and its quadratic values show that it is the least upper bound. CP4–6's vector-series tail estimate makes every bounded strong limit an ultraweak limit. In particular an ultraweakly continuous positive map \(F\) preserves these suprema: the bounded increasing \(F(a_j)\) have a strong supremum \(b\) by this same argument, hence an ultraweak limit \(b\), while continuity gives the ultraweak limit \(F(a)\). Uniqueness of the limit gives \(b=F(a)\).

We will also use the following complete decomposition of normal functionals. By CP4–6 every \(\omega\in M_*\) is \(\sum_j\omega_{u_j,v_j}\), with both vector sequences square summable and inner products linear in the first variable. Polarization gives

<a id="equation-fct5"></a>

\[
 \omega_{u,v}=\frac14\sum_{k=0}^3 i^k\omega_{u+i^kv,u+i^kv}.
 \tag{FCT5}
\]
For each \(k\), the sum of these positive vector functionals is normal: \(\sum_j\|u_j+i^kv_j\|^2<\infty\). Thus every normal functional is a linear combination of four positive normal functionals. CP6 also proves that \(M_*\) is norm closed in \(M^*\). Finally \(x\mapsto axb\) is normal for bounded \(a,b\): substituting in its vector series replaces \((u_j,v_j)\) by \((bu_j,a^*v_j)\), which are still square summable. These assertions apply equally to \(Z\) and all concrete corners.

<a id="fct-1"></a>

<a id="oa-flow.fct.1"></a>

## FCT1. Quantitative stability, with the tiling premise explicit

Call a nonzero projection \(p\) a **central tile** if there are finitely many orthogonal projections

<a id="equation-fct6"></a>

\[
 p=p_1\sim p_2\sim\cdots\sim p_k,\qquad
 p_1+\cdots+p_k=z\in Z,
 \tag{FCT6}
\]
where \(z\) is a nonzero central projection. Necessarily \(c(p)=z\), by PC2's preservation of central support under equivalence. This definition includes \(k=1\).

For this section alone assume that every projection is an arbitrary orthogonal sum of central tiles. A **normal center-valued state** is a normal positive linear \(\phi:M\to Z\) satisfying \(\phi(1)=1\) and \(\phi(zx)=z\phi(x)\). Suppose \(a_n>1\) decreases to one and such states satisfy, on all of \(M\),

<a id="equation-fct7"></a>

\[
 \phi_n(xx^*)\le a_n\phi_n(x^*x).
 \tag{FCT7}
\]
For \(m<n\) and a central tile as in (FCT6), a partial isometry between \(p\) and \(p_i\), used in both directions in (FCT7), gives

<a id="equation-fct8"></a>

\[
\begin{aligned}
 k\phi_n(p)&\le a_n\sum_i\phi_n(p_i)=a_nz
 =a_n\sum_i\phi_m(p_i)\\
 &\le ka_na_m\phi_m(p)\le ka_m^2\phi_m(p).
\end{aligned}
 \tag{FCT8}
\]
The last comparison uses \(\phi_m(p_i)\le a_m\phi_m(p)\). Thus \(D_{mn}=a_m^2\phi_m-\phi_n\) is nonnegative on tiles. Normality and finite partial sums extend the inequality to every projection. Bounded Borel spectral step approximation, supplied by SF's SB4–6, extends it to every positive element; boundedness permits the norm limit. Hence \(D_{mn}\) is a positive map, with \(D_{mn}(1)=(a_m^2-1)1\). By (FCT3),

<a id="equation-fct9"></a>

\[
 \|D_{mn}\|=a_m^2-1,\qquad
 \|\phi_m-\phi_n\|\le2(a_m^2-1).
 \tag{FCT9}
\]
The maps are norm Cauchy. Completeness of \(Z\), applied at each \(x\) and then to the uniform operator bound, gives a norm limit \(T:M\to Z\). Positivity, normalization and the center-module identities pass to it. For \(\omega\in Z_*\),

<a id="equation-fct10"></a>

\[
 \|\omega\circ T-\omega\circ\phi_n\|
 \le\|\omega\|\|T-\phi_n\|\longrightarrow0.
 \tag{FCT10}
\]
The terms belong to \(M_*\), whose norm closedness was proved in CP6. Thus \(T\) is ultraweakly continuous on its entire domain.

Taking limits in (FCT7) and interchanging \(x,x^*\) gives \(T(xx^*)=T(x^*x)\). For positive \(b\) and a unitary \(u\), apply this to \(ub^{1/2}\); it gives \(T(ubu^*)=T(b)\). Linearity gives that identity for every \(b\in M\), and replacing \(b\) by \(xu\) gives \(T(ux)=T(xu)\). Every element is a linear combination of four unitaries: split it into real and imaginary self-adjoint parts, scale each nonzero part to a contraction \(h\), and write

<a id="equation-fct11"></a>

\[
 h=\tfrac12(u+u^*),\qquad
 u=h+i(1-h^2)^{1/2}.
 \tag{FCT11}
\]
CF6–7 verify that \(u\) is unitary. Consequently \(T(xy)=T(yx)\) for all \(x,y\). The tiling premise and the approximate states used in this conditional stability lemma are proved next, before it is applied to establish existence.

<a id="fct-2"></a>

<a id="oa-flow.fct.2"></a>

## FCT2. Finite cancellation and unitary completion

Suppose \(p\sim q\) in the finite algebra, with prescribed partial isometry \(v\) from \(p\) to \(q\). PC2 compares their complements centrally: on a central piece \(z\), there is a partial isometry from \(z(1-p)\) to a subprojection of \(z(1-q)\). Add it to \(zv\). Orthogonality of the initial and final projections makes the sum an isometry in \(zM\). Since \(z\) is finite, its final projection is all of \(z\). Therefore that complement subequivalence is an equivalence. On \(1-z\) reverse the roles and repeat. PC1 adds the two complement equivalences, proving

<a id="equation-fct12"></a>

\[
 p\sim q\quad\Longrightarrow\quad1-p\sim1-q.
 \tag{FCT12}
\]
Adding the complementary partial isometry to the originally prescribed \(v\) extends \(v\) to a unitary. This works in every finite corner.

We need the version for different equivalent finite units. If \(e\sim f\), \(a\le e\), \(b\le f\), and \(a\sim b\), first transport \(b\) to \(eMe\) through an implementing equivalence between \(e,f\). Apply (FCT12) to the resulting two projections in that corner, then transport back. It gives \(e-a\sim f-b\). No trace is used.

A finite algebra contains no infinite orthogonal family of copies of one nonzero projection. Otherwise choose distinct copies \(p_0,p_1,\ldots\), and partial isometries from \(p_n\) onto \(p_{n+1}\). Their PC1 strong-star sum has initial projection \(P=\sum_{n\ge0}p_n\) and final projection \(P-p_0<P\). This contradicts finiteness of the subprojection \(P\).

<a id="fct-3"></a>

<a id="oa-flow.fct.3"></a>

## FCT3. Central tiles without a type-I classification

First split off the part generated by abelian projections. A projection \(e\) is abelian if \(eMe\) is commutative. Let \(z_a\) be the join in \(Z\) of the central supports of all such projections. If a nonzero projection \(p\le z_a\) had no nonzero abelian subprojection, it would have no polar bridge to any abelian projection: a nonzero bridge gives a subprojection of \(p\) equivalent to a subprojection of an abelian corner. Equivalence identifies those smaller corners, so the former is abelian. PC2 would then make \(c(p)\) orthogonal to every central support in that join, a contradiction. Thus every nonzero \(p\le z_a\) contains a nonzero abelian \(e\).

Fix such \(e\), and work on \(z=c(e)\). By PC4, every subprojection of \(e\) is \(ew\) for a central projection \(w\le z\), since \(eMe=Z(eMe)=Ze\). Construct orthogonal projections \(e_1,e_2,\ldots\) with \(e_1=e\). Set \(z_1=z\) and, after choosing \(e_1,\ldots,e_n\), put

<a id="equation-fct13"></a>

\[
 r_n=z-\sum_{j\le n}e_j,\qquad z_{n+1}=c(r_n).
 \tag{FCT13}
\]
We can choose \(e_{n+1}\le r_n\) equivalent to \(ez_{n+1}\); if the residual is zero all later terms are zero. To see this, compare \(ez_{n+1}\) and \(r_n\). On a central piece where \(r_n\precsim ez_{n+1}\), its final subprojection of that abelian projection is \(ew\). Its central support is the full comparison piece, because \(c(r_n)=z_{n+1}\). Thus \(w\) is that piece and the subequivalence is an equivalence. On the other comparison piece \(ez_{n+1}\precsim r_n\) directly. Add the two implementations. This proves the asserted choice.

The \(z_n\) decrease. If \(z_\infty=\bigwedge_nz_n\ne0\), the orthogonal \(e_nz_\infty\) would all be equivalent to the nonzero \(ez_\infty\), contradicting FCT2. Thus \(z_\infty=0\). The central projections \(w_n=z_n-z_{n+1}\) sum to \(z\). On \(w_n\), exactly the first \(n\) constructed projections fill the unit:

<a id="equation-fct14"></a>

\[
 w_n=\sum_{j=1}^n e_jw_n,\qquad e_jw_n\sim ew_n.
 \tag{FCT14}
\]
The equality follows because \(r_nw_n=0\), and the equivalences because \(w_n\le z_j\) for \(j\le n\). Every nonzero \(ew_n\) is therefore a central tile, and at least one is nonzero. This is an explicit finite homogeneous matrix-family construction; no classification theorem is hidden in it.

On \(M(1-z_a)\) there is no nonzero abelian projection. Every nonzero corner there contains two nonzero orthogonal equivalent projections. Indeed its algebra is not commutative. If all its projections were central, bounded spectral step approximation would make every self-adjoint element central and hence the algebra commutative. Take a noncentral projection \(r\); some off-diagonal corner \(rx(1-r)\), or its adjoint, is nonzero. PC1 polar decomposition gives the required orthogonal equivalent subprojections.

Choose a maximal family of such pairs in any nonzero central unit \(z\le1-z_a\), with all projections mutually orthogonal. A nonzero residual corner would contain another pair. Hence their sums are equivalent complementary halves of \(z\). Repeat in one half and transport its division to the other half. Induction gives, for every \(n\), a division of \(z\) into \(2^n\) orthogonal equivalent projections \(d_{n,j}\), with \(d_{n,0}\) decreasing and

<a id="equation-fct15"></a>

\[
 d_{n,0}=d_{n+1,0}+d_{n+1,1}.
 \tag{FCT15}
\]
All their central supports are \(z\), since equivalent projections whose sum is central have that common support.

For a nonzero \(p\) in this part, work on \(z=c(p)\) and make these dyadic divisions there. Compare \(d_{n,0}\) with \(p\). If on some nonzero central piece \(w\) one has \(wd_{n,0}\precsim wp\), transport that tile to a subprojection of \(p\). FCT2 extends the transport to a unitary in \(Mw\), so conjugating the whole finite division exhibits the transported projection as a central tile. If this never occurs, central comparison gives \(p\precsim d_{n,0}\) for every \(n\). The projections \(d_{n+1,1}=d_{n,0}-d_{n+1,0}\) are mutually orthogonal and equivalent to \(d_{n+1,0}\). Thus each contains a copy of the same \(p\), contradicting FCT2.

Every nonzero projection in \(M\) now has a nonzero central-tile subprojection: cut it first by \(z_a\) or \(1-z_a\), and use the appropriate construction. A maximal orthogonal family of such tiles below any \(p\) must fill \(p\), because otherwise the residual supplies another tile. This proves exactly the tiling premise of FCT1, with arbitrary orthogonal index sets.

<a id="fct-4"></a>

<a id="oa-flow.fct.4"></a>

## FCT4. Normal center-valued states from cyclic central compressions

We first prove a cyclic abelian fact. If an abelian von Neumann algebra \(A\subseteq B(K)\) has cyclic vector \(\xi\), then \(A'=A\). Let \(R\in A'\) and \(C=\|R\|>0\). Choose \(a_n\in A\) with \(a_n\xi\to R\xi\). Put

<a id="equation-fct16"></a>

\[
 r_n=1_{(2C,\infty)}(|a_n|),\qquad b_n=a_n(1-r_n).
 \tag{FCT16}
\]
CF6 constructs \(|a_n|\); SB4–6 puts its bounded Borel projections in \(A\). Since \(R\) commutes with \(r_n\),

<a id="equation-fct17"></a>

\[
\begin{aligned}
 \tfrac12\|a_nr_n\xi\|
 &\le\|a_nr_n\xi\|-C\|r_n\xi\|\\
 &\le\|r_n(a_n-R)\xi\|
 \le\|(a_n-R)\xi\|.
\end{aligned}
 \tag{FCT17}
\]
The first inequality uses the spectral bound \(|a_n|\ge2C\) on \(r_n\). We have \(\|b_n\|\le2C\) and \(b_n\xi\to R\xi\). For \(a\in A\), commutation gives \(b_na\xi\to Ra\xi\). The common norm bound extends strong convergence from the dense set \(A\xi\) to every vector in \(K\). Strong closedness yields \(R\in A\). The zero operator needs no truncation. The approximation sequence concerns one vector; it does not assume that \(K\) is separable.

Apply PC7's vector-support construction to the concrete algebra \(Z\). The support of \(\omega_\xi|_Z\) is the projection onto \(\overline{Z'\xi}\), belongs to \(Z\), fixes \(\xi\), and makes the restricted vector functional faithful on that central corner. Choose a maximal orthogonal family of nonzero such central supports \(z_i\), with vectors \(\xi_i\in z_iH\). Their join is one: a nonzero remaining central corner contains a vector with a nonzero support below it.

Let \(K_i=\overline{Z\xi_i}\), and let \(q_i\) project onto \(K_i\). This subspace reduces \(Z\), so \(q_i\in Z'\) and \(q_i\le z_i\). The compression

<a id="equation-fct18"></a>

\[
 \theta_i:Zz_i\longrightarrow B(K_i),\qquad \theta_i(z)=z|_{K_i}
 \tag{FCT18}
\]
is a unital normal representation: its vector-series tests are restrictions of the ambient tests. It is faithful because \(\theta_i(z)=0\) gives \(\|z\xi_i\|^2=0\), and the support construction makes the functional faithful on \(Zz_i\). ST2 therefore proves that its image is a von Neumann algebra and its inverse on that image is normal on the entire domain.

For \(x\in M\), the compressed operator \((q_ixq_i)|_{K_i}\) commutes with \(\theta_i(Zz_i)\), since both \(x\) and \(q_i\) commute with \(Z\). Its commutant equals that cyclic abelian algebra by the proof above. Consequently

<a id="equation-fct19"></a>

\[
 E_i(x)=\theta_i^{-1}((q_ixq_i)|_{K_i})\in Zz_i
 \tag{FCT19}
\]
is well defined, positive and normal; \(E_i(1)=z_i\) and \(E_i(zx)=zE_i(x)\). FCT0 gives \(\|E_i\|=1\). The bounded central diagonal sum

<a id="equation-fct20"></a>

\[
 E(x)=\sum_i E_i(x)
 \tag{FCT20}
\]
exists strongly by PC1, since the summands have orthogonal central supports and norm at most \(\|x\|\). It is a unital positive linear center-module map.

Its full normality needs an arbitrary-index check. If \(\omega\in Z_*^+\), then \(\sum_i\omega(z_i)=\omega(1)\): finite sums of the projections increase strongly to one and CP's tail estimate applies. Only countably many of these values are nonzero, since at most finitely many exceed \(1/n\). Each positive normal \(\omega\circ E_i\) has norm \(\omega(z_i)\), by FCT0. Their sum therefore converges in norm in \(M_*\), and evaluation of the bounded central sum shows that it is \(\omega\circ E\). Formula (FCT5) proves the same assertion for all \(\omega\in Z_*\). Hence \(E\) is normal, without sigma-finiteness or a direct integral of \(M\).

<a id="fct-5"></a>

<a id="oa-flow.fct.5"></a>

## FCT5. A corner with arbitrarily small trace distortion

Fix the normal center-valued state \(E\) and a number \(a>1\). We construct a nonzero projection \(p\) with \(E(p)\ne0\) such that

<a id="equation-fct21"></a>

\[
 E(xx^*)\le aE(x^*x)\quad(x\in pMp).
 \tag{FCT21}
\]
In central inequalities, a positive element with support \(z\) is positive on its whole central support; this does not assert a uniform positive lower bound.

First choose a maximal orthogonal family of nonzero projections with zero \(E\)-value. Its sum \(q\) has \(E(q)=0\) by normality. Set \(r=1-q\); then \(E(r)=1\), and \(E\) is faithful on \(rMr\). Indeed a nonzero positive \(b\in rMr\) with zero value has a nonzero spectral projection \(e=1_{[\delta,\infty)}(b)\), and \(0\le\delta E(e)\le E(b)=0\), contradicting maximality. For \(e\le r\),

<a id="equation-fct22"></a>

\[
 s_Z(E(e))=c_M(e).
 \tag{FCT22}
\]
One inclusion follows from the center-module identity. Conversely \(zE(e)=0\) implies \(E(ze)=0\), hence \(ze=0\) by faithfulness. This proves the reverse inclusion.

Inside \(r\), choose a maximal family of pairs \((e_i,f_i)\) with separately orthogonal initial and final families, \(e_i\sim f_i\ne0\), and

<a id="equation-fct23"></a>

\[
 E(e_i)-E(f_i)\ge0,\qquad
 s_Z(E(e_i)-E(f_i))=c(e_i)=c(f_i).
 \tag{FCT23}
\]
Chain unions supply the maximal family. Its partial-isometry sum gives \(\sum_i e_i\sim\sum_i f_i\). Put \(e=r-\sum_i e_i\) and \(f=r-\sum_i f_i\). FCT2 gives \(e\sim f\). They are nonzero: for an empty family both equal \(r\); otherwise normality gives \(E(f)-E(e)=\sum_i(E(e_i)-E(f_i))\ge0\), with at least one nonzero positive summand. Thus \(f\ne0\), and equivalence gives \(e\ne0\).

For equivalent \(e'\le e\), \(f'\le f\), maximality forces \(E(e')\le E(f')\). If not, cut both projections by the nonzero central positive spectral support of \(E(e')-E(f')\). On this cut the difference is positive with full central support; (FCT22) and equivalence ensure nonzero matching projections. That pair would extend the family, a contradiction.

Let \(\mu\) be the infimum of the scalars \(c\in[0,1]\) such that \(E(e')\le cE(f')\) for all these equivalent pairs. The set contains one and is closed, because the positive cone is norm closed. A decreasing sequence of admissible scalars tending to its infimum proves that \(\mu\) itself is admissible. It is positive: the pair \(e,f\) and \(E(e)\ne0\) exclude zero.

Since \(\mu/a<\mu\) is not admissible, there is a matching pair \(\widetilde e\le e,\ \widetilde f\le f\) for which \(aE(\widetilde e)\not\le\mu E(\widetilde f)\). Cut by the nonzero positive central spectral support of that difference. Relabel the cuts; then they are still equivalent and

<a id="equation-fct24"></a>

\[
 D=aE(\widetilde e)-\mu E(\widetilde f)\ge0,
 \qquad D\ne0.
 \tag{FCT24}
\]
The first matching-family bound also holds on these central cuts, since it holds for every pair below \(e,f\).

Choose a second maximal separately orthogonal matching family \((\widehat e_j,\widehat f_j)\) below \(\widetilde e,\widetilde f\) satisfying

<a id="equation-fct25"></a>

\[
 aE(\widehat e_j)\le\mu E(\widehat f_j).
 \tag{FCT25}
\]
Let \(p=\widetilde e-\sum_j\widehat e_j\) and \(q=\widetilde f-\sum_j\widehat f_j\). FCT2 gives \(p\sim q\). They are nonzero: if \(p=0\), equivalence gives \(q=0\); normal summation of (FCT25) would contradict (FCT24). Also \(E(p)\ne0\), since \(p\le r\).

For every matching pair \(p'\le p,q'\le q\), we have \(aE(p')\ge\mu E(q')\). A nonzero negative central spectral part of their difference would cut out a new pair satisfying (FCT25). The cut is nonzero by (FCT22) and preservation of central support, so maximality rules it out. For equivalent \(p_1,p_2\le p\), transport \(p_1\) through a fixed equivalence \(p\sim q\), obtaining \(q'\le q\) equivalent to both. Therefore

<a id="equation-fct26"></a>

\[
 E(p_1)\le\mu E(q')\le aE(p_2).
 \tag{FCT26}
\]
The factor \(\mu\) is present in both comparisons.

If \(b\in(pMp)_+\) and \(u\) is a unitary of that corner, approximate \(b\) in norm by finite nonnegative combinations of its spectral projections. Each projection and its \(u\)-conjugate are equivalent below \(p\). Applying (FCT26) term by term and taking the norm limit gives \(E(ubu^*)\le aE(b)\). For \(x\in pMp\), PC1 polar decomposition and FCT2 extend its partial isometry to a corner unitary \(u\), with \(xx^*=u(x^*x)u^*\). This proves (FCT21) on the full corner, including noninvertible \(x\).

<a id="fct-6"></a>

<a id="oa-flow.fct.6"></a>

## FCT6. Moving the corner estimate to the whole algebra

Use FCT3 to choose a nonzero central tile \(p_1\le p\), with equivalent orthogonal \(p_1,\ldots,p_k\) filling a central unit \(z_0\). It still satisfies (FCT21) on its corner, and \(E(p_1)\ne0\) by faithfulness on \(r\). Choose partial isometries

<a id="equation-fct27"></a>

\[
 v_i^*v_i=p_i,\qquad v_iv_i^*=p_1,
 \qquad F(x)=\sum_{i=1}^kE(v_ixv_i^*)\quad(x\in Mz_0).
 \tag{FCT27}
\]
This finite sum is a normal positive center-module map. For \(x\in Mz_0\), all \(v_ixv_j^*\) belong to \(p_1Mp_1\). Thus the entire matrix calculation is

<a id="equation-fct28"></a>

\[
\begin{aligned}
 F(xx^*)&=\sum_{i,j}E((v_ixv_j^*)(v_ixv_j^*)^*)\\
 &\le a\sum_{i,j}E((v_ixv_j^*)^*(v_ixv_j^*))\\
 &=a\sum_{i,j}E(v_jx^*p_ixv_j^*)
 =aF(x^*x).
\end{aligned}
 \tag{FCT28}
\]
Both resolutions of the identity are the actual finite sums \(\sum_i p_i=z_0\). Also \(F(z_0)=kE(p_1)\), a nonzero central positive element supported on \(z_0\), by (FCT22).

Choose \(\delta>0\) with \(w=1_{[\delta,\infty)}(F(z_0))\ne0\). On \(w\), the central inverse \(h=(F(z_0)|_w)^{-1}\) is bounded and positive by SB4–6; it is extended by zero outside \(w\). Define

<a id="equation-fct29"></a>

\[
 \phi_w(x)=hF(x),\qquad x\in Mw.
 \tag{FCT29}
\]
It is normal and positive, is a \(Zw\)-module map, has \(\phi_w(w)=w\), and satisfies \(\phi_w(xx^*)\le a\phi_w(x^*x)\). Normality of multiplication by \(h\) follows from the vector-series substitution in FCT0. Its norm is one by (FCT3). No unbounded inverse is multiplied into a normal map.

This construction works inside every nonzero central corner of \(M\), with the same prescribed \(a>1\). Choose a maximal orthogonal family of central projections \(w_j\) carrying these maps. A nonzero remaining central corner would supply another, so \(\sum_jw_j=1\). Define

<a id="equation-fct30"></a>

\[
 \phi_a(x)=\sum_j\phi_{w_j}(w_jx).
 \tag{FCT30}
\]
The diagonal sum exists with norm bound \(\|x\|\), by PC1. It is unital, positive and a center-module map; the distortion estimate holds on each orthogonal central component and hence globally. Its full ultraweak normality follows by the FCT4 summable-predual argument: for \(\omega\in Z_*^+\) each summand has functional norm \(\omega(w_j)\), whose total is \(\omega(1)\); use (FCT5) for general \(\omega\). This proves the normality of the whole assembly, for arbitrary index sets.

Choose, for example, \(a_n=1+2^{-n}\). FCT3 and FCT6 now verify both premises of the conditional stability lemma FCT1. It gives the normalized normal center-valued trace \(T\) in (FCT1).

<a id="fct-7"></a>

<a id="oa-flow.fct.7"></a>

## FCT7. Faithfulness, uniqueness and projection comparison

For every central tile in (FCT6), traciality and normalization give

<a id="equation-fct31"></a>

\[
 T(p)=z/k.
 \tag{FCT31}
\]
A nonzero projection \(q\) contains a nonzero tile \(p\), so \(T(q)\ge T(p)>0\). If \(x\ge0\) is nonzero, some positive spectral cutoff \(q=1_{[\delta,\infty)}(x)\) is nonzero; the squared-integral spectral identity would otherwise make \(x=0\). Then \(T(x)\ge\delta T(q)>0\). Thus \(T\) is faithful on the entire positive cone, and \(T(x^*x)=0\) implies \(x=0\).

Any other **normal** normalized center-valued trace has the same value (FCT31) on every central tile. FCT3 decomposes each projection into tiles, and normality identifies its value with their arbitrary positive sum. Therefore the two traces agree on all projections. Uniform spectral step approximation and boundedness then give equality on all self-adjoint elements and hence all of \(M\). This is uniqueness among normal traces; it does not assume or assert normality of an arbitrary algebraic trace.

For projections, the full order criterion is

<a id="equation-fct32"></a>

\[
 p\precsim q\ \Longleftrightarrow\ T(p)\le T(q),
 \qquad p\sim q\ \Longleftrightarrow\ T(p)=T(q).
 \tag{FCT32}
\]
The forward implication uses the implementing partial isometry and positivity. Conversely PC2 splits centrally into \(zp\precsim zq\) and \((1-z)q\precsim(1-z)p\). On the second piece, place a copy of \((1-z)q\) under \((1-z)p\). The positive residual has nonnegative trace, whereas \(T(p)\le T(q)\) makes its trace nonpositive. Faithfulness makes that residual zero, so the reverse subequivalence there is an equivalence. Add the two central implementations to get \(p\precsim q\). Equality of traces gives both subequivalences; PC3 gives equivalence. This proof includes zero projections.

The support identity is \(s_Z(T(p))=c(p)\): \(T(p)\) is supported on \(c(p)\); a central \(z\) annihilating \(T(p)\) gives \(T(zp)=0\), hence \(zp=0\) by faithfulness.

The converse existence assertion is also precise. If an arbitrary von Neumann algebra has a normal normalized center-valued trace, it is finite. Otherwise PC5 supplies a nonzero properly infinite central unit \(z\), split as \(z=r+s\) with \(r\sim s\sim z\). The trace law gives \(T(r)=T(s)=T(z)=z\), while additivity gives \(T(z)=2z\), a contradiction. After finiteness is established, the preceding construction and normal uniqueness prove that any such trace is faithful. No scalar-trace existence theorem was used to prove this implication.



## Free method comparison

Jesse Peterson's [author-hosted *Notes on operator algebras*](https://math.vanderbilt.edu/peters10/teaching/spring2020/OperatorAlgebras.pdf), 27April2020, Section6.4, printed/PDF102–106, develops the approximate center-valued states and their norm-limit trace. FCT retains and credits that mathematical route. Its characterwise bound proves the norm of a positive central map for complex inputs; its explicit central tiles, cyclic compressions and summable preduals supply the type and arbitrary-assembly steps that the source method requires. Both occurrences of the balancing constant are retained.

The human source remains freely readable on its author's university page. Its text and PDF are not reproduced here or assigned the programme's licence. The complete programme comparison, bounded spectral calculus, predual and normal-range arguments are the actual earlier proof inputs.
