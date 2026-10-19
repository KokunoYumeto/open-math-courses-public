# Tangent spaces and obstructions for Hilbert and Quot schemes

*Written by GPT-6.1 Sol (OpenAI) (Codex), October 2026. Public domain (CC0).*

A quotient can change infinitesimally even when its source stays fixed. Its kernel records that change: moving a relation produces an element of the quotient. This gives the tangent space of Quot. Over a thicker base, the same relations may fail to fit together, and that failure is an extension class.

We construct the class and prove its exact lifting criterion. For a regular embedding, equations lift locally, so the remaining obstruction is the failure of the local lifts to agree. That failure lies in the first cohomology of the normal bundle. We then turn this obstruction space into a bound on the number of local equations of the Hilbert scheme. Applications distinguish a possible obstruction space from an obstruction that actually occurs: a line on a smooth quartic surface has a nonzero obstruction space and still gives a reduced isolated point. For a smooth cubic surface, a separate intersection calculation counts its 27 lines. Finite algebras and explicit degenerations then prove smoothness and irreducibility of every Hilbert scheme of points on a smooth surface. A contrasting cubic-surface construction gives a generically nonreduced component: we prove both its dimension bound and its persistent extra tangent direction.

We use the representing schemes constructed in *Hilbert and Quot schemes*, the deformation conventions in *Formal moduli and Schlessinger's theorem*, and the affine-cover cohomology methods of *Deformations of rings and schemes and the naive cotangent complex*. Coherent Ext means Ext in the category of sheaves of modules, not just the sections of sheaf Ext. This distinction matters in the obstruction calculation.

## 1 A tangent vector moves the kernel

Let \(X\) be quasi-projective of finite type over a field \(k\), let \(E\) be coherent, and fix a quotient with proper support

\[
0\longrightarrow K\longrightarrow E\xrightarrow{q}G\longrightarrow0.
\tag{1.1}
\]

Write \(D=k[\epsilon]/(\epsilon^2)\). The tangent space at this point of the fixed-polynomial Quot scheme consists of quotients of \(E_D\) flat over \(D\) whose reduction is (1.1). Two quotients are the same when their kernels agree. The identification of their reductions with \(G\) is then unique, because they are quotients of the same source.

**Proposition 1.1.** There is a canonical \(k\)-linear isomorphism

\[
T_{[q]}\operatorname{Quot}_{E/X/k}
\simeq\operatorname{Hom}_X(K,G).
\tag{1.2}
\]

**Proof.** Identify \(E_D=E\oplus\epsilon E\). For \(\phi:K\to G\), define the subsheaf

\[
\begin{gathered}
K_\phi=\\
\left\{\begin{gathered}\,k+\epsilon e:k\in K,\ e\in E,\ \\
q(e)=\phi(k)\,\end{gathered}\right\}.
\end{gathered}
\tag{1.3}
\]

The formula denotes a fibre product of sheaves, so local representatives need not be chosen globally. It is an \(\mathcal O_{X_D}\)-submodule: multiplication by \(a+\epsilon b\) replaces the pair by \(ak,\ ae+bk\), and \(q(ae+bk)=a\phi(k)\). Its reduction is \(K\), and

\[
K_\phi\cap\epsilon E=\epsilon K.
\]

Consequently \(G_\phi=E_D/K_\phi\) reduces to \(G\), and multiplication by \(\epsilon\) identifies its image with \(G\); its kernel is the same image. This is the dual-number flatness criterion proved in the preceding lesson. Thus \(G_\phi\) is flat and gives a tangent vector. The zero map gives the constant quotient.

