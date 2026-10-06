# Reductive groups, root data and the L-group

*Draft lesson. Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Public domain (CC0).*

An unramified representation of a torus is described by complex numbers assigned to its one-parameter subgroups. For a reductive group, the same idea survives, but its roots impose symmetries on those numbers. The resulting parameter belongs to a second reductive group, the dual group. If the original group is not split, a Galois action must be included. The L-group records these two pieces together.

We construct this object and calculate it for the classical groups. We assume familiarity with algebraic groups, characters and cocharacters of tori, and root systems. The structural proofs we use are in Tori, maximal tori and their conjugacy, Regular elements and centralizers, Roots and reductive groups of rank one, Root data, Weyl chambers and the Bruhat decomposition, and Pinnings and the classification of split reductive groups. Representations of Weil groups, Sections 1 and 5, supplies the local Weil groups; the global construction is proved in Brauer groups of local and global fields, Section 7. Basic freely accessible references are [Milne], [Conrad], [Getz–Hahn] and [Langlands]. All groups called reductive here are connected. Orthogonal-group examples are in characteristic different from two.

## 1. Why the dual torus has the opposite lattice

Let \(T\) be a torus over a field \(F\). Over a separable closure \(F^s\), put

\[
X=X^*(T)=\operatorname{Hom}_{F^s}(T_{F^s},\mathbf G_m),
\qquad
Y=X_*(T)=\operatorname{Hom}_{F^s}(\mathbf G_m,T_{F^s}).
\]

These are free abelian groups of the same finite rank. Composition gives a perfect pairing: \(\chi\circ\lambda(z)=z^{\langle\chi,\lambda\rangle}\). Thus \(Y=\operatorname{Hom}(X,\mathbf Z)\). Their Galois actions preserve the pairing.

**Proposition 1.1 (dual torus).** The complex torus with character lattice \(Y\) is

\[
\widehat T=\operatorname{Spec}\mathbf C[Y],\qquad
\widehat T(\mathbf C)=\operatorname{Hom}(Y,\mathbf C^\times)
\cong X\otimes_{\mathbf Z}\mathbf C^\times.
\]

The last isomorphism is canonical. The induced action is \((w\cdot t)(\lambda)=t(w^{-1}\lambda)\).

*Proof.* The group algebra \(\mathbf C[Y]\) has basis \(e^\lambda\), multiplication \(e^\lambda e^\mu=e^{\lambda+\mu}\), and coproduct \(e^\lambda\mapsto e^\lambda\otimes e^\lambda\). An algebra homomorphism to \(\mathbf C\) sends every \(e^\lambda\) to a nonzero number and is exactly a homomorphism \(Y\to\mathbf C^\times\). A basis of \(Y\) identifies the resulting algebraic group with a product of multiplicative groups. An algebraic character is a group-like element \(f=\sum c_\lambda e^\lambda\): the equation \(\Delta(f)=f\otimes f\) has no mixed terms on its left, so at most one coefficient is nonzero. Its counit is one, making that coefficient one. Thus all characters are exactly the \(e^\lambda\), and the character lattice is \(Y\).

Define the displayed tensor map by

\[
\chi\otimes z\longmapsto\bigl[\lambda\longmapsto
z^{\langle\chi,\lambda\rangle}\bigr].
\]

Bilinearity makes it well-defined. In dual bases it is the identity map on \((\mathbf C^\times)^r\), and hence an isomorphism. The formula for the action follows by precomposing a character of \(Y\) with the inverse action on \(Y\); it is compatible with the tensor description because the pairing is invariant. \(\square\)

The distinction between \(X\) and \(Y\) matters even for a split torus. Both have abstract rank \(r\), but there is no preferred identification between them. The expression \(Y\otimes\mathbf C^\times\) instead has character lattice \(X\).

For a nonarchimedean field with uniformizer \(\varpi\), a split torus satisfies

\[
T(F)/T(\mathcal O_F)\cong Y,\qquad
\lambda\longmapsto\lambda(\varpi).
\]

To see this, choose coordinates \(T\cong\mathbf G_m^r\) and apply the valuation to each coordinate. An unramified complex character \(\xi\) of \(T(F)\) therefore gives the dual point \(t_\xi(\lambda)=\xi(\lambda(\varpi))\). Replacing \(\varpi\) by a unit times \(\varpi\) changes the representative by \(T(\mathcal O_F)\), so the point is unchanged. This is the simplest Satake parameter.

## 2. Roots determine the dual group, including its isogeny type

A connected reductive group over \(F\) is a smooth affine group whose geometric fibres are connected and have trivial connected unipotent radical. Choose a maximal torus \(T\) in \(G_{F^s}\). Its root datum is

\[
\mathcal R(G,T)=(X,\Phi,Y,\Phi^\vee).
\]

Here \(\Phi\subset X\) is the set of nonzero torus weights on the Lie algebra, and each root \(\alpha\) has a coroot \(\alpha^\vee\in Y\). In particular, \(\langle\alpha,\alpha^\vee\rangle=2\). The reflections are

\[
s_\alpha(x)=x-\langle x,\alpha^\vee\rangle\alpha,
\qquad
s_\alpha(y)=y-\langle\alpha,y\rangle\alpha^\vee.
\]

