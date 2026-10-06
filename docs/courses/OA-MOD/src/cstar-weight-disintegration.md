# Separable GNS spaces and disintegration of C*-weights

**Self-checked by the writing AI.**

A separable C*-algebra can carry an unbounded weight whose finite domain is not norm dense. Its finite-weight GNS space is nevertheless separable when the weight is lower semicontinuous. We first prove this directly from a closed graph. We then prove uniqueness of modular weights from a common invariant finite algebra, and disintegrate a modular weight on the original C*-algebra. The last argument verifies both fibre semifiniteness and the onto property of the fibre GNS map.

The source antecedents are M. Takesaki, *Theory of Operator Algebras II*, VIII.4, Lemmas 4.9–4.10, Theorem 4.11 and Lemmas 4.12–4.13, printed 137–140/PDF 157–160. The complete governing page images were inspected. The statements and proofs below are independently written. Inner products are linear in the first variable. C*-semifiniteness means norm density of the finite domain, as in CS-01 and LW-08; it must not be replaced by von Neumann sigma-weak density.

WD-01–03 use CS's finite-domain construction, lower semicontinuity, Hahn–Banach separation of closed linear subspaces, and weak compactness of a Hilbert ball. WD-04–05 also use the positive approximate identity An approximate identity indexed by finite sets, Nondegeneracy on the finite-weight GNS space's nondegeneracy, The modular condition builds continuous GNS unitaries and The normal weight recovered from this algebra/05/07's modular normal extension and GNS identification, and Two identities on the full finite left ideal's full entire right multiplier formula. WD-06–09 use A countable contractive family detects every positive value and Recovering measurable GNS vectors by an injective equation/05/07 and the existing DI FIELD, CENTRAL and SELECTION contracts, including the still-open compatible GNS-field comparison MW-DEP-GNS-FIELD. These are the course's named inputs with their current statuses; no general measurable-field comparison is proved here.

## A lower-semicontinuous C*-weight has a closed GNS graph

Let \(A\) be any complex C*-algebra and \(\varphi:A_+\to[0,\infty]\) an additive, positively homogeneous, norm-lower-semicontinuous weight. No faithfulness, semifiniteness or separability is assumed. CS gives its finite left ideal \(\mathfrak n_\varphi\), Hilbert space \(H_\varphi\), and linear quotient map \(\Lambda_\varphi\). We claim that

\[
 \Gamma_\varphi
 =\{(x,\Lambda_\varphi(x)):x\in\mathfrak n_\varphi\}
 \subseteq A\oplus H_\varphi
 \tag{WD.1}
\]

is closed for the product norm.

Suppose \(x_k\to x\) in \(A\) and \(\Lambda_\varphi(x_k)\to\xi\) in Hilbert norm. Continuity of multiplication and lower semicontinuity give

\[
 \varphi(x^*x)
 \leq\liminf_k\varphi(x_k^*x_k)
 =\|\xi\|^2<\infty.
 \tag{WD.2}
\]

Thus \(x\in\mathfrak n_\varphi\). For fixed \(j\), apply lower semicontinuity to \((x_j-x_k)^*(x_j-x_k)\) as \(k\to\infty\):

\[
 \|\Lambda_\varphi(x_j)-\Lambda_\varphi(x)\|^2
 \leq\liminf_k
       \|\Lambda_\varphi(x_j)-\Lambda_\varphi(x_k)\|^2
 =\|\Lambda_\varphi(x_j)-\xi\|^2.
 \tag{WD.3}
\]

Letting \(j\to\infty\) proves \(\xi=\Lambda_\varphi(x)\). Metric closedness proves the claim for the whole product space, not only the chosen sequence. The graph is a linear subspace. Hahn–Banach therefore also makes it closed for the product weak topology: a continuous linear functional separating a point from this graph is a sum of a functional on \(A\) and one on \(H_\varphi\).

An especially useful consequence is the following bounded-energy limit rule. If \(x_k\to x\) in norm and \(\sup_k\|\Lambda_\varphi(x_k)\|<\infty\), then \(x\in\mathfrak n_\varphi\) by lower semicontinuity, and

