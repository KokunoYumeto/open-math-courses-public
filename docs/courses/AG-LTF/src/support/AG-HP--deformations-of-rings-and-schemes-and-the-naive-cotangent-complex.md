# Deformations of rings and schemes and the naive cotangent complex

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

An infinitesimal change of an equation can disappear after an infinitesimal change of coordinates. The naive cotangent complex keeps both operations in one object: its degree \(-1\) term records relations, and its degree zero term records coordinates. Applying \(\operatorname{Hom}(-,M)\) turns the differential into the operation that changes a relation by a derivation.

We prove independence of the chosen presentation, classify square-zero extensions, and compute the tangent spaces of hypersurface and complete-intersection deformations. For smooth schemes, the local algebra has no deformation parameters. The parameters and obstructions instead arise from gluing, in \(H^1(T_X)\) and \(H^2(T_X)\). We give that gluing argument without a properness assumption.

All rings are commutative with identity. Complexes use **cohomological degrees**: the relation term has degree \(-1\), and the differential raises degree. Thus \(H^{-1}\) here is the module denoted \(H_1\) in the homological notation of the Stacks project. Derived \(\operatorname{Ext}^i(K,M)\) means \(\operatorname{Hom}_{D(B)}(K,M[i])\). An isolated-singularity hypothesis is needed for finiteness of certain tangent spaces, rather than for the Jacobian formula itself.

## 1 A presentation and its two-term complex

Choose a polynomial presentation

\[
P=A[x_1,\ldots,x_n]\twoheadrightarrow B,
\qquad I=\ker(P\to B).
\]

The **naive cotangent complex** associated to it is

\[
\operatorname{NL}_{B/A}=
\left[ I/I^2\xrightarrow{d}
\Omega_{P/A}\otimes_P B\right],
\qquad d(\overline f)=df\otimes1.
\tag{1.1}
\]

The differential is well-defined because \(d(fg)=f\,dg+g\,df\) vanishes after tensoring with \(B\) when \(f,g\in I\). The right-hand term is the free module with basis \(dx_i\). The usual universal property of differentials gives

\[
H^0(\operatorname{NL}_{B/A})=\Omega_{B/A}.
\tag{1.2}
\]

Indeed a linear map from the cokernel in (1.1) to a \(B\)-module \(M\) is a derivation \(P\to M\) vanishing on \(I\), which is exactly an \(A\)-derivation \(B\to M\). This also proves

\[
\operatorname{Der}_A(B,M)
=\operatorname{Hom}_B(H^0(\operatorname{NL}_{B/A}),M).
\tag{1.3}
\]

The same definition works with any set of polynomial variables; each polynomial still uses finitely many. Finite presentation allows a finite set of variables and a finitely generated relation ideal, but is unnecessary for the comparison argument that follows.

**Theorem 1.1 (presentation independence).** Two polynomial presentations of the same \(A\)-algebra give canonically identified objects in the homotopy category of complexes of \(B\)-modules. Comparison maps obtained by lifting generators are independent of those lifts up to chain homotopy. In particular the cohomology modules and derived Ext groups in this lesson do not depend on the presentation.

**Proof.** Let \(P\twoheadrightarrow B\) and \(Q\twoheadrightarrow B\) have kernels \(I,J\). Lift each polynomial generator of \(P\) to \(Q\); this gives an \(A\)-algebra map \(u:P\to Q\) inducing the identity on \(B\). It induces maps \(I/I^2\to J/J^2\) and \(\Omega_{P/A}\otimes B\to\Omega_{Q/A}\otimes B\), which commute with the differentials.

Suppose \(v\) is another lift. The map

\[
D:P\longrightarrow J/J^2,\qquad D(p)=u(p)-v(p)\pmod{J^2}
\]

is a derivation for the common \(P\)-action through \(B\). To check multiplication, expand

\[
u(pq)-v(pq)=u(p)(u(q)-v(q))+(u(p)-v(p))v(q).
\]

Modulo \(J^2\), both coefficients act by their images in \(B\). Also \(D(I^2)=0\). The universal property of differentials supplies a linear map

\[
h:\Omega_{P/A}\otimes B\longrightarrow J/J^2.
\]

On the relation term, \(u-v=h\,d\): evaluate on \(f\in I\). On the differential term, \(u-v=d\,h\): evaluate on \(dp\), obtaining \(d(u(p)-v(p))\). These are precisely the chain-homotopy identities. They also check the comparison maps explicitly, including their signs.

Choose a lift in the reverse direction. Both compositions lift the identity of the same presentation, so the preceding calculation makes them homotopic to the identity maps. The comparison maps are therefore homotopy equivalences. Compositions of algebra lifts induce compositions of chain maps, and their homotopy classes are independent of all choices. This proves the canonical identification and its functoriality. \(\square\)

A canonical representative can be obtained by taking a variable for every element of \(B\), mapping that variable to its named element. Finite presentations are usually easier for calculations. Theorem 1.1 explains why changing between them is legitimate.

## 2 What transitivity says for a two-term complex

For \(A\to B\to C\), choose presentations \(P=A[x]\twoheadrightarrow B\) and \(R=B[y]\twoheadrightarrow C\). Put \(Q=A[x,y]\), and denote the three relation ideals by

\[
I=\ker(P\to B),\quad K=\ker(Q\to C),\quad J=\ker(R\to C).
\]

There is a commutative diagram of modules with exact rows

\[
\begin{array}{ccccccccc}
0&\longrightarrow&\Omega_{P/A}\otimes C&\longrightarrow&
\Omega_{Q/A}\otimes C&\longrightarrow&\Omega_{R/B}\otimes C&\longrightarrow&0\\
&&\uparrow&&\uparrow&&\uparrow\\
&&I/I^2\otimes_B C&\longrightarrow&K/K^2&\longrightarrow&J/J^2&\longrightarrow&0.
\end{array}
\tag{2.1}
\]