The same notation on the two lattices denotes mutually dual actions. Root data, Weyl chambers and the Bruhat decomposition, Theorem 2.1 proves that these data satisfy the reduced root-datum axioms. Theorem 4.1 there identifies a Borel subgroup \(B\supset T\) with a positive system, hence with simple roots \(\Delta\) and simple coroots \(\Delta^\vee\).

**Definition 2.1.** The dual root datum is

\[
\mathcal R^\vee=(Y,\Phi^\vee,X,\Phi).
\]

The pairing and reflection axioms are symmetric in roots and coroots, so this is again a reduced root datum.

The Langlands dual group \(\widehat G\) is a complex connected reductive group with this datum. Its existence and uniqueness follow from Pinnings and the classification of split reductive groups, Theorems 10.1 and 5.1. These are the root-data classification theorems of Chevalley and Demazure. They construct a group for every reduced datum and prove that isomorphisms of based data lift uniquely once pinnings are fixed. Applying them over \(\mathbf C\) defines \(\widehat G\). A based dual datum specifies \((\widehat G,\widehat B,\widehat T)\); a pinning removes the remaining ambiguity in isomorphisms. For a free human treatment, see [Conrad 2014, Theorems 6.1.16(2) and 6.1.17].

Dualizing twice returns the original datum. Merely dualizing a Dynkin diagram is insufficient: the lattices specify whether a semisimple group is simply connected, adjoint or intermediate. For example, the diagrams of \(SL_2\) and \(PGL_2\) agree, but their dual groups do not.

A group over \(F\) is **split** if it has a split maximal torus; it is **quasi-split** if it has an \(F\)-defined Borel subgroup. A split group is quasi-split because each positive system gives an \(F\)-defined Borel by the preceding theorem. Two groups are **inner forms** if an isomorphism over \(F^s\) makes their descent actions differ by inner automorphisms. Section 4 proves that they have the same action on the based root datum and hence the same L-group. Their local representation theories and the relevance conditions on parameters can differ. The L-group alone does not classify inner forms.

For orientation, \(GL_n\), \(SL_n\), \(PGL_n\) and the split symplectic and special orthogonal groups are split; their displayed tori below exhibit this. Section 5 treats unitary groups and restriction of scalars. For a central simple algebra \(A\) of degree \(n\), Automorphisms, forms and parabolic subgroups, Lemma 6.1 and Theorem 6.2 proves that \(A\) becomes \(\operatorname{Mat}_n\) over a finite separable extension and that its algebra descent maps are conjugations by matrices. Restricting those maps to units shows directly that \(A^\times\) is an inner form of \(GL_n\).

### Root subgroups and Borel pairs

We make explicit the structure used in the calculations and in the pinning comparison. Over an algebraically closed field, the root subgroup attached to \(\alpha\) has a parameter \(x_\alpha:\mathbf G_a\to U_\alpha\) satisfying

\[
t x_\alpha(u)t^{-1}=x_\alpha(\alpha(t)u).
\tag{2.1}
\]

Its tangent space is the one-dimensional root space. This statement, including existence of the parameter and its torus equivariance, is proved in Roots and reductive groups of rank one, Theorem 4.1. The coroot is the diagonal cocharacter of the associated rank-one \(SL_2\)-map, constructed there in Theorems 6.1 and 7.1.

**Lemma 2.2 (generation and the stabilizer of a Borel pair).** Let \(H\) be split connected reductive over a field \(k\), with split maximal torus \(T\subset B\). The torus and the root subgroups generate \(H(k)\), and

\[
N_H(B)(k)\cap N_H(T)(k)=T(k).
\tag{2.2}
\]

Every element of \(Z(H)(k)\) lies in \(T(k)\).

*Proof.* The root coordinates of Root data, Weyl chambers and the Bruhat decomposition, Section 5 express the unipotent radical of \(B\) as an ordered product of its positive root groups. Thus \(B\) is generated by \(T\) and those groups. Theorem 6.2 of that lesson expresses every point as \(b_1n_wb_2\). Each representative \(n_w\) is a product of the simple representatives

\[
n_\alpha=x_\alpha(1)x_{-\alpha}(-1)x_\alpha(1),
\]

by the rank-one formulas of the same lesson, Section 2. This proves generation.

An element normalizing both \(B\) and \(T\) induces a Weyl element preserving the positive roots of \(B\). Theorem 4.1 of that lesson proves that the Weyl group acts simply transitively on positive systems, so this Weyl element is the identity. The element therefore centralizes \(T\). Regular elements and centralizers, Theorem 2.2 proves the schematic identity \(C_H(T)=T\), giving (2.2) on \(k\)-points. The same centralizer theorem puts any central \(k\)-point in \(T(k)\). \(\square\)

Finally, Borel subgroups are conjugate by Tori, maximal tori and their conjugacy, Lemma 2.1. Its Section 2 proves that maximal tori of a connected solvable group are conjugate within that group. Applied to \(B\), these two results make all Borel pairs conjugate. These are proofs already supplied by the preceding lessons; the free references [Milne, 19.11–19.22] and [Conrad, Corollary 1.2.4] give further treatments of the root and centralizer statements.

## 3. Calculating the classical dual groups

Write \(e_1,\ldots,e_n\) for coordinate characters and \(f_1,\ldots,f_n\) for their dual cocharacters. In the formulas involving \(\mathbf Z^n\), the pairing is the ordinary dot product. The following calculations determine the full root data, not just the Lie algebras.

