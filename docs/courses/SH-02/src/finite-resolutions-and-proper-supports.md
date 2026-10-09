# Finite resolutions and proper supports on locally compact spaces

*Written by GPT-6.1 Sol (OpenAI). Self-checked by the writing AI. CC0 1.0.*

A kernel operator integrates along a fibre, so the bound needed for its construction is a compact-support bound on that fibre. No manifold coordinates are necessary when this bound is already known. We establish the resolution criterion, retain the actual proper-support comparisons, and construct the bounded-below right adjoint at this general scope.

<a id="LCH0"></a>

## LCH0. Spaces, sheaves and the coefficient convention

Let all spaces be locally compact Hausdorff. For a sheaf \(E\), sections on a subset mean sections of its inverse-image restriction. A sheaf is **c-soft** if every section on every compact subset extends to a global section. Fix \(d\geq0\). Saying that \(X\) has c-soft dimension at most \(d\) means that every abelian sheaf on \(X\) has an exact c-soft resolution of length at most \(d\).

Let \(k\) be any unital coefficient ring until LCH4 specifies commutativity and finite global dimension. For a continuous map \(f:Y\to X\), \(f_!E\) is the sheaf of sections whose support is proper over the base open. All derived functors below are on the ordinary derived categories of sheaves. We write \(D^+\) for a uniform global lower cohomological bound and use \(H^q(C[s])=H^{q+s}(C)\).

The elementary compact-support proofs in [Duality maps for constructible inverse and direct images](../../constructible-duality-and-infinite-twists/duality-maps-for-constructible-inverse-and-direct-images.html) apply to locally compact Hausdorff spaces before that lesson's manifold applications. Its compact-support section proves finite compact-germ gluing, c-soft restriction and open-extension stability, coproduct stability, injective c-softness, compact-section lifting through a c-soft kernel, and

\[
\begin{gathered}
E\text{ is c-soft}\quad\Longleftrightarrow\\
H_c^q(U;E|_U)=0\\
\quad(U\subset X\text{ open},\ q>0).
\end{gathered}
\tag{LCH0a}
\]

These are the specific preliminary facts used here. In the reverse implication, the closed-open exact sequence for a compact \(K\subset X\) makes the obstruction to extending its section lie in \(H_c^1(X\setminus K;E)\). In the forward implication, compact-section lifting and c-soft quotients make an injective resolution exact after compact sections. Thus the criterion concerns every open subset, rather than ordinary global-section acyclicity. No countable exhaustion or paracompactness is involved.

<a id="LCH1"></a>

## LCH1. The full finite-dimension criterion

**Theorem.** For a locally compact Hausdorff \(X\) and \(d\geq0\), the following are equivalent:

1. Every abelian sheaf on \(X\) has a c-soft resolution of length at most \(d\).
2. For every abelian sheaf \(E\) on \(X\), \(H_c^q(X;E)=0\) for \(q>d\).
3. For every open \(U\subset X\) and every abelian sheaf \(E\) on \(U\), \(H_c^q(U;E)=0\) for \(q>d\).

**Proof.** A finite c-soft resolution consists of compact-section-acyclic terms by LCH0a. It computes compact cohomology by the acyclic-resolution comparison, so condition 1 implies condition 2.

For an open inclusion \(j:U\hookrightarrow X\), extension by zero is exact, preserves c-softness, and gives the natural derived identity

\[
 R\Gamma_c(X;j_!E)=R\Gamma_c(U;E).
 \tag{LCH1a}
\]

To check it, extend an injective resolution on \(U\) by zero. Its terms are c-soft on \(X\), hence compact-section-acyclic; the two compact-section complexes agree term by term. Condition 2 applied to \(j_!E\) therefore gives condition 3.

Assume condition 3 and take an injective resolution \(0\to E\to I^0\to I^1\to\cdots\). Put \(Z^0=E\) and \(Z^{r+1}=I^r/Z^r\). Its constituent sequences are

