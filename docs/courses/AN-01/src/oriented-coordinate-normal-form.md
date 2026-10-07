# An oriented coordinate normal form for a real finite-order zero

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by the writing AI. Text: CC0.*

*Prerequisite integration and source/proof self-check by GPT-6 Astra (OpenAI), Ultra, October 2026. Historical authorship and component terms are retained.*

Smooth preparation expresses a finite-order divisor as a polynomial times a nonvanishing smooth function. For a real divisor with positive distinguished derivative, one can instead change its real distinguished coordinate. The value of the function is preserved, the leading coefficient becomes exactly \(1/k\), and the term of degree \(k-1\) disappears.

**Theorem.** Let \(k\ge1\) be an integer and \(f(t,x)\) be real valued and smooth near \((0,0)\in\mathbb R\times\mathbb R^n\). Assume
\[
 \partial_t^j f(0,0)=0\quad(0\le j<k),\qquad
 \partial_t^k f(0,0)>0.
 \tag{C1}
\]
There exist real smooth functions \(T(t,x)\) and \(c_j(x)\), \(0\le j\le k-2\), on a neighborhood of the mark, such that
\[
 T(0,0)=0,\qquad \partial_tT>0,\qquad c_j(0)=0,
\]
and
\[
 f(t,x)=\frac{T(t,x)^k}{k}
                +\sum_{j=0}^{k-2}c_j(x)T(t,x)^j.
 \tag{C2}
\]
For \(k=1\) the sum is empty. The map \((t,x)\mapsto(T(t,x),x)\) is a real local diffeomorphism preserving the orientation of the distinguished coordinate. No multiplying unit appears in (C2).

