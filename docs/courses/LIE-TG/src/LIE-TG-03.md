# One-parameter groups

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI), in Codex at Ultra. Public domain (CC0).*

A vector field specifies a velocity at every point. Its flow is the finite transformation obtained by following those velocities. For analytic fields, repeated differentiation gives a convergent series for the transformation. For a finite-dimensional transformation group, every element sufficiently close to the identity is obtained from these flows.

We use The fundamental differential equations, the analytic inverse-function theorem, and elementary complex analysis. We prove the local analytic flow statement needed here, including parameter dependence, so that the convergence assertions have explicit hypotheses. Basic references are [Kunzinger], [Lie–Engel I], and [Merker]. Composition of maps is written in the ordinary operator order: in $A\circ B$, $B$ acts first. Our bracket is $[X,Y]F=X(YF)-Y(XF)$.

## 1. Analytic flows and their domain

For $X=\sum_i\xi^i(x)\partial_{x_i}$, a flow solves

$$
\frac{d}{dt}\Phi_X^t(x)=\xi(\Phi_X^t(x)),\qquad \Phi_X^0(x)=x.
\tag{1.1}
$$

**Lemma 1.1.** An analytic vector field has a unique analytic local flow. Time, initial point, and any additional analytic parameters can be chosen in product neighbourhoods. On a possibly smaller neighbourhood,

$$
\Phi_X^{s+t}(x)=\Phi_X^t(\Phi_X^s(x)),\qquad
(\Phi_X^t)^{-1}=\Phi_X^{-t}.
\tag{1.2}
$$

**Proof.** First work over $\mathbb C$. Choose concentric coordinate polydiscs whose closures lie in the domain of $\xi$. On the larger one, bound $\|\xi\|$ by $M$ and $\|D\xi\|$ by $L$. Initial points lie in the smaller disc, at distance $\delta>0$ from the larger boundary. Choose $T>0$ with $TM<\delta$ and $TL<1$.

Starting with $y_0(t,x)=x$, iterate

$$
y_{k+1}(t,x)=x+\int_0^t\xi(y_k(s,x))\,ds.
$$

The integral is along a segment in the time disc; its holomorphic integrand also gives a holomorphic primitive. Each iterate stays within distance $TM$ of the initial point. On the space of such bounded holomorphic maps, the iteration is a contraction in the uniform norm, with factor at most $TL$. Its uniformly convergent limit is holomorphic in $(t,x)$ and satisfies the integral equation. Differentiating proves (1.1). The same Lipschitz estimate proves uniqueness, shrinking the common domain if required. Additional parameters can be included in the initial polydisc and in the uniform bounds, proving analytic dependence on them.

A real-analytic field extends holomorphically near a real point. The construction above restricted to real data has real values by uniqueness and complex conjugation, giving the real-analytic statement.

For fixed $s$, both sides of the first equation in (1.2), viewed as functions of $t$, solve the same differential equation with initial value $\Phi_X^s(x)$. Uniqueness proves equality. Setting $s=-t$ gives the inverse. $\square$

This is local existence. The field $x^2\partial_x$ has trajectories that blow up in finite real time, so it need not give transformations for all $t$ on one fixed domain.

## 2. Lie series with a convergence proof

Write $\exp(tX)$ for the map $\Phi_X^t$. Let $F$ be an analytic function, and let $X^kF$ mean repeated application of the differential operator $X$, with $X^0F=F$.

**Theorem 2.1 (Lie series).** On sufficiently small product neighbourhoods,

$$
F(\exp(tX)(x))=\sum_{k=0}^\infty\frac{t^k}{k!}(X^kF)(x).
\tag{2.1}
$$

The convergence is locally uniform in $x$ and $t$.

**Proof.** By Lemma 1.1, $G(t,x)=F(\Phi_X^t(x))$ is holomorphic after complexifying real-analytic data if needed. The chain rule gives