Conversely let \(K'\) be the kernel of a flat deformation. Tensoring its defining exact sequence with \(k\) is exact, because the quotient is flat, so \(K'/\epsilon K'=K\). Also \(K'\cap\epsilon E=\epsilon K\). For a local lift \(k+\epsilon e\in K'\) of a section \(k\), the class \(q(e)\) is independent of the lift: changing it changes \(e\) by a section of \(K\). It defines an \(\mathcal O_X\)-linear map \(\phi:K\to G\). Formula (1.3) recovers the kernel, giving inverse constructions.

To check linearity, replace \(k\epsilon\) by an arbitrary square-zero vector space \(M\). The same formula identifies the deformations with \(\operatorname{Hom}_X(K,G\otimes_k M)\), functorially in \(M\). The maps \(M=k\oplus k\to k\) given by addition and by scalar multiplication induce respectively the usual addition and scalar multiplication of homomorphisms. These are the tangent-space operations. \(\square\)

Finite presentation and the proper support condition hold for these deformations: the source and kernels are coherent on the Noetherian \(X_D\), and properness of the support persists through the nilpotent thickening [Stacks, Tag 0BPG]. Their fibre polynomial is the prescribed one, since the Artinian base has a single fibre.

For a closed subscheme \(Z\subset X\), apply the proposition to \(E=\mathcal O_X\), \(K=\mathcal I_Z\), \(G=\mathcal O_Z\). A map \(\mathcal I_Z\to\mathcal O_Z\) kills \(\mathcal I_Z^2\), because every local section of the ideal acts as zero on the target. Define

\[
\mathcal N_{Z/X}
=\mathcal Hom_{\mathcal O_Z}
(\mathcal I_Z/\mathcal I_Z^2,\mathcal O_Z).
\]

We obtain

\[
\begin{gathered}
T_{[Z]}\operatorname{Hilb}_{X/k}\\
=\operatorname{Hom}_X(\mathcal I_Z,\mathcal O_Z)\\
=H^0(Z,\mathcal N_{Z/X}).
\end{gathered}
\tag{1.4}
\]

The last formula holds for every closed subscheme. For a **regular embedding**, the conormal sheaf is finite locally free and \(\mathcal N_{Z/X}\) is the normal bundle. Without regularity it is a normal sheaf, and the local lifting argument in Section 3 need not hold.

Here is the relative tangent formula once, in a form that fixes its scope. If a \(T\)-point \(g\) of a represented relative Quot functor has kernel \(K\) and quotient \(G\), and \(M\) is quasi-coherent on \(T\), split thickenings \(T[M]\) give

\[
\begin{gathered}
\operatorname{Hom}_T(g^*\Omega_{\operatorname{Quot}/S},M)\\
=\operatorname{Hom}_{X_T}(K,G\otimes_T M).
\end{gathered}
\tag{1.5}
\]

The kernel construction above applies with \(\epsilon E\) replaced by \(E\otimes_T M\). Its exactness uses flatness of \(G/T\), which makes \(K\otimes_T M\to E\otimes_T M\) injective. The square-zero flatness criterion then gives a flat quotient over \(T[M]\). Universal derivations identify the other side with the same split lifts. This proves (1.5); it requires no flatness assumption on the coherent source for this split calculation.

## 2 The obstruction extension

Let

\[
0\longrightarrow J\longrightarrow A'\longrightarrow A\longrightarrow0
\tag{2.1}
\]

be a small extension of local Artinian \(k\)-algebras with residue field \(k\): \(\mathfrak m_{A'}J=0\). Allow \(J\) to have any finite \(k\)-dimension. A one-dimensional kernel is a special case. On \(X_A\), let

\[
0\longrightarrow K_A\longrightarrow E_A\longrightarrow G_A\longrightarrow0
\tag{2.2}
\]

be a flat quotient reducing to (1.1). Both \(E_A\) and \(K_A\) are flat over \(A\): the first is a pullback from the field, and the kernel of a surjection between flat modules with flat quotient is flat.

Reduction \(\pi:E_{A'}\to E_A\) has kernel \(E\otimes_k J\). Let \(\widetilde K=\pi^{-1}(K_A)\). The submodule \(K\otimes_k J\) injects into \(E\otimes_k J\), and put

\[
C=\widetilde K/(K\otimes_k J).
\]

Multiplication by \(J\) kills \(C\): for a section reducing to \(k_A\in K_A\), its \(J\)-multiple belongs to \(K_A\otimes_A J=K\otimes_k J\). Hence \(C\) is an \(\mathcal O_{X_A}\)-module. The reduction map gives an exact sequence

\[
0\longrightarrow G\otimes_k J
\longrightarrow C\longrightarrow K_A\longrightarrow0.
\tag{2.3}
\]

**Theorem 2.1.** The class of (2.3) is a canonical obstruction

\[
\begin{gathered}
o(G_A,A')\in\\

\operatorname{Ext}^1_{X_A}(K_A,G\otimes_k J)\\
=\operatorname{Ext}^1_X(K,G)\otimes_k J.
\end{gathered}
\tag{2.4}
\]

It vanishes if and only if a flat quotient lift over \(A'\) exists. If it vanishes, the set of lifts is a torsor under

\[
\operatorname{Hom}_X(K,G)\otimes_k J.
\tag{2.5}
\]

The construction commutes with homomorphisms of small extensions and with linear maps of their kernels.

**Proof.** Suppose (2.3) has a splitting \(s:K_A\to C\). Let \(K'\subset\widetilde K\subset E_{A'}\) be the inverse image of \(s(K_A)\). It is an \(\mathcal O_{X_{A'}}\)-submodule, since \(C\) is an \(\mathcal O_{X_A}\)-module. It satisfies

\[
\begin{gathered}
K'\cap(E\otimes_k J)=K\otimes_k J,\\
\qquad
K'\longrightarrow K_A\text{ is surjective}.
\end{gathered}
\tag{2.6}
\]

The quotient \(G'=E_{A'}/K'\) therefore reduces to \(G_A\), and its \(J\)-multiple is canonically \(G\otimes_k J\). In particular the canonical multiplication map

\[
J\otimes_A G_A\longrightarrow G'
\]

is injective onto \(JG'\). Since \(G_A\) is flat over \(A\), the square-zero flatness criterion [Stacks, Tag 08MQ] says that \(G'\) is flat over \(A'\). Thus a splitting supplies a lift.

Conversely, suppose \(G'\) is a flat quotient lift, with kernel \(K'\). Flatness gives \(K'\otimes_{A'}A=K_A\). The exact kernel computation after multiplying by \(J\) gives (2.6). Consequently the image of \(K'\) in \(C\) maps isomorphically to \(K_A\), and is the image of a splitting of (2.3). The two constructions are inverse. This proves the vanishing criterion, including its necessity.

Splittings of an extension form a torsor under \(\operatorname{Hom}_{X_A}(K_A,G\otimes_k J)\): subtracting two splittings is exactly a map into the kernel of (2.3), and adding such a map gives another splitting. No nontrivial automorphism of a quotient fixes its source map, so there is no further quotient of this torsor.

For completeness, the Ext identifications in (2.4) do not assert that \(K\) is locally free. Resolve the coherent \(K_A\) on the quasi-projective \(X_A\) by finite sums of sufficiently negative powers of an ample line bundle. Such surjections exist by ample generation, also on a quasi-projective scheme. The resolution can continue to the left indefinitely. Each successive kernel is \(A\)-flat, by exactness and flatness of the preceding terms. Reduction to \(k\) remains exact and gives a resolution of \(K\). Compute sheaf Hom followed by the finite affine-cover cohomology complex. Since the target \(G\otimes_k J\) is annihilated by \(\mathfrak m_A\), this complex is exactly the reduced resolution's Hom complex on \(X\), tensored with the finite vector space \(J\). It computes both Ext groups and proves their identification. The same argument in degree zero proves (2.5).

All operations defining (2.3) are inverse image, quotient, and the canonical multiplication maps in the flat exact sequences. A map of extensions carries these sequences to each other and pushes out the kernel by the induced map on \(J\). It therefore carries the extension class to the corresponding obstruction class. Equivalently, use local presentations of (2.3): its additive transition terms are pushed forward by that linear map. This proves the stated naturality. \(\square\)

The Hom and Ext groups in degrees zero and one are finite-dimensional. In the resolution just used, each Hom sheaf is a finite sum of twists of \(G\), supported on its proper scheme-theoretic support. Its coherent cohomology is finite-dimensional [Stacks, Tag 02O6]. The first two total cohomology groups of the resulting first-quadrant double complex involve only finitely many such cohomology groups, and are therefore finite-dimensional.

The same extension proof works for a relative quotient when the prescribed source on \(X_{A'}\) is flat over \(A'\). For relative Hilbert schemes this holds when \(X/S\) is flat. A nonflat relative source can have additional lifting failures; one cannot apply the nonsplit obstruction formula by silently dropping this hypothesis.

This theorem includes local failures. The group \(\operatorname{Ext}^1_X(K,G)\) is generally larger than \(H^1(X,\mathcal Hom(K,G))\), because an extension can be nonsplit on an affine open. If local quotient lifts are known to exist, only their gluing failure remains. We isolate that case next.

## 3 A regular embedding lifts locally

Let \(X\) be smooth and quasi-projective over \(k\), and let \(Z\subset X\) be a proper closed subscheme that is a regular embedding. Write \(N=\mathcal N_{Z/X}\). We consider flat embedded deformations \(Z_A\subset X_A\), with the ambient scheme fixed.

**Lemma 3.1.** Every such deformation lifts locally on \(X\) across every small extension (2.1).

**Proof.** On an affine neighbourhood of a point of \(Z\), its ideal is generated by a regular sequence \(f_1,\ldots,f_c\). Write the ambient coordinate algebra as \(B\), and the ideal of \(Z_A\) as \(I_A\subset B\otimes_k A\). The exact ideal sequence and flatness of its quotient show that \(I_A\) is \(A\)-flat and that its reduction is the ideal of \(Z\). Lift the \(f_i\) to generators \(f_{i,A}\in I_A\). They generate \(I_A\): their cokernel is coherent, zero modulo the nilpotent \(\mathfrak m_A\), and hence zero by the nilpotent form of Nakayama's lemma.

Lift those elements to \(f_{i,A'}\in B\otimes_k A'\). Their common quotient is flat over \(A'\). Indeed, cutting a flat finitely presented algebra by lifts of a regular sequence in its special fibre gives a flat algebra [Stacks, Tag 0CEQ], applied with nilpotent ideal \(\mathfrak m_{A'}\); the special-fibre quotient is automatically flat over \(k\). Reduction to \(A\) gives precisely the equations \(f_{i,A}\), so this is the desired local lift. Away from \(Z\) the empty closed subscheme is its unique local lift. \(\square\)

Choose an affine cover \(U_i\) of \(X\) and local lifts over it. The difference of two lifts on \(U_i\cap U_j\) is, by the splitting-torsor construction of Theorem 2.1, a section

\[
\alpha_{ij}\in
\mathcal Hom_X(\mathcal I_Z,\mathcal O_Z)
(U_i\cap U_j)\otimes_k J.
\]

This Hom sheaf is the pushforward of \(N\). Differences add, so
\(\alpha_{ij}+\alpha_{jk}=\alpha_{ik}\). Changing the chosen lift on \(U_i\) by a section \(\beta_i\) changes this cocycle by \(\beta_j-\beta_i\), with a fixed choice of sign for differences. Thus its class is canonical:

\[
c(Z_A,A')\in H^1(Z,N)\otimes_k J.
\tag{3.1}
\]

Intersections of the affine opens are affine since \(X\) is separated. Their intersections with \(Z\) are affine as well. Consequently Čech cohomology here is sheaf cohomology [Stacks, Tag 01XD]. Refinement does not change the class.

### Detecting smoothness by local Artinian tests

**Lemma 3.A (the pointwise lifting criterion).** Let \(X\to S\) be locally of finite type, with \(S\) locally Noetherian, and let \(x\in X\). It is smooth at \(x\) if and only if every diagram centred at \(x\), with test rings local Artinian \(S\)-algebras and a small surjection between them, admits a lift. The residue field in the tests may be \(\kappa(x)\); no separability assumption on \(\kappa(x)/\kappa(s)\) is needed.

**Proof.** Work over an affine neighbourhood \(\operatorname{Spec}R\) of \(s\), and present a neighbourhood of \(x\) as
\[
\operatorname{Spec}(R[t_1,\ldots,t_N]/I).
\]
Let \(\mathfrak q\) be the prime of the polynomial ring corresponding to \(x\), and put \(P=R[t_1,\ldots,t_N]_{\mathfrak q}\), with maximal ideal \(\mathfrak n\) and residue field \(K=\kappa(x)\). Write \(I\) also for its extension to \(P\). Both \(P\) and \(I\) are Noetherian. Artin–Rees gives, for sufficiently large \(n\),
\[
I\cap\mathfrak n^n\subset\mathfrak n I.
\]
Consequently the local Artinian surjection
\[
\begin{gathered}
A'=P/(\mathfrak n I+\mathfrak n^n)
\longrightarrow A=P/(I+\mathfrak n^n)
\end{gathered}
\]
has kernel canonically \(J=I/\mathfrak n I\), annihilated by the maximal ideal of \(A'\). The natural map \(P/I\to A\) is a test centred at \(x\).

Assume the lifting property and lift that map to \(P/I\to A'\). Compare its composite \(v:P\to A'\) with the natural map \(u:P\to A'\). They agree modulo \(J\); their difference \(v-u\) is an \(R\)-derivation with values in \(J\), because \(J^2=0\). Since \(\mathfrak n J=0\), it factors through
\[
\Omega_{P/R}\otimes_P K\longrightarrow I/\mathfrak n I.
\]
On an element \(f\in I\), its value is \(-[f]\). Hence the differential map
\[
I/\mathfrak n I
\longrightarrow\Omega_{P/R}\otimes_P K
\]
has a left inverse, up to this harmless minus sign. In particular it is injective.

Choose \(f_1,\ldots,f_c\in I\) lifting a basis of \(I/\mathfrak n I\). Nakayama says that they generate \(I\), and their differentials are linearly independent in the free \(K\)-module on \(dt_1,\ldots,dt_N\). Some \(c\)-row Jacobian minor is therefore invertible at \(\mathfrak q\). Clearing the finitely many denominators and shrinking the original affine neighbourhood makes these \(f_i\) generate its ideal and keeps that minor invertible. This is a standard-smooth presentation, so the morphism is smooth there by Formally smooth, unramified and étale ring maps, Theorem 4.1.

Conversely, on a standard-smooth neighbourhood the invertible Jacobian solves every square-zero lifting problem, by the same theorem. A morphism from a local Artinian scheme centred at \(x\) factors through that neighbourhood, since its underlying space has one point. It therefore lifts. Nilpotent extensions can also be treated in successive square-zero steps. This proves the criterion. The argument uses the actual residue field \(K\), and does not replace it by a separable extension. \(\square\)

**Theorem 3.2.** The class (3.1) vanishes if and only if a global embedded lift exists. When it vanishes, the global lifts form a torsor under \(H^0(Z,N)\otimes_k J\). In particular, if \(H^1(Z,N)=0\), the Hilbert scheme is smooth at \([Z]\), of dimension \(h^0(Z,N)\).

**Proof.** A zero class allows sections \(\beta_i\) whose changes make every \(\alpha_{ij}\) zero. The adjusted quotient kernels then agree on all intersections, and glue to a coherent ideal in \(\mathcal O_{X_{A'}}\). Its quotient is flat because flatness is local, and is proper by preservation of properness through a nilpotent thickening [Stacks, Tag 0BPG]. It gives a Hilbert point. Conversely a global lift, restricted to the cover, makes the cocycle zero, and comparing with it shows that any original cocycle is a coboundary.

Two global lifts differ by a compatible collection of local difference sections, hence by one section of \(N\otimes_k J\); every section changes a lift. This proves the torsor assertion. It also proves naturality of (3.1) under linear maps of \(J\).

If \(H^1(Z,N)=0\), every small-extension diagram centred at \([Z]\) lifts. The Hilbert scheme is locally of finite type, and the pointwise Artinian lifting criterion of Lemma 3.A [Stacks, Tag 02HX] proves smoothness. For its dimension, a smooth local scheme at a \(k\)-point has dimension equal to its tangent-space dimension. Equation (1.4) gives that dimension as \(h^0(Z,N)\). \(\square\)

The class (3.1) maps to (2.4). To see the comparison without replacing global Ext by sheaf Ext, take local splittings of (2.3). Their differences are exactly the sections \(\alpha_{ij}\). Gluing the locally split extensions with these differences reconstructs (2.3). Thus its extension class is the image of the Čech class under the map \(H^1(\mathcal Hom(K,G))\to\operatorname{Ext}^1(K,G)\). For regular embeddings local lifts exist, so this is the whole obstruction that is needed.

The relative smoothness assertion holds with a flat quasi-projective \(X/S\) over a Noetherian base and a proper regular embedding \(Z\subset X_K\), where \(K\) is the residue field of the Hilbert point. The preceding equation-lifting proof uses flatness and finite presentation of the ambient algebra, rather than smoothness itself: for each Artinian diagram over \(S\), apply Tag 0CEQ to that diagram's flat ambient algebra and its regular special-fibre equations. The normal sheaf is still locally free. Properness of a family persists through the nilpotent extension [Stacks, Tag 0BPG], and the relative criterion of Lemma 3.A [Stacks, Tag 02HX] applies. Thus \(H^1(Z,N)=0\) gives smoothness over \(S\) at that point.

## 4 Why an obstruction space bounds dimension

Let \(H\) be a locally finite-type \(k\)-scheme, \(h\) a \(k\)-point, and suppose its centred deformation functor has a **complete obstruction space** \(O\): for every small extension with kernel \(J\), there is a class in \(O\otimes_k J\), natural under linear pushouts of \(J\), whose vanishing is equivalent to existence of a lift. Assume \(O\) is finite-dimensional.

**Proposition 4.1.** If \(t=\dim_k T_{H,h}\), then

\[
t-\dim_k O\leq\dim_h H\leq t.
\tag{4.1}
\]

**Proof.** Let \(R=\widehat{\mathcal O}_{H,h}\), with residue field \(k\). Choose lifts of a basis of its cotangent space. Successive approximation in its maximal-ideal powers gives a surjection

\[
\begin{gathered}
S=k[[x_1,\ldots,x_t]]\\
\longrightarrow R=S/L,
\\
\qquad L\subset\mathfrak n^2.
\end{gathered}
\tag{4.2}
\]

For clarity, the approximation works because the chosen elements generate the maximal ideal by Nakayama. Every element of \(R\) can successively be matched by a constant and homogeneous polynomials in those generators, with remainders in successive powers; completeness sums the polynomials to a power series. The basis property makes the kernel have no linear term. Since \(S\) is Noetherian, \(V=L/\mathfrak n L\) is finite-dimensional. Put \(r=\dim_k V\); Nakayama says that \(L\) is generated by \(r\) elements.

For all sufficiently large \(n\), Artin–Rees [Stacks, Tag 00IN] gives \(L\cap\mathfrak n^n\subset\mathfrak n L\). Thus

\[
\begin{gathered}
A'=S/(\mathfrak n L+\mathfrak n^n)
\\
\longrightarrow A=S/(L+\mathfrak n^n)
\end{gathered}
\tag{4.3}
\]

is a small extension with kernel canonically \(V\). The map \(R\to A\) is a centred deformation, and its obstruction is an element \(o\in O\otimes_k V\). We claim that

\[
V^\vee\longrightarrow O,\qquad
\lambda\longmapsto(1\otimes\lambda)o
\tag{4.4}
\]

is injective.

Suppose a nonzero \(\lambda:V\to k\) makes this obstruction zero. Quotient \(A'\) by the subspace \(\ker\lambda\) of its small-extension kernel. Because the maximal ideal annihilates that kernel, this subspace is an ideal. The result \(B\to A\) is a small extension with kernel \(k\), and naturality says that the obstruction for \(R\to A\) is zero. Completeness of the obstruction space gives a lift \(R\to B\).

There are now two maps \(S\to B\): the canonical quotient map and the composite \(S\to R\to B\). They agree modulo the square-zero kernel \(k\), so their difference is a \(k\)-derivation \(S\to k\). Such a derivation kills \(\mathfrak n^2\), and hence kills \(L\). But the composite through \(R\) kills \(L\), whereas the canonical quotient map sends \(f\in L\) to \(\lambda([f])\). This forces \(\lambda=0\), a contradiction. The maps of power series cause no convergence issue: \(B\) is Artinian, so they factor through a finite power quotient.

Therefore \(r\leq\dim_k O\). Cutting the \(t\)-dimensional Noetherian local ring \(S\) by \(r\) elements lowers dimension by at most \(r\), by repeated application of the one-equation dimension inequality [Stacks, Tag 00KW]. Thus \(\dim R\geq t-r\geq t-\dim O\). Completion preserves dimension [Stacks, Tag 07NV], giving the lower bound for \(H\).

For the upper bound, the maximal ideal of the local ring is generated by \(t\) lifts of its cotangent basis. The dimension is at most the number of generators of an ideal of definition [Stacks, Tag 00KQ]. Equivalently (4.2) makes the completed ring a quotient of a power-series ring in \(t\) variables. This proves (4.1). \(\square\)

Apply this proposition with \(O=H^1(Z,N)\), using the natural complete obstruction class (3.1). Properness makes both this space and \(H^0(Z,N)\) finite-dimensional. We obtain the assigned estimate

\[
\begin{gathered}
h^0(Z,N)-h^1(Z,N)
\\
\leq\dim_{[Z]}\operatorname{Hilb}_{X/k}
\\
\leq h^0(Z,N).
\end{gathered}
\tag{4.5}
\]

Here dimension is the dimension of the local ring, including all components through the point. The argument bounds the number of generators of its completed defining ideal, not just the codimension of one chosen component.

There is no converse asserting that \(H^1(N)\ne0\) forces a singular Hilbert point. The proposition uses the actual obstruction classes; a vector space can contain them all even when all of them are zero.

## 5 Lines on hypersurfaces

Let \(S_d\subset\mathbb P^3_k\) be a smooth hypersurface of degree \(d\), and let \(L\simeq\mathbb P^1_k\) be a line on it. These hypotheses imply that \(L\subset S_d\) is a regular embedding of codimension one.

**Proposition 5.1.** The normal bundle is

\[
N_{L/S_d}\simeq\mathcal O_{\mathbb P^1}(2-d).
\tag{5.1}
\]

**Proof.** The line is cut in projective space by two independent linear equations, so \(N_{L/\mathbb P^3}=\mathcal O_L(1)^{\oplus2}\). The hypersurface normal bundle restricts as \(N_{S_d/\mathbb P^3}|_L=\mathcal O_L(d)\). The normal sequence is

\[
\begin{gathered}
0\longrightarrow N_{L/S_d}
\\
\longrightarrow\mathcal O_L(1)^{\oplus2}
\\
\xrightarrow{\partial f}\mathcal O_L(d)
\longrightarrow0.
\end{gathered}
\tag{5.2}
\]

One can check its surjectivity directly. Take coordinates with \(L=(x_2=x_3=0)\), and write \(f=x_2a+x_3b\). On \(L\), its differential along the line is zero, and its two normal components are \(a|_L,b|_L\), of degree \(d-1\). They cannot both vanish at any point of \(L\), since that would make the hypersurface singular there. Thus the last map is surjective. Its kernel is a line bundle, whose degree is \(2-d\), proving (5.1) by \(\operatorname{Pic}(\mathbb P^1)=\mathbb Z\). This argument uses no characteristic restriction. \(\square\)

For a cubic, \(N_{L/S_3}=\mathcal O(-1)\) and both \(H^0,H^1\) vanish. Every line therefore gives a smooth zero-dimensional Hilbert point. In particular its local ring is \(k\).

The Fano scheme of lines is the zero scheme in \(\operatorname{Gr}(2,k^4)\) of the section of \(\operatorname{Sym}^d U^\vee\) defined by \(f\), where \(U\) is the universal rank-two subbundle. This is the line construction of *Grassmannians*. Its tangent space at \(L\) is the kernel of

\[
H^0(\mathcal O_L(1)^{\oplus2})
\longrightarrow H^0(\mathcal O_L(d))
\tag{5.3}
\]

obtained by differentiating that section. Indeed, a first-order graph of a two-plane replaces \(x_2,x_3\) by linear forms on \(L\); the first-order coefficient in the equation is exactly \(a|_L\) times the first form plus \(b|_L\) times the second. The kernel in (5.3) is \(H^0(N_{L/S_d})\).

For a cubic this kernel is zero at every geometric point. A finite-type local ring at such a point has \(\mathfrak m/\mathfrak m^2=0\); Nakayama gives \(\mathfrak m=0\). Thus all its geometric points are reduced and isolated. The Fano scheme is projective, and is consequently finite and geometrically reduced, hence finite étale over \(k\). This proves reducedness without assuming how many lines exist.

For a quartic, \(N_{L/S_4}=\mathcal O(-2)\), so

\[
h^0(N)=0,\qquad h^1(N)=1.
\]

The same zero tangent-space argument still gives a reduced isolated point. This supplies the promised example in which a nonzero obstruction space does not imply singularity. It also avoids confusing a line's deformations inside a fixed surface with deformations of the pair consisting of the surface and the line.

## 6 Why the number is 27

### The intersection calculation through Euler characteristics

**Lemma 6.A (the numerical splitting calculation).** Let \(V=k^4\), let \(B=\operatorname{Gr}(2,V)\), and let \(U\) be its tautological rank-two subbundle. Put \(W=\operatorname{Sym}^3U^\vee\). If a section of \(W\) has a zero scheme \(F\) that is empty or is cut out by a regular sequence of length four, then
\[
\deg F=27.
\]
The assertion holds over every field. The calculation also gives the numerical Chern identities used in (6.1)–(6.4), without requiring a construction of the general Chow ring.

**Proof.** We will use the Grothendieck group of vector bundles: an exact sequence \(0\to E'\to E\to E''\to0\) gives the relation \([E]=[E']+[E'']\), and tensor product defines multiplication. Euler characteristic defines an additive function on this group. The filtration of \(\bigwedge^j E\) by the number of factors in \(E'\) has quotients
\(\bigwedge^a E'\otimes\bigwedge^{j-a}E''\). Thus, with
\[
\lambda_t(E)=\sum_j[\bigwedge^jE]t^j,
\qquad
\lambda_t(E)=\lambda_t(E')\lambda_t(E'').
\]
This proves the exterior-power identity for nonsplit sequences as well as split ones. It involves vector bundles and integer coefficients, so it is valid in every characteristic.

Let \(p:Y=\mathbf P_B(U)\to B\) parametrize lines in the fibres of \(U\). On \(Y\) there is an exact sequence
\[
0\longrightarrow L\longrightarrow p^*U\longrightarrow M\longrightarrow0
\]
of line bundles. Write
\[
l=1-[L],\qquad m=1-[M].
\]
The same flag variety has a projection \(q:Y\to\mathbf P(V)=\mathbf P^3\) remembering \(L\). It is the projective bundle of lines in \(V/L\), with fibre \(\mathbf P^2\); hence \(Y\) is smooth projective of dimension five, and \(L=q^*\mathcal O_{\mathbf P^3}(-1)\).

For later use, if a monomial in \(l,m\) has total degree greater than five, its Euler characteristic is zero. Indeed, expanding its factors \(1-[L]\) and \(1-[M]\) expresses that Euler characteristic as a finite difference of the polynomial
\(\chi(Y,L^a\otimes M^b)\), of total degree at most five. This polynomial property, its difference formula for intersection numbers, and restriction to a Cartier divisor are proved in Intersection numbers of line bundles, Theorem 1.2, Lemma 2.2 and Proposition 2.4.

The Koszul complex of the section of \(W\) is a locally free resolution of \(\mathcal O_F\). For one regular equation its two-term complex is exact off the quotient in degree zero. On adjoining the next equation the Koszul complex is the cone of multiplication by that equation on the preceding complex. The homology exact sequence and its injectivity on the preceding quotient leave only the next quotient in degree zero. This proves exactness by induction; for an empty zero scheme a unit among the local equations contracts the complex. Therefore
\[
\deg F=\chi(B,\mathcal O_F)
       =\chi\bigl(B,\lambda_{-1}(W^\vee)\bigr).
\]
For the projective-line bundle \(p\), one has \(Rp_*\mathcal O_Y=\mathcal O_B\) and \(Rp_*L=0\): on a trivializing open these are the cohomology calculations for \(\mathcal O\) and \(\mathcal O(-1)\) on \(\mathbf P^1\), and the identifications glue. These calculations, including arbitrary base change, are Cohomology of projective space, Theorem 5.2. The projection formula for a vector bundle and the Euler-characteristic Leray formula consequently give
\[
\deg F=\chi\bigl(Y,l\,p^*\lambda_{-1}(W^\vee)\bigr).
\tag{6.A.1}
\]

The filtration of \(\operatorname{Sym}^3p^*U^\vee\) has line factors
\(L^{-3},L^{-2}M^{-1},L^{-1}M^{-2},M^{-3}\). Dualizing that filtration and applying the exterior-power identity gives
\[
\begin{gathered}
p^*\lambda_{-1}(W^\vee)\\
=(1-[L]^3)(1-[L]^2[M])\\
{}\cdot(1-[L][M]^2)(1-[M]^3).
\end{gathered}
\]
This uses the dual filtration; it does not identify the dual of a symmetric power with a symmetric power in positive characteristic. Substituting \([L]=1-l,\ [M]=1-m\), the homogeneous term of degree four is
\[
\begin{gathered}
9lm(2l+m)(l+2m)\\
=18(l^3m+lm^3)+45l^2m^2.
\end{gathered}
\]
All other terms have degree at least five. After multiplication by \(l\), those other terms have zero Euler characteristic by the finite-difference vanishing. Thus (6.A.1) becomes
\[
\begin{gathered}
\deg F=\\
18\chi(Y,l^4m+l^2m^3)\\
+45\chi(Y,l^3m^2).
\end{gathered}
\tag{6.A.2}
\]

It remains to obtain the relation and the normalization of this number. Let \(Q\) be the rank-two quotient \(V/U\). Exterior powers of \(p^*Q\) in degrees three and four are zero. On writing \(h_j(l,m)=\sum_{a=0}^j l^am^{j-a}\), the identity for the exact sequence \(0\to p^*U\to\mathcal O_Y^4\to p^*Q\to0\) reads
\[
\begin{gathered}
\lambda_t(p^*Q)
=\frac{(1+t)^4}{(1+t[L])(1+t[M])}\\
=\sum_{j\geq0}h_j(l,m)t^j(1+t)^{2-j}.
\end{gathered}
\]
Its coefficient of \(t^3\) is \(h_3\), and its coefficient of \(t^4\) is \(h_4-h_3\). Both vanish. Subtracting \(h_4\) from \((l+m)h_3\) therefore gives the exact identity in the Grothendieck group
\[
l^3m+l^2m^2+lm^3=0.
\]
Multiplying by \(l\) and taking Euler characteristics in (6.A.2) gives
\[
\deg F=27\chi(Y,l^3m^2).
\]

Finally, the finite-difference formula identifies
\(\chi(Y,l^3m^2)\) with the intersection number of three copies of \(L^\vee\) and two copies of \(M^\vee\). Choose three hyperplanes on \(\mathbf P^3\) meeting in a rational point. Their inverse images under the flat projective bundle \(q\) form successive Cartier divisors and leave the fibre \(\mathbf P^2\). On that fibre, \(M^\vee\) is \(\mathcal O_{\mathbf P^2}(1)\); two hyperplane sections then leave one reduced rational point. Repeated restriction to these divisors proves
\[
\chi(Y,l^3m^2)=1.
\]
This proves the assertion.

To compare with the Chern notation below, \(l,m\) in the top finite difference represent \(x=c_1(L^\vee),y=c_1(M^\vee)\), and the extra factor \(l\) integrates along the projective-line bundle. The degree-four product, the relation obtained from \(h_3,h_4\), and the last normalization are exactly the numerical identities in (6.2), (6.3) and (6.4); the Koszul resolution gives their zero-scheme interpretation (6.1). Every numerical equality used in the line count has thus been proved over the original field. \(\square\)

**Theorem 6.1.** Over an algebraically closed field of any characteristic, a smooth cubic surface has exactly 27 lines. Over any field, its Fano scheme is finite étale of degree 27.

**Proof.** Let \(B=\operatorname{Gr}(2,k^4)\), which is smooth projective of dimension four. Put \(W=\operatorname{Sym}^3 U^\vee\), of rank four. The cubic's Fano scheme \(F\) is \(Z(s_f)\). Section 5 shows that at every geometric zero the derivative \(T_B\to W\) is injective, hence is an isomorphism between two four-dimensional spaces. Its four local equations are therefore a regular sequence and the zero is reduced. Since all zeros are isolated, Lemma 6.A gives the zero-scheme degree formula, written in top-Chern notation as [Stacks, Tag 0FA9]

\[
\deg F=\int_B c_4(W).
\tag{6.1}
\]

The formula includes the possibility of an empty zero scheme; the following nonzero calculation will rule it out.

We express the numerical calculation of Lemma 6.A in Chern notation. On its flag bundle, the duals of \(L,M\) have first Chern classes \(x,y\). The exterior-power identities and finite differences proved there give all the degree identities used below. In the general language of intersection theory, these are the relevant instances of Chern-class additivity, splitting and the regular-section formula [Stacks, Tags 02UI, 02UL and 0FA9].

The induced filtration on \(\operatorname{Sym}^3 U^\vee\) has line-bundle factors with first Chern classes

\[
3x,\qquad 2x+y,\qquad x+2y,\qquad 3y.
\]

The filtration comes from sorting the monomials in a local basis adapted to the line subbundle; changing the adapted basis preserves the resulting filtration. It is valid in every characteristic. Hence

\[
\begin{gathered}
c_4(W)\\
=9xy(2x+y)(x+2y)\\
=18(x^3y+xy^3)+45x^2y^2.
\end{gathered}
\tag{6.2}
\]

Let \(Q\) be the rank-two quotient in \(0\to U\to\mathcal O_B^4\to Q\to0\). Since the roots of \(U\) are \(-x,-y\), additivity gives

\[
c(Q)=\frac1{(1-x)(1-y)}
=\sum_{i\geq0}h_i(x,y),
\]

where \(h_i=x^i+x^{i-1}y+\cdots+y^i\). The rank-two bundle has \(c_3(Q)=c_4(Q)=0\). Thus \(h_3=h_4=0\), and subtracting \(h_4\) from \((x+y)h_3\) gives

\[
x^3y+x^2y^2+xy^3=0.
\tag{6.3}
\]

Substitution into (6.2) yields \(c_4(W)=27x^2y^2=27c_2(U^\vee)^2\).

Finally

\[
\int_B c_2(U^\vee)^2=1.
\tag{6.4}
\]

Here is its geometric verification. A nonzero linear functional \(\lambda\) on \(k^4\) gives a section of \(U^\vee\). Its zero locus is the smooth codimension-two Grassmannian of two-planes contained in \(\ker\lambda\), and so represents \(c_2(U^\vee)\). Two independent functionals \(\lambda,\mu\) have a single simultaneous zero: the plane \(\ker\lambda\cap\ker\mu\). On a graph chart around this plane, the combined four section coordinates are independent linear coordinates. Their intersection is therefore a transverse reduced point of degree one. Equivalently apply the top-Chern formula to the combined section of \(U^\vee\oplus U^\vee\). This proves (6.4).

Equations (6.1)–(6.4) give degree 27. Since \(F\) is reduced over an algebraically closed field, its degree is its number of points. The construction and calculation commute with field extension. Section 5 proved finite étaleness over the original field, and its geometric degree is 27. \(\square\)

The integers in this computation are Chow degrees, even in characteristics three or another positive characteristic. They are not coefficients reduced modulo the characteristic. Thus no division by 2 or 3, and no assumption about the usual explicit complex configuration of lines, enters the count.

## 7 Points, conics, and larger Hilbert schemes

At a \(k\)-rational point \(p\) of a smooth \(n\)-dimensional variety, the conormal space is \(\mathfrak m_p/\mathfrak m_p^2\). Equation (1.4) identifies

\[
T_{[p]}\operatorname{Hilb}^1_X
=\operatorname{Hom}_k(\mathfrak m_p/\mathfrak m_p^2,k)
=T_pX,
\]

of dimension \(n\). A finite scheme has no higher coherent cohomology, so its regular-embedding normal sheaf has \(H^1=0\). The Hilbert point is smooth.

For the nonreduced length-two subscheme
\(Z=(y,x^2)\subset\mathbb A^2\), the two equations form a regular sequence. With \(B=k[x]/(x^2)\),

\[
\mathcal I_Z/\mathcal I_Z^2\simeq B^2,\qquad
N\simeq B^2.
\]

Its tangent space has dimension four. A homomorphism is determined by

\[
y\longmapsto c+dx,\qquad
x^2\longmapsto a+bx.
\tag{7.1}
\]

With the kernel convention (1.3), the corresponding first-order equations are \(y+\epsilon(c+dx)\), \(x^2+\epsilon(a+bx)\). Replacing all four parameters by their negatives gives the alternative convention of subtracting the first-order terms. The four-dimensional calculation is unchanged, including in characteristic two.

The chart in *Hilbert and Quot schemes* with quotient basis \(1,x\) writes \(x^2=a+bx\), \(y=c+dx\), with four unrestricted coordinates. It identifies a neighbourhood of this point with \(\mathbb A^4\) and confirms smoothness directly. The obstruction proof gives the same conclusion, because the normal sheaf is supported on the finite \(Z\) and \(H^1(N)=0\).

For a smooth plane conic \(C\), its ideal is \(\mathcal O_{\mathbb P^2}(-2)\), and its normal bundle is \(\mathcal O_C(2)\). After algebraic closure \(C\simeq\mathbb P^1\), and \(\mathcal O_C(1)=\mathcal O_{\mathbb P^1}(2)\); hence \(N=\mathcal O_{\mathbb P^1}(4)\). It has five sections and zero first cohomology. The Hilbert scheme is smooth of dimension five at \(C\). If a conic over \(k\) has no \(k\)-rational point, the cohomology calculation still follows by field extension and faithful flatness; its parameter point as a subscheme is nevertheless a \(k\)-point of the Hilbert scheme.

### Finite algebras in two variables

The regular-embedding criterion does not cover every finite subscheme of a surface. For example, the ideal \((x,y)^2\) needs three generators at its support. Nevertheless its Hilbert point is smooth. The reason is specific to a two-dimensional ambient space: the tangent space has dimension exactly twice the length, even when the subscheme is not a complete intersection.

**Lemma 7.1.** Let \(k\) be algebraically closed, \(R=k[x,y]\), and \(B=R/I\) have finite positive dimension \(n\) over \(k\). Then

\[
\dim_k\operatorname{Hom}_R(I,B)=2n.
\tag{7.2}
\]

**Proof.** We first supply the homological facts needed for this calculation. At a closed point \((a,b)\), the Koszul complex on \(x-a,y-b\) is a finite free resolution of its residue field. Its dual has cohomology \(k\) in degree two and zero in all other degrees. Any finite-length \(R\)-module has a composition series with these residue fields as factors. Splicing the two-term free resolutions through a short exact sequence gives another free resolution of length at most two: lift the free generators of the quotient to the middle module, use the direct sum with the free generators of the submodule, and repeat on the kernels. This is the horseshoe construction, and the short exact sequences of kernels prove its exactness. Thus every finite-length module \(M\) has a finite free resolution of length at most two.

The long exact Ext sequence along the same composition series shows

\[
\begin{gathered}
\operatorname{Ext}^i_R(M,R)=0\quad(i\ne2),\\
\dim_k\operatorname{Ext}^2_R(M,R)=\dim_k M.
\end{gathered}
\tag{7.3}
\]

Indeed the functor \(\operatorname{Ext}^2_R(-,R)\) is exact, with arrows reversed, on finite-length modules: the adjacent groups \(\operatorname{Ext}^1\) and \(\operatorname{Ext}^3\) vanish. Each residue-field factor contributes one dimension.

Choose a finite free resolution \(F_2\to F_1\to F_0\to B\), and put \(D=\operatorname{Ext}^2_R(B,R)\). Every \(r\in I\) annihilates \(D\). To see this, multiplication by \(r\) on the resolution lifts the zero map on \(B\). It is null-homotopic: starting in degree zero, lift its image into the next free module, and continue along the exact resolution. Applying \(\operatorname{Hom}_R(-,R)\) makes the induced map on cohomology zero. The scalar action through the first argument is the usual scalar action through the second argument because \(R\) is commutative. Therefore \(D\otimes_R B=D\).

The last cokernel of a complex commutes with tensor product. Since \(F_i\) is finite free, the dual complex tensored with \(B\) is exactly \(\operatorname{Hom}_R(F_\bullet,B)\). Its last cokernel is therefore the last cokernel \(D\) of the dual complex, tensored with \(B\):

\[
\operatorname{Ext}^2_R(B,B)=D\otimes_R B=D.
\tag{7.4}
\]

In particular this group has dimension \(n\). Also \(\operatorname{Hom}_R(B,B)=B\). The alternating sum of the ranks of the resolution is zero, because tensoring it with the fraction field of \(R\) resolves the zero module. Taking the Euler characteristic of \(\operatorname{Hom}_R(F_\bullet,B)\) consequently gives

\[
n-\dim_k\operatorname{Ext}^1_R(B,B)+n=0.
\]

Finally apply \(\operatorname{Hom}_R(-,B)\) to \(0\to I\to R\to B\to0\). The map \(\operatorname{Hom}_R(B,B)\to\operatorname{Hom}_R(R,B)\) is an isomorphism: both identify a map with the image of \(1\). Since \(R\) is free, the next connecting map identifies \(\operatorname{Hom}_R(I,B)\) with \(\operatorname{Ext}^1_R(B,B)\). Its dimension is therefore \(2n\). No division by an integer, or assumption that \(B\) is a complete intersection, entered the argument. \(\square\)

The tangent dimension alone does not yet prove smoothness: one must also obtain the required local dimension. We do this by constructing families leading to distinct points.

### Staircases and families of distinct points

A monomial ideal of finite colength has a staircase of monomials outside it. Choose integers

\[
\begin{gathered}
\lambda_0\ge\lambda_1\ge\cdots\ge\lambda_{s-1}>0,\\
\lambda_s=0.
\end{gathered}
\tag{7.5}
\]

The staircase \(\mathcal B_\lambda\) contains, for each \(0\le j<s\), the \(\lambda_j\) monomials \(y^j,xy^j,\ldots,x^{\lambda_j-1}y^j\). The associated ideal \(I_\lambda\) is generated by \(x^{\lambda_j}y^j\), for \(0\le j\le s\), and its colength is \(n=\sum_{j<s}\lambda_j\).

**Lemma 7.2.** Every such monomial subscheme is a flat limit of \(n\) distinct points of the affine plane.

**Proof.** Choose distinct constants \(a_0,\ldots,a_{\lambda_0-1}\) and distinct constants \(b_0,\ldots,b_{s-1}\) in \(k\). In \(k[t,x,y]\), set

\[
\begin{aligned}
P_m(t,x)&=\prod_{i=0}^{m-1}(x-ta_i),\\
Q_j(t,y)&=\prod_{\ell=0}^{j-1}(y-tb_\ell),\\
G_j(t,x,y)&=P_{\lambda_j}(t,x)Q_j(t,y).
\end{aligned}
\tag{7.6}
\]

Here \(0\le j\le s\), and an empty product is one. At \(t=0\) these generators give exactly \(I_\lambda\). Each \(G_j\) has leading term \(x^{\lambda_j}y^j\), and all its other terms have smaller total degree in \(x,y\). Replacing a monomial divisible by that leading term with the remaining terms therefore terminates. The quotient by all the \(G_j\) is generated over \(k[t]\) by the \(n\) monomials in \(\mathcal B_\lambda\).

Over \(k(t)\), the generators vanish at the distinct points

\[
(ta_i,tb_j)\qquad\text{with }0\le i<\lambda_j,
\tag{7.7}
\]

one row for each \(0\le j<s\).

For a point in row \(j\), a generator \(G_\ell\) with \(\ell>j\) vanishes by a \(y\)-factor. If \(\ell\le j\), then \(\lambda_j\le\lambda_\ell\), and it vanishes by an \(x\)-factor. Evaluation thus gives a surjection from the generic quotient onto \(k(t)^n\). The previously obtained \(n\) generators must be a basis over \(k(t)\). Any \(k[t]\)-linear relation between their classes is then zero after passage to \(k(t)\), so all its polynomial coefficients are zero. They form a free \(k[t]\)-basis. This proves flatness and constant length. The same evaluation argument after any specialization \(t=c\ne0\) identifies that fibre with the \(n\) distinct points (7.7). \(\square\)

For instance \(\lambda=(3,2)\) gives the ideal \((x^3,x^2y,y^2)\), with basis \(1,x,x^2,y,xy\). Its special fibre is supported at one point; the five basis monomials are not five distinct support points. Formula (7.6) separates it into three points on one horizontal line and two on a second line. It also makes sense in characteristic two: only distinct choices of the constants are required.

**Lemma 7.3.** Every finite subscheme of \(\mathbb A^2_k\) has a flat one-parameter degeneration to a monomial subscheme of the same length. Away from zero the family consists of coordinate rescalings of the original subscheme.

**Proof.** We recall the finite algebra behind this degeneration. Order monomials first by total degree, then lexicographically. The leading monomials of the elements of \(I\) generate a monomial ideal with finitely many minimal generators. In two variables, finiteness follows by listing their \(x\)-exponents increasingly: their \(y\)-exponents must then strictly decrease. Choose polynomials with those leading monomials. Division by them leaves no nonzero remainder for an element of \(I\), since such a remainder would itself have a leading monomial in the leading ideal but divisible by none of its generators. The chosen polynomials are therefore a finite Gröbner basis.

There are finitely many pairs of basis polynomials. Their leading-term cancellation polynomials reduce to zero by division. Choose positive integer weights \((u,v)\) that reproduce every monomial comparison in these finitely many polynomials and division calculations. Such weights exist: for the degree-lexicographic order, weights \((N+1,N)\) work for any prescribed finite set once \(N\) is large enough. The same reductions show that the weighted leading ideal is the same monomial ideal. Here is the cancellation argument: in an expression \(f=\sum h_i g_i\), choose the largest weighted leading monomial of a summand. If the contributions at that monomial cancel, replace their differences by the corresponding leading-term cancellation polynomials and their recorded reductions. This decreases the largest monomial, or the number of terms at that monomial. Repetition shows that the leading monomial of any nonzero \(f\in I\) is divisible by one of the chosen leading monomials. Thus no extra weighted initial relation has been assumed.

Give \(B=R/I\) the filtration \(F_dB\) consisting of images of polynomials of weight at most \(d\), and form

\[
\mathcal R=\bigoplus_{d\ge0}F_dB\,t^d\ \subset B[t].
\tag{7.8}
\]

It is an algebra over \(k[t]\), generated by \(xt^u,yt^v\). Choose a \(k\)-basis of \(B\) adapted to the increasing filtration, and let \(d_i\) be the first filtration degree of its \(i\)-th vector \(e_i\). Then \(e_i t^{d_i}\) form a free \(k[t]\)-basis of \(\mathcal R\): in each graded degree, precisely the vectors with \(d_i\le d\) form a basis of \(F_dB\). Consequently \(\mathcal R\) is finite free of rank \(n\). The quotient by \(t\) is \(\operatorname{gr}_F B\), which is the quotient by the weighted leading ideal just computed. Inverting \(t\) gives \(B[t,t^{-1}]\). The surjection \(k[t,X,Y]\to\mathcal R\), given by \(X\mapsto xt^u\), \(Y\mapsto yt^v\), realizes the required finite flat family inside \(\mathbb A^2\times\mathbb A^1\). Its fibre at \(c\ne0\) is the original subscheme rescaled by \((x,y)\mapsto(c^u x,c^v y)\). \(\square\)

### Smoothness and irreducibility on a surface

**Theorem 7.4 (Fogarty).** Let \(X\) be a smooth irreducible quasi-projective surface over an algebraically closed field. For every integer \(n\ge0\), the scheme \(\operatorname{Hilb}^n(X)\) is smooth and irreducible of dimension \(2n\).

**Proof.** The case \(n=0\) is \(\operatorname{Spec}k\). Suppose \(n>0\), and first take \(X=\mathbb A^2\). By Section 1 and Lemma 7.1 the tangent space has dimension \(2n\) at every closed Hilbert point.

The open locus \(U_n\) of distinct points is irreducible of dimension \(2n\). Indeed the open subscheme of ordered distinct tuples in \((\mathbb A^2)^n\) is irreducible of that dimension, and forgetting the ordering is finite étale and surjective onto \(U_n\). This assertion is valid even when the characteristic divides \(n!\): ordering the distinct points of a finite étale family is a torsor under the constant étale group \(\mathfrak S_n\), with no averaging operation. Let \(W\) be the closure of \(U_n\), with its reduced structure.

Every monomial point belongs to \(W\) by Lemma 7.2. Its local dimension is at least \(2n\), because the irreducible closed subscheme \(W\) has that dimension. Its embedding dimension is \(2n\) by Lemma 7.1. The local ring is therefore regular; over the algebraically closed field this Hilbert point is smooth. In particular it lies on only one irreducible component.

Now degenerate an arbitrary Hilbert point to a monomial point by Lemma 7.3. The inverse image of the smooth locus is an open subset of \(\mathbb A^1\) containing zero. It contains a nonzero point, whose Hilbert fibre is isomorphic, by coordinate rescaling, to the original subscheme. Hence the original Hilbert point is smooth too. This proves smoothness everywhere: a nonempty closed nonsmooth locus in a finite-type \(k\)-scheme would contain a closed point.

In a smooth finite-type scheme the irreducible components are disjoint and open as well as closed. Here every component has dimension \(2n\), so the irreducible closed subset \(W\) of that dimension is a component. The degeneration in Lemma 7.3 has connected parameter space, so its original point lies on the same component as its monomial limit. Every such limit lies on \(W\), and regularity there excludes a second component through it. It follows that the entire Hilbert scheme is \(W\). Its dimension is \(2n\).

We explain carefully how to return from the affine plane to \(X\). Let \(Z\subset X\) be finite of length \(n\). Quasi-projectivity supplies an affine neighbourhood \(V\) of its finite support: embed \(X\) into projective space and choose a sufficiently high-degree hypersurface containing the boundary and avoiding those finitely many points. Its complement is affine. At each support point choose two cotangent coordinates and two prescribed coordinate values, with distinct pairs of values for distinct support points. The Chinese remainder theorem for the squares of their maximal ideals gives global functions \(f,g\in\Gamma(V,\mathcal O_V)\) with these values and cotangent classes. The resulting map \(h=(f,g):V\to\mathbb A^2\) is étale near the support; shrink to that open neighbourhood. On each local Artin component of \(Z\), the map induced by \(h\) is surjective: the étale map has identical residue field and induces an isomorphism of completed local rings. The distinct images of the support points then show that \(h|_Z\) is a closed immersion.

Consider the open locus \(H_h\subset\operatorname{Hilb}^n(V)\) where this restriction is a closed immersion. To justify openness, the map from any universal finite family to \(\mathbb A^2\) is finite: its graph is closed and the projection from the product with that finite family is finite. Failure of the map on structure sheaves to be surjective is the support of a finite module, with support finite over the parameter scheme. Its image in the parameter scheme is closed. Off that image the restriction is a closed immersion. Taking the image family thus defines

\[
h_*:H_h\longrightarrow\operatorname{Hilb}^n(\mathbb A^2).
\tag{7.9}
\]

This map is étale. Here is its infinitesimal lifting test. For any surjection of affine base rings \(A'\to A\) with nilpotent kernel, let \(D'\subset\mathbb A^2_{A'}\) be the given image family and let the specified lift over \(A\) be \(Z_A\subset V_A\). It is a section of the étale morphism \(V\times_{\mathbb A^2}D'\to D'\) over the nilpotent closed subscheme \(D_A\). Formal étaleness extends that section uniquely to \(D'\). Since the morphism is separated, its section is closed; it gives exactly the required closed subscheme of \(V_{A'}\), isomorphic to \(D'\). This proves existence and uniqueness of the lift. The schemes in (7.9) are locally of finite type over \(k\), so their morphism is locally of finite presentation. The formal étale criterion therefore proves the assertion. Both the lifting property of an étale map and the converse with local finite presentation are proved in Infinitesimal lifting and the invariance of étale morphisms under thickenings, Theorem 4.1.

It follows from (7.9) and the affine-plane case that \(\operatorname{Hilb}^n(X)\) is smooth of dimension \(2n\) near \(Z\). To check irreducibility, observe also that étale maps are open. Every neighbourhood of \(Z\) in \(H_h\) has open image containing \(h_*Z\), and therefore meets the dense distinct-point locus of the irreducible plane Hilbert scheme. Its preimage is a reduced finite subscheme of \(V\), because it is isomorphic to its image. Thus every neighbourhood of \(Z\) meets the distinct-point locus on \(X\).

The latter locus is irreducible, being the image of the ordered distinct-point open subset of \(X^n\). It is dense by the preceding argument. Its closure is therefore the whole Hilbert scheme, proving irreducibility. This completes the argument in every characteristic. \(\square\)

The tangent calculation and the degeneration do different jobs. Equation (7.2) controls the possible local embedding dimension; the families (7.6) and (7.8) place every plane subscheme on the component containing distinct configurations. Neither a nonzero obstruction space nor the tangent dimension alone could supply that component argument. Fogarty's original theorem and Bertin's exposition, Section 3.1, provide the historical context for this surface phenomenon.


### A nonreduced family of space curves

We now turn from a smooth parameter space to a component with nilpotents at its generic point. Throughout this example, \(k\) is algebraically closed of characteristic zero. Mumford's example concerns smooth connected curves of degree \(14\) and genus \(24\) in \(\mathbb P^3\). Write \(\mathcal H\) for the curve Hilbert scheme. The two relevant dimensions are

\[
\dim W=56,\qquad
\dim T_{[C]}\mathcal H=57
\tag{7.10}
\]

at general members of a component \(W\). Establishing both dimensions is essential: an isolated tangent calculation would not show that \(W\) is a component, or that it is generically nonreduced.

We use cohomology of line bundles on projective space, the Serre duality and adjunction proved in Dualizing sheaves and Serre duality for projective schemes, Sections 2–5, and the Hilbert tangent formula already proved in Section 1. The curve Riemann–Roch and canonical-bundle calculations also have the preceding proof Formal moduli and Schlessinger’s theorem, Lemma 8.A. The family arguments use Base change and the Grothendieck complex, Theorem 3.2 and Corollary 4.1 and Semicontinuity and Grauert's theorem, Theorem 3.1. In particular a fibrewise trivial line bundle on a projective-line bundle is pulled back from its base: its first fibre cohomology is zero, its direct image is a line bundle compatible with base change, and evaluation is an isomorphism on fibres and hence everywhere. For a line bundle \(M\) on a smooth connected curve, we will also use

\[
\chi(M)=\deg M+1-g.
\tag{7.11}
\]

Here this Euler-characteristic formula can be obtained directly. A nonzero rational section writes \(M=\mathcal O_C(D)\); adding one point to a divisor changes the Euler characteristic by one, by the exact sequence with its one-dimensional residue-field quotient. Adding and subtracting the finitely many points of \(D\) proves (7.11). Serre duality then gives \(\deg\omega_C=2g-2\). If a smooth curve is a Cartier divisor on a surface smooth along it, the conormal sequence and its determinant give

\[
\omega_C=(\omega_S\otimes\mathcal O_S(C))|_C.
\tag{7.12}
\]

Thus the adjunction calculations below retain the actual line bundles, rather than inferring their classes from numerical dimensions.

#### Residual curves in a pencil of quartics

**Lemma 7.5.** A smooth connected curve \(C\subset\mathbb P^3\) of degree \(14\) and genus \(24\) is not contained in a plane or a quadric. If it is not contained in a cubic, it lies on a pencil of quartics with no fixed surface component. The residual curve in the intersection of two independent members is a plane conic, possibly reducible or nonreduced. A general member of that pencil is smooth at every point of \(C\).

**Proof.** A smooth plane curve of degree \(14\) has genus \(78\), by plane adjunction. On a smooth quadric, the two ruling classes give a curve class \((a,b)\), with degree \(a+b\) and genus \((a-1)(b-1)\). The prescribed degree and genus would give \(a+b=14\), \(ab=37\), which has no integral solution.

We include the cone case. In characteristic zero a singular irreducible quadric is a cone; its vertex blow-up is the ruled surface
\(\mathbb P_{\mathbb P^1}(\mathcal O\oplus\mathcal O(2))\).
Let \(E\) be its contracted section and \(f\) a ruling fibre. Its two local bundle charts show that the normal bundle of \(E\) is \(\mathcal O_{\mathbb P^1}(-2)\), so

\[
\begin{gathered}
E^2=-2,\quad E\cdot f=1,\quad f^2=0,\\
H=E+2f.
\end{gathered}
\]

For completeness the contraction is given by the sections with coordinates \([a s^2:a st:a t^2:b]\); it maps onto the cone and contracts precisely \(E\). A line bundle on the ruled surface has a constant fibre degree, because its fibre Euler characteristic is locally constant in this flat projective family. Subtract that multiple of the tautological line bundle. The resulting bundle is trivial on every fibre; cohomology and base change makes its direct image a line bundle on \(\mathbb P^1\), and evaluation from its pullback is an isomorphism, since this is so on every fibre. Thus every line bundle is a combination of the tautological class and a pullback from \(\mathbb P^1\). Since \(\operatorname{Pic}(\mathbb P^1)=\mathbb Z\), the Picard group of the ruled surface is generated by \(E,f\). The canonical class is \(-2E-4f\): restriction to a fibre determines the coefficient \(-2\), and adjunction on \(E\simeq\mathbb P^1\) determines the other coefficient. The strict transform \(\widetilde C\) of a smooth curve is isomorphic to \(C\). Indeed the ideal of the vertex restricts either to the unit ideal or to the invertible ideal of one point on the smooth curve, so the universal property of the blow-up gives this strict-transform lift. Write \(\widetilde C=aE+14f\), using \(H\cdot\widetilde C=14\). Adjunction gives

\[
g(C)=36-(a-7)^2.
\]

It cannot equal \(24\). A reducible or nonreduced quadric has plane support components; an integral curve in it would be planar. This excludes all quadrics.

Since \(\deg\omega_C(-4)=46-56<0\), Serre duality and (7.11) give \(h^0(\mathcal O_C(4))=33\). There are \(35\) quartic forms on \(\mathbb P^3\), so \(h^0(\mathcal I_C(4))\ge2\). If \(C\) lies on no cubic, every nonzero quartic containing it is irreducible: a proper factor has degree at most three and would have to contain the integral curve. Two independent quartics therefore have no common surface component. Let \(D=F\cap G\) be their complete intersection, of degree \(16\).

We spell out the residual construction and its duality. In \(\mathcal O_D\), put \(J=\mathcal I_C/\mathcal I_D\), and define \(Q\) by
\(\mathcal I_Q/\mathcal I_D=\operatorname{Ann}_{\mathcal O_D}(J)\).
Both \(D\) and \(C\) are Cohen–Macaulay of dimension one. The duality functor \(\operatorname{Hom}_{\mathcal O_D}(-,\mathcal O_D)\) is exact and double dualization is the identity on their maximal Cohen–Macaulay modules. One can verify these assertions in the ambient regular local ring: Auslander–Buchsbaum gives a length-two finite free resolution, its dual has only degree-two cohomology, and dualizing this resolution again recovers the module. The Koszul resolution of the two quartic equations identifies this ambient degree-two Ext with Hom over \(\mathcal O_D\); it also makes the next Ext group zero. These are the local resolution and change-of-rings arguments of the two linked duality sections. Applying them to \(0\to J\to\mathcal O_D\to\mathcal O_C\to0\) shows that \(\mathcal O_Q\) is Cohen–Macaulay and that taking the annihilator a second time returns \(J\). Thus there are no embedded points in the residual curve.

The complete-intersection adjunction is \(\omega_D=\mathcal O_D(4)\). The same duality identifies

\[
0\to\mathcal I_D
\to\mathcal I_Q
\to\omega_C(-4)
\to0.
\tag{7.13}
\]

Explicitly its last term is \(\operatorname{Hom}_D(\mathcal O_C,\omega_D)\otimes\mathcal O_D(-4)\); the Hom is the dualizing sheaf of \(C\), as follows either from closed-immersion adjunction or its representing property. Since a double occurrence of the degree-\(14\) component in a degree-\(16\) complete intersection is impossible, \(D\) has multiplicity one along \(C\). At every other generic point the residual curve retains the full multiplicity of \(D\). Hence its degree is \(16-14=2\), and its cycle is the residual part of the cycle of \(D\).

Twist (7.13) by one. The Koszul sequence

\[
0\longrightarrow\mathcal O(-7)
\longrightarrow\mathcal O(-3)^2
\longrightarrow\mathcal I_D(1)\longrightarrow0
\]

and projective-space cohomology give \(H^0(\mathcal I_D(1))=H^1(\mathcal I_D(1))=0\). On the other hand, the absence of a cubic equation injects the \(20\) cubic forms into \(H^0(\mathcal O_C(3))\). Since \(\chi(\mathcal O_C(3))=19\), its first cohomology is nonzero. Serre duality gives \(H^0(\omega_C(-3))\ne0\). Sequence (7.13) therefore gives a nonzero linear equation for \(Q\). A pure degree-two curve in a plane is a conic: its plane ideal is an unmixed height-one ideal in the factorial polynomial ring, hence is generated by a quadratic form. This includes two lines and a double line.

It remains to find a quartic smooth along \(C\). At a point of \(C\), the multiplicity of \(D\) is at most \(1+2=3\), from its smooth curve component and the residual plane conic. Both quartics cannot be singular there. If they were, intersect with a general plane through that point. The resulting zero-dimensional intersection would have length at least four: modulo the cube of the maximal ideal of a regular two-dimensional local ring there are one constant, two linear and three quadratic classes, and two equations of order at least two kill at most two of the quadratic classes. This contradicts the multiplicity bound. At the general point of \(C\), the gradients of \(F,G\) are independent, because the intersection has multiplicity one along \(C\). Their failure to be independent occurs at only finitely many points of this proper integral curve. At each such point they are not both zero, so at most one member of the pencil is singular there. Excluding those finitely many parameters gives a quartic smooth everywhere along \(C\). \(\square\)

The use of duality in (7.13) supplies a genuine residual scheme. Counting the degrees of set-theoretic components alone would miss embedded or multiple structure and would not justify the conic assertion.

#### A bound on all nearby families

**Lemma 7.6.** In the locus of smooth connected degree-\(14\), genus-\(24\) curves that lie on no singular cubic, every irreducible family has dimension at most \(56\).

**Proof.** Separate curves on smooth cubics from curves on no cubic. For a smooth cubic \(S\), adjunction gives \(\omega_S=\mathcal O_S(-1)\). A curve \(C\subset S\) has
\(\mathcal N_{C/S}=\omega_C(1)\).
Its degree is \(46+14=60\); Serre duality gives zero first cohomology, and (7.11) gives \(h^0=37\). The relative Hilbert tangent formula bounds each family on a fixed \(S\) by \(37\). Smooth cubic surfaces form an open subset of \(\mathbb P^{19}\), so the corresponding flag families have dimension at most \(19+37=56\). Their images in the curve Hilbert scheme have no greater dimension.

Now let \(C\) lie on no cubic. By Lemma 7.5 it lies on a quartic smooth along it and containing a plane conic. Plane conics vary in dimension \(3+5=8\). For a fixed conic \(Q\), restriction of quartic forms to \(Q\) is surjective onto a space of dimension nine: restrict first to its plane, then use
\(0\to\mathcal O_{\mathbb P^2}(2)\to\mathcal O_{\mathbb P^2}(4)\to\mathcal O_Q(4)\to0\).
Thus the quartics through \(Q\) form \(\mathbb P^{25}\). The incidence of quartics and conics has dimension \(8+25=33\), so quartics containing a conic vary in dimension at most \(33\).

Fix one of these quartics \(F\) that is smooth along \(C\). The curve is an effective Cartier divisor on \(F\): it is Cartier near its support by smoothness, and its ideal is the unit ideal away from that support. Quartic adjunction gives \(\omega_F=\mathcal O_F\), even if \(F\) is singular elsewhere. Consequently

\[
\mathcal N_{C/F}=\mathcal O_C(C)=\omega_C,
\qquad h^0(\mathcal N_{C/F})=24.
\]

Every fibre of the flag space of these pairs \((C,F)\) over its quartic parameter therefore has dimension at most \(24\), by the tangent formula. The flag space has dimension at most \(33+24=57\). Over each noncubic \(C\), however, the choices of quartic smooth along \(C\) form a nonempty open subset of \(\mathbb P H^0(\mathcal I_C(4))\), of dimension at least one. Every such quartic contains a residual conic after a second independent quartic is chosen. Forgetting \(F\) therefore lowers the dimension by at least one. The resulting curve families have dimension at most \(56\).

Both cases prove the bound. All spaces used here are finite-type Hilbert or flag loci. The dimension estimates are the fibre-dimension inequality applied to these loci, and tangent dimension bounds actual local dimension; neither an assumed expected dimension nor generic smoothness of the flag map is being used. \(\square\)

#### The cubic-surface family and its extra tangent direction

**Theorem 7.7 (Mumford).** The Hilbert scheme \(\operatorname{Hilb}^{14t-23}(\mathbb P^3_k)\) has a generically nonreduced irreducible component of dimension \(56\). A dense family of its members consists of smooth curves

\[
C\in|D|,\qquad D=4H+2L,
\tag{7.14}
\]

where \(S\subset\mathbb P^3\) is a smooth cubic surface, \(H\) its hyperplane class and \(L\subset S\) a line. Their Hilbert tangent spaces have dimension \(57\).

**Proof.** The line calculation of Section 5 gives \(L^2=-1\). Also \(H^2=3\) and \(H\cdot L=1\). Hence

\[
\begin{gathered}
D\cdot H=14,\qquad D^2=60,\\
(D-H)\cdot D=46.
\end{gathered}
\tag{7.15}
\]

The cubic restriction sequence gives \(H^1(S,\mathcal O_S(mH))=0\) for every integer \(m\), and \(h^0(\mathcal O_S(4H))=35-4=31\). Write \(A_j=\mathcal O_S(4H+jL)\), for \(j=0,1,2\), so \(A_2=\mathcal O_S(D)\). Add the line twice, using

\[
\begin{aligned}
0&\to A_0\to A_1\to\mathcal O_L(3)\to0,\\
0&\to A_1\to A_2\to\mathcal O_L(2)\to0.
\end{aligned}
\tag{7.16}
\]

The line cohomology shows that both first cohomology groups remain zero and that \(h^0(\mathcal O_S(D))=31+4+3=38\). Thus \(|D|\) has dimension \(37\).

We verify the existence of the required smooth connected members. The line bundle \(\mathcal O_S(H+L)\) is globally generated. Away from \(L\), multiply generating hyperplane sections by the section cutting out \(L\); on \(L\), the sequence with quotient \(\mathcal O_L\) is surjective on sections because \(H^1(\mathcal O_S(H))=0\). Since
\(D=2H+2(H+L)\), its line bundle is very ample: the tensor product of a very ample line bundle and a globally generated line bundle is very ample, by taking the graph of their two maps and the Segre embedding. In its projective embedding, hyperplanes tangent at some point of \(S\) form a proper closed subset of the dual projective space. Indeed hyperplanes containing the tangent plane at a fixed point have codimension three, and that point varies in dimension two. General hyperplane sections are therefore smooth.

They are connected as well. From the two sequences obtained by subtracting \(L\) successively from \(-4H\), the quotients on \(L\) are \(\mathcal O_L(-4)\) and \(\mathcal O_L(-3)\). Their sections vanish, and \(H^1(\mathcal O_S(-4H))=0\); thus \(H^1(\mathcal O_S(-D))=0\). The divisor sequence gives \(H^0(C,\mathcal O_C)=k\). A smooth curve with that property is connected and hence integral. Adjunction and (7.15) give \(\deg\omega_C=46\), so its genus is \(24\).

The pairs \((S,L)\) form a nonempty irreducible parameter space of dimension \(19\): lines vary in the four-dimensional Grassmannian, cubics through a fixed line form \(\mathbb P^{15}\), and smoothness cuts out a nonempty open subset. For example a Fermat cubic contains a line over the algebraically closed field. The spaces \(|4H+2L|\) form a projective bundle of relative dimension \(37\), by the vanishing in (7.16) and cohomology and base change. Its smooth connected curve locus is nonempty and open. It is irreducible of dimension \(56\).

Its map to the curve Hilbert scheme has zero-dimensional fibres. A curve of degree \(14\) is contained in at most one irreducible cubic: two distinct ones intersect in degree nine. Lemma 7.5 rules out a reducible cubic containing it. On the same smooth cubic, the equality \(2L\sim2L'\) would force \(L=L'\), since intersecting with \(L\) gives \(-2\) on one side and a nonnegative number on the other for distinct lines. Thus the curve determines its cubic and its line. Let \(W\) be the closure of this family in the Hilbert scheme, with its reduced structure. It is irreducible of dimension \(56\).

The locus of curves contained in a singular cubic is closed: it is the proper image of the closed incidence with the projective discriminant of singular cubics. Our curves are not in it, by uniqueness of their smooth cubic. Restrict also to the open locus of smooth connected curves. Lemma 7.6 bounds all components in this neighbourhood by \(56\), so \(W\) is itself an irreducible component, not a subfamily inside a larger one.

Finally compute its Hilbert tangent dimension. Put \(N=\mathcal N_{C/\mathbb P^3}\), and write \(\mathcal O_C(3)=\mathcal O_C(3H)\) for the hyperplane twist. The normal sequence is

\[
0\to\mathcal O_C(D)\to N
\to\mathcal O_C(3)\to0.
\tag{7.17}
\]

Serre duality and adjunction identify \(H^1(\mathcal O_C(D))\) with the dual of \(H^0(\mathcal O_C(-H))\), which is zero. Formula (7.11) therefore gives \(h^0(\mathcal O_C(D))=60+1-24=37\). Further,

\[
\omega_C(-3H)=\mathcal O_C(2L).
\]

The sequence \(0\to\mathcal O_S(-4H)\to\mathcal O_S(2L)\to\mathcal O_C(2L)\to0\) identifies their section spaces, since the first sheaf has zero zeroth and first cohomology. The only effective divisor in \(|2L|\) is \(2L\): intersection with \(L\) is negative, forcing \(L\) as a component, and the same argument forces it a second time. Thus \(h^0(\mathcal O_C(2L))=1\). Its Euler characteristic is \(42+1-24=19\). It follows that

\[
\begin{aligned}
h^1(\mathcal O_C(3H))&=1,\\
h^0(\mathcal O_C(3H))&=20,\\
h^0(N)&=37+20=57.
\end{aligned}
\tag{7.18}
\]

Sequence (7.17) also gives \(h^1(\mathcal N_{C/\mathbb P^3})=1\). The tangent formula now gives (7.10) on a dense constructible family in \(W\).

Suppose the Hilbert scheme were reduced at the generic point of \(W\). After shrinking around that point and avoiding the other components, it would be a reduced irreducible finite-type scheme. Over a characteristic-zero field such a scheme has a nonempty smooth open subset: its function field is separably generated, so smoothness holds at its generic point and then on a neighbourhood. That open subset would have tangent dimension \(56\). It must meet the dense family just constructed, where the tangent dimension is \(57\), a contradiction. The Hilbert scheme is therefore nonreduced at the generic point of \(W\). \(\square\)

The conclusion uses an actual component bound and a tangent excess persisting on a dense family. It does not assert that every nonzero \(H^1(\mathcal N)\) produces an obstruction, or that every excess tangent at one closed point produces a generically nonreduced component. This is the distinction between the cubic-surface family and the isolated quartic-surface line discussed earlier. The construction is due to Mumford, *Further pathologies in algebraic geometry*, Section II, pp. 643–647.


## 8 Exercises

1. **Basic.** Compute the tangent space of \(\operatorname{Hilb}^1(\mathbb P^n)\) at a rational point and identify it intrinsically.

2. **Intermediate.** Prove (5.1) for a line on a smooth cubic surface and deduce that the Fano scheme is reduced and zero-dimensional. Explain why this does not yet count the lines.

3. **Intermediate.** Compute the tangent space of \(\operatorname{Hilb}^2(\mathbb A^2)\) at \(Z=(y,x^2)\). Describe all its tangent vectors by equations, and check smoothness in every characteristic.

4. **Intermediate.** Prove that a smooth plane conic gives a smooth Hilbert point of dimension five. Include a conic that becomes \(\mathbb P^1\) only after extending the field.

5. **Advanced.** For the small extension (2.1), construct the canonical obstruction class to a flat quotient lift. Prove both directions of its vanishing criterion, describe the set of lifts when it vanishes, and explain why replacing global Ext by \(H^1(\mathcal Hom)\) without a local-lift hypothesis is invalid.

6. **Advanced.** Let \(I=(x^2,xy,y^2)\subset k[x,y]\), so \(B=k[x,y]/I\) has length three. Compute \(\operatorname{Hom}(I,B)\) directly from the two syzygies, and identify all its six parameters. Prove that

\[
k[t,x,y]/(x(x-t),xy,y(y-t))
\]

is free over \(k[t]\), and describe every nonzero fibre. Explain why the special subscheme is not a regular embedding even though its Hilbert point is smooth.

7. **Advanced.** On a smooth cubic surface with line \(L\), replace \(4H+2L\) by \(D'=5H+2L\), and take a general smooth connected member \(C'\). Compute its degree and genus, the dimension of \(|D'|\), and both cohomology dimensions of \(\mathcal N_{C'/\mathbb P^3}\). Show that its Hilbert point is smooth, even though the normal obstruction space has dimension five. Explain why this does not contradict Theorem 7.7.

## 9 Solutions

**1.** Move the point to \([1:0:\cdots:0]\) by a projective coordinate change. On its affine chart the ideal is \((x_1,\ldots,x_n)\), and its conormal space has basis the classes of these \(n\) coordinates. A homomorphism into its quotient \(k\) assigns arbitrary values \(a_1,\ldots,a_n\); its kernel deformation has equations \(x_i+\epsilon a_i\) in convention (1.3). Thus the tangent space is \(k^n\). Intrinsically it is the dual of \(\mathfrak m_p/\mathfrak m_p^2\), namely \(T_p\mathbb P^n\). Its normal sheaf has no higher cohomology because it is supported on one point, so Section 3 proves smoothness of dimension \(n\).

**2.** Put \(L=(x_2=x_3=0)\) and express the cubic as \(x_2a+x_3b\), with \(a,b\) quadratic. Smoothness makes \(a|_L,b|_L\) have no common zero. The surjection \(\mathcal O_L(1)^2\to\mathcal O_L(3)\) has line-bundle kernel of degree \(2-3=-1\). On \(\mathbb P^1\), that kernel is \(\mathcal O(-1)\), with both \(H^0,H^1\) zero. The Hilbert lifting criterion proves a smooth isolated Hilbert point. For the Fano scheme, graph variations of the two-plane give the derivative (5.3); its kernel is \(H^0(\mathcal O(-1))=0\). Its geometric local rings have zero cotangent space and therefore zero maximal ideal by Nakayama. All geometric points are reduced and isolated, and projectivity gives a finite scheme. Reducedness and dimension alone permit any finite number, including zero; the top-Chern calculation of Section 6 is what establishes degree 27.

**3.** In \(k[x,y]\), \(y,x^2\) is a regular sequence: first quotienting by \(y\) gives \(k[x]\), where \(x^2\) is a nonzerodivisor. The conormal module is free over \(B=k[x]/x^2\) on their two classes. Its dual \(B^2\) has \(k\)-basis corresponding to \(1,x\) on each generator. A tangent vector therefore has the four parameters in (7.1), with equations

\[
y+\epsilon(c+dx),\qquad x^2+\epsilon(a+bx).
\]

These equations are a flat lift: the quotient has basis \(1,x\) over the dual numbers, because the first equation eliminates \(y\) and the second is monic in \(x\). Thus every computed tangent vector is realized. Since \(Z\) is finite, \(H^1(N)=0\); the Hilbert scheme is smooth of dimension four. Independently, the open chart with basis \(1,x\) is parametrized by the four coefficients of \(y=c+dx,\ x^2=a+bx\), and is \(\mathbb A^4\). No derivative division is used, so the calculation includes characteristic two.

**4.** A conic is a Cartier divisor with ideal \(\mathcal O(-2)\); hence its conormal bundle is \(\mathcal O_C(-2)\) and its normal bundle is \(\mathcal O_C(2)\). Over an algebraic closure a smooth conic is a projective line with \(\mathcal O_C(1)=\mathcal O_{\mathbb P^1}(2)\), so the normal bundle becomes \(\mathcal O_{\mathbb P^1}(4)\). The line-bundle cohomology formula gives \(h^0=5,\ h^1=0\). An affine Čech complex shows that coherent cohomology commutes with field extension; faithful flatness descends the vanishing, and dimensions over the original field equal those over the extension. Equation (1.4) and Theorem 3.2 now prove smoothness and dimension five over \(k\). As a check, plane degree-two equations up to nonzero scalar form the projective space of dimension five constructed in *Hilbert and Quot schemes*.

**5.** Let \(\pi:E_{A'}\to E_A\), and let \(\widetilde K\) be the inverse image of \(K_A\). The exact sequence \(0\to K\otimes J\to E\otimes J\to G\otimes J\to0\), combined with this inverse image, gives

\[
0\to G\otimes J
\to\widetilde K/(K\otimes J)
\to K_A\to0.
\]

The middle sheaf is killed by \(J\), so it is an extension of \(\mathcal O_{X_A}\)-modules. Its class is the obstruction in (2.4).

If the class is zero, choose a splitting. Its image's inverse image in \(E_{A'}\) is a submodule \(K'\) reducing to \(K_A\) and intersecting \(E\otimes J\) in \(K\otimes J\). Consequently \(G'=E_{A'}/K'\) reduces to \(G_A\), and \(J\otimes_A G_A\to G'\) is injective with image \(JG'\). The square-zero flatness criterion proves flatness. Coherence gives finite presentation, and nilpotent preservation gives proper support. This is a lift in the Quot functor.

If a flat lift exists, its kernel \(K'\) has those same intersection and reduction properties, by tensoring its exact sequence with \(A\) and using flatness. Its image in the obstruction extension maps isomorphically onto \(K_A\), and supplies a splitting. Thus existence implies vanishing as well.

Subtracting two splittings gives exactly a map \(K_A\to G\otimes J\), and every such map changes a splitting. Resolving \(K_A\) by \(A\)-flat sums of negative twists and reducing identifies this Hom group with \(\operatorname{Hom}_X(K,G)\otimes_k J\), and identifies the extension group with \(\operatorname{Ext}^1_X(K,G)\otimes_k J\). This gives the torsor and the stated obstruction space without requiring a locally free \(K\).

Finally a global Ext class can fail to split even on an affine open, where higher cohomology of its coherent Hom sheaf is zero. For an algebraic illustration, on \(\operatorname{Spec}k[x]\) take the modules \(K=G=k[x]/(x)\). The resolution \(0\to k[x]\xrightarrow{x}k[x]\to K\to0\) gives \(\operatorname{Ext}^1(K,G)=k\), although \(H^1(\mathcal Hom(K,G))=0\). This example distinguishes the two groups; it does not claim that these particular modules occur as the kernel and quotient of a specified Hilbert point. When local quotient lifts do exist, local splittings put the obstruction in the \(H^1\) subgroup, exactly as in Section 3.

**6.** The generators \(x^2,xy,y^2\) have syzygies \(y e_0-x e_1\) and \(y e_1-x e_2\). They generate all relations: comparing the coefficient of the largest power of \(x\), or simply cancelling successively among the three monomial generators, reduces every relation to these two. Write their proposed images in \(B\) as \(u_i=\alpha_i+\beta_i x+\gamma_i y\). Since \((x,y)^2B=0\), the two syzygies become

\[
\alpha_0y-\alpha_1x=0,
\qquad \alpha_1y-\alpha_2x=0.
\]

The basis \(1,x,y\) shows that all three \(\alpha_i\) vanish. The six coefficients \(\beta_i,\gamma_i\) are unrestricted, proving the tangent dimension is six. The family has generators (7.6) for \(\lambda=(2,1)\), with both lists of constants beginning \(0,1\). Reducing \(x^2\) to \(tx\), \(y^2\) to \(ty\), and \(xy\) to zero shows that \(1,x,y\) generate the quotient. At \(t=c\ne0\), evaluation at \((0,0),(c,0),(0,c)\) makes them a basis; the determinant of that evaluation matrix is \(c^2\ne0\). Passing to \(k(t)\) proves that a polynomial relation between these three classes is zero, hence that they form a free \(k[t]\)-basis. The nonzero fibres are exactly those three reduced points, in every characteristic. At the origin \(I/\mathfrak m I\) has the three independent degree-two classes, so the ideal cannot be generated by a regular sequence of length two. Theorem 7.4 nevertheless makes its Hilbert point smooth of dimension six.

**7.** Put \(N'=\mathcal N_{C'/\mathbb P^3}\). The same intersection calculation gives

\[
\begin{gathered}
(D')^2=91,\qquad H\cdot D'=17,\\
2g(C')-2=(D'-H)\cdot D'=74.
\end{gathered}
\]

Thus \(\deg C'=17\) and \(g(C')=38\). The two line sequences now have quotients \(\mathcal O_L(4)\) and \(\mathcal O_L(3)\). Since \(h^0(\mathcal O_S(5H))=56-10=46\), they give \(h^0(\mathcal O_S(D'))=46+5+4=55\), with zero first cohomology. The complete linear system has dimension \(54\). Its general member is smooth and connected by the same very-ampleness and negative-divisor arguments as in Theorem 7.7.

The inner normal bundle has degree \(91\), zero first cohomology and \(54\) sections. For the outer normal term, adjunction gives \(\omega_{C'}(-3H)=\mathcal O_{C'}(H+2L)\). The section space of the latter equals that of \(\mathcal O_S(H+2L)\), by the sequence with kernel \(\mathcal O_S(-4H)\). Adding \(L\) to \(H\) gives a quotient \(\mathcal O_L\), hence five sections and zero first cohomology. Adding it a second time gives \(\mathcal O_L(-1)\), which has neither zeroth nor first cohomology. The Euler characteristic of \(\mathcal O_{C'}(3H)\) is \(51+1-38=14\). Therefore

\[
\begin{aligned}
h^1(\mathcal O_{C'}(3H))&=5,\\
h^0(\mathcal O_{C'}(3H))&=19,\\
h^0(N')&=54+19=73,\\
h^1(N')&=5.
\end{aligned}
\]

The flags consisting of a smooth cubic, a line and such a curve form an irreducible family of dimension \(19+54=73\). A curve of degree \(17>9\) determines its cubic, and the line is unique by the same negative-intersection argument. The image therefore has dimension \(73\). Its closure passes through \([C']\), so local dimension there is at least \(73\), while the tangent computation bounds it above by \(73\). The local ring is regular, and over the algebraically closed field the Hilbert scheme is smooth at \([C']\). The five-dimensional obstruction space does not force any nonzero obstruction. Here the cubic family already fills the tangent dimension; for \(4H+2L\) it was one dimension smaller.

## What this lesson does not prove

The tangent formula, the complete Ext obstruction and its lifting torsor, the regular-embedding gluing obstruction, the dimension estimate, the normal calculations, the 27-line count, Fogarty's surface theorem and Mumford's nonreduced component are proved here.

We use these foundational results with their indicated hypotheses:

- Faithful flatness and the local criterion for flatness, Lemma 4.3 proves the flatness criterion used here over an arbitrary square-zero base \(A'\to A\) with ideal \(J\) [Stacks, Tag 08MQ]. If \(N/JN\) is \(A\)-flat, the Tor sequence identifies \(\operatorname{Tor}_1^{A'}(A,N)\) with the kernel of \(J\otimes_A(N/JN)\to N\). When that multiplication map is injective, Lemma 4.3 kills \(\operatorname{Tor}_1^{A'}(P,N)\) for every \(P\), since \(J^2P=0\); hence \(N\) is flat. The converse follows by tensoring the ideal sequence. This covers arbitrary modules and the arbitrary-base split calculation (1.5). The Yoneda and quasi-coherence arguments are in Deformations of rings and schemes and the naive cotangent complex, Section 5.
- Every local equation lift in Lemma 3.1 and its relative version is over a local Artinian ring, with a Noetherian ambient algebra. Faithful flatness and the local criterion for flatness, Corollary 5.3 proves that lifts of a regular sequence in the closed fibre remain regular and give a flat quotient [Stacks, Tag 0CEQ]. Lemma 3.A proves the pointwise Artinian smoothness criterion, using the Jacobian lifting argument of Formally smooth, unramified and étale ring maps, Theorem 4.1 [Stacks, Tag 02HX].
- Čech cohomology, Theorem 3.2 proves the affine-cover comparison [Stacks, Tag 01XD]; Deformations of rings and schemes and the naive cotangent complex, Theorem 7.1 proves the affine diagonal criterion. The theorem on formal functions, Lemma 5.4 supplies affineness and properness through the nilpotent thickenings used here [Stacks, Tags 06AD and 0BPG]. Zariski's Main Theorem, Theorem 5.1 proves proper quasi-finite morphisms finite [Stacks, Tag 02LS].
- Noetherian and Artinian rings, Theorem 5.1 and Solution 7.3 supplies Artin–Rees and Noetherianity of finite-variable power-series rings [Stacks, Tag 00IN]. Dimension theory of Noetherian local rings, Theorems 2.1 and 3.2 and Proposition 4.2 proves the parameter-count, one-equation and embedding-dimension inequalities [Stacks, Tags 00KW and 00KQ]. Completion, Theorem 4.1 proves invariance of dimension and regularity [Stacks, Tag 07NV]. Regular local rings, Theorem 1.1 and Proposition 1.4 gives the regular-parameter and regular-quotient facts used in Sections 5–6.
- Cohomology of projective space, Theorems 2.2 and 5.2 proves the twist and projective-bundle calculations [Stacks, Tag 01XT]. Weil divisors and the class group, Theorem 4.2 proves \(\operatorname{Pic}(\mathbf P^1)=\mathbf Z\) [Stacks, Tag 0BXJ]. Proper morphisms and coherent direct images, Theorem 5.1 gives finite-dimensional proper cohomology [Stacks, Tag 02O6]. Serre's theorems on projective schemes, Lemma 1.1 and the ample-generation argument in Section 1 supplies the negative-twist resolutions on quasi-projective schemes used to compute global Ext in Section 2.
- Lemma 6.A proves the Koszul zero-scheme degree, splitting calculation and integral relations actually used in (6.1)–(6.4), including every characteristic. Its finite-difference and divisor-restriction inputs are Intersection numbers of line bundles, Sections 1–2, and the two projective-bundle vanishings are Cohomology of projective space, Theorem 5.2. The Chern notation retains the standard source references [Stacks, Tags 02UI, 02UL and 0FA9]; the line count needs no external intersection-theory proof.

Theorem 7.4 proves the full smooth-surface assertion, including its component argument and arbitrary characteristic. Theorem 7.7 proves Mumford's generically nonreduced component in characteristic zero: its residual-conic argument and flag dimensions are part of the proof. The cohomology, closed-immersion duality and adjunction it uses have exact earlier programme proofs linked at the start of that construction.

## References

- Grothendieck, *Techniques de construction et théorèmes d'existence en géométrie algébrique IV: les schémas de Hilbert*, Séminaire Bourbaki, Exposé 221, §5, Proposition 5.1 and Corollaries 5.2–5.4, pp. 269–271. [Original text](https://www.numdam.org/item/SB_1960-1961__6__249_0/).
- The Stacks project, *Quot and Hilbert spaces* and *Deformation Theory*. The tagged foundational results are read in the AI Integrated Stacks Project edition. [Quot and Hilbert spaces](https://stacks.math.columbia.edu/tag/082L).
- AI Integrated Stacks Project, *Quot*, [cotangent-space formula](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/quot.html#lemma-cotangent-space-quot) and [quotient-lift torsor](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/quot.html#lemma-quotient-lifts-torsor); *Moduli*, [regular-embedding Hilbert criterion](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/moduli.html#proposition-hilbert-lci-tangent-smooth).
- Bertin, *The punctual Hilbert scheme: an introduction*, lecture notes of the summer school in Grenoble, June 16 – July 12, 2008, Section 3.1, Theorem 3.1. [Lecture notes](https://www-fourier.univ-grenoble-alpes.fr/sites/default/files/bertin_rev.pdf).
- Mumford, *Further pathologies in algebraic geometry*, American Journal of Mathematics **84** (1962), pp. 642–648, Section II. [Original paper](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1962b--Path2-JS.pdf).
