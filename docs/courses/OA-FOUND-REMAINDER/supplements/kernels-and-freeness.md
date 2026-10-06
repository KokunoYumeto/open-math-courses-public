# Identity parts and the algebraic freeness criterion

*Retained original OA-FLOW lesson 06 proof under its recorded exact published CC0 component grant. Scoped selection and bindings by GPT-6.1 Sol (OpenAI), Ultra, October 2026; original contributions CC0. The original source has no individual model attribution in this section.*

This supplement treats the algebraic setting, largest identity-part projection and multiplier criterion (3a). The published bounded spectral chapter supplies supports of bounded normal operators; the projection-lattice proof or the explicit finite-join net below supplies arbitrary joins. Point-space realizations, null-set quantifiers and periodic-flow continuity are separate topics. The measure-theoretic facts recalled in the setting are not used in this algebraic argument.

<a id="OA-FLOW.KERNEL.FOUNDATIONS"></a>
## OA-FLOW.KERNEL.FOUNDATIONS — Setting and exact prerequisites

Let $M$ be a nonzero commutative von Neumann algebra with identity $1$. All automorphisms are unital and normal. Initially $G$ is an arbitrary group with identity $e_G$, and

$$
\alpha:G\longrightarrow\operatorname{Aut}(M),\qquad
\alpha_{gh}=\alpha_g\alpha_h
$$

is a group homomorphism. No topology, countability, separable predual, faithful normal state, or measure-space presentation is required for the algebraic results.

We use the elementary realization of $M$ as a strongly closed algebra on a Hilbert space, bounded functional calculus, and the fact that a von Neumann algebra's normal functionals separate its elements. We recall the required projection and support arguments in the next section. These basic operator-algebra foundations are prerequisites, not new proofs of the representation theorem for abstract von Neumann algebras. The point-space statements additionally use countable separating families for standard Borel spaces and elementary measure theory; the periodic-flow example uses Fubini's theorem for finite Lebesgue measure. No modular theory, operator-valued weight, disintegration theorem, or crossed-product theorem is imported.

For the periodic-flow continuity argument, the precise additional measure-theory import is $L^\infty(\mathbb R/\mathbb Z,m)_*=L^1(\mathbb R/\mathbb Z,m)$ under integration, where $m$ is normalized Lebesgue measure. Thus testing against every $L^1$ density tests every normal functional. This foundational identification is not proved in this unit.

Write

$$
M^\alpha=\{x\in M:\alpha_g(x)=x\text{ for every }g\in G\},
\qquad
K=\ker\alpha=\{g\in G:\alpha_g=\operatorname{id}_M\}.
$$

The action is **ergodic** when $M^\alpha=\mathbb C1$ and **faithful** when $K=\{e_G\}$. A nonzero projection $p$ is an **identity part** for an automorphism $\beta$ when $\beta(p)=p$ and the restriction of $\beta$ to $Mp$ is the identity. We call $\beta$ **free** when it has no identity part. The action is **free** when $\alpha_g$ is free for every $g\ne e_G$.

This is a definition on the algebra. A pointwise action and a common conull set of free points are separate objects. Also, $M^\beta$ records globally fixed elements; it does not itself identify the region where every element is fixed.

<a id="OA-FLOW.KERNEL.PROJECTION"></a>
## OA-FLOW.KERNEL.PROJECTION — The largest identity part

**Proposition.** For every $\beta\in\operatorname{Aut}(M)$ there is a unique largest projection $p_\beta$ such that

$$
\beta(x)p_\beta=xp_\beta\qquad(x\in M).
\tag{1}
$$

It is $\beta$-invariant. On $Mp_\beta$ the automorphism is the identity, and on $M(1-p_\beta)$ its restriction is free. More precisely, let $s(a)$ denote the support projection of an element $a\in M$. Then

$$
p_\beta=1-\bigvee_{x\in M}s(\beta(x)-x),
\qquad
\{a\in M:(\beta(x)-x)a=0\ (x\in M)\}=Mp_\beta.
\tag{2}
$$

**Proof.** We first justify all the projection operations in (2). In a concrete representation, $s(a)$ is the projection onto the closure of the range of $|a|$. It belongs to $M$: for $a\ne0$, the positive contractions

$$
\left(\frac{|a|}{1+\|a\|}\right)^{1/n}
$$

converge strongly to that projection by bounded functional calculus, and $M$ is strongly closed. Set $s(0)=0$. Since every element of $M$ is normal, $\ker a=\ker|a|=(1-s(a))H$. Consequently, for any $b\in M$,

$$
ab=0\quad\Longleftrightarrow\quad s(a)b=0.
\tag{3}
$$

For any family of projections $(q_i)_{i\in I}$ in $M$, the finite joins are in $M$. Commutativity gives the concrete formula

$$
\bigvee_{i\in F}q_i=1-\prod_{i\in F}(1-q_i)
$$

for each finite subset $F\subset I$. These projections form an increasing net. Its strong limit is the projection onto the closed linear span of the subspaces $q_iH$: on that closed span the net converges to the identity, and on its orthogonal complement it is zero. The limit belongs to $M$ and is the least upper bound of the family. This construction uses a net over finite subsets, not an enumeration of $I$.

Now put $q=\bigvee_{x\in M}s(\beta(x)-x)$ and $p=1-q$. Equation (3) shows that $(\beta(x)-x)p=0$ for every $x$, so $p$ satisfies (1). If $a$ is annihilated by every $\beta(x)-x$, then its range lies in every kernel of $s(\beta(x)-x)$, hence in $(1-q)H$. Thus $a=pa$. Conversely $a=pa$ and (1) imply $(\beta(x)-x)a=0$. This proves the second formula in (2). Taking $a$ to be a projection proves maximality and uniqueness.

A projection $r$ satisfying (1) with $r$ in place of $p_\beta$ is automatically invariant. Substitution of $x=r$ gives $\beta(r)r=r$, so $r\leq\beta(r)$. Substitution of $x=\beta^{-1}(r)$ gives $r=\beta^{-1}(r)r$, so $r\leq\beta^{-1}(r)$. Applying $\beta$ to the latter inequality gives $\beta(r)\leq r$. Therefore $\beta(r)=r$. For $y=xr\in Mr$ we obtain

$$
\beta(y)=\beta(x)\beta(r)=\beta(x)r=xr=y.
$$

Conversely, invariance of $r$ and the identity restriction on $Mr$ imply (1), by applying $\beta$ to $xr$.

In particular $p_\beta$ and $1-p_\beta$ are invariant, so both restrictions in the statement exist. If the restriction on $M(1-p_\beta)$ had a nonzero identity part $r\leq1-p_\beta$, then, for arbitrary $x\in M$, applying its defining identity to $x(1-p_\beta)$ would give $\beta(x)r=xr$. Maximality gives $r\leq p_\beta$, a contradiction. This proves freeness on the complement. If a complementary summand is zero, the assertion about that summand simply has no nonzero projection to test. $\square$

**Multiplier criterion.** The automorphism $\beta$ is free if and only if

$$
xa=a\beta(x)\quad\text{for all }x\in M
\quad\Longrightarrow\quad a=0.
\tag{3a}
$$

Indeed, commutativity identifies the hypothesis with $a\in Mp_\beta$ in (2). This also explains why “$\beta\ne\operatorname{id}$” is weaker than freeness: it says $p_\beta\ne1$, while freeness says $p_\beta=0$.
