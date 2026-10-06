# Induced algebras and Green's imprimitivity theorem

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A representation of a subgroup can be spread over the cosets of that subgroup. Green's theorem does the same thing with a C*-algebra carrying a subgroup action. Its two crossed products act on opposite sides of one Hilbert module. We construct that module, including positivity and the norm estimates needed for the full completions.

Throughout, \(G\) is a locally compact Hausdorff group, \(H\subseteq G\) is closed, and \(\beta:H\to\operatorname{Aut}(A)\) is strongly continuous. The algebra \(A\) may be nonunital. No countability or amenability assumption is imposed. Fix left Haar measures \(dr\) and \(dh\), with the convention
\[
 \int q(rs)\,dr=\Delta_G(s)^{-1}\int q(r)\,dr,
 \qquad d\nu_G(r)=\Delta_G(r)^{-1}\,dr.
 \tag{7.1}
\]
Thus \(\nu_G\) is right Haar measure. In general \(\Delta_G|_H\ne\Delta_H\). All crossed products without a subscript are full crossed products, with the convolution and involution of Lesson 1.

## The induced algebra

Write \(q:G\to G/H\) for the quotient map. Define
\[
\begin{aligned}
 D&=\operatorname{Ind}_H^G(A,\beta)\\
  &=\{d\in C_b(G,A):d(rh)=\beta_h^{-1}(d(r)),\\
  &\hspace{5em}rH\mapsto\|d(r)\|\in C_0(G/H)\}.
\end{aligned}
 \tag{7.2}
\]
Its operations are pointwise and its norm is the supremum norm. The group acts by
\[
 (\operatorname{lt}_s d)(r)=d(s^{-1}r).
 \tag{7.3}
\]
For trivial scalar coefficients, \(D=C_0(G/H)\).

Here are the topological facts we need, with their proofs. The map \(q\) is open because \(q^{-1}(q(U))=UH\) is open for open \(U\subseteq G\). Distinct cosets have disjoint quotient neighborhoods: if \(r^{-1}s\notin H\), choose neighborhoods \(U\) of \(r\) and \(V\) of \(s\) with \(U^{-1}V\cap H=\varnothing\). Then \(q(U)\cap q(V)=\varnothing\). Images of relatively compact neighborhoods show that \(G/H\) is locally compact. Moreover, every compact \(T\subseteq G/H\) has a compact lift \(C\subseteq G\) with \(q(C)=T\): cover \(T\) by finitely many \(q(U_i)\), where the \(U_i\) are relatively compact, and take \(C=(\bigcup_i\overline U_i)\cap q^{-1}(T)\).

The right \(H\)-action on \(G\) is proper. Indeed, \((r,h)\mapsto(r,rh)\) is a homeomorphism onto the closed subset \(\{(r,s):r^{-1}s\in H\}\) of \(G\times G\). In particular, for compact \(C,K\subseteq G\), all \(h\) with \(r\in C\) and \(rh\in K\) belong to the compact set \(C^{-1}K\cap H\).

For \(f\in C_c(G,A)\), set
\[
 Qf(r)=\int_H\beta_h(f(rh))\,dh.
 \tag{7.4}
\]
Properness bounds the integration parameters on compact neighborhoods of \(r\), so this is norm-continuous. Substitution \(u=kh\) gives \(Qf(rk)=\beta_k^{-1}(Qf(r))\), and its quotient support is contained in \(q(\operatorname{supp}f)\). Thus \(Qf\in D\).

We will repeatedly use a scalar cutoff. Given compact \(T\subseteq G/H\), choose \(p\in C_c(G)_+\) such that
\(P(rH)=\int_H p(rh)\,dh\) is positive on \(T\). Such a \(p\) is obtained from finitely many nonnegative bumps positive at representatives of cosets covering \(T\). Choose \(\psi\in C_c(G/H)\), with \(0\le\psi\le1\), equal to \(1\) on \(T\), and supported where \(P>0\). Then
\[
 w(r)=p(r)\psi(rH)/P(rH),\qquad
 \int_Hw(rh)\,dh=\psi(rH).
 \tag{7.5}
\]
Extend \(w\) by zero where the denominator is zero. Its continuity follows because the denominator is bounded away from zero on \(\operatorname{supp}\psi\). In particular, \(w\in C_c(G)_+\).

Let \(D_c\) denote the elements of \(D\) having compact quotient support. Multiplication by scalar quotient cutoffs makes \(D_c\) dense in \(D\). For \(d\in D_c\), choose (7.5) with \(\psi=1\) on its quotient support. Equivariance gives \(Q(wd)=d\). This also proves that \(Q(C_c(G,A))\) is dense in \(D\). The defining conditions in (7.2) are closed under uniform limits, and the C*-identity holds pointwise; hence \(D\) is a C*-algebra.

The action (7.3) is strongly continuous. For \(d\in D_c\) and \(s\) in a fixed compact neighborhood of the identity, the quotient supports of \(\operatorname{lt}_s d-d\) lie in one compact subset. Take a compact lift of that subset. Equivariance lets us compute the supremum norm on this lift, where continuity of \(d(s^{-1}r)\) gives uniform convergence as \(s\to e\). Density proves the assertion for every \(d\in D\).

Evaluation at any \(r\) maps \(D\) onto \(A\). To see density of its range, fix \(a\in A\) and a small neighborhood \(V\subseteq H\) on which \(\beta_h(a)\) is close to \(a\). Choose a nonnegative bump \(p\) supported in an open set meeting \(rH\) only in \(rV\), and normalize \(\int_Hp(rh)\,dh=1\). Then \(Q(pa)(r)\) is arbitrarily close to \(a\). The range of a C*-homomorphism is closed, so evaluation is onto.

## Four formulas, with both modular functions

Put
\[
 E=D\rtimes_{\operatorname{lt}}G,\qquad B=A\rtimes_\beta H,
 \qquad X_0=C_c(G,A).
 \tag{7.6}
\]
Use \(B_0=C_c(H,A)\). For \(E_0\), use the continuous functions \(c(t,r)\) satisfying \(c(t,rh)=\beta_h^{-1}(c(t,r))\) and having support in \(K\times q^{-1}(T)\), for compact \(K\subseteq G\), \(T\subseteq G/H\). Compact lifts show that \(t\mapsto c(t,\cdot)\) is norm-continuous. These functions form a dense *-subalgebra of \(C_c(G,D)\): approximate a compact set of coefficient values by a common quotient cutoff, and use finite sums of scalar functions of \(t\) times elements of \(D_c\). Its convolution and star are
\[
 (c*d)(t,r)=\int_Gc(v,r)d(v^{-1}t,v^{-1}r)\,dv,
 \quad c^*(t,r)=\Delta_G(t)^{-1}c(t^{-1},t^{-1}r)^*.
 \tag{7.7}
\]
Convergence in the inductive limit topology below means uniform convergence with all supports in one fixed compact set; for \(E_0\), the fixed compact set is in \(G\times G/H\). It implies convergence in the crossed-product norm by the \(L^1\) bound.

For \(c\in E_0\), \(b\in B_0\), and \(x,y\in X_0\), define
\[
 (c x)(r)=\int_G c(t,r)x(t^{-1}r)\Delta_G(t)^{1/2}\,dt,
 \tag{7.8}
\]
\[
 (x b)(r)=\int_H\beta_h^{-1}(x(rh^{-1})b(h))\Delta_H(h)^{-1/2}\,dh,
 \tag{7.9}
\]
\[
 R(x,y)(h)=\Delta_H(h)^{-1/2}
       \int_Gx(r)^*\beta_h(y(rh))\,d\nu_G(r),
 \tag{7.10}
\]
\[
 L(x,y)(t,r)=\Delta_G(t)^{-1/2}
       \int_H\beta_h(x(rh)y(t^{-1}rh)^*)\,dh.
 \tag{7.11}
\]
The right inner product \(R\) is linear in its second variable; the left inner product \(L\) is linear in its first variable. This choice of half densities is particularly convenient for an arbitrary \(H\)-action. The formulas agree with the untwisted induced-algebra form of Green's theorem; see [Williams]. We prove the theorem from them rather than assume that theorem.

All four expressions have the indicated ranges. For example, if \(K_x,K_y\) are the supports of \(x,y\), then the support of \(R(x,y)\) is contained in \(K_x^{-1}K_y\cap H\). The support of \(L(x,y)\) is contained in \((K_xK_y^{-1})\times q(K_x)\). Its equivariance follows by changing \(h\) to \(k^{-1}h\) in its value at \(rk\). To check continuity uniformly in \(r\), take a compact lift of \(q(K_x)\) and use properness to bound \(h\). The same compact-support bounds prove continuity of every expression and its continuity for inductive limit convergence. Products in (7.8) and (7.9) have compact support contained, respectively, in \(K K_x\) and \(K_x\operatorname{supp}b\).

**Lemma 7.1 (Algebraic identities).** The actions are associative and commute. Moreover,
\[
\begin{gathered}
 R(x,yb)=R(x,y)*b,\qquad L(cx,y)=c*L(x,y),\\
 R(x,y)^*=R(y,x),\qquad L(x,y)^*=L(y,x),\\
 R(cx,y)=R(x,c^*y),\qquad L(xb,y)=L(x,yb^*),\\
 L(x,y)z=xR(y,z).
\end{gathered}
 \tag{7.12}
\]

