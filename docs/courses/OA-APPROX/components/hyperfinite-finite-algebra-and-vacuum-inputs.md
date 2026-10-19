# Complete finite-algebra and vacuum inputs for hyperfinite factors

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Original programme exposition: CC0 to the extent of rights held. Human and earlier provider notices retain their own terms.*

The [hyperfinite finite-factor lesson](../src/hyperfinite-finite-factors.md) has nine original results and ten solved problems. Its assertions reach beyond the separable tracial factor: projection rotation permits an arbitrary finite center, local corner permanence has no separability hypothesis, finite-level implementation permits any von Neumann algebra, and a normal representation may have an arbitrarily large Hilbert multiplicity. The inputs below keep those scopes.

The complete bounded calculus, Hilbert completion, polar and support operations are CF1–10. The complete Banach coefficient predual is CP1–6. [PC0–7 and FCT0–7](central-finite-trace-inputs.md#retained-pc-complete-inputs) prove arbitrary orthogonal sums, central comparison, cancellation, finite/properly infinite parts, central tiles and the faithful normal center-valued trace. These are general finite-algebra proofs. The scalar-factor trace arguments alone would not cover all the lesson's claims.

<a id="hf0"></a>

## HF0. The whole tracial commutant and every subalgebra expectation

Let \(M\) have a faithful normal finite trace \(\tau\), normalized by \(\tau(1)=1\), and let \(N\subset M\) be any unital von Neumann subalgebra. Neither algebra nor its representation needs to be separable, and neither needs to be a factor. In this section inner products are linear in the first variable. Write \(\Omega=1\) in \(H=L^2(M,\tau)\); its dense vectors are \(a\Omega\), \(a\in M\), with \(\langle a\Omega,b\Omega\rangle=\tau(b^*a)\). Left and right multiplication by \(x\) are bounded by \(\|x\|\), using the trace ideal estimates.

The trace GNS representation is normal in the complete coefficient sense. Indeed, on dense vectors, its coefficient at \(x\) is \(\tau(b^*xa)\). A square-summable coefficient representation of the known normal functional \(\tau\) makes this normal by bounded multiplication of its two vector lists. Approximating arbitrary GNS vectors in Hilbert norm gives the estimate
\[
\|\ell_{\xi,\eta}-\ell_{\xi',\eta'}\|
\le\|\xi-\xi'\|\|\eta\|+\|\xi'\|\|\eta-\eta'\|.
\]
CP1–6 makes the predual norm closed. Thus every GNS vector coefficient is normal. A square-summable series of these coefficients converges in functional norm and is normal as well. These are all ultraweak tests in the target. Faithfulness follows from \(\tau(x^*x)=0\Rightarrow x=0\). The complete faithful normal range and inverse theorem ST1–2 makes its image a von Neumann algebra with a normal inverse.

We prove its full commutant, including the bounded-vector step. Define the antiunitary \(J(a\Omega)=a^*\Omega\), and denote right multiplication by \(R_b\). Both extend to the whole Hilbert space, and \(R_b\) commutes with every left multiplication.

Suppose \(T\) commutes with all \(R_b\), and put \(C=\|T\|\), \(\xi=T\Omega\). If \(C=0\), \(T=0\); otherwise consider
\[
\mathcal K_C=\{a\Omega:a\in M,\ \|a\|\le C\}.
\]
This convex set is weakly compact in \(H\). The bounded ball of \(M\) is ultraweakly compact by CP and the compact dual-ball proof. Its map to \(H\) is weakly continuous on that ball: the tests \(b\Omega\) are \(\tau(b^*a)\), and approximation of an arbitrary Hilbert test by these dense vectors is uniform because \(\|a\Omega\|\le C\). Its image is therefore weakly compact and weakly closed.

For \(b=v|b|\in M\), put \(r=|b|^{1/2}\). Polar decomposition and the trace give
\[
b\Omega=R_r(vr\Omega),\qquad
\|r\Omega\|^2=\|vr\Omega\|^2=\tau(|b|).
\]
Since \(T\) commutes with \(R_r\),
\[
|\langle\xi,b\Omega\rangle|
=|\langle R_r\xi,vr\Omega\rangle|
\le C\,\tau(|b|).
\]
On the other hand
\[
\sup_{\|a\|\le C}\operatorname{Re}\tau(b^*a)=C\,\tau(|b|).
\]
The upper bound follows by writing \(b=v r^2\), moving one \(r\) with the trace and applying the trace-vector norm bound; the lower bound is attained at \(a=Cv\). Hence no dense test \(b\Omega\) separates \(\xi\) from \(\mathcal K_C\). The support function of this bounded set and the pairing with \(\xi\) are continuous in the Hilbert test, so no Hilbert vector separates them. The complete Hilbert separation proof in CF now gives \(\xi\in\mathcal K_C\). Thus \(\xi=a\Omega\) for some \(\|a\|\le C\), and
\[
T(b\Omega)=R_b\xi=ab\Omega.
\]
Density proves \(T=L_a\) on all of \(H\). Therefore the commutant of the whole right algebra is the left algebra; conjugation by \(J\) gives the converse. This argument also applies to \(N\) with its restricted trace.

Let \(e\) be the orthogonal projection of \(H\) onto \(H_N=\overline{N\Omega}\). The space is reducing for both left and right \(N\). For \(x\in M\), \(eL_xe|_{H_N}\) commutes with right multiplication by \(N\). The commutant result on \(H_N=L^2(N,\tau|_N)\) therefore gives a unique \(E_N(x)\in N\) with
\[
L_{E_N(x)}=eL_xe|_{H_N},\qquad
E_N(x)\Omega=e x\Omega,\qquad
\|E_N(x)\|\le\|x\|.                                    \tag{E1}
\]
Faithfulness gives linearity. Compression gives \(E_N(1)=1\) and \(E_N(x^*)=E_N(x)^*\). It fixes \(N\). Commutation of \(e\) with the left action of \(N\) proves \(E_N(axb)=aE_N(x)b\). Compression on the direct sum of \(m\) copies of \(H_N\) preserves positivity for every \(m\); the faithful matrix representation of \(M_m(N)\) reflects positivity by the bounded continuous calculus. Thus \(E_N\) is completely positive.

Because \(e\Omega=\Omega\), \(\tau(E_N(x))=\tau(x)\). If \(x\ge0\) and \(E_N(x)=0\), faithfulness of \(\tau\) gives \(x=0\); the expectation is faithful. Formula (E1) is the entire trace-GNS orthogonal projection, so it is the nearest \(2\)-norm point in \(N\). In particular it supplies norm-bounded approximants at no larger \(2\)-norm error.

Normality holds on all ultraweak nets. For square-summable lists in \(H_N\), the pullback of a coefficient series of the compressed operator is the corresponding series in \(H\), using \(e\) on its vector legs. The normal trace representation just proved makes it normal on \(M\). The faithful normal trace representation of \(N\) has a normal inverse by ST1–2, so \(E_N:M\to N\) is ultraweakly continuous. No assertion that an arbitrary ultraweakly convergent net is norm bounded is used.

If another trace-preserving \(N\)-bimodule projection has the same range, then for \(b\in N\) its value at \(x\) pairs against \(b\Omega\) as \(\tau(b^*x)\). Those pairings determine \(e x\Omega\), and faithfulness gives equality with \(E_N\). This proves uniqueness at the whole stated scope, including \(N=\mathbb C1\), \(N=M\) and \(N=G'\cap M\) for any unitary subgroup \(G\).

The predual density PB1 in the lesson also follows directly: if the closed span of \(x\mapsto\tau(bx)\) were proper in \(M_*\), Hahn–Banach and CP would give a nonzero \(x\in M\) annihilating it; taking \(b=x^*\) contradicts faithfulness. For a normal positive \(\psi\), choose \(\|\psi-\tau(b\,\cdot)\|<\eta\). On \(\|x\|\le C\),
\[
\psi(x^*x),\ \psi(xx^*)\le\|b\|\|x\|_2^2+\eta C^2.
\]
This is the whole bounded trace topology, for nets. Bounded \(2\)-norm Cauchy sequences remain in \(M\), by compactness of the bounded ultraweak ball and identification of their pairings against all \(y\Omega\). This proof requires no unbounded density identification.

The optional \(L^1\) notation in equation (1) has a complete intrinsic meaning. For \(d\in M\), polar decomposition \(d=v|d|\) and positive-form Cauchy–Schwarz give
\[
\|\tau(d\,\cdot)\|=\sup_{\|x\|\le1}|\tau(dx)|=\tau(|d|).
\]
For the upper bound move \(|d|^{1/2}\) to both sides with the trace and bound the middle operator by one; for equality take \(x=v^*\), using the support of \(|d|\). Thus \(d\mapsto\tau(d\,\cdot)\) is an isometry for the norm \(\|d\|_1=\tau(|d|)\), and the norm triangle inequality follows from the functional norm. Complete \(M\) in this norm. Its isometric image in \(M_*\) is closed and contains the dense PB1 subspace, hence is all of \(M_*\). This constructs the entire tracial \(L^1\) and its functional pairing; no assertion that its elements are bounded operators is made.

If a normal positive functional is already written as \(\tau(h\,\cdot)\), its density denotes the corresponding \(L^1\) element. For any bounded positive approximation \(b\) and \(\|x\|\le C\), the just proved isometry gives
\[
\tau(hx^*x)\le\tau(bx^*x)
+|\tau((h-b)x^*x)|
\le\|b\|\|x\|_2^2+C^2\|h-b\|_1.
\]
This proves the whole conditional density estimate (1). Existence of an affiliated-operator realization of \(h\) is not a premise of the estimate or the topology proof.

<a id="hf1"></a>

## HF1. Whole spectral cutoffs and all normal-state error bounds

The [interval support construction in Bogoliubov Section 6.3](../src/bogoliubov-automorphisms-and-innerness.md#6-3-interval-projections-from-continuous-positive-parts) starts with continuous positive parts and the strong limit \(B(B+\epsilon)^{-1}\). It proves the support projection of every bounded positive \(B\), its commutation properties and the order on each complementary interval. Thus a spectral cutoff here is an actual reducing projection in the von Neumann algebra; no unproved spectral probability representation is needed.

For a threshold \(a\), the projection onto \(\ker(h-a)_+\) includes the lower interval through \(a\). To include \(a\) in the upper interval instead, take the complement of the support of \((a-h)_+\), namely the projection onto its kernel. Equivalently its upper range has \(h\ge a\), and its complementary range has \(h\le a\). On a possible \(a\)-eigenspace the upper cutoff equals one. The order estimates used below are valid at that endpoint too.

Let \(0\le h\le1\), let \(\varphi\) be any normal state, and assume
\[
\|h-h^2\|_\varphi
=\varphi((h-h^2)^2)^{1/2}\le\delta.
\]
The positive-functional Cauchy–Schwarz inequality gives \(\varphi(h-h^2)\le\delta\). Put \(q=1_{[1/2,1]}(h)\), with the just constructed cutoff. The scalar inequalities on its two reducing intervals give the operator inequalities
\[
(h-q)^2\le4h^2(1-h)^2,\qquad
(h^{1/2}-q)^2\le2h(1-h).
\]
For the first, use \(s\le2s(1-s)\) when \(s<1/2\) and \(1-s\le2s(1-s)\) when \(s\ge1/2\). For the second, the lower branch is \(s\le2s(1-s)\), and the upper branch follows from \((1-\sqrt s)^2\le1-s\le2s(1-s)\). Bounded continuous calculus on each reducing space transfers these inequalities, including the cutoff endpoint. Applying \(\varphi\) proves
\[
\|h-q\|_\varphi\le2\delta,\qquad
\|h^{1/2}-q\|_\varphi\le\sqrt{2\delta}.                 \tag{C1}
\]

For \(0<\delta<1/4\), set \(\epsilon=\sqrt\delta\) and \(q'=1_{[1-\epsilon,1]}(h)\). On \(1-q'\), \((1-h)^2\ge\delta(1-q')\), while on \(q'\), \((1-h)^2\le\delta q'\). These commuting order inequalities imply
\[
\varphi(h^2(1-q'))\le
\delta^{-1}\varphi(h^2(1-h)^2)\le\delta.
\]
Also \(h(1-q')=h^2(1-q')+h(1-h)(1-q')\), so positivity and \(\varphi(h(1-h))\le\delta\) give \(\varphi(h(1-q'))\le2\delta\). The squared root error on \(1-q'\) is \(h(1-q')\); on \(q'\) it is at most \((1-h)^2q'\le\delta q'\). The two exact sums therefore give
\[
\|h-q'\|_\varphi\le\sqrt{2\delta},\qquad
\|h^{1/2}-q'\|_\varphi\le\sqrt{3\delta}.                \tag{C2}
\]
They imply the original weaker bounds \(2\sqrt\delta\) and \(\sqrt3\,\delta^{1/4}\), since \(0<\delta<1\). Thus both (6) and (6a) retain their full state and parameter scope. For \(\delta=0\), the \(L^2(\varphi)\) statements in (C1) remain valid without faithfulness; no inference that \(h\) itself is a projection is made from a nonfaithful state.

The rotation proof of Lemma 1.1 uses the same support machinery for \(k=\ker(1-(e-f)^2)\). Its polar part is unitary on \(1-k\), even when the nonzero spectrum accumulates at zero. On \(k\), the two orthogonal exceptional supports are \(e\wedge(1-f)\) and \((1-e)\wedge f\). The complete finite center-valued comparison gives a partial isometry between them, because the initial equivalence of \(e,f\) and the equivalence on \(1-k\) give equal central trace values. The skewadjoint exchange \(v-v^*\) has squared distance \(2k\) from \(k\). Together with the continuous scalar inequality \(1-\sqrt{1-s}\le s\), this gives the full operator bound, not just a scalar trace estimate.

<a id="hf2"></a>

## HF2. Arbitrary finite centers and finite-level implementation in any algebra

FCT0–7 constructs the normalized faithful normal center-valued trace on every finite von Neumann algebra. Its normal uniqueness and projection comparison apply with arbitrary center. Every normal center state gives a normal scalar trace; these states separate the center by vector tests. Thus in the lesson's increasing directed family of unital subfactors all those scalar traces agree on the directed union and, by bounded density and normality, everywhere. Their restrictions to the center must agree. States supported on a nontrivial central projection and its complement would disagree, so the generated finite algebra is a factor. This is the complete nonseparable argument of Lemma 6.1, with no presupposed globally faithful scalar state.

Every type \(\mathrm{II}_1\) algebra, including a nonfactor, contains commuting unital \(M_2\) legs. PC5 supplies type-II halving. The explicit matrix-coordinate map identifies each relative commutant with a type-II corner, where halving can continue. The generated algebra is finite, is a factor by the preceding directed argument and has a normalized faithful normal scalar trace from FCT. Its countable finite matrix union has the unique normalized traces and a separable trace GNS completion. The whole trace-preserving orbit isomorphism identifies its generated normal algebra with the product \(R\); faithful normal range and inverse are supplied by ST1–2. This proves the full nonseparable ambient assertion. For the maximality assertion, the ambient separable predual passes to normal subalgebras by the CP quotient predual. A chain upper bound is a finite factor by the same directed proof, and the two finite-set approximation errors give local AFD. The complete [AF5 uniqueness construction](central-afd-uniqueness-inputs.md#af5-full-finite-afd-uniqueness) identifies that upper bound with \(R\). Choice then supplies a maximal member, with exactly the stated separable ambient hypothesis.

The finite-level implementation lemma allows an arbitrary von Neumann algebra \(P\), even a nonfactor with properly infinite central parts. PC5 gives its finite/properly infinite central split; a star automorphism preserves that split because all its projection definitions and arbitrary least upper bounds are preserved.

On the finite part, if \(e_{11},\ldots,e_{dd}\) are the diagonals of a unital \(M_d\), they are equivalent and sum to the central unit. Their central trace values are all \(1/d\). The images under the automorphism are also \(d\) equivalent diagonals summing to that unit, so they have the same trace values. Projection comparison gives \(e_{11}\sim\alpha(e_{11})\). This calculation does not require an extra naturality assertion about a trace transported by the automorphism.

On the properly infinite part, \(e_{11}\) has full central support. PC4 identifies every central corner projection as a compression of an ambient central projection. If any such nonzero central cut were finite, its \(d\) equivalent diagonal cuts would have finite sum by PC6, contrary to proper infiniteness of the ambient central part. Hence \(e_{11}\) is properly infinite. Iterated halving puts \(d\) orthogonal equivalent copies of it under itself. Matching the original \(d\) diagonals to these copies and taking the full orthogonal sum gives \(1\precsim e_{11}\). The reverse inclusion and PC3 give \(e_{11}\sim1\). The identical argument applies to \(\alpha(e_{11})\). Adding the finite and properly infinite central implementations gives \(w^*w=e_{11}\), \(ww^*=\alpha(e_{11})\).

The finite sum
\[
u=\sum_{i=1}^d\alpha(e_{i1})w e_{1i}
\]
then satisfies \(u^*u=uu^*=1\) and \(ue_{ij}u^*=\alpha(e_{ij})\). This proves the original any-algebra result, including \(d=1\). It uses only the projection properties of the automorphism. For the subsequent point-predual assertion on the finite factor, preservation of the trace gives the full normal GNS implementation and inverse by HF0; all normal-functional estimates apply on the entire predual.

<a id="hf3"></a>

## HF3. All finite corners and arbitrary normal-representation commutants

The entire dyadic replacement, exact containment and uniqueness route is [AF1–5](central-afd-uniqueness-inputs.md#af1-finite-matrices-and-trace-projections). HF0 supplies its finite-dimensional trace expectations; HF1 supplies the spectral rounding. The lesson keeps its actual constants: matrix-unit error \(2^{-p/2}\), \(a(\delta)=7\delta+\sqrt{7\delta}\), first-corner rotation \(\sqrt2\,a(\delta)\), and reconstruction factor \(d^2\). There is no assertion that the whole aligning unitary is close to one.

Finite amplification is a finite entry calculation,
\[
\|[a_{ij}]\|_{2,M\otimes M_n}^2
=n^{-1}\sum_{i,j}\|a_{ij}\|_{2,M}^2.
\]
For any nonzero corner \(eMe\), the dyadic subprojection \(e_1\le e\), retained exactly by the new finite matrix algebra, gives the ambient error \(2\|e-e_1\|_2\) plus the independently chosen matrix error. The normalized corner norm is \(\tau(e)^{-1/2}\) times that ambient norm. These local statements require no separability. For the converse, if \(Q=e(M\bar\otimes M_n)e\) is locally AFD, choose \(r\) with \(1/(nr)\le\tau(e)\). Central-factor comparison embeds an equivalent copy of \(M\) as a corner of \(Q\bar\otimes M_r\). Local amplification and corner permanence therefore give local AFD of \(M\). Only the later identification with \(R\) uses the original separability hypothesis.

For the separate representation assertion, the entire [normal amplification proof NA0–6](normal-representations-and-finite-trace-corners.md#na0) has been retained with its full Hilbert multiplicity. NA3 constructs every normal positive coefficient from the CP predual series, a dominated bounded form and its bounded positive root. NA4 takes a maximal orthogonal family of cyclic spaces and the whole orthogonal sum of their isometries. Thus
\[
\rho(R)'\cong p(R^{\mathrm{op}}\bar\otimes B(K))p
\]
with arbitrary \(K\) and nonzero \(p\). HF0 supplies the full tracial commutant needed in NA5. NA0 gives every matrix entry and the full spatial commutant.

NA1's diagonal trace is the supremum of finite positive diagonal sums. Its column-square identity proves the trace law, all-net normality, faithfulness and semifinite cuts. NA2 proves that a projection is finite exactly when this trace is finite: if it had infinite trace, successive factor comparisons produce countably many trace-one equivalent projections below it, and their shift is an isometry onto a proper subprojection. This countable contradiction does not restrict the cardinality of \(K\). A finite trace \(t\) puts \(p\) below a rank-\(n\) matrix projection for an integer \(n>t\).

Compatible finite-level transposition identifies the whole opposite algebra with \(R\) on its trace GNS space, with a normal inverse. Apply the already proved corner theorem to that finite amplified corner. The order is essential: the corner theorem precedes the commutant application, so NA6 introduces no proof cycle.

If \(\rho(1)\) is instead a proper identity projection \(e\), compress to \(eL\). The full uncompressed commutant is
\[
B((1-e)L)\oplus(\rho(R)|_{eL})'.
\]
Finiteness makes the zero-action space finite dimensional. A nonzero such summand therefore gives \(M_d\oplus R\), whereas the active corner commutant is \(R\). The whole normal inverse and this precise convention are part of the lesson.

<a id="hf4"></a>

## HF4. The vacuum/tracial direct sum in the whole solved problem

Let \(K\) be separable infinite dimensional with basis \(f_j\). Define \(\mathcal F(K)\) as the Hilbert completion with orthonormal basis \(e_S\), where \(S\) runs over all finite subsets of positive integers; \(e_\varnothing\) is the vacuum. This is the complete antisymmetric Fock space, with \(e_S\) identified with the increasing wedge of its occupied basis modes. Define the annihilator \(a_j\) to be zero when \(j\notin S\), and otherwise to remove \(j\) with sign \((-1)^{|\{i\in S:i<j\}|}\). The adjoint inserts the unoccupied mode with the same sign.

These formulas define norm-one operators on the whole completion. For distinct modes, the removal/insertion positions differ by one when both operations are possible, so the two orders give opposite signs; when either operation is impossible both relevant terms vanish. For one mode, removal followed by insertion and insertion followed by removal are the complementary occupation projections. Thus
\[
a_i a_j+a_j a_i=0,\qquad
a_i a_j^*+a_j^*a_i=\delta_{ij}1.
\]
For a finite coefficient vector, the conjugate-linear combination \(a(f)=\sum_j\overline{f_j}a_j\) obeys \(a(f)^2=0\) and \(a(f)a(f)^*+a(f)^*a(f)=\|f\|^2 1\). As in CO3, \(a(f)^*a(f)/\|f\|^2\) is a nonzero projection when \(f\ne0\), so \(\|a(f)\|=\|f\|\). Nonzeroness also follows by applying the annihilator to its one-particle vector. Norm completion extends it to every \(f\in K\). The finite-mode algebra is the full \(M_{2^n}\) on the occupation choices of its first \(n\) modes; the same universal finite-mode maps as [CO3](continuous-outer-action-regular-and-car-inputs.md#co3-complete-tracial-car-action) identify this with the represented CAR.

To prove irreducibility explicitly, let \(T\) commute with every field and its adjoint. Each \(a_jT e_\varnothing=T a_j e_\varnothing=0\). The common kernel of the annihilators is exactly the vacuum line: the coefficient of \(e_{S\setminus\{j\}}\) in \(a_j\xi\) is, up to sign, the coefficient of \(e_S\) in \(\xi\); each nonempty \(S\) contains a \(j\). Therefore \(T e_\varnothing=c e_\varnothing\). Applying all finite products of creation operators gives \(T e_S=c e_S\) for every finite \(S\). Their dense span gives \(T=c1\). The full bicommutant theorem BD1–3 then proves that the vacuum closure is \(B(\mathcal F(K))\).

Put \(n_j=a_j^*a_j\) and \(q_n=n^{-1}\sum_{j\le n}n_j\). On the vacuum basis,
\[
q_n e_S=\frac{|S\cap\{1,\ldots,n\}|}{n}\,e_S.
\]
This tends to zero for every finite \(S\). Since \(0\le q_n\le1\), finite-vector approximation gives strong convergence to zero on the whole Fock space, without an occupation bound on an arbitrary vector.

In the tracial CAR representation of CO3, the occupations have trace \(1/2\), and distinct legs have product traces \(1/4\). Consequently
\[
\|(q_n-\tfrac12)\Omega\|_2^2=\frac1{4n}.
\]
If \(x\) is supported in the first \(m\) modes, each \(n_j\) with \(j>m\) commutes with \(x\), by the two CAR sign cancellations. The finitely many other terms give
\[
\|[q_n,x]\|\le\frac{2m\|x\|}{n}.
\]
Thus \((q_n-\tfrac12)x\Omega\to0\). All local vectors are dense in the trace GNS space, and the operators are uniformly bounded, so \(q_n\to\tfrac12\,1\) strongly on the whole trace space.

For the direct sum representation, the strong limit is \(0\oplus\tfrac12\,1\). Twice that limit is the nontrivial central projection \(z=0\oplus1\) in the generated von Neumann algebra. Multiplication by \(z\) and \(1-z\) separates the two component closures; bounded strong density on each component gives exactly
\[
B(\mathcal F(K))\oplus R.
\]
Every finite-mode represented algebra is still a unital full matrix factor, since its two faithful finite matrix representations are linked by the same generators. Their increasing closure nevertheless has the nontrivial center just exhibited.

Finally \(\mathcal F(K)\) has countably infinitely many basis vectors. Enumerating them defines a unilateral shift isometry whose range omits the first basis vector, proving that \(B(\mathcal F(K))\) is not finite. The direct sum is therefore not finite. This proves every assertion in Exercise 7 and shows precisely why finiteness is required in Lemma 6.1.

<a id="hf5"></a>

## HF5. Exact scope of the original results and solved problems

| Whole assertion or problem | Complete mathematical inputs |
| --- | --- |
| Lemma 1.1; state estimates (5), (6), (6a); Problems 1–2 | PC/FCT with arbitrary center; HF1 for every cutoff, endpoint and normal-state bound; the full planar matrices and normalized trace calculations. |
| Lemmas 3.1 and 4.1; Problems 3–4 | HF0, HF1 and AF1–4: all finite-dimensional blocks, dyadic remainders, arbitrarily large size, exact old-head containment and every original error constant. |
| Theorem 5.1, Corollary 5.2; Problems 5–6 and 8 | AF5 and HF3: full normal trace-GNS identification, every amplified corner and the converse, arbitrary local approximation without separability and precise normalized corner norms. |
| The unnumbered normal finite-commutant application | HF0, NA0–6 and HF3: arbitrary Hilbert multiplicity, finite trace criterion, opposite algebra, full normal inverse and the proper-identity variant. |
| Lemma 2.1 and its commutant bound | HF0 and the whole compact convex orbit minimization of FH2, for every subgroup and without separability. |
| Lemma 6.1; the copies and maximality assertions; Problem 10 | HF2, PC/FCT and AF5: all finite centers and directed families, all ambient type-II algebras, exact stated maximality hypothesis, every trace cut and \(M_7\). |
| Lemma 6.2 | HF2: any algebra, including finite/properly infinite central parts, full finite matrix implementation and no factor or separability restriction. |
| Theorem 6.3 and Problem 9 | The full trace-predual density HF0, finite implementations, all inverse estimates and the distant-leg outer contradiction. |
| Problem 7 | HF4: entire vacuum and trace representations, complete irreducibility, both strong limits, central separation and the nonfinite summand. |

The three human comparisons retain their separate scopes. [Anantharaman–Popa's free author draft](https://idpoisson.fr/anantharaman/publications/IIun.pdf), printed pp.185–188, uses amenability for its containment induction; the local proof establishes corner permanence directly from finite-set AFD. [Connes's free Numdam article](https://numdam.org/item/ASENS_1975_4_8_3_383_0.pdf), printed pp.388–389, supplies the projection-repair and cutoff comparison; HF1 proves all displayed state estimates directly. [Peterson's free university-hosted notes](https://math.vanderbilt.edu/peters10/teaching/spring2020/OperatorAlgebras.pdf), April 27, 2020, Section 6.4, pp.102–107, gives the general center-trace and tracial-commutant comparisons. The complete local PC/FCT and HF0 routes supply all consumed arguments. Free access grants no additional expression-reuse licence; no human proof text is relabelled CC0.
