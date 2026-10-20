# Boundary means and measurable cocycles

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The finite-factor part of the proof starts from unitaries \(v_g\) of the second algebra, indexed by a countable dense subgroup \(G\) of the unitary group of the first, whose products are only approximately respected: \(\|v_gv_h-v_{gh}\|\) is small. For an amenable group one would average over the group and correct the \(v_g\) into a representation. The group \(G\) need not be amenable. This lesson constructs, for every countable group, a probability space with a nonsingular \(G\)-action and an equivariant conditional mean (Lemma 2.1). With it, approximate cocycles are corrected into exact measurable cocycles (Lemma 3.1), and cocycles close to a representation are intertwined with it (Lemma 4.1). The mean is the conditional-expectation form of amenability of the action of \(G\) on the Poisson boundary of a random walk [AEG, Theorem 3.4]; the correction is the averaging and polar decomposition iteration of Kazhdan and Burger–Ozawa–Thom [BOT, Theorem 3.2], carried out over this action [OpenAI-289, Section 4].

We use: standard measure theory as in the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10) (Fremlin, *Measure Theory*, Volumes 1 and 2: the Radon–Nikodym theorem, Section 232; conditional expectations, Section 233; Fubini's theorem, Section 252; infinite product measures, Section 254); the [Banach–Alaoglu theorem](course:foundations-of-von-neumann-algebras/weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian#OA-FND-WT-03) and Tychonoff's theorem; and the [bicommutant theorem](course:foundations-of-von-neumann-algebras/the-double-commutant-theorem#OA-FND-BI-06).

## 1. Conventions

Let \(G\) be a countable group acting on a probability space \((D,\nu)\) by measurable maps. The action is *nonsingular* when each \(g\in G\) maps \(\nu\)-null sets to null sets; measure preservation is not required. On \(G\times D\) we use counting measure times \(\nu\). For functions on \(D\) and on \(G\times D\) put
\[
\begin{aligned}
\alpha_gF(x)&=F(g^{-1}x),\\
(\lambda_gF)(t,x)&=F(g^{-1}t,g^{-1}x).
\end{aligned}
\]
Let \(K\) be a separable Hilbert space. A *bounded operator field* on \(D\) is a map \(B:D\to B(K)\) such that \(x\mapsto\langle B(x)\xi,\eta\rangle\) is measurable for all \(\xi,\eta\), and \(\|B\|_\infty=\operatorname{ess\,sup}_x\|B(x)\|<\infty\); fields equal almost everywhere are identified. The operator norm \(\|B(x)\|\) is a measurable function of \(x\), since it can be computed on a countable dense set of unit vectors. Products of bounded operator fields are bounded operator fields: for fixed \(\xi\), the map \(x\mapsto C(x)\xi\) is weakly measurable with values in the separable space \(K\), hence a pointwise limit of countably valued measurable maps \(\zeta_n\), and \(\langle B(x)C(x)\xi,\eta\rangle=\lim_n\langle\zeta_n(x),B(x)^*\eta\rangle\). For a von Neumann algebra \(A\subseteq B(K)\), \(L^\infty(D,A)\) denotes the bounded fields with values in \(A\) almost everywhere, and \(L^\infty(D,\mathcal U(A))\) the unitary-valued ones. Fields on \(G\times D\) are defined in the same way.

## 2. Equivariant boundary means

**Lemma 2.1** (boundary means). For every countable group \(G\) there are a standard probability space \((D,\nu)\) with a nonsingular \(G\)-action and a positive unital contraction
\[
m:L^\infty(G\times D)\to L^\infty(D)
\]
such that, for \(g\in G\), \(F\in L^\infty(G\times D)\) and \(f\in L^\infty(D)\),
\[
\begin{gathered}
m(\lambda_gF)=\alpha_g(mF),\\
m(fF)=f\,m(F).\quad(2.1)
\end{gathered}
\]
There is a mean \(m^{(2)}:L^\infty(G^2\times D^2)\to L^\infty(D^2)\) with the same properties for the separate action \((g,h)(x,y)=(gx,hy)\) of \(G\times G\) on \(D\times D\). Each of the two means extends to a contraction on bounded operator fields, on any separable \(K\), that preserves adjoints, maps fields with values in a von Neumann algebra \(A\subseteq B(K)\) to fields with values in \(A\), satisfies the analogue of (2.1), and satisfies
\[
m(BFC)=B\,m(F)\,C
\tag{2.2}
\]
for bounded operator fields \(B,C\) on \(D\) (independent of the group variable).

**Proof.** *The random walk.* Choose a probability measure \(\mu\) on \(G\) with \(\mu(g)=\mu(g^{-1})>0\) for every \(g\). Let \(X=G^{\{0,1,2,\dots\}}\) with the product probability \(\mathbb P=\mu^{\otimes\{0,1,2,\dots\}}\), and define
\[
\begin{aligned}
g(\omega_0,\omega_1,\dots)&=(g\omega_0,\omega_1,\dots),\\
S(\omega_0,\omega_1,\omega_2,\dots)&=(\omega_0\omega_1,\omega_2,\dots).
\end{aligned}
\]
These maps commute. Under the image of \(\mathbb P\) by \(g\), the coordinates are independent, the first with law \(\mu(g^{-1}\,\cdot)\) and the others with law \(\mu\); under the image by \(S\), the first coordinate has law \(\mu*\mu\) and the others are independent with law \(\mu\). Both first-coordinate laws give positive mass to every point of the countable set \(G\) (note \(\mu*\mu(h)\ge\mu(1)\mu(h)\)), so they are equivalent to \(\mu\), and the image measures are equivalent to \(\mathbb P\), with densities depending only on the first coordinate. Thus \(G\) and \(S\) act nonsingularly on \((X,\mathbb P)\).

*The invariant sets.* Let \(\mathcal I\) be the family of measurable \(E\subseteq X\) with \(S^{-1}E=E\) up to a null set; it is a \(\sigma\)-algebra. The measure algebra of \(X\), with the metric \(\mathbb P(E\triangle F)\), is separable, because the product \(\sigma\)-algebra is countably generated; so its subset \(\mathcal I\) contains a countable dense family \((E_j)_{j\ge1}\). For \(E\in\mathcal I\) choose \(j_k\) with \(\mathbb P(E\triangle E_{j_k})<2^{-k}\); by the Borel–Cantelli lemma \(1_{E_{j_k}}\to1_E\) almost everywhere, so every \(E\in\mathcal I\) agrees up to a null set with a set in the \(\sigma\)-algebra generated by the \(E_j\). Since \(S\) commutes with \(g\), \(S^{-1}(gE)=g\,S^{-1}E\), so \(gE\in\mathcal I\) for \(E\in\mathcal I\).

*The boundary.* Put \(D=\{0,1\}^{\mathbb N\times G}\), a compact metrizable space, define \(b:X\to D\) by \(b(\omega)_{j,g}=1_{gE_j}(\omega)\), and let \(\nu=b_*\mathbb P\). The group acts on \(D\) by \((hx)_{j,g}=x_{j,h^{-1}g}\), and \(b(h\omega)_{j,g}=1_{h^{-1}gE_j}(\omega)=(h\,b(\omega))_{j,g}\), so \(b\) is equivariant. If \(\nu(N)=0\), then \(\mathbb P(b^{-1}N)=0\), so \(\mathbb P(h^{-1}b^{-1}N)=0\), and \(h^{-1}b^{-1}N=b^{-1}(h^{-1}N)\); the action on \(D\) is nonsingular. Each coordinate of \(b\) is the indicator of a set in \(\mathcal I\), so \(b\circ S=b\) almost everywhere.

Composition with \(b\) is an isometric \(*\)-isomorphism of \(L^\infty(D,\nu)\) onto the algebra of \(F\in L^\infty(X)\) with \(F\circ S=F\) almost everywhere. Indeed, \(f\circ b=0\) almost everywhere exactly when \(f=0\) \(\nu\)-almost everywhere, and \(f\circ b\) is \(S\)-invariant because \(b\circ S=b\). Conversely, an \(S\)-invariant \(F\) has level sets in \(\mathcal I\), hence is measurable for the completion of the \(\sigma\)-algebra generated by the coordinates of \(b\), and is therefore almost everywhere of the form \(f\circ b\).

*The mean.* For \(F\in L^\infty(G\times D)\) put \((JF)(\omega)=F(\omega_0,b(\omega))\). This is well defined on classes: if \(F=0\) almost everywhere, then for each \(t\) the section \(F(t,\cdot)\) vanishes off a \(\nu\)-null set \(N_t\), and \(JF\) vanishes off the null set \(\bigcup_tb^{-1}N_t\). Put
\[
T_nF=\frac1n\sum_{j=0}^{n-1}(JF)\circ S^j .
\]
The maps \(T_n\) are positive unital contractions into \(L^\infty(X)=L^1(X)^*\). By Tychonoff's theorem and the Banach–Alaoglu theorem, a subnet converges pointwise in the weak\* topology to a positive unital contraction \(T\). Composition with a nonsingular map \(R\) is weak\* continuous on \(L^\infty(X)\): its preadjoint sends \(q\in L^1\) to the Radon–Nikodym density of the measure \(E\mapsto\int_{R^{-1}E}q\,d\mathbb P\). Since
\[
\begin{aligned}
&\|(T_nF)\circ S-T_nF\|_\infty\\
&\quad =\tfrac1n\|(JF)\circ S^n-JF\|_\infty\\
&\quad \le\tfrac2n\|F\|_\infty,
\end{aligned}
\]
the limit satisfies \((TF)\circ S=TF\), and we may define \(mF\in L^\infty(D)\) by \(TF=(mF)\circ b\). It is a positive unital contraction, since composition with \(b\) is an isometric order isomorphism onto the invariant functions.

*Equivariance and module property.* Since \(b(g^{-1}\omega)=g^{-1}b(\omega)\) and \((g^{-1}\omega)_0=g^{-1}\omega_0\), we get \(J(\lambda_gF)=(JF)\circ g^{-1}\), and because \(g\) commutes with \(S\), \(T_n(\lambda_gF)=(T_nF)\circ g^{-1}\). Weak\* continuity of composition with \(g^{-1}\) gives \(T(\lambda_gF)=(TF)\circ g^{-1}\)\(=(mF)\circ b\circ g^{-1}=(\alpha_gmF)\circ b\), which is the first identity of (2.1). For \(f\in L^\infty(D)\), \(J(fF)=(f\circ b)\,JF\) and \((f\circ b)\circ S^j=f\circ b\), so \(T_n(fF)=(f\circ b)T_nF\); multiplication by a fixed bounded function is weak\* continuous, which gives the second identity.

*The product mean.* On \(X\times X\) use the commuting shifts \(S_1=S\times\mathrm{id}\) and \(S_2=\mathrm{id}\times S\) and the averages
\[
\begin{gathered}
\frac1{nk}\sum_{i<n}\sum_{j<k}F\bigl((S^i\omega)_0,(S^j\omega')_0,\\
b(\omega),b(\omega')\bigr)
\end{gathered}
\]
over pairs \((n,k)\) directed by the product order. A weak\* cluster point \(T^{(2)}F\) is invariant under both shifts by the same telescoping estimate in each variable. An \(L^\infty\) function \(\Phi\) on \(X^2\) invariant under \(S_1\) and \(S_2\) is almost everywhere a function of \((b(\omega),b(\omega'))\). To see this, regard \(\Phi\in L^2(X)\otimes L^2(X)\) and let \(Q\) be the orthogonal projection of \(L^2(X)\) onto the \(S\)-invariant functions, which form \(L^2(X,\mathcal I)\). By Fubini's theorem almost every section \(\Phi(\cdot,\omega')\) is \(S\)-invariant, so \(\Phi\) lies in the range of \(Q\otimes1\); similarly in the range of \(1\otimes Q\). These projections commute, and their product \(Q\otimes Q\) has range \(L^2(X,\mathcal I)\otimes L^2(X,\mathcal I)\), the square integrable functions measurable for the completed product of \(\mathcal I\) with itself, which is generated up to null sets by the coordinates of \(b(\omega)\) and \(b(\omega')\). So \(T^{(2)}F=(m^{(2)}F)\circ(b\times b)\) defines \(m^{(2)}\), and the equivariance and module arguments apply in each coordinate.

*Operator fields.* Let \(F\) be a bounded operator field on \(G\times D\). Let \(K_0\subseteq K\) be the countable set of rational complex combinations of an orthonormal basis. For \(\xi,\eta\in K_0\) let \(c_{\xi,\eta}=m(\langle F(\cdot)\xi,\eta\rangle)\in L^\infty(D)\) and fix representatives. Outside one null set the countably many relations of sesquilinearity over \(\mathbb Q+i\mathbb Q\) hold, and \(|c_{\xi,\eta}(x)|\le\|F\|_\infty\|\xi\|\|\eta\|\) because \(m\) is a contraction. For such \(x\), \(c_{\cdot,\cdot}(x)\) extends to a bounded sesquilinear form on \(K\), the coefficient form of an operator \(m(F)(x)\) of norm at most \(\|F\|_\infty\); on the null set put \(m(F)(x)=0\). This defines a bounded operator field \(m(F)\), and \(\|m(F)\|_\infty\le\|F\|_\infty\). Since a positive map preserves complex conjugation, \(m(F^*)=m(F)^*\). Equivariance follows from the coefficient formula.

The module identity (2.2) needs the coefficient formula with vectors depending on \(x\). Let \(\zeta,\zeta'\) be bounded measurable maps \(D\to K\). If both are countably valued, take a countable measurable partition \((A_k)\) of \(D\) on whose pieces both are constant, and let \(\Phi(t,x)=\langle F(t,x)\zeta(x),\zeta'(x)\rangle\). On \(A_k\) the function \(\Phi\) agrees with the coefficient \(\Phi_k\) of \(F\) at the constant vectors, so the scalar module identity gives \(1_{A_k}m(\Phi)=m(1_{A_k}\Phi)\)\(=m(1_{A_k}\Phi_k)=1_{A_k}m(\Phi_k)\). Hence
\[
m(\Phi)(x)=\bigl\langle m(F)(x)\zeta(x),\zeta'(x)\bigr\rangle
\]
almost everywhere; only the module identity was used, not countable additivity of \(m\). General bounded measurable \(\zeta,\zeta'\) are uniform limits of countably valued measurable maps (choose, at each \(x\), the first element of a countable dense set within \(1/n\)), and both sides depend continuously on \(\zeta,\zeta'\) in the uniform norm. Testing \(BFC\) on constant vectors \(\xi,\eta\) with \(\zeta=C\xi\) and \(\zeta'=B^*\eta\) gives (2.2).

If \(F\) takes values in a von Neumann algebra \(A\), then (2.2) with constant \(B=c\in A'\) and \(C=1\), and with \(B=1\), \(C=c\), gives \(c\,m(F)=m(cF)=m(Fc)=m(F)\,c\) almost everywhere. Choose a countable subset of the unit ball of \(A'\) that is strongly dense in it (possible since \(K\) is separable); off one null set \(m(F)(x)\) commutes with \(A'\), so \(m(F)(x)\in A\) by the bicommutant theorem. Every step applies to \(m^{(2)}\). \(\square\)

The mean is not normal: it is a limit along a subnet and does not commute with monotone limits. Nothing below needs normality. If \(G\) is amenable, a one-point space and an invariant mean on \(G\) give a mean with the same properties (Exercise 5.1); the point of Lemma 2.1 is that it requires nothing of \(G\).

## 3. Correction of measurable cocycles

For a family \(V_g\in L^\infty(D,\mathcal U(A))\), \(g\in G\), the *defect* is
\[
\operatorname{def}(V)=\sup_{g,h\in G}\|V_g\,\alpha_g(V_h)-V_{gh}\|_\infty .
\]
The family is an *exact cocycle* when its defect is zero, that is, \(V_g(x)V_h(g^{-1}x)=V_{gh}(x)\) almost everywhere for all \(g,h\).

**Lemma 3.1** (correction of a measurable unitary cocycle). Let \(D\) and \(m\) be as in Lemma 2.1, \(A\subseteq B(K)\) a von Neumann algebra on a separable Hilbert space, and \(V_g\in L^\infty(D,\mathcal U(A))\) a family with \(e=\operatorname{def}(V)\le1/64\). There is an exact cocycle \(W_g\in L^\infty(D,\mathcal U(A))\) with
\[
\sup_g\|W_g-V_g\|_\infty\le2e,\qquad W_1=I .
\]
After deleting one null set and its countably many translates, the cocycle identities hold everywhere on a \(G\)-invariant conull set.

**Proof.** *One step.* Define fields on \(G\times D\) and their means by
\[
\begin{gathered}
H_g(t,x)=V_t(x)\,V_{g^{-1}t}(g^{-1}x)^*,\\
A_g=m(H_g).
\end{gathered}
\]
The defect inequality with \(h=g^{-1}t\) says \(\|V_t(x)-V_g(x)V_{g^{-1}t}(g^{-1}x)\|\le e\); multiplying on the right by the unitary \(V_{g^{-1}t}(g^{-1}x)^*\) gives \(\|H_g-V_g\|_\infty\le e\). By (2.2) and contractivity, \(\|A_g-V_g\|_\infty=\|m(H_g-V_g)\|_\infty\le e\), and \(\|H_g-A_g\|_\infty\le2e\). The fields \(H_g\) are unitary, the \(A_g\) are contractions in \(L^\infty(D,A)\), and a direct computation gives the exact factorization
\[
\begin{gathered}
H_{gh}=H_g\,\lambda_g(H_h),\\
m(\lambda_gH_h)=\alpha_g(A_h).
\end{gathered}
\]
Expanding the product and using (2.2) to take the fields \(A_g\) and \(\alpha_g(A_h)\), which do not depend on \(t\), out of the mean, one gets
\[
\begin{aligned}
&A_{gh}-A_g\alpha_g(A_h)\\
&\quad=m\bigl((H_g-A_g)(\lambda_gH_h-\alpha_gA_h)\bigr),\\
&I-A_g^*A_g\\
&\quad=m\bigl((H_g-A_g)^*(H_g-A_g)\bigr),
\end{aligned}
\]
and similarly \(I-A_gA_g^*=m((H_g-A_g)(H_g-A_g)^*)\). The right sides have norm at most \(4e^2\). Since \(\|A_g-V_g\|_\infty\le e<1\), each \(A_g\) is invertible in \(L^\infty(D,A)\), and its polar part
\[
V'_g=A_g(A_g^*A_g)^{-1/2}
\]
is a unitary field in \(L^\infty(D,\mathcal U(A))\); the functional calculus preserves measurability, being a uniform limit of polynomials on a fixed interval away from zero. From \(|\sqrt s-1|\le|s-1|\) we get \(\|V'_g-A_g\|_\infty=\|I-|A_g|\|_\infty\)\(\le\|I-A_g^*A_g\|_\infty\le4e^2\). Replacing the three factors in \(A_g\alpha_g(A_h)-A_{gh}\) by their polar parts costs at most \(12e^2\), so
\[
\begin{gathered}
\operatorname{def}(V')\le16e^2,\\
\sup_g\|V'_g-V_g\|_\infty\le e+4e^2 .
\end{gathered}
\]

*Iteration.* Start with \(e_0=e\) and repeat. While \(e_j\le1/64\), \(e_{j+1}\le16e_j^2\le e_j/4\), so \(e_j\le4^{-j}e\). The families converge uniformly in \(g\), in the norm \(\|\cdot\|_\infty\), to unitary fields \(W_g\) whose defect is zero, and the total change is at most
\[
\sum_{j\ge0}(e_j+4e_j^2)\le\frac{17}{16}\sum_{j\ge0}e_j\le\frac{17}{12}\,e\le2e .
\]
The identities hold almost everywhere for each of the countably many pairs \((g,h)\); a nonsingular countable group maps the union of the exceptional sets to null sets, so all identities hold on a \(G\)-invariant conull set. With \(g=h=1\) the cocycle identity says \(W_1^2=W_1\), and a unitary idempotent is \(I\). \(\square\)

## 4. Averaged intertwiners

In this section \((\Gamma,Z)\) is either \((G,D)\) with the mean \(m\) of Lemma 2.1, or \((G\times G,D\times D)\) with the separate action and the mean \(m^{(2)}\). Exact cocycles for \(\Gamma\) on \(Z\) are defined as in Section 3.

**Lemma 4.1** (averaged intertwiner). Let \(s\mapsto U_s\) be a unitary representation of \(\Gamma\) on a separable Hilbert space \(K\), and \(\Sigma_s\in L^\infty(Z,\mathcal U(K))\) an exact cocycle with
\[
\sup_{s\in\Gamma}\|\Sigma_s-U_s\|_\infty\le\delta<1 .
\]
There is \(L\in L^\infty(Z,\mathcal U(K))\) with \(\|L-I\|_\infty\le2\delta\) and
\[
L(z)\,U_s=\Sigma_s(z)\,L(s^{-1}z)\qquad(s\in\Gamma)
\]
for almost every \(z\).

**Proof.** Put \(B=m\bigl((t,z)\mapsto\Sigma_t(z)U_t^*\bigr)\), a field on \(Z\) with \(\|B-I\|_\infty\le\delta\); so \(B\) is invertible. For fixed \(s\), equivariance gives \(\alpha_s(B)=m\bigl((t,z)\mapsto\Sigma_{s^{-1}t}(s^{-1}z)U_{s^{-1}t}^*\bigr)\). By (2.2), with the field \(\Sigma_s\) on the left and the constant \(U_s^*\) on the right,
\[
\begin{aligned}
&\Sigma_s\,\alpha_s(B)\,U_s^*\\
&=m\bigl((t,z)\mapsto\Sigma_s(z)\Sigma_{s^{-1}t}(s^{-1}z)\\
&\qquad\qquad\cdot U_{s^{-1}t}^*U_s^*\bigr)=B,
\end{aligned}
\]
because \(\Sigma_s(z)\Sigma_{s^{-1}t}(s^{-1}z)=\Sigma_t(z)\) and \(U_{s^{-1}t}^*U_s^*=U_t^*\). So \(BU_s=\Sigma_s\alpha_s(B)\). Taking adjoints and multiplying, \(U_s^*B^*BU_s=\alpha_s(B)^*\Sigma_s^*\Sigma_s\alpha_s(B)\)\(=\alpha_s(B^*B)\), so \(|B|^{-1}=U_s\,\alpha_s(|B|^{-1})\,U_s^*\). Let \(L=B|B|^{-1}\), a unitary field. Then
\[
\begin{aligned}
\Sigma_s\alpha_s(L)&=\Sigma_s\alpha_s(B)\,\alpha_s(|B|^{-1})\\
&=BU_s\,\alpha_s(|B|^{-1})\\
&=B|B|^{-1}U_s=LU_s .
\end{aligned}
\]
Finally \((1-\delta)\le|B|\le(1+\delta)\), so \(\|L-B\|_\infty=\|I-|B|\|_\infty\le\delta\) and \(\|L-I\|_\infty\le2\delta\). \(\square\)

## 5. Exercises

**Exercise 5.1.** Let \(G\) be amenable, with a left-invariant mean \(m_G\) on \(\ell^\infty(G)\). Show that the one-point space \(D=\{x_0\}\) and \(m(F)=m_G(t\mapsto F(t,x_0))\) satisfy (2.1), and that Lemma 3.1 then corrects every family of unitaries \(v_g\) with \(\sup_{g,h}\|v_gv_h-v_{gh}\|\le1/64\) into a unitary representation within \(2e\).

**Exercise 5.2.** Show that \(m(F)=f\) when \(F(t,x)=f(x)\) does not depend on \(t\), and that \(\alpha_g(m(F))=m(F)\) when \(\lambda_gF=F\).

**Exercise 5.3.** Check the factorization \(H_{gh}=H_g\,\lambda_g(H_h)\) in the proof of Lemma 3.1.

**Exercise 5.4.** Verify the estimate \(\operatorname{def}(V')\le16e^2\) by writing \(V'_g\alpha_g(V'_h)-V'_{gh}\) as \(A_g\alpha_g(A_h)-A_{gh}\) plus three differences.

**Exercise 5.5.** Show that the intertwiner of Lemma 4.1 for the trivial cocycle \(\Sigma_s=U_s\) is \(L=I\).

## 6. Solutions

**Solution 5.1.** For a one-point space \(\alpha_g\) is the identity and \(\lambda_gF(t)=F(g^{-1}t)\), so (2.1) is the invariance of \(m_G\) and its linearity. Fields over a point are single operators, and an exact cocycle over a point is a representation. Lemma 3.1 uses only (2.1), (2.2) and the contractivity of \(m\).

**Solution 5.2.** \(F=f\cdot1\) with \(1\) the constant function, so \(m(F)=f\,m(1)=f\). If \(\lambda_gF=F\), then \(m(F)=m(\lambda_gF)=\alpha_g(mF)\).

**Solution 5.3.** \(H_g(t,x)\,H_h(g^{-1}t,g^{-1}x)\) equals
\[
\begin{gathered}
V_t(x)V_{g^{-1}t}(g^{-1}x)^*\\
\cdot V_{g^{-1}t}(g^{-1}x)V_{h^{-1}g^{-1}t}(h^{-1}g^{-1}x)^*,
\end{gathered}
\]
and the middle factors cancel, leaving \(H_{gh}(t,x)\).

**Solution 5.4.** \(V'_g\alpha_g(V'_h)-V'_{gh}\) equals \(A_g\alpha_g(A_h)-A_{gh}\) plus \((V'_g-A_g)\alpha_g(V'_h)\), \(A_g\alpha_g(V'_h-A_h)\) and \(A_{gh}-V'_{gh}\). The first has norm at most \(4e^2\) and each of the others at most \(4e^2\), since \(\|A_g\|\le1\) and \(\alpha_g\) preserves norms.

**Solution 5.5.** \(B=m(U_sU_s^*)=m(1)=I\), so \(L=I\).

## References

- [OpenAI-289] OpenAI, Universal strong Kadison–Kastler stability, preprint, 23 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/Universal-strong-Kadison-Kastler-stability-September-23-2026
- [BOT] M. Burger, N. Ozawa, A. Thom, On Ulam stability, Israel Journal of Mathematics 193 (2013), 109–129. https://arxiv.org/abs/1010.0565
- [AEG] S. Adams, G. A. Elliott, T. Giordano, Amenable actions of groups, Transactions of the American Mathematical Society 344 (1994), 803–822. https://doi.org/10.1090/S0002-9947-1994-1250814-5
