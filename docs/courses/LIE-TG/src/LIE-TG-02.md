# The fundamental differential equations

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI), in Codex at Ultra. Public domain (CC0).*

A small change in a group parameter moves every point by the same infinitesimal transformation, evaluated at that point's current position. This is stronger than merely saying that each transformation is differentiable. It separates the dependence on parameters from the dependence on position and is the first step from a transformation group to its Lie algebra.

We use the definitions and finite-jet parameter test in Transformation groups and their parameters. We assume analytic differentiation and the inverse-function theorem. Basic references are [Lie–Engel I], [Merker], and [Kunzinger]. Throughout, composition is the right-action convention

$$
f(f(x,a),b)=f(x,m(a,b)).
\tag{1.1}
$$

The identity has parameter $0$ in the coordinates used in the general proof. A concrete example may have another identity parameter.

## 1. A tangent vector at the identity becomes a vector field

Let $a=(a_1,\ldots,a_r)$ be coordinates on the parameter group near its identity. Define

$$
\xi_j^i(x)=\left.\frac{\partial f_i(x,b)}{\partial b_j}\right|_{b=0},
\qquad
X_j=\sum_{i=1}^n\xi_j^i(x)\partial_{x_i}.
\tag{1.2}
$$

Thus a parameter curve $b(t)$ through zero with initial velocity $v$ moves $x$ with initial velocity $\sum_jv_jX_j(x)$. A tangent vector at the identity defines a vector field on the whole coordinate neighbourhood of $M$.

The fields can be pointwise dependent. Three rotation fields on $\mathbb R^3$ span only a two-dimensional tangent plane away from zero. Essentiality asks whether a constant combination is the zero field on an open set; it does not ask whether their values at one point are independent.

## 2. Moving the parameter origin

Define a parameter-space vector field $B_j$ by

$$
B_j(a)=\left.\frac{\partial m(a,b)}{\partial b_j}\right|_{b=0}
=\sum_{k=1}^r B^k_j(a)\partial_{a_k}.
\tag{2.1}
$$

For fixed $a$, multiplication $b\mapsto m(a,b)$ is locally invertible: its inverse is multiplication by $\iota(a)$ on the same side, with domains restricted as needed. Therefore the matrix $B(a)=(B^k_j(a))_{k,j}$ is invertible. At the identity it is the identity matrix.

**Theorem 2.1 (first fundamental theorem).** An analytic local action satisfies

$$
\frac{\partial f_i}{\partial a_k}(x,a)
=\sum_{j=1}^r\psi_{kj}(a)\xi_j^i(f(x,a)),
\qquad
\psi_{kj}(a)=(B(a)^{-1})^j_k.
\tag{2.2}
$$

In particular, $\psi$ is analytic and invertible. Its rows are indexed by the differentiating parameter $a_k$; its columns are indexed by the field $X_j$.

**Proof.** Differentiate (1.1) with respect to $b_j$ at $b=0$. The left side gives $\xi_j^i(f(x,a))$. The right side gives

$$
\sum_k\frac{\partial f_i}{\partial a_k}(x,a)B^k_j(a).
\tag{2.3}
$$

For each $i$, solve this matrix equation by multiplying by $B^{-1}$. The result is (2.2). Analyticity and invertibility follow from (2.1). $\square$

Equation (2.3) has a geometric meaning. The derivative of the orbit map $a\mapsto f(x,a)$ carries $B_j(a)$ to $X_j(f(x,a))$. Every parameter-space velocity can be expressed in the frame $B_1,\ldots,B_r$, which explains why the coefficients in (2.2) depend only on $a$.

## 3. Which tangent directions act trivially?

**Theorem 3.1.** The fields $X_1,\ldots,X_r$ are independent over $\mathbb K$ if and only if the transformation family has $r$ essential local parameters. This is independence with constant coefficients.

**Proof.** Suppose $\sum_jv_jX_j=0$ for a nonzero constant vector $v$. Set $\chi(a)=\sum_jv_jB_j(a)$. It is a nonzero analytic parameter-space vector field, since the $B_j$ form a frame. Equation (2.3) gives $\chi(f_i(x,a))=0$ for every $i$ and every $x$. The infinitesimal parameter test in the preceding lesson shows that the family can be reduced to fewer parameters on a regular neighbourhood.

Conversely, suppose the family has fewer than $r$ essential parameters. That test supplies a nonzero analytic field $\chi=\sum_k\chi_k(a)\partial_{a_k}$ killing $f$. Write $\chi=\sum_jv_j(a)B_j$. At a parameter value $a_*$ where $\chi\ne0$, the constant numbers $v_j(a_*)$ are not all zero. Equation (2.3) implies

