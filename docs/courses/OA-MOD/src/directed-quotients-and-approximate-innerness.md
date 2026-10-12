# Directed quotients and approximate innerness

A faithful normal state need not give a separable predual. The distinction matters when infinitely many normal functionals must be controlled at once: a net of approximate intertwiners cannot simply be replaced by a sequence. We construct the finite quotient for a directed family and use it to prove the local criterion for approximate innerness in every type III factor that has a faithful normal state.

We use the local estimates LC01–06, the net with a fixed positive mass from GI04–05, and the functional-to-vector estimate AI04. The pointwise projection comparison and unitary replacement are proved in IU04–05. We will specify why those two arguments do not require a sequence. For the quotient we use only the faithful-state metric criterion and the finite-algebra completeness criterion, Sections 1–2; the directed completeness argument is given below.

For a normal functional \(\rho\), our conventions are \((x\rho)(a)=\rho(ax)\), \((\rho x)(a)=\rho(xa)\), and \([x,\rho]=x\rho-\rho x\). In standard form we write \(\xi x=Jx^*J\xi\), \(\theta\rho=\rho\circ\theta^{-1}\), and \(\theta\xi=U_\theta\xi\).

## 1. A cofinal ultrafilter with an unbounded integer coordinate

Let \(M\) be a type III factor with faithful normal state \(\varphi_0\). The local condition on \(\theta\in\operatorname{Aut}(M)\) is that for every finite family \(\xi_1,\ldots,\xi_r\) in the natural cone and every \(\varepsilon>0\), some \(x\ne0\) satisfies

\[
\sum_{j=1}^r\|x\xi_j-(\theta\xi_j)x\|^2
\le\varepsilon^2\sum_{j=1}^r\|x\xi_j\|^2.
\tag{DQI.1}
\]

The version with an individual squared error on the left is equivalent: apply that version with tolerance \(\varepsilon^2/r\) and sum. A family of zero vectors causes no difficulty.

Put \(\mathcal D=\{\rho\in M_*^+:\rho\le C\varphi_0\text{ for some finite }C\}\). GI04 proves its norm density in \(M_*^+\). GI05 constructs contractions indexed by

\[
I=\{(F,m):F\subset\mathcal D\setminus\{0\}\text{ finite},\ m\in\mathbb N_{\ge1}\},
\qquad (F,m)\le(G,n)\iff F\subset G\text{ and }m\le n,
\]

such that, writing \(h(F,m)=m\),

\[
\|y_i\rho-(\theta\rho)y_i\|\longrightarrow0\quad(\rho\in M_*),
\qquad \varphi_0(y_i^*y_i)\ge\delta:=1/38400.
\tag{DQI.2}
\]

The convergence here is ordinary convergence of a net. In particular it holds along any ultrafilter containing every tail of \(I\).

Such an ultrafilter \(\mathcal U\) exists. Finite intersections of tails contain a tail, so they generate a proper filter. Order the proper filters containing it by inclusion. The union of a chain is again proper and a filter, so Zorn's lemma gives a maximal one. If neither a set \(A\) nor its complement belongs to it, adjoining \(A\) must make the filter improper, which means an existing filter set is disjoint from \(A\). Its complement therefore already belongs to the filter, a contradiction. The maximal filter is an ultrafilter.

For every integer \(n\), \(\{i:h(i)\ge n\}\in\mathcal U\), and these sets have empty intersection. This explicit countable incompleteness, rather than countability of the entire index set, will permit a diagonal construction. Bounded complex families have ultralimits: compactness of a closed disk gives a cluster point for the ultrafilter, and two distinct cluster points would give disjoint members of the filter. Uniqueness and continuity of addition and multiplication give their usual limit rules.

## 2. The single-state quotient is a tracial C*-algebra

For this section let \(N\) be any von Neumann algebra with faithful normal state \(\psi\). Use the same \(I,\mathcal U,h\), and define the normalized seminorm

