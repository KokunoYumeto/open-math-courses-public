# Central sequence algebras and exact lifts

*Written by GPT-6.1 Sol (OpenAI), Ultra. New original exposition: CC0-1.0 to the extent of rights held. Comparison sources retain their own terms.*

Matrix units require exact equations: two diagonal projections must be orthogonal, and a connecting partial isometry must have the prescribed initial and final projections. A limit can make those equations exact while every coordinate still has an error. This lesson explains how to repair the coordinates without changing their limit.

We first examine the two repairs that will be needed: moving finite trace mass, and making room at infinite endpoints. We then construct the limiting algebra, lift one projection, prove completeness of its trace metric, and assemble the repaired matrix units. Original result and problem numbers remain stable labels throughout this order.

Our setting is a nonzero factor \(M\) with separable predual, a faithful normal state \(\varphi\), and a free ultrafilter \(\omega\) on \(\mathbb N\). The complete [quotient and lifting inputs](../components/central-sequence-quotient-and-lifting-inputs.md) prove CQ1–7. The [preceding central-sequence lesson](central-sequences-and-free-group-factors.md) proves the passage from predual commutators to bounded strong* centrality; [NT1–2](../components/central-sequence-foundations.md#nt1-normal-functional-decomposition) proves the normal-functional and faithful-state topology facts used below.

<a id="7-exercises-with-complete-solutions"></a>

## Two coordinate repairs to keep in view

Finite cancellation concerns a finite removed subpiece. CQ4 proves it even when the containing endpoints are infinite. Removing an infinite subpiece requires a different argument.

**Exercise 6.** Use the unilateral shift \(S\) on \(\ell^2(\mathbb N)\), with \(S^*S=1\) and \(SS^*=1-p_0\), to exhibit equivalent whole projections and equivalent subprojections whose complements are not equivalent. Explain the role of the infinite-piece removal in the lifting proof.

*Solution.* Set \(e=f=1\), \(p=1\), and \(q=1-p_0\). The identity gives \(e\sim f\), and \(S\) gives \(p\sim q\). The complements are \(e-p=0\) and \(f-q=p_0\). A partial isometry with zero initial projection is zero, so it cannot have the nonzero final projection \(p_0\). Thus cancellation fails for this infinite \(p\). In Theorem 5.1 we remove a small infinite projection from the initial support of an approximate partial isometry. Its image is removed at the other end as well. Both remaining endpoint defects then contain an infinite projection, and CQ5 proves that they are equivalent. The removal is small in both state seminorms, so it does not alter the quotient element.

**Exercise 7.** A partition \(e_1+e_2=1\) in a type \(\mathrm{II}_1\) factor has traces \(3/8\) and \(5/8\). Give an exact equal-trace partition and compute the squared trace \(2\)-norm of each change.

*Solution.* CQ7's trace-cut construction supplies \(r\leq e_2\) with \(\tau(r)=1/8\). Put \(e'_1=e_1+r\) and \(e'_2=e_2-r\). Because \(r\) is in the second original cell, these are orthogonal projections and their sum remains \(1\). Their traces are \(3/8+1/8=1/2\) and \(5/8-1/8=1/2\). The respective differences are \(r\) and \(-r\), whose squares are both \(r\). Consequently both squared changes are exactly \(1/8\). FCT7 makes the corrected cells equivalent.

**Exercise 8.** Let \(e_1,\ldots,e_m\) be equivalent orthogonal projections and let \(v_j^*v_j=e_1,\ v_jv_j^*=e_j\). For \(e_{ij}=v_iv_j^*\), check the products, adjoints, diagonal entries, and total support, allowing a support smaller than \(1\).

*Solution.* Write \(v_j=e_jv_je_1\). If \(j\ne k\), then
\(v_j^*v_k=v_j^*e_je_kv_k=0\); for \(j=k\) it equals \(e_1\). Hence
\[
e_{ij}e_{k\ell}
=v_i(v_j^*v_k)v_\ell^*
=\delta_{jk}v_ie_1v_\ell^*
=\delta_{jk}e_{i\ell}.
\]
Taking adjoints gives \(e_{ij}^*=e_{ji}\). Also \(e_{ii}=e_i\), so the sum of the diagonal entries is \(\sum_i e_i\), exactly the support initially specified. Nothing in the calculation requires that support to be the identity.

<a id="1-limits-along-an-ultrafilter"></a>

## Which scalar does the limiting algebra remember?

A free ultrafilter contains every cofinite set, is closed under supersets and finite intersections, excludes the empty set and every finite set, and chooses exactly one of \(A,A^c\) for each subset \(A\subseteq\mathbb N\). Convergence along it means
\[
x_n\to_\omega x
\quad\Longleftrightarrow\quad
\{n:x_n\in V\}\in\omega\text{ for every neighborhood }V\text{ of }x.
\tag{1}
\]

**Lemma 1.1.** Every sequence in a compact Hausdorff space has a unique \(\omega\)-limit. A sequence converges ordinarily to \(x\) if and only if its limit along every free ultrafilter is \(x\).

**Proof.** For \(A\in\omega\), let \(F_A\) be the closure of the values indexed by \(A\). Every finite intersection of the \(F_A\) contains the values indexed by the corresponding nonempty finite intersection of index sets. Compactness therefore gives a common point \(x\). If an open neighborhood \(V\) of \(x\) had index set outside \(\omega\), its complementary index set would lie in \(\omega\), and its closed value set would be contained in the closed complement of \(V\). That would exclude \(x\), a contradiction. Hausdorff separation supplies disjoint neighborhoods for distinct points, and an ultrafilter cannot contain their disjoint index sets. This proves uniqueness.

An ordinary limit has the stated ultralimit because every required set is cofinite. For the converse, if \(x\) is not the ordinary limit, choose a neighborhood \(V\) with infinitely many indices \(B=\{n:x_n\notin V\}\). The filter generated by \(B\) and the cofinite sets is proper: every basic finite intersection still contains infinitely many points of \(B\). Ordered by inclusion, its proper filter extensions have upper bounds given by unions of chains. Choice in CF/PC0 supplies a maximal proper extension. If neither \(A\) nor \(A^c\) belonged to it, adjoining \(A\) would fail only if a filter member were disjoint from \(A\), which would force \(A^c\) into the filter. Thus the maximal extension chooses one of every complementary pair and is an ultrafilter. It cannot contain a finite set because it contains that set's cofinite complement. Its compact-space limit lies outside \(V\), since its \(B\)-value closure lies there. This contradicts the asserted common limit of all free ultrafilters. \(\square\)

Scalar disks are compact Hausdorff. For bounded scalars the limit operation is linear, multiplicative and compatible with conjugation: intersect the finitely many sets on which each scalar is close to its limit, and use their common bounds for products.

**Exercise 1.** For \(a_n=(-1)^n\), determine all free-ultrafilter limits and decide ordinary convergence.

*Solution.* Exactly one parity class belongs to the ultrafilter. Membership of the even class makes the sequence identically \(1\) on an ultrafilter-large set; membership of the odd class makes it identically \(-1\) there. These are the only limits. Both parity classes are infinite and can be used as \(B\) in the proper-filter extension proved above, so both limits occur. Since the even and odd ordinary subsequences have distinct limits, the original sequence does not converge ordinarily.

**Exercise 2.** Can one specified ultrafilter limit recover the limsup of every bounded real sequence? Establish the relation to both liminf and limsup.

*Solution.* The sequence in Exercise 1 has limsup \(1\), while an ultrafilter containing the odd indices gives limit \(-1\). This disproves the proposed recovery. In general, for every \(\varepsilon>0\), eventually every term is above \(\liminf a_n-\varepsilon\) and below \(\limsup a_n+\varepsilon\). Those two eventual index sets are cofinite and belong to every free ultrafilter. Their scalar limit consequently lies between those two bounds. Let \(\varepsilon\) decrease to zero. The resulting interval contains every ultralimit; a given ultrafilter need not select either endpoint.

<a id="2-the-sequence-algebra-and-its-trace"></a>

Use the normal-functional actions
\[
(x\psi)(a)=\psi(ax),\qquad
(\psi x)(a)=\psi(xa),\qquad [x,\psi]=x\psi-\psi x.
\tag{2}
\]
Our sequence algebra is
\[
C_\omega(M)=\{(x_n)\in\ell^\infty(\mathbb N,M):
\|[x_n,\psi]\|\to_\omega0\text{ for every }\psi\in M_*\}.
\tag{3}
\]
Coordinate multiplication, adjoints and the supremum norm make \(\ell^\infty(\mathbb N,M)\) a complete C* algebra: a norm Cauchy sequence has coordinate norm limits with uniform bounds, and the uniform Cauchy estimate proves convergence in the supremum norm.

The subalgebra \(C_\omega(M)\) contains the unit and is norm closed. Products obey
\[
[xy,\psi]=x[y,\psi]+[x,\psi]y.
\tag{4}
\]
NT1 bounds the functional module actions by the operator norm. For adjoints, putting \(\psi^*(a)=\overline{\psi(a^*)}\) gives \([x^*,\psi]=-[x,\psi^*]^*\). Finally a uniform perturbation of size \(\varepsilon\) changes any commutator norm by at most \(2\varepsilon\|\psi\|\). These observations prove all the asserted algebra and closure properties.

NT2 identifies bounded strong* convergence with vanishing of
\[
\|x\|_{\varphi,\#}
=\left(\frac{\varphi(x^*x)+\varphi(xx^*)}{2}\right)^{1/2}.
\tag{5}
\]
The preceding lesson's complete normal-commutator argument uses only finite estimates; applying them on ultrafilter-large sets proves
\[
[x_n,a]\to_\omega0\text{ strongly*}\qquad(a\in M)
\tag{6}
\]
for every sequence in (3).

**Proposition 2.1.** The ultraweak \(\omega\)-limit of a sequence \(x=(x_n)\in C_\omega(M)\) is a scalar. Denote that scalar by \(\tau_\omega(x)\). This is a normalized trace on \(C_\omega(M)\).

**Proof.** A bounded ball in \(M=(M_*)^*\) is ultraweakly compact. In the complete CP/CF construction this is the closed set of linear, uniformly norm-bounded coordinate assignments in the product of compact scalar disks indexed by \(M_*\); CP identifies those assignments with elements of \(M\). It is Hausdorff because the predual separates operators. Lemma 1.1 therefore supplies an ultraweak ultralimit \(z\in M\).

For fixed \(a\in M,\psi\in M_*\), the two normal pairings \(\psi(ax_n)\) and \(\psi(x_na)\) have the same limit by (3). Thus \(\psi(az-za)=0\) for every \(\psi\); separation puts \(z\) in \(Z(M)=\mathbb C1\). This defines \(\tau_\omega\). Scalar pairings establish its linearity and normalization; positive coordinate sequences have positive limits because every positive normal functional is nonnegative on them.

For two centralizing sequences \(x,y\), choose any normal state \(\psi\). Then
\[
|\psi(x_ny_n-y_nx_n)|
\leq\|y_n\|\,\|[x_n,\psi]\|\to_\omega0.
\tag{7}
\]
Both products are in (3) and have scalar limits, so their \(\psi\)-limits are their scalar values. Equality proves the trace law. \(\square\)

Define
\[
J_\omega=\{x\in C_\omega(M):x_n\to_\omega0\text{ strongly*}\}.
\tag{8}
\]
The trace law and the ultraweak limits of the two square sequences give
\[
\lim_\omega\|x_n\|_{\varphi,\#}^2
=\tau_\omega(x^*x)=\tau_\omega(xx^*).
\tag{9}
\]
Thus \(J_\omega\) is the trace-square null space. It is a linear closed star ideal: scalar Schwarz gives the triangle inequality for the trace square norm, its operator-norm bound proves closure, and positivity and the trace law give
\[
\tau_\omega((yx)^*(yx))\leq\|y\|^2\tau_\omega(x^*x),\qquad
\tau_\omega((xy)^*(xy))\leq\|y\|^2\tau_\omega(xx^*).
\]
This proves two-sidedness inside \(C_\omega(M)\). We have made no ideal assertion for strong*-zero sequences in the full bounded sequence algebra.

A bounded strong*-zero perturbation preserves centralizing. For a positive normal functional, the full positive-functional Schwarz estimate gives
\[
\|[z_n,\psi]\|
\leq\psi(1)^{1/2}
\left(\psi(z_n^*z_n)^{1/2}+\psi(z_nz_n^*)^{1/2}\right)\to_\omega0.
\tag{10}
\]
NT1's four-positive-functional decomposition treats every normal functional. The uniform bound on the perturbation is part of this assertion.

CQ1 now constructs the C* quotient, including its norm and continuous calculus:
\[
M_\omega=C_\omega(M)/J_\omega,\qquad
\pi_\omega:C_\omega(M)\longrightarrow M_\omega.
\tag{11}
\]
The trace descends because Schwarz annihilates its null ideal. It is faithful there by (9), normalized because the unit is not null, and tracial because products descend. Write
\(\|X\|_{2,\omega}=\tau_\omega(X^*X)^{1/2}\).

**Exercise 3.** Suppose \(x_n-\lambda_n1\to_\omega0\) strongly*, where \((\lambda_n)\) is bounded. Identify the represented scalar and explain what would happen if the quotient discarded every scalar-trivial sequence.

*Solution.* Let \(\lambda=\lim_\omega\lambda_n\). A scalar sequence tending to zero tends strongly* to zero, since both state square seminorms are its squared absolute value. Therefore
\[
x_n-\lambda1=(x_n-\lambda_n1)+(\lambda_n-\lambda)1
\to_\omega0\text{ strongly*}.
\]
Its image in (11) is \(\lambda1\). In particular the scalar-trivial space is
\[
T_\omega=\pi_\omega^{-1}(\mathbb C1).
\tag{12}
\]
This space contains the unit. An ideal containing all of it would contain the unit and hence every element, making the quotient zero. The quotient by \(J_\omega\) instead retains the scalar unit. Although \(T_\omega\) is the preimage of a scalar subalgebra, it is generally not an ideal.

<a id="4-exact-projection-lifts"></a>

## Repair one projection before completing the trace metric

The C* quotient already permits projection lifting; its von Neumann completeness is not a premise of this repair. CQ1's quotient calculus also gives a contraction lift of every quotient contraction. For any representative \(a\), use
\[
a f(a^*a),\qquad
f(t)=
\begin{cases}1,&0\leq t\leq1,\\t^{-1/2},&t\geq1.\end{cases}
\tag{14}
\]
This is a coordinate contraction by the positive calculus. Its quotient image is unchanged because the square of the quotient contraction has spectrum in \([0,1]\), where \(f=1\).

**Lemma 4.1.** Every projection \(E\in M_\omega\) has a representing sequence of projections \(e_n\in M\). If \(Q=\pi_\omega(q_n)\) already has a projection representative and \(E\le Q\), the lift can be chosen with \(e_n\le q_n\).

**Proof.** Lift \(E\) to contractions \(x_n\), and set \(h_n=x_n^*x_n\). The positive contractions \(h_n\) represent \(E\), so \(h_n-h_n^2\in J_\omega\). With the bounded spectral calculus supplied by SC8–9, set
\[
e_n=\mathbf1_{[1/2,1]}(h_n).
\]
The scalar bound is
\[
|\mathbf1_{[1/2,1]}(t)-t|\leq2t(1-t)
\quad(0\leq t\leq1).
\tag{20}
\]
Squaring, applying the spectral calculus, and then the positive state gives
\[
\varphi((e_n-h_n)^2)
\leq4\varphi((h_n-h_n^2)^2)\to_\omega0.
\tag{21}
\]
The difference is self-adjoint and bounded; (5) makes it strong*-zero. Equation (10) shows that the new projections are centralizing, and their quotient class remains \(E\).

For the specified support, first compress the contraction lift to \(q_nx_nq_n\). Coordinate compression keeps its norm at most one, and its image is \(QEQ=E\). Its square lies in \(q_nMq_n\). Since the cutoff function vanishes at zero, its spectral projection vanishes on \(1-q_n\), so the lifted projection is at most \(q_n\) at every coordinate. \(\square\)

**Exercise 4.** Check (20) on both intervals and at \(0,1/2,1\), then derive the squared state estimate (21).

*Solution.* On \(0<t<1/2\), the left side is \(t\), and \(t/[t(1-t)]=1/(1-t)\leq2\). On \(1/2\leq t<1\), it is \(1-t\), whose ratio to \(t(1-t)\) is \(1/t\leq2\). At \(0\) and \(1\) both sides are zero. At the included cutoff point \(1/2\), they are both \(1/2\). All quantities are nonnegative, so squaring preserves the pointwise inequality. The complete bounded calculus preserves that order for \(h_n\), and the positive functional \(\varphi\) preserves it again. The resulting estimate is exactly (21), including the squared factor \(4\).

<a id="3-why-the-quotient-is-already-a-von-neumann-algebra"></a>

## A countable diagonal supplies completeness; the trace supplies normality

**Theorem 3.1.** \(M_\omega\) is a finite von Neumann algebra, with faithful normal tracial state \(\tau_\omega\). Every \(\theta\in\operatorname{Aut}(M)\) induces a normal trace-preserving automorphism
\[
\theta_\omega(\pi_\omega(x_n))=\pi_\omega(\theta(x_n)).
\tag{13}
\]
The map \(\theta\mapsto\theta_\omega\) is a group homomorphism.

**Proof.** We first prove that the operator-norm unit ball of (11) is complete for its trace metric. From a Cauchy sequence choose a subsequence \(X_r\) such that
\[
\|X_r-X_p\|_{2,\omega}<2^{-p}\qquad(r>p).
\tag{15}
\]
Lift each \(X_r\) to coordinate contractions \(x_r(k)\) using (14). Separability of \(M_*\) gives a countable norm-dense family \((\psi_j)\) in its normal state space; subspaces of a separable metric space are separable, for example by selecting one point in each nonempty basic ball. NT1's four-positive-functional decomposition makes tests on all these states sufficient for tests on every normal functional.

For each \(r\), impose the following finite tests on a set \(A_r\in\omega\):
\[
\begin{aligned}
\|[x_r(k),\psi_j]\|&\leq1/r&&(j\leq r),\\
\|x_r(k)-x_p(k)\|_{\varphi,\#}
&\leq2^{-p}+2^{-r}&&(p<r).
\end{aligned}
\tag{16}
\]
The first tests follow from centralizing. For the second, (9) identifies their squared ultralimits with the distances in (15), which are strictly below the displayed bounds. Intersect these finitely many large sets with \(A_{r-1}\) and the cofinite set \(\{k:k\geq r\}\); take \(A_0=\mathbb N\). This constructs nested \(A_r\) without requiring any countable intersection.

At coordinate \(k\), let \(r(k)\) be the largest \(r\leq k\) for which \(k\in A_r\), or zero if none exists. Define \(x(k)=x_{r(k)}(k)\), with \(x_0(k)=0\). For fixed \(p\), membership in \(A_p\) implies \(r(k)\geq p\), so \(r(k)\to_\omega\infty\). Each fixed state test in the first line of (16) therefore vanishes. The bound \(\|x(k)\|\leq1\) gives
\(\|[x(k),\psi-\psi_j]\|\leq2\|\psi-\psi_j\|\);
norm density and positive decomposition show \(x\in C_\omega(M)\).

Fix \(p\). On the large set where \(r(k)>p\), the second line bounds the distance to \(x_p(k)\) by \(2^{-p}+2^{-r(k)}\). Taking the square ultralimit and using (9) yields
\[
\|\pi_\omega(x)-X_p\|_{2,\omega}\leq2^{-p}.
\tag{17}
\]
The subsequence converges in the quotient unit ball, and the original Cauchy sequence converges to the same element by the triangle inequality.

CQ2 constructs the isometric trace Hilbert representation; CQ3 uses this complete metric ball and bounded density to identify it with its entire bicommutant. Its vector trace is faithful and normal there, and the trace law makes the algebra finite. The key extension from the cyclic vector to its dense right-multiplier orbit is
\[
\|(X_i-X)Y\|_{2,\omega}
\leq\|Y\|\|X_i-X\|_{2,\omega}.
\tag{18}
\]
CQ3 explicitly treats arbitrary Cauchy nets, so sequential metric completeness is sufficient. No separability or factor property of the resulting \(M_\omega\) is inferred.

For a normal automorphism \(\theta\) of \(M\), the functional identity is
\[
[\theta(x),\psi]=[x,\psi\circ\theta]\circ\theta^{-1}.
\tag{19}
\]
Its norm and normal-functional pullback preserve (3). Pulling back each normal positive functional proves preservation of bounded strong*-zero sequences, and the same argument applies to \(\theta^{-1}\). Thus \(J_\omega\) is preserved and (13) defines an invertible star homomorphism of the quotient. Scalar ultraweak limits are preserved under the normal map \(\theta\), so it preserves the trace.

For whole-domain normality apply CQ3: the trace-preserving map implements the unitary
\(U_\theta(X\Omega)=\theta_\omega(X)\Omega\)
in the trace Hilbert space. Conjugation by this unitary pulls every square-summable CP vector-pair functional back to another such functional. It is therefore ultraweakly continuous on its entire domain, as is its inverse. Composing the coordinate maps proves
\((\theta\eta)_\omega=\theta_\omega\eta_\omega\), including the identity and inverse. \(\square\)

**Exercise 5.** Justify \(r(k)\to_\omega\infty\) in this diagonal argument using individual finite-threshold sets.

*Solution.* Given any integer \(p\), the already constructed set \(A_p\) lies in \(\omega\). For \(k\in A_p\) one has \(k\geq p\), and \(p\) is one of the permissible candidates in the finite maximum defining \(r(k)\). Thus
\(A_p\subseteq\{k:r(k)\geq p\}\).
Closure under supersets makes the latter set large. This holds for each fixed \(p\), which is precisely convergence to infinity along the ultrafilter. The construction nowhere uses largeness of \(\bigcap_p A_p\), a property that free ultrafilters do not have in general.

**Exercise 9.** Prove that an inner automorphism induces the identity on \(M_\omega\), and identify why its implementer must be fixed.

*Solution.* If \(\theta=\operatorname{Ad}u\) for one fixed unitary \(u\in M\), equation (6) applied to \(a=u\) gives \(ux_n-x_nu\to_\omega0\) strongly*. The fixed multiplication topology from CP/ST then gives
\[
ux_nu^*-x_n=(ux_n-x_nu)u^*\to_\omega0
\quad\text{strongly*}.
\]
Both representatives belong to \(C_\omega(M)\), so their difference is in \(J_\omega\), and (13) fixes their quotient element. A varying unitary \(u_n\) is not one of the fixed tests in (6). Neither that estimate nor continuity of multiplication by a single fixed operator proves the analogous varying-implementer assertion.

<a id="5-prescribing-both-ends-of-a-partial-isometry"></a>

## Fill the endpoint defects

**Theorem 5.1.** Let \(e=(e_n),f=(f_n)\) be projection sequences in \(C_\omega(M)\), with \(e_n\sim f_n\) for every \(n\). Suppose \(U\in M_\omega\) satisfies
\[
U^*U=\pi_\omega(e),\qquad UU^*=\pi_\omega(f).
\tag{22}
\]
There are partial isometries \(v_n\), centralizing along \(\omega\), such that
\[
v_n^*v_n=e_n,\qquad v_nv_n^*=f_n,\qquad
\pi_\omega(v)=U.
\tag{23}
\]

**Proof.** Lift \(U\) to contractions and compress to \(y_n=f_nx_ne_n\). Both products stay centralizing and the image remains \(\pi_\omega(f)U\pi_\omega(e)=U\). For the bounded polar decomposition \(y_n=w_n^0h_n^{1/2}\), put
\[
h_n=y_n^*y_n,\quad
p_n=\mathbf1_{[1/2,1]}(h_n),\quad
w_n=w_n^0p_n,\quad q_n=w_nw_n^*.
\tag{24}
\]
The quotient identities say \(e-h\in J_\omega\) and \(f-yy^*\in J_\omega\). Both are positive coordinate contractions. The same spectral calculus as in the projection repair gives
\[
\begin{aligned}
e_n-p_n&\leq2(e_n-h_n),\\
f_n-q_n&\leq2(f_n-y_ny_n^*),\\
(w_n-y_n)^*(w_n-y_n)&\leq2(e_n-h_n),\\
(w_n-y_n)(w_n-y_n)^*&\leq2(f_n-y_ny_n^*).
\end{aligned}
\tag{25}
\]
For the first inequality the spectral values below \(1/2\) obey \(1\leq2(1-t)\), and the other values give zero on the left. The final-support version uses the polar transport of the nonzero spectrum; at the remaining kernel it has the same bound. The two difference-square estimates use
\((\mathbf1_{[1/2,1]}(t)-\sqrt t)^2\leq2(1-t)\)
on \(0<t\leq1\); at the zero polar support the difference is zero. Taking \(\varphi\), bounded strong*-zero convergence makes the right sides tend to zero. Projection differences and both squares of \(w-y\) are therefore small. In particular \(w\) is centralizing by (10) and represents \(U\).

At coordinates with finite \(p_n\), CQ4 gives
\(e_n-p_n\sim f_n-q_n\),
using the assumed \(e_n\sim f_n\). That argument works for finite or infinite endpoints and includes \(p_n=0\).

At coordinates with infinite \(p_n\), use CQ5 with \(\varphi\) and the normal positive functional \(a\mapsto\varphi(w_naw_n^*)\) to obtain \(r_n\leq p_n\) such that
\[
p_n-r_n\text{ is infinite},\qquad
\varphi(r_n)+\varphi(w_nr_nw_n^*)<1/n^2.
\tag{26}
\]
Set
\[
p'_n=p_n-r_n,\quad w'_n=w_np'_n,\quad
q'_n=w'_nw_n'^*.
\tag{27}
\]
Then \(e_n-p'_n\) contains \(r_n\), and \(f_n-q'_n\) contains \(w_nr_nw_n^*\); both are infinite and are equivalent by CQ5. The removed operator \(w_nr_n\) has the two square masses exactly shown in (26). Its strong*-zero removal preserves the representative \(U\), and the new endpoint defects still tend strongly* to zero. In the finite case use \(p'_n=p_n,\ w'_n=w_n,\ q'_n=q_n\).

Choose a partial isometry \(s_n\) between the equivalent remaining defects. Its initial and final projections are those defects, so
\[
\varphi(s_n^*s_n)=\varphi(e_n-p'_n)\to_\omega0,\qquad
\varphi(s_ns_n^*)=\varphi(f_n-q'_n)\to_\omega0.
\]
Thus \(s\) is a bounded strong*-zero sequence. Its initial and final supports are orthogonal to the respective supports of \(w'_n\), so \(v_n=w'_n+s_n\) has exactly the endpoints in (23). It represents \(U\), and (10) proves it centralizing. \(\square\)

<a id="6-partitions-and-matrix-units"></a>

## Assemble the finite system, retaining its support

**Theorem 6.1.** Every finite partition \(E_1+\cdots+E_m=1\) by orthogonal projections in \(M_\omega\) has an exact projection-partition representative \(e_1(n)+\cdots+e_m(n)=1\) in \(M\). If the \(E_j\) are equivalent, the coordinate projections can be chosen equivalent. Every finite system of matrix units in \(M_\omega\) has an exact centralizing system of coordinate matrix units, including a system whose support is smaller than \(1\).

**Proof.** For an arbitrary partition, lift its first cell by Lemma 4.1, its second cell inside the complementary coordinate projections, and each later cell inside the remaining complements. Use the final remainder for the last cell. Orthogonality and the sum to \(1\) now hold at every coordinate; the quotient of the last remainder is the last prescribed cell. This works for \(m=1\) and zero cells as well. Within a previously lifted support \(Q=\pi_\omega(q_n)\), the same finite induction gives an exact partition of \(q_n\).

Consider next equivalent cells with nonzero total support \(Q\). Since
\(\varphi(q_n)\to_\omega\tau_\omega(Q)>0\),
the set \(S=\{n:q_n\ne0\}\) is large. Off \(S\), replace \(q_n\) and the first cell by \(1\) and all other cells by zero. Every change is supported off an ultrafilter-large set, so all its normal-functional and strong* tests have zero ultralimit. The new support is nonzero at each coordinate.

If \(M\) is a type \(\mathrm{II}_1\) factor, its normalized trace \(\tau\) is normal by the complete FCT construction. Proposition 2.1 evaluated against \(\tau\) identifies quotient trace values with scalar coordinate trace ultralimits. The quotient cells have equal trace, so
\[
\tau(e_j(n))-\tau(q_n)/m\to_\omega0.
\tag{28}
\]
Apply CQ7's donor-and-deficit construction inside \(q_nMq_n\). It gives equivalent exact cells of trace \(d_n=\tau(q_n)/m\), retaining the sum \(q_n\), with the complete error identity
\[
\|e'_j(n)-e_j(n)\|_{2,\tau}^2
=|\tau(e_j(n))-d_n|\to_\omega0.
\tag{29}
\]
NT2 transports bounded trace convergence to strong* convergence for the original faithful state; (10) preserves the centralizing quotient classes.

If \(M\) is infinite, apply CQ7's infinite-support construction. A finite nonzero coordinate support can acquire an infinite projection from its complement of \(\varphi\)-mass below \(1/n^2\). Then one infinite cell can donate \(m-1\) small infinite pieces to the other cells while keeping an infinite remainder. All corrected cells are infinite and equivalent by CQ5. The total state square error is at most \(2/n^2\); it vanishes strongly* and preserves the classes. For an initial support \(1\) no support enlargement occurs, so the corrected support stays exactly \(1\).

There is also the minimal-projection case, without a matrix-factor classification premise. CQ6, using the scalar ultraweak limit from Proposition 2.1 and (6), shows that \(M_\omega=\mathbb C\) for any factor with a minimal projection, hence for every type I factor. A nonzero equivalent orthogonal quotient partition of size \(m>1\) cannot exist in this scalar algebra. The size-one case is precisely Lemma 4.1. The finite factors without a minimal projection are the type \(\mathrm{II}_1\) case just handled. These cases cover the whole factor setting.

Finally let \((E_{ij})\) be the specified finite matrix system and \(Q=\sum_jE_{jj}\). If \(Q=0\), all \(E_{ij}\) are zero since \(E_{ij}^*E_{ij}=E_{jj}\); use the zero coordinate system. Otherwise lift and balance the diagonal partition as above. The corrected coordinate endpoints are equivalent at every coordinate, so Theorem 5.1 lifts each \(E_{j1}\) to \(v_j(n)\) with initial support \(e_1(n)\) and final support \(e_j(n)\). Choose \(v_1(n)=e_1(n)\), and put
\[
e_{ij}(n)=v_i(n)v_j(n)^*.
\tag{31}
\]
Exercise 8's full calculation proves all matrix-unit products and adjoints. Centralizing is preserved under these products, their images are \(E_{i1}E_{1j}=E_{ij}\), and their diagonal sum is the corrected support \(q_n\). In the unital case this support is exactly \(1\); in the nonunital case it still represents \(Q\). \(\square\)

**Exercise 10.** \(B(H)\) contains matrix units, including infinitely many when \(H\) is infinite-dimensional. Why does \(B(H)_\omega=\mathbb C\) not contradict this, and what prevents a varying centralizing sequence from leaving a nonscalar class?

*Solution.* A fixed matrix unit gives a constant bounded sequence, but constancy alone does not satisfy (3). If a constant sequence does satisfy (3), its commutators with all normal functionals vanish identically; the separation argument of Proposition 2.1 makes the fixed operator central and hence scalar in \(B(H)\). Thus the original matrix units are not automatically quotient matrix units.

For a varying bounded sequence, let \(p_j\) project onto a basis vector \(\xi_j\). The scalar ultraweak limit is \(\lambda1\), and (6) supplies the rank-one commutator test
\[
(x_n-\lambda)\xi_j
=[x_n,p_j]\xi_j+
(\langle\xi_j,x_n\xi_j\rangle-\lambda)\xi_j
\to_\omega0.
\tag{30}
\]
Apply the same formula to adjoints. Uniform boundedness extends it from finite linear combinations of basis vectors to every vector, giving strong*-zero distance from \(\lambda1\). The finite-dimensional case uses the finite basis and has the same conclusion. The lifting theorem starts with matrix units already in the quotient; the scalar quotient has no nonzero system of size greater than one to lift.

<a id="references"></a>

## Free proofs and method comparisons

The quotient norm, faithful trace representation, whole-domain normality, finite cancellation, small infinite pieces, minimal-projection test and partition error are proved in [CQ1–7](../components/central-sequence-quotient-and-lifting-inputs.md). Their complete earlier inputs are the retained CF, CP, SC, BD, PC, FCT, NT and AF arguments, with their existing notices. This supplies the construction before any appeal to an external ultraproduct theorem.

Alain Connes, [*Outer conjugacy classes of automorphisms of factors*](https://www.numdam.org/articles/10.24033/asens.1295/), Propositions 1.1.1–1.1.3 and Lemmas 1.1.4–1.1.5, printed pp.387–390 (PDF pp.6–9), is the historical free comparison for the scalar trace and exact repairs. Proposition 1.1.1 recalls an earlier result rather than proving completeness there. Proposition 1.1.3(b) explicitly requires equivalent coordinate endpoints. Its proof removes small pieces at both infinite endpoints; our repair instead removes a piece and its image from the polar partial isometry, controlling both state masses. We use a fixed cutoff \(1/2\), prove finite-subpiece cancellation through a finite join, and retain every nonunital matrix support.

Adrian Ocneanu, [*Actions of discrete amenable groups on factors*](https://wrap.warwick.ac.uk/id/eprint/110062/), Chapter 5, Section 5.1, printed pp.47–50 (PDF pp.61–64), proves completeness and normality for the normalizer ultraproduct and its centralizing subalgebra. The objects there are distinguished: the normalizer quotient is larger. Our proof constructs only the centralizing quotient, using its tracial metric and predual tests, and obtains normal automorphisms by their trace Hilbert unitaries.

Hiroshi Ando and Uffe Haagerup, [*Ultraproducts of von Neumann algebras*](https://arxiv.org/pdf/1212.5457v3), v3, Section 3.1 and Propositions 3.14–3.15, gives the complementary normalizer/corner construction. Its hereditary-subalgebra and modular prerequisites are not premises of the proofs here. The mathematical comparisons use the actual free editions; no external source prose or figure is reproduced.
