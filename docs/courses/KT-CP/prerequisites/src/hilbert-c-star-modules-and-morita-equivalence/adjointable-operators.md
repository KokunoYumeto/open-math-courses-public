# Adjointable operators

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A Hilbert module carries both a norm and an inner product with values in a C*-algebra. Its operators must respect this extra information. Bounded module maps need not have adjoints, and closed submodules need not admit orthogonal projections. We will see both failures explicitly. We will then prove that adjointable maps form a C*-algebra, develop their order properties, and show how closed range restores orthogonal decompositions and polar decomposition.

The prerequisite is [Hilbert C*-modules](hilbert-c-star-modules.md). We use its norm Cauchy–Schwarz inequality and finite direct sums, together with elementary C*-algebra functional calculus and the Banach-space open mapping and closed graph theorems. Their precise statements and references are collected near the end. Basic references are [Blackadar 2006], [Blackadar 1998] and [Emerson 2024].

Throughout, \(A\) is a C*-algebra, possibly nonunital, and \(E,F\) are right Hilbert \(A\)-modules. Inner products are linear in the second variable:

\[
\langle xa,yb\rangle=a^*\langle x,y\rangle b,
\qquad \|x\|^2=\|\langle x,x\rangle\|.
\]

A map \(T:E\to F\) is **adjointable** if there is a map \(T^*:F\to E\) such that

\[
\langle Tx,y\rangle_F=\langle x,T^*y\rangle_E
\quad(x\in E,\ y\in F).
\tag{1}
\]

We initially impose neither linearity nor boundedness: both will follow. Write \(\mathcal L(E,F)\) for these maps and \(\mathcal L(E)=\mathcal L(E,E)\).

## 1. A closed submodule without a projection

Before developing the operator algebra, it helps to see why the adjoint condition matters. Regard \(A=C[0,1]\) as a Hilbert module over itself, with \(\langle f,g\rangle=\overline f g\). The ideal

\[
I=\{f\in C[0,1]:f(0)=0\}
\]

is a Hilbert \(A\)-module with the same inner product. Indeed, evaluation at zero is continuous, so its kernel \(I\) is closed and complete. Restriction identifies \(I\) with \(C_0((0,1])\): extending a function by zero is continuous precisely when it vanishes at the missing endpoint.

**Proposition 1.1.** The inclusion \(j:I\to A\) is an isometric \(A\)-linear map with closed range, but it is not adjointable.

**Proof.** The norm and module action on \(I\) are inherited from \(A\), so the first assertions follow directly. If an adjoint existed, put \(h=j^*(1)\in I\). Equation (1) would imply

\[
\overline{f(t)}=\overline{f(t)}h(t)
\quad(f\in I).
\]

Choose \(f(t)=t\). Then \(h(t)=1\) for every \(t>0\). Continuity gives \(h(0)=1\), whereas membership in \(I\) requires \(h(0)=0\). This contradiction proves the claim. \(\square\)

For a submodule \(M\subseteq E\), define

\[
M^\perp=\{x\in E:\langle m,x\rangle=0\text{ for every }m\in M\}.
\]

Conjugate symmetry makes the reverse inner products vanish too. The complement is a closed submodule: each condition is closed by Cauchy–Schwarz, and the conditions are preserved by the right action.

In our example \(I^\perp=\{0\}\). In fact, if \(g\in I^\perp\), testing against \(f(t)=t\) gives \(tg(t)=0\). Hence \(g\) vanishes on \((0,1]\), and continuity gives \(g(0)=0\). Thus

\[
I\oplus I^\perp=I\ne A,
\qquad I^{\perp\perp}=A.
\tag{2}
\]

Closedness alone therefore supplies neither an orthogonal decomposition nor equality with the double orthogonal complement. Even preservation of the inner product does not guarantee an adjoint when the map is not onto.

## 2. The algebra forced by an adjoint

The boundedness argument needs completeness rather than an assumption that the adjoint is continuous. Here are the Banach-space facts in the form we will use.

**Lemma (Complete graphs and bounded maps).** A bounded surjection between Banach spaces is open. A linear map defined on a whole Banach space, with values in another Banach space and a closed graph, is bounded. The bounded maps into a Banach space form a Banach space in the operator norm.

*Proof.* Recall the elementary category argument. A complete metric space cannot be a countable union of closed sets with empty interior: starting in any open ball, choose nested closed balls avoiding the successive sets, with positive radii tending to zero and each ball inside the preceding interior. Their centers form a Cauchy sequence. Its limit belongs to every ball and hence avoids every set, a contradiction.

