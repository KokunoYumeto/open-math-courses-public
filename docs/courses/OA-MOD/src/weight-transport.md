# Changing algebra coordinates and scaling a weight

**Self-checked by the writing AI.**

The exact order prerequisites and the weighted-space completeness argument were added and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026, CC0.

A weight can be transported without constructing a modular operator. The essential data are an algebra isomorphism and a scalar: they determine the entire new weight, its finite and null domains, and an explicitly normalized map of GNS spaces. This unit proves those statements before considering any automorphism action.

## The transport convention

Let \(M\) and \(N\) be concrete unital von Neumann algebras on arbitrary complex Hilbert spaces. Let \(\theta:N\to M\) be a complex-linear *-isomorphism, and let \(\varphi:M_+\to[0,\infty]\) be a weight. For a real number \(c>0\), write

\[
\psi=c\,\theta^*\varphi,
\qquad
\psi(a)=c\,\varphi(\theta(a))\quad(a\in N_+).
\tag{WT.1}
\]

Thus the star on \(\theta^*\varphi\) means pullback by composition; it is not an operator adjoint. The weight moves opposite to the algebra map. Multiplication of \(+\infty\) by a strictly positive finite scalar leaves \(+\infty\). The separate case \(c=0\) uses \(0\cdot\infty=0\) and is treated in WT-08.

Use the finite cone \(F_\varphi\), finite left ideal \(\mathfrak n_\varphi\), finite algebra \(\mathfrak m_\varphi\), null ideal \(N_\varphi\), finite linear extension \(\widetilde\varphi\), and GNS triple from WG002–006. Inner products are linear in the first variable. Semifiniteness means ultraweak density of \(\mathfrak m_\varphi\); normality means preservation of arbitrary bounded increasing positive suprema.

The other inputs are the bounded support theorem BK06, the finite/null/support projections WS02–06, and the normal-map and isomorphism results NP04/06. The square-root and order facts needed here are proved in AC3–4; their self-adjoint calculus covers every positive element of either algebra. The exact Hilbert and concrete-predual foundations are retained. No abstract realization theorem, standard form or modular theorem is used here.

## What an algebra isomorphism preserves

**Proposition.** The map \(\theta\) and its inverse are unital, isometric, positive, normal, and ultraweak homeomorphisms. They are also homeomorphisms for the sigma-strong and sigma-strong* topologies. They preserve positive suprema and support projections:

\[
a_i\uparrow a\ \Longrightarrow\ \theta(a_i)\uparrow\theta(a),
\qquad
s(\theta(a))=\theta(s(a))\quad(a\in N_+).
\tag{WT.2}
\]

No normality assumption in addition to *-isomorphism is needed for these concrete von Neumann algebras.

**Proof.** Surjectivity makes \(\theta(1_N)\) act as an identity on every element of \(M\), so it is \(1_M\). The inverse is unital for the same reason. The positive cone, its square-root factorization and its norm bounds are supplied by AC4. If \(a\geq0\), square-root factorization gives
\(\theta(a)=\theta(a^{1/2})^*\theta(a^{1/2})\geq0\).
Applying positivity to \(x^*x\leq\|x\|^2 1_N\) gives
\(\|\theta(x)\|\leq\|x\|\); here AC4 bounds the norm of the positive image and the C*-identity takes its square root. The inverse gives equality. Consequently the maps are order isomorphisms on the self-adjoint parts.

If \(a\) is the supremum of the given positive net, \(\theta(a)\) is an upper bound for its image. Any other self-adjoint upper bound \(b\) pulls back to an upper bound \(\theta^{-1}(b)\) for the original net. Hence \(b\geq\theta(a)\). This proves preservation of suprema for the original arbitrary directed set. NP-04 now gives normality and ultraweak continuity in both directions. For \(\omega\in M_*^+\), the positive preadjoint identity gives

\[
p_\omega(\theta(x))^2
=\omega(\theta(x^*x))
=p_{\omega\circ\theta}(x)^2.
\]

