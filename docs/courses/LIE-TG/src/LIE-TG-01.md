# Transformation groups and their parameters

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI), in Codex at Ultra. Public domain (CC0).*

A transformation can have many formulas without having many degrees of freedom. The map $x\mapsto x+a+b$, for example, depends on two displayed numbers but only on their sum. Before differentiating a family of transformations, we need to identify its actual parameters. We also need to distinguish a group from a family closed under composition. The latter need not contain an identity or inverses.

We work over $\mathbb K=\mathbb R$ or $\mathbb C$, with analytic maps; over $\mathbb C$ this means holomorphic maps. The prerequisite courses are [Multivariable Calculus](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-B50), [Complex Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C50), and [Smooth Manifolds and Differential Geometry](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D50). The analytic facts actually used are stated, with verified proof locators, at the end. The parameter arguments use finite measurements of a family, so that no inverse-function theorem on an infinite-dimensional space is needed.

## 1. Composition, identity, and domains

Let $M$ be an analytic manifold. A local transformation is an analytic diffeomorphism between open subsets of $M$. Its inverse exists on its image. This does not say that the inverse belongs to a specified family.

An analytic local Lie group is an analytic manifold $G$ with a distinguished point $e$, an analytic multiplication $m(a,b)$ defined on an open neighbourhood of $(e,e)$, and an analytic inverse $\iota(a)$ defined near $e$. We require

$$
m(e,a)=a=m(a,e),\qquad
m(a,\iota(a))=e=m(\iota(a),a).
$$

Associativity holds whenever both sides of

$$
m(m(a,b),c)=m(a,m(b,c))
$$

are defined near $(e,e,e)$. A restriction to a smaller neighbourhood is allowed. In particular, a local group need not have a single neighbourhood closed under every product.

For this course an action is a **right action**. Write $T_a(x)=f(x,a)$. Its equations are

$$
T_e(x)=x,\qquad T_b(T_a(x))=T_{m(a,b)}(x).
\tag{1.1}
$$

They hold on an open neighbourhood of $(x,e,e)$ on which the displayed expressions are defined. The map $(x,a)\mapsto T_a(x)$ is analytic. Each $T_a$ is a local diffeomorphism. The action may have stabilizers: different parameters can act alike at one point while acting differently on a neighbourhood.

**Example 1.1 (affine transformations).** Put

$$
T_{(\alpha,\beta)}(x)=\alpha x+\beta,\qquad \alpha\ne0.
$$

For $a=(\alpha,\beta)$ and $b=(\gamma,\delta)$,

$$
m(a,b)=(\gamma\alpha,\gamma\beta+\delta),\quad
e=(1,0),\quad
\iota(a)=(\alpha^{-1},-\beta/\alpha).
\tag{1.2}
$$

Substitution checks both inverse equations. Associativity follows either by substituting into (1.2) or by composing three affine maps. On the real line, parameters near $(1,0)$ have $\alpha>0$; the component with negative slope is not part of this identity neighbourhood.

**Example 1.2 (translations and rotations).** Translations on $\mathbb K^n$ have $T_a(x)=x+a$ and $m(a,b)=a+b$. On $\mathbb R^2$, rotations have

$$
T_t(x,y)=(x\cos t-y\sin t,\ x\sin t+y\cos t).
$$

The addition formulas give $T_s\circ T_t=T_{t+s}$. The angle is an essential local parameter near zero. Globally $t$ and $t+2\pi$ represent the same rotation; this discrete redundancy does not reduce the local dimension.

## 2. Measuring a family by finite jets

Consider an analytic family

$$
f:\Omega\times A\longrightarrow\mathbb K^n,
$$

where $\Omega\subset\mathbb K^n$ and $A\subset\mathbb K^r$ are connected open sets. Assume $D_xf$ is invertible. Fix $x_0\in\Omega$. For every component $i$ and multi-index $\nu$, let

$$
c_{i,\nu}(a)=\frac{1}{\nu!}\partial_x^\nu f_i(x_0,a).
$$