Let \(S:X\to Y\) be bounded and onto. The closed sets \(\overline{S(nB_X)}\), for positive integers \(n\), cover \(Y\), where \(B_X\) is the closed unit ball. One has interior. Subtracting two points in a small ball in that interior and using linearity gives
\(\delta B_Y\subset\overline{S(B_X)}\) for some \(\delta>0\), after rescaling. For \(\|y\|<\delta/2\), successively choose \(x_j\) with \(\|x_j\|\leq2^{-j}\) so that
\[
\left\|y-S\sum_{k=1}^j x_k\right\|<\delta 2^{-j-1}.
\]
Each choice is possible by the rescaled closure inclusion. Completeness gives \(x=\sum_jx_j\), with \(\|x\|\leq1\), and continuity gives \(Sx=y\). Hence the image of a unit ball contains a neighborhood of zero. Scaling and translation prove openness, and a bounded bijection therefore has bounded inverse.

For a closed graph \(G\subset X\oplus Y\), use \(\|(x,y)\|=\|x\|+\|y\|\). The graph is Banach and its first-coordinate projection onto \(X\) is a bounded bijection. Its inverse is bounded by the preceding argument; composing with the second-coordinate projection makes the original map bounded. Finally an operator-norm Cauchy sequence of bounded maps has pointwise limits in its Banach codomain. Passing its uniform Cauchy estimates to those limits gives a bounded linear limit and convergence in operator norm. ∎

**Theorem 2.1.** An adjointable map is complex-linear, \(A\)-linear and bounded. Its adjoint is unique, is itself adjointable, and satisfies \((T^*)^*=T\).

**Proof.** If \(S_1,S_2\) satisfy (1), then \(\langle x,(S_1-S_2)y\rangle=0\) for every \(x\). Taking \(x=(S_1-S_2)y\) proves uniqueness. Taking adjoints of the values in (1) gives \(\langle T^*y,x\rangle=\langle y,Tx\rangle\). Thus \(T\) is the adjoint of \(T^*\).

For \(x_1,x_2\in E\), additivity of the inner products shows

\[
\langle T(x_1+x_2)-Tx_1-Tx_2,y\rangle=0
\quad(y\in F).
\]

Testing against the vector on the left proves additivity of \(T\). The same calculation with a scalar proves complex homogeneity. For \(a\in A\),

\[
\langle T(xa),y\rangle
=a^*\langle x,T^*y\rangle
=\langle (Tx)a,y\rangle,
\]

so \(T(xa)=(Tx)a\). These arguments apply to \(T^*\) as well.

To prove boundedness, suppose \(x_n\to x\) in \(E\) and \(Tx_n\to z\) in \(F\). For each fixed \(y\in F\), Cauchy–Schwarz gives

\[
\langle z,y\rangle
=\lim_n\langle Tx_n,y\rangle
=\lim_n\langle x_n,T^*y\rangle
=\langle Tx,y\rangle.
\]

Hence \(z=Tx\). The graph is closed, and the closed graph theorem makes \(T\) bounded. Notice that this argument did not assume continuity of \(T^*\); only the fixed vector \(T^*y\) was used. \(\square\)

**Theorem 2.2.** The space \(\mathcal L(E,F)\) is complete in the operator norm, and

\[
\|T^*\|=\|T\|,
\qquad \|T^*T\|=\|T\|^2.
\tag{3}
\]

Consequently \(\mathcal L(E)\), with composition and adjoint, is a C*-algebra. If \(E\ne0\), its identity is \(1_E\), even when \(A\) is nonunital.

**Proof.** Cauchy–Schwarz and the choice \(y=z/\|z\|\) for \(z\ne0\) yield the useful norm formula

\[
\|z\|=\sup_{\|y\|\le1}\|\langle z,y\rangle\|.
\]

Apply this to \(z=Tx\) and use (1). It follows that \(\|Tx\|\le\|x\|\|T^*\|\), and therefore \(\|T\|\le\|T^*\|\). Interchanging \(T,T^*\) proves the first identity. Also,

\[
\|Tx\|^2
=\|\langle x,T^*Tx\rangle\|
\le\|x\|\|T^*Tx\|
\le\|T^*T\|\|x\|^2.
\]

Taking the supremum over the unit ball gives \(\|T\|^2\le\|T^*T\|\). Submultiplicativity and the first identity give the reverse inequality.

If \(T_n\) is Cauchy, then so is \(T_n^*\). Completeness of the spaces of bounded maps gives norm limits \(T_n\to T\) and \(T_n^*\to S\). Passing to the limit in (1) shows \(S=T^*\). Thus the limit remains adjointable.

