# Cyclic towers in finite algebras

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Spot-checked by GPT-6 Astra (OpenAI) in a separate session. Original text is public domain (CC0).*

## Introduction

An orbit can be cut into long pieces whose endpoints occupy little of the space. In a finite von Neumann algebra, projections play the role of measurable sets. They need not commute, so making orbit pieces disjoint requires an additional geometric step.

We prove a cyclic form of Connes's noncommutative Rokhlin theorem. Given a trace-preserving automorphism whose nonzero powers remain outer in every invariant corner, we find a partition of the identity that it almost rotates. The algebra may have nonseparable predual. This matters when the algebra is an asymptotic centralizer, even if the original factor has separable predual.

The tower construction follows [Connes], Theorem 1.2.5 and its supporting lemmas. The present treatment adds the simultaneous Gram estimate, explicit trace budgets, a full probability-algebra tower argument and five worked exercises. Its spectral input and the exact remaining programme prerequisites are specified in Section 2. It uses the complete local [finite free-action coboundary theorem](finite-free-actions-and-coboundaries.md) for a finite cyclic character, and the elementary discrete spectrum argument proved below. [Bounded topology and tracial representations](bounded-topology-and-tracial-representations.md), Theorem 3.1 and Sections 4–7, supplies the bounded tracial topology used in the limiting arguments. The projection and center-valued trace interfaces, including equal-center-valued-trace comparison, are given in [Finite free actions and unitary coboundaries](finite-free-actions-and-coboundaries.md), Sections 1–2 and 9. Spectral calculus and polar decomposition remain background. The later application uses Central sequence algebras and exact lifts, Theorems 3.1, 5.1 and 6.1.

## 1. The theorem and its hypotheses

Let \(N\) be a von Neumann algebra with a faithful normal tracial state \(\tau\). Put
\[
\|x\|_1=\tau(|x|),\qquad \|x\|_2=\tau(x^*x)^{1/2}.
\]
An automorphism \(\alpha\) is **properly outer** if its restriction to \(eNe\) is not inner for every nonzero projection \(e\) with \(\alpha(e)=e\). It is **aperiodic** if \(\alpha^k\) is properly outer for every nonzero integer \(k\).

For a factor, outerness and proper outerness agree. For an algebra with center they differ: an automorphism may be nontrivial on one summand and the identity on another.

**Theorem 1.1 (cyclic towers).** Suppose \(\alpha\) is aperiodic and \(\tau\circ\alpha=\tau\). For every positive integer \(n\) and every \(\varepsilon>0\), there are orthogonal projections \(p_0,\ldots,p_{n-1}\) with sum \(1\) such that
\[
\|\alpha(p_j)-p_{j+1}\|_2<\varepsilon\quad(0\leq j<n),
\tag{1.1}
\]
where subscripts are read modulo \(n\). No separability assumption is made on \(N\).

The projections need not have trace exactly \(1/n\). Equation (1.1) implies
\[
|\tau(p_j)-\tau(p_{j+1})|<\varepsilon.
\]
When \(\alpha\) fixes the center pointwise, the proof gives more: a unitary arbitrarily close to \(1\) in \(\|\cdot\|_1\) changes \(\alpha\) into an automorphism that rotates a partition exactly.

## 2. Finding a small overlap

We state precisely the spectral facts used in this section. These are general action-spectrum results, rather than additional assumptions about \(N\).

- An automorphism has a largest invariant central summand on which it is inner. On its complement it is properly outer.
- If every nonzero power of \(\beta\) is properly outer and \(\beta\) fixes the center, its action spectrum is the whole circle. In particular there are norm-one \(x\) with \(\|\beta(x)+x\|\) arbitrarily small.
- If \(\beta\) gives a free action of a finite cyclic group of order \(r\) and fixes the center, there is a unitary \(u\) with \(\beta(u)=e^{2\pi i/r}u\).

For the first statement, take a maximal family of orthogonal invariant central summands on which the automorphism is inner. The strong sum of their implementing unitaries implements it on their join. If the complement contained a nonzero invariant inner corner, the corner-to-center extension calculation in Proposition 2.3 would produce another inner central summand. That calculation uses only central support, the partial-isometry covering and matrix coefficients; it does not use the local cutting conclusion of that proposition. This proves maximality and proper outerness on the complement. The historical statement is [Connes 1973], Proposition 1.5.1 and Lemma 1.5.2, printed pages 161–162 / PDF pages 30–31.

