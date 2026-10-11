# Positive equivalence and atomic expectations

Two positive operators can be assembled from the same family of operators, using initial squares on one side and final squares on the other. This relation has a useful refinement property. It compares arbitrary positive elements, agrees with partial-isometry equivalence on projections, and retains cardinal information that a trace can lose. A separate rank-one argument identifies exactly which algebras admit enough normal expectations from all bounded operators.

Throughout, \(M\subseteq B(H)\) is a unital von Neumann algebra, with arbitrary Hilbert dimension. A sum of positive operators means the strong limit of its finite subsums, when these are bounded. Existence and the quadratic-form description of that limit are proved in bounded increasing nets. Empty sums are zero. We write \(s(h)\) for the support of a positive operator and \(c(h)=c(s(h))\) for its central carrier. The zero algebra satisfies the conclusions with their empty interpretations.

## Factoring a bounded positive sum

For \(h,k\in M_+\), define \(h\approx k\) when there is a family \((x_\alpha)\subset M\) such that
\[
 \begin{gathered}
 h=\sum_\alpha x_\alpha^*x_\alpha,\\
 k=\sum_\alpha x_\alpha x_\alpha^*.
 \end{gathered}
 \tag{PE.1}
\]
This notation is distinct from \(e\sim f\) for Murray–von Neumann equivalence of projections.