These coefficients determine the germ of $f(\cdot,a)$ at $x_0$. Define $q$ to be the largest rank attained by the derivative of any finite tuple of these coefficient functions on $A$. Thus $0\le q\le r$. If $q>0$, choose $q$ coefficients whose derivative has rank $q$ at a point $a_0$. This rank remains $q$ on a neighbourhood of $a_0$.

The points where such a maximal minor does not vanish form an open dense set: a nonzero real-analytic or holomorphic function cannot vanish on an open subset of a connected domain. We call these parameter points regular. Statements about essential parameters below concern a regular neighbourhood, not an arbitrary critical point.

**Theorem 2.1 (finite-jet reduction).** Near a regular parameter point there are analytic coordinates $(u,v)$ on $A$, with $u\in\mathbb K^q$, such that

$$
f(x,a)=g(x,u(a)).
\tag{2.1}
$$

The reduced family $g$ has $q$ essential parameters. No analytic reparametrization by fewer than $q$ parameters represents the same family on this neighbourhood.

**Proof.** Choose maximal-rank coefficients $c_1,\ldots,c_q$ and a nonzero $q\times q$ minor of their derivative at the regular point. Adjoin the $r-q$ original parameter coordinates outside the columns of that minor. The resulting map $a\mapsto(u,v)$, with $u_j=c_j$, has invertible derivative, so the analytic inverse theorem makes it a coordinate chart after shrinking. For any other coefficient $c$, the derivative of $(c_1,\ldots,c_q,c)$ has rank at most $q$ by the definition of $q$. Therefore $dc$ lies in the span of $du_1,\ldots,du_q$ at every point in the chosen neighbourhood. In coordinates, $\partial c/\partial v_\ell=0$.

Take a product coordinate neighbourhood, so that each $v$-fibre is connected. Every coefficient is constant on each fibre. For two parameter values with the same $u$, the Taylor series of $f$ at $x_0$ are identical. Analyticity gives equality near $x_0$, and uniqueness of analytic continuation gives equality on $\Omega$. Fixing one value $v_*$ defines $g(x,u)=f(x,(u,v_*))$, which proves (2.1). If necessary, shrink the $x$ and parameter neighbourhoods together to keep this expression defined.

Conversely, if $f(x,a)=h(x,w(a))$ with $w\in\mathbb K^s$, every finite coefficient map factors through $w$. The chain rule bounds its derivative rank by $s$. The chosen rank-$q$ coefficient map forces $s\ge q$. Applying this to $g$ proves its essentiality. If $q=0$, all coefficient derivatives vanish, and the same argument says that $f$ is locally independent of $a$. $\square$

**Theorem 2.2 (infinitesimal test for essentiality).** On a regular neighbourhood, the following are equivalent:

1. The family has $r$ essential parameters.
2. Some finite tuple of its Taylor coefficients has derivative rank $r$.
3. There is no nonzero analytic parameter vector field $\chi=\sum_{k=1}^r\chi_k(a)\partial_{a_k}$ satisfying

$$
\sum_{k=1}^r\chi_k(a)\frac{\partial f_i}{\partial a_k}(x,a)=0
\quad\text{for every }i\text{ and every }x.
\tag{2.2}
$$

Here nonzero means not identically zero on the neighbourhood.

**Proof.** Theorem 2.1 gives the equivalence of the first two conditions. If a coefficient tuple has full rank, differentiating (2.2) in $x$ shows that its derivative kills $\chi$, hence $\chi=0$. If the maximal rank is $q<r$, the coordinates $(u,v)$ constructed above give a nonzero field $\partial_{v_1}$ that kills $f$. Its expression in the original coordinates supplies analytic coefficients in (2.2). $\square$

The criterion concerns independence as functions of $x$. It does not require $r$ independent tangent vectors at a single $x$. The projective group of a line will have three essential parameters, although the tangent space of the line has dimension one.

The choice of $x_0$ does not change the reduced dimension. An identity between analytic transformations on a neighbourhood of one point holds on the connected domain, so reduction at one base point is reduction at any other. Applying Theorem 2.1 at both base points and using its minimality proves equality of the dimensions.