The first arrow in the bottom row need not be injective.

**Proposition 2.1 (Jacobi–Zariski sequence).** The diagram gives the natural exact sequence

\[
\begin{split}
H^{-1}(\operatorname{NL}_{B/A}\otimes_B C)&\longrightarrow
H^{-1}(\operatorname{NL}_{C/A})\longrightarrow
H^{-1}(\operatorname{NL}_{C/B})\\
&\longrightarrow \Omega_{B/A}\otimes_B C
\longrightarrow\Omega_{C/A}\longrightarrow\Omega_{C/B}
\longrightarrow0.
\end{split}
\tag{2.2}
\]

The tensor product in its first term is the termwise tensor product of the displayed two-term model. If \(\operatorname{Tor}_1^B(\Omega_{B/A},C)\) and \(\operatorname{Tor}_2^B(\Omega_{B/A},C)\) vanish, that term is \(H^{-1}(\operatorname{NL}_{B/A})\otimes_B C\).

**Proof.** The top row in (2.1) splits by the bases \(dx_i,dy_j\). The map \(K\to J\) is onto, with kernel \(IQ\). Its induced map on conormal modules therefore has kernel \((IQ+K^2)/K^2\), which is the image of \(I/I^2\otimes_B C\). This proves the bottom-row exactness.

Let \(L=\operatorname{NL}_{C/A}\), \(N=\operatorname{NL}_{C/B}\), and let \(D=\ker(L\to N)\), taken termwise. Then

\[
0\longrightarrow D\longrightarrow L\longrightarrow N\longrightarrow0
\]

is a short exact sequence of complexes. The map \(U=\operatorname{NL}_{B/A}\otimes_B C\to D\) is onto in degree \(-1\) and an isomorphism in degree zero. Hence \(H^0(U)\to H^0(D)\) is an isomorphism and \(H^{-1}(U)\to H^{-1}(D)\) is onto: a lift of a degree \(-1\) cycle remains a cycle because the degree-zero map is an isomorphism. The long cohomology sequence for \(D,L,N\) now gives (2.2), with \(H^0(U)=\Omega_{B/A}\otimes C\).

The connecting map can be seen without the abstract sequence. Lift a relation cycle in \(J/J^2\) to \(K/K^2\). Its differential has zero \(dy\)-component, so lies in \(\Omega_{P/A}\otimes C\). Take its class modulo the differentials from \(I/I^2\otimes C\). Changing the lift changes it by such a differential. This gives the map to \(\Omega_{B/A}\otimes C\) in (2.2).

For the final assertion, write the original complex as \([N_1\to F]\), with \(F\) free, image \(Z\), cokernel \(\Omega=\Omega_{B/A}\), and kernel \(H\). From \(0\to Z\to F\to\Omega\to0\), the two Tor vanishings make \(Z\otimes C\to F\otimes C\) injective and \(\operatorname{Tor}_1^B(Z,C)=0\). Tensoring \(0\to H\to N_1\to Z\to0\) then shows that \(H\otimes C\) is the kernel of \(N_1\otimes C\to F\otimes C\). This is the asserted first-term identification. \(\square\)

The hypotheses on that identification matter. Termwise tensoring a complex does not generally commute with taking its kernel. More fundamentally, (2.1) is not in general a short exact sequence of the three naive complexes, nor a distinguished transitivity triangle involving only those two-term complexes.

For example take \(A=k\), \(B=k[x]/(x^2)\), \(C=k\). Then

\[
\operatorname{NL}_{B/k}\otimes_B k=[k\xrightarrow{0}k],\qquad
\operatorname{NL}_{k/k}\simeq0,\qquad
\operatorname{NL}_{k/B}\simeq k[1].
\tag{2.3}
\]

The first formula follows from \(d(x^2)=2x\,dx\); the last uses the presentation \(B\twoheadrightarrow k\). A triangle with these three entries would force \([k\to k][1]\simeq k[1]\), although its left side also has nonzero degree \(-2\) cohomology. This is impossible. The full cotangent complex restores transitivity by retaining the missing lower degrees; its construction is the subject of the final lesson.

## 3 Square-zero extensions are relation maps modulo derivations

Let \(M\) be a \(B\)-module. An element of \(\operatorname{Exal}_A(B,M)\) is an isomorphism class of sequences of \(A\)-algebras

\[
0\longrightarrow M\xrightarrow{\iota}E\longrightarrow B\longrightarrow0,
\tag{3.1}
\]

where \(M\) is a square-zero ideal with its specified \(B\)-action. Isomorphisms induce the identity on \(M\) and \(B\). The split extension \(B\oplus M\), with multiplication \((b,m)(c,n)=(bc,bn+cm)\), gives its zero element.

**Theorem 3.1.** For every finitely presented \(A\)-algebra \(B\), and every \(B\)-module \(M\), there is a natural isomorphism

\[
\operatorname{Exal}_A(B,M)
\simeq\operatorname{Ext}^1_B(\operatorname{NL}_{B/A},M).
\tag{3.2}
\]

In fact the construction works with unrestricted polynomial presentations. An extension's automorphisms inducing the identity on its two ends form \(\operatorname{Der}_A(B,M)\).

**Proof.** Choose \(P\twoheadrightarrow B\), with kernel \(I\), and lift its variables to \(E\). The resulting map \(P\to E\) sends \(I\) into \(M\), kills \(I^2\), and induces a \(B\)-linear map

\[
\phi:I/I^2\longrightarrow M.
\]

