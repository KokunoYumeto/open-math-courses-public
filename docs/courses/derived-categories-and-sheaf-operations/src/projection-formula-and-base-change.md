# The projection formula and the base change map

*Written and edited by GPT-6.1 Sol (OpenAI), in Codex at Ultra, October 2026. Mathematically self-checked by the writing AI. Original text: public domain (CC0). Authorship and sources are listed in the [course notice](../LICENCE.md).*

The projection formula compares tensoring after pushforward with tensoring before it. Base change compares pullback after pushforward with pushforward after pullback. Each comparison has a canonical direction, supplied by adjunction. Their existence is general; their invertibility needs hypotheses. Keeping these two questions separate prevents a flatness assumption from being mistaken for a universal base-change theorem.

The prerequisites are [Derived pullback and pushforward](derived-pullback-and-pushforward.md), Theorem 1.1, Proposition 1.2, Theorem 2.2, Propositions 3.1–3.2 and 4.2; [Perfect complexes and duals](perfect-complexes-and-duals.md), Lemma 1.1, Corollary 3.3 and Theorems 4.1–4.2; [The derived tensor product and Tor sheaves](derived-tensor-products-and-tor-sheaves.md), Theorems 1.2 and 2.2; and the exact pullback and closed-support arguments in the first lesson's Theorem 4.4 and the support lesson's Proposition 1.1. We use maps into K-injectives from the bounded-derived lesson's Theorem 3.3 and unbounded resolutions from the K-injective lesson's Theorem 4.1.

All structure sheaves are commutative and unital. Objects may be unbounded. Let \(f:X\to Y\) be a morphism of ringed spaces. Every tensor in a derived formula below is over the structure sheaf of the indicated space. Ordinary tensors and functors are expressly distinguished when models are used.

The construction follows the Stacks project authors’ *Cohomology of Sheaves*, “Projection formula” (Tags 01E7, 01E8, 0B54 and 0B55), “The base change map” (Tag 02N7), and the unbounded base-change and composition results, in the [AI Integrated Stacks Project edition](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/cohomology.tex). We prove the local identifications and compatibility diagrams, keeping the existence and invertibility hypotheses explicit. Source attribution appears in the [course notice](../LICENCE.md).
## 1. Finite locally free coefficients

**Lemma 1.1.** If \(V\) is finite locally free and \(I\) is an injective module sheaf on a ringed space, then \(V\otimes I\) is injective. Tensoring a K-injective complex with \(V\) also gives a K-injective complex.

**Proof.** Put \(V^*=\mathcal Hom(V,\mathcal O)\). The ordinary dual-basis evaluation maps give a natural bijection

\[
\begin{gathered}
\operatorname{Hom}(A,V\otimes I)\\
\cong\operatorname{Hom}(A\otimes V^*,I).
\end{gathered}
\tag{1.1}
\]

Indeed, this is the finite free tensor–Hom identity on a trivializing open; the canonical evaluation and coevaluation maps define inverse operations globally, so the local descriptions glue. Both \(V\) and \(V^*\) are flat by the stalk criterion. For a monomorphism \(A\to B\), tensoring with \(V^*\) remains monic. Injectivity of \(I\), followed by (1.1), extends every map \(A\to V\otimes I\) across \(B\). This proves injectivity.

The same degree-zero duality induces a bijection of chain maps modulo homotopy from a complex \(A\) to \(V\otimes I^\bullet\), and from \(A\otimes V^*\) to \(I^\bullet\). An acyclic \(A\) stays acyclic after this exact tensor. The K-injective acyclic test therefore proves the second assertion. The ranks can vary on the space; global constancy of rank was not used. \(\square\)

**Theorem 1.2 (finite coefficient projection).** For a finite locally free sheaf \(V\) on \(Y\) and any \(E\in D(\mathcal O_X)\), there is a natural isomorphism

\[
Rf_*E\otimes V\ \cong\ Rf_*(E\otimes f^*V).
\tag{1.2}
\]

For a module sheaf \(F\) and \(q\ge0\), this induces

\[
\begin{gathered}
R^qf_*F\otimes V\\
\cong R^qf_*(F\otimes f^*V).
\end{gathered}
\tag{1.3}
\]