For the second statement, the exact historical source is [Connes–Takesaki], Section IV, Theorem 3.2 and Lemma 3.3, printed pages 537–538 / Part 2 PDF pages 14–15: for an action of a separable locally compact abelian group on a sigma-finite von Neumann algebra, the Connes spectrum is the kernel of the dual action on the crossed-product center. The algebra is not required to be a factor or to have separable predual. Our faithful normal tracial state makes \(N\) sigma-finite. For a center-fixed aperiodic \(\beta\), the discrete crossed-product coefficient calculation makes its relative commutant exactly \(Z(N)\): every nonzero-degree coefficient \(a\) satisfies \(xa=a\beta^k(x)\) for all \(x\in N\), with \(k\ne0\). Then \(a^*a\) and \(aa^*\) are central, and its polar part \(v\) has equal central initial and final support \(z\). If \(a\ne0\), \(v\) is a unitary on \(zN\) and \(\beta^k(x)=v^*xv\) there, contradicting proper outerness. Thus all those coefficients vanish. Coefficient uniqueness leaves exactly \(Z(N)\), which also commutes with the group unitary because the center is fixed. Therefore the crossed-product center is \(Z(N)\), and the dual circle action fixes it. The Connes spectrum, and hence the action spectrum, is the whole circle. This is the route in [Connes], Lemma 1.2.3, printed page 392 / PDF page 11. The normal coefficient expectation and coefficient uniqueness for a discrete crossed product are explained in [Finite outer period and its obstruction](finite-outer-period-and-obstruction.md), Section 3. The earlier programme lesson *The Connes spectrum as a dual-center kernel* (OA-FLOW 115), equations (K1)–(K43), writes out the dual-center proof, including spectral absorption, stabilization, regular tensor integrability and the two kernel inclusions. *Free actions and discrete crossed-product commutants* (OA-FLOW 128), equations (S1)–(S17), proves the normal coefficient and relative-commutant argument. The exact local versions of those proof slices have been read for this interface. They are not bundled in this selection, and their transitive fixed-corner, integrability and regular-model prerequisites have not all been reconciled here. The external citation alone does not close that programme-proof obligation.

If Lemma 2.2 is read for a finite algebra without a faithful normal tracial state, its center-fixed case can first be restricted to a nonzero sigma-finite central summand. Choose a nonzero normal positive functional on the center and take its support \(z\). It is faithful on \(Z(N)z\); composing with the faithful normal center-valued trace gives a faithful normal tracial state on \(zN\), after normalization. Since the center is fixed, \(z\) is invariant, and properly outer powers remain properly outer on this summand. The same argument applies there. This localization adds no separable-predual assumption.

The third statement follows from the full-scope local [finite free-action theorem](finite-free-actions-and-coboundaries.md), Section 1.3, equation (B2), proved in Sections 3–10. In the corner with identity \(e\), put \(\zeta=e^{2\pi i/r}\) and take the scalar cocycle \(c_{[j]}=\zeta^j e\). Equation (B2) gives \(c_{[j]}=v^*\gamma^j(v)\), so \(\gamma(v)=\zeta v\). The theorem applies to arbitrary finite nonfactors and invariant corners. Thus the spectral corner used in Lemma 2.2 has exactly the required scope.

### 2.1a. The elementary discrete spectrum step

For a single automorphism the approximate-eigenvector assertion can be proved without a general harmonic-analysis localization theorem. Let \(T\) be a surjective isometry of a complex Banach space. Its spectrum as a bounded operator is contained in \(\mathbb T\): Neumann series give the resolvent both outside the circle and inside it, using \(T^{-1}\).

The action spectrum of the discrete representation \(n\mapsto T^n\) is contained in that operator spectrum. Here is the needed inclusion directly. For \(a=(a_n)\in\ell^1(\mathbb Z)\), put \(A(a)=\sum_n a_nT^n\) and \(\widehat a(z)=\sum_n a_nz^n\). With the conjugated-character convention for the Fourier transform, this coordinate labels the character \(\gamma_z(n)=z^{-n}\). Inverting the circle coordinate leaves the full circle and \(-1\) unchanged. By definition, the action spectrum is the common zero set of the \(\widehat a\) for which \(A(a)=0\). Suppose \(\lambda\in\mathbb T\) is outside the operator spectrum. Choose a smooth function \(h\) on the circle, supported in a small closed arc of the resolvent set and satisfying \(h(\lambda)=1\). Put \(a_n=\int_{\mathbb T}h(z)z^{-n}\,dm(z)\), where \(dm\) is normalized Haar measure. Two integrations by parts give \(a_n=O(|n|^{-2})\) for \(n\ne0\), so these coefficients are absolutely summable.

For completeness, their Fourier series equals \(h\). The scalar Poisson kernel \(K_r(w)=(1-r^2)/|1-rw|^2=\sum_n r^{|n|}w^n\) is positive and has integral \(1\). Outside any fixed neighborhood of \(1\), its supremum tends to zero as \(r\uparrow1\). Uniform continuity of \(h\), splitting the convolution integral into that neighborhood and its complement, therefore gives \(K_r*h\to h\) uniformly. On the other hand, termwise integration gives \((K_r*h)(w)=\sum_n r^{|n|}a_nw^n\), and absolute summability makes these sums converge uniformly to \(\widehat a(w)\). Thus \(\widehat a=h\). For the operator series, absolute convergence gives
\[
\begin{gathered}
\sum_n r^{|n|}a_nT^n
=\int_{\mathbb T}h(z)P_r(T,z)\,dm(z),\\
0<r<1,\\
P_r(T,z)=\sum_n r^{|n|}z^{-n}T^n\\
=(1-r^2)(I-rz^{-1}T)^{-1}(I-rzT^{-1})^{-1}.
\end{gathered}
\]
On the compact support of \(h\), both inverse factors stay uniformly bounded as \(r\uparrow1\), because their limits are invertible and inversion is continuous. The integral therefore tends to zero in operator norm. The absolutely summable Fourier series makes its left side tend to \(A(a)\). Thus \(A(a)=0\), whereas \(\widehat a(\lambda)=h(\lambda)=1\). Consequently \(\lambda\) is outside the action spectrum, proving the inclusion.