Direct substitution in (1) proves that adjoints respect sums, conjugate scalars and reverse composition: \((ST)^*=T^*S^*\) whenever the domains fit. The identity has itself as adjoint. These facts, completeness, submultiplicativity and (3) are precisely the C*-algebra axioms for \(\mathcal L(E)\). \(\square\)

The domains matter. For distinct \(E,F\), the space \(\mathcal L(E,F)\) is a Banach space, with adjoint mapping it to \(\mathcal L(F,E)\); it has no internal composition law in general.

**Example 2.3: matrices.** Suppose \(A\) is unital and give \(A^n\) the inner product \(\langle x,y\rangle=\sum_i x_i^*y_i\). A matrix \(b=(b_{ij})\in M_n(A)\) acts by

\[
(T_bx)_i=\sum_jb_{ij}x_j.
\]

Expanding the inner product gives \(T_b^*=T_{b^*}\), where \((b^*)_{ji}=b_{ij}^*\). Conversely, every \(A\)-linear map is determined by its values on the coordinate vectors \(e_j\): since \(x=\sum_j e_jx_j\), its columns are \(Te_j\). Thus

\[
\mathcal L(A^n)\cong M_n(A)
\quad\text{for unital }A.
\tag{4}
\]

This is an isometric *-isomorphism, by the isometry theorem for injective C*-algebra homomorphisms. For a concrete projection, take \(A=C[0,1]\), let \(u(t)=(\cos(\pi t),\sin(\pi t))^{\mathsf T}\), and put \(p(t)=u(t)u(t)^*\). Pointwise, \(p^2=p=p^*\), so \(pA^2\) is an orthogonally complemented submodule. It contrasts with the ideal in (2).

Unitality in (4) is essential. If \(A=C_0((0,1])\), the identity on \(A\) is adjointable but cannot be multiplication by an element of \(A\): such an element would have to equal one at every positive point. The general identification \(\mathcal L(A)\cong M(A)\) belongs to [Compact operators, multipliers and the strict topology](compact-operators-multipliers-and-the-strict-topology.md); it is announced here, with a reference in the final section.

## 3. Positivity seen by vectors and states

In \(\mathcal L(E)\), positivity means positivity as an element of a C*-algebra. We first show how this order is reflected in the coefficient algebra \(A\).

The state tests used here have a concrete programme proof. The Gelfand–Naimark theorem in *Representations and positive functionals*, Theorem 7.2, represents \(A\) faithfully and nondegenerately on a Hilbert space. Its unit-vector functionals are states: a positive contractive approximate identity converges strongly to identity, so each such functional has norm one. If a self-adjoint element has nonnegative value at all states, its faithful operator image has nonnegative quadratic form and is positive by *C\*-algebras: continuous functional calculus, automatic continuity, positive cones, approximate identities and quotients*, Proposition 8.5(11). Faithfulness reflects positivity by Proposition 8.5(12). For a positive operator the supremum of its unit-vector quadratic forms equals its operator norm: the upper bound is immediate, and \(\|b^{1/2}\xi\|^2\) has supremum \(\|b^{1/2}\|^2=\|b\|\). Thus states detect positivity and recover the norm of positive elements. The zero algebra is interpreted separately.

**Theorem 3.1.** For \(T\in\mathcal L(E,F)\) and \(x\in E\),

\[
\langle Tx,Tx\rangle\le\|T\|^2\langle x,x\rangle
\quad\text{in }A.
\tag{5}
\]

For \(S\in\mathcal L(E)\),

\[
S\ge0
\quad\Longleftrightarrow\quad
\langle Sx,x\rangle\ge0\text{ for every }x\in E.
\tag{6}
\]

**Proof.** If \(B\ge0\) in \(\mathcal L(E)\), its positive square root gives

\[
\langle Bx,x\rangle
=\langle B^{1/2}x,B^{1/2}x\rangle\ge0.
\tag{7}
\]

This proves the forward implication in (6).

Suppose now that all the forms in (6) are positive. They are self-adjoint, so \(\langle x,(S-S^*)x\rangle=0\). An \(A\)-valued sesquilinear form is determined by its diagonal: expand at \(x+y\) and \(x+iy\) to recover both cross terms. Applying this observation gives \(\langle x,(S-S^*)y\rangle=0\) for all \(x,y\), hence \(S=S^*\).

If a negative number belonged to \(\sigma(S)\), choose a real continuous function \(f\), nonzero on the spectrum, supported where \(t\le-\delta\) for some \(\delta>0\). Functional calculus gives \(f(S)\ne0\), so there is \(y\) with \(x=f(S)y\ne0\). The operator

\[
(-S-\delta1_E)f(S)^2
\]

is positive. By (7),

\[
-\langle Sx,x\rangle-\delta\langle x,x\rangle\ge0.
\]

