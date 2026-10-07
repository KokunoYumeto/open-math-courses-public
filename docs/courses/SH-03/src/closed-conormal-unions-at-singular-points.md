# Closed conormal unions at singular points

A closed union of stratum conormals is involutive even when the chosen stratification fails the μ-condition. The proof works at each singular covector: select one smooth conormal through it, then use that conormal's entire tangent space inside both normal cones of the union. An explicit polynomial example will distinguish this involutivity from the stronger control of cancelling conormals required by μ.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources retain their named credit and their own terms.*

The singular involutivity criterion compares two normal cones, with the Hamiltonian sign fixed by the canonical symplectic form. We prove the conormal-union assertion directly from that criterion. Involutive subsets of subanalytic isotropic sets explains the relation with isotropy; Whitney secants and the microlocal stratification condition defines the two Whitney conditions and μ. The arguments below are geometric and require no coefficient ring or sheaf-theoretic hypothesis.

## Keep the two normal cones distinct

Let $P=T^*X$, with $X$ a smooth $n$-manifold. In local coordinates use

\[
 \alpha=\sum_i\xi_i\,dx_i,\qquad
 \omega=d\alpha=\sum_i d\xi_i\wedge dx_i,
 \qquad
 H\Bigl(\sum_i a_i dx_i+b_i d\xi_i\Bigr)
   =\sum_i b_i\partial_{x_i}-a_i\partial_{\xi_i}.
 \qquad\text{(1)}
\]

Thus $\iota_{H\theta}\omega=-\theta$. For $p\in S\subset P$, the point and pair cones are

\[
 \begin{aligned}
 C_p(S)&=\left\{\lim_j\frac{s_j-p}{h_j}:
                   s_j\in S,\ s_j\to p,\ h_j\downarrow0\right\},\\
 C_p(S,S)&=\left\{\lim_j\frac{s_j-t_j}{h_j}:
             s_j,t_j\in S,\ s_j,t_j\to p,\ h_j\downarrow0\right\}.
 \end{aligned}
 \qquad\text{(2)}
\]

Only convergent quotients enter. Here is the coordinate comparison for two moving endpoints. In a convex coordinate neighborhood, a $C^1$ coordinate change $F$ satisfies $F(s)-F(t)=dF_p(s-t)+r(s,t)$, with $|r(s,t)|\leq\sup_{z\in[s,t]}\|dF_z-dF_p\|\,|s-t|$. If $(s_j-t_j)/h_j$ converges, its norm is bounded, while the supremum tends to zero. Division by $h_j$ therefore sends the remainder to zero. Applying the same argument to $F^{-1}$ proves that the pair cone transforms exactly by $dF_p$. Taking $t_j=p$ proves the point-cone assertion. Separate Taylor remainders at $p$ would not suffice when $s_j-t_j$ is much smaller than either endpoint's distance to $p$.

The pair cone is symmetric, by exchanging its two endpoints; the point cone need not be. Since $p\in S$, choosing the second endpoint to be $p$ gives $C_p(S)\subset C_p(S,S)$. These are the two-endpoint comparison and cone properties. A locally closed $S$ is involutive at $p$ when

\[
 C_p(S,S)\subset\ker\theta
 \quad\Longrightarrow\quad
 -H\theta\in C_p(S)
 \qquad(\theta\in T_p^*P).
 \qquad\text{(3)}
\]

This condition must hold at every point of the set, including its singular points. It is not a statement only about the largest smooth pieces.

## A smooth coisotropic piece supplies the required direction

**Tangent inclusion.** If a smooth submanifold $L\subset S$ passes through $p$, then

\[
 T_pL\subset C_p(S),\qquad T_pL\subset C_p(S,S).
 \qquad\text{(4)}
\]

**Proof.** Given $v\in T_pL$, take a smooth curve $c$ in $L$ with $c(0)=p$ and $c'(0)=v$. For $h_j>0$ tending to zero,
$(c(h_j)-p)/h_j\to v$. This is a point-cone witness. With $s_j=c(h_j)$ and $t_j=p$, it is also a pair-cone witness. All these points belong to $S$. Negative tangent vectors are obtained by reversing the curve. $\square$