The pulled-back functional belongs to \(N_*^+\), so this proves sigma-strong continuity; applying it to \(x^*\) proves sigma-strong* continuity. The inverse has the same properties.

Finally \(s(a)\) is the least projection \(q\) with \(qa=a\), by BK-06. The maps \(\theta\) and \(\theta^{-1}\) biject projections, preserve their order, and preserve this multiplication identity. They therefore carry that least projection to the least projection fixing \(\theta(a)\). This is the support formula. \(\square\)

An arbitrary strongly convergent net need not have a common norm bound. We have not used unrestricted continuity for the strong operator topology. Ultraweak or sigma-strong continuity is sufficient for the domain arguments below.

## The weight and every finite domain

**Theorem.** Formula (WT.1) defines a weight on all of \(N_+\). For \(c>0\),

\[
F_\psi=\theta^{-1}(F_\varphi),\quad
\mathfrak n_\psi=\theta^{-1}(\mathfrak n_\varphi),\quad
N_\psi=\theta^{-1}(N_\varphi),\quad
\mathfrak m_\psi=\theta^{-1}(\mathfrak m_\varphi).
\tag{WT.3}
\]

On the finite algebra,

\[
\widetilde\psi(z)=c\,\widetilde\varphi(\theta(z)).
\tag{WT.4}
\]

Moreover \(\psi\) is normal, semifinite, or faithful if and only if \(\varphi\) has the respective property. These are three separate equivalences, with no assumption that either of the other properties holds.

**Proof.** Positivity and linearity of \(\theta\), followed by the weight axioms and distributivity of positive finite scaling over nonnegative extended sums, give

\[
\psi(a+b)=\psi(a)+\psi(b),\qquad
\psi(t a)=t\psi(a)\quad(t\geq0),\qquad \psi(0)=0.
\]

For \(t=0\) the homogeneity equation uses the stated convention at infinity. For \(t>0\) it is the usual extended-positive identity. No finite-value restriction has been imposed on these equations.

Strictly positive scaling preserves finiteness and vanishing of a nonnegative extended value. This proves the finite-cone equality, and the identity
\(\theta(x)^*\theta(x)=\theta(x^*x)\)
proves the finite-left-ideal and null-ideal equalities. The finite-algebra equality follows by applying \(\theta\) to its spanning products and using surjectivity between the two finite left ideals. The right side of (WT.4) is a positive linear extension agreeing with \(\psi\) on its finite cone; uniqueness in WG-004 proves (WT.4).

For normality, use (WT.2) and

\[
c\sup_i t_i=\sup_i ct_i\qquad(0\leq t_i\leq+\infty).
\]

If the supremum is finite, this is scalar order continuity; if it is infinite, the scaled values exceed every finite bound. Thus a normal \(\varphi\) makes \(\psi\) normal. Apply the same argument to
\(\varphi=c^{-1}\psi\circ\theta^{-1}\)
for the reverse implication. Ultraweak homeomorphism and (WT.3) show that the finite algebra is dense on one side exactly when it is dense on the other, proving the semifiniteness equivalence. Finally
\(\psi(a)=0\) is equivalent to \(\varphi(\theta(a))=0\), and \(a=0\) is equivalent to \(\theta(a)=0\). This proves faithfulness in both directions. \(\square\)

For fixed \(c>0\) and \(\theta\), this is also an order isomorphism between the cones of all weights: a pointwise inequality transports in both directions, and addition and positive scaling commute with transport on the entire positive cone. Its inverse is pullback by \(\theta^{-1}\) followed by scaling by \(c^{-1}\). These assertions include weights taking only the values zero and infinity.

## Finite, null and support projections

For every weight use the finite-domain projection \(e_\varphi\) of WS-02, characterized by
\(\overline{\mathfrak n_\varphi}^{\mathrm{ultraweak}}=Me_\varphi\).
For a normal weight also use its largest null projection \(f_\varphi\), effective support \(p_\varphi=e_\varphi-f_\varphi\), and null carrier \(r_\varphi=1-f_\varphi\).