\[
 \Lambda_\varphi(x_k)\longrightarrow\Lambda_\varphi(x)
 \quad\text{weakly in }H_\varphi.
 \tag{WD.4}
\]

Indeed, a bounded Hilbert ball is weakly compact. Every weakly convergent subnet, paired with the norm limit of its algebra entries, has a limit in the weakly closed graph and hence has the displayed unique limit. If weak convergence failed, a subnet staying outside some weak neighbourhood would have a cluster point in the compact ball, contradicting that uniqueness. This assertion does not give Hilbert-norm convergence.

## Separability without a dense finite domain

**Theorem.** If \(A\) is separable and \(\varphi\) is any norm-lower-semicontinuous weight, then \(H_\varphi\) is separable. The weight may be nonfaithful, nondensely defined, or zero; its GNS representation may have a kernel.

For each positive integer \(m\), set

\[
 F_m=\{x\in A:\varphi(x^*x)\leq m^2\}.
 \tag{WD.5}
\]

The norm topology of a separable metric space has a countable base; its restriction to any subset still has a countable base. Choosing a point in each nonempty restricted basic open set gives a countable norm-dense subset \(D_m\subseteq F_m\). This statement is about the inherited algebra norm, rather than the GNS graph norm. Define

\[
 L=\overline{\operatorname{span}_{\mathbb C}
       \{\Lambda_\varphi(d):d\in\bigcup_{m\geq1}D_m\}}
       ^{\,H_\varphi}.
 \tag{WD.6}
\]

This closed subspace is separable. If \(x\in F_m\), choose \(d_k\in D_m\) with \(d_k\to x\) in norm. Their GNS norms are at most \(m\). By (WD.4), \(\Lambda_\varphi(d_k)\to\Lambda_\varphi(x)\) weakly. A closed Hilbert subspace is weakly closed: its orthogonal complement tests membership. Consequently \(\Lambda_\varphi(x)\in L\).

Every finite GNS vector comes from an \(x\) in some \(F_m\). The defining density of \(\Lambda_\varphi(\mathfrak n_\varphi)\) now gives \(L=H_\varphi\). This proves separability of the semicyclic representation in the full generality of source Lemma 4.9, without first assuming a normal faithful extension or a single cyclic vector. The zero Hilbert space is included. \(\square\)

## Norm approximation with bounded energy need not be strong

Let \(A=c_0(\mathbb N)\), and for \(a\in A_+\) define

\[
 \varphi(a)=\sum_{j\geq1}j^2a_j.
 \tag{WD.7}
\]

The nonnegative series is additive and homogeneous, including infinite values. It is norm lower semicontinuous because it is the supremum of its continuous positive finite partial sums. Its finite domain contains the finitely supported sequences, so this particular weight is densely defined and faithful. Its GNS space is \(\ell^2\), with

\[
 \Lambda_\varphi(x)=(j x_j)_{j\geq1},\qquad
 \mathfrak n_\varphi
 =\{x\in c_0:\sum_j j^2|x_j|^2<\infty\}.
 \tag{WD.8}
\]

For \(x_n=n^{-1}e_n\),

\[
 \|x_n\|_A=n^{-1}\to0,\qquad
 \Lambda_\varphi(x_n)=e_n,\qquad
 \|\Lambda_\varphi(x_n)\|=1.
 \tag{WD.9}
\]

The last vectors converge weakly to zero because every \(\ell^2\) coordinate sequence tends to zero, but they do not converge to zero in norm. This is why WD-02 uses weak compactness and the weakly closed span. A claim that the chosen norm-dense \(D_m\) is already a graph core would not follow from that proof.

## An invariant finite algebra is a GNS graph core

Now let \(A\) be separable, let \(\alpha:\mathbb R\to\operatorname{Aut}(A)\) be pointwise norm continuous, and let \(\theta\) be faithful, norm-lower-semicontinuous and C*-semifinite, satisfying the modular condition for \(\alpha\). Suppose \(B\) is a norm-dense invariant *-subalgebra contained in \(\mathfrak n_\theta\cap\mathfrak n_\theta^*\). We prove that the graph of \(\Lambda_\theta|_B\) is norm dense in \(\Gamma_\theta\). The hypothesis \(B\subseteq\mathfrak m_\theta\) used in the source is stronger than this finite-adjoint hypothesis.

