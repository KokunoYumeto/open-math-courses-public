# A finite semidefinite lift

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

[Angular slices of the cone](angular-slices-of-the-cone.md) describes each slice of the cone \(K\) by the matrix inequality \(L_\theta\succeq0\) of size \(20\), whose coefficients are trigonometric polynomials in the angle \(\theta\). This lesson removes the angle. A linear functional on trigonometric polynomials, constrained by one positive semidefinite matrix of size \(100\), plays the part of an unknown angle: evaluation at an angle is always feasible, and a matching identity of degree two shows that every feasible functional certifies membership in \(K\). The \(307\) coordinates of the functional that are not fixed by the point give the auxiliary variables of Theorem C. The proof follows OpenAI [OpenAI-LIFT, Sections 3 and 4]; the use of a finite matrix to encode positivity against a space of test functions is the idea of moment relaxations in polynomial optimization.

Throughout, \(c,s,w,d(\theta),k,Y_\theta,U(\theta),V_0,F_\theta,B(r),J_u\) and \(L_\theta\) are as in the previous lesson, and \(Q(y,z)=\frac12\bigl(Q(y+z)-Q(y)-Q(z)\bigr)\) is the symmetric bilinear form with \(Q(y,y)=Q(y)\).

## 1. A degree-two matching identity

A *trigonometric polynomial of degree at most \(j\)* is a linear combination of \(e^{i\ell\theta}\), \(-j\le\ell\le j\); the real ones form the space \(\mathcal T_j\) with basis \(1,\cos\theta,\sin\theta,\dots,\cos j\theta,\sin j\theta\), of dimension \(2j+1\). For \(S\in\mathbb S^3\) and \(F,H\in\mathbf C^{3\times2}\) put
\[
\langle F,H\rangle_S=\operatorname{Re}\operatorname{tr}(F^*SH)=\operatorname{tr}\bigl(\widetilde F^{\mathsf T}S\widetilde H\bigr),
\]
a symmetric real bilinear form; the second expression follows column by column from \(\operatorname{Re}\bigl((a-ib)^{\mathsf T}S(c+id)\bigr)=a^{\mathsf T}Sc+b^{\mathsf T}Sd\). Polarizing Lemma 5.1 of the previous lesson within one plane gives, for \(F_i=F_\theta(\eta_i,\xi_i)\) and \(Y_i=Y_\theta(\eta_i,\xi_i)\),
\[
\langle F_1,F_2\rangle_S=\operatorname{tr}\bigl(SQ(Y_1,Y_2)\bigr).
\]
We call this the *polarized identity*. Indeed \(\langle F,H\rangle_S=\operatorname{tr}\bigl(S\operatorname{Re}(HF^*)\bigr)\), the matrix \(\operatorname{Re}(HF^*)\) is the transpose of \(\operatorname{Re}(FH^*)\), and the symmetric part of \(\operatorname{Re}(F_1F_2^*)\) is \(Q(Y_1,Y_2)\) by Lemma 5.1.

**Lemma 6.1** (OpenAI). Let \(S\in\mathbb S^3\), possibly indefinite, and \(z\in\mathbf R^3\) with \((z_1,z_2)\ne(0,0)\). There is a matrix \(C(\theta)\in\mathbf C^{3\times2}\) whose entries are trigonometric polynomials of degree at most \(2\) such that for all \(\theta,\eta,\xi\in\mathbf R\)
\[
\begin{aligned}
\widetilde C(\theta)\widetilde C(\theta)^{\mathsf T}&=Q(z),\\
\bigl\langle F_\theta(\eta,\xi),C(\theta)\bigr\rangle_S&=\operatorname{tr}\bigl(SQ(Y_\theta(\eta,\xi),z)\bigr).
\end{aligned}
\]