$$
\sum_jv_j(a_*)X_j(f(x,a_*))=0
$$

on an open set. Since $f(\cdot,a_*)$ is a local diffeomorphism, this is a constant linear dependence of the $X_j$ on its open image. Analytic continuation extends it throughout the connected coordinate neighbourhood where these fields are defined. Hence the fields are dependent. $\square$

There is also a direct rank interpretation. At any parameter value, (2.2) identifies parameter derivatives of the transformation germ with an invertible change of basis of the fields $X_j$, followed by evaluation at $f(x,a)$. Thus the finite-jet rank of a local action is constant near its identity. The critical-parameter phenomenon of $x\mapsto x+ab$ disappears once the effective local group has been given regular coordinates.

An action is **infinitesimally effective** if the linear map

$$
T_eG\longrightarrow\{\text{analytic vector fields on }M\},
\qquad v\longmapsto X_v,
$$

is injective. Theorem 3.1 identifies this with essentiality of the parameters. This is a local assertion; a global action can still have a discrete kernel.

## 4. The generator space is intrinsic

Let $u$ be other analytic parameter coordinates, with $a=a(u)$ and identity $u=0$. The new generators are

$$
Y_\ell=\sum_j\left.\frac{\partial a_j}{\partial u_\ell}\right|_{u=0}X_j.
\tag{4.1}
$$

The coefficient matrix is constant and invertible. Therefore the vector space

$$
\mathfrak g_M=\operatorname{span}_{\mathbb K}\{X_1,\ldots,X_r\}
$$

does not depend on parameter coordinates.

If $y=H(x)$ is an analytic change of coordinates on $M$, its transformed action is $H\circ T_a\circ H^{-1}$. Differentiating at the identity gives

$$
\widetilde X_j(H(x))=DH(x)X_j(x),
\tag{4.2}
$$

which is exactly the pushforward of a vector field. Equations (4.1) and (4.2) prove the invariance of the generator space and specify how its representatives change.

For a check on the full differential equations, parameter reparametrization changes $\partial_{a_k}$ by the parameter Jacobian, while (4.1) changes the generator basis by the Jacobian **at the identity**. These two matrices occur at different points and must not be conflated. Applying both changes to (2.2) gives the same equation in the new coordinates.

## 5. Computations

**Example 5.1 (the affine line).** For $x'=\alpha x+\beta$, the identity is $(1,0)$. Differentiating there gives

$$
X_1=x\partial_x,\qquad X_2=\partial_x.
$$

The product from the preceding lesson gives

$$
B(\alpha,\beta)=\begin{pmatrix}\alpha&0\\\beta&1\end{pmatrix},
\qquad
\psi(\alpha,\beta)=\begin{pmatrix}\alpha^{-1}&-\beta/\alpha\\0&1\end{pmatrix}.
$$

Indeed,

$$
\partial_\alpha x'=x=\alpha^{-1}x'-\beta/\alpha,
\qquad \partial_\beta x'=1.
$$

This checks the index order in (2.2).

**Example 5.2 (the projective line).** Use $x'=(\alpha x+\beta)/(\gamma x+1)$ near the identity. The parameter derivatives there give $x\partial_x$, $\partial_x$, and $-x^2\partial_x$. Replacing the last parameter by its negative gives the basis

$$
\partial_x,\quad x\partial_x,\quad x^2\partial_x.
$$

These three fields are independent over constants on every open interval or disc, though their values are always collinear at each point. The family therefore has three essential parameters.

**Example 5.3 (three-dimensional rotations).** A skew matrix $A$ gives a curve $R(t)=\exp(tA)$ through the identity, with velocity field $X_A(x)=Ax$. Rotations about the three coordinate axes give

$$
X_1=y\partial_z-z\partial_y,\quad
X_2=z\partial_x-x\partial_z,\quad
X_3=x\partial_y-y\partial_x.
$$

If $c_1X_1+c_2X_2+c_3X_3=0$ as a field, its skew matrix is zero, so each $c_i=0$. At a nonzero point their values span the plane perpendicular to $x$. At zero they all vanish. Essential parameter dimension is three in all these cases; orbit dimension is a different quantity.

**Example 5.4 (fundamental form without a group).** For $0<|a|<1$, let $x'=ax$. Then

$$
\partial_a x'=a^{-1}x',\qquad X=x\partial_x.
$$

This has the separated form (2.2), with an invertible coefficient $1/a$, but its given parameter domain has no identity. Fundamental-form equations alone do not imply that the given family contains an identity. The converse theorem later in the course must include an identity normalization or replace the family by its relative transformations.

