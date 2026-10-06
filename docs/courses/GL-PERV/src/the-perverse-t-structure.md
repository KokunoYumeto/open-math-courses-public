# The perverse t-structure

*Rewritten and self-checked by GPT-6 Astra (OpenAI) in Codex, Ultra setting, October 2026. Public domain (CC0).*

A local system on a curve and a vector space at one point can belong to the same abelian category, although their nonzero ordinary cohomology occurs in different degrees. This lesson constructs that category by cutting a complex on a smooth open set and then correcting the cut on its boundary. Explicit curve and surface calculations show what the boundary correction detects. We subsequently construct descent and prove finite length.

Our coefficients are a field \(\Lambda\). We retain both the classical complex-algebraic setting and the finite or rational-adic étale settings of Constructible complexes on algebraic varieties. In the étale setting the torsion characteristic is invertible on the varieties. The adic statements require the normalized operations and comparison maps listed in that lesson; their unfinished proof obligations remain obligations here. Dimension means complex dimension classically and algebraic dimension étale-locally. A shift has \(\mathcal H^q(K[m])=\mathcal H^{q+m}K\).

The mathematical source for the dimension conditions is the freely readable author-hosted edition of BBD, especially §§2.1–2.2 and 4.0. We use the reconstructed adjunction, localization and heart arguments of Gluing t-structures. Below, an external reference identifies source material; the written arguments and their explicitly identified programme prerequisites carry the proof obligations.

## 1. Degrees at a puncture

Begin with a disc, its punctured open part \(j:U\hookrightarrow X\), and the centre \(i:\{0\}\hookrightarrow X\). A local system on \(U\) is specified by a finite-dimensional space \(V\) and an invertible monodromy \(T\). Write \(S=T-1\). The first lesson's Proposition 1.1 and Appendix A compute the actual boundary complex:

\[
i^*Rj_*L[1]=[V\xrightarrow{S}V],
\qquad\text{in degrees }-1,0.
\tag{1.1}
\]

Thus moving a local system into degree \(-1\) does not force everything at the missing point into degree \(-1\). There can be degree-zero boundary information. The attaching construction and its morphisms, proved in Exercise 5 and Appendix B of the preceding lesson, describe the heart for the open placement \(L[1]\) and the closed placement \(E[0]\) by

\[
V\xrightarrow{u}W\xrightarrow{v}V,
\qquad vu=T-1.
\tag{1.2}
\]

Its stalk and costalk are respectively \([V\xrightarrow uW]\) in degrees \(-1,0\) and \([W\xrightarrow vV]\) in degrees \(0,1\). The invertibility conditions in that description hold because \(1+vu=T\) is invertible; explicitly
\((1+uv)^{-1}=1-u(1+vu)^{-1}v\).
For the familiar extensions the diagrams are

| Object | \(W\) | \(u\) | \(v\) |
|---|---|---|---|
| \(j_!L[1]\) | \(V\) | \(1\) | \(S\) |
| \(Rj_*L[1]\) | \(V\) | \(S\) | \(1\) |
| \(j_{!*}L[1]\) | \(\operatorname{im}S\) | \(S\) | inclusion |
| \(i_*E\) | \(E\) | \(0\) | \(0\) |

The third row has stalk \(\ker S\) in degree \(-1\) and costalk \(\operatorname{coker}S\) in degree \(1\). The zero-degree boundary subobject and quotient have been removed. These are calculations in the previously proved recollement heart, before any assertion about all varieties. They suggest the placements to glue: degree \(-s\) for a local system on a smooth stratum of dimension \(s\).

## 2. Constructing the dimension cuts

For a constructible sheaf, define its support dimension as the dimension of the closure of its nonzero locus, with dimension \(-\infty\) for zero. On the full bounded constructible category set

\[
\begin{aligned}
{}^pD^{\leq0}(X)&=\{K:\dim\operatorname{Supp}\mathcal H^qK\leq-q
                                      \text{ for every }q\},\\
{}^pD^{\geq0}(X)&=\{K:D_XK\in{}^pD^{\leq0}(X)\}.
\end{aligned}
\tag{2.1}
\]

Here \(D_X\) is structural Verdier duality. This is a definition by support dimensions, not by codimension in an embedding. Components of different dimensions are allowed.

### The local tests and the input they require

Choose finitely many smooth pure-dimensional locally closed pieces on which the needed restrictions and exceptional restrictions have lisse cohomology. Classically the first lesson's Appendices I–K construct suitable algebraic Whitney refinements and their operation properties. Our étale base fields, a finite field or its algebraic closure, are perfect, so a reduced variety has a dense smooth open; bounded constructibility of the finitely many complexes and their images permits successive refinement of the lower-dimensional boundary. We use only the finite list of objects in the argument: no arbitrary smooth partition is asserted to be stable under all boundary operations. The needed smooth-open algebraic argument is included in the first lesson, M.1. The normalized adic operation and duality comparisons remain among the stated foundations.

Write \(a:S\hookrightarrow X\) and \(s=\dim S\). Then

\[
K\in{}^pD^{\leq0}\iff H^q(a^*K)=0\ (q>-s),
\qquad
K\in{}^pD^{\geq0}\iff H^q(a^!K)=0\ (q<-s).
\tag{2.2}
\]

For the first assertion, the support of a nonzero lisse sheaf on a connected piece has dimension \(s\); the support dimension of a sheaf on a finite partition is the maximum of those dimensions. For the second use \(a^*D_XK=D_Sa^!K\). Smooth duality over a field gives

\[
H^q(D_SF)=\bigl(H^{-q-2s}F\bigr)^\vee(s)
\tag{2.3}
\]