**Covering lemma.** Suppose $S\subset P$ is locally closed and every $p\in S$ lies on a smooth coisotropic submanifold $L_p\subset S$. Then $S$ is involutive.

Here coisotropic means $(T_pL_p)^\omega\subset T_pL_p$. The pieces can overlap, need not form a stratification of $S$, and need not vary continuously with $p$. No subanalyticity or local finiteness is needed for this pointwise lemma.

**Proof.** If $\theta$ annihilates $C_p(S,S)$, (4) says it annihilates $T_pL_p$. From (1),

\[
 -H\theta\in(T_pL_p)^\omega
                 \subset T_pL_p\subset C_p(S).
 \qquad\text{(5)}
\]

This is precisely (3), at the arbitrary point $p$. It uses a whole smooth piece **through the point**. A smooth piece merely approaching a missing limit point does not provide (4) there. $\square$

Lagrangian pieces satisfy equality in the middle of (5). Their union need not be a smooth manifold; smoothness of the union was never used.

## Apply the lemma to the total conormal

Let $X$ be real analytic, Hausdorff and countable at infinity, and let $(S_\beta)$ be a locally finite subanalytic stratification. Its strata are locally closed smooth submanifolds of fixed dimension; the ordinary frontier rule says that a stratum meeting another's closure lies wholly in that closure. Strata may be disconnected. We do not add a μ- or Whitney hypothesis. Set

\[
 \Lambda=\bigcup_\beta T^*_{S_\beta}X.
 \qquad\text{(6)}
\]

Each conormal here is over the stratum itself. Formula (6) does not insert its closure or add missing boundary covectors.

**Closed total-conormal theorem.** If $\Lambda$ is closed in $T^*X$, it is involutive in the full sense of (3).

**Proof.** Take $p\in\Lambda$. Its base point belongs to a unique stratum $S_\beta$, and $p$ belongs to its smooth conormal $L=T^*_{S_\beta}X$. This conormal is Lagrangian. In coordinates straightening a $d$-dimensional stratum to $x_{d+1}=\cdots=x_n=0$, its equations are

\[
 x_{d+1}=\cdots=x_n=0,
 \qquad\xi_1=\cdots=\xi_d=0.
 \qquad\text{(7)}
\]

It has $d+(n-d)=n$ free coordinates and $\omega|_{TL}=0$: each term $d\xi_i\wedge dx_i$ has one zero factor. Nondegeneracy gives $\dim(T_pL)^\omega=2n-\dim T_pL=n$; isotropy then gives $(T_pL)^\omega=T_pL$. Under a base coordinate change $x'=F(x)$ the cotangent coordinates satisfy $\xi'=(dF_x)^{-\mathsf t}\xi$, hence $\sum_i\xi_i'\,dx_i'=\sum_i\xi_i\,dx_i$. Both $\alpha$ and $\omega=d\alpha$ are therefore preserved, so this calculation applies to every smooth conormal, including zero covectors.

Since $L\subset\Lambda$ passes through the specified $p$, (4) and (5) prove (3) at that point. Closedness makes $\Lambda$ locally closed, as required by the definition. The point $p$ was arbitrary, including points where several conormal closures meet. $\square$

For completeness, subanalyticity of a conormal must also hold near the frontier of its base stratum. The bounded tangent-witness proof, (B1)–(B2) gives it as follows. The tangent bundle of a smooth subanalytic stratum is the restriction of its pair normal cone to that stratum, so it is subanalytic by the normal-cone calculus. A covector fails to annihilate that tangent space precisely when there is a tangent vector $v$ of norm at most one with nonzero pairing. The set of these witnesses is subanalytic. Forgetting $v$ is proper on its closure over every compact cotangent-coordinate set, since the auxiliary vector lies in a closed unit ball. The proper-closure projection theorem makes the nonannihilating locus subanalytic; its complement over the stratum is exactly the conormal. This argument applies to smooth subanalytic strata, without requiring a subanalytic extension of a straightening chart across their frontier.