**Theorem.** For arbitrary \(\varphi\),

\[
e_\psi=\theta^{-1}(e_\varphi).
\tag{WT.5}
\]

If \(\varphi\) is normal, then

\[
f_\psi=\theta^{-1}(f_\varphi),\qquad
p_\psi=\theta^{-1}(p_\varphi),\qquad
r_\psi=\theta^{-1}(r_\varphi).
\tag{WT.6}
\]

The support restrictions are transported by the restricted *-isomorphism:

\[
\psi|_{p_\psi Np_\psi}
=c\,\bigl(\varphi|_{p_\varphi Mp_\varphi}\bigr)
\circ\theta|_{p_\psi Np_\psi}.
\tag{WT.7}
\]

All weight equations in this item are equations on their entire positive cones.

**Proof.** Taking ultraweak closures in (WT.3), using the homeomorphism from WT-02, gives

\[
\overline{\mathfrak n_\psi}^{\mathrm{ultraweak}}
=\theta^{-1}(Me_\varphi)
=N\theta^{-1}(e_\varphi).
\]

The uniqueness statement in WS-02 proves (WT.5). Normality on one side is equivalent to normality on the other. Among projections, the equality \(\psi(q)=0\) holds exactly when \(\varphi(\theta(q))=0\). A bijection preserving the projection order therefore carries the largest null projection to the largest null projection, proving the first formula of (WT.6). Subtraction and the identity-preserving property give the other two formulas.

The map \(\theta\) carries the support corner onto the support corner, so (WT.7) is the restriction of the defining weight identity. More explicitly, WS-06 gives for every \(a\in N_+\)

\[
\psi(a)=
\begin{cases}
c\,\varphi_{p_\varphi}\bigl(\theta(p_\psi a p_\psi)\bigr),
  &a=e_\psi a e_\psi,\\
+\infty,&a\ne e_\psi a e_\psi.
\end{cases}
\tag{WT.8}
\]

Indeed the first condition is equivalent to \(\theta(a)=e_\varphi\theta(a)e_\varphi\), and the two compression expressions agree by multiplicativity. The first line permits an infinite value. This proves the reconstruction formula without subtracting infinite numbers. \(\square\)

For normal semifinite weights, \(e=1\) and \(p=r\), so (WT.8) reduces to the usual faithful support-corner formula. For arbitrary normal weights, the projections \(p\) and \(r\) still record different information and must not be identified during transport.

## GNS transport and the square-root scalar

Fix one GNS triple for each weight. The following construction is determined by its action on the dense GNS ranges, independently of the concrete representation originally used for the algebras. The completion, extension and adjoint results used below are proved in BK01.

**Theorem.** There is a unique bounded bijection

\[
A_{\theta,c}^{\varphi}:H_\varphi\longrightarrow H_\psi,
\qquad
A_{\theta,c}^{\varphi}\Lambda_\varphi(y)
=\Lambda_\psi(\theta^{-1}(y))
\quad(y\in\mathfrak n_\varphi).
\tag{WT.9}
\]

It satisfies

\[
\langle A_{\theta,c}^{\varphi}\xi,A_{\theta,c}^{\varphi}\eta\rangle
=c\langle\xi,\eta\rangle.
\tag{WT.10}
\]

Consequently

\[
B_{\theta,c}^{\varphi}=c^{-1/2}A_{\theta,c}^{\varphi}
\tag{WT.11}
\]

is unitary. If \(H_\varphi\ne\{0\}\), the exact norms of \(A\) and \(A^{-1}\) are \(\sqrt c\) and \(c^{-1/2}\). If \(H_\varphi=\{0\}\), both spaces are zero and both operator norms are zero.

The inverse-direction unitary \(U=(B_{\theta,c}^{\varphi})^*:H_\psi\to H_\varphi\) is characterized by

