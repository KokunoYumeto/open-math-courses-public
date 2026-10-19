# Bicentralizer structure and injective factors



The asymptotic bicentralizer is a von Neumann algebra preserved by modular time. Its intersection with the state centralizer is much more restricted: in type III1 it is atomic, and two nonzero orthogonal projections in that intersection cannot have the same state value. We prove these assertions, including the projection-splitting step behind atomicity. We then show how finite-dimensional averages in a dominant centralizer prove the bicentralizer theorem for injective factors.

The exact earlier inputs are the asymptotic-centralizer tests and compact convex criterion, QA01–02, operator and predual scalar averaging, QA03–04, faithful-state modular invariance, FS09, and the dominant-centralizer equivalence, PDC06 and PDC08. The type III argument uses state homogeneity, HC2–7, projection comparison, PC1–2 and PC8, and type transport to corners, CT1–2. For the injective application we use fixed-point injectivity, Section 2, the finite and semifinite injective-factor theorem, Section 5, the dominant reference, IAP5, and the trace-scaling relative commutant, RCC4–5.

Until a type hypothesis is explicitly imposed, \(M\ne0\) is any von Neumann algebra with faithful normal state \(\varphi\). In its standard representation let \(\xi=\xi_\varphi\) be the cyclic separating unit vector and \(\|x\|_\varphi=\|x\xi\|\). The conventions are \((x\psi)(a)=\psi(ax)\), \((\psi x)(a)=\psi(xa)\), and \(u\psi u^*=\psi\circ\operatorname{Ad}(u^*)\). Write

\[
 \begin{split}
 \mathrm{AC}(\varphi)&=\{(x_n)\in\ell^\infty(M):
                    \|x_n\varphi-\varphi x_n\|\longrightarrow0\},\\
 B_\varphi&=\{a\in M:\|[a,x_n]\|_\varphi\longrightarrow0
                    \text{ for every }(x_n)\in\mathrm{AC}(\varphi)\}.
 \end{split}\tag{BSI.1}
\]

QA01 proves that \(\mathrm{AC}(\varphi)\) is a unital C*-algebra, that its unitary sequences suffice in the second test, and that bounded convergence in \(\|\cdot\|_\varphi\) to zero is strong and sigma-strong convergence. These facts include the four-unitary decomposition and the dense commutant-orbit proof of the topology assertion.

## Algebraic closure, adjoints and modular invariance

For \(\delta>0\) put

\[
 \begin{aligned}
 U_\delta&=\{u\in\mathcal U(M):\|u\varphi-\varphi u\|<\delta\},\\
 C_\delta(a)&=\overline{\operatorname{co}}^{\,uw}
                      \{u^*au:u\in U_\delta\},\\
 C(a)&=\bigcap_{\delta>0}C_\delta(a).
 \end{aligned}
 \tag{BSI.2}
\]

The complete criterion proved in QA02 is

\[
 a\in B_\varphi\quad\Longleftrightarrow\quad C(a)=\{a\}.
 \tag{BSI.3}
\]

Its converse uses ultraweak compactness of the operator orbit, followed by weak convergence and convergence of the squared Hilbert norms. In particular it does not treat right multiplication by a nearly centralizing unitary as an exact state-norm isometry.

We now prove that \(B_\varphi\) is a von Neumann subalgebra. It contains one and is a linear space. For \(a,b\in B_\varphi\) and \((x_n)\in\mathrm{AC}(\varphi)\),

\[
 [ab,x_n]=a[b,x_n]+[a,x_n]b.
\]

The first term tends to zero on \(\xi\). The uniformly bounded operators \([a,x_n]\) tend strongly to zero by QA01, so the second tends to zero on \(\xi\) as well. Thus \(ab\in B_\varphi\). Taking adjoints is an ultraweakly continuous real-linear involution and preserves convex hulls. Hence \(C_\delta(a)^*=C_\delta(a^*)\) and \(C(a)^*=C(a^*)\). Equation (BSI.3) proves closure under adjoints.

Suppose \(a\) belongs to the strong closure of \(B_\varphi\). For \(\varepsilon>0\), choose \(b\in B_\varphi\) with \(\|a-b\|_\varphi<\varepsilon\). For any unitary sequence \((u_n)\in\mathrm{AC}(\varphi)\), put \(c=a-b\). Then

\[
 \|u_n^*c u_n\|_\varphi^2
 =\varphi(u_n^*c^*c u_n)\longrightarrow\varphi(c^*c),
 \tag{BSI.4}
\]

