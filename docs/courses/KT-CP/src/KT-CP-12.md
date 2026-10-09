# Exterior equivalence and Connes's construction of the Thom map

*Written by GPT-6.1 Sol (OpenAI), October 2026. Tensor-norm proof-provider reconciliation by GPT-6 Astra (OpenAI), Ultra. Self-checked; independent review is separate. Public domain (CC0).*

A projection can move under an action even though its K-class cannot move along a continuous orbit. We first replace it by a smooth projection, then compensate for its motion with a unitary cocycle. The resulting action fixes the projection. Its scalar suspension class can then be transported back to the original crossed product.

We prove that this procedure gives the suspension-compatible family \(\Gamma_\alpha^i=(-1)^{i+1}T_\alpha^i\) of Lesson 11. In particular the construction is independent of both choices. The comparison uses the Wiener–Hopf extension directly.

## The direction of a cocycle isomorphism

Let \(\alpha\) be a point-norm continuous action of a locally compact group \(G\) on a C*-algebra \(A\). Its automorphisms extend strictly to \(M(A)\). A strictly continuous unitary cocycle is a map \(u:G\to UM(A)\) with
\[
 u_{st}=u_s\alpha_s(u_t).
 \tag{12.1}
\]
Strict continuity means continuity of both \(u_sa\) and \(au_s\) in norm for each \(a\in A\). For a unitary-valued map either condition, together with continuity of the adjoints, supplies the other. The identity gives \(u_e=1\) and
\[
 u_{s^{-1}}=\alpha_{s^{-1}}(u_s^*).
 \tag{12.2}
\]
Define the exterior equivalent action
\[
 \beta_s(a)=u_s\alpha_s(a)u_s^*.
 \tag{12.3}
\]
The cocycle equation proves \(\beta_s\beta_t=\beta_{st}\). Strict continuity, point-norm continuity of \(\alpha\), and multiplication of bounded multipliers by elements of \(A\) prove point-norm continuity of \(\beta\).

**Theorem 12.1.** Exterior equivalence gives isomorphisms of full and reduced crossed products. With left coefficients and the integrated form \(\int \pi(f(s))U_s\,ds\), their direction and core formula are
\[
 \begin{gathered}
 \Theta_u:A\rtimes_\beta G\longrightarrow A\rtimes_\alpha G,\\
 (\Theta_u g)(s)=g(s)u_s,\qquad
 (\Theta_u^{-1}f)(s)=f(s)u_s^* .
 \end{gathered}
 \tag{12.4}
\]
For abelian \(G\), these maps intertwine the dual actions.

**Proof.** Strict multiplication makes \(g(s)u_s\) a norm-continuous, compactly supported \(A\)-valued function. The cocycle relation gives
\[
 u_r^*u_s=\alpha_r(u_{r^{-1}s}).
 \tag{12.5}
\]
Consequently
\[
 \begin{aligned}
 \Theta_u(g*_\beta k)(s)
 &=\int_G g(r)u_r\alpha_r(k(r^{-1}s))u_r^*u_s\,dr\\
 &=\int_G g(r)u_r\alpha_r(k(r^{-1}s)u_{r^{-1}s})\,dr\\
 &=(\Theta_u g)*_\alpha(\Theta_u k)(s).
 \end{aligned}
 \tag{12.6}
\]
For the involution, (12.2) gives
\[
 \begin{aligned}
 (\Theta_u g)^{*_\alpha}(s)
 &=\Delta_G(s)^{-1}\alpha_s(u_{s^{-1}}^*g(s^{-1})^*)\\
 &=\Delta_G(s)^{-1}u_s\alpha_s(g(s^{-1})^*)\\
 &=\Theta_u(g^{*_\beta})(s).
 \end{aligned}
 \tag{12.7}
\]
These calculations also establish the inverse core map.

If \((\pi,U)\) is covariant for \(\alpha\), extend \(\pi\) nondegenerately to multipliers and put \(V_s=\pi(u_s)U_s\). The cocycle identity makes \(V\) a continuous unitary representation, and its covariance is exactly (12.3). Conversely \(U_s=\pi(u_s^*)V_s\) recovers an \(\alpha\)-covariant pair from a \(\beta\)-covariant one. These operations are inverse. Their integrated forms agree with (12.4), so the universal norm suprema agree. This proves the full isomorphism.

Here is also the reduced norm calculation. Use a faithful nondegenerate representation \(\pi\) of \(A\). On \(L^2(G,H_\pi)\), multiplication by
\[
 (V\xi)(t)=\pi(u_{t^{-1}}^*)\xi(t)
 \tag{12.8}
\]
is a unitary. It conjugates the regular coefficient representation for \(\beta\) to that for \(\alpha\). For the left regular group operator,
\[
 \begin{aligned}
 V\lambda_sV^*\xi(t)
 &=\pi(u_{t^{-1}}^*u_{t^{-1}s})\xi(s^{-1}t)\\
 &=\pi(\alpha_{t^{-1}}(u_s))\xi(s^{-1}t).
 \end{aligned}
 \tag{12.9}
\]
Thus it conjugates the integrated regular representation of \(g\) to that of \(\Theta_u g\). Reduced norms agree, and the full maps commute with the regular quotient maps.

Finally the dual action multiplies a core value at \(s\) by the scalar \(\chi(s)\). That multiplication commutes with right multiplication by \(u_s\), proving dual equivariance. ∎

Specifying the direction in (12.4) is essential. From \(\beta=\operatorname{Ad}u\circ\alpha\), the multiplier \(U_\beta(s)\) maps to \(u_sU_\alpha(s)\). The reverse map has coefficient \(f(s)u_s^*\).

## When implementers leave a projective obstruction

An inner automorphism at every group element does not supply a unitary representation of the group. Suppose \(W_s\in UM(A)\) implements an action \(\alpha_s=\operatorname{Ad}W_s\). Then
\[
c(s,t)=W_sW_tW_{st}^*
\tag{12B.1}
\]
commutes with \(A\), since the two products implement the same automorphism. Unless its central values can be removed coherently, the \(W_s\) are projective implementers. Replacing group unitaries by \(W_s^*U_s\) makes them commute with \(A\), but their multiplication retains a scalar or central multiplier. The ordinary cocycle condition (12.1) is exactly what avoids this problem.