$$
\partial_tG(t,x)=(XF)(\Phi_X^t(x)).
$$

Repeated differentiation gives $\partial_t^kG(0,x)=X^kF(x)$. Choose a smaller compact initial-point polydisc and a time radius $R>0$ such that $G$ is holomorphic on a neighbourhood of the product with $|t|\le R$. Let $C$ bound $|G|$ there. Cauchy's formula in time gives

$$
\frac{|X^kF(x)|}{k!}\le CR^{-k}.
$$

For $|t|\le r<R$, the series is dominated uniformly by $\sum_kC(r/R)^k$. Its sum is the Taylor expansion of $G$ in time, which proves (2.1). $\square$

Applying (2.1) to each coordinate function gives the flow itself. Analyticity is essential for this Taylor-series conclusion. Existence of a smooth flow alone does not imply that its Taylor series in time represents it.

**Example 2.2.** For $X=x^2\partial_x$, induction gives $X^kx=k!x^{k+1}$. Thus

$$
\exp(tX)(x)=x\sum_{k=0}^\infty(tx)^k=\frac{x}{1-tx},\qquad |tx|<1.
$$

Solving $\dot x=x^2$ gives the same expression wherever its denominator is nonzero. The series domain and the maximal rational expression's domain are not the same assertion.

For $X=x\partial_x$, $X^kx=x$ for $k\ge1$, giving $e^t x$. For $X=-y\partial_x+x\partial_y$, the powers alternate between $(x,y)$, $(-y,x)$, $(-x,-y)$, and $(y,-x)$, giving the rotation matrix from the first lesson.

## 3. Straightening and invariants

**Theorem 3.1.** If $X(p)\ne0$, there are analytic coordinates $(t,z_2,\ldots,z_n)$ near $p$ in which $X=\partial_t$. Every analytic first integral of $X$ is locally a function of $z_2,\ldots,z_n$.

**Proof.** Choose an analytic hypersurface $q(z)$ through $p$ whose tangent space is complementary to the line $\mathbb K X(p)$. Consider

$$
H(t,z)=\Phi_X^t(q(z)).
$$

Its derivative at $(0,z(p))$ has first column $X(p)$ and remaining columns spanning the chosen transverse hypersurface. It is invertible. The analytic inverse-function theorem makes $H$ a coordinate chart. Equation (1.2) says $\Phi_X^s(H(t,z))=H(t+s,z)$, hence $X=\partial_t$. The equation $XF=0$ becomes $\partial_tF=0$, so $F$ is a function of $z$ on a product coordinate neighbourhood. $\square$

For the dilation field $x\partial_x+y\partial_y$ on the real region $x>0$, take $t=\log x$ and $z=y/x$. Then $Xt=1$, $Xz=0$. Near any complex point with $x\ne0$, a local branch of $\log x$ gives the same construction. A point with $x=0$, $y\ne0$ uses the corresponding chart with $y$ instead. The zero of the field at the origin is excluded from the straightening theorem.

## 4. The bracket is a commutator of motions

For vector fields with coefficient columns $\xi$ and $\eta$,

$$
X,Y=D\eta(x)\xi(x)-D\xi(x)\eta(x).
\tag{4.1}
$$

**Theorem 4.1.** With map composition interpreted as above,

$$
\Phi_Y^{-s}\circ\Phi_X^{-t}\circ\Phi_Y^s\circ\Phi_X^t(x)
=x+stX,Y+O\bigl(|st|(|s|+|t|)\bigr).
\tag{4.2}
$$

The remainder bound is uniform on compact subsets of a sufficiently small coordinate neighbourhood.

**Proof.** The composition is analytic in $(s,t,x)$ and is the identity when $s=0$ or $t=0$. Thus every nonconstant Taylor monomial contains both $s$ and $t$. To find the mixed coefficient, retain only terms of degree at most one in each parameter. The first two motions give

$$
x+t\xi+s\eta+stD\eta\,\xi.
$$

