# Invariant connections on homogeneous bundles

*Written by GPT-6.1 Sol (OpenAI), Ultra effort, October 2026. Self-checked by the writing AI. Original text dedicated to the public domain under CC0 1.0.*

A symmetry can turn a differential problem into a finite-dimensional one. When a Lie group acts transitively on the base and preserves a principal connection, the connection is determined by one linear map. Its failure to preserve brackets is exactly the curvature. Repeatedly bracketing that curvature with the image of the map gives the holonomy algebra. We prove these statements and apply them to canonical connections and the Hopf bundle.

Read [Local tools for bundles and transport](local-tools-for-bundles-and-transport.md), Principal bundles and associated bundles, Connections and parallel transport, and Reduction and the holonomy theorem first. The exponential and Lie bracket conventions are those of these lessons. We also use the integration and uniqueness of a connected subgroup with a prescribed Lie algebra from Section 3 of [Flat connections and infinitesimal holonomy](flat-connections-and-infinitesimal-holonomy.md). Semisimple Lie-algebra theory is unnecessary here. Basic references are [Wang] and [Hammerl].

All manifolds and Lie groups are finite dimensional, Hausdorff and second countable. The acting group is denoted by \(K\), the structure group by \(G\), and the isotropy group by \(L\). The left \(K\)-action commutes with the right principal \(G\)-action. Exterior forms have ordinary, unnormalized evaluation. Unless connectedness is explicitly required, the groups may be disconnected.

## 1. Closed subgroups and transitive actions

We first justify the smooth homogeneous space needed below. Closedness of a subgroup supplies more than a well-behaved topological quotient.

**Theorem 1.1 (closed-subgroup theorem).** A closed subgroup \(L\) of a Lie group \(K\) is an embedded Lie subgroup. Consequently \(K/L\) is a smooth Hausdorff second-countable manifold, and \(K\to K/L\) is a principal \(L\)-bundle with smooth local sections.

**Proof.** The exponential map is a local diffeomorphism at zero, by Section 2 of the local-tools lesson. Put

\[
\mathfrak l=\{X\in\mathfrak k:\exp(tX)\in L\text{ for every }t\in\mathbb R\}.
\]

This is closed, as an intersection of inverse images of the closed set \(L\), and is stable under real scalar multiplication. We prove additivity. For \(X,Y\in\mathfrak l\), let \(c(s)=\exp(sX)\exp(sY)\). Near zero, the local logarithm satisfies

\[
\log c(s)=s(X+Y)+o(|s|).
\]

Indeed, the differentials of the exponential and logarithm at zero are identities, and the differential of multiplication at \((e,e)\) adds tangent vectors. For any fixed \(t\),

\[
\begin{aligned}
&c(t/n)^n=\exp\bigl(n\log c(t/n)\bigr)\\
&\qquad\longrightarrow\exp(t(X+Y)).
\end{aligned}
\]

Each term belongs to \(L\). Closedness gives \(\exp(t(X+Y))\in L\). Thus \(\mathfrak l\) is a vector subspace.

Choose a linear complement \(\mathfrak m\). We claim that, for sufficiently small \(Y\in\mathfrak m\), \(\exp Y\in L\) implies \(Y=0\). Otherwise there are nonzero \(Y_j\in\mathfrak m\) tending to zero with \(\exp Y_j\in L\). After taking a subsequence, compactness of the unit sphere gives

\[
Y_j/\|Y_j\|\longrightarrow Y_\infty\in\mathfrak m,
\qquad \|Y_\infty\|=1.
\]

For each fixed real \(t\), choose integers \(n_j\) with \(n_j\|Y_j\|\to t\). Then

\[
(\exp Y_j)^{n_j}=\exp(n_jY_j)\longrightarrow\exp(tY_\infty).
\]

Negative integers cause no difficulty, because \(L\) is a group. Closedness gives \(Y_\infty\in\mathfrak l\), contradicting \(\mathfrak l\cap\mathfrak m=0\).

