<span id="continuity-of-actions-scalar-tests-preduals-and-bounded-nets"></span>
# Continuity of actions: scalar tests, preduals, and bounded nets

*CC0 1.0.*

The weak compact convex hull input in the foundations below is proved in [Weak sequences and compact convex hulls](../../reader/weak-sequences-and-convex-hull-compactness.html#4-convexification-in-an-arbitrary-banach-space), Sections 0–4; its Section 0 also proves dual completeness and weak closures. The [Baire proof](../../../foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.html#oa-fnd-hb-03) and [convex-separation proofs](../../../foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.html#oa-fnd-hb-06) supply the Banach inputs. The [Haar and Radon foundations](../../../KT-CP/prerequisites/OA-FLOW/repaired-20261004/haar-and-radon-foundations.html) and [concrete predual proofs](../../../OA-MOD/concrete-preduals.html) supply the indicated measure and predual inputs.

A scalar coefficient tests one vector against one functional. Norm continuity asks for control against the entire dual unit ball at once. For a representation of a locally compact group on a Banach space, these two continuity requirements turn out to be equivalent. Applied to the predual of a von Neumann algebra, this converts scalar tests on algebra elements into norm control of normal functionals. That norm control also permits the algebra element and the group parameter to vary together.

<a id="OA-FLOW.TOP.FOUNDATIONS"></a>

<span id="oa-flowtopfoundations--exact-foundations-and-scope"></span>
<span id="oa-flow.top.foundations"></span>
## OA-FLOW.TOP.FOUNDATIONS — Exact foundations and scope

Throughout, a locally compact group is Hausdorff, and Haar measure is a left Haar measure. Banach spaces may have arbitrary dimension and need not be separable. Group actions are genuine homomorphisms; no measurability or continuity is built into the word “representation” below.

We use the following foundational statements, with exactly these meanings:

1. **Banach and separation facts.** A complete metric space is a Baire space. The continuous dual of a normed space is complete; the Hahn–Banach theorem gives the dual norm formula and separates a point from a norm-closed convex subset. Finite-dimensional separation is included. A norm-closed linear subspace is therefore weakly closed. We prove the needed uniform-boundedness consequence of Baire below.
2. **Weak compact convex hull.** If $Q$ is compact for $\sigma(X,X^*)$ in a Banach space $X$, its norm-closed convex hull is weakly compact. Here convex combinations have nonnegative real coefficients summing to one, also when $X$ is complex. This is the weak-compact-convex-hull theorem, used as an exact foundational import. It is not inferred from weak boundedness. The barycenter argument that uses it is proved below.
3. **Haar and compact-support facts.** Left Haar measure is positive on every nonempty open set and finite on compact sets. For each identity neighborhood $V$ there is $f\in C_c(G)$ with $f\geq0$, support contained in $V$, and $\int f=1$. Scalar integrals satisfy linearity, the elementary integral inequality, and left-translation invariance. The space $C_c(G)$ is dense in $L^1(G)$ for this Haar measure. The last density statement is used only for the translation model and one exercise; the main representation theorem uses compactly supported continuous functions directly.
4. **Von Neumann predual facts.** For a von Neumann algebra $M$, its predual $M_*$ is a Banach space with dual $M$. Normal automorphisms preserve $M_*$, positivity, products and adjoints, and are isometric on $M$. Multiplication on either side by a fixed algebra element is ultraweakly continuous. In a faithful normal concrete representation, each normal functional has an absolutely summable vector-functional expansion

$$
\omega(x)=\sum_{j\geq1}\langle x\xi_j,\eta_j\rangle,
\qquad \sum_{j\geq1}\|\xi_j\|\,\|\eta_j\|<\infty.
\tag{1}
$$

Vector functionals themselves are normal, and those with the same vector in both slots are positive. For the commutative translation model, the identification of the predual of $L^\infty(\mathbb R)$ with $L^1(\mathbb R)$ for Lebesgue measure is also a specified foundation.

The weak compact convex hull theorem in item 2 is a prerequisite of the Banach-space argument. We do not presume that a weakly continuous orbit is strongly measurable, essentially norm separably valued, or Bochner integrable.

<a id="OA-FLOW.TOP.BOUNDEDNESS"></a>

<span id="oa-flowtopboundedness--bounds-forced-by-weak-continuity"></span>
<span id="oa-flow.top.boundedness"></span>
## OA-FLOW.TOP.BOUNDEDNESS — Bounds forced by weak continuity

**Uniform-boundedness lemma.** Let $X$ be a Banach space, $Y$ a normed space, and $(T_i)$ any family of bounded linear maps $X\to Y$. If $\sup_i\|T_i x\|<\infty$ for every $x\in X$, then $\sup_i\|T_i\|<\infty$.

**Proof.** The closed sets

$$F_n=\{x:\sup_i\|T_i x\|\leq n\},\qquad n\geq1,$$

cover $X$. By Baire, some $F_n$ contains an open ball about a point $x_0$ of radius $r>0$. For $\|x\|\leq1$, both $x_0$ and $x_0+(r/2)x$ are in that ball. Hence

$$\frac r2\|T_i x\|\leq\|T_i(x_0+(r/2)x)\|+\|T_i x_0\|\leq2n.$$

Taking the supremum over $i$ and the unit ball gives $\sup_i\|T_i\|\leq4n/r$. $\square$

**Corollary.** If $Q\subset X$ is weakly compact, then it is norm bounded. If $U:G\to\operatorname{GL}(X)$ has weakly continuous orbits, then

$$M_L:=\sup_{t\in L}\|U_t\|<\infty$$

for each compact subset $L\subset G$.

**Proof.** Apply the lemma to the evaluation maps $J_x:X^*\to\mathbb C$, $J_x(\ell)=\ell(x)$, indexed by $x\in Q$. For each $\ell$, compactness makes $\sup_{x\in Q}|\ell(x)|$ finite. The dual norm formula gives $\|J_x\|=\|x\|$, proving the first assertion. For the second, $\{U_t x:t\in L\}$ is weakly compact for each fixed $x$, being the continuous image of $L$. It is therefore norm bounded. Apply the uniform-boundedness lemma a second time, now to the family $(U_t)_{t\in L}$. $\square$

The family of operators need not be countable. The countable sets in the Baire argument are the norm-level sets $F_n$, not an enumeration of the group or of an orbit.

<a id="OA-FLOW.TOP.BARYCENTER"></a>

<span id="oa-flowtopbarycenter--weak-averages-really-belong-to-the-banach-space"></span>
<span id="oa-flow.top.barycenter"></span>
## OA-FLOW.TOP.BARYCENTER — Weak averages really belong to the Banach space

**Lemma.** Let $S$ be a compact Hausdorff space with a finite positive Borel measure $\nu$, and let $F:S\to X$ be weakly continuous. There is a unique $b\in X$ such that

$$\ell(b)=\int_S\ell(F(t))\,d\nu(t)\qquad(\ell\in X^*).\tag{2}$$

If $\nu(S)>0$, then $b/\nu(S)$ belongs to the norm-closed convex hull of $F(S)$.

**Proof.** If the measure has mass zero, take $b=0$. Otherwise replace $\nu$ by a probability measure and multiply the answer by its original mass at the end. The set $F(S)$ is weakly compact. Its norm-closed convex hull $Q$ is weakly compact by OA-FLOW.TOP.FOUNDATIONS, item 2, and is convex.

For finitely many functionals $\ell_1,\ldots,\ell_m$, consider the continuous linear map

$$T:X\to\mathbb C^m,\qquad T(x)=(\ell_1(x),\ldots,\ell_m(x)).$$

The set $T(Q)$ is compact and convex in finite dimension. The vector

$$v=\left(\int\ell_1(F(t))\,d\nu(t),\ldots,\int\ell_m(F(t))\,d\nu(t)\right)$$

belongs to $T(Q)$. Indeed, if it did not, real finite-dimensional separation would give a real-linear functional $a$ with $a(v)>\sup_{w\in T(Q)}a(w)$. Since $T(F(t))\in T(Q)$, integrating $a(T(F(t)))$ contradicts that strict inequality.

Thus the closed subsets of $Q$ defined by the equations $\ell(x)=\int\ell(F(t))\,d\nu(t)$ have the finite-intersection property. Weak compactness of $Q$ gives a point in their total intersection. It satisfies (2), and functionals separate points, so it is unique. $\square$

Now suppose $U:G\to\operatorname{GL}(X)$ has weakly continuous orbits. For $f\in C_c(G)$ and $x\in X$, apply the lemma to

$$t\longmapsto f(t)U_t x$$

on the compact support of $f$, with restricted Haar measure. This map is weakly continuous. Its barycenter defines $U(f)x\in X$, characterized by

$$\ell(U(f)x)=\int_G f(t)\ell(U_t x)\,dt.\tag{3}$$

The zero function gives the zero operator. Uniqueness in (2) proves linearity in both $f$ and $x$. For $L$ containing the support of $f$, the dual norm formula and OA-FLOW.TOP.BOUNDEDNESS give

$$\|U(f)x\|\leq M_L\|f\|_1\|x\|,\qquad \|U(f)\|\leq M_L\|f\|_1.\tag{4}$$

All integrals used to construct (3) were scalar integrals followed by a proved barycenter argument. We have not replaced a possibly nonseparable weak orbit by an unproved Bochner integral.

<a id="OA-FLOW.TOP.SMOOTHING"></a>

<span id="oa-flowtopsmoothing--continuous-vectors-from-compact-averages"></span>
<span id="oa-flow.top.smoothing"></span>
## OA-FLOW.TOP.SMOOTHING — Continuous vectors from compact averages

For $s\in G$ write

$$(L_s f)(t)=f(s^{-1}t).$$

**Lemma.** For every $f\in C_c(G)$,

$$\|L_s f-f\|_1\longrightarrow0\qquad(s\to e_G).\tag{5}$$

**Proof.** Choose a compact identity neighborhood $V$, and put $L=V\operatorname{supp}f\cup\operatorname{supp}f$. This is compact. For $s$ in the interior of $V$, both functions in (5) vanish outside $L$.

The function $(s,t)\mapsto f(s^{-1}t)-f(t)$ is continuous and vanishes at $(e_G,t)$ for every $t\in L$. Given $\varepsilon>0$, joint continuity at each such point gives a neighborhood of $e_G$ and a neighborhood of $t$ on which its absolute value is less than $\varepsilon$. Finitely many of the latter neighborhoods cover $L$. Intersecting the corresponding identity neighborhoods shows that

$$\sup_{t\in L}|f(s^{-1}t)-f(t)|\longrightarrow0.$$

Multiplication by the finite Haar measure of $L$ proves (5). $\square$

**Proposition.** For every $f\in C_c(G)$ and $x\in X$, the orbit of $U(f)x$ is norm continuous at $e_G$.

**Proof.** Apply a functional $\ell$ to $U_sU(f)x$. In (3), the functional $\ell\circ U_s$ gives

$$
\ell(U_sU(f)x)=\int_G f(t)\ell(U_{st}x)\,dt
=\int_G f(s^{-1}r)\ell(U_r x)\,dr.
$$

Left Haar invariance justifies the substitution $r=st$; no modular-function factor occurs. Since functionals separate points,

$$U_sU(f)x=U(L_s f)x.\tag{6}$$

For $s$ near the identity, choose the common compact support set $L$ from the preceding lemma. Equations (4)–(6) yield

$$\|U_sU(f)x-U(f)x\|\leq M_L\|L_s f-f\|_1\|x\|\longrightarrow0.$$

The local bound $M_L$ was derived from weak continuity, not added as an extra assumption. $\square$

<a id="OA-FLOW.TOP.BANACH"></a>

<span id="oa-flowtopbanach--the-full-banach-representation-theorem"></span>
<span id="oa-flow.top.banach"></span>
## OA-FLOW.TOP.BANACH — The full Banach representation theorem

**Theorem.** Let $G$ be any locally compact group and $X$ any Banach space. Let $U:G\to\operatorname{GL}(X)$ be a homomorphism into the bounded invertible linear operators. The following are equivalent:

1. For every $x\in X$, the map $t\mapsto U_t x$ is norm continuous.
2. For every $x\in X$ and $\ell\in X^*$, the map $t\mapsto\ell(U_t x)$ is continuous.

**Proof.** Norm continuity implies scalar continuity because every $\ell$ is bounded. Assume scalar continuity and let

$$X_c=\{x\in X:\|U_s x-x\|\to0\text{ as }s\to e_G\}.$$

This is a linear subspace. It is norm closed: on a compact identity neighborhood $V$, let $M_V=\sup_{s\in V}\|U_s\|<\infty$. For $y\in X_c$,

$$\|U_s x-x\|\leq(M_V+1)\|x-y\|+\|U_s y-y\|\qquad(s\in V).\tag{7}$$

If $x$ belongs to the norm closure of $X_c$, first choose $y$ so that the first term is arbitrarily small, and then let $s\to e_G$. This proves $x\in X_c$. Hahn–Banach separation makes $X_c$ weakly closed as well.

For every identity neighborhood $W$, choose $f_W\in C_c(G)$ nonnegative, with support in $W$ and integral one. The vectors $U(f_W)x$ lie in $X_c$ by OA-FLOW.TOP.SMOOTHING. Directly from (3),

$$
|\ell(U(f_W)x)-\ell(x)|
\leq\sup_{t\in W}|\ell(U_t x)-\ell(x)|
$$

whenever the right side is finite; equivalently one may take the supremum over the support of $f_W$. Scalar continuity says that this bound is arbitrarily small once $W$ lies in a sufficiently small prescribed identity neighborhood. Thus, with neighborhoods directed by reverse inclusion,

$$U(f_W)x\longrightarrow x\quad\text{weakly}.$$

Weak closedness of $X_c$ gives $x\in X_c$. Since $x$ was arbitrary, every orbit is norm continuous at the identity. At any $t_0\in G$,

$$\|U_t x-U_{t_0}x\|\leq\|U_{t_0}\|\,\|U_{t_0^{-1}t}x-x\|\longrightarrow0.$$

This proves norm continuity everywhere. $\square$

The proof uses all identity neighborhoods, not a sequence of them. It assumes neither a countable neighborhood base nor norm-separable orbits, and it does not require the operators $U_t$ to be isometries or the group to be unimodular.

Only after this theorem is proved may the averages also be regarded as Bochner integrals without an additional orbit hypothesis: the continuous compactly supported map $t\mapsto f(t)U_t x$ now has norm-compact, hence norm-separable, range. The weak barycenter route supplied the argument before that norm continuity was available.

<a id="OA-FLOW.TOP.PREDUAL"></a>

<span id="oa-flowtoppredual--scalar-tests-for-von-neumann-actions"></span>
<span id="oa-flow.top.predual"></span>
## OA-FLOW.TOP.PREDUAL — Scalar tests for von Neumann actions

Let $M$ be a von Neumann algebra, and let $\alpha:G\to\operatorname{Aut}(M)$ be a homomorphism by normal automorphisms. Define its predual representation by

$$U_t\omega=\omega\circ\alpha_{t^{-1}}\qquad(\omega\in M_*).\tag{8}$$

These maps are surjective linear isometries. They preserve the predual by normality. Isometry follows because an automorphism maps the unit ball of $M$ onto itself. Their order is worth checking:

$$U_sU_t\omega=\omega\circ\alpha_{t^{-1}}\circ\alpha_{s^{-1}}
=\omega\circ\alpha_{(st)^{-1}}=U_{st}\omega.$$

**Theorem.** For a locally compact group $G$, the following conditions are equivalent:

1. For every $x\in M$ and $\omega\in M_*$, the scalar function $t\mapsto\omega(\alpha_t(x))$ is continuous.
2. For every $\omega\in M_*$, the map $t\mapsto\omega\circ\alpha_t$ is norm continuous in $M_*$.
3. Both $t\mapsto\omega\circ\alpha_t$ and $t\mapsto\omega\circ\alpha_t^{-1}$ are norm continuous for every $\omega\in M_*$.

Thus point-ultraweak continuity is exactly continuity into the automorphism topology defined by predual norm orbits and their inverses.

**Proof.** Under condition 1, the representation (8) is weakly continuous as a Banach-space representation of $M_*$. Indeed, every continuous linear functional on $M_*$ is evaluation at an element $x\in M$, and

$$\langle U_t\omega,x\rangle=\omega(\alpha_{t^{-1}}(x))$$

is continuous by condition 1 and continuity of inversion in $G$. OA-FLOW.TOP.BANACH gives norm continuity of $t\mapsto U_t\omega$. Composing again with inversion gives condition 2 and also the inverse orbit required in condition 3. Conversely, condition 2 immediately gives condition 1 by evaluating at a fixed $x$. Condition 3 includes condition 2. $\square$

This theorem supplies the action-topology component of IMP.CP.REGULAR. Its exact Banach, Haar, weak compactness, and predual foundations remain those stated in this lesson. No assertion about regular representation independence or dual weights has entered the proof.

<a id="OA-FLOW.TOP.UTOPOLOGY"></a>

<span id="oa-flowtoputopology--the-automorphism-group-topology-itself"></span>
<span id="oa-flow.top.utopology"></span>
## OA-FLOW.TOP.UTOPOLOGY — The automorphism group topology itself

For an arbitrary net $(\beta_i)$ of normal automorphisms, define $\beta_i\to\beta$ in the **$u$ topology** by

$$\|\omega\circ\beta_i-\omega\circ\beta\|\longrightarrow0\qquad(\omega\in M_*).\tag{9}$$

The inverse-orbit requirements may be added without changing this topology. To prove that assertion, composition on the right by $\beta_i$ is an isometry of $M_*$, so

$$
\begin{aligned}
\|\omega\circ\beta_i^{-1}-\omega\circ\beta^{-1}\|
&=\|\omega-\omega\circ\beta^{-1}\circ\beta_i\|\\
&\longrightarrow0,
\end{aligned}
$$

by applying (9) to the fixed functional $\omega\circ\beta^{-1}$.

This is a Hausdorff group topology. The seminorm tests in (9) define a topology as a subspace of the product of normed predual spaces. They separate automorphisms because normal functionals separate algebra elements. Inversion is continuous by the displayed calculation. If $\beta_i\to\beta$ and $\eta_i\to\eta$, then

$$
\begin{aligned}
\|\omega\circ\beta_i\circ\eta_i-\omega\circ\beta\circ\eta\|
&\leq\|\omega\circ\beta_i-\omega\circ\beta\|\\
&\quad+\|(\omega\circ\beta)\circ\eta_i-(\omega\circ\beta)\circ\eta\|
\longrightarrow0.
\end{aligned}
$$

This proves joint continuity of composition. The argument uses arbitrary nets and does not require $\operatorname{Aut}(M)$ itself to be locally compact or Polish.

<a id="OA-FLOW.TOP.STRONGSTAR"></a>

<span id="oa-flowtopstrongstar--intrinsic-seminorms-and-concrete-bounded-nets"></span>
<span id="oa-flow.top.strongstar"></span>
## OA-FLOW.TOP.STRONGSTAR — Intrinsic seminorms and concrete bounded nets

For $\varphi\in M_*^+$, write

$$p_\varphi(x)=\bigl(\varphi(x^*x)+\varphi(xx^*)\bigr)^{1/2}.$$

Convergence for all these seminorms is called $\sigma$-strong-star convergence. Positivity of $\varphi((a+zb)^*(a+zb))$ for every scalar $z$ gives the Cauchy–Schwarz inequality $|\varphi(b^*a)|^2\leq\varphi(a^*a)\varphi(b^*b)$. It follows that $a\mapsto\varphi(a^*a)^{1/2}$ is a seminorm. Apply this also to adjoints and use the Euclidean triangle inequality to see that $p_\varphi$ is a seminorm. On a norm-bounded set this topology agrees with strong-star convergence in every faithful normal concrete representation.

Here is the exact comparison. Strong-star convergence means convergence of $x_i\xi$ and $x_i^*\xi$ for each vector $\xi$. The vector functionals are among the positive normal functionals, so convergence of all $p_\varphi$ implies this concrete convergence. Conversely suppose $(x_i)$ is uniformly bounded and tends strongly-star to zero. Use the expansion (1) for a positive normal $\varphi$ to write

$$\varphi(x_i^*x_i)=\sum_j\langle x_i\xi_j,x_i\eta_j\rangle.$$

For a fixed finite number of terms the sum tends to zero. The absolute value of its remaining tail is bounded by $\sup_i\|x_i\|^2\sum_{j>n}\|\xi_j\|\,\|\eta_j\|$, uniformly in $i$, and this bound tends to zero as $n\to\infty$. Applying the same argument to $x_i^*$ gives $\varphi(x_i x_i^*)\to0$. This proves the comparison for bounded nets, using the exact normal-functional expansion from OA-FLOW.TOP.FOUNDATIONS.

**Lemma.** If $\beta_i\to\beta$ in the $u$ topology, then $\beta_i(x)\to\beta(x)$ $\sigma$-strong-star for every fixed $x\in M$.

**Proof.** The $u$ convergence gives ultraweak convergence of $\beta_i(y)$ to $\beta(y)$ for every $y$. Set $z_i=\beta_i(x)$ and $z=\beta(x)$. For a positive normal $\varphi$,

$$
\varphi((z_i-z)^*(z_i-z))
=\varphi(\beta_i(x^*x))-
\varphi(\beta_i(x)^*z)-\varphi(z^*\beta_i(x))+\varphi(z^*z).
\tag{10}
$$

The first term tends to $\varphi(\beta(x^*x))=\varphi(z^*z)$ by multiplicativity. Each mixed term tends to $\varphi(z^*z)$ by ultraweak continuity of multiplication by a fixed element and of $\varphi$. Thus (10) tends to zero. Apply the same argument to $x^*$ for the other seminorm term. $\square$

The proof of this lemma in fact only used point-ultraweak convergence of the automorphisms at every algebra element. The stronger predual norm convergence is used in the next result to allow that element to vary.

<a id="OA-FLOW.TOP.JOINT"></a>

<span id="oa-flowtopjoint--simultaneously-varying-the-automorphism-and-the-element"></span>
<span id="oa-flow.top.joint"></span>
## OA-FLOW.TOP.JOINT — Simultaneously varying the automorphism and the element

**Theorem.** Let $\beta_i\to\beta$ in the $u$ topology. Let $(x_i)$ be a uniformly norm-bounded net with $x_i\to x$ strong-star in a faithful normal representation. Then

$$\beta_i(x_i)\longrightarrow\beta(x)\quad\text{strong-star}.\tag{11}$$

Equivalently, on each norm-bounded part of $M$, evaluation is jointly continuous from the $u$ topology and the strong-star topology to the strong-star topology. In particular, for a point-ultraweakly continuous action of a locally compact group,

$$t_i\to t,\quad x_i\to x\text{ strong-star},\quad\sup_i\|x_i\|<\infty
\quad\Longrightarrow\quad\alpha_{t_i}(x_i)\to\alpha_t(x)\text{ strong-star}.\tag{12}$$

**Proof.** Put $y_i=x_i-x$ and choose $R$ with $\|y_i\|\leq R$ for every $i$. For any $\varphi\in M_*^+$, positivity gives

$$
\begin{aligned}
\varphi(\beta_i(y_i)^*\beta_i(y_i))
&=(\varphi\circ\beta_i)(y_i^*y_i)\\
&\leq(\varphi\circ\beta)(y_i^*y_i)
+R^2\|\varphi\circ\beta_i-\varphi\circ\beta\|.
\end{aligned}
\tag{13}
$$

The first term tends to zero because $\varphi\circ\beta$ is positive normal and $y_i$ tends $\sigma$-strong-star to zero by the bounded-set comparison. The second tends to zero by $u$ convergence. Replacing $y_i^*y_i$ by $y_i y_i^*$ proves the other half of $p_\varphi(\beta_i(y_i))\to0$.

By the preceding lemma, $p_\varphi(\beta_i(x)-\beta(x))\to0$. The triangle inequality now gives $p_\varphi(\beta_i(x_i)-\beta(x))\to0$. The output net is norm bounded because automorphisms are isometric. The bounded-set comparison converts this intrinsic convergence back to concrete strong-star convergence, proving (11). Apply OA-FLOW.TOP.PREDUAL to obtain (12). $\square$

The uniform norm bound is used explicitly in (13) and in the representation-independent topology comparison. It is part of the theorem. The statement does not assert joint continuity on an arbitrary unbounded set with the concrete strong-star topology.