for bounded lisse \(F\); omit the twist classically. Indeed local finite-dimensional dualization reverses cohomological degree, and the dualizing complex supplies the shift \(2s\). Exactness of vector-space dualization gives the formula on cohomology. The bound \(q\leq-s\) for the dual is precisely the bound \(q\geq-s\) for \(F\).

For an open–closed pair \(j:U\hookrightarrow X\), \(i:F\hookrightarrow X\), (2.1) consequently satisfies

\[
\begin{aligned}
K\in{}^pD^{\leq0}(X)&\iff j^*K\in{}^pD^{\leq0}(U),\ i^*K\in{}^pD^{\leq0}(F),\\
K\in{}^pD^{\geq0}(X)&\iff j^*K\in{}^pD^{\geq0}(U),\ i^!K\in{}^pD^{\geq0}(F).
\end{aligned}
\tag{2.4}
\]

The upper equivalence also follows directly by decomposing the support into its open and closed parts. Duality and its restriction exchanges give the lower one.

### An actual truncation triangle

**Theorem 2.1.** The pair (2.1) is a bounded t-structure. Its heart, \(\operatorname{Perv}(X)\), is independent of the partition used to compute it. Duality is an exact anti-equivalence of this heart.

**Proof.** We induct on dimension, with the empty space as the initial case. In dimension zero the assertion is the ordinary bounded t-structure on finite collections of finite-dimensional coefficient representations. Shift closure follows at once from (2.1).

For orthogonality take \(A\in{}^pD^{\leq0}(X)\), \(B\in{}^pD^{\geq1}(X)\). Choose a dense open \(U\) which is a disjoint union of smooth pure-dimensional pieces and on which both objects have lisse cohomology. Its complement \(F\) has smaller dimension. On a piece of dimension \(s\), the restrictions of \(A,B\) have ordinary bounds \(\leq-s\) and \(\geq1-s\), so their Hom is zero by ordinary truncation. On \(F\), (2.4) and induction give \(\operatorname{Hom}(i^*A,i^!B)=0\). Apply \(\operatorname{Hom}(-,B)\) to
\(j_!j^*A\to A\to i_*i^*A\to\).
Adjunction identifies its two outside Hom terms with the two zero groups just obtained. Hence \(\operatorname{Hom}(A,B)=0\).

Now take an arbitrary \(K\), choose such a dense smooth \(U\) for its ordinary cohomology, and form on each component
\(U_0=\tau_{\mathrm{ord}}^{\leq-s}j^*K\).
These complexes assemble on the disjoint components. Make the first cone and then a cut on its closed part:

\[
j_!U_0\longrightarrow K\longrightarrow K_1\longrightarrow,
\qquad
F_0={}^p\tau_F^{\leq0}i^!K_1.
\tag{2.5}
\]

The second cut exists by induction. Adjunction and its truncation map give \(i_*F_0\to K_1\); complete it to
\(i_*F_0\to K_1\to B\to\).
The octahedron for \(K\to K_1\to B\) supplies

\[
A\longrightarrow K\longrightarrow B\longrightarrow,
\qquad
j_!U_0\longrightarrow A\longrightarrow i_*F_0\longrightarrow.
\tag{2.6}
\]

Applying \(j^*,i^*\) to the second triangle gives \(j^*A=U_0\), \(i^*A=F_0\), so (2.4) puts \(A\) in the upper half. The first cut gives \(j^*B=\tau_{\mathrm{ord}}^{\geq1-s}j^*K\). Applying \(i^!\) to the triangle defining \(B\) gives \(i^!B={}^p\tau_F^{\geq1}i^!K_1\). Thus \(B\) is in the lower half shifted to degree one. All these objects remain bounded constructible by the earlier operation theorems. This is the required truncation triangle, using the same cone construction as the gluing theorem of Lesson 2.

The categorical uniqueness argument in that lesson's Appendix A makes these cuts functorial and independent of every open set and cone choice. The classes themselves were intrinsic in (2.1), so a compatible refinement cannot change them. Boundedness can also be checked without a uniform partition for the whole category: a fixed complex and its dual have only finitely many nonzero cohomology sheaves of finite support dimension. Sufficient shifts put each in the upper half of (2.1), and biduality supplies a lower bound.

Finally, (2.1) and biduality exchange the two halves. Duality reverses a triangle representing a short exact sequence of heart objects. The heart long exact sequence therefore reverses that short exact sequence. It is an exact anti-equivalence. \(\square\)

In particular, a lisse \(L\) on smooth pure \(d\)-dimensional \(X\) gives \(L[d]\in\operatorname{Perv}(X)\). Its dual is \(L^\vee[d]\) classically and \(L^\vee(d)[d]\) étale-locally. A point-supported vector space belongs in degree zero. These assertions concern field coefficients. Already on a point, \(\ell^n\mathbf Z_\ell\) gives an infinite descending chain in \(\mathbf Z_\ell\), and derived integral dualization need not preserve the same heart.

### Why the generic points matter

For an algebraic point \(x\), put \(d_x=\dim\overline{\{x\}}\). Use a geometric stalk over \(x\). For exceptional restriction to a nonclosed point, first apply exceptional restriction to its closure and then pass to its generic point. With this convention the two conditions are

\[
H^q(i_x^*K)=0\ (q>-d_x),\qquad
H^q(i_x^!K)=0\ (q<-d_x).
\tag{2.7}
\]

Here is the comparison, including the lower bound. Let \(x\) lie in a smooth stratum \(S\) of dimension \(s\). Take a smooth dense open \(T\) in its closure inside \(S\), of dimension \(t=d_x\); work near its generic point. For \(b:T\hookrightarrow S\) and a lisse complex \(F\), smooth duality and the exceptional-restriction exchange give

