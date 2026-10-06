# The Fourier transform of D-modules

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

Fourier transformation turns a position into a differentiation operator. For algebraic differential equations this is an exact operation, with no integral convergence condition. An exponential kernel gives the same operation geometrically. On an abelian variety the kernel changes: a universal line bundle with connection replaces the exponential, and the answer lives on a space of flat line bundles.

The algebraic arguments work over a field $k$ of characteristic zero. Geometric varieties are smooth over an algebraically closed such field; the comparison with topological sheaves uses $k=\mathbb C$. Modules are left D-modules, quasi-coherent over the structure sheaf. Complexes have cohomological grading. We use the Bernstein filtration, direct images, base change and the projection formula, and regular singularities. The sheaf transform belongs to Fourier kernels as radial averaging.

Our signs and shifts will be fixed by two tests:
\[
\mathcal F(\delta_a)=\mathcal O_{\mathbb A^1}e^{-ay},
\qquad
\mathcal F^2=(-1)^*
\quad\text{without a shift}.                              \tag{0.1}
\]
Here $\mathcal O e^f$ denotes the algebraic rank-one module with generator $e$ and $\partial(e)=\partial(f)e$. This notation does not assert that the exponential is an algebraic function. A horizontal section has coefficient proportional to $e^{-f}$.

## 1. Transporting a Weyl module

Write
\[
A_x=k\langle x_1,\ldots,x_n,\partial_{x_1},\ldots,\partial_{x_n}\rangle,
\qquad [\partial_{x_i},x_j]=\delta_{ij},
\]
and use $y_i,\partial_{y_i}$ for a second copy. Define
\[
\sigma:A_x\longrightarrow A_y,\qquad
x_i\longmapsto-\partial_{y_i},\quad
\partial_{x_i}\longmapsto y_i.                            \tag{1.1}
\]
Indeed $[y_i,-\partial_{y_j}]=\delta_{ij}$, and the other required commutators vanish. The inverse sends $y_i$ to $\partial_{x_i}$ and $\partial_{y_i}$ to $-x_i$, so this is an isomorphism.

For a left module set
\[
\mathcal F(M)=A_y\otimes_{\sigma,A_x}M.                   \tag{1.2}
\]
Transport identifies its underlying vector space with that of $M$, with actions
\[
y_i\cdot m=\partial_{x_i}m,\qquad
\partial_{y_i}\cdot m=-x_i m.                             \tag{1.3}
\]
The direction matters: these are the actions of the inverse of (1.1) on the underlying vector space. Restricting an action along (1.1) would define the opposite Fourier convention.

Transport preserves exact sequences, finite generation, and all colimits. It extends termwise to complexes. Applying (1.3) twice changes both generators to their negatives; hence the identity on underlying vectors gives a natural isomorphism
\[
\mathcal F_{y\to z}\mathcal F_{x\to y}(M)
\simeq a^*M,\qquad a(x)=-x.                              \tag{1.4}
\]
This already proves the algebraic square formula. Section 3 will also prove it directly from the kernel.

**Theorem 1.1.** Fourier transformation preserves holonomicity. More precisely, it preserves Bernstein dimension and Bernstein multiplicity.

**Proof.** Give every $x_i$ and $\partial_{x_i}$ degree one. The Bernstein piece $B_jA_x$ consists of operators of total degree at most $j$. Equation (1.1) identifies it with $B_jA_y$. If $G_\bullet M$ is a good Bernstein filtration, use the identical filtered vector space on $\mathcal F(M)$. For example, if
$G_jM=\sum_\nu B_{j-b_\nu}A_x\,m_\nu$, transport gives
$G_j\mathcal F(M)=\sum_\nu B_{j-b_\nu}A_y\,m_\nu$.
Thus it remains a good filtration, and every filtered dimension is unchanged. Its eventual Hilbert polynomial has the same degree and leading coefficient.

For a nonzero finitely generated Weyl module, the Bernstein dimension equals the dimension of its ordinary characteristic variety, as established in lesson 4. Bernstein's inequality makes this dimension at least $n$, and holonomicity means equality. It therefore holds for $M$ precisely when it holds for $\mathcal F(M)$. The zero module is preserved too. $\square$

This argument rotates the *Bernstein* graded support. It does not say that the usual order characteristic variety always rotates in $T^*\mathbb A^n$: the order filtration assigns degree zero to $x_i$ and degree one to $\partial_i$, and is not preserved by $\sigma$. Miličić's *Lectures on Algebraic Theory of D-Modules*, Chapter I, §§5–8, proves the holonomicity statement by the same filtration argument, with the Fourier convention (1.3).

### Point modules, Euler modules, and a Gaussian

