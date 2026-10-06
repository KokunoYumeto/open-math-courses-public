# Invariant states and ergodic projections

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. Original text: CC0 1.0.*

An automorphism group can have many invariant normal states even when it is not compact as a group. Those states determine a unique averaging map onto its fixed algebra. They also control weak compactness of every orbit in the predual. We prove these equivalences without assuming a countable group, a separable predual, or a single faithful invariant state.

We use normal GNS representations, normal vector-functional expansions and preduals from [The double commutation theorem](../../foundations-of-von-neumann-algebras/the-double-commutant-theorem.html) and [Operator spaces and preduals](../../foundations-of-von-neumann-algebras/compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies.html). [Proposition 8.1(3)](../../foundations-of-von-neumann-algebras/integral-representations-of-states.html#oa-fnd-ir-09) of the freely readable programme lesson on integral representations gives the full commutant proof for dominated functionals. Its large-group and simplex arguments are used through the exact proof chain given in Section 6 below. We also use the tracial GNS result, Proposition 11.2 of [Multiplicity](../reader/supplements/tracial-gns-and-finite-algebras.html#oa-fnd-mu-21), and [Central averaging and maximal ideals](../reader/central-averaging-and-maximal-ideals.html). These programme lessons contain the complete prerequisite arguments. Takesaki’s book provides further context.

Section 4 uses Theorem 4.1 of [Weak sequences and compact convex hulls](../reader/weak-sequences-and-convex-hull-compactness.html), which proves compactness of the closed convex hull of a weakly compact Banach-space set. The fixed-point step is proved in Theorem 5.1 of [Weakly compact convex sets and fixed points](../reader/weakly-compact-convex-sets-and-fixed-points.html): a group of weakly continuous affine isometries preserving a nonempty weakly compact convex set has a common fixed point. Both proofs allow arbitrary Banach spaces, and the latter allows an arbitrary group. The arguments below verify their hypotheses. The fixed-point result also supplies the invocation in Theorem 4.7 of [Traces, part A](../reader/supplements/traces-on-von-neumann-algebras-part-a-def-v-2-1-to-def-v-2-17.html). Its weak-compactness criterion is proved in Theorem 10.2 of [Polar decomposition and weak compactness](../../foundations-of-von-neumann-algebras/polar-decomposition-of-functionals-and-weak-compactness-in-preduals.html#oa-fnd-pd-17); the sequence criterion used there is Theorem 2.1 of the convex-hull lesson.

Let \(M\) be a nonzero von Neumann algebra and \(G\subseteq\operatorname{Aut}(M)\) a group. Automorphisms are normal. Write
\[
N=M^G=\{x\in M:g(x)=x\text{ for every }g\in G\},
\qquad
K_G(x)=\overline{\operatorname{co}}^{\,\sigma(M,M_*)}\{g(x):g\in G\}.
\tag{0.1}
\]
The set \(K_G(x)\) is compact: it is ultraweakly closed and lies in the ball of radius \(\|x\|\), which is ultraweakly compact. The full Banach–Alaoglu proof is [Lemma 0.3](../reader/weak-sequences-and-convex-hull-compactness.html#0-banach-space-compactness-inputs); its Hahn–Banach proof in Lemma 0.1 also supplies the equality of weak and norm closures of convex sets used below.

Call \(M\) **\(G\)-finite** if its invariant normal states separate \(M_+\): for every nonzero positive \(x\), at least one such state has positive value on \(x\). This definition asks for a separating family, not a single faithful member.

## 1. The minimum seen by an invariant state

For a positive invariant normal functional \(\varphi\), use its GNS triple \((\pi_\varphi,H_\varphi,\xi_\varphi)\). Zero functionals can be omitted. The formula
\[
U_\varphi(g)\pi_\varphi(a)\xi_\varphi
=\pi_\varphi(g(a))\xi_\varphi
\]
defines a unitary representation, since \(\varphi(g(a)^*g(a))=\varphi(a^*a)\). Let \(P_\varphi\) project onto its fixed vectors.

We first recall a Hilbert-space fact, with proof. The norm-closed convex hull of a unitary orbit of a vector \(v\) has a unique vector \(w\) of smallest norm. Existence follows by taking a sequence whose norms tend to the infimum: the parallelogram identity makes it Cauchy. Strict convexity gives uniqueness. Every unitary in the group preserves the hull and its norm, so \(w\) is fixed. The fixed-space projection \(P\) is constant on the hull, because \(PU(g)v=Pv\). Thus \(w=Pw=Pv\). In particular \(Pv\) belongs to that hull.

**Proposition 1.1.** On \(K_G(x)\), the function
\[
y\longmapsto\varphi(y^*y)^{1/2}
\]
attains its minimum, and a point \(y\) minimizes it exactly when
\[
\pi_\varphi(y)\xi_\varphi
=P_\varphi\pi_\varphi(x)\xi_\varphi.
\tag{1.1}
\]

**Proof.** The bounded linear map \(y\mapsto\pi_\varphi(y)\xi_\varphi\) is ultraweak-to-weak continuous. For vectors \(\pi_\varphi(b)\xi_\varphi\), its coordinates are the normal functionals \(y\mapsto\varphi(b^*y)\); approximation of an arbitrary vector gives normal coordinates, since the predual is norm closed. Consequently the image of \(K_G(x)\) is weakly compact.

This image is the closed convex hull of the orbit of \(\pi_\varphi(x)\xi_\varphi\). One inclusion follows from weak continuity and separation by vector functionals; the other follows because the image is a weakly closed convex set containing that orbit. Weak and norm closures of a convex set agree. Apply the Hilbert-space fact. The norm is weakly lower semicontinuous, and the smallest vector is unique, giving (1.1). \(\square\)

Let \(F_\varphi(x)\subseteq K_G(x)\) be this compact, nonempty set of minimizing points.

**Proposition 1.2.** For invariant positive normal \(\varphi_1,\ldots,\varphi_m\), with \(\varphi=\sum_j\varphi_j\),
\[
F_\varphi(x)=\bigcap_{j=1}^mF_{\varphi_j}(x).
\tag{1.2}
\]

**Proof.** The isometry
\[
a\xi_\varphi\longmapsto
(a\xi_{\varphi_1},\ldots,a\xi_{\varphi_m})
\]
realizes \(H_\varphi\) as a closed subspace \(S\) of \(\bigoplus_jH_{\varphi_j}\). It intertwines the group representations. Since the action is a group of unitaries, \(S\) and \(S^\perp\) are invariant. The projection onto \(S\) therefore commutes with every group unitary and with its fixed-space projection. Hence the restriction of \(\bigoplus_jP_{\varphi_j}\) to \(S\) is \(P_\varphi\). Equation (1.1) for \(\varphi\) is now exactly the list of equations (1.1) for all \(\varphi_j\). \(\square\)

The same argument works for a finite tuple \((x_1,\ldots,x_r)\) acted on by the same \(g\). Use the compact orbit hull in \(M^r\) and the vectors in \(H_\varphi^r\); their fixed-space projection is the coordinatewise \(P_\varphi\). It is essential that the same group element acts on every coordinate.

## 2. A unique fixed point in each orbit hull

**Theorem 2.1.** If \(M\) is \(G\)-finite, then
\[
K_G(x)\cap N=\{E(x)\}
\tag{2.1}
\]
for every \(x\in M\). The resulting map \(E:M\to N\) is a faithful normal positive projection of norm one. It satisfies
\[
E(g(x))=E(x),\qquad
E(bxc)=bE(x)c\quad(b,c\in N),\qquad
\varphi E=\varphi
\tag{2.2}
\]
for every invariant normal positive functional \(\varphi\).

**Proof.** By (1.2) the sets \(F_\varphi(x)\), over all invariant normal states, have the finite intersection property. Compactness gives a common point \(y\). For every \(g\),
\[
\pi_\varphi(g(y)-y)\xi_\varphi
=U_\varphi(g)P_\varphi\pi_\varphi(x)\xi_\varphi
-P_\varphi\pi_\varphi(x)\xi_\varphi=0.
\]
Thus \(\varphi((g(y)-y)^*(g(y)-y))=0\) for every member of the separating family. It follows that \(g(y)=y\).

Conversely any fixed \(z\in K_G(x)\) has \(\pi_\varphi(z)\xi_\varphi\) fixed. The fixed-space projection is constant on the image of \(K_G(x)\), so that vector equals the right side of (1.1). Two fixed points therefore have zero difference under every separating GNS seminorm, and are equal. This proves (2.1).

To prove linearity, apply the finite intersection argument to the simultaneous orbit hull of \((x_1,\ldots,x_r)\), using the tuple version after Proposition 1.2. It gives the tuple \((E(x_1),\ldots,E(x_r))\) in that hull. Every scalar linear combination of the tuple lies in the orbit hull of the same combination. Since the resulting combination is fixed, uniqueness proves
\[
E\!\left(\sum_j\lambda_jx_j\right)=\sum_j\lambda_jE(x_j).
\]
Likewise the hulls commute with taking adjoints, so \(E(x^*)=E(x)^*\). Positive elements have positive orbit hulls; hence \(E\) is positive. Also \(E(1)=1\), \(E\) fixes \(N\), and \(\|E(x)\|\leq\|x\|\) from the hull bound. Thus it is a projection of norm one.

The functional \(\varphi\) is constant on each orbit hull, so \(\varphi E=\varphi\). If \(x\geq0\) and \(E(x)=0\), all invariant normal states vanish on \(x\); separation gives \(x=0\). This proves faithfulness.

For \(b\in N\), \(\pi_\varphi(b)\) commutes with the group unitaries and hence with \(P_\varphi\). Using (1.1),
\[
\pi_\varphi(E(bx))\xi_\varphi
=P_\varphi\pi_\varphi(bx)\xi_\varphi
=\pi_\varphi(b)P_\varphi\pi_\varphi(x)\xi_\varphi
=\pi_\varphi(bE(x))\xi_\varphi.
\]
Separation gives \(E(bx)=bE(x)\). Taking adjoints gives right multiplication, and then the two-sided identity in (2.2). The invariant-hull identity \(K_G(g(x))=K_G(x)\) gives the first part of (2.2).

Finally let \(x_i\uparrow x\) be a bounded increasing net in \(M_+\). The elements \(E(x_i)\) increase to an element \(e\leq E(x)\) of \(N\). For every invariant normal state,
\[
\varphi(e)=\sup_i\varphi(E(x_i))
=\sup_i\varphi(x_i)=\varphi(x)=\varphi(E(x)).
\]
The positive difference \(E(x)-e\) vanishes under the separating family, so it is zero. Preservation of these suprema proves normality. \(\square\)

The map \(E\) is the **ergodic projection**, and (2.2) makes it a conditional expectation onto the fixed algebra.

**Theorem 2.2.** The following are equivalent:

1. \(M\) is \(G\)-finite.
2. There is a faithful normal norm-one projection \(Q:M\to N\) satisfying \(Q g=Q\) for every \(g\in G\).

When they hold this projection is unique.

**Proof.** Theorem 2.1 proves existence from (1). Conversely a projection onto \(N\) fixes \(1\), so a norm-one \(Q\) is positive. For completeness, each state \(\theta\) on \(N\) makes \(\theta Q\) a norm-one unital functional on \(M\), hence a state; states detect positivity in \(N\). If \(x\in M_+\setminus\{0\}\), faithfulness gives \(Q(x)\ne0\). Some normal positive functional \(\theta\) on \(N\) has \(\theta(Q(x))>0\). The functional \(\theta Q\) is normal, positive and invariant, and its normalization is the required separating state.

If \(Q\) has the stated properties, it is constant on an orbit and, by normality, on its ultraweak convex hull. Since \(E(x)\in K_G(x)\cap N\),
\[
Q(x)=Q(E(x))=E(x).
\]
This proves uniqueness. \(\square\)

Group invariance is one of the hypotheses of this uniqueness statement. Faithful normal norm-one projections onto a given algebra can otherwise be plentiful, as Exercise 7.3 shows.

## 3. Domination and weakly compact intervals

The predual has its Banach-space weak topology \(\sigma(M_*,M)\).

**Lemma 3.1.** For a positive normal functional \(\omega\) and \(C<\infty\), the interval
\[
[0,C\omega]=\{\theta\in M_*^+:0\leq\theta\leq C\omega\}
\]
is weakly compact.

**Proof.** In the normal GNS representation of \(\omega\), Proposition 8.1(3) of the integral-representation lesson identifies this interval with
\[
\theta_h(x)=\langle h\pi_\omega(x)\xi_\omega,\xi_\omega\rangle,
\qquad h\in\pi_\omega(M)',\quad0\leq h\leq C1.
\]
The operator interval is ultraweakly compact. Every scalar coordinate \(\theta_h(x)\) is ultraweakly continuous in \(h\). All \(\theta_h\) are normal because \(\pi_\omega\) is normal. Thus its image is a weakly compact subset of \(M_*\), and the domination theorem says this image is exactly the displayed interval. \(\square\)

**Lemma 3.2.** If \(\varphi,\omega\) are positive normal functionals with \(s(\varphi)\leq s(\omega)\), then for every \(\varepsilon>0\) there are \(C<\infty\) and a positive normal \(\theta\leq C\omega\) with
\[
\|\varphi-\theta\|<\varepsilon.
\tag{3.1}
\]

**Proof.** Write \(p=s(\omega)\) and work in \(pMp\), where \(\omega\) is faithful. Its normal GNS representation is faithful, and \(\xi_\omega\) is separating: \(\pi_\omega(x)\xi_\omega=0\) implies \(\omega(x^*x)=0\), hence \(x=0\). It is cyclic for the commutant as well. Indeed the projection onto \([\pi_\omega(M)'\xi_\omega]\) belongs to \(\pi_\omega(M)\), fixes \(\xi_\omega\), and is \(1\) because that vector is separating.

By the normal positive vector-functional expansion, \(\varphi\) is a sum of vector functionals in this representation, with summable squared vector norms. Truncate this sum and approximate its finitely many vectors \(\eta_j\) by \(y'_j\xi_\omega\), \(y'_j\in\pi_\omega(M)'\). The estimate
\[
\|\omega_\eta-\omega_\zeta\|
\leq\|\eta-\zeta\|(\|\eta\|+\|\zeta\|)
\]
makes the resulting positive sum \(\theta\) as close to \(\varphi\) as desired. For \(x\geq0\), commutation gives
\[
\theta(x)=\sum_j
\|\pi_\omega(x)^{1/2}y'_j\xi_\omega\|^2
\leq\left(\sum_j\|y'_j\|^2\right)\omega(x).
\]
This proves domination in the corner. Extend by \(x\mapsto pxp\). Since both \(\varphi\) and \(\omega\) are supported on \(p\), (3.1) and the domination inequality also hold on \(M\). \(\square\)

We will also use this elementary compactness observation. If a bounded set \(S\) in a Banach space \(X\) can be approximated uniformly in norm, to every positive accuracy, by a relatively weakly compact set, then \(S\) is relatively weakly compact. To prove it, take the weak-star closure of \(S\) in \(X^{**}\). A cluster point \(a\) has distance at most \(\varepsilon\) from \(X\): along a subnet the approximating points converge weakly to a point of \(X\), and the error lies in the weak-star compact ball of radius \(\varepsilon\). Since \(X\) is norm closed in \(X^{**}\) and \(\varepsilon\) is arbitrary, every cluster point is in \(X\). The resulting compact closure carries precisely the weak topology of \(X\).

## 4. Weak compactness of the predual orbits

**Theorem 4.1.** \(M\) is \(G\)-finite if and only if every orbit
\[
\{\varphi\circ g:g\in G\}\subseteq M_*
\tag{4.1}
\]
is relatively weakly compact. It suffices to check positive normal \(\varphi\).

**Proof.** Suppose first that \(M\) is \(G\)-finite, and let \(E\) be its ergodic projection. For \(\varphi\geq0\), put \(\omega=\varphi E\). This functional is normal and invariant. Its support \(p\) is fixed by \(G\), because the support is determined by the functional. Since \(E\) fixes \(p\),
\[
\varphi(1-p)=\varphi(E(1-p))=\omega(1-p)=0.
\]
Thus \(s(\varphi)\leq p=s(\omega)\).

Apply Lemma 3.2. The orbit of an approximation \(\theta\leq C\omega\) is contained in \([0,C\omega]\), because \(\omega\) is invariant. It is relatively weakly compact by Lemma 3.1. Composition with an automorphism preserves norm, so this approximation works uniformly for the whole orbit of \(\varphi\). The compactness observation proves relative weak compactness of (4.1). Every normal functional is a linear combination of four positive normal functionals, by taking real and imaginary parts and their Jordan decompositions. The corresponding sum of four weakly compact closures is weakly compact, proving the claim for all \(\varphi\).

Conversely suppose every positive normal orbit is relatively weakly compact. Its weakly closed convex hull is weakly compact by the convex-hull theorem. It consists of positive normal functionals of the same value at \(1\). Use \(T_g\varphi=\varphi\circ g^{-1}\); these maps form a group of surjective linear isometries of the Banach space \(M_*\). They are weakly continuous because bounded linear maps are continuous for the weak topologies, and they preserve the hull. Theorem 5.1 of the fixed-point lesson gives an invariant positive normal functional in it. Starting with a state gives an invariant state.

We still need separation. Let \(p\) be the supremum of the supports of all invariant normal states. It is fixed by \(G\). If \(q=1-p\ne0\), choose a normal state \(\varphi\) supported on \(q\); normal functionals separate the positive elements of the nonzero corner \(qMq\). Every point in its orbit hull remains supported on \(q\), since the equation \(\theta(q)=1\) is weakly closed and \(g(q)=q\). The fixed point just constructed would be an invariant normal state with nonzero support below \(q\), contradicting the definition of \(p\). Hence \(p=1\).

If \(x\geq0\) vanishes under every invariant normal state \(\theta\), then \(x^{1/2}s(\theta)=0\): on the support corner \(\theta\) is faithful, and \(\theta(x)=\theta(s(\theta)xs(\theta))\). Since those supports have supremum \(1\), \(x^{1/2}=0\). Thus the invariant normal states separate \(M_+\). \(\square\)

## 5. The topology on bounded maps

Let \(\mathcal L(M)\) be the bounded linear maps from \(M\) to itself and \(\mathcal L_*(M)\) its normal maps. The natural weak-star topology on \(\mathcal L(M)\) comes from
\[
\mathcal L(M)=(M\widehat\otimes_\pi M_*)^*,
\qquad \langle S,x\otimes\varphi\rangle=\varphi(Sx).
\tag{5.1}
\]
Here \(\widehat\otimes_\pi\) is the Banach projective tensor product. The identity follows from the correspondence between bounded bilinear forms on \(M\times M_*\) and bounded maps \(M\to(M_*)^*=M\). On uniformly norm-bounded sets this topology is just convergence of every scalar \(\varphi(Sx)\): finite sums of elementary tensors are dense, and the uniform norm bound controls their approximation.

Every automorphism has norm one, so its weak-star closure \(C\) in \(\mathcal L(M)\) is compact. Saying that \(G\) is **relatively compact within the normal maps** means
\[
C\subseteq\mathcal L_*(M).
\tag{5.2}
\]
It includes a condition on the limits.

**Theorem 5.1.** Condition (5.2) holds exactly when the predual orbits in Theorem 4.1 are relatively weakly compact, hence exactly when \(M\) is \(G\)-finite.

**Proof.** If every predual orbit has weakly compact closure, take \(S\in C\) and a net \(g_i\to S\) in the topology (5.1). For \(\varphi\in M_*\), the functionals \(\varphi g_i\) have a subnet converging weakly in \(M_*\), to \(\theta\). Evaluation on \(x\) gives
\[
\theta(x)=\lim_i\varphi(g_i(x))=\varphi(Sx).
\]
Thus \(\varphi S\) is normal for every normal \(\varphi\), which is precisely normality of \(S\).

Conversely if all \(S\in C\) are normal, the map
\[
C\longrightarrow M_*,\qquad S\longmapsto\varphi S
\]
is continuous for the weak topology of \(M_*\), by (5.1). Its image is compact and contains the predual orbit of \(\varphi\). \(\square\)

**Corollary 5.2.** For a factor \(M\), the full automorphism group is relatively compact within the normal maps in this topology if and only if \(M\) is finite.

**Proof.** If \(M\) is finite, its normalized normal trace is faithful and unique. Every automorphism preserves it, so it is an invariant separating state. Apply Theorem 5.1.

Conversely \(G\)-finiteness for \(G=\operatorname{Aut}(M)\) gives a nonzero invariant normal state. Invariance under inner automorphisms implies that it is tracial: for self-adjoint \(b\), differentiate \(\theta(e^{itb}xe^{-itb})=\theta(x)\) at zero to obtain \(\theta(bx)=\theta(xb)\), then extend linearly in \(b\). The support of a normal trace is central, hence is \(1\) in a factor. A faithful finite trace makes \(M\) finite: if \(v^*v=1\), then the trace of \(1-vv^*\) is zero, so faithfulness gives \(vv^*=1\). \(\square\)

## 6. Tracial states form a simplex

Let \(B\) be a unital C*-algebra. Its tracial state space
\[
\mathcal T(B)=\{\theta\in\mathcal S(B):\theta(ab)=\theta(ba)\text{ for all }a,b\in B\}
\]
is a weak-star closed convex set. A nonempty compact convex set is a simplex here in the sense of Definition 7.1 of the integral-representation lesson; equivalently, its points have unique maximal representing probability measures. If \(\mathcal T(B)\) is empty, the assertion concerns no points.

**Proposition 6.1.** When nonempty, \(\mathcal T(B)\) is a simplex.

**Proof.** It is the invariant state space for the inner automorphism group \(G=\operatorname{Int}(B)\). Traces are invariant. Conversely the exponential differentiation argument in Corollary 5.2 works in any unital C*-algebra and proves traciality from invariance.

We verify the large-group hypothesis (S) of Theorem 24.1 of the integral-representation lesson. Fix an invariant state \(\theta\), its GNS representation \(\pi\), and \(b\in B\). The tracial GNS theorem makes \(R=\pi(B)''\) finite, with faithful normal vector trace. Let \(C_b\) be the weak operator closed convex hull of
\[
\{\pi(ubu^*):u\in\mathcal U(B)\}.
\]
Every unitary \(w\in R\) is a strong-star limit of unitaries in \(\pi(B)\) obtained from exponentials in \(B\). To check this, take a bounded self-adjoint logarithm \(h\) of \(w\) in \(R\), approximate \(h\) strongly by uniformly bounded self-adjoint elements of \(\pi(B)\) using Kaplansky density, and exponentiate. Uniform polynomial approximation of the exponential gives strong-star convergence. Thus \(w\pi(b)w^*\in C_b\) for every unitary \(w\in R\).

Central averaging in the finite von Neumann algebra \(R\) puts \(T_R(\pi(b))\) in the norm-closed convex hull of that larger unitary orbit. Since \(C_b\) contains the larger orbit and is weakly closed and convex,
\[
T_R(\pi(b))\in C_b\cap Z(R).
\]
This is exactly hypothesis (S), for every invariant state and every \(b\). The full proof of [Theorem 24.1(b)](../../foundations-of-von-neumann-algebras/integral-representations-of-states.html#oa-fnd-ir-26) shows that compression of \(\pi(B)\) to the fixed-vector space is commutative. [Proposition 23.3](../../foundations-of-von-neumann-algebras/integral-representations-of-states.html#oa-fnd-ir-25), using the explicit lifting argument of [Proposition 12.3(b)](../../foundations-of-von-neumann-algebras/integral-representations-of-states.html#oa-fnd-ir-13), then makes \(\pi(B)'\cap U(G)'\) abelian. [Proposition 17.1(6)](../../foundations-of-von-neumann-algebras/integral-representations-of-states.html#oa-fnd-ir-18) constructs a representing measure for this abelian algebra and proves that it majorizes every other representing probability measure on the invariant state space. It therefore gives the unique maximal measure for each invariant state. Finally [Theorem 7.4](../../foundations-of-von-neumann-algebras/integral-representations-of-states.html#oa-fnd-ir-23), with its full three-implication proof, identifies this property with being a simplex. This chain applies to every unital \(B\), without separability or a claim that one measure is carried by the extreme points in the nonmetrizable case. \(\square\)

For \(B=M_n(\mathbb C)\), this simplex is a single point, the normalized trace. For a finite direct sum of full matrix algebras it is the simplex of weights on the summands. A general unital C*-algebra may have no tracial states.

## 7. Exercises with solutions

**Exercise 7.1 — Basic: averaging a sign action.** On \(M_3(\mathbb C)\), let \(g=\operatorname{Ad}\operatorname{diag}(1,1,-1)\) and \(G=\{1,g\}\). Find \(N=M_3^G\) and its ergodic projection. Prove faithfulness directly.

**Solution.** In the decomposition \(\mathbb C^3=\mathbb C^2\oplus\mathbb C\), conjugation changes the signs of the two off-diagonal blocks. Thus
\[
N=M_2(\mathbb C)\oplus\mathbb C,\qquad
E\!\begin{pmatrix}A&b\\c&d\end{pmatrix}
=\begin{pmatrix}A&0\\0&d\end{pmatrix}
=\tfrac12(x+g(x)).
\]
This map is normal, positive, unital and invariant. For \(x\geq0\), \(E(x)=0\) implies \(\operatorname{Tr}(x)=\operatorname{Tr}(E(x))=0\), hence \(x=0\). Equivalently the faithful normalized trace is invariant, proving \(G\)-finiteness.

**Exercise 7.2 — Intermediate: the bilateral shift.** Let \(M=\ell^\infty(\mathbb Z)\), and let \(G\) be the translation group. Prove that there is no invariant normal state, and show directly that the orbit of the coordinate state at \(0\) is not relatively weakly compact in \(M_*=\ell^1(\mathbb Z)\).

**Solution.** A normal state has nonnegative weights \((a_j)\) summing to one. Translation invariance would make all weights equal; a summable constant sequence on \(\mathbb Z\) is zero, a contradiction.

The coordinate state orbit is \(\{\delta_j:j\in\mathbb Z\}\). If it were relatively weakly compact, the sequence \(\delta_n\), \(n\geq1\), would have a weakly convergent subnet with limit \(a\in\ell^1\). Every coordinate evaluation tends to zero, so \(a_j=0\) for all \(j\). But evaluation at the bounded constant sequence \(1\) is identically one on the subnet and would give \(\sum_ja_j=1\). This contradiction also explains why compactness of the orbit hull in the larger dual \(M^*\) does not ensure a normal limit.

**Exercise 7.3 — Advanced: why invariance belongs in uniqueness.** Let \(M=M_2(\mathbb C)\), \(G=\operatorname{Int}(M)\), and
\[
Q_\rho(x)=\operatorname{Tr}(\rho x)1,
\qquad
\rho=\begin{pmatrix}3/4&0\\0&1/4\end{pmatrix}.
\]
Show that \(Q_\rho\) is a faithful normal norm-one projection onto \(M^G\), but is not \(G\)-invariant. Determine the unique invariant projection and describe the tracial states of \(M_2(\mathbb C)\oplus M_3(\mathbb C)\).

**Solution.** Commutation with all unitaries forces \(M^G=\mathbb C1\). The density matrix \(\rho\) is strictly positive with trace one. Thus \(Q_\rho\) is positive and unital, has norm one, fixes scalars and is a projection. In finite dimension it is normal; if \(x\geq0\), its value is zero only when \(x=0\), by strict positivity of \(\rho\). But a unitary exchanging the two basis vectors sends \(e_{11}\) to \(e_{22}\), while
\[
Q_\rho(e_{11})=\tfrac34\,1,\qquad
Q_\rho(e_{22})=\tfrac14\,1.
\]
It therefore fails invariance. The unique invariant projection is \(E(x)=\frac12\operatorname{Tr}(x)1\), by Theorem 2.2, or by uniqueness of the normalized trace.

For the direct sum, restriction of a tracial state to each matrix summand is a nonnegative multiple of its normalized trace. Consequently all tracial states are
\[
\theta_t(a,b)=t\,\operatorname{tr}_2(a)+(1-t)\operatorname{tr}_3(b),
\qquad0\leq t\leq1.
\]
The extreme points are the two endpoint traces, and the unique maximal representing measure of \(\theta_t\) gives them weights \(t\) and \(1-t\). This is a segment simplex, rather than a singleton.

## References

[Namioka–Asplund] I. Namioka and E. Asplund, *A geometric proof of Ryll-Nardzewski's fixed point theorem*, Bulletin of the AMS 73 (1967), 443–445. [Freely accessible paper](https://www.ams.org/journals/bull/1967-73-03/S0002-9904-1967-11779-8/S0002-9904-1967-11779-8.pdf). The paper treats a broader locally convex semigroup setting. The linked fixed-point lesson supplies the arbitrary-group Banach-space theorem used here.

[Whitley] R. Whitley, *The Krein–Šmulian theorem*, Proceedings of the AMS 97 (1986), 376–377. [Freely accessible paper](https://math.univ-lyon1.fr/wikis/rouge/lib/exe/fetch.php?media=rodrigues6_whitley2.pdf). The linked programme proof supplies the sequence and barycentre arguments explicitly, including the nonseparable case.

[Takesaki] M. Takesaki, *Theory of Operator Algebras I*, Springer.