**Example 2.3 (critical parameters).** For $f(x,a,b)=x+ab$, the coefficient $ab$ has derivative $(b,a)$. Its generic rank is one. Thus the family has one essential parameter $u=ab$ near every point with $(a,b)\ne(0,0)$. At $(0,0)$ this coefficient has rank zero, so $ab$ cannot be used as a coordinate there. The formula still factors through $ab$; what fails there is a regular coordinate reduction. For $f(x,a,b)=x+a+b$, the reduction $u=a+b$, $v=a-b$ is regular everywhere.

## 3. The projective line has three parameters

An invertible matrix

$$
M=\begin{pmatrix}a&b\\c&d\end{pmatrix}
$$

acts on an affine chart of the projective line by

$$
T_M(x)=\frac{ax+b}{cx+d},\qquad ad-bc\ne0.
\tag{3.1}
$$

The denominator must be nonzero at the points under consideration. Near any such point the derivative is $(ad-bc)/(cx+d)^2$, so the map is locally invertible. Matrix inversion gives the inverse transformation. Multiplying $M$ by a nonzero scalar gives the same transformation.

**Proposition 3.1.** The family (3.1) has exactly three essential parameters near every projective transformation.

**Proof.** Near the identity, $d\ne0$, and scaling gives the representative

$$
M=\begin{pmatrix}\alpha&\beta\\\gamma&1\end{pmatrix}.
$$

At $(\alpha,\beta,\gamma)=(1,0,0)$ the three parameter derivatives of $T_M$ are $x$, $1$, and $-x^2$. They are independent as analytic functions on every open subset of the line. Theorem 2.2 therefore gives three essential parameters near the identity.

Composition with a fixed invertible projective transformation is an analytic invertible operation on transformation germs and an analytic coordinate change on projective matrix classes. It preserves the minimal number of parameters, giving the assertion near any matrix class.

For completeness, no further continuous ambiguity is hidden in the matrix description. If $M$ and $N$ have the same transformation on an open set, $N^{-1}M$ fixes every point of that set. Writing it as $\begin{pmatrix}A&B\\C&D\end{pmatrix}$ gives $Cx^2+(D-A)x-B=0$ on an open set. All three coefficients vanish, so $C=B=0$, $A=D$, and the matrix is scalar. $\square$

With the right-action convention (1.1), the parameter product represented by matrices is $[M]\cdot[N]=[NM]$. This order follows from $T_N\circ T_M=T_{NM}$.

## 4. A finite semigroup behaves differently

**Proposition 4.1.** A finite nonempty subset $S$ of a group, closed under multiplication, is a subgroup.

**Proof.** For $s\in S$, all positive powers lie in $S$. Finiteness gives $s^i=s^j$ with $1\le i<j$. Cancellation in the ambient group gives $s^{j-i}=e$, hence $e\in S$. If $j-i>1$, then $s^{j-i-1}\in S$ is the inverse of $s$. If $j-i=1$, then $s=e$ and its inverse is already in $S$. This works for every $s$. $\square$

Finiteness is essential. The maps

$$
x\longmapsto zx,\qquad 0<|z|<1,
\tag{4.1}
$$

are biholomorphisms of $\mathbb C$ and are closed under composition. Their multipliers multiply. They contain no identity, and the inverse multiplier $1/z$ never belongs to the family. They have one essential parameter because $\partial_z(zx)=x$ is not the zero function.

The zero multiplier must be excluded. Including it would make (4.1) cease to be a family of local diffeomorphisms.

## 5. An analytic parameter chart that cannot be continued

The example (4.1) embeds in the multiplicative group $\mathbb C^*$. Engel's historical example addresses a subtler question: can a chosen analytic **parameter chart and its multiplication law** be continued to reach the identity? We give a version with an explicit verified chart. This distinction prevents a coordinate obstruction from being mistaken for an intrinsic obstruction to embedding transformations in a group.

Let $D=\{z:|z|<1\}$ and define

$$
h(z)=z+\frac14\sum_{k=1}^\infty\frac{z^{2^k}}{4^k}.
\tag{5.1}
$$

**Lemma 5.1.** The map $h$ is holomorphic and injective on $D$, extends continuously and injectively to $\overline D$, has $h'(z)\ne0$ on $\overline D$, and admits no holomorphic continuation across any point of $\partial D$.

