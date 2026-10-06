# Matrix eigenvectors and tensor absorption

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Mathematical and source review by GPT-6 Astra (OpenAI), Ultra, October 2026, under the stated prerequisites. New original text is public domain (CC0).*

## Introduction

An automorphism can carry a matrix algebra with a prescribed phase on every matrix entry. If we can place infinitely many such algebras so that they commute and become increasingly central, their union forms a hyperfinite tensor factor. The automorphism then contains a concrete product action on that factor.

This is the mechanism of tensor absorption. A model of period \(p\) can be absorbed exactly when the automorphism's asymptotic period is divisible by \(p\). Infinite asymptotic period is denoted by \(0\); the model indexed by \(0\) tests every nonzero power.

The matrix and absorption arguments are [Connes], Lemmas 2.3.3–2.3.6 and Theorem 2.3.1; the related book treatment is [Takesaki III], Lemmas XVII.2.1, XVII.2.6–2.7 and Theorem XVII.2.10. We separate the finite tests, matrix estimates, product models and convergence controls. [Connes periodic] supplies classification background, and [Ando–Haagerup] supplies modern quotient context; neither substitutes for a programme proof below. The prerequisites are [Central towers and unitary cocycles](central-towers-and-unitary-cocycles.md), specifically Lemma 2.1 for proper outerness and Theorem 5.1 for aperiodic centralizer cohomology; Central sequence algebras and exact lifts, for the canonical trace, normal induced actions and exact lifts; and Strong stability and tensor absorption, for the general tensor construction. The finite-action input is the complete local proof in [Finite free actions and unitary coboundaries](finite-free-actions-and-coboundaries.md). We use center-valued trace comparison, finite matrix tensor decompositions and the strong stability theorem in the precise forms stated below.

## 1. The tensor and finite-action prerequisites

Let \(R\) be the hyperfinite factor of type II₁ with its normalized trace. A factor \(M\) is **strongly stable** when \(M\cong M\overline\otimes R\). Throughout Sections 2–3 and the absorption theorem, \(M\) is a strongly stable factor with separable predual. A bounded sequence \((x_n)\) is **strongly central** if \(\|[x_n,\psi]\|\to0\) for every \(\psi\in M_*\). An automorphism is **centrally trivial** if it fixes every such sequence modulo strong-star null sequences. The **asymptotic period** \(p_a(\theta)\) is the least positive integer \(q\) for which \(\theta^q\) is centrally trivial, or \(0\) if there is none. Section 2 of the central-tower prerequisite proves that this is the order of \(\theta_\omega\) for every free ultrafilter, with infinite order written as \(0\). Inner automorphisms induce the identity there, so inner perturbation preserves this period. Every automorphism and isomorphism in this lesson is normal.

The following two consequences of strong stability are required.

