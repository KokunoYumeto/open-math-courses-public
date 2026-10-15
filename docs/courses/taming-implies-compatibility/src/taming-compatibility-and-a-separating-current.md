# Taming, compatibility and a separating current

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

An almost complex structure \(J\) on a manifold is a smooth field of linear maps \(J_x\colon T_xX\to T_xX\) with \(J_x^2=-1\). A two-form \(\omega\) *tames* \(J\) if \(\omega(v,Jv)>0\) for every nonzero tangent vector \(v\); it is *compatible* with \(J\) if it tames \(J\) and in addition \(\omega(Ju,Jv)=\omega(u,v)\). A taming form is nondegenerate, so a closed taming form is symplectic. Donaldson asked whether, on a closed four-manifold, an almost complex structure that is tamed by a symplectic form admits a compatible symplectic form [Donaldson, Section 5.2, Question 2]. [OpenAI-TC] answers this affirmatively. This course gives the proof.

The proof is by contradiction. If no compatible form exists, separation produces a positive current that annihilates every closed invariant two-form; a correction by an anti-invariant distribution makes the sum annihilate every closed two-form. This lesson constructs both. The second lesson proves that the positive current has quadratic mass growth, the third that the correction is square integrable and that nearby complex lines of the current are close on average, the fourth and fifth that the part of the current carried by points of positive two-dimensional density is closed, and then that the correction vanishes. The positive current then annihilates the taming form, which is impossible.

- Two-forms at a point of an almost Hermitian four-manifold (Lemmas 1.1 and 1.2), and a Borel choice of measures with given barycentres (Lemma 1.3).
- The theorem (Theorem 2.1).
- A closed lift of anti-invariant forms (Lemmas 3.1 and 3.2, Proposition 3.3, Lemma 3.4).
- Positive functionals on invariant forms and their measures (Proposition 4.1).
- The separating current (Proposition 5.1).

The lesson follows [OpenAI-TC, Sections 1 and 2]. Elliptic operators on closed manifolds are those of the lesson [Symbols, finite defects, and the index on a closed manifold](course:elliptic-boundary-reduction/global-elliptic-symbol-index) (course *Elliptic boundary reduction*). We apply it to complexified bundles of real forms; the Riemannian volume identifies half-densities with functions, and an operator with real coefficients maps real sections to real sections.

## 1. Two-forms at a point

Throughout the course, \(X\) is a closed connected smooth four-manifold, \(J\) a smooth almost complex structure on \(X\), and \(g\) a smooth Riemannian metric with \(g(Ju,Jv)=g(u,v)\). Such a *\(J\)-Hermitian* metric exists: for any Riemannian metric \(h\), take \(g(u,v)=h(u,v)+h(Ju,Jv)\). The *fundamental form* is
\[
F(u,v)=g(Ju,v) .
\]
It is skew, since \(g(Jv,u)=g(J^2v,Ju)=-g(Ju,v)\).

We orient \(X\) by \(J\): a basis \((v,Jv,w,Jw)\) of \(T_xX\) is declared positive. Such bases correspond to the bases \((v,w)\) of the complex vector space \((T_xX,J)\), two of them differ by a complex linear map, and a complex linear map has positive real determinant \(|\det_{\mathbb C}|^2\); so this is an orientation.

A *unitary frame* at \(x\) is an orthonormal basis of the form \((e_1,Je_1,e_3,Je_3)\). Every unit vector \(v\) is the first vector of one. Indeed \(g(v,Jv)=g(Jv,J^2v)=-g(Jv,v)\) forces \(g(v,Jv)=0\); for a unit vector \(w\) orthogonal to \(v\) and \(Jv\), the unit vector \(Jw\) is orthogonal to \(v\), \(Jv\) and \(w\), because \(g(Jw,v)=-g(w,Jv)\) and \(g(Jw,Jv)=g(w,v)\). Unitary frames are positive. The same construction applied to smooth vector fields with the Gram–Schmidt process gives a smooth unitary frame field near every point.

The metric identifies bivectors with two-forms. We write \(\alpha(\ell)=\langle\alpha,\ell\rangle\) for a two-form \(\alpha\) and a bivector \(\ell\), so that \(\alpha(u\wedge v)=\alpha(u,v)\). For an orthonormal basis \(e_1,\dots,e_4\) with dual basis \(e^1,\dots,e^4\), the forms \(e^{ij}=e^i\wedge e^j\), \(i<j\), are orthonormal. The Hodge star satisfies \(\alpha\wedge*\beta=\langle\alpha,\beta\rangle\,dV_g\). On two-forms, \(*\) is a self-adjoint isometry with \(**=1\), and for a positive orthonormal basis
\[
*e^{12}=e^{34},\quad *e^{13}=e^{42},\quad *e^{14}=e^{23} .
\]
The self-dual and anti-self-dual forms \(\Lambda^\pm=\{\alpha:*\alpha=\pm\alpha\}\) are orthogonal and three-dimensional. We write \(\alpha^+=\frac12(\alpha+*\alpha)\).