The input is the complete smooth division in Classical finite-order preparation and division, including its real-valued option. We also use the complete [real inverse/implicit proof](../prerequisites/U011-free-foundations/implicit-maps-U070.md) and [nonlinear local parameter-flow proof](../prerequisites/U011-free-foundations/smooth-parameter-flows-U072.md) in AN03, *Geometric and microlocal calculus*, §§16.4–16.5 and §§17.1–17.5. Their receiving hypotheses are an invertible real derivative for the inverse map, and a smooth real vector field on an open neighborhood for the flow. The proofs include every higher parameter derivative. Their complete selected readings are supplied under their separate CC0 1.0 component terms. The [scalar foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12–13, supplies positive roots, exponential and trigonometric calculations used below.

The complete [integral Taylor proof](when-a-kernel-is-smooth.md#taylor-estimates-on-compact-neighborhoods) supplies the finite-order remainders used here, including signed increments, complex-valued functions, directional derivatives and uniform bounds for all required derivatives on compact neighborhoods.

## The zero-parameter case and the case of order one

For \(k=1\), set \(T=f\). The hypotheses give \(T(0,0)=0\) and \(\partial_tT>0\) after shrinking. The real inverse theorem applies to \((f(t,x),x)\), whose derivative is block triangular with nonzero distinguished derivative. Formula (C2) is immediate.

Fix \(k\ge2\). With no parameters, Taylor's integral formula gives
\[
 f(t)=t^k h(t),\qquad
 h(t)=\frac1{(k-1)!}\int_0^1(1-s)^{k-1}f^{(k)}(st)\,ds,
 \qquad h(0)=\frac{f^{(k)}(0)}{k!}>0.
 \tag{C3}
\]
Shrink so that \(h>0\). The positive real root of \(kh\) is smooth: it is \(\exp(k^{-1}\log(kh))\). Set
\[
 T(t)=t\,(kh(t))^{1/k}.
 \tag{C4}
\]
Then \(f=T^k/k\), \(T(0)=0\), and \(T'(0)=(kh(0))^{1/k}>0\). By continuity its derivative remains positive nearby. This is the induction base in the number of parameters, with the exact factorial and leading coefficient retained.

## Induction on the parameter dimension

Suppose the theorem has been proved for \(n-1\) parameters. Write \(x=(x',s)\), where \(s=x_n\). Apply that result to the real slice \(f(t,x',0)\). It gives a coordinate \(u=U(t,x')\), with \(U(0,0)=0\) and \(\partial_tU>0\), and real smooth \(b_j(x')\) vanishing at zero. Extend this coordinate change to the whole family by retaining \(s\). Its real inverse is smooth by the inverse theorem.

In the new distinguished coordinate, temporarily named \(t\) again, the slice has exactly the form
\[
 f(t,x',0)=\frac{t^k}{k}+\sum_{j=0}^{k-2}b_j(x')t^j.
 \tag{C5}
\]
All transformations so far preserve the distinguished orientation. At \(x=0\), (C5) gives \(f(t,0)=t^k/k\) on an interval, so the distinguished derivative is \((k-1)!\), and all its lower jets vanish as required.

Introduce independent real coefficient variables \(a=(a_0,\ldots,a_{k-2})\) and put
\[
 F(t,x,a)=f(t,x)+\sum_{j=0}^{k-2}a_jt^j.
 \tag{C6}
\]
At the joint mark \((t,x,a)=0\), the divisor \(F_t\) has distinguished order \(k-1\):
\[
 \partial_t^l F_t(0)=0\quad(0\le l<k-1),\qquad
 \partial_t^{k-1}F_t(0)=(k-1)!\ne0.
 \tag{C7}
\]
Apply smooth division to the dividend \(f_s(t,x)\), with all of \((x,a)\) retained as real parameters. The degree-below-\(k-1\) remainder gives
\[
 f_s(t,x)=q(t,x,a)F_t(t,x,a)
                 +\sum_{j=0}^{k-2}r_j(x,a)t^j.
 \tag{C8}
\]
The quotient and coefficients are smooth on an actual joint neighborhood. They can be chosen real: if a complex representation was first obtained, take real parts of its quotient and coefficients, since both dividend and divisor are real. The key property is that each \(r_j\) is independent of \(t\).

## The conserved function and its local flow

Use \(s\) as time, \((t,a)\in\mathbb R^k\) as state, and \(x'\) as external parameters. On the open joint domain of (C8), solve the real system
\[
 \frac{d\theta}{ds}=-q(\theta,x',s,a),\qquad
 \frac{da_j}{ds}=-r_j(x',s,a),\qquad
 \theta(0)=\tau,\quad a(0)=A.
 \tag{C9}
\]
The proved local flow theorem gives \(\theta(\tau,x,A)\) and \(a(x,A)\), smooth jointly in all variables, for small two-sided \(s\), initial state \((\tau,A)\), and parameters \(x'\). To check its domain requirement, take a compact time/state/parameter rectangle inside the open domain of (C8). If \(M\) bounds the field and \(L\) bounds its state derivative there, choose \(h>0\) so that \(hM\) stays within a quarter of the available state radius and \(hL<1/2\). The complete contraction and variational construction then gives one common interval \((-h,h)\) for nearby data. No existence until a prescribed time one is assumed.

The exact receiving map for (NF1) in the supplied flow proof has time $s$, state $(\theta,a)$, external parameter $x'$, initial time zero and initial state $(\tau,A)$. Its smooth vector field is $(-q,-r_0,\ldots,-r_{k-2})$ on the joint domain from (C8). Thus (NF5) and (NF12)–(NF15) apply to every initial-state and external-parameter derivative used here, including the time derivatives.

The coefficient subsystem does not involve \(\theta\). Its local uniqueness implies that \(a(x,A)\) is independent of the initial distinguished coordinate \(\tau\). Along a trajectory, the full real chain rule gives
\[
 \frac{d}{ds}F(\theta,x',s,a)
 =f_s+F_t\theta'+\sum_{j=0}^{k-2}\theta^j a_j'
 =f_s-qF_t-\sum_{j=0}^{k-2}r_j\theta^j=0.
 \tag{C10}
\]
Every coefficient and sign is that of (C8). The equality holds throughout the actual common time interval. Evaluate the constant at \(s=0\), using (C5):
\[
 f(\theta(\tau,x,A),x)
     +\sum_{j=0}^{k-2}a_j(x,A)\theta(\tau,x,A)^j
 =\frac{\tau^k}{k}
       +\sum_{j=0}^{k-2}(A_j+b_j(x'))\tau^j.
 \tag{C11}
\]

## Inverting the coefficient flow and preserving orientation

At \(s=0\), \(a(x',0,A)=A\). Thus \(D_Aa=I\) there. The real inverse theorem applied to \((x,A)\mapsto(x,a(x,A))\) gives a smooth inverse coefficient map
\[
 A=\Lambda(x,a),\qquad a(x,\Lambda(x,a))=a,
 \qquad \Lambda(x',0,a)=a.
 \tag{C12}
\]
The full map \((\tau,x,A)\mapsto(\theta(\tau,x,A),x,a(x,A))\) also has an invertible derivative at the mark. With state coordinates first, its derivative at \(s=0\) has the form
\[
 \begin{pmatrix}I_k&B\\0&I_n\end{pmatrix}.
 \tag{C13}
\]
Its \(s\)-column in the state block is \((-q,-r)\); that column need not vanish. The state derivative is the identity, whereas the full augmented derivative need not be the identity. Multiplication by the corresponding block matrix with \(-B\) verifies invertibility directly.

For the distinguished orientation, differentiate the scalar equation in (C9) with respect to \(\tau\). The proved smooth parameter dependence permits this differentiation. Since the coefficient solution is independent of \(\tau\), no coefficient variation enters. The actual scalar derivative is
\[
 J(s)=\partial_\tau\theta(\tau,x',s,A),\qquad
 J'=-q_t(\theta,x',s,a)J,\qquad J(0)=1,
\]
and hence
\[
 J(s)=\exp\left(-\int_0^s q_t(\theta(\tau,x',u,A),x',u,a(x',u,A))\,du\right)>0.
 \tag{C14}
\]
The formula applies also for negative \(s\), with the oriented integral retained. Thus the scalar inverse \(\tau=\Psi(t,x,a)\), obtained after substituting \(A=\Lambda(x,a)\), is smooth and has
\[
 \partial_t\Psi(t,x,a)=
      \frac1{J(s)} >0.
 \tag{C15}
\]
Here \(\Lambda\) is independent of \(t\), so taking \(t\)-derivatives introduces no hidden variation of \(A\). Positivity of the determinant of a coupled state flow by itself would not justify this scalar conclusion; the triangular subsystem and (C14) supply it.

Set the final auxiliary coefficient \(a=0\) in (C11). Define
\[
 T(t,x)=\Psi(t,x,0),\qquad
 c_j(x)=\Lambda_j(x,0)+b_j(x').
 \tag{C16}
\]
Then (C11) becomes exactly (C2). At the marked point, \(s=0\), (C12) gives \(\Lambda(0,0)=0\); the initial and final distinguished coordinates agree, and all \(b_j(0)=0\). Thus \(T(0,0)=0\) and every \(c_j(0)=0\). Equation (C15) gives the positive distinguished derivative. Composing back with the earlier slice coordinate \(U\) preserves its sign and leaves the parameter coordinates fixed. This closes the induction in \(n\) and proves the theorem. \(\square\)

There is no \(T^{k-1}\) term because the augmented coefficients and the division remainder have indices only \(0\) through \(k-2\). The conservation identity preserves the original value of \(f\), so it introduces no multiplying smooth unit. Both facts follow from the actual construction, not merely from the existence of a prepared polynomial.

## Graded problems

**Exercise 1 (intermediate).** For \(f(t,s)=t^2/2+st+s^2\), carry out (C6)–(C16) explicitly. Find \(q,r_0\), both flow components, their inverses, the final coordinate and the coefficient. Give an augmented derivative which is invertible but not the identity.

**Exercise 2 (advanced).** Repeat the flow calculation for \(f(t,s)=t^3/3+st^2\), retaining both auxiliary coefficients \(a_0,a_1\). Show by conservation and direct expansion that no quadratic term remains, with the exact constant coefficient.

**Exercise 3 (advanced).** Explain why the scalar orientation proof uses independence of the coefficient equation from the scalar state. Construct a smooth linear flow on \(\mathbb R^2\) whose determinant stays positive but whose first scalar diagonal derivative becomes negative. State why it does not contradict (C14).

## Complete solutions

**Solution 1.** Here \(F=f+a_0\) and \(F_t=t+s\). The exact division is
\[
 f_s=t+2s=(t+s)+s,
 \qquad q=1,\quad r_0=s.
\]
System (C9) gives
\[
 \theta=\tau-s,\qquad a_0=A_0-s^2/2.
\]
The conservation identity is \(f(\tau-s,s)+A_0-s^2/2=\tau^2/2+A_0\). Its inverse is \(A_0=a_0+s^2/2\), \(\tau=t+s\). At final \(a_0=0\), the normal form is
\[
 T=t+s,\qquad c_0(s)=s^2/2,\qquad
 f=T^2/2+s^2/2.
\]
The map \((\tau,s,A_0)\mapsto(\theta,s,a_0)\) has derivative at the mark
\[
 \begin{pmatrix}1&-1&0\\0&1&0\\0&0&1\end{pmatrix}.
\]
Its determinant is one, but its time column is not an identity column. The distinguished derivative of the inverse is exactly one.

**Solution 2.** Write \(F=f+a_0+a_1t\). Then
\[
 F_t=t^2+2st+a_1,\qquad f_s=t^2
 =F_t-a_1-2st,
\]
so \(q=1,r_0=-a_1,r_1=-2s\). The coefficient equations and scalar equation have the exact solutions
\[
 a_1=A_1+s^2,\qquad
 a_0=A_0+A_1s+s^3/3,\qquad
 \theta=\tau-s.
\]
Substitution in \(F\) cancels all the \(s\)-dependent terms, leaving \(\tau^3/3+A_1\tau+A_0\). Setting final \(a_1=a_0=0\) gives
\[
 A_1=-s^2,\qquad A_0=2s^3/3,\qquad
 T=t+s,
\]
and therefore
\[
 f=T^3/3-s^2T+2s^3/3.
\]
For a direct check, expand \((T-s)^3/3+s(T-s)^2\): the coefficients of \(T^2\) cancel, the linear coefficient is \(-s^2\), and the constant is \(2s^3/3\). Both coefficients vanish at \(s=0\), and \(\partial_tT=1>0\).

**Solution 3.** If the coefficient state depends on the initial scalar coordinate, differentiating \(\theta'=-q(\theta,a,s)\) adds the term \(-D_aq\,\partial_\tau a\). The scalar derivative no longer satisfies the homogeneous one-dimensional equation in (C14). For example, the linear system \(u'=-v,v'=u\) has the real rotation flow
\[
 \begin{pmatrix}u(s)\\v(s)\end{pmatrix}
 =\begin{pmatrix}\cos s&-\sin s\\\sin s&\cos s\end{pmatrix}
   \begin{pmatrix}u(0)\\v(0)\end{pmatrix}.
\]
Its determinant is one for every \(s\), but \(\partial u(s)/\partial u(0)=\cos s\) is negative at \(s=\pi\). Here \(v'\) depends on \(u\), so the triangular independence hypothesis fails. Moreover our theorem uses a small actual local time interval; no global time claim follows from a local inverse. The example shows why a positive full determinant cannot replace the specific scalar variational argument.

## Sources and scope

This is the classical real coordinate preparation theorem credited to Lars Hörmander, *The Analysis of Linear Partial Differential Operators I*, reprint of the second edition (1990), §7.5, Theorem 7.5.13. The exact copy was compared with this proof. The augmented Jacobian is the block matrix (C13), whose time column may be nonzero; the state Jacobian at time zero is the identity. The original orientation argument and three worked problems are retained. The division input and its full finite-order receiving proof occur in the preceding AN01 lesson. The complete nonlinear flow and inverse constructions used here are the stated AN03 providers. We have retained the exact leading coefficient, omitted degree, real parameter domains, local existence interval and scalar orientation calculation.

This proof does not establish uniqueness of the coordinate or coefficients, or a global coordinate normal form.