\[
b^!F=b^*F(t-s)[2t-2s].
\tag{2.8}
\]

One obtains this formula by dualizing on \(S\), restricting, and dualizing on \(T\): the two coefficient dualizations cancel, and their shifts and twists subtract. Ordinary restriction preserves an upper bound \(-s\), which is no larger than \(-t\). The exceptional restriction changes a lower bound \(-s\) into \(-s+2(s-t)=-t+(s-t)\), which is at least \(-t\). Hence (2.2) implies (2.7). Conversely use the generic point of each irreducible stratum. There \(t=s\), and vanishing of a lisse cohomology sheaf at that point implies its vanishing everywhere on the stratum. This proves the equivalence.

These are BBD's all-point conditions in §4.0, with its convention from §2.2.12. Ordinary classical points do not include generic points of algebraic strata. On a smooth complex curve the unshifted constant sheaf has stalk only in degree zero and closed-point costalk only in degree two. It passes inequalities \(q>0\) and \(q<0\) at every such point, yet fails the dimension-one upper test. Classical perversity must use (2.1) or (2.2).

## 3. Reading the boundary cohomology

### Curves

Let \(X\) be a reduced curve of pure dimension one. Given a constructible complex, choose a finite closed set \(F\) containing the singularities of \(X\) and its cohomology sheaves; write \(U=X\setminus F\). The boundary complex \(i^*Rj_*L[1]\) for a lisse \(L\) on \(U\) has cohomology only in degrees \(-1,0\).

Classically, the branch neighborhoods and their punctures are constructed in the first lesson's Appendix L. They give finitely many punctured discs. The explicit cochains of its Appendix A prove the claim on each branch, and the finite disjoint union takes their direct sum.

For finite étale coefficients, make the assertion locally at a boundary point. On an affine curve neighborhood choose a function vanishing at that point but not identically on any branch. Prime avoidance supplies it. Its other zeros form a finite set; removing those makes the given puncture a principal affine open. Theorem 6.2 of the earlier programme lesson [Cohomological dimension and the Künneth formula, §6](course:ag-etale-cohomology/cohomological-dimension-and-the-kunneth-formula) proves the affine support bound: for a sheaf with support dimension at most one, \(R^qj_*L\) is supported in points of dimension at most \(1-q\). It is therefore zero for \(q>1\). This uses that theorem's strict-local stalk argument, not ordinary cohomology of the geometric fibre of a nonproper map. The remaining cohomology stalks are finite by the first lesson's finite-coefficient image theorem, Appendix M.

For an adic lattice and its finite quotients, the same degrees occur at every finite level. In each fixed finite cohomology group, the images from later levels form a descending chain and eventually stabilize. For a countable inverse system with this property, the map
\(1-\mathrm{shift}:\prod A_n\to\prod A_n\)
is onto: first solve recursively in the stable images, whose transition maps are onto; in the quotient system each fixed coordinate eventually receives only zero, so the finite-coordinate sums solve the same equation there. Lifting a quotient solution leaves an error in the stable images, removed by the first solution. Its kernel is \(\varprojlim A_n\), so the product-cone model of derived limit adds no cohomology group. Thus the bound passes to the lattice and then, by exact localization, to rational coefficients, **provided** the actual normalized stalk/image and derived-limit comparison maps have the properties required in the first lesson. Those adic comparisons are still an identified proof obligation. No tame-monodromy description is assumed for a wild étale local system.

**Proposition 3.1 (curve criterion).** At these coefficient settings, with their stated operation prerequisites, a bounded constructible \(K\) is perverse precisely when

1. its only possible ordinary cohomology sheaves are \(M=\mathcal H^{-1}K\) and \(N=\mathcal H^0K\);
2. \(N\) is supported at finitely many points;
3. \(M\) has no nonzero sections supported at a point.

**Proof.** If \(K\) is perverse, its restriction to \(U\) is \(L[1]\). The upper bound at the points of \(F\) excludes all positive ordinary cohomology. For the lower ordinary degrees, use the actual localization triangle at a point:

\[
i_x^!K\longrightarrow i_x^*K\longrightarrow i_x^*Rj_*L[1]\longrightarrow.
\tag{3.1}
\]

The first term has no negative cohomology; the last has degrees \(-1,0\). Hence the middle has none below \(-1\). Degree-zero ordinary cohomology vanishes on \(U\), proving the first two claims. The ordinary truncation triangle now is
\(M[1]\to K\to N\to M[2]\).
Exceptional restriction of \(N\) at a point is concentrated in degree zero. For the sheaf \(M\), it is the right derived functor of sections with that support, and has no negative cohomology. The long exact sequence therefore gives

\[
H^{-1}(i_x^!K)=H^0(i_x^!M)
                         =\{\text{germs of sections of }M\text{ supported at }x\}.
\tag{3.2}
\]

The lower perverse bound gives the third claim. In the converse direction, the three assumptions make the open restriction lisse in degree \(-1\) after a finite refinement. All closed stalk bounds hold. Equation (3.2) removes degree \(-1\) in the costalk, and the same truncation triangle shows that there are no still lower groups. Thus all tests in (2.2) hold. \(\square\)

The constant sheaf has no section supported at a nonisolated point: a locally constant nonzero germ remains nonzero on a neighborhood, which contains another point. Consequently \(\Lambda_X[1]\) is perverse for a reduced **pure** curve, including nodes. An isolated zero-dimensional component would instead require degree zero. The disc diagrams in §1 also prove that \(j_!\Lambda[1]\) and \(Rj_*\Lambda[1]\) are perverse for \(\mathbf C^*\hookrightarrow\mathbf C\).

