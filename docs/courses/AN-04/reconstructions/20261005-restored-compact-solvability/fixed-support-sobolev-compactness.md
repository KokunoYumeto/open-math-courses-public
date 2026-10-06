# Fixed-support Sobolev spaces and compactness

This is a modified selection from *Elliptic Operators & Boundary Problems: Renewed 2026 Course Draft*. Original principal author: AN-03 course-writing task; original publisher: AN-03 local course project. Copyright © 2026 AN-03 course project contributors. The renewed edition is by the AN-03 course-writing task and OpenAI Codex. Current selection, exact prerequisite connections and explicitly identified additions: GPT-6 Astra (OpenAI), Ultra, 5 October 2026 UTC; publisher: AN-04 local course project.

Permission is granted to copy, distribute and modify this component under the GNU Free Documentation License, Version 1.2 only, with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts. The [complete licence](notices/COPYING), [title page](notices/TITLE_PAGE.md), [history](notices/HISTORY.md) and rights notice accompany it. Its combined text retains that licence.

## S0. Exact setting and earlier inputs

Section 1 below is the complete retained AN03-U023 argument I1–I2 for a closed manifold. In that retained section only, \(X\) is compact without boundary and the bundle has finite rank. S1–S4 below give the fixed-compact-support version on a possibly noncompact manifold, which is what the compact-solvability lesson uses. No density assertion for smooth functions supported in an arbitrary compact set is imported.