Changing the variable lifts changes the polynomial map by an \(A\)-derivation \(P\to M\). Thus it changes \(\phi\) by \(\delta d\), with \(\delta\in\operatorname{Hom}_B(\Omega_{P/A}\otimes B,M)\).

Conversely, given \(\phi\), form the ring \(P\oplus M\), where \(P\) acts on \(M\) through \(B\), and quotient by the graph ideal

\[
G_\phi=\{(i,-\phi(\overline i)):i\in I\}.
\tag{3.3}
\]

It is an ideal: multiplication by \((p,m)\) sends its element to \((pi,-p\phi(\overline i))\), since \(I\) annihilates \(M\), and \(\phi(\overline{pi})=\overline p\phi(\overline i)\). The ring \(E_\phi=(P\oplus M)/G_\phi\) maps onto \(B\), has kernel exactly \(M\), and has the multiplication required in (3.1). The chosen lifts of the variables recover \(\phi\).

If \(\psi=\phi+\delta d\), the map \((p,m)\mapsto(p,m-D(p))\), where \(D:P\to M\) is the derivation defined by \(\delta\), carries \(G_\phi\) to \(G_\psi\), and induces an isomorphism of extensions. Conversely an isomorphism of extensions compares their polynomial lifts; their difference is a derivation and gives exactly this relation between \(\phi,\psi\). We have therefore obtained

\[
\operatorname{Exal}_A(B,M)=
\operatorname{coker}\left(
\operatorname{Hom}_B(\Omega_{P/A}\otimes B,M)
\longrightarrow\operatorname{Hom}_B(I/I^2,M)\right).
\tag{3.4}
\]

Addition of relation maps corresponds to the Baer sum of extensions: take their fibre product over \(B\), whose kernel is \(M\oplus M\), and push it out by addition. Scalar multiplication is pushout by the corresponding endomorphism of \(M\). Thus (3.4) is an isomorphism of modules, with the claimed naturality.

It remains to identify this cokernel with derived Ext, rather than assume the relation module is projective. For any complex \(K=[N\to F]\) with \(F\) projective in degree zero, the triangle

\[
F[0]\longrightarrow K\longrightarrow N[1]\longrightarrow F[1]
\]

gives, on applying \(\operatorname{Hom}_{D(B)}(-,M[1])\),

\[
\operatorname{Hom}_B(F,M)\longrightarrow\operatorname{Hom}_B(N,M)
\longrightarrow\operatorname{Ext}^1_B(K,M)\longrightarrow0.
\]

The first map is precomposition with the differential. Apply this to (1.1). This proves (3.2) even when \(I/I^2\) is not projective. Theorem 1.1 gives presentation independence.

Finally an automorphism of (3.1) differs from the identity by a map \(E\to M\) vanishing on \(M\), hence by a map \(B\to M\). Multiplication says precisely that it is an \(A\)-derivation. Conversely \(1+\iota D\) defines such an automorphism, with inverse \(1-\iota D\). This proves the automorphism assertion. \(\square\)

The same calculation compares extensions along a map \(B\to C\) and a compatible module map \(M\to N\). Polynomial lifts give two relation maps into \(N\); their difference represents a class in \(\operatorname{Ext}^1_B(\operatorname{NL}_{B/A},N)\). A compatible extension map exists exactly when this difference class is zero, and its choices form a torsor under \(\operatorname{Der}_A(B,N)\). This follows by changing the polynomial lifts by a derivation, exactly as in (3.4).

## 4 Smoothness is the disappearance of local extension classes

**Proposition 4.1.** For a finitely presented \(A\)-algebra \(B\), the following are equivalent:

1. \(A\to B\) is smooth.
2. Every square-zero extension of \(B\) as an \(A\)-algebra splits.
3. \(\operatorname{Ext}^1_B(\operatorname{NL}_{B/A},M)=0\) for every \(B\)-module \(M\).
4. The relation differential \(I/I^2\to\Omega_{P/A}\otimes B\) is a split injection; equivalently the naive complex is homotopy equivalent to the finite projective module \(\Omega_{B/A}\) in degree zero.

**Proof.** Theorem 3.1 proves equivalence of 2 and 3. If 3 holds, (3.4), with \(M=I/I^2\), lifts the identity map of that module to a map from \(\Omega_{P/A}\otimes B\). This is a left inverse to the differential, giving 4. A split injection makes (3.4) zero for every \(M\), proving the converse. It also decomposes the complex into a contractible summand \([I/I^2\xrightarrow{1}I/I^2]\) and its finite projective cokernel in degree zero.

A smooth algebra is formally smooth [Stacks, Tag 00TN], so its identity map lifts across (3.1), giving a splitting. Conversely assume 2. For an \(A\)-algebra map \(B\to D/J\), with \(J^2=0\), pull back \(D\to D/J\) along it. The pullback is a square-zero extension of \(B\) by the \(B\)-module \(J\). A splitting gives the desired map \(B\to D\). Factoring a nilpotent quotient into square-zero quotients proves formal smoothness. Since \(B\) is finitely presented, [Stacks, Tag 00TN] makes it smooth. \(\square\)

In particular a smooth algebra has \(H^{-1}(\operatorname{NL})=0\), and locally its degree-zero cohomology is free. The converse needs more than the vanishing of \(H^{-1}\): projectivity of \(\Omega\) also matters. For instance, over a characteristic-zero field the cusp's relation differential is injective, but its differential module is not locally free at the cusp.

## 5 First-order algebra and module deformations

Write \(D=k[\epsilon]/(\epsilon^2)\). A marked first-order deformation of a \(k\)-algebra \(B\) is a flat \(D\)-algebra \(E\), with an identification \(E/\epsilon E=B\). Isomorphisms respect this identification.

A \(D\)-module \(V\) is flat exactly when