The structure \(J\) acts on two-forms by \(\alpha\mapsto\alpha(J\,\cdot,J\,\cdot)\), an isometric involution. A two-form is *invariant* if \(\alpha(Ju,Jv)=\alpha(u,v)\), and *anti-invariant* if \(\alpha(Ju,Jv)=-\alpha(u,v)\). Put
\[
(R\alpha)(u,v)=\tfrac12\bigl(\alpha(u,v)-\alpha(Ju,Jv)\bigr) .
\]
Then \(R\) is the orthogonal projection onto the anti-invariant forms, and \(1-R\) the orthogonal projection onto the invariant forms. The same formulas act on bivectors.

Finally let \(\mathscr C\to X\) be the bundle of *unit complex-line bivectors*,
\[
\mathscr C_x=\{v\wedge Jv:\ v\in T_xX,\ |v|=1\},
\]
and for \(\ell=v\wedge Jv\in\mathscr C_x\) let \(L_\ell=\operatorname{span}(v,Jv)\), the oriented plane of \(\ell\). The space \(\mathscr C\) is compact, as the image of the unit sphere bundle under \(v\mapsto v\wedge Jv\).

**Lemma 1.1** (pointwise algebra; [OpenAI-TC, (2.1)]). Let \((e_1,e_2,e_3,e_4)\) be a unitary frame, \(e_2=Je_1\), \(e_4=Je_3\).

1. \(F=e^{12}+e^{34}\), \(*F=F\) and \(|F|^2=2\).
2. The anti-invariant forms are spanned by \(e^{13}-e^{24}\) and \(e^{14}+e^{23}\), and they are self-dual. The invariant forms are spanned by \(e^{12}\), \(e^{34}\), \(e^{13}+e^{24}\), \(e^{14}-e^{23}\). Every anti-self-dual form is invariant, so \(R\) vanishes on \(\Lambda^-\) and \(R\circ*=R\).
3. Every \(\ell\in\mathscr C_x\) is invariant, and \(|\ell|=1\), \(F(\ell)=1\), \(\ell^+=F/2\), \(*\ell=F-\ell\).

*Proof.* (1) \(F(e_i,e_j)=g(Je_i,e_j)\), and \(Je_1=e_2\), \(Je_2=-e_1\), \(Je_3=e_4\), \(Je_4=-e_3\). Thus \(F(e_1,e_2)=F(e_3,e_4)=1\), and \(F(e_i,e_j)=0\) for the other pairs \(i<j\). The rest follows from the formulas for \(*\).

(2) The covectors \(e^i\circ J\) are \(-e^2,\ e^1,\ -e^4,\ e^3\) for \(i=1,2,3,4\), and \(\theta\wedge\eta\mapsto(\theta\circ J)\wedge(\eta\circ J)\) is the action on decomposable forms. It fixes \(e^{12}\) and \(e^{34}\), exchanges \(e^{13}\) and \(e^{24}\), and maps \(e^{14}\mapsto-e^{23}\) and \(e^{23}\mapsto-e^{14}\). This gives both spans. From \(*e^{24}=-e^{13}\) and \(*e^{23}=e^{14}\), the two anti-invariant basis forms are self-dual. The space \(\Lambda^-\) is spanned by \(e^{12}-e^{34}\), \(e^{13}+e^{24}\) and \(e^{14}-e^{23}\), which are invariant. Since \(R\) is the orthogonal projection onto a subspace of \(\Lambda^+\) and vanishes on \(\Lambda^-\), \(R(*\alpha)=R(\alpha^+-\alpha^-)=R\alpha^+=R\alpha\) when \(\alpha=\alpha^++\alpha^-\).

(3) Write \(\ell=v\wedge Jv\) and choose the unitary frame with \(e_1=v\). Then \(\ell=e^{12}\), and all claims follow from (1) and (2). \(\blacksquare\)

We also need a matrix description of invariant bivectors. Write \(e_{ij}=e_i\wedge e_j\).

**Lemma 1.2** (invariant bivectors as Hermitian matrices). Fix a unitary frame. For an invariant bivector
\[
\begin{aligned}
A&=a\,e_{12}+b\,e_{34}\\
&\quad+p\,(e_{14}-e_{23})+q\,(e_{13}+e_{24})
\end{aligned}
\]
put
\[
M(A)=\begin{pmatrix}a&p+iq\\p-iq&b\end{pmatrix} .
\]

1. \(M\) is a linear bijection from invariant bivectors onto Hermitian \(2\times2\) matrices, \(\langle A,B\rangle=\operatorname{tr}(M(A)M(B))\), and \(M(F)=I\).
2. For \(v=x_1e_1+y_1e_2+x_2e_3+y_2e_4\) put \(z=(x_1+iy_1,\,x_2+iy_2)\in\mathbb C^2\). Then \(Jv\) corresponds to \(iz\), \(|v|=|z|\), and \(M(v\wedge Jv)=zz^*\).
3. An invariant two-form \(\alpha\) satisfies \(\alpha(v,Jv)\ge0\) for all \(v\) if and only if \(M(\alpha)\) is positive semidefinite.
4. Let \(A\) be invariant with \(M(A)\ge0\) and \(\operatorname{tr}M(A)=1\). Then \(A=t_1\ell_1+t_2\ell_2\) with \(t_1\ge t_2\ge0\), \(t_1+t_2=1\), \(\ell_k=u_k\wedge Ju_k\), and \((u_1,Ju_1,u_2,Ju_2)\) a unitary frame. Moreover \(|A|^2=t_1^2+t_2^2\le1\), with equality exactly when \(A\in\mathscr C_x\). The skew matrix of \(A\) in an orthonormal basis has rank \(2\) if \(t_2=0\) and rank \(4\) if \(t_2>0\); if \(t_2=0\), its column space is the plane \(L_{\ell_1}\).