We shall repeatedly use the following bounded factorization. If \(a^*a\leq h\), define on \(h^{1/2}H\)
\[
 u(h^{1/2}\xi)=a\xi.
\]
The inequality makes this well defined and contractive. Extend it by continuity to \(s(h)H\), and by zero on its orthogonal complement. Then \(a=uh^{1/2}\) and \(u=us(h)\). Commutation with each unitary in \(M'\) follows first on this range and its kernel, and then by continuity. The bicommutant and unitary tests put \(u\) in \(M\).

In particular, if \(\sum_i a_i^*a_i=h\), choose \(a_i=u_i h^{1/2}\) in this way. For a finite set \(F\), the inequality
\[
 \sum_{i\in F}\|u_i h^{1/2}\xi\|^2
 \leq\|h^{1/2}\xi\|^2
\]
extends to every vector in \(s(h)H\), while all \(u_i\) vanish on its complement. Thus the partial sums of \(u_i^*u_i\) are bounded by \(s(h)\). Their supremum \(d\) satisfies \(h^{1/2}dh^{1/2}=h\). Density of the range of \(h^{1/2}\) in its support, followed by polarization, gives
\[
 \sum_i u_i^*u_i=s(h).
 \tag{PE.2}
\]
No inverse of \(h\) on all of \(H\) has been used.

If (PE.1) holds, the individual bounds imply
\[
 x_\alpha=s(k)x_\alpha s(h).
 \tag{PE.3}
\]
For example, \(x_\alpha^*x_\alpha\leq h\) makes \(x_\alpha\) vanish on \(\ker h\). Apply the same argument to its adjoint for the other equality. Also \(h\approx0\) forces every witness to vanish, hence \(h=0\).

Positive double sums can be interchanged: on each vector both orders give the supremum of all finite rectangular subsums of nonnegative real numbers. Every finite subset of a product lies in a finite rectangle. This observation justifies the regroupings below, including uncountable index sets.

## Equivalence, addition and simultaneous refinement

The relation \(\approx\) is reflexive, using the single witness \(h^{1/2}\), and symmetric, using adjoints. For transitivity, suppose \(h\approx k\) has witnesses \(x_\alpha\), and \(k\approx l\) has witnesses \(y_\beta\). Factor \(y_\beta=v_\beta k^{1/2}\) as in PE01. Then \(\sum_\beta v_\beta^*v_\beta=s(k)\), so the family \(v_\beta x_\alpha\) satisfies
\[
 \begin{gathered}
 \sum_{\alpha,\beta}
 x_\alpha^*v_\beta^*v_\beta x_\alpha=h,\\
 \sum_{\alpha,\beta}
 v_\beta x_\alpha x_\alpha^*v_\beta^*=l.
 \end{gathered}
\]
Here fixed bounded congruences commute with increasing strong limits. Thus \(h\approx l\).

If \(h_i\approx k_i\) and both positive sums are bounded, taking the disjoint union of the witness families proves \(\sum_i h_i\approx\sum_i k_i\). Multiplying each witness by \(\sqrt\lambda\) proves \(\lambda h\approx\lambda k\) for \(\lambda\geq0\). More generally, for \(a\in Z(M)_+\), the witnesses \(a^{1/2}x_\alpha\) prove \(ah\approx ak\). Centrality is used in both products.

Here is the stronger refinement statement we will need. Suppose
\[
 \begin{gathered}
 h=\sum_{i\in I}h_i\approx k,\\
 k=\sum_{j\in J}k_j.
 \end{gathered}
 \tag{PE.4}
\]
There are positive elements \(h_{ij},k_{ij}\) such that
\[
 \begin{gathered}
 h_i=\sum_jh_{ij},\\
 k_j=\sum_i k_{ij},\\
 h_{ij}\approx k_{ij}.
 \end{gathered}
 \tag{PE.5}
\]
To prove this, factor \(h_i^{1/2}=u_i h^{1/2}\) and \(k_j^{1/2}=v_j k^{1/2}\) by PE01, and let \(x_\alpha\) witness \(h\approx k\). Put
\[
 \begin{gathered}
 w_{ij\alpha}=v_jx_\alpha u_i^*,\\
 h_{ij}=\sum_\alpha w_{ij\alpha}^*w_{ij\alpha},\\
 k_{ij}=\sum_\alpha w_{ij\alpha}w_{ij\alpha}^*.
 \end{gathered}
 \tag{PE.6}
\]
All these sums are bounded: summing the first over \(j,\alpha\) gives
\(u_i h u_i^*=h_i\), by (PE.2)–(PE.3), and summing the second over \(i,\alpha\) gives \(v_jkv_j^*=k_j\). These computations also prove (PE.5). Taking a one-element family on the left shows in particular that \(h\approx\sum_j k_j\) can be split as \(h=\sum_jh_j\) with \(h_j\approx k_j\).

## Matching remainders and central comparison

If \(hMk\ne\{0\}\), there are nonzero equivalent positive pieces below \(h\) and \(k\). Indeed some \(k^{1/2}a h^{1/2}\) is nonzero: otherwise \(kMh=0\), and taking adjoints would give \(hMk=0\). Choose \(t>0\) small enough that, for
\(x=t k^{1/2}a h^{1/2}\),
\[
 x^*x\leq h,\qquad xx^*\leq k.
\]
The estimates \(a^*ka\leq\|a\|^2\|k\|1\) and \(aha^*\leq\|a\|^2\|h\|1\) supply such a \(t\). These two pieces are nonzero and equivalent by the single witness \(x\).

We recall the carrier test with its mechanism. For a projection \(e\), the projection onto \([MeH]\) commutes with both \(M\) and \(M'\), and is its least central majorant. This is \(c(e)\), as in central carriers. If \(eMf=0\), the subspaces \([MeH]\) and \([MfH]\) are orthogonal, so \(c(e)c(f)=0\). Conversely that central orthogonality plainly gives \(eMf=0\). The same test holds for positive \(h,k\): bounded resolvent cutoffs \(h(h+\varepsilon)^{-1}\uparrow s(h)\) and the corresponding cutoffs for \(k\) turn \(hMk=0\) into \(s(h)Ms(k)=0\).

Choose a maximal family of nonzero witnesses whose finite sums of initial squares are at most \(h\) and whose finite sums of final squares are at most \(k\). Here is a precise use of Zorn's lemma that allows repeated witnesses. Order admissible subsets of \((M\setminus\{0\})\times\mathbb N\) by inclusion, using the first coordinate as the witness. A chain union remains admissible. Any particular nonzero operator occurs only finitely many times, since \(n x^*x\leq h\) would imply \(n\|x\|^2\leq\|h\|\). Thus an additional nonzero witness can always receive an unused label.

Let \(h_0,k_0\) be the two sums of a maximal family and put \(r=h-h_0\), \(s=k-k_0\). The first paragraph would enlarge the family if \(rMs\ne0\). Therefore \(c(r)c(s)=0\). For \(z=1-c(r)\), we have \(zr=0\) and \((1-z)s=0\). Central multiplication and addition from PE02 now give
\[
 \begin{gathered}
 zh=zh_0\\
 \approx zk_0\leq zk,\\
 (1-z)k=\\
 (1-z)k_0\\
 \approx(1-z)h_0\\
 \leq(1-z)h.
 \end{gathered}
 \tag{PE.7}
\]
This is comparison for arbitrary bounded positive elements, with no trace or countability hypothesis.

The witnesses also show that \(h\approx k\) implies \(c(h)=c(k)\). A central projection annihilates \(h\) exactly when it annihilates every witness, exactly when it annihilates \(k\).

## When the center-valued trace determines equivalence

Let \(M\) be semifinite and let \(T\) be a faithful normal semifinite extended center-valued trace. Its construction and conventions are in extended center-valued traces. Normality, additivity and the trace identity applied to (PE.1) show
\[
 \begin{gathered}
 h\approx k\\
 \Longrightarrow\\
 T(h)=T(k).
 \end{gathered}
 \tag{PE.8}
\]

Conversely suppose \(T(h)=T(k)=H_0\) and this central extended positive has no infinite part. Equivalently, its value is finite on an open dense subset of the central spectrum, by the resolvent description. Take the central comparison (PE.7). Write \(zh\approx b\leq zk\). Then \(T(b)=zH_0=T(zk)\). The central spectral cutoffs
\(q_n=1_{[0,n]}(H_0)\uparrow1\)
give bounded central values. Additivity on this bounded part permits subtraction and yields
\[
 T\bigl(q_n(zk-b)\bigr)=0.
\]
Faithfulness gives \(q_n(zk-b)=0\), and taking the strong limit gives \(b=zk\). The identical argument on \(1-z\) turns the other comparison into equivalence as well. Adding the two central pieces proves \(h\approx k\). No subtraction of infinite values occurs.

Consequently, if either \(T(h)\) or \(T(k)\) is finite on an open dense set, equality of their traces is equivalent to \(h\approx k\).

When \(M\) is finite, let \(T_0:M\to Z(M)\) be its canonical normalized trace, constructed in central traces. It is bounded and fixes the center, so \(T_0(T_0(h))=T_0(h)\). Apply the result just proved to this finite-valued trace:
\[
 \begin{gathered}
 h\approx T_0(h),\\
 h\in M_+.
 \end{gathered}
 \tag{PE.9}
\]

## Countability belongs to the support

Call a positive element \(h\) sigma-finite if every decomposition of \(h\) as a sum of nonzero positive elements has at most countably many terms. A projection is sigma-finite in the usual sense when its corner has no uncountable orthogonal family of nonzero projections. The countable detection theorem equates that condition with a faithful normal state on a nonzero corner.

We claim that \(h\) is sigma-finite exactly when \(s(h)\) is. For \(h=0\), both conditions hold because neither object has a nonzero positive subelement. Otherwise, if \(p=s(h)\) is sigma-finite, take a faithful normal state \(\varphi\) on \(pMp\). Every positive summand \(h_i\leq h\) is supported in \(p\), so \(\varphi(h_i)>0\) when \(h_i\ne0\). The sums of these numbers are bounded by \(\varphi(h)\). For each positive integer \(n\), only finitely many can exceed \(1/n\); hence there are at most countably many summands.

Conversely, let \((e_i)\) be any orthogonal family of nonzero projections below \(p\). Each \(h^{1/2}e_i h^{1/2}\) is nonzero: if it vanished then \(e_i h^{1/2}=0\), contradicting density of \(h^{1/2}H\) in \(pH\). These elements sum to \(h^{1/2}e h^{1/2}\), where \(e=\sum_i e_i\leq p\). Adding \(h^{1/2}(p-e)h^{1/2}\) when nonzero gives a decomposition of \(h\). Sigma-finiteness of \(h\) makes the original family countable.

Sigma-finiteness is preserved by \(\approx\). Indeed, split \(h\approx k=\sum_jk_j\) using PE02. If every \(k_j\ne0\), its equivalent piece \(h_j\) is nonzero by PE01. A sigma-finite \(h\) therefore forces \(J\) countable. Symmetry proves the converse.

We also need two existence facts. Every nonzero projection contains a nonzero sigma-finite projection: choose \(0\ne\xi\in pH\) and use the projection \(q\) onto \([M'\xi]\). It belongs to \(M\), lies under \(p\), and the vector functional is faithful on \(qMq\), since \(x\xi=0\) implies \(xq=0\); see vector support projections. A maximal orthogonal family of such projections therefore sums to \(p\).

A countable orthogonal sum \(p=\sum_n p_n\) of sigma-finite projections is sigma-finite. Choose normal states \(\varphi_n\) faithful on the nonzero corners and set
\[
 \varphi(x)=\sum_n2^{-n}\varphi_n(p_nxp_n).
\]
The series converges in the predual norm by positive normal functionals. If \(x\geq0\) and \(\varphi(x)=0\), then \(x^{1/2}p_n=0\) for every \(n\), hence \(x=0\) in \(pMp\). Thus \(\varphi\) is faithful; normalizing it and applying countable detection proves the assertion.

## Finite projections

Suppose \(e,f\) are projections, \(e\approx f\), and \(e\) is finite. We prove \(e\sim f\). Their carriers coincide by PE03; write this carrier as \(c\).

The algebra \(Mc\) is semifinite. To see the projection condition, let \(0\ne q\leq c\). Since \(c(q)c(e)\ne0\), the carrier test gives \(qMe\ne0\). The polar decomposition of a nonzero element of this space matches a nonzero subprojection of \(q\) with one of \(e\). The former is finite: subprojections of a finite projection are finite, because an isometry onto a proper subprojection would extend by the identity on the complement to contradict finiteness; equivalence transports the same test. Thus every nonzero \(q\) contains a nonzero finite projection. The semifinite trace-existence theorem applies.

Choose a faithful normal semifinite extended center-valued trace on \(Mc\), using EC03. The finite-projection criterion says that \(T(e)\) has no infinite part. By (PE.8), \(T(f)=T(e)\), so that criterion also makes \(f\) finite.

The earlier projection comparison theorem gives a central cut on which \(e\) is equivalent to a subprojection \(f_0\leq f\), and the reverse comparison on its complement. On the first cut, \(T(f_0)=T(e)=T(f)\). The bounded central cutoff argument of PE04 forces \(f-f_0=0\). On the other cut it forces the opposite remainder to vanish. Add the partial isometries from the two central pieces to obtain \(e\sim f\). By symmetry the argument applies when either projection is finite.

## Sigma-finite projections

We first establish the projection facts used in this step. A projection is properly infinite when none of its nonzero central cuts is finite.

**Central splitting.** Choose a maximal family of orthogonal central projections \(z_i\leq c(e)\) such that \(z_i e\) is nonzero and finite. Their sum \(ze\), where \(z=\sum_i z_i\), is finite: an equivalence of \(ze\) with one of its subprojections restricts on each \(z_i\) to an equivalence of the finite projection \(z_i e\), so the subprojection has every cut \(z_i e\), and hence equals \(ze\). Maximality implies that \((1-z)e\) has no nonzero finite central cut. This is the required finite/properly infinite splitting, including a zero part when appropriate.

**Countable absorption.** The exact earlier halving theorem used in central traces says that a properly infinite algebra's identity contains two orthogonal copies of itself. Apply it to \(pMp\). The corner-center isomorphism identifies its central projections with central cuts of \(p\), so this corner is properly infinite whenever \(p\) is. Repeatedly split one remaining copy to obtain mutually orthogonal \(p_n\leq p\), each equivalent to \(p\). If orthogonal projections \(q_n\) are each subequivalent to \(p\), place a copy of \(q_n\) under \(p_n\). The strong sum of their partial isometries, justified by orthogonality of both initial and final spaces, shows \(\sum_nq_n\precsim p\).

Keep \(p\) properly infinite, and let \(q\) be sigma-finite with \(c(q)\leq c(p)\). A maximal orthogonal family of nonzero subprojections \(q_n\leq q\) subequivalent to \(p\) is at most countable. If its sum left a nonzero remainder \(r\), the carrier test from PE03 would give \(rMp\ne0\). Its polar factor would supply another such subprojection, contradicting maximality. Thus \(q=\sum_nq_n\precsim p\).

**Mutual subequivalence.** We include the cancellation argument for infinite projections. If \(r_2\leq r_1\leq r\) and \(w^*w=r\), \(ww^*=r_2\), let \(d=r-r_1\). The projections \(d_n=w^n d w^{*n}\), for \(n\geq0\), are orthogonal: each lies in the difference of consecutive projections of the decreasing chain \(w^n w^{*n}\), with zeroth term \(r\). Put \(D=\sum_n d_n\). The operator \(wD+(r-D)\) has initial projection \(r\) and final projection \(r-d=r_1\), since it shifts the orthogonal sequence by one and is the identity on its complement. Hence \(r\sim r_1\). If \(r\precsim s\precsim r\), choose copies \(s_1\leq s\) of \(r\) and \(r_1\leq r\) of \(s\). Transport \(s_1\) into \(r_1\) to obtain \(r_2\leq r_1\) equivalent to \(r\). The just-proved assertion gives \(r\sim r_1\sim s\).

It follows that two sigma-finite properly infinite projections with the same carrier are equivalent: the absorption result gives subequivalence in both directions, and the last paragraph gives equivalence.

Now suppose \(e\approx f\) and \(e\) is sigma-finite. PE05 makes \(f\) sigma-finite too. Their carriers coincide. Split each into its finite and properly infinite central parts and refine the two central partitions together. On a piece where either projection is finite, PE06 makes the two projections equivalent. On every remaining nonzero piece both projections are properly infinite, sigma-finite, and have the same central carrier. The preceding consequence applies. Summing over the finitely many central pieces proves
\[
 \begin{gathered}
 e\approx f\\
 \Longrightarrow\\
 e\sim f
 \end{gathered}
 \tag{PE.10}
\]
whenever either projection is sigma-finite. Neither the algebra nor the ambient representation has been assumed sigma-finite.

## Cardinality of decompositions

Suppose \(h=\sum_{i\in I}h_i\approx k=\sum_{j\in J}k_j\), with every \(h_i,k_j\) nonzero and sigma-finite. Use the simultaneous refinement (PE.5). Draw an edge between \(i\) and \(j\) precisely when \(h_{ij}\ne0\), equivalently \(k_{ij}\ne0\). Every vertex has an edge. Each row and each column has at most countably many edges, by sigma-finiteness of its total.

Choose a neighbor \(j(i)\) for every \(i\). For each \(j\), enumerate its at most countable neighbors by distinct natural numbers. These choices define an injection \(I\hookrightarrow J\times\mathbb N\). The symmetric choices give \(J\hookrightarrow I\times\mathbb N\). Taking products with \(\mathbb N\) and using the elementary pairing injection
\((m,n)\mapsto2^m(2n+1)\)
gives mutual injections between \(I\times\mathbb N\) and \(J\times\mathbb N\).

For completeness, mutual injections \(a:A\to B\) and \(b:B\to A\) give a bijection as follows. Put \(A_0=A\setminus b(B)\) and \(A_*=\bigcup_{n\geq0}(ba)^n(A_0)\). Use \(a\) on \(A_*\) and \(b^{-1}\) on its complement. These two images are disjoint: if \(a(x)=b^{-1}(y)\), then \(y=ba(x)\in A_*\). They cover \(B\): if \(t\notin a(A_*)\), then \(b(t)\notin A_*\), since it cannot belong to \(A_0\), and membership in any later stage would force \(t\in a(A_*)\). Thus the stated map is a bijection. Applying this construction proves
\[
 \aleph_0|I|=\aleph_0|J|.
 \tag{PE.11}
\]
If one index set is empty, PE01 forces the other to be empty, and the formula still holds. Excluding zero summands is essential.

## Equivalence of arbitrary projections

Let \(e\approx f\). By PE05 choose orthogonal decompositions \(e=\sum_i e_i\) and \(f=\sum_j f_j\) into nonzero sigma-finite projections. Apply PE02 to obtain \(h_{ij}\approx k_{ij}\), with row sums \(e_i\) and column sums \(f_j\).

The bipartite graph from PE08 is locally countable. Each of its connected components is countable: starting at one vertex, vertices at distance at most \(n+1\) are a countable union of the countable neighbor sets from distance at most \(n\); the union over finite \(n\) is countable. This uses only that a countable product or union of countable sets can be enumerated by finite sequences of natural numbers, using the pairing map above.

For a component \(C\), let \(I_C,J_C\) be its vertices on the two sides, and put
\[
 \begin{gathered}
 e_C=\sum_{i\in I_C}e_i,\\
 f_C=\sum_{j\in J_C}f_j.
 \end{gathered}
\]
They are sigma-finite projections by PE05. All nonzero refinement pieces in these rows or columns belong to this same component. Addition of equivalences therefore gives \(e_C\approx f_C\), hence \(e_C\sim f_C\) by PE07. Choose an implementing partial isometry \(v_C\).

Both the initial projections \(e_C\) and the final projections \(f_C\) are orthogonal as \(C\) varies. The finite sums of \(v_C\) and of \(v_C^*\) converge strongly: the squared norm of each tail on a fixed vector is the corresponding sum of orthogonal projection energies. Their strong limits \(v,v^*\) belong to \(M\), and give \(v^*v=e\), \(vv^*=f\). Conversely, a partial isometry itself is a one-element witness in (PE.1). We have proved, at arbitrary cardinality,
\[
 \begin{gathered}
 e\approx f\\
 \Longleftrightarrow\\
 e\sim f.
 \end{gathered}
 \tag{PE.12}
\]

## Rank-one tests force atomicity

Call \(M\) atomic if every nonzero projection of \(M\) contains a minimal projection. A family \(\mathscr E\) of positive maps \(E:B(H)\to M\) is sufficiently many here if it separates positive operators: \(x\geq0\) and \(E(x)=0\) for every \(E\in\mathscr E\) imply \(x=0\). We require each map to be normal and to satisfy
\[
 E(axb)=aE(x)b
 \tag{PE.13}
\]
for \(a,b\in M\) and \(x\in B(H)\). The maps constructed in PE11 will also be unital and onto.

Let \(z\) be the join of all minimal projections in \(M\). Unitary conjugation permutes these projections, so \(z\) commutes with every unitary in \(M\), hence is central by the unitary test. The algebra \(M\) is atomic exactly when \(z=1\). Indeed, if \(z=1\) and \(q\ne0\), some minimal \(p\) satisfies \(qp\ne0\); otherwise \(q\) would annihilate the closed span of their ranges. Polar decomposition of \(qp\) gives a nonzero projection under \(q\) equivalent to \(p\), which is minimal. The converse follows by applying atomicity to \(1-z\).

Fix one positive normal bimodule map \(E\) and a vector \(\xi\). Let \(r_\xi\) be the rank-one positive operator \(\eta\mapsto\langle\eta,\xi\rangle\xi\), using inner products linear in the first variable. Put \(b=E(r_\xi)\), \(C=\|E(1)\|\), and \(p=1_{[\varepsilon,\infty)}(b)\), where \(\varepsilon>0\). For any nonzero projection \(q\leq p\), bimodularity and positivity give
\[
 \begin{gathered}
 \varepsilon q\leq qbq\\
 =E(r_{q\xi}),\\
 E(r_{q\xi})\\
 \leq\|q\xi\|^2E(1),\\
 \varepsilon\leq C\|q\xi\|^2.
 \end{gathered}
 \tag{PE.14}
\]
Thus an orthogonal family of nonzero subprojections of \(p\) has at most \(C\|\xi\|^2/\varepsilon\) members. This bound forces \(p\) to be a finite sum of minimal projections. Start with \(p\), if nonzero, and split any nonminimal member into two nonzero orthogonal projections. Each split increases the number of members, so the bound makes the process terminate. Minimality in the corner is minimality in \(M\). Consequently \(p\leq z\). Taking \(\varepsilon=1/n\) and then the join gives \(b=zb\).

Choose any orthonormal basis of \(H\). Its finite-rank coordinate projections increase to \(1\). Linearity and normality of \(E\) show that \(E(1)\) is supported in \(z\), since every rank-one image is. Hence
\[
 E(1-z)=(1-z)E(1)=0.
\]
If sufficiently many such maps exist, they detect \(1-z\), so \(z=1\) and \(M\) is atomic. This proof did not require surjectivity of the maps. In fact one surjective map already forces atomicity: for every \(0\leq x\leq\|x\|1\), its image is supported in \(z\); linear decomposition into positive parts gives the same conclusion for every image, so surjectivity puts \(1\) in \(Mz\).

## Atomic matrix blocks supply normal expectations

Suppose \(M\) is atomic. A maximal orthogonal family \((p_a)\) of minimal projections sums to \(1\); a nonzero complementary projection would contain another minimal projection. Partition the family into equivalence classes. Distinct classes have zero cross corners: a nonzero \(p_a x p_b\) would have a polar factor matching \(p_b\) with \(p_a\), by minimality. Therefore the sum \(z_i\) of a class commutes with every \(x\in M\), as is seen by its matrix entries against all the \(p_a\). The \(z_i\) are orthogonal central projections with sum \(1\).

Fix one class, choose \(p_0\) in it, and let \(L=p_0H\). For each \(a\) choose \(v_a\in M\) with \(v_a^*v_a=p_0\), \(v_av_a^*=p_a\). The map
\[
 U(\delta_a\otimes\eta)=v_a\eta
 \tag{PE.15}
\]
extends from the algebraic tensor product to a unitary from \(\ell^2(A)\otimes L\) onto \(z_iH\): orthogonality gives its norm identity, and the ranges of the \(p_a\) span that summand. The tensor product is the completion of finite sums with their usual inner product, using the Hilbert completion construction.

The minimal corner \(p_0Mp_0\) equals \(\mathbb Cp_0\). A self-adjoint nonscalar element would have a nontrivial spectral projection, contrary to minimality; real and imaginary parts give the assertion for all elements. Hence \(v_a^*xv_b\) is scalar on \(L\). These scalars form a bounded matrix on \(\ell^2(A)\): test finite vectors tensored with a fixed unit vector of \(L\) to obtain the bound \(\|x\|\). Conversely every bounded scalar matrix is present, since its finite coordinate compressions give finite linear combinations of the matrix units \(v_av_b^*\), and their uniformly bounded strong limit belongs to \(M\). Write \(M_i=B(K_i)\otimes1_{L_i}\) for each block. Thus in the coordinates (PE.15),
\[
 \begin{gathered}
 H=\\
 \bigoplus_i(K_i\otimes L_i),\\
 M=\prod_i M_i.
 \end{gathered}
 \tag{PE.16}
\]
All \(K_i,L_i\) in a nonzero block are nonzero. This also proves the atomic structure in the given representation, without any countability assumption.

Choose a unit vector \(\eta_i\in L_i\) for every block. Write \(V_i:K_i\to K_i\otimes L_i\) for \(V_i\zeta=\zeta\otimes\eta_i\), and define
\[
 \begin{gathered}
 a_i=V_i^*z_i xz_iV_i,\\
 E_\eta(x)=\\
 \bigoplus_i a_i\otimes1_{L_i}.
 \end{gathered}
 \tag{PE.17}
\]
Each coordinate has norm at most \(\|x\|\), so this defines an element of \(M\). Compression proves positivity and unitality. For \(a,b\in M\), write their restrictions to block \(i\) as \(a^{(i)}\otimes1_{L_i}\) and \(b^{(i)}\otimes1_{L_i}\). The equalities \(aV_i=V_i a^{(i)}\) and \(bV_i=V_i b^{(i)}\), also applied to adjoints, give \(V_i^*z_i axb z_iV_i=a^{(i)}(V_i^*z_i xz_iV_i)b^{(i)}\). Hence \(E_\eta(axb)=aE_\eta(x)b\); taking \(x=1\) shows that \(E_\eta\) fixes \(M\), hence is onto and idempotent. For a bounded increasing net \(x_\lambda\uparrow x\), every compressed coordinate increases to the displayed coordinate of \(E_\eta(x)\). Their block sum is the least upper bound in \(M\). Thus \(E_\eta\) is normal by the positive normal-map criterion. These are normal positive projections of norm one when \(H\ne0\).

The family over all choices \(\eta=(\eta_i)\) separates positive operators. If \(x\geq0\) and every \(E_\eta(x)=0\), then
\(\langle x(\zeta\otimes\eta_i),\zeta\otimes\eta_i\rangle=0\)
for every block, every \(\zeta\), and every unit \(\eta_i\). Consequently \(x^{1/2}\) vanishes on all these simple tensors. They span a dense subspace of \(H\), so \(x=0\).

Together with PE10 this characterizes atomic algebras by sufficiently many normal positive onto bimodule maps from \(B(H)\). It proves representation independence as well. A star isomorphism preserves projections, minimality and the statement that every nonzero projection contains a minimal one. In each faithful normal concrete representation of an atomic algebra, the construction above supplies the required family. Thus the property depends only on the algebra, even though the individual maps depend on its representation.

## Five checks on the conclusions

**Equivalence need not be unitary conjugacy.** In \(M_n(\mathbb C)\), the canonical trace is \(T_0(h)=\operatorname{Tr}(h)1/n\), as computed in matrix examples for the central trace. PE04 says that positive elements are equivalent exactly when their scalar traces agree. For \(n>1\), a rank-one projection is equivalent to \(1/n\), although the two have different kernels and cannot be unitarily conjugate. This does not contradict PE09, because \(1/n\) is not a projection.

**The abelian case.** In an abelian algebra every witness satisfies \(x_\alpha^*x_\alpha=x_\alpha x_\alpha^*\). Thus positive equivalence is equality. Reflexivity supplies its converse.

**Infinite traces can lose cardinal information.** In \(B(\ell^2(I))\), for uncountable \(I\), take a projection onto a countably infinite coordinate subspace and compare it with the identity. Both have infinite ordinary trace, since their finite-rank subprojections have arbitrarily large integer trace. The first projection is sigma-finite, the second is not: its uncountable coordinate family violates the defining condition. PE05 therefore rules out positive equivalence. This explains the finite-on-an-open-dense-set condition in PE04.

**Zero summands must be excluded.** Adding arbitrarily many zero terms changes the index cardinality without changing a sum. For instance a fixed nonzero scalar has its one-term decomposition and a decomposition with that same term and uncountably many zeros. The cardinal conclusion (PE.11) would fail for these two lists. With nonzero terms, PE08 applies.

**A separating family need not contain one faithful normal expectation.** Let \(M=\mathbb C1\) on a nonseparable \(H\). The maps \(x\mapsto\langle x\eta,\eta\rangle1\), for unit \(\eta\), form a separating family of normal unital expectations. There is no faithful normal positive functional on \(B(H)\), by the uncountable orthogonal rank-one projections and countable detection. Hence no one normal expectation to \(\mathbb C1\) is faithful. This is why the characterization uses a family in arbitrary representations.

Further reading: Masamichi Takesaki, *Theory of Operator Algebras I*, Chapter V, §2, Exercises 7–8, pp. 334–335. The positive relation, its projection consequences and the normal-expectation characterization are classical.