On the line write $D=A_1$ and
\[
\mathcal O=D/D\partial_x,\qquad
\delta_a=D/D(x-a).
\]
For a cyclic quotient transport carries the entire left ideal to the corresponding left ideal, so
\[
\begin{aligned}
\mathcal F(\mathcal O)&=D_y/D_y y=\delta_0,\\
\mathcal F(\delta_a)&=D_y/D_y(\partial_y+a)
                    =\mathcal O e^{-ay}.                 \tag{1.5}
\end{aligned}
\]
For the second identification, move every derivative to the right using the Weyl relation and then use $(\partial_y+a)e=0$. Every class is a polynomial in $y$ times $e$. Conversely the action
$\partial_y(fe)=f'e-afe$ defines a module on $k[y]e$ with precisely this presentation. In particular $\mathcal F(\delta_0)=\mathcal O$.

Let $\theta_x=x\partial_x$ and $Q_\lambda=D/D(\theta_x-\lambda)$. Then
\[
\sigma(\theta_x-\lambda)
=-\partial_y y-\lambda
=-(y\partial_y+\lambda+1),
\]
and consequently
\[
\mathcal F(Q_\lambda)
=D_y/D_y(\partial_y y+\lambda)
=Q_{-\lambda-1}.                                        \tag{1.6}
\]
The extra $1$ comes from $\partial_y y=y\partial_y+1$. It cannot be removed by treating the generators as commuting variables. The parameter involution $\lambda\mapsto-\lambda-1$ squares to the identity, as it should: negation preserves the Euler operator.