Together with the assumed positivity of \(\langle Sx,x\rangle\), this forces \(\langle x,x\rangle=0\), a contradiction. Thus \(\sigma(S)\subseteq[0,\infty)\), proving (6).

For a map \(T:E\to F\), the operator \(T^*T\) belongs to \(\mathcal L(E)\), and \(\langle T^*Tx,x\rangle=\langle Tx,Tx\rangle\ge0\). The now-proved criterion (6) makes \(T^*T\) positive, even when \(E\) and \(F\) differ. By (3) and functional calculus, \(\|T\|^2 1_E-T^*T\ge0\). Applying (7) to this operator proves (5). \(\square\)

Inequality (5) contains more information than its norm consequence. For \(A=C(X)\), it compares two functions at every point; taking their supremum norms would discard that information.

**Proposition 3.2: localization by states.** Let \(\varphi\) be a state of \(A\). Define the scalar semidefinite inner product

\[
(x,y)_\varphi=\varphi(\langle x,y\rangle),
\qquad N_\varphi=\{x:\varphi(\langle x,x\rangle)=0\}.
\]

Divide by \(N_\varphi\) and complete to obtain a Hilbert space \(E_\varphi\). Every \(T\in\mathcal L(E,F)\) induces a bounded operator \(T_\varphi:E_\varphi\to F_\varphi\), with

\[
(T_\varphi)^*=(T^*)_\varphi,
\qquad \|T\|=\sup_\varphi\|T_\varphi\|.
\tag{8}
\]

Also \(S\ge0\) if and only if every \(S_\varphi\ge0\).

**Proof.** Applying \(\varphi\) to (5) proves \(T(N_\varphi)\subseteq N_\varphi\) in the respective domain and codomain, and gives \(\|T_\varphi\|\le\|T\|\). Equation (1) gives the adjoint identity on the dense quotient spaces, hence on their completions.

Put \(C=\sup_\varphi\|T_\varphi\|\). For every \(x\),

\[
\varphi(\langle Tx,Tx\rangle)
\le C^2\varphi(\langle x,x\rangle)
\le C^2\|x\|^2.
\]

The norm of a positive element of \(A\) is the supremum of its values under states. Thus \(\|Tx\|\le C\|x\|\), proving (8). If every \(S_\varphi\) is positive, then \(\varphi(\langle Sx,x\rangle)\ge0\) for all states. States detect positivity in \(A\), so (6) applies. The converse follows from (7) after applying each state. \(\square\)

No right \(A\)-module structure is asserted on the scalar quotient \(E/N_\varphi\). A state supplies a Hilbert-space test, and adjointability supplies the estimate that lets the operator pass to that test.

## 4. Orthogonal decompositions require adjoints

A closed submodule \(M\subseteq E\) is **orthogonally complemented** if every vector has a unique expression \(m+n\) with \(m\in M\), \(n\in M^\perp\). We write \(E=M\oplus M^\perp\).

**Proposition 4.1.** For a closed submodule \(M\subseteq E\), the following are equivalent:

1. \(M\) is orthogonally complemented.
2. \(M=pE\) for a projection \(p=p^*=p^2\in\mathcal L(E)\).
3. The inclusion \(j:M\to E\) is adjointable.

**Proof.** Under the first condition define \(p(m+n)=m\). Uniqueness makes \(p\) linear and \(A\)-linear. Orthogonality gives

\[
\|m\|^2\le\|\langle m,m\rangle+\langle n,n\rangle\|
=\|m+n\|^2,
\]

so \(p\) is bounded. Expanding the inner products of two decomposed vectors gives \(\langle px,y\rangle=\langle x,py\rangle\); hence \(p=p^*\) and \(p^2=p\).

Conversely, for a projection \(p\), the submodules \(pE\) and \((1_E-p)E\) are closed, orthogonal, and sum to \(E\). If \(x\perp pE\), then \(\langle px,px\rangle=\langle px,x\rangle=0\), so \(px=0\). Thus \((pE)^\perp=(1_E-p)E\).

If \(j\) has an adjoint, inner-product preservation gives \(j^*j=1_M\), and \(jj^*\) is a projection onto \(M\). If a projection onto \(M\) exists, the same map viewed as \(E\to M\) is the adjoint of \(j\). \(\square\)

For any adjointable \(T:E\to F\), one always has

\[
(\operatorname{ran}T)^\perp=\ker T^*,
\qquad (\operatorname{ran}T^*)^\perp=\ker T.
\tag{9}
\]