Finally every point \(\lambda\) of the operator spectrum has norm-one approximate eigenvectors. Otherwise \(\|(T-\lambda I)x\|\geq c\|x\|\) for some \(c>0\). Choose \(\mu\) outside the circle with \(0<|\mu-\lambda|<c/4\). Then \(T-\mu I\) is invertible and is bounded below by \(c/2\), so its inverse has norm at most \(2/c\). The factorization
\[
\begin{gathered}
T-\lambda I\\
=(T-\mu I)\bigl(I+(\mu-\lambda)(T-\mu I)^{-1}\bigr)
\end{gathered}
\]
makes \(T-\lambda I\) invertible by a Neumann series, a contradiction. Apply this to \(T=\beta\) on \(N\) and \(\lambda=-1\). This closes the exact discrete approximate-eigenvector step. It does not prove the separate dual-center theorem used to obtain the full action spectrum. The general historical route is [Connes 1973], Lemmas 2.3.5–2.3.6 and 2.3.8, printed pages 179–181 / PDF pages 48–50.

**Lemma 2.1 (an approximate negative eigenvector).** If norm-one elements \(x\) satisfy \(\|\beta(x)+x\|\) arbitrarily close to zero, then for every \(a>0\) there is a nonzero projection \(f\) with \(\|f\beta(f)\|<a\).

*Proof.* Write \(x=h+ik\) with \(h,k\) self-adjoint. At least one has norm at least \(1/2\). After normalization and a choice of sign, we obtain a self-adjoint contraction \(b\) with \(1\) in its spectrum and \(\|\beta(b)+b\|<2d\), where \(d>0\) can be arbitrarily small.

Let \(f=1_{[1-d,1]}(b)\), which is nonzero. On \(fH\), \(b\) differs from \(1\) by at most \(d\). On \(\beta(f)H\), \(\beta(b)\) differs from \(1\) by at most \(d\), so \(b\) differs from \(-1\) by at most \(3d\). Thus for \(\xi\in fH\), \(\eta\in\beta(f)H\),
\[
\begin{aligned}
2|\langle\xi,\eta\rangle|
&\leq |\langle(1-b)\xi,\eta\rangle|\\
&\quad +|\langle\xi,(1+b)\eta\rangle|\\
&\leq4d\|\xi\|\|\eta\|.
\end{aligned}
\]
Hence \(\|f\beta(f)\|\leq2d\). Choose \(2d<a\). \(\square\)

**Lemma 2.2 (one small overlap for an outer automorphism).** An outer automorphism \(\beta\) of a finite von Neumann algebra admits such an \(f\) for every \(a>0\).

*Proof.* If \(\beta\) moves a central projection, the abelian algebra generated by that projection and its image contains a nonzero \(f\) with \(f\beta(f)=0\). More generally, a nonidentity automorphism of an invariant abelian algebra admits this conclusion: choose a self-adjoint element it moves, then a spectral projection \(q\) it moves; one of \(q(1-\beta(q))\) and the corresponding inverse-image difference is nonzero and gives a disjoint translate.

We may therefore suppose \(\beta\) fixes the center. Restrict to its nonzero properly outer central summand. If every power is properly outer, the spectral fact above and Lemma 2.1 apply.

Otherwise let \(r\geq2\) be the smallest positive integer for which \(\beta^r\) has a nonzero inner central summand. That summand is \(\beta\)-invariant, since \(\beta\) commutes with \(\beta^r\). Restrict to it and write \(\beta^r=\operatorname{Ad}v\). Then \(\beta(v)=cv\) for a central unitary \(c\), and \(\beta(c)=c\). If \(c\ne1\), \(W^*(v,c)\) is an invariant abelian algebra on which \(\beta\) is nonidentity, giving an exactly disjoint projection.

If \(c=1\), choose by spectral calculus a \(\beta\)-fixed unitary \(w\) with \(w^r=v^*\). Set \(\gamma=\operatorname{Ad}w\circ\beta\). Then \(\gamma^r=\mathrm{id}\); its first \(r-1\) powers remain properly outer. Choose a nonzero spectral projection \(e\) of \(w\) on which \(\|we-\lambda e\|<d\) for some \(\lambda\in\mathbb T\). The corner \(eNe\) is invariant under both automorphisms. The finite cyclic spectral fact gives a unitary eigenvector there. A sufficiently short spectral arc of that eigenvector gives a nonzero \(f\leq e\) with \(f\gamma(f)=0\). On this corner,
\[
\|\gamma(x)-\beta(x)\|\leq2d\|x\|.
\]
Consequently \(\|f\beta(f)\|\leq2d\). Choose \(2d<a\). \(\square\)

**Proposition 2.3 (the local cutting criterion).** For an automorphism \(\beta\) of a finite von Neumann algebra, the following are equivalent:

1. \(\beta\) is properly outer.
2. Every nonzero projection \(q\) contains a nonzero projection \(f\leq q\) with \(\|f\beta(f)\|<a\), for every \(a>0\).
3. In every nonzero corner \(qNq\), positive contractions \(x\) can satisfy \(\|x-\beta(x)\|>1-a\), for every \(a>0\).
4. On every nonzero invariant corner \(eNe\), \(\|\beta_e-\mathrm{id}\|=2\).

*Proof.* Assume proper outerness but suppose the infimum of \(\|f\beta(f)\|\), over nonzero \(f\leq q\), is \(b>0\). Choose \(e\leq q\) with \(\|e\beta(e)\|<b+d\).

The spectrum of \(e\beta(e)e\) lies in \([b^2,(b+d)^2]\). Indeed, if a nonzero spectral projection \(g\leq e\) lay below \(b^2\), then
\[
\|g\beta(g)\|^2=\|g\beta(g)g\|
\leq\|g\beta(e)g\|<b^2,
\]
contradicting the infimum. The same argument applied in \(\beta(e)N\beta(e)\), after transporting subprojections back by \(\beta^{-1}\), shows that \(\beta(e)e\beta(e)\) is invertible there.

The polar decomposition therefore gives
\[
\begin{gathered}
e\beta(e)=h u,\quad uu^*=e,\\
u^*u=\beta(e),\quad \|e\beta(e)-bu\|<d.
\end{gathered}
\]
The automorphism \(\rho(x)=u\beta(x)u^*\) of \(eNe\) is outer. Here is the corner-to-center argument. If \(\rho=\operatorname{Ad}s\), then \(t=s^*u\) intertwines \(\beta(x)\) with \(x\) for \(x\in eNe\), and has initial projection \(\beta(e)\) and final projection \(e\). Their central supports are the same invariant projection \(z\). Choose a maximal family of partial isometries \(r_i\) whose initial projections lie under \(e\), whose final projections are orthogonal and lie under \(z\). Their final projections sum to \(z\): a nonzero remainder would have a nonzero corner against \(e\) by central support, and polar decomposition would enlarge the family. The family may be uncountable; all sums below are strong sums over the net of finite subsets. The strong sum
\[
U=\sum_i r_i t\beta(r_i^*)
\]
is a unitary on \(z\), and \(U\beta(y)U^*=y\) for \(y\in zN\). To check this, expand \(y\) in the matrix coefficients \(r_i^*yr_j\in eNe\) and use the intertwining identity for \(t\). The initial and final projection sums verify unitarity. This would make \(\beta\) inner on \(zN\), contrary to proper outerness.

Lemma 2.2 now supplies \(0\ne f\leq e\) with \(\|f\rho(f)\|<d\). Since \(f\leq e\),
\[
\begin{aligned}
\|f\beta(f)\|
&=\|f e\beta(e)\beta(f)\|\\
&\leq d+b\|fu\beta(f)\|\\
&=d+b\|f\rho(f)\|<(1+b)d.
\end{aligned}
\]
Taking \((1+b)d<b\) is a contradiction. This proves (1) implies (2).

For a nonzero vector \(\xi\in fH\),
\[
\|(f-\beta(f))\xi\|\geq(1-\|f\beta(f)\|)\|\xi\|,
\]
so (2) implies (3). On an invariant corner, apply (3) to \(2x-e\), a contraction, to obtain norm difference arbitrarily close to \(2\); automorphisms have norm one, so the upper bound is \(2\). Thus (3) implies (4).

Finally suppose \(\beta_e=\operatorname{Ad}v\) on a nonzero invariant corner. A nonzero short-arc spectral projection \(q\) of \(v\) is fixed by \(\beta\), and \(v\) is arbitrarily close to a scalar on \(q\). Hence \(\|\beta_q-\mathrm{id}\|<2\), contradicting (4). It also prevents (3) on that \(q\). \(\square\)

For the tower proof, apply (2) successively to \(\alpha,\ldots,\alpha^{m-1}\). It gives a nonzero \(f\) with
\[
\|\alpha^i(f)\alpha^j(f)\|<d\qquad(0\leq i<j<m).
\tag{2.1}
\]
Passing to a smaller projection preserves every previous bound.

## 3. Orthogonalizing a family all at once

**Lemma 3.1 (the Gram operator).** Suppose \(f_0,\ldots,f_{m-1}\) are projections with \(\|f_if_j\|\leq d\) for \(i\ne j\). If \(a=(m-1)d<1\), there are orthogonal projections \(e_j\sim f_j\), with
\[
\sum_j e_j=\bigvee_j f_j,\qquad
\|e_j-f_j\|\leq3a.
\tag{3.1}
\]

*Proof.* On \(K=\bigoplus_j f_jH\), let \(T(\xi_j)=\sum_j\xi_j\). Its Gram operator has identity diagonal and off-diagonal entries \(f_if_j\), so \(\|T^*T-1\|\leq a\). This estimate follows from the scalar matrix bound whose row and column sums are at most \(a\).