The map \((X,Y)\mapsto\exp X\exp Y\), from \(\mathfrak l\oplus\mathfrak m\) to \(K\), has invertible differential at zero. Shrink its inverse-function neighbourhood so that the preceding claim applies. If an element \(\exp X\exp Y\) of that neighbourhood belongs to \(L\), then \(\exp X\in L\), hence \(\exp Y\in L\) and \(Y=0\). Conversely, every \(\exp X\) with \(X\in\mathfrak l\) belongs to \(L\). In these coordinates, \(L\) is therefore exactly the coordinate slice \(Y=0\).

Translating this chart by elements of \(L\) makes \(L\) an embedded submanifold with its subspace topology. Multiplication and inversion restrict smoothly: in each slice chart their ambient expressions are smooth and their complementary coordinates vanish. Hausdorffness and second countability are inherited from \(K\). Its tangent space at the identity is the subspace \(\mathfrak l\) above; the Lie bracket is the ambient bracket, since left-invariant fields on \(L\) are restrictions of the corresponding fields on \(K\). This proves the first assertion. Apply Theorem 4.1 of the local-tools lesson to obtain the quotient and principal-bundle assertions. □

There is also a point to check when a homogeneous space is originally given by a transitive action rather than by a quotient.

**Lemma 1.2 (a transitive orbit is a submersion).** If \(K\) acts smoothly and transitively on a manifold \(M\), the orbit map \(a(k)=k x_0\) is a submersion. For \(L=\{k:kx_0=x_0\}\), it induces a diffeomorphism \(K/L\to M\).

**Proof.** Left translation in \(K\) and the diffeomorphism of \(M\) given by an acting element identify the differentials of \(a\) at different points. Thus its rank is constant, say \(r\). Suppose \(r<\dim M\). Constant-rank coordinates, proved in Corollary 1.4 of the local-tools lesson, put each sufficiently small orbit-map image in a lower-dimensional coordinate slice. Cover \(K\) by countably many such neighbourhoods and then by countably many compact coordinate pieces contained in them. Their images are compact, hence closed in \(M\), and have empty interior. Transitivity would express \(M\) as their countable union.

Here is the needed impossibility. Choose a closed coordinate ball \(D\) with nonempty interior. Each of those closed sets meets \(D\) in a set with empty relative interior: every nonempty relatively open subset of \(D\) meets its interior, where a lower-dimensional slice cannot contain an open set. Recursively choose closed Euclidean balls \(B_j\) of positive radius, each contained in the interior of the preceding ball, avoiding the \(j\)-th closed set, and with radius at most \(2^{-j}\). Begin inside \(D\). Such a choice is possible because the set to be avoided is closed with empty interior. The centres form a Cauchy sequence; completeness and nesting give a common limit in every \(B_j\). It belongs to \(D\) and to none of the listed sets, a contradiction. Hence \(r=\dim M\).

The subgroup \(L\) is closed, since it is the inverse image of \(x_0\). Theorem 1.1 gives its smooth structure and the quotient. The orbit map descends smoothly, using local sections of \(K\to K/L\). It is bijective. The submersion level-set coordinates identify \(T_eL=\ker da_e\), so its descended differential is an isomorphism at every point. A bijective local diffeomorphism has a smooth inverse: its local inverses agree on overlaps. □

If \(M\) is connected, the identity component \(K^0\) is already transitive. Its Lie algebra is the same as that of \(K\), so its orbits are open by the just proved surjectivity and the inverse function theorem. These orbits partition \(M\); connectedness permits only one.

## 2. A homogeneous principal bundle

Let \(P\to M\) be a principal \(G\)-bundle, and suppose \(K\) acts by bundle automorphisms transitively on \(M\). Fix \(p\in P_{x_0}\). For \(l\in L\), there is a unique \(\lambda(l)\in G\) with

\[
lp=p\lambda(l).
\]

