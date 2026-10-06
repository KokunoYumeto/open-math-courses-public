# Complete systems and invariants

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI), in Codex at Ultra. Public domain (CC0).*

An invariant is a function constant along the motions of a group. Infinitesimally this is a system of first-order equations. The number of independent equations is the dimension of a moving orbit, rather than the number of group parameters. We first solve the general regular system, then apply it to group invariants, invariant submanifolds, symmetries of complete systems, and integration of an ordinary differential equation.

We assume the analytic inverse-function theorem and use the flow and straightening results of One-parameter groups. We prove the regular Frobenius theorem in the form needed here. Basic references are [Kunzinger], [Lie–Engel I], and [Merker]. All assertions are local near a point where the indicated ranks are constant.

## 1. Why brackets create new equations

Let $X_1,\ldots,X_q$ be analytic vector fields with pointwise independent values on a neighbourhood in $\mathbb K^n$. Write $D$ for their pointwise span. The system

$$
X_1f=\cdots=X_qf=0
\tag{1.1}
$$

is **complete** if

$$
[X_i,X_j]=\sum_k c_{ij}^k(x)X_k
\tag{1.2}
$$

with analytic function coefficients. This is involutivity of the rank-$q$ distribution $D$. The coefficients in (1.2) need not be constant.

If $f$ solves (1.1), then $[X_i,X_j]f=0$ too. Thus any bracket outside $D$ adds a necessary equation.

**Example 1.1.** In three variables take $X=\partial_x+y\partial_z$, $Y=\partial_y$. Their bracket is $[X,Y]=-\partial_z$. A common solution must therefore satisfy $f_z=0$, then $f_y=0$ and $f_x=0$. Only constants remain. Counting three variables minus the two originally displayed equations would have given the wrong answer.

More generally, complete a finite system as follows. On a regular neighbourhood choose a basis for its pointwise span. If a bracket of basis fields increases the generic rank, adjoin it and restrict to a neighbourhood where the increased rank is constant. Repeat. The rank increases at most to $n$, so this process terminates after finitely many increases. At termination every bracket lies in the span; solving through a nonvanishing basis minor gives analytic coefficients in (1.2). At each stage the solution set is unchanged because the adjoined brackets kill every previous solution. This procedure concerns a regular neighbourhood; it makes no claim of one uniform basis across singular points.

## 2. Straightening a complete system

**Theorem 2.1 (Clebsch–Jacobi).** A complete rank-$q$ system in $n$ variables has $n-q$ independent analytic solutions $z_1,\ldots,z_{n-q}$ near each regular point. Every analytic solution is locally a function of these. There are coordinates $(t_1,\ldots,t_q,z_1,\ldots,z_{n-q})$ in which $D$ is spanned by $\partial_{t_1},\ldots,\partial_{t_q}$.

**Proof.** We induct on $q$. For $q=0$ the coordinates themselves suffice. For $q\ge1$, straighten a nonvanishing basis field to $\partial_t$ by the preceding lesson. Replace the remaining basis fields by subtracting their $\partial_t$ components. Call the resulting independent fields $Y_2,\ldots,Y_q$. They have only transverse $z$ components.

Involutivity and absence of a $\partial_t$ component give

$$
\partial_tY_a=\sum_{b=2}^q C_{ab}(t,z)Y_b.
$$

The coefficients are analytic, obtained by solving through a nonvanishing transverse basis minor. Regard $Y$ as a column of fields and solve the analytic matrix equation

$$
\partial_tP=-PC,\qquad P(0,z)=I.
$$

Analytic parameter dependence of ordinary differential equations gives $P(t,z)$; its determinant stays nonzero after shrinking. The fields $Z=PY$ satisfy $\partial_tZ=0$, so they depend only on transverse coordinates. They span the same transverse subspace as the $Y_a$.

