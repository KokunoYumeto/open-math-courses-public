<span id="kernels-local-fixed-parts-and-freeness"></span>
# Kernels, local fixed parts, and freeness

*CC0 1.0.*

The [largest identity-part projection and intertwining-multiplier theorem](../../reader/supplements/kernels-and-freeness.html#OA-FLOW.KERNEL.PROJECTION) supplies the projection used in the covariance and abelian-action proofs below.

An action can be ergodic even when some nonidentity group elements do nothing. The right first step is to identify the kernel. A second issue is local: an automorphism can move part of an algebra while acting identically on a nonzero summand. We will detect that summand by a projection, before choosing any measure-space realization.

<a id="OA-FLOW.KERNEL.FOUNDATIONS"></a>

<span id="oa-flowkernelfoundations--setting-and-exact-prerequisites"></span>
<span id="oa-flow.kernel.foundations"></span>
## OA-FLOW.KERNEL.FOUNDATIONS — Setting and exact prerequisites

Let $M$ be a nonzero commutative von Neumann algebra with identity $1$. All automorphisms are unital and normal. Initially $G$ is an arbitrary group with identity $e_G$, and

$$
\alpha:G\longrightarrow\operatorname{Aut}(M),\qquad
\alpha_{gh}=\alpha_g\alpha_h
$$

is a group homomorphism. No topology, countability, separable predual, faithful normal state, or measure-space presentation is required for the algebraic results.

We use the elementary realization of $M$ as a strongly closed algebra on a Hilbert space, bounded functional calculus, and the fact that a von Neumann algebra's normal functionals separate its elements. The required projection and support arguments are proved in the [largest identity-part projection theorem](../../reader/supplements/kernels-and-freeness.html#OA-FLOW.KERNEL.PROJECTION). These basic operator-algebra foundations are prerequisites, not new proofs of the representation theorem for abstract von Neumann algebras. The point-space statements additionally use countable separating families for standard Borel spaces and elementary measure theory; the periodic-flow example uses Fubini's theorem for finite Lebesgue measure. No modular theory, operator-valued weight, disintegration theorem, or crossed-product theorem is imported.

For the periodic-flow continuity argument, the precise additional measure-theory import is $L^\infty(\mathbb R/\mathbb Z,m)_*=L^1(\mathbb R/\mathbb Z,m)$ under integration, where $m$ is normalized Lebesgue measure. Thus testing against every $L^1$ density tests every normal functional. This foundational identification is not proved in this unit.

Write

$$
M^\alpha=\{x\in M:\alpha_g(x)=x\text{ for every }g\in G\},
\qquad
K=\ker\alpha=\{g\in G:\alpha_g=\operatorname{id}_M\}.
$$

The action is **ergodic** when $M^\alpha=\mathbb C1$ and **faithful** when $K=\{e_G\}$. A nonzero projection $p$ is an **identity part** for an automorphism $\beta$ when $\beta(p)=p$ and the restriction of $\beta$ to $Mp$ is the identity. We call $\beta$ **free** when it has no identity part. The action is **free** when $\alpha_g$ is free for every $g\ne e_G$.

This is a definition on the algebra. A pointwise action and a common conull set of free points are separate objects, treated below. Also, $M^\beta$ records globally fixed elements; it does not itself identify the region where every element is fixed.
<a id="OA-FLOW.KERNEL.COVARIANCE"></a>

<span id="oa-flowkernelcovariance--transport-and-commuting-symmetries"></span>
<span id="oa-flow.kernel.covariance"></span>
## OA-FLOW.KERNEL.COVARIANCE — Transport and commuting symmetries

**Proposition.** For $\beta,\gamma\in\operatorname{Aut}(M)$,

$$
p_{\gamma\beta\gamma^{-1}}=\gamma(p_\beta).
\tag{4}
$$

If a family of automorphisms commutes with $\beta$ and its common fixed algebra is $\mathbb C1$, then $\beta$ is either the identity or free.

**Proof.** Apply $\gamma$ to $\beta(x)p_\beta=xp_\beta$ and replace $\gamma(x)$ by an arbitrary $y\in M$. The result says that $\gamma(p_\beta)$ satisfies the defining identity for $\gamma\beta\gamma^{-1}$. Thus $\gamma(p_\beta)\leq p_{\gamma\beta\gamma^{-1}}$. Applying the same reasoning with $\gamma^{-1}$ gives the reverse inequality. If $\gamma$ commutes with $\beta$, (4) gives $\gamma(p_\beta)=p_\beta$. Under the stated common fixed-algebra hypothesis, $p_\beta$ is a scalar projection and therefore is $0$ or $1$. Equation (1) says that $p_\beta=1$ is equivalent to $\beta=\operatorname{id}$; the preceding proposition says that $p_\beta=0$ is equivalent to freeness. $\square$

For completeness, ergodicity can equivalently be stated by saying that the only projections fixed by every automorphism in the family are $0$ and $1$. One implication is immediate. For the other, any common fixed self-adjoint element has all its spectral projections fixed, by normality and spectral functional calculus. If it were nonscalar, a spectral cut strictly between two points of its spectrum would be a nonzero proper fixed projection. Thus every common fixed self-adjoint element is scalar. Taking real and imaginary parts proves that the common fixed algebra is $\mathbb C1$.

<a id="OA-FLOW.KERNEL.ABELIAN"></a>

<span id="oa-flowkernelabelian--the-ergodic-dichotomy-and-effective-quotient"></span>
<span id="oa-flow.kernel.abelian"></span>
## OA-FLOW.KERNEL.ABELIAN — The ergodic dichotomy and effective quotient

**Theorem.** Let $G$ be an arbitrary abelian group acting ergodically on $M$. Then

$$
p_{\alpha_g}=
\begin{cases}
1,&g\in K,\\
0,&g\notin K.
\end{cases}
\tag{5}
$$

Consequently, the action is free if and only if it is faithful. For an arbitrary kernel $K$, the action

$$
\overline\alpha:G/K\longrightarrow\operatorname{Aut}(M),
\qquad \overline\alpha_{gK}=\alpha_g
\tag{6}
$$

is well defined, faithful, ergodic, and free.

**Proof.** Every $\alpha_h$ commutes with $\alpha_g$. The preceding proposition applies to the ergodic family $\alpha(G)$, so each $p_{\alpha_g}$ is either $0$ or $1$. Its value is $1$ exactly when $\alpha_g$ is the identity, that is, when $g\in K$. This proves (5).

If the action is faithful, no $g\ne e_G$ lies in $K$, and (5) proves freeness. Conversely, a nonidentity element of $K$ fixes the nonzero projection $1$ pointwise, contradicting freeness. This converse does not require ergodicity or commutativity of $G$.

As the kernel of a homomorphism, $K$ is a normal subgroup. If $gK=hK$, then $h^{-1}g\in K$, so $\alpha_g=\alpha_h$; hence (6) is well defined and is a homomorphism. If $\overline\alpha_{gK}=\operatorname{id}$, then $g\in K$, proving faithfulness. The two actions have the same set of automorphisms and therefore the same fixed algebra. Finally $G/K$ is abelian, so the already proved faithful case applies. $\square$

The proof does not use a countable union of projections or null sets. In particular, it applies when $G$ is uncountable or $M$ has nonseparable predual. If $M=\mathbb C$, every action is ergodic and $K=G$; the effective quotient is the trivial group, whose freeness is vacuous. If $G$ is not abelian, (4) still gives

$$
\alpha_h(p_{\alpha_g})=p_{\alpha_{hgh^{-1}}}.
\tag{7}
$$

Thus central group elements satisfy the same dichotomy under ergodicity. General elements need not do so.
