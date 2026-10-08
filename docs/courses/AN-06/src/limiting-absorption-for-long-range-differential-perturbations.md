# Limiting absorption for long-range differential perturbations

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

**Working question: How do radiation uniqueness and compactness create a boundary resolvent?** Normalize a hypothetical sequence for which the endpoint bound fails. Compactness produces a graph limit, radiation makes it a homogeneous outgoing solution, and the zero-flux decay identifies it as an eigenfunction. At a good energy that is impossible. At an eigenvalue the same reasoning must be applied after the appropriate orthogonality removes the pole.

The resolvent has a uniform endpoint bound near a regular energy once that energy is not an eigenvalue. A limit from either half-plane then exists, and a directional radiation condition singles out its solution. We prove the bound, all derivative boundary limits, their weak continuity, and the formula that recovers the spectral measure. At an eigenvalue, an orthogonality condition removes the resolvent pole; the remaining graph limit also has a precise description.

Read [Admissible differential perturbations](admissible-differential-perturbations.md) for the complete coefficient class and actual local products, [The Sobolev domain of an elliptic operator](the-sobolev-domain-of-an-elliptic-operator.md) for the self-adjoint realization, and [Endpoint spaces and flat energy shells](endpoint-spaces-and-flat-energy-shells.md) for the integral duality. [Combining the long-range resolvent estimates](combining-the-long-range-resolvent-estimates.md) supplies the estimate with a compact error. [Radiation for limits of long-range resolvents](radiation-for-limits-of-long-range-resolvents.md) proves radiation and strong weighted convergence for a convergent graph. [Outgoing flux and vanishing shell mass](outgoing-flux-and-vanishing-shell-mass.md) and [Weighted endpoint estimates and polynomial decay](weighted-endpoint-estimates-and-polynomial-decay.md) identify the homogeneous radiation solutions.