**Theorem 3.1.** For the split groups, the duals are

| Group | Complex dual group |
|---|---|
| \(GL_n\) | \(GL_n(\mathbf C)\) |
| \(SL_n\) | \(PGL_n(\mathbf C)\) |
| \(PGL_n\) | \(SL_n(\mathbf C)\) |
| \(Sp_{2n}\) | \(SO_{2n+1}(\mathbf C)\) |
| \(SO_{2n+1}\) | \(Sp_{2n}(\mathbf C)\) |
| \(SO_{2n}\), \(n\geq2\) | \(SO_{2n}(\mathbf C)\) |

*Proof.* For \(GL_n\), the diagonal torus has \(X=Y=\mathbf Z^n\). Conjugation on the matrix unit \(E_{ij}\) has weight \(e_i-e_j\). Its coroot sends \(z\) to a diagonal matrix with entries \(z,z^{-1}\) in positions \(i,j\), so it is \(f_i-f_j\). Interchanging the two lattices gives the same datum.

For \(SL_n\), restricting characters from the diagonal torus of \(GL_n\) kills exactly the determinant. Thus

\[
X=\mathbf Z^n/\mathbf Z(1,\ldots,1),\qquad
Y=\{(a_i)\in\mathbf Z^n\mid\sum_i a_i=0\}.
\]

Roots are the classes of \(e_i-e_j\); coroots are \(f_i-f_j\) in the sum-zero lattice. For \(PGL_n\), a character of the diagonal torus must be trivial on scalar matrices. Its datum has

\[
X=\{(a_i)\in\mathbf Z^n\mid\sum_i a_i=0\},\qquad
Y=\mathbf Z^n/\mathbf Z(1,\ldots,1),
\]

with the same coordinate differences interpreted in these lattices. The two data are dual.

For \(Sp_{2n\!}\), use the torus

\[
\operatorname{diag}(t_1,\ldots,t_n,t_1^{-1},\ldots,t_n^{-1}).
\]

Its character and cocharacter lattices are \(\mathbf Z^n\). In block form the symplectic Lie algebra consists of matrices

\[
\begin{pmatrix}A&B\\ C&-A^t\end{pmatrix},\qquad B=B^t,\quad C=C^t.
\]

The off-diagonal entries of \(A\) have weights \(e_i-e_j\); the entries of \(B,C\) have weights \(\pm(e_i+e_j)\), including \(\pm2e_i\) on their diagonals. Therefore

\[
\Phi=\{\pm e_i\pm e_j:i<j\}\cup\{\pm2e_i\},
\qquad
\Phi^\vee=\{\pm f_i\pm f_j:i<j\}\cup\{\pm f_i\}.
\]

Here are the rank-one maps that determine the coroots. Choose paired basis vectors \(v_i,w_i\) with symplectic pairing \((v_i,w_j)=\delta_{ij}\). For the root \(2e_i\), let \(SL_2\) act on \(\langle v_i,w_i\rangle\), fixing its symplectic complement. Its diagonal acts with \(t_i=z\), giving coroot \(f_i\). For \(e_i-e_j\), act by \(A\in SL_2\) on \(\langle v_i,v_j\rangle\) and by \(A^{-t}\) on \(\langle w_i,w_j\rangle\). The diagonal gives \(t_i=z,t_j=z^{-1}\), so its coroot is \(f_i-f_j\). Conjugate this map by the symplectic change \(v_j\mapsto w_j,w_j\mapsto-v_j\) to obtain the root \(e_i+e_j\) and coroot \(f_i+f_j\). Negative roots use the opposite parameters and negative coroots. Each map has the prescribed root tangent line, so the intrinsic rank-one characterization above identifies these diagonal maps with the coroots.

In \(SO_{2n+1}\) the torus has eigenvalues \(t_1,\ldots,t_n,1,t_1^{-1},\ldots,t_n^{-1}\) on the standard representation. If \(q\) denotes its nondegenerate symmetric pairing, the map

\[
v\wedge w\longmapsto\bigl[u\longmapsto q(v,u)w-q(w,u)v\bigr]
\]

identifies the exterior square with the orthogonal Lie algebra: it takes values in the skew operators for \(q\), is injective in a paired basis, and both spaces have dimension \(\binom{2n+1}{2}\). Adding two distinct standard weights therefore gives the nonzero weights \(\pm e_i\pm e_j\) and \(\pm e_i\). There is no weight \(2e_i\), since a basis vector wedges with itself to zero. The displayed torus is \(\mathbf G_m^n\), so \(X=Y=\mathbf Z^n\).

For \(e_i-e_j\), the action by \(A,A^{-t}\) on two paired isotropic planes again preserves \(q\), has determinant one, and gives coroot \(f_i-f_j\). Swapping \(v_j,w_j\) is an orthogonal change of basis; its conjugation preserves \(SO_{2n+1}\) and carries this map to the one with root \(e_i+e_j\) and coroot \(f_i+f_j\). For the short root \(e_i\), use the \(SL_2\)-action on binary quadratic forms. It preserves their nondegenerate discriminant pairing and acts on the basis \(u^2,uv,v^2\) with diagonal weights \(z^2,1,z^{-2}\). The discriminant model is isometric, after rescaling its paired basis over the algebraically closed field, to \(\langle v_i,v_0,w_i\rangle\). Extend this action by the identity on the complement. Its positive root tangent vector has torus weight \(e_i\), and its diagonal has \(t_i=z^2\). Thus its coroot is \(2f_i\). These maps, and their opposites, give all coroots. The resulting datum is exactly the dual symplectic datum, in both directions.