\[
U\Lambda_\psi(x)=\sqrt c\,\Lambda_\varphi(\theta(x)),
\qquad
U\pi_\psi(b)U^*=\pi_\varphi(\theta(b)).
\tag{WT.12}
\]

**Proof.** The null-ideal equality in (WT.3) proves representative independence of the assignment in (WT.9). Linearity follows from the linear GNS maps and the linearity of \(\theta^{-1}\). For \(y,z\in\mathfrak n_\varphi\), the finite linear-extension formula gives

\[
\begin{aligned}
\langle\Lambda_\psi(\theta^{-1}(y)),
       \Lambda_\psi(\theta^{-1}(z))\rangle
&=\widetilde\psi\bigl(\theta^{-1}(z)^*\theta^{-1}(y)\bigr)\\
&=c\,\widetilde\varphi(z^*y).
\end{aligned}
\]

Thus the map extends continuously to the completion and satisfies (WT.10). After normalization it is an isometry. Its range contains a dense scalar multiple of \(\Lambda_\psi(\mathfrak n_\psi)\), because \(\theta^{-1}\) maps the finite left ideals onto one another. The range of an isometry from a complete space is closed: the preimages of a convergent sequence in its range are Cauchy. Therefore this range is the entire target, proving unitarity and bijectivity. Density proves uniqueness. Equation (WT.10) gives the stated exact norms whenever there is a unit vector to test; the zero-space convention gives the remaining case.

For \(a\in M\) and \(y\in\mathfrak n_\varphi\), the left-ideal property makes all terms in

\[
A_{\theta,c}^{\varphi}\pi_\varphi(a)\Lambda_\varphi(y)
=\Lambda_\psi(\theta^{-1}(a)\theta^{-1}(y))
=\pi_\psi(\theta^{-1}(a))A_{\theta,c}^{\varphi}\Lambda_\varphi(y)
\]

legitimate. Boundedness and density extend this intertwining equality. Normalization leaves it unchanged. The formula for \(U\) follows by applying the inverse to the dense-range identity for \(B\); conjugating the intertwining identity gives (WT.12). \(\square\)

These maps are between the GNS spaces of the explicitly related weights. They do not identify different weights with cone vectors in a single standard Hilbert space. In particular, there is no use of \(\Lambda_\varphi(1)\) when \(\varphi(1)=\infty\).

## Composition, with all arrows visible

Let \(\kappa:P\to N\) be another *-isomorphism and let \(d>0\). Set

\[
\psi=c\varphi\circ\theta,
\qquad \chi=d\psi\circ\kappa
=cd\varphi\circ(\theta\circ\kappa).
\tag{WT.13}
\]

The last equality holds on all of \(P_+\), including infinite values. With the fixed triples of WT-05,

\[
A_{\kappa,d}^{\psi}A_{\theta,c}^{\varphi}
=A_{\theta\circ\kappa,cd}^{\varphi},
\qquad
B_{\kappa,d}^{\psi}B_{\theta,c}^{\varphi}
=B_{\theta\circ\kappa,cd}^{\varphi}.
\tag{WT.14}
\]

The maps go successively from \(H_\varphi\) to \(H_\psi\) to \(H_\chi\).

**Proof.** Evaluate the first composite on \(\Lambda_\varphi(y)\). It produces

\[
\Lambda_\chi\bigl(\kappa^{-1}(\theta^{-1}(y))\bigr)
=\Lambda_\chi\bigl((\theta\circ\kappa)^{-1}(y)\bigr).
\]

All domains match by (WT.3), so this is exactly the defining value of the right side. Density proves equality of the bounded maps. Multiplying by the two normalization scalars gives the second equality, since \(c^{-1/2}d^{-1/2}=(cd)^{-1/2}\). For identity transport the maps are the identity on a dense range and hence everywhere. Taking \(\kappa=\theta^{-1}\), \(d=c^{-1}\), gives the inverse transport. In particular

\[
\bigl(B_{\theta,c}^{\varphi}\bigr)^*
=B_{\theta^{-1},c^{-1}}^{\psi}.
\]