Indeed, \(y\perp\operatorname{ran}T\) means \(\langle x,T^*y\rangle=0\) for every \(x\), which is equivalent to \(T^*y=0\). The other equality follows by interchanging \(T,T^*\). Equation (9) alone does not allow taking a double complement and concluding equality with a closed range; (2) explains the obstruction.

## 5. Closed range creates a spectral gap

**Theorem 5.1 (closed range theorem).** If \(T\in\mathcal L(E,F)\) has closed range, then \(T^*\) has closed range and

\[
E=\ker T\oplus\operatorname{ran}T^*,
\qquad
F=\operatorname{ran}T\oplus\ker T^*.
\tag{10}
\]

Both sums are orthogonal. In particular, the range and kernel submodules in (10) are ranges of adjointable projections.

*Reference:* [Blackadar 2006, Theorem II.7.2.9], which attributes the theorem to Miščenko.

**Proof.** If \(T=0\), the statements are immediate. Otherwise let \(K=\ker T\), a closed submodule, and put \(Q=T^*T\ge0\). Since \(\langle x,Qx\rangle=\langle Tx,Tx\rangle\), we have \(\ker Q=K\).

The induced bounded map of Banach spaces

\[
\overline T:E/K\longrightarrow\operatorname{ran}T
\]

is bijective. The quotient is Banach: from a Cauchy sequence of classes choose a subsequence whose successive quotient distances are less than \(2^{-j}\). By adjusting representatives by elements of \(K\), lift this subsequence to vectors whose successive distances are less than \(2^{1-j}\). They form a Cauchy sequence in \(E\), so their limit gives a limit class. The original Cauchy sequence has the same limit. Closedness of \(K\) ensures that the quotient seminorm is a norm.

The range is Banach by the closed-range hypothesis. The open mapping theorem gives a constant \(C>0\) such that

\[
\operatorname{dist}(x,K)\le C\|Tx\|.
\tag{11}
\]

We claim that

\[
\sigma(Q)\cap(0,C^{-2})=\varnothing.
\tag{12}
\]

Suppose instead that \(\lambda\) lies in this interval. Choose a real continuous \(f\) supported in a compact interval \([a,b]\subset(0,C^{-2})\), with \(f(\lambda)=1\). Then \(f(Q)\ne0\). Choose \(y\) such that \(x=f(Q)y\ne0\).

For \(k\in K\), functional calculus gives \(f(Q)k=f(0)k=0\); this identity follows first for polynomials and then by uniform approximation. Since \(f(Q)\) is self-adjoint, \(x\perp K\). Therefore, for every \(k\in K\),

\[
\|x-k\|^2
=\|\langle x,x\rangle+\langle k,k\rangle\|
\ge\|x\|^2.
\]

Taking \(k=0\) shows \(\operatorname{dist}(x,K)=\|x\|\). This equality uses only orthogonality of this particular vector, and does not assume that \(K\) is complemented.

The scalar function \((b-t)f(t)^2\) is nonnegative on \(\sigma(Q)\). By functional calculus and (7),

\[
\langle Tx,Tx\rangle
=\langle x,Qx\rangle
\le b\langle x,x\rangle.
\]

Thus \(\|Tx\|\le\sqrt b\|x\|\). Combined with (11), this gives \(1\le C\sqrt b<1\), a contradiction. This proves (12).

On the spectrum of \(Q\), the function

\[
g(0)=0,\qquad g(t)=t^{-1}\quad(t>0)
\]

is continuous by (12); if zero is absent, only the second formula is needed. Define \(G=g(Q)\) and \(p=QG\). Functional calculus gives

\[
p=p^*=p^2,\qquad Q(1_E-p)=0,\qquad GQG=G.
\]

We have \((1_E-p)E=K\): one inclusion follows from \(Q(1_E-p)=0\), and for \(k\in K\), \(pk=0\). Also \(T(1_E-p)=0\), so its adjoint gives \((1_E-p)T^*=0\). Consequently

\[
\operatorname{ran}T^*\subseteq pE,
\qquad
pE=QGE\subseteq\operatorname{ran}T^*.
\]

Thus \(\operatorname{ran}T^*=pE\), which is closed, and the first decomposition in (10) follows.

Finally put \(q=TGT^*\in\mathcal L(F)\). It is self-adjoint, and

\[
q^2=TGQGT^*=TGT^*=q,
\qquad qT=T GQ=Tp=T.
\]

The formula for \(q\) gives \(qF\subseteq\operatorname{ran}T\), while \(qT=T\) gives the reverse inclusion. Hence \(qF=\operatorname{ran}T\). Its orthogonal complement is \(\ker T^*\) by (9), proving the second decomposition. \(\square\)