A useful framework records the multiplier as part of the action. A **normalized continuous twisted action** consists of point-norm continuous automorphisms \(\gamma_s\), with \(\gamma_e=1\), and a jointly strictly continuous \(w:G\times G\to UM(A)\), satisfying
\[
\begin{aligned}
\gamma_s\gamma_t&=\operatorname{Ad}w(s,t)\,\gamma_{st},\\
w(s,t)w(st,r)&=\gamma_s(w(t,r))w(s,tr),\\
w(e,s)&=w(s,e)=1.
\end{aligned}
\tag{12B.2}
\]
Inverses such as \(\gamma_s^{-1}\) below mean inverse automorphisms; they must not be silently replaced by \(\gamma_{s^{-1}}\). The second identity is the associativity constraint: the two ways to reduce three group operators must agree. This is the Busby–Smith formulation; Meyer's correspondence viewpoint explains it as coherence for a weak action.

A twisted covariant pair is a nondegenerate representation \(\rho\) and a strongly continuous unitary map \(T\), with
\[
T_s\rho(a)T_s^*=\rho(\gamma_s(a)),\qquad
T_sT_t=\rho(w(s,t))T_{st}.
\tag{12B.3}
\]
Its coefficient algebra is \(C_c(G,A)\), with
\[
\begin{aligned}
(f*_w g)(r)&=\int_G f(s)\gamma_s(g(s^{-1}r))w(s,s^{-1}r)\,ds,\\
f^{*_w}(r)&=\Delta_G(r)^{-1}w(r,r^{-1})^*
                         \gamma_r(f(r^{-1})^*).
\end{aligned}
\tag{12B.4}
\]
For example, the coefficient of a threefold product in \((f*_wg)*_wh\), at the triple \((s,t,z)\), contains
\[
f(s)\gamma_s(g(t))w(s,t)\gamma_{st}(h(z))w(st,z).
\]
Moving the middle \(w(s,t)\) through the third coefficient by the first identity in (12B.2), and using the second identity, gives the coefficient in \(f*_w(g*_wh)\). Haar substitutions and compact-support Fubini prove associativity. Taking the adjoint of \(\rho(a)T_s\), and then applying Haar inversion, gives exactly the second line of (12B.4); the cocycle identity at \((s,s^{-1},s)\) verifies the alternative expression using \(T_s^*\). Thus the integrated form is a *-homomorphism, bounded by the coefficient \(L^1\)-norm.

There are always enough such representations. Given a faithful nondegenerate \(\rho_0:A\to B(\mathcal H_0)\), set on \(L^2(G,\mathcal H_0)\)
\[
\begin{aligned}
(\pi(a)\xi)(r)&=\rho_0(\gamma_r^{-1}(a))\xi(r),\\
(R_s\xi)(r)&=\rho_0\!\left(\gamma_r^{-1}(w(s,s^{-1}r))\right)\xi(s^{-1}r).
\end{aligned}
\tag{12B.5}
\]
These are a nondegenerate coefficient representation and unitary operators, continuous on compactly supported continuous vectors by the stated continuity assumptions, then on all vectors by density. Put \(q=s^{-1}r\). The first identity of (12B.2) gives
\[
\gamma_r^{-1}\gamma_s
 =\operatorname{Ad}\!\left(\gamma_r^{-1}(w(s,q))\right)\gamma_q^{-1}.
\tag{12B.6}
\]
It proves covariance in (12B.5). With \(z=t^{-1}q\), the second identity becomes
\[
w(s,t)w(st,z)=\gamma_s(w(t,z))w(s,q).
\]
Substituting (12B.6) proves \(R_sR_t=\pi(w(s,t))R_{st}\).

The integrated representation separates the coefficient core. Its kernel, after putting \(s=rt^{-1}\) in left Haar integration, is
\[
K_f(r,t)=\Delta_G(t)^{-1}
 \rho_0\!\left(\gamma_r^{-1}(f(rt^{-1})w(rt^{-1},t))\right).
\tag{12B.7}
\]
If \(f(s_0)\ne0\), a matrix coefficient of this kernel is nonzero at \((s_0,e)\). Its continuity permits compact scalar test bumps in the two variables, with a constant phase, whose integrated matrix coefficient is nonzero. Thus the operator is nonzero. Suprema over twisted covariant pairs define the full algebra \(A\rtimes_{\gamma,w}G\); (12B.5) defines its reduced quotient. Representation-independence of the reduced norm follows by the same faithful localization argument as Lesson 2: replace \(\rho_0\) in (12B.5) by left multiplication on \(L^2(G,A)\), obtain adjointable module operators, and localize through a faithful representation of \(A\). Their coefficients and group factors are the displayed ones, so the operator norm is preserved by that localization.

## Removing a twist after stabilization