There is a positive contractive sequential approximate identity \((u_n)\) of \(A\): restrict BG-01's finite-set construction to the first \(n\) members of a fixed dense sequence, with its error parameter tending to zero. Choose \(b_n\in B\) approaching \(u_n^{1/2}\), then divide by \(\max(1,\|b_n\|)\). These are contractions in \(B\), and \(a_n=b_n^*b_n\) are positive contractions in \(B\) with \(\|a_n-u_n\|\to0\). Hence \((a_n)\) is another approximate identity, though it need not be increasing. Put

\[
 e_n=\pi^{-1/2}\int_{\mathbb R}e^{-t^2}\alpha_t(a_n)\,dt,
 \qquad
 \alpha_z(e_n)=\pi^{-1/2}\int_{\mathbb R}
                 e^{-(t-z)^2}\alpha_t(a_n)\,dt.
 \tag{WD.10}
\]

These are norm Bochner integrals in \(A\). The second formula is entire in \(z\), agrees with the real orbit, and obeys

\[
 0\leq e_n\leq1,\quad e_n=e_n^*,\qquad
 \|\alpha_z(e_n)\|\leq e^{(\operatorname{Im}z)^2}.
 \tag{WD.11}
\]

For every \(c\in A\) and every fixed \(z\in\mathbb C\),

\[
 \alpha_z(e_n)c\to c,\qquad
 c\alpha_z(e_n)\to c
 \quad\text{in norm}.
 \tag{WD.12}
\]

To prove this, the approximate identity converges uniformly on the compact norm orbit \(\{\alpha_{-t}(c):|t|\leq T\}\), by a finite-net argument and uniform boundedness. The complex Gaussian tail has an integrable bound independent of \(n\), while its total integral is one. First use the compact interval, then let its tail shrink. This proves both products. Nondegeneracy LW-01 and the uniform bound in (WD.11) imply

\[
 \pi_\theta(\alpha_z(e_n))\to I_{H_\theta}
 \quad\text{strongly}.
 \tag{WD.13}
\]

The same integral can be taken in the product Banach space \(A\oplus H_\theta\). Indeed, \(t\mapsto\Lambda_\theta(\alpha_t(a_n))\) is norm continuous by KL-02's GNS modular unitaries and has constant finite norm. Its finite Gaussian Riemann sums are graph pairs from \(B\), because \(\alpha_t(B)=B\). The closed graph WD-01 therefore gives

\[
 e_n\in\mathfrak n_\theta,\qquad
 \Lambda_\theta(e_n)
 =\pi^{-1/2}\int_{\mathbb R}e^{-t^2}
             \Lambda_\theta(\alpha_t(a_n))\,dt.
 \tag{WD.14}
\]

In fact this pair lies in the norm closure of the graph restricted to \(B\). Since \(e_n\) is self-adjoint, it is finite-adjoint as well. For \(b\in B\), multiply each Riemann-sum pair on the left by \(b\). Its algebra entry remains in \(B\); its Hilbert entry is multiplied by \(\pi_\theta(b)\). Thus the graph pair of \(b e_n\) lies in that same graph closure.

For an arbitrary \(x\in A\), take \(b_k\in B\) approaching \(x\) in norm. For fixed \(n\), the left-ideal property and the GNS representation give

\[
 \|\Lambda_\theta((b_k-x)e_n)\|
 \leq\|b_k-x\|\,\|\Lambda_\theta(e_n)\|\to0.
 \tag{WD.15}
\]

Also \(b_k e_n\to x e_n\) in algebra norm. Consequently the graph pair of \(x e_n\) belongs to the closure of the graph on \(B\), even when \(x\) is not finite for \(\theta\).

Finally take \(x\in\mathfrak n_\theta\). KL's precise GNS identification transports CX-03's entire right multiplier formula back to this C*-domain:

\[
 \Lambda_\theta(x e_n)=R_n^\theta\Lambda_\theta(x),\qquad
 R_n^\theta=J_\theta\pi_\theta(\alpha_{-i/2}(e_n))J_\theta.
 \tag{WD.16}
\]

