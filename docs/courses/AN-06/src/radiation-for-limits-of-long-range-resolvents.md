# Radiation for limits of long-range resolvents

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*


**Working question: Which directional information survives a resolvent graph limit?** Weak endpoint bounds permit persistent shell mass, so they do not by themselves select an outgoing wave. Symbols vanishing on the outgoing normal bundle test the unwanted directions. Their action lies in the vanishing-tail space after the graph limit, providing a radiation statement compatible with the full-order rough perturbation.

An outgoing wave can retain a nonzero amount of mass per unit radius. Its direction, rather than decay of the whole wave, distinguishes an upper resolvent boundary value. We prove this directional statement for a limit of resolvent graphs: every smooth operator whose symbol vanishes on the outgoing free normal bundle sends the limit into the vanishing shell space. The perturbation can have the full differential order and rough, unbounded lower coefficients.

Use [Admissible differential perturbations](admissible-differential-perturbations.md), [The Sobolev domain of an elliptic operator](the-sobolev-domain-of-an-elliptic-operator.md), and [Weighted Sobolev spaces and rough elliptic estimates](weighted-sobolev-spaces-and-rough-elliptic-estimates.md) for the coefficient class, realization and weighted maps. The two frequency estimates are [The resolvent away from the energy surface](the-resolvent-away-from-the-energy-surface.md) and [A resolvent estimate at noncritical frequencies](a-resolvent-estimate-at-noncritical-frequencies.md). [Combining the long-range resolvent estimates](combining-the-long-range-resolvent-estimates.md) proves both rough short-range maps. [Endpoint spaces and flat energy shells](endpoint-spaces-and-flat-energy-shells.md) gives the integral endpoint duality. Agmon [A] supplies the freely readable directional-radiation construction; Sections 5–8 prove its weighted and exact-bundle extensions. The self-adjoint resolvent input is proved in the earlier programme lessons; Teschl [T] provides a freely accessible comparison.

Write \(D=-i\partial\), \(X=\langle x\rangle\), \(\Xi=\langle\xi\rangle\), and
\(\|w\|_{s,t}=\|X^t\langle D\rangle^s w\|_2\).
The position metric and its symbol convention are

\[
 \begin{gathered}
G_\vartheta=X^{-2\vartheta}|dx|^2+\Xi^{-2}|d\xi|^2,\\
 h\in S(\Xi^m,G_1)
 \ \Longleftrightarrow\
 \\
|\partial_x^\alpha\partial_\xi^\beta h|
       \le C_{\alpha\beta}X^{-|\alpha|}\Xi^{m-|\beta|}.
 \end{gathered}
 \tag{1}
\]

We use left quantization and an inner product linear in the first entry.

The operative calculus is [Finite composition and adjoints with spatial weights](../providers/analysis/finite-weighted-calculus.md), including its finite remainders and weighted mapping proof. [Weighted positivity from Gaussian packets](../providers/analysis/weighted-positivity.md) proves the two positivity and norm inputs used below. Free external references supply construction material and comparisons; they do not replace those programme arguments.

## 1. The outgoing bundle and the graph limit

Use the shells \(A_0=\{|x|<1\}\), \(A_j=\{2^{j-1}\le|x|<2^j\}\), \(R_j=2^j\), and

\[
 \begin{aligned}
 \|f\|_B&=\sum_{j\ge0}R_j^{1/2}\|f\|_{L^2(A_j)},\\
 \|w\|_{B^*}&=\sup_{j\ge0}R_j^{-1/2}\|w\|_{L^2(A_j)}.
 \end{aligned}
 \tag{2}
\]

Let \(P_0(D)\) be real, scalar, constant-coefficient and elliptic of order \(m\ge1\). Let \(V\) be a symmetric \(1\)-admissible perturbation. Its self-adjoint realization \(H=P_0+V\) has domain \(H^m\). For a regular free energy \(\lambda\), put

\[
 \begin{gathered}
 M_\lambda=\{\xi:P_0(\xi)=\lambda\},\qquad
 v(\xi)=\nabla P_0(\xi),\\
 N_+(M_\lambda)
   =\{(t\,v(\xi),\xi):\xi\in M_\lambda,\ t>0\}.
 \end{gathered}
 \tag{3}
\]

Regular means \(\lambda\notin\{P_0(\xi):v(\xi)=0\}\). Ellipticity makes \(M_\lambda\) compact. The bundle in (3) records the positive spatial ray at each velocity. Denote the closure of Schwartz space in \(B^*\) by \(\dot B^*\).

<a id="radiation-theorem"></a>
The graph-limit radiation statement is Hörmander [H4, Theorem 30.2.6].

**Theorem 1.1.** Suppose

\[
 \begin{gathered}
 \operatorname{Im}z_j>0,\qquad z_j\longrightarrow\lambda,\\
 u_j=(H-z_j)^{-1}f_j,\qquad f_j\longrightarrow f\text{ in }B,\\
 D^\alpha u_j\rightharpoonup^*D^\alpha u
       \text{ in }B^*,\qquad |\alpha|\le m.
 \end{gathered}
 \tag{4}
\]

Then \((H-\lambda)u=f\) as a distribution, with the actual local coefficient products. For every symbol

\[
 \begin{gathered}
 h\in S(\Xi^m,G_1),\qquad h|_{N_+(M_\lambda)}=0,\\
 h(x,D)u\in\dot B^*.
 \end{gathered}
 \tag{5}
\]

The theorem includes dimension one, an empty free shell, and perturbed eigenvalues. Its assumptions concern a convergent graph. The outgoing component may carry nonzero shell mass; Exercise 3 exhibits this explicitly.

## 2. What vanishing shell mass means

<a id="radiation-shell-closure"></a>
**Lemma 2.1.** For \(w\in B^*\), the following conditions are equivalent:

\[
 \begin{gathered}
 w\in\dot B^*,\\
 R_j^{-1}\|w\|_{L^2(A_j)}^2\longrightarrow0,\\
 R^{-1}\int_{|x|<R}|w(x)|^2\,dx\longrightarrow0.
 \end{gathered}
 \tag{6}
\]

**Proof.** Schwartz functions have vanishing normalized shell norms. Approximation in \(B^*\), followed by the shell triangle inequality, gives the second condition for every element of their closure.

Conversely, truncate \(w\) inside \(|x|<R_J\). Its endpoint error is the supremum of the normalized norms on shells \(j>J\), which tends to zero. The truncated function has bounded support and belongs to \(L^2\). Approximate it in \(L^2\) by compact smooth functions, and use \(\|g\|_{B^*}\le\|g\|_2\). This proves the closure assertion.

Put \(q_j=R_j^{-1}\|w\|_{L^2(A_j)}^2\). At a dyadic radius,

\[
 R_J^{-1}\int_{|x|<R_J}|w|^2
       =\sum_{j=0}^J2^{j-J}q_j.
 \tag{7}
\]

If \(q_j\to0\), the finite early part tends to zero and the remaining geometric sum is as small as desired. Neighboring dyadic radii control every real radius, with a factor at most two. In the reverse direction, each shell mass is bounded by the corresponding ball mass. This proves all three conditions, including the inner shell. \(\square\)

A bounded \(B^*\) operator that carries Schwartz space into \(\dot B^*\) preserves this closure. In particular, the smooth order-zero shell maps in the near-frequency lesson preserve \(\dot B^*\).

The full-order action in (5) is finite before any vanishing argument. Indeed,