because the error is at most \(\|c\|^2\|u_n\varphi u_n^*-\varphi\|\). The triangle inequality and the test for \(b\) give

\[
 \limsup_n\|u_n^*a u_n-a\|_\varphi
       \le2\|a-b\|_\varphi<2\varepsilon.
\]

Letting \(\varepsilon\downarrow0\), the unitary test gives \(a\in B_\varphi\). This proves strong closure, without imposing a common norm bound on a net approximating \(a\). The unital strong-closed star algebra is therefore a von Neumann algebra.

Let \(\sigma_t=\sigma_t^\varphi\). State invariance and the module conventions give

\[
 [\sigma_t(x),\varphi]=[x,\varphi]\circ\sigma_{-t},
 \qquad
 \|\sigma_t(x)\|_\varphi=\|x\|_\varphi.
 \tag{BSI.5}
\]

Thus \(\sigma_t\) carries \(\mathrm{AC}(\varphi)\) onto itself. For \(a\in B_\varphi\), apply its test to \((\sigma_{-t}(x_n))\) and then (BSI.5) to obtain \(\sigma_t(a)\in B_\varphi\). Applying the same argument at \(-t\) proves \(\sigma_t(B_\varphi)=B_\varphi\).

## Excluding equal-mass orthogonal projections

From now through Section 3, assume that \(M\) is a type \(\mathrm{III}_1\) factor with separable predual. Every constant sequence from \(M_\varphi\) lies in \(\mathrm{AC}(\varphi)\). Equation (BSI.1) and separation of \(\xi\) therefore imply

\[
 A:=B_\varphi\cap M_\varphi\subset Z(M_\varphi).
 \tag{BSI.6}
\]

In particular \(A\) is an abelian von Neumann algebra.

Suppose that nonzero orthogonal projections \(e,f\in A\) satisfy \(\varphi(e)=\varphi(f)=c>0\). PC8 supplies \(w\in M\) with \(w^*w=e\), \(ww^*=f\). The corner \(eMe\) is still type \(\mathrm{III}_1\) with separable predual, by CT1–2. The two states on it

\[
 \alpha(x)=c^{-1}\varphi(x),\qquad
 \beta(x)=c^{-1}\varphi(w x w^*)
\]

are faithful and normal. HC's unitary homogeneity supplies unitaries \(v_n\in eMe\) such that \(\|\beta\circ\operatorname{Ad}v_n-\alpha\|\to0\). Set \(w_n=w v_n\). Then

\[
 w_n^*w_n=e,\qquad w_nw_n^*=f,
 \qquad
 \varepsilon_n:=\|\varphi(w_n\,\cdot\,w_n^*)|_{eMe}
                         -\varphi|_{eMe}\|\longrightarrow0.
 \tag{BSI.7}
\]

Put \(r=1-e-f\) and \(s_n=w_n+w_n^*+r\). The three supports show that \(s_n=s_n^*\) and \(s_n^2=1\). Because \(e,f,r\) are in \(M_\varphi\), the state has no mixed block terms: for distinct such projections \(p,q\), \(\varphi(pxq)=\varphi(qpx)=0\). Conjugation by \(s_n\) swaps the \(e\) and \(f\) blocks and fixes the \(r\) block. The error on \(eMe\) is \(\varepsilon_n\); the error on \(fMf\) is the same, transported by the isomorphism \(x\mapsto w_nxw_n^*\). Compression has norm one, so

\[
 \|s_n\varphi s_n-\varphi\|\le2\varepsilon_n\longrightarrow0.
 \tag{BSI.8}
\]

Thus \((s_n)\in\mathrm{AC}(\varphi)\). However,

\[
 [s_n,e]=w_n-w_n^*,\qquad
 [s_n,e]^*[s_n,e]=e+f,\qquad
 \|[s_n,e]\|_\varphi^2=2c>0.
 \tag{BSI.9}
\]

This contradicts \(e\in B_\varphi\). There is no such pair of nonzero orthogonal projections. Adding the residual \(r\) made the test sequence unitary on all of \(M\); no unitary extension of an unmatched complement was assumed.

## Why the central intersection is atomic

We supply the measure-splitting argument needed to turn Section 2 into atomicity. Let \(D\) be an abelian von Neumann algebra with faithful normal finite positive functional \(\rho\), and suppose a nonzero projection \(r\in D\) contains no minimal nonzero projection.

Every nonzero \(q\le r\) contains nonzero projections of arbitrarily small positive \(\rho\)-value. Indeed split \(q\) into two nonzero orthogonal subprojections; retain one with value at most \(\rho(q)/2\), and repeat. None of the retained projections is minimal, so this iteration continues.

