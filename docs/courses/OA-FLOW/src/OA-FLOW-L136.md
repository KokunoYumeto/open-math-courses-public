# Pointwise inner flows and continuous implementers

Suppose every time map of a real action is inner. Choosing one implementing unitary at each time does not automatically produce a representation: the choices may be only measurable, may fail the group law by central factors, and need not be continuous. Under the separable-predual hypothesis, the crossed product turns those imperfect choices into an abelian dual system. Integrability and disintegration then supply an eigenunitary group whose dual character cancels that of the crossed-product generators.

The result is a genuine continuous implementing group inside the original von Neumann algebra. We prove the measurable implementer selection, the vanishing of the real-line commutation defect, the tensor multiplier construction, and the passage from an integrable abelian action to an actual measurable real coordinate. The two dual characters then give the implementing group.

*New expression is dedicated under CC0 to the extent of rights held; inherited component terms remain in force.*

<a id="innerflow.setting"></a>

## The theorem and its exact separability hypothesis

Let $M$ be a nonzero von Neumann algebra with separable predual, and let

$$\alpha:\mathbb R\longrightarrow\operatorname{Aut}(M) \tag{1}$$

be a point-ultraweakly continuous action. Assume that every individual automorphism is inner:

$$\alpha_t\in\operatorname{Int}(M)
\qquad(t\in\mathbb R). \tag{2}$$

We will prove that there is a sigma-strong-star continuous one-parameter unitary group $(U_t)_{t\in\mathbb R}$ in $M$ such that

$$U_{s+t}=U_sU_t,\qquad
\alpha_t=\operatorname{Ad}U_t. \tag{3}$$

Here **separable** means separable predual. It makes the unitary group a Polish parameter space and gives a countable continuous model for the abelian integrable action used below. A faithful normal state alone is insufficient for these countability conclusions. The zero algebra, if allowed, has its unique constant implementing group and may be handled separately.