\[
 \begin{gathered}
 S_m(\xi)=\sum_{|\alpha|\le m}\xi^{2\alpha}
               \asymp\Xi^{2m},\\
 h(x,\xi)=\sum_{|\alpha|\le m}
       \frac{h(x,\xi)\xi^\alpha}{S_m(\xi)}\,\xi^\alpha.
 \end{gathered}
 \tag{8}
\]

Every fraction is in \(S(1,G_1)\). Right composition with \(D^\alpha\) is exact for left quantization. The shell interface therefore bounds \(\|h(x,D)u\|_{B^*}\) by a constant times \(\sum_{|\alpha|\le m}\|D^\alpha u\|_{B^*}\). The common distributional action agrees with this finite sum.

## 3. Strong weighted convergence of the graph

**Lemma 3.1.** Under (4), for every \(b>1/2\),

\[
 u_j\longrightarrow u\quad\text{in }H^{m,-b}.
 \tag{9}
\]

Choose the symmetric split \(V=V_L+V_S\) from the combined-estimate lesson, including its compact adjustment making \(P_0+V_L\) elliptic. Fix \(0<\delta\le1\) within the available decay gaps, and put \(d=1+\delta\). If \(b<1/2+\delta\), then also \(V_Su_j\to V_Su\) in \(B\).

<a id="radiation-uniform-bounds"></a>
**Proof.** We first prove the boundedness consequence of weak-star convergence. The endpoint lesson proves that \(B\) is Banach and that its integral dual norm is exactly the \(B^*\) norm. For a fixed derivative let \(F_j(g)=(g,D^\alpha u_j)\). These bounded linear functionals are pointwise bounded by (4). Put

\[
 E_k=\{g\in B:\sup_j|F_j(g)|\le k\},\qquad k\ge1.
\]

The sets are closed and cover \(B\). Some \(E_k\) contains an open ball: otherwise, starting in any open ball, successively choose a closed ball of positive radius at most \(2^{-k}\), inside the preceding ball's interior and disjoint from \(E_k\). Such a choice is possible because a closed set with empty interior leaves a nonempty open part of every open ball. The centers are Cauchy, and completeness supplies a point in all the nested closed balls. That point belongs to none of the \(E_k\), a contradiction. If \(B(g_0,r)\subset E_k\), then for every \(\|g\|_B\le1\), both \(g_0\) and \(g_0+(r/2)g\) lie in \(E_k\). Subtraction gives \(|F_j(g)|\le4k/r\). Exact endpoint duality now gives a bound for \(\|D^\alpha u_j\|_{B^*}\) independent of \(j\). There are only finitely many derivatives through \(m\), so their bounds can be combined. This is the full completeness argument, compared with the free proofs in Teschl [T], Theorems 0.38–0.39.