This also holds on zero Hilbert spaces. \(\square\)

Composition in (WT.14) is a statement about specified GNS triples. If different choices of triples are made, the unique GNS unitaries of WG-006 conjugate these identities to the new choices.

## Automorphisms and a weight scaled by an action

Every automorphism \(\beta\) of a concrete von Neumann algebra is a special case of WT-02. In particular,

\[
\varphi\text{ normal, semifinite and faithful}
\quad\Longrightarrow\quad
\varphi\circ\beta\text{ normal, semifinite and faithful}.
\tag{WT.15}
\]

There is no innerness or weight-invariance assumption on \(\beta\).

A distinct useful situation keeps the GNS space fixed. Suppose \(\varphi\circ\beta=c\varphi\) for a specified \(c>0\). Then \(\beta\) bijects the finite left ideal and its null ideal with themselves. The rule

\[
L_\beta\Lambda_\varphi(x)=\Lambda_\varphi(\beta(x))
\]

is well defined and satisfies
\(\|L_\beta\xi\|=\sqrt c\,\|\xi\|\).
Its inverse is obtained from \(\beta^{-1}\), because
\(\varphi\circ\beta^{-1}=c^{-1}\varphi\).
Thus

\[
V_\beta=c^{-1/2}L_\beta
\quad\text{is unitary},\qquad
V_\beta\pi_\varphi(a)V_\beta^*=\pi_\varphi(\beta(a)).
\tag{WT.16}
\]

The proof is the same dense-domain inner-product and left-action calculation as WT-05, with the stated weight equality supplying the scalar factor. Explicitly,
\(L_\beta\pi_\varphi(a)\Lambda_\varphi(x)
=\Lambda_\varphi(\beta(a)\beta(x))
=\pi_\varphi(\beta(a))L_\beta\Lambda_\varphi(x)\);
density proves the operator equation.

Suppose a group acts algebraically by \(\alpha_{st}=\alpha_s\alpha_t\), and
\(\varphi\circ\alpha_s=c_s\varphi\), \(c_s>0\).
If \(H_\varphi\ne\{0\}\), there is \(a\in M_+\) with \(0<\varphi(a)<\infty\): take \(a=x^*x\) for a nonzero GNS vector. Evaluate

\[
\varphi\circ\alpha_{st}
=(\varphi\circ\alpha_s)\circ\alpha_t
=c_sc_t\varphi
\]

at this element to obtain \(c_{st}=c_sc_t\), and similarly \(c_e=1\). Therefore the normalization in (WT.16) gives
\(V_sV_t=V_{st}\) on dense GNS vectors and hence everywhere. If \(H_\varphi=\{0\}\), there is only one unitary on that space and its group law holds without determining the scalars. No continuity in the group parameter has been claimed. A continuous canonical implementation on a standard form is a separate theorem.

## Zero scaling and zero Hilbert spaces

For any weight, including a nonnormal one, the convention \(0\cdot\infty=0\) makes \(0\varphi\) the zero weight. Its finite cone is all of \(M_+\), all three ideals \(\mathfrak n,\mathfrak m,N\) are \(M\), and its GNS Hilbert space is zero. It is normal and semifinite. It is faithful exactly when \(M\) is the zero algebra.

For this zero weight, WS gives

\[
e=f=1,\qquad p=r=0.
\]

Indeed every element is finite and every projection is null. Thus setting \(c=0\) in the domain, inverse or support formulas of WT-03–06 is not permitted. For example, positive scaling preserves the domain of the everywhere-infinite-off-zero weight, whereas zero scaling changes that domain from \(\{0\}\) to \(M\).

More generally,

\[
H_\varphi=\{0\}
\quad\Longleftrightarrow\quad
\varphi(a)\in\{0,+\infty\}\quad(a\in M_+).
\tag{WT.17}
\]