Commutation of the two actions gives \(\lambda(l_1l_2)=\lambda(l_1)\lambda(l_2)\). The fibre coordinate in any principal trivialization at \(x_0\) makes \(\lambda\) smooth. Its differential \(\lambda_*:\mathfrak l\to\mathfrak g\) preserves brackets: a smooth group homomorphism sends the left-invariant field determined by \(X\) to the field determined by its differential, and the chain rule for commutators of derivations gives bracket preservation.

Define

\[
\begin{gathered}
P_\lambda=K\times_LG,\\
(kl,g)\sim(k,\lambda(l)g).
\end{gathered}
\tag{2.1}
\]

This is the associated bundle of the principal \(L\)-bundle \(K\to K/L\), with \(L\) acting on \(G\) by left multiplication through \(\lambda\). The associated-bundle construction in the principal-bundle lesson proves smoothness and local triviality. Right multiplication in the second factor is a free transitive \(G\)-action on each fibre. The left \(K\)-action is \(a[k,g]=[ak,g]\).

**Proposition 2.1 (homogeneous bundle description).** The map

\[
\Phi:P_\lambda\longrightarrow P,
\qquad [k,g]\longmapsto kpg
\]

is a \(K\)-equivariant principal-bundle isomorphism over \(K/L\simeq M\).

**Proof.** Relation (2.1) preserves \(kpg\), by the definition of \(\lambda\). If \(kpg=k'pg'\), their base points agree, so \(k'=kl\) for some \(l\in L\). Freeness on the fibre then gives \(g=\lambda(l)g'\), exactly the same equivalence relation. Every base point is \(kx_0\), and every point in its fibre is uniquely \(kpg\), so \(\Phi\) is onto. A smooth local section \(s:U\to K\) gives the section \(s(x)p\) of \(P\). In the corresponding product charts, \(\Phi\) is \((x,g)\mapsto(x,g)\), proving smoothness of it and its inverse. Equivariance follows from the formula. □

*Reference:* [Hammerl], Section 1.1, displays representatives \((kl,\lambda(l)g)\). With \(lp=p\lambda(l)\), representatives preserving \(kpg\) are instead \((kl,\lambda(l)^{-1}g)\), as the proof above shows.

Changing the reference frame to \(pb\) changes the isotropy homomorphism to \(b^{-1}\lambda b\). This is the same bundle with a different reference frame, rather than a new geometric construction.

## 3. Wang's classification theorem

A connection is **\(K\)-invariant** if \(a^*\omega=\omega\) for every \(a\in K\). Let \(\alpha:K\to P\) be the orbit map \(\alpha(k)=kp\). Its pullback is a left-invariant \(\mathfrak g\)-valued one-form, hence

\[
\alpha^*\omega=W\theta_K,
\]

where \(\theta_K\) is the left Maurer–Cartan form and \(W:\mathfrak k\to\mathfrak g\) is linear.

**Theorem 3.1 (Wang).** The assignment \(\omega\mapsto W\) is a bijection between \(K\)-invariant principal connections on \(P_\lambda\) and linear maps satisfying

\[
\begin{aligned}
&W|_{\mathfrak l}=\lambda_*,\\
&W(\operatorname{Ad}(l)X)=\\
&\qquad\operatorname{Ad}(\lambda(l))W(X).
\end{aligned}
\tag{3.1}
\]

The second equality holds for every \(l\in L\) and \(X\in\mathfrak k\). No connectedness of \(K\) or \(L\) is needed for this classification. The second condition is a condition on every element of \(L\), not merely on its Lie algebra.

*Reference:* [Wang], Theorem 1.

**Proof.** For \(Z\in\mathfrak l\), the curve \(\exp(tZ)p=p\lambda(\exp(tZ))\) is vertical. Reproduction of vertical generators gives \(W(Z)=\lambda_*Z\). For \(l\in L\),

\[
\alpha(kl)=\alpha(k)\lambda(l).
\]

Pulling back the connection equivariance identity gives

\[
R_l^*(W\theta_K)
=\operatorname{Ad}(\lambda(l)^{-1})W\theta_K.
\]