\[
q_\psi(a)^2=\tfrac12\bigl(\psi(a^*a)+\psi(aa^*)\bigr).
\]

In the C*-algebra of bounded families in \(N\), put

\[
\mathcal A_\psi=\{X=(X_i):\lim_{\mathcal U}\|[X_i,\psi]\|=0\},
\qquad
\mathcal J_\psi=\{X:\lim_{\mathcal U}q_\psi(X_i)=0\}.
\tag{DQI.3}
\]

The faithful-state metric criterion identifies the latter condition with bounded strong* convergence to zero along \(\mathcal U\). The product rule for the commutator and \(\|[a^*,\psi]\|=\|[a,\psi]\|\) show that \(\mathcal A_\psi\) is a norm-closed unital C*-algebra. Cauchy–Schwarz gives

\[
\|a\psi\|\le\psi(a^*a)^{1/2},\qquad
\|\psi a\|\le\psi(aa^*)^{1/2},\qquad
\|[a,\psi]\|\le2q_\psi(a),
\tag{DQI.4}
\]

so \(\mathcal J_\psi\subset\mathcal A_\psi\).

We check the ideal property inside \(\mathcal A_\psi\); no ideal property in the entire bounded-family algebra is presumed. If \(X\in\mathcal A_\psi\), \(Y\in\mathcal J_\psi\), and \(K=\sup_i\|X_i\|\), \(L=\sup_i\|Y_i\|\), then

\[
\psi((X_iY_i)^*X_iY_i)\le K^2\psi(Y_i^*Y_i).
\]

For the other quadratic expression, moving one \(X_i\) across \(\psi\) incurs at most \(KL^2\|[X_i,\psi]\|\), and Cauchy–Schwarz gives

\[
\begin{aligned}
\psi(X_iY_iY_i^*X_i^*)
&\le KL^2\|[X_i,\psi]\|+
       |\psi(Y_iY_i^*X_i^*X_i)|\\
&\le KL^2\|[X_i,\psi]\|+
       K^2L\,\psi(Y_iY_i^*)^{1/2}\longrightarrow0.
\end{aligned}
\tag{DQI.5}
\]

Thus \(XY\in\mathcal J_\psi\). Taking adjoints proves \(YX\in\mathcal J_\psi\). Linearity, adjoint closure and norm closure follow directly from the seminorm definition. Hence \(R_\psi=\mathcal A_\psi/\mathcal J_\psi\) is a unital C*-algebra.

Define \(\tau([X])=\lim_{\mathcal U}\psi(X_i)\). Cauchy–Schwarz makes this well defined, and positivity and normalization descend from \(\psi\). For bounded \(Y\),

\[
|\psi(X_iY_i)-\psi(Y_iX_i)|
\le\|[X_i,\psi]\|\|Y_i\|,
\]

so \(\tau\) is tracial. If \(\tau([X]^*[X])=0\), then also \(\lim_{\mathcal U}\psi(X_iX_i^*)=0\), since the difference is bounded by \(K\|[X_i,\psi]\|\). Thus \(X\in\mathcal J_\psi\); \(\tau\) is faithful. In particular,

\[
\|[X]\|_{2,\tau}=
\lim_{\mathcal U}q_\psi(X_i).
\tag{DQI.6}
\]


## 3. Completing the unit ball without enumerating the tests

Every contraction in \(R_\psi\) has a contractive representative. Starting with any representative \(X\), replace it by \(Xg(X^*X)\), where \(g(t)=1\) for \(0\le t\le1\) and \(g(t)=t^{-1/2}\) for \(t\ge1\). Continuous functional calculus keeps it in \(\mathcal A_\psi\), makes it contractive, and leaves its quotient unchanged.