**Proof.** The series for $h$ and for

$$
h'(z)=1+\frac14\sum_{k=1}^\infty\frac{z^{2^k-1}}{2^k}
$$

converge uniformly on the closed disc. Consequently $|h'(z)-1|\le1/4$. For $z,w\in D$, integration along the straight segment gives

$$
|h(z)-h(w)-(z-w)|\le\frac14|z-w|.
$$

Continuity extends this inequality to $\overline D$. Thus $h$ is injective there, with $|h(z)-h(w)|\ge3|z-w|/4$, and $h'$ is nonzero.

Now let $\zeta$ be any root of unity whose order is a power of two. For all sufficiently large $k$, $\zeta^{2^k}=1$. Inside $D$,

$$
h''(z)=\frac14\sum_{k=1}^\infty(1-2^{-k})z^{2^k-2}.
$$

At $z=r\zeta$, after multiplying by $\zeta^2$, all sufficiently late summands are the positive real numbers $(1-2^{-k})r^{2^k-2}/4$. Their sum tends to $+\infty$ as $r\uparrow1$: for any fixed number of late terms each tends to at least $1/8$, and that number can be arbitrarily large. The finitely many earlier terms stay bounded. Hence $h''$ is unbounded along this radius. A holomorphic extension across $\zeta$ would have bounded second derivative on a smaller neighbourhood, a contradiction.

These roots of unity are dense in the unit circle. An extension across any other boundary point would also extend across a nearby such root, since an open disc about that point contains an arc of the circle. Thus no boundary point permits an extension. $\square$

Put $\Lambda=h(D)$ and $\chi=h^{-1}:\Lambda\to D$. The inverse is holomorphic by the inverse-function theorem. Since $h$ is injective on the compact closed disc, it is a homeomorphism onto its image there. In particular, $\partial\Lambda=h(\partial D)$.

**Lemma 5.2.** The function $\chi$ has no holomorphic extension across a point of $\partial\Lambda$.

**Proof.** Suppose it extends across $\lambda_0=h(\zeta)$, $|\zeta|=1$. Along $\lambda=h(r\zeta)$, continuity gives $\chi(\lambda)\to\zeta$ and