**Proof.** Introduce coefficient multiplications and translations
\[
\begin{aligned}
 M_d x(r)&=d(r)x(r),\quad v_sx(r)=\Delta_G(s)^{1/2}x(s^{-1}r),\\
 V_hx(r)&=\Delta_H(h)^{-1/2}\beta_h^{-1}(x(rh^{-1})).
\end{aligned}
 \tag{7.13}
\]
The \(v_s\) form a group representation, \(V_kV_h=V_{hk}\), and
\(V_h(xa)=(V_hx)\beta_h^{-1}(a)\). If \(R_a x=xa\), then \(R_aR_b=R_{ba}\) and \(V_hR_a=R_{\beta_h^{-1}(a)}V_h\). The multiplications \(M_d\) commute with the \(V_h\) because \(d(rh^{-1})=\beta_h(d(r))\); left translations commute with the \(V_h\) and with right coefficient multiplication. Also \(v_sM_dv_{s^{-1}}=M_{\operatorname{lt}_s d}\). Integrating these identities proves associativity and commutation in (7.8)–(7.9), using Fubini on the compact integration sets.

For right linearity of \(R\), expand (7.9) inside (7.10). In the convolution \(R(x,y)*b\), substitute \(k=ht^{-1}\). Inversion gives \(dk=\Delta_H(t)^{-1}dt\), and
\[
 \Delta_H(k)^{-1/2}dk
   =\Delta_H(h)^{-1/2}\Delta_H(t)^{-1/2}dt.
 \tag{7.14}
\]
The two integrands are then both
\(x(r)^*\beta_{ht^{-1}}(y(rht^{-1})b(t))\), with exactly the same measures and scalar factor. For left linearity of \(L\), expand \(cx\). Equivariance moves \(\beta_h(c(v,rh))\) to \(c(v,r)\), and
\(\Delta_G(v^{-1}t)^{-1/2}=\Delta_G(t)^{-1/2}\Delta_G(v)^{1/2}\); this is precisely (7.7).

For the right adjoint identity, the crossed-product star gives
\[
 R(x,y)^*(h)=\Delta_H(h)^{-1/2}
   \int_G y(rh^{-1})^*\beta_h(x(r))\,d\nu_G(r).
\]
Substitute \(u=rh^{-1}\); right invariance of \(\nu_G\) gives \(R(y,x)(h)\). For the left adjoint identity, substitute (7.11) into (7.7). Its two modular factors combine as
\(\Delta_G(t)^{-1}\Delta_G(t^{-1})^{-1/2}=\Delta_G(t)^{-1/2}\), leaving \(L(y,x)\).

The adjoint relation for the left action can also be checked before integration: \(M_d\) has formal adjoint \(M_{d^*}\) for \(R\), by equivariance, and \(v_s\) has formal adjoint \(v_{s^{-1}}\), because \(d\nu_G(su)=\Delta_G(s)^{-1}d\nu_G(u)\). Integration gives the relation for \(c\). For \(L\), right multiplication by \(a\) has formal adjoint right multiplication by \(a^*\). Substitution \(k=uh\), with \(dk=\Delta_H(h)du\), gives
\(L(V_hx,y)=L(x,V_{h^{-1}}y)\). Integration, with the star on \(B_0\), proves the relation for \(b\).

Finally, substitute (7.11) into (7.8). Its \(\Delta_G(t)\) factors cancel, giving
\[
 (L(x,y)z)(r)=\int_H\int_G
  \beta_h(x(rh)y(t^{-1}rh)^*)z(t^{-1}r)\,dt\,dh.
 \tag{7.15}
\]
Put \(u=t^{-1}rh\); inversion followed by left translation gives \(dt=d\nu_G(u)\). The integrand becomes
\(\beta_h(x(rh)y(u)^*)z(uh^{-1})\). Inverting the variable in (7.9) gives the equivalent formula
\[
 (xb)(r)=\int_H\beta_h(x(rh)b(h^{-1}))\Delta_H(h)^{-1/2}\,dh.
 \tag{7.16}
\]
For \(b=R(y,z)\), its factor \(\Delta_H(h^{-1})^{-1/2}\) cancels the factor in (7.16). This produces exactly the preceding double integral. All changes of variables take place on compact supports, so Fubini is justified. ∎

## Constructing the positive approximate identities

Positivity of (7.10) and (7.11) in the full C*-algebras is an essential step. It does not follow by inspecting their values at individual group elements. We first construct approximate identities out of their diagonal terms, without presupposing positivity.

**Lemma 7.2.** There are nets
\[
 e_i=\sum_{j=1}^{n_i}L(w_{ij},w_{ij})\in E_0,
 \qquad b_k=R(z_k,z_k)\in B_0
 \tag{7.17}
\]
which are two-sided approximate identities on \(E_0\) and \(B_0\), respectively, in the inductive limit topology. They also satisfy \(e_i x\to x\) and \(xb_k\to x\) in that topology for every \(x\in X_0\).

**Proof.** First, multiplication by \(D\) is nondegenerate on \(X_0\) in this topology. For compact \(K\supseteq\operatorname{supp}x\), take \(w\) from (7.5) with quotient average \(1\) on \(q(K)\). If \(a\) is a positive contraction in a contractive approximate identity of \(A\), then \(d=Q(wa)\) is a positive contraction in \(D\). For \(r\in K\), the relevant \(h\)'s lie in one compact set. The family \(\beta_h^{-1}(x(r))\) is compact in \(A\), so
\[
 d(r)x(r)-x(r)
  =\int_Hw(rh)\beta_h\bigl(a\beta_h^{-1}(x(r))-\beta_h^{-1}(x(r))\bigr)\,dh
\]
converges uniformly to zero. The support stays in \(K\). It follows that any contractive approximate identity of \(D\) acts in the same way: approximate \(x\) first by \(dx\), and then use \(a_i d\to d\) in the norm of \(D\).

We construct the left net. Fix compact \(T\subseteq G/H\), a small relatively compact neighborhood \(U\) of \(e\) in \(G\), a positive contraction \(a\) from an approximate identity of \(D\), and \(\delta>0\). Take a compact lift of \(T\) and a compact neighborhood \(C\) of that lift. Choose \(\phi\in C_c(G)\), equal to \(1\) on \(C\), and put \(z(r)=\phi(r)a(r)^{1/2}\). After shrinking a neighborhood of \(e\), continuity on compact sets ensures
\[
 \|z(r)z(t^{-1}r)^*-a(r)\|<\delta
 \quad(r\in C,\ t\text{ in that neighborhood}).
 \tag{7.18}
\]
Choose finitely many nonnegative bumps \(h_j\) supported in open sets \(V_j\subseteq C\) such that \(V_jV_j^{-1}\subseteq U\) and also within the neighborhood in (7.18). Arrange that the quotient average of \(\sum h_j\) is positive on \(T\). Normalize, exactly as in (7.5), to obtain functions \(k_j\ge0\), supported in \(V_j\), with
\[
 \sum_j\int_H k_j(rh)\,dh=\psi(rH),\quad
 0\le\psi\le1,\quad \psi|_T=1.
 \tag{7.19}
\]
Discard the zero functions. Let \(c_j=\int_G k_j\,d\nu_G>0\), \(g_j=k_j/\sqrt{c_j}\), and \(w_j=g_jz\). Put \(e=\sum_jL(w_j,w_j)\) and \(\widetilde e(t,r)=\Delta_G(t)^{1/2}e(t,r)\). If
\(F(t,r)=\sum_jg_j(r)g_j(t^{-1}r)\), then
\[
 \widetilde e(t,r)=\int_H F(t,rh)
   \beta_h(z(rh)z(t^{-1}rh)^*)\,dh.
 \tag{7.20}
\]
The function \(F\) is nonnegative and supported where \(t\in U\). Inversion gives
\(\int_Gg_j(t^{-1}r)\,dt=\int_Gg_j\,d\nu_G=\sqrt{c_j}\). Consequently
\[
 \int_G\int_HF(t,rh)\,dh\,dt=\psi(rH).
 \tag{7.21}
\]
On the support of \(F(t,rh)\), the point \(rh\) belongs to \(C\); (7.18) applies. Since \(\beta_h(a(rh))=a(r)\), (7.20)–(7.21) imply
\[
 \int_G\|\widetilde e(t,r)\|\,dt\le1+\delta,
 \quad
 \left\|\int_G\widetilde e(t,r)\,dt-a(r)\right\|\le\delta
       \quad(rH\in T).
 \tag{7.22}
\]
These are pointwise-in-\(r\) integral bounds; no interchange of supremum and integral is needed.

For a specified \(x\), take \(T\) containing \(q(U_0\operatorname{supp}x)\), where \(U_0\) is a fixed compact neighborhood and \(U\subseteq U_0\). Formula (7.8) becomes \(ex(r)=\int\widetilde e(t,r)x(t^{-1}r)\,dt\). Its error from \(x\), uniformly in \(r\), is at most
\[
 (1+\delta)\sup_{t\in U,r}\|x(t^{-1}r)-x(r)\|
      +\delta\|x\|_\infty+\|ax-x\|_\infty.
 \tag{7.23}
\]
All terms tend to zero as \(U\) shrinks, \(\delta\) decreases and the approximate identity advances. The supports stay in \(U_0\operatorname{supp}x\).

