# Projection partitions and dominant centralizers



A projection that barely moves one vector can be extended to a partition that removes a definite part of another vector. Finite sign averages then give projections with a uniform displacement bound. We use this to pass from scalar averaging by a dominant centralizer to a trivial bicentralizer. For the reverse direction we construct a dominant weight explicitly and average in three stages.

The earlier inputs are the nonzero projection estimate, MSD06, faithful standard-form corners, SE01–03, functional commutator control, NC21, the bicentralizer definition and compact convex averaging, QA01–02, and the equivalence between trivial bicentralizers and irreducible state centralizers, SCV09. We also use the concrete predual, CP06, projection corners and filling families, PC4–5 and PC8, whole-cone tensor weights, TW2–5, unbounded centralizer densities, CZ2 and CZ5, the dominant reference in type III1, IAP5, and faithful dominant-weight uniqueness, DS5.

Throughout, \(M\) is a type \(\mathrm{III}_1\) factor with separable predual, in standard form \((M,H,J,P)\). Inner products are linear in the first variable, \(\zeta a=Ja^*J\zeta\), and \([a,\zeta]=a\zeta-\zeta a\). Fix a cyclic separating unit vector \(\xi\in P\) and put \(\varphi=\omega_\xi\). A dominant weight is faithful normal semifinite, has properly infinite centralizer, and is unitarily equivalent to every positive scalar multiple. Write

\[
 C_N(x)=\overline{\operatorname{co}}^{\,uw}
       \{u x u^*:u\in\mathcal U(N)\}\qquad(N\subset M).
 \tag{PDC.1}
\]

Sections 1–4 assume the dominant-weight averaging property: for one dominant weight \(\Phi\), every \(C_{M_\Phi}(x)\) meets \(\mathbb C1\). DS5 transports this property to every dominant weight and every normally isomorphic copy of \(M\), as checked in the introduction to MSD. Sections 5–7 prove that property from an irreducible state centralizer.

## A projection estimate depending on the angle

Let \(\eta\) be a \(J\)-real unit vector other than \(\xi\) and \(-\xi\). Its inner product with \(\xi\) is real. Define \(0<\theta<\pi\) by \(\langle\eta,\xi\rangle=\cos\theta\), and write

\[
 \eta=\cos\theta\,\xi+\sin\theta\,\zeta,
 \qquad J\zeta=\zeta,\quad \zeta\perp\xi,\quad\|\zeta\|=1.
\]

For \(0<\delta<1\), apply MSD06 to \(\xi,\zeta\) with tolerance \(\delta_1=\delta\sin^2\theta/4\). Its nonzero projection \(q\) satisfies

\[
 \|q\xi\|^2+\|q\zeta\|^2<128\|[q,\zeta]\|^2,
 \qquad \|[q,\xi]\|^2<\delta_1\|[q,\zeta]\|^2.
\]

The target commutator is nonzero, since the first inequality is strict. The triangle inequality gives

\[
 \|[q,\eta]\|\ge
   \sin\theta\|[q,\zeta]\|-|\cos\theta|\|[q,\xi]\|
   >\tfrac12\sin\theta\|[q,\zeta]\|.
\]

Cauchy–Schwarz applied to \(q\eta=\cos\theta\,q\xi+\sin\theta\,q\zeta\) yields \(\|q\eta\|^2\le\|q\xi\|^2+\|q\zeta\|^2\). Therefore

\[
 \boxed{\quad
 \|q\xi\|^2+\|q\eta\|^2
    <\frac{1024}{\sin^2\theta}\|[q,\eta]\|^2,
 \qquad \|[q,\xi]\|^2<\delta\|[q,\eta]\|^2.
 \quad}\tag{PDC.2}
\]

Both inequalities retain their force when the angle is close to either endpoint; the first constant records the resulting loss.

## Refining a partition and counting its energy

Now assume \(J\eta=\eta\), \(\eta\perp\xi\), and \(\|\eta\|=1\). We will construct a finite or countable partition \((e_i)\) of the identity such that

\[
 \left\|\xi-\sum_i e_i\xi e_i\right\|^2\le\delta,
 \qquad
 \left\|\eta-\sum_i e_i\eta e_i\right\|^2\ge2^{-18}
 \quad(0<\delta<1).
 \tag{PDC.3}
\]

For an orthogonal family \(F\) of nonzero projections, let \(p=1-\sum_{e\in F}e\) and define

