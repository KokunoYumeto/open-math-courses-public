# Prolongation, differential invariants and the projective group

*Written and self-checked by the writing AI, GPT-6.1 Sol (OpenAI), in Codex at Ultra, October 2026. Public domain (CC0).*

A transformation of points also transforms derivatives of graphs. Prolongation records that transformation on a finite-dimensional jet space. It makes differential equations into geometric subsets and their symmetry conditions into tangency equations. Curvature and the Schwarzian derivative arise as coordinates transverse to the resulting orbits.

We use analytic graphs $u:\mathbb K^n\to\mathbb K^m$ and local point diffeomorphisms of $(x,u)$, with $\mathbb K=\mathbb R$ or $\mathbb C$. The regular-submanifold criterion and invariant count from Complete systems and invariants are available. Real oriented plane curves are used for Euclidean curvature. The invariant count is local at regular jets; the finite-generation theorem stated later has additional hypotheses.

## 1. Jets and transformed graphs

Two graphs have the same $k$-jet at $x$ when their derivatives through order $k$ agree there. Write coordinates on $J^k(\mathbb K^n,\mathbb K^m)$ as

$$
(x^i,u^\alpha_J),\qquad |J|\le k,\quad
1\le i\le n,\quad1\le\alpha\le m.
$$

Here $J$ is an unordered multi-index, including the empty index $u^\alpha_\varnothing=u^\alpha$. Mixed derivatives are symmetric, so each multi-index occurs once. The dimension is

$$
N_k=n+m\binom{n+k}{k}.
\tag{1.1}
$$

The binomial coefficient counts all monomials in $n$ variables of degree at most $k$, equivalently all partial derivatives of those orders.

For a function $F$ of jets of order at most $k$, its total derivative is a function of order at most $k+1$:

$$
D_iF=\partial_{x^i}F+
\sum_{\alpha,\,|J|\le k}u^\alpha_{J,i}\partial_{u^\alpha_J}F.
\tag{1.2}
$$

It satisfies $(D_iF)(j^{k+1}u(x))=\partial_i(F(j^ku(x)))$ by the ordinary chain rule. The total derivatives commute on functions of finite jet order, because mixed partial derivatives of every realizing graph commute. Every finite jet is realized by its Taylor polynomial, so this graph calculation proves the identity on jet coordinates.

Let a point transformation be $(x,u)\mapsto(\widetilde x,\widetilde u)=(X(x,u),U(x,u))$. On a graph, put

$$
A^j_i=D_iX^j.
$$

Where $\det A\ne0$, the transformed submanifold is again a graph over $\widetilde x$. Its derivatives are calculated using

$$
\widetilde D_j=(A^{-1})^i_jD_i,\qquad
\widetilde u^\alpha_j=(A^{-1})^i_jD_iU^\alpha.
\tag{1.3}
$$

Repeating (1.3) determines all transformed derivatives through order $k$. At each step, the result depends only on the original derivatives through that order, so it is independent of the realizing graph. This defines the **prolonged transformation** on $J^k$. Transforming a graph in two steps gives the same jet as transforming it by the composite; therefore prolongation preserves the transformation law. Its domain includes the graph-transversality condition $\det A\ne0$.

## 2. The prolongation formula

Let

$$
v=\sum_i\xi^i(x,u)\partial_{x^i}
+\sum_\alpha\phi^\alpha(x,u)\partial_{u^\alpha}.
$$

The generator of its prolonged flow has the form

$$
\operatorname{pr}^{(k)}v=
\sum_i\xi^i\partial_{x^i}
+\sum_{\alpha,\,|J|\le k}\phi^\alpha_J\partial_{u^\alpha_J},
\qquad \phi^\alpha_\varnothing=\phi^\alpha.
\tag{2.1}
$$

**Theorem 2.1 (prolongation).** Set $Q^\alpha=\phi^\alpha-\sum_i\xi^iu^\alpha_i$. Then