\[
 0\longrightarrow Z^r\longrightarrow I^r
 \longrightarrow Z^{r+1}\longrightarrow0.
 \tag{LCH1b}
\]

Restriction to an open \(U\) preserves injectives: its exact left adjoint is extension by zero. In particular the restricted \(I^r\) are c-soft and compact-section-acyclic. Their long exact sequences yield, for \(q>0\),

\[
 H_c^q(U;Z^d|_U)
 =H_c^{q+d}(U;E|_U)=0.
 \tag{LCH1c}
\]

The equality denotes the successive connecting isomorphisms. For \(d=0\) the vanishing is condition 3 directly. LCH0a makes \(Z^d\) c-soft, so

\[
\begin{gathered}
0\longrightarrow E\longrightarrow I^0\longrightarrow\cdots\\
\longrightarrow I^{d-1}\longrightarrow Z^d\longrightarrow0
\end{gathered}
\tag{LCH1d}
\]

is the required resolution. When \(d=0\), this says that \(E\) itself is c-soft. This proves condition 1 and the equivalence. \(\square\)

The same bound holds for sheaves of modules over every unital ring. A module-injective sheaf is flabby and hence c-soft also as an abelian sheaf. Forgetting its action therefore identifies its compact-section complex with an acyclic computation of abelian compact cohomology. The abelian bound gives the module bound on every open; the identical dimension shift gives a c-soft resolution in the module category. A bound tested only over one convenient field would not establish this assertion.

<a id="LCH2"></a>

## LCH2. Fibre and product bounds, with the actual comparisons

The proper-image section of the linked duality lesson proves, on locally compact Hausdorff spaces, the actual fibre restriction

\[
\begin{gathered}
(Rf_!B)_x\simeq R\Gamma_c(f^{-1}(x);B|_{f^{-1}(x)})\\
\qquad(B\in D^+(k_Y)).
\end{gathered}
\tag{LCH2a}
\]

Its proof represents \(f_!E\) by the sheaf union of ordinary direct images of relatively compact open extensions. On a stalk, compact-neighbourhood continuity turns this into exactly the compactly supported fibre sections. Restricting an injective resolution gives c-soft terms on the fibre, so the same restriction calculates the derived comparison. In particular, every c-soft sheaf is \(f_!\)-acyclic. The subsequent composition section proves base change and composition by pulling back or retaining those same proper-supported sections; their derived maps inherit the identity and consecutive-comparison compatibilities.

For the projection \(p:S\times T\to S\), if \(T\) has c-soft dimension at most \(d_T\), LCH2a and LCH1 give \(R^qp_!=0\) for \(q>d_T\), on abelian sheaves and on module sheaves. If \(S\) also has bound \(d_S\), the compact-support Leray sequence has terms

\[
 H_c^a(S;R^bp_!E)
 \Longrightarrow H_c^{a+b}(S\times T;E).
 \tag{LCH2b}
\]

The terms vanish for \(a>d_S\) or \(b>d_T\). The bounded-below sequence converges with this finite rectangle of derived-functor indices, so its total degrees exceed at most \(d_S+d_T\). LCH1, applied on the product to every abelian sheaf, proves

\[
 d_{S\times T}\leq d_S+d_T.
 \tag{LCH2c}
\]

The spectral sequence is the one for the composition of compact sections and proper image: proper image sends c-soft injective terms to c-soft sheaves, as the composition proof shows. Thus its acyclicity hypothesis is supplied, and neither a manifold reduction nor exactness of a countable inverse limit is used.

<a id="LCH3"></a>

## LCH3. A universal finite model and the exceptional adjoint

Suppose \(Y\) has c-soft dimension at most \(d_Y\). There is a finite resolution \(L^\bullet\) of \(\mathbb Z_Y\) whose terms are flat and c-soft, whose constituent short exact sequences split on stalks, and for which \(M\otimes_{\mathbb Z}L^p\) is c-soft for every abelian sheaf \(M\).