The proof explains the mechanism: closed range prevents nonzero singular values from approaching zero. The resulting continuous inverse on the nonzero spectrum produces actual projections in the operator algebra.

A **partial isometry** \(V\in\mathcal L(E,F)\) is an operator for which \(V^*V\) and \(VV^*\) are projections. A polar decomposition \(T=V|T|\), where \(|T|=(T^*T)^{1/2}\), requires \(V\) to have initial submodule \(\overline{\operatorname{ran}|T|}\) and final submodule \(\overline{\operatorname{ran}T}\). It is zero on the orthogonal complement of the initial submodule.

**Corollary 5.2.** Every adjointable operator with closed range has such a polar decomposition. Its initial projection is the projection \(p\) onto \(\operatorname{ran}T^*\), and its final projection is the projection \(q\) onto \(\operatorname{ran}T\).

**Proof.** Use the spectral gap in Theorem 5.1 and define \(H=h(Q)\) by \(h(0)=0\) and \(h(t)=t^{-1/2}\) on the positive spectrum. Put \(V=TH\). Then

\[
V^*V=HQH=p,\qquad VV^*=TH^2T^*=q,
\qquad V|T|=THQ^{1/2}=Tp=T.
\]

Since \(Q^{1/2}\) is invertible on \(pE\) and zero on \((1_E-p)E\), its range is \(pE\). The final submodule is \(qF\). These are exactly the required submodules. \(\square\)

**Example 5.3: polar decomposition can fail.** Let \(A=C([-1,1])\), \(E=A\), and let \(T\) be multiplication by the coordinate \(s\). It is self-adjoint and \(|T|\) is multiplication by \(|s|\). By (4) with \(n=1\), any \(V\in\mathcal L(A)\) is multiplication by a continuous function \(v\). The equation \(V|T|=T\) forces

\[
v(s)=1\ (s>0),\qquad v(s)=-1\ (s<0),
\]

which no continuous function satisfies. There is no polar decomposition, even before imposing the support conditions.

Here the range is not closed. The functions \(s/(|s|+\varepsilon)^{1/2}\) belong to \(sA\) and converge uniformly to \(\operatorname{sgn}(s)\sqrt{|s|}\), extended by zero at zero. The error is at most \(\sqrt\varepsilon\). The limit cannot equal \(sf(s)\) with continuous \(f\), because it would force \(f(s)=1/\sqrt{|s|}\) away from zero.

## 6. When an isomorphism is unitary

An operator \(U\in\mathcal L(E,F)\) is **unitary** if \(U^*U=1_E\) and \(UU^*=1_F\). Thus \(U^*=U^{-1}\). The following characterization separates preservation of length from the existence of an adjoint.

**Theorem 6.1.** A complex-linear \(A\)-linear map \(U:E\to F\) is unitary if and only if it is surjective and preserves inner products. Equivalently, it is unitary if and only if it is surjective and isometric for the module norms.

**Proof.** A unitary preserves inner products because

\[
\langle Ux,Uy\rangle=\langle x,U^*Uy\rangle=\langle x,y\rangle,
\]

and it is surjective because \(UU^*=1_F\). Conversely, an inner-product-preserving surjection is injective. If \(y=Uz\), then

\[
\langle Ux,y\rangle=\langle Ux,Uz\rangle
=\langle x,z\rangle=\langle x,U^{-1}y\rangle.
\]

Thus \(U^{-1}\) is its adjoint, proving unitarity.

It remains to show that an isometric module map preserves inner products. This step does not need surjectivity. Fix \(x\in E\), put \(a=\langle x,x\rangle\), \(b=\langle Ux,Ux\rangle\), and work in the unitization \(\widetilde A\) if necessary. The module action extends by \(x(c+\lambda1)=xc+\lambda x\); \(U\) respects it by complex linearity and \(A\)-linearity.

For \(\varepsilon>0\), put \(r=(a+\varepsilon1)^{-1/2}\in\widetilde A\). Functional calculus gives \(rar\le1\), so \(\|xr\|\le1\). Isometry gives \(\|(Ux)r\|\le1\), hence \(rbr\le1\), since a positive element of norm at most one is at most the identity. Multiplying this inequality on both sides by \(r^{-1}\) yields \(b\le a+\varepsilon1\). Letting \(\varepsilon\downarrow0\) gives \(b\le a\).

Repeat with \(r=(b+\varepsilon1)^{-1/2}\). The same norm equality now yields \(a\le b+\varepsilon1\), hence \(a\le b\). Thus \(a=b\). Polarizing this diagonal equality proves \(\langle Ux,Uy\rangle=\langle x,y\rangle\) for all \(x,y\). The preceding paragraph applies when \(U\) is surjective. \(\square\)