It includes membership \(x e_n\in\mathfrak n_\theta\). Equation (WD.13) makes \(R_n^\theta\to I\) strongly; (WD.12) makes \(x e_n\to x\) in algebra norm. Thus these graph pairs tend in both norms to \((x,\Lambda_\theta(x))\). All lie in the already established graph closure of \(B\), proving the graph-core assertion. The order of approximation is fixed: Gaussian Riemann sums, norm approximation at fixed \(n\), then \(n\to\infty\). No continuity of the unbounded GNS map in the algebra norm is assumed. \(\square\)

## Equality of modular C*-weights from common finite data

**Theorem.** Let \(\varphi,\psi\) be faithful, norm-lower-semicontinuous C*-semifinite weights on a separable \(A\), both satisfying the modular condition for the same pointwise norm-continuous \(\alpha\). Let \(B\subseteq\mathfrak m_\varphi\) be a norm-dense \(\alpha\)-invariant *-subalgebra on which they agree. Then \(\varphi=\psi\) on all \(A_+\), including infinite values.

Only their agreement on the positive squared moduli in \(B\) is needed below. For every \(b\in B\), \(b^*b,bb^*\in B\cap A_+\), and their \(\varphi\)-values are finite. Equality gives the same finite \(\psi\)-values. Hence \(B\subseteq\mathfrak n_\psi\cap\mathfrak n_\psi^*\), as well as the corresponding \(\varphi\)-domain. Polarizing the equal squared norms gives an isometric assignment

\[
 U_0\Lambda_\varphi(b)=\Lambda_\psi(b),\qquad b\in B.
 \tag{WD.17}
\]

It is representative independent and linear by the finite-domain GNS construction. WD-04 proves that \(B\) is a graph core for each map; in particular both \(\Lambda_\varphi(B)\) and \(\Lambda_\psi(B)\) are Hilbert dense. Therefore \(U_0\) extends to a unitary \(U:H_\varphi\to H_\psi\).

If \(x\in\mathfrak n_\varphi\), its graph-core approximants satisfy

\[
 b_k\to x\ \text{in }A,\qquad
 \Lambda_\varphi(b_k)\to\Lambda_\varphi(x),\qquad
 \Lambda_\psi(b_k)\to U\Lambda_\varphi(x).
 \tag{WD.18}
\]

The closed \(\psi\)-graph now forces \(x\in\mathfrak n_\psi\) and
\(\Lambda_\psi(x)=U\Lambda_\varphi(x)\). Reverse the roles to obtain equality of the entire finite left ideals, and hence equality of their squared GNS norms there. For \(a\in A_+\), apply this to \(x=a^{1/2}\) when either weight of \(a\) is finite. The two finite values coincide. If one were infinite and the other finite, the same finite-ideal equality would contradict it. The all-infinite case also agrees. This proves the full source Lemma 4.10, without an interchange of a general unbounded weight and an operator integral. \(\square\)

## Restriction to the fibres recovers every positive value

Return to a faithful, norm-lower-semicontinuous C*-semifinite \(\varphi\) on separable \(A\), with modular action \(\alpha\). Let \((H,\pi,\Lambda)\) be its semicyclic representation, \(M=\pi(A)''\), and \(D\subseteq Z(M)\) a specified abelian von Neumann subalgebra. WD-02 makes \(H\) separable. KL-07 supplies the specific faithful normal semifinite envelope \(\Phi\) on \(M\), with

\[
 \Phi(\pi(a))=\varphi(a)\quad(a\in A_+),\qquad
 \sigma_t^\Phi\circ\pi=\pi\circ\alpha_t.
 \tag{WD.19}
\]

Use the existing central decomposition and MW-07 over a standard sigma-finite diagonal base \((Y,\mu)\):

\[
 H=\int_Y^\oplus H_y\,d\mu(y),\quad
 \pi=\int_Y^\oplus\pi_y\,d\mu(y),\quad
 (M,\Phi)=\int_Y^\oplus(M_y,\Phi_y)\,d\mu(y).
 \tag{WD.20}
\]