For \(SO_{2n}\), the middle eigenvalue \(1\) is absent. The exterior-square calculation gives only \(\pm e_i\pm e_j\), and the coroots are \(\pm f_i\pm f_j\). Both lattices are \(\mathbf Z^n\), so the datum is self-dual. The assertion includes \(n=2\), whose root system has two \(A_1\) factors. For \(n=1\), \(SO_2\cong\mathbf G_m\) is instead the torus calculation of Proposition 1.1. \(\square\)

The lattice calculation also describes the centres. It is useful to derive the relation once rather than memorize a table.

**Proposition 3.2 (centre and algebraic fundamental group).** Define

\[
\pi_1(G)=Y/\mathbf Z\Phi^\vee.
\]

For a split connected reductive group,

\[
Z(\widehat G)(\mathbf C)
=\operatorname{Hom}(\pi_1(G),\mathbf C^\times).
\]

For semisimple \(G\), \(\pi_1(G)\) is finite. The group called \(\pi_1\) here is the algebraic fundamental group defined by the root datum.

*Proof.* Lemma 2.2 puts every central element in \(\widehat T\). Equation (2.1) says that \(z\in\widehat T\) conjugates the root subgroup for \(\beta\in\Phi^\vee\) by multiplying its coordinate by \(\beta(z)\). It is central exactly when every such value is one, by the generation proved in that lemma. Consequently, on complex points,

\[
Z(\widehat G)(\mathbf C)=\bigcap_{\beta\in\Phi^\vee}\ker(\beta)(\mathbf C)
\subset\widehat T(\mathbf C).
\]

A point of \(\widehat T\) is a homomorphism \(Y\to\mathbf C^\times\). Being trivial on all coroots is exactly factoring through \(Y/\mathbf Z\Phi^\vee\). This proves the formula. In the semisimple case coroots span \(Y\otimes\mathbf Q\), so their lattice has finite index. \(\square\)

For \(SL_n\), the coroots generate \(Y\), hence the dual has trivial centre. For \(PGL_n\), imposing all coordinate differences on \(\mathbf Z^n\) identifies every basis vector with one generator; the additional relation \((1,\ldots,1)=0\) is \(n\) times that generator. The quotient is therefore \(\mathbf Z/n\mathbf Z\), giving \(Z(SL_n)=\mu_n\). For \(Sp_{2n}\), the coroots include all \(f_i\), giving trivial dual centre. For \(SO_{2n+1}\), the coroots generate the even-sum lattice. For \(n\geq2\), the differences \(f_i-f_j\) reduce any vector to its coordinate sum times one basis vector, and \((f_i+f_j)+(f_i-f_j)=2f_i\) supplies every even sum; all the generators themselves have even sum. For \(n=1\), the coroot lattice is directly \(2\mathbf Zf_1\). Thus the dual centre is \(\mu_2\). For \(SO_{2n}\), \(n\geq2\), the same even-sum calculation gives \(\mu_2\), in agreement with \(\{I,-I\}\subset SO_{2n}\).

## 4. Turning the Galois action into group automorphisms

Galois need not preserve the chosen pair \((B,T)\). Write \(G^{\mathrm{ad}}=G/Z(G)\); it acts on \(G\) by inner automorphisms, as proved in Automorphisms, forms and parabolic subgroups, Theorem 3.1. Write \(\sigma_\gamma\) for the semilinear descent action of \(\gamma\in\operatorname{Gal}(F^s/F)\). Choose \(g_\gamma\in G^{\mathrm{ad}}(F^s)\) so that

\[
f_\gamma=\operatorname{Int}(g_\gamma)\sigma_\gamma
\]

preserves \(B,T\), and take its induced action on \((X,\Delta,Y,\Delta^\vee)\). The Borel-pair conjugacy proved above supplies these elements. Over a separably closed field the same argument applies: the Borel-pair transporters are nonempty and smooth, by the Borel and torus conjugacy constructions in Automorphisms, forms and parabolic subgroups, Theorem 3.1. A nonempty smooth scheme of finite type has a point over a finite separable extension, by an étale coordinate chart; over \(F^s\) that point is already rational.

If \(g'_\gamma\) is another correction, \(g'_\gamma g_\gamma^{-1}\) normalizes the images of both \(B\) and \(T\) in the adjoint group, hence lies in \(T^{\mathrm{ad}}\) by Lemma 2.2 applied there. Its conjugation acts trivially on \(T\), and hence on both lattices. Thus the resulting **based**, or star, action is independent of the correction. Moreover

\[
f_\gamma f_\delta
=\operatorname{Int}\bigl(g_\gamma\sigma_\gamma(g_\delta)\bigr)\sigma_{\gamma\delta}.
\]