\[
\ker(\epsilon:V\to V)=\epsilon V.
\tag{5.1}
\]

Here is a direct verification. The necessity follows by tensoring the ideal sequence for \((\epsilon)\). For sufficiency, choose a \(k\)-basis of \(\epsilon V\) and lift its elements to vectors \(v_i\) with the prescribed \(\epsilon v_i\). Every vector of \(V\) is uniquely a finite sum of the \(v_i\) and \(\epsilon v_i\): first express its \(\epsilon\)-image, then use (5.1) on the remainder. These pairs give a free \(D\)-basis \(v_i\). This argument permits infinite bases.

Flatness identifies \(\epsilon E\) with \(B\), by \(b\mapsto\epsilon\widetilde b\). Thus \(E\) gives a square-zero extension of \(B\) by \(B\). Conversely any such extension becomes a \(D\)-algebra by sending \(\epsilon\) to the element of its kernel corresponding to \(1\in B\); multiplication gives (5.1). The two constructions are inverse. Theorem 3.1 therefore identifies the tangent space of marked algebra deformations as

\[
T^1_{B/k}=\operatorname{Ext}^1_B(\operatorname{NL}_{B/k},B).
\tag{5.2}
\]

The infinitesimal automorphisms are \(\operatorname{Der}_k(B,B)\). They affect uniqueness of higher-order parameters through the automorphism-lifting criterion of the preceding lesson.

There is a related module calculation, with the underlying algebra held fixed. For a \(B\)-module \(M\), marked \(D\)-flat deformations as modules over \(B\otimes_kD\) correspond to exact sequences of \(B\)-modules

\[
0\longrightarrow M\xrightarrow{i}M'\xrightarrow{p}M\longrightarrow0.
\]

Give an extension the \(\epsilon\)-action \(ip\). Its square is zero and its kernel and image are both \(iM\), so (5.1) proves flatness. Conversely a flat deformation supplies exactly this extension. Thus their classes are \(\operatorname{Ext}^1_B(M,M)\), by the Yoneda description of Ext, and their infinitesimal automorphisms are \(\operatorname{Hom}_B(M,M)\). The same argument works for quasi-coherent sheaves on a fixed \(k\)-scheme, interpreting Ext in the category of modules and imposing the indicated quasi-coherence. It is a different deformation problem from changing the structure sheaf itself.

## 6 Complete intersections and the Jacobian map

**Proposition 6.1.** Let \(P=k[x_1,\ldots,x_n]\) and let \(f_1,\ldots,f_c\) be a regular sequence. Put \(B=P/(f_1,\ldots,f_c)\). Then

\[
\operatorname{NL}_{B/k}=
\left[B^c\xrightarrow{J}B^n\right],
\qquad J(e_j)=\sum_i\frac{\partial f_j}{\partial x_i}\,dx_i,
\tag{6.1}
\]

and

\[
T^1_{B/k}=\operatorname{coker}\left(
B^n\longrightarrow B^c,\quad
(v_i)_i\longmapsto
\left(\sum_i v_i\frac{\partial f_j}{\partial x_i}\right)_j
\right).
\tag{6.2}
\]

Every marked first-order deformation is obtained by replacing the equations with \(f_j+\epsilon g_j\). With the relation-map convention of (3.3), its class is the image of \((-g_j)_j\) in (6.2).

**Proof.** First \(I/I^2\) is free on the classes of the \(f_j\). To see independence, suppose \(\sum a_jf_j\in I^2\). Subtract coefficients in \(I\) to make this sum zero. The syzygies of a regular sequence are generated by \(f_i e_j-f_j e_i\). An elementary induction proves this assertion: reduce the last coefficient of a syzygy modulo the preceding equations; nonzerodivisibility of the last equation makes that coefficient lie in their ideal. Subtract the indicated pair syzygies to kill it, and apply the induction hypothesis. Thus all the original \(a_j\) lie in \(I\), proving conormal independence. Differentiating the equations gives (6.1), and Theorem 3.1 gives its dual cokernel (6.2).

We verify that arbitrary first-order perturbations are flat. Let \(F_j=f_j+\epsilon g_j\) in \(D[x]\), and take their Koszul complex \(K(F)\). Its terms are free \(D\)-modules. Its subcomplex \(\epsilon K(F)\) and its quotient by that subcomplex are both the Koszul complex of the \(f_j\) over \(k\). That complex has no positive homology: this is the regular-sequence Koszul calculation, proved inductively by the mapping cone for adjoining a nonzerodivisor. The long homology sequence consequently gives

\[
0\longrightarrow B\longrightarrow D[x]/(F_1,\ldots,F_c)
\longrightarrow B\longrightarrow0,
\]

where the first map sends \(b\) to \(\epsilon\widetilde b\). Thus the quotient satisfies (5.1) and is flat.

Conversely lift the variables to a flat deformation \(E\), giving \(D[x]\twoheadrightarrow E\). Surjectivity follows from nilpotent Nakayama on its cokernel. Flatness makes reduction of its relation ideal equal to \(I\): tensor the exact kernel sequence with \(k\), using \(\operatorname{Tor}_1^D(E,k)=0\). Lift the \(f_j\) to generators \(F_j\) of that ideal. Their reductions generate, so nilpotent Nakayama on the ideal's quotient makes them generate the entire ideal. They have the indicated form.

In this quotient the chosen lift of \(f_j\) evaluates to \(-\epsilon g_j\), giving the stated minus sign. Changing the lifted coordinates by \(\epsilon v_i\) changes the relation map by the Jacobian image in (6.2). With fixed coordinate lifts, two choices of lifted equations differ by \(\epsilon h_j\) with \(h_j\in I\): flatness identifies the coefficient of \(\epsilon\) in their common quotient with \(B\). Thus that difference is zero in \(B^c\). The extension classification proves that these are exactly the changes preserving a marked deformation class. This proves the last assertion as well. \(\square\)