$$
\chi'(\lambda)=\frac1{h'(r\zeta)}\longrightarrow\frac1{h'(\zeta)}\ne0.
$$

The extension therefore takes value $\zeta$ and has nonzero derivative at $\lambda_0$. Its local inverse extends $h$ across $\zeta$, contradicting Lemma 5.1. $\square$

**Theorem 5.3 (Engel-type family).** On $\Lambda^*=\Lambda\setminus\{0\}$, the family

$$
T_\lambda(x)=\chi(\lambda)x
$$

has one essential parameter and is closed under composition with analytic law

$$
\phi(\lambda,\mu)=h\bigl(\chi(\lambda)\chi(\mu)\bigr).
\tag{5.2}
$$

It contains neither identity nor inverses. The law (5.2) cannot be holomorphically extended across any point of $\partial\Lambda$ in either parameter. In particular, it cannot reach the identity while retaining this parameter chart. After the reparametrization $z=\chi(\lambda)$, the same transformations are a subfamily of $\mathbb C^*$.

**Proof.** Nonzero multipliers of modulus less than one multiply to another such multiplier. This proves closure and the formula. Since $\chi'\ne0$, the derivative $\chi'(\lambda)x$ is not identically zero, proving essentiality. The identity has multiplier one, and an inverse multiplier has modulus greater than one, proving their absence.

Fix $\mu\in\Lambda^*$ and set $w=\chi(\mu)$. Then $0<|w|<1$.

Suppose $\phi(\lambda,\mu)$ extends across $\lambda_0=h(\zeta)\in\partial\Lambda$. Its limiting value there is $h(\zeta w)$, an interior point of $\Lambda$. On a sufficiently small neighbourhood the extended values remain in $\Lambda$. Then

$$
\frac1w\chi\bigl(\phi(\lambda,\mu)\bigr)
$$

extends $\chi(\lambda)$ across $\lambda_0$, contrary to Lemma 5.2. The argument in the other parameter is identical. Reparametrizing by $z$ gives exactly (4.1), which lies in $\mathbb C^*$. $\square$

The useful conclusion is that closure alone supplies neither the identity axiom nor the inverse axiom. The statement that such a family cannot belong to any larger one-parameter group would be false. In the next lessons we work near a specified identity and derive the infinitesimal structure there.

## 6. Exercises

**Exercise 1 (introductory).** For $T_{(\alpha,\beta)}(x)=\alpha x+\beta$, derive the product, identity, and inverse using (1.1). Compute the commutator of a translation by $b$ and a dilation by $\alpha$.

**Exercise 2 (intermediate).** Near the identity in (3.1), show that the value, first derivative, and second derivative at zero already detect all three essential parameters.

**Exercise 3 (intermediate).** Reduce $x\mapsto x+ab$ near $(a,b)=(2,0)$ and explain why the same coordinate choice fails at $(0,0)$.

**Exercise 4 (intermediate).** Give a proof of Proposition 4.1 using the injectivity of left multiplication on the finite set $S$.

**Exercise 5 (advanced).** Replace $1/4$ in (5.1) by a real number $\varepsilon$ with $0<\varepsilon<1$. Prove all assertions of Theorem 5.3 and explain which conclusions fail when the puncture is filled.

## 7. Solutions

**Solution 1.** Substitution gives $\gamma(\alpha x+\beta)+\delta$, so the product is (1.2). Solving $\alpha x+\beta=y$ gives the inverse $y/\alpha-\beta/\alpha$. Let $A(x)=x+b$ and $B(x)=\alpha x$. With the explicitly specified commutator $B^{-1}\circ A^{-1}\circ B\circ A$, the successive images are $x+b$, $\alpha x+\alpha b$, $\alpha x+\alpha b-b$, and $x+b-b/\alpha$. Thus it is translation by $b(1-1/\alpha)$. This also shows that translations and dilations need not commute.

**Solution 2.** In the chart $d=1$,

$$
T(0)=\beta,\quad T'(0)=\alpha-\beta\gamma,\quad
T''(0)=-2\gamma(\alpha-\beta\gamma).
$$

Because $T'(0)\ne0$, these data recover $\beta=T(0)$, $\gamma=-T''(0)/(2T'(0))$, and $\alpha=T'(0)+\beta\gamma$. They are analytic local coordinates on the three-parameter family. Scalar matrix ambiguity has already removed the fourth parameter.

**Solution 3.** Set $u=ab$, $v=a$. The Jacobian determinant of $(u,v)$ with respect to $(a,b)$ is $-a$, which is nonzero near $(2,0)$. The family becomes $x\mapsto x+u$. At $(0,0)$ every first derivative of $ab$ vanishes, so $(ab,a)$ is not a coordinate chart. The generic essential dimension remains one; it is not computed by the rank at this critical point.

**Solution 4.** For $s\in S$, the map $L_s:S\to S$ is injective by cancellation, hence surjective by finiteness. Some $t\in S$ satisfies $st=s$. Cancelling $s$ in the ambient group gives $t=e$, so $e\in S$. Surjectivity again gives $u\in S$ with $su=e$, and $u=s^{-1}$. Hence $S$ is a subgroup.

**Solution 5.** The derivative bound becomes $|h'-1|\le\varepsilon$, and the lower Lipschitz bound is $(1-\varepsilon)|z-w|$. Both remain positive. At a dyadic root of unity the tail of $\zeta^2h''(r\zeta)$ is a positive sum with coefficients $\varepsilon(1-2^{-k})$, so it diverges exactly as before. Lemmas 5.1 and 5.2 follow, and the fixed-$\mu$ argument proves the multiplication-law obstruction. Filling the puncture adds $T_0(x)=0$. This map has zero derivative, so it is not a local diffeomorphism and has no inverse. The family is still a semigroup, now with an absorbing element, but no longer consists entirely of transformations in the sense of Section 1.

## What this lesson assumes

