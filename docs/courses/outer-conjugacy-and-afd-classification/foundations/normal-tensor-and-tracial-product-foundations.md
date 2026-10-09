# Normal tensor tests and tracial GNS identifications

*Classical prerequisite reconciliation and independently written interface proofs by GPT-6 Astra (OpenAI), Ultra, October 2026. Original AI programme exposition: CC0 1.0. This packet does not certify the surrounding classification programme.*

The two construction scopes below are different. TF1 concerns arbitrary concrete von Neumann algebras on Hilbert spaces of arbitrary cardinality, with no trace, separability or faithful-state assumption. TF2–TF3 construct and compare countable products equipped with specified faithful normal tracial states. The component algebras in that second construction need not be factors or finite-dimensional. Its applications here use full matrix algebras. TF4 supplies the consumer limits, retaining an arbitrary nontracial complementary tensor leg.

Inner products are linear in the first variable. Write \(\omega_{\xi,\eta}(x)=\langle x\xi,\eta\rangle\). The exact existing inputs are the real Hilbert tools, GP0, NP1–NP2, AB04–AB05, CP01–CP07, BK01–BK04, HA03 and HAP04–HAP05 in the [bounded-topology companion](bounded-topology-foundations.md), the faithful normal GNS proof in Lemma 3A.3 and the image/topology argument of Theorem 3.1 in [the bounded-topology lesson](../src/bounded-topology-and-tracial-representations.md), and TP1 of the [tracial-normality companion](tracial-normality-foundations.md). Their completed proofs are reused here. They supply Hilbert completion and Riesz representation, bounded calculus, concrete predual duality and norm closure, fixed-multiplication normality, compact dual balls and bounded strong* density. The first two companions retain the exact proof and source notices for those dependencies. No general modular or standard-form theorem is an input to this packet.

## TF0. The Hilbert tensor operations used below

Give the algebraic tensor space \(H\odot K\) the form

\[
\begin{aligned}
&\left\langle\sum_i h_i\otimes k_i,\sum_j h'_j\otimes k'_j\right\rangle\\
&\qquad=\sum_{i,j}\langle h_i,h'_j\rangle\langle k_i,k'_j\rangle.
\end{aligned}
\tag{TF.1}
\]

The bilinear relations respect this form. Choose an orthonormal basis of the finite span of the \(h_i\), and write a finite tensor as \(\sum_r e_r\otimes\ell_r\). Its squared norm is \(\sum_r\|\ell_r\|^2\). The coordinate maps on that finite span show that zero norm means the algebraic tensor itself is zero. The Hilbert completion is \(H\otimes K\); finite sums of elementary tensors are dense by construction. This is exactly the complete construction in OA-APPROX, *Infinite tensor products*, Section 10.3. That source uses the other inner-product convention; (TF.1) fixes the conversion explicitly.

For \(A\in B(H)\), expansion over finitely many orthonormal second factors proves
\(\|(A\otimes1)v\|\leq\|A\|\|v\|\). Expanding over orthonormal first factors gives the other leg. Thus \(A\otimes B\) extends boundedly, its adjoint is \(A^*\otimes B^*\), and its norm is \(\|A\|\|B\|\) when both spaces are nonzero: the reverse inequality is tested on unit elementary vectors approaching the two operator norms. Multiplication and adjoints are checked on the dense elementary span. Permutations and regroupings preserve (TF.1), have dense ranges, and therefore extend to unitaries. These are the finite tensor operations proved in Section 10.4 of that provider; all spans used in the proof are finite.

Amplification \(A\mapsto A\otimes1\) is normal on the whole of \(B(H)\). Indeed, a vector coefficient on the target pulls back to a norm limit of finite sums of vector coefficients on \(B(H)\): approximate its two vectors by finite elementary sums and use the coefficient estimate (TF.4) below and the norm bound for amplification. CP06 makes that norm limit a normal functional. Every target normal functional is a norm-convergent sum of vector coefficients by CP04–CP06; its pullback is therefore also normal, by the same norm bound and norm closure. This proves global ultraweak continuity by the defining predual tests. It makes no assertion that an arbitrary ultraweakly convergent net has a bounded tail.