## 6. Exercises

**Exercise 1 (introductory).** Use parameters $s=\log\alpha$, $\beta$ in the real identity component of the affine group. Compute the generators and $\psi$, and compare with Example 5.1.

**Exercise 2 (intermediate).** Choose three one-parameter matrix curves that yield $\partial_x$, $x\partial_x$, and $x^2\partial_x$ in the projective line action. Compute their finite transformations.

**Exercise 3 (intermediate).** For $1\le i<j\le3$, derive $x_i\partial_{x_j}-x_j\partial_{x_i}$ by differentiating a coordinate-plane rotation. Determine the kernel of their evaluation map at $(1,0,0)$.

**Exercise 4 (intermediate).** Let $a=C u+O(|u|^2)$, where $C$ is invertible. Prove that the new generators are the columns of $C$ applied to the old basis. Explain why nonlinear terms do not affect this conclusion.

**Exercise 5 (advanced).** Complete the converse direction of Theorem 3.1 without assuming that an inessential parameter direction is nonzero at the identity. Explain why choosing a regular value $a_*$ is legitimate.

## 7. Solutions

**Solution 1.** The transformation is $x'=e^s x+\beta$, with identity $(0,0)$. The generators remain $x\partial_x$ and $\partial_x$. Its derivatives are $\partial_sx'=x'-\beta$ and $\partial_\beta x'=1$, so

$$
\psi(s,\beta)=\begin{pmatrix}1&-\beta\\0&1\end{pmatrix}.
$$

The first row of Example 5.1 is multiplied by $\partial\alpha/\partial s=\alpha$, exactly as the chain rule requires.

**Solution 2.** The curves

$$
\begin{pmatrix}1&t\\0&1\end{pmatrix},\qquad
\begin{pmatrix}e^t&0\\0&1\end{pmatrix},\qquad
\begin{pmatrix}1&0\\-t&1\end{pmatrix}
$$

give respectively $x+t$, $e^t x$, and $x/(1-tx)$. Differentiation at zero gives the stated fields. The last transformation is defined only where $1-tx\ne0$; for a local action take $t$ and $x$ in a suitable product neighbourhood.

**Solution 3.** Rotate the $(x_i,x_j)$ coordinates by $\bigl(\begin{smallmatrix}\cos t&-\sin t\\\sin t&\cos t\end{smallmatrix}\bigr)$. The velocities are $\dot x_i=-x_j$, $\dot x_j=x_i$, giving the stated field. At $(1,0,0)$ the fields for pairs $(1,2)$ and $(1,3)$ give $\partial_{x_2}$ and $\partial_{x_3}$; the field for $(2,3)$ gives zero. The evaluation kernel is its one-dimensional span, the infinitesimal rotation about the first axis.

**Solution 4.** Differentiate $f(x,a(u))$ at $u=0$. The chain rule gives $Y_\ell=\sum_jC_{j\ell}X_j$. Terms of order two or higher have zero derivative at zero. Since $C$ is invertible, this is a change of basis, proving equality of the generator spans.

**Solution 5.** Inessentiality gives an analytic field $\chi$ killing $f$ on a regular parameter neighbourhood by the finite-jet reduction theorem. It may vanish at the identity; choose any $a_*$ at which it does not vanish. Since $B(a_*)$ is invertible, the numbers $v_j(a_*)$ in $\chi(a_*)=\sum_jv_j(a_*)B_j(a_*)$ are not all zero. Equation (2.3) gives a constant combination of $X_j$ vanishing on the open image of $f(\cdot,a_*)$. Analytic continuation gives the same identity near the original base point. This is the required constant dependence. The proof uses no assumption about $\chi(0)$.

## What this lesson does not prove

The converse construction of a local group from bracket-closed fields is proved in The second fundamental theorem and the group of parameters. The convergence and existence assertions for analytic flows are treated in One-parameter groups. Neither converse is needed to derive (2.2).

## References

- Michael Kunzinger, *Lie Transformation Groups: An Introduction to Symmetry Group Analysis of Differential Equations*, 2015, corrected December 2024, Section 3.1. [Author's text](https://www.mat.univie.ac.at/~mike/teaching/ss15/ltg.pdf).
- Sophus Lie, with Friedrich Engel, *Theorie der Transformationsgruppen*, Volume I, 1888, Chapter 2, first fundamental theorem.
- Joël Merker, *Theory of Transformation Groups, by S. Lie and F. Engel (Vol. I, 1888): Modern Presentation and English Translation*, 2010, chapter on fundamental differential equations. [Author's preprint](https://arxiv.org/abs/1003.3202).