Their brackets belong to $D$ by involutivity and have no $\partial_t$ component. Consequently their restrictions to the slice $t=0$ form a complete rank-$(q-1)$ distribution in $n-1$ variables. By induction, choose coordinates on this slice that straighten its distribution. Use those same coordinate functions on all $t$-slices. Together with $t$ they give the desired chart.

In this chart (1.1) is equivalent to $\partial_{t_i}f=0$ for all $i$. On a product neighbourhood every such function is $F(z_1,\ldots,z_{n-q})$. The $z_j$ have independent differentials and give the stated solutions. If additional independent solutions existed, their differentials would have to fit into the $(n-q)$-dimensional annihilator of $D$, which is impossible. $\square$

**Proposition 2.2 (the dual equations).** Suppose the coefficient rows of $X_1,\ldots,X_q$ form a rank-$q$ matrix $\Xi$. A tangent vector $v$ belongs to $D$ exactly when all $(q+1)$-row minors of the matrix obtained by adjoining $v$ to $\Xi$ vanish. Equivalently, every one-form annihilating $D$ vanishes on $v$.

**Proof.** The minors vanish exactly when adjoining $v$ does not increase the row rank, which is exactly membership in the row span. Solving through a nonzero $q$-minor gives a normalized frame, after reordering coordinates,

$$
Y_k=\partial_{x_{n-q+k}}+\sum_{i=1}^{n-q}\eta_{ki}(x)\partial_{x_i},
\qquad 1\le k\le q.
$$

The remaining $n-q$ equations for $v$ are

$$
v_i-\sum_{k=1}^q\eta_{ki}v_{n-q+k}=0.
$$

Thus the forms $\theta_i=dx_i-\sum_k\eta_{ki}dx_{n-q+k}$ annihilate the frame and are independent, so they form a basis of its annihilator. This proves the equivalence. For $q=0$ the equations are $v=0$; for $q=n$ the annihilator has dimension zero. $\square$

This is pointwise linear algebra and does not require involutivity. Theorem 2.1 supplies the additional integrability statement: in its product chart the integral leaves are $z=c$, and every analytic field in $D$ has a flow that keeps $z$ fixed. Any connected submanifold tangent to $D$ has constant $z$; if its dimension is $q$, it is locally an open part of one such leaf. The zero field has stationary point trajectories.

## 3. Invariants of a local group

Let a local group have generators $X_1,\ldots,X_r$. Define $\rho$ as their pointwise rank near a regular point. The distribution $D=\operatorname{span}\{X_j(x)\}$ has rank $\rho$, which may be less than $r$.

**Lemma 3.1.** The group preserves $D$, and $D$ is involutive on its regular neighbourhood.

**Proof.** Conjugating a small transformation by $T_a$ gives another small transformation: under the right-action convention,

$$
T_a\circ T_b\circ T_a^{-1}
=T_{m(m(\iota(a),b),a)}.
$$

Differentiating in $b$ at the identity shows that $(T_a)_*X_j$ is a constant linear combination of the generators. Conjugation is invertible, so it preserves their pointwise spans.

Each generator's flow belongs to the group by the preceding lesson. At a fixed point, transporting $X_j$ by the negative flow of $X_i$ gives a curve of vectors in the fixed subspace $D(x)$. Its derivative at time zero is $X_i,X_j$, as follows by differentiating the pushforward or by the coefficient formula for brackets. Hence this bracket lies in $D(x)$. A regular basis minor gives analytic coefficients, proving involutivity. $\square$

**Theorem 3.2.** An analytic function $f$ is locally invariant under the group if and only if $X_jf=0$ for all generators. There are $n-\rho$ independent invariants near a regular point, and every invariant is a function of them.

**Proof.** Differentiate invariance along each one-parameter subgroup to obtain $X_jf=0$. Conversely, along the flow of $X_j$, the derivative of $f$ is $X_jf$, so $f$ stays constant. Canonical product coordinates express every nearby group transformation as a finite product of these flows. Thus $f$ is group-invariant. Lemma 3.1 and Theorem 2.1 give the count and the functional-dependence assertion. $\square$