Similarly, conjugation by any specified Hilbert unitary is a normal isomorphism with normal inverse: its pullback sends the vector-series test \(\sum_j\omega_{\xi_j,\eta_j}\) to \(\sum_j\omega_{U^*\xi_j,U^*\eta_j}\). These are square-summable sequences with exactly the original sums of squared norms.

## TF1. Product normal functionals are norm total

**Theorem.** Let \(M\subseteq B(H)\) and \(N\subseteq B(K)\) be concrete unital von Neumann algebras and let
\(P=(M\odot N)''\subseteq B(H\otimes K)\).
For every \(\varphi\in M_*\) and \(\psi\in N_*\) there is a unique normal functional \(\varphi\otimes\psi\in P_*\) satisfying

\[
\begin{aligned}
(\varphi\otimes\psi)(a\otimes b)&=\varphi(a)\psi(b),\\
\|\varphi\otimes\psi\|&=\|\varphi\|\|\psi\|.
\end{aligned}
\tag{TF.2}
\]

If the two functionals are positive, so is their product; a product of states is a state. Finite linear combinations of these functionals are norm dense in \(P_*\). Already the products of restricted vector functionals have norm-dense span. All Hilbert cardinalities are allowed. If either space is zero, every assertion reduces to the zero functional on the zero product algebra.

**Proof of existence, normality and norm.** For \(h\in H\), let \(S_h:K\to H\otimes K\) send \(k\) to \(h\otimes k\). For \(X\in P\), the compression
\(S_{h'}^*XS_h\) belongs to \(N\): it commutes with \(N'\), because \(X\) commutes with every \(1\otimes b'\), \(b'\in N'\), and the two elementary intertwining identities for \(S_h\) pass that commutation through the compression. BK02 gives \(N''=N\).

For a bounded linear \(\psi\) on \(N\), the formula

\[
\langle T_\psi(X)h,h'\rangle=\psi(S_{h'}^*XS_h)
\tag{TF.3}
\]

is a bounded sesquilinear form with bound \(\|\psi\|\|X\|\|h\|\|h'\|\). Riesz representation gives a linear map \(T_\psi:P\to B(H)\), with \(\|T_\psi(X)\|\leq\|\psi\|\|X\|\). If \(a'\in M'\), the relations \(S_{a'h}=(a'\otimes1)S_h\) and \(S_{h'}^*(a'\otimes1)=S_{a'^*h'}^*\), together with commutation of \(X\) and \(a'\otimes1\), show that \(T_\psi(X)a'=a'T_\psi(X)\). Thus \(T_\psi(X)\in M\). It sends \(a\otimes b\) to \(\psi(b)a\).

