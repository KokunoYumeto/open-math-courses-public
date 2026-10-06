# Given unitary cocycles for arbitrary locally compact groups

*Original proof exposition: GPT-6.1 Sol (OpenAI), Ultra, 2026-10-04. CC0-1.0 to the extent of rights held.*

Let $G$ be a locally compact Hausdorff group, written multiplicatively, with identity $e$. Let $M\subseteq B(H)$ be an arbitrary von Neumann algebra; $H$ need not be separable and $M$ need not be a factor or admit a faithful normal state. An action means normal unital $*$-automorphisms $\alpha_g$, with $\alpha_e=\mathrm{id}$, $\alpha_g\alpha_h=\alpha_{gh}$, and pointwise $\sigma$-strong* continuity. Normal means ultraweak continuity here. The concrete and intrinsic bounded-set topology identifications are proved in [CP1–6](OA-FLOW-CP.md#oa-flow.cp.1) and ST2. The norm-series, involution and continuous-calculus inputs are the full local proofs in CF1, CF3 and CF6–8. All algebraic assertions below also hold for an abstract group when the continuity clauses are omitted.

<a id="oa-flow.uc.0"></a>

## UC0. Topology checks used in every construction

A $*$-automorphism is isometric: CF6 proves contractivity of unital $*$-homomorphisms, and applying it to the inverse gives equality. Multiplication on uniformly bounded subsets of $B(H)$ is jointly strong* continuous. Indeed, if $x_i\to x$ and $y_i\to y$ strongly*, with $\sup_i\|x_i\|\le C$, then

<a id="equation-uc1"></a>

\[
 \|(x_i y_i-xy)\xi\|
 \le C\|(y_i-y)\xi\|+\|(x_i-x)y\xi\|\longrightarrow0.
 \tag{UC1}
\]
Apply the same estimate to $y_i^*x_i^*$ for adjoints. Involution is strong* continuous by its definition. Multiplication by a fixed bounded operator is also ultraweakly continuous: in a CP4 vector-series test, multiplying on the left replaces $\eta_n$ by $a^*\eta_n$, and multiplying on the right replaces $\xi_n$ by $a\xi_n$; the new sequences are square summable. Involution is conjugate-ultraweakly continuous by interchanging the two vector sequences and taking a complex conjugate.

On the unitary group the strong and strong* topologies agree. If $u_i\to u$ strongly and $u_i,u$ are unitary, then

<a id="equation-uc2"></a>

\[
 \|(u_i^*-u^*)\xi\|=\|(u-u_i)u^*\xi\|\longrightarrow0.
 \tag{UC2}
\]
Ultraweak convergence of unitaries to a unitary gives strong convergence, since

<a id="equation-uc3"></a>

\[
 \|(u_i-u)\xi\|^2
 =2\|\xi\|^2-2\operatorname{Re}\langle u_i\xi,u\xi\rangle\longrightarrow0.
 \tag{UC3}
\]
Conversely bounded strong convergence gives ultraweak convergence: the finite initial part of each CP4 vector series converges, and Cauchy–Schwarz makes its complementary tail uniformly small. Thus requiring strong* continuity of a unitary-valued map is equivalent to requiring its ultraweak continuity. ST2 proves that these bounded-set statements are independent of the chosen faithful normal concrete representation. For a normal isomorphism $\pi$, this can also be seen directly: every positive normal functional on its target pulls back to a positive normal functional, so $f(\pi(z)^*\pi(z))=(f\circ\pi)(z^*z)$; use the inverse for the converse.

<a id="oa-flow.uc.1"></a>

## UC1. Perturbation and inverse

A given unitary $\alpha$-cocycle is a strong* continuous map $u:G\to\mathcal U(M)$ satisfying

<a id="equation-uc4"></a>

\[
 u_{gh}=u_g\alpha_g(u_h)\qquad(g,h\in G).
 \tag{UC4}
\]
This is a definition of an already supplied cocycle; it asserts no existence for an arbitrary family of outer automorphisms. At $g=h=e$, (UC4) gives $u_e=u_e^2$, hence $u_e=1$. At $(g,g^{-1})$ it gives

<a id="equation-uc5"></a>

\[
 u_{g^{-1}}=\alpha_{g^{-1}}(u_g^*).
 \tag{UC5}
\]
Define $\beta_g=\operatorname{Ad}(u_g)\alpha_g$. Each $\beta_g$ is a normal automorphism by UC0. The cocycle law gives, for every $x\in M$,

<a id="equation-uc6"></a>

\[
 \begin{aligned}
 \beta_g\beta_h(x)
 &=u_g\alpha_g(u_h)\alpha_{gh}(x)\alpha_g(u_h^*)u_g^*\\
 &=u_{gh}\alpha_{gh}(x)u_{gh}^*=\beta_{gh}(x).
 \end{aligned}
 \tag{UC6}
\]
For fixed $x$, both $g\mapsto u_g$ and $g\mapsto\alpha_g(x)$ are strong* continuous and bounded; (UC1) proves the required continuity of $\beta$. Its inverse at $g$ is consequently $\beta_{g^{-1}}$.

The map $r_g=u_g^*$ is a cocycle for the perturbed action $\beta$, because

<a id="equation-uc7"></a>

\[
 r_g\beta_g(r_h)
 =u_g^*u_g\alpha_g(u_h^*)u_g^*
 =\alpha_g(u_h^*)u_g^*=u_{gh}^*=r_{gh}.
 \tag{UC7}
\]
Moreover $\operatorname{Ad}(r_g)\beta_g=\alpha_g$. This is the inverse perturbation, with its action explicitly specified. Pointwise adjoints need not form a cocycle for the original action.

<a id="oa-flow.uc.2"></a>

## UC2. Composition of perturbations

Let $v$ be a unitary cocycle for $\beta=\operatorname{Ad}(u)\alpha$, and put $\gamma=\operatorname{Ad}(v)\beta$. Then $w_g=v_g u_g$ is an $\alpha$-cocycle. Indeed,

<a id="equation-uc8"></a>

\[
 \begin{aligned}
 w_{gh}
 &=v_g\beta_g(v_h)u_g\alpha_g(u_h)\\
 &=v_g u_g\alpha_g(v_h)u_g^*u_g\alpha_g(u_h)\\
 &=w_g\alpha_g(w_h).
 \end{aligned}
 \tag{UC8}
\]
Products are strongly* continuous by UC0, and $\gamma_g=\operatorname{Ad}(w_g)\alpha_g$. Three successive perturbations multiply in their order of application: first $u$, then $v$, then $z$ produces $z_g v_g u_g$. Associativity is the associativity in $M$; no factors are permuted. The identity cocycle is $g\mapsto1$, and (UC7) supplies the inverse.

Even two cocycles for the same action cannot usually be multiplied as if they were scalar characters. For a concrete example take the trivial action of $\mathbb Z$ on $M_2(\mathbb C)$, and

<a id="equation-uc9"></a>

\[
 X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
 Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
 \tag{UC9}
\]
The maps $n\mapsto X^n$ and $n\mapsto Z^n$ are cocycles. Their pointwise product has value $XZ$ at $1$ and $I$ at $2$, whereas $(XZ)^2=-I$. It is not a cocycle. In (UC8) the second cocycle is for the already perturbed action; that hypothesis supplies precisely the missing conjugation.

<a id="oa-flow.uc.3"></a>

## UC3. Gauge changes and the central ambiguity

For a fixed unitary $a\in M$, define

<a id="equation-uc10"></a>

\[
 u^a_g=a u_g\alpha_g(a^*).
 \tag{UC10}
\]
Expanding and cancelling the adjacent $\alpha_g(a^*a)$ gives

<a id="equation-uc11"></a>

\[
 u^a_g\alpha_g(u^a_h)
 =a u_g\alpha_g(u_h)\alpha_{gh}(a^*)=u^a_{gh}.
 \tag{UC11}
\]
Continuity follows because $a$ is fixed and the action is pointwise continuous. Its perturbed action is

<a id="equation-uc12"></a>

\[
 \operatorname{Ad}(u^a_g)\alpha_g
 =\operatorname{Ad}(a)\,\beta_g\,\operatorname{Ad}(a^*).
 \tag{UC12}
\]
A gauge change generally conjugates the perturbed action; it does not leave that action unchanged. Performing the gauge change by $a$ and then by $b$ gives $(u^a)^b=u^{ba}$, since $a^*b^*=(ba)^*$. Thus the relation $v=u^a$ is reflexive, symmetric (use $a^*$) and transitive (use $ba$).

Suppose $u$ and $v$ are both $\alpha$-cocycles and produce exactly the same perturbed action. Then

<a id="equation-uc13"></a>

\[
 z_g=v_g^*u_g\in\mathcal U(Z(M)),\qquad
 u_g=v_g z_g,\qquad z_{gh}=z_g\alpha_g(z_h).
 \tag{UC13}
\]
To prove centrality, equality of the two inner automorphisms says that $v_g^*u_g$ commutes with every $\alpha_g(x)$; surjectivity gives commutation with every $x$. Automorphisms preserve the centre. Substitute $u_g=v_g z_g$ into (UC4), and move only the central factors across $v_h$ to obtain (UC13). Conversely multiplying $v$ by any central $\alpha$-cocycle gives a cocycle with the same perturbed action. This identifies the exact central ambiguity without asserting that every central cocycle is a coboundary.

<a id="oa-flow.uc.4"></a>

## UC4. Cocycle conjugacy, with the nonabelian order

Let $(M,\alpha)$ and $(N,\beta)$ be actions of the same $G$. A cocycle-conjugacy datum from the first to the second is a normal unital $*$-isomorphism $\varphi:M\to N$ and a unitary cocycle $u$ for

<a id="equation-uc14"></a>

\[
 A_g=\varphi\alpha_g\varphi^{-1},\qquad
 \beta_g=\operatorname{Ad}(u_g)A_g.
 \tag{UC14}
\]
Normality of the inverse is included in the isomorphism hypothesis. UC0 makes $A$ and the transported unitary cocycles pointwise strong* continuous. Suppose $(\psi,v)$ is a datum from $(N,\beta)$ to $(P,\gamma)$. Then the composite datum is

<a id="equation-uc15"></a>

\[
 (\psi\varphi,w),\qquad w_g=v_g\psi(u_g).
 \tag{UC15}
\]
Write $B_g=\psi A_g\psi^{-1}$. The second datum says that $v$ is a cocycle for $\psi\beta_g\psi^{-1}=\operatorname{Ad}(\psi(u_g))B_g$. Consequently

<a id="equation-uc16"></a>

\[
 \begin{aligned}
 w_{gh}
 &=v_g\psi(u_g)B_g(v_h)\psi(u_g)^*\psi(u_g)B_g(\psi(u_h))\\
 &=w_g B_g(w_h),\qquad
 \gamma_g=\operatorname{Ad}(w_g)B_g.
 \end{aligned}
 \tag{UC16}
\]
The inverse datum is

<a id="equation-uc17"></a>

\[
 (\varphi^{-1},\,g\mapsto\varphi^{-1}(u_g^*)).
 \tag{UC17}
\]
Indeed the transported target action is $\varphi^{-1}\beta_g\varphi=\operatorname{Ad}(\varphi^{-1}(u_g))\alpha_g$, and UC1 proves that its adjoint cocycle reverses this perturbation. Composing (UC17) with (UC14) in either order gives the identity isomorphism and the identity cocycle. For three data, the composite cocycle is $z_g\chi(v_g)\chi\psi(u_g)$, independent of the parenthesization. This proves the equivalence-relation and composition laws with no commutativity assumption on $G$ or $M$.

<a id="oa-flow.uc.5"></a>

## UC5. Exercises and precise scope

**Exercise 1.** Starting from (UC4), compute $u_{h^{-1}g^{-1}}$ without reversing the operator factors incorrectly. **Solution.** Apply (UC5) to $gh$ and then take the adjoint of (UC4):

<a id="equation-uc18"></a>

\[
 u_{h^{-1}g^{-1}}
 =\alpha_{h^{-1}g^{-1}}(\alpha_g(u_h^*)u_g^*)
 =\alpha_{h^{-1}}(u_h^*)\alpha_{h^{-1}g^{-1}}(u_g^*).
 \tag{UC18}
\]
The first factor is $u_{h^{-1}}$, so this is also the cocycle law at $(h^{-1},g^{-1})$.

**Exercise 2.** If $u_g=a\alpha_g(a^*)$, identify the perturbed action and an inverse gauge. **Solution.** Equation (UC12) with the identity cocycle gives $\beta_g=\operatorname{Ad}(a)\alpha_g\operatorname{Ad}(a^*)$, and the gauge by $a^*$ takes $u$ to $1$. No boundedness or abelian group hypothesis is needed.

**Exercise 3.** Explain why equality in $\operatorname{Out}(M)$ at every $g$ is not itself a given cocycle. **Solution.** Individual implementers need not satisfy (UC4). Their products can differ from the chosen implementer at $gh$ by central unitaries; continuity and that two-variable defect must be resolved separately. UC1 starts with a cocycle satisfying the exact law and makes no realization assertion.

Historical source ancestry for the exterior-equivalence definition is [Connes, *Une classification des facteurs de type III*, Definition 2.2.3, printed 175](https://numdam.org/article/ASENS_1973_4_6_2_133_0.pdf#page=44). That definition concerns factors and an abelian group. The present ordered computations prove the stated arbitrary-algebra, arbitrary-group scope directly. No modular weight or spectral invariant is an input or a conclusion of this chapter.