The [strict endpoint embedding](combining-the-long-range-resolvent-estimates.md#combined-embeddings) \(B^*\subset H^{0,-b}\) and the [integer derivative characterization](weighted-sobolev-spaces-and-rough-elliptic-estimates.md#weighted-integer-derivatives) give \(u_j,u\in H^{m,-b}\), uniformly.

<a id="radiation-local-compactness"></a>
On each compact set the sequence is bounded in \(H^m\). Here is its local compactness. After input and output compact cutoffs, a smooth Fourier cutoff at frequency \(L\) leaves an \(L^2\) remainder bounded by \(CL^{-m}\) times the input \(H^m\) norm. For fixed \(L\) the low-frequency map between the bounded supports has a square-integrable kernel. Approximate that kernel by finite sums of products of \(L^2\) functions, using the rectangular simple-function density proved in the [Euclidean measure reading](../providers/analysis/finite-derivative-l2.md#euclidean-products). Cauchy–Schwarz bounds the operator error by the kernel's \(L^2\) error. The low-frequency map is therefore a norm limit of finite-rank maps. To see compactness explicitly, choose such approximations with errors tending to zero, successively extract convergent subsequences of their finite-dimensional images of this bounded sequence, and take the diagonal subsequence. The operator errors make its exact images Cauchy. Combining this with the \(CL^{-m}\) high-frequency error proves local \(L^2\) precompactness. Every subsequential limit has distributional limit \(u\), by (4). If local convergence of the whole sequence failed, a subsequence separated from \(u\) by a fixed positive norm would have a further convergent subsequence, contradicting that unique limit. Thus the entire sequence converges locally.

The endpoint bound makes its weighted tail uniformly small:

\[
 \begin{aligned}
 \|1_{\{|x|>R\}}X^{-b}(u_j-u)\|_2^2
 &\le C\sup_j\|u_j-u\|_{B^*}^2\\
 &\quad\cdot\sum_{R_k\gtrsim R}R_k^{1-2b}.
 \end{aligned}
 \tag{10}
\]

First choose \(R\), then use local convergence on its interior. This proves strong convergence in \(H^{0,-b}\).

<a id="radiation-rough-graph"></a>
All derivatives converge weakly in local \(L^2\): compactly supported \(L^2\) tests belong to \(B\). After multiplication by a compact smooth cutoff, these finitely many weak derivative limits give weak convergence in \(H^m\), by its integer derivative norm. The [local coefficient multiplier](admissible-differential-perturbations.md#admissible-global-mapping) maps \(H^m\to L^2\) continuously after compact cutoffs, even for unbounded lower coefficients. Its weak continuity identifies the limit of \((H-\lambda)u_j\) with \((H-\lambda)u\). The equations and \(f_j\to f\) identify this limit as \(f\).

We must now extend the graph inequality to an input already known in weighted \(H^m\). The [rough graph theorem](weighted-sobolev-spaces-and-rough-elliptic-estimates.md#weighted-rough-graph-proof) is initially stated on the unweighted domain. For each real \(t\), \(P_0\) maps \(H^{m,t}\to H^{0,t}\); \(V_L\) maps to \(H^{0,t+\delta}\); the [primary rough map](combining-the-long-range-resolvent-estimates.md#combined-primary-map) sends \(V_S\) to \(H^{0,t+d}\). These larger output weights embed into \(H^{0,t}\). Thus the full expression is bounded \(H^{m,t}\to H^{0,t}\), with its actual differential action.

Approximate an already known \(w\in H^{m,t}\) by Schwartz functions in that space. Their images converge in \(H^{0,t}\). Apply the unweighted-domain graph inequality to each approximant and pass to the limit:

\[
 \|w\|_{m,t}
 \le C_t\bigl(\|(H-\lambda)w\|_{0,t}
                  +\|w\|_{0,t}\bigr).
 \tag{11}
\]

This proves an inequality on known weighted inputs. Apply it to \(w_j=u_j-u\), whose weighted membership was already established. Since

\[
 (H-\lambda)w_j=f_j-f+(z_j-\lambda)u_j,
 \tag{12}
\]

both right-side norms in (11) at \(t=-b\) tend to zero. This proves (9). Finally the primary rough map gives

\[
 \|V_S(u_j-u)\|_{0,d-b}
       \le C_b\|u_j-u\|_{m,-b}\longrightarrow0.
 \tag{13}
\]

If \(b<1/2+\delta\), then \(d-b>1/2\), and the strict weighted embedding puts this convergence in \(B\). \(\square\)

Consequently the entire smooth forcing \(f_{0,j}=f_j-V_Su_j\) converges to \(f_0=f-V_Su\) in \(B\). Fix

\[
 \begin{gathered}
 0<\gamma<\delta/2,\qquad a=(1+\delta)/2,\\
 b=a-\gamma>1/2,\qquad
 \|u_j-u\|_{0,\gamma-a}\longrightarrow0.
 \end{gathered}
 \tag{14}
\]

All auxiliary norms used below are finite before passing to the graph limit.

<a id="radiation-off-energy"></a>
## 4. Removing the off-energy frequencies

The inclusion \(B\subset H^{0,1/2}\) follows by bounding its weighted shell \(\ell^2\) norm by the defining \(\ell^1\) norm. The rough map gives \(V_Su\in H^{0,d-b}\) with \(d-b>1/2\). Thus \(f_0\in H^{0,1/2}\).

Choose real compact smooth \(\chi\), equal one near \(M_\lambda\), supported where \(v\ne0\). The off-energy theorem applies at the real parameter \(\lambda\) to \((P_0+V_L-\lambda)u=f_0\):

\[
 \begin{gathered}
 (1-\chi(D)^2)u\in H^{m,1/2},\\
 h(x,D)(1-\chi(D)^2)u
       \in H^{0,1/2}\subset L^2\subset\dot B^*.
 \end{gathered}
 \tag{15}
\]

It remains to study \(h(x,D)\chi(D)^2u\). Its exact left symbol \(h(x,\xi)\chi(\xi)^2\) has compact frequency support and is in \(S(1,G_1)\). If the free shell is empty, take \(\chi=0\); (15) proves the whole conclusion.

## 5. A smooth escape multiplier outside every fixed ball

Choose smooth even \(\rho_0,\rho_1,\rho_2\), values in \([0,1]\), decreasing on the positive half-line, with successively nested small supports in \((-1/2,1/2)\). Require \(\rho_0(0)=1\), its derivative strictly negative on some positive open interval, \(\rho_1=1\) near \(\operatorname{supp}\rho_0\), and \(\rho_2=1\) near \(\operatorname{supp}\rho_1\). Their final support can be as close to zero as needed. For \(w,y\ne0\), put

\[
 c_\ell(w,y)=
   \rho_\ell\left(1-\frac{w\cdot y}{|w||y|}\right).
 \tag{16}
\]

Choose radial \(\psi\ge0\), supported in \(1/2<|w|<5/2\), positive on \(3/4\le|w|\le9/4\). Set

\[
 \begin{aligned}
 \psi_1(w,y)&=(1-c_1(w,-y))\psi(w),\\
 \Psi(x,y)&=\int\psi_1(x-z,y)c_0(z,y)\,dz.
 \end{aligned}
 \tag{17}
\]

<a id="radiation-angular-escape"></a>
**Lemma 5.1.** For some fixed \(c>0\), \(\Psi=0\) on \(|x|<c\). It is smooth for \(y\ne0\), homogeneous of degree zero in \(y\), and

\[
 |\partial_x^\alpha\partial_y^\beta\Psi|
       \le C_{\alpha\beta}X^{-|\alpha|}|y|^{-|\beta|}.
 \tag{18}
\]

Moreover,

\[
 \begin{gathered}
\Psi'=y\cdot\partial_x\Psi\ge0,
 \\
 \Psi,\Psi'>0\text{ where }\psi_1>0.
 \end{gathered}
 \tag{19}
\]

**Proof.** For bounded \(x\), put position derivatives on \(\psi_1(x-z,y)\). Direction derivatives of \(c_0\) are bounded by \(C|y|^{-|\beta|}\), uniformly as \(z\to0\); its degree in \(z\) is zero. Differentiation under the compact integral proves smoothness and the bounded-region estimates. For \(|x|\ge5\), use \(\int\psi_1(w,y)c_0(x-w,y)\,dw\). Now \(|x-w|\asymp|x|\), and homogeneity gives all mixed bounds.

The averaging cone of \(c_0(z,y)\) points along \(y\). The annular support of \(\psi_1(w,y)\) excludes a strictly larger cone about \(-y\). Thus \(w+z\) cannot be zero on these supports. Restrict \(|y|=1\) and \(|w+z|\le1\); then \(|z|\le7/2\). The resulting joint closed support is compact and separated from \(w+z=0\). Its positive distance proves the exterior zero region uniformly in \(y\).

For \(n\ge2\), \(y\cdot\partial_z c_0\) is nonnegative, bounded by \(C|y|/|z|\), and locally integrable. The boundary term at a puncture of radius \(\varepsilon\) is \(O(|y|\varepsilon^{n-1})\), so this is its distributional derivative. Integrating it against \(\psi_1(x-z,y)\) gives (19). Where \(\psi_1(x,y)>0\), small \(z\) in the angular transition cone give strict positivity of \(\Psi'\); small \(z\) in the inner cone give strict positivity of \(\Psi\).

For \(n=1\), \(c_0(z,y)=1_{\{zy>0\}}\) and \(\psi_1(w,y)=\psi(w)1_{\{wy>0\}}\). Hence

\[
 \Psi'(x,y)=|y|\psi_1(x,y).
 \tag{20}
\]

The half-line integral is positive where \(\psi_1>0\). Both summands \(w,z\) have the sign of \(y\), so their sum is separated from zero by the annular support of \(w\). The same bounds hold on each component \(y\ne0\). \(\square\)

Choose radial smooth \(\omega\), supported strictly inside \(3/4<|x|<9/4\), equal one on \(1\le|x|\le2\), with values in \([0,1]\). Put

\[
 \phi_1(x,y)=k(1-c_2(x,-y))\omega(x).
 \tag{21}
\]

Its closed support lies where \(c_1(x,-y)=0\) and \(\psi>0\). On that support and \(|y|=1\), the positive continuous product \(\Psi\Psi'/|y|\) has a minimum \(\mu>0\). Let \(\nu=\min_{\operatorname{supp}\chi}|v|>0\). Choose \(k^2\le\nu\mu\). Homogeneity gives

\[
 \begin{gathered}
|\phi_1(x,-v(\xi))|^2
 \\
\le \Psi(x,-v(\xi))\Psi'(x,-v(\xi))
       \\
\quad(\xi\in\operatorname{supp}\chi).
 \end{gathered}
 \tag{22}
\]

This choice retains every positive minimum velocity. For \(R\ge1\), define

\[
 \begin{aligned}
 q_R(x,\xi)&=\Psi(x/R,-v(\xi))\chi(\xi),\\
 \Phi_R(x,\xi)&=\phi_1(x/R,-v(\xi))\chi(\xi).
 \end{aligned}
 \tag{23}
\]

<a id="radiation-scaled-escape"></a>
Both are uniformly in \(S(1,G_1)\), with compact frequency support. The first is zero for \(|x|<cR\); the second has annular output support. The transport calculation gives

\[
 s_R=-q_R\,v\cdot\partial_xq_R-R^{-1}\Phi_R^2\ge0.
 \tag{24}
\]

It is uniformly in \(S(X^{-1},G_1)\) and zero inside a fixed multiple of \(R\).

<a id="radiation-weighted-positivity"></a>
## 6. The weighted commutator and its graph limit

For the positive exponent \(\gamma\) fixed in (14), exterior support permits exchange of a radius factor for a spatial weight, with all differentiated bounds:

\[
 \begin{aligned}
 R^\gamma q_R&\in S(X^\gamma,G_1),\\
 R^{\gamma-1/2}\Phi_R&\in S(X^{\gamma-1/2},G_1),\\
 R^{2\gamma}s_R&\in S(X^{2\gamma-1},G_1).
 \end{aligned}
 \tag{25}
\]

All families are bounded uniformly in \(R\). Exact Fourier conjugation sends the last symbol to a right symbol \(b_R(y,\eta)=R^{2\gamma}s_R(-\eta,y)\). Its adjoint has left quantization of the same real symbol. The symbol \(b_R\) is nonnegative and uniformly in the classical class \(S^{2\gamma-1}_{1,0}\): a new frequency derivative is an old position derivative and lowers that order by one, while every new position derivative is bounded by the old frequency estimates.

For any fixed real \(\gamma\), the following reduction to the programme's [proved packet positivity, Theorem 1](../providers/analysis/weighted-positivity.md#weighted-positivity) applies to a nonnegative family \(c_R\) uniformly in \(S(X^{2\gamma-1},G_1)\). In the present application set \(c_R=R^{2\gamma}s_R\); (25) verifies that hypothesis for the positive \(\gamma\) chosen in (14). Put \(a_R=X^{-2\gamma}c_R\). The latter is nonnegative and uniformly in \(S(X^{-1},G_1)\), with precisely the derivative bounds (P1) of that theorem. Write \(M_\gamma=X^\gamma\). The [finite first product and all-real weighted mapping proof](../providers/analysis/finite-weighted-calculus.md#finite-composition) give

\[
 M_\gamma\operatorname{Op}(a_R)M_\gamma
 =\operatorname{Op}(c_R)+T_R,
 \qquad T_R\in\operatorname{Op}S(X^{2\gamma-2},G_1).
\]

All seminorms are uniform in \(R\). Indeed the right product's leading symbol is \(a_RX^\gamma\); its remainder has weight \(X^{\gamma-2}\Xi^{-1}\), because one frequency derivative and one position derivative occur. Left multiplication by \(X^\gamma\) is exact and gives the stated remainder class. The weighted map sends \(T_R:H^{0,\gamma-1}\to H^{0,1-\gamma}\), so its quadratic form is bounded by \(C\|w\|_{0,\gamma-1}^2\). Apply packet positivity to \(M_\gamma w\) on Schwartz inputs, and use self-adjointness of the real multiplication factor:

\[
 \operatorname{Re}(M_\gamma\operatorname{Op}(a_R)M_\gamma w,w)
 \ge -C\|X^{-1}M_\gamma w\|_2^2.
\]

Subtract the bounded remainder form. This proves

\[
 \begin{aligned}
 \operatorname{Re}(\operatorname{Op}(R^{2\gamma}s_R)w,w)
 &\ge-C\|w\|_{0,\gamma-1}^2\\
 &\ge-C\|w\|_{0,\gamma-a}^2.
 \end{aligned}
 \tag{26}
\]

Here \(a\le1\). The common distributional action, exact Fourier convention and finite products are proved in the linked programme calculus. In the application \(0<\gamma<\delta/2\le1/2\), so \(c_R\) and the remainder have nonpositive spatial weights and bounded frequency derivatives. Their operators are bounded on \(L^2\); Schwartz density extends (26) to the actual \(H^m\) inputs used below. In the Fourier variables the same lower norm is \(\|\mathcal Fw\|_{H^{\gamma-1}}\), by Plancherel and the even bracket. Thus the classical order and Sobolev exponent stated above also follow from this local proof.

<a id="radiation-fourier-conjugation"></a>
**An alternative by Fourier conjugation.** The classical sharp lower bound of Hörmander [H3, Theorem 18.1.14] and Lerner [L, Theorem 2.5.4] gives another route to the first inequality in (26). Here is the complete reduction to the [proved order-one bound in The Sobolev domain of an elliptic operator](the-sobolev-domain-of-an-elliptic-operator.md#domain-half-order-conjugation).

Fix any real \(\gamma\) and any nonnegative family
\(c_R\in S(X^{2\gamma-1},G_1)\) with uniform seminorms. Set
\[
 \begin{gathered}
 b_R(y,\eta)=c_R(-\eta,y),\qquad
 Y=\langle y\rangle,\quad H=\langle\eta\rangle,\\
 G'_1=Y^{-2}|dy|^2+H^{-2}|d\eta|^2,\qquad
 J=\langle D_y\rangle,\quad \tau=1-\gamma.
 \end{gathered}
\]
The derivative bounds give \(b_R\in S(H^{2\gamma-1},G'_1)\). Hence
\(d_R=H^{2\tau}b_R\) is nonnegative in \(S(H,G'_1)\), since
\(2\tau+2\gamma-1=1\). The linked order-one proof yields
\(\operatorname{Re}(\operatorname{Op}_L(d_R)v,v)\geq-C_\gamma\|v\|_2^2\)
on Schwartz inputs, uniformly in \(R\).

Right multiplication by the real Fourier power \(J^\tau\) is exact in left quantization. The finite product with the remaining left factor therefore gives
\[
 J^\tau\operatorname{Op}_L(b_R)J^\tau
       =\operatorname{Op}_L(d_R)+T_R,
 \qquad T_R\in\operatorname{Op}S(Y^{-1},G'_1).
\]
Indeed the product has leading weight \(H\), and its first remainder gains \(Y^{-1}H^{-1}\). This conclusion holds for every fixed real \(\tau\), by the proved all-real symbol calculus. The finite-derivative bound makes \(T_R\) uniformly bounded on \(L^2\).

For \(w\in\mathcal S\), put \(v=J^{-\tau}\mathcal Fw\). Real Fourier powers preserve Schwartz space and are symmetric there. Exact Fourier conjugation sends \(\operatorname{Op}_L(c_R)\) to right quantization of \(b_R\); its adjoint is left quantization of the same real symbol. Their real forms agree, so
\[
 \begin{aligned}
 \operatorname{Re}(\operatorname{Op}_L(c_R)w,w)
 &=\operatorname{Re}((\operatorname{Op}_L(d_R)+T_R)v,v)\\
 &\geq-C'_\gamma\|v\|_2^2
 =-C'_\gamma\|\mathcal Fw\|_{H^{\gamma-1}}^2
 =-C'_\gamma\|X^{\gamma-1}w\|_2^2.
 \end{aligned}
\]
This proves the sharp weighted inequality for every fixed real \(\gamma\) on Schwartz inputs. For the actual \(c_R=R^{2\gamma}s_R\), the range \(0<\gamma<\delta/2\) makes the operators bounded on \(L^2\), so the same density argument as above gives (26) on the required inputs. The spatial-conjugation proof remains an independent route to the same bound.

<a id="radiation-commutator"></a>
We spell out the weighted finite calculation needed to combine this bound with the equation. Set \(Q_R=\operatorname{Op}(q_R)\). Apply the same finite calculus as in the near-frequency commutator to \(R^\gamma Q_R\). The free polynomial term is exact:

\[
 \begin{gathered}
[P_0(D),Q_R]
 \\
=\sum_{1\le|\beta|\le m}
  \frac{(-i)^{|\beta|}}{\beta!}
  \operatorname{Op}
   \bigl((\partial_\xi^\beta P_0)
                     (\partial_x^\beta q_R)\bigr).
 \end{gathered}
 \tag{27}
\]

The first term supplies \(-q_Rv\cdot\partial_xq_R\) after left multiplication by the adjoint and division by \(i\). Higher free terms and the first adjoint correction have weight \(X^{2\gamma-2}\).

For \(V_L\), the scalar zero-degree products cancel. A term differentiating its coefficient uses weight \(X^{-1-\delta}\); a term differentiating the escape factor instead uses \(X^{\gamma-1}\) with the undifferentiated coefficient weight \(X^{-\delta}\). After the other escape factor, both cases have weight \(X^{2\gamma-1-\delta}\). Choose a finite product order \(N\) with \(\delta N\ge1\). The exact remainder has weight at most \(X^{2\gamma-\delta-\delta N}\), hence the same required weight, with arbitrary rapid frequency bounds. This verifies all terms of the full differential order; the first generic \(G_\delta\) remainder alone would be insufficient.

The positive operator associated with \(R^{\gamma-1/2}\Phi_R\) has principal symbol \(R^{2\gamma-1}\Phi_R^2\). Its adjoint/product remainder has weight \(X^{2\gamma-2}\), contained in \(X^{2\gamma-1-\delta}\) because \(\delta\le1\). Thus the exact identity is

\[
 \begin{gathered}
R^{2\gamma}Q_R^*[P_0+V_L,Q_R]/i
 \\
={}\operatorname{Op}(R^{2\gamma}s_R)\\
 +R^{2\gamma-1}\operatorname{Op}(\Phi_R)^*
                         \operatorname{Op}(\Phi_R)\\
 +E_{R,\gamma},
 \end{gathered}
 \tag{28}
\]

where \(E_{R,\gamma}\) is uniformly in
\(S(X^{2\gamma-1-\delta},G_\delta)\). The weighted mapping theorem gives

\[
 \begin{gathered}
 E_{R,\gamma}:H^{0,\gamma-a}\longrightarrow H^{0,a-\gamma},\\
 |(E_{R,\gamma}w,w)|\le C\|w\|_{0,\gamma-a}^2.
 \end{gathered}
 \tag{29}
\]

For each fixed \(R\), the escape operator preserves \(H^m\). Approximation in \(H^m\) justifies (28) on each actual \(u_j\), exactly as in the near-frequency proof. Symmetry of \(P_0+V_L\) gives the real commutator form
\(-\operatorname{Im}z_j\|Q_Ru_j\|_2^2-\operatorname{Im}(Q_Rf_{0,j},Q_Ru_j)\).
The first term is nonpositive. Equations (26)–(29) imply

\[
 \begin{aligned}
 R^{-1}\|\operatorname{Op}(\Phi_R)u_j\|_2^2
 \le{}&-\operatorname{Im}(Q_Rf_{0,j},Q_Ru_j)\\
 &+CR^{-2\gamma}\|u_j\|_{0,\gamma-a}^2.
 \end{aligned}
 \tag{30}
\]

<a id="radiation-graph-limit"></a>
For fixed \(R\), the compact output and frequency support of \(\Phi_R\) turn the strong weighted convergence into strong \(L^2\) convergence of its outputs. The forcing converges strongly in \(B\). Both \(Q_R\) and its adjoint have the shell bounds, so \(Q_Ru_j\) converges weak-star in \(B^*\). The pairings therefore converge. We obtain

\[
 \begin{aligned}
 R^{-1}\|\operatorname{Op}(\Phi_R)u\|_2^2
 \le{}&-\operatorname{Im}(Q_Rf_0,Q_Ru)\\
 &+CR^{-2\gamma}\|u\|_{0,\gamma-a}^2.
 \end{aligned}
 \tag{31}
\]

For a Schwartz input, integration by parts in the compact frequency integral bounds the output by \(C_LX^{-L}\), uniformly in \(R\), and it is exactly zero inside \(|x|<cR\). Its \(B\) norm tends to zero. Schwartz space is dense in \(B\), by truncating its summable shell tail and smoothly approximating the remaining bounded-support \(L^2\) function. Uniform shell continuity gives

\[
 \|Q_Rf_0\|_B\longrightarrow0,\qquad
 \sup_R\|Q_Ru\|_{B^*}<\infty.
 \tag{32}
\]

The finite auxiliary norm and \(\gamma>0\) now yield

\[
 R^{-1}\|\operatorname{Op}(\Phi_R)u\|_2^2
       \longrightarrow0.
 \tag{33}
\]

<a id="radiation-fixed-collar"></a>
## 7. Operators away from a fixed outgoing collar

First suppose \(h_0\) vanishes in a fixed conic neighborhood of \(N_+(M_\lambda)\) for all sufficiently large \(|x|\). Choose the energy support of \(\chi\) sufficiently close to \(M_\lambda\), and the support of \(\rho_2\) sufficiently narrow. Then \(h_0=0\) wherever \(c_2(x,v(\xi))\) can be nonzero on a large annulus \(R<|x|<2R\). Since \(\omega(x/R)=1\) there, the following symbol identity holds at every output point of that annulus:

\[
 \begin{gathered}
h_0(x,\xi)\chi(\xi)^2=b(x,\xi)\Phi_R(x,\xi),
 \\
 b=h_0\chi/k.
 \end{gathered}
 \tag{34}
\]

The fixed symbol \(b\) lies in \(S(1,G_1)\). The exact finite first product gives

\[
 \begin{gathered}
 \operatorname{Op}(b)\operatorname{Op}(\Phi_R)
  =\operatorname{Op}(b\Phi_R)+\operatorname{Op}(r_R),\\
 r_R\text{ uniformly in }S(X^{-1},G_1).
 \end{gathered}
 \tag{35}
\]

The symbol difference in (34) is zero at every output point of the annulus. Its left quantization is therefore exactly zero there. The first term in (35) has vanishing normalized annular norm by (33) and the fixed \(L^2\) bound for \(\operatorname{Op}(b)\).

For the remainder, exact left multiplication gives
\(X\operatorname{Op}(r_R)=\operatorname{Op}(Xr_R)\).
The latter has a uniform order-zero shell bound. Consequently

\[
 \begin{gathered}
R^{-1/2}\|\operatorname{Op}(r_R)u\|_{L^2(R<|x|<2R)}
       \\
\le CR^{-1}\|u\|_{B^*}\longrightarrow0.
 \end{gathered}
 \tag{36}
\]

Lemma 2.1 proves \(h_0(x,D)\chi(D)^2u\in\dot B^*\).

## 8. Vanishing exactly on the bundle

A shrinking angular cutoff can have large derivatives. The following sharp shell estimate isolates the amplitude in the limiting constant.

<a id="radiation-sharp-shell"></a>
The amplitude-leading operator estimate used here is Hörmander [H3, Theorem 18.1.15]. The following proof also supplies the endpoint shell passage needed for the shrinking angular collar.

**Lemma 8.1.** If \(g\in S(1,G_1)\) has compact frequency support and \(M=\sup|g|\), then

\[
 \begin{gathered}
\limsup_{R\to\infty}R^{-1/2}
  \|\operatorname{Op}(g)w\|_{L^2(R<|x|<2R)}
       \\
\le C_{\mathrm{sh}}M\|w\|_{B^*}.
 \end{gathered}
 \tag{37}
\]

The constant \(C_{\mathrm{sh}}\) is independent of the derivative bounds of \(g\).

**Proof.** Choose \(\psi_R=\psi_*(x/R)\), values in \([0,1]\), equal one on the annulus and supported in \(R/2<|x|<3R\). Put \(A_R=\psi_R\operatorname{Op}(g)\). Multiplication on the left has exact left symbol \(\psi_Rg\). Its Fourier-conjugated adjoint is the left operator \(B_R=\operatorname{Op}_{\mathrm{left}}(b_R)\), with

\[
 b_R(y,\eta)=\psi_R(-\eta)\overline{g(-\eta,y)}.
\]

This family has amplitude at most \(M\) and is zero for \(|\eta|<R/2\). On its support \(|\eta|\asymp R\). Every \(\eta\) derivative either hits \(\psi_*(-\eta/R)\) or becomes an old position derivative of \(g\), and therefore supplies \(R^{-1}\). The old frequency derivatives become \(y\) derivatives and remain bounded. Thus, for every \(\alpha,\beta\),

\[
 |\partial_y^\alpha\partial_\eta^\beta b_R|
 \le C_{g,\alpha\beta}R^{-|\beta|}.
\]

The programme's [complex packet norm theorem, Theorem 4](../providers/analysis/weighted-positivity.md#high-frequency-norm), now applies with these exact bounds. Its proved Gaussian comparison gives \(\|B_R\|_{2\to2}\le M+C_g/R\), hence also \(M+C_gR^{-1/2}\) for \(R\ge1\). The error uses finitely many derivative bounds of this fixed \(g\); the coefficient of \(M\) is exactly one, including \(M=0\). Fourier unitarity and the proved equality of adjoint norms give

\[
 \|\psi_R\operatorname{Op}(g)\|_{2\to2}
       \le M+C_gR^{-1/2}.
 \tag{38}
\]

<a id="radiation-quadratic-form-alternative"></a>
**A quadratic-form proof of (38).** The finite-adjoint/product argument in [The Sobolev domain of an elliptic operator, the alternative proof of (32)](the-sobolev-domain-of-an-elliptic-operator.md#domain-quadratic-form-alternative), applies to this family as well. Here are its hypotheses and cutoff constants. The support in \(y\) is contained in the fixed compact frequency support of \(g\); on the support in \(\eta\), \(|\eta|\asymp R\). Thus the displayed derivative bounds for \(b_R\) give uniform \(S(1,G_1)\) seminorms in \((y,\eta)\). The symbol \(M^2-|b_R|^2\) is real, nonnegative and uniformly of classical order zero. The [complete order-zero positivity theorem](../providers/analysis/weighted-positivity.md#ordinary-order-zero-positivity) and the exact finite product and adjoint formulas give

\[
 \begin{aligned}
 B_R^*B_R&=\operatorname{Op}_L(|b_R|^2)+T_R,\\
 T_R&\in\operatorname{Op}S(\langle y\rangle^{-1}\langle\eta\rangle^{-1},G_1),\\
 \|B_Rv\|_2^2&\le M^2\|v\|_2^2+C_g\|v\|_{H^{-1/2}}^2.
 \end{aligned}
 \tag{38a}
\]

For the remainder bound, conjugation by \(\langle D_y\rangle^{1/2}\) on both sides leaves weight \(\langle y\rangle^{-1}\), so the programme's order-zero bound applies exactly as in that earlier proof. Choose \(0\le\kappa\le1\), zero on \(|\eta|\le1/4\) and one on \(|\eta|\ge1/2\). The vanishing of \(b_R\) for \(|\eta|<R/2\) gives \(B_R=B_R\kappa(D_y/R)\) exactly. For \(v=\kappa(D_y/R)h\), Plancherel bounds the two terms in (38a) by \(M^2\|h\|_2^2\) and \(4C_gR^{-1}\|h\|_2^2\). Taking square roots and absorbing four into the fixed constant proves \(\|B_R\|\le M+\sqrt{C_g}R^{-1/2}\). Fourier unitarity and equality of adjoint norms recover (38), again with coefficient one on \(M\), including \(M=0\). No derivative bound of a later shrinking angular cutoff enters that coefficient.

Choose a smooth input cutoff \(\theta_R\), equal one on \(R/4<|x|<4R\), supported in \(R/8<|x|<8R\), with values in \([0,1]\). Fixed shell geometry gives

\[
 \|\theta_Rw\|_2
       \le C_{\mathrm{sh}}R^{1/2}\|w\|_{B^*}.
 \tag{39}
\]

<a id="radiation-distant-kernel"></a>
For the remaining input, compact frequency support and integration by parts give the kernel bound

\[
 \begin{gathered}
|K_R(x,y)|
 \\
\le C_N1_{\{R/2<|x|<3R\}}(1+|x-y|)^{-N}.
 \end{gathered}
 \tag{40}
\]

The inner input ball is separated from the output by a fixed multiple of \(R\). Its \(L^1\) norm is at most \(CR^{(n+1)/2}\|w\|_{B^*}\), by Cauchy–Schwarz and the endpoint ball bound. An exterior input shell of radius \(2^kR\) has the analogous bound. Multiply by the output volume square root and sum the distant shells. For \(N>n+1\),

\[
 \begin{gathered}
\|\psi_R\operatorname{Op}(g)(1-\theta_R)w\|_2
       \\
\le C_NR^{n+1/2-N}\|w\|_{B^*}.
 \end{gathered}
 \tag{41}
\]

The integrals are absolutely convergent and give the common distributional action. Combine (38)–(41), divide by \(R^{1/2}\), and let \(R\to\infty\). All derivative-dependent terms vanish for this fixed \(g\), proving (37). \(\square\)

<a id="radiation-exact-bundle"></a>
Now let the compact-frequency symbol \(h\chi^2\) vanish only exactly on \(N_+(M_\lambda)\). The [proved energy-coordinate inverse (CI1)–(CI3) and finite smooth partitions](../providers/analysis/coordinate-inverses-and-integration.md#coordinate-inverse), already used in the earlier curved-trace lesson, give finitely many smooth projections \(\pi(\xi)\in M_\lambda\) near the compact regular shell. On smaller charts their first derivatives are bounded and \(|\xi-\pi(\xi)|\le C|P_0(\xi)-\lambda|\), by integrating the energy-coordinate derivative. The velocity has a positive minimum there, so \(v/|v|\) is Lipschitz. On each spatial sphere use a smooth angular collar about that direction. For \(|x|=r\ge1\), a directional displacement of angle \(\theta\) has path length at most \(Cr\theta\); the symbol's position derivative is \(O(\langle r\rangle^{-1})\), so this changes its value by at most \(C\theta\). Its frequency derivatives are uniformly bounded on the compact support. Moving frequency to \(\pi(\xi)\), then direction to \(v(\pi(\xi))/|v(\pi(\xi))|\) at the same radius, consequently changes the symbol by at most \(C(\kappa+\theta)\) when the energy-collar width is \(\kappa\). The final point belongs to the outgoing bundle, where the symbol is zero. In dimension one the direction set has two isolated points; for a sufficiently small collar the direction already agrees, and only the frequency estimate is needed. This proves uniform smallness on the chosen collar in every dimension.

For every \(\varepsilon>0\), multiply by a smooth collar equal one on a smaller neighborhood to obtain a decomposition

\[
 h\chi^2=g_0+g_1,\qquad \sup|g_1|\le\varepsilon,
 \tag{42}
\]

outside a fixed bounded spatial region. For this fixed \(\varepsilon\), first narrow the energy support of \(\chi\) to lie in the chosen energy collar. Replacing a previous cutoff by this one changes the near-energy output by an off-energy term covered by (15). Thus \(g_0\) vanishes throughout a fixed outgoing angular collar on the remaining frequency support, exactly as Section 7 requires. Both pieces are \(G_1\) symbols with compact frequency support. Their derivative constants may depend on \(\varepsilon\). A bounded spatial output cutoff contributes an \(L^2\) function, by its smoothing compact-frequency kernel and the polynomial endpoint growth, hence an element of \(\dot B^*\).

To apply Section 7 to \(g_0\), choose a further compact smooth frequency cutoff \(\zeta\), equal one near its frequency support and supported in the same noncritical energy neighborhood. The angular collar for \(g_0\) can be taken on this slightly larger neighborhood: outside its own frequency support the symbol is zero. Exact right composition with a frequency multiplier gives \(\operatorname{Op}(g_0)\zeta(D)^2=\operatorname{Op}(g_0)\). Section 7, with \(h_0=g_0\) and \(\chi=\zeta\), therefore puts this output in \(\dot B^*\). Lemma 8.1 treats \(g_1\). Take the radius limit for this fixed decomposition, then let \(\varepsilon\downarrow0\):

\[
 \begin{gathered}
\limsup_{R\to\infty}R^{-1/2}
 \|h(x,D)\chi(D)^2u\|_{L^2(R<|x|<2R)}
 \\
\le C_{\mathrm{sh}}\varepsilon\|u\|_{B^*}
 \longrightarrow0.
 \end{gathered}
 \tag{43}
\]

Lemma 2.1 and the off-energy result (15) prove Theorem 1.1 in its full stated scope. \(\square\)

### Use the conclusion

Check weighted strong convergence of the graph before applying a full-order symbol. Distinguish being supported away from the outgoing bundle from vanishing exactly on it; both steps are needed in the theorem.

<a id="radiation-solutions"></a>
## 9. Graded exercises with complete solutions

**Exercise 1 — Basic: shell decay and closure.** Choose \(L^2\)-normalized \(e_j\), supported in \(A_j\), \(j\ge1\), and define

\[
 \begin{aligned}
 w&=\sum_{j\ge1}\frac{R_j^{1/2}}{j+1}e_j,\\
 v&=\sum_{j\ge1}R_j^{1/2}e_j.
 \end{aligned}
 \tag{44}
\]

Determine their \(B^*\) norms and membership in \(\dot B^*\). Calculate the normalized ball mass of \(v\) at \(R_J\).

**Solution 1.** Every fixed ball meets finitely many shells, so both functions are locally square-integrable. Their normalized shell norms are \(1/(j+1)\) and \(1\). Thus \(\|w\|_{B^*}=1/2\) and \(\|v\|_{B^*}=1\). Lemma 2.1 puts \(w\) in \(\dot B^*\) and excludes \(v\). Directly,

\[
 \begin{gathered}
R_J^{-1}\|v\|_{L^2(|x|<R_J)}^2
   \\
=2^{-J}\sum_{j=1}^J2^j
   =2-2^{1-J}\longrightarrow2.
 \end{gathered}
 \tag{45}
\]

An endpoint bound permits a nonzero mass per unit radius. The closure condition requires that mass to tend to zero.

**Exercise 2 — Intermediate: extend the inequality before using the limit.** Suppose the graph inequality is known on Schwartz inputs. Prove it for every input already known in \(H^{m,t}\). Then assume \((H-z_j)u_j=f_j\), \((H-\lambda)u=f\), uniform derivative endpoint bounds through \(m\), \(f_j\to f\) in \(B\), \(z_j\to\lambda\), and \(u_j\to u\) in \(H^{0,-b}\), \(b>1/2\). Prove convergence in \(H^{m,-b}\), and in \(B\) of the short-range outputs when \(b<1/2+\delta\).

**Solution 2.** The smooth maps give \(P_0:H^{m,t}\to H^{0,t}\) and \(V_L:H^{m,t}\to H^{0,t+\delta}\). The primary rough map gives \(V_S:H^{m,t}\to H^{0,t+1+\delta}\). Both larger weights embed into \(H^{0,t}\). Thus the full expression is continuous \(H^{m,t}\to H^{0,t}\), with its actual local differential action. Schwartz approximation in the input norm also approximates its image in the output norm. Pass the graph inequality to that limit. This gives (11) on an already regular weighted input.

The derivative endpoint bounds and the strict embedding put \(u_j,u\) in \(H^{m,-b}\). Hence their difference is an admissible input. Its equation is (12). The forcing difference tends to zero in \(H^{0,-b}\), since \(B\subset L^2\subset H^{0,-b}\). The parameter difference tends to zero times a uniformly bounded weighted norm. Together with the assumed zeroth-order convergence, (11) proves full \(H^{m,-b}\) convergence. The primary short-range map gives

\[
 \begin{gathered}
\|V_S(u_j-u)\|_{0,1+\delta-b}
       \\
\le C_b\|u_j-u\|_{m,-b}\longrightarrow0.
 \end{gathered}
 \tag{46}
\]

The output weight exceeds \(1/2\) in the stated range, so its strict embedding into \(B\) proves convergence of the entire short-range forcing.

**Exercise 3 — Intermediate: the upper normal bundle on the line.** Let \(H=-\partial_x^2\), \(\lambda=1\), and take a nonzero, nonnegative, even \(f\in C_c^\infty((-1/4,1/4))\). Put

\[
 u_\pm(x)=\frac{\pm i}{2}
        \int e^{\pm i|x-y|}f(y)\,dy.
 \tag{47}
\]

Choose smooth even \(\kappa\), zero on \(|x|\le1\), one on \(|x|\ge2\). Define \(h(x,\xi)=\kappa(x)(\xi-\operatorname{sign}x)\), extended by zero near the origin. Describe \(N_+(M_1)\). Show that \(u_+\notin\dot B^*\) but \(h(x,D)u_+=0\). Show that the same operator sends \(u_-\) to a function outside \(\dot B^*\). Verify an actual upper graph sequence with fixed forcing and limit \(u_+\).

**Solution 3.** The shell is \(\{-1,1\}\) and the velocities are \(2\xi\). Therefore

\[
 \begin{aligned}
 N_+(M_1)
 ={}&\{(x,1):x>0\}\\
 &\cup\{(x,-1):x<0\}.
 \end{aligned}
 \tag{48}
\]

The symbol vanishes on both rays. It is smooth, since \(\kappa\) removes the sign discontinuity; its positive position derivatives have compact support. Its frequency order is one, within the theorem's order \(m=2\).

Let \(F=\int\cos(y)f(y)\,dy\). Evenness removes the sine contribution, and \(\cos y>0\) on the support, so \(F>0\). Outside that support, \(u_\pm=\pm iF e^{\pm i|x|}/2\). All derivatives through two have bounded tail amplitudes and finite endpoint norms. The normalized ball mass of \(u_+\) tends to \(2(F/2)^2>0\), so \(u_+\notin\dot B^*\).

For \(|x|>1\), \(De^{i|x|}=\operatorname{sign}(x)e^{i|x|}\); inside that interval \(\kappa=0\). The exact left differential action therefore gives

\[
 \begin{gathered}
h(x,D)u_+=0,\\
 h(x,D)u_-=-2\operatorname{sign}(x)\kappa(x)u_-.
 \end{gathered}
 \tag{49}
\]

The second output has tail amplitude \(F\), with normalized ball mass tending to \(2F^2>0\). The upper sign selects the positive bundle.

For the graph sequence take \(z_j=1+i/j\), and its square root \(k_j\) with positive real and imaginary parts. Set

\[
 u_j(x)=\frac{i}{2k_j}
        \int e^{ik_j|x-y|}f(y)\,dy.
 \tag{50}
\]

The first derivative of the kernel has jump \(-1\) at \(x=y\), giving \((-\partial_x^2-z_j)u_j=f\). Its exponential tails put it in \(H^2\), so it is the nonreal resolvent solution. The \(k_j\) are bounded and bounded away from zero. The functions and their first derivatives are uniformly pointwise bounded; \(u_j''=-z_ju_j-f\) bounds the second derivatives. All derivative endpoint norms through two are uniformly bounded. The integral and the equation give local convergence of those derivatives to the derivatives of \(u_+\). Compact \(L^2\) tests are dense in \(B\), so local convergence and uniform endpoint norms imply the required weak-star convergence. The forcing remains the same \(f\in B\).

**Exercise 4 — Advanced: disappearing escape forcing.** Suppose \(q_R\) has compact frequency support, uniformly bounded frequency derivatives, exact zero output on \(|x|<cR\), and uniformly bounded maps on \(B\). Prove \(\|\operatorname{Op}(q_R)g\|_B\to0\) for every \(g\in B\). Give a power bound for Schwartz \(g\).

**Solution 4.** Repeated integration by parts in its exact compact frequency integral gives \(|\operatorname{Op}(q_R)g(x)|\le C_NX^{-N}\), uniformly in \(R\), for every sufficiently large integer \(N\). The output is zero for \(|x|<cR\). Shell volume comparison and a geometric sum therefore give

\[
 \begin{aligned}
 \|\operatorname{Op}(q_R)g\|_B
 &\le C_N\sum_{R_j\gtrsim cR}
                      R_j^{(n+1)/2-N}\\
 &\le C'_NR^{(n+1)/2-N}.
 \end{aligned}
 \tag{51}
\]

Choose \(N>(n+1)/2\). For general \(g\), truncate its summable shell tail. Smoothly approximate the remaining bounded-support \(L^2\) function; on fixed bounded support, finitely many shell weights control its \(B\) norm by its \(L^2\) norm. This proves Schwartz density in \(B\). Choose \(g_0\) with \(\|g-g_0\|_B<\varepsilon\), use the uniform operator norm on the difference, and the proved decay on \(g_0\). The upper limit is at most \(C\varepsilon\). Let \(\varepsilon\downarrow0\).

**Exercise 5 — Advanced: weighted errors and iterated limits.** Take \(\delta=1/3\), \(\gamma=1/12\). Compute the smallest finite product order satisfying \(\delta N\ge1\), the auxiliary weight, the classical positive-symbol order and its sharp lower-bound Sobolev exponent, and the power \(R^{-2\gamma}\). Explain the order of limits for angular pieces of amplitude at most \(\varepsilon\) whose derivative-dependent sharp error is \(C_\varepsilon R^{-1/2}\).

**Solution 5.** The smallest integer is \(N=3\). With \(a=2/3\), the relevant exponents are

\[
 \begin{aligned}
 \gamma-a&=-7/12,\\
 2\gamma-1&=-5/6=2(-11/12)+1,\\
 \gamma-1&=-11/12,\\
 2\gamma-1-\delta&=-7/6=2(-7/12).
 \end{aligned}
 \tag{52}
\]

The sharp lower-bound norm with weight \(-11/12\) is controlled by the auxiliary norm with weight \(-7/12\). The full scaled error maps \(H^{0,-7/12}\) to \(H^{0,7/12}\), so its quadratic form is bounded by the squared auxiliary norm. Dividing by \(R^{2\gamma}\) leaves \(R^{-1/6}\), which tends to zero.

For each fixed angular decomposition, (37) gives a limiting shell norm bounded by \(C_{\mathrm{sh}}\varepsilon\|u\|_{B^*}\). Derivative-dependent errors disappear in that radius limit. Letting \(\varepsilon\to0\) afterward proves shell vanishing. An uncontrolled simultaneous choice does not justify the inference: if the available constant is \(C_\varepsilon=e^{1/\varepsilon}\), choosing \(\varepsilon_R=1/\log R\) makes \(C_{\varepsilon_R}R^{-1/2}=R^{1/2}\). This shows that this error bound supplies no decay for that choice. The iterated limit requires no uniform derivative constants for shrinking angular collars.

## 10. Further questions

The graph-limit radiation statement is the directional step toward a limiting resolvent theorem. The next arguments compute the perturbed flux, convert zero flux into vanishing shell mass of all derivatives, and obtain stronger decay and point-spectrum conclusions.

## References

The [accessible scalar comparisons in the limiting-absorption lesson](limiting-absorption-for-long-range-differential-perturbations.md#accessible-scalar-comparisons-and-their-proof-limits) state Ito–Skibsted's Theorem 1.23 and Proposition 4.14 with their exact smoothness, dimension, eigenvalue and weight restrictions. Their eikonal radiation derivatives provide a scalar comparison. The exact polynomial normal-bundle assertion and rough graph proof of this lesson are supplied by Sections 3–8.

[A] Shmuel Agmon, notes by Karl Gustafson, reworked by Michael Taylor, [*Limiting Absorption Principle for Long Range Potentials*](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2020/08/AGMON.pdf), lectures of 17–21 July 1978, §2, Theorem 2.J, and §4, Theorem 4.A, supplies the freely readable amplitude-collar and normal-ray construction. The latter uses the unproved Proposition 3.F. Here Sections 5–6 replace that step by the fully displayed finite weighted commutator, and Sections 7–8 prove the exact-bundle conclusion for general \(G_1\) symbols, including symbols not homogeneous in position. Section 3 proves passage of the actual rough differential graph. These are the additional bridges needed for the stated full-order conclusion.

[L] Nicolas Lerner, [*Metrics on the Phase Space and Non-Selfadjoint Pseudo-Differential Operators*, free author chapter on phase-space metrics](https://webusers.imj-prg.fr/~nicolas.lerner/ch2booklerner.pdf), Proposition 2.4.3, printed pp. 101–103, presents the positive-packet construction reconstructed in the programme's weighted-positivity reading. The general-metric Theorems 2.5.1 and 2.5.4, printed pp. 111–115, are broader comparisons whose proofs use further localization and almost-orthogonality results. Here Section 6 obtains (26) from the programme's proved Theorem 1 by an explicit spatial conjugation; Section 8 uses its proved complex packet Theorem 4. Neither step assumes the external general-metric theorems.

[T] Gerald Teschl, [*Mathematical Methods in Quantum Mechanics*, author's online edition](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf), Theorems 0.38–0.39, printed pp. 32–33, proves the completeness and uniform-boundedness argument reconstructed for the endpoint graph in Section 3. Its self-adjoint resolvent theory provides additional comparison; the earlier programme supplies the resolvent input used here.


[H3] Lars Hörmander, *The Analysis of Linear Partial Differential Operators III: Pseudo-Differential Operators*, reprint of the 1994 edition, Springer, 2007, Theorems 18.1.14–18.1.15 and their proofs, pp. 76–80. ISBN 978-3-540-49938-1. [Edition information](https://doi.org/10.1007/978-3-540-49938-1).

[H4] Lars Hörmander, *The Analysis of Linear Partial Differential Operators IV: Fourier Integral Operators*, reprint of the 1994 edition, Springer, 2009, §30.2, Theorem 30.2.6 and its proof, pp. 289–291. ISBN 978-3-642-00136-9. [Edition information](https://doi.org/10.1007/978-3-642-00136-9).