Since \(R_l^*\theta_K=\operatorname{Ad}(l^{-1})\theta_K\), this is the second condition in (3.1).

Conversely, given \(W\) satisfying (3.1), consider on \(K\times G\) the form

\[
\widehat\omega=
\operatorname{Ad}(g^{-1})W\theta_K+\theta_G.
\tag{3.2}
\]

We show that it descends through the map \(F(k,g)=[k,g]\). The equivalence classes are orbits of

\[
(k,g)\cdot l=(kl,\lambda(l)^{-1}g).
\]

Under this transformation, \(\theta_K\) becomes \(\operatorname{Ad}(l^{-1})\theta_K\), \(\theta_G\) is unchanged, and the first term in (3.2) is unchanged by (3.1). Thus \(\widehat\omega\) is invariant under this \(L\)-action. On the tangent of \((k\exp(tZ),\lambda(\exp(tZ))^{-1}g)\), its value is

\[
\operatorname{Ad}(g^{-1})\bigl(WZ-\lambda_*Z\bigr)=0.
\]

It therefore annihilates the kernel of \(dF\). In local product charts from a section of \(K\to K/L\), these two properties mean precisely that the form is the pullback of a unique smooth one-form on \(P_\lambda\): evaluate on a local lift of a tangent vector; the kernel condition removes the choice of lift, and invariance removes the choice of representative.

Right multiplication by \(b\in G\) changes (3.2) by \(\operatorname{Ad}(b^{-1})\). On the vertical curve \((k,g\exp(tA))\), its value is \(A\). The descended form is consequently a principal connection. Left translation in the first factor leaves (3.2) unchanged, so it is \(K\)-invariant. Its value on \(\alpha\) is \(W\theta_K\).

Finally, any connection with that value on \(\alpha\) has pullback (3.2). At \((k,g)\), differentiate \(F(k,g)=\alpha(k)g\): the first tangent contribution is evaluated by connection equivariance, and the second by vertical reproduction. Since \(F\) is a submersion, its pullback determines the connection. This proves both uniqueness and the bijection. □

If one such map exists, all of them form an affine space. The difference of two maps vanishes on \(\mathfrak l\) and is \(L\)-equivariant, so the translation space is

\[
\operatorname{Hom}_L(\mathfrak k/\mathfrak l,\mathfrak g),
\]

where \(L\) acts on \(\mathfrak g\) through \(\operatorname{Ad}\lambda\). Conversely adding any such map preserves (3.1). The space can be empty if the isotropy differential has no equivariant extension.

## 4. Curvature and the holonomy algebra

Define the alternating bilinear map

\[
\begin{aligned}
&C(X,Y)\\
&\quad=[WX,WY]-W[X,Y].
\end{aligned}
\tag{4.1}
\]

**Proposition 4.1 (curvature).** For the connection determined by \(W\),

\[
(\alpha^*\Omega)_k(X^L_k,Y^L_k)=C(X,Y),
\tag{4.2}
\]

where \(X^L,Y^L\) are left-invariant fields on \(K\). More generally,

\[
\begin{aligned}
&(F^*\Omega)_{(k,g)}(u,v)\\
&\quad=\operatorname{Ad}(g^{-1})
C\bigl(\theta_Ku_K,\theta_Kv_K\bigr).
\end{aligned}
\tag{4.3}
\]

The right side vanishes if either argument of \(C\) belongs to \(\mathfrak l\). The connection is flat if and only if \(W\) is a Lie-algebra homomorphism.

**Proof.** Pull back the structure equation. The two functions \((W\theta_K)(X^L)\) and \((W\theta_K)(Y^L)\) are constant, so the definition of exterior differentiation gives

\[
d(W\theta_K)(X^L,Y^L)=-W[X,Y].
\]

The bracket part \(\tfrac12[W\theta_K,W\theta_K]\) evaluates to \([WX,WY]\). This proves (4.2). To get (4.3), split each tangent of \(K\times G\) into its \(K\)- and \(G\)-parts. The latter map to vertical vectors and curvature annihilates them. On the former, right equivariance of curvature supplies the adjoint factor, and (4.2) supplies \(C\).

