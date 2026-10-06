# Finite measured groupoids and AFD algebras

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text: public domain (CC0).*

Finite equivalence classes give matrix algebras with a measurable center. They need not give finite-dimensional algebras. To obtain finite-dimensional approximation, one must also discretize that center. We carry out both steps and prove that an ergodic principal measured AF groupoid of type \(\mathrm{II}_1\) has an AFD factor of type \(\mathrm{II}_1\).

We use standard Borel spaces, countable separating families, measure completion, monotone convergence and Hilbert-space operator theory. The injective-image input is the exact Lusin–Souslin Theorem 3.6 and Polish topology refinement F4 from *Polish spaces and standard Borel spaces*, already used in the [fullness lesson](central-sequences-and-free-group-factors.md). We explain its needed Borel-map version below. The finite-trace local AFD criterion and separable uniqueness theorem are proved in [Hyperfinite finite factors](hyperfinite-finite-factors.md). General modular weights or expectations are not needed for the kernel construction.

The freely readable equivalence-relation construction is Anantharaman–Popa, §1.5. We use the type \(\mathrm{II}_1\) hypothesis to choose an equivalent invariant probability measure; we do not infer invariance from quasi-invariance alone. The AF exhaustion and its fixed finite class sizes are given hypotheses.

## 1. The measured equivalence relation

Principality identifies the groupoid with a Borel equivalence relation \(\mathcal R\subset X\times X\), with countable classes, on a standard Borel space \(X\). The arrow \((x,y)\) runs from \(y\) to \(x\); multiplication is
\[
(x,y)(y,z)=(x,z).
\tag{1}
\]
Its source counting measure relative to a probability measure \(\mu\) is
\[
\nu(E)=\int_X\#\{x:(x,y)\in E\}\,d\mu(y).
\tag{2}
\]
The measured-relation setup includes measurability of source counting functions for Borel arrow sets and of countable-relation saturations. These are countable-section inputs; the finite-class labels below do not by themselves prove them for an arbitrary countable relation. Complete proofs of these Borel inputs are not established in these lessons.

Invariance means that \(\nu\) is unchanged by the flip \((x,y)\mapsto(y,x)\). Equivalently, every Borel partial bijection whose graph lies in \(\mathcal R\) preserves the restricted measure. The forward implication follows by comparing its graph and inverse graph over any Borel subset of its domain. The converse follows by decomposing the relation into countably many such graphs; our finite-class labels below provide that decomposition in the AF case.

The source AF hypothesis supplies increasing Borel subrelations
\[
\mathcal R_1\subset\mathcal R_2\subset\cdots,\qquad
\nu\left(\mathcal R\setminus\bigcup_n\mathcal R_n\right)=0,
\tag{3}
\]
where each \(\mathcal R_n\) has a fixed finite class size \(k_n\) almost everywhere. This is the source's type \(\mathrm I_{k_n}\) condition. Statements and functions are taken modulo null sets.

There is no difficulty in discarding common exceptional classes. If \(N\subset X\) is null, invariance gives
\[
\nu\{(x,y):x\in N\}
=\nu\{(x,y):y\in N\}=0.
\]
The first set has a nonempty source fiber exactly on the saturation of \(N\), so that saturation is null as well. Thus countably many null exceptions can be removed without retaining arrows into them.

We can also make the AF model exact on a conull invariant set. Put \(\mathcal R_\infty=\bigcup_n\mathcal R_n\) and let \(N_0\) be the measurable set of sources with at least one arrow in \(\mathcal R\setminus\mathcal R_\infty\). Equation (3) makes \(N_0\) null. It is saturated: if \(y\in N_0\) and \(z\sim y\) had no missing arrows, every point of their common orbit would be \(\mathcal R_\infty\)-equivalent to \(z\); transitivity would contradict the missing arrow at \(y\). Remove \(N_0\) and the null saturations of the countably many finite-stage class-size exceptions. On the resulting conull invariant model, \(\mathcal R=\mathcal R_\infty\) literally and every stage has its stated finite class size. Its labeled stage graphs then describe every arrow.