*Proof.* Write \(z=\tau d(\alpha)+\rho k\) with \(\tau>0\), and put \(w_0=e^{i\alpha}\), \(R_0=\tau U(\alpha)+\rho V_0\) and \(N=SR_0\). By Lemma 5.1, \(\widetilde R_0\widetilde R_0^{\mathsf T}=Q(z)\). We take \(C(\theta)=R_0M(\theta)\) with a unitary \(2\times2\) matrix \(M(\theta)\); then \(\widetilde C\widetilde C^{\mathsf T}=\operatorname{Re}(R_0MM^*R_0^*)=Q(z)\), the first identity.

*The pairing with \(V_0\).* Write \(N_1,N_2,N_3\) for the rows of \(N\), and for a row \(x=(x_+,x_-)\) write \(x^M=xM\). Put \(v=N_3-iN_2\). The two rows of \(V_0^*\) are both \((0,-i,1)/\sqrt2\), so
\[
\begin{aligned}
\sqrt2\,\langle V_0,C\rangle_S&=\operatorname{Re}\bigl(v^M_++v^M_-\bigr)\\
&=\operatorname{Re}\bigl(v^M_++\overline{v^M_-}\bigr).
\end{aligned}
\]

*The pairing with \(U\).* Put \(m=N_3+iN_2\) and \(n=N_1\). Using \(s=(w-\bar w)/2i\) and \(c=(w+\bar w)/2\) in the rows of \(U(\theta)^*\), a direct expansion gives
\[
\begin{aligned}
&\sqrt2\,\langle U(\theta),C\rangle_S\\
&\quad=\operatorname{Re}\Bigl[\tfrac{w^3}2\bigl(v^M_+-\overline{v^M_-}\bigr)\\
&\qquad+w\bigl(\tfrac12m^M_+-n^M_+\\
&\qquad\quad-\tfrac12\overline{m^M_-}-\overline{n^M_-}\bigr)\Bigr],
\end{aligned}
\]
where the terms with negative powers of \(w\) were replaced by their complex conjugates inside the real part.

*Choosing \(M\).* Write \(M=\bigl(\begin{smallmatrix}a&b\\-\bar b&\bar a\end{smallmatrix}\bigr)\), unitary when \(|a|^2+|b|^2=1\). For a row \(x\), \((xM)_+=x_+a-x_-\bar b\) and \(\overline{(xM)_-}=\bar x_+\bar b+\bar x_-a\). Put
\[
\begin{aligned}
g&=v_++\overline{v_-},\quad h=v_+-\overline{v_-},\\
\kappa(\theta)&=(w_0/w)^2,\quad\delta=|g|^2+|h|^2 .
\end{aligned}
\]
Then \(v^M_++\overline{v^M_-}=ga+\bar h\bar b\) and \(v^M_+-\overline{v^M_-}=ha-\bar g\bar b\). We require
\[
ga+\bar h\bar b=g,\qquad ha-\bar g\bar b=h\kappa .
\]
If \(\delta>0\), the coefficient matrix \(\bigl(\begin{smallmatrix}g&\bar h\\h&-\bar g\end{smallmatrix}\bigr)\) has orthogonal columns of squared length \(\delta\), and the solution is
\[
a=\frac{|g|^2+|h|^2\kappa}\delta,\qquad\bar b=\frac{gh(1-\kappa)}\delta .
\]
Since \(|\kappa|=1\), the right side \((g,h\kappa)\) has squared length \(\delta\), so \(|a|^2+|b|^2=1\). If \(\delta=0\), then \(g=h=0\), and \(a=1\), \(b=0\) satisfy the requirement. In both cases \(M(\alpha)=I\), because \(\kappa(\alpha)=1\), and \(a\) and \(\bar b\) contain only the frequencies \(0\) and \(-2\). Hence \(C=R_0M\) has degree at most \(2\), and \(C(\alpha)=R_0\).

*Frequencies.* With this choice, \(\sqrt2\langle V_0,C\rangle_S=\operatorname{Re}g\) is constant. In the pairing with \(U\), the first term is \(\frac12w^3h\kappa=\frac12hw_0^2w\), of frequency \(1\). In the second, each of \(m^M_+\), \(n^M_+\), \(\overline{m^M_-}\), \(\overline{n^M_-}\) is a combination of \(a\) and \(\bar b\), with frequencies \(0\) and \(-2\), so after multiplication by \(w\) only the frequencies \(\pm1\) remain. So \(P(\theta)=\langle U(\theta),C(\theta)\rangle_S\) is a real combination of \(\cos\theta\) and \(\sin\theta\), and so is \(T(\theta)=\operatorname{tr}(SQ(d(\theta),z))\), which is linear in \(d(\theta)\).