This and \(f_{\gamma\delta}\) preserve the same pair, so their difference is again the action of \(T^{\mathrm{ad}}\). Their lattice actions agree, proving the group law for the star action. Choose a finite separable extension over which the group is split, \(B,T\) are defined, and a basis of their characters is defined. Its Galois subgroup acts trivially on the based datum. Taking the Galois closure shows that the action factors through a finite quotient, even when the full automorphism group of the based datum is infinite.

For an inner form with descent action \(\sigma'_\gamma=\operatorname{Int}(z_\gamma)\sigma_\gamma\), where \(z_\gamma\in G^{\mathrm{ad}}(F^s)\), use \(g'_\gamma=g_\gamma z_\gamma^{-1}\). The corrected semilinear automorphism is exactly \(f_\gamma\). Hence inner forms have the same star action. Using the adjoint group also makes this argument valid when an adjoint point has no lift to \(G(F^s)\).

A pinning of a complex reductive group is a pair \((\widehat B,\widehat T)\) together with a nonzero vector \(X_\alpha\) in each simple root space. Pinnings and the classification of split reductive groups, Theorem 5.1 lifts each based-datum automorphism uniquely to an algebraic automorphism preserving this pinning. Uniqueness makes the lift of a product equal the product of the lifts. Applying this to the dual star action gives

\[
a:W_F\longrightarrow\operatorname{Aut}(\widehat G).
\]

The Weil group acts through its map to the Galois group. Define

\[
{}^LG=\widehat G(\mathbf C)\rtimes_a W_F,\qquad
(g,w)(h,u)=(ga(w)(h),wu).
\]

The topology is the product topology. One may also use \(\widehat G\rtimes\operatorname{Gal}(F^s/F)\), or replace Galois by a finite quotient through which its action factors. The finite quotient retains the action on \(\widehat G\); it does not retain all Weil-group information needed for archimedean parameters or reciprocity.

**Proposition 4.1 (independence of the pinning).** Two pinnings yield isomorphic L-groups, with the isomorphism commuting with projection to \(W_F\).

*Proof.* First conjugate their Borel subgroups into agreement, then conjugate their maximal tori inside that Borel into agreement, using the preceding Borel-pair conjugacy proofs. Equation (2.1) and the one-dimensional root spaces show that the two sets of simple root vectors now differ by scalars \(c_\alpha\in\mathbf C^\times\).

There exists \(t\in\widehat T\) with \(\alpha(t)=c_\alpha\) for every simple root. Indeed, simple roots are independent over \(\mathbf Q\). The map \(\widehat T\to(\mathbf C^\times)^{|\Delta|}\) has a character-lattice map which is injective; Smith normal form reduces its surjectivity on complex points to the surjectivity of \(z\mapsto z^m\) on \(\mathbf C^\times\). Conjugation by \(t\) therefore makes the vectors agree. We have obtained an inner automorphism \(c\) taking the first entire pinning to the second.