For \(0<t<\rho(r)\), order the projections \(p\le r\) satisfying \(\rho(p)\le t\) by inclusion. A chain has an upper bound: its increasing projection supremum remains under \(r\), and normality gives value at most \(t\). Choose a maximal such \(p\). If \(\rho(p)<t\), then \(r-p\ne0\), and the preceding construction gives a nonzero \(q\le r-p\) with \(\rho(q)\le t-\rho(p)\). The projection \(p+q\) contradicts maximality. Therefore

\[
 \text{for every }0<t<\rho(r),\quad
 \text{some }p\le r\text{ satisfies }\rho(p)=t.
 \tag{BSI.10}
\]


Apply this to \(A\) from (BSI.6) and \(\rho=\varphi|_A\). Distinct minimal nonzero projections in an abelian algebra are orthogonal: their product is a subprojection of each, hence is either zero or both. They form a countable family \((p_i)\), since their positive state values sum to at most one. Its strong sum is a projection \(p\). If \(r=1-p\ne0\), this residual contains no minimal projection. Equation (BSI.10), with \(t=\varphi(r)/2\), gives two nonzero orthogonal projections of equal value, contradicting Section 2. Thus \(\sum_i p_i=1\).

For completeness, \(p_iA p_i=\mathbb Cp_i\). Otherwise a nonscalar selfadjoint element in that corner would have a proper nonzero spectral projection, contradicting minimality. Every \(a\in A\) consequently has the unique form \(a=\sum_i a_i p_i\), with \(\sup_i|a_i|=\|a\|\). Conversely each bounded scalar family defines such a strong sum in \(A\); its finite sums are uniformly bounded and the projection tails tend strongly to zero. Hence \(A\cong\ell^\infty(I)\), proving atomicity. Its state is

\[
 \varphi\left(\sum_i a_i p_i\right)=\sum_i c_i a_i,
 \qquad c_i=\varphi(p_i)>0,\quad\sum_i c_i=1.
 \tag{BSI.11}
\]

Section 2 says more than distinct individual weights: two disjoint nonempty subsets of the atoms cannot have equal sums of their \(c_i\)'s. This includes infinite subsets, by normality.

## The four scalar-averaging criteria with their topologies

For an arbitrary \(M\) and faithful normal state \(\varphi\), the following conditions are equivalent:

1. \(B_\varphi=\mathbb C1\).
2. For every \(a\in M\) and \(\delta>0\), \(C_\delta(a)\cap\mathbb C1\ne\varnothing\).
3. A functional \(\psi\in M_*\) satisfying \(\|x_n\psi-\psi x_n\|\to0\) for every \((x_n)\in\mathrm{AC}(\varphi)\) is a scalar multiple of \(\varphi\).
4. For every \(\psi\in M_*\) and \(\delta>0\), the norm-closed convex hull of \(\{u\psi u^*:u\in U_\delta\}\) meets \(\mathbb C\varphi\).

Here is the complete chain in terms of the previously proved lemmas. QA03 obtains, by Hilbert norm minimization, an element of \(B_\varphi\) in \(C(a)\). If condition 1 holds, that element is scalar. Its value under \(\varphi\) is \(\varphi(a)\), by QA02, so it is \(\varphi(a)1\). This proves condition 2. Conversely, the nonempty compact scalar intersections \(C_\delta(a)\cap\mathbb C1\) are nested. Their common scalar is \(\varphi(a)1\). For \(a\in B_\varphi\), (BSI.3) makes it equal to \(a\), proving condition 1.

If condition 2 holds, the same compact intersection puts \(\varphi(a)1\) in every \(C_\delta(a)\). Applying every real functional \(\operatorname{Re}\psi\), and using the real Hahn–Banach separation argument of QA04 in \(M_*\), gives

\[
 \psi(1)\varphi\in
 \overline{\operatorname{co}}^{\,\|\cdot\|}
       \{u\psi u^*:u\in U_\delta\}.
 \tag{BSI.12}
\]

Thus condition 4 holds. Conversely, evaluation at one forces any scalar multiple in that convex hull to be \(\psi(1)\varphi\); no compactness of a predual ball is required. If \(\psi\) satisfies condition 3's antecedent, the contrapositive sequence test in QA04 gives

\[
 \lim_{\delta\downarrow0}\sup_{u\in U_\delta}
               \|u\psi-\psi u\|=0.
\]

Equation (BSI.12) and the convex triangle inequality therefore give \(\psi=\psi(1)\varphi\). This proves condition 3 from condition 4.