The factor case already has a different proof in [TP2](OA-FLOW-TP.md#tp-2), using the compact scalar kernel of the projective unitary group. The present theorem allows a nontrivial center; its kernel is the whole central unitary group. We construct the required group without a scalar-kernel assumption.

We use the crossed-product convention fixed in [the normal regular representation](OA-FLOW-NR.md#oa-flow.nr.3). For

$$K=M\rtimes_\alpha\mathbb R \tag{4}$$

write $v_t$ for the canonical unitary, so $v_txv_t^*=\alpha_t(x)$, and write $\theta$ for the dual action:

$$\theta_p(x)=x,\qquad
\theta_p(v_t)=e^{-ipt}v_t. \tag{5}$$

The bounded positive definition of integrability is proved in [L114](OA-FLOW-L114.md#ip-average). The entire dual fixed algebra is proved in [DA](OA-FLOW-DA.md#da-fixed), and the [regular-amplification argument](OA-FLOW-L115.md#dk-regular-integrability) is proved in L115. We use the [continuous abelian model](OA-FLOW-L72.md#oa-flow.model.transport) and the [conditional Haar-orbit theorem](OA-FLOW-L69.md#oa-flow.orbits.conditional). These supply an invariant conull measured model and actual orbit probabilities; no properness of the initial continuous space is assumed.

<a id="innerflow.polish"></a>

## Polish parameter spaces for the implementers

### A countable faithful Hilbert-space model

We first establish the group topologies needed for selection. The internal inputs are [the GNS construction](OA-FLOW-GNS.md#gns-theorem-5-1), [normality of the faithful-state representation](OA-FLOW-STC.md#oa-flow.st.coefficient), [normal faithful representation transport](OA-FLOW-ST12.md#oa-flow.st.2), and [the concrete predual](OA-FLOW-CP.md#oa-flow.cp.6). In particular \(M=(M_*)^*\) isometrically, and its normal functionals are the summable vector series of [CP4](OA-FLOW-CP.md#oa-flow.cp.4).

For precision, the positive normal functionals separate \(M_+\): a nonzero positive concrete operator has strictly positive value on some vector. They span the predual. If \(\omega(x)=\sum_n\langle x\xi_n,\eta_n\rangle\), with both vector sequences square summable, polarization gives
\[
\omega=\frac14\sum_{k=0}^3 i^k\omega_k,\qquad
\omega_k(x)=\sum_n\langle x(\xi_n+i^k\eta_n),\xi_n+i^k\eta_n\rangle.
\tag{PF0}
\]
Each \(\omega_k\) is positive and normal, and its defining positive vector norms have finite sum. Fixed multiplication preserves normal functionals by multiplying one sequence in this vector-series formula by the fixed bounded operator. These facts supply exactly the positivity and normality assertions used next.

The normal-state space is a separable metric subspace of $M_*$. Choose a norm-dense sequence $(\omega_n)_{n\geq1}$ in it and set

$$\varphi=\sum_{n\geq1}2^{-n}\omega_n. \tag{PF1}$$

The sum converges in $M_*$ and is a normal state. If $x\geq0$ and $\varphi(x)=0$, every $\omega_n(x)$ vanishes. Density and positive-functional separation give $x=0$, so $\varphi$ is faithful. Let $(\pi,H,\Omega)$ be its GNS representation, with $\pi(M)\Omega$ dense and $\|\Omega\|=1$.

The unit ball of $M=(M_*)^*$ is compact metrizable for the weak-star topology in this separable case. Here is the needed elementary proof, so Banach–Alaoglu is unnecessary for this step. Choose a norm-dense sequence $(\rho_n)$ in $(M_*)_1$. The metric

$$d_0(x,y)=\sum_{n\geq1}2^{-n}\min\{1,|(x-y)(\rho_n)|\} \tag{PF2}$$

induces the weak-star topology on $M_1$, since the common norm bound extends convergence from the dense tests to every predual functional. From any sequence in $M_1$, successive extraction and a diagonal subsequence make every coordinate converge. Uniform boundedness by one extends the coordinate limits to a linear functional on all of $M_*$ of norm at most one. This functional belongs to $M_1$, and the subsequence converges in $d_0$. Thus $M_1$ is sequentially compact in this metric, hence compact. It is second countable as a subspace of a countable product of complex disks, and therefore has a countable dense subset $D$.

For $y\in M$, the functional $x\mapsto\varphi(y^*x)$ is normal, and

$$\langle\pi(x)\Omega,\pi(y)\Omega\rangle=\varphi(y^*x). \tag{PF3}$$

Approximation of an arbitrary test vector by $\pi(y)\Omega$, using $\|\pi(x)\Omega\|\leq1$ on $M_1$, shows that $x\mapsto\pi(x)\Omega$ is weak-star to weak continuous there. The closed linear span of $\pi(D)\Omega$ is weakly closed: its orthogonal complement characterizes it, by the Hilbert projection theorem. It therefore contains $\pi(M_1)\Omega$ and equals $H$. Rational complex linear combinations of the countably many vectors $\pi(D)\Omega$ are norm dense in $H$. This proves separability without a weak-compact-convex-hull theorem.

On a norm-bounded set, the seminorms from $\varphi$ and its adjoint version determine the intrinsic sigma-strong-star topology. Indeed, positivity of (PF1) gives $\omega_n(a^*a)\leq2^n\varphi(a^*a)$. For any normal state $\omega$ and $\|a\|\leq R$,

$$\omega(a^*a)\leq\omega_n(a^*a)+R^2\|\omega-\omega_n\|. \tag{PF4}$$

First choose a close state, then let $\varphi(a^*a)$ tend to zero. Scaling handles every positive normal functional; apply the same argument to $a^*$.

### A complete metric on the unitary group

For $u,v\in\mathcal U(M)$ put

$$d_\varphi(u,v)=\|(\pi(u)-\pi(v))\Omega\|+\|(\pi(u^*)-\pi(v^*))\Omega\|. \tag{PF5}$$

Faithfulness makes this a metric. By (PF4), it induces the sigma-strong-star topology on the unitary group. Its coordinate embedding into $H\times H$ makes it second countable and separable.

To prove completeness, take a $d_\varphi$-Cauchy sequence $(u_j)$. Equations (PF1) and (PF4), now applied to $u_j-u_k$, make it Cauchy for every positive normal seminorm. For $x\in M$, $a\mapsto\varphi(x^*ax)$ is a positive normal functional, so $\pi(u_j)$ and $\pi(u_j^*)$ are strongly Cauchy on the dense vectors $\pi(x)\Omega$. Their norm-one bounds extend this to all of $H$. They have strong limits $A,B$. Taking scalar inner products gives $B=A^*$, and bounded strong multiplication gives $AB=BA=1$.

The weak-star compactness just proved supplies a subsequence $u_{j_k}\to u\in M_1$. Formula (PF3), with fixed multiplication on both sides, identifies $\pi(u)$ with $A$ on all GNS coefficient pairs. Since $\pi$ is faithful and $A$ is unitary, $u^*u=uu^*=1$. The strong limits on $\Omega$ show $u_j\to u$ in (PF5). Thus this metric is complete. The bounded multiplication estimate and the interchange of the two coordinates under $u\mapsto u^*$ prove that $\mathcal U(M)$ is a Polish group. This proof does not require assuming that an arbitrary strong limit of unitaries is unitary.

<a id="innerflow.automorphisms"></a>

## The automorphism group in the predual topology

For a separable complex Banach space $E$, let $\operatorname{Iso}(E)$ denote the surjective complex-linear isometries. If $(\rho_n)$ is dense in $E_1$, use

$$d_E(S,T)=\sum_{n\geq1}2^{-n}\left(\min\{1,\|(S-T)\rho_n\|\}+\min\{1,\|(S^{-1}-T^{-1})\rho_n\|\}\right). \tag{PF6}$$

A Cauchy sequence gives pointwise norm limits $S,R$ of its maps and inverses, both linear isometries. The estimate

$$\|S_jR_j\rho-SR\rho\|\leq\|R_j\rho-R\rho\|+\|(S_j-S)R\rho\|\longrightarrow0 \tag{PF7}$$

and the reversed estimate give $SR=RS=1$. This proves completeness. The coordinate embedding into $E^{\mathbb N}\times E^{\mathbb N}$ gives second countability and separability. The same estimates give continuous multiplication. If $S_j\to S$ pointwise with $S$ still a surjective isometry, then $\|S_j^{-1}\rho-S^{-1}\rho\|=\|\rho-S_jS^{-1}\rho\|\to0$. Thus the pointwise norm topology itself is Polish and has continuous inversion.

Embed $\operatorname{Aut}(M)$ into $\operatorname{Iso}(M_*)$ by $T_\beta\omega=\omega\circ\beta^{-1}$. This respects multiplication, and its induced topology is the $u$-topology. Suppose $T_{\beta_j}\to T$ in the isometry group, with inverses tending to $S$. Then $A=T^*$ and $B=S^*$ are inverse normal maps on $M$, and $\beta_j^{-1}(x)\to A(x)$, $\beta_j(x)\to B(x)$ ultraweakly for every $x$.

Both limits are unital completely positive. At every fixed matrix size, the positive cone is ultraweakly closed: positivity is tested by the quadratic expressions $\sum_{i,k}\langle x_{ik}\xi_k,\xi_i\rangle$ in any faithful normal concrete representation. Their entries are normal functionals. Hence positivity of each matrix amplification passes to the limit. A unital completely positive map satisfies the Schwarz inequality: apply its second amplification to the positive matrix $\left(\begin{smallmatrix}x^*x&x^*\\x&1\end{smallmatrix}\right)$ and test the resulting quadratic form at $(\xi,-A(x)\xi)$.

Apply these inequalities to the inverse maps:

$$x^*x=B(A(x))^*B(A(x))\leq B(A(x)^*A(x))\leq B(A(x^*x))=x^*x. \tag{PF8}$$

Injectivity of $B$ gives $A(x^*x)=A(x)^*A(x)$. Polarizing this identity gives $A(x^*y)=A(x)^*A(y)$; positivity gives adjoint preservation. Thus $A$ and $B$ are inverse normal star automorphisms, and $T=T_B$. The automorphism image is closed in $\operatorname{Iso}(M_*)$, so $\operatorname{Aut}(M)$ is a Polish group. For the given action, [AT3](OA-FLOW-AT.md#oa-flow.at.3) proves that point-ultraweak continuity implies point-norm continuity of its predual action, so $t\mapsto\alpha_t$ is continuous for this topology. No joint ultraweak continuity of multiplication is used.

### Continuity and fibers of the inner-automorphism map

For a positive normal $\omega$, Cauchy–Schwarz applied to the two terms in

$$\omega(u_jxu_j^*-uxu^*)=\omega((u_j-u)xu_j^*)+\omega(ux(u_j^*-u^*)) \tag{PF9}$$

gives, for $\|x\|\leq1$,

$$\|\omega\circ\operatorname{Ad}u_j-\omega\circ\operatorname{Ad}u\|\leq2\omega(1)^{1/2}\omega((u_j-u)(u_j^*-u^*))^{1/2}\longrightarrow0. \tag{PF10}$$

For the first term use $\omega(u_jx^*xu_j^*)\leq\omega(1)$; for the second use $xx^*\leq1$. Every normal functional is a linear combination of four positive normal functionals, by (PF0), so the result extends to all of $M_*$. Applying it to $u_j^*\to u^*$ gives the convention $T_{\operatorname{Ad}u_j}$. Therefore

$$q:\mathcal U(M)\longrightarrow\operatorname{Aut}(M),
\qquad q(u)=\operatorname{Ad}u, \tag{6}$$

is continuous. Its fibers are exactly the cosets of the closed subgroup $\mathcal U(Z(M))$.

The induced map
\[
\overline q:\mathcal U(M)/\mathcal U(Z(M))
\longrightarrow\operatorname{Aut}(M)
\tag{7}
\]
is one-to-one with image \(\operatorname{Int}(M)\). The preceding continuity of \(q\) makes it continuous for the quotient topology. To obtain a Borel lift of the particular real action, we now give a direct selection and null-set removal argument.

<a id="innerflow.selection"></a>

## Borel implementers at every real parameter

The space \(\mathbb R\times\mathcal U(M)\) is Polish for the metrics just constructed. Let
\[
\mathcal E=\{(t,u):uxu^*=\alpha_t(x)\text{ for every }x\in M\}.
\tag{S1}
\]
This is closed. For fixed \(x\) and fixed GNS vectors, the coefficient of \(uxu^*\) depends continuously on \(u\) in the strong-star topology, and that of \(\alpha_t(x)\) depends continuously on \(t\) by the assumed point-ultraweak continuity. Equality of all coefficients is therefore a closed condition. Intersecting over \(x\) preserves closedness. Equivalently one may use the countable weak-star dense set \(D\subset M_1\) from (PF2) and countably many dense vector tests; normality extends equality from \(D\) to all of \(M\). Every fiber is nonempty by (2).

The earlier programme lesson [SCF5: choosing a witness after completing the measure](../../OA-MOD/OA-MOD-SCF.html#choose-a-witness-after-completing-the-measure) proves completed-measure selection for a Borel relation with Polish witness space. Its proof constructs a closed code, proves measurability of its projected hitting sets in the completed measure, and takes limits in nested closed cells. Apply it to \(\mathcal E\) with the probability measure \(\tfrac12e^{-|t|}\,dt\) on \(\mathbb R\). Its strictly positive density gives exactly the Lebesgue null sets: a zero weighted integral forces zero Lebesgue measure on each set where the density is at least \(1/n\), and these sets exhaust the line. Thus it gives a Lebesgue-measurable selector, initially only measurable in the completion.

Here are the additional steps needed to obtain an everywhere Borel selector. A completed-measurable map into a complete separable metric space has a Borel version off a Borel null set: approximate it by countably valued maps using the first point of a countable \(1/n\)-net within distance \(1/n\). Replace their countably many measurable level sets by Borel versions, remove a Borel null superset of all discrepancies, and take the Cauchy limit there. The set where the Borel approximants are Cauchy is itself Borel. Completeness supplies the limit; give the map the value \(1\) elsewhere. This yields a Borel map \(u^{(0)}:\mathbb R\to\mathcal U(M)\) for which
\[
E=\{t:(t,u^{(0)}_t)\in\mathcal E\}
\quad\text{is Borel and conull.}
\tag{S2}
\]

Choose a compact set \(C\subset E\cap[0,1]\) of positive Lebesgue measure, using [scalar regularity](OA-FLOW-HR.md#hr-03). The overlap function
\[
h(r)=\int_{\mathbb R}1_C(q)1_C(q-r)\,dq
\]
satisfies \(h(0)=|C|>0\) and
\[
|h(r)-h(0)|\le\|1_C(\,\cdot-r)-1_C\|_1\longrightarrow0
\]
by [L24's translation continuity](OA-FLOW-L24.md#oa-flow.grp.translations). Thus \((-\varepsilon,\varepsilon)\subset C-C\) for some \(\varepsilon>0\). For \(r\in C-C\), define
\[
a(r)=\min\{q\in C:q-r\in C\}.
\tag{S3}
\]
The set minimized is nonempty and compact. For each real \(b\),
\[
\{r\in C-C:a(r)\le b\}
=(C\cap(-\infty,b])-C
\]
is compact, so \(a\) is Borel. Consequently
\[
Y_r=u^{(0)}_{a(r)}\bigl(u^{(0)}_{a(r)-r}\bigr)^*
\quad(|r|<\varepsilon)
\tag{S4}
\]
is Borel, has \(Y_0=1\), and implements \(\alpha_r\). Indeed both parameters belong to \(C\subset E\), and
\(\operatorname{Ad}Y_r=\alpha_{a(r)}\alpha_{-(a(r)-r)}=\alpha_r\).

For arbitrary \(t\), set
\[
n(t)=1+\lfloor |t|/\varepsilon\rfloor,\qquad
u_t=Y_{t/n(t)}^{\,n(t)}.
\tag{S5}
\]
Then \(|t/n(t)|<\varepsilon\). On each Borel stratum where the positive integer \(n(t)\) is constant, this is a Borel expression in the continuous unitary operations. Thus
\[
\mathbb R\ni t\longmapsto u_t\in\mathcal U(M),
\qquad\alpha_t=\operatorname{Ad}u_t
\tag{8}
\]
is Borel for **every** \(t\), with \(u_0=1\). The equality follows by composing the same automorphism \(\alpha_{t/n(t)}\) exactly \(n(t)\) times. No group law or continuity for the selected \(u_t\) has been asserted.

More generally an initial value \(u_0\) of any implementer selector is central; multiplication of the entire field by \(u_0^*\) normalizes it at zero. A scalar normalization would not suffice for an arbitrary center.

<a id="innerflow.defect"></a>

## The central commutation defect is a bicharacter

Because the action group is abelian,

$$\operatorname{Ad}(\alpha_t(u_s))
=\alpha_t\alpha_s\alpha_{-t}
=\alpha_s
=\operatorname{Ad}u_s. \tag{9}$$

Thus there is a central unitary

$$\chi(s,t)=\alpha_t(u_s)u_s^*\in\mathcal U(Z(M)) \tag{10}$$

such that $\alpha_t(u_s)=\chi(s,t)u_s$. Joint Borel measurability follows from the Borel implementer field, [joint bounded strong-star continuity of evaluation](OA-FLOW-AT.md#oa-flow.at.4), and the algebra operations on the unitary group.

Every $\alpha_t$ fixes the center pointwise because it is inner. Therefore

$$
\begin{aligned}
\chi(r,s+t)&=\chi(r,s)\chi(r,t),\\
\chi(s,t)&=\chi(t,s)^*,\\
\chi(s,s)&=1.
\end{aligned} \tag{11}$$

For the first identity, apply $\alpha_s\alpha_t$ to $u_r$ and use center fixation. For the second, the two formulas

$$u_tu_s=\chi(s,t)u_su_t,
\qquad
u_su_t=\chi(t,s)u_tu_s \tag{12}$$

give $\chi(s,t)\chi(t,s)=1$. The last identity is direct:

$$\alpha_s(u_s)=u_su_su_s^*=u_s. \tag{13}$$

For fixed $r$, continuity in $t$ follows directly from the action on the one unitary $u_r$. In a faithful normal representation, the unitary field $w_t=\alpha_t(u_r)$ is weak-operator continuous because the action is point-ultraweakly continuous. At any $t_0$ and for any vector $\xi$,

$$\|(w_t-w_{t_0})\xi\|^2
   =2\|\xi\|^2-2\operatorname{Re}
       \langle w_t\xi,w_{t_0}\xi\rangle
   \longrightarrow0. \tag{13a}$$

Apply the same identity to $w_t^*=\alpha_t(u_r^*)$. Thus $w_t$ is strong-star continuous. On bounded sets the faithful-normal strong-star topology is the intrinsic sigma-strong-star topology, so multiplication by the fixed $u_r^*$ makes $t\mapsto\chi(r,t)$ continuous. Skew symmetry in (11), together with continuous adjunction on unitaries, gives continuity in the first variable. We have a separately continuous central-unitary bicharacter with trivial diagonal; no automatic-continuity theorem for Borel homomorphisms is needed in this step.

<a id="innerflow.trivial"></a>

## Every alternating bicharacter of the real line is trivial

Bicharacter homogeneity gives, for integers $m,n$,

$$\chi(mr,s)=\chi(r,s)^m=\chi(r,ms). \tag{14}$$

If $p=m/n\in\mathbb Q$ with $n\neq0$, two uses of (14) yield

$$\chi(p,q)
=\chi(1/n,mq)
=\chi(1,mq/n)
=\chi(1,pq) \tag{15}$$

for every real $q$. For rational $t$, equations (11) and (15) give

$$\chi(1,t^2)=\chi(t,t)=1. \tag{16}$$

The squares of rational numbers are dense in $[0,\infty)$. Continuity of $r\mapsto\chi(1,r)$ therefore makes it $1$ on the nonnegative half-line, and the character identity makes it $1$ on the negative half-line too. Equation (15) now shows $\chi(p,q)=1$ whenever $p$ is rational. Continuity in the first variable and density of $\mathbb Q$ prove

$$\boxed{\chi(s,t)=1\quad(s,t\in\mathbb R).} \tag{17}$$

Consequently

$$\alpha_t(u_s)=u_s,\qquad
u_su_t=u_tu_s. \tag{18}$$

This argument never assumes that the originally selected map $s\mapsto u_s$ is continuous. Separate continuity of the bicharacter follows from point-ultraweak continuity of the action on each fixed $u_r$, then from skew symmetry. Borel measurability is used later to construct the measurable diagonal unitary $\mathcal W$ in (27).

<a id="innerflow.abelian"></a>

## An abelian eigenoperator algebra in the crossed product

Inside $K$ define

$$a_s=u_sv_s^*\qquad(s\in\mathbb R). \tag{19}$$

For $x\in M$,

$$a_sxa_s^*
=u_s\alpha_{-s}(x)u_s^*=x, \tag{20}$$

so $a_s\in M'\cap K$. Equation (18) also gives

$$v_ta_sv_t^*
=\alpha_t(u_s)v_s^*=a_s. \tag{21}$$

Thus every $a_s$ commutes with every canonical generator $v_t$. It follows again from (18), (21), and commutativity of the real group that

$$a_sa_t=a_ta_s. \tag{22}$$

Let

$$B=W^*(a_s:s\in\mathbb R)\subset M'\cap K. \tag{23}$$

This is an abelian von Neumann algebra. To check separable predual, realize the regular crossed product faithfully on \(L^2(\mathbb R,H)\), with the separable \(H\) constructed above; [NR3](OA-FLOW-NR.md#oa-flow.nr.3) supplies the normal coefficient embedding. Scalar step functions on rational intervals and a countable dense family in \(H\) make this Hilbert space separable. Its projective predual is separable: finite rational linear combinations of tensors from a countable dense vector set are dense in the projective completion. By [CP6](OA-FLOW-CP.md#oa-flow.cp.6), the preduals of \(K\) and its concrete von Neumann subalgebra \(B\) are quotients of this separable space. In particular \(B_*\) is separable. It commutes with all \(v_t\). By (5),

$$\theta_p(a_s)=e^{ips}a_s. \tag{24}$$

Hence $B$ is globally invariant under the restricted dual action

$$\beta_p=\theta_p|_B. \tag{25}$$

The family $(a_s)$ need not be a representation. What matters here is commutativity, Borel dependence on $s$, and the complete set of eigenrelations (24).

<a id="innerflow.twist"></a>

## A measurable diagonal unitary untwists the amplification

Let $P_p$ be the multiplication representation on $L^2(\mathbb R)$,

$$ (P_p\xi)(r)=e^{ipr}\xi(r). \tag{26}$$

Use the faithful separable representation of \(B\) just obtained. The map \(r\mapsto a_r=u_rv_r^*\) is strong-star Borel: the coefficient embedding is normal, hence continuous on bounded strong-star sets by [ST2](OA-FLOW-ST12.md#oa-flow.st.2), and \(v_r\) is strongly continuous. Define the operator on square-integrable vector fields by \((\mathcal W\xi)(r)=a_r\xi(r)\). Borel fixed-vector maps and simple approximation make this vector field measurable. Pointwise norm preservation and the Borel adjoint field give a unitary with inverse \(\xi(r)\mapsto a_r^*\xi(r)\). We next justify the tensor-algebra membership in

$$\mathcal W=\int_{\mathbb R}^{\oplus}a_r\,dr
\in B\ \overline\otimes\ L^\infty(\mathbb R)
\subset B\ \overline\otimes\ B(L^2(\mathbb R)). \tag{27}$$

Choose a countable strong-star dense sequence \((b_j)\) in \(\mathcal U(B)\), using the Polish unitary proof above for \(B\). For each \(n,r\), let \(a^{(n)}_r\) be the first \(b_j\) within distance \(1/n\) of \(a_r\), and let \(E_{nj}\) be its Borel level sets. For fixed \(n\), the finite sums
\[
\sum_{j\le m}b_j\otimes1_{E_{nj}}
\]
belong to \(B\bar\otimes L^\infty(\mathbb R)\), have norm at most one, and converge strongly together with their adjoints to multiplication by \(a^{(n)}\). The squared tail norm on a vector field is bounded by its squared integral over the unused partition cells. As \(n\to\infty\), pointwise strong-star convergence and the bound \(2\|\xi(r)\|\) permit dominated convergence for operators and adjoints. Thus their strong-star limit is \(\mathcal W\), proving (27).

Normal amplification has the expected action on this field. If \((e_i)\) is a scalar orthonormal basis of \(L^2(\mathbb R)\), the \((i,j)\) entry is the ultraweak integral
\[
c_{ij}=\int_{\mathbb R}e_j(r)\overline{e_i(r)}a_r\,dr\in B.
\]
The integrand paired with \(\omega\in B_*\) has absolute integral at most \(\|\omega\|\|e_i\|_2\|e_j\|_2\), so [CP6](OA-FLOW-CP.md#oa-flow.cp.6) constructs this element. Pairing \(\beta_p(c_{ij})\) replaces \(\omega\) by \(\omega\circ\beta_p\). The normal amplification constructed in [TW1](OA-FLOW-TW.md#tw-1) is determined by all these entries; hence it sends \(\mathcal W\) to multiplication by \(\beta_p(a_r)\). This proves that the next field identity is an identity in the actual tensor algebra. The same construction, with general eigenfields, is [DS4](OA-FLOW-DS.md#ds-4).

Equation (24) gives

$$ (\beta_p\otimes\operatorname{id})(\mathcal W)
=(1\otimes P_p)\mathcal W. \tag{28}$$

Both factors on the right are decomposable and commute. Therefore, for every $X\in B\overline\otimes B(L^2(\mathbb R))$,

$$
\begin{aligned}
&\operatorname{Ad}(\mathcal W^*)
\circ(\beta_p\otimes\operatorname{id})
\circ\operatorname{Ad}(\mathcal W)(X)\\
&\hspace{35mm}
=(1\otimes P_p)(\beta_p\otimes\operatorname{id})(X)(1\otimes P_p^*).
\end{aligned} \tag{29}$$

Equivalently,

$$\boxed{
\beta_p\otimes\operatorname{Ad}P_p
=\operatorname{Ad}(\mathcal W^*)
\circ(\beta_p\otimes\operatorname{id})
\circ\operatorname{Ad}(\mathcal W).} \tag{30}$$

Thus the action with a regular inner factor is conjugate to the action with a trivial second factor.

<a id="innerflow.integrability"></a>

## Integrability passes through a fixed full corner

For an action $\gamma$ of $\mathbb R$ on a von Neumann algebra $N$, write

$$
\mathcal P_\gamma^+
=\left\{x\in N_+:
\sup_{C\Subset\mathbb R}
\left\|\int_C\gamma_p(x)\,dp\right\|<\infty\right\}. \tag{31}$$

The action is integrable when the complex span of this positive domain is ultraweakly dense.

The regular-amplification lemma says that

$$\beta\otimes\operatorname{Ad}P
\quad\text{on}\quad B\overline\otimes B(L^2(\mathbb R)) \tag{32}$$

is integrable. Here is the bounded positive cutoff argument. Let $R_p\xi(x)=\xi(x+p)$ and let $\mathcal F$ be the unitary Fourier transform with kernel $(2\pi)^{-1/2}e^{-irx}$, so $\mathcal F R_p\mathcal F^*=P_p$. For a compact measurable $C\subset\mathbb R$, put $T_C=\mathcal F M_{1_C}\mathcal F^*$. Translation and Tonelli give

$$\int_{\mathbb R}\operatorname{Ad}P_p(T_C)\,dp
   =|C|1,\qquad
   T_C\uparrow1\text{ strongly}. \tag{32a}$$

The first equality follows from $R_pM_{1_C}R_p^*=M_{1_C(\,\cdot+p)}$; increasing compact intervals give the second. Therefore $e_C=1\otimes T_C$ lies in the positive domain of $\gamma=\beta\otimes\operatorname{Ad}P$. For every $X\ge0$, the inequality $0\le e_CXe_C\le\|X\|e_C$ bounds its orbit integral by $\|X\||C|1$, while $e_CXe_C\to X$ strongly. Thus the positive domain is ultraweakly dense. The Fourier convention and Plancherel unitary are proved in [FF2–FF3](OA-FLOW-FF.md#oa-flow.ff.2); the translation convention here is \(R_p\xi(x)=\xi(x+p)\). This transports the multiplication-cutoff argument of [L115](OA-FLOW-L115.md#dk-regular-integrability).

Conjugacy (30) preserves the positive domain and its density, so $\beta\otimes\operatorname{id}$ is integrable. Let $e$ be a rank-one projection in $B(L^2(\mathbb R))$ and put $q=1\otimes e$. The projection \(q\) is fixed by \(\beta\otimes\operatorname{id}\) and has full central support: choose an orthonormal basis starting with a unit vector in \(eL^2(\mathbb R)\), and let \(w_j\) be the rank-one partial isometries sending that vector to the basis vectors. The projections \((1\otimes w_j)q(1\otimes w_j)^*\) sum strongly to \(1\). Any central projection dominating \(q\) dominates them all, and hence equals \(1\). For $X\in\mathcal P_{\beta\otimes\operatorname{id}}^+$,

$$
\int_C(\beta_p\otimes\operatorname{id})(qXq)\,dp
=q\left(\int_C(\beta_p\otimes\operatorname{id})(X)\,dp\right)q. \tag{33}$$

Thus fixed compression preserves bounded orbit integrals. Compressing an ultraweakly dense integrability domain gives an ultraweakly dense domain in the corner, and

$$q\bigl(B\overline\otimes B(L^2(\mathbb R))\bigr)q\cong B. \tag{34}$$

It follows that $(B,\mathbb R,\beta)$ is an integrable abelian separable covariant system. The conclusion uses the dense bounded-value domain (31), not merely the existence of the eigenoperators (24).

<a id="innerflow.orbits"></a>

## Transitive disintegration has trivial stabilizers

The [continuous-model theorem L72](OA-FLOW-L72.md#oa-flow.model.transport) identifies \(B\) normally with \(L^\infty(X,\lambda)\) for a locally compact second-countable space \(X\), a continuous real action \(T_p\), and a quasi-invariant Radon probability. Its convention is
\[
\beta_p(F)(x)=F(T_{-p}x).
\tag{C1}
\]
It identifies the whole bounded averaging cone with the scalar orbit-integrability condition. The [Haar-orbit theorem L69](OA-FLOW-L69.md#oa-flow.orbits.selector) therefore supplies an invariant conull Borel \(X_1\), a Borel quotient \(q:X_1\to Q\) whose fibers are the actual orbits, a Borel section \(s:Q\to X_1\), and conditional probabilities \(\lambda_q\). On one conull Borel base, these probabilities have exactly the Haar orbit null sets. The stabilizers \(H_q=\{p:T_ps(q)=s(q)\}\) are compact and form a Borel field, by [L69's stabilizer proof](OA-FLOW-L69.md#oa-flow.orbits.stabilizers). Its [homogeneous-fiber proof](OA-FLOW-L69.md#oa-flow.orbits.homogeneous) gives the equivariant normal decomposition

$$ (B,\mathbb R,\beta)
\cong
\int_Q^{\oplus}
\bigl(L^\infty(\mathbb R/H_q),\mathbb R,\operatorname{lt}\bigr)
\,d\nu(q). \tag{35}$$

The fiber measures have the quotient-Haar class. Choose the negative orbit coordinate \(r\mapsto T_{-r}s(q)\), so the algebra action denoted \(\operatorname{lt}_p\) in (35) is \(f(r)\mapsto f(r+p)\). The homogeneous-fiber identification is Borel in both directions on each orbit and normal on its \(L^\infty\) algebra. This is a measured decomposition; properness of the originally chosen space \(X\) is unnecessary. Compactness already forces a subgroup of \(\mathbb R\) to be trivial: if it contained \(h\ne0\), its integer multiples would be unbounded. The following eigenrelation argument also verifies the needed freeness directly and records exactly how a common conull set is obtained.

Take \(D=\mathbb Q\). Choose a bounded Borel representative for each of the countably many \(a_s\), \(s\in D\). The equation \(|a_s|=1\) fails only on a \(\lambda\)-null set. For each \(p,s\in D\), the discrepancy
\[
a_s(T_{-p}x)-e^{ips}a_s(x)
\]
also vanishes \(\lambda\)-almost everywhere. Apply the conditional-probability identity to its absolute value and to \(||a_s|-1|\). Each has zero integral on almost every fiber. Intersect the resulting countably many conull Borel base sets with the Haar-class set from L69. Thus all unitary and rational eigenrelations hold on one common conull base. The translation action on every homogeneous Haar fiber is point-ultraweakly continuous, proved by \(L^2\) translation and vector-series tests in [L69](OA-FLOW-L69.md#oa-flow.orbits.ergodic). For each \(s\in D\), its rational-parameter eigenrelation therefore extends by continuity to every real \(p\). Fix $q$ in that common set. On the fiber $L^\infty(\mathbb R/H_q)$, the nonzero unitary component $a_s(q)$ satisfies

$$\operatorname{lt}_p(a_s(q))=e^{ips}a_s(q)
\qquad(p\in\mathbb R, s\in D). \tag{36}$$

If $h\in H_q$, translation by $h$ is the identity on this fiber. Taking $p=h$ in (36) gives

$$e^{ihs}=1\qquad(s\in D). \tag{37}$$

No nonzero $h$ has this property for a dense set $D$. Hence $H_q=\{0\}$ almost everywhere. The following explicit coordinate construction realizes (35), after restriction to this invariant conull set, as

$$B\cong L^\infty(Q\times\mathbb R,\mu),
\qquad
(\beta_p f)(q,r)=f(q,r+p), \tag{38}$$

Here is the joint measurable identification needed for (38). Define
\[
\Psi:Q\times\mathbb R\longrightarrow X_1,\qquad
\Psi(q,r)=T_{-r}s(q).
\tag{C2}
\]
It is Borel because \(s\) is Borel and the action is continuous. Each orbit is a fiber of \(q\), so it is onto; triviality of the stabilizers makes it one-to-one. Its inverse is explicitly \(x\mapsto(q(x),r(x))\). To prove measurability of the real coordinate, fix a compatible metric \(d_X\) and a compact interval \(I\). Then
\[
r(x)\in I
\quad\Longleftrightarrow\quad
\inf_{t\in I}d_X(T_{-t}s(q(x)),x)=0.
\tag{C3}
\]
Compactness of \(I\) and continuity in \(t\) ensure attainment, so zero infimum really gives the unique parameter. The infimum equals that over a fixed countable dense subset of \(I\), and every such test is Borel in \(x\). Closed intervals with rational endpoints generate the real Borel sigma-algebra. Hence \(r\) and the inverse of \(\Psi\) are Borel.

Pull \(\lambda\) back by this bijection. For every Borel \(A\subset Q\times\mathbb R\), the conditional formula and the Haar equivalence on the common conull base give
\[
\lambda(\Psi(A))=0
\ \Longleftrightarrow\
|A_q|=0\text{ for }\nu\text{-almost every }q
\ \Longleftrightarrow\
(\nu\otimes dr)(A)=0.
\tag{C4}
\]
The final equivalence is Tonelli; measurability of \(\Psi^{-1}\) ensures that \(\Psi(A)\) is Borel. Thus the pulled measure has precisely the product Haar null sets, and we may use \(\mu=\nu\otimes dr\) in (38). Pullback and its inverse preserve bounded increasing suprema, so [NF6](OA-FLOW-NF.md#oa-flow.nf.6) makes the two algebra maps normal. Formula (C1) and the negative sign in (C2) give exactly \(f(q,r)\mapsto f(q,r+p)\). This also proves that the measurable product coordinate, its measure class and the stated action belong to the same model.

The fixed algebra in this model is \(L^\infty(Q,\nu)\), by [L69's fixed-algebra theorem](OA-FLOW-L69.md#oa-flow.orbits.ergodic). The countable eigenrelations were used on one common conull set, rather than on a different exceptional set for each frequency.

<a id="innerflow.eigengroup"></a>

## The translation coordinate supplies a positive-character group

In the model (38), define

$$b_s(q,r)=e^{isr}
\qquad(s\in\mathbb R). \tag{39}$$

These multiplication operators form a genuine unitary group in $B$:

$$b_{s+t}=b_sb_t,\qquad b_0=1. \tag{40}$$

Dominated convergence on the standard representation proves sigma-strong-star continuity in $s$. Equivalently, the real coordinate is a selfadjoint operator affiliated with $B$ and $b_s$ is its bounded exponential. Translation gives the positive dual character

$$\boxed{\beta_p(b_s)=e^{ips}b_s.} \tag{41}$$

This sign is chosen to cancel the negative character of $v_s$ in (5). The original eigenoperators $a_s$ were used to force the free translation model; the new family $b_s$ is the genuine group extracted from that model.

<a id="innerflow.cancellation"></a>

## Dual-character cancellation returns the group to M

Define in the crossed product

$$U_s=b_sv_s. \tag{42}$$

The algebra $B$ commutes with every $v_t$ by (21) and (23). Therefore (40) and the group law for $v$ give

$$U_sU_t=b_sb_tv_sv_t=b_{s+t}v_{s+t}=U_{s+t}. \tag{43}$$

Both factors are sigma-strong-star continuous, so $(U_s)$ is a continuous one-parameter unitary group in $K$.

Now track the two characters exactly. Equations (5) and (41) give

$$\theta_p(U_s)
=\theta_p(b_s)\theta_p(v_s)
=e^{ips}b_s\,e^{-ips}v_s
=U_s. \tag{44}$$

The [full dual fixed-algebra theorem, DA](OA-FLOW-DA.md#da-fixed) proves that the fixed-point algebra of this dual action is the canonical normal copy of $M$. Thus $U_s\in M$. The coefficient embedding from [NR3](OA-FLOW-NR.md#oa-flow.nr.3) has a normal inverse on its image by [ST2](OA-FLOW-ST12.md#oa-flow.st.2); composing positive normal seminorms with this inverse transports bounded sigma-strong-star continuity back to the original algebra. Hence the group is continuous in $M$ itself. Finally $b_s\in B\subset M'\cap K$, so for $x\in M$,

$$\operatorname{Ad}U_s(x)
=b_sv_sxv_s^*b_s^*
=\alpha_s(x). \tag{45}$$

Equation (21), which came from $\alpha_t(u_s)=u_s$, is what proves that $B$ commutes with $v_t$. Relative commutation with $M$ alone would not justify the group calculation (43).

<a id="innerflow.theorem"></a>

## The continuous implementation theorem

Combining (43)–(45) proves the promised statement:

$$\boxed{
\begin{gathered}
M_*\text{ separable},\quad
\alpha:\mathbb R\to\operatorname{Aut}(M)\text{ continuous},\quad
\alpha_t\text{ inner for every }t\\
\Longrightarrow\quad
\exists\ (U_t)_{t\in\mathbb R}\subset\mathcal U(M)
\text{ sigma-strong-star continuous},\\
U_{s+t}=U_sU_t,\qquad \alpha_t=\operatorname{Ad}U_t.
\end{gathered}} \tag{46}$$

The construction distinguishes four objects that should not be conflated: the Borel implementers $u_s$, the commuting relative-commutant eigenoperators $a_s=u_sv_s^*$, the genuine positive-character group $b_s\in B$, and the final fixed unitaries $U_s=b_sv_s\in M$. Only the last family is the implementing group required by the theorem.

No assertion is made here after removing separable predual. The measurable selection and common-conull disintegration are substantive hypotheses, not automatic consequences of sigma-finiteness.

<a id="innerflow.diagnostics"></a>

## Two choices that the construction must distinguish

**A Borel implementer field can fail both continuity and the group law.** Take \(M=\mathbb C\) and \(\alpha_t=\operatorname{id}\). Put \(u_t=1\) for rational \(t\) and \(u_t=-1\) for irrational \(t\). This is Borel and implements every time map, with \(u_0=1\). Every interval contains rationals and irrationals, so the field is nowhere continuous. Also \(u_{\sqrt2}^2=1\), whereas \(u_{2\sqrt2}=-1\), so it is not a representation. In the crossed product, \(a_t=u_tv_t^*\) still has the eigenrelation (24); the genuine choice \(b_t=v_t^*\) gives \(U_t=1\). Thus the correction acts on the family of choices, even when the underlying action is already trivial.

**The negative dual phase must be canceled by a positive one.** If a proposed group \(c_s\) instead satisfies \(\theta_p(c_s)=e^{-ips}c_s\), then
\[
\theta_p(c_sv_s)=e^{-2ips}c_sv_s.
\]
For \(s\ne0\), choose \(p=\pi/(2s)\); the phase is \(-1\), so this nonzero unitary is not dual fixed. It cannot be asserted to lie in the coefficient algebra. Equations (5), (41) and (44) give the required opposite phases without changing the crossed-product convention.

The mathematical source is M. Takesaki, *Theory of Operator Algebras II*, Theorem XI.3.11 and Lemma XI.3.12, printed pages 357–358 ([edition record](https://doi.org/10.1007/978-3-662-10451-4)). The lesson treats all von Neumann algebras with separable predual, with the crossed-product dual convention (5).