Differentiating the equivariance condition (3.1) along \(\exp(tZ)\), for \(Z\in\mathfrak l\), yields

\[
W[Z,X]=[\lambda_*Z,WX].
\]

Together with \(WZ=\lambda_*Z\), this gives \(C(Z,X)=0\). Finally, every tangent on \(P\) has a lift through \(F\), so (4.3) says that \(\Omega=0\) exactly when \(C=0\). By (4.1), the latter is bracket preservation. □

Let \(V_0\) be the span of all values of \(C\), and define recursively

\[
V_{j+1}=V_j+[W\mathfrak k,V_j].
\tag{4.4}
\]

The bracket notation means a linear span. This increasing sequence stabilizes because it lies in the finite-dimensional vector space \(\mathfrak g\). Once two consecutive spaces are equal, all later ones are equal. Write \(V\) for their union. Equivalently, \(V\) is the smallest vector subspace containing \(V_0\) and preserved by every \(\operatorname{ad}(WX)\).

**Theorem 4.2 (homogeneous holonomy formula).** If the base \(M\) is connected, the Lie algebra of \(\operatorname{Hol}_p\) is \(V\). In particular \(V\) is a Lie subalgebra. Its connected integrated subgroup is the restricted holonomy group. Formula (4.4) does not determine the discrete components of full holonomy.

*Reference:* [Wang], Theorem 3.