Finally assume condition 3 and let \(a\in B_\varphi\). The module product rule gives

\[
 [x_n,a\varphi]=[x_n,a]\varphi+a[x_n,\varphi].
\]

The second term tends to zero in norm. The first does too, because \(\|z\varphi\|\le\|z\xi\|\), the Cauchy–Schwarz estimate proved in QA04. Hence \(a\varphi=\varphi(a)\varphi\). Testing on \((a-\varphi(a)1)^*\) and using faithfulness gives \(a=\varphi(a)1\). This proves condition 1 and completes every implication. These equivalences do not require factoriality or separable predual.

## Exact finite averages and the ambient commutant

Let \(N\subset B(K)\) be generated by an increasing sequence of finite-dimensional unital star subalgebras \(F_n\). We prove that for every \(T\in B(K)\),

\[
 \overline{\operatorname{co}}^{\,uw}
       \{uTu^*:u\in\mathcal U(N)\}\cap N'\ne\varnothing.
 \tag{BSI.13}
\]

First consider \(F=\bigoplus_{\alpha=1}^k M_{d_\alpha}(\mathbb C)\), with central block units \(p_\alpha\) summing to one and matrix units \(e_{ij}^{\alpha}\). Average conjugations by the \(2^k\) sign unitaries \(\sum_\alpha\epsilon_\alpha p_\alpha\). Mixed blocks cancel, leaving \(\sum_\alpha p_\alpha T p_\alpha\).

Inside a block of dimension \(d\), use the clock and shift unitaries

\[
 C=\sum_{j=0}^{d-1}e^{2\pi i j/d}e_{jj},
 \qquad S=\sum_{j=0}^{d-1}e_{j+1,j},
\]

where indices are modulo \(d\). Extend each by the identity on the complementary blocks. Averaging the \(d\) clock conjugations kills all unequal matrix indices, since the sum of a nontrivial \(d\)-th root character is zero. Averaging the \(d\) shift conjugations makes all diagonal entries equal. Thus composing these finite averages over all blocks gives

\[
 E_F(T)=\sum_\alpha\frac1{d_\alpha}
                  \sum_{i,j=0}^{d_\alpha-1}
                  e_{ij}^{\alpha}T e_{ji}^{\alpha}.
 \tag{BSI.14}
\]

This is a finite convex combination of conjugations by unitaries of \(F\), including blocks of dimension one. Matrix multiplication shows that its output commutes with every \(e_{ij}^{\alpha}\), hence with \(F\). Its norm is at most \(\|T\|\).

Apply (BSI.14) to \(F_n\). The bounded sequence \(E_{F_n}(T)\) has an ultraweakly convergent subnet by dual-ball compactness. Its limit belongs to the closed convex hull in (BSI.13). For each fixed \(m\), every term with \(n\ge m\) commutes with \(F_m\). Separate ultraweak continuity of multiplication passes these identities to the limit. It therefore commutes with the generated algebra \(N\), proving (BSI.13). No normality of a limiting averaging map is claimed or needed. The same argument works for a directed increasing family.

## The dominant centralizer of an injective factor

Assume that \(M\) is an injective type \(\mathrm{III}_1\) factor with separable predual. We use injectivity in its equivalent concrete form: in a faithful normal representation there is a unital completely positive retraction \(B(H)\to M\). The retraction need not be normal. The fixed-point injectivity theorem linked at the beginning applies to the modular action of every faithful normal semifinite weight. To make its averaging step explicit, the maps

\[
 P_T(x)=\frac1{2T}\int_{-T}^{T}\sigma_t(x)\,dt\qquad(T>0)
\]

are defined ultraweakly by normal coefficients. They are unital completely positive contractions. A point-ultraweak cluster map exists by compactness of the product of the operator balls containing \(P_T(x)\). For fixed \(s\) and \(T>|s|\),

\[
 \|\sigma_s(P_T(x))-P_T(x)\|
       \le\frac{|s|}{T}\|x\|.
 \tag{BSI.15}
\]

Normality of \(\sigma_s\) makes the cluster map take values in the fixed algebra; constant orbits show that it fixes that algebra. Linearity, the unit, and matrix positivity pass to the point-ultraweak limit. Composing with the original retraction proves injectivity of the centralizer. This also explains why normality of the new retraction is unnecessary.

Choose IAP5's dominant reference. It gives an actual presentation

\[
 M=N\rtimes_\theta\mathbb R,
 \qquad N=M_\Phi,\qquad Z(N)=\mathbb C1,
 \qquad \tau\circ\theta_s=e^{-s}\tau,
 \tag{BSI.16}
\]