Here each \(\Phi_y\) is faithful normal semifinite, \(H_y\) is identified with its GNS space, and \(\pi_y(A)''=M_y\) outside a common null set. The identifications are those supplied by the compatible associated GNS realization and diagonal uniqueness; an arbitrary unrelated abstract realization would not suffice. The named open field and central providers are in force.

Define on the original C*-algebra

\[
 \psi_y(a)=\Phi_y(\pi_y(a))\quad(a\in A_+).
 \tag{WD.21}
\]

Each is a weight by positivity, additivity and homogeneity of the homomorphism and the normal fibre weight. It is norm lower semicontinuous: norm convergence of positives is carried to norm convergence by the contractive homomorphism, and a normal weight is lower semicontinuous there. MW-02 supplies measurability of \(y\mapsto\psi_y(a)\). MW-05 and (WD.19) give

\[
 \varphi(a)=\Phi(\pi(a))
 =\int_Y\Phi_y(\pi_y(a))\,d\mu(y)
 =\int_Y\psi_y(a)\,d\mu(y)
 \quad(a\in A_+).
 \tag{WD.22}
\]

This is the whole equality of source Lemma 4.12 and clause (i) of Theorem 4.11. Every positive element is included. A finite-cone equality alone is not being extended without justification: the all-positive identity is precisely MW-05's input. Measurability and equality for a fixed \(a\) do not require taking an uncountable union of exceptional sets over all \(a\).

## One null set for every element and every modular time

For a fixed \(a\in A\) and \(t\in\mathbb R\), the modular decomposition in MW-07 and (WD.19) show that

\[
 \sigma_t^{\Phi_y}(\pi_y(a))=\pi_y(\alpha_t(a))
 \quad\text{for almost every }y.
 \tag{WD.23}
\]

The null set at this stage may depend on \(a,t\). Choose a countable norm-dense *-algebra \(A_0\) over \(\mathbb Q(i)\) in \(A\), and apply (WD.23) only to \(a\in A_0\) and \(t\in\mathbb Q\). There are countably many such pairs. Intersect their conull sets with the previously required field conull set. On the resulting single conull set, continuity in \(a\) extends (WD.23) to all \(a\in A\) for rational \(t\): both maps are contractive.

For any real \(t\), take rationals \(t_k\to t\). The left side converges sigma-strongly, by continuity of a fibre modular group. The right side converges in norm because \(\alpha\) is pointwise norm continuous and \(\pi_y\) is contractive. Norm convergence also implies sigma-strong convergence on these bounded orbits. Uniqueness of that limit proves, on this same conull set,

\[
 \sigma_t^{\Phi_y}\circ\pi_y=\pi_y\circ\alpha_t
 \quad\text{for all }t\in\mathbb R.
 \tag{WD.24}
\]

Invariance of \(\Phi_y\) then gives invariance of \(\psi_y\). If \(b,c\in\mathfrak n_{\psi_y}\cap\mathfrak n_{\psi_y}^*\), their images belong to the finite-adjoint domain of \(\Phi_y\). The bounded strip function for that image pair has edges

\[
 F_{b,c}(t)=\psi_y(\alpha_t(b)c),\qquad
 F_{b,c}(t+i)=\psi_y(c\alpha_t(b)).
 \tag{WD.25}
\]

Both finite products are valid by the finite-ideal rules. Thus \(\psi_y\) satisfies the full modular condition for \(\alpha\), on one conull set simultaneously for all finite test pairs. This proves source Lemma 4.13. The uncountable collection of strip pairs needs no further union of null sets: once (WD.24) holds for all algebra elements, each pair is supplied inside that fixed fibre by the modular theorem.

## Fibre semifiniteness and the onto GNS identification

Two density statements are needed. First choose a countable norm-dense set \(\{d_j\}\subseteq\mathfrak m_\varphi\), possible because this finite algebra is norm dense and \(A\) is separable. By (WD.22),

\[
 \int_Y\psi_y(d_j^*d_j)\,d\mu(y)
 =\varphi(d_j^*d_j)<\infty.
 \tag{WD.26}
\]