**Example 3.3 (rotations).** Away from the origin, the rotation fields on $\mathbb R^3$ span the plane perpendicular to $x$. Their rank is two. The function $r^2=x^2+y^2+z^2$ is invariant and has nonzero differential there, so every local invariant is a function of $r^2$. The origin is a singular orbit; the regular-rank assertion is not applied there.

**Example 3.4 (dilation and axial rotation).** Take

$$
A=x\partial_x+y\partial_y+z\partial_z,\qquad
B=y\partial_z-z\partial_y.
$$

Their bracket is zero. On $x\ne0$, $(y,z)\ne(0,0)$ they have rank two, and

$$
I=\frac{y^2+z^2}{x^2}
$$

is invariant with nonzero differential. Thus all local invariants on that region are functions of $I$. This statement also holds over $\mathbb C$ when $y^2+z^2=0$ but $(y,z)\ne(0,0)$: the differential remains nonzero. An invariant's value need not be nonzero for it to be an independent coordinate.

## 4. Invariant equations need regularity

Let

$$
S=\{x:\Omega_1(x)=\cdots=\Omega_m(x)=0\},
$$

and assume the differentials $d\Omega_1,\ldots,d\Omega_m$ are independent on $S$. Then $S$ is a regular analytic submanifold and

$$
T_xS=\bigcap_i\ker d\Omega_i(x).
$$

**Theorem 4.1.** The regular submanifold $S$ is locally invariant under the identity neighbourhood of the group if and only if

$$
X_j\Omega_i=0\quad\text{on }S
\quad\text{for all }i,j.
\tag{4.1}
$$

**Proof.** Invariance makes each generator curve through a point of $S$ stay in $S$. Differentiating its defining equations proves necessity. Conversely, (4.1) makes each $X_j$ tangent to $S$. Restricting a tangent analytic field to submanifold coordinates gives a flow in $S$. Viewed in the ambient manifold, it solves the same initial-value equation as the ambient flow, so uniqueness makes them agree. Each generator flow therefore preserves $S$ locally. Their finite products give all nearby group transformations, proving sufficiency. $\square$

If regularity is omitted, necessity remains true but sufficiency can fail. For $S=\{x:x^2=0\}$ in a real or complex line, $X=\partial_x$ satisfies $X(x^2)=2x=0$ on $S$, but its flow moves zero to $t$. The issue is the singular defining equation, not the set's underlying shape. Replacing it by the regular equation $x=0$ correctly detects failure of tangency.

For the unit sphere, $\Omega=x^2+y^2+z^2-1$ has nonzero differential on $S$ and every rotation field kills $\Omega$. The theorem verifies its invariance without solving the finite rotation equations.

### Tangency, saturation, and restriction

**Lemma 4.2 (the vanishing ideal).** For a regular analytic submanifold $S$, an analytic field $X$ is tangent to $S$ if and only if $XF$ vanishes on $S$ for every analytic function $F$ vanishing there. Tangent fields are closed under analytic function combinations and brackets.

**Proof.** If $X$ is tangent, its derivative of a function along $S$ is the derivative of that function's restriction. The restriction of $F$ is zero, so $XF$ vanishes on $S$. Conversely, applying the condition to regular local defining functions for $S$ gives tangency. For tangent $X,Y$ and $F$ vanishing on $S$, both $YF$ and $XF$ vanish there, so

$$
[X,Y]F=X(YF)-Y(XF)=0\quad\text{on }S.
$$

The same property holds for $aX+bY$, proving closure. $\square$

The regular defining equations also explain the coefficient condition often used in the historical argument. Choose coordinates $(u,v)$ with $S=\{u=0\}$. Every analytic function $G$ vanishing on $S$ can be written