**Proof.** The ordinary projection map is the adjoint of the tensor of the ordinary counit \(f^*f_*F\to F\) with \(f^*V\). On an open \(W\subset Y\) trivializing \(V\) as \(\mathcal O_W^r\), put \(F_W=F|_{f^{-1}W}\). Its restriction identifies with

\[
(f_W)_*(F_W)^r\longrightarrow(f_W)_*(F_W^r).
\tag{1.4}
\]

It is the identity on each component: the adjoint of each component inclusion is the corresponding counit. Finite sums equal finite products, and pushforward preserves them. Hence (1.4) is an isomorphism. Since the map was globally defined by adjunction, these local isomorphisms prove its global invertibility without choosing compatible trivializations.

Choose a K-injective resolution \(E\to I\). The pullback \(f^*V\) is finite locally free, and Lemma 1.1 makes \(I\otimes f^*V\) K-injective. Its exact tensor represents \(E\otimes f^*V\). Applying the ordinary projection isomorphism termwise gives

\[
f_*I\otimes V\cong f_*(I\otimes f^*V),
\tag{1.5}
\]

which computes both sides of (1.2). All maps are natural in chain maps and homotopies, hence in derived maps through their K-injective representatives. For \(F\) in degree zero use its bounded-below injective resolution; Lemma 1.1 makes the tensor another injective resolution. Flatness of \(V\) commutes its tensor with kernels, images and cohomology, giving (1.3). This proves the source's bounded-below assertion and the stronger unbounded version. \(\square\)

## 2. The general map and perfect coefficients

For any \(E\in D(\mathcal O_X)\), \(K\in D(\mathcal O_Y)\), define

\[
\begin{gathered}
\pi_{f,E,K}:Rf_*E\otimes^L K\\
\longrightarrow Rf_*(E\otimes^L Lf^*K)
\end{gathered}
\tag{2.1}
\]

as the adjoint, under \(Lf^*\dashv Rf_*\), of

\[
\begin{gathered}
Lf^*(Rf_*E\otimes^L K)\\
\cong Lf^*Rf_*E\otimes^L Lf^*K\\
\xrightarrow{\epsilon_f\otimes1}E\otimes^L Lf^*K.
\end{gathered}
\tag{2.2}
\]

Here \(\epsilon_f\) is the derived counit. The proven tensor comparison and the adjunction supply every arrow for arbitrary unbounded inputs. This is a definition of a global map, not an attempt to glue local derived morphisms.

Naturality follows by taking adjoints: in either variable the relevant square transposes to the naturality square of \(\epsilon_f\), with the same tensor identity on the other factor. The same argument proves compatibility with shifts and triangles. More concretely, the resolution functors, tensor cone comparison and adjunction identify the transposes of all three arrows in the cone triangle; they agree with those in (2.2). Thus (2.1) is a morphism of the two triangle-valued functors in \(K\). The map for \(K=\mathcal O_Y\) is the identity of \(Rf_*E\): its transpose is \(\epsilon_f\), exactly the transpose of that identity.

**Theorem 2.1 (perfect projection formula).** If \(K\) is perfect on \(Y\), (2.1) is an isomorphism for every \(E\).

**Proof.** Restrict to an open \(W\subset Y\), replacing \(X\) by \(f^{-1}W\). Proposition 3.2 of the pullback–pushforward lesson identifies the restricted pushforward, while its Theorem 1.1 and Proposition 1.2 identify the restricted pullbacks and tensors. The counit restricts to the same counit by its defining Hom bijection; hence (2.1) restricts to the projection map for \(f_W\).

Now work on a strict-model neighbourhood for \(K\). For \(\mathcal O_Y\) the map is the identity. Finite direct sums preserve that assertion, and naturality with the inclusion and retraction of a finite projective summand makes the map on the summand an isomorphism too. Shifts preserve it by the comparison above. Filter the bounded strict complex by its brutal lower tails. Each successive triangle has one term equal to a finite projective sheaf in one degree. The compatible two triangle sequences, and their long exact cohomology sequences, prove the assertion inductively on its finite number of terms. The cone of (2.1) is consequently zero on an open cover, so all its cohomology sheaves vanish globally. Thus the map is an isomorphism. \(\square\)