\[
 \begin{split}
 B_\zeta(F)&=\left\|\zeta-p\zeta p-\sum_{e\in F}e\zeta e\right\|^2,\\
 A(F)&=\|\xi-p\xi p\|^2+\|\eta-p\eta p\|^2.
 \end{split}\tag{PDC.4}
\]

Left and right projection actions commute. Consequently the maps \(\zeta\mapsto e\zeta e\) and \(\zeta\mapsto p\zeta p\) are mutually orthogonal projections on \(H\). Every displayed sum converges in norm, and \(0\le B_\zeta(F)\le\|\zeta\|^2\).

Call \(F\) admissible when \(A(F)\le2^{14}B_\eta(F)\) and \(B_\xi(F)\le\delta B_\eta(F)\). The empty family is admissible. A chain of admissible families has admissible union. Here are the limit details. The sums of the left projections increase strongly to the union sum; their complementary projections \(p\) decrease strongly. The commuting right actions do the same, so their products converge strongly on each vector. The orthogonal diagonal sums converge in norm to the union diagonal sum. Indeed their squared tails are tails of a summable family of nonnegative squared norms. Thus both quantities in (PDC.4) converge along the chain and the two non-strict inequalities persist. Maximality by inclusion therefore supplies an admissible family \(F\). Every such orthogonal family is countable: faithfulness gives \(\varphi(e)>0\), and there are finitely many members with \(\varphi(e)\ge1/n\) for each integer \(n\).

Suppose, towards a contradiction, that \(B_\eta(F)<2^{-18}\). Then \(A(F)<1/16\). Put \(\xi'=p\xi p\), \(\eta'=p\eta p\), \(a=\|\xi'\|\), \(b=\|\eta'\|\). Each original vector is within \(1/4\) of its compression, so \(3/4<a,b\le1\). Also

\[
 |\langle\xi',\eta'\rangle|
  =|\langle\xi',\eta\rangle|
  =|\langle\xi'-\xi,\eta\rangle|<1/4.
\]

The unit vectors \(\xi'/a,\eta'/b\) consequently have \(|\cos\theta|<4/9<1/2\), hence \(\sin^2\theta>3/4\). The corner standard form is supplied by SE02–03. Its vector \(\xi'\) is cyclic and separating: if a projection \(r\le p\) has \(r\xi'=0\), then \(r\xi r=0\); SE03's cone-support argument gives \(r\xi=0\), hence \(r=0\). Faithfulness and the standard-form support formulas give the assertion.

PC8 makes the nonzero corner \(pMp\) normally isomorphic to \(M\), so the averaging hypothesis holds there too. Apply Section 1 to the normalized corner vectors with tolerance \(\delta/2\). The resulting nonzero \(q\le p\) satisfies