Here is why the construction in the linked lesson's adjunction section applies at precisely this scope. Set \(C(E)(U)=\prod_{y\in U}E_y\). This sheaf is flabby, and the germ map \(E\to C(E)\) is injective with a stalk retraction obtained by evaluating the coordinate at that stalk's point. Starting with \(E^0=\mathbb Z_Y\), form \(L^p=C(E^p)\), \(E^{p+1}=L^p/E^p\), for \(p<d_Y\), and end with \(L^{d_Y}=E^{d_Y}\). Every stalk remains torsion-free: products and filtered stalk colimits preserve torsion-freeness, and each quotient stalk is a direct summand. Torsion-free abelian groups are flat, by expressing them as filtered unions of finitely generated free subgroups. LCH1 and dimension shift make the last term c-soft.

If \(L\) is flat and c-soft, resolve any \(M\) to the left by sums of open integral constant sheaves. Tensoring preserves exactness; all the middle terms are sums of open extensions of \(L\), hence c-soft. The last \(d_Y\) middle terms and LCH1 give positive compact-cohomology vanishing for \(M\otimes L\) on every open, so LCH0a makes it c-soft. When \(d_Y=0\), every abelian sheaf is already c-soft. This proves the extra tensor property without assuming that the coefficient ring is flat over \(\mathbb Z\).

Stalkwise splitting preserves exactness after tensoring, and the finite length makes all rows of the augmented tensor double complex finite. Therefore

\[
\begin{gathered}
Rf_!G\simeq f_!\operatorname{Tot}(G\otimes_{\mathbb Z}L^\bullet)\\
\qquad(G\in D^+(k_Y)).
\end{gathered}
\tag{LCH3a}
\]

For a term \(L\), the functor \(T_L(M)=f_!(M\otimes_{\mathbb Z}L)\) is exact and preserves coproducts. Exactness follows from flatness and \(f_!\)-acyclicity of all three c-soft terms; the coproduct assertion follows from the fibre formula and finite local summand support on a compact set. For an injective \(k_X\)-sheaf \(I\), the sheaf

\[
 J_L(I)(U)=\operatorname{Hom}_{k_X}(T_L(k_U),I)
 \tag{LCH3b}
\]

represents \(\operatorname{Hom}(T_L(-),I)\). Its sheaf equalizer follows by applying \(T_L\) and injective Hom to the open-cover presentation of \(k_U\). For a possibly noncommutative \(k\), its left action is \(r\cdot h=h\circ T_L(R_r)\), where \(R_r:k_U\to k_U\) is right multiplication by \(r\), a morphism of left module sheaves. This gives \(r\cdot(s\cdot h)=(rs)\cdot h\), preserves restrictions and makes the represented map \(M\to J_L(I)\) a morphism of left \(k\)-module sheaves. Multiplying values in \(I\) by \(r\) would not give that construction. Every sheaf has a two-term presentation by sums of such open generators; naturality on the generators and their relations then proves the representing bijection for every module sheaf. Exactness of this contravariant Hom functor makes \(J_L(I)\) injective.

For a bounded-below injective \(I^\bullet\) representing \(F\), define

\[
\begin{gathered}
J(I)^n=\bigoplus_{p=0}^{d_Y}J_{L^p}(I^{n+p}),\\
(dh)_p=d_Ih_p-(-1)^n h_{p+1}d_L^p.
\end{gathered}
\tag{LCH3c}
\]

The last summand of the differential is zero when \(p=d_Y\). Currying identifies the Hom complex from the model LCH3a into \(I\) with \(\operatorname{Hom}^\bullet(G,J(I))\): the differential's three contributions are \(d_I\), \(-(-1)^n d_G\), and \(-(-1)^{n+i}d_L\) on a degree-\(i\) source component. Formula LCH3c has exactly these signs and squares to zero. There are only \(d_Y+1\) choices of \(p\), so this reindexing uses finite sums even if \(G\) is unbounded above. Both target complexes are bounded-below injective complexes. Degree-zero cohomology of their Hom complexes therefore gives