If \(a(w)\) is the first pinned lift, then \(c a(w)c^{-1}\) preserves the second pinning and induces the same transported action on its based datum. The uniqueness in the pinned isomorphism theorem makes it the second lift \(a'(w)\). The map

\[
(g,w)\longmapsto(c(g),w)
\]

is thus a homomorphism: \(c(ga(w)(h))=c(g)a'(w)(c(h))\). Its inverse uses \(c^{-1}\), and it is continuous and algebraic on the connected factor. It fixes the quotient \(W_F\). \(\square\)

For split groups the star action is trivial, so all entries of Theorem 3.1 give direct products with \(W_F\). For instance,

\[
{}^LSL_2=PGL_2(\mathbf C)\times W_F,\qquad
{}^LPGL_2=SL_2(\mathbf C)\times W_F.
\]

## 5. Unitary groups and restriction of scalars

Let \(E/F\) be quadratic and separable, with conjugation \(x\mapsto\bar x\). Take the Hermitian form with matrix \(H_n\) having every antidiagonal entry equal to one. Its unitary group is

\[
U(n)(R)=\{g\in GL_n(E\otimes_F R):\bar g^{\,t}H_ng=H_n\}.
\]

After extending to \(F^s\), the algebra \(E\otimes_F F^s\) is \(F^s\times F^s\) and conjugation exchanges the factors. A unitary element becomes a pair \((g,h)\) with \(h^tH_ng=H_n\), so \(h=H_ng^{-t}H_n^{-1}\). Projection to \(g\) identifies the group with \(GL_n\). The nontrivial Galois element therefore acts by \(g\mapsto H_ng^{-t}H_n^{-1}\). This action preserves the upper triangular Borel and diagonal torus: transpose inverse reverses triangularity, and antidiagonal conjugation reverses it back. Those subgroups descend to \(F\), making this model quasi-split. On diagonal characters the action is \(e_i\mapsto-e_{n+1-i}\). Thus \(\widehat{U(n)}=GL_n(\mathbf C)\), and its dual based action reverses the coordinates and changes their signs.

Put \(J_n\) equal to the antidiagonal matrix with antidiagonal entries \(1,-1,1,-1,\ldots\), and set

\[
\tau(g)=J_n(g^t)^{-1}J_n^{-1}.
\]

Inverse transpose is a homomorphism, since \((gh)^{-t}=g^{-t}h^{-t}\). Also \(J_n^t=(-1)^{n-1}J_n\), so \(\tau^2=1\). On the diagonal torus,

\[
\tau(\operatorname{diag}(z_1,\ldots,z_n))
=\operatorname{diag}(z_n^{-1},\ldots,z_1^{-1}).
\]

It preserves the upper triangular Borel. Its differential sends \(E_{i,i+1}\) to \(E_{n-i,n+1-i}\): the minus sign from inverse transpose is cancelled by adjacent antidiagonal signs. Thus it preserves the standard pinning, with its simple root vectors permuted. This verifies the precise lift of the diagram action, rather than just its outer-automorphism class.

Consequently

\[
{}^LU(n)=GL_n(\mathbf C)\rtimes W_F,
\]

where \(W_E\) acts trivially and the other coset acts by \(\tau\). Restriction of this extension to \(W_E\) is \(GL_n(\mathbf C)\times W_E\). For \(n\geq3\), \(\tau\) induces the nontrivial reversal of the \(A_{n-1}\) diagram; for \(n=2\), that diagram has one node, but \(\tau\) still inverts the centre and is not an inner automorphism of \(GL_2\).

**Example 5.1 (two variables).** With \(J_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\), direct multiplication gives

\[
\tau(g)=\frac{g}{\det g}.
\]

Indeed, if \(g=\begin{pmatrix}a&b\\c&d\end{pmatrix}\), its inverse transpose is \((\det g)^{-1}\begin{pmatrix}d&-c\\-b&a\end{pmatrix}\), and conjugation by \(J_2\) returns \((\det g)^{-1}g\). Thus \(\tau\) fixes \(SL_2\) pointwise but inverts scalar matrices. A nonsplit unitary group in two variables has this nontrivial L-group action even though its derived-group diagram looks split.

**Proposition 5.2 (restriction of scalars).** For a finite separable extension \(E/F\), let \(\Sigma=\operatorname{Hom}_F(E,F^s)\). Then

\[
\widehat{\operatorname{Res}_{E/F}GL_n}
=\prod_{\sigma\in\Sigma}GL_n(\mathbf C),\qquad
{}^L(\operatorname{Res}_{E/F}GL_n)
=\left(\prod_{\sigma\in\Sigma}GL_n(\mathbf C)\right)\rtimes W_F,
\]

with Galois permuting the factors through its action on \(\Sigma\).

*Proof.* The separable algebra \(E\otimes_FF^s\) is the product of copies of \(F^s\) indexed by \(\Sigma\). Accordingly, restriction of scalars becomes the product of those \(GL_n\)'s. Its character lattice is the direct sum of their character lattices; roots and coroots stay in their own factors. Dualizing therefore gives the same product. Galois sends the factor indexed by \(\sigma\) to that indexed by \(\gamma\sigma\), and the product of the standard pinnings makes these permutations pinned automorphisms. \(\square\)

For a quadratic extension and \(n=1\), this is \((\mathbf C^\times\times\mathbf C^\times)\rtimes W_F\), with the other coset exchanging the two coordinates. It differs from \({}^LU(1)=\mathbf C^\times\rtimes W_F\), where that coset inverts the coordinate. Restriction of scalars and the norm-one torus are distinct constructions.

## 6. Maps and parameters

An **L-homomorphism** \({}^LH\to{}^LG\) is a continuous homomorphism over \(W_F\) whose restriction \(\widehat H\to\widehat G\) is algebraic. A parameter is considered up to conjugation by \(\widehat G\), not by an arbitrary automorphism of the target.

For a nonarchimedean local field, a parameter in the \(SL_2\) convention is a homomorphism

\[
W_F\times SL_2(\mathbf C)\longrightarrow{}^LG
\]

over \(W_F\). We use the \(SL_2\) convention of Beyond general linear groups: parameters and packets, Section 1: its Weil restriction is continuous, its \(SL_2\)-restriction is algebraic, its dual inertia coordinates form a finite set, and its Weil images are semisimple in the finite-action target described below. We also require relevance for the chosen \(F\)-form. Explicitly, let \(\Theta\) be any Galois-stable subset of the dual simple roots and \(\widehat P_\Theta\) the corresponding standard parabolic. If the image is contained, after \(\widehat G\)-conjugation, in \(\widehat P_\Theta\rtimes W_F\), then \(G\) must have an \(F\)-parabolic of the corresponding geometric type, using the matching simple roots in its original datum. The parabolic types and their descent are proved in Automorphisms, forms and parabolic subgroups, Theorems 1.1 and 2.1. This condition is where an inner form can restrict the permitted parameters.

Write \(\phi(w,1)=(c(w),w)\) and let \(a(w)\) denote the pinned action. The homomorphism law gives

\[
c(wu)=c(w)a(w)(c(u)).
\]

The finite-inertia condition concerns \(c(I_F)\); semisimplicity of Weil images is understood after mapping to \(\widehat G\rtimes\Gamma\), where \(\Gamma\) is a finite quotient through which the pinned action factors. The full Weil projection is retained. In particular, an inertia element \(i\) cannot have full image equal to the identity unless \(i=1\).

Suppose now that inertia acts trivially on \(\widehat G\); this is the based-action condition used for an unramified group. An **unramified parameter** has \(c(i)=1\), equivalently \(\phi(i,1)=(1,i)\), for every \(i\in I_F\), and trivial algebraic \(SL_2\) part. Representations of Weil groups, Proposition 1.1 proves \(W_F=I_F\rtimes\langle\Phi\rangle\) for a Frobenius lift \(\Phi\). Hence a parameter of this kind is determined by \(\phi(\Phi,1)=(g,\Phi)\): define its values on powers by the homomorphism law, and the inertia relation holds because inertia acts trivially. Admissibility imposes semisimplicity in the finite-action target, and relevance is still required for the chosen form. Conjugation by \(h\in\widehat G\) sends \(g\) to \(hg\,a(\Phi)(h^{-1})\). For split groups this is ordinary semisimple conjugacy in \(\widehat G\).

The unramified-action hypothesis matters. If a ramified pinned action is allowed, homomorphisms with the canonical inertia section \(\phi(i,1)=(1,i)\) require

\[
g\in\widehat G^{I_F},\qquad
g\sim hg\,a(\Phi)(h^{-1})\quad(h\in\widehat G^{I_F}).
\]

Indeed conjugating \((1,i)\) by \((g,\Phi)\) gives

\[
\bigl(g\,a(\Phi i\Phi^{-1})(g^{-1}),\Phi i\Phi^{-1}\bigr).
\]

Equality with \((1,\Phi i\Phi^{-1})\) forces the fixed-subgroup condition, because \(\Phi\) normalizes inertia. Conversely that condition verifies the defining relation in \(W_F=I_F\rtimes\langle\Phi\rangle\), so the prescribed inertia and Frobenius values extend to a homomorphism. Conjugation by \(h\) preserves the canonical inertia section exactly when \(h\in\widehat G^{I_F}\), proving the stated equivalence relation. For example, the dual of a ramified quadratic norm-one torus is \(\mathbf C^\times\) with inertia acting by inversion. Its fixed subgroup is \(\{1,-1\}\). A Frobenius lift with trivial pinned action and candidate \(g=2\) would give dual coordinate \(2(1/2)^{-1}=4\) in the displayed conjugation, contradicting the required coordinate one.

At an archimedean place, use its archimedean Weil group. Over a number field, a single universally constructed global parameter group classifying all automorphic representations is conjectural. The formal expression “global L-parameter” must therefore specify its proposed domain. A compatible Galois representation and an automorphic representation are concrete objects; the existence of a universal global Langlands group is an additional conjecture. The functoriality and reciprocity lessons distinguish these assertions.

## 7. Exercises

**Exercise 7.1 (basic).** For the diagonal tori in \(GL_2\) and \(SL_2\), compute both lattices, the two roots, the two coroots and the dual groups. Explain why the root in \(SL_2\) is twice a primitive character.

**Exercise 7.2 (intermediate).** Calculate the dual of \(Sp_4\), including its centre, without identifying a group from its Lie algebra alone.

**Exercise 7.3 (intermediate).** For quadratic \(E/F\), describe the L-group of \(\operatorname{Res}_{E/F}\mathbf G_m\). Embed the dual norm-one torus in its connected factor and check equivariance.

**Exercise 7.4 (advanced).** Write the pinned action for \(U(3)\) explicitly. Verify its order, its effect on both simple root vectors and its restriction to \(W_E\). Determine its action on the centre.

## 8. Solutions

**Solution 7.1.** For \(GL_2\), \(X=\mathbf Ze_1\oplus\mathbf Ze_2\), \(Y=\mathbf Zf_1\oplus\mathbf Zf_2\), \(\Phi=\{\pm(e_1-e_2)\}\), and \(\Phi^\vee=\{\pm(f_1-f_2)\}\). Interchanging lattices preserves this datum, so the dual is \(GL_2\).

The torus in \(SL_2\) is \(\operatorname{diag}(t,t^{-1})\). Let \(e(t)=t\) and let \(f:z\mapsto\operatorname{diag}(z,z^{-1})\). Then \(X=\mathbf Ze\), \(Y=\mathbf Zf\), \(\langle e,f\rangle=1\), the roots are \(\pm2e\), and the coroots are \(\pm f\). Conjugation on \(E_{12}\) multiplies it by \(t^2\), proving the assertion about twice a primitive character. The dual datum has primitive roots and doubled coroots, the datum of \(PGL_2\). This lattice distinction is why the simply connected group becomes adjoint.

**Solution 7.2.** The two lattices are \(\mathbf Z^2\). The roots of \(Sp_4\) are \(\pm e_1\pm e_2,\pm2e_1,\pm2e_2\); their coroots are \(\pm f_1\pm f_2,\pm f_1,\pm f_2\). The dual datum is \(B_2\) with coordinate character lattice \(\mathbf Z^2\), exactly the datum of \(SO_5\). Since \(f_1,f_2\) are themselves coroots of the original group, the original \(\pi_1\) is zero. Proposition 3.2 gives trivial centre for the dual. In particular the answer is \(SO_5\), not its simply connected cover \(Spin_5\).

**Solution 7.3.** The character and cocharacter lattices of the restriction-of-scalars torus are permutation lattices on two embeddings. Their dual torus is \((\mathbf C^\times)^2\); \(W_E\) acts trivially and the other coset exchanges coordinates. The dual of the norm-one torus is \(\mathbf C^\times\) with inversion action. Its embedding is

\[
z\longmapsto(z,z^{-1}).
\]

Swapping the two target coordinates sends this point to \((z^{-1},z)\), the image of \(z^{-1}\). Thus it is equivariant and extends to an L-homomorphism which is the identity on \(W_F\). The corresponding original-torus map is the quotient \((x,y)\mapsto x/y\) after splitting, illustrating the reversal of arrows under duality.

**Solution 7.4.** Take

\[
J_3=\begin{pmatrix}0&0&1\\0&-1&0\\1&0&0\end{pmatrix}.
\]

Here \(J_3^t=J_3=J_3^{-1}\). Hence applying \(g\mapsto J_3g^{-t}J_3^{-1}\) twice returns \(g\). The derivative \(X\mapsto-J_3X^tJ_3^{-1}\) sends \(E_{12}\) to \(E_{23}\) and \(E_{23}\) to \(E_{12}\). It preserves the upper triangular Borel and diagonal torus and exchanges the two pinned simple root vectors. The diagonal map is \((z_1,z_2,z_3)\mapsto(z_3^{-1},z_2^{-1},z_1^{-1})\). On scalar matrices it sends \(zI\) to \(z^{-1}I\). This is the pinned lift of the nontrivial quadratic Galois action, and it acts trivially for every \(w\in W_E\). Restricting the extension therefore gives \(GL_3(\mathbf C)\times W_E\), as required.

## Prerequisite proofs

The following are proved prerequisites, with the hypotheses we use here.

- **Classification and pinned isomorphisms.** Every reduced root datum is realized by a split connected reductive group; for pinned split groups, a based-datum isomorphism lifts uniquely to a pinning-preserving group isomorphism. We apply this over \(\mathbf C\). The proofs are Pinnings and the classification of split reductive groups, Theorems 10.1 and 5.1, using the construction in Sections 6–10. See also [Conrad, Theorems 6.1.16(2) and 6.1.17] and [Milne, 19.52 and 19.58].
- **Conjugacy.** For a smooth connected affine group over an algebraically closed field, Borel subgroups are conjugate; maximal tori in a connected solvable group are conjugate within it. These are proved in Tori, maximal tori and their conjugacy, Section 2, Lemma 2.1 and Theorem 2.2. For the separably closed case, the smooth transporters used in Automorphisms, forms and parabolic subgroups, Theorem 3.1 supply rational conjugacies as explained in Section 4.
- **Roots, coroots and the big cell.** In a split connected reductive group over a field, each root space is one-dimensional, its additive root parameter satisfies (2.1), and the rank-one \(SL_2\)-map has the prescribed coroot. These are proved in Roots and reductive groups of rank one, Theorems 4.1, 6.1 and 7.1. The reduced datum, positive systems, root-product coordinates and Bruhat decomposition are proved in Root data, Weyl chambers and the Bruhat decomposition, Theorems 2.1, 4.1 and 6.2 and Section 5. Lemma 2.2 proves the generation consequence we need.
- **Centralizer.** If \(H\) is connected reductive over a field and \(T\) is a maximal torus, then \(C_H(T)=T\) schematically, proved in Regular elements and centralizers, Theorems 2.1–2.2. We use its points consequence over \(\mathbf C\) and \(F^s\). See also [Conrad, Corollary 1.2.4].
- **Weil groups and parabolic types.** The local exact sequence, its Frobenius splitting, the subgroup \(W_E=G_E\cap W_F\) for a finite separable extension, and the archimedean groups are provided in Representations of Weil groups, Propositions 1.1–1.2 and Section 5. For a number field, the locally compact global Weil group, its continuous dense Galois map and its maps from the local Weil groups are constructed in Brauer groups of local and global fields, Theorem 24.6 and Section 7, using relative fundamental-class extensions and their inverse limit. The parabolic types used to define relevance are proved in Automorphisms, forms and parabolic subgroups, Theorems 1.1 and 2.1. Section 6 adopts the parameter definition of Beyond general linear groups: parameters and packets, Section 1; it asserts no local or global correspondence. The original role of the dual group and its Galois extension is described in [Langlands, Sections 2–3].

## References

- [Milne] J. S. Milne, [*Reductive Groups*](https://www.jmilne.org/math/CourseNotes/RG.pdf), free author notes, version 2.00, 10 March 2018. Section 19, especially 19.11–19.22, 19.49–19.52 and 19.58, treats roots, pinnings and classification. The numbering here is that of these notes.
- [Conrad] B. Conrad, [*Reductive Group Schemes*](https://math.stanford.edu/~conrad/papers/luminysga3smf.pdf), freely accessible author's text, 2014. Corollary 1.2.4 gives the maximal-torus centralizer; Theorems 6.1.16(2) and 6.1.17 give existence and pinned classification.
- [Getz–Hahn] J. R. Getz and H. Hahn, [*An Introduction to Automorphic Representations, with a View toward Trace Formulae*](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), free author draft of 22 April 2022. Theorem 1.8.3 concerns classification and Section 7.3 constructs the dual group and Galois action; Proposition 7.3.2 identifies pinned automorphisms with based-datum automorphisms. All locators refer to this draft.
- [Langlands] R. P. Langlands, [“Problems in the theory of automorphic forms”](https://publications.ias.edu/sites/default/files/problems-in-the-theory-of-automorphic-forms-rpl_2.pdf), 1970, freely accessible author re-typeset edition compiled 27 January 2023. Sections 2–3 construct the dual group and its Galois extension.