$$
G(u,v)=\sum_i u_i R_i(u,v),\qquad
R_i(u,v)=\int_0^1\partial_{u_i}G(\tau u,v)\,d\tau.
$$

The $R_i$ are analytic, as follows by locally convergent power-series integration. Hence a tangent field satisfies $Xu=R(u,v)u$ with coefficients regular near $S$. Along its flow the defining functions solve a homogeneous linear ODE and remain zero by uniqueness. Coefficients with poles on $S$ would not supply this argument.

**Theorem 4.3 (relations among first integrals).** Let $D$ be complete of constant rank $q$ near $p$, and let $S$ be a regular analytic submanifold of dimension $m$ through $p$. Every field in $D$ is tangent to $S$ if and only if, in a sufficiently small Frobenius chart $(t,z)$,

$$
S=T\times N=\{(t,z):g_1(z)=\cdots=g_{n-m}(z)=0\},
$$

where $N$ is a regular analytic submanifold of the transverse coordinate space and the differentials $dg_i$ are independent on $N$. In particular $m\ge q$. Thus regular invariant submanifolds are locally relations among first integrals.

**Proof.** Tangency gives $D_p\subset T_pS$, so $q\le m$. Translate the $t$ coordinates so that $t(p)=0$. Since $D$ is spanned by the $t$ coordinate fields, $S$ is transverse to the slice $t=0$: its tangent space together with the slice tangent space spans the ambient tangent space. The inverse-function theorem therefore makes $N=S\cap\{t=0\}$ a regular submanifold of that slice, of dimension $m-q$.

Each $\partial_{t_i}$ is tangent to $S$. Its local flow is coordinate translation and preserves $S$ by the restriction-and-uniqueness argument of Theorem 4.1. After shrinking the chart, compositions of these translations carry a point of $S$ to the slice and carry slice points through a small product box. Consequently $S=T\times N$ locally. One may see the uniform shrinking directly by expressing $S$ as a graph over $t$ and $m-q$ transverse coordinates using a nonzero graph minor at $p$; tangency forces that graph to be independent of $t$. The inverse-function theorem gives the independent local equations $g_i$ for $N$.

Conversely, the equations $g_i(z)$ have zero derivative under every field in $D$. Their regular zero set is therefore tangent to $D$ and preserved by its local flows. $\square$

**Theorem 4.4 (restriction through a rank drop).** Let $S$ be a regular invariant analytic submanifold of dimension $m$. Suppose analytic ambient fields $X_1,\ldots,X_r$ are tangent to $S$ and satisfy

$$
[X_i,X_j]=\sum_k c_{ij}^kX_k
$$

with coefficients analytic near $S$. Their restricted fields $\overline X_i$ preserve brackets. On a neighbourhood in $S$ where their span has constant rank $h$, they form a complete rank-$h$ system. There are $m-h$ independent local first integrals on $S$, and its regular invariant submanifolds are relations among these. Necessarily $h\le m$.

**Proof.** Write $i:S\hookrightarrow M$ for inclusion. Tangency defines $\overline X$ intrinsically, and for every ambient analytic $F$,

$$
\overline X(i^*F)=i^*(XF).
$$

Every local analytic function on $S$ extends to the ambient graph coordinates. Applying the displayed identity twice and subtracting proves

$$
[\overline X_i,\overline X_j]
=\overline{[X_i,X_j]}
=\sum_k(i^*c_{ij}^k)\overline X_k.
$$

Choose $h$ restricted fields with a nonzero basis minor. Constant rank and solving through that minor express every remaining field as an analytic combination of this frame. Its brackets lie in the span by the displayed identity and the product rule. Theorem 2.1 applied in coordinates on $S$ gives the $m-h$ first integrals; Theorem 4.3 applied within $S$ gives the invariant-submanifold assertion. The dimension bound follows from their values lying in $T S$. If $h=0$, every restricted field vanishes: its flow fixes each point of $S$, and every local analytic function on $S$ is a first integral. $\square$