Thus \(T^*T\) is invertible. Its polar isometry \(W=T(T^*T)^{-1/2}\) maps \(K\) onto the closed sum of the \(f_jH\). With \(P_j\) the coordinate projections, put \(e_j=WP_jW^*\). These projections belong to \(N\), since the formula uses finite matrices over \(N\) and spectral calculus. They are orthogonal, their sum is the join, and \(WP_j\) gives their equivalence with \(f_j\).

Moreover
\[
\begin{aligned}
\|W-T\|&=\|1-(T^*T)^{1/2}\|\\
&\leq\frac{a}{1+\sqrt{1-a}}\leq a.
\end{aligned}
\]
Because \(TP_jT^*=f_j\),
\[
\|e_j-f_j\|\leq(1+\sqrt{1+a})\|W-T\|\leq3a.
\]
\(\square\)

The Gram argument works in any von Neumann algebra; neither finiteness nor countable decomposability is used in Lemma 3.1.

**Corollary 3.3 (a factorial bound).** For \(0<d<1/m!\), the same conclusion holds with \(\|e_j-f_j\|<m!d\).

*Proof.* For \(m=1\), take \(e_0=f_0\). For \(m=2\), retain the sharper estimate from the proof:
\[
\|e_j-f_j\|\leq
\frac{1+\sqrt{1+d}}{1+\sqrt{1-d}}d<2d,
\]
because \(d<1/2\). For \(m\geq3\), \((m-1)d<1\), and the proof actually gives a bound strictly below \(3(m-1)d\). The elementary inequality \(3(m-1)\leq m!\) finishes the argument. \(\square\)

**Lemma 3.2 (matching close projections).** If \(p,q\) have the same center-valued trace, there is a partial isometry \(v\) with \(v^*v=p\), \(vv^*=q\) and
\[
\|v-q\|_2\leq\|p-q\|_2.
\tag{3.2}
\]

*Proof.* Take the polar partial isometry of \(qp\). Its unmatched initial and final projections have equal center-valued traces, so complete it by a partial isometry between them. For the completed \(v\),
\[
\operatorname{Re}\tau(v)=\tau((pqp)^{1/2})\geq\tau(pqp)=\tau(pq).
\]
The added part has trace zero, since its initial projection is orthogonal to \(q\). Expanding the squares gives
\[
\begin{aligned}
\|v-q\|_2^2&=2\tau(p)-2\operatorname{Re}\tau(v)\\
&\leq2\tau(p)-2\tau(pq)\\
&=\|p-q\|_2^2.
\end{aligned}
\]
The same proof applies to a normalized trace in any finite corner. \(\square\)

## 4. A small exact cycle at a controlled cost

Assume now that \(\alpha\) fixes \(Z(N)\) pointwise. It then preserves the center-valued trace, so a projection and any of its images are equivalent.

**Lemma 4.1 (a nonzero cycle fragment).** For \(n>1\) and \(\delta>0\), there are nonzero orthogonal projections \(g_0,\ldots,g_{n-1}\), all equivalent, and a unitary \(w\in N\), such that, writing \(E=\sum_jg_j\),
\[
w\alpha(g_j)w^*=g_{j+1},\qquad
\|w-1\|_1<\delta\tau(E).
\tag{4.1}
\]

*Proof.* Choose a large multiple \(m=nr\). Use (2.1) and Lemma 3.1 to orthogonalize \(\alpha^j(f)\), \(0\leq j<m\), obtaining \(e_j\), and let
\[
\begin{gathered}
b=3(m-1)d,\\
E=\sum_{j=0}^{m-1}e_j,\qquad F=E\vee\alpha(E).
\end{gathered}
\]
Every \(e_j\) has the same center-valued trace as \(f\). Put \(t=\tau(f)>0\). Then \(\tau(E)=mt\) and \(\tau(F)\leq(m+1)t\): the join \(F\) is generated by \(m+1\) orbit projections.

Work in \(FNF\) with \(\tau_F=\tau/\tau(F)\). For \(j<m-1\),
\[
\|\alpha(e_j)-e_{j+1}\|_{2,F}\leq2b.
\]
Group the projections by residue modulo \(n\):
\[
g_k=\sum_{\ell=0}^{r-1}e_{n\ell+k}\quad(0\leq k<n).
\]
All \(g_k\) have the same center-valued trace. For every \(k\),
\[
\|\alpha(g_k)-g_{k+1}\|_{2,F}
\leq2mb+\frac{2}{\sqrt m}=:\eta.
\tag{4.2}
\]
For \(k<n-1\), sum the adjacent-level bounds. For the final residue class, all but its final term obey the same bound. The remaining two projections each have normalized trace at most \(1/m\), giving the last term of (4.2).

