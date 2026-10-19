# Central sequences, fullness and free group factors

*Written by GPT-6.1 Sol (OpenAI), Ultra. Course exposition: CC0-1.0 to the extent of rights held. Human comparison sources retain their own terms.*

How much can two commutators reveal about an operator? In a free-group factor they bound its entire distance from the scalars. In the dyadic tensor factor \(R\), a unitary can instead escape into a later tensor position, commute asymptotically with every fixed operator, and stay a definite distance from every scalar.

We compute these examples first, then relate their behavior to the topology of automorphism groups, retaining the whole center for algebras that are not factors.

<a id="7-exercises-with-complete-solutions"></a>

The problems are interleaved with the arguments they test. Every problem has its complete solution immediately below it. The [foundations](../components/central-sequence-foundations.md) prove the normal-functional, faithful-state, metric, Borel-image and phase constructions, and the two factor constructions used here.

<a id="5-an-explicit-free-group-gap"></a>

## Two generators control the distance from the scalars

Let \(\Gamma=\mathbb F_n\), \(2\leq n\leq\infty\), and choose distinct generators \(a,b\). Its reduced words give the group operations; the [free-word construction](free-group-norm-averaging.md#free-word-and-operator-inputs) establishes the cancellation and uniqueness rules for every generator set. Put \(L(\Gamma)=\lambda(\Gamma)''\), where
\(\lambda_g\delta_h=\delta_{gh}\) on \(\ell^2(\Gamma)\).

[FG1](../components/central-sequence-foundations.md#fg1-countable-group-von-neumann) constructs the faithful normal trace
\(\tau(x)=\langle\delta_e,x\delta_e\rangle\), proves separability of the predual, and proves the coefficient identity
\[
\|x-\tau(x)1\|_2^2=\sum_{g\ne e}|\widehat x(g)|^2,
\qquad
\widehat x(g)=\langle\delta_g,x\delta_e\rangle.
\tag{21}
\]
It also proves that an infinite countable ICC group gives a factor of type \(\mathrm{II}_1\).

Here is the required ICC check. If \(g\ne e\) is not an \(a\)-power, strip its maximal initial and final \(a\)-runs to write \(g=a^rwa^s\), where \(w\) is nonempty and neither endpoint is an \(a\)-letter. For all sufficiently large positive \(k\), the conjugate
\(a^kga^{-k}=a^{k+r}wa^{s-k}\)
has initial run of length \(k+r\) and final negative run of length \(k-s\). Distinct such \(k\) give distinct reduced words. If \(g\) is a nonzero \(a\)-power, its conjugates by positive \(b\)-powers are distinct instead. Every nonidentity conjugacy class is therefore infinite.

**Theorem 5.1.** For every \(x\in L(\Gamma)\),
\[
\|x-\tau(x)1\|_2
\le14\max\{\|[x,\lambda_a]\|_2,\|[x,\lambda_b]\|_2\}.
\tag{22}
\]

**Proof.** We prove the stronger bound \(10\delta\), where
\(\delta=\max(\|[x,\lambda_a]\|_2,\|[x,\lambda_b]\|_2)\).
Let \(\eta\) be the coefficient vector of \(x-\tau(x)1\) on \(\Gamma\setminus\{e\}\), and put \(r=\|\eta\|_2\). For a set \(A\) of nonidentity words, let \(P_A\) be the coordinate projection onto \(\ell^2(A)\).
Conjugation by \(h\) permutes this Hilbert basis; write the resulting unitary as \(C_h\). FG1's coefficient identity gives
\[
\|C_h\eta-\eta\|_2=\|[x,\lambda_h]\|_2.
\]
The values for \(h=b\) and \(h=b^{-1}\) agree, by applying the unitary \(C_b\) to their difference.

Let \(S\) consist of words ending in \(a\) or \(a^{-1}\). A word outside \(S\) ends in a different letter; conjugating it by \(a^{-1}\) leaves an \(a\) at the right endpoint. Hence
\[
S\cup aSa^{-1}=\Gamma\setminus\{e\}.
\tag{23}
\]
In contrast, the sets
\[
S,\qquad bSb^{-1},\qquad b^{-1}Sb
\tag{24}
\]
are disjoint. The last two have respectively a final \(b^{-1}\)-run and a final \(b\)-run of length one. The terminal \(a\)-letter prevents right cancellation, and left cancellation cannot pass that letter. These are the free-word geometric inputs.

Put \(t=\|P_S\eta\|_2\) and \(t_h=\|P_{hSh^{-1}}\eta\|_2\). Since
\(P_{hSh^{-1}}C_h\eta=C_hP_S\eta\), the reverse triangle inequality on that coordinate subspace gives
\( |t_h-t|\leq\delta\) for \(h=a,b,b^{-1}\).
The cover in (23) controls the entire vector by two coordinate pieces, even if they overlap:
\[
r^2\leq t^2+t_a^2\leq t^2+(t+\delta)^2.
\tag{25}
\]
The three projections in (24) have mutually orthogonal ranges. Pythagoras therefore gives the estimate in the other direction,
\[
r^2\geq t^2+t_b^2+t_{b^{-1}}^2
\geq t^2+2\max\{t-\delta,0\}^2.
\tag{27}
\]

If \(\delta=0\), these inequalities give \(3t^2\leq r^2\leq2t^2\), so \(r=0\). Suppose \(\delta>0\). For \(t<\delta\), (25) gives \(r^2<5\delta^2\). For \(t\geq\delta\), combine (25) and (27) and expand to obtain
\[
t^2-6t\delta+\delta^2\leq0.
\]
In particular \(t\leq6\delta\), and (25) gives
\(r^2\leq(36+49)\delta^2=85\delta^2<100\delta^2\).
Thus \(r\leq10\delta\leq14\delta\) in every case. Equation (21) identifies \(r\) with the distance in (22). \(\square\)

**Exercise 7.** Decide whether the cover (23) needs disjoint sets. State and justify the direction of the measure inequality it supplies; compare it with the three-set estimate.

*Solution.* For comparison with measures, set
\(\mu(A)=\|P_A\eta\|_2^2=\sum_{g\in A}|\widehat x(g)|^2\) and \(k=\mu(\Gamma\setminus\{e\})=r^2\).
The word \(a\) lies in \(S\) and in \(aSa^{-1}\), because conjugating \(a\) by \(a\) leaves it unchanged. This overlap is allowed. The cover gives
\[
k=\mu(S\cup aSa^{-1})\leq\mu(S)+\mu(aSa^{-1}),
\]
which is exactly the first inequality in (25). The three sets in (24) are pairwise disjoint subsets of the total space. Their measures therefore add without overlap, and their sum is at most \(k\), as in (27). The cover supplies a lower bound on the sum of two squared coordinate norms; disjointness supplies an upper bound on the sum of three. Neither inequality may be reversed. Their combination, with the coordinate norm error at most \(\delta\), yields the scalar-distance bound.

**Exercise 8.** Suppose the \(a\)-commutator has \(2\)-norm at most \(10^{-3}\), and the \(b\)-commutator has \(2\)-norm at most \(2\cdot10^{-3}\). Find the certified scalar approximation, including its error, and prove that its scalar minimizes the \(2\)-norm distance.

*Solution.* The larger commutator bound is \(0.002\), hence (22) gives
\(\|x-\tau(x)1\|_2\leq14(0.002)=0.028\).
For every \(c\in\mathbb C\), expanding the trace and using
\(\tau(x-\tau(x)1)=0\) gives
\[
\|x-c1\|_2^2
=\|x-\tau(x)1\|_2^2+|c-\tau(x)|^2.
\]
The second term has its unique minimum at \(c=\tau(x)\). Equivalently, this is orthogonal projection onto \(\mathbb C1\) in the trace Hilbert space.

## A tensor tail defeats any scalar approximation

[FG2](../components/central-sequence-foundations.md#fg2-tracial-dyadic-product) constructs \(R\) from \(M_{2^n}\), their normalized traces and their tracial Hilbert completion. It proves trace faithfulness, factoriality, type \(\mathrm{II}_1\), separable predual and the bounded approximation
\(\|E_n(x)-x\|_2\to0\) by the first \(n\) tensor positions. These properties follow from the local matrix construction itself.

Let \(z_m\) put \(\operatorname{diag}(1,-1)\) at position \(m\). If \(m>n\), it commutes with \(E_n(x)\), so
\[
\|[z_m,x]\|_2\leq2\|x-E_n(x)\|_2.
\]
Given \(x\), first choose \(n\) to make the right side small and then take \(m>n\). Also \(\tau(z_m)=0\) and \(z_m\) is unitary, whence
\[
\|z_m-c1\|_2^2=1+|c|^2.
\tag{28}
\]
This gives the opposite of the free-group estimate. Below we show why the distinction is exactly a failure of fullness.

**Exercise 9.** Allow the scalar approximant to vary with \(m\). Prove that the tensor-tail unitaries still form a nontrivial sequence, including the passage from \(2\)-norm to bounded strong* convergence.

*Solution.* The trace of each \(z_m\) is zero, and
\(\tau(z_m^*z_m)=1\). Thus any choice \(c_m\in\mathbb C\) satisfies
\(\|z_m-c_m1\|_2^2=1+|c_m|^2\geq1\).
If the scalar approximants are bounded, the differences are bounded too. NT2 proves that bounded intrinsic strong* convergence forces trace \(2\)-norm convergence, by using the trace as a test; the latter is impossible here. Since FG2 proves \(Z(R)=\mathbb C1\), this excludes every allowed bounded central approximating sequence.

<a id="1-two-meanings-of-almost-commuting"></a>

## Which commutators test a sequence?

For \(\omega\in M_*\), fix the module convention
\[
(x\omega)(y)=\omega(yx),\qquad
(\omega x)(y)=\omega(xy),\qquad
[x,\omega]=x\omega-\omega x.
\tag{1}
\]
A norm-bounded sequence is **centralizing** when
\(\|[x_n,\omega]\|\to0\) for every \(\omega\in M_*\).
It is **central** when \([x_n,a]\to0\) intrinsic strong* for every \(a\in M\). Here intrinsic strong* on bounded sets tests both
\(\|x\|_\psi=\psi(x^*x)^{1/2}\) and \(\|x^*\|_\psi\) for every positive normal \(\psi\).
A sequence is **trivial** when \(x_n-a_n\to0\) in that topology for a bounded sequence \(a_n\in Z(M)\).

**Lemma 1.1.** Every centralizing sequence is central. If \(M\) has a faithful normal state \(\varphi\), a central sequence is centralizing whenever \(\|[x_n,\varphi]\|\to0\).

**Proof.** For fixed \(x,a\) and positive normal \(\psi\), put \(c=xa-ax\). Expanding (1) gives the exact identity
\[
\psi(c^*c)
=[x,a\psi](a^*x^*-x^*a^*)
 +[x,\psi](x^*a^*a-a^*x^*a).
\]
The first test variable has norm at most \(2\|a\|\|x\|\), and the second at most \(2\|a\|^2\|x\|\). Therefore
\[
\psi([x,a]^*[x,a])
\leq2\|x\|\|a\|\|[x,a\psi]\|
 +2\|x\|\|a\|^2\|[x,\psi]\|.
\tag{2}
\]
NT1 supplies the bounded module functionals appearing here. If the sequence is centralizing and bounded, both terms tend to zero. The functional involution
\(\omega^*(y)=\overline{\omega(y^*)}\) satisfies
\[
[x,\omega]^*=-[x^*,\omega^*],
\qquad \|[x^*,\omega]\|=\|[x,\omega^*]\|.
\tag{3}
\]
It follows that \(x_n^*\) is centralizing as well. Apply (2) with \(x_n^*,a^*\) to obtain the adjoint seminorm of the original commutator. Both tests now vanish.

For the state converse, NT1 proves that \(M\varphi\) is norm dense in \(M_*\) when \(\varphi\) is faithful. The identity
\[
[x_n,a\varphi]=[x_n,a]\varphi+a[x_n,\varphi]
\tag{4}
\]
reduces the dense family to the assumed two kinds of convergence. Indeed Schwarz gives
\[
\|b\varphi\|\leq\varphi(1)^{1/2}\|b\|_\varphi.
\tag{5}
\]
Centrality makes the first term of (4) tend to zero; the stated state-commutator assumption controls the second. If \(\sup_n\|x_n\|=C\), the estimate
\(\|[x_n,\omega]\|\leq2C\|\omega\|\) extends convergence from \(M\varphi\) to its norm closure. \(\square\)

**Exercise 1.** Prove the product rule for convention (1). Give a matrix example showing why a vanishing commutator with one faithful state, without centrality, does not suffice.

*Solution.* At a test element \(t\),
\[
\begin{aligned}
x[y,\omega](t)&=\omega(txy)-\omega(ytx),\\
[x,\omega]y(t)&=\omega(ytx)-\omega(xyt).
\end{aligned}
\]
Adding cancels the middle values and gives
\[
[xy,\omega]=x[y,\omega]+[x,\omega]y.
\tag{7}
\]
In \(M_2(\mathbb C)\), take \(x=\operatorname{diag}(1,-1)\) and the faithful normalized trace. Traciality makes \([x,\tau]=0\), but \(xe_{12}-e_{12}x=2e_{12}\ne0\). The constant sequence \(x_n=x\) is not central. Lemma 1.1's first implication then shows it is not centralizing either. The state test alone misses this obstruction.

**Exercise 2.** Show that \(M\varphi\) is norm dense for a faithful normal state. For a nonfaithful state, identify an explicit nonzero annihilator and the exact support obstruction.

*Solution.* The concrete duality \(M=(M_*)^*\) is proved in CP. A dual element \(y\) annihilating \(M\varphi\) obeys \(\varphi(ya)=0\) for all \(a\in M\). Testing \(a=y^*\) gives \(\varphi(yy^*)=0\), so faithfulness gives \(y=0\). If the norm closure were proper, Hahn–Banach would supply a nonzero annihilator; thus the closure is all of \(M_*\).
For a nonfaithful \(\varphi\), NT4 constructs \(p=s(\varphi)\ne1\) with \(\varphi(1-p)=0\). Schwarz gives \(\varphi((1-p)a)=0\) for every \(a\). Hence \(y=1-p\ne0\) annihilates \(M\varphi\), and the norm closure is proper. The support being one is equivalent to faithfulness, so this is precisely the obstruction.

**Corollary 1.2.** In every finite von Neumann algebra, central and centralizing bounded sequences coincide. No separability or countable decomposition is required.

**Proof.** In the presence of a faithful normal tracial state, the additional state commutator in Lemma 1.1 is zero, so centrality implies centralizing. For the general finite case, the complete [FCT0–7 construction](../components/central-finite-trace-inputs.md#retained-fct-complete-inputs) gives the faithful normal center-valued trace \(T_Z:M\to Z(M)\). Its projection and central-corner inputs [PC0–7](../components/central-finite-trace-inputs.md#retained-pc-complete-inputs) are retained in the same component; neither proof requires countable decomposition. Fix \(0\ne\psi\in M_*^+\) and use NT4 on the center to obtain \(z=s(\psi|_{Z(M)})\). The functional
\[
\tau_z(x)=\frac{\psi(T_Z(x))}{\psi(z)},\qquad x\in Mz,
\tag{6}
\]
is normal and tracial. It is faithful because both the trace map and \(\psi|_{Z(M)z}\) are faithful. Its value at the corner unit \(z\) is one. The bounded central sequence \(zx_n\) is therefore centralizing in \(Mz\), by the state case.
NT4 also gives \(\psi(y)=\psi(zyz)\). Since \(z\) is central, evaluating the predual commutator against \(y\) is the same as evaluating the corner commutator against \(zyz\); this compression has norm at most \(\|y\|\). Thus \(\|[x_n,\psi]\|\to0\). NT1's four-positive decomposition extends the assertion to every normal functional. Lemma 1.1 gives the reverse implication on any algebra. \(\square\)

Before using unitary sequences, note that centralizing bounded sequences form a unital C-star algebra in \(\ell^\infty(\mathbb N,M)\). Equation (3) handles adjoints, (7) handles products, and the \(2C\)-commutator estimate handles norm limits. CF's continuous calculus therefore stays inside this algebra. For a centralizing self-adjoint contraction \(h_n\),
\[
w_n=h_n+i(1-h_n^2)^{1/2}
\tag{8}
\]
is a centralizing unitary with real part \(h_n\). Taking real and imaginary parts of any bounded sequence, scaling by a common bound and using (8), expresses it as a linear combination of four centralizing unitary sequences, with fixed bounded coefficients.

<a id="2-complete-metrics-for-the-relevant-groups"></a>

## Automorphisms and their implementing cosets

Assume \(M_*\) is separable and \(M\ne0\). NT2 constructs a faithful normal state \(\varphi\) and proves that its two bounded seminorms give intrinsic strong*. For an arbitrary separable Banach space \(X\), choose \((\xi_j)\) dense in its unit ball. On its surjective linear isometries use
\[
d(S,T)=\sum_{j\geq1}2^{-j}
\bigl(\|S\xi_j-T\xi_j\|+\|S^{-1}\xi_j-T^{-1}\xi_j\|\bigr).
\tag{9}
\]
The sum is finite, and its coordinates separate the maps. Coordinate convergence is equivalent to pointwise norm convergence of maps and inverses, by their common isometric bound; tails of the sum are uniformly bounded.

A Cauchy sequence has pointwise isometric limits \(S,R\) for the maps and inverses. The equality
\(\|S_nR\xi-\xi\|=\|R\xi-S_n^{-1}\xi\|\)
and passage to the limit give \(SR=1\); exchanging the roles gives \(RS=1\). Thus (9) is complete. Its coordinate embedding lies in a countable product of separable metric spaces, which TS1 makes second countable; its subspace is separable. The estimate for compositions of two isometries proves joint continuity of multiplication. If \(S_n\to S\) pointwise and \(S\) is onto,
\(\|S_n^{-1}\xi-S^{-1}\xi\|=\|\xi-S_nS^{-1}\xi\|\to0\),
which also proves continuity of inversion. The isometry group is Polish.

Give \(\operatorname{Aut}(M)\) its \(u\)-topology,
\[
\alpha_n\to\alpha\ \Longleftrightarrow\
\|\omega\circ\alpha_n-\omega\circ\alpha\|\to0
\quad(\omega\in M_*).
\tag{10}
\]
For \(T_\alpha\omega=\omega\circ\alpha^{-1}\), composition shows \(T_{\alpha\beta}=T_\alpha T_\beta\). The map is injective and takes values in the isometry group of \(M_*\).

**Lemma 2.1.** This image is closed. Consequently \(\operatorname{Aut}(M)\) is a Polish group, with a complete metric obtained from (9).

**Proof.** Suppose \(T_{\alpha_n}\) converges to a surjective isometry \(T\). Its inverse also converges pointwise. Put
\(\beta=(T^{-1})^*\), \(\gamma=T^*\). Concrete predual duality makes these inverse normal linear maps on \(M\). Their pointwise ultraweak limits are respectively \(\alpha_n,\alpha_n^{-1}\). Vector tests on every finite matrix level show that these limits remain unital completely positive.
NT1 proves Schwarz from a positive \(2\times2\) block. Applying it successively gives
\[
x^*x=\gamma\beta(x^*x)
\geq\gamma(\beta(x)^*\beta(x))
\geq x^*x.
\]
The two positive differences vanish. Injectivity of \(\gamma\) forces
\(\beta(x^*x)=\beta(x)^*\beta(x)\).
Polarize this equality using \(x+y\) and \(x+iy\) to get
\(\beta(x^*y)=\beta(x)^*\beta(y)\).
Positivity preserves adjoints, so \(\beta\) is a star homomorphism; \(\gamma\) is its normal inverse. Thus \(T=T_\beta\), proving closedness. A closed subspace of the complete metric space is complete. The preceding inverse-coordinate identity shows that the induced topology is exactly (10). \(\square\)

For the unitaries put
\[
D(u,v)=\|u-v\|_\varphi+\|u^*-v^*\|_\varphi.
\tag{11}
\]
Faithfulness makes this a metric, and NT2 identifies its topology with bounded intrinsic strong*. In the faithful GNS representation, a bounded family converging on \(\Omega\) converges strongly on the dense orbit \(M'\Omega\), by commutation, and hence on the whole Hilbert space. This justifies both seminorm tests. For a unitary limit, strong convergence alone also controls adjoints:
\[
(u_n^*-u^*)\xi=u_n^*(u-u_n)u^*\xi.
\tag{12}
\]
NT2 proves separability of this GNS Hilbert space. Evaluations of operators and adjoints on a countable dense set embed the bounded strong* topology into a countable product of separable Hilbert spaces. The unitary group is consequently separable.

**Lemma 2.2.** Metric (11) is complete, and
\[
\mathcal U(M)/\mathcal U(Z(M))
\tag{13}
\]
is a Polish group with the complete quotient metric
\[
\rho(u\,\mathcal U(Z),v\,\mathcal U(Z))
=\inf_{z\in\mathcal U(Z)}D(u,vz).
\tag{14}
\]

**Proof.** A \(D\)-Cauchy sequence gives Cauchy values \(u_n\Omega,u_n^*\Omega\). Commuting with \(M'\) extends these to Cauchy vectors on its dense orbit; the norm-one bound extends the limits to all vectors. Strong closedness puts the bounded limits \(u,w\) in \(M\). Passing to the Hilbert pairing shows \(w=u^*\). Strong continuity of multiplication on bounded sets then gives \(u^*u=uu^*=1\), so the limit is unitary and the metric complete.

Right multiplication by a central unitary preserves both terms of \(D\): for a difference \(x\), it leaves \(x^*x\) and \(xx^*\) unchanged. Consequently (14) does not depend on representatives. Aligning representatives for two consecutive distances proves its triangle inequality; reversing the alignment proves symmetry. If \(\rho=0\), choose \(z_n\) with \(vz_n\to u\) strong*. Then \(z_n\to v^*u\), and the strong* closed central unitary group contains this limit. Thus the cosets are equal.
The image of a \(D\)-ball is exactly the corresponding \(\rho\)-ball; the quotient map is open because its full preimage is the union of central translates of that ball. Hence this is the quotient topology. From a \(\rho\)-Cauchy sequence choose a subsequence whose consecutive distances are less than \(2^{-j-2}\). Successive central adjustments give representatives with \(D\)-increments less than \(2^{-j-1}\). Completeness gives a representative limit, then a coset limit. The entire Cauchy sequence converges by the triangle inequality. The quotient is separable, and its group operations are continuous: products and inversion descend through the open quotient map and the subgroup is normal. \(\square\)

The quotient-metric argument applies to a complete metric invariant under right multiplication by any closed subgroup, with left cosets as its orbits. Complete metrizability of a Polish group also implies completeness for its two-sided group uniformity. Exercise 4 proves that implication and distinguishes it from one-sided completeness.

**Exercise 3.** Construct unitaries converging strongly to a nonunitary on \(\ell^2(\mathbb N_0)\). Show that they are strong Cauchy and that their adjoints fail the metric (11) for a faithful diagonal state.

*Solution.* Let \(u_n\) cycle \(e_0,\ldots,e_n\) forward, taking \(e_n\) to \(e_0\), and fix \(e_j\) for \(j>n\). On each fixed finite-support vector, eventually this agrees with the unilateral shift \(S e_j=e_{j+1}\). The norm-one bound extends the convergence to every vector, so \(u_n\to S\) strongly and is strong Cauchy. The range of \(S\) omits \(e_0\), so the limit is not unitary. However \(u_n^*e_0=e_n\). For \(n\ne m\) these vectors have squared distance two. For the faithful normal state
\(\varphi(x)=\sum_{j\geq0}2^{-j-1}\langle e_j,xe_j\rangle\),
the adjoint term satisfies
\(\|u_n^*-u_m^*\|_\varphi^2\geq2^{-1}\|e_n-e_m\|^2=1\).
Thus the sequence fails to be \(D\)-Cauchy. Both convergence tests are necessary for completeness.

**Exercise 4.** Explain the role of centrality in the quotient metric. State what completeness of a compatible metric permits one to infer about the two-sided group uniformity.

*Solution.* If \(z\) is central unitary and \(x=u-v\), then
\((xz)^*(xz)=x^*x\) and \((xz)(xz)^*=xx^*\).
For a noncentral right multiplier, the first expression becomes \(z^*x^*xz\); a general faithful state changes under this conjugation. For a left multiplier the other square instead changes. Central multipliers therefore give the simultaneous invariance used to align representatives in (14).

A Polish group is complete for its **two-sided group uniformity**: a sequence \((g_j)\) is Cauchy for that uniformity when both \(g_j^{-1}g_k\) and \(g_jg_k^{-1}\) tend to one uniformly over pairs of sufficiently large indices. This is called Raikov completeness. A compatible complete metric need not be invariant, so we prove the implication rather than identify its Cauchy sequences with the group-uniformity Cauchy sequences.

First construct a bounded compatible left-invariant metric. Choose symmetric identity neighborhoods \(V_0=G,V_1,V_2,\ldots\), forming a neighborhood base and satisfying \(V_{n+1}^3\subset V_n\). Such a sequence is obtained successively from a countable base and continuity of multiplication and inversion. Define
\[
d_L(g,h)=\inf\left\{\sum_{i=1}^m2^{-n_i}:
g^{-1}h=v_1\cdots v_m,\quad v_i\in V_{n_i}\right\}.
\]
The empty product has cost zero. Every other group element has a factorization of cost at most one, using \(V_0\). Reversing a factorization and taking inverses proves symmetry; concatenating factorizations proves the triangle inequality. Left invariance follows from the occurrence of \(g^{-1}h\).

Here is the bound that prevents this infimum from collapsing. If an ordered product has total cost less than \(2^{-n}\), its product lies in \(V_n\). Prove this by induction on the number of factors, simultaneously for every \(n\). For one factor the assertion follows from nesting. For more factors, choose a factor at a weighted median: the total costs strictly before and strictly after it are each at most half the total. By induction both surrounding products belong to \(V_{n+1}\). The middle factor also belongs to \(V_{n+1}\), since its own cost is less than \(2^{-n}\). The three-factor inclusion gives the assertion. Empty surrounding products cause no exception. Consequently
\[
V_{n+1}\subset B_{d_L}(1,2^{-n})\subset V_n.
\]
Their intersection is \(\{1\}\), so \(d_L\) separates points and induces the group topology.

Let \(X\) be the metric completion of \((G,d_L)\). Explicitly, identify two Cauchy sequences when their pointwise distances tend to zero and define distance between classes by the limit of those distances. The triangle inequality makes the limit and equivalence well defined; constant sequences embed \(G\) densely. A Cauchy sequence of classes has a subsequence with successive distances below \(2^{-j}\). Choose representatives from \(G\) within \(2^{-j}\) of those classes. They are Cauchy and define the required limit class; the original Cauchy sequence then has the same limit. This proves completeness. A countable dense subset of \(G\) remains dense in \(X\), so \(X\) is separable.

The surjective isometry group of any complete separable metric space \((X,d_X)\) is Polish. To verify this without a completeness assumption about a group uniformity, choose a dense sequence \((\xi_j)\) and use
\[
d_I(S,T)=\sum_{j\geq1}2^{-j}
\left(\min\{1,d_X(S\xi_j,T\xi_j)\}
+\min\{1,d_X(S^{-1}\xi_j,T^{-1}\xi_j)\}\right).
\]
The common isometry bound extends coordinate convergence and coordinate Cauchy convergence to every point of \(X\). For a Cauchy sequence, completeness of \(X\) gives pointwise isometric limits \(S,R\) for the maps and inverses. The equality
\[
d_X(S_nR\xi,\xi)=d_X(R\xi,S_n^{-1}\xi)
\]
gives \(SR=1\); exchanging maps and inverses gives \(RS=1\). Thus the limit is a surjective isometry. Uniformly bounded tails of the displayed sum prove convergence in \(d_I\). Its coordinate embedding in \(X^{\mathbb N}\times X^{\mathbb N}\) gives second countability and separability by TS1. Inversion swaps the two coordinate families; the triangle inequality and the isometry bound prove continuity of composition. This proves the assertion about the isometry group.

Left translation by \(g\) is a surjective isometry of \((G,d_L)\), and hence extends uniquely to a surjective isometry \(L_g\) of \(X\). These maps give a faithful homomorphism. For \(x\in G\),
\[
d_L(gx,hx)=d_L(1,x^{-1}g^{-1}hx).
\]
Continuity of conjugation, also for the inverse-coordinate maps, proves continuity into the isometry group on this dense subset. The common isometry bound extends it to all of \(X\). Evaluation at \(1\in G\) recovers the metric \(d_L(g,h)\), so this embedding induces exactly the original topology on \(G\).

We need its image to be closed. Let \(H\) be the closure of the image in the complete isometry group; this is a Polish group. Identify \(G\) with its image and let \(d_0\) be a compatible complete metric on \(G\). For every \(n\), let \(O_n\) be the union of the open subsets \(U\) of \(H\) for which the \(d_0\)-diameter of \(U\cap G\) is less than \(2^{-n}\). Compatibility of the topologies gives \(G\subset O_n\). In fact
\[
G=\bigcap_n O_n.
\]
For a point \(h\) in the intersection, choose such a neighborhood \(U_n\) containing \(h\), and choose \(g_j\in G\) in \(U_1\cap\cdots\cap U_j\) and within \(1/j\) of \(h\) in a metric of \(H\). Density permits every choice. For \(j,k\geq n\), both points lie in \(U_n\), so \((g_j)\) is \(d_0\)-Cauchy. It converges to a point of \(G\); compatibility and uniqueness of its limit in \(H\) identify that point with \(h\). This proves the equality. Each \(O_n\) is open and dense in \(H\), so \(G\) is comeager there. Every translate \(hG\) is also comeager. The Baire theorem TS5 gives a point in \(G\cap hG\), whence \(h\in GG^{-1}=G\). Thus \(G=H\), proving closedness.

Now let \((g_j)\) be two-sided Cauchy. For every \(x\in G\), the preceding conjugation formula makes \((L_{g_j}x)\) Cauchy in \(X\). Applying it to \(g_j^{-1},g_k^{-1}\) uses \(g_jg_k^{-1}\) and makes the inverse-coordinate sequence Cauchy as well. Density and the common isometry bound extend both assertions to every \(x\in X\). Thus \((L_{g_j})\) is \(d_I\)-Cauchy. It converges in the isometry group, and the closed-image result puts the limit in \(G\). The embedding then gives convergence in the original group topology.

This also proves completeness for Cauchy filters, the uniform-space formulation. The identity has a countable neighborhood base. From a Cauchy filter choose nested filter members whose pairs lie in the first \(n\) basic two-sided entourages, and choose a point in each member. The resulting sequence is two-sided Cauchy and converges by the argument just given. For any entourage choose a smaller one whose square lies in it; one sufficiently small filter member and a sufficiently late chosen point then put that entire member in the prescribed neighborhood of the limit. Hence the filter converges.

One-sided completeness is different. In Exercise 3, the unitary cycles satisfy
\[
\|(u_j^*u_k-1)\xi\|=\|(u_k-u_j)\xi\|\longrightarrow0
\]
uniformly over late pairs for every fixed vector. For a unitary \(w\), \(\|(w^*-1)\xi\|=\|(w-1)\xi\|\), so these relative unitaries tend to one in the group topology. The sequence is left Cauchy. The opposite relative differences test the adjoints, which fail to be Cauchy on \(e_0\). Its strong limit is the unilateral shift, outside the unitary group; it therefore has no group limit. This gives a Polish group whose left uniformity is incomplete. Inversion gives the corresponding right-uniformity example. The direct lifting proof below uses summable increments in both faithful-state seminorms.

For implementers, the module convention gives
\[
\|\omega\circ\operatorname{Ad}u-\omega\|=\|[u,\omega]\|.
\tag{15}
\]
Indeed \(\omega\circ\operatorname{Ad}u=u^*\omega u\); left multiplication by \(u\) is a predual isometry and turns its difference from \(\omega\) into \(\omega u-u\omega\).
The map \(u\mapsto\operatorname{Ad}u\) is continuous. At one, Schwarz bounds \([u,\varphi]\) by
\(\varphi(1)^{1/2}(\|u-1\|_\varphi+\|u^*-1\|_\varphi)\).
Equation (4) treats \(a\varphi\), and their norm density and uniform module bound treat every normal functional. Translation proves continuity everywhere. Its kernel consists exactly of the central unitaries.

<a id="3-the-needed-open-mapping-theorem"></a>

## Why the quotient map has a continuous inverse when its image is closed

**Lemma 3.1.** If \(A\) is nonmeager and has the Baire property in a Polish group \(K\), then \(AA^{-1}\) contains a neighborhood of \(1\).

**Proof.** The Baire property gives a nonempty open \(O\) on which \(A\) is comeager. Choose \(a_0\in O\). For \(k\in Oa_0^{-1}\), the point \(ka_0\) lies in \(O\cap kO\), so this intersection is nonempty and open. TS5 proves that a nonempty open subset of a Polish space is not meager. The exceptions to membership in \(A\) and in \(kA\) form a meager set there. Some point therefore has the form \(a=kb\), with \(a,b\in A\). Then \(k=ab^{-1}\), and the open neighborhood \(Oa_0^{-1}\) of one lies in \(AA^{-1}\). \(\square\)

**Theorem 3.2.** A continuous bijective homomorphism between Polish groups is a homeomorphism.

**Proof.** For a neighborhood \(V\) of one in \(G\), continuity of group operations provides an open neighborhood \(W\) with \(WW^{-1}\subset V\). Separability gives a countable translate cover of \(G\) by \(W\): a dense set meets every translate of \(W^{-1}\). Its images cover \(K\). TS5's Baire theorem excludes all those translates being meager, so \(f(W)\) is nonmeager.
TS4 proves the Borel-image theorem for an injective Borel map on any Polish domain; apply it to this continuous bijection and the open Borel set \(W\). Thus \(f(W)\) is Borel, and TS5 proves that it has the Baire property. Lemma 3.1 gives a neighborhood of one inside
\(f(W)f(W)^{-1}\subset f(V)\).
Translating proves that \(f\) is open. Bijectivity then turns openness into continuity of the inverse. These inputs are proved for all Polish groups; no invariant complete metric or local compactness is assumed. \(\square\)

<a id="4-fullness-with-the-center-retained"></a>

## Lifting convergent inner automorphisms

An algebra is **full** if its inner automorphism group \(\operatorname{Int}(M)\) is closed in \(\operatorname{Aut}(M)\) for (10).

**Theorem 4.1.** For every von Neumann algebra with separable predual, the following are equivalent:

1. \(M\) is full.
2. Every bounded centralizing sequence is trivial.
3. Whenever \(\operatorname{Ad}u_n\to\mathrm{id}\), there are central unitaries \(z_n\) with \(D(u_n,z_n)\to0\).

**Proof.** For the zero algebra each group is a singleton and each sequence is zero, so all three assertions hold. Suppose \(M\ne0\).
If the inner subgroup is closed, Lemma 2.1 makes it Polish. Lemma 2.2 gives a Polish domain for the induced continuous bijection
\(\mathcal U(M)/\mathcal U(Z(M))\to\operatorname{Int}(M)\).
Theorem 3.2 makes this bijection a homeomorphism. An implementing sequence for automorphisms tending to the identity has coset distance tending to zero. Choose central unitaries within an error \(1/n\) of those infima to obtain assertion 3.

Equation (15) identifies the sequences in assertion 3 as the centralizing unitary sequences. The four-unitary decomposition (8) then replaces each term of any bounded centralizing sequence by the same fixed linear combination of bounded central unitary approximants. The errors tend to zero in both seminorms, proving assertion 2.

Conversely, assertion 2 gives bounded \(a_n\in Z(M)\) with \(u_n-a_n\to0\) intrinsic strong* whenever \(u_n\) is centralizing and unitary. NT3 constructs the central phase \(z_n\), taking phase one on the zero support, and proves both squared operator inequalities from the scalar bound
\[
|\operatorname{phase}(a)-w|\leq2|a-w|\qquad(|w|=1).
\tag{16}
\]
It does so by bounded polar operators and continuous approximants, including the zero-support case. Applying \(\varphi\) gives \(D(u_n,z_n)\to0\), which is assertion 3.

To finish, assume assertion 3 and let \(\theta\) be in the closure of the inner subgroup. Metrizability turns assertion 3 into continuity at one of the inverse implementing-coset map. In particular, for a faithful positive normal functional \(\psi\) and \(\varepsilon>0\), there is an identity neighborhood \(\mathcal W\) in the \(u\)-topology such that
\[
\operatorname{Ad}v\in\mathcal W
\ \Longrightarrow\
\inf_{z\in\mathcal U(Z(M))}
(\|v-z\|_\psi+\|v^*-z^*\|_\psi)<\varepsilon.
\tag{17}
\]
If no such neighborhood existed, a decreasing countable base would give a sequence contradicting assertion 3, because NT2 identifies the bounded topology for both faithful functionals.

Set \(\psi=\varphi+\varphi\circ\theta\). Choose a sequence \(\operatorname{Ad}v_n\to\theta\) whose consecutive relative automorphisms lie in the neighborhoods for \(\varepsilon=2^{-n}\), and also satisfy
\[
\|\varphi\circ\operatorname{Ad}v_{n+1}-\varphi\circ\theta\|<4^{-n}.
\tag{18}
\]
For precision, start with any convergent implementing sequence. For each predetermined neighborhood, the convergence and continuous group operations supply a common threshold for both indices of a relative automorphism. Choose the \(n\)-th subsequence index above the thresholds for neighborhoods \(n-1,n\), and above the functional threshold for \(4^{-(n-1)}\). This makes all successive choices simultaneous.

Choose central \(c_n\) with
\[
y_n=c_n-v_{n+1}^*v_n,\qquad
\|y_n\|_\psi+\|y_n^*\|_\psi<2^{-n}.
\]
Define \(\gamma_1=1\), \(\gamma_{n+1}=c_n\gamma_n\), and \(u_n=v_n\gamma_n\). Its difference is \(v_{n+1}y_n\gamma_n\). The central unitary \(\gamma_n\) cancels from both squared seminorms. Thus
\[
\|u_{n+1}-u_n\|_\varphi^2
=\varphi(y_n^*y_n)<4^{-n}.
\tag{19}
\]
For the other square use (18), \(\|y_n\|\leq2\), and the \(\varphi\circ\theta\) part of \(\psi\):
\[
\|(u_{n+1}-u_n)^*\|_\varphi^2
=(\varphi\circ\operatorname{Ad}v_{n+1})(y_ny_n^*)
<5\cdot4^{-n}.
\tag{20}
\]
Both increment norms are summable. Lemma 2.2 gives a unitary limit \(u\). Continuity of implementation gives
\(\operatorname{Ad}u=\theta\), since the central adjustments leave every implemented automorphism unchanged. This proves closedness and assertion 1. \(\square\)

**Exercise 5.** Establish (16) also at zero. Then construct a bounded central unitary approximation from a bounded central approximation to any unitary sequence, proving both intrinsic strong* estimates.

*Solution.* For \(a=r\zeta\ne0\), with \(r>0\) and \(|\zeta|=1\),
\(|1-r|\leq|a-w|\) by the reverse triangle inequality, and
\(|\zeta-w|\leq|\zeta-a|+|a-w|\leq2|a-w|\).
At \(a=0\) choose phase one; \(|1-w|\leq2=2|0-w|\).
For a central operator \(a\), NT3 constructs its polar operator inside the center and extends it by one on the kernel to a central unitary \(z\). Its continuous regularizations commute with the unitary \(u\), and their characterwise scalar inequalities pass to bounded strong* limits. This proves
\[
(z-u)^*(z-u)\leq4(a-u)^*(a-u),\qquad
(z-u)(z-u)^*\leq4(a-u)(a-u)^*.
\]
For every positive normal \(\psi\), the two seminorms of \(z-u\) are at most twice the corresponding ones of \(a-u\). Apply this construction at every index. The phases have norm one, and both errors tend to zero, including indices at which the central approximant is zero.

**Corollary 5.2.** Every \(L(\mathbb F_n)\), \(2\le n\le\infty\), is full and is not isomorphic to \(R\).

**Proof.** A bounded centralizing sequence in \(L(\mathbb F_n)\) is central by Lemma 1.1. Use its faithful trace as a seminorm test: the two fixed commutators in (22) tend to zero in \(2\)-norm. Hence
\(\|x_m-\tau(x_m)1\|_2\to0\).
The scalar approximants are bounded by \(\sup_m\|x_m\|\). NT2 gives bounded intrinsic strong* convergence, and FG1 gives separable predual. Theorem 4.1 therefore proves fullness.
In \(R\), FG2's tensor-tail sequence is central, and its commutator with the faithful trace is zero. Lemma 1.1 makes it centralizing. Equation (28) and the scalar center make it nontrivial, so Theorem 4.1 proves that \(R\) is not full. A normal isomorphism preserves centralizing sequences, both intrinsic seminorms and the center, as verified in Exercise 10. It thus preserves fullness, and cannot identify these factors. \(\square\)

This conclusion applies to every rank in the stated range. It does not compare the isomorphism classes of free-group factors of different ranks.

**Exercise 6.** Prove fullness for every abelian von Neumann algebra with separable predual. Give a concrete example showing that the sequence criterion in that case requires its full center.

*Solution.* In an abelian algebra every inner conjugation is the identity. The inner subgroup is the closed singleton in the Hausdorff automorphism group, so the algebra is full. A bounded sequence is trivial by choosing its central approximant equal to itself. In \(\mathbb C^2\), the constant sequence \((1,0)\) is nonscalar and stays a positive distance from the scalar diagonal, although it lies in the center. Thus replacing central approximants by scalar ones would change the criterion.

**Exercise 10.** Prove invariance under a normal isomorphism. Include the predual norms, boundedness, the center, and each of the two strong* seminorms.

*Solution.* Let \(\theta:M\to N\) be a normal star isomorphism. Its normal inverse makes pullback \(\omega\mapsto\omega\circ\theta\) an onto isometry of preduals, and \(\theta\) preserves operator norms. Evaluating against \(\theta(y)\) gives
\[
[\theta(x),\omega]\circ\theta=[x,\omega\circ\theta].
\]
Thus predual-commutator convergence is equivalent in both algebras. For every positive normal \(\psi\) on \(N\),
\[
\|\theta(x)\|_\psi=\|x\|_{\psi\circ\theta},\qquad
\|\theta(x)^*\|_\psi=\|x^*\|_{\psi\circ\theta}.
\]
The onto positive pullback gives both directions of bounded strong* convergence. An element commutes with all of \(M\) exactly when its image commutes with all of \(N\), so \(\theta(Z(M))=Z(N)\). Bounded central approximating sequences transport with identical seminorm errors. Finally the preduals are isomorphic, hence separability transports; Theorem 4.1 gives invariance of fullness.

<a id="6-a-group-algebra-that-is-hyperfinite"></a>

## Finite group stages and the permutation factor

Let \(S_{\mathrm{fin}}\) be the group of permutations of \(\mathbb N\) with finite support. Write \(S_m\) for the permutations of the first \(m\) points, fixing the rest. Then
\[
S_{\mathrm{fin}}=\bigcup_m S_m.
\tag{29}
\]
This countable union of finite sets is countable; the group is infinite.

**Proposition 6.1.** The algebra \(L(S_{\mathrm{fin}})\) is an AFD factor of type \(\mathrm{II}_1\), hence is isomorphic to \(R\).

**Proof.** If \(g\ne e\), choose a point \(i\) moved by \(g\). For each \(j\) outside its finite support, conjugation by \((i\ j)\) changes that support to
\[
(\operatorname{supp}g\setminus\{i\})\cup\{j\}.
\]
The supports are distinct, so the conjugacy class is infinite. FG1 now supplies the faithful normal trace, scalar center, separable predual and type \(\mathrm{II}_1\).
The spans
\(D_m=\operatorname{span}\{\lambda_g:g\in S_m\}\)
are increasing unital finite-dimensional star algebras: finite group multiplication and inversion close them under products and adjoints. Their union contains every group unitary. BD1–5 gives bounded strong density of the norm closure of that union in its bicommutant, so these stages provide the AFD approximation. Equivalently their generated von Neumann algebra is all of \(L(S_{\mathrm{fin}})\). The complete [AF1–5 proof of finite AFD uniqueness](../components/central-afd-uniqueness-inputs.md#af5-full-finite-afd-uniqueness) now identifies it with \(R\), including the initial direct-sum finite algebras and the exact dyadic-containment construction. \(\square\)

The finite stages may be direct sums of matrix algebras. Their centers can disappear when later group elements are added, as the next calculation shows. AF1–5 turns those finite approximations into a compatible dyadic chain; FG2 identifies its tracial completion with \(R\).

**Exercise 11.** Describe the algebra generated by \(S_2\), including its two minimal projections. Exhibit a later group unitary that prevents its nonscalar central element from being central in \(L(S_{\mathrm{fin}})\).

*Solution.* Put \(t=(1\ 2)\). The two group operators \(1,\lambda_t\) are linearly independent on \(\delta_e\), and \(\lambda_t=\lambda_t^*\), \(\lambda_t^2=1\). Thus
\[
p_+=(1+\lambda_t)/2,\qquad p_-=(1-\lambda_t)/2
\]
are nonzero orthogonal projections summing to one. Their spans give an isomorphism of this two-dimensional algebra with \(\mathbb C\oplus\mathbb C\); it is abelian and is not a factor. Take \(s=(2\ 3)\in S_3\). The permutations \(st,ts\) are different, hence
\(\lambda_s\lambda_t\delta_e=\delta_{st}\ne\delta_{ts}=\lambda_t\lambda_s\delta_e\).
So \(\lambda_t\), central in the \(S_2\) stage, is not central after the \(S_3\) stage is included. Centrality in a finite approximant need not survive in the generated algebra.

<a id="references"></a>

## Free comparisons and prerequisite proofs

Claire Anantharaman and Sorin Popa, [*An introduction to II₁ factors*](https://idpoisson.fr/anantharaman/publications/IIun.pdf), author draft, Theorem 15.3.2, printed 266–267 (PDF 272–273), proves the finite-factor fullness route. Section 15.4 on those and the following page gives the free-word cover and disjoint conjugates, and the trace-zero tensor-tail example. Those methods are credited here. The orthogonal coordinate projections give the bound 10 and therefore the stated bound 14; the faithful-state estimates prove the criterion with the whole center.

Christian Rosendal's [author version of *Automatic continuity of group homomorphisms*](https://homepages.math.uic.edu/~rosendal/PapersWebsite/AutomaticContinuity06.pdf), November 2008, Section 2.1, Lemma 2.1 and Theorem 2.2, p.4, gives the category argument. Anush Tserunyan's [author-hosted descriptive-set-theory notes](https://www.math.mcgill.ca/atserunyan/Teaching_notes/dst_lectures.pdf), 26 November 2025, Theorem 12.6 p.48 and Theorem 13.3 pp.51–52, provide complete separation and Borel-image comparisons. TS1–6 proves their metric, refinement and category inputs locally on all Polish domains.

Julien Melleray, [*Some aspects of Topological dynamics of Polish groups, with an introduction to descriptive set theory*](https://math.univ-lyon1.fr/~melleray/Topological_dynamics_of_Polish_groups.pdf), author-hosted notes, Definition 4.1 and Theorem 4.3, printed 39–40 (PDF 45–46), distinguish the group uniformities and the compatible invariant metric. Exercise 48, printed 41 (PDF 47), states Raikov completeness for Polish groups. Exercise 4 here supplies the complete metric, isometric embedding, closed-image and Cauchy-filter arguments. The author’s text retains its own rights.

NT1–4 and FG1–2 provide the functional decomposition, faithful-state topology, bounded phase construction, support localization and the two factor constructions. Their exact earlier CF, CP, GNS, bounded-density and normal-range proofs are linked in the foundations. The complete retained PC0–7/FCT0–7 arguments supply Corollary 1.2's general finite center-valued trace. Their method comparison is Jesse Peterson's [author-hosted *Notes on operator algebras*](https://math.vanderbilt.edu/peters10/teaching/spring2020/OperatorAlgebras.pdf), 27 April 2020, Section 6.4, printed/PDF 102–106. AF1–5 proves the whole finite AFD uniqueness input for Proposition 6.1. Its freely accessible method comparison is Anantharaman–Popa, Lemma 11.2.1 and Theorem 11.2.2, printed 185–188 (PDF 191–194); its local exact-containment argument supplies the nesting step directly.