**Local analytic inverse theorem.** If $F:U\subset\mathbb K^r\to\mathbb K^r$ is analytic and $\det DF(a_0)\ne0$, there are open neighbourhoods $V$ of $a_0$ and $W$ of $F(a_0)$ such that $F:V\to W$ is bijective with analytic inverse. Its derivative at $F(a)$ is $DF(a)^{-1}$. In one complex variable, this is [Lebl, *Guide to Cultivating Complex Analysis*, Theorem 2.2.8, p. 36]. The underlying real $C^1$ theorem, including its contraction proof, is Theorem B.3.16, pp. 289–291; the contraction theorem is B.3.15, p. 288.

Here is the analytic upgrade needed in several variables. For holomorphic $F$, the real determinant is $|\det DF|^2$ [Lebl, *Tasty Bits of Several Complex Variables*, Proposition 1.3.7, p. 27]. The real inverse theorem therefore gives a $C^1$ inverse. Its differential is the inverse of a complex-linear map and hence is complex-linear; the Cauchy–Riemann equations make the inverse holomorphic. This proves the inverse statement asked for in Exercise 1.3.6, p. 27, by the same route as Theorem 1.3.8 there. A real-analytic $F$ extends locally holomorphically by its convergent power series [Proposition 3.1.3, p. 87]. Its derivative at a real point remains invertible over $\mathbb C$. The holomorphic inverse commutes with conjugation by uniqueness, so its restriction to real points is real analytic. Thus a smooth inverse theorem alone is not the analytic justification.

**Finite-rank coordinate consequence.** If $q$ analytic scalar functions have independent differentials at a point of $\mathbb K^r$, they can serve as the first $q$ coordinates of an analytic chart. The proof is precisely the minor-and-adjoined-coordinates argument in Theorem 2.1. If every additional coefficient has differential in their span, its derivatives in the remaining coordinates vanish. This is the entire constant-rank consequence used here.

**Connected-domain analytic identity theorem.** An analytic scalar function on a connected open subset of $\mathbb K^n$ that vanishes on a nonempty open subset vanishes everywhere. The holomorphic theorem and proof are [Lebl, *Tasty Bits*, Theorem 1.2.6, p. 21]; its real-analytic version is Exercise 3.1.1, p. 87. For either field, take the set of points where every derivative vanishes. It is nonempty and closed by continuity, and open because the convergent Taylor series is zero there. Connectedness makes it the entire domain. Applying this to the difference of two functions gives the uniqueness used in Section 2.

All parameter-reduction and semigroup assertions used here are proved in the lesson. No theorem about infinite-dimensional analytic manifolds or existence of a Riemann map is used.

## References

- Michael Kunzinger, *Lie Transformation Groups: An Introduction to Symmetry Group Analysis of Differential Equations*, lecture notes, 2015, corrected version December 2024, Chapter 3, Section 3.1. [Author's text](https://www.mat.univie.ac.at/~mike/teaching/ss15/ltg.pdf).
- Sophus Lie, with Friedrich Engel, *Theorie der Transformationsgruppen*, Volume I, 1888, Chapter 1, §§1–5, pp. 11–26; Chapter 9, §44, pp. 163–165, for the inverse axiom and Engel's example. The construction in Section 5 uses a different explicitly checked series.
- Joël Merker, *Theory of Transformation Groups, by S. Lie and F. Engel (Vol. I, 1888): Modern Presentation and English Translation*, 2010, introductory discussion of the inverse axiom. [Author's preprint](https://arxiv.org/abs/1003.3202).
- Jiří Lebl, *Guide to Cultivating Complex Analysis*, Theorem 2.2.8, p. 36, and Theorems B.3.15–B.3.16, pp. 288–291. [Author's text](https://www.jirka.org/ca/ca.pdf).
- Jiří Lebl, *Tasty Bits of Several Complex Variables*, version 3.4 (2020), Theorem 1.2.6, p. 21; Proposition 1.3.7, Theorem 1.3.8 and Exercise 1.3.6, p. 27; Proposition 3.1.3 and Exercise 3.1.1, p. 87. [Author's text](https://www.jirka.org/scv/scv-3.4.pdf).