Local finiteness in the base gives only finitely many such conormals over a sufficiently small base neighborhood. Their union is therefore subanalytic there and has dimension at most $n$. At every one of its points it contains an $n$-dimensional smooth conormal through that point, so its local dimension is exactly $n$. Each conormal is invariant under every real fibre scale and has zero canonical form. The singular one-form test, (C1)–(C4) extends this vanishing to its point-cone directions at frontier points. A witness for a point cone of the finite union has a subsequence lying in a single member. The canonical form consequently vanishes on the union in the same singular sense. These observations establish its subanalytic isotropic geometry; its involutivity already follows from the smooth piece through each actual point.

The covering lemma also applies when this actual union is only locally closed. Replacing it by its closure is a different operation: a newly added covector need not lie on any of the smooth conormals already present. The proof requires a coisotropic piece through the point being tested, not merely pieces converging to it.

## Closedness is exactly Whitney (a) for this stratification

For an incident pair of strata $M,N$, Whitney (a) says that $x_j\in M$, $x_j\to p\in N$, and $T_{x_j}M\to T$ imply $T_pN\subset T$. Tangent-plane convergence can be described by convergence of orthogonal projectors in a coordinate chart. For a locally finite smooth stratification, the total conormal (6) is closed if and only if every incident pair satisfies this condition.

Suppose first that $\Lambda$ is closed. For any $\xi\in T^\perp$, let $P_j$ be the orthogonal projector onto $T_{x_j}M$ and set $\xi_j=(I-P_j)\xi$. Then $\xi_j\in(T_{x_j}M)^\perp$ and $\xi_j\to\xi$. Closedness puts $(p,\xi)$ in $\Lambda$, and the unique stratum through $p$ is $N$. Thus $\xi$ annihilates $T_pN$. This holds for every $\xi\in T^\perp$, so $T_pN\subset(T^\perp)^\perp=T$, proving (a).

Conversely, assume (a) for every incident pair and take a convergent sequence $(x_j,\xi_j)\in\Lambda$ with limit $(p,\xi)$. Local finiteness near $p$ lets us pass to a subsequence whose bases lie in one stratum $M$. Compactness of the Grassmannian lets us further arrange $T_{x_j}M\to T$. If $p$ lies in $M$, smoothness gives $T=T_pM$. Otherwise the frontier rule makes the stratum $N$ through $p$ incident to $M$, and (a) gives $T_pN\subset T$. In either case the limit covector annihilates $T$, because each $\xi_j$ annihilates $T_{x_j}M$. It therefore annihilates the stratum through $p$, and $(p,\xi)\in\Lambda$. This proves closedness. Only finite-dimensional linear algebra, smooth tangent continuity and local finiteness were used in this equivalence.

Thus the closedness hypothesis already encodes Whitney (a); it does not encode Whitney (b), whose test also includes secant lines between two moving base points. The example below separates those two conditions and μ.

## Closed conormals can still fail μ

In coordinates $(t,x,y)$ on $\mathbb R^3$, consider

\[
 \begin{gathered}
 g=y^2-t^2x^2-x^3,\qquad Z=\{g=0\},\\
 S_2=\{x=y=0\},\qquad S_1=Z\setminus S_2,
 \qquad S_0=\mathbb R^3\setminus Z.
 \end{gathered}
 \qquad\text{(8)}
\]

All three pieces are semialgebraic. The complement $S_0$ is open and $S_2$ is the closed $t$-axis. On $S_1$, $x\ne0$, since $x=0$ and $g=0$ force $y=0$. The gradient is $dg=(-2tx^2,-2t^2x-3x^2,2y)$. If $y\ne0$ it is nonzero; if $y=0$, the equation gives $x=-t^2\ne0$, so its $dx$ component is $-t^4\ne0$. Thus $S_1$ is a smooth analytic hypersurface. Dividing its defining equation by $x^2$ and putting $s=y/x$ gives

\[
 x=s^2-t^2,\qquad y=s(s^2-t^2),\qquad s\ne\pm t.
 \qquad\text{(9)}
\]