For a strictly continuous unitary map \(v:G\to UM(A)\), \(v_e=1\), define
\[
\begin{aligned}
\gamma'_s&=\operatorname{Ad}v_s\,\gamma_s,\\
w'(s,t)&=v_s\gamma_s(v_t)w(s,t)v_{st}^*.
\end{aligned}
\tag{12B.8}
\]
Substitution in (12B.2) proves that these are a twisted action. The change of covariant pairs \(T'_s=\rho(v_s)T_s\) is invertible and gives the full core isomorphism \(f(s)\mapsto f(s)v_s\), from the primed algebra to the original one. It preserves reduced norms as well. In the regular models (12B.5), the multiplication unitary
\[
(Q\xi)(r)=\rho_0(\gamma_r^{-1}(v_r^*))\xi(r)
\tag{12B.9}
\]
satisfies \(Q\pi(a)Q^*=\pi'(a)\) and
\(Q\pi(v_s)R_sQ^*=R'_s\). To check the second equality, expand its coefficient and use (12B.6); its value is
\[
\rho_0\!\left(\gamma_r^{-1}
 (v_r^*v_s\gamma_s(v_q)w(s,q))\right),
\quad q=s^{-1}r,
\]
which equals \(\rho_0((\gamma'_r)^{-1}(w'(s,q)))\). This proves the reduced assertion without assuming \(w=1\).

**Theorem 12B.1 (continuous stabilization trick).** Put \(\mathcal E=L^2(G,A)\), \(B=\mathcal K_A(\mathcal E)\cong A\otimes\mathcal K(L^2(G))\), and \(\gamma_s^B=\gamma_s\otimes1\). There is an ordinary continuous action \(\beta\) of \(G\) on \(B\) with
\[
\begin{aligned}
(A\rtimes_{\gamma,w}G)\otimes\mathcal K(L^2(G))
   &\cong B\rtimes_\beta G,\\
(A\rtimes_{\gamma,w,r}G)\otimes\mathcal K(L^2(G))
   &\cong B\rtimes_{\beta,r}G.
\end{aligned}
\tag{12B.10}
\]
No separability, amenability, or countability assumption is needed for this normalized jointly continuous formulation.

**Proof.** Define adjointable module unitaries by
\[
(v_s\xi)(r)=w(s,s^{-1}r)^*\xi(s^{-1}r),\qquad
(v_s^*\xi)(r)=w(s,r)\xi(sr).
\tag{12B.11}
\]
Left invariance of Haar measure proves preservation of the \(A\)-valued inner product, and the second formula is the inverse and adjoint. Strict continuity follows first on compactly supported \(A\)-valued continuous vectors, using joint strict continuity of \(w\), and then on all module vectors by density. For module unitaries, strong continuity of the operators and their adjoints gives strict continuity as multipliers of the compact endomorphisms, since their products with rank-one operators converge in norm.

Write \(q=s^{-1}r\), \(z=t^{-1}q\). The coefficient of \(v_s\gamma_s^B(v_t)(w(s,t)\otimes1)\) is
\[
w(s,q)^*\gamma_s(w(t,z)^*)w(s,t)=w(st,z)^*.
\tag{12B.12}
\]
Indeed this is obtained by taking the adjoint of the cocycle equation just below (12B.6) and multiplying by \(w(s,t)\). Hence the primed twist in (12B.8) is identically one for
\(\beta_s=\operatorname{Ad}v_s\,\gamma_s^B\). The same identities make \(\beta_s\beta_t=\beta_{st}\), and strict continuity of \(v\) makes \(\beta\) point-norm continuous on \(B\). The preceding full and reduced norm comparison identifies the twisted crossed products of \(B\) with its ordinary crossed products by \(\beta\).

Finally
\[
B\rtimes_{\gamma^B,w\otimes1}G
 \cong (A\rtimes_{\gamma,w}G)\otimes\mathcal K(L^2(G)).
\tag{12B.13}
\]
For full norms this follows from commuting representations of the coefficient factors: the trivial compact factor commutes with all group unitaries in (12B.3), and tensoring any twisted pair with a representation of the compacts supplies the inverse correspondence. The maximal tensor norm with compacts equals the spatial norm by [Example 3.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-APPROX/completely-positive-finite-models.html#3-finite-models-that-we-can-see) and [Theorem 4.3, with Lemmas 4.1 and 4.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-APPROX/completely-positive-finite-models.html#4-why-matrix-models-control-tensor-norms) in Completely positive finite models. The compression maps use the net of all finite-dimensional subspaces, so the proof covers arbitrary Hilbert spaces and nonunital coefficient algebras. The Hilbert-module tensor prerequisite supplies the separate compact-endomorphism identification in Theorem 5.1. For reduced norms apply (12B.5) to \(\rho_0\otimes1\) and interchange the two Hilbert-space tensor factors; the regular coefficient and group formulas become those for \(A\), tensored with the identity. Faithful localization supplies the same norm conclusion for arbitrary Hilbert-space dimension. Combining (12B.13) with (12B.8)–(12B.12) proves both lines of (12B.10). ∎

The theorem explains the stabilization principle without treating a nonsplit normal-subgroup extension as an ordinary quotient action. Green's \((G,N)\)-twisted formulation is another formulation, with separate topological data; it is not defined by assuming a continuous section of \(G\to G/N\).

## A pointwise inner action with a nontrivial crossed product

For a concrete obstruction let \(\mathcal H=\ell^2(\mathbb Z)\), fix irrational \(\theta\), put \(c=e^{2\pi i\theta}\), and define
\[
S e_n=e_{n+1},\qquad D e_n=c^n e_n,\qquad DS=cSD.
\tag{12B.14}
\]
On \(A=\mathcal K(\mathcal H)\), the commuting automorphisms \(\operatorname{Ad}S,\operatorname{Ad}D\) define a \(\mathbb Z^2\)-action. In its crossed product write \(U,V\) for the commuting group unitaries. The unitaries \(X=S^*U\), \(Y=D^*V\) commute with \(A\), and direct multiplication gives
\[
YX=c^{-1}XY.
\tag{12B.15}
\]
Indeed, \(UD^*U^*=cD^*\) and \(VS^*V^*=c^{-1}S^*\), giving \(XY=cS^*D^*UV\), \(YX=S^*D^*UV\). Conversely, if \(X,Y\) commute with \(A\) and satisfy (12B.15), then \(U=SX,V=DY\) commute and implement the original action. These inverse covariant-pair constructions prove
\[
A\rtimes\mathbb Z^2\cong
 A\otimes A_{-\theta},
\tag{12B.16}
\]
where \(A_{-\theta}\) is the universal rotation algebra with relation (12B.15). Its realization as an irrational rotation crossed product and its simplicity are proved in Lesson 3. Spatial tensoring with compacts preserves simplicity, as follows by cutting an ideal by matrix units. Thus (12B.16) is simple. The trivial action instead gives \(A\otimes C(\mathbb T^2)\), which has proper ideals \(A\otimes C_0(\mathbb T^2\setminus\{z\})\). Pointwise innerness has not supplied the ordinary cocycle needed to identify these crossed products.

## A smooth representative of a projection

Now \(G=\mathbb R\), and \(\delta\) denotes the generator of \(\alpha\) on its differentiable domain. Extend the action entrywise to matrix algebras and to the external unitization \(A^+\), fixing its scalar quotient.

**Lemma 12.2.** Every projection \(p\in M_n(A^+)\) is homotopic, through conjugate projections with the same scalar part, to a projection \(f\) whose orbit \(t\mapsto\alpha_t(f)\) is \(C^\infty\) in norm. If \(p\in M_n(A)\), then \(f\in M_n(A)\).

**Proof.** Choose a nonnegative smooth compactly supported function \(\rho\) on \(\mathbb R\) with integral one. For sufficiently small \(\varepsilon>0\),
\[
 b=\int_{\mathbb R}\varepsilon^{-1}\rho(s/\varepsilon)
                  \alpha_s(p)\,ds,\qquad
 \|b-p\|<\tfrac18 .
 \tag{12.10}
\]
Point-norm continuity proves the estimate. Changing variables in \(\alpha_t(b)\) moves \(t\) into the smooth scalar kernel. Its derivatives of every order are integrals against derivatives of that kernel, so \(b\) has a smooth orbit.

The spectrum of the self-adjoint \(b\) lies within distance \(1/8\) of \(\{0,1\}\). Let \(\gamma\) be the positively oriented circle of radius \(1/2\) about \(1\), and set
\[
 f=\frac{1}{2\pi i}\int_\gamma(z-b)^{-1}\,dz .
 \tag{12.11}
\]
Functional calculus makes \(f\) a self-adjoint projection. On \(\gamma\), the resolvent norms for \(p,b\) are at most \(2,8/3\), respectively. The resolvent identity therefore gives
\[
 \|f-p\|\leq \tfrac12\cdot2\cdot\tfrac83\|b-p\|<\tfrac13.
 \tag{12.12}
\]
Differentiating the inverse along the smooth orbit of \(b\), and then the compact contour integral, proves smoothness of \(f\). The scalar quotient of \(b\) is \(p_0=q(p)\), so \(q(f)=p_0\). When \(p\in M_n(A)\), functional calculus uses a function vanishing at zero and gives \(f\in M_n(A)\).

For the actual equivalence put
\[
 v=fp+(1-f)(1-p)=1+(f-p)(2p-1).
 \tag{12.13}
\]
Since \(\|v-1\|<1\), \(v\) is invertible; \(vp=fv\) implies that \(v^*v\) commutes with \(p\). Its polar unitary \(w=v(v^*v)^{-1/2}\) consequently satisfies \(wpw^*=f\). The invertible path \(v_r=1+r(v-1)\) has a continuous polar-unitary path \(w_r\), joining \(1\) to \(w\). Its scalar quotient is \(1\). Thus \(w_rpw_r^*\) is the required projection homotopy, and all its scalar parts equal \(p_0\). ∎

## A cocycle which stops the projection

Work in the relevant matrix algebra, with the scalar action extended as above. For the smooth projection \(f\), differentiation of \(f^2=f\) gives
\[
 f\delta(f)+\delta(f)f=\delta(f),\qquad
 f\delta(f)f=0.
 \tag{12.14}
\]
The element
\[
 h=f\delta(f)-\delta(f)f
 \tag{12.15}
\]
is skew-adjoint and belongs to \(M_n(A)\), even when \(f\) is in the unitization. Direct use of (12.14) gives
\[
 [h,f]=-\delta(f).
 \tag{12.16}
\]

**Lemma 12.3.** The norm differential equation
\[
 u_t'=u_t\alpha_t(h),\qquad u_0=1
 \tag{12.17}
\]
has a norm-continuous unitary solution for all real \(t\). It is an \(\alpha\)-cocycle, belongs to \(1+M_n(A)\), and the action \(\beta_t=\operatorname{Ad}u_t\circ\alpha_t\) fixes \(f\).

**Proof.** Iterating the integral equation gives uniformly convergent Picard series on every bounded time interval: the term of order \(k\) has norm at most \(|t|^k\|h\|^k/k!\). The same estimates applied to a difference prove uniqueness. Negative intervals use the oriented integral from \(0\) to \(t\). This constructs a solution globally; each term except the constant belongs to \(M_n(A)\).

Writing \(a(t)=\alpha_t(h)\), skew-adjointness gives \((u_tu_t^*)'=0\). Also \(u_t^*u_t\) solves \(y'=-a(t)y+ya(t)\), whose solution with initial value \(1\) is uniquely \(1\). Thus \(u_t\) is unitary.

For fixed \(s\), both \(t\mapsto u_{s+t}\) and \(t\mapsto u_s\alpha_s(u_t)\) solve \(v'=v\alpha_{s+t}(h)\) with initial value \(u_s\). Uniqueness gives the cocycle equation. Finally
\[
 \frac d{dt}\bigl(u_t\alpha_t(f)u_t^*\bigr)
     =u_t\alpha_t(\delta(f)+[h,f])u_t^*=0.
 \tag{12.18}
\]
Its value at zero is \(f\), proving the assertion. On the domain of \(\delta\), differentiation at zero gives the generator formula \(\delta+[h,\,\cdot\,]\). No identification of the entire generator domain is needed. ∎

Lemmas 12.2–12.3 supply the projection and fixed action in Connes's construction. Notice the skew-adjoint \(h\) and the order of the factors in (12.17). Both are forced by (12.18).

## Exterior equivalence of the Wiener–Hopf extensions

Write \(B_\alpha=A\rtimes_\alpha\mathbb R\), and use the extensions and coefficient K-theory identifications of Lessons 10–11. For a real cocycle \(u\), right multiplication by \(u_s\) gives an isomorphism
\[
 W_\beta\longrightarrow W_\alpha,\qquad
 g(s,t)\longmapsto g(s,t)u_s.
 \tag{12.19}
\]
Indeed the cocycle becomes the constant-in-\(t\) multiplier \(u_s\) of the cone coefficient algebra. Multiplication by this multiplier preserves the limit at \(+\infty\). Theorem 12.1 applies, and evaluation there gives exactly \(\Theta_u:B_\beta\to B_\alpha\).

**Lemma 12.4.** Under the untwisted identifications of the ideals with \(A\otimes\mathcal K(L^2(\mathbb R))\), the ideal map in (12.19) is \(\operatorname{Ad}W\), where the adjointable unitary \(W\) on \(L^2(\mathbb R,A)\) is
\[
 (W\xi)(t)=\alpha_{-t}(u_t)\xi(t)=u_{-t}^*\xi(t).
 \tag{12.20}
\]
It acts as the identity on both K-groups after the usual corner identification.

**Proof.** Multiplication by the bounded strictly continuous unitary field in (12.20) preserves the \(A\)-valued inner product. Its pointwise adjoint is its inverse. It is therefore an adjointable module unitary and a multiplier of the compact endomorphism algebra.

It suffices to compute on the rank kernels used in Lesson 10. Before untwisting, the \(\beta\)-kernel for \(a\otimes\theta_{k,l}\) is
\(\beta_t(a)k(t)\overline{l(t-s)}\). After (12.19) and \(\alpha\)-untwisting it becomes, with \(r=t-s\),
\[
 \alpha_{-t}(\beta_t(a)u_s)k(t)\overline{l(r)}
       =W(t)aW(r)^*k(t)\overline{l(r)}.
 \tag{12.21}
\]
Here \(u_t=u_s\alpha_s(u_r)\) gives
\(\alpha_{-t}(u_t^*u_s)=\alpha_{-r}(u_r^*)\).
Finite rank kernels are dense, so this proves the ideal formula.

For completeness, every multiplier-inner automorphism of an algebra \(D\) induces the identity on K-theory. If \(w\in UM(D)\), the multiplier-unitary path
\[
 H_\vartheta=
 \begin{pmatrix}w&0\\0&1\end{pmatrix}
 R_\vartheta
 \begin{pmatrix}1&0\\0&w^*\end{pmatrix}
 R_\vartheta^*,\qquad
 R_\vartheta=
 \begin{pmatrix}\cos\vartheta&-\sin\vartheta\\
                 \sin\vartheta&\cos\vartheta\end{pmatrix},
 \tag{12.22}
\]
joins \(\operatorname{diag}(w,w^*)\) to \(1\) as \(\vartheta\) runs from \(0\) to \(\pi/2\).
For a projection \(p\in M_m(D^+)\) with scalar part \(p_0\), amplify \(w\) by \(1_m\) and conjugate \(\operatorname{diag}(p,p_0)\) by this path. Every member commutes with the repeated scalar matrix \(\operatorname{diag}(p_0,p_0)\). Thus the differences from that matrix remain in \(M_{2m}(D)\). This is a homotopy, in the unitization, between \(\operatorname{diag}(\operatorname{Ad}w(p),p_0)\) and \(\operatorname{diag}(p,p_0)\), with constant scalar part. It proves equality on relative projection classes. For a unitary \(z\in M_m(D^+)\) with scalar part \(1\), conjugating \(\operatorname{diag}(z,1)\) gives the corresponding K-one homotopy. These generators prove both assertions. Apply this to \(D=A\otimes\mathcal K\) and \(w=W\). ∎

Naturality of the two extension boundaries now gives, in coefficient K-theory,
\[
 \partial_j^\alpha(\Theta_u)_*=\partial_j^\beta.
 \tag{12.23}
\]
Since both boundaries are invertible by Lesson 11, we obtain
\[
 (\Theta_u)_*T_\beta^i=T_\alpha^i,\qquad
 (\Theta_u)_*\Gamma_\beta^i=\Gamma_\alpha^i.
 \tag{12.24}
\]
The argument includes arbitrary strictly continuous cocycles. It does not impose norm differentiability on them.

## The transported scalar unitary

Use the positive Fourier transform of Lesson 6, and choose the positive winding-one scalar unitary of Lesson 10:
\[
 v(x)=\frac{x-i/(4\pi)}{x+i/(4\pi)}
     =1-\int_0^\infty e^{-s/2}e^{2\pi ixs}\,ds .
 \tag{12.25}
\]
Thus \([v]=\beta_{\mathbb C}[1]\) for the positive Bott map \(\beta_{\mathbb C}\), while its Wiener–Hopf index is \(-1\).

Suppose first that \(A\) is unital and \(p\in M_n(A)\). Choose a smooth equivalent \(f\), and an exterior cocycle \(u\) such that \(\beta=\operatorname{Ad}u\circ\alpha\) fixes \(f\). The possibly degenerate coefficient map \(j_f:\mathbb C\to M_n(A)\), \(z\mapsto zf\), is equivariant from the trivial action to \(\beta\). Its crossed map sends \(v-1\) to an element of \(M_n(B_\beta)\). Therefore
\[
 Z_{f,u}=1-\int_0^\infty e^{-s/2}f u_s U_\alpha(s)\,ds
       \ \in M_n(B_\alpha)^+
 \tag{12.26}
\]
is unitary: it is the image of \(1+j_f\rtimes1(v-1)\) under the unitized isomorphism \(\Theta_u\). The integral denotes the integrated \(L^1(\mathbb R,M_n(A))\) coefficient kernel, extended by zero on negative times. Its norm is bounded by the coefficient \(L^1\)-norm, so it is a well-defined element of the crossed product. The endpoint discontinuity is harmless for the \(L^1\) completion; continuous compactly supported kernels approximate it there.

Define the tentative projection map by \([p]\mapsto[Z_{f,u}]\), using the standard matrix identification of K-theory.

**Theorem 12.5 (construction and comparison).** This procedure defines an additive homotopy-invariant map, independent of \(f,u\), and
\[
 \varphi_\alpha^0=\Gamma_\alpha^0=-T_\alpha^0:
      K_0(A)\longrightarrow K_1(B_\alpha).
 \tag{12.27}
\]
It extends to every C*-algebra by relative projections in the unitization.

**Proof.** Naturality in Lesson 11 applies to \(j_f\), including its degeneracy. Since the scalar value of \(\Gamma^0\) is the positive class \([v]\), it gives
\[
 (j_f\rtimes1)_*[v]=\Gamma_\beta^0[f].
 \tag{12.28}
\]
Equation (12.24) then sends this to \(\Gamma_\alpha^0[f]=\Gamma_\alpha^0[p]\). Thus every allowed pair of choices gives precisely the right side of (12.27). This proves all choice independence at once, including choices of cocycles which are only strictly continuous. Additivity, matrix stability and projection-homotopy invariance follow from the already proved homomorphism \(\Gamma_\alpha^0\). Group completion gives the map on differences of projection classes.

For nonunital \(A\), perform the construction in \(A^+\). The equivariantly split sequence \(0\to A\to A^+\to\mathbb C\to0\) gives a split exact crossed-product sequence by Lesson 1, and a split exact K-theory sequence by the general foundations fixed in Lesson 10. Hence \(K_1(B_\alpha)\) embeds in \(K_1(B_{\alpha^+})\) as the kernel of the scalar quotient map. If \(x\in K_0(A)\), its image in \(K_0(A^+)\) has scalar quotient zero. Naturality makes the scalar quotient of \(\Gamma_{\alpha^+}^0(x)\) zero as well. There is consequently a unique class in \(K_1(B_\alpha)\) represented by the constructed difference of unitization classes. Naturality for \(A\to A^+\) identifies it with \(\Gamma_\alpha^0(x)\). This proves (12.27) for all \(A\). ∎

Using the ordinary positive maps \(\theta_A:K_1(A)\to K_0(SA)\) and \(\beta_{B_\alpha}:K_0(B_\alpha)\to K_1(SB_\alpha)\), define
\[
 \varphi_\alpha^1
     =\beta_{B_\alpha}^{-1}\varphi_{S\alpha}^0\theta_A.
 \tag{12.29}
\]
The coefficient isomorphism \((SA)\rtimes_{S\alpha}\mathbb R\cong S B_\alpha\) keeps the original suspension coordinate first. The suspension identity (11.27) proves
\[
 \varphi_\alpha^1=\Gamma_\alpha^1=+T_\alpha^1.
 \tag{12.30}
\]
Thus both constructed maps are isomorphisms. Their trivial-action values and index-normalized conversion are
\[
 \begin{gathered}
 \varphi_{\mathrm{triv}}^0=\beta_A,\qquad
 \varphi_{\mathrm{triv}}^1=-\theta_A,\\
 \Phi_\alpha^i=(-1)^i\varphi_\alpha^i.
 \end{gathered}
 \tag{12.31}
\]
The even positive winding class does not make the odd map positive with the same suspension ordering. The signed interchange of two odd Bott coordinates in Lesson 11 explains the second formula.

## Parameter paths and what they prove

The equality with \(\Gamma\) proved independence for all choices. One can also see the norm homotopies behind the smooth choices.

For a continuous projection path \(p_r\), \(0\leq r\leq1\), choose the averaging scale in (12.10) uniformly in \(r\). This is possible because \(\{p_r\}\) is norm compact: a finite approximation of this set and point-norm continuity of the action give uniform continuity at zero. The Riesz formulas then give a continuous family \(f_r\), smooth in the action variable, with \(\delta(f_r)\) continuous in \(r\). Consequently the skew-adjoint \(h_r\) of (12.15) is norm continuous.

Picard estimates for (12.17), uniform on compact \((r,t)\)-sets, give \(u_t^{(r)}\) jointly norm continuous. The cocycle and fixed-projection arguments hold at every \(r\). The kernels in (12.26) are therefore continuous in \(r\) in coefficient \(L^1\)-norm: truncate to a bounded time interval for uniform continuity, and bound the remaining tail by \(e^{-s/2}\). Their integrated unitaries form a norm homotopy.

For a fixed smooth \(f\), any two skew-adjoint bounded perturbations \(h_0,h_1\) with \([h_j,f]=-\delta(f)\) can be joined by \(h_r=(1-r)h_0+rh_1\). The same ODE construction gives a homotopy of cocycles, each fixing \(f\) after perturbation. Different sufficiently close averaging choices can also be joined: interpolate their averaged self-adjoint elements inside the \(1/8\)-ball about \(p\), and apply the common Riesz contour. This supplies \(f_r,h_r,u^{(r)}\) as above.

These path arguments apply to bounded-generator constructions. A general strictly continuous cocycle need not have a bounded norm derivative. Its comparison with these choices is supplied by the extension calculation (12.19)–(12.24), which requires no such derivative.

## Double Thom maps and Takai duality

The double Thom compatibility is the product assertion conditional on the bivariant prerequisite *Descent and the K-theory of crossed products*, in *Kasparov's KK-theory*. The additional compatibility requires the full Fack–Skandalis proof, agreement with the Wiener–Hopf normalization, and the exercise proving the dual Thom product. In the source conventions of [Connes 1994], the assertion is:
\[
 \begin{gathered}
 \varphi_{C,\alpha}:K_i(A)\ \cong\
          K_{i+1}(A\rtimes_\alpha\mathbb R),\\
 (\Psi_C)_*\varphi_{C,\widehat\alpha}\varphi_{C,\alpha}
       =s_A:K_i(A)\longrightarrow K_i(A\otimes\mathcal K).
 \end{gathered}
 \tag{12.32}
\]
Here \(s_A\) is the rank-one stabilization map, and \(\Psi_C\) is the regular-module double-duality identification of that source's Theorem 6, p. 178. Both parities are included. The required proof is the Connes–Thom section and the dual-product exercise of the KK lesson just named. Its required comparison identifies the KK Thom classes with these source-convention maps, including the suspension sign and the Takai identification. This is an existing proof prerequisite not included in this edition; we do not assert that its proof has already been written. Its inputs from this course are the Thom theorem and its normalization in Lesson 11, not (12.32), so the product proof does not assume the compatibility being supplied.

The KK proof applies to separable coefficient algebras. Here is the extension to the arbitrary coefficients of this course. A countable subset of \(A\) lies in a separable \(\alpha\)-invariant C*-subalgebra: generate from its rational-time translates and adjoints. Point-norm continuity makes the closed generated algebra invariant under every real time. These subalgebras are directed and have dense union. Their full crossed products embed by reduced embedding and amenability of \(\mathbb R\), as proved in Lessons 2 and 4. Compact-support coefficient approximation makes their union dense in \(A\rtimes\mathbb R\); the same assertion applies to the dual products and to stabilization.

The projection construction, suspension extension and regular-module Takai maps commute with these coefficient inclusions. For the first this follows from (12.27)-(12.30) and Thom naturality; for Takai it follows from its coefficient kernel formula. The finite-matrix and compact-homotopy continuity proof in Lesson 11 puts every input K-class at one separable stage. Applying the separable product identity there and then its inclusion proves (12.32) for arbitrary \(A\). This passage uses no KK group for a nonseparable algebra.

The source symbols \(\varphi_C,\Psi_C\) in (12.32) specify its normalization. Passing to another Fourier model or to the positive-both-parities family \(\Phi\) requires the corresponding identifications and the signed conversion in (12.31). The extension argument above proves choice independence and invertibility directly; the planned product proof supplies the additional double compatibility.

## Examples

**Inner actions.** Let \(v_t\) be a strictly continuous unitary group in \(M(A)\), and let \(\gamma_t=\operatorname{Ad}v_t\). It is an exterior perturbation of the trivial action. Formula (12.4), followed by the positive Fourier transform, gives
\[
 \begin{gathered}
 A\rtimes_\gamma\mathbb R\cong A\otimes C_0(\mathbb R),\\
 f\longmapsto\left(x\longmapsto
       \int_{\mathbb R}f(s)v_s e^{2\pi ixs}\,ds\right).
 \end{gathered}
 \tag{12.33}
\]
The trivial-action full tensor product is maximal initially; commutativity of \(C_0(\mathbb R)\) identifies it with the minimal product, as in Lemma 8.1. No norm continuity of \(v_t\) is needed. For \(v_t=e^{itk}\), \(k=k^*\in M(A)\), norm continuity follows from the exponential series. If \(k\) is scalar on a block, (12.33) translates that block's frequency by its scalar value divided by \(2\pi\). Naturality (12.24) identifies the Thom maps under this isomorphism with the trivial-action values in (12.31).

**An explicit moving matrix projection.** On \(A=M_2(\mathbb C)\), put \(k=\operatorname{diag}(0,c)\) for nonzero real \(c\), \(\alpha_t=\operatorname{Ad}e^{itk}\), and let \(f\) project onto \((1,1)/\sqrt2\). It is already smooth, with \(\delta(f)=i[k,f]\). The \(h\) of (12.15) is skew-adjoint, and
\[
 u_t=e^{t(ik+h)}e^{-itk}
 \tag{12.34}
\]
solves (12.17): differentiation cancels the \(ik\)-terms and leaves \(u_t e^{itk}h e^{-itk}\). Thus the perturbed action is \(\operatorname{Ad}e^{t(ik+h)}\). Since \([ik+h,f]=0\), it fixes \(f\). Formula (12.26) produces its transported K-one generator, and (12.27) identifies that class independently of this particular matrix calculation.

**An action on a compact amplification.** Let \(\eta_t=\alpha_t\otimes\operatorname{id}\) on \(A\otimes\mathcal K(H)\), and let \(v_t\) be a strongly continuous unitary group on \(H\). The multipliers \(w_t=1\otimes v_t\) are strictly continuous: check left and right multiplication on rank-one tensors, then use density. They are \(\eta\)-cocycles because \(\eta\) fixes them. Hence
\[
 \begin{gathered}
 (A\otimes\mathcal K(H))
       \rtimes_{\alpha\otimes\operatorname{Ad}v}\mathbb R\\
 \cong (A\otimes\mathcal K(H))\rtimes_\eta\mathbb R
 \cong (A\rtimes_\alpha\mathbb R)\otimes\mathcal K(H).
 \end{gathered}
 \tag{12.35}
\]
The first core map is \(g(s)\mapsto g(s)(1\otimes v_s)\); the second is the inactive-factor representation bijection of Lesson 8, with the compact tensor norm identification. This applies to the surviving Takai action \(\alpha\otimes\operatorname{Ad}\lambda\), even though the translation group is not norm continuous.

## Exercises with complete solutions

**Exercise 1 (basic).** Let \(v_t\) be a norm-continuous unitary group in \(M(A)\). Prove (12.33), including the map on the integrated core.

**Solution.** For the trivial action the cocycle identity is \(v_{s+t}=v_sv_t\), which is precisely the group law. Theorem 12.1 therefore maps the inner-action product to the trivial-action product by \(f(s)\mapsto f(s)v_s\), with inverse \(g(s)\mapsto g(s)v_s^*\). The full norm equality is the covariant-pair bijection: \(U_t\) implements the inner action exactly when \(v_t^*U_t\) commutes with the coefficient representation. The trivial crossed product is \(A\otimes_{\max}C^*(\mathbb R)\). Positive Fourier identifies the second factor with \(C_0(\mathbb R)\), whose maximal and minimal tensor norms agree. Its integrated formula is the integral in (12.33). This also proves surjectivity and injectivity of that completed map, rather than just verifying multiplication of kernels. ∎

**Exercise 2 (intermediate).** Verify the cocycle identity for the solution generated by \(h\) in (12.17), including negative times.

**Solution.** The integral equation on any interval is
\(u_b=u_a+\int_a^b u_t\alpha_t(h)\,dt\); it holds for \(b<a\) with the oriented integral. Fix arbitrary real \(s\). For every real \(t\), the derivative of \(u_s\alpha_s(u_t)\) is that function multiplied on the right by \(\alpha_{s+t}(h)\). It agrees at \(t=0\) with \(u_{s+t}\). The uniqueness estimate on a compact interval uses the uniformly bounded coefficient \(\|h\|\); Picard iteration bounds the difference by a factorial tail tending to zero. Therefore equality holds for positive and negative \(t\), and on all real times by increasing compact intervals. This proves \(u_s\alpha_s(u_t)=u_{s+t}\). ∎

**Exercise 3 (intermediate).** Show that the perturbed action fixes \(f\), without treating the unbounded derivation as a bounded operator on \(A\).

**Solution.** Differentiate only the known smooth orbit of \(f\). From \(f^2=f\), (12.14) gives
\([f\delta(f)-\delta(f)f,f]=-f\delta(f)-\delta(f)f=-\delta(f)\).
The norm differentiable functions \(u_t,\alpha_t(f),u_t^*\) can now be multiplied and differentiated. Their derivative is (12.18), hence zero. Integration on any real interval gives \(u_t\alpha_t(f)u_t^*=f\). This computes the needed orbit and does not assert a domain theorem for \(\delta+[h,\,\cdot\,]\). ∎

**Exercise 4 (advanced).** Prove that the transported class is independent of \(f\) and the fixing cocycle. Also describe the homotopy when two fixing cocycles are generated by bounded skew-adjoint perturbations of a fixed smooth \(f\).

**Solution.** For any smooth equivalent \(f\) and any strictly continuous fixing cocycle \(u\), naturality for \(z\mapsto zf\) gives the class \(\Gamma_\beta^0[f]\) before transport. The cocycle isomorphism of Wiener–Hopf extensions has ideal map \(\operatorname{Ad}W\), so it induces the identity on coefficient K-theory by (12.22). Boundary naturality and inversion then give (12.24). The transported class is consequently \(\Gamma_\alpha^0[f]=\Gamma_\alpha^0[p]\), independent of all choices.

For the additional homotopy let \(h_r=(1-r)h_0+rh_1\). It remains skew-adjoint and satisfies \([h_r,f]=-\delta(f)\). Solve (12.17) with this coefficient at each \(r\). The uniformly convergent Picard series makes the solution jointly continuous on compact parameter-time sets; uniqueness gives the cocycle identity; (12.18) gives fixation of \(f\). Finally the exponentially decaying kernels in (12.26) are continuous in coefficient \(L^1\)-norm by truncation and dominated tails, so their integrated unitaries give a norm homotopy. For varying smooth representatives arising from averaging, use the common contour path described above. The extension argument covers arbitrary additional strictly continuous fixing cocycles, for which a bounded-generator interpolation is not presumed. Relative projection differences and the split scalar quotient complete the nonunital case. ∎

**Exercise 5 (advanced).** For \(\Gamma=\mathbb Z^2\), the trivial action on \(\mathbb C\), and \(c\in\mathbb T\), put \(w((m,n),(p,q))=c^{np}\). Verify (12B.2), and prove that if \(c\ne1\) no scalar change of implementers makes this twist trivial.

**Solution.** For \(r=(a,b)\), the exponents in the two cocycle products are \(np+(n+q)a\) and \(qa+n(p+a)\), which are equal. Normalization is immediate; scalar multipliers act trivially by inner conjugation, so the automorphism condition holds too. For an abelian group a scalar change (12B.8) multiplies \(w(s,t)\) by \(v_sv_t\overline{v_{s+t}}\), a symmetric factor. Thus the ratio \(w(s,t)/w(t,s)\) is invariant. At \(s=(0,1),t=(1,0)\) it is \(c\), whereas a trivial twist has ratio one. In its covariant algebra the corresponding generators satisfy \(VU=cUV\). Stabilization removes the twist using noncommuting compact-operator multipliers, not scalar cochains. ∎

## What this lesson does not prove

We use the full integrated-form and ideal exactness results of Lesson 1, the regular norm construction of Lesson 2, positive C*-Fourier theory of Lesson 6, the tensor identities and Takai model of Lesson 8, and the Wiener–Hopf extension and fully proved inverse-boundary isomorphisms of Lessons 10–11. General K-theory foundations are the exact ones recorded in Lesson 10: unitization, matrix stability, homotopy invariance, split exactness, Bott periodicity and naturality of six-term boundaries. Holomorphic functional calculus and elementary norm-valued integral equations are used in the displayed proofs.

The normalized continuous twisted-action algebra, its regular norm, the full and reduced stabilization maps, and the projective example are proved here. No broader measurable or Green normal-subgroup twisted formulation is asserted by that theorem.

The source-convention double-duality compatibility (12.32), including its normalization calculation, is supplied by the specified bivariant KK product lesson identified above. Its arbitrary-coefficient extension is proved here. We have proved the choice independence and the comparison (12.27), (12.30) directly. We do not import KK-theoretic uniqueness to replace either proof.

[Connes 1994] A. Connes, *Noncommutative Geometry*, Chapter II, Appendix C, Definition 5 and Theorem 6, p. 178; Lemma 7 and Theorem 8, p. 179. [Author's electronic edition](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf). The product theorem is specified in (12.32), with its required bivariant proof identified above.

[Blackadar 1998] B. Blackadar, *K-Theory for Operator Algebras*, second edition, §19.3, Definition 19.3.3, Examples 19.3.4 and Theorem 19.3.6, pp. 191–192. These describe the Thom element, examples and the stronger separable KK equivalence. We prove cocycle compatibility directly through the Wiener–Hopf extension; it is not imported from those locators. [Author's second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf).

[Rosenberg 2012] J. Rosenberg, *Examples and applications of noncommutative geometry and K-theory*, in *Topics in Noncommutative Geometry*, pp. 93–129, §2.4, pp. 106–107. It discusses the projection perturbation and the KK approach as two routes to the Thom isomorphism. [Electronic volume](https://www.claymath.org/wp-content/uploads/2022/03/cmip016c.pdf).

[Meyer 2012] R. Meyer, *Actions of Higher Categories on C*-Algebras*, in [*Topics in Noncommutative Geometry*](https://www.claymath.org/wp-content/uploads/2022/03/cmip016c.pdf), 2012.

[Buss–Meyer–Zhu] A. Buss, R. Meyer and C. Zhu, [*A higher category approach to twisted actions on C*-algebras*](https://arxiv.org/abs/0908.0455v1), author preprint 2009; published 2013. The stabilization mechanism is the Packer–Raeburn trick.

