# Compact Fredholm operators and strongly continuous families

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

The extension input is the pinned CC0 programme Hahn–Banach theorem, Theorems 2.1–2.2 and Corollary 2.3(1), including extension from an arbitrary subspace. Its Baire Theorem 3.1, open-mapping Theorem 5.1 and inverse-mapping Corollary 5.2 supply the general Banach inverse assertion used in local index stability. Its notice credits Claude Opus 5.5 and GPT-6.1 Sol under CC0. Read the proved [finite-dimensional compactness facts](hilbert-valued-integration.md#compact-scalar-calculus) for coefficient spheres and bounded complex sequences. Banach completeness is a hypothesis. The compact, Fredholm and family arguments below apply to general complex Banach spaces, including spaces without an approximation property.

<a id="compact-fredholm"></a>
## Compact perturbations of the identity

Let $X$ be a complex Banach space and $C:X\to X$ be bounded and compact, meaning that the closure of $C$ of the unit ball is compact in norm. Then $A=I+C$ has finite-dimensional kernel, closed range, finite-dimensional cokernel and Fredholm index zero:
\[
 \dim\ker A=\dim(X/\operatorname{Ran}A).
 \tag{1}
\]
It is invertible if and only if its kernel is zero. For a closed complement $X_0$ of its kernel, $A:X_0\to\operatorname{Ran}A$ is an isomorphism with bounded inverse. Thus for every $y$ in the range there is a unique $x\in X_0$ with $Ax=y$, and $\|x\|\leq M\|y\|$. This includes nonzero kernels.

<a id="fredholm-finite-tools"></a>
## Elementary finite-dimensional tools

Here are the compactness facts used below, including the case of parameters that are not first countable. Compactness means that every open cover has a finite subcover. A net $(x_d)$ in a compact space has a cluster point: the closed sets $\overline{\{x_e:e\geq d\}}$ have the finite-intersection property, and their intersection cannot be empty, since their open complements would then have a finite subcover. Let $x$ belong to that intersection. For every index $d$ and neighbourhood $V$ of $x$, some $e\geq d$ has $x_e\in V$. Use triples $(d,V,e)$ with these properties, ordered by increasing $d,e$ and shrinking $V$. They form a directed set: after two triples, choose $e$ beyond both old indices and the new lower bound with $x_e$ in the intersection of their neighbourhoods. The map to $e$ is increasing and cofinal. It therefore gives a subnet converging to $x$.

In a metric space this also gives a convergent subsequence of every sequence in a compact set: at its cluster point choose increasing indices within successive $1/k$ balls. Compact sets have finite $\varepsilon$-nets by the ball cover. A set in which every sequence has a convergent subsequence has finite $\varepsilon$-nets: otherwise choose successively points at distance at least $\varepsilon$ from all preceding points, contradicting convergence of any subsequence. Conversely, total boundedness gives a Cauchy subsequence by repeatedly retaining an infinite part in one of finitely many balls of radius $2^{-k}$; in a complete space it converges. To deduce compactness from this subsequence property, suppose an open cover has no finite subcover. If it has a positive number $\delta$ such that every $\delta$-ball lies in one cover member, a finite $\delta$-net gives a finite subcover, a contradiction. Otherwise choose $x_k$ whose $1/k$-ball lies in no member. A convergent subsequence has limit $x$ in some open cover member; a small ball around $x$ lies in it, and eventually contains those $1/k$-balls, a contradiction. Thus a complete totally bounded metric space is compact. Closure preserves total boundedness by slightly enlarging each radius; a closed subset of a complete space is complete. These facts justify every later subsequence, subnet and compact-closure assertion.

A finite-dimensional subspace with basis $e_1,\ldots,e_d$ is closed and its coordinate functionals are continuous. Indeed $a\mapsto\|\sum a_je_j\|$ is continuous in the Euclidean coefficient norm by the triangle inequality; on its compact unit sphere it has a positive minimum by linear independence. The resulting upper and lower bounds prove completeness, closedness, and bounded coordinates. Extend these coordinates to $X$ by Hahn–Banach. Then $Px=\sum_j\ell_j(x)e_j$ is a bounded projection onto that subspace, and $X=PX\oplus\ker P$ is a closed direct sum. A finite-codimensional closed subspace has a closed finite-dimensional complement by choosing representatives of a basis of the quotient; the quotient coordinate maps are continuous by the same finite-dimensional bounds.

The quotient $X/Y$ of a Banach space by a closed subspace is Banach. To prove this, choose a subsequence of a quotient Cauchy sequence whose consecutive quotient differences have norms less than $2^{-j}$. Represent those differences by vectors of norm less than $2^{1-j}$, using the definition of the quotient norm. Starting with one lift, their convergent series in $X$ lifts the limit of the quotient subsequence. The original Cauchy sequence has that same limit. Closedness of $Y$ makes the quotient norm a genuine norm.

The Riesz lemma needed here follows directly from distance. For a proper closed subspace $Y$ choose $x\notin Y$ and put $d=\operatorname{dist}(x,Y)>0$. For $0<r<1$ choose $y\in Y$ with $\|x-y\|<d/r$. The unit vector $v=(x-y)/\|x-y\|$ has distance greater than $r$ from $Y$. Iterating with finite-dimensional spans gives a sequence of unit vectors mutually more than $1/2$ apart in any infinite-dimensional normed space. Its unit ball therefore cannot be relatively compact.

<a id="fredholm-kernel-range"></a>
## Kernel and closed range

On $\ker A$, $C=-I$. The unit ball of this closed kernel is therefore relatively compact, and the preceding Riesz argument makes the kernel finite-dimensional. Choose its bounded projection $P$ and $X_0=\ker P$.

There is $c>0$ with $\|Ax\|\geq c\|x\|$ on $X_0$. Otherwise choose unit $x_j\in X_0$ with $Ax_j\to0$. Compactness gives a subsequence with $Cx_j\to v$, and $x_j=Ax_j-Cx_j\to-v$. Its limit is a unit vector in $X_0\cap\ker A$, a contradiction. If $Ax_j\to y$ for arbitrary $x_j\in X$, replace each by $(I-P)x_j$ without changing its image. The lower bound makes these new vectors Cauchy, so their limit maps to $y$. Hence the range is closed. The same bound gives its inverse on $X_0$ and all the stated range-solver conclusions.

<a id="fredholm-dual-cokernel"></a>
## Compactness of the adjoint and finite cokernel

The continuous dual $X^*$ is Banach: a norm-Cauchy sequence of functionals has a pointwise limit, which is linear and bounded; the uniform Cauchy bound on the unit ball passes to the limit and proves norm convergence.

The adjoint $C^*$ is compact. Let $K$ be the compact closure of the image of the unit ball under $C$. A sequence of functionals in the dual unit ball is uniformly bounded on $K$ and has common Lipschitz constant one there. Choose finite $1/m$-nets in $K$ for each $m$. Successive subsequences and a diagonal selection make all values at the resulting countable net points convergent, because they are bounded complex numbers. On a fixed sufficiently fine net, the Lipschitz bound shows that convergence of those finitely many values makes the sequence uniformly Cauchy on $K$. Therefore
\[
 \|C^*(\ell_j-\ell_k)\|
 =\sup_{\|x\|\leq1}|(\ell_j-\ell_k)(Cx)|\to0.
\]
The dual is complete, so every sequence has a norm-convergent subsequence after applying $C^*$. In a metric space this is relative compactness; equivalently finite nets give total boundedness and completeness gives compact closure. Thus $I+C^*$ has finite-dimensional kernel by the preceding kernel proof.

The annihilator of $\operatorname{Ran}A$ is exactly $\ker A^*$ by the definition of the adjoint. Since the range is closed, the dual of $X/\operatorname{Ran}A$ identifies with that annihilator: compose a quotient functional with the quotient map for one direction, and use vanishing on the range for the other; the quotient norm makes the latter bounded. If a normed space had dimension larger than its finite-dimensional dual, choose that many independent vectors, take their bounded coordinate functionals on their finite-dimensional span, and extend by Hahn–Banach. The resulting dual functionals are independent, a contradiction. Hence the quotient here is finite-dimensional, with dimension exactly that of its dual. This proves that $A$ is Fredholm, without claiming that compact operators are norm limits of finite-rank operators on an arbitrary Banach space.

<a id="fredholm-index"></a>
## Why the index is zero

We prove the needed local index stability rather than assuming it. Let $B:X\to X$ be Fredholm. Split its domain as $N\oplus X_0$, where $N=\ker B$, and its target as $R\oplus Z$, where $R=\operatorname{Ran}B$. The first and last spaces are finite-dimensional, and $B_0:X_0\to R$ is an isomorphism. Its inverse is bounded: in this application it was proved above; in general this is the Banach inverse theorem proved in the cited programme lesson.

The required spaces of bounded operators are complete: if $T_j:X\to Y$ is norm Cauchy and $Y$ is Banach, define $Tx=\lim_jT_jx$; the uniform Cauchy bounds give linearity, boundedness and operator-norm convergence. Thus an operator $I+D$ with $\|D\|<1$ has inverse $\sum_{j\geq0}(-D)^j$: this series is norm convergent, and multiplication of each finite partial sum leaves an error $(-D)^{n+1}$ tending to zero.

For any operator $T$ sufficiently close to $B$ in norm, its $X_0\to R$ block $T_{00}$ remains invertible by the geometric series for $I+B_0^{-1}(T_{00}-B_0)$. Bounded invertible row and column operations reduce its two-by-two block matrix to the direct sum of $T_{00}$ and the finite-dimensional map
\[
 S:N\to Z,\qquad
 S=T_{ZN}-T_{Z0}T_{00}^{-1}T_{RN}.
\]
Explicitly first replace the $X_0$ variable by itself plus $T_{00}^{-1}T_{RN}$ times the $N$ variable, and then subtract $T_{Z0}T_{00}^{-1}$ times the $R$ output from the $Z$ output. These transformations and their inverses are bounded. They preserve kernel and quotient dimensions and give a closed range. Thus
\[
 \operatorname{ind}T=\dim\ker S-\dim(Z/\operatorname{Ran}S)
 =\dim N-\dim Z=\operatorname{ind}B.
\]
For $B_t=I+tC$, every $t\in[0,1]$ is Fredholm by the compact arguments above. The path is norm-continuous, so its index is locally constant. A locally constant function on an interval is constant: for a fixed left endpoint, take the supremum of the points up to which it has that endpoint value throughout; local constancy at the supremum first gives the same value there and then extends it if it were short of the right endpoint. At $t=0$ the index is zero, so it is zero throughout the interval. This proves (1). If $\ker A=0$, (1) gives surjectivity and the previously proved lower bound gives a bounded inverse. The converse is immediate.

<a id="collectively-compact-families"></a>
## Strong families and the actual local lower bound

Let $z$ range over a topological space, fix $z_0$, and suppose $z\mapsto C_zx$ is continuous for each $x\in X$. Assume that in one neighbourhood $U$ of $z_0$ the set
\[
 \{C_zx:z\in U,\ \|x\|\leq1\}
 \tag{2}
\]
has compact closure. This is collective compactness. It implies a uniform bound on $\|C_z\|$ in $U$. Put $A_z=I+C_z$. Then near $z_0$:

- $\dim\ker A_z\leq\dim\ker A_{z_0}$;
- on any fixed closed complement $X_0$ of $\ker A_{z_0}$ there is one $c>0$ with $\|A_zx\|\geq c\|x\|$ for every $x\in X_0$;
- if $A_{z_0}$ is invertible, all $A_z$ are invertible in a neighbourhood and $\|A_z^{-1}\|\leq c^{-1}$ there.

For the first assertion choose a projection $P$ onto $N=\ker A_{z_0}$. If kernels of larger dimension occurred arbitrarily near $z_0$, the restriction of $P$ to each such kernel would have a nonzero kernel. Select a unit $u_z\in\ker A_z\cap\ker P$. Their identity $u_z=-C_zu_z$ and (2) give a norm-convergent subnet with limit $u$, $\|u\|=1$, $Pu=0$. Strong continuity and the uniform norm bound give
\[
 \|C_zu_z-C_{z_0}u\|
 \leq\|C_z\|\|u_z-u\|+\|(C_z-C_{z_0})u\|\to0.
\]

The limit therefore satisfies $A_{z_0}u=0$, contradicting $N\cap\ker P=0$. Here a net is indexed by shrinking neighbourhoods if the parameter space is not first countable; compactness supplies its convergent subnet. For metric parameters ordinary sequences suffice.

For the lower bound, if none existed choose parameters tending to $z_0$ and unit $u_z\in X_0$ with $A_zu_z\to0$, indexed also by a positive error tending to zero. The identity $u_z=-C_zu_z+o(1)$ gives a norm-convergent subnet. Passing to the limit as above yields a unit vector in $X_0\cap\ker A_{z_0}$, again a contradiction. At an invertible parameter $X_0=X$, the bound gives zero kernel nearby. The zero-index theorem makes every $A_z$ there surjective, and its inverse norm is at most $c^{-1}$.

It follows that the noninvertible parameter set is closed wherever these local hypotheses hold. The inverses are strongly continuous on its complement: for fixed $y$,
\[
 A_z^{-1}y-A_{z_0}^{-1}y
 =A_z^{-1}(C_{z_0}-C_z)A_{z_0}^{-1}y\to0
\]
by the local inverse bound and strong continuity. These are the exact $A_z=I+C_z$ family hypotheses consumed in AN06-U014. The fixed-operator range solver applies to AN06-U018 even at a nonzero kernel. This statement does not substitute a Hilbert orthogonal-complement proof for the actual general Banach-space argument.