The spectral measure part uses the written arbitrary-self-adjoint theorem in [Self-adjoint spectral calculus with the original domain](../providers/analysis/self-adjoint-spectral-domains.md#self-adjoint-pvm-domain): its bounded Borel calculus, exact second-moment domain and Cayley-transform proof require no lower bound or separability. Its bounded input is the complete bundled unitary spectral foundation, including the scalar-measure construction and arbitrary-cardinality cyclic decomposition. [Distorted Fourier transforms and spectral density](distorted-fourier-transforms-and-spectral-density.md), Lemma 1.1, supplies the continuous-test inversion proof. Teschl [T] remains a classical reference.

Write \(D=-i\partial\), \(X=\langle x\rangle\), \(\Xi=\langle\xi\rangle\), and use an inner product linear in its first entry.

## 1. The full theorem and its topology

Let \(P_0(D)\) be a real scalar elliptic constant-coefficient differential operator of integer order \(m\ge1\). Let \(V(x,D)\) be a symmetric \(1\)-admissible perturbation, including its continuous highest coefficients, sharp translated local \(L^p\) lower coefficients, total ellipticity and positive long-range and short-range decay gaps. Its self-adjoint realization is

\[
 H=P_0(D)+V(x,D),\qquad \mathcal D(H)=H^m.
 \tag{1}
\]

For \(A_0=\{|x|<1\}\), \(A_j=\{2^{j-1}\le|x|<2^j\}\) and \(R_j=2^j\), use

\[
 \begin{aligned}
 \|f\|_B&=\sum_{j\ge0}R_j^{1/2}\|f\|_{L^2(A_j)},\\
 \|u\|_{B^*}&=\sup_{j\ge0}R_j^{-1/2}\|u\|_{L^2(A_j)}.
 \end{aligned}
 \tag{2}
\]

Here \(\dot B^*\) is the \(B^*\)-norm closure of Schwartz space. Set

\[
 \begin{gathered}
 \mathcal Y_m=\{u:D^\alpha u\in B^*,\ |\alpha|\le m\},\\
 \|u\|_{\mathcal Y_m}
       =\sum_{|\alpha|\le m}\|D^\alpha u\|_{B^*},\\
 Z(P_0)=\{P_0(\xi):\nabla P_0(\xi)=0\},\\
 \mathcal A=\{\lambda\in\mathbb R\setminus Z(P_0):
                   \ker(H-\lambda)\ne0\},\\
 \Omega=\mathbb R\setminus(\mathcal A\cup Z(P_0)).
 \end{gathered}
 \tag{3}
\]

The topology on \(\mathcal Y_m\) in this lesson is weak-star convergence of every displayed derivative against \(B\). The derivative relations must hold distributionally; these are not arbitrary independent elements of a product of dual spaces.

Let \(v(\xi)=\nabla P_0(\xi)\). At a regular energy define

\[
 \begin{gathered}
 M_\lambda=\{\xi:P_0(\xi)=\lambda\},\\
 N_\sigma(M_\lambda)
       =\{(\sigma t\,v(\xi),\xi):
                   \xi\in M_\lambda,\ t>0\},\\
 \sigma=\pm1,\\
 G_1=X^{-2}|dx|^2+\Xi^{-2}|d\xi|^2.
 \end{gathered}
 \tag{4}
\]

Thus \(h\in S(\Xi^m,G_1)\) means
\(|\partial_x^\alpha\partial_\xi^\beta h|
\le C_{\alpha\beta}X^{-|\alpha|}\Xi^{m-|\beta|}\).
All symbols act by left quantization.
Including \(t=0\) in (4) gives the same vanishing condition on a smooth symbol, by continuity along each ray.

<a id="lap-theorem"></a>

This limiting-absorption theorem is Hörmander [H4, Theorem 30.2.10].

**Theorem 1.1 (limiting absorption).** The eigenvalues in the regular free-energy set have finite multiplicity, form a discrete subset of that set, and have eigenfunctions in \(H^{m,t}\) for every real \(t\), where
\(\|u\|_{m,t}=\|X^t\langle D\rangle^m u\|_2\).
Every compact \(K\subset\Omega\) has an open neighborhood \(K'\subset\mathbb C\) and a constant \(C_K\) such that

\[
 \begin{gathered}
 f\in B,\quad z\in K',\quad\operatorname{Im}z\ne0,\\
 R(z)=(H-z)^{-1},\\
 \|R(z)f\|_{\mathcal Y_m}\le C_K\|f\|_B.
 \end{gathered}
 \tag{5}
\]

For either \(\sigma\), as \(z\to\lambda\in\Omega\) through
\(\sigma\operatorname{Im}z>0\), all derivatives through \(m\) have weak-star limits:

\[
 \begin{gathered}
 D^\alpha R(z)f\rightharpoonup^*
          D^\alpha R_\sigma(\lambda)f\\
 \text{in }B^*,\qquad |\alpha|\le m.
 \end{gathered}
 \tag{6}
\]

The limit \(u=R_\sigma(\lambda)f\) is the unique solution with

\[
 \begin{gathered}
 (H-\lambda)u=f,\qquad u\in\mathcal Y_m,\\
 h|_{N_\sigma(M_\lambda)}=0,\quad h\in S(\Xi^m,G_1)\\
       \ \Longrightarrow\ h(x,D)u\in\dot B^*.
 \end{gathered}
 \tag{7}
\]

The equation uses the actual local differential products. The map
\(\lambda\mapsto D^\alpha R_\sigma(\lambda)f\) is weak-star continuous on
\(\Omega\). If \(E\) is the spectral measure of \(H\),
\(\mu_f(A)=(E(A)f,f)\), and \(\chi\in C_c(\Omega)\), then

\[
 \begin{gathered}
 \int\chi\,d\mu_f\\
   =\frac{\sigma}{\pi}
       \int_{\mathbb R}\chi(\lambda)
          \operatorname{Im}(R_\sigma(\lambda)f,f)\,d\lambda,\\
 f\in B.
 \end{gathered}
 \tag{8}
\]

Both empty free shells and dimension one are included. An eigenvalue has been excluded in (5) and (7); Section 8 gives the exact replacement there.

## 2. Compactness of bounded derivative graphs

<a id="lap-compactness"></a>

**Lemma 2.1.** A bounded sequence in \(\mathcal Y_m\) has a subsequence for which every derivative converges weak-star in \(B^*\) to the corresponding derivative of one distribution \(u\). Along that subsequence,

\[
 u_j\longrightarrow u\quad\text{in }H^{0,-b}
              \qquad\text{for every }b>1/2.
 \tag{9}
\]

**Proof.** Here are the Hilbert-space details of the extraction. The [Euclidean measure and density proof](../providers/analysis/finite-derivative-l2.md#euclidean-products) approximates finite-measure sets by finite unions of bounded rectangles. Moving their endpoints to rationals changes the volume by an arbitrarily small amount. Thus finite linear combinations of rational rectangles, with rational real and imaginary coefficients, are countable and dense in \(L^2\). Restricting them to \(A_j\) proves separability of \(L^2(A_j)\). The endpoint duality identifies \(B\) with their weighted \(\ell^1\) sum; finite shell truncations and the same rational combinations prove separability of \(B\).

Apply Gram–Schmidt to a countable dense list in a shell, skipping zero residuals. It gives an orthonormal basis, since the closed span contains the dense list. The [elementary Hilbert proof](../providers/analysis/finite-trace-ideals.md#elementary-hilbert-tools) supplies Bessel's inequality, convergence of square-summable orthogonal series and approximation by finite projections. For a sequence of shell norms at most \(M\), each coordinate is bounded. Repeated extraction in the real and imaginary coordinates, followed by the countable diagonal, makes every coordinate converge to \(c_k\). For every \(N\), \(\sum_{k\le N}|c_k|^2\le M^2\), so \(\sum_k c_ke_k\) converges in \(L^2\) to a vector of norm at most \(M\). Testing first against finite basis sums and then approximating any test in norm proves weak convergence. The same finite-projection inequality proves lower semicontinuity of the norm. A further countable diagonal over the shells and finitely many derivatives gives all the shellwise weak limits together.

The normalized shell bound passes to the limits by weak lower semicontinuity. Thus each joined limit belongs to \(B^*\). Against a test in \(B\), the finite-shell part converges weakly and the remaining pairing is bounded by the uniform endpoint norm times the \(B\)-norm of the test's tail. This proves weak-star convergence. Compact smooth tests show that the limits respect all distributional derivative identities.

The derivative bounds give boundedness in \(H^m\) on every fixed ball. The finite-rank kernel argument in [Radiation for limits of long-range resolvents, Section 3](radiation-for-limits-of-long-range-resolvents.md#radiation-local-compactness) then gives local compactness: a compact cutoff followed by a Fourier cutoff at frequency \(L\) has an \(L^2\) remainder at most \(CL^{-m}\) times that local \(H^m\) bound. For fixed \(L\), its map between bounded supports has a square-integrable kernel, hence is a norm limit of finite-rank maps by approximation of that kernel by finite tensor sums. The local sequence is consequently \(L^2\) precompact. Every convergent local subsequence has the already identified distributional limit \(u\); if the whole sequence did not converge locally, a subsequence a fixed distance from \(u\) would have a convergent further subsequence, a contradiction.

For the tail, the uniform endpoint bound gives

\[
 \begin{aligned}
 \|1_{\{|x|>R\}}X^{-b}(u_j-u)\|_2^2
 &\le C_b\sup_j\|u_j-u\|_{B^*}^2\\
 &\quad\cdot\sum_{R_k\gtrsim R}R_k^{1-2b}.
 \end{aligned}
 \tag{10}
\]

The last geometric tail tends to zero exactly when \(b>1/2\). Choose \(R\), then use local convergence on its interior. This proves (9). \(\square\)

<a id="lap-rough-graph"></a>

**Lemma 2.2 (limits of the actual equation).** Suppose also
\(z_j\to\lambda\) and
\((H-z_j)u_j=f_j\to f\) in \(B\). Then
\((H-\lambda)u=f\) with the actual local products. For a graph of nonreal resolvents approaching from one fixed half-plane, its limit has the corresponding radiation condition (7).

**Proof.** On a compact set, all derivatives converge weakly in \(L^2\). The [sharp local coefficient multiplier](admissible-differential-perturbations.md#admissible-global-mapping) is a bounded map from local \(H^m\) to \(L^2\), after input and output compact cutoffs. This holds even for unbounded lower coefficients. Its weak continuity identifies the limit of the local differential expression; no rough coefficient is differentiated. The limiting equation follows from \(f_j\to f\) and \(z_j\to\lambda\).

For upper resolvents, the [full graph-limit theorem](radiation-for-limits-of-long-range-resolvents.md#radiation-theorem) applies. Its [strong weighted graph argument](radiation-for-limits-of-long-range-resolvents.md#radiation-rough-graph) also upgrades (9) to strong \(H^{m,-b}\) convergence on these graphs, using the weighted graph inequality on already known weighted inputs. The latter inequality does not assert new regularity of an arbitrary distribution.

For a lower graph, apply the upper theorem to

\[
 \begin{gathered}
 \widetilde H=-H,\quad \widetilde P_0=-P_0,\quad\\
 \widetilde V=-V,\quad w_j=-z_j,\quad\\
 g_j=-f_j.
 \end{gathered}
 \tag{11}
\]

The full \(1\)-admissible class, ellipticity and domain are preserved. Moreover
\((\widetilde H-w_j)^{-1}g_j=R(z_j)f_j\), while
\(\nabla\widetilde P_0=-v\) makes its positive bundle exactly
\(N_-(M_\lambda)\). This gives the lower radiation condition and the same weighted convergence. \(\square\)

<a id="lap-topology"></a>

On every bounded subset of \(\mathcal Y_m\), this weak-star topology is metrizable. If \((\psi_k)\) is dense in \(B\), one possible metric is

\[
 \begin{gathered}
 d(u,w)=\\
 \sum_{|\alpha|\le m}\sum_{k\ge1}2^{-k}
       \frac{|(D^\alpha(u-w),\psi_k)|}
            {1+|(D^\alpha(u-w),\psi_k)|}.
 \end{gathered}
 \tag{12}
\]

This is a metric: the tests separate distributions by density, and \(s/(1+s)\) is increasing and subadditive for \(s\ge0\), since \((s+t)/(1+s+t)\le s/(1+s)+t/(1+t)\). These facts give separation and the triangle inequality term by term. Convergence of this metric gives convergence against every \(B\) test by density and the common endpoint bound. Conversely convergence against every test makes each summand tend to zero; the summable majorant proves convergence of the metric.

## 3. Homogeneous radiation solutions are eigenfunctions

<a id="lap-homogeneous"></a>

**Lemma 3.1.** At any regular free energy \(\lambda\), a homogeneous solution \(u\in\mathcal Y_m\) satisfying either sign of (7) is an \(L^2\) eigenfunction, and in fact belongs to \(H^{m,t}\) for every real \(t\).

**Proof.** For the upper condition, the [zero-flux corollary](outgoing-flux-and-vanishing-shell-mass.md#flux-zero) applies to \(f=0\), whose imaginary pairing is zero. It gives

\[
 D^\alpha u\in\dot B^*,\qquad |\alpha|\le m.
 \tag{13}
\]

The [homogeneous polynomial-decay corollary](weighted-endpoint-estimates-and-polynomial-decay.md#decay-homogeneous) now gives \(u\in H^{m,t}\) for every \(t\). In particular \(u\in H^m=\mathcal D(H)\), so its actual differential equation is the operator eigenvalue equation.

For the lower condition apply zero flux to \(-H\), free energy \(-\lambda\), and zero forcing, as in (11). The conclusion (13) is unchanged. Apply the same weighted decay result to the original equation. An empty shell causes no difficulty in either result. \(\square\)

Conversely every regular-energy eigenfunction has all these weights, by [the point-spectrum theorem](weighted-endpoint-estimates-and-polynomial-decay.md#decay-point-spectrum). In particular each of its derivatives belongs to \(B\), \(L^2\) and \(\dot B^*\). A full-order symbol action belongs to \(L^2\): use the [exact decomposition into order-zero maps followed by derivatives](radiation-for-limits-of-long-range-resolvents.md#radiation-exact-bundle), and their \(L^2\) bounds. Hence it satisfies both radiation conditions. We have proved, at a regular energy,

\[
 \begin{gathered}
 \{\text{homogeneous solutions of (7)}\}\\
           =\ker(H-\lambda)\\
 \text{for either sign}.
 \end{gathered}
 \tag{14}
\]

<a id="lap-open-energies"></a>

The weighted endpoint lesson also proves finite multiplicity and local finiteness of these eigenvalues. The set \(Z(P_0)\) is closed: if critical values converge, ellipticity bounds the corresponding frequencies, and a subsequence converges to a critical point. Local finiteness of \(\mathcal A\) away from this closed set shows that \(\mathcal A\cup Z(P_0)\) is closed. Thus \(\Omega\) is open.

<a id="lap-compact-error"></a>

## 4. Removing the compact error

The [combined-estimate theorem](combining-the-long-range-resolvent-estimates.md#combined-theorem) gives, on a fixed punctured disc about each regular \(\lambda\),

\[
 \|R(z)f\|_{\mathcal Y_m}
       \le C_\lambda\bigl(\|f\|_B+\|R(z)f\|_{0,-1}\bigr).
 \tag{15}
\]

Both half-planes are included, and the constant is fixed before a sequence is chosen.

Fix \(\lambda\in\Omega\). Suppose that no smaller disc has a bound without the second term. For each \(j\), choose a nonreal \(z_j\) within \(1/j\) of \(\lambda\) and a forcing whose resolvent-to-forcing norm ratio exceeds \(j\). Normalize its solution and forcing by the solution's nonzero \(\mathcal Y_m\) norm. Renaming them, we obtain

\[
 \begin{gathered}
 u_j=R(z_j)f_j,\qquad\\
 \|u_j\|_{\mathcal Y_m}=1,\qquad \|f_j\|_B<1/j.
 \end{gathered}
 \tag{16}
\]

For large \(j\), all \(z_j\) lie in the disc for (15). Extract a subsequence with one fixed sign of imaginary part, and then apply Lemma 2.1. It gives a weak-star derivative limit \(u\) and strong \(H^{0,-1}\) convergence. Equation (15) consequently gives

\[
 1\le C_\lambda\|u\|_{0,-1}.
 \tag{17}
\]

Thus \(u\ne0\). Lemma 2.2 gives the homogeneous actual equation and the radiation condition at \(\lambda\), with the chosen sign. Lemma 3.1 makes \(u\) an eigenfunction, contradicting \(\lambda\in\Omega\). A smaller disc therefore has the full bound (5).

For compact \(K\subset\Omega\), cover \(K\) by finitely many such discs and take the maximum of their constants. Their union is a complex neighborhood \(K'\), giving (5) for every nonreal \(z\) in it. The centers and radii can first be reduced so that their real traces lie in \(\Omega\). This proves the uniform estimate required by Theorem 1.1.

<a id="lap-boundary"></a>

## 5. Existence and full radiation characterization

Fix \(\lambda\in\Omega\), \(f\in B\), and one sign \(\sigma\). For every sequence \(z_j\to\lambda\) from that half-plane, (5) makes its derivative graphs bounded. Lemmas 2.1 and 2.2 give a subsequential limit \(u\) satisfying the actual equation and (7).

If \(u_1,u_2\) are two such limits, their difference is a homogeneous solution in \(\mathcal Y_m\). Every action by a symbol vanishing on the chosen bundle is the difference of two elements of the closed linear space \(\dot B^*\). Lemma 3.1 therefore makes \(u_1-u_2\) an eigenfunction. There is no such eigenfunction at \(\lambda\), so \(u_1=u_2\).

All convergent subsequences have this one limit. If the original sequence did not converge in (12), a subsequence would stay a positive metric distance from that limit; Lemma 2.1 would supply a further subsequence converging to it, a contradiction. This proves (6) for every sequence. It also proves the limit as \(z\) approaches \(\lambda\) through the entire half-plane: failure of any weak-star test limit would produce a sequence witnessing that failure. No restriction on the ratio of real to imaginary displacement is imposed.

The limit depends linearly on \(f\), and weak lower semicontinuity on each shell gives

\[
 \|R_\sigma(\lambda)f\|_{\mathcal Y_m}
       \le C_K\|f\|_B,\qquad \lambda\in K.
 \tag{18}
\]

The distributional derivatives in (6) are those of its zeroth-order limit, by compact smooth testing. For any other solution of the actual equation with the derivative and radiation conditions (7), subtraction of the constructed solution again gives a homogeneous radiation solution. The same argument proves equality. This establishes the full characterization, including solutions that were not supplied with an approximating resolvent graph.

<a id="lap-continuity"></a>

## 6. Continuity up to the real boundary

Radiation at a varying energy must be justified; its bundle is also varying. We use genuine nonreal approximants to do so.

Let \(\lambda_j\to\lambda\) in \(\Omega\), with \(f_j\to f\) in \(B\). All these real energies lie eventually in one compact interval contained in \(\Omega\), so (18) gives one common bound. Choose a countable dense set \((\psi_k)\) in \(B\). For every \(j\), existence of the boundary limit at the fixed energy \(\lambda_j\) lets us choose \(0<\eta_j<1/j\) such that, for every \(|\alpha|\le m\) and \(k\le j\),

\[
 \begin{gathered}
 z_j=\lambda_j+\sigma i\eta_j,\\
 |(D^\alpha[R(z_j)f_j-R_\sigma(\lambda_j)f_j],\psi_k)|<1/j.
 \end{gathered}
 \tag{19}
\]

The endpoint bound is uniform for both terms. Thus their difference tends weak-star to zero against every \(B\) test, by density. Now \(z_j\to\lambda\), and Lemma 2.2 applies to the graphs \(R(z_j)f_j\). Every subsequential limit solves the equation with forcing \(f\) and has radiation on the bundle at the limiting energy \(\lambda\). The uniqueness just proved makes that limit \(R_\sigma(\lambda)f\). Compactness and the metric argument give

\[
 D^\alpha R_\sigma(\lambda_j)f_j
       \rightharpoonup^*D^\alpha R_\sigma(\lambda)f.
 \tag{20}
\]

The same proof permits \(z_j\) already in the closed chosen half-plane: keep its genuinely nonreal terms, and approximate only the real-boundary terms as in (19). At a nonreal limiting point, the [resolvent identity and ordinary \(L^2\) bound](resolvents-domains-and-spectral-density.md#u001-resolvent-identities) give continuity in \(H^m\), hence in \(\mathcal Y_m\). Indeed

\[
 \begin{gathered}
 R(z)-R(w)=(z-w)R(z)R(w),\\
 \|R(z)\|_{L^2\to L^2}\le|\operatorname{Im}z|^{-1},\\
 \|u\|_{H^m}\le C\bigl(\|Hu\|_2+\|u\|_2\bigr).
 \end{gathered}
 \tag{21}
\]

On a disc that stays off the real axis, the first two lines control the \(L^2\) difference; the resolvent equations and the graph inequality control its \(H^m\) norm. Thus the boundary extension is jointly continuous for strong \(B\) forcing and weak-star derivative output, locally in the closed half-plane away from \(\mathcal A\cup Z(P_0)\).

In particular, with \(f\) fixed, the scalar pairing
\((R(z)f,f)\) is continuous up to either real boundary. This uses \(f\in B\) as the test in the endpoint duality, rather than an unproved \(L^2\) boundary convergence.

<a id="lap-poisson"></a>

## 7. Recovering the spectral measure with the correct sign

Here we use the general projection-valued spectral theorem specified before Section 1. It gives, for \(f\in L^2\) and \(\varepsilon>0\),

\[
 \begin{gathered}
 \sigma\operatorname{Im}(R(\lambda+\sigma i\varepsilon)f,f)\\
       =\int_{\mathbb R}
          \frac{\varepsilon}{(t-\lambda)^2+\varepsilon^2}
                    \,d\mu_f(t).
 \end{gathered}
 \tag{22}
\]

This sign is fixed by our convention \(R(z)=(H-z)^{-1}\) and an inner product linear in the first entry.

For completeness, take real \(\chi\in C_c(\mathbb R)\). The kernel in (22) integrates in \(\lambda\) to \(\pi\), and \(\mu_f(\mathbb R)=\|f\|_2^2\). Fubini is therefore justified with a bounded signed test. If

\[
 P_\varepsilon(s)
       =\frac{\varepsilon}{\pi(s^2+\varepsilon^2)},
 \tag{23}
\]

the tested right side, divided by \(\pi\), is
\(\int(P_\varepsilon*\chi)(t)\,d\mu_f(t)\).
It converges to \(\int\chi\,d\mu_f\). To see the uniform convergence of the convolution, split at \(|s|=\rho>0\). The inner part of its error is bounded by the uniform modulus of continuity \(\omega_\chi(\rho)\). The outer part is at most

\[
 2\|\chi\|_\infty
       \int_{|s|>\rho}P_\varepsilon(s)\,ds
       \le \frac{4\|\chi\|_\infty\varepsilon}{\pi\rho}.
 \tag{24}
\]

Let \(\varepsilon\downarrow0\), then \(\rho\downarrow0\). We have independently supplied the continuous-test Poisson argument of Lemma 1.1 in the distorted Fourier lesson; it requires no spectral lower bound.

Now suppose \(\chi\in C_c(\Omega)\) and \(f\in B\). A compact neighborhood of its support lies in \(\Omega\), and (5) gives, for all sufficiently small \(\varepsilon\),

\[
 |(R(\lambda+\sigma i\varepsilon)f,f)|
           \le C\|f\|_B^2
           \quad(\lambda\in\operatorname{supp}\chi).
 \tag{25}
\]

Section 6 gives pointwise convergence of this scalar pairing to its boundary pairing. Dominated convergence in the \(\lambda\) integral of (22), combined with the Poisson argument, proves (8). A complex continuous test follows by separating its real and imaginary parts. This completes every assertion of Theorem 1.1. \(\square\)

<a id="lap-density"></a>

The continuous nonnegative function

\[
 q_{\sigma,f}(\lambda)
       =\frac{\sigma}{\pi}
              \operatorname{Im}(R_\sigma(\lambda)f,f)
              \quad(\lambda\in\Omega)
 \tag{26}
\]

is the density of \(\mu_f\) there. Nonnegativity follows from (22) and boundary continuity. To justify the measure identification, fix a bounded open interval \(J\) with \(\overline J\subset\Omega\). For every open subinterval \((a,b)\subset J\), the continuous functions

\[
 \chi_k(t)=\min\{1,k\operatorname{dist}(t,\mathbb R\setminus(a,b))\}
\]

have compact support in \(\Omega\) and increase to \(1_{(a,b)}\). Monotone convergence in (8) gives equality of the two measures on these intervals, including \(J\). Both measures are finite on \(J\), since \(q_{\sigma,f}\) is bounded on \(\overline J\). The intervals and the empty set form an intersection-stable family generating its Borel sets. The [proved pi-lambda argument](../providers/analysis/finite-derivative-l2.md#pi-lambda-uniqueness) therefore gives equality on all Borel subsets of \(J\). Countably many such intervals cover \(\Omega\); disjointifying that cover proves equality throughout \(\Omega\). Finally two continuous densities with the same measure agree at every point: a nonzero difference at one point would have a fixed sign bounded away from zero on a smaller interval and a nonzero integral there. This also proves that the two signs give the same continuous density.

<a id="lap-projection"></a>

## 8. The reduced boundary value at an eigenvalue

Fix \(\lambda_0\in\mathcal A\), and let
\(Z_0=\ker(H-\lambda_0)\). It has a finite orthonormal basis
\(\phi_1,\ldots,\phi_d\); every basis vector is in \(H^{m,t}\) for every \(t\). In particular \(\phi_\ell\in B\), so the orthogonal projection has a consistent extension from \(L^2\) to \(B^*\):

\[
 \Pi u=\sum_{\ell=1}^d(u,\phi_\ell)\phi_\ell.
 \tag{27}
\]

The integral pairings in (27) are absolutely defined by endpoint duality. This map is bounded on \(B\), and maps \(B^*\) boundedly into \(\mathcal Y_m\). Indeed the basis vectors and all their derivatives belong to both \(B\) and \(B^*\); the finite sum gives both bounds. It is continuous from bounded weak-star derivative graphs to the norm topology of \(\mathcal Y_m\), because each coefficient is a \(B\) test.

Write

\[
 B_\perp=\{f\in B:\Pi f=0\}.
 \tag{28}
\]

On \(L^2\), self-adjointness and the eigenvalue equation give
\(\Pi R(z)=R(z)\Pi=(\lambda_0-z)^{-1}\Pi\). Explicitly, if
\((H-z)u=f\), pairing with \(\phi_\ell\) gives
\((f,\phi_\ell)=(\lambda_0-z)(u,\phi_\ell)\).
Thus

\[
 R(z)f=(\lambda_0-z)^{-1}\Pi f
                   +R(z)(I-\Pi)f.
 \tag{29}
\]

<a id="lap-reduced"></a>

**Theorem 8.1 (reduced limiting absorption).** There is a disc about \(\lambda_0\), containing no other regular eigenvalue or critical free energy on its real trace, such that

\[
 \begin{gathered}
 \|R(z)f\|_{\mathcal Y_m}\le C\|f\|_B,\\
 f\in B_\perp,\quad\operatorname{Im}z\ne0.
 \end{gathered}
 \tag{30}
\]

For either sign, these resolvents have derivative weak-star limits
\(R^\perp_\sigma(\lambda_0)f\). Their limits are orthogonal to \(Z_0\) under (27). They are the unique solutions of (7) at \(\lambda_0\) with this additional orthogonality.

**Proof.** Discreteness from Section 3 and closedness of \(Z(P_0)\) let us choose the stated disc. The compact-error estimate (15) holds there. If (30) failed on every smaller disc, repeat the normalization (16) with all \(f_j\in B_\perp\). The solutions also obey \(\Pi u_j=0\), by (29). Lemmas 2.1 and 2.2 yield a nonzero homogeneous radiation solution \(u\) at \(\lambda_0\), exactly as in (17). Lemma 3.1 gives \(u\in Z_0\). Testing its weak-star limit against the finitely many \(\phi_\ell\in B\) also gives \(\Pi u=0\), a contradiction. This proves (30).

The compactness and uniqueness arguments in Section 5 now apply on the orthogonal space. Every limit has radiation and \(\Pi u=0\). The difference of two limits is in \(Z_0\) by Lemma 3.1, and is also orthogonal to it; hence it is zero. The constructed solution is unique among all solutions with these conditions. \(\square\)

<a id="lap-reduced-continuity"></a>

On a smaller real interval \(I\) about \(\lambda_0\), this gives a continuous reduced boundary family
\(R^\perp_\sigma(\lambda):B_\perp\to\mathcal Y_m\), including
\(\lambda=\lambda_0\). For other \(\lambda\in I\), it is the restriction of
\(R_\sigma(\lambda)\), whose outputs remain orthogonal to \(Z_0\) by (29).
The argument of Section 6 applies with the same uniform estimate (30); at the center its uniqueness statement is the orthogonal uniqueness just proved. Thus continuity includes all derivatives in the weak-star topology, and also strong \(B_\perp\) variation of the forcing.

<a id="lap-graph"></a>

## 9. The complete graph limit at an eigenvalue

Fix any sequence \(z_j\to\lambda_0\) through one chosen half-plane. A limiting graph pair means

\[
 \begin{gathered}
 u_j=R(z_j)f_j,\qquad f_j\to f\text{ in }B,\\
 D^\alpha u_j\rightharpoonup^*D^\alpha u
                 \text{ in }B^*,\qquad|\alpha|\le m.
 \end{gathered}
 \tag{31}
\]

This graph decomposition is the eigenvalue remark following Hörmander [H4, Theorem 30.2.10].

**Theorem 9.1 (graph limit).** The set of these pairs is exactly

\[
 \begin{gathered}
 \{(g+R^\perp_\sigma(\lambda_0)f,f):
                         g\in Z_0,\ f\in B_\perp\}\\
 =(Z_0\times\{0\})
       +\operatorname{graph}(R^\perp_\sigma(\lambda_0)).
 \end{gathered}
 \tag{32}
\]

This assertion holds along every prescribed sequence \(z_j\) of the chosen sign.

**Proof of necessity.** Each coefficient \((u_j,\phi_\ell)\) converges, hence is bounded, by (31) and \(\phi_\ell\in B\). Therefore

\[
 \begin{gathered}
 (f_j,\phi_\ell)=(\lambda_0-z_j)(u_j,\phi_\ell)\longrightarrow0,\\
 (f,\phi_\ell)=0,\qquad f\in B_\perp.
 \end{gathered}
 \tag{33}
\]

The convergence of the forcing gives
\((I-\Pi)f_j\to f\) in \(B_\perp\), since \(\Pi:B\to B\) is bounded. By (30),
changing the reduced forcing from \((I-\Pi)f_j\) to \(f\) changes its solution by a quantity tending to zero in \(\mathcal Y_m\). Hence

\[
 \begin{gathered}
 (I-\Pi)u_j=R(z_j)(I-\Pi)f_j\\
       \rightharpoonup^*R^\perp_\sigma(\lambda_0)f\\
 \text{with every derivative}.
 \end{gathered}
 \tag{34}
\]

Meanwhile \(\Pi u_j\to\Pi u\) in \(\mathcal Y_m\), by its finite coefficient convergence. Take \(g=\Pi u\). This proves the required decomposition.

**Proof of sufficiency.** For any \(g\in Z_0\) and \(f\in B_\perp\), set

\[
 f_j=f+(\lambda_0-z_j)g.
 \tag{35}
\]

Since \(g\in B\), this tends to \(f\) in \(B\). The exact eigenvector identity gives

\[
 R(z_j)f_j=g+R(z_j)f.
 \tag{36}
\]

The reduced limiting absorption theorem yields the full derivative limit prescribed in (32). This proves sufficiency and the graph equality. \(\square\)

For a fixed forcing with \(\Pi f\ne0\), (29) displays the pole; a finite boundary value in \(B^*\) is impossible, since pairing with an appropriate \(\phi_\ell\) already diverges. In (35), the forcing's vanishing eigencomponent cancels that pole while leaving any specified finite eigenvector in the graph limit. This explains why the limit of graphs has more points than the graph of the reduced boundary operator alone.

### Use the conclusion

Check the reduced boundary value and the full graph description at an eigenvalue separately. For good energies retain the topology of every derivative limit and the sign in the spectral-measure formula.

<a id="lap-solutions"></a>

## 10. Graded exercises with complete solutions

**Exercise 1 — Basic — the strict weighted compactness threshold.**

Suppose \(u_j\) is bounded in \(\mathcal Y_m\) and its derivative graphs converge weak-star to those of \(u\). Prove \(u_j\to u\) in \(H^{0,-b}\) for every \(b>1/2\). Explain why the analogous claim at \(b=1/2\) does not follow from endpoint membership. Include the finite inner shell and justify local compactness.

**Solution 1.** On each fixed ball the derivative bounds give a common \(H^m\) bound. Apply a compact spatial cutoff on a larger ball. A frequency cutoff at \(L\) leaves an \(L^2\) remainder at most \(CL^{-m}\); for fixed \(L\), the low-frequency map between bounded supports has a square-integrable kernel and is a norm limit of finite-rank maps. Thus any local subsequence has an \(L^2\)-convergent further subsequence. Its limit must be \(u\) by distributional weak-star testing, so the whole sequence converges locally.

On every outer shell,

\[
 \begin{gathered}
 \|X^{-b}(u_j-u)\|_{L^2(A_k)}^2\\
       \le C_b R_k^{1-2b}
                 \sup_j\|u_j-u\|_{B^*}^2.
 \end{gathered}
 \tag{37}
\]

For \(b>1/2\), the summed outer tail is uniformly small. The finitely many remaining shells, including \(A_0\), lie in a fixed ball and are controlled by local convergence. This proves the result.

For the threshold, take the smooth function \(w=X^{-(n-1)/2}\). Its normalized shell masses are bounded above and below by positive constants for large shells; every derivative gains inverse powers of radius, so \(w\in\mathcal Y_m\) for each fixed \(m\). But

\[
 \begin{gathered}
 \|X^{-1/2}w\|_2^2\\
 \text{has a tail comparable to}\\
          \int_2^\infty r^{-1}\,dr=\infty.
 \end{gathered}
 \tag{38}
\]

This already shows failure of the target-space embedding. There is also a sequence whose terms all belong to the target space but do not converge in its norm. Choose nonzero \(\psi\in C_c^\infty(\{1<|x|<2\})\), let \(L_j=2^j\), and put \(w_j(x)=L_j^{-(n-1)/2}\psi(x/L_j)\). Its endpoint derivative norms are uniformly bounded, and its supports escape to infinity. Testing against the \(B\)-small tail of any \(B\) function proves that every derivative tends weak-star to zero. Each term has compact support, but a change of variables gives \(\|X^{-1/2}w_j\|_2^2\to\int |y|^{-1}|\psi(y)|^2\,dy>0\). Hence it does not converge in \(H^{0,-1/2}\). These examples test endpoint compactness alone; they impose no resolvent equation.

**Exercise 2 — Intermediate — signs and density for a first-order operator.**

On the line let \(H=D_x=-i\partial_x\), with no perturbation, and take \(f\in C_c^\infty(\mathbb R)\). Compute both boundary values at \(\lambda\), identify their nonzero tail directions, and calculate
\(\sigma\operatorname{Im}(R_\sigma(\lambda)f,f)/\pi\).
Show that, when the Fourier coefficient at \(\lambda\) is nonzero, the lower solution fails an upper radiation test.

**Solution 2.** The exact boundary formulas are

\[
 \begin{aligned}
 u_+(x)&=i\int_{-\infty}^{x}e^{i\lambda(x-s)}f(s)\,ds,\\
 u_-(x)&=-i\int_x^\infty e^{i\lambda(x-s)}f(s)\,ds.
 \end{aligned}
 \tag{39}
\]

Differentiating gives \((D_x-\lambda)u_\pm=f\), with the displayed signs. For a nonreal parameter in the appropriate half-plane, the same formulas have exponentially decaying kernels in their integration directions and Fourier multiplier \((\xi-z)^{-1}\); hence they are the Hilbert-space resolvents. Dominated convergence on bounded intervals and the common endpoint bound give their weak-star boundary limits.

Write \(F_\lambda=\int e^{-i\lambda s}f(s)\,ds\). Outside the support of \(f\), the upper solution is zero on the left and \(iF_\lambda e^{i\lambda x}\) on the right. The lower solution is \(-iF_\lambda e^{i\lambda x}\) on the left and zero on the right. Here \(v=1\), so \(N_+\) is the positive spatial ray at \(\xi=\lambda\) and \(N_-\) the negative ray.

Put
\[
 A=\int_{s<x}e^{i\lambda(x-s)}
                     f(s)\overline{f(x)}\,ds\,dx.
 \tag{40}
\]

The opposite triangle is its complex conjugate. The diagonal has measure zero, so \(|F_\lambda|^2=2\operatorname{Re}A\).
The pairings are \((u_+,f)=iA\) and \((u_-,f)=-i\overline A\). Therefore

\[
 \begin{gathered}
 \frac{\sigma}{\pi}\operatorname{Im}(u_\sigma,f)
       =\frac{|F_\lambda|^2}{2\pi}
       =|\widehat f(\lambda)|^2,\\
 \widehat f(\xi)=(2\pi)^{-1/2}
                   \int e^{-ix\xi}f(x)\,dx.
 \end{gathered}
 \tag{41}
\]

For a wrong-sign test, choose smooth \(k_-(x)\) equal one for \(x<-2\) and zero for \(x>-1\), and compact smooth \(\chi(\xi)=1\) near \(\lambda\). Then
\(h(x,\xi)=k_-(x)\chi(\xi)\) belongs to \(S(\Xi,G_1)\) and vanishes on \(N_+\).
The off-frequency function
\((1-\chi(D))u_-\) is Schwartz: its Fourier transform is
\((1-\chi(\xi))(\xi-\lambda)^{-1}\widehat f(\xi)\), which is smooth and rapidly decreasing. Thus
\(h(x,D)u_-\) has the same negative tail as \(k_-u_-\), up to a Schwartz error. On \(A_j\) the left interval has length \(R_j/2\), giving

\[
 R_j^{-1}\|h(x,D)u_-\|_{L^2(A_j)}^2
              \longrightarrow |F_\lambda|^2/2.
 \tag{42}
\]

If \(F_\lambda\ne0\), this output is not in \(\dot B^*\). The upper radiation condition thus rejects the lower solution. The free Fourier density in (41) confirms both the sign and the factor \(1/\pi\) in the general theorem.

**Exercise 3 — Intermediate — continuity without a fixed radiation bundle.**

Let \(\lambda_j\to\lambda\) in \(\Omega\), \(f_j\to f\) in \(B\), and fix one sign. Construct genuine nonreal resolvent graphs that prove the weak-star continuity of every derivative of \(R_\sigma(\lambda_j)f_j\). State where uniform boundedness and separability enter.

**Solution 3.** Choose a compact interval contained in \(\Omega\) around \(\lambda\). All sufficiently large \(\lambda_j\) lie there; the uniform estimate gives a common \(\mathcal Y_m\) bound for the boundary values and nearby nonreal resolvents. Separability of \(B\) gives tests \(\psi_1,\psi_2,\ldots\) with dense linear span.

At the fixed \(j\)-th energy, choose \(0<\eta_j<1/j\) so the nonreal value at \(z_j=\lambda_j+\sigma i\eta_j\) differs from the boundary value by less than \(1/j\) when paired against each of the first \(j\) tests, for each derivative through \(m\). This is possible by existence of the fixed-energy boundary limit. The uniform bound controls pairing with an arbitrary test after approximation by one of those finite tests; hence the two sequences differ weak-star by a quantity tending to zero.

The nonreal graphs have \(z_j\to\lambda\) and strong \(B\) forcing \(f_j\to f\). Lemma 2.2 proves that any extracted derivative limit solves the limiting equation and has radiation on \(N_\sigma(M_\lambda)\). Homogeneous uniqueness identifies it as \(R_\sigma(\lambda)f\). Bounded graph compactness and metrizability rule out a subsequence separated from that limit. Adding back the weak-star small approximation error proves the desired continuity.

Uniform boundedness is needed twice: for graph compactness and for extending convergence on the countable tests to every test in \(B\). The countable tests allow one nonreal approximation to meet all the first \(j\) requirements. No passage from radiation on \(N_\sigma(M_{\lambda_j})\) directly to radiation on \(N_\sigma(M_\lambda)\) has been assumed.

**Exercise 4 — Advanced — eigenprojection and graph limits.**

Let \(\lambda_0\) be a regular eigenvalue, \(Z_0=\ker(H-\lambda_0)\), and \(\Pi\) its projection. Prove that a limiting graph pair (31) must have \(\Pi f=0\), and that every pair in (32) occurs along any prescribed sequence \(z_j\to\lambda_0\) of the chosen sign. Explain why a fixed forcing with \(\Pi f\ne0\) has no finite weak-star boundary limit.

**Solution 4.** Every basis vector \(\phi_\ell\) has arbitrary polynomial Sobolev decay, so belongs to \(B\) and can test the weak-star limit. Hence \((u_j,\phi_\ell)\) converges. The eigenvalue pairing

\[
 (f_j,\phi_\ell)=(\lambda_0-z_j)(u_j,\phi_\ell)
 \tag{43}
\]

tends to zero. Strong \(B\) convergence also makes its left side tend to \((f,\phi_\ell)\), proving \(\Pi f=0\).

The projection is bounded on \(B\), so \((I-\Pi)f_j\to f\) in \(B_\perp\). The reduced estimate and its boundary limit yield
\((I-\Pi)u_j\rightharpoonup^*R^\perp_\sigma(\lambda_0)f\) with all derivatives. The finite projection part converges in \(\mathcal Y_m\) to \(g=\Pi u\), since its finitely many coefficients converge. This proves necessity in (32).

Conversely, for any \(g\in Z_0\) and \(f\in B_\perp\), put
\(f_j=f+(\lambda_0-z_j)g\). The decay of \(g\) puts it in \(B\), so this forcing tends strongly to \(f\). The exact resolvent identity on an eigenvector gives
\(R(z_j)f_j=g+R(z_j)f\), whose derivative limit is the required pair. This construction works for either sign and for every prescribed sequence.

For fixed \(\Pi f\ne0\), at least one coefficient \((f,\phi_\ell)\) is nonzero. Its solution coefficient is
\((\lambda_0-z)^{-1}(f,\phi_\ell)\), which has unbounded modulus as \(z\to\lambda_0\). Since \(\phi_\ell\in B\), this alone rules out a finite weak-star \(B^*\) limit. For example \(z_j=\lambda_0+i/j\) in the construction above gives \(f_j=f-i g/j\), explicitly cancelling the upper pole.

**Exercise 5 — Advanced — the spectral atom and continuous reduced density.**

Take a small interval \(I\) about a regular eigenvalue \(\lambda_0\), with no other eigenvalue or critical free energy there. For \(f\in B\), prove that its spectral measure on \(I\) is

\[
 \begin{gathered}
 \mu_f|_I=\|\Pi f\|_2^2\,\delta_{\lambda_0}
                    +q^\perp_f(\lambda)\,d\lambda,\\
 q^\perp_f(\lambda)=\frac{\sigma}{\pi}
       \operatorname{Im}
       (R^\perp_\sigma(\lambda)(I-\Pi)f,(I-\Pi)f).
 \end{gathered}
 \tag{44}
\]

Show that the density is continuous and nonnegative even at \(\lambda_0\), and that its expression is independent of the chosen sign.

**Solution 5.** The general spectral theorem identifies
\(\Pi=E(\{\lambda_0\})\). Indeed the second-moment domain formula gives, for an eigenvector \(g\),

\[
 \|(H-\lambda_0)g\|_2^2
       =\int|t-\lambda_0|^2\,d\mu_g(t)=0,
 \tag{45}
\]

so its spectral measure is supported on \(\{\lambda_0\}\). Conversely a vector in \(E(\{\lambda_0\})L^2\) has finite second moment and satisfies the eigenvalue equation. This proves equality of the two ranges and hence of the orthogonal projections.

Projection-valued measure multiplication shows that \(E(A)\) preserves both ranges of \(\Pi\) and \(I-\Pi\). The cross pairings therefore vanish. For \(f_\perp=(I-\Pi)f\) we get

\[
 \mu_f=\|\Pi f\|_2^2\delta_{\lambda_0}+\mu_{f_\perp}.
 \tag{46}
\]

Here \(f_\perp\in B_\perp\), since the eigenbasis belongs to \(B\) and \(\Pi:B\to B\) is bounded.

Apply (22) and the continuous-test Poisson proof to \(f_\perp\) and any \(\chi\in C_c(I)\). The reduced estimate (30) bounds its scalar resolvent pairing uniformly, including near \(\lambda_0\). Reduced boundary continuity gives pointwise convergence everywhere on \(I\). Dominated convergence proves

\[
 \int\chi\,d\mu_{f_\perp}
       =\int_I\chi(\lambda)q^\perp_f(\lambda)\,d\lambda.
 \tag{47}
\]

The continuous-test measure-identification proof in Section 7, applied inside \(I\), shows that \(\mu_{f_\perp}|_I\) has the claimed density. The reduced pairing is continuous on the entire interval; its signed imaginary part is nonnegative by (22) and its pointwise boundary limit. Both signs give the same measure in (47). The same local sign argument for continuous densities proves equality everywhere, including at the center. Combining (46) and (47) proves (44).

At \(\lambda_0\), the missing atom is precisely the part that a density formed from an unrestricted finite boundary value could not represent. The reduced boundary value recovers the continuous part while the eigenspace projection gives the atom.

## 11. What follows

The full rough long-range boundary theorem is now available, including its eigenvalue graph remark. The next part of long-range scattering constructs the Hamilton trajectories and phases needed for modified wave operators. Those constructions require the stated stronger smoothness of the long-range part; the \(1\)-admissible hypothesis used here is not silently upgraded. The general spectral theorem remains an explicitly named prerequisite of the spectral formula.

### Accessible scalar comparisons and their proof limits

Ito–Skibsted [IS] treats \(H=-\tfrac12\Delta+V+q\) on \(\mathbb R^d\), \(d\ge2\), with real scalar multiplication potentials and no positive eigenvalues. Its Condition 1.1 assumes \(V\in C^l\), \(\sigma\in(0,1)\), \(\rho\in(0,1]\), and

\[
 |\partial^\alpha V(x)|\le C_\alpha X^{-m(|\alpha|)},
 \quad m(k)=\begin{cases}
 \sigma+k,&k=0,1,2,\\
 \sigma+2+(\rho+1)(k-2)/2,&k\ge2.
 \end{cases}
\]

It permits a measurable real \(q\) for which
\(X^{1+\tau}q(-\Delta+1)^{-1}\) is compact on \(L^2\), for some \(\tau\in(0,1)\). The strong radiation result, Theorem 1.23, additionally requires \(l=4\) and \(q=0\). With its eikonal phase \(S\), cutoff phase \(\chi_1S\), radiation derivatives
\(\gamma=p\mp\nabla(\chi_1S)\) and
\(\gamma_\parallel=\operatorname{Re}(\nabla(\chi_1S)\cdot\gamma)\), it gives, locally uniformly at positive energies,

\[
 \begin{aligned}
 \gamma_\parallel R(\lambda\pm i0),\ \gamma_i\gamma_jR(\lambda\pm i0)
 &:L^2_{\beta+1/2}\longrightarrow L^2_{\beta-1/2},
 &&0<\beta<\beta_c,\\
 \gamma_iR(\lambda\pm i0)
 &:L^2_{\beta'+t}\longrightarrow L^2_{\beta'-t},
 &&0<\beta'<\beta_c/2,\quad t>1/2,
 \end{aligned}
 \qquad \beta_c=\min(2,1+\sigma+\rho).
\]

These are additional quantitative scalar radiation estimates with a specified weight range. The proof in §§3.3–3.6 constructs bounded distance weights, expands a distorted commutator, exchanges its quartic and parallel forms, absorbs the lower-order errors, takes the spectral limit before the weight limit, and obtains the first-derivative estimate by interpolation. Its last estimates use Theorem 3.17, which imports LAP from Adachi–Itakura–Ito–Skibsted [AIIS2]. Remark 3.16 states a \(C^3\) variant with a modified nonsymmetric parallel observable and critical exponent \(1+\sigma\); it explicitly omits the remaining details. Proposition 4.14, under \(l=2\), regularizes \(V\), uses the second resolvent identity and radial flux to put the homogeneous remainder in \(B^*_0\); the final vanishing invokes [AIIS2], Theorem 1.4. Thus those two imported proofs remain dependencies of this comparison, and the \(C^3\) remark is not a complete proof provider. The source does not supply the full polynomial or rough differential construction of Sections 2–9, the arbitrary-weight bootstrap, or the reduced eigenvalue graph.

Yafaev [Y], §3, concerns \(H=-\Delta+v\) with real scalar \(v\) and
\(|\partial^\alpha v|\le C_\alpha X^{-\rho-|\alpha|}\), \(\rho>0\), \(|\alpha|\le1\). Equation (3.5) is the dilation Mourre estimate on a sufficiently small positive-energy interval. Its consequence is continuous weighted \(L^2\) resolvent boundary values with weight \(r>1/2\), away from eigenvalues. The lectures state the passage from that commutator estimate to the limiting absorption principle without proving it. This gives a scalar operator-norm comparison, without replacing the endpoint, every-derivative or eigenvalue-reduction proof here.

Isozaki [I], §2, Lemmas 2.4–2.6, concerns \(H=-\Delta+V\), real \(V\in C^3\), with
\(\partial^\alpha V=O(|x|^{-\delta-|\alpha|})\), \(0\le|\alpha|\le3\), at positive energy. Its proof differentiates a spherical radiation pairing, solves the resulting oscillatory first-order equation by an integrating factor, and uses a Green identity to recover the norm flux. Earlier LAP and radiation estimates are imported. This scalar argument illustrates the radial-flux mechanism. The [full radial identity, sharp shell passage and all derivative tails](outgoing-flux-and-vanishing-shell-mass.md#flux-radial-identity) used here are proved for the polynomial differential operator in the preceding flux lesson.

The result-level roles in the five long-range lessons are therefore explicit:

| Lesson | What the scalar comparisons contribute | Full-scope construction retained here |
| --- | --- | --- |
| Combining the estimates | A comparison with a distorted-commutator programme that already assumes LAP | The two rough short-range maps, actual domain forcing, finite full-order errors and compact-error absorption |
| Radiation for graph limits | Quantitative eikonal radiation derivatives in the scalar case | Every symbol vanishing on the exact polynomial normal bundle, its collar limit and the complete rough derivative graph |
| Outgoing flux | The radial-flux mechanism of [IS], Proposition 4.14, and [I], Lemmas 2.4–2.6 | The velocity-normalized symbol identity, rough real pairing, both signs and vanishing tails through order \(m\) |
| Weighted decay | The finite range \(\beta<\beta_c\) of the scalar strong-radiation estimates | The bounded-weight frame, absorption and finite bootstrap to every polynomial weight |
| Limiting absorption | Scalar positive-energy weighted \(L^2\) boundary estimates | Every regular polynomial energy, including an empty shell, both endpoint boundary values and the full reduced eigenvalue graph |

## References

[A] Shmuel Agmon, notes by Karl Gustafson, reworked by Michael Taylor, [*Limiting Absorption Principle for Long Range Potentials*](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2020/08/AGMON.pdf), lectures of 17–21 July 1978, §5, Theorem 5.A and Lemma 5.B, supplies the freely readable compactness/radiation/uniqueness construction. Its introduction only remarks on an eigenvalue reduction. Sections 8–9 above prove that reduction and the complete every-sequence graph description; Section 6 proves continuity with a varying radiation bundle through genuine nonreal approximants. The preceding lessons prove the rough differential and weighted bridges required by Sections 2–5, rather than importing the transcription's unproved Proposition 3.F.


[T] Gerald Teschl, [*Mathematical Methods in Quantum Mechanics*, second online edition](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf), §3.1, Theorems 3.1–3.2 and 3.6, printed pp. 102–109, gives the bounded Borel calculus, exact second-moment domain and general self-adjoint spectral measure. In its scalar product convention the linear entry is second; exchanging the entries gives precisely (22) in our convention. Section 7 supplies the complete continuous-test Poisson passage used here. No spectral lower bound is imposed.

[IS] Kenichi Ito and Erik Skibsted, [*Scattering theory for \(C^2\) long-range potentials*, arXiv:2408.02979v1](https://arxiv.org/pdf/2408.02979v1), submitted 6 August 2024, PDF dated 7 August 2024. The exact compared results are Condition 1.1, Theorem 1.23, §§3.3–3.6 and Proposition 4.14. Its reference label [AIIS2] denotes the work for which the free author preprint is cited next.

[AIIS2] T. Adachi, K. Itakura, K. Ito and E. Skibsted, [*New methods in spectral theory of N-body Schrödinger operators*, arXiv:1804.07874v1](https://arxiv.org/pdf/1804.07874v1), submitted 21 April 2018, PDF dated 24 April 2018. This is the freely accessible author version. Its Rellich statements are Theorems 1.4–1.5 and its LAP bound is Theorem 1.7. The reference to “Theorem 1.4” in the comparison above reports [IS]'s own dependency locator; numbering and statements must be checked in the version actually used. None of these external results is a substitute for the programme proofs in Sections 2–9.

[Y] Dmitri Yafaev, [*Lectures on scattering theory*, arXiv:math/0403213v1](https://arxiv.org/pdf/math/0403213v1), submitted 12 March 2004, §3, especially equation (3.5) and its LAP discussion. The lectures cite external proofs for that implication.

[I] Hiroshi Isozaki, [*Eikonal equations and spectral representations for long-range Schrödinger Hamiltonians*, author-uploaded text](https://www.researchgate.net/publication/258235181_Eikonal_equations_and_spectral_representations_for_long-range_Schrodinger_Hamiltonians), J. Math. Kyoto Univ. 20(2) (1980), 243–261, §2, Lemmas 2.4–2.6. The spherical radiation pairing and Green identity give a scalar comparison with the polynomial flux argument.

[H4] Lars Hörmander, *The Analysis of Linear Partial Differential Operators IV: Fourier Integral Operators*, reprint of the 1994 edition, Springer, 2009, Theorem 30.2.10, formulas (30.2.30)–(30.2.31), its proof and the following eigenvalue graph remark, pp. 295–296. ISBN 978-3-642-00136-9. [Edition information](https://doi.org/10.1007/978-3-642-00136-9).