The parametrization (9) reaches every point of $S_1$. For each fixed $t_0$, taking $s\to t_0$ through $s\ne\pm t_0$ approaches $(t_0,0,0)$; for $t_0=0$, take nonzero $s\to0$. Hence $\overline{S_1}=Z$. A nonzero polynomial cannot vanish on an open ball, so $Z$ has empty interior and $\overline{S_0}=\mathbb R^3$. The three frontiers are therefore $S_1\cup S_2$, $S_2$, and the empty set, respectively. They are unions of whole lower-dimensional strata, proving the ordinary frontier rule and the required finite stratification.

Substituting (9) into $dg/x$ gives the nonzero generator

\[
 n(t,s)=\bigl(-2t(s^2-t^2),\ t^2-3s^2,\ 2s\bigr).
 \qquad\text{(10)}
\]

**All finite conormal limits remain in the total union.** Consider base points of $S_1$ approaching the axis and covectors $\lambda_j n(t_j,s_j)$ approaching a finite limit. The relation $s_j^2=t_j^2+x_j$ shows that $s_j$ is bounded and every subsequential limit satisfies $s^2=t^2$.

If the limiting axis point has $t_0\ne0$, then $|s_j|\to|t_0|>0$. The $dy$ component $2\lambda_js_j$ being bounded forces $\lambda_j$ bounded. The $dt$ component $-2\lambda_jt_jx_j$ tends to zero.

At the origin use the two elementary estimates

\[
 \frac{|n_t|}{\sqrt{n_x^2+n_y^2}}
 \leq
 \begin{cases}
  \frac{14}{3}|t|,&s^2\leq t^2/6,\\
  7\sqrt6\,s^2,&s^2>t^2/6.
 \end{cases}
 \qquad\text{(11)}
\]

For the first case, $|n_x|=|t^2-3s^2|\geq t^2/2$ and
$|n_t|\leq2|t|(t^2+s^2)\leq(7/3)|t|t^2$. In the second, $|t|<\sqrt6|s|$, $t^2+s^2<7s^2$, and $|n_y|=2|s|$. These prove (11). Its right side tends to zero at the origin. Multiplying by the bounded norm of $(\lambda_jn_x,\lambda_jn_y)$ shows that $\lambda_jn_t\to0$, even when $\lambda_j$ is unbounded.

Every finite limiting covector from $S_1$ at an axis point has $dt$ component zero, so belongs to $T^*_{S_2}\mathbb R^3$. The axis conormal is closed because it is given by $x=y=\xi_t=0$. Zero covectors from the open stratum have zero limits, and a zero covector over any limit base belongs to that base's stratum conormal. If an $S_1$ sequence has limit base in $S_1$, then in a neighborhood of that base the continuous tangent planes of the hypersurface make its conormal bundle closed; its limit covector is conormal there. There are only three stratum types, so any convergent sequence in the total union has a subsequence of one of these types. Each case puts its limit in the union. This proves closedness and hence, by the preceding equivalence, Whitney (a) for the whole stratification. The closed total-conormal theorem also proves its singular involutivity.

Nevertheless the pair $S_1,S_2$ fails μ. For $u_j>0$ tending to zero, let

\[
 a_j=(u_j,-u_j^2,0),\qquad b_j=(u_j,0,0),
 \qquad
 \xi_j=dt+\frac{1}{2u_j}dx,\qquad
 \eta_j=-\frac{1}{2u_j}dx.
 \qquad\text{(12)}
\]

The first covector is conormal to $S_1$ at $a_j$, since $dg$ there spans $(2u_j,1,0)$. The second annihilates the axis tangent at $b_j$. They satisfy

\[
 \xi_j+\eta_j=dt,
 \qquad
 |a_j-b_j|\,|\xi_j|
 =\frac{u_j}{2}\sqrt{1+4u_j^2}\longrightarrow0.
 \qquad\text{(13)}
\]

Thus the full limiting sum of the two conormals contains $dt$ at the origin, outside the axis conormal, and μ fails. The Whitney (b) failure can be checked independently: at $a_j$ the normal line spans $(2u_j,1,0)$, so the tangent plane is spanned by $(1,-2u_j,0)$ and $(0,0,1)$. Its limit is the $(t,y)$-plane. But $a_j-b_j=(0,-u_j^2,0)$, so the secant line is always the $x$-axis, which is absent from that plane. This contradicts the secant requirement in Whitney (b).