Choose CP06 vector-series representations
\(\varphi=\sum_i\omega_{h_i,h_i'}|_M\) and
\(\psi=\sum_j\omega_{k_j,k_j'}|_N\), with all four sequences square summable. Formula (TF.3) and absolute convergence give

\[
\varphi(T_\psi(X))
=\sum_{i,j}\langle X(h_i\otimes k_j),h_i'\otimes k_j'\rangle.
\]

The two tensor-vector families are square summable, since each double sum of squared norms factors into the two finite sums on its legs. Their index set is countable. CP06 therefore proves that this functional belongs to \(P_*\), globally. Its definition as \(\varphi T_\psi\) makes it independent of the chosen series. Its norm is at most \(\|\varphi\|\|\psi\|\). The reverse inequality follows by testing \(a\otimes b\) on the two unit balls and taking the two independent suprema. The zero-functional cases are immediate.

If \(X\geq0\) and \(\psi\geq0\), (TF.3) gives \(\langle T_\psi(X)h,h\rangle\geq0\), since \(S_h^*XS_h\geq0\). Thus positivity of \(\varphi\) proves positivity of the product. Evaluation at the identity proves the state assertion. The algebraic tensor algebra is ultraweakly dense in \(P\): BK02 identifies its bicommutant with its weak closure, HAP05 supplies bounded strong* approximants, and BK03 converts these specified bounded nets to ultraweak convergence. Two normal functionals agreeing there consequently agree on \(P\). This proves uniqueness, including for the restricted vector products.

**Proof of norm density.** CP04–CP06 represent every \(\rho\in P_*\) as
\(\rho=\sum_l\omega_{\zeta_l,\eta_l}|_P\), with \(\zeta,\eta\in\ell^2(H\otimes K)\). The norm of its tail is at most
\((\sum_{l>L}\|\zeta_l\|^2)^{1/2}(\sum_{l>L}\|\eta_l\|^2)^{1/2}\), and tends to zero. For each of the finitely many retained pairs, use TF0 to choose finite elementary sums \(\alpha,\beta\) close to \(\zeta,\eta\). Uniformly on the operator unit ball,

\[
\begin{aligned}
\|\omega_{\zeta,\eta}-\omega_{\alpha,\beta}\|
&\leq\|\zeta-\alpha\|\|\eta\|\\
&\quad+\|\alpha\|\|\eta-\beta\|.
\end{aligned}
\tag{TF.4}
\]

Expand the coefficient of those two finite sums. Each term is a product of restricted vector functionals, by (TF.2) and uniqueness. First truncate the series, then approximate its finitely many vectors closely enough that the sum of the errors in (TF.4) is as small as prescribed. This gives approximation in predual norm. No trace or faithful state has appeared. \(\square\)

This is the full mechanism in *Spatial tensor products of von Neumann algebras*, Theorems 9.2 and 10.1(1)–(2), with its concrete-predual dependencies supplied by the already inspected CP proofs. It also expands the brief density sentence in OA-APPROX, *Strong stability and tensor absorption*, Section 5.

## TF2. The countable tracial product and its GNS space

Let \((A_j,\tau_j)_{j\geq1}\) be nonzero unital von Neumann algebras with specified faithful normal tracial states. Write \(H_j=L^2(A_j,\tau_j)\), \(\Lambda_j(a)\) for the GNS vector and \(\Omega_j=\Lambda_j(1)\). Lemma 3A.3 gives the faithful normal left representation \(\lambda_j\).

Complete the increasing Hilbert union

\[
\begin{gathered}
\mathcal H_n=H_1\otimes\cdots\otimes H_n,\\
\mathcal H_n\longrightarrow\mathcal H_{n+1},\\
\xi\longmapsto\xi\otimes\Omega_{n+1},
\end{gathered}
\]

and call the completion \(H\). The common reference vector is \(\Omega\). Each inclusion is isometric by (TF.1). Finite-support elementary vectors are dense. Splitting at any finite head, or into disjoint sets of coordinates, preserves their inner products and has dense range, and so gives the corresponding Hilbert unitary. This is the pointed-product construction of OA-APPROX, Section 2, now used only at its stated countable tracial scope.

Let \(\mathcal A\) be the unital *-algebra of finite sums of local operator tensors \(\lambda_1(a_1)\otimes\cdots\otimes\lambda_n(a_n)\), acting as identity on the tail, and put \(P=\mathcal A''\). Their actions are bounded by TF0, compatible with unit padding, and faithful on each specified local factor. Finite-head amplification is normal by TF0. Each \(\Lambda_j(A_j)\) is dense in \(H_j\); approximating the finitely many factors of an elementary vector and using \(\|h\otimes k\|=\|h\|\|k\|\) therefore proves that \(\mathcal A\Omega\) is dense in \(H\). Hence this constructs the concrete countable tracial product in the specified GNS representations.

The vector functional \(\tau(X)=\langle X\Omega,\Omega\rangle\) is normal by CP06, and its value on a local elementary tensor is \(\prod_j\tau_j(a_j)\). It is faithful. For clarity, on each \(H_j\) right multiplication
\(r_j(b)\Lambda_j(a)=\Lambda_j(ab)\) is bounded by \(\|b\|\): traciality gives

\[
\|\Lambda_j(ab)\|^2
=\tau_j(a^*a\,bb^*)
\leq\|b\|^2\tau_j(a^*a).
\]

For the inequality, use traciality to replace the middle expression by \(\tau_j((a^*a)^{1/2}bb^*(a^*a)^{1/2})\), and apply \(bb^*\leq\|b\|^2 1\) between these two square roots.

Its adjoint is \(r_j(b^*)\), by the same trace identity. The local right actions commute with all local left actions, hence with \(P\), and their orbit of \(\Omega\) has the same dense span as the local left orbit. If \(X\in P\) and \(X\Omega=0\), it annihilates that dense right orbit and is zero. If \(X\geq0\) and \(\tau(X)=0\), then \(X^{1/2}\Omega=0\), and the preceding argument gives \(X=0\).

The state is tracial on \(\mathcal A\), by the finite product formula. For fixed local \(a\), the identity \(\tau(Xa)=\tau(aX)\) passes to all \(X\in P\), using ultraweak density of \(\mathcal A\), normality of \(\tau\), and BK03's fixed-multiplication normality. Now fix such an arbitrary \(X\) and use the same argument in the other variable. Thus \(\tau\) is tracial on \(P\). This proves the full faithful normal product trace without a tensor-commutant theorem.

The map \(\Lambda_\tau(X)\mapsto X\Omega\) is isometric, since its squared norm is \(\tau(X^*X)\), and its range is dense because it includes all local vectors. It extends to a unitary from the trace GNS space of \(P\) onto the constructed \(H\), intertwining left multiplication. Thus the identification with the tracial GNS product is proved, not inferred merely from agreement of scalar traces. No type or hyperfinite uniqueness assertion is needed here.

## TF3. Compatible finite identifications extend normally

**Theorem.** Let \((P,\tau)\), \((Q,\sigma)\) be von Neumann algebras with faithful normal tracial states. Let \(\mathcal A\subset P\), \(\mathcal B\subset Q\) be ultraweakly dense unital *-subalgebras. Every bijective unital *-algebra map \(\theta_0:\mathcal A\to\mathcal B\) satisfying \(\sigma\theta_0=\tau\) extends uniquely to a trace-preserving normal *-isomorphism \(\theta:P\to Q\), with normal inverse.

**Proof.** The map

\[
U_0:\Lambda_\tau(a)\longmapsto\Lambda_\sigma(\theta_0(a))
\quad(a\in\mathcal A)
\tag{TF.5}
\]

is complex linear and preserves inner products, since
\(\sigma(\theta_0(b)^*\theta_0(a))=\tau(b^*a)\).
Its domain and range are dense in their GNS spaces. Indeed HAP05 supplies bounded strong* approximation from the two subalgebras, and Theorem 3.1 transports it to their faithful normal GNS representations; applying it to the cyclic vectors gives the required density. Surjectivity onto \(\mathcal B\) proves dense range on the second side. Thus \(U_0\) extends to an onto Hilbert unitary \(U:H_\tau\to H_\sigma\), with \(U\Omega_\tau=\Omega_\sigma\).

For \(a,b\in\mathcal A\), multiplicativity gives
\(U\lambda_\tau(a)\Lambda_\tau(b)=\lambda_\sigma(\theta_0(a))U\Lambda_\tau(b)\).
The operators are bounded and these vectors are dense, so
\(U\lambda_\tau(a)U^*=\lambda_\sigma(\theta_0(a))\).
The faithful normal represented algebras are von Neumann algebras by Theorem 3.1; the same bounded approximation shows that they are generated by these two local subalgebras. Taking bicommutants therefore gives equality

\[
U\lambda_\tau(P)U^*=\lambda_\sigma(Q).
\tag{TF.6}
\]

Define \(\theta=\lambda_\sigma^{-1}\circ\operatorname{Ad}U\circ\lambda_\tau\). These maps are typed respectively from \(P\) to \(\lambda_\tau(P)\), to \(\lambda_\sigma(Q)\), and to \(Q\). The GNS maps are faithful unital *-isomorphisms onto their images, and (TF.6) proves surjectivity of the middle comparison.

Their inverses are normal at the required global scope. A *-isomorphism and its inverse preserve positive order, hence preserve every bounded increasing positive supremum: the defining least-upper-bound property transfers in both directions. Composing any positive normal functional with either inverse therefore gives an order-normal bounded positive functional. TP1 makes it ultraweakly continuous, and CP07's positive spanning theorem gives this for every predual test. This proves global normality of the inverses. TF0 proves normality of unitary conjugation; Lemma 3A.3 supplies normality of the forward GNS maps. Consequently \(\theta\) and \(\theta^{-1}\) are normal. Preservation of the reference vector proves \(\sigma\theta=\tau\). Uniqueness follows from normality and the specified ultraweak density of \(\mathcal A\). \(\square\)

For the countable products of TF2, take their local unions. Compatible trace-preserving *-isomorphisms of finite heads, or a bijective trace-preserving identification of their local tensor unions obtained by blocking and reindexing, give exactly \(\theta_0\). Every finite support must be covered in each direction; that condition proves surjectivity of the union map. TF3 then supplies the normal extension and its inverse. This is a reference-tracial product theorem, not a claim that the reference product is the universal inductive limit in the category of all von Neumann algebras.

If the second product is an already constructed algebra \(K\) generated by commuting matrix blocks and carrying a faithful normal state whose finite-head restrictions are the normalized traces, that state is tracial on \(K\) by the two density arguments of TF2. The finite-head multiplication maps must be injective and preserve those traces; under these explicit hypotheses TF3 applies to \(P\to K\). These are exactly the data proved in the tensor-splitting prerequisite. Commutation alone would not suffice for this conclusion.

If local maps intertwine specified trace-preserving product actions, their extensions intertwine those actions, because the two normal composites agree on the ultraweakly dense local union. One can also leave any fixed concrete von Neumann algebra \(C\subseteq B(L)\) unchanged: in the displayed GNS representations, \(U\otimes1_L\) conjugates \(\lambda_\tau(P)\overline\otimes C\) onto \(\lambda_\sigma(Q)\overline\otimes C\), by its action on generators and (TF.6), and is normal in both directions by TF0.

## TF4. The predual limits actually used by the consumers

First, the finite-head density used in the matrix model has a direct proof. By CP04–CP06, vector coefficients have norm-dense span in \(P_*\). Approximate their two vectors by local vectors \(a\Omega,b\Omega\), using TF2 and (TF.4). Traciality gives

\[
\begin{gathered}
\langle X a\Omega,b\Omega\rangle
=\tau(b^*Xa)=\tau(ab^*X),\\
a,b\in\mathcal A.
\end{gathered}
\tag{TF.7}
\]

The element \(ab^*\) lies in a finite tensor head. Thus the functionals \(\psi_y(X)=\tau(yX)\), with \(y\) in a finite head, have norm-dense span in \(P_*\). If \((x_v)\) is norm bounded and each \(x_v\) lies entirely beyond every fixed head for all sufficiently large \(v\), then it eventually commutes with such a \(y\). For every \(X\in P\), traciality and \(x_vy=yx_v\) give \(\tau(yXx_v)=\tau(yx_vX)\). Hence \([x_v,\psi_y]=0\) eventually. The bound \(\|[x_v,\rho]\|\leq2\sup_v\|x_v\|\|\rho\|\) extends the limit to all of \(P_*\). This proves exactly the finite-head normal-functional test used for the model's far-tail matrix units; it does not assert the entire noncommutative \(L^1\) representation theorem.

Let \(\alpha_j\) be trace-preserving normal automorphisms of the component algebras of TF2. The product of all the \(\alpha_j\), and the action \(\alpha^{(n)}\) which uses them only on the first \(n\) coordinates, are supplied by TF3. Their GNS unitaries and inverse unitaries agree eventually with the full product unitary and its inverse on every local vector. They therefore converge strongly on all vectors, since all are unitaries and local vectors are dense.

For any restricted vector functional, pullback by \(\alpha^{(n)}=\operatorname{Ad}U_n\) is the coefficient with vectors \(U_n^*\xi,U_n^*\eta\). Estimate (TF.4) proves convergence in functional norm. CP04–CP06 and the predual isometry of automorphisms extend it to every \(\rho\in P_*\). Thus the partial products converge in the \(u\)-topology. This supplies the finite-coordinate approximation invoked in the aperiodic comparison proof, without importing an unproved \(L^1\)-density theorem.

On \(C\overline\otimes P\), pullback of \(\eta\otimes\rho\) by \(\operatorname{id}\otimes\alpha^{(n)}\) is \(\eta\otimes(\rho\circ\alpha^{(n)})\). TF1 gives convergence in norm, first for these products and then for finite sums. The two predual operators are isometries, so the error on an arbitrary functional differs from its error on a chosen finite sum by at most twice the approximation error. TF1 proves the full \(u\)-limit on this possibly nontracial ambient algebra.

The same density argument transfers centralizing sequences. Define \([x,\rho](y)=\rho(yx-xy)\). If \(\sup_n\|x_n\|=B<\infty\) in \(P\) and \(\|[x_n,\rho]\|\to0\) for every \(\rho\in P_*\), then

\[
[1\otimes x_n,\eta\otimes\rho]
=\eta\otimes[x_n,\rho].
\tag{TF.8}
\]

This identity holds first on elementary operators and then everywhere by normality and density. Its norm is \(\|\eta\|\|[x_n,\rho]\|\) by TF1. Finite sums and the uniform bound \(\|[1\otimes x_n,\chi]\|\leq2B\|\chi\|\) prove the assertion for every \(\chi\in(C\overline\otimes P)_*\). There is no trace assumption on \(C\).

Finally let \(D,E\) be arbitrary concrete von Neumann algebras, and suppose the normal tensor automorphism \(\alpha\otimes\beta\) on \(D\overline\otimes E\) is specified. If \(\operatorname{Ad}u_i\to\alpha\) and \(\operatorname{Ad}v_j\to\beta\) in the \(u\)-topology, use the product directed set for \((i,j)\). The implementers \(u_i\otimes v_j\) are unitaries. For a product functional their pullback error has norm at most

\[
\begin{aligned}
&\|\varphi\circ\operatorname{Ad}u_i-\varphi\circ\alpha\|\,\|\psi\|\\
&\quad+\|\varphi\|\,\|\psi\circ\operatorname{Ad}v_j-\psi\circ\beta\|.
\end{aligned}
\tag{TF.9}
\]

Both terms tend to zero. TF1 and the predual isometry bound extend the limit to all normal functionals, proving the required tensor approximate innerness. The stated existence of the normal tensor automorphism remains a hypothesis here; this limit argument does not prove the general tensor functor theorem.

## The precise classification interfaces

The matrix absorption lesson, Section 5 and Corollary 6.2, uses TF3 for its coordinate bijections, regroupings and the map \(J_p\), tensored with the unchanged complement. The aperiodic comparison lesson, Section 3, uses TF3 for \(\iota:K_{\mathrm{mod}}\to K\), and TF4 for the limit of the finite product actions. The finite cyclic lesson, Lemma 4.1, uses TF3 for the finite trace-preserving basis permutations and their regrouped infinite product; its tensor approximate-innerness and central-sequence passages use TF1 and TF4.

The finite matrix identities, the existence and trace independence of the embedded commuting blocks, and the normal tensor splitting of the ambient algebra are still the actual hypotheses at these uses; this packet does not manufacture them. Hyperfinite uniqueness, type classification, centralizer/lifting/cohomology results, and the full representation-independent tensor functor for arbitrary normal maps are separately scoped. The general theorem TF1 has not been reduced to the countable tracial setting.

## Source and construction history

TF0–TF4 reconcile earlier independently written programme proofs: Claude Opus 5.5, *Spatial tensor products of von Neumann algebras*, Theorems 9.2 and 10.1(1)–(2), and OA-APPROX, *Infinite tensor products*, Sections 2, 4–5 and 10.3–10.4, together with *Strong stability and tensor absorption*, Theorem 3.1. The present exposition and organization were written for the exact interfaces above. These are classical mathematical constructions, not claims of new discovery.

The retained OA-APPROX construction map records Takesaki, *Theory of Operator Algebras III*, XIV.1.1–XIV.1.14 and XIV.4.10, as original targets. The tensor-course provider names Blackadar’s author edition as its basic reference. Reading access does not grant permission to copy their expression.

The independent AI text here is CC0. This packet incorporates no human expression from the separately scoped Lebl or Daws adaptations elsewhere in the infinite-product provider. Genuine component notices in the two linked foundation companions remain with their respective components.