Let a sequence in the unit ball of \(R_\psi\) be Cauchy for \(\|\cdot\|_{2,\tau}\). Choose a subsequence \(a_n\) with \(\|a_{n+1}-a_n\|_{2,\tau}\le4^{-n}\), and choose contractive lifts \(X^n\). For each \(n\), take the intersection of the following finitely many sets, and intersect with the preceding choices to make the resulting sets \(K_n\) decreasing:

\[
\begin{gathered}
\{i:h(i)\ge n\},\qquad
\{i:\|[X_i^j,\psi]\|\le1/n\}\quad(1\le j\le n),\\
\{i:q_\psi(X_i^{j+1}-X_i^j)\le2^{-j}\}\quad(1\le j<n).
\end{gathered}
\tag{DQI.7}
\]

All are members of \(\mathcal U\), by (DQI.6) and the strict inequality \(4^{-j}<2^{-j}\). Define

\[
k(i)=\max\{n\le h(i):i\in K_n\},
\qquad Z_i=X_i^{k(i)},
\tag{DQI.8}
\]

with \(k(i)=0\) and \(Z_i=0\) when the set is empty. The maximum is finite. Since \(K_n\subset\{i:k(i)\ge n\}\), we have \(k(i)\to\infty\) along \(\mathcal U\). On \(k(i)>0\), the commutator of \(Z_i\) has norm at most \(1/k(i)\); hence \(Z\in\mathcal A_\psi\).

For \(k(i)\ge n\), membership in \(K_{k(i)}\) permits telescoping all the intervening differences:

\[
q_\psi(Z_i-X_i^n)
\le\sum_{j=n}^{k(i)-1}2^{-j}\le2^{1-n}.
\tag{DQI.9}
\]

Thus the contraction \([Z]\) is the \(2\)-norm limit of \(a_n\), and the original Cauchy sequence has the same limit. The closed unit ball is complete. Proposition 2.1 of the earlier ultraproduct lesson now makes \(R_\psi\) a finite von Neumann algebra and \(\tau\) a faithful normal trace. That proposition applies to an arbitrary C*-algebra: it uses bounded strong approximation in the trace GNS representation and the bounded right multiplications to identify the strong closure. It has no separability assumption.

Only a sequence of approximations to one element was diagonalized. The set of normal-functional tests, and the original directed set \(I\), have not been replaced by countable sets.

## 4. A finite quotient imposing all normal-functional tests

Return to \(M,\theta,\varphi_0\). On \(N=M_2(M)\), put

\[
\begin{aligned}
\Psi_\rho(A)&=\rho(A_{11})+(\theta\rho)(A_{22}),
\qquad \psi=\tfrac12\Psi_{\varphi_0},\\
\mathcal A_D&=\bigcap_{\rho\in M_*^+}
\{X:\lim_{\mathcal U}\|[X_i,\Psi_\rho]\|=0\}.
\end{aligned}
\tag{DQI.10}
\]

The state \(\psi\) is faithful. The algebra \(\mathcal A_D\) is a unital C*-subalgebra of \(\mathcal A_\psi\). Strong*-null bounded families centralize every normal positive functional by Cauchy–Schwarz, so \(\mathcal J_\psi\subset\mathcal A_D\). We may therefore view \(Q=\mathcal A_D/\mathcal J_\psi\) as a C*-subalgebra of \(R_\psi\).

Its unit ball is \(2\)-norm closed. Indeed, suppose contractions \([Y^n]\in Q\) converge to a contraction \([X]\in R_\psi\), and use contractive lifts. If \(\rho\le C\varphi_0\), then \(\Psi_\rho\le2C\psi\). For \(Z=X-Y^n\), Cauchy–Schwarz and (DQI.6) give

\[
\lim_{\mathcal U}\|[Z_i,\Psi_\rho]\|
\le2\sqrt{2C\Psi_\rho(1)}\,\|[Z]\|_{2,\tau}.
\tag{DQI.11}
\]