Each integrand is finite almost everywhere. Remove the union of these countably many null sets. Then every \(d_j\) is in \(\mathfrak n_{\psi_y}\) on the remaining fibres. Their algebra-norm density gives norm density of that left ideal. CS-01 then gives norm density of \(\mathfrak m_{\psi_y}\): approximate square roots of positive elements by finite-left-ideal elements and take their squared moduli. This proves C*-semifiniteness of \(\psi_y\) on this same common conull set.

Second, WD-02 and the defining GNS density let us choose \(a_j\in\mathfrak n_\varphi\) with \(\{\Lambda(a_j)\}\) Hilbert total in \(H\). For every \(j\), (WD.22) applied to \(a_j^*a_j\), and the full finite-left-ideal GNS identity MW-05, give

\[
 \Lambda(a_j)(y)=\Lambda_{\Phi_y}(\pi_y(a_j)),\qquad
 \int_Y\|\Lambda_{\Phi_y}(\pi_y(a_j))\|^2\,d\mu(y)
 =\varphi(a_j^*a_j)<\infty.
 \tag{WD.27}
\]

Here KL's GNS identification identifies \(\Lambda(a_j)\) with \(\Lambda_\Phi(\pi(a_j))\). Choose the representatives and remove the union of the countably many null sets for (WD.27).

The fields in (WD.27) are fibrewise Hilbert total almost everywhere. To justify this, let \(P_y\) be the orthogonal projection onto the closed span of their values. Countable measurable Gram–Schmidt in DI FIELD makes \(P_y\) a measurable, norm-at-most-one field. Its integral \(P\) fixes every global \(\Lambda(a_j)\); global density gives \(P=I_H\). Uniqueness of bounded decomposable operator fields gives \(P_y=I_{H_y}\) almost everywhere. This argument proves pointwise totality; it does not infer it merely by selecting representatives of a globally dense sequence.

Let \((K_y,\pi_{\psi_y},\Lambda_{\psi_y})\) be the C*-GNS triple of \(\psi_y\). On its actual finite domain define

\[
 V_y\Lambda_{\psi_y}(a)
 =\Lambda_{\Phi_y}(\pi_y(a)),\qquad
 a\in\mathfrak n_{\psi_y}.
 \tag{WD.28}
\]

The equality of squared norms is (WD.21) applied to \(a^*a\). It proves representative independence and isometry; polarization proves preservation of all inner products. The extension has closed range because \(K_y\) is complete. It contains the fibre-total family in (WD.27), so that range is all \(H_y\). Hence \(V_y\) is unitary. For \(b\in A\), the left-ideal rule gives, on the dense GNS core,

\[
 V_y\pi_{\psi_y}(b)\Lambda_{\psi_y}(a)
 =\Lambda_{\Phi_y}(\pi_y(ba))
 =\pi_y(b)V_y\Lambda_{\psi_y}(a).
 \tag{WD.29}
\]

Boundedness extends this equality to every vector. Thus \(\pi_{\psi_y}\) is unitarily equivalent to \(\pi_y\), proving clause (iii) of Theorem 4.11. A norm-dense finite ideal and a Hilbert-total GNS range are different requirements; both have now been established.

## The full C*-disintegration theorem and its kernels

**Theorem.** Let \(A\) be separable, \(\alpha\) a pointwise norm-continuous one-parameter automorphism group, and \(\varphi\) a faithful, norm-lower-semicontinuous C*-semifinite weight satisfying its modular condition. Let \(D\) be any specified von Neumann subalgebra of the center of \(\pi_\varphi(A)''\). Relative to the representation's central disintegration over \(D\), there exist weights \(\psi_y\) on \(A\) with the following properties:

1. For every \(a\in A_+\), \(y\mapsto\psi_y(a)\) is measurable and \(\varphi(a)=\int_Y\psi_y(a)\,d\mu(y)\), with extended nonnegative values.
2. Off one null set, \(\psi_y\) is norm lower semicontinuous, C*-semifinite, and satisfies the modular condition for \(\alpha\).
3. Off one null set, its C*-GNS representation is unitarily equivalent to the specified fibre representation \(\pi_y\).