This proof does not require \(f\) to be proper, flat, separated or of finite cohomological dimension. Finiteness is in the coefficient \(K\), and it is local finiteness. In particular, a perfect coefficient without a uniform bound on a noncompact target is allowed.

## 3. Closed inclusions with arbitrary coefficients

**Theorem 3.1.** If the underlying map of \(f:X\to Y\) is a homeomorphism onto a closed subset, the projection map (2.1) is an isomorphism for every \(E,K\). The coefficient map need not be flat or an isomorphism.

**Proof.** Identify the underlying space \(X\) with its image \(Z\). At \(y\notin Z\), a neighbourhood disjoint from \(Z\) makes \((f_*F)_y=0\). At \(y=f(x)\), intersections of neighbourhoods in \(Y\) with \(Z\) are cofinal among neighbourhoods in \(X\), so \((f_*F)_y=F_x\), with its action restricted from \(\mathcal O_{Y,y}\). These stalk formulas prove that \(f_*\) is exact and commutes with arbitrary sheaf direct sums: the respective comparison maps are exact or isomorphisms on every stalk. This remains true for arbitrary structure sheaves and their given coefficient homomorphism.

For module sheaves the ordinary projection map is an isomorphism on stalks. Outside \(Z\) both sides vanish; at \(y=f(x)\), with \(R=\mathcal O_{Y,y}\), \(S=\mathcal O_{X,x}\), it is the balanced isomorphism

\[
\begin{gathered}
F_x\otimes_R M_y\\
\longrightarrow F_x\otimes_S(S\otimes_R M_y),\\
e\otimes m\longmapsto e\otimes(1\otimes m).
\end{gathered}
\tag{3.1}
\]

Its inverse sends \(e\otimes(s\otimes m)\) to \(se\otimes m\). Balancing verifies both inverse composites, without flatness.

Choose a K-flat model \(P\) for \(K\), and any representative \(G\) of \(E\). Pullback \(f^*P\) is K-flat. Exactness of \(f_*\) makes the right side of (2.1) represented by \(f_*\operatorname{Tot}(G\otimes f^*P)\), and the left by \(\operatorname{Tot}(f_*G\otimes P)\). The ordinary projection maps in each pair of degrees give a chain isomorphism between them: (3.1) is an isomorphism and \(f_*\) commutes with the totalization's sums.

This is the canonical derived map. To check it, take a K-flat resolution \(Q\to f_*G\). The map \(Q\otimes P\to f_*G\otimes P\) is a quasi-isomorphism. Under the ordinary adjunction the chain projection map, precomposed with this resolution, transposes to the map

\[
f^*Q\otimes f^*P\longrightarrow G\otimes f^*P
\tag{3.2}
\]

from the adjoint \(f^*Q\to G\). That adjoint represents the derived counit: comparing \(G\to I\) with a K-flat resolution of \(f_*I\), and refining the two roofs by the common reading's fraction theorem, gives a commuting-up-to-homotopy square; its adjoint is precisely the counit construction in the pullback–pushforward lesson's Theorem 2.2. Thus (3.2) is (2.2). The isomorphism proved on these models is (2.1). \(\square\)

For a one-point coefficient homomorphism \(R\to S\), this says

\[
E\otimes_R^L K\cong E\otimes_S^L(S\otimes_R^L K),
\tag{3.3}
\]

where on the left \(E\) is regarded as an \(R\)-complex. Even \(R\to R/I\) is allowed. On more general spaces the closed image is what ensures exact pushforward and its stalk description. An open inclusion has different boundary stalks, as Section 5 will demonstrate.

## 4. Base change, flat models and compatibility

Consider a commutative square of ringed spaces

\[
\begin{array}{ccc}
X'&\xrightarrow{g'}&X\\
{\scriptstyle f'}\downarrow&&\downarrow{\scriptstyle f}\\
Y'&\xrightarrow{g}&Y.
\end{array}
\tag{4.1}
\]

Commutative includes the coefficient homomorphisms, not just the continuous maps. The square need not be Cartesian.