For \(c\in E_0\), the same expansion of \((e*c)(v,r)\) uses
\(c(t^{-1}v,t^{-1}r)\) in place of \(x(t^{-1}r)\). Its difference from \(c(v,r)\) tends uniformly to zero for \(t\to e\): use compact lifts of the joint quotient support and continuity there. Also \(a c(v,\cdot)\to c(v,\cdot)\) uniformly for \(v\) in its compact support. Replacing \(\widetilde e\) by \(e\) adds an error bounded by
\(\sup_{t\in U}|\Delta_G(t)^{-1/2}-1|(1+\delta)\|c\|_\infty\).
Thus \(e*c\to c\) uniformly, with supports in fixed compact subsets of \(G\times G/H\). Every \(e\) is self-adjoint by Lemma 7.1, so \(c*e\to c\) too.

For the right net, take a positive contraction \(a\) from an approximate identity of \(A\). Choose a small neighborhood \(U\subseteq H\) on which \(\beta_h(a^{1/2})\) is uniformly close to \(a^{1/2}\), and on which the modular functions are close to \(1\). There is a relatively compact neighborhood \(V\subseteq G\) with \(V^{-1}V\cap H\subseteq U\). Choose \(p\in C_c(G)_+\), supported in \(V\) and positive at \(e\). Set
\[
 q_0(h)=\Delta_H(h)^{-1/2}\int_Gp(r)p(rh)\,d\nu_G(r),
 \quad m=\int_Hq_0(h)\,dh>0,\quad q=q_0/m.
 \tag{7.24}
\]
Then \(q\ge0\), \(\int q=1\), and its support is in \(U\). For \(z(r)=p(r)a^{1/2}/\sqrt m\),
\[
 b(h)=R(z,z)(h)=q(h)a^{1/2}\beta_h(a^{1/2}),\qquad \|b\|_1\le1.
 \tag{7.25}
\]
Its \(L^1\) distance from \(q(h)a\) is as small as the chosen variation of \(\beta_h(a^{1/2})\). More explicitly,
\((b*c)(k)-c(k)\) is bounded uniformly by the sum of that variation times \(\|c\|_\infty\),
\(\sup_{h\in U,k}\|\beta_h(c(h^{-1}k))-c(k)\|\), and
\(\sup_k\|a c(k)-c(k)\|\).
The first two terms tend to zero as \(U\) shrinks; the last tends to zero because the range of \(c\) is compact. Supports stay in \(U_0\operatorname{supp}c\). Hence \(b*c\to c\) in the inductive limit topology. Self-adjointness gives the other side.

Likewise, expand \(xb\) in (7.9). The variations of \(\Delta_H(h)^{-1/2}\), \(\beta_h^{-1}(a)\), and \(\beta_h^{-1}(x(rh^{-1}))\) are uniformly small on the relevant compact sets. The expression tends uniformly to \(x(r)a\), which tends uniformly to \(x(r)\); supports stay in \(\operatorname{supp}x\,U_0\). This proves the module assertion. Direct the constructions by finite sets of functions, compact support bounds, shrinking neighborhoods and decreasing errors. They therefore give nets satisfying all the asserted limits simultaneously, without assuming a countable neighborhood basis. ∎

**Proposition 7.3 (Positivity and fullness).** The diagonal inner products are positive in \(B\) and \(E\). The linear spans of the ranges of \(R\) and \(L\) are dense in \(B\) and \(E\), respectively.

**Proof.** Lemmas 7.1–7.2 give, in the full norms,
\[
\begin{aligned}
 R(x,x)&=\lim_i\sum_j R(w_{ij},x)^*R(w_{ij},x)\ge0,\\
 L(x,x)&=\lim_k L(x,z_k)L(x,z_k)^*\ge0.
\end{aligned}
 \tag{7.26}
\]
For the first equality use \(L(w,w)x=wR(w,x)\); for the second use \(xR(z,z)=L(x,z)z\). The positive cones of C*-algebras are closed. The span of the \(L\)'s is a *-ideal in \(E_0\), by left linearity and adjoints, and contains the \(e_i\). Since \(e_i*c\to c\), its closure is \(E\). The same argument with \(R\) and \(b_k\) proves fullness in \(B\). ∎

## Completion in the full crossed-product norms

We use the following Hilbert-module prerequisites in their precise forms. A positive finite Gram matrix gives Cauchy–Schwarz and a continuous inner product on the null quotient; completing a pre-Hilbert module gives a Hilbert module. Interior tensor products and their associativity are available. The compact operators on an exterior tensor product satisfy
\(\mathcal K(P\boxtimes Q)\cong\mathcal K(P)\otimes_{\min}\mathcal K(Q)\).
Proofs are in Hilbert C*-modules, Theorems 2.1–2.3 and 3.1 and Tensor products and C*-correspondences, Theorems 1.2, 3.1 and 5.1. The dense coefficient algebras in our construction require the following small precaution.

For \(x_1,\ldots,x_n\in X_0\) and \(b_i\in B_0\),
\[
 \sum_{i,j}b_i^*R(x_i,x_j)b_j
   =R\left(\sum_i x_i b_i,\sum_jx_jb_j\right)\ge0.
 \tag{7.27}
\]
Density of \(B_0\) extends this inequality to arbitrary \(b_i\in B\), so the matrix positivity test makes \((R(x_i,x_j))\) positive in \(M_n(B)\). A positive two-by-two matrix \(\begin{pmatrix}a&c\\c^*&b\end{pmatrix}\) satisfies
\(b\ge c^*(a+\varepsilon1)^{-1}c\), by multiplying by a triangular matrix in the unitization. Since \((a+\varepsilon1)^{-1}\ge(\|a\|+\varepsilon)^{-1}1\), letting \(\varepsilon\downarrow0\) gives \(c^*c\le\|a\|b\). Thus Cauchy–Schwarz is valid here without assuming that \(X_0\) already admits multiplication by inverses outside \(B_0\).

The same argument applies to the left form, using
\(\sum c_i^*L(x_i,x_j)c_j=L(\sum c_i^*x_i,\sum c_j^*x_j)\) for \(c_i\in E_0\).
Consequently the two seminorms
\[
 \|x\|_R=\|R(x,x)\|^{1/2},\qquad
 \|x\|_L=\|L(x,x)\|^{1/2}
 \tag{7.28}
\]
satisfy the triangle inequality and Cauchy–Schwarz. For \(b\in B_0\),
\(R(xb,xb)=b^*R(x,x)b\), so \(\|xb\|_R\le\|x\|_R\|b\|_B\). The right completion therefore admits the entire coefficient algebra \(B\), by density, and is a Hilbert \(B\)-module. Likewise the conjugate of the left completion is a Hilbert \(E\)-module. Inductive limit convergence implies convergence in both seminorms, by continuity of the formulas and the \(L^1\) bound.

**Theorem 7.4 (Green imprimitivity).** There is an \(E\)-\(B\) imprimitivity bimodule \(X\), obtained by the null quotient and completion of \(X_0\) in (7.28). The two seminorms coincide, and left multiplication identifies
\[
 \operatorname{Ind}_H^G(A,\beta)\rtimes_{\operatorname{lt}}G
       \cong\mathcal K_B(X).
 \tag{7.29}
\]
In particular, the two full crossed products \(E\) and \(B\) are strongly Morita equivalent.

**Proof.** We first bound the left action in the full norm on the right completion. For \(d\in D\), the function
\(\psi(r)=(\|d\|^2 1-d(r)^*d(r))^{1/2}\), formed in the unitization of \(A\), is norm-continuous and equivariant. Although \(\psi\) need not lie in \(D\), the product \(\psi x\) lies in \(X_0\). Direct substitution into (7.10) gives
\[
 \|d\|^2R(x,x)-R(M_dx,M_dx)=R(\psi x,\psi x)\ge0.
 \tag{7.30}
\]
Thus \(M_d\) is bounded by \(\|d\|\), with adjoint \(M_{d^*}\). The \(v_s\) in (7.13) are unitaries for the right form: in \(R(v_sx,v_sy)\), substitution \(r=su\) multiplies \(d\nu_G\) by \(\Delta_G(s)^{-1}\), canceling the two half densities. They are strongly continuous because translations of compactly supported functions converge in the inductive limit topology. The nondegeneracy of \(M\) was proved in Lemma 7.2. The pair \((M,v)\) is covariant, so the full crossed-product universal property for Hilbert modules, proved in Lesson 1, gives a *-homomorphism
\(E\to\mathcal L_B(X_R)\), extending (7.8). In particular,
\[
 \|cx\|_R\le\|c\|_E\|x\|_R.
 \tag{7.31}
\]

For the other norm, work on the conjugate of the left completion. Its vectors are written \(\bar x\), with
\(\langle\bar x,\bar y\rangle_E=L(x,y)\) and \(\bar x c=\overline{c^*x}\). Define
\[
 \pi(a)\bar x=\overline{x a^*},\qquad
 W_h\bar x=\overline{V_{h^{-1}}x}
       =\Delta_H(h)^{1/2}\overline{\beta_h(x(\,\cdot\,h))}.
 \tag{7.32}
\]
Right multiplication by \(a\) is bounded for the left form: if
\(u=(\|a\|^2 1-aa^*)^{1/2}\), then
\(\|a\|^2 L(x,x)-L(xa,xa)=L(xu,xu)\ge0\).
It has the formal adjoint already checked in Lemma 7.1. Formula (7.32) therefore makes \(\pi\) a *-representation. It is nondegenerate because \(xa_i\to x\) uniformly on a fixed compact support for an approximate identity of \(A\).