If the Hilbert space is zero and \(\varphi(a)<\infty\), then the square root supplied by AC4 satisfies \(a^{1/2}\in\mathfrak n_\varphi\) and
\(\varphi(a)=\|\Lambda_\varphi(a^{1/2})\|^2=0\).
Conversely, if every finite value is zero, every GNS vector has zero norm, so its completion is zero. Such a weight is unchanged by every strictly positive scalar. This is why a scaling constant cannot in general be recovered from equality of weights, and why the exact operator norm in WT-05 explicitly distinguishes the zero Hilbert space.

## A coordinate model with infinite coefficients

Let \(I\) be any set and choose coefficients \(w_i\in[0,+\infty]\). On the diagonal algebra \(\ell^\infty(I)\), define

\[
\varphi_w(a)=\sum_{i\in I}w_i a_i\qquad(a\geq0),
\tag{WT.18}
\]

where sums mean suprema of finite subsums and \(\infty\cdot0=0\). Finite unions of index sets prove additivity. For normality, each coordinate map followed by multiplication by \(w_i\) preserves increasing positive suprema, including \(w_i=\infty\): a positive limiting coordinate is eventually positive somewhere in the net. Commuting the finite-subset supremum with the original net supremum proves normality of (WT.18).

Write

\[
Z=\{i:w_i=0\},\quad P=\{i:0<w_i<\infty\},\quad
Q=\{i:w_i=\infty\}.
\]

The finite domain and projections are

\[
\mathfrak n_{\varphi_w}
=\left\{x\in\ell^\infty(I):x_i=0\ (i\in Q),\quad
               \sum_{i\in P}w_i|x_i|^2<\infty\right\},
\]

\[
e=1_{Z\cup P},\quad f=1_Z,\quad p=1_P,\quad r=1_{P\cup Q}.
\tag{WT.19}
\]

To check \(e\), every finite positive element vanishes on \(Q\), while the finite-coordinate projections in \(Z\cup P\) have finite weight and increase to \(1_{Z\cup P}\). The finite-domain closure characterization proves its formula. A positive element has weight zero exactly when it is supported on \(Z\); this gives the null projection and hence the remaining formulas. In particular the weight is semifinite exactly when \(Q\) is empty, and faithful exactly when \(Z\) is empty.

The GNS space is the weighted space \(\ell^2(P,w)\), with the GNS map given by restriction to \(P\). Its norm identity is (WT.18), null representatives differ only on \(Z\), and finite-support vectors prove density. No cardinality bound on \(I\) or \(P\) has entered the argument.

Here are the completeness and density details for this weighted space. Define its squared norm by the supremum of the finite sums of \(w_i|\xi_i|^2\). For each positive integer \(m\), only finitely many summands can be at least \(1/m\); otherwise finite subsums would be arbitrarily large. Thus every such vector has countable support. Finite Cauchy–Schwarz shows that the weighted inner-product series is absolutely convergent. The finite sums define a genuine inner product since every \(w_i\), for \(i\in P\), is finite and strictly positive. Given a finite norm sum and \(\varepsilon>0\), choose a finite set whose subsum is within \(\varepsilon^2\) of its supremum. The remaining tail then has norm at most \(\varepsilon\), which proves density of finite truncations.

For completeness, let \((\xi^{(n)})\) be a Cauchy sequence in this norm. Each coordinate is Cauchy because its absolute difference is bounded by the norm difference divided by \(\sqrt{w_i}\); write its limit as \(\xi_i\). Given \(\varepsilon>0\), choose \(N\) so that all norm differences after \(N\) are at most \(\varepsilon\). For fixed \(n\geq N\), take the coordinate limit of the other sequence index in any finite sum to obtain

\[
 \sum_{i\in F}w_i|\xi_i^{(n)}-\xi_i|^2
 \leq\varepsilon^2.
\]

Taking the supremum over finite \(F\) gives the same norm bound. The finite-dimensional triangle inequality then bounds the norm of \(\xi\) by the norm of \(\xi^{(n)}\) plus \(\varepsilon\), so the limit belongs to the weighted space and the sequence converges there. This proves completeness. Finally every finite-support family on \(P\), extended by zero to \(I\), is a bounded element of the finite left ideal. Its GNS image is that family. The preceding density and norm identity therefore identify the GNS completion with the entire weighted space, for arbitrary \(P\).