**Proof at the named field/central inputs.** WD-06 proves clause 1 and lower semicontinuity. WD-07 proves modularity on one common conull set. WD-08 proves norm-semifiniteness and the explicit onto intertwining isometry there. Intersect the finitely many conull sets constructed in these arguments. This is the whole source Theorem 4.11; the countability uses are displayed rather than suppressed. Zero fibres and the zero algebra have their usual zero-space interpretations. \(\square\)

Although \(\varphi\) is faithful on \(A\), the fibre \(\psi_y\) need not be. Faithfulness of \(\Phi_y\) gives the precise kernel:

\[
 \mathcal Z_{\psi_y}
 =\{a:\psi_y(a^*a)=0\}
 =\ker\pi_y.
 \tag{WD.30}
\]

This is a norm-closed two-sided ideal, invariant under \(\alpha\) by (WD.24). The fibre weight factors through \(A/\ker\pi_y\) as a faithful weight. Its descended homomorphism into \(M_y\) is injective and therefore isometric, so the descended weight is norm lower semicontinuous. Images of the norm-dense finite domain show its semifiniteness, and modular covariance descends as well. These statements clarify the quotient, rather than adding fibre faithfulness on the original algebra to the source theorem.

The general compatible associated measurable realization and the FIELD, CENTRAL and SELECTION contracts are not proved in this lesson. It supplies all five source-item arguments at those specified inputs.

## A faithful global weight with nonfaithful fibres

Take \(A=C_0((0,1])\), Lebesgue measure, the identity action, and

\[
 \varphi(f)=\int_0^1 y^{-2}f(y)\,dy\quad(f\in A_+).
 \tag{WD.31}
\]

This weight is faithful because a nonzero continuous positive function is positive on a nonempty interval. It is norm lower semicontinuous by Fatou's lemma for norm-convergent positive sequences. The compactly supported functions away from zero are finite and norm dense, proving C*-semifiniteness. Commutativity and the identity action give the modular condition with constant strip functions.

Its GNS space is \(L^2((0,1],y^{-2}dy)\). Multiplication represents \(A\), whose bicommutant is the multiplication algebra \(L^\infty\); compactly supported continuous functions are dense in the indicated \(L^2\) space, and their bounded multiplication approximations generate the measurable multiplication projections. In the Lebesgue-base realization the unitary is

\[
 W:L^2((0,1],y^{-2}dy)\longrightarrow L^2((0,1],dy),
 \qquad (Wg)(y)=g(y)/y.
 \tag{WD.32}
\]

It is onto, with inverse \(h\mapsto yh\). The fibre algebra and Hilbert space are both \(\mathbb C\), while

\[
 \pi_y(f)=f(y),\qquad
 \psi_y(f)=y^{-2}f(y),\qquad
 \Lambda_{\psi_y}(f)=f(y)/y.
 \tag{WD.33}
\]

Each fibre weight is a bounded functional on \(A\), but is not faithful there: any function vanishing at that \(y\) is in its GNS kernel. It is faithful on the quotient identified with \(\mathbb C\). Its GNS map is onto because for any fixed \(y>0\) a compactly supported bump function can take any prescribed value there.

For \(f_\beta(y)=y^\beta\), \(\beta>0\), the two different finite-domain thresholds are

\[
 \varphi(f_\beta)=
 \begin{cases}
  +\infty,&0<\beta\leq1,\\
  (\beta-1)^{-1},&\beta>1,
 \end{cases}
 \qquad
 \|\Lambda_\varphi(f_\beta)\|^2=
 \begin{cases}
  +\infty,&0<\beta\leq\tfrac12,\\
  (2\beta-1)^{-1},&\beta>\tfrac12.
 \end{cases}
 \tag{WD.34}
\]

The second expression denotes the extended energy; an actual GNS vector exists only in its finite case. Integrating \(y^{\gamma-2}\) from \(\varepsilon\) to one and taking \(\varepsilon\downarrow0\) proves each branch, including logarithmic divergence at its boundary. For example, \(f_{3/4}\) has a GNS vector of squared norm two while its positive weight is infinite. All fibre evaluations remain finite.