The \(V_h\) preserve the left form. In (7.11), replace the integration variable \(k\) by \(uh\); the Haar factor \(\Delta_H(h)\) cancels the two factors \(\Delta_H(h)^{-1/2}\). Thus the \(W_h\) are unitaries. They form a group representation, are strongly continuous by compact-support continuity, and satisfy
\(W_h\pi(a)W_h^*=\pi(\beta_h(a))\), by (7.13). Their integrated representation of the full algebra \(B\) is
\[
 (\pi\rtimes W)(b)\bar x=\overline{x b^*}.
 \tag{7.33}
\]
For clarity, the integrand on the left is \(\pi(b(h))W_h\bar x\). Substitution of
\(b^*(h^{-1})=\Delta_H(h)\beta_h^{-1}(b(h)^*)\) into (7.16) proves (7.33). Consequently
\[
 \|xb\|_L\le\|x\|_L\|b\|_B.
 \tag{7.34}
\]
Both estimates concern the full C*-norms, rather than only the integral norms.

Now take \(p=L(x,x)\ge0\), \(q=R(x,x)\ge0\). Compatibility gives \(px=xq\). Right linearity and (7.31) give
\[
 \|q\|^3=\|xq\|_R^2=\|px\|_R^2\le\|p\|^2\|q\|.
 \tag{7.35}
\]
Left linearity and (7.34) give
\[
 \|p\|^3=\|px\|_L^2=\|xq\|_L^2\le\|q\|^2\|p\|.
 \tag{7.36}
\]
If either is zero, these inequalities force the other to be zero. Otherwise division proves \(\|p\|=\|q\|\). Hence the completions coincide; call the resulting module \(X\). Cauchy–Schwarz extends both forms continuously to \(X\), and all identities in (7.12) pass to limits.

The left action sends \(L(x,y)\) to the rank-one operator
\(\theta_{x,y}(z)=xR(y,z)\). Proposition 7.3 makes their span dense in \(E\); thus the entire image lies in \(\mathcal K_B(X)\). Conversely their images span a dense subspace of \(\mathcal K_B(X)\). The image of a C*-homomorphism is closed, so the map is onto. If \(cX=0\), then \(cL(x,y)=L(cx,y)=0\) for every \(x,y\). Fullness of the left form gives \(cE=0\), hence \(c=0\). The map is injective. Fullness of the right form, already established, finishes the imprimitivity assertion. ∎

## A useful change of density

For comparisons and examples, replace the old vector \(f\in X_0\) by \(f(r)=\Delta_G(r)^{1/2}x(r)\), and set
\[
 \kappa(h)=\left(\frac{\Delta_G(h)}{\Delta_H(h)}\right)^{1/2}.
 \tag{7.37}
\]
Transporting (7.8)–(7.11) gives the equivalent formulas
\[
\begin{aligned}
 (c x)(r)&=\int_Gc(t,r)x(t^{-1}r)\,dt,\\
 (x b)(r)&=\int_H\kappa(h)\beta_h(x(rh)b(h^{-1}))\,dh,\\
 R(x,y)(h)&=\kappa(h)\int_Gx(r)^*\beta_h(y(rh))\,dr,\\
 L(x,y)(t,r)&=\frac{\Delta_G(r)}{\Delta_G(t)}
       \int_H\Delta_G(h)\beta_h(x(rh)y(t^{-1}rh)^*)\,dh.
\end{aligned}
 \tag{7.38}
\]
The symbols \(R,L\) now refer to these transported forms. The raw change of vector is bijective on \(C_c(G,A)\) and preserves the completed inner products, so it introduces no new completion. For instance, the two vector factors in the right form contribute
\(\Delta_G(r)^{1/2}\Delta_G(rh)^{1/2}\); combined with \(d\nu_G(r)=\Delta_G(r)^{-1}dr\), they leave \(\Delta_G(h)^{1/2}\). The last line follows in the same way from
\(\Delta_G(t^{-1}rh)^{1/2}=\Delta_G(t)^{-1/2}\Delta_G(r)^{1/2}\Delta_G(h)^{1/2}\).
The left group unitary in these coordinates is simply \(x(r)\mapsto x(s^{-1}r)\).

## Translation gives compact operators for every group

Take \(H=\{e\}\), with the singleton Haar measure of mass \(1\). Then (7.2) is \(C_0(G,A)\), and (7.38) gives
\[
 R(x,y)=\int_Gx(r)^*y(r)\,dr.
 \tag{7.39}
\]
Thus \(X\) is the exterior Hilbert module \(L^2(G)\boxtimes A\), often denoted \(L^2(G)\otimes A\). Finite sums of scalar compactly supported functions times elements of \(A\) are dense in \(C_c(G,A)\) on fixed compact supports, and hence dense in this completion. The coefficient representation is multiplication, and the group representation is left translation. Theorem 7.4 and the exterior compact-algebra theorem yield
\[
 C_0(G,A)\rtimes_{\operatorname{lt}}G
   \cong\mathcal K_A(L^2(G)\boxtimes A)
   \cong\mathcal K(L^2(G))\otimes_{\min}A.
 \tag{7.40}
\]
Here \(\mathcal K_A(A)=A\): the rank-one maps on the standard module \(A\) are multiplication by \(ab^*\), and these products have dense span in \(A\). Neither unitality of \(A\) nor separability of \(L^2(G)\) is needed.

For \(A=\mathbb C\), (7.40) is the Stone–von Neumann–Mackey theorem in crossed-product form:
\[
 C_0(G)\rtimes_{\operatorname{lt}}G\cong\mathcal K(L^2(G)).
 \tag{7.41}
\]
It includes nonamenable groups. It also identifies all nondegenerate representations of the covariant system with amplifications of multiplication and left translation. To check the last assertion directly, choose an orthonormal basis \((e_i)\) of \(L^2(G)\) and a basis vector \(e_o\). For a nondegenerate representation \(\rho\) of the compact algebra, set \(K=\rho(\theta_{e_o,e_o})\mathcal H\). The map \(e_i\otimes v\mapsto\rho(\theta_{e_i,e_o})v\) is an isometry on finite sums, by the matrix-unit relations. Finite-rank projections converge strongly to the identity under a nondegenerate representation, so the map is onto. It intertwines every rank-one operator, hence every compact operator. The canonical coefficient and group multipliers are then intertwined too, by their unique strict extensions.

## Finite coset spaces and mapping tori

If \(G/H\) consists of \(n\) cosets, then it is a finite Hausdorff space, hence discrete, so \(H\) is open. Normalize Haar measure on \(G\) so its restriction to \(H\) is the chosen Haar measure on \(H\). Right translation of functions supported in \(H\) shows \(\Delta_G|_H=\Delta_H\), so \(\kappa=1\). Choose representatives \(s_1,\ldots,s_n\) for the cosets \(s_jH\). In the coordinates (7.38), put
\[
 T_jx(h)=\beta_h(x(s_jh))\in C_c(H,A).
 \tag{7.42}
\]
Substitution in the right action gives \(T_j(xb)=(T_jx)*b\). Moreover, expanding the star and convolution and then putting \(u=h^{-1}\) gives
\[
 (T_jx)^**(T_jy)(k)
  =\int_Hx(s_ju)^*\beta_k(y(s_juk))\,du.
 \tag{7.43}
\]
Summing over the cosets gives \(R(x,y)\). The map \(x\mapsto(T_jx)_j\) is onto \(B_0^n\): recover \(x(s_jh)=\beta_h^{-1}(b_j(h))\), a continuous compactly supported function because the cosets are open. It therefore extends to a unitary \(X\cong B^n\). Taking compact operators in (7.29) gives the concrete isomorphism
\[
 \operatorname{Ind}_H^G(A,\beta)\rtimes G\cong M_n(A\rtimes H).
 \tag{7.44}
\]
This matrix description depends on the representatives. For a finite group with scalar coefficients, it is \(C(G/H)\rtimes G\cong M_n(C^*(H))\).

Now let \(G=\mathbb R\), \(H=\mathbb Z\), and \(\beta_n=\alpha^n\). The induced functions satisfy \(f(t+n)=\alpha^{-n}(f(t))\). Restriction to \([0,1]\) identifies this algebra with
\[
 M_{\alpha^{-1}}=\{F\in C([0,1],A):F(1)=\alpha^{-1}(F(0))\}.
 \tag{7.45}
\]
The inverse extends \(F\) using the displayed covariance, which is continuous at the integers by the endpoint relation. To use the mapping-torus convention \(M_\alpha\) from Lesson 5, instead set \(F(t)=f(-t)\). Then \(F(t+n)=\alpha^n(F(t))\), so \(F(1)=\alpha(F(0))\). Under this isomorphism left translation becomes
\[
 (\tau_rF)(t)=F(t+r),
 \tag{7.46}
\]
where \(F\) is extended to the whole real line with that covariance. Therefore Green's theorem gives
\[
 A\rtimes_\alpha\mathbb Z\ \sim_M\ M_\alpha\rtimes_\tau\mathbb R.
 \tag{7.47}
\]
For \(A=\mathbb C\), this yields
\(C(\mathbb R/\mathbb Z)\rtimes\mathbb R\sim_M C^*(\mathbb Z)\cong C(\mathbb T)\).
This is a Morita equivalence; the compact-operator theorem (7.41) concerns the different translation space \(\mathbb R\) itself.

## Induction and Mackey's theorem