Letting \(n\to\infty\) shows that \(X\) centralizes every such \(\Psi_\rho\). For arbitrary \(\rho\ge0\), use the norm density of \(\mathcal D\) from GI04 and

\[
\|[X_i,\Psi_\rho-\Psi_\sigma]\|
\le4\|\rho-\sigma\|.
\tag{DQI.12}
\]

It follows that \(X\in\mathcal A_D\). The completeness criterion applies again: \(Q\) is a finite von Neumann algebra with faithful normal trace \(\tau\).

Let \(E,F\) be the classes of the constant upper and lower diagonal matrix units. Both diagonal corners identify with

\[
\begin{aligned}
C={}&\{(a_i):\lim_{\mathcal U}\|[a_i,\rho]\|=0
                 \text{ for all }\rho\in M_*^+\}\\
 &/\{\text{bounded strong*-null families in }M\}.
\end{aligned}
\tag{DQI.13}
\]

Write these identifications as \(\iota_1:C\to EQE\) and \(\iota_2:C\to FQF\). The automorphism \(\theta\) permutes the tests and preserves strong* nullity, so it induces \(\bar\theta\) on \(C\).

Every projection \(e\in C\) has projection representatives \(e_i\). First lift it to positive contractions \(a_i\). The defect \(a_i-a_i^2\) is strong*-null, and the scalar inequality

\[
|1_{[1/2,1]}(a_i)-a_i|\le2(a_i-a_i^2)
\]

shows the spectral projections differ from \(a_i\) by a strong*-null family. Cauchy–Schwarz keeps them in the numerator of (DQI.13). This also verifies directly that the projection-lifting argument of IU03 is independent of the index set.

## 5. Reindexing a net to obtain a nonzero corner link

Set \(b_i=y_i^*y_i\) using (DQI.2). For \(\rho\ge0\),

\[
[b_i,\rho]
=y_i^*\bigl(y_i\rho-(\theta\rho)y_i\bigr)
 +\bigl(y_i^*(\theta\rho)-\rho y_i^*\bigr)y_i.
\tag{DQI.14}
\]

Thus \(b_i\) centralizes every normal functional asymptotically. Its ultraweak ultralimit exists because \(M=(M_*)^*\): evaluate each normal functional and take its scalar ultralimit. It is a positive contraction commuting with every element of \(M\). Since \(M\) is a factor, this limit is \(\lambda1\), with \(\lambda\ge\delta\).

AI04 applied to (DQI.2) gives \(y_i\xi-(\theta\xi)y_i\to0\) for every cone vector. The cone has dense complex span, and the operators are uniformly bounded, so this holds for every \(\xi\in H\). Comparing the formula for \(a\xi\) with the formula for \(\xi\) multiplied on the left by \(\theta(a)\) gives

\[
(y_i a-\theta(a)y_i)\xi\longrightarrow0
\qquad(a\in M,\ \xi\in H).
\tag{DQI.15}
\]

Here \(a\) is fixed; the equation alone says nothing uniform about a varying projection.

Let \(0\ne e\in C\) be a projection, with projection lifts \(e_i\). Faithfulness of the quotient trace gives \(t=\lim_{\mathcal U}\varphi_0(e_i)>0\). For each fixed \(i\), choose \(j(i)\ge i\) satisfying

\[
\begin{aligned}
\varphi_0(e_i b_{j(i)}e_i)&\ge\lambda\varphi_0(e_i)-1/h(i),\\
\|(1-\theta(e_i))y_{j(i)}e_i\xi_{\varphi_0}\|&<1/h(i).
\end{aligned}
\tag{DQI.16}
\]

This choice exists: the first requirement holds on a member of \(\mathcal U\) by the ultraweak limit with the fixed test \(a\mapsto\varphi_0(e_i a e_i)\). The second holds on a tail by (DQI.15) with \(a=e_i\), since \((1-\theta(e_i))\theta(e_i)=0\). Intersect these sets with the tail \(j\ge i\).