$$
\phi^\alpha_{J,i}
=D_i\phi^\alpha_J-\sum_j u^\alpha_{J,j}D_i\xi^j,
\qquad
\phi^\alpha_J=D_JQ^\alpha+\sum_i\xi^iu^\alpha_{J,i}.
\tag{2.2}
$$

In particular, the apparent order-$|J|+1$ derivatives in the second formula cancel.

**Proof.** Write the point flow to first order as $X^j=x^j+t\xi^j+O(t^2)$ and $U^\alpha=u^\alpha+t\phi^\alpha+O(t^2)$. Its total derivative matrix is $A^j_i=\delta^j_i+tD_i\xi^j+O(t^2)$, so (1.3) gives

$$
\widetilde D_i=D_i-t\sum_j(D_i\xi^j)D_j+O(t^2).
$$

If $\widetilde u^\alpha_J=u^\alpha_J+t\phi^\alpha_J+O(t^2)$, differentiate it with $\widetilde D_i$. The coefficient of $t$ is precisely the recurrence in (2.2). Its initial coefficient is $\phi^\alpha$. This proves the recurrence for every order by induction.

At the empty index, the characteristic formula is $Q^\alpha+\xi^iu^\alpha_i=\phi^\alpha$. Suppose it holds for $J$. Substitute it into the recurrence:

$$
\begin{aligned}
\phi^\alpha_{J,i}
&=D_iD_JQ^\alpha+
\sum_j(D_i\xi^j)u^\alpha_{J,j}
+\sum_j\xi^ju^\alpha_{J,j,i}
-\sum_j u^\alpha_{J,j}D_i\xi^j\\
&=D_{J,i}Q^\alpha+\sum_j\xi^ju^\alpha_{J,i,j}.
\end{aligned}
$$

Commutation of total derivatives and symmetry of jet indices complete the induction. Since $Q^\alpha=\phi^\alpha-\xi^iu^\alpha_i$, its highest derivative term is $-\xi^iu^\alpha_{J,i}$, canceling the displayed correction. Alternatively, the recurrence directly proves that $\phi_J$ has order at most $|J|$. $\square$

The compact notation is

$$
\operatorname{pr}v=\operatorname{pr}v_Q+\sum_i\xi^iD_i,
\qquad
\operatorname{pr}v_Q=\sum_{\alpha,J}D_JQ^\alpha\partial_{u^\alpha_J}.
\tag{2.3}
$$

These are identities on the infinite jet space, or on functions of finite order with one extra jet level available. The two terms on the right need not separately be vector fields on $J^k$; their sum has the cancellation just proved. This qualification avoids treating a top-order total derivative as an intrinsic vector field on a finite jet space.

## 3. Equations as jet submanifolds

Let $\Delta=(\Delta_1,\ldots,\Delta_s)$ be a system on $J^k$, with $d\Delta$ of rank $s$ on $E=\{\Delta=0\}$.

**Theorem 3.1 (infinitesimal criterion).** A connected local point group preserves the equation submanifold $E$ under prolongation exactly when

$$
\operatorname{pr}^{(k)}v(\Delta_a)=0\quad\text{on }E
\tag{3.1}
$$

for each equation and each infinitesimal generator.

**Proof.** The rank assumption identifies $T_\zeta E$ with $\ker d\Delta_\zeta$. Condition (3.1) is exactly tangency of the prolonged fields. A tangent field has a restricted flow on $E$; uniqueness of the ambient ODE makes that flow agree with its ambient flow. Products of generator flows give every sufficiently small transformation of the connected group. Conversely, differentiating preservation of $E$ yields tangency and (3.1). $\square$

Preservation of $E$ implies that transformed solution graphs are still solutions, whenever they remain graphs. If “symmetry” means only preservation of actual solutions, necessity of (3.1) additionally requires that every equation jet being tested be locally realized by a solution. A maximal-rank system alone does not guarantee this realization for an arbitrary PDE system. The theorem above concerns the entire jet submanifold and is the precise geometric version proved here.