The estimate (11) controls every finite limit of an individual conormal, even with an unbounded scalar multiplier. The witness (12)–(13) instead adds two conormals whose divergent components cancel. Closedness and Whitney (a) permit the former limits; μ excludes the latter tangential output. The involutivity of the closed union is compatible with both its Whitney (b) failure and its μ-failure.

## Exercises with complete solutions

### Check the Hamiltonian sign on a conormal

*Difficulty: Introductory.*

For the coordinate conormal (7), describe its tangent space and the covectors annihilating it. Compute $-H\theta$ for such a covector and verify that it lies in the tangent space.

**Solution.** Tangent vectors have free $\delta x_i$ for $i\leq d$ and free $\delta\xi_i$ for $i>d$; the other components are zero. An annihilating covector has $a_i=0$ for $i\leq d$ and $b_i=0$ for $i>d$. Formula (1) gives

\[
 -H\theta=-\sum_{i\leq d}b_i\partial_{x_i}
             +\sum_{i>d}a_i\partial_{\xi_i}.
\]

These are exactly allowed tangent directions. The plus sign in the second term follows from $\iota_{H\theta}\omega=-\theta$. Since the tangent space is linear, both Hamiltonian signs lie there, as the involutivity definition requires when also applied to $-\theta$.

### The two cones of crossing conormals have different dimensions

*Difficulty: Intermediate.*

Stratify $\mathbb R$ by its negative halfline, origin and positive halfline. Find the total conormal $\Lambda\subset\mathbb R^2_{x,\xi}$. Compute both cones (2) at $(0,0)$ and verify (3).

**Solution.** The open strata give zero covectors, and the point stratum gives the full vertical fibre. Hence

\[
 \Lambda=\{x\xi=0\},\qquad
 C_0(\Lambda)=\mathbb R e_x\cup\mathbb R e_\xi.
\]

Every point-cone quotient remains on one of those two axes; every axis vector is realized by a linear sequence. For arbitrary $(a,b)$, take $s_j=(h_ja,0)$ on the horizontal branch and $t_j=(0,-h_jb)$ on the vertical branch. Their quotient is $(a,b)$, so
$C_0(\Lambda,\Lambda)=\mathbb R^2$. A covector annihilating this whole pair cone is zero, and its Hamiltonian vector is the zero point-cone vector. This proves involutivity at the crossing. At other points the set is locally a single Lagrangian line, where (5) applies. The pair cone's dimension two does not contradict the union's dimension one.

### Isotropic containment alone does not supply involutivity

*Difficulty: Intermediate.*

In the symplectic plane take the closed singleton $S=\{(0,0)\}$. Compute the two cones and test (3) with $\theta=dx$. Explain why merely lying in the zero section is insufficient.

**Solution.** Both cones are $\{0\}$. The covector $dx$ annihilates the pair cone, but $-H(dx)=\partial_\xi$ is nonzero and therefore absent from the point cone. The set is not involutive. It is conic, subanalytic and canonically isotropic, and lies in the Lagrangian zero section. The covering lemma would require a whole smooth coisotropic submanifold **contained in** $S$ through its point. A containing zero section has the opposite inclusion and supplies no curve in $S$. Thus neither isotropic containment nor subanalyticity proves the exercise.

### Finite normal limits can survive arbitrary rescaling

*Difficulty: Advanced.*

For (10), consider $(t_j,s_j)\to(0,0)$ through $s_j\ne\pm t_j$ and arbitrary scalars $\lambda_j$. Assuming the $dx$ and $dy$ components of $\lambda_jn$ are bounded, prove the $dt$ component tends to zero. Test this on $s_j=0$, $t_j=1/j$, $\lambda_j=j^2$, and explain why it does not exclude the cancelling witness (12).

**Solution.** On each term use whichever line of (11) applies. Both bounds tend to zero, so their maximum tends to zero along the full sequence. Multiplication by the uniformly bounded norm of the last two scaled components gives $|\lambda_jn_t|\to0$. On the stated test sequence,