### Isolated surface singularities

Let the punctured neighborhood of an isolated complex surface singularity \(x\) have compact link \(M\). The normal cone neighborhoods of the first lesson, I.6, identify sufficiently small neighborhoods with an open cone on \(M\). Its Appendix C supplies the relative cochain comparison, and J.4 identifies this relative complex with the sheaf costalk. The cone is contractible and its puncture retracts to \(M\), whence

\[
H^k(i_x^!\Lambda_X[2])=\widetilde H^{k+1}(M;\Lambda).
\tag{3.3}
\]

Since \(M\ne\varnothing\), the negative costalk groups vanish exactly when \(\widetilde H^0(M)=0\). The open smooth surface and the closed stalk already satisfy their tests. Thus \(\Lambda_X[2]\) is perverse near the singularity exactly when \(M\) is connected. In particular, \(H^1(M)\) occurs in allowed costalk degree zero, not in an obstructing negative degree.

For the two coordinate planes in \(\mathbf C^4\), namely
\(\{z_3=z_4=0\}\cup\{z_1=z_2=0\}\),
the link is \(S^3\sqcup S^3\). Reduced cohomology is \(\Lambda\) in degree zero and \(\Lambda^2\) in degree three. Equation (3.3) gives costalk degrees \(-1\) and \(2\), respectively, so the shifted constant complex is not perverse.

For a normal analytic surface germ, connectedness has a short proof using the analytic definition of normality: locally bounded holomorphic functions on the regular locus extend holomorphically over the germ. If its conical puncture were disconnected, assign values zero and one to a nontrivial partition of its components. This gives a bounded holomorphic function on the puncture. Its normal extension is continuous at the vertex, whereas both values approach the vertex along radial cone lines. This is impossible. Hence the link is connected and the shifted constant complex is perverse. This uses the definition and equivalent local-ring formulation in Demailly, Chapter II, §7. The equivalence with the algebraic normality hypothesis for an algebraic surface is a required analytic-comparison foundation; it is not proved merely by citing that definition, and is retained as an open prerequisite below.

For a normal isolated surface singularity, rational smoothness is the stronger requirement that its link have the rational cohomology of \(S^3\). The link is a connected closed oriented three-manifold: away from the vertex the surface is a complex manifold, and a transverse radial level inherits the boundary orientation. The compact oriented duality constructed in the first lesson identifies its degree-one and degree-two cohomology dually, while degrees zero and three are \(\mathbf Q\). Thus rational smoothness here is equivalent to \(H^1(M;\mathbf Q)=0\). For a cone over a smooth plane cubic, the first lesson's Thom–Gysin and plane-curve calculations give Betti numbers \(1,2,2,1\). Its constant complex shifted by two is perverse but the vertex is not rationally smooth. We use rational coefficients for this particular Betti-number assertion.

## 4. Constructing objects from local data

The support and cosupport tests are local for open restrictions. They are also local for étale pullback: local dimensions agree, and ordinary and exceptional restrictions satisfy the étale base-change comparisons. Thus an étale pullback \(f^*\) is t-exact; if \(f\) is surjective it is conservative, as geometric stalks show. Its derived right adjoint \(Rf_*\) preserves the lower half. Indeed, for \(A\in{}^pD^{\leq-1}\), \(B\in{}^pD^{\geq0}\), adjunction gives \(\operatorname{Hom}(A,Rf_*B)=\operatorname{Hom}(f^*A,B)=0\); the orthogonality characterization of a t-structure yields the assertion.

**Proposition 4.1 (effective descent).** Perverse sheaves and their morphisms glue uniquely from descent data on algebraic open or étale covers. On topological open covers the same statement holds for a fixed compatible finite stratification. With varying stratifications, global finite constructibility must be imposed.

**Proof.** First take a quasi-compact separated étale surjection \(f:Y\to X\). A finite disjoint union of algebraic opens is included in this case. Let \(P_Y\) be perverse and let \(\theta:p_1^*P_Y\to p_0^*P_Y\) on \(Y\times_XY\) satisfy the cocycle condition. Write \(g:Y\times_XY\to X\). Adjunction and \(\theta\) give two maps

\[
C^0={}^pH^0(Rf_*P_Y)\quad\rightrightarrows\quad
C^1={}^pH^0(Rg_*p_0^*P_Y).
\tag{4.1}
\]

Define \(P\) as their equalizer, or the kernel of their difference, in the already constructed heart. The images in (4.1) exist as bounded constructible complexes by the operation theorems. They lie in perverse degrees at least zero, by the preceding adjunction argument.

We check effectiveness without assuming descent of complexes. Pull back to \(Y\). T-exactness commutes with \({}^pH^0\) and kernels; étale base change identifies the result with the first two direct images for the pulled-back cover \(Y\times_XY\to Y\). This cover has its diagonal section. The cocycle \(\theta\) identifies its coefficient system with the pullback of \(P_Y\). Inserting the diagonal section gives an augmentation \(a:P_Y\to f^*C^0\), a retraction \(h^0:f^*C^0\to P_Y\), and a map \(h^1:f^*C^1\to f^*C^0\) satisfying

\[
h^0a=1,\qquad h^1(d^0-d^1)=1-ah^0.
\tag{4.2}
\]

For completeness these identities already hold before perverse cohomology. The map \(h^0\) restricts a section on the cover to the chosen section; \(h^1\) restricts a two-fold section to the pair consisting of that chosen lift and the variable lift. The two faces then give, respectively, the original section and its value at the chosen lift transported by \(\theta\). Their difference is \(1-ah^0\). The cocycle condition makes these transports agree on triples. These are maps induced by units, pullbacks and the section, so the same identities hold for their derived maps and after \({}^pH^0\). Equation (4.2) identifies the equalizer with \(P_Y\). The induced identifications on the double overlap are precisely \(\theta\), again by its cocycle. Thus \(f^*P\simeq P_Y\) with the prescribed descent datum.

