# The KMS boundary condition determines the modular group

A weight is usually infinite on the identity, so its modular boundary condition must specify which products have finite values. We begin with that domain, construct the strip function from the two modular half powers, and prove that the boundary condition determines the automorphism group. The uniqueness argument uses Gaussian vectors in bounded spectral subspaces of the modular operator and a periodicity argument. It requires neither a faithful state nor a theorem introducing generators of unitary groups.

The source antecedents are Takesaki, *Theory of Operator Algebras II*, VIII.1, Definition 1.1, Theorem 1.2, Definition 1.3 and Corollary 1.4. All theorem statements below concern arbitrary von Neumann algebras and faithful normal semifinite weights unless another hypothesis is stated explicitly.

For a comparison exposition, see Hiai, [*Concise lectures on selected topics of von Neumann algebras*, version 1](https://arxiv.org/abs/2004.02383v1), Theorem 2.14 for the state case and Section 7.1(C) for the weight statement. Half-power continuation, analytic averaging and imaginary periodicity are classical mechanisms. The proof here applies periodicity to Gaussian GNS vectors in spectral bands of the already constructed modular operator.

## The finite products and the strip convention

Let \(\varphi\) be a faithful normal semifinite weight on a von Neumann algebra \(M\). Use WG and WH for the finite left ideal, finite linear domain and finite *-algebra

\[
\mathfrak n_\varphi=\{x\in M:\varphi(x^*x)<\infty\},\qquad
\mathfrak m_\varphi=\operatorname{span}\{y^*x:x,y\in\mathfrak n_\varphi\},\qquad
\mathfrak a_\varphi=\mathfrak n_\varphi\cap\mathfrak n_\varphi^*.
\tag{KM.1}
\]

The same symbol \(\varphi\) denotes the linear extension to \(\mathfrak m_\varphi\). Its GNS map satisfies

\[
\langle\Lambda_\varphi(x),\Lambda_\varphi(y)\rangle
=\varphi(y^*x),\qquad x,y\in\mathfrak n_\varphi,
\tag{KM.2}
\]

with inner product linear in the first variable. We identify \(M\) with its faithful normal GNS image when writing operators on \(H_\varphi\). The representation is faithful and has the bounded-set topology properties proved in WH-02.

Set \(\overline{\mathcal S}=\{z\in\mathbb C:0\leq\operatorname{Im}z\leq1\}\), with interior \(\mathcal S\). An algebraic one-parameter group \(\beta_t\) of *-automorphisms satisfies the **modular KMS condition** for \(\varphi\) when:

1. \(\varphi\circ\beta_t=\varphi\) on \(M_+\) for every real \(t\).
2. For every \(x,y\in\mathfrak a_\varphi\), there is a bounded continuous scalar function \(F_{x,y}\) on \(\overline{\mathcal S}\), holomorphic on \(\mathcal S\), with

\[
F_{x,y}(t)=\varphi(\beta_t(x)y),\qquad
F_{x,y}(t+i)=\varphi(y\beta_t(x))\quad(t\in\mathbb R).
\tag{KM.3}
\]

Invariance implies that \(\beta_t\) preserves each domain in (KM.1). The first product in (KM.3) is \((\beta_t(x)^*)^*y\); both factors in this form lie in \(\mathfrak n_\varphi\). The second is \((y^*)^*\beta_t(x)\), with the same property. Thus both scalar values are defined in \(\mathfrak m_\varphi\). No value of the weight on an arbitrary nonpositive element of \(M\) is intended.

The bounded strip uniqueness and maximum principle in MA-08 give uniqueness of \(F_{x,y}\), and

\[
\sup_{z\in\overline{\mathcal S}}|F_{x,y}(z)|
\leq\max\left\{
\varphi(yy^*)^{1/2}\varphi(x^*x)^{1/2},
\varphi(y^*y)^{1/2}\varphi(xx^*)^{1/2}
\right\}.
\tag{KM.4}
\]

Here the two terms may be listed in either order: Cauchy–Schwarz on the lower boundary gives \(\varphi(y^*y)^{1/2}\varphi(xx^*)^{1/2}\), and on the upper boundary gives the other term. Invariance makes these bounds uniform in \(t\).

We initially impose no continuity on \(\beta\) beyond the scalar strip condition. KM-03 will derive strong continuity of its GNS implementers and pointwise sigma-strong* continuity of \(\beta\). In particular the uniqueness assertion also applies to automorphism groups for which continuity is part of the definition.

The exact prerequisites are WG/WH for (KM.1–2), the full finite-star Hilbert algebra and its graph core; TC for closed-involution polar uniqueness; MF-06 for the existing modular group and weight invariance; SK-05, SK-07–09 for spectral bands, transported functional calculus and powers; and MA-08–09, MA-16 for bounded strips, half-power continuation and Gaussian entire vectors. Scalar Liouville follows from the Cauchy estimate as recalled in KM-05. The proofs of these prerequisites are not given here.

## Existence from the two half powers

Let \(S\) be the closed involution of the full Hilbert algebra
\(\mathcal A=\Lambda_\varphi(\mathfrak a_\varphi)\), and let

\[
S=J\Delta^{1/2},\qquad D(S)=D(\Delta^{1/2}),\qquad U_t=\Delta^{it}.
\]

The automorphisms constructed in MF are

\[
\sigma_t^\varphi(x)=\pi_\varphi^{-1}
       (U_t\pi_\varphi(x)U_{-t}).
\tag{KM.5}
\]

They satisfy the modular KMS condition (KM.3).

**Proof.** MF-06 proves weight invariance on all of \(M_+\), including infinite values, and the exact GNS covariance
\(\Lambda_\varphi(\sigma_t^\varphi(x))=U_t\Lambda_\varphi(x)\) for \(x\in\mathfrak n_\varphi\). For \(x,y\in\mathfrak a_\varphi\), put
\(\xi=\Lambda_\varphi(y)\) and \(\eta=\Lambda_\varphi(x^*)\). Both lie in \(D(\Delta^{1/2})\). Define

\[
F_{x,y}(z)=
\left\langle\Delta^{-iz/2}\xi,
                \Delta^{i\overline z/2}\eta\right\rangle
\quad(z\in\overline{\mathcal S}).
\tag{KM.6}
\]

Each power uses only a real exponent between zero and one half. MA-09 makes the first vector a bounded continuous, interior holomorphic function on the closed upper strip; the second is antiholomorphic there. The antilinearity of the second slot makes their pairing holomorphic. Both vectors have uniformly bounded norms on the strip, so (KM.6) has the required boundedness and continuity.

On the lower boundary, the unitary group law gives

\[
F_{x,y}(t)=\langle\xi,U_t\eta\rangle
=\varphi(\sigma_t^\varphi(x)y).
\tag{KM.7}
\]

On the upper boundary, spectral transport and the antiunitarity of \(J\) give

\[
\begin{aligned}
F_{x,y}(t+i)
&=\langle\Delta^{1/2}\xi,\Delta^{1/2}U_t\eta\rangle\\
&=\langle SU_t\eta,S\xi\rangle\\
&=\langle\Lambda_\varphi(\sigma_t^\varphi(x)),
                \Lambda_\varphi(y^*)\rangle
=\varphi(y\sigma_t^\varphi(x)).
\end{aligned}
\tag{KM.8}
\]

These identities prove the condition for every required pair. The maximum principle gives the sharper boundary bound (KM.4). \(\square\)

## An invariant competing group acts continuously on the GNS space

Suppose \(\beta_t\) satisfies (KM.3). Invariance defines unitaries by

\[
V_t\Lambda_\varphi(x)=\Lambda_\varphi(\beta_t(x))
\quad(x\in\mathfrak n_\varphi).
\tag{KM.9}
\]

They form a strongly continuous group. They implement \(\beta\), preserve \(D(S)\), and commute with \(S,J\) and every spectral projection of \(\Delta\).

**Proof.** The GNS norm in (KM.2) and invariance prove that (KM.9) is a well-defined isometry on the dense GNS subspace. Applying \(-t\) makes its extension a surjective isometry. The group law holds on that dense subspace and hence on \(H_\varphi\). For \(a\in M\) and \(x\in\mathfrak n_\varphi\), left-ideal covariance gives

\[
V_t\pi_\varphi(a)V_{-t}\Lambda_\varphi(x)
=\pi_\varphi(\beta_t(a))\Lambda_\varphi(x).
\tag{KM.10}
\]

Thus the equality holds as an equality of bounded operators.

If \(\xi=\Lambda_\varphi(x)\), \(\eta=\Lambda_\varphi(y)\) with \(x,y\in\mathfrak a_\varphi\), the lower boundary of the KMS function for the pair \((y^*,x)\) is

\[
\varphi(\beta_t(y^*)x)=\langle\xi,V_t\eta\rangle.
\tag{KM.11}
\]

It is continuous in \(t\). Since \(\mathcal A\) is dense and the operator norms are one, approximation extends this weak continuity to every pair of Hilbert vectors. The identity for the squared distance of two unitary orbit vectors then gives strong continuity.

On \(\mathcal A\), preservation of the adjoint in \(M\) gives \(SV_t=V_tS\), and \(V_t\mathcal A=\mathcal A\). Since \(\mathcal A\) is a graph core for \(S\), closedness and approximation give

\[
V_tD(S)=D(S),\qquad V_tSV_{-t}=S.
\tag{KM.12}
\]

The polar decomposition of the left side is
\((V_tJV_{-t})(V_t\Delta^{1/2}V_{-t})\). Uniqueness of the closed-involution polar factors therefore gives

\[
V_tJV_{-t}=J,\qquad V_t\Delta^{1/2}V_{-t}=\Delta^{1/2}.
\tag{KM.13}
\]

These identities include domains. Spectral transport SK-08 implies commutation with every spectral projection and every power of \(\Delta\), on its domain.

Equation (KM.10) and strong continuity show that each operator orbit is bounded and strongly* continuous. A *-automorphism of a von Neumann algebra is normal: it preserves the positive order and hence all bounded increasing suprema. WH-02 transports the bounded-set continuity back from the faithful normal representation, yielding pointwise sigma-strong* continuity of \(\beta\). \(\square\)

## Extending the boundary identity to the whole form domain

For any \(\xi,\eta\in D(S)\), there is a unique bounded continuous function \(G_{\xi,\eta}\) on \(\overline{\mathcal S}\), holomorphic on \(\mathcal S\), such that

\[
\begin{aligned}
G_{\xi,\eta}(t)&=\langle\xi,V_t\eta\rangle,\\
G_{\xi,\eta}(t+i)&=\langle SV_t\eta,S\xi\rangle
=\langle\Delta^{1/2}\xi,\Delta^{1/2}V_t\eta\rangle.
\end{aligned}
\tag{KM.14}
\]

Its supremum norm is at most
\(\max\{\|\xi\|\|\eta\|,\|S\xi\|\|S\eta\|\}\).

**Proof.** On \(\mathcal A\), use (KM.11) and the upper boundary of the same pair; (KM.2) gives exactly the first expression on the second line of (KM.14). The last expression follows from \(S=J\Delta^{1/2}\). For general \(\xi,\eta\in D(S)\), choose \(\xi_n,\eta_n\in\mathcal A\) converging in the \(S\)-graph norm. On the lower boundary the difference between the functions for indices \(n,m\) is bounded uniformly in \(t\) by

\[
\|\xi_n-\xi_m\|\,\|\eta_n\|
+\|\xi_m\|\,\|\eta_n-\eta_m\|.
\]

On the upper boundary the analogous bound has \(S\) applied to each vector, because \(SV_t=V_tS\) and \(V_t\) is unitary. Both bounds tend to zero. The bounded-strip maximum principle makes the entire sequence Cauchy in the supremum norm on the closed strip. Its uniform limit is bounded and continuous there and holomorphic inside; the limits of the two edges are (KM.14). Uniqueness and the stated bound follow from MA-08. The sequence is used only in the metrizable graph norm, not as a replacement for arbitrary von Neumann algebra nets. \(\square\)

## Uniqueness by an imaginary shift and periodicity

Every group \(\beta\) satisfying (KM.3) equals \(\sigma^\varphi\).

**Proof.** Write

\[
P_n=1_{[e^{-n},e^n]}(\Delta),\qquad H_n=P_nH_\varphi
\quad(n\geq1).
\tag{KM.15}
\]

These projections commute with every \(V_t\) by (KM.13), and increase strongly to the identity because \(\Delta\) is injective. On \(H_n\), the restriction \(\Delta_n\) is bounded positive and has bounded inverse; its powers at every complex exponent are bounded. Every vector of \(H_n\) belongs to \(D(\Delta)\subseteq D(S)\).

Fix \(v\in H_\varphi\), \(r>0\), and \(n\). Define an entire vector function, without introducing any nonreal bounded operator \(V_z\), by

\[
h(w)=\sqrt{r/\pi}\int_{\mathbb R}e^{-r(t-w)^2}V_tP_nv\,dt
\quad(w\in\mathbb C).
\tag{KM.16}
\]

MA-16 gives the norm integral, holomorphy and the identities

\[
h(w)\in H_n,\qquad V_th(w)=h(w+t),\qquad
\|h(t+is)\|\leq e^{rs^2}\|P_nv\|.
\tag{KM.17}
\]

For fixed \(w\) and \(\xi\in D(S)\), compare \(G_{\xi,h(w)}\) from KM-04 with the scalar function

\[
z\longmapsto\langle\xi,h(w+\overline z)\rangle.
\tag{KM.18}
\]

This function is holomorphic, since conjugating the parameter and using the antilinear second inner-product slot cancel. It is continuous and bounded on the closed upper strip by (KM.17). On its lower boundary it equals \(\langle\xi,V_th(w)\rangle\). Bounded-strip boundary uniqueness identifies it with \(G_{\xi,h(w)}\). At \(z=i\), (KM.14) therefore gives

\[
\langle\xi,h(w-i)\rangle
=\langle\Delta^{1/2}\xi,\Delta^{1/2}h(w)\rangle
=\langle\xi,\Delta h(w)\rangle.
\tag{KM.19}
\]

The last equality has its domain because \(h(w)\in H_n\subseteq D(\Delta)\). Density of \(D(S)\) yields the vector identity

\[
h(w-i)=\Delta_nh(w)\quad(w\in\mathbb C).
\tag{KM.20}
\]

Consider now the \(H_n\)-valued entire function

\[
q(w)=\Delta_n^{-iw}h(w).
\tag{KM.21}
\]

The factor is operator-norm entire by the bounded logarithm of \(\Delta_n\). The exponent calculation \(-i(w-i)=-iw-1\), together with (KM.20), gives \(q(w-i)=q(w)\). If \(w=t+is\) and \(0\leq s\leq1\),

\[
\|q(w)\|\leq\|\Delta_n^s\|\,\|h(w)\|
\leq e^{n+r}\|P_nv\|.
\tag{KM.22}
\]

Its imaginary period makes this a bound on the entire plane. Testing against any Hilbert vector gives a bounded entire scalar function, hence a constant: the scalar Cauchy derivative estimate on circles of radius \(R\) is at most the global bound divided by \(R\), and letting \(R\to\infty\) gives zero derivative. Equality of all vector coefficients makes \(q\) constant. Thus

\[
V_th(0)=h(t)=\Delta^{it}h(0)\quad(t\in\mathbb R).
\tag{KM.23}
\]

For fixed \(n,v\), Gaussian approximation MA-16 gives \(h(0)\to P_nv\) as \(r\to\infty\). Both operators in (KM.23) are unitary, so the identity extends to \(P_nv\). Finally \(P_nv\to v\) gives

\[
V_t=\Delta^{it}\quad\text{on }H_\varphi.
\tag{KM.24}
\]

Comparing their bounded implementers in (KM.10) and (KM.5), and using faithfulness of \(\pi_\varphi\), proves \(\beta_t=\sigma_t^\varphi\) for every real \(t\). The argument used bounded spectral bands of the already known modular operator; it did not replace \(M\) or \(\varphi\) by sigma-finite corners. \(\square\)

Combining KM-02 and KM-05 proves the full existence and uniqueness statement: every faithful normal semifinite weight has exactly one automorphism group satisfying (KM.3). This is its **modular automorphism group**. Its bounded strip functions are often called its two-point functions.

## Coordinate changes and positive scalar multiples

Let \(\theta:N\to M\) be a *-isomorphism of von Neumann algebras, let \(c>0\), and set \(\psi=c\,\varphi\circ\theta\) on \(N_+\). Then

\[
\sigma_t^\psi=\theta^{-1}\circ\sigma_t^\varphi\circ\theta.
\tag{KM.25}
\]

In particular multiplying a faithful normal semifinite weight by a positive finite scalar does not change its modular group.

**Proof.** WT-02–03 prove that \(\psi\) is faithful, normal and semifinite and that \(\theta\) bijects all the finite domains. Define the group on the right of (KM.25) to be \(\gamma_t\). For \(a\in N_+\), weight invariance gives

\[
\psi(\gamma_t(a))=c\,\varphi(\sigma_t^\varphi(\theta(a)))
=c\,\varphi(\theta(a))=\psi(a),
\]

including the value \(+\infty\). If \(x,y\in\mathfrak a_\psi\), let

\[
H_{x,y}(z)=c\,F^\varphi_{\theta(x),\theta(y)}(z).
\tag{KM.26}
\]

It has exactly the two boundary values required by (KM.3) for \(\gamma\) and \(\psi\), since \(\theta\) preserves multiplication and the finite linear extension. KM-05 applied to \(\psi\) proves (KM.25). This supplies a proof even when the isomorphism is presented abstractly rather than by a unitary on a common Hilbert space. \(\square\)

There is also an exact relation between the GNS polar data. The inverse-direction unitary of WT-05 is

\[
W:H_\psi\longrightarrow H_\varphi,
\qquad W\Lambda_\psi(x)=\sqrt c\,\Lambda_\varphi(\theta(x)).
\tag{KM.27}
\]

It maps the finite-star graph cores onto each other. Because \(\sqrt c\) is real and \(\theta(x^*)=\theta(x)^*\), it intertwines the initial antilinear involutions. Passing to their closures and using polar uniqueness gives, with the domains transported by \(W\),

\[
WS_\psi W^*=S_\varphi,\qquad
WJ_\psi W^*=J_\varphi,\qquad
W\Delta_\psi W^*=\Delta_\varphi.
\tag{KM.28}
\]

Thus equality of modular groups under scalar rescaling is consistent with the change in the GNS norm; the square-root normalization in (KM.27) accounts for that change.

## The same condition on a C*-algebra and its time convention

The boundary condition itself makes sense beyond faithful normal semifinite weights. Let \(A\) be a C*-algebra, possibly nonunital, and let \(\omega:A_+\to[0,\infty]\) be a lower semicontinuous weight. Here lower semicontinuity means that every set \(\{a\in A_+:\omega(a)\leq C\}\), for finite real \(C\), is norm closed. Form \(\mathfrak n_\omega\), \(\mathfrak m_\omega\), and \(\mathfrak a_\omega\) as in (KM.1), using \(A\) in place of \(M\).

For a group \(\gamma_t\) of *-automorphisms of \(A\), the modular KMS condition consists of invariance on all of \(A_+\) and the bounded strip condition (KM.3) for all \(x,y\in\mathfrak a_\omega\). No faithfulness, semifiniteness or normal extension is part of this definition. The finite-domain Cauchy–Schwarz inequality still proves that both boundary products and the bound (KM.4) are meaningful. If the phrase C*-dynamical system is used, we additionally require \(t\mapsto\gamma_t(a)\) to be norm continuous for each \(a\in A\); the boundary condition can be stated without that additional terminology.

Here is the sign and scale when a physical time evolution \(\alpha_t\) is fixed. For a state \(\omega\) and an inverse temperature \(b>0\), define its KMS condition relative to \(\alpha\) by requiring the modular condition for

\[
\gamma_t=\alpha_{-bt}.
\tag{KM.29}
\]

Equivalently, \(\omega\) is invariant under \(\alpha\) and, for every \(a,d\in A\), there is a bounded continuous function on \(0\leq\operatorname{Im}z\leq b\), holomorphic inside, whose boundaries are

\[
G_{a,d}(t)=\omega(a\alpha_t(d)),\qquad
G_{a,d}(t+ib)=\omega(\alpha_t(d)a).
\tag{KM.30}
\]

Indeed, the transformation

\[
G_{a,d}(z)=F^\gamma_{d,a}(-z/b+i)
\tag{KM.31}
\]

is an affine holomorphic change of variable taking one closed strip onto the other and interchanging its boundary lines. Substitution verifies (KM.30); the inverse change gives the converse. The state is finite everywhere, so its finite-star algebra is all of \(A\). In the convention of (KM.3), the modular group itself corresponds to inverse temperature \(-1\); equation (KM.29) is the conversion to a positive inverse temperature for a separately named time evolution.

KM-05 does not claim uniqueness in the generality of this definition. For example, the zero weight on \(M_2(\mathbb C)\) is invariant and has zero two-point functions for every automorphism group, including all groups \(a\mapsto u_t a u_t^*\) for continuous unitary groups \(u_t\). Its lack of faithfulness removes the GNS faithfulness used at the end of KM-05. Lifting a faithful semifinite lower semicontinuous C*-weight to a normal weight on its GNS von Neumann algebra is a separate theorem, with its own closability and extension obligations.

## A block model with infinite mass and arbitrarily fast modular motion

Let \(I\) be any set, with no countability hypothesis. Choose \(\lambda_i\geq0\) for each \(i\in I\), and set

\[
M=\prod_{i\in I}M_2(\mathbb C),\qquad
h_i=\begin{pmatrix}1&0\\0&e^{\lambda_i}\end{pmatrix},\qquad
\varphi(a)=\sum_{i\in I}\operatorname{Tr}(h_i a_i)\quad(a\in M_+).
\tag{KM.32}
\]

The positive sum means the supremum of its sums over finite subsets of \(I\). It defines a faithful normal semifinite weight. Additivity follows by taking a common finite subset approximating the two positive sums; homogeneity is immediate. Faithfulness follows from invertibility of each positive \(h_i\). For a bounded increasing positive net, each finite block sum preserves its supremum by finite-dimensional continuity. The two suprema, over the original net and over finite subsets of \(I\), commute because both are the supremum over their product set. This proves normality for arbitrary nets. Finite central block cuts \(p_Fa\), where \(F\subset I\) is finite, have finite weight and increase strongly to \(a\), proving semifiniteness. If \(I\) is infinite, \(\varphi(1)=+\infty\).

The GNS realization is

\[
H_\varphi=\bigoplus_{i\in I}\operatorname{HS}(\mathbb C^2),\qquad
\Lambda_\varphi(x)=(x_i h_i^{1/2})_i,
\qquad \pi_\varphi(a)(Z_i)_i=(a_iZ_i)_i.
\tag{KM.33}
\]

The Hilbert–Schmidt inner product is \(\operatorname{Tr}(W^*Z)\). Formula (KM.33) is isometric by (KM.2), and it has dense range because it contains every finitely supported family of matrices. On each such block the antilinear involution is

\[
S_i Z=h_i^{-1/2}Z^*h_i^{1/2},
\quad J_iZ=Z^*,
\quad \Delta_iZ=h_iZh_i^{-1}.
\tag{KM.34}
\]

The direct sum of the \(S_i\) has domain \(\{Z:\sum_i\|S_iZ_i\|_2^2<\infty\}\). It is closed because convergence of a vector and its image implies the corresponding identities on every finite-dimensional block. Finite block truncations converge in its graph norm and belong to the initial finite-star algebra. Conversely, for every \(x\in\mathfrak a_\varphi\), the vector \(Z=\Lambda_\varphi(x)\) belongs to that direct-sum domain, with image \(\Lambda_\varphi(x^*)\). These two inclusions identify its closure with the GNS involution. Thus (KM.34) determines the full modular polar data, with the direct-sum spectral domains of SK.

Theorem KM-05 now identifies the unique KMS group explicitly:

\[
(\sigma_t^\varphi(a))_i=h_i^{it}a_i h_i^{-it}.
\tag{KM.35}
\]

For the upper off-diagonal matrix unit \(e_{12}^{(i)}\),

\[
\sigma_t^\varphi(e_{12}^{(i)})=e^{-it\lambda_i}e_{12}^{(i)}.
\tag{KM.36}
\]

For instance, choose distinct indices \(i_n\) with \(\lambda_{i_n}\to\infty\), and let \(a_i=e_{12}\) for every \(i\). At \(t_n=\pi/\lambda_{i_n}\),

\[
\|\sigma_{t_n}^\varphi(a)-a\|=2.
\tag{KM.37}
\]

Thus a modular orbit need not be norm continuous, although KM-03 guarantees pointwise sigma-strong* continuity. The group still satisfies the strip condition on its precise finite-star domain. There is no contradiction: a bounded two-point function tests finite weight products, not the operator norm of every orbit.

## Three exercises with solutions

**Problem 1: detect the sign on a single block.** In (KM.32) take one index, \(\lambda>0\), \(x=e_{12}\) and \(y=e_{21}\). Compute the KMS function, verify its two boundaries, and decide whether the reversed group \(\sigma_{-t}^\varphi\) satisfies the same modular condition for \(\varphi\).

**Solution.** We have \(\varphi(e_{11})=1\), \(\varphi(e_{22})=e^\lambda\), and hence the unique function for the modular group is

\[
F_{x,y}(z)=e^{-i\lambda z}.
\tag{KM.38}
\]

It is bounded on the unit upper strip. The lower boundary is \(e^{-i\lambda t}\), while the upper boundary is \(e^\lambda e^{-i\lambda t}\), exactly as required. For the reversed group the lower boundary would be \(e^{i\lambda t}\). Boundary uniqueness forces the candidate \(e^{i\lambda z}\); at height one its coefficient is \(e^{-\lambda}\), whereas the required coefficient is \(e^\lambda\). They differ because \(\lambda>0\). Weight invariance alone therefore does not determine the sign.

**Problem 2: two finite ideals are really needed.** On \(B(\ell^2(\mathbb N_0))\), define the faithful normal semifinite weight

\[
\varphi(a)=\sum_{k=0}^{\infty}4^k\langle ae_k,e_k\rangle
\quad(a\geq0).
\tag{KM.39}
\]

Find a bounded rank-one \(x\) with \(x\in\mathfrak n_\varphi\) but \(x^*\notin\mathfrak n_\varphi\).

**Solution.** Put \(v=e_0\), \(u=\sum_{k\geq1}2^{-k}e_k\), and define \(x\xi=\langle\xi,v\rangle u\). Then

\[
x^*x=\|u\|^2|v\rangle\langle v|,
\qquad xx^*=|u\rangle\langle u|,
\]

so \(\varphi(x^*x)=\|u\|^2<\infty\) and
\(\varphi(xx^*)=\sum_{k\geq1}4^k4^{-k}=+\infty\).
The formula (KM.39) is a weight because it is a positive sum of vector functionals; it is normal by commuting the directed positive suprema and faithful because all diagonal coefficients of a positive zero-weight operator vanish. For semifiniteness, its finite-rank matrix units span a sigma-weakly dense subalgebra of \(\mathfrak m_\varphi\). Thus the example has the hypotheses of KM-01 and shows why replacing \(\mathfrak a_\varphi\) by \(\mathfrak n_\varphi\) in all boundary pairs would require a new assertion with new domains.

**Problem 3: the same group does not determine the weight.** Give two faithful normal semifinite weights which have equal modular groups but are not positive scalar multiples.

**Solution.** On \(M=\mathbb C\oplus\mathbb C\), take
\(\varphi(a,b)=a+b\) and \(\psi(a,b)=a+2b\) for positive \((a,b)\). Both are faithful finite weights. The identity group satisfies (KM.3) for each, since the algebra is commutative and the constant function \(F_{x,y}(z)=\varphi(xy)\), respectively \(\psi(xy)\), has both required boundaries. KM-05 makes both modular groups the identity. Their values on \((1,0)\) would force a common scalar to be one, but their values on \((0,1)\) then disagree. The uniqueness theorem fixes the group from a specified weight; it does not invert that assignment.

## What the characterization supplies next

The unit proves the full existence and uniqueness characterization for a faithful normal semifinite weight, exact transport under algebra isomorphisms and positive rescaling, and the broader C*-algebra definition with its time convention. Its continuity conclusion follows from the boundary condition itself. The proof passes through the full finite-star graph core and bounded spectral bands on the given GNS Hilbert space, so no countability reduction is hidden in the construction.

Three distinct next questions use this result. First, lifting a C*-weight requires proving a closed involution and comparing the lifted weight, not merely copying its scalar strip functions. Second, describing elements fixed by the modular group requires matching the fixed-point algebra to finite-domain trace identities. Third, comparing two different weights requires relative modular operators and weight cocycles. The present uniqueness proof can recognize a proposed automorphism group once its KMS condition has been established; it does not supply any of those additional constructions automatically.
