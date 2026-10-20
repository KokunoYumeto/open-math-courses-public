# Nearby and vanishing cycles

*AI-generated exposition by GPT-6.1 Sol and GPT-6 Astra (OpenAI), October 2026. Public domain (CC0).*

What must be added to a local system to extend it across a puncture? Its monodromy already determines the cohomology around the missing point. The new choice is how the actual stalk maps to that boundary cohomology. We begin with this map. It leads to two vector spaces and two arrows, from which stalks, costalks and every extension can be calculated. Only after those computations will we identify the spaces as nearby and vanishing cycles and pass to functions with larger zero fibres.

The preceding [gluing lesson](gluing-t-structures.md#appendix-b-the-sheaf-model-behind-the-puncture-diagrams) supplies the actual sheaf attaching construction and its mapping complexes. We also use the support tests and finite-length arguments of [The perverse t-structure](the-perverse-t-structure.md). The general-function argument requires the affine bounds of [Lesson 5](affine-morphisms-artin-vanishing-and-perverse-cohomology.md), including the unresolved classical and adic inputs stated there. The free texts of Reich and Beilinson listed at the end supply the general gluing comparison; Illusie, Deligne and Lu–Zheng supply the arithmetic statements and distinctions examined in the appendices.

The disc calculations use a characteristic-zero field \(\Lambda\). Arithmetic cycles use \(\overline{\mathbb Q}_\ell\), with \(\ell\) invertible on the base, and retain full continuous inertia. A shift satisfies \(\mathcal H^q(K[r])=\mathcal H^{q+r}K\). All disc matrices use positive geometric monodromy and the sign \(T-1\).

## 1. Recover an extension from its boundary map

Let \(j:D^*\hookrightarrow D\) be a punctured complex disc and \(i:\{0\}\hookrightarrow D\). A local system \(L\) on \(D^*\) is specified by a finite-dimensional fibre \(V\) and an invertible operator \(T\). Put \(N=T-1\). The angular-cover computation in the first lesson identifies

\[
B=i^*Rj_*L[1]=[V\xrightarrow{N}V]
\quad\text{in degrees }-1,0.
\tag{1.1}
\]

An extension has a stalk complex \(A\) and an attaching map \(a:A\to B\). Appendix B of the gluing lesson proves, on actual sheaf resolutions, the reconstruction

\[
K(A,a)=\operatorname{Fib}\left(
Rj_*L[1]\oplus i_*A\xrightarrow{\mathrm{res}-i_*a}i_*B
\right).
\tag{1.2}
\]

It also proves that its stalk is \(A\), its costalk is \(\operatorname{Fib}(a)\), and a map of attaching data must retain the homotopy in its attaching square. Those facts include the derived mapping-complex comparison; no general-cycle theorem is needed on this disc.

The perverse conditions are \(A\in D^{\le0}\) and \(\operatorname{Fib}(a)\in D^{\ge0}\). The long exact sequence with (1.1) forces \(A\) to have degrees only \(-1,0\) and makes \(H^{-1}(a)\) injective. Choose a two-term representative
\(A=[E\xrightarrow d F]\), with \(a=(a_{-1},a_0)\). Its equations are

\[
a_0d=Na_{-1},\qquad \ker d\cap\ker a_{-1}=0.
\tag{1.3}
\]

One quotient replaces these data by a factorization of \(N\). Set

\[
W=(F\oplus V)/\{(dx,-a_{-1}x):x\in E\},\qquad
u(y)=[0,y],\qquad v[z,y]=a_0z+Ny.
\tag{1.4}
\]

The relation in (1.3) makes \(v\) well defined, and \(vu=N\). The map from \([E\to F]\) to \([V\xrightarrow uW]\) is \(a_{-1}\) in degree minus one and \(z\mapsto[z,0]\) in degree zero. It respects both differentials and attaching maps. On cokernels it is the identification \(F/dE=W/uV\). On kernels, \([0,y]=0\) says that \(y=-a_{-1}x\) for some \(x\in\ker d\); injectivity in (1.3), with \(-x\) in place of \(x\), proves that its kernel map is also an isomorphism. Thus it is a quasi-isomorphism of attaching data.

We have obtained the normal form

\[
V\xrightarrow uW\xrightarrow vV,\qquad T=1_V+vu\text{ invertible},
\quad A=[V\xrightarrow uW],\quad a=(1,v).
\tag{1.5}
\]

Conversely, start with any diagram (1.5), construct the local system with monodromy \(T\), and use (1.2). With the fibre convention of the earlier appendix, its costalk is the complex
\(V\to W\oplus V\to V\), with maps \(x\mapsto(ux,x)\) and \((w,y)\mapsto vw-Ny\), in degrees \(-1,0,1\). Replacing \((w,y)\) by \((w-uy,y)\) cancels an identity complex. The remaining costalk is \([W\xrightarrow vV]\) in degrees \(0,1\). The stalk has degrees \(-1,0\), so both perverse tests hold. In particular,

\[
\begin{array}{ll}
H^{-1}(i^*K)=\ker u,&H^0(i^*K)=\operatorname{coker}u,\\
H^0(i^!K)=\ker v,&H^1(i^!K)=\operatorname{coker}v.
\end{array}
\tag{1.6}
\]

**Theorem 1.1 (disc category).** These constructions give an equivalence between perverse sheaves on \(D\) constructible for \(D^*,\{0\}\) and diagrams (1.5). Morphisms are pairs \((b,c)\) such that \(cu=u'b\) and \(v'c=bv\). Kernels and cokernels are componentwise.

**Proof of the morphism assertion.** Essential surjectivity was proved by (1.4). For full faithfulness, use the mapping complex already justified in the earlier gluing lesson, Appendix B.3–B.4. A degree-zero cocycle between the normal forms consists of a monodromy intertwiner \(b\), a stalk chain map \((g_{-1},g_0)\), and a homotopy \(h:W\to V'\). Its equations reduce to

\[
b-g_{-1}=hu,\qquad bv-v'g_0=N'h,\qquad
g_0u=u'g_{-1}.
\tag{1.7}
\]

Changing the homotopy by \(r:W\to V'\) changes the last three entries by \((ru,u'r,-r)\). Thus there is a unique representative with \(h=0\); its second component is \(c=g_0+u'h\), and the equations become exactly the two displayed commuting relations. Every such pair supplies that representative, and the block maps of the earlier mapping complex show that composition is the composition of pairs. That appendix proves why positive open Ext groups do not invalidate this degree-zero computation. We have not replaced the entire derived Hom complex by ordinary Hom.

The pair \((b,c)\) also intertwines \(1+vu\) and \(1+uv\). The latter is invertible, since

\[
(1_W+uv)^{-1}=1_W-u(1_V+vu)^{-1}v.
\tag{1.8}
\]

Multiplying on either side verifies (1.8), using \((1+uv)u=u(1+vu)\) and \(v(1+uv)=(1+vu)v\). The inverses preserve kernels and images of any morphism. Componentwise kernels and cokernels therefore remain in the diagram category and have their usual universal properties. This makes the equivalence abelian. \(\square\)

Exactly the same proof applies to the whole plane stratified by \(\mathbb C^*,\{0\}\): the punctured local-system category and the boundary complex are the same.

## 2. Read the standard extensions and a connection

The two arrows now make the standard objects explicit. In the table, \(L\) has fibre \(V\) and \(N=T-1\).

| Object | First space | Second space | \(u\) | \(v\) |
|---|---|---|---|---|
| \(\Lambda_D[1]\) | \(\Lambda\) | \(0\) | \(0\) | \(0\) |
| \(i_*E\) | \(0\) | \(E\) | \(0\) | \(0\) |
| \(j_!L[1]\) | \(V\) | \(V\) | \(1\) | \(N\) |
| \(Rj_*L[1]\) | \(V\) | \(V\) | \(N\) | \(1\) |
| \(j_{!*}L[1]\) | \(V\) | \(NV\) | \(N:V\to NV\) | Inclusion |

The constant shifted sheaf has stalk \(\Lambda[1]\) and costalk \(\Lambda[-1]\); (1.6) gives its first row. A point-supported sheaf has no open part and has the same degree-zero stalk and costalk, giving the second. The third row has acyclic stalk and hence is extension by zero; the fourth has acyclic costalk and hence is direct image. Their membership in the heart follows from the direct point tests, without invoking general Artin vanishing.

For the final row, a boundary quotient of an extension is detected by \(H^0i^*K=\operatorname{coker}u\), and a boundary subobject by \(H^0i^!K=\ker v\). Their absence says that \(u\) is onto and \(v\) is one-to-one. Then \(v\) identifies the second space with \(vuV=NV\). Conversely those two conditions hold for the displayed row. The intermediate-extension characterization in the gluing lesson proves it is \(j_{!*}L[1]\).

There is a second useful verification. The canonical map from extension by zero to direct image is \((1_V,N)\); it is the unique adjunction map restricting to the identity on the puncture. Its componentwise image is the final row. Its kernel and cokernel give

\[
0\to i_*\ker N\to j_!L[1]\to j_{!*}L[1]\to0,
\qquad
0\to j_{!*}L[1]\to Rj_*L[1]\to i_*\operatorname{coker}N\to0.
\tag{2.1}
\]

If \(N=0\), intermediate extension has no second space. If \(N\) is invertible, all three extensions coincide, with zero boundary stalk and costalk. For the rank-two block

\[
Ne_2=e_1,\qquad Ne_1=0,
\qquad T=\begin{pmatrix}1&1\\0&1\end{pmatrix},
\tag{2.2}
\]

intermediate extension has second space \(\Lambda w\), with \(ue_2=w\), \(ue_1=0\), \(vw=e_1\). Thus \(uv=0\): its second monodromy is trivial even though its second space is nonzero. The stalk group is \(\Lambda e_1\) in degree minus one, and the costalk group is \(V/\Lambda e_1\) in degree one.

To compare the matrices with connections, write on \(D^*\)

\[
\nabla=d-A\,\frac{dz}{z}.
\tag{2.3}
\]

On a logarithm branch, the equation \(ds=A s\,dz/z\) has the fundamental solution \(s=\exp(A\log z)c\). Differentiating the convergent matrix-exponential series verifies the equation; its inverse is \(\exp(-A\log z)\), so every horizontal section has this form. Positive continuation adds \(2\pi i\) to the logarithm and gives \(T=\exp(2\pi iA)\). Consequently the factorization relation is \(vu=\exp(2\pi iA)-1\), and the residue of the written connection is \(-A\). In (2.2), take \(A=N/(2\pi i)\), since the exponential truncates at \(N^2=0\).

The comparison with the D-module programme requires its regular Riemann–Hilbert theorem: the covariant normalized de Rham convention places the horizontal system in degree minus one, and the five extensions then have the five rows above. The contravariant solution convention instead dualizes the system, giving \(T^{-\mathsf t}\). The differential-equation computation just made is a proof of the monodromy formula; it is not a proof of the full Riemann–Hilbert equivalence, whose exact earlier provider remains an obligation.

## 3. Classify every indecomposable with nearby rank two

At this stage the classification is finite-dimensional algebra. Give \(M=V\oplus W\) the parity with \(V\) even and \(W\) odd, and let

\[
q|_V=u,\qquad q|_W=v.
\tag{3.1}
\]

If \(\dim V=2\) and \(1+vu\) is unipotent, then \((vu)^2=0\). Hence \(q^5=0\) on both summands: on \(V\) it is \(u(vu)^2\), and on \(W\) it is \((vu)^2v\). A splitting of the original diagram is exactly a graded splitting commuting with \(q\).

**Lemma 3.1.** A nilpotent odd operator on a finite-dimensional graded vector space is a direct sum of alternating homogeneous chains. A single chain is indecomposable as a graded module.

**Proof by explicit projections.** Choose the largest \(r\) with \(q^{r-1}a\ne0\) for some homogeneous \(a\), so \(q^r=0\). The vectors \(a,qa,\ldots,q^{r-1}a\) are independent: in a relation, apply the power of \(q\) which sends its first nonzero coefficient to the last vector. Choose a homogeneous functional \(\lambda\) which is one on \(q^{r-1}a\) and zero on the earlier chain vectors. Such a functional exists by extending the homogeneous independent vectors to a graded basis. Define

\[
p(x)=\sum_{j=0}^{r-1}\lambda(q^{r-1-j}x)q^ja.
\tag{3.2}
\]

Its parity is zero: a nonzero coefficient forces the parity of \(x\) to be the parity of \(q^ja\). Its restriction to the chain is the identity. Moreover \(p(qx)=qp(x)\): shift the summation index, noting that the term with \(q^rx\) and the term with \(q^ra\) vanish. Thus \(p\) is a graded commuting projection. Its kernel is a smaller graded \(q\)-module. Repeat there to split all chains.

On a chain of length \(r\), a commuting endomorphism is determined by the image of its first vector, hence is a polynomial in \(q\) modulo \(q^r\). A parity-preserving one uses only even powers. Its constant coefficient is nonzero precisely when it is invertible, by the finite geometric series. The positive-degree ideal is nilpotent, so this ring has no idempotent other than zero and one. A chain therefore cannot split. Length and starting parity are invariants; alternatively, the graded quotients of \(\ker q\cap\operatorname{im}q^{r-1}\) count the ending parities of chains of each length. \(\square\)

Exactly four single alternating chains have two even vertices:

| Chain in the direction of \(q\) | \(\dim W\) | Extension |
|---|---|---|
| \(V\to W\to V\) | \(1\) | Intermediate extension |
| \(V\to W\to V\to W\) | \(2\) | Extension by zero |
| \(W\to V\to W\to V\) | \(2\) | Direct image |
| \(W\to V\to W\to V\to W\) | \(3\) | The additional five-vector block |

In each case the square of \(q\) between the two even vertices is nonzero, so \(T\) is the nontrivial block (2.2). Lemma 3.1 proves that these are all the indecomposables with the stated rank and unipotence. If \(T=1\) on a two-dimensional \(V\), every chain has at most one even vertex; at least two chains are necessary, so the object is decomposable.

The fourth row deserves actual maps. Take \(W=\Lambda w_0\oplus\Lambda w_1\oplus\Lambda w_2\) and put

\[
ue_2=w_1,\quad ue_1=w_2,\qquad
vw_0=e_2,\quad vw_1=e_1,\quad vw_2=0.
\tag{3.3}
\]

Then \(vu=N\), whereas \(uv\) has chain \(w_0\to w_1\to w_2\to0\). Its second monodromy has a size-three unipotent block. Its only stalk group is \(W/uV=\Lambda\bar w_0\) in degree zero, and its only costalk group is \(\ker v=\Lambda w_2\) in degree zero. For the first three rows, (1.6) gives respectively: stalk \(\ker N\) in degree minus one and costalk \(\operatorname{coker}N\) in degree one; zero stalk and costalk \(\ker N,\operatorname{coker}N\) in degrees zero and one; stalk \(\ker N,\operatorname{coker}N\) in degrees minus one and zero and zero costalk. These groups distinguish the four rows as well.

## 4. Identify the two spaces as cycles

Let \(f:X\to\mathbb C\) be regular, or holomorphic in the analytic constructible setting. Write \(Z=f^{-1}(0)\), \(i:Z\hookrightarrow X\), \(j:U=X\setminus Z\hookrightarrow X\). Pull the universal cover of \(\mathbb C^*\) back to \(U\), with map \(p:\widetilde U\to U\). The unshifted nearby complex and specialization map are

\[
C=R\psi_f(j^*K)=i^*R(jp)_*p^*j^*K,
\qquad s:i^*K\longrightarrow C.
\tag{4.1}
\]

The second map is induced by the adjunction unit to the cover. The deck action gives geometric monodromy \(T\). Define the unshifted vanishing complex by the actual complex cone, so that

\[
i^*K\xrightarrow{s}R\psi_f(j^*K)
\xrightarrow{\mathrm{can}}R\phi_fK\longrightarrow i^*K[1].
\tag{4.2}
\]

Use derived sheaf resolutions with their coherent maps to make this construction functorial; an unspecified cone in an abstract triangulated category would not suffice. The normalized functors are

\[
\Psi_fK=R\psi_f(j^*K)[-1],\qquad
\Phi_fK=R\phi_fK[-1].
\tag{4.3}
\]

The elementary group resolution explains the second cycle map. The augmentation kernel of \(\Lambda[t,t^{-1}]\to\Lambda\) is generated freely by \(t-1\): a Laurent polynomial vanishing at one is divisible by \(t-1\), and the Laurent polynomial ring has no zero divisor \(t-1\). This two-term free resolution computes the derived invariants of the deck group. Apply it to cochains on the lifted punctured neighbourhoods, and then take the exact filtered colimit over those neighbourhoods. Descent along the covering and its augmented resolution give

\[
B=i^*Rj_*j^*K\simeq\operatorname{Fib}(N:C\to C),
\qquad N=T-1.
\tag{4.4}
\]

The sheaf comparison (4.4) is proved in [Proposition F.1](#f-1-the-actual-cyclic-cover-comparison). It applies to every bounded-below classical complex on the open complement, including a positive-dimensional zero fibre. Bounded constructibility of nearby cycles is the separate geometric input used in Section 5.

The attaching map \(a:i^*K\to B\) includes more information than \(s\): it includes a homotopy \(h\) satisfying \(dh+hd=Ns\). On the cone \(F=\operatorname{Cone}(s)\), in coordinates
\(d_F(c,x)=(dc+sx,-dx)\), define

\[
w:F\to C,\qquad w(c,x)=Nc+hx.
\tag{4.5}
\]

The homotopy equation makes this a chain map. If \(q:C\to F\) is inclusion, then \(wq=N\). The compatible monodromy on \(F\) is \(1+qw\), which is invertible with inverse \(1-qT^{-1}w\), by the same multiplication as (1.8). Thus both composites are fixed, not just the first:

\[
\mathrm{var}\,\mathrm{can}=T_\Psi-1,\qquad
\mathrm{can}\,\mathrm{var}=T_\Phi-1,
\quad \mathrm{var}=w[-1].
\tag{4.6}
\]

Pasting the fibre sequences for \(i^*K\to B\to C\), with localization \(i^!K=\operatorname{Fib}(a)\), yields

\[
\Psi_fK\xrightarrow{\mathrm{can}}\Phi_fK\longrightarrow i^*K\longrightarrow,
\qquad
i^!K\longrightarrow\Phi_fK\xrightarrow{\mathrm{var}}\Psi_fK\longrightarrow.
\tag{4.7}
\]

This also proves naturality: the maps are induced by maps of resolutions and their attaching homotopies. Changing from \(T-1\) to \(1-T\) changes the variation sign.

For \(f=z\) on the disc, the lifted puncture is contractible. Thus \(R\psi_zL[1]=V[1]\), giving \(\Psi_z=V\). In the normal form (1.5), specialization is the identity from the degree-minus-one copy of \(V\) to \(V[1]\). Its cone cancels that identity pair and leaves \(W[1]\), giving \(\Phi_z=W\) and \(\mathrm{can}=u\). The attaching homotopy is the degree-zero component \(v\), so (4.5) gives \(\mathrm{var}=v\). This identifies Theorem 1.1 with the nearby/vanishing cycle diagram, with the actual maps and signs. Smooth shifted constants have zero vanishing space; a skyscraper has zero nearby space and vanishing space its stalk.

For the arithmetic definition, take a strict henselian trait \(S\), a geometric generic point \(\bar\eta\), and a geometric special point \(\bar s\). For \(X/S\) use

\[
R\psi_fL=\bar i^*R\bar j_*L_{X_{\bar\eta}}.
\tag{4.8}
\]

It carries full continuous inertia and any residue-field descent. Vanishing cycles are the cone of geometric specialization, and (4.3) is the total-space normalization. No tame generator replaces the full action. Appendix A treats constructibility; Appendix B treats the trait degree bounds; Appendices C–E distinguish full variation and duality from the untwisted classical formulas.

## 5. Locate exactly what t-exactness requires

**Theorem 5.1 (cycle t-exactness under the geometric hypotheses below).** Under those hypotheses, normalized nearby and vanishing cycles preserve the two middle-perverse halves. Classically the scope is regular functions and the corresponding local holomorphic constructible setting. Arithmetically it is separated finite-type families over henselian traits with \(\ell\)-adic coefficients, \(\ell\ne p\). For the generic fibre's own dimension convention, nearby cycles use \(R\psi\) without the extra shift; for a total-space perverse object the normalization is (4.3).

For a regular function on a separated finite-type complex variety with finite-dimensional algebraically constructible coefficients over a characteristic-zero field, all three inputs of the classical deduction are supplied here or in earlier lessons. Proposition F.1 proves the descent comparison (4.4). [Theorem G.4](#appendix-g-finite-nearby-complexes-and-the-resolution-reduction), with Appendices H–I, proves bounded constructibility. Affine morphisms, Theorem A.3, combined with its Section 2 dimension bounds, proves perverse exactness of both extensions for the principal affine open complement. Theorem 5.1 therefore holds at this algebraic scope. The unrestricted holomorphic setting retains its own constructibility and Stein-open hypotheses. The disc equivalence and examples above have their direct local proofs.

**Classical deduction.** Let \(M\) be perverse on \(U\). If \(j_!M\) and \(Rj_*M\) are perverse, localization gives

\[
B=i^*Rj_*M\in{}^pD^{[-1,0]}(Z).
\tag{5.1}
\]

Set \(C=R\psi_fM\). The perverse cohomology sequence of \(B\to C\xrightarrow N C\to\) says that \(N\) is surjective on \({}^pH^qC\) for \(q\ge0\), and injective for \(q\le-2\). On each generalized eigenvalue-one part it is nilpotent. A nilpotent epimorphism or monomorphism forces the object to vanish, since a sufficiently high iterate is both zero and epic or monic. Thus that part has only degree minus one.

Here is the finite decomposition used in this argument. A finite-length heart object with an endomorphism admits a Fitting decomposition for any polynomial in that endomorphism: its kernel and image chains stabilize, and at a large common exponent their intersection is zero and their sum is the object. On a finite-dimensional endomorphism algebra, an annihilating polynomial splits into relatively prime factors after scalar extension; Bézout projections give the corresponding generalized eigenspaces. These constructions commute with intertwiners and hence with the cohomology sequence. Their local finite-dimensionality and constructibility hypotheses are part of the stated sheaf foundations.

For any eigenvalue \(\lambda\), tensor \(M\) with the pullback of the rank-one local system on \(\mathbb C^*\) with monodromy \(\lambda^{-1}\). Tensoring with a local system is t-exact by the stalk and costalk tests. Its pullback to the universal cover is constant, so it tensors the nearby complex with that one-dimensional representation. The \(\lambda\)-part has become the eigenvalue-one part and therefore has no perverse degree other than minus one. This proves that all of \(C[-1]\) is perverse. Exact faithful scalar extension descends the conclusion to the original characteristic-zero field.

For perverse \(K\) on \(X\), the first triangle in (4.7), together with \(i^*K\in{}^pD^{\le0}\), gives the upper bound on \(\Phi_fK\). The second, with \(i^!K\in{}^pD^{\ge0}\), gives its lower bound. Both functors preserve heart objects. Their exact triangles and the finite perverse truncation tower then prove both t-exactness inequalities and exactness on hearts. This proves the algebraic assertion and the holomorphic deduction under its stated geometric hypotheses. \(\square\)

We will also need to split a bounded cycle complex itself. If a polynomial in its monodromy vanishes on each ordinary cohomology sheaf, a sufficiently high power vanishes on the complex: successive ordinary truncations make each composite with zero cohomology maps pass through one fewer layer. Factor the resulting annihilator into relatively prime powers and use Bézout idempotents. These idempotents split in the bounded constructible category: the usual mapping telescope of an idempotent in the ambient derived sheaf category has, on cohomology, its image; those images are bounded constructible direct summands, so the telescope belongs to the same constructible subcategory. Uniqueness follows because a map intertwining a nilpotent and an invertible operator is zero after multiplying by a sufficiently high power. This gives the functorial unipotent/complement decomposition used below and in the arithmetic appendices, under their constructibility assumptions.

## 6. Reconstruct along a general function

For a regular \(f:X\to\mathbb A^1_{\mathbb C}\), put \(E=\Psi_f^uP_U\), the unipotent nearby part of \(P_U\in\operatorname{Perv}(U)\), and \(N=(T-1)|_E\). The zero fibre may now have positive dimension, so the second datum is a perverse sheaf \(P_0\) there rather than a vector space.

**Theorem 6.1 (general gluing).** Subject to the cycle and operation inputs in Sections 4–5, perverse sheaves on \(X\) are equivalent to

\[
(P_U,P_0,u:E\to P_0,v:P_0\to E),\qquad vu=N.
\tag{6.1}
\]

Morphisms commute with the two arrows and the induced nearby map of their open component. The closed component is the unipotent vanishing-cycle sheaf. The following construction gives the inverse and explains why the nonunipotent part is forced.

First use all nearby cycles \(\widetilde E=\Psi_fP_U\) and a full factorization \(\widetilde E\xrightarrow uW\xrightarrow v\widetilde E\) of \(\widetilde N=T-1\). In the enhanced derived category set

\[
A=\operatorname{Cone}(u),\quad B=\operatorname{Cone}(\widetilde N),
\quad a=(v,1):A\to B,
\quad
P=\operatorname{Fib}(Rj_*P_U\oplus i_*A\to i_*B).
\tag{6.2}
\]

In target-first cone coordinates, \(A=W\oplus\widetilde E[1]\), \(B=\widetilde E\oplus\widetilde E[1]\), and \(a(w,e)=(vw,e)\). In the degree-ordered notation of (1.5), this same map has components \((1,v)\). The last arrow is restriction minus \(i_*a\). Equation (4.4) identifies \(B=i^*Rj_*P_U\). The sheaf recollement gives \(j^*P=P_U\), \(i^*P=A\), \(i^!P=\operatorname{Fib}(a)\). The identity nearby components in the last fibre cancel, leaving \(\operatorname{Cone}(v)[-1]\). Therefore the stalk has perverse degrees \([-1,0]\), the costalk has degrees \([0,1]\), and \(P\) is perverse. The specialization cone cancels in the same way, identifying its cycles and arrows with \(\widetilde E,W,u,v\).

Conversely, for a perverse \(P\), take its actual attaching map \(i^*P\to B\). Composing with \(B\to\widetilde E[1]\), then taking its cone and shifting, gives \(W=\Phi_fP\). The attaching homotopy gives \(v\), as in (4.5); rotation recovers \(i^*P=\operatorname{Cone}(u)\). The fibre reconstruction returns \(P\), because its comparison is an isomorphism on the open and closed restrictions.

For morphisms the enhanced attaching square must again be retained. Applying derived Hom to the fibre in (6.2) gives the fibre of the difference between the open-induced boundary map and the closed attaching map. Substitute the two cone models for the closed terms. Cancelling the identical nearby summands eliminates the degree-minus-one homotopy coordinates, just as the explicit cancellation (1.7) does on a disc. After taking degree zero, the remaining coordinates are a heart map on \(P_U\) and a heart map on \(W\); their differential has the two components expressing commutation with \(u\) and \(v\). The negative Hom groups between heart objects vanish, so there is no residual degree-minus-one boundary or choice in these coordinates. Positive Ext groups remain in the mapping complex but do not alter this degree-zero cancellation. This recovers precisely the stated pairs and their composition. [Proposition F.3 and Corollary F.4](#f-3-the-mapping-complex-of-two-factorizations) establish this calculation on the actual sheaf mapping complexes for a closed fibre of any dimension. The geometric constructibility and t-exactness hypotheses remain those of Section 5.

Now decompose \(\widetilde E=E\oplus E'\), with \(N'\) invertible on \(E'\). Let \(u'\) be the restriction of \(u\) and \(v'\) the projection of \(v\) to this summand. The endomorphism

\[
e=u'(N')^{-1}v':W\to W
\tag{6.3}
\]

is idempotent because \(v'u'=N'\). Its image is the copy of \(E'\) embedded by \(u'\), and its kernel is \(\ker v'\). The mixed composites are zero, so the remaining arrows use only \(E\). On \(\ker v'\), if \(N^m=0\), then \((uv)^{m+1}=uN^mv=0\); this is the unipotent vanishing part \(P_0\). The discarded notation has thus removed only the forced summand \((E',E',1,N')\). Adding it back turns (6.1) into the full factorization (6.2). All these operations commute with morphisms. Finally \(\Psi_f^u\) is exact, so componentwise kernels and cokernels satisfy (6.1) and their universal properties. This proves the claimed abelian equivalence subject to the identified inputs. \(\square\)

The maximal extension can be made explicit in this description. Give \(\Xi_fP_U\) unipotent factorization
\(x\mapsto(Nx,x):E\to E\oplus E\) followed by \((a,b)\mapsto a\), and add the forced complementary part. On this two-copy component put

\[
\alpha_-(x)=(Nx,x),\quad\alpha_+(a,b)=a,\qquad
\beta_+(x)=(0,-x),\quad\beta_-(a,b)=a-Nb.
\tag{6.4}
\]

The two alpha maps have the identity open component; the beta maps have zero open component. Their commuting equations follow by substitution. Their componentwise kernels and cokernels give

\[
0\to j_!P_U\xrightarrow{\alpha_-}\Xi_fP_U\xrightarrow{\beta_-}i_*E\to0,
\qquad
0\to i_*E\xrightarrow{\beta_+}\Xi_fP_U\xrightarrow{\alpha_+}Rj_*P_U\to0.
\tag{6.5}
\]

Here \(\beta_-\beta_+=N\), and \(\alpha_+\alpha_-\) is the canonical extension map. The usual three-term inverse to gluing is therefore the middle cohomology in the perverse heart of

\[
i_*E\xrightarrow{(\beta_+,u)}\Xi_fP_U\oplus i_*P_0
\xrightarrow{(\beta_-,-v)}i_*E.
\tag{6.6}
\]

Its composite is \(N-vu=0\); its first map is monic and its last epic by (6.5). On vanishing components, the middle kernel consists of \((a,b,y)\) with \(a=Nb+vy\), modulo \((a,b,y)\sim(a,b-x,y+ux)\). The map to \(P_0\) is \((a,b,y)\mapsto y+ub\). It is unchanged under that relation, is onto by \(y\mapsto(vy,0,y)\), and has kernel precisely the divided-out image. Its induced arrows are \(u,v\), since \(a=v(ub+y)\). Its open component is \(P_U\), and the complementary cycles are forced. The equivalence thus identifies (6.6) with (6.2), including its signs.

The function itself matters. On \(X=\mathbb A^1_z\times\mathbb G_{m,w}\), compare \(f=z\) and \(g=z/w\). Both vanish on \(Z=\{0\}\times\mathbb G_m\). Take a local system \(L\) on \(\mathbb C^*\) with nonidentity monodromy \(T\), and \(P_U=f^*L[2]\). It is perverse on the smooth two-dimensional open set. Holding a lifted \(f\)-parameter fixed leaves the coefficient fibre constant as \(w\) moves, so \(\Psi_fP_U=V_Z[1]\). Holding a lifted \(g\)-parameter fixed makes \(z=gw\) wind with \(w\), so \(\Psi_gP_U=L_Z[1]\) with monodromy \(T\) along the zero fibre. The parameter deck action is \(T\) in both cases, but these local systems on \(Z\) differ. Taking a nontrivial unipotent \(T\) gives the same distinction for unipotent cycles. A zero divisor alone therefore does not determine (6.1). This example is also recorded in the free Reich source; the calculation here specifies which of its two monodromies changes.

## 7. Exercises and solutions

**Exercise 1 (easy).** Calculate the nearby and vanishing diagrams of the smooth shifted constant sheaf and a skyscraper. Include both monodromies.

**Solution.** For \(\Lambda_D[1]\), lifting to the universal cover gives \(\Lambda[1]\); specialization from its stalk is the identity. The cone is zero, hence the diagram is \((\Lambda,0,0,0)\) and the nearby monodromy is one. For \(i_*\Lambda\), open restriction and nearby cycles vanish. The cone of \(\Lambda\to0\) is \(\Lambda[1]\), so normalized vanishing cycles are \(\Lambda\). This gives \((0,\Lambda,0,0)\), with vanishing monodromy one. The general formulas \(T_V=1+vu\), \(T_W=1+uv\) also give identity on every nonzero component. Formula (1.6) recovers the smooth stalk/costalk degrees minus one/one and the skyscraper's two degree-zero groups.

**Exercise 2 (easy).** Determine \(j_!L[1]\) and \(Rj_*L[1]\) for arbitrary invertible monodromy, including their boundary groups.

**Solution.** Extension by zero has acyclic stalk. In (1.6) this means that \(u\) is an isomorphism; choose it as the identification \(W=V\). Then \(v=N\), so its costalk is \([V\xrightarrow{N}V]\) in degrees zero and one, with groups \(\ker N\) and \(\operatorname{coker}N\). Direct image has acyclic costalk, so use \(v\) to identify \(W=V\); then \(u=N\), and its stalk is that same two-term complex in degrees minus one and zero. The other boundary complex is acyclic in each case. Both second monodromies are \(1+N=T\). Nothing in this computation assumes unipotence.

**Exercise 3 (medium).** Prove the intermediate-extension row and both exact sequences (2.1).

**Solution.** The universal boundary quotient is measured by \(\operatorname{coker}u\), and the universal boundary subobject by \(\ker v\). Their simultaneous vanishing forces \(u\) onto and \(v\) injective. Identify its target subspace through \(v\): it is \(vW=vuV=NV\), and its first arrow is \(N\). Conversely these arrows have the required surjectivity and injectivity, so the uniqueness characterization of intermediate extension applies. The map from extension by zero is \((1,N:V\to NV)\), with kernel \((0,\ker N)\). The map to direct image is \((1,NV\hookrightarrow V)\), with cokernel \((0,V/NV)\). Componentwise exactness proves the two sequences, with precisely those point-supported terms.

**Exercise 4 (medium).** Prove that \(1+uv\) is invertible whenever \(1+vu\) is, without equating the dimensions of the two spaces.

**Solution.** Put \(T=1+vu\) and \(S=1+uv\). Associativity gives \(Su=uT\) and \(vS=Tv\). Thus
\(S(1-uT^{-1}v)=S-uv=1\), and
\((1-uT^{-1}v)S=S-uv=1\).
This gives a two-sided inverse. The computation uses only additive-category composition and the inverse of \(T\), so it does not require a determinant or equal dimensions.

**Exercise 5 (hard).** Classify the indecomposable disc objects with two-dimensional unipotent nearby cycles, and write maps for the case beyond the three standard extensions.

**Solution.** Combine the arrows into the odd operator (3.1). Since \((vu)^2=0\), it satisfies \(q^5=0\). The explicit projection (3.2) splits off a longest homogeneous chain and then all remaining chains. An indecomposable is exactly one chain, by the local endomorphism-ring calculation in Lemma 3.1. Counting two even vertices leaves the four rows in Section 3. Each has nonzero \(q^2\) between those vertices, so its nearby monodromy is the nontrivial Jordan block. In particular there is no indecomposable with nearby dimension two and identity monodromy. The three shorter rows are the intermediate, zero and direct extensions in Section 2. For the five-vector row use (3.3); its combined chain is \(w_0\to e_2\to w_1\to e_1\to w_2\to0\). Its vanishing rank is three, its vanishing monodromy is a size-three block, and its boundary groups are \(\Lambda\bar w_0\) and \(\Lambda w_2\), both in degree zero. The chain splitting proves completeness, rather than only producing four examples.

## Arithmetic coefficients and geometric hypotheses

Appendix A treats finite-coefficient trait constructibility through coordinate-field arguments and induction. Appendix B treats full-inertia degree bounds, including the tame quotient, continuous character twists and the faithful regular-representation test on perverse objects. Appendix C gives the Iwasawa coefficient functors and variation target, with their arithmetic actions, group-algebra injectivity and generator comparisons. Appendix D derives generic nearby duality from evaluation and trace, with the two coordinate-fibre dualizing lines and the induction base. Appendix E gives the dual group-complex signs, a contraction retaining the attaching homotopy, and the boundary-pairing deduction from localization, the Kummer divisor sign and ordinary trace. The deductions use the ordinary, normalized adic, purity, finiteness and coherence hypotheses stated in each appendix. The disc calculation alone does not establish these arithmetic hypotheses.

## Appendix A. Constructibility over a trait

This appendix develops the finite-coefficient argument of the freely available author edition of SGA 4½, *Théorèmes de finitude*, §§3.1–3.6. The proof separates finite-data approximation, the auxiliary coordinate field, and the final proper-cohomology calculation. In particular, we prove that the tensor product defining the coordinate field is a field; we do not assume an unproved regular-extension assertion.

Fix a strictly henselian discrete valuation trait \(S\), with generic field \(K\), residue field \(k\), residual characteristic exponent \(p\), and \(\ell\) invertible on \(S\). For now use \(\Lambda=O/\pi^m\), a finite coefficient ring. Let \(X/S\) be separated of finite type and \(F\) a constructible sheaf on \(X_\eta\). The ordinary inputs are finite-presentation continuity, smooth and proper base change, the affine field cohomological bound, and proper cohomological finiteness over separably closed fields. These are identified in the first lesson and in the preceding lesson's field-bound proof and are prerequisites of this argument. They are not nearby-cycle constructibility assumptions.

For a geometric special point, the stalk of \(R^q\psi F\) is the filtered colimit of \(H^q(V_{\bar\eta},F)\) over affine pointed étale neighborhoods \(V\). If \(n=\dim X_\eta\), each such geometric generic fibre is affine of dimension at most \(n\). The affine field bound gives \(R^q\psi F=0\) for \(q>n\), before any constructibility conclusion. If \(X_\eta\) is empty, every such group is zero. We use that empty case as the start of dimension induction.

### Reduce the remaining defect to point-supported sections

A subsheaf of a finite constructible sheaf on a Noetherian scheme is constructible. To prove the assertion, take a finite stratification on which the ambient sheaf is finite locally constant, and trivialize it by finite étale covers. For each of its finitely many values, membership in the subsheaf is an open condition: a germ in the subsheaf lifts on an étale neighborhood, whose image is open, and the ambient section has that same value there. Each such open is constructible on a Noetherian stratum. Their finite membership partition, refined into locally closed pieces, makes the subsheaf constant on each piece. Descent gives the assertion downstairs. Consequently the image of a finite constructible sheaf in an arbitrary sheaf is constructible too: its kernel is such a subsheaf, and the image is the corresponding finite constructible quotient.

Now let \(G\) be a sheaf on an affine \(Y\subset\mathbb A_k^a\). Suppose its restriction to the geometric generic fibre of every coordinate projection is constructible. We construct a finite constructible subsheaf \(G_0\subset G\) whose quotient has only sections with finite support.

For each coordinate, spread that generic constructible sheaf and its map into \(G\) to a finite-presentation étale neighborhood of the coordinate generic point. The finite generators, relations and covering identities are exactly the compact-presentation input proved in [Constructible sheaves and extension by zero, §5](course:ag-etale-cohomology/constructible-sheaves-and-extension-by-zero#5-filtered-approximation-not-always-a-union). If \(u:Y'\to Y\) is the resulting étale map and \(H\) the spread sheaf, adjunction gives \(u_!H\to G\). Its image is constructible by the preceding paragraph. On the chosen geometric generic fibre this map is onto: the pointed étale neighborhood has a lift of that geometric point, and the summand at that lift gives the spread isomorphism. Summing these images over the finitely many coordinates gives \(G_0\).

The quotient vanishes on all the coordinate generic fibres. The support of any one of its sections on a finite-type étale chart is closed, since the zero-germ locus is open. If a positive-dimensional irreducible component of that support existed, its image in \(Y\) would still have positive dimension: an étale map has zero-dimensional fibres. Some coordinate would be nonconstant on that image. The section would then have a nonzero geometric generic germ for that coordinate, contrary to the quotient's vanishing there. The support is therefore zero dimensional, hence a finite set of closed points. On a general finite-type \(Y\), use finitely many affine charts and sum the resulting subsheaves after extension by zero.

Over a separably closed field, a sheaf all of whose local sections have finite support is the direct sum of its closed-point skyscraper sheaves. This assertion is local: isolate each of the finitely many supporting points of a section, extend by zero off its support, and glue; a germ at one point determines its point-supported section uniquely. Closed points have purely inseparable residue extensions, so their étale sites have no nontrivial finite separable extensions. Each skyscraper has no positive cohomology. Finite sums have the same property, and the filtered-colimit cohomology comparison on the qcqs étale site gives it for their direct sum. The actual finite-cover continuity proof, rather than an exchange of arbitrary infinite products, is the prerequisite used here.

### Prove the auxiliary tensor product is a field

Let \(S_t\) be the strict localization of \(\mathbb A^1_S\) at a geometric generic point of its special line; denote its fraction field by \(K_t\). The uniformizer of \(S\) is still a uniformizer of \(S_t\). Indeed \(O_S[t]_{(\pi_S)}\) has the Gauss valuation: divide a polynomial by a coefficient of minimum valuation, after which its nonzero reduction is invertible at the generic point of the special line. Every nonzero element is thus a uniformizer power times a unit. Pointed étale neighborhoods and their strict-local limit keep that uniformizer, and their residue fields form the separable closure of \(k(t)\). This gives a strictly henselian discrete valuation ring with value group \(\mathbf Z\).

Choose a separable closure \(\bar K\) of \(K\) and form the algebra
\(A=\bar K\otimes_K K_t\).
For a finite separable \(L/K\) inside \(\bar K\), the algebra \(L\otimes_KK_t\) is a finite product of fields: a separable primitive polynomial stays square-free over \(K_t\), and its distinct irreducible factors give that product. We show that the product has only one factor.

For each such finite extension, write \(j_L:\operatorname{Spec}L\to S\). The special stalk of \((j_L)_*\mathbf F_\ell\) is \(\mathbf F_\ell\): the base is strictly local and \(\operatorname{Spec}L\) is connected. Apply ordinary smooth base change to \(\mathbb A^1_S\to S\) and this direct image. At the chosen geometric generic point of the special line, finite-presentation continuity through its pointed étale neighborhoods identifies the resulting stalk as

\[
H^0\bigl(\operatorname{Spec}(L\otimes_K K_t),\mathbf F_\ell\bigr)
=\mathbf F_\ell.
\]

Each field factor contributes an independent constant section to this group. The displayed equality therefore proves that there is exactly one factor. This uses ordinary smooth base change for \(j_L\), before any nearby-cycle constructibility theorem.

Every algebra \(L\otimes_KK_t\) injects into \(A\), since extending fields is faithfully flat. Their directed union \(A\) is a field: the inverse of a nonzero element already belongs to its finite-stage field. Write this field as \(K'\). At a finite Galois stage, the original automorphisms extend faithfully and their number equals the unchanged degree over \(K_t\). Taking their compatible limits shows that \(K'/K_t\) is Galois with group \(\operatorname{Gal}(\bar K/K)\).

### Separate henselian algebra from valuation extension

The two uses of henselian valuation extension in this appendix and Appendix B share the integral-algebra deduction A.1a and the general valuation-extension theorem A.1b below. Neither requires a finite normalization.

**Lemma A.1a (the integral-algebra part).** Let \(R\) be a henselian local domain with fraction field \(K\), let \(L/K\) be an arbitrary algebraic extension, and let \(C\) be the integral closure of \(R\) in \(L\). Then \(C\) is a local henselian domain, its maximal ideal contracts to that of \(R\), its residue field is algebraic over the residue field of \(R\), and
\[
C=\varinjlim_{B\subset C}B,\qquad \operatorname{Frac}(C)=L,
\tag{A.V1}
\]
where \(B\) runs over the finite \(R\)-subalgebras of \(C\). The maps in this filtered system are local. No Noetherianity, completeness, finite normalization or absence of defect is assumed.

To prove this, any finite list of integral elements generates a finite \(R\)-module: reduce powers of each generator using its monic equation, leaving a finite list of spanning monomials. Each such algebra \(B\) is a domain. By Henselian local rings, Theorem 2.2, it is a finite product of local rings. A domain has no idempotents other than zero and one, so there is only one nonzero factor. Thus \(B\) is local; Proposition 3.1 makes it henselian.

For \(B\subset D\) in this system, every element of \(D\) is integral over \(B\), because its monic equation over \(R\) is already one over \(B\). A maximal ideal of \(D\) contracts to a maximal ideal of \(B\). Indeed, the resulting integral subring of the field \(D/\mathfrak m_D\) is a field: the monic equation for the inverse of a nonzero element expresses that inverse in the subring after multiplication by a suitable power of the element. The contraction is therefore the unique maximal ideal of \(B\). This proves that the transition maps are local. Their union is \(C\), and Proposition 3.2 proves that this union is local and henselian, with the union of the stage residue fields as its residue field. Each stage residue field is algebraic over that of \(R\), by reduction of monic equations; so is the union.

For completeness, take \(z\in L\) and a monic equation
\[
z^n+\sum_{i=0}^{n-1}a_i z^i=0,\qquad a_i\in K.
\]
Choose a nonzero \(a\in R\) with every \(aa_i\in R\), by clearing the finitely many denominators. Multiplication by \(a^n\) gives a monic equation for \(az\) with coefficients \(a^{n-i}a_i\in R\). Hence \(az\in C\) and \(z=(az)/a\in\operatorname{Frac}(C)\). The other inclusion is immediate. This proves (A.V1). \(\square\)

**Theorem A.1b (valuation extension, VE).** Let \(R\) be a valuation ring with fraction field \(K\), let \(L/K\) be an arbitrary algebraic field extension, and let \(C\) be the integral closure of \(R\) in \(L\). A valuation ring \(W\) of \(L\) extending \(R\) exists. For every such \(W\),
\[
\mathfrak n=\mathfrak m_W\cap C\text{ is maximal},\qquad
W=C_{\mathfrak n},\qquad \mathfrak n\cap R=\mathfrak m_R.
\tag{A.V2}
\]
Here extending means \(W\cap K=R\). The assertion includes inseparable and infinite algebraic extensions and valuations of arbitrary rank.

**Existence.** More generally, let \(A\) be a local subring of a field \(F\). Order the local subrings of \(F\) dominating \(A\) by domination. A chain has its union as an upper bound: the union of its maximal ideals is an ideal, and every element outside that ideal already has an inverse at one stage. Zorn's lemma gives a maximal member \(B\), with maximal ideal \(\mathfrak m\).

If \(z\in F\) is integral over \(B\), then \(D=B[z]\) is a finite \(B\)-module and \(\mathfrak mD\ne D\). To see the latter assertion without a finiteness assumption on the ring, suppose \(\mathfrak mD=D\), choose finitely many module generators, and express each as an \(\mathfrak m\)-linear combination of those generators. Multiplying the resulting matrix relation by its adjugate shows that a determinant congruent to one modulo \(\mathfrak m\) annihilates all the generators. This determinant is a unit, contradicting \(1\in D\). A maximal ideal of \(D\) containing \(\mathfrak mD\) therefore gives a localization dominating \(B\). Maximality forces \(z\in B\).

For \(x\in F^*\setminus B\), the same maximality gives \(\mathfrak mB[x]=B[x]\): otherwise a maximal ideal above this proper ideal and localization at it would give a larger dominating local ring. Thus
\[
1=\sum_{i=0}^{d}b_i x^i,\qquad b_i\in\mathfrak m,\quad d\geq1.
\]
Multiplying by \(x^{-d}\) and dividing by the unit \(1-b_0\) gives a monic equation over \(B\) for \(x^{-1}\). The preceding paragraph puts \(x^{-1}\) in \(B\). Hence for every nonzero element of \(F\), that element or its inverse lies in \(B\); this is the valuation-ring criterion and also implies \(\operatorname{Frac}(B)=F\).

Apply this construction with \(A=R\) and \(F=L\). If \(a\in K\setminus R\), then \(a^{-1}\in\mathfrak m_R\). A local ring dominating \(R\) cannot contain both this element in its maximal ideal and its inverse. Therefore \(B\cap K=R\). The same construction extends a given valuation ring through any further field extension; it does not depend on the localization assertion still to be proved.

**The easy inclusion and the residue field.** Use additive valuation notation \(v\), allowing any totally ordered value group. It can be obtained directly from a valuation ring as \(F^*/B^*\), ordered by divisibility. Products add values and \(v(a+b)\geq\min(v(a),v(b))\); if two summands have distinct values, factoring out the smaller one shows that equality holds. In particular, a sum with a unique smallest-valued term is nonzero. A negative-valued element cannot satisfy a monic equation with nonnegative-valued coefficients, because its highest power would be the unique smallest-valued term. Every valuation ring is consequently integrally closed in its fraction field.

It follows that \(C\subset W\). Units and nonunits in \(R\) remain respectively units and nonunits in \(W\), by \(W\cap K=R\). Thus \(\mathfrak n=\mathfrak m_W\cap C\) lies above \(\mathfrak m_R\). The domain \(C/\mathfrak n\) is integral over \(k=R/\mathfrak m_R\), so it is a field: a nonzero algebraic element over a field has its inverse in the algebra it generates. This makes \(\mathfrak n\) maximal and gives \(C_{\mathfrak n}\subset W\). Domination alone has not established equality.

**A denominator integral at every conjugate.** Fix \(0\ne x\in W\). Choose an algebraic closure \(\Omega\) of \(L\), and extend \(W\) to a valuation ring \(U\) of \(\Omega\) by the existence argument. In particular \(U\cap L=W\) and \(U\cap K=R\). Let \(z_1,\ldots,z_n\) be all the roots, counted with multiplicity, of the minimal polynomial of \(x\) over \(K\).

Each unit \(z_i\) of \(U\) has residue algebraic over \(k\). Indeed, in any polynomial relation for \(z_i\) over \(K\), divide all the coefficients by one having least valuation. They then lie in \(R\), at least one is a unit, and reduction gives a nonzero polynomial over \(k\) annihilating the residue. Choose a monic \(\bar q\in k[T]\) vanishing on the finitely many unit residues, for example the product of their monic minimal polynomials. If there are no such residues, take \(\bar q=1\). Lift its coefficients to a monic \(q\in R[T]\), and put
\[
h(T)=1+Tq(T),\qquad d=\deg h\geq1,\qquad
y=\frac1{h(x)},\quad u=\frac{x}{h(x)}.
\tag{A.V3}
\]
The constant term of \(h\) is one. For every \(z=z_i\) the following valuations follow directly from this construction:
\[
\begin{array}{c|ccc}
 &v(h(z))&v(1/h(z))&v(z/h(z))\\ \hline
v(z)\geq0&0&0&v(z)\\
v(z)<0&d\,v(z)&-d\,v(z)&(1-d)v(z)
\end{array}
\tag{A.V4}
\]
For positive value, \(zq(z)\) belongs to the maximal ideal. For value zero, its residue vanishes by the choice of \(\bar q\). In both cases \(h(z)\) is a unit. For negative value, the monic highest-degree term of \(h(z)\) has strictly smaller value than every other term, even in a non-Archimedean ordered group. This proves the second row. In particular \(h(z_i)\ne0\), and both rational expressions in (A.V4) have nonnegative value at every conjugate.

Here is why this proves integrality, without a separability assumption. On the \(K\)-vector space \(K(x)\), let \(M\) be multiplication by \(x\) in the basis \(1,x,\ldots,x^{n-1}\). Its characteristic polynomial is the minimal polynomial of \(x\). Over \(\Omega\), successively choosing an eigenvector and then doing the same in the quotient triangularizes \(M\), with diagonal entries \(z_1,\ldots,z_n\), including repetitions. Consequently \(h(M)\) is invertible, and the two matrices
\[
h(M)^{-1},\qquad Mh(M)^{-1}
\]
have diagonal entries \(1/h(z_i)\) and \(z_i/h(z_i)\) after triangularization. Their characteristic polynomials are monic with coefficients in \(K\); those coefficients are also in \(U\), being sums of products of nonnegative-valued diagonal entries. They therefore belong to \(K\cap U=R\). The characteristic-polynomial identity, obtained from the adjugate identity for \(TI-M'\) for each of these two matrices \(M'\), annihilates the corresponding multiplication operator. Applying it to \(1\in K(x)\) supplies monic equations over \(R\) for \(y\) and \(u\). Thus \(y,u\in C\). This matrix argument retains algebraic multiplicities in the inseparable case rather than replacing them by distinct automorphisms.

Since \(x\in W\), the first row of (A.V4) makes \(y\) a unit of \(U\), hence a unit of \(W=U\cap L\). Thus \(y\notin\mathfrak n\) and \(x=u/y\in C_{\mathfrak n}\). The case \(x=0\) is immediate. This proves the other inclusion in (A.V2). Only the finite field \(K(x)\) was used for each element; \(L/K\) itself need not be finite. \(\square\)

When \(R\) is henselian, Lemma A.1a makes \(C\) local and henselian. Theorem A.1b now makes every extending valuation ring equal to \(C\) itself. It is therefore unique, and remains henselian through further algebraic extensions by the same argument. This gives the precise valuation-theoretic input for \(K'\), its finite intermediate fields, and \(K^t\). No discreteness, finite normalization, completeness, residue-field finiteness or ramification-degree equality was used.

For valuation-ring domination and normality, see the Stacks Project authors' lemmas in the [AI Integrated Stacks native Commutative Algebra edition](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex), revision 565b10e987aba5969b21145a0833f42d69f96790, labels `lemma-dominate`, `lemma-valuation-ring-normal`, `lemma-valuation-ring-x-or-x-inverse` and `lemma-valuation-ring-cap-field`. The localization deduction follows from the domination construction above. The henselian conclusion also uses the exact programme proofs linked in A.1a. Their recursive foundations and the remaining nearby-cycle sheaf-theoretic prerequisites are separate from Theorem A.1b.

### Control the auxiliary Galois group, including possible defect

Extend the henselian valuation of \(K_t\) to \(K'\). Its residue field is an algebraic extension of the separably closed residue field of \(K_t\), hence is purely inseparable over that field and remains separably closed. Its value group is \(\mathbf Q\), with the original uniformizer valued at one. For the upper inclusion, in any finite algebraic extension, elements representing distinct value-group cosets are linearly independent over the base: a proposed relation has a term of uniquely smallest valuation. The index is therefore finite, so all the new values are rational. For the reverse inclusion, \(K'\) contains \(\bar K\). In characteristic zero that field contains all roots of a uniformizer. In characteristic \(p\), prime-to-\(p\) roots give the corresponding denominators, while a root of \(z^p-z=\pi_S^{-1}\) has valuation \(-1/p\); iterating this separable equation with the preceding root on the right gives every denominator \(p^r\). Together these give all rational values.

Put \(P=\operatorname{Gal}(\overline{K_t}/K')\), for a compatible separable closure. We prove that \(P\) is pro-\(p\), allowing defect in the finite extensions. Every finite algebraic extension of \(K'\) still has value group \(\mathbf Q\): a finite-index enlargement of a divisible subgroup in a torsion-free group is equal to it. To check this last statement, multiply a new value by the finite index, divide that multiple in the old group, and use torsion-freeness. Its residue field remains separably closed, and the extended valuation is henselian. The full algebraic input is [Lemmas A.1a and Theorem A.1b](#separate-henselian-algebra-from-valuation-extension): the integral closure is local henselian and is the unique extending valuation ring, also through further algebraic extensions.

Suppose a finite Galois extension \(N/K'\) had an automorphism \(\sigma\) of prime order \(r\ne p\), and let \(M=N^{\langle\sigma\rangle}\). Every element of \(M^\times\) has an \(r\)-th root in \(M\). First match its valuation by an \(r\)-th power, using divisibility; the remaining unit has an \(r\)-th root in the separably closed residue field, and Hensel's lemma lifts that root because \(r\) is invertible in the residue field. The same reasoning puts every \(r\)-th root of unity in \(M\). As an \(M\)-linear operator, \(\sigma\) is diagonalizable: its minimal polynomial divides the split polynomial \(x^r-1\) with distinct roots. A nonidentity eigenvalue would have an eigenvector \(u\) with \(u^r\in M\). If \(b\in M\) satisfies \(b^r=u^r\), then \(u/b\) is a root of unity in \(M\), contradicting the nonidentity eigenvalue. Thus no such automorphism exists.

For clarity, the finite-group step needs no ramification-degree formula. If a prime \(r\) divides the order of a finite group, cyclic rotation acts on the tuples \((g_1,\ldots,g_r)\) with product one. Rotation preserves that condition, and all nonfixed orbits have size \(r\). There are \(|G|^{r-1}\) tuples, so the number of fixed tuples is divisible by \(r\). The identity tuple is one; another gives a nonidentity element with \(g^r=1\), hence an element of order \(r\). Applied above, this shows that every finite Galois quotient is a \(p\)-group. If \(p=1\), every finite quotient is trivial.

### The actual coordinate Galois descent

**Lemma A.2.** Suppose \(L_\infty/L\) is a Galois extension with pro-\(p\) group \(P\), and \(\ell\ne p\). For a qcqs \(L\)-scheme \(V\) and an \(\ell\)-primary torsion étale sheaf \(F\), restriction induces
\[
H^q(V,F)\xrightarrow{\sim}
H^q(V_{L_\infty},F)^P.
\tag{A.D1}
\]
The maps are natural in pointed neighbourhoods, coefficients and their connecting maps. The corresponding bounded-below comparison uses exact continuous invariants. In the application above \(L=K'\) and \(L_\infty=\overline{K_t}\). No finite-residue or defectless hypothesis is needed for this descent step; the preceding valuation argument supplies the pro-\(p\) assertion separately.

Here is a proof retaining the restriction map. For a finite Galois subextension \(E/L\), its group \(Q\) is a finite \(p\)-group and \(V_E\to V\) is finite étale and surjective. The augmented Čech sheaf complex of this cover is locally split: after pulling back to the cover, insertion of its diagonal section contracts the alternating face differential. Resolving its terms gives the descent double complex. The iterated fibre products are disjoint unions of copies of \(V_E\) indexed by powers of \(Q\). Thus its other filtration is the group-cochain complex, with its actual permutation action and restriction augmentation, and gives
\[
H^a\bigl(Q,H^b(V_E,F)\bigr)\Longrightarrow H^{a+b}(V,F).
\tag{A.D2}
\]
The continuous-cochain resolution, §§2–3 fixes this differential and the connecting maps. Since \(|Q|\) is invertible on every \(\ell\)-primary group, averaging contracts its positive cohomology; equivalently, the lift-and-average argument in that lesson's Solution 3 makes invariants exact. Therefore (A.D2) identifies restriction with the isomorphism onto \(Q\)-invariants, in every degree. This argument uses neither constructibility nor nearby cycles.

For the infinite extension use Constructible complexes, BA.5: the cohomology upstairs is the filtered colimit over these finite field extensions. A class descending to \(V_E\) has an open stabilizer, so this is the actual discrete continuous action. Do not interchange invariants with an arbitrary colimit without proof. Instead, let an invariant class upstairs be represented by \(c_E\). Averaging \(c_E\) over \(Q\) produces an invariant at that same stage whose image is the original class, because every summand has that image. Its finite-stage descent proves surjectivity in (A.D1). If a class downstairs vanishes upstairs, continuity makes it vanish at a finite stage; the finite-stage restriction is injective, so it was zero. This proves injectivity.

Exactness of continuous \(P\)-invariants follows by the same finite lift-and-average argument: a lift of an invariant element is fixed by an open normal subgroup, and averaging its finite orbit produces an invariant lift. For a bounded-below complex, its cohomological filtration has only finitely many contributing terms in each degree of derived sections. The sheaf comparisons above therefore give the bounded-below comparison with these same restriction maps. Applying it on the pointed neighbourhoods defining nearby cycles and sheafifying gives (A.1), not just an equality of dimensions. The auxiliary invariants commute with the surviving quotient action by naturality. They do not discard the original full inertia action. \(\square\)

### Apply the coordinate induction and finish by proper cohomology

For a family over \(S_t\), also viewed over \(S\), the geometric-generic construction and continuous Galois descent now give

\[
R\psi_S(F)=\bigl(R\psi_{S_t}(F)\bigr)^P
\tag{A.1}
\]

after the indicated base restrictions. On pointed neighborhoods, this is the Hochschild–Serre comparison for \(\overline{K_t}/K'\); its higher \(P\)-cohomology vanishes by finite-group averaging, since \(\ell\ne p\). The averaging maps are compatible with enlarging finite quotients and with restriction. They yield an actual exact invariant functor here. This auxiliary \(P\) concerns the coordinate-field extension only; it does not replace the original full inertia action by tame invariants.

Proceed by induction on \(n=\dim X_\eta\), starting with the empty generic fibre. On an affine chart, embed \(X\) into \(\mathbb A_S^a\) and apply a coordinate projection to \(S_t\). A generic component on which that coordinate is nonconstant has new generic dimension at most \(n-1\): adjoining the coordinate to the base field lowers its transcendence degree by one, and the further algebraic field extension to \(K_t\) preserves dimension. If the coordinate is algebraic over \(K\), a nonzero polynomial relation becomes an invertible scalar over the field containing the transcendental coordinate, so that component disappears. Thus induction applies to every resulting coordinate family, including when \(n=0\), when all these generic fibres are empty.

Smooth base change and continuity identify the coordinate-generic restriction of \(R^q\psi_S F\) with the left side of (A.1). The right side is a subsheaf of a finite constructible sheaf by induction, and is therefore constructible by the finite-data observation. That observation supplies constructible subsheaves
\(G_q\subset R^q\psi F\)
whose quotients \(Q_q\) have only finite-support local sections.

We may work on a projective \(S\)-scheme: take the projective closure of the original affine chart and extend its generic sheaf by zero. This preserves constructibility on the generic fibre; restricting cycles back to the chart is open, hence smooth, base change. Over the separably closed residue field, each \(Q_q\) is the skyscraper sum described above. Hence \(H^a(X_s,Q_q)=0\) for \(a>0\). The groups \(H^a(X_s,G_q)\) are finite by the first lesson's [Proposition 3.2](constructible-complexes-on-algebraic-varieties.md#proposition-3-2-finite-coefficients-and-proper-supports), so the long exact sequence makes \(H^a(X_s,R^q\psi F)\) finite for \(a>0\).

Proper base change gives

\[
E_2^{a,b}=H^a(X_s,R^b\psi F)
\Longrightarrow H^{a+b}(X_{\bar\eta},F).
\tag{A.2}
\]

The abutment is finite by proper finiteness over the separably closed generic field. Every positive-column term is already finite. No differential enters column zero; every outgoing differential has finite image, and for \(E_r^{0,b}\) it vanishes once \(r>b+1\). Its eventual kernel is a subquotient of the finite abutment. Climbing back through these finitely many kernels proves that \(H^0(X_s,R^b\psi F)\) is finite. The sequence
\(H^0(G_b)\to H^0(R^b\psi F)\to H^0(Q_b)\to H^1(G_b)\)
then makes \(H^0(Q_b)\) finite. A direct sum of point modules with finite total group has only finitely many nonzero summands, all finite. Thus \(Q_b\), and then \(R^b\psi F\), are constructible. For \(n=0\), the empty coordinate restrictions supply the same finite-support reduction; no separate assertion about the dimension of a projective special fibre is needed.

### Preserve the coefficient and prerequisite distinctions

Finite ordinary truncation triangles extend the finite-coefficient conclusion to bounded constructible complexes. For compatible lattice systems, the actual geometric-generic construction must also commute with derived coefficient reduction. The derived-complete constructibility criterion in [The pro-étale site and ℓ-adic complexes, §5](course:AG-LTF/the-pro-etale-site-and-l-adic-complexes#5-constructible-complexes-and-classical-sheaves), with its coherent reductions and finite Tor hypotheses, then supplies the normalized integral passage. Rationalization gives finite \(E/\mathbf Q_\ell\), and finite coefficient descent gives \(\overline{\mathbf Q}_\ell\). Those exact normalized comparison maps are supplied by Weights, Lemma C.2a, and their general constructible application is Proposition A.3 below; inverse limits of finite stalk groups alone do not prove them.

The finite-coefficient argument uses ordinary base change, finite presentation, the affine cohomological bound, proper finiteness and henselian valuation extensions, with the hypotheses of their cited programme proofs. Lemma A.2 gives auxiliary Galois descent. Proposition A.3 gives the normalized coefficient passage using its completed-operation hypotheses.

### Normalized constructibility for bounded inputs

**Proposition A.3.** Retain the separated finite-type trait family above, and put \(d=\dim X_\eta\) when its generic fibre is nonempty. Let \(O\) be the integers of a finite extension \(E/\mathbf Q_\ell\), let \(\pi\) be a uniformizer, and let \(O_n=O/\pi^n\). Let \(P\) be a complete integral complex on \(X_\eta\) whose first derived reduction is bounded constructible. If that reduction has cohomology in \([a,b]\), then the normalized nearby complex is complete constructible, with all its derived reductions in \([a,b+d]\). It retains the full inertia action. The empty generic fibre gives the zero object. Rational localization gives the same constructibility assertion for every bounded constructible \(E\)-complex, not merely a lisse sheaf or a surface calculation.

This proposition integrates the finite-coefficient proof of Appendix A with the actual formal comparison; it is relative to the ordinary geometric and algebraic providers recorded there. It is not a substitute proof of those providers.

Let \(u:X_\eta\hookrightarrow X\), \(v:X_{\bar\eta}\to X_\eta\), \(j=uv\), and \(i:X_{\bar s}\to X\). For any map \(f\), write \(f_c^*=Cf^*\), where \(C\) is derived \(\pi\)-completion. Set
\[
K=C u_!P,\qquad
N=i_c^*Rj_*v_c^*P.
\tag{A.C1}
\]
This does not require a pre-existing extension of \(P\) across the special fibre. Ordinary open extension is exact, commutes with the finite coefficient cone, and restricts back to \(P\). Completion does not change any derived reduction, by BK.4. Hence \(K_n=u_!P_n\) with its quotient transitions, and \(j_c^*K=v_c^*P\) by reduction detection. The coefficient triangles of BM.6 give a single bound \([a,b]\) for every \(P_n\). Exact open extension retains it. Each \(K_n\) is a bounded-below classical étale complex, so the hypotheses of Weights, Lemma C.2a apply to this \(K\) on the trait family.

That lemma's formal statement allows this arbitrary \(X\). Only its later worked vanishing-cycle calculation specializes to a surface. Its actual maps identify
\[
N\otimes_O^LO_n
 \simeq \nu_{\bar s}^*\bigl(i_{\mathrm e}^*Rj_{\mathrm e,*}v_{\mathrm e}^*P_n\bigr)
 =\nu_{\bar s}^*R\psi(P_n).
\tag{A.C2}
\]
Here \(\nu_{\bar s}\) is the pro-étale to étale comparison. The map \(j\) is affine: it is the base change of the geometric-generic-point map, which is an affine field extension followed by the principal open of a uniformizer. It need not be of finite type. C.2a uses qcqs ordinary direct image and its bounded-below classical comparison, not a finite-type image theorem for this \(j\). Formula (A.C2) respects quotient transitions and the actual inertia maps; it is not a family of independently selected isomorphisms.

Finite ordinary truncations apply the geometric proof above to \(P_n\). Its affine bound is exactly Cohomological dimension, Theorem 5.1, on the geometric generic affine neighbourhoods. Thus the right side of (A.C2) is bounded constructible in \([a,b+d]\), uniformly in \(n\). In particular \(N_1\) is bounded constructible. Completeness and the definition in BM.6 put \(N\) in the complete constructible category; BO.6 and BQ.4 give the local integral models and the normalized bounded cohomology. There is no assumption that a constructible heart realizes its entire ambient derived category.

There is no extra cohomological degree from the inverse limit. At the top degree \(t=b+d\), the coefficient triangle \(N_1\to N_{n+1}\to N_n\) makes \(H^t(N_{n+1})\to H^t(N_n)\) surjective. The replete product-and-lifting argument of BM.6 therefore kills the potential degree-\(t+1\) derived-limit term. At the bottom all reductions are in degrees at least \(a\). This proves the bounded normalized assertion on the special fibre without exchanging ordinary stalks and inverse limits. Completed geometric fibres use C.2a's separate, actual comparison (C.14c).

Finally BX.5–BX.7 supplies integral models and all higher morphisms for every bounded constructible rational complex on the generic fibre. The construction (A.C1) is exact and \(O\)-linear. After rationalizing its target it sends multiplication by \(\pi\) to an invertible map, so it factors through the central localization of the integral category. The resulting functor is independent of the chosen integral model, by that localization's universal property; arbitrary complexes are not reduced to a claim about two sheaf lattices. Finite coefficient extension is compatible by C.2a's finite-free scalar comparison and the cofinal uniformizer filtrations. This gives the stated finite-coefficient-field interpretation of \(\overline{\mathbf Q}_\ell\). Full inertia continuity is then [Lemma B.0](#finite-derived-endomorphisms-and-continuous-inertia), using the constructibility just obtained; it was not an input to the finite-coefficient induction. \(\square\)

## Appendix B. Degree bounds with full inertia

The argument has three tests. First, a local affine calculation bounds the boundary of an extension from the generic fibre. Next, continuous characters test each monodromy eigenvalue, and a finite regular representation detects the parts removed by inertia invariants. Finally, the actual augmentation map controls closed-supported subobjects and proves the vanishing-cycle assertion. The permitted comparisons are Illusie's §§1.1, 3.6 and 4.5–4.6 and Reich's free nearby-cycle argument. We give the group and categorical steps explicitly, using the sign \(T-1\).

Work first over a strictly henselian discrete valuation trait \(S\), with generic point \(\eta\), special point \(s\), residual characteristic exponent \(p\), and \(\ell\ne p\). The coefficients of the perverse assertions are a finite extension \(E/\mathbf Q_\ell\). Write \(X/S\) for a separated finite-type scheme, \(j:X_\eta\hookrightarrow X\), and \(i:X_s\hookrightarrow X\). Bounded constructibility of the nearby object is the separate conclusion of Appendix A, subject to its recorded foundations. We also require the exact ordinary six operations, constructible Hom finiteness, their continuous equivariant interpretation, and the normalized adic comparisons stated at the end. These requirements are not consequences of the group calculations alone.

### Finite derived endomorphisms and continuous inertia

**Lemma B.0 (the whole-object finiteness and continuity input).** Let \(Y\) be separated of finite type over a separably closed field \(k\), and let \(E/\mathbf Q_\ell\) be finite, with \(\ell\ne\operatorname{char}k\). Write \(O\) for its valuation ring, \(\pi\) for a uniformizer, and \(O_n=O/\pi^n\). Every pair of bounded constructible rational complexes has finite-dimensional derived Hom in every degree. For a normalized nearby-cycle object, its actual inertia action is continuous for this finite-dimensional topology, provided its first finite reduction is bounded constructible. The finite-coefficient argument of Appendix A and [Proposition A.3](#normalized-constructibility-for-bounded-inputs) supply this condition subject to their recorded ordinary and algebraic foundations; it is not a consequence of the present lemma. The coefficient identifications are the actual ones in Weights, Lemma C.2a.

**Derived Hom, not only stalk Hom.** Take complete constructible integral models \(P,Q\) on \(Y\). Constructible complexes, BV.5 puts \(R\mathcal Hom_O(P,Q)\) in the complete constructible category. BV.1 applies to the structural morphism of \(Y\); over our separably closed field the resulting point category is the category of coefficient complexes. Hence
\[
C=R\operatorname{Hom}_Y(P,Q)
 =R\Gamma\bigl(Y,R\mathcal Hom_O(P,Q)\bigr)
\tag{B.H1}
\]
is complete and its first derived reduction is a bounded complex of finite-dimensional residue-field spaces. The finiteness here is the ordinary direct-image theorem M.4, not compact-support finiteness silently substituted on a nonproper scheme. No finite-field descent of \(Y\) is assumed.

Here is the coefficient argument making \(C\) perfect. If its first reduction has cohomology in \([a,b]\), the coefficient triangles put every reduction in that interval, with finite cohomology groups. Each inverse system of those groups is Mittag–Leffler, so completeness and the inverse-limit exact sequence put \(C\) in the same interval. Lift a basis of its top reduced cohomology to \(H^b(C)\); the coefficient triangle gives surjectivity because \(H^{b+1}(C)=0\). A map from a finite free module in degree \(b\) inducing that basis has a cone whose first reduction has top degree at most \(b-1\). Repeat downwards. At degree \(a\) the basis map is also injective on the only possible bottom reduced group, so the final cone has zero first reduction. It is complete, and therefore zero by BK.4. This constructs a bounded finite free representative of \(C\). In particular all its cohomology modules are finite over \(O\).

Integral models for arbitrary bounded constructible rational complexes, and localization of all their higher morphisms, are proved in BX.5–BX.7, using the completed-ring comparison BW. Thus
\[
\operatorname{Hom}_{D(Y,E)}(P[1/\pi],Q[1/\pi][m])
 \simeq H^m(C)[1/\pi]
\tag{B.H2}
\]
is finite dimensional for every integer \(m\). This includes derived endomorphisms of an entire complex with its extension and attaching data. It does not replace that algebra by the product of its stalk endomorphism algebras, and it does not assume realization from the derived category of the constructible heart.

**The topology detected by reductions.** Put \(Q=P\), \(A=H^0(C)\), and \(P_n=P\otimes_O^LO_n\). The evaluation-defined coefficient map BL.5, followed by BV.1, identifies the actual reduction of (B.H1) with the derived endomorphism complex of \(P_n\). Its coefficient long exact sequence gives
\[
0\longrightarrow A/\pi^nA
\longrightarrow\operatorname{End}_{D(Y,O_n)}(P_n)
\longrightarrow H^1(C)[\pi^n]\longrightarrow0.
\tag{B.H3}
\]
Thus each finite-level endomorphism group is a finite set, and the kernel of the reduction map on \(A\) is exactly \(\pi^nA\). The extra term on the right need not vanish: not every finite-level endomorphism lifts. The image \(\bar A\) of \(A\) in \(A[1/\pi]\) is a finite free lattice spanning the latter algebra; its kernel is the finite torsion submodule of \(A\). The images of \(\pi^nA\) are precisely \(\pi^n\bar A\). Consequently a compatible integral action whose finite-level endomorphisms are locally constant gives a continuous map into the rational endomorphism algebra. The continuity is for its ordinary finite-dimensional \(E\)-topology.

**Why the actual nearby action has this property.** We supply the finite-stage argument, so continuity is not inferred merely from continuity on individual stalks. Work over a strict henselian trait with separably closed residue field \(k\), fraction field \(K\), and chosen separable closure \(\bar K\). Let \(\mathcal P\) be the integral coefficient input on the total space, and let \(N\) be its complete nearby object. Lemma C.2a identifies its coherent reductions \(N_n\), with their action maps, with the ordinary finite-coefficient nearby objects. The reductions of \(\mathcal P\) are uniformly bounded below in the present application; a bounded integral constructible model more generally has a common lower bound by its finite local models. Assume \(N_1\) bounded constructible as above. Completeness, the coefficient triangles and BO.6 then make every \(N_n\) bounded constructible and locally finite perfect on a finite stratification of \(Y\).

For the finite Galois extensions \(L/K\) in \(\bar K\), let \(j_L:X_L\to X\) be the generic map and put
\[
N_{n,L}=i^*Rj_{L,*}(\mathcal P_n|_{X_L}),
\qquad
N_n\simeq\varinjlim_L N_{n,L}.
\tag{B.H4}
\]
All stages have one common lower bound: inverse images are exact and derived images are left t-exact. The second comparison is the canonical restriction map. On a strict-local stalk it is higher continuity for the inverse system of finite field extensions with affine transitions, proved in BA.5. A bounded-below cohomology filtration extends that sheaf assertion degree by degree to these complexes; in each fixed degree only finitely many terms contribute. Stalks detect the comparison. No special-fibre formula for an arbitrary nonproper image is being used. Each stage carries its canonical action through \(\operatorname{Gal}(L/K)\), and its map to \(N_n\) is equivariant for restriction of the full inertia group.

We also need continuity of Hom into this colimit. A bounded constructible finite-coefficient complex \(B\), locally perfect on a finite stratification, satisfies
\[
\varinjlim_\alpha\operatorname{Hom}(B,T_\alpha)
 \simeq\operatorname{Hom}\bigl(B,\varinjlim_\alpha T_\alpha\bigr)
 \qquad(T_\alpha\in D^{\ge c}\text{ for one fixed }c).
\tag{B.H5}
\]
This is the finite-coefficient form of the bounded-below proof BX.4. Explicitly, on a stratum a finite dual complex computes internal Hom and preserves these colimits and a common lower bound. For an open stratum use \(Rj_*R\mathcal Hom(B,j^*T_\alpha)\); for the closed complement use \(i_*R\mathcal Hom(B,i^!T_\alpha)\). Ordinary sections and qcqs derived image commute with the bounded-below colimit by finite-degree hypercover continuity. The localization fibre defining \(i^!\) gives the same continuity and a common lower bound. Induct on the finitely many strata, retaining their actual localization maps. Applying derived global sections finishes (B.H5). The étale/pro-étale comparisons in BK.2 and BV.5 identify these with the finite-coefficient category in (B.H4). There is no assertion of compactness against targets unbounded below.

Apply (B.H5) with \(B=N_n\) to (B.H4). Its identity factors through a finite stage:
\[
N_n\xrightarrow{s}N_{n,L}\xrightarrow{r}N_n,
\qquad rs=1.
\tag{B.H6}
\]
For \(g\in\operatorname{Gal}(\bar K/L)\), the stage action is the identity, so equivariance gives \(gr=r\). Hence \(g=grs=rs=1\) as an actual derived endomorphism of \(N_n\). The section \(s\) itself need not be equivariant. This proves that the finite-level action factors through a finite quotient of inertia, including all extension data; it is stronger than checking separate stalk actions. The finite extension may depend on \(n\), which is sufficient for continuity and makes no claim that the full rational tame action has finite image.

Now use (B.H3) for \(P=N\). The kernel of the action at level \(n\) is open, and its elements satisfy \(\rho(g)-1\in\pi^n A\). Its rational image therefore lies in \(1+\pi^n\bar A\). These are a neighbourhood basis at the identity in the finite-dimensional endomorphism algebra. The group homomorphism is continuous at the identity and hence everywhere. A shift of \(N\) has the same endomorphism algebra and action. The additive \(E\)-linear perverse-cohomology functor, whenever defined on these constructible complexes, induces an \(E\)-linear map from the endomorphism algebra of \(N[1/\pi]\) to that of its perverse cohomology. Both algebras are finite dimensional by (B.H2), so this map is continuous and preserves composition and identities. Composing the action with it proves continuity on perverse cohomology. This uses neither exactness of perverse cohomology on the whole derived category nor commutation of perverse truncation with finite coefficient reduction; no nearby-cycle t-exactness was used to prove continuity of \(N\).

Finally, left multiplication, not conjugation, embeds the units of \(A[1/\pi]\) faithfully in the linear automorphisms of that algebra. A continuous compact inertia image preserves an \(O\)-lattice. A pro-\(p\) wild image intersects its pro-\(\ell\) congruence kernel trivially, and therefore has finite image. The fixed-quotient and uniform-conductor deduction is exactly Weights, Lemma A.1a. This direction is not circular: (B.H1)–(B.H6) use ordinary coefficient operations, finite constructibility and continuity only; they use neither the perverse degree conclusion of this appendix nor a weight theorem.

The lemma supplies the previously implicit finite-End and continuous-action steps once the normalized nearby object has bounded constructible first reduction. It does not prove that geometric constructibility hypothesis, the ordinary affine bound, trait purity, or all recursive inputs of the linked operation providers. Over an arbitrary non-separably-closed field, finiteness of arithmetic cohomology needs its own hypotheses; we have made no such enlargement. Faithful finite coefficient extension, and the stated finite-coefficient-field convention, give the usual \(\overline{\mathbf Q}_\ell\) interpretation. \(\square\)

### Compare dimensions at the generic and special fibres

Use the dimension function

\[
\delta(x)=\operatorname{trdeg}_{\kappa(fx)}\kappa(x)
 +\begin{cases}1,&fx=\eta,\\0,&fx=s.\end{cases}
\tag{B.1}
\]

The upper test is \(H^q(i_x^*K)=0\) for \(q>-\delta(x)\); the lower test uses \(i_x^!\) and \(q<-\delta(x)\). Equivalently, glue the usual special-fibre perverse structure to the generic-fibre heart \(\operatorname{Perv}(X_\eta)[1]\). The shift also applies to components contained entirely in the generic fibre. Thus, if \(M\) lies in this generic heart, \(M[-1]\) is perverse for the usual dimension convention over the field.

**Lemma B.1.** For this convention, both \(j_!\) and \(Rj_*\) are t-exact, provided the ordinary field affine bound and the stated duality and adic comparisons hold.

**Proof.** Restriction is t-exact. Adjunction therefore makes \(j_!\) upper t-exact and \(Rj_*\) lower t-exact. We prove the missing upper bound for \(Rj_*\) by a stalk calculation; the other bound for \(j_!\) will follow by ordinary duality.

Let \(M\) satisfy the upper generic test. The closure of the support of \(H^bM\) has dimension at most \(e=-b-1\) over \(K=\kappa(\eta)\): at its generic points the stalk test gives precisely this inequality. Fix a geometric point over \(y\in X_s\), and put \(d=\operatorname{trdeg}_{\kappa(s)}\kappa(y)\). Choose a transcendence basis of this residue extension and lift it to regular functions on an affine neighborhood of \(y\). They give a map to \(\mathbb A^d_S\). Its special image is the generic point of that affine space. The strict localization \(S_d\) there is a strictly henselian discrete valuation trait with the original uniformizer, by the Gauss-ring argument of Appendix A in \(d\) variables. Write \(K_d\) for its fraction field.

Discard the finitely many closed support components whose closures miss \(y\). The chosen coordinate functions are algebraically independent on every surviving generic component. Indeed, a relation over \(K\) can be multiplied by a scalar to have coefficients in the valuation ring, at least one a unit. It vanishes on the reduced closure of that generic component. Reduction at \(y\) would give a nonzero polynomial relation on the chosen residue transcendence basis, a contradiction. The generic fibre of each such component after base change to \(S_d\) therefore has dimension at most \(e-d\): passing to the coordinate fraction field removes \(d\) transcendence degrees, and its further algebraic extension to \(K_d\) preserves that dimension.

The universal property of strict localization identifies \(X_{(y)}\) with the strict localization at the corresponding point of this base change. Its pointed affine étale neighborhoods are finite type over \(S_d\); étale pullback preserves the support bound. The finite-presentation continuity input therefore computes the desired stalk on affine generic models with support dimension at most \(e-d\), rather than on an unrelated ordinary fibre of \(X/S\).

The group calculation in the next subsection proves \(\operatorname{cd}_\ell K_d\leq1\). Apply the field affine bound of Lesson 5 to the closed support on each affine model, then pass to the pointed limit. For finite coefficients it gives

\[
H^a\bigl((X_{(y)})_\eta,H^bM\bigr)=0
\qquad\text{for }a>-b-d.
\tag{B.2}
\]

The bounded ordinary cohomology spectral sequence then vanishes in total degree \(a+b>-d\). This is exactly the upper perverse stalk test for \(Rj_*M\) at \(y\); the generic stalks already satisfy their tests. For \(E\)-coefficients, use the integral upper model of Lesson 5, with its stated field-level and stratification hypotheses. [Lemma B.1a below](#complete-the-ordinary-generic-open-fibre) identifies the actual completed coefficient fibre of its image and transfers this upper bound using the quotient transitions. No finite-stalk Nakayama assumption at the strict-local limit is needed for that step. [Proposition B.1b](#ordinary-images-constructibility-and-rational-coefficients) supplies the separate ordinary-image constructibility and rational comparison from the recorded nearby-cycle, continuous-descent and site providers. Its geometric coefficient-fibre identification makes the bound the actual rational upper test; it does not supply trait duality. Trait purity and duality in the next paragraph are separate inputs.

For the last step use the normalizing complex \(E(1)[2]\) on the regular trait. [Proposition B.1c](#base-trait-purity-with-its-divisor-orientation) supplies its divisor-oriented base restrictions. [Proposition B.1d](#family-duality-from-the-boundary-trace) deduces constructible family biduality and the evaluation-compatible exchange of the cuts in (B.1) from the specified ambient adjunctions, ordinary-image constructibility and the generic nearby/boundary-trace proofs. It does not substitute the field-only BV theorem for a trait theorem. Dualizing the upper bound just proved now gives the lower bound for \(j_!\); together with the adjoint bounds this proves the lemma under those explicit foundational inputs. Base-trait purity alone is not whole-family biduality. \(\square\)

### Complete the ordinary generic-open fibre

**Lemma B.1a (completed coefficient fibre).** Keep the trait and dimension convention of Lemma B.1, and write \(j:X_\eta\hookrightarrow X\) for the ordinary generic open, not the geometric generic-fibre map. Let \(O\) be the integers of a finite extension \(E/\mathbb Q_\ell\), put \(O_n=O/\pi^n\), and use the constant \(O\)-module sheaf on the pro-étale sites. Let \(L\) be a derived-complete complex on \(X_\eta\) whose actual derived reductions \(L_n=L\otimes_O^LO_n\) come from bounded-below étale complexes \(L_n^{\mathrm e}\). Retain their coherent quotient transitions. For a geometric point \(x:\operatorname{Spec}\Omega\to X\) over \(y\in X_s\), define

\[
B_n=(Rj_{\mathrm{\acute et},*}L_n^{\mathrm e})_{\bar x},
\qquad
C_x=R\Gamma\bigl((\operatorname{Spec}\Omega)_{\mathrm{pro\acute et}},
                 x_c^*Rj_{\mathrm{pro\acute et},*}L\bigr),
\qquad x_c^*=Cx^*.
\]

Here \(C\) is derived \(\pi\)-completion. There is a natural comparison \(C_x\simeq R\varprojlim_n B_n\) with the actual coefficient arrows. If \(H^q(B_n)=0\) for every \(n\) and every \(q>t\), then \(H^q(C_x)=0\) for \(q>t\). In particular the finite-coefficient estimate in Lemma B.1 gives \(t=-\operatorname{trdeg}_{\kappa(s)}\kappa(y)\) whenever every \(L_n^{\mathrm e}\) satisfies its upper generic test. No finite-generation hypothesis on the modules \(H^q(B_n)\) is used in this conclusion.

**Proof.** The completion and operation maps are BK.2–BK.5 and BL.6. The map \(j\) is the base change of the principal open of a uniformizer in the affine trait, so it is affine and hence qcqs. Thus the pro-étale/étale comparison (BK.4) applies to each bounded-below \(L_n^{\mathrm e}\). BK.5 says that \(Rj_*L\) is complete and that its reduction is the actual image of \(L_n\). BL.6 and (BK.9) identify the reductions of \(x_c^*Rj_*L\) with \(\nu_x^*B_n\), where \(\nu_x\) is the morphism from the pro-étale to the étale site of the geometric point.

By completeness, \(x_c^*Rj_*L\simeq R\varprojlim_n\nu_x^*B_n\). Derived sections, a right adjoint, preserves this homotopy limit. On the geometric point the étale coefficient category is the category of modules and sections is exact; (BK.3) therefore identifies \(R\Gamma(\nu_x^*B_n)\) with \(B_n\). This proves the asserted comparison. These are the same actual completion and restriction maps used in Weights, Lemma C.2a; here they are applied to the ordinary \(j\). We have not replaced its strict-local generic fibre by a geometric nearby-cycle fibre, nor interchanged an ordinary sheaf stalk with an inverse limit.

The possible extra degree in the derived limit must still be removed. Tensor the short exact sequence \(0\to O_1\xrightarrow{\pi^n}O_{n+1}\to O_n\to0\) with \(L\), then apply derived image and the exact étale stalk. The preceding comparisons preserve these coefficient maps and give the triangle

\[
B_1\longrightarrow B_{n+1}\xrightarrow{r_n}B_n\longrightarrow B_1[1].
\]

Consequently \(H^t(B_{n+1})\to H^t(B_n)\) is surjective, since \(H^{t+1}(B_1)=0\). The product-cone description of a countable derived limit gives

\[
0\longrightarrow\varprojlim{}^1 H^{q-1}(B_n)
 \longrightarrow H^q(C_x)
 \longrightarrow\varprojlim H^q(B_n)\longrightarrow0.
\]

For \(q>t+1\) both terms are zero. At \(q=t+1\), the remaining derived-limit term is the cokernel of \(1-r\) on \(\prod_n H^t(B_n)\). It vanishes: given \((b_n)\), choose \(a_1=0\) and recursively lift \(a_n-b_n\) along the surjection \(r_n\) to obtain \(a_{n+1}\). Then \(a_n-r_na_{n+1}=b_n\). Products of modules are exact, so this product-cone calculation has no further derived-product term. It is the coefficient-transition argument of BM.6, applied to these coefficient complexes rather than used to assert a new trait constructibility theorem. This proves the upper bound. \(\square\)

To use the lemma for a rational generic-upper object \(M\), first apply Lesson 5, Lemma 4.2 to \(M[-1]\), with all of that lemma's hypotheses, and take its integral upper model \(Q\). Put \(L=Q[1]\); then \(L\otimes_O E\simeq M\). For every \(n\), the triangle \(L\xrightarrow{\pi^n}L\to L_n\to L[1]\) puts \(L_n\) in the upper generic cut, since that cut contains \(L[1]\) and is extension closed. This is derived reduction, including the adjacent-degree torsion term, not underived reduction of cohomology. Bounded constructibility of the generic model supplies bounded classical reductions; if \(L\) has ordinary amplitude \([a,b]\), they have the common lower bound \(a-1\). The finite-coefficient calculation (B.2) and its spectral sequence thus apply to every \(L_n^{\mathrm e}\), giving the bound on \(C_x\). Flat scalar localization gives the same bound on \(C_x\otimes_O E\).

This last object is the rationalized completed coefficient fibre of the normalized image. The degree calculation alone does not prove whole-trait constructibility or the ordinary rational-image comparison. [Proposition B.1b](#ordinary-images-constructibility-and-rational-coefficients) supplies those comparisons separately and identifies the actual geometric coefficient fibre. Trait duality remains a different assertion. The field-level finite-fibre and Nakayama proof in Lesson 5 remains a useful alternative at its stated scope; no part of it is discarded. Lemma B.1 retains its full statement and its explicit operation and duality prerequisites.

### Ordinary images, constructibility and rational coefficients

**Proposition B.1b (the ordinary generic open).** Retain the strictly henselian trait, separated finite-type family and coefficient rings of B.1a. Put \(d=\dim X_\eta\) when the generic fibre is nonempty. Subject to the ordinary foundations of Appendix A and the site and completion providers specified below, the following statements hold.

1. If \(F\) is a bounded constructible \(O_n\)-complex on \(X_\eta\), with cohomology in \([a,b]\), then \(Rj_{\mathrm{\acute et},*}F\) is bounded constructible on \(X\), in \([a,b+d+1]\).
2. If \(L\) is derived complete and its first derived reduction is bounded classical constructible in \([a,b]\), its ordinary pro-étale image \(N=Rj_*L\) is complete. All its reductions are bounded classical constructible in \([a,b+d+1]\), with their actual quotient maps. Its ordinary integral cohomology is bounded and constructible on a finite stratification of the whole trait family.
3. Write \(R_Y=\widehat O_Y\) and \(E_Y=R_Y[1/\pi]\). Under the specified completed-ring equivalence, let \(P\) represent \(L\). There is the natural scalar-localization isomorphism

\[
 (Rj_{R,*}P)[1/\pi]
 \xrightarrow{\ \sim\ }
 Rj_{E,*}(P[1/\pi]).
\]

The right side is an ordinary bounded constructible rational sheaf complex, not merely a functor defined by central localization. Its geometric coefficient fibre is the rationalization of the completed fibre in B.1a. These conclusions hold for every bounded constructible rational input by its generic-fibre integral model. If \(X_\eta\) is empty, all these images are zero.

**Finite coefficients and the actual descent map.** Put \(C=R\psi F\) and \(B=i^*Rj_{\mathrm{\acute et},*}F\). The finite-coefficient argument of Appendix A makes \(C\) constructible in \([a,b+d]\). Continuous Galois descent identifies

\[
B\simeq R\Gamma_{\mathrm{cont}}(I,C),
\qquad I=\operatorname{Gal}(K^{\mathrm{sep}}/K),
\]

with restriction \(B\to C\) equal to its augmentation. Here derived invariants is a functor on equivariant sheaves on the special fibre, not global sections of that fibre. We spell out how the already supplied descent proof applies without incorrectly averaging full inertia. On an affine pointed neighbourhood, a finite Galois field extension gives a finite étale torsor. The augmented Čech complex is locally contracted by insertion of its diagonal section, exactly as in A.2. Its iterated fibre products give the group-cochain differential with the restriction augmentation. Pass through the finite Galois subextensions using BA.5 and the continuous resolution and finite-quotient comparison, §§2–3. A continuous cochain has finitely many values and factors through a finite quotient; these finitely many representatives and their equalities descend to a common stage. A common lower bound makes each total-degree diagonal finite. Thus the filtered passage preserves the differential, augmentation and connecting maps. Taking pointed neighbourhoods and sheafifying gives the displayed comparison. This is the continuous descent in (B.4) at finite coefficients; A.2's pro-\(p\) averaging is not asserted for \(I\).

The [inertia calculation below](#construct-the-inertia-quotient-and-its-exact-invariants) supplies \(H=\ker(I\to\mathbf Z_\ell(1))\). Its invariants are exact by prime-to-\(\ell\) averaging. For \(\Gamma=I/H\), the continuous cyclic calculation gives only degrees zero and one, the kernel and cokernel of \(T-1\) on the \(H\)-invariants. These statements apply to the cohomology sheaves of \(C\). They preserve constructibility: choose a common finite connected stratification for these finitely many constructible sheaves. On each stratum each is a finite local system. An automorphism is determined by one geometric fibre, and the continuous inertia action on that finite fibre factors through a finite group. Intersect the finitely many open kernels. Averaging for \(H\), and the kernel and cokernel of \(T-1\), are then morphisms of finite local systems on the same strata. They remain finite local systems. This uses finite actions on cohomology sheaves; it does not assume that the whole derived object has a strict action factoring through a finite quotient.

The cohomological spectral sequence

\[
\mathcal H^r_{\mathrm{cont}}(I,\mathcal H^q C)
 \Longrightarrow \mathcal H^{r+q}B
\]

has only columns \(r=0,1\). Hence \(B\) is constructible in \([a,b+d+1]\). Exact étale restriction identifies the generic restriction of \(Rj_*F\) with \(F\) and its special restriction with \(B\). Geometric stalks detect the cohomology bounds. The two finite stratifications together form a finite locally closed stratification of \(X\), so its cohomology sheaves are constructible. This proves statement 1, without a properness assumption on \(j\).

**Completion and whole-space constructibility.** The coefficient triangles \(L_1\to L_{n+1}\to L_n\) put every reduction in the same range \([a,b]\). BK.2–BK.5 identifies the actual reduction of \(N\) with \(\nu^*Rj_{\mathrm{\acute et},*}L_n^{\mathrm e}\) and proves completeness. Statement 1 gives the uniform range \([a,t]\), where \(t=b+d+1\). In the top degree the quotient triangle makes \(\mathcal H^t(N_{n+1})\to\mathcal H^t(N_n)\) surjective. The replete product-and-lifting proof of BM.6 removes the possible degree-\(t+1\) derived-limit term; no ordinary stalk is interchanged with an inverse limit. Thus \(N\) has ordinary bounds \([a,t]\).

For the constructible assertion on the whole space, use the actual ordinary open and closed restrictions, not a general finite-type-over-a-field image theorem applied to the trait. BX.1–BX.2 proves exactness, completeness preservation and joint conservativity of these restrictions from affine ind-étale neighbourhoods. That proof uses an arbitrary ring and ideal and a quasi-compact open complement; here the generic open is principal and \(X\) is Noetherian. Its coefficient-ring identities therefore apply on this trait family. The generic restriction of \(N\) is \(L\); its special restriction is complete with first reduction the bounded constructible boundary already proved. Each fibre is finite type over its field. The local finite integral models of BO.6 and the truncation comparison of BQ.4 apply there. Exact restriction identifies the cohomology restrictions, and joining the two finite stratifications proves the whole-space assertion. This does not extend all of BV's six-operation or duality results to traits.

**Ordinary rational image and its fibre.** The actual completed-ring adjunction BW.1–BW.2 uses the same two-term free coefficient complexes and completion detection on both sites. Its proof is formal at this scope. Forgetting the completed-ring action identifies \(Rj_{R,*}P\) with \(N\): scalar extension from the constant ring is exact, so restriction preserves the injective resolutions used for these images. It preserves the actual coefficient and adjunction maps.

Now apply BX.4 to

\[
P\xrightarrow{\pi}P\xrightarrow{\pi}P\longrightarrow\cdots,
\qquad \operatorname*{colim}P=P[1/\pi].
\]

This is a uniformly bounded-below tower. The proof of (BX.12) is valid on each qcqs pro-étale slice: its weakly contractible hypercover has finite diagonals in any fixed total degree, and section evaluation on its quasi-compact terms commutes with filtered colimits. For this comparison it requires qcqs and the common lower bound, not a finite-type-over-a-field target. The inverse image of a qcqs target slice under the affine \(j\) is qcqs. Consequently \(Rj_*\) commutes with this tower, giving precisely the natural displayed scalar-localization map, as in (BX.22). Flat coefficient localization and the finite integral models on both fibres prove bounded rational constructibility. Only this comparison has been extended by its stated proof; no trait exceptional-image or dualizing theorem has been inferred.

Finally take a geometric point \(x\) on a stratum of either fibre. Its pulled-back finite integral model is a finite perfect complex over \(O\). The ordinary ringed inverse image is already complete on that model, so its completion unit identifies it with \(x_c^*N\). Localization of the finite model is its ordinary rational inverse image; on the geometric point its derived sections are the corresponding finite complex of modules. Thus, with \(C_x\) as in B.1a and with the actual coefficient maps,

\[
R\Gamma\bigl((\operatorname{Spec}\Omega)_{\mathrm{pro\acute et}},
 x_E^*Rj_{E,*}(P[1/\pi])\bigr)
 \simeq C_x\otimes_O E.
\]

This is a constructible geometric coefficient-fibre comparison, not a claim that ordinary stalks commute with arbitrary inverse limits. The upper bound of B.1a therefore gives the actual rational upper test. BX.6–BX.7 supplies generic integral models for every bounded constructible rational input, including its higher-morphism comparison. Naturality of the displayed localization map makes the result independent of that model. The trait purity and duality needed for the lower test, the full classical comparison and the recursive ordinary and site foundations remain separate. \(\square\)

### Base-trait purity with its divisor orientation

**Proposition B.1c (purity of the closed point).** Let \(S\) be a henselian discrete valuation trait, with closed immersion \(i_S:s\hookrightarrow S\) and generic open \(j_S:\eta\hookrightarrow S\). Let \(O\) be the integers of a finite extension of \(\mathbf Q_\ell\), with \(\ell\) invertible on \(S\), uniformizer \(\pi\), and \(O_n=O/\pi^n\). Write \(R_Y=\widehat O_Y\) and \(E_Y=R_Y[1/\pi]\). The actual closed-support right adjoints have divisor-oriented isomorphisms

\[
Ri_{S,\mathrm{\acute et}}^!O_{n,S}(1)[2]\simeq O_{n,s},
\qquad
Ri_{S,R}^!R_S(1)[2]\simeq R_s,
\qquad
Ri_{S,E}^!E_S(1)[2]\simeq E_s.
\]

They respect coefficient quotients and residue-field descent. Their Gysin orientation sends \(1\) to the class of the closed divisor, not to its negative. The proof uses the inertia, localization and coefficient providers below; it does not assume an absolute-purity theorem for higher-dimensional regular schemes, smoothness of \(S\) over a field, or constructible duality for a family over \(S\).

**Finite coefficients.** First suppose \(S\) strictly henselian, and let \(t\) be a uniformizer of its valuation ring; \(t\) is distinct from the coefficient uniformizer \(\pi\). The support triangle is obtained from sections supported on \(s\) in an injective resolution. After exact restriction to \(s\), it gives the actual fibre

\[
Ri_S^!O_{n,S}(1)
 \simeq\operatorname{Fib}\bigl(O_{n,s}(1)
       \longrightarrow i_S^*Rj_{S*}O_{n,\eta}(1)\bigr).
\]

This is the support construction in Poincaré duality, §11, before its smooth-pair purity theorem is applied. That theorem's smooth-over-a-field hypothesis is not imposed or silently removed here.

The pointed-neighbourhood formula for an open image identifies the second term with \(R\Gamma_{\mathrm{cont}}(I,O_n(1))\), where \(I\) is the absolute Galois group of the strict fraction field. Indeed a pointed étale neighbourhood of the closed point has a section over the strict local trait; its selected strict-local germ is therefore computed on that trait itself. The field-sheaf equivalence and continuous resolution identify the map with restriction of constant sections. The [inertia quotient and cyclic calculation below](#construct-the-inertia-quotient-and-its-exact-invariants) give

\[
\begin{aligned}
H^0(I,O_n(1))&=O_n(1),\\
H^1(I,O_n(1))
 &=\operatorname{Hom}_{\mathrm{cont}}(\mathbf Z_\ell(1),O_n(1))
 \simeq O_n,\\
H^q(I,O_n(1))&=0\quad(q\geq2).
\end{aligned}
\]

All prime-to-residue-characteristic roots of unity already lie in the strict trait: lift their simple residue roots by Hensel's lemma. Thus inertia acts trivially on \(O_n(1)\). Only the prime-to-\(\ell\) kernel \(H\) is averaged; its exact invariants reduce the calculation to the continuous procyclic quotient. The middle identification is intrinsic: it cancels the source and target Tate lines, rather than selecting an arithmetic splitting. It applies to the finite \(O_n\)-module even when \(O_n\) is not free over a chosen \(\mathbf Z/\ell^a\).

The unit in the fibre induces the identity in degree zero. The long exact sequence therefore makes the fibre zero in every degree except degree two, where its cohomology is \(O_n\). In particular, purity here is a consequence of this local calculation, not a premise for the cohomology of the puncture.

**The class and the sign.** Choose \(a\) with \(\ell^aO_n=0\). The Kummer class of \(t\) with coefficients \(\mu_{\ell^a}\), followed by coefficient extension to \(O_n(1)\), is the tame character reduced to those coefficients: an automorphism acts on a chosen root of \(t\) by its root-of-unity ratio. Under the intrinsic \(H^1\) identification above this class has value \(1\). It is independent of increasing \(a\), by the compatible Kummer and quotient maps. Hence its supported localization boundary generates the unique degree-two module.

Use the fibre convention \(d(a,b)=(da,a|_\eta-db)\). Its localization boundary sends a cocycle \(b\) to \((0,-b)\). The coefficient and localization boundaries anticommute, by the double-complex lift calculation of §12, Lemma 12.2. That sign calculation uses the two resolution differentials, not smooth purity. Equivalently it is the calculation of (E.12) below before identifying the divisor class with a purity generator. Thus

\[
\operatorname{cl}_n(s)
   =-\partial_{\mathrm{loc}}\kappa_n(t)
       \ \in H^2_s(S,O_n(1)).
\]

The class on the left is the supported Kummer class of the divisor line bundle with its canonical generic trivialization. This description, or the relative cocycle in that linked calculation, fixes the sign. Define the purity orientation by \(1\mapsto\operatorname{cl}_n(s)\); the preceding one-degree calculation proves it is an isomorphism. Changing \(t\) to \(ut\) for a unit \(u\) does not change this class: the Kummer class of \(u\) extends over \(S\), so its localization boundary is zero. This also shows compatibility with pointed étale restriction.

For a general henselian trait, perform this calculation on its strict localization. The stalk and higher-continuity comparisons identify the closed-support complex there with the strict-local calculation. The class of the divisor is defined over \(S\) and preserved by its residue Galois action. On inertia the action on \(\operatorname{Hom}(\mathbf Z_\ell(1),O_n(1))\) is the simultaneous conjugation action on the first Tate line and coefficient action on the second; these cancel. Consequently its identified degree-two module has the constant residue descent \(O_n\). Geometric stalks are conservative on the small étale site, so the divisor-class map is the claimed isomorphism over \(s\) itself. No section of the residue Galois quotient has been chosen.

**Actual complete and rational supports.** On the pro-étale sites, use BX.1–BX.2. Their arbitrary-ring closed-neighbourhood construction applies to this trait and its principal generic open. In particular their actual adjoint (BX.8) is

\[
i_S^!Q=i_S^{-1}\operatorname{Fib}
          \bigl(Q\longrightarrow Rj_{S*}j_S^{-1}Q\bigr).
\]

The coefficient identities \(i_S^{-1}R_S=R_s\) and \(j_S^{-1}R_S=R_\eta\) make this the right adjoint for the completed coefficient rings as well. Exact closed restriction preserves products and derived inverse limits by that same proof. Direct image is a right adjoint and preserves those limits. The construction consequently commutes with the actual inverse system of finite coefficient constants. BK.1–BK.5 identifies their derived limit with \(R_S\) and identifies the finite pro-étale support fibres with the pullbacks of the étale fibres just computed. The finite orientation maps are compatible quotient maps because the Kummer and localization maps are. Taking their derived limit therefore gives

\[
Ri_{S,R}^!R_S(1)[2]
 \simeq R\varprojlim_n O_{n,s}\simeq R_s.
\]

The last equality uses the surjective coefficient tower and the replete product-cone calculation. It is not an interchange of ordinary stalks with inverse limits. These maps retain the closed adjunction counit, since (BX.8) retains its actual fibre map.

Finally restriction commutes with flat coefficient localization. For the image term in (BX.8), BX.4 applies on the qcqs trait slices to the common-bounded-below tower \(R_\eta\xrightarrow{\pi}R_\eta\to\cdots\). As in B.1b, it identifies the actual ordinary \(E\)-image with the localization of the \(R\)-image. Localization is exact, so it commutes with the displayed fibre. This proves the rational purity map with its counit and divisor orientation. It also gives \(j_S^*E_S(1)[2]=E_\eta(1)[2]\) with the ordinary restriction map.

In (E.11), the fibre-coordinate map \(\lambda(b)=(0,b)\) is the negative of the localization boundary. It sends the Kummer generator to \(\operatorname{cl}_n(s)\), hence to \(1\) under this purity isomorphism. Thus the base trace there has the positive normalization used in (E.12), also after completion and rationalization.

These base calculations alone do **not** prove that \(f^!E_S(1)[2]\) is a constructible dualizing complex for every \(X/S\). The supplied BV.6–BV.7 is over a field, not over an arbitrary trait. The following proposition deduces the family statement from the specified ambient operations and generic nearby/boundary-trace comparisons. Those are additional hypotheses; the base calculation alone does not imply them. \(\square\)

### Family duality from the boundary trace

**Proposition B.1d (the family deduction).** Let \(f:X\to S\) be separated and of finite type over a henselian discrete valuation trait, with \(\ell\) invertible on \(S\) and \(E/\mathbf Q_\ell\) finite. Write \(j:X_\eta\hookrightarrow X\) and \(i:Z=X_s\hookrightarrow X\). Retain the actual ambient enhanced proper-support and exceptional adjunctions, their tensor projection and composition maps, localization and multiplicative continuous descent used in Appendix D and (E.8)–(E.13). Retain their stated normalized adic/rational comparisons, the field duality providers, the ordinary-image constructibility of B.1b and the evaluation-defined generic nearby-duality comparison of Appendix D. These are the inputs; constructible biduality on \(X/S\), (E.1), and the specialization-cone duality conclusion (E.2) are **not** assumed.

Set
\[
\Omega_X=f^!E_S(1)[2],\qquad
\mathbb D K=R\mathcal Hom_E(K,\Omega_X),\qquad
\mathbb D_U L=D_{X_\eta}L(1)[2].
\]
Then \(\Omega_X\) and \(\mathbb D K\) are bounded constructible for every bounded constructible \(K\). The evaluation map \(K\to\mathbb D\mathbb D K\) is an isomorphism. Its open and closed exchanges include
\[
\begin{aligned}
j^*\mathbb D K&\simeq\mathbb D_Uj^*K,\\
i^!\mathbb D K&\simeq D_Zi^*K,\\
i^*\mathbb D K&\simeq D_Zi^!K.
\end{aligned}
\]
They are the maps induced by evaluation and the specified counits. Consequently \(\mathbb D\) exchanges the two perverse cuts for the dimension function (B.1), whose generic heart is \(\operatorname{Perv}(X_\eta)[1]\) and whose special heart is \(\operatorname{Perv}(Z)\). No excellence or smooth-curve origin is added to the trait hypothesis.

**First obtain constructibility, without using biduality.** Transitivity of the actual right adjoints and B.1c give
\[
j^*\Omega_X=\omega_\eta(1)[2],\qquad
i^!\Omega_X=\omega_Z,
\]
where \(\omega_\eta=f_\eta^!E\) and \(\omega_Z=f_s^!E\) are the field-relative complexes. For example \(f i=i_S f_s\) gives \(i^!f^!=f_s^!i_S^!\); B.1c then identifies \(i_S^!E_S(1)[2]\) with \(E_s\). For the open square use \(j^!=j^*\) and the generic base restriction. Thus the localization triangle
\[
i_*\omega_Z\longrightarrow\Omega_X
 \longrightarrow Rj_*\bigl(\omega_\eta(1)[2]\bigr)\longrightarrow
\]
and B.1b prove that \(\Omega_X\) is bounded constructible. This does not presume that ambient \(f^!\) already preserves all constructible complexes.

The raw tensor–Hom adjunctions similarly give the open identity above and
\[
i^!R\mathcal Hom_E(K,\Omega_X)
 \simeq R\mathcal Hom_E(i^*K,i^!\Omega_X).
\]
To see its map, test against a closed-fibre complex \(A\): the closed projection formula identifies \(i_*A\otimes K\) with \(i_*(A\otimes i^*K)\), and the adjunction \(i_*\dashv i^!\) transposes evaluation into the displayed Hom. The same argument on every étale slice gives the internal identity. No inverse of a family biduality map is used. Both \(i^!\mathbb D K\) and \(j^*\mathbb D K\) are therefore bounded constructible by field duality. Applying localization and B.1b once more proves the same for \(\mathbb D K\). Also \(i^!K=i^*\operatorname{Fib}(K\to Rj_*j^*K)\) is bounded constructible by that same ordinary-image result; thus the closed dual in the next step belongs to the stated field category.

**Construct the other closed comparison.** Define
\[
\chi_K:i^*\mathbb D K\longrightarrow D_Zi^!K
\]
as the adjoint of the supported evaluation pairing
\[
i^*\mathbb D K\otimes i^!K
 \longrightarrow i^!(\mathbb D K\otimes K)
 \longrightarrow i^!\Omega_X=\omega_Z.
\]
The first arrow is the mate of the closed projection formula followed by the support counit \(i_*i^!K\to K\). This defines a natural morphism of exact contravariant functors, including their triangle maps and signs.

For \(K=i_*A\), internal exceptional adjunction gives \(\mathbb D i_*A=i_*D_ZA\). Both closed restrictions of \(i_*\) are the identity. The map \(\chi_{i_*A}\) is therefore the identity on \(D_ZA\): the support counit on an object in the image of \(i_*\) is its adjunction identity. It remains to check \(K=j_!L\), since every \(K\) belongs to the functorial triangle \(j_!j^*K\to K\to i_*i^*K\to\).

Put \(B(L)=i^*Rj_*L\). Internal open adjunction, rather than family biduality, gives \(\mathbb D j_!L=Rj_*\mathbb D_U L\). Localization gives \(i^!j_!L=B(L)[-1]\) with the specified fibre-coordinate map (E.8). Hence the comparison to prove is
\[
\chi_{j_!L}:B(\mathbb D_U L)
 \longrightarrow D_Z\bigl(B(L)[-1]\bigr).
\]
Let \(C=R\psi L\). The evaluation comparison of Appendix D identifies \(R\psi\mathbb D_U L\) with \(D_ZC(1)[2]\), with its full inertia and residue descent. Continuous descent and the group-duality pairing (E.4) consequently give
\[
\begin{aligned}
B(\mathbb D_U L)
 &\simeq R\Gamma(I,D_ZC)(1)[2]\\
 &\simeq D_ZR\Gamma(I,C)[1]
  =D_Z\bigl(B(L)[-1]\bigr).
\end{aligned}
\]
This argument does not discard wild inertia. The exact \(H\)-averaging projector and the bounded Fitting decomposition at the start of Appendix E split off the generalized eigenvalue-one part. Its two-term computation is (E.4). The other tame eigenvalues have invertible \(T-1\), and the complementary \(H\)-part has zero derived invariants. Their dual parts have the same vanishing: averaging is self-adjoint and \(T^{-1}-1=-T^{-1}(T-1)\). Thus the displayed comparison applies to the entire \(C\). The logarithms used on its unipotent part require \(E\); this is not a proof of the larger torsion sliced-topos assertion.

An abstract isomorphism would not suffice to identify \(\chi\). Its defining pairing is precisely the lower supported product of (E.9), with inputs \(M=\mathbb D_U L\), \(N=L\), followed by evaluation and \(q_X\). The calculation (E.10)–(E.13) identifies that map with the nearby evaluation followed by the continuous-inertia trace. The base trace is positive by B.1c and (E.11)–(E.12); (E.8) is the negative of the localization boundary, and (E.9) retains the tensor-shift sign. After tensor symmetry, with its Koszul signs, this is exactly the perfect pairing defining (E.4). Therefore the actual \(\chi_{j_!L}\), not merely some map with the same objects, is an isomorphism. Exactness applied to the preceding open–closed triangle proves that \(\chi_K\) is an isomorphism for all bounded constructible \(K\).

There is no circular use of the later specialization proof in this step. The part of Appendix E used here is the field-valued group calculation (E.4), the localization construction (E.8)–(E.10), and the coefficient/exceptional-trace comparison (E.11)–(E.13). Those calculations need the raw adjunctions, the two restrictions of \(\Omega_X\), B.1c and Appendix D. They do not use (E.1), the dualized attaching diagram (E.5), its contraction (E.6), or the conclusion (E.2).

**Now test the canonical double evaluation.** The closed tensor structure defines \(\eta_K:K\to\mathbb D\mathbb D K\). Open restriction identifies it with field double evaluation for \(\mathbb D_U\); the line twist and the shift cancel on applying this duality twice. On the closed fibre consider
\[
i^*K\xrightarrow{i^*\eta_K}i^*\mathbb D\mathbb D K
 \xrightarrow{\chi_{\mathbb D K}}
D_Zi^!\mathbb D K\simeq D_ZD_Zi^*K.
\]
This composite is field double evaluation. Indeed, transpose it against \(D_Zi^*K\) and expand the definitions of \(\chi\) and the raw closed Hom identity: the closed projection formula moves the test object through \(i_*\), and the support counit meets its adjunction unit. Their triangle identity leaves evaluation on \(i^*K\), with the tensor symmetry already used to define \(\eta_K\). This identifies the map and not only its target. Field biduality therefore makes the composite invertible. The second arrow and final identification are already invertible, so \(i^*\eta_K\) is invertible. Exact open and closed restrictions are jointly conservative; their vanishing on the cone of \(\eta_K\) proves biduality on \(X\).

The same evaluation construction gives \(\mathbb D\eta_K\circ\eta_{\mathbb D K}=1\), by the two closed tensor evaluation identities. Thus the proved double evaluation is coherent and the stated exchanges retain their actual adjunction maps. On \(Z\) these exchanges interchange the field perverse stalk and costalk tests. On \(X_\eta\), if \(L=P[1]\), then \(\mathbb D_U L=(D_{X_\eta}P)(1)[1]\); field perverse self-duality therefore interchanges the shifted generic cuts as well. These are exactly the glued tests of (B.1). This proves the asserted perverse self-duality and supplies (E.1).

The remaining foundational work is specific: the ambient proper-support/exceptional construction and coherence, and the recursive ordinary and normalized adic providers used above. The family deduction no longer needs a separate unproved biduality assertion, but it does not certify those inputs. The regular one-dimensional-base alternative in [Lu–Zheng, version 7](https://arxiv.org/abs/1712.10216v7), in the discussion of dualizing complexes, provides a matching finite-coefficient scope comparison; it is not substituted for this rational-coefficient proof or for the ambient constructions. \(\square\)

### Ordinary proper support and its adjoint over a Noetherian base

**Proposition B.1e (the ordinary torsion stage).** Let \(f:X\to Y\) be separated and of finite type between Noetherian schemes, and let \(\Lambda\) be a commutative ring killed by a positive integer. The earlier programme constructions give an exact coproduct-preserving functor
\[
Rf_!:D(X_{\mathrm{et}},\Lambda)\longrightarrow D(Y_{\mathrm{et}},\Lambda)
\]
on unbounded ordinary complexes, with an exact right adjoint \(f^!\). The proper-support functors have their canonical compactification-independent, associative composition and base-change comparisons, and satisfy the derived tensor projection formula. In particular this construction applies to finite-type schemes over an arbitrary henselian discrete valuation trait. The base need not be excellent or arise from a smooth curve; the torsion order need not be invertible for this ordinary construction. This assertion does **not** yet assert constructibility, exceptional coefficient-change, normalized adic adjunctions or rational-coefficient operations.

**Proof from the supplied providers.** The needed compactification is The right adjoint of derived pushforward, Appendix N, Theorem N.E.1. Its proof is Noetherian-relative, not field-relative: N.A retains scheme-theoretic closures and the protected opens in blowup charts; N.B eliminates the rational section while protecting the specified larger open; N.C and N.D assemble two compactifications; N.E handles a finite affine cover. The dense affine cover used there is explicitly constructed in the retained Chow provider, Theorem 4.1. Around a point, take an affine open avoiding the components not through that point, and add disjoint affine opens of the remaining generic points. The finite disjoint union is affine and contains every generic point. A finite cover by these opens has dense intersection. The relative coordinate construction in N.E works even for a nonaffine base. These arguments preserve the original open source, including nilpotents. The alternative quasi-affineness input from AW.5 is available as specified in BG.5; neither that alternative nor the original N.A.4 route is discarded.

Choose the resulting \(X\xrightarrow{j}\overline X\xrightarrow{p}Y\), and put \(Rf_!=Rp_*j_!\). The field label of the assembled BG statement is not itself an extension theorem. The relevant proof is BG.2–BG.4: proper geometric fibres reduce the cohomological bound to schemes over algebraically closed fields, regardless of the original base. Finite affine charts give a uniform finite fibre-dimension bound, so the cycle-sequence argument of BG.3 applies to arbitrary complexes. BG.4 proves the actual unbounded proper base-change map and coproduct preservation from this bound and ordinary higher-direct-image continuity. Exact open extension by zero preserves coproducts. Their composite is therefore the asserted exact coproduct-preserving functor on the full ordinary derived category.

For precision, independence uses the actual proper–open exchange, not an unspecified isomorphism of objects. In a commuting square with proper vertical maps and open horizontal maps, the induced open in the cartesian proper pullback is proper and hence clopen. Restricting to the bottom open identifies the two functors by this clopen pushforward; the open adjunction determines their comparison globally. Off that open, proper base change makes both sides zero. Cohomology with compact support, Lemma 6.1 and Theorems 7.1–9.1 prove vertical and horizontal pasting for this map and carry it through common compactification refinements. Their proofs use the Noetherian compactifications just supplied and BG.4; no field hypothesis is used in the pasting. They therefore give the identity, cocycle, composition and base-change compatibilities here. This is ordinary derived-functor coherence; it is not a substitute for the enhanced diagram construction required later.

The tensor map is also identified. The same lesson, Lemma 10.1, Proposition 10.2 and Theorem 10.3 prove
\[
Rf_!K\otimes^L M\xrightarrow{\sim}
Rf_!\bigl(K\otimes^L f^*M\bigr).
\]
For proper \(p\), its geometric stalk is the global-sections tensor map on a proper geometric fibre. The preceding finite cohomological bound makes global sections preserve coproducts on unbounded complexes. Testing the tensor comparison on shifts of \(\Lambda\), and then free resolutions and their homotopy colimits, proves it for every coefficient complex. Exact proper base change identifies this test with the actual counit-defined projection map. Open extension by zero preserves K-flatness by its stalk description, so the proper formula gives the displayed formula for \(f=pj\). The refinement exchange preserves this same map. No finite global dimension of \(\Lambda\) is assumed.

Finally BF.5–BF.6, using Lemma 1.F and Theorem 1.G, supplies the right adjoint on the small étale site. Free representable presheaves are compact generators of the presheaf derived category. Exact sheafification \(a\) has fully faithful right adjoint \(Ri\). For a cohomological product-valued functor \(H\), represent \(H\circ a\) by \(L\). In the triangle \(N\to L\to Ri(aL)\to\), one has \(aN=0\); adjunction gives \(\operatorname{Hom}(N,Ri(aL)[-1])=0\), and representation gives \(\operatorname{Hom}(N,L)=0\). Hence \(\operatorname{Hom}(N,N)=0\), so \(L=Ri(aL)\) and \(aL\) represents \(H\). Applying this to \(H(K)=\operatorname{Hom}(Rf_!K,B)\) constructs \(f^!B\). BF.6 checks its naturality and exactness. This does not assume that the sheafified generators are compact.

Taking right adjoints of the established composition isomorphism gives the ordinary transitivity isomorphism \((gf)^!\simeq f^!g^!\): both sides represent the same Hom functor, and the unique isomorphism intertwines their counits. The associativity and units agree for the same reason. This proves the stated ordinary stage from its exact programme providers. It does not prove that tensor reduction commutes with this right adjoint; that is a separate comparison, not a consequence of existence or uniqueness. \(\square\)

B.1d requires compatible enhanced operations and coefficient constructions: exceptional reduction maps and uniform bounds, whole-diagram adjunctions, normalized completion and rational localization comparisons. Applying the field-scoped arguments BV.2–BV.4 at a trait requires proofs at that trait scope. The ordinary construction and family-duality deduction do not by themselves give an unconditional rational six-operation theorem.

### Smooth trace and coefficient change over the trait base

**Proposition B.1f (smooth ordinary coefficients).** Let \(p:X\to Y\) be separated and smooth of finite presentation, of pure relative dimension \(d\), between Noetherian schemes. Let \(n\geq2\) be invertible on \(Y\), put \(\Lambda=\mathbf Z/n\), and let \(R\) be a commutative \(\Lambda\)-algebra. Set \(R(d)=R\otimes_\Lambda\Lambda(d)\). For every, possibly unbounded, \(B\in D(Y_{\mathrm{et}},R)\), the trace-defined comparison is an isomorphism
\[
p^*B\otimes_R R(d)[2d]\xrightarrow{\sim}p_R^!B.
\tag{B.SC1}
\]
Its counit is the projection formula followed by the positive Kummer-normalized trace. It respects smooth composition and base change and is compatible with arbitrary coefficient homomorphisms \(R\to R'\). In particular, no flatness or finite projective dimension of \(R'\) over \(R\) is required. For \(B\in D^{[a,b]}\), the exceptional image has degrees \([a-2d,b-2d]\). If \(R\) is Noetherian, bounded constructible inputs remain bounded constructible. The statement applies over an arbitrary henselian discrete valuation trait on which \(n\) is invertible; no excellence or field-base assumption is added.

**The already available general-base proof.** Proposition E.2k identifies the relevant companion, not merely a field-scoped analogue. Poincaré duality for smooth varieties, Theorem 9.1 is stated for a quasi-compact, quasi-separated base and every complex of \(\Lambda\)-modules. Its Theorem 2.1 and formula (2.3) construct the trace, its positive divisor normalization, smooth composition, base change and extension to arbitrary input complexes. Thus the base condition here is within that theorem's stated scope.

The strict-local input has the following base and finite-presentation hypotheses. In Sections 4–6, the selected base is a strict henselization \(T\), and the source is \(U\times_VT\) for its selected map \(T\to V\); it is not the union of all sheets of \(U\times_YT\). The morphism to \(T\) is separated of finite presentation, and \(\Lambda(1)\) is finite locally constant. Compact supports, Theorem 12.3 therefore gives constructible compact-support cohomology on this actual base. Its affine-line proof input is an additional prerequisite of the compact-support assertion. Constructible image supports and compactness of the constructible topology turn the stalkwise zero transitions into uniform zero cohomology maps. A bounded chain of such maps kills the derived trace-cone map. Finite-presentation descent gives an actual refined neighbourhood map; smooth-coordinate induction and the trace composition law give the same conclusion in dimension \(d\).

The companion's Section 9 then applies Hom from this trace system into the arbitrary complex \(A[r]\). Because a later cone map itself is zero, every such Hom class dies; no boundedness or finite projective resolution of \(A\) is used. The local adjunction formula (8.2) identifies this Hom colimit with the stalk of \(p_\Lambda^!A\), while the other side is the stalk of \(p^*A(d)[2d]\). Both maps are induced by the same trace, so this proves the comparison, not only an equality of stalk dimensions. The ordinary adjoint constructed in B.1e is identified with the companion's adjoint by the unique adjunction isomorphism preserving the counit. The field-only label on the separate BV statement is consequently not being used to extend its theorem.

**Restriction of coefficients and the actual adjunction.** Let \(f:Z\to W\) be any separated finite-type map of Noetherian schemes. For a coefficient homomorphism \(R\to R'\), write \(L_Z=R'\otimes_R^L-\), \(L_W=R'\otimes_R^L-\), and \(U_Z,U_W\) for exact restriction of coefficients. The proper-support part of BV.1, together with B.1e, gives the canonical map
\[
L_W Rf_{!,R}\xrightarrow{\sim}Rf_{!,R'}L_Z.
\tag{B.SC2}
\]
Here only the proper-support argument is used. The hypercover section comparison respects coefficient restriction; the finite proper-fibre bound extends it to arbitrary complexes. Open extension by zero is exact on its zero or unchanged stalks. For a coefficient complex \(P\), the projection map is invertible first for \(P=R\), and then for all \(P\) by shifts, coproducts, free cell resolutions and their homotopy colimits. This uses the unbounded projection formula and coproduct preservation of B.1e, not the field-scoped ordinary-image bound M.1. Applying it to \(P=R'\), and using conservative coefficient restriction, proves (B.SC2). Tensor associativity and the same projection map identify successive extensions. In particular the proof does not assume that restriction preserves injective objects.

For \(E\in D(Z,R)\) and \(B'\in D(W,R')\), the two adjunctions now give
\[
\begin{aligned}
\operatorname{Hom}(E,U_Zf_{R'}^!B')
&=\operatorname{Hom}(L_ZE,f_{R'}^!B')\\
&=\operatorname{Hom}(Rf_{!,R'}L_ZE,B')\\
&=\operatorname{Hom}(L_WRf_{!,R}E,B')\\
&=\operatorname{Hom}(E,f_R^!U_WB').
\end{aligned}
\tag{B.SC3}
\]
Yoneda yields \(U_Zf_{R'}^!\simeq f_R^!U_W\), with the counit comparison specified by this calculation. This is the coefficient-*restriction* identity of BV.2, formula (BV.4). It is not yet an exceptional scalar-extension isomorphism for a non-smooth \(f\).

Apply (B.SC3) to \(\Lambda\to R\) and the smooth \(p\). Extend the companion's trace to \(R\) via (B.SC2), use projection, and transpose to define (B.SC1). Under restriction to \(\Lambda\), its pairing is the companion's formula (2.3) for \(U_YB\): associativity identifies the pairing with \(U_YB\otimes_\Lambda^L Rp_{!,\Lambda}\Lambda(d)[2d]\) followed by the same trace. Its underlying comparison is therefore Theorem 9.1. Since restriction is conservative, (B.SC1) is an isomorphism. This establishes the \(R\)-linear formula without any finite-generation or self-injectivity assumption on \(R\).

**Exceptional extension for smooth maps.** For arbitrary \(f\), there is a canonical comparison
\[
\gamma_{f,B}:L_Zf_R^!B\longrightarrow f_{R'}^!L_WB.
\tag{B.SC4}
\]
It is defined by applying \(Rf_{!,R'}\) to the left side, using (B.SC2), extending the \(R\)-counit, and transposing. When \(f=p\) is smooth, substitute (B.SC1) on both sides. Tensor associativity and the pullback comparison identify both with
\[
p^*(R'\otimes_R^LB)\otimes_{R'}R'(d)[2d].
\tag{B.SC5}
\]
The resulting map is the identity comparison of these tensor expressions: after transposition, each is projection followed by the trace extended to \(R'\). Thus \(\gamma_{p,B}\) is an isomorphism, including nonflat quotient maps. For \(R\to R'\to R''\), both composites transpose to the counit extended once to \(R''\); the same calculation with the composed smooth trace proves compatibility with geometric composition and base change. These are identities of the specified ordinary comparisons, not unspecified isomorphisms of objects.

The twist is invertible and pullback exact, so (B.SC1) gives the displayed amplitude. Pullback and tensor by an invertible local system preserve finite constructible stratifications and finitely generated stalks, proving the Noetherian-coefficient constructibility assertion. For the finite quotients \(O/\pi^m\) used later, a common power of the residue characteristic annihilates any fixed finite diagram of levels. The proof therefore applies to every transition and its composites, and its smooth amplitude does not depend on the level. This does not assume that tensor reduction of an arbitrary bounded complex stays bounded. \(\square\)

The smooth comparison alone does not imply the full operation premise of B.1d. For a general closed immersion, BV.2 also uses the complementary ordinary image \(Rj_*\) in the closed-support triangle. Its arbitrary-trait coefficient comparison, uniform bound and constructibility must be justified before using local closed–smooth factorizations to prove general exceptional scalar extension. Likewise, smooth levelwise compatibility does not by itself construct the adjunction on whole coefficient diagrams, prove that its right adjoint preserves derived-cartesian constructible systems, or identify normalized completion and rationalization. The general coefficient comparison therefore requires those closed-support and whole-diagram constructions in addition to the smooth comparison.

### Finite-coefficient operations on the whole trait family

**Proposition B.1g (finite coefficients, including non-smooth maps).** Let \(S\) be a henselian discrete valuation trait and let \(\ell\) be invertible on \(S\). Let \(f:X\to Y\) be an \(S\)-map between separated finite-type \(S\)-schemes. For a finite commutative ring \(R\) annihilated by a power of \(\ell\), the ordinary functor \(Rf_{*,R}\) has finite cohomological dimension with a bound depending only on the geometry, not on \(R\), and preserves bounded constructibility. The ordinary adjoint \(f_R^!\) of B.1e also preserves bounded constructibility and has coefficient-independent bounds on each fixed input interval. For a homomorphism \(R\to R'\) of these rings, the actual comparisons
\[
R'\otimes_R^L Rf_{*,R}K\xrightarrow{\sim}
Rf_{*,R'}(R'\otimes_R^LK),\qquad
R'\otimes_R^Lf_R^!B\xrightarrow{\sim}
f_{R'}^!(R'\otimes_R^LB)
\tag{B.TF1}
\]
hold for arbitrary, possibly unbounded, complexes. They respect successive coefficient changes and geometric composition. No excellence assumption is added to the trait. These are ordinary finite-coefficient assertions; a completed or rational six-operation statement is not being asserted here.

**The two fibres supply different inputs.** Write \(u_Z:Z_\eta\hookrightarrow Z\) and \(i_Z:Z_s\hookrightarrow Z\) for \(Z=X,Y\). First suppose the trait strictly henselian. Proposition B.1b supplies constructibility for \(Ru_{Z,*}\), with bound \(c_Z=\dim Z_\eta+1\) when the generic fibre is nonempty. Set \(c_Z=0\) if that fibre is empty. Only its finite-coefficient proof is used: Appendix A constructs finite nearby-cycle sheaves, and continuous inertia descent has just the two columns of kernel and cokernel after exact prime-to-\(\ell\) invariants. That proof works for every finite \(R\) here. Its finite groups, sheaf maps, averaging and cohomology sequences are \(R\)-linear; neither a valuation-ring lift of \(R\) nor any completion enters this part of B.1b.

The same bound holds for arbitrary \(R\)-module sheaves, not only constructible ones. Their underlying sheaves are annihilated by a fixed power of \(\ell\). Express them as filtered colimits of finite constructible module sheaves using the finite-presentation generators of the constructible-sheaf companion, as in E.2m's coefficient input. These presentations need not be subsheaves. BA.5 gives filtered-coefficient continuity on each qcqs inverse-image étale slice of the affine \(u_Z\). All terms have the same bound \(c_Z\), so their colimit does too. The free-module hypercover contraction in BB.3 identifies this computation with module-sheaf derived image. It does not assume that coefficient restriction preserves injectives.

For \(f_\eta\) and \(f_s\), use the genuine field theorems M.1 and M.4, or equivalently E.2m with a field as parameter base. Over a field its dense open is the entire base. They give geometry-only bounds \(c_\eta,c_s\) on arbitrary module sheaves and bounded constructibility over these finite rings. Finite affine covers give sufficient such bounds; they need not be sharp. No field theorem is being applied directly to \(f\).

**A closed-fibre defect, not a generic-base-change assertion.** For a sheaf \(F\) on \(X\), form the adjunction triangle
\[
D_X(F)\longrightarrow F\longrightarrow Ru_{X,*}u_X^*F
 \longrightarrow D_X(F)[1].
\tag{B.TF2}
\]
Its left term is in degrees \([0,c_X+1]\), by the long exact sequence. Its generic restriction is zero, because the open adjunction unit restricts to the identity. Exact closed pushforward and its stalkwise localization triangle identify
\(D_X(F)\simeq i_{X,*}i_X^*D_X(F)\).
This identification does not require the defect to be constructible. Derived direct-image composition therefore gives
\[
Rf_*D_X(F)\simeq i_{Y,*}Rf_{s,*}i_X^*D_X(F),\qquad
Rf_*Ru_{X,*}u_X^*F\simeq Ru_{Y,*}Rf_{\eta,*}u_X^*F.
\tag{B.TF3}
\]
The two bounds proved above put these objects in \([0,c_X+1+c_s]\) and \([0,c_\eta+c_Y]\), respectively. Applying \(Rf_*\) to (B.TF2) consequently proves the sufficient bound
\[
c_f=\max\{c_X+1+c_s,\ c_\eta+c_Y\}.
\tag{B.TF4}
\]
Every constant in this expression comes from geometry and finite covers. In particular none grows with the coefficient exponent. Empty fibres give zero functors and cause no exception to the bound. A bounded input in \([a,b]\) has image in \([a,b+c_f]\), by its finite cohomology tower.

If \(F\) is constructible, B.1b makes the third term of (B.TF2) bounded constructible. Its defect and closed restriction are therefore bounded constructible. The first object of (B.TF3) is constructible by the special-fibre field theorem. The second is constructible by the generic-fibre field theorem followed by B.1b on \(Y\). The triangle proves bounded constructibility of \(Rf_*F\). Finite truncation triangles prove it for every bounded constructible complex. This uses neither unknown nearby-cycle finiteness nor family biduality: the specific nearby-cycle argument in Appendix A is an earlier input.

For an arbitrary henselian trait, pull back to its strict henselization. It is an affine limit of pointed étale neighbourhoods. Étale restriction and BA.5 identify the ordinary images after this pullback, first degree by degree and then on the finite windows above. Pullback is exact and conservative. Constructibility descends by the finite-presentation detection argument used in M.1; geometric stalks detect the bound. The finite affine covers used for the constants persist under this algebraic base extension. Thus the result is on the original trait, not only on a chosen geometric fibre.

The source route for this assembly is [Deligne, *Théorèmes de finitude*, Theorem 1.1 and §§3.10–3.12](https://publications.ias.edu/sites/default/files/Number32.pdf), printed pp.233–234 and 248–249. Its regular dimension-one hypothesis does not include excellence. Here the already supplied B.1b and field arguments provide its two fibre inputs; (B.TF2)–(B.TF4) also exhibit the uniform ordinary bound needed below. E.2l–E.2n by themselves give dense-open results and would not justify silently including the special fibre.

**Coefficient extension and the closed-support comparison.** With the bound (B.TF4), the proof of BV.1 now applies to this \(f\). Filtered-coefficient continuity first gives coproduct preservation on sheaf cohomology. The finite-window resolution argument extends it to unbounded complexes. For a coefficient complex \(P\), the projection map is an isomorphism for \(P=R\). Both sides are exact and preserve coproducts; the free-cell resolution and its homotopy colimit extend the comparison to every \(P\in D(R)\). Taking \(P=R'\), and checking after conservative restriction of coefficients, proves the first comparison in (B.TF1). This includes nonflat quotients and does not assume finite projective dimension of \(R'\).

For a closed immersion \(v:Z\hookrightarrow W\) in a separated finite-type trait scheme, with complementary open \(w\), use the actual closed-support counit triangle
\[
v_*v_R^!B\longrightarrow B\longrightarrow Rw_*w^*B
 \longrightarrow v_*v_R^!B[1].
\tag{B.TF5}
\]
The just-proved ordinary coefficient comparison applies to this arbitrary open \(w\), not only to a generic-fibre open. Extending (B.TF5) gives the corresponding triangle over \(R'\). Exact closed pushforward commutes with extension on its zero or unchanged geometric stalks. Consequently the exceptional comparison is invertible. As in BV.2, it is the map defined by extending the counit and transposing, not an arbitrarily chosen isomorphism of fibres.

On affine source and target pieces, factor \(f\) as a closed immersion into \(\mathbb A^N_{Y_0}\), followed by the smooth projection. B.1f supplies the smooth trace and coefficient comparison over this base; (B.TF5) supplies the closed step. Open restriction of the adjoint follows from the composition of its left functors and preserves the counit. These local identifications are conservative, so they prove the second comparison of (B.TF1) globally. Transposing consecutive coefficient comparisons gives the same extended counit. This proves the asserted coherence, including geometric composition, without changing the specified maps.

For \(B\) in \([a,b]\), the smooth piece is in \([a-2N,b-2N]\). If the complement in that affine factorization has ordinary bound \(c_w\), (B.TF5) gives the sufficient interval \([a-2N,b-2N+c_w+1]\). Finitely many such pieces give a common interval independent of \(R\). The same triangle, the ordinary constructibility just proved, and smooth pullback with its invertible twist show that \(f_R^!B\) is bounded constructible. These bounds do not claim that derived reduction of an arbitrary bounded complex remains bounded. \(\square\)

This proves the finite-coefficient comparison for the non-smooth case of B.1f. The whole-diagram right adjoint, its derived-cartesian restriction, normalized completion and the actual rational comparisons still require their separate constructions. In particular B.1d's ambient rational-operation premise remains explicit. The whole-diagram, completion and rationalization comparisons are additional hypotheses of the ambient rational-operation statement.

### Whole coefficient diagrams and complete adjunction over the trait

**Proposition B.1h (the complete coefficient stage).** Let \(S\) be an arbitrary henselian discrete valuation trait with \(\ell\) invertible, and let \(f:X\to Y\) be a map between separated finite-type \(S\)-schemes. Fix a complete discrete valuation ring \(O\), a uniformizer \(\pi\), and a finite residue field of characteristic \(\ell\); set \(O_n=O/\pi^n\). On \(Z_{\mathrm{pro\acute et}}\), use the constant coefficient sheaf \(\underline O\), not an identification of it with \(\widehat O=\varprojlim\underline{O_n}\). Let \(\mathscr C_Z\) consist of derived-complete \(\underline O\)-complexes whose first derived reduction is a bounded constructible classical étale complex. Then the proper-support and exceptional functors constructed below preserve these categories and have a full adjunction
\[
Rf_!^c:\mathscr C_X\rightleftarrows\mathscr C_Y:f_c^!,
\qquad (f_c^!L)_n\simeq f_{O_n}^!L_n.
\tag{B.DC1}
\]
The reduction comparison includes the specified transitions, units and counits. The construction respects composition. For a smooth map of pure relative dimension \(d\) and a closed immersion with open complement, respectively, it gives
\[
p_c^!L\simeq p_c^*L(d)[2d],\qquad
i_*i_c^!L\longrightarrow L\longrightarrow Rj_*j_c^*L
 \longrightarrow i_*i_c^!L[1].
\tag{B.DC2}
\]
No excellence or smooth-curve-origin hypothesis is imposed on \(S\). This is the complete, reduction-defined category, with all its derived morphisms. Comparison with actual rational sheaves, and realization from the bounded derived category of its strict-system heart, are separate statements.

**Which parts of the earlier construction apply here.** BK.1–BK.5 use the pro-étale covering constructions over arbitrary rings, the classical bounded-below site comparison and the two-term free resolution of \(O_n\) over \(O\). They give the completion functor \(C_Z\), its adjunction unit, unchanged derived reductions and compatibility of direct image with completion. These steps require neither a field base nor constructibility of a nonproper image. The first part of BM.6 likewise uses only coefficient triangles and closure of finite constructible sheaves under extensions. If the first reduction lies in \([a,b]\), every reduction is classical constructible in that same interval. The needed geometric finiteness will be supplied by B.1g, not by treating BM's opening field hypothesis as already removed.

Let \(\mathcal A_Z^{\mathrm e}\) be the abelian category of actual étale \((O_n)_n\)-module diagrams, and let \(\mathcal A_Z^{\mathrm p}\) be its pro-étale counterpart. The free generators indexed by a site object and an integer, exact componentwise sheafification and simultaneous flat resolutions in BR.1 are site constructions. They apply on these same schemes. Write \(D_{\mathrm{cart,cons}}(\mathcal A)\) for the full subcategory whose transition maps induce
\[
O_n\otimes_{O_{n+1}}^L M_{n+1}\xrightarrow{\sim}M_n
\tag{B.DC3}
\]
and whose first component is bounded constructible, classical in the pro-étale case. The morphisms are those in the derived category of whole diagrams, not families of finite-level morphism classes.

BR.2–BR.4 prove that derived reduction and derived limit are inverse equivalences between complete complexes and cartesian pro-étale diagrams. In particular, for a cartesian \(M\), the adjunction counit identifies
\[
(\operatorname{holim}_n M_n)\otimes_O^L O_r\xrightarrow{\sim}M_r.
\tag{B.DC4}
\]
The decisive conservativity argument uses the exact sequence
\(0\to O_{m-r}\xrightarrow{\pi^r}O_m\to O_r\to0\): after simultaneous flat resolution it is a triangle of actual diagrams; taking its limit shows that zero limit forces every component to vanish. Thus the equivalence supplies the coefficient actions and the maps, not merely matching underlying complexes.

BS.1–BS.3 compare the two diagram sites. Their derived-prefix adjunction identifies each evaluation of derived site image with the finite-level derived image, including transitions. The bounded-below classical comparison in BK.2 then makes the diagram unit and counit isomorphisms on the classical subcategory. The coefficient triangles just described give a common finite interval, so this bounded-below condition is met here. Consequently there is an equivalence
\[
E_Z:D_{\mathrm{cart,cons}}(\mathcal A_Z^{\mathrm e})
 \xrightarrow{\sim}\mathscr C_Z,
\qquad E_Z(M)=\operatorname{holim}_n\nu_Z^*M_n.
\tag{B.DC5}
\]
Its inverse is \(R\nu_{Z,\mathrm s,*}(K\otimes_O^LO_n)_n\). The equivalence itself uses no field finiteness theorem, no duality and no rationalization. BM.6's coefficient-triangle and product-cone proof also bounds the complete object: possible cohomology above the common top degree is killed by the epimorphic top-degree transition tower. This establishes the boundedness needed here without asserting that arbitrary derived scalar extension preserves boundedness.

**The adjoint is constructed before restricting the diagrams.** Use the Noetherian compactification supplied in B.1e, \(f=pj\). Its proper middle scheme is again separated and finite type over \(S\). On the full unbounded diagram categories define
\[
F_f=Rp_{\mathrm s,*}j_{\mathrm s,!}:
D(\mathcal A_X^{\mathrm e})\longrightarrow D(\mathcal A_Y^{\mathrm e}).
\tag{B.DC6}
\]
For evaluation \(e_n\), its derived left adjoint \(Le_{n,!}\) has component \(O_m\otimes_{O_n}^LH\) at \(m\leq n\), and zero above \(n\), with the quotient transitions. The BS.2 adjunction calculation, with \(p\) in place of the site map, gives
\[
e_nF_fK\simeq Rf_{!,O_n}K_n.
\tag{B.DC7}
\]
Here inverse image commutes with the derived prefixes. This calculation does not assume that evaluating an injective diagram gives an injective sheaf. Precomposing with BS.7's map between two prefixes identifies the actual transition of (B.DC7).

B.1e supplies coproduct preservation and the proper-image bounds at all these finite coefficient levels. Evaluations preserve coproducts and jointly detect isomorphisms; hence \(F_f\) preserves coproducts. The BV.3 representability argument now applies to this full diagram category: free presheaf generators at \((U,n)\) are compact projective generators before sheafification, and exact sheafification with its fully faithful derived right adjoint gives the BF.6 argument. Compactness of the sheafified generators is not assumed. It yields a right adjoint \(\Psi_f\) to \(F_f\), with one diagram unit and counit.

The coefficient projection comparison of B.1e–B.1f gives a natural isomorphism
\[
F_f Le_{n,!}\simeq Le_{n,!}Rf_{!,O_n}.
\tag{B.DC8}
\]
At \(m\leq n\) this is proper support with derived coefficient extension to \(O_m\); the other components vanish. The coefficient comparisons preserve the prefix maps by tensor associativity and their counit construction. Testing the right adjoint against \(Le_{n,!}H\), for every \(H\) and every shift, therefore gives
\[
\begin{aligned}
\operatorname{Hom}(H,e_n\Psi_fG)
&\simeq\operatorname{Hom}(F_fLe_{n,!}H,G)\\
&\simeq\operatorname{Hom}(Rf_{!,O_n}H,G_n)\\
&\simeq\operatorname{Hom}(H,f_{O_n}^!G_n).
\end{aligned}
\tag{B.DC9}
\]
Yoneda identifies the component and its counit. Precomposition with the map between prefixes identifies its transition as precisely B.1g's exceptional coefficient-change map followed by the exceptional image of the transition in \(G\). It follows that \(\Psi_fG\) is cartesian whenever \(G\) is: both maps
\[
O_n\otimes_{O_{n+1}}^Lf_{O_{n+1}}^!G_{n+1}
 \xrightarrow{\sim}f_{O_n}^!(O_n\otimes_{O_{n+1}}^LG_{n+1})
 \xrightarrow{\sim}f_{O_n}^!G_n
\tag{B.DC10}
\]
are the already established comparisons. Nonflat quotients are included; no finite projective dimension over \(O_{n+1}\) is presumed.

For a cartesian constructible input, all components have a common interval. B.1g supplies bounded constructibility and a common output interval for \(\Psi_f\). It supplies the same assertion for \(F_f\) by applying ordinary proper image to the exact extension by zero in the chosen compactification. The proper-support coefficient comparison makes \(F_f\) cartesian. Thus both functors preserve the indicated full subcategories, and their diagram adjunction restricts without changing its Hom groups, units or counits.

**Identify the completed functor, not just its reductions.** The construction of BM.1–BM.4 uses the same compactification, completed open extension \(Cj_!\), proper image, and the proper–open exchange specified by open adjunction. B.1e supplies the needed Noetherian compactification and ordinary proper comparisons at this base; B.1g supplies the constructibility just used. BK.2 and BS.2 compare proper image on the two diagram sites, and BM.2 compares open extension. Applying their actual diagram maps, then the derived limit, gives
\[
E_Y F_f\simeq Rf_!^c E_X,
\qquad Rf_!^cK=Rp_*C_{\overline X}j_!K
 \simeq C_YRp_*j_!K.
\tag{B.DC11}
\]
The common-refinement and proper–open pasting proofs of BM.3–BM.4 use those adjunction maps before evaluation. They give independence of compactification and associative composition here. Componentwise conservativity proves that these maps are invertible; it is not used to infer equality of two maps merely because all their reductions agree.

Define \(f_c^!=E_X\Psi_fE_Y^{-1}\). Transporting the restricted adjunction through (B.DC5) and (B.DC11) proves (B.DC1). Its triangle identities hold in the diagram category before transport. Composition of the right adjoints is the unique comparison preserving the already specified composite counit. B.1f's smooth trace and B.1g's closed-support counit give diagram maps; their transported maps prove (B.DC2). The twist is the compatible rank-one coefficient system, not a choice of separate twists at each level.

Finally BR.5 and BS.4 retain, for each integer \(r\), the exact sequence
\[
\begin{aligned}
0&\longrightarrow\varprojlim{}^1_n
 \operatorname{Hom}_{D(Z_{\mathrm{et}},O_n)}(K_n,L_n[r-1])\\
&\longrightarrow\operatorname{Hom}_{\mathscr C_Z}(K,L[r])\\
&\longrightarrow\varprojlim_n
 \operatorname{Hom}_{D(Z_{\mathrm{et}},O_n)}(K_n,L_n[r])
 \longrightarrow0.
\end{aligned}
\tag{B.DC12}
\]
Here \(K_n,L_n\) denote the classical reductions specified by (B.DC5). The adjunction was proved in the middle groups for every shift; it was not inferred by taking the ordinary inverse limit of finite-level Hom groups. No global finiteness assertion removes the degree-one-limit term. As a coefficient check, a strict constant residue-field system is not its derived-cartesian diagram: the reductions of its complete sheaf have both degree \(-1\) and degree zero terms, with zero and identity transitions, respectively, as in BK.7 and BR.4. Keeping this torsion correction is essential. \(\square\)

This gives the whole-diagram and derived-completion operations used after B.1g. It does not identify \(\underline O\) with \(\widehat O\), invert \(\pi\), establish the BW–BX rational comparison over the trait, or prove BT.5's higher-effacement condition for realization from the strict-system heart. In particular B.1d's ambient rational-operation premise remains explicit. The cited site and geometric theorems are inputs at their stated hypotheses.

### Actual rational coefficients over the trait

**Proposition B.1i (rational comparison with all higher morphisms).** Keep the arbitrary henselian trait, separated finite-type schemes and complete coefficient DVR \(O\) of B.1h. Its residue field is finite of characteristic \(\ell\), with \(\ell\) invertible on the trait. Put \(E=O[1/\pi]\), and distinguish the pro-étale coefficient sheaves
\[
A_Z=\underline O,\qquad R_Z=\varprojlim_n\underline{O/\pi^n},\qquad E_Z=R_Z[1/\pi].
\tag{B.RQ1}
\]
Let \(\widehat{\mathscr C}_Z\) be the full category of derived-complete \(R_Z\)-complexes with bounded constructible classical first reduction. Let \(D_{\mathrm{cons}}(Z_{\mathrm{pro\acute et}},E_Z)\) mean the **full subcategory of the ambient derived category** with bounded constructible cohomology, pro-étale locally finite free on the members of a finite algebraic stratification. There is a canonical t-exact equivalence
\[
\mathscr C_Z[1/\pi]\simeq\widehat{\mathscr C}_Z[1/\pi]
\xrightarrow{\Phi_Z}
D_{\mathrm{cons}}(Z_{\mathrm{pro\acute et}},E_Z).
\tag{B.RQ2}
\]
The functor sends \(P\) to the sheaf localization \(P[1/\pi]\). It identifies tensor, internal Hom, inverse image and derived direct image with the ordinary ringed-site functors. Proper support is ordinary \(Rp_*j_!\) for a compactification; its constructible right adjoint is the rationalization of B.1h's complete exceptional functor. These comparisons include the adjunction maps. No excellence, normality or global lisse integral lattice is assumed. This is not a realization theorem for the bounded derived category of the constructible heart.

**The Noetherian and scalar inputs.** These schemes are Noetherian and finite dimensional. BO.1–BO.6 use finite Tor induction, compatible matrices and an actual internal-Hom limit map to produce local finite-free models. BP.1–BP.2 use the ascending chain condition for subsheaves of a finite constructible sheaf to give one finite stratification and a uniform torsion exponent. BQ.1–BQ.4 recover cohomology from the stabilized **images** in its reduction tower and prove truncation closure. These site and coefficient arguments use no field image-finiteness theorem. Finite-level cohomology itself need not form a strict system.

Use BW.1–BW.3 for the actual scalar adjunction
\[
T_ZK=C_{R_Z}(R_Z\otimes_{A_Z}^{L}K),\qquad
T_Z:D_{A_Z}^{c}\rightleftarrows D_{R_Z}^{c}:U_Z.
\tag{B.RQ3}
\]
Restriction \(U_Z\) is exact and conservative. Torsion-freeness over the DVR makes \(R_Z\) flat over \(A_Z\). The two-term quotient resolutions identify reduction before and after scalar extension. Thus the unit is an isomorphism by complete reduction detection; the triangle identity and \(U_Z\)'s conservativity prove the same for the counit. This gives all higher morphisms and restricts to the constructible categories with the bounded t-structures above. It does not identify \(A_Z\) with \(R_Z\).

BW.6–BW.8 construct central localization by
\[
\operatorname{Hom}_{\widehat{\mathscr C}_Z[1/\pi]}(P,Q[m])
=\operatorname{Hom}_{\widehat{\mathscr C}_Z}(P,Q[m])[1/\pi].
\tag{B.RQ4}
\]
Clearing finitely many denominators, then killing a commutativity defect by one further power, supplies the triangle axioms. Truncation triangles supply the bounded t-structure. BP's uniform torsion bound and finite truncation identify the kernel of rationalization. No Hom group is replaced by a mere limit of finite-level Hom groups: B.1h's degree-one inverse-limit term remains in the integral comparison.

**Ordinary support and bounded-below continuity.** BX.1–BX.3 work with a ring and an arbitrary ideal, then a quasi-compact open complement. Their lifted ind-étale neighbourhoods prove the ordinary closed/open localization sequence. The exact \(i^{-1},i_*,j^{-1},j_!\) have the stated coefficient comparisons and preserve completeness. Detection is on a weakly contractible basis, not an assumption that ordinary geometric stalks detect every pro-étale sheaf. Finite stratification and BO's models consequently make ordinary tensor and the ringed inverse image
\[
Lf_R^*P=R_X\otimes_{f^{-1}R_Y}^{L}f^{-1}P
\tag{B.RQ5}
\]
already complete and constructible. The coefficient map in this formula cannot be discarded for a general morphism.

The needed continuity is exactly BX.4: on a quasi-compact quasi-separated object, derived sections commute with filtered colimits having a **common lower bound**. The weakly contractible hypercover calculation has only finitely many resolution degrees in each total degree. It gives continuity for \(Rf_*\); the closed-support triangle gives it for \(i^!\). Finite-perfect models on strata and finite closed/open devissage give it for internal and global derived Hom from fixed \(P\in\widehat{\mathscr C}_Z\). For constructible targets, the closed-support terms are constructible by B.1h; this does not import BV's field-only biduality.

The multiplication-by-\(\pi\) tower of bounded \(Q\) has that same lower bound and colimit \(Q[1/\pi]\). Scalar adjunction and BX.5 therefore identify the actual map
\[
\operatorname{Hom}_{D(R_Z)}(P,Q[m])[1/\pi]
\xrightarrow{\sim}
\operatorname{Hom}_{D(E_Z)}(P[1/\pi],Q[1/\pi][m])
\quad(m\in\mathbb Z).
\tag{B.RQ6}
\]
The internal-Hom comparison uses the same localized evaluation map. This proves full faithfulness in every degree; no unrestricted unbounded-below continuity has been used.

**Integral models, not an assumed global lisse lattice.** The descent input is AG-LTF, Lemma 7.1 and Proposition 7.2. Lemma 7.1 descends classicality through a two-arrow sheaf equalizer, using the affine ind-étale presentation criterion and commutation of filtered colimits with finite limits. It is independent of coefficients. To extend the following lattice argument from the finite extensions of \(\mathbb Q_\ell\) named in Proposition 7.2 to the present \(O\), use that \(O=\varprojlim O/\pi^n\) is compact and \(\mathrm{GL}_r(O)\) is open in the valuation topology of \(\mathrm{GL}_r(E)\). On a trivializing affine pro-étale object the lattice sheaf is the constant discrete sheaf
\[
\mathrm{GL}_r(E)/\mathrm{GL}_r(O).
\tag{B.RQ7}
\]
Continuous matrices yield locally constant cosets on the profinite component space; cosets may differ on clopen pieces. Lemma 7.1 makes this sheaf classical. Its local inhabitation descends to the étale site through the exact fully faithful inverse image. Thus an étale covering has lattices. The same reasoning covers the equal-characteristic complete DVR, without assuming a global profinite monodromy representation.

BX.6 now constructs integral models. At a generic point, a finite-presentation étale lattice neighbourhood has finite separable fibre. Clearing the finitely many equations making its algebra generators integral and shrinking makes the neighbourhood finite étale over a dense open. Repeat on the lower-dimensional closed remainder to obtain a finite stratification with finite étale lattice covers. Nilpotent thickenings do not change this site. On a stratum replace the finite étale cover by the finite torsor of orderings, with group \(G\). The sum \(\sum_{g\in G}gN\) of its pulled-back lattices is invariant and is again a lattice. Trivialize the rational sheaf and refine into clopen pieces on which the finitely many relative lattice cosets are fixed. On each piece the sum comes from a finite torsion-free \(O\)-module of full rank, hence a free one. This does not assert that every torsion-free module over the sheaf ring \(R_Z\) is free. Finite descent gives a lattice on the stratum; BP and BX.2 give its complete integral object and complete extension by zero.

For gluing, (B.RQ6) expresses each rational degree-one extension as \(u/\pi^a\). Lift the integral class \(u\) in the heart and rescale one chosen rational endpoint identification. This realizes the required extension. Induction produces an integral constructible model for every constructible rational sheaf. Full faithfulness, cones of fractions and the finite cohomological truncation tower then produce integral complexes for the full target of (B.RQ2), proving essential surjectivity and t-exactness. The model is constructible. AG-LTF's nodal counterexample still forbids asserting a global lisse lattice.

**Operations with their maps.** BW.4–BW.5 transport completed tensor, evaluation and geometric adjunctions through (B.RQ3). Use B.1e–B.1h for their geometric scope, not BV's opening field hypotheses. Tensor and inverse image were identified above. The common-lower-bound argument identifies the localization map for \(Rf_*\), and ordinary \(j_!\) commutes with localization. Therefore BX.7 gives
\[
\Phi_Y\,\overline{Rf_!^c}\simeq Rp_*j_!\Phi_X,\qquad
\operatorname{Hom}(Rf_!K,L[m])\simeq\operatorname{Hom}(K,f^!L[m]).
\tag{B.RQ8}
\]
The bar denotes transport through (B.RQ3) and central localization. The second bijection is on the constructible rational categories for every integer \(m\), obtained by localizing B.1h's full adjunction. Compactification refinements, composition, smooth Tate orientation and the closed-support triangle retain their units and counits. Closed exceptional image agrees with BX.2's ambient fibre formula; no unbounded nonconstructible exceptional comparison is asserted.

This supplies the scalar and rational comparison part of B.1d's operation inputs, at that proposition's finite-extension-of-\(\mathbb Q_\ell\) scope. It does not itself construct the ambient enhancements, higher coherence or multiplicative continuous descent also required there. The family biduality deduction remains the separate argument given there; BX.7's field-scope biduality sentence is not silently generalized. The enhanced inputs and strict-heart higher effacement are separate assertions; (B.RQ2) does not imply them.


### Mapping complexes and the continuous cochain product

**Lemma B.1j (what the existing models supply).** The ordinary derived categories used above have actual mapping-complex models. The continuous resolution also has an explicit associative cup product, compatible with the field-topos comparison. We give the maps and their bounds because neither fact alone proves the enhanced exceptional and geometric-descent premises of B.1d.

**Unbounded maps.** For a Grothendieck abelian category \(\mathcal A\), take the full differential-graded category of K-injective complexes, with
\[
\mathscr H^r(I,J)=\prod_a\operatorname{Hom}_{\mathcal A}(I^a,J^{a+r}),
\qquad d f=d_Jf-(-1)^r f d_I.
\tag{B.EI1}
\]
Composition is ordinary composition of homogeneous maps. Expanding the two differentials gives \(d(gf)=(dg)f+(-1)^{|g|}g(df)\); the identity is a degree-zero cycle. BF.1–BF.3 prove existence of K-injective replacements and show that precomposition by a quasi-isomorphism is a quasi-isomorphism on these Hom complexes. Their cone proof works in every shift. Consequently
\[
H^r\mathscr H(I,J)=\operatorname{Hom}_{D(\mathcal A)}(I,J[r]).
\tag{B.EI2}
\]
This constructs the mapping model without choosing an additive resolution functor. Products in (B.EI1) are products of groups of maps, not an assertion that products of sheaves are exact. A degree-minus-one map \(h\) with \(dh=f-g\) remains part of a diagram; equality of the classes of \(f,g\) does not specify that homotopy.

For an exact additive left adjoint \(v:\mathcal A\to\mathcal B\) with right adjoint \(u\), BF.4 proves that \(uJ\) is K-injective when \(J\) is. Its component adjunction is the chain isomorphism
\[
\mathscr H_{\mathcal B}(vM,J)
\simeq\mathscr H_{\mathcal A}(M,uJ).
\tag{B.EI3}
\]
Both differentials are identified by naturality, including the sign on the term involving \(d_M\). Since both targets are K-injective, these are the derived mapping complexes for the two sides, for arbitrary \(M\). The original unit, counit and their triangle identities give these particular adjunction maps. This does not assert that \(v\) preserves K-injectives. Likewise BH.2–BH.4 use simultaneous K-flat and K-injective models: currying is an isomorphism of Hom complexes, with the three differential terms of (BH.13), and the tensor associativity, symmetry and unit maps are the elementary-tensor maps of (BH.8). These are actual chain calculations, not only dimension counts.

There is a precise remaining distinction. BF.6 represents ordinary Hom functors and obtains the triangulated exceptional adjoint. To lift it one must also give the compatible maps on mapping complexes, or an equivalent coherent representing construction, and compare composition and compactification refinements there. Representability on \(H^0\), even with all shifted Hom bijections, is not that construction. The explicit attaching model in Gluing, Appendix B has classical bounded-below field-coefficient scope; it cannot silently replace this arithmetic obligation.

**Continuous complexes.** Let \(G\) be profinite and \(\Lambda\) a commutative ring, with discrete continuous left \(G\)-modules and \(\Lambda\)-linear action. For a complex \(M\) zero below \(a\), use Galois cohomology, Section 2 term by term. In group degree \(p\) and internal degree \(r\), put
\[
C^{p,r}(M)=\operatorname{Maps}_{\mathrm{cont}}(G^p,M^r),
\qquad D=\delta+(-1)^p d_M.
\tag{B.EI4}
\]
Here \(\delta\) is its inhomogeneous differential (2.6). For fixed total degree \(n\), only \(0\leq p\leq n-a\) occur. The homogeneous resolution is exact by insertion of the identity; each term is invariants-acyclic by its explicit coinduced-module identification. The same proof works for \(\Lambda\)-modules: continuous functions lift through a surjection by lifting their finitely many values, and coinduction is right adjoint to exact forgetting. Thus the finite-diagonal totalization computes derived invariants for these bounded-below complexes. One may compare with an injective double resolution; the augmented rows are exact and its two filtrations have finitely many entries in each total degree. The resulting comparisons are quasi-isomorphisms. The continuous-function functor is exact, so the same finite-diagonal argument shows that this totalization preserves quasi-isomorphisms between bounded-below complexes. No assertion is made for unrestricted unbounded-below totalizations.

For an equivariant homogeneous internal map \(f:M\to N\) of degree \(s\), its map on group degree \(p\) is \((-1)^{ps}f\). Substitution into (B.EI4) gives \(D C(f)-(-1)^s C(f)D=C(df)\). This retains internal chain homotopies, rather than merely their induced maps on cohomology.

**The product and its two gradings.** For \(x\in C^{p,r}(M)\), \(y\in C^{q,s}(N)\), define
\[
\begin{aligned}
(x\smile y)(g_1,\ldots,g_{p+q})
={}&(-1)^{rq}x(g_1,\ldots,g_p)\\
&\otimes (g_1\cdots g_p)y(g_{p+1},\ldots,g_{p+q}).
\end{aligned}
\tag{B.EI5}
\]
The empty product acts as the identity. This is continuous: each function has finite image and factors through finite quotient coordinates, and an open normal subgroup fixing the finitely many values controls the action. It defines a map from the ordinary tensor of the two total cochain complexes to the total cochain complex of the ordinary tensor of the inputs.

Deleting homogeneous coordinates before and after the shared vertex gives
\(\delta(x\smile_0 y)=\delta x\smile_0 y+(-1)^p x\smile_0\delta y\) for the unsigned, purely group-degree product. The two terms at that vertex cancel. Applying the internal tensor differential and then the sign \((-1)^{rq}\) gives
\[
D(x\smile y)=Dx\smile y+(-1)^{p+r}x\smile Dy.
\tag{B.EI6}
\]
In detail the internal differential on the first factor has sign \((-1)^{p+q+rq}\), which equals \((-1)^p(-1)^{(r+1)q}\); on the second it has sign \((-1)^{p+q+rq+r}\), which equals \((-1)^{p+r}(-1)^q(-1)^{rq}\). These are the two required terms. The group-differential signs agree because changing \(q\) adds \((-1)^r\), while the total Leibniz sign contributes \((-1)^{p+r}\). Associativity follows from the common prefix action and
\(rq+(r+s)t=st+r(q+t)\) for a third cochain of group degree \(t\). The constant degree-zero unit is a unit. This product is not claimed to be strictly graded commutative; no higher commutativity structure has been constructed by this calculation.

**Which derived product this is.** In homogeneous coordinates the same formula takes the front and back blocks sharing one vertex. It is equivariant, preserves the constant-function augmentations, and obeys (B.EI6). The map from invariant cochains to the underlying homogeneous resolution, followed by the inverse of its augmentation, represents the derived counit from trivial-action \(R\Gamma(G,M)\) to \(M\). The front/back product is compatible with this inclusion. Its augmentation compatibility therefore makes its transpose precisely the derived cup product
\[
R\Gamma(G,M)\otimes^L_\Lambda R\Gamma(G,N)
\longrightarrow R\Gamma(G,M\otimes^L_\Lambda N).
\tag{B.EI7}
\]
For this last comparison use bounded-below input models whose ordinary tensor computes the derived tensor, for example bounded complexes of flat \(\Lambda\)-modules, and resolve the tensor on the source as necessary. The elementary formula alone does not authorize replacing a nonflat ordinary tensor by a derived one. It gives the counit-defined product in this stated model scope. Group restriction and coefficient maps commute with (B.EI5), before taking cohomology; arbitrary nonflat coefficient extension retains its derived comparison obligation.

Galois cohomology, Theorem 1.1 identifies the small étale topos of a field with discrete continuous Galois sets, hence its \(\Lambda\)-module categories. This equivalence is symmetric monoidal: the geometric stalk commutes with tensor because every tensor and balancing relation uses finitely many sections, representable on one pointed refinement; the tensor unit goes to \(\Lambda\). Its inverse equivalence and exactness then identify the derived tensors and the section/invariant counits. Consequently the field-cohomology comparison preserves precisely (B.EI7), in the model scope just proved.

For (B.4) and (E.9) this supplies the continuous-resolution product and its field-level identification, not yet the geometric nearby-cycle descent comparison. One must still compare the actual geometric-generic covering diagram, its pullback to the closed fibre and its products; retain its homotopies through normalized coefficient diagrams and derived limits; and reconcile the enhanced exceptional adjunction above. Complete lattices and their rationalizations are not discrete rational modules. Nor is the two-term generator model of Appendix C automatically a multiplicative model merely because it is quasi-isomorphic to these cochains. The logarithmic change in Appendix E needs its own pairing comparison. These are exact remaining interfaces, not reasons to discard the existing ordinary operations or their proofs. \(\square\)


### Resolution graphs and the proper-support mapping bimodule

**Proposition B.1k (an actual model before compactification comparisons).** The unbounded resolution inputs of BF.1–BF.4 give a dg roof for the right derived functor of an additive functor between Grothendieck abelian categories. Applied to a fixed compactification in B.1e, this gives a dg model of its ordinary proper-support functor. The ordinary right adjoint then quasi-represents the actual right mapping modules of this model. We construct the roof and the representing maps; we do not identify objectwise representation with a completed comparison of all compactification and coefficient diagrams.

Use the cochain Hom convention in (B.EI1). Write \(\mathcal I(\mathcal A)\) for the dg category of all K-injective complexes in \(\mathcal A\). Its degree-zero homotopy category is \(D(\mathcal A)\), by BF.2. Work with the universe convention of BF; if a category of modules on this dg category is formed, place that category in a larger universe. No compact-generation assumption is added to the following graph construction.

Let \(\Phi:\mathcal A\to\mathcal B\) be additive, extended term by term, including on homogeneous maps. Define \(\mathcal G_\Phi\) to have objects \(U=(I,J,q)\), where \(I\in\mathcal I(\mathcal A)\), \(J\in\mathcal I(\mathcal B)\), and \(q:\Phi I\to J\) is a degree-zero closed quasi-isomorphism. A degree-\(n\) map from \(U\) to \(U'=(I',J',q')\) is a triple
\[
\begin{aligned}
t&=(f,g,h),\\
f&\in\operatorname{Hom}^n(I,I'),\qquad
g\in\operatorname{Hom}^n(J,J'),\\
h&\in\operatorname{Hom}^{n-1}(\Phi I,J').
\end{aligned}
\tag{B.RG1}
\]
The third component retains a homotopy, rather than just the statement that the two routes around a square agree in the derived category. Set
\[
D(f,g,h)=(df,dg,q'\Phi(f)-gq-dh).
\tag{B.RG2}
\]
For \(s=(f_s,g_s,h_s):U'\to U''\) of degree \(m\), define
\[
s\circ t=
\bigl(f_sf_t,\ g_sg_t,\
h_s\Phi(f_t)+(-1)^m g_sh_t\bigr).
\tag{B.RG3}
\]
These formulas make a dg category. To check \(D^2=0\), its third component is
\(q'\Phi(df)-(dg)q-d(q'\Phi(f)-gq-dh)=0\), since both \(q,q'\) are closed. For the signed Leibniz rule, the third component of \(D(s\circ t)\) is
\[
\begin{aligned}
&q''\Phi(f_s)\Phi(f_t)-g_sg_tq
 -(dh_s)\Phi(f_t)\\
&\quad+(-1)^m h_s\Phi(df_t)
 +(-1)^{m+1}(dg_s)h_t-g_sdh_t.
\end{aligned}
\tag{B.RG4}
\]
In \((Ds)\circ t+(-1)^m s\circ(Dt)\), the extra terms are
\(-g_sq'\Phi(f_t)+g_sq'\Phi(f_t)\); they cancel and leave exactly (B.RG4). The first two components satisfy the ordinary Hom-complex Leibniz identity. For three maps of degrees \(\ell,m,n\), either association has third component
\(h_r\Phi(f_s)\Phi(f_t)+(-1)^\ell g_rh_s\Phi(f_t)+(-1)^{\ell+m}g_rg_sh_t\).
Thus composition is associative. The units are \((1_I,1_J,0)\), closed of degree zero.

**Why this roof computes the derived functor.** Projection \(\pi:U\mapsto I\) is a dg functor, surjective in every degree on each Hom complex. Its kernel, in the order \((g,h)\), has differential
\[
(g,h)\longmapsto(dg,-gq-dh).
\tag{B.RG5}
\]
This is \(\operatorname{Cone}(q^*)[-1]\), with the two factors reordered, where
\(q^*:\operatorname{Hom}^\bullet(J,J')\to\operatorname{Hom}^\bullet(\Phi I,J')\).
Here the convention is
\(\operatorname{Cone}(a)^n=B^n\oplus A^{n+1}\) with differential \((b,a_0)\mapsto(db+a(a_0),-da_0)\).
The target \(J'\) is K-injective, and \(q\) is a quasi-isomorphism, so the Hom-cone argument of BF.1 makes \(q^*\) a quasi-isomorphism. The kernel (B.RG5) is therefore acyclic, and \(\pi\) is a quasi-isomorphism on every Hom complex. For every \(I\), BF.1 supplies at least one replacement \(q:\Phi I\to J\). Thus \(\pi\) is also essentially surjective on the degree-zero homotopy categories: it is a dg quasi-equivalence. Projection \(\rho:U\mapsto J\), on maps \(t\mapsto g\), is another dg functor, giving the roof
\[
\mathcal I(\mathcal A)
\xleftarrow{\ \pi\ }\mathcal G_\Phi
\xrightarrow{\ \rho\ }\mathcal I(\mathcal B).
\tag{B.RG6}
\]
In the ordinary derived category, the maps \(q\) identify \(H^0\rho\) with termwise \(\Phi\) on K-injective objects: for a closed triple, \(dh=q'\Phi(f)-gq\) is the needed naturality homotopy. Consequently (B.RG6) realizes precisely \(R\Phi\) of BF.4. No additive choice of \(I\mapsto J\) has been used. All possible replacements are objects of the graph.

The exactness comparison can also be made at the level of these objects. For a closed degree-zero \(t=(f,g,h)\), take
\[
\begin{aligned}
\operatorname{Cone}(t)&=
\left(\operatorname{Cone}(f),\operatorname{Cone}(g),q_t\right),\\
q_t&=\begin{pmatrix}q'&h\\0&q\end{pmatrix}.
\end{aligned}
\tag{B.RG7}
\]
The upper-right chain identity for this matrix is
\(d_{J'}h+h\Phi(d_I)=q'\Phi(f)-gq\), exactly the closedness equation. Its diagonal maps are quasi-isomorphisms; the degreewise split cone sequences and their long exact cohomology sequences make \(q_t\) a quasi-isomorphism. Both cones are K-injective by BF.1. Cone inclusion and projection, in both first components and with zero homotopy component, are closed graph maps. Under \(\pi\) they give the usual cone triangle, and under \(\rho\) they give the corresponding target cone triangle. Hence the transferred triangulated structure is respected. For shifts, set \(U[1]=(I[1],J[1],q[1])\); the dg shift on a degree-\(n\) map is
\[
t[1]=\bigl((-1)^nf[1],\ (-1)^ng[1],\
(-1)^{n-1}h[1]\bigr).
\tag{B.RG8}
\]
Since shifting both source and target negates the Hom differential before these degree factors are inserted, (B.RG2) gives \(D(t[1])=(Dt)[1]\). Substitution in (B.RG3) also respects composition and the unit. This specifies the signs behind the shift comparison, not only its existence on \(H^0\).

**Fixed-compactification proper support.** Retain the full scope of B.1e: \(f:X\to Y\) is separated of finite type between Noetherian schemes, and \(\Lambda\) is a commutative ring killed by a positive integer. Choose \(f=pj\) as there. Open extension \(j_!\) on ordinary étale \(\Lambda\)-modules is exact. Apply the graph to \(\Phi=j_!\). Exact inverse image \(p^*\), left adjoint to \(p_*\), makes \(p_*J\) K-injective by BF.4. There is therefore the explicit dg roof
\[
\begin{aligned}
\mathcal I(X_{\mathrm{et}},\Lambda)
&\xleftarrow{\ \pi\ }\mathcal G_{j_!}
\xrightarrow{\ F_{p,j}\ }\mathcal I(Y_{\mathrm{et}},\Lambda),\\
F_{p,j}(I,J,q)&=p_*J,\qquad
F_{p,j}(f,g,h)=p_*g.
\end{aligned}
\tag{B.RG9}
\]
Its degree-zero functor is \(Rp_*j_!=Rf_!\): exactness of \(j_!\) permits the K-injective representative on \(X\), and \(J\) is a K-injective replacement of its extension. Additivity of \(p_*\) preserves the displayed cones, shifts and composition. There is no bounded-below assumption, no finite global dimension assumption on \(\Lambda\), and no requirement that its torsion order be invertible on \(Y\) at this ordinary stage. This construction does not yet compare two different compactifications.

**The actual representing-module maps.** Put \(\mathcal C=\mathcal G_{j_!}\), \(\mathcal D=\mathcal I(Y_{\mathrm{et}},\Lambda)\), and \(F=F_{p,j}\). For \(L\in\mathcal D\), consider the right dg \(\mathcal C\)-module
\[
\begin{aligned}
M_L(U)&=\operatorname{Hom}_{\mathcal D}^\bullet(FU,L),\\
u\cdot a&=uF(a),\qquad v\cdot u=vu.
\end{aligned}
\tag{B.RG10}
\]
The second formula is the right action for a homogeneous map \(a\) in \(\mathcal C\); the third is covariant postcomposition by a homogeneous map \(v\) in \(\mathcal D\). The Hom Leibniz identity proves both compatibility with differentials and compatibility of the two actions. Thus this is an actual mapping bimodule, before any choice of representing objects.

The ordinary adjoint \(R\) to \(H^0F\) exists and is exact by B.1e and BF.6. Choose \(Q_L\in\mathcal C\) representing \(RL\) under \(H^0\pi\), and choose a closed degree-zero map \(e_L:FQ_L\to L\) representing its counit. This is possible because the target Hom complexes compute ordinary derived morphisms. There is a strict right-module map
\[
\begin{aligned}
\eta_L:\operatorname{Hom}_{\mathcal C}^\bullet(-,Q_L)&\longrightarrow M_L,\\
a&\longmapsto e_LF(a).
\end{aligned}
\tag{B.RG11}
\]
Indeed \(de_L=0\) gives \(d(e_LF(a))=e_LF(da)\), and associativity gives
\(e_LF(ab)=e_LF(a)F(b)\). In degree \(r\), the cohomology of the source at \(U\) is \(\operatorname{Hom}_{D(X,\Lambda)}(\pi U,RL[r])\), by the quasi-equivalence and the shift computation. The target cohomology is \(\operatorname{Hom}_{D(Y,\Lambda)}(F U,L[r])\). The induced map is the ordinary adjunction bijection, using the shift-compatible counit. Hence (B.RG11) is an objectwise quasi-isomorphism, for every integer \(r\) and every unbounded object \(U\). This proves right quasi-representability of the particular bimodule (B.RG10), with its maps and homotopies; it is not an argument from abstract dimensions or an unspecified family of shifted bijections.

The remaining comparison is precise. The module \(M_L\) depends dg-functorially on \(L\), but the chosen \(Q_L,e_L\) above have not been supplied with coherent transition maps. To use them as an enhanced exceptional adjunction in the whole diagrams of B.1d, one must carry the representing-module construction through enriched Yoneda, identify its unit and counit compositions, and compare compactification refinements there. Ordinary uniqueness of representing objects is not a proof of those higher comparisons. Geometric nearby descent, the two-term/logarithmic product comparison and normalized adic or rational transport likewise remain separate obligations. The unbounded roof and quasi-representing maps above concern the specified fixed presentation. \(\square\)



### The dg-module adjunction for fixed proper support

**Proposition B.1l (representing modules, with unit and counit).** For the fixed compactification and dg functor \(F=F_{p,j}:\mathcal C\to\mathcal D\) in B.1k, its ordinary adjunction has the following dg-module presentation. There are dg categories of homotopy-representable modules, quasi-equivalent to \(\mathcal C,\mathcal D\); induction gives the left functor on these categories, and a resolution graph gives the right functor as a dg roof. Their mapping complexes have the explicit quasi-isomorphisms below. Their unit and counit come from a strict adjunction on all dg modules, and their triangle homotopies can be exhibited on resolved objects. This is the fixed-model representing-module construction for B.1k. It does not supply compactification-refinement, geometric base-change or coefficient-diagram comparisons.

We give the construction for a unital dg functor between dg categories over a commutative ring \(k\), using the universe convention of B.1k. For its application take \(k=\Lambda\), with the full ordinary unbounded scope of B.1e. Neither the complexes nor the dg Hom modules are required to be bounded or flat over \(k\).

**Representables and resolutions.** A right dg \(\mathcal C\)-module \(P\) assigns a complex \(P(X)\) to each object and associative unital actions
\(P(X)\otimes_k\mathcal C(Y,X)\to P(Y)\), written \(pa\), satisfying
\(d(pa)=(dp)a+(-1)^{|p|}p\,da\).
A homogeneous module map \(t\) has \(t(pa)=t(p)a\); its differential is \(dt=d_Qt-(-1)^{|t|}td_P\). These formulas define the dg category of modules. For \(h_X=\mathcal C(-,X)\), evaluation at the identity gives an isomorphism of complexes
\[
\begin{aligned}
\operatorname{Hom}_{\mathrm{dgMod}(\mathcal C)}^\bullet(h_X,P)
&\xrightarrow{\ \sim\ }P(X),\\
t&\longmapsto t_X(1_X),\qquad
p\longmapsto\bigl(a\longmapsto pa\bigr).
\end{aligned}
\tag{B.DA1}
\]
The inverse respects degrees and module actions; evaluating its differential on \(a\) cancels the two terms involving \(da\). Thus (B.DA1) is an enriched Yoneda isomorphism, not just a degree-zero bijection.

Call a module acyclic when every \(P(X)\) is acyclic, and call \(P\) h-projective when its Hom complex to every acyclic module is acyclic. Representables are h-projective by (B.DA1). Every module \(M\) has an h-projective replacement \(P\to M\), as follows. At stage zero take a free module generator at \(X\) in degree \(r\) for each cycle in \(M(X)^r\), mapping that generator to the cycle. A generator at \(X\) means a shifted representable; its action determines its values at every other object. At each later stage include a new generator for every pair
\[
\begin{aligned}
z&\in P_i(X)^r,\quad dz=0,\\
m&\in M(X)^{r-1},\quad q_i(z)=dm,\\
|e_{z,m}|&=r-1,\qquad de_{z,m}=z,\qquad
q_{i+1}(e_{z,m})=m.
\end{aligned}
\tag{B.DA2}
\]
Extend by the module Leibniz law. The equations \(dz=0\) and \(q_i(z)=dm\) verify the new differential and chain map. The old module is a graded direct summand; the quotient is a direct sum of shifted representables. Take the increasing union \(P=\bigcup_iP_i\). Initial generators make cohomology surjective at every object. A kernel class has a representative at some finite stage, and (B.DA2) makes it a boundary at the next stage. Consequently \(P\to M\) is an objectwise quasi-isomorphism. This construction involves all degrees at once, not a bounded-below truncation.

Here is also a direct h-projectivity proof, including the infinite union. For a closed degree-zero map \(t:P\to N\) with \(N\) acyclic, build a degree-minus-one module map \(H\) stage by stage so that \(t=dH+Hd\). Once \(H\) is defined on earlier generators, the required value on a new generator \(e\) at \(X\) must satisfy
\(dH(e)=t(e)-H(de)\).
The right side is a cycle in \(N(X)\): apply \(d\) and use the already established identity on \(de\). Acyclicity supplies \(H(e)\). Extend it freely and keep all old values. The resulting map on the union is well-defined since each element is a finite sum of generator actions. Applying the same argument to every shift of \(N\) proves h-projectivity. In particular, Hom from an h-projective module preserves quasi-isomorphisms, by taking the cone of the target map.

Let \(\mathcal Q(\mathcal C)\) be the full dg category of h-projective modules homotopy equivalent to representables. Yoneda \(X\mapsto h_X\) is a dg quasi-equivalence onto it: (B.DA1) identifies the Hom complexes, and the stipulated homotopy equivalences give essential surjectivity. We will check that the resolved modules actually needed for the right adjoint belong to this category; membership will not be inferred merely from a name.

**The strict module adjunction.** Restriction \(U=F^*\) is given by \(UN(X)=N(FX)\). Define induction \(T=F_!\) by the balanced tensor
\[
\begin{aligned}
(TP)(Y)
&=\left(\bigoplus_{X\in\mathcal C}
 P(X)\otimes_k\mathcal D(Y,FX)\right)\big/\mathcal R,\\
(pa)\otimes v&\equiv p\otimes F(a)v.
\end{aligned}
\tag{B.DA3}
\]
In the relation, \(a:X'\to X\), \(p\in P(X)\), and \(v:Y\to FX'\); all may be homogeneous. The differential on the direct sum is
\(d(p\otimes v)=dp\otimes v+(-1)^{|p|}p\otimes dv\).
The module Leibniz rule shows that it preserves the balancing relations. Right composition in \(\mathcal D\) gives the right-module action on \(TP\).

There is an isomorphism of Hom complexes
\[
\operatorname{Hom}^\bullet_{\mathrm{dgMod}(\mathcal D)}(TP,N)
\ \simeq\
\operatorname{Hom}^\bullet_{\mathrm{dgMod}(\mathcal C)}(P,UN).
\tag{B.DA4}
\]
From left to right, send \(\psi\) to \(p\mapsto\psi([p\otimes1_{FX}])\); its inverse sends \(s\) to \([p\otimes v]\mapsto s(p)v\). Balancing is exactly the module-linearity condition. For a degree-\(n\) map \(s\), applying the Hom differential to its inverse gives the terms
\(d_N(s(p))v-(-1)^n s(dp)v\): the terms containing \(dv\), both with exponent \(n+|p|\), cancel. This is the inverse applied to \(ds\), proving the chain-level assertion.

The unit and counit are the closed degree-zero module maps
\[
\begin{aligned}
\eta_P:p&\longmapsto[p\otimes1_{FX}],\\
\epsilon_N:[n\otimes v]&\longmapsto nv.
\end{aligned}
\tag{B.DA5}
\]
They are natural also with respect to homogeneous maps. For the first triangle, \(T\eta_P\) followed by \(\epsilon_{TP}\) sends \([p\otimes v]\) to itself. For the second, \(U\epsilon_N\) following \(\eta_{UN}\) sends \(n\) to \(n1=n\). Thus these are identities of dg-module maps before taking cohomology.

Restriction preserves acyclic modules and quasi-isomorphisms object by object. By (B.DA4), induction carries h-projective modules to h-projective modules. A quasi-isomorphism between h-projectives is a homotopy equivalence: its cone is h-projective and acyclic, and the identity of that cone is a boundary in its endomorphism complex. Induction therefore preserves such quasi-isomorphisms. This justifies deriving induction with the replacements above; it does not assert that ordinary tensoring preserves every quasi-isomorphism.

The induced module of a representable is again representable, by the actual co-Yoneda maps
\[
\begin{aligned}
Th_X&\xrightarrow{\ \sim\ }h_{FX},&
[a\otimes v]&\longmapsto F(a)v,\\
h_{FX}&\longrightarrow Th_X,&
w&\longmapsto[1_X\otimes w].
\end{aligned}
\tag{B.DA6}
\]
The balancing relation makes these mutually inverse; the differential and right actions agree. Induction hence restricts to a dg functor
\(T:\mathcal Q(\mathcal C)\to\mathcal Q(\mathcal D)\) representing the original \(F\).

**The right-adjoint roof and its mapping complexes.** B.1k supplies, for each \(L\in\mathcal D\), a quasi-isomorphism from a representable to
\(Uh_L=\mathcal D(F(-),L)\).
The same assertion, up to homotopy equivalence, holds for \(UQ\) whenever \(Q\in\mathcal Q(\mathcal D)\). Given an h-projective replacement \(q:P\to UQ\), choose such a quasi-isomorphism \(b:h_X\to UQ\). Since Hom from \(h_X\) preserves \(q\), there is a closed map \(a:h_X\to P\) with \(qa\) homotopic to \(b\). Thus \(a\) is a quasi-isomorphism; both its endpoints are h-projective, so it is a homotopy equivalence. This proves \(P\in\mathcal Q(\mathcal C)\).

Define a dg graph \(\mathcal R_F\) whose objects are \((Q,P,q)\) with \(Q\in\mathcal Q(\mathcal D)\), \(P\) h-projective and \(q:P\to UQ\) a quasi-isomorphism. A degree-\(n\) map is \((v,u,h)\), with \(v:Q\to Q'\), \(u:P\to P'\) of degree \(n\) and \(h:P\to UQ'\) of degree \(n-1\). Its differential and composition, for \(|s|=m\), are
\[
\begin{aligned}
D(v,u,h)&=(dv,du,q'u-U(v)q-dh),\\
s\circ t&=\bigl(v_sv_t,u_su_t,\,
h_su_t+(-1)^mU(v_s)h_t\bigr).
\end{aligned}
\tag{B.DA7}
\]
Expansion gives \(D^2=0\) and the signed Leibniz identity as in B.1k; associativity follows by expanding the three terms in the third component, and the identity has zero homotopy component. The projection \(\sigma:(Q,P,q)\mapsto Q\) is surjective on each graded Hom group. Its kernel has differential
\((u,h)\mapsto(du,q'u-dh)\).
After replacing \(h\) by \(-h\), this is the shifted cone of postcomposition
\(\operatorname{Hom}(P,P')\to\operatorname{Hom}(P,UQ')\).
It is acyclic because \(P\) is h-projective and \(q'\) is a quasi-isomorphism. Replacements exist for every \(UQ\), so \(\sigma\) is a dg quasi-equivalence. The other projection \(\tau:(Q,P,q)\mapsto P\) lands in \(\mathcal Q(\mathcal C)\), by the preceding paragraph. Thus the right functor is presented without a functorial choice of resolutions by
\[
\mathcal Q(\mathcal D)
\xleftarrow{\ \sigma\ }\mathcal R_F
\xrightarrow{\ \tau\ }\mathcal Q(\mathcal C).
\tag{B.DA8}
\]

For \(A\in\mathcal Q(\mathcal C)\) and \((Q,P,q)\in\mathcal R_F\), its adjunction comparison is the explicit chain of maps
\[
\begin{aligned}
\operatorname{Hom}^\bullet(A,P)
&\xrightarrow{\ q\circ-\ }
\operatorname{Hom}^\bullet(A,UQ)\\
&\xrightarrow{\ (B.DA4)^{-1}\ }
\operatorname{Hom}^\bullet(TA,Q).
\end{aligned}
\tag{B.DA9}
\]
The first arrow is a quasi-isomorphism by h-projectivity; the second is an isomorphism. For a graph map, the defect of the corresponding square is the differential of the map obtained by applying (B.DA4) to \(h\). Composing two such homotopies is exactly the third component of (B.DA7). Hence the graph retains the comparison homotopies and their composition, rather than choosing arbitrary isomorphisms in the homotopy category.

**Resolved units, counits and the two triangles.** For an object \((Q,P,q)\), its counit is the actual closed map
\[
\begin{aligned}
e_Q&=\epsilon_Q\,T(q):TP\longrightarrow Q.\\
q_{TA}u_A-\eta_A&=dk_A,\qquad
u_A:A\longrightarrow P_{TA},\quad |k_A|=-1.
\end{aligned}
\tag{B.DA10}
\]
Here \((TA,P_{TA},q_{TA})\) is any graph object over \(TA\). The closed map \(u_A\) and the displayed homotopy \(k_A\) exist because
\(\operatorname{Hom}(A,q_{TA})\) is a quasi-isomorphism. This is a concrete lift of the strict unit, not an additive choice of a replacement functor. The first triangle has the specified homotopy
\[
e_{TA}\,T(u_A)-1_{TA}
=d\bigl(\epsilon_{TA}\,T(k_A)\bigr),
\tag{B.DA11}
\]
by (B.DA10) and the first strict identity in (B.DA5).

For the other triangle, fix \((Q,P,q)\), take a graph object over \(TP\), and lift the closed counit \(e_Q:TP\to Q\) to a closed graph map
\((e_Q,r_e,h_e)\). Such a lift exists by the Hom quasi-isomorphism of \(\sigma\); equivalently, lift \(U(e_Q)q_{TP}\) through \(\operatorname{Hom}(P_{TP},q)\). Its homotopy equation and the unit lift give
\[
q(r_eu_P-1_P)
=d\bigl(h_eu_P+U(e_Q)k_P\bigr).
\tag{B.DA12}
\]
Indeed substitute \(q r_e=U(e_Q)q_{TP}+dh_e\) and
\(q_{TP}u_P=\eta_P+dk_P\).
The remaining term is zero because
\(U(e_Q)\eta_P=q\), by naturality of the strict unit and the second strict identity in (B.DA5).
Finally \(\operatorname{Hom}(P,q)\) is a quasi-isomorphism, so (B.DA12) forces the closed map \(r_eu_P-1_P\) to be a boundary. Choosing its degree-minus-one preimage gives the second triangle homotopy. Its existence is justified at the Hom-complex level, not merely asserted from uniqueness of an ordinary adjoint.

All the displayed maps originate in the strict module adjunction, and (B.DA7) keeps their resolution-comparison homotopies in an actual dg category. Different lift choices are handled there, instead of being declared equal as chain maps. Via Yoneda and (B.DA6), this is the promised dg-module presentation for the fixed \(F_{p,j}\). No claim is made that independently chosen lifts for different compactifications, base changes or coefficient extensions already form the required higher comparison diagrams. Those maps, geometric nearby descent and normalized adic/rational transport remain additional geometric hypotheses of B.1d. The ordinary adjoint and its full unbounded scope are retained throughout. \(\square\)



### Compactification refinements on the dg models

**Proposition B.1m (refinement and adjunction comparisons).** Retain the full Noetherian, unbounded ordinary torsion scope of B.1e. For each proper refinement between compactifications of the same map, the B.1k models admit an actual dg quasi-equivalence over the source model, together with a closed natural isomorphism of their proper-image dg functors. These maps respect successive refinements through specified composition identifications. Their induced module adjunctions have explicit compatible units and counits; on the resolved objects of B.1l the comparison is a homotopy equivalence, with the homotopies described below. This constructs the refinement diagram. It does not yet enhance the general geometric composition and base-change grids, nearby-cycle descent or coefficient diagrams.

Write the two compactifications as \(f=p_1j_1=p_2j_2\), and let \(h:\overline X_1\to\overline X_2\) satisfy \(hj_1=j_2\) and \(p_2h=p_1\). Such an \(h\) is proper by the closed-graph argument in Compact supports, Section 3. Its Lemma 3.1 supplies common refinements. Existence here uses the Noetherian-relative native compactification already bound in B.1e; no broader compactification assertion is imported from a citation alone. Put \(\mathcal C_i=\mathcal G_{j_{i,!}}\), \(\mathcal D=\mathcal I(Y_{\mathrm{et}},\Lambda)\), and \(F_i=F_{p_i,j_i}\).

**The actual map before resolutions.** Let \(V=h^{-1}(X)\subset\overline X_1\). The induced \(k:X\to V\) is both open and proper, hence clopen, as in Lemma 6.1. Open restriction of ordinary direct image, followed by this clopen identification, gives
\[
\begin{aligned}
j_2^*h_*j_{1,!}E&\simeq(h|_V)_*k_*E\simeq E,\\
\kappa_h:j_{2,!}E&\longrightarrow h_*j_{1,!}E.
\end{aligned}
\tag{B.CR1}
\]
The second map is the open-adjunction transpose of the inverse of the first identification. These are natural maps of additive sheaf functors. Extend them termwise to complexes and to every homogeneous map; \(\kappa_h\) is closed of degree zero. No choice of an additive resolution functor is involved.

If \(q_1:j_{1,!}I\to J_1\) is an object of \(\mathcal C_1\), set \(q_2=(h_*q_1)\kappa_h\). The exact left adjoint \(h^*\) makes \(h_*J_1\) K-injective, by BF.4. We must also check that \(q_2\) is a quasi-isomorphism, rather than assume that \(h_*\) preserves arbitrary quasi-isomorphisms. On \(X\), restriction of \(q_1\) is a quasi-isomorphism from \(k_*I\) to the restriction of \(J_1\). Both are K-injective: clopen pushforward has exact left adjoint, and open restriction has the exact left adjoint given by extension by zero. Hence that restricted map is a homotopy equivalence, preserved by the additive functor \((h|_V)_*\). The restriction of \(q_2\) is therefore a quasi-isomorphism. Off \(X\), unbounded proper base change of Proposition 5.2 identifies the target stalk with the proper image of the zero restriction of \(j_{1,!}I\); both sides vanish there. Stalkwise detection proves the claim. This is the exact derived exchange of Lemma 6.1: on the open its adjoint is the same clopen identification. The common torsion annihilator is retained; there is no bounded-below or invertible-torsion-order restriction added here.

**A dg functor, including its homotopy component.** For a graph map \(t=(a,b,\tau)\) of degree \(n\), define
\[
\begin{aligned}
G_h(I,J_1,q_1)&=(I,h_*J_1,(h_*q_1)\kappa_{h,I}),\\
G_h(a,b,\tau)&=(a,h_*b,(h_*\tau)\kappa_{h,I}).
\end{aligned}
\tag{B.CR2}
\]
In particular, the homotopy component is not discarded. Naturality and closedness of \(\kappa_h\) give
\[
\begin{aligned}
&q_2'j_{2,!}a-(h_*b)q_2-d((h_*\tau)\kappa_{h,I})\\
&\qquad=h_*(q_1'j_{1,!}a-bq_1-d\tau)\kappa_{h,I}.
\end{aligned}
\tag{B.CR3}
\]
This proves preservation of the differential in the third component; the first two follow from additivity. For composable maps \(s,t\), the third component of their images' composite is
\(h_*(\tau_s j_{1,!}a_t+(-1)^{|s|}b_s\tau_t)\kappa_{h,I}\), by naturality once more. This is exactly the image of (B.RG3), including its sign. The units are preserved. Thus \(G_h\) is a dg functor.

The projections satisfy \(\pi_2G_h=\pi_1\). Both projections are quasi-isomorphisms on Hom complexes, by B.1k, so the same is true of \(G_h\). Given an object of \(\mathcal C_2\), choose in \(\mathcal C_1\) a replacement over its source \(I\). Its image under \(G_h\) and the given object become identical under \(H^0\pi_2\); full faithfulness lifts this identity and its inverse to a homotopy equivalence. Hence \(G_h\) is a dg quasi-equivalence, not merely an equivalence asserted on objects.

For refinements \(\overline X_0\xrightarrow{g}\overline X_1\xrightarrow{h}\overline X_2\), use the canonical identification \(h_*g_*\simeq(hg)_*\). At the sheaf level, open adjunction gives
\[
\kappa_{hg}=(h_*\kappa_g)\kappa_h,
\qquad G_hG_g\simeq G_{hg}.
\tag{B.CR4}
\]
Indeed restrict the two maps in the first identity to the protected open. Both are the inverse of the same clopen pushforward identification; their adjunction determines equality globally. The second identification sends the first component identically, the second by direct-image composition and the homotopy component by the same map. Its graph homotopy component is zero, because the first identity makes its square commute exactly. Direct-image composition on sections is rebracketing successive pullbacks of the same site object. All associations give the same pullback identification; consequently these closed graph isomorphisms satisfy their associativity pentagon and unit identities. This proves coherence for chains of refinements at the actual dg-model level, without choosing an inverse quasi-equivalence for each \(G_h\).

Likewise proper direct-image composition supplies a closed dg-natural isomorphism
\[
\beta_h:F_2G_h\xrightarrow{\sim}F_1,
\qquad p_{2,*}h_*J_1\xrightarrow{\sim}p_{1,*}J_1.
\tag{B.CR5}
\]
It is natural for all homogeneous graph maps, since those functors use the second component. It respects (B.CR4) by the same associativity of direct image. The resulting roofs therefore recover precisely the ordinary refinement comparison of Theorem 7.1, with its direction fixed by that exchange. No ordinary uniqueness argument is being substituted for (B.CR2)–(B.CR5).

**Compare the module adjunctions before making any lifts.** Abbreviate \(G=G_h\), \(\beta=\beta_h\), \(S=G_!\), \(T_i=(F_i)_!\), and \(U_i=F_i^*\). All induction functors are the actual balanced tensors of B.1l. For any right dg \(\mathcal D\)-module \(N\), the comparison of restriction modules is the strict isomorphism
\[
\chi_N:U_1N\longrightarrow G^*U_2N,
\qquad n\longmapsto n\beta_A\quad(n\in N(F_1A)).
\tag{B.CR6}
\]
Its differential and right-action identities follow from \(d\beta=0\) and \(\beta_{A'}F_2G(a)=F_1(a)\beta_A\). For representable \(N=h_L\) this is the map between the actual mapping bimodules, not an isomorphism of their cohomology dimensions.

The comparison on induction is the closed natural isomorphism
\[
\begin{aligned}
c_P:T_2SP&\longrightarrow T_1P,\\
[[p\otimes a]\otimes v]&\longmapsto[p\otimes\beta_A F_2(a)v],\\
[p\otimes w]&\longmapsto[[p\otimes1_{GA}]\otimes\beta_A^{-1}w].
\end{aligned}
\tag{B.CR7}
\]
Here \(p\in P(A)\), \(a:B\to GA\), and \(v:Y\to F_2B\). The last line is its inverse. The inner balancing relation follows from naturality of \(\beta\), and the outer relation from composition in \(\mathcal D\). For the inverse composite use those two balancing relations to absorb \(a\) and then \(v\). The differential agrees by the tensor Leibniz rule: none of the homogeneous factors is permuted, and \(\beta\) has degree zero. This checks (B.CR7) as a dg-module map with its inverse, not just on representable modules.

Its mate is the closed natural map
\[
\begin{aligned}
k_N:SU_1N&\longrightarrow U_2N,
&[n\otimes a]&\longmapsto n\beta_A F_2(a),\\
\epsilon^2_N T_2(k_N)&=\epsilon^1_N c_{U_1N}.
\end{aligned}
\tag{B.CR8}
\]
Balancing is again \(F_1(a')\beta=\beta F_2G(a')\). The second identity is checked on a tensor \([[n\otimes a]\otimes v]\): either side evaluates it to \(n\beta_A F_2(a)v\). For the units one has
\[
k_{T_1P}\,S(\eta^1_P)
=U_2(c_P)\,\eta^2_{SP}.
\tag{B.CR9}
\]
Both sides send \([p\otimes a]\) to \([p\otimes\beta_A F_2(a)]\). Equations (B.CR8)–(B.CR9) are identities of module maps before taking cohomology. Under successive refinements all these formulas flatten a tensor in its original order and compose the same \(\beta\)'s. Thus their composition and unit comparisons respect (B.CR4); no extra flatness or boundedness hypothesis enters.

Induction \(S\) preserves h-projectives and sends \(h_A\) to \(h_{GA}\), by B.1l. It restricts to a dg quasi-equivalence \(\mathcal Q(\mathcal C_1)\to\mathcal Q(\mathcal C_2)\). On representables, full faithfulness is the Hom quasi-isomorphism of \(G\); homotopy equivalences to representables extend it to all objects of these full subcategories. Essential surjectivity follows from that of \(H^0G\), using Yoneda to carry its homotopy equivalences to module homotopy equivalences. In particular the unit \(\eta^G_P:P\to G^*SP\) is an objectwise quasi-isomorphism for homotopy-representable \(P\): on a representable its values are precisely the Hom maps of \(G\), and the general case follows by a homotopy equivalence. This does not assert that ordinary induction preserves every quasi-isomorphism of arbitrary modules.

**Resolved adjoints and their actual homotopies.** Let \(N\in\mathcal Q(\mathcal D)\). Choose graph objects \(q_i:P_i\to U_iN\) as in B.1l. Since \(SP_1\) is h-projective, lift \(k_N S(q_1)\) through \(q_2\) to a closed map \(a_N:SP_1\to P_2\), with a degree-minus-one module map \(b_N\) such that
\[
\begin{aligned}
q_2a_N-k_NS(q_1)&=db_N,\\
e^2_N T_2(a_N)-e^1_N c_{P_1}
&=d\bigl(\epsilon^2_N T_2(b_N)\bigr).
\end{aligned}
\tag{B.CR10}
\]
Here \(e^i_N=\epsilon^i_NT_i(q_i)\). The first lift exists because \(\operatorname{Hom}(SP_1,q_2)\) is a quasi-isomorphism. The second identity follows by applying \(T_2\), then (B.CR8) and naturality of \(c\); it gives the counit-comparison homotopy explicitly.

The map \(a_N\) is a homotopy equivalence. After restricting along \(G\) and precomposing with \(\eta^G_{P_1}\), the first line of (B.CR10) identifies its composite with \(\chi_Nq_1\), up to the displayed homotopy. The identity \(G^*k_N\,\eta^G_{U_1N}=\chi_N\) is immediate on \(n\), and naturality of the unit gives this assertion. The other three maps \(q_2,\eta^G_{P_1},\chi_Nq_1\) are objectwise quasi-isomorphisms, so \(G^*a_N\) is one. Every object of \(\mathcal C_2\) is homotopy equivalent to a \(GA\); evaluation of any dg module carries such an equivalence to a homotopy equivalence. Hence \(a_N\) is a quasi-isomorphism at every object. Its endpoints are h-projective, so B.1l makes it a homotopy equivalence.

For clarity the unit comparison can also be traced through its homotopies. Put \(N=T_1P\), \(N'=T_2SP\). Choose resolved unit lifts \(u_1:P\to P_1(N)\), \(u_2:SP\to P_2(N')\) with \(q_iu_i-\eta^i=d\ell_i\), and lift \(c_P:N'\to N\) in the second right-resolution graph to \((c_P,r_c,h_c)\). Thus \(q_2(N)r_c-U_2(c_P)q_2(N')=dh_c\). Substituting these equations into (B.CR9) gives
\[
\begin{aligned}
q_2(N)\bigl(a_N S(u_1)-r_cu_2\bigr)&=dW,\\
W&=b_N S(u_1)+k_N S(\ell_1)\\
&\quad-U_2(c_P)\ell_2-h_cu_2.
\end{aligned}
\tag{B.CR11}
\]
All terms of \(W\) have degree minus one and source \(SP\). The Hom quasi-isomorphism \(\operatorname{Hom}(SP,q_2(N))\) now implies that the closed unit-comparison defect itself is a boundary. Taking its degree-minus-one preimage supplies its homotopy. This is a Hom-complex argument with a specified image \(W\), not a claim that the two chosen lifts are equal as chain maps.

There is also a direct check for two successive refinements. With \(S_h,S_g\) denoting their inductions and with the canonical identifications of (B.CR4) and (B.CR7), the composite chosen right comparison has witness
\[
\begin{aligned}
a_{h,g}&=a_h S_h(a_g),\\
b_{h,g}&=b_h S_h(a_g)+k_h S_h(b_g),\\
q_2a_{h,g}-k_{hg}S_{hg}(q_0)&=db_{h,g}.
\end{aligned}
\tag{B.CR12}
\]
Expand the first defining equation (B.CR10) for \(h\), substitute the one for \(g\), and use the strict mate identity \(k_{hg}=k_hS_h(k_g)\); all maps except the witnesses have degree zero. A separately chosen direct lift differs from this composite by a map whose image under \(\operatorname{Hom}(S_{hg}P_0,q_2)\) is a boundary. That Hom map is a quasi-isomorphism, so the difference is itself null-homotopic. These witnesses are retained in the resolution graphs, rather than suppressed by a claim of strictly natural resolution choices.

We have thus connected the earlier ordinary refinement proof to explicit dg functors, their canonical chain-of-refinement identifications, the actual mapping modules and the unit/counit comparison homotopies. The full ordinary statements, alternative compactification input and unbounded scope remain intact. The next required construction is the enhanced version of the general proper-open grids in Theorem 8.1, together with geometric base change, nearby attaching maps and normalized coefficient transport. The present refinement construction does not declare those diagrams complete or certify their recursive foundations. \(\square\)



### Proper–open exchange and horizontal resolution homotopies

**Proposition B.1n (general squares and the first horizontal correction).** In the Noetherian unbounded ordinary torsion scope of B.1e, the proper–open exchange has an actual comparison of dg resolution roofs. Vertically stacked squares give the same comparison as their outer rectangle. For two horizontally adjacent squares we construct the two-stage resolution comparison and its folding homotopy, including the three-input identity and compatibility with exchange. Folding is not asserted to be a strict dg functor. Arbitrary resolution strings, geometric base-change enhancements and coefficient transport remain separate obligations.

Use the cochain and graph signs of [B.1k](#resolution-graphs-and-the-proper-support-mapping-bimodule). Let the commutative square be
\[
\begin{matrix}
U&\xrightarrow{j}&T\\
p'\downarrow&&\downarrow p\\
V&\xrightarrow{i}&S,
\end{matrix}
\qquad j,i\text{ open},\quad p',p\text{ proper}.
\tag{B.PO1}
\]
The square need not be cartesian. Write \(J=j_!\), \(L=i_!\), \(P=p_*\), and \(P'=p'_*\) for the additive functors on complexes, not for unchosen derived-functor representatives. The right adjoints \(P,P'\) preserve K-injectives by BF.4.

**The map before replacement.** Put \(T_V=T\times_SV\), with \(w:T_V\hookrightarrow T\), \(a:T_V\to V\), and \(k:U\to T_V\). The graph argument in Compact supports, Lemma 6.1 makes \(k\) clopen. Ordinary open restriction and clopen pushforward give, on every sheaf and then termwise,
\[
i^*PJ\simeq a_*k_*\simeq P',
\qquad \epsilon:LP'\longrightarrow PJ.
\tag{B.PO2}
\]
Here \(\epsilon\) is the open-adjunction transpose of the inverse identification. It is a closed degree-zero natural transformation for all homogeneous maps. Neither side has been replaced by an asserted functorial injective resolution.

For a K-injective \(I\) on \(U\), choose an object \(x=(I,A,q:JI\to A)\) of \(\mathcal G_J\). The composite \((Pq)\epsilon_I:LP'I\to PA\) is a quasi-isomorphism. Indeed \(w^*q:k_*I\to w^*A\) is a quasi-isomorphism between K-injectives: both \(k_*\) and \(w^*\) have exact left adjoints. By BF.1 it is a homotopy equivalence, and \(a_*\) preserves that homotopy equivalence. This proves the claim after restriction to \(V\). On its closed complement, the unbounded proper-base-change comparison of Proposition 5.2 identifies \(PA\), representing \(Rp_*JI\), with the proper image of a zero restricted complex. The source also vanishes there. Geometric stalks prove the claim. This uses the common torsion annihilator, not an invertibility assumption or a bounded-below truncation.

Define \(\mathcal G_{LP'}\) with objects \((I,B,r:LP'I\to B)\), where the first object is still K-injective on \(U\) and \(B\) is K-injective on \(S\). Use (B.RG1)–(B.RG3) with the dg functor \(LP'\). The proof of B.1k uses only additivity on Hom complexes, existence of replacements and the K-injective Hom comparison, so applies without requiring \(LP'\) to be exact. We obtain
\[
\begin{aligned}
E:\mathcal G_J&\longrightarrow\mathcal G_{LP'},\\
(I,A,q)&\longmapsto(I,PA,(Pq)\epsilon_I),\\
(u,v,h)&\longmapsto(u,Pv,(Ph)\epsilon_I).
\end{aligned}
\tag{B.PO3}
\]
For the third differential component, naturality gives
\(r'LP'u-(Pv)r-d((Ph)\epsilon_I)
=P(q'Ju-vq-dh)\epsilon_I\).
For composition, the third component is
\(P(h_sJu_t+(-1)^{|s|}v_sh_t)\epsilon_I\), by the same naturality. Thus \(E\) preserves the differential, signed composition and units, not only closed maps. Its source projection equals that of \(\mathcal G_J\); both projections are quasi-equivalences by the Hom-cone proof. Two-out-of-three on each Hom complex makes \(E\) quasi-fully faithful. Every \(I\) has an object of \(\mathcal G_J\), and full faithfulness of the other projection lifts an identity of source objects to an isomorphism in \(H^0\). Thus \(E\) is essentially surjective there and is a dg quasi-equivalence. Output projection is exactly \(P\rho_J\).

The other roof computes \(i_!Rp'_*\): \(P'I\) already computes the proper direct image and \(L\) is exact. Consequently (B.PO3) compares the two actual roofs for the ordinary exchange of Lemma 6.1. Taking \(P'=\mathrm{id}\) recovers the refinement construction of B.1m. An arbitrary proper square does not make \(P'\) an equivalence; the quasi-equivalence assertion concerns the two graphs over the same source \(I\).

**Vertical pasting.** Stack a second square below (B.PO1), with bottom open \(M\), proper direct images \(Q,Q'\), and transformation \(\eta:MQ'\to QL\). Under the canonical direct-image composition identifications, open adjunction gives
\[
\epsilon_{\mathrm{outer}}=(Q\epsilon)(\eta P'),
\qquad
(QPq)\epsilon_{\mathrm{outer},I}
=Q((Pq)\epsilon_I)\eta_{P'I}.
\tag{B.PO4}
\]
For the first identity, restrict to the bottom open. Both maps are the same clopen-supported direct-image identification; the composition units in the adjunction identify their parentheses. The adjunction then determines the whole map. The second equality follows by functoriality. The same calculation for \(h\) proves equality of the graph homotopy components. This comparison can be performed in graphs over \(I\), restricting the second square along the dg functor \(P'\). Three or more vertical squares give the same ordered product of transformations. The canonical rebracketings satisfy the associator identity because they agree on every section. No choice of quasi-inverse to a graph projection is made.

**Why horizontal replacement requires a correction.** For two horizontal squares, use the exact additive open functors \(J,K\) above and \(L,M\) below, with proper direct images \(P_0,P_1,P_2\):
\[
\begin{matrix}
U_0&\xrightarrow{j}&U_1&\xrightarrow{k}&U_2\\
p_0\downarrow&&p_1\downarrow&&p_2\downarrow\\
V_0&\xrightarrow{i}&V_1&\xrightarrow{l}&V_2.
\end{matrix}
\qquad
\epsilon_1:LP_0\to P_1J,\quad
\epsilon_2:MP_1\to P_2K.
\tag{B.PO5}
\]
The diagram shows schemes and geometric maps: \(J=j_!\), \(K=k_!\), \(L=i_!\), \(M=l_!\), and \(P_a=p_{a,*}\). Ordinary open adjunction gives
\(\epsilon_{02}=(\epsilon_2J)(M\epsilon_1):MLP_0\to P_2KJ\): restrict to \(V_0\) and compare the identical clopen pushforward identifications, exactly as in Lemma 6.1. This is equality of natural transformations on complexes before choosing replacements.

Let \(\mathcal R_{K,J}\) have objects and degree-\(n\) maps
\[
\begin{aligned}
x&=(I,A,B,q:JI\to A,r:KA\to B),\\
t:x\to x'&=(u,v,z,\alpha,\beta),\\
|u|=|v|=|z|&=n,\qquad
\alpha:JI\to A',\quad\beta:KA\to B',
\quad |\alpha|=|\beta|=n-1.
\end{aligned}
\tag{B.PO6}
\]
All three objects are K-injective and \(q,r\) are closed quasi-isomorphisms. Apply the graph differential and composition separately to \((u,v,\alpha)\) and \((v,z,\beta)\), sharing \(v\). This is a dg category. Forgetting the last stage is degreewise surjective on Hom complexes; its kernel is the acyclic shifted cone for \(r^*\), as in (B.RG5). Every first-stage object has a last-stage replacement. Hence this projection, and then the projection to \(I\), are quasi-equivalences.

Exactness of \(K\) makes \(rKq\) a quasi-isomorphism. Define the object and chain-map parts of folding by
\[
\begin{aligned}
C(x)&=(I,B,rKq)\in\mathcal G_{KJ},\\
C_1(t)&=(u,z,\theta_t),\qquad
\theta_t=r'K\alpha+\beta Kq.
\end{aligned}
\tag{B.PO7}
\]
The equality \(DC_1=C_1D\) follows by expanding the third component: the two terms containing \(r'KvKq\) cancel. The first components and units agree as well. Since both source projections are Hom quasi-isomorphisms, \(C_1\) is a quasi-isomorphism on Hom complexes. But it need not preserve composition. If \(|s|=m\), expansion gives the following third component of \(C_1(st)-C_1(s)C_1(t)\), with the other two components zero:
\[
(-1)^m(r''Kv_s-z_sr')K\alpha_t
-\beta_sK(q'Ju_t-v_tq).
\tag{B.PO8}
\]
Discarding this expression would lose an actual horizontal coherence, even when its class later vanishes.

Here is its specified correction, a map of total degree \(m+n-1\) in \(\mathcal G_{KJ}\):
\[
\begin{aligned}
H(s,t)&=(0,0,(-1)^{m+1}\beta_sK\alpha_t),\\
C_1(st)-C_1(s)C_1(t)
&=DH(s,t)+H(Ds,t)+(-1)^mH(s,Dt).
\end{aligned}
\tag{B.PO9}
\]
The minus sign in the third component of (B.RG2) is important. Its contribution to the right side is
\((-1)^m(d\beta_s)K\alpha_t-\beta_sK(d\alpha_t)\).
The last two terms replace these differentials by
\(r''Kv_s-z_sr'\) and \(q'Ju_t-v_tq\), respectively; the unwanted differential terms cancel, leaving (B.PO8). This checks the formula for arbitrary homogeneous inputs, not just cycles. In particular closed degree-zero inputs give the displayed chain homotopy for their composition defect.

For three homogeneous inputs, \(|a|=\ell\), the correction satisfies the exact identity
\[
H(as,t)+H(a,s)C_1(t)
=H(a,st)+(-1)^\ell C_1(a)H(s,t).
\tag{B.PO10}
\]
To check it, use \(\beta_{as}=\beta_aKv_s+(-1)^\ell z_a\beta_s\) and \(\alpha_{st}=\alpha_sJu_t+(-1)^m v_s\alpha_t\). On either side the third component is the sum
\((-1)^{\ell+m+1}\beta_aKv_sK\alpha_t
+(-1)^{m+1}z_a\beta_sK\alpha_t
+(-1)^{\ell+1}\beta_aK\alpha_sKJu_t\).
The first two components are zero. The correction vanishes when either argument is an identity. Products of two correction triples vanish, since both of their first two components are zero. These are explicit normalized composition-homotopy identities for this two-stage fold; they do not assert that independently selected longer folds are already compatible.

**The horizontal exchange preserves the correction.** The two-square graph transfer sends
\[
\begin{aligned}
(I,A,B,q,r)\ &\longmapsto
 (P_0I,P_1A,P_2B,q_L,r_M),\\
q_L&=(P_1q)\epsilon_{1,I},\qquad
r_M=(P_2r)\epsilon_{2,A},\\
(u,v,z,\alpha,\beta)&\longmapsto
(P_0u,P_1v,P_2z,
 (P_1\alpha)\epsilon_{1,I},
 (P_2\beta)\epsilon_{2,A}).
\end{aligned}
\tag{B.PO11}
\]
The output is an object of \(\mathcal R_{M,L}\) by the quasi-isomorphism argument for (B.PO3), applied first to \(I\) and then to \(A\). Both component graph maps are dg maps, so (B.PO11) is a dg functor. Here its source has genuinely changed by \(P_0\); this functor is not asserted to be a quasi-equivalence. Its pulled-back square graphs over the original input are the quasi-equivalences used above.

Folding the bottom object gives
\((P_2r)\epsilon_{2,A}M(P_1q)M\epsilon_{1,I}
=P_2(rKq)\epsilon_{02,I}\), by naturality of \(\epsilon_2\). For homogeneous maps, naturality with respect to \(\alpha\) and \(q\) similarly identifies both terms of the folded homotopy. Most importantly, for the pure third component of (B.PO9),
\[
\begin{aligned}
&(-1)^{m+1}(P_2\beta_s)\epsilon_{2,A'}
 M\bigl((P_1\alpha_t)\epsilon_{1,I}\bigr)\\
&\hspace{1em}=
P_2\bigl((-1)^{m+1}\beta_sK\alpha_t\bigr)
\epsilon_{02,I}.
\end{aligned}
\tag{B.PO12}
\]
Thus the outer-square transfer carries the specified folding correction to the bottom folding correction, with its degree and sign. It also carries (B.PO10) to the same identity below. Vertical transfers respect these equalities by (B.PO4). This provides actual map and homotopy data for the elementary two-square horizontal comparison; ordinary pasting on \(H^0\) alone would not supply (B.PO9) or (B.PO12).

The geometric composition arrays of Theorem 8.1 use the general proper–open square map and the first horizontal resolution comparison above. Arbitrary strings, changes of those arrays, inverse-image/proper-image base change, nearby attaching maps and whole coefficient diagrams require further higher comparisons. The ordinary statements, alternate compactification argument and B.1m refinement maps do not by themselves give the full enhanced six-operation system. □



### All-length resolution folding and its higher components

**Proposition B.1o (folding without discarding higher maps).** Every finite string of exact additive functors between the Grothendieck abelian categories used here admits a strictly unital higher folding map from its iterated resolution graph to the graph for the composite. Its first component is a Hom-complex quasi-isomorphism; its higher components are given by finite path sums. The complete bar identity holds, and every binary parenthesization gives exactly the same bar map after the canonical functor-composition identifications. Proper–open exchange preserves all these components. This is the arbitrary-string folding construction for B.1n. It does not identify that fixed-string construction with completed geometric base-change, compactification-choice or coefficient coherence.

**The string model.** Let \(J_i:\mathcal A_{i-1}\to\mathcal A_i\), \(1\leq i\leq N\), be exact additive functors. Open extension and inverse image are examples; no assertion is made that they preserve K-injectives. An object of \(\mathcal R(J_N,\ldots,J_1)\) is
\[
x=(X_0,\ldots,X_N;q_1,\ldots,q_N),
\qquad q_i:J_iX_{i-1}\longrightarrow X_i,
\tag{B.RS1}
\]
where every \(X_i\) is K-injective and every \(q_i\) is a closed degree-zero quasi-isomorphism. For \(t:x\to x'\) of degree \(d\), retain vertex maps \(v_i(t):X_i\to X_i'\) of degree \(d\) and edge homotopies \(h_i(t):J_iX_{i-1}\to X_i'\) of degree \(d-1\). Use the graph formulas separately on each edge, sharing its vertex maps:
\[
\begin{aligned}
h_i(Dt)&=q_i'J_i v_{i-1}(t)-v_i(t)q_i-dh_i(t),\\
h_i(st)&=h_i(s)J_i v_{i-1}(t)
             +(-1)^{|s|}v_i(s)h_i(t).
\end{aligned}
\tag{B.RS2}
\]
The vertex differential is the Hom differential and vertex composition is ordinary composition. Thus the edgewise checks of [B.1k](#resolution-graphs-and-the-proper-support-mapping-bimodule) prove the dg axioms for the whole string. Forgetting the last stage is surjective in every degree on Hom complexes; its kernel is the acyclic cone for precomposition by \(q_N\), as in (B.RG5). Every shorter string has a last-stage replacement by BF.1. Induction shows that projection to \(X_0\) is a dg quasi-equivalence. This argument keeps all replacement choices as objects, not as an assumed additive resolution functor.

Put \(\Phi=J_N\cdots J_1\) and \(\Psi_i=J_N\cdots J_{i+1}\), with \(\Psi_N=\mathrm{id}\). Transport every edge to \(\mathcal A_N\): write \(\widetilde q_i=\Psi_iq_i\), \(\widetilde h_i=\Psi_ih_i\), and \(A_i=\Psi_iX_i\); in particular \(A_0=\Phi X_0\). The object part of folding is
\[
Q_x=\widetilde q_N\cdots\widetilde q_1:
\Phi X_0\longrightarrow X_N,
\qquad C(x)=(X_0,X_N,Q_x)\in\mathcal G_\Phi.
\tag{B.RS3}
\]
Exactness of every \(J_i\) makes \(Q_x\) a quasi-isomorphism. The intermediate \(A_i\) need not be K-injective; only the stated \(X_i\) and the final graph targets need be so.

**Paths and their degrees.** Take composable homogeneous inputs \(t_a:x^{a-1}\to x^a\), \(1\leq a\leq r\), with \(|t_a|=d_a\). For each increasing selection \(1\leq j_1<\cdots<j_r\leq N\), traverse edges from 1 to \(N\). At edge \(j_a\), use \(\widetilde h_{j_a}(t_a)\) and move from level \(a-1\) to level \(a\). At every other edge \(i\), use \(\widetilde q_i^{,a}\), where \(a\) is the number of selected edges already traversed. Compose in traversal order, with later factors on the left. Let
\[
W_r(t_r,\ldots,t_1)
=\sum_{1\leq j_1<\cdots<j_r\leq N}
   \operatorname{word}(j_1,\ldots,j_r).
\tag{B.RS4}
\]
Every summand maps \(\Phi X_0^0\) to \(X_N^r\) and has degree \(\sum_a d_a-r\). There are no factor permutations. The sum is zero for \(r>N\). For example, when \(N=3,r=2\), the selection \((1,3)\) is the homogeneous path
\[
A_0^0\xrightarrow{\ \widetilde h_1(t_1)\ }A_1^1
\xrightarrow{\ \widetilde q_2^{,1}\ }A_2^1
\xrightarrow{\ \widetilde h_3(t_2)\ }A_3^2.
\tag{B.RS5}
\]
Its arrow degrees are \(d_1-1,0,d_2-1\); this picture specifies one summand, not a claim that the homogeneous arrows are closed. The other two selections are \((1,2)\) and \((2,3)\), giving respectively
\(\widetilde q_3^{,2}\widetilde h_2(t_2)\widetilde h_1(t_1)\) and
\(\widetilde h_3(t_2)\widetilde h_2(t_1)\widetilde q_1^{,0}\).

Define graph-valued coefficients, of degree \(\sum d_a+1-r\), by
\[
\begin{aligned}
K_1(t)&=(v_0(t),v_N(t),W_1(t)),\\
K_r(t_r,\ldots,t_1)&=(0,0,W_r(t_r,\ldots,t_1))
                       \quad(r\geq2).
\end{aligned}
\tag{B.RS6}
\]
For \(N=2\), \(K_1\) is (B.PO7), and the correction of (B.PO9) is
\(H(s,t)=(-1)^{|s|+1}K_2(s,t)\).
The unsigned path coefficients therefore do not erase the earlier sign; it is encoded by the suspension convention that follows.

**All signs and the complete identity.** Use the larger-universe convention of B.1k and take the bar tensors over \(\mathbf Z\); the same formulas are linear over a common coefficient ring when the functors are linear over it. If \(sV\) denotes the degree-minus-one suspension, write \(|st|=|t|-1\). On the tensor cocategory of suspended Hom complexes, define the degree-one bar coderivation by
\[
b_1(st)=-s(Dt),\qquad
b_2(su\otimes st)=(-1)^{|u|}s(ut).
\tag{B.RS7}
\]
Extend by the Koszul sign given by the sum of suspended degrees to the left of the operation. Its square is zero: the one-input terms use \(D^2=0\), the two-input terms are the signed Leibniz identity, the three-input terms cancel by associativity, and disjoint odd operations anticommute. These are tensors and finite algebraic identities, not a claim that this bar construction is a flat resolution or computes a derived tensor product.

Let \(F\) be the degree-zero coalgebra map with object part \(C\) and Taylor coefficients
\(F_r(st_r\otimes\cdots\otimes st_1)=sK_r(t_r,\ldots,t_1)\).
On a finite input word its coalgebra extension is the sum over all ordered partitions into nonempty consecutive blocks. Hence every value is a finite sum; no completion or convergence assumption is present. To make \(bF=Fb\) completely explicit, put
\(p_i=\sum_{a=i+1}^r(d_a-1)\) and
\(e_k=\sum_{a=k+1}^r d_a+1-(r-k)\).
Suppress unchanged arguments in the two sums on the right. The identity is
\[
\begin{aligned}
&-D K_r(t_r,\ldots,t_1)\\
&\quad+\sum_{k=1}^{r-1}(-1)^{e_k}
 K_{r-k}(t_r,\ldots,t_{k+1})K_k(t_k,\ldots,t_1)\\
&=\sum_{i=1}^r(-1)^{p_i+1}K_r(\ldots,Dt_i,\ldots)\\
&\quad+\sum_{i=1}^{r-1}(-1)^{p_{i+1}+d_{i+1}}
 K_{r-1}(\ldots,t_{i+1}t_i,\ldots).
\end{aligned}
\tag{B.RS8}
\]
An empty sum is zero. In particular \(r=1\) says that \(K_1\) is a chain map, while \(r=2\) recovers the entire homogeneous-input identity (B.PO9).

Here is a wordwise proof for every \(N,r\). The \(q\)'s are closed and all have degree zero. Differentiating a path word therefore differentiates only a selected \(h_i(t_a)\), with sign \((-1)^{p_a}\) from the selected factors to its left. Substituting (B.RS2) into the first sum on the right of (B.RS8) makes its \(-dh_i(t_a)\) terms exactly these differentiated factors; the minus in the graph differential accounts for the initial \(-DK_r\). The vertex components for \(r=1\) obey the ordinary chain identity.

It remains to check the two vertex terms in
\(h_i(Dt_a)=q_i^aJ_iv_{i-1}(t_a)-v_i(t_a)q_i^{a-1}-dh_i(t_a)\).
Fix all selected edges other than the one carrying \(t_a\), and sum over its possible positions between its two neighbours. The positive term places \(v\) just before that edge, and the negative term just after it. At adjacent positions these give the same ordered word with opposite signs: all intervening \(q\)'s have degree zero. Thus the interior positions telescope. At a neighbouring selected edge, the two surviving words are precisely the two terms of the composition formula in (B.RS2). Their coefficients are \((-1)^{p_{a+1}+d_{a+1}}\), the bar sign for merging that adjacent pair, including the \((-1)^{d_{a+1}}\) on its second graph-composition term. These are the second sum on the right of (B.RS8).

At the two outside ends, the surviving vertex maps instead multiply the folded output. For \(r=1\) they are \(Q_{x^1}\Phi v_0-v_NQ_{x^0}\) in its graph differential. For \(r\geq2\) they are the two end-split products on the left of (B.RS8), with sign \((-1)^{e_k}\). Every internal split with both block lengths at least two is zero: both graph triples have zero first and second components, so (B.RG3) makes their product zero. These exhaust the differentiated, merged and endpoint words. This proves (B.RS8), including the case \(r>N\), where the displayed path coefficient itself vanishes but the endpoint and merging terms must still cancel. It proves \(bF=Fb\), not only identities on cycles or a fixed finite list of arities.

The unit has all edge homotopies zero. Therefore \(K_1\) preserves it and every higher coefficient with a unit among its inputs vanishes. For the empty string take \(\Phi=\mathrm{id}\), \(Q=1\), \(K_1(v)=(v,v,0)\) and all higher coefficients zero. This specifies the unital higher folding map also at length zero.

**Quasi-equivalence and all parenthesizations.** The source projections of both the string category and \(\mathcal G_\Phi\) are Hom-complex quasi-isomorphisms, and projection after \(K_1\) is the original vertex projection. Hence \(K_1\) is a quasi-isomorphism on every Hom complex. The \(r=2\) identity makes its induced \(H^0\) map preserve composition. Every K-injective initial object has a resolution string, so full faithfulness of the target projection lifts identities of initial objects to isomorphisms between the corresponding folded and arbitrary target objects. Thus the higher folding map is a quasi-equivalence in the precise sense of Hom quasi-isomorphisms and essential surjectivity on \(H^0\).

We also compare the maps obtained by successive binary folds, not just their object values. Split the edge interval into consecutive left and right intervals. Write \(W_0\) for the product of its \(q\)'s at the specified object level. The binary coalgebra-composition formula gives the higher homotopy component
\[
\sum_{k=0}^r
 W_{r-k}^{\mathrm{right}}(t_r,\ldots,t_{k+1})
 W_k^{\mathrm{left}}(t_k,\ldots,t_1).
\tag{B.RS9}
\]
All interval maps are transported to the final category before multiplication. The zero-length right block uses the final object level \(r\); the zero-length left block uses level zero. In a middle split, the right interval starts at level \(k\). These conventions are the endpoint data of the word, not additional choices.

For completeness, the child folds combine into the two-stage graph because they share the middle vertex projection, whose higher components are zero. Its two edge identities are the child identities (B.RS8). Composing with the two-stage fold then gives (B.RS9): the first coefficient supplies the two endpoint terms, and its second coefficient supplies each nonempty two-block split. There are no further coefficients of that binary fold. No extra signs occur in coalgebra composition, since these suspended coalgebra maps have degree zero.

Each selection of \(r\) increasing edges has a unique number \(k\) in the left interval. Conversely, its left and right selections determine the whole selection and the same ordered word. Thus (B.RS9) is exactly \(W_r\). Induction on a binary tree proves
\[
F^{\mathcal T}_r=F_r
\quad\text{for every binary parenthesization }\mathcal T
\text{ and every }r\geq1.
\tag{B.RS10}
\]
The vertex components agree as well. Associativity polygons, including the pentagon, therefore commute as these bar maps: every route gives the same coefficients, not just homologous ones. This statement concerns folds of the fixed resolved string; it does not silently choose resolutions for changing geometric inputs.

**Exchange on every higher component.** Consider a horizontal string of proper–open squares, with top exact functors \(J_i\), bottom exact functors \(L_i\), proper direct images \(P_i\), and closed natural exchanges
\(\epsilon_i:L_iP_{i-1}\to P_iJ_i\).
The dg string transfer is the edgewise construction of [B.1n](#proper-open-exchange-and-horizontal-resolution-homotopies):
\[
\begin{aligned}
X_i&\longmapsto P_iX_i,\\
q_i&\longmapsto(P_iq_i)\epsilon_{i,X_{i-1}},\\
v_i(t)&\longmapsto P_iv_i(t),\qquad
h_i(t)\longmapsto(P_ih_i(t))\epsilon_{i,X_{i-1}}.
\end{aligned}
\tag{B.RS11}
\]
All output vertices are K-injective, and the output edges are quasi-isomorphisms by the proper–open graph comparison already proved there. Let \(\epsilon_{\mathrm{out}}:L_N\cdots L_1P_0\to P_NJ_N\cdots J_1\) be the ordered composite of the exchanges. Moving each closed degree-zero \(\epsilon_i\) through the next homogeneous factor by naturality, one edge at a time, proves on every selected path, hence on its sum,
\[
W_r^{\mathrm{bottom}}(Et_r,\ldots,Et_1)
=P_N\bigl(W_r^{\mathrm{top}}(t_r,\ldots,t_1)\bigr)
  \epsilon_{\mathrm{out},X_0^0}.
\tag{B.RS12}
\]
The same equality for \(r=0\) identifies the folded replacement maps. For \(r=1\) the endpoint vertex maps are also those of the outer graph transfer. For \(r\geq2\) both endpoint components are zero. Thus exchange commutes with every Taylor coefficient of folding and with (B.RS10). There is no degree sign hidden in moving an exchange: its degree is zero. The vertical pasting identity (B.PO4) makes successive vertical transfers give this same comparison for the outer vertical rectangle. This closes the arbitrary-length horizontal-folding comparison for these proper–open strings, while preserving all specified homotopies.

The exactness and K-injective arguments apply to unbounded complexes; no finite global dimension, coefficient flatness or bounded-below condition has been inserted. The path sums are finite because a composition string has finitely many edges, not because the complexes are bounded. What remains is to construct the actual inverse-image/proper-image base-change graph comparisons and integrate changing compactification arrays, then the geometric nearby attaching maps and whole normalized coefficient diagrams. □



### Canonical proper base change on resolution graphs

**Proposition B.1p (the enhanced comparison for proper squares).** Let \(\Lambda\) be a commutative ring with \(n\Lambda=0\) for some positive integer \(n\). In a cartesian square of schemes
\[
\begin{matrix}
X'&\xrightarrow{a}&X\\
f'\downarrow&&\downarrow f\\
Y'&\xrightarrow{g}&Y,
\end{matrix}
\qquad f\text{ proper},
\tag{B.BC1}
\]
use the small étale sites and inverse images of sheaves of \(\Lambda\)-modules. The canonical proper-base-change map has the dg graph presentation below for all unbounded complexes. It respects vertical composition of proper maps and every higher folding component for every finite sequence of base changes. These are comparisons of specified models; the further integration with changing compactifications, exceptional adjunctions and nearby-cycle pairings is not inferred from them.

There is no Noetherian, bounded-below, finite-global-dimension or invertibility-of-\(n\) assumption in this proper-square assertion. The common annihilator is essential to the invoked unbounded provider. Proper base change, §1 separately supplies the bounded-below torsion-cohomology theorem over arbitrary coefficients; that does not supply an unrestricted unbounded arbitrary-ring extension.

**Keep the canonical map.** Write \(A=a^*\), \(G=g^*\), \(P=f_*\), and \(P'=f'_*\). The inverse-image functors are exact. Direct image preserves K-injectives by the actual Hom-complex adjunction of BF.4. Let \(\eta^a\) be the unit of \(a^*\dashv a_*\), and \(\epsilon^g\) the counit of \(g^*\dashv g_*\). Using \(Pa_*\cong g_*P'\), the underived comparison, extended termwise, is the closed degree-zero natural transformation
\[
\begin{aligned}
\beta&:GP\longrightarrow P'A,\\
\beta_M&=\epsilon^g_{P'AM}\,G(P\eta^a_M),\\
(P'A u)\beta_I&=\beta_{I'}(GPu).
\end{aligned}
\tag{B.BC2}
\]
for every homogeneous \(u:I\to I'\), not just chain maps. Indeed the sheaf naturality identity holds on each component \(u^k:I^k\to I'^{k+|u|}\); the transformation is of degree zero, so no sign is introduced. Commutation with the complex differential follows by applying the same identity to \(d_I\).

Take \(I\) K-injective on \(X\), and any closed quasi-isomorphism \(q:AI\to J\) with \(J\) K-injective on \(X'\). The map
\[
\alpha_{I,J,q}=(P'q)\beta_I:
GPI\longrightarrow P'J
\tag{B.BC3}
\]
is a quasi-isomorphism. Here is why it is the required map rather than an abstract isomorphism. The source computes \(g^*Rf_*I\), since \(I\) is K-injective and \(G\) is exact. The target computes \(Rf'_*a^*I\). The adjunction construction in §1 of the proper-base-change lesson identifies (B.BC3) with its canonical comparison. Compact support, Proposition 5.2 proves that this very map is invertible: locally a finite fibre-dimension bound gives finite cohomological amplitude; for a termwise injective K-injective resolution the pulled-back terms are \(f'_*\)-acyclic, and Lemma 5.1 permits their unbounded complex to compute the derived image. No exactness of \(P'\) on arbitrary complexes is asserted. To pass to an arbitrary K-injective representative, compare it by a quasi-isomorphism with a termwise injective K-injective representative, using BF.1. That map is a homotopy equivalence, preserved by all the termwise additive functors here. Lift the corresponding map between the chosen pulled-back replacements by the BF.1 Hom quasi-isomorphism. Its naturality homotopy survives \(P'\). Hence the canonical map for the arbitrary representative is the same derived isomorphism.

**The two graphs share the original input.** Form \(\mathcal G_A\) and \(\mathcal G_{GP}\) over \(\mathcal I(X_{\mathrm{et}},\Lambda)\), with their respective target K-injective categories on \(X'\) and \(Y'\). The functor \(GP\) is additive but need not be exact. This is allowed: the proof of (B.RG5) uses only a K-injective graph target and the quasi-isomorphism of its replacement. Every complex \(GPI\) has such a replacement. Define
\[
\begin{aligned}
E_{f,g}(I,J,q)&=(I,P'J,(P'q)\beta_I),\\
E_{f,g}(u,v,h)&=(u,P'v,(P'h)\beta_I).
\end{aligned}
\tag{B.BC4}
\]
The first entry is \(I\), not \(PI\). In a degree-\(d\) triple, \(h:AI\to J'\) has degree \(d-1\), so its image has source \(GPI\), target \(P'J'\), and that same degree. Equation (B.BC3) and preservation of K-injectives make the object formula valid.

The third component of the target differential is
\[
\begin{aligned}
 &(P'q')\beta_{I'}GPu-(P'v)(P'q)\beta_I
       -d((P'h)\beta_I)\\
 &\hspace{1em}=P'(q'Au-vq-dh)\beta_I.
\end{aligned}
\tag{B.BC5}
\]
For \(|s|=m\), its composition component is
\(P'(h_sAu_t+(-1)^m v_sh_t)\beta_I\), by (B.BC2). Thus (B.BC4) is a unital dg functor. Both graph projections to the same \(I\) are quasi-equivalences by (B.RG5), and \(\pi E_{f,g}=\pi\). It follows on Hom complexes by two-out-of-three that \(E_{f,g}\) is a quasi-isomorphism. For essential surjectivity, choose an \(A\)-replacement over the original input of a target graph object. Full faithfulness of the target projection on \(H^0\) lifts the identity of that input to an isomorphism between the two target graph objects. This proves that \(E_{f,g}\) is a dg quasi-equivalence. It does not claim that \(P\), or a functor changing the source to \(PI\), is an equivalence.

The target projection after (B.BC4) is exactly \(P'\rho_A\). Together with the quasi-equivalences on the left, it compares the roof for \(g^*Rf_*\) with the roof for \(Rf'_*a^*\). Closed degree-zero triples retain the naturality homotopy in (B.BC5); higher homogeneous triples are not discarded.

**Vertical proper composites.** Stack a cartesian proper square for \(p:Y\to Z\), with inverse image \(H=h^*\), direct images \(R=p_*\), \(R'=p'_*\), and comparison \(\gamma:HR\to R'G\). The adjunction units give, under the canonical direct-image composition identifications,
\[
\beta_{pf,h}=(R'\beta)(\gamma P):
HRP\longrightarrow R'P'A.
\tag{B.BC6}
\]
This is an equality of termwise natural transformations. Substitute the unit/counit formula (B.BC2) for the two factors on the right and transpose through \(H\dashv h_*\). Naturality moves the unit for \(a\) past the middle comparison; the unit and counit of \(G\dashv g_*\) then cancel by the triangle identity. The remaining transpose is \(RP\eta^a\), followed by \(RPa_*\cong h_*R'P'\), exactly the transpose of the left side. This also specifies the direct-image composition convention in §1 of the proper-base-change provider.

Do not compose wrongly typed graph functors. First (B.BC4) gives an edge \(G(PI)\to P'J\); its input on \(Y\) is the K-injective \(PI\). Apply the second square to that edge, retaining the original label \(I\) and forcing its input maps to be \(Pu\). The resulting graph over \(I\) has object map and homotopy component
\[
\begin{aligned}
 &(R'P'q)(R'\beta_I)\gamma_{PI},\\
 &(R'P'h)(R'\beta_I)\gamma_{PI},
\end{aligned}
\tag{B.BC7}
\]
and vertices \((I,R'P'J)\), with maps \((u,R'P'v)\). By (B.BC6) these are exactly the direct outer-square formulas. For three or more vertical proper maps, iterating the composite-unit formula and ordinary associativity gives the same ordered factors; this proves all finite vertical pasting identities, including identities. The canonical composition identifications are retained, not replaced by literal equality of differently bracketed sheaf functors.

**Successive base changes and every higher component.** Let \(Y_N\to\cdots\to Y_0\) be any finite string of base maps, let \(X_i=X_0\times_{Y_0}Y_i\), and let \(f_i:X_i\to Y_i\) be the pulled-back proper maps. Put \(A_i=a_i^*\), \(G_i=g_i^*\), \(P_i=f_{i,*}\). Each square has
\(\beta_i:G_iP_{i-1}\to P_iA_i\). For an \(A\)-resolution string \((I_i,q_i)\) of B.1o, set
\[
\begin{aligned}
 I_i^{Y}&=P_iI_i,&
 q_i^{Y}&=(P_iq_i)\beta_{i,I_{i-1}},\\
 v_i^{Y}(t)&=P_iv_i(t),&
 h_i^{Y}(t)&=(P_ih_i(t))\beta_{i,I_{i-1}}.
\end{aligned}
\tag{B.BC8}
\]
Every vertex is K-injective and every replacement is a quasi-isomorphism by (B.BC3), applied to the K-injective \(I_{i-1}\). The differential and composition calculation (B.BC5) works on each edge. To compare equivalent source models, define the pulled-back \(G\)-string category to retain \(I_0\), with first vertex forced to be \(P_0I_0\) and its map forced to be \(P_0u\). All later vertices and edges remain free replacement data. Its projection to \(I_0\) is a quasi-equivalence: forget the final stage successively, using the same acyclic Hom cones as (B.RG5); the length-zero category is precisely \(\mathcal I(X_0)\). The map (B.BC8) into this pulled-back category is therefore a quasi-equivalence over \(I_0\). The unlabelled functor to all \(G\)-strings need not be one.

Let \(A^{[N]}=A_N\cdots A_1\) and \(G^{[N]}=G_N\cdots G_1\). The outer underived comparison is determined recursively by
\[
\beta^{[N]}=(\beta_N A^{[N-1]})(G_N\beta^{[N-1]}):
G^{[N]}P_0\longrightarrow P_NA^{[N]},
\quad \beta^{[0]}=1_{P_0}.
\tag{B.BC9}
\]
The identity is again the adjunction-unit formula, now for successive inverse images. In the path sums (B.RS4), slide these degree-zero comparisons through each homogeneous \(q_i\) and \(h_i\), using (B.BC2) at that edge. Each increasing edge selection gives the same ordered word on both sides. Summing the finite set of selections gives
\[
W_r^{Y}(Et_r,\ldots,Et_1)
=P_N\bigl(W_r^{X}(t_r,\ldots,t_1)\bigr)
  \beta^{[N]}_{I_0^0}.
\tag{B.BC10}
\]
For \(r=0\), this compares the folded replacement maps. For \(r=1\), the endpoint maps are exactly those of (B.BC4) for the outer square; for \(r\geq2\), both endpoint components are zero. Thus folding in the pulled-back \(G\)-string category agrees, in every Taylor coefficient, with first folding the \(A\)-string and then applying the outer-square graph map. The full bar identity, strict units and exact agreement of all binary parenthesizations follow from B.1o and this equality; equality merely on cohomology is not being substituted. Terms of arity greater than \(N\) are zero on both sides. The length-zero case is the identity roof.

Finally, for a finite rectangular grid of proper maps and base changes, vertical pasting uses (B.BC6) edge by edge. In a horizontal path word, naturality moves those vertical factors to the same outside position. Both orders therefore give (B.BC10) for the outer rectangle, with the same vertically composed direct images. This proves interchange on every homogeneous Taylor coefficient for these fixed cartesian proper grids. It uses neither exactness of proper direct image nor preservation of K-injectives by inverse image.

**Compact-support base change.** Compact support, Theorem 9.1 factors compact-support base change into this proper comparison and the exact open-base-change isomorphism \(a^*j_!\cong j'_!u^*\). Its ordinary refinement and composition identities do not themselves identify all the enhanced roofs. Applying B.1m–B.1p to compact support also requires the open, compactification and refinement diagrams and their adjunction units and counits. Geometric nearby-cycle descent, attaching-map and logarithmic-pairing comparisons, and normalized coefficient completion remain their stated obligations. \(\square\)



### Compact-support base change and refinement cubes

**Proposition B.1q (one comparison through the actual resolution roofs).** Retain the full Noetherian, unbounded ordinary torsion-ring scope of B.1e. Let \(f:U\to Y\) be separated of finite type, choose a compactification \(f=pj\), and let \(g:Y'\to Y\) be a base change with \(Y'\) Noetherian. Use the pulled-back factorization:
\[
\begin{matrix}
U'&\xrightarrow{j'}&X'&\xrightarrow{p'}&Y'\\
u\downarrow&&a\downarrow&&g\downarrow\\
U&\xrightarrow{j}&X&\xrightarrow{p}&Y.
\end{matrix}
\quad
\begin{gathered}
j,j'\text{ open},\\ p,p'\text{ proper}.
\end{gathered}
\tag{B.CB1}
\]
The two squares are cartesian. There is an explicit zigzag of dg or strictly unital higher quasi-equivalences between resolution roofs for \(g^*Rf_!\) and \(Rf'_!u^*\). It represents the canonical map of Compact support, Theorem 9.1. The zigzag commutes with proper refinement through the maps below, including its homogeneous homotopy components and higher folding corrections. No finite-global-dimension, bounded-below or invertible-torsion-order restriction is added. The ordinary theorem, including its other stated domains, remains intact; it is not replaced by this enhanced-model assertion.

**Open base change before choosing resolutions.** Put \(J=j_!\), \(J'=j'_!\), \(A=a^*\), \(V=u^*\), \(G=g^*\), \(P=p_*\), and \(P'=p'_*\). The four functors \(J,J',A,V\) are exact. There is a closed degree-zero natural isomorphism
\[
\theta:AJ\xrightarrow{\sim}J'V.
\tag{B.CB2}
\]
On the pulled-back open it is the identity under the inverse-image composition identifications; off that open both sheaves have zero stalks. More intrinsically, open adjunction gives the map \(J'V\to AJ\) whose restriction is this identity, and the stalk calculation proves it invertible; \(\theta\) is its inverse. This specifies a canonical map, natural for every sheaf morphism, hence termwise for every homogeneous complex map. For successive base changes and identities, all the comparison maps restrict to the same identity and have zero complementary stalks. Their composites therefore agree. In particular, \(\theta\) is not a choice of an isomorphism between derived objects.

For an exact functor \(T\), write \(\mathcal G_T\) with the original K-injective input on \(U\), as in B.1k. Equation (B.CB2) gives a strict dg isomorphism
\[
\begin{aligned}
\Theta:\mathcal G_{AJ}&\longrightarrow\mathcal G_{J'V},\\
(I,K,Q)&\longmapsto(I,K,Q\theta_I^{-1}),\\
(x,z,H)&\longmapsto(x,z,H\theta_I^{-1}).
\end{aligned}
\tag{B.CB3}
\]
Its inverse precomposes the third entries by \(\theta_I\). Closed degree-zero naturality verifies both the graph differential and signed composition, including for nonclosed homogeneous triples. The endpoint maps are unchanged.

**The left-hand roof really computes the pulled-back proper support.** Let \(\mathcal C=\mathcal G_J\) and \(H=GP\rho_J:\mathcal C\to\operatorname{Ch}(Y',\Lambda)\). Here \(H(x,y,\alpha)=GPy\). A resolution graph \(\mathcal R_H\) over this dg category has objects \((c,L,s:Hc\to L)\), with \(L\) K-injective and \(s\) a closed quasi-isomorphism. Its degree-\(d\) maps are \((t,w,\delta)\), with \(t\in\mathcal C^d(c,c')\), \(w\in\operatorname{Hom}^d(L,L')\), and \(\delta\in\operatorname{Hom}^{d-1}(Hc,L')\). Use
\[
\begin{aligned}
D(t,w,\delta)&=(Dt,dw,s'H(t)-ws-d\delta),\\
(t_2,w_2,\delta_2)(t_1,w_1,\delta_1)
 &=(t_2t_1,w_2w_1,
       \delta_2H(t_1)+(-1)^{|t_2|}w_2\delta_1).
\end{aligned}
\tag{B.CB4}
\]
The B.1k verification works for a dg base category: the Hom kernel of projection to \(c\) is still \(\operatorname{Cone}(s^*)[-1]\), acyclic since the receiving \(L'\) is K-injective. Every \(Hc\) has a replacement, so that projection is a dg quasi-equivalence. Thus \(\mathcal R_H\) supplies an actual roof for \(g^*Rf_!\), without assuming that \(G\) preserves K-injectives or that \(P\) is exact.

Write a two-edge object of \(\mathcal R(A,J)\) as \((I,B,K;q:JI\to B,r:AB\to K)\). For a homogeneous map use vertices \((x,y,z)\) and edge homotopies \((\alpha,\delta)\), in the conventions of B.1o. The proper-base-change transformation \(\beta:GP\to P'A\) of B.1p defines
\[
\begin{aligned}
E_p(I,B,K;q,r)&=((I,B,q),P'K,(P'r)\beta_B),\\
E_p(x,y,z;\alpha,\delta)
 &=((x,y,\alpha),P'z,(P'\delta)\beta_B).
\end{aligned}
\tag{B.CB5}
\]
The object map is a quasi-isomorphism by (B.BC3), applied to the K-injective \(B\). Its target is K-injective. Equation (B.BC5), with the shared base map \((x,y,\alpha)\), proves the dg identities. Both projections to \(\mathcal C\) are quasi-equivalences, so \(E_p\) is one as well, by Hom two-out-of-three and lifting the identity in \(H^0\). Its output is exactly \(P'K\).

The right-hand operation \(Rf'_!u^*\) is computed by \(\mathcal R(J',V)\), with output \(P'\) of the last vertex. Use the higher folds \(C_L,C_R\) from B.1o to obtain
\[
\mathcal R_H
\xleftarrow{\ E_p\ }\mathcal R(A,J)
\xrightarrow{\ \Theta C_L\ }\mathcal G_{J'V}
\xleftarrow{\ C_R\ }\mathcal R(J',V).
\tag{B.CB6}
\]
All these comparison categories retain the original \(I\). The middle arrows are higher quasi-equivalences, not falsely asserted strict dg folds. Their object-level common replacement is \(Q=rAq\,\theta_I^{-1}:J'VI\to K\). The output functor on the common graph is \(P'\rho\). For the first Taylor coefficient its value is \(P'z\); for every higher coefficient it is zero, since folding's higher coefficients have zero endpoint vertices. Consequently the output functors agree on the nose along these comparisons. The nonzero higher *graph homotopies* are nevertheless retained in the middle categories. The map on derived values is first \((P'r)\beta_B:GPB\to P'K\), followed by the identification of \(K\) as a replacement of \(J'VI\). Thus it is precisely the proper/open factorization in Theorem 9.1.

**The refinement cube before resolutions.** Suppose \(h:X_1\to X_2\) is a proper refinement between two compactifications of \(f\), and let \(h':X'_1\to X'_2\) be its pullback. Put \(T=h_*\), \(T'=h'_*\), \(A_i=a_i^*\), \(J_i=j_{i,!}\), \(J_i'=j'_{i,!}\). Let
\(\kappa:J_2\to TJ_1\), \(\kappa':J_2'\to T'J_1'\)
be the clopen/open-adjunction comparisons of (B.CR1), and let \(\beta_h:A_2T\to T'A_1\) be proper base change before resolutions. The fundamental cube identity is
\[
(T'\theta_1)(\beta_hJ_1)(A_2\kappa)
   =(\kappa'V)\theta_2:
A_2J_2\longrightarrow T'J_1'V.
\tag{B.CB7}
\]
To prove it, identify the source by \(\theta_2\) with \(J_2'V\) and use the \(j'_2\)-adjunction. The inverse image of the protected open under \(h\) contains the given copy of \(U\) as a clopen subscheme; this is exactly the construction of Lemma 6.1 and (B.CR1). Pullback preserves that clopen subscheme. After restriction to \(U'\), open restriction of direct image and clopen pushforward identify both sides of (B.CB7) with the identity on \(V\). The proper comparison there is its unit-defined map, whose restriction is the same clopen identity. The adjunction is injective on maps from \(J_2'V\), hence determines equality globally. This proves the identity on sheaves, then on all complex degrees and homogeneous maps, before passing to a derived category.

**Lift the cube without discarding its edge homotopies.** The refinement functor between the left two-edge models is
\[
\begin{aligned}
\mathcal H(I,B,K;q,r)
 &=\bigl(I,TB,T'K;(Tq)\kappa_I,(T'r)\beta_{h,B}\bigr),\\
\mathcal H(x,y,z;\alpha,\delta)
 &=\bigl(x,Ty,T'z;(T\alpha)\kappa_I,
                         (T'\delta)\beta_{h,B}\bigr).
\end{aligned}
\tag{B.CB8}
\]
The first edge is a valid refinement replacement by B.1m and the second a valid proper-base-change replacement by B.1p. Its vertices are K-injective. The two edge calculations show it is a dg functor; projection to the same original \(I\) proves it a quasi-equivalence. Direct-image composition gives the closed output isomorphism \(P'_2T'K\cong P'_1K\).

On the common graphs define \(\Xi:\mathcal G_{J'_1V}\to\mathcal G_{J'_2V}\) by
\[
\begin{aligned}
\Xi(I,K,Q)&=(I,T'K,(T'Q)\kappa'_{VI}),\\
\Xi(x,z,H)&=(x,T'z,(T'H)\kappa'_{VI}).
\end{aligned}
\tag{B.CB9}
\]
One must not assume \(VI\) is K-injective. The replacement assertion instead uses Theorem 7.1 on the actual unbounded object \(VI\). Its canonical refinement comparison is represented by \((T'Q)\kappa'_{VI}\), since \(K\) is a K-injective replacement of \(J'_1VI\); it is a quasi-isomorphism. This is the full ordinary refinement result already supplied there, not exactness of \(T'\) on arbitrary quasi-isomorphisms. The same homogeneous naturality calculation as (B.CR3), now for the composite functors \(J_i'V\), makes (B.CB9) a dg functor. Its projections to \(I\) are quasi-equivalences, so it too is one.

For \(r=0,1,2\), let \(W_r^i\) be the folded path sum of the two-edge model for \((A_i,J_i)\), with \(W_0^i\) its object replacement. Naturality of \(\beta_h\) and \(\kappa\) in every homogeneous factor gives
\[
\begin{aligned}
W_r^2(\mathcal Ht_r,\ldots,\mathcal Ht_1)\theta_{2,I_0}^{-1}
 &=T'\bigl(W_r^1(t_r,\ldots,t_1)\bigr)
       (\beta_{h,J_1I_0})(A_2\kappa_{I_0})\theta_{2,I_0}^{-1}\\
 &=T'\bigl(W_r^1(t_r,\ldots,t_1)\theta_{1,I_0}^{-1}\bigr)
       \kappa'_{VI_0}.
\end{aligned}
\tag{B.CB10}
\]
For \(r=0\) there are no input maps and \(I_0\) is the object's original input. For \(r\geq1\), it is the original input of the first source object. The second equality is exactly (B.CB7). To check the first, the three possible path expressions are \(rAq\), \(r_{\mathrm{target}}A\alpha+\delta A q_{\mathrm{source}}\), and \(\delta(t_2)A\alpha(t_1)\). Substitute (B.CB8), slide the degree-zero comparison through the indicated \(q\) or \(\alpha\), and each has the same outside factor \((\beta_hJ_1)(A_2\kappa)\). No factor is permuted, so no sign is lost. Higher arities are zero for this two-edge fold. The endpoint components agree as well. Hence \(\Theta_2 C_L^2\mathcal H=\Xi\Theta_1 C_L^1\) as higher functors, not merely on their degree-zero cohomology.

On the right two-edge models the corresponding refinement keeps the \(V\)-replacement vertex and applies \(T'\) to the final vertex; the second edge and its homotopy are precomposed by \(\kappa'\). Equation (B.RS12), applied to this identity/proper refinement, proves that its fold commutes with \(\Xi\) in every coefficient. Finally the left edge of (B.CB6) commutes with refinement: after identifying \(P_2T=P_1\) and \(P'_2T'=P'_1\), the new comparison map is
\[
(P'_2T'r)(P'_2\beta_{h,B})\beta_{p_2,TB}
   =(P'_1r)\beta_{p_1,B},
\tag{B.CB11}
\]
by (B.BC6). Replacing \(r\) by the homogeneous second-edge homotopy \(\delta\) gives exactly the same identity for that component; the base edge is (B.CR2). Thus the entire zigzag (B.CB6) has the required refinement cube, with its specified proper-image composition identifications.

For a finite chain of refinements, (B.CR4) composes the \(\kappa\)'s and (B.BC6) composes the proper comparisons. Substitution in (B.CB8)–(B.CB11) gives the same ordered factors as the outer refinement. Their canonical composition isomorphisms have zero graph homotopy component and satisfy the unit and associativity identities of B.1m. For successive changes of base, use the cocycle of (B.CB2) and the all-length proper comparison (B.BC10). Expand the intervening resolution strings and use B.1o: every selected-edge word has the same degree-zero cube factors slid to its outside, so the same argument holds in every arity and for every binary parenthesization. This proves the compatibility of these fixed compactification/base-change/refinement diagrams without selecting strictly natural resolution inverses. Common refinements from Lemma 3.1 connect any two chosen compactifications through these quasi-equivalences; the actual refinement diagram is retained rather than suppressed into an asserted strict identification.

The result gives the enhanced base-change and refinement comparisons for proper-support roofs. It does not yet verify the general two-morphism geometric composition array of Theorem 8.1 together with its exceptional-adjunction unit and counit. Those module comparisons, geometric nearby-cycle attaching maps and multiplicative descent, and the normalized coefficient and rational transports are additional hypotheses for that application. \(\square\)



### Geometric composition through compatible resolution arrays

**Proposition B.1r (composition with its resolutions still present).** In the full Noetherian unbounded ordinary torsion-ring scope of B.1e, the canonical composition map for compact supports is represented by the resolution-roof comparison below. Its proper-refinement comparisons, associative and unital composition comparisons, and base-change interchange agree on common resolved arrays, including the higher folding components. This does not select strictly functorial K-injective replacements or strict inverses to quasi-equivalences. The ordinary statement on the other domains of Compact support, Theorem 8.1 is preserved, not replaced by this enhanced assertion. No bounded-below, coefficient-flatness or finite-global-dimension restriction is introduced.

**The two-map geometry.** For \(X\xrightarrow{f}Y\xrightarrow{g}Z\), use the compatible compactification of that theorem. Thus \(f=hj\), \(g=qi\), \(gf=qpkj\), and the middle square is cartesian:
\[
\begin{matrix}
X&\xrightarrow{j}&U&\xrightarrow{k}&C\\
&&h\downarrow&&p\downarrow\\
&&Y&\xrightarrow{i}&D&\xrightarrow{q}&Z.
\end{matrix}
\qquad
\begin{gathered}
j,k,i\text{ open},\\h,p,q\text{ proper}.
\end{gathered}
\tag{B.GC1}
\]
Put \(J=j_!\), \(K=k_!\), \(L=i_!\), \(H=h_*\), \(P=p_*\), and \(Q=q_*\). The first three are exact; the last three preserve K-injectives. Write \(\epsilon:LH\to PK\) for the actual closed natural transformation of B.1n. In particular we do **not** regard \(H\) as exact or fold a replacement through it.

Let \(\mathcal C=\mathcal G_J\), with objects \(c=(I,B,s:JI\to B)\). The dg functor \(F=LH\rho_J\) on this base sends \(c\) to \(LHB\) and a homogeneous base map \((u,v,\alpha)\) to \(LHv\). Form the graph over the entire base \(\mathcal C\):
\[
\begin{aligned}
\mathcal L_{g,f}:\quad &(c,N,t:LHB\longrightarrow N),\\
&((u,v,\alpha),w,\delta),\qquad
\delta:LHB\longrightarrow N'[d-1],\\
\text{output}:\quad &(c,N,t)\longmapsto QN.
\end{aligned}
\tag{B.GC2}
\]
Here \(I,B,N\) are K-injective, \(s,t\) are quasi-isomorphisms, and the graph differential and signed composition are (B.CB4), with this \(F\). Forgetting \(N,t\) is a quasi-equivalence: its Hom kernel is the shifted cone for precomposition by \(t\), and all targets of that Hom comparison are K-injective. Every base object has a replacement. This proves the assertion over \(\mathcal C\), not by assuming that \(H\rho_J\) is an equivalence. Since \(HB\) is K-injective, the output computes \(Rg_!Rf_!\).

Use the exact two-open string \(\mathcal R(K,J)\), with object \((I,B,A;s,r:KB\to A)\) and map \((u,v,w;\alpha,\delta)\). Define
\[
\begin{aligned}
E(I,B,A;s,r)&=((I,B,s),PA,(Pr)\epsilon_B),\\
E(u,v,w;\alpha,\delta)&=((u,v,\alpha),Pw,(P\delta)\epsilon_B).
\end{aligned}
\tag{B.GC3}
\]
B.1n proves that the new replacement is a quasi-isomorphism and that the second line preserves the differential, signed composition and units. The first-stage map is unchanged. Both projections to \(\mathcal C\) are quasi-equivalences, so \(E\) is one, by Hom two-out-of-three and lifting the identity of a base object in \(H^0\). Its output is \(QPA\).

The other comparison is the higher fold of the **exact** opens \(J,K\):
\[
\mathcal L_{g,f}\xleftarrow{\ E\ }
\mathcal R(K,J)\xrightarrow{\ C_{K,J}\ }\mathcal G_{KJ},
\qquad QP\rho_{KJ}\text{ on the right}.
\tag{B.GC4}
\]
Use \(KJ\simeq(kj)_!\) and \(QP\simeq(qp)_*\), with their canonical composition identifications. The right output is a model of \(R(gf)_!\). The first folding component keeps the final vertex map \(w\), and every higher component has zero endpoint vertices. Consequently both outputs of (B.GC4) are the same strict output \(QPA\), while the nonzero higher homotopies are retained in the middle graph. The underlying exchange is the quasi-isomorphism \((Pr)\epsilon_B:LHB\to PA\). Apply **derived** \(Rq_*\) to it through the graph target \(N\): on the image of \(E\), that target is already \(PA\). For any other replacement \(t:LHB\to N\), BF.1 gives a comparison \(a:N\to PA\) and a homotopy \(at\simeq(Pr)\epsilon_B\). The map \(a\) is a quasi-isomorphism between K-injectives, hence a homotopy equivalence, so \(Qa\) is a homotopy equivalence. This supplies the required derived comparison independently of the choice of \(N\). Applying \(Q\) directly to the unresolved source \(LHB\) is not justified. The graph construction instead gives exactly the derived proper–open exchange in equation (8.3) of the ordinary theorem, with the preceding \(J\)-replacement retained.

**Changing both compactifications.** Write a refinement of the array as \(r:C'\to C\), \(s:D'\to D\), and \(t:U'\to U\). All are proper; they protect the copies of \(X,Y\), and
\(pr=sp'\), \(ht=h'\), \(qs=q'\). Put \(R=r_*\), \(S=s_*\), \(T=t_*\). The open functors above the refinement are \(J',K',L'\). There are closed natural exchanges
\(\kappa^j:J\to TJ'\), \(\epsilon^k:KT\to RK'\), and \(\kappa^i:L\to SL'\). The two vertical pastings of B.1n give the following identity before any replacement:
\[
(P\epsilon^k)(\epsilon T)
 =(S\epsilon')(\kappa^i H'):
 LH'\longrightarrow SP'K',
\qquad PR\simeq SP',\quad HT\simeq H'.
\tag{B.GC5}
\]
Indeed both sides are the exchange of the outer proper–open rectangle. Restriction to its bottom open identifies both with the same clopen-supported direct image, and open adjunction determines the whole natural map. This includes noncartesian refinement squares of the type already allowed in B.1n.

The top two-open string is transferred by
\[
\begin{aligned}
(I,B',A';s',r')&\longmapsto
 (I,TB',RA';(Ts')\kappa^j_I,(Rr')\epsilon^k_{B'}),\\
(u,v,w;\alpha,\delta)&\longmapsto
 (u,Tv,Rw;(T\alpha)\kappa^j_I,(R\delta)\epsilon^k_{B'}).
\end{aligned}
\tag{B.GC6}
\]
The object assertions are B.1m and B.1n; every target vertex remains K-injective. On the left graph (B.GC2), transfer its entire base by the first stage of (B.GC6), send \(N'\) to \(SN'\), and send its second edge or edge homotopy \(z\) to \((Sz)\kappa^i_{H'B'}\). These are dg functors by homogeneous naturality. Their projections keep the original \(I\), so the resulting comparison roofs remain quasi-equivalences over that original input.

Equation (B.GC5), followed by \(SP'r'\), identifies the two object edges obtained by applying \(E\) before or after refinement; replacing \(r'\) by \(\delta\) proves the identical assertion for the second edge homotopy. The other components already agree. On the right, (B.RS12) for the exchanges \(\kappa^j,\epsilon^k\) compares **every** folding coefficient, including its nonzero second coefficient. Thus the full comparison (B.GC4), not only its derived value, commutes with refinement. Successive refinements use the ordered exchange products, with the direct-image associators of B.1m.

The dense common-refinement construction in Theorem 8.1 supplies a common array for any two choices: first refine \(D\), then take the proper product for the \(C\)'s with the closed equations enforcing their maps to the refined targets, and take the schematic closure of \(X\). Over the protected open its graph is closed, hence this closure still contains that same open. Equation (3.2) identifies the inverse images of the protected \(Y\). Every comparison just proved therefore applies. Keep these common-refinement roofs; no selected quasi-inverse or purported strict identification of different choices is required.

**The three-map array and associativity.** For \(X\xrightarrow{f}Y\xrightarrow{g}Z\xrightarrow{h}W\), first compactify \(h\), then the composite from \(Y\) to that compactification, and finally the composite from \(X\) to the next compactification, as in Theorem 8.1. Taking inverse images of the opens gives this compatible array; \(X\xrightarrow{j}U\) is the remaining first open:
\[
\begin{matrix}
U&\xrightarrow{k}&T&\xrightarrow{\ell}&B\\
p_0\downarrow&&p_1\downarrow&&p_2\downarrow\\
Y&\xrightarrow{i}&V&\xrightarrow{m}&C\\
&&q_0\downarrow&&q_1\downarrow\\
&&Z&\xrightarrow{a}&D&\xrightarrow{r}&W.
\end{matrix}
\tag{B.GC7}
\]
All named horizontal arrows except \(r\) are open; all vertical arrows and \(r\) are proper. Every displayed elementary square is cartesian. More explicitly, \(V=q_1^{-1}(Z)\), \(T=p_2^{-1}(V)\), and \(U=p_2^{-1}(Y)\); the vertical arrows are their restrictions. Then \(f=p_0j\), \(g=q_0i\), and \(h=ra\).

Use \(J=j_!\), \(K=k_!\), \(L=\ell_!\), \(I=i_!\), \(M=m_!\), \(A=a_!\), \(H_b=p_{b,*}\), \(Q_b=q_{b,*}\), and \(R=r_*\). Here the letter \(I\) denotes the open functor only in this array; write \(I_0\) for an original K-injective input on \(X\). Its three exchanges and two relevant pasted exchanges are
\[
\begin{aligned}
\epsilon_1 &: IH_0\longrightarrow H_1K,&
\epsilon_2 &: MH_1\longrightarrow H_2L,&
\epsilon_3 &: AQ_0\longrightarrow Q_1M,\\
\epsilon_{23}&=(Q_1\epsilon_2)(\epsilon_3H_1),&
\epsilon_{21}&=(\epsilon_2K)(M\epsilon_1).
\end{aligned}
\tag{B.GC8}
\]
Before resolution, the two parenthesizations move the opens in
\(RAQ_0IH_0J\) to obtain \(RQ_1H_2LKJ\). After omitting the common outer \(R\) and final \(J\), their equality is
\[
\begin{aligned}
&(Q_1\epsilon_2K)(\epsilon_3H_1K)(AQ_0\epsilon_1)\\
&\hspace{1em}=(Q_1\epsilon_2K)(Q_1M\epsilon_1)(\epsilon_3IH_0).
\end{aligned}
\tag{B.GC9}
\]
The middle interchange is precisely naturality of \(\epsilon_3\) for the homogeneous map \(\epsilon_1\); the outer factors are unchanged. The vertical and horizontal pastings in (B.GC8) identify these with the two canonical composition routes. This calculation alone is not yet the resolved assertion.

For that assertion take the **single** three-open master graph \(\mathcal R(L,K,J)\), with K-injective vertices \(I_0,B_0,B_1,B_2\) and replacements \(s_0:JI_0\to B_0\), \(s_1:KB_0\to B_1\), \(s_2:LB_1\to B_2\). Its map to the iterated actual \(f,g,h\) graph retains \(s_0\) and uses
\[
\begin{aligned}
\gamma_1&=(H_1s_1)\epsilon_{1,B_0}:
 IH_0B_0\longrightarrow H_1B_1,\\
\gamma_2&=(Q_1H_2s_2)\epsilon_{23,B_1}:
 AQ_0H_1B_1\longrightarrow Q_1H_2B_2.
\end{aligned}
\tag{B.GC10}
\]
The first, second and third output stages are \(H_0B_0\), \(Q_0H_1B_1\), and \(RQ_1H_2B_2\). Every replacement in (B.GC10) is a quasi-isomorphism by the corresponding proper–open graph comparison. On homogeneous maps apply the same proper functors to the vertex maps, and in \(\gamma_b\) replace \(s_b\) by its edge homotopy. The proofs of (B.PO3) and (B.PO4) make this a dg functor.

Both the master graph and the iterated actual graph project by successive acyclic Hom-cone kernels to \(I_0\). Their comparison is therefore a quasi-equivalence over \(I_0\), just as in (B.GC3). In particular it is not being justified by the false claim that a proper direct image is a quasi-equivalence. Computing \(gf\) first uses the outer exchange \(\epsilon_{23}\) in (B.GC10). Computing \(hg\) first uses \(\epsilon_3\) after the middle replacement \((H_2s_2)\epsilon_2\); vertical pasting makes that edge **exactly** \(\gamma_2\), including its edge homotopy. The remaining difference is the parenthesization of the exact opens, not a fold across an unresolved \(H_b\) or \(Q_b\).

For that difference, transport each selected-edge word of B.1o through the proper–open array. Homogeneous naturality moves each closed degree-zero exchange to the outside, without permuting any homogeneous factor. Equations (B.RS9)–(B.RS12) give
\[
W_r^{\mathrm{bottom}}(Et_r,\ldots,Et_1)
 =P_{\mathrm{last}}W_r^{\mathrm{top}}(t_r,\ldots,t_1)
       \epsilon_{\mathrm{out}},
\qquad F_r^{\mathcal T}=F_r
\tag{B.GC11}
\]
on each horizontal row, for every arity \(r\) and every binary tree \(\mathcal T\). The source object in \(\epsilon_{\mathrm{out}}\) is the first input vertex, as in (B.RS12); \(P_{\mathrm{last}}\) is the proper image at the last vertex of that row. For object maps use \(W_0\); for the first coefficient also retain both endpoint maps. Higher endpoint maps are zero, not their graph homotopies. Thus (B.GC9) remains true for all resolved coefficients: vertical pasting handles \(\gamma_2\), horizontal wordwise transfer handles the folds, and both final outputs are \(RQ_1H_2B_2\). This proves associativity as comparison roofs on the common resolved array.

For any finite number of morphisms, construct the compatible triangular array successively from its last target. Use the exact-open master string along the top row and retain every proper-image stage. Each adjacent change of parentheses is the three-map calculation just given inside the larger array. More strongly, expanding any parenthesization yields the same selected-edge words by (B.GC11), so different sequences of those changes have the same coefficients. This proves the associativity polygons, including the pentagon; it does not merely connect parenthesizations by unrecorded isomorphisms. Refine two finite arrays from the last target backwards, imposing the same closed commutativity equations at each finite stage. Equation (B.GC5) at each elementary square and (B.GC11) on each row compare their coefficients. Identity morphisms use identity compactifications and the length-zero fold of B.1o. Its higher components vanish, giving the two unit comparisons and their compatibility with the associativity comparisons.

**Base change of a composition square.** In (B.GC1), pull back the middle square along \(b:D'\to D\). Denote the four inverse images by \(A_D,A_Y,A_C,A_U\), the pulled-back open and proper functors by \(L',K',H',P'\), the open-base-change isomorphisms by \(\theta_i:A_DL\to L'A_Y\), \(\theta_k:A_CK\to K'A_U\), and the underived proper-base-change maps by \(\beta_h:A_YH\to H'A_U\), \(\beta_p:A_DP\to P'A_C\). The precise mixed cube is
\[
(P'\theta_k)(\beta_pK)(A_D\epsilon)
 =(\epsilon'A_U)(L'\beta_h)(\theta_iH):
 A_DLH\longrightarrow P'K'A_U.
\tag{B.GC12}
\]
Identify the source with \(L'A_YH\) using \(\theta_i\), then use open adjunction. After restriction to \(Y'\), both sides are the unit-defined proper-base-change map \(\beta_h\), under the canonical open-restriction identifications. For a refinement square, the same assertion uses the clopen component of Lemma 6.1, which is preserved by pullback. Restricting the adjunction units in the definition of \(\beta_p\) gives exactly those defining \(\beta_h\); hence the equality is of actual sheaf maps. It extends termwise to complexes and is natural for every homogeneous map. This proves the cube before deriving either side.

Here is the resolved replacement calculation explicitly. Start with a K-injective \(B\) on \(U\), and choose \(s:KB\to C_0\) and \(t:A_CC_0\to D_0\) with K-injective targets. Put \(z=t(A_Cs)\theta_{k,B}^{-1}:K'A_UB\to D_0\). Naturality of \(\beta_p\) followed by (B.GC12) gives
\[
\begin{aligned}
&(P't)\beta_{p,C_0}\,A_D((Ps)\epsilon_B)\\
&\hspace{1em}=(P'z)\epsilon'_{A_UB}(L'\beta_{h,B})\theta_{i,HB}.
\end{aligned}
\tag{B.GC13}
\]
The left side is a quasi-isomorphism: the original proper–open comparison is one, \(A_D\) is exact, and B.1p applies to the K-injective \(C_0\) and its specified replacement \(t\). On the right, \(A_UB\) need not be K-injective, and we do not pretend that \(H'A_UB\) already computes its derived image. Instead compare the exact strings \(\mathcal R(A_C,K)\) and \(\mathcal R(K',A_U)\) through their common graph \(\mathcal G_{K'A_U}\), using \(\theta_k\), precisely as in (B.CB6). The second string has replacements \(u:A_UB\to B'\) and \(v:K'B'\to D'\). Its standard lower-route edge is
\((P'v)\epsilon'_{B'}L'((H'u)\beta_{h,B})\theta_{i,HB}\).
Naturality of \(\epsilon'\) turns this into the right side of (B.GC13) with \(z=v(K'u)\). It is a quasi-isomorphism by B.1p on \(B\) and B.1n on \(B'\). Every other common-graph replacement is related to one of these by the K-injective Hom-cone comparison; the resulting homotopy equivalences are preserved by \(P'\). This supplies the same graph over the original \(B\), without assigning an exactness property to \(P'\) or \(H'\).

Every graph transfer sends an edge or its homotopy to its proper image followed by the specified comparison. In (B.GC13), the two-edge fold supplies \(z=W_0\theta_k^{-1}\) on objects and \(W_r\theta_k^{-1}\) on its higher homogeneous components. Naturality of \(\beta_p\) and (B.GC12) apply to each such ordered word; the identical outer factors give the same transferred component. The first coefficient also retains its endpoint maps, and higher endpoint maps are zero. The vertex components have the canonical proper composition identifications of B.1p. Thus all the graph homotopy components, including the two-edge second coefficient, are compared; the bar signs are those of (B.RS8). This is an all-coefficient calculation, rather than an inference of equality from an \(H^0\) square.

Apply these local cubes to every square of the finite composition array. Vertical proper pasting is (B.BC6), successive base change uses (B.BC10), and the open replacements use (B.CB2)–(B.CB3). All folds occur in exact-open or exact-inverse-image blocks; the intervening proper-image stages stay in their shared-base graphs. The expanded comparisons therefore identify base change before composition with composition before base change, and refinement before either route with refinement after it. The outputs and all higher graph components agree on the common expanded models. No claim is made that independently chosen inverses to their projections commute strictly.

The composition arrays above give the comparisons for the stated ordinary compact-support theorem. They do not establish the full exceptional-adjunction unit and counit comparison with those arrays, geometric nearby attaching maps, multiplicative descent, whole normalized coefficient transport or strict-heart higher effacement. These are distinct hypotheses in applications to the general nearby-cycle system. □



### Module adjunctions on the common composition span

**Proposition B.1s (the strict span and its two mates).** Work over an arbitrary commutative coefficient ring, in the universe convention of [B.1k](#resolution-graphs-and-the-proper-support-mapping-bimodule). The common geometric span of B.1r has a module-adjunction comparison obtained from a strictly commuting square. We construct its two exchange maps, prove that their correctly resolved forms are quasi-isomorphisms, and give the actual unit and counit identities and comparison homotopies. No coefficient-flatness, finite-global-dimension or boundedness restriction is added. This supplies the strict-span part of the geometric adjunction comparison; transport through the higher folding in B.1r remains a separate construction.

**What a quasi-equivalence does to modules.** Let \(q:\mathcal A\to\mathcal B\) be a strict unital dg quasi-equivalence. Use right modules, balanced induction and the units and counits of [B.1l](#the-dg-module-adjunction-for-fixed-proper-support). Restriction \(q^*\) preserves objectwise quasi-isomorphisms. It also detects them: every object of \(\mathcal B\) is homotopy equivalent to a \(qA\), and any dg module sends such a homotopy equivalence to a homotopy equivalence of complexes.

For every h-projective \(P\), the actual module unit is an objectwise quasi-isomorphism:
\[
\eta^q_P:P\longrightarrow q^*q_!P,
\qquad x\longmapsto[x\otimes1_{qA}].
\tag{B.SM1}
\]
Here is a proof that does not assume flat Hom complexes. First take the semifree replacement constructed in B.1l. On a shifted representable cell, (B.SM1), evaluated at \(A'\), is the shift of \(\mathcal A(A',A)\to\mathcal B(qA',qA)\), a quasi-isomorphism. Each attachment is split as a sequence of graded modules; induction and restriction preserve that graded splitting. The long exact cohomology sequence therefore extends the assertion over each attachment stage. Direct sums and filtered unions of module complexes are exact degreewise, so it holds for the full, possibly unbounded semifree module. For an arbitrary h-projective \(P\), choose a semifree quasi-isomorphism \(S\to P\). Both ends are h-projective, hence this map is a homotopy equivalence by B.1l. Induction and restriction preserve that homotopy equivalence, and naturality proves (B.SM1) for \(P\). The proof uses the split cell filtration, not tensor-flatness of arbitrary modules.

For a module \(N\) over \(\mathcal B\), choose an h-projective replacement \(r:Q\to q^*N\). The resolved counit is
\[
e_N=\epsilon^q_Nq_!(r):q_!Q\longrightarrow N,
\qquad q^*(e_N)\eta^q_Q=r.
\tag{B.SM2}
\]
The second identity is the strict triangle identity and naturality of the unit, or direct evaluation of \([x\otimes1]\). Thus \(q^*e_N\) is a quasi-isomorphism by (B.SM1), and detection proves the same for \(e_N\). If \(N\) is h-projective, both ends of \(e_N\) are h-projective and it is a homotopy equivalence. These explicit maps prove that derived induction and restriction give inverse equivalences of the unbounded derived module categories. On homotopy-representable modules they give the corresponding equivalence of the dg models of B.1l, using its resolution graphs rather than selecting a strict inverse to \(q\).

When all h-projective modules are used below, use exactly (B.DA7)'s graph formula with those objects in place of its homotopy-representable subcategories. For any strict functor \(T\), objects are \((N,P,r:P\to T^*N)\), with both vertices h-projective and \(r\) a quasi-isomorphism. They exist by the semifree construction. The Hom kernel of projection to \(N\) is the shifted cone of postcomposition by the receiving replacement; it is acyclic because the source \(P\) is h-projective. The differential and composition are unchanged. Thus the projection remains a dg quasi-equivalence, and the same closed-map lifts and witnesses exist. No quasirepresentability assertion is required for this larger module graph; the geometric restriction back to homotopy-representable objects is checked below.

Restriction need **not** preserve h-projectivity. For example, over \(R=\mathbf Z/4\), let \(E\) be the exact complex \(R/2\xrightarrow{2}R\xrightarrow{\bmod 2}R/2\) in degrees \(0,1,2\), and give \(A=R\oplus E\) the square-zero dg-algebra extension. The inclusion \(R\to A\) is a one-object dg quasi-equivalence. The representable right \(A\)-module \(A\) is h-projective, but its restriction is not: the projection \(R\oplus E\to E\) would be null-homotopic if it were, which would contract \(E\). Such a contraction is impossible because an \(R\)-linear map \(R\to R/2\) sends \(2\) to zero and cannot split the first differential. This is why the replacements below cannot be omitted.

**The strictly commuting square.** Write
\[
\begin{matrix}
\mathcal A&\xrightarrow{\beta}&\mathcal C\\
\alpha\downarrow&&p\downarrow\\
\mathcal B&\xrightarrow{F}&\mathcal D,
\end{matrix}
\qquad p\beta=F\alpha,
\qquad \alpha,p\text{ dg quasi-equivalences}.
\tag{B.SM3}
\]
The horizontal functors need not be quasi-equivalences. For an \(\mathcal A\)-module \(L\), induction composition has a strict closed isomorphism
\[
\begin{aligned}
C_L:p_!\beta_!L\xrightarrow{\sim}F_!\alpha_!L,\\
&[[x\otimes a]\otimes v]\longmapsto
 [[x\otimes1_{\alpha A}]\otimes p(a)v],\\
C_L^{-1}:&[[x\otimes b]\otimes w]\longmapsto
 [[x\otimes1_{\beta A}]\otimes F(b)w].
\end{aligned}
\tag{B.SM4}
\]
In the forward formula \(x\in L(A)\), \(a:C\to\beta A\), \(v:D\to pC\); in the inverse \(b:B\to\alpha A\), \(w:D\to FB\). The inner balancing relation is carried to the other one by \(p\beta=F\alpha\). The outer relation is composition in \(\mathcal D\). Their two composites reduce to the original tensor by these relations. The differential agrees by the tensor Leibniz rule, with no permutation of factors. This proves a dg-module isomorphism for all modules, not merely a bijection on representables.

For arbitrary modules \(M\) over \(\mathcal B\) and \(N\) over \(\mathcal C\), define the two mates
\[
\begin{aligned}
b_M:\beta_!\alpha^*M&\longrightarrow p^*F_!M,
&[m\otimes a]&\longmapsto[m\otimes p(a)],\\
d_N:\alpha_!\beta^*N&\longrightarrow F^*p_!N,
&[n\otimes b]&\longmapsto[n\otimes F(b)].
\end{aligned}
\tag{B.SM5}
\]
The same commutative square proves balancing; these maps preserve right actions and the differential. They are natural for every homogeneous module map, not only for closed maps. In general they are not asserted to be quasi-isomorphisms before the appropriate replacements.

**The four identities before replacement.** With superscripts indicating the functor whose adjunction supplies a unit or counit, one has
\[
\begin{aligned}
b_{\alpha_!L}\,\beta_!(\eta^\alpha_L)
 &=p^*(C_L)\eta^p_{\beta_!L},\\
\epsilon^p_{F_!M}\,p_!(b_M)
 &=F_!(\epsilon^\alpha_M)C_{\alpha^*M}.
\end{aligned}
\tag{B.SM6}
\]
For the first identity, both sides send \([x\otimes a]\) to \([[x\otimes1]\otimes p(a)]\). For the second, a tensor \([[m\otimes a]\otimes v]\) is sent to \([m\otimes p(a)v]\); the expression through \(F_!\epsilon^\alpha\) reduces to it by balancing. Similarly,
\[
\begin{aligned}
d_{\beta_!L}\,\alpha_!(\eta^\beta_L)
 &=F^*(C_L^{-1})\eta^F_{\alpha_!L},\\
\epsilon^F_{p_!N}\,F_!(d_N)C_{\beta^*N}
 &=p_!(\epsilon^\beta_N).
\end{aligned}
\tag{B.SM7}
\]
The first formula sends \([x\otimes b]\) to \([[x\otimes1]\otimes F(b)]\). In the second, \([[n\otimes a]\otimes v]\) evaluates to \([n\otimes p(a)v]\) on both sides. Thus both mates and their directions are fixed by actual tensor evaluation. No uniqueness-of-adjoint argument replaces these identities.

**Why the resolved mates are equivalences.** Let \(M\) be h-projective, and choose \(s:Q\to\alpha^*M\) with \(Q\) h-projective. Put
\[
\begin{aligned}
\widetilde b&=b_M\beta_!(s):\beta_!Q\longrightarrow p^*F_!M,\\
e_M^\alpha&=\epsilon^\alpha_M\alpha_!(s),\\
z&=F_!(e_M^\alpha)C_Q:
p_!\beta_!Q\longrightarrow F_!M,\\
\widetilde b&=p^*(z)\eta^p_{\beta_!Q}.
\end{aligned}
\tag{B.SM8}
\]
The last identity follows by applying the formulas to \([q\otimes a]\). The map \(e_M^\alpha\) is a homotopy equivalence by (B.SM2); induction preserves it. Hence \(z\) is a homotopy equivalence. Since \(\beta_!Q\) is h-projective, (B.SM1) makes \(\widetilde b\) a quasi-isomorphism. This argument does not apply induction to a general unresolved quasi-isomorphism.

For h-projective \(N\), choose \(t:Q'\to\beta^*N\) with \(Q'\) h-projective. The other mate satisfies
\[
\begin{aligned}
\widetilde d&=d_N\alpha_!(t):\alpha_!Q'\longrightarrow F^*p_!N,\\
\alpha^*(\widetilde d)\eta^\alpha_{Q'}
 &=\beta^*(\eta^p_N)t.
\end{aligned}
\tag{B.SM9}
\]
Here the strict square identifies \(\alpha^*F^*\) with \(\beta^*p^*\). The right side and \(\eta^\alpha_{Q'}\) are quasi-isomorphisms, so detection by \(\alpha^*\) proves that \(\widetilde d\) is one. Again, \(\beta^*N\) and \(F^*p_!N\) have not been declared h-projective.

Choose a replacement \(r:P\to p^*F_!M\) with \(P\) h-projective. The Hom-complex quasi-isomorphism induced by \(r\) gives a closed lift \(u:\beta_!Q\to P\) and a degree-minus-one \(h\) with
\[
\begin{aligned}
ru-\widetilde b&=dh,\\
\epsilon^p_{F_!M}\,p_!(r)\,p_!(u)-z
 &=d\bigl(\epsilon^p_{F_!M}\,p_!(h)\bigr).
\end{aligned}
\tag{B.SM10}
\]
Both \(r\) and \(\widetilde b\) are quasi-isomorphisms, hence \(u\) is a quasi-isomorphism between h-projectives and therefore a homotopy equivalence. The second formula is the resolved counit identity, including its witness, obtained from (B.SM6).

For \(\widetilde d\), choose \(r':P'\to F^*p_!N\), lift it to \(u':\alpha_!Q'\to P'\), and retain \(r'u'-\widetilde d=dh'\). The other counit comparison is
\[
\begin{aligned}
&\epsilon^F_{p_!N}\,F_!(r')F_!(u')C_{Q'}
-p_!(\epsilon^\beta_N)\,p_!\beta_!(t)\\
&\qquad=d\bigl(\epsilon^F_{p_!N}\,F_!(h')C_{Q'}\bigr).
\end{aligned}
\tag{B.SM11}
\]
This is (B.SM7) and naturality of \(C\). The lift \(u'\) is a homotopy equivalence by the same argument. These are concrete comparison maps on the h-projective models.

The unit comparison also has an explicit four-term witness. Let \(L\) be h-projective, put \(M=\alpha_!L\), and choose replacements \(r_1:P_1\to\alpha^*\alpha_!L\), \(r_2:P_2\to p^*p_!\beta_!L\), \(r_3:P_3\to p^*F_!\alpha_!L\). Choose unit lifts \(u_1:L\to P_1\), \(u_2:\beta_!L\to P_2\) with \(r_1u_1-\eta^\alpha_L=d\ell_1\), \(r_2u_2-\eta^p_{\beta_!L}=d\ell_2\). Equation (B.SM10) supplies a closed \(a:\beta_!P_1\to P_3\) with \(r_3a-b_M\beta_!(r_1)=dh\). Lift \(C_L\) to a closed map of the right-resolution graph for \(p\), with components \((C_L,v,h_C)\), so \(r_3v-p^*(C_L)r_2=dh_C\). The first line of (B.SM6) gives
\[
\begin{aligned}
r_3\bigl(a\,\beta_!(u_1)-vu_2\bigr)&=dW,\\
W&=h\,\beta_!(u_1)+b_M\beta_!(\ell_1)\\
 &\quad-p^*(C_L)\ell_2-h_Cu_2.
\end{aligned}
\tag{B.SM12}
\]
Substitute the four defining equations; the remaining degree-zero terms cancel by (B.SM6), while the Leibniz rule gives precisely the four displayed terms. Since \(\beta_!L\) is h-projective, \(\operatorname{Hom}(\beta_!L,r_3)\) is a quasi-isomorphism. Injectivity on \(H^0\) shows that the closed unit defect is itself \(dH\), for a degree-minus-one \(H\). No assertion that \(r_3H=W\) is needed or made. For the first line of (B.SM7), the identical calculation uses \((\beta,\alpha,F,p,d,C^{-1})\) in place of \((\alpha,\beta,p,F,b,C)\); all the replacement sources and targets are obtained by that substitution. This proves the other resolved unit comparison without assuming that either horizontal functor is an equivalence.

Changed lift choices are handled in the same Hom complexes: if \(ra-b=dh\) and \(ra'-b=dh'\), then \(r(a-a')=d(h-h')\), so injectivity on \(H^0\operatorname{Hom}(K,r)\) supplies a homotopy between the closed maps \(a,a'\). For successive comparisons the witnesses compose by the Leibniz rule; for example \(ra-b=dh\), \(sb-c=dk\) give \(sr a-c=d(sh+k)\). The resolution graphs of B.1l retain these witnesses. Their strict module triangle identities and its explicit (B.DA11)–(B.DA12) still supply the triangles on each fixed model. This does not assert a coherently chosen system of all higher homotopies across the higher folding map.

**Identify the geometric consumer.** For \(X\xrightarrow fY\xrightarrow gZ\), use the actual B.1r graph \(\mathcal L_{g,f}\) of (B.GC2), not an unresolved proper-image complex. There are strict functors
\[
\begin{gathered}
\mathcal A=\mathcal L_{g,f},\quad
\mathcal B=\mathcal C_f,\quad
\mathcal C=\mathcal C_g,\quad
\mathcal D=\mathcal I_Y,\\
\alpha(c,N,t)=c,\qquad
\beta(c,N,t)=(F_fc,N,t),\qquad
p=\pi_g,\quad F=F_f,\\
\pi_g\beta=F_f\alpha,\qquad
\alpha,\pi_g\text{ dg quasi-equivalences},\qquad
F_g\beta(c,N,t)=QN.
\end{gathered}
\tag{B.SM13}
\]
On a homogeneous map \((v,w,\delta)\), the functor \(\beta\) uses \((F_fv,w,\delta)\). The graph differential and composition of (B.CB4) verify strictness, including the last component. The projection \(\alpha\) is a quasi-equivalence by the shared-base Hom-cone argument; \(\pi_g\) is one by B.1k. Neither \(F_f\) nor \(\beta\) is required to be a quasi-equivalence.

For example, start with an h-projective \(M\) on \(\mathcal C_f\). The sequential left model is \((F_g)_!P\), with \(P\to\pi_g^*(F_f)_!M\) an h-projective replacement. The common-span model is \((F_g\beta)_!Q\), with \(Q\to\alpha^*M\) an h-projective replacement. Equation (B.SM10) gives a homotopy equivalence between them after the induction-composition identification and application of \((F_g)_!\). Its counit compatibility is the displayed homotopy, and its unit compatibility is obtained as just specified from (B.SM6). Equation (B.SM9) gives the corresponding right-module comparison; the actual mate is \(d\), not an unspecified inverse on cohomology.

To return from \(\mathcal C_f\) to the source enhancement, retain the source projection \(\pi_f:\mathcal C_f\to\mathcal I_X\). For any strict span \(\mathcal I_X\xleftarrow{q}\mathcal C\xrightarrow{H}\mathcal I_Y\) with \(q\) a quasi-equivalence, (B.SM1)–(B.SM2) and the module adjunction give
\[
\mathbb L H_!\,q^*\ \dashv\ \mathbb L q_!\,H^*.
\tag{B.SM14}
\]
Here is the mapping-complex comparison explicitly. Choose h-projective \(M,N\) on the two endpoint categories and replacements \(P\to q^*M\), \(Q\to H^*N\), and write \(e_M:q_!P\to M\) for (B.SM2). There is a zigzag of actual Hom-complex quasi-isomorphisms
\[
\begin{aligned}
\operatorname{Hom}(H_!P,N)&\cong\operatorname{Hom}(P,H^*N)
\ \longleftarrow\ \operatorname{Hom}(P,Q),\\
\operatorname{Hom}(P,Q)&\longrightarrow
\operatorname{Hom}(P,q^*q_!Q)
\cong\operatorname{Hom}(q_!P,q_!Q),\\
\operatorname{Hom}(M,q_!Q)&\xrightarrow{\ -\circ e_M\ }
\operatorname{Hom}(q_!P,q_!Q).
\end{aligned}
\tag{B.SM15}
\]
The first arrow is postcomposition by the replacement of \(H^*N\); the middle one is postcomposition by \(\eta^q_Q\); both are quasi-isomorphisms because \(P\) is h-projective. The last arrow is a homotopy equivalence because \(e_M\) is. This proves (B.SM14) at the mapping-complex level. The inverse-equivalence adjunction \(q^*\dashv\mathbb Lq_!\) has unit the inverse of (B.SM2) and counit the inverse of (B.SM1), as roofs; no strict inverse replacement functor is selected. Its identities on representatives are (B.SM2) and the fixed-model triangle calculations of B.1l.

For the geometric common span, this also stays in the intended homotopy-representable models. If \(Y\) is homotopy-representable on \(\mathcal I_Z\), B.1k gives a homotopy-representable replacement \(N\to F_g^*Y\) on \(\mathcal C_g\). Then \((\pi_g)_!N\) is homotopy-representable, and B.1k gives the same property for a replacement of \(F_f^*(\pi_g)_!N\). Equation (B.SM9), and the equivalence induced by \(\alpha\), imply that a replacement of \(\beta^*N\) is homotopy-representable. Restriction preserves the quasi-isomorphism to \(\beta^*F_g^*Y\). This checks the right mapping module for \(F_g\beta\); it does not assume that restriction along the nonequivalence \(\beta\) preserves all representables. Thus the comparison concerns the same geometric operations, not a substitute theory on unrelated modules.

The construction gives the strict common span and both module mates needed by B.1r. Comparison with the single-compactification model uses the higher exact-string fold of B.1o. That fold is not a strict dg functor, so the balanced induction formulas cannot be applied directly to it. Higher-functor module transport requires coherent units, counits and triangle comparisons across the geometric composition, base-change and refinement grids. These fixed-span calculations do not establish geometric nearby attaching maps, multiplicative descent or normalized coefficient transport at their full stated geometric and coefficient scope. \(\square\)



### Strict dg roofs for higher folding

**Proposition B.1t (retain the higher map before inducing modules).** The strictly unital higher folding map of [B.1o](#all-length-resolution-folding-and-its-higher-components) has a common strict dg source with quasi-equivalent maps to its string and folded models. Both endpoint projections agree strictly on this source. The construction works over an arbitrary commutative coefficient ring and for unbounded Hom complexes. It respects the strict outer transfers of B.1o and the identical coefficients of all parenthesizations. Consequently the fixed-roof module comparisons of B.1m and B.1s apply to folding. We construct the source and its contraction explicitly; no flatness or splitting of the original category's units is assumed.

**First make the units freely split.** Work in the larger universe already used for B.1k, so the objects and all arrow labels below form sets. For a unital linear dg category \(\mathcal A\), construct a dg category \(Q\mathcal A\) with the same objects and a strict functor \(q:Q\mathcal A\to\mathcal A\). Start with the free graded category on a closed arrow \(c_z:X\to Y\), of degree \(|z|\), for every homogeneous cycle \(z\in\mathcal A(X,Y)\), and send \(c_z\) to \(z\). The label includes both objects and the specified degree, including for the zero cycle. These are formal generators, including when \(z=0\) or \(z=1_X\); the actual identity in the free category is a separate empty path.

At stage \(n+1\), for every homogeneous cycle \(z\in Q_n\mathcal A(X,Y)^r\) and every \(m\in\mathcal A(X,Y)^{r-1}\) with \(qz=dm\), adjoin a generator
\[
e_{n,z,m}:X\longrightarrow Y,
\qquad |e_{n,z,m}|=r-1,
\qquad de_{n,z,m}=z,
\qquad q(e_{n,z,m})=m.
\tag{B.SF1}
\]
Extend the differential by the graded Leibniz rule, and take the union of these stages. Its square vanishes on every generator, hence on every path. The map \(q\) is surjective on each Hom cohomology group because every target cycle has an initial generator. If a cycle in the union maps to a boundary, its expression uses finitely many generators and therefore lies at some stage; (B.SF1) kills its class at the next stage. Thus \(q\) is a Hom quasi-isomorphism, and it is a dg quasi-equivalence because it is the identity on objects.

Every underlying graded Hom module is free on paths. In particular the identity at an object is a direct summand, with the nonempty paths as a specified complement. This remains true when the original identity is zero or torsion. For example, if its image is zero, the next stage can have \(de=1\); the free graded identity has not been identified with zero. The complement need not be a subcomplex, and no such assertion will be used.

The construction is functorial for strict unital dg functors \(P:\mathcal A\to\mathcal A'\). Send \(c_z\) to \(c_{Pz}\), and send the stage-\(n+1\) generator to \(e_{n,Q_nP(z),P(m)}\). Its differential and image satisfy the same equation. This preserves the stage labels, nonempty paths, identities, and composition of functors exactly. In particular \(q'QP=Pq\). No choice of representatives or null-homotopies was required: all the stated labels were adjoined.

**The normalized word category.** Let \(\mathcal D\) now be a dg category whose identities are split as graded modules; we will use \(\mathcal D=Q\mathcal A\). Before normalization take the free unital graded category on multilinear symbols
\[
[t_r|\cdots|t_1],
\qquad |[t_r|\cdots|t_1]|=\sum_{i=1}^r|t_i|+1-r,
\qquad r\geq1,
\tag{B.SF2}
\]
for composable homogeneous arrows. Impose \([1_X]=1_X\) and declare every symbol of length at least two with an identity input to be zero. Thus the underlying graded category \(U\mathcal D\) is free on positive-length tensors of the quotients by the identity lines, with the identities themselves retained separately. This description uses a graded splitting only; the quotient by the identity line is a complex because \(d1=0\).

For \(d_i=|t_i|\), put \(p_i=\sum_{a=i+1}^r(d_a-1)\) and \(e_k=\sum_{a=k+1}^r d_a+1-(r-k)\). Define the differential on generators by
\[
\begin{aligned}
d[t_r|\cdots|t_1]
&=\sum_{i=1}^r(-1)^{p_i}
 [t_r|\cdots|dt_i|\cdots|t_1]\\
&\quad+\sum_{k=1}^{r-1}(-1)^{e_k}
 [t_r|\cdots|t_{k+1}][t_k|\cdots|t_1]\\
&\quad+\sum_{i=1}^{r-1}(-1)^{p_{i+1}+d_{i+1}+1}
 [t_r|\cdots|t_{i+1}t_i|\cdots|t_1].
\end{aligned}
\tag{B.SF3}
\]
Extend by the graded Leibniz rule to products of generators. These are exactly the signs of (B.RS8), solved for the differential of its Taylor coefficient. For instance
\(d[u|t]=[du|t]+(-1)^{|u|-1}[u|dt]+(-1)^{|u|}([u][t]-[ut])\).

Here are the dg and normalization checks. On the unnormalized tensor cocategory use the coderivation \(b\) of (B.RS7). If \(w\) is a suspended word and \(\gamma(w)\) denotes its degree-one desuspension, (B.SF3) says
\[
d\gamma(w)=-\gamma(bw)
 +\sum_{w=uv}(-1)^{|u|+1}\gamma(u)\gamma(v),
\qquad |\gamma(u)|=|u|+1.
\tag{B.SF4}
\]
Splits are into two nonempty consecutive words. Applying \(d\) again, the linear part is \(\gamma(b^2w)=0\). The terms with one \(b\) and one split cancel by the coderivation identity: applying \(b\) in the right part contributes \((-1)^{|u|}\), while applying the derivation after the left desuspension contributes \((-1)^{|u|+1}\). In the terms with two splits, each ordered three-block word occurs twice. Splitting its left pair first gives sign \((-1)^{|v|}\), and splitting its right pair first gives \((-1)^{|v|+1}\), where \(v\) is the middle suspended block. They cancel. This proves \(d^2=0\).

The normalization relations form a differential ideal. A unit has zero differential. For a length-two symbol with a unit input, its split term and its merged term cancel, including when both inputs are units. In a longer word an interior unit can survive normalization only in the two adjacent merges; their exponents in (B.SF3) differ by one. At an end, the only possibly surviving merge cancels the split that isolates that unit as a one-input block. Terms retaining a unit in a longer block vanish. The same reasoning covers additional unit inputs, since the remaining word then also normalizes to zero. Thus (B.SF3) is well defined after normalization, even when differentiating a nonunit arrow produces a scalar identity.

**An explicit finite-word contraction.** There is a strict functor \(\epsilon:U\mathcal D\to\mathcal D\), identical on objects, sending \([t]\) to \(t\) and longer generators to zero. It is a chain map: the two length-two product terms have the same image and opposite signs, and every term of a longer differential maps to zero. There is also a linear chain section \(j(t)=[t]\), with \(\epsilon j=1\). It is not a multiplicative section.

Filter each Hom complex of \(U\mathcal D\) by the total number of input letters in a product of generators. The identity has length zero. Internal differentials preserve length or decrease it through identity components; a merge decreases length; a split preserves length. The length-at-most-one subcomplex is exactly \(j\mathcal D\), including the identity terms in its differential.

We exhibit a contraction of every associated graded piece of length \(n\geq2\). For this paragraph number the inputs **from left to right** as \(x_1,\ldots,x_n\), with degrees \(d_i\), and let \(S\subseteq\{1,\ldots,n-1\}\) be the set of cuts between blocks. Write \(E_S(x_1,\ldots,x_n)\) for the corresponding product of bracket generators. Its degree is \(\sum_i(d_i-1)+|S|+1\). Put \(A_j=\sum_{i=1}^j(d_i-1)\). The length-preserving split differential and the quotient internal differential are
\[
\begin{aligned}
\delta E_S
 &=\sum_{j\notin S}(-1)^{A_j+|S\cap\{1,\ldots,j-1\}|+1}
 E_{S\cup\{j\}},\\
d_0 E_S
 &=\sum_{i=1}^n(-1)^{A_{i-1}+|S\cap\{1,\ldots,i-1\}|}
 E_S(x_1,\ldots,\overline d x_i,\ldots,x_n).
\end{aligned}
\tag{B.SF5}
\]
The omitted entries in the first line are unchanged. Here \(\overline d\) is the differential modulo identity lines; it is well defined without choosing a chain splitting. The signs follow by adding the degrees of whole blocks to the left to the within-block signs of (B.SF3).

Contract by removing the first cut:
\[
hE_S=
\begin{cases}
(-1)^{d_1}E_{S\setminus\{1\}},&1\in S,\\
0,&1\notin S,
\end{cases}
\qquad
(d_0+\delta)h+h(d_0+\delta)=1.
\tag{B.SF6}
\]
For \(\delta h+h\delta\), toggling the first cut contributes the identity because its coefficient is \((-1)^{d_1}\) in both directions. Every other cut appears twice with opposite signs: removing the first cut changes the number of cuts to its left by one. For \(d_0h+hd_0\), differentiating \(x_1\) changes the sign of \(h\), and differentiating any later input changes the internal sign when the first cut is removed. These terms therefore cancel as well. This proves (B.SF6) on tensors, with arbitrary coefficients; no tensor exactness is invoked.

For clarity, at three inputs the four block patterns are
\( [x_1|x_2|x_3], [x_1][x_2|x_3], [x_1|x_2][x_3], [x_1][x_2][x_3] \).
The contraction pairs the first two and the last two by deleting the same first cut. The second-cut differential has opposite signs on the two sides of each pair, as (B.SF5) specifies. This is the mechanism of the contraction, not a numerical approximation.

Every element has finite word length. A cycle in the quotient by \(j\mathcal D\) has some largest length \(n\); applying (B.SF6) to its highest part and subtracting the resulting boundary reduces that largest length. Repeating finitely many times proves that the quotient is acyclic. Hence \(\epsilon\) is a Hom quasi-isomorphism and a dg quasi-equivalence. This finite reduction works for completely unbounded complexes. In particular it is not a convergence assertion for an infinite spectral sequence, nor a claim that uncorrected bar tensors compute derived tensor products. For a nonflat example the same contraction works over \(R=\mathbf Z/4\) for \(R\oplus(R/2)e\) with \(e^2=0\); its positive-length quotient tensors are not flat over \(R\).

The word construction is functorial for strict unital dg functors, by applying the functor to every input. The differential and the normalization relations are preserved. This statement uses the quotient definition; it does not require the functor to preserve a chosen complement of the identity.

**Extend the actual higher fold.** More generally let \(K:\mathcal A\to\mathcal B\) be a strictly unital higher functor in the precise suspension convention (B.RS7)–(B.RS8). Suppose \(K_1\) is a Hom quasi-isomorphism and its object map is essentially surjective on \(H^0\). Set \(\mathcal W_{\mathcal A}=UQ\mathcal A\). Its two strict arrows are
\[
\begin{gathered}
\mathcal A\xleftarrow[e_{\mathcal A}=q\epsilon]{\sim}
\mathcal W_{\mathcal A}
\xrightarrow[h_K]{\sim}\mathcal B,\\
h_K[x_r|\cdots|x_1]=K_r(qx_r,\ldots,qx_1).
\end{gathered}
\tag{B.SF7}
\]
Strict unitality makes this formula respect the normalization relations. Equation (B.RS8) is exactly the assertion that it commutes with (B.SF3), and extension over products makes it a strict dg functor. Its composite with the linear chain section \(j:Q\mathcal A\to UQ\mathcal A\) is \(K_1q\). Since \(j,q,K_1\) are Hom quasi-isomorphisms, so is \(h_K\). Essential surjectivity is that of \(K\). This proves both labels \(\sim\) in the diagram; it does not replace a higher coefficient by zero.

If strict endpoint functors \(b:\mathcal A\to\mathcal E\) and \(c:\mathcal B\to\mathcal E\) satisfy \(cK_1=b\) and \(cK_r=0\) for \(r\geq2\), then
\[
c h_K=b e_{\mathcal A}
\quad\text{as strict dg functors.}
\tag{B.SF8}
\]
This is equality on each bracket generator, including the higher ones, hence on all products. Apply it separately to the first and final vertex projections of B.1o, and then to any stipulated strict proper-output functor. The resulting roof therefore compares the actual geometric operations, not merely their unlabelled Hom categories.

For a strictly commuting outer diagram with strict functors \(P:\mathcal A\to\mathcal A'\), \(V:\mathcal B\to\mathcal B'\) and \(VK_r=K'_r(P-,\ldots,P-)\) in every arity, functoriality and evaluation on generators give
\[
e_{\mathcal A'}\,UQP=P e_{\mathcal A},
\qquad h_{K'}\,UQP=V h_K.
\tag{B.SF9}
\]
In particular (B.RS12) supplies this equality for the proper–open transfers. The exact parenthesization equality (B.RS10) gives the very same \(h_K\) from a fixed master string for every tree; its associativity polygons commute strictly on this roof. The geometric master arrays and refinement/base-change transfers of B.1r can now use these strict arrows wherever their coefficient comparisons were established. We have used functoriality of \(Q\) only on **strict** outer functors, not posited a lift of an arbitrary higher functor through \(Q\).

**Apply the existing module adjunctions to strict maps only.** For either roof arrow \(d:\mathcal W\to\mathcal C\), let the proper-output functors satisfy \(F_{\mathcal C}d=F_{\mathcal W}\). Write \(S=d_!\), \(T_{\mathcal W}=(F_{\mathcal W})_!\), \(T_{\mathcal C}=(F_{\mathcal C})_!\), and \(U_{\mathcal W},U_{\mathcal C}\) for restriction along the two outputs. The strict output identification gives the actual balanced maps
\[
\begin{aligned}
c_P:T_{\mathcal C}SP&\longrightarrow T_{\mathcal W}P,
&[[x\otimes a]\otimes v]&\longmapsto[x\otimes F_{\mathcal C}(a)v],\\
k_N:SU_{\mathcal W}N&\longrightarrow U_{\mathcal C}N,
&[n\otimes a]&\longmapsto nF_{\mathcal C}(a).
\end{aligned}
\tag{B.SF10}
\]
These are precisely (B.CR6)–(B.CR9) with the closed output isomorphism equal to the identity. In particular \(c\) is an isomorphism, and the tensor identities there prove compatibility with the actual units and counits, not only their classes. All tensor factors keep their order.

For replacements \(r_{\mathcal W}:P_{\mathcal W}\to U_{\mathcal W}N\), \(r_{\mathcal C}:P_{\mathcal C}\to U_{\mathcal C}N\), retain a closed map \(a:SP_{\mathcal W}\to P_{\mathcal C}\) and degree-minus-one witness \(b\) with \(r_{\mathcal C}a-k_NS(r_{\mathcal W})=db\), exactly as in B.1m. Their existence uses the Hom quasi-isomorphism out of the h-projective \(SP_{\mathcal W}\). Since \(d\) is a quasi-equivalence, (B.SM2) applied to the replacement of \(d^*U_{\mathcal C}N\) makes \(k_NS(r_{\mathcal W})\) a quasi-isomorphism. Thus \(a\) is a homotopy equivalence between h-projectives. If \(E_{\mathcal W},E_{\mathcal C}\) denote the resolved counits, the actual comparison is
\[
E_{\mathcal C}T_{\mathcal C}(a)-E_{\mathcal W}c_{P_{\mathcal W}}
=d\bigl(\epsilon^{F_{\mathcal C}}_N T_{\mathcal C}(b)\bigr).
\tag{B.SF11}
\]
The resolved unit comparison is the four-term Hom-complex calculation (B.CR11), or (B.SM12) in the strict-square form. The fixed-model triangles remain the explicit (B.DA11)–(B.DA12). The source endpoint equality (B.SF8), the inverse module equivalence (B.SM1)–(B.SM2), and the mapping-complex zigzag (B.SM15) identify these with the adjunctions on the same endpoint enhancements. Quasi-equivalences preserve and reflect homotopy-representable modules through those equivalences; no assertion that unresolved restriction preserves h-projectivity is inserted.

For **fixed-roof** module induction, the construction gives both strict quasi-equivalences, the endpoint equalities, the balanced comparisons and their resolved witnesses. The strict outer diagrams (B.SF9) and identical parenthesization maps are available for the remaining global assembly. Choosing individual resolution lifts and homotopies independently does not automatically specify a coherent system of higher homotopies on that entire diagram. That assembly, the full enhanced geometric adjunction comparison, nearby attaching and multiplicative descent, normalized coefficient transport are additional geometric requirements. \(\square\)



### Natural diagram resolutions and relative coherent lifts

**Proposition B.1u (naturality is part of the resolution problem).** The strict folding roofs of [B.1t](#strict-dg-roofs-for-higher-folding) admit module comparisons natural in an arbitrary dg-indexed family after replacing its index by the free dg model and resolving the **whole diagram**. The required tensor quasi-equivalences, objectwise h-projectivity and natural Hom-complex lifts are proved below over the original arbitrary commutative ring. Resolution-graph projections then lift prescribed relative free dg diagrams, including their higher cells. This supplies a natural lifting construction for the geometric assembly; it is not a claim that all of that assembly's index changes and boundaries have already been specified.

**Why pointwise resolutions do not suffice.** Over a field \(k\), put \(A=k[\varepsilon]/(\varepsilon^2)\). Regard an \(A\)-module as a diagram indexed by the one-object degree-zero dg category \(A\). The trivial module \(k\) is projective as a \(k\)-vector space, but not h-projective as an indexed diagram. Indeed the complex
\[
E:\quad k\xrightarrow{\ 1\mapsto\varepsilon\ }A
\xrightarrow{\ a+b\varepsilon\mapsto a\ }k
\quad\text{in degrees }0,1,2
\tag{B.ND1}
\]
is exact. In \(\operatorname{Hom}_A(k,E)\), the first map is an isomorphism onto \(k\varepsilon\), whereas the second is zero; its degree-two cohomology is \(k\). Thus pointwise h-projectivity cannot be substituted for h-projectivity in the complex of natural transformations. The replacement below addresses this exact distinction.

**The free index has h-projective and K-flat Hom complexes.** Let \(\mathcal I\) be a dg category over \(k\), in the existing universe convention, and write \(\mathcal J=Q\mathcal I\) for (B.SF1)'s free dg model. Here \(Q\) is that free-category construction, not the homotopy-representable module notation \(\mathcal Q\). Give an initial closed generator stage zero and a generator adjoined at step \(n\) stage \(n\). A path has finitely many generators. If \(c_n\) counts its stage-\(n\) generators, order its weight by the ordinal
\[
w=\omega^N c_N+\cdots+\omega c_1+c_0,
\qquad w(1_X)=0.
\tag{B.ND2}
\]
Replacing any stage-\(n\) generator by its differential replaces it by a finite sum of paths with strictly smaller stages. Each resulting path therefore has smaller weight, even if it has more arrows. Initial generators and identities have zero differential. The path basis of each Hom complex consequently has a well-founded filtration, with graded-split attachments and quotients direct sums of shifts of \(k\).

The generatorwise null-homotopy argument of B.1l works along this ordinal filtration: after values on smaller weights are fixed, the equation on the next basis vector has a cycle as its right side, and an acyclic target supplies its primitive. Limit stages retain all earlier values; every input is a finite sum of paths. This proves h-projectivity of each \(\mathcal J(i,j)\) as a complex of \(k\)-modules, with no bound on its degrees. It also proves K-flatness directly: tensor the graded-split filtration with an acyclic complex. Each successive quotient is a direct sum of shifts of that complex, hence acyclic; exact sequences and the increasing unions preserve acyclicity. At a union a cycle and any finite equation involving it already occur at a stage, so no inverse-limit or spectral-sequence convergence assertion is being used.

It follows that a strict dg quasi-equivalence \(f:\mathcal C\to\mathcal D\) induces one after adjoining this index:
\[
\widehat f=1_{\mathcal J^{\mathrm{op}}}\otimes f:
\mathcal J^{\mathrm{op}}\otimes\mathcal C
\longrightarrow\mathcal J^{\mathrm{op}}\otimes\mathcal D.
\tag{B.ND3}
\]
On each Hom complex its map is a Hom quasi-isomorphism of \(f\) tensored with \(\mathcal J(j,i)\); the cone is acyclic by the just-proved K-flatness. Essential surjectivity follows by taking the identity at \(i\) tensored with the closed degree-zero equivalences and homotopies supplied by \(H^0f\). This is why the free index is used. No analogous tensor-invariance assertion is made for an arbitrary nonflat index. In particular this does not assert that \(q\otimes1_{\mathcal C}\) is a quasi-equivalence when the Hom complexes of \(\mathcal C\) are nonflat; comparison of changes in the original index requires its own justification.

**Diagram modules and all signs.** Use the usual dg opposite and tensor conventions: opposite composition of homogeneous \(a,b\) has factor \((-1)^{|a||b|}\), and composition of \(a'\otimes b'\) with \(a\otimes b\) has factor \((-1)^{|b'||a|}\). A covariant dg diagram \(M:\mathcal J\to\mathrm{dgMod}(\mathcal C)\) is equivalently a right module \(\widetilde M\) over \(\mathcal E=\mathcal J^{\mathrm{op}}\otimes\mathcal C\). Set \(\widetilde M(i,X)=M_i(X)\). For \(a:i\to j\), \(b:Y\to X\), and homogeneous \(p\in M_i(X)\), the correspondence is
\[
\begin{aligned}
p\,(a^{\mathrm{op}}\otimes b)
 &=(-1)^{|a||p|}M(a)(p)b,\\
M(a)(p)&=(-1)^{|a||p|}
 p\,(a^{\mathrm{op}}\otimes1_X),\\
t_jM(a)&=(-1)^{|t||a|}M'(a)t_i.
\end{aligned}
\tag{B.ND4}
\]
The last line is the naturality condition corresponding to a homogeneous right \(\mathcal E\)-module map \(t\). For completeness, in the second line's Hom differential the two terms involving \(dp\) cancel; the remaining term has sign \((-1)^{(|a|+1)|p|}\), giving \(M(da)\). For two consecutive arrows the two occurrences of \((-1)^{|a||b|}\), one from the opposite composition and one from passing the degree of the first arrow through the second action, cancel. Moving a \(\mathcal C\)-action past the index action uses the tensor sign and gives an ordinary right-linear homogeneous module map. Applying the same computation to \(t\) gives the third line. These verifications identify both the actions and the Hom differentials, so
\(\operatorname{Hom}_{\mathcal E}(\widetilde M,\widetilde N)\)
is the full complex of graded natural transformations, not just degree-zero pointwise maps.

Apply the many-object semifree construction (B.DA2) to \(\widetilde M\), obtaining a whole-diagram quasi-isomorphism \(r:P\to\widetilde M\) with \(P\) semifree over \(\mathcal E\). It gives a strict dg diagram \(i\mapsto P_i\) and a closed natural map. Its defining commutative square, for every homogeneous \(a\), is
\[
\begin{array}{ccc}
P_i&\xrightarrow{\ P(a)\ }&P_j\\
{r_i}\downarrow&&\downarrow{r_j}\\
M_i&\xrightarrow{\ M(a)\ }&M_j.
\end{array}
\tag{B.ND5}
\]
The horizontal maps have degree \(|a|\), the vertical maps degree zero. Thus this is an equality of homogeneous module maps, not only a square in the homotopy category. Arbitrary diagrams on \(\mathcal I\) are first pulled back along \(q:\mathcal J\to\mathcal I\).

The diagram is resolved on \(\mathcal J\); the roof through \(q\) retains its homotopy-coherent relation to the original index. A strict resolution functor on \(\mathcal I\) has not been silently asserted. Every \(P_i\) is h-projective over \(\mathcal C\), as must be checked separately. A representable \(\mathcal E\)-cell at \((j,X)\), evaluated at \(i\), is
\[
\mathcal E((i,-),(j,X))
=\mathcal J(j,i)\otimes_k\mathcal C(-,X).
\tag{B.ND6}
\]
Using the path basis of \(\mathcal J(j,i)\), this is a free graded \(\mathcal C\)-module on shifted representables. For a whole-diagram cell of stage \(n\) and a path of weight \(w\), order its evaluated generators lexicographically by \((n,w)\), with \(n\) first. Differentiating the path decreases \(w\). Differentiating the diagram-cell generator lands in earlier cell stages, possibly multiplied by longer index paths, so decreases \(n\) regardless of their weights. This is a well-founded semifree filtration over \(\mathcal C\). The same transfinite null-homotopy argument proves h-projectivity. The argument for an arbitrary h-projective \(\mathcal E\)-module follows by replacing it by a semifree one: that quasi-isomorphism is a homotopy equivalence over \(\mathcal E\), and evaluation preserves the homotopy. In particular an h-projective diagram replacement is also an admissible replacement at every geometric module object.

For the fixed geometric right mapping module, take \(\mathcal I=\mathcal Q(\mathcal D)\) and the diagram given by restriction along \(F\). B.1k proves each value quasi-representable. Each \(P_i\) is h-projective and quasi-isomorphic to that value, hence homotopy equivalent to its representable by B.1l's Hom-lifting argument. Thus \(P\) actually gives a strict dg functor from \(Q\mathcal Q(\mathcal D)\) into \(\mathcal Q(\mathcal C)\), not just into an unrelated category of all modules. Its left roof arrow is the free index quasi-equivalence. Unit comparisons still require the whole input diagrams to be resolved where the following Hom argument is used.

**Lifting naturally, rather than object by object.** If \(P\) is h-projective over \(\mathcal E\) and \(r:N\to N'\) is an objectwise quasi-isomorphism, then
\[
\operatorname{Hom}_{\mathcal E}(P,N)
\xrightarrow{\ r\circ-\ }
\operatorname{Hom}_{\mathcal E}(P,N')
\quad\text{is a quasi-isomorphism.}
\tag{B.ND7}
\]
Its cone is the Hom complex into the objectwise acyclic cone of \(r\). Thus a closed natural map \(z:P\to N'\) of any degree lifts to a closed natural map \(a:P\to N\), together with a graded natural witness \(ra-z=dh\). Differences of closed lifts with the same cohomology image are themselves boundaries in the natural Hom complex. This conclusion uses h-projectivity of the whole diagram, not merely of the evaluated modules; (B.ND1) explains why the distinction is necessary.

For a strict functor \(F:\mathcal C\to\mathcal D\), restriction along \(\widehat F=1\otimes F\) is pointwise restriction. Induction along it is canonically pointwise induction. On balanced tensors its identification and inverse are
\[
\begin{aligned}
{}[p\otimes(a^{\mathrm{op}}\otimes v)]
 &\longmapsto[p(a^{\mathrm{op}}\otimes1)\otimes v],\\
[z\otimes v]&\longmapsto[z\otimes(1_i^{\mathrm{op}}\otimes v)].
\end{aligned}
\tag{B.ND8}
\]
In the first line \(p\) is at index \(j\), \(a:j\to i\), and \(v:Y\to FX\); the result is evaluated at \((i,Y)\). The equality
\(a^{\mathrm{op}}\otimes v=(a^{\mathrm{op}}\otimes1)(1_i^{\mathrm{op}}\otimes v)\)
and the balancing relation give both inverse identities. The dg actions prove that these are chain maps; expressing the first action through \(M(a)\) introduces exactly (B.ND4)'s sign. The units and counits are therefore the pointwise tensors of (B.DA5), now as closed maps of entire diagrams. The Hom adjunction proves that this induction preserves h-projectivity over the full index-product category.

Replace every category and strict functor in B.1s's square by its product with \(\mathcal J^{\mathrm{op}}\). The square still commutes strictly. Its two vertical quasi-equivalences remain quasi-equivalences by (B.ND3). Therefore (B.SM4)–(B.SM12) apply verbatim to these product categories: both balanced mates, their four strict unit/counit identities, both resolved quasi-isomorphisms and the actual unit/counit witnesses are obtained **in the natural-transformation complexes**. Equations (B.ND4) and (B.ND8) identify their evaluations with the geometric formulas already constructed. The same substitution applies to either strict folding-roof arrow in (B.SF7), so (B.SF10)–(B.SF11) and the fixed-model triangle witnesses can be made natural on the entire replaced parameter diagram. The input diagrams must be h-projective over the product category where those proofs require h-projectivity; resolving only their values would not justify this substitution.

**Lifting a whole relative free dg diagram.** The following elementary lifting statement gives the higher-cell step. Let \(\pi:\mathcal V\to\mathcal B\) be a dg functor that is degreewise surjective and a quasi-isomorphism on every Hom complex between the chosen objects. Its Hom kernels are acyclic: the degreewise short exact sequence of complexes and its cohomology sequence show this. Let \(\mathcal K\) be obtained from a dg subcategory \(\mathcal K_0\) by freely adjoining homogeneous arrows in a well-founded order, with the differential of each arrow in the earlier subcategory. Suppose a strict functor \(T:\mathcal K\to\mathcal B\), object lifts, and a compatible strict lift on \(\mathcal K_0\) have been fixed.

To extend the lift across a generator \(x\) of degree \(r\), choose a graded lift \(x_0\) of \(T(x)\). If \(L\) is the lift already constructed, its defect and correction are
\[
\begin{aligned}
\theta&=dx_0-L(dx)\in\ker\pi,\qquad d\theta=0,\\
dy&=\theta\quad(y\in(\ker\pi)^r),\\
L(x)&=x_0-y.
\end{aligned}
\tag{B.ND9}
\]
The kernel assertion follows from \(dT(x)=T(dx)\); closedness follows from \(d^2x=0\) and the established chain property on earlier arrows. Acyclicity supplies \(y\). Thus \(dL(x)=L(dx)\) and \(\pi L(x)=T(x)\). Extend by freeness, preserving all earlier values. At limit stages take the compatible union. This constructs a strict lift of the **entire** relative diagram, not a collection of unrelated lifts. Already specified higher boundaries remain fixed. It does not assert lifting through a nonfree quotient without checking its relations, or manufacture missing target-side coherence data.

Both the free index \(Q\mathcal I\) and its normalized word category \(UQ\mathcal I\) have the required free dg presentations. For the latter, the graded generators are bracket words in nonempty path-basis inputs. Order such a generator first by the sum of its path-stage counts as in (B.ND2), and then by its number of inputs. Its internal differential decreases the first weight; a merge keeps that weight and decreases the number of inputs; in a split each of the two resulting generators has smaller first weight, since the other block contains a nonempty positive-weight path. Identity terms are already in the base category. Thus (B.SF3) is triangular in this well-founded order. This verifies the freeness needed for lifting the actual strict-fold source; it is not an appeal to an unstated model-category structure.

Apply the lifting statement to the resolution graph (B.DA7), now formed from modules over the product categories used above. Projection onto the target diagram is surjective on every graded Hom group. Its Hom kernel is the shifted cone of postcomposition by the receiving replacement, acyclic by (B.ND7). Every target has a whole-diagram replacement. Consequently any prescribed relative free dg diagram of these target modules and natural transformations lifts, once its object replacements and already-fixed boundary lifts are supplied. Its higher maps and homotopies are natural in the parameter index because all entries lie in the same product-category module complexes.

For an explicit low-dimensional check, take closed degree-zero arrows \(a,b,c\) and chosen degree-zero lifts of these arrows and their composites. Suppose their pairwise composition witnesses \(H_{b,a}\) lie in the kernel and satisfy \(dH_{b,a}=L(b)L(a)-L(ba)\). The next obstruction and its filler are
\[
\begin{aligned}
\Omega_{c,b,a}
 &=L(c)H_{b,a}-H_{cb,a}+H_{c,ba}-H_{c,b}L(a),\\
d\Omega_{c,b,a}&=0,
\qquad \Omega_{c,b,a}\in\ker\pi,
\qquad dT_{c,b,a}=\Omega_{c,b,a},\quad |T_{c,b,a}|=-2.
\end{aligned}
\tag{B.ND10}
\]
Expanding the four differentials cancels the two copies of each composite by associativity. The image vanishes because the lower witnesses are in the kernel. This is the three-input instance of (B.ND9). A diagram with more cells is handled by the same well-founded induction after its boundary differential has been specified and checked to square to zero. An arbitrary chosen family of homotopies has not been declared coherent merely because the first composition defects vanish.

The whole-diagram resolutions and relative natural lifting constructions apply over the coefficient rings specified in B.1t. For the geometric consumer, the fixed strict square and folding-roof module comparisons have natural witnesses, and prescribed free higher diagrams can be lifted with their boundaries retained. The remaining assembly must still specify the actual joint compactification, base-change and composition parameter diagrams, account for changes of their module-variable index, and verify the simultaneous unit, counit and triangle boundaries there. The general nearby attaching, multiplicative descent and normalized coefficient comparisons are not established by this construction. \(\square\)



### Joint transport diagrams and changes of index

**Proposition B.1v (resolve the square, retaining its transport).** The two mate squares of (B.SM3) can be resolved as entire diagrams over their four different module categories. Their counit comparisons are then equalities on the joint models, with the specified induction-composition isomorphism, not just independently chosen homotopies at the four corners. There is also a transport-labelled resolution graph for changes of these indexing categories. It supplies coherent comparison maps for every supplied strict target diagram of index changes. Neither assertion requires restriction to preserve h-projectivity. We give the constructions and identify the geometric input, while keeping the remaining unit/triangle assembly separate.

**A category that records varying coefficients.** Let \(I\) be a small ordinary category and \(\mathcal C:I\to\mathrm{dgCat}_k\) a strict diagram, writing \(F_a:\mathcal C_i\to\mathcal C_j\) for \(a:i\to j\). Define its transport category \(\mathcal T\) to have objects \((i,X)\), and
\[
\mathcal T((j,Y),(i,X))
 =\bigoplus_{a:i\to j}\mathcal C_j(Y,F_aX).
\tag{B.TD1}
\]
The direction is important: the indexing arrow goes from \(i\) to \(j\), whereas its transport morphism goes from the \(j\)-fibre to the \(i\)-fibre. For \(u:Y\to F_aX\) and \(v:Z\to F_bY\), composition in \(\mathcal T\) is
\[
(a,u)\circ(b,v)=(ba,F_b(u)v).
\tag{B.TD2}
\]
The differential is the differential of each summand. The arrows of \(I\) have degree zero, so the Leibniz sign in the right side is exactly \((-1)^{|u|}\). Associativity is the equality
\(F_c(F_b(u)v)w=F_{cb}(u)F_c(v)w\), and the identity is \((1_i,1_X)\). This verifies a dg category over the original ring without any flatness assumption on the fibre Hom complexes.

A right \(\mathcal T\)-module is equivalent to right modules \(M_i\) and closed structure maps
\[
s_a:M_i\longrightarrow F_a^*M_j,
\qquad s_{ba}=F_a^*(s_b)s_a,\quad s_{1_i}=1.
\tag{B.TD3}
\]
Indeed \(m\in M_i(X)\) acts on \((a,u)\) by \(s_a(m)u\). The module identity is precisely (B.TD3) and (B.TD2). Conversely use the action on \((a,1_{F_aX})\). Equivalently the adjoints \(t_a:F_{a!}M_i\to M_j\) compose using the explicit balanced-tensor associator. This correspondence also identifies all homogeneous maps and their differentials: the structure maps have degree zero, so the required naturality is ordinary equality, with the usual Hom differential supplying its degree signs.

Resolve this one \(\mathcal T\)-module by the many-object semifree construction, obtaining \(r:P\to M\). Its evaluations \(P_i\) are h-projective over \(\mathcal C_i\). To prove this rather than assume it, evaluate a representable cell:
\[
\mathcal T(-,(i,X))|_{\mathcal C_j}
 =\bigoplus_{a:i\to j}\mathcal C_j(-,F_aX).
\tag{B.TD4}
\]
Each is a sum of representables. Every stage of the evaluated semifree filtration has graded-split attachments of their shifts, and the differential of a new generator lands in earlier stages. Thus the generatorwise acyclic-target Hom argument of B.1l applies. For arbitrary h-projective \(P\), first take a semifree replacement; its quasi-isomorphism is a homotopy equivalence over \(\mathcal T\), and evaluation preserves that equivalence. In particular no restriction along a general functor was claimed to preserve h-projectivity: it is this specific representable calculation that proves it. The map \(r\) respects every structure map exactly.

**The actual first mate square.** In (B.SM3) put \(M\) h-projective over \(\mathcal B\). Use the commutative-square category for \(I\), including its relation \(p\beta=F\alpha\). The following four modules, with the listed induction structure maps, form a right transport module:
\[
\begin{array}{c|c}
\text{fibre}&\text{module}\\\hline
\mathcal A&\alpha^*M\\
\mathcal B&M\\
\mathcal C&p^*F_!M\\
\mathcal D&F_!M
\end{array}
\qquad
\begin{array}{c|c}
\text{edge}&t_a\\\hline
\alpha&\epsilon^\alpha_M\\
F&1_{F_!M}\\
\beta&b_M\\
p&\epsilon^p_{F_!M}
\end{array}
\tag{B.TD5}
\]
The only nontrivial path relation is the second identity of (B.SM6), which was proved by tensor evaluation. Hence this is a module on the commutative square, not just on its free edge graph. Resolve it over \(\mathcal T\). Write \(P_A,P_B,P_C,P_D\) for the four h-projective values, \(r_A,r_B,r_C,r_D\) for the replacements, and \(t_\alpha,t_F,t_\beta,t_p\) for the new induction structure maps. Naturality of \(r\) and the path relation give
\[
\begin{aligned}
r_Ct_\beta&=b_M\beta_!r_A,\\
r_Bt_\alpha&=\epsilon^\alpha_M\alpha_!r_A,\\
r_Dt_F&=F_!r_B,\qquad
r_Dt_p=\epsilon^p_{F_!M}p_!r_C,\\
t_p\,p_!t_\beta
 &=t_F\,F_!t_\alpha\,C_{P_A}.
\end{aligned}
\tag{B.TD6}
\]
All four new structure maps are homotopy equivalences in this particular module square. For \(t_\alpha\) and \(t_p\), (B.SM2) makes the respective right sides quasi-isomorphisms. For \(t_\beta\), use (B.SM8) with the actual replacement \(r_A\). For \(t_F\), both ends of \(r_B\) are h-projective, so \(r_B\) is a homotopy equivalence and \(F_!\) preserves it. In every case the receiving \(r\) is a quasi-isomorphism, and both ends of the structure map are h-projective. These conclusions do not assert that the horizontal functor \(F\) itself is a quasi-equivalence.

Thus (B.SM10)'s comparison has a joint choice with zero defect in its first line: the equality is the first line of (B.TD6). The final line supplies its compatible counit square on the same joint resolution. Here is that square, entirely in h-projective modules over \(\mathcal D\):
\[
\begin{array}{ccc}
p_!\beta_!P_A&\xrightarrow{\ p_!t_\beta\ }&p_!P_C\\
{C_{P_A}}\downarrow&&\downarrow{t_p}\\
F_!\alpha_!P_A&\xrightarrow{\ t_F\,F_!t_\alpha\ }&P_D.
\end{array}
\]
The lower arrow is the displayed composite, and the left arrow is the balanced-tensor isomorphism (B.SM4); neither is an unnamed identification. This diagram also displays (B.TD8)'s equality below, but its horizontal arrows are not then asserted to be equivalences. The construction does not replace the original counit by a bare isomorphism class.

**The other mate, with different equivalence claims.** For h-projective \(N\) over \(\mathcal C\), the second transport module is
\[
\begin{array}{c|c}
\mathcal A&\beta^*N\\
\mathcal B&F^*p_!N\\
\mathcal C&N\\
\mathcal D&p_!N
\end{array}
\qquad
\begin{array}{c|c}
\alpha&d_N\\
\beta&\epsilon^\beta_N\\
p&1_{p_!N}\\
F&\epsilon^F_{p_!N}
\end{array}
\tag{B.TD7}
\]
Its path relation is exactly the second identity of (B.SM7). On its joint resolution,
\[
\begin{aligned}
r_Bt_\alpha&=d_N\alpha_!r_A,\\
r_Ct_\beta&=\epsilon^\beta_N\beta_!r_A,\\
r_Dt_p&=p_!r_C,\qquad
r_Dt_F=\epsilon^F_{p_!N}F_!r_B,\\
t_F\,F_!t_\alpha\,C_{P_A}
 &=t_p\,p_!t_\beta.
\end{aligned}
\tag{B.TD8}
\]
Here \(t_\alpha\) is a homotopy equivalence by (B.SM9), and \(t_p\) is one because \(r_C\) is a homotopy equivalence. No equivalence claim is made for \(t_\beta\) or \(t_F\): they represent counits of horizontal adjunctions, which need not be invertible. The last line is the joint resolved form of (B.SM11), retaining those actual counits.

Both constructions are natural in a whole dg-indexed parameter family. First use \(\mathcal J=Q\mathcal I\), and replace the input family by an h-projective module over \(\mathcal J^{\mathrm{op}}\otimes\mathcal B\), or over \(\mathcal J^{\mathrm{op}}\otimes\mathcal C\) in the second construction. Use these product categories as the fibres in (B.TD1). The vertical quasi-equivalences survive by (B.ND3), and the preceding proofs apply to the whole parameter family. By (B.ND6), evaluating it gives admissible h-projective modules. Resolving only the individual inputs would not justify this natural-family assertion.

**Changes of the indexing category.** A strict morphism of fibre diagrams consists of \(u:I\to I'\) and functors \(A_i:\mathcal C_i\to\mathcal C'_{ui}\) with \(A_jF_a=F'_{ua}A_i\). It induces a strict dg functor
\[
\tau:\mathcal T\longrightarrow\mathcal T',
\quad (i,X)\longmapsto(ui,A_iX),
\quad(a,v)\longmapsto(ua,A_jv).
\tag{B.TD9}
\]
The composition check is \(A_k(F_b(v)w)=F'_{ub}(A_jv)A_kw\). Distinct summands can map to the same summand; extend linearly, without asserting injectivity. Restriction \(\tau^*\) preserves objectwise quasi-isomorphisms, since it evaluates at the displayed objects. It need not preserve h-projectivity, and \(\tau\) is not assumed to be a quasi-equivalence. This avoids the invalid inference that tensoring an original-index quasi-equivalence with a nonflat fibre always preserves it.

We now construct higher comparisons, not just separate first lifts. Let \(K\) be an ordinary indexing category, \(s\mapsto\mathcal T_s\) a strict diagram with functors \(\tau_u\), and let \(M_s\) be modules with specified closed maps \(b_u:M_s\to\tau_u^*M_t\) satisfying the strict path and unit relations. Choose whole-module resolutions \(r_s:P_s\to M_s\), with \(P_s\) h-projective over \(\mathcal T_s\). For a fixed transport \(u:s\to t\), a degree-\(n\) resolution-graph arrow is \((v,a,h)\), with
\[
\begin{aligned}
v&:M_s\to\tau_u^*M_t,& |v|&=n,\\
a&:P_s\to\tau_u^*P_t,& |a|&=n,\\
h&:P_s\to\tau_u^*M_t,& |h|&=n-1,\\
D(v,a,h)&=(dv,da,(\tau_u^*r_t)a-vr_s-dh).
\end{aligned}
\tag{B.TD10}
\]
Take the direct sum of these complexes over transports with the same endpoints. If \((w,c,k)\) has degree \(m\) over \(z:t\to q\), composition is
\[
\begin{aligned}
(w,c,k)\circ(v,a,h)
 =\bigl(&\tau_u^*(w)v,\ \tau_u^*(c)a,\\
        &\tau_u^*(k)a+(-1)^m\tau_u^*(w)h\bigr)
\end{aligned}
\tag{B.TD11}
\]
over \(zu\). Strict pullback composition and (B.DA7)'s signed graph calculation prove \(D^2=0\), the graded Leibniz rule and associativity; all pullbacks here are degree-zero dg functors. Units are \((1,1,0)\).

Projection onto \(v\) is degreewise surjective, even in a fixed transport summand. Its kernel is the shifted cone of
\(\operatorname{Hom}_{\mathcal T_s}(P_s,\tau_u^*P_t)\to
\operatorname{Hom}_{\mathcal T_s}(P_s,\tau_u^*M_t)\).
This map is a quasi-isomorphism: \(\tau_u^*r_t\) is an objectwise quasi-isomorphism and \(P_s\) is h-projective. Thus the kernel is acyclic **for each transport**, without requiring \(\tau_u^*P_t\) to be h-projective. Direct sums retain acyclicity.

To retain the index labels when lifting, use the normalized word category \(U(kK)\), not an unlabelled free replacement that could mix transports. Its generator \([u_n|\cdots|u_1]\) has degree \(1-n\) and label \(u_n\cdots u_1\). For degree-zero arrows (B.SF3) has only the split and merge terms. Both preserve this composite label, and every term involves generators of smaller word length. Identities are normalized as in B.1t. The strict target functor sends a one-letter generator to \(b_u\) and longer generators to zero; its chain property is precisely the strict composition law for \(b\). Lift inductively by (B.ND9), within the fixed-label acyclic kernel. This gives a strict graph-valued functor on \(U(kK)\), hence the entire strictly unital higher comparison system. Its first and second components satisfy
\[
\begin{aligned}
(\tau_u^*r_t)a_u-b_ur_s&=dh_u,\qquad da_u=0,\\
d a_{z,u}&=\tau_u^*(a_z)a_u-a_{zu}.
\end{aligned}
\tag{B.TD12}
\]
The second equation is the \(a\)-component of the graph differential, and the corresponding \(h\)-component is retained by the same lift. Higher word boundaries and all unit relations hold because the lift is a dg functor, not because an arbitrary collection of homotopies was declared coherent. Previously fixed lifts on a relative free dg subdiagram remain fixed by the relative form of (B.ND9); a subdiagram with additional relations needs those relations checked separately.

If \(b_u\) is a quasi-isomorphism, then \(a_u\) is one by the first equation and two-out-of-three. It is not automatically a homotopy equivalence over \(\mathcal T_s\), because its pulled-back target need not be h-projective there. In particular applying an induction functor to that comparison still requires the h-projective or homotopy-equivalence hypotheses used in B.1s. This distinction is essential for subsequent unit and triangle constructions.

**The geometric composition square.** For the actual two-morphism composition, use B.1r's strict square \(\alpha:\mathcal L_{g,f}\to\mathcal G_J\), \(\beta:\mathcal L_{g,f}\to\mathcal G_L\), \(p=\pi_g\), \(F=F_f\), with \(p\beta=F\alpha\). Its \(\alpha,p\) are the already-proved quasi-equivalences; no unresolved proper image replaces \(\mathcal L_{g,f}\). Equations (B.TD5)–(B.TD8) therefore supply joint natural resolved models of both of its mates and their counit squares. The strict arrows of the folding roof (B.SF7) may be used as fibre functors as well. Each specified strict refinement map and strict outer map (B.SF9) induces (B.TD9); composition is retained by (B.TD11)–(B.TD12). Canonical proper-image isomorphisms are not silently treated as equalities: work with the formal paths of their strict maps and retain each specified isomorphism and coherence cell when presenting the target diagram.

The remaining task is to supply the joint geometric unit and triangle boundaries, with their changes of compactification and base, and apply the relative construction to those actual target cells. The fact that every *supplied* strict index-change diagram has coherent lifts does not manufacture missing target-side cells. Both natural mate/counit squares and the index-change lifting obstruction have been handled here; full enhanced geometric adjunction, nearby attaching, normalized coefficient transport are not asserted. \(\square\)



### Joint unit and paired triangle diagrams

**Proposition B.1w (retain both triangles in the same target).** The common-span square of (B.SM3) has joint h-projective models of both unit comparisons as well as its two counit comparisons. For each strict fibre functor, both triangle boundaries can be included in one target diagram before taking its resolution. We construct the diagrams and their relations explicitly. In particular the second triangle uses a replacement of the restricted input, not an unresolved induction of that input. This supplies the fixed-square adjunction boundary diagrams needed after B.1v; it does not assert the remaining global geometric comparison cells.

**The unit-mate diagram.** Temporarily write a strict square as
\[
\begin{matrix}
\mathcal A&\xrightarrow{H}&\mathcal C\\
K\downarrow&&J\downarrow\\
\mathcal B&\xrightarrow{V}&\mathcal D,
\end{matrix}
\quad JH=VK,
\qquad
b_{K_!L}H_!(\eta^K_L)=J^*(C_L)\eta^J_{H_!L}.
\tag{B.JT1}
\]
Here \(C_L:J_!H_!L\longrightarrow V_!K_!L\) is the balanced-tensor isomorphism and \(b:H_!K^*\longrightarrow J^*V_!\) its first mate. We use only the two substitutions below, for which (B.JT1) is the already checked first line of (B.SM6) or (B.SM7). Let \(L\) be h-projective over \(\mathcal A\). Take the following five labelled vertices:
\[
\begin{array}{c|c|c}
\text{vertex}&\text{fibre}&\text{target module}\\\hline
0&\mathcal A&L\\
1&\mathcal A&K^*K_!L\\
2&\mathcal C&H_!L\\
3&\mathcal C&J^*J_!H_!L\\
4&\mathcal C&J^*V_!K_!L.
\end{array}
\tag{B.JT2}
\]
There are edges \(0\to1\), \(0\to2\), \(1\to4\), \(2\to3\), \(3\to4\). Their fibre functors are respectively \(1,H,H,1,1\); their induction structure maps are \(\eta^K_L,1_{H_!L},b_{K_!L},\eta^J_{H_!L},J^*C_L\). Impose the path relation \((0\to1\to4)=(0\to2\to3\to4)\). Both paths have fibre functor \(H\), and (B.JT1) proves their equality on the target modules. Consequently this is a genuine module over B.1v's transport category with that relation, not just a collection of maps on its free edge graph.

Resolve the whole transport module, with values \(Q_i\) and quasi-isomorphisms \(r_i\) to (B.JT2). All \(Q_i\) are h-projective in their respective fibres by (B.TD4). Name the new structure maps \(u:Q_0\to Q_1\), \(\mu:H_!Q_0\to Q_2\), \(\nu:H_!Q_1\to Q_4\), \(v:Q_2\to Q_3\), \(w:Q_3\to Q_4\). The single resolution gives
\[
\begin{aligned}
r_1u&=\eta^K_Lr_0,&r_2\mu&=H_!r_0,\\
r_4\nu&=b_{K_!L}H_!r_1,\\
r_3v&=\eta^J_{H_!L}r_2,&r_4w&=J^*(C_L)r_3,\\
\nu H_!u&=wv\mu.
\end{aligned}
\tag{B.JT3}
\]
Thus the actual unit comparison is the commutative diagram
\[
\begin{array}{ccc}
H_!Q_0&\xrightarrow{H_!u}&H_!Q_1\\
{\mu}\downarrow&&\downarrow{\nu}\\
Q_2&\xrightarrow{\ wv\ }&Q_4.
\end{array}
\]
The lower arrow still factors through \(Q_3\): it is the resolved unit followed by the specified induction-composition isomorphism, not an unspecified comparison. The map \(r_0\) is a homotopy equivalence since \(L,Q_0\) are h-projective. Hence \(H_!r_0\), and then \(\mu\), are homotopy equivalences. Also \(w\) is a homotopy equivalence, because \(J^*C_L\) is an actual isomorphism and \(r_3,r_4\) are quasi-isomorphisms. These arguments do not apply induction to an arbitrary quasi-isomorphism.

The two required specializations are
\[
\begin{array}{c|cccc|cc}
&K&H&J&V&\text{mate}&\text{associator}\\\hline
\text{first unit}&\alpha&\beta&p&F&b&C\\
\text{other unit}&\beta&\alpha&F&p&d&C^{-1}.
\end{array}
\tag{B.JT4}
\]
In the first row, (B.SM8), applied to the replacement \(r_1\) and the h-projective module \(\alpha_!L\), proves that \(\nu\) is a homotopy equivalence. The units for \(\alpha,p\) are quasi-isomorphisms by (B.SM1), so \(u,v\) are homotopy equivalences too. In the other row, (B.SM9), with h-projective input \(\beta_!L\), proves the same assertion for \(\nu\). However \(\eta^\beta\) and \(\eta^F\) need not be quasi-isomorphisms: no equivalence claim is made for \(u,v\) in that row. Both rows retain the full unit equations.

**A paired triangle target.** Let \(F:\mathcal C\to\mathcal D\) be any strict dg functor, \(T=F_!\), \(U=F^*\). For h-projective \(N\) over \(\mathcal D\), first choose an h-projective replacement \(q:P\to UN\), and put
\[
e=\epsilon_N Tq:TP\longrightarrow N,
\qquad
\begin{array}{c|c|c}
\text{vertex}&\text{fibre}&\text{target module}\\\hline
a&\mathcal C&P\\
b&\mathcal C&UTP\\
c&\mathcal C&UN\\
d&\mathcal D&TP\\
n&\mathcal D&N.
\end{array}
\tag{B.JT5}
\]
The edges within the \(\mathcal C\)-fibre carry \(\eta_P\) on \(a\to b\), \(Ue\) on \(b\to c\), and \(q\) on \(a\to c\). The three edges with fibre functor \(F\) have induction structure maps \(1_{TP}\) on \(a\to d\), \(\epsilon_{TP}\) on \(b\to d\), and \(\epsilon_N\) on \(c\to n\). Finally \(d\to n\) has fibre functor \(1_{\mathcal D}\) and map \(e\). Impose these four relations, with the unit induction identifications retained:
\[
\begin{aligned}
Ue\,\eta_P&=q,\\
\epsilon_{TP}T\eta_P&=1_{TP},\\
e&=\epsilon_N Tq,\\
e\,\epsilon_{TP}&=\epsilon_N T(Ue).
\end{aligned}
\tag{B.JT6}
\]
The first follows from naturality \(UTq\,\eta_P=\eta_{UN}q\) and the second strict triangle \(U\epsilon_N\eta_{UN}=1_{UN}\). The second is the first strict triangle. The third is the definition of \(e\), and the fourth is counit naturality for the closed map \(e:TP\to N\). These identities can also be checked on the tensors of (B.DA3)–(B.DA5); no permutation of homogeneous factors occurs. The corresponding index paths have identical fibre functors: either \(1_{\mathcal C}\) or \(F\). Thus quotienting the path category by these relations defines a strict fibre diagram and a target transport module. An unresolved \(TUN\) occurs only inside the strict identity proving the first relation; it is never substituted for the derived input \(TP\).

Resolve this entire target. Denote its five h-projective values by \(Q_a,Q_b,Q_c,Q_d,Q_n\), and replacements by \(r_a,r_b,r_c,r_d,r_n\). Name the lifted structure maps
\(u:Q_a\to Q_b\), \(b:Q_b\to Q_c\), \(c:Q_a\to Q_c\),
\(\ell:TQ_a\to Q_d\), \(h:TQ_b\to Q_d\), \(d:TQ_c\to Q_n\), and \(e':Q_d\to Q_n\).
Here the roman edge name \(d\) is a closed degree-zero map, not the differential, which below is written \(\partial\). The four relations are now exact on these common models:
\[
bu=c,\qquad hTu=\ell,\qquad
e'\ell=dTc,\qquad e'h=dTb.
\tag{B.JT7}
\]
The following diagram displays both squares of the counit compatibility; the separate relation \(bu=c\) retains the other triangle on the \(\mathcal C\)-side:
\[
\begin{array}{ccccc}
TQ_a&\xrightarrow{Tu}&TQ_b&\xrightarrow{Tb}&TQ_c\\
{\ell}\downarrow&&\downarrow{h}&&\downarrow{d}\\
Q_d&\xrightarrow{1}&Q_d&\xrightarrow{e'}&Q_n.
\end{array}
\]
These are not new arbitrary maps satisfying the same abstract relations. Naturality of the replacement binds them to the actual unit and counit:
\[
\begin{aligned}
r_bu&=\eta_Pr_a,&r_cb&=Ue\,r_b,&r_cc&=qr_a,\\
r_d\ell&=Tr_a,&r_dh&=\epsilon_{TP}Tr_b,\\
r_nd&=\epsilon_NTr_c,&r_ne'&=er_d.
\end{aligned}
\tag{B.JT8}
\]
The map \(c\) is a quasi-isomorphism by its displayed equation, since \(q,r_a,r_c\) are. It is therefore a homotopy equivalence between h-projectives. The map \(r_a:Q_a\to P\) is likewise a homotopy equivalence, so \(Tr_a\) is one. Its equation and \(r_d\) show that \(\ell\) is a homotopy equivalence as well. Neither \(d\) nor \(e'\) is generally invertible. The argument has not required \(UTP\) or \(UN\) to be h-projective.

Equations (B.JT7)–(B.JT8), with the explicit equivalence legs \(c,\ell\), represent the two derived triangle boundaries on one diagram. To see concrete homotopies after transporting the legs, choose inverses \(\iota:Q_c\to Q_a\), \(j:Q_d\to TQ_a\), and degree-minus-one maps \(s_c,s_\ell\) such that \(c\iota-1=\partial s_c\), \(j\ell-1=\partial s_\ell\). Then
\[
bu\iota-1_{Q_c}=\partial s_c,
\qquad
jhTu-1_{TQ_a}=\partial s_\ell.
\tag{B.JT9}
\]
The first is the right triangle after identifying the replacement of \(UN\) by \(c\); the second is the left triangle at \(Q_a\) after identifying \(Q_d\) with \(TQ_a\). The other two relations in (B.JT7) identify their counit maps with the same resolved \(e\). More explicitly \(r_ne'\ell=\epsilon_NT(qr_a)\) and \(r_nd=\epsilon_NTr_c\), so \(e'\ell=dTc\) is exactly the change of restricted-input model from \(Q_a\) to \(Q_c\). The two sides of (B.JT9) must not be called strict identities before the inverse homotopies are chosen. This is consistent with, and supplies common models for, the earlier fixed-choice formulas (B.DA11)–(B.DA12).

**One joint presentation, not independent corner replacements.** For the fixed common-span square, take the two unit diagrams (B.JT2), the two counit diagrams (B.TD5), (B.TD7), and the paired triangle diagrams (B.JT5) for the fibre functors at the required inputs. Choose the finitely many input replacements \(q\) first. Form the category generated by all these labelled diagrams. Whenever an input is shared, use one vertex if the fibre and module are literally the same; otherwise keep the two vertices and the specified identity or closed isomorphism between their target modules. Identify only equal fibre functors, and impose only the checked relations (B.SM6)–(B.SM7), (B.JT6) and those of the counit diagrams. Each generator has its displayed target map, and every imposed relation has just been proved. This constructs a single target transport module. Its one semifree resolution supplies all these equations simultaneously; the proof of (B.TD4) still applies if gluing introduces further index paths. Direct sums over those paths cause no finiteness or flatness assumption.

This procedure need not preserve an earlier *choice* of replacement literally. It does preserve the earlier counit target and its relation, and has controlled comparisons with those choices. For an old subdiagram with transport category \(\mathcal T_s\), let \(\tau:\mathcal T_s\to\mathcal T\) be its inclusion, and let \(\rho_s:P_s\to M_s\), \(\rho:Q\to M\) be its old and the new whole resolutions. By construction \(M_s=\tau^*M\). Since \(P_s\) is h-projective, the graph lift of the identity target map yields
\[
A:P_s\longrightarrow\tau^*Q,\qquad
(\tau^*\rho)A-\rho_s=\partial H,
\qquad \partial A=0.
\tag{B.JT10}
\]
The map \(A\) is a quasi-isomorphism. For these inclusions the fibre functors are identities, so its value at each fibre is between h-projectives by (B.TD4), and is a homotopy equivalence. Applying an induction functor to such a *fibrewise* comparison is justified. We have not claimed that \(\tau^*Q\) is h-projective over the whole subdiagram category. For the strict diagram of inclusions, (B.TD10)–(B.TD12) supply the labelled higher comparison maps and their witnesses. Earlier specified lifts can be kept on a relative free dg subdiagram as in (B.ND9); extra relations are not made automatic by that relative lifting assertion.

For a dg-indexed family, first use the free index \(\mathcal J=Q\mathcal I\) of B.1u, and choose the initial \(L,N,P,q\) over the appropriate product categories \(\mathcal J^{\mathrm{op}}\otimes\mathcal C_i\). The entire construction then takes place over those fibres. Equations (B.JT1) and (B.JT6) are strict natural identities there, with the homogeneous naturality convention (B.ND4); evaluating after the joint resolution gives h-projective values by (B.ND6). In particular \(q\) is a single natural replacement of the whole input family, not a list of unrelated pointwise replacements. This proves family naturality in the stated free-index model. It does not turn a resolution-graph arrow whose compatibility holds only up to its recorded homotopy into a strictly commuting map of the target presentations.

**Exact geometric application and remaining boundary.** For \(f,g\), substitute \(\mathcal A=\mathcal L_{g,f}\), \(\mathcal B=\mathcal G_J\), \(\mathcal C=\mathcal G_L\), \(\mathcal D=\mathcal I_Y\), \(K=\alpha\), \(H=\beta\), \(J=\pi_g\), \(V=F_f\) from (B.GC2)–(B.GC6). Their equation \(\pi_g\beta=F_f\alpha\) is strict and their vertical functors are the proved quasi-equivalences, so both rows of (B.JT4) apply. The paired triangle construction applies to each strict functor in this common span and the strict folding roof (B.SF7). Thus the fixed common-span unit, counit and paired triangle targets are now supplied with common resolved models and explicit comparison legs.

What remains is the actual map of these target presentations for every geometric refinement and base-change/composition array, including their specified proper-image isomorphisms and higher fold cells. A strict fibre-diagram map alone does not assert compatibility of an arbitrarily chosen \(q\); its target comparison must be supplied, or its resolution-graph homotopy retained. General fibre pullback still need not preserve h-projectivity. The inclusion argument above has identity fibres and must not be used to erase this distinction for geometric maps. Full global enhanced adjunction, nearby attaching, normalized coefficient transport are not established by this fixed-fibre comparison. \(\square\)



### The joint left triangle at every input

**Proposition B.1x (do not restrict the first triangle to right inputs).** For every h-projective left input \(A\), the first triangle of \(T=F_!\dashv U=F^*\) has a joint resolved target diagram. It joins the paired right-input construction of B.1w along its actual three-vertex subdiagram. Thus the common presentation covers the first triangle at arbitrary \(A\) and the second triangle at arbitrary h-projective \(N\), without requiring \(A\) to be equivalent to a replacement of some \(UN\).

**The additional target.** For a strict dg functor \(F:\mathcal C\to\mathcal D\), take the three vertices
\[
\begin{array}{c|c|c}
\text{vertex}&\text{fibre}&\text{target module}\\\hline
0&\mathcal C&A\\
1&\mathcal C&UTA\\
2&\mathcal D&TA.
\end{array}
\tag{B.LA1}
\]
The edge \(0\to1\) has identity fibre functor and map \(\eta_A\). The edges \(1\to2\) and \(0\to2\) both have fibre functor \(F\), with induction structure maps \(\epsilon_{TA}\) and \(1_{TA}\), respectively. Impose the relation that the two paths from \(0\) to \(2\) agree. Their fibre functors agree, and their target maps agree by the strict triangle \(\epsilon_{TA}T\eta_A=1_{TA}\) proved in (B.DA5). This is a transport module on the triangle category with its relation. The target \(UTA\) is not assumed h-projective, and the unit \(\eta_A\) is not assumed a quasi-isomorphism.

Resolve this one transport module. Its values \(R_0,R_1,R_2\) are h-projective in their fibres by (B.TD4). Write \(r_0:R_0\to A\), \(r_1:R_1\to UTA\), \(r_2:R_2\to TA\) for the replacements, and \(u:R_0\to R_1\), \(v:TR_1\to R_2\), \(\lambda:TR_0\to R_2\) for its structure maps. All are closed and
\[
\begin{aligned}
r_1u&=\eta_A r_0,\\
r_2v&=\epsilon_{TA}Tr_1,\qquad r_2\lambda=Tr_0,\\
vTu&=\lambda.
\end{aligned}
\tag{B.LA2}
\]
The equation is visible as a triangle, with the comparison leg labelled rather than erased:
\[
\begin{array}{ccc}
TR_0&\xrightarrow{Tu}&TR_1\\
{\lambda}\downarrow&&\downarrow{v}\\
R_2&\xrightarrow{1}&R_2.
\end{array}
\]
Since \(A,R_0\) are h-projective, \(r_0\) is a homotopy equivalence. Induction preserves that equivalence, so \(Tr_0\) is one; its equality with \(r_2\lambda\) implies that \(\lambda\) is a quasi-isomorphism. Its two ends are h-projective, so \(\lambda\) is a homotopy equivalence. Equivalently \(r_2\) is itself between h-projectives, because \(T\) preserves h-projectivity and \(A\) is h-projective. This proof never applies \(T\) to the unresolved quasi-isomorphism \(r_1\) as though it preserved all quasi-isomorphisms.

Choose a homotopy inverse \(j:R_2\to TR_0\) and a degree-minus-one map \(s\) on \(TR_0\) with \(j\lambda-1=\partial s\). Then the actual transported counit \(jv\) and the unit \(u\) have first triangle
\[
(jv)Tu-1_{TR_0}=\partial s.
\tag{B.LA3}
\]
It is a homotopy identity, not a claim that the comparison leg is literally an identity. Naturality in (B.LA2) binds it to the original strict adjunction. Indeed \(r_1u=\eta_A r_0=UT(r_0)\eta_{R_0}\), while \(r_2v=\epsilon_{TA}Tr_1\). Thus the diagram represents the unit at \(R_0\) and the counit at \(TR_0\) after the explicit equivalences \(r_0\), \(Tr_0\) and \(\lambda\). Formula (B.DA11) supplies the earlier fixed-choice witness, and this construction supplies compatible choices on the whole target triangle.

**The overlap is exact.** In (B.JT5) the left input happens to be \(P\), a replacement of \(UN\). When \(A=P\), the target (B.LA1) is exactly the subdiagram on vertices \(a,b,d\) of that paired target:
\[
\begin{array}{c|ccc}
\text{left target vertex}&0&1&2\\\hline
\text{paired target vertex}&a&b&d\\
\text{target module}&P&UTP&TP.
\end{array}
\qquad
(u,v,\lambda)=(u,h,\ell)
\text{ on a common resolution}.
\tag{B.LA4}
\]
Here the equality of lifted maps is asserted only after taking one resolution of the combined presentation and restricting its structure maps; independently chosen earlier resolutions need not agree literally. The target relation in (B.LA2) is the second relation in (B.JT6), and the resolved relation is \(hTu=\ell\) in (B.JT7). Consequently the first witness in (B.LA3) agrees with the left-triangle witness in (B.JT9) on that shared model if the same inverse and homotopy are chosen. No additional target relation is being postulated on the overlap.

For other \(A\), attach (B.LA1) as an additional three-vertex diagram to B.1w's common presentation. Use the same target modules whenever they are shared and the explicit closed comparison maps otherwise. Only the proved strict triangle and the existing checked relations are imposed. One transport-module resolution then handles these triangles, both unit-mate squares, both counit squares and the paired right-input triangles. Comparison with an earlier separate triangle or paired resolution uses (B.JT10): the inclusion has identity fibre functors, its evaluated comparison is a homotopy equivalence, and its higher inclusion comparisons retain the graph witnesses of (B.TD10)–(B.TD12). Literal preservation of arbitrary old replacement choices is not claimed.

The distinction between arbitrary \(A\) and the chosen \(P\) matters. Already for scalar extension \(k\to M_2(k)\), \(A=k\) has one-dimensional cohomology, whereas the underlying vector-space cohomology of a right \(M_2(k)\)-module has even dimension when finite. The latter assertion follows directly from the two diagonal matrix idempotents: they split the module into two summands, and the off-diagonal matrix units give inverse isomorphisms between those summands. The same identities hold on cohomology. Thus an arbitrary left input need not be covered by calling it a replacement of a restricted right input. The three-vertex construction does not make that assumption.

Whole dg-indexed families are handled before evaluation over \(\mathcal J^{\mathrm{op}}\otimes\mathcal C\) and \(\mathcal J^{\mathrm{op}}\otimes\mathcal D\), with \(\mathcal J=Q\mathcal I\) and \(A\) h-projective over the product. The unit and counit are natural on that product category, and (B.ND6) gives h-projective evaluations. This is the same family convention as B.1w, so the overlap and the inclusions remain compatible there.

Apply the construction to every strict functor in the geometric common span of (B.GC2)–(B.GC6) and to the strict folding roofs (B.SF7). Together with B.1w, this gives the fixed-input unit, counit and two-triangle target diagrams at the stated h-projective module scope. Geometric refinements, compositions and base changes require comparisons of these target presentations that preserve the proper-image isomorphisms and higher fold cells. The identity-fibre inclusion argument proves neither general pullback preservation of h-projectivity nor global geometric coherence. It also does not construct nearby attaching maps or normalized coefficient transport. \(\square\)



### Refinement maps of the joint adjunction targets

**Proposition B.1y (compare the actual targets across a refinement).** The proper refinements of B.1m admit compatible resolutions of their restricted target modules. Their unit and counit comparisons then have joint models, and there are actual maps of both the paired triangle target of B.1w and the arbitrary left-input target of B.1x. These maps retain the canonical direct-image isomorphisms rather than replacing them by equalities. Their resolution comparisons have the labelled higher coherence described below. This assertion concerns the refinement diagram at fixed geometric endpoints; compatibility with the full composition and base-change arrays is a further stated obligation.

**Transport with specified associators.** Let \(K\) be a small category of refinements, with dg categories \(\mathcal C_i\), strict dg functors \(G_g:\mathcal C_i\to\mathcal C_j\), and closed natural isomorphisms \(m_{h,g}:G_hG_g\to G_{hg}\). Require the pentagon and unit identities. Use normalized identities \(G_1=1\), retaining the given unit identifications when comparing to an unnormalized model. Concretely replace only the identity-arrow functors and conjugate the composition maps by their given unit isomorphisms; the unit identities make the new unit maps identities, and conjugation preserves the pentagon. For the actual refinements these data and their identities are (B.CR2)–(B.CR4). The transport construction becomes
\[
\begin{aligned}
\mathcal T((j,Y),(i,X))&=\bigoplus_{g:i\to j}\mathcal C_j(Y,G_gX),\\
(g,u)\circ(h,v)&=(hg,m_{h,g,X}G_h(u)v).
\end{aligned}
\tag{B.RT1}
\]
Naturality of \(m\) moves it through the homogeneous morphism \(u\) without a sign, since \(m\) has degree zero. The two triple composites are equal by its pentagon; its unit identities give identities in \(\mathcal T\). Closedness of \(m\) gives the same differential and Leibniz rule as (B.TD2). This proves the dg-category axioms with the original associators present.

A right module consists of \(M_i\) and closed maps \(s_g:M_i\to G_g^*M_j\) satisfying
\[
m_{h,g}^*s_{hg}=G_g^*(s_h)s_g.
\tag{B.RT2}
\]
Here \(m_{h,g}^*:G_{hg}^*M\to G_g^*G_h^*M\) is induced by the contravariant module action on \(m\). The action is still \(x(g,u)=s_g(x)u\); its associativity is precisely (B.RT2). Evaluating a representable gives the same sum \(\bigoplus_g\mathcal C_j(-,G_gX)\) as (B.TD4). Thus one semifree resolution over \(\mathcal T\) has h-projective values in every fibre. No flatness or projectivity-preserving general restriction is assumed.

**Resolve the refinement inputs together.** Write \(F_i:\mathcal C_i\to\mathcal D\) for the fixed-endpoint output functors and \(\beta_g:F_jG_g\xrightarrow{\sim}F_i\) for (B.CR5). Their compatibility is \(\beta_{hg}F_k(m_{h,g})=\beta_g(\beta_hG_g)\). Put \(S_g=G_{g!}\), \(T_i=F_{i!}\), \(U_i=F_i^*\), and use the actual maps \(\chi_g,c_g,k_g\) of (B.CR6)–(B.CR8). For h-projective \(N\) over \(\mathcal D\), the modules \(M_i=U_iN\) with \(s_g=\chi_{g,N}\) satisfy (B.RT2): both sides act on \(n\) by the displayed composite of \(\beta\)'s. Resolve this single module. Its values \(q_i:P_i\to U_iN\) and induction structure maps \(a_g:S_gP_i\to P_j\) obey
\[
\begin{aligned}
q_ja_g&=k_{g,N}S_gq_i,\\
a_hS_ha_g&=a_{hg}\,\widehat m_{h,g,P_i}.
\end{aligned}
\tag{B.RT3}
\]
The isomorphism \(\widehat m:S_hS_g\to S_{hg}\) combines balanced-tensor associativity and induction along \(m\); it is specified, not suppressed. The second equation is the induction form of the module relation. Each \(a_g\) is a homotopy equivalence when \(G_g\) is a quasi-equivalence. Indeed the adjoint of its first equation is
\(G_g^*(q_j)G_g^*(a_g)\eta^{G_g}_{P_i}=\chi_{g,N}q_i\).
The units are quasi-isomorphisms by (B.SM1), while \(q_i,q_j\) are quasi-isomorphisms and \(\chi\) is an isomorphism. Two-out-of-three and the detection argument of (B.SM2) show that \(a_g\) is a quasi-isomorphism; its two ends are h-projective. This does not presume that \(S_gq_i\) is a quasi-isomorphism.

Set \(e_i=\epsilon^i_NT_iq_i\), the actual resolved counit. Equations (B.CR8), (B.RT3) and naturality of \(c\) give
\[
\begin{aligned}
e_jT_ja_g&=e_i c_{g,P_i},\\
t_g&=T_ja_g\,c_{g,P_i}^{-1}:T_iP_i\longrightarrow T_jP_j,\\
e_jt_g&=e_i,\qquad t_ht_g=t_{hg}.
\end{aligned}
\tag{B.RT4}
\]
The maps \(t_g\) are homotopy equivalences. For their composition, naturality moves \(T_ja_g\) through \(c_h^{-1}\); then use \(a_hS_ha_g=a_{hg}\widehat m\) and
\(c_g c_{h,S_gP_i}=c_{hg}T_k\widehat m\).
The two factors \(T_k\widehat m\) cancel. This proves the last equality with its canonical identifications accounted for, rather than choosing a separate direct comparison. The units are identities. Diagrammatically the exact counit comparison is
\[
\begin{array}{ccc}
T_jS_gP_i&\xrightarrow{T_ja_g}&T_jP_j\\
{c_{g,P_i}}\downarrow&&\downarrow{e_j}\\
T_iP_i&\xrightarrow{e_i}&N.
\end{array}
\]

**The induced map on transport categories.** A change of a strict fibre diagram need only commute through specified isomorphisms. More precisely, let \(u:I\to I'\), let \(A_i:\mathcal C_i\to\mathcal C'_{ui}\), and give closed natural isomorphisms \(\theta_a:A_jF_a\to F'_{ua}A_i\), compatible with composition and identities. Then
\[
\tau(i,X)=(ui,A_iX),\qquad
\tau(a,v)=(ua,\theta_{a,X}A_j(v))
\tag{B.RT5}
\]
is a strict functor between the transport categories. For \(a:i\to j\), \(b:j\to k\), compatibility means
\(\theta_{ba}=F'_{ub}(\theta_a)(\theta_bF_a)\).
Naturality of \(\theta_b\) moves \(A_kF_b(v)\) to \(F'_{ub}A_j(v)\), and this compatibility makes (B.TD2) agree on both sides. Differentials and units are preserved because \(\theta\) is closed and unital. This is a direct verification, not an identification of \(A_jF_a\) with \(F'_{ua}A_i\).

For the paired triangle shape, take \(A_i=G_g\) on its three \(\mathcal C\)-vertices and the identity on its two \(\mathcal D\)-vertices. On each crossing edge use \(\theta=\beta_g^{-1}:F_i\to F_jG_g\); on the other edges use identities. Every path relation in (B.JT6) crosses at most once, so the required compatibility is the same \(\beta_g^{-1}\) on both paths. This defines an actual functor \(\tau_g\) between the two paired-target transport categories.

**All seven edges of the paired target.** Use the \(q_i,P_i,a_g\) of (B.RT3), not independently chosen replacements. On the five vertices \((P_i,U_iT_iP_i,U_iN,T_iP_i,N)\) of (B.JT5), specify the following induction-side comparison maps:
\[
\begin{array}{c|c}
\text{vertex}&\text{comparison}\\\hline
a&a_g:S_gP_i\to P_j\\
b&B_g=U_j(t_g)k_{g,T_iP_i}:S_gU_iT_iP_i\to U_jT_jP_j\\
c&k_{g,N}:S_gU_iN\to U_jN\\
d&t_g:T_iP_i\to T_jP_j\\
n&1_N.
\end{array}
\tag{B.RT6}
\]
After adjunction on the first three vertices, these are a map of modules over \(\tau_g\). Here are the checks, including the unit, not only the terminal counit:
\[
\begin{aligned}
B_gS_g\eta^i_{P_i}&=\eta^j_{P_j}a_g,\\
k_{g,N}S_g(U_ie_i)&=U_je_j B_g,\\
k_{g,N}S_gq_i&=q_ja_g.
\end{aligned}
\tag{B.RT7}
\]
For the first, (B.CR9) changes the left side to \(U_j(t_gc_{g,P_i})\eta^j_{S_gP_i}\); use \(t_gc_{g,P_i}=T_ja_g\) and unit naturality. For the second use naturality of \(k\) and \(e_jt_g=e_i\). The third is (B.RT3). The remaining four edges satisfy
\[
\begin{aligned}
t_gc_{g,P_i}&=T_ja_g,\\
t_g\epsilon^i_{T_iP_i}c_{g,U_iT_iP_i}
 &=\epsilon^j_{T_jP_j}T_jB_g,\\
\epsilon^i_Nc_{g,U_iN}&=\epsilon^j_NT_jk_{g,N},\\
e_jt_g&=e_i.
\end{aligned}
\tag{B.RT8}
\]
The middle two are (B.CR8), with counit naturality for \(t_g\) in the second line. The first and last are (B.RT4). These are precisely the crossing-edge conditions for (B.RT5); the factors \(c_g\) encode the specified \(\beta_g\). Thus all seven edges and the four target relations are respected. The triangle comparisons have not been inferred from a bare equivalence of adjoints.

Every component of this target-module map is an objectwise quasi-isomorphism after taking its restriction-side form. At \(a\) it is \(G_g^*a_g\,\eta^{G_g}_{P_i}\). At \(b\) it is \(G_g^*U_j(t_g)\chi_{g,T_iP_i}\); at \(c\) it is \(\chi_{g,N}\). The last two are \(t_g,1\). These assertions follow from (B.SM1), the actual isomorphisms \(\chi\), and preservation of homotopy equivalences by dg functors. No projectivity of an unresolved restricted module is used.

**Arbitrary left inputs and the unit square.** More generally, let h-projective \(A_i\) have coherent homotopy equivalences \(a_g:S_gA_i\to A_j\) satisfying (B.RT3)'s composition equation, without any \(q_i\). Set \(t_g=T_ja_g c_{g,A_i}^{-1}\) and \(B_g=U_j(t_g)k_{g,T_iA_i}\). The three vertices of (B.LA1) have comparisons \((a_g,B_g,t_g)\). The first equation of (B.RT7) and first two of (B.RT8), with \(P_i\) replaced by \(A_i\), verify all three edges. No replacement of a restricted right input is required. For a single refinement, take \(A_j=S_gA_i\) and \(a_g=1\); for all refinements of an arbitrary initial \(A\) simultaneously, use the coslice category \(i/K\). Its object \(g:i\to j\) has input \(A_g=S_gA\), and an arrow \(h\) has comparison \(\widehat m_{h,g,A}:S_hS_gA\to S_{hg}A\). Their coherence is the pentagon already checked. Thus no existence of an unrelated global family of \(A_i\)'s is assumed. For \(A_i=P_i\), this is exactly the \(a,b,d\) subdiagram of (B.RT6). The arbitrary left triangle and the paired triangles agree on their actual overlap.

For completeness the refinement unit comparison itself has a joint target, not just its edge calculation. Fix h-projective \(L\) over \(\mathcal C_i\), put \(N_1=T_iL\), \(N_2=T_jS_gL\), and retain \(c_{g,L}:N_2\to N_1\). Use the five vertices \(L,U_iN_1,S_gL,U_jN_2,U_jN_1\), in fibres \(\mathcal C_i,\mathcal C_i,\mathcal C_j,\mathcal C_j,\mathcal C_j\). Their edges are the unit \(\eta^i\), the induction identity, \(k_{g,N_1}\), \(\eta^j\), and \(U_jc_{g,L}\), exactly as in (B.JT2). The two paths have fibre functor \(G_g\), and their target relation is (B.CR9); it does not require \(F_jG_g=F_i\). Include the two input rows \(U_iN_r,U_jN_r\), their \(k_{g,N_r}\) edges and the maps induced by \(c_{g,L}\). Naturality of \(k\) proves the additional square relation. One resolution of this combined presentation gives
\[
a_1S_gu_i=z_j u_j\lambda,
\qquad z_ja_2=a_1S_gz_i.
\tag{B.RT9}
\]
Here \(u_i:R_L\to P_i(N_1)\), \(u_j:R_{S_gL}\to P_j(N_2)\), \(\lambda:S_gR_L\to R_{S_gL}\) is the induction-identity comparison, and \(z_i,z_j\) lift the maps induced by \(c_{g,L}\). All domains are thereby fixed. The maps \(\lambda,z_i,z_j,a_1,a_2\) are homotopy equivalences by the same arguments as (B.JT3), (B.RT3), and two-out-of-three for the isomorphism \(c\). The units themselves need not be equivalences. If these \(q_i\)'s are used as the initial inputs of the paired targets, keep their now-exact \(u,a,z,\lambda\) maps as target maps before forming the combined presentation. This gives an explicit two-stage construction, with comparison to the first stage by (B.JT10), not a circular choice of replacements. The unit target and the paired/left targets can then be included in one presentation as in B.1w; only the displayed checked relations are imposed.

**Coherent comparisons of the resolved targets.** Successive \(\tau_g\)'s above compose through a natural isomorphism \(\gamma_{h,g}:\tau_h\tau_g\to\tau_{hg}\). Its components are \(m_{h,g}\) on the \(\mathcal C\)-fibres and identities on the \(\mathcal D\)-fibres. Naturality on the crossing edges is the stated compatibility of \(\beta\) with \(m\); the pentagon is that of \(m\). The target maps of (B.RT6) satisfy (B.RT2) for this \(\gamma\), by (B.RT3), (B.RT4) and naturality of \(k\). The left-target maps do also. Hence these are supplied coherent target diagrams, with their actual comparison isomorphisms.

Here is the precise extension of the graph lift when the index composition is not literal. For a resolution \(\rho_s:Q_s\to M_s\) of each whole transport module, use (B.TD10)'s triples \((v,a,H)\) over \(g:s\to t\). Their differential is unchanged. For a degree-\(m\) triple \((w,b,K)\) over \(h:t\to r\), the composite over \(hg\) is
\[
\left(
(\gamma^*_{M_r})^{-1}\tau_g^*(w)v,
(\gamma^*_{Q_r})^{-1}\tau_g^*(b)a,
(\gamma^*_{M_r})^{-1}
 \bigl(\tau_g^*(K)a+(-1)^m\tau_g^*(w)H\bigr)
\right).
\tag{B.RT10}
\]
The inverse occurs because \(\gamma^*\) goes from \(\tau_{hg}^*\) to \(\tau_g^*\tau_h^*\). Its naturality with \(\rho_r\), closedness, and the pentagon reduce the differential, Leibniz and associativity checks to those of (B.TD10)–(B.TD11). Projection to \(v\) is degreewise surjective and has, in each fixed label, the same acyclic shifted-cone kernel as before: \(Q_s\) is h-projective and \(\tau_g^*\rho_t\) is an objectwise quasi-isomorphism. No preservation of h-projectivity by \(\tau_g^*\) enters.

The supplied target maps give a strict functor from \(kK\) into this isomorphism-corrected target category. Lift its normalized word category \(U(kK)\) within each transport label, as in (B.ND9). Every differential has only shorter-word split and merge terms with the same composite label. Thus the lift exists in all lengths, respects units, and has, for example,
\[
\begin{aligned}
\tau_g^*(\rho_t)A_g-b_g\rho_s&=\partial H_g,\qquad \partial A_g=0,\\
\partial A_{h,g}
 &=(\gamma^*_{Q_r})^{-1}\tau_g^*(A_h)A_g-A_{hg}.
\end{aligned}
\tag{B.RT11}
\]
Higher identities follow from the same dg functor, not from independent choices of homotopies. The relative free-subdiagram form preserves earlier specified lifts where its hypotheses hold. Additional quotient relations require their checked target relations; none are inferred from acyclicity alone.

The maps \(A_g\) are objectwise quasi-isomorphisms since their target maps \(b_g\) are. On a \(\mathcal C\)-fibre their pulled-back targets may fail to be h-projective, so it would be wrong to call those components homotopy equivalences before changing fibres. Instead take the actual induction adjoint
\[
\overline A_g=\epsilon^{G_g}_{Q_t}S_gA_g:S_gQ_s\longrightarrow Q_t,
\qquad G_g^*\overline A_g\,\eta^{G_g}_{Q_s}=A_g.
\tag{B.RT12}
\]
Equation (B.SM2), or its displayed unit/detection proof, makes \(\overline A_g\) a quasi-isomorphism between h-projectives, hence a homotopy equivalence. On identity \(\mathcal D\)-fibres the same conclusion is immediate. It is these adjoint fibre comparisons to which further induction may safely be applied. The higher equations are retained under this adjunction: balanced-tensor associativity identifies the adjoint of \(\tau_g^*A_h A_g\), with its \(\gamma\) correction, with the composite of the induction adjoints and the specified induction associator. Adjunction is an isomorphism of Hom complexes, so it preserves their differentials and the signs in (B.RT11). This resolves the projectivity issue without assuming that arbitrary restriction preserves it.

The natural-family version uses the product fibres of B.1u and makes the initial family h-projective there before evaluation. Quasi-equivalence of the refinement functors survives those products by (B.ND3). The whole-module resolutions, target relations and graph kernels above then apply to that family, including its homogeneous maps. This is not a pointwise choice promoted to strict naturality.

**Geometric binding and limit.** For actual compactifications use \(G_h\) of (B.CR2), \(m\) of (B.CR4), and \(\beta_h\) of (B.CR5). Their quasi-equivalence, closedness and canonical coherences were proved there; all hypotheses used above are present. The same argument applies to each fixed-endpoint strict model in the refinement arrays (B.GC5)–(B.GC6) when its specified output isomorphism is retained. It supplies the actual adjunction-target comparisons for those refinements, not merely fixed-choice homotopies. The remaining work is to place these maps together with the two-morphism common-span mate diagrams, the higher folding roofs and the geometric base-change/composition interchange cells. Those additional maps need not be quasi-equivalences of the fibres, so (B.RT12) is not a blanket assertion about them. Full enhanced geometric coherence, nearby attaching, normalized coefficient transport remain open. \(\square\)



### Normalize the refinement array before folding

**Proposition B.1z (one model for the refinement and fold roof).** The proper-refinement array of the two-open composition model (B.GC4) admits a simultaneous normalization in which the refinement arrows and the strict folding roofs commute strictly. Evaluation returns the original models together with their specified canonical isomorphisms. All higher folding coefficients and the original source and proper-output functors are retained. This fills the strict-outer-diagram hypothesis of (B.SF9) for this array; it does not yet identify the entire geometric composition/base-change adjunction diagram.

**Objects remember their origin.** Use the normalized pseudofunctor data \((\mathcal C_i,G_g,m_{h,g})\) of (B.RT1), indexed by a small category \(K\). Define a dg category \(\widehat{\mathcal C}_i\) whose objects are pairs \((u,X)\), where \(u:a\to i\) is an arrow of \(K\) and \(X\in\mathcal C_a\). Different pairs remain different objects, even when their evaluations agree. Put
\[
\begin{aligned}
\widehat{\mathcal C}_i((u,X),(v,Y))
 &=\mathcal C_i(G_uX,G_vY),\\
E_i(u,X)&=G_uX.
\end{aligned}
\tag{B.SN1}
\]
Differentials and composition are exactly those on the right. Evaluation \(E_i\) is an isomorphism on every Hom complex. It is essentially surjective, since \((1_i,X)\) evaluates to \(X\); hence it is a quasi-equivalence. This is not a restriction of objects to a selected refinement image.

For \(g:i\to j\), define
\[
\widehat G_g(u,X)=(gu,X),\qquad
\widehat G_g(f)=m_{g,v,Y}G_g(f)m_{g,u,X}^{-1}.
\tag{B.SN2}
\]
Every factor \(m\) is closed of degree zero. Thus the formula preserves differentials, units and composition. For successive \(g,h\), the pentagon says
\[
m_{h,gv}G_h(m_{g,v})
 =m_{hg,v}(m_{h,g}G_v).
\tag{B.SN3}
\]
Insert this equality at both ends of \(\widehat G_h\widehat G_g(f)\), and use naturality of \(m_{h,g}\) on \(f\). The middle expression becomes \(G_{hg}(f)\), proving \(\widehat G_h\widehat G_g=\widehat G_{hg}\) on objects and all homogeneous maps. The identity functor is literal. The maps \(m_{g,u,X}\) give the closed natural isomorphism \(G_gE_i\to E_j\widehat G_g\); (B.SN3) is precisely its composition coherence. In particular, if \(G_g\) is a quasi-equivalence, so is \(\widehat G_g\), by evaluation and Hom two-out-of-three. No inverse to \(G_g\) was selected.

**Normalize the fixed output at the same time.** Suppose \(F_i:\mathcal C_i\to\mathcal D\) and \(\beta_g:F_jG_g\to F_i\) satisfy (B.RT3)'s stated output coherence. On the same origin-labelled objects define
\[
\widehat F_i(u,X)=F_aX,\qquad
\widehat F_i(f)=\beta_{v,Y}F_i(f)\beta_{u,X}^{-1}.
\tag{B.SN4}
\]
This is a dg functor by cancellation of the middle inverse factors. The components \(\beta_{u,X}:F_iE_i(u,X)\to\widehat F_i(u,X)\) are a closed natural isomorphism. The actual identity

\[
\beta_{gu}F_j(m_{g,u})=\beta_u(\beta_gG_u)
\tag{B.SN5}
\]
makes \(\widehat F_j\widehat G_g=\widehat F_i\) strictly: substitute (B.SN2) in (B.SN4), use (B.SN5) at both ends, and move \(\beta_g\) across \(F_jG_g(f)\) by naturality. The output of an object is its original \(F_aX\), so object equality also holds. One may do this for several fixed endpoint outputs at once. These are conjugated models, not declarations that the original direct-image isomorphisms were identities.

**Horizontal maps and the extra requirement for a higher map.** Let a second pseudofunctor have fibres \(\mathcal D_i\), refinement functors \(H_g\), and associators \(n_{h,g}\). For strict dg functors \(P_i:\mathcal C_i\to\mathcal D_i\), suppose the specified closed natural isomorphisms \(\alpha_g:P_jG_g\to H_gP_i\) obey
\[
\alpha_{hg}P_k(m_{h,g})
 =(n_{h,g}P_i)(H_h\alpha_g)(\alpha_hG_g).
\tag{B.SN6}
\]
Define \(\widehat P_i(u,X)=(u,P_aX)\) and \(\widehat P_i(f)=\alpha_vP_i(f)\alpha_u^{-1}\). Equation (B.SN6) and naturality give \(\widehat P_j\widehat G_g=\widehat H_g\widehat P_i\) strictly, by the same two-end cancellation. This construction preserves a composite \(QP\) exactly when its comparison is the specified composite \(\alpha^Q_uP_a\circ Q_i\alpha^P_u\). Consequently a strictly commuting horizontal square with equal composite comparisons remains a strictly commuting square. An arbitrary incoherent choice of four comparisons is not enough.

For a strictly unital higher functor \(L_i:\mathcal C_i\to\mathcal D_i\), replace naturality by the actual all-arity identities
\[
\alpha_{g,X_r}L_{j,r}(G_gf_r,\ldots,G_gf_1)
 =H_gL_{i,r}(f_r,\ldots,f_1)\alpha_{g,X_0}.
\tag{B.SN7}
\]
Here the object components of \(\alpha_g\) are actual closed invertible arrows, and (B.SN6) uses \(L_{k,1}(m_{h,g})\). There is one more condition: for the designated closed object isomorphisms \(\sigma_b\) occurring in the associators, their images must be closed invertible arrows and
\[
L_r(\sigma_r f_r\sigma_{r-1}^{-1},\ldots,
       \sigma_1f_1\sigma_0^{-1})
 =L_1(\sigma_r)L_r(f_r,\ldots,f_1)L_1(\sigma_0)^{-1}.
\tag{B.SN8}
\]
This equivariance is automatic for a strict functor but is not inferred for an arbitrary higher functor. In particular it is not a new assertion that \(Q\) acts functorially on arbitrary higher maps or natural transformations.

Under these hypotheses the normalized higher functor is given in every arity by
\[
\begin{aligned}
\widehat L_i(u,X)&=(u,L_aX),\\
\widehat L_{i,r}(f_r,\ldots,f_1)
 &=\alpha_{u_r,X_r}L_{i,r}(f_r,\ldots,f_1)
          \alpha_{u_0,X_0}^{-1}.
\end{aligned}
\tag{B.SN9}
\]
It has degree \(1-r\). Closedness of the outer factors preserves internal differential terms of (B.RS8); in split terms the two factors at the intermediate object cancel; merge terms retain the original composition of \(f\)'s. This proves all higher identities with the same signs. Strict units are preserved. To check strict refinement compatibility, substitute (B.SN2) in (B.SN9). First apply (B.SN8) to the \(m_{g,u_b}\), then (B.SN7), and finally (B.SN6) for the pair \(g,u_b\). The resulting outer factors are \(n_{g,u_r}H_g(\alpha_{u_r})\) and its initial-end inverse. They are exactly the formula for \(\widehat H_g\widehat L_{i,r}\). Thus
\[
\widehat L_{j,r}(\widehat G_gf_r,\ldots,\widehat G_gf_1)
 =\widehat H_g\widehat L_{i,r}(f_r,\ldots,f_1)
\tag{B.SN10}
\]
is equality for every arity, not only for \(r=1\). Evaluation compares \(\widehat L\) with \(L\) through the displayed \(\alpha_u\), retaining (B.SN7). If \(L_1\) is Hom-quasi-isomorphic and essentially surjective on \(H^0\), the same is true of \(\widehat L_1\): its Hom maps are conjugates of those of \(L_1\); essential surjectivity follows using \(E_i\), \((1_i,X)\), and the isomorphisms \(\alpha_u\).

**Why the actual folding coefficients satisfy the extra condition.** An isomorphism of resolution strings with closed invertible vertex maps \(\sigma_b\) and zero edge homotopies sends a homogeneous edge homotopy \(h_b\) to

\[
h_b\longmapsto\sigma'_b h_b J_b(\sigma_{b-1}^{-1}),
\qquad
q_b\longmapsto\sigma_b q_b J_b(\sigma_{b-1}^{-1}).
\tag{B.SN11}
\]
The endpoint maps transform by ordinary conjugation. The zero edge homotopies and the string equations prove this by the signed composition rule of B.1o. In every selected-edge word defining \(W_r\), adjacent \(\sigma^{-1}\sigma\) cancel, also after transport by the exact \(J_b\)'s. What remains is the final vertex factor and the transported inverse initial factor. This proves (B.SN8) for each word separately, hence their sum, for all string lengths and arities. The factors have degree zero, so no bar sign changes. The first folding coefficient includes the two transformed endpoint maps; higher coefficients have zero endpoints. Folding a designated zero-homotopy isomorphism gives the graph isomorphism with these endpoints and zero homotopy, whose inverse is the fold of the inverse. This verifies the invertibility requirement as well.

Apply this to the actual proper-image associators of (B.CR4) in the string transfers (B.GC6). Their graph components have zero edge homotopies. The ordered-exchange identity (B.RS12) supplies (B.SN7) for every coefficient; (B.GC5) identifies the exchange edges, and the canonical proper-image pentagon and exchange pasting supply (B.SN6). The strict exchange functor \(E\) of (B.GC3) satisfies the strict-functor version; the equality with refinement on its second edge and its homogeneous homotopy component was checked explicitly after (B.GC6). Thus the hypotheses are checked on the actual composition roof, rather than postulated for an unrelated higher functor.

**A strict roof of the whole normalized refinement diagram.** At refinement index \(i\), write \(\widehat{\mathcal R}_i\) for the normalized two-open string category, \(\widehat{\mathcal L}_i\) for the normalized iterated-composition graph, and \(\widehat{\mathcal G}_i\) for the normalized single-open graph. Let \(\widehat C_i\) be the normalized higher fold and \(\widehat E_i:\widehat{\mathcal R}_i\to\widehat{\mathcal L}_i\) the normalized strict exchange. Form
\[
\begin{array}{ccccc}
&&UQ\widehat{\mathcal R}_i&&\\
&{\scriptstyle e_i}\swarrow&&\searrow{\scriptstyle h_{\widehat C_i}}&\\
\widehat{\mathcal R}_i&&&&\widehat{\mathcal G}_i\\
{\scriptstyle\widehat E_i}\downarrow&&&&\\
\widehat{\mathcal L}_i.&&&&
\end{array}
\tag{B.SN12}
\]
All three arrows are strict quasi-equivalences: evaluation proves the claim for \(\widehat E_i\), and (B.SF7) proves it for \(e_i\) and \(h_{\widehat C_i}\). Refinement on the upper vertex is \(UQ\widehat G_g\), using only a strict dg functor. Equations (B.SN10) and (B.SF9) prove that both slanted edges commute with it strictly; the strict-functor case proves the same for \(\widehat E_i\). The upper refinement is a quasi-equivalence by two-out-of-three in its commuting square with \(e_i,e_j\) and \(\widehat G_g\). Refinement composition on the upper vertex is literal by functoriality of \(UQ\). No lift of an original \(m_{h,g}\) through \(Q\) is required: those maps have already been accounted for by (B.SN2)–(B.SN3) before \(Q\) is applied.

There are fixed endpoint outputs to the original source enhancement and to the final proper-target enhancement. Here is the required compatibility explicitly. Write \(O_i:\mathcal C_i\to\mathcal E\) and \(V_i:\mathcal D_i\to\mathcal E\), with \(V_iL_{i,1}=O_i\), \(V_iL_{i,r}=0\) for \(r>1\), and output comparisons \(b_g:O_jG_g\to O_i\), \(c_g:V_jH_g\to V_i\). The condition and its normalized consequence are
\[
\begin{aligned}
b_g&=(c_gL_i)V_j(\alpha_g),\\
\widehat V_i\widehat L_{i,1}&=\widehat O_i,\qquad
\widehat V_i\widehat L_{i,r}=0\quad(r>1).
\end{aligned}
\tag{B.SN13}
\]
Indeed, substitute (B.SN9) in (B.SN4). Its value on an \(r\)-tuple is \(b_{u_r}V_iL_{i,r}(f_r,\ldots,f_1)b_{u_0}^{-1}\). This is the required normalized output for \(r=1\) and is zero for \(r>1\); object equality is \(V_aL_aX=O_aX\). In the actual composition array the outputs are the first and final vertex projections followed, for the latter, by the specified proper direct images. The first-component comparison is the identity at the protected original source. At the proper output, the first line of (B.SN13) equates the two canonical reassociations of the same ordered proper images; it is their composition pentagon from (B.CR4)–(B.CR5), used in (B.GC4)–(B.GC6). The designated graph comparisons have zero edge homotopies, and the higher folding components have zero endpoints. This verifies all the stated output hypotheses. Equation (B.SF8) now makes both paths through (B.SN12) have literally equal fixed endpoint outputs. Evaluation back to the geometric models retains, rather than erases, the original proper-image comparison maps.

This gives a concrete simultaneous adjunction target model for this roof and its refinements. Take the category presented by the refinement arrows, the three arrows in (B.SN12), and their checked commuting faces. Its fibre categories and functors form a strict diagram; all its arrows are quasi-equivalences, and the normalized final output is constant along them. Apply (B.RT1)–(B.RT4) with \(m=\beta=1\) to a right input \(N\). A single module resolution supplies all \(q\)'s and all comparison maps, with the exact counit identities simultaneously. Equations (B.RT5)–(B.RT12) then supply the paired triangles, arbitrary left-input triangles along each coslice, the unit target and their labelled higher resolution comparisons. Include the checked boundary presentations before resolving, as in B.1w and (B.RT9); do not choose incompatible lifts separately for the two slanted legs. The induction adjoints are homotopy equivalences because every fibre arrow of this roof/refinement diagram is a quasi-equivalence. This claim does not extend to arbitrary horizontal geometric or base-change functors.

The construction is not yet the comparison with the two-stage adjunction on the intermediate category. That requires the actual common-span mate targets of B.1s and B.1w, their intermediate input modules, and the base-change/interchange maps. Nearby attaching, multiplicative descent, normalized coefficient transport also remain open. The normalization just proved removes the roof-level strictness gap without treating these further statements as automatic. \(\square\)



### Join the intermediate adjunction to the composition roof

**Proposition B.1aa (the actual two-stage adjunction).** The common-span square in (B.SM13) identifies the two-stage adjunction with the common-span adjunction, including their mapping complexes, actual units and counits, and both triangle homotopies. This comparison joins the fixed composition roof of (B.SN12); it is not merely an isomorphism of the resulting objects. The construction works over an arbitrary commutative coefficient ring with possibly unbounded dg modules. Horizontal functors are not assumed to be quasi-equivalences.

Use the notation
\[
\begin{array}{ccccc}
\mathcal A&\xrightarrow{\ \beta\ }&\mathcal C&
       \xrightarrow{\ G\ }&\mathcal E\\
{\scriptstyle\alpha}\downarrow&&\downarrow{\scriptstyle p}&&\\
\mathcal B&\xrightarrow{\ F\ }&\mathcal D,&&
\end{array}
\qquad p\beta=F\alpha .
\tag{B.IA1}
\]
Only \(\alpha,p\) are required to be quasi-equivalences. The arrows depict the actual functors, not inverses chosen in a derived category. Write \(C_Q:p_!\beta_!Q\to F_!\alpha_!Q\) for (B.SM4)'s balanced induction isomorphism and \(b,d\) for (B.SM5)'s two mates. Keep the right-module conventions and the induction/restriction units and counits of B.1l.

**Synchronized models cover every source object.** For an h-projective \(\mathcal A\)-module \(Q\), put \(M=\alpha_!Q\), \(P=\beta_!Q\), and \(L=G_!P\). These are h-projective. The particular replacement needed by the second stage is
\[
\begin{aligned}
r_Q&=p^*C_Q\,\eta^p_P:
       P\longrightarrow p^*F_!M,\\
r_Q&=b_M\beta_!\eta^\alpha_Q .
\end{aligned}
\tag{B.IA2}
\]
The second equality is (B.SM6); the first makes \(r_Q\) a quasi-isomorphism by (B.SM1). Thus the two-stage left object is literally \(G_!\beta_!Q\), canonically identified by balanced tensors with \((G\beta)_!Q\). This is not an assumption that the unresolved \(b_M\) is invertible.

There is no loss of source scope in using \(M=\alpha_!Q\). For h-projective \(Q,Q'\), adjunction identifies the map on Hom complexes induced by \(\alpha_!\) with \(\operatorname{Hom}(Q,\eta^\alpha_{Q'})\), a quasi-isomorphism. For arbitrary h-projective \(M_0\), choose \(Q\to\alpha^*M_0\); its adjoint \(\alpha_!Q\to M_0\) is a homotopy equivalence by (B.SM2). Consequently \(\alpha_!:\operatorname{HP}(\mathcal A)\to\operatorname{HP}(\mathcal B)\) is a quasi-equivalence. This proves coverage of all h-projective source modules, not just modules already in a selected right-adjoint image.

For an h-projective \(\mathcal E\)-module \(Y\), choose h-projective replacements \(r:R\to G^*Y\) over \(\mathcal C\) and \(t:Z\to\beta^*R\) over \(\mathcal A\). Set
\[
\begin{aligned}
q_Y&=\beta^*r\,t:Z\longrightarrow(G\beta)^*Y,\\
W_Y&=\alpha_!Z,\\
s_Y&=d_R\alpha_!t:W_Y\longrightarrow F^*p_!R .
\end{aligned}
\tag{B.IA3}
\]
Both \(q_Y\) and \(s_Y\) are quasi-isomorphisms, the latter by (B.SM9), not by assuming \(d_R\) invertible. Thus \(W_Y\) is simultaneously the common-span right model and an actual replacement in the sequential right model. No restriction functor is claimed to preserve h-projectivity.

**The pairing agrees as a map of complexes.** For every homogeneous \(a:P=\beta_!Q\to R\), its adjoint is \(a^\flat=\beta^*a\,\eta^\beta_Q\). Naturality of \(d\) and the first identity of (B.SM7) give the exact equality
\[
\begin{aligned}
d_R\alpha_!(a^\flat)
 &=F^*(p_!a\,C_Q^{-1})\,\eta^F_M,\\
\operatorname{Adj}_F\!\left(d_R\alpha_!(a^\flat)\right)
 &=p_!a\,C_Q^{-1}.
\end{aligned}
\tag{B.IA4}
\]
All displayed structural maps have degree zero, so this equality holds for arbitrary homogeneous \(a\), with no additional degree sign. In particular, if \(f:Q\to Z\), apply it to \(a=\operatorname{Adj}_\beta(tf)\).

Here are the two mapping-complex routes. They share
\(\operatorname{Hom}_{\mathcal E}(G_!P,Y)
 \cong\operatorname{Hom}_{\mathcal C}(P,G^*Y)
 \longleftarrow\operatorname{Hom}_{\mathcal C}(P,R)\).
The common-span route then uses
\[
\begin{array}{ccccc}
\operatorname{Hom}_{\mathcal C}(P,R)&\cong&
\operatorname{Hom}_{\mathcal A}(Q,\beta^*R)&
\longleftarrow&\operatorname{Hom}_{\mathcal A}(Q,Z)\\
&&&&\downarrow{\scriptstyle\alpha_!}\\
&&&&\operatorname{Hom}_{\mathcal B}(M,W_Y).
\end{array}
\tag{B.IA5}
\]
The sequential route sends \(a\) to \(p_!a\,C_Q^{-1}\) in
\(\operatorname{Hom}_{\mathcal D}(F_!M,p_!R)\), uses the \(F\)-adjunction, and compares with
\(\operatorname{Hom}_{\mathcal B}(M,W_Y)\) by postcomposition with \(s_Y\).
Equation (B.IA4) makes the resulting comparison square commute on the nose. Every arrow in these zigzags is a quasi-isomorphism: use h-projectivity for \(r,t,s_Y\), and the just-proved Hom assertion for the quasi-equivalences \(p_!,\alpha_!\). This establishes the same mapping-complex pairing, rather than appealing to uniqueness of adjoints only on \(H^0\).

**Unit and its actual witnesses.** At \(Y=L=G_!P\), choose closed maps \(u:P\to R_L\), \(a:Q\to Z_L\), and degree-minus-one maps \(k,h\) with
\[
\begin{aligned}
r_Lu-\eta^G_P&=dk,\\
t_La-\beta^*u\,\eta^\beta_Q&=dh .
\end{aligned}
\tag{B.IA6}
\]
The Hom quasi-isomorphisms out of \(P,Q\) supply these choices. The shared unit on the \(\mathcal B\)-model is \(\alpha_!a:M\to W_L\). Define
\(\omega_Q=F^*(p_!u\,C_Q^{-1})\eta^F_M\). Equations (B.IA4) and (B.IA6) give
\[
\begin{aligned}
s_L\alpha_!a-\omega_Q
 &=d\!\left(d_{R_L}\alpha_!h\right),\\
q_La-\eta^{G\beta}_Q&=d\ell_Q,\\
\ell_Q&=\beta^*r_L\,h+\beta^*k\,\eta^\beta_Q .
\end{aligned}
\tag{B.IA7}
\]
Here \(\eta^{G\beta}_Q=\beta^*\eta^G_{\beta_!Q}\eta^\beta_Q\), with the balanced induction identification retained. The first line is the sequential unit witness; the other lines are the common-span unit witness. Units need not be quasi-isomorphisms.

**Counit, including the intermediate map.** Put
\(v_Y=\varepsilon^\beta_R\beta_!t:\beta_!Z\to R\). Then both counits are represented by the same map
\[
\begin{aligned}
e_Y&=\varepsilon^G_Y\,G_!r\,G_!v_Y:
         G_!\beta_!Z\longrightarrow Y,\\
e_Y&=\varepsilon^{G\beta}_Y(G\beta)_!q_Y,\\
\varepsilon^F_{p_!R}F_!s_Y\,C_Z&=p_!v_Y .
\end{aligned}
\tag{B.IA8}
\]
The last line follows from the second identity of (B.SM7) and naturality of \(C\). It identifies the actual intermediate counit, before passing through the \(p\)-equivalence. Thus that passage is represented by \(v_Y\) itself, not by an unspecified inverse on cohomology. The first two lines follow by composing the two ordinary induction/restriction counits. There is no claim that \(v_Y\) or \(e_Y\) is invertible.

For the left triangle, put \(w=\varepsilon^\beta_{R_L}\beta_!h\). Naturality and the ordinary \(\beta\)-triangle give \(v_L\beta_!a-u=dw\). Applying the \(G\)-triangle yields the full witness
\[
e_L\,G_!\beta_!a-1_L
 =d\!\left(\varepsilon^G_L\,G_!(r_Lw+k)\right).
\tag{B.IA9}
\]
This is a triangle at arbitrary \(Q\); the coverage argument above transports it to every source object. Neither induction of an arbitrary quasi-isomorphism nor contractibility of an arbitrary acyclic module was used.

**The nested right-resolution graph is not strictly folded.** Retain the objects \((Y,R,Z;r,t)\) of (B.IA3). A degree-\(n\) map has vertex maps \((f,\rho,z)\) and edge maps \(k,h\) of degree \(n-1\). Its differential on the edges is
\[
\begin{aligned}
Dk&=r'\rho-G^*f\,r-dk,\\
Dh&=t'z-\beta^*\rho\,t-dh .
\end{aligned}
\tag{B.IA10}
\]
Vertex differentials are ordinary Hom differentials. For a degree-\(m\) map \(S\) after \(T\), the edge components of their composite are
\(k_S\rho_T+(-1)^mG^*f_Sk_T\) and
\(h_Sz_T+(-1)^m\beta^*\rho_Sh_T\).
Associativity, the Leibniz rule and \(D^2=0\) follow from these formulas as in (B.RS2).

The sequential right-resolution map is a **strict** dg functor:
\[
(f,\rho,z;k,h)\longmapsto
       (p_!\rho,\alpha_!z,d_{R'}\alpha_!h)
\tag{B.IA11}
\]
to the graph of \(s_Y:W_Y\to F^*p_!R\). For example, its differential identity is
\(s_{Y'}\alpha_!z-F^*p_!\rho\,s_Y
 =d_{R'}\alpha_!(t'z-\beta^*\rho\,t)\);
its signed composition identity follows by homogeneous naturality of \(d\). Thus the strict claim has been checked, not inferred from a commutative square on objects.

In contrast, the comparison with the graph of \(q_Y:Z\to(G\beta)^*Y\) is the higher fold of the two-edge string
\(Z\to\beta^*R\to\beta^*G^*Y\).
In exactly the suspended convention of (B.RS7), its coefficients are
\[
\begin{aligned}
K_1(T)&=(f_T,z_T,H_T),&
H_T&=\beta^*r'\,h_T+\beta^*k_T\,t,\\
K_2(S,T)&=(0,0,\beta^*k_S\,h_T),&
K_j&=0\quad(j>2).
\end{aligned}
\tag{B.IA12}
\]
The triples here are ordered as (target vertex, replacement vertex, witness), as in B.1l. The selected-edge proof of (B.RS8) applies purely algebraically; its cancellation does not require the intermediate module \(\beta^*R\) to be h-projective. It proves all higher identities, including the three-input identity involving \(K_2\). The ordinary multiplicativity homotopy has the sign \((-1)^{|S|+1}K_2(S,T)\). Omitting \(K_2\) is generally false. Inserting an identity makes every higher coefficient vanish, since its edge witnesses are zero.

Projection of the nested graph to \(\operatorname{HP}(\mathcal E)\) is a Hom-surjective quasi-isomorphism. To prove it, forget the \(Z,t,h,z\) data first. The kernel on Hom complexes is the shifted cone of
\(\operatorname{Hom}_{\mathcal A}(Z,Z')\to
 \operatorname{Hom}_{\mathcal A}(Z,\beta^*R')\),
induced by \(t'\), hence acyclic. The remaining projection has kernel the analogous cone induced by \(r'\), with h-projective source \(R\). Both projections are surjective on graded Hom groups, and replacements exist for every object. The common graph projects to the same category by the same argument with \(q_Y\). Since \(K_1\) commutes with projection, it is a Hom quasi-isomorphism. Every common-graph object is isomorphic in \(H^0\) to the image of a nested object over the same \(Y\): lift \(1_Y\) through the common graph's Hom quasi-isomorphism and lift its inverse in the reverse direction. Thus \(K\) is essentially surjective as well.

Apply (B.SF7) to obtain a strict quasi-equivalence roof from \(UQ\) of the nested graph to the nested and common graphs. Both the input \(Y\) and right output \(\alpha_!Z\) commute strictly along this roof: their projections send \(K_2\) to zero and have the same \(K_1\) values. This supplies the coherent comparison for homogeneous parameter maps; independent pairwise choices of \(k,h\) would not do so.

**Right triangle on the same models.** At \(Y\), apply the unit construction to \(Q=Z_Y\), so its source is \(L_W=G_!\beta_!Z_Y\). Lift the closed counit \(e_Y:L_W\to Y\) through the nested graph, obtaining \((e_Y,\rho_e,z_e;k_e,h_e)\); the preceding Hom quasi-isomorphism supplies the lift. Put
\(H_e=\beta^*r_Yh_e+\beta^*k_e t_{L_W}\). The common graph equation and (B.IA7) give
\[
q_Y(z_ea_{Z_Y}-1_{Z_Y})
 =d\!\left(H_ea_{Z_Y}+(G\beta)^*e_Y\,\ell_{Z_Y}\right).
\tag{B.IA13}
\]
In deriving this identity use
\((G\beta)^*e_Y\,\eta^{G\beta}_{Z_Y}=q_Y\), the ordinary counit identity for the adjoint of \(q_Y\). The defect \(z_ea_{Z_Y}-1\) is closed. Since \(\operatorname{Hom}(Z_Y,q_Y)\) is a quasi-isomorphism, that defect equals \(dJ\) for some degree-minus-one \(J\). Then \(\alpha_!J\) proves the sequential and common right triangle on \(W_Y\). This argument asserts a boundary, not the unjustified stronger equation that \(q_YJ\) equals the displayed witness.

For parameter diagrams, use the whole-diagram resolutions of B.1v before evaluation. Include (B.IA4), (B.IA8), the unit equations and the two displayed triangle witnesses in their actual target presentation. They are checked relations, not new relations imposed without proof. The Hom-surjective acyclic-kernel argument of (B.ND9) lifts a free dg indexing resolution relative to already chosen faces; the strict roof just constructed retains (B.IA12) on its free words. It does not turn arbitrary higher coherence relations into consequences of separately chosen homotopies.

**Insert the actual geometric intermediate category.** For (B.GC2), take
\[
\begin{aligned}
(\mathcal A,\mathcal B,\mathcal C,\mathcal D)
 &=(\mathcal L_{g,f},\mathcal C_f,\mathcal C_g,\mathcal I_Y),\\
(\alpha,\beta,p,F,G)
 &=(\alpha,\beta,\pi_g,F_f,F_g),\\
\pi&=\pi_f:\mathcal C_f\longrightarrow\mathcal I_X .
\end{aligned}
\tag{B.IA14}
\]
Here \(\alpha(c,N,t)=c\) and
\(\beta(c,N,t)=(F_fc,N,t)\); hence \(p\beta=F\alpha\) literally. The actual two-stage left functor is \(LG_!\,p^*\,LF_!\,\pi^*\), and the common-span functor is \(L(G\beta)_!(\pi\alpha)^*\), with h-projective replacements understood as above. On the full family of source models \(\pi_!\alpha_!Q\), use \(\eta^\pi_{\alpha_!Q}\) for the first inverse-equivalence replacement and (B.IA2) for the second. The two left models are then \(G_!\beta_!Q\). Their right model is \(\pi_!\alpha_!Z_Y\), their unit is \(\pi_!\alpha_!a\), and their counit is (B.IA8). Induction by \(\pi\) transports the right-triangle witness; the left witness remains (B.IA9). Since \((\pi\alpha)_!\) is a quasi-equivalence on h-projectives, these source models cover every object of the original source enhancement.

**Join, rather than replace, the strict composition roof.** A leg of (B.SN12), followed by evaluation, gives a strict quasi-equivalence \(j:\mathcal V\to\mathcal A\). Its endpoint outputs are \((\pi\alpha)j,(G\beta)j\), after inserting the specified closed evaluation isomorphisms of (B.SN13). Their induction maps are the canonical balanced-tensor maps of (B.CR6)–(B.CR9), not discarded identifications. For fixed \(j\), use \(Q=j_!Q_0\) in the preceding construction. On the right choose \(\zeta:Z_0\to j^*Z_Y\), and write \(e_j=\varepsilon^j_{Z_Y}j_!\zeta:j_!Z_0\to Z_Y\). This is a homotopy equivalence by (B.SM2). If \(a:j_!Q_0\to Z_Y\) is the unit lift, lift its adjoint to \(a_0:Q_0\to Z_0\), with \(\zeta a_0-j^*a\,\eta^j_{Q_0}=dh_0\). The actual comparison identities are
\[
\begin{aligned}
e_jj_!a_0-a
 &=d\!\left(\varepsilon^j_{Z_Y}j_!h_0\right),\\
\varepsilon^{G\beta}_Y(G\beta)_!q_Y\,(G\beta)_!e_j
 &=\varepsilon^{(G\beta)j}_Y
        ((G\beta)j)_!(j^*q_Y\,\zeta).
\end{aligned}
\tag{B.IA15}
\]
The first follows by counit naturality and the \(j\)-triangle; the second is the composed-counit identity on balanced tensors. Apply \((\pi\alpha)_!\) to the first line for the source unit. The right output comparison is \((\pi\alpha)_!e_j\). These are the concrete maps that attach the intermediate adjunction to each roof leg. The joint unit, paired and arbitrary-left-triangle target constructions of B.1w–B.1y retain these maps and their witnesses across that roof; they induce only homotopy equivalences between h-projective replacements. The nested right comparison continues to use its \(K_2\) term.

The fixed intermediate-square comparison attaches to the normalized composition roof as above. It does **not** establish the geometric base-change/interchange target maps, compatibility of the entire intermediate square with every proper refinement, geometric nearby-cycle multiplicative descent, or completed coefficient transport. Those remaining arguments must use the actual maps above; they cannot be replaced by uniqueness of an ordinary adjoint or by declaring all horizontal functors equivalences.



### Transpose the actual base-change cells

**Proposition B.1ab (base-change mates and their resolved pasting).** The actual left-hand comparison in a strict common model determines a right-adjoint comparison with explicit unit, counit and composition witnesses. The construction does not require the vertical functors to be equivalences. An invertible left comparison does **not** imply that its right mate is invertible. We give the maps before and after h-projective replacement, and identify the precise cellwise input supplied by (B.GC12)–(B.GC13). Global descent across every change of geometric model is distinguished at the end.

Work over an arbitrary commutative coefficient ring with possibly unbounded modules. Let \(L_i:\operatorname{Mod}(\mathcal C_i)\to\operatorname{Mod}(\mathcal D_i)\) be balanced induction by a dg functor \(F_i\), with right adjoint \(U_i=F_i^*\). Let \(S,V\) be induction functors between the source and target module categories, respectively. In particular, they preserve h-projectives and homotopy equivalences, not necessarily arbitrary quasi-isomorphisms. Suppose a closed dg-natural map has been specified:
\[
\begin{array}{ccc}
\operatorname{Mod}(\mathcal C_0)&\xrightarrow{\ L_0\ }&
 \operatorname{Mod}(\mathcal D_0)\\
{\scriptstyle S}\downarrow&&\downarrow{\scriptstyle V}\\
\operatorname{Mod}(\mathcal C_1)&\xrightarrow{\ L_1\ }&
 \operatorname{Mod}(\mathcal D_1),
\end{array}
\qquad \theta:L_1S\longrightarrow VL_0 .
\tag{B.BM1}
\]
The arrow direction of \(\theta\) is part of the data. For geometric compact-support base change the usual comparison points the other way; its inverse in a common resolved model is the input here, with its homotopies retained. No inverse to a general vertical functor is being chosen.

**Transpose on the actual module categories.** Denote the ordinary units and counits of \(L_i\dashv U_i\) by \(\eta^i,\varepsilon^i\). Define
\[
\begin{aligned}
\mu_N:S U_0N&\longrightarrow U_1VN,\\
\mu_N
 &=U_1(V\varepsilon^0_N\,\theta_{U_0N})\,
       \eta^1_{S U_0N}.
\end{aligned}
\tag{B.BM2}
\]
This is a closed dg-natural map, since every factor is closed of degree zero. Its defining transposition and its unit identity are
\[
\begin{aligned}
\varepsilon^1_{VN}L_1\mu_N
 &=V\varepsilon^0_N\,\theta_{U_0N},\\
\mu_{L_0A}S\eta^0_A
 &=U_1\theta_A\,\eta^1_{SA}.
\end{aligned}
\tag{B.BM3}
\]
The first equality is the induction/restriction Hom-complex adjunction. For the second, move \(S\eta^0_A\) through \(\eta^1\), then move \(L_1S\eta^0_A\) through \(\theta\). The remaining middle product is
\(V(\varepsilon^0_{L_0A}L_0\eta^0_A)=1\).
This proves the identity as a module map. Homogeneous naturality follows by the same adjunction isomorphism; no homogeneous factor has been permuted.

Conversely, a closed natural \(\mu:SU_0\to U_1V\) has left mate
\(\varepsilon^1_{VL_0A}L_1(\mu_{L_0A}S\eta^0_A)\).
Inserting (B.BM2), using naturality and the two ordinary triangle identities, gives \(\theta_A\). In the reverse direction the same calculation gives \(\mu_N\). Thus an equality between actual left cells gives an equality between their actual right mates. This is a concrete transposition, not an inference from the dimensions of mapping spaces.

**Why invertibility must be checked separately.** Over a field \(k\), use the algebra square with \(F_0:k\to k\times k\) diagonal, \(F_1:k\to k\) the identity, \(S\) the identity, and \(V\) induction along the first projection \(k\times k\to k\). Then \(VL_0=L_1S=1\), so \(\theta=1\) is invertible. A right \(k\times k\)-module is a pair \((N_1,N_2)\), and the mate is
\[
\mu_{(N_1,N_2)}:
       N_1\oplus N_2\longrightarrow N_1,\qquad
       (x,y)\longmapsto x .
\tag{B.BM4}
\]
For \((N_1,N_2)=(0,k)\) it is \(k\to0\), not a quasi-isomorphism. All these modules are projective. The failure is therefore not caused by unresolved replacements or unboundedness. A geometric right-exchange isomorphism needs its own hypotheses; ordinary compact-support base change alone does not establish it.

**Resolve the right mate without inducing an unresolved quasi-isomorphism.** For h-projective \(N\), choose
\(r_0:P_0\to U_0N\) and \(r_1:P_1\to U_1VN\) with h-projective sources. Since \(SP_0\) is h-projective, there are a closed \(c_N:SP_0\to P_1\) and a degree-minus-one \(b_N\) with
\[
\begin{aligned}
r_1c_N-\mu_N S r_0&=db_N,\\
e^1_{VN}L_1c_N-Ve^0_N\,\theta_{P_0}
 &=d\!\left(\varepsilon^1_{VN}L_1b_N\right),\\
e^0_N&=\varepsilon^0_NL_0r_0,\qquad
e^1_{VN}=\varepsilon^1_{VN}L_1r_1 .
\end{aligned}
\tag{B.BM5}
\]
Existence uses \(\operatorname{Hom}(SP_0,r_1)\), a quasi-isomorphism, not any assertion that \(Sr_0\) is one. The second line follows by applying \(L_1\), then the first identity in (B.BM3) and naturality of \(\theta\). It compares the actual counits, with the actual witness. The resulting \(c_N\) need not be a homotopy equivalence.

For the unit comparison, take \(N=L_0A\), with \(A\) h-projective. Choose
\(u_0:A\to P_0\) and \(k_0\) with \(r_0u_0-\eta^0_A=dk_0\).
To represent the other unit, first choose a replacement
\(r':P'\to U_1L_1SA\) and a unit lift \(u':SA\to P'\) with
\(r'u'-\eta^1_{SA}=dk'\).
Lift the map \(\theta_A:L_1SA\to VL_0A\) through the right-resolution graph to \((\theta_A,z,h)\), so \(r_1z-U_1\theta_A\,r'=dh\). Then
\[
\begin{aligned}
u_1&=zu',&
k_1&=hu'+U_1\theta_A\,k',\\
r_1u_1-U_1\theta_A\,\eta^1_{SA}&=dk_1,\\
r_1(c_{L_0A}Su_0-u_1)
 &=d\!\left(b_{L_0A}Su_0+\mu_{L_0A}Sk_0-k_1\right).
\end{aligned}
\tag{B.BM6}
\]
The last identity uses the second line of (B.BM3). Its closed defect is a boundary because \(\operatorname{Hom}(SA,r_1)\) is a quasi-isomorphism. Thus this is the unit followed by the actual lifted \(\theta_A\), not a replacement chosen merely to make a desired diagram commute.

The underlying triangle faces also agree before replacement. Two useful explicit forms are
\[
\begin{aligned}
V\varepsilon^0_{L_0A}\,\theta_{U_0L_0A}\,L_1S\eta^0_A
 &=\theta_A
 =\varepsilon^1_{VL_0A}L_1U_1\theta_A\,L_1\eta^1_{SA},\\
U_1V\varepsilon^0_N\,\mu_{L_0U_0N}\,S\eta^0_{U_0N}
 &=\mu_N
 =U_1\varepsilon^1_{VN}\,\eta^1_{U_1VN}\,\mu_N .
\end{aligned}
\tag{B.BM7}
\]
For the first line use naturality of \(\theta,\varepsilon^1\) and the left triangles. For the second use naturality of \(\mu\), the right triangle for \(L_0\), and then the right triangle for \(L_1\). The resolved witnesses (B.BM5)–(B.BM6), together with (B.IA9) and (B.IA13), are the corresponding triangle target data. A Hom quasi-isomorphism gives a boundary lift of a closed defect; it does not assert equality with a prescribed primitive after applying \(r_1\).

**Successive changes of base: actual vertical pasting.** Add a second square
\(\theta_2:L_2S_2\to V_2L_1\), and write \(\theta_1,\mu_1\) for the first. With the balanced induction associators inserted, the composite left and right maps are
\[
\begin{aligned}
\theta_{21}&=(V_2\theta_1)(\theta_2S_1),\\
\mu_{21,N}&=\mu_{2,V_1N}\,S_2\mu_{1,N}.
\end{aligned}
\tag{B.BM8}
\]
To prove the second formula, transpose it under \(L_2\dashv U_2\). The first identity of (B.BM3) gives
\(V_2\varepsilon^1\,\theta_{2,U_1V_1N}\,L_2S_2\mu_{1,N}\).
Naturality of \(\theta_2\) moves \(L_2S_2\mu_1\) to the left. Apply (B.BM3) for \(\mu_1\); the result is
\(V_2V_1\varepsilon^0_N\,\theta_{21,U_0N}\).
This is exactly the defining transpose of \(\mu_{21}\).

For compatible replacements \(P_0,P_1,P_2\), suppose \(c_1,b_1\) and \(c_2,b_2\) are the two lifts in (B.BM5). A lift of the composite, with no new choice, is
\[
\begin{aligned}
c_{21}&=c_2S_2c_1,\\
b_{21}&=b_2S_2c_1+\mu_{2,V_1N}S_2b_1,\\
r_2c_{21}-\mu_{21,N}S_2S_1r_0&=db_{21}.
\end{aligned}
\tag{B.BM9}
\]
Expand the left side, substitute both lift equations, and use closedness of \(c_1,\mu_2\). For three successive squares the witness is
\[
b_3S_3c_2\,S_3S_2c_1+
\mu_3S_3b_2\,S_3S_2c_1+
\mu_3S_3\mu_2\,S_3S_2b_1 .
\tag{B.BM10}
\]
Both parenthesizations give this ordered sum by (B.BM8). Induction gives the analogous finite sum for any length. No factors are permuted. If a separately chosen composite lift is retained, subtract its witness from (B.BM9); the Hom quasi-isomorphism out of \(S_2S_1P_0\) supplies the comparison homotopy. Identity squares use \(c=1,b=0\).

**Composition of geometric operations: horizontal pasting.** Let \(M_i\dashv W_i\) be a second pair of induction/restriction adjunctions after \(L_i\dashv U_i\). Write the vertical functors as \(S,T,V\), and the cells as
\(\theta:L_1S\to TL_0\), \(\phi:M_1T\to VM_0\).
Their mates are \(\mu:SU_0\to U_1T\) and \(\nu:TW_0\to W_1V\). For the composite adjunction \(M_iL_i\dashv U_iW_i\), the formulas are
\[
\begin{aligned}
\Xi&=(\phi L_0)(M_1\theta),\\
\psi_N&=U_1\nu_N\,\mu_{W_0N}:
          SU_0W_0N\longrightarrow U_1W_1VN .
\end{aligned}
\tag{B.BM11}
\]
For a direct check, transpose \(\psi_N\) first under \(L_1\). Naturality of \(\varepsilon^1\) turns its transpose into
\(\nu_N\,T\varepsilon^0_{W_0N}\,\theta_{U_0W_0N}\).
Now transpose under \(M_1\). Naturality of \(\phi\) and the defining transpose of \(\nu\) give
\[
V\!\left(\varepsilon^{M_0}_N
          M_0\varepsilon^0_{W_0N}\right)
       \phi_{L_0U_0W_0N}\,M_1\theta_{U_0W_0N}.
\tag{B.BM12}
\]
The first parenthesis is the composite counit and the final factors are \(\Xi_{U_0W_0N}\). This proves (B.BM11), including its direction and factor order. Together (B.BM8) and (B.BM11) prove raw interchange: both orders transpose the same pasted left cell. The ordinary unit and counit identifications used here are exactly those retained in (B.IA7)–(B.IA8).

Here is the horizontal resolved witness, where the intermediate replacement cannot be omitted. Choose
\(r:R\to W_0N\), \(t:Z\to U_0R\),
\(r':R'\to W_1VN\), \(t':Z'\to U_1R'\), all with h-projective sources. Lift the second mate to \(c_\nu:TR\to R'\), with
\(r'c_\nu-\nu_NTr=db_\nu\).
Then lift the closed map \(U_1c_\nu\,\mu_R\,St\) through \(t'\) to \(c_\psi:SZ\to Z'\), with witness \(b_\psi\). The complete equation is
\[
\begin{aligned}
t'c_\psi-U_1c_\nu\,\mu_R\,St&=db_\psi,\\
(U_1r'\,t')c_\psi-\psi_N\,S(U_0r\,t)
 &=d\!\left(U_1r'\,b_\psi+
               U_1b_\nu\,\mu_R\,St\right).
\end{aligned}
\tag{B.BM13}
\]
Expand the left side using the first line, substitute the equation for \(b_\nu\), and use homogeneous naturality of \(\mu\) on the closed \(r\). Every lift exists because its source is h-projective and its target replacement is a quasi-isomorphism. No induction of an unresolved quasi-isomorphism is asserted.

For homogeneous parameter maps, the two replacements \(r,t\) have the nested graph of (B.IA10). Its passage to the composite replacement retains
\[
K_1(f,\rho,z;k,h)
 =(f,z,U_0r'\,h+U_0k\,t),\qquad
K_2(B,A)=(0,0,U_0k_Bh_A).
\tag{B.BM14}
\]
These are exactly (B.IA12), with \(G=M_0,\beta=F_0\); the target route has the same formula with subscript \(1\). The signs are those of (B.RS7)–(B.RS8), not signs deduced from the degree-zero witness alone. Thus (B.BM13) is attached to the same nested models as the intermediate adjunction, not an incompatible third selection of replacements.

**Whole parameter diagrams, rather than independent pointwise choices.** Suppose the strict source/target functors and \(\theta,\phi\) are given over a specified free dg parameter index \(J\). Resolve the full modules over \(J^{\mathrm{op}}\otimes\mathcal C_i\) and \(J^{\mathrm{op}}\otimes\mathcal D_i\) before evaluation, as in B.1u–B.1v. The induced \(S,V,L_i\) preserve h-projectivity in these whole categories by their actual induction/restriction adjunctions. The Hom quasi-isomorphisms used in (B.BM5), (B.BM6), (B.BM9) and (B.BM13) therefore hold for whole diagrams. Their lifts and witnesses are graded-natural, not independently chosen at each vertex.

For already specified faces, use the graph form of these lifts: its kernel is the shifted cone of the relevant Hom quasi-isomorphism, and projection is surjective on graded maps. The relative free-index lifting argument (B.ND9) extends the lifts while retaining those faces. Include the checked unit, counit and triangle relations (B.BM3), (B.BM7), and their displayed witnesses in the target presentation. Include the nested comparison through its strict roof, so its free words retain (B.BM14). This supplies coherent lifts for the specified strict parameter diagram. It does not assert that an arbitrary geometric changing-model diagram has already been made strict, or that adding an unchecked relation to a quotient presentation is harmless.

**When the left inverse is available only on resolved inputs.** This distinction matters geometrically. A homotopy inverse of a left base-change comparison on h-projective models is not automatically a natural transformation on every unresolved module. In particular, one may not evaluate that inverse at \(U_0N\) without further evidence. There is a direct resolved construction that needs only its values on the h-projective inputs.

Retain \(P_0,r_0,e^0_N\) from (B.BM5). Suppose the specified closed left comparison \(\theta\) is natural on the h-projective inputs and maps of the whole parameter diagram under consideration. Define its resolved transpose by
\[
\begin{aligned}
\zeta_N&=\operatorname{Adj}_{L_1}
              (Ve^0_N\,\theta_{P_0}):
                 SP_0\longrightarrow U_1VN,\\
r_1c_N-\zeta_N&=db_N,\\
\ell_0&=\varepsilon^0_{L_0A}L_0k_0,\\
r_1(c_{L_0A}Su_0-u_1)
 &=d\!\left(b_{L_0A}Su_0+
       \operatorname{Adj}_{L_1}(V\ell_0\,\theta_A)-k_1\right).
\end{aligned}
\tag{B.BM16}
\]
The notation \(\operatorname{Adj}_{L_1}\) denotes the full Hom-complex adjunction in every degree, so the transpose of the degree-minus-one map in the last line is defined. The counit equation in (B.BM5) is unchanged, by definition of \(\zeta_N\). For the last line, \(e^0_{L_0A}L_0u_0-1=d\ell_0\) by (B.DA11). Naturality of \(\theta\) on the map \(u_0:A\to P_0\), whose ends are h-projective, gives
\(\zeta_{L_0A}Su_0-U_1\theta_A\eta^1_{SA}
 =d\operatorname{Adj}_{L_1}(V\ell_0\theta_A)\).
This proves the displayed unit witness. If the full unresolved \(\mu\) exists, naturality identifies \(\zeta_N=\mu_NSr_0\), so this retains rather than changes the earlier construction.

There are equally direct pasting formulas. Set \(D_1=\varepsilon^1_{V_1N}L_1b_1\). With the ordered composite \(\theta_{21}\) from (B.BM8), a vertical witness is
\[
\begin{aligned}
b_{21}^{\mathrm{res}}
 &=b_2S_2c_1+
   \operatorname{Adj}_{L_2}
      \!\left(V_2D_1\,\theta_{2,S_1P_0}\right),\\
r_2c_2S_2c_1-\zeta_{21,N}
 &=db_{21}^{\mathrm{res}} .
\end{aligned}
\tag{B.BM17}
\]
Indeed, transpose the second term in the difference under \(L_2\), move \(c_1\) through \(\theta_2\), and use
\(e^1L_1c_1-V_1e^0\theta_1=dD_1\).
All values of \(\theta_2\) are at h-projectives. When the full unresolved mate exists, its naturality identifies the second term with \(\mu_2S_2b_1\) in (B.BM9). Without it, (B.BM17) is the formula to use. Repeated pasting is defined by these transposed counit witnesses; associativity follows by expanding them in their original order and using the same balanced associators.

For horizontal composition retain \(R,Z,R',Z'\) of (B.BM13), and put \(e_L=\varepsilon^0_RL_0t:L_0Z\to R\), \(e_M=\varepsilon^{M_0}_NM_0r:M_0R\to N\). Define and lift
\[
\begin{aligned}
\zeta_\nu&=\operatorname{Adj}_{M_1}(Ve_M\,\phi_R),
 &r'c_\nu-\zeta_\nu&=db_\nu,\\
\kappa&=\operatorname{Adj}_{L_1}
                 (c_\nu\,Te_L\,\theta_Z),
 &t'c_\psi-\kappa&=db_\psi,\\
\zeta_\Xi&=\operatorname{Adj}_{M_1L_1}
                 \!\left(V(e_M M_0e_L)\,\Xi_Z\right),\\
(U_1r'\,t')c_\psi-\zeta_\Xi
 &=d\!\left(U_1r'\,b_\psi+
       \operatorname{Adj}_{L_1}(b_\nu\,Te_L\,\theta_Z)\right).
\end{aligned}
\tag{B.BM18}
\]
Transpose the last equation first under \(L_1\), substitute the equation for \(c_\nu\), and then transpose under \(M_1\). Naturality of \(\phi\) on the h-projective map \(e_L:L_0Z\to R\) gives (B.BM12)'s ordered composite, while the remaining differential is exactly the displayed witness. No value \(\theta_{U_0R}\) or \(\phi_{W_0N}\) is used. Thus the resolved-only construction covers the geometric input actually supplied, even when an unresolved inverse is unavailable. Its parameter lifts still use whole modules and the nested coefficient (B.BM14).

**Bind the formulas to the actual geometric cube.** In a common strict module model of the compact-support square, use
\[
L_0=Rf_!,\qquad L_1=Rf'_!,\qquad
S=u^*,\qquad V=g^*,\qquad
\theta=(g^*Rf_!\longrightarrow Rf'_!u^*)^{-1}.
\tag{B.BM15}
\]
These symbols mean the functors represented by the common resolved model, with their induction descriptions and specified endpoint comparisons inserted; inverse image is not being asserted to preserve K-injectives. The usual left base-change map comes from (B.CB2)–(B.CB6). Its proper/open mixed cell is the actual sheaf-map cube (B.GC12), and (B.GC13) gives its resolved edge
\(z=t(A_Cs)\theta_k^{-1}\).
Those paragraphs compare all selected-edge coefficients, including the second coefficient.

On a specified whole strict parameter model, the left comparison on representable cells is the resolved geometric comparison just cited. Both sides are induction functors and preserve sums and graded-split cell attachments. The split semifree filtration, exact filtered unions and passage along homotopy-equivalent h-projective replacements, as in (B.SM1), extend its quasi-isomorphism assertion to the whole h-projective module. Thus the left comparison is a quasi-isomorphism between h-projective whole-module representatives. Its cone is acyclic and h-projective, hence contractible; choose its chain-homotopy inverse there, retaining both inverse homotopies. That is the \(\theta\) in (B.BM15). It need not be a literal inverse on the original K-injective models. In particular, the present construction never applies a proper direct image to an unresolved quasi-isomorphism.

Use (B.BM16) for the actual exchange map \(u^*f^!\to f'^!g^*\) in this common model; an unresolved inverse is not assumed. Its counit face is (B.BM5), and its unit face is the resolved-only witness in (B.BM16). For a composition \(gf\), use (B.BM18) and the actual replacements of (B.IA14), comparing with the common-span right target. Successive base changes use (B.BM17). Where a full unresolved comparison is already supplied, these reduce to (B.BM2), (B.BM9) and (B.BM13). The supplied geometric mixed cube therefore has the indicated cellwise right-adjoint mate and pasted witnesses. No general right-exchange isomorphism follows: (B.BM4) explains the logical obstruction.

The remaining geometric step is to join these whole-parameter constructions across the entire varying-refinement and changing-model array. B.1z normalizes the fixed-endpoint refinement/fold roof; it does not by itself supply that larger parameter model. Its source/target model-change maps and higher components must be explicitly joined to define the global enhanced operation system. Geometric nearby attaching and multiplicative descent, normalized coefficient transport and strict-heart higher effacement are not established by this construction. \(\square\)



### Resolve inverse-image transport over the geometric index

**Proposition B.1ac (one parameter category for inverse images).** In the ordinary coefficient setting, let \(K\) be any small category of geometric changes of base: an arrow \(g:i\to j\) denotes a scheme map \(X_j\to X_i\), with its actual étale inverse-image/direct-image adjunction. There is a single labelled dg category of mapping kernels for all these inverse images. Its composition is strictly associative and retains the actual geometric adjunction maps. A relative-free resolution of the whole category makes every labelled kernel h-projective separately in either module variable. Its compositors induce homotopy equivalences on h-projective modules. This supplies the changing-base parameter input; joining the compact-support cells and their exceptional-adjunction targets to this input remains a separate, explicit step below.

No map \(g\) is assumed proper, an equivalence, or a map whose inverse image preserves K-injectives. Complexes may be unbounded and the coefficient ring need not be a field. Categories and modules are taken in successively larger universes as in B.1k.

**Start with the right adjoints, not a choice of inverse-image replacements.** Put \(\mathcal C_i=\mathcal I(X_{i,\mathrm{et}},\Lambda)\). Exactness of \(g^*\) gives, for an acyclic complex \(A\) and K-injective \(J\),
\[
\operatorname{Hom}^{\bullet}(A,g_*J)
 \cong\operatorname{Hom}^{\bullet}(g^*A,J).
\tag{B.IP1}
\]
The right side is acyclic. Thus \(g_*\) restricts to an actual dg functor \(\mathcal C_j\to\mathcal C_i\), without a properness hypothesis. The adjunction isomorphism respects all homogeneous maps. The canonical comparisons \(g_*h_*\cong(hg)_*\) and the unit comparisons satisfy the composition pentagon: their sections identify the same iterated direct image, with the same restriction maps.

Apply (B.SN1)–(B.SN3) to this contravariant system, that is, on \(K^{\mathrm{op}}\). Write \(\widehat{\mathcal C}_i\) for its origin-labelled fibres. Their evaluation maps are quasi-equivalences; the normalized functors \(\widehat G_g:\widehat{\mathcal C}_j\to\widehat{\mathcal C}_i\) compose literally. Now, and only now, apply the strict-functorial free replacement \(Q\) of B.1t:
\[
\mathcal E_i=Q\widehat{\mathcal C}_i,\qquad
D_g=Q\widehat G_g,\qquad
D_gD_h=D_{hg},\qquad D_{1_i}=1.
\tag{B.IP2}
\]
Let \(e_i:\mathcal E_i\to\mathcal C_i\) be augmentation followed by evaluation. It is a quasi-equivalence, with specified closed natural isomorphisms
\(e_iD_g\cong g_*e_j\). These comparisons retain their pentagon. We have not applied \(Q\) to a natural transformation. The Hom complexes of \(\mathcal E_i\) are semifree over \(\Lambda\): in the free-word construction of \(Q\), filter by the ordered cell generators and then their finite words; the differential of each generator uses earlier cells. This also makes them h-projective and K-flat over \(\Lambda\). It does not say that \(g_*\) itself is a quasi-equivalence.

For \(I\in\mathcal E_i\), \(J\in\mathcal E_j\), define
\[
\begin{aligned}
B_g(J,I)&=\mathcal E_i(I,D_gJ),\\
a\cdot u\cdot b&=D_g(a)\,u\,b.
\end{aligned}
\tag{B.IP3}
\]
Here \(a:J\to J'\), \(b:I'\to I\); the order of the factors is part of the formula. This is covariant in \(J\) and contravariant in \(I\). Evaluation and (B.IP1) give the natural quasi-isomorphism
\[
B_g(J,I)\longrightarrow
 \operatorname{Hom}^{\bullet}(e_iI,g_*e_jJ)
 \cong\operatorname{Hom}^{\bullet}(g^*e_iI,e_jJ).
\tag{B.IP4}
\]
The second complex computes the derived Hom with the actual inverse image, because its target is K-injective. There is no unresolved direct image being applied to a quasi-isomorphism in this assertion.

**The composition is a co-Yoneda isomorphism.** For successive \(g:i\to j\), \(h:j\to k\), use the usual balanced tensor, with no permutation of homogeneous factors:
\[
\begin{aligned}
B_h(K,-)\otimes_{\mathcal E_j}B_g(-,I)
 &\xrightarrow{\ \mu_{h,g}\ }B_{hg}(K,I),\\
v\otimes u&\longmapsto D_g(v)u,\\
w&\longmapsto 1_{D_hK}\otimes w.
\end{aligned}
\tag{B.IP5}
\]
The last line is its inverse. Indeed \(B_h(K,-)=\mathcal E_j(-,D_hK)\) is a representable right module. The balancing relation turns \(v\otimes u\) into \(1_{D_hK}\otimes D_g(v)u\), while the forward map sends the latter to \(D_g(v)u\). This verifies both inverses, not merely equality of cohomology dimensions. The differential is respected since
\(d(D_g(v)u)=D_g(dv)u+(-1)^{|v|}D_g(v)du\).
Representable tensor is evaluation, so the same tensor already computes the derived tensor in this variable, over an arbitrary \(\Lambda\).

For three changes and arbitrary homogeneous \(u,v,w\), both associations give
\[
D_gD_h(w)\,D_g(v)\,u
   =D_{hg}(w)\,D_g(v)\,u.
\tag{B.IP6}
\]
The units are the identity kernels. Thus every finite parenthesization gives exactly the same ordered expression. Under (B.IP4), this is the usual successive inverse-image adjunction, with the canonical inverse-image composition isomorphism retained. It is not a statement that inverse images themselves were chosen as strict functors on K-injective objects.

Here is that geometric interpretation on representatives. Choose a quasi-isomorphism \(q:g^*e_iI\to J_0\), with \(J_0\) K-injective, and a fibre object representing \(J_0\). Full faithfulness on cohomology of \(e_i\) lifts the adjoint of \(q\) to a closed \(u\in B_g(J_0,I)\), after inserting the chosen fibre equivalence. Then
\[
\mathcal E_j(J_0,J)\longrightarrow B_g(J,I),
 \qquad a\longmapsto D_g(a)u
\tag{B.IP7}
\]
is a quasi-isomorphism for every \(J\). To prove it, evaluate, apply (B.IP1), and precompose with \(q\). Precomposition is a quasi-isomorphism because the target \(e_jJ\) is K-injective. A homotopic lift of the adjoint gives the same conclusion. This proves quasi-corepresentability of the entire left module \(B_g(-,I)\).

If \(q_h:h^*J_0\to J_1\) is a second such replacement, the element \(D_g(u_h)u\) represents \(q_hh^*q\), with the inverse-image associator inserted. This follows by applying the two actual adjunction bijections in succession; their unit/counit triangles cancel the middle pair. Exactness of \(h^*\) makes this composite a quasi-isomorphism. More generally, precomposition by \(u\) on every subsequent labelled Hom is a quasi-isomorphism, since it becomes precomposition by the quasi-isomorphism \(b^*q\) into a K-injective target. This is the homotopical universal property of the transported object, not a claim that \(g\) is invertible.

**Put all labels in one category.** Define \(\mathcal T\) with objects \((i,I)\) and
\[
\begin{aligned}
\mathcal T((i,I),(j,J))
 &=\bigoplus_{g:i\to j}B_g(J,I),\\
(h,v)\circ(g,u)&=(hg,D_g(v)u).
\end{aligned}
\tag{B.IP8}
\]
Its differential preserves labels. Equations (B.IP5)–(B.IP6) prove the dg axioms, including the signed Leibniz identity, for the whole category. Parallel arrows of \(K\) remain distinct summands. A nonidentity endomorphism is not merged with the identity sector. Direct sums are exact for modules, so evaluation gives a quasi-isomorphism on each labelled Hom and on their sums. The identity-labelled sectors are the \(\mathcal E_i\); their disjoint union \(\mathcal E=\coprod_i\mathcal E_i\) is a dg subcategory with all the same objects.

The kernel composition is already strict, but its left modules need not yet be h-projective. Resolve this defect **once over \(\mathcal E\)**, rather than replacing the arrows independently. Construct
\[
\mathcal E\ \hookrightarrow\ \mathcal R
 \xrightarrow{\ p\ }\mathcal T,
 \qquad p|_{\mathcal E}=1.
\tag{B.IP9}
\]
Start with \(\mathcal E\), and freely adjoin closed generators mapping to every closed homogeneous element of every labelled Hom of \(\mathcal T\). At each following stage, for every closed \(z\) in a labelled Hom of the current category and every \(a\) of the same label with \(p(z)=da\), adjoin \(t\) of degree \(|z|-1\), with \(dt=z\), \(p(t)=a\). Iterate through the countable stages and take their union. Every word is finite. Consequently every kernel cohomology class appears at some stage and is killed at the next one; every target class was hit at the first stage. Thus \(p\) is a quasi-isomorphism on **each** labelled Hom. It is the identity on objects and fixes every original fibre arrow. No relation between labels is imposed by deleting a generator; its specified boundary is retained.

We justify the required module property, including the identity sector. Fix \(I\), \(g:i\to j\). In a relative free word with at least one newly adjoined generator, separate its last fibre arrow. As a left \(\mathcal E_j\)-module its resulting graded summand has form
\(\mathcal E_j(B,-)\otimes_\Lambda V\), where \(V\) consists of earlier fibre Hom factors, finitely many shifted new generators and the first fibre factor from \(I\). The intervening fibre Homs are semifree over \(\Lambda\), by (B.IP2); their finite tensors and direct sums are semifree. Filter the relative words by the ordered new cells, refining by these coefficient filtrations. The differential of a new cell lowers this filtration, since its specified boundary uses earlier cells; the fibre differentials lower the coefficient filtration. Thus the summands give a semifree filtration of the left module. The zero-new-generator summand exists only for \(i=j,g=1_i\), and is the representable \(\mathcal E_i(I,-)\). It is included at the initial stage. Separating the first fibre arrow gives the dual argument for a fixed target and a right \(\mathcal E_i\)-module. Therefore
\[
C_g(J,I)=\mathcal R((i,I),(j,J))_g
 \longrightarrow B_g(J,I)
\tag{B.IP10}
\]
is an objectwise quasi-isomorphism, with \(C_g\) h-projective and K-flat separately in either module variable. This assertion does not require the diagonal bimodule itself to be h-projective as a module on the tensor-product category.

Composition in \(\mathcal R\) supplies one associative system, with the canonical balanced-tensor associators inserted:
\[
\begin{array}{ccc}
C_h(K,-)\otimes_{\mathcal E_j}C_g(-,I)
 &\xrightarrow{\ c_{h,g}\ }&C_{hg}(K,I)\\
{\scriptstyle p\otimes p}\downarrow&&\downarrow{\scriptstyle p}\\
B_h(K,-)\otimes_{\mathcal E_j}B_g(-,I)
 &\xrightarrow[\ \cong\ ]{\ \mu_{h,g}\ }&B_{hg}(K,I).
\end{array}
\tag{B.IP11}
\]
Every such map is a quasi-isomorphism. Compare it with (B.IP5). First replace \(C_h(K,-)\) by \(B_h(K,-)\); tensoring this quasi-isomorphism with the K-flat left module \(C_g(-,I)\) preserves it. Then replace \(C_g(-,I)\) by \(B_g(-,I)\); the right module \(B_h(K,-)\) is representable, so this second tensor also preserves the quasi-isomorphism. The bottom map (B.IP5) is an isomorphism and the right vertical map (B.IP10) is a quasi-isomorphism. Two-out-of-three proves the assertion. Omitting either flatness justification would not be valid for arbitrary coefficients.

For clarity, on left modules use
\[
\begin{aligned}
\mathsf A_g(N)(J)&=C_g(J,-)\otimes_{\mathcal E_i}N,\\
\mathsf A_h\mathsf A_g(N)&\xrightarrow{\ c_{h,g}\ }
       \mathsf A_{hg}(N),\qquad
N\xrightarrow{\ \iota_i\ }\mathsf A_{1_i}(N).
\end{aligned}
\tag{B.IP12}
\]
Equivalently these are right modules on \(\mathcal E_i^{\mathrm{op}}\), with the standard Koszul convention. Each \(\mathsf A_g\) sends h-projectives to h-projectives: apply it to a semifree filtration of \(N\); its representable cells become the h-projective left modules \(C_g(-,I)\), and refine by their just-proved semifree filtrations. Retracts and homotopy equivalences are retained. For h-projective \(N\), tensoring (B.IP11) with \(N\) is a quasi-isomorphism, and both resulting left modules are h-projective. Its cone is therefore acyclic and h-projective, so it is contractible; the compositor is a homotopy equivalence. The same argument applies to the unit \(\iota_i\), induced by the protected inclusion \(\mathcal E_i\subset\mathcal R\): its composite with augmentation is the ordinary Yoneda identity of \(N\). Composition and the two unit diagrams commute exactly, because they are the composition and identity laws of the one category \(\mathcal R\). No separately chosen inverses enter those diagrams.

Before resolution, the corresponding tensor functor is simply \(N\mapsto N\circ D_g\), by co-Yoneda. For h-projective \(N\), augmentation gives a quasi-isomorphism from \(\mathsf A_g(N)\) to this restriction: tensor (B.IP10), in its right \(\mathcal E_i\)-variable, with the K-flat left module \(N\). Restriction preserves objectwise quasi-isomorphisms. Thus on a h-projective replacement of a corepresentable, (B.IP7) identifies the result with the opposite of the actual geometric inverse-image functor. Taking opposites returns its original variance. This identifies the parameter action; it is not the right adjoint of \(g_*\) obtained by using representable **right** modules in place of these left modules.

**What has been joined, and what has not.** The index \(K\) can contain the entire chosen family of geometric base changes and their compositions, not only one square or a finite sample. The same normalization and relative-free category treats every label and every composition. Proper compactification refinements remain the distinct fixed-endpoint equivalences of B.1z; the inverse-image arrows here are not promoted to equivalences. In (B.GC12), the four symbols \(A_D,A_Y,A_C,A_U\) now have these actual mapping-kernel models. Equation (B.GC13) still supplies their mixed compact-support cell, with the original edge \(t(A_Cs)\theta_k^{-1}\) and its higher coefficients. Those existing coefficients must be included when attaching that cell and the compact-support operation kernels to this parameter category.

In particular, (B.IP11)–(B.IP12) give strictly associative compositor **maps** which become homotopy equivalences on h-projective inputs. They are not literal isomorphisms and have not been replaced by pointwise inverses to claim a strictly commuting exceptional-operation system. The remaining join must use the common strict roof and whole-diagram lifts of B.1t–B.1aa, retaining the resolved-only transposes (B.BM16)–(B.BM18). That join, geometric nearby attaching and multiplicative descent, coefficient completion/rationalization and strict-heart higher effacement are not established by this construction. \(\square\)



### Join the geometric kernels in right-module variance

**Proposition B.1ad (the module side of the compact-support join).** The inverse-image kernels of B.1ac admit actual right-module models and natural composition roofs. The fixed-compactification functor of (B.RG9) admits a right-module kernel over the same source and target models. Both constructions preserve h-projectives and homotopy-representable right modules. The compact-support kernel has a strict tensor–Hom adjunction, whose resolved unit and counit represent the ordinary exceptional adjunction. We construct these maps, including the bar and dual-evaluation signs.

This addresses a variance issue in joining the preceding constructions. The left-module functor of (B.IP12) models the **opposite** inverse image; it cannot simply be substituted for the right-module functors in (B.BM15). The construction below supplies the correctly directed functors. It does not assert that their geometric mixed-cell diagrams have already been assembled or that an objectwise homotopy inverse is a natural inverse of bimodules.

All models are over the original commutative \(\Lambda\). Compact support retains the full Noetherian, separated finite-type, unbounded ordinary torsion scope of (B.RG9); inverse images have the scope of B.1ac. Keep its chosen locally semifree models \(\mathcal E_i\), their evaluations \(e_i\), and the label-preserving kernels \(C_g\). For left modules a homogeneous degree-\(r\) map satisfies \(u(ax)=(-1)^{r|a|}a\,u(x)\). For right modules use exactly (B.DA1)'s convention \(u(xa)=u(x)a\).

**Dualize the quasi-corepresentable kernel, not its variance label.** For \(g:i\to j\), define
\[
P_g(J,I)=
 \operatorname{Hom}^{\bullet}_{\mathcal E_j\text{-}\mathrm{Mod}}
       \bigl(C_g(-,I),\mathcal E_j(J,-)\bigr).
\tag{B.RK1}
\]
This is contravariant in \(J\), covariant in \(I\), hence a kernel for right-module transport from \(\mathcal E_i\) to \(\mathcal E_j\). The Hom is the ordinary full complex of graded module maps. No extra derived-Hom replacement is needed: \(C_g(-,I)\) is h-projective by (B.IP10).

Here is why its columns have the required properties. Equations (B.IP4) and (B.IP7), together with the augmentation from (B.IP10), give a zigzag from \(C_g(-,I)\) to a left corepresentable \(\mathcal E_j(J_0,-)\), where \(e_jJ_0\) represents \(g^*e_iI\). Lift the corepresentable's quasi-isomorphism through that zigzag by Hom from a corepresentable, as in B.1l. The resulting quasi-isomorphism between h-projectives is a homotopy equivalence. Applying the contravariant Hom functor in (B.RK1) carries this homotopy equivalence to one of right modules. On the corepresentable the enriched Yoneda map gives exactly \(\mathcal E_j(-,J_0)\). Therefore \(P_g(-,I)\) is h-projective and homotopy representable, with the **actual inverse image** as its representing object. Tensoring a right module with \(P_g\) sends representable cells to these columns. The cell-filtration proof of B.1l then proves preservation of h-projectives and homotopy representables. This is not the generally different right adjoint of \(g_*\).

**Composition has a canonical roof, not an inverted arrow by fiat.** Set
\(R_{h,g}(-,I)=C_h(-,-)\otimes_{\mathcal E_j}C_g(-,I)\), with the factor order of (B.IP11). Write \(D R(K,I)=\operatorname{Hom}_{\mathcal E_k\text{-}\mathrm{Mod}}^\bullet(R(-,I),\mathcal E_k(K,-))\). The common right-module kernel is
\[
 P_g\otimes_{\mathcal E_j}P_h
   \xrightarrow{\ \nu_{h,g}\ }D R_{h,g}
   \xleftarrow{\ D c_{h,g}\ }P_{hg}.
\tag{B.RK2}
\]
Here the first tensor is ordered as right-module transport: \(g\) first, then \(h\). The arrow on the right points **from** \(P_{hg}\), because Hom dualization reverses the compositor. At \(K,I\), the first arrow is balanced evaluation. For homogeneous \(u\in P_g(J,I)\), \(v\in P_h(K,J)\), \(x\in C_h(L,J')\) and \(y\in C_g(J',I)\), it is
\[
 \nu_{h,g}(u\otimes v)(x\otimes y)
   =(-1)^{|u|(|v|+|x|)}\,v\bigl(x\,u(y)\bigr).
\tag{B.RK3}
\]
This sign moves \(u\) past \(v,x\) before evaluation on \(y\); no other factor is permuted. In these conventions
\((u a)(y)=(-1)^{|a||y|}u(y)a\) and
\((a v)(x)=(-1)^{|a|(|v|+|x|)}v(xa)\).
Substitution verifies the balancing relation in the first tensor. The relation
\((xa)\otimes y=x\otimes ay\) in the second tensor uses the left-linearity rule for \(u\) and gives the same sign. Evaluation, tensor symmetry with its Koszul sign, and the module action are chain maps; thus (B.RK3) is a chain map and has the indicated right and left kernel actions.

Both arrows of (B.RK2) are objectwise homotopy equivalences of right modules for every fixed \(I\). Indeed, \(R_{h,g}(-,I)\) is h-projective: resolve the left \(\mathcal E_j\)-module \(C_g(-,I)\) by its semifree filtration, and its cells become the h-projective columns of \(C_h\). The compositor \(c_{h,g}\) is a quasi-isomorphism between these h-projectives by (B.IP11), hence a homotopy equivalence. Its dual is a homotopy equivalence. To check \(\nu\), replace \(C_g(-,I)\), by a homotopy equivalence, with \(\mathcal E_j(J_0,-)\). Both the tensor and the Hom constructions preserve such homotopies, without a flatness assumption. The resulting map is precisely the co-Yoneda isomorphism onto \(P_h(-,J_0)\). Also \(P_g(-,I)\otimes P_h\) is h-projective by its representable-cell filtration. Thus all columns in the displayed roof are legitimate h-projective representatives.

There is an all-length compatibility already at the common kernels. For three arrows, the two evaluation routes to the dual of \(C_\ell\otimes C_h\otimes C_g\) both send \(u\otimes v\otimes w\), evaluated on \(x\otimes y\otimes z\), to
\[
 (-1)^{\,|u|(|v|+|w|+|x|+|y|)
                 +|v|(|w|+|x|)}
 w\bigl(x\,v(y\,u(z))\bigr).
\tag{B.RK4}
\]
Here \(x,y,z\) belong respectively to the \(\ell,h,g\) kernels. The sign is the permutation moving each evaluator next to its argument. The same ordered evaluation and its permutation sign prove the assertion for every finite length, with the usual tensor associators. Precomposition with \(c\) respects these comparisons because the \(c\)'s come from the associative category \(\mathcal R\) of B.1ac. Identity evaluations give the unit comparisons. These are compatible **roofs**; no choice of pointwise inverse is promoted to a strict natural composition map.

**Put the actual compactification roof over these same endpoint models.** The diagram to be used is
\[
 \mathcal E_X\xleftarrow{\ p\ }\mathcal A_f
       \xrightarrow{\ q\ }\mathcal E_Y,
 \qquad p\text{ a quasi-equivalence}.
\tag{B.RK5}
\]
We construct it from (B.RG9), not from a new compactification theorem. First pull its graph back along \(e_X:\mathcal E_X\to\mathcal I(X)\). Projection of (B.RG9) is surjective on graded Homs with acyclic kernel, and a replacement exists over every object. Its strict pullback therefore has the same properties and is a quasi-equivalence onto \(\mathcal E_X\). Its proper-output functor still lands in \(\mathcal I(Y)\).

To lift this output to \(\mathcal E_Y\), use objects \((a,J,t)\), where \(a\) is in that pullback, \(J\in\mathcal E_Y\), and \(t:F(a)\to e_YJ\) is a closed homotopy equivalence. Such objects exist: the identity-origin objects in (B.SN1) include every K-injective target. A degree-\(n\) map has components \((b,c,k)\) with \(k:F(a)\to e_YJ'\) of degree \(n-1\), and its third differential is \(t'F(b)-e_Y(c)t-dk\). Use exactly the graph composition (B.RG3). Projection to \(a\) is graded-Hom-surjective. Its kernel is the shifted cone of
\(\mathcal E_Y(J,J')\to\operatorname{Hom}^\bullet(F(a),e_YJ')\),
\(c\mapsto e_Y(c)t\).
This map is a quasi-isomorphism, because \(e_Y\) is one on Homs and \(t\) is a homotopy equivalence. Thus this projection is also a quasi-equivalence; projection to \(J\) is a strict dg functor. Finally apply the free replacement \(Q\) of B.1t to this source and compose its augmentation with the two projections. This gives (B.RK5) with semifree Hom complexes in \(\mathcal A_f\). The endpoint categories have not been replaced. In degree-zero derived categories the roof is still exactly \(Rf_!\), and \(p\) remains surjective on objects. No functorial choice of a K-injective resolution has been asserted.

**One bar kernel retains all source-module actions.** For a right \(\mathcal A_f\)-module \(M\), let \(P_{\mathcal A_f}M\) be its unnormalized augmented bar resolution. Its length-\(n\) terms are
\(M(a_n)\otimes\mathcal A_f(a_{n-1},a_n)\otimes\cdots\otimes
\mathcal A_f(a_0,a_1)\otimes\mathcal A_f(-,a_0)\),
summed over all \(a_0,\ldots,a_n\).
Set
\[
\begin{aligned}
 H_f(J,I)&=q_!P_{\mathcal A_f}\bigl(p^*\mathcal E_X(-,I)\bigr)(J),\\
 H_f^{[n]}(J,I)&=
 \bigoplus_{a_0,\ldots,a_n}
 \mathcal E_X(pa_n,I)\otimes
 \mathcal A_f(a_{n-1},a_n)\\
 &\qquad\otimes\cdots\otimes
 \mathcal A_f(a_0,a_1)\otimes\mathcal E_Y(J,qa_0).
\end{aligned}
\tag{B.RK6}
\]
Every \(n\geq0\) is included, by **direct-sum** totalization. No truncation or product completion is implicit. Give an element of internal degree \(r\) in length \(n\) total degree \(r-n\). The faces, from left to right, first act on \(M\), then compose adjacent arrows, and finally act on the last representable. With the ordinary internal tensor differential, use
\[
 d_{\mathrm{tot}}\big|_{[n]}
   =(-1)^n d_{\mathrm{int}}+\sum_{s=0}^{n}(-1)^s d_s,
 \qquad
 P(\phi)\big|_{[n]}=(-1)^{n|\phi|}\phi
\tag{B.RK7}
\]
for a homogeneous module map \(\phi\); the face sum is zero at length zero in the unaugmented complex. In the last formula \(\phi\) acts on the first factor. Simplicial face identities give \(\delta^2=0\), internal differentials commute with faces, and the factor \((-1)^n\) reverses when a face lowers length. Hence \(d_{\mathrm{tot}}^2=0\). The second sign makes \(P\) an actual dg functor, also for odd homogeneous maps. Right actions on the last factor are unaltered; their Leibniz exponent is the total degree \(r-n\). Source \(I\)-actions in (B.RK6) use the second sign in (B.RK7).

At each test object \(a\), augment \(P M(a)\) by module composition. The section is \(m\mapsto m\otimes1_a\). On an unaugmented word, append its last representable factor as a new bar arrow and put \(1_a\) in the new last position; denote this insertion by \(s_{\mathrm{end}}\). Then
\[
 h_n=(-1)^{n+1}s_{\mathrm{end}},\qquad
 d_{\mathrm{tot}}h+h\,d_{\mathrm{tot}}
     =1-\mathrm{section}\,\mathrm{augmentation}.
\tag{B.RK8}
\]
To verify it, the last face after insertion is the original word, while every other face pairs with insertion after that face with the opposite sign. Internal terms cancel because insertion commutes with the internal differential and changes the length by one. This contraction is objectwise; it is not asserted to be a right-module-linear contraction of the augmentation. It proves the needed quasi-isomorphism for unbounded complexes without a convergence argument.

For \(M=p^*\mathcal E_X(-,I)\), all coefficient complexes in the length filtration are h-projective over \(\Lambda\): the endpoint and source Hom complexes are semifree. Finite tensors of such semifree complexes remain semifree. Each successive bar quotient is a sum of those coefficient complexes tensored with right representables. It is h-projective as a module: Hom into an acyclic module is Hom from the coefficient complex into its acyclic value. The length filtration is split on graded modules. The recursive primitive construction from (B.DA2) applies to these quotients as well: at each length the defect is a closed map into an acyclic Hom complex, and can be filled while preserving all previous lengths. Thus \(P M\) is h-projective, including its infinite union. Induction \(q_!\) preserves h-projectivity by (B.DA4), so every column \(H_f(-,I)\) is h-projective.

Choose an object \(a\) of (B.RK5) with \(pa=I\). Quasi-full faithfulness of \(p\) gives a quasi-isomorphism
\(\mathcal A_f(-,a)\to p^*\mathcal E_X(-,I)\).
Lift this through the bar augmentation using Hom from the representable. The lift is a quasi-isomorphism between h-projectives, hence a homotopy equivalence. Induction sends it to a homotopy equivalence between \(H_f(-,I)\) and \(\mathcal E_Y(-,qa)\). Under the graph above, \(e_Yqa\) is precisely a representative of \(Rf_!e_XI\). This proves the required geometric identification, not merely abstract quasi-representability.

For any right module \(N\), co-Yoneda in the \(I\)-variable gives an actual natural isomorphism of complexes
\[
\begin{aligned}
 N\otimes_{\mathcal E_X}H_f
    &\cong q_!P_{\mathcal A_f}(p^*N),\\
 m\otimes(e\otimes f_n\otimes\cdots\otimes f_1\otimes v)
    &\longmapsto
      (-1)^{n|m|}(me)\otimes f_n\otimes\cdots\otimes f_1\otimes v .
\end{aligned}
\tag{B.RK9}
\]
There are \(n\) internal bar arrows in the second line. Its sign is the tensor–totalization sign. It agrees with the source-action sign in (B.RK7), so the formula is balanced. For the internal differential the exponent on \(dm\) changes by \(n\); for a face it changes by \(|m|\), precisely compensating the tensor differential. This verifies the chain identity. For h-projective \(N\), its values are h-projective over \(\Lambda\), by a representable-cell resolution and the locally semifree Hom complexes of \(\mathcal E_X\). The preceding bar argument therefore still applies. Alternatively, the h-projective columns of \(H_f\) and a cell resolution of \(N\) prove that \(N\otimes H_f\) is h-projective directly. Homotopy representables are sent to homotopy representables.

**The common right-module adjunction has actual units and counits.** For either right kernel \(K=P_g\) or \(K=H_f\), write
\[
\begin{aligned}
 T_K M&=M\otimes_{\mathcal E_X}K,\\
 (U_KN)(I)&=\operatorname{Hom}_{\mathrm{Mod}\text{-}\mathcal E_Y}^\bullet
                         (K(-,I),N),\\
 \operatorname{Hom}^\bullet(T_KM,N)
    &\cong\operatorname{Hom}^\bullet(M,U_KN),\\
 \eta_M(m)(k)&=m\otimes k,\\
 \varepsilon_N(\phi\otimes k)&=\phi(k).
\end{aligned}
\tag{B.RK10}
\]
The Hom-complex bijection sends \(b\) to \(m\mapsto(k\mapsto b(m\otimes k))\). Its inverse is evaluation. The balancing relation is exactly right-module linearity. Differentiating this formula cancels the terms containing \(dk\), with exponent \(|b|+|m|\); hence it holds in every degree. The two triangle identities follow on \(m\otimes k\) and on \(\phi\) by evaluation, before passing to cohomology. Since the columns of \(K\) are h-projective, \(U_K\) preserves quasi-isomorphisms. Its adjunction therefore also proves that \(T_K\) preserves h-projectives.

For \(H_f\), the ordinary exceptional adjoint in B.1e identifies \(U_{H_f}\) on represented targets. More explicitly, choose the representing source object for \(f^!Y\), and represent the ordinary counit by a closed map from its image under \(T_{H_f}\) to \(h_Y\). Its transpose under (B.RK10) gives a right-module map from that representable to \(U_{H_f}h_Y\). On every shifted input its cohomology is the ordinary adjunction bijection, with this very counit, so it is a quasi-isomorphism in every degree. This is the same argument as (B.RG11), now over the common endpoint models. No claim that \(U_{H_f}h_Y\) itself is h-projective is needed.

Use the resolution graph of (B.DA7), now with this \(T_K,U_K\). Its Hom-kernel argument uses only h-projectivity of the resolved source and the target replacement, so is unchanged. If \(r:P\to U_KN\) is the chosen graph object, the maps are
\[
 e_N=\varepsilon_NT_Kr,\qquad
 r_{T_KA}u_A-\eta_A=dk_A.
\tag{B.RK11}
\]
Their actual triangle witnesses are
\[
\begin{aligned}
 e_{T_KA}T_Ku_A-1&=d(\varepsilon_{T_KA}T_Kk_A),\\
 r(r_eu_P-1)&=d(h_eu_P+U_Ke_N\,k_P).
\end{aligned}
\tag{B.RK12}
\]
Here \((e_N,r_e,h_e)\) is a closed lift of the counit through the graph. The second equation and the Hom quasi-isomorphism imply that \(r_eu_P-1\) is a boundary; they do not require a prescribed primitive upstairs to map to that particular primitive downstairs. For compact support the resolved right modules are homotopy representable by the counit argument just given. These formulas thus supply the ordinary exceptional adjunction in the common right-module variance.

**The remaining geometric join is now a map problem with specified endpoints.** In (B.BM15) use \(L_0=T_{H_f}\), \(L_1=T_{H_{f'}}\), \(S=T_{P_u}\), and \(V=T_{P_g}\). All four are now actual dg functors on right modules that preserve h-projectives. The inverse-image composition comparisons are the natural roofs (B.RK2), not nonexistent inverses of the left-module compositors. The compactification and folding comparisons retain the existing spans and all coefficients of B.1s–B.1aa.

It remains to present the **actual** mixed cell (B.GC12)–(B.GC13) as a whole-diagram map between these kernels, including \(t(A_Cs)\theta_k^{-1}\), the nested second coefficient (B.IA12), and the common composition roofs. A comparison merely identifying each represented object, or merely identifying functors on \(H^0\), would not do this. Only after that whole map and its relative faces are supplied may its homotopy inverse be used in (B.BM16)–(B.BM18). The right mate is not thereby an isomorphism. This module-side join does not establish the full exceptional-operation system or coefficient completion. \(\square\)


### Construct the whole-bimodule compact-support base-change cell

**Proposition B.1ae (an actual cell over the common endpoints).** For one cartesian compactification diagram, the proper and open base-change maps define a homotopy equivalence of **whole bimodule** models. Their composite represents the canonical compact-support base-change map. A signed bar construction compares this model with the actual compactification-roof kernel \(H_f\) of (B.RK6), retaining the replacement edges and their homotopies. Its inverse therefore supplies the resolved input to (B.BM16), not just an isomorphism of functors on \(H^0\).

This statement is about the specified diagram and its recorded faces. It does not declare that all changing compactifications, iterated compositions and base changes have already been assembled into one coherent parameter diagram. The geometric hypotheses remain those of (B.RG9), (B.BC3) and (B.CB6): Noetherian separated finite-type compactifications and the stated unbounded ordinary torsion scope, with the common annihilator required by the proper-base-change provider. The algebra below works over the original arbitrary commutative \(\Lambda\); this does not extend the geometric theorem to arbitrary coefficients.

Use the locally semifree endpoint categories \(\mathcal E_T\), with evaluations \(e_T\), from B.1ac. Consider
\[
\begin{array}{ccccc}
 X'&\xrightarrow{\ j'\ }&U'&\xrightarrow{\ h'\ }&Y'\\
 {\scriptstyle u}\downarrow&&{\scriptstyle v}\downarrow&&
                    \downarrow{\scriptstyle g}\\
 X&\xrightarrow{\ j\ }&U&\xrightarrow{\ h\ }&Y .
\end{array}
\qquad f=hj,\quad f'=h'j'.
\tag{B.KC1}
\]
Both squares are cartesian; \(j,j'\) are open immersions and \(h,h'\) are proper. This is a diagram of the actual schemes and maps, not a claim that inverse image preserves K-injective complexes. Every unnamed tensor associator and direct-image comparison below is its canonical one.

**Choose resolutions in both variables at once.** For an inverse image \(a^*:D(T)\to D(T')\), an open extension \(j_!:D(X)\to D(U)\), and a proper image \(h_*:D(U)\to D(Y)\), the raw left kernels are
\[
\begin{aligned}
 B_a(J,I)&=\operatorname{Hom}^{\bullet}(e_TI,a_*e_{T'}J),\\
 B_j(J,I)&=\operatorname{Hom}^{\bullet}(e_XI,j^*e_UJ),\\
 B_h(J,I)&=\operatorname{Hom}^{\bullet}(h_*e_UI,e_YJ).
\end{aligned}
\tag{B.KC2}
\]
They are covariant in \(J\) and contravariant in \(I\). The first two formulas are the actual complex-level adjunctions. The functors \(a_*\), \(j^*\) and \(h_*\) occurring here preserve K-injectives: each has the appropriate exact left adjoint. Proper direct image is not being called exact.

Resolve each kernel as a left module over
\(\mathcal E_{\mathrm{target}}\otimes\mathcal E_{\mathrm{source}}^{\mathrm{op}}\).
For an inverse image, take a whole semifree replacement \(L_a\to C_a\) of the existing kernel (B.IP10), and then its augmentation to \(B_a\). For the open and proper kernels take whole semifree replacements \(L_j\to B_j\) and \(L_h\to B_h\). The many-object construction (B.DA2), applied to these product categories, supplies these maps.

These are stronger replacements than separate columnwise choices. An exterior representable cell, evaluated in either variable, is a representable module tensored with a semifree endpoint Hom complex. The filtration proof (B.ND2), (B.ND6) therefore makes every row and column h-projective and K-flat. A tensor of two whole semifree kernels is again whole h-projective: tensor two exterior cells over the middle category and apply co-Yoneda. The resulting exterior cell has as its coefficient a middle Hom complex, which is semifree over \(\Lambda\). Filter first by the two cell stages and then by that coefficient's path filtration. Differentials decrease this order. The recursive primitive argument of B.1u proves h-projectivity into every objectwise acyclic bimodule; the corresponding split filtration proves K-flatness. Direct sums and limit stages cause no convergence problem.

Each \(L_F(-,I)\) is homotopy corepresentable by the actual derived image of \(eI\). For \(a,j\), choose a K-injective replacement of the exact image and use adjunction. For \(h\), the object \(h_*e_UI\) is already K-injective. The evaluation quasi-equivalence and a lift from a corepresentable give a quasi-isomorphism between h-projectives, hence a homotopy equivalence. This argument also proves that \(L_h\otimes L_j\) is homotopy corepresentable by \(h_*B\) when \(j_!e_XI\to B\) is a K-injective replacement. It does **not** identify this composite with the unresolved expression \(h_*j_!e_XI\).

**The proper cell before any inverse is chosen.** Put
\[
\begin{aligned}
 M(Q,I)&=\operatorname{Hom}^{\bullet}_Y(h_*e_UI,g_*e_{Y'}Q),\\
 \chi_{\mathrm{raw}}(w\otimes z)
      &=g_*(w)\,\kappa_K\,h_*(z),\\
 \kappa_K:\ h_*v_*e_{U'}K&\xrightarrow{\ \sim\ }g_*h'_*e_{U'}K .
\end{aligned}
\tag{B.KC3}
\]
Here \(z:e_UI\to v_*e_{U'}K\) and
\(w:h'_*e_{U'}K\to e_{Y'}Q\). Thus \(\chi_{\mathrm{raw}}\) is defined on
\(B_{h'}\otimes_{\mathcal E_{U'}}B_v\).
The square of direct images supplies the closed canonical \(\kappa\).
Composition and its homogeneous naturality prove the balancing relation and the chain-map identity. No homogeneous factors are interchanged.

If \(q_z:v^*e_UI\to e_{U'}K\) is the adjoint of \(z\), transposing the output of (B.KC3) under \(g^*\dashv g_*\) gives
\[
 \operatorname{Adj}_g\bigl(\chi_{\mathrm{raw}}(w,z)\bigr)
   =w\,h'_*(q_z)\,\beta_{h,e_UI}.
\tag{B.KC4}
\]
Indeed substitute the unit-and-counit definition (B.BC2) of \(\beta\). Naturality moves the units past \(z,w\); the two adjunction triangles cancel the inserted counits and units. What remains is exactly \(g_*w\,\kappa_Kh_*z\). This proves equality for every homogeneous \(z,w\), not merely for cohomology classes.

Let \(A=L_{h'}\otimes L_v\) and \(B=L_g\otimes L_h\). Augment the first word and apply (B.KC3), giving \(\chi:A\to M\). Augment the second word and compose maps
\(h_*e_UI\to e_YK\to g_*e_{Y'}Q\), giving \(\pi:B\to M\).
Both maps are quasi-isomorphisms. For \(\pi\), fix \(I\), replace \(L_h(-,I)\) by its homotopy-corepresentable model and apply co-Yoneda; the remaining map is the inverse-image kernel augmentation. For \(\chi\), replace \(L_v(-,I)\) by a corepresentable associated to
\(q:v^*e_UI\to e_{U'}K_0\). Under this comparison, (B.KC4) is precomposition by
\((h'_*q)\beta_{h,e_UI}\). This is the exact quasi-isomorphism of (B.BC3). Hom into the K-injective \(e_{Y'}Q\) preserves that quasi-isomorphism. This proof does not apply \(h'_*\) to an arbitrary quasi-isomorphism.

Since \(A\) is whole h-projective, (B.ND7) gives closed \(\lambda_h\) and degree-minus-one \(\omega_h\), in the whole bimodule Hom complex, with
\[
 \lambda_h:A\longrightarrow B,\qquad
 \pi\lambda_h-\chi=d\omega_h.
\tag{B.KC5}
\]
The map \(\lambda_h\) is a quasi-isomorphism between whole h-projectives, hence a **bimodule-linear homotopy equivalence**. To see the last assertion directly, lift the identity of the target through the Hom quasi-isomorphism induced by \(\lambda_h\). This gives a closed inverse with one composite homotopic to the identity. Applying the other Hom quasi-isomorphism makes the second composite a boundary as well. Both witnesses are bimodule-linear; no family of pointwise inverses has been promoted to a natural inverse.

**The open cell uses its actual right-adjoint mate.** The exact open-base-change isomorphism and its right-adjoint mate are
\[
 \theta:v^*j_!\xrightarrow{\ \sim\ }j'_!u^*,
 \qquad
 \theta^R:u_*j'^*\xrightarrow{\ \sim\ }j^*v_* .
\tag{B.KC6}
\]
For the mate, evaluate a sheaf on an open of \(X\): both sides restrict the direct image of the same sheaf on its inverse image in \(U'\). The maps agree with the adjunction units and restrictions. Thus this is the canonical isomorphism on complexes and all homogeneous maps, not an arbitrary identification.

Set \(A_o=L_{j'}\otimes L_u\), \(B_o=L_v\otimes L_j\).
Composition after the augmentations gives
\[
\begin{aligned}
 A_o(J,I)&\longrightarrow
       \operatorname{Hom}^{\bullet}_X(e_XI,u_*j'^*e_{U'}J),\\
 B_o(J,I)&\xrightarrow{\ \pi_o\ }
       \operatorname{Hom}^{\bullet}_X(e_XI,j^*v_*e_{U'}J)=M_o(J,I).
\end{aligned}
\tag{B.KC7}
\]
These maps are quasi-isomorphisms. Reduce the first exact operation to its corepresentable replacement, then use co-Yoneda; exactness of the second operation preserves the chosen replacement. Composing the first line with \(\theta^R\) gives \(\chi_o:A_o\to M_o\). Whole h-projectivity gives a closed \(\lambda_j:A_o\to B_o\) and a whole witness
\(\pi_o\lambda_j-\chi_o=d\omega_o\), exactly as in (B.KC5). It is again a whole-bimodule homotopy equivalence.

With \(W_f=L_h\otimes L_j\), the resulting left-kernel comparison is the explicit two-step map
\[
\begin{aligned}
 W_{f'}\otimes L_u
  &\xrightarrow{\ 1\otimes\lambda_j\ }
                L_{h'}\otimes L_v\otimes L_j\\
  &\xrightarrow{\ \lambda_h\otimes1\ }
                L_g\otimes W_f .
\end{aligned}
\tag{B.KC8}
\]
The indicated factors fix the variance and order. Tensoring preserves the actual inverse maps and homotopies, so (B.KC8) is a whole homotopy equivalence. It is the left-module, hence opposite, version of
\(g^*Rf_!\to Rf'_!u^*\). To use it with (B.RK10), we still have to connect \(W_f\) to the **existing** right-roof kernel; agreement on represented objects alone is not sufficient.

**A signed bar map carries the graph homotopies.** We give that connection rather than appeal to uniqueness on \(H^0\). Let \(N_0,N_1\) be left modules on a dg category \(\mathcal A\), possibly also carrying a commuting target-module structure. Suppose there are closed degree-zero object maps \(\alpha_a\) and degree-\((|t|-1)\) maps \(k_t\) such that
\[
\begin{aligned}
 dk_t+k_{dt}&=\alpha_bN_0(t)-N_1(t)\alpha_a,\\
 k_{st}&=k_sN_0(t)+(-1)^{|s|}N_1(s)k_t,\qquad k_{1_a}=0 .
\end{aligned}
\tag{B.KC9}
\]
These are the differential, composition and unit relations in the actual resolution graph (B.RG2)–(B.RG3). For a right module \(M\), use the direct-sum two-sided bar with total degree internal degree minus length, and differential (B.RK7). There is a map to the ordinary balanced tensor \(M\otimes_{\mathcal A}N_1\):
\[
\begin{aligned}
 \Psi(m\otimes x)&=m\otimes\alpha_a x&&(\text{length }0),\\
 \Psi(m\otimes t\otimes x)
   &=(-1)^{|m|+1}m\otimes k_t x&&(\text{length }1),\\
 \Psi\big|_{[n]}&=0&& (n\geq2).
\end{aligned}
\tag{B.KC10}
\]
For length one the chain defect is minus
\(m\otimes(dk_t+k_{dt})x\); the two face terms are
\(m\otimes(N_1(t)\alpha-\alpha N_0(t))x\).
For length two the remaining expression, after factoring
\((-1)^{|m|+1}\), is
\((-1)^{|s|}N_1(s)k_t-k_{st}+k_sN_0(t)\), which is zero by (B.KC9). Higher lengths give zero. Length zero uses \(d\alpha=0\). This verifies every bar length, including the internal differential.

The map is natural for homogeneous maps of \(M\), with the factor
\((-1)^{n|\phi|}\) of (B.RK7) on length \(n\); the degree of \(m\) in the second line makes the two routes agree. It is also natural in any commuting target variable, using the ordinary Koszul interchange. If \(M\) is h-projective and every \(\alpha_a\) is a quasi-isomorphism, then \(\Psi\) is a quasi-isomorphism. For \(M=\mathcal A(-,a)\), the endpoint insertion contraction of (B.RK8) identifies the source with \(N_0(a)\); its section followed by \(\Psi\) is exactly \(\alpha_a\). For a semifree \(M\), use its graded-split cell filtration: the assertion holds on each shifted representable quotient, then on the successive extensions and their unions. A general h-projective is homotopy equivalent to its semifree replacement, and both constructions preserve the homotopies with the same length signs. No flatness of the \(N_i(a)\), finite bar truncation, or module-linear endpoint contraction is assumed.

Here is the opposite convention needed for the geometric graph. If
\(s_a:F_0a\to F_1a\), with graph homotopies \(h_t\), apply
\(\operatorname{Hom}^{\bullet}(-,J)\). On \(\mathcal A^{\mathrm{op}}\) the two left modules are \(N_0(a)=\operatorname{Hom}(F_1a,J)\) and
\(N_1(a)=\operatorname{Hom}(F_0a,J)\). For \(t:a\to b\) and homogeneous \(\phi:F_1b\to J\), their comparison is
\[
 \alpha_a(\psi)=\psi s_a,\qquad
 \widehat h_{t^{\mathrm{op}}}(\phi)
    =(-1)^{(|t|-1)|\phi|+1}\phi h_t .
\tag{B.KC11}
\]
Here \(\psi:F_1a\to J\). The action of \(t^{\mathrm{op}}\) is
\(\phi\mapsto(-1)^{|t||\phi|}\phi F_i(t)\).
Differentiating the second formula cancels its two \(d\phi\) terms; the remaining terms are
\(-(-1)^{|t||\phi|}\phi(dh_t+h_{dt})\), precisely
\(\alpha N_0(t^{\mathrm{op}})-N_1(t^{\mathrm{op}})\alpha\).
Composition follows by inserting the graph composition and the dg-opposite sign \((-1)^{|s||t|}\). Thus (B.KC10) applies with its signs specified, rather than with an unspecified “opposite homotopy.”

**Compare the actual compactification graph.** Refine (B.RK5) by also lifting its middle K-injective to \(\mathcal E_U\). Before the free replacement its objects are
\((I,K,J;s,t)\), with
\(s:j_!e_XI\to e_UK\) a quasi-isomorphism and
\(t:h_*e_UK\to e_YJ\) a homotopy equivalence. Its morphisms retain the two graph homotopies for \(s,t\). Forgetting \(K\) by evaluation gives a strict map to the raw graph used in (B.RK5). Both graphs project quasi-equivalently to \(\mathcal E_X\): the new middle Hom kernel is the shifted cone of
\(\mathcal E_U(K,K')\to\operatorname{Hom}(j_!e_XI,e_UK')\);
it is acyclic by evaluation and the replacement \(s\). The output kernel is the one already checked in B.1ad. Therefore the forgetful map is also a quasi-equivalence.

The construction \(Q\) in (B.SF1) is functorial on these **strict** maps. Send \(c_z\) to \(c_{Fz}\), and at each later stage send \(e_{n,z,m}\) to \(e_{n,QF(z),F(m)}\). The defining differential and augmentation equations are preserved, including the formally labelled zero cycles. Hence we obtain a commuting diagram
\[
\begin{array}{ccc}
 \mathcal A_f^+&\xrightarrow{\ \rho\ }&\mathcal A_f\\
 {\scriptstyle p^+}\downarrow&&\downarrow{\scriptstyle p}\\
 \mathcal E_X&=&\mathcal E_X,
\end{array}
\qquad q^+=q\rho .
\tag{B.KC12}
\]
All three source Hom complexes are in the stated semifree models, and \(\rho\) is a quasi-equivalence. This use of \(Q\) on strict functors does not apply it directly to an \(A_\infty\) map.

The replacement \(s\) gives the objectwise quasi-isomorphism
\(\mathcal E_U(K,-)\to B_j(-,p^+a)\),
\(z\mapsto e_U(z)s\). Its homotopy is obtained from the \(s\)-edge by (B.KC11). After tensoring with the K-flat row \(L_h(J,-)\), co-Yoneda gives the comparison from \(L_h(J,K)\) to
\((L_h\otimes B_j)(J,p^+a)\). The augmentation
\(W_f\to L_h\otimes B_j\) is a quasi-isomorphism. The second edge \(t\) gives
\(\mathcal E_Y(q^+a,J)\to B_h(J,K)\),
\(z\mapsto e_Y(z)t\), with its recorded \(t\)-homotopy; insert also the augmentation \(L_h(J,K)\to B_h(J,K)\).
For the intermediate raw Hom functors, evaluation from the endpoint representables is a quasi-isomorphism. All these arrows are thus justified in their actual directions.

Apply (B.KC10) to each of these graph comparisons over
\((\mathcal A_f^+)^{\mathrm{op}}\), retaining a bar source and its augmentation for each arrow. Resolve the whole parameter modules before tensoring. It gives a zigzag of actual bimodule quasi-isomorphisms, natural in both \(I,J\), between \(W_f(J,I)\) and the derived coend
\(\mathcal E_Y(q^+-,J)\otimes_{\mathcal A_f^+}^{\mathbb L}
\mathcal E_X(I,p^+-)\).
Indeed induction along the quasi-equivalence \(p^+\) identifies the coend with the original left \(\mathcal E_X\)-parameter by (B.SM1)–(B.SM2). The two augmentations and the length-one terms retain \(s,t\) and their homotopies. They have not been replaced by a pointwise naturality claim.

We identify this coend with the dual of the old \(H_f\) explicitly. Write
\(R_I=P_{\mathcal A_f}(p^*\mathcal E_X(-,I))\), a homotopy-representable right module, and
\(R_I^\vee(a)=\operatorname{Hom}^{\bullet}_{\mathrm{Mod}-\mathcal A_f}
(R_I,\mathcal A_f(-,a))\).
Put \(Z_{I,a}=\operatorname{Hom}^{\bullet}_{\mathcal A_f}
(R_I,p^*\mathcal E_X(-,pa))\). There is a natural zigzag
\[
 \mathcal E_X(I,pa)\longrightarrow Z_{I,a}
       \longleftarrow R_I^\vee(a).
\tag{B.KC13}
\]
The first arrow is restricted Yoneda followed by the bar augmentation; it is a quasi-isomorphism by the full mapping-complex equivalence of (B.SM1)–(B.SM2). The second is induced by the canonical
\(\mathcal A_f(-,a)\to p^*\mathcal E_X(-,pa)\), and is a quasi-isomorphism since \(R_I\) is h-projective. This proves the assertion in every degree and in both parameters.

For \(N=q^*\mathcal E_Y(-,J)\), evaluation gives
\[
\begin{aligned}
 N\otimes_{\mathcal A_f}R_I^\vee
  &\longrightarrow \operatorname{Hom}^{\bullet}_{\mathcal A_f}(R_I,N),\\
 v\otimes\phi&\longmapsto\bigl(x\longmapsto v\,\phi(x)\bigr),\\
 \operatorname{Hom}^{\bullet}_{\mathcal A_f}(R_I,N)
  &\cong
 \operatorname{Hom}^{\bullet}_{\mathcal E_Y}
             (H_f(-,I),\mathcal E_Y(-,J)).
\end{aligned}
\tag{B.KC14}
\]
The first map is balanced, right-linear and a chain map, with the right-module convention of B.1ad. It is a quasi-isomorphism: \(R_I\) is homotopy equivalent to a representable, for which it is exactly co-Yoneda. The last line is the literal induction–restriction adjunction, since \(H_f=q_!R_I\). Use whole replacements of (B.KC13) before any tensor that needs to preserve a quasi-isomorphism; no ordinary tensor of unresolved nonflat modules is being substituted for a derived one.

Changing \(\mathcal A_f^+\) to \(\mathcal A_f\) is also an actual bar map: apply \(\rho\) to every object and internal arrow in (B.RK6). All faces and length signs commute. It is a quasi-isomorphism by the induction–restriction equivalence for \(\rho\); after replacing the two source modules by h-projectives the comparison is a homotopy equivalence, and induction preserves it. Both resulting right bar kernels are whole h-projective: filter by bar length, then by the path weights of their internal Hom coefficients; the outer factors are exterior endpoint representables. Thus this comparison retains whole, not just columnwise, naturality.

Equations (B.KC10)–(B.KC14) identify \(W_f\), by actual quasi-isomorphism roofs, with the right-Yoneda dual of \(H_f\). Double Yoneda evaluation is a quasi-isomorphism on each column because that column is homotopy representable. After whole endpoint replacements these roofs give the comparison of \(D W_f\) with \(H_f\), where \(D\) is the left-to-right dual (B.RK1). This proves the needed roof connection with the original geometric graph, not just with another functor having the same \(H^0\).

**Return to right-module base change and the resolved mate.** Dualize (B.KC8); use the signed composition evaluations (B.RK2)–(B.RK4) and the preceding roof comparisons. For inverse images the map \(L_a\to C_a\) gives \(D C_a\to D L_a\), a natural columnwise homotopy equivalence, so the endpoints are the existing \(P_a\). Resolve the full right kernels before selecting inverses. We obtain the comparison roof
\[
\begin{aligned}
 H_f\otimes_{\mathcal E_Y}P_g
    &\xrightarrow{\ \beta_f\ }P_u\otimes_{\mathcal E_{X'}}H_{f'},\\
 T_{P_g}T_{H_f}&\longrightarrow T_{H_{f'}}T_{P_u}.
\end{aligned}
\tag{B.KC15}
\]
The first line uses balanced right tensor order: compact support and then base change on the left, base change and then compact support on the right. The arrow is represented on the common whole h-projective kernel models just constructed. Its inverse and both homotopies exist there, not on an unresolved target.

To identify the map, evaluate on a replacement string
\(s:j_!e_XI\to B\), \(r:v^*B\to C\). The proper factor is
\((h'_*r)\beta_{h,B}\) by (B.KC4), and the common open edge is
\(r(v^*s)\theta^{-1}\) by (B.KC6)–(B.KC7). These are exactly (B.CB5)–(B.CB6). The length-one bar terms are the graph edge homotopies, with (B.KC11)'s signs. If a higher fold has first been replaced by its strict \(UQ\) roof, its higher coefficients are already the images of the free words; (B.KC10) does not discard them. In particular the second coefficient of (B.IA12) must remain when this cell is inserted into the composition square. The identical-word identities (B.GC12)–(B.GC13) specify those boundary comparisons; a joint global lift is an additional requirement.

Now put \(L_0=T_{H_f}\), \(L_1=T_{H_{f'}}\), \(S=T_{P_u}\), \(V=T_{P_g}\) in the common models, and let \(\vartheta:L_1S\to VL_0\) be the inverse of (B.KC15). For a resolved \(r_0:P_0\to U_0N\), set \(e_0=\varepsilon_0L_0r_0\). The exact resolved mate equations are
\[
\begin{aligned}
 \zeta&=\operatorname{Adj}_{L_1}(V e_0\,\vartheta_{P_0}),\\
 r_1c-\zeta&=db,\\
 e_1L_1c-Ve_0\,\vartheta_{P_0}
       &=d(\varepsilon_1L_1b).
\end{aligned}
\tag{B.KC16}
\]
Here \(r_1:P_1\to U_1VN\); \(c:SP_0\to P_1\) and its witness are lifted in the whole natural Hom complex as in (B.BM16). These are the actual unit/counit adjunction maps (B.RK10). Neither \(\vartheta_{U_0N}\) nor an inverse on an unresolved right adjoint is used. The unit witness and both pasting witnesses are precisely (B.BM16)–(B.BM18) with this supplied cell and its comparison roofs. The right mate is not thereby an isomorphism.

The one-square whole-bimodule map has the stated comparison with the compact-support roof. What remains is the simultaneous relative assembly over changing compactifications and composition/base-change arrays, with their specified (B.GC13) and (B.IA12) faces and both inverse homotopies. That requires checking the boundaries of the full free parameter presentation before (B.ND9) is applied; it is not implied by independent choices of the above lifts. Geometric nearby multiplicative descent, normalized coefficient-system transport and strict-heart effacement are not established by this construction. \(\square\)


### The proper–open kernel and the common mixed cube

**Proposition B.1af (one common target for the six vertices).** Keep the Noetherian, separated finite-type, unbounded ordinary torsion scope and the locally semifree endpoint categories of B.1ae. The actual mixed cube (B.GC12) has a comparison in whole bimodules, with an explicit boundary for its two composite routes. Its proper–open edge is the derived exchange of (B.GC3), and its common target uses the actual sheaf maps, not an arbitrary identification of represented objects. The comparison can be lifted relative to the supplied graph and nested-resolution faces. The global changing-array assembly is not inferred merely from this elementary cube.

Use the two-map square (B.GC1). To avoid confusing a geometric functor with a kernel, retain \(L=i_!\), \(K=k_!\), \(H=h_*\), \(P=p_*\), and write \(\mathbb L_F\) for the whole left kernel of an elementary operation \(F\). Thus \(\mathbb L_G\otimes\mathbb L_F\) represents the opposite of \(GF\). Tensors below are balanced over their indicated intermediate endpoint categories, with the canonical associators.

**The missing proper–open edge.** For \(I\in\mathcal E_U\), \(J\in\mathcal E_D\), set
\[
\begin{aligned}
M_\epsilon(J,I)&=\operatorname{Hom}^{\bullet}(LH e_UI,e_DJ),\\
\chi_\epsilon(w\otimes z)&=w\,P(z)\,\epsilon_{e_UI},\\
z&:K e_UI\longrightarrow e_CA,\qquad
w:P e_CA\longrightarrow e_DJ .
\end{aligned}
\tag{B.MX1}
\]
The input of the second line is \(B_P\otimes_{\mathcal E_C}B_K\). The raw open kernel is written using its adjunction, as in (B.KC2). The other word has the composition map
\(B_L\otimes_{\mathcal E_Y}B_H\to M_\epsilon\).
Both formulas are balanced chain maps: the middle action moves through \(P\), and the homogeneous Leibniz rule is the rule for ordered composition. There is no permutation of \(w,z\).

Augment the whole kernels and denote the resulting maps by \(\chi\) and \(\pi\). They give
\[
\mathbb L_P\otimes\mathbb L_K
 \xrightarrow{\ \chi\ }M_\epsilon
 \xleftarrow{\ \pi\ }\mathbb L_L\otimes\mathbb L_H,
\qquad
\pi\lambda_\epsilon-\chi=d\omega_\epsilon .
\tag{B.MX2}
\]
Here \(\lambda_\epsilon\) points from the left word to the right word; \(|\omega_\epsilon|=-1\). To prove both arrows are quasi-isomorphisms, fix \(I\). Since \(H e_UI\) is K-injective, reducing its homotopy-corepresentable column and applying co-Yoneda identifies the right word with the mapping complex for the exact \(L\)-image. For the left word choose \(s:K e_UI\to C_0\) with K-injective target. The same reduction identifies \(\chi\) with precomposition by
\((P s)\epsilon_{e_UI}:LH e_UI\to P C_0\).
This is precisely the quasi-isomorphism proved in (B.GC3), using B.1n on the original K-injective input. Hom into \(e_DJ\) preserves it. This argument does not apply \(P\) to an arbitrary quasi-isomorphism.

Both word kernels are whole h-projective by B.1ae. Thus (B.ND7) supplies \(\lambda_\epsilon,\omega_\epsilon\) in the whole bimodule Hom complex. As in (B.KC5), \(\lambda_\epsilon\) has a bimodule-linear homotopy inverse and both inverse witnesses. This is the actual derived proper–open exchange, with the variance reversed by the left kernel.

**All six objects, with their maps to the same target.** Pull the square back along \(D'\to D\), with notation as in (B.GC12). Put
\[
\begin{array}{c|c|c}
v&F_v&\tau_v:A_DLH\longrightarrow F_v\\ \hline
0&A_DLH&1\\
1&A_DPK&A_D\epsilon\\
2&P'A_CK&(\beta_pK)(A_D\epsilon)\\
3&P'K'A_U&(P'\theta_k)(\beta_pK)(A_D\epsilon)\\
4&L'A_YH&\theta_iH\\
5&L'H'A_U&(L'\beta_h)(\theta_iH).
\end{array}
\tag{B.MX3}
\]
The six directed edges on geometric operations are
\(0\to1\to2\to3\) and \(0\to4\to5\to3\).
Their labels are, respectively,
\(A_D\epsilon,\beta_pK,P'\theta_k\) and
\(\theta_iH,L'\beta_h,\epsilon'A_U\).
Equation (B.GC12) says that the last route also has composite \(\tau_3\), as an actual natural map on complexes.

Let \(W_v\) be the ordered tensor of whole kernels for the letters of \(F_v\), and set
\[
M_\square(J,I)
 =\operatorname{Hom}^{\bullet}
       (A_DLH e_UI,e_{D'}J),\qquad
a_v:W_v\longrightarrow M_\square .
\tag{B.MX4}
\]
These maps have a concrete definition. For a word \(F_m\cdots F_1\), augment its kernel factors to maps
\(z_b:F_b eI_{b-1}\to eI_b\). Compose them in the order
\(z_mF_m(z_{m-1})\cdots(F_m\cdots F_2)(z_1)\), then precompose with \(\tau_v\).
This is a balanced chain map natural in both endpoints. Intermediate images need not be K-injective for this raw composition to be defined. Their derived meaning is established separately below; raw direct image is not declared exact.

Every \(a_v\) is a quasi-isomorphism. The following reductions check all six cases, not only the two endpoints.

- For \(v=0\), \(H\) is applied to the original K-injective input; \(L,A_D\) are exact. Successive corepresentable reductions compute precisely the source of (B.MX4).
- For \(v=1\), choose \(s:K e_UI\to C_0\) with K-injective target. Its map from the source is \(A_D((Ps)\epsilon_{e_UI})\), a quasi-isomorphism by (B.GC3) and exactness of \(A_D\).
- For \(v=2\), also choose \(t:A_CC_0\to D_0\). The map is the left side of (B.GC13). Its two proper comparisons have exactly the K-injective inputs required there.
- For \(v=4\), use the open-base-change isomorphism \(\theta_iH\); the subsequent \(A_Y,L'\) operations are exact.
- For \(v=5\), choose \(u:A_U e_UI\to B'\) with K-injective target. The comparison is
  \(L'((H'u)\beta_{h,e_UI})\theta_{i,H e_UI}\).
  Equation (B.BC3), followed by exact \(L'\), proves it is a quasi-isomorphism.
- For \(v=3\), additionally choose \(v':K'B'\to D'\!_0\) with K-injective target. The comparison is
  \((P'v')\epsilon'_{B'}L'((H'u)\beta_{h,e_UI})\theta_{i,H e_UI}\),
  the standard lower route in the paragraph following (B.GC13). That proof establishes its quasi-isomorphism, retaining both replacements.

In each reduction, a kernel column is replaced through an actual homotopy equivalence to its corepresentable. Tensoring preserves that homotopy. The remaining map is precomposition into the K-injective final endpoint. Thus no flatness of unresolved sheaves or exactness of a proper image is assumed. The resulting objectwise quasi-isomorphisms are quasi-isomorphisms of the whole bimodules because the maps themselves are already natural.

**The edge witnesses belong to this common comparison.** For an edge \(u\to v\), choose
\[
\lambda_{uv}:W_v\longrightarrow W_u,\qquad
a_u\lambda_{uv}-a_v=d\omega_{uv}.
\tag{B.MX5}
\]
Whole h-projectivity and (B.ND7) give both entries. Each \(\lambda_{uv}\) is a whole homotopy equivalence. They can represent the elementary maps of (B.KC5), (B.KC7), and (B.MX2), with the other factors retained. Indeed the augmented elementary formula is exactly precomposition with its labelled sheaf map in (B.MX3). Whiskering its original witness gives (B.MX5); the equality of raw composites supplies no extra term. For a witness in a right tensor factor the action is
\((1\otimes\omega)(x\otimes y)=(-1)^{|x|}x\otimes\omega(y)\).
This is the ordinary graded tensor rule, so the assertion concerns homogeneous natural maps, not just degree-zero elements. If a different whole lift was already chosen, apply the same Hom quasi-isomorphism to their difference; retain the resulting comparison homotopy rather than replacing the previous lift without a witness.

Here is the kernel diagram. Its arrows run opposite to those on the geometric operations:
\[
\begin{array}{ccccc}
W_0&\xleftarrow{\lambda_{01}}&W_1&\xleftarrow{\lambda_{12}}&W_2\\
{\scriptstyle\lambda_{04}}\uparrow&&&&
                   \uparrow{\scriptstyle\lambda_{23}}\\
W_4&\xleftarrow{\lambda_{45}}&W_5&\xleftarrow{\lambda_{53}}&W_3 .
\end{array}
\qquad a_v:W_v\longrightarrow M_\square .
\tag{B.MX6}
\]
The common target identifies which maps this diagram compares. Replacing \(a_3\) by an arbitrary isomorphism class would lose that information.

**The whole two-route boundary, including its witness.** Define
\[
\begin{aligned}
T&=\lambda_{01}\lambda_{12}\lambda_{23},
& B&=\lambda_{04}\lambda_{45}\lambda_{53},\\
\Omega_T&=\omega_{01}\lambda_{12}\lambda_{23}
                  +\omega_{12}\lambda_{23}+\omega_{23},\\
\Omega_B&=\omega_{04}\lambda_{45}\lambda_{53}
                  +\omega_{45}\lambda_{53}+\omega_{53},\\
d(\Omega_T-\Omega_B)&=a_0(T-B).
\end{aligned}
\tag{B.MX7}
\]
The two telescoping sums follow directly from (B.MX5). All \(\lambda\)'s are closed of degree zero; no Koszul sign is omitted in these sums.

The necessary filler is stronger than \(T=B\) on cohomology:
\[
dH=T-B,\qquad
a_0H-(\Omega_T-\Omega_B)=dK,\qquad
|H|=-1,\quad |K|=-2 .
\tag{B.MX8}
\]
To prove both equations simultaneously, use the actual resolution category of the common target. Its objects are pairs \((W,a:W\to M_\square)\), with \(W\) whole h-projective and \(a\) a quasi-isomorphism. A degree-\(n\) map is a triple \((b,f,h)\), with
\(b:{M_\square}\to M_\square\), \(f:W\to W'\) of degree \(n\) and \(h:W\to M_\square\) of degree \(n-1\). Its differential and composition are
\[
\begin{aligned}
D(b,f,h)&=(db,df,a'f-ba-dh),\\
(c,g,k)(b,f,h)&=(cb,gf,kf+(-1)^{|c|}ch).
\end{aligned}
\tag{B.MX9}
\]
These are the graph formulas (B.DA7). The identities \(D^2=0\), associativity and the signed Leibniz rule follow by expansion, using \(da=da'=0\). Projection onto \(b\) is surjective in each graded degree. Its Hom kernel is the shifted cone of
\(\operatorname{Hom}(W,W')\xrightarrow{a'\circ-}\operatorname{Hom}(W,M_\square)\);
it is acyclic because \(W\) is whole h-projective.

The edges in (B.MX5) are the closed triples \((1,\lambda_{uv},\omega_{uv})\). Their composite difference is the kernel cycle
\((0,T-B,\Omega_T-\Omega_B)\).
Acyclicity supplies its primitive \((0,H,K)\), which is exactly (B.MX8). In particular the chosen six edge witnesses are retained, not replaced by unrelated pointwise choices. A map \(H\) satisfying only the first equation would not yet compare those witnesses.

**The relative boundary is specified before it is lifted.** Start with the free path category on the six reversed edges. Adjoin a degree-minus-one arrow \(c:3\to0\) with
\[
dc=e_{01}e_{12}e_{23}-e_{04}e_{45}e_{53},
\qquad d^2c=0 .
\tag{B.MX10}
\]
The target functor sends every vertex to \(M_\square\), every edge to \(1\), and \(c\) to \(0\); hence it respects this differential. The already chosen edge triples form its relative boundary lift. Equation (B.ND9), applied to (B.MX9), supplies the lift of \(c\); its two non-base components are \(H,K\). This is an application to a checked free presentation, not to a quotient with an unverified commutativity relation.

For comparison of different composites of these lifts, the next standard free boundary is
\[
\begin{aligned}
\Xi_{c,b,a}
 &=L(c)H_{b,a}-H_{cb,a}+H_{c,ba}-H_{c,b}L(a),\\
d\Xi_{c,b,a}&=0 .
\end{aligned}
\tag{B.MX11}
\]
Here \(dH_{b,a}=L(b)L(a)-L(ba)\), and the symbols denote closed degree-zero edges of the specified target diagram. Expanding the four differentials cancels each ordered triple product. When these are resolution-graph lifts of the same target composition, their full graph obstruction has zero base component and is a cycle in the same acyclic kernel. It therefore has a degree-minus-two primitive, including the next witness component. Longer boundaries are supplied by the already specified free dg index and its differential, not guessed from a list of pairwise homotopies. This explains exactly the relative hypothesis needed when inserting this cube into a larger array.

**Retain the original graphs, bars and nested coefficient.** Use the two replacement strings in (B.GC13), not a new claim that \(A_U e_UI\) is K-injective. Their folds compare the objects
\(z=t(A_Cs)\theta_k^{-1}\) and \(z=v'(K'u)\).
For each homogeneous selected-edge word, (B.GC13) proves equality after the specified outer proper comparisons. Its first coefficients retain the endpoint maps, and its higher endpoint maps vanish while the graph homotopies remain present.

Pass to the strict \(UQ\) roofs already constructed in (B.SF7). The two-sided bar of a strict functor applies that functor to every object and every arrow in each bar tensor. It preserves the internal differential, multiplication faces and identity insertions because those are precisely the strict dg-functor identities. It also preserves ordered composition of strict functors. The quasi-equivalence comparisons are the ones proved in (B.KC12)–(B.KC14), with whole replacements made before tensoring. These statements therefore give maps on the actual bar kernels, not merely an identification of their representing objects.

For the nested right-resolution face, this strict roof must still contain
\[
K_2(S,T)=(0,0,\beta^*k_S h_T),
\qquad
\text{ordinary multiplicativity witness}
       =(-1)^{|S|+1}K_2(S,T).
\tag{B.MX12}
\]
This is (B.IA12), in its suspended convention. The strictification evaluates its free words using both \(K_1\) and \(K_2\); it does not replace \(K\) by \(K_1\). The graph-to-bar transfer uses (B.KC10)'s length-one sign and (B.KC11)'s opposite-Hom sign. The endpoint functors kill the higher graph vertices, so the supplied higher comparison faces project to the prescribed endpoint diagram. Their differential identities are (B.RS8), (B.GC13), and (B.IA12), already checked on homogeneous words. They can consequently be retained as fixed faces in the relative lift (B.ND9). An arbitrary extra face, without those identities, is not covered by this assertion.

**Right kernels and the resolved mate.** Dualize through the canonical evaluation roofs (B.RK2)–(B.RK4), retaining the actual comparison with \(H_f\) from (B.KC12)–(B.KC15). If a family of inverses is needed on a parameter diagram, first resolve the entire diagram over its free index and endpoint product category, as in (B.ND5)–(B.ND8). A quasi-isomorphism between those whole h-projectives has a whole natural inverse and both witnesses. Objectwise inverse choices alone do not justify this step.

On these models, set \(L_0=T_{H_f}\), \(L_1=T_{H_{f'}}\), \(S=T_{P_u}\), \(V=T_{P_g}\). For the resulting resolved left inverse \(\vartheta\), the right mate is obtained from
\[
\begin{aligned}
r_0:P_0&\longrightarrow U_0N,\qquad
e_0=\varepsilon^0_N L_0r_0,\\
\zeta_N&=\operatorname{Adj}_{L_1}(Ve_0\,\vartheta_{P_0}),\\
r_1c_N-\zeta_N&=db_N,\qquad
e_1L_1c_N-Ve_0\,\vartheta_{P_0}
       =d(\varepsilon^1_{VN}L_1b_N).
\end{aligned}
\tag{B.MX13}
\]
The full Hom-complex adjunction carries the retained cube homotopy and its boundary to the mate diagram. For vertical and horizontal pasting use the actual witnesses (B.BM17) and (B.BM18); horizontal pasting retains its intermediate replacements and the coefficient (B.MX12). All arguments of \(\vartheta\) are h-projective. No value at an unresolved \(U_0N\), and no invertibility of the right mate, is asserted.

This supplies the proper–open kernel edge, a common six-vertex model for the actual mixed cube, and its relative resolved-mate boundary. To finish the enhanced operation system one must still assemble the entire changing-compactification and finite composition arrays with their shared unit, counit and triangle faces and prove their common-refinement compatibility in these kernel models. Geometric nearby attaching maps and multiplicative descent, whole coefficient-system completion/rationalization and strict-heart higher effacement are not established by this construction. \(\square\)


### Transport the nested adjunction across refinements

**Proposition B.1ag (both nested replacements must travel).** Consider a strict normalized diagram of the intermediate squares (B.IA1). Its refinement functors on \(\mathcal A,\mathcal B,\mathcal C\) are quasi-equivalences; the horizontal functors \(\beta,F,G\) need not be. There is a transport-labelled nested resolution graph over the entire refinement category. Its projection is surjective on graded Hom groups and a quasi-isomorphism on each Hom complex. Its fold to the common-span right replacement retains the nonzero second coefficient of (B.IA12). The actual sequential right maps and counits have the comparison witnesses below. A unit comparison has a second witness, and that second witness supplies the left-triangle comparison rather than leaving an unexplained closed defect. All constructions use possibly unbounded modules over an arbitrary commutative coefficient ring.

Here is the precise input. For \(g:i\to j\), write \(a_g,b_g,c_g\) for the three refinement functors. The categories \(\mathcal D,\mathcal E\) stay fixed, and
\[
\begin{gathered}
b_g\alpha_i=\alpha_j a_g,\qquad
c_g\beta_i=\beta_j a_g,\qquad p_jc_g=p_i,\\
F_jb_g=F_i,\qquad G_jc_g=G_i,\qquad
T_i=G_i\beta_i=T_j a_g .
\end{gathered}
\tag{B.NR1}
\]
Identity and composite refinement functors agree literally. For the geometric squares, these are the normalized forms of the specified proper-image comparisons in (B.SN1)–(B.SN13); evaluation back to the original squares retains their named isomorphisms. This input is not an assertion that arbitrary independently chosen models already form such a strict diagram.

Use the actual canonical induction isomorphisms
\[
\begin{aligned}
A_g&:\alpha_{j!}a_{g!}\longrightarrow b_{g!}\alpha_{i!},&
B_g&:\beta_{j!}a_{g!}\longrightarrow c_{g!}\beta_{i!},\\
C_g&:T_{j!}a_{g!}\longrightarrow T_{i!},&
P_g&:p_{j!}c_{g!}\longrightarrow p_{i!}.
\end{aligned}
\tag{B.NR2}
\]
They are balanced-tensor maps, not chosen inverses of quasi-isomorphisms. Their associativity is the equality on tensor generators already checked in (B.CR6)–(B.CR9).

**A labelled graph, not conjugation by a homotopy equivalence.** An object over \(i,Y\) is the actual nested pair
\[
r_i:R_i\longrightarrow G_i^*Y,\qquad
t_i:Z_i\longrightarrow\beta_i^*R_i,\qquad
q_i=\beta_i^*r_i\,t_i:Z_i\longrightarrow T_i^*Y,
\tag{B.NR3}
\]
where \(R_i,Z_i\) are h-projective and \(r_i,t_i\) are quasi-isomorphisms. A degree-\(n\) morphism \(U\), labelled by \(g:i\to j\), has vertex maps
\(f:Y\to Y'\), \(\rho:R_i\to c_g^*R_j\), \(z:Z_i\to a_g^*Z_j\), and witnesses
\(k:R_i\to G_i^*Y'\), \(h:Z_i\to\beta_i^*c_g^*R_j\) of degree \(n-1\).
The two edge components of its differential are
\[
\begin{aligned}
(DU)_k&=c_g^*r_j\,\rho-G_i^*f\,r_i-dk,\\
(DU)_h&=a_g^*t_j\,z-\beta_i^*\rho\,t_i-dh .
\end{aligned}
\tag{B.NR4}
\]
The vertex components use the ordinary Hom differential. For \(V\) of degree \(m\), labelled \(u:j\to l\), after \(U\), composition is labelled \(ug\) and is
\[
\begin{aligned}
f_{VU}&=f_Vf_U,\\
\rho_{VU}&=c_g^*\rho_V\,\rho_U,\\
z_{VU}&=a_g^*z_V\,z_U,\\
k_{VU}&=c_g^*k_V\,\rho_U+(-1)^mG_i^*f_V\,k_U,\\
h_{VU}&=a_g^*h_V\,z_U+(-1)^m\beta_i^*c_g^*\rho_V\,h_U .
\end{aligned}
\tag{B.NR5}
\]
Restriction is a strict dg functor and (B.NR1) identifies the middle modules, so these are well typed. Expanding \(D^2\) cancels the two copies of each edge defect. In the Leibniz identity the differential of a witness changes its degree by one, giving precisely the displayed \((-1)^m\). For a triple composite, both expansions have the three terms with coefficients \(1,(-1)^{|W|},(-1)^{|W|+|V|}\). This proves associativity. Identities have identity vertex maps, identity label and zero witnesses. Taking direct sums over labels gives a dg category.

Let \(\mathcal H\) have objects \((i,Y)\) and
\(\mathcal H((i,Y),(j,Y'))=\bigoplus_{g:i\to j}\operatorname{Hom}_{\mathcal E}(Y,Y')\),
with composition using the composite label. Projection sends \(U\) to \((g,f)\).
On one label, forget \(z,h\) first. Its kernel is the shifted cone of the first map below; the remaining projection has kernel the shifted cone of the second:
\[
\begin{aligned}
\operatorname{Hom}_{\mathcal A_i}(Z_i,a_g^*Z_j)
 &\xrightarrow{\ a_g^*t_j\circ-\ }
 \operatorname{Hom}_{\mathcal A_i}(Z_i,\beta_i^*c_g^*R_j),\\
\operatorname{Hom}_{\mathcal C_i}(R_i,c_g^*R_j)
 &\xrightarrow{\ c_g^*r_j\circ-\ }
 \operatorname{Hom}_{\mathcal C_i}(R_i,G_i^*Y').
\end{aligned}
\tag{B.NR6}
\]
Both are quasi-isomorphisms: their sources of Hom are h-projective, and restrictions preserve quasi-isomorphisms. Both projections are surjective as graded maps, by choosing the forgotten components zero; this does not claim that this zero section is a chain map. Thus each kernel, and then the total kernel, is acyclic. Direct sums over labels preserve exactness. Replacements exist over every \((i,Y)\). This proves the asserted Hom property without claiming that \(a_g^*Z_j\) or \(\beta_i^*R_i\) is h-projective.

For a closed degree-zero \(U\) with \(f\) a quasi-isomorphism, (B.NR4) and two-out-of-three show successively that \(\rho\) and \(z\) are quasi-isomorphisms. Their induction adjoints
\(\bar\rho=\varepsilon^{c_g}c_{g!}\rho\) and
\(\bar z=\varepsilon^{a_g}a_{g!}z\)
are homotopy equivalences between h-projectives: apply (B.SM2) to each actual restriction-side quasi-isomorphism. No step assumes that induction preserves an arbitrary quasi-isomorphism. The maps \(\rho,z,\bar\rho,\bar z\) are not treated as invertible chain maps for conjugation.

**The second coefficient survives a change of fibre.** The common graph has objects \(q_i\) and labelled maps \((f,z,H)\), with the analogue of (B.NR4). In the suspended convention of (B.RS7), the fold is
\[
\begin{aligned}
K_1(U)&=(f_U,z_U,H_U),\\
H_U&=\beta_i^*c_g^*r_j\,h_U+\beta_i^*k_U\,t_i,\\
K_2(V,U)&=(0,0,\beta_i^*c_g^*k_V\,h_U),\qquad
K_s=0\quad(s>2).
\end{aligned}
\tag{B.NR7}
\]
Every expression is pulled to the source fibre \(i\). The selected-edge expansion in (B.RS8) applies there verbatim: the two available edges give the two terms of \(K_1\), selecting both gives \(K_2\), and there is no selection of three edges. Restriction preserves products and differentials, so every split/merge cancellation has the same composite label. This proves all arities, including the three-input identity. The ordinary multiplicativity homotopy is \((-1)^{|V|+1}K_2(V,U)\), not an unsigned replacement. Higher coefficients vanish on identity inputs.

The common graph has the same Hom projection property, now using \(a_g^*q_j\) and h-projective \(Z_i\). Hence \(K_1\) is a quasi-isomorphism on each labelled Hom complex. An object of the common graph is isomorphic in \(H^0\), over its identity label, to a folded nested replacement: lift the identity on \(Y\) in both directions and use injectivity on \(H^0\) to verify their composites. Applying (B.SF7) to this entire labelled graph gives a strict roof over \(\mathcal H\). This is one use of \(UQ\) on a specified higher functor; it is not an unsupported assertion that \(Q\) is functorial on arbitrary higher maps.

**The actual sequential right comparison.** Put \(W_i=\alpha_{i!}Z_i\) and \(s_i=d_{i,R_i}\alpha_{i!}t_i\), as in (B.IA3). Let \(U\) be closed of degree zero, with arbitrary closed degree-zero \(f:Y\to Y'\). Define
\[
\begin{aligned}
w_g&=\alpha_{j!}\bar z\,A_g^{-1}:b_{g!}W_i\longrightarrow W_j,\\
v_i&=\varepsilon^{\beta_i}_{R_i}\beta_{i!}t_i,\qquad
R_g=p_{j!}\bar\rho\,P_g^{-1}:p_{i!}R_i\longrightarrow p_{j!}R_j .
\end{aligned}
\tag{B.NR8}
\]
Write \(\kappa_g:b_{g!}F_i^*\to F_j^*\) for the actual mate of \(F_jb_g=F_i\); it need not be invertible. Adjoint the witness \(h_U\) along \(a_g\), writing
\(h_U^\sharp=\varepsilon^{a_g}_{\beta_j^*R_j}a_{g!}h_U\). Then
\[
s_jw_g-F_j^*R_g\,\kappa_g\,b_{g!}s_i
 =d\!\left(d_{j,R_j}\alpha_{j!}h_U^\sharp\,A_g^{-1}\right).
\tag{B.NR9}
\]
Here is a check of the less immediate term. The \(\beta_j\)-adjoint of
\(\operatorname{Adj}_{a_g}(\beta_i^*\rho\,t_i)\) is
\(\bar\rho\,c_{g!}v_i\,B_g\). Apply \(p_{j!}\), then the balanced isomorphism
\(p_{j!}\beta_{j!}\cong F_{j!}\alpha_{j!}\). The result is the \(F_j\)-adjoint of
\(F_j^*R_g\,\kappa_g\,b_{g!}s_i\,A_g\), because the four balanced maps commute on a tensor generator. This is exactly the second identity of (B.SM7) in the two fibres. Adjointing the second line of (B.NR4) and using that equality proves (B.NR9). Thus both actual intermediate maps, and not merely their derived isomorphism classes, are retained.

**Counits with their defect.** Define \(e_i=\varepsilon^{T_i}_Y T_{i!}q_i\), the same sequential/common counit as (B.IA8). Let
\[
\Theta_U=
\varepsilon^{T_j}_{Y'}T_{j!}
  \bigl(\varepsilon^{a_g}_{T_j^*Y'}a_{g!}H_U\bigr).
\quad
e_jT_{j!}\bar z-f e_i C_g=d\Theta_U .
\tag{B.NR10}
\]
Its domain is \(T_{j!}a_{g!}Z_i\), its codomain is \(Y'\), and its degree is \(-1\).
Indeed the folded closed-map equation is
\(a_g^*q_j\,z-T_i^*f\,q_i=dH_U\).
Take its \(a_g\)-adjoint, then its \(T_j\)-adjoint. The composed-counit identity identifies the second term with \(f e_i C_g\). This also proves
\(\Theta_U C_{g,Z_i}^{-1}=\operatorname{Adj}_{T_i}(H_U)\).
No quasi-isomorphism claim about a counit is needed.

**One unit comparison, including its second witness.** Let \(Q_i,Q_j\) be h-projective and let \(A:a_{g!}Q_i\to Q_j\) be a closed homotopy equivalence. Write
\[
A^\flat=a_g^*A\,\eta^{a_g}_{Q_i},\qquad
L_i=T_{i!}Q_i,\quad L_j=T_{j!}Q_j,\quad
f=T_{j!}A\,C_{g,Q_i}^{-1}:L_i\longrightarrow L_j .
\tag{B.NR11}
\]
Choose the nested replacements over \(L_i,L_j\) and the actual unit lifts
\(u_i:Q_i\to Z_i(L_i)\), \(u_j:Q_j\to Z_j(L_j)\), with
\(q_i u_i-\eta^{T_i}_{Q_i}=d\ell_i\) and
\(q_j u_j-\eta^{T_j}_{Q_j}=d\ell_j\), as in (B.IA6)–(B.IA7).
Lift the closed \((g,f)\) through the nested graph, retaining its \(z,H_U\).
The unit defect and its image witness are
\[
\begin{aligned}
D_U&=a_g^*u_j\,A^\flat-z u_i,\\
I_U&=a_g^*\ell_j\,A^\flat-T_i^*f\,\ell_i-H_Uu_i,\\
dD_U&=0,\qquad dI_U=a_g^*q_j\,D_U .
\end{aligned}
\tag{B.NR12}
\]
The last equality follows by expansion. The remaining degree-zero terms cancel by the actual composed-unit identity
\(a_g^*\eta^{T_j}_{Q_j}A^\flat=T_i^*f\,\eta^{T_i}_{Q_i}\).
Thus the pair \((D_U,I_U)\) is a closed element of the shifted cone of
\(\operatorname{Hom}(Q_i,a_g^*q_j)\), not just an unexplained closed map.
That cone is acyclic. It supplies \(J_U\) of degree \(-1\) and \(K_U\) of degree \(-2\) with
\[
dJ_U=D_U,\qquad
a_g^*q_j\,J_U-I_U=dK_U .
\tag{B.NR13}
\]
Both equations matter. Finding only \(J_U\) does not prove the second with \(K_U=0\).
One can see the two-stage correction explicitly: first choose \(J_U\) by injectivity on \(H^0\); the difference \(a_g^*q_jJ_U-I_U\) is closed in degree \(-1\). Surjectivity on \(H^{-1}\) allows subtraction of a closed map from \(J_U\) so that this difference is a boundary, giving \(K_U\).

**The left-triangle comparison now has a boundary.** Use the actual left-triangle witness
\(\lambda_i=\operatorname{Adj}_{T_i}(\ell_i)\), so
\(d\lambda_i=e_iT_{i!}u_i-1_{L_i}\).
This is the witness of (B.IA9): adjointing the two terms of (B.IA7) gives
\(\varepsilon^G G_!(r\,\varepsilon^\beta\beta_!h+k)\) there.
Put \(\bar J_U=\operatorname{Adj}_{a_g}(J_U)\). The comparison built from the unit and counit homotopies, and its second filler, are
\[
\begin{aligned}
\Xi_U&=e_jT_{j!}\bar J_U\,C_{g,Q_i}^{-1}
       +\Theta_U T_{j!}a_{g!}u_i\,C_{g,Q_i}^{-1},\\
\Gamma_U&=\operatorname{Adj}_{T_i}(K_U),\\
\Xi_U-\lambda_j f+f\lambda_i&=d\Gamma_U .
\end{aligned}
\tag{B.NR14}
\]
For a direct verification, adjunction identifies the first line with
\(\operatorname{Adj}_{T_i}(a_g^*q_jJ_U+H_Uu_i)\).
Naturality and (B.NR11) identify
\(\lambda_j f-f\lambda_i\) with
\(\operatorname{Adj}_{T_i}(a_g^*\ell_j A^\flat-T_i^*f\ell_i)\).
Subtract and apply (B.NR13). Adjunction is an isomorphism of complexes, so its differential introduces no additional sign. The diagram below shows the two unit routes whose defect is \(d\bar J_U\):
\[
\begin{array}{ccc}
a_{g!}Q_i&\xrightarrow{\ a_{g!}u_i\ }&a_{g!}Z_i(L_i)\\
{\scriptstyle A}\downarrow&&\downarrow{\scriptstyle\bar z}\\
Q_j&\xrightarrow{\ u_j\ }&Z_j(L_j).
\end{array}
\qquad
u_jA-\bar z\,a_{g!}u_i=d\bar J_U .
\tag{B.NR15}
\]
The arrows \(u_i,u_j\) are units, not asserted equivalences. The degree-minus-two filler in (B.NR14) is what makes the displayed triangle witnesses compatible; the fact that their difference is closed alone would not suffice.

**What is joined, and what still has to be joined.** The labelled graph and fold are defined over the whole specified refinement category, not separately on each edge. A supplied parameter diagram is first resolved over its whole product/transport category as in (B.TD4) and (B.ND6); this supplies the h-projective Hom sources used above without claiming arbitrary restriction preserves them. A free dg presentation of that supplied diagram can then be lifted through the Hom-surjective acyclic-kernel projection, relative to already checked free faces, using (B.ND9). The finite equations above give the actual targets and boundaries of the unit, counit and left-triangle comparisons. That lifting statement does not supply an absent target presentation or authorize prescribing arbitrary old homotopies with incompatible boundaries.

The original bar comparisons, the nonzero nested \(K_2\), and the mixed-cube pair \((H,K)\) from (B.MX8) are part of the joint presentation. The shared right-triangle and geometric composition, refinement and mixed-cube faces require compatible maps in the complete graph-bar arrays. The fixed-model construction here does not establish that general assembly, geometric nearby-cycle multiplicative descent, whole coefficient-system transport or strict-heart effacement. \(\square\)



### Join the two triangles over the whole refinement family

**Proposition B.1ah (choose the two stages together).** In the strict normalized refinement system (B.NR1), the nested replacements, their actual units and counits, and both triangle witnesses can be chosen as maps of the **whole refinement/input diagram**. The right triangle has a second witness, and that witness compares the two triangle homotopies after the actual counit. The paired target (B.JT5) then varies by genuine target-diagram maps, including when the input module varies. The comparison uses (B.TD4), (B.IA6)–(B.IA13) and (B.NR13). Gluing of the entire geometric mixed-cube/master-bar presentation is an additional assertion. All modules may be unbounded, over an arbitrary commutative coefficient ring.

**Which category contains a natural homotopy?** Let \(I\) be the ordinary refinement category, let \(\mathcal T_A,\mathcal T_C\) be its transport categories for \(a_g,c_g\), and let \(\mathcal T_E\) be the constant-\(\mathcal E\) transport category. The equalities in (B.NR1) give strict dg functors
\[
\widehat\beta:\mathcal T_A\longrightarrow\mathcal T_C,\qquad
\widehat G:\mathcal T_C\longrightarrow\mathcal T_E,\qquad
\widehat T=\widehat G\widehat\beta .
\tag{B.JF1}
\]
For example \(\widehat\beta(i,A)=(i,\beta_iA)\) and
\(\widehat\beta(g,v)=(g,\beta_jv)\); its target is correct because
\(c_g\beta_i=\beta_j a_g\). The other formulas are the same, using \(G_jc_g=G_i\).
Here \(T_i=G_i\beta_i\). A module \(Y\) over \(\mathcal T_E\) is precisely a strict input family \(Y_i\), with closed maps \(n_g:Y_i\to Y_j\).
These input maps need not be quasi-isomorphisms.

Restriction along each functor in (B.JF1) is fibrewise restriction. Its left adjoint is canonically fibrewise induction with the actual balanced-tensor comparison on each structure map. This last assertion needs a check when the fibre category varies. For any one of these functors \(\widehat F\), induction of a transport representable at \((i,X)\), evaluated at \(j\), is
\[
\begin{aligned}
\bigl(\widehat F_!\mathcal T_A(-,(i,X))\bigr)_j
 &=\bigoplus_{g:i\to j}\mathcal C_j(-,c_gF_iX),\\
F_{j!}\bigl(\mathcal T_A(-,(i,X))_j\bigr)
 &=\bigoplus_{g:i\to j}\mathcal C_j(-,F_j a_gX).
\end{aligned}
\tag{B.JF2}
\]
The displayed instance has \(F_i:\mathcal A_i\to\mathcal C_i\) with \(F_ja_g=c_gF_i\); for the other functors replace the letters accordingly. The two sums are identified term by term by that equality. The identification is natural in every homogeneous transport morphism, since both composites act by the same \(F_j(v)\) and labelled transport composition. An arbitrary module is the coequalizer of sums of shifts of representables tensored with its value complexes, using the module action and composition as the two maps. Both induction constructions preserve those sums, tensors and coequalizers. The displayed identification therefore descends to every module. Equivalently, on balanced tensors it moves the index arrow onto the source module, as in (B.ND8). In particular it identifies the units, counits and Hom-complex adjunctions, not just the isomorphism classes of the values.

Induction preserves whole-diagram h-projectivity: its Hom into an acyclic module is the Hom of the h-projective source into its restriction, which is still objectwise acyclic. Evaluation preserves h-projectivity here by (B.TD4). No converse from pointwise h-projectivity is used.

**First build the right-input family, then its left image.** Choose whole semifree replacements
\[
R\xrightarrow{r}\widehat G^*Y,\qquad
Z\xrightarrow{t}\widehat\beta^*R,\qquad
q=\widehat\beta^*r\,t:Z\longrightarrow\widehat T^*Y .
\tag{B.JF3}
\]
The first replacement is over \(\mathcal T_C\), the second over \(\mathcal T_A\).
Both are quasi-isomorphisms, and \(q\) is one as well. Their structure maps give the nested refinement maps of (B.NR3) with zero edge defects along this specified strict diagram. This choice does not set the nonzero \(K_2\) of the full nested resolution graph to zero.

Put \(L=\widehat T_!Z\), and use (B.JF2) to write its components as \(L_i=T_{i!}Z_i\).
If \(z_g:Z_i\to a_g^*Z_j\) is the structure map and \(\bar z_g\) its induction adjoint, then its structure maps and the actual counit are
\[
\begin{aligned}
\tau_g&=T_{j!}\bar z_g\,C_{g,Z_i}^{-1}:L_i\longrightarrow L_j,\\
e_i&=\epsilon^{T_i}_{Y_i}\,T_{i!}q_i:L_i\longrightarrow Y_i,\\
\tau_{hg}&=\tau_h\tau_g,\qquad e_j\tau_g=n_ge_i .
\end{aligned}
\tag{B.JF4}
\]
Here \(C_g:T_{j!}a_{g!}\to T_{i!}\) is exactly (B.NR2)'s tensor isomorphism.
The composition equality follows by the structure-map law of \(Z\) and associativity on balanced tensors. The counit equality is the adjoint of
\(a_g^*q_j\,z_g=T_i^*n_g\,q_i\), using the composed ordinary unit. Thus \(e:L\to Y\) is already a map of entire diagrams before the second resolution is chosen.

Now resolve \(\widehat G^*L\), and then its restriction:
\[
R^L\xrightarrow{r^L}\widehat G^*L,\qquad
Z^L\xrightarrow{t^L}\widehat\beta^*R^L,\qquad
q^L=\widehat\beta^*r^L\,t^L:Z^L\longrightarrow\widehat T^*L .
\tag{B.JF5}
\]
There is no circular choice: \(L\) and \(\tau\) were constructed from the first stage, and (B.JF5) resolves that already specified diagram.
All four replacements in (B.JF3) and (B.JF5) are h-projective in their whole transport categories; their restricted targets need not be h-projective.

**Use the same nested unit in both triangles.** Set \(P=\widehat\beta_!Z\); then \(L=\widehat G_!P\) through the canonical composition isomorphism.
Whole-diagram Hom lifting first gives closed \(v:P\to R^L\), and then closed \(u:Z\to Z^L\), with degree-minus-one witnesses \(k,h\):
\[
\begin{aligned}
r^Lv-\eta^{\widehat G}_P&=dk,\\
t^Lu-\widehat\beta^*v\,\eta^{\widehat\beta}_Z&=dh,\\
\ell&=\widehat\beta^*r^L\,h+
        \widehat\beta^*k\,\eta^{\widehat\beta}_Z,\\
q^Lu-\eta^{\widehat T}_Z&=d\ell .
\end{aligned}
\tag{B.JF6}
\]
The first lift uses h-projectivity of \(P\), proved by induction, and the second uses h-projectivity of \(Z\). Expanding the differential of the third line and substituting the first two lines gives the fourth, by the composed-unit identity. These are the actual nested unit formulas of (B.IA6)–(B.IA7), now in the natural Hom complexes.

The counit at the second stage and its left-triangle witness are
\[
e^L=\epsilon^{\widehat T}_L\,\widehat T_!q^L,\qquad
\lambda=\operatorname{Adj}_{\widehat T}(\ell),\qquad
d\lambda=e^L\widehat T_!u-1_L .
\tag{B.JF7}
\]
The last equality uses the ordinary left triangle before passing to replacements.
For an arbitrary whole h-projective left-input family \(Q\), the same construction with \(Q\) in place of \(Z\) and \(L_Q=\widehat T_!Q\) supplies its left unit and triangle. When \(Q=Z\), reuse exactly (B.JF5)–(B.JF7), not a separately chosen second copy. If a supplied \(Q\) is only pointwise h-projective, first replace the whole diagram and retain the resulting comparison; pointwise h-projectivity alone does not justify this lift.

**Lift the counit through both nested replacements.** Apply the same whole-diagram Hom argument to \(e:L\to Y\). It gives closed \(\rho:R^L\to R\), \(z:Z^L\to Z\), and witnesses \(k_e,h_e\), all natural, satisfying
\[
\begin{aligned}
r\rho-\widehat G^*e\,r^L&=dk_e,\\
tz-\widehat\beta^*\rho\,t^L&=dh_e,\\
H&=\widehat\beta^*r\,h_e+\widehat\beta^*k_e\,t^L,\\
qz-\widehat T^*e\,q^L&=dH .
\end{aligned}
\tag{B.JF8}
\]
The sources for these two lifts are respectively \(R^L\) and \(Z^L\); neither proof assumes that restriction preserves h-projectivity. The third line is precisely the first folding coefficient of (B.IA12), including both terms.

**The full right-triangle boundary.** In the natural Hom complexes put
\[
D=zu-1_Z,\qquad
I=Hu+\widehat T^*e\,\ell,\qquad
dD=0,\qquad qD=dI .
\tag{B.JF9}
\]
Indeed, insert (B.JF6) and (B.JF8) in \(qzu-q\); the remaining term is
\(\widehat T^*e\,\eta^{\widehat T}_Z-q=0\), the ordinary adjunction identity for the actual adjoint \(e=\operatorname{Adj}_{\widehat T}(q)\).
Postcomposition by \(q\) induces a quasi-isomorphism
\(\operatorname{Hom}_{\mathcal T_A}(Z,Z)\to
\operatorname{Hom}_{\mathcal T_A}(Z,\widehat T^*Y)\).
Its shifted cone has differential \((x,y)\mapsto(dx,qx-dy)\).
It is acyclic because \(Z\) is h-projective over \(\mathcal T_A\), not merely at each fibre. A primitive of its closed element \((D,I)\) gives **both** witnesses
\[
dJ=D,\qquad qJ-I=dK,\qquad |J|=-1,\quad |K|=-2 .
\tag{B.JF10}
\]
One can see the second step directly. First choose \(J_0\) with \(dJ_0=D\), using injectivity on \(H^0\). The difference \(qJ_0-I\) is closed of degree minus one. Surjectivity on \(H^{-1}\) allows a closed correction to \(J_0\) whose image removes that cohomology class. The remaining difference is \(dK\). A choice of \(J_0\) alone would not justify setting \(K=0\).

This second witness joins the two triangle homotopies along their common counit. Set \(\theta=\operatorname{Adj}_{\widehat T}(H)\) and
\(\Gamma=\operatorname{Adj}_{\widehat T}(K)\). Applying the Hom-complex adjunction gives
\[
\begin{aligned}
d\theta&=e\,\widehat T_!z-e\,e^L,\\
e\,\widehat T_!J-\theta\,\widehat T_!u-e\lambda&=d\Gamma .
\end{aligned}
\tag{B.JF11}
\]
For the second line, the adjoints of \(qJ,Hu,\widehat T^*e\,\ell\) are respectively \(e\widehat T_!J,\theta\widehat T_!u,e\lambda\); the adjunction is a chain isomorphism, so no extra differential sign is introduced. Differentiating the left side cancels its two copies of \(e\widehat T_!(zu)\), of \(e e^L\widehat T_!u\), and of \(e\). This checks its boundary, while (B.JF10) supplies the actual primitive. The two triangle routes, rather than just their equal homotopy classes, are thus compared.

**The actual varying paired target.** At \(i\) use the five vertices
\(Z_i,T_i^*L_i,T_i^*Y_i,L_i,Y_i\), and the seven arrows of (B.JT5), with \(q_i,e_i\).
Let \(\kappa_g:a_{g!}T_i^*\to T_j^*\) be the actual mate for \(T_ja_g=T_i\).
Write \(A_g=\bar z_g\),
\(B_g=T_j^*\tau_g\,\kappa_{g,L_i}\), and
\(C'_g=T_j^*n_g\,\kappa_{g,Y_i}\).
The five vertex comparisons are \(A_g,B_g,C'_g,\tau_g,n_g\).
They respect all seven edges as follows:
\[
\begin{aligned}
B_g\,a_{g!}\eta^{T_i}_{Z_i}&=\eta^{T_j}_{Z_j}A_g,\\
C'_g\,a_{g!}(T_i^*e_i)&=T_j^*e_j\,B_g,\\
C'_g\,a_{g!}q_i&=q_jA_g,\\
\tau_g C_{g,Z_i}&=T_{j!}A_g,\\
\tau_g\epsilon^{T_i}_{L_i}C_{g,T_i^*L_i}
 &=\epsilon^{T_j}_{L_j}T_{j!}B_g,\\
n_g\epsilon^{T_i}_{Y_i}C_{g,T_i^*Y_i}
 &=\epsilon^{T_j}_{Y_j}T_{j!}C'_g,\\
n_ge_i&=e_j\tau_g .
\end{aligned}
\tag{B.JF12}
\]
The first line is naturality of the unit and its composition identity; the second uses naturality of \(\kappa_g\) and (B.JF4); the third is the adjoint of the structure equality for \(q\). The fourth is the definition of \(\tau_g\). In the fifth and sixth lines, the counit-composition identity reduces the left side to the receiving counit followed by \(T_{j!}(T_j^*\tau_g\,\kappa_g)\) or \(T_{j!}(T_j^*n_g\,\kappa_g)\), exactly the displayed right side. The final line was proved in (B.JF4). The four path relations of (B.JT6) hold in every fibre by the ordinary adjunction identities, and these edge equalities preserve them. Composition of the five comparisons follows from the structure laws for \(Z,Y,L\) and associativity of the actual mates. Thus this is a map of the whole target presentation, not an inference from a square that commutes only up to homotopy. When \(n_g\) is a quasi-isomorphism, the equivalence conclusions of (B.RT3) follow by restriction and the quasi-equivalence unit. No equivalence is claimed for a general \(n_g\), for the unit, or for a noninvertible right mate.

The two routes in (B.JF11) are displayed here:
\[
\begin{array}{ccccccc}
L&\xrightarrow{\widehat T_!u}&\widehat T_!Z^L&
\xrightarrow{\widehat T_!z}&L&\xrightarrow{e}&Y\\
L&\xrightarrow{\widehat T_!u}&\widehat T_!Z^L&
\xrightarrow{e^L}&L&\xrightarrow{e}&Y .
\end{array}
\tag{B.JF13}
\]
The upper composite is shortened to \(e\) by \(e\widehat T_!J\). The witness
\(\theta\widehat T_!u\) compares the upper composite with the lower one, and
\(e\lambda\) shortens the lower composite to \(e\). The difference between these two homotopy routes is \(d\Gamma\), exactly (B.JF11). The rows are not asserted to be literally equal chain maps. Every object and arrow belongs to the same resolved family.

For an additional dg parameter category, pull back to its free index \(Q\mathcal J\) and perform this entire two-stage construction over \((Q\mathcal J)^{\mathrm{op}}\otimes\mathcal T_A\), and similarly for the other two transport categories. The path-cell filtration of (B.ND6), followed by (B.TD4), proves h-projectivity after evaluation; (B.ND4) gives the graded naturality signs. The induction identification (B.JF2) remains valid with those tensor signs, so every displayed Hom lift takes place in the whole parameter-and-refinement category. An arbitrary nonflat index is not silently substituted for the free one.

**Remaining geometric join.** The construction retains the original strict folding roofs, the nonzero nested second coefficient, and the mixed-cube pair \((H,K)\) in (B.MX8). It does not identify independently chosen old pointwise replacements or homotopies with the new natural choices. Compatible old whole-diagram faces can be compared and retained through the resolution graphs and the relative free lifting theorem (B.ND9), after their actual target maps and boundaries are supplied. The horizontal geometric base-change functors need not be quasi-equivalences; their joins still require the resolved mates of (B.MX13) and the original common mapping target. The full mixed-cube/composition array, geometric multiplicative descent, coefficient-system transport and strict-heart effacement are not established by this construction. \(\square\)



### Join the unit comparison to the resolved cube

**Proposition B.1ai (the unit interface, with its higher witness).** In the common resolved model of (B.MX13), the unit comparison of (B.BM16) extends over a specified whole mixed-cube cell, retaining the already chosen mate and unit lifts. Its extension includes a degree-minus-three witness comparing the second unit witnesses. This supplies the unit interface of that cube, not the entire changing-geometric-model presentation.

Work over an arbitrary commutative coefficient ring, with possibly unbounded modules. Use the whole parameter/refinement categories of (B.JF1)–(B.JF3), and the free dg parameter extension after (B.JF13) when needed. In particular, h-projectivity below is **whole** h-projectivity. Let \(L_i\dashv U_i\), \(S,V\), and the resolved left comparison have the meanings of (B.BM1), (B.BM16), and (B.MX13). The induction functors preserve h-projectives. They need not be equivalences.

**One set of actual unit targets.** Fix a whole h-projective \(Q\), and put \(N=L_0Q\), \(X=L_1SQ\), and \(Y=VN\). From the existing whole-family construction choose
\[
\begin{aligned}
r_0:P_0&\longrightarrow U_0N,&
r_X:A&\longrightarrow U_1X,\\
r_Y:B&\longrightarrow U_1Y,\\
r_0u_0-\eta^0_Q&=d\ell_0,&
r_Xu_1-\eta^1_{SQ}&=d\ell_1,\\
e_0&=\varepsilon^0_NL_0r_0,&
\lambda_0&=\operatorname{Adj}_{L_0}^{-1}(\ell_0),\\
\lambda_1&=\operatorname{Adj}_{L_1}^{-1}(\ell_1).
\end{aligned}
\tag{B.UC1}
\]
The three \(r\)'s are quasi-isomorphisms with whole h-projective sources. The unit maps \(u_0,u_1\) are closed; the two \(\ell\)'s have degree \(-1\). Hence
\(d\lambda_0=e_0L_0u_0-1_N\) and
\(d\lambda_1=e_XL_1u_1-1_X\), where \(e_X=\varepsilon^1_XL_1r_X\).
Use the very same nested stages and witnesses as (B.JF6)–(B.JF7) on an overlap. No unresolved restriction module is declared h-projective.

**Transpose every degree, not just a closed edge.** Let \(\Theta\) be the complex of whole dg-natural transformations from \(L_1S\) to \(VL_0\) on the specified resolved inputs. For homogeneous \(\vartheta\in\Theta^n\) define
\[
\begin{aligned}
\Psi(\vartheta)&=\operatorname{Adj}_{L_1}(Ve_0\,\vartheta_{P_0}),\\
F(\vartheta)&=\Psi(\vartheta)Su_0,&
G(\vartheta)&=U_1(\vartheta_Q)\eta^1_{SQ},\\
\mathcal A(\vartheta)&=\operatorname{Adj}_{L_1}(V\lambda_0\,\vartheta_Q),\\
d\mathcal A(\vartheta)+\mathcal A(d\vartheta)
 &=F(\vartheta)-G(\vartheta).
\end{aligned}
\tag{B.UC2}
\]
Here \(\operatorname{Adj}\) is the actual Hom-complex isomorphism in all degrees. The map \(\Psi\) is a chain map. For the last line, the signed Leibniz rule gives
\(d(V\lambda_0\,\vartheta_Q)=V(d\lambda_0)\vartheta_Q-
 V\lambda_0(d\vartheta)_Q\).
Naturality on the closed map \(u_0\) identifies
\(Ve_0\,\vartheta_{P_0}L_1Su_0\) with
\(Ve_0\,VL_0u_0\,\vartheta_Q\).
The remaining term transposes to \(G(\vartheta)\). Only the h-projective inputs \(Q,P_0\) are used; \(\vartheta_{U_0N}\) is not.

**Keep both lifts in one graded complex.** A degree-\(n\) element \(e\) of a complex \(\mathcal E\) is a tuple
\[
\begin{aligned}
e&=(\vartheta,c,b,z,h),\\
c &:SP_0\longrightarrow B,&z &:A\longrightarrow B,\\
b &:SP_0\longrightarrow U_1Y,&h &:A\longrightarrow U_1Y,\\
|c|=|z|&=n,&|b|=|h|&=n-1,\\
\partial e&=\bigl(d\vartheta,dc,\,
 r_Yc-\Psi(\vartheta)-db,\,
 dz,\,r_Yz-U_1(\vartheta_Q)r_X-dh\bigr).
\end{aligned}
\tag{B.UC3}
\]
The two graph maps are chain maps, so \(\partial^2=0\).
For a closed degree-zero element, \((c,b)\) is exactly the resolved mate lift in (B.BM16), and \((z,h)\) lifts the actual map \(\vartheta_Q:X\to Y\). They are not new unit targets.

The projection \(\mathcal E\to\Theta\) is surjective in each graded degree. Its kernel is the direct sum of the shifted cones of
\(\operatorname{Hom}(SP_0,r_Y)\) and \(\operatorname{Hom}(A,r_Y)\).
Both are acyclic by whole h-projectivity. Compatible existing lifts can therefore be retained while a specified free **linear** cell diagram in \(\Theta\) is lifted. At a new generator, choose any graded lift of its target value. Its differential error is a cycle in the kernel; subtract a primitive. This is the relative obstruction calculation of (B.ND9). It does not assign a composition law to \(\mathcal E\), or claim that \(\Psi\) alone preserves multiplication. Products are first formed using the actual pasting formulas (B.BM17)–(B.BM18).

**A chain map to the full unit-defect cone.** Let
\[
\begin{aligned}
\mathcal C^n&=\operatorname{Hom}^n(SQ,B)
       \oplus\operatorname{Hom}^{n-1}(SQ,U_1Y),\\
\delta(D,I)&=(dD,r_YD-dI),\\
D_e&=cSu_0-zu_1,\\
I_e&=bSu_0-hu_1-(-1)^nU_1(\vartheta_Q)\ell_1
                       +\mathcal A(\vartheta),\\
\Phi(e)&=(D_e,I_e),&\delta\Phi(e)&=\Phi(\partial e).
\end{aligned}
\tag{B.UC4}
\]
The complex \(\mathcal C\) is acyclic: it is a shifted cone of the quasi-isomorphism
\(\operatorname{Hom}(SQ,r_Y)\), with the displayed sign convention.
Explicitly, the second component of \(\Phi(\partial e)\) is
\[
\begin{aligned}
&r_YD_e-F(\vartheta)+G(\vartheta)+U_1(\vartheta_Q)d\ell_1\\
&\quad{}-db\,Su_0+dh\,u_1
 +(-1)^nU_1((d\vartheta)_Q)\ell_1+\mathcal A(d\vartheta)
 =r_YD_e-dI_e .
\end{aligned}
\tag{B.UC5}
\]
The expression follows from (B.UC1) and (B.UC3); the equality uses (B.UC2).
The first component is \(dD_e=D_{\partial e}\), since the unit lifts are closed.
The sign on the \(\ell_1\) term changes for a degree-minus-one cube cell. Keeping the degree-zero sign there would break the chain-map identity.

**Resolve the unit comparison together with the cube.** Form
\[
\begin{aligned}
\widetilde{\mathcal E}^{\,n}&=\mathcal E^n\oplus\mathcal C^{n-1},\\
\widetilde\partial(e,j)&=(\partial e,\Phi(e)-\delta j),\\
j&=(J,K),&|J|&=n-1,\quad |K|=n-2 .
\end{aligned}
\tag{B.UC6}
\]
Equation (B.UC4) proves \(\widetilde\partial^{\,2}=0\).
Projection to \(\mathcal E\) is a degreewise surjection with acyclic kernel
\(\mathcal C[-1]\), whose differential is \(-\delta\).
The same relative generator argument retains any previously fixed compatible unit faces. For closed degree-zero \(e\), a closed lift gives
\[
dJ=cSu_0-zu_1,\qquad r_YJ-I_e=dK.
\tag{B.UC7}
\]
The second equation is necessary. A primitive of the first difference alone does not prescribe its image under \(r_Y\).

This also joins the actual counit and the two left-triangle witnesses. Put
\(\beta=\operatorname{Adj}_{L_1}^{-1}b\),
\(\gamma=\operatorname{Adj}_{L_1}^{-1}h\),
\(e_Y=\varepsilon^1_YL_1r_Y\), and
\(\Gamma=\operatorname{Adj}_{L_1}^{-1}K\).
Transposing the second equation of (B.UC7) gives
\[
\begin{aligned}
&e_YL_1J-\beta L_1Su_0+\gamma L_1u_1\\
&\qquad{}+\vartheta_Q\lambda_1-V\lambda_0\vartheta_Q=d\Gamma .
\end{aligned}
\tag{B.UC8}
\]
Every summand has source \(X=L_1SQ\) and target \(Y\). This uses the actual
\(\lambda_0,\lambda_1\) shared with the whole-family triangle construction, not unrelated primitives.

**The two routes of the original mixed cube.** Apply this construction to the two pasted comparisons in the common model of (B.MX13). Their left cells come from the six labelled words and augmentations of (B.MX3)–(B.MX8), the original graph/bar comparison, and its strict roof. Take their right lifts using (B.BM17)–(B.BM18), and call the resulting closed elements of \(\mathcal E\) \(e_T,e_B\).
The full retained left cube cell gives a degree-minus-one element
\(\vartheta_H\) with \(d\vartheta_H=\vartheta_T-\vartheta_B\).
Lift it relatively to \(e_H\in\mathcal E^{-1}\) with
\(\partial e_H=e_T-e_B\), using the acyclic kernel of (B.UC3).
Here \(\vartheta_H\) means the image of the **full** cell \((0,H,K)\) of (B.MX8) through the specified strict common roof. It does not authorize dropping \(K\), the nested \(K_2\) of (B.MX12), or the signed graph-to-bar transfer. If only objectwise inverse maps rather than that whole common roof are supplied, this application is not yet available.

Let \(j_T=(J_T,K_T)\), \(j_B=(J_B,K_B)\) be the retained unit comparisons from (B.UC7). Then
\(\delta(j_T-j_B-\Phi(e_H))=0\).
Acyclicity gives \(w_H=(J_H,K_H)\in\mathcal C^{-2}\) with
\[
\begin{aligned}
\delta w_H&=j_T-j_B-\Phi(e_H),\\
dJ_H&=J_T-J_B-D_{e_H},\\
r_YJ_H-dK_H&=K_T-K_B-I_{e_H},\\
|J_H|&=-2,& |K_H|&=-3 .
\end{aligned}
\tag{B.UC9}
\]
Thus the two unit-homotopy routes are compared as full cone elements, not just as cohomology classes of degree-zero endpoints. At any further specified free linear cell, the same calculation yields a cycle in the same acyclic kernel and supplies the next witness with its fixed boundary retained. It does not manufacture an unspecified geometric boundary.

The first layer has these actual endpoints:
\[
\begin{gathered}
\begin{array}{ccccc}
SQ&\xrightarrow{Su_0}&SP_0&\xrightarrow{c}&B\\
SQ&\xrightarrow{u_1}&A&\xrightarrow{z}&B .
\end{array}\\
dJ=\text{upper composite}-\text{lower composite},\\
r_YJ-I_e=dK .
\end{gathered}
\tag{B.UC10}
\]
Equation (B.UC9) compares this entire two-level diagram for the top and bottom cube routes. Under the actual Hom-complex adjunction it also compares their counit/left-triangle diagrams (B.UC8), since that adjunction commutes with differential in every degree.

**Scope.** These are whole Hom complexes; evaluation uses (B.ND6) and (B.TD4), not a converse from pointwise projectivity. Horizontal functors can be non-equivalences, and no invertibility of a right mate is inferred. The fixed common-model cube has this higher unit interface. The full changing-compactification and finite composition presentation still needs its shared right-triangle and nested horizontal faces joined on actual overlaps; (B.JF8)–(B.JF11) and (B.BM18) are their existing providers. Geometric multiplicative descent, coefficient transport and strict-heart effacement are not established by this construction. \(\square\)



### Join the right triangle to resolved base change

**Proposition B.1aj (the right triangle across an actual mate).** The resolved mate of (B.BM16) admits a comparison between the two retained right-triangle homotopies of (B.JF10). The comparison uses the actual unit interface, counit naturality, and the homotopy obtained by transposing the mate lift. It retains a second, degree-minus-three witness. All choices and equalities below take place in the whole parameter/refinement Hom complexes; no assertion of invertibility of a right mate is needed.

**Retain the original two stages.** Use the whole categories of (B.JF1)–(B.JF3), with the free dg parameter extension following (B.JF13) when required. Let \(L_i\dashv U_i\), \(S,V\), and the closed natural comparison \(\vartheta:L_1S\to VL_0\) be the actual common-model data of (B.MX13). The induction functors preserve whole h-projectives. Fix a whole h-projective right input \(N\), and write
\[
\begin{aligned}
q_0:Q_0&\longrightarrow U_0N,&
q_1:Q_1&\longrightarrow U_1VN,\\
M_i&=L_iQ_i,&
e_0&=\varepsilon^0_N L_0q_0,\\
e_1&=\varepsilon^1_{VN} L_1q_1 .
\end{aligned}
\tag{B.RJ1}
\]
The \(q_i\) are quasi-isomorphisms with whole h-projective sources. For each \(i\), reuse the second replacement \(\rho_i:R_i\to U_iM_i\), the unit \(u_i:Q_i\to R_i\), and the counit lift \(z_i:R_i\to Q_i\) from (B.JF6)–(B.JF10):
\[
\begin{aligned}
\rho_i u_i-\eta^i_{Q_i}&=d\ell_i,&
q_i z_i-U_i e_i\,\rho_i&=dH_i,\\
dJ_i&=z_i u_i-1_{Q_i},\\
q_iJ_i-H_i u_i-U_i e_i\,\ell_i&=dK_i .
\end{aligned}
\tag{B.RJ2}
\]
Here \(u_i,z_i\) are closed; \(\ell_i,H_i,J_i\) have degree \(-1\), and \(K_i\) has degree \(-2\). In particular \(H_i\) is the full two-term nested coefficient in (B.JF8), not its first summand. Put \(e_0^M=\varepsilon^0_{M_0}L_0\rho_0\). The Hom-complex adjunction, with \(\operatorname{Adj}_i\) mapping a left-side Hom to its right-side Hom, gives
\[
\begin{aligned}
\lambda_0&=\operatorname{Adj}_0^{-1}\ell_0,&
\alpha_0&=\operatorname{Adj}_0^{-1}H_0,&
\Gamma_0&=\operatorname{Adj}_0^{-1}K_0,\\
d\lambda_0&=e_0^M L_0u_0-1_{M_0},\\
d\alpha_0&=e_0L_0z_0-e_0e_0^M,\\
e_0L_0J_0&=\alpha_0L_0u_0+e_0\lambda_0+d\Gamma_0 .
\end{aligned}
\tag{B.RJ3}
\]
These are the already shared left/right triangle formulas (B.JF7), (B.JF11), not newly chosen homotopies.

**The actual mate and its three comparison maps.** Write \(X=L_1SQ_0\). Take whole h-projective replacements \(r_A:A\to U_1X\), \(r_C:C\to U_1VM_0\). Choose the left unit \(u_X:SQ_0\to A\) with \(r_Au_X-\eta^1_{SQ_0}=d\ell_X\). Reuse the mate lifts at \(N\) and \(M_0\):
\[
\begin{aligned}
c:SQ_0&\longrightarrow Q_1,&
c_M:SR_0&\longrightarrow C,\\
q_1c-\operatorname{Adj}_1(Ve_0\,\vartheta_{Q_0})&=db,\\
r_Cc_M-\operatorname{Adj}_1(Ve_0^M\,\vartheta_{R_0})&=db_M .
\end{aligned}
\tag{B.RJ4}
\]
All occurrences of \(\vartheta\) are evaluated on whole h-projectives. The sources of \(b,b_M\) are respectively \(SQ_0,SR_0\), their targets are \(U_1VN,U_1VM_0\), and both have degree \(-1\). The closed lifts \(w,v,a\), with degree-minus-one witnesses, satisfy
\[
\begin{aligned}
w:C&\longrightarrow Q_1,&
q_1w-U_1(Ve_0)r_C&=dh_w,\\
v:A&\longrightarrow C,&
r_Cv-U_1(\vartheta_{Q_0})r_A&=dh_v,\\
a:A&\longrightarrow R_1,&
\rho_1a-U_1(L_1c)r_A&=dh_a,\\
\beta&=\operatorname{Adj}_1^{-1}b,&
d\beta&=e_1L_1c-Ve_0\vartheta_{Q_0}.
\end{aligned}
\tag{B.RJ5}
\]
They exist by the whole Hom lifting theorem applied to \(C\) or \(A\). The final identity is the transpose of (B.RJ4); \(\beta:X\to VN\) is the prescribed homotopy, not an arbitrary witness with the same endpoints. For later use define
\[
\begin{aligned}
\upsilon&=\operatorname{Adj}_1(V\lambda_0\,\vartheta_{Q_0}),\\
\chi&=\operatorname{Adj}_1(V\alpha_0\,\vartheta_{R_0}),\\
\xi&=\operatorname{Adj}_1(V\Gamma_0\,\vartheta_{Q_0}).
\end{aligned}
\tag{B.RJ6}
\]
Their degrees are \(-1,-1,-2\), and their sources are \(SQ_0,SR_0,SQ_0\); their targets are \(U_1VM_0,U_1VN,U_1VN\).

**Four full cone comparisons.** First retain the unit comparison \((J_U,K_U)\) of (B.UC7), applied to \(Q_0\), and choose the unit-naturality comparison \((J_F,K_F)\) for the actual \(c\):
\[
\begin{aligned}
dJ_U&=c_MSu_0-vu_X,&r_CJ_U-I_U&=dK_U,\\
I_U&=b_MSu_0-h_vu_X
       -U_1(\vartheta_{Q_0})\ell_X+\upsilon,\\
dJ_F&=u_1c-au_X,&\rho_1J_F-I_F&=dK_F,\\
I_F&=\ell_1c-U_1(L_1c)\ell_X-h_au_X .
\end{aligned}
\tag{B.RJ7}
\]
Both \(J\)'s have degree \(-1\) and both \(K\)'s degree \(-2\). The second pair exists because
\(\rho_1(u_1c-au_X)=dI_F\): substitute (B.RJ2), (B.RJ5), and the ordinary unit naturality
\(\eta^1_{Q_1}c=U_1(L_1c)\eta^1_{SQ_0}\).
The whole h-projective source is \(SQ_0\); \(c\) need not be a quasi-isomorphism.

Next compare the mate with the actual counit at \(N\):
\[
\begin{aligned}
dJ_C&=cSz_0-wc_M,\\
q_1J_C-I_C&=dK_C,\\
I_C&=bSz_0-h_wc_M-U_1(Ve_0)b_M+\chi .
\end{aligned}
\tag{B.RJ8}
\]
Indeed, the difference of the unlifted transposes is
\[
\operatorname{Adj}_1\bigl(V(e_0L_0z_0-e_0e_0^M)
                          \vartheta_{R_0}\bigr)=d\chi.
\]
Naturality of \(\vartheta\) on \(z_0\) and (B.RJ4)–(B.RJ5) therefore give
\(q_1(cSz_0-wc_M)=dI_C\). The full cone of
\(\operatorname{Hom}(SR_0,q_1)\) gives \(J_C,K_C\), since \(SR_0\) is whole h-projective.

Finally lift the particular homotopy \(\beta\) through \(q_1\):
\[
\begin{aligned}
dt&=z_1a-wv,&q_1t-I_\beta&=dk,\\
I_\beta&=U_1\beta\,r_A+H_1a+U_1e_1\,h_a\\
 &\qquad{}-h_wv-U_1(Ve_0)h_v .
\end{aligned}
\tag{B.RJ9}
\]
Here \(t:A\to Q_1\) has degree \(-1\) and \(k:A\to U_1VN\) degree \(-2\). To check the prescribed boundary, insert
\(q_1z_1=U_1e_1\rho_1+dH_1\), the equations for \(a,w,v\), and
\(U_1(d\beta)=U_1(e_1L_1c-Ve_0\vartheta_{Q_0})\).
This gives \(q_1(z_1a-wv)=dI_\beta\). Whole h-projectivity of \(A\) then supplies the entire pair \(t,k\). Replacing this calculation by an unspecified lift of the endpoints would lose the \(U_1\beta r_A\) term.

For clarity, every existence argument just used has the same form. For a whole h-projective source \(P\) and a replacement \(r:B\to D\), use the acyclic complex
\[
\mathcal C_r^n(P)=\operatorname{Hom}^n(P,B)
 \oplus\operatorname{Hom}^{n-1}(P,D),\qquad
\delta(x,y)=(dx,rx-dy).
\]
A closed pair \((D,I)\) with \(rD=dI\) has a primitive \((J,K)\) satisfying
\(dJ=D,\ rJ-I=dK\). This follows from the quasi-isomorphism
\(\operatorname{Hom}(P,r)\); it is not a claim that each desired primitive can be chosen with \(K=0\). Previously supplied compatible pairs in (B.RJ7)–(B.RJ9) can be retained.

**Compare the two right triangles without discarding a face.** Define maps of degree \(-1\), from \(SQ_0\) to \(Q_1\), by
\[
\begin{aligned}
\mathcal B&=J_CSu_0+wJ_U-tu_X-z_1J_F,\\
d\mathcal B&=cS(z_0u_0)-z_1u_1c,\\
\mathcal R&=cSJ_0-J_1c-\mathcal B,&d\mathcal R&=0.
\end{aligned}
\tag{B.RJ10}
\]
The second equation is obtained by substituting the four first-component boundaries; the intermediate \(wc_MSu_0\), \(wvu_X\), and \(z_1au_X\) cancel in order. The final equality then follows from the two equations for \(dJ_i\). A closed \(\mathcal R\) alone is not yet the required compatible comparison.

Its prescribed image under \(q_1\) is computed using all four second witnesses. Put
\[
\begin{aligned}
\mathcal T={}&K_CSu_0+U_1(Ve_0)K_U+h_wJ_U\\
 &{}-ku_X+U_1\beta\,\ell_X-U_1e_1K_F-H_1J_F,\\
\mathcal V={}&\xi+bSJ_0-K_1c-\mathcal T .
\end{aligned}
\tag{B.RJ11}
\]
Every term has degree \(-2\), source \(SQ_0\), and target \(U_1VN\).
A direct expansion gives
\[
\begin{aligned}
q_1\mathcal B={}&bS(z_0u_0-1)+\chi Su_0+U_1(Ve_0)\upsilon\\
 &{}-H_1u_1c-U_1e_1\ell_1c+d\mathcal T,\\
q_1cSJ_0={}&\chi Su_0+U_1(Ve_0)\upsilon
             +bS(z_0u_0-1)\\
 &{}+d(\xi+bSJ_0),\\
q_1J_1c={}&H_1u_1c+U_1e_1\ell_1c+d(K_1c),\\
q_1\mathcal R={}&d\mathcal V .
\end{aligned}
\tag{B.RJ12}
\]
Here are the sign-sensitive steps in the first expansion. The product
\(dh_w\,J_U\) is \(d(h_wJ_U)+h_wdJ_U\), and
\(dH_1\,J_F=d(H_1J_F)+H_1dJ_F\).
The remaining \(\beta,\ell_X\) terms combine as
\[
-U_1\beta\,r_Au_X+U_1(d\beta)\ell_X
=-b+d(U_1\beta\,\ell_X),
\]
using \(r_Au_X=\eta^1_{SQ_0}+d\ell_X\) and
\(U_1\beta\,\eta^1_{SQ_0}=b\).
These are precisely the three product terms in \(\mathcal T\), with their displayed signs. For the second line of (B.RJ12), naturality of the closed \(\vartheta\) on the degree-minus-one \(J_0\), followed by (B.RJ3), yields the terms \(\chi Su_0\), \(U_1(Ve_0)\upsilon\), and \(d\xi\). The remaining identity is
\((db)SJ_0=d(bSJ_0)+bS(dJ_0)\).
The third line is the retained second right-triangle equation (B.RJ2). Subtracting gives the fourth line, without assuming that any unresolved square strictly commutes.

Now \((\mathcal R,\mathcal V)\) is a closed element of
\(\mathcal C_{q_1}^{-1}(SQ_0)\). Its acyclicity supplies
\[
\begin{aligned}
dP&=\mathcal R,&q_1P-\mathcal V&=dW,\\
P:SQ_0&\longrightarrow Q_1,&|P|&=-2,\\
W:SQ_0&\longrightarrow U_1VN,&|W|&=-3 .
\end{aligned}
\tag{B.RJ13}
\]
This is the promised full compatibility of the right triangles, including their images at the actual right input. The degree-minus-three term is not an assertion that \(\mathcal V=q_1P\) literally.

The four composite routes being compared are:
\[
\begin{array}{ccccccc}
SQ_0&\xrightarrow{Su_0}&SR_0&\xrightarrow{Sz_0}&SQ_0&\xrightarrow{c}&Q_1\\
SQ_0&\xrightarrow{u_X}&A&\xrightarrow{v}&C&\xrightarrow{w}&Q_1\\
SQ_0&\xrightarrow{u_X}&A&\xrightarrow{a}&R_1&\xrightarrow{z_1}&Q_1\\
SQ_0&\xrightarrow{c}&Q_1&\xrightarrow{u_1}&R_1&\xrightarrow{z_1}&Q_1 .
\end{array}
\tag{B.RJ14}
\]
The first minus the second row has witness \(J_CSu_0+wJ_U\); the third minus the second has witness \(tu_X\); the fourth minus the third has witness \(z_1J_F\). Their signed sum is \(\mathcal B\). Shortening the first and fourth rows by the retained right triangles gives respectively \(cSJ_0\) and \(J_1c\). Their discrepancy from \(\mathcal B\) is \(dP\), whose image discrepancy is \(dW\). Thus the diagram records actual objects, arrows and both levels of comparison, rather than equalities asserted only after passing to cohomology.

**Geometric hypotheses.** All Hom complexes and cone primitives here are in the whole supplied diagram category. The free-index and evaluation arguments of (B.ND6), (B.TD4), and (B.JF13) give their fibrewise interpretations; pointwise h-projectivity is not substituted for whole h-projectivity. The comparison uses the actual \(\vartheta\) from the common graph/bar roof and preserves the old \(J_i,K_i\). When a comparison with a composite in the original nested resolution graph is required, the retained \(K_2\) of (B.BM14), (B.MX12) must be inserted before identifying the folded composite. Ordinary composition of the already folded maps above does not assert that this \(K_2\) vanishes.

This supplies the shared right-triangle interface for a closed resolved mate, and for an actual whole family of such mates. Extending \(P,W\) over the higher mixed-cube cells and the nested horizontal composition faces in the full changing-compactification presentation requires an additional geometric construction; a linear cone argument does not manufacture those target boundaries. Geometric multiplicative descent, coefficient transport and strict-heart effacement are not established by this construction. \(\square\)



### Join the right-triangle comparison to the cube

**Proposition B.1ak (retain the unit cube and both right-triangle witnesses).** The right-triangle comparison (B.RJ13) extends over the original mixed-cube cell in the fixed common resolved model (B.MX13), retaining the already chosen endpoint comparisons and the entire unit-cube face (B.UC9). Its final witness has degree \(-4\). The proof is a graded extension of the actual four-face calculation, not an inference from equality of degree-zero endpoints. Modules can be unbounded over an arbitrary commutative coefficient ring.

Keep the whole parameter/refinement categories, all replacements and the fixed maps of (B.RJ1)–(B.RJ6). In particular \(u_i,z_i,J_i,K_i,u_X,\ell_X,w,h_w\) are fixed. Let \(\Theta\) be the complex of homogeneous whole dg-natural comparisons \(L_1S\to VL_0\) on the resolved inputs. A homogeneous comparison has naturality sign
\(\vartheta_B L_1S(f)=(-1)^{|\vartheta||f|}VL_0(f)\vartheta_A\).
No value on an unresolved restriction module is introduced.

**First retain all mate and map lifts in one complex.** In degree \(n\), let
\(e=(\vartheta,c,b,c_M,b_M,v,h_v,a,h_a)\).
The maps \(c,c_M,v,a\) have degree \(n\), and \(b,b_M,h_v,h_a\) degree \(n-1\), with exactly the sources and targets of (B.RJ4)–(B.RJ5). Define
\[
\begin{aligned}
\Psi_N(\vartheta)&=\operatorname{Adj}_1(Ve_0\vartheta_{Q_0}),\\
\Psi_M(\vartheta)&=\operatorname{Adj}_1(Ve_0^M\vartheta_{R_0}),\\
\vartheta'&=d\vartheta,\qquad
(c',c_M',v',a')=(dc,dc_M,dv,da),\\
b'&=q_1c-\Psi_N(\vartheta)-db,\\
b_M'&=r_Cc_M-\Psi_M(\vartheta)-db_M,\\
h_v'&=r_Cv-U_1(\vartheta_{Q_0})r_A-dh_v,\\
h_a'&=\rho_1a-U_1(L_1c)r_A-dh_a .
\end{aligned}
\tag{B.RC1}
\]
These primed components define \(\partial_{\mathscr E}e\). Every displayed graph map is a chain map, including the map from \(c\) into the \(a\)-lift target, so \(\partial_{\mathscr E}^2=0\).
Write \(\beta(e)=\operatorname{Adj}_1^{-1}b\), and use \(\upsilon(\vartheta),\chi(\vartheta),\xi(\vartheta)\) from (B.RJ6), now in every degree. Their degrees are \(n-1,n-1,n-2\).

For a replacement \(r:B\to D\), write \(\mathcal C_r(P)\) for the full cone complex used after (B.RJ9), with
\(\delta(x,y)=(dx,rx-dy)\). Use the five particular complexes
\[
\begin{aligned}
\mathcal C_U&=\mathcal C_{r_C}(SQ_0),&
\mathcal C_F&=\mathcal C_{\rho_1}(SQ_0),\\
\mathcal C_C&=\mathcal C_{q_1}(SR_0),&
\mathcal C_\beta&=\mathcal C_{q_1}(A),\\
\mathcal C_N&=\mathcal C_{q_1}(SQ_0).
\end{aligned}
\tag{B.RC2}
\]
They are acyclic by the whole h-projectivity of \(SQ_0,SR_0,A\), not by pointwise projectivity.

**The four faces are chain maps in every degree.** Define
\(\Phi_\nu(e)=(D_\nu(e),I_\nu(e))\in\mathcal C_\nu^n\) for
\(\nu=U,F,C,\beta\), using
\[
\begin{aligned}
D_U&=c_MSu_0-vu_X,\\
I_U&=b_MSu_0-h_vu_X
       -(-1)^nU_1(\vartheta_{Q_0})\ell_X+\upsilon(\vartheta),\\
D_F&=u_1c-au_X,\\
I_F&=\ell_1c-(-1)^nU_1(L_1c)\ell_X-h_au_X .
\end{aligned}
\tag{B.RC3}
\]
The other two faces are
\[
\begin{aligned}
D_C&=cSz_0-wc_M,\\
I_C&=bSz_0-h_wc_M-U_1(Ve_0)b_M+\chi(\vartheta),\\
D_\beta&=z_1a-wv,\\
I_\beta&=U_1\beta(e)\,r_A+H_1a+U_1e_1h_a\\
 &\qquad{}-h_wv-U_1(Ve_0)h_v .
\end{aligned}
\tag{B.RC4}
\]
Then
\[
\begin{aligned}
\delta\Phi_\nu(e)&=\Phi_\nu(\partial_{\mathscr E}e),\\
d\upsilon(\vartheta)+\upsilon(d\vartheta)
 &=\Psi_M(\vartheta)Su_0-U_1(\vartheta_{Q_0})\eta^1_{SQ_0},\\
d\chi(\vartheta)+\chi(d\vartheta)
 &=\Psi_N(\vartheta)Sz_0-U_1(Ve_0)\Psi_M(\vartheta),\\
d\xi(\vartheta)-\xi(d\vartheta)
 &=\operatorname{Adj}_1(V(d\Gamma_0)\vartheta_{Q_0}).
\end{aligned}
\tag{B.RC5}
\]
The last three identities are the graded Leibniz rule and the retained equations (B.RJ3). They justify the first identity for the \(U,C\) faces. For the \(F\) face, use
\(d(\ell_1c)=d\ell_1c-\ell_1dc\), the unit naturality on the homogeneous \(c\), and the last equation of (B.RC1). After cancellation,
\(\rho_1D_F-dI_F=\ell_1dc+(-1)^nU_1(L_1dc)\ell_X-h_a'u_X\), precisely \(I_F(\partial_{\mathscr E}e)\).
For the final face,
\(d\beta(e)=e_1L_1c-Ve_0\vartheta_{Q_0}-\beta(\partial_{\mathscr E}e)\).
Substituting it gives
\(q_1D_\beta-dI_\beta=
 U_1\beta(\partial_{\mathscr E}e)r_A+H_1da+U_1e_1h_a'
 -h_wdv-U_1(Ve_0)h_v'\), the required \(I_\beta\) at the primed tuple.
The first components commute with differential because the fixed maps \(u_i,z_i,w,u_X\) are closed.

**Include the entire four-face lift.** Set
\[
\begin{aligned}
\mathscr F^n&=\mathscr E^n\oplus
 \bigoplus_{\nu=U,F,C,\beta}\mathcal C_\nu^{\,n-1},\\
f&=(e,j_U,j_F,j_C,j_\beta),\\
j_U&=(J_U,K_U),\quad j_F=(J_F,K_F),\\
j_C&=(J_C,K_C),\quad j_\beta=(t,k),\\
\partial_{\mathscr F}f
 &=\bigl(\partial_{\mathscr E}e,\,
         (\Phi_\nu(e)-\delta j_\nu)_\nu\bigr).
\end{aligned}
\tag{B.RC6}
\]
Equation (B.RC5) proves that this differential squares to zero. Its closed degree-zero elements are exactly the data and four full faces in (B.RJ4)–(B.RJ9).

Retaining only \(\vartheta,c_M,b_M,v,h_v\) and \(j_U\) gives the old unit extension \(\widetilde{\mathscr U}\) of (B.UC3)–(B.UC6), with
\(Q=Q_0,\ P_0=R_0,\ B=C\). This projection is a degreewise surjective chain map with acyclic kernel. To see this without assuming that the coupled lifts are a direct sum, first filter the omitted \(c,b,a,h_a\) complex by its \(a,h_a\) subcomplex. The subcomplex and quotient are the shifted cones of \(\operatorname{Hom}(A,\rho_1)\) and \(\operatorname{Hom}(SQ_0,q_1)\). In the full kernel, the three omitted face cones shifted by \(-1\) form a subcomplex; the quotient is this omitted-lift complex. This finite filtration has acyclic subquotients, so its total kernel is acyclic. Consequently an already fixed whole unit-cube cell can be retained while the other three faces are supplied relatively.

**The right-triangle discrepancy is an anticommuting map.** For homogeneous \(f\in\mathscr F^n\) put
\[
\begin{aligned}
\mathcal B(f)&=J_CSu_0+wJ_U-tu_X-z_1J_F,\\
\mathcal R(f)&=(-1)^n cSJ_0-J_1c-\mathcal B(f),\\
d\mathcal R(f)+\mathcal R(\partial_{\mathscr F}f)&=0 .
\end{aligned}
\tag{B.RC7}
\]
The sign in the first term of \(\mathcal R\) is essential: \(J_0\) is composed on the right, whereas \(J_1\) is composed on the left. To verify the last line, use
\(d(cSJ_0)=dc\,SJ_0+(-1)^ncS(dJ_0)\) and
\(d(J_1c)=dJ_1c-J_1dc\).
The four first-component equations of (B.RC6) give
\(\mathcal B(\partial_{\mathscr F}f)
 =cS(z_0u_0)-z_1u_1c-d\mathcal B(f)\).
The two retained right-triangle equations complete the cancellation.

Define degree-\((n-2)\) maps from \(SQ_0\) to \(U_1VN\) by
\[
\begin{aligned}
\mathcal T(f)={}&K_CSu_0+U_1(Ve_0)K_U+h_wJ_U-ku_X\\
 &{}+(-1)^nU_1\beta(e)\ell_X-U_1e_1K_F-H_1J_F,\\
\mathcal V_0(e)={}&\xi(\vartheta)+(-1)^n bSJ_0-K_1c,\\
\mathcal V(f)={}&\mathcal V_0(e)-\mathcal T(f).
\end{aligned}
\tag{B.RC8}
\]
For \(n=0\) these are exactly (B.RJ11), without a new choice of primitive.
Let
\(\mathcal A(e)=bS(z_0u_0-1)+\chi(\vartheta)Su_0+
 U_1(Ve_0)\upsilon(\vartheta)-H_1u_1c-U_1e_1\ell_1c\).
The full graded expansion is
\[
\begin{aligned}
q_1\mathcal B(f)
 &=\mathcal A(e)+d\mathcal T(f)-\mathcal T(\partial_{\mathscr F}f),\\
q_1\bigl((-1)^ncSJ_0-J_1c\bigr)
 &=\mathcal A(e)+d\mathcal V_0(e)
                  -\mathcal V_0(\partial_{\mathscr E}e),\\
q_1\mathcal R(f)-d\mathcal V(f)
 &=-\mathcal V(\partial_{\mathscr F}f).
\end{aligned}
\tag{B.RC9}
\]
Here the second components of (B.RC6) read, for example,
\(q_1J_C=I_C+dK_C-K_C'\). The extra primed terms in all four faces assemble to \(-\mathcal T(\partial_{\mathscr F}f)\); omitting them would only prove the closed-edge calculation. In the sign-sensitive part, the \(\beta,\ell_X\) terms combine to
\[
-b+d\bigl((-1)^nU_1\beta(e)\ell_X\bigr)
       +(-1)^nU_1\beta(\partial_{\mathscr E}e)\ell_X.
\]
The terms from \(dh_wJ_U\) and \(dH_1J_F\) give the primed corrections
\(-h_wJ_U'\) and \(+H_1J_F'\), respectively.
For the second line of (B.RC9), naturality on the degree-minus-one \(J_0\) supplies the additional \((-1)^n\). It cancels the displayed sign before \(cSJ_0\). Equation (B.RJ3), followed by the last identity of (B.RC5), gives the \(\xi\) contribution; and
\((-1)^n(db)SJ_0=d((-1)^nbSJ_0)+bS(dJ_0)\).
These computations prove (B.RC9) in every degree.

Thus \(\Omega(f)=(\mathcal R(f),\mathcal V(f))\) has degree \(-1\) as a map into \(\mathcal C_N\), and
\[
\begin{aligned}
\delta\Omega+\Omega\partial_{\mathscr F}&=0,\\
\mathscr G^n&=\mathscr F^n\oplus\mathcal C_N^{\,n-2},\\
\partial_{\mathscr G}(f,p)
 &=\bigl(\partial_{\mathscr F}f,\,\delta p-\Omega(f)\bigr),\\
\partial_{\mathscr G}^{\,2}&=0 .
\end{aligned}
\tag{B.RC10}
\]
The plus differential on the \(\mathcal C_N[-2]\) summand is deliberate. Replacing it by the sign for a once-shifted cone would not square to zero.
The kernel of \(\mathscr G\to\mathscr F\) is the acyclic complex
\(\mathcal C_N[-2]\), and the projection is surjective in every degree.
At degree zero, a closed lift has \(p=(P,W)\) and
\(\delta p=\Omega(f)\), exactly (B.RJ13).

**Retain the original mixed-cube face.** Let \(\vartheta_T,\vartheta_B,\vartheta_H\) be the two pasted left comparisons and their full degree-minus-one cube cell from (B.MX13), so
\(d\vartheta_H=\vartheta_T-\vartheta_B\). This is the image of the full \((0,H,K)\) cell through the original common graph/bar roof; the retained nested \(K_2\) and transfer signs are not discarded. Let \(f_T,f_B\) be the closed endpoint data from B.1aj, using the unit faces retained by B.1ai.

The old unit-cube record consists of \(e_H^U\), with differential
\(e_T^U-e_B^U\), and \(w_U\) satisfying
\(\delta w_U=j_{U,T}-j_{U,B}-\Phi_U(e_H^U)\), as in (B.UC9). With the differential convention of (B.RC6), its retained degree-minus-one element is
\[
\begin{aligned}
u_H&=(e_H^U,-w_U)\in\widetilde{\mathscr U}^{-1},\\
\partial u_H&=u_T-u_B,\\
\pi(f_H)&=u_H,\qquad
\partial_{\mathscr F}f_H=f_T-f_B .
\end{aligned}
\tag{B.RC11}
\]
The last lift exists by the acyclic kernel of
\(\pi:\mathscr F\to\widetilde{\mathscr U}\).
Explicitly, choose a graded lift of \(u_H\). Its differential minus the prescribed endpoint difference is a cycle in that kernel; subtract a primitive there. This retains the full old unit-cube witness with its required minus sign, as well as both endpoint four-face records. It does not replace them with independently selected pointwise homotopies.

Now retain any endpoint comparisons
\(p_T=(P_T,W_T)\), \(p_B=(P_B,W_B)\) satisfying (B.RJ13).
Equation (B.RC10) shows that
\(p_T-p_B+\Omega(f_H)\) is closed in \(\mathcal C_N^{-2}\).
Acyclicity supplies \(p_H=(P_H,W_H)\) with
\[
\begin{aligned}
\delta p_H&=p_T-p_B+\Omega(f_H),\\
dP_H&=P_T-P_B+\mathcal R(f_H),\\
q_1P_H-dW_H&=W_T-W_B+\mathcal V(f_H),\\
|P_H|&=-3,\qquad |W_H|=-4 .
\end{aligned}
\tag{B.RC12}
\]
Equivalently
\(\partial_{\mathscr G}(f_H,p_H)=(f_T,p_T)-(f_B,p_B)\).
This compares the full right-triangle witnesses over the actual cube. A primitive of the first equation alone, or a new arbitrary choice of endpoint \(P,W\), would not supply this relative extension.

The comparison complexes and the retained-data map are:
\[
\begin{array}{ccccc}
\mathscr G&\xrightarrow{\mathrm{forget}\ (P,W)}&
\mathscr F&\xrightarrow{\mathrm{retain}\ U}&
\widetilde{\mathscr U}\\
(f,p)&\longmapsto&f&\longmapsto&(e_U,j_U).
\end{array}
\tag{B.RC13}
\]
Both arrows are degreewise surjective chain maps with acyclic kernels. The right-hand endpoint and cube records are the existing unit comparison; the middle layer adds the other three faces; the left layer retains the right triangles and the degree-minus-four cube witness. A further **specified free linear cell** can be extended by the same kernel argument, after its target differential and all retained faces are actually supplied.

**Scope.** The fixed-common-model mixed cube carries unit and right-triangle interfaces with their prescribed higher witnesses. These linear complexes do not provide a multiplicative presentation. A complete changing-compactification and finite composition diagram requires the nested horizontal faces, their prescribed \(K_2\), and compatible higher overlap boundaries. This construction does not imply arbitrary proper-image quasi-isomorphisms, the existence of unresolved inverses, or invertibility of the right mate. It also does not establish geometric multiplicative descent, coefficient-system transport or strict-heart effacement. \(\square\)



### Retain every stage in horizontal mate pasting

**Proposition B.1al (the target of an arbitrary horizontal string).** The resolved two-stage construction (B.BM18) has one ordered formula for every finite string of adjunctions. It retains every intermediate replacement and every lift witness. Cutting the string anywhere, or evaluating any binary parenthesization of these cuts, gives the same mate lift and the same counit homotopy, under the canonical balanced associators. This supplies actual horizontal target maps for the remaining assembly; it does not assert that all of their unit and triangle faces have already been joined across changing geometric models.

Fix \(m\geq1\). For \(0\leq i<m\), let \(L_i\dashv U_i\) and \(L_i'\dashv U_i'\) be the induction/restriction adjunctions at the two ends of the horizontal array, with vertical induction functors \(S_i\) and specified closed comparisons
\[
 \theta_i:L_i'S_i\longrightarrow S_{i+1}L_i.
 \tag{B.HS1}
\]
As in (B.BM16), these comparisons need only be natural on the whole h-projective inputs used below. They are never evaluated at an unresolved restriction module. The induction functors preserve whole h-projectivity; the restrictions preserve quasi-isomorphisms. Keep the actual kernel models and strict common roofs of B.1ad--B.1af when applying this calculation geometrically.

**Keep the nested replacement at every vertex.** Set \(Q_m=N\), \(Q_m'=S_mN\). Choose the two chains
\[
\begin{aligned}
q_i:Q_i&\longrightarrow U_iQ_{i+1},&
q_i':Q_i'&\longrightarrow U_i'Q_{i+1}',\\
e_i&=\varepsilon^i_{Q_{i+1}}L_iq_i,&
e_i'&=\varepsilon^{i'}_{Q_{i+1}'}L_i'q_i',\\
a_i&=S_{i+1}e_i\,\theta_{i,Q_i},&
c_m&=1_{S_mN}.
\end{aligned}
\tag{B.HS2}
\]
The \(q_i,q_i'\) are quasi-isomorphisms with whole h-projective sources. The final module \(N\) need not itself be h-projective. Choose closed \(c_i:S_iQ_i\to Q_i'\), descending from \(i=m-1\) to \(0\), together with degree-minus-one \(b_i\), by
\[
\begin{aligned}
q_i'c_i-\operatorname{Adj}_{L_i'}(c_{i+1}a_i)&=db_i,\\
D_i=\operatorname{Adj}_{L_i'}^{-1}(b_i),\qquad
dD_i&=e_i'L_i'c_i-c_{i+1}a_i .
\end{aligned}
\tag{B.HS3}
\]
Existence is the Hom quasi-isomorphism out of \(S_iQ_i\), whose whole h-projectivity has just been specified. These are the actual successive resolved transposes, not a product of unresolved right mates. In particular every \(D_i\) is the full Hom-complex transpose of the retained \(b_i\).

For \(a\leq b\), write
\[
\begin{aligned}
P_{b:a}&=L_{b-1}\cdots L_a,&
P_{b:a}'&=L_{b-1}'\cdots L_a',&
U_{a:b}'&=U_a'\cdots U_{b-1}',\\
E_{a:a}&=1,&E_{b:a}&=e_{b-1}L_{b-1}E_{b-1:a},\\
E_{a:a}'&=1,&E_{b:a}'&=e_{b-1}'L_{b-1}'E_{b-1:a}',\\
A_{a:a}&=1,&A_{b:a}&=a_{b-1}L_{b-1}'A_{b-1:a},\\
\Xi_{a:a}&=1,&
\Xi_{b:a}&=(\theta_{b-1}P_{b-1:a})(L_{b-1}'\Xi_{b-1:a}),\\
A_{b:a}&=S_bE_{b:a}\,\Xi_{b:a,Q_a}.
\end{aligned}
\tag{B.HS4}
\]
Empty strings mean the identity functor or map on the indicated object. The last identity follows by induction: move \(\theta_{b-1}\) past \(E_{b-1:a}:P_{b-1:a}Q_a\to Q_{b-1}\). Both ends are h-projective whenever this move is needed. The final step uses \(\theta_{m-1}\) only at such inputs, not at \(N\). Thus the ordered composite uses exactly the resolved naturality allowed in (B.BM18).

**One full counit witness for the string.** Define
\[
\begin{aligned}
D_{b:a}
 &=\sum_{i=a}^{b-1}
 E_{b:i+1}'\,P_{b:i+1}'
       \bigl(D_i\,L_i'A_{i:a}\bigr),\\
dD_{b:a}
 &=E_{b:a}'P_{b:a}'c_a-c_bA_{b:a}.
\end{aligned}
\tag{B.HS5}
\]
All summands have source \(P_{b:a}'S_aQ_a\), target \(Q_b'\), and degree \(-1\). The sum is finite because the string is finite, not because any module is bounded. To verify its differential, substitute (B.HS3). The negative term for index \(i\) is
\(-E_{b:i+1}'P_{b:i+1}'(c_{i+1}a_iL_i'A_{i:a})\).
It cancels the positive term for index \(i+1\), by the recursions for \(A\) and \(E'\). The only surviving terms are the two displayed endpoints. All outer factors are closed of degree zero, so no factor interchange or additional sign is implicit.

Let
\[
\begin{aligned}
q_{a:b}'&=(U_{a:b-1}'q_{b-1}')\cdots
                   (U_a'q_{a+1}')q_a',\\
B_{b:a}&=\operatorname{Adj}_{P_{b:a}'}(D_{b:a}),\\
\zeta_{b:a}&=\operatorname{Adj}_{P_{b:a}'}
                  (c_bS_bE_{b:a}\,\Xi_{b:a,Q_a}),\\
q_{a:b}'c_a-\zeta_{b:a}&=dB_{b:a}.
\end{aligned}
\tag{B.HS6}
\]
For \(a=b\), set \(q_{a:a}'=1\), \(D_{a:a}=B_{a:a}=0\). The composite adjunction is \(P_{b:a}'\dashv U_{a:b}'\). Its counit is the iterated counit, so the transpose of \(q_{a:b}'\) is exactly \(E_{b:a}'\), as can also be checked by applying each Hom adjunction in order. This proves the last line from (B.HS5). Exactness of restriction makes \(q_{a:b}'\) a quasi-isomorphism; its source remains \(Q_a'\), not an unresolved intermediate module. At the full interval \(c_b=c_m=1\), so \(c_0,B_{m:0}\) are the desired lift and complete witness for the pasted left cell \(\Xi_{m:0}\).

**Cuts preserve the witness, not only its class.** For \(a<k<b\),
\[
\begin{aligned}
D_{b:a}
 &=E_{b:k}'P_{b:k}'D_{k:a}
       +D_{b:k}P_{b:k}'A_{k:a},\\
B_{b:a}
 &=U_{a:k}'(q_{k:b}')\,B_{k:a}
       +\operatorname{Adj}_{P_{k:a}'}
                       (B_{b:k}A_{k:a}).
\end{aligned}
\tag{B.HS7}
\]
The first equality partitions the sum (B.HS5) at \(k\): for \(i<k\), factor the final \(E'\); for \(i\geq k\), factor the initial \(A\). The second follows by the full Hom-complex adjunction, naturality of its unit and counit, and the equality between the transpose of \(q_{k:b}'\) and \(E_{b:k}'\). This argument also proves the signs of the degree-minus-one term; it is not a transpose limited to closed degree-zero maps.

For \(a=0,k=1,b=2\), the second line is exactly
\[
 B_{2:0}=U_0'q_1'\,b_0+
       \operatorname{Adj}_{L_0'}(b_1S_1e_0\,\theta_{0,Q_0}),
 \tag{B.HS8}
\]
with \(Q_1=R,Q_0=Z,Q_1'=R',Q_0'=Z'\), \(b_1=b_\nu\), \(b_0=b_\psi\). It is (B.BM18), including both terms. Repeatedly partitioning the same finite sum proves equality for every binary parenthesization. No new primitive is chosen at an internal node, and no cancellation of a merely closed unexplained defect is claimed.

The cut and its homotopies have the following native diagram:
\[
\begin{array}{ccccc}
 P_{b:a}'S_aQ_a&
 \xrightarrow{\ P_{b:k}'A_{k:a}\ }&
 P_{b:k}'S_kQ_k&
 \xrightarrow{\ A_{b:k}\ }&S_bQ_b\\
 {\scriptstyle P_{b:a}'c_a}\downarrow&&
 {\scriptstyle P_{b:k}'c_k}\downarrow&&
 \downarrow{\scriptstyle c_b}\\
 P_{b:a}'Q_a'&
 \xrightarrow{\ P_{b:k}'E_{k:a}'\ }&
 P_{b:k}'Q_k'&
 \xrightarrow{\ E_{b:k}'\ }&Q_b'.
\end{array}
\tag{B.HS9}
\]
The left and right squares commute up to \(P_{b:k}'D_{k:a}\) and \(D_{b:k}\), respectively. Equation (B.HS7) is the precise outer homotopy. This is a homotopy-commutative diagram, not a claim of strict commutativity.

**Bind the parameter folds to the original nested graph.** For this identification keep the adjunctions identical, with \(S_i=1,\theta_i=1\), and allow an arbitrary terminal vertex map instead of the identity in (B.HS2). The closed degree-zero equation (B.HS3) is then the nested replacement-graph equation. For general homogeneous vertex and witness coordinates use the same graded sum (B.HS5), whether or not the graph differential vanishes; its chain and higher identities are (B.RS8), not an assumption that these coordinates are closed lifts. Transport all edges and witnesses to the innermost category by \(U_{0:i}=U_0\cdots U_{i-1}\). The one-input witness in (B.HS6) then becomes the selected-edge coefficient \(W_1\) of (B.RS4). Indeed the transpose identity
\(\operatorname{Adj}_{L_i}(h\,\varepsilon^i L_iq_i)=U_i(h)q_i\)
moves each witness to its original position in the ordered product. It holds in every homogeneous degree. This verifies the link to (B.NR7); it does not supply a different fold whose higher coefficients vanish.

For example, in a three-stage string, write \(\widetilde q_i,\widetilde h_i\) for these transported maps, with edge indices \(0,1,2\). For parameter arrows \(t:x^0\to x^1\), \(s:x^1\to x^2\), \(u:x^2\to x^3\), the retained coefficients are
\[
\begin{aligned}
W_2(s,t)
 &=\widetilde q_2^{\,2}\widetilde h_1(s)\widetilde h_0(t)
   +\widetilde h_2(s)\widetilde q_1^{\,1}\widetilde h_0(t)\\
 &\quad+\widetilde h_2(s)\widetilde h_1(t)\widetilde q_0^{\,0},\\
W_3(u,s,t)
 &=\widetilde h_2(u)\widetilde h_1(s)\widetilde h_0(t).
\end{aligned}
\tag{B.HS10}
\]
They have degrees \(|s|+|t|-2\) and \(|u|+|s|+|t|-3\); their graph triples have one greater degree. The full all-length coefficients, bar differential and cut convolution are (B.RS4), (B.RS8), and (B.RS9), respectively. Their proof is algebraic and does not require the intermediate restricted modules to be h-projective. For the right-replacement graphs the Hom quasi-isomorphism instead follows by forgetting the inner replacement one at a time and using whole h-projectivity of each \(Q_i\), exactly as in (B.NR6). This distinguishes the algebraic fold identity from the reason that its graph projections are quasi-equivalences. The ordinary multiplicativity correction still has sign \((-1)^{|s|+1}K_2(s,t)\); at three stages \(K_3\) need not vanish.

The strict roof (B.SF7) evaluates every word using these coefficients. Its cut equality follows from (B.RS10); it does not follow by pretending that \(K_1\) is a strict functor. The graph-to-bar signs and opposite-Hom convention remain those of (B.KC10)--(B.KC11).

**Geometric hypotheses.** Equations (B.HS5)--(B.HS8) specify the full horizontal mate targets, counit witnesses and all cut comparisons for each supplied finite resolved string. They can be used as the actual input to the unit and right-triangle complexes of B.1ai--B.1ak after passing to the stated common strict roof. They do not yet identify the retained triangles of a composite adjunction with the sequential triangles on every overlap of changing compactifications. That common target presentation and its shared unit, triangle and mixed-cube faces still have to be assembled; the degree-minus-four witness of (B.RC12) and the higher coefficients above must be retained there. Geometric multiplicative descent, coefficient-system transport and strict-heart effacement are not established by this construction. \(\square\)



### Compare the sequential and composite triangles

**Proposition B.1am (the second folding coefficient enters the second triangle witness).** For any finite nested chain in the whole normalized refinement categories of B.1ah, the sequential unit and counit lifts admit a nested right-triangle primitive. Folding that primitive gives the composite right triangle only after adding the original second folding coefficient to its second witness. The resulting two-level triangle and its comparison with the left triangle are independent of the binary parenthesization of the fixed master string. Previously chosen whole-diagram triangle records can remain unchanged, with the explicit degree-minus-two and degree-minus-three transition below. This is an actual comparison over the supplied refinement family, not completion of the full geometric base-change array.

Work with a finite string \(L_i\dashv U_i\), \(0\leq i<m\), in the whole transport module categories. Concretely these are the inductions and restrictions of strict functors between the transport categories, as in (B.JF1)--(B.JF2), now with finitely many intermediate categories. Induction preserves whole h-projectivity and restriction preserves quasi-isomorphisms. Evaluation has the properties proved in (B.TD4); an extra dg parameter is replaced by its free index before using (B.ND6). Thus the following Hom arguments are about entire diagrams, not independent fibrewise choices. No boundedness or field assumption is made.

Keep the original right-input chain
\[
 q_i:Q_i\longrightarrow U_iQ_{i+1},\qquad Q_m=N,
 \qquad q=q_{0:m}:Q_0\longrightarrow U_{0:m}N.
 \tag{B.NT1}
\]
The \(q_i\) are quasi-isomorphisms with whole h-projective sources for \(i<m\), and \(q\) is their ordered restriction composite (B.HS6). Put \(P_{b:a}=L_{b-1}\cdots L_a\), \(P=P_{m:0}\), \(U=U_{0:m}\), and
\[
\begin{aligned}
A_i&=P_{i:0}Q_0,\qquad M=A_m=PQ_0,\\
e_i&=\varepsilon^i L_iq_i,\qquad
v_i=E_{i:0}:A_i\longrightarrow Q_i,\\
v_0&=1,\qquad v_m=e=\operatorname{Adj}_{P}^{-1}(q),\\
q_iv_i&=U_i(v_{i+1})\eta^i_{A_i}.
\end{aligned}
\tag{B.NT2}
\]
The last identity is the ordinary adjunction identity for
\(v_{i+1}=e_iL_iv_i\). Each \(A_i\) is whole h-projective, although \(N\) need not be. The maps \(\eta^i_{A_i}:A_i\to U_iA_{i+1}\) are unit maps, not assumed quasi-isomorphisms.

**Resolve the left image and lift the entire nested unit.** Choose
\(r_i:R_i\to U_iR_{i+1}\), \(R_m=M\), with whole h-projective replacement sources and quasi-isomorphisms \(r_i\). Write \(r=r_{0:m}:R_0\to UM\). Descending from \(u_m=1_M\), choose closed \(u_i:A_i\to R_i\) and degree-minus-one \(\ell_i\) with
\[
 r_i u_i-U_i(u_{i+1})\eta^i_{A_i}=d\ell_i .
 \tag{B.NT3}
\]
Every lift uses \(\operatorname{Hom}(A_i,r_i)\); it does not use a quasi-isomorphism claim about the unit. Let \(\ell=W_1(u)\) be the first folding coefficient for this unit ladder. The algebraic formula (B.RS4) applies even though the source unit edges are not quasi-isomorphisms, and gives
\(ru_0-\eta^P_{Q_0}=d\ell\).

Likewise descend from \(z_m=e:M\to N\), choosing closed \(z_i:R_i\to Q_i\) and degree-minus-one \(h_i\) with
\[
 q_i z_i-U_i(z_{i+1})r_i=dh_i .
 \tag{B.NT4}
\]
Here the Hom source is \(R_i\). Set \(H=W_1(z)\); then
\(qz_0-U(e)r=dH\). These are the same two folded unit/counit equations as (B.JF6) and (B.JF8), with every intermediate stage retained.

**Solve the right triangle inside the nested graph.** Define
\[
\begin{aligned}
D_i&=z_iu_i-v_i,\\
I_i&=h_i u_i+U_i(z_{i+1})\ell_i,\\
dD_i&=0,\qquad
q_iD_i-U_i(D_{i+1})\eta^i_{A_i}=dI_i,\qquad D_m=0.
\end{aligned}
\tag{B.NT5}
\]
Expand \(q_i z_i u_i\), first using (B.NT4), then (B.NT3), and subtract (B.NT2). The two retained degree-zero maps are closed, so the result is exactly the displayed \(dI_i\).

There are degree-minus-one \(J_i:A_i\to Q_i\) and degree-minus-two
\(K_i:A_i\to U_iQ_{i+1}\), with \(J_m=0\), satisfying
\[
\begin{aligned}
dJ_i&=D_i,\\
q_iJ_i-U_i(J_{i+1})\eta^i_{A_i}-I_i&=dK_i .
\end{aligned}
\tag{B.NT6}
\]
Here is the complete descending construction. Suppose \(J_{i+1}\) has been chosen. The pair
\((D_i,I_i+U_i(J_{i+1})\eta^i_{A_i})\)
is closed in the cone with differential
\(\delta(x,y)=(dx,q_ix-dy)\), by (B.NT5) and
\(dJ_{i+1}=D_{i+1}\). That cone is acyclic because
\(\operatorname{Hom}(A_i,q_i)\) is a quasi-isomorphism. Choose its full primitive \((J_i,K_i)\). Starting with \(J_m=0\) proves every equation. This also proves acyclicity of the nested Hom kernel of projection to its terminal vertex: forgetting one inner stage has precisely such a shifted cone as kernel. Crucially, this uses the **receiving** replacement \(q_i\) and h-projectivity of \(A_i\), not the false premise that a source unit is a quasi-isomorphism.

Let \(\mathcal J\) denote the degree-minus-one nested graph map with vertex coordinates \(J_i\) and edge coordinates \(K_i\). Let \(v\) denote the canonical ladder (B.NT2), with zero edge witnesses. Equations (B.NT6) say
\(D\mathcal J=zu-v\) as a full graph equality, not just an equality on its first vertex.

**The fold is not multiplicative in its first coefficient.** Use the original higher fold, denoted \(\mathcal F\) here, in exactly the suspension convention (B.RS7)--(B.RS8). Transport every edge to the innermost category by \(U_{0:i}\) before evaluating its path sums. Define
\[
\begin{aligned}
K_{\mathrm{seq}}&=W_1(\mathcal J),&
C&=W_2(z,u),\\
I&=Hu_0+U(e)\ell,&
J&=J_0,\qquad K=K_{\mathrm{seq}}+C .
\end{aligned}
\tag{B.NT7}
\]
Both \(K_{\mathrm{seq}}\) and \(C\) have degree \(-2\).
For the closed degree-zero inputs \(z,u\), the ordinary multiplicativity homotopy is
\[
\begin{aligned}
\mathcal H(z,u)&=-\mathcal F_2(z,u),\\
\mathcal F_1(zu)-\mathcal F_1(z)\mathcal F_1(u)
   &=D\mathcal H(z,u),\\
W_1(zu)&=I+dC,\\
dJ&=z_0u_0-1,\qquad qJ-I=dK .
\end{aligned}
\tag{B.NT8}
\]
The minus in the first line is \((-1)^{|z|+1}\), not an optional convention. Since the graph differential on a pure third component is minus its ordinary differential, the third component of \(D(-\mathcal F_2)\) is \(+dC\). Next apply the chain map \(\mathcal F_1\) to \(D\mathcal J=zu-v\). Its terminal vertex is zero, its initial vertex is \(J_0\), and \(W_1(v)=0\); hence
\(qJ_0-dK_{\mathrm{seq}}=W_1(zu)=I+dC\).
Rearranging proves the final line. This is why using \(K_{\mathrm{seq}}\) alone can give a false second triangle equation.

The two homotopy routes are summarized by the following diagram of boundaries:
\[
\begin{array}{ccc}
 \mathcal F_1(zu)-\mathcal F_1(v)&=&D\mathcal F_1(\mathcal J)\\
 {\scriptstyle -\,D\mathcal H(z,u)}\downarrow&&
 \downarrow{\scriptstyle -\,D\mathcal H(z,u)}\\
 \mathcal F_1(z)\mathcal F_1(u)-\mathcal F_1(v)&=&
 D\bigl(\mathcal F_1(\mathcal J)-\mathcal H(z,u)\bigr).
\end{array}
\tag{B.NT9}
\]
The arrows mean subtraction of the indicated boundary, not new degree-zero module maps. In the lower right, the third component of
\(\mathcal F_1(\mathcal J)-\mathcal H\) is precisely \(K_{\mathrm{seq}}+C\).

For two stages the correction is the actual nested coefficient
\(C=U_0(h_1)\ell_0\).
For an arbitrary finite string it is the entire selected-pair sum (B.RS4), not just this one product. The cut convolution (B.RS9) and equality (B.RS10) identify both \(\mathcal F_1(\mathcal J)\) and \(\mathcal F_2(z,u)\) for every binary tree on the same master string. Thus \(J,K\) are identical under every such parenthesization, with the balanced associators retained. The higher coefficients, including the nonzero cubic coefficient (B.HS10), remain in the strict roof on parameter words. This conclusion is not obtained by suppressing those coefficients.

**Compare with the left triangle and preserve an older right triangle.** Let
\[
\begin{aligned}
e^M&=\operatorname{Adj}_P^{-1}(r),&
\lambda&=\operatorname{Adj}_P^{-1}(\ell),&
\alpha&=\operatorname{Adj}_P^{-1}(H),&
\Gamma&=\operatorname{Adj}_P^{-1}(K).
\end{aligned}
\]
Then the full Hom adjunction, applied to (B.NT3), (B.NT4) and (B.NT8), gives
\[
\begin{aligned}
d\lambda&=e^M P u_0-1_M,\\
d\alpha&=ePz_0-e\,e^M,\\
ePJ-\alpha Pu_0-e\lambda&=d\Gamma .
\end{aligned}
\tag{B.NT10}
\]
These are exactly the left/right comparison identities (B.JF7), (B.JF11), now with the second coefficient included by construction.

If an older whole-diagram pair \(J_{\mathrm{old}},K_{\mathrm{old}}\) for these same retained \(u_0,z_0,\ell,H,q\) is already fixed, leave it unchanged. The difference is closed in the same acyclic full cone, so there exist \(P_2,W_3\) with
\[
\begin{aligned}
J-J_{\mathrm{old}}&=dP_2,& |P_2|&=-2,\\
qP_2-(K-K_{\mathrm{old}})&=dW_3,& |W_3|&=-3 .
\end{aligned}
\tag{B.NT11}
\]
This compares the actual second witnesses as well as the first homotopies; it does not silently replace an old record by a newly chosen one. The equality-of-inputs hypothesis matters. If unit or counit lifts differ, first retain and compare their complete cone data as in B.1aj--B.1ak; (B.NT11) does not identify incompatible endpoint records.

All lifts above occur in the whole normalized refinement categories. The actual transport induction comparisons (B.JF2) therefore make them natural under their specified refinement and input maps. For additional specified free cells one uses the same acyclic-kernel calculation, relative to the already checked boundary. It remains necessary to give the actual noninvertible base-change and horizontal-composition overlap maps before making that relative application. In particular (B.HS6) supplies the horizontal mate target, and (B.RC11)--(B.RC12) supplies the retained mixed-cube triangle; their joint changing-model target presentation requires an additional comparison of geometric diagrams. Geometric multiplicative descent, coefficient-system transport and strict-heart effacement are not established by this construction. \(\square\)



### Join horizontal mates and retained triangle cubes

**Proposition B.1an (keep the horizontal witness while joining the triangles).** In a supplied common geometric refinement/base-change model, the actual finite-string horizontal mate of (B.HS6) and the retained unit-cube record of (B.RC11) can be kept simultaneously while the other three faces are supplied. The corrected sequential triangle of (B.NT7) then transports the complete right-triangle comparison and its degree-minus-four cube witness by an explicit chain isomorphism. This retains compatible old records; it does not identify incompatible choices without a comparison. The result concerns the whole parameter/refinement Hom complexes, over an arbitrary commutative ring and with unbounded modules.

**Put the actual horizontal input in the common target.** For one finite horizontal string, use (B.HS2)--(B.HS6) and, in the notation of B.1ak, set
\[
\begin{aligned}
(L_0,U_0)&=(P_{m:0},U_{0:m}),&
(L_1,U_1)&=(P'_{m:0},U'_{0:m}),\\
S&=S_0,\qquad V=S_m,&
\vartheta&=\Xi_{m:0},\\
q_0&=q_{0:m},\qquad q_1=q'_{0:m},&
c&=c_0,\qquad b=B_{m:0},\\
q_1c-\Psi_N(\vartheta)&=db,&
\Psi_N(\vartheta)&=\operatorname{Adj}_1(Ve_0\vartheta_{Q_0}).
\end{aligned}
\tag{B.HC1}
\]
Here \(Q_1\) in the two-column notation means the primed initial replacement \(Q'_0\) of the string; \(e_0=E_{m:0}\). The subscripts \(0,1\) on \(L_i,U_i\) now distinguish the two composite adjunctions, not two consecutive stages. The identity is exactly (B.HS6), since its terminal \(c_m\) is the identity. The left comparison is the actual pasted resolved cell, and \(b\) is its full retained witness, not a product of unresolved right mates. Balanced-tensor associators are those already used in (B.HS4). No invertibility of \(\vartheta\) or its mate is assumed.

Use the fixed other replacements and maps of (B.RJ1)--(B.RJ6) in the same whole category. Let \(\Theta\) be the homogeneous comparison complex of B.1ak. Define the mate complex
\[
\begin{aligned}
\mathscr M^n&=\{(\vartheta,c,b):
 |\vartheta|=|c|=n,\ |b|=n-1\},\\
\partial_{\mathscr M}(\vartheta,c,b)
 &=\bigl(d\vartheta,dc,q_1c-\Psi_N(\vartheta)-db\bigr),\\
\mathscr B&=\widetilde{\mathscr U}\times_{\Theta}\mathscr M .
\end{aligned}
\tag{B.HC2}
\]
The sources of \(c,b\) are \(SQ_0\), and their targets are \(Q_1,U_1VN\), respectively. Since \(\Psi_N\) is a chain map, \(\partial_{\mathscr M}^2=0\). The fibre product requires equality of the **actual** \(\vartheta\) coordinates. It does not merely match their cohomology classes.

The map from (B.RC6) is
\[
\begin{aligned}
\pi_{\mathscr B}:\mathscr F&\longrightarrow\mathscr B,\\
(e,j_U,j_F,j_C,j_\beta)
 &\longmapsto
 \bigl((\vartheta,c_M,b_M,v,h_v,j_U),(\vartheta,c,b)\bigr).
\end{aligned}
\tag{B.HC3}
\]
It is a degreewise surjective chain map: the differential of these retained coordinates does not involve \(a,h_a,j_F,j_C,j_\beta\). Its kernel has the three omitted face cones
\(\mathcal C_F[-1]\oplus\mathcal C_C[-1]\oplus\mathcal C_\beta[-1]\)
as a subcomplex. The quotient is the full cone of
\(\operatorname{Hom}(A,\rho_1)\), in coordinates \(a,h_a\); its differential is \((da,\rho_1a-dh_a)\) because \(c=0\) in the kernel. These four cones are acyclic by the whole h-projectivity hypotheses of (B.RC2) and of \(A\). This finite filtration proves that \(\ker\pi_{\mathscr B}\) is acyclic. In particular one need not discard \(c,b\) in order to retain the old unit cube.

**Supply the common cube boundary before lifting it.** Retain the actual left cube
\(d\vartheta_H=\vartheta_T-\vartheta_B\) from (B.MX13), the complete unit cell \(u_H\) of (B.RC11), and closed horizontal endpoint triples \(m_T,m_B\) from (B.HC1). Their \(\vartheta\) coordinates must be those of the retained unit endpoints. The pair
\[
 \bigl(c_T-c_B,\ b_T-b_B+\Psi_N(\vartheta_H)\bigr)
 \in\mathcal C_{q_1}(SQ_0)^0
 \tag{B.HC4}
\]
is closed: differentiation of its second entry is \(q_1(c_T-c_B)\), by the two mate equations and the displayed differential of \(\vartheta_H\). Acyclicity gives a full primitive \((c_H,b_H)\), of degrees \(-1,-2\). Thus
\[
\begin{aligned}
dc_H&=c_T-c_B,\\
q_1c_H-\Psi_N(\vartheta_H)-db_H&=b_T-b_B,\\
\pi_{\mathscr B}(f_H)&=(u_H,(\vartheta_H,c_H,b_H)),\\
\partial_{\mathscr F}f_H&=f_T-f_B .
\end{aligned}
\tag{B.HC5}
\]
For the last two lines retain any already fixed endpoint lifts \(f_T,f_B\). Take a graded lift of the third line. Its differential minus \(f_T-f_B\) is a cycle in \(\ker\pi_{\mathscr B}\); subtract a primitive in that kernel. This proves the relative assertion and preserves both the full unit-cube face and the horizontal mate cube. If \(c_H,b_H\) were already fixed with the required equations, use them unchanged.

If an older horizontal mate lift for the same \(\vartheta\) differs from (B.HC1), add a bridge with \(\vartheta_H=0\) and the two actual lifts as endpoints. Their full difference is closed in the same cone, so (B.HC4)--(B.HC5) apply. The old records are not overwritten. Likewise, changing unit or counit inputs first requires their full comparison from B.1aj--B.1ak; the following change of triangles assumes those inputs fixed.

**Transport the corrected sequential triangle, including its second witness.** At each of the two columns keep \(q_i,u_i,z_i,\ell_i,H_i\). Let \((J_i,K_i)\) be an old triangle and let \((J_i^+,K_i^+)\) be the corrected folded triangle of (B.NT7)--(B.NT8), or another fixed whole triangle for exactly these inputs. By (B.NT11), choose and retain
\[
\begin{aligned}
J_i^+-J_i&=dP_i,& |P_i|&=-2,\\
K_i^+-K_i&=q_iP_i-dW_i,& |W_i|&=-3 .
\end{aligned}
\tag{B.HC6}
\]
Write \(\Omega,\Omega^+\) for (B.RC7)--(B.RC10) using the old and new triangles. The complex \(\mathscr F\) does not change: none of its differential or four-face maps uses \(J_i,K_i\).

Set
\[
\begin{aligned}
Z_0&=\operatorname{Adj}_0^{-1}(W_0),\\
\sigma(\vartheta)&=\operatorname{Adj}_1(VZ_0\vartheta_{Q_0}),\\
d\sigma(\vartheta)+\sigma(d\vartheta)
 &=\operatorname{Adj}_1(V(dZ_0)\vartheta_{Q_0}).
\end{aligned}
\tag{B.HC7}
\]
Here \(|Z_0|=-3\) and, if \(|\vartheta|=n\), \(|\sigma(\vartheta)|=n-3\). The plus sign in the last line follows from the odd degree of \(Z_0\). The formula uses the full Hom-complex adjunction, not its degree-zero restriction.

For \(f\in\mathscr F^n\), with coordinates \(c,b,\vartheta\), define a degree-minus-two map into \(\mathcal C_N\) by
\[
\begin{aligned}
\Lambda(f)&=(X(f),Y(f)),\\
X(f)&=cSP_0-P_1c,\\
Y(f)&=bSP_0+\sigma(\vartheta)-W_1c .
\end{aligned}
\tag{B.HC8}
\]
The degrees of \(X,Y\) are \(n-2,n-3\). This uses both witnesses \(P_i,W_i\); omitting the transposed \(W_0\) term is not justified.

We claim
\[
 \Omega^+-\Omega
   =\delta\Lambda-\Lambda\partial_{\mathscr F}.
 \tag{B.HC9}
\]
For the first coordinate, (B.RC7) gives
\(\Delta\mathcal R=(-1)^ncS(dP_0)-(dP_1)c\).
This equals \(dX-X(\partial f)\) by the Leibniz rule, since \(P_i\) has even degree. For the second coordinate, the only changed terms of (B.RC8) are \(\xi,(-1)^nbSJ_0,-K_1c\). Transposing (B.HC6) gives
\(\Gamma_0^+-\Gamma_0=e_0L_0P_0-dZ_0\).
Naturality of \(\vartheta\) on the degree-minus-two \(P_0\) has no extra sign. Hence
\[
\begin{aligned}
\Delta\xi(\vartheta)
 &=\Psi_N(\vartheta)SP_0-d\sigma(\vartheta)-\sigma(d\vartheta),\\
\Delta\mathcal V(f)
 &=\Delta\xi(\vartheta)+(-1)^nbS(dP_0)
          -q_1P_1c+(dW_1)c,\\
q_1X(f)-dY(f)-Y(\partial f)&=\Delta\mathcal V(f).
\end{aligned}
\tag{B.HC10}
\]
For the last equality insert \(b'=q_1c-\Psi_N(\vartheta)-db\).
The terms \(dc\,SP_0,P_1dc\) cancel in the first coordinate.
In the second use
\(d(bSP_0)=db\,SP_0-(-1)^nbS(dP_0)\) and
\(d(W_1c)=dW_1c-W_1dc\);
the \(W_1dc\) terms cancel against \(Y(\partial f)\).
The remaining terms are exactly the middle line. This proves (B.HC9) in every homogeneous degree, including the nonclosed cube input.

Let \(\mathscr G,\mathscr G^+\) be the twice-shifted extensions of (B.RC10) for \(\Omega,\Omega^+\). Then
\[
\begin{aligned}
\mathcal T:\mathscr G&\longrightarrow\mathscr G^+,&
\mathcal T(f,p)&=(f,p+\Lambda(f)),\\
\mathcal T^{-1}(f,p)&=(f,p-\Lambda(f)),&
\partial_{\mathscr G^+}\mathcal T
 &=\mathcal T\partial_{\mathscr G}.
\end{aligned}
\tag{B.HC11}
\]
Indeed the second coordinate on the left is
\(\delta p+\delta\Lambda(f)-\Omega^+(f)
 =\delta p-\Omega(f)+\Lambda(\partial f)\), by (B.HC9).
Thus this is an actual triangular chain isomorphism over the unchanged \(\mathscr F\), not only an agreement of classes.
For successive specified transitions on the same fixed inputs, take \(P_i^{02}=P_i^{01}+P_i^{12}\) and \(W_i^{02}=W_i^{01}+W_i^{12}\). Formula (B.HC8) is linear in these transition records, so \(\mathcal T_{02}=\mathcal T_{12}\mathcal T_{01}\) exactly. This assertion uses the stated additive records; it does not identify separately chosen transition primitives without another comparison.

In particular, for a retained cube
\(\partial_{\mathscr G}(f_H,p_H)=(f_T,p_T)-(f_B,p_B)\), put
\[
\begin{aligned}
p_T^+&=p_T+\Lambda(f_T),&
p_B^+&=p_B+\Lambda(f_B),\\
p_H^+&=p_H+\Lambda(f_H),\\
\delta p_H^+
 &=p_T^+-p_B^++\Omega^+(f_H).
\end{aligned}
\tag{B.HC12}
\]
The two entries of \(\Lambda(f_H)\) have degrees \(-3,-4\), so this transports the original last cube witness as well as its first homotopy. The unit-cube element, the two horizontal mate witnesses and all four-face records \(f_T,f_B,f_H\) remain unchanged. Keep the old comparison and this explicit transition in the record; do not silently relabel its old \(p\) as the new one.

The retained data and the change of triangles fit into
\[
\begin{array}{ccc}
 \mathscr G&\xrightarrow{\ \mathcal T\ }&\mathscr G^+\\
 {\scriptstyle\mathrm{retain}\ (u,m)}\downarrow&&
 \downarrow{\scriptstyle\mathrm{retain}\ (u,m)}\\
 \mathscr B&\xrightarrow{\ 1\ }&\mathscr B .
\end{array}
\tag{B.HC13}
\]
This diagram displays an actual chain isomorphism over the common target retaining both the unit and mate records. The vertical maps forget the other faces and triangle comparisons, not the specified unit or mate data.

For a fixed master string, (B.HS7) gives identical \(c,b\) under every cut and (B.NT7)--(B.NT8), with (B.RS9)--(B.RS10), gives identical corrected \(J_i^+,K_i^+\). Retain one whole choice of \(P_i,W_i\) for these endpoint records rather than rechoose it at each cut. Equations (B.HC7)--(B.HC12) are then identical under every parenthesization. In particular the original \(W_2\) contained in \(K_i^+\) remains present. The higher folding coefficients on longer parameter words have not been set to zero.

This supplies the shared **linear** target and the actual horizontal/unit/triangle overlap maps for every supplied common model and cube with these boundaries. It does not make \(\mathscr B,\mathscr F,\mathscr G\) into a multiplicative presentation or assert that all geometric higher faces have already been supplied. Their composition maps and higher overlap boundaries must still be constructed and checked using the original graph/bar roof. Geometric multiplicative descent, whole coefficient-system transport and strict-heart effacement are not established by this construction. \(\square\)



### Encode all four faces in one arrow graph

**Proposition B.1ao (typed four-face paths and their full graph witnesses).** The complete comparison of B.1ak--B.1an has an explicit representation in one dg category of arrows. It retains the two intermediate replacements \(A,C\), all four cone faces, the actual horizontal-mate witness, and the last degree-minus-four cube coordinate. No right mate is evaluated on an unresolved restriction module. The distinction between the unit and counit versions of an endpoint is essential: their comparison is the already prescribed transpose \(\beta\), not an identity imposed on the target. We also give the actual composition law for graph-valued triangle comparisons. These constructions supply a typed common-model boundary presentation; the final changing-geometric-model assembly remains a separate obligation.

**The arrow category does not require its objects to be quasi-isomorphisms.** For any unital dg category \(\mathscr D\), let \(\operatorname{Ar}(\mathscr D)\) have objects \(a:X\to N\) closed of degree zero. A degree-\(n\) map from \(a_0\) to \(a_1\) is \((c,v,b)\), with \(c:X_0\to X_1\), \(v:N_0\to N_1\) of degree \(n\), and \(b:X_0\to N_1\) of degree \(n-1\). Put
\[
\begin{aligned}
d_{\rm ar}(c,v,b)&=(dc,dv,a_1c-va_0-db),\\
(c_s,v_s,b_s)(c_t,v_t,b_t)
 &=\bigl(c_sc_t,v_sv_t,b_sc_t+(-1)^{|s|}v_sb_t\bigr).
\end{aligned}
\tag{B.FG1}
\]
These are the graph formulas (B.RG2)--(B.RG3). Expanding the third component proves \(d_{\rm ar}^2=0\), the graded Leibniz rule and strict associativity; the unit is \((1,1,0)\). The two product terms yield the same ordered terms under either bracketing, with the sign \((-1)^{|r|+|s|}\) on the last one. Only \(da_i=0\) is used. The earlier quasi-isomorphism hypotheses belong to the projection assertions, not to these dg axioms. Thus the following unit arrows are legitimate objects even when they are not quasi-isomorphisms.

Use the whole diagram category on the \(U_1\) side of (B.RJ1)--(B.RJ5). Write \(X=L_1SQ_0\), and retain the following **seven** graph objects:
\[
\begin{aligned}
\mathsf Q_0^u&=(SQ_0\xrightarrow{\eta^1}U_1L_1SQ_0),&
\mathsf R_0^u&=(SR_0\xrightarrow{\eta^1}U_1L_1SR_0),\\
\mathsf A&=(A\xrightarrow{r_A}U_1X),&
\mathsf C&=(C\xrightarrow{r_C}U_1VM_0),\\
\mathsf Q_1^u&=(Q_1\xrightarrow{\eta^1}U_1M_1),&
\mathsf R_1&=(R_1\xrightarrow{\rho_1}U_1M_1),\\
\mathsf Q_1^q&=(Q_1\xrightarrow{q_1}U_1VN).
\end{aligned}
\tag{B.FG2}
\]
The two objects with underlying \(Q_1\) are not identified. Every unit is evaluated on the displayed resolved input. All the maps below belong to the same whole Hom complexes; the graph argument does not replace whole h-projectivity by pointwise h-projectivity.

The fixed graph arrows, written as their three components, are
\[
\begin{aligned}
\mathbf s_u&=(Su_0,U_1L_1Su_0,0),&
\mathbf s_z&=(Sz_0,U_1L_1Sz_0,0),\\
\mathbf u_X&=(u_X,1,\ell_X),&
\mathbf u_1&=(u_1,1,\ell_1),\\
\mathbf z_1&=(z_1,U_1e_1,H_1),&
\mathbf e_1&=(1,U_1e_1,0),\\
\mathbf w&=(w,U_1(Ve_0),h_w).
\end{aligned}
\tag{B.FG3}
\]
Their types are, in order, \(\mathsf Q_0^u\to\mathsf R_0^u\), the reverse, \(\mathsf Q_0^u\to\mathsf A\), \(\mathsf Q_1^u\to\mathsf R_1\), \(\mathsf R_1\to\mathsf Q_1^q\), \(\mathsf Q_1^u\to\mathsf Q_1^q\), and \(\mathsf C\to\mathsf Q_1^q\). They are closed by unit naturality, (B.RJ2), (B.RJ5), and \(q_1=U_1(e_1)\eta^1_{Q_1}\). The two retained triangle arrows are
\[
\begin{aligned}
\mathbf J_0&=(SJ_0,U_1L_1SJ_0,0),&
d_{\rm ar}\mathbf J_0&=\mathbf s_z\mathbf s_u-1,\\
\mathbf J_1&=(J_1,0,K_1),&
d_{\rm ar}\mathbf J_1&=\mathbf z_1\mathbf u_1-\mathbf e_1.
\end{aligned}
\tag{B.FG4}
\]
Both have degree \(-1\). In particular \(K_1\) is present in the actual arrow, and the second equation has \(\mathbf e_1\), not an identity between distinct graph objects.

**Encode a homogeneous RC record before taking its boundary.** For \(e\in\mathscr E^n\) from (B.RC1), put
\[
\begin{aligned}
\mathbf c_L(e)&=(c,U_1L_1c,0),\\
\mathbf c_R(e)&=(c,U_1(Ve_0\vartheta_{Q_0}),b),\\
\mathbf c_M(e)&=(c_M,U_1(Ve_0^M\vartheta_{R_0}),b_M),\\
\mathbf v(e)&=(v,U_1\vartheta_{Q_0},h_v),\\
\mathbf a(e)&=(a,U_1L_1c,h_a).
\end{aligned}
\tag{B.FG5}
\]
Their types are respectively \(\mathsf Q_0^u\to\mathsf Q_1^u\), \(\mathsf Q_0^u\to\mathsf Q_1^q\), \(\mathsf R_0^u\to\mathsf C\), \(\mathsf A\to\mathsf C\), and \(\mathsf A\to\mathsf R_1\). Each assignment commutes with differential. For example its third coordinate for \(\mathbf c_R\) is precisely \(q_1c-\operatorname{Adj}_1(Ve_0\vartheta_{Q_0})-db\), since the second coordinate is composed with the source unit. The comparison \(\vartheta\) is evaluated at \(Q_0\), never at \(U_0N\).

Let \(\beta(e)=\operatorname{Adj}_1^{-1}b\). The graph arrow
\[
\begin{aligned}
\mathbf b(e)&=(0,U_1\beta(e),0):
  \mathsf Q_0^u\longrightarrow\mathsf Q_1^q,\\
|\mathbf b(e)|&=n-1,\\
d_{\rm ar}\mathbf b(e)+\mathbf b(\partial_{\mathscr E}e)
 &=\mathbf e_1\mathbf c_L(e)-\mathbf c_R(e)
\end{aligned}
\tag{B.FG6}
\]
is the required bridge. Indeed \(d\beta=e_1L_1c-Ve_0\vartheta-\beta(\partial e)\); its unit transpose is \(U_1\beta\,\eta^1_{SQ_0}=b\). Thus the last coordinate on both sides of (B.FG6) is \(-b\). Declaring \(\mathbf e_1\mathbf c_L=\mathbf c_R\) would discard this prescribed homotopy.

For \(f=(e,j_U,j_F,j_C,j_\beta)\in\mathscr F^n\), write the component pairs as in (B.RC6), and define degree-\(n-1\) graph arrows
\[
\begin{aligned}
\mathbf j_U(f)&=(J_U,U_1(V\lambda_0\vartheta_{Q_0}),K_U),\\
\mathbf j_F(f)&=(J_F,0,K_F),\\
\mathbf j_C(f)&=(J_C,U_1(V\alpha_0\vartheta_{R_0}),K_C),\\
\mathbf j_\beta(f)&=(t,U_1\beta(e),k).
\end{aligned}
\tag{B.FG7}
\]
Their sources and targets are respectively \((\mathsf Q_0^u,\mathsf C)\), \((\mathsf Q_0^u,\mathsf R_1)\), \((\mathsf R_0^u,\mathsf Q_1^q)\), and \((\mathsf A,\mathsf Q_1^q)\). All four identities hold in every degree:
\[
\begin{aligned}
d_{\rm ar}\mathbf j_U(f)+\mathbf j_U(\partial f)
 &=\mathbf c_M(e)\mathbf s_u-\mathbf v(e)\mathbf u_X,\\
d_{\rm ar}\mathbf j_F(f)+\mathbf j_F(\partial f)
 &=\mathbf u_1\mathbf c_L(e)-\mathbf a(e)\mathbf u_X,\\
d_{\rm ar}\mathbf j_C(f)+\mathbf j_C(\partial f)
 &=\mathbf c_R(e)\mathbf s_z-\mathbf w\mathbf c_M(e),\\
d_{\rm ar}\mathbf j_\beta(f)+\mathbf j_\beta(\partial f)
 &=\mathbf z_1\mathbf a(e)-\mathbf w\mathbf v(e).
\end{aligned}
\tag{B.FG8}
\]
Here \(\partial=\partial_{\mathscr F}\). To check the first identity, its first coordinate is \(D_U\). Its second is \(U_1(V(d\lambda_0)\vartheta)\), because the degree of \(\lambda_0\) is \(-1\), so the differentiated-\(\vartheta\) terms cancel. The last coordinate is \(I_U-\upsilon\), namely
\(b_MSu_0-h_vu_X-(-1)^nU_1(\vartheta_{Q_0})\ell_X\), exactly the difference of the graph products. The third identity is the same computation with \(\alpha_0,\chi\), giving \(I_C-\chi\). The second uses the zero middle coordinate and gives exactly \(I_F\). For the fourth, the second coordinate follows from the displayed differential of \(\beta\); the last is \(I_\beta-U_1\beta r_A\), which is the difference of the last coordinates of \(\mathbf z_1\mathbf a\) and \(\mathbf w\mathbf v\). These are componentwise proofs of (B.FG8), not just equalities after applying a projection.

**Paste the actual four faces.** In the single arrow category, set
\[
\begin{aligned}
\mathbf B(f)&=\mathbf j_C(f)\mathbf s_u+\mathbf w\mathbf j_U(f)
 -\mathbf j_\beta(f)\mathbf u_X-\mathbf z_1\mathbf j_F(f),\\
d_{\rm ar}\mathbf B(f)+\mathbf B(\partial f)
 &=\mathbf c_R(e)\mathbf s_z\mathbf s_u
      -\mathbf z_1\mathbf u_1\mathbf c_L(e).
\end{aligned}
\tag{B.FG9}
\]
The interior paths through \(\mathsf A,\mathsf C,\mathsf R_1\) cancel in order by (B.FG8). The first coordinate is exactly \(\mathcal B\) of (B.RC7). The last is exactly \(\mathcal T\) of (B.RC8): in particular the third component of
\(-\mathbf j_\beta\mathbf u_X\) is \(-ku_X+(-1)^nU_1\beta\,\ell_X\). Thus its sign and both product terms \(h_wJ_U,H_1J_F\) have not been discarded.

Correct the resulting triangle discrepancy by the bridge (B.FG6):
\[
\begin{aligned}
\widehat{\mathbf R}(f)
 &=(-1)^n\mathbf c_R(e)\mathbf J_0-\mathbf J_1\mathbf c_L(e)
       -\mathbf B(f)-\mathbf b(e),\\
d_{\rm ar}\widehat{\mathbf R}(f)
       +\widehat{\mathbf R}(\partial f)&=0 .
\end{aligned}
\tag{B.FG10}
\]
For the second line use the graded Leibniz rule, (B.FG4), (B.FG9), and (B.FG6). The four uncancelled terms before subtracting \(\mathbf b\) are exactly \(\mathbf e_1\mathbf c_L-\mathbf c_R\). This also explains why that subtraction cannot be omitted, even when the first-coordinate path diagram already commutes up to homotopy.

Let
\(\gamma(f)=U_1(V\Gamma_0\vartheta_{Q_0})\), of degree \(n-2\), where \(\Gamma_0=\operatorname{Adj}_0^{-1}K_0\) is the retained second triangle witness. Its unit transpose is \(\xi(e)\). A componentwise expansion gives
\[
\begin{aligned}
\widehat{\mathbf R}(f)
 &=\bigl(\mathcal R(f),\,
       d\gamma(f)-\gamma(\partial f),\,
       \mathcal V(f)-\xi(e)\bigr).
\end{aligned}
\tag{B.FG11}
\]
The first and last coordinates follow from (B.RC7)--(B.RC8). For the middle coordinate, move \(\vartheta\) past \(J_0\); its sign \((-1)^n\) cancels the displayed sign in (B.FG10). The \(\beta\) terms from \(\mathbf B\) and \(\mathbf b\) cancel. What remains is \(U_1(V(e_0L_0J_0-\alpha_0L_0u_0-e_0\lambda_0)\vartheta)=U_1(V(d\Gamma_0)\vartheta)\), by (B.RJ3). Since \(|\Gamma_0|=-2\), this is \(d\gamma(f)-\gamma(\partial f)\). This calculation uses the complete \(K_0\), including the \(W_2\) correction of (B.NT7).

For \(g=(f,p)\in\mathscr G^n\), with \(p=(P,W)\) from (B.RC10), define
\[
\begin{aligned}
\mathbf P(g)&=(P,\gamma(f),W):
       \mathsf Q_0^u\longrightarrow\mathsf Q_1^q,
       &|\mathbf P(g)|&=n-2,\\
d_{\rm ar}\mathbf P(g)-\mathbf P(\partial_{\mathscr G}g)
       &=\widehat{\mathbf R}(f),\\
d_{\rm ar}\mathbf P(g_H)
       &=\mathbf P(g_T)-\mathbf P(g_B)+\widehat{\mathbf R}(f_H)
       &&\text{if }\partial_{\mathscr G}g_H=g_T-g_B .
\end{aligned}
\tag{B.FG12}
\]
The last coordinate of the second line is
\((q_1P-\xi-dW)-(q_1P-dW-\mathcal V)=\mathcal V-\xi\); the other two are (B.FG11). In the cube line \(\mathbf P(g_H)\) has graph degree \(-3\), hence its last coordinate \(W_H\) has degree \(-4\). Nothing in this encoding removes it.

The endpoints and the four routes now have the following typed form:
\[
\begin{array}{ccccc}
\mathsf Q_0^u&\xrightarrow{\mathbf s_u}&\mathsf R_0^u
 &\xrightarrow{\mathbf s_z}&\mathsf Q_0^u\xrightarrow{\mathbf c_R}\mathsf Q_1^q\\
\mathsf Q_0^u&\xrightarrow{\mathbf s_u}&\mathsf R_0^u
 &\xrightarrow{\mathbf c_M}&\mathsf C\xrightarrow{\mathbf w}\mathsf Q_1^q\\
\mathsf Q_0^u&\xrightarrow{\mathbf u_X}&\mathsf A
 &\xrightarrow{\mathbf v}&\mathsf C\xrightarrow{\mathbf w}\mathsf Q_1^q\\
\mathsf Q_0^u&\xrightarrow{\mathbf u_X}&\mathsf A
 &\xrightarrow{\mathbf a}&\mathsf R_1\xrightarrow{\mathbf z_1}\mathsf Q_1^q\\
\mathsf Q_0^u&\xrightarrow{\mathbf c_L}&\mathsf Q_1^u
 &\xrightarrow{\mathbf u_1}&\mathsf R_1\xrightarrow{\mathbf z_1}\mathsf Q_1^q .
\end{array}
\tag{B.FG13}
\]
The adjacent differences have the witnesses in (B.FG9); closing the shortened endpoints additionally uses \(\mathbf b\). This is a diagram of homogeneous paths and their specified boundaries, not a claim that every displayed arrow is closed for a nonclosed input \(f\).

Retain \(\vartheta\) itself with these records. Then every old coordinate is recoverable without inverses: \(c,b\) from \(\mathbf c_R\), \(c_M,b_M\) from \(\mathbf c_M\), \(v,h_v,a,h_a\) from \(\mathbf v,\mathbf a\), all four first/second face pairs from \(\mathbf j_\nu\), and \(P,W\) from \(\mathbf P\). Hence the original unit cube and actual horizontal mate remain recorded; the construction is not a replacement by a smaller comparison with the same endpoints.

**Composition really needs a cross term.** The following algebraic construction may be used in the arrow category just defined. For any dg category \(\mathscr D\), take triangle objects \((X,Y,u,z,J)\) with \(du=dz=0\) and \(dJ=zu-1_X\). A degree-\(n\) comparison is \((c,r,h,k,p)\), with types \(X_0\to X_1,Y_0\to Y_1,X_0\to Y_1,Y_0\to X_1,X_0\to X_1\) and degrees \(n,n,n-1,n-1,n-2\). Define
\[
\begin{aligned}
R(f)&=(-1)^ncJ_0-J_1c-ku_0-z_1h,\\
Df&=(dc,dr,ru_0-u_1c-dh,\,
                  cz_0-z_1r-dk,\,dp-R(f)).
\end{aligned}
\tag{B.FG14}
\]
Expansion gives \(dR(f)+R(Df)=0\), so \(D^2=0\). For homogeneous \(s,t\), with \(|s|=m\), the actual composition is
\[
\begin{aligned}
(st)_c&=c_sc_t,&(st)_r&=r_sr_t,\\
(st)_h&=h_sc_t+(-1)^m r_sh_t,&
(st)_k&=k_sr_t+(-1)^m c_sk_t,\\
(st)_p&=c_sp_t+p_sc_t+(-1)^m k_sh_t.
\end{aligned}
\tag{B.FG15}
\]
Here all products are those of \(\mathscr D\). To verify the last Leibniz coordinate, put \(\Delta_u(t)=r_tu_0-u_1c_t\), \(\Delta_z(s)=c_sz_1-z_2r_s\). Then
\(R(st)-R(s)c_t-(-1)^mc_sR(t)=(-1)^m\Delta_z(s)h_t-k_s\Delta_u(t)\).
The derivative of the last term in (B.FG15) is
\((-1)^m(dk_s)h_t-k_s(dh_t)\). Substituting
\(dk_s=\Delta_z(s)-k_{Ds}\), \(dh_t=\Delta_u(t)-h_{Dt}\) gives exactly the required two remaining Leibniz terms. The other coordinates are the graph calculation (B.FG1).

Strict associativity follows by expanding both bracketings. If \(|r|=l\), their last coordinates are the same six terms:
\(c_rc_sp_t+c_rp_sc_t+p_rc_sc_t
+(-1)^mc_rk_sh_t+(-1)^lk_rh_sc_t+(-1)^{l+m}k_rr_sh_t\).
The unit \((1,1,0,0,0)\) is closed and two-sided. Thus this is a dg category in all degrees.

For a small integral check of necessity, take a free complex with basis in degrees \(-1,0,1\), with \(d(e_{-1})=e_0\) and other differentials zero; put \(u=z=1,J=0\). Let \(h_s:e_0\mapsto e_{-1}\), \(h_t:e_1\mapsto e_0\), all other images zero. Set \(c_s=c_t=r_t=1\), \(r_s=\operatorname{diag}(2,2,1)\), \(k_s=-h_s,k_t=-h_t,p_s=p_t=0\). These are closed degree-zero comparisons: \(dh_s=r_s-1\), \(dh_t=0\), and their discrepancies vanish. Their composite has \(h=h_s+2h_t,k=-h_s-h_t,R=-h_t\). Its required \(p=-h_sh_t\) satisfies \(dp=-h_t\). Omitting this term leaves the nonzero last differential coordinate \(h_t\).

The higher product boundaries are also specified, not replaced by existence claims. For retained degree-minus-one \(f_H,g_H\) with boundaries \(f_T-f_B,g_T-g_B\), define
\[
\begin{aligned}
L&=g_Hf_T+g_Bf_H,&U&=g_Tf_H+g_Hf_B,\\
DL&=DU=g_Tf_T-g_Bf_B,&D(g_Hf_H)&=U-L,\\
D(h_r\cdots h_1)
 &=\sum_{i=1}^r(-1)^{r-i}h_r\cdots D(h_i)\cdots h_1
 &&(|h_i|=-1).
\end{aligned}
\tag{B.FG16}
\]
These follow from the proved Leibniz rule; strict associativity identifies their bracketings. They describe these actual products, not every as-yet-unspecified geometric higher cell.

To see why this construction retains both triangle witnesses, for each original endpoint take arrow objects
\((Q_i,U_iN_i,q_i)\) and \((R_i,U_iN_i,U_i(e_i)\rho_i)\). In their arrow category the unit, counit and triangle are
\((u_i,1,U_i(e_i)\ell_i)\), \((z_i,1,H_i)\), and \((J_i,0,K_i)\). Equation (B.RJ2) says exactly that the third is a triangle between the product of the first two and the identity. Its \(K_i\) is not erased; nor is \(U_i(e_i)\rho_i\) asserted to be a quasi-isomorphism. A degree-minus-one comparison in this triangle category again has a degree-minus-four last graph coordinate.

For fixed \(u,z\), a specified change \(J_i^+=J_i+d\Pi_i\), \(|\Pi_i|=-2\), gives a strict dg isomorphism
\[
\begin{aligned}
T(f)&=(c,r,h,k,p+c\Pi_0-\Pi_1c),\\
T(st)&=T(s)T(t),&
D^+T&=TD .
\end{aligned}
\tag{B.FG17}
\]
The chain identity is the Leibniz rule; multiplicativity is the literal cancellation of \(c_s\Pi_1c_t\). The cross term is unchanged. In the arrow category choose \(\Pi_i=(P_i,0,W_i)\), so its differential is \((dP_i,0,q_iP_i-dW_i)\), retaining both entries of (B.HC6). The inverse subtracts the displayed correction. Successive specified additive transition records compose exactly. A change in unit or counit inputs is not covered by this assertion.

**Fixed-model and varying-model comparisons.** Equations (B.FG2)--(B.FG13) give the typed graph representation of the entire fixed-common-model four-face and cube record, including \(\beta,\Gamma_0\) and all original higher witnesses. Equations (B.FG14)--(B.FG17) supply an actual multiplicative triangle target and its product boundaries. The four-face record has distinct intermediate objects and a nontrivial endpoint bridge; it has not silently been identified with one direct middle map \(r\) in (B.FG14). Pasting between changing adjunction/compactification models must still be represented by actual maps between these diagrams, with the full original bar folding coefficients and their geometric overlap boundaries. Strict associativity of formal graph paths does not alone prove that assembly. Nearby-cycle multiplicative descent, whole coefficient transport and strict-heart effacement are not established by this construction. \(\square\)



### Transport the whole four-face diagram through a proper refinement

**Proposition B.1ap (actual right-refinement transport, with its target labels).** Use the complete data of B.1ak--B.1ao over the original commutative coefficient ring. Let \(G:\mathcal C_1\to\mathcal C'_1\) be an actual proper-refinement dg quasi-equivalence of B.1m, and write \(R=G_!\). Keep the left adjunction, the target module category, \(V\), and \(N\) fixed. Write \(L'_1\dashv U'_1\) for the new right-side adjunction. The maps (B.CR7)--(B.CR9), now denoted
\[
\begin{aligned}
c_P:L'_1RP&\xrightarrow{\sim}L_1P,&
\kappa_Z:RU_1Z&\longrightarrow U'_1Z,\\
\kappa_{L_1P}R\eta^1_P&=U'_1(c_P)\eta'^1_{RP},&
\epsilon'^1_ZL'_1\kappa_Z&=\epsilon^1_Zc_{U_1Z},
\end{aligned}
\tag{B.FT1}
\]
give an explicit transport of **all seven** objects and their entire four-face and mixed-cube record. Its new horizontal input is \(S'=RS\), and its comparison is \(\vartheta'_P=\vartheta_Pc_{SP}\). No intermediate object, endpoint bridge, or higher homotopy is discarded. Successive such refinements agree by a specified dg natural isomorphism satisfying the unit and pentagon identities. This is a construction for these actual induced replacement diagrams, not a claim that arbitrary separately chosen models or horizontal geometric pastings have already been compared.

**Keep the maps before restriction.** Define \(\mathcal A_U\) to have objects \((P,Z,q:P\to UZ)\), with \(q\) closed of degree zero. Retain \(Z\) itself, not just \(UZ\). A degree-\(n\) arrow is \((a,w,h)\), where \(a:P\to P'\), \(w:Z\to Z'\) have degree \(n\), and \(h:P\to UZ'\) has degree \(n-1\). Put
\[
\begin{aligned}
D(a,w,h)&=(da,dw,q'a-U(w)q-dh),\\
(a_s,w_s,h_s)(a_t,w_t,h_t)
 &=(a_sa_t,w_sw_t,h_sa_t+(-1)^{|s|}U(w_s)h_t).
\end{aligned}
\tag{B.FT2}
\]
The differential squares to zero by the dg functor identity for \(U\) and \(dq=dq'=0\). Expanding a product gives the Leibniz rule; expanding a triple product gives the same three terms in its last coordinate, with signs \(1,(-1)^{|r|},(-1)^{|r|+|s|}\). Units are \((1,1,0)\). Thus this is a dg category. Forgetting to \((a,U(w),h)\) is a dg functor to (B.FG1), but need not be faithful. Consequently an equality after applying \(U\) is not used as a proof of an equality of the retained \(w\)'s.

The seven decorated objects have the sources of (B.FG2), and actual target labels
\[
\begin{array}{c|ccccccc}
\text{object}&\mathsf Q_0^u&\mathsf R_0^u&\mathsf A&\mathsf C&\mathsf Q_1^u&\mathsf R_1&\mathsf Q_1^q\\
Z&L_1SQ_0&L_1SR_0&X&VM_0&M_1&M_1&VN
\end{array}
\tag{B.FT3}
\]
where \(X=L_1SQ_0\), \(M_i=L_iQ_i\). Every displayed \(U_1(w)\) in (B.FG3)--(B.FG7) is lifted to its displayed \(w\). In particular the targets of \(\mathbf c_L,\mathbf a\) use \(L_1c\), that of \(\mathbf c_R\) uses \(Ve_0\vartheta\), and the bridge uses \(\beta=\operatorname{Adj}_1^{-1}b\). For \(\mathbf J_1\) and \(\mathbf j_F\) the target component is zero. The lift of \(\mathbf P\) uses \(\bar\gamma=V\Gamma_0\vartheta_{Q_0}\), not merely its restriction.

Here is the check that these really satisfy the identities upstairs. The target components of the four face equations (B.FG8), for a degree-\(n\) record \(f\), are respectively
\[
\begin{aligned}
d(V\lambda_0\vartheta_{Q_0})+
 V\lambda_0\vartheta_{Q_0}(\partial f)
 &=Ve_0^M\vartheta_{R_0}L_1Su_0-\vartheta_{Q_0},\\
0&=L_1c-L_1c,\\
d(V\alpha_0\vartheta_{R_0})+
 V\alpha_0\vartheta_{R_0}(\partial f)
 &=Ve_0\vartheta_{Q_0}L_1Sz_0-Ve_0Ve_0^M\vartheta_{R_0},\\
d\beta(f)+\beta(\partial f)&=e_1L_1c-Ve_0\vartheta_{Q_0}.
\end{aligned}
\tag{B.FT4}
\]
In the first and third lines the notation with \(\partial f\) means evaluation of the corresponding linear assignment on that record. Their differentiated-\(\vartheta\) terms cancel because \(\lambda_0,\alpha_0\) have degree minus one. The remaining equations are (B.RJ3) and homogeneous naturality of \(\vartheta\); the last is the actual adjunction transpose of the defining differential of \(b\). The fixed unit arrows are checked by naturality before restriction. The target component of the corrected discrepancy is
\[
\begin{aligned}
\widehat{\mathbf R}(f)_Z
 &=V(e_0L_0J_0-\alpha_0L_0u_0-e_0\lambda_0)\vartheta_{Q_0}\\
 &=d\bar\gamma(f)-\bar\gamma(\partial f),
 &\bar\gamma(f)&=V\Gamma_0\vartheta_{Q_0}.
\end{aligned}
\tag{B.FT5}
\]
Indeed the \(\beta\) terms from \(-\mathbf B\) and \(-\mathbf b\) cancel; moving the degree-\(n\) comparison through \(J_0\) cancels the factor \((-1)^n\). Now use (B.RJ3). Since \(\Gamma_0\) has degree minus two, the last sign is a minus. The first and last coordinates are exactly the already proved RC equations. This proves the decorated lifts of (B.FG8)--(B.FG12) without assuming faithfulness of restriction. It retains the complete \(K_0\), including the correction in (B.NT7).

**The actual transport functor.** Before changing any target labels, set
\[
\begin{aligned}
T_G(P,Z,q)&=(RP,Z,\kappa_ZRq),\\
T_G(a,w,h)&=(Ra,w,\kappa_{Z'}Rh).
\end{aligned}
\tag{B.FT6}
\]
This is a strict unital dg functor \(\mathcal A_{U_1}\to\mathcal A_{U'_1}\). For the differential, closedness of \(\kappa\) and naturality for every homogeneous \(w\) give
\(U'_1(w)\kappa_Z=\kappa_{Z'}R(U_1w)\). Substitution into (B.FT2) gives precisely \(\kappa_{Z'}R(q'a-U_1(w)q-dh)\). For a product the two third-coordinate terms are \(\kappa Rh_sRa_t\) and \((-1)^{|s|}U'_1(w_s)\kappa Rh_t\); the same naturality makes them \(\kappa R(h_sa_t+(-1)^{|s|}U_1(w_s)h_t)\). Target components remain the actual \(w\)'s. No tensor factors are interchanged, so there is no additional sign.

Induction preserves whole h-projective modules by (B.DA4). If \(q:P\to U_1Z\) is a replacement with \(P\) whole h-projective, then \(\kappa_ZRq\) is a quasi-isomorphism. To see this, restriction along \(G\) and the induction unit give
\[
G^*(\kappa_ZRq)\eta^G_P=\chi_Zq,
\qquad \chi_Z:U_1Z\xrightarrow{\sim}G^*U'_1Z.
\tag{B.FT7}
\]
Here \(\chi\) is the actual map (B.CR6); the identity follows from (B.CR8) and naturality of the unit. The unit on \(P\) is a quasi-isomorphism by the whole-module semifree argument (B.SM1), and \(\chi_Zq\) is one. Thus the restricted map is one; detection in B.1s proves the assertion. This does **not** assume that ordinary induction preserves arbitrary quasi-isomorphisms, or that restriction preserves h-projectivity. Unit arrows themselves need not be quasi-isomorphisms. When whole diagram modules are used, this argument is made in that whole module category, with its actual quasi-equivalence; fibrewise projectivity alone is insufficient.

**Restore canonical unit labels, explicitly.** Put \(c_0=c_{SQ_0}\), \(c_R=c_{SR_0}\), \(c_1=c_{Q_1}\). The letter \(c_R\) here denotes this degree-zero induction isomorphism, not the bold comparison \(\mathbf c_R\). For the seven objects choose new targets \(Z'_i\) and isomorphisms \(\delta_i:Z'_i\to Z_i\):
\[
\begin{array}{c|ccccccc}
i&\mathsf Q_0^u&\mathsf R_0^u&\mathsf A&\mathsf C&\mathsf Q_1^u&\mathsf R_1&\mathsf Q_1^q\\
Z'_i&L'_1RSQ_0&L'_1RSR_0&L'_1RSQ_0&VM_0&L'_1RQ_1&L'_1RQ_1&VN\\
\delta_i&c_0&c_R&c_0&1&c_1&c_1&1
\end{array}
\tag{B.FT8}
\]
Replace each transported object by \(q'_i=U'_1(\delta_i^{-1})\kappa_{Z_i}Rq_i\). The closed graph isomorphism from this object to (B.FT6) is \((1,\delta_i,0)\), with inverse \((1,\delta_i^{-1},0)\). For the unit objects (B.FT1) says exactly \(q'_i=\eta'^1_{RP_i}\). Every arrow from object \(i\) to object \(j\), of any degree, becomes
\[
\overline T_G(a,w,h)=
 \bigl(Ra,\delta_j^{-1}w\delta_i,
       U'_1(\delta_j^{-1})\kappa_{Z_j}Rh\bigr).
\tag{B.FT9}
\]
This follows by composing the two graph isomorphisms, whose third coordinates vanish and whose degree is zero. It is a dg functor on this entire labelled diagram. Naturality of \(c\) gives \(c_1^{-1}L_1(c)c_0=L'_1R(c)\), as required for the new \(\mathbf c_L\) and \(\mathbf a\); it is not a guessed identification of their target maps.

For clarity, its replacement maps and endpoint counit are
\[
\begin{aligned}
q'_1&=\kappa_{VN}Rq_1,&e'_1&=e_1c_1,\\
r'_A&=U'_1(c_0^{-1})\kappa_XRr_A,&
\rho'_1&=U'_1(c_1^{-1})\kappa_{M_1}R\rho_1,\\
r'_C&=\kappa_{VM_0}Rr_C,&
\vartheta'_{Q_0}&=\vartheta_{Q_0}c_0.
\end{aligned}
\tag{B.FT10}
\]
The formula for \(e'_1\) follows from the counit identity in (B.FT1) and naturality of \(c\), so it really is \(\epsilon'^1_{VN}L'_1(q'_1)\). All seven source objects are induced by \(R\); the two copies of \(RQ_1\) remain distinct unit/counit graph objects. All first-coordinate arrows and homotopies are induced by \(R\). Each third coordinate is transformed by its **receiving** target in (B.FT9). Thus \(\ell_X\) receives the factor \(U'_1c_0^{-1}\); \(\ell_1,h_a,K_F\) receive \(U'_1c_1^{-1}\); \(b_M,h_v,K_U\) receive \(\kappa_{VM_0}R\); and \(b,H_1,K_1,h_w,K_C,k,W\) receive \(\kappa_{VN}R\). The left-side data are unchanged. This accounts for every original third coordinate, rather than just the closed arrows.

The two especially important target labels transform as
\[
\beta'=\beta c_0
   =\operatorname{Adj}'_1{}^{-1}(\kappa_{VN}Rb),
\qquad \bar\gamma'=\bar\gamma c_0.
\tag{B.FT11}
\]
To prove the transpose equality, compose \(U'_1(\beta c_0)\) with \(\eta'^1_{RSQ_0}\), use (B.FT1), then naturality of \(\kappa\), and finally \(U_1\beta\eta^1=b\). This gives \(\kappa_{VN}Rb\) in every homogeneous degree. The endpoint bridge therefore remains prescribed, not replaceable by zero. In particular the transported extension arrow is \((RP,\bar\gamma c_0,\kappa_{VN}RW)\). Applying the dg functor to the full cube gives
\[
D\overline T_G\mathbf P(g_H)=
 \overline T_G\mathbf P(g_T)-\overline T_G\mathbf P(g_B)
       +\overline T_G\widehat{\mathbf R}(f_H).
\tag{B.FT12}
\]
Its last coordinate still has degree minus four and is exactly \(\kappa_{VN}RW_H\). The actual horizontal-mate record of B.1an is transported together with its four face pairs; no new choice replaces it.

**Composition of refinements, not only composition of formal paths.** For composable proper refinements \(g,h\), let \(m:R_hR_g\xrightarrow{\sim}R_{hg}\) be their actual induction comparison. Flattening the tensors in their original order in (B.CR7)--(B.CR9), with the geometric comparison (B.CR4), gives
\[
\begin{aligned}
\kappa_hR_h(\kappa_g)&=\kappa_{hg}m_{U_1(-)},\\
c_{g,P}c_{h,R_gP}&=c_{hg,P}L''_1(m_P),\\
\mathfrak m_{(P,Z,q)}&=(m_P,1_Z,0):T_hT_g(P,Z,q)\to T_{hg}(P,Z,q).
\end{aligned}
\tag{B.FT13}
\]
The first line and naturality of \(m\) make the last triple closed. For an arbitrary homogeneous \((a,w,h_0)\), its first coordinate is naturality of \(m\), its second is the same \(w\), and its third is \(\kappa_{hg}R_{hg}(h_0)m_P=\kappa_hR_h(\kappa_gR_g(h_0))\). Hence \(\mathfrak m\) is an actual dg natural isomorphism on the whole decorated category. The inverse uses \(m_P^{-1}\) and has zero third coordinate. The tensor associators and geometric comparison satisfy the pentagon and units by B.1m; all three coordinates therefore do so here. After (B.FT8), the target component on the five changed-target objects is \(L''_1(m_P)\) for their corresponding source parameter, and on \(\mathsf C,\mathsf Q_1^q\) it is the identity. The second line of (B.FT13) checks this canonical-label comparison. It must not be replaced by an identity on unequal canonical unit targets.

**Retain all supplied bar coefficients.** A strict degree-zero dg functor induces a map on the suspended bar tensors by applying it to every arrow. With \(b_1(st)=-sDt\) and \(b_2(su\otimes st)=(-1)^{|u|}s(ut)\), (B.FT6) commutes with each elementary bar operation: it commutes with \(D\), preserves the ordered product, and does not change degrees. Thus it commutes with their sum in every length. Apply this to the decorated lifts of the supplied folding/overlap data, retaining the actual target-side labels as above. A higher coefficient with coordinates \((0,0,W_r)\) is sent to \((0,0,\kappa R W_r)\) before the target changes, and then by (B.FT9). It is not set to zero for \(r>1\). More generally a nonzero target coordinate is transported by (B.FT9), not inferred from its restriction. The zero-third-coordinate isomorphisms (B.FT8) telescope between adjacent factors exactly as in (B.SN11); no extra bar signs or omitted endpoint factors occur. The same identities retain each already supplied geometric overlap boundary and commute with (B.FT13). This assertion transports supplied decorated coefficients; it does not assert that an arbitrary unlabelled arrow-graph record has a lift through a nonfaithful restriction functor.

The following typed diagram displays the two stages for **each** of the seven rows of (B.FT3). The vertical arrows are the actual decorated morphisms; their target components remain visible. The right-hand isomorphisms are from canonical new targets to transported old targets:
\[
\begin{array}{ccccc}
(P_i,Z_i,q_i)&\xrightarrow{\ T_G\ }&(RP_i,Z_i,\kappa Rq_i)
 &\xleftarrow{\ (1,\delta_i,0)\ }&(RP_i,Z'_i,q'_i)\\
{\scriptstyle(a,w,h)}\downarrow&&{\scriptstyle(Ra,w,\kappa Rh)}\downarrow
 &&\downarrow{\scriptstyle\overline T_G(a,w,h)}\\
(P_j,Z_j,q_j)&\xrightarrow{\ T_G\ }&(RP_j,Z_j,\kappa Rq_j)
 &\xleftarrow{\ (1,\delta_j,0)\ }&(RP_j,Z'_j,q'_j).
\end{array}
\tag{B.FT14}
\]
The right square commutes by (B.FT9). This schematic applies to the seven distinct objects, their four faces, the bridge and the full cube; it does not identify objects sharing a source. Its reproducible source is the displayed array itself. The \(A,C\) replacements are retained wherever they occur in the original paths; no path is made to pass through an additional object.

This gives the **right-side proper-refinement** map on the full diagram, with comparison for successive refinements and all supplied higher coordinates. Simultaneous change of the left adjunction, comparison with independently chosen replacement diagrams, and the geometric horizontal-composition/base-change assembly remain to be constructed and checked. Geometric nearby-cycle multiplicative descent, whole coefficient transport and strict-heart effacement are not established by this construction. The fixed-model proposition does not establish the corresponding general geometric assertion. \(\square\)



### Join both refinements with the horizontal comparison

**Proposition B.1aq (the induced two-sided diagram).** Use the whole four-face data of B.1ak--B.1ao and the actual normalized induction presentations of (B.NR1)--(B.NR2). Both adjunction models may now change. The induced seven-object diagram, all its four faces and the full mixed-cube witness admit the simultaneous transport below. The horizontal induction comparison changes two source objects, and the left refinement also changes the target at \(C\). Neither change may be omitted. The statement applies over the original commutative coefficient ring to possibly unbounded whole h-projective sources. It does not identify independently chosen replacement diagrams, nor assert an unconstructed geometric overlap.

**Specify the actual square first.** Write \(E_i=G_{i!}\) for the two proper-refinement inductions, \(L_i'\dashv U_i'\) for the new adjunctions, and retain their balanced-tensor comparisons and actual mates:
\[
\begin{aligned}
a_{i,P}:L_i'E_iP&\xrightarrow{\sim}L_iP,&
\kappa_{i,Z}:E_iU_iZ&\longrightarrow U_i'Z,\\
\kappa_{i,L_iP}E_i\eta^i_P&=U_i'(a_{i,P})\eta'^i_{E_iP},&
\varepsilon'^i_ZL_i'\kappa_{i,Z}&=\varepsilon^i_Za_{i,U_iZ}.
\end{aligned}
\tag{B.BT1}
\]
Here \(i=0,1\), and the two final target categories, \(V\), and \(N\) are unchanged. These are (B.CR7)--(B.CR9), not inverses selected in a derived category. The horizontal comparison is a specified closed natural **isomorphism**
\[
\begin{aligned}
d_P:E_1SP&\xrightarrow{\sim}S'E_0P,\\
V(a_{0,P})\,\vartheta'_{E_0P}\,L_1'd_P
 &=\vartheta_P\,a_{1,SP}.
\end{aligned}
\tag{B.BT2}
\]
The second line is an equality of actual target-side maps, for every required homogeneous parameter coefficient. It cannot be deduced by applying a restriction functor and assuming that functor is faithful.

In the strict normalized horizontal square, (B.NR2)'s balanced induction isomorphism, in the required orientation, is \(d\): both sides induce along the same composite dg functor. Associativity sends a balanced tensor to the same flattened tensor, so it proves naturality, invertibility and compatibility with composition. If \(\vartheta\) is supplied as a map of the whole normalized transport diagram, (B.JF2)'s identification of whole induction with fibrewise induction gives exactly the second line of (B.BT2). Equivalently, at the induced objects it defines the transported coefficient by
\(\vartheta'_{E_0P}=V(a_{0,P})^{-1}\vartheta_Pa_{1,SP}(L_1'd_P)^{-1}\).
This formula does not extend a comparison to unrelated objects by fiat. The original geometric comparison is identified with it only through that supplied whole-diagram map. A horizontal geometric functor need not be a quasi-equivalence; \(d\) is an induction-composition isomorphism, not a claim that the geometric base-change map \(\vartheta\) or its right mate is invertible.

**Transport the left triangle before using it.** Put \(Q_0'=E_0Q_0\), \(R_0'=E_0R_0\), \(M_0'=L_0'Q_0'\), and abbreviate \(a=a_{0,Q_0}:M_0'\to M_0\), \(a_R=a_{0,R_0}\). The old right replacement, second replacement, and their witnesses give
\[
\begin{aligned}
q_0'&=\kappa_{0,N}E_0q_0,& e_0'&=e_0a,\\
\rho_0'&=U_0'(a^{-1})\kappa_{0,M_0}E_0\rho_0,&
e_0^{M\prime}&=a^{-1}e_0^M a_R,\\
u_0'&=E_0u_0,& z_0'&=E_0z_0,\\
\ell_0'&=U_0'(a^{-1})\kappa_{0,M_0}E_0\ell_0,&
H_0'&=\kappa_{0,N}E_0H_0,\\
J_0'&=E_0J_0,&K_0'&=\kappa_{0,N}E_0K_0.
\end{aligned}
\tag{B.BT3}
\]
The ordinary counit equations in (B.BT1) prove the two formulas for \(e_0'\) and \(e_0^{M\prime}\); the unit equation proves the formula involving \(\ell_0'\). Naturality of \(\kappa_0\) for the actual map \(e_0\) proves the equation involving \(H_0'\). Applying these operations to both equations of (B.RJ2) retains the old \(J_0,K_0\), rather than choosing fresh triangle witnesses. Adjointing the three witnesses gives
\[
\begin{aligned}
\lambda_0'&=a^{-1}\lambda_0a,&
\alpha_0'&=\alpha_0a_R,&\Gamma_0'&=\Gamma_0a,\\
d\lambda_0'&=e_0^{M\prime}L_0'u_0'-1_{M_0'},\\
d\alpha_0'&=e_0'L_0'z_0'-e_0'e_0^{M\prime},\\
e_0'L_0'J_0'&=\alpha_0'L_0'u_0'+e_0'\lambda_0'+d\Gamma_0'.
\end{aligned}
\tag{B.BT4}
\]
For example naturality gives \(a_RL_0'E_0u_0=L_0u_0a\); substituting this identity verifies the first and last differential equations directly. The analogous identity for \(z_0\) verifies the middle equation. Adjunction is an isomorphism of Hom complexes in every degree, so these calculations also apply to the homogeneous parameter coefficients used in the cube.

**Two source comparisons and six target comparisons.** For the right-side diagram set
\[
\begin{aligned}
X'&=L_1'S'E_0Q_0,&x&=a_{1,SQ_0}(L_1'd_{Q_0})^{-1}:X'\xrightarrow{\sim}X,\\
Y'&=L_1'S'E_0R_0,&y&=a_{1,SR_0}(L_1'd_{R_0})^{-1}:Y'\xrightarrow{\sim}L_1SR_0,\\
M_1'&=L_1'E_1Q_1,&b&=a_{1,Q_1}:M_1'\xrightarrow{\sim}M_1.
\end{aligned}
\tag{B.BT5}
\]
Use the following seven **labelled** objects. An entry \(\lambda_i\) is a map \(P_i'\to E_1P_i\), whereas \(\delta_i\) is a map \(Z_i'\to Z_i\). These have different roles and must not be interchanged.
\[
\begin{array}{c|c|c|c|c}
i&P_i'&Z_i'&\lambda_i&\delta_i\\\hline
Q_0^u&S'E_0Q_0&X'&d_{Q_0}^{-1}&x\\
R_0^u&S'E_0R_0&Y'&d_{R_0}^{-1}&y\\
A&E_1A&X'&1&x\\
C&E_1C&VM_0'&1&Va\\
Q_1^u&E_1Q_1&M_1'&1&b\\
R_1&E_1R_1&M_1'&1&b\\
Q_1^q&E_1Q_1&VN&1&1
\end{array}
\tag{B.BT6}
\]
With \(q_i:P_i\to U_1Z_i\) denoting the original object map, define
\[
q_i'=U_1'(\delta_i^{-1})\kappa_{1,Z_i}E_1q_i\,\lambda_i.
\tag{B.BT7}
\]
For \(Q_0^u,R_0^u,Q_1^u\) these are exactly the new ordinary units: substitute (B.BT1), then use naturality of \(\eta'^1\) for \(d^{-1}\). In particular, a unit has not been replaced by a quasi-isomorphism. For \(A,C,R_1,Q_1^q\), these are the transported old replacements. They are quasi-isomorphisms by the precise induction-unit/detection argument of (B.FT7), followed by the displayed isomorphisms. Induction preserves whole h-projectivity by the Hom adjunction. The first two new source objects are isomorphic to the corresponding induced old sources. Thus every required whole h-projective source remains such, without assuming that restriction preserves h-projectivity or that induction preserves arbitrary quasi-isomorphisms.

**One dg formula transports every face.** Keep the decorated arrow category \(\mathcal A_{U_1}\) of (B.FT2)--(B.FT4), whose second coordinate is the actual target map \(w:Z_i\to Z_j\), not only its restriction. On a homogeneous triple define
\[
\mathscr B(a_*,w,h)=
\left(
\lambda_j^{-1}E_1a_*\lambda_i,
\delta_j^{-1}w\delta_i,
U_1'(\delta_j^{-1})\kappa_{1,Z_j}E_1h\lambda_i
\right).
\tag{B.BT8}
\]
The letter \(a_*\) here denotes an arrow component, not the comparison \(a\) of (B.BT3). This is a strict dg functor on the full labelled subcategory. To check the third coordinate of its differential, substitute (B.BT7) into \(q_j'a_*'-U_1'w'q_i'-dh'\). The first term becomes the transported \(q_ja_*\). Naturality of \(\kappa_1\) for the homogeneous \(w\), and \(\delta_j\delta_j^{-1}=1\), convert the second term to the transported \(U_1wq_i\). All comparisons have degree zero and are closed, so the third term is the transported \(dh\), with no new sign. In a product, the adjacent \(\lambda\)'s and \(\delta\)'s cancel. The two witness terms retain exactly the coefficients \(1\) and \((-1)^{|s|}\) of (B.FT4). Identities have zero witness and remain identities. This proves differential, composition and unit compatibility in all degrees, not just for closed edges.

The canonical new object maps to the raw right-induced object by the closed graph isomorphism \((\lambda_i,\delta_i,0)\); its inverse is \((\lambda_i^{-1},\delta_i^{-1},0)\). Only these genuine isomorphisms are inverted. A chosen replacement homotopy equivalence is never used as a chain-level inverse in (B.BT8).

Here are enough explicit entries to identify this with the actual four-face calculation rather than an unlabelled isomorphic diagram:
\[
\begin{aligned}
c'&=E_1c\,d_{Q_0}^{-1},&c_M'&=E_1c_M\,d_{R_0}^{-1},\\
u_X'&=E_1u_X\,d_{Q_0}^{-1},&v'&=E_1v,\\
a_*'&=E_1a_*,&w'&=E_1w,\\
\vartheta'_{E_0Q_0}&=(Va)^{-1}\vartheta_{Q_0}x,&
\vartheta'_{E_0R_0}&=(Va_R)^{-1}\vartheta_{R_0}y,\\
b'_{\rm mate}&=\kappa_{1,VN}E_1b_{\rm mate}\,d_{Q_0}^{-1},&
\beta'&=\beta x,\\
b_M'&=U_1'((Va)^{-1})\kappa_{1,VM_0}E_1b_M\,d_{R_0}^{-1},&
h_v'&=U_1'((Va)^{-1})\kappa_{1,VM_0}E_1h_v.
\end{aligned}
\tag{B.BT9}
\]
In this display \(b_{\rm mate}\) is (B.RC1)'s old degree-minus-one mate witness, distinguished from the isomorphism \(b\) of (B.BT5). The old map called \(a\) in the four-face diagram is denoted \(a_*\) here. The target component of that arrow is \(b^{-1}(L_1c)x=L_1'c'\), by naturality of \(a_1\). The target component of \(c_M'\) is
\((Va)^{-1}(Ve_0^M)\vartheta_{R_0}y=(Ve_0^{M\prime})\vartheta'_{E_0R_0}\).
The target component of \(w'\) is \((Ve_0)(Va)=Ve_0'\), and that of the right counit is \(e_1b=e_1'\). These are equalities before restriction.

Likewise the three transposed left witnesses have the required targets:
\[
\begin{aligned}
(V\lambda_0')\vartheta'_{E_0Q_0}
 &=(Va)^{-1}(V\lambda_0)\vartheta_{Q_0}x,\\
(V\alpha_0')\vartheta'_{E_0R_0}
 &=(V\alpha_0)\vartheta_{R_0}y,\\
(V\Gamma_0')\vartheta'_{E_0Q_0}
 &=(V\Gamma_0)\vartheta_{Q_0}x.
\end{aligned}
\tag{B.BT10}
\]
Equations (B.BT3)--(B.BT4) and (B.BT9)--(B.BT10), together with (B.BT8), specify the transformed \(J_U,K_U,J_F,K_F,J_C,K_C,t,k\) with their original incidences. For instance \(J_U'=E_1J_Ud_{Q_0}^{-1}\), while
\(K_U'=U_1'((Va)^{-1})\kappa_{1,VM_0}E_1K_Ud_{Q_0}^{-1}\).
The additional factor \((Va)^{-1}\) at \(C\) is essential; the earlier right-only rule would give the wrong comparison when the left adjunction changes.

The original discrepancy, endpoint bridge, lift and cube therefore transport together. Writing \(\mathbf P=(P,\bar\gamma,W)\) as in (B.FG11), their last lift is
\[
\begin{aligned}
\mathbf P'&=(E_1P\,d_{Q_0}^{-1},\ \bar\gamma x,\
       \kappa_{1,VN}E_1W\,d_{Q_0}^{-1}),\\
D\mathbf P'-\mathbf P'\partial&=\mathscr B(\widehat R),\\
D\mathbf P'(g_H)&=\mathbf P'(g_T)-\mathbf P'(g_B)
                         +\mathscr B(\widehat R(f_H)).
\end{aligned}
\tag{B.BT11}
\]
The second and third lines follow by applying the strict dg functor to (B.FG11)--(B.FG13). They retain the whole degree-minus-four coordinate of the cube, not only its first component. The \(\beta x\) bridge in (B.BT9) and the \(\bar\gamma x\) target component in (B.BT11) are retained independently of that final witness.

**Successive two-sided refinements.** For refinements \(g\), then \(h\), use the actual induction compositors \(\mu_i:E_i^hE_i^g\to E_i^{hg}\). The horizontal and output comparisons satisfy
\[
\begin{aligned}
d^{hg}_P\mu_{1,SP}
 &=S''\mu_{0,P}\,d^h_{E_0^gP}\,E_1^hd^g_P,\\
a^g_{i,P}a^h_{i,E_i^gP}
 &=a^{hg}_{i,P}L_i''\mu_{i,P}.
\end{aligned}
\tag{B.BT12}
\]
For the normalized induction diagrams these identities follow on each balanced tensor by flattening the same ordered factors; no permutation or sign is introduced. They include all nonidentity proper-image comparisons upon evaluating the normalization back to the original models, as in (B.SN6). The mate identity is the adjoint identity (B.FT13). Consequently the canonical iterated transport is compared with direct transport by closed graph isomorphisms whose witness coordinate is zero and whose first two components are
\[
\begin{array}{c|c|c}
i&\text{source component}&\text{target component}\\\hline
Q_0^u&S''\mu_{0,Q_0}&L_1''S''\mu_{0,Q_0}\\
R_0^u&S''\mu_{0,R_0}&L_1''S''\mu_{0,R_0}\\
A&\mu_{1,A}&L_1''S''\mu_{0,Q_0}\\
C&\mu_{1,C}&VL_0''\mu_{0,Q_0}\\
Q_1^u&\mu_{1,Q_1}&L_1''\mu_{1,Q_1}\\
R_1&\mu_{1,R_1}&L_1''\mu_{1,Q_1}\\
Q_1^q&\mu_{1,Q_1}&1_{VN}
\end{array}
\tag{B.BT13}
\]
To verify the table, first compare the raw right-induced objects by \((\mu_{1,P_i},1_{Z_i},0)\), using the actual mate composition. Conjugate by the two systems \((\lambda_i,\delta_i,0)\). The first identity of (B.BT12) gives the first two source entries; the second gives their target entries and the entries at \(A,C,Q_1^u,R_1\). The other source entries are the original \(\mu_1\). This also proves naturality on every homogeneous triple in (B.BT8). The unit and pentagon equations reduce to the induction unit and pentagon equations on these same components, so they hold before passing to homotopy classes. In particular the canonical comparison is not declared to have identity target components at \(A\) or \(C\).

**Keep the supplied bars.** Since (B.BT8) preserves differential and ordered multiplication, it commutes with both the internal bar differential and the signed multiplication faces. Apply it to every supplied decorated coefficient. A higher coefficient with only witness \(W_r\) becomes
\(U_1'(\delta_j^{-1})\kappa_{1,Z_j}E_1W_r\lambda_i\).
The zero-witness graph isomorphisms telescope exactly as in (B.SN11). Thus the nonzero nested \(K_2\) of (B.MX12), its suspension sign, and all supplied higher coefficients survive. An arbitrary ordinary arrow-graph coefficient without an actual target-side lift is not silently promoted to a decorated one.

The diagram records the two distinct comparisons used at each vertex:
\[
\begin{array}{ccc}
P_i'&\xrightarrow{\lambda_i}&E_1P_i\\
{\scriptstyle q_i'}\downarrow&&\downarrow{\scriptstyle\kappa_{1,Z_i}E_1q_i}\\
U_1'Z_i'&\xrightarrow{U_1'\delta_i}&U_1'Z_i.
\end{array}
\qquad
\begin{gathered}
\lambda_{Q_0^u}=d_{Q_0}^{-1},\quad\lambda_{R_0^u}=d_{R_0}^{-1},\\
\delta_A=x,\qquad\delta_C=Va.
\end{gathered}
\tag{B.BT14}
\]
The square commutes by (B.BT7). Its horizontal maps are actual isomorphisms; its vertical maps need not be. The table (B.BT6) preserves the seven original vertices and the paths on which each occurs.

**Geometric hypotheses.** The simultaneous *induced* refinement of the four-face diagram has actual source/target comparisons and successive-refinement coherence. It uses (B.BT2)'s supplied whole-diagram comparison; merely having a map with the same name, a derived isomorphism class, or separately chosen pointwise replacements does not establish that input. Comparing independently chosen replacement diagrams still requires their actual target maps and checked shared boundaries, especially at the three unit objects, whose structure maps need not be invertible. The full geometric horizontal-composition/base-change and higher overlap assembly is therefore still open. Geometric nearby-cycle multiplicative descent, coefficient-system completion and rationalization with derived limits and strict-heart effacement are not established by this construction. \(\square\)



### Whole replacement comparison without inverting units

**Proposition B.1ar (one whole envelope, including the unit vertices).** Fix the actual decorated seven-object diagram of (B.FT2)--(B.FT5), or its induced bilateral transport in B.1aq. There is an explicit path envelope of this entire diagram and a whole semifree replacement of that envelope. It compares back to the original objects, faces and full cube without assuming that a unit map is a quasi-isomorphism. Independent whole replacements **of this same envelope** admit natural graph comparisons with all relative free choice-coherences. Their comparisons back to the original diagram include an explicit second witness. This does not identify geometric diagrams with different, as yet uncompared, target maps.

**An envelope for every arrow, not only replacements.** Work in the actual decorated category \(\mathcal A_U\) of (B.FT2). Write \(q:P\to Y=UZ\), with \(q\) closed of degree zero; no quasi-isomorphism condition on \(q\) is imposed. Set
\[
\begin{aligned}
W(q)^n&=P^n\oplus Y^n\oplus Y^{n-1},\\
d_W(p,y,z)&=(dp,dy,-dz+qp-y),\\
r(p,y,z)&=p,& t(p,y,z)&=y,\\
H(p,y,z)&=z,\\
j(p)&=(p,qp,0),& s(p,y,z)&=(0,-z,0).
\end{aligned}
\tag{B.PE1}
\]
Here \(r,t,j\) have degree zero and \(H,s\) degree minus one. Use the ordinary right module action on the three summands; the shifted differential has the displayed minus sign. The module Leibniz rule follows directly, and the last coordinate of \(d_W^2\) is \(-d(qp-y)+qdp-dy=0\). With \(d\) on maps denoting the Hom differential, substitution gives
\[
\begin{aligned}
dr=dt=dj&=0,& dH&=qr-t,\\
rj&=1,& tj&=q,& Hj&=0,\\
ds&=1-jr,& ts&=-H,& rs=Hs&=0.
\end{aligned}
\tag{B.PE2}
\]
For example \((d_Ws+sd_W)(p,y,z)=(0,y-qp,z)\). Thus \(r\) and \(j\) are chain homotopy inverses for **any** \(q\). If \(P\) is h-projective, so is \(W(q)\): precomposition with these maps identifies its Hom complex up to homotopy with \(\operatorname{Hom}(P,-)\). No projectivity of \(UZ\) is needed. Since \(t\) is homotopic to \(qr\), it is a quasi-isomorphism exactly when \(q\) is. In particular the envelope has not turned a non-quasi-isomorphic unit into a replacement of its target.

For a homogeneous decorated arrow \(f=(a,w,h):q\to q'\) of degree \(n\), define
\[
\begin{aligned}
W(f)(p,y,z)&=(ap,U(w)y,hp+(-1)^nU(w)z),\\
F(q)&=(W(q),Z,t),& F(f)&=(W(f),w,0).
\end{aligned}
\tag{B.PE3}
\]
Both are strict unital dg functors. For the differential, the third coordinate of \(d_W'W(f)-(-1)^nW(f)d_W\) on \(p\) is \(q'a-U(w)q-dh\), the third coordinate in (B.FT2). Its remaining diagonal blocks are \(da,U(dw),(-1)^{n+1}U(dw)\), with the other block zero. For a product of degrees \(m,n\), the third-source block is \(h_sa_t+(-1)^mU(w_s)h_t\) and the last diagonal block is \((-1)^{m+n}U(w_sw_t)\). These are exactly \(W(sf)\)'s blocks. The identity is immediate. Moreover \(t'W(f)=U(w)t\), proving the assertion for \(F\). The actual target map is still \(w\), not an equality inferred from its restriction.

The projection \(H\) is not a graded natural transformation to \(UZ\). Its precise defect is essential:
\[
\begin{aligned}
r'W(f)&=ar,& t'W(f)&=U(w)t,\\
H'W(f)-(-1)^nU(w)H&=hr,\\
C_q&=(r,1_Z,H):F(q)\longrightarrow q,\\
fC_q&=C_{q'}F(f),& DC_q&=0.
\end{aligned}
\tag{B.PE4}
\]
The first two naturality coordinates follow from the projections. The third is \(hr+(-1)^nU(w)H=H'W(f)\), exactly the defect just displayed. Consequently \(C\), unlike \(H\) alone, is a strict dg natural comparison. It is an objectwise homotopy equivalence in \(\mathcal A_U\):
\[
J_q=(j,1_Z,0),\qquad
C_qJ_q=1_q,\qquad
1_{F(q)}-J_qC_q=D(s,0,0).
\tag{B.PE5}
\]
The last third coordinate is \(ts=-H\), not zero. The maps \(J_q\) are used only as objectwise inverses; no naturality of the family \(J\) is asserted.

**Keep the actual canonical unit and counit interface.** For the actual dg adjunction \(L\dashv U\), write \(\operatorname{Adj}(q):LP\to Z\) for the transpose of \(q\). This notation fixes its direction. Put \(e_q=\operatorname{Adj}(q)\), \(e_t=\operatorname{Adj}(t)\), and \(\beta=\operatorname{Adj}(H)\). Let \(J_L(P)=(P,LP,\eta_P)\) and \(J_L(a)=(a,La,0)\). Naturality of the unit makes \(J_L\) a dg functor. The canonical closed arrows \(E_q=(1_P,e_q,0)\) and \(E_t=(1_W,e_t,0)\) satisfy
\[
\begin{aligned}
d\beta&=e_qLr-e_t,\\
E_qJ_L(r)-C_qE_t&=D(0,\beta,0),\\
(0,\beta,0)&:J_L(W(q))\longrightarrow q
\quad\text{has degree }-1.
\end{aligned}
\tag{B.PE6}
\]
The actual target-side equality is the transpose of \(dH=qr-t\). The third coordinate of the right side is \(-U(\beta)\eta_W=-H\), equal to the left side. This proves the square before any assumption that \(U\) is faithful. For degree-\(n\) \(f\), this witness itself has the explicitly controlled defect
\[
(0,\beta',0)J_L(W(f))
-(-1)^nf(0,\beta,0)
=(0,\operatorname{Adj}(hr),0).
\tag{B.PE7}
\]
Indeed its target component is the transpose of the second line of (B.PE4), and its other components vanish. Thus (B.PE6) is not silently promoted to a strictly natural square of homotopies.

At an old unit object \(q=\eta_P\), one has \(e_q=1_{LP}\). Hence \(e_t\) is homotopic to \(Lr\), and is a homotopy equivalence, because a dg functor preserves an explicit chain homotopy equivalence. Neither \(\eta_P\) nor \(t\) need be quasi-isomorphisms. For a concrete example over a field, take \(L=T\otimes-\), \(U=\operatorname{Hom}(T,-)\), with \(T=k^2\), and \(P=k\) in degree zero. The unit sends \(1\) to the identity endomorphism in \(\operatorname{Hom}(T,T)\), a one-dimensional subspace of a four-dimensional space. It is not a quasi-isomorphism; nevertheless (B.PE1)--(B.PE7) apply. Keep \(e_t\) and its witnesses as maps. Do not insert a homotopy inverse in an expression requiring a genuine chain isomorphism, such as the target conjugation in (B.BT8).

**Resolve the seven objects as one diagram.** Take \(\mathcal I\) to be the small labelled full dg subcategory of \(\mathcal A_U\) on the seven objects in (B.FT3), with their actual target maps. Distinct labels remain distinct even when underlying objects coincide. The supplied four faces, the \(\beta\) bridge, \(\bar\gamma\), and the full cube are actual homogeneous arrows with the boundaries checked in (B.FT4)--(B.FT5). For an original higher bar presentation, first use its supplied strict decorated roof; a mere restricted map is not an invented decorated lift. Pull the inclusion back to \(\mathcal J=Q\mathcal I\) of B.1t, and denote the resulting strict diagram by \(D\). Apply (B.ND5)--(B.ND6) to the whole diagram \(WD\), as a module over \(\mathcal J^{\mathrm{op}}\otimes\mathcal C\):
\[
\begin{aligned}
\rho:V&\xrightarrow{\ \simeq\ }WD,
&q_i^\rho&=t_i\rho_i,\\
D^\rho_i&=(V_i,Z_i,q_i^\rho),
&D^\rho(f)&=(V(f),w_f,0),\\
C_i^\rho&=(r_i\rho_i,1_{Z_i},H_i\rho_i):D_i^\rho\longrightarrow D_i.
\end{aligned}
\tag{B.PE8}
\]
Here \(V\) is whole semifree, and every \(V_i\) is h-projective by the free-index path filtration, not by an assertion that pointwise projectivity implies diagram projectivity. The maps \(q^\rho\) are strictly natural, and (B.PE4) proves strict naturality and closedness of \(C^\rho\). If \(q_i\) is a genuine replacement, so is \(q_i^\rho\); at the unit vertices no such assertion is made. Applying the strict functor \(F\) and the natural comparison to the full decorated diagram retains every original boundary. A formerly nonzero third coordinate, including the degree-minus-four cube term, is now the third-source block of \(W(f)\); it has not disappeared merely because \(F(f)\)'s external third coordinate is zero.

For completeness \(C_i^\rho\) is also an objectwise graph homotopy equivalence. Since \(W_i\) is homotopy equivalent to the original h-projective \(P_i\), the quasi-isomorphism \(\rho_i:V_i\to W_i\) is a homotopy equivalence. Choose \(\sigma,A,B\) with \(dA=\rho\sigma-1\), \(dB=\sigma\rho-1\). The cycle \(\rho B-A\rho\) can be made a boundary by changing \(B\) by a closed map: postcomposition by \(\rho\) on \(\operatorname{Hom}(V_i,-)\) is a quasi-isomorphism. Thus choose \(K\) so that \(\rho B-A\rho=dK\). Suppressing \(i\), in the graph category put
\[
\begin{aligned}
R&=(\rho,1,0),& S&=(\sigma,1,tA),\\
RS-1&=D(A,0,0),& SR-1&=D(B,0,tK).
\end{aligned}
\tag{B.PE9}
\]
The last coordinate in the second identity is \(t\rho B-d(tK)=tA\rho\); closedness of \(S\) follows from \(dA=\rho\sigma-1\). Compose \(R\) with (B.PE5). The use of \(A,B,K\) here is objectwise; it is not a substitute for the whole natural choice comparison below. The canonical-unit interface for \(V_i\) is (B.PE6) with \(r\rho\), \(t\rho\), \(H\rho\); transpose these actual maps before restriction.

**Compare independent whole choices over this envelope.** Let \(\rho:V\to WD\) and \(\rho':V'\to WD\) be two whole h-projective replacements. By (B.ND7), postcomposition by \(\rho'\) on the whole natural Hom complex with source \(V\) is a quasi-isomorphism. It supplies a closed degree-zero \(a\) and a degree-minus-one graded natural \(h\) such that
\[
\begin{aligned}
\rho'a-\rho&=dh,\\
A_{\rho',\rho}&=(a,1_Z,th):D^\rho\longrightarrow D^{\rho'},\\
DA_{\rho',\rho}&=0.
\end{aligned}
\tag{B.PE10}
\]
All seven components are chosen simultaneously. The sign in (B.ND4), together with naturality of \(t\), gives the third-coordinate naturality of \(A\). The source map \(a\) is a quasi-isomorphism and hence a whole homotopy equivalence. The comparison to the original diagram requires a second witness, not just \(rh\):
\[
\begin{aligned}
C^{\rho'}A_{\rho',\rho}-C^\rho&=DB_{\rho',\rho},\\
B_{\rho',\rho}&=(rh,0,Hh),
&|rh|&=-1,& |Hh|&=-2.
\end{aligned}
\tag{B.PE11}
\]
The third coordinate of \(DB\) is
\(qrh-d(Hh)=(dH+t)h-dHh+Hdh=th+Hdh\), exactly that of the left side. For a degree-\(n\) index arrow, \(h_jV(f)=(-1)^nW(f)h_i\). Insert (B.PE4)'s defect to obtain \(B_jD^\rho(f)=(-1)^nD(f)B_i\): the extra term is \((-1)^nh_fr_ih_i\), precisely the graph product's term. This proves whole graded naturality of \(B\), despite the nonnaturality of \(H\) alone. Omitting \(Hh\) would change the boundary.

**All higher choice cells use a genuine acyclic projection.** Form a dg category whose objects are these whole maps \(\rho\). A degree-\(n\) arrow is \(x=(\lambda,a,h)\), with \(a:V\to V'\) of degree \(n\), \(h:V\to WD\) of degree \(n-1\), and \(\lambda\in k^n\), where \(k\) is concentrated in degree zero. Keep \(\lambda\) as a formal scalar coordinate even if its action on \(WD\) is zero. For composable arrows \(x_s,x_t\), define
\[
\begin{aligned}
D(\lambda,a,h)&=(0,da,\rho'a-\lambda\rho-dh),\\
x_sx_t&=(\lambda_s\lambda_t,a_sa_t,
       h_sa_t+(-1)^{|s|}\lambda_sh_t),\\
\pi(\lambda,a,h)&=\lambda,\\
\Phi(\lambda,a,h)&=(a,\lambda1_Z,th).
\end{aligned}
\tag{B.PE12}
\]
These are the graph differential and multiplication of (B.FT2), with a retained scalar coordinate, and so obey \(D^2=0\), Leibniz and associativity. The unit is \((1,1,0)\). Projection \(\pi\) to the one-object dg category \(k\) is degreewise surjective. Its Hom kernel is the shifted cone of \(\operatorname{Hom}(V,\rho')\), acyclic by (B.ND7). This argument uses \(\rho'\), **never the unit map**. The map \(\Phi\) is a strict dg functor to the category of whole decorated diagrams and graded natural transformations, since \(t\) is closed and strictly natural. Reverse lifts of scalar \(1\) exist; each composite minus its identity is a closed kernel element and hence a boundary. Applying \(\Phi\) proves that (B.PE10)'s graph comparison is a whole homotopy equivalence.

For every homogeneous choice arrow, put \(B(x)=(rh,0,Hh)\), of degree \(|x|-1\). A computation using \(dH=qr-t\) strengthens (B.PE11):
\[
\begin{aligned}
DB(x)+B(Dx)&=C^{\rho'}\Phi(x)-\lambda C^\rho,\\
B(st)&=B(s)\Phi(t)+(-1)^{|s|}\lambda_sB(t).
\end{aligned}
\tag{B.PE13}
\]
For the first equality, the first coordinate is \(rdh+r(\rho'a-\lambda\rho-dh)\), and the third is \(th+Hdh+H(\rho'a-\lambda\rho-dh)\); these simplify to the claimed coordinates. Target coordinates are zero. For the product equality, both nonzero coordinates are the corresponding projections of \(h_sa_t+(-1)^{|s|}\lambda_sh_t\); the target coordinate of \(B(s)\) is zero, so no term is missing from its graph product. These identities also verify the compatibility of the comparison-back witnesses with higher choice differentials and compositions.

Now (B.ND9) lifts any **specified relative free** choice-comparison diagram over \(k\), preserving its already supplied boundary lifts, through \(\pi\). Applying \(\Phi\) and (B.PE13) gives natural higher comparisons and the compatible comparisons back to the original diagram. No claim is made for a nonfree quotient with unchecked relations. The basic shape, on each of the seven labels and with all index maps retained, is
\[
\begin{array}{ccc}
D^\rho&\xrightarrow{\ A_{\rho',\rho}\ }&D^{\rho'}\\
{C^\rho}\downarrow&&\downarrow{C^{\rho'}}\\
D&\xrightarrow{\ 1\ }&D
\end{array}
\qquad
C^{\rho'}A-C^\rho=DB.
\tag{B.PE14}
\]
This is a homotopy-commutative square, not a strictly commutative one; \(B\) includes its degree-minus-two component. Equations (B.PE12)--(B.PE13) explain how the square varies over the chosen free comparison index.

**Geometric hypotheses.** The whole roof preserves the unit and is independent of its whole-diagram resolution choices for the seven-object decorated diagram, including the induced bilateral model. This construction uses no acyclic-cone assertion at \(\eta\); it includes the four faces, their target maps and the full cube. It does not assert that two separately constructed geometric diagrams already have this same target or matching shared boundaries. That identification, the full horizontal-composition/base-change overlap assembly, geometric nearby-cycle multiplicative descent, coefficient-system completion and rationalization with derived limits and strict-heart effacement remain required. \(\square\)



### Compare envelope choices across geometric refinements

**Proposition B.1as (the actual refinement map between envelopes).** In the full scope of B.1m, the unit-safe whole envelope in B.1ar is compatible with the **actual** compactification-refinement dg functor, its induction and its mate. This supplies a common target for an induced old replacement and an independently chosen replacement on the refined model, over the same supplied whole parameter index. It includes the seven source/target labels of the bilateral diagram and the successive-refinement comparisons. An unresolved base-change mate is not inferred from this proper-refinement construction.

**Bind the geometric maps before choosing replacements.** For a proper refinement \(h:\overline X_0\to\overline X_1\) fixing the protected open and its final target, take \(G=G_h\) exactly as in (B.CR2), including the image of its graph homotopy. Let \(R=G_!\), \(L=F_{0!}\), \(L'=F_{1!}\), \(U=F_0^*\), and \(U'=F_1^*\). The clopen adjunction map (B.CR1) and proper-image composition (B.CR5) give the actual maps
\[
\begin{aligned}
c_P:L'RP&\xrightarrow{\sim}LP,\\
\kappa_Z:RUZ&\longrightarrow U'Z,\\
\varepsilon'_ZL'\kappa_Z&=\varepsilon_Zc_{UZ},\\
\kappa_{LP}R\eta_P&=U'(c_P)\eta'_{RP}.
\end{aligned}
\tag{B.ER1}
\]
These are (B.CR7)--(B.CR9), not chosen isomorphism classes. In particular \(\kappa\) exists on **all** restriction modules here, by its balanced-tensor formula. Write \(Tq=(RP,Z,q^g)\), \(q^g=\kappa_ZRq\), and \(T(a,w,h)=(Ra,w,\kappa Rh)\), as in (B.FT6). The functor \(T\) is strict dg. Neither its definition nor the following envelope calculation requires the structure map \(q\) to be a quasi-isomorphism.

Use \(r,t,H,j,s\) for the maps of \(W(q)\), and superscript \(g\) for those of \(W'(Tq)\), formed with \(U'\). There is a closed map
\[
\begin{aligned}
\Theta_q:RW(q)&\longrightarrow W'(Tq),\\
\Theta_q&=(Rr,\kappa_ZRt,\kappa_ZRH),\\
r^g\Theta_q&=Rr,&t^g\Theta_q&=\kappa_ZRt,\\
H^g\Theta_q&=\kappa_ZRH,&\Theta_qRj&=j^g.
\end{aligned}
\tag{B.ER2}
\]
The three entries on the second line are the three projections into the envelope, not a decorated graph arrow: their unshifted degrees are \(0,0,-1\). This intrinsic formula uses the actual dg induction on maps; it therefore includes its shift identifications rather than assuming that a choice of bases makes induction commute with shifts literally. Closedness follows from
\(d(\kappa RH)=\kappa R(qr-t)=q^gRr-\kappa Rt\).
The first two components are closed. The final identity follows from \(rj=1,tj=q,Hj=0\).

For every homogeneous decorated \(f=(a,w,h)\), the comparison is strictly natural:
\[
W'(Tf)\Theta_q=\Theta_{q'}RW(f).
\tag{B.ER3}
\]
The first and second projections use naturality of \(r,t,\kappa\). For the third, (B.PE4) gives
\(\kappa R(H'W(f))=\kappa R(hr)+(-1)^{|f|}\kappa R(U(w)H)\).
Naturality of \(\kappa\) turns its last term into
\((-1)^{|f|}U'(w)\kappa RH\), the last coordinate of the other composite. This retains \(h\) and its sign in every degree.

Let \(F,F'\) be the two envelope functors. Then
\[
\begin{aligned}
\tau_q&=(\Theta_q,1_Z,0):TF(q)\longrightarrow F'T(q),\\
D\tau_q&=0,& C^g_q\tau_q&=T(C_q).
\end{aligned}
\tag{B.ER4}
\]
The first assertion is \(t^g\Theta=\kappa Rt\); the second uses all three projection identities in (B.ER2). Thus it is an equality of decorated maps, retaining their actual target components. No faithfulness of \(U'\) is invoked. Although \(\Theta\) need not be a chain isomorphism, \(\tau\) is an objectwise graph homotopy equivalence with explicit inverse and witnesses. Put
\[
\begin{aligned}
\upsilon_q&=(Rj\,r^g,1_Z,H^g),\\
\tau_q\upsilon_q-1&=D(-s^g,0,0),\\
\upsilon_q\tau_q-1&=D(-Rs,0,0).
\end{aligned}
\tag{B.ER5}
\]
Closedness of \(\upsilon\) is \(q^gr^g-t^g=dH^g\). The first composite has source component \(j^gr^g\) and witness \(H^g\); the second has \(R(jr)\) and \(\kappa RH\). Equation (B.PE2), including \(ts=-H\), gives the displayed differentials. As with (B.PE5), these inverses are objectwise witnesses, not an asserted natural inverse family. In particular no inverse to \(\kappa\), to a unit, or to a homotopy equivalence as a literal chain isomorphism has been used.

**Transport a whole replacement to this actual new target.** Let \(D:\mathcal J\to\mathcal A_U\) be the supplied seven-object decorated diagram over its free index, with h-projective source modules at every object. Take \(\rho:V\to WD\) as in (B.PE8). Use the whole induction along \(1_{\mathcal J^{\mathrm{op}}}\otimes G\), identified with pointwise \(R\) by (B.ND8). Define
\[
\begin{aligned}
\rho^g&=\Theta_D R\rho:RV\longrightarrow W'TD,\\
t^g\rho^g&=\kappa R(t\rho),\\
C^{\rho^g}&=T(C^\rho).
\end{aligned}
\tag{B.ER6}
\]
This is a closed natural whole quasi-isomorphism. Here is the necessary check: induction preserves whole h-projectivity by its Hom adjunction, so \(RV\) is whole h-projective. At each index value \(V_i\) and \(W(D_i)\) are h-projective, the former by (B.ND6) and the latter by (B.PE2). Hence \(\rho_i\) is a homotopy equivalence. The dg functor \(R\) preserves that explicit equivalence, and \(\Theta_i\) is one by (B.ER5). Their composite is a quasi-isomorphism at every index value. This is **not** an application of ordinary induction to an arbitrary quasi-isomorphism, nor a claim that \(WD\) is automatically whole h-projective. Formula (B.ER4) proves the last equality, component by component. The actual source, target and full cube maps of the old diagram therefore compare to the new ones simultaneously.

If \(\rho':V'\to W'TD\) is an independently chosen whole h-projective replacement on that refined model, (B.ND7) now applies to an identified common target. Choose \(a,h\) in the whole Hom complexes with
\[
\begin{aligned}
\rho'a-\rho^g&=dh,& da&=0,\\
A&=(a,1_Z,t^gh),\\
C^{\rho'}A-T(C^\rho)&=D(r^gh,0,H^gh).
\end{aligned}
\tag{B.ER7}
\]
This is precisely (B.PE10)--(B.PE11), now between the independent new model and the transported old one. The graph map \(A\) is a whole homotopy equivalence. The final coordinate has degree minus two and is required. All relative free choice-comparisons and their compatibility with comparison back follow from (B.PE12)--(B.PE13), over this same identified whole target. Values at a different, unconnected parameter index are not silently substituted.

**Successive geometric refinements.** For \(g\), then \(h\), use the actual induction compositor \(\mu:R_hR_g\to R_{hg}\) from (B.CR4), together with its mate identity. Let \(m_q=(\mu_P,1_Z,0):T_hT_gq\to T_{hg}q\). It is a closed graph isomorphism by that mate identity. On envelopes,
\[
\begin{aligned}
W''(m_q)\Theta^h_{T_gq}R_h\Theta^g_q
 &=\Theta^{hg}_q\mu_{W(q)},\\
W''(m_D)\,\rho^{h,g}
 &=\rho^{hg}\mu_V.
\end{aligned}
\tag{B.ER8}
\]
For the first equality the source projection is the naturality equation for \(\mu\) and \(r\). Each of the other two projections is the mate identity
\(\kappa^{hg}_Z\mu_{UZ}=\kappa^h_ZR_h\kappa^g_Z\),
composed respectively with \(R_hR_gt\) and \(R_hR_gH\). These three projections determine the map into the direct-sum envelope. The second equality follows by naturality of \(\mu\) on \(\rho\). Induction's unit and pentagon identities now give the same equations for every finite refinement string: project to these three components, flatten the ordered balanced tensors, and use (B.CR4)'s actual composition identities. No independently chosen inverse of \(\Theta\) is used to assert coherence. Independent replacement choices at those vertices are subsequently compared in the fixed receiving envelope as in (B.ER7); specified relative free higher boundaries are retained by (B.PE12)--(B.PE13).

**Restore all seven bilateral labels.** In (B.BT6)--(B.BT8), take \(R=E_1\), and retain the specified closed isomorphisms
\(\lambda_i:P_i'\to RP_i\), \(\delta_i:Z_i'\to Z_i\).
The normalized object \(\bar q_i=U'(\delta_i^{-1})q_i^g\lambda_i\) has the actual graph isomorphism
\[
\begin{aligned}
I_i&=(\lambda_i,\delta_i,0):\bar q_i\longrightarrow Tq_i,\\
W'(I_i)&=\operatorname{diag}(\lambda_i,U'\delta_i,U'\delta_i),\\
\bar\Theta_i&=W'(I_i^{-1})\Theta_i.
\end{aligned}
\tag{B.ER9}
\]
The diagonal formula uses the envelope direct-sum coordinates; it includes the shifted third block with the same degree-zero map. The functor on the normalized diagram is conjugation by the \(I_i\)'s, so (B.ER3) proves naturality of \(\bar\Theta\) for every homogeneous arrow. Its receiving target is now **the normalized geometric envelope**, with the actual target at \(C\) changed by \(\delta_C=Va\), as well as the changes at \(A\) and the unit vertices. The two horizontal source comparisons \(\lambda_{Q_0^u}=d_{Q_0}^{-1}\), \(\lambda_{R_0^u}=d_{R_0}^{-1}\) are not dropped.

The transported whole source remains \(RV_i\); its target label becomes \(Z_i'\). Its actual replacement and comparison-back components are
\[
\begin{aligned}
\bar\rho_i&=\bar\Theta_iR\rho_i,\\
\bar q_i^{\bar\rho}&=U'(\delta_i^{-1})\kappa_{Z_i}R(t_i\rho_i),\\
\bar C_i&=(\lambda_i^{-1}R(r_i\rho_i),1_{Z_i'},
       U'(\delta_i^{-1})\kappa_{Z_i}R(H_i\rho_i)).
\end{aligned}
\tag{B.ER10}
\]
The \(\bar\rho\)'s are whole quasi-isomorphisms because (B.ER9) is an actual isomorphism after (B.ER6). Compare them with independent whole replacements of \(W'\bar D\) by (B.ER7). The \(\lambda_i\)'s act on the **old comparison-back source**, not by an invented isomorphism on the newly chosen \(RV_i\). Equations (B.BT12)--(B.BT13) and functoriality of \(W'\) supply the normalized versions of (B.ER8), with their nonidentity target components. Every original decorated face, the \(\beta\) and \(\bar\gamma\) components, and the nested second and cube coefficients are retained: (B.ER3) applies to their actual homogeneous arrows, and (B.ER9) only conjugates by the displayed graph isomorphisms. Ordered bar differentials are preserved by these dg functors; no absent decorated lift is created.

**Check the actual adjunction targets as well.** Denote by \(e_t,\beta\) the transposes of \(t,H\) from (B.PE6). Let \(e_{t^g},\beta^g\) be their new-envelope counterparts. Transposing the second and third projections in (B.ER2), using the counit identity in (B.ER1), gives actual maps before restriction:
\[
\begin{aligned}
e_{q^g}&=e_qc_P,\\
e_{t^g}L'\Theta_q&=e_tc_{W(q)},\\
\beta^g L'\Theta_q&=\beta c_{W(q)},\\
e_{\bar t_i}L'\bar\Theta_i&=\delta_i^{-1}e_{t_i}c_{W(q_i)},\\
\bar\beta_iL'\bar\Theta_i&=\delta_i^{-1}\beta_i c_{W(q_i)}.
\end{aligned}
\tag{B.ER11}
\]
For example \(\operatorname{Adj}'(\kappa RH)=\varepsilon'L'(\kappa RH)=\varepsilon c_{UZ}L'RH=\varepsilon LHc_W=\beta c_W\), by naturality of \(c\) for the degree-minus-one \(H\). The other lines are the same computation, and target conjugation gives the last two. Their differentials are the transported (B.PE6) unit/counit square; its nonzero graded naturality defect (B.PE7) is retained through (B.ER3). At a canonical old unit, \(e_q=1\) and \(e_{q^g}=c_P\); restoration by the prescribed target isomorphism gives the new canonical unit using (B.ER1). A general whole-envelope replacement of that object is still compared by (B.PE6), not declared literally canonical or quasi-isomorphic to the unit's target.

The resulting comparison diagram is
\[
\begin{array}{ccc}
TFD&\xrightarrow{\ \tau_D\ }&F'TD\\
{T(C_D)}\downarrow&&\downarrow{C^g_D}\\
TD&\xrightarrow{\ 1\ }&TD.
\end{array}
\tag{B.ER12}
\]
This square commutes strictly by (B.ER4). Replacing its top row by independently chosen whole resolutions gives the witnessed square (B.ER7), whose second witness must not be erased. Equations (B.ER8)--(B.ER11) specify its refinement composition, bilateral labels and actual adjunction interfaces.

**Proper refinement and geometric inverse image.** The common target required for independent choices across the actual proper-refinement maps, including their normalized bilateral labels, is defined over the specified whole index. This uses the globally defined mate \(\kappa\) of (B.CR8). For geometric base change, the left inverse comparison in (B.BM15) is defined on resolved h-projective inputs. Equations (B.BM16)--(B.BM18) intentionally use \(\operatorname{Adj}(Ve^0_N\theta_{P_0})\), not \(\theta_{U_0N}\). Therefore (B.ER2) cannot be reused there by postulating a mate on unresolved \(U_0N\). The remaining changing-index assembly must retain those resolved-only transposes, the actual mixed cell (B.GC12)--(B.GC13), both inverse witnesses and the nested second coefficient (B.MX12). Geometric nearby-cycle multiplicative descent, whole coefficient completion and rationalization with derived limits and strict-heart effacement are not established by this construction. \(\square\)



### Resolved base-change transport and its comparison witnesses

**Proposition B.1at (transport without an unresolved mate).** The resolved left comparison supplied by (B.KC15) transports the decorated objects, homogeneous arrows and whole path envelopes used above. Its homotopies have an explicit signed naturality witness, to which the existing bar comparison applies. This identifies the receiving envelope for independently chosen replacements of the transported diagram. It does not make the right mate invertible, identify unrelated replacement targets, or supply the higher changing-index assembly without its boundary checks.

**Keep the domain of the comparison explicit.** Work with actual dg adjunctions \(L_i\dashv U_i\), for \(i=0,1\), between the chosen module models. Let \(S\) act on their source categories and \(V\) on their target categories. Assume that \(S\) preserves h-projectives and that a closed degree-zero dg-natural map
\[
\theta_P:L_1SP\longrightarrow VL_0P
\tag{B.ZT1}
\]
is supplied on the full dg subcategory of admitted h-projective source models. In applications it is a map of the whole kernel models, not independently chosen values at each object. Naturality includes nonclosed homogeneous maps. No value on an unresolved \(U_0Z\) is assumed. Write \(\operatorname{Adj}_i\) for the chain isomorphism from maps out of \(L_i\) to maps into \(U_i\). For \(q:P\to U_0Z\), set \(e_q=\varepsilon^0_ZL_0q\). For a degree-\(n\) decorated arrow \(f=(a,w,h):q\to q'\), set \(\beta_f=\varepsilon^0_{Z'}L_0h\), of degree \(n-1\). Define
\[
\begin{aligned}
\zeta_q&=\operatorname{Adj}_1(Ve_q\,\theta_P),\\
T_\theta(q)&=(SP,VZ,\zeta_q),\\
T_\theta(f)&=(Sa,Vw,\operatorname{Adj}_1(V\beta_f\,\theta_P)).
\end{aligned}
\tag{B.ZT2}
\]
This is a strict dg functor on the admitted decorated category. Indeed, the transpose of the third component of \(Df\) is
\(e_{q'}L_0a-we_q-d\beta_f\).
Naturality of the closed \(\theta\) identifies its transported first term with \(Ve_{q'}\theta_{P'}L_1Sa\); the chain adjunction then gives exactly (B.FT3). For a degree-\(m\) arrow \(g=(b,v,k)\), the transpose of the composite witness is
\(\beta_gL_0a+(-1)^m v\beta_f\).
The same naturality identity proves preservation of composition. The unit has zero witness. This argument uses \(\theta\) only on h-projective sources, and does not require \(q\) or \(\theta\) to be invertible.

**The receiving envelope.** Use \(r,t,H,j,s\) for the path envelope \(W(q)\) of (B.PE1)--(B.PE2). Its source is h-projective because \(W(q)\) is homotopy equivalent to \(P\), even when \(U_0Z\) is not h-projective. Put \(e_t=\varepsilon^0_ZL_0t\) and \(\beta=\varepsilon^0_ZL_0H\). Use superscript \(*\) for the envelope \(W'(T_\theta q)\) formed with \(U_1\). Define a map by its three envelope projections:
\[
\begin{aligned}
\Theta_q:SW(q)&\longrightarrow W'(T_\theta q),\\
r^*\Theta_q&=Sr,\\
t^*\Theta_q&=\operatorname{Adj}_1(Ve_t\,\theta_{W(q)}),\\
H^*\Theta_q&=\operatorname{Adj}_1(V\beta\,\theta_{W(q)}).
\end{aligned}
\tag{B.ZT3}
\]
These are envelope projections of unshifted degrees \(0,0,-1\), not the entries of a decorated graph arrow. Since \(d\beta=e_qL_0r-e_t\), their differentials satisfy
\(d(H^*\Theta)=\zeta_qSr-t^*\Theta\).
The first two projections are closed, so \(\Theta\) is a closed map into the direct-sum envelope. Naturality of \(\theta\) on \(j\) and \(s\), with (B.PE2), also gives
\[
\begin{aligned}
\Theta_qSj&=j^*,\\
(t^*\Theta_q)Ss&=-H^*\Theta_q,\\
(H^*\Theta_q)Ss&=0.
\end{aligned}
\tag{B.ZT4}
\]
For every homogeneous decorated \(f:q\to q'\),
\[
W'(T_\theta f)\Theta_q=\Theta_{q'}SW(f).
\tag{B.ZT5}
\]
The first projection is naturality of \(r\). For the second use \(t'W(f)=U_0(w)t\), transpose and apply naturality of \(\theta\) on \(W(f)\). For the third use the complete equation \(H'W(f)=hr+(-1)^nU_0(w)H\). Its transpose has both terms; naturality on \(r\) turns the first into the transported witness composed with \(Sr\), and the second remains \((-1)^nU_1(Vw)H^*\Theta\). This is the third projection of the left side. In particular the graph homotopy is not discarded to obtain naturality.

Let \(F,F'\) be the envelope functors and \(C,C^*\) their comparison-back maps. There are explicit graph maps and inverse witnesses
\[
\begin{aligned}
\tau_q&=(\Theta_q,1_{VZ},0):T_\theta Fq\longrightarrow F'T_\theta q,\\
\upsilon_q&=(Sj\,r^*,1_{VZ},H^*),\\
C^*_q\tau_q&=T_\theta C_q,\\
\tau_q\upsilon_q-1&=D(-s^*,0,0),\\
\upsilon_q\tau_q-1&=D(-Ss,0,0).
\end{aligned}
\tag{B.ZT6}
\]
The transpose defining the structure map of \(T_\theta Fq\) is the second projection in (B.ZT3); hence \(\tau\) is closed. Closedness of \(\upsilon\) follows from \(t^*\Theta Sj=\zeta_q\) and \(dH^*=\zeta_qr^*-t^*\). The two composite sources are \(j^*r^*\) and \(S(jr)\), with witnesses \(H^*\) and \(H^*\Theta\). Now (B.PE2) and (B.ZT4) give the two displayed boundaries. Thus \(\Theta\) is a homotopy equivalence without inverting \(\theta\). The inverse \(\upsilon\) is an objectwise witness, not an asserted strictly natural inverse family.

The actual target-side transposes are retained as well:
\[
\begin{aligned}
e_{\zeta_q}&=Ve_q\,\theta_P,\\
e_{t^*}L_1\Theta_q&=Ve_t\,\theta_{W(q)},\\
\beta^*L_1\Theta_q&=V\beta\,\theta_{W(q)}.
\end{aligned}
\tag{B.ZT7}
\]
Each equality is the chain adjunction applied to its defining projection; these are actual maps before restriction, not conclusions from faithfulness of \(U_1\). At an old canonical unit \(e_q=1\), the first map is \(\theta_P\), not an invented identity. In general the unit is not a quasi-isomorphism, and its envelope still uses (B.PE6)--(B.PE7).

**Whole choices over the transported diagram.** Let \(D\) be the supplied decorated diagram over its free parameter index, and \(\rho:R\to WD\) a whole h-projective replacement. Require the whole extension of \(S\) to agree with pointwise transport and preserve whole h-projectivity. Induction along a strict source functor has this property by (B.ND8). For the actual kernel functor \(S=T_{P_u}\), it follows instead from (B.RK1): each kernel column is h-projective, and tensor transport takes a whole representable cell at \((j,X)\) to \(\mathcal J(j,-)\otimes P_u(-,X)\). Hom from this diagram into an acyclic diagram is Hom from the h-projective column into its acyclic value at \(j\). Thus the image cell is whole h-projective. Tensoring the graded-split semifree filtration and using the recursive primitive argument of B.1l proves the assertion for a semifree source; a general h-projective source is homotopy equivalent to such a source. This identifies the whole functor without equating kernel transport with strict-functor induction. Require \(\theta\) to be natural over that same whole index. Then
\[
\begin{aligned}
\rho^\theta&=\Theta_D S\rho:SR\longrightarrow W'T_\theta D,\\
C^{\rho^\theta}&=T_\theta C^\rho.
\end{aligned}
\tag{B.ZT8}
\]
This is a whole quasi-isomorphism: evaluation of \(R\) is h-projective by (B.ND6), and \(WD\) is objectwise h-projective by (B.PE2). Therefore each \(\rho_i\) is a homotopy equivalence. A dg functor preserves those witnesses, and \(\Theta_i\) is a homotopy equivalence by (B.ZT6). This does not claim that induction preserves an arbitrary quasi-isomorphism. It also does not assert that \(WD\) was whole h-projective. An independent whole replacement \(\rho':R'\to W'T_\theta D\) now has this same identified whole target. Apply (B.PE10)--(B.PE13): if \(\rho'a-\rho^\theta=dh\), its comparison-back boundary has all three entries \((r^*h,0,H^*h)\), including the degree-minus-two entry. Bilateral normalization, when supplied, uses the actual graph isomorphisms of (B.ER9), with their seven target labels. It does not create isomorphisms between independently chosen replacement sources.

**A homotopy of left comparisons is generally not strict naturality.** Suppose \(\theta'-\theta=dK\), where \(K\) is a degree-minus-one graded-natural map on the same admitted whole sources. Put
\[
\begin{aligned}
k_q&=\operatorname{Adj}_1(Ve_q\,K_P),\\
B_q&=(1_{SP},1_{VZ},k_q):T_\theta q\longrightarrow T_{\theta'}q,\\
b_K(f)&=(0,0,(-1)^{n+1}\operatorname{Adj}_1(V\beta_f\,K_P)).
\end{aligned}
\tag{B.ZT9}
\]
The graph map \(B_q\) is closed, with inverse obtained from \(-K\). The arrow \(b_K(f)\) has graph degree \(n-1\); its third coordinate has degree \(n-2\). These arrows satisfy
\[
\begin{aligned}
Db_K(f)+b_K(Df)
 &=B_{q'}T_\theta(f)-T_{\theta'}(f)B_q,\\
b_K(gf)
 &=b_K(g)T_\theta(f)+(-1)^{|g|}T_{\theta'}(g)b_K(f),\\
b_K(1)&=0.
\end{aligned}
\tag{B.ZT10}
\]
For the first identity, graded naturality reads
\(K_{P'}L_1Sa=(-1)^nVL_0a\,K_P\).
The transpose of the difference's third component is consequently
\[
(-1)^n V(d\beta_f+\beta_{Df})K_P-V\beta_f\,dK_P.
\tag{B.ZT11}
\]
Taking the differential of the last entry in (B.ZT9), remembering that \(D(0,0,x)=(0,0,-dx)\), and then adding \(b_K(Df)\), gives exactly (B.ZT11). For composition substitute \(\beta_{gf}=\beta_gL_0a+(-1)^{|g|}v\beta_f\). Moving \(K\) past the degree-\(n\) map \(L_1Sa\) supplies \((-1)^n\); the two remaining terms are precisely the two products in (B.ZT10). The unit has \(\beta_1=0\). Thus the sign and degree of this witness are essential, not optional corrections to an otherwise strictly natural family.

These are exactly (B.KC9)'s equations. For a fixed graph object \(Q\), apply the covariant dg functor \(\operatorname{Hom}(Q,-)\) to obtain its left-module comparison, and then use the signed length-one bar map (B.KC10). Its quasi-isomorphism conclusion retains that proposition's h-projective right-module hypothesis. If a contravariant Hom realization is used instead, the opposite-category signs of (B.KC11) must be inserted. This passage supplies a witnessed bar comparison, not permission to erase \(b_K\). For successive \(K\) and \(K'\), from \(\theta\) to \(\theta'\) and then to \(\theta''\), direct graph multiplication gives
\[
\begin{aligned}
B^{K+K'}_q&=B^{K'}_qB^K_q,\\
b_{K+K'}(f)&=b_{K'}(f)B^K_q+B^{K'}_{q'}b_K(f).
\end{aligned}
\tag{B.ZT12}
\]
The first equation adds the two third coordinates; in the second, each zero source and target component leaves only its displayed third coordinate. Higher homotopies between these choices still require their own relative boundary equations.

**Vertical pasting uses the same receiving envelope.** For a second comparison \(\theta_2:L_2S_2\to V_2L_1\), define \(\theta_{21}=V_2\theta_1\,\theta_{2,S_1}\). With the canonical ordered induction associators,
\[
\begin{aligned}
T_{\theta_2}T_{\theta_1}&=T_{\theta_{21}},\\
\Theta^{21}_q&=\Theta^2_{T_{\theta_1}q}\,S_2\Theta^1_q.
\end{aligned}
\tag{B.ZT13}
\]
The first equality follows by transposing twice in (B.ZT2): the intermediate transpose is exactly \(V_1e_q\theta_{1,P}\), or \(V_1\beta_f\theta_{1,P}\) for the witness. For the second project first to the source, giving \(S_2S_1r\). Transpose the second projection. Naturality of \(\theta_2\) on the closed map \(\Theta^1_q\), followed by (B.ZT7), gives \(V_2V_1e_t\,V_2\theta_{1,W}\theta_{2,S_1W}\). The third projection is the same calculation with \(\beta\), so all three agree. This proof never evaluates a comparison on an unresolved target. The unit comparison gives the identity, and ordered tensor associativity proves the corresponding equality for every finite vertical string. This is vertical pasting; the nested horizontal coefficient in (B.BM18) remains separate.

The envelope comparison and its actual target square are
\[
\begin{array}{ccc}
T_\theta FD&\xrightarrow{\ \tau_D\ }&F'T_\theta D\\
{T_\theta C_D}\downarrow&&\downarrow{C^*_D}\\
T_\theta D&\xrightarrow{\ 1\ }&T_\theta D.
\end{array}
\tag{B.ZT14}
\]
It commutes strictly. Replacing its top sources by independent whole choices introduces precisely the second comparison witness in (B.ZT8), not a new assertion that their chosen chain models coincide.

**Exact geometric application and the remaining boundary.** In (B.KC15)--(B.KC16), use the actual whole right kernels and the specified inverse: \(L_0=T_{H_f}\), \(L_1=T_{H_{f'}}\), \(S=T_{P_u}\), and \(V=T_{P_g}\). Admit the whole h-projective kernel sources and their induction models already constructed there. The inverse is chosen in the whole kernel Hom complex with both inverse homotopies, so the required source naturality is retained. Its resolved transpose is exactly (B.BM16), and (B.ZT7) is exactly the last equation of (B.KC16). The actual proper--open replacement edges remain the ones in (B.KC4), (B.KC6)--(B.KC7), and (B.GC13); they have not been replaced by abstract isomorphism classes.

In particular, if \(r_1c-\zeta_q=db\), the right-mate comparison is the closed decorated arrow \((c,1,b):T_\theta q\to r_1\). Apply the envelope functor to this **arrow**, retaining \(b\). Unless \(c\) is separately proved a homotopy equivalence, its envelopes are not thereby interchangeable as replacement targets. Equation (B.ZT6) does not imply that the right mate is invertible. The vertical witness in (B.BM17) is retained after transporting the first counit homotopy; the nested horizontal witness is still the two-term expression in (B.BM18), with the second coefficient (B.MX12). Its shared boundaries with (B.GC12)--(B.GC13) and the four-face diagram must be checked over the actual changing index before invoking (B.ND9). The formulas above give transport and comparisons on resolved inputs; they do not establish that full assembly. Geometric nearby multiplicative descent, whole coefficient transport and rationalization with derived limits and strict-heart effacement are not established by this construction. \(\square\)



### Lift changing diagrams without inverting comparison arrows

**Proposition B.1au (resolve the receiving envelope, not the comparison arrow).** Over a specified common free parameter index and receiving adjunction model, independently chosen whole path-envelope replacements admit a dg projection onto the category of actual decorated diagrams. This projection is surjective and a quasi-isomorphism on Hom complexes even when the base comparison arrow is not invertible. It lifts any supplied relative free diagram, retaining its actual target maps and a second comparison-back witness. Applied to the typed four-face and cube provider, it preserves every supplied boundary. It does not construct a missing geometric base face or turn a homotopy-natural family into a strict natural map by forgetting its witnesses.

**Objects and their receiving targets.** Fix the receiving dg functor \(U\) and a free index \(\mathcal J\) as in B.1ar. Let \(\mathcal B\) be the small labelled dg category of the admitted diagrams \(D:\mathcal J\to\mathcal A_U\), whose source modules are h-projective at each value; its arrows are the full graded natural transformations. In particular target-side maps are retained before restriction. For every chosen object use a whole h-projective replacement
\[
\rho_i:R_i\xrightarrow{\simeq}WD_i,
\qquad
q_i^\rho=t_i\rho_i,
\qquad
C_i^\rho=(r_i\rho_i,1,H_i\rho_i).
\tag{B.CE1}
\]
These are the whole diagrams of (B.PE8), not just unrelated objectwise resolutions. The whole source \(R_i\) exists by (B.ND5). Every value is h-projective by (B.ND6). The comparison \(C_i^\rho\) is strictly natural over \(\mathcal J\) and an objectwise graph homotopy equivalence by (B.PE9). It is not asserted to have a whole strictly natural homotopy inverse. No quasi-isomorphism assumption is made on the original structure maps of \(D_i\), including its unit vertices.

Make a dg category \(\mathcal R_W\) of these pairs \((D_i,\rho_i)\). A degree-\(n\) arrow is \(x=(f,a,h)\), where \(f:D_0\to D_1\) is a degree-\(n\) graded natural decorated arrow, \(a:R_0\to R_1\) has degree \(n\), and \(h:R_0\to WD_1\) has degree \(n-1\). The last two are whole graded natural maps. Define
\[
\begin{aligned}
Dx&=(Df,da,\rho_1a-W(f)\rho_0-dh),\\
\pi(x)&=f.
\end{aligned}
\tag{B.CE2}
\]
For \(x=(f,a,h)\) of degree \(n\) and \(y=(g,b,k)\) of degree \(m\), put
\[
yx=(gf,ba,ka+(-1)^mW(g)h),
\qquad 1_{(D,\rho)}=(1_D,1_R,0).
\tag{B.CE3}
\]
These are the arrow-graph formulas applied to the strict dg functor \(W\). Its source map is retained as the full \(f\), not recovered from \(W(f)\). Expanding the third differential uses \(dW(f)=W(Df)\), \(d\rho_i=0\), and the ordinary Hom Leibniz rule; its cross terms cancel, giving \(D^2=0\) and the graded product rule. The three terms of a triple product have coefficients \(1,(-1)^{|z|},(-1)^{|z|+|y|}\), proving associativity. Units follow directly. Thus \(\pi\) is a strict dg functor, whether or not \(W\) or \(U\) is faithful.

Projection is degreewise surjective: \((f,0,0)\) is a graded lift of any \(f\). Its Hom kernel is
\[
\begin{aligned}
\ker\pi^n&=\operatorname{Hom}^n(R_0,R_1)
 \oplus\operatorname{Hom}^{n-1}(R_0,WD_1),\\
d(a,h)&=(da,\rho_1a-dh).
\end{aligned}
\tag{B.CE4}
\]
All Hom complexes here are whole natural Hom complexes over the index-product category. Postcomposition by \(\rho_1\) is a quasi-isomorphism on them by (B.ND7), since \(R_0\) is whole h-projective and \(\rho_1\) is objectwise a quasi-isomorphism. Its shifted cone (B.CE4) is therefore acyclic. The map used in this argument is \(\rho_1\), **not** \(q_1\), \(t_1\rho_1\), a unit, or the base comparison \(f\). This is the reason a noninvertible right mate presents no obstruction to lifting its arrow.

**The lifted decorated diagram and its full comparison back.** Write \(f=(a_f,w_f,h_f)\) at each parameter value. There is a strict dg functor into the category of whole decorated diagrams,
\[
\Phi(D_i,\rho_i)=D_i^\rho,
\qquad
\Phi(f,a,h)=(a,w_f,t_1h).
\tag{B.CE5}
\]
For the differential, use \(t_1W(f)=U(w_f)t_0\); applying \(t_1\) to the third coordinate in (B.CE2) gives exactly the graph differential of (B.CE5). The same identity proves preservation of (B.CE3). Whole graded naturality also holds: for an index arrow of degree \(l\), \(h\) moves past it with \((-1)^{(n-1)l}\), exactly the product of the graph's third-coordinate sign \((-1)^l\) and the degree-\(n\) naturality sign \((-1)^{nl}\). This retains \(w_f\) itself, not only its image under \(U\).

For every homogeneous \(x\), define the degree-\(n-1\) decorated map
\[
B(x)=(r_1h,0,H_1h):D_0^\rho\longrightarrow D_1.
\tag{B.CE6}
\]
Its third coordinate has degree \(n-2\). This is a whole graded natural map even though \(H_1\) alone is not natural. Indeed substitute
\(H_{1,j}W(D_1(u))=h_{D_1(u)}r_{1,i}+(-1)^{|u|}U(w_{D_1(u)})H_{1,i}\)
from (B.PE4), and then the graded naturality of \(h\). The two terms are precisely those in the graph product with \(B(x)\). Direct computation gives
\[
\begin{aligned}
DB(x)+B(Dx)&=C_1^\rho\Phi(x)-fC_0^\rho,\\
B(yx)&=B(y)\Phi(x)+(-1)^m gB(x),\\
B(1)&=0.
\end{aligned}
\tag{B.CE7}
\]
For the first equation the source component reduces to \(r_1\rho_1a-r_1W(f)\rho_0\). The third component is
\(t_1h+H_1(\rho_1a-W(f)\rho_0)\), using \(dH_1=q_1r_1-t_1\). Equation (B.PE4) identifies it with the third component on the right, including \(h_fr_0\rho_0\) and its signed target term. The target components cancel before restriction. For the product equation, its third component follows from
\(H_2W(g)h=h_gr_1h+(-1)^mU(w_g)H_1h\).
The term involving \(h_g\) must be retained; deleting the base graph homotopy would change the product law. These are also the algebraic comparison equations of (B.KC9). Any use of its bar comparison still retains (B.KC10)'s source-projectivity and (B.KC11)'s variance hypotheses.

**A single arrow, then its composites.** For a closed degree-zero \(f:D_0\to D_1\), (B.ND7) lifts the actual whole map \(W(f)\rho_0\). Choose
\[
\begin{aligned}
da&=0,&\rho_1a-W(f)\rho_0&=dh,\\
\widetilde f&=(a,w_f,t_1h),\\
C_1^\rho\widetilde f-fC_0^\rho&=D(r_1h,0,H_1h).
\end{aligned}
\tag{B.CE8}
\]
The target is still \(WD_1\), not an identification of \(WD_0\) with \(WD_1\). The source map \(a\) need not be a quasi-isomorphism. In particular the inverse witnesses for the envelope itself in (B.ZT6) do not supply an inverse to \(\widetilde f\).

If \(x,y\) are closed lifts of \(f,g\), and \(z\) is an independently chosen closed lift of the **same actual composite** \(gf\), then \(yx-z\) is a closed kernel element. Acyclicity gives a degree-minus-one \(K\) with
\[
\begin{aligned}
DK&=yx-z,&\pi K&=0,\\
D\Phi(K)&=\Phi(y)\Phi(x)-\Phi(z),\\
DB(K)&=C_2^\rho\Phi(K)-B(yx)+B(z).
\end{aligned}
\tag{B.CE9}
\]
The last equation is (B.CE7) applied to \(K\). Here \(B(K)\) has degree minus two, with a degree-minus-three third coordinate. It is the compatibility witness between the two comparison-back homotopies. Comparing different geometric base composites instead requires their actual supplied base comparison; a zero-base kernel filler cannot establish that missing fact.

**Every specified relative free boundary is lifted, not guessed.** Let \(\mathcal K\) be obtained from \(\mathcal K_0\) by freely adjoining homogeneous generators in well-founded order, with their differentials in earlier stages. Let \(E:\mathcal K\to\mathcal B\) be the supplied strict base diagram and suppose its already fixed boundary has a compatible lift into \(\mathcal R_W\). At a degree-\(n\) generator \(v\), take any graded lift \(x_0\) of \(E(v)\). If \(L\) is the earlier lift, set
\[
\delta=Dx_0-L(dv),\qquad
\pi\delta=0,\quad D\delta=0,\qquad
DK=\delta,\quad L(v)=x_0-K.
\tag{B.CE10}
\]
The cycle condition uses the **checked** differential of the free presentation and the earlier dg lift: \(D L(dv)=L(d^2v)=0\). The kernel primitive \(K\) has degree \(n\) and exists by (B.CE4). Extend multiplicatively; identities stay the identities of (B.CE3). At a limit stage retain all earlier assignments. This is the concrete relative construction of (B.ND9), now over actual changing diagrams instead of the scalar-only projection of (B.PE12). Applying \(\Phi\) and (B.CE7) retains every higher comparison and its compatible comparison back. It is not a claim that a nonfree quotient or an unverified boundary admits such a lift.

For the existing seven labelled objects, take the actual targets of (B.FT3), the four decorated faces and the endpoint bridge checked in (B.FT4), and the full cube checked in (B.FT5). In its supplied free presentation, (B.CE10) can keep already chosen lower faces fixed. The retained base coordinate of the lifted cube is exactly the original \(\mathbf P(f_H)\), including its degree-minus-four third coordinate. The new source maps and witnesses are chosen to satisfy that full boundary, not just its image after restriction. The target component of every \(\Phi(x)\) remains \(w_f\), so neither \(\beta\) nor \(\bar\gamma\) is erased. The finite diagnostic accompanying this construction uses independent resolution models at all seven objects, lifts the supplied lower and upper faces before the change faces, and finally lifts the full cube with its given differential. It checks these algebraic identities, not the separate geometric identification of a new overlap diagram.

**Change the parameter index without assuming projectivity survives restriction.** For a dg functor \(\psi:\mathcal J'\to\mathcal J\), where \(\mathcal J'\) is again an admitted free index, restriction is pointwise. It commutes with \(W\) and preserves objectwise quasi-isomorphisms, but need not preserve whole h-projectivity. Instead choose a new whole h-projective replacement \(\lambda:R^\psi\to\psi^*R\) by (B.ND5), and set
\[
\begin{aligned}
\rho^\psi&=(\psi^*\rho)\lambda:
 R^\psi\longrightarrow W(\psi^*D),\\
I_\lambda&=(\lambda,1,0):
 (\psi^*D)^{\rho^\psi}\longrightarrow\psi^*(D^\rho),\\
(\psi^*C^\rho)I_\lambda&=C^{\rho^\psi}.
\end{aligned}
\tag{B.CE11}
\]
The first map is an objectwise quasi-isomorphism and its source is whole h-projective over the **new** index. Each value of \(\psi^*R\) is h-projective because it is a value of \(R\); hence each \(\lambda\) is a homotopy equivalence. The proof of (B.PE9) applied valuewise makes \(I_\lambda\) an objectwise graph homotopy equivalence. Its source, target and third coordinates give the last equality directly. No inverse of a unit and no assertion about \(\psi\otimes1\) being a quasi-equivalence is used.

For two restrictions, compose the two actual maps to the restricted old source: \((\chi^*\lambda_\psi)\lambda_\chi\). The resulting envelope map and an independently chosen replacement for \((\psi\chi)^*D\) have the same literal receiving envelope. Equations (B.PE10)--(B.PE13), or the identity-base case of (B.CE2)--(B.CE10), compare them with all specified relative free choice boundaries. Do not replace this re-resolution by a claim that the initially restricted source is already whole h-projective.

**Bind the noninvertible geometric arrows.** For the actual (B.KC16) or (B.BM16) data, the closed arrow to be lifted is
\[
f_{\mathrm{bc}}=(c,1,b):T_\theta q_0\longrightarrow r_1,
\qquad r_1c-\zeta_{q_0}=db.
\tag{B.CE12}
\]
Both objects are in the same receiving \(\mathcal A_{U_1}\) after the resolved transport of B.1at. Use its supplied whole parameter scope; for a single instance the index has one object. Equation (B.CE8) applies to this actual arrow even if \(c\) is not a quasi-isomorphism. The two independently chosen envelopes are distinct receiving objects connected by \(W(f_{\mathrm{bc}})\), not silently equated. This is also valid at non-quasi-isomorphic unit structure maps, because the acyclic projection still uses the whole envelope replacement \(\rho_1\).

For two geometric base changes, work in the final receiving category. The three objects are \(T_{\theta_{21}}q_0\), \(T_{\theta_2}q_1\), and \(q_2\). The actual composite of \(T_{\theta_2}f_1\) with \(f_2\) is
\[
\begin{aligned}
c_{21}&=c_2S_2c_1,\\
b_{21}&=b_2S_2c_1+
 \operatorname{Adj}_2(V_2D_1\,\theta_{2,S_1P_0}),\\
D_1&=\varepsilon^1 L_1b_1.
\end{aligned}
\tag{B.CE13}
\]
This is exactly (B.BM17), using (B.ZT2) on the first arrow's third coordinate and (B.ZT13) on its source object. Thus the replacement-level composition comparison (B.CE9) has a specified geometric base composite. A different independently chosen geometric arrow must first be related to that base composite by its actual Hom witness; it is not automatically the same arrow. Horizontal composition still retains (B.BM18)'s nested two-term witness and the second folding coefficient (B.MX12).

For any one closed lifted comparison the full square is
\[
\begin{array}{ccc}
D_0^\rho&\xrightarrow{\ \Phi(x)\ }&D_1^\rho\\
{C_0^\rho}\downarrow&&\downarrow{C_1^\rho}\\
D_0&\xrightarrow{\ f\ }&D_1,
\end{array}
\qquad C_1^\rho\Phi(x)-fC_0^\rho=DB(x).
\tag{B.CE14}
\]
The bottom arrow may be noninvertible. The square is witnessed, not strictly commutative, and (B.CE9)--(B.CE10) keep its higher comparisons compatible.

**Changing geometric presentations.** The common receiving models for actual noninvertible comparison arrows, independently selected whole resolutions, and index re-restrictions are given by the preceding construction. To use this across changing geometric presentations, first put their maps in the actual common receiving category via the checked B.1as--B.1at transports and their specified index maps. The family \(B_q\) from (B.ZT9) is generally not strictly natural; retain (B.ZT10)'s witness and its actual strict bar/free roof before treating it as a map of whole diagrams. The geometric (B.GC13) edge, the nested (B.MX12) coefficient and their higher shared boundaries must be verified in that base presentation. Surjectivity of \(\pi\) cannot create a missing geometric face or certify an unchecked relation. Full changing-model horizontal/composition assembly, nearby-cycle multiplicative descent, normalized coefficient completion and rationalization with derived limits and strict-heart higher effacement are not established by this construction. \(\square\)



### Strictify the recorded comparison homotopy on a free cylinder

**Proposition B.1av (a strict common index retains the naturality defect).** The actual comparison of B.1at, including its arrow witness (B.ZT10), has an explicit common strict dg parameter cylinder whenever its parameter category is presented semifreely. Both endpoint sections of this cylinder are quasi-equivalences. Its realization in the receiving decorated category retains the actual target maps and the full comparison homotopy. The construction works over any commutative coefficient ring and for unbounded Hom complexes. It requires neither a tensor-flatness hypothesis nor a strict naturality assertion about the original comparison. It supplies the strict roof for the comparison described at the end of B.1au; separately prescribed geometric higher boundaries still have to satisfy their compatibility equations.

**The comparison data and normalization.** Let \(\mathcal A\) be a small semifree dg category: its underlying graded category is free on homogeneous generators in a well-founded order, and each generator's differential is a finite linear combination of earlier paths, possibly including identities. Let \(N_0,N_1:\mathcal A\to\mathcal E\) be strict dg functors, with closed degree-zero objectwise isomorphisms \(B_a:N_0a\to N_1a\). Suppose the supplied linear arrow assignment \(b_f:N_0a\to N_1b\), of degree \(|f|-1\) for \(f:a\to b\), satisfies
\[
\begin{aligned}
D b_f+b_{df}&=B_bN_0(f)-N_1(f)B_a,\\
b_{gf}&=b_gN_0(f)+(-1)^{|g|}N_1(g)b_f,
\qquad b_1=0.
\end{aligned}
\tag{B.CY1}
\]
These are the exact identities (B.KC9) and (B.ZT10), not just an equality on closed arrows in the homotopy category. For B.1at use \(N_0=T_\theta D\), \(N_1=T_{\theta'}D\), \(B_a=B_{D(a)}\), and \(b_f=b_K(D(f))\) for the actual parameter diagram \(D\). The inverse of each \(B_a\) is its explicit graph arrow with \(-k_{D(a)}\). Thus the isomorphism hypothesis is satisfied here; an arbitrary objectwise homotopy equivalence is not silently given a strict inverse.

Conjugate the second diagram onto the first diagram's objects, putting
\[
\begin{aligned}
\overline N_1(a)&=N_0(a),&
\overline N_1(f)&=B_b^{-1}N_1(f)B_a,\\
h_f&=B_b^{-1}b_f.
\end{aligned}
\tag{B.CY2}
\]
Closedness and the inverse identities for \(B\) show directly that \(\overline N_1\) is a strict dg functor. Multiplying (B.CY1) by \(B_b^{-1}\) gives
\[
\begin{aligned}
D h_f+h_{df}&=N_0(f)-\overline N_1(f),\\
h_{gf}&=h_gN_0(f)+(-1)^{|g|}\overline N_1(g)h_f,
\qquad h_1=0.
\end{aligned}
\tag{B.CY3}
\]
The family \(B\) is strictly natural from \(\overline N_1\) to \(N_1\) by definition. It is **not strictly natural from** \(N_0\) to \(N_1\) in general. Normalization has not asserted that \(h\) or \(b\) vanishes.

**Adjoin contractible pairs, not new relations.** Form \(C\mathcal A\) with the same objects, the copy \(i_0\mathcal A\), and two free arrows for each original generator \(t:a\to b\) of degree \(n\):
\[
\begin{aligned}
z_t,v_t &:a\longrightarrow b,&
|z_t|&=n-1,& |v_t|&=n,\\
dz_t&=-v_t,&dv_t&=0.
\end{aligned}
\tag{B.CY4}
\]
There are no quotient relations beyond linearity, units and the free category laws. Extend the differential by the graded Leibniz rule. It squares to zero because it does on the old generators and on each new pair. This is again semifree: retain the order of the old generators and put each \(v_t\) before \(z_t\); the new pair differentials involve no old or later generators.

Define a second section \(i_1\) and a degree-minus-one linear assignment \(H\) recursively by
\[
\begin{aligned}
H(t)&=z_t,&H(1)&=0,\\
H(gf)&=H(g)i_0(f)+(-1)^{|g|}i_1(g)H(f),\\
i_1(t)&=i_0(t)+v_t-H(dt).
\end{aligned}
\tag{B.CY5}
\]
The value \(H(dt)\) uses only earlier generators, so the definition is well founded, even if \(dt\) contains a scalar identity. Extend \(i_1\) multiplicatively and preserve units. The product rule for \(H\) is unambiguous on free paths: expanding a triple product in either order has the three signs \(1,(-1)^{|g|},(-1)^{|g|+|f|}\) in left-to-right notation. By induction on the original generators,
\[
di_1(f)=i_1(df),\qquad
dH(f)+H(df)=i_0(f)-i_1(f).
\tag{B.CY6}
\]
Indeed assume both identities on earlier generators and their paths. Then
\(di_1(t)=i_0(dt)-dH(dt)=i_1(dt)\), since \(d^2t=0\). The homotopy identity on \(t\) is \(-v_t+H(dt)=i_0(t)-i_1(t)\), precisely (B.CY5). For a product, expand its differential and (B.CY5); the terms involving \(H\) of a differential cancel with opposite Leibniz signs, leaving the product difference. Thus both identities extend to every path and finite linear combination. Limit stages take the union of earlier assignments. The nonlinear correction \(-H(dt)\) is necessary; merely using \(i_0(t)+v_t\) generally fails to give a chain map.

The strict collapse is
\[
p:C\mathcal A\longrightarrow\mathcal A,
\qquad pi_0=pi_1=1,\qquad p(z_t)=p(v_t)=0.
\tag{B.CY7}
\]
Its compatibility with the differential follows from (B.CY4); its second section identity follows inductively from (B.CY5), because every term of \(H\) contains a new letter.

**A contraction on actual Hom complexes.** Write a nonempty free word with new letters uniquely as old path segments separated by single new letters. Differential preserves the number of new letters. On words containing a new letter define a degree-minus-one operator \(S\) by acting on the **first new letter**, reading the written product from left to right. If that letter is \(v_t\), replace it by \(-z_t\) and multiply by \((-1)^{|u|}\), where \(u\) is the entire old prefix; if it is \(z_t\), set the value to zero. Set \(S=0\) on old words and extend linearly. Then
\[
dS+Sd=1-i_0p,
\qquad S^2=0,\quad pS=0,\quad Si_0=0.
\tag{B.CY8}
\]
For the identity, the two-letter complex has contraction \(v_t\mapsto-z_t\), \(z_t\mapsto0\), since \(d(-z_t)=v_t\). A differential in the old prefix changes its degree by one, so its two contributions to \(dS+Sd\) cancel. A differential after the first new letter cancels because \(S\) lowers the degree of that letter by one. The remaining contribution is exactly the original word, whether the first new letter is \(v_t\) or \(z_t\). Old-only words contribute zero on both sides. This calculation also allows a prefix differential to produce an identity: total degree and the unique empty old segment are retained. The three side identities follow from the definition. Every word and every differential expression is finite; no infinite summation or completion is used. In particular this is an actual contraction over the coefficient ring, not a tensor-exactness or spectral-convergence argument.

It follows that \(p\) is a quasi-isomorphism on each Hom complex. It is the identity on objects, hence a dg quasi-equivalence. Both \(i_0\) and \(i_1\) are quasi-equivalences, since their composites with \(p\) are the identity. They are not claimed to be identical or strict inverses to \(p\).

**Realize the given homotopy, including all free paths.** There is a strict dg functor \(F:C\mathcal A\to\mathcal E\) defined by
\[
F i_0=N_0,\qquad
F(z_t)=h_t,\qquad F(v_t)=-D h_t.
\tag{B.CY9}
\]
The differential relations hold: \(F(dz_t)=-F(v_t)=D h_t\) and \(D F(v_t)=0\). Induction in (B.CY5), using (B.CY3), gives \(F H(f)=h_f\) and \(F i_1=\overline N_1\) for every arrow, not only for the original generators. Indeed the endpoint formula on \(t\) becomes \(N_0(t)-D h_t-h_{dt}=\overline N_1(t)\), and the two product rules agree. The strict common-index diagram is therefore
\[
\begin{array}{ccccc}
\mathcal A&\xrightarrow{\ i_0\ }&C\mathcal A
 &\xleftarrow{\ i_1\ }&\mathcal A\\
&&\downarrow F&&\\
&&\mathcal E&&
\end{array}
\quad
Fi_0=N_0,\qquad Fi_1=\overline N_1
 \xrightarrow[\cong]{\ B\ }N_1.
\tag{B.CY10}
\]
The arrow labelled \(B\) is an isomorphism of diagrams on the right endpoint index, not an additional strict equality of the left and right restrictions. The collapse \(p\) of (B.CY7) is a strict quasi-equivalence back to either endpoint index. Thus the actual diagrams may be compared through one strict common parameter category. Their non-strict comparison remains present as \(F(z_t)=h_t\); erasing the new generators would erase the datum the cylinder was built to retain. Induction of modules uses these strict dg functors, subject to the replacement requirements of B.1m and B.1s, not the original non-strict family as if it were a strict functor.

If the given index is not semifree, first precompose both diagrams and all the comparison data with the **same** strict \(q:Q\mathcal A\to\mathcal A\) of (B.SF1). Its staged construction is semifree and a quasi-equivalence even when the original units do not split. Apply the present construction to \(Q\mathcal A\). This gives a common free roof, not a claimed extension over relations of the original category. If lower geometric boundaries were already fixed, their exact pullbacks must be retained; this construction does not assert an unproved relative extension of independently prescribed data.

**Actual whole inverse choices and geometric scope.** For the same whole comparison \(\beta:A\to B\) of (B.KC15), let its supplied whole inverse choices \(\theta_i:B\to A\) have witnesses
\(dA_i=\beta\theta_i-1_B\) and \(dB_i=\theta_i\beta-1_A\). Their explicit comparison is
\[
K_{ij}=\theta_i A_j-B_i\theta_j,
\qquad dK_{ij}=\theta_j-\theta_i.
\tag{B.CY11}
\]
The differential of the first term is \(\theta_i\beta\theta_j-\theta_i\), and that of the second is \(\theta_i\beta\theta_j-\theta_j\), proving the equation. These are whole homogeneous maps before evaluation, so they give the required graded natural \(K\) on the admitted h-projective inputs. No comparison is evaluated on an unresolved \(U(Z)\). If a particular \(K_{ij}\) has already been prescribed by a geometric face, use that datum instead; a different formula with the same differential is not automatically equal or homotopic to it. In particular this construction does not supply a prescribed higher boundary among three or more inverse choices merely from pairwise existence.

For the actual (B.ZT9)--(B.ZT10) family, \(B\) has identity source and target components and \(b_f\) has only its third component. Hence \(h_f=B^{-1}b_f\) still has zero source and target components. Its differential also does. If \(J:\mathcal A_{U_1}\to\mathcal T_1\) denotes the functor retaining the **actual** target coordinate, then
\[
JF=(JN_0)p,\qquad
J F(z_t)=J F(v_t)=0.
\tag{B.CY12}
\]
These equalities hold before applying \(U_1\), with no faithfulness assumption. All object values of \(F\) are the admitted \(N_0(a)\), so their source modules remain h-projective. Whole projectivity over the enlarged parameter category is a separate matter: choose the whole replacement over \(C\mathcal A\) using (B.ND5), and after either endpoint restriction use (B.CE11)'s whole re-resolution. Do not infer preservation of whole projectivity from the fact that the section is a quasi-equivalence. Once a strict relative base diagram and its boundaries are actually supplied, (B.CE10) lifts it to independently selected whole envelope models.

The common receiving presentation requires the actual (B.GC13) horizontal edge, the nested (B.MX12) coefficient and their prescribed shared higher boundaries. The bounded strictification above does not establish the full changing-model geometric multiplication, nearby-cycle descent, completed coefficient transport or strict-heart higher effacement. \(\square\)



### Place the horizontal mate in the actual nested graph

**Proposition B.1aw (the resolved horizontal mate is one nested arrow).** The horizontal comparison (B.BM18), with its actual left comparisons and independently selected receiving replacements, is a closed arrow in a single decorated nested graph. Its image under the original two-stage fold is exactly the displayed horizontal mate, including both witness terms. The same presentation retains (B.MX12) on composable homogeneous arrows and admits a strict receiving functor from its free bar resolution. The receiving functor is not asserted to be a quasi-equivalence: the transported source structure maps need not be quasi-isomorphisms. This joins the actual mate to the supplied fold, beyond the identical-adjunction specialization used to identify the coefficients after (B.HS9).

**Use a decorated graph, not only a graph of replacements.** Fix dg adjunctions \(L\dashv U\) and \(M\dashv W\), in the strict common models already used above. Write \(\mathcal N_{U,W}\) for the small labelled category of admitted objects
\[
 X=(Z,R,N;t,r),\qquad
 Z\xrightarrow{\ t\ }UR\xrightarrow{\ U r\ }UWN,
 \qquad r:R\longrightarrow WN.
\tag{B.HN1}
\]
Here \(Z,R\) are the specified h-projective source modules and \(t,r\) are closed degree-zero maps; neither structure map is required to be a quasi-isomorphism. Work in the whole parameter module categories when parameters are present. Labels and the actual terminal object \(N\) are retained, not identified whenever their restrictions happen to agree. A homogeneous arrow of degree \(n\) is
\[
\begin{aligned}
x&=(a,b,w;h,k):X\longrightarrow X',\\
a &:Z\to Z',\quad b:R\to R',\quad w:N\to N',\\
h &:Z\to UR'\ [n-1],\qquad k:R\to WN'\ [n-1].
\end{aligned}
\tag{B.HN2}
\]
The three vertex maps have degree \(n\). The brackets in the last line specify the degree of the maps, not a change of endpoint object. Keep \(w\) before applying \(W\) or \(UW\); no faithfulness assumption is made.

Use exactly the graph differential and product of (B.IA10), now in the order (source, intermediate, actual target). For \(y:X'\to X''\) of degree \(m\),
\[
\begin{aligned}
Dx&=(da,db,dw;\ t'a-U(b)t-dh,\ r'b-W(w)r-dk),\\
yx&=(a_y a,b_y b,w_y w;\ h_y a+(-1)^mU(b_y)h,\\
 &\hspace{12em} k_y b+(-1)^mW(w_y)k).
\end{aligned}
\tag{B.HN3}
\]
Identities have identity vertex maps and zero witnesses. Each edge is an ordinary decorated arrow graph (B.FT2), so its differential square, signed Leibniz rule and associativity hold componentwise. The two edges share the same intermediate vertex map, whose ordinary differential and product agree on both sides. This proves the dg laws on the fibre product, without any acyclicity inference from \(t\) or \(r\).

**The existing fold on this larger receiving category.** Define the object value \(F_0X=(Z,N,U(r)t)\) in \(\mathcal A_{UW}\). The coefficients, with the suspended convention (B.RS7), are
\[
\begin{aligned}
F_1(x)&=(a,w,\ U(r')h+U(k)t),\\
F_2(y,x)&=(0,0,U(k_y)h),\qquad F_j=0\quad(j>2).
\end{aligned}
\tag{B.HN4}
\]
This is (B.IA12)/(B.MX12), with the vertex order stated explicitly. To apply its selected-edge proof, send (B.HN1) to the two-edge string \(Z\to UR\to UWN\); send vertices to \(a,U(b),UW(w)\) and witnesses to \(h,U(k)\). This assignment respects (B.HN3). The proof of (B.RS8) is algebraic and does not use quasi-isomorphisms or projectivity of \(UR\). Its terminal differential and product are the images of the retained actual \(w\), and both higher terminal coordinates are zero already in the terminal category. Thus it proves the equations in the decorated target, not just after forgetting its terminal coordinate.

In particular \(DF_1=F_1D\). The two-input equation, useful for checking the sign of a composition witness, is
\[
\begin{aligned}
DF_2(y,x)
 &=F_2(Dy,x)+(-1)^{m-1}F_2(y,Dx)\\
 &\quad+(-1)^m\bigl(F_1(y)F_1(x)-F_1(yx)\bigr).
\end{aligned}
\tag{B.HN5}
\]
For closed inputs the witness for \(F_1(yx)-F_1(y)F_1(x)\) is therefore \((-1)^{m+1}F_2(y,x)\), not its unsigned negative in every degree. At three inputs the identity is the cancellation
\(F_2(zy,x)-F_1(z)F_2(y,x)=(-1)^{m-1}(F_2(z,y)F_1(x)-F_2(z,yx))\).
For example, expanding either side leaves \(U(k_z)U(b_y)h_x\). At four inputs the only possible nonzero product is a product of two pure third-coordinate maps, hence zero. Above four inputs all terms vanish. This also checks the higher identities directly in the two-stage case. Higher coefficients vanish on a unit because its edge witnesses vanish.

**Locate the actual source of (B.BM18).** Restore subscripts \(0,1\) on both adjunctions. Keep its actual induction functors and closed comparisons
\(\theta:L_1S\to TL_0\), \(\phi:M_1T\to VM_0\), and \(\Xi=(\phi L_0)(M_1\theta)\) in this order. Starting with \(t:Z\to U_0R\), \(r:R\to W_0N\), use their specified counit transposes
\(e_L:L_0Z\to R\), \(e_M:M_0R\to N\). Put
\[
\begin{aligned}
A&=T(e_L)\theta_Z:L_1SZ\longrightarrow TR,\\
B&=V(e_M)\phi_R:M_1TR\longrightarrow VN,\\
\chi&=\operatorname{Adj}_{L_1}(A):SZ\longrightarrow U_1TR,\\
\zeta_\nu&=\operatorname{Adj}_{M_1}(B):TR\longrightarrow W_1VN,\\
X&=(SZ,TR,VN;\chi,\zeta_\nu)\ \in\mathcal N_{U_1,W_1}.
\end{aligned}
\tag{B.HN6}
\]
The required h-projectivity of \(SZ\) and \(TR\) is the admitted induction/whole-module hypothesis, as in B.1at, not a claim about unresolved right-adjoint values. Its structure maps need not be quasi-isomorphisms. Its terminal object is \(VN\), not an object inferred from \(U_1W_1VN\).

The source of the folded arrow is the *actual* composite transpose. Indeed the successive Hom adjunctions give
\[
\begin{aligned}
U_1(\zeta_\nu)\chi
 &=\operatorname{Adj}_{M_1L_1}\bigl(B\,M_1(A)\bigr)\\
 &=\operatorname{Adj}_{M_1L_1}
       \bigl(V(e_M M_0e_L)\,\Xi_Z\bigr)
 =\zeta_\Xi.
\end{aligned}
\tag{B.HN7}
\]
For the first equality transpose under \(L_1\): naturality of that adjunction identifies the transpose with \(\zeta_\nu A\); transposing under \(M_1\) gives \(B M_1(A)\). For the second use
\(\phi_R M_1T(e_L)=VM_0(e_L)\phi_{L_0Z}\).
Both inputs of \(\phi\) are admitted h-projectives. Thus the equality uses the actual counits, units and the given naturality, not a formal resemblance between two ladders.

Let \(Y=(Z',R',VN;t',r')\) be the receiving nested replacements from (B.BM18). Its chosen closed maps and degree-minus-one witnesses satisfy
\[
\begin{aligned}
r'c_\nu-\zeta_\nu&=db_\nu,\\
t'c_\psi-U_1(c_\nu)\chi&=db_\psi,\\
x&=(c_\psi,c_\nu,1_{VN};b_\psi,b_\nu):X\longrightarrow Y,
\qquad Dx=0.
\end{aligned}
\tag{B.HN8}
\]
The middle expression is the original \(\kappa\), since postcomposition under the Hom adjunction gives \(\operatorname{Adj}_{L_1}(c_\nu A)=U_1(c_\nu)\chi\). Substitution in (B.HN3) proves closedness of both edge coordinates. No unspecified inverse of a right mate is involved.

The folded arrow and its witness are therefore
\[
\begin{aligned}
F_1(x)&=(c_\psi,1_{VN},H):
 (SZ,VN,\zeta_\Xi)\longrightarrow(Z',VN,U_1(r')t'),\\
H&=U_1(r')b_\psi+U_1(b_\nu)\chi\\
 &=U_1(r')b_\psi+
       \operatorname{Adj}_{L_1}(b_\nu A),\\
dH&=(U_1(r')t')c_\psi-\zeta_\Xi.
\end{aligned}
\tag{B.HN9}
\]
The second equality is the Hom-complex adjunction on the homogeneous degree-minus-one map \(b_\nu\), so no extra sign is inserted. Directly, the two terms of \(dH\) are \(U_1(r')(t'c_\psi-U_1(c_\nu)\chi)\) and \(U_1(r'c_\nu-\zeta_\nu)\chi\); the middle terms cancel. This recovers (B.BM18) with its exact endpoints and both terms, not merely an equality of cohomology classes. In the following diagram the top two squares carry \(b_\psi\) and \(U_1b_\nu\); the outside rectangle carries \(H\):
\[
\begin{array}{ccccc}
SZ&\xrightarrow{\ \chi\ }&U_1TR&\xrightarrow{\ U_1\zeta_\nu\ }&U_1W_1VN\\
\downarrow c_\psi&&\downarrow U_1c_\nu&&\Vert\\
Z'&\xrightarrow{\ t'\ }&U_1R'&\xrightarrow{\ U_1r'\ }&U_1W_1VN.
\end{array}
\tag{B.HN10}
\]
This is a homotopy-commutative diagram with the displayed witnesses, not a claim that its squares commute strictly. Its rightmost identity comes from the actual identity of \(VN\).

**A strict receiving map retaining the second coefficient.** For \(\mathcal N=\mathcal N_{U_1,W_1}\), apply the free presentation \(q:Q\mathcal N\to\mathcal N\) and bar construction (B.SF1)--(B.SF6). Then
\[
\begin{aligned}
\mathcal N&\xleftarrow[\simeq]{\ e=q\varepsilon\ }UQ\mathcal N
 \xrightarrow{\ \widetilde F\ }\mathcal A_{U_1W_1},\\
\widetilde F[x_j|\cdots|x_1]&=F_j(qx_j,\ldots,qx_1).
\end{aligned}
\tag{B.HN11}
\]
The differential (B.SF3) and the identities just checked prove that \(\widetilde F\) is a strict dg functor. The left arrow is a quasi-equivalence by (B.SF6). The right arrow is deliberately **not** labelled a quasi-equivalence. That conclusion in (B.SF7) used the additional Hom and essential-surjectivity hypotheses for replacement graphs; those hypotheses have not been proved for this enlarged decorated category. Its strictness proof, which is all that is used here, requires neither. A lift \(\widehat x\) of the closed arrow (B.HN8) can be chosen closed through the Hom-surjective quasi-isomorphism \(q\): correct a graded lift by a primitive of its differential error in the acyclic kernel. Its one-letter image is (B.HN9). Two-letter images retain (B.HN4), not zero. No multiplicative section of \(q\) is asserted.

Let \(J\) retain the actual terminal object and terminal map, and let \(I\) retain the initial source. As in (B.SF8),
\[
J\widetilde F=J_{\mathcal N}e,\qquad
I\widetilde F=I_{\mathcal N}e,\qquad
JF_2=IF_2=0.
\tag{B.HN12}
\]
These are equalities before applying either right-adjoint functor. Whole re-resolution over the common index, and after a restriction of that index, remains necessary as in (B.CE11); this roof does not justify a pointwise-to-whole projectivity inference.

**Join to the existing geometric provider without substituting for it.** The left comparisons in (B.HN6) are the resolved geometric comparisons (B.BM15), obtained from the original (B.GC12)--(B.GC13) cell and its retained whole inverse homotopies. The cell supplies its actual edge \(z=t(A_Cs)\theta_k^{-1}\) and all selected-edge coefficients, rather than an unresolved inverse. Its wordwise equality is already proved immediately after (B.GC13). Consequently any strict outer transfer of this receiving presentation must carry both terms of (B.HN9) and \(U_1(k_y)h_x\). When the specified outer maps satisfy that all-coefficient equality, (B.SF9) makes their induced square on \(UQ\mathcal N\) strictly commute. This gives the exact interface at which the existing geometric cell is inserted; it does not assert that separately chosen geometric boundaries already meet that hypothesis.

In particular, the seven actual targets of (B.FT3), the distinction between the unit and counit endpoint, and the degree-minus-four cube coordinate (B.FG13) must still be retained when this horizontal arrow is attached to the full changing-model diagram. The common-cylinder construction B.1av treats a supplied comparison homotopy; it does not erase that attachment obligation. The identification above compares the resolved mate with the nested fold. Simultaneous geometric higher-boundary assembly, nearby multiplicative descent, whole coefficient transport and strict-heart effacement are not established by this construction. The fixed-model identities do not establish the general geometric system. \(\square\)



### Attach the horizontal counit bridge with its second boundary

**Proposition B.1ax (the actual endpoint bridge, before restriction).** The horizontal arrow of (B.HN9) supplies exactly the counit homotopy required by the decorated four-face target (B.FT3). Its composition boundary contains the second coefficient of (B.HN4). This coefficient cannot be omitted even when only the first endpoint comparison is wanted. The endpoint construction extends to every arrow of the strict receiving roof (B.HN11). This identifies the endpoint part of the attachment; it does not assert that independently prescribed intermediate faces or geometric cubes already fit together.

**Transpose the whole decorated arrow.** Fix a dg adjunction \(L\dashv U\) between the admitted whole module categories, with its actual Hom-complex adjunction, unit \(\eta\) and counit. For \(Q=(P,N,q:P\to UN)\) in (B.FT2), write \(e_Q=\operatorname{Adj}^{-1}(q):LP\to N\). There is a strict dg functor to the ordinary arrow category of the target category:
\[
\begin{aligned}
\mathcal C_L(Q)&=(LP\xrightarrow{e_Q}N),\\
\mathcal C_L(a,w,h)&=(La,w,\operatorname{Adj}^{-1}h).
\end{aligned}
\tag{B.HB1}
\]
In particular it retains \(w\), not just \(U(w)\). The Hom adjunction commutes with differential and satisfies, for every homogeneous map,
\(\operatorname{Adj}^{-1}(h a)=\operatorname{Adj}^{-1}(h)L(a)\) and
\(\operatorname{Adj}^{-1}(U(w)h)=w\operatorname{Adj}^{-1}(h)\).
No factors change order. Applying these identities to (B.FT2) gives the arrow differential and product (B.FG1), including its sign \((-1)^{|y|}\). It also preserves the unit. This proves (B.HB1) without requiring \(q\) to be a quasi-isomorphism or \(U\) to be faithful.

**Identify the given horizontal counit, rather than choosing another one.** Use exactly \(X,Y,A,B,\chi,\zeta_\nu,x\) of (B.HN6)--(B.HN9). Put
\[
\begin{aligned}
D_\psi&=\operatorname{Adj}_{L_1}^{-1}(b_\psi),&
D_\nu&=\operatorname{Adj}_{M_1}^{-1}(b_\nu),\\
e'_L&=\operatorname{Adj}_{L_1}^{-1}(t'),&
e'_M&=\operatorname{Adj}_{M_1}^{-1}(r'),\\
e_X&=B\,M_1(A),&e_Y&=e'_M M_1(e'_L).
\end{aligned}
\tag{B.HB2}
\]
These maps use the original resolved inputs. In particular no comparison is evaluated on an unresolved right-adjoint value. Transposing the two terms of \(H\), first under \(L_1\) and then under \(M_1\), gives
\[
\begin{aligned}
\beta_x&=\operatorname{Adj}_{M_1L_1}^{-1}(H)\\
 &=e'_M M_1(D_\psi)+D_\nu M_1(A),\\
d\beta_x&=e_Y M_1L_1(c_\psi)-e_X.
\end{aligned}
\tag{B.HB3}
\]
For the first term the first transpose is \(r'D_\psi\); its second is \(e'_M M_1(D_\psi)\). For the second term the first transpose is \(b_\nu A\); its second is \(D_\nu M_1(A)\). These are Hom-complex identities, so they apply to the degree-minus-one witnesses. For the differential, transpose the two equations of (B.HN8):
\(dD_\psi=e'_L L_1c_\psi-c_\nu A\) and
\(dD_\nu=e'_M M_1c_\nu-B\).
Differentiate the middle line of (B.HB3). The two terms with \(e'_M M_1(c_\nu A)\) cancel. All other factors are closed of degree zero. The result is its last line. This also identifies (B.HB3) with the two-stage case of (B.HS5), with the same counits and not only the same differential.

**A universal endpoint bridge in the decorated category.** For any \(Q=(P,N,q)\), retain its separate unit object \(Q^u=(P,LP,\eta_P)\). For \(f=(a,w,h):Q_0\to Q_1\) of degree \(n\), set
\[
\begin{aligned}
E_Q&=(1_P,e_Q,0):Q^u\longrightarrow Q,\\
A(f)&=(a,La,0):Q_0^u\longrightarrow Q_1^u,\\
\mathcal B(f)&=(0,\beta_f,0):Q_0^u\longrightarrow Q_1,\\
\beta_f&=\operatorname{Adj}^{-1}(h),\\
|E_Q|&=0,\qquad |A(f)|=n,\qquad |\mathcal B(f)|=n-1.
\end{aligned}
\tag{B.HB4}
\]
The unit transpose \(U(e_Q)\eta_P=q\) makes \(E_Q\) closed. Unit naturality makes \(A\) a strict dg functor. All these maps are in \(\mathcal A_U\), before its possibly nonfaithful forgetful functor. Direct calculation gives
\[
D\mathcal B(f)+\mathcal B(Df)=E_{Q_1}A(f)-fE_{Q_0}.
\tag{B.HB5}
\]
The first coordinate is zero. In the target coordinate this reads
\(d\beta_f+\operatorname{Adj}^{-1}(q_1a-U(w)q_0-dh)=e_{Q_1}La-we_{Q_0}\).
The last coordinate on either side is \(-h\), because \(U(\beta_f)\eta_{P_0}=h\). Thus the equation is proved in all degrees, not just for closed comparisons.

For composable \(f,g\), with \(|g|=m\), the same calculation also gives
\[
\mathcal B(gf)=\mathcal B(g)A(f)+(-1)^m g\mathcal B(f),
\qquad \mathcal B(1)=0.
\tag{B.HB6}
\]
Its target component is
\(\operatorname{Adj}^{-1}(h_g)L(a_f)+(-1)^m w_g\operatorname{Adj}^{-1}(h_f)\), the transpose of the product witness in (B.FT2). Its first and third components vanish. This is the precise product rule for this degree-minus-one bridge; treating it as an ordinary degree-zero natural transformation would give the wrong sign.

Apply this construction to \(L=M_1L_1\), \(U=U_1W_1\), and \(f=F_1(x)\). In (B.FG5)--(B.FG6), the exact endpoint records are
\(\mathbf c_L=A(f)\), \(\mathbf c_R=fE_X\), \(\mathbf e_1=E_Y\), and \(\mathbf b=\mathcal B(f)\).
The actual target component of \(\mathbf c_R\) is \(e_X\), since \(f\) has terminal map \(1_{VN}\); (B.HN7) identifies it with \(V(e_M M_0e_L)\Xi_Z\). The target component of \(\mathbf b\) is precisely (B.HB3). The following homotopy rectangle displays the distinction between the two endpoint paths:
\[
\begin{array}{ccc}
X^u&\xrightarrow{\ A(f)\ }&Y^u\\
\downarrow E_X&&\downarrow E_Y\\
F_0X&\xrightarrow{\ f\ }&F_0Y
\end{array}
\qquad
E_YA(f)-fE_X=D\mathcal B(f)\quad(Df=0).
\tag{B.HB7}
\]
Here \(X^u,Y^u\) denote the unit objects associated to the folded objects \(F_0X,F_0Y\). The rectangle is homotopy-commutative, not strictly commutative. Its reproducible diagram source is this displayed array, and its witness is the actual two-term counit in (B.HB3). It does not identify the intermediate \(\mathsf A,\mathsf C\) of (B.FT3) with an endpoint.

**The second coefficient is part of the bridge boundary.** For general composable homogeneous nested arrows \(x,y\), let \(|x|=n\), \(|y|=m\), use the coefficients (B.HN4), and set
\(B_1(x)=\mathcal B(F_1x)\), \(B_2(y,x)=\mathcal B(F_2(y,x))\), \(A_x=A(F_1x)\).
The degree of \(B_2\) is \(m+n-2\). Then
\[
\begin{aligned}
&B_1(yx)-B_1(y)A_x-(-1)^mF_1(y)B_1(x)\\
&\quad=(-1)^m\bigl(DB_2(y,x)+B_2(Dy,x)\\
&\hspace{5em}+(-1)^{m-1}B_2(y,Dx)+F_2(y,x)E_X\bigr).
\end{aligned}
\tag{B.HB8}
\]
To prove this, solve (B.HN5) for \(F_1(yx)-F_1(y)F_1(x)\), then apply \(\mathcal B\) and (B.HB6). Since the initial coordinate of \(F_2\) is zero, \(A(F_2)=0\). Equation (B.HB5) therefore says
\(\mathcal B(DF_2)=-F_2E_X-D\mathcal B(F_2)\).
Substitution gives every term and sign in (B.HB8).

Writing \(H_2=U_1(k_y)h_x\), its target and last coordinates can be seen explicitly:
\[
\begin{aligned}
\beta_2&=\operatorname{Adj}_{M_1L_1}^{-1}(H_2)\\
 &=\operatorname{Adj}_{M_1}^{-1}(k_y)\,
       M_1\bigl(\operatorname{Adj}_{L_1}^{-1}(h_x)\bigr),\\
B_2&=(0,\beta_2,0),\\
(DB_2)_h&=-H_2,\qquad (F_2E_X)_h=H_2.
\end{aligned}
\tag{B.HB9}
\]
Naturality of the two Hom adjunctions proves the first line in the displayed order. The final two terms cancel in (B.HB8); dropping \(F_2E_X\) would leave \(-H_2\). Thus even a pure third-coordinate folding term supplies a necessary target-side composition homotopy. Neither a zero terminal coordinate for \(F_2\) nor equality on \(H^0\) permits discarding it.

**All arrows of the strict roof, including its higher generators.** Let \(\mathscr R=UQ\mathcal N\) and \(T=\widetilde F\) be (B.HN11). Apply the just-proved universal construction to its strict images:
\[
\begin{aligned}
\widetilde A&=A T,&\widetilde B(s)&=\mathcal B(Ts),\\
D\widetilde B(s)+\widetilde B(Ds)
 &=E_{\mathrm{target}(s)}\widetilde A(s)-T(s)E_{\mathrm{source}(s)},\\
\widetilde B(ts)&=\widetilde B(t)\widetilde A(s)
                   +(-1)^{|t|}T(t)\widetilde B(s).
\end{aligned}
\tag{B.HB10}
\]
These hold on every homogeneous arrow because \(T\) is strict and (B.HB5)--(B.HB6) hold on every arrow of its receiving category. On a one-letter generator \(\widetilde B\) is \(B_1\); on a two-letter generator it is \(B_2\), with the generator normalization of (B.HN11). On longer single generators it is zero for this two-edge fold, but on their products it is determined by the displayed product rule, not set to zero. The free differential includes its split-word terms: its two-letter instance is exactly (B.HB8). This supplies the higher endpoint identities without assuming that \(F_1\) itself is multiplicative or inventing a multiplicative section of the roof projection.

**Retain the existing geometric and cube boundaries.** The actual mixed-cell transfer remains (B.GC13), including \(z=t(A_Cs)\theta_k^{-1}\) and every selected-edge coefficient. For its admitted strict outer maps, that equation compares the same homogeneous word before transposition; (B.HB1) and Hom naturality compare its counit transpose. No inverse is introduced on an unresolved object. Under the actual proper-refinement functor (B.FT9), the endpoint target witnesses become
\[
\beta_x'=\beta_x c_{P_0},\qquad
\beta_2'=\beta_2 c_{P_0},\qquad
\bar\gamma'=\bar\gamma c_{P_0},
\tag{B.HB11}
\]
with the original canonical source comparison \(c_{P_0}:L'RP_0\to LP_0\). The transpose proof of (B.FT11) works in every degree, hence also for \(\beta_2\). Formula (B.FT9) acts on the entire decorated arrows, including their receiving-target factors. In particular, for a *supplied* full four-face cube the retained equation is still
\[
D\mathbf P(g_H)=\mathbf P(g_T)-\mathbf P(g_B)
                    +\widehat{\mathbf R}(f_H),
\qquad \mathbf P(g_H)=(P_H,\bar\gamma(f_H),W_H).
\tag{B.HB12}
\]
Here \(\mathbf P(g_H)\) has degree minus three and \(W_H\) has degree minus four. The discrepancy includes \(-\mathbf b\) as in (B.FG10); its target proof is (B.FT5). A transported cube retains \(\kappa RW_H\), not zero. This is a preservation statement for the actual supplied cube, not its existence for independently chosen geometric faces.

The endpoint attachment and its second boundary are specified before restriction and on a strict common roof. The simultaneous changing geometric diagram still needs the intermediate \(\mathsf A,\mathsf C\) face maps with their actual (B.FT4) targets and their common higher overlap boundary. Only after those identities are checked may the relative lift (B.CE10) keep them fixed. Neither the endpoint calculation nor acyclicity of a lifting kernel creates a missing face. Whole-index re-resolution remains required. Geometric nearby multiplicative descent, normalized coefficient transport with derived inverse limits and strict-heart higher effacement are not established by this construction. The endpoint identities alone do not establish those geometric comparisons. \(\square\)


### Transport the seven-object diagram with canonical new units

**Proposition B.1ay (a directed unit comparison, not a unit isomorphism).** The fixed-common-model intermediate faces already constructed in B.1aj and B.1an admit a simultaneous transport through any resolved outer comparison of B.1at. The three unit vertices can be replaced by the canonical new unit vertices, without assuming the comparison invertible. The other four vertices remain their actual transported objects. This gives a receiving diagram with all four faces and the full cube. It does not identify that diagram with independently chosen standard replacements in a new geometric model.

**The comparison at a unit vertex.** Write the old and new adjunctions as \(L\dashv U\) and \(\widehat L\dashv\widehat U\). Let \(\Sigma,\Omega\) be the whole source and target dg functors, and let \(\sigma_P:\widehat L\Sigma P\to\Omega LP\) be the closed dg-natural comparison on the admitted whole h-projective sources. These are the data of (B.ZT1), with new letters to distinguish them from the inner \(S,V,\vartheta\) of the seven-object diagram. As there, \(\Sigma\) preserves the required whole h-projective sources. Write \(e_q=\operatorname{Adj}_L^{-1}q\), \(\beta_f=\operatorname{Adj}_L^{-1}h\). The existing strict dg transport is
\[
\begin{aligned}
Tq&=(\Sigma P,\Omega N,\widehat{\operatorname{Adj}}(\Omega e_q\,\sigma_P)),\\
T(a,w,h)&=(\Sigma a,\Omega w,
       \widehat{\operatorname{Adj}}(\Omega\beta_f\,\sigma_P)).
\end{aligned}
\tag{B.UT1}
\]
In particular \(T(P,LP,\eta_P)\) has target \(\Omega LP\), not \(\widehat L\Sigma P\). Put
\[
\begin{aligned}
u'_P&=(\Sigma P,\widehat L\Sigma P,\widehat\eta_{\Sigma P}),\\
K_P&=(1_{\Sigma P},\sigma_P,0):u'_P\longrightarrow T(P,LP,\eta_P).
\end{aligned}
\tag{B.UT2}
\]
This arrow is closed: the third coordinate of its differential is
\(\widehat{\operatorname{Adj}}(\sigma_P)-\widehat U(\sigma_P)\widehat\eta_{\Sigma P}=0\).
There is no inverse in this construction. Naturality of the degree-zero \(\sigma\), in every homogeneous degree, and the Hom adjunction give
\[
\begin{aligned}
T(A(a))K_P&=K_{P'}\widehat A(\Sigma a),\\
T(E_q)K_P&=E_{Tq},\\
T(\mathcal B(f))K_P&=\widehat{\mathcal B}(Tf).
\end{aligned}
\tag{B.UT3}
\]
Here \(A(a)=(a,La,0)\), and \(E,\mathcal B\) are (B.HB4). The first equality has identical first coordinates; its target equality is \(\Omega(La)\sigma_P=\sigma_{P'}\widehat L(\Sigma a)\); both witnesses are zero. The second target is \(\Omega e_q\sigma_P\), the counit transpose of \(Tq\). The third target is \(\Omega\beta_f\sigma_P\), the transpose of its transported witness. This proves all three identities before restriction and without evaluating \(\sigma\) on an unresolved right-adjoint value.

**Exactly which vertices change.** Set \(P_0=SQ_0\), \(P_R=SR_0\). In the old diagram \(L=L_1\), \(X=LP_0\), \(M_1=LQ_1\). Denote its new diagram by \(\overline D\). Its source object at each row is the \(\Sigma\)-image of the original source. Its target objects are
\[
\begin{array}{c|c}
\text{label}&\text{target of }\overline D\\ \hline
\mathsf Q_0^u&\widehat L\Sigma P_0\\
\mathsf R_0^u&\widehat L\Sigma P_R\\
\mathsf A&\Omega X\\
\mathsf C&\Omega(VM_0)\\
\mathsf Q_1^u&\widehat L\Sigma Q_1\\
\mathsf R_1&\Omega M_1\\
\mathsf Q_1^q&\Omega(VN)
\end{array}
\tag{B.UT4}
\]
At the three unit rows use \(u'_P\). At the other four rows use \(Tq\) literally, with its structure map from (B.UT1). Those structure maps are not asserted to be quasi-isomorphisms. Thus, for example, the target of \(\mathsf A\) has not been relabelled as \(\widehat L\Sigma P_0\), and the targets of \(\mathsf Q_1^u,\mathsf R_1\) need not coincide.

**The actual directed presentation suffices.** Use the generators and their relations in (B.FG3)--(B.FG12), with the actual decorated targets of (B.FT3)--(B.FT5). Every generator whose target is a unit vertex has a unit source: these are \(\mathbf s_u,\mathbf s_z,\mathbf c_L,\mathbf J_0\), their differential records and identities. Each is an \(A(a)\). There is no generator from a nonunit vertex into a unit vertex. Keep this presentation; do not adjoin arbitrary arrows into unit vertices. Define \(K_i=K_{P_i}\) at a unit row and \(K_i=1\) at the other rows. For a generator \(g:i\to j\), put
\[
\overline D(g)=
\begin{cases}
\widehat A(\Sigma a),&j\text{ is a unit row},\quad g=A(a),\\
T(g)K_i,&j\text{ is a nonunit row}.
\end{cases}
\tag{B.UT5}
\]
All labels refer to vertices, not accidental equalities of underlying modules. The comparison is the following strictly commutative square of decorated arrows:
\[
\begin{array}{ccc}
\overline D(i)&\xrightarrow{\ \overline D(g)\ }&\overline D(j)\\
\downarrow K_i&&\downarrow K_j\\
TD(i)&\xrightarrow{\ T(g)\ }&TD(j).
\end{array}
\tag{B.UT6}
\]
For a unit target this is the first identity of (B.UT3); for a nonunit target it is the definition. Naturality therefore holds on every word. To check that all differential and linear relations are preserved, separate their targets. A relation with nonunit target transports to that same relation under the strict functor \(T\), precomposed with \(K_i\); here \(K_j=1\), so no cancellation of a noninvertible map is used. A relation with unit target consists entirely of \(A\)-arrows. Its first-coordinate relation transports by \(\Sigma\) and then the strict dg functor \(\widehat A\). The comparisons \(K_i\) are closed, so these arguments also prove compatibility with differential, including the nonclosed generator \(\mathbf J_0\). Products and identities follow by the same word calculation. This proves the construction on the stated presentation, not on an arbitrary full subcategory.

**Retain the intermediate target maps.** Write \(\sigma_0=\sigma_{P_0}\), \(\sigma_R=\sigma_{P_R}\), \(\sigma_1=\sigma_{Q_1}\), and \(\vartheta_0=\vartheta_{Q_0}\), \(\vartheta_R=\vartheta_{R_0}\) in the original notation. The target components of representative arrows are
\[
\begin{aligned}
(\overline{\mathbf u}_X)_Z&=\sigma_0,&
(\overline{\mathbf u}_1)_Z&=\sigma_1,\\
(\overline{\mathbf c}_L)_Z&=\widehat L\Sigma c,&
(\overline{\mathbf a})_Z&=\Omega(Lc),\\
(\overline{\mathbf v})_Z&=\Omega\vartheta_0,&
(\overline{\mathbf w})_Z&=\Omega(Ve_0),\\
(\overline{\mathbf c}_M)_Z&=\Omega(Ve_0^M\vartheta_R)\sigma_R,\\
(\overline{\mathbf c}_R)_Z&=\Omega(Ve_0\vartheta_0)\sigma_0,\\
(\overline{\mathbf e}_1)_Z&=\Omega e_1\sigma_1.
\end{aligned}
\tag{B.UT7}
\]
Every third coordinate at a nonunit target is exactly the transpose in (B.UT1). Precomposition with \(K_i\) leaves the transported arrow's first and third coordinates unchanged, because the comparison has identity first coordinate and zero third coordinate. The transported witness itself need not be zero and is not reconstructed from a restricted target map. The four face targets and the separate endpoint bridge are
\[
\begin{aligned}
(\overline{\mathbf j}_U)_Z&=\Omega(V\lambda_0\vartheta_0)\sigma_0,\\
(\overline{\mathbf j}_F)_Z&=0,\\
(\overline{\mathbf j}_C)_Z&=\Omega(V\alpha_0\vartheta_R)\sigma_R,\\
(\overline{\mathbf j}_\beta)_Z&=\Omega\beta,\\
(\overline{\mathbf b})_Z&=\Omega\beta\,\sigma_0.
\end{aligned}
\tag{B.UT8}
\]
The last two maps have different sources: \(\mathsf A\) has target \(\Omega X\), whereas \(\mathsf Q_0^u\) has target \(\widehat L\Sigma P_0\). The \(\sigma_0\) appears in the face path only upon composition with \(\overline{\mathbf u}_X\). Thus its target becomes \(\Omega\beta\sigma_0\), exactly the bridge target. Dropping \(\sigma_0\), or inserting it prematurely into the \(\mathsf A\)-origin face, is not an alternative normalization.

The full four face identities, with the original degree conventions and the record differential \(\partial\), are
\[
\begin{aligned}
D\overline{\mathbf j}_U(f)+\overline{\mathbf j}_U(\partial f)
 &=\overline{\mathbf c}_M\overline{\mathbf s}_u
   -\overline{\mathbf v}\overline{\mathbf u}_X,\\
D\overline{\mathbf j}_F(f)+\overline{\mathbf j}_F(\partial f)
 &=\overline{\mathbf u}_1\overline{\mathbf c}_L
   -\overline{\mathbf a}\overline{\mathbf u}_X,\\
D\overline{\mathbf j}_C(f)+\overline{\mathbf j}_C(\partial f)
 &=\overline{\mathbf c}_R\overline{\mathbf s}_z
   -\overline{\mathbf w}\overline{\mathbf c}_M,\\
D\overline{\mathbf j}_\beta(f)+\overline{\mathbf j}_\beta(\partial f)
 &=\overline{\mathbf z}_1\overline{\mathbf a}
   -\overline{\mathbf w}\overline{\mathbf v}.
\end{aligned}
\tag{B.UT9}
\]
These are images of (B.FG8), by the proof of (B.UT5). They can also be checked upstairs directly: the first and third target equations of (B.FT4) are acted on by \(\Omega\) and precomposed with \(\sigma_0,\sigma_R\), respectively; naturality of \(\sigma\) moves the unit-only arrows past these comparisons. The second uses \(\Omega(Lc)\sigma_0=\sigma_1\widehat L\Sigma c\). The fourth is simply \(\Omega\) of its old target equation, because its source is \(\mathsf A\), not a unit row. This verifies the target distinction needed for all four equations, rather than only their images under \(\widehat U\).

**The full cube and ordered successive transports.** Form the new bridge sum and corrected discrepancy by the same signed words as (B.FG9)--(B.FG10), including the separate term \(-\overline{\mathbf b}\). For \(\mathbf P(g_H)=(P_H,\bar\gamma(f_H),W_H)\), the actual transported lift and its boundary are
\[
\begin{aligned}
\overline{\mathbf P}(g_H)
 &=\bigl(\Sigma P_H,\Omega\bar\gamma(f_H)\sigma_0,\widehat W_H\bigr),\\
\widehat W_H
 &=\widehat{\operatorname{Adj}}\bigl(
       \Omega(\operatorname{Adj}_L^{-1}W_H)\sigma_0\bigr),\\
D\overline{\mathbf P}(g_H)
 &=\overline{\mathbf P}(g_T)-\overline{\mathbf P}(g_B)
     +\overline{\widehat{\mathbf R}}(f_H).
\end{aligned}
\tag{B.UT10}
\]
The first equality is (B.UT5), and the last is the image of the already supplied (B.FG12). Here the lift has degree minus three and its retained third coordinate \(\widehat W_H\) has degree minus four. The construction transports the specified \(W_H\); it does not set it to zero or infer it from the endpoint bridge. Likewise the degree-minus-two extension equation holds for every homogeneous record, not just for closed endpoints.

For two composable outer transports, use the strict composition conventions of (B.ZT13). The combined comparison and unit arrow are
\[
\begin{aligned}
\sigma^{21}_P&=\Omega_2(\sigma^1_P)\sigma^2_{\Sigma_1P},\\
K^{21}_P&=T_2(K^1_P)K^2_{\Sigma_1P}.
\end{aligned}
\tag{B.UT11}
\]
Their source and target components are identities and the displayed composite; their third components vanish. At a nonunit target, successive applications of (B.UT5) give \(T_2T_1(g)T_2(K^1_i)K^2_i\), which is precisely the combined rule. At unit targets both give the same \(\widehat A\)-arrow. Thus successive normalizations agree under these conventions, with all intermediate labels retained. With nonstrict functor models one must retain the specified associators of the original transport rather than claiming literal equality of differently parenthesized targets.

**The geometric parameter inputs.** The label-preserving inverse-image parameter category is constructed in [B.1ac](#resolve-inverse-image-transport-over-the-geometric-index); its correctly oriented right-module kernels and composition roofs are given in [B.1ad](#join-the-geometric-kernels-in-right-module-variance). For the mixed compact-support square, [B.MX3–B.MX11](#the-proper-open-kernel-and-the-common-mixed-cube) specifies the six operation words, their common mapping target and the two-route boundary. These are the inputs to be joined to the proper-refinement and folding family of [B.SN12–B.SN13](#normalize-the-refinement-array-before-folding). The compositors in (B.IP11) become homotopy equivalences on h-projective inputs; the right-module comparisons in (B.RK2) remain roofs, not chosen strictly natural inverses. The joint comparison must retain their actual maps and shared higher boundaries.

**Replacement choices and geometric comparisons.** Independent whole replacements of the same seven-object envelope are compared in [B.1ar](#whole-replacement-comparison-without-inverting-units); [B.1as](#compare-envelope-choices-across-geometric-refinements) identifies the common envelope across actual proper refinements, including the normalized bilateral source and target comparisons. These constructions retain both comparison-back witnesses without assuming that unit arrows are quasi-isomorphisms. For horizontal geometric composition, [B.1aw](#place-the-horizontal-mate-in-the-actual-nested-graph) identifies the resolved mate with the original nested fold, and [B.1ax](#attach-the-horizontal-counit-bridge-with-its-second-boundary) supplies its counit endpoint bridge with the second folding coefficient. The endpoint bridge does not identify the intermediate A and C diagrams or supply their common higher boundary. The remaining comparison therefore concerns independently prescribed geometric diagrams and their actual shared boundaries, not the existence of whole replacement-choice comparisons over an already identified proper-refinement target.

**Successive base change and the actual comparison roofs.** For two successive base changes, the targets in [B.1aj](#join-the-right-triangle-to-resolved-base-change) give the following route: the A-target comparison is the second left base-change map evaluated at the first transported initial resolution, and the C-target is the ordered double inverse image. [B.1ad](#join-the-geometric-kernels-in-right-module-variance) compares each ordered inverse-image transport with its direct-composite model by two actual maps into a common dual kernel. Applying the receiving left functor to the source-kernel roof gives a zigzag for the A-targets; the target-kernel roof gives cospans for the C-targets and counit endpoints. The endpoint maps exist on general modules, but their equivalence properties require the admitted resolved inputs. These are directed roofs, not chosen strictly natural inverses. The resolved vertical-pasting formula in [B.1ab](#transpose-the-actual-base-change-cells) retains both endpoint-witness terms. For the second-resolution targets, [B.1ay](#transport-the-seven-object-diagram-with-canonical-new-units) retains the span through the transported canonical unit rather than inverting the mate or its source lift. These individual routes do not identify independently prescribed geometric comparison cells on the whole parameter diagram: their common four faces and higher boundary must still be matched.

**Scope of the remaining comparison.** This construction supplies the induced receiving diagram and its actual map to the transported old diagram. It assumes the fixed-model faces. The whole-envelope method (B.CE10) resolves the resulting diagram without inverting any \(K_P\); after an index restriction, (B.CE11) still requires whole re-resolution. Comparing it with an independently prescribed new geometric diagram requires the actual maps of their intermediate targets and common boundaries. Changes in \(\sigma\) require the retained homotopies (B.ZT9)--(B.ZT10) and their common-cylinder realization, not a claim that objectwise comparisons are strictly natural. The original geometric transfer (B.GC13) retains every word coefficient. Those changing-parameter identifications, geometric nearby-cycle multiplicative descent, coefficient completion with derived inverse limits, strict-heart higher effacement are not established by the unit normalization. \(\square\)


### Compare successive base-change kernels and their resolved mates

**Proposition B.1az (two successive base changes on a common whole model).** Fix two successive cartesian changes of base of one open/proper compactification. The ordered and direct left-kernel compact-support comparisons admit a comparison homotopy retaining their original lift witnesses. The actual right-kernel roofs transport this comparison to a whole right-kernel homotopy and its comparison-back witness. The chosen inverses have an explicit three-term comparison, and the resolved right mates have a full decorated-graph comparison whose endpoint bridge retains a degree-minus-two target.

The scope is the Noetherian separated finite-type compactification setting, with ordinary unbounded torsion coefficients and the common annihilator required by the proper-base-change theorem, as in [B.1ae](#construct-the-whole-bimodule-compact-support-base-change-cell). The algebra uses the original commutative coefficient ring. Whole replacements are made on the specified common free parameter category times both endpoint categories. A change of index requires the re-resolution of (B.CE11). The assertion does not identify unspecified higher geometric cells or assert global compatibility of all composition/refinement arrays.

#### The actual left-kernel words

Use three cartesian rows \(X_i\xrightarrow{j_i}U_i\xrightarrow{h_i}Y_i\), for \(i=0,1,2\), with \(j_i\) open and \(h_i\) proper. The successive vertical scheme maps are \(u_i,v_i,g_i\). Their direct composites are \(u_{21}=u_1u_2\), \(v_{21}=v_1v_2\), \(g_{21}=g_1g_2\). In this paragraph capital letters denote **kernels**:
\[
\begin{gathered}
\mathsf H_i=L_{h_i},\quad \mathsf J_i=L_{j_i},\\
\mathsf U_i=L_{u_i},\\
\mathsf V_i=L_{v_i},\\
\mathsf G_i=L_{g_i},\\
\mathsf W_i=\mathsf H_i\mathsf J_i .
\end{gathered}
\tag{B.OD1}
\]
Juxtaposition denotes balanced tensor in left-kernel order; canonical tensor associators are retained. The proper and open maps of (B.KC5)–(B.KC8) are
\[
\begin{aligned}
P_i:\mathsf H_i\mathsf V_i&\longrightarrow
       \mathsf G_i\mathsf H_{i-1},\\
O_i:\mathsf J_i\mathsf U_i&\longrightarrow
       \mathsf V_i\mathsf J_{i-1}.
\end{aligned}
\tag{B.OD2}
\]
Each has its original whole witness \(\pi_i\lambda_i-\chi_i=d\omega_i\).

Start with the actual [inverse-image compositor](#resolve-inverse-image-transport-over-the-geometric-index), \(C_bC_a\to C_{ba}\). Lift the composite from \(L_bL_a\) through \(L_{ba}\to C_{ba}\) by (B.ND7). With its lift witness retained, this gives
\[
\begin{gathered}
c_a:L_bL_a\longrightarrow L_{ba},\\
\begin{aligned}
&\epsilon_{ba}c_a\\
&\quad-\mu(\epsilon_b\otimes\epsilon_a)=d\eta_a .
\end{aligned}
\end{gathered}
\tag{B.OD3}
\]
Here \(\epsilon\) includes the evaluation in (B.IP4), and \(\mu\) is actual direct-image composition. The whole exterior-cell filtration of (B.KC2) and the quasi-isomorphism proof in (B.IP11) show that \(c_a\) is a quasi-isomorphism between whole h-projectives. It has a whole inverse with both inverse homotopies. This does not make independently chosen lifts strictly associative. Use \(c_u,c_v,c_g\) in one common model; the proper and open comparisons use the **same** \(c_v\).

For the proper rectangle the common raw complex is
\[
\begin{aligned}
&M_{12}(Q,I)\\
&\quad=\operatorname{Hom}^{\bullet}\bigl(h_{0,*}eI,\\
&\hspace{5em}g_{1,*}g_{2,*}eQ\bigr).
\end{aligned}
\tag{B.OD4}
\]
Take homogeneous \(z_1:eI\to v_{1,*}eK_1\), \(z_2:eK_1\to v_{2,*}eK_2\) and \(w:h_{2,*}eK_2\to eQ\). The successive map (B.KC3) is
\[
g_{1,*}\!\left[g_{2,*}(w)\kappa_{2,K_2}
                          h_{1,*}(z_2)\right]
              \kappa_{1,K_1}h_{0,*}(z_1).
\]
Naturality of \(\kappa_1\) rewrites it as
\[
\begin{aligned}
&g_{1,*}g_{2,*}(w)
 (g_{1,*}\kappa_{2,K_2})\\
&\,\cdot\kappa_{1,v_{2,*}K_2}h_{0,*}
       \!\left[v_{1,*}(z_2)z_1\right].
\end{aligned}
\tag{B.OD5}
\]
This is the direct map: its comparison is
\(\kappa_{21}=(g_{1,*}\kappa_2)(\kappa_1v_{2,*})\), and (B.IP5) composes \(z_2,z_1\) as \(v_{1,*}(z_2)z_1\). No homogeneous factors were permuted. Equations (B.BC9)–(B.BC10) identify the same equality under the inverse-image adjunction in every resolution-string coefficient.

For clarity, the witness of the ordered proper map can be written before any inverse is chosen. Put
\[
\begin{aligned}
M_1&=\operatorname{Hom}^{\bullet}
          (h_{0,*}eI,g_{1,*}eQ_1),\\
M_2&=\operatorname{Hom}^{\bullet}
          (h_{1,*}eK_1,g_{2,*}eQ).
\end{aligned}
\]
There are balanced degree-zero composition maps
\[
\begin{aligned}
F_g(y\otimes t)&=g_{1,*}(\epsilon y)t,\\
F_v(t\otimes z)&=g_{1,*}(t)\kappa_{1,K_1}
                                      h_{0,*}(\epsilon z)
\end{aligned}
\]
from \(\mathsf G_2\otimes M_1\) and \(M_2\otimes\mathsf V_1\), respectively, into \(M_{12}\). The ordered witness is
\[
\begin{aligned}
\omega_o={}&F_g(1\otimes\omega_1)\\
&\quad\cdot(P_2\otimes1)\\
&+F_v(\omega_2\otimes1).
\end{aligned}
\tag{B.OD6}
\]
The tensor \(1\otimes\omega_1\) acts on \(y\otimes t\) with sign \((-1)^{|y|}\). Differentiation and naturality of \(\kappa_1\) give \(\pi_o\lambda_o-\chi_o=d\omega_o\), where
\(\lambda_o=(\mathsf G_2P_1)(P_2\mathsf V_1)\). Thus the original witnesses, rather than only their cohomology classes, occur in the comparison.

For the open rectangle use the actual right-adjoint mates
\(\theta_i^R:u_{i,*}j_i^*\to j_{i-1}^*v_{i,*}\). Evaluating on the same inverse image of an open subset gives
\[
\theta_{21}^R=
   (\theta_1^Rv_{2,*})(u_{1,*}\theta_2^R).
\tag{B.OD7}
\]
For homogeneous \(z_1,z_2,w\) of the corresponding open kernels, the ordered expression is
\(\theta_1^Ru_{1,*}[\theta_2^Ru_{2,*}(w)z_2]z_1\); by (B.OD7) it is
\(\theta_{21}^Ru_{1,*}u_{2,*}(w)u_{1,*}(z_2)z_1\), the direct expression. Its common complex is
\(\operatorname{Hom}^{\bullet}(eI,j_0^*v_{1,*}v_{2,*}eQ)\).
The composition maps replacing \(F_g,F_v\) are
\(F_V(y\otimes t)=j_0^*v_{1,*}(y)t\) and
\(F_U(t\otimes z)=\theta_1^Ru_{1,*}(t)z\).
They give precisely (B.OD6) with \(O\) in place of \(P\), including its tensor sign.

#### Preserve the full comparison pair

For either rectangle write \(A_o,A_d\) for its ordered and direct source words and \(B_o,B_d\) for its target words. Let \(a:A_o\to A_d\), \(b:B_o\to B_d\) be the compositor maps. In the proper case \(a=\mathsf H_2c_v\), \(b=c_g\mathsf H_0\); in the open case \(a=\mathsf J_2c_u\), \(b=c_v\mathsf J_0\). The compositor witnesses give
\[
\pi_db-\pi_o=d\tau_g,\qquad
\chi_da-\chi_o=d\tau_v.
\]
Together with the original ordered and direct witnesses, set
\[
\begin{aligned}
\Delta&=b\lambda_o-\lambda_da,\\
K&=\tau_g\lambda_o+\omega_o\\
 &\quad-\omega_da-\tau_v.
\end{aligned}
\tag{B.OD8}
\]
The exact identity is \(dK=\pi_d\Delta\). The raw map \(\pi_d\) is a quasi-isomorphism by (B.KC3)–(B.KC7), using their K-injective argument, not preservation of arbitrary quasi-isomorphisms by proper image. Since \(A_o\) is whole h-projective, (B.ND7) gives
\[
\begin{gathered}
dH=\Delta,\\
\pi_dH-K=dT,\\
|H|=-1,\quad |T|=-2.
\end{gathered}
\tag{B.OD9}
\]
Indeed first choose a primitive \(H_0\) of \(\Delta\) by injectivity on cohomology. The closed difference \(\pi_dH_0-K\) is, in cohomology, the image of a closed degree-minus-one map \(Z\). Replace \(H_0\) by \(H_0-Z\); its remaining image difference is a boundary \(dT\). All maps are in the whole natural Hom complex. Denote the proper and open pairs by \((H_P,T_P)\), \((H_O,T_O)\).

Let \(O_o=(\mathsf V_2O_1)(O_2\mathsf U_1)\) and
\(P_o=(\mathsf G_2P_1)(P_2\mathsf V_1)\). Define
\[
K_i=(P_i\mathsf J_{i-1})(\mathsf H_iO_i).
\]
Closed degree-zero tensor interchange gives
\(K_o=(\mathsf G_2K_1)(K_2\mathsf U_1)
     =(P_o\mathsf J_0)(\mathsf H_2O_o)\).
The direct map is
\(K_d=(P_{21}\mathsf J_0)(\mathsf H_2O_{21})\).
The compact-support comparison is the explicit two-term homotopy
\[
\begin{aligned}
&H_K\\
&\quad=(H_P\mathsf J_0)(\mathsf H_2O_o)\\
&\qquad+(P_{21}\mathsf J_0)(\mathsf H_2H_O),\\
&dH_K\\
&\quad=(c_g\mathsf W_0)K_o\\
&\qquad-K_d(\mathsf W_2c_u).
\end{aligned}
\tag{B.OD10}
\]
The middle terms cancel because the same \(c_v\) occurs on both sides. Retain \(T_P,T_O\) and all compositor witnesses.

#### The actual right roofs, not only their endpoints

Use the complete [right-module construction](#join-the-geometric-kernels-in-right-module-variance) and [compact-support comparison](#construct-the-whole-bimodule-compact-support-base-change-cell). Its route retains the refined graph with both \(s,t\) edges, the strict \(\rho:\mathcal A_f^+\to\mathcal A_f\), both signed bar comparisons, and the augmentations \(W_f\to L_h\otimes B_j\), \(L_h\to B_h\). Continue through the coend, the cospan (B.KC13), evaluation and induction–restriction in (B.KC14), and double Yoneda. These are the actual roofs from \(DW_f\) to \(H_f\).

The full dual is \(D(f)(\phi)=(-1)^{|f||\phi|}\phi f\); it satisfies
\(dD(f)=D(df)\) and
\(D(gf)=(-1)^{|f||g|}D(f)D(g)\).
The inverse-image roof remains
\[
\begin{aligned}
P_gP_h&\longrightarrow D(C_hC_g),\\
P_{hg}&\longrightarrow D(C_hC_g).
\end{aligned}
\tag{B.OD11}
\]
Its right leg points from the direct kernel. Whole replacements precede inverses; both inverse homotopies are retained. Write \(q_i:R_i\to D_i\) for the resulting whole comparisons, including the original zigzags back to the right words:
\[
\begin{aligned}
R_0&:\ H_{f_0}P_{g_{21}},\\
D_0&:\ D(\mathsf G_{21}\mathsf W_0),\\
R_1&:\ H_{f_0}P_{g_1}P_{g_2},\\
D_1&:\ D(\mathsf G_2\mathsf G_1\mathsf W_0),\\
R_2&:\ P_{u_{21}}H_{f_2},\\
D_2&:\ D(\mathsf W_2\mathsf U_{21}),\\
R_3&:\ P_{u_1}P_{u_2}H_{f_2},\\
D_3&:\ D(\mathsf W_2\mathsf U_2\mathsf U_1).
\end{aligned}
\tag{B.OD12}
\]
These symbols denote whole representatives, not equality of unresolved tensor products. On the dual side set
\(x=D(c_g\mathsf W_0)\), \(y=D(\mathsf W_2c_u)\),
\(f_o=D(K_o)\), \(f_d=D(K_d)\), \(h=D(H_K)\).
Their types are \(x:D_0\to D_1\), \(y:D_2\to D_3\),
\(f_o:D_1\to D_3\), \(f_d:D_0\to D_2\); and
\(dh=f_ox-yf_d\).

A closed right arrow \(B:R_i\to R_j\) is retained with its actual roof witness
\[
q_jB-fq_i=dA.
\tag{B.OD13}
\]
For example \(B=p_jfq_i\) and \(q_jp_j-1=ds_j\) give \(A=s_jfq_i\).
For a path of closed arrows, the witness is the sum
\(\sum_i f_n\cdots f_{i+1}A_iB_{i-1}\cdots B_1\).
This follows by telescoping; it keeps the internal inverse-cancellation witnesses instead of replacing the original path by a new collapsed map. For homogeneous maps the composition rule is
\(A_{gf}=A_gB_f+(-1)^{|g|}f_gA_f\), the resolution-graph rule.

The tensor, induction and bar operations used in this construction act on full Hom complexes. On a bar of length \(n\), a homogeneous map \(\phi\) acts with \((-1)^{n|\phi|}\), as in (B.RK7); (B.KC10) and (B.KC11) retain their length-one and opposite signs. RK3 evaluation is a closed natural map with its displayed sign. After passage to the existing strict \(UQ\) roof, a bracket word is an actual homogeneous arrow. Vanishing of the external KC10 terms in bar lengths at least two does not delete the image of that arrow or the internal coefficient \(K_2\) of (B.MX12).

Take the actual ordered and direct KC paths \(B_o:R_1\to R_3\), \(B_d:R_0\to R_2\), and the RK comparison maps \(X:R_0\to R_1\), \(Y:R_2\to R_3\), with witnesses \(A_o,A_d,A_x,A_y\) from (B.OD13). Set
\[
\begin{aligned}
\Delta_R&=B_oX\\
        &\quad-YB_d,\\
K_R={}&hq_0+A_oX\\
      &+f_oA_x\\
      &-A_yB_d\\
      &-yA_d .
\end{aligned}
\tag{B.OD14}
\]
Expansion gives \(dK_R=q_3\Delta_R\). The same whole-Hom argument as (B.OD9) supplies
\[
\begin{gathered}
dH_R=\Delta_R,\\
q_3H_R-K_R=dT_R,\\
|T_R|=-2.
\end{gathered}
\tag{B.OD15}
\]
An arbitrary primitive of \(\Delta_R\) would not establish the second equation. This constructs the comparison on the specified common realization; another stored representative requires its actual comparison roof, not merely an identification of represented objects.

#### Chosen inverses and the resolved right mate

Let \(\vartheta_o,\vartheta_d\) be the chosen whole inverses of \(B_o,B_d\), with all four homotopies
\[
\begin{aligned}
\vartheta_oB_o-1&=dl_o,&B_o\vartheta_o-1&=dr_o,\\
\vartheta_dB_d-1&=dl_d,&B_d\vartheta_d-1&=dr_d.
\end{aligned}
\]
Their comparison is
\[
\begin{aligned}
J={}&-\vartheta_oH_R\vartheta_d\\
    &+l_oX\vartheta_d\\
    &-\vartheta_oYr_d,\\
dJ={}&\vartheta_oY-X\vartheta_d .
\end{aligned}
\tag{B.OD16}
\]
Direct differentiation cancels the terms with \(\vartheta_oB_o\) and \(B_d\vartheta_d\). Neither of the last two terms may be omitted.

For the mate use the actual factor maps \(s:S_d\to S_o\), \(v:V_d\to V_o\) represented by the RK roofs. Tensoring the same legs with \(H_{f_0}\) or \(H_{f_2}\), and using RK3–4, gives their comparison graphs with \(X=vL_0\), \(Y=L_2s\). If separate whole word replacements intervene, apply (B.OD14)–(B.OD15) to those supplied graphs first, retaining their degree-minus-two witness. A replacement is not declared to commute strictly with tensor. The inverse comparison on these actual factorized maps, evaluated at an admitted resolved \(P_0\), reads
\[
dJ_{P_0}=
 \vartheta_oL_2(s_{P_0})
            -v_{L_0P_0}\vartheta_d .
\]
For \(r_0:P_0\to U_0N\), put \(e_0=\varepsilon_0L_0r_0\) and, under \(L_2\dashv U_2\), define
\[
\begin{aligned}
\zeta_o&=\operatorname{Adj}(V_oe_0\,\vartheta_o),\\
\zeta_d&=\operatorname{Adj}(V_de_0\,\vartheta_d),\\
\xi&=\operatorname{Adj}(V_oe_0\,J_{P_0}).
\end{aligned}
\]
The full Hom adjunction and naturality of \(v\) give
\[
\begin{aligned}
d\xi={}&\zeta_os_{P_0}\\
       &-U_2(v_N)\zeta_d .
\end{aligned}
\tag{B.OD17}
\]
There is no evaluation at the unresolved \(U_0N\), and no equivalence claim for an arbitrary unresolved \(N\). The distinct targets \(V_dN,V_oN\) and their actual map \(v_N\) remain explicit.

Choose whole receiving replacements
\(r_d:Q_d\to U_2V_dN\), \(r_o:Q_o\to U_2V_oN\), with the mate lifts
\(r_dc_d-\zeta_d=db_d\), \(r_oc_o-\zeta_o=db_o\).
Lift the actual target comparison as
\(t:Q_d\to Q_o\), \(r_ot-U_2(v_N)r_d=dw\).
This uses \(\operatorname{Hom}(Q_d,r_o)\), not an inverse of \(v_N\) or of the right mate. Set
\[
\begin{aligned}
\delta&=c_os_{P_0}-tc_d,\\
K_M&=\xi+b_os_{P_0}\\
   &\quad-U_2(v_N)b_d\\
   &\quad-wc_d .
\end{aligned}
\tag{B.OD18}
\]
Then \(dK_M=r_o\delta\), and (B.ND7) gives
\[
\begin{gathered}
dj=\delta,\\
r_oj-K_M=dk,\\
|j|=-1,\quad |k|=-2.
\end{gathered}
\tag{B.OD19}
\]
In the decorated graph the two closed arrows from
\((S_dP_0,V_dN,\zeta_d)\) to \((Q_o,V_oN,r_o)\) are
\((c_os_{P_0},v_N,b_os_{P_0}+\xi)\) and
\((tc_d,v_N,wc_d+U_2(v_N)b_d)\).
Thus \(D(j,0,k)=(\delta,0,K_M)\). The target map was retained before taking the difference; no nonfaithful forgetful functor erased it.

The [all-degree endpoint bridge](#attach-the-horizontal-counit-bridge-with-its-second-boundary) now gives
\[
\begin{aligned}
\Gamma_{o,d}&=\operatorname{Adj}^{-1}(k),\\
d\Gamma_{o,d}
 &=e_oL_2j\\
 &\quad-\operatorname{Adj}^{-1}(K_M).
\end{aligned}
\tag{B.OD20}
\]
The zero middle coordinate of \((j,0,k)\) does not make this target zero. It is determined by the third coordinate. Equations (B.HB5), (B.HB6) and (B.HB8) retain the remaining graph coordinate and the second product coefficient. This proves the stated fixed-diagram comparison. \(\square\)

#### The boundary required to attach a prescribed four-face cube

The following gives an exact attachment criterion, not an assertion that all independently prescribed target data satisfy it. Use the four-face notation of [B.1ao](#encode-all-four-faces-in-one-arrow-graph). For two DG realizations \(F,G\) on the same free diagram, let \(\alpha\) be the closed degree-zero vertex comparisons and \(\mathscr H\) a degree-minus-one comparison on its arrows. Its equations are
\[
\begin{aligned}
&d\mathscr H(c)+\mathscr H(dc)\\
&\quad=\alpha_tF(c)-G(c)\alpha_s,\\
&\mathscr H(gf)\\
&\quad=\mathscr H(g)F(f)\\
&\, +(-1)^{|g|}G(g)\mathscr H(f).
\end{aligned}
\tag{B.OD21}
\]
The graded Leibniz rule verifies consistency of these two equations on products. For
\(\mathbf B=\mathbf j_C\mathbf{su}
+\mathbf w\mathbf j_U-\mathbf j_\beta\mathbf u_X
-\mathbf z\mathbf j_F\), the product rule determines
\[
\begin{aligned}
&\mathscr H(\mathbf B)\\
&\quad=\mathscr H(\mathbf j_C)F(\mathbf{su})\\
&\qquad-G(\mathbf j_C)\mathscr H(\mathbf{su})\\
&\qquad+\mathscr H(\mathbf w)F(\mathbf j_U)\\
&\qquad+G(\mathbf w)\mathscr H(\mathbf j_U)\\
&\qquad-\mathscr H(\mathbf j_\beta)F(\mathbf u_X)\\
&\qquad+G(\mathbf j_\beta)\mathscr H(\mathbf u_X)\\
&\qquad-\mathscr H(\mathbf z)F(\mathbf j_F)\\
&\qquad-G(\mathbf z)\mathscr H(\mathbf j_F).
\end{aligned}
\tag{B.OD22}
\]
All four face comparisons and all four product terms are required. For the corrected discrepancy
\(\widehat R=\mathbf c_RJ_0-J_1\mathbf c_L-\mathbf B-\mathbf b\),
\[
\begin{aligned}
&\mathscr H(\widehat R)\\
&\quad=\mathscr H(\mathbf c_R)F(J_0)\\
&\qquad+G(\mathbf c_R)\mathscr H(J_0)\\
&\qquad-\mathscr H(J_1)F(\mathbf c_L)\\
&\qquad+G(J_1)\mathscr H(\mathbf c_L)\\
&\qquad-\mathscr H(\mathbf B)\\
&\qquad-\mathscr H(\mathbf b).
\end{aligned}
\tag{B.OD23}
\]
If \(D\mathbf P=\widehat R\), its next comparison must satisfy
\[
\begin{aligned}
D\mathscr H(\mathbf P)
 &={}\alpha_tF(\mathbf P)\\
 &-G(\mathbf P)\alpha_s\\
 &-\mathscr H(\widehat R).
\end{aligned}
\tag{B.OD24}
\]
Here \(\mathscr H(\mathbf P)\) has graph degree \(-3\); its third coordinate has degree \(-4\). The right side is closed by (B.OD21), but closedness alone does not identify its **actual target**. That target includes the original \(\Gamma\)-terms and the endpoint bridges. To use the relative whole-cone lift, one must first supply its target primitive, or prove the target is zero, before restriction. Acyclicity of the source resolution cone is not a replacement for this target comparison.

Consequently (B.OD20) supplies data needed by this attachment, not permission to discard \(\Gamma_{o,d}\), replace earlier triangle choices, omit \(K_2\), or infer a complete changing-parameter cube. Global mixed-array compatibility, geometric nearby-cycle multiplicative descent, coefficient completion, strict-heart higher effacement and recursive provider closure retain their stated scopes.


### Paste successive base-change faces with their triangle witnesses

**Proposition B.1ba (the complete fixed ordered paste).** For two successive
base changes on the common whole model of [B.1az](#compare-successive-base-change-kernels-and-their-resolved-mates),
the four faces of the ordered composite admit a comparison with the pasted
first and second faces. The comparison retains the original unit, counit,
endpoint and triangle witnesses, including a degree-minus-four coordinate.
All maps below are in the decorated graph of [B.1ao](#encode-all-four-faces-in-one-arrow-graph),
with their actual target labels as in (B.FT2). This proposition concerns the
fixed ordered choice; the next proposition compares it with prescribed
direct choices.

#### Receiving objects and the complete comparison pairs

Apply [the normalized transport](#transport-the-seven-object-diagram-with-canonical-new-units)
to the first square using the second square's \(S_2,V_2,\vartheta_2\).
Subscript \(T\) means this normalized transport, not an unidentified
replacement. Put
\[
\begin{gathered}
X_1=L_1S_1Q_0,\\
X_{21}=L_2S_2S_1Q_0,\\
X_2=L_2S_2Q_1,\\
Z_A=V_2X_1,\\ Z_C=V_2V_1M_0,\\
s=\vartheta_{2,S_1Q_0},\\
t=V_2\vartheta_{1,Q_0},\\
s_1=\vartheta_{2,Q_1},\\
h_0=L_2S_2c_1,\\ h=V_2L_1c_1,\\
\vartheta_{21}=(V_2\vartheta_1)(\vartheta_2S_1),\\
s_1h_0=hs.
\end{gathered}
\tag{B.OP1}
\]
Use \(Q,R,B,Q_2^u\) for the canonical unit graph objects on
\(S_2S_1Q_0,S_2S_1R_0,S_2Q_1,Q_2\), respectively. The normalized
first-square nonunit vertices are \(A_T,C_T,R_T,Q_T\), with actual targets
\(Z_A,Z_C,V_2M_1,V_2V_1N\). Their structure maps are those of (B.UT1);
they are not assumed to be quasi-isomorphisms.

Choose whole replacements \(A_+\to U_2Z_A\), \(C_+\to U_2Z_C\).
Keep the combined ordered replacements \(A_{21}\to U_2X_{21}\),
\(C_{21}\to U_2Z_C\), and the second-square replacements
\(A_2\to U_2X_2\), \(C_2\to U_2V_2M_1\),
\(R_2\to U_2M_2\), \(Q_2\to U_2V_2V_1N\).
In particular \(A_2\) and \(A_{21}\) have different targets.

The resolved-mate construction (B.BM16), with its original witness, gives
\(m_A:A_T\to A_+\), \(m_C:C_T\to C_+\),
\(m_R:R_T\to C_2\), \(m_Q:Q_T\to Q_2\), all with identity target
component. For example
\(m_R=(c_{M2},1,b_{M2})\) and \(m_Q=(c_2,1,b_2)\).
The second-resolution route is the directed span
\[
R_T\xrightarrow{m_R}C_2
\xleftarrow{v_2}A_2\xrightarrow{a_2}R_2.
\]
Its target maps are \(1,s_1,L_2c_2\); none of these arrows is inverted.

Write \(p=v_T\), and choose the following closed graph arrows by whole
Hom lifting through the receiving replacement. The last column specifies
their actual target component.

| Arrow | Graph source and target | Target component |
|---|---|---|
| \(v_+\) | \(A_+\to C_+\) | \(t\) |
| \(i_A\) | \(A_{21}\to A_+\) | \(s\) |
| \(i_C\) | \(C_{21}\to C_+\) | \(1\) |
| \(a_+\) | \(A_+\to C_2\) | \(h\) |
| \(f\) | \(A_{21}\to A_2\) | \(h_0\) |
| \(w_+\) | \(C_+\to Q_2\) | \(V_2V_1e_0\) |

Each such arrow is \((a,w,h_a)\) with its entire witness
\(r'a-U_2(w)r=dh_a\). The transported \(u_T,c_{MT},a_T,w_T,z_T\)
and faces retain (B.UT7)–(B.UT9)'s targets and transposed witnesses.
Let \(l_1=A(S_2c_1)\), \(l_2=A(c_2)\), and use the ordered choices
\(c_{L21}=l_2l_1\), \(c_{R21}=m_Qc_{RT}\). Their full witness is the
two-term formula (B.BM17), not a new chosen primitive.

For each displayed difference below its target component is zero. The
whole Hom theorem [B.ND7](#natural-diagram-resolutions-and-relative-coherent-lifts)
gives the indicated degree-minus-one full comparison:
\[
\begin{aligned}
DF_p&=m_Cp\\&\quad-v_+m_A,\\
DF_{21}&=i_Cv_{21}\\&\quad-v_+i_A,\\
DF_u&=m_Au_T\\&\quad-i_Au_{21},\\
DF_c&=m_Cc_{MT}\\&\quad-i_Cc_{M21},\\
DF_{aT}&=m_Ra_T\\&\quad-a_+m_A,\\
DF_{a21}&=v_2f\\&\quad-a_+i_A.
\end{aligned}
\tag{B.OP2}
\]
\[
\begin{aligned}
DK_f&=fu_{21}\\&\quad-u_{X2}l_1,\\
DF_R&=a_2f\\&\quad-a_{21},\\
DG_{wT}&=m_Qw_T\\&\quad-w_+m_C,\\
DG_{w21}&=w_{21}\\&\quad-w_+i_C.
\end{aligned}
\tag{B.OP3}
\]
For precision, a closed difference \((\Delta,0,I)\) is lifted as
\((J,0,K)\), where \(dJ=\Delta\), \(r'J-I=dK\).
The witness K has degree −2 and is retained. The target equalities for
OP2–3 follow from (B.OP1), \(\vartheta_{21}=ts\), and the common
targets in the table. For \(F_c\), the common actual target is
\(V_2V_1e_0^M\vartheta_{21,R_0}\).

The prescribed beta receiving face is
\(B_+=(t_+,V_2\beta_1,k_+):A_+\to Q_2\), with
\[
DB_+=w_2a_+-w_+v_+.
\]
Indeed the target differential is
\((V_2e_1)h-(V_2V_1e_0)t\). The full Hom-cone witness is
\[
\begin{aligned}
I_+={}&U_2(V_2\beta_1)r_{A+}+h_{w2}a_+\\
 &+U_2(V_2e_1)h_{a+}-h_{w+}v_+\\
 &-U_2(V_2V_1e_0)h_{v+}.
\end{aligned}
\]
Thus \(dt_+=w_{2,\mathrm{src}}a_+-w_{+,\mathrm{src}}v_+\) and
\(q_2t_+-I_+=dk_+\), by (B.RJ9). This uses the original beta target,
not an arbitrary homotopy with the same endpoints.

#### Six face residuals with their full witnesses

The [endpoint bridge and product rule](#attach-the-horizontal-counit-bridge-with-its-second-boundary)
give the following normalized second-square arrows. Let \(E_R\) be the
canonical-unit-to-\(R_T\) arrow, and \(E_Q\) the canonical-unit-to-\(Q_T\)
arrow. Write \(s_{u1}=A(S_2u_1)\), \(s_{z1}=A(S_2z_1)\).
Define
\[
\begin{aligned}
L&=(0,V_2\lambda_1s_1,0),\\
DL&=E_Rs_{u1}-u_{1T},\\
B_\alpha&=(0,V_2\alpha_1\vartheta_{2,R_1},0),\\
DB_\alpha&=m_QE_Qs_{z1}\\&\quad-m_Qz_TE_R,\\
h_{U2}&=j_{U2}-m_RL,\\
Dh_{U2}&=m_Ru_{1T}\\&\quad-v_2u_{X2},\\
j_{C2}&=G_zE_R+B_\alpha,\\
DG_z&=m_Qz_T\\&\quad-w_2m_R.
\end{aligned}
\tag{B.OP4}
\]
Here \(h_{U2}=(J_{U2},0,K_{U2})\) and
\(G_z=(J_{C2},0,K_{C2}):R_T\to Q_2\) are the original full pairs.
Precomposition with \(E_R\), whose source map is the identity and whose
witness is zero, retains both entries. This does not require an inverse
of \(E_R\), and does not delete the nonzero targets of \(j_{U2},j_{C2}\).

In the following formulas su and sz are the normalized initial unit arrows,
and \(j_{B*}\) denotes the beta face \(j_{\beta*}\), not the endpoint
bridge b. Put
\[
\begin{aligned}
E_U={}&m_Cj_{UT}\\&-i_Cj_{U21}\\
 &-F_csu+F_pu_T\\
 &+v_+F_u-F_{21}u_{21},\\
E_{Fj}={}&m_Rj_{FT}\\&-h_{U2}l_1\\
 &+a_+F_u\\&-F_{a21}u_{21}\\
 &+v_2K_f\\&+F_{aT}u_T,\\
E_F={}&j_{F2}l_1-j_{F21}\\
 &-a_2K_f+F_Ru_{21}.
\end{aligned}
\tag{B.OP5}
\]
\[
\begin{aligned}
E_C={}&m_Qj_{CT}\\&-j_{C21}\\
 &+w_+F_c\\&+G_{wT}c_{MT}\\
 &-G_{w21}c_{M21},\\
E_{Bo}={}&m_Qj_{BT}\\&-B_+m_A\\
 &-w_2F_{aT}\\&+w_+F_p\\
 &-G_za_T\\&+G_{wT}p,\\
E_{B21}={}&j_{B2}f\\&+B_+i_A\\
 &-j_{B21}\\&-z_2F_R\\
 &+w_2F_{a21}\\&-w_+F_{21}\\
 &-G_{w21}v_{21}.
\end{aligned}
\tag{B.OP6}
\]
Differentiate these six expressions using OP2–4 and the four original
face equations (B.FG8) or their transported versions (B.UT9).
Every interior path occurs twice with opposite coefficients, hence
all six displayed residuals have zero differential.
Their actual targets vanish as well. For U and C the two nonzero targets
agree by \(\vartheta_{21}=(V_2\vartheta_1)(\vartheta_2S_1)\).
For the beta comparisons this uses both terms of
\[
\beta_{21}=\beta_2h_0+(V_2\beta_1)s.
\tag{B.OP7}
\]
The other terms have zero target by their stated full comparison pairs.

All sources remain whole h-projective. The receiving replacements for
these six cycles are respectively \(C_+,C_2,R_2,Q_2,Q_2,Q_2\), all
quasi-isomorphic to their stated targets. The shifted whole Hom cones
therefore give full zero-target degree-minus-two fillers
\(H_U,H_{Fj},H_F,H_C,H_{Bo},H_{B21}\) with differentials the corresponding
E's. Each third coordinate has degree −3. The six lower faces and all
these chosen fillers will remain in the next formula.

#### The common four-face and triangle boundary

Let \(J_{01}=A(S_2J_1)\), and let \(J_{1T}\) be the normalized transport
of the first square's original triangle. Their boundaries are
\(DJ_{01}=s_{z1}s_{u1}-1\) and \(DJ_{1T}=z_Tu_{1T}-E_Q\).
The degree-minus-one old triangle's third coordinate contributes a further
bridge, now of degree −2:
\[
\begin{aligned}
G&=(0,\gamma_2,0),\\
\gamma_2&=V_2\Gamma_1s_1,\\
DG&=m_QE_QJ_{01}\\&\quad-m_QJ_{1T}\\
 &\quad-B_\alpha s_{u1}\\&\quad-m_Qz_TL.
\end{aligned}
\tag{B.OP8}
\]
This is (B.HB5) applied to \((J_1,0,K_1)\), followed by the full product
rule (B.HB6); \(\Gamma_1=\operatorname{Adj}_1^{-1}K_1\).
The bridge of \(E_Q\) is zero, but the bridge of this triangle is generally
not zero. No part of K1 is omitted.

Form the three four-face sums, with all products in the decorated category:
\[
\begin{aligned}
&B_T=j_{CT}su\\&\qquad+w_Tj_{UT}\\
&\qquad-j_{BT}u_T\\&\qquad-z_Tj_{FT},\\
&B_2=j_{C2}s_{u1}\\&\qquad+w_2j_{U2}\\
&\qquad-j_{B2}u_{X2}\\&\qquad-z_2j_{F2},\\
&B_{21}=j_{C21}su\\&\qquad+w_{21}j_{U21}\\
&\qquad-j_{B21}u_{21}\\&\qquad-z_2j_{F21},\\
&C_\triangle=m_QE_QJ_{01}\\
&\qquad-m_QJ_{1T},\\
&B_{\mathrm{comp}}\\
&\quad=m_QB_T\\&\qquad+(B_2-C_\triangle)l_1.
\end{aligned}
\tag{B.OP9}
\]
Both \(DB_{21}\) and \(DB_{\mathrm{comp}}\) equal
\(m_Qc_{RT}szsu-z_2u_2l_2l_1\). The intermediate triangle
\(C_\triangle\) is required for this equality.

Retain the following degree-minus-two cross terms and fillers:
\[
\begin{aligned}
&\Psi=G_{w21}j_{U21}\\&\qquad-G_{wT}j_{UT}\\
&\qquad-B_+F_u\\&\qquad+j_{B2}K_f\\&\qquad+G_zj_{FT},\\
&H_\Sigma=H_{Bo}u_T\\&\qquad-H_Csu\\
&\qquad-w_+H_U\\&\qquad+H_{B21}u_{21}\\
&\qquad+z_2H_F\\&\qquad+w_2H_{Fj},\\
&K_{\mathrm{paste}}\\&\quad=G_zLl_1+\Psi+H_\Sigma.
\end{aligned}
\tag{B.OP10}
\]
Substitution of OP5–6 gives
\[
\begin{aligned}
&B_{21}-B_{\mathrm{comp}}\\
&\quad=D(Gl_1+K_{\mathrm{paste}}).
\end{aligned}
\tag{B.OP11}
\]
To see the cancellation explicitly, first replace the six E's by their
displayed boundaries. Their unmatched products are exactly the five terms
in \(D\Psi\). Using OP4 and OP8 for the remaining second-square terms gives
\[
\begin{aligned}
B_2&-\bigl(G_zu_{1T}+w_2h_{U2}\\
 &\qquad-j_{B2}u_{X2}-z_2j_{F2}\bigr)\\
 &=C_\triangle-DG-D(G_zL).
\end{aligned}
\]
This is the remaining contribution to OP11, with its graded signs.
Every term of \(K_{\mathrm{paste}}\) has actual target zero, whereas
\(Gl_1\) has target \(\gamma_2h_0\).

The endpoint bridge is
\(b_{21}=b_2l_1+m_Qb_{1T}\). Use the corrected discrepancies of (B.FG10)
and the original full triangle fillers \(P_{1T},P_2,P_{21}\). Then
\[
\begin{aligned}
&P_{\mathrm{assembled}}\\
&\quad=m_QP_{1T}+P_2l_1\\
&\qquad-Gl_1-K_{\mathrm{paste}},\\
&DP_{\mathrm{assembled}}=\widehat R_{21},\\
&(P_{\mathrm{assembled}})_Z=\gamma_{21},\\
&\gamma_{21}=V_2V_1\Gamma_0\vartheta_{21,Q_0}.
\end{aligned}
\tag{B.OP12}
\]
Indeed the sum of the first two boundaries differs from
\(\widehat R_{21}\) by \(D(Gl_1+K_{\mathrm{paste}})\).
In the target component, the additional \(\gamma_2h_0\) from \(P_2l_1\)
is canceled by \(Gl_1\), not discarded. Hence
\(P_{\mathrm{assembled}}-P_{21}\) is closed with actual target zero.
The whole Hom cone through \(q_2\) supplies
\[
\begin{gathered}
\Omega=(\Omega_{\mathrm{src}},0,W_\Omega),\\
D\Omega=P_{\mathrm{assembled}}-P_{21},\\
|\Omega_{\mathrm{src}}|=-3,\\
|W_\Omega|=-4.
\end{gathered}
\tag{B.OP13}
\]
This compares the original specified triangle choices and retains all six
face fillers. It establishes the fixed ordered paste, not compatibility
under every geometric change of index. The common whole-source hypotheses
and re-resolution requirement of (B.CE11) remain in force. \(\square\)


### Compare the prescribed ordered and direct triangle data

**Proposition B.1bb (the fixed seven-object higher comparison).** The actual
ordered/direct kernel and inverse comparisons of [B.1az](#compare-successive-base-change-kernels-and-their-resolved-mates)
extend to the seven-object and triangle data of [B.1ao](#encode-all-four-faces-in-one-arrow-graph)
on the specified common whole model. The higher comparison has an explicit
actual target primitive and retains its degree-minus-four third coordinate.
This is a comparison of the fixed closed two-base-change diagram, not a
claim about every changing-parameter or nonzero-degree cube record.

#### Preserve the two realizations

Use the same receiving adjunction \(L=L_2\dashv U=U_2\), the initial
\(L_0\dashv U_0\), and the original initial triangle data
\(Q_0,R_0,u_0,z_0,J_0,\lambda_0,\alpha_0,\Gamma_0\).
Write \(F=d\) and \(G=o\) for the direct and ordered realizations, respectively.
Retain their independently prescribed replacements and all source, target and
third coordinates. Every source used in a Hom lift is h-projective on the
same whole free parameter diagram, not merely at its individual values.

The exact RK/KC comparison graphs of B.OD11–19 provide closed degree-zero
\(s:S_d\to S_o\), \(v:V_d\to V_o\), and the specified degree-minus-one
natural transformation
\[
\begin{gathered}
 J:LS_d\longrightarrow V_oL_0,\\
 dJ=\vartheta_oLs-vL_0\vartheta_d.
\end{gathered}\tag{B.HT1}
\]
Here J is the three-term chosen-inverse comparison of B.OD16, including its
two inverse-homotopy terms. If intervening whole word replacements occur,
their actual comparison graphs have already been transported as required
there. Merely identifying represented objects would not supply this input.

For the receiving replacements and mate lifts keep
\[
\begin{aligned}
 &q_\sigma c_\sigma-\zeta_\sigma=db_\sigma,\\
 &\zeta_\sigma\\&\quad=\operatorname{Adj}(V_\sigma e_0\vartheta_\sigma),\\
 &q_ot-U(v_N)q_d=dw,\\
 &dj=c_os-tc_d,\\
 &q_oj-K_M=dk,\\
 &K_M=\operatorname{Adj}(V_oe_0J)\\
 &\qquad+b_os\\&\qquad-U(v_N)b_d\\&\qquad-wc_d.
\end{aligned} \tag{B.HT2}
\]
Set \(e_\sigma=\epsilon Lq_\sigma\),
\(\beta_\sigma=\operatorname{Adj}^{-1}b_\sigma\),
\(\beta_t=\operatorname{Adj}^{-1}w\), and
\(\Gamma_{o,d}=\operatorname{Adj}^{-1}k\). The full Hom adjunction gives
\[
\begin{aligned}
d\beta_t&=e_oLt-v_Ne_d,\\
d\Gamma_{o,d}
 &=e_oLj-V_oe_0J\\
 &\quad-\beta_oLs+v_N\beta_d\\
 &\quad+\beta_tLc_d.
\end{aligned} \tag{B.HT3}
\]
All maps in B.HT3 are actual target-category maps before applying U. In
particular the third coordinate k has not disappeared.

#### Seven vertices, with their actual comparison maps

Use the decorated category [(B.FT2)](#transport-the-whole-four-face-diagram-through-a-proper-refinement): its objects are \((P,Z,q:P\to UZ)\), and
\[
 D(a,w,h)=(da,dw,q'a-U(w)q-dh).
\]
The following table retains the distinct graph vertices even when their target
labels coincide. The target column of the vertex comparison is denoted
\(a_Z\), to avoid confusing it with the initial counit witness \(\alpha_0\).

| Vertex | Direct target | Ordered target | Target comparison |
|---|---|---|---|
| \(\mathsf Q_0^u\) | \(LS_dQ_0\) | \(LS_oQ_0\) | \(Ls_{Q_0}\) |
| \(\mathsf R_0^u\) | \(LS_dR_0\) | \(LS_oR_0\) | \(Ls_{R_0}\) |
| \(\mathsf A\) | \(LS_dQ_0\) | \(LS_oQ_0\) | \(Ls_{Q_0}\) |
| \(\mathsf C\) | \(V_dM_0\) | \(V_oM_0\) | \(v_{M_0}\) |
| \(\mathsf Q_1^u\) | \(LQ_d\) | \(LQ_o\) | \(Lt\) |
| \(\mathsf R_1\) | \(LQ_d\) | \(LQ_o\) | \(Lt\) |
| \(\mathsf Q_1^q\) | \(V_dN\) | \(V_oN\) | \(v_N\) |

On the three unit vertices use \(A(s_{Q_0}),A(s_{R_0}),A(t)\), where
\(A(f)=(f,Lf,0)\). On \(\mathsf Q_1^q\) use the actual \((t,v_N,w)\).
On A, C and R use whole Hom lifts of the displayed targets through the
ordered receiving replacements \(r_{A,o},r_{C,o},\rho_o\). Retain their
degree-minus-one witnesses. These are closed full graph arrows, not inverses
of the unit or of the right mate.

#### Compare all prescribed arrows and faces

We construct a degree-minus-one comparison H with
\[
\begin{aligned}
&DH(g)+H(Dg)\\
&\quad=a_tF(g)-G(g)a_s,\\
&H(gf)=H(g)F(f)\\
&\qquad+(-1)^{|g|}G(g)H(f).
\end{aligned}\tag{B.HT4}
\]
For the fixed closed degree-zero base-change record, prescribe the following
**actual target components**. Subscripts on J indicate the resolved input;
the symbol \(\mathbf v\) in this table is the A-to-C graph arrow, not the
functor comparison v.

| Generator(s) g | \(H(g)_Z\) |
|---|---|
| \(\mathbf s_u,\mathbf s_z\) | 0 |
| \(\mathbf J_0,\mathbf u_X\) | 0 |
| \(\mathbf w,\mathbf u_1\) | 0 |
| \(\mathbf J_1,\mathbf j_F\) | 0 |
| \(\mathbf c_R\) | \(-V_oe_0J_{Q_0}\) |
| \(\mathbf c_M\) | \(-V_oe_0^MJ_{R_0}\) |
| \(\mathbf v\) | \(-J_{Q_0}\) |
| \(\mathbf c_L,\mathbf a\) | \(-Lj\) |
| \(\mathbf e_1,\mathbf z_1\) | \(-\beta_t\) |
| \(\mathbf j_U\) | \(V_o\lambda_0J_{Q_0}\) |
| \(\mathbf j_C\) | \(V_o\alpha_0J_{R_0}\) |
| \(\mathbf b,\mathbf j_\beta\) | \(\Gamma_{o,d}\) |

For the unchanged initial unit diagram, the full comparisons of su, sz and
J0 are zero by the graded naturality of the closed s. For cL use the full
comparison \(-A(j)\); no acyclicity assertion for a receiving unit is used.
Three further full comparisons are explicit:
\[
\begin{aligned}
 &H(\mathbf e_1)=(0,-\beta_t,0),\\
 &H(\mathbf c_R)\\
 &\quad=(-j,-V_oe_0J,-k),\\
 &H(\mathbf b)=(0,\Gamma_{o,d},0).
\end{aligned} \tag{B.HT5}
\]
The first two follow from B.HT2–3 and unit transposition. To check the third,
\(D\mathbf b=\mathbf e_1\mathbf c_L-\mathbf c_R\) gives
\[
 H(D\mathbf b)
 =(0,-\beta_tLc_d-e_oLj+V_oe_0J,k).
\]
Subtract this from \(a_tF(\mathbf b)-G(\mathbf b)a_s\). B.HT3 leaves
\((0,d\Gamma_{o,d},-k)=D(0,\Gamma_{o,d},0)\), since
\(U(\Gamma_{o,d})\eta=k\). This retains the original mate pair (j,k).

For the remaining generators, the target identities can be checked before
any graph lift. For instance, \(d\lambda_0=e_0^ML_0u_0-1\) gives
\[
\begin{aligned}
&H(D\mathbf j_U)_Z=-V_o(d\lambda_0)J,\\
&d(V_o\lambda_0J)+H(D\mathbf j_U)_Z\\
&\quad=-V_o\lambda_0dJ.
\end{aligned}
\]
Likewise \(d\alpha_0=e_0L_0z_0-e_0e_0^M\) verifies jC. Both b and jβ
have target boundary comparison
\(-\beta_tLc_d-e_oLj+V_oe_0J\), so B.HT3 verifies their two entries with the
same \(\Gamma_{o,d}\). For J1 the two terms \(-\beta_t\) cancel; for jF
the two terms \(-Lj\) cancel. Closed naturality verifies uX, w and u1.

Here is the full lift, not an inference from target equations alone. In a
well-founded order, suppose H has already been defined on Dg. Its residual
\[
 Z_g=a_tF(g)-G(g)a_s-H(Dg)
\]
is closed by B.HT4 on earlier generators and \(D^2g=0\). If the displayed
target component is T, the verified identity is \((Z_g)_Z=dT\).
Subtract \(D(0,T,0)\) from \(Z_g\). The result is a closed, zero-target
element of the full graph Hom complex. Except for the unit-headed arrows
handled explicitly above, every receiving vertex is one of A, C, R or Qq
with a whole quasi-isomorphic replacement. The kernel is therefore the
shifted cone of \(\operatorname{Hom}(P_d,q_o)\), acyclic by [(B.ND7)](#natural-diagram-resolutions-and-relative-coherent-lifts). Choose
a full zero-target primitive and add it to \((0,T,0)\). This produces H(g)
with exactly the prescribed target and the required third coordinate.
Earlier comparisons and all original F/G arrows and faces remain fixed.
The free presentation and B.HT4 extend this to every path; no relations of
an unexamined nonfree quotient are being imposed.

#### The actual target of the higher discrepancy

Retain all eight terms of B.OD22, even those whose target vanishes. For
\(\mathbf B=\mathbf j_C\mathbf s_u+\mathbf w\mathbf j_U
-\mathbf j_\beta\mathbf u_X-\mathbf z_1\mathbf j_F\), the table gives
\[
\begin{aligned}
 &H(\mathbf B)_Z\\
 &\quad=V_o\alpha_0J_{R_0}LS_du_0\\
 &\qquad+V_oe_0V_o\lambda_0J-\Gamma_{o,d}\\
 &\quad=V_o\bigl(\alpha_0L_0u_0\\
 &\qquad+e_0\lambda_0\bigr)J-\Gamma_{o,d}.
\end{aligned} \tag{B.HT6}
\]
The simplification uses naturality of J at the closed u0. The Hz1 term
vanishes only because the prescribed target of F(jF) is zero; Hz1 itself
is generally nonzero.

For the corrected discrepancy
\(\widehat{\mathbf R}=\mathbf c_R\mathbf J_0
-\mathbf J_1\mathbf c_L-\mathbf B-\mathbf b\), the odd-degree naturality
sign is essential:
\[
\begin{aligned}
&J_{Q_0}LS_dJ_0\\
&\quad=-V_o(L_0J_0)J_{Q_0}.
\end{aligned}\tag{B.HT7}
\]
Thus the cR J0 term contributes \(+V_o(e_0L_0J_0)J\). The J1 cL target
is zero. The two occurrences of \(\Gamma_{o,d}\), one from B.HT6 and the
other from H(b), cancel. They are not separately set to zero. Consequently
\[
\begin{aligned}
&H(\widehat{\mathbf R})_Z\\
&\quad=V_o\bigl(e_0L_0J_0\\
&\qquad-\alpha_0L_0u_0-e_0\lambda_0\bigr)J\\
&\quad=V_o(d\Gamma_0)J.
\end{aligned}\tag{B.HT8}
\]
Here \(\Gamma_0=\operatorname{Adj}_0^{-1}K_0\) retains the entire original
K0, including the nested correction required by B.NT7.

Let the original full triangle fillers be \(P_d,P_o\), with
\(DP_\sigma=\widehat R_\sigma\) and actual targets
\(\gamma_\sigma=V_\sigma\Gamma_0\vartheta_\sigma\). For B.OD24 the
closed graph residual is
\[
 Z_P=a_{Qq}P_d-P_oa_{Q0u}-H(\widehat R).
\]
Closed naturality of v at the degree-minus-two Γ0 gives
\[
\begin{aligned}
 &(Z_P)_Z=-V_o\Gamma_0dJ\\
 &\qquad-V_o(d\Gamma_0)J\\
 &\quad=d\bigl(-V_o\Gamma_0J\bigr).
\end{aligned} \tag{B.HT9}
\]
This is the required **actual target primitive**, not just closedness after
applying U. Set \(T_P=-V_o\Gamma_0J\), of degree −3. The residual
\(Z_P-D(0,T_P,0)\) is closed with target zero. Apply B.ND7 to the whole
Hom from \(S_dQ_0\) through \(q_o\), obtaining a zero-target primitive
\((h_P,0,w_P)\). Then
\[
\begin{gathered}
 H(P)=(h_P,T_P,w_P),\\
 DH(P)=Z_P,\\
 |h_P|=|T_P|=-3,\\
 |w_P|=-4.
\end{gathered}\tag{B.HT10}
\]
The third coordinate is retained. Neither Pσ nor its original third
coordinate is replaced: both occur literally in ZP.

#### Compare the ordered paste with the prescribed direct triangle

The ordered construction of [B.1ba](#paste-successive-base-change-faces-with-their-triangle-witnesses) has
\[
\begin{aligned}
&P_{\rm assembled}=m_QP_{1T}+P_2l_1\\
&\qquad-G l_1-K_{\rm paste},\\
&D\Omega=P_{\rm assembled}-P_{21}.
\end{aligned}
\]
Its actual target equals \(\gamma_o\); the Γ1 bridge cancels the additional
\(\gamma_2h_0\) rather than being discarded. The full Ω has zero target,
degree −3 and a degree-minus-four third coordinate. Take \(P_o=P_{21}\)
in B.HT10. Since the initial vertex comparison a is closed, the comparison
with the assembled filler is exactly
\[
\begin{aligned}
&H(P)_{\rm assembled}\\
&\quad=H(P)_{21}-\Omega a_{Q0u}.
\end{aligned}\tag{B.HT11}
\]
Differentiation subtracts \((P_{\rm assembled}-P_{21})a_{Q0u}\), exactly
the change in ZP. The target primitive remains TP because Ω has target
zero. This preserves the original P1T, P2, P21, all six prior face-residual
fillers, Γ0/Γ1/Γ21, and Ω's degree-minus-four witness in one explicit
fixed ordered/direct comparison. It is not a replacement of them by an
unspecified convenient primitive.

#### Scope of the comparison

The construction compares the specified closed two-step diagram on the
admitted common whole parameter model. It does not automatically extend to
every nonzero-degree record, an already prescribed horizontal gH cube,
changing-index restrictions, or mixed horizontal/vertical UQ words. In
particular H(P(gH)) has another degree and needs its own target calculation;
B.HT10 must not be used as a certificate for that next dimension. Re-resolve
after changed restriction; preserve KC signed bars and the GC/MX K2 terms.
Global geometric assembly, nearby-cycle descent, coefficient completion,
strict-heart higher effacement, recursive provider closure are not consequences of this fixed-diagram comparison.

\(\square\)


### Compare homogeneous records with their full boundary

**Proposition B.1bc (conditional homogeneous-record comparison).** The target calculation of [B.1bb](#compare-the-prescribed-ordered-and-direct-triangle-data) extends to the full record differential, provided the actual graded comparison and its lower boundary are supplied on one whole parameter model. The construction retains the mate pair and the higher third coordinate; it does not assert that the geometric higher comparison has already been constructed.

**Earlier constructions:** [B.RC](#join-the-right-triangle-comparison-to-the-cube); [B.CE](#lift-changing-diagrams-without-inverting-comparison-arrows).

The [full arrow graph B.FG](#encode-all-four-faces-in-one-arrow-graph) retains the third coordinates.

#### Exact inputs and the remaining geometric distinction

Work on one admitted whole parameter model with the receiving adjunction
\(L\dashv U\). Preserve the initial resolved triangle, including
\(Q_0,R_0,u_0,z_0,J_0,\lambda_0,\alpha_0,\Gamma_0\), and the direct and
ordered realizations of B.HT. For this calculation \(S_d,S_o,V_d,V_o\)
and the closed comparisons \(s:S_d\to S_o\), \(v:V_d\to V_o\) are fixed.
Do not identify different functors or parameter indices without their
actual transport maps. The result is an interface on a common model,
not permission to pretend that a changing-model diagram is fixed.

Let \(f\) be a homogeneous record of degree \(n\), with differential
\(\partial f\) of degree \(n+1\). Its two cells \(\theta_\sigma(f)\)
are chain-linear in the record:
\(d\theta_\sigma(f)=\theta_\sigma(\partial f)\).
The necessary additional datum is a graded natural, linear comparison
\(J(f):LS_d\to V_oL_0\) of degree \(n-1\), satisfying
\[
\begin{aligned}
&dJ(f)+J(\partial f)\\
&\quad=\theta_o(f)Ls\\
&\qquad-vL_0\theta_d(f).
\end{aligned}\tag{B.RCmp1}
\]
This is an input equation in the actual target category, before applying
\(U\). The closed degree-zero comparison of B.HT1 alone does not specify
\(J(f_H)\), nor its value on the boundary of a horizontal record.

For a supplied free cellular record presentation, lower values are kept
fixed. A claim over an arbitrary complex with relations would need its own
extension argument; no projectivity of that arbitrary complex is assumed.
Changing the underlying parameter index requires B.CE11 re-resolution.

The existing geometric providers supply different, indispensable data:

| Provider | Actual supplied datum | What it does not identify on its own |
|---|---|---|
| B.MX8–10 | The six-edge whole-kernel cell \((H,K)\), with \(dH=T-B\) and the common-target witness equation | \(J(f_H)\) after the chosen inverse, duality and seven-object transports |
| B.KC10–16 and B.MX12 | Signed bar/dual roofs, the resolved mate and retained nested \(K_2\) | Equality of independently prescribed higher faces |
| B.CE10–11 | Relative lifts of a checked base diagram and re-resolution on restriction | A missing base boundary |
| B.CY1–12 | A strict free cylinder realizing an already supplied comparison homotopy | A new homotopy not contained in its input |

Thus the elementary mixed cube is not absent. The specific attachment still
to verify is B.RCmp1, with its chosen geometric higher comparison and boundary,
on the common whole model.

#### The full mate pair, with its record differential

Write \(e_\sigma=\epsilon Lq_\sigma\). Keep the receiving comparison
\((t,v_N,w)\), with \(q_ot-U(v_N)q_d=dw\), and put
\(\beta_t=\operatorname{Adj}^{-1}w\).
The RC records retain
\[
\begin{aligned}
dc_\sigma(f)&=c_\sigma(\partial f),\\
db_\sigma(f)&+b_\sigma(\partial f)\\
 &=q_\sigma c_\sigma(f)\\
 &\quad-\operatorname{Adj}(V_\sigma e_0\theta_\sigma(f)).
\end{aligned}
\]
Define the actual degree-\(n-1\) map
\[
\begin{aligned}
K_M(f)&=\operatorname{Adj}(V_oe_0J(f))\\
 &\quad+b_o(f)s\\
 &\quad-U(v_N)b_d(f)-wc_d(f).
\end{aligned}
\]
Keep the full pair \(j(f),k(f)\), of degrees \(n-1,n-2\), satisfying
\[
\begin{aligned}
&dj(f)+j(\partial f)\\
&=c_o(f)s-tc_d(f),\\
&q_oj(f)-K_M(f)\\
&=dk(f)-k(\partial f).
\end{aligned}\tag{B.RCmp2}
\]
The minus sign in the second equation is not optional.
Indeed, differentiating \(K_M\), including
\(d(-wc_d)=-(dw)c_d+w c_d(\partial f)\), gives
\[
dK_M(f)+K_M(\partial f)=q_o(c_o(f)s-tc_d(f)).
\]
Consequently \((c_os-tc_d,K_M)\) is a chain map to the shifted Hom cone
with differential \(\delta(x,y)=(dx,q_ox-dy)\).
On a free cell whose lower boundary pair has already been selected,
subtract that lower pair. The remaining cone element is closed.
B.ND7 supplies its primitive through the actual whole quasi-isomorphism
\(q_o\), giving B.RCmp2 without altering the lower choices.
This is not an assertion that an objectwise cone is whole-acyclic.

Let \(\beta_\sigma(f)=\operatorname{Adj}^{-1}b_\sigma(f)\) and
\(\Gamma(f)=\operatorname{Adj}^{-1}k(f)\). Full Hom adjunction gives
\[
\begin{aligned}
&d\beta_t\\
&\quad=e_oLt-v_Ne_d,\\
&d\Gamma(f)\\
&\quad-\Gamma(\partial f)\\
&\quad=e_oLj(f)\\
&\qquad-V_oe_0J(f)\\
&\qquad-\beta_o(f)Ls\\
&\qquad+v_N\beta_d(f)\\
&\qquad+\beta_tLc_d(f).
\end{aligned}\tag{B.RCmp3}
\]
These are actual target maps; \(k\) has not been projected away.

#### The comparison on the four faces and the endpoint bridge

Use the full decorated graph differential of B.FT2 and the degree-minus-one
comparison convention
\[
\begin{aligned}
&DH(g)\\
&+H(Dg)\\
&\quad=a_tF(g)\\
&\qquad-G(g)a_s,\\
&H(gh)\\
&=H(g)F(h)\\
&+(-1)^{|g|}\\
&\quad G(g)H(h).
\end{aligned}\tag{B.RCmp4}
\]
Here \(F=d,G=o\); \(a\) is the seven-vertex comparison of B.HT.
The fixed generators and vertex maps remain as in B.HT4–5.
For the record-dependent arrows the target entries are
\[
\begin{array}{c|c}
g(f)&H(g(f))_Z\\ \hline
\mathbf c_R&-V_oe_0J\\
\mathbf c_M&-V_oe_0^MJ_{R_0}\\
\mathbf v&-J\\
\mathbf c_L,\mathbf a&-Lj\\
\mathbf j_U&V_o\lambda_0J\\
\mathbf j_C&V_o\alpha_0J_{R_0}\\
\mathbf j_F&0\\
\mathbf b,\mathbf j_\beta&\Gamma
\end{array} \tag{B.RCmp5}
\]
The full formulas, not just their target coordinates, include
\[
\begin{gathered}
H(\mathbf c_L(f))\\
=-A(j(f)),\\
H(\mathbf c_R(f))\\
=(-j(f),\\
-V_oe_0J(f),\\
-k(f)),\\
H(\mathbf b(f))\\
=(0,\Gamma(f),0).
\end{gathered}\tag{B.RCmp6}
\]

The record differential is essential. B.FG6 says
\(D\mathbf b(f)=\mathbf e_1\mathbf c_L(f)-\mathbf c_R(f)
-\mathbf b(\partial f)\). Hence
\[
\begin{aligned}
&H(D\mathbf b(f))\\
&\quad=(0,-\beta_tLc_d\\
&\qquad-e_oLj+V_oe_0J\\
&\qquad-\Gamma(\partial f),k(f)).
\end{aligned}
\]
Adding \(DH(\mathbf b(f))=(0,d\Gamma(f),-k(f))\) and using
B.RCmp3 proves the full equation B.RCmp4. The last coordinates cancel
because they were retained, not because they were assumed zero.
For \(\mathbf c_R\), the last coordinate of
\(DH(\mathbf c_R(f))+H(\mathbf c_R(\partial f))\) is
\[
\begin{aligned}
&-q_oj+\operatorname{Adj}(V_oe_0J)\\
&\quad+dk-k(\partial f)\\
&\qquad=wc_d+U(v_N)b_d-b_os.
\end{aligned}
\]
This is exactly the last coordinate of its comparison boundary.

For the unit face, the lower-boundary contribution is
\[
H(D\mathbf j_U(f))_Z
 =-V_o(d\lambda_0)J(f)-V_o\lambda_0J(\partial f).
\]
Adding \(d(V_o\lambda_0J(f))\) leaves
\(-V_o\lambda_0(dJ(f)+J(\partial f))\), the required boundary.
The counit face is identical with \(\alpha_0\) and its actual differential.
The \(\mathbf j_\beta\) face uses B.RCmp3; the \(\mathbf j_F\) terms cancel.
Thus the table is compatible with the *nonclosed* record, not only with
its degree-zero endpoints.

At each remaining free generator subtract its already fixed lower comparison
and the differential of the prescribed target triple \((0,T,0)\).
The residual is closed with target zero. For the non-unit receiving
vertices the whole Hom cone through the recorded replacement is acyclic.
Lift this residual there, keeping the third coordinate. The unit-headed
arrows use the explicit \(A(j)\) and naturality formulas above, not
acyclicity of a unit. This is the same relative construction as B.HT,
now with the record differential retained.

#### Target of the triangle comparison in every record degree

B.FG10 uses the degree-dependent discrepancy
\[
\begin{aligned}
\widehat{\mathbf R}(f)&=(-1)^n\mathbf c_R(f)\mathbf J_0\\
 &\quad-\mathbf J_1\mathbf c_L(f)\\
 &\quad-\mathbf B(f)-\mathbf b(f).
\end{aligned}
\]
Since \(J(f)\) has degree \(n-1\), its actual graded naturality is
\[
\begin{gathered}
J_{Q_0}(f)LS_dJ_0\\
=(-1)^{n-1}\\
V_o(L_0J_0)\\
\qquad J_{Q_0}(f).
\end{gathered}\tag{B.RCmp7}
\]
Multiplying this by the coefficient \((-1)^n\) in the discrepancy
and by the minus sign in \(H(\mathbf c_R)\) gives a *positive*
\(V_o(e_0L_0J_0)J(f)\), for every \(n\).
The \(\mathbf J_1\mathbf c_L\) target vanishes, while
\[
H(\mathbf B(f))_Z
 =V_o(\alpha_0L_0u_0+e_0\lambda_0)J(f)-\Gamma(f).
\]
The two \(\Gamma(f)\) occurrences cancel. Consequently
\[
\begin{gathered}
H(\widehat{\mathbf R}(f))_Z\\
=V_o(d\Gamma_0)J(f).
\end{gathered}\tag{B.RCmp8}
\]

For \(g=(f,p)\) in the full RC record complex, B.FG12 says
\(D\mathbf P_\sigma(g)=\mathbf P_\sigma(\partial g)
+\widehat{\mathbf R}_\sigma(f)\). Its actual target is
\(V_\sigma\Gamma_0\theta_\sigma(f)\).
Put
\[
\begin{aligned}
Z(g)&=a_{Qq}\mathbf P_d(g)-\mathbf P_o(g)a_{Q0u}
                -H(\widehat{\mathbf R}(f)),\\
T(g)&=-V_o\Gamma_0J(f).
\end{aligned}
\]
Closed naturality of \(v\), B.RCmp1 and B.RCmp8 give the exact identity
\[
\begin{gathered}
Z(g)_Z\\
=dT(g)+T(\partial g).
\end{gathered}\tag{B.RCmp9}
\]
In detail the right side is
\(-V_o(d\Gamma_0)J(f)-V_o\Gamma_0[dJ(f)+J(\partial f)]\).
There is no acyclicity assumption on the actual target category.
If the lower comparisons are already given, subtract
\(H(\mathbf P(\partial g))\) from \(Z(g)\), then subtract
\(D(0,T(g),0)\). The full residual is a closed zero-target graph element.
The whole Hom cone supplies its primitive. This gives
\[
\begin{gathered}
DH(\mathbf P(g))\\
+H(\mathbf P(\partial g))\\
=Z(g),\\
H(\mathbf P(g))_Z\\
=T(g),
\end{gathered}\tag{B.RCmp10}
\]
without replacing either original \(\mathbf P_\sigma\) or its witnesses.
The degrees are
\[
\begin{gathered}
|\mathbf P(g)|=n-2,\\
|H(\mathbf P(g))|=|T(g)|=n-3,\\
|\text{third coordinate of }H(\mathbf P(g))|\\
=n-4.
\end{gathered}
\]

#### The horizontal boundary and the scope of the result

For the recorded \(g_H\) with \(|g_H|=-1\) and
\(\partial g_H=g_T-g_B\), B.RCmp10 becomes
\[
\begin{aligned}
&DH(\mathbf P(g_H))\\
&=a\mathbf P_d(g_H)\\
&-\mathbf P_o(g_H)a\\
&-H(\widehat{\mathbf R}(f_H))\\
&-H(\mathbf P(g_T))\\
&+H(\mathbf P(g_B)).
\end{aligned}\tag{B.RCmp11}
\]
Its target primitive is \(-V_o\Gamma_0J(f_H)\), of degree minus four;
its new third coordinate has degree minus five.
The old \(\mathbf P(g_H)\) remains degree minus three with its original
degree-minus-four third coordinate. The two must not be conflated.
The endpoint target terms \(-T(g_T)+T(g_B)\) are required. Applying the
closed-record B.HT9 equation without them leaves a nonzero boundary term.

This establishes the target and full-lift interface *given* B.RCmp1–3 on
the actual common model. It does not construct the geometric
\(J(f_H)\). That map, its endpoints and the corresponding mate pair require
compatible representatives through the KC/GC/MX and HN roofs, preserving the relative unit face,
both inverse witnesses, signed bar coefficients, \(K_2\), and the specified ordered
\(\Omega\). Applying the fixed-degree \(\Omega\) formula to a nonclosed family additionally
requires its family differential.

This conditional comparison does not establish all-array coherence,
nearby-cycle descent, coefficient completion or the existence of its geometric inputs.


### Keep the inverse witnesses and their higher obstruction

**Proposition B.1bd (inverse witnesses and the obstruction to extending endpoints).** The fixed comparison of [B.1az](#compare-successive-base-change-kernels-and-their-resolved-mates) does not imply that arbitrary endpoint homotopies extend over a higher cell. The obstruction is an explicit whole-Hom class. There is also an explicit alternative inverse package with two triangle coherences; its closed displacement from the original package must be retained.

**Earlier constructions:** [B.CY](#strictify-the-recorded-comparison-homotopy-on-a-free-cylinder); [B.RCmp](#compare-homogeneous-records-with-their-full-boundary).

#### 1. The exact higher obstruction

On the actual common model required by B.RCmp1, write the two mixed cells as
\(\theta_{d,H},\theta_{o,H}\), with
\(d\theta_{\sigma,H}=\theta_{\sigma,T}-\theta_{\sigma,B}\).
Let the already chosen endpoint inverse comparisons satisfy
\[
dJ_E=\theta_{o,E}Ls-vL_0\theta_{d,E},\qquad E=T,B.
\]
The required comparison on the higher record must satisfy
\[
\begin{aligned}
\mathcal O&=\theta_{o,H}Ls\\
&\quad-vL_0\theta_{d,H}\\
&\quad-J_T+J_B,\\
dJ_H&=\mathcal O,\\
|\mathcal O|&=-1,\quad |J_H|=-2.
\end{aligned}\tag{B.IW1}
\]
Differentiation cancels the four endpoint terms, so \(d\mathcal O=0\).
Existence with the stated fixed endpoints is therefore exactly vanishing
of its class in the **whole natural Hom complex**
\[
[\mathcal O]\in
H^{-1}\operatorname{Hom}(LS_d,V_oL_0).
\]
This is not the acyclic zero-target kernel of a resolution graph.
It cannot be filled merely because a receiving replacement is a
quasi-isomorphism or because the two endpoints have the same represented
object. If the actual geometry supplies a primitive, that precise primitive
or its full comparison is needed.

#### 2. Why pairwise inverse equations are insufficient

This example tests the inference, not the actual geometric kernels.
Let \(E^0=E^1=\mathbb Z\), all other degrees vanish, and let the
differential of \(E\) be zero. The map
\(a:E^1\to E^0\) given by the identity is a nonzero degree-minus-one
endomorphism; every Hom differential is zero and
\(\operatorname{End}^{-2}(E)=0\).

Take every kernel comparison, inverse, roof and endpoint comparison map
to be \(1_E\). Take the right-kernel mixed comparisons and their witnesses
to be zero. All the ordinary inverse equations
\[
d\ell=\theta\beta-1,\qquad dr=\beta\theta-1
\]
then hold for any degree-minus-one \(\ell,r\).
At the top endpoint choose \(\ell_{o,T}=a,r_{d,T}=0\).
At the bottom choose \(\ell_{o,B}=r_{d,B}=0\); take all other inverse
witnesses to be zero.

The literal B.OD16 formula
\[
J=-\theta_oH_R\theta_d+\ell_oX\theta_d-\theta_oYr_d
\]
gives \(J_T=a,J_B=0\). Both satisfy their required closed endpoint
equations. The two higher inverse cells may both be zero because their
endpoint inverse maps are equal. Nevertheless B.IW1 gives
\(\mathcal O=-a\), which has no degree-minus-two primitive.

Thus valid inverse maps, both valid inverse homotopies, and a supplied
mixed kernel cube do not by themselves establish compatibility of
*arbitrarily selected* endpoint comparison homotopies. This does not
invalidate B.OD16 or the conditional RCmp calculation. It prevents
promoting them to an unconditional higher geometric attachment.

#### 3. A concrete triangle-coherent inverse package

Let \(\beta:A\to B,\theta:B\to A\) be closed degree-zero maps on the
whole models, with the retained old witnesses
\[
d\ell=\theta\beta-1_A,\qquad dr=\beta\theta-1_B.
\]
Define the closed inverse-coherence defect and an additional left witness
\[
\begin{gathered}
\delta=\beta\ell-r\beta,\\
d\delta=0,\\
\ell^{c}=\ell-\theta\delta.
\end{gathered}\tag{B.IW2}
\]
The original \(\ell,r\) are not deleted or renamed. The new witness
\(\ell^c\) has the same differential as \(\ell\), but their difference
\(-\theta\delta\) is only known to be closed, not a boundary.

Set
\[
\tau=-r\delta.
\]
Then, by direct differentiation,
\[
\begin{gathered}
d\ell^c=\theta\beta-1_A,\\
d\tau=\beta\ell^c-r\beta.
\end{gathered}\tag{B.IW3}
\]
Indeed the right side of the second equation is
\(\delta-\beta\theta\delta=-(dr)\delta=d(-r\delta)\).
This adds an explicit degree-minus-two coherence without imposing
acyclicity on \(\operatorname{Hom}(A,B)\).

The opposite triangle has an explicit witness too. Put
\[
\begin{aligned}
\delta_R&=\theta r-\ell^c\theta,\\
Q&=r^2-\tau\theta,\\
\sigma&=\theta Q-\ell^c\delta_R .
\end{aligned} \tag{B.IW4}
\]
Here \(|\delta_R|=-1\), \(|Q|=|\sigma|=-2\), and the maps are respectively
\(B\to A,B\to B,B\to A\). Their differentials give
\[
\begin{gathered}
d\delta_R=0,\\
dQ=\beta\delta_R,\\
d\sigma=\delta_R.
\end{gathered}\tag{B.IW5}
\]
For the middle identity,
\[
\begin{aligned}
&d(r^2-\tau\theta)\\
&\quad=(\beta\theta-1)r-r(\beta\theta-1)\\
&\qquad-(\beta\ell^c-r\beta)\theta\\
&\quad=\beta(\theta r-\ell^c\theta).
\end{aligned}
\]
The last follows by subtracting
\(d(\ell^c\delta_R)=(\theta\beta-1)\delta_R\)
from \(d(\theta Q)=\theta\beta\delta_R\).
All products, signs, source/target types and degrees are literal.

These polynomial formulas are whole natural maps when their inputs are.
They do not require evaluating an inverse on an unresolved right adjoint.
They supply the two displayed triangle coherences, not an unspecified
infinite coherent inverse system.

#### 4. The old B.OD16 comparison is retained with its exact displacement

For the original square
\[
H_R:A_d\to B_o[-1],\qquad
dH_R=\beta_oX-Y\beta_d,
\]
retain its full roof witness as well as both pairs of inverse homotopies.
Changing only the left witness used on the ordered side yields the
additional comparison
\[
J^c=-\theta_oH_R\theta_d+\ell_o^cX\theta_d-\theta_oYr_d.
\]
The old and new comparisons have the same differential, and their literal
difference is
\[
\begin{gathered}
J^c=J-C,\\
C=\theta_o\delta_oX\theta_d,\\
dC=0.
\end{gathered}\tag{B.IW6}
\]
There is no claim that \(C\) is exact. In the example above it is the
nonzero map \(a\).

For the fixed higher input of B.IW1 this changes the obstruction by
\[
\mathcal O^c=\mathcal O+C_T-C_B, \tag{B.IW7}
\]
provided the actual \(\theta_{\sigma,H}\) are kept unchanged. The example
then has zero obstruction, but the formula is not a proof of vanishing
for the geometric programme.

This distinction is operationally important: do not silently replace
the old endpoint \(J_E\) and then claim that a primitive has been found
for its original boundary. Keep \(J_E,J_E^c,C_E\) as distinct maps.
Changing the canonical comparison route must propagate these literal
closed displacements through its mate, four faces and target primitive.
The original fixed comparison is still valid as a separate route.

#### 5. Geometric application and its additional hypotheses

The geometric inputs are the MX cube, KC signed bar roofs and HN nested
folding. B.CY11 and the obstruction above show that an inverse comparison
alone does not supply arbitrary prescribed higher boundaries.

Application of B.RCmp1 requires the actual common geometric models and
their precise endpoint choices, together with either of the following:

1. a full primitive of B.IW1 retaining the endpoint \(J_T,J_B\); or
2. a coherent whole-index inverse package, its endpoint-comparison
   displacements, and a proof of the corresponding higher boundary.

B.IW2–5 give part of the second construction. Normalization of individual
inverse packages does not imply \(\mathcal O^c=0\) or construct the geometric
\(J_H\). Both alternatives retain the signed bars, nested \(K_2\), original
unit/counit/triangle witnesses and ordered \(\Omega\). A changed parameter
index requires a new resolution of the whole restricted diagram.

The counterexample concerns the inference from pairwise choices; it does
not compute the actual geometric obstruction or contradict a source theorem.
The displayed coherences do not establish all-array coherence.


### Place the mixed cube on one whole inverse model

**Proposition B.1be (the whole-index mixed roof).** The six-vertex cube of [B.MX6–10](#the-proper-open-kernel-and-the-common-mixed-cube) determines a strict signed bar roof on its free parameter category. The higher witness is an actual component of that roof. An inverse and both homotopies can be selected on the whole index before taking endpoint values. Their identification with independently chosen endpoint comparisons is a separate question.

**Earlier constructions:** [B.KC](#construct-the-whole-bimodule-compact-support-base-change-cell); [B.ND](#natural-diagram-resolutions-and-relative-coherent-lifts).

#### The actual free index and its two diagrams

Let \(\mathcal D\) be the B.MX10 free dg category on vertices
\(0,1,2,3,4,5\), the six reversed closed edges
\[
\begin{gathered}
e_{01}:1\to0,\ e_{12}:2\to1,\ e_{23}:3\to2,\\
e_{04}:4\to0,\ e_{45}:5\to4,\ e_{53}:3\to5,
\end{gathered}
\]
and the degree-minus-one generator \(c:3\to0\) with
\[
dc=e_{01}e_{12}e_{23}-e_{04}e_{45}e_{53}.
\]
Use the exact whole bimodules \(W_i\), maps \(a_i:W_i\to M_\square\),
edges \(\lambda_{ij}\), witnesses \(\omega_{ij}\), and full mixed
pair \((H,K)\) of B.MX5–8. They define two strict dg diagrams:
\[
\begin{array}{c|ccc}
&i&e_{ij}&c\\ \hline
\mathcal W&W_i&\lambda_{ij}&H\\
\mathcal M&M_\square&1&0 .
\end{array} \tag{B.MP1}
\]
The first is a dg diagram because \(dH=T-B\); the second because the
two edge words both map to the identity. Their parameter category is
literally the stated free category, not a quotient asserting \(T=B\).

The comparison has object values \(\alpha_i=a_i\), arrow homotopies
\(k_{e_{ij}}=\omega_{ij}\), and the indispensable higher value
\[
k_c=K. \tag{B.MP2}
\]
For homogeneous paths extend by
\[
k_{gf}=k_g\mathcal W(f)+(-1)^{|g|}\mathcal M(g)k_f,\qquad k_1=0.
\]
These are exactly the third coordinates of the resolution-graph
composition B.MX9. On an edge, the B.KC9 differential equation is B.MX5.
On \(c\), it is the **second** equation of B.MX8:
\[
\begin{aligned}
&dk_c+k_{dc}\\
&=dK+\Omega_T-\Omega_B\\
&=a_0H\\
&=\alpha_0\mathcal W(c)\\
&\quad-\mathcal M(c)\alpha_3.
\end{aligned}\tag{B.MP3}
\]
The path differential and product rule extend this to all homogeneous
words. Dropping \(K\) would lose B.MP3 even though the first equation
\(dH=T-B\) remained true.

#### The signed bar map is a strict map of the whole diagrams

For each vertex \(i\), apply B.KC10 with the right representable
\(\mathcal D(-,i)\). The source is
\[
\mathcal P\mathcal W(i)
 =B(\mathcal D(-,i),\mathcal D,\mathcal W).
\]
It has the ordinary augmentation to \(\mathcal W(i)\).
After co-Yoneda on the target, the comparison is the literal map
\[
\begin{gathered}
\Psi_i(m\otimes x)\\
=\mathcal M(m)\alpha_a x,\\
\Psi_i(m\otimes t\otimes x)\\
=(-1)^{|m|+1}\mathcal M(m)k_t x,\\
\Psi_i\big|_{[n]}=0\quad(n\geq2).
\end{gathered}\tag{B.MP4}
\]
Its chain identity is B.KC9–10 with the input B.MP2–3, including the
original total-degree convention (internal degree minus bar length).
For a homogeneous parameter arrow \(u:i\to j\), the representable map
postcomposes \(m\) by \(u\), with the B.RK7 factor
\((-1)^{n|u|}\) on bar length \(n\). At length one the coefficient in
\(\Psi_j\mathcal P\mathcal W(u)\) is
\((-1)^{|u|+|u|+|m|+1}=(-1)^{|m|+1}\), exactly the coefficient in
\(\mathcal M(u)\Psi_i\). Thus this is graded naturality, including
nonzero-degree parameter arrows, not just naturality of closed edges.
The original endpoint variables use the same Koszul interchange, because
all \(a,\lambda,\omega,H,K\) are whole bimodule maps.
It is an objectwise quasi-isomorphism by B.KC10: the
right representable is h-projective and each \(\alpha_i\) is the actual
B.MX4 quasi-isomorphism. No unresolved proper image is assumed exact.

In particular, at the distinguished length-one tensor with \(m=1_0\),
\[
\Psi_0(1_0\otimes c\otimes x)=-Kx. \tag{B.MP5}
\]
The degree of \(c\) is minus one and this tensor has one bar position,
so both sides have degree \(|x|-2\). The higher witness has become an
actual component of the strict map; it was not discarded.
The vanishing at *external* bar length at least two does not erase a
nonzero image of an internal UQ word. On a larger supplied index use
the strict UQ word images with the original \(K_2\), as B.MX12 requires.

#### Select the inverse on this index, not vertex by vertex

Take a whole h-projective replacement
\(\rho:R\to\mathcal P\mathcal W\) over \(\mathcal D\) times the
endpoint product category, and a whole replacement
\(q:Q\to\mathcal M\). B.ND5 provides these without assuming that
restriction preserves whole projectivity.
Apply B.ND7 to the actual closed map \(\Psi\rho\). Obtain
\[
\begin{gathered}
\beta:R\to Q,\\
b:R\to\mathcal M[-1],\\
q\beta-\Psi\rho=db.
\end{gathered}\tag{B.MP6}
\]
Here \(\beta,b\) are whole-index maps. The two maps to \(\mathcal M\)
are quasi-isomorphisms, so \(\beta\) is a quasi-isomorphism between
whole h-projectives. Select its whole inverse \(\theta:Q\to R\)
and both whole inverse witnesses \(\ell,r\).
The exact formulas B.IW2–5 then provide the additional
\(\ell^c,\tau,\sigma\), also whole-index maps.

Thus this particular six-vertex geometry has an explicit strict roof
\[
\begin{gathered}
\mathcal W\ \longleftarrow\ \mathcal P\mathcal W\\
\ \longleftarrow R\ \xrightarrow{\beta} Q\\
\ \xrightarrow{q}\mathcal M,
\end{gathered}\tag{B.MP7}
\]
with the recorded \(\Psi\rho\), its full witness \(b\), and the
whole inverse package. The arrow to \(\mathcal W\) is the bar
augmentation, not the non-strict family \(\alpha_i\).
All original data remain accessible through B.MP1–5.
The choices are not asserted to be unique or canonical.

#### Scope of the whole-index construction

B.MP1–7 instantiate the whole inverse-selection step on the actual MX
parameter category with its actual higher comparison. The higher bar component is therefore determined by the given mixed cube.
The inverse and witnesses must first be chosen on this whole index.
For a new index, restrict the displayed diagram and then re-resolve
as B.CE11 prescribes.

Application of the RCmp target and mate formulas requires transport of
this roof through the original right-kernel dual/evaluation and factorized
\(S,V\) comparisons of B.OD11–19. Its comparison with the fixed endpoint
routes must retain the closed displacements \(C_T,C_B\); their exactness
is an additional condition. The required datum is a geometric \(J_H\),
or a primitive of the literal B.IW1 obstruction, on the same receiving
seven-object diagram.

B.MP7 alone does not imply extension of the independently prescribed
\(J_T,J_B\), compatibility over all changing arrays, or existence of
the degree-minus-five witness.


### Dualize the mixed model with all graph witnesses

**Proposition B.1bf (signed dual graph and inverse span).** The whole mixed model of [B.1be](#place-the-mixed-cube-on-one-whole-inverse-model) has a signed right-dual graph and a safe comparison span. All statements retain the original coefficient, proper-base-change, whole-resolution and resolved-input hypotheses. The raw dual of the unresolved mapping target is not asserted to be an equivalence.

**Earlier constructions:** [B.RK](#join-the-geometric-kernels-in-right-module-variance); [B.IW](#keep-the-inverse-witnesses-and-their-higher-obstruction).

#### 1. The full graded dual, including graph witnesses

For a left kernel \(A\), use the literal B.RK1 full Hom dual
\(DA(J,I)=\operatorname{Hom}(A(-,I),\mathcal E(J,-))\).
For homogeneous \(f:A\to B\) of degree \(p\), its action is
\[
\begin{gathered}
(Df)(\phi)=(-1)^{p|\phi|}\phi f,\\
d(Df)=D(df),\\
D(gf)\\
=(-1)^{|g||f|}(Df)(Dg).
\end{gathered}\tag{B.RD1}
\]
These formulas follow by the Hom differential and graded precomposition.
They are the dg-opposite convention, not unsigned reversal.

Write an ordinary graph object as \(a:P\to Q\), and a degree-\(n\)
arrow as \((c,v,h)\), with differential
\[
D_{\rm ar}(c,v,h)=(dc,dv,a'c-va-dh).
\]
The dual graph object is \(Da:DQ\to DP\). The full dual graph map is
\[
\begin{gathered}
\mathfrak D(c,v,h)\\
=(Dv,Dc,-Dh).
\end{gathered}\tag{B.RD2}
\]
It is a strict dg functor from the opposite graph category:
\[
\begin{gathered}
D_{\rm ar}\mathfrak D(x)\\
=\mathfrak D(D_{\rm ar}x),\\
\mathfrak D(yx)\\
=(-1)^{|x||y|}\mathfrak D(x)\mathfrak D(y).
\end{gathered}\tag{B.RD3}
\]
For the third differential, both sides are
\(Da\,Dv-Dc\,Da'+D(dh)\).
For the product, dualizing
\(h_yc_x+(-1)^{|y|}v_yh_x\) gives precisely the
third coordinate of the right side, including the
\((-1)^{|x|}\) in the reversed graph product.
Thus a third-coordinate witness changes sign; it does not disappear.

#### 2. Apply it to the actual MX cube

For B.MX5–9 use the ordinary graph convention
\((c,v,h)=(\lambda,1,\omega)\). The mixed cell is \((H,0,K)\).
After dualization the recorded data are
\[
\begin{array}{c|c}
\begin{gathered}\text{left graph}\\
\text{datum}\end{gathered}&
\begin{gathered}\text{right graph}\\
\text{datum}\end{gathered}\\ \hline
\begin{gathered}a_i:W_i\\
\to M_\square\end{gathered}&
\begin{gathered}Da_i:DM_\square\\
\to DW_i\end{gathered}\\
\begin{gathered}(\lambda_{ij},1,\\
\omega_{ij})\end{gathered}&
\begin{gathered}(1,D\lambda_{ij},\\
-D\omega_{ij})\end{gathered}\\
\begin{gathered}(H,0,\\
K)\end{gathered}&
\begin{gathered}(0,DH,\\
-DK).\end{gathered}
\end{array}\tag{B.RD4}
\]
The parameter category is \(\mathcal D^{\rm op}\); its mixed generator
runs from \(0\) to \(3\). Both edge words reverse order.
For the top word it is
\(D\lambda_{23}D\lambda_{12}D\lambda_{01}\).
The bottom word has the corresponding reversed order.
Since the edges have degree zero, no extra sign occurs in these words.
The full mixed differential is
\[
\begin{gathered}
D_{\rm ar}(0,DH,-DK)\\
=(0,D(T-B),\\
-D\Omega_T+D\Omega_B).
\end{gathered}\tag{B.RD5}
\]
Indeed \(d(DK)=DH\,Da_0-D\Omega_T+D\Omega_B\).
Its \(DH\,Da_0\) term cancels the target/source term in the graph
differential. This retains both original mixed equations, not only
the equation for \(H\).

The raw maps \(Da_i\) are not thereby quasi-isomorphisms, and
\(DM_\square\) has not been proved whole h-projective.
B.RD4 is an actual dg diagram; it is not an acyclic lifting category.
In particular, do not try to fill B.IW1 by inverting \(Da_i\).

#### 3. The safe dual roof and the inverse coherences

Let \(p=\epsilon\rho:R\to\mathcal W\) be the B.MP7 bar augmentation,
and retain \(\beta:R\to Q\), \(\theta:Q\to R\) and its whole inverse
package. The dual comparison span at every vertex is
\[
\begin{gathered}
DW_i\xrightarrow{Dp_i}DR_i\\
\xleftarrow{D\beta_i}DQ_i.
\end{gathered}\tag{B.RD6}
\]
The first arrow is an objectwise homotopy equivalence: \(p_i\) is a
quasi-isomorphism between h-projective endpoint modules. B.ND6 supplies
h-projectivity of \(R_i\), and B.MX supplies it for \(W_i\).
The Hom dual preserves this actual homotopy equivalence.
The second arrow is a whole homotopy equivalence, since \(\beta\)
has its inverse and both homotopies on the whole parameter diagram.
Neither statement uses the unproved exactness of dualizing a
quasi-isomorphism with an unresolved source.

Use the coherent alternative \(\ell^c,r,\tau,\sigma\) of B.IW2–5.
For the dual map and inverse put
\[
\begin{gathered}
\gamma=D\beta,\quad\eta=D\theta,\\
\ell^\vee=Dr,\quad r^\vee=D\ell^c,\\
\tau^\vee=-D\tau,\quad\sigma^\vee=-D\sigma.
\end{gathered}
\]
Their literal differentials are
\[
\begin{gathered}
d\ell^\vee=\eta\gamma-1,\\
dr^\vee=\gamma\eta-1,\\
d\tau^\vee=\gamma\ell^\vee-r^\vee\gamma,\\
d\sigma^\vee=\eta r^\vee-\ell^\vee\eta.
\end{gathered}\tag{B.RD7}
\]
The two inverse homotopies are exchanged by duality. The degree-minus-two
coherences also acquire a minus sign. The old \(\ell\), its dual, and
the B.IW6 displacement remain separate retained data.

The B.MP6 comparison with the geometric target also has an exact dual:
\[
\begin{gathered}
q\beta-\Psi\rho=db\\
\quad\Longrightarrow\quad\\
(D\beta)(Dq)-D(\Psi\rho)\\
=d(Db).
\end{gathered}\tag{B.RD8}
\]
This equation retains the actual signed bar component \(-K\) inside
\(\Psi\), and its whole witness \(b\). It makes no equivalence claim
about \(Dq:DM_\square\to DQ\).

Duality alone need not preserve whole h-projectivity on the new
opposite index. Before a whole Hom lift, take the B.ND5 right-module
replacements there. Treat B.RD6–8 as the supplied strict base diagram,
including the free inverse/coherence generators and their displayed
differentials, and apply B.CE10 to retain them on the selected
receiving resolutions. The checked \(d^2=0\) identities make this a
specified relative free boundary, not an unspecified lift of relations.
After any subsequent restriction use B.CE11 again.

#### 4. Connect to the existing right-kernel words without discarding data

At vertex \(i\), let \(E_i:K_i\to DW_i\) denote a collapsed representative
of the *recorded* B.KC12–15 zigzag for that geometric word, with every
original leg and inverse-cancellation witness kept. Its new receiving
map is the actual composite
\[
\begin{gathered}
\widetilde E_i=(Dp_i)E_i\\
:K_i\to DR_i.
\end{gathered}\tag{B.RD9}
\]
For the elementary factors these are exactly the original \(H_f,P_g\)
roofs. For words use B.RK3's evaluation with
\((-1)^{|u|(|v|+|x|)}\), and B.RK4's all-length associator compatibility.
Do not replace a word evaluation by an unsigned identification.

There is a useful exact rule for an already supplied old right edge.
Suppose \(B_e:K_i\to K_j\) is closed and its retained roof witness is
\[
E_j B_e-(D\mathcal W)(e)E_i=dA_e.
\]
The strict naturality of \(p\), dualized by B.RD1, then gives
\[
\begin{gathered}
\widetilde E_jB_e-(DR)(e)\widetilde E_i\\
=d\bigl((Dp_j)A_e\bigr).
\end{gathered}\tag{B.RD10}
\]
Thus no additional unspecified homotopy is needed merely for composing
that *given* edge witness with the whole bar roof.
The degree-zero \(Dp_j\) retains the order of its factors.

For a homogeneous higher graph arrow use B.RD2–3 on the full triple and
the actual graph product, not B.RD10 stripped of its differential term.
If only the lower right edges have already been supplied, B.CE10 may
lift the actual strict \(DR(c)\) boundary to the selected whole
right-kernel resolutions; its base is given by B.RD5, not guessed.
A prescribed full higher cell can be compared through the zero-base
difference only when its base and boundary agree with those of the
displayed cell. This agreement is a separate hypothesis.

#### 5. The remaining geometric identification

The dual MX graph, its signs, the whole inverse span and transfer of a
prescribed edge witness do not by themselves identify the geometric
comparison. That identification requires the actual \(E_i,A_e\) for the
factorized \(L S,V L_0\) endpoint routes on the same opposite parameter
index, with their endpoint-comparison displacements. B.RCmp1–11 require
a primitive of B.IW1 evaluated on those choices.

Neither the span nor its acyclic resolution kernels imply exactness of
the fixed closed endpoint displacement, as the IW counterexample shows.
A coherent replacement route and an independently prescribed alternative
route can be identified only through their full comparison.

The actual geometric \(J_H\), the degree-minus-five triangle comparison,
all-array coherence, nearby-cycle descent and coefficient completion
remain additional proof obligations.


### Construct the inertia quotient and its exact invariants

Here is the group input for every strictly henselian trait used above. Fix a uniformizer \(u\) and a compatible system of its roots. For an integer \(n\) prime to \(p\), the field \(K\) contains \(\mu_n\): the distinct residue roots lift by Hensel's lemma. The extension \(K(u^{1/n})/K\) is cyclic of degree \(n\). Its powers \(1,u^{1/n},\ldots,u^{(n-1)/n}\) are linearly independent because their valuations occupy distinct classes modulo \(\mathbf Z\); the defining polynomial gives the opposite degree inequality. Its value group is \(n^{-1}\mathbf Z\), and its residue field is unchanged. For the latter assertion, the terms in a basis expansion have distinct fractional valuations, so the least term determines the residue after division by an element of the same valuation.

Let \(K^t\) be the union of these extensions. Its value group is \(\mathbf Z[1/n:(n,p)=1]\), its residue field is separably closed, and
\(\operatorname{Gal}(K^t/K)=\varprojlim_{(n,p)=1}\mu_n=\prod_{r\ne p}\mathbf Z_r(1)\).
The field is henselian by [Lemma A.1a and Theorem A.1b](#separate-henselian-algebra-from-valuation-extension), which identify the extending valuation ring with the local henselian integral closure without assuming a finite normalization.

We verify that \(P=\operatorname{Gal}(K^{\mathrm{sep}}/K^t)\) is pro-\(p\), including when finite extensions have defect. For a prime \(r\ne p\), the value group of \(K^t\) is \(r\)-divisible. A finite-index enlargement \(\Gamma'\) of an \(r\)-divisible subgroup \(\Gamma\) in a torsion-free group is still \(r\)-divisible. In fact, \(r\gamma'\in\Gamma\) implies \(\gamma'\in\Gamma\), by dividing in \(\Gamma\) and using torsion-freeness. Hence the finite group \(\Gamma'/\Gamma\) has no \(r\)-torsion. Multiplication by \(r\) on that quotient is bijective; lift a division there and correct its error by division in \(\Gamma\).

Every finite extension of \(K^t\) has such a finite value-group index, by the distinct-value linear-independence argument in Appendix A, and has separably closed residue field. If a finite Galois extension had an automorphism of prime order \(r\ne p\), its fixed field would thus have \(r\)-divisible value group and separably closed residue field. Every nonzero element of that field is an \(r\)-th power: match its valuation, extract a root of the remaining residue unit, and lift by Hensel's lemma. It also contains \(\mu_r\). Diagonalizing the automorphism would produce a nontrivial eigenvector \(v\) with \(v^r\) in the fixed field. A root \(b\) of \(v^r\) there would imply \(v/b\in\mu_r\), contradicting the nontrivial eigenvalue. The finite-group argument proved in Appendix A now excludes every prime divisor other than \(p\) from each finite Galois quotient. When \(p=1\), it excludes every prime.

Over the strict trait full inertia is \(I=\operatorname{Gal}(K^{\mathrm{sep}}/K)\). Project the tame quotient to its \(\ell\)-factor and put

\[
H=\ker\bigl(I\longrightarrow\mathbf Z_\ell(1)\bigr).
\tag{B.3}
\]

Every finite quotient of \(H\) has order prime to \(\ell\): its normal wild image is a \(p\)-group and its remaining quotient comes from the other tame factors. Invariants on discrete \(\ell\)-primary modules are exact. To lift an invariant element through a surjection, lift it first arbitrarily, choose a finite quotient through which the orbit of this lift factors, and average over that quotient. Its order is invertible in the coefficients. Refining the quotient repeats every summand equally, so the average is independent of that choice and commutes with maps and restrictions.

These compatible averaging idempotents split the underlying sheaf and its complement. Stalks and costalks preserve the splitting, so both perverse support cuts are preserved as well. The normalized coefficient comparison carries this construction to adic complexes. Thus the resulting invariant functor is perverse t-exact and commutes with perverse cohomology; that normalized comparison is part of the stated formalism prerequisites.

The remaining quotient \(\Gamma=\mathbf Z_\ell(1)\) has cohomology only in degrees zero and one on discrete \(\ell\)-primary modules. We verify the continuous comparison directly. Choose a generator \(T\), put \(\Gamma_n=\ell^n\Gamma\), and first let \(M\) be killed by \(\ell^a\). A continuous cochain on \(\Gamma\) has finite image by compactness. For sufficiently large \(n\), it factors through \(\Gamma/\Gamma_n\) and its values lie in \(M^{\Gamma_n}\). Thus the continuous cochain complex is the filtered union of the finite cyclic group cochain complexes with these coefficient submodules; filtered unions commute with kernels and images.

For a cyclic group of order \(\ell^n\), the augmented free group-ring resolution alternates multiplication by \(T-1\) and by \(N_n=1+T+\cdots+T^{\ell^n-1}\). Its exactness is a coefficient calculation: the kernel of \(T-1\) consists of constant coefficient vectors, the image of \(N_n\); the kernel of \(N_n\) consists of coefficient vectors of sum zero, the image of \(T-1\). For the quotient from order \(\ell^{n+1}\) to order \(\ell^n\), inflation is represented in resolution degree \(q\) by projection multiplied by \(\ell^{\lfloor q/2\rfloor}\). This is a chain map because projection sends \(N_{n+1}\) to \(\ell N_n\) and preserves \(T-1\). Consequently every class in degree \(q\geq2\) dies after at most \(a\) successive inflations. In degree one, any \(v\in M\) eventually belongs to \(\ker N_n\): if its orbit has period dividing \(\ell^r\), then \(N_nv=\ell^{n-r}N_rv=0\) for \(n\geq r+a\). We obtain

\[
H^0(\Gamma,M)=\ker(T-1),\qquad
H^1(\Gamma,M)=M/(T-1)M,\qquad
H^q(\Gamma,M)=0\quad(q\geq2).
\]

The natural two-term comparison sends its degree-zero element to the corresponding zero-cochain and its degree-one element \(v\) to the continuous crossed homomorphism with value \(v\) at \(T\), constructed in Appendix C. The coboundary of a zero-cochain has value \((T-1)v\), so this is a chain map; the calculation above proves it a quasi-isomorphism. Taking the union of the submodules killed by \(\ell^a\) proves the claim for every discrete \(\ell\)-primary module. Together with exact \(H\)-invariants this proves \(\operatorname{cd}_\ell K\leq1\), including for the fields \(K_d\) above. The application to equivariant sheaves and normalized adic coefficients still requires their stated descent and coefficient comparisons.

### The étale proof keeps full inertia

Let \(M\) be perverse for the shifted generic convention, and set \(C=R\psi M\) and \(B=i^*Rj_*M\). On pointed neighborhoods the geometric generic Galois cover, its augmentation and continuous descent give

\[
B=R\Gamma(I,C)=R\Gamma(\mathbf Z_\ell(1),C^H).
\tag{B.4}
\]

This identity is compatible with the augmentation \(B\to C\). Exact invariants, the length-one resolution and boundedness allow passage through the pointed filtered limit. After choosing \(T\) and forgetting residue-field descent, it becomes

\[
B\simeq\operatorname{Fib}(T-1:C^H\longrightarrow C^H).
\tag{B.5}
\]

The two copies have the same underlying sheaf. Their intrinsic arithmetic descent structures differ by the Iwasawa functor constructed in Appendix C. A uniform identification with an ordinary Tate twist is not used here.

The localization triangle
\(j_!M\to Rj_*M\to i_*B\)
and Lemma B.1 put \(B\) in perverse degrees \([-1,0]\). The long exact sequence of (B.5) makes \(T-1\) surjective on \({}^pH^q(C^H)\) for \(q\geq0\), and injective for \(q\leq-2\). To exploit these statements we must justify both the eigenvalue decomposition and the permitted twists.

For a constructible perverse object \(A\), its algebra \(\operatorname{End}(A)\) is finite dimensional over \(E\). The exact finiteness input \(H^0(X_s,R\mathcal Hom(A,A))\) is proved for entire derived objects by [Lemma B.0](#finite-derived-endomorphisms-and-continuous-inertia), from the complete integral Hom complex and its rationalization. Its finite-stage argument also supplies continuity of the actual nearby action, subject to the separately recorded nearby constructibility hypothesis. The argument uses those operation theorems with their stated geometric and coefficient hypotheses. The automorphism \(T\) therefore satisfies a polynomial. After a finite coefficient extension, factor its minimal polynomial as \(\prod_\lambda(x-\lambda)^{m_\lambda}\). Bézout identities for these relatively prime factors give orthogonal polynomial idempotents adding to one. Their images split \(A\) in the abelian perverse heart, and \(T-\lambda\) is nilpotent on the corresponding image. There are finitely many nonzero perverse cohomology objects, so one finite coefficient extension suffices for all of them. This argument does not require an injective resolution inside constructible sheaves or a Jordan decomposition of the entire derived object.

Each eigenvalue gives a continuous character of \(\mathbf Z_\ell(1)\). Here are the topological details. Left multiplication embeds the unit group of \(\operatorname{End}(A)\) faithfully in the linear automorphisms of that finite-dimensional algebra. The given continuous action has \(T^{\ell^n}\to1\), so its eigenvalues satisfy \(\lambda^{\ell^n}\to1\) in a finite coefficient extension. Compactness of all integer powers makes \(\lambda\) a unit. If an integer difference is divisible by \(\ell^n\), the corresponding powers of \(\lambda\) differ by at most \(|\lambda^{\ell^n}-1|\): use the geometric sum for positive powers and the unit inverse for negative powers. Thus \(a\mapsto\lambda^a\) on \(\mathbf Z\) is uniformly continuous for the \(\ell\)-adic topology. Completeness extends it uniquely to a continuous homomorphism on \(\mathbf Z_\ell\). Sending \(T\) to \(\lambda^{-1}\) gives the required inverse character.

Pull this rank-one local system back from the generic point of the strict trait and tensor it with \(M\). At finite coefficient levels a finite free local system is étale locally constant, and the stalk and costalk tensor comparisons follow there. The normalized coefficient comparisons give those maps for \(E\); tensoring either test with a finite-dimensional fibre preserves its vanishing, so tensoring is t-exact. After passage to the geometric generic point, the parameter system is constant; the construction of nearby cycles gives the coefficient tensor identity with its descent action. On \(H\)-invariants the twist replaces \(T\) by \(\lambda^{-1}T\). The preceding surjectivity or injectivity therefore applies to a nilpotent operator on each forbidden-degree eigencomponent. A nilpotent monomorphism or epimorphism forces its object to be zero, by iterating to the zero power. Faithful scalar extension detects that zero before the coefficient extension. We obtain

\[
C^H[-1]\in\operatorname{Perv}(X_s).
\tag{B.6}
\]

The parameter characters exist on the strict generic point itself. No extension to a chosen arithmetic Frobenius, or geometric-origin condition on the original complex, was needed for this step.

### Recover the full inertia object from a finite regular representation

We now detect what \(H\)-invariants alone might lose. For each nonzero \(A_q={}^pH^qC\), use the faithful linear action on \(\operatorname{End}(A_q)\) just described. A continuous compact group action on a finite-dimensional \(E\)-space preserves a lattice. Indeed, the matrices of its compact image have uniformly bounded entries. The sum of the translates of any initial lattice lies in one fixed larger lattice, contains the initial lattice, and is finitely generated over the valuation ring; it is the required invariant lattice.

The kernel of reduction on the automorphisms of that lattice is pro-\(\ell\). Its filtration by matrices congruent to one modulo successive powers of the uniformizer has finite additive residue-field quotients and trivial intersection. The image of \(H\) is pro-prime-to-\(\ell\), and its closed subgroups have the same property: any finite quotient of a closed subgroup is detected inside a finite quotient of the original profinite group. Its intersection with that pro-\(\ell\) kernel is therefore trivial. Consequently the kernel of the finite residue representation of \(I\), when intersected with \(H\), acts trivially on \(A_q\). Combine the finitely many residue representations to obtain a finite quotient \(Q\) of \(I\) with this property for every \(q\).

Let \(\rho=E[Q]\) with its regular left action. It defines a finite parameter local system on the strict generic point. Geometric-generic pullback trivializes it, so the finite direct-sum coefficient comparison gives

\[
R\psi(M\otimes f^*\rho)=C\otimes\rho
\tag{B.7}
\]

with the diagonal descent action. Apply (B.6) to this new perverse input. Thus \((C\otimes\rho)^H\) has only perverse degree \(-1\).

Let \(J\) be the image of \(H\) in \(Q\). The \(H\)-action on each \(A_q\) factors through \(J\). For a single regular copy there is an explicit isomorphism of underlying perverse objects

\[
A_q\longrightarrow (A_q\otimes E[J])^J,
\qquad x\longmapsto\sum_{h\in J}h x\otimes e_h.
\]

The inverse extracts the coefficient of \(e_1\). Invariance says that the coefficient of \(e_h\) must be \(h\) times that coefficient, proving both inverse identities. The displayed notation is a finite matrix of actual morphisms in the additive category, so it detects the whole perverse object, including its attaching maps. Restriction of \(E[Q]\) to \(J\) is the direct sum of these regular copies, one for each left coset. Hence the twisted-invariant functor is faithful on the \(A_q\). Exact invariants and finite coefficient tensoring commute with perverse cohomology. Their vanishing in every degree except \(-1\) forces

\[
R\psi M[-1]\in\operatorname{Perv}(X_s)
\quad\text{with full continuous inertia}.
\tag{B.8}
\]

Thus the conclusion concerns the original nearby object, including its wild and prime-to-\(\ell\) tame actions.

### Use the augmentation to handle vanishing cycles

Write \(E_M=R\psi M[-1]\). The normalized specialization fibre gives \(\Phi(j_!M)=E_M\), since the special restriction of \(j_!M\) is zero. For a closed-supported object it gives \(\Phi(i_*A)=A\). To pass from these cases to every perverse object we need the map between them, not only their isomorphism classes.

Localization gives
\(i^!j_!M=B[-1]=R\Gamma(I,E_M)\).
The two-term resolution and exact \(H\)-invariants put this costalk in perverse degrees \([0,1]\), with degree-zero object \(E_M^I\). A morphism from a perverse \(A\) into it factors uniquely through that degree-zero truncation, by the two orthogonality vanishings in its truncation triangle. Accordingly adjunction identifies a heart morphism \(i_*A\to j_!M\) with \(A\to E_M^I\). Under \(\Phi\) its map is

\[
A\longrightarrow E_M^I\hookrightarrow E_M.
\tag{B.9}
\]

To verify this last identification, apply the enhanced specialization fibre to the localization triangle \(i_*B[-1]\to j_!M\to Rj_*M\). For \(Rj_*M\), specialization is the augmentation \(B=R\Gamma(I,C)\to C\) of (B.4). Taking the corresponding fibres and rotating gives \(B[-1]\to C[-1]\to\operatorname{Cone}(B\to C)[-1]\), whose first map is that same augmentation shifted. In perverse degree zero it is exactly \(E_M^I\hookrightarrow E_M\). Naturality and adjunction give (B.9) for every \(A\). The enhanced attaching homotopy is retained in this calculation; an unenhanced square of zero stalk maps would not determine it.

If \(i_*A\to j_!M\) is monic in the heart, its adjoint \(A\to E_M^I\) is monic too: a kernel would push forward to a subobject killed by the original monomorphism. Hence (B.9) is monic. For any perverse \(K\), set \(M=j^*K\) and factor the heart counit through its image \(J_K\):

\[
0\longrightarrow i_*A\longrightarrow j_!M\longrightarrow J_K\longrightarrow0,
\qquad
0\longrightarrow J_K\longrightarrow K\longrightarrow i_*D\longrightarrow0.
\]

The kernel and cokernel are closed-supported because their generic restrictions vanish. Applying \(\Phi\) to the first triangle gives a monomorphism \(A\to E_M\) of perverse objects, so its cone \(\Phi J_K\) is perverse. The second triangle then makes \(\Phi K\) an extension of \(\Phi J_K\) by \(D\), hence perverse. Finite perverse truncation triangles now prove both cuts for \(\Psi\) and \(\Phi\) on bounded complexes: each complex is a finite extension of its shifted perverse cohomology objects, and the functors preserve the heart and shifts. They are therefore t-exact and exact on the hearts.

For a non-strict henselian trait, pull back to its strict localization for these tests; faithfully forgetting residue-field descent detects the two cuts. With the total-space convention, \(\Psi_fK=R\psi(j^*K)[-1]\); for a usual generic-fibre perverse input \(L\), the assertion reads \(R\psi L\) perverse. Finite coefficient descent and faithful extension give \(\overline{\mathbf Q}_\ell\).

The full assigned arbitrary-trait statements are thus reduced to explicit foundations, including the ordinary affine and constructible-finiteness theorems, strict-local continuity, henselian valuation extension, trait purity and duality, the continuous sheaf-descent comparison, and normalized adic reduction and rationalization. Their exact recursive proofs remain required. This argument does not use a nearby- or vanishing-cycle duality theorem; the separate comparisons are developed in Appendices D and E.

## Appendix C. Full étale variation and the Iwasawa twist

The variation target must carry the arithmetic action, as well as the operator seen after choosing a geometric inertia generator. We construct that target from continuous crossed homomorphisms, prove the change-of-generator and group-algebra statements, and then obtain variation from the actual specialization map. For the Iwasawa twist and its sheaf version, see Lu–Zheng, arXiv version 7. The full sliced-topos duality theorem is a separate result; the construction here does not assume it.

### Construct the target before choosing its coordinates

Keep \(H=\ker(I\to\mathbf Z_\ell(1))\) from Appendix B and put \(\Gamma=I/H\). Exact averaging gives

\[
V=V^H\oplus V^{\mathrm{rest}}.
\tag{C.1}
\]

The second summand has zero \(H\)-invariants. We will leave it unchanged. On \(V^H\) write \(G=G_\eta/H\); then \(\Gamma\) is a normal subgroup of \(G\), and conjugation is \(gTg^{-1}=T^{\chi(g)}\) for a geometric generator \(T\) and the cyclotomic character \(\chi\). No splitting of \(G\to G_s\) is needed.

Begin with a finite coefficient ring \(\Lambda=O/\pi^m\), annihilated by some power \(\ell^a\). For a discrete continuous \(G\)-module \(M\), let \(Z^1(\Gamma,M)\) consist of continuous maps satisfying

\[
c(xy)=c(x)+x\,c(y),
\qquad (g c)(x)=g\,c(g^{-1}xg).
\]

This definition is independent of a generator. Evaluation at \(T\) identifies its underlying coefficient module with \(M\). Here is the existence and continuity argument. Given \(v\in M\), a cocycle must have
\(c(T^n)=\sum_{i=0}^{n-1}T^iv\) for positive integers \(n\), and its values at negative powers follow from \(c(1)=0\). The orbit of \(v\) has a period dividing \(\ell^r\), since a compact pro-\(\ell\) group acts continuously on a discrete set. Hence the displayed sum over \(\ell^{r+a}\) terms is zero, and \(T^{\ell^{r+a}}\) fixes the cyclic submodule generated by \(v\). The formula therefore defines a cocycle on the finite cyclic quotient of that order, then a continuous cocycle on \(\Gamma\). Uniqueness follows because the integer powers of \(T\) are dense and \(M\) is discrete.

Put \(t=T-1\), and for \(b\in\mathbf Z_\ell^\times\) define

\[
u_b(t)=\frac{(1+t)^b-1}{t}
       =b+\binom b2t+\binom b3t^2+\cdots.
\]

These series act on discrete torsion modules. On the cyclic submodule of a section with period \(\ell^r\), the relation \((1+t)^{\ell^r}=1\) implies \(t^{\ell^r}\in\ell\Lambda[t]\), so \(t^{a\ell^r}\) acts by zero. Only finitely many terms matter there. The constant term of \(u_b\) is a unit, so its inverse is obtained recursively, or by a finite geometric series on each such submodule. The integer sum formula and continuity give
\(c(T^b)=u_b(t)c(T)\).

In these coordinates the action on \(Z^1(\Gamma,M)\) is

\[
g\star_-v=u_{\chi(g)}(t)^{-1}g v.
\]

Indeed its original expression is \(g\,u_{\chi(g)^{-1}}(t)v\). Moving the series through \(g\), and using \(((1+t)^{\chi(g)})^{\chi(g)^{-1}}=1+t\), gives the displayed inverse. The opposite action
\(g\star_+v=u_{\chi(g)}(t)g v\)
defines an inverse functor. To check the group law explicitly, put \(t_b=(1+t)^b-1\); then

\[
u_{bc}(t)=u_b(t)u_c(t_b).
\]

For positive integers this follows by factoring \((1+t)^{bc}-1\) twice; continuity gives it for \(b,c\in\mathbf Z_\ell^\times\). Since \(g f(t)=f(t_{\chi(g)})g\), this identity verifies both action laws. Both actions leave the operator \(T\) unchanged, so composing them cancels the two units. They are exact inverse functors on coefficient modules and on equivariant sheaves, where the formulas apply to sections and commute with restriction. In particular their underlying sheaves and perverse degrees are unchanged.

Changing the generator to \(T^b\) replaces the cocycle coordinate by multiplication by \(u_b(t)\). This is an invertible, natural comparison. For the positive functor the comparison in the reverse direction is multiplication by the same unit; the displayed product identity verifies its equivariance and the compatibility of successive changes. Thus the functors are intrinsic, despite these useful coordinates.

### Identify the invertible augmentation ideal

We also prove the group-algebra description, including the point that does not follow just from a one-variable power-series calculation. Let
\(R=\varprojlim_N\Lambda[G/N]\), over open normal subgroups \(N\) of \(G\). Multiplication by \(t\) is injective on either side of \(R\).

For left multiplication, suppose \(tr=0\). At any finite quotient, the coefficients of \(r_N\) are constant along left \(T\)-orbits. Fix \(N\), and choose \(N'\subset N\) such that
\([\Gamma\cap N \mathbin{:} \Gamma\cap N']\) is divisible by \(\ell^a\). Such subgroups exist because the topology induced on the closed subgroup \(\Gamma\) is its profinite topology: an arbitrarily small open subgroup of \(\Gamma\) contains \(\Gamma\cap N'\) for a sufficiently small open normal \(N'\) of \(G\). The fibre over any coset of \(G/N\) is partitioned by the left action of \(\Gamma\cap N\) into orbits of precisely that index; normality of \(N'\) gives the stated stabilizer. Coefficients are constant on each orbit, so their sum is zero in \(\Lambda\). The transition map consequently sends \(r_{N'}\) to zero. Hence \(r_N=0\) for every \(N\), proving \(r=0\). Right orbits prove right injectivity in the same way.

Conjugation gives
\(gt=t\,u_{\chi(g)}(t)g\) and
\(tg=u_{\chi(g)}(t)^{-1}gt\).
Therefore \(J=tR=Rt\). These identities first give the two inclusions on finite linear combinations of group elements, then on their completion: \(R\) is compact, the multiplication maps are continuous, and their images are closed. Replacing \(T\) by \(T^b\) multiplies its generator by the unit \(u_b(t)\), so \(J\) is independent of that choice.

Every \(r\in R\) has a unique \(\beta(r)\) with \(rt=t\beta(r)\). Injectivity just proved shows that \(\beta\) preserves addition, multiplication and the identity. The reverse equality \(tR=Rt\) gives its inverse. For a group element, \(\beta(g)=u_{\chi(g)}(t)g\). Thus the two free rank-one module structures on \(J\) differ by this actual algebra automorphism. Tensoring with \(J\) twists the action by \(\beta\), while \(\operatorname{Hom}_R(J,-)\) twists it by \(\beta^{-1}\); their evaluations are inverse. This proves invertibility as a bimodule, not merely freeness on one side.

On the full inertia object the resulting functors are

\[
\tau V=(J\otimes_R V^H)\oplus V^{\mathrm{rest}},
\qquad
\tau^{-1}V=\operatorname{Hom}_R(J,V^H)\oplus V^{\mathrm{rest}}.
\tag{C.2}
\]

The negative functor on \(V^H\) is the intrinsic crossed-homomorphism construction above: an \(R\)-linear map \(J\to V^H\) is determined by its value at \(t\), and its induced action is \(\star_-\). The same formulas at all coefficient quotients are compatible with reduction. Inverse limits give them on coefficient lattices, and rationalization gives the finite \(E/\mathbf Q_\ell\) version. A change between commensurable lattices gives the same rationalized maps. Passing these coefficient calculations through the normalized constructible adic sheaf category still requires the completeness, reduction and operation comparisons identified in Appendix A; this algebra calculation does not prove that formalism.

### The differential and the variation triangle

There is a natural morphism \(\iota:V\to\tau^{-1}V\). On \(V^H\) it sends \(v\) to the crossed homomorphism \(x\mapsto xv-v\); on \(V^{\mathrm{rest}}\) it is the identity. Its coordinate on the first summand is \(t\), but its target carries the action \(\star_-\), which is needed for arithmetic equivariance.

The continuous group resolution and geometric-generic descent used in Appendix B now give the invariant form of its two-term complex:

\[
R\Gamma(I,V)=\operatorname{Fib}(\iota:V\to\tau^{-1}V).
\tag{C.3}
\]

Here the left side is viewed back in the equivariant category by pullback from the residue-field category. More explicitly, exact \(H\)-invariants reduce to \(\Gamma\), whose augmented completed-group resolution is multiplication by \(t\) on \(\Lambda[[t]]\), followed by evaluation at \(t=0\). Injectivity and the description of its cokernel prove exactness of that resolution. Applying the continuous coefficient Hom gives the two terms and the differential above; the crossed-homomorphism description supplies their descent action. On the complementary summand, derived \(H\)-invariants vanish and the identity differential gives a contractible complex. This is compatible with the augmentation to \(V\), not just with the cohomology groups. The equivariant sheaf and adic interpretation uses the actual continuous-descent comparison of Appendix B and its stated foundations.

Its degree-zero cohomology is \(V^I\). The degree-one cohomology is \(V_I(-1)\): quotienting by \(t\) makes \(u_{\chi(g)}(t)^{-1}\) equal to \(\chi(g)^{-1}\), and the complementary \(H\)-coinvariants vanish by averaging. Thus the Tate factor on degree one follows from the action on the second term.

**Proposition C.1 (full variation triangle).** The normalized full cycles admit a natural triangle

\[
i^!K\longrightarrow\Phi_fK
\xrightarrow{\mathrm{var}}\tau^{-1}\Psi_fK
\longrightarrow i^!K[1],
\tag{C.4}
\]

and \(\mathrm{var}\,\mathrm{can}=\iota\).

**Proof.** Retain the enhanced attaching map
\(a:A=i^*K\to B=i^*Rj_*j^*K\)
and put \(C=R\psi j^*K\). Localization identifies \(\operatorname{Fib}(a)=i^!K\); specialization is \(A\to B\to C\). Equation (C.3) identifies \(B\to C\) with the augmentation and its cofiber with \(\tau^{-1}C\). Pasting the two composable maps gives the triangle of fibres

\[
\operatorname{Fib}(A\to B)\longrightarrow
\operatorname{Fib}(A\to C)\longrightarrow
\operatorname{Fib}(B\to C)\longrightarrow.
\]

The three terms are respectively \(i^!K\), \(\Phi_fK\), and \(\tau^{-1}C[-1]=\tau^{-1}\Psi_fK\). On the common cone model the composite out of \(C[-1]\) is the differential \(\iota[-1]\), giving the claimed identity with the course sign \(T-1\). The maps and their homotopies come from the same augmentation and attaching map, so this is a natural triangle. \(\square\)

For perverse \(K\), once Appendix B's full nearby-cycle bound is available, (C.4) also proves the lower bound for \(\Phi_fK\): its first and third terms are lower-perverse. The specialization triangle gives the upper bound. This consequence retains the operation and constructibility prerequisites of that appendix.

### When a Tate twist suffices, and when it fails

Over a characteristic-zero coefficient field, let \(t\) be nilpotent and put
\(c(t)=\log(1+t)/t=1-t/2+t^2/3-\cdots\), a finite invertible series. Multiplication by \(c(t)\) gives an isomorphism \(V(1)\to\tau V\) on the unipotent tame part. Its equivariance follows from

\[
c(t_b)=\frac{b\,c(t)}{u_b(t)},
\qquad
u_{\chi(g)}(t)g\,c(t)=\chi(g)c(t)g.
\]

The first identity follows by taking the finite formal logarithm of \((1+t)^b\), initially for integers and then by continuity. The second is exactly the intertwining equation for \(\star_+\) and the Tate action. On a part where \(t\) is invertible, the map induced by \(J\hookrightarrow R\) instead identifies \(\tau V\) with \(V\): in coordinates it is multiplication by \(t\). On \(V^{\mathrm{rest}}\) the functor was already the identity.

There is a concrete torsion obstruction to replacing \(\tau\) uniformly by \((1)\). Take coefficients \(\mathbf F_2\), a two-dimensional space with \(N\ne0\), \(N^2=0\), and tame generator \(T=1+N\). Let an arithmetic element \(g\) have \(\chi(g)=3\) and act as the identity on that space. This satisfies the required relation because \(T^3=T\); it gives a continuous representation of the corresponding tame semidirect group. The usual Tate action of \(g\) is still the identity modulo two. But

\[
u_3(N)=3+3N+N^2=1+N,
\]

so its action on \(\tau V\) is nontrivial. No intertwining isomorphism can conjugate an identity operator to that operator. Thus these two twists are not isomorphic in this example. The field logarithm comparison and the full torsion Iwasawa construction must remain distinct; neither establishes the additional torsion sliced-duality theorem.

## Appendix D. Generic nearby-cycle duality

Nearby duality must compare the actual evaluation pairings, not just the dimensions of the resulting groups. We first define its comparison using the exceptional-pushforward counit. We then test that map on coordinate generic fibres and on proper global cohomology. The permitted primary source is Illusie's Theorem 4.2, construction 4.3 and Variant 4.4, in the freely readable Numdam edition; the auxiliary field and finite-support arguments are supplied in Appendix A. Lu–Zheng's free text distinguishes this generic-fibre theorem from the larger sliced duality theorem used for general torsion coefficients.

**Proposition D.1.** Let \(X/S\) be separated of finite type over a henselian discrete valuation trait, with \(\ell\) invertible on \(S\), and let \(L\in D_c^b(X_\eta,E)\), for a finite extension \(E/\mathbf Q_\ell\). With the ordinary duality, base-change and normalized coefficient foundations specified below, there is a natural isomorphism

\[
\beta_{X,L}:R\psi(D_{X_\eta}L)\xrightarrow{\sim}
D_{X_s}(R\psi L).
\tag{D.1}
\]

Both dualizing complexes are relative to their respective fields. The special object retains its full inertia action and residue-field descent. The comparison and its dimension argument below use the specified ordinary and adic operations.

### Define the comparison by evaluation and counit

Write \(a_\eta:X_\eta\to\eta\) and \(a_s:X_s\to s\), and set \(\omega_\eta=a_\eta^!E\), \(\omega_s=a_s^!E\). For a separated finite-type map \(h:X\to Y\) over the trait, the ordinary operations give a natural transformation

\[
\alpha_h:Rh_{s!}R\psi_X\longrightarrow R\psi_YRh_{\eta!}.
\]

Here is the construction needed in this proof. For an open immersion \(u\), smooth base change identifies \(u_s^*R\psi_Yu_{\eta!}\) with \(R\psi_X\). Take the adjoint of that identity under \(u_{s!}\dashv u_s^*\). For a proper map \(p\), take the proper base-change isomorphism. For a factorization \(h=p u\), compose \(Rp_{s*}\alpha_u\) with that proper comparison. On a common compactification, the proper comparisons compose and the open comparisons have the same adjoint identity. The triangle identities for the two adjunctions therefore identify the composites. This also proves compatibility with a further proper map. The compactification and ordinary operation-coherence statements required here are part of the earlier six-operation foundations; affine charts in the induction admit projective closures directly.

Apply \(\alpha_h\) to \(h_\eta^!N\), follow it by the exceptional-pushforward counit, and take the adjoint under \(Rh_{s!}\dashv h_s^!\). This gives

\[
R\psi_Xh_\eta^!N\longrightarrow h_s^!R\psi_YN.
\]

For the structure map and \(N=E_\eta\), use \(R\psi_SE_\eta=E_s\). The latter identity is the cohomology of the separably closed geometric generic point of the strict trait. We obtain a specified map \(\theta_X:R\psi\omega_\eta\to\omega_s\).

The tensor comparison for nearby cycles is the adjoint of tensoring the pullback counits on the geometric generic fibre. It is the usual cup product on the same cochain construction. Compose it with evaluation and \(\theta_X\):

\[
R\psi L\otimes R\psi(D_{X_\eta}L)
\longrightarrow R\psi(L\otimes D_{X_\eta}L)
\longrightarrow R\psi\omega_\eta
\xrightarrow{\theta_X}\omega_s.
\]

Adjunction for internal Hom defines \(\beta_{X,L}\). Thus its normalization is fixed by the ordinary trace; we have not chosen an unspecified scalar multiple of a pairing.

We will use two compatibilities of this construction. Under proper pushforward, the resulting pairing is the pairing of the pushed-forward complex followed by its trace. Before taking adjoints, the verification is the counit identity
\(\epsilon_{gh}=\epsilon_g\circ Rg_!(\epsilon_h)\)
and the composition identity for \(\alpha\); the tensor counits used in evaluation obey the same identity. Under open restriction, both comparisons have the identity as their adjoint, so restriction preserves \(\beta\). Smooth purity similarly preserves the evaluation after inserting its relative dualizing line. Finite-presentation continuity gives the corresponding identifications through the pointed étale limits used next. These checks use the actual base-change and duality maps, not merely isomorphism classes of complexes.

### Compare the two dualizing lines on a coordinate fibre

Pass to a strict localization of the base, and let \(k\) be its separably closed residue field. Faithful restriction will later detect an isomorphism with descent. On an affine chart choose a coordinate map \(f:X\to\mathbb A^1_S\). Let \(S_t\) be the auxiliary strict trait of Appendix A and put \(Y=X\times_{\mathbb A^1_S}S_t\). Denote the generic and special restriction maps by \(q_\eta\) and \(q_s\), and set \(L'=q_\eta^*L\).

The factor in the duality comparison comes from the affine line, not from a choice of inertia generator. Factor the structure map of \(X_\eta\) through \(\mathbb A^1_K\). The composition of exceptional inverse images and smooth purity give
\(\omega_{X_\eta/K}=f_\eta^!E_{\mathbb A^1_K}(1)[2]\).
Restricting to the coordinate generic field and using ordinary exceptional base change therefore gives

\[
q_\eta^*D_{X_\eta}L
\simeq D_{Y_{\eta_t}}L'(1)[2].
\]

The same factorization over \(k\), with \(\mathbb A^1_k\) in place of \(\mathbb A^1_K\), gives for a constructible complex \(M\) on \(X_s\)

\[
q_s^*D_{X_s}M
\simeq D_{Y_{s_t}}(q_s^*M)(1)[2].
\]

These are identifications from the same smooth-line trace orientation. At each finite pointed neighborhood they follow from the ordinary purity and exceptional-base-change maps; constructible continuity passes them to the generic-field limit. Consequently the factor \((1)[2]\) occurs on both sides of the desired comparison.

Appendix A proved that \(K'=\bar K\otimes_KK_t\) is a field and that \(P=\operatorname{Gal}(\overline{K_t}/K')\) is pro-\(p\). Its comparison (A.1) identifies \(q_s^*R\psi_SL\) with \((R\psi_{S_t}L')^P\). Averaging commutes with duality by an explicit pairing calculation. For a finite quotient acting on coefficients, let \(e=|P_0|^{-1}\sum_{g\in P_0}g\). Contragredient evaluation satisfies \(\langle gv,w\rangle=\langle v,g^{-1}w\rangle\); replacing \(g\) by \(g^{-1}\) in the sum gives \(\langle ev,w\rangle=\langle v,ew\rangle\). Thus \(e\) is self-adjoint, its two images are orthogonal complements, and
\(D(N^P)\simeq(DN)^P\).
The compatible projectors at finite coefficient levels give the adic statement under the recorded normalization comparison. The auxiliary \(P\) acts trivially on the prime-to-\(p\) Tate line, whose roots of unity already lie in the strictly henselian base field.

Combining these identities, the source and target of \(q_s^*\beta_{X,L}\) identify respectively with

\[
\bigl(R\psi_{S_t}D_{Y_{\eta_t}}L'\bigr)^P(1)[2],
\qquad
\bigl(D_{Y_{s_t}}R\psi_{S_t}L'\bigr)^P(1)[2].
\]

Under these identifications its map is \((\beta_{Y,L'})^P(1)[2]\). To check the map, restrict the defining evaluation-and-counit composite: both exceptional base-change identifications insert the same line trace, and the self-adjoint projector restricts that evaluation to the invariant summands. Its tensor and counit composites are exactly those defining \(\beta_{Y,L'}\). In particular this comparison uses the canonical augmentation and trace maps rather than an arbitrary isomorphism between the displayed objects.

### Eliminate the comparison cone by dimension and proper cohomology

Induct on \(n=\dim X_\eta\), beginning with \(X_\eta=\varnothing\). In that initial case both sides of (D.1) are zero. Nearby constructibility from Appendix A and ordinary Verdier constructibility make the cone \(C\) of \(\beta_{X,L}\) bounded constructible. Take this cone in the same enhanced sheaf category as its defining maps.

The coordinate-family dimension calculation of Appendix A applies to each affine chart. A component with nonconstant coordinate loses one transcendence degree; a component with algebraic coordinate disappears over the coordinate fraction field. Hence \(\dim Y_{\eta_t}<n\) whenever that generic fibre is nonempty. The induction hypothesis and the preceding map comparison show \(q_s^*C=0\) for every coordinate. When \(n=0\), all these coordinate generic fibres are empty, so the same initial case applies. No assertion that the original special fibre is zero dimensional is needed.

If a cohomology sheaf of \(C\) had a positive-dimensional support stratum in an affine chart, some coordinate would be nonconstant on its irreducible closure. Its nonzero generic germ would survive on the corresponding coordinate generic fibre, contradicting \(q_s^*C=0\). A finite constructible stratification therefore leaves only finitely many closed points in the support. Boundedness gives one finite set for all the cohomology sheaves of \(C\).

We may now prove that \(C\) vanishes on an arbitrary affine chart by embedding that chart into a projective \(S\)-scheme and extending its generic complex by zero. Its restriction back to the chart is the original comparison, by the open compatibility above. The generic dimension has not increased. Run the same coordinate test on affine charts of this projective closure; its comparison cone again has finite closed-point support. Thus it suffices to consider projective \(X/S\).

Proper base change and ordinary proper duality identify the global comparison with

\[
R\Gamma(X_{\bar\eta},D_{X_{\bar\eta}}L_{\bar\eta})
\longrightarrow D_E R\Gamma(X_{\bar\eta},L_{\bar\eta}),
\qquad D_E=R\operatorname{Hom}_E(-,E).
\]

This is the ordinary proper-duality isomorphism: the compatibility already checked identifies its pairing with evaluation followed by the proper trace. On the target we also used ordinary proper duality on \(X_s\) and proper base change for \(R\psi L\). It follows that \(R\Gamma(X_s,C)=0\).

Finally, a constructible cohomology sheaf supported on finitely many closed points over a separably closed field is the finite sum of its skyscrapers. Those points have purely inseparable residue extensions and no positive étale cohomology, as in Appendix A. The bounded cohomology spectral sequence therefore identifies
\(H^qR\Gamma(X_s,C)=\bigoplus_x H^q(C_x)\).
The left side is zero, so every geometric stalk of \(C\) is zero and \(C=0\). This proves the induction and the local comparisons, which glue by their common evaluation-and-counit construction. Faithful restriction from the original trait to its strict localization detects the isomorphism, while the natural maps retain full inertia and residue-field descent. \(\square\)

The outstanding inputs are exact ordinary compactification and six-operation coherence, proper and smooth base change, exceptional base change and purity with the stated trace orientation, constructible duality and proper finiteness, the continuous geometric-generic comparison, and normalized adic reduction and rationalization. These are hypotheses of the stated deduction. The \(P\)-invariants in the induction concern only the auxiliary coordinate field; they do not replace the final full-inertia object by tame cycles.

## Appendix E. Duality of the full specialization cone

The algebra of dual cones depends on a differential, an augmentation and the homotopy in the attaching map. We write these data before comparing them with geometric duality. The boundary comparison below proves agreement of the localization and continuous-inertia pairings from the specified ordinary operations, including the Kummer divisor sign. An isomorphism between the underlying objects alone would not prove that agreement.

Use a finite extension \(E/\mathbf Q_\ell\). For the structure map \(a_X:X\to S\), put \(\omega_X^\delta=a_X^!E(1)[2]\), and write \(D_X^\delta\) for its duality. Write \(D_Z\) for duality on \(Z=X_s\), with its field-relative dualizing complex \(\omega_Z\). The ordinary purity and restriction comparisons required here are

\[
i^*D_X^\delta K\simeq D_Zi^!K,
\qquad
j^*D_X^\delta K\simeq D_{X_\eta}(j^*K)(1)[2].
\tag{E.1}
\]

[Proposition B.1d](#family-duality-from-the-boundary-trace) proves these evaluation-defined exchanges and family biduality from the specified ambient operations, B.1b, B.1c and the generic nearby/boundary-trace comparisons. The ambient construction and its ordinary and normalized adic providers remain exact prerequisites, not an assumed family-biduality theorem. For a trait coming from a smooth curve, this is the absolute total-space normalization. The ordinary torsion stage is supplied by [Proposition B.1e](#ordinary-proper-support-and-its-adjoint-over-a-noetherian-base); its enhanced, completed and rational comparisons remain distinct obligations.

**Proposition E.1 (full-inertia comparison under the stated foundational inputs).** At the arbitrary henselian-trait scope of Appendix D, the required comparison is

\[
D_Z\Phi_fK\simeq\tau\Phi_f(D_X^\delta K)(-1).
\tag{E.2}
\]

The deduction below proves this from Appendix D, (E.1), functorial localization and tensor adjunctions, multiplicative continuous descent, and divisor-oriented purity. It includes the boundary-pairing comparison and compatibility with specialization and variation. Complete proofs of the ordinary and normalized adic foundations are still required, so the proposition remains conditional on those inputs. Its assigned scope has not been reduced to a point or to tame inertia.

### Separate the forced summand by its actual map

Set \(A=i^*K\), \(C=R\psi j^*K\), and \(B=R\Gamma(I,C)\). Descent identifies the attaching map with \(a:A\to B\), and localization identifies \(i^!K=\operatorname{Fib}(a)\). All fibres and cones below retain the homotopies in this map.

The averaging projector of Appendix B and the bounded Fitting construction of Section 5 split
\(C=C_u\oplus C_r\). Here \(C_u\) is the generalized eigenvalue-one part of the \(H\)-invariants; \(C_r\) includes both the other tame eigenvalues and the entire complement of the \(H\)-invariants. This is a functorial split. Changing the tame generator to a unit power preserves its eigenvalue-one part, as does arithmetic conjugation, so it preserves residue-field descent.

The intrinsic map of Appendix C restricts to an isomorphism
\(\iota_r:C_r\to\tau^{-1}C_r\). On the nonunipotent \(H\)-invariant part its coordinate map is the invertible operator \(T-1\); on the complement of the \(H\)-invariants it is the identity. Thus its fibre is zero and \(R\Gamma(I,C_r)=0\). The inverse of \(\iota_r\) contracts the two-term complex, giving the nullhomotopy of the other specialization component. Consequently

\[
\Phi_fK\simeq\Phi_uK\oplus C_r[-1],
\qquad
\Phi_uK=\operatorname{Fib}(A\longrightarrow C_u).
\tag{E.3}
\]

The simplification of the positive twist on this summand is the specific natural isomorphism
\(\tau(\iota_r):\tau C_r\to C_r\). On the nonunipotent tame part this is multiplication by \(T-1\), not a literal identity of its two arithmetic actions. This distinction also applies to the corresponding summand of the dual.

### Compute the dual group complex with both signs

On \(C_u\), the finite series \(c(t)=\log(1+t)/t\), where \(t=T-1\), is invertible. The change of the second generator by \(c(t)\) converts the resolution of Appendix C to
\(G(C_u)=[C_u\xrightarrow{\nu}C_u(-1)]\), in group degrees zero and one, where \(\nu=\log T\) includes the Tate line. The augmentation is still projection from group degree zero. The denominators in this step require the field \(E\).

Put \(V=D_ZC_u\) and \(m=D_Z\nu:V(1)\to V\). The contragredient action is \((T^{-1})^{\mathsf t}\), so its logarithm satisfies
\(\nu_V(1)=-m\). Indeed, the finite logarithm commutes with transpose, and \(\log(T^{-1})=-\log T\); both follow by substituting the nilpotent operator into the formal power-series identities. The dual group complex and the shifted group complex therefore have the same two-term description:

\[
\begin{array}{c|cc|c}
&\text{degree }-1&\text{degree }0&\text{differential}\\
D_ZG(C_u)&V(1)&V&m\\
G(V)(1)[1]&V(1)&V&-\nu_V(1)=m.
\end{array}
\]

The minus sign from shifting a cochain complex cancels the minus sign in the contragredient logarithm. Omitting either one changes the comparison. With the usual totalization for an internal complex, this gives

\[
D_ZR\Gamma(I,C_u)\simeq R\Gamma(I,D_ZC_u)(1)[1].
\tag{E.4}
\]

Here is the pairing that fixes the signs, before any geometric identification. Pair the degree-zero term of \(G(C_u)\) with the degree-zero term of \(G(V)(1)[1]\) by evaluation; pair their degree-one and degree-minus-one terms by negative evaluation. On \(c\otimes v\) of total degree minus one, the differential followed by this pairing is
\(-\langle\nu c,v\rangle+\langle c,mv\rangle=0\). These are precisely the dual evaluations on the two resolution terms. For complexes, the internal differentials obey the same rule with the Koszul signs from their degrees. Computing on resolutions for derived internal Hom and totalizing gives the displayed natural comparison. The ordinary constructible biduality and coefficient comparisons used to do this are still required foundations.

For trivial coefficients the resulting degree-one trace is
\(H^1(I,E(1))\to E\): evaluate the continuous homomorphism on the chosen generator and contract with its Tate basis. A generator change multiplies that value and the dual basis by inverse factors, so this trace is intrinsic. The geometric identification below uses this normalization together with the negative localization boundary in the fibre-coordinate identification (E.8).

### Keep the attaching homotopy in the cancellation

We use the following explicit cochain conventions:

\[
\begin{aligned}
\operatorname{Cof}(f)^n&=Y^n\oplus X^{n+1},&
d(y,x)&=(d_Yy+fx,-d_Xx),\\
\operatorname{Fib}(f)^n&=X^n\oplus Y^{n-1},&
d(x,y)&=(d_Xx,fx-d_Yy)
\end{aligned}
\]

for \(f:X\to Y\). The second model maps to \(\operatorname{Cof}(f)[-1]\) by \((x,y)\mapsto(-y,x)\). A resolved model here represents the finite diagram and its specified homotopies in the ambient enhanced derived category; it does not mean a bounded resolution by constructible injective sheaves. In these coordinates the map \(a:A\to G(C_u)\) consists of specialization \(s:A\to C_u\) and a degree-minus-one map \(h:A\to C_u(-1)\), with
\(\nu s=d h+h d\). The normalized variation is \((a_0,c)\mapsto h a_0-\nu c\) on \(\operatorname{Fib}(s)\). The canonical map from \(C_u[-1]\) sends \(c\) to \((0,-c)\), so their composite is \(\nu[-1]\), with the sign fixed by the logarithmic change of generator from Appendix C.

Now write \(W=D_ZA\), \(Q=D_ZB=\operatorname{Cof}(m:V(1)\to V)\), and \(b=D_Za:Q\to W\). Let \(g:V\to W\) be the restriction of \(b\), namely the dual specialization. In a resolved model, the other component is a degree-minus-one map \(k:V(1)\to W\). The chain-map equation for \(b\) is
\(g m=d_W k+k d_{V(1)}\). It is the dual attaching homotopy, and cannot be discarded. Dualizing localization yields

\[
i^*D_X^\delta K\simeq U=\operatorname{Cof}(b:Q\to W).
\tag{E.5}
\]

Appendix D identifies the unipotent nearby object of the dual input with \(V(1)[2]\). The candidate for its geometric specialization is

\[
p:U\longrightarrow Q[1]\longrightarrow V(1)[2].
\tag{E.6}
\]

The second arrow is the group augmentation under (E.4): \(Q[1]\) has differential \(-m=\nu_V(1)\). In coordinates,

\[
\begin{aligned}
U^n&=W^n\oplus V^{n+1}\oplus V(1)^{n+2},\\
d_U(w,v,z)&=(d_Ww+gv+kz,-d_Vv-mz,d_{V(1)}z),\\
p(w,v,z)&=z.
\end{aligned}
\]

The equality \(d_U^2=0\) uses exactly the displayed homotopy equation. Its kernel is \(\operatorname{Cof}(g:V\to W)\), but a calculation of the fibre also records the actual contraction. A fibre element is \((w,v,z,y)\), where \(y\in V(1)^{n+1}\), and its differential is

\[
d(w,v,z,y)=
(d_Ww+gv+kz,-d_Vv-mz,dz,z-dy).
\]

Define the inclusion \(e(w,v)=(w,v,0,0)\), the retraction
\(r(w,v,z,y)=(w-ky,v+my)\), and the degree-minus-one homotopy
\(H(w,v,z,y)=(0,0,y,0)\). Direct substitution gives
\(re=1\), \(rd=dr\), and \(dH+Hd=1-er\). For example, the first component of the latter identity is \(ky\), and the second is \(-my\); these are the terms lost by ignoring the attaching homotopy. Thus
\(\operatorname{Fib}(p)\simeq\operatorname{Cof}(g)=D_Z\Phi_uK\). This is a calculation of maps of resolved complexes, not just an equality of their cohomology dimensions. It is natural for maps of attaching diagrams, with the homotopies transported along those maps.

### The geometric boundary pairing

We now compare the two pairings with their actual boundary maps. The argument uses the ordinary functorial localization, tensor and exceptional adjunctions, open and proper base change, and multiplicative continuous descent. These are the same ambient operations used in Appendix D. Their geometric construction and normalized adic realization remain prerequisite obligations; the argument below proves the compatibility from these specified operations.

Write \(B_X(N)=i^*Rj_*N\) for an object on the generic fibre. Localization identifies it with \(G(R\psi_XN)\). Fix the isomorphism

\[
\lambda_N:B_X(N)[-1]\xrightarrow{\sim}i^!j_!N
\tag{E.8}
\]

by the fibre coordinates already used above: \(i^!j_!N=\operatorname{Fib}(0\to B_X(N))\), and \(\lambda_N(b)=(0,b)\). Thus \(\lambda_N\) is the **negative** of the boundary \(B_X(N)[-1]\to i^!j_!N\) in the rotated localization triangle. That boundary sends \(b\) to \((0,-b)\). Keeping this distinction is essential for the purity sign.

**Localization and multiplication.** For generic-fibre objects \(M,N\), let \(\mu:B_X(M)\otimes^L B_X(N)\to B_X(M\otimes^L N)\) be the cup product. Then the square

\[
\begin{array}{ccc}
B_X(M)\otimes^L B_X(N)[-1]&\xrightarrow{\mu[-1]}&B_X(M\otimes^L N)[-1]\\
\downarrow{1\otimes\lambda_N}&&\downarrow{\lambda_{M\otimes N}}\\
i^*Rj_*M\otimes^L i^!j_!N&\longrightarrow&i^!j_!(M\otimes^L N)
\end{array}
\tag{E.9}
\]

commutes. The top arrow includes the tensor-shift isomorphism: a homogeneous element of degree \(p\) in the first factor acquires \((-1)^p\) when the shift in the second factor is moved outside the tensor product.

Here is a proof that also specifies the lower arrow. Tensor the localization triangle for \(j_!N\) with \(Rj_*M\). The closed projection formula identifies its first term with
\(i_*(B_X(M)\otimes^L i^!j_!N)\); the open projection formula identifies its middle term with \(j_!(M\otimes^L N)\). The adjoint of the tensor product of the two open-restriction counits supplies the map from its third term to \(Rj_*(M\otimes^L N)\). These three maps form a morphism to the localization triangle of \(j_!(M\otimes^L N)\). On applying \(i^*\), the middle terms vanish and the third map is \(\mu\). The induced map of fibres is therefore the shifted cup product. In fibre coordinates it is the square (E.9); replacing each fibre-coordinate identification by the triangle boundary inserts a minus sign in both vertical arrows and leaves the square unchanged. The tensor-shift sign follows directly by comparing \(d(x\otimes y)=dx\otimes y+(-1)^p x\otimes dy\) before and after shifting.

The descent identification preserves this cup product. The direct-image and invariant functors have products adjoint to the tensor products of their pullback counits; the intervening restrictions are exact symmetric monoidal functors. In a descent resolution, taking these adjoints successively gives the nearby-cycle product followed by the continuous group-cochain product. Taking the composite counits at once gives the product on \(i^*Rj_*\). The counit of a composite adjunction is the composite of its counits, so these constructions agree. This identifies the maps, rather than just the cohomology groups of a descent spectral sequence. It applies to the entire inertia action; no tame replacement is made here.

**Transporting a boundary through a map.** Let \(h:X\to Y\) be separated and of finite type over the trait. There is a specified map

\[
b_h:Rh_{s!}i_X^!j_{X!}N\longrightarrow
i_Y^!j_{Y!}Rh_{\eta!}N.
\]

It is the adjoint, under \(i_{Y*}\dashv i_Y^!\), of

\[
i_{Y*}Rh_{s!}i_X^!j_{X!}N
\simeq Rh_!i_{X*}i_X^!j_{X!}N
\longrightarrow Rh_!j_{X!}N
\simeq j_{Y!}Rh_{\eta!}N.
\]

The middle arrow is the closed-support counit. Under (E.8) and descent, this map is

\[
Rh_{s!}G_X(R\psi_XN)[-1]
\xrightarrow{\kappa}
G_Y(Rh_{s!}R\psi_XN)[-1]
\xrightarrow{G_Y(\alpha_h)[-1]}
G_Y(R\psi_YRh_{\eta!}N)[-1].
\tag{E.10}
\]

Here \(\alpha_h\) is the map defined in Appendix D. The exchange map \(\kappa\) is the adjoint comparison with derived invariants, obtained from the base-change identity for pullback to the inertia topos. It is not being asserted to be an isomorphism for a general \(h\).

To prove (E.10), first let \(h=u\) be open. Transpose both proposed maps under \(u_{s!}\dashv u_s^*\). Open base change and \(u_\eta^*u_{\eta!}N=N\) identify their targets with \(i_X^!j_{X!}N\). The transpose of \(b_u\) is the identity, by the counit used to define it. The transpose of \(\alpha_u\) is also the identity by its definition. Open restriction preserves the localization fibre and \(\lambda\); hence the second transpose is that same identity, with the same fibre-coordinate sign. Adjunction proves equality.

For \(h=p\) proper, proper base change gives

\[
Rp_{s*}i_X^*Rj_{X*}N
\simeq i_Y^*Rp_*Rj_{X*}N
\simeq i_Y^*Rj_{Y*}Rp_{\eta*}N.
\]

Apply the same base-change maps to the localization triangle. Its closed-support arrow is the adjoint defining \(b_p\), so its fibre map gives \(b_p\) under \(\lambda\). Applying geometric-generic restriction followed by descent gives the right side of (E.10), since \(\alpha_p\) is that proper base-change map. Thus both are obtained from the same morphism of localization triangles. Finally choose a compactification \(h=pu\). Both constructions compose: for the first this follows by composing the displayed closed-support counits; for the second it follows by composing the pullback adjunctions defining \(\kappa\) and the maps \(\alpha\). The counit identity \(\epsilon_{vu}=\epsilon_v\circ Rv_!\epsilon_u\) identifies these composites. This proves (E.10), and also its independence of the compactification, under the ordinary compactification and coherence inputs of Appendix D.

**The base-trait trace and its sign.** Put \(\Omega_S=E_S(1)[2]\). Let \(q_S\) be the map

\[
G(E(1)[2])[-1]
\xrightarrow{\lambda}i_S^!j_{S!}E_\eta(1)[2]
\longrightarrow i_S^!\Omega_S\simeq E_s.
\tag{E.11}
\]

The last identification is the divisor-oriented purity of [Proposition B.1c](#base-trait-purity-with-its-divisor-orientation), with its compatible finite, complete and rational maps. We check that \(q_S\) is the positive group trace, including the sign relating that divisor class to Kummer theory. The passage from this base trace to a general \(X/S\) still uses the separate family-level exceptional adjunction and duality inputs.

At level \(\mathbf Z/\ell^n\), choose a uniformizer \(\pi\). Its Kummer torsor defines a class \(\kappa_\pi\) on the generic point. On inertia it is the tame character \(I\to\mathbf Z_\ell(1)\) reduced modulo \(\ell^n\): compatible roots of \(\pi\) are taken to each other by their root-of-unity ratios. Its value on the selected tame generator is the selected Tate basis. The divisor class is formed in the other order: take the localization boundary of \(\pi\) in \(\mathbf G_m\), then the Kummer boundary with supports. These two boundary operations anticommute. To see the sign, resolve the Kummer sequence and the restriction-to-the-open map in two directions; in the total complex the second differential on column \(r\) is multiplied by \((-1)^r\). Moving once in each direction in the opposite order therefore changes the sign. Equivalently, the two successive lifts defining the connecting maps have opposite total differentials. Consequently

\[
\partial_{\mathrm{loc}}\kappa_\pi=-\operatorname{cl}_{\ell^n}(s).
\tag{E.12}
\]

This is the convention in the free author edition of SGA 4½, *Cycle*, 2.1.1–2.1.3, printed pp. 138–139. It also explains the negative fundamental-class description on Illusie's printed p. 37. The author's [erratum](https://www.imo.universite-paris-saclay.fr/~luc.illusie/ErrTML.pdf) changes the upper differential of the shifted diagram there to \(1-T\); it does not remove (E.12).

In the fibre convention of this appendix, the ordinary localization boundary sends \(b\) to \((0,-b)\). In contrast, (E.11) first uses \(\lambda(b)=(0,b)\). Thus (E.12) and the divisor orientation give \(q_S(\kappa_\pi)=1\). The group trace has the same value by its defining evaluation on the tame character. There is no further component of the map to determine: \(G(E(1))[1]\) has cohomology only in degrees \(-1,0\), with degree-zero cohomology \(E\); its negative truncation belongs to \(D^{\leq-1}\), so every map from that truncation to \(E\in D^{\geq0}\) vanishes. A morphism from \(G(E(1))[1]\) to \(E\) is therefore determined by the induced map from its degree-zero truncation. Both maps induce the identity. This also works with residue-field descent, without choosing a splitting of its Galois extension. The compatible finite-level equality passes to the stated field coefficients through the normalized adic realization assumed in the lesson. Hence \(q_S=\operatorname{Tr}_I\).

**The trace on \(X\).** Write \(f:X\to S\), \(\omega_\eta=f_\eta^!E\), and \(\omega_Z=f_s^!E\). Let \(q_X\) be the geometric map

\[
G(R\psi_X\omega_\eta)(1)[1]
\xrightarrow{\lambda}i^!j_!j^*\omega_X^\delta
\longrightarrow i^!\omega_X^\delta\simeq\omega_Z.
\]

Its adjoint under \(Rf_{s!}\dashv f_s^!\) is (E.10) for \(N=\omega_\eta(1)[2]\), followed by the generic-fibre trace, and finally by \(q_S\). This follows directly from the defining counit of \(b_f\): after applying \(i_{S*}\), its composite is \(Rf_!j_!j^*f^!\Omega_S\to\Omega_S\); the two possible ways to compose it coincide by the open and exceptional counit identities.

The adjoint of

\[
G(R\psi_X\omega_\eta)(1)[1]
\xrightarrow{G(\theta_X)(1)[1]}G(\omega_Z)(1)[1]
\xrightarrow{\operatorname{Tr}_I}\omega_Z
\tag{E.13}
\]

is the same composite. Indeed, \(\theta_X\) was defined as the adjoint of \(\alpha_f\) followed by the generic trace. The exchange \(\kappa\) is the mate of pullback base change, and the group trace with a trivially acting complex is the tensor extension of the coefficient trace. Transposing the composite therefore inserts \(\kappa\), then \(G(\alpha_f)\), then that generic trace, then the base coefficient trace. This is exactly the composite just obtained from \(b_f\), since (E.11) is the coefficient trace. No invertibility of \(\kappa\) is used. Adjunction proves that \(q_X\) equals (E.13).

Now take \(M=j^*K\), \(M'=j^*D_X^\delta K\), \(C=R\psi M\), and \(C'=R\psi M'\). Apply (E.9) to their evaluation \(M\otimes^L M'\to\omega_\eta(1)[2]\), and then apply (E.13). The geometric pairing

\[
i^*Rj_*M\otimes^L i^!j_!M'\longrightarrow i^!\omega_X^\delta\simeq\omega_Z
\]

becomes exactly

\[
G(C)\otimes^L G(C')[-1]
\longrightarrow G(C\otimes^L C')[-1]
\longrightarrow G(\omega_Z(1)[2])[-1]
\xrightarrow{\operatorname{Tr}_I}\omega_Z.
\]

The middle map uses Appendix D's specified evaluation and \(\theta_X\). Thus the comparison holds for arbitrary constructible coefficients under the stated ambient inputs. The constant-coefficient calculation supplied the base trace only; (E.9), (E.10) and exceptional adjunction supplied its passage to every \(X\) and every evaluation pairing. All these constructions are maps of the same enhanced localization diagrams, so they retain the attaching homotopies used in (E.5), rather than just the isomorphism classes of the vertices.

Dualizing the actual localization diagram now identifies its boundary with \(U\to Q[1]\), and its specialization with the projection (E.6), using (E.8)'s sign. The displayed contraction consequently gives
\(D_Z\Phi_uK\simeq\Phi_u(D_X^\delta K)\). The finite-logarithm isomorphism \(\tau\simeq(1)\) on the unipotent object converts this into (E.2) there, with the specialization and variation maps of those same diagrams.

On \(C_r\), duality preserves the split: averaging is self-adjoint as in Appendix D, and the dual of an invertible \(T-1\) remains invertible, since \(T^{-1}-1=-T^{-1}(T-1)\). There are no derived invariants. The dual nearby summand is \(D_ZC_r(1)[2]\), whose vanishing summand is \(D_ZC_r(1)[1]\). Applying the actual isomorphism \(\tau\iota\) constructed above gives

\[
\tau\bigl(D_ZC_r(1)[1]\bigr)(-1)
\simeq D_ZC_r[1]
=D_Z(C_r[-1]).
\]

Together these calculations prove the full deduction of (E.2), with every inertia type and its descent action. Its outstanding proof prerequisites are now the ordinary enhanced six-operation and purity foundations, multiplicative continuous descent and their normalized adic realization, in addition to Appendix D's listed inputs. The formal deduction does not supply those foundations.

### Normalizing the duality comparison

Suppose the trait is obtained from a smooth curve over a field, and let \(D_X\) denote absolute total-space duality over that field. Its relative version is \(D_{X/S}=D_X(-1)[-2]\), because the base curve contributes \(E(1)[2]\). The normalized objects are \(\Psi_fK=R\psi j^*K[-1]\) and \(\Phi_fK=R\phi K[-1]\). Accordingly the required absolute formulas are

\[
D_Z\Psi_fK\simeq\Psi_f(D_XK)(-1),
\qquad
D_Z\Phi_fK\simeq\tau\Phi_f(D_XK)(-1).
\tag{E.7}
\]

The first follows from Appendix D with its stated inputs: dualizing \([-1]\) contributes \([1]\), and the total-space generic restriction contributes \((1)[2]\). The second is (E.2), using the boundary comparison (E.8)–(E.13) under its stated foundational inputs. Equivalently, substituting \(D_{X/S}=D_X(-1)[-2]\) in the unnormalized relative formula and then dualizing its shift gives exactly the second displayed formula. Agreement with that formula checks the normalization; the comparison map itself is supplied by the preceding localization and trace argument.

The two assigned tests remain useful. If \(K=i_*A\), its nearby object is zero and \(\Phi_fK=A\). Trivial inertia makes \(\tau A\simeq A(1)\), so the two twists in the second formula cancel and give ordinary closed-fibre duality.

For a wild test, work on the affine line over an algebraically closed field of characteristic \(p\ne\ell\). Choose a coefficient field containing the values of a nontrivial character of \(\mathbf F_p\), and take the rank-one local system \(L\) on the punctured line defined by \(y^p-y=1/t\) and that character. This cover is connected locally: if a Laurent-series element has a pole of order \(d>0\), then \(y^p-y\) has pole order \(pd\); an element without a pole cannot give \(1/t\). Hence the equation has no root even in the completed local field. Its roots are \(y+c\), for \(c\in\mathbf F_p\); adjoining one gives all of them, so the Galois group is a subgroup of the prime-order translation group. Without a root it has order \(p\). Over a strictly henselian base this degree-\(p\) quotient of inertia is wild, since tame inertia has only prime-to-\(p\) finite quotients. Its invariants on the chosen character vanish. Exact averaging then gives \(R\Gamma(I,L)=0\), so localization identifies \(Rj_*L=j_!L\) near zero. If \(V\) is its geometric generic representation and \(K=j_!L[1]\), direct specialization and ordinary smooth-curve duality give

\[
\Phi_fK=V,
\qquad D_XK=j_!L^\vee(1)[1],
\qquad\Phi_f(D_XK)=V^\vee(1).
\]

Here the twist functor is literally the identity on the non-\(H\)-invariant summand, so the remaining \((-1)\) in (E.7) is necessary to recover \(V^\vee\). This verifies the twist distinction in the example, subject to its ordinary sheaf and duality inputs. The general geometric compatibility uses the preceding localization and trace argument, not these two tests alone.

The full torsion-coefficient sliced-duality theorem is a separate, broader formalism result. The finite logarithm used in this appendix cannot prove it, and no such extension of the field calculation is claimed.

## Appendix F. Cyclic-cover descent and general gluing morphisms

This appendix uses classical sheaves of vector spaces over a field \(k\). Complexes are cohomologically graded, with \(d(a)=d_2a-(-1)^{|a|}ad_1\). The injective resolution functor \(I\) and the bounded-below injective Hom calculation are constructed in [Lesson 1, A.1 and B.1](constructible-complexes-on-algebraic-varieties.md#b-1-complexes-resolutions-and-triangle-signs). Its resolution terms are exact additive functors of sheaves. Its totalization acts on homogeneous maps, preserves their differentials and compositions, and commutes with finite cones and shifts under the coordinate identifications of that construction.

### F.1. The actual cyclic-cover comparison

**Proposition F.1.** Let \(j:U\hookrightarrow X\) be open with closed complement \(i:Z\hookrightarrow X\), and let \(p:\widetilde U\to U\) be a covering with deck group \(\mathbb Z\), acting transitively on every fibre. Fix its generator \(T\). For every bounded-below complex \(M\) of sheaves on \(U\), put \(C(M)=i^*R(jp)_*p^*M\). There is a natural comparison, on the actual complexes and homogeneous maps,

\[
i^*Rj_*M\simeq\operatorname{Fib}(T-1:C(M)\to C(M)).
\tag{F.1}
\]

**Proof.** A covering has an exact left adjoint \(p_!\) to inverse image. On an evenly covered open, it is the direct sum of the sheaves on the sheets, transported to that open. These definitions agree on overlaps by the permutation of sheets. Its stalk at \(x\) is \(\bigoplus_{y\in p^{-1}(x)}F_y\), which proves exactness. A map from that direct sum to a sheaf on the base is precisely a compatible family of maps to its pullbacks on the sheets, proving the adjunction. Hence \(p^*\) sends injectives to injectives: extend a map from a subobject by applying exact \(p_!\) and injectivity. Direct image along any continuous map preserves injectives, because inverse image is exact.

Choose the additive bounded-below injective model \(J=I_U(M)\). For each term there is a natural exact sequence on \(U\),

\[
0\longrightarrow J^n\longrightarrow p_*p^*J^n
\xrightarrow{T-1}p_*p^*J^n\longrightarrow0.
\tag{F.2}
\]

On an evenly covered open the middle and last section groups are products indexed by \(\mathbb Z\). The first arrow is the constant-sequence map. The kernel of the difference operator consists of constant sequences. Given a sequence \((b_m)\), solve \(a_{m+1}-a_m=b_m\) by setting \(a_0=0\) and taking finite forward or backward sums for each integer \(m\). This proves surjectivity locally and hence exactness of sheaves, with no interchange of stalks and infinite products. Reversing the indexing handles the equivalent inverse-generator convention.

The left term of (F.2) is injective, so its monomorphism has a sheaf retraction. The sequence therefore splits on terms. Applying \(j_*\) preserves its exactness, and applying exact \(i^*\) gives the short exact sequence of complexes

\[
0\longrightarrow D_J:=i^*j_*J
\longrightarrow C_J:=i^*(jp)_*p^*J
\xrightarrow{N}C_J\longrightarrow0,
\qquad N=T-1.
\tag{F.3}
\]

The retractions establish exactness only; no chosen retraction enters these maps. Since \(p^*J\) is a bounded-below injective complex, \((jp)_*p^*J\) computes \(R(jp)_*p^*M\); \(j_*J\) computes \(Rj_*M\). The kernel-to-fibre map of (F.3) is a quasi-isomorphism. For the fibre convention \(d(x,y)=(dx,Nx-dy)\), its quotient is the fibre of the identity on the quotient \(C_J/D_J\cong C_J\), and is contractible. All its maps commute with homogeneous maps of \(J\)'s. This proves (F.1). \(\square\)

Here is a useful injective version of the comparison. Set

\[
E_J=I_Z(C_J[-1]),\qquad
B_J=\operatorname{Cone}(N:E_J\to E_J).
\tag{F.4}
\]

The shift is the normalized nearby-cycle shift. The map \(D_J\to\operatorname{Cone}(N:C_J[-1]\to C_J[-1])\) sends \(x\) to \((0,x)\), where the cone coordinates are target followed by shifted source. It is the comparison of (F.3), with the cone/fibre shift sign included. Applying \(I_Z\) and its natural unit gives a natural quasi-isomorphism \(q_J:D_J\to B_J\). Both \(E_J\) and \(B_J\) are bounded-below injective complexes. For a homogeneous open map \(f\) of degree \(n\), write \(t=E(f)\). On the cone, \(B(f)=\operatorname{diag}(t,(-1)^nt)\). This sign makes it a map of Hom complexes, and \(N't=tN\) holds in every degree.

For a regular or holomorphic function in §4, the pullback of the universal cover of \(\mathbb C^*\) is exactly such a covering. Thus (F.1) proves (4.4) at the bounded-below classical sheaf scope, including positive-dimensional \(Z\). It does not assert bounded constructibility of \(C(M)\); that geometric assertion is a separate input to §5.

### F.2. Attaching data on a general closed fibre

**Lemma F.2.** Let \(A\) be a bounded-below injective complex on \(Z\), and let \(a:A\to B_J\) be a chain map. Define

\[
K(J,A,a)=\operatorname{Fib}\bigl(j_*J\oplus i_*A
\xrightarrow{q_J\rho-i_*a}i_*B_J\bigr),
\tag{F.5}
\]

where \(\rho\) is the restriction unit. Then \(j^*K=J\), \(i^*K\simeq A\), and \(i^!K\simeq\operatorname{Fib}(a)\). Every bounded-below sheaf complex is recovered from its open restriction and closed attaching map. For two data, the derived mapping complex is

\[
\mathcal G=\operatorname{Fib}\!\left(
\operatorname{Hom}_U(J,J')\oplus\operatorname{Hom}_Z(A,A')
\xrightarrow{(f,g)\mapsto B(f)a-a'g}
\operatorname{Hom}_Z(A,B_{J'})\right).
\tag{F.6}
\]

**Proof.** The terms in (F.5) are injective: direct images \(j_*\) and \(i_*\) preserve injectives, and a finite sum of injectives is injective. Its fibre is therefore a bounded-below injective model. Open restriction gives \(J\). Closed restriction is \(\operatorname{Fib}(D_J\oplus A\to B_J)\). Its projection \(r:i^*K\to A\) has kernel \(\operatorname{Fib}(q_J)\), which is acyclic, so \(r\) is a quasi-isomorphism. It need not be a homotopy equivalence between the closed restrictions themselves. Support restriction kills \(j_*J\), and on \(i_*\) it is the identity; the fibre sign is changed by negating its second coordinate. This gives the costalk assertion, using the support sequence of [Lesson 1, B.2](constructible-complexes-on-algebraic-varieties.md#b-2-the-actual-open-closed-recollement).

For recovery, resolve the actual open and closed restrictions of a complex. The map to its boundary transfers to a map \(a:A\to B_J\), with the comparison homotopy retained: Hom into the injective target \(B_J\) sends the resolution quasi-isomorphism to a quasi-isomorphism. The two restriction units and that homotopy give a map to (F.5). Its open and closed restrictions are quasi-isomorphisms. Its cone is acyclic on every stalk, hence is acyclic on \(X\).

A degree-\(n\) element of (F.6) is \((f,g,h)\), with \(|h|=n-1\) and differential

\[
(f,g,h)\longmapsto(df,dg,B(f)a-a'g-dh).
\tag{F.7}
\]

In the fibre coordinates \((r_0,x,y)\) of (F.5), its map to \(\operatorname{Hom}_X(K,K')\) is

\[
(r_0,x,y)\longmapsto
\bigl(j_*f(r_0),g(x),(-1)^n B(f)y+h(x)\bigr).
\tag{F.8}
\]

Substitution of the fibre differential gives (F.7). Applying \(\operatorname{Hom}_X(K,-)\) to (F.5) for \(K'\), the adjunctions give the open term \(\operatorname{Hom}_U(J,J')\) and closed terms \(\operatorname{Hom}_Z(i^*K,A')\), \(\operatorname{Hom}_Z(i^*K,B_{J'})\). Precomposition by \(r\) is a quasi-isomorphism on both closed terms because their targets are bounded-below injectives. Filtering the two mapping fibres by their last shifted term proves that (F.8) is a quasi-isomorphism. In degree zero its composition law is \((f',g',h')(f,g,h)=(f'f,g'g,B(f')h+h'g)\). This proves (F.6) for arbitrary \(Z\), without treating its sheaves as vector spaces or suppressing their positive Ext groups. \(\square\)

For later use, every attaching map has a factorization model. Write \(E=E_J\), \(B=E\oplus E[1]\), and \(a=(a_0,a_1):A\to B\). In unshifted coordinates \(a_1:A\to E\) has degree one. The chain-map identities are

\[
da_0=-Na_1,\qquad da_1=0.
\tag{F.9}
\]

Put \(W=\operatorname{Fib}(-a_1:A\to E[1])\), with

\[
d_W(x,e)=(d_Ax,-a_1x+d_Ee),\qquad
u(e)=(0,e),\qquad v(x,e)=a_0x+Ne.
\tag{F.10}
\]

Equation (F.9) gives \(du=dv=0\) and \(vu=N\). Projection \(\operatorname{Cone}(u)\to A\) is a quasi-isomorphism: its kernel is the contractible cone of \(1_E\). The induced attaching map \((v,1):\operatorname{Cone}(u)\to B\) differs from \(a\) after projection by the differential of \(H(x,e,z)=(0,e)\). Indeed that differential is \((Ne,z-a_1x)\). Thus the comparison includes its attaching homotopy. Under the resolution comparison \(C_J\simeq E[1]\), the map \(a_1\) represents specialization. Hence \(W\) is the normalized vanishing complex with the convention of (4.2)–(4.3); swapping the two fibre coordinates identifies it with \(\operatorname{Cone}(a_1)[-1]\).

Conversely, if \(u:E\to W\), \(v:W\to E\) are closed and \(vu=N\), take \(A=\operatorname{Cone}(u)\), \(a=(v,1)\). Its costalk fibre cancels the identity on the shifted copy of \(E\) and is \(\operatorname{Cone}(v)[-1]\). This can be checked in coordinates: in \(\operatorname{Fib}(a)\), write \((w,e;x,y)\), where \((w,e)\in W\oplus E[1]\) and \((x,y)\in E[-1]\oplus E\). The coordinate change \((w,e;x,y)\mapsto(w-uy,x;y,e)\) splits its differential into \(W\oplus E[-1]\) with differential \((w,x)\mapsto(d_Ww,vw-d_Ex)\), and the contractible pair \((y,e)\mapsto(d_Ey+e,-d_Ee)\). The first summand is the fibre of \(v\), identified with \(\operatorname{Cone}(v)[-1]\) by negating its cone target coordinate. The same identity cancellation in specialization returns \(W,u,v\).

### F.3. The mapping complex of two factorizations

**Proposition F.3.** Suppose \(vu=N\) and \(v'u'=N'\) hold as chain maps between the injective models \(E,W\) and \(E',W'\). Let \(K,K'\) be their glued objects. Set

\[
\begin{aligned}
\mathcal A&=\operatorname{Hom}_U(J,J')\oplus\operatorname{Hom}_Z(W,W'),\\
\mathcal B&=\operatorname{Hom}_Z(E,W')\oplus\operatorname{Hom}_Z(W,E'),\\
\mathcal C&=\operatorname{Hom}_Z(E,E'),\\
\delta_0(f,g)&=(gu-u'E(f),\ E(f)v-v'g),\\
\delta_1(b,c)&=v'b+cu.
\end{aligned}
\tag{F.11}
\]

Then \(R\operatorname{Hom}_X(K,K')\) is represented by the three-column total complex

\[
\begin{gathered}
\mathcal T^n=\mathcal A^n\oplus\mathcal B^{n-1}\oplus\mathcal C^{n-2},\\
D(a,\beta,\gamma)=(da,\delta_0a-d\beta,\delta_1\beta+d\gamma).
\end{gathered}
\tag{F.12}
\]

**Proof.** Both \(\delta_i\) commute with the internal differentials, and
\(\delta_1\delta_0(f,g)=E(f)N-N'E(f)=0\). Hence \(D^2=0\). We compare this specific complex with (F.6). Order the cone coordinates as \(A=W\oplus E[1]\), \(B'=E'\oplus E'[1]\). In degree \(n\) write the two closed components of (F.6) as matrices

\[
g_A=\begin{pmatrix}g&m\\r&s\end{pmatrix},\qquad
h=\begin{pmatrix}b&c\\\ell&e\end{pmatrix}.
\tag{F.13}
\]

In unshifted Hom complexes the degrees of \((g,m,r,s)\) are \((n,n-1,n+1,n)\), and those of \((b,c,\ell,e)\) are \((n-1,n-2,n,n-1)\). Put \(t=E(f)\). There is a subcomplex given by

\[
r=\ell=e=0,\qquad s=(-1)^nt,
\qquad m=(-1)^n\beta_1,\quad b=\beta_2,\quad c=(-1)^n\gamma.
\tag{F.14}
\]

Indeed the surviving components of (F.7) are

\[
\begin{aligned}
g_{\mathrm{new}}&=dg,\\
m_{\mathrm{new}}&=dm-(-1)^n(gu-u't),\\
b_{\mathrm{new}}&=tv-v'g-db,\\
c_{\mathrm{new}}&=-v'm-dc-(-1)^nbu.
\end{aligned}
\tag{F.15}
\]

After the signs in (F.14), these are exactly (F.12). To prove that its inclusion is a quasi-isomorphism, use quotient coordinates \((r,\bar s,\ell,e)\), with \(\bar s=s-(-1)^nt\). Their differential is

\[
(r,\bar s,\ell,e)\longmapsto
\bigl(-dr,-d\bar s-(-1)^nru,\ -r+d\ell,\ -\bar s+de-(-1)^n\ell u\bigr).
\tag{F.16}
\]

The subcomplex \(r=\ell=0\) and the quotient by it each have the form
\((x,y)\mapsto(-dx,-x+dy)\). Such a complex contracts by \((x,y)\mapsto(-y,0)\): the two composites with its differential sum to the identity. Both successive pieces are therefore acyclic, so the quotient of (F.6) by (F.14) is acyclic. This proves the claimed quasi-isomorphism in every degree. In particular, the term \(\mathcal C^{n-2}\) retains the homotopy of the relation \(vu=N\); omitting it would change the derived mapping problem. \(\square\)

### F.4. Heart morphisms and independence of representatives

**Corollary F.4.** Suppose \(M,M'\) are perverse on \(U\) and \(E,E',W,W'\) are perverse on \(Z\), at the cycle t-exactness scope of §5. Then

\[
\operatorname{Hom}_X(K,K')
\cong\{(f,g):gu=u'E(f),\quad E(f)v=v'g\},
\tag{F.17}
\]

where \(f:M\to M'\) and \(g:W\to W'\) are heart morphisms. Composition is componentwise. No restriction on the dimension of \(Z\), and no vanishing of positive Ext groups, is needed.

**Proof.** Negative derived Hom between two heart objects vanishes by t-structure orthogonality: for \(q<0\), the shifted target lies in \({}^pD^{\ge1}\) and the source in \({}^pD^{\le0}\). Consequently \(H^{<0}\mathcal A=H^{<0}\mathcal B=H^{<0}\mathcal C=0\). We show directly that
\(H^0\mathcal T=\ker(H^0\delta_0)\).

Represent a pair in this kernel by a closed \(a\in\mathcal A^0\). Choose \(\beta\in\mathcal B^{-1}\) with \(d\beta=\delta_0a\). Then \(\delta_1\beta\) is closed in degree minus one; since \(H^{-1}\mathcal C=0\), there is \(\gamma\in\mathcal C^{-2}\) with \(d\gamma=-\delta_1\beta\). These give a cocycle of (F.12). If a cocycle maps to zero in \(H^0\mathcal A\), first subtract the boundary of an element of \(\mathcal A^{-1}\) to make its \(\mathcal A\)-coordinate zero. Its \(\mathcal B^{-1}\)-coordinate is now closed and is a boundary, since \(H^{-1}\mathcal B=0\). Subtract the corresponding total boundary to remove it. The remaining \(\mathcal C^{-2}\)-coordinate is closed and is a boundary because \(H^{-2}\mathcal C=0\). This proves injectivity as well as surjectivity. Formula (F.11) gives precisely the two equations in (F.17). The degree-zero matrix representatives in (F.14) have zero lower-left component; (F.8) therefore makes their open and \(W\)-components compose as \(f'f\) and \(g'g\). This proves the composition assertion. \(\square\)

An equality \(vu=N\) of heart morphisms need not hold strictly on initially selected injective representatives. Let \(h:E\to E\) have degree minus one and \(dh=vu-N\). There is an explicit strict representative. Put \(W_s=W\oplus\operatorname{Cone}(1_E)\), and in its coordinates \((w,x,y)\) define

\[
u_s(e)=(ue,e,0),\qquad
v_s(w,x,y)=vw+(N-vu)x-hy.
\tag{F.18}
\]

Both maps are closed: on the cone summand, \(d(-h)=N-vu\) is exactly the chain-map equation for \((x,y)\mapsto(N-vu)x-hy\). Their composite is \(N\). The added summand contracts, so \(W_s\simeq W\). The projection to \(W\) carries \(u_s\) to \(u\); \(v_s-v\operatorname{pr}_W\) is the differential of \((w,x,y)\mapsto-hx\). Thus it represents the same heart factorization. Every such factorization admits the strict model required by Proposition F.3. Different choices induce the identity pair on the heart data; Corollary F.4 gives a unique isomorphism of their glued objects with that pair. The same argument gives independence of chosen representatives of a morphism.

Together, (F.10), (F.17) and (F.18) prove the full attaching and morphism assertions used in Theorem 6.1. Under §5's bounded constructibility and t-exactness hypotheses, the stalk and costalk bounds in (6.2) make the reconstructed object perverse, and its recovered \(W\) is the perverse vanishing object. The unipotent/complement splitting in (6.3) then gives the stated unipotent equivalence. These arguments prove the classical descent and mapping statements; the geometric constructibility and affine/Stein hypotheses of §5 and the arithmetic operation and descent statements in Appendices A–E retain their own proof requirements.

## Appendix G. Finite nearby complexes and the resolution reduction

Throughout this appendix, coefficients are finite-dimensional vector spaces over an arbitrary field \(k\). No finite-monodromy, unipotence or characteristic-zero condition on \(k\) is imposed. The spaces carry the classical topology. The algebraic conclusions concern separated complex varieties of finite type. Analytic spaces enter the local coordinate calculation; the global algebraic reduction does not assert an analytic resolution theorem.

### G.1. Local coefficients on a covered torus

Let \(V\) be a finite-dimensional \(k\)-space and let \(A_1,\ldots,A_s\) be commuting automorphisms. Define the cochain complex

\[
Q^q(V;A_1,\ldots,A_s)=
V\otimes_k\bigwedge^q k^s,
\qquad
d(v\otimes\omega)=\sum_{i=1}^s(A_i-1)v\otimes(e_i\wedge\omega).
\tag{G.1}
\]

It occupies degrees \(0,\ldots,s\). Commutativity and the alternating exterior product give \(d^2=0\), including in characteristic two, where the exterior algebra still has \(e_i\wedge e_i=0\).

**Lemma G.1.** If \(L\) is the local system with these transports on \(\mathbb R^s/\mathbb Z^s\), then \(R\Gamma(\mathbb R^s/\mathbb Z^s,L)\) is represented by (G.1). The comparison is natural in maps of local systems. Products with contractible intervals or balls give the same complex, with the comparisons induced by restriction and transport.

**Proof.** Put \(R=k[t_1^{\pm1},\ldots,t_s^{\pm1}]\). For one generator the sequence

\[
0\longrightarrow k[t^{\pm1}]
\xrightarrow{t-1}k[t^{\pm1}]
\xrightarrow{t\mapsto1}k\longrightarrow0
\tag{G.2}
\]

is exact. Multiplication by \(t-1\) is injective, and a Laurent polynomial whose coefficients sum to zero is divisible by \(t-1\): multiply by a power of \(t\) and use the finite geometric-sum identity on each monomial. Tensor these \(s\) augmented resolutions over \(k\). Tensoring preserves their quasi-isomorphisms, since an acyclic complex of vector spaces contracts after choosing complements to its cycle spaces. The resulting bounded free \(R\)-resolution of \(k\) has one exterior generator for every subset of \(\{1,\ldots,s\}\). Its differential is the alternating multiplication by \(t_i-1\).

The universal cover \(\mathbb R^s\) has an augmented singular-chain complex that is another free \(R\)-resolution of \(k\). Freeness follows by choosing one lift of each singular simplex downstairs; contraction of \(\mathbb R^s\), with the prism identity, proves exactness. Two such free resolutions have chain maps lifting the identity of \(k\): lift a generator at degree zero through the augmentation, then lift its boundary at each succeeding degree through the cycle space of the other resolution. The same lifting constructs a homotopy between two choices. Applying \(\operatorname{Hom}_R(-,V)\) therefore identifies their cochain complexes up to homotopy. On the finite resolution this is exactly (G.1).

Local-coefficient singular cochains compute derived sheaf sections by the explicit resolution in [Lesson 1, G.2](constructible-complexes-on-algebraic-varieties.md#g-2-local-coefficients-and-finite-cohomology-of-the-links-used-here). The same proof gives homotopy invariance with coefficient transport. It applies to the projections and slices of the asserted contractible factors, and to restrictions between smaller such factors. This proves the lemma. \(\square\)

We next keep track of the components of a cyclic cover. For integers \(m_1,\ldots,m_r\geq0\), not all zero, write

\[
m:\mathbb Z^r\longrightarrow\mathbb Z,
\qquad m(n)=\sum_i m_i n_i,
\qquad d=\gcd(m_1,\ldots,m_r)>0,
\qquad H=\ker m.
\tag{G.3}
\]

The Euclidean algorithm, applied to two entries at a time, gives a basis \(h_1,\ldots,h_{r-1},v\) of \(\mathbb Z^r\) with \(m(h_i)=0\), \(m(v)=d\). Indeed each Euclidean row operation is an invertible integral change of basis; it reduces the row \((m_i)\) to \((0,\ldots,0,d)\). Thus \(H\cong\mathbb Z^{r-1}\) and \(\mathbb Z^r=H\oplus\mathbb Zv\).

Consider \(f(z)=z_1^{m_1}\cdots z_r^{m_r}\) on
\(S=(\Delta^*)^r\times\Delta^{n-r}\). Its pullback of the universal cover of \(\mathbb C^*\) has exactly \(d\) connected components. To see both the count and the topology, write \(z_i=\exp(x_i+2\pi\mathrm i y_i)\), where \(x_i<\log\epsilon_i\). A point of the pulled-back cover has a lift

\[
\tau=\sum_i m_i(x_i+2\pi\mathrm i y_i)+2\pi\mathrm i\ell,
\qquad \ell\in\mathbb Z.
\tag{G.4}
\]

Replacing \(y\) by \(y+a\), \(a\in\mathbb Z^r\), replaces \(\ell\) by \(\ell-m(a)\). The component label is therefore \(\ell\bmod d\), and a fixed label identifies its angular coordinate with \(\mathbb R^r/H\). The basis above identifies this quotient with \(\mathbb R\times(\mathbb R/\mathbb Z)^{r-1}\). Its other factors are the convex radial box and \(\Delta^{n-r}\).

Consequently, if \(L\) has fibre \(V\) and transport representation \(\rho:\mathbb Z^r\to\operatorname{GL}(V)\), the section complex on the pulled-back cover is

\[
\bigoplus_{c\in\mathbb Z/d\mathbb Z}
Q^\bullet(V;\rho(h_1),\ldots,\rho(h_{r-1})).
\tag{G.5}
\]

The finite sum records distinct components, not a sum over all deck translates. Choices of origins and bases give models for the same derived section complex. Restriction to a smaller polydisc contracts only radial and ball factors; it is a quasi-isomorphism under (G.5). Deck translation acts on the actual cover, permutes its components and transports the coefficients. The comparisons with cochains retain that action. No specialization of the eigenvalues of \(\rho\) is used.

### G.2. Proper direct images commute with the actual cycle complex

**Proposition G.2.** Let \(\pi:Y\to X\) be proper, let \(f:X\to\mathbb C\) be continuous, and put \(g=f\pi\). Assume the locally compact, Hausdorff, metrizable and finite-dimensional hypotheses of [Lesson 1, H.1–H.2](constructible-complexes-on-algebraic-varieties.md#h-2-derived-fibers-bounds-and-arbitrary-proper-support-base-change). Write \(\pi_U:Y\setminus g^{-1}(0)\to X\setminus f^{-1}(0)\) and \(\pi_0:g^{-1}(0)\to f^{-1}(0)\). For every bounded-below complex \(M\) on the open part of \(Y\), there is a natural isomorphism

\[
R\psi_f(R\pi_{U*}M)\simeq R\pi_{0*}R\psi_g(M).
\tag{G.6}
\]

It respects deck monodromy. For a complex on all of \(Y\), it also respects specialization and hence gives the corresponding vanishing-cycle comparison.

**Proof.** Use subscripts \(X,Y\) for the open inclusions, cover maps and closed inclusions, and put \(q_X=j_Xp_X\), \(q_Y=j_Yp_Y\). There is a Cartesian square on the open covers, with induced proper map \(\widetilde\pi\). Proper base change and composition of ordinary direct images give

\[
\begin{aligned}
i_X^*Rq_{X*}p_X^*R\pi_{U*}M
&\simeq i_X^*Rq_{X*}R\widetilde\pi_*p_Y^*M\\
&\simeq i_X^*R\pi_*Rq_{Y*}p_Y^*M\\
&\simeq R\pi_{0*}i_Y^*Rq_{Y*}p_Y^*M.
\end{aligned}
\tag{G.7}
\]

The final use of proper base change is valid before any bounded-constructibility assertion: H.2 proves its actual map for bounded-below complexes. Every object to which it is applied here is bounded below. Composition is computed on injective resolutions, since direct images preserve injectives. The first base-change square can also be checked on the open sets where the covering is a disjoint union of homeomorphisms. Thus the infinite covering introduces no properness assumption on \(p_X\) and no interchange of a product with a stalk colimit.

All maps in (G.7) are the adjunction comparisons for the indicated squares. The pasting statement of H.2 makes them commute with a deck transformation and with the unit defining specialization. For a complex on \(Y\), proper base change also identifies its restricted direct image with \(R\pi_{0*}\) of its closed restriction. The two specialization triangles are therefore identified term by term, and their actual cone construction gives the vanishing-cycle assertion. \(\square\)

### G.3. Normal-crossing boundary data

**Proposition G.3.** Let \(Y\) be a smooth complex algebraic variety of dimension at most \(n\), let \(D\) be a simple-normal-crossing divisor, and put \(S=Y\setminus D\). Let \(g:Y\to\mathbb C\) be regular, nonzero on every component, with \(g^{-1}(0)\subset D\). Let \(L\) be a finite-rank local system on \(S\), and let \(b:S\hookrightarrow Y\setminus g^{-1}(0)\). Then

\[
R\psi_g(Rb_*L)\in D^{[0,n-1]}_c(g^{-1}(0);k).
\tag{G.8}
\]

For a zero-dimensional component the zero fibre is empty. More precisely, at a point where \(r\) components of \(D\) meet and where \(g=u\prod_{i=1}^r z_i^{m_i}\), the stalk is (G.5). In particular,

\[
\dim_k H^q(R\psi_gRb_*L)_y
\leq d\,\operatorname{rank}(L)\binom{r-1}{q}
\quad(0\leq q\leq r-1),
\tag{G.9}
\]

and it vanishes in other degrees. In a holomorphic chart with this monomial form the same local statement holds.

**Proof.** At a point of the zero fibre choose algebraic normal-crossing parameters. The local monomial form follows directly from the Nullstellensatz: since the zero set of \(g\) lies in the boundary, some power of the product of its parameters belongs to \((g)\). Each parameter is prime, because its quotient is a regular local domain. Dividing this monomial between \(g\) and the other factor shows that \(g\) is a unit times a product of powers of those parameters, as in G.4 below. The domain and regular-quotient facts are proved in Regular local rings, Theorem 1.1 and Corollary 1.2; the Nullstellensatz input is Lesson 1, K.1. The corresponding holomorphic coordinates are supplied by the invertible Jacobian. The multiplicities \(m_i\) are nonnegative, and at least one is positive. A nonvanishing holomorphic unit has an \(m_i\)-th root on a smaller chart: divide by its value at the centre, use the convergent logarithm series near one, and exponentiate the divided logarithm. Replace that coordinate by \(z_i u^{1/m_i}\). Its Jacobian is invertible at the centre, so this is a holomorphic coordinate change; it preserves every coordinate boundary hyperplane and makes \(g=\prod_i z_i^{m_i}\). Smaller polydiscs in the new coordinates are cofinal neighborhoods of the point.

Inverse image by a covering commutes with the direct image of an open inclusion, including its derived version. On a sheet it is the same restriction of sections; inverse image by a covering preserves injectives by F.1, and open direct image also preserves injectives. Apply this to \(b\). By composition, the stalk of the left side of (G.8) is the filtered colimit of derived sections of the pullback of \(L\) on the covered punctured polydiscs \((\Delta^*)^r\times\Delta^{n-r}\). Stalks and filtered colimits of vector spaces are exact, so this is a calculation on the actual injective model, without a product–colimit exchange. The restriction maps on this cofinal family are the quasi-isomorphisms proved after (G.5). Thus (G.5) computes the stalk and gives (G.9).

Fix one boundary stratum, determined by exactly which divisor components contain the point. On a small ball in that stratum the same normal coordinates, root of the unit and radial contractions work with the tangential coordinate as a parameter. The local system on the punctured product is pulled back from its normal factor, because the tangential ball is contractible; path transport and its homotopy invariance give this identification. Sections over smaller tangential balls therefore give the same complex (G.5), with the actual restriction maps. Its cohomology sheaves are locally constant on the stratum. The divisor has finitely many algebraic components and hence finitely many such algebraic strata. Refining them by Lesson 1, K.6 preserves local constancy. The uniform bound \(r\leq n\) proves bounded algebraic constructibility and (G.8). \(\square\)

For \(g=z^d\), the covered puncture has \(d\) contractible components, so its nearby stalk is \(V^{\oplus d}\) in degree zero. For \(g=z_1^2z_2^4\) on a two-dimensional chart, \(H\) has basis \((2,-1)\), and (G.5) is two copies of \([V\xrightarrow{A_1^2A_2^{-1}-1}V]\) in degrees zero and one. For \(g=z_1\) with the additional boundary \(z_2=0\), the kernel generator is \((0,1)\), so the complex is \([V\xrightarrow{A_2-1}V]\). The last example displays the horizontal-boundary contribution even though the defining function is smooth.

Horizontal boundary components are included: their exponent \(m_i\) is zero, while their transport still occurs in \(\rho|_H\). Thus (G.8) is not limited to a local system on the entire complement of the zero fibre. This is the form needed for the reduction below.

### G.4. The algebraic reduction and its geometric inputs

The geometric input has two parts: a projective smooth resolution of a reduced irreducible affine complex variety, unchanged over its smooth locus; and principalization of an ideal on its smooth modification by smooth blow-ups, unchanged outside its zero set. [Theorem I.1](#i-4-the-required-projective-modifications) proves these assertions using the fixed-dimensional order-reduction and maximal-contact construction. [Appendix H](#appendix-h-blow-up-charts-projectivity-and-boundary-factors) supplies the Rees-chart, projectivity and boundary-factor calculations. The following proof combines those geometric results with the actual proper comparison and the local normal-crossing model.

**Theorem G.4 (algebraic constructibility).** \(R\psi_f\) sends bounded algebraically constructible complexes on \(X\setminus f^{-1}(0)\) to bounded algebraically constructible complexes on \(f^{-1}(0)\), for every regular function on a separated complex variety of finite type. Consequently the actual specialization cone has the same property. No condition on the finite-rank monodromy representations is needed.

**Proof.** This assertion is local on \(X\). Open restriction commutes with the defining derived direct image by restriction of injective resolutions. Choose a finite affine open cover. Finite algebraic stratifications on the members combine by a common refinement and their membership conditions, and the maximum of finitely many amplitude bounds is finite. It is therefore enough to work with affine \(X\).

First let \(a:S\to U=X\setminus f^{-1}(0)\) be a smooth locally closed stratum with a local system \(L\), and put \(Y=\overline S\subset X\). We may take \(S\) connected: its finitely many components give a finite direct sum of the same generators. A connected smooth variety is irreducible, as proved in I.4, so \(Y\) is irreducible. Because \(S\) is locally closed in \(X\), it is dense open in \(Y\); its smoothness makes it part of the smooth locus of \(Y\). The resolution input supplies a projective \(Y_1\to Y\), with \(Y_1\) smooth and an isomorphism over \(S\). On \(Y_1\), let \(J\) be the ideal of the inverse image of \(Y\setminus S\). Principalize \(J\cdot(f)\). This ideal is nonzero on every component: each component meets the dense inverse image of \(S\), where both factors are units. The resulting projective map

\[
\pi:\widetilde Y\longrightarrow Y\hookrightarrow X
\tag{G.10}
\]

is an isomorphism over \(S\); its complement \(D=\widetilde Y\setminus S\) has simple normal crossings, and contains the zero fibre of \(g=f\pi\).

The principalized ideal also gives the asserted monomial form of \(g\). At a point, its local generator is a unit times a monomial in the boundary parameters. Since the ideal is \(g\) times another ideal, this generator equals \(g h\) for a local element \(h\). Each boundary parameter is prime: its quotient local ring is regular local and a domain. Repeatedly divide \(g\) or \(h\) by each boundary prime in the monomial. At the end their product is a unit, so the remaining factor of \(g\) is a unit. Thus \(g=u\prod z_i^{m_i}\). Algebraic smooth coordinates give holomorphic coordinates by their invertible complex Jacobian. The map (G.10) is proper in the classical topology: locally it factors as a closed inclusion in \(Y\times\mathbb P^N\), and projective space is compact.

Let \(b:S\hookrightarrow\widetilde Y\setminus g^{-1}(0)\). Composition of derived direct images gives \(Ra_*L=R\pi_{U*}Rb_*L\). Proposition G.2 identifies its nearby complex with

\[
R\psi_f(Ra_*L)
\simeq R\pi_{0*}R\psi_g(Rb_*L).
\tag{G.11}
\]

The inner complex is bounded algebraically constructible by G.3. The outer proper image is bounded algebraically constructible by [Lesson 1, K.8](constructible-complexes-on-algebraic-varieties.md#k-8-constructibility-of-the-classical-operations), using its actual compatible-stratification and compact-fibre proofs. This proves the assertion for these direct-image generators.

Here is the finite reduction to them. For a constructible sheaf \(F\) on \(U\), let \(Y\) be the reduced closure in \(X\) of its support. Choose a disjoint union \(S\) of smooth dense opens in the irreducible components of \(Y\), avoiding their intersections and \(f^{-1}(0)\), on which \(F\) is a local system. With \(a:S\to U\), use the adjunction map

\[
F\longrightarrow Ra_*a^*F.
\tag{G.12}
\]

Its cone is bounded constructible by the ordinary-image theorem of Lesson 1, K.8. It restricts to zero on \(S\), and both terms are supported on \(Y\cap U\). Hence every cohomology sheaf of the cone has support closure contained in the proper closed subset \(Y\setminus S\), of strictly smaller dimension on each component. Induction on that dimension, together with the finitely many ordinary truncation triangles of the cone, proves the assertion for \(F\). At dimension zero, the closed support is disjoint from the zero fibre, so the nearby complex is zero. Empty support gives the same starting case. The finitely many ordinary truncation triangles of a general bounded constructible input complete the argument. No nonproper direct-image stalk was replaced by the cohomology of its geometric fibre.

Finally, ordinary restriction to the zero fibre is bounded constructible by Lesson 1, K.8. Taking the cone of its actual specialization map to nearby cycles preserves that category. This proves the vanishing-cycle assertion. \(\square\)

The proof of G.4 uses algebraic resolution in characteristic zero. An unrestricted holomorphic analogue requires its analytic resolution or analytic specialization inputs. Neither G.4 nor the bound (G.8) proves the affine/Stein perverse vanishing theorem of Lesson 5, nor an arithmetic nearby-cycle finiteness theorem over a trait.

## Appendix H. Blow-up charts, projectivity and boundary factors

The geometric reduction in G.4 uses blow-ups of finite-type ideals on smooth complex varieties. The following arguments give the chart, properness and boundary-ideal properties of those maps. The finite order-reduction and gluing argument is given in Appendix I.

### H.1. The chart and strict-transform algebras

Let \(A\) be a ring and \(I=(a_0,\ldots,a_r)\). The Rees algebra is the graded subalgebra \(A[IT]\subset A[T]\), with \(T\) of degree one. Its Proj has standard charts

\[
R_i=(A[IT]_{a_iT})_0=A[I/a_i]\subset A_{a_i}.
\tag{H.1}
\]

Indeed, the degree-zero fraction \(uT^n/(a_iT)^n\), with \(u\in I^n\), maps to \(u/a_i^n\). If this fraction vanishes, some power of \(a_i\) kills \(u\), which is exactly the vanishing criterion in the graded localization. The map is therefore injective, and its image is generated by the ratios \(a_j/a_i\). The overlaps invert \(a_j/a_i\); the transition maps are the corresponding fraction identities. The chart construction and its gluing are the ones proved in Proj of a graded ring, Sections 1–2.

On this chart \(IR_i=a_iR_i\), and multiplication by \(a_i\) is injective because \(R_i\subset A_{a_i}\). Thus the inverse image of the centre is an effective Cartier divisor. Outside the centre, \(I\) is the unit ideal and the blow-up is the identity. If \(A\) is reduced, every \(R_i\) is reduced. If \(I=(a)\) with \(a\) a nonzerodivisor, its single chart is \(A\), so blowing up this Cartier divisor is also the identity. The centre and its exceptional divisor must still be retained in the transform of an ideal.

For an arbitrary ring map \(A\to C\), put \(J=IC\) and let \(\alpha_i\) be the image of \(a_i\). On the total-transform chart there is a surjection

\[
C\otimes_A R_i\longrightarrow C[J/\alpha_i]\subset C_{\alpha_i}.
\tag{H.2}
\]

Surjectivity follows by expressing elements of \(J\) as \(C\)-linear combinations of the images of the \(a_j\). After inverting \(\alpha_i\), both sides become \(C_{\alpha_i}\). Consequently the kernel is exactly the \(\alpha_i\)-power torsion. Removing that torsion is the schematic closure of the complement of the exceptional divisor: its defining ideal is the kernel of the map to the localization. Hence the strict transform of \(\operatorname{Spec}C\) is its blow-up along \(J\). The ratio maps agree on overlaps, so this assertion glues for closed subschemes and, more generally, for any scheme over \(\operatorname{Spec}A\). This also proves reducedness of the strict transform of a reduced scheme.

If \(C\) is flat over \(A\), tensoring \(I^n\hookrightarrow A\) remains injective and has image \(J^n\). Thus the entire base-changed Rees algebra is \(C[JT]\). Localization and taking degree zero identify its charts with the flat base changes of (H.1), proving flat base change for blow-ups. These arguments also appear in Blowing up, Sections 1–5.

For a smooth centre given in smooth coordinates by \(z_1=\cdots=z_c=0\), the \(z_j\)-chart is

\[
z_j=t,\qquad z_i=t u_i\quad(1\le i\le c,\ i\ne j),
\qquad z_i=z_i\quad(i>c).
\tag{H.3}
\]

For polynomial coordinates these are polynomial chart rings: substitution identifies the subring in (H.1) with the polynomial ring on \(t,u_i,z_i\). Smooth coordinates are étale over polynomial coordinates, so the flat-base-change calculation gives the same charts after the étale pullback. They are smooth, and the exceptional divisor is \(t=0\). A coordinate boundary component \(z_i=0\) with \(i\le c\) has strict transform \(u_i=0\) when \(i\ne j\), and has empty strict transform in the \(j=i\) chart. A boundary coordinate with \(i>c\) remains \(z_i=0\). Distinct retained components and the exceptional divisor are therefore distinct coordinate hyperplanes. This proves preservation of simple normal crossings for an adapted smooth centre, including the trivial Cartier blow-up when \(c=1\).

### H.2. A projective embedding for the composite

**Lemma H.1.** Let \(B\) be an affine complex variety. A finite sequence of blow-ups of coherent ideals starting with a scheme closed in \(B\times\mathbb P^N\) has a composite that admits a closed embedding in \(B\times\mathbb P^M\) for some finite \(M\). Its restriction to any closed strict transform is proper in the classical topology.

**Proof.** Suppose \(Y\subset B\times\mathbb P^N\) is closed, and let \(L\) be the restricted hyperplane line bundle. Its coordinate sections \(s_i\) have affine nonvanishing loci covering \(Y\). Let \(I\) be the coherent centre ideal. Choose finitely many module generators of \(I\) on each of these affine opens. The denominator-extension argument in Ample invertible sheaves, Lemma 2.1 extends each such generator after multiplication by a power of \(s_i\) to a global section of \(I\otimes L^{d_i}\). That argument uses a finite affine cover to clear denominators, then a finite cover of the overlaps to annihilate the differences by a further power; thus the extensions agree as sheaf sections. The scheme \(Y\) is quasi-compact and separated, so both finite-cover steps apply.

Take one exponent \(d\) at least all the finitely many exponents, multiplying each numerator by the appropriate power of its \(s_i\). The resulting finite global sections \(q_0,\ldots,q_r\) generate \(I\otimes L^d\): on the \(s_i\)-open their quotients by \(s_i^d\) include the chosen generators. They give a surjection of graded algebras

\[
\mathcal O_Y[Q_0,\ldots,Q_r]
\longrightarrow\bigoplus_{n\ge0} I^n\otimes L^{dn}.
\tag{H.4}
\]

The Proj on the right is canonically the blow-up along \(I\). Locally trivializing \(L\) gives its Rees algebra; changing the frame multiplies degree \(n\) by the \(n\)-th power of a unit, which cancels from every degree-zero chart fraction. The identifications therefore agree on overlaps. The surjection (H.4) is a closed immersion on each Proj chart, and gives

\[
\operatorname{Bl}_IY\hookrightarrow Y\times\mathbb P^r
\hookrightarrow B\times\mathbb P^N\times\mathbb P^r.
\tag{H.5}
\]

The Segre map embeds the last two projective factors closedly in \(\mathbb P^{(N+1)(r+1)-1}\). Explicitly its coordinates are \(W_{ij}=X_iQ_j\); its equations are the two-by-two minors. On the chart \(W_{ij}\ne0\), these equations express every ratio as
\(W_{kl}/W_{ij}=(W_{kj}/W_{ij})(W_{il}/W_{ij})\). The remaining row and column ratios are free coordinates, giving exactly the product of the two affine projective charts. These identifications agree on overlaps and prove the closed-immersion assertion, including its scheme structure. This is also the Segre calculation in Projective space and relative Proj, Section 2.

Applying this construction at each of the finitely many steps proves the asserted embedding for the composite. A closed strict transform stays closed in the resulting projective space. After analytification it is a closed subspace of \(B(\mathbb C)\times\mathbb P^M(\mathbb C)\). Complex projective space is compact: it is the continuous image of the compact unit sphere in \(\mathbb C^{M+1}\). For a compact subset \(K\subset B(\mathbb C)\), its inverse image is closed in the compact space \(K\times\mathbb P^M(\mathbb C)\), hence compact. This proves classical properness directly. \(\square\)

In particular, begin with the identity embedding of an affine ambient variety in its product with \(\mathbb P^0\). Every finite ambient blow-up sequence and every closed strict transform in it has the projectivity and classical properness required in G.4. Composing with a closed inclusion of the original affine variety preserves this property.

### H.3. Extracting the boundary monomial

Let \(R\) be the regular local ring at a point of a smooth complex variety, and let \(x_1,\ldots,x_r\) be the boundary parameters of a simple-normal-crossing divisor. Each \((x_i)\) is prime: the parameter quotient is regular local and a domain, by Regular local rings, Theorem 1.1 and Corollary 1.2. Distinct parameters do not divide one another, since their images are independent in the cotangent space.

For every \(a\ge0\),

\[
R\cap x_i^aR_{(x_i)}=x_i^aR,
\qquad
\bigcap_{i=1}^r(x_i^{a_i})=
\left(\prod_{i=1}^r x_i^{a_i}\right).
\tag{H.6}
\]

For the first equality, membership in the left side gives \(sf=x_i^a g\) for some \(s\notin(x_i)\). Primality first forces \(x_i\mid f\), and repeating after cancellation proves divisibility by \(x_i^a\). For the second, divide by the powers of one parameter at a time. A different prime parameter cannot divide the powers already removed, so its required divisibility persists. The reverse inclusion is immediate. No factorization theorem for arbitrary elements of \(R\) is needed.

For a nonzero finite ideal \(I\), let \(a_i\) be its order at the generic point of the boundary component \(x_i=0\). The first equality of (H.6) says that every element of \(I\) is divisible by \(x_i^{a_i}\) already in \(R\). The second gives

\[
I=M N,\qquad M=\left(\prod_i x_i^{a_i}\right),
\tag{H.7}
\]

where \(N\subset R\) is an ideal and has order zero along every boundary component. To see the latter, a finite generating list for \(I\) attains the minimum order \(a_i\); the other boundary parameters are units at that generic point. The quotients in (H.7) glue, because replacing a boundary equation by a unit multiple changes its product by a unit. Thus (H.7) gives the monomial and residual ideal sheaves used in marked order reduction.

Let a smooth adapted centre have generic order \(e\) for \(N\), and let \(F\) be its exceptional divisor. Work on one connected component of the centre; the argument applies separately to the others. The unmarked transform \(N'=\mathcal O(eF)\pi^*N\) is an ideal and has order zero along \(F\). For the last assertion, the nonzero initial form of degree \(e\) at the generic point of the centre becomes a nonzero polynomial on each affine exceptional chart after division by its exceptional equation to degree \(e\). The homogeneous degree fixes the omitted exponent, so dehomogenizing that form cannot make it zero. Integrality and divisibility are also the explicit assertions of Smooth blow-ups and transforms, Lemma 4.1.

At the generic point of each retained strict boundary component the blow-up is an isomorphism, so \(N'\) has order zero there too. For an admissible marking \(m\), the transformed ideal consequently has the factorization

\[
\mathcal O(mF)\pi^*I
=\bigl(\mathcal O((m-e)F)\pi^*M\bigr)N'.
\tag{H.8}
\]

The first factor is an ideal: if \(b\) is the order of \(M\) along the centre, its exceptional exponent is \(b+e-m\ge0\) by admissibility, and its other exponents are the nonnegative strict-boundary exponents. It is therefore precisely the new boundary monomial, and \(N'\) is precisely the residual ideal. This proves the transform rule without an additional local factoriality input.

## Appendix I. Resolution for the algebraic nearby-cycle argument

The reduction in G.4 needs a smooth modification of an affine variety and a normal-crossing boundary on that modification. We construct these maps over \(\mathbb C\). At each inductive stage the smooth ambient schemes have one fixed dimension, and the changes of charts are étale. A finite disjoint union of charts is treated as one scheme by the order-reduction construction. Its centres are not obtained by aligning independently shortened sequences on its components.

### I.1. Coordinates and descent from completion

Let \(p\) be a closed point of a smooth complex variety of dimension \(n\). Functions \(x_1,\ldots,x_n\) vanishing at \(p\), whose differentials form a basis at \(p\), define an étale map to \(\mathbb A^n\) on a neighbourhood of \(p\). Here is the presentation argument. In a standard smooth presentation with variables \(u_1,\ldots,u_{n+c}\) and relations \(F_1,\ldots,F_c\), the rows \(dF_j\) span the conormal space. The rows \(dx_i\) give a basis of its quotient. Consequently the square matrix with rows \(dF_j,dx_i\) has nonzero determinant at \(p\). Over the target ring \(\mathbb C[t_1,\ldots,t_n]\), the equations are \(F_j=0\) and \(x_i-t_i=0\). Inverting that determinant gives a square Jacobian presentation. Across a square-zero ideal, multiplication by its inverse corrects the equation errors uniquely; iteration gives the formally étale lifting property. Finite presentation makes the morphism étale. The standard presentations used here are proved in Formally smooth, unramified and étale ring maps, Sections 4–5.

The completed local ring is \(\mathbb C[[x_1,\ldots,x_n]]\). Indeed, the parameters generate each successive quotient of the maximal-ideal filtration, giving a surjection from this power-series ring to the completion. The associated graded ring of a regular local ring is the polynomial ring on the parameter classes, so the least nonzero homogeneous term of a putative kernel element cannot vanish. This proves injectivity. The associated-graded assertion and preservation of regularity under completion are proved in Regular local rings, Sections 1–3 and Completion, Sections 3–4. An invertible change of the linear parameter terms induces an isomorphism of completions: solve for the inverse one homogeneous degree at a time and take the limit.

We will use three further properties with their actual algebraic proofs. Étale morphisms are flat and open, and their diagonals are open immersions; [Lesson 1, AW.1](constructible-complexes-on-algebraic-varieties.md#aw-1-the-algebra-used-at-one-point) proves these from monic neighbourhoods, free-module localization, the characteristic polynomial of multiplication, and the idempotent diagonal ideal. Coordinate derivations pull back to the derivations dual to the pulled-back coordinate differentials. The product rule then shows that derivative ideals commute with étale pullback. Finite coherent-module equalities descend from a completed local ring: completion is faithfully flat by the cited completion lesson, so a quotient that becomes zero was already zero at the point. A finite list of generators then makes it zero on a neighbourhood. Finally, compatible finite ideals on an open cover glue to a coherent ideal, by the module and closed-immersion constructions in Affine schemes, Sections 2–3 and Schemes, gluing and immersions, Sections 2–3.

### I.2. Comparing local choices without changing the centres

For an ideal \(J\) of maximal order \(w>0\), write \(D^aJ\) for the ideal generated by derivatives of order at most \(a\), and \(B=D^{w-1}J\). A maximal-contact hypersurface has a smooth local equation in \(B\). Its strict transforms contain every admissible centre and the successive order-\(w\) loci, by the derivative-transform inclusion and Hypersurfaces of maximal contact, Theorem 2.3. Suppose that \(J\) satisfies

\[
B\,DJ\subseteq J.
\tag{I.1}
\]

At a closed point of the order-\(w\) locus, two maximal-contact equations \(h,h'\) can be completed to parameter systems \((h,x_2,\ldots,x_n)\) and \((h',x_2,\ldots,x_n)\) with the same remaining parameters. If both hypersurfaces are transverse to a prescribed normal-crossing boundary, include its local equations among those remaining parameters. To choose the rest, the nonvanishing of each of the two basis determinants is an open condition on a matrix of coefficients. Their product is a nonzero polynomial, so over the infinite field \(\mathbb C\) there is a simultaneous choice.

In the completion, the substitution \(h'\mapsto h\), \(x_i\mapsto x_i\) preserves \(J\). To verify this, (I.1) implies \(B^aD^aJ\subseteq J\) for every \(a\): differentiate a product of \(a\) elements of \(B\) and an element of \(D^aJ\), and apply (I.1) and induction to its product-rule terms. Taylor expansion of a substitution whose parameter differences belong to \(B\) therefore sends \(J\) into \(J\). The Taylor sums converge in the maximal-ideal topology; ideals of the Noetherian complete local ring are closed, by the exactness and separatedness statements of the completion lesson. If \(\sigma(J)\subseteq J\), the ascending chain \(J\subseteq\sigma^{-1}J\subseteq\cdots\) stabilizes, so applying a power of \(\sigma\) gives equality. Moreover \(f-\sigma(f)\in B\) for every formal function \(f\), by the same Taylor expansion.

This substitution is realized by an algebraic neighbourhood. Let \(x=(h,x_2,\ldots,x_n)\), \(x'=(h',x_2,\ldots,x_n)\), and form

\[
V=X\mathbin{\times_{\mathbb A^n}}X,
\qquad x\text{ on the first factor},\quad x'\text{ on the second}.
\tag{I.2}
\]

Both projections \(v,v':V\to X\) are étale near \((p,p)\). Their completed maps are isomorphisms, and their composite is the substitution above. Equality of the completed pullback ideals descends by I.1. The boundary equations and \(v^*h=v'^*h'\) agree already on \(V\). The ideal generated by \(v^*f-v'^*f\), for a finite list of local algebra generators, is contained in \(v^*B\) after completion and hence on a smaller neighbourhood. Thus, there,

\[
v^*J=v'^*J,
\qquad v|_{V(v^*B)}=v'|_{V(v^*B)}.
\tag{I.3}
\]

The images of these neighbourhoods are open. They cover every closed point of the order-\(w\) locus, hence the entire locus: a nonempty closed subset of a finite-type complex scheme has a closed point. Quasi-compactness gives finitely many neighbourhoods, whose disjoint union has both projection images containing that locus.

Here is why these comparisons determine the actual sequence, rather than just its final space. Suppose two order-\(w\) sequences become the same sequence under \(v\) and \(v'\). Let \(B_i\) be the controlled transform of \((B,1)\). The derivative-transform inclusion puts every common centre inside \(V(B_i)\). Inductively assume that the preceding centres agree and that the two lifted maps agree on \(V(B_i)\). Their images of the common next centre are equal; the centre is smooth and reduced, and both maps cover it. Thus the next centres are the same closed subscheme.

The agreement persists after that blow-up. In adapted coordinates the centre is \((z_1,\ldots,z_c)\). Write the differences between the two pulled-back coordinates as \(b_l\in B_i\). On a common blow-up chart with exceptional equation \(g=v^*z_k\), write \(b_l=g b'_l\), where \(b'_l\in B_{i+1}\). Along \(V(B_{i+1})\), \(1-b'_k\) is a unit and \(v'^*z_k=g(1-b'_k)\), so the second map uses the same chart. For \(y_l=z_l/z_k\), \(l\le c\), \(l\ne k\), the difference is

\[
v^*y_l-v'^*y_l
=\frac{b'_l-b'_k v^*y_l}{1-b'_k}\in B_{i+1}.
\tag{I.4}
\]

For the remaining coordinates it is \(g b'_l\in B_{i+1}\). On the exceptional fibre the base point and the fibre coordinates consequently agree. Near that common image the coordinate differences generate the diagonal ideal, since the coordinate map is étale and its diagonal is open. This proves equality of the maps on \(V(B_{i+1})\). Induction proves equality of every centre. Surjectivity over the original cosupport means that none of these centres disappears under either comparison. This is the centre calculation of Uniqueness of maximal contact, Theorem 4.1.

For open gluing, choose finitely many charts \(U_\alpha\) carrying a maximal-contact hypersurface and run the local construction on \(U'=\coprod_\alpha U_\alpha\). On \(U''=U'\times_XU'\), the two projections onto \(U'\) are surjective local isomorphisms. Functoriality gives the same sequence on \(U''\), with no deleted step under either projection. At each index the centre ideals agree on the overlaps and glue by I.1. Blow up the glued ideal; H.1 identifies its flat pullbacks with the prescribed chart blow-ups. The transformed ideals and boundary divisors agree too. Induction through the finite sequence gives the global sequence. A common refinement proves independence of the chosen cover. This argument uses synchronized indices on the surjective cover, as in Blow-up sequences, Theorem 5.1.

### I.3. Finite order reduction in a fixed dimension

We use the order of a nonzero ideal in a regular local ring and an ordered normal-crossing boundary. A marked transform with marking \(m\) is \(\mathcal O(mF)\pi^*J\), where the centre has order at least \(m\); the marking stays fixed. H.1 proves the smooth chart and boundary properties, and H.3 proves the monomial/residual factorization and its transform rule. The Taylor criterion, upper semicontinuity of order, and preservation of the maximum under a blow-up of that maximum are proved in Smooth blow-ups and transforms, Sections 2 and 4. These make the maximal order finite and the order loci closed.

The induction is simultaneous: marked order reduction in dimensions below \(n\) gives ordinary order reduction at the maximum in dimension \(n\); the latter gives marked order reduction in dimension \(n\). Dimension zero starts with the unit ideal. All schemes compared by the functoriality used in this induction have the same dimension. In particular, inverse images of hypersurfaces under the étale comparisons have dimension \(n-1\).

For the ordinary step, Tuning of ideals, Corollary 2.2 replaces \((J,m)\) by a derivative-generated ideal \((W,w)\) with the same admissible sequences and end cosupports. It satisfies (I.1) and the inequalities \((D^aW)^w\subseteq W^{w-a}\), \(0\le a<w\). The weighted-product proof there establishes these assertions for the initial tuned ideal; they need not persist under every transform. Logarithmic derivatives and going up, Theorem 4.1 instead proves that a sequence for its restriction to a smooth hypersurface lifts, with the same marking, to the ambient scheme. Its derivative-transform formula supplies the needed assertion along the entire sequence.

Apply this first to each old boundary member. Remove its components contained in the order-\(w\) locus by a Cartier blow-up; locally \(W\) is their equation to power \(w\), so its controlled transform becomes the unit ideal there. On the remaining boundary member the restriction is nonzero on every component. Lower-dimensional marked reduction, followed by going up, makes the cosupport disjoint from its strict transform. There are finitely many old members. Their treatment leaves the strict transform of any initial maximal-contact hypersurface transverse to the new boundary near the remaining cosupport: each new centre lies in that hypersurface and is adapted to the previous boundary, so the coordinate charts of H.1 preserve this transversality. Old members are absent near that cosupport.

Retune the resulting ideal there and apply the same hypersurface procedure with this strict maximal-contact hypersurface as the distinguished boundary member. At the end, its strict transform is disjoint from the cosupport. Maximal contact also forces it to contain the cosupport for as long as the maximum stays \(m\). Thus the order drops below \(m\). I.2 makes this finite sequence independent of the choice of hypersurface and glues it over the ambient scheme. The full construction, including extension of its centres from the neighbourhood of the closed cosupport, is Order reduction for ideals, Lemma 2.1 and Theorem 3.1. Each lower-dimensional invocation terminates by induction; the boundary loop is finite.

For a marked ideal \((J,m)\), write \(J=MN\) as in H.3. While \(\max\operatorname{ord}N=e\ge m\), use ordinary order reduction at \(e\). H.3 shows that its ordinary transforms are precisely the residual parts of the marked transforms of \(J\). Each round strictly lowers the nonnegative integer \(e\). Next, for \(t=m-1,\ldots,1\), apply ordinary order reduction with marking \(mt\) to

\[
K_t=N^m+J^t.
\tag{I.5}
\]

At the start of that round, \(\operatorname{ord}N\le t\) on the order-\(m\) locus of \(J\). Outside it, \(\operatorname{ord}J<m\); hence \(\max\operatorname{ord}K_t\le mt\) everywhere. Its maximum locus is the intersection of the order-\(t\) locus of \(N\) and the order-\(m\) locus of \(J\). The transform formula H.3 identifies the transforms of (I.5) with the same expression in the new ideals. Thus this round lowers the order of \(N\) below \(t\) on the cosupport of \(J\). After finitely many rounds, \(N\) is a unit near that cosupport, so the remaining ideal is monomial.

For that last case, process intersections of \(r=1,\ldots,n\) boundary components. When all smaller intersections have exponent sum less than \(m\), choose the largest sum \(\mu\ge m\) on an \(r\)-fold intersection and the least boundary index tuple attaining it. Blow up the disjoint union of all intersections with that tuple and sum. The new exceptional exponent is \(\mu-m\). A new \(r\)-fold intersection containing it has sum less than \(\mu\), since its other \(r-1\) exponents have sum less than \(m\). Smaller intersections keep sum less than \(m\): split the old \(r\) centre components into the ones retained at the new point and the ones omitted; the new sum plus \(m\) is a sum of two old intersection sums, each involving fewer than \(r\) components. Both are less than \(m\). The explicit split and chart calculation are given in Order reduction for marked ideals, Theorem 2.1, Step 3. Thus the pair consisting of \(\mu\) and the number of tuples attaining it decreases lexicographically. It is a pair of nonnegative integers, so each phase terminates. This completes the dimension induction.

The procedure just described is defined on disconnected equidimensional schemes using the maxima and ordered boundary data on the whole scheme. Under an étale map the orders, boundary exponents and restriction problems pull back unchanged. A round at a larger maximum that misses the image pulls back to empty centres and changes none of the data on the image. The remaining rounds therefore occur in the same order. The same argument applies to the maximum exponent sum and its least tuple. Inserting empty boundary members changes no component or comparison of nonempty index tuples, so it changes no centre. These observations prove the étale compatibility used in I.2 throughout the induction; they do not require an assertion about aligning sequences in different dimensions.

### I.4. The required projective modifications

**Theorem I.1.** A reduced irreducible affine complex variety \(Y\) has a projective morphism \(Y_1\to Y\) with \(Y_1\) smooth, which is an isomorphism over \(Y^{\mathrm{sm}}\). If \(V\) is a smooth variety projective over an affine complex variety and \(J\) is a coherent ideal nonzero on every component, a finite sequence of smooth blow-ups makes its total transform invertible with normal-crossing support and is an isomorphism over \(V\setminus V(J)\). The final variety is still projective over the affine base. These morphisms are proper for the classical topology.

**Proof.** On each equidimensional open-and-closed part of \(V\), apply I.3 with marking one and initially empty boundary. There are finitely many such parts; concatenate their finite sequences, extending each centre by the empty set on the other parts. This constructs the required modification without a functoriality assertion for this concatenation. At the end the controlled transform is the unit ideal. If the exceptional divisors at the successive steps are \(F_{i+1}\), pulling the identities \(\pi_i^*J_i=\mathcal O(-F_{i+1})J_{i+1}\) to the last variety gives

\[
\Pi^*J=\mathcal O\left(-\sum_i\Pi_{r,i+1}^*F_{i+1}\right).
\tag{I.6}
\]

Its support is contained in the normal-crossing total boundary. Every centre lies over \(V(J)\), since the ideal and all its transforms are the unit ideal outside that inverse image. H.2 supplies a projective embedding over the affine base for the finite composite. It also proves classical properness by compactness of complex projective space. This proves the second assertion.

For the first, embed \(Y\) in \(P=\mathbb A^N\), increasing \(N\) by one if necessary so that \(Y\) contains no component of \(P\). Its smooth locus is nonempty and dense. Indeed, the fraction field of its affine domain has a separating transcendence basis in characteristic zero; a finite list of generators and the nonzero derivative of a primitive-element equation give a smooth presentation after localization. This is the separating-normalization argument of [Lesson 1, M.1](constructible-complexes-on-algebraic-varieties.md#m-1-preparations-fields-smooth-open-subsets-and-bounds), together with the Jacobian presentation in I.1. The Jacobian minors also make the smooth locus open.

Run marking-one principalization on the ideal of \(Y\) in \(P\). Over \(P^0=P\setminus\operatorname{Sing}Y\), the ideal is that of the smooth closed subscheme \(Y^{\mathrm{sm}}\). The construction for the ideal of a smooth subscheme of constant codimension consists of its single blow-up. To see this directly, choose adapted coordinates \(S=V(z_1,\ldots,z_c)\). In the smooth subspace \(V(z_2,\ldots,z_c)\), the ideal of \(S\) is the principal ideal \((z_1)\). Its maximal-contact hypersurface is \(S\), and the Cartier step in I.3 makes its marking-one transform a unit after one blow-up. Moving up the chain of coordinate hypersurfaces preserves this sequence: for an ideal containing a hypersurface equation, its maximum is one, tuning leaves it unchanged, the old-boundary step is empty, and the maximal-contact step is exactly the pushed-forward marked sequence on that hypersurface. The chain has the same length on every chart of this constant-codimension embedding. Run the construction on their disjoint union and descend the single common centre as in I.2. Thus the global sequence is the single blow-up of \(S\).

Étale compatibility now shows that exactly one centre of the sequence on \(P\) meets the inverse image of \(P^0\); call its index \(j\). Earlier centres lie over \(\operatorname{Sing}Y\). Just before the \(j\)-th blow-up, the strict transform \(Y_j\) is the reduced closure of the copy of \(Y^{\mathrm{sm}}\), and that copy is an open subset of the smooth centre \(Z_j\). A smooth connected component is irreducible: regular local rings are domains, so distinct irreducible components cannot meet, and the finitely many components are open and closed. Hence this closure is a union of smooth components of \(Z_j\). H.1 proves that the strict transform is reduced, so equality of these closed sets is equality of reduced closed subschemes. In particular \(Y_j\) is smooth. The map \(Y_j\to Y\) is an isomorphism over \(Y^{\mathrm{sm}}\). H.2 gives its projective embedding over the affine \(Y\), and classical properness. Taking \(Y_1=Y_j\) proves the assertion. This is the distinguished-centre construction of Principalization and resolution, Proposition 4.3, with only the fixed-dimensional comparisons above. \(\square\)

For G.4, take each smooth stratum connected. There are finitely many connected components, and finite direct sums commute with all the direct-image and nearby-cycle constructions in that argument. Its closure \(Y\) is then irreducible, so Theorem I.1 supplies \(Y_1\to Y\). Apply its second assertion to the boundary ideal times \((f)\) on \(Y_1\). This gives exactly the map (G.10), with normal-crossing complement and the projectivity needed in (G.11). Thus both geometric inputs to G.4 hold at its stated algebraic scope.

## Geometric hypotheses and references

The disc equivalence uses the actual attaching and mapping-complex proofs in the earlier gluing lesson, Appendix B, and its intermediate-extension characterization. The classical general-function statements use Proposition F.1 for deck-cover descent and Appendix F.2–F.4 for the enhanced attaching and mapping-complex comparison on a closed fibre of any dimension. For regular functions on complex varieties with finite-dimensional algebraically constructible characteristic-zero field coefficients, G.4 and Lesson 5, Theorem A.3, supply bounded constructibility and the affine-open bound. The unrestricted holomorphic setting still requires its own constructibility and Stein-open input; its general ordinary/microlocal comparison is not proved here. The trait appendices require finite-presentation continuity, proper and smooth base change, the torsion affine bound, ordinary purity and duality, constructible finiteness, and normalized adic reduction and rationalization. Appendix E deduces the equality of the geometric localization and continuous-inertia trace pairings, including the negative Kummer boundary and its cancelling fibre-coordinate sign. Its proof still requires the exact ordinary enhanced localization, tensor and exceptional adjunctions, compactification, multiplicative continuous descent, divisor-oriented purity and normalized adic realization at the stated geometric scope. Full torsion sliced-topos duality is additional to the field-coefficient cone argument and is not supplied by its finite logarithms. The Riemann–Hilbert interpretation requires its own complete earlier provider. The general statements depending on these inputs are conditional at the scopes specified above.

Reich uses the sign \(1-t\); this lesson uses \(T-1\) in the variation and maximal-extension formulas. Constructibility of nearby cycles is a separate theorem. Section 5 uses bounded truncations and the splitting of idempotents in the ambient derived sheaf category, without assuming constructible injective resolutions.

- R. Reich, [*Notes on Beilinson's “How to glue perverse sheaves”*](https://arxiv.org/abs/1002.1686v4), arXiv version 4 (2010); free native text, especially the nearby-cycle preliminaries and the gluing and cone comparison sections.
- A. Beilinson, [*How to glue perverse sheaves*](https://people.mpim-bonn.mpg.de/gaitsgde/grad_2009/Beilinson%20--%20How%20to%20glue%20perverse%20sheaves.pdf), freely readable MPIM-hosted text (1987).
- A. Beilinson, J. Bernstein and P. Deligne, with contributions by O. Gabber, [*Faisceaux pervers*](https://publications.ias.edu/sites/default/files/Faisceaux%20pervers.pdf), freely readable IAS edition, Section 4.4.
- P. Deligne, [*Cohomologie étale*, SGA 4½](https://publications.ias.edu/node/378), author-hosted free edition; *Théorèmes de finitude*, §§3.1–3.6, printed pp. 244–247, for the finite-coefficient constructibility argument in Appendix A; *Cycle*, 2.1.1–2.1.3, printed pp. 138–139, for the divisor/Kummer boundary convention in Appendix E.
- L. Illusie, [*Autour du théorème de monodromie locale*](https://www.numdam.org/item/AST_1994__223__9_0/), freely readable Numdam edition, Astérisque 223 (1994), 9–57; §1.1, §3.6, Theorem 4.2, construction 4.3, Variant 4.4 and Corollaries 4.5–4.6, especially printed pp. 11–12, 36–37 and 45–51, for the group, dimension, evaluation/trace and augmentation comparisons in Appendices B and D.
- M. A. A. de Cataldo and L. Migliorini, [*The Decomposition Theorem and the topology of algebraic maps*](https://arxiv.org/abs/0712.0349v2), free arXiv version 2, Section 5.7.2.
- B. Bhatt, M. Blickle, G. Lyubeznik, A. K. Singh and W. Zhang, [*Applications of perverse sheaves in commutative algebra*](https://arxiv.org/abs/2308.03155), free arXiv text, Section 2 for the stated covariant Riemann–Hilbert comparison.
- Q. Lu and W. Zheng, [*Duality and nearby cycles over general bases*](https://arxiv.org/abs/1712.10216v7), free arXiv version 7 (2019), the subsections on the Iwasawa twist, its sheaf version, quasi-periodic adjunctions and duality, and the henselian-trait specialization/variation comparisons. Appendix C supplies the coefficient and group-algebra constructions; Appendix E supplies the dual-cone algebra and a localization, Kummer-sign and exceptional-trace deduction of the geometric pairing comparison, under explicit ordinary and adic foundations.