Proposition 1.1 shows why surjectivity cannot be dropped from the adjointability conclusion. A bounded module bijection need not itself be unitary either. Multiplication by two on any nonzero module is an adjointable bijection, but it multiplies squared inner products by four. By contrast, the map defined by a unitary matrix in (4) preserves the inner product and is a Hilbert-module isomorphism in this sense.

## 7. Exercises with complete solutions

### Exercise 7.1 — basic: recover an operator from its columns

Let \(A\) be unital. Prove \(\mathcal L(A^n)\cong M_n(A)\), including the adjoint formula. For \(A=C[0,1]\), determine the range and kernel of the projection with constant matrix \(\begin{pmatrix}1&0\\0&0\end{pmatrix}\).

**Solution.** Write \(e_j\) for the coordinate vector whose \(j\)-th entry is \(1_A\). For \(T\in\mathcal L(A^n)\), set \(b_{ij}=(Te_j)_i\). Since \(T\) is \(A\)-linear,

\[
Tx=T\Bigl(\sum_j e_jx_j\Bigr)=\sum_j(Te_j)x_j=T_bx.
\]

Conversely, for any matrix \(b\), expanding the finite sums gives

\[
\langle T_bx,y\rangle
=\sum_{i,j}x_j^*b_{ij}^*y_i
=\langle x,T_{b^*}y\rangle.
\]

Thus each matrix defines an adjointable map, its adjoint is the conjugate transpose, and columns determine it uniquely. Matrix products agree with composition. This proves a bijective *-homomorphism; the C*-algebra isometry theorem makes it isometric. The displayed projection has range \(A\oplus0\) and kernel \(0\oplus A\), which are orthogonal complements.

### Exercise 7.2 — intermediate: the missing endpoint obstructs an adjoint

For \(I=C_0((0,1])\subseteq C[0,1]\), prove that the inclusion is bounded and \(C[0,1]\)-linear but has no adjoint. Identify the contradiction using a single vector of the target.

**Solution.** Extend the functions by zero at zero. The extension preserves the supremum norm and commutes with multiplication by \(C[0,1]\), so the inclusion is a module map of norm one. If it had an adjoint, the target vector \(1\) would be sent to \(h\in I\). Testing the adjoint equation with \(f(t)=t\) gives \(t=t h(t)\). Thus \(h(t)=1\) for \(t>0\). A continuous extension has value one at zero, contrary to \(h\in I\). Hence there is no adjoint.

### Exercise 7.3 — intermediate: an order estimate rather than a norm estimate

For \(T\in\mathcal L(E)\), derive (5) from positivity of \(\|T\|^2 1_E-T^*T\). Explain which algebra contains each positive element.

**Solution.** The operator \(B=\|T\|^2 1_E-T^*T\) is positive in \(\mathcal L(E)\), since \(T^*T\ge0\) has norm \(\|T\|^2\). Its square root belongs to \(\mathcal L(E)\). For \(x\in E\),

\[
\|T\|^2\langle x,x\rangle-\langle Tx,Tx\rangle
=\langle x,Bx\rangle
=\langle B^{1/2}x,B^{1/2}x\rangle\ge0.
\]

The last element is positive in \(A\). Therefore the comparison is in the order of \(A\), and taking norms only afterward gives \(\|Tx\|\le\|T\|\|x\|\).

### Exercise 7.4 — intermediate: a closed submodule with zero complement

Give a proper closed submodule \(M\subset E\) for which \(M\oplus M^\perp\ne E\). Compute \(M^\perp\) and \(M^{\perp\perp}\), and decide whether \(M\) can be the range of an adjointable projection.

**Solution.** Take \(E=C[0,1]\), \(M=\{f:f(0)=0\}\). It is closed as the kernel of the continuous evaluation map, and proper because \(1\notin M\). If \(g\in M^\perp\), testing against \(f(t)=t\) gives \(tg(t)=0\), so continuity forces \(g=0\). Hence \(M^\perp=0\) and \(M^{\perp\perp}=E\). It follows that \(M\oplus M^\perp=M\ne E\). By Proposition 4.1 it cannot be the range of an adjointable projection.

### Exercise 7.5 — advanced: construct the polar factor

Assume \(T\in\mathcal L(E,F)\) has closed range. Use the closed range theorem to construct \(V\) with \(T=V|T|\), \(V^*V\) the projection onto \(\operatorname{ran}T^*\), and \(VV^*\) the projection onto \(\operatorname{ran}T\). Determine the action of \(V\) on both summands of \(E\).