**Example 4.5.** On the plane take $X=\partial_x$ and $Y=x\partial_y$. The rank is two off $x=0$ and one on $x=0$. Although $[X,Y]=(1/x)Y$ on $x\ne0$, the coefficient has a pole at the rank-drop set. That set is not invariant, since the flow of $X$ moves it. Rank determinants locate rank drops; they do not by themselves prove invariance. To use Theorem 4.4 one first verifies a regular invariant submanifold, regular bracket coefficients there, and a constant restricted rank. A mixture of fixed and moving points need not admit one uniform chart.

## 5. Symmetries of a complete system

A local diffeomorphism $T$ **preserves a distribution** if $dT_x(D_x)=D_{T(x)}$ wherever it is defined. This condition does not require preservation of a chosen frame. In the regular complete case, it says that $T$ takes leaves to leaves.

**Lemma 5.1.** A local diffeomorphism preserves a complete regular distribution $D$ if and only if the pullback of every local first integral is a first integral. In compatible Frobenius charts its form is

$$
T(t,z)=(A(t,z),B(z)).
$$

**Proof.** If $T$ preserves $D$ and $df$ annihilates $D$, the chain rule shows that $d(f\circ T)$ annihilates $D$. Conversely, it suffices to apply the pullback condition to the target chart's first-integral coordinates. It gives $\partial_{t_i}(z\circ T)=0$, hence the displayed form on a product neighbourhood. The derivative of $T$ then sends the $t$ subspace into the target $t$ subspace. These subspaces have equal dimension, and $dT$ is invertible, so the inclusion is equality. The block triangular derivative also shows that $B$ is a local diffeomorphism of the transverse coordinates. $\square$

**Theorem 5.2 (the infinitesimal symmetry criterion).** Let $X_1,\ldots,X_q$ be a frame for a complete regular distribution $D$, and let $Y$ be analytic. The following are equivalent:

1. The local flow of $Y$ preserves $D$.
2. $[Y,X_i]$ belongs to $D$ for every $i$.
3. In a Frobenius chart,
   $$
   Y=\sum_i a_i(t,z)\partial_{t_i}+\sum_j b_j(z)\partial_{z_j}.
   $$

The induced motion of the first-integral coordinates is the convergent local ODE $\dot z=b(z)$. The flow fixes each local leaf if and only if $b=0$, equivalently $Y$ belongs to $D$.

**Proof.** The bracket condition for a frame is equivalent to $[Y,W]\in D$ for every analytic section $W$ of $D$, since $[Y,cW]=(Yc)W+c[Y,W]$. In a Frobenius chart write $Y=a(t,z)\partial_t+b(t,z)\partial_z$. Then

$$
[Y,\partial_{t_i}]
=-\sum_k\partial_{t_i}a_k\,\partial_{t_k}
 -\sum_j\partial_{t_i}b_j\,\partial_{z_j}.
$$

Membership in $D$ is exactly $\partial_{t_i}b_j=0$. This proves the equivalence of 2 and 3.

Under 3, analytic ODE existence and uniqueness give a transverse flow $z(s)=\psi_s(z_0)$ independent of $t_0$. The full flow therefore has the form $(t,z)\mapsto(A_s(t,z),\psi_s(z))$ and preserves $D$ by Lemma 5.1. The inverse flow supplies equality on compatible local domains. Conversely, if the full flow preserves $D$, its transverse coordinates are independent of $t$ by Lemma 5.1. Differentiating at $s=0$ gives 3. Finally, all leaf labels stay fixed exactly when $\psi_s(z)=z$ for all sufficiently small $s$, which is equivalent to $b=0$. $\square$

For example, with $D=\operatorname{span}\{\partial_t\}$, the field $Y=z\partial_z$ is a symmetry. It sends the leaf $z=c$ to $z=e^sc$; it preserves the family without fixing every member. Fields in $D$, including fields with variable coefficients, fix all first-integral coordinates.