For singular defining equations, tangency can fail to be sufficient. For example $\Delta=u^2$ has zero derivative on $u=0$, so $v=\partial_u$ satisfies $v\Delta=0$ there, but its translations do not preserve $u=0$. Necessity survives for a preserved zero set. The sketch's statement reversing this implication is corrected accordingly.

**Example 3.2: heat scaling and a boost.** For $\Delta=u_t-u_{xx}$, take $v=x\partial_x+2t\partial_t$. Formula (2.2) gives $\phi_t=-2u_t$ and $\phi_{xx}=-2u_{xx}$, hence $\operatorname{pr}v(\Delta)=-2\Delta$.

For $w=2t\partial_x-xu\partial_u$, the same recurrence gives

$$
\phi_t=-xu_t-2u_x,\qquad
\phi_x=-u-xu_x,\qquad
\phi_{xx}=-2u_x-xu_{xx}.
$$

Thus $\operatorname{pr}w(\Delta)=-x\Delta$. Both are symmetries. Their finite transformations are

$$
(x,t,u)\mapsto(e^\varepsilon x,e^{2\varepsilon}t,u),\qquad
(x,t,u)\mapsto(x+2\varepsilon t,t,e^{-\varepsilon x-\varepsilon^2t}u).
$$

The boost consequently sends a solution $f$ to $e^{-\varepsilon x+\varepsilon^2t}f(x-2\varepsilon t,t)$. The differing signs of the two exponential expressions come from expressing the transformed graph in its new independent variables.

## 4. Counting invariants and differentiating them

A differential invariant of order at most $k$ is a function on $J^k$ constant along prolonged orbits.

**Theorem 4.1 (local count).** If the prolonged orbit distribution has constant rank $r_k$ near a jet, there are $N_k-r_k$ functionally independent local invariants, and every local invariant is a function of these.

**Proof.** The prolonged action is a local transformation group by Section 1. Its orbit distribution is involutive. Frobenius provides coordinates $(s^1,\ldots,s^{r_k},I^1,\ldots,I^{N_k-r_k})$ with orbits given by constant $I$. A function is invariant exactly when it is independent of the $s$ coordinates. The $I$ are independent, and no larger independent family can be constant on a distribution of rank $r_k$. $\square$

An **invariant derivative** is a total derivative combination that carries invariants to invariants. For instance, if $n$ invariants $I^1,\ldots,I^n$ have invertible horizontal derivative matrix $A^a_i=D_iI^a$, define $\nabla_a$ by

$$
\nabla_a=(A^{-1})^i_aD_i.
\tag{4.1}
$$

The horizontal differential of another invariant has the unique expression $d_HF=\sum_a(\nabla_aF)d_HI^a$. Point prolongations preserve horizontal differentiation, as (1.3) shows. Pulling back this equality and using invariance of $F,I^a$ proves invariance of its coefficients $\nabla_aF$. The invertibility condition is essential. In other actions, invariant derivatives can instead come from invariant geometric quantities such as arclength.