Finally
\[
\mathcal O e^{x^2/2}=D/D(\partial_x-x).
\]
Its defining operator becomes $y+\partial_y$, whence
\[
\mathcal F(\mathcal O e^{x^2/2})
=D_y/D_y(\partial_y+y)
=\mathcal O e^{-y^2/2}.                                  \tag{1.7}
\]
The quotient identification follows by the same derivative reduction as in (1.5), now with $\partial_y(fe)=(f'-yf)e$.

**A regular module with an irregular transform.** The point module $\delta_1$ is regular holonomic: it is the closed direct image of the one-dimensional module on a point. Its transform is $\mathcal O e^{-y}$. In the coordinate $w=1/y$ at infinity its connection satisfies
\[
\partial_w e=w^{-2}e.                                    \tag{1.8}
\]
Changing a meromorphic frame multiplies it by $g\in k((w))^\times$ and changes the coefficient by $g'/g$. Writing $g=w^m u$ with $u\in k[[w]]^\times$ gives
$g'/g=m/w+u'/u$, which has no double pole. Thus no meromorphic frame makes (1.8) logarithmic. The rank-one criterion in lesson 13 proves irregularity at infinity. Algebraic regularity includes this boundary condition.

## 2. The exponential kernel on a vector bundle

Let $S$ be smooth of dimension $m$, let $E\to S$ have rank $n$, and put
\[
Z=E\times_S E^\vee,\qquad
p_1:Z\to E,\quad p_2:Z\to E^\vee,\quad
\varphi(x,y)=\langle x,y\rangle.
\]
The dimensions are $d_E=m+n$ and $d_Z=m+2n$. The exponential $\operatorname{Exp}(-\varphi)$ is $\mathcal O_Z e$ with connection
$\nabla e=-d\varphi\,e$.

For a smooth variety $V$, our tensor product is
\[
M\otimes^!N=(M\otimes_{\mathcal O_V}^{L}N)[-d_V].
\]
For a smooth map of relative dimension $r$, $f^!=f^\dagger[r]$, where $f^\dagger$ is the usual unshifted left-module pullback. These are the conventions of lessons 7–10. Define the normalized kernel and transform by
\[
\begin{aligned}
K_E&=\operatorname{Exp}(-\varphi)[d_E],\\
\mathcal F_E(M)&=p_{2,\mathrm{dR},*}
                  (p_1^!M\otimes^!K_E).                  \tag{2.1}
\end{aligned}
\]
The symbol $p_{2,\mathrm{dR},*}$ is D-module direct image, computed by the relative de Rham complex; it is not ordinary pushforward of the underlying module.

The shift inside the direct image cancels:
\[
n+d_E-d_Z=0.                                             \tag{2.2}
\]
Thus its integrand, in ordinary left-module notation, is
$p_1^\dagger M\otimes_{\mathcal O_Z}\operatorname{Exp}(-\varphi)$
in degree zero when $M$ is a module. The exponential is locally free over $\mathcal O_Z$, so its tensor has no additional derived correction. Using the unshifted exponential in (2.1) instead would give $\mathcal F_E(M)[-d_E]$. The base dimension matters in this course's absolute $\otimes^!$ convention.

**Theorem 2.1.** On a trivialized bundle, (2.1) is transport along (1.1) in the fiber Weyl algebra, with the base action unchanged. In particular it is an exact equivalence on quasi-coherent D-modules and induces an equivalence on their derived categories.

**Proof.** Work on an affine trivializing open in $S$. Because $p_2$ is affine, its direct image is the relative Spencer complex on $M[y_1,\ldots,y_n]$. It is the Koszul complex for the commuting operators
\[
T_i=D_i-y_i,\qquad D_i=\partial_{x_i}|_M,                 \tag{2.3}
\]
placed in degrees $-n,\ldots,0$. This degree convention is the one for direct images in lesson 8.

Here is an exactness argument valid for every $M$, without assuming finite generation or local freeness. On polynomials with coefficients in $M$ form
\[
U=\exp\!\left(-\sum_iD_i\partial_{y_i}\right).
\]
Each exponential series is finite on each polynomial because $\partial_{y_i}$ lowers degree. Its inverse uses the positive sign. The commutator formula gives
$Uy_iU^{-1}=y_i-D_i$, so $T_i=-Uy_iU^{-1}$. This identifies the Koszul complex (2.3), up to the harmless signs of its exterior generators, with the Koszul complex for multiplication by the $y_i$ on $M[y]$.

Multiplication by $y_1$ is injective, and its quotient is $M[y_2,\ldots,y_n]$; repeat for every remaining variable. Tensoring these one-variable complexes, or induction on their number, shows that their only cohomology is $M$ in degree zero. Therefore (2.3) has no negative cohomology either.

Its degree-zero quotient has the natural identification with $M$ given by evaluation of a polynomial $P(y)m$ at the commuting operators $D_i$:
\[
[P(y)m]\longmapsto P(D)m.                                \tag{2.4}
\]
Indeed this kills all $T_i$, and the conjugation above proves it is an isomorphism; constants represent every class. Multiplication by $y_i$ acts there by $D_i$. The output derivative acts before passing to the quotient by
$\partial_{y_i}-x_i$. It commutes with all $T_j$, since the two scalar commutators cancel. On a constant representative it acts by $-x_i$. These are exactly (1.3). In a trivialization the pairing has no base-coordinate derivative, so base differential operators retain their action on $M$. All constructions are natural in $M$.

The geometric definition (2.1) is intrinsic. Consequently these local identifications glue on changes of bundle frame, with the base differential operators transformed as part of the same connection. The exact local equivalences and their inverses therefore give the asserted equivalence globally. $\square$

For bounded complexes with holonomic cohomology, the relative transform preserves holonomicity. One can use the preservation results of lesson 11 directly: smooth inverse image, tensor with a rank-one connection, and de Rham direct image preserve holonomicity. In a vector space Theorem 1.1 gives the sharper Bernstein-filtration proof.

## 3. Computing the square from the kernel on the line

We now compute the entire convolution kernel, rather than only its action on a cyclic generator. Let $x$ and $z$ be the input and output coordinates and let $y$ be the middle coordinate. On the triple product both pulled-back kernels acquire a shift $[1]$ from smooth $!$-pullback in addition to their own $[1]$. Their $\otimes^!$ subtracts the triple-product dimension $3$. Thus the integrand for kernel composition is
\[
\operatorname{Exp}(-xy-yz)[1].
\]
This is the kernel composition formula from lesson 10, with its shifts included.

Set $w=x+z$. Integration in $y$ computes the complex
\[
R\xrightarrow{\ T=\partial_y-w\ }R,\qquad
R=k[x,w,y],                                             \tag{3.1}
\]
in degrees $-1,0$, followed by the shift $[1]$.

The map $T$ is injective. If a nonzero polynomial has highest $y$-coefficient $f_b(x,w)$, the highest coefficient of $Tf$ is $-wf_b$, which is nonzero. In its cokernel the identities
\[
[wy^b]=b[y^{b-1}]\quad(b\geq1),\qquad [w]=0             \tag{3.2}
\]
reduce every polynomial to a unique polynomial in $x,y$. To verify uniqueness, define a $k[x]$-linear reduction map by
\[
\pi(w^a y^b)=
\begin{cases}
\dfrac{b!}{(b-a)!}\,y^{b-a},&a\leq b,\\
0,&a>b.
\end{cases}                                             \tag{3.3}
\]
It annihilates $T(w^a y^b)=b w^a y^{b-1}-w^{a+1}y^b$. Conversely repeated use of this very relation, including $T(w^{a-1})=-w^a$, reduces a polynomial modulo $\operatorname{im}T$ to its image under $\pi$. Since $\pi$ is the identity on $k[x,y]$, this proves uniqueness and describes the full cokernel.

The output operators in the $(x,w)$ coordinates act by ordinary differentiation in $x$ and by $\partial_w-y$ in the normal direction. On its representative polynomials the latter acts by $-y$, while $w$ acts by $\partial_y$ through (3.2). Let
\[
i:\mathbb A^1_x\hookrightarrow\mathbb A^2_{x,w},
\qquad w=0.
\]
Kashiwara's normal-coordinate presentation of $i_*\mathcal O_x$ has generator $\delta$ killed by $w$ and freely adjoins its normal derivatives. The map
\[
\partial_w^b\delta\longmapsto(-1)^b[y^b]                 \tag{3.4}
\]
intertwines $\partial_w$, $w$, and the tangent operators:
$w\partial_w^b\delta=-b\partial_w^{b-1}\delta$, which maps to (3.2) with precisely the same sign. It is an isomorphism by the unique normal forms just proved. Hence (3.1) has cokernel $i_*\mathcal O_x$ and no other cohomology.

Returning to $(x,z)$, this is the graph $z=-x$. The normalized composition kernel is therefore
\[
K\circ K\simeq i_*\mathcal O_x[1],
\qquad i(x)=(x,-x).                                     \tag{3.5}
\]

**Theorem 3.1.** For every quasi-coherent D-module complex on the line,
$\mathcal F^2(M)\simeq a^*M$ naturally, with no shift.

**Proof.** The transform with (3.5) is
$p_{z,\mathrm{dR},*}(p_x^!M\otimes^!i_*\mathcal O_x[1])$.
Apply the closed-embedding projection formula in lesson 10 to rewrite the tensor as
\[
i_*\bigl(i^!p_x^!M\otimes^!\mathcal O_x[1]\bigr).
\]
Transitivity gives $i^!p_x^!M=M$ because $p_xi=\mathrm{id}$. On the line,
$M\otimes^!\mathcal O_x[1]=(M\otimes_{\mathcal O_x}^{L}\mathcal O_x)[-1+1]=M$.
Composing the two direct images now gives $a_{\mathrm{dR},*}M$, which is canonically $a^*M$ for the involutive isomorphism $a$. This proves the natural formula, including every shift. $\square$

For a trivial rank-$n$ bundle the computation is the tensor product of these $n$ normal-direction computations, over the base. The graph kernel is $i_*\mathcal O_E[d_E]$: the triple-product shifts give $[m+n]=[d_E]$. The same projection formula proves $\mathcal F_{E^\vee}\mathcal F_E\simeq a_E^*$. Local bundle trivializations suffice because (2.1) and the graph construction are intrinsic.

## 4. The monodromic comparison

For a Weyl module on $V=\mathbb A^n$ put
$\theta=\sum_i x_i\partial_{x_i}$. Call it **monodromic** when $\theta$ acts locally finitely: each vector lies in a finite-dimensional $\theta$-stable subspace. This permits arbitrary eigenvalues and generalized eigenvectors; it is weaker than an algebraic strong $\mathbb G_m$-linearization.

Transport gives
\[
\sigma(\theta_x)=-\theta_y-n.                            \tag{4.1}
\]
Local finiteness is therefore preserved. The modules $Q_\lambda$ illustrate this for every $\lambda$, including resonant integral values. Their generator has Euler eigenvalue $\lambda$, and pure powers $x^j u$, $\partial_x^j u$ have eigenvalues $\lambda+j$, $\lambda-j$. Moving mixed powers into this span with the relation $\theta u=\lambda u$ shows that every vector has a finite Euler orbit. These modules are regular by their Kummer connections and the regular extensions discussed in lessons 6 and 13.

For topological sheaves on a complex vector space, monodromicity means that cohomology sheaves are locally constant on the $\mathbb C^\times$-orbits. Such a sheaf is also conic for positive real scaling. Use the underlying real pairing
$\operatorname{Re}\langle x,y\rangle$ and define
\[
\begin{aligned}
T_-(F)&=Rq_!\bigl(p^{-1}F\otimes
       \mathbb C_{\{\operatorname{Re}\langle x,y\rangle\leq0\}}\bigr),\\
T_+(F)&=Rq_!\bigl(p^{-1}F\otimes
       \mathbb C_{\{\operatorname{Re}\langle x,y\rangle\geq0\}}\bigr).
\end{aligned}                                            \tag{4.2}
\]
The constant sheaves on these closed sets are extended by zero; $q_!$ is proper-support sheaf image. Changing $y$ to $-y$ identifies $T_+$ with $a_{V^\vee}^*T_-$. The SH-02 lesson linked above uses $T_-$. Real rank is $2n$, whereas the perverse normalization below uses complex rank $n$.

**Theorem 4.1 (Brylinski; stated).** If $M$ is a regular holonomic monodromic algebraic D-module on a complex vector space $V$ of dimension $n$, then $\mathcal F(M)$ is again regular holonomic and monodromic. With the perverse-normalized de Rham functor of lesson 12,
\[
\operatorname{DR}_{V^\vee}\mathcal F(M)
\simeq T_+\bigl(\operatorname{DR}_V M\bigr)[n].            \tag{4.3}
\]
This extends to bounded derived complexes with such cohomology. The normalized transform on the right preserves monodromic perverse sheaves.

The precise source is Brylinski, *Transformations canoniques…*, Proposition 7.12 and Theorem 7.24, with Corollary 7.23 for perversity. His Definition 7.16 transports $x_i$ to $\partial_{y_i}$ and $\partial_{x_i}$ to $-y_i$, the inverse of (1.1), and his topological transform uses the negative halfspace. Postcomposing both sides by negation gives exactly (4.3). His §6, following Proposition 6.13, inserts the complex-rank shift $[n]$.

The normalization has concrete checks:
$T_-(\mathbb C_V)=\mathbb C_{\{0\}}[-2n]$ and
$T_-(\mathbb C_{\{0\}})=\mathbb C_{V^\vee}$, and the same formulas hold for $T_+$. Hence (4.3) sends
$\operatorname{DR}(\mathcal O_V)=\mathbb C_V[n]$
to $\mathbb C_{\{0\}}$, and sends the point module to $\mathbb C_{V^\vee}[n]$. The sheaf square has real-rank shift $[-2n]$; applying the normalization twice cancels it, consistently with Theorem 3.1. These sheaf identities and inversion are part of the Fourier-Sato theory in SH-02.

Equation (1.8) explains why the regularity hypothesis alone is insufficient. Indeed $\mathcal O e^{-y}$ is not monodromic: the vectors $\theta^j e$ have polynomial coefficients with successively increasing degree and nonzero leading coefficient. Fourier-Sato comparison for ordinary constructible sheaves cannot be applied to this example by omitting monodromicity. Theorem 4.1 is not a consequence of moving an arbitrary irregular exponential kernel through the regular Riemann-Hilbert correspondence.

## 5. Flat line bundles as the abelian spectral space

Let $A$ be an abelian variety of dimension $g$ in characteristic zero, and let
$\widehat A=\operatorname{Pic}^0(A)$ be its dual. Denote by $A_{\mathrm{conn}}$ the moduli scheme of degree-zero line bundles with integrable connection **on $A$**, rigidified at its identity. This rigidification removes their scalar automorphisms and supplies a universal line bundle. There is an exact sequence of algebraic groups
\[
0\longrightarrow H^0(A,\Omega_A^1)_{\mathrm{add}}
\longrightarrow A_{\mathrm{conn}}
\longrightarrow\widehat A
\longrightarrow0.                                       \tag{5.1}
\]
It is the universal vector extension of $\widehat A$, and is smooth of dimension $2g$. These facts are stated here with Laumon, Theorems 2.1.2 and 2.2.1. For a fixed line bundle, its connections form an affine space under invariant one-forms; there is no canonical origin for that space in general. The fiber over the trivial bundle does have the origin $d$.

Some authors write $A^\natural$ for $A_{\mathrm{conn}}$; others attach the superscript to the abelian variety being extended, and write $\widehat A^\natural$ for the same space. Definition (5.1), rather than the superscript alone, specifies our meaning. For D-modules on $A$ it is flat lines on $A$, not flat lines on $\widehat A$, that form this spectral space.

Let $\mathcal P^\nabla$ be the universal rigidified line bundle on
$A\times A_{\mathrm{conn}}$, with its connection in the $A$ directions. Write $p$ and $q$ for the projections to $A$ and $A_{\mathrm{conn}}$. Define
\[
\begin{aligned}
F_A(M)&=Rq_*
  \operatorname{DR}_{/A_{\mathrm{conn}}}
       (\mathcal P^\nabla\otimes^L Lp^*M),\\
G_A(N)&=Rp_*(\mathcal P^\nabla\otimes^L Lq^*N).            \tag{5.2}
\end{aligned}
\]
The relative de Rham complex in the first line has terms
$[\mathcal P^\nabla\otimes Lp^*M\to\Omega^1_{/A_{\mathrm{conn}}}\otimes
\mathcal P^\nabla\otimes Lp^*M\to\cdots]$
in degrees $-g,\ldots,0$. The second line uses ordinary derived quasi-coherent image and retains the partial D-action in the $A$ directions. There is no relative de Rham operation in the parameter directions in that line.

**Theorem 5.1 (Laumon–Rothstein; stated).** The functors (5.2) give equivalences of bounded derived quasi-coherent categories and preserve the bounded coherent subcategories. Their compositions are
\[
\begin{aligned}
G_AF_A&\simeq a_A^*[-g],\\
F_AG_A&\simeq a_{\mathrm{conn}}^*[-g],                    \tag{5.3}
\end{aligned}
\]
where the two $a$'s are inversion in the respective groups. In particular $F_A$ has inverse $a_A^*G_A[g]$.

The confirmed locator for these formulas is Laumon, *Transformation de Fourier généralisée*, §3.1 and Theorem 3.2.1, with Corollaries 3.1.3 and 3.2.5 for coherence. Rothstein's *Sheaves with connection on abelian varieties* is the independent original construction. This is a derived equivalence; it does not identify the ordinary module hearts as abelian categories.

It is useful to renormalize the first line:
\[
\widehat F_A=a_{\mathrm{conn}}^*F_A[g].
\]
Universality of $\mathcal P^\nabla$ gives
$G_Aa_{\mathrm{conn}}^*\simeq a_A^*G_A$: inversion of a flat line is its dual, also obtained by pullback along inversion of $A$. Together with (5.3) this makes $\widehat F_A$ inverse to $G_A$.

For a point $\ell=(L,\nabla)$, the pullback of its skyscraper to the product and tensor with $\mathcal P^\nabla$ restricts to $(L,\nabla)$ on $A\times\{\ell\}$. Its ordinary pushforward to $A$ is that same flat line, with no higher image or shift. Thus, as a consequence of the stated equivalence,
\[
G_A(k_\ell)=(L,\nabla),\qquad
\widehat F_A(L,\nabla)=k_\ell.                            \tag{5.4}
\]
In the unrenormalized convention $F_A(L,\nabla)=k_{\ell^{-1}}[-g]$. The shift in (5.4) differs from (5.3) because the functor itself has been renormalized.

### An explicit family of commuting equations

Put $V=\operatorname{Lie}(A)$ and
$B=\operatorname{Sym}_k V=k[V^*]$. Translation trivializes $T_A$ by commuting invariant vector fields. Choose a basis $v_1,\ldots,v_g$. Their ordered monomials give, by the PBW theorem, a global isomorphism
\[
\mathcal D_A\simeq\mathcal O_A\otimes_k B
\quad\text{as a right }B\text{-module}.                  \tag{5.5}
\]
To see surjectivity, subtract the highest-order symbol of a differential operator using these monomials and induct on order; injectivity follows from independence of their symbols. Since $\Gamma(A,\mathcal O_A)=k$, taking global sections in this direct-sum decomposition gives
\[
\Gamma(A,\mathcal D_A)=B.                                \tag{5.6}
\]
Global sections here commute with direct sums of these quasi-coherent summands, as $A$ is quasi-compact and separated. Thus no additional global differential operators are missing.

For any $B$-module $N$ form
\[
M_N=\mathcal D_A\otimes_B N
    \simeq\mathcal O_A\otimes_k N.
\]
This tensor is exact by the right-$B$ freeness in (5.5). The action is explicitly
\[
v(f\otimes n)=v(f)\otimes n+f\otimes vn.                  \tag{5.7}
\]
Indeed $vf=fv+v(f)$ in $\mathcal D_A$, and its commuting invariant vector fields give an integrable connection. The formula extends to bounded complexes.

For the character $k_\lambda$ at $\lambda\in V^*$ this is the flat line on the trivial bundle with connection $d+\alpha_\lambda$, where $\alpha_\lambda(v)=\lambda(v)$. Equivalently,
\[
M_{k_\lambda}
=\mathcal D_A\Big/\sum_i
       \mathcal D_A(v_i-\lambda(v_i)).                   \tag{5.8}
\]
On a simply connected analytic coordinate chart its horizontal coefficient is
$\exp(-\sum_i\lambda(v_i)t_i)$. The minus sign is the distinction between the action on the chosen frame and the equation for its horizontal coefficient.

Identify $V^*=H^0(A,\Omega_A^1)$ with the fiber over the trivial line in (5.1), and let $j:V^*\hookrightarrow A_{\mathrm{conn}}$ be its inclusion. The universal connection restricted to $A\times V^*$ is exactly (5.7), with the coordinate functions on $V^*$ acting on $N$. The projection $A\times V^*\to A$ is affine, so its ordinary derived image has no higher terms on quasi-coherent sheaves. We have therefore proved directly that
\[
G_A(j_*\widetilde N)=M_N.
\]
Applying the stated equivalence gives the entire family, not only its closed points:
\[
\widehat F_A(M_N)\simeq j_*\widetilde N.                   \tag{5.9}
\]
Here $\widetilde N$ is the quasi-coherent sheaf on the affine space $V^*$. In particular a finitely generated $B$-module gives a coherent D-module and a coherent spectral sheaf.

For $A=\operatorname{Jac}(X)$, the tangent space is
$H^1(X,\mathcal O_X)$ and its dual is $H^0(X,\Omega_X^1)$ by Serre duality. Thus (5.7)–(5.9) give the concrete family discussed in Frenkel, §§4.4–4.5: a one-form specifies scalar eigenvalues for the invariant vector fields. Arbitrary coherent spectral sheaves need not have finite support. The point correspondence (5.4) is not a claim that finite sums and cones of skyscrapers generate every coherent sheaf.

### Two appearances in geometric Langlands

The Jacobian version is the finite-dimensional Fourier–Mukai–Laumon ingredient in the abelian geometric Langlands correspondence. Arinkin–Gaitsgory, §11.2, places it beside the degree component and the derived stabilizer factors of the Picard stack; their statement uses the presentable DG categories. The calculation for $B\mathbb G_m$ and for the discrete degree set in lesson 17 supplies those other factors. They are not part of the ordinary scheme $A_{\mathrm{conn}}$ and cannot be discarded by restricting to degree-zero line bundles.

There is also an infinite-dimensional Weyl construction in Hilburn–Raskin, *Tate's thesis in the de Rham setting*. Their §4 builds the required $\operatorname{IndCoh}^*$ categories, and §5.1 constructs compact objects $\mathcal F_n$ from the scheme of a flat line together with a horizontal section of bounded pole order. They carry actions of the opposite finite Weyl algebras; the commutator is the negative residue pairing. Section 7.1 states full faithfulness of the associated finite-stage functor. These are stated inputs here, discussed further in lesson 17. The use of an opposite algebra changes the commutator sign, so it must be translated before comparing it with $[\partial,x]=1$ in (1.1).

The three constructions have different spaces of parameters: linear dual coordinates for (2.1), flat line bundles for (5.2), and formal local-system/section data for Hilburn–Raskin. The explicit point and Gaussian calculations do not by themselves prove the latter two equivalences.

## 6. Exercises with complete solutions

**Exercise 18.1 (easy).** Compute $\mathcal F(\mathcal O)$, $\mathcal F(\delta_0)$, and $\mathcal F(\delta_a)$ with the fixed sign.

**Solution.** Apply $\sigma$ to the defining left ideals. The ideal $D\partial_x$ becomes $D_y y$, giving $\delta_0$. The ideal $Dx$ becomes $D_y(-\partial_y)=D_y\partial_y$, giving $\mathcal O$. Finally $D(x-a)$ becomes $D_y(-\partial_y-a)$, giving the quotient by $\partial_y+a$. It is the free $k[y]$-module on $e$ with $\partial_y(fe)=(f'-af)e$, namely $\mathcal O e^{-ay}$. None of these transports changes degree. Applying the transform twice sends $\delta_a$ to $\delta_{-a}$, agreeing with negation.

**Exercise 18.2 (easy).** Exhibit a regular holonomic module whose transform is irregular, and prove the irregularity.

**Solution.** Take $\delta_1$. Closed direct image from a point preserves regular holonomicity, so it is regular. Exercise 18.1 gives its transform $\mathcal O e^{-y}$. At infinity $\partial_w e=w^{-2}e$. A meromorphic frame change adds $g'/g$, and for $g=w^m u$ this is $m/w+u'/u$, with $u'/u$ regular. The double pole survives every such change; hence there is no logarithmic lattice in rank one. By the boundary criterion of lesson 13 the transform is irregular. This does not contradict preservation of holonomicity in Theorem 1.1.

**Exercise 18.3 (medium).** Compute $\mathcal F(D/D(x\partial_x-\lambda))$ and check the parameter after a second transform.

**Solution.** The image of the operator is
$-\partial_y y-\lambda$. Multiplication by the nonzero scalar $-1$ does not change its generated left ideal. Thus the quotient is
$D_y/D_y(\partial_y y+\lambda)
=D_y/D_y(y\partial_y+\lambda+1)$.
Its Euler parameter is $-\lambda-1$, for every $\lambda$; no nonresonance assumption was used. Applying the same rule again gives
$-(-\lambda-1)-1=\lambda$. Negation fixes $x\partial_x$, so this is also the answer dictated by the square formula.

**Exercise 18.4 (medium).** Prove preservation of holonomicity for finitely generated $A_n$-modules using a good filtration. Explain why an order-filtration argument would be invalid.

**Solution.** Use the total-degree Bernstein filtration $B_\bullet A_n$. The images of its degree-one generators under $\sigma$ again have degree one, and the inverse has the same property, so $\sigma(B_j)=B_j$. Transport a good filtration with its chosen finite generators and their filtration shifts. Every vector-space piece, and therefore its Hilbert polynomial, is identical before and after transport. Lesson 4 identifies its degree with the characteristic dimension. Thus the degree equals $n$ before transport exactly when it equals $n$ afterward, proving holonomicity in both directions; the zero case is immediate. The order filtration is not preserved because $x$ has order zero while $\sigma(x)=-\partial_y$ has order one. It cannot be substituted in this proof.

**Exercise 18.5 (hard).** Prove the square formula on $\mathbb A^1$ from the exponential kernel, including the natural isomorphism and the shift.

**Solution.** Each kernel is $\operatorname{Exp}(-xy)[1]$. Pulling the two kernels to the triple product contributes two further shifts $[1]$, and its $\otimes^!$ contributes $[-3]$. Their composition is therefore middle-variable direct image of $\operatorname{Exp}(-y(x+z))[1]$.

Put $w=x+z$. The relative direct image is the two-term complex (3.1), followed by $[1]$. Its kernel vanishes by the highest-$y$-coefficient test. Relations (3.2) reduce its cokernel to $k[x,y]$, and the explicit map (3.3) proves these representatives are unique: it kills the differential, and reduction changes a polynomial only by its image. The output normal operator is $-y$, with $w$ acting by $\partial_y$. Map the normal derivatives of the delta generator to $(-1)^b y^b$ as in (3.4). This identifies the full output D-module with $i_*\mathcal O_x$ on the graph $z=-x$. Hence the composition kernel is (3.5), with shift $[1]$.

For an arbitrary $M$, the closed projection formula identifies its transform with
$p_{z,\mathrm{dR},*}i_*(i^!p_x^!M\otimes^!\mathcal O_x[1])$.
The first argument is $M$ by transitivity; the tensor is $M[-1+1]=M$. The composition of direct images is $a_{\mathrm{dR},*}M=a^*M$. Every identification used a natural kernel map or a functorial projection formula, so this proves a natural isomorphism on the whole category and on complexes, with no residual shift.

## What this lesson does not prove

The Riemann-Hilbert comparison with Fourier-Sato, including regularity preservation in the monodromic case and perverse exactness, is Theorem 4.1 stated with Brylinski's exact locators. The conic sheaf-transform inversion and its normalization are developed in SH-02.

The representability and universal-extension assertions (5.1), and the full Laumon–Rothstein equivalence (5.3), are stated with Laumon's Theorems 2.1.2, 2.2.1, and 3.2.1 and the coherence corollaries. The point and commuting-vector-field calculations are proved here relative to that stated equivalence; they are not a proof of its essential surjectivity. The presentable DG Picard-stack comparison in Arinkin–Gaitsgory, §11.2, and the Hilburn–Raskin §5/§7 spectral construction are likewise stated external inputs.

The proofs of Bernstein dimension equals characteristic dimension, Kashiwara's equivalence, and the functor composition/projection formulas are earlier course results. This lesson proves the Weyl transport, its holonomicity preservation, its agreement with the normalized vector-bundle kernel, the full line-kernel square, the examples, and all five exercise solutions.

## References

Miličić, [*Lectures on Algebraic Theory of D-Modules*](https://www.math.utah.edu/~milicic/Eprints/dmodules.pdf), Chapter I, §§5–8: the Fourier automorphism of the Weyl algebra and the Bernstein filtration, the equality of Bernstein dimension and characteristic dimension, and preservation of holonomicity under Fourier transformation.

Brylinski, [*Transformations canoniques, dualité projective, théorie de Lefschetz, transformations de Fourier et sommes trigonométriques*](https://www.numdam.org/item/AST_1986__140-141__3_0/), Astérisque 140–141 (1986), 3–134: §6 normalization, Definition 7.16, Proposition 7.12, Corollary 7.23, and Theorem 7.24.

Laumon, [*Transformation de Fourier généralisée*](https://arxiv.org/abs/alg-geom/9603004): Theorems 2.1.2 and 2.2.1, §3.1, Theorem 3.2.1, Corollaries 3.1.3 and 3.2.5.

Rothstein, [*Sheaves with connection on abelian varieties*](https://arxiv.org/abs/alg-geom/9602023), Duke Mathematical Journal 84 (1996), 565–598: independent original abelian construction.

Frenkel, [*Lectures on the Langlands program and conformal field theory*](https://arxiv.org/abs/hep-th/0512172), §§4.4–4.5: the Jacobian example and its commuting differential operators.

Arinkin and Gaitsgory, [*Singular support of coherent sheaves, and the geometric Langlands conjecture*](https://arxiv.org/abs/1201.6343), §11.2: the torus/Picard-stack comparison.

Hilburn and Raskin, [*Tate's thesis in the de Rham setting*](https://arxiv.org/abs/2107.11325), §4, §5.1, and §7.1: the categories, opposite-Weyl action, and full-faithfulness statement for the local spectral construction.