Applying $\Phi_X^{-t}$ cancels $t\xi$ and adds the mixed term $-stD\xi\,\eta$. Applying $\Phi_Y^{-s}$ cancels $s\eta$; it creates no further term of degree $st$ because the pure $t$ term has already vanished. The remaining mixed coefficient is (4.1). Analyticity bounds the remaining terms by the stated expression on compact subsets. $\square$

As a sign check, take $X=\partial_x$ and $Y=x\partial_x$. The four maps send

$$
x\longmapsto x+t\longmapsto e^s(x+t)
\longmapsto e^s(x+t)-t\longmapsto x+t-te^{-s}.
$$

This is $x+st+O(|t||s|^2)$, consistent with $[X,Y]=\partial_x$. Reversing the two positive motions reverses the leading sign.

## 5. One-parameter subgroups inside a local group

Let $B_j$ be the parameter-space frame of the preceding lesson. For $v\in T_eG$, write $B_v=\sum_jv_jB_j$.

**Lemma 5.1.** The solution $a_v(t)$ of $\dot a=B_v(a)$, $a(0)=e$, satisfies

$$
a_v(s+t)=m(a_v(s),a_v(t)).
\tag{5.1}
$$

Its action on $M$ is the flow of $X_v=\sum_jv_jX_j$.

**Proof.** Differentiating local associativity shows that left multiplication $L_a(b)=m(a,b)$ carries $B_v(b)$ to $B_v(m(a,b))$. For fixed $s$, the right side of (5.1), as a curve in $t$, therefore solves the $B_v$ equation with initial value $a_v(s)$. So does $a_v(s+t)$. Uniqueness proves (5.1). The fundamental differential equations in geometric form give

$$
\frac{d}{dt}f(x,a_v(t))=X_v(f(x,a_v(t))),
$$

with initial value $x$, hence the last assertion. $\square$

**Theorem 5.2 (canonical coordinates).** Let an effective analytic local group have dimension $r$, with generators $X_1,\ldots,X_r$. Near the identity its transformations are precisely

$$
x\longmapsto\exp\left(\sum_{j=1}^r v_jX_j\right)(x),
\tag{5.2}
$$

for $v$ near zero. The parameters $v$ are essential. Ordered products of $r$ basis flows also give local coordinates.

**Proof.** Define $E(v)=a_v(1)$ for $v$ small. This is legitimate although Lemma 1.1 first provides a short time interval: the field $B_v$ tends uniformly to zero with $v$, so its flow exists through time one for $v$ in a sufficiently small neighbourhood. Analytic dependence makes $E$ analytic. Its expansion is $E(v)=e+v+O(|v|^2)$ in identity coordinates, since $B_j(e)=\partial_{a_j}$. Thus $DE(0)$ is the identity. The inverse-function theorem makes $E$ a parameter chart, and Lemma 5.1 gives (5.2). Essentiality is preserved by this invertible coordinate change.

For ordered products, the map

$$
(t_1,\ldots,t_r)\longmapsto
m(\cdots m(a_{e_1}(t_1),a_{e_2}(t_2))\cdots,a_{e_r}(t_r))
$$

also has derivative the identity at zero. It is a chart by the same theorem, and its action is $\Phi_{X_r}^{t_r}\circ\cdots\circ\Phi_{X_1}^{t_1}$. $\square$

For a one-dimensional local group, $E$ gives an additive parameter: (5.1) identifies multiplication with addition of times. For higher dimensions, canonical parameters do not generally add; their product records the brackets studied in the next lessons.

## 6. Exercises

**Exercise 1 (introductory).** Derive the flow of $x^2\partial_x$ by both the Lie series and separation of variables. State the domains of each derivation.

**Exercise 2 (intermediate).** Straighten $X=y\partial_x-x\partial_y$ near $(1,0)$ and identify one independent invariant.

**Exercise 3 (intermediate).** Verify (4.2) for $X=\partial_x$, $Y=x\partial_x$, including its sign and error term.