where \(N\) is properly infinite with separable predual and \(\tau\) is a faithful normal semifinite trace on \(N\). The trace is part of the coefficient presentation, not an asserted finite restriction of \(\Phi\). The preceding fixed-point argument makes \(N\) injective.

This coefficient factor has no minimal nonzero projection. If \(p\) were minimal, semifiniteness would give \(0<\tau(p)<\infty\): a nonzero finite-trace positive element below \(p\) is a positive scalar multiple of \(p\). Any two minimal projections in a factor are equivalent, since PC2's nonzero polar bridge exhausts both of their minimal supports. In particular \(p\sim\theta_s(p)\), so traciality would give \(\tau(p)=\tau(\theta_s(p))=e^{-s}\tau(p)\), impossible for \(s\ne0\). Thus the properly infinite semifinite factor \(N\) is of type \(\mathrm{II}_\infty\).

The complete earlier finite injective-factor theorem and its semifinite Corollary 5.2 now give a normal isomorphism

\[
 N\cong R\bar\otimes B(\ell^2),
 \tag{BSI.17}
\]

where \(R\) has a generating increasing sequence of dyadic matrix algebras \(R_n\). This input is the finite-factor theorem, not the type III uniqueness theorem for which the current bicentralizer result is used. To see the required finite approximations explicitly, let \(p_n\) project onto the first \(n\) coordinates of \(\ell^2\) and put

\[
 F_n=R_n\otimes\bigl(p_nB(\ell^2)p_n+\mathbb C(1-p_n)\bigr).
 \tag{BSI.18}
\]

Each \(F_n\) is a finite-dimensional unital algebra and \(F_n\subset F_{n+1}\). The generated algebra contains \(R_n\otimes1\) for all \(n\) and every finite matrix unit in the second factor. These generate \(R\bar\otimes B(\ell^2)\). Transporting (BSI.18) through (BSI.17) gives the finite-dimensional sequence required in Section 5 inside the actual centralizer.

## The injective type III1 bicentralizer theorem

The relative-commutant theorem RCC5 applies to exactly the trace-scaling presentation (BSI.16). It states

\[
 N'\cap(N\rtimes_\theta\mathbb R)=Z(N)=\mathbb C1.
 \tag{BSI.19}
\]

Its proof uses the normal coefficient embedding throughout, so the relative commutant here is that of the specified centralizer in \(M\).

For \(x\in M\), apply the averages of Section 5 to the finite-dimensional sequence in Section 6. Every conjugate stays in \(M\), and \(M\) is ultraweakly closed in \(B(H)\). The limit therefore lies in \(N'\cap M\), not merely in the ambient commutant. Equation (BSI.19) makes it scalar. Thus the dominant-weight averaging condition holds for \(\Phi\).

PDC08 now proves both conclusions:

1. Every faithful normal state \(\varphi\) on \(M\) has \(B_\varphi=\mathbb C1\).
2. Faithful normal states with irreducible centralizer are norm dense in the full normal state space of \(M\).

The dominant-weight comparison already included in PDC also makes scalar averaging hold for every faithful dominant weight. The density assertion includes approximation of nonfaithful normal states. We have used injectivity only to obtain injectivity of the dominant centralizer and its finite-dimensional approximations; all intervening averaging and commutation arguments have been given explicitly.

## Source comparison and the boundaries of the assertions

The mathematical antecedents are Takesaki, *Theory of Operator Algebras III*, Chapter XVIII, Section 3, Lemma 3.1, Corollary 3.2, Lemma 3.3, Proposition 3.4 and Corollary 3.7, printed pp.329–334. Lemma 3.1 is the complete earlier QA02 compact-convex criterion used in Section 1. Proposition 3.4 is QA03–04's equivalence, with every direction and normalization displayed in Section 4. These two source identifications use existing proofs, rather than add different assertions under the same names.

The closure proof retains squared state norms in (BSI.4); the convergence line in the source proof of Lemma 3.1 must likewise compare squared norms with state values. Section 2's forbidden equal-mass pair is explicitly nonzero. Section 3 supplies the atomicity argument after that exclusion.

For Proposition 3.4, operator convex closure is ultraweak, while functional convex closure is in predual norm. Evaluation at one determines the scalar in the latter; it does not require weak compactness of an arbitrary predual ball. For Corollary 3.7, we have used the earlier finite injective-factor theorem to construct the centralizer averages. This route keeps the finite-factor theorem, the trace-scaling relative commutant, and the type III conclusion in their proper order. The arguments do not assume uniqueness of the injective type III1 factor.