*Proof.* (1) The four bivectors in the definition of \(A\) are orthogonal, with squared norms \(1,1,2,2\). With \(w=p+iq\) and \(w'=p'+iq'\),
\[
\begin{aligned}
&\operatorname{tr}(M(A)M(B))\\
&\quad=aa'+bb'+2\operatorname{Re}(w\bar w') ,
\end{aligned}
\]
which is \(aa'+bb'+2pp'+2qq'=\langle A,B\rangle\). Both spaces are four-dimensional and \(M\) is injective. \(F=e_{12}+e_{34}\) gives \(M(F)=I\).

(2) \(Jv=-y_1e_1+x_1e_2-y_2e_3+x_2e_4\), whose coordinates are \(iz\). Expanding \(v\wedge Jv\) in the basis \(e_{ij}\): the coefficient of \(e_{12}\) is \(|z_1|^2\), that of \(e_{34}\) is \(|z_2|^2\), those of \(e_{14}\) and \(e_{23}\) are \(\pm(x_1x_2+y_1y_2)\), and those of \(e_{13}\) and \(e_{24}\) are both \(x_2y_1-x_1y_2\). Since \(z_1\bar z_2=(x_1x_2+y_1y_2)+i(x_2y_1-x_1y_2)\), this is \(M(v\wedge Jv)=zz^*\).

(3) By (1) and (2), \(\alpha(v,Jv)=\langle\alpha,v\wedge Jv\rangle\), which is \(\operatorname{tr}(M(\alpha)zz^*)=z^*M(\alpha)z\).

(4) Diagonalize: \(M(A)=t_1z^{(1)}z^{(1)*}+t_2z^{(2)}z^{(2)*}\) with orthonormal \(z^{(1)},z^{(2)}\in\mathbb C^2\). Let \(u_k\) correspond to \(z^{(k)}\). By (2) and injectivity, \(A=t_1u_1\wedge Ju_1+t_2u_2\wedge Ju_2\). For vectors \(u,u'\) with coordinates \(z,z'\), the Hermitian product is \(z'^*z=g(u,u')+i\,g(u,Ju')\), so \((u_1,Ju_1,u_2,Ju_2)\) is a unitary frame. Then \(|A|^2=\operatorname{tr}(M(A)^2)=t_1^2+t_2^2\), and \(t_1^2+t_2^2=1-2t_1t_2\), which is \(1\) exactly when \(t_2=0\), that is \(A=\ell_1\). In the unitary frame \(f=(u_1,Ju_1,u_2,Ju_2)\), \(A=t_1f_{12}+t_2f_{34}\), whose skew matrix has rank \(2\) or \(4\) as stated and, for \(t_2=0\), column space \(\operatorname{span}(f_1,f_2)\). An orthogonal change of basis conjugates the matrix and moves the column space with the basis. \(\blacksquare\)

Let \(\mathscr K_x\) be the set of invariant bivectors \(A\) at \(x\) with \(\langle\alpha,A\rangle\ge0\) for every invariant \(\alpha\) with \(\alpha(v,Jv)\ge0\) for all \(v\), and with \(\langle F,A\rangle=1\). By Lemma 1.2(1) and (3), these are the \(A\) with \(M(A)\ge0\) and \(\operatorname{tr}M(A)=1\) in any unitary frame. By Lemma 1.2(4), \(\mathscr K_x\) is the convex hull of \(\mathscr C_x\), and \(|A|\le1\) on it. Since \(*\ell=F-\ell\) and \(\ell^+=F/2\) are affine identities, also, for \(A\in\mathscr K_x\),
\[
*A=F-A,\qquad A^+=F/2 .
\]

**Lemma 1.3** (measures with a given barycentre). For \(x\in X\) and \(A\in\mathscr K_x\) there is a probability measure \(\kappa_{x,A}\) on \(\mathscr C_x\) with \(\int\ell\,d\kappa_{x,A}(\ell)=A\), with \(\kappa_{x,A}=\delta_A\) when \(A\in\mathscr C_x\), and such that \((x,A)\mapsto\int f\,d\kappa_{x,A}\) is Borel for every continuous function \(f\) on \(\mathscr C\).

*Proof.* With \(t_1,t_2\) as in Lemma 1.2(4), \((t_1-t_2)^2=2(t_1^2+t_2^2)-(t_1+t_2)^2\), which is \(2|A|^2-1\). If \(A\ne F/2\), then \(t_1>t_2\), and \(F=\ell_1+\ell_2\) gives
\[
\ell_1=\frac{A-t_2F}{t_1-t_2},\qquad \ell_2=F-\ell_1 ,
\]
with \(t_{1,2}=\frac12\bigl(1\pm(2|A|^2-1)^{1/2}\bigr)\). Put \(\kappa_{x,A}=t_1\delta_{\ell_1}+t_2\delta_{\ell_2}\); it depends continuously on \((x,A)\) where \(A\ne F/2\). If \(A=F/2\), let \(\kappa_{x,A}\) be the image of the normalized rotation-invariant measure \(\sigma_x\) on the unit sphere of \(T_xX\) under \(v\mapsto v\wedge Jv\). Its barycentre \(\beta\) is invariant under the orthogonal maps of \(T_xX\) commuting with \(J\), which act on \(M\) by \(M\mapsto UMU^*\) with \(U\) unitary. A Hermitian matrix commuting with every unitary matrix is a multiple of \(I\), and \(\operatorname{tr}M(\beta)=\int|z|^2\,d\sigma_x=1\). So \(M(\beta)=I/2\) and \(\beta=F/2\). The function \(x\mapsto\int f(v\wedge Jv)\,d\sigma_x(v)\) is continuous, as one sees in a local orthonormal frame. The two cases are a Borel partition. \(\blacksquare\)

## 2. The theorem

**Theorem 2.1** ([OpenAI-TC, Theorem 1.1]). Let \(J\) be a smooth almost complex structure on a closed connected smooth four-manifold \(X\). If a closed two-form tames \(J\), then a closed two-form is compatible with \(J\).

The course proves Theorem 2.1 from one named hypothesis, the short-time asymptotics of the heat kernel of the Hodge Laplacian, stated as (HK) in [Regularization and angular control](regularization-and-angular-control.md); the proof is completed in Theorem 5.1 of [Closedness of the density part and the proof](closedness-of-the-density-part-and-the-proof.md). A closed compatible form is a symplectic form, and the structure \(J\) is the given one. The theorem says nothing about the cohomology class of the compatible form. The projection \(1-R\) keeps taming:
\[
\begin{aligned}
&((1-R)\omega)(v,Jv)\\
&\quad=\tfrac12\bigl(\omega(v,Jv)+\omega(Jv,-v)\bigr)\\
&\quad=\omega(v,Jv) .
\end{aligned}
\]
But \((1-R)\omega\) is in general not closed, and this is the difficulty. The question is special to dimension four: in higher dimensions a generic almost complex structure has no compatible symplectic form even locally [Donaldson, Section 5.2]. Earlier work answered the question in special cases, for instance for integrable \(J\) and, when \(b_2^+=1\), for generic \(J\); see [OpenAI-TC, Section 1] for these results. They are not used here.

From now on assume, for a contradiction, that \(\omega\) is a closed form taming \(J\) and that no closed form is compatible with \(J\).

## 3. A closed lift of anti-invariant forms

Let \(\Lambda^-_J\) be the rank-two bundle of anti-invariant two-forms, and \(d^*\) the formal adjoint of \(d\) for the \(L^2\) products \(\langle\alpha,\beta\rangle_{L^2}=\int_X\langle\alpha,\beta\rangle\,dV_g\).

**Lemma 3.1.** On two-forms, \(d^*=-*d*\). In particular a self-dual two-form \(a\) satisfies \(d^*a=-*da\), so \(d^*a=0\) exactly when \(da=0\).

*Proof.* For a one-form \(\beta\) and a two-form \(a\), \(d(\beta\wedge*a)=d\beta\wedge*a-\beta\wedge d{*a}\). By Stokes' theorem on the closed manifold \(X\),
\[
\langle d\beta,a\rangle_{L^2}=\int_Xd\beta\wedge*a=\int_X\beta\wedge d{*a} .
\]
On three-forms of a four-manifold \(**=-1\), so \(d{*a}=*\gamma\) with \(\gamma=-*d{*a}\), and \(\beta\wedge*\gamma=\langle\beta,\gamma\rangle\,dV_g\). Hence \(d^*a=\gamma\). \(\blacksquare\)

Consider the second-order differential operator on sections of \(\Lambda^-_J\)
\[
\mathcal L a=R\,dd^*a .
\]

**Lemma 3.2** (the principal symbol). For a covector \(\xi\) and \(a\in\Lambda^-_J\) at the same point,
\[
R\bigl(\xi\wedge\iota_{\xi}a\bigr)=\tfrac12|\xi|^2a ,
\]
where \(\iota_\xi\) is contraction with the vector dual to \(\xi\). So \(\mathcal L\) has principal symbol \(\frac12|\xi|^2\,\mathrm{id}\) and is elliptic of order two.

*Proof.* For every two-form \(a\), \(\xi\wedge\iota_\xi a+\iota_\xi(\xi\wedge a)=|\xi|^2a\). In dimension four, \(*(\xi\wedge\iota_\xi a)=\iota_\xi(\xi\wedge*a)\) for two-forms \(a\): both sides are quadratic in \(\xi\) and commute with rotations, so it suffices to take \(\xi=e^1\), where the four cases \(a=e^{12},e^{34},e^{13},e^{24}\) and the two similar ones are checked with the formulas for \(*\). For self-dual \(a\) this gives
\[
\begin{aligned}
\bigl(\xi\wedge\iota_\xi a\bigr)^+&=\tfrac12\bigl(\xi\wedge\iota_\xi a+\iota_\xi(\xi\wedge a)\bigr)\\
&=\tfrac12|\xi|^2a .
\end{aligned}
\]
Since \(R\) vanishes on \(\Lambda^-\) (Lemma 1.1(2)), \(R\beta=R\beta^+\), and \(Ra=a\). The symbols of \(d\) and \(d^*\) are \(i\xi\wedge\) and \(-i\iota_\xi\), so that of \(dd^*\) is \(\xi\wedge\iota_\xi\). \(\blacksquare\)

**Proposition 3.3** (the generalized inverse). (1) For smooth sections \(a,b\) of \(\Lambda^-_J\), \(\langle\mathcal La,b\rangle_{L^2}=\langle d^*a,d^*b\rangle_{L^2}\). (2) The kernel \(N\) of \(\mathcal L\) is a finite-dimensional space of smooth closed forms. (3) Let \(H\) be the \(L^2\)-orthogonal projection onto \(N\). There is an operator \(G\) of order \(-2\) on sections of \(\Lambda^-_J\), with real coefficients, such that
\[
\begin{gathered}
\mathcal LG=G\mathcal L=1-H,\\
GH=HG=0 .
\end{gathered}
\]

*Proof.* (1) \(R\) is a pointwise orthogonal projection and \(Rb=b\), so \(\langle R\,dd^*a,b\rangle=\langle dd^*a,b\rangle=\langle d^*a,d^*b\rangle\).

(2) By Lemma 3.2 and (I5) of [Symbols, finite defects, and the index on a closed manifold](course:elliptic-boundary-reduction/global-elliptic-symbol-index), the kernel of \(\mathcal L\) on every Sobolev space is a finite-dimensional space of smooth sections. For \(a\in N\), (1) gives \(\|d^*a\|^2=0\), and \(da=0\) by Lemma 3.1, since anti-invariant forms are self-dual.

(3) By (1), \(\mathcal L\) is formally self-adjoint, so by (I7) of that lesson the range of \(\mathcal L\colon H^s\to H^{s-2}\) consists of the elements annihilating \(N\). Put \(\mathcal J=\mathcal L+H\). It is injective: if \(\mathcal Lu+Hu=0\), pairing with \(e\in N\) gives \(0=\langle u,\mathcal Le\rangle+\langle u,e\rangle=\langle u,e\rangle\), so \(Hu=0\), then \(\mathcal Lu=0\) and \(u=Hu=0\). It is surjective: for \(f\in H^{s-2}\), \(f-Hf=\mathcal Lu\) with \(Hu=0\) after replacing \(u\) by \(u-Hu\), and then \(\mathcal J(u+Hf)=f\). The inverse \(\mathcal J^{-1}\) is an operator of order \(-2\), by the parametrix argument following (I9) in that lesson. Since \(\mathcal LH=0\) and \(H\mathcal L=0\) (the latter because \(\mathcal L\) is formally self-adjoint), \(\mathcal JH=H\mathcal J=H\), so \(\mathcal J^{-1}H=H\mathcal J^{-1}=H\). Put \(G=\mathcal J^{-1}-H\). Then
\[
\mathcal LG=(\mathcal J-H)\mathcal J^{-1}-\mathcal LH=1-H ,
\]
and likewise \(G\mathcal L=1-H\), \(GH=H-H=0\), \(HG=0\). \(H\) has a smooth kernel \(\sum_ke_k(x)\langle\cdot,e_k\rangle\) for an orthonormal basis \((e_k)\) of \(N\), so \(G\) has order \(-2\). All the operators commute with complex conjugation. \(\blacksquare\)

**Lemma 3.4** (a closed lift; [OpenAI-TC, Lemma 2.1]). The operator \(B=dd^*G+H\), from sections of \(\Lambda^-_J\) to two-forms, has order zero and satisfies
\[
dB=0,\qquad RB=\mathrm{id} .
\]

*Proof.* \(dd^*\) has order two and \(G\) order \(-2\), so their composite has order zero (products of operators between bundles: Sections 5 and 13 of [Detecting regularity without choosing coordinates](course:elliptic-boundary-reduction/geometric-microlocal-calculus), same course). \(d(dd^*G)=0\), and \(dH=0\) because \(N\) consists of closed forms. Finally \(RB=\mathcal LG+RH=1-H+H\). \(\blacksquare\)

So every smooth anti-invariant form \(a\) is the anti-invariant part of the closed form \(Ba\). The operator \(\mathcal L\) is the projected operator used by Lejmi for local compatibility in dimension four [OpenAI-TC, Section 2]. The lift alone does not give positivity, which is the content of the rest of the course.

## 4. Positive functionals on invariant forms

Let \(\Omega^2(X)\) be the space of smooth two-forms, with the topology of uniform convergence of all derivatives in charts. Call an invariant form \(\alpha\) *semidefinite* if \(\alpha(v,Jv)\ge0\) for all \(v\), and *positive definite* if \(\alpha(v,Jv)>0\) for all \(v\ne0\). For a two-form \(\alpha\) put \(\|\alpha\|_\infty=\sup_x|\alpha_x|\).

**Proposition 4.1** (measure representation; [OpenAI-TC, proof of Proposition 2.2]). Let \(P\) be a linear functional on \(\Omega^2(X)\) with \(P(R\alpha)=0\) for all \(\alpha\), \(P(\alpha)\ge0\) for every semidefinite invariant \(\alpha\), and \(P(F)=1\). Then there are a positive Borel measure \(\mu\) on \(X\) with \(\mu(X)=1\), a Borel field \(x\mapsto A(x)\in\mathscr K_x\), and a Borel probability measure \(\lambda\) on \(\mathscr C\) whose projection to \(X\) is \(\mu\), such that for every \(\alpha\in\Omega^2(X)\)
\[
\begin{aligned}
P(\alpha)&=\int_X\langle\alpha_x,A(x)\rangle\,d\mu(x)\\
&=\int_{\mathscr C}\alpha_x(\ell)\,d\lambda(x,\ell) .
\end{aligned}
\]
In particular \(P(bF)=\int_Xb\,d\mu\) for every smooth function \(b\), and \(|P(\alpha)|\le\|\alpha\|_\infty\).

*Proof.* *The trace measure.* Choose finitely many open sets \(U_j\) covering \(X\), each a coordinate chart carrying a smooth unitary frame field, a smooth partition of unity \(\chi_j\) subordinate to them, and \(\psi_j\in C^\infty_c(U_j)\) with \(0\le\psi_j\le1\), equal to one on the support of \(\chi_j\). For \(b\ge0\) in \(C^\infty_c(U_j)\), \(\chi_jbF\) is semidefinite, so \(b\mapsto P(\chi_jbF)\) is a positive linear form on \(C^\infty_c(U_j)\). By Theorem 4.1 of [Order, positivity and distributional limits](course:AN-01/reader/AN01-U008) (course *Distributions, kernels and analytic singularities*) it is integration against a positive Radon measure \(\nu_j\) on \(U_j\). Put \(\mu=\sum_j\psi_j\nu_j\), each term extended by zero. For smooth \(b\) on \(X\), \(P(bF)=\sum_jP(\chi_j\psi_jbF)=\int b\,d\mu\). Taking \(b=1\) gives \(\mu(X)=1\).

*Coefficient densities.* Fix \(j\), write \(U=U_j\), and let \(\varphi\) be a smooth invariant form on \(U\) whose matrix \(M(\varphi)\) in the frame has operator norm at most one at every point. For real \(b\in C^\infty_c(U)\) and \(\varepsilon>0\), the form \(\sqrt{b^2+\varepsilon^2}\,F\pm b\varphi\) has matrix \(\sqrt{b^2+\varepsilon^2}\,I\pm bM(\varphi)\ge0\), hence is semidefinite. Applying \(P\) and letting \(\varepsilon\to0\) gives \(|P(b\varphi)|\le\int|b|\,d\mu\). So \(b\mapsto\int b\,d\mu\pm P(b\varphi)\) are positive linear forms on \(C^\infty_c(U)\), given by positive Radon measures \(\rho_\pm\) with \(\rho_++\rho_-=2\mu\) on \(U\) (by the uniqueness in Corollary 3.3 of the same lesson). Then \(\rho_\pm\le2\mu\), so \(\rho_\pm\) are absolutely continuous with respect to \(\mu\), and by the Radon–Nikodym theorem ([Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10); [Fremlin, Measure Theory, Volume 2, Section 232](https://www1.essex.ac.uk/maths/people/fremlin/cont23.htm)) \(\rho_\pm=h_\pm\mu\) with \(0\le h_\pm\le2\) and \(h_++h_-=2\) almost everywhere. Hence
\[
\begin{gathered}
P(b\varphi)=\int b\,a_\varphi\,d\mu,\\
a_\varphi=\tfrac12(h_+-h_-),\qquad|a_\varphi|\le1 .
\end{gathered}
\]

*The field \(A\).* Apply this to the four forms with matrices \(\operatorname{diag}(1,0)\), \(\operatorname{diag}(0,1)\), \(\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)\) and \(\bigl(\begin{smallmatrix}0&i\\-i&0\end{smallmatrix}\bigr)\), a basis of the invariant forms. Let \(A(x)\) be the invariant bivector whose inner products with these four forms are the four densities. Then \(P(b\varphi)=\int b\langle\varphi,A\rangle\,d\mu\) for every smooth invariant \(\varphi\) on \(U\) and every \(b\in C^\infty_c(U)\). With \(\varphi=F\), \(\langle F,A\rangle=1\) almost everywhere. For \(\zeta\) in a countable dense subset of the unit sphere of \(\mathbb C^2\), the form with constant matrix \(\zeta\zeta^*\) is semidefinite, so \(\zeta^*M(A)\zeta\ge0\) almost everywhere; by continuity in \(\zeta\), \(M(A)\ge0\) almost everywhere. Two charts give the same \(A\) almost everywhere on their overlap, since both satisfy the same identity. Redefining \(A=F/2\) on a \(\mu\)-null Borel set, \(A(x)\in\mathscr K_x\) for every \(x\).

*The representation.* Let \(\lambda\) be the measure \(\int_X\kappa_{x,A(x)}\,d\mu(x)\) on \(\mathscr C\), with \(\kappa\) from Lemma 1.3. Explicitly, on the Borel set where \(A\ne F/2\) it is the sum of the images of \(t_1\mu\) and \(t_2\mu\) under the Borel maps \(x\mapsto\ell_1(x)\) and \(x\mapsto\ell_2(x)\), and on the rest it is the image of \(\mu\otimes\sigma\) under \((x,v)\mapsto v\wedge Jv\) (image measures and product measures: Fremlin, Volume 2, [Section 234](https://www1.essex.ac.uk/maths/people/fremlin/cont23.htm) and [Section 251](https://www1.essex.ac.uk/maths/people/fremlin/cont25.htm)). Its projection is \(\mu\), and \(\int\ell\,d\kappa_{x,A(x)}=A(x)\) gives the second equality. For the first, \(P(\alpha)=P((1-R)\alpha)\), which is \(\sum_jP(\chi_j(1-R)\alpha)\), and each term is \(\int\chi_j\langle(1-R)\alpha,A\rangle\,d\mu\). Since \(A\) is invariant, \(\langle R\alpha,A\rangle=\langle\alpha,RA\rangle=0\). Finally \(|\langle\alpha_x,A(x)\rangle|\le|\alpha_x|\,|A(x)|\le|\alpha_x|\). \(\blacksquare\)

We call \(\mu\) the *trace measure* and \(A\) the *polarization* of \(P\), and write \(\lambda_x=\kappa_{x,A(x)}\) for the measures on the fibers, so that \(\lambda=\int\lambda_x\,d\mu(x)\).

## 5. The separating current

A *two-current* is a linear functional on \(\Omega^2(X)\); it is *closed* if it annihilates every exact two-form \(d\beta\). Pointwise operations act on currents by duality: \((RS)(\alpha)=S(R\alpha)\) and \((*S)(\alpha)=S(*\alpha)\). Sobolev spaces of forms are those of Section 1 of [Symbols, finite defects, and the index on a closed manifold](course:elliptic-boundary-reduction/global-elliptic-symbol-index); by (I1) there, \(H^3\) embeds continuously in the continuous forms, since \(3>\dim X/2\).

**Proposition 5.1** (the separating current; [OpenAI-TC, Proposition 2.2]). Under the assumption at the end of Section 2, there are linear functionals \(P\), \(Q\), \(T\) on \(\Omega^2(X)\) and \(\mu\), \(A\), \(\lambda\) as in Proposition 4.1 such that:

1. \(P(\alpha)=\int_{\mathscr C}\alpha_x(\ell)\,d\lambda(x,\ell)\), and \(P\) annihilates every closed invariant two-form;
2. \(T=P+Q\), \(RP=0\), \(RQ=Q\) and \(*Q=Q\);
3. \(T(\alpha)=0\) for every closed two-form \(\alpha\); in particular \(T\) is closed;
4. \(P\), \(Q\) and \(T\) extend continuously to \(H^3\), that is, they are elements of \(H^{-3}\).

*Proof.* Let \(V\) be the space of smooth invariant two-forms, a closed subspace of \(\Omega^2(X)\). Let \(K\subseteq V\) be the set of positive definite forms and \(W\subseteq V\) the subspace of closed invariant forms. \(K\) is convex and nonempty (\(F\in K\)). It is open: if \(a\in K\), the continuous function \(a(v,Jv)\) on the compact unit sphere bundle has a positive minimum \(m\), and every invariant \(\alpha\) with \(\|\alpha-a\|_\infty<m\) lies in \(K\). An element of \(K\cap W\) is a closed form compatible with \(J\), so \(K\cap W=\varnothing\). Theorem 6.2 of [Hahn–Banach, Baire and the basic theorems on Banach spaces](course:foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces) gives a continuous linear functional \(\varphi\) on \(V\) and \(t\in\mathbb R\) with \(\varphi(a)<t\le\varphi(w)\) for \(a\in K\) and \(w\in W\). A linear functional bounded below on a subspace vanishes there, so \(\varphi|_W=0\) and \(t\le0\). Thus \(\psi=-\varphi\) is positive on \(K\) and zero on \(W\).

Put \(P(\alpha)=\psi((1-R)\alpha)/\psi(F)\). Then \(P(R\alpha)=0\), \(P(F)=1\), and \(P\ge0\) on semidefinite invariant forms, because \(\alpha+\varepsilon F\in K\) for every \(\varepsilon>0\). Proposition 4.1 gives \(\mu\), \(A\), \(\lambda\) and the integral formula, and \(P=0\) on \(W\) by construction.

With \(B\) from Lemma 3.4 put
\[
Q(\alpha)=-P(BR\alpha),\qquad T=P+Q .
\]
Then \(RQ=Q\) since \(R^2=R\), and \(*Q=Q\) since \(R*=R\) (Lemma 1.1(2)). If \(\alpha\) is closed, then \(\alpha-BR\alpha\) is closed because \(dB=0\), and invariant because \(R(\alpha-BR\alpha)=R\alpha-R\alpha=0\). So \(T(\alpha)=P(\alpha-BR\alpha)=0\). Finally \(|P(\alpha)|\le\|\alpha\|_\infty\le C\|\alpha\|_{H^3}\), and \(\|BR\alpha\|_{H^3}\le C\|\alpha\|_{H^3}\) because \(B\) has order zero and \(R\) is a smooth bundle map ((G32) and Section 13 of the lesson Detecting regularity without choosing coordinates). \(\blacksquare\)

The current \(P\) is the obstruction. It is positive on every complex line, it annihilates closed invariant forms, and \(T=P+Q\) annihilates all closed forms. The reverse also holds: if a closed compatible form exists, no such \(P\) exists (Exercise 6.4). The trace measure \(\mu\) is the measure of the bivectors' base points; the next lesson shows that \(\mu\) of a ball of radius \(s\) is at most \(Cs^2\), as for a surface.

## 6. Exercises

**6.1.** Show that a closed form compatible with \(J\) is symplectic, and that \((1-R)\omega\) tames \(J\) whenever \(\omega\) does.

**6.2.** In a unitary frame, compute \(R(e^{13})\), \(R(e^{14})\) and \(R(e^{12})\). Deduce that \(R\) has rank two at every point.

**6.3.** Using the coordinates of Lemma 1.2(2), show that \(\int|z_1|^2\,d\sigma=\frac12\) and \(\int z_1\bar z_2\,d\sigma=0\) for the normalized rotation-invariant measure \(\sigma\) on the unit sphere of \(\mathbb C^2\), and deduce again that the barycentre of the image of \(\sigma\) under \(v\mapsto v\wedge Jv\) is \(F/2\).

**6.4.** Suppose that \(\omega_0\) is a closed form compatible with \(J\). Show that there is no pair of linear functionals \(P\), \(Q\) with properties 1 to 3 of Proposition 5.1 and \(P(F)=1\).

**6.5.** On \(\mathbb R^4=\mathbb C^2\) with the Euclidean metric and constant \(J\), let \(a_0\) be a constant anti-invariant form and \(f\) a smooth function with compact support. Show that \(\mathcal L(fa_0)=-\frac12(\Delta_0f)\,a_0\), where \(\Delta_0=\sum_i\partial_i^2\).

## 7. Solutions

**6.1.** A compatible form \(\omega\) tames \(J\), so \(\omega(v,Jv)>0\) and \(\omega(v,\cdot)\ne0\) for \(v\ne0\): \(\omega\) is nondegenerate, and a closed nondegenerate form is symplectic. For the second claim, \(((1-R)\omega)(v,Jv)\) equals \(\frac12\bigl(\omega(v,Jv)+\omega(Jv,J^2v)\bigr)\), and \(\omega(Jv,-v)=\omega(v,Jv)\).

**6.2.** From the action of \(J\) in the proof of Lemma 1.1, \(R(e^{13})=\frac12(e^{13}-e^{24})\), \(R(e^{14})=\frac12(e^{14}+e^{23})\) and \(R(e^{12})=0\). Likewise \(R(e^{24})=-\frac12(e^{13}-e^{24})\), \(R(e^{23})=\frac12(e^{14}+e^{23})\) and \(R(e^{34})=0\). The image is spanned by the two anti-invariant forms, so the rank is two.

**6.3.** The measure \(\sigma\) is invariant under \((z_1,z_2)\mapsto(z_2,z_1)\) and \((z_1,z_2)\mapsto(z_1,-z_2)\). The first gives \(\int|z_1|^2=\int|z_2|^2\), and their sum is \(1\); the second gives \(\int z_1\bar z_2=-\int z_1\bar z_2\). So \(\int zz^*\,d\sigma=I/2\), which is \(M(F/2)\) by Lemma 1.2.

**6.4.** \(\omega_0\) is closed, so \(T(\omega_0)=0\). It is invariant, so \(R\omega_0=0\), and \(Q(\omega_0)=Q(R\omega_0)=0\) since \(RQ=Q\). Hence \(P(\omega_0)=0\). But \(\omega_0(\ell)\ge m>0\) on the compact set \(\mathscr C\), so \(P(\omega_0)=\int\omega_0(\ell)\,d\lambda\ge m\).

**6.5.** In flat coordinates \(d=\sum_je^j\wedge\partial_j\) and \(d^*=-\sum_i\iota_{e_i}\partial_i\). Hence
\[
dd^*(fa_0)=-\sum_{i,j}\partial_i\partial_jf\;e^j\wedge\iota_{e_i}a_0 .
\]
Polarizing the identity of Lemma 3.2 in \(\xi=\sum_i\xi_ie^i\) gives \(R\bigl(e^j\wedge\iota_{e_i}a_0+e^i\wedge\iota_{e_j}a_0\bigr)=\delta_{ij}a_0\). Since \(\partial_i\partial_jf\) is symmetric in \(i,j\), \(R\,dd^*(fa_0)=-\frac12\sum_i\partial_i^2f\,a_0\).

## References

- [OpenAI-TC] OpenAI, *Taming implies compatibility on four-manifolds*, OpenAI Math Release preprint, 6 October 2026, Sections 1 and 2. https://github.com/openai/math/tree/main/preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026
- [Donaldson] S. K. Donaldson, *Two-forms on four-manifolds and elliptic equations*, in: Inspired by S. S. Chern, World Scientific, 2006, Section 5.2. https://arxiv.org/abs/math/0607083