**Proposition 5.3 (brackets of symmetries).** The analytic fields normalizing $D$, meaning $[Y,W]\in D$ for every section $W$ of $D$, are closed under brackets. The sections of $D$ are themselves normalizers and form an ideal within this algebra of fields.

**Proof.** Involutivity proves that sections of $D$ normalize it. If $Y,Z$ normalize it, then for $W\in D$ the Jacobi identity gives

$$
[[Y,Z],W]=[Y,[Z,W]]-[Z,[Y,W]]\in D.
$$

The identity follows by expanding the brackets as commutators of derivations: the six triple compositions cancel in pairs. This proves bracket closure. The ideal assertion is precisely the defining relation $[Y,W]\in D$. $\square$

**Proposition 5.4 (common distributions).** Let $D,E$ be analytic complete distributions of constant rank, and let $Y$ normalize both.

If $D\cap E$ has constant rank on the chosen neighbourhood, it is complete and $Y$ normalizes it. Its local leaves are the regular intersections of a $D$-leaf and an $E$-leaf. If the involutive completion $C$ of $D+E$ has constant rank on a regular neighbourhood as in Section 1, $Y$ normalizes $C$. The first integrals of $C$ are exactly the functions that are first integrals of both $D$ and $E$.

**Proof.** Constant intersection rank gives an analytic frame for $D\cap E$: use a nonzero matrix minor to solve the linear equations equating combinations of frames for $D$ and $E$. For sections $U,V$ of the intersection, $[U,V]$ belongs to both distributions by their involutivity; likewise $[Y,U]$ belongs to both. This proves completeness and normalization. If $z,w$ are first-integral coordinates for $D,E$, then the kernel of $d(z,w)$ is $D\cap E$. Its rank is constant, so the inverse-function theorem makes its local level sets regular submanifolds with that tangent space. These level sets are exactly the local intersections of the two leaves.

For the completed sum, generate fields by the original frames, brackets and analytic combinations. Normalization of the original frames starts an induction. The product rule and

$$
[Y,[U,V]]=[[Y,U],V]+[U,[Y,V]]
$$

show that $[Y,\cdot]$ preserves the resulting module. A nonzero regular basis minor expresses its fields with analytic coefficients, so $Y$ normalizes $C$. A function killed by $D$ and $E$ is killed by all their combinations and brackets; conversely $D,E\subset C$. This proves the assertion about first integrals. $\square$

These results use regular neighbourhoods for the intersection and completion. An arbitrary singular intersection or rank-drop set is not assigned a regular leaf space by this argument.

## 6. An integrating factor from a symmetry

Consider

$$
\frac{dy}{dx}=F(x,y),\qquad
V=\partial_x+F\partial_y,\qquad \alpha=dy-Fdx.
$$

A vector field $X=\xi\partial_x+\eta\partial_y$ is a local symmetry of the equation's direction field if $[X,V]=hV$ for an analytic function $h$. Computing components gives the equivalent condition

$$
V\eta-FV\xi-XF=0,
\qquad h=-V\xi.
\tag{6.1}
$$