**Lie–Tresse finiteness, stated without proof.** For an algebraic transitive pseudogroup action on a formally integrable irreducible differential equation, outside a suitable invariant exceptional set pulled back from a finite jet level, its rational-polynomial differential invariants are generated by finitely many basic invariants and finitely many rational invariant derivations. Higher derivatives of those generators and rational functions of the basic ones supply the specified invariant algebra. This is differential generation, not ordinary finite generation without derivatives. A precise modern statement is Kruglikov–Lychagin, [*Global Lie–Tresse theorem*](https://math.uit.no/seminar/Preprints/11-12-BKVL.pdf), Theorems 1–2, printed pp. 3–4. The hypotheses and exceptional set cannot be dropped; Theorem 4.1 alone is an order-by-order local result and does not prove this finiteness theorem.

## 5. Euclidean curvature

For a graph $y=f(x)$, write $p=f'$, $q=f''$, $r=f'''$. Its oriented tangent is $(1,p)$ and its speed is $\sqrt{1+p^2}$. In the real graph chart with the orientation of increasing $x$, define

$$
\kappa=\frac{q}{(1+p^2)^{3/2}},\qquad
D_s=\frac1{\sqrt{1+p^2}}D_x.
\tag{5.1}
$$

Translation leaves derivatives unchanged. A rotation preserves speed and the determinant of the tangent and its derivative; for a parametrized curve $\gamma$, their ratio $\det(\gamma',\gamma'')/|\gamma'|^3$ is unchanged. This proves invariance of signed curvature and arclength differentiation under $\operatorname{SE}(2)$. In a graph chart, restrict to nearby transformations for which the new increasing independent coordinate agrees with the chosen orientation. A distant rotation that reverses that coordinate requires a change of graph orientation.

Move the point to the origin and rotate its tangent to the positive horizontal axis. The normalized jet has $x=y=p=0$, and its second derivative is $\kappa$. At third order its third derivative is

$$
D_s\kappa=\frac{r}{(1+p^2)^2}-\frac{3pq^2}{(1+p^2)^3}.
\tag{5.2}
$$

Indeed, (5.2) follows by differentiating (5.1), and at a horizontal normalized tangent it equals the third graph derivative. The point and tangent normalization is unique locally. It follows that all invariants through order two are functions of $\kappa$, and all through order three are functions of $\kappa,D_s\kappa$. The prolonged action has rank three from order one onward, so the count is zero at orders zero and one, one at order two, and two at order three.

For comparison, special affine transformations preserve determinants rather than Euclidean length. Where $\det(\gamma',\gamma'')>0$, set $ds=\det(\gamma',\gamma'')^{1/3}dt$. Then $\det(\gamma_s,\gamma_{ss})=1$. Differentiating gives $\det(\gamma_s,\gamma_{sss})=0$, so $\gamma_{sss}=-\kappa_{\rm aff}\gamma_s$, with $\kappa_{\rm aff}=\det(\gamma_{ss},\gamma_{sss})$. These equations define equiaffine curvature and show its invariance under translations and determinant-one linear maps. They apply only on the stated nondegenerate branch.

## 6. The Schwarzian derivative

Now let the projective group act on the dependent variable alone:

$$
y\longmapsto M(y)=\frac{ay+b}{cy+d},\qquad ad-bc\ne0,
$$

while $x$ is fixed. Work where $y'\ne0$ and $cy+d\ne0$. Define

$$
S(y)=\frac{y'''}{y'}-\frac32\left(\frac{y''}{y'}\right)^2.
\tag{6.1}
$$

**Theorem 6.1.** The Schwarzian is invariant under this action. Locally on its regular jet domain, every differential invariant of order at most three is a function of $x$ and $S(y)$.

**Proof.** Put $L_y=y''/y'$. Differentiation gives $S(y)=D_xL_y-\tfrac12L_y^2$. For a composition $f\circ y$,

$$
L_{f\circ y}=\frac{f''(y)}{f'(y)}y'+L_y.
$$

Differentiate and subtract half the square. The mixed terms cancel because $y''=L_y y'$, yielding the chain rule

$$
S(f\circ y)=S(f)(y)(y')^2+S(y).
\tag{6.2}
$$

For a Möbius function, $M''/M'=-2c/(cy+d)$, whose derivative is $2c^2/(cy+d)^2$; subtraction of half its square gives $S(M)=0$. Equation (6.2) proves invariance.

To prove completeness, take a jet $(x,y_0,p,q,r)$ with $p\ne0$. The Möbius transformation

$$
M(y)=\frac{(y-y_0)/p}{1+\frac{q}{2p^2}(y-y_0)}
\tag{6.3}
$$

normalizes its dependent-variable coordinates to $\widetilde y=0$, $\widetilde p=1$, $\widetilde q=0$. Its third derivative on the graph is

$$
\widetilde r=\frac rp-\frac32\frac{q^2}{p^2}=S(y).
$$

The three normalization conditions determine (6.3) uniquely. They define a local orbit section; after normalizing a reference jet, restrict nearby jets so that their relative normalizers lie near the identity. Thus a locally invariant function depends only on the remaining section coordinates $x,S$. Their differentials are independent, since $\partial S/\partial r=1/p\ne0$. For the real identity component, the sign of $p$ is fixed on each regular component; one may use normalized $\widetilde p=-1$ instead on the negative component. The same conclusion holds locally there. $\square$

There are no new invariants below order three besides $x$: the action has ranks one, two, and three on the dependent jet coordinates through orders zero, one, and two. Since $x$ is fixed, $D_x$ itself is an invariant derivative and produces $D_xS,D_x^2S,\ldots$ at higher orders.

## 7. The projective algebra in any dimension

In homogeneous coordinates $(x,1)$, an infinitesimal matrix

$$
A=\begin{pmatrix}B&b\\c^t&d\end{pmatrix},\qquad \operatorname{tr}B+d=0,
$$

acts in an affine chart with coefficient field

$$
\xi_A(x)=b+(B-dI)x-(c\cdot x)x.
\tag{7.1}
$$

This follows by differentiating the ratio of the first $n$ homogeneous coordinates to the last one for $I+tA$.

**Theorem 7.1.** The projective infinitesimal fields form a Lie algebra of dimension $n(n+2)$, spanned by

$$
P_i=\partial_{x_i},\qquad
L_{ij}=x_j\partial_{x_i},\qquad
Q_i=x_iE,\quad E=\sum_jx_j\partial_{x_j}.
\tag{7.2}
$$

With bracket $XY-YX$, the isomorphism from $\mathfrak{sl}_{n+1}$ is $A\mapsto-\xi_A$.

**Proof.** Formula (7.1) gives exactly the constant, arbitrary linear, and indicated quadratic fields. To see that every linear matrix occurs, for a desired matrix $L$ choose $d=-\operatorname{tr}L/(n+1)$ and $B=L+dI$. The other blocks supply arbitrary constant and quadratic coefficients. These $n+n^2+n$ fields are independent: separate homogeneous degrees, then the coefficients of $(c\cdot x)x$ force $c=0$.

The kernel of (7.1) is also zero on trace-zero matrices. Its polynomial coefficients force $b=c=0$ and $B=dI$; the trace gives $(n+1)d=0$. The infinitesimal fields of a left matrix action reverse the matrix commutator, so $[\xi_A,\xi_C]=-\xi_{[A,C]}$, as follows either by differentiating the composition law or by the coordinate coefficient formula. Negating the fields gives the claimed bracket-preserving isomorphism. Their dimension equals $\dim\mathfrak{sl}_{n+1}=(n+1)^2-1=n(n+2)$. $\square$

For example,

$$
[P_i,L_{kj}]=\delta_{ij}P_k,\quad
[L_{ij},L_{k\ell}]=\delta_{i\ell}L_{kj}-\delta_{kj}L_{i\ell},
\qquad
[P_i,Q_j]=\delta_{ij}E+L_{ij},\quad
[L_{ij},Q_k]=\delta_{ik}Q_j,\quad[Q_i,Q_j]=0.
$$

In the plane the eight fields are $\partial_x,\partial_y,x\partial_x,y\partial_x,x\partial_y,y\partial_y,xE,yE$.

The full isotropy at the affine origin is spanned by the linear and quadratic fields in (7.2), with dimension $n^2+n$. Its linear homogeneous subgroup is $\operatorname{GL}_n$, of dimension $n^2$. These are different groups: the full projective stabilizer also has nonlinear transformations whose quadratic generators vanish to first order at the origin.

Full translation subgroups associated to affine charts are conjugate. To see this precisely, let the hyperplane at infinity be $\ker\ell$ in homogeneous space. Its translations are represented by $I+v\ell$ with $v\in\ker\ell$; multiplication adds $v$ because $(v\ell)(w\ell)=0$. Conjugation by an invertible matrix $C$ gives $I+(Cv)(\ell C^{-1})$, the translation group for $C(\ker\ell)$. The projective group is transitive on hyperplanes. This establishes conjugacy for these translation groups, rather than for every abelian projective subgroup.

The same statement holds for translation subgroups of any fixed dimension $m\le n$. Within an affine chart, such a subgroup translates by a vector subspace $V$ of dimension $m$. Choose a basis of $V$, extend it to a basis of $\mathbb K^n$, and do the same for another $m$-dimensional subspace $W$. The linear map carrying the first basis to the second conjugates the two translation groups. Combining this with the preceding change of affine chart proves the projective conjugacy of all the stated $m$-dimensional translation subgroups. The value of $m$ must agree.

## 8. Exercises

**Exercise 1 (easy).** Prolong $v=x\partial_x+2u\partial_u$ through order two, with $p=u'$ and $q=u''$.

**Exercise 2 (medium).** Find every infinitesimal point symmetry of $u''=0$. Prove that the answer is eight-dimensional and identify it with the projective algebra of the plane.

**Exercise 3 (medium).** Verify (6.2) directly and use it to prove Möbius invariance of (6.1). Explain why $x$ must be included in the list of all invariants.

**Exercise 4 (medium).** Count the local differential invariants of $\operatorname{SE}(2)$ on oriented graph curves through order three. Prove that (5.1) and (5.2) form a complete independent set at order three.

**Exercise 5 (hard).** Prove the multi-index formula (2.2) by induction, including the cancellation of order-$|J|+1$ derivatives and the role of the graph-transversality matrix.

## 9. Solutions

**Solution 1.** The recurrence gives $\phi_p=D_x(2u)-pD_xx=p$, and $\phi_q=D_xp-qD_xx=0$. Thus $\operatorname{pr}^{(2)}v=x\partial_x+2u\partial_u+p\partial_p$, with no $\partial_q$ term. Equivalently, the finite scaling sends $(x,u,p,q)$ to $(e^t x,e^{2t}u,e^tp,q)$.

**Solution 2.** Let $v=\xi(x,u)\partial_x+\phi(x,u)\partial_u$. Its first prolonged coefficient is $\phi_x+(\phi_u-\xi_x)p-\xi_up^2$. Applying the recurrence once more and setting $q=0$ gives

$$
\phi_{xx}+(2\phi_{xu}-\xi_{xx})p
+(\phi_{uu}-2\xi_{xu})p^2-\xi_{uu}p^3=0.
$$

Every slope $p$ is realized by a straight-line solution, so the four coefficients vanish. From $\xi_{uu}=0$ and $\phi_{xx}=0$, write $\xi=A(x)u+B(x)$ and $\phi=C(u)x+D(u)$. The second coefficient gives $2C'(u)=A''(x)u+B''(x)$, so $A''=a$, $B''=b$ are constants and $C(u)=au^2/4+bu/2+c$. The third coefficient then reads $(a/2)x+D''(u)=2ax+2a_1$, where $A'(x)=ax+a_1$. Hence $a=0$ and $D''=2a_1$. Integrating yields, with eight independent constants,

$$
\xi=a_0+b_1x+c_0u+d_0x^2+e_0xu,\qquad
\phi=f_0+g_0x+h_0u+d_0xu+e_0u^2.
$$

Conversely these coefficients satisfy all four equations, so every such field is a symmetry. Their span is precisely the eight fields of the plane in (7.2). Projective transformations send lines to lines, and on the graph-transverse chart this agrees with the determining calculation. Discrete point symmetries are not additional infinitesimal dimensions.

**Solution 3.** Put $a=f''/f'$ as a function of its argument and $b=y''/y'$. Then $L_{f\circ y}=a(y)y'+b$. Its derivative minus half its square is

$$
\big(a'(y)-\tfrac12a(y)^2\big)(y')^2
+a(y)y''-a(y)y'b+b'-\tfrac12b^2.
$$

The two mixed terms cancel, leaving $S(f)(y)(y')^2+S(y)$. For Möbius $f$, $a=-2c/(cy+d)$ and $a'=2c^2/(cy+d)^2$, so $S(f)=0$. This proves invariance. The group acts only on $y$ and its derivatives; $x$ is fixed and is an independent invariant. On $y'\ne0$, $\partial S/\partial y'''=1/y'$, so $x$ and $S$ are functionally independent. The normalization in (6.3) proves completeness.

**Solution 4.** At order zero the two-dimensional point space has orbit rank two. At order one, point and tangent determine a unique nearby rigid motion, so the three-dimensional jet space has rank three and no invariant. Higher prolongations project onto this action and therefore still have rank three, the full group dimension. Orders two and three have dimensions four and five, giving one and two invariants. Moving the point to zero and its tangent to the horizontal axis leaves exactly the normalized coordinates $q=\kappa$ and $r=D_s\kappa$. They are independent: $\partial\kappa/\partial q=(1+p^2)^{-3/2}\ne0$ and $\partial(D_s\kappa)/\partial r=(1+p^2)^{-2}\ne0$, while $\kappa$ has no $r$ dependence. Every invariant restricts to a function of those two coordinates on the local normalization section, proving completeness.

**Solution 5.** The inverse of $D_iX^j=\delta_i^j+tD_i\xi^j+O(t^2)$ changes differentiation to $\widetilde D_i=D_i-t(D_i\xi^j)D_j+O(t^2)$. Applying this to $u_J^\alpha+t\phi_J^\alpha$ gives the recurrence. For the empty index, $\phi^\alpha=Q^\alpha+\xi^iu_i^\alpha$. Assuming the characteristic expression at $J$, differentiate it, subtract $u_{J,j}^\alpha D_i\xi^j$, and cancel the two terms containing $D_i\xi^j$. Commutation of total derivatives gives the formula at $J,i$. The term $-\xi^iu_{J,i}^\alpha$ from differentiating the characteristic cancels its explicit positive counterpart, so the coefficient has order at most $|J|$. The inverse transversality matrix is what accounts for the subtraction in the recurrence; omitting it would differentiate at the old independent coordinates and would not be a prolongation of transformed graphs.

## References

- Michael Kunzinger, [*Lie Transformation Groups*](https://www.mat.univie.ac.at/~mike/teaching/ss15/ltg.pdf), §§3.8–3.12; in particular the prolongation construction, Theorem 3.10.6, the heat-equation example 3.11.1, and the local-solvability qualification in §3.12.
- Joël Merker, [*Four explicit formulas for the prolongations of an infinitesimal Lie symmetry and multivariate Faà di Bruno formulas*](https://arxiv.org/abs/math/0411650), §1, for arbitrary numbers of independent and dependent variables. The recurrence and characteristic proof above supply the full multi-index argument required here.
- Boris Kruglikov and Valentin Lychagin, [*Global Lie–Tresse theorem*](https://arxiv.org/abs/1111.5480), Theorems 1–2, for the finiteness statement with its precise regularity and algebraic hypotheses.
- Sophus Lie and Friedrich Engel, *Theorie der Transformationsgruppen*, Volume I, Chapters 26–27, for projective and linear homogeneous transformation groups; Volume II for differential equations and contact transformations.

This lesson proves its five main results locally on the specified regular domains. The Lie–Tresse theorem is cited without proof, as permitted; it is not used to replace any of those proofs.