\[
\begin{gathered}
Rf_!\dashv f^!,\qquad f^!F=J(I),\\
f^!D^{\geq a}\subset D^{\geq a-d_Y}.
\end{gathered}
\tag{LCH3d}
\]

Maps and homotopies of injective representatives give maps and homotopies of \(J(I)\), so this is a functor on \(D^+\). Its unit and counit are the transposes of identities under this bijection. Their triangle identities follow by applying the two inverse transpositions. Different resolution choices produce the unique trace-preserving adjoint comparison; successive choices satisfy the cocycle identity because they transpose the same trace. Proper-image composition then gives the exceptional composition comparison with its ordered counits. These are the actual comparisons used in the kernel adjunction, rather than an unspecified isomorphism of objects.

The construction uses only LCH1's uniform bound on all open subsets, flat integral sheaves, compact-support exactness and enough injectives. The manifold step in the linked lesson was one way to obtain that bound; it is not required here. For a projection with fibre bound \(d_T\), the adjunction improves the lower estimate to \(a-d_T\): if \(E=f^!F\) and \(B=\tau_{\leq a-d_T-1}E\), then \(B\in D^b\), \(Rf_!B\in D^{\leq a-1}\), and \(\operatorname{Hom}(B,E)=\operatorname{Hom}(Rf_!B,F)=0\). The truncation map is zero and is an isomorphism on the lower cohomology sheaves, which forces them to vanish.

<a id="LCH4"></a>

## LCH4. Derived algebra and the projection comparison

Let \(k\) be commutative of finite global dimension \(g\). The linked lesson's tensor–Hom section constructs injectives on arbitrary spaces by products of injective skyscrapers and proves that bounded-below injective complexes are K-injective. It constructs bounded-above K-flat models from sums of open constant sheaves. For a bounded complex in degrees \([a,b]\), good truncation of such a model at \(a-g\) gives a finite flat model: the boundary quotient is a \(g\)-th projective module syzygy on every stalk, hence a flat sheaf. None of these arguments uses manifold coordinates or finitely generated stalks.

The mixed tensor–Hom adjunction required by kernels also follows at the full \(D^+\) test-object range. Choose a finite flat model \(P\) for a bounded kernel \(K\) and a bounded-below injective model \(I\) for the target \(Q\). The complex \(\mathcal Hom(P,I)\) is bounded below with injective terms. For any bounded-below source \(G\), ordinary chain-level currying gives

\[
 \operatorname{Hom}^{\bullet}(P\otimes G,I)
 \simeq\operatorname{Hom}^{\bullet}(G,\mathcal Hom(P,I)).
 \tag{LCH4a}
\]

Only the index of \(P\) is finite. Any products over the unbounded source degrees are retained on both sides and merely reindexed; no stalk or filtered-colimit operation is interchanged with them. The tensor is derived because \(P\) is K-flat, and both Hom targets are K-injective. Degree-zero cohomology gives the desired derived adjunction, with the cochain currying signs. This justifies the kernel argument even when its test object is unbounded above.

For the bounded proper-support projection formula, use the same open-generator flat model of the base input and a finite c-soft model of the source input, supplied by LCH1. Each tensor term is a finite sum of sums of open extensions of c-soft sheaves. It is \(f_!\)-acyclic. The full projection proof in the linked lesson removes the exact left tail using the finite \(f_!\)-dimension bound: its cycles are acyclic by repeated connecting isomorphisms. Consequently applying \(f_!\) termwise computes the derived image. On one open generator the projection map is exactly the proper-support/open-extension comparison; summing and tensoring gives the canonical bounded projection isomorphism. The proof needs only the uniform compact-cohomology bound, finite coefficient global dimension and these support properties, so LCH1 supplies its topological input on the present spaces.

We also construct the actual comparison in both mixed ranges before using truncation to prove it invertible. First let the base input \(N\) be bounded and the source input \(M\) bounded below. Choose a finite flat model \(P_N\) and a bounded-below representative \(G_M\), and put \(A_M=\operatorname{Tot}(G_M\otimes_{\mathbb Z}L)\). Then \(f_!A_M\) computes \(Rf_!M\). Proper-section multiplication defines a chain map