We now apply two general Hilbert-module results: inverse evaluation from *Imprimitivity bimodules and Morita equivalence*, Theorem 3.2 and the representation equivalence from *The Rieffel correspondence and induced representations*, Theorem 3.1. Let \(\bar X\) be the conjugate of the Green module, with
\[
 b\bar x=\overline{x b^*},\quad \bar x c=\overline{c^*x},
 \quad \langle\bar x,\bar y\rangle_E=L(x,y).
 \tag{7.48}
\]
The inverse-evaluation theorem supplies the following unitary bimodule maps for its particular inner products:
\[
\begin{aligned}
 \bar X\otimes_E X&\longrightarrow B,&\quad \bar x\otimes y&\longmapsto R(x,y),\\
 X\otimes_B\bar X&\longrightarrow E,&\quad x\otimes\bar y&\longmapsto L(x,y).
\end{aligned}
 \tag{7.49}
\]
If \(\rho\) is a nondegenerate representation of \(B\) on \(K\), let
\[
 \operatorname{Ind}_X\rho(c)(x\otimes v)=(cx)\otimes v
 \quad\text{on }X\otimes_\rho K.
 \tag{7.52}
\]
Nondegeneracy follows from Lemma 7.2. The cited representation theorem says that induction through \(\bar X\) is its inverse, and that tensoring with \(X\) gives isometric bijections on bounded intertwiner spaces. Thus the recovered representation is unique up to unitary equivalence. The remaining task here is to identify this tensor induction with the analytic function model for the subgroup \(H\subseteq G\).

For \(A=\mathbb C\), a representation of \(B=C^*(H)\) is the integrated form of a strongly continuous unitary representation \(\sigma\) of \(H\). A representation of \(E=C_0(G/H)\rtimes G\) is a nondegenerate covariant pair \((M,U)\). Such a pair is a continuous system of imprimitivity over \(G/H\):
\[
 U_sM(\varphi)U_s^*=M(\varphi(s^{-1}\,\cdot\,)),\qquad
       \varphi\in C_0(G/H).
 \tag{7.53}
\]
The unitary group representation induced from \(\sigma\) is the group part of (7.52), with \(U_s(x\otimes v)=x(s^{-1}\,\cdot\,)\otimes v\) in (7.38), and \(M(\varphi)(x\otimes v)=(\varphi\circ q)x\otimes v\).

Here is its usual function model, derived without assuming a measurable or continuous cross-section. Let \(\mathcal F_0\) consist of continuous \(K\)-valued functions of compact quotient support satisfying
\[
 F(rh)=\kappa(h)^{-1}\sigma_h^{-1}F(r).
 \tag{7.54}
\]
For \(F,J\in\mathcal F_0\), choose a nonnegative cutoff \(w\in C_c(G)\) with \(Pw(rH)=\int_Hw(rh)dh=1\) on their quotient supports, and put
\[
 \langle F,J\rangle=\int_Gw(r)\langle F(r),J(r)\rangle_K\,dr.
 \tag{7.55}
\]
The result is independent of \(w\). To check this, write \(a(r)=\langle F(r),J(r)\rangle\), so \(a(rh)=\kappa(h)^{-2}a(r)\). If \(p\) is another such cutoff, substitution \(u=rh\) gives
\[
\begin{aligned}
 \int_Gp(r)a(r)Pw(rH)\,dr
 &=\int_G\int_Hp(r)a(r)w(rh)\,dh\,dr\\
 &=\int_Ga(u)w(u)\int_Hp(uh^{-1})\Delta_H(h)^{-1}\,dh\,du\\
 &=\int_Ga(u)w(u)Pp(uH)\,du.
\end{aligned}
 \tag{7.56}
\]
The middle factor uses \(\kappa(h)^2\Delta_G(h)^{-1}=\Delta_H(h)^{-1}\). Both quotient averages are \(1\) where \(a\ne0\), proving independence. Positivity follows from \(w\ge0\). If \(F(r)\ne0\), its value stays nonzero everywhere on \(rH\), and \(Pw(rH)=1\) makes \(w\) positive at some point of that orbit. Continuity and full support of Haar measure make the integral strictly positive. Thus (7.55) is an inner product. Let \(\mathcal F\) be its Hilbert-space completion.

For scalar \(x\in C_c(G)\), define
\[
 S(x\otimes v)(r)=\int_H\kappa(h)x(rh)\sigma_hv\,dh.
 \tag{7.57}
\]
Substitution \(h=k^{-1}u\) proves (7.54). Balancing follows by expanding the second line of (7.38): put \(u=kh\) in the double integral. Right translation contributes \(\Delta_H(h)^{-1}\), and the remaining operator is
\(\int_H b(h^{-1})\sigma_{h^{-1}}\Delta_H(h)^{-1}dh=\sigma(b)\).
Hence \(S((xb)\otimes v)=S(x\otimes\sigma(b)v)\).

To check its inner product, expand (7.55) for two vectors (7.57), put \(u=rh\) and \(k=h\ell\), and use (7.1). The scalar factor becomes
\(\kappa(\ell)\Delta_H(h)^{-1}\). Integration of the cutoff gives
\(\int_Hw(uh^{-1})\Delta_H(h)^{-1}dh=Pw(uH)=1\) on the needed support. Therefore
\[
 \langle S(x\otimes v),S(y\otimes z)\rangle
 =\int_H\kappa(\ell)\int_G\overline{x(u)}y(u\ell)\,du\,
          \langle v,\sigma_\ell z\rangle\,d\ell
 =\langle v,\sigma(R(x,y))z\rangle.
 \tag{7.58}
\]
It follows that \(S\) is an isometry on the tensor null quotient.

It is onto after completion. Every \(F\in\mathcal F_0\) is a weighted average of a compactly supported vector function: take \(a=wF\), so
\(F(r)=\int_H\kappa(h)\sigma_h a(rh)dh\).
Approximate \(a\), on a fixed compact support \(K\), by finite sums \(x_j(r)v_j\), using a finite partition of unity and the compactness of its range. The averages converge in the norm (7.55). In fact, on the compact support \(C\) of a cutoff for \(q(K)\), the integration parameters lie in \(C^{-1}K\cap H\); the boundedness of \(\kappa\) there gives a uniform bound by a constant times the approximation error, and integration over \(C\) gives the norm bound. This argument only needs uniform control on compact representatives, even when (7.54) allows unbounded values along an orbit. Hence \(S\) is unitary onto \(\mathcal F\). It intertwines the induced group action with \(F(r)\mapsto F(s^{-1}r)\), and the coefficient action with multiplication by \(\varphi(rH)\). The function model agrees with [Echterhoff 2011] after the modular-density change in (7.38); the freely available [Echterhoff 2017], §7, equation (7.1) and Proposition 7.7, give the same comparison. Balancing, isometry and density are proved above.

**Theorem 7.5 (Mackey imprimitivity).** A strongly continuous unitary representation \(U\) of \(G\) admits a nondegenerate covariant representation of \(C_0(G/H)\) if and only if it is unitarily equivalent to a representation induced from a strongly continuous unitary representation \(\sigma\) of \(H\). The entire covariant system is equivalent to the canonical system above, and determines \(\sigma\) uniquely up to unitary equivalence.

**Proof.** The integrated-form correspondence of Lesson 1 identifies the given system with a nondegenerate representation of \(E\). Apply the inverse tensor functor (7.49) to obtain a representation of \(C^*(H)\), and hence \(\sigma\). Re-induction recovers the original representation of \(E\), including its canonical strict multiplier actions, so it recovers both \(M\) and \(U\). Conversely (7.52) constructs a covariant system for every \(\sigma\), and (7.57) identifies its group part with the induced representation. The inverse functors prove uniqueness for systems. Uniqueness is not asserted from the group representation alone with the coefficient action forgotten. ∎