Use Lemma 3.2 to match \(\alpha(g_k)\) to \(g_{k+1}\) by partial isometries \(v_k\) with \(\|v_k-g_{k+1}\|_{2,F}\leq\eta\). Also match \(F-\alpha(E)\) to \(F-E\). Each of these complementary projections has trace at most \(t\), so the corresponding partial isometry \(v_*\) satisfies
\[
\|v_*-(F-E)\|_{2,F}\leq2/\sqrt m.
\]
The sum \(W=\sum_kv_k+v_*\) is a unitary in \(FNF\). Extending by \(1-F\) gives \(w\in N\). It has the required exact permutation and
\[
\begin{aligned}
\|w-1\|_1&\leq\tau(F)\bigl(n\eta+2/\sqrt m\bigr)\\
&\leq2\tau(E)\left(2nmb+\frac{2n+2}{\sqrt m}\right).
\end{aligned}
\]
First choose \(m\) so that \(2(2n+2)/\sqrt m<\delta/2\), then choose \(d\) so small that \(4nmb<\delta/2\). This proves (4.1). \(\square\)

This order of choices is essential. The orbit projection may have tiny trace, so an absolute error estimate alone would not let us fill the algebra with cycle fragments. The cost must be proportional to the fragment's trace.

## 5. Filling the algebra

**Proposition 5.1 (an exact cycle after a small perturbation).** If \(\alpha\) is aperiodic, trace preserving and fixes the center, then for every \(n\) and \(\delta>0\) there are a partition \(p_0,\ldots,p_{n-1}\) of \(1\) and a unitary \(v\) with
\[
v\alpha(p_j)v^*=p_{j+1},\qquad \|v-1\|_1\leq\delta.
\tag{5.1}
\]

*Proof.* The case \(n=1\) is immediate. Consider partial partitions of equivalent projections with a unitary \(v\) satisfying the exact permutation and \(\|v-1\|_1\leq\delta\tau(E)\), where \(E\) is their sum. Order them by enlargement of every projection and the additional requirement
\[
\|v'-v\|_1\leq\delta\tau(E'-E).
\tag{5.2}
\]
The empty partition with \(v=1\) belongs to this ordered set.

Every chain has an upper bound. Trace is strictly increasing whenever the support increases, so a chain has a countable cofinal subsequence, or a largest element. Along that subsequence the projections increase strongly and (5.2) makes the unitaries Cauchy in \(\|\cdot\|_1\). On uniformly bounded sets, \(\|x\|_2^2\leq\|x\|\|x\|_1\). Thus the unitaries and their adjoints converge in \(\|\cdot\|_2\). Their limit is a unitary, because multiplication on bounded sets is continuous for this topology. The permutation and cost inequalities pass to the limit.

Take a maximal element by Zorn's lemma. If \(q=1-E\ne0\), the automorphism \(\beta=\operatorname{Ad}v\circ\alpha\) fixes \(q\). Its restriction to \(qNq\) remains aperiodic and fixes the center of that corner. Indeed, each power is an inner perturbation of the corresponding power of \(\alpha\), and proper outerness is unchanged by such perturbations and invariant-corner restriction.

Apply Lemma 4.1 in this corner with its normalized trace. The resulting cycle fragment enlarges every \(p_j\). Extend its correcting unitary by \(1-q\) and multiply it on the left of \(v\). Its \(\|\cdot\|_1\) cost is at most \(\delta\) times the added support's trace, so the new element satisfies (5.2) and strictly enlarges the old one. This contradicts maximality. Therefore \(E=1\). \(\square\)

Since
\[
\begin{aligned}
\|v\alpha(p)v^*-\alpha(p)\|_2
&\leq2\|v-1\|_2\\
&\leq2\sqrt{2\|v-1\|_1},
\end{aligned}
\tag{5.3}
\]
Proposition 5.1 proves Theorem 1.1 when the center is fixed, by taking \(\delta<\varepsilon^2/8\).

## 6. When the center moves

We first prove the abelian theorem in exactly the generality needed for the center.

**Lemma 6.1 (cyclic partitions of a probability algebra).** Let \(A\) be abelian with a faithful normal tracial state \(\tau\), and let \(\sigma\) be trace preserving and aperiodic. For every \(n\geq1\) and \(m\geq1\), there is a partition \(p_0,\ldots,p_{n-1}\) of \(1\) such that
\[
\|\sigma(p_j)-p_{j+1}\|_2\leq1/\sqrt m.
\tag{6.1}
\]

*Proof.* A properly outer trace-preserving automorphism \(\rho\) of an abelian probability algebra admits an exactly disjoint translate in every nonzero projection \(q\). If \(q\ne\rho(q)\), equal traces ensure \(q(1-\rho(q))\ne0\), and this projection is disjoint from its image. If \(q=\rho(q)\), the restriction cannot be the identity, so choose \(b\leq q\) with \(b\ne\rho(b)\) and use \(b(1-\rho(b))\).

Choose a maximal projection \(B\) such that \(B,\sigma(B),\ldots,\sigma^{m-1}(B)\) are disjoint. Such a maximal projection exists by Zorn's lemma: the join of a chain retains these disjointness relations, since \(\sigma\) preserves joins.

Maximality implies
\[
\bigvee_{k=-(m-1)}^{m-1}\sigma^k(B)=1.
\tag{6.2}
\]
Otherwise the remaining projection contains a nonzero \(C\) whose first \(m\) translates are disjoint, by applying the first paragraph successively to \(\sigma,\ldots,\sigma^{m-1}\). Every cross-product of a translate of \(B\) with a translate of \(C\) is zero because \(C\) avoids the shifts in (6.2). Thus \(B+C\) contradicts maximality.

