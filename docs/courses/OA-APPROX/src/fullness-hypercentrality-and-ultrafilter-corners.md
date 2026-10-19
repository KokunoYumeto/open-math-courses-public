# Fullness, hypercentrality and ultrafilter corners

*Written by GPT-6.1 Sol (OpenAI), Ultra. Course exposition: CC0-1.0 to the extent of rights held. Earlier programme and human-source notices retain their own terms.*

A noncommuting pair does not tell us what happens in every corner of an algebra. Nor does type \(\mathrm{II}_1\) imply a scalar center. We begin by separating those questions, then use the dyadic tensor factor to show how a tail unitary detects distance from the scalars. The final argument carries a commutator into any chosen nonzero corner of a general central sequence algebra.

Throughout the general-factor arguments, \(M\) is a nonzero factor with separable predual, \(\varphi\) is a faithful normal state, and \(\omega\) is a free ultrafilter on \(\mathbb N\). The [preceding quotient and lifting lesson](central-sequence-algebras-and-exact-lifts.md) constructs \(C_\omega,J_\omega,T_\omega,M_\omega,\pi_\omega,\tau_\omega\), with a faithful normal quotient trace and exact projection lifts. Its seminorm is
\[
\|x\|_{\varphi,\#}^2=\frac{\varphi(x^*x)+\varphi(xx^*)}{2}.
\]
The complete [FH0–5 inputs](../components/fullness-hypercentrality-and-tail-inputs.md) prove trace normality on finite factors, division with the full center retained, unitary displacement, the exact tail map, the nonfactor example, and multiplication estimates for strongly*-zero perturbations.

Scalar-trivial means approaching a bounded scalar sequence strongly*. Hypercentral means commuting strongly* asymptotically with every other bounded centralizing sequence. We fix a countable norm-dense family \((\psi_j)\) of normal states for the general selection arguments. Such a family exists: the separable norm metric of \(M_*\) has a countable base; selecting one state in each nonempty intersection of a basic ball with the state space gives a countable dense family. The normal state space is nonempty because it contains \(\varphi\).

<a id="6-exercises-with-complete-solutions"></a>

## What type does, and does not, say about the center

An abelian projection is one whose corner is commutative. A finite von Neumann algebra is type \(\mathrm{II}_1\) when its abelian part is absent; it can still have a nontrivial center. FH1 constructs this part from central supports and proves the full projection-halving result without a factor or countability assumption.

**Exercise 4.** Exhibit a finite algebra with a noncommuting pair and a nonzero abelian projection. Explain why one noncommuting pair cannot establish type \(\mathrm{II}_1\).

*Solution.* Take \(N=M_2(\mathbb C)\oplus\mathbb C\). Matrix units \(e_{12},e_{21}\) in the first summand have commutator \(e_{11}-e_{22}\ne0\). But the projection \(p=(0,1)\) has corner \(pNp=\mathbb C p\), which is abelian. The algebra is finite because an isometry is a unitary in each of its two finite matrix summands. A noncommuting pair somewhere in \(N\) therefore does not exclude an abelian corner elsewhere. Theorem 4.1 will construct a noncommuting pair inside every prescribed nonzero corner; that is the stronger statement needed to exclude the entire abelian part.

**Exercise 7.** Give a finite type \(\mathrm{II}_1\) algebra with nontrivial center. One candidate is \(L^\infty([0,1])\bar\otimes R\) with its product trace.

*Solution.* Use Lebesgue measure \(\lambda\) and the dyadic factor's normalized trace \(\tau\). FH4 constructs the multiplication algebra \(A=L^\infty([0,1])\) on \(L^2(\lambda)\), proves \(A'=A\), and constructs the spatial product \(N=A\bar\otimes R\) with its faithful normal normalized trace
\[
\tau_N(M_f\otimes b)=\left(\int_0^1 f\,d\lambda\right)\tau(b).
\]
It proves \(Z(N)=A\otimes1\) by compressing a central operator between first-leg vectors: each resulting second-leg operator commutes with both \(R\) and \(R'\), hence is scalar. The bounded scalar form reconstructs a first-leg multiplier. The characteristic function of \([0,1/2]\) supplies a central projection of trace \(1/2\), so this center is nontrivial.

Here is the type check in the same full construction. If \(p\) were a nonzero abelian projection, FCT3 would give a nonzero central \(w\) filled by \(k\) equivalent copies of \(pw\), for a finite \(k\). Its center-valued trace would be \(w/k\). A unital dyadic matrix stage of size \(d>k\), compressed by \(w\), has equivalent diagonal cells of center-valued trace \(w/d\). FCT7 comparison places one under \(pw\). PC4 makes such a subprojection \(pwt\) for a central projection \(t\leq w\), forcing \(t/k=w/d\). The element \((k/d)w\) is not a projection, a contradiction. Thus \(N\) has no nonzero abelian projection and is type \(\mathrm{II}_1\). This example distinguishes type from factoriality; it does not claim that this particular product is a central sequence algebra. FH4 includes the complete measure, Hilbert, trace, center and comparison proofs.

<a id="5-the-center-of-the-hyperfinite-central-sequence-algebra"></a>

## A tensor-tail unitary detects nonscalar mass

Let \(R\) be the complete dyadic model of FG2, with
\[
R=\overline{\bigotimes_{j\geq1}}(M_2,\operatorname{tr}_2),
\qquad D_r=\bigotimes_{j=1}^rM_2,\qquad N_r=D_r'\cap R.
\tag{12}
\]
FH3 proves that \(N_r\) is exactly the remaining tensor tail and is normally trace-preservingly isomorphic to \(R\). It is therefore a type \(\mathrm{II}_1\) factor. For matrix units \((e_{ij})\) of \(D_r\), \(d=2^r\), the exact normal unital completely positive map onto this tail is
\[
E_r(x)=\frac1d\sum_{i,j=1}^d e_{ij}x e_{ji},\qquad
E_r(x)-x=\frac1d\sum_{i,j}e_{ij}[x,e_{ji}].
\]
It preserves the trace and contracts the trace \(2\)-norm. Each displayed difference is a finite sum of fixed-multiplier commutators. Hence for a bounded centralizing sequence,
\[
\|E_r(a_n)-a_n\|_{2,\tau}\longrightarrow0
\tag{13}
\]
in the ordinary or ultrafilter sense being used, for each fixed \(r\). There is no Haar-average prerequisite in this formula.

**Lemma 5.1.** If \(N\) is a finite factor with faithful normalized trace and \(\tau(b)=0\), there is a unitary \(u\in N\) such that
\[
\|b-ubu^*\|_2\ge\frac12\|b\|_2.
\tag{14}
\]

**Proof.** FH0 first proves that the specified normalized trace is the canonical normal trace; normality need not be added to the statement. Take the ultraweakly closed convex hull \(K\) of the unitary orbit of \(b\). It is compact inside its fixed operator-norm ball by CP/CF's complete compact-ball proof.

The trace norm is ultraweakly lower semicontinuous because
\[
\|x\|_2=\sup_{\|d\|_2\leq1,\ d\in N}|\tau(d^*x)|.
\]
Schwarz gives one inequality and \(d=x/\|x\|_2\) gives equality when \(x\ne0\). Each scalar pairing is normal. Nested closed sublevel sets in compact \(K\) give a minimizer; the parallelogram identity makes it unique, as Exercise 8 checks. Every unitary conjugation preserves \(K\) and its trace norm, so it fixes this minimizer. The four-unitary decomposition makes the minimizer central; factoriality makes it scalar. All points in \(K\) have trace zero by normality, so the minimizer is zero.

For \(b\ne0\), failure of (14) for every unitary would put the orbit in the closed trace ball of radius \(\|b\|_2/2\) about \(b\). This ball is convex and ultraweakly closed by the same scalar formula. It would contain \(K\), hence zero, whose distance from \(b\) is \(\|b\|_2\), a contradiction. At \(b=0\), the identity unitary works. FH2 supplies the whole compactness and scalar-functional argument. \(\square\)

**Exercise 8.** Prove uniqueness of the point of smallest trace \(2\)-norm in the compact convex set used in Lemma 5.1.

*Solution.* Suppose \(x,y\in K\) both have the minimal norm \(m\). Their midpoint is in \(K\). Expanding its Hilbert square gives
\[
\left\|\frac{x+y}{2}\right\|_2^2
=\frac{\|x\|_2^2+\|y\|_2^2}{2}-\frac{\|x-y\|_2^2}{4}
=m^2-\frac{\|x-y\|_2^2}{4}.
\]
If \(x\ne y\), trace faithfulness makes the last subtracted term strictly positive, contradicting minimality. Thus \(x=y\). Existence is supplied separately by the compact sublevel argument, so uniqueness does not presume a Hilbert projection theorem for this convex set.

**Theorem 5.2.** Every ordinary hypercentral sequence in \(R\) is scalar-trivial. For every free ultrafilter, \(R_\omega\) is a factor of type \(\mathrm{II}_1\).

**Proof.** FH3 gives finite matrix witnesses for scalar distance. In its notation, \(\Gamma_r\) is the family of finite Pauli words in the tensor legs after \(r\). For every \(a\in R\), one can choose \(u\in\Gamma_r\) such that
\[
\|[a,u]\|_2\geq\tfrac12\Delta(a)-\tfrac52\varepsilon_r(a),\qquad
\Delta(a)=\|a-\tau(a)1\|_2,\quad
\varepsilon_r(a)=\|a-E_r(a)\|_2.
\tag{15}
\]
The proof is the four-matrix trace average, the exact mean squared displacement and finite-tail trace density in (FH3.5)–(FH3.7). The witnesses have operator norm one and commute exactly with the initial matrix stage \(D_r\).

First consider an ordinary bounded hypercentral sequence \(a_n\). It is centralizing, so (13) makes \(\varepsilon_r(a_n)\to0\) for each fixed \(r\). Choose strictly increasing integers \(K_r\geq r\) such that
\(n\geq K_r\) implies \(\varepsilon_r(a_n)\leq1/r\). Each choice follows from that ordinary convergence, after enlarging the threshold to exceed the previous one. Define on every original coordinate
\[
r(n)=\max\bigl(\{r:1\leq r\leq n,\ K_r\leq n\}\cup\{0\}\bigr).
\]
For fixed \(s\), every \(n\geq K_s\) has \(r(n)\geq s\); hence \(r(n)\to\infty\) ordinarily. For \(r(n)>0\), choose \(u_n\in\Gamma_{r(n)}\) by (15); at the remaining coordinates use \(u_n=1\).

This entire unitary sequence is ordinary centralizing. Indeed it eventually commutes exactly with each fixed \(D_s\). If \(x\in R\) and \(x_0\) is a finite-stage approximation in trace \(2\)-norm, then
\(\|[u_n,x-x_0]\|_2\leq2\|x-x_0\|_2\).
Choosing the approximation first proves trace \(2\)-centrality. NT2 gives bounded strong* centrality, and the complete finite-algebra criterion gives predual centralizing. Hypercentrality of \(a_n\) therefore forces \([a_n,u_n]\to0\) strongly*, hence in trace \(2\)-norm. But (15) gives, for \(r(n)>0\),
\[
\Delta(a_n)\leq2\|[a_n,u_n]\|_2+\frac5{r(n)}\longrightarrow0.
\tag{16}
\]
Thus \(a_n-\tau(a_n)1\) is strongly*-zero by NT2. The scalar coefficients are bounded by the common operator-norm bound on \(a_n\), so the sequence is scalar-trivial. Conversely every scalar-trivial sequence is hypercentral by FH5.

For the ultrafilter assertion, suppose \(A=\pi_\omega(a_n)\in Z(R_\omega)\) is nonscalar. Subtract \(\tau(a_n)1\) at every coordinate. These bounded scalar sequences are centralizing, and their quotient is their scalar ultralimit. The resulting class is still central and is nonzero after centering. Keep \(A,a_n\) for this centered class and representative. Then \(\tau(a_n)=0\), and faithfulness of the quotient trace gives \(\delta=\|A\|_{2,\omega}>0\).

For each \(r\), the two conditions
\[
\|a_n\|_2\geq\delta/2,\qquad
\varepsilon_r(a_n)\leq1/r
\tag{17}
\]
hold on an ultrafilter-large set: the first follows from the quotient trace-square limit, the second from (13). Intersect their sets with the previously chosen set and \(\{n:n\geq r\}\), giving nested \(B_r\in\omega\). Let \(r(n)\) be the largest \(r\leq n\) with \(n\in B_r\), or zero. Since \(B_s\subseteq\{n:r(n)\geq s\}\), one has \(r(n)\to_\omega\infty\). This uses only individual finite-threshold sets, with no countable intersection assertion.

Choose the finite Pauli witness \(u_n\in\Gamma_{r(n)}\) from (15) when \(r(n)>0\), and use the identity otherwise. On the large set where \(r(n)\geq s\), it commutes with \(D_s\). The same uniform-bound and finite-stage density argument therefore makes \(u_n\) centralizing along \(\omega\). On \(B_1\), (15) and (17) give
\[
\|[a_n,u_n]\|_2\geq\delta/4-\frac5{2r(n)}.
\tag{18}
\]
The ultralimit is at least \(\delta/4>0\). Since \(u_n\) represents a quotient element, centrality of \(A\) requires its quotient commutator to be zero. The trace-square ideal criterion would make that same ultralimit zero, a contradiction. Therefore \(Z(R_\omega)=\mathbb C1\).

The matrix units in tensor leg \(n\), regarded as sequences in \(n\), eventually commute with every fixed finite initial stage. The same trace density and finite criterion make them ordinary centralizing. Their exact coordinate relations and diagonal sum \(1\) survive every quotient; their diagonal quotient traces are \(1/2\), so the resulting unital \(M_2\) is nonzero and noncommutative. Theorem 4.1 below, whose proof uses only the general selection argument, gives type \(\mathrm{II}_1\). Together with the center just proved, this gives the whole factor conclusion for every free ultrafilter. \(\square\)

**Exercise 9.** Let \(k(r)\) be strictly increasing and let \(u_r\in\mathcal U(N_r)\). Define \(v_{k(r)}=u_r\) and \(v_n=1\) at every other original index. Check that \(v_n\) is ordinary central on its whole index set and hence centralizing.

*Solution.* Fix \(s\). If \(n=k(r)\) with \(r\geq s\), then \(v_n\in N_r\subseteq D_s'\cap R\). At all other indices it is the identity, except possibly the finitely many selected indices with \(r<s\). Thus it eventually commutes with every \(x_0\in D_s\). For \(x\in R\), approximate it in trace \(2\)-norm by a bounded element \(x_0\) of a finite stage, using FG2's complete density model. Since every \(v_n\) is unitary,
\[
\|[v_n,x-x_0]\|_2\leq2\|x-x_0\|_2.
\]
Choose the approximation first, then use eventual exact commutation with \(x_0\). This proves trace \(2\)-centrality, and NT2 gives intrinsic bounded strong* centrality. The earlier complete finite-algebra criterion then gives predual centralizing. No original coordinate outside the selected set was discarded.

**Exercise 10.** Derive the constant \(5/2\) in (18) from the approximation error and Lemma 5.1.

*Solution.* Put \(\varepsilon=\|a_n-b_n\|_2\leq1/r(n)\). The triangle inequality gives
\(\|b_n\|_2\geq\|a_n\|_2-\varepsilon\geq\delta/2-\varepsilon\).
The chosen unitary therefore moves \(b_n\) by at least \(\delta/4-\varepsilon/2\). Replacing \(b_n\) by \(a_n\) in the first term loses at most \(\varepsilon\); replacing it inside its unitary conjugate loses at most another \(\varepsilon\), because that conjugation preserves the trace norm. The total lower bound is
\[
\delta/4-\varepsilon/2-2\varepsilon
=\delta/4-(5/2)\varepsilon
\geq\delta/4-\frac5{2r(n)}.
\]
The estimate remains valid when its right side is negative at small \(r(n)\); its positive ultralimit is what the proof uses.

<a id="1-ordinary-and-ultrafilter-witnesses"></a>

## Normal tests and two ways to select a witness

Let \(C(M)\) be the bounded ordinary centralizing sequences:
\[
\|[x_n,\psi]\|\longrightarrow0\qquad(\psi\in M_*).
\tag{1}
\]
Let \(T(M)\) be the sequences approaching bounded scalars strongly*. Set
\[
H(M)=\{x\in C(M):[x_n,y_n]\to0
\text{ strongly* for every }y\in C(M)\}.
\tag{2}
\]
Replacing ordinary limits by ultralimits defines \(H_\omega(M)\). The quotient lesson already defines \(C_\omega(M)\) and \(T_\omega(M)\). FH5's complete varying-multiplier estimate proves
\[
T(M)\subseteq H(M)\subseteq C(M),\qquad
T_\omega(M)\subseteq H_\omega(M)\subseteq C_\omega(M).
\tag{3}
\]

The normalization \(x_n-\varphi(x_n)1\) detects scalar-triviality in either mode. If \(x_n-\lambda_n1\) tends strongly* to zero, positive-functional Schwarz gives \(\varphi(x_n)-\lambda_n\to0\), so the normalized difference does too. Conversely, that normalized difference itself supplies the bounded scalar approximation, since \(|\varphi(x_n)|\leq\|x_n\|\).

**Exercise 2.** For a bounded scalar sequence \(\lambda_n1\), identify its quotient image and decide whether its lack of ordinary convergence can contradict fullness.

*Solution.* Compactness of the bounded scalar disk gives \(\lambda=\lim_\omega\lambda_n\). The scalar difference \((\lambda_n-\lambda)1\) has both state square seminorms equal to \(|\lambda_n-\lambda|^2\), so its quotient is zero. The image is \(\lambda1\). All these sequences are scalar-trivial, including alternating or other nonconvergent ordinary scalar sequences. Fullness tests distance from bounded scalars; it does not require the scalar coefficients themselves to converge ordinarily.

**Lemma 1.1.** Let \((\psi_j)\) be norm dense in the normal state space.

If \(x\in C_\omega(M)\) and
\[
\lim_{n\to\omega}
\|x_n-\varphi(x_n)1\|_{\varphi,\#}^2=\delta>0,
\tag{4}
\]
there is an increasing sequence \(n(k)\) such that \(x_{n(k)}\) is ordinary centralizing and its squared scalar distance is at least \(\delta/2\). If \(x,y\in C_\omega(M)\) and their commutator has positive limiting squared seminorm, the same selection makes both subsequences ordinary centralizing with a uniformly nonvanishing commutator.

**Proof.** In the scalar case, its squared-distance ultralimit makes the set with squared distance at least \(\delta/2\) large. At step \(k\), intersect it with the finite collection
\[
\{n:\|[x_n,\psi_j]\|<1/k\},\qquad j\leq k.
\tag{5}
\]
Every set is large by centralizing. Intersect also with the cofinite set of indices greater than the previous selected index. The intersection is nonempty, so choose \(n(k)\) there. This gives the increasing sequence and its lower bound.

For the pair assertion, take half the positive commutator squared-seminorm limit as the lower bound and include the corresponding \(y_n\)-tests in the same finite intersection. Both sequences are bounded. For every fixed \(\psi_j\), their selected commutator norms tend to zero. The estimate
\(\|[x,\psi-\psi_j]\|\leq2\|x\|\|\psi-\psi_j\|\)
extends this to all normal states. NT1's complete four-positive-functional decomposition extends state tests to every normal functional. Thus the selected scalar or pair witnesses are ordinary centralizing, with the required uniformly positive distance or commutator. \(\square\)

**Exercise 1.** Explain why these selected indices can be strictly increasing and why that matters for a witness.

*Solution.* Each finite-test intersection lies in a free ultrafilter and is therefore infinite. The set \(\{1,\ldots,n(k-1)\}\) is finite. Its complement is large, and intersecting with it leaves a large nonempty set from which to choose \(n(k)\). Then \(n(k)>n(k-1)\). In particular no fixed original coordinate is reused indefinitely; every fixed state test is eventually among the finitely imposed tests and its bound tends to zero.

<a id="2-fullness-is-independent-of-the-ultrafilter"></a>

## Scalars and commutators give different tests

**Theorem 2.1.** The following are equivalent:

1. \(M\) is full.
2. \(C_\omega(M)=T_\omega(M)\) for some free ultrafilter.
3. \(C_\omega(M)=T_\omega(M)\) for every free ultrafilter.
4. \(M_\omega=\mathbb C\) for some free ultrafilter.
5. \(M_\omega=\mathbb C\) for every free ultrafilter.

**Proof.** The quotient identity \(T_\omega=\pi_\omega^{-1}(\mathbb C1)\) identifies (2) with (4), and (3) with (5), since \(\pi_\omega\) is onto.

Suppose \(M\) is full. The whole preceding fullness theorem says that every bounded ordinary centralizing sequence is scalar-trivial. If \(x\in C_\omega(M)\) were not scalar-trivial, its quotient \(X\) would be nonscalar. Expanding the state square norms gives
\[
\|x_n-\varphi(x_n)1\|_{\varphi,\#}^2
=\|x_n\|_{\varphi,\#}^2-|\varphi(x_n)|^2.
\]
The scalar ultraweak limit and the trace-square identity therefore identify its ultralimit with
\[
\tau_\omega(X^*X)-|\tau_\omega(X)|^2
=\|X-\tau_\omega(X)1\|_{2,\omega}^2>0.
\]
Faithfulness supplies strict positivity for the nonscalar centered element. Lemma 1.1 makes an ordinary centralizing sequence with this scalar distance uniformly positive. The scalar-normalization criterion contradicts fullness. This proves the every-ultrafilter assertions, and hence the some-ultrafilter assertions.

If \(M\) is not full, the same complete fullness theorem supplies \(x\in C(M)\setminus T(M)\). The squared normalized faithful-state distance does not tend to zero, so its limsup is positive. Choose an increasing ordinary subsequence on which it is at least a fixed positive \(\delta\). This sequence, now indexed by its subsequence position, remains ordinary centralizing. Along any free ultrafilter its squared normalized distance is still at least \(\delta\), and the displayed quotient identity makes its class nonscalar. Thus no free-ultrafilter quotient is scalar. This contrapositive proves all remaining implications without changing the factor or its faithful-state topology. \(\square\)

<a id="3-hypercentrality-is-also-independent-of-the-ultrafilter"></a>

**Theorem 3.1.** The following are equivalent:

1. \(C(M)=H(M)\).
2. \(C_\omega(M)=H_\omega(M)\) for some free ultrafilter.
3. \(C_\omega(M)=H_\omega(M)\) for every free ultrafilter.
4. \(M_\omega\) is commutative for some free ultrafilter.
5. \(M_\omega\) is commutative for every free ultrafilter.

Furthermore,
\[
H_\omega(M)=\pi_\omega^{-1}(Z(M_\omega)).
\tag{6}
\]

**Proof.** Products and commutators of bounded centralizing sequences are centralizing. Their quotient commutator is zero precisely when their coordinate commutator is in \(J_\omega\), that is, strongly*-zero along \(\omega\). Surjectivity of \(\pi_\omega\) therefore gives (6) and identifies each universal hypercentrality assertion with its commutative-quotient assertion.

If a quotient is noncommutative, choose two classes with nonzero commutator and bounded centralizing representatives \(x_n,y_n\). Faithfulness of its trace makes the limiting squared faithful-state seminorm of their commutator positive. The pair part of Lemma 1.1 produces two ordinary centralizing sequences with a uniformly nonvanishing commutator. They contradict \(C(M)=H(M)\). Consequently ordinary universal hypercentrality gives the every-ultrafilter version.

Conversely, if \(C(M)\ne H(M)\), choose \(x,y\in C(M)\) whose commutator does not tend strongly* to zero. Its bounded faithful-state seminorm has positive squared limsup. Restrict both sequences to the same increasing indices on which this square is bounded below by a positive constant. Along every free ultrafilter the two restricted sequences remain centralizing and their quotient commutator has positive squared trace norm. Thus none of the quotients is commutative. This proves the converse from any some-ultrafilter assertion, and completes all five equivalences. \(\square\)

**Exercise 3.** Starting from ordinary failure of hypercentrality, prove noncommutativity of \(M_\omega\) for every free ultrafilter.

*Solution.* Failure means that some bounded pair \(x,y\in C(M)\) has a commutator that is not strongly*-zero. Its squared \(\varphi,\#\)-seminorm has positive limsup. Choose a common increasing subsequence on which that square is at least \(\delta>0\), and restrict both members of the pair synchronously. Each restriction remains ordinary centralizing and hence is centralizing along any free ultrafilter. The quotient trace-square formula makes the quotient commutator's squared \(2\)-norm at least \(\delta\). It is nonzero by faithfulness, so the quotient is noncommutative. The synchronous choice preserves the witness pair at each coordinate.

<a id="4-moving-a-commutator-into-every-corner"></a>

## Every nonzero corner receives a commutator

**Theorem 4.1.** If \(M_\omega\) is noncommutative, it has no nonzero abelian projection. Consequently it is type \(\mathrm{II}_1\). The conclusion describes its type and does not assert trivial center.

**Proof.** By the just-proved pair selection, noncommutativity supplies bounded ordinary centralizing sequences \(x_k,y_k\) with
\[
\liminf_k\|[x_k,y_k]\|_{\varphi,\#}^2>0.
\tag{7}
\]
Put \(c_k=[x_k,y_k]\). Products, adjoints and commutators remain ordinary centralizing. The scalar trace construction of the preceding quotient lesson gives
\[
\kappa=\lim_{k\to\omega}\|c_k\|_{\varphi,\#}^2
=\tau_\omega(c^*c)>0,
\tag{8}
\]
and both square sequences \(c_k^*c_k,\ c_kc_k^*\) have scalar ultraweak limit \(\kappa1\).

Fix any nonzero projection \(F\in M_\omega\). Exact lifting gives centralizing coordinate projections \(f_n\) representing \(F\). Faithfulness gives \(\beta=\tau_\omega(F)>0\), and \(\varphi(f_n)\to_\omega\beta\). Replace \(f_n\) by \(1\) off the large set where \(\varphi(f_n)\geq\beta/2\). This keeps the quotient and centralizing class and makes that lower bound hold at every coordinate, as Exercise 6 verifies.

Now fix \(n\) while taking a \(k\)-limit. Ordinary strong* centrality gives \([f_n,x_k]\to0\) and \([f_n,y_k]\to0\) strongly*. The exact expansion is
\[
[f_nx_kf_n,f_ny_kf_n]-f_nc_kf_n
=f_nx_k[f_n,y_k]f_n-f_ny_k[f_n,x_k]f_n.
\tag{9}
\]
FH5 controls the products of the varying centralizing \(x_k,y_k\) with these bounded strongly*-zero commutators. Fixed multiplication by \(f_n\) then preserves convergence. Thus (9) tends strongly* to zero, ordinarily and along \(\omega\).

The same argument applies to \([f_n,c_k]\). For example
\[
(f_nc_kf_n)^*(f_nc_kf_n)-f_nc_k^*c_kf_n
=f_nc_k^*[f_n,c_k]f_n
\]
is strongly*-zero by FH5. The adjoint square has the corresponding expansion with \(c_k^*\). Pair the two scalar ultraweak square limits with the fixed normal positive functional \(a\mapsto\varphi(f_naf_n)\). This proves both identities
\[
\begin{aligned}
\lim_{k\to\omega}\varphi((f_nc_kf_n)^*(f_nc_kf_n))
&=\kappa\varphi(f_n),\\
\lim_{k\to\omega}\varphi((f_nc_kf_n)(f_nc_kf_n)^*)
&=\kappa\varphi(f_n).
\end{aligned}
\tag{10}
\]
The triangle inequality for the two state square seminorms makes strongly*-small bounded changes preserve their limiting squares, so the compressed commutator in (9) has the same limiting squared symmetric seminorm. It is at least \(\kappa\beta/2\).

For each \(n\), choose \(k(n)\geq n\) in the relevant finite intersection of large sets so that
\[
\begin{aligned}
\|[x_{k(n)},\psi_j]\|+\|[y_{k(n)},\psi_j]\|
&<1/n&&(j\leq n),\\
\|[f_nx_{k(n)}f_n,f_ny_{k(n)}f_n]\|_{\varphi,\#}^2
&\geq\kappa\beta/4.
\end{aligned}
\tag{11}
\]
The second set is large by the strictly larger limit in (10); the first tests hold eventually because \(x_k,y_k\) are ordinary centralizing. Normal-state density and NT1's positive-functional decomposition make the reindexed \(x_{k(n)},y_{k(n)}\) ordinary centralizing, with their common uniform bounds.

Their products with \(f_n\) are centralizing along \(\omega\), by the sequence C* algebra property. The two quotient images lie in \(FM_\omega F\). Their commutator has squared trace norm at least \(\kappa\beta/4>0\) by (11) and the quotient seminorm identity. Hence this prescribed corner is noncommutative.

Since \(F\) was arbitrary, there is no nonzero abelian projection. The quotient is finite with a faithful normal normalized trace by its completed construction. FH1's whole-center finite type criterion gives type \(\mathrm{II}_1\), and its full halving proof gives a unital two-by-two matrix system even without a separable predual for the quotient. No assertion of a scalar center has been made here. \(\square\)

**Exercise 5.** Identify the normal functional used to evaluate the scalar limit of \(c_k^*c_k\) in (10), and explain which projection is fixed during that limit.

*Solution.* For the fixed coordinate \(n\), use \(\psi_n(a)=\varphi(f_naf_n)\). NT1's fixed left and right multiplier maps keep a normal functional normal. Its value at \(1\) is \(\varphi(f_n)\). The scalar ultraweak limit \(c_k^*c_k\to_\omega\kappa1\) therefore gives \(\psi_n(c_k^*c_k)\to_\omega\kappa\varphi(f_n)\). This is the \(k\)-limit with \(f_n\) fixed. Only after that limit supplies a large set is the index \(k(n)\) chosen.

**Exercise 6.** Why may the lower bound \(\varphi(f_n)\geq\beta/2\) be imposed at every coordinate without changing \(F\) or its centralizing representative?

*Solution.* The original projection lift has \(\varphi(f_n)\to_\omega\beta\), so \(S=\{n:\varphi(f_n)\geq\beta/2\}\) is large. Leave it unchanged on \(S\) and use \(1\) off \(S\). The two lifts agree on a large set, so their difference has zero limit in every bounded strong* seminorm. The altered lift still satisfies every predual centralizing test, because its commutator sequence agrees with the original on \(S\). It represents the same quotient projection. Finally \(\beta\leq1\), so \(\varphi(1)=1\geq\beta/2\) at the replaced coordinates too.

The [tensor-absorption lesson](strong-stability-and-tensor-absorption.md) can now use FH1's full matrix system and the preceding exact coordinate lifts. The corner theorem and the separate dyadic center theorem supply their respective type and factor conclusions.

<a id="references"></a>

## Freely accessible proofs and the corner comparison

The whole mathematical route is the completed quotient and ordinary-central-sequence construction together with [FH0–5](../components/fullness-hypercentrality-and-tail-inputs.md). These inputs include the entire Lebesgue/Lp construction for the nonfactor example, canonical finite-factor trace normality, full-center comparison and halving, compact-orbit displacement, the normal finite matrix tail map and explicit finite Pauli displacement identities, and the two-square perturbation estimate. The proofs do not use an unspecified type decomposition, Haar average, direct integral, or omitted similar-argument step.

Dusa McDuff, [*On the structure of II₁-factors*](https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&option_lang=eng&paperid=5426&what=fullteng), Theorem 1.1(iii) and Lemmas 1.3–1.4, printed pp.33–35 (PDF pp.5–7), compares hypercentrality with the center of the tracial central-sequence algebra and proves a compact-orbit approximation result. Theorem 1.1 leaves the first two similar proofs unstated. The finite Pauli identities, all-coordinate trace-distance test and both complete selection modes used here are supplied in FH3 and the present proofs. The human paper retains its own rights; no expression-reuse licence is inferred from access.

Alain Connes, [*Outer conjugacy classes of automorphisms of factors*](https://www.numdam.org/articles/10.24033/asens.1295/), Theorem 2.2.1, implication (d) \(\Rightarrow\) (e), printed pp.400–401 (PDF pp.19–20), is the freely accessible historical corner-method comparison. Its hypothesis is a factor with separable predual. The argument chooses a new pair for each fixed lifted corner; our proof writes both faithful-state square tests, the fixed-coordinate versus reindexed limits, and the \(\kappa\beta/4\) bound explicitly. Its subsequent implication (e) \(\Rightarrow\) (a) refers to Araki's absorption theorem and is not a premise here.