\[
 n=(2/j^3,1/j^2,0),\qquad
 \lambda_jn=(2/j,1,0)\longrightarrow dx.
\]

This limit is an axis conormal. In (12), by contrast, the first $dx$ component is $1/(2u_j)$ and is unbounded. The other conormal cancels it before the finite sum is taken. The bounded-component hypothesis used to deduce a finite **individual** conormal limit is absent for that first factor. The two conclusions are therefore compatible.

### Ordinary union and limiting sum at the same axis point

*Difficulty: Advanced.*

Put $u_j=1/j$ in (12). Verify the conormal equations, the full norm-product condition and the output $dt$. Compare membership of this output in the closed total union with its membership in the limiting sum.

**Solution.** At $a_j$, $dg=(-2u_j^5,-u_j^4,0)$, and multiplication by $-1/(2u_j^5)$ gives $dt+(2u_j)^{-1}dx$. At $b_j$ the tangent is $\mathbb R\partial_t$, so $-(2u_j)^{-1}dx$ is conormal. Their sum is exactly $dt$. The base distance is $u_j^2$, and the first norm is $\sqrt{1+(2u_j)^{-2}}$, giving the vanishing product in (13). Both bases tend to the origin, so this is an actual full limiting-sum witness.

At the origin the base belongs to $S_2$ alone; the union (6) has only covectors with $dt$ component zero there. The nonzero $dt$ is therefore outside that ordinary closed union. It is inside the limiting sum of two of its conormal pieces. Closure of a set does not make it closed under this limiting addition. Singular involutivity of the union remains valid by (5), while μ fails by this witness.

### Vanishing-function brackets are a consequence of the full cone proof

*Difficulty: Intermediate.*

Let $S$ satisfy the covering lemma with Lagrangian pieces. If $\varphi,\psi$ are $C^2$ functions vanishing on $S$, prove $d\psi_p(Hd\varphi_p)=0$ at every $p\in S$. Explain the relation to the singular criterion already proved.

**Solution.** Choose $L_p\subset S$ through $p$. The restrictions of both functions vanish on that smooth piece, so both differentials annihilate $T_pL_p$. Its Lagrangian equality and (1) imply $Hd\varphi_p\in T_pL_p$. Therefore $d\psi_p(Hd\varphi_p)=0$. This is vanishing of the Hamiltonian bracket in the stated convention; the opposite bracket sign gives the same zero.

The calculation holds even if the union is singular at $p$, since the smooth piece passes through that point. The earlier proof established (3) for **every** covector annihilating the pair cone, rather than just differentials of the particular vanishing functions. The bracket consequence does not replace that quantifier or excuse a proof only on regular strata.

## References and further geometry

Pierre Schapira, [*A short review on microlocal sheaf theory*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf), 19 January 2016, §2.1, pp. 5–6, gives the point and pair normal cones, the canonical form, the Hamiltonian isomorphism used in (1), and singular coisotropy in Definition 2.2. The annihilator of the pair cone is a vector subspace, so using −H rather than H gives the same quantified condition (3).

Masaki Kashiwara and Pierre Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), §8.1, Proposition 8.1.4, pp. 142–143, uses limiting tangent planes to prove conormal closedness for a Whitney stratification. The proof above isolates the exact equivalence with Whitney (a) and proves singular involutivity directly through the smooth conormal passing through each tested point.

The two-cone definition and Hamiltonian convention distinguish singular involutivity from a condition checked only on smooth points. The direct argument (4)–(7) uses those definitions and elementary symplectic linear algebra. The bounded conormal construction and singular one-form calculus explain the additional subanalytic isotropic geometry.

The Whitney secant lesson studies the same polynomial surface and its quantitative conormal failure. Here the complete finite-limit estimate proves closedness of its total conormal and hence Whitney (a). Its explicit secant and cancelling-conormal sequences show why Whitney (b) and μ impose further control.

The pointwise covering lemma extends beyond stratifications: any locally closed set covered through each point by contained smooth coisotropic pieces is involutive. The conormal application supplies such pieces canonically, while the crossing example shows why the two cones must remain distinct at their intersections.