For \(r\geq1\), let the first-return projection be
\[
B_r=B\,\sigma^{-r}(B)\prod_{l=1}^{r-1}(1-\sigma^{-l}(B)).
\]
The forward nonreturning part \(D_+=B\prod_{l\geq1}(1-\sigma^{-l}(B))\) is wandering: an overlap with a positive translate would give a forward return. Its infinitely many disjoint translates have the same trace, so its trace is zero. Faithfulness makes \(D_+=0\). The backward nonreturning part \(D_-\), defined with \(\sigma^l(B)\), is zero by the same argument for \(\sigma^{-1}\). The return towers
\[
\sigma^i(B_r)\qquad(r\geq m,\ 0\leq i<r)
\]
are disjoint and sum to \(1\). Indeed, if \(i\geq j\), transport an overlap of \(\sigma^i(B_r)\) and \(\sigma^j(B_s)\) by \(\sigma^{-i}\). When \(i>j\), it would place \(B_r\) in \(\sigma^{-(i-j)}(B)\) with \(0<i-j<r\), contrary to its first return. When \(i=j\), the disjoint first-return bases force \(r=s\).

Here is a projection-algebra verification of exhaustion. Put \(H=\bigvee_{r\geq m,\ 0\leq i<r}\sigma^i(B_r)\). Since \(D_+=0\), the bases \(B_r\) sum to \(B\), so \(B\leq H\). Every internal level maps to another level of \(H\), and the top of an \(r\)-tower maps into \(B\). Thus \(\sigma(H)\leq H\). Equal traces and faithfulness imply \(\sigma(H)=H\). It contains every translate of \(B\), and (6.2) makes it \(1\). This argument uses only joins, products and the normal trace; it requires no point-space representation.

Trace preservation now gives
\[
\begin{gathered}
1=\sum_{r\geq m}r\tau(B_r),\\
\tau(B)=\sum_{r\geq m}\tau(B_r)\leq1/m.
\end{gathered}
\tag{6.3}
\]
Group all levels by their residue modulo \(n\):
\[
p_j=\sum_{r\geq m}\ \sum_{\substack{0\leq i<r\\i\equiv j\ ({\rm mod}\ n)}}\sigma^i(B_r).
\]
Away from \(B\), a level and its predecessor belong to successive residue classes. Only returns from tower tops can disagree with cyclic rotation. Thus \(\sigma(p_j)-p_{j+1}\) is supported in \(B\). The difference of two commuting projections has square at most that support projection, so (6.3) proves (6.1). \(\square\)

This proof allows nonseparable \(A\), and it does not require ergodicity. It also explains why varying return heights are harmless: the whole error is confined to the small common base.

Write \(A=Z(N)\) and \(\sigma=\alpha|_A\). Decompose the identity into its central period sectors \(z_1,z_2,\ldots,z_\infty\). On \(z_pA\), \(\sigma\) has exact period \(p\); on \(z_\infty A\), every nonzero power is properly outer. These projections are \(\sigma\)-invariant.

Here is an algebraic construction of the sectors. Let \(q_p\) be the largest projection on whose abelian corner \(\sigma^p\) is the identity. Joins preserve this property, and conjugating by \(\sigma\) shows that \(q_p\) is invariant. Put \(z_p=q_p\prod_{1\leq k<p}(1-q_k)\), and \(z_\infty=1-\bigvee_pq_p\). A point with a smaller period is removed from the later sector. The faithful finite measure makes the nonzero sectors countable.

On a finite-period sector choose \(c\in A\) such that \(c,\sigma(c),\ldots,\sigma^{p-1}(c)\) partition \(z_p\). Such a partition follows by maximal packing of disjoint \(p\)-orbits in the abelian projection lattice. A leftover invariant projection would contain another nonzero disjoint orbit, since no lower power is the identity on a nonzero part of this sector.

The automorphism \(\alpha^p\) of \(cNc\) is aperiodic and fixes its center. The case already proved supplies an approximate \(n\)-cycle \(g_0,\ldots,g_{n-1}\) there. Arrange the \(np\) projections
\[
h_{sp+r}=\alpha^r(g_s)\qquad(0\leq s<n,\ 0\leq r<p)
\]
in their cyclic order. All adjacent moves are exact except the return from the last central level, where the error is the chosen error for \(\alpha^p\). Group indices modulo \(n\):
\[
p_j=\sum_{k=0}^{p-1}h_{kn+j}\qquad(0\leq j<n).
\]
The triangle inequality bounds each error by \(p\) times the error chosen in the \(c\)-corner. That error can be arbitrarily small.

On \(z_\infty\), apply Lemma 6.1 directly to the abelian probability algebra \(z_\infty A\), with its normalized trace and \(m\) so large that \(1/\sqrt m\) is below the desired error. Its projections lie in the center of \(z_\infty N\), so the same partition and estimate apply in that algebra.

Finally use the normalized trace on each nonzero sector and choose the same error bound \(\varepsilon' <\varepsilon\). Take the orthogonal central sums of their partitions. Squared errors add with weights \(\tau(z_p)\), so their sum is below \((\varepsilon')^2\). This finishes the proof of Theorem 1.1. \(\square\)