Put \(z_i=\theta(e_i)y_{j(i)}e_i\). Its mass satisfies

\[
\varphi_0(z_i^*z_i)\ge\lambda\varphi_0(e_i)-3/h(i),
\qquad \lim_{\mathcal U}\varphi_0(z_i^*z_i)\ge\lambda t>0.
\tag{DQI.17}
\]

Indeed, the compressed and uncompressed vectors have norm at most one and differ by less than \(1/h(i)\), so their squared norms differ by at most \(2/h(i)\). The bimodule product rule gives

\[
\|z_i\rho-(\theta\rho)z_i\|
\le2\|[e_i,\rho]\|
 +\|y_{j(i)}\rho-(\theta\rho)y_{j(i)}\|.
\tag{DQI.18}
\]

The first term vanishes along \(\mathcal U\). The second vanishes as an ordinary net, because \(j(i)\ge i\): once \(i\) lies beyond a tail threshold, so does \(j(i)\). Monotonicity of the map \(i\mapsto j(i)\) is unnecessary.

The lower off-diagonal matrix with entry \(z_i\) therefore belongs to \(\mathcal A_D\). Testing its functional commutator on an upper off-diagonal matrix shows that its norm is exactly the defect in (DQI.18). By (DQI.17), its class is nonzero. We have proved

\[
\iota_2(\bar\theta(e))\,Q\,\iota_1(e)\ne\{0\}
\qquad(0\ne e\in\operatorname{Proj}(C)).
\tag{DQI.19}
\]


## 6. Comparison on every central summand

We give the comparison step to make its lack of countability assumptions explicit. A central projection \(Z\) of \(Q\) commutes with \(E\), so it is diagonal, say \(Z=\iota_1(a)+\iota_2(b)\), with \(a,b\) central projections of \(C\). If \(e=a(1-\bar\theta^{-1}(b))\ne0\), (DQI.19) gives a nonzero link \(W\) with \(WZ=W\) and \(ZW=0\), a contradiction. Applying the same argument to \((1-a)\bar\theta^{-1}(b)\) gives the reverse inclusion. Hence \(b=\bar\theta(a)\).

Projection lifts of \(a\) now give

\[
\tau(ZE)=\tfrac12\lim_{\mathcal U}\varphi_0(a_i)
 =\tfrac12\lim_{\mathcal U}(\theta\varphi_0)(\theta(a_i))
 =\tau(ZF).
\tag{DQI.20}
\]

Apply the projection comparison theorem as in IU04: on a central summand where \(ZE\precsim ZF\), a partial isometry has initial projection \(ZE\) and final projection at most \(ZF\). The remaining projection has trace zero by (DQI.20), hence is zero. On the complementary central summand compare in the reverse direction and take the adjoint. The sum gives

\[
V\in FQE,\qquad V^*V=E,\qquad VV^*=F.
\tag{DQI.21}
\]

This uses central comparison for a von Neumann algebra and a faithful trace. Neither the algebra nor its center needs a separable predual.

## 7. Unitary representatives and the full faithful-state criterion

Lift \(V\) to a lower off-diagonal family and apply the radial continuous functional calculus from Section 3. This gives contractions \(x_i\in M\) with

\[
\begin{gathered}
\|x_i\rho-(\theta\rho)x_i\|\longrightarrow_{\mathcal U}0
\quad(\rho\in M_*),\\
1-x_i^*x_i\longrightarrow_{\mathcal U}0,
\qquad1-x_ix_i^*\longrightarrow_{\mathcal U}0
\quad\text{strongly*}.
\end{gathered}
\tag{DQI.22}
\]

The second line is precisely the lifted pair of quotient identities in (DQI.21).