The spectral-measure formulation uses the written lesson *Unitary representations of abelian groups: the spectral theorem*, in *Harmonic analysis on locally compact abelian groups*. Its background spectral theorem concerns every nondegenerate representation of a commutative C*-algebra, including \(C_0(Y)\) for arbitrary locally compact Hausdorff \(Y\), on an arbitrary Hilbert space: there is a unique regular projection-valued measure \(P\) with
\[
M(a)=\int_Y a(y)\,dP(y),\qquad P(Y)=1.
\tag{7A.1}
\]
We use that general commutative theorem, with \(Y=G/H\), rather than the abelian-group special case of the lesson. The full proof is [Theorem 3.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/HA-LCA/src/unitary-representations-of-abelian-groups-the-spectral-theorem.html#ha-lca-13-theorem-3-1) of that lesson. Its complete programme proof supplies the result used here.

Here is the additional covariance check. If \(U_sM(a)U_s^*=M(a\circ s^{-1})\), then both sides of
\[
U_sP(E)U_s^*=P(sE)
\tag{7A.2}
\]
are regular projection-valued measures as functions of the Borel set \(E\). Their integrals against every \(a\in C_0(Y)\) agree by covariance and change of variable. Uniqueness in (7A.1), equivalently uniqueness of every scalar regular measure, proves (7A.2). Conversely (7A.2) gives coefficient covariance by integration. The Green construction above therefore classifies systems in either formulation, while its module proof uses the continuous coefficient representation throughout.

## The reduced form

The same module also gives the reduced Green equivalence. We include the regular-representation comparison that distinguishes this claim from the full theorem.

Choose a faithful nondegenerate representation \(\pi:A\to\mathcal B(K)\). Let \(\sigma\) be its regular representation of \(B\) on \(L^2(H,K)\), as in Lesson 2:
\[
 (\sigma(b)\eta)(u)=\int_H\pi(\beta_u^{-1}(b(h)))\eta(h^{-1}u)\,dh.
 \tag{7.59}
\]
Its kernel is the kernel of the quotient onto \(B_r=A\rtimes_{\beta,r}H\). Use the transported module coordinates (7.38). Define, initially for compactly supported vectors,
\[
 T(x\otimes\eta)(r)=\int_H\kappa(h)\pi(\beta_h(x(rh)))\eta(h^{-1})\,dh.
 \tag{7.60}
\]
This is a compactly supported continuous \(K\)-valued function. It is balanced over \(B_0\). Indeed, expansion of \(T(xb\otimes\eta)\), followed by \(u=kh\) and then \(k=uv\), leaves inside the outer integral
\(\int_H\pi(\beta_u(b(v)))\eta(v^{-1}u^{-1})dv=(\sigma(b)\eta)(u^{-1})\).
This is exactly \(T(x\otimes\sigma(b)\eta)\).

The inner product can be checked on two elementary tensors by expanding the double integral, setting \(s=rh\) and \(k=h\ell\), and then \(u=h^{-1}\). The right translation of \(dr\) contributes \(\Delta_G(h)^{-1}\), and
\(\kappa(h)\kappa(h\ell)\Delta_G(h)^{-1}
 =\Delta_H(h)^{-1}\kappa(\ell)\).
Inversion converts \(\Delta_H(h)^{-1}dh\) to \(du\). Abbreviate \(a_\ell=\int_Gx(s)^*\beta_\ell(y(s\ell))\,ds\). Thus
\[
\begin{aligned}
 &\langle T(x\otimes\eta),T(y\otimes\zeta)\rangle\\
 &\quad=\int_H\int_H\kappa(\ell)
   \langle\eta(u),\pi(\beta_u^{-1}(a_\ell))\zeta(\ell^{-1}u)\rangle\,d\ell\,du\\
 &\quad=\langle\eta,\sigma(R(x,y))\zeta\rangle.
\end{aligned}
 \tag{7.61}
\]
The identity for finite sums makes \(T\) isometric on the tensor null quotient. Its image is dense in \(L^2(G,K)\). For fixed \(x\) and \(v\in K\), take \(\eta(h^{-1})=p(h)v\), where \(p\in C_c(H)_+\) is a probability bump shrinking to \(e\). Formula (7.60) tends to \(r\mapsto\pi(x(r))v\), uniformly on a fixed compact support, and hence in \(L^2\). Such functions have dense span: scalar compactly supported functions times \(\pi(a)v\) are dense because \(\pi\) is nondegenerate. Therefore \(T\) extends to a unitary
\[
 X\otimes_\sigma L^2(H,K)\cong L^2(G,K).
 \tag{7.62}
\]
Under it, the induced coefficient and group representations are
\[
 (M_\pi(d)\xi)(r)=\pi(d(r))\xi(r),\qquad
 (\lambda_s\xi)(r)=\xi(s^{-1}r).
 \tag{7.63}
\]
Equivariance of \(d\) proves the coefficient identity directly in (7.60); the translation identity is immediate. The coefficient representation \(M_\pi\) is faithful: a nonzero continuous coefficient is nonzero on an open set, detected by \(\pi\), and Haar measure has full support. It is nondegenerate by the multiplication assertion in Lemma 7.2 and the dense functions used above.

The integrated pair (7.63) is faithful for the reduced norm on \(E_r=D\rtimes_{\operatorname{lt},r}G\). To prove this, apply Fell absorption from Lesson 2 to this covariant pair with faithful coefficient representation. Its regularization is equivalent to \((M_\pi\otimes1,\lambda\otimes\lambda)\). The unitary shear
\[
 (W\xi)(r,s)=\xi(r,rs)
 \tag{7.64}
\]
on \(L^2(G\times G,K)\) leaves coefficients unchanged and takes diagonal translation to translation in the first variable alone. Left invariance in the second variable proves its unitarity. Hence the regularization is an amplification of (7.63), and has exactly the same norm. Faithfulness of the regularization gives the assertion.

To finish, put \(I=\ker(B\to B_r)\), and form the Hilbert \(B_r\)-module \(Y\) by completing \(X\) for the quotient inner product
\(\langle[x],[y]\rangle=R(x,y)+I\), removing null vectors first. Its right coefficient action is bounded by the usual inner-product estimate, and it is full. For \(S\in\mathcal K_B(X)\), the inequality
\(R(Sx,Sx)\le\|S\|^2 R(x,x)\) descends to the quotient. Thus \(S\) acts boundedly on \(Y\), and \(\theta_{x,y}\) becomes \(\theta_{[x],[y]}\). The resulting homomorphism \(E=\mathcal K_B(X)\to\mathcal K_{B_r}(Y)\) is onto: its image contains the dense rank-one span and is closed.

Localizing \(Y\) by the faithful regular representation of \(B_r\) gives precisely the tensor Hilbert space in (7.62), since their inner products agree on elementary tensors. Faithful localization detects every adjointable operator: if an operator vanishes after localization, then \(\pi_r(\langle Sx,Sx\rangle)\) has every scalar quadratic form zero, whence \(Sx=0\). Its proof is Tensor products and C*-correspondences, Theorem 4.1. Consequently the kernel of \(E\to\mathcal K_{B_r}(Y)\) equals the kernel of (7.63), which we just identified with \(\ker(E\to E_r)\). We have proved
\[
 \operatorname{Ind}_H^G(A,\beta)\rtimes_{\operatorname{lt},r}G
     \cong\mathcal K_{A\rtimes_{\beta,r}H}(Y),\qquad
 E_r\sim_M B_r.
 \tag{7.65}
\]
For \(H=\{e\}\), (7.40) therefore holds with the reduced crossed product as well, and the full-to-reduced quotient for this translation system is an isomorphism, whether or not \(G\) is amenable.

## Exactness passes through the induction module

Green's theorem can transfer a failure of reduced exactness as well as a representation. Call a locally compact group **exact** when, for every continuous action on \(A\) and every invariant ideal \(I\), the reduced sequence
\[
0\longrightarrow I\rtimes_r G\longrightarrow A\rtimes_rG
 \longrightarrow (A/I)\rtimes_rG\longrightarrow0
\tag{7B.1}
\]
is exact. This is exactness of the crossed-product functor; we make no identification here with tensor exactness of \(C_r^*(G)\).

**Theorem 7B.1 (Kirchberg–Wassermann permanence).** A closed subgroup of an exact locally compact group is exact. Conversely, if \(G/H\) is compact and \(H\) is exact, then \(G\) is exact. Neither assertion requires separability, a discrete quotient, or a subgroup action extending to \(G\).

**Proof.** Begin with an \(H\)-algebra \(A\) and an invariant ideal \(I\). Pointwise quotient gives an exact sequence
\[
0\to\operatorname{Ind}_H^G I\to\operatorname{Ind}_H^G A
 \to\operatorname{Ind}_H^G(A/I)\to0.
\tag{7B.2}
\]
Here is the surjectivity detail. For a section \(d\) with compact quotient support, the cutoff (7.5) writes \(d=Q(wd)\). Approximate the compactly supported \(A/I\)-valued function \(wd\) uniformly, on a fixed compact neighborhood, by finite sums of scalar bumps times elements of \(A/I\). Lift their finitely many coefficient values to \(A\) and apply \(Q\). Properness of the right \(H\)-action gives a uniform bound for these averaging integrals on a compact lift of the quotient support. Thus the resulting induced sections approach \(d\) uniformly. Such sections are dense; the range of the induced C*-homomorphism is closed, so it is onto. Its kernel is exactly the sections taking values in \(I\).

Write \(X_r(A)\) for the reduced Green module already constructed. The closure of \(C_c(G,I)\) is the submodule \(X_r(A)(I\rtimes_r H)\). Its right and left inner products generate respectively
\[
I\rtimes_rH,\qquad (\operatorname{Ind}_H^GI)\rtimes_rG.
\tag{7B.3}
\]
The density follows from the same compact-support averaging and finite Gram sums used in (7.17), now with coefficients in \(I\). Quotienting coefficients gives a map to \(X_r(A/I)\). If

\[
J=\ker\bigl(A\rtimes_rH\to(A/I)\rtimes_rH\bigr),
\]
the inner-product quotient formula shows its null submodule is \(X_r(A)J\): the quotient norm is the norm of the right inner product modulo \(J\). Compactly supported quotient-valued functions have dense lifts by finite coefficient approximation. Therefore \(X_r(A)/X_r(A)J=X_r(A/I)\). The induced left kernel is consequently
\[
\ker\bigl((\operatorname{Ind}_H^GA)\rtimes_rG
 \to(\operatorname{Ind}_H^G(A/I))\rtimes_rG\bigr).
\tag{7B.4}
\]
The Rieffel ideal correspondence, proved in the prerequisite lesson, is injective. Thus (7B.3) equals (7B.4) precisely when \(J=I\rtimes_rH\). Exactness of \(G\), applied to (7B.2), proves exactness of \(H\).

For the converse take a \(G\)-algebra \(A\) and a \(G\)-invariant \(I\). Untwisting the induced algebra by its given \(G\)-action identifies it with \(C(G/H,A)\), with diagonal \(G\)-action. Constant functions give equivariant embeddings of \(A,I,A/I\) into the corresponding function algebras. Reduced crossed products preserve these embeddings: the faithful regular coefficient representation from Lesson 2 proves this directly. Exactness of \(H\), followed by the equivalence just proved, makes the lower row exact in
\[
\begin{array}{ccccccc}
0&\to&I\rtimes_rG&\to&A\rtimes_rG&\to&(A/I)\rtimes_rG\to0\\
&&\downarrow&&\downarrow&&\downarrow\\
0&\to&C(G/H,I)\rtimes_rG&\to&C(G/H,A)\rtimes_rG
 &\to&C(G/H,A/I)\rtimes_rG\to0.
\end{array}
\tag{7B.5}
\]
All vertical arrows are injective. In the middle lower algebra the upper kernel is therefore the intersection of \(A\rtimes_rG\) with \(C(G/H,I)\rtimes_rG\). Choose a contractive approximate identity \(e_i\) of \(I\) and nonnegative integral-one kernels \(\phi_j\in C_c(G)\) shrinking to the identity. The elements \(\phi_j(s)e_i\) form an approximate identity of \(I\rtimes_rG\), and also of \(C(G/H,I)\rtimes_rG\). For the latter assertion the approximate-identity estimates of Lesson 1 apply uniformly to the compact set of coefficient values in \(C(G/H,I)\); continuity is uniform on the compact coset space. If \(y\) belongs to the intersection, these elements times \(y\) belong to the upper ideal and converge to \(y\). The intersection is exactly \(I\rtimes_rG\). This proves the upper exact sequence and the theorem. ∎

Compactness is used twice: constant sections must vanish at infinity on \(G/H\), and approximation must be uniform over that space. It cannot simply be deleted from the second assertion. Amenable groups are exact by Lessons 1 and 4, so any closed subgroup of a group possessing an amenable cocompact subgroup is exact by this theorem.

## Covariant localization and its dilation

Let \(X=G/H\). A nondegenerate representation \(\pi:C_0(X)\to B(\mathcal H)\), together with a continuous unitary representation \(U\), describes a covariant position observable when
\[
U_s\pi(f)U_s^*=\pi(f(s^{-1}\,\cdot)).
\tag{7B.6}
\]
The induction theorem above classifies these pairs by representations of \(H\). Its content concerns the observable and the symmetry together; \(U\) alone need not be irreducible. For example, on \(X=\mathbb R^d\), the Euclidean group and a representation \(\sigma\) of \(\mathrm{SO}(d)\) give
\[
(U_{(R,a)}\xi)(x)=\sigma(R)\xi(R^{-1}(x-a)),
 \qquad (\pi(f)\xi)(x)=f(x)\xi(x).
\tag{7B.7}
\]
Lebesgue measure is invariant under these coordinate changes. Substitution proves the group law and (7B.6), while compactly supported continuous vectors prove strong continuity by density. This puts position covariance in bounded-operator form, without making unsupported assertions about domains of momentum operators.

A blurred position observable replaces \(\pi\) by a **nondegenerate completely positive map** \(Q:C_0(X)\to B(\mathcal H)\), with \(Q(e_i)\to1\) strongly for a positive contractive approximate identity. Assume the same covariance (7B.6) for \(Q\).

**Theorem 7B.2 (covariant Stinespring–imprimitivity dilation).** Every such \((Q,U)\) has a dilation
\[
Q(f)=V^*\widetilde\pi(f)V,\qquad
\widetilde U_sV=VU_s,\qquad V^*V=1,
\tag{7B.8}
\]
where \((\widetilde\pi,\widetilde U)\) is a nondegenerate covariant representation of \(C_0(G/H),G\). Hence it is a Green-induced system from some representation of \(H\). The smallest dilation is unique up to a unitary fixing the embedded original Hilbert space. The projection \(VV^*\) commutes with \(\widetilde U\).

**Proof.** First, for each \(\xi\), the positive functional \(a\mapsto\langle\xi,Q(a)\xi\rangle\) has norm \(\|\xi\|^2\): the norm of a positive functional is its limit on a positive contractive approximate identity, by “Representations and positive functionals,” Theorem 4.7. The squares \(e_i^2\) are also a positive contractive approximate identity, since \(\|e_i^2a-a\|\leq2\|e_i a-a\|\), and likewise on the right. Consequently
\[
0\leq\langle\xi,(1-Q(e_i^2))\xi\rangle\longrightarrow0,
 \qquad 0\leq Q(e_i^2)\leq1.
\]
The positive contractions \(1-Q(e_i^2)\) have square bounded by themselves, so their quadratic-form convergence implies strong convergence to zero. Now extend \(Q\) by \(Q^+(a+\lambda1)=Q(a)+\lambda1\). Compress a positive matrix over the unitization on both sides by the diagonal approximate identity. Complete positivity of \(Q\) gives positive operator matrices. Their strong limits are the unitized matrices, since \(e_i a e_i\to a\) in norm and \(Q(e_i^2)\to1\) strongly. This proves complete positivity of \(Q^+\).

On \(C_0(X)^+\odot\mathcal H\) put
\[
\left\langle\sum_i a_i\otimes\xi_i,\sum_j b_j\otimes\eta_j\right\rangle
 =\sum_{i,j}\langle\xi_i,Q^+(a_i^*b_j)\eta_j\rangle.
\tag{7B.9}
\]
Complete positivity makes this positive. Divide out its null space and complete to \(\mathcal K\). Left multiplication by \(b\) is bounded by \(\|b\|\): apply complete positivity to the positive matrix \([a_i^*(\|b\|^2-b^*b)a_j]\). Its adjoint is left multiplication by \(b^*\), so it defines a representation \(\widetilde\pi\). The map \(V\xi=1\otimes\xi\) is an isometry and gives the compression in (7B.8).

Define on these tensor vectors
\[
\widetilde U_s(a\otimes\xi)=\alpha_s(a)\otimes U_s\xi,
 \qquad\alpha_s(a)(x)=a(s^{-1}x).
\tag{7B.10}
\]
Covariance of \(Q^+\) shows that (7B.9) is preserved; its inverse is \(\widetilde U_{s^{-1}}\). The group law, intertwining with \(V\), and covariance with left multiplication follow on tensors. Point-norm continuity of \(\alpha\) and strong continuity of \(U\), together with the bound \(\|a\otimes\xi\|\leq\|a\|\|\xi\|\), prove strong continuity on the dense tensor space and then on \(\mathcal K\).

The representation of \(C_0(X)\) is nondegenerate. Indeed
\[
\|(1-\widetilde\pi(e_i))V\xi\|^2
 =\langle\xi,Q^+((1-e_i)^2)\xi\rangle\longrightarrow0.
\tag{7B.11}
\]
The convergence follows from the preceding approximate-identity calculation. The vectors \(\widetilde\pi(a)V\xi\), including unitized \(a\), span \(\mathcal K\); (7B.11) and coefficient approximation prove nondegeneracy on all of it. Green's representation-category equivalence now supplies the subgroup representation, without needing a global coset section or a projection-valued spectral theorem.

For uniqueness, send \(\widetilde\pi(a)V\xi\) in one minimal dilation to the same expression in another. Equation (7B.9) makes this map well defined and isometric. Minimality makes it onto, and (7B.10) makes it intertwine the unitary representations. Finally \(V\mathcal H\) is invariant under both \(\widetilde U_s\) and its inverse, so its projection commutes with them. ∎

This argument is the covariant localization mechanism explained by Landsman. It shows precisely how an unsharp observable can be compressed from an induced sharp one.

## Exercises with solutions

**Exercise 1 (The trivial subgroup).** Identify \(\operatorname{Ind}_{\{e\}}^G(A)\) and its group action, and identify its Green module and both crossed products.

**Solution.** The covariance condition in (7.2) imposes no condition, \(G/\{e\}=G\), and vanishing of the norm at infinity is exactly the definition of \(C_0(G,A)\). Formula (7.3) is ordinary left translation. In (7.38), the subgroup integral has one term, so the right inner product is \(\int x(r)^*y(r)dr\). This identifies the completion with \(L^2(G)\boxtimes A\); the old coordinates would instead use \(\nu_G\), related by the density change. The full theorem (7.40) and the reduced theorem (7.65) identify both crossed products with \(\mathcal K(L^2(G))\otimes_{\min}A\), by the same multiplication-and-translation representation. ∎

**Exercise 2 (Compatibility without modular weights).** Suppose \(G\) and \(H\) are unimodular. Verify \(L(x,y)z=xR(y,z)\) directly for an arbitrary \(H\)-action on \(A\).

**Solution.** All weights in (7.8)–(7.11) are \(1\), and right and left Haar measures on \(G\) coincide. At \(r\), the left side is
\[
 \int_H\int_G\beta_h(x(rh)y(t^{-1}rh)^*)z(t^{-1}r)\,dt\,dh.
\]
For each \(h\), put \(u=t^{-1}rh\). Unimodularity makes \(dt=du\), so this is
\[
 \int_H\beta_h(x(rh))\int_G\beta_h(y(u)^*)z(uh^{-1})\,du\,dh.
\]
The inner integral is \(\beta_h(R(y,z)(h^{-1}))\). Formula (7.16), with its weight now equal to \(1\), is therefore exactly this expression. Properness and compact supports bound both integration parameters, so the changes of variables and Fubini are legitimate. No extension of \(\beta\) from \(H\) to \(G\) was used. ∎

**Exercise 3 (Recovering the imprimitivity theorem).** Starting with a nondegenerate covariant pair \((M,U)\) for \(C_0(G/H)\), construct its subgroup representation and prove the existence and uniqueness claims in Mackey's theorem.

**Solution.** Integrate the pair to a nondegenerate representation \(\rho\) of \(E=C_0(G/H)\rtimes G\). On \(\bar X\otimes_\rho\mathcal H\), left multiplication by \(B=C^*(H)\) is nondegenerate, and therefore recovers a strongly continuous unitary representation \(\sigma\) of \(H\) by Lesson 1. Associativity and the second unitary in (7.49) give
\[
 X\otimes_B(\bar X\otimes_E\mathcal H)
  \cong (X\otimes_B\bar X)\otimes_E\mathcal H
  \cong E\otimes_E\mathcal H\cong\mathcal H.
 \tag{7.66}
\]
On a dense set the last two maps send \(x\otimes\bar y\otimes v\) to \(\rho(L(x,y))v\). They are the inverse-evaluation unitaries of *Imprimitivity bimodules and Morita equivalence*, Theorem 3.2, applied as in (7.49). They intertwine \(E\), hence its canonical coefficient and group multipliers. Thus the induced pair is the original pair. Formula (7.57) realizes its group representation as the usual induced representation. Conversely any subgroup representation produces this pair. If two subgroup representations give equivalent entire systems, applying the inverse tensor functor and the first unitary in (7.49) yields equivalent representations of \(C^*(H)\), hence equivalent subgroup unitary representations. This proves uniqueness with exactly the data retained in the question. ∎

**Exercise 4 (Modular functions).** Derive (7.38) from the half-density formulas and recheck the adjoints and compatibility without assuming \(\Delta_G|_H=\Delta_H\). Exhibit a closed subgroup for which that equality fails.

**Solution.** Put \(f(r)=\Delta_G(r)^{1/2}x(r)\). In (7.8), the factor
\(\Delta_G(t)^{1/2}\Delta_G(t^{-1}r)^{1/2}\) equals \(\Delta_G(r)^{1/2}\), eliminating the left-action weight. In (7.16), the vector factor is \(\Delta_G(rh)^{1/2}\); dividing by \(\Delta_G(r)^{1/2}\) leaves \(\kappa(h)\). The two factors in (7.10) together with \(d\nu_G\) leave \(\Delta_G(h)^{1/2}\), again giving \(\kappa(h)\). In (7.11) their product, including its prefactor, is \(\Delta_G(r)\Delta_G(h)/\Delta_G(t)\). These are the four lines of (7.38).

For the right adjoint in these coordinates, the crossed-product star gives
\[
 R(x,y)^*(h)=\Delta_H(h)^{-1}\kappa(h)^{-1}
       \int_G y(rh^{-1})^*\beta_h(x(r))\,dr.
\]
Put \(u=rh^{-1}\), so \(dr=\Delta_G(h)du\). The total scalar is
\(\Delta_G(h)/(\Delta_H(h)\kappa(h))=\kappa(h)\); the result is \(R(y,x)(h)\). For the left adjoint, substitute the last line of (7.38) into (7.7). Its prefactor becomes
\[
 \Delta_G(t)^{-1}\frac{\Delta_G(t^{-1}r)}{\Delta_G(t^{-1})}
      =\frac{\Delta_G(r)}{\Delta_G(t)},
\]
and the starred product reverses \(x,y\), giving \(L(y,x)\).

For compatibility, the left side of (7.38) at \(r\) is
\[
 \int_H\int_G\frac{\Delta_G(r)\Delta_G(h)}{\Delta_G(t)}
       \beta_h(x(rh)y(t^{-1}rh)^*)z(t^{-1}r)\,dt\,dh.
\]
Put \(u=t^{-1}rh\). Now \(dt=\Delta_G(u)^{-1}du\), while
\(\Delta_G(t)=\Delta_G(r)\Delta_G(h)/\Delta_G(u)\), so these two factors cancel completely. The resulting integral is
\(\int_H\int_G\beta_h(x(rh)y(u)^*)z(uh^{-1})\,du\,dh\).
On the right, the right-action weight \(\kappa(h)\) cancels the weight \(\kappa(h^{-1})\) in \(R(y,z)(h^{-1})\). Thus exactly the same integral results. Associativity and the remaining adjoint-action identities also transport through the bijection \(x\mapsto f\); their half-density verifications in Lemma 7.1 used each group’s own Haar inversion and did not identify the modular functions.

For an explicit mismatch, let \(G\) be the affine group of the line, with
\((b,a)(d,c)=(b+ad,ac)\), \(a,c>0\). Its left Haar measure is \(db\,da/a^2\), and \(\Delta_G(b,a)=a^{-1}\). Indeed right multiplication by \((d,c)\) changes the integral by \(c\), as (7.1) requires. The closed dilation subgroup \(H=\{(0,a):a>0\}\) has Haar measure \(da/a\) and \(\Delta_H=1\). Hence \(\kappa(0,a)=a^{-1/2}\). With scalar coefficients its right form is
\[
 R(x,y)(a)=a^{-1/2}\int_{\mathbb R}\int_0^\infty
       \overline{x(b,c)}y(b,ca)\,\frac{dc\,db}{c^2}.
 \tag{7.67}
\]
Replacing \(c\) by \(ca\) in its adjoint reproduces the factor \(a^{-1/2}\), exactly as above. Omitting the modular ratio would violate this adjoint identity. ∎

**Exercise 5 (advanced).** In the covariant dilation (7B.8), prove
\[
Q(|f|^2)-Q(f)^*Q(f)
 =V^*\widetilde\pi(f)^*(1-VV^*)\widetilde\pi(f)V\geq0.
\]
Show that \(Q\) is a *-homomorphism exactly when \(V\mathcal H\) reduces \(\widetilde\pi(C_0(G/H))\).

**Solution.** Insert \(Q(f)=V^*\widetilde\pi(f)V\) and \(V^*V=1\) into the two terms. Their difference is the displayed compression of the positive projection \(1-VV^*\), so it is positive. If the difference vanishes for every \(f\), its factorization as \(T^*T\) gives \((1-VV^*)\widetilde\pi(f)V=0\). Applying this also to \(f^*\) makes the range of \(V\) reducing. Compression to a reducing subspace is multiplicative and adjoint preserving. Conversely, if \(Q\) is multiplicative, the difference is zero and the same argument gives reduction. This distinguishes a sharp covariant observable from a compression that loses position information. ∎

## What this lesson does not prove

We use Haar existence and inversion, Bochner integration and Fubini on compact supports, C*-algebra functional calculus and contractive approximate identities, and the ordinary scalar \(L^2\) density theorem as foundational prerequisites. The full universal property, its Hilbert-module version, regular norms and Fell absorption are the owned results of Lessons 1–2. The Hilbert-module completion and finite Gram matrix test are Hilbert C*-modules, Theorems 2.1–2.3 and 3.1. Interior tensor products, their associativity, faithful localization and the exterior compact-algebra theorem are Tensor products and C*-correspondences, Theorems 1.2, 3.1, 4.1 and 5.1. The inverse tensor maps and representation-category equivalence are the general results *Imprimitivity bimodules and Morita equivalence*, Theorem 3.2 and *The Rieffel correspondence and induced representations*, Theorem 3.1, applied in (7.49)–(7.52). Positivity of the Green forms, full norm bounds, the imprimitivity isomorphism, the induced-function model and the reduced comparison are proved here. The induced-ideal argument, exactness permanence and covariant completely positive dilation are also proved here. The equivalent projection-valued formulation uses the written general commutative spectral theorem identified above; its covariance equivalence is proved in (7A.1)-(7A.2).

Hilbert C*-modules and Tensor products and C*-correspondences are the prerequisite lessons named above.

Imprimitivity bimodules and Morita equivalence, Proposition 3.1 and Theorem 3.2, and The Rieffel correspondence and induced representations, Theorem 3.1, supply the general conjugate-module and representation results.

[Green 1978] P. Green, *The local structure of twisted covariance algebras*, Acta Mathematica 140 (1978), 191–250, §2, especially pp. 199–204. The present lesson treats ordinary actions and full untwisted crossed products; it does not assert the additional twisted results of that paper.

[Williams] D. P. Williams, *Crossed Products of C*-Algebras*, §§3.6 and 4.1–4.4; Example 3.47, Lemma 3.54, Corollary 4.17 and Theorem 4.22. [Author's draft, version 3.1](https://math.dartmouth.edu/~dana/cpcsa/draft3.1.pdf). Corollary 4.17 is the induced-algebra theorem for an arbitrary subgroup action; Theorem 4.22 also describes the special case in which that action extends to the whole group.

[Blackadar 2006] B. Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*, §§II.10.4.14–II.10.4.16, p. 224. Those sections describe the scalar imprimitivity and Stone–von Neumann consequences. [Author's revised edition, 2017](https://bruceblackadar.com/Mathematics/Cycr.pdf).

[Echterhoff 2011] S. Echterhoff, *Crossed products, the Mackey–Rieffel–Green machine and applications*, arXiv:1006.4975v2, 24 August 2011. [Author manuscript](https://arxiv.org/abs/1006.4975v2). Section 9 gives the induced-function model; the balancing, isometry and density arguments are included above.

[Echterhoff 2017] S. Echterhoff, [*Crossed products and the Mackey–Rieffel–Green machine*](https://arxiv.org/abs/1006.4975v4), arXiv:1006.4975v4, 13 June 2017. §7, equation (7.1), Proposition 7.7, pp. 36–37, give the induced-function comparison; balancing, isometry and density are proved in this lesson.

[Landsman 1998] N. P. Landsman, [*Lecture Notes on C*-Algebras, Hilbert C*-modules, and Quantum Mechanics*](https://arxiv.org/abs/math-ph/9807030v1), 1998. Covariant localization and quantization motivate the dilation above.