A compatible morphism of descent data induces maps of the two terms of (4.1), hence a map of equalizers. It restricts to the prescribed morphism by (4.2). Uniqueness follows because a conservative exact functor on abelian categories is faithful: the image of a morphism which pulls back to zero pulls back to zero, and is consequently zero. This proves full descent, not just existence of an object.

An arbitrary étale cover of a finite-type scheme has a finite subcover by quasi-compact separated étale charts: refine the domains by affine opens and use quasi-compactness of the target. Apply the construction to their disjoint union. On every additional chart its restriction is the prescribed object, because this can be checked after the already chosen covering base change; the uniqueness just proved makes these identifications compatible. This includes arbitrary algebraic open covers.

Here are the extra details for arbitrary classical topological open covers. One may temporarily work in bounded-below complexes of all sheaves, with the finite fixed stratification and perversities \(-\dim S\). The ordinary shifted structures on individual strata glue by Lesson 2; no constructibility or duality is needed for this auxiliary structure. Its restriction to the constructible category is the structure already proved. For the local homeomorphism \(f:\coprod U_\alpha\to X\), restriction is exact and t-exact for these stratum tests. Its right adjoint preserves the lower half, and its open base change is obtained simply by restricting sections and their injective resolutions. Form (4.1) in this larger heart. The same diagonal-section identities prove that its restriction is the prescribed perverse object on each open. It is therefore locally lisse of finite rank along the fixed strata. With the stipulated global finite constructibility, it lies in the required constructible category. Its ordinary cohomology is uniformly in degrees \([-\dim X,0]\): the upper bound follows from the stalk tests, and the lower bound follows by induction from \(i_*i^!K\to K\to Rj_*j^*K\to\) and left exactness of ordinary right derived images. Thus boundedness is also global. The previous faithful-exact argument proves uniqueness of morphisms. \(\square\)

## 5. Finite chains of subobjects

We first show that allowing finer singular strata does not create new kinds of subobjects of a shifted local system on a smooth variety.

**Lemma 5.1.** If \(X\) is smooth connected of dimension \(s\), the subobjects and quotients of \(L[s]\) in \(\operatorname{Perv}(X)\) are exactly the shifted sub-local systems and quotient local systems.

**Proof.** Let \(F\subsetneq X\) be closed and \(T\subset F\) a smooth piece of dimension \(t<s\). The restriction of \(L[s]\) is concentrated in degree \(-s<-t\); its exceptional restriction is concentrated in degree \(s-2t>-t\), by (2.8). The strict-boundary test of Lesson 2, Lemma 3.1, says that \(L[s]\) has no nonzero boundary subobject or quotient.