**Theorem 6.1 (Lie's integrating factor).** If (6.1) holds and $A=\xi F-\eta\ne0$, then

$$
\beta=\frac{dy-Fdx}{\xi F-\eta}
\tag{6.2}
$$

is closed and locally exact. Its potential is a first integral of the differential equation.

**Proof.** The fields $X,V$ are independent because their determinant is $A$. The form $\beta$ satisfies $\beta(V)=0$ and $\beta(X)=-1$. By the formula for the exterior derivative,

$$
d\beta(X,V)=X(\beta(V))-V(\beta(X))-\beta([X,V])=0.
$$

An alternating two-form in two dimensions is determined by its value on an independent pair, so $d\beta=0$. To see local exactness explicitly, write $\beta=Pdx+Qdy$ on a small rectangle. The condition is $Q_x=P_y$. Then

$$
H(x,y)=\int_{x_0}^xP(s,y_0)\,ds+\int_{y_0}^yQ(x,u)\,du
$$

satisfies $H_y=Q$ and $H_x=P(x,y_0)+\int_{y_0}^yQ_x(x,u)du=P(x,y)$. Hence $dH=\beta$ and $VH=0$. Complex integrals on a small product disc give the same analytic construction. $\square$

The opposite sign also gives an integrating factor, with potential $-H$. Formula (6.2) fixes the sign used here. The condition $A\ne0$ means that the symmetry is transverse to the equation's trajectories. A symmetry tangent to them does not yield this particular factor.

**Example 6.2.** On $x\ne0$, consider $y'=y/x+x$. Its weighted dilation symmetry is $X=x\partial_x+2y\partial_y$. Equation (6.1) holds: $V\eta=2F$, $V\xi=1$, and $XF=F$. Here $A=x^2-y$. Setting $I=y/x-x$ gives $dI=\alpha/x$, hence on $I\ne0$

$$
\beta=-\frac{dI}{I}.
$$

A local logarithm gives $H=-\log I$; over a real region use $-\log|I|$. The solution family is $y=x^2+Cx$. The solution $C=0$ lies on the excluded set $A=0$ and is recovered directly from the original equation.

**Theorem 6.3 (reduction to a quadrature).** Suppose a nonvanishing analytic direction field $V$ in two variables has a symmetry $X$ with $[X,V]\in\operatorname{span}\{V\}$, and $X,V$ are independent at the point considered. There are local analytic coordinates $(s,r)$ in which its solution curves satisfy

$$
\frac{ds}{dr}=g(r),\qquad
s-\int_{r_0}^{r}g(u)\,du=C.
$$

**Proof.** Straighten $X$ to $\partial_s$ by Lesson 3, with $r$ its transverse coordinate. Independence gives $a=Vr\ne0$, so normalize the direction field to

$$
W=a^{-1}V=\partial_r+g(s,r)\partial_s.
$$

The product rule and the symmetry hypothesis make $[\partial_s,W]$ a multiple of $W$. Its $r$ component is zero, so that multiple is zero. Its remaining component is $\partial_sg$, proving that $g$ depends only on $r$. Along a solution curve $r$ is a valid local parameter because $Vr\ne0$. The displayed primitive then follows by integration, and its differential has $s$ component one, so it is an independent first integral. $\square$

The coordinate construction and the quadrature are local. This proves a first-order reduction on the transverse region; tangent symmetries and singular points require separate treatment. The integrating factor above constructs a first integral directly in the original coordinates on the same transverse region.

## 7. Exercises

**Exercise 1 (introductory).** Find all local invariants of $x\partial_x+y\partial_y$ on a chart with $x\ne0$. Explain the change of chart needed when $x=0$, $y\ne0$.

**Exercise 2 (intermediate).** Complete the system in Example 1.1 and determine every analytic common solution.

**Exercise 3 (intermediate).** Apply Theorem 4.1 to the unit sphere and to the singular defining equation $(x^2+y^2+z^2-1)^2=0$. Explain what the singular equation can and cannot establish for a general field.

**Exercise 4 (intermediate).** Integrate a homogeneous equation $y'=F(y/x)$ by the dilation symmetry. Include the straight-line solutions excluded by the integrating factor.

**Exercise 5 (advanced).** In the induction proof of Theorem 2.1, verify both the invertibility of $P$ and the involutivity of the transverse fields $Z_a$. Explain why the coefficients in (1.2) may depend on position.

## 8. Solutions

**Solution 1.** On $x\ne0$, $v=y/x$ is invariant and $dv\ne0$. The field has rank one, so Theorem 3.2 says every local invariant is $H(v)$. Near $x=0$, $y\ne0$, use $u=x/y$ instead. These are local coordinate assertions, not a single global quotient coordinate on the punctured plane.

**Solution 2.** Adjoin $[X,Y]=-\partial_z$. The three fields span all tangent directions: $\partial_z$ is present, $\partial_y=Y$, and $\partial_x=X-y\partial_z$. The completed system has rank three, hence zero independent nonconstant solutions. Directly, $f_z=f_y=f_x=0$ makes $f$ constant on a connected neighbourhood.

**Solution 3.** Each rotation field kills $\Omega=x^2+y^2+z^2-1$, and $d\Omega$ has rank one on the sphere, proving invariance. For $\Omega^2$, every field $X$ satisfies $X(\Omega^2)=2\Omega X\Omega=0$ on the sphere, even a radial field that moves it. Thus the singular defining equation supplies a necessary condition that is not sufficient. The underlying sphere still has a regular equation, and that equation must be used for the equivalence.

**Solution 4.** The symmetry is $X=x\partial_x+y\partial_y$. Set $v=y/x$ on $x\ne0$. Then $\alpha=x\,dv+(v-F(v))dx$ and $A=x(F(v)-v)$. Where $F(v)\ne v$,

$$
\beta=\frac{dv}{F(v)-v}-\frac{dx}{x},\qquad
H=\int^v\frac{ds}{F(s)-s}-\log x.
$$

Choose a local complex logarithm, or $\log|x|$ over a real chart. The level sets of $H$ are solutions. For every root $v_0$ of $F(v_0)=v_0$, the line $y=v_0x$ satisfies the original equation and must be added separately. If $F(v)=v$ identically on an interval, every such line is a solution and the integrating factor has no transverse region there; direct substitution handles this case.

**Solution 5.** The determinant starts at one, so continuity keeps $P$ invertible near the initial slice; alternatively its derivative is $-(\operatorname{tr}C)\det P$. Since $Z=PY$ with analytic coefficients, the product rule expresses $[Z_a,Z_b]$ as combinations of the $Y_c$ and their brackets. All lie in $D$. As $Z_a$ have no $\partial_t$ component, neither does their bracket, so it lies in the transverse span of $Z_2,\ldots,Z_q$. Also $\partial_tZ=0$, so this is an involutive distribution on the slice. Position-dependent coefficients are necessary: changing a distribution's frame by a nonconstant invertible matrix introduces derivatives of that matrix into its brackets, even when a previous frame commuted.

## What this lesson assumes

The analytic inverse-function theorem is assumed. Analytic flow existence and straightening were proved in the preceding lesson. The regular complete-system theorem, dual equations, invariant count, invariant-submanifold criterion and saturation, restriction through a rank drop, complete-system symmetry criterion, closure of symmetries, regular common distributions, integrating factor, and transverse reduction to quadrature are proved here. The constant-rank and graph consequences used above follow from the assumed analytic inverse-function theorem by solving through the indicated nonzero minors. Singular distributions, singular quotient spaces, and global first-integral coordinates are outside these local regular statements.

## References

- Michael Kunzinger, *Lie Transformation Groups: An Introduction to Symmetry Group Analysis of Differential Equations*, 2015, corrected December 2024, Sections 3.2, 3.3, and 3.13. [Author's text](https://www.mat.univie.ac.at/~mike/teaching/ss15/ltg.pdf).
- Sophus Lie, with Friedrich Engel, *Theorie der Transformationsgruppen*, Volume I, 1888, Chapters 5–8.
- Joël Merker, *Theory of Transformation Groups, by S. Lie and F. Engel (Vol. I, 1888): Modern Presentation and English Translation*, 2010, complete corresponding Chapters 5–8, on complete systems, invariants, invariant equations, and symmetries of complete systems. Consulted for source comparison; the proofs and historical English translations here are independently written. [Author's preprint](https://arxiv.org/abs/1003.3202).

