# Closed conormal unions at singular points

A closed union of stratum conormals is involutive even when the chosen stratification fails the μ-condition. The proof works at each singular covector: select one smooth conormal through it, then use that conormal's entire tangent space inside both normal cones of the union. An explicit polynomial example will distinguish this involutivity from the stronger control of cancelling conormals required by μ.

*Written by GPT-6.1 Sol (OpenAI), Ultra, 1 October 2026. Self-checked by the writing AI. New original text is public domain (CC0).*

This lesson studies closed unions of conormal bundles at singular points, using the real normal-cone conventions fixed earlier. See Involutive subsets of subanalytic isotropic sets for their earlier isotropic applications, and Whitney secants and the microlocal stratification condition for the ordinary polynomial stratification and its μ-failure. The argument here is geometric and requires no coefficient ring, finiteness of sheaf stalks or derived-category assumption.

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

Only convergent quotients enter. These definitions transform by the tangent map under a $C^1$ change of coordinates. The pair cone can have many more directions than the point cone; it is symmetric, whereas the point cone need not be. A locally closed $S$ is involutive at $p$ when

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

Let $X$ be real analytic, Hausdorff and countable at infinity, and let $(S_\beta)$ be a locally finite subanalytic stratification. Retain the ordinary stratification assumptions; impose no μ- or Whitney hypothesis. Set

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

It has $d+(n-d)=n$ free coordinates and $\omega|_{TL}=0$: each term $d\xi_i\wedge dx_i$ has one zero factor. Hence $(T_pL)^\omega=T_pL$. The coordinate calculation is invariant under cotangent changes of coordinates. Since $L\subset\Lambda$, (4) and (5) prove (3) at $p$. Closedness makes $\Lambda$ locally closed as required by the definition, and $p$ was arbitrary. $\square$

The geometric prerequisites also make each conormal conic and subanalytic. Local finiteness in the **base** means that only finitely many strata, hence finitely many conormals, occur over a sufficiently small base neighborhood. Thus their union is locally subanalytic, without a global finite-stratum assumption. The canonical form vanishes on each conormal; finite local union preserves this singular-set vanishing. Every point lies on an $n$-dimensional piece, and finite local union gives local dimension exactly $n$. These explain the isotropic geometry of (6), but the singular involutivity proof is the pointwise argument (4)–(7).

Closedness is retained exactly as in the source. The covering lemma also applies to any such union that is locally closed. Neither statement permits one to replace a union by its closure and silently assume a smooth coisotropic piece passes through each newly added point.

## Closed conormals can still fail μ

In coordinates $(t,x,y)$ on $\mathbb R^3$, take the previously checked ordinary stratification

\[
 \begin{gathered}
 g=y^2-t^2x^2-x^3,\qquad Z=\{g=0\},\\
 S_2=\{x=y=0\},\qquad S_1=Z\setminus S_2,
 \qquad S_0=\mathbb R^3\setminus Z.
 \end{gathered}
 \qquad\text{(8)}
\]

The open complement, analytic hypersurface and closed axis are semialgebraic strata with the ordinary frontier rule. On $S_1$, $x\ne0$, and $s=y/x$ gives

\[
 x=s^2-t^2,\qquad y=s(s^2-t^2),\qquad s\ne\pm t.
 \qquad\text{(9)}
\]

Dividing the nonzero normal $dg$ by $x$ gives a convenient generator of the conormal line,

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

Every finite limiting covector therefore has $dt$ component zero, so lies in $T^*_{S_2}\mathbb R^3$ at its limiting base. The axis conormal is closed; the open-stratum zero covectors remain zero under limits; and over interior points of $S_1$ the conormal bundle is closed relative to that smooth stratum. Passing to one of the three stratum types in any converging sequence proves that their total union is closed. The theorem applies and proves its singular involutivity.

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

Thus the full limiting sum of the two conormals contains $dt$ at the origin, which is not an axis conormal. This violates μ. The failing Whitney (b) secant is the $x$-axis, whereas the upper tangent planes tend to the $(t,y)$-plane. Ordinary bounded conormal limits, which (11) controls, and the sums of two unbounded cancelling conormals, which (13) detects, are different operations. The source exercise requires the former closed union, without assuming the latter μ-control.

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

## References and remaining boundaries

The mathematical source target is Exercise VIII.11. The exact real singular definition and sign are Definition 6.5.1 represented by the current `SH02-INV-SECANTS` and `SH02-INV-DEFINITION` contracts. We reuse the definition and its coordinate comparison, and prove the conormal-union application directly. We do not import the general microsupport involutivity theorem or its propagation proof to obtain this exercise.

The polynomial stratification and failing μ-witness were taught in the earlier Whitney lesson. Here the estimate (11) checks **all** individual finite conormal limits, and proves the closedness needed for this separate exercise. The proof illustrates why that geometric hypothesis permits a stratification failing μ; it does not assert that every ordinary stratification has closed total conormal.

The six solutions are complete relative to the exact prerequisites. The prerequisites themselves are not proved here.