Use the pointwise unitary replacement lemma proved in IU05, with faithful states \(\varphi_0,\theta\varphi_0\) and tolerance \(1/h(i)\). Its hypotheses require countable decomposability of \(M\), which follows from the faithful state: a family of orthogonal nonzero projections has positive state values with bounded finite sums, and is therefore countable. No separable predual is used in that lemma. For clarity, its construction takes the polar isometry of \(x_i\) and fills its complementary supports by a partial isometry. If just one complement is zero, it first removes a nonzero subprojection of arbitrarily small mass for both relevant states; splitting a nonzero type III projection into infinitely many orthogonal nonzero projections supplies such a subprojection. Both complements are then nonzero and equivalent. IU05 proves the resulting bounds in the two state seminorms.

Consequently there are unitaries \(u_i\) with \(u_i-x_i\to0\) strongly* along \(\mathcal U\). Specifically, the two seminorm errors are bounded by terms tending to zero with the two deficits in (DQI.22) and the chosen tolerance. The faithful-state metric criterion converts these bounds into strong* convergence for all normal-functional tests. Cauchy–Schwarz then gives, for every \(\rho\in M_*\),

\[
\|u_i\rho-(\theta\rho)u_i\|\longrightarrow_{\mathcal U}0.
\tag{DQI.23}
\]

For positive \(\rho\) this follows by bounding each multiplication by \(u_i-x_i\) in its corresponding state seminorm; four positive parts give the general case. Right multiplication by \(u_i^*\) is isometric on the predual, so (DQI.23) says

\[
\|\rho\circ\operatorname{Ad}(u_i^*)-\theta\rho\|
\longrightarrow_{\mathcal U}0.
\tag{DQI.24}
\]

Every finite set of these tests, at any positive tolerance, holds on an intersection of members of \(\mathcal U\), hence at some index. Therefore \(\theta\) lies in the point-norm predual closure of the inner automorphisms. If an ordinarily convergent implementing net is desired, index by finite subsets of \(M_*\) and positive inverse-integer tolerances, and select one such unitary for each neighborhood. Directed inclusion and decreasing tolerance give ordinary convergence. No assertion about an implementing sequence has been made.

Conversely, an approximately inner automorphism satisfies (DQI.1) by the canonical standard-form implementation and the net argument of LC04: unitaries preserve each denominator \(\|x\xi_j\|=\|\xi_j\|\), and their vector intertwining errors tend to zero. We have proved:

**Theorem.** For a type III factor with a faithful normal state, the local condition (DQI.1) is equivalent to approximate innerness. A separable predual is not required.

## 8. The scope of the criterion and the source comparison

The faithful-state assumption cannot simply be removed from this argument. GI06 proves that in a factor without a faithful normal state the bare local condition holds for every automorphism: the joint support of any finite family of positive normal functionals is a proper projection, and a nonzero element in the two complementary corners annihilates all the test vectors on both sides. This observation makes the local test vacuous in that setting; it does not assert that every automorphism there is approximately inner, nor provide such a classification.

The source comparison is with M. Takesaki, *Theory of Operator Algebras III*, Chapter XVIII, §4, Theorem 4.7 and Lemmas 4.8–4.11, pp. 371–380. The theorem's headline says “type III factor,” while the proof fixes a faithful normal state and explicitly uses separability of the standard Hilbert space to obtain a sequence. The present theorem supplies the directed construction under the faithful-state hypothesis and keeps the wider unqualified statement separate.

The companion lessons retain the remaining quantitative and logical details. LC01–02 prove the common spectral-cut bounds with constant \(200\); LC03–05 give polar localization and the mass bound \(1/(64\cdot200)\), including the zero-mass case. LC06 uses an aggregate matrix-entry estimate when passing to a fixed corner, with its projection-equivalence hypothesis stated explicitly. GI01–05 supply the orthogonal-block assembly, its countable limit stages, and a net whose mass in one fixed faithful state is at least \(1/38400\). Sections 2–7 above prove that this net suffices for the final comparison and unitary approximation. Thus no separability is hidden in a selection of a subsequence.
