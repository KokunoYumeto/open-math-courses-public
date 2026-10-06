# Tangent spaces and obstructions for Hilbert and Quot schemes

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A quotient can change infinitesimally even when its source stays fixed. Its kernel records that change: moving a relation produces an element of the quotient. This gives the tangent space of Quot. Over a thicker base, the same relations may fail to fit together, and that failure is an extension class.

We construct the class and prove its exact lifting criterion. For a regular embedding, equations lift locally, so the remaining obstruction is the failure of the local lifts to agree. That failure lies in the first cohomology of the normal bundle. We then turn this obstruction space into a bound on the number of local equations of the Hilbert scheme. Applications distinguish a possible obstruction space from an obstruction that actually occurs: a line on a smooth quartic surface has a nonzero obstruction space and still gives a reduced isolated point. For a smooth cubic surface, a separate intersection calculation counts its 27 lines.

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
K_\phi=
\{\,k+\epsilon e:k\in K,\ e\in E,\ q(e)=\phi(k)\,\}.
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
T_{[Z]}\operatorname{Hilb}_{X/k}
=\operatorname{Hom}_X(\mathcal I_Z,\mathcal O_Z)
=H^0(Z,\mathcal N_{Z/X}).
\tag{1.4}
\]

The last formula holds for every closed subscheme. For a **regular embedding**, the conormal sheaf is finite locally free and \(\mathcal N_{Z/X}\) is the normal bundle. Without regularity it is a normal sheaf, and the local lifting argument in Section 3 need not hold.

Here is the relative tangent formula once, in a form that fixes its scope. If a \(T\)-point \(g\) of a represented relative Quot functor has kernel \(K\) and quotient \(G\), and \(M\) is quasi-coherent on \(T\), split thickenings \(T[M]\) give