Let \(\gamma:I\to J\) be a bijection and define \(\theta:\ell^\infty(J)\to\ell^\infty(I)\) by \(\theta(a)_i=a_{\gamma(i)}\). Reindexing finite subsets gives on every positive element

\[
c\varphi_w\circ\theta=\varphi_v,
\qquad v_j=cw_{\gamma^{-1}(j)}.
\tag{WT.20}
\]

The finite, null and support sets are therefore the images under \(\gamma\) of their old sets. The map \(A_{\theta,c}^{\varphi_w}\) sends coordinates \(\xi_i\) to \(\eta_j=\xi_{\gamma^{-1}(j)}\), with squared norm multiplied by \(c\). Its unitary normalization is \(c^{-1/2}\) times this reindexing map. This checks both the direction of the inverse coordinate map and the square-root normalization, including infinite-weight and null coordinates.

## Why an arbitrary normal homomorphism is insufficient

Pullback through a normal *-homomorphism still defines a normal weight when the original weight is normal: the homomorphism is positive and preserves the required bounded increasing suprema. The isomorphism hypothesis was used for the converse assertions, surjectivity between finite domains, and transport of semifiniteness and faithfulness. Two examples show concrete failures.

**An injective, unital normal map can lose semifiniteness.** Take the counting weight \(\varphi\) on \(\ell^\infty(\mathbb N)\). It is normal, semifinite and faithful by the finite-coordinate argument in WT-09. Let

\[
\iota:\mathbb C\longrightarrow\ell^\infty(\mathbb N),
\qquad \iota(z)=(z,z,\ldots).
\]

This is a unital injective *-homomorphism. It preserves bounded increasing positive suprema coordinatewise, so NP-04 makes it normal. But

\[
(\varphi\circ\iota)(t)=
\begin{cases}0,&t=0,\\+\infty,&t>0,\end{cases}
\qquad(t\geq0).
\]

Its finite algebra is zero, so it is not semifinite on \(\mathbb C\). Its GNS space is zero whereas \(H_\varphi=\ell^2(\mathbb N)\). There can be no GNS unitary of the isomorphism type above. Injectivity and normality alone have not transported finite-domain density.

**A surjective normal map can lose faithfulness.** Let
\(q:\mathbb C^2\to\mathbb C\), \(q(z_1,z_2)=z_1\), and let \(\tau(t)=t\) for \(t\geq0\). The map is a unital surjective normal *-homomorphism, and \(\tau\) is a faithful finite normal weight. Its pullback is
\((\tau\circ q)(a_1,a_2)=a_1\), which vanishes on the nonzero positive projection \((0,1)\). It is finite and normal but not faithful. These examples keep the two losses distinct.

## Exercises with complete solutions

**1. Move a noncentral finite domain.** In \(M_2(\mathbb C)\), let \(e=E_{11}\) and define

\[
\varphi(a)=
\begin{cases}a_{11},&a=eae,\\+\infty,&a\ne eae,\end{cases}
\qquad a\geq0.
\]

Let \(Q\) swap the two coordinate vectors, \(\beta(x)=QxQ^*\), and \(\psi=4\varphi\circ\beta\). Compute the projection data and both maps in WT-05.

**Solution.** The positive cone supported on \(e\) is hereditary, and a positive sum is supported there exactly when both summands are. This proves the weight axioms using the finite coordinate functional on that corner and infinity outside it. For an increasing positive net, a supremum outside the corner requires a member outside it, by bounded monotone convergence in BK04 and closedness of the corner. If the supremum is in the corner, every member is in the corner and the scalar functional preserves the supremum. Thus the weight is normal. It is faithful, with finite projection \(e\), null projection zero, effective support \(e\), and null carrier one.