**Exercise 4 (intermediate).** Show that the flow of $(a+bx+cx^2)\partial_x$ is projective. Give a matrix formula and explain why all projective maps near the identity arise this way.

**Exercise 5 (advanced).** On a compact initial-point polydisc, establish an explicit geometric majorant for (2.1) using the time radius $R$ and bound $C$ in its proof. Explain why a formal exponential without this argument would not prove convergence.

## 7. Solutions

**Solution 1.** Since $X^kx=k!x^{k+1}$, the Lie series is $x\sum_{k\ge0}(tx)^k$, convergent for $|tx|<1$ and locally uniformly on strict subregions. For $x\ne0$, separation gives $-1/x(t)=t-1/x(0)$ and hence $x(t)=x(0)/(1-tx(0))$. The solution with initial value zero is constant. This rational expression continues the solution wherever its denominator is nonzero; it does not remove a finite-time pole.

**Solution 2.** Near $(1,0)$ choose $r=\sqrt{x^2+y^2}$ and a local angle $\theta=\arctan(y/x)$. Then $Xr=0$ and $X\theta=-1$. The coordinates $t=-\theta$, $z=r$ have independent derivatives there and give $X=\partial_t$. The independent invariant is $r$, or equivalently $r^2$ on this neighbourhood.

**Solution 3.** The exact composition is $x+t(1-e^{-s})$. Expanding $1-e^{-s}=s-s^2/2+O(s^3)$ gives $x+st+O(|t||s|^2)$, which satisfies the remainder bound in (4.2). Since $[\partial_x,x\partial_x]=\partial_x$, the sign is positive.

**Solution 4.** Let

$$
A=\begin{pmatrix}b/2&a\\-c&-b/2\end{pmatrix},\qquad M(t)=\exp(tA).
$$

If $x(t)$ is the ratio of the two components of a vector satisfying $\dot v=Av$, differentiating the ratio gives $\dot x=a+bx+cx^2$. Thus $x(t)=T_{M(t)}(x(0))$ on the chart where the denominator is nonzero. The three matrices obtained by varying $a,b,c$ independently form a basis of $\mathfrak{sl}_2$. The derivative at zero of $(a,b,c)\mapsto[\exp A]$ is invertible in the three-dimensional projective matrix chart. The inverse-function theorem therefore gives all projective transformations near the identity. This is a local assertion; it does not assert that every global real projective matrix has a real logarithm.

**Solution 5.** For $|t|\le r<R$, Cauchy's estimate gives $|t^kX^kF(x)/k!|\le C(r/R)^k$, uniformly on the compact initial-point set. The tail beginning at $N$ is at most $C(r/R)^N/(1-r/R)$. This proves uniform convergence and a quantitative error estimate. A formal series gives neither this bound nor a positive radius of convergence; the analytic flow supplies the required holomorphic time disc.

## What this lesson assumes

The analytic inverse-function theorem, elementary uniform convergence of holomorphic functions, and Cauchy's integral formula are assumed. Local analytic flow existence, its group law, Lie-series convergence, straightening, the commutator formula, and canonical parameter charts are proved here. No completeness or global exponential-surjectivity assertion is made.

## References

- Michael Kunzinger, *Lie Transformation Groups: An Introduction to Symmetry Group Analysis of Differential Equations*, 2015, corrected December 2024, Section 3.1. [Author's text](https://www.mat.univie.ac.at/~mike/teaching/ss15/ltg.pdf).
- Sophus Lie, with Friedrich Engel, *Theorie der Transformationsgruppen*, Volume I, 1888, Chapters 3 and 4.
- Joël Merker, *Theory of Transformation Groups, by S. Lie and F. Engel (Vol. I, 1888): Modern Presentation and English Translation*, 2010, discussions of flows, exponential formulas, and generation by one-term groups. [Author's preprint](https://arxiv.org/abs/1003.3202).