All real coordinate and half-density bounds are the exact [manifold transfer proof M2](../20261005-restored-invariant-folds/invariant-fold-continuity-and-sobolev-transfer.md), together with [global Sobolev multiplication G1](../20261005-cauchy-foundations/sharp-lower-bound.md#g1-global-sobolev-bounds-with-the-original-norms). The [measure, completeness and density proofs M0–M8](../20261004-free-intrinsic-graph/prerequisites/measure-and-l2.md) and [Fourier L1–L3](../20261004-free-intrinsic-graph/prerequisites/fourier-l2.md) supply all weighted spaces and pairings. The [complete Hilbert and compact-operator proof T1](../20261004-free-canonical-composition/compactness-and-essential-norms.md#t1-the-hilbert-space-facts-with-proofs) gives representation, finite-rank compactness and norm limits. The [full periodic expansion in Section 13.2](../20261005-restored-analytic-composition/scalar-kernels-and-strong-topology.md) proves the smooth kernel expansion used in I2. [Base partitions and exhaustion PS5](../20261004-free-intrinsic-graph/prerequisites/global-principal-symbol.md) give all locally finite chart choices. The [exact proof map](proof-map.json) records current versions.

The original AN03 names inside the retained argument identify these supplied proofs. The two connecting additions S2 and S3 make the weighted kernel tail and the actual fixed-support completion explicit.

## 1. Compactness and duality in bundle Sobolev spaces

Choose a finite family of relatively compact bundle charts, smooth local frames, and cutoffs \(\chi_j\) such that \(\sum_j\chi_j^2=1\). One construction starts with nonnegative subordinate functions \(\rho_j\) whose sum is positive and sets \(\chi_j=\rho_j/(\sum_k\rho_k^2)^{1/2}\). A smooth Hermitian metric is obtained by adding the local metrics with a partition of unity. Define \(H^s(X;\mathcal E)\) by the finite sum of local \(H^s(\mathbb R^n)\) norms of \(\chi_j u\), expressed as vector-valued half-density components and extended by zero. [Detecting regularity without choosing coordinates](../20261005-restored-invariant-folds/invariant-fold-continuity-and-sobolev-transfer.md) proves equivalence of these norms under changes of frame, charts, and cutoffs. Completion can equally be taken inside distributions: the local limits agree on overlaps, because multiplication and coordinate changes are continuous. Thus the spaces are Hilbert, smooth sections are dense, and
\[
\bigcap_{s\in\mathbb R}H^s(X;\mathcal E)=C^\infty(X;\mathcal E),
\qquad
\bigcup_{s\in\mathbb R}H^s(X;\mathcal E)=\mathcal D'(X;\mathcal E).
\tag{I1}
\]
For the first equality, in each chart Cauchy–Schwarz gives absolute convergence of the differentiated inverse Fourier integral when \(s>k+n/2\), hence \(k\) continuous derivatives. Conversely a compact smooth section has rapidly decreasing local Fourier transforms. For the second, the finite-order distribution bound on each of the finitely many chart supports bounds the local Fourier transform by a polynomial; it is consequently square integrable after multiplication by a sufficiently negative Sobolev weight. A common negative order works for all charts. Density follows by local convolution and cutoffs, first for each of the finitely many local components and then by summing.

For every \(\delta>0\), the inclusion
\[
H^{s+\delta}(X;\mathcal E)\longrightarrow H^s(X;\mathcal E)
\quad\text{is compact.}
\tag{I2}
\]
Here is a local proof that includes negative \(s\). For a distribution \(v\) supported in a fixed compact chart set, let \(L_R\) be the Fourier multiplier \(\psi(\xi/R)\), with \(\psi=1\) near zero and compactly supported. Then
\(\|(I-L_R)v\|_{H^s}\leq C R^{-\delta}\|v\|_{H^{s+\delta}}\).
Choose compact smooth \(\theta\) equal to one on that support. The same estimate after multiplication by \(\theta\) bounds \(v-\theta L_Rv\). On this support the latter operator has the smooth compactly supported kernel
\(\theta(x)\check\psi_R(x-y)\theta_1(y)\), where \(\theta_1=1\) on the input support. Any such kernel gives a compact map between any two fixed Sobolev spaces. To verify this claim, enclose its support in two cubes, extend it smoothly and periodically by zero in larger cubes, and expand in a double Fourier series. Integration by parts gives coefficients decreasing faster than every power of both indices. Each finite sum is a finite-rank kernel with smooth input and output functions; Cauchy–Schwarz with the fixed Sobolev weights bounds the operator-norm tail by a convergent weighted square sum. The kernel is therefore an operator-norm limit of finite-rank maps. Letting \(R\to\infty\) proves local compactness, and finitely many charts prove (I2). The same argument proves that a smooth bundle kernel is compact between all fixed Sobolev spaces and can be approximated there by smooth finite-rank kernels.

The anti-dual bundle \(E^*\) consists of conjugate-linear functionals on \(E\). As in [Detecting regularity without choosing coordinates](../20261005-restored-invariant-folds/invariant-fold-continuity-and-sobolev-transfer.md), use \(\langle u,v\rangle=\overline{v(u)}\), linear in the first argument and conjugate-linear in the second. Integration identifies the continuous anti-dual of \(H^s(X;\mathcal E)\) with \(H^{-s}(X;E^*\otimes\Omega_X^{1/2})\). Locally, this is the Fourier identity between weighted \(L^2\) spaces: Cauchy–Schwarz proves boundedness, and Hilbert representation gives every bounded functional by a Fourier function with the reciprocal weight. To pass to bundles, localize a functional with cutoffs, use that representation in each frame, and sum the resulting anti-dual sections. The pairing transition law from [Detecting regularity without choosing coordinates](../20261005-restored-invariant-folds/invariant-fold-continuity-and-sobolev-transfer.md) makes this construction independent of charts. For a closed subspace of this Hilbert space, orthogonal projection separates every vector outside it by a bounded functional. Indeed its nonzero orthogonal component supplies such a functional by the inner product. Hilbert representation itself follows from the projection theorem: for a nonzero functional, the orthogonal complement of its kernel is one-dimensional, and its value on a unit vector in that line determines the representing vector. Thus a closed subspace is exactly the common nullspace of its annihilating functionals. These statements will determine the correct cokernel space, rather than an adjoint chosen from an unrelated Sobolev inner product.

## S1. Local Fourier weights and exact pairings

The Fourier extension L1–L3 makes \(H^r(\mathbb R^n)\) a complete Hilbert space for the norm \((2\pi)^{-n/2}\|\langle\xi\rangle^r\widehat u\|_2\). Conversely a weighted L2 function gives a tempered distribution by Cauchy–Schwarz against Schwartz tests with reciprocal weight. Its inverse Fourier transform is the required \(u\). Both constructions are inverse, including negative \(r\). Weighted Cauchy–Schwarz gives the pairing of \(H^r\) and \(H^{-r}\); Hilbert representation gives every bounded conjugate-linear functional with exactly the reciprocal weight. Their distributional pairings agree by the Fourier identities first on Schwartz inputs and then by continuity.

For a compact smooth cutoff \(b\), its Fourier transform decreases faster than every power. The elementary inequality
\[
 \langle\xi+\eta\rangle^r
 \le C_r\langle\xi\rangle^r\langle\eta\rangle^{|r|}
 \tag{FSA1}
\]
holds for all real \(r\): for \(r\ge0\) use \(1+|\xi+\eta|^2\le2(1+|\xi|^2)(1+|\eta|^2)\); for \(r<0\) apply that positive-order inequality to \(\xi=(\xi+\eta)-\eta\) and rearrange. It follows that \(\|b e^{ik\cdot x}\|_{H^r}\le C_{b,r}\langle k\rangle^{|r|}\). These deliberately symmetric polynomial bounds suffice for every Fourier-series tail below.

Compact distributions have a finite test-derivative bound on each compact chart support. Applying it to a compact cutoff times \(e^{-ix\cdot\xi}\) gives polynomial growth of their Fourier transforms. Thus each belongs to some \(H^{-N}\), by choosing \(N\) so that the weighted square is integrable. The integrability follows by dyadic boxes: the shell of size \(2^j\) has volume bounded by \(C2^{nj}\), and a power less than \(-n\) makes their sum geometric. Conversely \(u\in H^r\) with \(r>k+n/2\) has continuous derivatives through order \(k\), since Cauchy–Schwarz makes \(\xi^\alpha\widehat u\) integrable. The same dyadic estimate bounds the reciprocal weight. Dominated convergence and the Fourier inverse identify these as the actual distributional derivatives. Hence all local Sobolev orders imply smoothness.

## S2. Every smooth compact kernel has the required compact action

Let \(K(x,y)\) be smooth with compact support inside two coordinate charts. Enclose that support in smaller boxes inside larger boxes. Extend by zero and periodically on the larger boxes. The full periodic expansion in Section 13.2 of the kernel companion gives coefficients \(a_{kl}\), with \(|a_{kl}|\le C_N\langle k\rangle^{-N}\langle l\rangle^{-N}\) for every \(N\), and convergence with every derivative. Insert fixed compact cutoffs \(b(x),c(y)\) equal to one on the respective support projections. Each resulting summand is a rank-one smooth kernel. Its operator norm \(H^q\to H^r\) is at most
\[
 C_{q,r}|a_{kl}|\,\langle k\rangle^{|r|}
                         \langle l\rangle^{|q|}.
 \tag{FSA2}
\]
Indeed S1 bounds the output vector, and reciprocal-weight pairing bounds the input functional by the \(H^{-q}\) norm of its compact exponential. The coefficient estimate, with \(N>n+\max(|q|,|r|)+1\), makes the double sum of these bounds finite. Finite rectangular partial sums therefore converge in the actual operator norm. The distribution kernel limit is the original \(K\), so the limit operator is its original distributional action. Finite-rank maps are compact and their norm limit is compact by T1. This supplies the complete tail argument for all real orders in I2.

## S3. Completion and compactness on one fixed support

Let \(A\subset X\) be any compact set. Choose finitely many real compact chart cutoffs \(\chi_i\) with \(\sum_i\chi_i^2=1\) near \(A\), as in PS5. Half-density chart changes are those in M2. For distributions supported in \(A\), use the sum of the squared \(H^q\) norms of their chart components \(\chi_i u\). Multiplication and coordinate changes at every real order prove equivalence for two such families: insert the second squared partition before localizing each member of the first and sum the finitely many bounded transition operators.

For completeness take a Cauchy sequence \(u_j\) in this norm. Each chart component converges in \(H^q\). Transpose the chart cutoffs and sum these limits to obtain a global distribution \(u\). The identity \(\sum\chi_i^2=1\) on the supports shows that this is the distributional limit of \(u_j\). Pairing with tests outside \(A\) proves \(\operatorname{supp}u\subset A\), and localizing that distributional equality gives exactly the previously obtained chart limits. Hence the convergence holds in the original norm. This proves that \(H^q_A\) is Hilbert. It neither changes \(A\) nor asserts density of \(C^\infty_A\).

Fix \(\delta>0\). On one of these chart supports use \(L_R=\psi(D/R)\), where \(\psi=1\) on \(|\xi|\le1\), and a compact cutoff \(\theta=1\) near the support. The frequency weight gives
\[
 \|v-\theta L_Rv\|_{H^{q-\delta}}
 \le C R^{-\delta}\|v\|_{H^q},\qquad R\ge1.
 \tag{FSA3}
\]
Here \(v=\theta v\), and multiplication by \(\theta\) is bounded in the output order. After a compact input cutoff equal to one on the original support, \(\theta L_R\) has a smooth compact kernel; S2 makes it compact from \(H^q\) to \(H^{q-\delta}\). Thus the inclusion on that fixed chart support is an operator-norm limit of compact maps. For the finite chart family, extract successive convergent subsequences of the localized components; transposing and summing the cutoffs gives convergence in the weaker fixed-support norm. The limit is still supported in \(A\). This proves compactness of \(H^q_A\hookrightarrow H^{q-\delta}_A\), including every negative \(q\), without compactness of \(X\).

## S4. Finite-chart representation and orthogonal complements

The finite chart map \(J\) embeds \(H^q_A\) isometrically as a closed subspace of a finite sum of Euclidean \(H^q\) spaces. Closedness follows from S3's actual completeness. A functional defined on any subspace of this image and bounded in its original norm extends to the Hilbert sum by the complete Hahn–Banach proof. S1 represents each component at order \(-q\). Transposing the same compact chart cutoffs gives a global distribution of local order \(-q\) with exactly the original pairing on that subspace. No density or boundary regularity of \(A\) is required.

For a closed subspace \(M\) of a Hilbert space and a vector \(x\), choose \(m_j\in M\) with \(\|x-m_j\|\) tending to its infimum. The parallelogram identity shows that \(m_j\) is Cauchy; closedness gives a minimizer \(m\). Varying \(m\) by a real and then an imaginary multiple of each vector in \(M\) makes \(x-m\) orthogonal to \(M\). This proves existence and uniqueness of the orthogonal decomposition. Pythagoras gives the projection bound one and its linearity follows from uniqueness. If a closed Hilbert subspace were infinite-dimensional, recursively choose a unit vector orthogonal to the span of the preceding finite family. Its pairwise distances are \(\sqrt2\), so its unit ball cannot be compact. Thus compactness of that unit ball forces finite dimension, including the zero subspace.