**Proof.** Replace the acting group by \(K^0\) for the transport argument; it is transitive by Lemma 1.2. Its Lie algebra is still \(\mathfrak k\). Every finitely piecewise \(C^1\) base path starting at \(x_0\) has a lift \(k(t)\) to \(K\to K/L\) starting at \(e\). One precise way to obtain it is to choose a connection on that principal \(L\)-bundle, whose existence and whole-interval lifting were proved in the connection lesson. No invariance of this auxiliary connection is required. Put \(b(t)=\theta_K(k'(t))\). By (3.2), horizontal transport in \(P_\lambda\) is

\[
\begin{gathered}
q(t)=[k(t),g(t)],\\
g'(t)=-(dR_{g(t)})_e Wb(t),\\
g(0)=e.
\end{gathered}
\tag{4.5}
\]

The invariant-ODE lemma in the local-tools lesson proves existence on the entire interval.

The subspace \(V\) is preserved by \(\operatorname{Ad}(\exp(tWX))\): the adjoint curve solves \(Z'=[WX,Z]\), and the unique solution of this finite-dimensional linear equation starting in an invariant subspace stays in it. This adjoint derivative identity is proved in Lemma 3.2 of the flat-connections lesson.

The same assertion holds for the continuously varying coefficients in (4.5). In detail, set \(T(t)=\operatorname{Ad}(g(t))\). The chain rule for conjugation gives

\[
T'(t)=-\operatorname{ad}(Wb(t))\,T(t).
\]

In a basis adapted to \(V\), the complementary components of each column starting in \(V\) solve a homogeneous linear equation with zero initial value; uniqueness makes them zero. Thus \(T(t)V\subseteq V\). The restriction is invertible, so equality holds, and \(\operatorname{Ad}(g(t)^{-1})V=V\). The argument applies on each time piece.

At any reachable frame \([k(t),g(t)]\), formula (4.3) therefore puts all curvature values in \(V\). Horizontal projection does not change a curvature value. Ambrose–Singer, Theorem 4.1 of the reduction lesson, now gives

\[
\mathfrak{hol}_p\subseteq V.
\]

For the reverse inclusion, choose a path in \(K\) with constant left logarithmic derivative \(X\). On that segment its lift (4.5) multiplies the current group coordinate on the left by \(\exp(-tWX)\). Concatenating such segments realizes every finite product of these exponentials as a coordinate \(g\) at a reachable frame. At that frame (4.3), evaluated on arbitrary \(K\)-tangents and then on their horizontal projections, gives every vector \(\operatorname{Ad}(g^{-1})C(X,Y)\).

Let \(S\) be the span of these vectors over all finite products. Ambrose–Singer gives \(S\subseteq\mathfrak{hol}_p\). It contains \(V_0\), and multiplication of a product by one further exponential shows that \(S\) is invariant under \(\operatorname{Ad}(\exp(tWZ))\), for every real \(t\). Differentiate at zero. A finite-dimensional subspace is closed, so \([WZ,S]\subseteq S\). Minimality in (4.4) gives \(V\subseteq S\). This proves equality.

The holonomy Lie-group theorem proves that this is a Lie algebra, and Section 3 of the flat-connections lesson proves uniqueness of its connected integrated subgroup. That subgroup is consequently the already constructed restricted holonomy. □

The formula is effective: start with curvature values, take brackets with a basis of \(W\mathfrak k\), and stop when the span ceases to grow. Taking only \(V_0\) can give too small an answer.

## 5. Canonical connections and the Hopf bundle

A **reductive decomposition** is a direct sum

\[
\mathfrak k=\mathfrak l\oplus\mathfrak m,
\qquad \operatorname{Ad}(L)\mathfrak m=\mathfrak m.
\]

It need not mean that \(\mathfrak k\) is a reductive Lie algebra. Wang's theorem identifies invariant connections with equivariant linear maps \(A:\mathfrak m\to\mathfrak g\): set \(W|_{\mathfrak l}=\lambda_*\) and \(W|_{\mathfrak m}=A\). For \(X,Y\in\mathfrak m\), their curvature is

\[
\begin{aligned}
&C(X,Y)=[AX,AY]\\
&\qquad-A[X,Y]_{\mathfrak m}
-\lambda_*[X,Y]_{\mathfrak l}.
\end{aligned}
\tag{5.1}
\]

This follows by substituting the two components of \([X,Y]\) into (4.1).

The choice \(A=0\) is the **canonical connection** for this decomposition. On the principal bundle \(K\to K/L\), where \(G=L\) and \(\lambda\) is the identity, its form is

\[
\omega=\operatorname{pr}_{\mathfrak l}\theta_K,
\qquad C(X,Y)=-[X,Y]_{\mathfrak l}.
\]

Projection commutes with \(\operatorname{Ad}(L)\), which verifies (3.1). Thus these are a connection and its curvature, not merely candidate formulas. The span of \([\mathfrak m,\mathfrak m]_{\mathfrak l}\) is \(\operatorname{Ad}(L)\)-invariant: adjoint maps preserve brackets and the two projections. Differentiation makes it stable under \(\operatorname{ad}\mathfrak l\). Since \(W\mathfrak k=\mathfrak l\), Theorem 4.2 says that this span itself is the holonomy algebra when the base is connected. It can be a proper subspace of \(\mathfrak l\).

For a case where the iteration does grow, take \(K=\mathbb R^2\), \(L=\{e\}\), \(G=\mathrm{SU}(2)\), and

\[
\begin{aligned}
E_1&=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\\
E_2&=\begin{pmatrix}0&i\\i&0\end{pmatrix},\\
E_3&=\begin{pmatrix}i&0\\0&-i\end{pmatrix}.
\end{aligned}
\]

Matrix multiplication gives \([E_1,E_2]=2E_3\), \([E_2,E_3]=2E_1\), and \([E_3,E_1]=2E_2\). The translation-invariant potential \(A=E_1\,dx+E_2\,dy\) has curvature \(2E_3\,dx\wedge dy\). Its curvature span at the chosen frame is one dimensional, but one bracket step in (4.4) gives all of \(\mathfrak{su}(2)\). Its restricted holonomy is \(\mathrm{SU}(2)\). This group is connected: sending a matrix to its first column identifies it smoothly with \(S^3\), which is path connected by great-circle arcs, using an intermediate point for antipodal endpoints. As the base is simply connected, full holonomy has no further components, by the homotopy-class quotient proved in the holonomy-group lesson.

Now consider the Hopf bundle \(S^3\to\mathbb{CP}^1\), with right scalar \(U(1)\)-action. The identification

\[
z=(z_0,z_1)\longmapsto
\begin{pmatrix}z_0&-\overline z_1\\z_1&\overline z_0\end{pmatrix}
\]

identifies \(S^3\) with \(\mathrm{SU}(2)\). Its inverse takes the first column: unitarity forces the second column to be a unit scalar times the displayed column, and determinant one forces that scalar to be one. The stabilizer of the line \([1:0]\) is

\[
\begin{gathered}
L=\{\operatorname{diag}(e^{it},e^{-it})\},\\
\lambda(\operatorname{diag}(e^{it},e^{-it}))=e^{it}.
\end{gathered}
\]

Here \(\mathfrak l=\mathbb RE_3\) and \(\mathfrak m=\operatorname{span}(E_1,E_2)\). Conjugation by \(\operatorname{diag}(e^{it},e^{-it})\) rotates \(\mathfrak m\) by angle \(2t\); it acts trivially on \(\mathfrak u(1)=i\mathbb R\). An equivariant linear map from that plane to \(i\mathbb R\) must be zero: take \(t=\pi/2\), which negates every vector in the plane. Therefore

\[
W(E_1)=W(E_2)=0,\qquad W(E_3)=i
\]

is the unique Wang map. There is exactly one \(\mathrm{SU}(2)\)-invariant connection on this Hopf bundle.

Its form is the previously studied

\[
\omega=\overline z_0\,dz_0+\overline z_1\,dz_1.
\]

It is invariant under every constant unitary matrix and has the displayed values at \((1,0)\), so uniqueness identifies it with the Wang connection. Formula (4.1) gives \(C(E_1,E_2)=-2i\), and hence holonomy \(U(1)\). This sign agrees with the local formula \(F=2i\,dx\wedge dy/(1+|w|^2)^2\): at \((1,0)\), the two orbit tangents give \(dw(E_1)=-1\) and \(dw(E_2)=i\), so \((dx\wedge dy)(E_1,E_2)=-1\).

## 6. Exercises and complete solutions

**Exercise 6.1 (a central holonomy group).** On \(\mathbb R^2\), use the trivial bundle for the group of upper triangular real three-by-three matrices with diagonal entries one. Let \(P=E_{12}\), \(Q=E_{23}\), \(Z=E_{13}\), and take potential \(P\,dx+Q\,dy\). Find its curvature and full holonomy. Check the sign by a rectangle traversed in the order right, up, left, down.

**Solution.** The base acting group is abelian, so \(C=[P,Q]=Z\). Direct multiplication shows \([P,Z]=[Q,Z]=0\), so (4.4) stops with \(V=\mathbb RZ\). The connected subgroup is \(\{I+tZ:t\in\mathbb R\}\). The base \(\mathbb R^2\) is simply connected, since straight-line contraction contracts each loop, so full and restricted holonomy agree. For a rectangle with signed side lengths \(a,b\), the four transports give the product

\[
e^{bQ}e^{aP}e^{-bQ}e^{-aP}=I-abZ.
\]

Each exponential is \(I\) plus its linear term, because \(P^2=Q^2=0\); multiplying the four matrices proves the equality. As \(a,b\) vary, every element of the indicated subgroup occurs. The negative sign comes from the transport equation \(g'=-Ag\) and our first-then-second traversal convention. □

**Exercise 6.2 (isotropy contributes to flat monodromy).** Let \(K=\mathbb R\), \(L=2\pi\mathbb Z\), \(G=U(1)\), and \(\lambda(2\pi n)=e^{2\pi i\beta n}\). On \(P_\lambda\to S^1\), take \(W(1)=i\alpha\). Compute transport around the positive generator, and write the potential in a global section.

**Solution.** The isotropy Lie algebra is zero and all adjoint actions are trivial, so every \(\alpha\in\mathbb R\) is allowed. The curvature is zero. Lift the positive loop by \(k(t)=t\), \(0\leq t\leq2\pi\). Equation (4.5) gives \(g(t)=e^{-i\alpha t}\). At its endpoint,

\[
[2\pi,e^{-2\pi i\alpha}]
=[0,e^{2\pi i(\beta-\alpha)}].
\]

Thus \(h=e^{2\pi i(\beta-\alpha)}\), while the monodromy representation used in the flat-classification lesson sends the generator to \(h^{-1}\). The section \(s(e^{it})=[t,e^{-i\beta t}]\) is well-defined: increasing \(t\) by \(2\pi\) cancels the isotropy factor in (2.1). It is smooth and its potential is \(i(\alpha-\beta)\,dt\), a well-defined one-form on the circle. Full holonomy is the cyclic subgroup generated by \(h\), carrying the discrete holonomy topology when curvature is zero. It can be dense in \(U(1)\). □

**Exercise 6.3 (why disconnected isotropy matters).** Let \(K=\mathbb R\rtimes\{1,-1\}\) act on \(\mathbb R\) by \((a,\epsilon)x=a+\epsilon x\). Give \(\mathbb R\times U(1)\) the lifted action \((x,g)\mapsto(a+\epsilon x,g)\). Classify invariant connections. What goes wrong if one checks only infinitesimal isotropy equivariance?

**Solution.** At zero, \(L=\{(0,1),(0,-1)\}\), with \(\lambda=1\) and \(\mathfrak l=0\). The acting Lie algebra is \(\mathbb R\), so a linear map is \(W(X)=icX\). Conjugation by the reflection sends \(X\) to \(-X\), whereas its action on \(i\mathbb R\) is trivial. Equation (3.1) forces \(-icX=icX\), hence \(c=0\). The only invariant connection has zero potential. Infinitesimal isotropy imposes no condition at all because \(\mathfrak l=0\); it would incorrectly allow every \(ic\,dx\). Pulling such a potential back by \(x\mapsto-x\) changes its sign, which directly exhibits its failure of invariance for \(c\ne0\). □

**Exercise 6.4 (all integral Hopf weights).** Replace the Hopf isotropy homomorphism by \(\lambda_m(\operatorname{diag}(e^{it},e^{-it}))=e^{imt}\), where \(m\in\mathbb Z\). Determine all \(\mathrm{SU}(2)\)-invariant connections on \(\mathrm{SU}(2)\times_{\lambda_m}U(1)\), their curvature at the reference frame, and their holonomy.

**Solution.** The same rotation argument forces the Wang map to vanish on \(\mathfrak m\); the vertical condition gives \(W(E_3)=im\). This gives exactly one invariant connection for each \(m\). Its curvature has \(C(E_1,E_2)=-2im\). If \(m\ne0\), that value spans \(i\mathbb R\), so restricted holonomy is \(U(1)\); full holonomy, being a subgroup of \(U(1)\) containing it, is also \(U(1)\). If \(m=0\), \(\lambda_m\) is trivial and \([k,g]\mapsto(kL,g)\) is a global product trivialization. Formula (3.2) becomes \(\theta_{U(1)}\), whose global constant section is parallel. Both holonomy groups are trivial. No assertion about the topological classification of the nonzero-weight bundles is needed for these computations. □

## References

[Wang] Hsien-Chung Wang, *On invariant connections over a principal fibre bundle*, Nagoya Mathematical Journal **13** (1958), 1–19. [Original article and readable journal copy](https://doi.org/10.1017/S0027763000023461).

[Hammerl] Matthias Hammerl, *Homogeneous Cartan geometries*, Archivum Mathematicum **43** (2007), 431–442. [Author's preprint, version 3, 26 May 2011](https://arxiv.org/abs/math/0703627v3), Section 1, discusses the principal-connection classification and the holonomy algorithm; subsequent sections treat Cartan geometries.