\[
 \begin{split}
 \|q\xi'\|^2+\|q\eta'\|^2
  &< (4/3)^3\,1024\|[q,\eta']\|^2
    <2^{13}\|[q,\eta']\|^2,\\
 \|[q,\xi']\|^2
  &<\frac{a^2}{b^2}\frac\delta2\|[q,\eta']\|^2
    <\delta\|[q,\eta']\|^2.
 \end{split}\tag{PDC.5}
\]

In the first line we used \(a^2,b^2\le1\), \(b^{-2}<16/9\), and \(\sin^{-2}\theta<4/3\). The target commutator is nonzero, so \(q\ne p\).

We check exactly what adjoining \(q\) does, rather than estimate unrelated residuals. Put \(r=p-q\), \(\zeta'=p\zeta p\). The two new off-diagonal blocks are \(q\zeta r\) and \(r\zeta q\), orthogonal to each other and to all old off-diagonal blocks. Hence

\[
 B_\zeta(F\cup\{q\})-B_\zeta(F)
   =\|q\zeta r\|^2+\|r\zeta q\|^2
   =\|[q,\zeta']\|^2.
 \tag{PDC.6}
\]

For \(J\zeta=\zeta\), the other change obeys

\[
 \begin{split}
 \|\zeta-r\zeta r\|^2-\|\zeta-p\zeta p\|^2
 &=\|p\zeta q\|^2+\|q\zeta r\|^2\\
 &\le2\|q\zeta'\|^2.
 \end{split}\tag{PDC.7}
\]

The equality follows by orthogonal decomposition of the difference of the nested compression projections: \(L_pR_p-L_rR_r=L_pR_q+L_qR_r\). For the inequality use \(\|p\zeta q\|=\|q\zeta p\|\), since \(J\) interchanges these blocks, and \(\|q\zeta r\|\le\|q\zeta p\|\).

Equations (PDC.5)–(PDC.7) give

\[
 A(F\cup\{q\})\le A(F)+2^{14}\|[q,\eta']\|^2,
 \qquad
 B_\xi(F\cup\{q\})\le\delta B_\eta(F\cup\{q\}).
\]

The first inequality and admissibility of \(F\) imply the remaining admissibility inequality for the enlarged family. This contradicts maximality. We have proved \(B_\eta(F)\ge2^{-18}\). Adjoin the residual \(p\) when it is nonzero, and omit it otherwise. This is a partition of one. Its diagonal error is exactly \(B_\zeta(F)\), so \(B_\xi(F)\le\delta B_\eta(F)\le\delta\) proves (PDC.3).

## Finite signs give uniform projection displacement

Let first \(\eta\) be a \(J\)-real unit vector perpendicular to \(\xi\). For the partition from Section 2 write \(D\zeta=\sum_i e_i\zeta e_i\). Use the finite partition \(e_1,\ldots,e_n,r_n\), where \(r_n=1-\sum_{i\le n}e_i\), omitting zero members, and denote its diagonal map by \(D_n\). If the original partition is finite, take it itself. In the countably infinite case, \(r_n\to0\) strongly and the orthogonal series converges, so \(D_n\zeta\to D\zeta\). Also the range of \(D\) lies in the range of \(D_n\), and consequently

\[
 \|\xi-D_n\xi\|^2\le\delta,
 \qquad \|\eta-D_n\eta\|^2>2^{-19}
 \tag{PDC.8}
\]

for a sufficiently large finite partition. The strict second inequality follows from the limiting lower bound \(2^{-18}\).

For each assignment of signs to that finite partition, put \(u=\sum_j\epsilon_j f_j\). Then \(u=u^*=u^{-1}\), and averaging uniformly over the finitely many sign assignments gives

\[
 \mathbb E(u\eta u)=D_n\eta,
 \qquad
 \mathbb E\|[u,\eta]\|^2=2\|\eta-D_n\eta\|^2>2^{-18}.
 \tag{PDC.9}
\]

Indeed off-diagonal coefficients have mean zero and diagonal coefficients have mean one. Expanding \(\|u\eta u-\eta\|^2\), and using that \(D_n\) is an orthogonal projection, proves the second identity. Thus some sign choice has \(\|[u,\eta]\|^2>2^{-18}\). For every sign choice the diagonal vector commutes with \(u\), so
\(\|[u,\xi]\|\le2\|\xi-D_n\xi\|\).
The projection \(q=(1+u)/2\) therefore satisfies

\[
 \|[q,\xi]\|^2\le\delta,
 \qquad \|[q,\eta]\|^2>2^{-20}.
 \tag{PDC.10}
\]

This uses a finite probability space only.

For an arbitrary \(\eta\perp\xi\), decompose

\[
 \eta=\eta_1+i\eta_2,\qquad
 \eta_1=(\eta+J\eta)/2,\quad
 \eta_2=(\eta-J\eta)/(2i).
\]

The two vectors are \(J\)-real and perpendicular to \(\xi\), and their real inner product gives \(\|\eta\|^2=\|\eta_1\|^2+\|\eta_2\|^2\). At least one has squared norm at least \(\|\eta\|^2/2\). Apply (PDC.10) to that normalized vector. For a projection \(q\), each \([q,\eta_j]\) is \(J\)-anti-real; their inner product is real. Hence their mixed imaginary terms cancel and

\[
 \|[q,\eta]\|^2
  =\|[q,\eta_1]\|^2+\|[q,\eta_2]\|^2.
\]

Rescaling now proves, for every \(\eta\perp\xi\) and every \(\delta>0\), the existence of a nonzero projection with

\[
 \boxed{\quad \|[q,\xi]\|^2\le\delta,
 \qquad \|[q,\eta]\|^2\ge2^{-21}\|\eta\|^2.\quad}
 \tag{PDC.11}
\]

For \(\delta\ge1\) use any smaller positive tolerance; for \(\eta=0\) take \(q=1\). In the nonzero case the target bound ensures \(q\ne0\).

## Dominant averaging forces a trivial bicentralizer

Let \(a\in B_\varphi\), put \(a_0=a-\varphi(a)1\), and let \(\eta=a_0\xi\perp\xi\). Apply (PDC.11) with \(\delta=n^{-2}\) to obtain projections \(q_n\). NC21 gives

\[
 \|q_n\varphi-\varphi q_n\|\le2\|[q_n,\xi]\|\le2/n.
\]

Thus \((q_n)\) is a bounded asymptotic-centralizer sequence. The defining condition QA01 gives \(\|[q_n,a]\xi\|\to0\). Commutation of left and right actions yields the exact identity

\[
 [q_n,a]\xi=[q_n,\eta]-a_0[q_n,\xi].
\]

Consequently \(\|[q_n,\eta]\|\to0\). Its uniform lower bound in (PDC.11) forces \(\eta=0\). Separation of \(\xi\) gives \(a_0=0\). We have proved \(B_\varphi=\mathbb C1\), for every faithful normal state \(\varphi\).

## Two compact averaging arguments

We first give a useful state version. Let \(Q\) be a von Neumann algebra with faithful normal state \(\vartheta\), and let \(N\subset Q\) be a unital von Neumann subalgebra whose unitary conjugations preserve \(\vartheta\). Then

\[
 C_N(x)\cap(N'\cap Q)\ne\varnothing\qquad(x\in Q).
 \tag{PDC.12}
\]

Here is the full argument. The set \(C_N(x)\) is ultraweakly compact, as in QA02. In the faithful state GNS representation its image under \(b\mapsto b\xi_\vartheta\) is weakly compact: each vector coefficient is normal. The norm attains its minimum on that set, since its sublevel sets are weakly closed. The parallelogram identity makes the minimizing vector unique, and faithfulness makes its representing operator \(b\) unique. Every conjugation by \(u\in\mathcal U(N)\) preserves both the set and the squared GNS norm, because
\(\vartheta((uyu^*)^*(uyu^*))=\vartheta(y^*y)\).
It therefore fixes \(b\). Unitaries span \(N\), giving \(b\in N'\cap Q\). This proves (PDC.12).

Next let \(N\) be a factor with a faithful normal semifinite trace \(\tau\) and a faithful normal state. We prove

\[
 C_N(y)\cap\mathbb C1\ne\varnothing\qquad(y\in N).
 \tag{PDC.13}
\]

First choose nonzero finite-trace projections \(p_n\uparrow1\). To construct them, semifiniteness supplies a nonzero finite-trace positive element below any nonzero projection. A nonzero spectral cut away from zero is a finite-trace subprojection. A maximal orthogonal family of these fills one. The faithful normal state makes the family countable by the counting argument in Section 2. Its finite partial sums give the required sequence; a finite family gives the constant terminal sequence.

For each \(p=p_n\), averaging \(y\) with its conjugate by \(2p-1\) gives the block diagonal element \(pyp+(1-p)y(1-p)\). The corner \(pNp\) is a factor by PC4. Apply (PDC.12) there to the normalized trace \(\tau(p)^{-1}\tau|_{pNp}\) and the whole algebra \(pNp\). The first block averages to \(c_np_n\), with
\(c_n=\tau(p_nyp_n)/\tau(p_n)\) and \(|c_n|\le\|y\|\).
Extend each corner unitary by \(1-p_n\). The second block is unchanged, so

\[
 b_n=c_np_n+(1-p_n)y(1-p_n)\in C_N(y).
\]

A subsequence of the bounded scalars \(c_n\) converges to some \(c\). Along it, \(b_n\to c1\) strongly: the tail block tends strongly to zero and \(p_n\to1\). The norms are uniformly bounded. The vector-series description CP06 then gives ultraweak convergence, by first truncating each summable series and then passing to the strong limit on its finite part. Since \(C_N(y)\) is ultraweakly closed, it contains \(c1\). This proves (PDC.13), without a norm-closure averaging theorem.

## An explicit dominant stabilization

Assume now that some faithful normal state \(\varphi\) on \(M\) has irreducible centralizer \(N=M_\varphi\), so \(N'\cap M=\mathbb C1\). Put

\[
 K=L^2(\mathbb R,dq)\otimes\ell^2(\mathbb N),\qquad
 Q=M\bar\otimes B(K),\qquad
 \Omega=\varphi\otimes\operatorname{Tr}_K.
\]

TW2–5 constructs this weight on the entire positive cone, proves it faithful normal semifinite, and gives \(\sigma_t^\Omega=\sigma_t^\varphi\otimes\operatorname{id}\). Let \(Q_0\) be multiplication by \(q\) on \(L^2(\mathbb R)\), and set \(h=1_M\otimes e^{Q_0}\otimes1\). This is a positive injective selfadjoint operator affiliated with the centralizer of \(\Omega\). The precise unbounded-density construction CZ2 is

\[
 \Psi(Y)=\sup_{\varepsilon>0}
       \Omega(h_\varepsilon^{1/2}Yh_\varepsilon^{1/2}),
 \qquad h_\varepsilon=h(1+\varepsilon h)^{-1},\quad Y\in Q_+.
 \tag{PDC.14}
\]

It is faithful normal semifinite. CZ5 proves the full modular formula

\[
 \sigma_t^\Psi=sigma_t^\varphi\otimes
                   \operatorname{Ad}(e^{itQ_0}\otimes1).
 \tag{PDC.15}
\]

In particular its centralizer contains
\(1\otimes L^\infty(\mathbb R)\bar\otimes B(\ell^2)\).
The unital copy of \(B(\ell^2)\) supplies two isometries with orthogonal ranges. Compressing them by any nonzero central projection of \(Q_\Psi\) still gives such isometries, so this centralizer is properly infinite.

For \(T_sf(q)=f(q-s)\), direct substitution gives \(T_s^*Q_0T_s=Q_0+s\). Write \(v_s=1\otimes T_s\otimes1\). Basis independence in TW3 gives \(\Omega\circ\operatorname{Ad}v_s=\Omega\), on the entire positive cone. Also

\[
 v_s^*h_\varepsilon v_s
       =e^s h_{e^s\varepsilon}.
\]

Apply these identities to every bounded cutoff in (PDC.14), then take the increasing supremum. This gives

\[
 \Psi(v_sYv_s^*)=e^s\Psi(Y)\qquad(Y\ge0),
 \tag{PDC.16}
\]

including infinite values. Thus \(\Psi\) is dominant.

We also need a semifinite trace on \(Q_\Psi\), not a finite restriction of \(\Psi\). Here is the exact earlier input. IAP5 constructs on a type \(\mathrm{III}_1\) factor with separable predual a dominant reference \(\Phi\) whose centralizer is the semifinite coefficient factor of a trace-scaling crossed-product presentation. It carries a faithful normal semifinite trace \(\tau\); the type \(\mathrm{III}_1\) condition makes its center scalar. PC5's filling isometries identify \(M\bar\otimes B(K)\) normally with \(M\). Explicitly, for an orthonormal basis indexed by \(j\), choose \(s_j^*s_k=\delta_{jk}1\), \(\sum_js_js_j^*=1\); the unitary \((\zeta_j)\mapsto\sum_js_j\zeta_j\) carries matrices \((x_{jk})\) to \(\sum_{j,k}s_jx_{jk}s_k^*\), in the bounded strong sense of finite compressions. Transport the reference to \(Q\). DS5 gives a unitary equivalence of that dominant weight and \(\Psi\), so it identifies their centralizers. Hence \(Q_\Psi\) is a semifinite factor and inherits a faithful normal semifinite trace. This argument does not identify that trace with \(\Psi|_{Q_\Psi}\).

## Averaging into the dominant centralizer and then to scalars

Fix \(x\in Q\), and let \(C=C_{Q_\Psi}(x)\). This compact convex set is invariant under every conjugation by \(\mathcal U(Q_\Psi)\). In particular if \(z\in C\), every ultraweak convex average of such conjugates of \(z\) still belongs to \(C\).

First average into the second tensor factor. Fix an orthonormal basis of \(K\), choose strictly positive weights \(w_j\) with sum one, and define

\[
 \vartheta(Y)=\sum_j w_j\varphi(Y_{jj})\qquad(Y\in Q).
\]

This is a normal state. It is faithful: for \(Y\ge0\), zero value forces every positive diagonal entry to vanish; then \(Y^{1/2}\) vanishes on every coordinate subspace and hence \(Y=0\). The unitaries of \(N\otimes1\) preserve \(\vartheta\), since they preserve each diagonal state value. They also lie in \(Q_\Psi\) by (PDC.15). Equation (PDC.12) therefore puts an element of \((N\otimes1)'\cap Q\) inside \(C\). This commutant is exactly \(1\otimes B(K)\): every matrix entry of a commuting element is in \(N'\cap M=\mathbb C1\); compression to a fixed unit vector in a representation of \(M\) shows that the scalar matrix defines a bounded operator on \(K\), and equality of all entries gives the assertion. Thus \(C\) contains \(1\otimes T\) for some \(T\in B(K)\).

Next put \(A=L^\infty(\mathbb R)\bar\otimes\ell^\infty(\mathbb N)\subset B(K)\). We verify that it is maximal abelian in this representation. An operator commuting with the coordinate projections is diagonal in the \(\ell^2\) coordinate. Each diagonal block on \(L^2(\mathbb R)\) commutes with all bounded multipliers. On a unit interval \(E\), its value on \(1_E\) is a function \(g_E\); commutation gives \(Tf=f g_E\) for bounded \(f\) supported there. Testing this equality on indicators shows \(|g_E|\le\|T\|\) almost everywhere. Bounded functions are dense in \(L^2(E)\) by truncation, so the block is multiplication by \(g_E\). The countable intervals assemble a bounded multiplier on \(\mathbb R\). Applying this to every coordinate, with the same uniform bound, yields an element of \(A\). The bounded diagonal sum is the strong limit of its finite coordinate compressions. Thus \(A'=A\) in \(B(K)\).

All unitaries of \(1\otimes A\) belong to \(Q_\Psi\) by (PDC.15). For a finite set \(F\) of these commuting unitaries, average the first \(m\) powers of each conjugation and compose the averages. Applied to \(1\otimes T\), the result remains in \(C\cap(1\otimes B(K))\). For every \(v\in F\), its difference from its conjugate by \(v\) has norm at most \(2\|T\|/m\), by telescoping; the other averages commute and are contractions. Direct the pairs \((F,m)\) by inclusion and increasing integers. Ultraweak compactness gives a convergent subnet. For each fixed \(v\), the norm bound eventually applies and tends to zero, so its limit commutes with every unitary in \(1\otimes A\). It lies in the second tensor factor, and maximal abelianness therefore makes the limit an element

\[
 z\in C\cap(1\otimes A)\subset C\cap Q_\Psi.
\]

Finally \(Q_\Psi\) is a semifinite factor by Section 6. The state \(\vartheta\) restricts faithfully and normally to it. Apply (PDC.13) there to \(z\). Every average used stays in \(C\), so \(C\) contains a scalar. This proves dominant-weight scalar averaging on \(Q\). The normal isomorphism \(Q\cong M\), followed by DS5, gives the property on \(M\) for every dominant weight.

## The equivalence and the source calculations

We have now proved that the following three conditions are equivalent for a type \(\mathrm{III}_1\) factor with separable predual:

1. For a dominant weight \(\Phi\), the ultraweakly closed convex hull of every \(\mathcal U(M_\Phi)\)-conjugacy orbit meets \(\mathbb C1\).
2. Every faithful normal state has trivial bicentralizer.
3. There exists a faithful normal state with irreducible centralizer.

Condition 1 is independent of the chosen dominant weight by DS5. Sections 1–4 prove 1 implies 2. SCV09 proves 2 implies 3 and 3 implies 2, and also proves that in condition 3 such faithful states are norm dense in all normal states. Sections 5–7 prove 3 implies 1. No injectivity assumption has been used.

The mathematical antecedents are Takesaki, *Theory of Operator Algebras III*, Chapter XVIII, Section 3, Lemmas 3.14–3.16 and the remaining directions involving condition (i) of Theorem 3.6, printed pp.334 and 343–350, 360. The angle estimate uses its target vector consistently: after writing \(\eta=\cos\theta\,\xi+\sin\theta\,\zeta\), the upper bound for the reference commutator uses \([q,\zeta]\). The residual estimates in the proof of Lemma 3.15, printed pp.347–348, must compare the new residual \(r=p-q\) with the old residual \(p\). Equations (PDC.6)–(PDC.7) give the exact block identities, resolving the repeated or mismatched residual terms in those lines.

The partition bound is \(2^{-18}\), and the general-vector projection bound is \(2^{-21}\). A finite sign calculation with the squared average (PDC.9) retains these constants without an infinite product measure. For the reverse implication, Sections 5–7 replace the ambient maximal-abelian-subalgebra and norm-closure averaging route by a faithful-state minimization, an explicitly verified multiplication algebra, and ultraweak averaging in finite trace corners. The earlier weight construction and dominant-weight comparison retain their exact hypotheses. The structural results preceding the source theorem and its injective-factor corollary are separate assertions.