\[
\operatorname{Hom}_T(g^*\Omega_{\operatorname{Quot}/S},M)
=\operatorname{Hom}_{X_T}(K,G\otimes_T M).
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
o(G_A,A')\in
\operatorname{Ext}^1_{X_A}(K_A,G\otimes_k J)
=\operatorname{Ext}^1_X(K,G)\otimes_k J.
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
K'\cap(E\otimes_k J)=K\otimes_k J,\qquad
K'\longrightarrow K_A\text{ is surjective}.
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

**Theorem 3.2.** The class (3.1) vanishes if and only if a global embedded lift exists. When it vanishes, the global lifts form a torsor under \(H^0(Z,N)\otimes_k J\). In particular, if \(H^1(Z,N)=0\), the Hilbert scheme is smooth at \([Z]\), of dimension \(h^0(Z,N)\).

**Proof.** A zero class allows sections \(\beta_i\) whose changes make every \(\alpha_{ij}\) zero. The adjusted quotient kernels then agree on all intersections, and glue to a coherent ideal in \(\mathcal O_{X_{A'}}\). Its quotient is flat because flatness is local, and is proper by preservation of properness through a nilpotent thickening [Stacks, Tag 0BPG]. It gives a Hilbert point. Conversely a global lift, restricted to the cover, makes the cocycle zero, and comparing with it shows that any original cocycle is a coboundary.

Two global lifts differ by a compatible collection of local difference sections, hence by one section of \(N\otimes_k J\); every section changes a lift. This proves the torsor assertion. It also proves naturality of (3.1) under linear maps of \(J\).

If \(H^1(Z,N)=0\), every small-extension diagram centred at \([Z]\) lifts. The Hilbert scheme is locally of finite type, and the pointwise Artinian lifting criterion [Stacks, Tag 02HX] proves smoothness. For its dimension, a smooth local scheme at a \(k\)-point has dimension equal to its tangent-space dimension. Equation (1.4) gives that dimension as \(h^0(Z,N)\). \(\square\)

The class (3.1) maps to (2.4). To see the comparison without replacing global Ext by sheaf Ext, take local splittings of (2.3). Their differences are exactly the sections \(\alpha_{ij}\). Gluing the locally split extensions with these differences reconstructs (2.3). Thus its extension class is the image of the Čech class under the map \(H^1(\mathcal Hom(K,G))\to\operatorname{Ext}^1(K,G)\). For regular embeddings local lifts exist, so this is the whole obstruction that is needed.

The relative smoothness assertion holds with a flat quasi-projective \(X/S\) over a Noetherian base and a proper regular embedding \(Z\subset X_K\), where \(K\) is the residue field of the Hilbert point. The preceding equation-lifting proof uses flatness and finite presentation of the ambient algebra, rather than smoothness itself: for each Artinian diagram over \(S\), apply Tag 0CEQ to that diagram's flat ambient algebra and its regular special-fibre equations. The normal sheaf is still locally free. Properness of a family persists through the nilpotent extension [Stacks, Tag 0BPG], and the relative criterion in Tag 02HX applies. Thus \(H^1(Z,N)=0\) gives smoothness over \(S\) at that point.

## 4 Why an obstruction space bounds dimension

Let \(H\) be a locally finite-type \(k\)-scheme, \(h\) a \(k\)-point, and suppose its centred deformation functor has a **complete obstruction space** \(O\): for every small extension with kernel \(J\), there is a class in \(O\otimes_k J\), natural under linear pushouts of \(J\), whose vanishing is equivalent to existence of a lift. Assume \(O\) is finite-dimensional.

**Proposition 4.1.** If \(t=\dim_k T_{H,h}\), then

\[
t-\dim_k O\leq\dim_h H\leq t.
\tag{4.1}
\]

**Proof.** Let \(R=\widehat{\mathcal O}_{H,h}\), with residue field \(k\). Choose lifts of a basis of its cotangent space. Successive approximation in its maximal-ideal powers gives a surjection

\[
S=k[[x_1,\ldots,x_t]]\longrightarrow R=S/L,
\qquad L\subset\mathfrak n^2.
\tag{4.2}
\]

For clarity, the approximation works because the chosen elements generate the maximal ideal by Nakayama. Every element of \(R\) can successively be matched by a constant and homogeneous polynomials in those generators, with remainders in successive powers; completeness sums the polynomials to a power series. The basis property makes the kernel have no linear term. Since \(S\) is Noetherian, \(V=L/\mathfrak n L\) is finite-dimensional. Put \(r=\dim_k V\); Nakayama says that \(L\) is generated by \(r\) elements.

For all sufficiently large \(n\), Artin–Rees [Stacks, Tag 00IN] gives \(L\cap\mathfrak n^n\subset\mathfrak n L\). Thus

\[
A'=S/(\mathfrak n L+\mathfrak n^n)
\longrightarrow A=S/(L+\mathfrak n^n)
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
h^0(Z,N)-h^1(Z,N)
\leq\dim_{[Z]}\operatorname{Hilb}_{X/k}
\leq h^0(Z,N).
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
0\longrightarrow N_{L/S_d}
\longrightarrow\mathcal O_L(1)^{\oplus2}
\xrightarrow{\partial f}\mathcal O_L(d)
\longrightarrow0.
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

**Theorem 6.1.** Over an algebraically closed field of any characteristic, a smooth cubic surface has exactly 27 lines. Over any field, its Fano scheme is finite étale of degree 27.

**Proof.** Let \(B=\operatorname{Gr}(2,k^4)\), which is smooth projective of dimension four. Put \(W=\operatorname{Sym}^3 U^\vee\), of rank four. The cubic's Fano scheme \(F\) is \(Z(s_f)\). Section 5 shows that at every geometric zero the derivative \(T_B\to W\) is injective, hence is an isomorphism between two four-dimensional spaces. Its four local equations are therefore a regular sequence and the zero is reduced. Since all zeros are isolated, the top-Chern-class formula [Stacks, Tag 0FA9] gives

\[
\deg F=\int_B c_4(W).
\tag{6.1}
\]

The formula includes the possibility of an empty zero scheme; the following nonzero calculation will rule it out.

We compute this integral using only Chern-class additivity, the splitting principle, and the geometric zero loci of two sections. These foundational intersection identities are in [Stacks, Tags 02UI, 02UL and 0FA9]. Pull back to the flag bundle on which \(U^\vee\) has line-bundle quotients of first Chern classes \(x,y\). Pullback on Chow groups is injective, so symmetric identities established there hold on \(B\).

The induced filtration on \(\operatorname{Sym}^3 U^\vee\) has line-bundle factors with first Chern classes

\[
3x,\qquad 2x+y,\qquad x+2y,\qquad 3y.
\]

The filtration comes from sorting the monomials in a local basis adapted to the line subbundle; changing the adapted basis preserves the resulting filtration. It is valid in every characteristic. Hence

\[
c_4(W)
=9xy(2x+y)(x+2y)
=18(x^3y+xy^3)+45x^2y^2.
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

For context we state two precisely delimited inputs without reproducing their proofs.

- **Fogarty's theorem.** If \(X\) is a smooth irreducible quasi-projective surface over an algebraically closed field, \(\operatorname{Hilb}^d(X)\) is smooth and irreducible of dimension \(2d\). Fogarty proved this in 1968. Theorem 3.1 of José Bertin's lecture notes *The punctual Hilbert scheme: an introduction* states that for a smooth connected surface over an algebraically closed field this Hilbert scheme is connected and smooth of dimension \(2d\), and the notes reproduce Fogarty's proof. The proof identifies the unique component containing reduced configurations. For the quasi-projective version, the Hilbert–Chow map on the reduced Hilbert scheme over \(\operatorname{Sym}^d X\) is proper, with connected fibres (Proposition 2.27 of the notes). Thus the Hilbert scheme is connected. The tangent bound (3.3) of the notes applies at every point. The component containing distinct configurations has dimension \(2d\), so this bound makes the whole Hilbert scheme smooth at all its points and prevents intersection with any other component. This component is both open and closed; connectedness makes it the whole scheme. This argument includes every characteristic; the notes prove the linearized-determinant lemma used to construct the Hilbert–Chow map when \(d!\) is invertible in the base field, and leave the general case as Exercise 2.9.
- **Mumford's example.** In characteristic zero, \(\operatorname{Hilb}^{14t-23}(\mathbb P^3)\) has a generically nonreduced component whose general member is a smooth curve of degree 14 and genus 24. In *Further pathologies in algebraic geometry*, Section II, pp. 643–647, Mumford constructs curves in the class \(4H+2L\) on a smooth cubic surface, where \(H\) is the hyperplane class and \(L\) a line. The relevant reduced family has dimension 56, while the general tangent space has dimension 57. The discrepancy is proved to persist at the generic point. We use this as a warning, not as a proof that every nonzero \(H^1(N)\) makes a Hilbert scheme nonreduced.

For \(d=2\), the surface assertion also follows from the explicit local charts proved in *Hilbert and Quot schemes*. For higher \(d\), arbitrary finite subschemes of a surface need not be regular embeddings, so the vanishing criterion of Section 3 alone is not a proof of Fogarty's theorem.

## 8 Exercises

1. **Basic.** Compute the tangent space of \(\operatorname{Hilb}^1(\mathbb P^n)\) at a rational point and identify it intrinsically.

2. **Intermediate.** Prove (5.1) for a line on a smooth cubic surface and deduce that the Fano scheme is reduced and zero-dimensional. Explain why this does not yet count the lines.

3. **Intermediate.** Compute the tangent space of \(\operatorname{Hilb}^2(\mathbb A^2)\) at \(Z=(y,x^2)\). Describe all its tangent vectors by equations, and check smoothness in every characteristic.

4. **Intermediate.** Prove that a smooth plane conic gives a smooth Hilbert point of dimension five. Include a conic that becomes \(\mathbb P^1\) only after extending the field.

5. **Advanced.** For the small extension (2.1), construct the canonical obstruction class to a flat quotient lift. Prove both directions of its vanishing criterion, describe the set of lifts when it vanishes, and explain why replacing global Ext by \(H^1(\mathcal Hom)\) without a local-lift hypothesis is invalid.

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

## What this lesson does not prove

The tangent formula, the complete Ext obstruction and its lifting torsor, the regular-embedding gluing obstruction, the dimension estimate, the normal calculations and the 27-line count are proved here.

We use these foundational results with their indicated hypotheses:

- The flatness criterion for a module over a square-zero extension: when its reduction is flat, multiplication from the extension ideal tensor the reduction must be injective onto the ideal multiple [Stacks, Tag 08MQ]. The preceding deformation lesson proves its dual-number case.
- A flat finitely presented algebra cut by lifts of a quasi-regular sequence over a nilpotent reduction has flat quotient if the reduced quotient is flat [Stacks, Tag 0CEQ]. This supplies the local equation lifts; no global unobstructedness is imported.
- Affine-cover Čech cohomology for quasi-coherent sheaves [Stacks, Tag 01XD], the pointwise Artinian criterion for smoothness of a locally finite-type morphism over a locally Noetherian base [Stacks, Tag 02HX], preservation of properness across nilpotent thickenings [Stacks, Tag 0BPG], and finiteness of proper morphisms with finite fibres [Stacks, Tag 02LS].
- Artin–Rees for finite modules over a Noetherian ring [Stacks, Tag 00IN], the one-equation dimension inequality [Stacks, Tag 00KW], the bound by generators of an ideal of definition [Stacks, Tag 00KQ], and preservation of dimension by completion [Stacks, Tag 07NV].
- Line-bundle cohomology on projective space [Stacks, Tag 01XT], \(\operatorname{Pic}(\mathbb P^1)=\mathbb Z\) [Stacks, Tag 0BXJ], and finite-dimensional coherent cohomology on a proper scheme over a field [Stacks, Tag 02O6]. Section 2 explains how the last fact implies the needed Hom and Ext finiteness.
- Chern-class additivity and the splitting principle [Stacks, Tags 02UI and 02UL], and the formula identifying the top Chern class with the cycle of a regular section's zero scheme of the expected codimension [Stacks, Tag 0FA9]. Section 6 proves the Grassmannian integral it needs rather than importing the number 27.

Fogarty's general theorem and Mumford's generically nonreduced example are the two stated external geometric results in Section 7. Their full proofs are not supplied here. The local complete-intersection criterion does not encompass arbitrary finite subschemes of a smooth surface.

## References

- Grothendieck, *Techniques de construction et théorèmes d'existence en géométrie algébrique IV: les schémas de Hilbert*, Séminaire Bourbaki, Exposé 221, §5, Proposition 5.1 and Corollaries 5.2–5.4, pp. 269–271. [Original text](https://www.numdam.org/item/SB_1960-1961__6__249_0/).
- The Stacks project, *Quot and Hilbert spaces* and *Deformation Theory*. The tagged foundational results are read in the AI Integrated Stacks Project edition. [Quot and Hilbert spaces](https://stacks.math.columbia.edu/tag/082L).
- AI Integrated Stacks Project, *Quot*, [cotangent-space formula](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/quot.html#lemma-cotangent-space-quot) and [quotient-lift torsor](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/quot.html#lemma-quotient-lifts-torsor); *Moduli*, [regular-embedding Hilbert criterion](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/moduli.html#proposition-hilbert-lci-tangent-smooth). These AI-written additions have not been reviewed by the Stacks project maintainers.
- Bertin, *The punctual Hilbert scheme: an introduction*, lecture notes of the summer school in Grenoble, June 16 – July 12, 2008, Section 3.1, Theorem 3.1. [Lecture notes](https://www-fourier.univ-grenoble-alpes.fr/sites/default/files/bertin_rev.pdf).
- Mumford, *Further pathologies in algebraic geometry*, American Journal of Mathematics **84** (1962), pp. 642–648, Section II. [Original paper](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1962b--Path2-JS.pdf).
