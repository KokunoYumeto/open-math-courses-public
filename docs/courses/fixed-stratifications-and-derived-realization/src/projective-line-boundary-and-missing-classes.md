# The projective line: a boundary class and a missing object

Both strata of the projective line's partition into an affine line and infinity are contractible, yet its fixed constructible heart loses a degree-two ambient class and the cone object it determines. We prove this by classifying the ordinary heart, resolving its diagrams and calculating the link at infinity.

Work over any field. Standard sheaf adjunctions and truncation triangles are prerequisites. Equations 14–19 retain their locators in the parent lesson. The example concerns this fixed partition; the separate all-refinement K3 argument in the parent course is a stronger result and is not needed here.

*Original AI teaching expression and solutions: GPT-6.1 Sol (OpenAI), Ultra, October 2026, CC0. Human mathematical source and adapted proof structure: Lunts–Schnürer, CC BY 4.0; see [Sources and reuse](#sources-and-reuse).*

## A fixed projective-line stratification already loses a class

The parent course gives a K3 argument permitting every complex refinement. Here we prove a simpler failure for one fixed stratification, distinguished from that stronger assertion. Let \(X=\mathbb P^1(\mathbb C)\), let \(j:\mathbb C\hookrightarrow X\), and let \(i:\{\infty\}\hookrightarrow X\). Work over any field \(k\). Put
\(\mathcal B=\operatorname{Cons}_k(X,\{\mathbb C,\infty\})\), allowing arbitrary stalk vector spaces. Its finite-stalk subcategory is \(\mathcal B_f\). Both strata are contractible.

### The ordinary heart and its projectives

The open restriction is a constant sheaf \(M_{\mathbb C}\), since \(\mathbb C\) is simply connected. A punctured neighborhood of infinity is connected, so \(j_*M_{\mathbb C}=M_X\). The following stalkwise pullback construction identifies the heart with the category of one-arrow diagrams

\[
A\xrightarrow{\,u\,}M.
\tag{14}
\]

The stalk at infinity is \(A\), and the map is its ordinary specialization to the nearby constant module. Conversely take the pullback of \(M_X\to i_*M\) and \(i_*A\xrightarrow{i_*u}i_*M\). Its restriction to the open stratum is \(M_{\mathbb C}\), its closed stalk is \(A\), and its specialization is \(u\). The natural maps from a sheaf to this pullback are isomorphisms at every stalk. This proves the classification for finite and infinite vector spaces.

Write \(P_\infty(V)=(V\xrightarrow{\mathrm{id}}V)\) and \(P_o(W)=(0\to W)\). A map from the first to (14) is determined by \(V\to A\), and one from the second by \(W\to M\). Since vector spaces are projective, both diagrams are projective. Every diagram has the explicit resolution

\[
0\longrightarrow P_o(A)
\xrightarrow{\ a\mapsto(a,-u(a))\ }
P_\infty(A)\oplus P_o(M)
\longrightarrow (A\xrightarrow{u}M)\longrightarrow0.
\tag{15}
\]

The last map is identity at the closed vertex and \((a,m)\mapsto u(a)+m\) at the open vertex. Its kernel at the open vertex is \(\{(a,-u(a))\}\), and its closed kernel is zero. This verifies exactness. All terms remain finite when \(A,M\) are finite, so both hearts have no Yoneda extensions of degree at least two.

The constant sheaf \(k_X\) is \(P_\infty(k)\), already projective. Consequently

\[
\operatorname{Hom}_{D^b(\mathcal B)}(k_X,k_X[q])=0
\quad(q>0),\qquad
\operatorname{Hom}_{D^b(X;k)}(k_X,k_X[2])
=H^2(X;k)=k.
\tag{16}
\]

The same source vanishing holds in \(D^b(\mathcal B_f)\). For the ambient equality, \(\operatorname{Hom}(k_X,-)=\Gamma(X,-)\), and its derived functor is sheaf cohomology. The projective line is the two-sphere: its cell decomposition has a zero-cell and a two-cell, with zero differential. Thus its second cohomology over \(k\) is \(k\). This calculates the missing morphism directly.

### The missing object has the same constant cohomology

Choose \(0\ne u:k_X\to k_X[2]\) in the ambient category and set \(E=\operatorname{Cone}(-u)[-1]\). Rotation gives

\[
k_X[1]\longrightarrow E\longrightarrow k_X
\xrightarrow{\,u\,}k_X[2].
\tag{17}
\]

The cohomology sequence gives \(H^{-1}(E)=k_X\), \(H^0(E)=k_X\), and zero otherwise. The displayed triangle is its canonical truncation triangle, so its connecting class is exactly \(u\), including the cone sign. Thus \(E\) is constructible for the fixed two-stratum partition, with finite cohomology stalks.

If it were realized by a bounded complex from either heart, its cohomology there would be the same two constant sheaves. Its source truncation triangle would have connecting map in \(\operatorname{Ext}^2(k_X,k_X)=0\), hence would split. Realization preserves the canonical truncation maps, forcing the connecting map in (17) to vanish. This contradicts the choice of \(u\). Therefore realization from either fixed heart is neither full nor essentially surjective.

### The link explains why contractible strata do not suffice

The fixed-stratification criterion tests not only the strata but the comparison between direct images derived internally and in all sheaves. The constant local system \(k_{\mathbb C}\) is injective in \(\operatorname{Loc}_k(\mathbb C)\), because that category is vector spaces. Internally its derived direct image is therefore \(j_*k_{\mathbb C}=k_X\) in degree zero. Ambient direct image has the boundary stalk

\[
(R^qj_*k_{\mathbb C})_\infty
=H^q(S^1;k)
=
\begin{cases}
k,&q=0,1,\\
0,&q\geq2 .
\end{cases}
\tag{18}
\]

A punctured disk retracts to the circle, and arbitrarily small punctured disks give the same restriction on this cohomology. These are the actual stalks of the derived direct image. Its degree-one boundary term proves that the canonical comparison \(\sigma_j\) is not an isomorphism. The link's fundamental-group map is

\[
\pi_1(S^1)=\mathbb Z\longrightarrow\pi_1(\mathbb C)=0.
\tag{19}
\]

It is not injective. Universal-cover acyclicity holds for both strata, yet the independent boundary condition fails.

Removing also zero from the open stratum changes the answer. For the three torus-orbit strata \(\mathbb C^*,0,\infty\), each link circle maps isomorphically onto \(\pi_1(\mathbb C^*)=\mathbb Z\), after choosing a generator. The full comparison proof in the linked lesson establishes bounded and bounded-below realization for the unrestricted three-stratum heart, for every unital coefficient ring. Thus this fixed projective-line example does not assert failure after every complex refinement. The parent course's K3 argument supplies precisely that stronger phenomenon.

Lunts and Schnürer's [*Categories of constructible sheaves*, Theorem 5.25 and Remark 6.12](https://arxiv.org/abs/2601.05477v1) supplies the fixed-stratification criterion and the projective-line failure example. The full one-arrow calculation and cone argument here make the failure of both morphism and object realization explicit.

## Further exercises on the boundary comparison

### An injective open coefficient can have an ambient higher direct image

*Difficulty: Intermediate.*

On the two-stratum projective line, compute the boundary stalks of direct image derived within the constructible categories and of ambient derived direct image for \(k_{\mathbb C}\). Explain why applying the ambient functor to an internally injective object need not give a degree-zero complex.

**Solution.** The open local-system heart is vector spaces, so \(k_{\mathbb C}\) is injective there. Its internal resolution has one term, and its internal derived image has boundary stalk \(k\) in degree zero and zero in positive degree. In all sheaves, shrinking punctured disks computes \(H^*(S^1;k)\), with \(k\) in degrees zero and one. The coefficient is injective in the local-system heart, not asserted injective in all sheaves on \(\mathbb C\). Its nonzero boundary \(R^1j_*\) is exactly the obstruction to using that internal resolution for the ambient image.

### A finite constant coefficient is not the injective test on a torus stratum

*Difficulty: Advanced.*

Let \(A=k[t,t^{-1}]\), the monodromy ring of \(\mathbb C^*\). For any injective \(A\)-module \(I\), prove that multiplication by \(t-1\) is surjective and hence \(H^1(S^1;I)=0\). Compare with the constant finite module \(k=A/(t-1)\). Explain why \(H^1(S^1;k)=k\) does not disprove the three-stratum comparison.

**Solution.** For \(x\in I\), define an \(A\)-map from the ideal \((t-1)A\) by \((t-1)a\mapsto ax\). The ring is a domain, so the representation is unique. Injectivity extends this map to \(A\to I\). Its value \(y\) at one satisfies \((t-1)y=x\), proving surjectivity. The free resolution \(0\to A\xrightarrow{t-1}A\to k\to0\) computes group cohomology as \(H^0=\ker(t-1)\), \(H^1=\operatorname{coker}(t-1)\), and no higher groups. The injective coefficient therefore has no positive link cohomology. On \(k\) the map \(t-1\) is zero, and \(H^1=k\). That finite constant module is not injective over \(A\); the internal derived direct image uses an injective resolution of it and recovers the same degree-one boundary term as the ambient image. A comparison isomorphism does not require every ordinary local system to have acyclic links.

## Sources and reuse

Valery A. Lunts and Olaf M. Schnürer, [*Categories of constructible sheaves*, arXiv:2601.05477v1](https://arxiv.org/abs/2601.05477v1), 9 January 2026, Remark 6.12 (p. 31), identifies the failure for the two-stratum projective line. Theorem 5.25 and Theorem 6.10 give the realization and boundary criteria. Remark 6.12 does not supply the one-arrow resolution, the explicit missing cone object or the two solved calculations; those arguments are written out in this reading.

The original AI expression, expanded checks, exercises, solutions and reader code are dedicated under CC0. This dedication does not relicense the human source or any protected material adapted from it: Lunts–Schnürer is attributed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The presentation is rewritten and condensed, with calculations expanded; its proof structure is source-derived. No verbatim source prose is included. The [source and dependency notes](../source-notes.html) identify the exact passages, changes and remaining prerequisites.

Sheaf adjunctions, derived truncations and the usual local-coefficient cohomology of disks and circles and constant-coefficient cohomology of the two-sphere remain prerequisites. Lunts–Schnürer supplies the realization and boundary criteria and the projective-line failure example; the explicit resolution, missing cone object and solved calculations are given above. These readings do not supply a complete development of the underlying sheaf-theoretic and topological foundations.

[Reading index](../index.html) · [Source and dependency notes](../source-notes.html) · [Reuse terms](../LICENSE.txt) · Provenance