\[
 (f_!A_M)\otimes_k P_N
 \longrightarrow f_!(A_M\otimes_k f^{-1}P_N).
 \tag{LCH4b}
\]

The left side computes the derived left endpoint because \(P_N\) is K-flat. The source on the right computes \(M\otimes_k^Lf^{-1}N\): the fixed pulled-back flat model preserves the quasi-isomorphism \(G_M\to A_M\). Its tensor terms regroup as \((G_M^i\otimes_k f^{-1}P_N^p)\otimes_{\mathbb Z}L^q\), which are c-soft by LCH3. Only finitely many \(p,q\) occur, so this is a bounded-below \(f_!\)-acyclic computation of the right endpoint.

Next let \(M\) be bounded and \(N\) bounded below. Take a finite flat \(P_M\) and the finite complex \(A_M=\operatorname{Tot}(P_M\otimes_{\mathbb Z}L)\). Its terms are flat over \(k\): tensoring a short exact sequence over \(k\) first with \(P_M^p\), then over \(\mathbb Z\) with the flat \(L^q\), is exact. They are also c-soft. Choose the bounded-above open-generator flat replacement \(Q\to f_!A_M\), and a bounded-below representative \(G_N\). The comparison is

\[
\begin{gathered}
Q\otimes_k G_N\longrightarrow(f_!A_M)\otimes_k G_N\\
\longrightarrow f_!(A_M\otimes_k f^{-1}G_N).
\end{gathered}
\tag{LCH4c}
\]

The first endpoint computes \(Rf_!M\otimes_k^LN\) because \(Q\) is K-flat; its possibly infinite direct-sum tensor degrees are retained. The last endpoint computes the derived right side because \(A_M\) is finite K-flat, and its terms regroup as \((P_M^p\otimes_k f^{-1}G_N^i)\otimes_{\mathbb Z}L^q\), hence are c-soft. No flatness of \(f_!A_M\) was assumed.

Both maps use the same multiplication of local coefficient sections with proper-supported sections, with the stated tensor symmetry when the order of factors is changed. They commute with differentials and resolution comparisons. On a common flat and c-soft replacement they give the identical chain map, so their derived classes are independent of choices, natural, and agree with the bounded comparison. The explicit truncation squares and lower estimates in [Composing sheaf operators through an intermediate space](../../sheaf-proof-readings/SH02-kernel-calculus.html#SH02-KER-PF-RANGE) now prove that these particular maps are isomorphisms in the two mixed ranges.

<a id="LCH5"></a>

## LCH5. A noncountable test and the scope of the kernel calculation

An arbitrary discrete space, including an uncountable one, has c-soft dimension zero: a sheaf is a family of modules, restriction to any subset is a projection of that family, and sections extend by zero. Compact subsets are finite. Proper-supported integration along a discrete fibre is therefore direct sum; ordinary direct image is product. Every argument above applies to these spaces without introducing a sequence of compact sets. This example distinguishes finite c-soft dimension from a countability condition.

For a product of the spaces in LCH1, LCH2 supplies the fibre and product dimensions, LCH3 supplies the exceptional adjunction, and LCH4 supplies the coefficient algebra and projection comparison. These are exactly the prerequisites for the original kernel composition, right-adjoint mate, diagonal test and shifted inverse criterion. The spaces retain their general locally compact scope; bounded kernels act on globally bounded-below test objects, with arbitrary stalk modules. A zero coefficient ring is permitted, while equality of distinct cohomological shifts still requires the nonzero-stalk test stated in the kernel lesson.

The classical antecedents are Pierre Schapira's [An Introduction to Sheaves on Grothendieck Topologies, 1 August 2026, §§4.3–4.6 and 4.9](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf). The linked programme lesson gives the compact-support and algebraic constructions, and the arguments here identify the precise general topological bound they require. This is the classical module-sheaf construction; recognition of a separate stable-infinity-categorical sheaf model is a different theorem.