*Identifying the pairings.* By the polarized identity on the plane of angle \(\alpha\), \(\langle V_0,R_0\rangle_S=\operatorname{tr}(SQ(k,z))\) and \(\langle U(\alpha),R_0\rangle_S=\operatorname{tr}(SQ(d(\alpha),z))\). The pairing with \(V_0\) is constant, and at \(\theta=\alpha\), where \(C(\alpha)=R_0\), it equals \(\operatorname{tr}(SQ(k,z))\). For the pairing with \(U\), \(P(\alpha)=T(\alpha)\), and a real combination of \(\cos\theta\) and \(\sin\theta\) is determined by its value and its derivative at one point, so it suffices to show \(P'(\alpha)=T'(\alpha)\). Differentiating \(\langle C,C\rangle_S=\operatorname{tr}(SQ(z))\), which is constant, gives \(\langle R_0,C'(\alpha)\rangle_S=0\); the constancy of \(\langle V_0,C\rangle_S\) gives \(\langle V_0,C'(\alpha)\rangle_S=0\). As \(R_0=\tau U(\alpha)+\rho V_0\) with \(\tau>0\), \(\langle U(\alpha),C'(\alpha)\rangle_S=0\). The polarized identity with \(F_1=F_2=F_\theta(\tau,\rho)\) reads
\[
\begin{aligned}
&\langle\tau U(\theta)+\rho V_0,\tau U(\theta)+\rho V_0\rangle_S\\
&\quad=\operatorname{tr}\bigl(SQ(\tau d(\theta)+\rho k)\bigr);
\end{aligned}
\]
differentiating at \(\alpha\) and dividing by \(2\tau\) gives \(\langle U'(\alpha),R_0\rangle_S=\operatorname{tr}(SQ(d'(\alpha),z))\), which is \(T'(\alpha)\). Hence
\[
\begin{aligned}
P'(\alpha)&=\langle U'(\alpha),R_0\rangle_S\\
&\quad+\langle U(\alpha),C'(\alpha)\rangle_S,
\end{aligned}
\]
which equals \(T'(\alpha)\). The second identity follows by linearity in \((\eta,\xi)\). \(\square\)

## 2. The finite matrix condition

Let \(\mathcal E\) be the space of real functions of \((\theta,\mathcal X,\mathcal Z,\eta,\xi)\) that are linear in the \(22\) coordinates of \((\mathcal X,\mathcal Z,\eta,\xi)\in\mathbb S^4\times\mathbb S^4\times\mathbf R^2\), with coefficients in \(\mathcal T_7\). It has dimension \(22\cdot15=330\). For a linear functional \(\Lambda:\mathcal E\to\mathbf R\), applied entrywise to vectors and matrices, and a point \((X,Z,y)\), consider the *output equations*
\[
\begin{aligned}
&\Lambda(\mathcal X)=X,\qquad\Lambda(\mathcal Z)=Z,\\
&\Lambda\bigl(Y_\theta(\eta,\xi)\bigr)=y,
\end{aligned}
\]
the last meaning \(\Lambda(\eta\cos\theta)=y_1\), \(\Lambda(\eta\sin\theta)=y_2\), \(\Lambda(\xi)=y_3\), and the *moment condition*: for all \(q\in(\mathcal T_2)^{20}\),
\[
\Lambda\bigl(q(\theta)^{\mathsf T}L_\theta\,q(\theta)\bigr)\ge0,
\]
where \(L_\theta=L_\theta(\mathcal X,\mathcal Z,\eta,\xi)\).
The argument of \(\Lambda\) lies in \(\mathcal E\): the entries of \(L_\theta\) are linear in the \(22\) coordinates with coefficients of degree at most \(3\), and the entries of \(q\) have degree at most \(2\). With \(f_1=1\), \(f_2=\cos\theta\), \(f_3=\sin\theta\), \(f_4=\cos2\theta\) and \(f_5=\sin2\theta\), define \(H(\Lambda)\in\mathbb S^{100}\), with rows and columns indexed by pairs \((i,a)\), \(1\le i\le20\), \(1\le a\le5\), by
\[
H(\Lambda)_{(i,a),(j,b)}=\Lambda\bigl(f_af_b\,(L_\theta)_{ij}\bigr).
\]
If \(q_i=\sum_at_{i,a}f_a\), then \(\Lambda(q^{\mathsf T}L_\theta q)=t^{\mathsf T}H(\Lambda)t\). So the moment condition is equivalent to \(H(\Lambda)\succeq0\), a matrix whose entries are linear in \(\Lambda\).

**Proposition 6.2** (OpenAI). For \((X,Z,y)\in\mathbb S^4\times\mathbb S^4\times\mathbf R^3\), the following are equivalent:

1. \((X,Z,y)\in K\);
2. some linear functional \(\Lambda:\mathcal E\to\mathbf R\) satisfies the output equations and \(H(\Lambda)\succeq0\).

*Proof.* (1) implies (2): choose \(\theta_0,\eta_0,\xi_0\) with \(y=Y_{\theta_0}(\eta_0,\xi_0)\), and let \(\Lambda\) be evaluation at \((\theta_0,X,Z,\eta_0,\xi_0)\). The output equations hold, and with \(G_0=L_{\theta_0}(X,Z,\eta_0,\xi_0)\), which is positive semidefinite by Proposition 5.3 of the previous lesson, \(\Lambda(q^{\mathsf T}L_\theta q)=q(\theta_0)^{\mathsf T}G_0\,q(\theta_0)\ge0\). This includes singular \(X\).

(2) implies (1). *Step 1.* A constant \(q\) supported in the first block of four gives \(\Lambda(a^{\mathsf T}\mathcal Xa)=a^{\mathsf T}Xa\ge0\) for \(a\in\mathbf R^4\); so \(X\succeq0\).

*Step 2: a family of scalar inequalities.* Let \(u\in\mathbf R^4\), \(D\in\mathbb S^4\) and \(z\in\mathbf R^3\) with \((z_1,z_2)\ne(0,0)\). Apply Lemma 6.1 with \(S=J_uDJ_u^{\mathsf T}\), and let \(b_1(\theta),\dots,b_4(\theta)\) be the columns of \(\widetilde C(\theta)\); their entries lie in \(\mathcal T_2\). Take the vector \(q\in(\mathcal T_2)^{20}\) with the five blocks
\[
q=\bigl(-DJ_u^{\mathsf T}b_1,\dots,-DJ_u^{\mathsf T}b_4,u\bigr).
\]
Let \(r_j\) be the columns of \(\widetilde F_\theta(\eta,\xi)\). Since \(B(r_j)u=J_u^{\mathsf T}r_j\), the diagonal blocks and the cross terms of \(q^{\mathsf T}L_\theta q\) are, by the two identities of Lemma 6.1,
\[
\begin{aligned}
&\textstyle\sum_jb_j^{\mathsf T}J_uD\mathcal XDJ_u^{\mathsf T}b_j\\
&\quad=\operatorname{tr}\bigl(J_uD\mathcal XDJ_u^{\mathsf T}Q(z)\bigr),\\
&\textstyle-2\sum_jb_j^{\mathsf T}J_uDJ_u^{\mathsf T}r_j\\
&\quad=-2\bigl\langle C,F_\theta(\eta,\xi)\bigr\rangle_S\\
&\quad=-2\operatorname{tr}\bigl(SQ(Y_\theta(\eta,\xi),z)\bigr),
\end{aligned}
\]
and the last block contributes \(u^{\mathsf T}\mathcal Zu\). The angle has disappeared from the coefficient of \(\mathcal X\), and the cross term is linear in \(Y_\theta(\eta,\xi)\). Applying \(\Lambda\) and the output equations,
\[
\begin{aligned}
&u^{\mathsf T}Zu+\operatorname{tr}\bigl(J_uDXDJ_u^{\mathsf T}Q(z)\bigr)\\
&\quad-2\operatorname{tr}\bigl(J_uDJ_u^{\mathsf T}Q(y,z)\bigr)\ge0 .
\end{aligned}
\]
We call this the *test inequality*. Its left side is a polynomial in \(z\), so it holds for all \(z\in\mathbf R^3\) by continuity, for all \(u\) and \(D\).

*Step 3: the range condition.* Fix \(\theta_0,\eta_0,\xi_0\) with \(y=Y_{\theta_0}(\eta_0,\xi_0)\), let \(r_j\) be the columns of \(\widetilde F_{\theta_0}(\eta_0,\xi_0)\) and \(B_j=B(r_j)\). For \(v\in\ker X\) and \(t\in\mathbf R\), take \(D=t\,vv^{\mathsf T}\) and \(z=y\) in the test inequality. Since \(DXD=0\), for all real \(t\)
\[
u^{\mathsf T}Zu-2t\,(J_uv)^{\mathsf T}Q(y)(J_uv)\ge0 ,
\]
so \((J_uv)^{\mathsf T}Q(y)(J_uv)=0\). By Lemma 5.1, \(Q(y)=\sum_jr_jr_j^{\mathsf T}\), so \(\sum_j(v^{\mathsf T}J_u^{\mathsf T}r_j)^2=\sum_j(v^{\mathsf T}B_ju)^2=0\). As \(u\) and \(v\in\ker X\) are arbitrary, the range of every \(B_j\) is orthogonal to \(\ker X\), that is, contained in the range of \(X\).

*Step 4: positivity of the slice pencil.* Let \(X^\dagger\) be the symmetric matrix that inverts \(X\) on its range and vanishes on \(\ker X\); then \(X^\dagger XX^\dagger=X^\dagger\), and \(XX^\dagger B_j=B_j\) by Step 3. Taking \(D=X^\dagger\) and \(z=y\) in the test inequality, and using the second statement of Lemma 5.2 of the previous lesson, gives for all \(u\)
\[
u^{\mathsf T}Zu-u^{\mathsf T}\Phi_y(X^\dagger)u\ge0 ,
\]
so, by its first statement,
\[
Z\succeq\sum_jB_j^{\mathsf T}X^\dagger B_j .
\]
For \(a_1,\dots,a_4,u\in\mathbf R^4\), completing the square gives
\[
\begin{aligned}
&\textstyle\sum_ja_j^{\mathsf T}Xa_j+2\sum_ja_j^{\mathsf T}B_ju+u^{\mathsf T}Zu\\
&\quad=\textstyle\sum_j(a_j+X^\dagger B_ju)^{\mathsf T}X(a_j+X^\dagger B_ju)\\
&\qquad+u^{\mathsf T}\bigl(Z-\textstyle\sum_jB_j^{\mathsf T}X^\dagger B_j\bigr)u\ge0,
\end{aligned}
\]
where the cross terms agree because \(XX^\dagger B_j=B_j\). The left side is the quadratic form of \(L_{\theta_0}(X,Z,\eta_0,\xi_0)\), which is therefore positive semidefinite, and Proposition 5.3 gives \((X,Z,y)\in K\). \(\square\)

The converse uses an arbitrary feasible functional: \(\Lambda\) need not be an evaluation or an integral against a measure, and no closure of the projected set is taken.

## 3. Proof of Theorem C

Take as coordinates of \(\Lambda\) its values on the basis of \(\mathcal E\) formed by the products of the \(22\) coordinate functions with \(1,\cos\theta,\sin\theta,\dots,\cos7\theta,\sin7\theta\): \(330\) numbers. The output equations prescribe exactly \(23\) of them, namely \(\Lambda(\mathcal X_{ij})\) and \(\Lambda(\mathcal Z_{ij})\) for \(i\le j\), and \(\Lambda(\eta\cos\theta)\), \(\Lambda(\eta\sin\theta)\), \(\Lambda(\xi)\), and they are distinct basis coordinates. Substitute the entries of \(X\), \(Z\) and \(y\) for these coordinates in \(H(\Lambda)\), and let the other \(330-23=307\) coordinates be the auxiliary variables \(v\). The result is a fixed linear pencil \(\sum_\nu x_\nu A_\nu+\sum_jv_jG_j\) of size \(5\cdot20=100\), with no constant term, and by Proposition 6.2 the set of \(x\) for which some \(v\) makes it positive semidefinite is exactly \(K\). \(\square\)

Theorem A excludes affine representations in the original coordinates as well. If a cone \(K\ni0\) equals \(\{x:A_0+L(x)\succeq0\}\) with \(L\) linear, then \(A_0\succeq0\); for \(x\in K\) and \(t>0\), \(tx\in K\) gives \(A_0/t+L(x)\succeq0\), and \(t\to\infty\) gives \(L(x)\succeq0\); conversely \(L(x)\succeq0\) implies \(A_0+L(x)\succeq0\). So \(K=\{L\succeq0\}\), which Theorem A excludes. The sizes \(100\) and \(307\) in Theorem C are not claimed to be the least possible.

## 4. Exercises

**6.1** (easy). Check \(\dim\mathcal T_7=15\), \(\dim\mathcal E=330\), and that the entries of \(L_\theta\), multiplied by two entries of a vector in \((\mathcal T_2)^{20}\), lie in \(\mathcal E\).

**6.2** (medium). Show that a convex combination of evaluation functionals at points \((\theta_m,X,Z,\eta_m,\xi_m)\) with \(Y_{\theta_m}(\eta_m,\xi_m)=y\) for all \(m\) is feasible when \((X,Z,y)\in K\). Why does Proposition 6.2 not need every feasible \(\Lambda\) to be of this form?

**6.3** (medium). In Lemma 6.1, suppose \(S=0\). Show that \(g=h=0\), that \(C(\theta)=R_0\) for all \(\theta\), and that both identities hold trivially.

**6.4** (easy). In Step 3, explain why the coefficient of \(t\) must vanish in an inequality \(A-2tB\ge0\) that holds for all real \(t\).

## 5. Solutions

**6.1.** \(\mathcal T_7\) has the basis \(1\) and \(\cos\ell\theta,\sin\ell\theta\) for \(1\le\ell\le7\): \(15\) functions; \(22\cdot15=330\). The entries of \(L_\theta\) are linear in the coordinates with coefficients of degree at most \(3\), and a product of two trigonometric polynomials of degrees at most \(2\) has degree at most \(4\); the total degree is at most \(7\).

**6.2.** Each evaluation functional satisfies the output equations and gives \(\Lambda(q^{\mathsf T}L_\theta q)=q(\theta_m)^{\mathsf T}L_{\theta_m}q(\theta_m)\ge0\) by Proposition 5.3, and both conditions are preserved by convex combinations. Proposition 6.2 derives membership in \(K\) from the test inequalities alone, which every feasible \(\Lambda\) satisfies; it never represents \(\Lambda\).

**6.3.** If \(S=0\), then \(N=0\), so \(v=0\) and \(g=h=0\); hence \(\delta=0\), \(a=1\), \(b=0\), \(M=I\) and \(C=R_0\). The Gram identity is Lemma 5.1, and both sides of the pairing identity vanish.

**6.4.** If \(B\ne0\), take \(t\) of the sign of \(B\) and large: \(A-2tB<0\).

## References

- [OpenAI-LIFT] OpenAI, *An exact semidefinite lift of a nonspectrahedral hyperbolicity cone*, OpenAI Math Release preprint, 5 October 2026, Sections 3 and 4. https://github.com/openai/math/tree/main/preprints/An-Exact-Semidefinite-Lift-of-a-Nonspectrahedral-Hyperbolicity-Cone-October-5-2026