1. Given finitely many elements and normal functionals, one can find a unital copy of \(M_2(\mathbb C)\) whose matrix entries almost commute with the elements in specified strong-star seminorms and with the functionals in predual norm. The same statement holds in the relative commutant of any unital finite matrix factor. Such a relative commutant is again strongly stable.
2. Suppose mutually commuting unital matrix factors \(K_v\cong M_{d_v}(\mathbb C)\), \(d_v\geq2\), lie in \(M\). Write
   \[
   E_v(x)=\int_{\mathcal U(K_v)}uxu^*\,du,
   \tag{1.1}
   \]
   with normalized Haar measure. If a norm-total countable family \((\psi_j)\subset M_*\) satisfies
   \[
   \sum_v\|\psi_j-\psi_j\circ E_v\|<\infty\quad\text{for every }j,
   \tag{1.2}
   \]
   then \(K=\bigvee_vK_v\) is a hyperfinite II₁ factor and multiplication identifies
   \[
   M=K\overline\otimes(K'\cap M).
   \tag{1.3}
   \]

The first consequence follows from Strong stability and tensor absorption, Theorem 5.1: its proof constructs ordinary centralizing unital matrix systems; predual centrality also gives strong-star commutation with each fixed element. Lemma 4.1 identifies the centralizers after removing a finite matrix factor, and Theorem 5.1 consequently gives strong stability of that relative commutant. The second consequence is the general normal-functional proof of Theorem 3.1, which allows every separable-predual von Neumann algebra, without a trace or factor assumption.

Here (1.2) uses a norm-total family rather than a norm-dense sequence of states. This is sufficient for the two density steps of that proof. Put \(F_{m,N}=E_m\cdots E_N\). If \(\eta=\sum_{j\in J}c_j\psi_j\), with \(J\) finite, then commutativity and contractivity give, for \(L>N\geq m\),
\[
\begin{aligned}
&\|\psi\circ F_{m,L}-\psi\circ F_{m,N}\|\\
&\quad\leq2\|\psi-\eta\|\\
&\qquad+\sum_{j\in J}|c_j|\sum_{v=N+1}^{L}
\|\psi_j-\psi_j\circ E_v\|.
\end{aligned}
\tag{1.2a}
\]
First approximate \(\psi\) by \(\eta\), then use (1.2), to obtain the normal infinite-tail map \(T_m\). The same argument gives
\[
\begin{aligned}
&\|\psi-\psi\circ T_m\|\\
&\quad\leq2\|\psi-\eta\|\\
&\qquad+\sum_{j\in J}|c_j|\sum_{v\geq m}
\|\psi_j-\psi_j\circ E_v\|.
\end{aligned}
\tag{1.2b}
\]
Thus \(\psi\circ T_m\to\psi\) for every normal functional. The rest of Theorem 3.1's proof gives faithfulness, generation by \(K\) and its relative commutant, and the spatial product (1.3), with all \(d_v\geq2\) as required here. These arguments retain the provider's stated infinite-product, finite AFD, exact-lifting and functional-analytic foundations. The historical strong-stability and summability results are [Connes], Theorem 2.2.1 and Lemma 2.3.6.

We also use this finite-action result. If a finite group acts freely on a finite von Neumann algebra \(Q\), meaning that every nonidentity group element acts properly outerly, then
\[
\begin{gathered}
Z(Q^G)=Z(Q)^G,\\
u_{st}=u_s\alpha_s(u_t) \Longrightarrow\ u_s=v^*\alpha_s(v)
\end{gathered}
\tag{1.4}
\]
for some unitary \(v\in Q\). Both statements have no separability assumption. The complete construction is [Finite free actions and unitary coboundaries](finite-free-actions-and-coboundaries.md), theorem (B1)–(B3), specialized here to finite \(Q\). Section 5, (C4), proves the center identification. In Section 4, (M1)–(M2), the action on \(Q\overline\otimes M_2\) is twisted by \(\operatorname{diag}(1,u_s)\). Section 10, (D2)–(D3), proves that its two fixed diagonal projections have equal center-valued trace and are equivalent inside the fixed algebra. With initial projection \(1\otimes e_{22}\) and final projection \(1\otimes e_{11}\), their fixed off-diagonal partial isometry has entry \(v\), and (M2) is exactly \(\alpha_s(v)u_s^*=v\), hence (1.4). The center identification is what makes this trace comparison legitimate. The local lesson states and supplies its full projection, trace, fixed-point, support and topology routes; its general theorem imposes no finiteness, factor or countability assumption on the ambient algebra. [Connes], Lemma 2.3.3, retains its historical role.

The projection-division input is proved in [Dividing type-II projections and constructing matrix units](type-ii-projection-division.md), Theorem 1.1 and Corollaries 1.2–1.3. Its complete construction works with arbitrary center and cardinality: in a finite algebra it gives \(T(f)=T(e)/(n+1)\) for a nonzero piece of any nonzero \(e\), and unital matrix systems of every finite size. Section 6 also checks cancellation on the central support of \(e\) without assuming a bounded inverse of \(T(e)\). These are the exact inputs to Lemmas 1.1 and 3.1 below.

**Lemma 1.1 (the fixed algebra still has type II).** If \(Q\) is finite with no nonzero type I direct summand, and a finite group acts freely, then \(Q^G\) also has no nonzero type I direct summand.

*Proof.* Put \(F=Q^G\), \(n=|G|\), and \(E=n^{-1}\sum_s\alpha_s\). Suppose a nonzero type I summand of \(F\) existed. It would contain a nonzero abelian projection \(e\):
\[
eFe=Z(F)e.
\]
Since \(e\) is fixed, \(E\) restricts to a unital expectation on \(eQe\), and \(E(x)\geq x/n\) for positive \(x\).

Let \(T:Q\to Z(Q)\) be its normalized center-valued trace. The corner \(eQe\) is still of type II, so choose a projection \(f\leq e\) with
\[
T(f)=\frac{T(e)}{n+1}.
\]
Naturality of \(T\) and fixedness of \(e\) give \(T(E(f))=T(e)/(n+1)\). But \(E(f)=ae\) for some \(a\in Z(F)\subset Z(Q)\), by (1.4). Thus \(aT(e)=T(e)/(n+1)\), and faithfulness of \(T\) on the central support of \(e\) gives \(E(f)=e/(n+1)\). This contradicts \(E(f)\geq f/n\), after compression by the nonzero \(f\). Therefore no such \(e\) exists. \(\square\)

**Corollary 1.2 (matrices in an unrestricted fixed algebra).** Suppose \(Q\ne0\) has no nonzero direct summand of finite type I and a finite group acts freely on \(Q\). Then \(Q^G\) also has no nonzero finite type I direct summand and contains a unital matrix algebra of every size \(d\geq2\). No countability or finiteness assumption is imposed on \(Q\).

*Proof.* Let \(z\in Z(Q)\) be the finite central part: \(zQ\) is finite and \((1-z)Q\) is properly infinite. Automorphisms preserve finiteness, so \(z\) is fixed, and it is central in \(Q^G\). Freeness restricts to either nonzero invariant central part: an intertwiner in that part, extended by zero, would be an intertwiner in \(Q\).

The finite algebra \(zQ\) is type II, so Lemma 1.1 shows that \((zQ)^G=zQ^G\) is type II. On the other part, the fixed-corner assertion of the finite free-action theorem, (B1)–(B3), makes the fixed unit \(1-z\) properly infinite in \(((1-z)Q)^G\). A properly infinite unit has no nonzero finite central compression. Thus neither part of \(Q^G\) has a finite type I summand.

Use the type-II division theorem on the finite part. On the properly infinite part, use the two-piece split (NP5) in Section 2.8 of the finite-action lesson repeatedly: retain one piece and split the remaining piece until there are \(d\) orthogonal projections, all equivalent to the unit and summing to it. If these are \(q_j\), choose partial isometries \(v_j\) from \(q_1\) to \(q_j\), with \(v_1=q_1\). The elements \(v_i v_j^*\) are matrix units with diagonal sum \(1-z\). Add these units to those on \(z\); the central summands are orthogonal, so their sums are unital matrix units in \(Q^G\). A zero central part is simply absent. \(\square\)

## 2. Large matrices in relative centralizers

Write \(F=M_\omega\) for the asymptotic centralizer, with its canonical trace from Central sequence algebras and exact lifts, Theorem 3.1, where \(\omega\) is any free ultrafilter. Here \(M\) is a strongly stable factor with separable predual.

**Proposition 2.1.** For every von Neumann subalgebra \(P\subset F\) with separable predual, the finite algebra \(P'\cap F\) has no type I direct summand.

*Proof.* Choose a strong-star dense sequence \((X_j)\) in the unit ball of \(P\) and central representatives \(x_{j,k}\). Choose a norm-dense sequence \((\psi_j)\) in \(M_*\) and a faithful normal state \(\varphi\). At coordinate \(k\), the first strong stability prerequisite supplies unital matrix units \(e_{ab,k}\), \(a,b\in\{1,2\}\), satisfying
\[
\begin{gathered}
\|[e_{ab,k},\psi_j]\|<1/k,\\
\|[e_{ab,k},x_{j,k}]\|_\varphi^\sharp<1/k
\quad(j\leq k).
\end{gathered}
\tag{2.1}
\]
Here \(\|x\|_\varphi^\sharp=(\varphi(x^*x)+\varphi(xx^*))^{1/2}\). Their classes are unital matrix units in \(P'\cap F\). Commutation extends from the dense sequence to \(P\) by bounded strong-star continuity of multiplication.

Repeat the construction after adjoining each finite family of matrix units to \(P\). The enlarged algebra still has separable predual. Consequently \(P'\cap F\) contains mutually commuting unital copies of \(M_2\), and hence unital copies of \(M_{2^r}\) for every \(r\).

If a finite type I summand were nonzero, some nonzero homogeneous central summand would have type I\(_d\) for a finite integer \(d\). Compressing every one of these unital embeddings to that summand would force \(2^r\mid d\) for every \(r\), which is impossible. A finite von Neumann algebra has no infinite type I summand. Thus \(P'\cap F\) is of type II. \(\square\)

The word “unital” is essential. A small nonunital matrix corner is compatible with a type I summand; arbitrary unital matrix sizes are not.

## 3. Prescribed phases on matrix entries

Call an automorphism \(\alpha\) of \(Q\) **stable** if every unitary \(u\in Q\) can be written \(u=v^*\alpha(v)\). This is equivalent to the cohomology convention \(\alpha(w)=uw\): apply that equation to \(u^*\) and take adjoints.

**Lemma 3.1 (matrix eigenvectors).** Let \(Q\ne0\) be a von Neumann algebra with no nonzero direct summand of finite type I, let \(\alpha\in\operatorname{Aut}Q\), let \(d\geq2\), and let \(\lambda\in\mathbb T\). Suppose either:

- \(\alpha\) is stable; or
- \(\alpha^n=\mathrm{id}\), its first \(n-1\) powers are properly outer, and \(\lambda^n=1\).

Then there are unital \(d\)-by-\(d\) matrix units \((f_{ij})\) such that
\[
\alpha(f_{ij})=\lambda^{i-j}f_{ij}.
\tag{3.1}
\]

*Proof in the stable case.* Split \(Q\) into its invariant finite and properly infinite central parts, as in Corollary 1.2. On the finite part choose unital matrix units by type-II division. Their first diagonal and its image under \(\alpha\) both have normalized center-valued trace \(1/d\), so trace comparison makes them equivalent. On the properly infinite part choose the diagonal pieces all equivalent to its unit, using (NP5); the first diagonal and its image are then equivalent to that same unit. Add the two systems across the central split to obtain unital matrix units \((e_{ij})\) in \(Q\). The orthogonal sum of the two comparison partial isometries gives \(w\in Q\) with \(w^*w=e_{11}\) and \(ww^*=\alpha(e_{11})\). The unitary
\[
b=\sum_{j=1}^d\alpha(e_{j1})w e_{1j}
\]
satisfies \(be_{ij}b^*=\alpha(e_{ij})\). Set \(a=\sum_j\lambda^j e_{jj}\) and \(u=ab^*\). Then
\[
\operatorname{Ad}u\circ\alpha(e_{ij})=\lambda^{i-j}e_{ij}.
\]
By stability, \(u=v^*\alpha(v)\). Hence \(\operatorname{Ad}u\circ\alpha=\operatorname{Ad}(v^*)\circ\alpha\circ\operatorname{Ad}v\). Multiplying the last displayed eigenvector identity by \(v\) and \(v^*\) shows that \(f_{ij}=ve_{ij}v^*\) satisfies (3.1).

*Proof in the periodic case.* Corollary 1.2 gives unital matrix units \(e_{ij}\) in \(Q^\alpha\). With \(a=\sum_j\lambda^j e_{jj}\), fixedness and \(\lambda^n=1\) make \(u_k=a^k\), \(0\leq k<n\), a cocycle for the cyclic action. The unrestricted coboundary assertion (B2) of the finite-action prerequisite gives \(a=v^*\alpha(v)\); its orientation is the same as (1.4). As above, \(\operatorname{Ad}a\circ\alpha(e_{ij})=\lambda^{i-j}e_{ij}\), so \(ve_{ij}v^*\) are the required units. The case \(n=1\) simply uses \(\lambda=1\) and \(\alpha=\mathrm{id}\). \(\square\)

This retains the unrestricted ambient algebra of [Takesaki III], Lemma XVII.2.6, as well as the finite type-II case of [Connes], Lemma 2.3.3. The stable case allows every \(\lambda\in\mathbb T\); a root-of-unity condition belongs only to the finite-period case.

We use two further exact lifting statements for the asymptotic centralizer. Unital matrix units in \(F\) have central representatives that are unital matrix units at every coordinate. Also, if equivalent projections \(e_k,f_k\) represent the same projection \(E\in F\), there are partial isometries \(w_k\) from \(e_k\) to \(f_k\) whose class is \(E\). Their full proofs are Central sequence algebras and exact lifts, Theorem 6.1 for exact unital matrix systems, and Theorem 5.1, with \(U=E\), for the prescribed equivalent endpoints. Both keep the separable-predual factor hypothesis and every free ultrafilter. [Connes], Proposition 1.1.3 and Lemma 1.1.4, are the historical lifting references. On infinite factors their proofs leave small infinite complements before completing a polar partial isometry; equivalence alone does not justify an arbitrary completion being close to the identity.

**Theorem 3.2 (an exact finite matrix after a small perturbation).** Let \(M\) be a strongly stable factor with separable predual, let \(\theta\in\operatorname{Aut}M\), let \(d\geq2\), let \(\lambda\in\mathbb T\), and suppose
\[
\lambda^{p_a(\theta)}=1.
\tag{3.2}
\]
When \(p_a(\theta)=0\), (3.2) permits every \(\lambda\in\mathbb T\). Given finitely many \(\psi_l\in M_*\), a faithful normal state \(\varphi\) and \(\varepsilon>0\), there are unital matrix units \(e_{ij}\in M\) and a unitary \(a\in M\) such that
\[
\begin{gathered}
\|[e_{ij},\psi_l]\|<\varepsilon,\\
\operatorname{Ad}a\circ\theta(e_{ij})=\lambda^{i-j}e_{ij},\\
\|a-1\|_\varphi^\sharp<\varepsilon.
\end{gathered}
\tag{3.3}
\]

For \(d=1\), the same conclusion holds with \(e_{11}=1\) and \(a=1\).

*Proof.* Proposition 2.1 with \(P=\mathbb C\) makes \(F\) of type II. Put \(\gamma=\theta_\omega\). If \(p_a(\theta)=0\), the cohomology theorem makes \(\gamma\) stable. If \(p_a(\theta)=n>0\), then \(\gamma^n=\mathrm{id}\); the proper-outerness theorem for the centralizer makes its first \(n-1\) powers properly outer. Lemma 3.1 gives matrix units \(E_{ij}\in F\) with \(\gamma(E_{ij})=\lambda^{i-j}E_{ij}\).

Lift them to central systems \(e_{ij,k}\). Their first diagonals and their images under \(\theta\) are equivalent, since both belong to unital \(d\)-by-\(d\) systems in the factor \(M\). They represent the same \(E_{11}\). Use the lifting statement to choose \(w_k\) with
\[
\begin{gathered}
w_k^*w_k=e_{11,k},\\
w_kw_k^*=\theta(e_{11,k}),\qquad [(w_k)]=E_{11}.
\end{gathered}
\]
Define
\[
b_k=\sum_{j=1}^d\lambda^{1-j}\theta(e_{j1,k})w_ke_{1j,k}.
\tag{3.4}
\]
Matrix multiplication gives \(b_k^*b_k=b_kb_k^*=1\) and
\[
b_ke_{ij,k}b_k^*=\lambda^{j-i}\theta(e_{ij,k}).
\tag{3.5}
\]
The class of (3.4) is \(\sum_jE_{jj}=1\), because the factors \(\lambda^{1-j}\) cancel the eigenvalues of \(\gamma(E_{j1})\). Thus \(b_k-1\) tends strongly-star to zero along \(\omega\). Choose a coordinate at which the finitely many centrality tests and this state test are below \(\varepsilon\), and take \(a=b_k^*\). Rearranging (3.5) gives (3.3). \(\square\)

## 4. Matrix averaging and finite tensor corners

The induction needs a bound that turns matrix-entry centrality into predual control of a conditional expectation.

**Lemma 4.1.** If \(K\cong M_d(\mathbb C)\) is unital in \(M\), with matrix units \(e_{ij}\), and \(E_K\) is its Haar averaging expectation onto \(K'\cap M\), then
\[
\begin{gathered}
\|\psi-\psi\circ E_K\|\leq d^2\max_{i,j}\|[e_{ij},\psi]\|\\
(\psi\in M_*).
\end{gathered}
\tag{4.1}
\]

*Proof.* Put \(C=K'\cap M\) and \(\eta=\max_{i,j}\|[e_{ij},\psi]\|\). For \(x\in C\), \(\|x\|\leq1\), and \(i\ne j\), apply the commutator with \(e_{ii}\) to \(xe_{ij}\) to get \(|\psi(xe_{ij})|\leq\eta\). Applying the commutator with \(e_{ij}\) to \(xe_{ji}\) gives
\[
|\psi(xe_{ii})-\psi(xe_{jj})|\leq\eta.
\]
Average this over \(j\); since \(\sum_je_{jj}=1\),
\[
|\psi(xe_{ii})-\psi(x)/d|\leq\eta.
\]
Every contraction \(y\in M=K\overline\otimes C\) has a matrix expansion \(y=\sum_{i,j}x_{ij}e_{ij}\), with \(x_{ij}\in C\) contractions. On the off-diagonal entries \(E_K\) is zero; on each diagonal it replaces \(x_{ii}e_{ii}\) by \(x_{ii}/d\). Summing the \(d(d-1)\) off-diagonal and \(d\) diagonal bounds yields (4.1). \(\square\)

**Lemma 4.2 (asymptotic period survives a finite matrix leg).** Let \(M\) be a factor with separable predual, \(b\in\mathcal U(M_d(\mathbb C))\), and \(\beta\in\operatorname{Aut}C\). If
\[
M=M_d(\mathbb C)\overline\otimes C,\qquad
\theta=\operatorname{Ad}b\otimes\beta,
\]
then \(p_a(\theta)=p_a(\beta)\).

*Proof.* A bounded central sequence commutes strongly-star with all fixed scalar matrix units. Its difference from its matrix-trace average
\[
E(x)=\frac1d\sum_{i,j}e_{ij}xe_{ji}\in1\otimes C
\]
is strongly-star null. This follows by subtracting \(x=d^{-1}\sum_{i,j}e_{ij}e_{ji}x\) and using the finitely many fixed matrix-unit commutators. Normal functionals on the finite matrix tensor product have finitely many coefficient functionals, so \((1\otimes x_k)\) is central in \(M\) precisely when \((x_k)\) is central in \(C\). The same statement holds for the null ideal. Thus \(C_\omega\to M_\omega\), \([(x_k)]\mapsto[(1\otimes x_k)]\), is an isomorphism intertwining \(\beta_\omega\) and \(\theta_\omega\). Their orders agree. \(\square\)

The assertion uses a finite matrix leg. It does not identify the centralizers of arbitrary infinite tensor products this way.

## 5. Concrete product models

For \(p\geq2\), put \(\zeta_p=e^{2\pi i/p}\), choose standard matrix units in \(M_p\), and set
\[
c_p=\sum_{j=1}^p\zeta_p^j e_{jj},\qquad
\sigma_p=\bigotimes_{v=1}^\infty\operatorname{Ad}c_p
\tag{5.1}
\]
on the tracial infinite product, which is isomorphic to \(R\). Set \(\sigma_1=\mathrm{id}_R\). For \(p=0\), choose a sequence \((d_v)\) in which each integer \(d\geq2\) occurs infinitely often, and set
\[
\sigma_0=\bigotimes_v\operatorname{Ad}c_{d_v}.
\tag{5.2}
\]
Here and below a tracial product means the von Neumann algebra in the GNS representation of the tensor-product trace. The complete construction and normal extension of each specified coordinate map are supplied by [Normal tensor tests and tracial GNS identifications](../foundations/normal-tensor-and-tracial-product-foundations.md), TF0–TF3; TF1 and TF4 supply all product-functional and finite-head limits used here and in Section 6. Each finite-coordinate automorphism preserves that trace and is compatible with inclusion of larger finite heads. On their algebraic union, \(x\Omega\mapsto\sigma(x)\Omega\) is therefore an isometry with an inverse. Its unitary extension implements a normal automorphism of the generated algebra. This constructs the actions in (5.1)–(5.2).

A bijection between two coordinate sets that matches each matrix size sends a finite elementary tensor to the tensor with the same entries in the matched coordinates. It is a unital star isomorphism of the algebraic tensor unions and preserves the product trace. The same GNS isometry and its inverse extend it to a normal trace-preserving isomorphism of the von Neumann products. Matching the sizes also matches the diagonal clocks, so this isomorphism intertwines their actions. Thus the choice of sequence in (5.2) does not change its conjugacy class. The identification of each tracial matrix product with \(R\) uses the infinite-product and finite AFD uniqueness foundations stated in Section 1.

**Proposition 5.1.** These models satisfy
\[
\begin{gathered}
p_a(\sigma_p)=p,\qquad p_o(\sigma_p)=p,\\
\sigma_p\otimes\sigma_p\cong\sigma_p.
\end{gathered}
\tag{5.3}
\]
Here \(p_o\) is the order in the outer automorphism group, with infinite order denoted by \(0\).

*Proof.* For \(p\geq2\), \(\sigma_p^p=\mathrm{id}\). If \(p\nmid q\), let \(x_v\) be the entry \(e_{12}\) in coordinate \(v\). It is a bounded strongly central sequence. To check the predual norm, first take a functional \(\psi_y(x)=\tau(yx)\) with \(y\) in a finite tensor head. Every later \(x_v\) commutes with \(y\), and traciality gives \([x_v,\psi_y]=0\). Such functionals are norm dense in the predual by TF4: truncate a concrete predual vector series, approximate its vectors by finite-head vectors, and use traciality. The customary \(L^1\) route also uses bounded-density approximation in \(L^2\), hence in \(L^1\); the supplied TF4 proof establishes the needed density directly. The uniform bound \(\|[x_v,\psi]\|\leq2\|\psi\|\) extends the claim to every normal functional. Moreover,
\[
\|\sigma_p^q(x_v)-x_v\|_2
=|\zeta_p^{-q}-1|/\sqrt p>0.
\tag{5.4}
\]
Thus that power is not centrally trivial. Inner automorphisms are centrally trivial, so it is also outer. This gives both periods. For \(\sigma_0\), given \(q\ne0\), choose \(d>|q|\) and use (5.4) along its infinitely many coordinates. No nonzero power is centrally trivial or inner. The assertions for \(p=1\) are immediate.

Interlacing two sequences of size \(p\) coordinates proves the last assertion for \(p\geq2\), using the trace-GNS extension just established. For \(p=0\), each size occurs countably infinitely often in both the single and doubled coordinate sets, so choose a bijection within each size and apply the same extension. For \(p=1\), interlace the tracial \(M_2\) coordinates of \(R\overline\otimes R\); the actions on both sides are identities. These constructions give a normal isomorphism \(J_p:R\to R\overline\otimes R\) with \(J_p\sigma_p=(\sigma_p\otimes\sigma_p)J_p\) in every case. \(\square\)

For example, \(\sigma_3^2\) moves each far-out \(e_{12}\) by the fixed phase \(e^{-4\pi i/3}\). Moving the entry farther out makes it central but does not reduce this displacement.

## 6. Absorbing a model with a small inner perturbation

Automorphisms \(\theta\) on \(M\) and \(\eta\) on \(N\) are **outer conjugate** if an isomorphism \(\pi:M\to N\) and a unitary \(u\in M\) satisfy
\[
\eta=\pi\circ\operatorname{Ad}u\circ\theta\circ\pi^{-1}.
\tag{6.1}
\]
For a single automorphism, viewed as an action of \(\mathbb Z\), its inner perturbation determines a cocycle by iteration. For a finite cyclic group, one must additionally check that this iterated cocycle equals \(1\) after a full period. We retain that distinction in periodic classification.

**Theorem 6.1 (tensor absorption).** Let \(M\) be a strongly stable factor with separable predual and \(\theta\in\operatorname{Aut}M\). For \(p\in\{0,1,2,\ldots\}\), the following are equivalent:

1. \(p\) divides \(p_a(\theta)\), where divisibility by \(0\) means \(p_a(\theta)=0\).
2. \(\theta\) and \(\theta\otimes\sigma_p\) are outer conjugate.
3. For every faithful normal state \(\varphi\) and \(\delta>0\), there is a unitary \(u\) with \(\|u-1\|_\varphi^\sharp<\delta\) such that \(\theta'=\operatorname{Ad}u\circ\theta\) is conjugate to \(\theta'\otimes\sigma_p\).

*Proof of (1) implies (3).* Choose matrix sizes and phases: for \(p\geq2\), take \(d_v=p\), \(\lambda_v=\zeta_p\); for \(p=1\), take \(d_v=2\), \(\lambda_v=1\); for \(p=0\), use the sequence of (5.2), with \(\lambda_v=\zeta_{d_v}\). Choose a norm-dense sequence \((\psi_j)\) in the unit ball of \(M_*\).

We construct commuting unital matrix factors \(K_v\) with units \(e_{ij}^{(v)}\), correcting unitaries \(a_v\), and products \(U_v=a_v\cdots a_1\). At every stage require
\[
\begin{aligned}
&a_v\in(K_1\vee\cdots\vee K_{v-1})'\cap M,\\
&\|[e_{ab}^{(v)},\psi_j]\|<2^{-v}/d_v^2\\
&\qquad(1\leq a,b\leq d_v,\ j\leq v),\\
&\theta_v(e_{ij}^{(k)})=\lambda_k^{i-j}e_{ij}^{(k)}
\quad(k\leq v),\\
&\theta_v=\operatorname{Ad}U_v\circ\theta,\\
&\|U_v-U_{v-1}\|_\varphi^\sharp<\delta\,2^{-v-1},
\end{aligned}
\tag{6.2}
\]
where \(U_0=1\). Each entry is tested against every listed functional.

Assume the construction through \(v-1\). Put \(N=K_1\vee\cdots\vee K_{v-1}\) and \(C=N'\cap M\). This is a finite matrix tensor decomposition \(M=N\overline\otimes C\). The first strong stability prerequisite makes \(C\) strongly stable. The eigenvector identities already imposed make \(\theta_{v-1}\) preserve \(N\) and \(C\); on \(N\) its action is inner. Its restriction \(\beta\) to \(C\) has \(p_a(\beta)=p_a(\theta)\), by Lemma 4.2 and invariance of asymptotic period under inner perturbation. Therefore \(\lambda_v^{p_a(\beta)}=1\).

Expand the finitely many \(\psi_1,\ldots,\psi_v\) into coefficient functionals for \(N\overline\otimes C\). Making a contraction in \(C\) commute in predual norm with this finite list of coefficients makes its commutators with every original \(\psi_j\) arbitrarily small: each is a finite sum of coefficient commutators. Thus Theorem 3.2 in \(C\) can meet the second line of (6.2).

The last line requires care because \(U_{v-1}\) varies. On \(C\) use the faithful state obtained by normalizing the restriction of
\[
\chi=\varphi+\varphi\circ\operatorname{Ad}(U_{v-1}^*).
\tag{6.3}
\]
If \(a\in C\) is close enough to \(1\) in \(\|\cdot\|_\chi^\sharp\), then
\[
\begin{aligned}
&\|(a-1)U_{v-1}\|_\varphi^\sharp{}^2\\
&\quad={}(\varphi\circ\operatorname{Ad}(U_{v-1}^*))((a-1)^*(a-1))\\
&\qquad+\varphi((a-1)(a-1)^*),
\end{aligned}
\tag{6.4}
\]
is as small as required. Apply Theorem 3.2 with this state and the coefficient functionals. Set its matrix units to be \(e_{ij}^{(v)}\), and its unitary to be \(a_v\). It commutes with all previous \(K_k\), so their eigenvector identities persist; the new identities follow from (3.3). This completes the induction.

The faithful-state criterion and its uniform finite-test estimate are proved in [Bounded topology and tracial representations, Section 3A](bounded-topology-and-tracial-representations.md), with the exact preceding proofs in its companion. These results also justify the completeness step used here. In a faithful normal representation, a bounded strong-star Cauchy sequence has pointwise limits \(T\xi\) and \(S\xi\) for the operators and their adjoints, by Hilbert-space completeness. Uniform boundedness of the sequence makes \(T\) and \(S\) bounded linear operators. Passing to the adjoint pairings gives \(S=T^*\). The represented von Neumann algebra is strongly closed, so \(T\) belongs to it. For a sequence of unitaries, bounded strong continuity of multiplication passes both identities \(U_v^*U_v=U_vU_v^*=1\) to the limit; hence \(T\) is unitary. The faithful-state estimate applies to the bounded differences of two sequence terms, so state-seminorm Cauchy control supplies exactly this strong-star Cauchy hypothesis.

The summable last line of (6.2) makes both \(U_v\) and \(U_v^*\) Cauchy in the state seminorm. On bounded sets a faithful state generates the intrinsic strong-star topology, and bounded strong-star Cauchy sequences are complete. Hence \(U_v\to u\) strongly-star for a unitary \(u\), and \(\|u-1\|_\varphi^\sharp\leq\delta/2<\delta\). Conjugation by \(U_v\) converges to conjugation by \(u\), so all eigenvector identities pass to \(\theta'=\operatorname{Ad}u\circ\theta\).

By Lemma 4.1, for every fixed \(j\),
\[
\sum_{v\geq j}\|\psi_j-\psi_j\circ E_v\|
\leq\sum_{v\geq j}2^{-v}<\infty.
\]
The finitely many earlier terms are finite. The tensor-splitting prerequisite therefore gives \(M=K\overline\otimes C_\infty\), where \(K=\bigvee_vK_v\cong R\) and \(C_\infty=K'\cap M\). The eigenvector identities identify \(\theta'|_K\) with \(\sigma_p\). Since \(\theta'\) preserves \(K\), it also preserves \(C_\infty\); write its restriction there as \(\beta_\infty\). Then
\[
\theta'\cong\sigma_p\otimes\beta_\infty
\cong\sigma_p\otimes\sigma_p\otimes\beta_\infty
\cong\theta'\otimes\sigma_p,
\]
using Proposition 5.1. More explicitly, let \(\Phi:M\to R\overline\otimes C_\infty\) be the normal tensor isomorphism just constructed, with \(\Phi\theta'=(\sigma_p\otimes\beta_\infty)\Phi\). Let \(\mathrm{flip}_{23}:R\overline\otimes R\overline\otimes C_\infty\to R\overline\otimes C_\infty\overline\otimes R\) interchange the last two factors. Then the normal isomorphism
\[
\begin{aligned}
\Xi:M&\longrightarrow M\overline\otimes R,\\
\Xi&=(\Phi^{-1}\otimes\mathrm{id}_R)\circ\mathrm{flip}_{23}\\
&\qquad\circ(J_p\otimes\mathrm{id}_{C_\infty})\circ\Phi
\end{aligned}
\]
satisfies \(\Xi\theta'=(\theta'\otimes\sigma_p)\Xi\). Each factor is an isomorphism with the displayed source and target; the intertwining follows from the two identities for \(\Phi\) and \(J_p\). This proves (3).

*Proof of (3) implies (2).* Put \(\eta=\theta\otimes\sigma_p\), and let \(h:M\to M\overline\otimes R\) conjugate \(\theta'=\operatorname{Ad}u\circ\theta\) to \(\theta'\otimes\sigma_p\). Then
\[
h\circ\operatorname{Ad}u\circ\theta\circ h^{-1}
=\operatorname{Ad}(u\otimes1)\circ\eta.
\]
The unitary \(v=h^{-1}(u^*\otimes1)u\in M\) therefore satisfies \(h\circ\operatorname{Ad}v\circ\theta\circ h^{-1}=\eta\), which is (6.1).

*Proof of (2) implies (1).* Outer conjugacy preserves asymptotic period, since inner automorphisms act trivially on the asymptotic centralizer. If \(p_a(\theta)=0\), condition (1) holds for every \(p\). Otherwise let \(q=p_a(\theta)>0\). If \(p\nmid q\), Proposition 5.1 supplies a bounded central sequence \((x_v)\) in \(R\) for which \(\sigma_p^q(x_v)-x_v\) does not tend strongly-star to zero. This includes \(p=0\) and any \(q>0\). The sequence \((1\otimes x_v)\) is strongly central in \(M\overline\otimes R\): check product normal functionals and then use their norm density. It is moved by \((\theta\otimes\sigma_p)^q\). Thus that power is not centrally trivial, whereas \(\theta^q\) is. This contradicts (2), proving (1). \(\square\)

The near-identity statement concerns \(\theta'\) and its own tensor product. It does not assert that \(\theta\) is conjugate to its tensor product without an inner perturbation.

**Corollary 6.2 (extracting the factor).** Under condition (1), the unitary in (3) can be chosen so that there is a tensor decomposition \(M\cong R\overline\otimes C\) in which \(\operatorname{Ad}u\circ\theta=\sigma_p\otimes\beta\) for an automorphism \(\beta\) of \(C\).

*Proof.* This is the factor \(K\) and its relative commutant constructed in the proof of (1) implies (3), before its last reindexing. \(\square\)

**Proposition 6.3 (an arbitrarily small perturbation of the original action).** Under the equivalent conditions of Theorem 6.1, for every faithful normal state \(\varphi\) and \(\delta>0\), there are a unitary \(v\in M\) and a normal isomorphism \(h:M\to M\overline\otimes R\) such that
\[
\begin{gathered}
\|v-1\|_\varphi^\sharp<\delta,\\
h\circ\operatorname{Ad}v\circ\theta\circ h^{-1}
=\theta\otimes\sigma_p.
\end{gathered}
\]
This is the near-identity formulation printed in [Takesaki III], Theorem XVII.2.10(iii). Its right-hand action is the unperturbed \(\theta\otimes\sigma_p\), whereas Theorem 6.1(3) uses the perturbed action on both sides.

*Proof.* Corollary 6.2 gives a unitary \(u\), an action \(\alpha=\operatorname{Ad}u\circ\theta\), and a decomposition \(M=K\overline\otimes C\), where \(\alpha=\sigma_p\otimes\beta\). Keep the particular matrix coordinates \(K_v\) constructed there, and put \(A_m=K_1\vee\cdots\vee K_m\). Choose a faithful normal state \(\chi\) on \(C\), and let \(\rho=\tau_K\otimes\chi\) on \(M\).

For each \(m\), the coordinate bijection giving \(J_p\) in Proposition 5.1 can fix the first \(m\) coordinates in the first output copy of \(K\). The remaining coordinates still match the two output tails size by size: for \(p=0\) every size occurs infinitely often even after deleting a finite head; for \(p\geq2\) every size is \(p\); for \(p=1\) use size two with identity action. Extend this bijection through the trace GNS spaces and leave \(C\) fixed. After interchanging the final factors, this gives a normal isomorphism
\[
\begin{gathered}
h_m:M\longrightarrow M\overline\otimes R,\\
h_m\alpha=(\alpha\otimes\sigma_p)h_m,\\
(\rho\otimes\tau_R)\circ h_m=\rho,\\
h_m(y)=y\otimes1\quad(y\in A_m\vee C).
\end{gathered}
\]
These identities hold first on elementary tensors and then on the von Neumann algebras by normality.

The expectation \(F_m:M\to A_m\vee C\) obtained by tracing out the later \(K\)-coordinates is normal, unital and \(\rho\)-preserving. It sends contractions to contractions and \(F_m(x)\to x\) in \(\|\cdot\|_\rho^\sharp\). Indeed, on the product GNS space it acts on \(x\Omega_\rho\) as the orthogonal projection onto the first \(m\) matrix coordinates tensored with the entire \(C\)-space; these subspaces increase to a dense subspace. Apply the same argument to \(x^*\). With \(y=F_m(u^*)\), the last two identities for \(h_m\) give
\[
\begin{aligned}
&\|h_m(u^*)-u^*\otimes1\|_{\rho\otimes\tau_R}^\sharp\\
&\qquad\leq2\|u^*-F_m(u^*)\|_\rho^\sharp\longrightarrow0.
\end{aligned}
\]
Thus \(d_m=h_m^{-1}(u^*\otimes1)-u^*\) tends to zero strongly-star: its sharp seminorm equals the preceding one, it is bounded, and \(\rho\) is faithful. Fixed right multiplication by \(u\) preserves that convergence. The unitaries
\[
v_m=h_m^{-1}(u^*\otimes1)u
\]
therefore tend strongly-star to \(1\), in particular in \(\|\cdot\|_\varphi^\sharp\). The calculation in the proof of (3) implies (2), now with \(h=h_m\), gives
\[
h_m\circ\operatorname{Ad}v_m\circ\theta\circ h_m^{-1}
=\theta\otimes\sigma_p
\]
for every \(m\). Choose \(m\) with the required \(\varphi\)-error below \(\delta\). This proves the full assertion for all periods, including \(0\). \(\square\)

## 7. Exercises with solutions

**Exercise 7.1 (introductory: a phase table).** In \(M_3\), take \(\lambda=e^{2\pi i/3}\) and \(a=\sum_{j=1}^3\lambda^je_{jj}\). Find the eigenvalue of \(e_{13}\) under \(\operatorname{Ad}a\), and verify that diagonal entries are fixed.

*Solution.* Matrix multiplication gives \(ae_{ij}a^*=\lambda^{i-j}e_{ij}\). For \(e_{13}\) this is \(\lambda^{-2}=\lambda\). For \(i=j\) the eigenvalue is \(1\).

**Exercise 7.2 (intermediate: recover the lifting sign).** With \(b_k\) defined in (3.4), explain why the correcting unitary is \(b_k^*\), and check the phase on \(e_{12,k}\).

*Solution.* Equation (3.5) says \(b_ke_{12,k}b_k^*=\lambda\theta(e_{12,k})\). Thus \(b_k^*\theta(e_{12,k})b_k=\lambda^{-1}e_{12,k}\), the required phase \(\lambda^{1-2}\). Choosing \(b_k\) instead reverses the needed rearrangement.

**Exercise 7.3 (intermediate: summable centrality).** Suppose the \(v\)-th matrix factor has size \(d_v\), and for \(j\leq v\) every entry has \(\|[e_{ab}^{(v)},\psi_j]\|\leq3^{-v}/d_v^2\). Show the tensor-splitting sum (1.2) converges for every fixed \(j\), even if \(d_v\to\infty\).

*Solution.* Lemma 4.1 bounds each term for \(v\geq j\) by \(3^{-v}\). Its tail sums to \(3^{1-j}/2\). There are only finitely many earlier terms, each at most \(2\|\psi_j\|\). The matrix size cancels in the estimate, so unbounded sizes cause no problem.

**Exercise 7.4 (advanced: a periodic cocycle test).** Suppose \(\alpha^n=\mathrm{id}\) and \(a\) is a fixed unitary. What condition makes \(u_k=a^k\) a cocycle for \(\mathbb Z/n\mathbb Z\)? Why is \(a\) being fixed insufficient by itself?

*Solution.* Fixedness gives \(u_k\alpha^k(u_l)=a^{k+l}\). Reduction of the index modulo \(n\) respects this identity exactly when \(a^n=1\). Without it, the cocycle identity fails at the full-period wrap. In Lemma 3.1, \(a^n=1\) follows from \(\lambda^n=1\).

**Exercise 7.5 (advanced: the period obstruction).** An automorphism has asymptotic period \(6\). Which of the models \(\sigma_0,\sigma_1,\sigma_2,\sigma_3,\sigma_4,\sigma_6\) does Theorem 6.1 allow it to absorb?

*Solution.* It allows exactly \(\sigma_1,\sigma_2,\sigma_3,\sigma_6\), since their indices divide \(6\). The model \(\sigma_4\) has a central sequence moved by its sixth power, and \(\sigma_0\) has such a sequence for every nonzero power. Either would contradict central triviality of the sixth power after outer conjugacy.

**Exercise 7.6 (advanced: why both adjoints matter).** On \(\ell^2(\mathbb N)\), let \(u_n\) cyclically permute the first \(n\) basis vectors, sending the first to the second, and fix all remaining basis vectors. Show \(u_n\) converges strongly to the unilateral shift, but its adjoints do not converge strongly. Explain the relevance to (6.2).

*Solution.* For each fixed basis vector \(e_j\), eventually \(u_ne_j=e_{j+1}\); uniform boundedness extends this to strong convergence on all vectors. But \(u_n^*e_1=e_n\), which is not norm Cauchy. The limit is an isometry that is not onto. Strong-star Cauchy control of both products and their adjoints in (6.2) excludes this defect and makes their limit unitary.

## References

[Connes] Alain Connes, *Outer conjugacy classes of automorphisms of factors*, Annales scientifiques de l'École Normale Supérieure, série 4, 8 (1975), 383–419. Theorem 2.2.1, Lemmas 2.3.3–2.3.6 and Theorem 2.3.1 give the matrix, splitting and absorption arguments. [Article and original text](https://numdam.org/articles/10.24033/asens.1295/).

[Connes periodic] Alain Connes, *Periodic automorphisms of the hyperfinite factor of type II₁*, Acta Scientiarum Mathematicarum 39 (1977), 39–66. Background for periodic classification; no theorem from this paper is imported in the proof above. [Open original text](https://alainconnes.org/wp-content/uploads/szego.pdf).

[Ando–Haagerup] Hiroshi Ando and Uffe Haagerup, *Ultraproducts of von Neumann algebras*, Journal of Functional Analysis 266 (2014), 6842–6913. Definition 4.34 and Proposition 4.35, pages 38–39 of arXiv version 3, give quotient context; the exact programme lifting proofs used here are those cited above. [Open author version](https://arxiv.org/abs/1212.5457v3).

[OA-APPROX] *Central sequence algebras and exact lifts* (pinned source), Theorems 3.1, 5.1 and 6.1; and *Strong stability and tensor absorption* (pinned source), Theorem 3.1, Lemma 4.1 and Theorem 5.1. These pinned programme proofs supply the exact interfaces cited above; their stated projection, halving, infinite-product, finite AFD and functional-analytic prerequisites remain in force. Both lesson sources retain their original CC0 attribution.

[Takesaki III] Masamichi Takesaki, *Theory of Operator Algebras III*, Encyclopaedia of Mathematical Sciences 127, Springer, 2003. Lemma XVII.2.1; the product models; Lemmas XVII.2.6–2.7; Definition XVII.2.8 and Remark XVII.2.9; and Theorem XVII.2.10. Lemma 3.1 retains the full no-finite-type-I-summand scope; the small-perturbation theorem and absorption theorem retain the strongly stable separable-predual factor hypotheses and the zero-period model. [Publisher record](https://link.springer.com/book/10.1007/978-3-662-10453-8).