The new weight is finite exactly on the \(E_{22}\) corner, with value \(4a_{22}\) there. Thus
\(e_\psi=p_\psi=E_{22}\), \(f_\psi=0\), \(r_\psi=1\).
For \(\varphi\), the left ideal consists of matrices \(x=xe\), and its GNS identification is \(\Lambda_\varphi(x)=xe_1\in\mathbb C^2\). For \(\psi\), use \(\Lambda_\psi(x)=2xe_2\) on \(x=xE_{22}\). Both maps have dense, indeed onto, ranges. Since \(\beta^{-1}=\beta\), formula (WT.9) gives \(A\xi=2Q\xi\), while \(B\xi=Q\xi\). Their norms are two and one. The inverse-direction unitary is also \(Q\), agreeing with (WT.12). Values outside the finite corners remain infinite throughout.

**2. Recover or fail to recover the scalar.** Suppose \(a,b>0\) and \(a\varphi=b\varphi\). Prove that \(a=b\) whenever \(H_\varphi\ne\{0\}\), and characterize the case in which every positive scalar gives the same weight.

**Solution.** A nonzero GNS space contains a nonzero dense-range vector, so some \(x\in\mathfrak n_\varphi\) has \(0<\varphi(x^*x)<\infty\). Evaluating the weight equality at \(x^*x\) allows division by this finite positive number and gives \(a=b\). If \(H_\varphi=\{0\}\), (WT.17) says all values are zero or infinity; every positive scaling fixes both. Conversely, if every positive scaling fixes the weight, a finite strictly positive value would give a contradiction by comparing scalars one and two. Equation (WT.17) then gives the zero Hilbert space. This proves the characterization without equating faithfulness of a weight with nontriviality of its GNS space.

**3. Transport a finite cutoff net.** Let \(\varphi\) be semifinite, and let \((u_i)\) be increasing finite positive contractions with supremum \(1_M\). For \(\psi=c\varphi\circ\theta\), prove directly that \(\theta^{-1}(u_i)\) is such a net for \(\psi\). If the weights are normal and \(y\in\mathfrak n_\varphi\), compare the corresponding GNS cutoff errors.

**Solution.** Positivity, isometry and order preservation give increasing positive contractions with supremum \(1_N\). Their weights are \(c\varphi(u_i)<\infty\). This proves the cutoff assertion even without normality. Put \(x=\theta^{-1}(y)\) and \(v_i=\theta^{-1}(u_i)\). Formula (WT.10) gives

\[
\|\Lambda_\psi(x-v_ix)\|^2
=c\,\|\Lambda_\varphi(y-u_iy)\|^2.
\]

The arguments lie in their finite left ideals by WG-003. Under normality, WG-009 makes the right side tend to zero along the original directed set, proving the transported Hilbert-norm convergence. No sequence or finite projection approximation is required.

## Exact use in later weight theory

WT-03 and WT-07 supply the automorphism-pullback preservation clause needed in **OA-FLOW.AWC.IMPORT.WEIGHTS**: every normal automorphism carries a normal semifinite faithful weight to another weight with those three properties. The theorem here also covers isomorphisms between different algebras, arbitrary weights and strictly positive scaling, with all domains and infinite values retained. The underlying mathematical antecedents are the finite-domain and semicyclic GNS construction in Takesaki, *Theory of Operator Algebras II*, VII.1, as independently proved in WG, the support results independently proved in WS, and the bounded-map results of NP.

This is a partial match to that larger OA-FLOW contract. Tensor-product weights, their naturality on the entire positive cone, modular automorphisms, Connes derivatives and their scaling or naturality identities still require their own proofs. For example, \(c^{-1/2}\) in a GNS normalization does not by itself prove a modular-time factor \(c^{it}\). Likewise the maps between varying GNS spaces in WT-05 do not prove the continuous canonical implementation on a single standard form, or the common-standard-space relative GNS transport requested elsewhere. No fundamental modular theorem or general relative operator is inferred from this unit.