If the initially given measure is merely equivalent to an invariant probability \(\mu\), the associated regular algebras are normally isomorphic. Indeed if \(d\mu'/d\mu=h>0\), the source counting measures satisfy \(d\nu'/d\nu(x,y)=h(y)\), and
\[
V:L^2(\mathcal R,\nu)\longrightarrow L^2(\mathcal R,\nu'),
\qquad (V\xi)(x,y)=h(y)^{-1/2}\xi(x,y)
\tag{4}
\]
is unitary. Left convolution does not change the source coordinate \(y\), so it intertwines under \(V\). We may therefore work with the invariant probability furnished by the type \(\mathrm{II}_1\) assumption.

## 2. Borel labels for finite classes

We need actual measurable matrix coordinates, not just a choice of labels on each finite class.

First recall the Borel-map form of the injective-image theorem. If \(f:Y\to Z\) is an injective Borel map between standard Borel spaces, refine compatible Polish topologies on \(Y\) so that the inverse images of a countable base on \(Z\) become open and closed. F4 permits each refinement and their countable join, without changing the Borel sets. Then \(f\) is continuous. Lusin–Souslin makes its image, and the image of every Borel subset, Borel. Thus \(f\) is a Borel isomorphism onto its image. This uses the declared topology-refinement input; injectivity alone does not make arbitrary projections preserve Borel sets.

**Lemma 2.1.** A Borel equivalence relation with all classes of size \(k<\infty\) has a Borel partition
\[
X=A_1\sqcup\cdots\sqcup A_k
\]
such that each \(A_i\) meets every class once. With \(Y=A_1\), there are Borel isomorphisms \(\phi_i:Y\to A_i\), with \(\phi_1=\operatorname{id}_Y\), which list each class.

**Proof.** A countable separating family embeds \(X\) injectively and Borel measurably into the Cantor space by its membership bits. The preceding injective-image fact supplies a Borel order on \(X\), obtained from the lexicographic order of those bit sequences. Every finite class has a unique increasing listing.

Let \(T\subset X^k\) consist of the increasing \(k\)-tuples all of whose entries are equivalent. It is Borel. Each coordinate projection \(p_i:T\to X\) is injective: an entry determines its entire finite class, and hence its unique increasing tuple. The images \(A_i=p_i(T)\) are Borel and partition \(X\). The maps
\(\phi_i=p_i(p_1|_T)^{-1}\)
are Borel bijections and list the class as claimed. \(\square\)

For an invariant measure, the maps \(\phi_i\) preserve its restriction on \(Y\), so
\[
\mu(A_i)=\mu(Y)=1/k,\qquad
\beta=k\,\mu|_Y
\tag{5}
\]
is a probability measure. More precisely \(\mu(\phi_i(E))=\mu(E)\) for every Borel \(E\subset Y\).

Apply this lemma to every \(\mathcal R_n\). Its finitely many pair-coordinate graphs, as \(n\) varies, cover \(\mathcal R\) modulo the null set in (3). In particular all counting functions, kernel sums and null-set saturations used here can be evaluated through countably many Borel graphs.

## 3. The regular algebra and its trace

Put \(H=L^2(\mathcal R,\nu)\). Let \(\mathcal C_n\) be the bounded measurable kernels supported on \(\mathcal R_n\), extended by zero outside it. The union \(\mathcal C=\bigcup_n\mathcal C_n\) is a unital convolution *-algebra:
\[
(f*g)(x,y)=\sum_{z\sim x}f(x,z)g(z,y),\qquad
f^*(x,y)=\overline{f(y,x)}.
\tag{6}
\]
For \(f,g\) from two stages, all nonzero terms lie in the larger subrelation, whose finite class size bounds the sums. The diagonal kernel \(1_\Delta\) is the convolution identity.

Define left and right convolution by
\[
(L_f\xi)(x,y)=\sum_z f(x,z)\xi(z,y),\qquad
(Q_f\xi)(x,y)=\sum_z \xi(x,z)f(z,y).
\tag{7}
\]
These are bounded operators. For left convolution, if both absolute row and column sums of \(f\) are bounded by \(C\), weighted Cauchy–Schwarz gives on each orbit
\[
\sum_x\left|\sum_z f(x,z)\eta(z)\right|^2
\le C\sum_{x,z}|f(x,z)|\,|\eta(z)|^2
\le C^2\sum_z|\eta(z)|^2.
\tag{8}
\]
Integrating over the source coordinate proves \(\|L_f\|\le C\). For \(f\in\mathcal C_n\) we may take \(C=k_n\|f\|_\infty\). Flip invariance makes
\[
(J\xi)(x,y)=\overline{\xi(y,x)}
\]
antiunitary, and \(Q_f=J L_{f^*}J\), proving the right bound as well. Finite-sum multiplication gives
\[
L_f^*=L_{f^*},\qquad Q_f^*=Q_{f^*},\qquad
L_f Q_g=Q_g L_f.
\tag{9}
\]
Define the regular von Neumann algebra
\[
M=\{L_f:f\in\mathcal C\}''.
\tag{10}
\]

This is the associated groupoid algebra in the usual bounded-Schur-kernel definition, not a smaller algebra caused by (3). In fact let \(f\) have bounded absolute row and column sums. Then \(|f|\le C\) and \(f\in L^2(\nu)\), since
\(\int\sum_x|f(x,y)|^2\,d\mu(y)\le C^2\).
The same bound (8) defines its left operator. It commutes with each \(Q_g\), \(g\in\mathcal C\): first check on kernel vectors \(\xi\in\mathcal C\). Both composite sums are finite because \(g\) and \(\xi\) lie in finite-class stages. Interchanging their intermediate indices gives equality, which extends by density and boundedness.
Its cutoffs \(f_n=f1_{\mathcal R_n}\) belong to \(\mathcal C_n\), converge to \(f\) in \(L^2(\nu)\), and have the same uniform operator bound. The commuting right algebra used below has a dense orbit on the diagonal vector. Convergence on that vector therefore extends to strong convergence on all of \(H\), giving \(L_f\in M\). The reverse inclusion is immediate because every finite-stage kernel is a Schur kernel. This also matches the source's left regular convolution construction.

**Lemma 3.1.** The diagonal vector \(\Omega=1_\Delta\) is cyclic and separating for \(M\), and
\[
\tau(x)=\langle\Omega,x\Omega\rangle
\tag{11}
\]
is a faithful normal tracial state. For \(f\in\mathcal C\),
\[
\tau(L_f)=\int_X f(x,x)\,d\mu(x),\qquad
\|L_f\|_{2,\tau}^2=\int_{\mathcal R}|f|^2\,d\nu.
\tag{12}
\]

**Proof.** We have \(L_f\Omega=Q_f\Omega=f\). The bounded functions on \(\mathcal R_n\) are dense in \(L^2(\mathcal R_n,\nu)\), and (3) makes their union dense in \(H\). Here \(\nu(\mathcal R_n)=k_n<\infty\). Thus both convolution algebras have a dense orbit on \(\Omega\). The right algebra commutes with \(M\), so \(x\Omega=0\), \(x\in M\), forces \(xQ_f\Omega=0\) on a dense set and hence \(x=0\). This proves separation and faithfulness; \(\|\Omega\|=1\) and vector functionals are normal.

The first identity in (12) follows from \(L_f\Omega=f\). Invariance under the flip gives
\[
\int_X\sum_z f(x,z)g(z,x)\,d\mu(x)
=\int_X\sum_z g(x,z)f(z,x)\,d\mu(x).
\]
These are \(\tau(L_fL_g)\) and \(\tau(L_gL_f)\). Thus \(\tau\) is tracial on the unital generating *-algebra. Bounded strong* Kaplansky approximation extends this identity first in one variable and then in the other to \(M\). Finally \(\|L_f\|_{2,\tau}=\|L_f\Omega\|=\|f\|_{L^2(\nu)}\). \(\square\)

The dense right orbit just proved also justifies the strong-cutoff assertion preceding the lemma: for \(g\in\mathcal C\),
\[
\|(L_{f_n}-L_f)Q_g\Omega\|
\le\|Q_g\|\,\|f_n-f\|_{L^2(\nu)}.
\]
Uniform boundedness and density complete that assertion.

Bounded 2-norm convergence here implies sigma-strong* convergence, also when \(M\) is not a factor. Suppose \(z_a\in M\), \(\|z_a\|\le C\), and \(\|z_a\|_{2,\tau}\to0\). Commutation with the right algebra gives
\[
\|z_aQ_g\Omega\|\le\|Q_g\|\,\|z_a\Omega\|
=\|Q_g\|\,\|z_a\|_{2,\tau}\longrightarrow0.
\]
The right orbit is dense, so the common bound extends convergence to every vector. Traciality gives \(\|z_a^*\|_{2,\tau}=\|z_a\|_{2,\tau}\), and the same argument applies to the adjoints. Thus \(z_a\to0\) strongly*. Both \(z_a^*z_a\) and \(z_az_a^*\) are bounded and weakly null. Finite-rank approximation of a trace-class functional, with their common bound controlling its trace-norm tail, makes both products ultraweakly null. The concrete predual of \(M\) is a quotient of the trace-class predual of \(B(H)\), so every normal positive functional on \(M\) tends to zero on these products. These are precisely the sigma-strong* tests. The concrete-predual foundation remains explicit; this argument makes no factoriality assumption.

## 4. Finite stages are matrix fields

Fix a stage, and write \(k=k_n\), \(Y=A_1\) and \(\phi_i\) for its labels. Set \(v_{ij}=L_{1_{\operatorname{Gr}(\phi_i\phi_j^{-1})}}\). Direct convolution gives
\[
v_{ij}v_{\ell m}=\delta_{j\ell}v_{im},\qquad
v_{ij}^*=v_{ji},\qquad
\sum_i v_{ii}=1.
\tag{13}
\]
For \(d\in L^\infty(X,\mu)\), its diagonal kernel gives the multiplication operator \(D_d\xi(x,y)=d(x)\xi(x,y)\). This diagonal representation is normal and faithful.

Every kernel in \(\mathcal C_n\) is determined by
\[
F_{ij}(t)=f(\phi_i(t),\phi_j(t)),\qquad t\in Y.
\tag{14}
\]
Convolution is matrix multiplication of these fields, and involution is matrix adjoint. Its operator is
\(\sum_{i,j}v_{i1}D_{F_{ij}1_Y}v_{1j}\).
Consequently the stage algebra is
\[
M_n=\{L_f:f\in\mathcal C_n\}
\cong M_k\bigl(L^\infty(Y,\beta)\bigr).
\tag{15}
\]
This image is already a von Neumann algebra. To verify closedness, an operator \(T\) belongs to it exactly when all \(v_{1i}Tv_{j1}\) lie in the weakly closed diagonal corner \(D_{L^\infty(Y)}\). The reverse implication follows by reconstructing \(T\) with the finite matrix-unit sum (13). Each corner condition is ultraweakly closed. The entry maps and their inverse corner extraction are normal; faithfulness also follows from \(L_f\Omega=f\).

The trace is
\[
\tau(F)=\frac1k\int_Y\operatorname{Tr}_k(F(t))\,d\beta(t),\qquad
\|F\|_{2,\tau}^2=\frac1k\int_Y\sum_{i,j}|F_{ij}(t)|^2\,d\beta(t).
\tag{16}
\]
Indeed each \(\phi_i\) preserves \(\mu|_Y\), and (5) gives the normalization. The algebras \(M_n\) are increasing and generate \(M\).

**Lemma 4.1.** For a finite set of elements of \(M_n\) and \(\varepsilon>0\), one unital finite-dimensional subalgebra of \(M_n\) approximates every element within \(\varepsilon\) in \(\|\cdot\|_{2,\tau}\).

**Proof.** The finite collection of bounded entries in (14) can be approximated simultaneously by one finite measurable partition \(\mathcal P\) of \(Y\): discretize their real and imaginary ranges and take the common refinement. Average each matrix field over each positive-measure cell of \(\mathcal P\), entry by entry. The resulting field \(E_{\mathcal P}F\) lies in
\[
B_{\mathcal P}
=M_k\otimes\operatorname{span}\{1_C:C\in\mathcal P\},
\tag{17}
\]
a unital finite-dimensional algebra.

If each real and imaginary entry varies by at most \(\delta\) on a cell, its difference from its cell average has magnitude at most \(\sqrt2\delta\). Formula (16) gives
\[
\|F-E_{\mathcal P}F\|_{2,\tau}^2\le2k\delta^2.
\tag{18}
\]
Choose \(\delta\) for the prescribed \(\varepsilon\). Zero-measure cells are irrelevant. Matrix averaging is also contractive in operator norm, because the norm of an average is at most the average of the norms. No abstract conditional expectation theorem is needed for this finite-partition operation. \(\square\)

**Theorem 4.2.** The regular algebra \(M\) is finite and AFD. This conclusion does not require ergodicity.

**Proof.** Finiteness is supplied by the faithful normal trace. The increasing union of \(M_n\) is a unital \*-algebra generating \(M\), so Kaplansky density approximates any finite family \(x_1,\ldots,x_r\in M\) strongly\*, by elements \(y_j\) in one common stage with \(\|y_j\|\le\|x_j\|\). In particular \(\|x_j-y_j\|_{2,\tau}\) can be made arbitrarily small. Lemma 4.1 then approximates the \(y_j\) by \(b_j=E_{\mathcal P}y_j\) in one finite-dimensional algebra, with \(\|b_j\|\le\|y_j\|\). The triangle inequality makes every \(\|x_j-b_j\|_{2,\tau}\) arbitrarily small while \(\|x_j-b_j\|\le2\|x_j\|\). The bounded 2-norm argument in Section 3 therefore gives approximation in every prescribed sigma-strong* neighborhood. This proves AFD for the finite algebra, including its nonfactor cases. \(\square\)

## 5. Ergodicity and type

**Lemma 5.1.** The center of \(M\) consists exactly of the diagonal functions invariant under \(\mathcal R\).

**Proof.** Let \(z\in Z(M)\) and put \(\eta=z\Omega\). For each bounded diagonal function \(d\), its left and right multiplications agree on \(\Omega\). Centrality of \(z\) and commutation with the right algebra give
\[
D_d\eta=Q_d\eta,\qquad
(d(x)-d(y))\eta(x,y)=0.
\tag{19}
\]
A countable separating family on \(X\) forces \(\eta\) to vanish off the diagonal. Write \(\eta=h1_\Delta\), \(h\in L^2(X,\mu)\). For every measurable \(E\subset X\),
\[
\int_E|h|^2\,d\mu
=\|zD_{1_E}\Omega\|^2\le\|z\|^2\mu(E).
\]
Hence \(h\in L^\infty(X,\mu)\), with \(\|h\|_\infty\le\|z\|\). The separating vector gives \(z=D_h\).

Commutation with every matrix unit \(v_{ij}\) at every stage says
\(h(\phi_i(t))=h(\phi_j(t))\) almost everywhere. By (3) this is precisely \(h(x)=h(y)\) for \(\nu\)-almost every arrow. Conversely that equality makes \(D_h\) commute with every convolution generator.

The countably many stage graphs preserve null sets. Thus an almost invariant level set of \(h\) has an exactly saturated representative modulo a null set: take its saturation under those graphs; every newly added piece comes from a null violation of invariance. This justifies using the usual measured ergodicity definition. \(\square\)

**Theorem 5.2.** An ergodic principal orbitally countable measured AF groupoid of type \(\mathrm{II}_1\) has an AFD factor of type \(\mathrm{II}_1\). Its predual is separable, and it is isomorphic to the tracial infinite tensor product of \(M_2\).

**Proof.** Ergodicity makes every invariant bounded function constant, so Lemma 5.1 makes \(M\) a factor. Its trace is finite and faithful.

The invariant probability \(\mu\) has no atoms. On a standard Borel space every probability atom contains a point of positive mass: use a countable separating family, take on each set the side carrying the atom's full measure, and intersect those sides. Their intersection has the atom's measure and contains at most one point. If such a point \(x\) had mass \(c>0\), invariance applied to singleton arrows would give mass \(c\) to every point in its orbit. That orbit would be finite. Its positive-measure saturation would be conull by ergodicity, putting the relation in type I, contrary to its specified type \(\mathrm{II}_1\). Thus \(L^\infty(X,\mu)\subset M\) is diffuse and infinite dimensional. A finite factor containing it cannot be a finite matrix algebra; it is of type \(\mathrm{II}_1\).

AFD follows from Theorem 4.2. Each \(\mathcal R_n\) is a standard Borel space with finite counting measure. Its \(L^2\) space is separable, using simple functions from a countable Borel generator. Their increasing dense union makes \(H\) separable. The concrete predual of \(M\) is a quotient of the separable trace-class predual of \(B(H)\), so it is separable. The local finite AFD uniqueness theorem now identifies \(M\) with the tracial \(M_2\) product. \(\square\)

This proof uses the given AF exhaustion. It does not need the theorem converting amenability of measured relations to approximate finiteness.

## 6. Exercises with complete solutions

**Exercise 1.** Why does a relation with classes of size two on \(X=Y\times\{1,2\}\), with a nonatomic probability space \(Y\), fail to have a finite-dimensional regular algebra?

*Solution.* Relate \((t,1)\) only to \((t,2)\), and give the two coordinates equal weight. Formula (15) gives \(M_2(L^\infty(Y))\). Its center contains all scalar fields \(a(t)1_2\), an infinite-dimensional algebra because \(Y\) is nonatomic. Class finiteness controls matrix size, not the dimension of the coefficient algebra. Finite partitions of \(Y\) give the finite-dimensional approximants in (17).

**Exercise 2.** Verify the measure normalization in (16) for a single matrix-unit field.

*Solution.* For \(F=1_E e_{ij}\), \(E\subset Y\), its \(L^2\) norm squared is \(\mu(E)\), since the kernel has one nonzero arrow per source point in \(\phi_j(E)\), and \(\mu(\phi_j(E))=\mu(E)\). Formula (16) gives \(\beta(E)/k=\mu(E)\). Its trace is zero if \(i\ne j\), and \(\mu(E)\) if \(i=j\). In particular the identity has trace \(k\mu(Y)=1\), whereas a constant diagonal matrix unit has trace \(1/k\).

**Exercise 3.** On a finite class of size three, check the orientation of convolution using the arrows \((x_1,x_2)\) and \((x_2,x_3)\).

*Solution.* Their graph kernels are matrix units \(e_{12}\) and \(e_{23}\). In (6) the only surviving intermediate point is \(x_2\), giving \(e_{12}*e_{23}=e_{13}\), the arrow \((x_1,x_3)\). Reversing their order gives zero. The involution reverses an arrow and complex conjugates its coefficient, so \(e_{12}^*=e_{21}\).

**Exercise 4.** Prove the strong convergence claim for Schur-kernel cutoffs without claiming operator-norm convergence.

*Solution.* Let \(f_n=f1_{\mathcal R_n}\). Formula (3) and dominated convergence give \(\|f_n-f\|_{L^2(\nu)}\to0\); the Schur bounds give a common operator bound. For \(g\in\mathcal C\), commutation gives
\[
(L_{f_n}-L_f)Q_g\Omega=Q_g(f_n-f),
\]
whose norm tends to zero. The vectors \(Q_g\Omega\) span a dense subspace. Approximate an arbitrary vector by this subspace and use the common bound to control the error. This proves strong convergence. It supplies no estimate forcing \(\|L_{f_n}-L_f\|\to0\).

**Exercise 5.** Show that the finite-partition matrix average in Lemma 4.1 preserves positivity and the identity.

*Solution.* If \(F(t)\ge0\) almost everywhere, then for every vector \(\zeta\in\mathbb C^k\) its cell average satisfies
\[
\left\langle\zeta,\frac1{\beta(C)}\int_C F(t)\,d\beta(t)\,\zeta\right\rangle
=\frac1{\beta(C)}\int_C\langle\zeta,F(t)\zeta\rangle\,d\beta(t)\ge0.
\]
The same computation applies to matrices of such fields, giving complete positivity. The constant identity averages to the identity. This elementary finite integral explains the norm bound, without importing general von Neumann expectation theory.

**Exercise 6.** Why is a bounded invariant diagonal function central even before ergodicity is assumed?

*Solution.* For \(h(x)=h(z)\) on almost every arrow, the products \(D_hL_f\) and \(L_fD_h\) have kernels \(h(x)f(x,z)\) and \(f(x,z)h(z)\). They agree for every generating kernel \(f\). Hence \(D_h\) commutes with their von Neumann algebra. Ergodicity is used only to make these central functions scalar.

**Exercise 7.** Identify exactly what fails if one tries to deduce a factor from a finite-class exhaustion without ergodicity.

*Solution.* The construction still gives a faithful finite trace and the finite-dimensional approximation proof still works. However a nontrivial invariant subset \(E\subset X\) gives a central projection \(D_{1_E}\), by Lemma 5.1. Its trace is \(\mu(E)\in(0,1)\), so it is neither zero nor one. Thus the algebra is not a factor. The example in Exercise 1 has precisely this obstruction.

**Exercise 8.** If a probability measure assigns an atom of mass \(c>0\) to one point in an invariant measured relation, show that its orbit has at most \(1/c\) points.

*Solution.* For each equivalent point \(y\), the singleton partial bijection \(x\mapsto y\) preserves measure, so \(\mu(\{y\})=c\). Distinct orbit points are disjoint atoms. Any \(N\) of them have total measure \(Nc\le1\), so \(N\le1/c\). The orbit is therefore finite. Ergodicity then concentrates the measure on that orbit, the type I case excluded in Theorem 5.2.

**Exercise 9.** Explain why changing to an equivalent invariant measure in (4) does not require multiplying left-convolution kernels by a density ratio.

*Solution.* Source-coordinate densities multiply a vector by \(h(y)^{-1/2}\). Left convolution sums over the first coordinate while keeping \(y\) fixed:
\[
\sum_z f(x,z)h(y)^{-1/2}\xi(z,y)
=h(y)^{-1/2}(L_f\xi)(x,y).
\]
Thus \(VL_f=L_fV\) between the two \(L^2\) spaces. A right-convolution formula changes the source coordinate and would behave differently for a noninvariant measure. Only the invariant-probability model is used for the simple right formula (7).

**Exercise 10.** The algebras \(B_{\mathcal P}\) chosen for different finite tests need not form an increasing sequence. Why is this enough here, and how does one obtain the increasing matrix sequence for the final factor?

*Solution.* The definition of local AFD asks for one finite-dimensional algebra for each finite set and neighborhood; it does not demand that choices for different tests be nested. Theorem 4.2 proves exactly that property. In the separable \(\mathrm{II}_1\) factor, the earlier finite AFD lesson's dyadic replacement and exact containment arguments convert successive local approximations into an increasing sequence of matrix subfactors. Its uniqueness proof then identifies the closure with the tracial \(M_2\) product. A claim of nesting directly from unrelated partitions at unrelated relation stages would need a separate argument.

## 7. Elementary completion of finite-partition averaging

This section supplies the scalar integration, measurable partition, and matrix averaging details in Lemma 4.1 and Exercise 5. Its starting point is the unital matrix-field identification (15), with the usual field norm and order, and the normalized trace formula (16). In particular, \(\beta(Y)=1\),
\[
\mathcal A=M_k(L^\infty(Y,\beta)),\qquad
\|F\|=\operatorname*{ess\,sup}_{t\in Y}\|F(t)\|_{\mathrm{op}},\qquad
\|F\|_{2,\tau}^2=\frac1k\int_Y\sum_{i,j=1}^k|F_{ij}(t)|^2\,d\beta(t).
\]
The argument applies to any probability measure space, including one with atoms and one whose sigma-algebra is completed. The Borel labeling, the faithful normal operator model, and the trace construction that establish (15)-(16) keep their separate prerequisite status.

### Bounded scalar integration

For a complex simple function on a finite disjoint measurable partition, define
\[
s=\sum_{j=1}^m z_j1_{D_j},\qquad
I(s)=\sum_{j=1}^m z_j\beta(D_j).
\]
Two representations have a common refinement formed from the intersections of their cells. Finite additivity on that refinement shows that \(I(s)\) is independent of the representation and complex linear. The finite sums also give positivity for real nonnegative simple functions and
\[
|I(s)|\leq I(|s|)\leq\beta(Y)\|s\|_\infty.
\]

Every bounded measurable complex function \(h\) is a uniform limit of simple functions: divide its bounded real and imaginary ranges into finitely many half-open intervals, use their measurable inverse images, and let the interval widths tend to zero. If \(s_n\to h\) uniformly, the preceding bound makes \(I(s_n)\) Cauchy. Define \(I(h)=\lim_n I(s_n)\). For another uniform simple approximation \(u_n\to h\), the same bound on \(s_n-u_n\) shows that the two limits agree. Approximating sums proves linearity. A nonnegative real function has nonnegative simple approximants, so positivity passes to the limit and real order bounds pass to integrals. Since \(|s_n|\to|h|\) uniformly,
\[
|I(h)|\leq I(|h|)\leq\beta(Y)\|h\|_\infty.
\]
The construction on a measurable subset \(C\) gives \(I_C\), with the bound \(|I_C(h)|\leq\beta(C)\|h\|_\infty\). A bounded function supported on a null set therefore has integral zero, and the integral depends only on the almost-everywhere class.

These integrals agree with the usual Lebesgue integrals of bounded functions. For a nonnegative bounded \(h\), choose grid approximants with \(s_n\leq h\leq s_n+\eta_n\), where \(\eta_n\downarrow0\). If \(u\) is any nonnegative simple function below \(h\), then \(u\leq s_n+\eta_n\). Thus the supremum of the simple integrals below \(h\) lies between \(I(s_n)\) and \(I(s_n)+\beta(Y)\eta_n\). These bounds have the same limit. Positive and negative parts extend the agreement to real functions; real and imaginary parts extend it to complex functions. All integrals used below can consequently be obtained from finite sums and uniform limits.

### One common partition and a strict error bound

Let \(F^{(1)},\ldots,F^{(r)}\in\mathcal A\) and \(\varepsilon>0\). Choose measurable representatives for their finitely many entries. A single measurable null set contains every violation of chosen finite essential bounds on those entries. Redefine all entries as zero on that set. They are now bounded everywhere and represent the original fields. If the family is empty, use \(\mathcal P=\{Y\}\).

For a nonempty family set
\[
\delta=\frac{\varepsilon}{2\sqrt{2k}}.
\]
For each real and imaginary entry \(h\), take the inverse images of
\[
[m\delta,(m+1)\delta),\qquad m\in\mathbb Z.
\]
Only finitely many bins meet the bounded range. The half-open convention assigns every value to one bin, including a value on a boundary. Take all intersections of the \(2rk^2\) resulting partitions and discard empty intersections. This gives one finite measurable partition \(\mathcal P\) of \(Y\), on whose cells every real and imaginary entry has oscillation at most \(\delta\).

On a cell with \(\beta(C)>0\), define the matrix average entry by entry:
\[
\overline F_C=\frac1{\beta(C)}\int_C F(t)\,d\beta(t),\qquad
E_{\mathcal P}F=\sum_{\beta(C)>0}1_C\overline F_C.
\]
Boundedness and finite measure justify every scalar integral. Almost-everywhere equal representatives give the same averages. The formula makes no division on a null cell; assigning zero there gives the same \(L^\infty\) field as any other assignment.

The average of a real coordinate whose values lie in \([m\delta,(m+1)\delta)\) lies in the closed interval \([m\delta,(m+1)\delta]\), by positivity and real order bounds for the integral. Each real and imaginary difference from its average therefore has absolute value at most \(\delta\), and each complex entry difference has squared magnitude at most \(2\delta^2\). Formula (16) gives, for each original field,
\[
\begin{aligned}
\|F^{(a)}-E_{\mathcal P}F^{(a)}\|_{2,\tau}^2
&\leq\frac1k\sum_{\beta(C)>0}\int_C k^2(2\delta^2)\,d\beta\\
&=2k\delta^2=\frac{\varepsilon^2}{4}.
\end{aligned}
\]
Hence every error is at most \(\varepsilon/2<\varepsilon\). This proves the constant in (18) and the strict tolerance in Lemma 4.1.

### Positive cells and representatives before completion

If there are \(s\) positive-measure cells, their indicators are nonzero orthogonal central projections summing to \(1\) in \(L^\infty(Y,\beta)\). Null cells are zero projections. The map
\[
\bigoplus_{j=1}^s M_k(\mathbb C)\longrightarrow B_{\mathcal P},
\qquad (A_1,\ldots,A_s)\longmapsto\sum_{j=1}^s1_{C_j}A_j
\]
is a unital \(*\)-homomorphism onto the algebra in (17). It is injective because a nonzero constant matrix cannot vanish almost everywhere on a positive-measure cell. Thus \(B_{\mathcal P}\) is unital and has dimension \(sk^2\). There is a positive cell since \(\beta(Y)=1\). All null cells may be adjoined to one positive cell without changing its projection, its averages, or the estimates almost everywhere.

Suppose the given sigma-algebra is the completion of \(\Sigma_0\). Each of the finitely many cells has a \(\Sigma_0\)-representative differing from it inside a \(\Sigma_0\)-measurable null set. Successively subtract earlier representatives to make them disjoint, then adjoin their uncovered complement to the first representative. Every change lies inside the finite union of those null sets. The resulting sets form an actual \(\Sigma_0\)-partition and determine the same projections and averages. In the standard Borel setting \(\Sigma_0\) can be the Borel sigma-algebra. This finite replacement uses the definition of completion and finite set operations.

### Contractivity and complete positivity

Let \(M=\|F\|\), so \(\|F(t)\|_{\mathrm{op}}\leq M\) almost everywhere. For \(u,v\in\mathbb C^k\), linearity and the scalar integral bound give
\[
\begin{aligned}
|u^*\overline F_Cv|
&=\left|\frac1{\beta(C)}\int_C u^*F(t)v\,d\beta(t)\right|\\
&\leq\frac1{\beta(C)}\int_C|u^*F(t)v|\,d\beta(t)
\leq M\|u\|\|v\|.
\end{aligned}
\]
Taking the supremum over unit vectors proves \(\|\overline F_C\|_{\mathrm{op}}\leq M\) and \(\|E_{\mathcal P}F\|\leq\|F\|\). This establishes the operator bound used in Theorem 4.2.

At matrix level \(q\), a matrix of fields is a field of \(qk\)-by-\(qk\) matrices, and the amplified map still averages each entry over the same cells. If that field \(G\) is positive almost everywhere, then for every \(w\in\mathbb C^{qk}\),
\[
w^*\overline G_Cw
=\frac1{\beta(C)}\int_C w^*G(t)w\,d\beta(t)\geq0.
\]
Each cell average is positive. This works for every \(q\), proving complete positivity and supplying the amplification step in Exercise 5. The same bilinear estimate proves contractivity at every matrix level.

The identity and all cell-constant fields are fixed, proving unitality and idempotence onto \(B_{\mathcal P}\). Constant matrices may be brought through finite scalar integrals, so for \(b,d\in B_{\mathcal P}\),
\[
E_{\mathcal P}(bFd)=b(E_{\mathcal P}F)d.
\]
Summing the cell integrals in (16) proves \(\tau(E_{\mathcal P}F)=\tau(F)\). Moreover, the integral of every entry of \(F-\overline F_C\) on its cell is zero. Hence for cell-constant \(b\),
\[
\tau\bigl(b^*(F-E_{\mathcal P}F)\bigr)=0.
\]
Expanding the trace square gives
\[
\|F\|_{2,\tau}^2
=\|E_{\mathcal P}F\|_{2,\tau}^2
+\|F-E_{\mathcal P}F\|_{2,\tau}^2,
\]
so this averaging is also contractive in the tracial \(2\)-norm. These conclusions concern the finite-partition map constructed here.

The scalar finite-bin method can be compared with Sheldon Axler, [*Measure, Integration & Real Analysis*](https://measure.axler.net/MIRA.pdf), author revision of 12 June 2026, Theorem 2.89, printed p.65 / PDF p.80. The complete proof on that page constructs measurable simple approximants and proves uniform convergence for bounded real functions. The scalar integration and matrix arguments above are independently written. The Borel, operator-model, trace, Kaplansky, concrete-predual, and type foundations retain their separately stated status.

## References and proof scope

Claire Anantharaman and Sorin Popa, [*An introduction to II₁ factors*](https://idpoisson.fr/anantharaman/publications/IIun.pdf), author draft, §1.5.2, printed pp.19–21 (PDF pp.25–27), uses the same invariant source-counting measure and convolution construction. Its operator and tracial-vector assertions omit some details; Section 3 supplies them here in full. The full Proposition 1.5.5 proof, p.21, gives the actual center/factor comparison. Appendix B.3 and B.5 state the injective-image and countable-section inputs; complete transitive free proofs of those foundations remain pending. Section 12.5, p.209, assumes a nonatomic Lebesgue probability space; Section 5 here derives nonatomicity from its stated measured type hypothesis.

Alain Connes, Jacob Feldman and Benjamin Weiss, [*An amenable equivalence relation is generated by a single transformation*](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B3AB853E37B8B8C77565C2AABC7E47F1/S014338570000136Xa.pdf/an-amenable-equivalence-relation-is-generated-by-a-single-transformation.pdf), *Ergodic Theory and Dynamical Systems* 1(4) (1981), 431–450, §4, pp.436–439, gives invariant-mean and regular Cartan context. Its converse on p.439 is explicitly a sketch. Lemma 8 is in §5, pp.440–442; Lemma 9 and Theorem 10 are in §6, pp.442–444. Theorem 10 obtains a finite-subrelation exhaustion from amenability; this lesson already assumes an AF exhaustion with fixed finite class sizes and does not use that implication. Both comparisons concern principal equivalence-relation groupoids.

The finite labeling, matrix-field approximation and nonfactor topology bridge are complete local arguments relative to the declared Borel, operator and trace-class inputs. Kaplansky density, concrete preduals, type classification and the exact local hyperfinite uniqueness prerequisites remain pending full freely accessible closure. No source expression was imported.