**Solution.** Put \(N=\operatorname{ran}T^*\) and \(R=\operatorname{ran}T\). The theorem gives orthogonal sums \(E=\ker T\oplus N\), \(F=R\oplus\ker T^*\), so their inclusions and projections are adjointable. The restriction \(T_0:N\to R\) is an adjointable bijection: it is injective because \(N\perp\ker T\), and it is onto because every preimage can be projected onto \(N\). Its adjoint is \(T^*|_R\).

Its bounded inverse is adjointable. Indeed, \(T^*|_R:R\to N\) is bijective: it is onto by projecting a preimage in \(F\) onto \(R\), and its kernel is \(R\cap\ker T^*=0\). For \(r=T_0n\) and \(m\in N\),

\[
\langle T_0^{-1}r,m\rangle
=\langle n,m\rangle
=\langle T_0n,(T_0^*)^{-1}m\rangle.
\]

Thus \((T_0^{-1})^*=(T_0^*)^{-1}\). In particular, \(Q_0=T_0^*T_0\in\mathcal L(N)\) is positive and invertible. Define \(V\) to vanish on \(\ker T\), and on \(N\) set

\[
V|_N=T_0Q_0^{-1/2}:N\longrightarrow R.
\]

This construction uses adjointable projections and inclusions, hence defines an adjointable map. On \(N\),

\[
(V|_N)^*(V|_N)=1_N,
\qquad
(V|_N)(V|_N)^*=T_0Q_0^{-1}T_0^*=1_R,
\]

where \(Q_0^{-1}=T_0^{-1}(T_0^*)^{-1}\). Therefore \(V^*V\) and \(VV^*\) are the required projections. On \(N\), \(|T|=Q_0^{1/2}\), so \(V|T|=T_0\); on \(\ker T\), both sides vanish. Thus \(T=V|T|\). If \(T=0\), choose \(V=0\) directly.

## What this lesson does not prove

The Hilbert-module prerequisite supplies the norm Cauchy–Schwarz inequality \(\|\langle x,y\rangle\|\le\|x\|\|y\|\), the bound \(\|xa\|\le\|x\|\|a\|\), and completeness of finite direct sums with the summed inner product. References are [Blackadar 1998, Definition 13.1.1, Proposition 13.1.3 and Examples 13.1.2] and [Blackadar 2006, Proposition II.7.1.4 and Examples II.7.1.7(ii),(iv)].

We use the following foundational C*-algebra facts without reproving them. Continuous functional calculus for a self-adjoint element \(a\) respects products, involution and uniform limits, gives \(\|f(a)\|=\max_{t\in\sigma(a)}|f(t)|\), and sends nonnegative functions to positive elements. Positive elements have positive square roots; \(c^*c\ge0\); the positive cone is closed; \(0\le a\le b\) implies \(\|a\|\le\|b\|\). References are [Blackadar 2006, Corollary II.2.3.1, Proposition II.2.3.2 and II.3.1.2–II.3.1.8]. The norm comparison also follows immediately by evaluating states. An injective *-homomorphism of C*-algebras is isometric [Blackadar 2006, Corollary II.2.2.9].

States detect positivity, \(a\ge0\) exactly when \(\varphi(a)\ge0\) for every state, and for positive \(a\), \(\|a\|=\sup_\varphi\varphi(a)\) [Blackadar 2006, Proposition II.6.3.3 and Corollary II.6.3.5]. For the zero algebra these statements and the localization conclusions are read with the empty supremum equal to zero.

The Banach-space open mapping theorem, closed graph theorem and completeness of bounded-map spaces are proved in the opening lemma of Section 2; compare [Blackadar 2006, I.2.1.1 and Theorems I.2.1.4–I.2.1.5] for the classical formulations. Quotient completeness is proved in Theorem 5.1.

Finally, the canonical isomorphism \(\mathcal L(A)\cong M(A)\) for arbitrary \(A\) is announced, not proved [Emerson 2024, Proposition 5.5.13]. Its construction is reserved for *Compact operators, multipliers and the strict topology*. All operator theorems and counterexamples developed above, including the surjective-isometry characterization, have proofs in this lesson.

## References

- **[Blackadar 2006]** B. Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*, Encyclopaedia of Mathematical Sciences 122, Springer, 2006; [author's revised edition, 2017](https://www.bruceblackadar.com/Mathematics/Cycr.pdf).
- **[Blackadar 1998]** B. Blackadar, *K-Theory for Operator Algebras*, second edition, Mathematical Sciences Research Institute Publications 5, Cambridge University Press, 1998. [Author's corrected second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf).
- **[Emerson 2024]** H. Emerson, *An Introduction to C*-Algebras and Noncommutative Geometry*, Birkhäuser Advanced Texts, Birkhäuser, 2024.