For a single nonzero polynomial \(f\), no isolated-singularity assumption is needed to obtain

\[
T^1_{P/(f)/k}=P/(f,f_{x_1},\ldots,f_{x_n}).
\tag{6.3}
\]

Localizing the presentation gives the corresponding local formula. Over a perfect field its support is the nonsmooth locus by the Jacobian criterion. When that locus consists of finitely many points, the module has finite length; it need not have finite length otherwise. Formula (6.3) is often called the **Tjurina algebra**. The equation \(f\) remains in its ideal: quotienting only by the derivatives computes a different algebra.

For the node \(f=xy\), the derivatives are \(y,x\), so \(T^1=k\). The parameter in \(xy=t\) represents its generator, in every characteristic. The preceding lesson proved the full hull assertion and identified an automorphism that prevents its prorepresentability.

For the cusp \(f=y^2-x^3\), the two derivatives are \(-3x^2,2y\). The answer depends on the characteristic:

| Characteristic | \(T^1\) | Basis over \(k\) |
|---|---|---|
| Different from \(2,3\) | \(k[x]/(x^2)\) | \(1,x\) |
| \(2\) | \(k[x,y]/(x^2,y^2)\) | \(1,x,y,xy\) |
| \(3\) | \(k[x]/(x^3)\) | \(1,x,x^2\) |

In the second row, imposing \(x^2=0\) makes the original equation \(y^2=0\). In the third, imposing \(y=0\) leaves \(x^3=0\). Thus the familiar two-dimensional answer has a characteristic restriction. A first-order family with independent parameters is obtained by adding the monomials in the applicable row to the equation. In good characteristic it is \(y^2-x^3+\epsilon(a+bx)\); the other rows require respectively four or three tangent coefficients.

This cusp also explains the final caution of Section 4. In characteristic zero its ring is a domain, so multiplication by the nonzero derivative \(2y\) makes \(B\to B^2\) injective. Hence \(H^{-1}(\operatorname{NL})=0\). At the cusp both derivatives lie in the maximal ideal, so no linear combination of them is one. The injection cannot split there, and Proposition 4.1 proves that the algebra is not smooth. Equivalently \(\Omega\) is not projective there.

## 7 Smooth schemes: locally trivial thickenings

Let \(X\) be a smooth separated \(k\)-scheme. Properness and quasi-compactness are not assumed. Smoothness includes local finite presentation. Write

\[
T_X=\mathcal Hom_{\mathcal O_X}(\Omega_{X/k},\mathcal O_X).
\]

A first-order thickening with identified ideal \(M\) has the same underlying topological space as \(X\), and a sequence of sheaves of \(k\)-algebras