## 7. Examples and exercises with solutions

**Example 7.1 (an error confined to a boundary).** Consider a measure-preserving tower of height \(12\), with each level of measure \(t\), and ask for a cycle of length \(4\). Group the levels with the same residue modulo \(4\). The transformation carries the first three groups to the next group exactly. The final group differs at only the top and bottom boundary, of total measure at most \(2t\), so its \(L^2\) error is at most \(\sqrt{2t}\). Increasing the tower height makes this boundary small relative to its total measure.

**Exercise 7.2 (introductory: a fixed summand).** On \(\mathbb C\oplus L^\infty(\mathbb T)\), let an automorphism fix the first summand and act by irrational rotation on the second. Give both summands positive trace weight. Is the automorphism outer? Properly outer? Can its first summand admit a two-part cyclic partition with arbitrarily small error?

*Solution.* It is outer because the algebra is abelian and the rotation is nonidentity. It is not properly outer, since it is the identity on the first summand. On that summand the only two-part partitions are \((1,0)\) and \((0,1)\); the two projections differ by norm one. The global error is therefore bounded below by the square root of that summand's trace weight.

**Exercise 7.3 (intermediate: a Gram estimate).** If there are \(5\) projections and their pairwise products have norm at most \(10^{-4}\), give the bound from Lemma 3.1 for each orthogonalized projection.

*Solution.* Here \(a=4\cdot10^{-4}<1\). Equation (3.1) gives \(\|e_j-f_j\|\leq3a=0.0012\). This is an operator-norm bound; it does not depend on any projection's trace.

**Exercise 7.4 (intermediate: why the trace cost is weighted).** Suppose disjoint fragments have traces \(t_i\), with \(\sum_i t_i=1\). Compare correction bounds \(\|w_i-1\|_1\leq\delta\) and \(\|w_i-1\|_1\leq\delta t_i\).

*Solution.* The first gives only \(\delta\) times the number of fragments, which may be infinite. The second gives a total at most \(\delta\sum_i t_i=\delta\), even for countably many fragments. This summable bound is what the maximal-chain construction uses.

**Exercise 7.5 (advanced: a periodic obstruction).** Suppose \(\alpha^r=\mathrm{id}\), and a partition of \(1\) into \(n\) projections is rotated exactly by \(\alpha\). Show that if \(n\) does not divide \(r\), such a partition cannot have all projections nonzero.

*Solution.* Exact rotation gives \(p_j=\alpha^r(p_j)=p_{j+r}\). If \(r\) is nonzero modulo \(n\), these are distinct members of an orthogonal partition. Equality then forces \(p_j=0\) for every \(j\), contradicting their sum being \(1\). Thus exact rotation of a nonzero partition requires \(n\mid r\).

**Exercise 7.6 (advanced: quantitative central gluing).** On orthogonal invariant central sectors \(z_i\), suppose \(\|\alpha(p_{i,j})-p_{i,j+1}\|_{2,i}\leq b_i\) for the normalized trace. Show that \(p_j=\sum_i p_{i,j}\) has squared error at most \(\sum_i\tau(z_i)b_i^2\).

*Solution.* Distinct central sectors multiply to zero. Hence the square of the error is the sum of the squares of its sector components. Applying \(\tau\) and using normality gives
\[
\begin{gathered}
\|\alpha(p_j)-p_{j+1}\|_2^2\\
=\sum_i\tau(z_i)\|\alpha(p_{i,j})-p_{i,j+1}\|_{2,i}^2\\
\leq\sum_i\tau(z_i)b_i^2.
\end{gathered}
\]
This proves the assertion for finite or countable sums.

## References

[Connes] Alain Connes, *Outer conjugacy classes of automorphisms of factors*, Annales scientifiques de l'École Normale Supérieure, série 4, 8 (1975), 383–419. [Article and original text](https://numdam.org/articles/10.24033/asens.1295/).

[Connes 1973] Alain Connes, *Une classification des facteurs de type III*, Annales scientifiques de l'École Normale Supérieure, série 4, 6 (1973), 133–252. [Article and original text](https://numdam.org/articles/10.24033/asens.1247/). The maximal inner summand and the general action-spectrum facts are distinguished from the elementary discrete argument above.

[Connes–Takesaki] Alain Connes and Masamichi Takesaki, *The flow of weights on factors of type III*, Tohoku Mathematical Journal 29 (1977), 473–575. [Part 1](https://www.jstage.jst.go.jp/article/tmj1949/29/4/29_4_473/_article/-char/en), [Part 2 and free original PDF](https://www.jstage.jst.go.jp/article/tmj1949/29/4/29_4_524/_article/-char/en). The consumed result is Section IV, Theorem 3.2 and Lemma 3.3. The [1978 errata](https://www.jstage.jst.go.jp/article/tmj1949/30/4/30_4_653a/_article/-char/en) contain no correction on those two pages.

[OA-APPROX] *Central sequence algebras and exact lifts*, Theorems 3.1, 5.1 and 6.1 (pinned source). This is the current construction provider for the later centralizer application; its stated functional-analytic and projection prerequisites remain in force.