**Theorem 4.1 (canonical base change).** For every \(E\in D(\mathcal O_X)\) there is a natural map

\[
b_E:Lg^*Rf_*E\longrightarrow Rf'_*Lg'^*E.
\tag{4.2}
\]

It respects identity squares, horizontal and vertical composition of squares, and the projection maps. If both \(g,g'\) are flat, its construction uses ordinary exact pullbacks, for unbounded as well as bounded-below complexes. These statements construct and compare maps; they assert no general invertibility.

**Proof: definition and naturality.** Let \(A=Lg^*Rf_*E\). Define \(b_E\) to be the adjoint under \(Lf'^*\dashv Rf'_*\) of

\[
\begin{gathered}
Lf'^*A\cong Lg'^*Lf^*Rf_*E\\
\xrightarrow{Lg'^*\epsilon_{f,E}}Lg'^*E.
\end{gathered}
\tag{4.3}
\]

The pullback composition comparison supplies the isomorphism. Naturality of the counit and of this comparison proves naturality of \(b\) for every derived map, by taking its transpose. In particular, no choice of representatives occurs in the definition.

The equivalent pushforward description first takes the unit

\[
E\longrightarrow Rg'_*Lg'^*E,
\]

pushes it through \(Rf_*\), identifies \(Rf_*Rg'_*\) with \(Rg_*Rf'_*\) by composition, and takes its adjoint under \(Lg^*\dashv Rg_*\). To verify equivalence, take that map's further transpose under \(Lf'^*\). Successive Hom bijections identify the composite adjunctions for \(fg'=gf'\); cancel the unit–counit pairs using their triangle identities. What remains is \(Lg'^*\epsilon_{f,E}\), which is (4.3). This also identifies exactly which units are meant in model calculations.

**Proof: flat construction.** Flatness of a ringed-space morphism means that the target-to-source map on each relevant stalk makes the source stalk flat. The stalk formula for pullback then makes \(g^*\) and \(g'^*\) exact, so they compute \(Lg^*,Lg'^*\) on any representatives. Choose \(E\to I\) K-injective and \(g'^*E\to J\) K-injective. Pushforward \(g'_*J\) is K-injective because its left adjoint \(g'^*\) is exact, as proved in Proposition 4.2 of the pullback–pushforward lesson. The ordinary unit followed by the resolution gives a chain map \(E\to g'_*J\). Maps into K-injectives give a unique homotopy class

\[
\beta:I\longrightarrow g'_*J
\tag{4.4}
\]

extending it. Push (4.4) through \(f_*\) and use \(f_*g'_* = g_*f'_*\). Ordinary adjunction gives the chain map

\[
g^*f_*I\longrightarrow f'_*J.
\tag{4.5}
\]

The complexes in (4.5) represent the two sides of (4.2); a homotopy of \(\beta\) induces a homotopy of (4.5). Comparison between K-injective resolutions therefore makes this a well-defined natural derived map. A pullback of an injective was never asserted injective.

Here is a direct check that (4.5) agrees with (4.3). Resolve \(f_*I\) by a K-flat \(Q\). Since \(g\) is flat, \(g^*Q\to g^*f_*I\) is a quasi-isomorphism, and \(g^*Q\) is K-flat. The transpose of (4.5), on that model, is

\[
\begin{gathered}
f'^*g^*Q\cong g'^*f^*Q\\
\longrightarrow g'^*I\longrightarrow J.
\end{gathered}
\tag{4.6}
\]

The first arrow after the isomorphism is \(g'^*\) of the adjoint to \(Q\to f_*I\), hence of the derived counit. The last arrow is adjoint to \(\beta\). Its composite with \(g'^*E\to g'^*I\) is the chosen resolution map to \(J\), up to homotopy, by (4.4). Flatness makes that first map a quasi-isomorphism, so the last arrow represents the required identification with \(Lg'^*E\). Thus (4.6) is exactly (4.3).

For bounded-below \(E\), injective resolutions may be bounded below with injective terms. This specializes to Tag 02N7: **both horizontal maps are flat and the conclusion is a canonical map**. Its proof does not turn a Cartesian square, flat horizontal arrows, or any combination of those conditions into an isomorphism claim.

**Proof: pasting squares.** For any adjunction \(L\dashv R\), the transpose of \(u:A\to RB\) is \(\epsilon_B\circ L(u)\). We use this formula and (4.3). In an identity square (4.3) is a counit, so (4.2) is the identity.

For horizontal pasting, add a square with \(h:Y''\to Y'\), \(h':X''\to X'\) and \(f'':X''\to Y''\). The proposed composite is

\[
\begin{gathered}
Lh^*Lg^*Rf_*E\\
\longrightarrow Lh^*Rf'_*Lg'^*E\\
\longrightarrow Rf''_*Lh'^*Lg'^*E.
\end{gathered}
\tag{4.7}
\]

Transpose under \(Lf''^*\dashv Rf''_*\). The defining equation for the second base-change map replaces its pullback followed by the counit with \(Lh'^*\epsilon_{f'}\). The defining equation for the first then replaces \(\epsilon_{f'}\circ Lf'^*(b_E)\) with \(Lg'^*\epsilon_f\). The result is \(Lh'^*Lg'^*\epsilon_f\), with the coherent pullback-composition identification. This is the transpose for the outer rectangle, proving equality of the maps.

For vertical pasting take \(p:Y\to Z\), \(p':Y'\to Z'\), and \(h:Z'\to Z\), with \(pg=hp'\). The composite first applies base change for \(p\) to \(Rf_*E\), then \(Rp'_*\) to the base change for \(f\). The counit of the composite adjunction \(L(pf)^*\dashv R(pf)_*\), under the composition isomorphisms, is

\[
\begin{gathered}
Lf^*Lp^*Rp_*Rf_*E\\
\xrightarrow{Lf^*\epsilon_p}Lf^*Rf_*E\\
\xrightarrow{\epsilon_f}E.
\end{gathered}
\tag{4.8}
\]

This formula follows by composing the two Hom adjunction bijections: the identity of the composed right-adjoint value transposes successively through those two counits. Transposing the proposed pasted map uses the same two factors, pulled back through \(g'\). It is therefore the transpose (4.3) for the rectangle. This proves vertical pasting without an omitted diagram verification.

**Proof: projection compatibility.** Fix \(K\in D(\mathcal O_Y)\). The two routes from

\[
Lg^*(Rf_*E\otimes^L K)
\]

to

\[
Rf'_*(Lg'^*E\otimes^L Lf'^*Lg^*K)
\tag{4.9}
\]

are as follows. One pulls back \(\pi_f\), applies base change to \(E\otimes^L Lf^*K\), then uses tensor and pullback composition. The other uses tensor compatibility first, applies \(b_E\otimes1\), then \(\pi_{f'}\). Transpose both under \(Lf'^*\). On the common source model the first route is \(Lg'^*\epsilon_{f,E}\otimes1\), with the coefficient factor \(Lg'^*Lf^*K\). The second uses

\[
\epsilon_{f',Lg'^*E}\circ Lf'^*(b_E)
=Lg'^*\epsilon_{f,E},
\tag{4.10}
\]

which is precisely (4.3)'s defining transpose equation, and then tensors the same coefficient identity. The two transposes agree globally, proving compatibility. All tensor reassociations here are the coherent ones established earlier. No invertibility of \(b_E\) was needed. \(\square\)

Projection maps also compose for \(X\xrightarrow fY\xrightarrow pZ\). First apply \(\pi_p\) to \(Rf_*E\) and \(K\), then \(Rp_*\pi_f\) with coefficient \(Lp^*K\). Their transpose under the composite pullback is the tensor of (4.8) with \(L(pf)^*K\), hence is the transpose of \(\pi_{pf}\). The maps are equal by adjunction. This observation and Theorem 4.1 ensure that iterating these constructions changes neither their direction nor their definition.

## 5. Two boundary failures and a coefficient calculation

Let \(Y=\{0\}\cup\{1/n:n\ge1\}\) have its subspace topology in \(\mathbb R\), let \(U=Y\setminus\{0\}\), and let \(j:U\hookrightarrow Y\). Give both spaces the constant coefficient sheaf \(k\), for a field \(k\). Every point of \(U\) is isolated. A sheaf there is a family of vector spaces, and its sections on an open are their product. Products of vector-space short exact sequences are exact: choose a preimage in each component to prove surjectivity; kernels are componentwise. Consequently \(j_*\) is exact on these sheaves, and its derived functor is computed on any complex by ordinary pushforward.

Take \(F=k_U\). At the boundary point the neighbourhoods contain all sufficiently large \(n\), so

\[
\begin{gathered}
(j_*F)_0=\varinjlim_N\prod_{n\ge N}k\\
\cong\left(\prod_{n\ge1}k\right)\Big/\left(\bigoplus_{n\ge1}k\right).
\end{gathered}
\tag{5.1}
\]

Indeed, extending a tail by zero proves surjectivity from the full product to this colimit, and a sequence dies exactly when a tail is zero, equivalently when its support is finite. Write this quotient as \(A\); the class of the constant sequence one is nonzero.

**Failure with a flat infinite coefficient.** Put \(K=\bigoplus_{m\ge1}k_Y\), in degree zero. It is flat, but not perfect, since its stalk at any point is an infinite-dimensional vector space and Proposition 2.2 of the perfect lesson says a perfect module is of finite type. All derived tensors in this example are ordinary. The projection map at zero is

\[
\begin{gathered}
A\otimes_k\left(\bigoplus_{m\ge1}k\right)\\
\longrightarrow\varinjlim_N\prod_{n\ge N}\left(\bigoplus_{m\ge1}k\right).
\end{gathered}
\tag{5.2}
\]

An element on the left uses only finitely many coordinate indices \(m\), uniformly over its sequence entries. On the right take the sequence whose \(n\)-th value is the \(n\)-th basis vector \(e_n\). It is a valid section on the discrete \(U\). No tail of that sequence has its values in a fixed finite coordinate subspace. Hence its germ is not in the image of (5.2), and the projection map is not an isomorphism, even in degree zero. The failure is about finite coefficients, not about flatness: this coefficient is flat, and there is no higher-cohomology complication hiding the failure.

**Failure in a Cartesian flat square.** Base change the same open inclusion along \(g:\{0\}\hookrightarrow Y\), with coefficient \(k\) at the point. The Cartesian top-left space is empty, so \(g':\varnothing\to U\) and \(f':\varnothing\to\{0\}\). The stalk coefficient map for \(g\) is \(k\to k\), hence flat; \(g'\) is flat vacuously. For \(F\), (4.2) becomes

\[
A[0]\longrightarrow0.
\tag{5.3}
\]

This is not an isomorphism because \(A\ne0\). Thus both flat horizontal maps and a Cartesian square still do not imply base change for arbitrary ringed spaces and pushforward. Every hypothesis has been checked in this example; no appeal to a vague exceptional topology is needed.

The contrast with restriction to an open is instructive. If \(g:V\hookrightarrow Y\) is open and \(X'=f^{-1}V\) has restricted coefficients, the base-change map is an isomorphism. On a K-injective \(I\), restriction to \(X'\) remains K-injective, and the two sides are literally the complexes

\[
(f_*I)|_V=(f_V)_*(I|_{X'}).
\tag{5.4}
\]

Their section values on every smaller open coincide. The map (4.3) gives this same equality: its transpose is the restricted counit. This is precisely Proposition 3.2 of the pullback–pushforward lesson. Replacing an open neighbourhood by a boundary point removes the sectionwise equality that proves (5.4), which explains (5.3).

**A nonflat closed coefficient map.** On one-point spaces take \(R=\mathbb Z\), \(S=\mathbb Z/2\), \(E=S\), and \(K=\mathbb Z/2\). The free resolution \(\mathbb Z\xrightarrow{2}\mathbb Z\) in degrees \(-1,0\) represents \(K\). Its scalar extension is \(S\xrightarrow{0}S\). Thus both sides of (3.3) have one copy of \(S\) in each of degrees \(-1,0\), and the projection isomorphism is the identity on those copies. Replacing derived pullback by ordinary pullback would lose the negative cohomology. Closedness guarantees this projection formula even though the coefficient map is nonflat; it does not erase its Tor groups.

Continue with [Quasi-coherent sheaves and concentrated scheme maps](quasi-coherent-sheaves-and-concentrated-maps.md) for the scheme projection and flat-base-change proofs. After its Sections 1–2, return to [the inverse-limit lesson, Theorem 6.2](inverse-limits-and-unbounded-resolutions.md#finite-affine-cover-bound), for the finite affine-cover product bound.

## 6. Exercises with checked solutions

**Exercise 1 (easy: pushforward to a point).** Let \(f:X\to\{*\}\) have coefficient ring \(R\) at the point. Show the projection formula for \(K=R^r\), with \(r\) finite, directly on a K-injective model. Explain why this calculation does not justify arbitrary infinite free coefficients.

**Solution.** For \(E\to I\) K-injective, \(Lf^*R^r=\mathcal O_X^r\), and \(I^r\) is K-injective: finite Hom groups split into finite products, so the acyclic test vanishes in each component. Sections commute with finite direct sums, which are finite products. Both sides are therefore represented by \(\Gamma(X,I)^r\), and the map is the identity in every degree and on each component. For infinite rank a tensor uses a sheaf direct sum. Its section functor need not commute with that sum, and its pushforward at a boundary may include families with coordinate support varying without a common finite bound. Formula (5.2) supplies a checked counterexample to exactly that inference. The finite proof uses finiteness twice, in the direct-sum identity and in the coefficient dual.

**Exercise 2 (medium: more general degree-zero coefficients).** Extend (1.3) to a locally finite projective sheaf \(V\) that need not be finite locally free. State the needed ring hypothesis, and check independence of the chosen splitting.

**Solution.** The rings remain commutative, but their stalks need not be local. On an open neighbourhood choose \(V\) as a summand of \(\mathcal O^r\), with inclusion \(a\) and retraction \(b\). The ordinary projection maps commute with \(a,b\) because they are defined by the counit and tensor functoriality. Their map on the finite power is an isomorphism; restricting it and its inverse to the summand therefore gives an isomorphism on \(V\). The global projection map is already defined by adjunction, so a second splitting gives the same map, rather than a new choice of gluing data. The pullback remains locally finite projective and flat. Its ordinary duality gives (1.1), hence preserves injectives; alternatively this follows locally from finite projective dual bases, with globally canonical maps. Applying these facts to an injective resolution gives (1.3) on every member of the cover, hence globally. This includes the nonfree module \((1,0)(k\times k)\) on the one-point example in the perfect lesson.

**Exercise 3 (medium: a two-term strict model).** Prove the projection formula for \(K=(P^{-1}\xrightarrow dP^0)\), where both terms are finite projective. Specify the triangle and the comparison that is used; a reference to “devissage” alone is insufficient.

**Solution.** Inclusion of the top term gives the triangle

\[
\begin{gathered}
P^0[0]\longrightarrow K\longrightarrow P^{-1}[1]\\
\longrightarrow P^0[1].
\end{gathered}
\tag{6.1}
\]

It comes from the degreewise split short exact sequence of the brutal tails, using the common reading's cone convention. Apply the exact functors \(Rf_*E\otimes^L-\) and \(Rf_*(E\otimes^L Lf^*(-))\). Naturality and triangle compatibility of (2.1) give a map between these triangles, including their last arrows. The maps on \(P^0\) and \(P^{-1}[1]\) are isomorphisms by the finite-power, summand and shift cases. The long exact cohomology sequences then give an isomorphism on the middle object: injectivity follows by lifting a zero image to the preceding term and cancelling its isomorphic counterpart; surjectivity follows by lifting the following-term image and correcting by the preceding-term image. Thus the middle cone is acyclic. This proves the two-term case for any differential, rather than only for a split complex.

**Exercise 4 (hard: a global duality proof).** Give a second proof of Theorem 2.1 using perfect duality and the derived adjunction, without choosing a global strict model for \(K\).

**Solution.** Pullback preserves the evaluation, coevaluation and their identities, because it is a monoidal functor with coherent comparisons. Hence \(Lf^*(K^\vee)\) is the dual of \(Lf^*K\); uniqueness of the dual identifies it with \((Lf^*K)^\vee\). Write \(A=Rf_*E\), \(P=Lf^*K\), and \(T_X=Lf^*T\). For every \(T\in D(\mathcal O_Y)\), the dual and pullback adjunctions give successive natural bijections

\[
\begin{gathered}
\operatorname{Hom}(T,A\otimes K)\\
\cong\operatorname{Hom}(T\otimes K^\vee,A)\\
\cong\operatorname{Hom}(T_X\otimes P^\vee,E)\\
\cong\operatorname{Hom}(T_X,E\otimes P)\\
\cong\operatorname{Hom}(T,Rf_*(E\otimes P)).
\end{gathered}
\tag{6.2}
\]

The tensor symbols in this calculation are derived. The first bijection evaluates the coefficient dual, and the third inserts its coevaluation; the inverse operations use the other two maps and their triangle identities. The middle bijection uses the counit of \(f\), and pullback identifies the dual data just described. Composing the operations, the dual evaluation–coevaluation pairs cancel. The resulting map on Hom groups is composition with the map whose pullback transpose is \(\epsilon_f\otimes1\). By (2.2), that map is exactly \(\pi_{f,E,K}\). Thus composition with \(\pi\) is a bijection for all \(T\). With \(T\) equal to its target, surjectivity supplies a right inverse; with \(T\) equal to its source, injectivity makes that right inverse also a left inverse. This proves the canonical map is an isomorphism globally. It also explains why no uniform bound or global free presentation was necessary.

**Exercise 5 (medium: Cartesian flat change on one-point spaces).** Let \(R\to B\) and a flat homomorphism \(R\to R'\) be given, and let \(B'=B\otimes_RR'\). Form the square of one-point ringed spaces with these coefficient rings. Prove that its base-change map is an isomorphism for every unbounded \(B\)-complex, and explain why this does not contradict (5.3).

**Solution.** Both pushforwards are restriction of scalars, hence exact. The map \(B\to B'\) is flat: for a short exact sequence of \(B\)-modules, tensoring with \(B'\) over \(B\) identifies with tensoring the same underlying \(R\)-sequence with the flat \(R'\). Thus both horizontal pullbacks are exact. For any complex \(E\), the two base-change values are represented by \(R'\otimes_RE\) and \(B'\otimes_BE\). Their canonical balanced isomorphism sends \(r'\otimes e\) to \((1\otimes r')\otimes e\), with inverse \((b\otimes r')\otimes e\mapsto r'\otimes be\). It commutes with differentials. The counit for restriction and extension of scalars is multiplication, so its transpose is precisely this balanced map. Theorem 4.1 therefore identifies it with base change. These particular pushforwards have no boundary-section phenomenon. Flatness is sufficient in this coefficient-only situation, while the topological example (5.3) has nonzero boundary germs over an empty fibre. Neither example licenses replacing the other's hypotheses.

**Exercise 6 (hard: a nonflat algebraic square).** In the preceding square take \(R=\mathbb Z\), \(B=R'=B'=\mathbb Z/2\), and \(E=B[0]\). Compute the general derived base-change map and compare it with ordinary pullback.

**Solution.** The lower horizontal coefficient homomorphism \(\mathbb Z\to\mathbb Z/2\) is not flat: tensoring the injection \(2:\mathbb Z\to\mathbb Z\) makes it zero. The upper horizontal homomorphism \(B\to B'\) is the identity, hence flat. The source of (4.2) is \((\mathbb Z/2)\otimes^L_{\mathbb Z}(\mathbb Z/2)\), represented by \(B\xrightarrow0B\) in degrees \(-1,0\); the target is \(B[0]\). The transpose description is scalar-extension multiplication. On this model it is the identity on degree zero and zero on degree \(-1\), so it is the usual augmentation. It induces an isomorphism on \(H^0\) but kills the nonzero \(H^{-1}=B\). Thus it is not a quasi-isomorphism. Ordinary pullback would keep only the degree-zero tensor and obscure the failure. The square is Cartesian with the ordinary tensor coefficient ring, but that ring records no derived Tor correction. Theorem 4.1 supplies the comparison, while the calculation states exactly why it is not invertible.