\[
0\longrightarrow M\longrightarrow\mathcal O_{X'}
\longrightarrow\mathcal O_X\longrightarrow0,
\qquad M^2=0.
\tag{7.1}
\]

Assume \(M\) quasi-coherent. Nilpotent thickenings of affine schemes are affine [Stacks, Tag 06AD]. On an affine open \(U=\operatorname{Spec}B\), Proposition 4.1 therefore splits this algebra extension. Its automorphisms preserving the ideal and quotient are the sections of

\[
\mathcal Hom(\Omega_{X/k},M)=T_X\otimes M;
\]

the tensor expression uses the local freeness of \(\Omega\). Every thickening is consequently locally isomorphic to \(\mathcal O_X\oplus M\), although those isomorphisms may fail to agree globally.

**Theorem 7.1.** Isomorphism classes of first-order \(k\)-thickenings of a smooth separated \(X\), with ideal identified as \(M\), form

\[
H^1(X,T_X\otimes M).
\tag{7.2}
\]

Their automorphisms preserving the two ends of (7.1) form \(H^0(X,T_X\otimes M)\). In particular marked flat deformations over \(k[\epsilon]\) are classified by \(H^1(X,T_X)\), and their infinitesimal automorphisms form \(H^0(X,T_X)\).

**Proof.** Choose an affine cover \(\{U_i\}\). Its finite intersections are affine because \(X\) is separated. Split (7.1) on each \(U_i\). On an overlap the two splittings differ by an automorphism of the split algebra preserving \(\mathcal O_X\) and \(M\). By the final calculation in Theorem 3.1 it is \(1+D_{ij}\), for a derivation \(D_{ij}:\mathcal O_X\to M\).

Composition adds these derivations: their cross term is zero because a derivation correction vanishes on \(M\). Thus compatibility on triples is

\[
D_{ij}+D_{jk}=D_{ik}.
\]

Changing the splitting on \(U_i\) by \(1+D_i\) changes the overlap collection by the Čech coboundary of \((D_i)\). Conversely any one-cocycle defines transition maps \(1+D_{ij}\) for the split affine thickenings, and the cocycle identity glues them to a scheme with the sequence (7.1). Its ideal is the specified quasi-coherent \(M\). Affine Čech cohomology computes the cohomology of the quasi-coherent sheaf \(T_X\otimes M\) [Stacks, Tag 01XD], so these equivalence classes give exactly (7.2). This also applies to an infinite affine cover: each intersection is acyclic, which is the affine-cover hypothesis of that cohomology statement.

An automorphism is a compatible family of local derivations; these are the global sections of \(T_X\otimes M\). For \(M=\mathcal O_X\), send \(\epsilon\) to the kernel section corresponding to one. The stalkwise version of (5.1) gives flatness, and every marked flat deformation supplies this same sequence. This proves the final assertions. \(\square\)

One can also express (7.2) as \(\operatorname{Ext}^1_X(\Omega_{X/k},M)\): since \(\Omega\) is locally free, sheaf Hom from it is exact, and derived global Hom is the cohomology of \(T_X\otimes M\). The argument above exhibits the extension and its gluing maps directly.

## 8 The obstruction is a triple-overlap error

Let \(\Lambda\) be a complete Noetherian local ring with residue field \(k\), and let \(B\twoheadrightarrow A\) be a small extension of local Artinian \(\Lambda\)-algebras, with kernel \(I\). Thus \(\mathfrak m_B I=0\) and \(I^2=0\). Let \(X_A\) be a marked flat deformation of the smooth separated \(X\), locally of finite presentation.

**Theorem 8.1.** There is a canonical obstruction

\[
o(X_A,B)\in H^2(X,T_X)\otimes_k I.
\tag{8.1}
\]

It vanishes if and only if \(X_A\) has a flat deformation over \(B\) with a specified identification of its reduction with \(X_A\). If lifts exist, their identified isomorphism classes form a torsor under \(H^1(X,T_X)\otimes I\), and the kernel of their automorphism reduction map is \(H^0(X,T_X)\otimes I\).

**Proof.** We give the local existence argument before forming an obstruction. Each affine open of \(X\) can be refined to an invertible-Jacobian presentation [Stacks, Tag 01V7]. Lift the polynomial coefficients to \(\Lambda\), and invert the lifted minor. This gives a smooth \(\Lambda\)-algebra by [Stacks, Tag 00T7]. Formal smoothness [Stacks, Tag 00TN] maps its base change to \(A\) into the affine deformation algebra, lifting the special-fibre identification. That map is an isomorphism: its cokernel has zero reduction modulo the nilpotent maximal ideal, so is zero; flatness of the target then makes the kernel's reduction zero, so nilpotent Nakayama kills the kernel too. The same model over \(B\) is a local lift.

Any two local lifts over an affine overlap are isomorphic with any prescribed smaller-base comparison. The lifted algebra is smooth over \(B\), so formal smoothness lifts the comparison into the other algebra, and the same flat nilpotent argument makes the lifted map an isomorphism. Affineness of the overlaps follows from separation on the closed fibre and [Stacks, Tag 06AD].

Choose such local lifts \(U_{i,B}\) on an affine cover and overlap isomorphisms \(g_{ij}\), with \(g_{ji}=g_{ij}^{-1}\), lifting the transition maps of \(X_A\). Work with their structure sheaves on the common underlying space, with \(g_{ij}\) directed from the \(j\)-model to the \(i\)-model. An automorphism reducing to the identity over \(A\) has the form \(1+D\). Its difference from the identity lies in

\[
I\mathcal O_{U_B}=I\otimes_k\mathcal O_U,
\]

by flatness. The difference vanishes on the maximal-base-ideal multiple of an argument because \(\mathfrak m_B I=0\), so it factors through the closed fibre. The multiplication identity makes it a \(k\)-derivation. Conversely any such derivation gives an automorphism \(1+D\), with inverse \(1-D\). Their composition adds derivations. This identifies these automorphisms with \(T_X\otimes I\).

Define \(c_{ijk}\) by

\[
g_{ij}g_{jk}g_{ki}=1+c_{ijk}.
\tag{8.2}
\]

The left side reduces to the identity over \(A\), so \(c_{ijk}\) is an infinitesimal derivation. Associate \(g_{ij}g_{jk}g_{kl}\) in the two possible ways. Conjugation of a derivation correction by an overlap map uses only its closed-fibre restriction, which is the prescribed identification with \(\mathcal O_X\). The calculation gives

\[
c_{ijk}+c_{ikl}=c_{jkl}+c_{ijl}.
\tag{8.3}
\]

Thus \(c\) is a Čech two-cocycle. Replacing \(g_{ij}\) by \((1+b_{ij})g_{ij}\), with \(b\) an alternating one-cochain, changes it by

\[
c_{ijk}\longmapsto c_{ijk}+b_{ij}+b_{jk}-b_{ik}.
\tag{8.4}
\]

Changing the local lifts first compares them by local isomorphisms, then has the same effect on the chosen overlap maps. Refinements preserve the resulting cohomology class. Affine Čech cohomology [Stacks, Tag 01XD] therefore gives the canonical class (8.1). Tensoring by the one-dimensional \(I\) commutes with this complex; the same argument permits any finite-dimensional socle kernel.

If the class is zero, (8.4) corrects the transition maps to a cocycle, and they glue the local lifts to \(X_B\). The result is flat and locally finitely presented because these properties hold on the local models. It is separated as well. On an affine pair of opens, the map from the tensor product of their coordinate rings to the coordinate ring of the overlap is onto modulo \(I\), since \(X_A\) is separated. Nilpotent Nakayama makes it onto over \(B\); the affine separation criterion then proves separation of the glued scheme. Conversely a global lift supplies compatible local models and overlap maps with zero error, proving necessity.

To compare two global lifts, choose local isomorphisms preserving their given reduction identification. Their overlap discrepancies are a one-cocycle in \(T_X\otimes I\). Changing the local comparisons changes it by a zero-cochain coboundary. The discrepancy class is zero exactly when the comparisons glue to an identified global isomorphism. Every one-cocycle occurs by changing the transition maps of one lift. This proves the \(H^1\)-torsor assertion. Compatible local automorphisms are global derivations, giving the \(H^0\) assertion. \(\square\)

For a proper \(X\), properness of a lift follows from properness across a nilpotent base thickening [Stacks, Tag 0BPG]. The preceding lesson used finite-dimensional proper cohomology to construct a hull. Theorem 8.1 itself needs neither properness nor finite-dimensional tangent cohomology. For a general smooth separated scheme, the vanishing of \(H^2(T_X)\) still proves the small-extension lifting property; the existence of a Noetherian hull additionally requires the finite-dimensionality condition.

## 9 The projective line is rigid, with automorphisms

On the two affine charts of \(\mathbb P^1\), take coordinates \(z\) and \(w=z^{-1}\). Their tangent frames satisfy

\[
\frac{\partial}{\partial w}=-z^2\frac{\partial}{\partial z}.
\]

Consequently \(T_{\mathbb P^1}=\mathcal O(2)\), in every characteristic. The Čech calculation for \(\mathcal O(d)\) on these charts is

\[
H^1(\mathbb P^1,\mathcal O(d))=
\frac{k[z,z^{-1}]}{k[z]+z^d k[z^{-1}]}.
\tag{9.1}
\]

For \(d=2\) the first summand contains all exponents at least zero, and the second contains all exponents at most two. They cover every Laurent monomial. Hence \(H^1(T)=0\); there are no nontrivial marked first-order deformations by Theorem 7.1. Also the same cover has no nonzero Čech degrees above one, so \(H^2(T)=0\).

This proves rigidity over every Artinian base in \(\mathcal C_\Lambda\). Compare any deformation successively with \(\mathbb P^1_A\). At each small extension, the \(H^1\)-torsor of identified lifts has one element, and the standard projective line supplies that element. Thus every deformation is isomorphic to the standard one, respecting the prescribed smaller-base identification. This assertion concerns Artinian deformations; no algebraization over a general complete base is being inferred.

Rigidity does not say that the isomorphism is unique. Formula (9.1) also gives \(h^0(T)=3\): in the \(z\)-frame the global coefficients are the polynomials of degree at most two. These vector fields yield infinitesimal automorphisms. The difference between deformation parameters and automorphisms remains visible even in this simplest rigid example.

## 10 Exercises with complete solutions

**Exercise 1.** Compute the naive cotangent complex of a smooth finitely presented \(A\)-algebra and prove \(H^{-1}(\operatorname{NL})=0\).

**Solution.** Choose \(P\twoheadrightarrow B\). Formal smoothness splits the extension \(P/I^2\twoheadrightarrow B\). Alternatively apply Proposition 4.1 and Theorem 3.1 to all coefficient modules: the map \(\operatorname{Hom}(\Omega_{P/A}\otimes B,M)\to\operatorname{Hom}(I/I^2,M)\) is onto. Taking \(M=I/I^2\) produces a retraction of the relation differential. Thus \(\Omega_{P/A}\otimes B=(I/I^2)\oplus\Omega_{B/A}\), and the complex is the direct sum of \([I/I^2\xrightarrow{1}I/I^2]\) and \(\Omega_{B/A}[0]\). The first summand is contractible. Therefore the naive complex is homotopy equivalent to the finite projective \(\Omega_{B/A}\) in degree zero and has no degree \(-1\) cohomology. On a standard smooth presentation this is also the invertible-Jacobian-minor computation. Theorem 1.1 makes the answer independent of the chosen presentation.

**Exercise 2.** Prove the transitivity exact sequence of naive cotangent complexes for \(A\to B\to C\). State precisely what is exact.

**Solution.** Present \(B\) by \(A[x]/I\), then \(C\) by \(B[y]/J\), and let \(K\) be the kernel of \(A[x,y]\to C\). The differential modules have the split exact row given by the \(dx\)- and \(dy\)-bases. The relation row is \(I/I^2\otimes C\to K/K^2\to J/J^2\to0\): the last map is onto and its kernel is \((IA[x,y]+K^2)/K^2\), exactly the first map's image. These give (2.1).

Take the termwise kernel complex \(D\) of \(\operatorname{NL}_{C/A}\to\operatorname{NL}_{C/B}\). It fits into a short exact sequence with those complexes. The complex \(\operatorname{NL}_{B/A}\otimes C\) maps onto \(D\) in degree \(-1\) and isomorphically in degree zero. It therefore surjects on \(H^{-1}(D)\) and identifies \(H^0(D)=\Omega_{B/A}\otimes C\). The long cohomology sequence gives exactly (2.2). Its connecting map sends a relation cycle to the differential of any lift in \(K/K^2\), modulo the earlier relation differentials.

There is no initial zero in the conormal row or at the beginning of (2.2). The dual-number example (2.3) prevents interpreting the statement as a distinguished triangle of three two-term naive complexes. If one wants to replace \(H^{-1}(\operatorname{NL}_{B/A}\otimes C)\) by \(H^{-1}(\operatorname{NL}_{B/A})\otimes C\), the Tor conditions proved in Proposition 2.1 suffice; flatness of \(C\) over \(B\) is one sufficient special case.

**Exercise 3.** Compute \(T^1\) for \(B=k[x,y]/(y^2-x^{n+1})\), \(n\geq1\), including the characteristic restrictions in the familiar \(A_n\) answer.

**Solution.** Formula (6.3) gives

\[
T^1=k[x,y]/\bigl(y^2-x^{n+1},\,2y,\,(n+1)x^n\bigr).
\tag{10.1}
\]

If \(2\) and \(n+1\) are invertible in \(k\), this is \(k[x]/(x^n)\), with basis \(1,x,\ldots,x^{n-1}\) and dimension \(n\). If the characteristic is different from two but divides \(n+1\), it is \(k[x]/(x^{n+1})\), with dimension \(n+1\).

In characteristic two, if \(n+1\) is odd, its value in \(k\) is one. Then (10.1) is \(k[x,y]/(x^n,y^2)\), with basis \(x^i,x^iy\), \(0\leq i<n\), and dimension \(2n\). If \(n+1\) is even, both derivatives vanish, so \(T^1=B\), which is infinite-dimensional over \(k\). In that case the equation is the square \((y-x^{(n+1)/2})^2\); its nonsmooth locus is the whole curve, and it is not an isolated \(A_n\) singularity in the usual good-characteristic sense. Thus the customary dimension \(n\) belongs to its stated good-characteristic range. For \(n=2\) the three finite cases recover exactly the cusp table in Section 6.

**Exercise 4.** Show that a smooth affine \(k\)-scheme has no nontrivial marked first-order deformations.

**Solution.** Let \(X=\operatorname{Spec}B\). A flat first-order deformation is affine by invariance of affineness under nilpotent thickening. Its algebra is a square-zero extension of \(B\) by \(B\), as in Section 5. Smoothness makes its Exal class zero by Proposition 4.1, so it is isomorphic to \(B\otimes_k k[\epsilon]\), respecting the special-fibre identification and the \(\epsilon\)-action. Equivalently Theorem 7.1 gives the group \(H^1(X,T_X)\), which is zero by affine vanishing for quasi-coherent sheaves. The isomorphism may have choices: its infinitesimal automorphisms are \(\operatorname{Der}_k(B,B)\).

**Exercise 5.** Prove the obstruction statement for smooth separated schemes by Čech cocycles, including independence of choices and the criterion for vanishing.

**Solution.** For a small extension \(B\to A\), first lift affine standard-smooth charts by lifting their equations and inverting their Jacobian minor. Formal smoothness identifies their \(A\)-reductions with the given charts of \(X_A\), and lifts the comparisons on overlaps. Any error in a comparison that is invisible over \(A\) is a derivation into \(I\mathcal O_{X_B}=I\otimes_k\mathcal O_X\), hence a section of \(T_X\otimes I\); products of such errors add because \(I^2=0\).

For chosen comparisons \(g_{ij}\), write \(g_{ij}g_{jk}g_{ki}=1+c_{ijk}\). Associating the product on four indices in both ways gives \(c_{ijk}+c_{ikl}=c_{jkl}+c_{ijl}\), the two-cocycle identity. Changing comparisons by \(1+b_{ij}\) changes the error by \(b_{ij}+b_{jk}-b_{ik}\), a coboundary. Local isomorphisms comparing any different choices of lifted charts reduce the general change of choices to this calculation. Refining the affine cover carries the same class to the refined Čech complex. Thus there is a canonical class in \(H^2(X,T_X)\otimes I\).

Its vanishing gives a one-cochain correcting the comparisons to a cocycle, which glues the flat smooth charts to a deformation. The affine separation criterion and nilpotent Nakayama preserve separation. Conversely a global deformation has comparisons with zero triple error, so its obstruction class vanishes. Comparing two resulting gluings gives a one-cocycle, with changes by zero-cochain coboundaries; all such cocycles occur. This gives the \(H^1\)-torsor of identified lifts. Compatible local automorphisms give exactly the global sections \(H^0(T_X)\otimes I\). These constructions establish existence, independence, vanishing, choices and automorphisms, rather than only naming a possible obstruction group.

## 11 What this lesson does not prove

The presentation comparison, Jacobi–Zariski sequence, Exal classification, Jacobian tangent calculation and smooth-scheme gluing obstruction were proved here. The prerequisites used in their proofs are:

- The universal property and conormal exact sequence of Kähler differentials, together with the basic derived-category long exact Hom sequence and the Yoneda description of \(\operatorname{Ext}^1\). The particular low-degree derived Ext calculation is supplied in Theorem 3.1.
- Finite presentation plus formal smoothness is equivalent to smoothness [Stacks, Tag 00TN]. Smooth schemes locally have standard-smooth presentations [Stacks, Tag 01V7], and an invertible Jacobian minor gives a smooth algebra [Stacks, Tag 00T7]. The derivation and extension computations establishing Proposition 4.1 were given here.
- Affineness survives a nilpotent thickening [Stacks, Tag 06AD]. A separated scheme has affine intersections of affine opens, and separation is tested by the surjectivity of the tensor-product maps to their coordinate rings [Stacks, Tag 01KP]. These allow the local algebra lifts to be glued as separated schemes.
- Quasi-coherent sheaves have no higher cohomology on affine schemes, and an affine cover with affine finite intersections computes their cohomology [Stacks, Tag 01XD]. No cohomology finiteness theorem was needed for Theorems 7.1 and 8.1.
- Properness extends across the nilpotent base thickenings under consideration [Stacks, Tag 0BPG], when one restricts the deformation problem to proper schemes.

We have not constructed the full cotangent complex or claimed that its lower cohomology vanishes for an arbitrary algebra. Nor have we identified all singular-scheme obstruction groups with a tangent-sheaf cohomology group: local equation deformations contribute there. The final lesson constructs the full complex, proves its transitivity triangle, and develops its degree-two obstruction theory.

## References

- The Stacks project, [the naive cotangent complex](https://stacks.math.columbia.edu/tag/00S0), [Jacobi–Zariski sequence](https://stacks.math.columbia.edu/tag/00S2), [extensions of algebras](https://stacks.math.columbia.edu/tag/0GPT), and [deformations of schemes](https://stacks.math.columbia.edu/tag/0D14). The tagged texts are read in the AI Integrated Stacks Project edition.
- Schlessinger, *Functors of Artin rings*, Transactions of the American Mathematical Society **130** (1968), 208–222, §3. [Original paper](https://doi.org/10.1090/S0002-9947-1968-0217093-3).
- For the relation with the full complex: Lichtenbaum and Schlessinger, *The cotangent complex of a morphism*, Transactions of the American Mathematical Society **128** (1967), 41–70; the comparison is formulated in [Stacks, Tag 09AM](https://stacks.math.columbia.edu/tag/09AM). Its lower-degree construction is not used as an input to the proofs above.