For a subobject \(Q\subset L[s]\), choose a dense smooth open \(U\) on which \(Q\) and its quotient are shifted local systems. We need to extend the corresponding sub-local system \(M_U\subset L|_U\) to a sub-local system \(L'\subset L\) on all of \(X\). Here is the construction, with the classical and étale inputs separated.

**Classical extension across the boundary.** Put \(F=X\setminus U\). Around each point of \(X\), choose a real coordinate ball \(B\), convex in its coordinates, on which \(L\) is constant with fibre \(V\). If \(s=0\), the boundary is empty and there is nothing to extend. Otherwise \(F\cap B\) has a finite smooth stratification of real dimensions at most \(2s-2\), by the algebraic stratification constructed in Lesson 1, Appendix K. We first prove that \(B\setminus F\) is path connected.

Write \(m=2s\), and fix \(p\in B\setminus F\). An endpoint \(z\) for which the segment from \(p\) to \(z\) meets a stratum \(S\) lies in the image of

\[
S\times[1,\infty)\longrightarrow\mathbf R^m,
\qquad (y,t)\longmapsto p+t(y-p).
\tag{5.0}
\]

Each smooth stratum is covered by countably many coordinate pieces with compact parameter boxes. Restricting also \(t\) to compact intervals makes this a Lipschitz map from a box of dimension at most \(m-1\): its derivative is bounded on a slightly larger compact box, and integration along a segment bounds differences. Such an image can be covered by boxes of arbitrarily small total \(m\)-dimensional volume. Indeed subdivision of a bounded \(d\)-dimensional parameter box into mesh \(\epsilon\) gives \(O(\epsilon^{-d})\) image boxes of side \(O(\epsilon)\), whose total volume is \(O(\epsilon^{m-d})\), tending to zero for \(d<m\). For countably many compact pieces choose the volume budgets \(\delta/2^n\). The union then has a covering of total volume at most \(\delta\), for every \(\delta>0\).

Such a union cannot contain a coordinate ball. To see this without any measure-theoretic transversality theorem, put a closed cube inside that ball and use open covering boxes with total volume less than the cube's volume. Compactness would give a finite subcover. Partitioning along their finitely many coordinate faces shows that the volume of a covered cube is at most the sum of the covering volumes, a contradiction. Consequently the forbidden endpoints for \(p\) have empty interior; the same covering argument applies to the union of the forbidden endpoints for any two fixed points \(p,q\in B\setminus F\). Choose \(z\in B\) outside that union. The two segments \([p,z]\) and \([z,q]\) stay in the convex ball and avoid \(F\). This proves path connectedness.

In the chosen trivialization of \(L\), the image of each fibre of \(M_U\) is a subspace of the same \(V\). These subspaces are locally constant on \(B\setminus F\): on a neighborhood where both local systems are trivial, a sheaf morphism is given by a constant linear map. The connectedness just proved makes the image one fixed subspace \(W_B\subset V\). Thus \(M_U|_{B\setminus F}\) is exactly the constant subsheaf with fibre \(W_B\), and it extends to that constant subsheaf on \(B\).

These extensions agree on overlaps. Around any point of an overlap choose a connected ball \(D\) inside it. The two ambient trivializations differ on \(D\) by a constant invertible matrix. Since \(U\) is dense, \(D\cap U\) is nonempty; there both subspaces describe the given \(M_U\). Their constant descriptions consequently agree on all of \(D\). They therefore glue to a sub-local system \(L'\subset L\), with \(L'|_U=M_U\). The quotient \(L/L'\) is locally the constant quotient \(V/W_B\), so it too is a local system. The same argument proves uniqueness: any extension agrees on the dense open part of every sufficiently small trivializing ball, hence on the whole ball. This constructs the actual subsystem without importing a classification of local systems on an arbitrary variety.

**Étale extension.** In this setting we use the finite-cover correspondence and regular-local-ring normality among the stated algebraic foundations. Every connected finite étale cover of smooth connected \(X\) is regular, hence normal and integral; distinct irreducible components of a normal noetherian scheme are disjoint. Its nonempty dense open preimage of \(U\) remains integral and connected. This implies surjectivity of \(\pi_1(U)\to\pi_1(X)\), as follows. The image \(H\) is closed, since a continuous image of a compact profinite group is compact in a Hausdorff group. If \(H\) were proper, choose \(g\notin H\) and an open normal subgroup \(N\) with \(gN\cap H=\varnothing\). Then \(HN\) is a proper open subgroup. The finite connected cover corresponding to the transitive coset set \(\pi_1(X)/HN\) would become disconnected over \(U\): \(H\) fixes the identity coset and cannot act transitively on this set of more than one element. This contradicts the connectedness just proved. A fibre subspace invariant under \(\pi_1(U)\) is therefore invariant under \(\pi_1(X)\). The lisse representation correspondence supplies \(L'\subset L\) and its lisse quotient. For adic coefficients the correspondence and normalized passage remain the separately identified prerequisites; the finite-cover argument does not prove them.

Now map \({}^pH^0j_!(L'|_U[s])\) into \(Q\). Its image has no boundary quotient, by the left heart adjunction, and no boundary subobject, since it embeds in \(L[s]\). The uniqueness of intermediate extension identifies that image with \(L'[s]\), which satisfies the same two strict tests. The quotient \(Q/L'[s]\) embeds in \((L/L')[s]\) and is supported on \(F\); the strict test makes it zero. This proves the subobject statement. Taking its quotient proves the quotient statement. \(\square\)

**Theorem 5.2.** Every perverse sheaf with field coefficients has finite length.

**Proof.** We prove both chain conditions by induction on dimension. In dimension zero, a strict chain of subrepresentations changes vector-space dimension, so it has finitely many steps. The same holds for a shifted local system on a smooth variety by Lemma 5.1.

For \(P\), choose a dense disjoint smooth open \(U\) on which \(j^*P\) is shifted lisse on each component. Its complement \(F\) has smaller dimension. For any heart object \(R\), the two localization triangles and their perverse cohomology yield

\[
E(R)=i_*{}^pH^0(i^!R)\hookrightarrow R,
\qquad
R\twoheadrightarrow Q(R)=i_*{}^pH^0(i^*R).
\tag{5.1}
\]

The first map is injective because \(Rj_*j^*R\) has perverse degrees at least zero; the second is onto because \(j_!j^*R\) has degrees at most zero. Heart adjunction shows that every boundary subobject factors through \(E(R)\), and every boundary quotient factors through \(Q(R)\). Both objects have finite length by induction on \(F\).

Consider an ascending chain \(P_1\subset P_2\subset\cdots\subset P\). Its restriction to \(U\) stabilizes, since it is a chain of sub-local systems of the fixed finite-rank \(j^*P\). Choose \(n\) after stabilization. All \(P_m/P_n\), \(m\geq n\), are boundary subobjects of the single object \(P/P_n\); they therefore lie in \(E(P/P_n)\). That object has finite length, so this chain, and hence the original chain, stabilizes.

For a descending chain \(P_1\supset P_2\supset\cdots\), choose \(n\) after the open restrictions stabilize. Every quotient \(P_n/P_m\), \(m\geq n\), is supported on \(F\). The quotient map factors through \(Q(P_n)\), so every \(P_m\) contains the fixed kernel of \(P_n\to Q(P_n)\). Their images are a descending chain of subobjects in the finite-length object \(Q(P_n)\); they stabilize. Thus the original chain stabilizes too.

Finally, the ascending chain condition guarantees a maximal proper subobject of any nonzero object: otherwise repeated strict enlargement would contradict that condition. Choose one, then a maximal proper subobject inside it, and continue. The descending chain condition makes this process terminate. The successive quotients are simple, giving a finite composition series. No exactness of intermediate extension has been assumed. \(\square\)

For integral coefficients the failure on a point noted after Theorem 2.1 already prevents this conclusion. The two integral t-structures exchanged by duality in BBD §4.0(a)–(b) should not be identified with the single self-dual field-coefficient heart used here.

## 6. Exercises and solutions

**Exercise 1 (easy: a smooth piece).** Let \(L\) be lisse on a smooth pure \(d\)-dimensional variety. Check its perverse placement and compute the dual.

**Solution.** For the one-piece partition, ordinary and exceptional restrictions are the identity. Both inequalities in (2.2) hold precisely for the degree \(-d\) placement \(L[d]\). Smooth duality gives \(D_XL=L^\vee(d)[2d]\) in the étale setting and \(L^\vee[2d]\) classically. Since duality reverses shifts, the dual of \(L[d]\) is \(L^\vee(d)[d]\), or \(L^\vee[d]\) classically. The Tate twist changes the coefficient representation, not its cohomological placement.

**Exercise 2 (easy: a closed point).** For a closed point \(i:x\hookrightarrow X\), determine the perverse placement, subobjects and dual of a finite-dimensional coefficient representation \(V\) at \(x\).

**Solution.** Open restriction of \(i_*V\) is zero, and \(i^*i_*V=i^!i_*V=V\). The zero-dimensional bounds in (2.4) therefore put it in the heart in degree zero. Any subobject restricts to zero off \(x\), and closed direct image is fully faithful and t-exact. Thus the subobjects are exactly subrepresentations of \(V\); for a geometric point these are all vector subspaces. Proper duality gives \(D_Xi_*V=i_*V^\vee\). Over a nongeometric closed point the Galois action is dualized as well.

**Exercise 3 (medium: detecting a curve object).** Prove the ordinary-cohomology criterion for perversity on a pure reduced curve, and compute the shifted constant complex at a node.

**Solution.** Choose the smooth lisse open and finite boundary as in §3. Perverse upper bounds give ordinary cohomology at most zero and point support in degree zero. In (3.1), the costalk has lower bound zero and the puncture term has lower bound \(-1\), so the stalk has lower bound \(-1\). This leaves \(M=\mathcal H^{-1}K\), \(N=\mathcal H^0K\). Apply point support to \(M[1]\to K\to N\to\): because \(N\) is point supported and the derived support of a sheaf starts in degree zero, its only possibly forbidden group is exactly \(H^0(i_x^!M)\) in (3.2). This proves necessity. Conversely these three properties give the open placement, the closed upper bounds and the vanishing of all negative closed costalk groups by the same exact sequence, proving sufficiency.

For the node the first lesson proves that a small puncture has two branches. The constant section map is the diagonal \(\Lambda\to\Lambda^2\). The actual support fiber consequently has cohomology \(\operatorname{coker}(\Lambda\to\Lambda^2)=\Lambda\) in degree one and the two circle classes \(\Lambda^2\) in degree two. After shifting by one, the costalk has degrees zero and one, while the stalk is \(\Lambda\) in degree \(-1\). All perverse bounds hold. A degree-zero costalk can give a point-supported **perverse** subobject; this does not contradict the absence of point-supported sections of the ordinary sheaf \(\Lambda_X\).

**Exercise 4 (medium: a surface obstruction).** Compute the costalk of the shifted constant complex on two planes meeting only at their origins, and compare it over \(\mathbf Q\) with the cone over a smooth plane cubic.

**Solution.** Each punctured plane retracts to \(S^3\), and they remain disjoint after removing the origin. Their reduced link cohomology has ranks one in degree zero and two in degree three. The shift in (3.3) places these in degrees \(-1\) and \(2\). The first violates the closed-point lower bound, so the shifted constant complex is not perverse. For the cubic cone, the connected link has rational Betti numbers \(1,2,2,1\); reduced degree zero is absent. Formula (3.3) puts the groups of ranks \(2,2,1\) in degrees \(0,1,2\). Perversity holds, but the nonzero first and second link cohomology rule out rational smoothness.

**Exercise 5 (hard: the projective line with one exceptional point).** Classify the classical perverse sheaves on \(\mathbf P^1\) constructible for the strata \(\{0\}\) and \(\mathbf P^1\setminus\{0\}\). Determine all indecomposables and their multiplicities.

**Solution.** The open part is the complex affine line. Straight contraction makes it simply connected, and path transport identifies every local system with a constant space \(V\). Its boundary monodromy is the identity. The global attaching fiber construction of Lesson 2 still applies: its open derived maps are the maps of constant systems, and its boundary complex is \([V\xrightarrow0V]\) in degrees \(-1,0\). The full morphism computation there therefore gives exactly the category

\[
V\xrightarrow uW\xrightarrow vV,\qquad vu=0.
\tag{6.1}
\]

There is no omitted global attachment parameter. In particular the open derived Hom in negative degrees vanishes by the ordinary heart property, and in degree zero it is \(\operatorname{Hom}(V,V')\); the boundary mapping fiber is the one computed in the preceding lesson. Kernels and cokernels are componentwise. The extra invertibility is automatic since \((uv)^2=0\), giving inverse \(1-uv\) for \(1+uv\).

We prove the classification by splitting homogeneous nilpotent chains, rather than assuming a representation-classification theorem. Put \(E=V\oplus W\), with its two summands as a grading, and let \(N\) exchange them by \(u\) and \(v\). The relation implies
\(N^2|_V=0\), \(N^3=0\).
Choose a basis \(z_i\) of \(\operatorname{im}N^2\subset W\), lift it to \(w_i\in W\) with \(N^2w_i=z_i\), and set \(e_i=Nw_i\in V\). These length-three chains are linearly independent. Choose functionals \(\lambda_i\) on \(W\) with \(\lambda_i(z_j)=\delta_{ij}\), \(\lambda_i(w_j)=0\); the independence of the \(w_j,z_j\) permits this. Define

\[
\begin{aligned}
\pi_V(x)&=\sum_i\lambda_i(Nx)e_i,\\
\pi_W(y)&=\sum_i\bigl(\lambda_i(N^2y)w_i+\lambda_i(y)z_i\bigr).
\end{aligned}
\tag{6.2}
\]

Both are identity on the respective chain spaces, and direct substitution using \(N^3=0\), \(N^2|_V=0\) gives \(\pi N=N\pi\). Thus \(\pi\) is a graded projection onto those chains and its kernel is a graded invariant complement. On that complement \(N^2=0\), since its image under \(N^2\) lies both in the chain space and in the kernel.

For the remaining square-zero operator choose a homogeneous basis \(b_j\) of \(\operatorname{im}N\) and homogeneous lifts \(a_j\) in the opposite grade with \(Na_j=b_j\). The \(a_j,b_j\) are independent. Extend the coordinate functionals of the \(b_j\) to homogeneous functionals \(\mu_j\) which vanish on all \(a_j\). The map
\(x\mapsto\sum_j(\mu_j(Nx)a_j+\mu_j(x)b_j)\)
is again a graded projection commuting with \(N\). Its image consists of the length-two chains. Its kernel has \(N=0\) and splits into one-dimensional homogeneous spaces. This proves an exhaustive decomposition into the following blocks:

| Block | Dimensions \((\dim V,\dim W)\) | Arrows |
|---|---|---|
| \(S_V\) | \((1,0)\) | zero |
| \(S_W\) | \((0,1)\) | zero |
| \(E_u\) | \((1,1)\) | \(u=1,\ v=0\) |
| \(E_v\) | \((1,1)\) | \(u=0,\ v=1\) |
| \(P_W\) | \((1,2)\) | \(w_1\xmapsto v e\xmapsto u w_2\), \(v(w_2)=0\) |

The one-dimensional blocks are simple. Either two-dimensional block cannot split because its one nonzero arrow would then have to be zero. A three-dimensional block has \(N^2\ne0\), whereas every block of dimension at most two has square zero; a nontrivial decomposition of this block would force \(N^2=0\). Hence it too is indecomposable. This proves exactly five indecomposable isomorphism classes.

The number of length-three chains is \(r=\operatorname{rank}(uv)\). Subtracting their contributions from \(\operatorname{rank}u\), \(\operatorname{rank}v\), and the two dimensions gives

\[
\begin{aligned}
m_{P_W}&=r,&m_{E_u}&=\operatorname{rank}u-r,&m_{E_v}&=\operatorname{rank}v-r,\\
m_{S_V}&=\dim V-\operatorname{rank}u-\operatorname{rank}v+r,&&
m_{S_W}&=\dim W-\operatorname{rank}u-\operatorname{rank}v.
\end{aligned}
\tag{6.3}
\]

The actual splitting proves these integers nonnegative; their intrinsic expressions also prove uniqueness of the multiplicities. The simple sheaves are \(S_V=\Lambda_{\mathbf P^1}[1]\) and \(S_W=i_*\Lambda\). Every simple diagram has total dimension one, and exact sequences are componentwise, so every diagram has length \(\dim V+\dim W\). This classification is classical: the entire étale category of the affine line in positive characteristic also contains wild nonconstant local systems, and is not the constant-open category (6.1).

## Proof dependencies still requiring closure

The constructions above preserve the assigned classical and étale scope. Their prerequisites must be tracked at that same scope. Lesson 1 contains written classical resolutions, localization, normal-cone geometry, constructible duality and operations in Appendices A–K, and branch geometry in Appendix L; its finite-coefficient image and duality reconstruction is in Appendix M. Lesson 2 supplies the categorical heart, gluing, strict-boundary and attaching-complex proofs. Their own source provenance and transitive proofs remain subject to the course audit.

The finite étale curve bound uses the exact earlier affine-support theorem named in §3, including its strict-local, continuity, algebraic-dimension and curve-cohomology prerequisites. The finite-coefficient operation and exceptional-adjoint foundations used by Lesson 1 are not cleared merely because Appendix M has been written. The normalized adic operations, boundedness, biduality and stalk/derived-limit comparisons remain required unfinished inputs. The étale local-system argument also requires the finite-cover correspondence and the algebraic normality facts used explicitly in Lemma 5.1.

The normal-surface argument is written for a normal analytic germ via bounded holomorphic extension. The equivalence of that formulation with algebraic normality for the assigned algebraic examples needs its analytic-comparison proof. The compact oriented duality and cubic-link calculations must likewise be checked through their exact earlier proofs. The new equalizer argument in §4 removes a separate appeal to general descent of complexes; it still uses the specified operation adjunctions and étale base-change maps. These remaining obligations prevent whole-lesson P514 or source-independence clearance.

## References

- A. Beilinson, J. Bernstein and P. Deligne, with contributions by O. Gabber, [*Faisceaux pervers*, freely readable author-hosted edition](https://publications.ias.edu/sites/default/files/Faisceaux%20pervers.pdf), Astérisque 100 (1982), §§2.1–2.2 and 4.0. Used for the dimension conditions, gluing framework, locality and coefficient distinctions.
- Y. Laszlo and M. Olsson, [*Perverse t-structure on Artin stacks*, free author copy](https://www.cmls.polytechnique.fr/perso/laszlo/articleweb/faisceaux-pervers.pdf), §2. Comparison for the recollement construction and its precise categorical hypotheses.
- M. A. A. de Cataldo and L. Migliorini, [*The decomposition theorem, perverse sheaves and the topology of algebraic maps*](https://arxiv.org/abs/0712.0349), §2.3 and Example 2.5.1. Comparison for finite length, the normal-surface conclusion and the degree of the link contribution.
- J.-P. Demailly, [*Complex Analytic and Differential Geometry*, free author text](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf), 2012 version, Chapter II, §7, especially Theorem 7.3 and Definition 7.4. Used for the analytic normality formulation; its algebraic comparison is not treated as a proof supplied by the citation.
