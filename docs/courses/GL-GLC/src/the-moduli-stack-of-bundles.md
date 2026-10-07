# The moduli stack of bundles

*Draft. CC0 1.0.*

A bundle can have many automorphisms while admitting few deformations. A moduli stack records both. This is why its dimension can be negative, why the dimension of a coarse moduli space is a different calculation, and why its cotangent stack is a space of Higgs fields rather than an ordinary vector bundle of constant rank.

Throughout, \(X\) is a smooth projective connected curve over an algebraically closed field \(k\) of characteristic zero. Its genus is \(g\). The group \(G\) is connected reductive. We impose \(g\ge2\) only where it is needed and say so explicitly. A principal bundle is a right \(G\)-torsor; write \(\operatorname{ad}(P)=P\times^G\mathfrak g\) for its adjoint vector bundle. Complexes are cohomologically graded, so \(V[1]\) puts a vector space \(V\) in degree \(-1\).

Sections 1–2 construct the bundle stack and prove its deformation theory and Euler-characteristic formula. Serre duality on a curve is used later for the cotangent calculation. The [previous lesson](from-automorphic-functions-to-automorphic-sheaves.md) constructed bundles from lattices and identified the elementary Hecke fibres. Here we examine the stack on which those correspondences act.

## 1. The moduli problem, including its arrows

For a \(k\)-scheme \(S\), the groupoid \(\operatorname{Bun}_G(S)\) consists of \(G\)-torsors on \(X\times S\) and their isomorphisms. Pullback in \(S\) makes this a stack for the fppf topology: torsors, their actions, and their isomorphisms satisfy faithfully flat descent. For \(G=GL_n\), the associated standard representation identifies this groupoid with rank-\(n\) vector bundles. For \(G=\mathbb G_m\), it is the groupoid of line bundles, usually called the Picard stack.

Sections 7.1–7.7 prove formal-disc gluing, effective fppf descent of affine schemes and equivariant algebras, affineness of torsors under affine groups, and the scheme-theoretic torsor/vector-bundle dictionary. Passage from an affine cover to an arbitrary fppf family uses the explicitly linked earlier scheme-topological proofs in §7.5. Sections 1.1–1.6 supply the bundle-stack atlas, affine diagonal and formal effectivity; the remaining recursive foundations are specified in §6.4.

Sections 1.1–1.6 prove that \(\operatorname{Bun}_G\) is an algebraic stack locally of finite type over \(k\), with affine finitely presented diagonal, and prove effectivity of formal bundle families over complete Noetherian local coefficient rings. The proof constructs a smooth atlas from framed quotients and schemes of reductions. [Heinloth, Proposition 1] is a freely accessible reference for the classical algebraicity statement. Section 2 gives the deformation, smoothness and dimension calculation.

The diagonal is affine and of finite type. Here is a way to understand this assertion. Given two bundles \(P,Q\) over \(X\times S\), their isomorphism functor is the functor of sections of the affine \(X\times S\)-scheme \(\operatorname{Isom}_G(P,Q)\). Work locally on \(S\). An affine scheme of finite presentation over \(X\times S\) can be presented inside a vector bundle by finitely many equations, using a sufficiently ample twist to produce generators and relations. The section functor of that vector bundle is affine: it is represented by the degree-zero linear stack of \(R\pi_*V\), or directly by the linear equations in a two-term finite locally free presentation of that complex. Imposing the finitely many algebraic relations gives a closed affine subscheme. This represents the isomorphism functor.

For vector bundles the equations are particularly concrete. A pair of homomorphisms \(u:E\to F\) and \(v:F\to E\) is an isomorphism with its inverse precisely when \(vu=1_E\) and \(uv=1_F\). These are closed equations in the affine section functors of the two Hom bundles. Keeping the inverse as a variable explains affineness without asserting that every arbitrary open subscheme of an affine scheme is affine.

Local finite type does not mean that there is a single finite type space of all bundles. Degree and instability both produce unbounded families. We will distinguish them carefully.

### 1.1. Finite cohomology coordinates and all parameter changes

We begin with the parameter spaces needed for the diagonal and the atlas. Fix a very ample line bundle \(A\) on \(X\), and write \(F(m)=F\otimes A^m\). Here and below, finite presentation refers to the coefficient scheme as well as to the sheaf.

The earlier [*Algebra and sheaf cohomology before reductive groups*](../../AG-RG/AG-RG-S01.html), §§4–5 and 8, proves affine Čech cohomology, projective coherent finiteness, generation by high twists and Serre vanishing. Lemma 5.1 of [*Projective cohomology and smooth affine models*](../../AG-RG/AG-RG-S02.html) proves the following algebraic step: a bounded complex of flat modules over a Noetherian ring, with finite cohomology, has a finite projective replacement which remains a quasi-isomorphism after tensoring with every module.

To apply it, let \(Z\) be projective over a Noetherian affine base \(\operatorname{Spec}R_0\), and let \(F\) be coherent and flat over \(R_0\). Choose a finite affine cover of \(Z\). Its intersections are affine since \(Z\) is separated. The section module of \(F\) on every such intersection is \(R_0\)-flat: tensor an injection of base modules with \(F\), test exactness at every stalk, and then take sections on that affine intersection. The cover complex has flat terms, finite cohomology and commutes with every base tensor. The replacement therefore gives
\[
 \begin{gathered}
 K\simeq C^\bullet(Z,F),\\
 H^i(K\otimes_{R_0}M)
   =H^i\!\left(C^\bullet(Z,F)\otimes_{R_0}M\right).
 \end{gathered}
 \tag{BA.1}
\]
for every \(R_0\)-module \(M\). The interval of \(K\) is the interval of the cover complex, so it starts in degree zero.

For the fixed curve we can use just two affine opens. In its fixed projective embedding choose one hyperplane not containing the curve; its intersection with the curve is finite. A second hyperplane avoids that finite set, since \(k\) is infinite. The two affine hyperplane complements cover \(X\), and their intersection is affine. The same is true after every coefficient change. Their Čech complex is concentrated in degrees zero and one, proving that the curve has no higher coherent cohomology and giving \(K\) in those same two degrees.

For a vector bundle on \(X_R\), with arbitrary coefficient algebra \(R\), this construction is available after a finite-presentation model. Indeed, on each member of a fixed finite affine cover of \(X\), its module is the image of a finite idempotent matrix. The idempotents, the gluing maps and their inverses involve finitely many coefficients of \(R\); their equations descend to a finitely generated \(k\)-subalgebra \(R_0\subset R\). Rank \(r\) descends too: the idempotent has trace \(r\), and in characteristic zero this equality forces rank \(r\) at every field-valued point of the model. Thus these data give a vector bundle on \(X_{R_0}\). Tensor its complex in (BA.1) with \(R\). This computes the original bundle's cohomology after every coefficient change.

If all positive fibre cohomology vanishes near a parameter point, cancel each invertible differential entry of \(K\), using row and column operations. The equation \(d^2=0\) separates the corresponding contractible pair. After finitely many cancellations, all remaining differential entries vanish at the point. Their fibre terms are then the fibre cohomology, so all positive terms have rank zero; only degree zero remains. The cancellations persist after every tensor. This proves, on that neighbourhood,
\[
 \begin{gathered}
 V=\pi_*F\text{ finite locally free},\qquad
 R^i\pi_*F=0\quad(i>0),\\
 V\otimes_R B\simeq H^0(X_B,F_B)
       \quad\text{for every }R\text{-algebra }B.
 \end{gathered}
 \tag{BA.2}
\]
The vanishing locus is open by the same cancellation argument. The Euler characteristic is the alternating sum of the finite-projective ranks, hence locally constant.

For two vector bundles \(E,F\), apply (BA.1) to \(E^\vee\otimes F\). Locally on the coefficient base, its section functor is the kernel of the first differential of a complex of finite free modules. Writing that differential as \(d:K^0\to K^1\), the functor is represented by
\[
 \underline{\operatorname{Hom}}_X(E,F)
 =\operatorname{Spec}
 \left(\operatorname{Sym}_R((K^0)^\vee)/
       \bigl(d^\vee((K^1)^\vee)\bigr)\right).
 \tag{BA.3}
\]
The equations are linear, and remain the right equations after every tensor by (BA.1). These affine schemes glue because they represent the same functor on overlaps; the result is affine and finitely presented over the coefficient scheme.

Composition is a morphism between these represented Hom functors, obtained by composing their universal homomorphisms. In the product of the two Hom schemes impose
\[
 (u,v):\quad u:E\to F,\quad v:F\to E,\qquad
 vu=1_E,\quad uv=1_F.
 \tag{BA.4}
\]
The identity sections in the two affine finitely presented endomorphism schemes are closed immersions of finite presentation. Hence (BA.4) defines an affine finitely presented scheme. Its points are isomorphisms and their unique inverses, so it represents \(\underline{\operatorname{Isom}}_X(E,F)\), including all nonreduced coefficient changes.

### 1.2. A smooth atlas made from framed quotients

Fix rank \(r\geq1\) and degree \(d\), and set \(a=\deg A\). The Riemann–Roch calculation in §6.4 gives
\[
 P(t)=rat+d+r(1-g),\qquad N=P(m)>0.
 \tag{BA.5}
\]
Consider quotients \(\mathcal O_X(-m)^N\twoheadrightarrow E\) with polynomial \(P\). The representability construction in [*Hilbert and Quot schemes*](../../AG-HP/src/hilbert-and-quot-schemes.md), Theorem 4.1, §4, gives their finite-type scheme \(Q_m\). We use its locally closed Grassmannian/flattening construction. Its uniform kernel bound is proved in [*Regularity and bounded families*](../../AG-HP/src/regularity-and-bounded-families.md), Theorem 4.1, and its stabilized Fitting equations in [*Flattening stratifications*](../../AG-HP/src/flattening-stratifications.md), Theorem 6.1. The flat projective cohomology needed by that construction is exactly (BA.1)–(BA.2). The later valuative proof of projectivity of \(Q_m\) is unnecessary for this atlas.

Fibre cohomology is unchanged by a field extension, as follows by tensoring the affine cover complex. Thus the polynomial (BA.5), including its genus and geometric determinant degree, is the same over arbitrary parameter residue fields.

Take the open locus where the universal quotient is a vector bundle of rank \(r\). Here is the fibre-to-family check for that openness. Over the Noetherian universal base, at a point of a fibre where the quotient is free, lift a fibre basis to a map from a finite free module. Nakayama makes that map surjective near the point. Since the quotient is flat over the parameter base, its kernel remains exact on the residue field; that fibre kernel vanishes. The kernel is finite, so Nakayama makes it zero after shrinking. Thus freeness holds on a source neighbourhood. The complement of the resulting vector-bundle locus is closed; its image in the parameter scheme is closed by projectivity of \(X\). Removing that image gives the required open coefficient locus. Rank \(r\) is checked by the same finite presentations.

On it further require \(H^1(X_s,E_s(m))=0\) and that the section map of the universal quotient be an isomorphism:
\[
 R^N\xrightarrow{\ \sim\ }\pi_*E(m),\qquad
 \mathcal O_{X_R}(-m)^N\twoheadrightarrow E.
 \tag{BA.6}
\]
These are open conditions. The first uses (BA.2); the second is the nonvanishing determinant of a map between rank-\(N\) locally free modules. Call the resulting finite-type open scheme \(V_{r,d,m}\). Its universal quotient defines a map to \(\operatorname{Bun}_{GL_r}\).

For any vector bundle \(E\) over an arbitrary parameter scheme \(T\), let \(T_{d,m}\subset T\) be the open locus where it has degree \(d\), is generated after twist \(m\), and has no positive fibre cohomology after that twist. Generation is open: the evaluation cokernel is finite, and properness removes the image of its support. This argument is made on a Noetherian model and then pulled back; (BA.2) provides the section module and arbitrary base change. The fibre product with \(V_{r,d,m}\) is precisely the frame scheme of \(\pi_*E(m)\):
\[
 \begin{array}{ccc}
 \operatorname{Fr}(\pi_*E(m))
    &\longrightarrow&V_{r,d,m}\\
 \downarrow&&\downarrow\\
 T_{d,m}&\longrightarrow&\operatorname{Bun}_{GL_r}.
 \end{array}
 \tag{BA.7}
\]
It is a \(GL_N\)-torsor over \(T_{d,m}\), so is smooth and surjective there. A basis of sections gives the evaluation quotient; conversely (BA.6) recovers exactly that basis. An automorphism preserving the quotient is the identity since the quotient is surjective. Thus (BA.7) is an equality of the full fibre-product functors.

Serre generation and vanishing ensure that every fibre belongs to \(T_{d,m}\) for some \(m\geq0\). Degree is locally constant by (BA.1) and the vector-bundle Riemann–Roch formula. The fibre loci therefore cover every parameter scheme. We obtain a representable smooth surjection
\[
 \coprod_{\substack{d\in\mathbf Z,\ m\geq0\\P(m)>0}}
        V_{r,d,m}\longrightarrow\operatorname{Bun}_{GL_r}.
 \tag{BA.8}
\]
The source is a scheme locally of finite type over \(k\). Effective vector-bundle descent is §7.5, and its diagonal is the affine finitely presented Isom scheme (BA.4). These establish algebraicity and local finite type of the vector-bundle stack directly.

### 1.3. A schematic line stabilizer and its homogeneous space

We need a projective-coordinate description of a principal-bundle reduction. We construct it for the present smooth affine \(G\).

Every element of a field comodule is contained in a finite-dimensional subcomodule. To verify this, express its coaction using linearly independent coefficients in the Hopf-algebra factor. Coassociativity, followed by linear functionals selecting those coefficients, shows that the finitely many coefficients in the vector factor span a subcomodule containing the original element. Apply this to finitely many algebra generators of \(k[G]\). Right translation gives a finite-dimensional representation containing those generators. Evaluation at the identity expresses each generator as a matrix coefficient of that representation; the antipode supplies the inverse matrix. Thus the matrix-coordinate map onto \(k[G]\) is surjective, giving a faithful closed representation
\[
 j:G\hookrightarrow K=GL_n.
 \tag{BA.9}
\]

Let \(J\subset k[K]\) be its ideal. Choose a finite-dimensional right-translation subcomodule \(V\subset k[K]\) containing generators of \(J\), and put \(W=J\cap V\). For every test \(k\)-algebra \(B\), this intersection commutes with tensoring by \(B\), since \(B\) is flat over the field. Right translation by \(G(B)\) preserves \(W_B\). Conversely, an element of \(K(B)\) preserving \(W_B\) preserves the ideal generated by it, which is \(J_B\), and the same holds for its inverse. It therefore sends \(G_B\) onto itself by right translation. Applying this translation to the identity shows that the element lies in \(G(B)\). We have proved the scheme-theoretic identity
\[
 \operatorname{Stab}_K(W)=G.
 \tag{BA.10}
\]

Put \(b=\dim W\), \(\mathcal W=\bigwedge^bV\), and \(D=\bigwedge^bW\). The stabilizer of this line is the stabilizer of \(W\), on every test ring. In a basis whose first \(b\) vectors span \(W\), preservation of the wedge line says that the first square minor is a unit; the minors replacing one row make the lower-left block zero after multiplying by its inverse. Thus the matrix maps \(W_B\) isomorphically onto itself. This also covers \(b=0\), when the wedge line is the trivial representation. Consequently
\[
 D\subset\mathcal W,\qquad
 \operatorname{Stab}_K([D])=G
 \quad\text{in }\mathbf P_{\mathrm{lines}}(\mathcal W).
 \tag{BA.11}
\]
Here the projective space parametrizes lines, equivalently rank-one quotients of \(\mathcal W^\vee\).

The orbit \(O=K[D]\) is locally closed with its reduced scheme structure by [*Group schemes over a field*](../../AG-GS/src/group-schemes-over-a-field.md), Theorem 7.1 and its written constructible-image proof. We check that this reduced orbit has the full quotient structure needed here. It is integral because it is the image of the integral group \(K\).

Here is the nonempty smooth open used in this check. On an integral affine chart \(\operatorname{Spec}B\), [*Krull dimension and Noether normalization*](../../AG-CA/src/krull-dimension-and-noether-normalization.md), §2, supplies a polynomial ring \(k[t_1,\ldots,t_c]\subset B\) with \(B\) finite over it. Take the fraction fields and adjoin a finite list of algebra generators of \(B\), one at a time. Each has a monic minimal polynomial over the preceding fraction field; its derivative is nonzero in characteristic zero. Start with the polynomial ring, localize to include the finitely many coefficients and denominators of the first polynomial, adjoin its root, and invert its derivative. Repeat through the finite list, localizing at each stage to include the next coefficients. Monic division shows that each intermediate algebra injects into the corresponding fraction field: a remainder of smaller degree cannot vanish at that algebraic generator. The square-zero Taylor calculation of §7.6 shows that each root adjunction with invertible derivative is étale. These finitely presented localizations and adjunctions therefore give a smooth \(k\)-algebra containing \(B\), inside \(\operatorname{Frac}B\).

All the extra generators have only finitely many denominators in \(B\). Inverting their product in both algebras makes the last algebra equal to a localization \(B_f\). Hence \(B_f\) is a nonempty smooth chart. The transitive \(K(k)\)-action transports its smooth locus across every closed point of \(O\). The smooth locus is open by the local standard presentations; a nonempty complement would have a closed point. Thus all of \(O\) is smooth.

The dominant orbit map \(q:K\to O\) has surjective differential at a generic point. Indeed, a transcendence basis of \(k(O)\) extends to one of \(k(K)\); in characteristic zero the remaining algebraic extensions are separable. Differentiating a minimal polynomial expresses the differential of an algebraic generator in terms of the basis differentials, since its derivative is nonzero. The partial derivatives in the basis variables extend uniquely through the algebraic adjunctions by the same formula. Applying those derivations detects every coefficient of a relation between the basis differentials, proving their independence. Thus pullback of the rational differential spaces is injective, giving the asserted generic rank. The rank condition is open. Left translation transports a full-rank point to every closed point of \(K\).

For a map between smooth varieties, surjectivity of its differential gives smoothness locally: choose étale coordinates on the target and supplement their pullbacks by source coordinates to obtain an invertible square Jacobian. This gives an étale map to affine space whose projection to the target coordinates is smooth. The local standard form and square-zero Jacobian calculation are [*Formally smooth, unramified and étale ring maps*](../../AG-CA/src/formally-smooth-unramified-and-etale-ring-maps.md), §§3–5. Thus \(q\) is smooth everywhere. It is surjective by the orbit construction, and of finite presentation.

Finally two points of \(K\) have the same orbit line exactly when their difference belongs to the stabilizer (BA.11). This holds on all test rings, and gives
\[
 \begin{gathered}
 q:K\longrightarrow O\quad
   \text{smooth, surjective, finitely presented},\\
 K\times G\xrightarrow{\ \sim\ }K\times_O K,\qquad
 (a,h)\longmapsto(a,ah).
 \end{gathered}
 \tag{BA.12}
\]
Its inverse is \((a,a')\mapsto(a,a^{-1}a')\). Hence \(q\) is a \(G\)-torsor and represents the fppf quotient \(K/G\). The embedding of \(O\) in projective space is equivariant and locally closed, with its schematic stabilizer preserved.

### 1.4. Reductions are represented by section schemes

Let \(E\) be a rank-\(n\) vector bundle on \(X_R\), and let \(\operatorname{Fr}(E)\) be its frame torsor. Twist the equivariant projective embedding in §1.3 by this torsor. The representation \(\mathcal W\) gives a vector bundle \(\mathcal W(E)\), by module descent in §7.5. Equivariant homogeneous ideals descend degree by degree, giving the closed orbit closure \(Z_E\); its invariant open orbit descends as the open \(Y_E\). Thus
\[
 Y_E=\operatorname{Fr}(E)\times^K O
       \ \subset\ Z_E\
       \subset\mathbf P_{\mathrm{lines}}(\mathcal W(E)).
 \tag{BA.13}
\]
These are schemes; the last inclusion is closed and the first open. This construction of the projective ambient bundle and its ideals supplies the descent, including nilpotent test schemes.

A section of \(Y_E\to X_R\) pulls back the torsor \(\operatorname{Fr}(E)\to Y_E\) obtained from (BA.12). The resulting \(G\)-torsor has its specified \(K\)-extension \(\operatorname{Fr}(E)\). Conversely a \(G\)-reduction gives this section after a torsor cover, and effective descent glues it. The two constructions are inverse on objects and arrows:
\[
 \left\{(P,\ j_*P\xrightarrow{\sim}\operatorname{Fr}(E))\right\}
   \simeq
 \operatorname{Sec}_{X_R/R}(Y_E).
 \tag{BA.14}
\]
An arrow inducing the identity on the \(K\)-extension is the identity because \(j\) is a monomorphism. The left side therefore has no nonidentity automorphisms.

Over a Noetherian coefficient base, \(Z_E\) is projective over that base. For example, twist \(\mathcal W(E)^\vee\) by a sufficiently high power of \(A\) to make it generated by finitely many global sections. Projectivizing the resulting quotient embeds its line-projective bundle in a finite projective space over \(X_R\); combining with the fixed embedding of \(X\), and the Segre map, gives a projective embedding over \(R\). Thus the Hilbert construction from §1.2 applies to \(Z_E\).

Within each fixed-polynomial Hilbert scheme, the locus of graphs of sections of \(Z_E\to X_R\) is open. The precise graph-locus proof is in [*Beauville–Laszlo gluing and the moduli interpretation*](../../GL-SAT/src/GL-SAT-03.md), §7.2: near a graph, remove the proper image of the non-quasi-finite locus of its projection to \(X\); that projection is then finite. Its unit map is an isomorphism on the selected fibre. Remove the supports of its finite cokernel and kernel, using flatness over the Hilbert base for the kernel fibre test. This makes the projection an isomorphism. That proof uses only projectivity and flatness of the universal Hilbert family; smoothness of the ambient projective scheme is not needed for this graph-locus argument.

A graph lands in \(Y_E\) precisely when it avoids the closed boundary \(Z_E-Y_E\). Its intersection with that boundary is closed in the universal proper graph, so removing its proper image in the parameter scheme is another open condition. Taking all polynomials gives a scheme \(\mathscr S_E\), locally of finite type, with
\[
 \mathscr S_E(T)
   =\{s:X_T\to Y_{E,T}\mid \pi s=1_{X_T}\}.
 \tag{BA.15}
\]

This represents the functor on arbitrary coefficient schemes, not only Noetherian tests. To see this, descend \(E\), its idempotents and gluing maps to a Noetherian \(R_0\) as in §1.1, and carry out the construction there. For any \(R_0\)-algebra \(B\), write \(B\) as the filtered union of its finitely generated \(R_0\)-subalgebras \(B_i\). A section between these finitely presented schemes descends at a finite stage: on a finite affine cover its maps, inverse-image principal opens, unit-ideal relations witnessing the covers, and overlap identities involve finitely many coefficients and equalities. The identity \(\pi s=1\) descends in the same way. Conversely maps from \(\operatorname{Spec}B\) to the locally finitely presented \(\mathscr S_{E_0}\) have the identical finite-stage property; their quasi-compact images use only finitely many affine charts. Therefore
\[
 \begin{gathered}
 \operatorname{Sec}(Y_{E_0,B})
       =\underset{i}{\operatorname{colim}}\,
            \operatorname{Sec}(Y_{E_0,B_i}),\\
 \mathscr S_{E_0}(B)
       =\underset{i}{\operatorname{colim}}\,
            \mathscr S_{E_0}(B_i).
 \end{gathered}
 \tag{BA.16}
\]
The Noetherian identifications agree at every stage. Pulling back to \(R\) and gluing affine test schemes proves that \(\mathscr S_E\) represents (BA.14) over every parameter base, and is locally of finite presentation over it.

### 1.5. The reductive bundle atlas and its affine diagonal

Let \(V_{n,d,m}\) be a chart in (BA.8), with universal vector bundle \(E\). Its scheme of reductions \(\mathscr S_E\) from §1.4 gives the cartesian square
\[
 \begin{array}{ccc}
 \mathscr S_E&\longrightarrow&V_{n,d,m}\\
 \downarrow&&\downarrow\\
 \operatorname{Bun}_G&\xrightarrow{\ j_*\ }&
          \operatorname{Bun}_{GL_n}.
 \end{array}
 \tag{BA.17}
\]
It is cartesian as a square of groupoids, by (BA.14). For any torsor family \(P\) over \(T\), its base change on the left is the frame scheme (BA.7) for \(j_*P\) on the corresponding open coefficient locus. In particular
\[
 \mathscr S_E\times_{\operatorname{Bun}_G}T
   =V_{n,d,m}\times_{\operatorname{Bun}_{GL_n}}T.
 \tag{BA.18}
\]
These maps are representable and smooth; their images cover \(T\) by Serre generation and vanishing. The disjoint union of the \(\mathscr S_E\) is therefore a smooth surjective scheme atlas of \(\operatorname{Bun}_G\), locally of finite type over \(k\).

For completeness its diagonal is affine, not merely represented by an unspecified space of reductions. Given \(P,Q\), let \(E,F\) be their vector bundles, and let \(L_P\subset\mathcal W(E)\), \(L_Q\subset\mathcal W(F)\) be the line subbundles from their orbit sections in (BA.13). On the affine finitely presented scheme \(\underline{\operatorname{Isom}}_X(E,F)\), require
\[
 \begin{gathered}
 \left(L_P\longrightarrow\mathcal W(F)
          \longrightarrow\mathcal W(F)/L_Q\right)=0,\\
 \left(L_Q\longrightarrow\mathcal W(E)
          \longrightarrow\mathcal W(E)/L_P\right)=0,
 \end{gathered}
 \tag{BA.19}
\]
using the universal isomorphism and its inverse. Each is a zero-section equation in a Hom scheme (BA.3) for vector bundles on \(X\). It cuts out a closed subscheme of finite presentation. Together they say that the line subbundles, and hence the \(G\)-reductions by the exact schematic stabilizer (BA.11), are identified. The resulting affine finitely presented scheme represents \(\underline{\operatorname{Isom}}_X(P,Q)\). All constructions commute with coefficient change.

The fppf stack property is effective torsor descent from §7.5. We have exhibited its diagonal and smooth scheme atlas, which are the defining algebraicity conditions. This proves
\[
 \begin{gathered}
 \operatorname{Bun}_G\text{ is an algebraic stack
 locally of finite type over }k,\\
 \Delta_{\operatorname{Bun}_G}\text{ is affine and
 of finite presentation}.
 \end{gathered}
 \tag{BA.20}
\]
The statement includes the full connected reductive characteristic-zero scope of this lesson. The deformation and dimension calculation in §2 can now be applied to this represented stack.

### 1.6. Compatible formal bundles are algebraic

The same coordinates prove the formal effectivity needed for bundles. Let \(R\) be a complete Noetherian local \(k\)-algebra with maximal ideal \(\mathfrak m\), put \(R_\nu=R/\mathfrak m^{\nu+1}\), and keep the fixed projective curve \(X\).

**Theorem 1.6 (formal effectivity).** Restriction gives an equivalence of groupoids
\[
 \operatorname{Bun}_G(R)
    \xrightarrow{\ \sim\ }
 \varprojlim_{\nu\geq0}\operatorname{Bun}_G(R_\nu).
 \tag{BA.21}
\]
The inverse-limit groupoid consists of bundles with their compatible restriction isomorphisms, and of compatible systems of arrows.

**Proof of existence.** Start with such a formal torsor family \(P_\nu\), and take its vector bundles \(E_\nu\) under (BA.9). Choose \(m\) so that \(E_0(m)\) is generated and has zero positive cohomology. Every \(\operatorname{Spec}R_\nu\) has that single parameter point. Equations (BA.1)–(BA.2) consequently give finite free section modules of one common rank \(N\), compatible with reduction; evaluation is surjective by the fibre generation and Nakayama. Choose a basis at \(\nu=0\), and lift it successively. The reduction maps on these free section modules are surjective; a lifted basis is a basis over the local ring by Nakayama and the common rank. We obtain compatible quotients
\[
 \begin{gathered}
 R_\nu^N\xrightarrow{\sim}H^0(X_{R_\nu},E_\nu(m)),\\
 \mathcal O_{X_{R_\nu}}(-m)^N\twoheadrightarrow E_\nu.
 \end{gathered}
 \tag{BA.22}
\]
They define compatible points \(v_\nu\) of the single chart \(V_{n,d,m}\).

Choose an affine open \(\operatorname{Spec}C\subset V_{n,d,m}\) containing \(v_0\). Every \(v_\nu\) factors through it, because the underlying parameter point is the same. Their compatible coordinate maps give
\[
 C\longrightarrow\varprojlim_\nu R_\nu=R.
 \tag{BA.23}
\]
The resulting \(R\)-point supplies a vector bundle \(E\) whose framed quotients restrict to (BA.22). The isomorphisms with \(E_\nu\) preserving those quotients are unique, so are compatible.

Using those identifications, each \(P_\nu\) is a reduction of \(E|_{X_{R_\nu}}\), hence a point of \(\mathscr S_E(R_\nu)\) by (BA.14). Choose an affine open of \(\mathscr S_E\) containing the special point. Again every formal point factors through it. Its coordinate maps have a limit in \(R\), giving an actual reduction of \(E\), thus a \(G\)-torsor \(P\) on \(X_R\). Its restriction is identified with every \(P_\nu\), with the given compatibility, because the reduction functor has retained the specified \(K\)-extension and all arrows.

**Proof of full faithfulness.** For two actual torsors \(P,Q\), their Isom scheme is affine by (BA.19), say \(\operatorname{Spec}D\) over \(R\). Its coordinate algebra gives
\[
 \operatorname{Hom}_{R\text{-alg}}(D,R)
  =\varprojlim_\nu
       \operatorname{Hom}_{R\text{-alg}}(D,R_\nu).
 \tag{BA.24}
\]
This follows directly from the ring limit defining completeness: a compatible family of maps has a unique map into the limit, and conversely. Thus every compatible system of torsor isomorphisms comes from a unique actual isomorphism. Composition commutes with restriction and with that limit. This proves (BA.21). \(\square\)

The proof algebraizes the particular formal bundle and its reductions through finite-type scheme coordinates. Its hypotheses are the fixed projective curve and the complete Noetherian local coefficient ring displayed above.

| Construction | Coordinates | Result |
|---|---|---|
| Bundle Hom and Isom | Finite cohomology complex and inverse equations | Affine schemes of finite presentation, (BA.3)–(BA.4) |
| Vector-bundle atlas | A high-twist quotient with a basis of sections | Smooth \(GL_N\)-torsor charts, (BA.7)–(BA.8) |
| Principal-bundle reductions | Schematic orbit line and proper graphs | Section schemes on every coefficient base, (BA.13)–(BA.16) |
| Reductive bundle stack | Pullback of the vector-bundle charts | Smooth scheme atlas and affine diagonal, (BA.17)–(BA.20) |
| Formal torsor family | Compatible bases and affine coordinate maps | Effectivity and all arrows, (BA.21)–(BA.24) |

*The cartesian squares (BA.7) and (BA.17) identify the frame atlas and its reduction atlas. The line stabilizer (BA.11) and the two equations (BA.19) ensure that reductions and arrows retain their scheme structures. For the classical algebraicity statement, [Heinloth, Proposition 1](https://arxiv.org/pdf/0711.4450v2) is freely accessible further reading; the atlas and formal effectivity proofs used here are §§1.1–1.6.*

## 2. Deformations and the dimension formula

**Proposition 2.1.** At a bundle \(P\), the tangent complex of \(\operatorname{Bun}_G\) is

\[
T_P\operatorname{Bun}_G\simeq R\Gamma(X,\operatorname{ad}(P))[1].
\]

Its degree \(-1\) cohomology is the Lie algebra of automorphisms, its degree zero cohomology gives first-order deformations, and degree one gives obstructions. In particular,

\[
H^{-1}(T_P)=H^0(X,\operatorname{ad}(P)),\qquad
H^0(T_P)=H^1(X,\operatorname{ad}(P)),\qquad
H^1(T_P)=0.
\]

**Proof.** Choose an affine étale cover trivializing \(P\), with transition functions \(g_{ij}\). For a square-zero thickening with ideal \(I\), smoothness of \(G\) lets us lift each transition function. The failure of the lifted functions to satisfy the cocycle equation on triple overlaps is an additive Čech 2-cocycle with coefficients in \(\operatorname{ad}(P)\otimes I\). Conjugation by the transition functions gives precisely the adjoint bundle, rather than the constant Lie algebra sheaf.

Changing the lifts by 1-cochains changes that failure by a coboundary. Consequently its cohomology class is the obstruction. If it vanishes, correcting the lifts produces a bundle. The set of lift classes is a torsor under \(H^1(\operatorname{ad}(P)\otimes I)\), and an automorphism inducing the identity before thickening is a 0-cocycle, in \(H^0(\operatorname{ad}(P)\otimes I)\). Section 2.1 constructs the lifted cover and proves the affine étale Čech comparison with ordinary coherent cohomology. Section 2.2 proves the additive kernel, cocycle corrections, all arrows and universal tensor compatibility used in this argument. These groups and their cochain-level maps identify the deformation complex with \(R\Gamma(\operatorname{ad}(P))[1]\). On a curve coherent cohomology vanishes above degree one, proving the last assertion. \(\square\)

The same argument applies to families and successive square-zero extensions. The relative coherent cohomological dimension is one. Thus the infinitesimal lifting criterion, combined with the algebraicity and local finite presentation already stated, proves that \(\operatorname{Bun}_G\to\operatorname{Spec}k\) is smooth.

**Theorem 2.2.** The stack \(\operatorname{Bun}_G\) is smooth and has pure dimension

\[
\dim\operatorname{Bun}_G=(g-1)\dim G.
\]

**Proof.** A smooth algebraic stack with the tangent complex above has local dimension

\[
\dim H^1(X,\operatorname{ad}(P))-
\dim H^0(X,\operatorname{ad}(P))=-\chi(X,\operatorname{ad}(P)).
\]

The minus sign is the contribution of infinitesimal stabilizers. It also follows by taking a smooth presentation \(U\to\operatorname{Bun}_G\) and subtracting its relative dimension from \(\dim U\).

The character \(\det\operatorname{Ad}:G\to\mathbb G_m\) is trivial. The algebraic-hull and trace proof in §2.3 establishes this for every connected reductive group in the stated characteristic-zero scope. Hence \(\det\operatorname{ad}(P)\) is trivial and \(\deg\operatorname{ad}(P)=0\). The Euler-characteristic formula proved in §2.4 gives

\[
\chi(X,\operatorname{ad}(P))=(1-g)\dim G.
\]

This is independent of \(P\), so the stated dimension is pure. \(\square\)

For \(GL_n\), the answer is \(n^2(g-1)\). For the Picard stack it is \(g-1\). The Picard scheme of a fixed degree instead has dimension \(g\), because it has forgotten the scalar automorphisms. For \(X=\mathbb P^1\), the Picard stack has dimension \(-1\): each degree component is \(B\mathbb G_m\). Negative stack dimension records the stabilizer; it is not a negative number of parameters in a scheme.

*Further reading:* [Beilinson–Drinfeld, §2.1.1] describes the tangent and cotangent complexes in the semisimple case with \(g>1\). The proof just given also explains the reductive and low-genus cases without importing that restriction.

### 2.1. An affine étale nerve computes the required cohomology

Here are the cover and cohomology details behind Proposition 2.1. Let \(R'\twoheadrightarrow R\) have square-zero kernel \(I\), with no Noetherian or flatness assumption on \(R\) or \(I\). Let \(P_0\) be a \(G\)-bundle on \(X_R\). The two affine curve opens of §1.1 will be denoted \(V_1,V_2\), after any coefficient change.

The affine torsor dictionary of §7.5 and the smoothness argument of §7.6 make \(P_0\) affine, smooth and finitely presented over \(X_R\). Lemma 7.9, applied on each affine curve open, gives affine étale local sections. Choose finitely many such opens \(U_i\to X_R\), each lying over one \(V_j\), that cover \(X_R\) and trivialize \(P_0\). Finiteness follows from quasi-compactness. Refine by finitely many standard étale affine charts. In such a chart the algebra is a localized polynomial quotient with equally many variables and equations and invertible Jacobian determinant. This form and its infinitesimal criterion are proved in [*Formally smooth, unramified and étale ring maps*](../../AG-CA/src/formally-smooth-unramified-and-etale-ring-maps.md), §§3–5; finite presentations descend to a Noetherian coefficient model as in §§1.1 and 7.6.

Lift the finitely many coefficients of those equations and their localizing elements to the corresponding curve open over \(R'\), and invert the lifted Jacobian determinant. This gives affine étale \(U_i'\to X_{R'}\) with reduction \(U_i\). Their images cover: a nilpotent closed immersion is a homeomorphism on underlying spaces, so every point is still covered. Set \(U=\coprod_iU_i\) and \(U'=\coprod_iU_i'\). Write \(U^{q+1}_X\) for the \((q+1)\)-fold fibre product over \(X_R\), and likewise for \(U'\).

Every nerve term is affine. Indeed, an affine \(R\)-scheme mapping to the separated \(R\)-scheme \(X_R\) has affine inverse images of affine opens: its graph on such an open is closed in a product of affine schemes. The same graph argument makes the finite fibre products affine. Every lifted nerve term is flat over \(R'\), because it is étale over the \(R'\)-flat curve. If \(C_q'\) and \(C_q\) are their rings, therefore,

\[
0\longrightarrow I\otimes_R C_q
\longrightarrow C_q'\longrightarrow C_q\longrightarrow0,
\qquad (I\otimes_R C_q)^2=0.
\tag{DS.1}
\]

Flatness gives the injection by tensoring \(0\to I\to R'\to R\to0\); the identification uses \(I^2=0\). This does not require tensoring a nonflat module to preserve an unrelated injection.

For any quasi-coherent \(F\) on \(X_R\), the étale Čech complex \(C_U^\bullet(F)\) computes its coherent-sheaf cohomology. To prove this, form the double complex whose term in bidegree \((q,p)\) is the section module on \(U_X^{q+1}\) restricted to \(V_1\amalg V_2\) when \(p=0\), and to \(V_1\cap V_2\) when \(p=1\). There are only these two vertical degrees. For fixed \(q\), the vertical augmented complex is exact because the nerve term is affine, both restricted opens and their intersection are affine, and affine quasi-coherent cohomology vanishes. The all-ring affine-vanishing and finite-cover proofs are [*Algebra and sheaf cohomology before reductive groups*](../../AG-RG/AG-RG-S01.html), §§4–5.

For fixed \(p\), the horizontal augmented complex is the Amitsur complex of the faithfully flat affine cover \(U\times_XV_p\to V_p\), with the module \(F(V_p)\). Its exactness is the all-module contraction proved in §7.5. Taking these two augmented complexes in either order gives

\[
C_U^\bullet(F)\ \longrightarrow\operatorname{Tot}D^{\bullet,\bullet}
\ \longleftarrow\
\bigl[\Gamma(V_1,F)\oplus\Gamma(V_2,F)
\longrightarrow\Gamma(V_1\cap V_2,F)\bigr].
\tag{DS.2}
\]

Both arrows are quasi-isomorphisms. One may compute this directly by eliminating a horizontal coboundary and then a vertical one; the double-complex proof is the finite-cover calculation in the cited §4. There are two vertical degrees and finitely many summands in each total degree, so no convergence or infinite-product issue occurs. In particular, for \(F=\operatorname{ad}(P_0)\otimes_R I\), (BA.1) identifies the right-hand complex with \(K^\bullet\otimes_R I\), for a finite projective complex \(K^\bullet\) in degrees \(0,1\). Thus \(H^2(X_R,F)=0\), even when \(I\) is not flat.

### 2.2. The square-zero groupoid and smoothness

The additive kernel used in deformation theory has explicit coordinates. Let \(A_G=k[G]\), let \(\epsilon:A_G\to k\) be evaluation at the identity, and put \(\mathfrak a=\ker\epsilon\). For a square-zero ideal \(J\subset B'\), a \(B'\)-point of \(G\) reducing to the identity is a homomorphism \(f=\epsilon+\delta\), with values of \(\delta\) in \(J\). Multiplicativity is exactly
\(\delta(ab)=\epsilon(a)\delta(b)+\epsilon(b)\delta(a)\), since \(J^2=0\). Hence

\[
\ker\bigl(G(B')\longrightarrow G(B'/J)\bigr)
=\operatorname{Hom}_k(\mathfrak a/\mathfrak a^2,J)
=\operatorname{Lie}(G)\otimes_kJ.
\tag{DS.3}
\]

The last equality uses the finite dimension of the cotangent space. Comultiplication makes this group law addition: the product of two derivations has no quadratic term. Conjugation is the adjoint action, as follows by differentiating the conjugation morphism. These identifications hold for every square-zero \(J\); there is no reduced-test restriction.

Use the trivializations on \(U\) from §2.1, with transition functions \(g_{ij}\) written as maps from chart \(j\) to chart \(i\). Smoothness of the affine group and the affine lifting criterion of §7.6 lift each \(g_{ij}\) to the corresponding term of the lifted nerve. Choose the lifts \(\widetilde g_{ij}\) independently; they need not yet satisfy the cocycle condition. Their defect is

\[
1+c_{ijk}
=\widetilde g_{ij}\widetilde g_{jk}\widetilde g_{ik}^{-1},
\qquad
c_{ijk}\in
\bigl(\operatorname{ad}(P_0)\otimes_RI\bigr)(U_i\times_XU_j\times_XU_k),
\tag{DS.4}
\]

expressed in frame \(i\). The symbol \(1+c\) denotes the point of the kernel (DS.3), not an assumption that \(G\) is a general linear group. Associativity on a quadruple overlap gives

\[
c_{ijk}+c_{ikl}
=\operatorname{Ad}(g_{ij})c_{jkl}+c_{ijl}.
\tag{DS.5}
\]

To check the equality, expand \((\widetilde g_{ij}\widetilde g_{jk})\widetilde g_{kl}\) and \(\widetilde g_{ij}(\widetilde g_{jk}\widetilde g_{kl})\), move every kernel term to frame \(i\), and discard products of two elements of \(I\). This is exactly the twisted Čech 2-cocycle equation.

Replace a lift by \((1+a_{ij})\widetilde g_{ij}\). Its defect changes by
\(a_{ij}+\operatorname{Ad}(g_{ij})a_{jk}-a_{ik}\), the Čech coboundary \(da\). The vanishing of \(H^2\) proved in §2.1 supplies \(a\) with \(da=-c\). The corrected transition functions satisfy the cocycle equation, including its identity and inverse relations, and effective torsor descent from §7.5 supplies a \(G\)-bundle on \(X_{R'}\) together with the specified reduction to \(P_0\).

All lifts and all their arrows are described by the same calculation. Fix one corrected lift as origin. A second lift can be trivialized on \(U'\) with the prescribed frames on \(U\): a frame is a section of a smooth affine torsor, so the affine square-zero lifting criterion lifts that section. Its transition functions differ from the origin by a 1-cochain \(a\), and the cocycle equation says \(da=0\). A change of lifted frames by \(1+b_i\) replaces \(a\) by \(a-db\), where
\((db)_{ij}=\operatorname{Ad}(g_{ij})b_j-b_i\). Every isomorphism reducing to the identity has this form, since it is determined on the trivializing cover. Descent checks its agreement on overlaps. Consequently

\[
\operatorname{Lift}(P_0;R'\to R)
\simeq [\,Z^1(C_U^\bullet(F))/C_U^0(F)\,],
\qquad a\longmapsto a-db,
\quad F=\operatorname{ad}(P_0)\otimes_RI.
\tag{DS.6}
\]

This equivalence uses the chosen origin; the resulting isomorphism classes form a torsor under \(H^1(X_R,F)\), and each object's automorphisms reducing to the identity are \(H^0(X_R,F)\). The obstruction before choosing an origin is the \(H^2\)-class of (DS.4), which is always zero here.

Equation (DS.2) and the tensor-compatible complex of §1.1 give the two-term linearized deformation complex

\[
T_{P_0}\operatorname{Bun}_G\simeq K^\bullet[1],
\qquad
K^\bullet\simeq R\Gamma(X_R,\operatorname{ad}(P_0)),
\qquad K^\bullet\text{ in degrees }0,1.
\tag{DS.7}
\]

Indeed the groupoid of a two-term complex in degrees \(-1,0\) has vectors in degree zero as objects and degree \(-1\) vectors as arrows given by its differential. Applying this to the cocycle groupoid (DS.6) gives (DS.7); the quasi-isomorphism (DS.2) induces the same objects modulo boundaries and the same automorphism kernel. The construction is compatible with every \(R\)-module \(I\) and with coefficient changes by (BA.1). It is this linearized complex that is meant by the tangent complex in Proposition 2.1.

The represented stack of §1.5 is smooth over \(k\). Here is the connection with a scheme atlas, rather than an appeal to a criterion for an unrepresented functor. Let \(V\to\operatorname{Bun}_G\) be that smooth atlas. Given an affine infinitesimal lifting problem for \(V\), lift its underlying bundle by the argument above. The pullback of \(V\) along the lifted bundle is smooth over the extended coefficient ring, so its prescribed reduced section lifts locally on the coefficient scheme. Work in an affine neighborhood \(W\subset V\) containing the reduced image. All lifts factor through \(W\), since the coefficient thickening has the same underlying space. Differences of two local lifts are derivations from \(k[W]\) into the square-zero ideal. They form a Čech 1-cocycle in the module \(\operatorname{Hom}(\Omega_{W/k}\otimes B,I)\) on the affine coefficient scheme \(\operatorname{Spec}B\). This is a quasi-coherent module: \(\Omega_{W/k}\) is finitely presented, so its Hom commutes with localization. Affine vanishing from §2.1 makes the cocycle a coboundary. Subtract those derivations from the local lifts and glue; adding a derivation into a square-zero ideal preserves the ring-homomorphism equations. Thus affine infinitesimal problems for \(W\) have lifts. The atlas is locally of finite presentation by §1.5, and the scheme criterion is proved in [*Formally smooth, unramified and étale ring maps*](../../AG-CA/src/formally-smooth-unramified-and-etale-ring-maps.md), §§3–5. It makes \(V\) smooth over \(k\), and the smooth presentation proves smoothness of \(\operatorname{Bun}_G/k\). A general nilpotent thickening is handled by its successive square-zero powers.

| Step | Actual mathematical object | What its equation proves |
|---|---|---|
| Lift affine covers | Étale polynomial charts over \(R'\) | The same curve and torsor cover is available on the thickening |
| Linearize the group | Derivations of \(k[G]\) at its augmentation | The square-zero kernel is additive, with adjoint transition action |
| Repair transitions | The 2-cocycle \(c\) and a 1-cochain \(a\) | \(c+da=0\) gives an effective bundle lift |
| Keep arrows | The action \(a\mapsto a-db\) | \(H^1\) gives lift classes and \(H^0\) gives their infinitesimal automorphisms |

### 2.3. Why the adjoint determinant is trivial without root classification

We prove the character assertion in Theorem 2.2 for the original connected reductive characteristic-zero group. Two earlier Lie results are used at their exact hypotheses: [*Nilpotent and solvable Lie algebras: Engel's and Lie's theorems*](../../RT-LIE/src/RT-LIE-02.md), Theorem 3.1 and Proposition 4.1, prove triangularization of a solvable Lie algebra and existence of its solvable radical; [*The Killing form and Cartan's criteria*](../../RT-LIE/src/RT-LIE-03.md), Corollary 4.2, proves that a semisimple Lie algebra is perfect. We also use the finite-type characteristic-zero Cartier theorem, proved in [*Lie algebras and smoothness of group schemes*](../../AG-GS/src/lie-algebras-and-smoothness.md), Theorem 4.3. Only its finite-type case is needed.

Write \(\mathfrak g=\operatorname{Lie}G\), and let \(\mathfrak r\) be its solvable radical. Take the closed faithful representation from (BA.9), adjoining a trivial line if necessary to give it positive dimension. Lie's theorem puts \(\mathfrak r\) in the upper triangular matrix algebra in a suitable basis. Let \(B\) be the upper triangular group. Among all closed subgroup schemes of the ambient \(GL_n\) whose Lie algebra contains \(\mathfrak r\), take their scheme-theoretic intersection \(H\). This is a finite intersection: the sum of their defining ideals in the Noetherian ring \(k[GL_n]\) is generated by finitely many elements, and each generator uses finitely many of those ideals.

Tangent vectors satisfy the equations of an intersection exactly when they satisfy each set of equations; hence \(\mathfrak r\subset\operatorname{Lie}H\). In particular

\[
H\subset G\cap B,\qquad
\mathfrak r\subset\operatorname{Lie}H.
\tag{DS.8}
\]

Cartier makes \(H\) smooth. Its identity component has the same Lie algebra and is a closed subgroup, by [*Group schemes over a field*](../../AG-GS/src/group-schemes-over-a-field.md), Lemma 7.0. Minimality of \(H\) therefore makes \(H\) connected. Every \(\operatorname{Ad}(g)\) preserves \(\mathfrak r\), since the radical is characterized as the largest solvable ideal. Thus conjugation by every \(g\in G(k)\) preserves \(H\). This holds schematically: \(G\times H\) is reduced, and every pulled-back defining equation vanishes at all its \(k\)-points, so it vanishes by the Nullstellensatz. Therefore \(H\) is normal in \(G\).

Let \(U=H\cap U_B\), with \(U_B\) the upper unitriangular group. We need its connectedness, not an assumption that all subgroups of a unipotent group are connected. The finite polynomials
\(\log(1+N)=\sum_{j=1}^{n-1}(-1)^{j+1}N^j/j\) and
\(\exp(N)=\sum_{j=0}^{n-1}N^j/j!\) are inverse isomorphisms of varieties between strictly upper triangular matrices and \(U_B\). This follows by substitution in the usual formal series modulo degree \(n\); all denominators are invertible.

For \(u\in U(k)\), the curve \(t\mapsto\exp(t\log u)\) belongs to \(U\). Each defining polynomial restricts to a polynomial in \(t\) vanishing at every nonnegative integer, because those points are powers of \(u\); characteristic zero makes that an infinite set. Differentiating at zero gives \(\log u\in\operatorname{Lie}U\). Cartier makes \(U\) smooth and reduced. Hence its reduced closed image under \(\log\) is contained in the vector space \(\operatorname{Lie}U\) and has the same dimension as that vector space. A proper closed subset of an affine space has smaller dimension. Thus

\[
\log U=\operatorname{Lie}U,\qquad
U=\exp(\operatorname{Lie}U)\text{ is connected}.
\tag{DS.9}
\]

Within \(H\subset B\), the elements of \(U(k)\) are exactly the unipotent matrices. Conjugation by \(G(k)\) preserves unipotence and \(H(k)\), and therefore preserves \(U(k)\). The same reduced-product argument makes \(U\) a normal subgroup scheme of \(G\). It is a connected unipotent subgroup. Reductivity, namely the absence of a nontrivial connected normal unipotent subgroup, forces \(U=1\).

The diagonal map \(q:H\to(\mathbb G_m)^n\) now has trivial scheme-theoretic kernel. Let \(J\) be the reduced closure of its image. The closure of a subgroup of torus points is a subgroup: pull a defining equation back by multiplication and use density in each variable, and likewise use inversion. Reduced products make this a scheme-theoretic statement. Cartier makes \(J\) smooth; it is connected, as the closure of the image of connected \(H\). The differential of \(q:H\to J\) is injective because its kernel is \(\operatorname{Lie}U=0\). Dominance gives \(\dim J\le\dim H\), and injectivity of this differential between smooth groups gives the reverse inequality. Thus the differential is an isomorphism, everywhere by translation. The Jacobian criterion used in §1.3 makes \(q\) étale.

Its image is an open subgroup containing a nonempty open \(W\) of the integral group \(J\). For any \(j\in J(k)\), the opens \(W\) and \(jW\) meet, so \(j\) is a quotient of two image points. All closed points are therefore in the image. The open image is all of \(J\), since a nonempty closed complement would have a closed point. The trivial kernel makes \(q\) a monomorphism on every test ring: two points with the same image differ by a point of \(U\). A monomorphic étale cover is an isomorphism, by the effective descent proved in §7.5. Thus \(H\) is a closed connected subgroup of a split torus.

Such a subgroup is itself a split torus. Here is the relevant character calculation. Its coordinate algebra is a Hopf quotient of \(k[\mathbb Z^n]\). The images of the monomials are units and group-like elements. Distinct group-like elements are linearly independent: a shortest nontrivial relation, after applying comultiplication and subtracting its tensor with the last group-like element, makes all the other group-like elements equal to the last one, a contradiction. If \(M\subset\mathbb Z^n\) consists of exponents whose image is \(1\), it follows that this quotient is exactly \(k[\mathbb Z^n/M]\). Integer row and column division puts a finite relation matrix in diagonal form, so this finitely generated abelian group is a free group plus a finite torsion group. In characteristic zero a nonzero torsion summand gives a nontrivial finite étale factor, contradicting connectedness. The quotient exponent group is therefore free, and \(H\) is a split torus. This also proves the needed special case of [*Diagonalizable groups and groups of multiplicative type*](../../AG-GS/src/diagonalizable-groups.md), Theorem 4.1.

A normal torus in a connected affine group is central, including on nonreduced test rings. To see this directly, for a character \(z^\lambda\) of \(H\), pull it back by conjugation to
\(\sum_\mu c_\mu z^\mu\) in \(k[G]\otimes k[H]\). The assertion that conjugation is a group homomorphism in its second variable gives

\[
c_\mu^2=c_\mu,\qquad
c_\mu c_\nu=0\ (\mu\ne\nu),\qquad
\sum_\mu c_\mu=1.
\tag{DS.10}
\]

Connectedness of \(G\) allows only the idempotents \(0,1\), so exactly one coefficient is \(1\). At the identity of \(G\) the pullback is \(z^\lambda\); hence it is \(z^\lambda\) everywhere. Every character is fixed, and the coordinate algebra is generated by characters. Conjugation is the identity morphism on \(H\), proving centrality. In particular \(\mathfrak r\) is central in \(\mathfrak g\).

The quotient \(\mathfrak g/\mathfrak r\) has zero solvable radical by the earlier Proposition 4.1, so it is semisimple and perfect. Therefore

\[
\mathfrak g=[\mathfrak g,\mathfrak g]+\mathfrak r,
\qquad
\operatorname{tr}_{\mathfrak g}(\operatorname{ad}x)=0
\quad(x\in\mathfrak g).
\tag{DS.11}
\]

The trace vanishes on \(\mathfrak r\) because it is central, and on each commutator because
\(\operatorname{ad}[y,z]=[\operatorname{ad}y,\operatorname{ad}z]\) and the trace of a matrix commutator is zero.

For \(\chi=\det\operatorname{Ad}:G\to\mathbb G_m\), the coefficient of \(\varepsilon\) in
\(\det(1+\varepsilon\operatorname{ad}x)\) is this trace. Thus \(d\chi_e=0\), and translations make \(d\chi\) zero everywhere. A rational function with zero differential on an integral characteristic-zero \(k\)-variety is algebraic over \(k\): if it were transcendental, extend it to a transcendence basis of the function field, differentiate with respect to it, and extend that derivation through the remaining finite separable extension by differentiating minimal polynomials. The resulting derivative would be \(1\), a contradiction. This is also the field-differential argument of §1.3. Since \(k\) is algebraically closed, \(\chi\) is constant, and \(\chi(e)=1\). We have proved

\[
\det\operatorname{Ad}=1,\qquad
\det\operatorname{ad}(P)\simeq\mathcal O_X,\qquad
\deg\operatorname{ad}(P)=0.
\tag{DS.12}
\]

The first equality is an equality of morphisms, so the associated determinant line is trivial in every bundle family. No root classification or choice of a maximal torus of \(G\) is used in this determinant proof.

### 2.4. Euler characteristics from divisors and line filtrations

For completeness, the numerical curve formula needed here has a short proof that works in genus zero and one as well. Work first over any extension field \(K/k\). The connected smooth curve \(X\) is integral: its regular local rings are domains, so distinct irreducible components cannot meet; the finitely many components are then open and closed, and connectedness leaves one. Its affine coordinate domains remain domains after every field extension. For if two nonzero elements of \(A\otimes_kK\) had zero product, all their coefficients and that equality would lie over a finitely generated subalgebra \(R_0\subset K\). Pick a nonzero coefficient from each factor in a \(k\)-basis of \(A\), invert their product, and take a \(k\)-point of that nonzero finitely generated algebra by the Nullstellensatz. Specialization would give two nonzero elements of the domain \(A\) with zero product, a contradiction. Thus \(X_K\) is integral; applying the same argument to larger extension fields makes it geometrically integral.

The curve \(X_K\) is smooth and projective by coefficient change. Its closed-point local rings are discrete valuation rings: a regular one-dimensional local domain has principal maximal ideal \((t)\) by Nakayama. Every nonzero element is \(t^m\) times a unit. Indeed, infinite divisibility by \(t\) would give an ascending chain of ideals generated by \(a/t^j\); stabilization would give \(a/t^j=t r(a/t^j)\), impossible for a nonzero element because \(1-tr\) is a unit. This proves the required valuation assertion. The regular-domain and dimension-one hypotheses follow from the proved scheme criteria in [*Regular local rings*](../../AG-CA/src/regular-local-rings.md), Theorem 1.1, and [*Smooth algebras over a field and the Jacobian criterion*](../../AG-CA/src/smooth-algebras-over-a-field-and-the-jacobian-criterion.md), Theorem 2.1.

An invertible sheaf \(L\) has a nonzero rational section \(s\). Its orders in those discrete valuation rings are zero off finitely many closed points: the section is a regular frame on a nonempty open, and its complement on a Noetherian integral curve is finite. The local orders give a divisor \(D=\sum_pn_pp\) and identify \(L\) with \(\mathcal O(D)\): the local generator \(t_p^{-n_p}\) is sent to \(t_p^{-n_p}s\), a regular frame of \(L\). Define \(\deg D=\sum_pn_p[K(p):K]\).

For a closed point \(p\), multiplication by its local parameter gives
\(0\to\mathcal O(D-p)\to\mathcal O(D)\to K(p)\to0\), where the last term is a skyscraper line over \(K(p)\). Its only cohomology is its section space: the two-open complex of §1.1 is exact in positive degree for a sheaf supported at a point. Finite-dimensional cohomology and vanishing above degree one are already proved in §1.1. The long exact sequence therefore gives
\(\chi(\mathcal O(D))-\chi(\mathcal O(D-p))=[K(p):K]\). Repeating this equality, with subtraction for negative coefficients, proves

\[
\chi(X_K,L)=\deg L+1-g.
\tag{DS.13}
\]

Here \(H^0(X,\mathcal O_X)=k\): a regular function defines a map to \(\mathbb P^1\) whose image is closed because \(X\) is proper, lies in \(\mathbb A^1\), and is irreducible; it cannot be all of \(\mathbb P^1\), so it is a point. The section is constant. The flat field-change calculation (BA.1) gives \(H^0(X_K,\mathcal O)=K\) and
\(\dim_KH^1(X_K,\mathcal O)=g\). Thus \(\chi(\mathcal O)=1-g\), including both small genera. The divisor degree is independent of the rational frame because (DS.13) computes it from \(L\).

Every vector bundle \(E\) has a filtration with line-bundle quotients. Choose a nonzero vector in its generic fibre. On a trivializing affine chart, multiply its coordinates by a common denominator and take the kernel of their pairwise wedge equations; this is the saturated rank-one subsheaf whose generic fibre is the chosen rational line. These finite equations give a coherent subsheaf and agree on overlaps. At a closed point, write the rational vector as \(t^m\) times a vector with at least one unit coordinate. The intersection of its rational line with the local free module is the span of that primitive vector; elementary row operations make it the first basis vector. Hence the subsheaf is an invertible sheaf \(L\), and \(E/L\) is locally free of rank one less. Induction on the rank constructs the filtration.

Euler characteristic is additive in a short exact sequence by the finite long exact cohomology sequence. Determinants multiply in a vector-bundle exact sequence: locally split the sequence, take wedge products of a basis of the subbundle and lifts of a quotient basis, and observe that changing those lifts does not change the top wedge. Apply (DS.13) to the line quotients. The result is

\[
\chi(X_K,E)=\deg\det E+\operatorname{rank}(E)(1-g).
\tag{DS.14}
\]

This proves precisely the Euler-characteristic form of Riemann–Roch consumed in Theorem 2.2. It does not infer individual \(H^0\) or \(H^1\) dimensions from degree alone.

### 2.5. The tangent exact sequence measures stack dimension

Let \(\Omega\supset k\) be algebraically closed, \(P\) a bundle on \(X_\Omega\), and choose a point \(v\) over \(P\) in the smooth scheme atlas \(V\). Such a point exists: the smooth surjective atlas fibre is nonempty and locally of finite type, and a nonempty finite-type affine open has an \(\Omega\)-point. Put \(F=V\times_{\operatorname{Bun}_G}\operatorname{Spec}\Omega\), using \(P\), and let \(f\) include the chosen identification at \(v\). This fibre is a smooth scheme over \(\Omega\).

Set \(A^i=H^i(X_\Omega,\operatorname{ad}P)\). A tangent vector to \(F\) is a first-order point of \(V\) together with an isomorphism from its underlying bundle to the constant deformation of \(P\), reducing to the chosen identification. Forgetting that isomorphism gives a tangent vector to \(V\). The kernel consists exactly of infinitesimal automorphisms of \(P\), which are \(A^0\) by (DS.6). The map from \(T_vV\) to \(A^1\) sends a first-order point to its underlying deformation class. Its kernel consists of the points for which an isomorphism to the constant deformation exists, precisely the image of \(T_fF\). It is surjective because the atlas is smooth and hence lifts a prescribed reduced atlas point over each first-order bundle. Thus

\[
0\longrightarrow A^0\longrightarrow T_fF
\longrightarrow T_vV\longrightarrow A^1\longrightarrow0.
\tag{DS.15}
\]

All maps are linear: their formulas are the additive kernel and coboundary calculations (DS.3)–(DS.6). Since the schemes \(V\) and \(F\) are smooth, their tangent dimensions are their local dimensions. Consequently the local stack dimension, the atlas dimension minus its relative fibre dimension, is

\[
\begin{gathered}
\dim_vV-\dim_fF=\dim_\Omega A^1-\dim_\Omega A^0
=-\chi(X_\Omega,\operatorname{ad}P),\\
\dim_P\operatorname{Bun}_G=(g-1)\dim G.
\end{gathered}
\tag{DS.16}
\]

The second equality uses (DS.12) and (DS.14), and the rank of the adjoint bundle is \(\dim G\) because \(G\) is smooth. This dimension convention is independent of the chosen atlas: the fibre product of two atlases is smooth over both, and local dimensions of a smooth morphism add as they do in its étale-local affine-space coordinates. Subtracting the corresponding fibre dimensions therefore gives the same difference. It is constant at every geometric bundle point, so the dimension is pure. This proves all assertions of Theorem 2.2, with no assumption \(g>1\).

### 2.6. A rank-two example with changing stabilizers

On \(\mathbb P^1\), use \(t\) on the first affine chart and \(t^{-1}\) on the second. With the second frame of \(\mathcal O(m)\) equal to \(t^m\) times the first, the Čech complex has section images \(k[t]\) and \(t^mk[t^{-1}]\) inside \(k[t,t^{-1}]\). Their intersection has basis \(1,t,\ldots,t^m\) for \(m\ge0\), and is zero otherwise. Their quotient has basis the monomials \(t^j\) with \(m<j<0\). Thus

\[
h^0(\mathcal O(m))=\max(m+1,0),\qquad
h^1(\mathcal O(m))=\max(-m-1,0).
\tag{DS.17}
\]

Take \(E=\mathcal O(a)\oplus\mathcal O(b)\), with \(a\ge b\), and put \(d=a-b\). Its endomorphism bundle is
\(\mathcal O^{\oplus2}\oplus\mathcal O(d)\oplus\mathcal O(-d)\), so

\[
h^0(\operatorname{End}E)=d+3+\max(1-d,0),
\qquad
h^1(\operatorname{End}E)=\max(d-1,0).
\tag{DS.18}
\]

| Degree difference \(d\) | Infinitesimal automorphisms \(h^0\) | Bundle deformations \(h^1\) | Stack dimension \(h^1-h^0\) |
|---|---:|---:|---:|
| \(0\) | \(4\) | \(0\) | \(-4\) |
| \(1\) | \(4\) | \(0\) | \(-4\) |
| \(d\ge2\) | \(d+3\) | \(d-1\) | \(-4\) |

The stabilizer and deformation dimensions vary together. Their difference remains the dimension of \(\operatorname{Bun}_{GL_2}\) on the genus-zero curve. For the split torus \((\mathbb G_m)^r\), the adjoint bundle is \(\mathcal O_X^r\), so the same exact sequence gives \(rg-r=r(g-1)\). On a genus-one curve every reductive adjoint bundle has equal \(h^0\) and \(h^1\), by (DS.12)–(DS.14); this asserts a zero stack dimension, without asserting that either space vanishes.

**Exercise 2.A.** If \(E\) has rank \(r\) and \(L\) is an invertible sheaf, compute \(\chi(E\otimes L)-\chi(E)\). Explain why it does not require separate formulas for either cohomology dimension.

**Solution 2.A.** Taking the determinant of a local tensor-product basis gives
\(\det(E\otimes L)\simeq\det E\otimes L^{\otimes r}\). Degrees add by the divisor construction of §2.4. Equation (DS.14) therefore gives
\(\chi(E\otimes L)-\chi(E)=r\deg L\). This is an equality of alternating dimensions obtained from the exact-sequence argument; it puts no separate constraint on \(h^0\) and \(h^1\).

**Exercise 2.B.** Let \(B=\{\left(\begin{smallmatrix}a&b\\0&1\end{smallmatrix}\right):a\ne0\}\), the connected affine group \(\mathbb G_a\rtimes\mathbb G_m\). Compute its adjoint determinant. For a bundle induced from a line bundle \(L\) through \(a\mapsto\operatorname{diag}(a,1)\), compute the adjoint bundle and its Euler characteristic. Locate the reductivity hypothesis in §2.3.

**Solution 2.B.** With \(h=E_{11}\) and \(e=E_{12}\), direct matrix multiplication gives
\(\operatorname{Ad}(a,b)h=h-be\) and
\(\operatorname{Ad}(a,b)e=ae\). The matrix of the adjoint action in the ordered basis \(h,e\) has determinant \(a\). On the diagonal subgroup its weights are \(1,a\), so the associated adjoint bundle is \(\mathcal O_X\oplus L\). Equation (DS.14) gives Euler characteristic \(2(1-g)+\deg L\). The upper unitriangular subgroup is a nontrivial connected normal unipotent subgroup of \(B\); the inference \(U=1\) in §2.3 therefore fails for this group. The determinant conclusion of that proof uses reductivity essentially.

## 3. Why degree gives exactly the components of \(\operatorname{Bun}_{GL_n}\)

Degree is locally constant in a family of vector bundles on a proper curve. Indeed, Euler characteristic is locally constant for a flat proper family, and Riemann–Roch expresses it as \(\deg E+n(1-g)\). Thus there are disjoint open and closed substacks \(\operatorname{Bun}_n^d\). The work is to prove each is connected.

**Lemma 3.1.** The scheme \(\operatorname{Pic}^d(X)\) is connected for every integer \(d\).

**Proof.** Choose \(m\ge\max(0,2g-1)\). Riemann–Roch gives \(h^0(L)=m+1-g>0\) for every line bundle of degree \(m\). Every such \(L\) therefore has the form \(\mathcal O(D)\) for an effective divisor of degree \(m\). The Abel map \(\operatorname{Sym}^mX\to\operatorname{Pic}^mX\) is surjective: its proper image contains every closed point. The source is connected, since it is the image of the connected scheme \(X^m\). Hence the target is connected. Tensoring by \(\mathcal O((m-d)x)\), for any \(x\in X(k)\), identifies \(\operatorname{Pic}^d\) with \(\operatorname{Pic}^m\). \(\square\)

The algebraicity and representability of the Picard scheme used here are background inputs [Stacks, Tag 0B9Z]. The Picard stack in a fixed degree has the same connectedness: its map to the Picard scheme is a gerbe with connected fibre \(B\mathbb G_m\). A choice of a point of \(X\) gives a normalized Poincaré bundle and a neutralization, though connectedness does not require a chosen neutralization.

**Lemma 3.2.** Every vector bundle is connected, through algebraic families of the same rank and degree, to a direct sum of line bundles.

**Proof.** A nonzero vector in the generic fibre determines a rank-one subsheaf. Saturating it gives a line subbundle \(L\subset E\) with locally free quotient \(Q\): on a nonsingular curve, a torsion-free coherent sheaf is locally free. The extension class

\[
\eta\in\operatorname{Ext}^1(Q,L)
\]

can be multiplied by the coordinate \(t\) on \(\mathbb A^1\). The class \(t\eta\) defines a family of extensions on \(X\times\mathbb A^1\), with fibres \(E\) at \(t=1\) and \(L\oplus Q\) at \(t=0\). One may construct the family by multiplying the off-diagonal terms in transition matrices by \(t\); the extension cocycle equations are linear in those terms. The middle term remains locally free. Repeat with \(Q\) by induction on the rank. Each step keeps total degree fixed and has a connected parameter scheme. \(\square\)

**Lemma 3.3.** For line bundles \(L,M\) and \(x\in X(k)\), the bundles \(L\oplus M\) and \(L(-x)\oplus M(x)\) lie in the same connected component.

**Proof.** Start with \(V=L\oplus M(x)\). Its elementary modifications of length one at \(x\) are parameterized by the projective line of one-dimensional quotients of \(V_x\), as proved in the previous lesson. The universal kernel is a vector bundle on \(X\times\mathbb P(V_x^*)\). At the quotient supported on the second summand its kernel is \(L\oplus M\). At the quotient supported on the first summand it is \(L(-x)\oplus M(x)\). Both are fibres of this connected family. \(\square\)

**Theorem 3.4.** The degree map induces a bijection

\[
\pi_0(\operatorname{Bun}_{GL_n})\simeq\mathbb Z.
\]

**Proof.** Lemma 3.2 connects any \(E\in\operatorname{Bun}_n^d\) to \(L_1\oplus\cdots\oplus L_n\). Apply Lemma 3.3, in either direction and as many times as necessary, to transfer degrees from the last \(n-1\) summands to the first. This connects the sum to one with degree list \((d,0,\ldots,0)\). By Lemma 3.1, each degree-zero summand can be varied to \(\mathcal O_X\), and the first can be varied to the fixed line bundle \(\mathcal O_X(dx)\). Products of the corresponding Picard stacks are connected, and direct sum gives a morphism from that product to the bundle stack. Thus all \(k\)-points in degree \(d\) belong to one connected component. Every nonempty component of a stack locally of finite type over an algebraically closed field contains such a point. The degree-\(d\) stack is therefore connected. Every integer occurs, through \(\mathcal O_X(dx)\oplus\mathcal O_X^{n-1}\), and local constancy separates distinct degrees. \(\square\)

For a general connected reductive group the component theorem is

\[
\pi_0(\operatorname{Bun}_G)\simeq
\pi_{1,\mathrm{alg}}(G):=X_*(T)/\langle\text{coroots}\rangle.
\]

Here \(T\) is a maximal torus. This is the algebraic fundamental group from the root datum, not the étale fundamental group of the variety \(G\). We use the general component theorem as an input [Drinfeld–Gaitsgory, §7.2.4]. The semisimple case also appears in [Beilinson–Drinfeld, §2.1.1] and [Heinloth, Theorem 2]. The vector-bundle proof above is independent of this input. For a torus the result follows directly from its cocharacter lattice and the Picard calculation.

## 4. Stability, bounded pieces, and growing stabilizers

A vector bundle \(E\) of positive rank has slope \(\mu(E)=\deg E/\operatorname{rk}E\). It is semistable if every nonzero proper subbundle \(F\) satisfies \(\mu(F)\le\mu(E)\), and stable if every such inequality is strict. Saturation lets us use subbundles rather than all subsheaves: saturation increases degree without changing rank, so it supplies the strongest test.

For a principal bundle, reductions to maximal proper parabolics replace subbundles. If \(P_0\subset G\) is such a parabolic and \(P_{P_0}\) is a reduction, let \(\mathfrak n_{P_0}\) be the Lie algebra of its unipotent radical. Our sign convention defines semistability by

\[
\deg\bigl((\mathfrak n_{P_0})_{P_{P_0}}\bigr)\le0
\]

for every reduction, and stability by strict inequality. For \(GL_n\), the reduction belonging to \(F\subset E\), with rank \(r\), has unipotent Lie bundle \(\operatorname{Hom}(E/F,F)\), of degree

\[
n\deg F-r\deg E.
\]

Thus the convention recovers slope stability. In root notation this degree is \(\langle2\rho_{P_0},\deg P_{P_0}\rangle\). This is the convention in [Gaitsgory–Raskin, §9.1]. For a torus there are no proper parabolics, so the stability test is vacuous.

The Harder–Narasimhan theorem gives a unique filtration of a vector bundle with semistable quotients of strictly decreasing slopes, and a corresponding canonical parabolic reduction for principal bundles [Drinfeld–Gaitsgory, Theorem 7.4.3]. We state this theorem, together with openness and boundedness: in a fixed topological component, the semistable locus is an open quasicompact substack [Drinfeld–Gaitsgory, §7.3.2, Proposition 7.3.5]. These are background stability results, not consequences merely of smoothness. The fixed-component qualification matters: the semistable locus of the entire Picard stack is an infinite disjoint union of degree components and is not quasicompact.

Consider now \(X=\mathbb P^1\) and \(E_d=\mathcal O\oplus\mathcal O(d)\), with \(d>0\). Relative to this order of summands,

\[
\operatorname{Aut}(E_d)=
\left\{\begin{pmatrix}a&0\\s&b\end{pmatrix}:
a,b\in k^\times,\quad s\in H^0(\mathbb P^1,\mathcal O(d))\right\}.
\]

Its dimension is \(2+(d+1)=d+3\). The diagonal entries must be units; their nonzero product is also sufficient for invertibility, since the lower triangular inverse is again of the displayed form. For \(d=0\) the group is \(GL_2\), of dimension four. For \(d<0\) interchange the summands, obtaining dimension \(|d|+3\).

This example varies degree. To see unboundedness even in a fixed degree, use

\[
E_m=\mathcal O(m)\oplus\mathcal O(-m),\qquad m>0.
\]

These all have degree zero, and their automorphism groups have dimension \(2m+3\). A quasicompact algebraic stack locally of finite type with finite type diagonal has a uniform bound on stabilizer dimensions: cover it by finitely many finite type charts, pull back the inertia, and use the bound on fibre dimensions of a finite type morphism. The dimensions \(2m+3\) contradict such a bound. Hence \(\operatorname{Bun}_2^0(\mathbb P^1)\) is not quasicompact.

The same mechanism works on any \(X\) in rank at least two: take \(L_m\oplus L_m^{-1}\oplus\mathcal O^{n-2}\), with \(\deg L_m=m\to\infty\). Riemann–Roch gives \(h^0(L_m^2)=2m+1-g\) once \(2m>2g-2\), yielding unbounded stabilizers in degree zero. This argument is sufficient for the vector-bundle example. It does not say that each fixed-degree Picard stack is nonquasicompact.

## 5. Cotangent vectors are Higgs fields

Dualizing Proposition 2.1 gives the cotangent complex. Its degree-zero cohomology at \(P\) is

\[
H^0(T_P^*\operatorname{Bun}_G)
=H^1(X,\operatorname{ad}(P))^*
\simeq H^0(X,\operatorname{ad}(P)^*\otimes\omega_X),
\]

by Serre duality. A cotangent vector is therefore a coadjoint-valued one-form, called a Higgs field. For \(GL_n\), the trace pairing identifies \(\operatorname{End}(E)^*\) with \(\operatorname{End}(E)\), so it is a map

\[
\phi:E\longrightarrow E\otimes\omega_X.
\]

This identifies the classical cotangent stack \(T^*\operatorname{Bun}_G\) with the stack of pairs \((P,\phi)\). It is more than a pointwise dimension calculation. For a family, relative Serre duality identifies a linear functional on \(R\pi_*\operatorname{ad}(P)[1]\) with a global section of \(\operatorname{ad}(P)^*\otimes\omega_{X\times S/S}\). This description commutes with base change and gives the required equivalence of moduli functors. It also explains why jumping \(h^0\) need not give an ordinary vector bundle over the whole stack. See [Beilinson–Drinfeld, §2.2.3] for the construction.

For \(GL_n\), expand the characteristic polynomial as

\[
\det(t-\phi)=t^n+a_1t^{n-1}+\cdots+a_n,
\qquad a_i\in H^0(X,\omega_X^i).
\]

The powers of \(\omega_X\) follow from homogeneity: the coefficient is homogeneous of degree \(i\) in the matrix entries of a one-form-valued endomorphism. The **Hitchin map** is

\[
h:T^*\operatorname{Bun}_n\longrightarrow
\mathcal A_n:=\bigoplus_{i=1}^nH^0(X,\omega_X^i),
\qquad (E,\phi)\longmapsto(a_1,\ldots,a_n).
\]

For general \(G\), choose homogeneous generators of \(k[\mathfrak g^*]^G\), with degrees \(d_1,\ldots,d_r\). They give a presentation of the Hitchin base as \(\bigoplus_jH^0(X,\omega_X^{d_j})\). The base itself is canonical; the choice of polynomial generators need not be. An invariant nondegenerate pairing can identify adjoint and coadjoint bundles, but the definition should not depend on an unstated choice of pairing.

For \(GL_2\), Riemann–Roch and Serre duality give

\[
\dim\mathcal A_2=
\begin{cases}
4g-3,&g\ge2,\\
2,&g=1,\\
0,&g=0.
\end{cases}
\]

Indeed \(h^0(\omega_X)=g\). For \(g\ge2\), \(h^1(\omega_X^2)=h^0(\omega_X^{-1})=0\) and \(h^0(\omega_X^2)=3g-3\). In genus one the canonical bundle is trivial, so both summands have dimension one. On the projective line they are \(\mathcal O(-2)\) and \(\mathcal O(-4)\), with no sections.

When \(g\ge2\), the base has dimension one more than \(\dim\operatorname{Bun}_2=4g-4\). This is compatible with the generic Higgs fibre: it is a Picard stack of a smooth spectral curve, not its Picard scheme. The double spectral cover has genus \(4g-3\), so its Picard stack has dimension \(4g-4\). On the stable bundle locus the coarse moduli dimension is also \(4g-3\), because scalar automorphisms have dimension one. Forgetting the scalar stabilizer in just one of these calculations creates the apparent discrepancy.

The spectral-curve statement in this paragraph is explanatory background: for a smooth spectral cover, the spectral correspondence identifies Higgs bundles with line bundles on it. The genus follows from Riemann–Hurwitz: a generic discriminant is a section of \(\omega_X^2\), with \(4g-4\) simple zeros, and \(2g_{\Sigma}-2=2(2g-2)+(4g-4)\). We use neither a spectral correspondence nor smoothness of a generic spectral curve in the proofs above.

## 6. The global nilpotent cone

The global nilpotent cone is the zero fibre

\[
\operatorname{Nilp}_G=h^{-1}(0)\subset T^*\operatorname{Bun}_G.
\]

For \(GL_n\), its points are Higgs fields with characteristic polynomial \(t^n\). Cayley–Hamilton then gives \(\phi^n=0\), interpreted as a map \(E\to E\otimes\omega_X^n\). Conversely a nilpotent Higgs field has all characteristic coefficients zero. If it is nilpotent over the function field, those coefficients vanish there and hence everywhere on the integral curve. Thus generic nilpotence and everywhere nilpotence agree for individual fields. A family is defined scheme-theoretically by the invariant-polynomial equations, retaining the zero fibre's possibly nonreduced structure.

The target theorem is that the reduced global nilpotent cone is Lagrangian in the cotangent stack for every connected reductive \(G\) and every genus. [Beilinson–Drinfeld, Theorem 2.10.4] gives the semisimple comparison in every genus; [Ginzburg, Main Theorem] gives the \(g>1\) argument and its reductive qualification. Sections 6.1–6.3 give the nilpotent Lie triple, canonical parabolic reduction and isotropy. Sections 6.4–6.12 prove the dimension equality in every genus, including the reductive central correction and an algebraic elliptic tensor/reduction argument. Bundle-stack algebraicity is proved in §1.5; the remaining recursive Lie/flag/cohomology foundations retain the explicit boundary in §6.4.

The word Lagrangian has a precise stack interpretation. If \(U\to\operatorname{Bun}_G\) is a smooth presentation, then

\[
\operatorname{Nilp}_G\times_{\operatorname{Bun}_G}U
\hookrightarrow
T^*\operatorname{Bun}_G\times_{\operatorname{Bun}_G}U
\hookrightarrow T^*U
\]

is Lagrangian after taking its reduction. The symplectic form vanishes on its smooth locally closed subvarieties, and its components have half the ambient dimension. This is independent of the presentation. A zero fibre of an arbitrary map from a symplectic space need not have these properties; the theorem is additional geometry.

For a torus, the invariant linear coordinates already force the Higgs field to be zero. The nilpotent cone is the zero section, which is Lagrangian in this presentation sense. For example, locally \(\operatorname{Bun}_{\mathbb G_m}^d\simeq\operatorname{Pic}^d\times B\mathbb G_m\). In a presentation \(\operatorname{Pic}^d\to\operatorname{Pic}^d\times B\mathbb G_m\), the cone becomes the zero section of \(T^*\operatorname{Pic}^d\), of dimension \(g\), even though the original stack has dimension \(g-1\).

Write \(M=\operatorname{Bun}_G(X)\), and let \(\mathcal N_G\) denote the reduced zero fibre of the invariant-polynomial Hitchin map. The theorem to prove is:

> For every smooth presentation \(a:A\to M\), the image of \(\mathcal N_G\times_M A\) in \(T^*A\) is isotropic and every one of its irreducible components has dimension \(\dim A\).

One uses reductions throughout. The scheme-theoretic zero fibre need not be reduced; “Lagrangian” here concerns its reduction. No stable-locus restriction is imposed.

Choose a \(G\)-invariant nondegenerate symmetric pairing on \(\mathfrak g\). Such a pairing is obtained from the Killing form on the semisimple derived algebra and any nondegenerate pairing on the centre. It identifies \(\operatorname{ad}(P)^*\) with \(\operatorname{ad}(P)\). The theorem and the zero fibre are independent of this auxiliary identification.

The cotangent description already proved in the lesson gives

\[
T^*M(S)=\{(P,\phi):\phi\in H^0(X_S,\operatorname{ad}(P)\otimes\omega_{X_S/S})\}.
\]

The form on \(T^*A\) is \(d\lambda_A\), where \(\lambda_A\) is the tautological one-form: on a tangent vector to a pair \((u,\xi)\), it evaluates \(\xi\) on the variation of \(u\). All later isotropy calculations use this formula, so there is no implicit sign convention.

### 6.1. The nilpotent Lie triple

The Lie argument uses Jordan decomposition, the Killing form, Cartan root spaces and the representation strings of \(\mathfrak{sl}_2\). Relevant arguments include [*The Killing form and Cartan's criteria*](../../RT-LIE/src/RT-LIE-03.md) Theorem 3.3 and Lemma 6.1/Theorem 6.2, the Jordan and complete-reducibility arguments in [*Complete reducibility: Casimir elements and Weyl's theorem*](../../RT-LIE/src/RT-LIE-04.md), and the algebraic rank-one module construction in [*Representations of sl(2)*](../../RT-LIE/src/RT-LIE-05.md) Proposition 2.2. [*The root space decomposition of a semisimple Lie algebra*](../../RT-LIE/src/RT-LIE-07.md)'s Cartan/root-space proof is written over \(\mathbb C\); a complete algebraic proof or field-transfer argument with the exact matching generality is still required for its use over every algebraically closed characteristic-zero field here. The following mechanism is conditional on that Lie foundation and the flag/parabolic, torsor-stack and curve-duality foundations; those obligations do not change the statement to be proved.

**Lemma 6.1.** Let \(\mathfrak s\) be a semisimple Lie algebra over an algebraically closed field of characteristic zero. For every nonzero nilpotent \(e\in\mathfrak s\), there are \(h,f\in\mathfrak s\) with

\[
[h,e]=2e,\qquad [h,f]=-2f,\qquad [e,f]=h.
\]

**Proof.** Induct on \(\dim\mathfrak s\). First suppose that the centralizer \(\mathfrak s^e\) contains a nonzero semisimple element \(s\). The root-space decomposition, after putting \(s\) in a Cartan subalgebra, shows that \(\mathfrak l=\mathfrak s^s\) is a proper reductive algebra. Its centre is toral, and its derived algebra is semisimple. The nilpotent element \(e\) lies in \([\mathfrak l,\mathfrak l]\): its central component would otherwise be a nonzero commuting semisimple summand in its Jordan decomposition. Apply the induction hypothesis in \([\mathfrak l,\mathfrak l]\).

It remains to consider the case in which \(\mathfrak s^e\) has no nonzero semisimple element. Every element of \(\mathfrak s^e\) is then nilpotent, because its semisimple Jordan summand also centralizes \(e\).

Let \(\kappa\) be the Killing form. If \(z\in\mathfrak s^e\), then \(\operatorname{ad}e\) and \(\operatorname{ad}z\) commute; their product is nilpotent since \(\operatorname{ad}e\) is nilpotent. Consequently

\[
\kappa(e,z)=\operatorname{tr}(\operatorname{ad}e\operatorname{ad}z)=0.
\]

Invariance and nondegeneracy of \(\kappa\) give

\[
(\mathfrak s^e)^\perp=[e,\mathfrak s].
\]

Indeed the annihilator of \([e,\mathfrak s]\) is exactly the kernel of \(\operatorname{ad}e\), so the equality follows by taking annihilators. There is therefore an \(h_0\) such that \([h_0,e]=2e\). Replace \(h_0\) by its semisimple Jordan part \(h\). The Jordan decomposition of \(\operatorname{ad}h_0\) preserves its eigenvector \(e\), and on that eigenvector the semisimple part has eigenvalue \(2\) and the nilpotent part is zero. Thus \([h,e]=2e\).

Decompose \(z\in\mathfrak s^e\) into the eigenspaces of \(\operatorname{ad}h\). Every component \(z_m\) still centralizes \(e\), because \([e,z_m]\) has weight \(m+2\). For \(m\ne0\), invariance gives \(m\kappa(h,z_m)=\kappa(h,[h,z_m])=0\). The weight-zero component commutes with \(h\), and is nilpotent by the case assumption. Hence \(\operatorname{ad}h\operatorname{ad}z_0\) is nilpotent and \(\kappa(h,z_0)=0\). We obtain \(h\perp\mathfrak s^e\), so \(h=[e,y]\) for some \(y\). Taking the weight \(-2\) component of \(y\) gives \(f\) with \([e,f]=h\) and \([h,f]=-2f\). These are the required relations. \(\square\)

For a reductive algebra, nilpotent elements have zero central component, and the lemma applies to the derived algebra.

### 6.2. The canonical parabolic and its extension over the curve

**Lemma 6.2.** A nilpotent element in a reductive Lie algebra has a canonical decreasing filtration \(F^j\), and \(F^0\) is a parabolic algebra whose nilradical contains the element. The filtration is preserved by scalar multiplication of the element and descends over any characteristic-zero field and any inner form.

**Proof.** Put \(N=\operatorname{ad}e\). For a nilpotent linear operator define, using only kernels, images, intersections, and sums,

\[
F^j V=\sum_{i\ge\max(0,-j)}\bigl(\ker N^{i+1}\cap\operatorname{im}N^{i+j}\bigr).
\tag{6.1}
\]

Terms with exponent larger than the nilpotence index vanish, so this is a finite sum. On a Jordan block of length \(n+1\), choose the weights \(-n,-n+2,\ldots,n\), with \(N\) raising the weight by two. Direct inspection of that block shows that (6.1) is the span of the vectors of weight at least \(j\). The calculation is independent of a chosen Jordan basis, because the right side of (6.1) is intrinsic.

Use Lemma 6.1 on \(\mathfrak g\). The decomposition into \(\mathfrak{sl}_2\)-modules shows that \(F^j\mathfrak g\) is precisely the sum of the \(h\)-weight spaces with weight at least \(j\). In particular, \(e\in F^2\mathfrak g\). After putting \(h\) in a Cartan subalgebra, its root values are integers. A positive integer multiple of \(h\) is the differential of a cocharacter: this follows by clearing denominators in the cocharacter lattice of the torus. The root-space description of the parabolic of that cocharacter gives its Lie algebra \(F^0\mathfrak g\) and its nilradical \(F^1\mathfrak g\). Moreover

\[
(F^0\mathfrak g)^\perp=F^1\mathfrak g,
\tag{6.2}
\]

because an invariant pairing matches only opposite \(h\)-weights.

The stabilizer in \(G\) of the complete filtration is this parabolic: its positive-root subgroup preserves the filtration, and a filtration-preserving element normalizes \(F^0\mathfrak g\), whose normalizer is the parabolic itself by the root-space description. Formula (6.1) is defined over the field of definition of \(e\), and is unchanged when \(e\) is multiplied by a nonzero scalar. Thus its parabolic stabilizer descends. The same argument works for an inner form after passing to an algebraic closure and descending the intrinsic filtration. No generic trivialization of the original torsor is required. \(\square\)

**Lemma 6.3.** Every nilpotent Higgs field \((P,\phi)\) has a reduction to some parabolic \(Q\subset G\) such that \(\phi\) lies in the nilradical bundle of that reduction.

**Proof.** At the function field of \(X\), trivialize the canonical line and apply Lemma 6.2 in the inner Lie algebra \(\operatorname{ad}(P)\). Scalar invariance removes dependence on that trivialization. The resulting parabolic is a point of the associated projective flag bundle \(P/Q\). Properness extends its section across each missing point of the nonsingular curve, by the valuative criterion for the local DVRs. The projection of \(\phi\) to the quotient by the nilradical vanishes generically, and is a regular section of a vector bundle. It therefore vanishes everywhere. \(\square\)

The same construction has the following spreading property. If a reduced irreducible finite-type scheme \(S\) carries a nilpotent Higgs family, perform the construction on the curve over \(k(S)\). The reduction, defined on the entire generic fibre of the curve, spreads to \(X\times S_0\) for some nonempty open \(S_0\subset S\), since the flag bundle and the section have finite presentation. After shrinking \(S_0\), the vanishing in the quotient by the nilradical also spreads. Noetherian induction gives a finite stratification of a finite-type parameter scheme with a reduction on every stratum. This argument replaces the countable-cover argument in Ginzburg and works over countable algebraically closed fields as well.

### 6.3. Vanishing of the tautological one-form

For a fixed parabolic \(Q\), let \(f:\operatorname{Bun}_Q\to\operatorname{Bun}_G\) forget the reduction. The deformation calculation of the lesson applies to \(Q\) as a smooth affine group as well: its obstruction group is \(H^2(X,\mathfrak q_P)=0\), so \(\operatorname{Bun}_Q\) is smooth once its algebraicity is established by the same torsor-stack argument. Duality identifies the pullback of a Higgs covector along \(df\) with its image in

\[
H^0(X,\mathfrak q_P^*\otimes\omega_X).
\]

By (6.2), this pullback is zero when the Higgs field belongs to the nilradical bundle.

Take a smooth presentation \(A\to M\), and write \(N=A\times_M\operatorname{Bun}_Q\). It is smooth, because \(N\to\operatorname{Bun}_Q\) is the smooth base change of \(A\to M\). Let \(F:N\to A\) be the projection. A covector \(\xi\in T_u^*A\) coming from the cotangent stack pulls back to zero along \(dF\) exactly when the original Higgs field pulls back to zero along \(df\).

Now let \(W\) be an irreducible smooth locally closed subvariety of \(\mathcal N_G\times_M A\). The spreading argument gives a nonempty open \(W_0\subset W\) and a map \(r:W_0\to N\) carrying its canonical parabolic reduction. At a tangent vector \(v\in T_wW_0\),

\[
(\lambda_A|_{W_0})(v)
=\xi\bigl(dF(dr(v))\bigr)=0.
\]

Thus \(d\lambda_A\) vanishes on \(W_0\). It vanishes on all of \(W\), because it is a regular two-form and \(W_0\) is dense. Repeating on irreducible components proves isotropy on every smooth locally closed subvariety. In particular every irreducible component of the reduced cone in \(T^*A\) has dimension at most \(\dim A\).

This proves isotropy for every connected reductive \(G\), in every genus, in algebraic characteristic zero. It does not appeal to Steinberg's generic torsor-triviality theorem or to a countable-union assertion.

The cone controls allowed automorphic singularities in later lessons. Its role here is to give a geometric condition on covectors; it is not yet the spectral singular-support condition on the derived stack of local systems.

The ground field in the main statement is **algebraically closed of characteristic zero**. The curve \(X\) is smooth, projective and connected, and \(G\) is connected reductive. Put \(M=\operatorname{Bun}_G(X)\). For a smooth presentation \(a:A\to M\), work on an open on which \(A\) is a smooth finite-type scheme and the relative dimension of \(a\) is \(m\). Write \(n=\dim A\). The cotangent pullback has its usual closed immersion into \(T^*A\). Let \(N_A\) be the reduction of the image of the global nilpotent cone under this immersion.

**Dimension theorem, conditional on the exact stack and programme foundations in N0.** Every irreducible component of \(N_A\) has dimension \(n\). Together with the already written chartwise isotropy proof, this says that the reduced global nilpotent cone is Lagrangian for every genus and every connected reductive \(G\).

We prove the three genus cases below. In genus one, we construct the necessary adjoint Harder–Narasimhan reduction from vector bundles. We do not assume the principal Harder–Narasimhan theorem, the equivalence between Ramanathan semistability and adjoint semistability, or a theorem about tensor products of semistable bundles. No countability argument is used.

### 6.4. Precise foundations and the chart (N0)

The argument uses the local Lie/parabolic and isotropy proofs above and the earlier mathematical arguments specified below. Their remaining recursive foundations retain the stated proof obligations.

* The algebraicity of \(M\), its affine finitely presented diagonal and local finite presentation are proved by the explicit atlas in §1.5. Section 1.6 also proves effectivity and full faithfulness for complete Noetherian local formal bundle families. Smoothness and the tangent complex are the lesson's Čech deformation calculation: \(T_{M,P}=R\Gamma(X,\operatorname{ad}P)[1]\). On a curve the obstruction \(H^2\) is zero.
* The local canonical nilpotent filtration and its isotropy proof are proved in §§6.1–6.3 at the stated hypotheses. Thus every component of \(N_A\) has dimension at most \(n\), after its indicated Lie/group and geometric foundations are supplied. N7 below gives an algebraic torus argument for the Lie-of-\(G\) semisimple centralizer step, using the all-field AG-RG arguments, so a complex-only Cartan argument need not be transferred silently.
* [*Cohomology of affine schemes and Serre's criterion*](../../AG-QC/src/affine-cohomology-and-serres-criterion.md) supplies affine vanishing and finite affine Čech computation; [*Coherent sheaves on projective schemes: Serre's theorems*](../../AG-QC/src/serres-theorems-on-projective-schemes.md), Theorem 2.1 and Corollary 2.3, supplies relative Serre generation and projective cohomological finiteness; [*Base change and the Grothendieck complex*](../../AG-QC/src/base-change-and-the-grothendieck-complex.md), Lemma 3.1 and Theorem 3.2, supplies the universal finite projective cohomology complex for flat coherent families. [*Dualizing sheaves and Serre duality for projective schemes*](../../AG-QC/src/dualizing-sheaves-and-serre-duality-for-projective-schemes.md), Theorems 4.1–4.2, supplies projective duality. The local Koszul calculation identifying the dualizing line of a smooth curve with \(\Omega_X^1\) is recalled below. [*Hilbert and Quot schemes*](../../AG-HP/src/hilbert-and-quot-schemes.md), Theorem 4.1 and Corollary 4.2, supplies the projective Quot and Hilbert schemes. [*The Picard functor and the Picard scheme of a curve*](../../AG-HP/src/the-picard-functor-and-the-picard-scheme-of-a-curve.md), Theorem 2.1, Proposition 5.1 and Theorem 6.2, supplies normalized line bundles and the smooth Picard scheme. These calculations retain the stated hypotheses and the remaining algebraic and geometric foundations listed below.
* The Lie and group ingredients used here are [*Nilpotent and solvable Lie algebras: Engel's and Lie's theorems*](../../RT-LIE/src/RT-LIE-02.md), [*The Killing form and Cartan's criteria*](../../RT-LIE/src/RT-LIE-03.md), [*Complete reducibility: Casimir elements and Weyl's theorem*](../../RT-LIE/src/RT-LIE-04.md), [*Representations of sl(2)*](../../RT-LIE/src/RT-LIE-05.md) and the characteristic-zero extension sections of [*The isomorphism theorem and Serre's theorem*](../../RT-LIE/src/RT-LIE-11.md) and [*Weights, Verma modules and the theorem of the highest weight*](../../RT-LIE/src/RT-LIE-14.md), together with [*Tori, maximal tori and their conjugacy*](../../AG-RG/AG-RG-01.html), [*Roots and reductive groups of rank one*](../../AG-RG/AG-RG-03.html), [*Root data, Weyl chambers and the Bruhat decomposition*](../../AG-RG/AG-RG-04.html), [*Pinnings and the classification of split reductive groups*](../../AG-RG/AG-RG-05.html), [*Automorphisms, forms and parabolic subgroups*](../../AG-RG/AG-RG-06.html). In particular, Engel's triangularization is [*Nilpotent and solvable Lie algebras: Engel's and Lie's theorems*](../../RT-LIE/src/RT-LIE-02.md), Theorem 2.1; the all-base parabolic parameter scheme and its projective quotient are [*Automorphisms, forms and parabolic subgroups*](../../AG-RG/AG-RG-06.html), Theorems 1.1–2.1. Their remaining mathematical foundations are stated explicitly below.

For a smooth morphism \(A\to M\), let \(E=T_{A/M}\), a vector bundle of rank \(m\), and let \(\rho:E\to T_A\) be its differential. The classical cotangent pullback is

\[
T^*M\times_M A=\{(x,\xi):\xi\circ\rho_x=0\}\subset T^*A. \tag{N0.1}
\]

Indeed the cotangent triangle \(a^*L_M\to L_A\to L_{A/M}\), dualized, says precisely that a functional on \(T_A\) comes from a degree-zero cotangent vector of \(M\) if and only if it kills the relative tangent bundle. This identifies the functors on arbitrary ordinary test schemes, rather than just their geometric fibres. Locally (N0.1) is the zero locus of \(m\) scalar functions, with relations whenever \(\rho\) has a kernel.

Let \(z=\dim Z(G)^0\). The invariant decomposition \(\mathfrak g=\mathfrak z\oplus[\mathfrak g,\mathfrak g]\) gives a constant central summand \(\mathfrak z\otimes\mathcal O_X\) in every adjoint bundle. The boundary map in the tangent triangle embeds \(\mathfrak z\otimes\mathcal O_A\) into \(E\), and its composite with \(\rho\) is zero. Its fibre is the injection of the infinitesimal central automorphisms into the relative tangent space; hence it is a locally direct summand of \(E\). Consequently (N0.1) needs at most \(m-z\) equations locally. This is an identity of bundle maps over \(A\), including nonreduced test schemes.

For later use, here is the elementary Riemann–Roch calculation. A rational nonzero section of a line bundle \(L\) identifies it with \(\mathcal O_X(D)\). The exact sequence for adding one point changes its Euler characteristic by one. Since \(\chi(\mathcal O_X)=1-g\), this proves \(\chi(L)=\deg L+1-g\). A vector bundle has a saturated line subbundle: extend a nonzero vector of its generic fibre, then saturate; torsion-free sheaves on a nonsingular curve are locally free. Induction on rank and additivity prove

\[
\chi(V)=\deg V+(1-g)\operatorname{rk}V. \tag{N0.2}
\]

The identification of the dualizing line with \(\Omega_X^1\) is local: embed \(X\) in a smooth projective space, use the regular conormal sequence, and resolve its ideal by the local Koszul complex. Its top dual term is \(\det(I/I^2)^\vee\otimes\omega_{\mathbf P}|_X\). The determinant of \(0\to I/I^2\to\Omega_{\mathbf P}|_X\to\Omega_X\to0\) identifies that line with \(\Omega_X\); the Koszul identifications agree under change of regular generators. Thus [*Dualizing sheaves and Serre duality for projective schemes*](../../AG-QC/src/dualizing-sheaves-and-serre-duality-for-projective-schemes.md) duality gives \(h^0(\omega_X)=g\), \(h^1(\omega_X)=1\), and (N0.2) gives \(\deg\omega_X=2g-2\). In genus one a nonzero section of \(\omega_X\) has no zeros, so \(\omega_X\simeq\mathcal O_X\).

For arbitrary ordinary bases, the finite cohomology complex just cited still applies to the vector bundles used here. On an affine \(\operatorname{Spec}A\), choose a finite affine cover \(\operatorname{Spec}R_i\) of the fixed curve. Refine its base changes by finitely many distinguished opens on which the vector bundle is trivial. The distinguished-open equations, transition matrices, their inverses, and cocycle relations involve only finitely many coefficients of \(A\). Include also the finitely many unit-ideal identities proving that these opens cover each \(\operatorname{Spec}(R_i\otimes_kA)\). All this data is defined over a finitely generated \(k\)-subalgebra \(A_0\subset A\). The unit-ideal identities ensure that the descended opens still cover, and the matrix identities glue a vector bundle on \(X_{A_0}\) whose pullback is the original one. The [*Base change and the Grothendieck complex*](../../AG-QC/src/base-change-and-the-grothendieck-complex.md) argument gives a finite projective \(K_0\) computing cohomology after every \(A_0\)-algebra change. Pull it back to \(A\). Whenever fibre cohomology is zero outside degree zero, split off the contractible pairs corresponding to invertible differential entries near each parameter point. The remaining terms have zero fibre rank except in degree zero, so disappear there; the degree-zero term is locally free. Every cancellation remains valid after every tensor. This proves the locally free pushforward and arbitrary base-change claims used later, even for non-Noetherian or nonreduced \(A\). The construction concerns the cohomology complex; it never assumes that its individual cohomology sheaves always commute with base change.

The adjoint determinant of connected reductive \(G\) is trivial: on a maximal torus its weights are the roots in opposite pairs and zero weights, and root groups admit no nontrivial multiplicative character. Therefore every \(\operatorname{ad}P\) has degree zero. The Čech tangent calculation and (N0.2) give

\[
\dim M=(g-1)\dim G=:d,\qquad n=d+m. \tag{N0.3}
\]

### 6.5. Genus at least two, including the centre (N1)

We include the invariant degree calculation so that the required count is explicit. For the simply connected semisimple group with the same derived Lie algebra, let \(T\) be a maximal torus and \(W\) its Weyl group. Its fundamental representation characters \(\chi_i\) freely generate \(k[T]^W\). To prove this, use orbit sums of dominant weights as a basis. A monomial in the fundamental characters has a unique highest dominant weight, of coefficient one, and lower remaining weights. Induction in the dominance order proves generation, and distinct leading weights prove independence. The induction is finite because an interior positive coroot bounds the dominant weights below a fixed weight. The required fundamental representations and their characteristic-zero group realizations remain the highest-weight and group foundations of this argument.

Complete at \(1\in T\). The formal exponential is \(W\)-equivariant and identifies this completed invariant algebra with \(k[[\mathfrak t^*]]^W\). It is a regular local ring of dimension \(r=\operatorname{rk}G_{\mathrm{der}}\), because the character algebra is polynomial. Hence the graded algebra \(k[\mathfrak t]^W\) has \(r\) indecomposable positive-degree generators. Choose a homogeneous basis of its maximal ideal modulo its square. Induction on degree shows that it generates; the dimension shows algebraic independence.

They extend to the Lie algebra: the homogeneous coefficients in

\[
\chi_i(\exp H)=\sum_{j\ge0}\operatorname{tr}(\rho_i(H)^j)/j!
\]

are restrictions of invariant polynomials on \(\mathfrak g\), and span the indecomposable quotient just used. Regular semisimple elements are dense and conjugate into \(\mathfrak t\), so restriction is injective as well. We obtain homogeneous invariant generators \(Q_i\), of degrees \(d_i\ge2\), for the derived Lie algebra.

The Jacobian of the quotient \(\mathfrak t\to\mathfrak t/W\) has simple zeros exactly on the root hyperplanes. Off these hyperplanes stabilizers are trivial; generically on one hyperplane the stabilizer is its order-two reflection, whose local quotient is \((u_1,u_2,\ldots)\mapsto(u_1^2,u_2,\ldots)\). Thus the Jacobian divisor gives

\[
\sum_i(d_i-1)=|\Phi^+|,\qquad
\sum_i(2d_i-1)=\dim G_{\mathrm{der}}. \tag{N1.1}
\]

These stabilizer assertions can be checked in the real reflection representation of the rational root datum. If a Weyl element fixes a regular complex vector, it fixes its real and imaginary parts, hence a regular real combination, and therefore a chamber, whose stabilizer is trivial. Generically on a single wall only its reflection remains. The matrices and closed exceptional loci are defined over the rational root datum, so their verified identities extend to every characteristic-zero field; no embedding of the given \(k\) into \(\mathbb C\) is assumed.

Add \(z\) central degree-one generators. Their common zero locus with the derived generators is the nilpotent cone. For completeness, the local Jacobson–Morozov proof gives a cocharacter contracting a nilpotent element and forces every positive-degree invariant to vanish there. For the converse, take the Jordan decomposition and contract the nilpotent part inside the reductive centralizer of the semisimple part. Every invariant has the same value on the element and its semisimple part. Finite Weyl invariants have zero fibre only at zero: for a nonzero vector choose a linear form nonzero on every point of its finite orbit and take the product of its Weyl translates. Thus the semisimple part and the central part must vanish.

For \(g\ge2\), duality and (N0.2) give

\[
\begin{aligned}
D:=\dim\mathcal A_G
&=\sum_i(2d_i-1)(g-1)+zg\\
&=(g-1)\dim G+z=d+z.
\end{aligned} \tag{N1.2}
\]

Each higher-degree differential has no first cohomology because its Serre-dual line has negative degree. The centre contributes \(zg\), rather than \(z(g-1)\).

The zero Hitchin fibre imposes \(D\) scalar equations on (N0.1). After lifting these functions locally to \(T^*A\), its ideal has at most

\[
(m-z)+(d+z)=m+d=n
\]

generators. The Krull height theorem is [*Dimension theory of Noetherian local rings*](../../AG-CA/src/dimension-theory-of-noetherian-local-rings.md), Theorem 3.1: a prime minimal over an ideal generated by \(n\) elements has height at most \(n\). Applied in the smooth \(2n\)-dimensional chart, with the finite-type dimension formula of [*Krull dimension and Noether normalization*](../../AG-CA/src/krull-dimension-and-noether-normalization.md), it shows that every component has dimension at least \(n\). Isotropy gives the reverse bound. This proves the theorem for \(g\ge2\).

### 6.6. Genus zero on an arbitrary smooth presentation (N2)

In genus zero \(\deg\omega_X<0\), so every \(H^0(X,\omega_X^j)\), \(j>0\), vanishes. Hence the Hitchin base is zero and the global nilpotent cone is the full classical cotangent stack, after reduction.

We prove the needed lower bound without assuming a quotient presentation or classifying all bundles on a rational curve.

**Smooth groupoid lemma.** Let \(Y\) be a smooth algebraic stack locally of finite type over an algebraically closed characteristic-zero field, with finite-type diagonal and affine stabilizers. In a smooth finite-type presentation \(A\to Y\), every irreducible component of the image of \(T^*Y\times_Y A\) in \(T^*A\) has dimension at least \(\dim A\). The affine stabilizers of bundle stacks have the matrix smoothness proof in N7.

**Proof.** Put \(R=A\times_Y A\), with its smooth source and target maps; if it is an algebraic space use étale scheme charts for the following local constructions. For \(x\in A(k)\), its groupoid orbit \(O_x\subset A\) is smooth and locally closed. Here are the details of this assertion. Its image from the finite-type source fibre \(R_x\) is constructible, so contains a dense open in its reduced closure. At an arrow of \(R\), the kernels of the source and target differentials have the same dimension. Choose a common complementary tangent subspace and cut out a smooth local slice through the arrow with that tangent space. Both maps from this slice to \(A\) are étale after shrinking. Such local correspondences preserve the condition of belonging to \(O_x\); because étale maps are open they also preserve its reduced closure. They transport the dense open just found to a neighbourhood of every orbit point. Thus \(O_x\) is open in its closure and is locally closed. Generic smoothness in characteristic zero, followed by the same correspondences, transports a smooth open to every point of the orbit, proving smoothness. Finally the differential of \(R_x\to O_x\) is surjective: its rank is constant, since its fibres are translates of the same smooth stabilizer, and generic smoothness gives the rank equal to \(\dim O_x\).

At \(x\), the image of \(T_{A/Y,x}\to T_{A,x}\) is exactly \(T_{O_x,x}\). The equation (N0.1) therefore says that its cotangent fibre consists of the annihilator of this orbit tangent space. Consequently the entire conormal bundle \(T^*_{O_x}A\) belongs to the cotangent pullback. Each of its components has dimension \(\dim A\).

To deduce a bound for **each** component of the whole closed cone, select a closed point on that component outside the other components. The conormal bundle through this point has an irreducible component of dimension \(\dim A\). Its closure in \(T^*A\) lies in one component of the cone; the selected point forces that component to be the one selected. Its dimension is at least \(\dim A\). This avoids the invalid inference from a maximum of local component dimensions at an intersection. The existence of the selected closed point follows from the Jacobson property of a finite-type scheme over the algebraically closed field. \(\square\)

Apply the lemma to \(M\). Isotropy bounds every component by \(n\), so every component has dimension \(n\). The central torus and negative stack dimension cause no exception. No finiteness of the number of orbits, no principal-bundle classification on \(\mathbf P^1\), and no assertion of a quotient chart was used.

### 6.7. Vector bundles on a genus-one curve (N3)

Choose a nonzero differential and identify \(\omega_X\) with \(\mathcal O_X\). All bundles and morphisms in this section are algebraic. The slope of a nonzero bundle \(V\) is \(\mu(V)=\deg V/\operatorname{rk}V\); it is semistable if every subbundle has slope at most \(\mu(V)\).

### N3.1. Slope facts and existence of the vector filtration

If \(V,W\) are semistable and \(\mu(V)>\mu(W)\), every morphism \(V\to W\) is zero. For a nonzero image \(I\), its quotient description in \(V\) gives \(\mu(I)\ge\mu(V)\), while its saturation in \(W\) gives \(\mu(I)\le\mu(W)\), a contradiction. The same argument proves that a dual of a semistable bundle is semistable, and that an extension of semistable bundles of one slope is semistable: intersect any subbundle with the first term and take its image in the quotient, and add the degree inequalities.

The vector Harder–Narasimhan filtration follows directly from the maximum-slope construction. Embed \(V\) in \(\mathcal O_X(N)^b\) using global generation of a sufficiently large twist of \(V^\vee\). A rank-\(i\) subbundle has degree at most \(i\deg\mathcal O_X(N)\), by its determinant injection into the corresponding exterior power. The possible ranks are finite, and the degrees are integers bounded above, so a maximum slope is attained. Choose a subbundle of maximum slope and, among those, maximum rank. It is saturated, since saturation would increase its slope. It is semistable. Every nonzero subbundle of the quotient has smaller slope; otherwise its inverse image would contradict maximum slope or maximum rank. Induction constructs a filtration with semistable quotients of strictly decreasing slope.

Uniqueness uses the vanishing just proved. A maximum-slope subbundle maps to zero in the quotient by another such maximal-rank subbundle, whose maximum slope is strictly smaller. Thus the two first terms coincide. Repeat in the quotient. In particular, every automorphism of \(V\) preserves its filtration, and dualizing reverses the slopes and the filtration.

For a finite-type family, the same embedding can be chosen uniformly on a finite affine cover of the parameter scheme, by relative Serre generation. Semistability is open, with an parameter-space proof: for each rank \(i\), only finitely many integers

\[
i\mu(V)<e\le i\deg\mathcal O_X(N)
\]

can occur as the degree of a destabilizing subsheaf. The projective Quot scheme of quotients of rank \(\operatorname{rk}V-i\) and degree \(\deg V-e\) has closed image on the parameter scheme. A kernel of one of these quotients is torsion-free, and its saturation still destabilizes. Conversely every destabilizing subbundle supplies such a quotient. Therefore the finite union of these closed images is exactly the nonsemistable locus. This proves openness over schemes, including their nonreduced structure; no representability of a principal semistability locus has been assumed.

### N3.2. Degree-zero semistable bundles have line filtrations

**Lemma.** Every degree-zero semistable vector bundle \(V\) on \(X\) has a filtration by degree-zero line bundles.

**Proof.** Fix \(y\in X(k)\). The bundle \(V(y)\) is semistable of slope one. Duality and slope vanishing give \(H^1(V(y))=\operatorname{Hom}(V(y),\mathcal O_X)^\vee=0\). Riemann–Roch gives \(h^0(V(y))=r=\operatorname{rk}V\).

Take the evaluation map \(H^0(V(y))\otimes\mathcal O_X\to V(y)\). If it has generic rank less than \(r\), it has a nonzero kernel at some point \(x\). If it has generic rank \(r\), its determinant is a nonzero section of the line \(\det V(y)\), of degree \(r>0\), and so vanishes at some point \(x\). Again the evaluation at \(x\) has a nonzero kernel. In either case there is a nonzero section of \(V(y-x)\).

Its image from \(\mathcal O_X\) has a saturated line bundle of nonnegative degree. Semistability of the degree-zero bundle \(V(y-x)\) bounds that degree by zero. Thus the image was already saturated and has degree zero. Untwisting gives a degree-zero line subbundle in \(V\). The quotient has degree zero and is semistable: a positive-degree subbundle of the quotient would have a positive-degree inverse image in \(V\). Induction proves the lemma. \(\square\)

Tensor products of two such bundles consequently have filtrations by degree-zero lines: tensor the first filtration with the second and refine it by the second filtration. The extension slope argument proves semistability of their tensor product.

### N3.3. A finite étale cover clearing any denominator

We need tensor semistability also for rational, possibly nonzero, slopes. The following construction supplies the cover without importing a degree formula for multiplication on an elliptic curve.

With an origin \(o\), the map \(x\mapsto\mathcal O_X(x)\) identifies \(X\) with \(\operatorname{Pic}^1_X\) on **all ordinary test schemes**. Indeed every degree-one line has exactly one section and zero first cohomology. Its pushforward in a family is a line bundle, compatible with arbitrary base change. Evaluation defines a relative effective Cartier divisor finite flat of degree one. Such a divisor is the graph of a unique section: its rank-one finite flat algebra is the base algebra, since its unit is an isomorphism on every fibre and hence an isomorphism. The normalized line recovered from that divisor is the original one. This is also the genus-one specialization of the evaluation argument in [*The Picard functor and the Picard scheme of a curve*](../../AG-HP/src/the-picard-functor-and-the-picard-scheme-of-a-curve.md), Proposition 5.1. Tensoring by \(\mathcal O_X(-o)\) identifies \(X\) with the proper group scheme \(J=\operatorname{Pic}^0_X\).

For any prime \(\ell\), multiplication \([\ell]:J\to J\) is étale, since its differential is multiplication by the nonzero scalar \(\ell\), at the identity and therefore at every point by translation. It is nonconstant, proper and finite. It cannot have degree one. To see this without an isogeny-degree theorem, the line \(\mathcal O_X(3o)\) is very ample: Riemann–Roch and duality separate every subscheme of length two. It embeds \(X\) as a smooth plane cubic. Every automorphism fixing \(o\) acts projectively on this embedding and belongs to the closed subgroup of \(\operatorname{PGL}_3\) preserving the cubic and \(o\). Its tangent space injects into \(H^0(X,T_X(-o))=H^0(X,\mathcal O_X(-o))=0\). This algebraic group has dimension zero, hence finitely many geometric points. Thus every origin-preserving automorphism has finite order. Were \([\ell]\) an automorphism, some power would be the identity, whereas its differential would be \(\ell^a\), impossible in characteristic zero.

The nontrivial finite étale kernel of \([\ell]\) therefore contains a point of exact order \(\ell\), yielding a nontrivial line bundle \(L\in\operatorname{Pic}^0_X\) of exact order \(\ell\). A choice \(L^{\ell}\simeq\mathcal O_X\) defines

\[
Y=\operatorname{Spec}_X\left(\bigoplus_{j=0}^{\ell-1}L^j\right)\longrightarrow X. \tag{N3.1}
\]

Locally its equation is \(u^\ell=a\), with \(a\) invertible; its derivative is invertible, so it is finite étale of degree \(\ell\). It is connected because every nontrivial degree-zero \(L^j\) has no section, giving \(H^0(Y,\mathcal O_Y)=k\). It is a smooth proper connected genus-one curve: \(\omega_Y=p^*\omega_X\simeq\mathcal O_Y\), and duality gives genus one. It is a cyclic Galois cover, with deck transformations multiplying the local root by an \(\ell\)-th root of unity.

Repeating (N3.1) on successive genus-one curves produces a finite étale tower whose total degree is divisible by any prescribed integer. Pullback across each cyclic cover preserves semistability. If the pullback were unstable, its unique first Harder–Narasimhan subbundle would be deck-invariant; its inherited descent datum satisfies the cocycle because the subbundle is uniquely determined as a subbundle. Here is the descent as an subbundle. On an affine open \(\operatorname{Spec}A\subset X\), write its cyclic cover as \(\operatorname{Spec}B\), with deck group \(\Gamma\) of order \(\ell\). For the invariant subbundle \(W\subset B\otimes_AV\), put \(N=W^\Gamma\). Averaging by \(\ell^{-1}\sum_{\gamma\in\Gamma}\gamma\) is an \(A\)-linear idempotent. Thus \(N\) is finite projective over \(A\): \(W\) is finite projective over the finite projective \(A\)-algebra \(B\), and averaging makes \(N\) a direct summand. The quotient \((B\otimes_AV)/W\) is also finite projective, and exactness of averaging gives a finite projective quotient of \(V\) by \(N\). The map \(B\otimes_AN\to W\) is an isomorphism. This can be checked after the faithfully flat change \(A\to B\): the explicit cyclic-root identity \(B\otimes_AB\simeq\prod_{\gamma\in\Gamma}B\) splits the cover, its deck action permutes the factors, and invariants are the diagonal copy with the prescribed deck identifications. Faithful flatness detects the kernel and cokernel of the map. These invariant subbundles glue on overlaps and recover \(W\) after pullback. Finally the degree of a pulled-back line is \(\ell\) times its degree, since the pullback of a divisor has \(\ell\) points counted with multiplicity above each point. Apply this to determinants. The descended destabilizing subbundle therefore has slope equal to the upstairs slope divided by \(\ell\), contradicting semistability below. Conversely a destabilizing subbundle below pulls back to a destabilizing one, so semistability of the pullback also implies semistability below.

Choose such a tower of degree \(D\) clearing the denominators of the slopes of semistable \(V,W\). On its top curve, twist \(p^*V\) and \(p^*W\) by lines of respective degrees \(-D\mu(V)\) and \(-D\mu(W)\), which exist by using multiples of one point. The results are degree-zero semistable bundles. By N3.2 their tensor product is semistable of degree zero. Undo the twists and descend to prove:

**Tensor lemma.** On a genus-one curve in algebraic characteristic zero, the tensor product of semistable bundles is semistable, of the sum of their slopes.

Finally, the tensor filtration of any two Harder–Narasimhan filtrations has graded pieces which are these tensor products. Order the sums of slopes and group equal sums. The extension slope argument shows that this convolution is itself the Harder–Narasimhan filtration. A map from a bundle all of whose slopes are at least \(a\) to a bundle all of whose slopes are below \(a\) is zero, by successive use of the slope vanishing in N3.1.

### 6.8. The adjoint filtration gives the elliptic parabolic reduction (N4)

Let \(E=\operatorname{ad}P\), and use a nondegenerate invariant form, the Killing form on the derived algebra and any nondegenerate form on the centre. Write \(F^{\ge a}E\) for the part of its Harder–Narasimhan filtration of slopes at least \(a\), with \(F^{>a}\) defined similarly. The central summand is constant and has slope zero.

The tensor lemma and the uniqueness of the tensor filtration imply

\[
[F^{\ge a}E,F^{\ge b}E]\subset F^{\ge a+b}E. \tag{N4.1}
\]

Indeed the source of the bracket has all slopes at least \(a+b\), and the quotient by the proposed target has all slopes below \(a+b\). Its induced morphism to that quotient is zero. Self-duality of the filtration gives

\[
(F^{>0}E)^\perp=F^{\ge0}E. \tag{N4.2}
\]

Put \(\mathcal U=F^{>0}E\) and \(\mathcal Q=F^{\ge0}E\). Fibrewise, \(\mathcal U_x\) is a Lie algebra of nilpotent elements: its elements strictly raise the finite filtration of \(E_x\) under the adjoint action, by (N4.1). It has zero intersection with the reductive centre. The representation-preservation of Jordan decomposition, actually proved in [*Complete reducibility: Casimir elements and Weyl's theorem*](../../RT-LIE/src/RT-LIE-04.md), therefore makes it nilpotent in a faithful representation of the derived group as well.

Here is the algebraic integration used at this point. Engel triangularization puts its nilpotent representation in strictly upper triangular matrices. The finite polynomial exponential and logarithm identify its Lie algebra with a closed connected unipotent matrix group; closure and the group law follow from the finite Baker–Campbell–Hausdorff formula. That group belongs to \(G\). For a nilpotent \(v\in\mathfrak g\), the left invariant derivation defined by \(v\) preserves the defining ideal of \(G\) in a faithful matrix embedding, and its finite exponential on matrix coordinates proves \(\exp(tv)\in G\). Apply this to every \(v\in\mathcal U_x\). This is a polynomial calculation, not an analytic exponential.

A connected unipotent group is contained in a maximal connected solvable subgroup \(B\), by increasing dimension among connected solvable subgroups. Its projection to the torus quotient of \(B\) is trivial. Thus \(\mathcal U_x\) lies in the nilradical \(\mathfrak n_B\). By (N4.2), \(\mathcal Q_x\) contains \(\mathfrak n_B^\perp=\mathfrak b\).

Here is a group-level proof that this Lie subalgebra \(\mathfrak q=\mathcal Q_x\) is parabolic, avoiding a tacit integration assertion for an arbitrary subalgebra. Let \(H\) be its closed Grassmannian stabilizer in \(G\). Its Lie algebra is the Lie normalizer of \(\mathfrak q\). The latter equals \(\mathfrak q\): its quotient by \(\mathfrak q\) is annihilated by \(\mathfrak q\), whereas a Cartan algebra in \(\mathfrak b\) has no zero weights in \(\mathfrak g/\mathfrak q\), since \(\mathfrak q\) contains the whole Cartan algebra and is stable under it. The formal matrix argument in N7 makes \(H\), and \(H\cap B\), smooth. Their Lie-algebra intersection is \(\mathfrak b\), so \(H\cap B\) has the full dimension of the connected \(B\), and equals \(B\). Hence \(Q=H^0\) contains \(B\). [*Automorphisms, forms and parabolic subgroups*](../../AG-RG/AG-RG-06.html), Theorem 1.1, classifies such connected subgroups as standard parabolic groups. We have \(\operatorname{Lie}Q=\mathfrak q\). Its nilradical is \(\mathfrak q^\perp\), which is exactly \(\mathcal U_x\).

Let \(H\) be the full Grassmannian stabilizer of \(\mathfrak q\). The preceding argument gives \(H^0=Q\). Every element of \(H\) normalizes its identity component \(Q\). [*Automorphisms, forms and parabolic subgroups*](../../AG-RG/AG-RG-06.html), Theorem 1.1, proves the scheme-theoretic equality \(N_G(Q)=Q\); hence \(H=Q\). Thus the orbit map \(G/Q\to\operatorname{Gr}(\mathfrak g)\) is a monomorphism, with injective differential. It is proper because \(G/Q\) is projective, so is a closed immersion. The parameter scheme of parabolic Lie algebras is the finite disjoint union of these closed conjugacy orbits. Since \(X\) is connected, the type is constant. The map from the reduced curve to the Grassmannian factors scheme-theoretically through that orbit, because its defining equations vanish at all geometric points. It defines a \(Q\)-reduction of \(P\), on the entire curve. This is a construction from the existing vector filtration, not an assumed principal reduction theorem.

We need the other terms of the filtration as well. At one fibre choose a maximal torus \(T\subset Q\). By (N4.1), every \(F^{\ge a}E_x\) is stable under \(\mathfrak q\), hence under the connected group \(Q\); in characteristic zero Lie stability implies group stability by differentiating the Grassmannian stabilizer. Torus stability decomposes each term into root lines and, at weight zero, the Cartan algebra. The entire Cartan has filtration weight zero. It is contained in \(F^{\ge0}E_x=\mathfrak q\), while its intersection with \(F^{>0}E_x\) is zero: the latter consists of nilpotent elements, and every Cartan element is semisimple. Assign to each root \(\alpha\) its filtration weight \(s_\alpha\). Pairing with its opposite root gives \(s_{-\alpha}=-s_\alpha\). If \(\alpha,\beta,\alpha+\beta\) are roots, their nonzero bracket gives

\[
s_{\alpha+\beta}\ge s_\alpha+s_\beta.
\]

Bracketing \(\alpha+\beta\) with \(-\beta\) gives the reverse inequality. Therefore equality holds. Root-height induction now makes the weights an additive function on the root lattice. They define a rational cocharacter \(\mu\) in the derived torus, uniquely after imposing zero central part. It is dominant for \(B\subset Q\), is zero on the Levi roots, and is positive on the nilradical roots. Clearing denominators makes \(Q=P_G(N\mu)\), and gives exactly the filtration by the \(\mu\)-weights.

There are only finitely many \(Q\)-stable root-line filtrations with a given finite list of weights. Consequently the weights and their assignment are locally constant along the connected curve in a \(Q\)-trivialization, and the global filtration is the one associated to this fixed \(Q\)-module filtration. Its zero graded piece is \(\operatorname{ad}F_L\) for the induced Levi bundle \(F_L\), and is semistable of degree zero. Its positive graded pieces \(V_s(F_L)\), \(s>0\), are semistable of slope \(s\). Its negative graded pieces are semistable of negative slope. In particular

\[
H^0(X,\mathfrak g_P/\mathfrak q_{F_Q})=0,
\qquad H^1(X,V_s(F_L))=0\quad(s>0). \tag{N4.3}
\]

The first assertion follows from negative slopes; the second follows by duality, \(\omega_X=\mathcal O_X\), and positive slopes. Hence every Higgs field of \(P\) lies in \(H^0(X,\mathfrak q_{F_Q})\).

Conversely, fix a dominant rational \(\mu\), \(Q=P_G(N\mu)\) and its Levi \(L\). Let \(\mathcal D_\mu\subset\operatorname{Bun}_L\) be the open and closed degree conditions together with the open conditions that every \(\mu\)-graded representation \(V_s\) in \(\mathfrak g\) is semistable of slope \(s\). The zero one is \(\mathfrak l\) and has slope zero. Openness is N3.1 applied to these finitely many representations. For a \(Q\)-bundle above this open, the \(\mu\)-graded adjoint filtration has semistable quotients of the indicated strictly ordered slopes, so is its unique vector Harder–Narasimhan filtration. Thus this \(Q\)-reduction is canonical, and any isomorphism of the induced \(G\)-bundles preserves it.

On a finite-type chart of \(M\), only finitely many \(\mu\)'s occur. The uniform embedding of \(E\) bounds all its subbundle slopes above; its self-duality bounds them below as well. Ranks are at most \(\dim G\), so the possible slope fractions form a finite set. Assigning these finitely many values to the finitely many roots leaves only finitely many rational dominant cocharacters. This proves the local finiteness needed below directly; it assumes no principal boundedness theorem.

### 6.9. The elliptic nilpotent models and their dimensions (N5)

### N5.1. The unipotent directions have relative dimension zero

For a type \(\mu\) from N4, filter the unipotent radical \(U\) of \(Q\) by its strictly positive \(\mu\)-weights. The terms are normal in \(Q\), and successive quotients are the additive \(L\)-representations \(V_s\); a commutator strictly increases weight. The root-coordinate construction, or the finite exponential in characteristic zero, gives these group quotients. On \(\mathcal D_\mu\), their associated vector bundles have zero first cohomology by (N4.3).

Let \(F_L\) be a family of Levi bundles in \(\mathcal D_\mu(S)\). These vanishings and the finite locally free cohomology complex imply that \(R\pi_*\mathfrak u_{F_L}\) is a vector bundle in degree zero and commutes with arbitrary ordinary base change. The same holds for the graded quotients. Successive additive Čech lifting therefore makes every lift of \(F_L\) to a \(Q\)-bundle isomorphic, locally on \(S\), to the split lift. Its relative automorphism group is \(\mathcal H=\Gamma(X_S,U_{F_L})\). Finite exponential identifies \(\mathcal H\), as a scheme over \(S\), with the vector bundle \(\pi_*\mathfrak u_{F_L}\); its multiplication is the polynomial Baker–Campbell–Hausdorff law. It is smooth and of constant relative dimension

\[
h=\sum_{s>0}h^0(X,V_s(F_L))=
\sum_{s>0}\deg V_s(F_L). \tag{N5.1}
\]

The Čech assertion in families can be seen layer by layer: the only curve torsor obstruction is first cohomology of the additive quotient, which is zero; after arbitrary base change the quotient remains its degree-zero pushforward. Any remaining torsor under that vector bundle is a torsor on \(S\), and becomes trivial locally on \(S\). The second cohomology on the curve is zero. Thus the relative lift stack is \(B\mathcal H\).

For a fixed Levi Higgs field \(\bar\phi\), lifting it to \(\mathfrak q\) has an affine space of choices under \(\pi_*\mathfrak u_{F_L}\), since its first cohomology is zero. After the split lift, the Levi inclusion gives one such choice. The full relative stack of lifts of \((F_L,\bar\phi)\) is therefore

\[
[\mathbb A^h_S/\mathcal H], \tag{N5.2}
\]

with its polynomial conjugation action. This stack is smooth over \(S\), of relative stack dimension \(h-h=0\). The affine action need not be free; its stabilizers are retained in this calculation.

If \(\bar\phi\) is nilpotent then every lift is nilpotent, by contracting the unipotent part with \(N\mu\): every invariant of \(\phi\) equals its restriction to \(\bar\phi\). Conversely, a nilpotent parabolic element has nilpotent Levi part on geometric fibres, by its Jordan decomposition and the zero-fibre statement in N1. This converse is a statement about reduced support: the invariant ideal of \(G\) restricted to the Levi need not equal the invariant ideal of \(L\). For example, restricting the \(SL_2\) quadratic invariant to its torus gives a square instead of the torus's linear invariant. We use the model imposing nilpotence in \(L\), which has the same reduced support in the parabolic locus. We do not assert equality of the two functors on nonreduced \(S\).

### N5.2. Semistable adjoint bundles and centralizers

Let \(L\) be any connected reductive group, and consider pairs \((F,\eta)\) with \(\mathfrak l_F\) semistable of degree zero and \(\eta\) nilpotent. Every endomorphism of this vector bundle has constant rank. If \(K,I\) are its kernel and image, semistability gives \(\deg K\le0\), hence \(\deg I\ge0\). The saturation \(\bar I\) in the target has degree at most zero. Since \(\deg\bar I\ge\deg I\), all degrees are zero and the saturation torsion is zero. Thus the image is a subbundle. Apply this to \(\operatorname{ad}\eta\).

There are finitely many nilpotent \(L\)-orbits, by the local Lie-triple proof: put the semisimple element \(h\) of a triple in a dominant Cartan. All its adjoint weights are integers of absolute value at most \(\dim\mathfrak l-1\), by the explicit \(\mathfrak{sl}_2\)-module classification. Hence only finitely many simple-root values, and therefore only finitely many \(h\)'s, can occur. For a fixed \(h\), \([e,-]:\mathfrak l_0\to\mathfrak l_2\) is onto, by that same module calculation. The centralizer of \(h\) has an open orbit at \(e\) in the irreducible vector space \(\mathfrak l_2\). Two open orbits cannot be disjoint, so there is at most one. This proves finiteness without a table of nilpotent orbits.

The section \(\eta\) has a single orbit \(C\) at every point of \(X\). Its generic orbit is one of this finite list; all other fibre orbits lie in its closure. A boundary orbit has strictly smaller dimension, while constant rank of \(\operatorname{ad}\eta\) keeps the orbit dimension constant. There can be no boundary fibre.

Fix \(e\in C\), and write \(Z=C_L(e)\), possibly disconnected. A section of the orbit bundle \(F\times^L C=F/Z\) is exactly a \(Z\)-reduction. Thus the functor of pairs whose section takes values scheme-theoretically in this orbit is \(\operatorname{Bun}_Z\), with the open condition that the induced adjoint \(L\)-bundle is semistable. With further \(\mathcal D_\mu\) conditions, it is still an open substack.

The determinant of the adjoint representation of \(Z\) is trivial. In the exact sequence of \(Z\)-representations

\[
0\to\mathfrak z\to\mathfrak l\to\mathfrak l/\mathfrak z\to0,
\]

the middle determinant is trivial. The last term has the nondegenerate \(Z\)-invariant alternating form

\[
([a,e],[b,e])\longmapsto\kappa(e,[a,b]). \tag{N5.3}
\]

Invariance of \(\kappa\) identifies its kernel precisely with the centralizer before passing to the quotient. A symplectic representation has determinant one, including the disconnected components. Therefore \(\det\mathfrak z=1\). For any \(Z\)-torsor \(R\), \(\deg\mathfrak z_R=0\). Its bundle stack is smooth by the same additive Čech deformation calculation and \(H^2=0\), and has dimension

\[
-\chi(\mathfrak z_R)=0. \tag{N5.4}
\]

Algebraicity here introduces no new kind of moduli theorem: over \(\operatorname{Bun}_L\), these reductions are the functor of sections in the orbit subbundle of \(\mathfrak l_F\), a locally closed subfunctor of the finite-type section space. Vanishing of the orbit-closure equations is a closed condition on sections; avoiding its boundary on the entire proper curve is open. The usual Čech lifting uses smoothness of \(Z\), established algebraically in characteristic zero as recalled in N7 below. Only the determinant, rather than the whole adjoint bundle, has been shown trivial.

Consequently every fixed-orbit piece of the Levi nilpotent stack with the \(\mathcal D_\mu\) conditions is smooth of pure dimension zero. This is an assertion about the all-scheme orbit-factorization functor. Finitely many such pieces cover the geometric points of the reduced Levi nilpotent locus; infinitesimal points need not belong to a single piece.

### 6.10. Every elliptic component, with finite-type families (N6)

For each \(\mu\) and nilpotent Levi orbit \(C\), let \(\mathcal R_{\mu,C}\) be the following stack: its objects are a \(Q\)-bundle with Levi bundle in \(\mathcal D_\mu\), a Levi Higgs section taking values in the orbit bundle \(C\), and a lift of that section to the parabolic algebra. By N5.1–N5.2 it is smooth of pure stack dimension zero. Forgetting the reduction gives a map

\[
\mathcal R_{\mu,C}\longrightarrow\mathcal N_G. \tag{N6.1}
\]

It is representable: after fixing the underlying \(G\)-bundle and its Higgs field, its fibre is the scheme of parabolic reductions with the indicated conditions. It has at most one geometric point in each fibre. Indeed its induced adjoint filtration is the unique vector Harder–Narasimhan filtration, by the converse in N4, so its parabolic reduction is fixed. An isomorphism of induced bundles respecting the Higgs field respects this reduction. The possible infinitesimal movement of a reduction is \(H^0(X,(\mathfrak g/\mathfrak q)_{F_Q})=0\). Thus the fibres are zero-dimensional; no stabilizers have been discarded in constructing the source stack.

Every geometric point of \(\mathcal N_G\) belongs to one of these images. Construct its parabolic reduction by N4; its Higgs field lies in the parabolic algebra by (N4.3); its Levi part is nilpotent. The semistable zero graded piece makes that Levi part have constant orbit, by N5.2. This is exactly an object of one of the sources. This includes the type \(\mu=0\), \(Q=G\), and the zero orbit. The reductive central Higgs part is zero by its invariant linear equations.

We now verify the finite-type issue, which is needed to turn these sources into a component-dimension proof. Over a finite-type chart \(A\) of \(M\), the types \(\mu\) are finite by the last paragraph of N4, and each Levi has finitely many nilpotent orbits. The parameter space of the relevant reductions is finite type over \(A\). One explicit verification uses the projective flag bundle

\[
\mathscr F=P_A\times^G(G/Q)\longrightarrow X\times A.
\]

Embed it by the parabolic-algebra Grassmannian and its Plücker line. Twisting that relative ample line by a sufficiently high fixed power of an ample line on \(X\), on a finite cover of \(A\), makes it ample for the projective morphism \(\mathscr F\to A\). The degree of its restriction to the graph of a reduction is fixed by \(\mu\): the Plücker line has restriction \(\det\mathfrak q_{F_Q}^{\vee}\), of degree

\[
-\deg\mathfrak q_{F_Q}=-\sum_{s>0}s\operatorname{rk}V_s,
\]

and the chosen twist contributes a fixed integer. The graph is a genus-one curve, so this fixes its Hilbert polynomial. The corresponding [*Hilbert and Quot schemes*](../../AG-HP/src/hilbert-and-quot-schemes.md) Hilbert scheme is projective and finite type over \(A\). The locus where projection of the universal subscheme to \(X\times A\) is an isomorphism is open and represents sections: properness first removes the locus of positive-dimensional fibres; on the finite locus, the kernel and cokernel of the map of finite algebras vanish near any base point whose fibre map is an isomorphism, by flatness and Nakayama. Thus its graph locus is of finite type.

The \(\mathcal D_\mu\) conditions are open degree conditions and semistability conditions on the associated Levi bundles. Conditions on the Higgs field are finite-type section equations; on any finite chart, a finite locally free cohomology complex realizes the section functor as the kernel of a map between finite vector bundles. Factoring the Levi section through the orbit is locally closed: impose finitely many equations of its orbit closure and avoid the boundary on the whole proper curve. These descriptions show that

\[
Y_{\mu,C}:=\mathcal R_{\mu,C}\times_M A
\]

is a finite-type algebraic space, in fact a scheme in the section/graph description. It is smooth of pure dimension \(m\), because \(A\to M\) is smooth of relative dimension \(m\) and \(\mathcal R_{\mu,C}\) is smooth of stack dimension zero. In genus one (N0.3) gives \(m=n\).

The induced morphism \(Y_{\mu,C}\to N_A\) has zero-dimensional geometric fibres. Every irreducible component of its source therefore has image closure of dimension \(m\). This follows from the finite-type dimension formula: the extension of function fields at the generic image is algebraic when the generic fibre is zero-dimensional, and both dimensions are the corresponding transcendence degrees. Étale scheme charts give the same argument for algebraic spaces.

There are only finitely many such source components: the types and orbits are finite, and each \(Y_{\mu,C}\) is finite type. Their image closures lie in \(N_A\), have dimension \(m\), and cover every geometric closed point of \(N_A\), by the construction above. Their finite union is closed. Since a finite-type scheme over an algebraically closed field is Jacobson, that union is all of \(N_A\). The irreducible components of a finite closed union are its maximal irreducible members. All these members have dimension \(m=n\). Therefore **every** component of \(N_A\) has dimension \(n\).

This proves the elliptic dimension equality without using an external principal Harder–Narasimhan theorem or a countable union. It also avoids assuming that a fibrewise canonical reduction exists over an arbitrary nonreduced base: we use reduction stacks, all-base orbit-factorization functors, and their finite-type maps, which cover geometric points. Nilpotent thickenings of their images do not affect the reduced component dimensions.

### 6.11. Smooth stabilizers and the characteristic-zero calculation (N7)

For completeness, the smooth affine stabilizers used above can be established by a direct formal matrix argument. Let \(H\subset\operatorname{GL}(V)\) be a finite-type closed group over characteristic-zero \(k\), let \(R\) be an Artinian local \(k\)-algebra with residue field \(k\), and let \(I\) be its maximal ideal. For \(g\in H(R)\) reducing to \(1\), set

\[
g(t)=\sum_{j\ge0}\binom{t}{j}(g-1)^j.
\]

This is a finite polynomial because \(I\) is nilpotent. At every nonnegative integer \(t\), it is \(g^t\in H(R)\). Applying the defining equations of \(H\) gives polynomials over \(R\) which vanish at all these integers. Vandermonde matrices on finitely many distinct integers are invertible over the characteristic-zero field, so the polynomials vanish identically. Differentiating at zero gives \(\log g\in\operatorname{Lie}H\otimes I\).

Conversely, for \(v\in\operatorname{Lie}H\otimes I\), its left invariant derivation preserves the Hopf ideal of \(H\). Its finite exponential, evaluated at the identity, gives \(\exp v\in H(R)\). The finite matrix logarithm and exponential are inverse. Thus the identity formal group of \(H\), as a functor on these Artinian rings, is the formal affine space \(\operatorname{Lie}H\). Its completed local ring is a power series ring. Finite presentation and the infinitesimal smoothness criterion give smoothness at the identity; translation gives smoothness everywhere. This proves the affine characteristic-zero case of the smooth-group theorem needed here, including disconnected \(H\).

All the relevant stabilizers have such matrix embeddings. A faithful representation of \(G\) makes \(Z=C_G(e)\) a closed matrix subgroup. For \(\operatorname{Aut}_G(P)\), twist its associated faithful vector bundle until it is globally generated with zero first cohomology. The automorphism acts faithfully on its finite-dimensional section space, because the evaluation is onto. Preserving the bundle and the \(G\)-reduction gives closed equations in the general linear group of that space. Equivalently, over each Artinian ring, logarithms of bundle automorphisms glue as sections of \(\operatorname{ad}P\), and exponentials of those sections give the inverse. These are the same smooth formal coordinates. The stabilizers in the genus-zero groupoid proof and the centralizers in N5 are therefore smooth. The finite-type diagonal and matrix realization remain within the lesson's bundle algebraicity foundation.

Here is the matching algebraic Cartan step for the Lie algebra of the assigned reductive group. Let \(s\in\mathfrak g\) be semisimple, and diagonalize its action in a faithful representation of \(G\); Jordan preservation makes this action semisimple. For the reductive centre use its torus weight decomposition. Write its eigenvalues as \(\lambda_1,\ldots,\lambda_b\), and put

\[
L=\{(a_i)\in\mathbb Z^b:\textstyle\sum_i a_i\lambda_i=0\}.
\]

This sublattice is saturated, since characteristic is zero. The diagonal subtorus \(D\subset\operatorname{GL}_b\) defined by the characters in \(L\) has \(s\) in its Lie algebra. In fact \(D\subset G\). Every equation \(f\) of \(G\), restricted to the diagonal torus, is a Laurent polynomial. Evaluate it on \(\exp(us)\) in \(k[[u]]\). The formal matrix argument above gives \(\exp(us)\in G(k[[u]])\), so this evaluation is zero. Group its finitely many monomials by the values \(\sum a_i\lambda_i\). Distinct resulting formal exponentials are linearly independent: their first finitely many derivatives at zero form an invertible Vandermonde matrix. Thus the coefficient sum in every group is zero. Two monomials restrict to the same character on \(D\) exactly when their difference lies in \(L\). These coefficient sums say precisely that \(f|_D=0\), proving \(D\subset G\).

Contain \(D\) in a maximal torus and use [*Tori, maximal tori and their conjugacy*](../../AG-RG/AG-RG-01.html) torus conjugacy to put \(s\) in the Lie algebra of a chosen maximal torus of \(G\). Its Lie centralizer equals the torus centralizer's Lie algebra: in the faithful matrix adjoint representation, a diagonal character has derivative zero on \(s\) exactly when it is trivial on \(D\), by the definition of \(L\). [*Regular elements and centralizers*](../../AG-RG/AG-RG-02.html), Lemma 1.1, makes \(C_G(D)\) smooth and connected. Its root spaces consist of the pairs of opposite roots trivial on \(D\). It is reductive: the Lie algebra of a normal unipotent radical is a torus-stable ideal of nilpotent matrices; a nonzero root vector in it would yield a nonzero toral coroot by bracketing with its opposite root vector, a contradiction, and a nonzero zero-weight vector is already toral. Thus that ideal is zero, and the smooth unipotent radical is trivial. The usual root decomposition therefore gives a toral centre and a semisimple derived centralizer, with strictly smaller derived dimension when \(s\) is nonzero in a semisimple algebra.

This proves exactly the semisimple-centralizer input for the existing Lie-triple induction applied to the Lie algebra of any reductive algebraic \(G\) over the present \(k\). It also supplies actual-group conjugacy into a torus for the invariant-polynomial argument. For \(h\) in a Lie triple, the faithful representation has integral \(h\)-weights by the rank-one module calculation; its torus hull therefore has an integral cocharacter with differential \(h\). Alternatively clear denominators in its root values. The canonical cocharacter parabolic thus belongs to the given algebraic group, including a non-simply-connected one. The all-field group root arguments and the rational rank-one modules, rather than a complex-only Cartan statement, provide the exact matching foundations used here.

Every use of a field order, real chamber or integral weight in this argument concerns the rational root datum and its real reflection model, not an order on \(k\). The elliptic cyclic covers use characteristic zero for the derivative of \([\ell]\) and for the automorphism-order contradiction. The formal exponentials, Jacobson–Morozov and Lie-to-group passage use characteristic zero as well. No positive-characteristic assertion follows from the argument.

### 6.12. Conclusion and exact proof boundary (N8)

The argument gives three lower bounds, paired with the already written isotropy:

| Genus | Lower bound or direct dimension mechanism | Reductive centre |
|---|---|---|
| \(g\ge2\) | At most \((m-z)+(d+z)=n\) equations in \(T^*A\) | Constant central kernel cancels the extra Hitchin dimension |
| \(g=0\) | Every cotangent point lies on a conormal bundle of dimension \(n\); choose a point outside other components | Included in the full orbit/stabilizer calculation |
| \(g=1\) | Finite-type zero-fibre maps from smooth pure-\(n\) reduction models; finitely many image closures cover \(N_A\) | Central Higgs component zero; Levi and centralizer determinants give degree zero |

This proves the geometric dimension statement for all smooth charts and includes arbitrary ordinary test-scheme families in the constructions. It does **not** say that the nilpotent cone is flat over \(\operatorname{Bun}_G\), that its fibres there have constant dimension, or that a family with a constant set of fibrewise orbit/HN labels necessarily factors through the corresponding schematic stratum. All such stronger statements would be different assertions.

The main theorem retains exactly the lesson's algebraically closed characteristic-zero boundary. If one defines the theorem over a general characteristic-zero field as a geometric Lagrangian assertion, the same proof after algebraic closure gives that geometric assertion, provided the bundle/cotangent/invariant constructions commute with that base change. No arithmetic statement about rational torsor triviality, splitness or rational nilpotent-orbit representatives is claimed.

Sections 1.1–1.6 prove the bundle-stack representability and formal-effectivity results through explicit Quot and reduction atlases, finite cohomology coordinates and affine Isom schemes. The complete recursive closure of the other specified programme foundations remains open. The cohomology/base-change, duality, Quot and group arguments listed above supply the particular claims used here; N0 supplies the vector-family extension and smooth-curve adjunction identification, and N7 supplies the algebraic semisimple torus step. The local algebra, quotient/descent and representability foundations cited by those earlier courses are not proved here. Within those recorded foundations, **no genus-one principal Harder–Narasimhan/tensor-semistability gap and no genus-zero quotient-chart gap remains in this dimension argument**. The dimension argument uses the nilpotent Lie triple and isotropy of §§6.1–6.3. The dimension argument does not use uniformization. Sections 7.1–7.7 prove formal-disc gluing, affine torsor descent and formal local triviality, with the stated curve and earlier scheme-topological foundations; one-point family uniformization is proved in §7.8 using the exact earlier programme theorem, and §7.9 derives its full stack quotient.

Further reading: [Ginzburg, *The global nilpotent variety is Lagrangian*, alg-geom/9704005v6](https://arxiv.org/pdf/alg-geom/9704005v6), chiefly the chartwise definition and the higher-genus equation count; [Beilinson–Drinfeld, author draft, §2.10.4](https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf), for the division by genus and the elliptic centralizer idea; [Heinloth, *Uniformization of G-bundles*, 0711.4450v2, Proposition 1](https://arxiv.org/pdf/0711.4450v2), for the exact smooth-affine finite-type group hypotheses of the existing algebraicity foundation. The elliptic tensor argument, construction from the adjoint vector filtration and finite-family image argument above are proved above; the BD source's unproved principal stability package is not imported. Its final inference that trivial determinant makes the entire centralizer adjoint bundle trivial is not used: trivial determinant alone gives the needed degree zero.

The component calculations count chart dimensions rather than coarse-space dimensions, retain automorphisms in (N5.2), use finite-type image closures in N6, and distinguish reduced support from nilpotent test-family equations. The proof establishes tensor semistability in arbitrary algebraic characteristic zero and retains the stated recursive foundation obligations.

## 7. One point of uniformization: what it covers

Fix \(x\in X(k)\), put \(U=X\setminus\{x\}\), and write \(\operatorname{Gr}_{G,x}=G(k((t)))/G(k[[t]])\). It classifies bundles on \(X\) equipped with a trivialization on \(U\). Sections 7.1–7.7 prove this description on the coefficient fppf site for smooth affine groups, including the gluing, affineness and formal local-triviality steps over arbitrary ordinary parameter algebras. Changing the trivialization is an action of the group functor \(G(U)\).

Consequently the quotient \(G(U)\backslash\operatorname{Gr}_{G,x}\) maps to \(\operatorname{Bun}_G\), and identifies the substack of bundles that are trivial on \(U\) locally over their parameter schemes. It is an equivalence onto all of \(\operatorname{Bun}_G\) once every bundle admits such a trivialization locally in the relevant topology.

For semisimple simply connected \(G\), that last assertion is the uniformization theorem: families become trivial on \(U\) after an étale cover of the parameter scheme. Section 7.8 applies the full earlier [*Beauville–Laszlo gluing and the moduli interpretation*](../../GL-SAT/src/GL-SAT-03.md), Theorem 5.3 and §§6–7, and includes all connected semisimple groups in characteristic zero. Section 7.9 proves the quotient equivalence as an étale stack quotient. The gluing proof constructs bundles from specified local pieces; the family theorem supplies the trivialization on \(U\).

For \(G=\mathbb G_m\), a lattice at one point produces only line bundles \(\mathcal O(dx)\). On a positive-genus curve many degree-zero line bundles are absent. In detail, the localization sequence for divisors gives

\[
\operatorname{Pic}(U)\simeq
\operatorname{Pic}(X)/\mathbb Z[\mathcal O(x)].
\]

To verify it, extend a divisor on \(U\) to \(X\) to get surjectivity. A line bundle restricting trivially has a rational trivializing section whose divisor is supported at \(x\), so it is \(\mathcal O(dx)\). A nontrivial line bundle \(L\in\operatorname{Pic}^0(X)\) cannot be \(\mathcal O(dx)\), since degree would force \(d=0\). Hence \(L|_U\) is nontrivial. The bundle \(L\oplus\mathcal O^{n-1}\) similarly obstructs an unconditional \(GL_n\) assertion through its determinant. On \(\mathbb P^1\), in contrast, \(U\simeq\mathbb A^1\) and vector bundles on \(U\) are free, by the classification of finite projective modules over the principal ideal domain \(k[t]\). One-point uniformization then covers all vector bundles.

This does not conflict with the previous lesson's adelic dictionary: that construction used lattices at every closed point and allowed a rational generic frame. Triviality on one prescribed affine complement is stronger.

### 7.1. Gluing modules across a formal disc

The algebraic gluing step works over arbitrary commutative rings. In particular, the parameter algebra need not be Noetherian or reduced. We prove the statement before using it on the curve.

Let \(A\) be a commutative ring and let multiplication by \(f\in A\) be injective. Write
\[
 A_f=A[1/f],\qquad
 \widehat A=\varprojlim_{n\geq1}A/f^nA,\qquad
 \widehat A_f=\widehat A[1/f].
 \tag{BL.1}
\]
A module is **\(f\)-regular** when multiplication by \(f\) on it is injective. Completion of the ring and tensoring a module with that completed ring are different operations; the module used below is \(\widehat A\otimes_A M\).

We first establish the exact algebra that makes gluing possible. Multiplication by \(f\) on \(\widehat A\) is injective, and
\[
 A/f^nA\xrightarrow{\ \sim\ }\widehat A/f^n\widehat A
 \quad(n\geq1).
 \tag{BL.2}
\]
For injectivity, if \(fb=0\), represent the \((m+1)\)-st component of \(b\) by \(a\in A\). Then \(fa\in f^{m+1}A\), so \(a\in f^mA\), because \(f\) is a nonzero divisor. Every \(m\)-th component of \(b\) is zero. For (BL.2), projection onto the \(n\)-th component is onto: lift a residue by an element of \(A\) and take its compatible residues. If that component of \(b\) is zero, divide its \((m+n)\)-th component by \(f^n\). The resulting classes modulo \(f^m\) are uniquely determined and compatible, again by cancellation of \(f^n\). They define \(c\in\widehat A\) with \(b=f^nc\). This proves the kernel assertion. No separatedness assumption on \(A\) has been used.

If every element of an \(A\)-module \(T\) is killed by a power of \(f\), then
\[
 T\xrightarrow{\ \sim\ }\widehat A\otimes_A T.
 \tag{BL.3}
\]
Here is an explicit inverse. On an element \(t\) killed by \(f^n\), a coefficient \(b\in\widehat A\) acts through its unique class in \(A/f^nA\). Choosing a representative \(a\in A\), send \(b\otimes t\) to \(at\). Changing the representative changes this by zero, and larger exponents give the same answer. This defines the balanced inverse, since \(b-a\in f^n\widehat A\).

Consequently the two extensions of scalars jointly detect the zero module:
\[
 L_f=0\text{ and }\widehat A\otimes_A L=0
 \quad\Longrightarrow\quad L=0.
 \tag{BL.4}
\]
Indeed the first equality says that every element of \(L\) is killed by a power of \(f\), so (BL.3) applies. Since tensor is right exact, (BL.4) detects surjectivity by testing the cokernel. It also detects finite generation: if the two extended modules are finitely generated, their finitely many generators involve only finitely many elements of \(L\); the submodule generated by those elements has cokernel zero after both extensions, hence has cokernel zero over \(A\). The combined extension need not be flat.

There is an exact sequence
\[
 0\longrightarrow A\longrightarrow A_f
 \longrightarrow\widehat A_f/\widehat A\longrightarrow0.
 \tag{BL.5}
\]
The last arrow sends a fraction to its completed fraction modulo \(\widehat A\). A class \(b/f^n\) is represented by \(a/f^n\), where \(a\in A\) agrees with \(b\) modulo \(f^n\), proving surjectivity. If \(a/f^n\) maps into \(\widehat A\), then the image of \(a\) in \(\widehat A\) is divisible by \(f^n\); reduction in (BL.2) gives \(a=f^nc\) in \(A\). The fraction was already \(c\in A\). Injectivity of the first arrow follows from the nonzero-divisor hypothesis.

**The tensor exactness needed for the kernel.** Suppose
\[
 0\longrightarrow K\longrightarrow V\longrightarrow T\longrightarrow0,
 \qquad T_f=0.
 \tag{BL.6}
\]
Tensoring this sequence with \(\widehat A\) remains exact on the left as well as on the right. We give the proof, since assuming general flatness of completion would lose the stated generality.

Choose a free module \(F\) surjecting onto \(V\), and let \(L\) and \(K_0\) be the kernels of its maps to \(V\) and \(T\). Thus \(K=K_0/L\). We first show
\[
 \widehat A\otimes_A K_0\longrightarrow
 \widehat A\otimes_A F\quad\text{is injective}.
 \tag{BL.7}
\]
An element of a proposed kernel uses finitely many elements of \(K_0\), each supported on finitely many basis vectors of \(F\). Put these basis vectors in a finite free summand \(F_0\subset F\). Its image in \(T\) is killed by some common \(f^n\). Write \(K_{00}=K_0\cap F_0\); then
\[
 f^nF_0\subset K_{00}\subset F_0,
 \qquad Z=K_{00}/f^nF_0\subset F_0/f^nF_0.
 \tag{BL.8}
\]
The module \(Z\) is killed by \(f^n\), so its tensor extension is itself by (BL.3). If an element of \(\widehat A\otimes K_{00}\) maps to zero in \(\widehat A\otimes F_0\), its image in \(Z\) is zero: the displayed inclusion of \(Z\) in \(F_0/f^nF_0\) is unchanged under (BL.2). Right exactness therefore lifts the element from \(\widehat A\otimes f^nF_0\). Identifying \(f^nF_0\) with \(F_0\), its map to \(\widehat A\otimes F_0\) is multiplication by \(f^n\), which is injective by (BL.2). The lift is zero. This proves (BL.7) for every finitely supported element, hence for the entire free module.

Finally, right exactness identifies \(\widehat A\otimes K\) with the quotient of \(\widehat A\otimes K_0\) by the image of \(\widehat A\otimes L\), and \(\widehat A\otimes V\) with the corresponding quotient of \(\widehat A\otimes F\). Their inclusion follows from (BL.7). This proves the claim about (BL.6). Applying it to
\[
 0\longrightarrow M\xrightarrow{\ f\ }M
 \longrightarrow M/fM\longrightarrow0
 \tag{BL.9}
\]
shows that \(\widehat A\otimes_A M\) is \(f\)-regular whenever \(M\) is.

**The gluing theorem.** The category of \(f\)-regular \(A\)-modules is equivalent to the category of triples
\[
 (P,Q,\theta),\qquad
 P\in\operatorname{Mod}(A_f),\quad
 Q\in\operatorname{Mod}_{f\text{-reg}}(\widehat A),\quad
 \theta:\widehat A\otimes_A P\xrightarrow{\ \sim\ }Q_f.
 \tag{BL.10}
\]
Morphisms are pairs of module maps commuting with \(\theta\). The functor takes the ordinary scalar extensions of a module, with their canonical overlap identification.

To construct the inverse, use the actual kernel
\[
 \begin{aligned}
 T&=Q_f/Q,\\
 M&=\ker\bigl(P\longrightarrow Q_f/Q\bigr),\qquad
 p\longmapsto\theta(1\otimes p)\bmod Q.
 \end{aligned}
 \tag{BL.11}
\]
The quotient is defined because \(Q\) is \(f\)-regular. Every element of \(T\) is killed by a power of \(f\). The map in (BL.11) is onto: after tensoring with \(\widehat A\), (BL.3) identifies it with the surjection \(Q_f\to Q_f/Q\); after inverting \(f\) its cokernel is already zero. Apply (BL.4) to that cokernel. Hence
\[
 0\longrightarrow M\longrightarrow P\longrightarrow T\longrightarrow0.
 \tag{BL.12}
\]
The module \(M\) is \(f\)-regular as a submodule of \(P\). Localizing (BL.12) gives \(M_f=P\): localization is exact, since equality or vanishing of any finite sum of fractions can be tested after multiplication by one common power of \(f\). Tensoring (BL.12) with \(\widehat A\) is left exact by (BL.6), and gives
\[
 \begin{array}{ccccccccc}
 0&\longrightarrow&\widehat A\otimes_A M&\longrightarrow&Q_f
 &\longrightarrow&T&\longrightarrow&0,\\
 &&\downarrow{\scriptstyle\beta}&&\Vert&&\Vert\\
 0&\longrightarrow&Q&\longrightarrow&Q_f
 &\longrightarrow&Q_f/Q&\longrightarrow&0.
 \end{array}
 \tag{BL.13}
\]
The two kernels are equal, so \(\widehat A\otimes_A M=Q\), with precisely the required overlap map. The equality records a canonical isomorphism, not a change of coefficient ring.

For uniqueness, tensor (BL.5) with an \(f\)-regular module \(N\). Right exactness, together with the already injective map \(N\to N_f\), gives
\[
 0\longrightarrow N\longrightarrow N_f\longrightarrow
 (\widehat A\otimes_A N)_f/(\widehat A\otimes_A N)
 \longrightarrow0.
 \tag{BL.14}
\]
The quotient identification follows by tensoring the defining cokernel \(\widehat A\to\widehat A_f\); (BL.9) makes the resulting denominator a submodule. Thus the prescribed triple recovers \(N\) by the kernel (BL.11). A compatible pair of maps carries that kernel to the other kernel, yielding a unique global map. Its scalar extensions are the original pair by (BL.12)–(BL.13). This proves full faithfulness as well as essential surjectivity.

The ring version, and its module counterpart, are illustrated together by
\[
\begin{array}{ccccc}
 A&\longrightarrow&A_f&&
 P\oplus Q\\
 \downarrow&&\downarrow&&
 \big\downarrow{\scriptstyle (p,q)\mapsto\theta(p)-q}\\
 \widehat A&\longrightarrow&\widehat A_f&&Q_f.
\end{array}
 \tag{BL.15}
\]
*The left square is a fibre-product square of rings, by (BL.2) and (BL.5). On the right, the kernel is the compatible-pair module, equivalent to (BL.11); the map is onto by the same proof as (BL.12). Its recovery after the two scalar extensions is (BL.13)–(BL.14). The exactness comes from the power-torsion calculation (BL.6)–(BL.8), not an assumption that the completed ring is flat.*

### 7.2. Flatness, finite projectivity and arbitrary base change

The equivalence above preserves the finiteness properties required for vector bundles. Finite generation descends by the argument following (BL.4). Flatness needs its own proof.

We use the following elementary homological criterion, with its justification included. Choose a free resolution \(F_\bullet\to L\) of an arbitrary module \(L\): successively take a free module surjecting onto each kernel. A module \(N\) is flat exactly when
\[
 H_1(N\otimes_A F_\bullet)=0
 \quad\text{for every }L.
 \tag{BL.16}
\]
Flatness means that tensor preserves injections; tensor is already right exact. If tensor is exact, it preserves the cycles and boundaries of a resolution, giving the displayed vanishing. Conversely, let \(K\subset F_0\) be the kernel of a free surjection onto \(L\). Right exactness applied to \(F_2\to F_1\to K\) shows that the displayed first homology is the kernel of \(N\otimes K\to N\otimes F_0\). For an arbitrary injection \(L'\to V\) with quotient \(L\), form \(E=V\times_L F_0\). The sequence \(0\to L'\to E\to F_0\to0\) splits, since a basis of \(F_0\) has lifts in \(E\), and \(0\to K\to E\to V\to0\) is exact. If an element of \(N\otimes L'\) maps to zero in \(N\otimes V\), right exactness lifts its image in \(N\otimes E\) from \(N\otimes K\). Its projection to \(N\otimes F_0\) is zero, so (BL.16) makes that lift zero. The original element is zero because the first sequence split. Thus tensor preserves every injection.

Assume that \(P\) is flat over \(A_f\) and \(Q\) is flat over \(\widehat A\). Put
\[
 Q_n=Q/f^nQ,
 \qquad T=Q_f/Q=\varinjlim_n Q_n,
 \qquad Q_n\longrightarrow Q_{n+1},\quad q\longmapsto fq.
 \tag{BL.17}
\]
The limit description follows by writing a fraction as \(q/f^n\). The module \(Q_n\) is flat over \(A/f^nA\): any injection of modules over that quotient is also an injection of \(\widehat A\)-modules, and its tensor with \(Q\) is its tensor with \(Q_n\).

For the free resolution in (BL.16), there is a degreewise exact sequence of complexes
\[
 0\longrightarrow F_\bullet\xrightarrow{\ f^n\ }F_\bullet
 \longrightarrow F_\bullet/f^nF_\bullet\longrightarrow0.
 \tag{BL.18}
\]
It gives \(H_i(F_\bullet/f^nF_\bullet)=0\) for \(i\geq2\). For clarity, the homology exact sequence here is obtained by lifting a quotient cycle to the middle complex, taking its differential in the first complex, and passing to that differential's homology class. Changing a lift or a cycle by a boundary changes the class by a boundary. A class maps to zero exactly when that lift can be changed to a cycle or a boundary as appropriate; this proves exactness at each of the three successive terms. Since the free resolution has zero positive homology, the asserted vanishing follows. In degree one the same calculation gives the kernel of multiplication by \(f^n\) on \(L\), which may be nonzero.

Tensoring this quotient complex with the flat \(A/f^nA\)-module \(Q_n\) preserves its homology. Therefore
\[
 H_i(Q_n\otimes_A F_\bullet)=0\quad(i\geq2),
 \qquad H_i(T\otimes_A F_\bullet)=0\quad(i\geq2).
 \tag{BL.19}
\]
The second statement follows from (BL.17). Tensor commutes with a filtered direct limit by its balanced presentation, and such limits preserve exactness: a finite collection of elements and equations appears at one common stage, and an element which becomes zero vanishes at some later stage. This also proves that homology commutes with this particular limit.

Tensor (BL.12) degreewise with \(F_\bullet\). Each \(F_i\) is free, so this is an exact sequence of complexes. The module \(P\) is flat over \(A\), since localization is exact and it is flat over \(A_f\). Its tensor complex has zero positive homology. The homology exact sequence and (BL.19) now give (BL.16) for \(M\). Thus
\[
 P\text{ flat over }A_f, Q\text{ flat over }\widehat A
 \quad\Longrightarrow\quad M\text{ flat over }A.
 \tag{BL.20}
\]
The converse is base change of flatness: an injection over a scalar-extension ring, viewed over \(A\), remains injective after tensoring with a flat \(A\)-module. This proves flatness recognition without Noetherian assumptions.

**Finite projectivity.** A finite projective module is a direct summand of a finite free module. Such modules have duals and commute with every scalar extension. If \(P,Q\) are finite projective, glue their duals and endomorphism modules, obtaining modules \(D,E\). By full faithfulness in §7.1,
\[
 D=\operatorname{Hom}_A(M,A),\qquad
 E=\operatorname{End}_A(M).
 \tag{BL.21}
\]
To check the overlap identifications, represent a finite projective module by an idempotent matrix \(e\). Its dual is the corresponding transpose summand, and its endomorphisms are \(e\operatorname{Mat}(A)e\); all these formulas remain true after any scalar extension. Thus the prescribed dual and endomorphism pairs really are gluing triples. Compatible local linear maps are global maps by (BL.14), giving (BL.21).

The cokernel of the rank-one map
\[
 M\otimes_A D\longrightarrow E,
 \qquad m\otimes\ell\longmapsto(x\mapsto\ell(x)m)
 \tag{BL.22}
\]
vanishes after both scalar extensions. Over each ring a finite projective module has a finite dual basis, obtained by projecting a basis and its coordinate functionals from a finite free module. Its endomorphisms are therefore sums of rank-one maps. Right exactness and (BL.4) show that the cokernel of (BL.22) is zero over \(A\). In particular there are finitely many \(m_j\in M\), \(\ell_j\in D\) with
\[
 x=\sum_j\ell_j(x)m_j\quad(x\in M).
 \tag{BL.23}
\]
The maps \(A^r\to M\), \((a_j)\mapsto\sum a_jm_j\), and \(M\to A^r\), \(x\mapsto(\ell_j(x))\), have composite identity. They exhibit \(M\) as a finite free summand. This proves finite projectivity recognition directly, including projectivity rather than only finite presentation. The forward implication is scalar extension of the splitting.

For flat modules the equivalence is symmetric monoidal. The tensor of two flat modules is flat, because its tensor functor is a composite of two exact tensor functors, and is consequently \(f\)-regular. Ordinary scalar extension respects tensor products. The inverse gluing theorem therefore identifies
\[
 \operatorname{Glue}(P,Q,\theta)\otimes_A
 \operatorname{Glue}(P',Q',\theta')
 \simeq\operatorname{Glue}(P\otimes P',Q\otimes Q',\theta\otimes\theta').
 \tag{BL.24}
\]
The unit, permutation, associativity and evaluation maps agree after both extensions and hence agree globally by full faithfulness. The same statement applies to the finite projective subcategory.

Let \(A\to A'\) be any ring map for which the image of \(f\) is a nonzero divisor. For flat or finite projective \(M\), its pullback is again flat or finite projective and hence \(f\)-regular. Its gluing data are
\[
 \begin{aligned}
 M\otimes_A A'&\longleftrightarrow
 \bigl(P\otimes_{A_f}A'_f,
       Q\otimes_{\widehat A}\widehat{A'},\theta'\bigr),\\
 \widehat{A'}&=\varprojlim_n A'/f^nA'.
 \end{aligned}
 \tag{BL.25}
\]
Both sides have those scalar extensions by tensor associativity, so uniqueness proves the formula, including nonflat coefficient maps. The completed ring is the displayed inverse limit; no assertion that ordinary tensor commutes with this inverse limit is used.

### 7.3. Flat algebras and affine torsors

The monoidal statement proves gluing for flat commutative algebras. Given flat algebras \(C_1\) over \(A_f\) and \(C_2\) over \(\widehat A\), with an algebra isomorphism on the overlap, glue their underlying modules to \(C\). The two unit maps and multiplication maps give unique maps
\[
 A\longrightarrow C,\qquad C\otimes_A C\longrightarrow C.
 \tag{BL.26}
\]
The tensor source is flat, hence \(f\)-regular. Associativity, commutativity and the unit identities hold after both scalar extensions, so full faithfulness makes them hold over \(A\). Thus \(C\) is a flat commutative \(A\)-algebra with the prescribed algebra extensions. Algebra maps descend for the same reason. If both local algebras are faithfully flat, then \(C\) is faithfully flat: if \(C\otimes_A L=0\), the two local faithful-flatness assertions give \(L_f=0\) and \(\widehat A\otimes_A L=0\), and (BL.4) gives \(L=0\).

Let \(G\) be an affine group scheme over a field \(k\), with finitely presented coordinate Hopf algebra \(H=k[G]\), and let \(A\) be a \(k\)-algebra as in §7.1. Every \(k\)-module is flat, so \(H_A=A\otimes_k H\) is flat over \(A\). In affine coordinates a right torsor is a faithfully flat commutative \(A\)-algebra \(C\), with coaction \(\delta:C\to C\otimes_k H\), satisfying the coassociativity and counit equations and with canonical isomorphism
\[
 \operatorname{can}:C\otimes_A C\xrightarrow{\ \sim\ }C\otimes_k H,
 \qquad c\otimes d\longmapsto(c\otimes1)\delta(d).
 \tag{BL.27}
\]
Geometrically its inverse describes the unique group element taking one torsor point to another. The map on schemes is \((p,g)\mapsto(p,pg)\). Thus (BL.27) states precisely that the torsor becomes the trivial \(G\)-torsor after the cover \(\operatorname{Spec}C\to\operatorname{Spec}A\).

Suppose such affine torsors are given over \(A_f\) and \(\widehat A\), and their overlap isomorphism is \(G\)-equivariant. Glue the flat algebras as above. The two coactions descend to \(C\to C\otimes_k H\) because the tensor target is flat. Their identities descend from the corresponding identities on the pieces. The local canonical isomorphisms and their inverses also descend, since all the tensor modules in (BL.27) are flat. Consequently the global canonical map is an isomorphism. Faithful flatness was just proved. This constructs the affine torsor and every equivariant arrow, with no choice of a representation of \(G\).

We verify that this cover is also fppf. The algebra \(C\otimes_A C\), viewed as an algebra over its first factor, is finitely presented by (BL.27), because \(H\) is. Finite presentation of an algebra descends along a faithfully flat scalar extension by the following elementary argument. Suppose \(B\) is faithfully flat over \(A\) and \(D\otimes_A B\) is finitely presented over \(B\). Choose finitely many generators there and express them as sums of coefficients from \(B\) times elements of \(D\). Those finitely many elements generate an \(A\)-subalgebra \(D_0\). Flatness embeds \(D_0\otimes B\) in \(D\otimes B\), and the chosen generators make this inclusion onto. The quotient module \(D/D_0\) tensors to zero, so it is zero by faithful flatness. Write \(D=A[x_1,\ldots,x_r]/I\). After tensoring with \(B\), the relation ideal is finitely generated. Every chosen generator involves finitely many elements of \(I\); let \(J\subset I\) be the ideal they generate over \(A[x_1,\ldots,x_r]\). Then \((I/J)\otimes_A B=0\), again using flatness to identify the extended ideals. Faithful flatness gives \(I=J\), so \(D\) is finitely presented. Here the kernel of any fixed finite polynomial presentation of a finitely presented algebra is finitely generated: take a finite presentation with other generators, express both sets in terms of one another, and add the finitely many resulting substitution relations. Eliminating the other generators gives a finite relation list for the fixed presentation.

Apply this argument with \(B=C\), \(D=C\). The resulting affine map is flat, finitely presented and surjective. Surjectivity follows directly from faithful flatness: for every prime \(\mathfrak p\), the algebra \(C\otimes_A\kappa(\mathfrak p)\) is nonzero, so one of its prime ideals gives a point above \(\mathfrak p\). This proves the fppf assertion and hence the claimed torsor trivialization.

We have proved the groupoid equivalence
\[
 \operatorname{Tors}^{\mathrm{aff}}_G(A)
 \simeq
 \operatorname{Tors}^{\mathrm{aff}}_G(A_f)
 \mathop{\times}_{\operatorname{Tors}^{\mathrm{aff}}_G(\widehat A_f)}
 \operatorname{Tors}^{\mathrm{aff}}_G(\widehat A).
 \tag{BL.28}
\]
The product is a groupoid product: an overlap isomorphism and compatible arrows are part of the data. Section 7.5 proves that every \(G\)-torsor under an affine finitely presented group is affine over its base, with effective fppf descent and the full equivariant dictionary. It therefore identifies the affine torsor groupoids in (BL.28) with the usual torsor groupoids. The result (BL.28) itself is the full affine-torsor gluing calculation. It does not use reductivity, simply connectedness, or characteristic zero. For vector bundles, the equivalence of §7.2 already gives the required gluing without this additional affineness dictionary.

The construction respects every coefficient map allowed in (BL.25). A flat glued algebra stays flat after base change, and its torsor isomorphism and inverse stay inverse after tensoring. Its formal piece is extended to the new completed ring. Thus the torsor comparison is compatible with arbitrary, including nonflat and nonreduced, parameter changes for which the Cartier equation remains a nonzero divisor.

### 7.4. The curve, loop matrices and the missing uniformization step

Let \(x\) be the fixed smooth rational point of the curve, and put \(U=X\setminus\{x\}\). Choose an affine neighbourhood \(W=\operatorname{Spec}A_0\) and a function \(t\) cutting out exactly the reduced point \(x\) on \(W\). Such a choice follows from the uniformizer in the local discrete valuation ring: extend it to a neighbourhood and remove the other finitely many zeros. The existence of this affine neighbourhood and the regular local description of a smooth curve remain part of the stated curve foundations. Once chosen, the algebra below is explicit.

We have \(A_0/tA_0=k\) and \(t\) is a nonzero divisor. Induction using multiplication by \(t\) shows
\[
 k[t]/t^n\xrightarrow{\ \sim\ }A_0/t^nA_0.
 \tag{BL.29}
\]
For surjectivity, subtract the constant residue, divide the remainder by \(t\), and repeat \(n\) times. For injectivity, a polynomial of degree below \(n\) which vanishes modulo \(t^n\) has zero constant term; divide by \(t\) using cancellation and induct. For every ordinary \(k\)-algebra \(R\), tensoring these identities over the field and then taking their inverse limit gives
\[
 \begin{aligned}
 A&=A_0\otimes_k R,&A_f&=A[1/t],\\
 \widehat A&=R[[t]],&\widehat A_f&=R((t)).
 \end{aligned}
 \tag{BL.30}
\]
Multiplication by \(t\) remains injective, because tensor over a field preserves the injection on \(A_0\). This includes arbitrary non-Noetherian and nonreduced \(R\).

Given a vector bundle on \(U_R\), a vector bundle on \(D_R=\operatorname{Spec}R[[t]]\), and an isomorphism of their restrictions to \(D_R^\times=\operatorname{Spec}R((t))\), restrict the first bundle to \((W\cap U)_R=\operatorname{Spec}A[1/t]\). Section 7.2 constructs a finite projective module on \(W_R\), with precisely that punctured restriction and formal piece. Glue it to the original bundle on \(U_R\) across the open intersection. Ordinary open-set gluing is explicit: sections are pairs of local sections agreeing on the overlap; the locally free trivializations on the two opens furnish its bundle charts. The maps glue in the same way. These opens cover \(X_R\). Uniqueness in §7.1 proves independence of the neighbourhood and produces the inverse equivalence, including every arrow. The same argument for the affine torsors of §7.3 glues their schemes, group actions and trivializations over the two opens.

The geometric square is
\[
 \begin{array}{ccc}
 D_R^\times&\longrightarrow&D_R\\
 \downarrow&&\downarrow\\
 U_R&\longrightarrow&X_R.
 \end{array}
 \tag{BL.31}
\]
*The bottom arrow is the punctured open inclusion. The right arrow is the map given by the completed local coordinate ring (BL.29)–(BL.30). Its pullback of the punctured open is exactly \(t\ne0\), so the square is cartesian. Vector bundles glue across this square by the actual kernel (BL.11), flatness (BL.20) and finite projectivity (BL.21)–(BL.23). Affine torsors glue by the coaction and canonical isomorphism (BL.26)–(BL.28). This is the gluing mechanism; existence of a trivialization on the entire punctured curve is a separate theorem.*

Changing a chosen uniformizer changes only the coordinates of the same completed local ring. Each finite quotient in (BL.29) is intrinsic, and an alternative parameter is \(t\) times a formal unit. Substitution gives inverse ring maps on every finite quotient and on their limit. The overlap identifications and the kernel comparison therefore agree by uniqueness. Arbitrary change of \(R\) uses (BL.25) and (BL.30); the new formal ring is \(R'[[t]]\), with no ordinary-tensor identification of that ring asserted.

**Both frames and the right quotient.** Fix trivializations on \(U_R\) and \(D_R\). For \(GL_n\), specify the transition from the formal frame into the punctured-curve frame by
\[
 g\in GL_n(R((t))),\qquad
 \theta=g^{-1}:A[1/t]^n\otimes_A R[[t]]\longrightarrow R((t))^n.
 \tag{BL.32}
\]
The glued module on \(W_R\) is
\[
 M_g=\{p\in A[1/t]^n:g^{-1}p\in R[[t]]^n\}.
 \tag{BL.33}
\]
Thus the formal lattice in the punctured frame is \(gR[[t]]^n\). Changing the formal trivialization by \(h\in GL_n(R[[t]])\) replaces \(g\) by \(gh\). Changing the punctured-curve trivialization by a matrix \(a\) on \(U_R\) replaces \(g\) by \(ag\). These are the right formal and left punctured actions used in the quotient of §7.

Formal frames exist locally on the parameter scheme for a rank-\(n\) vector bundle on \(D_R\). Its reduction modulo \(t\) is a finite projective rank-\(n\) \(R\)-module, hence is free on a Zariski cover. Here is the local freeness fact: localize a finite free summand at a prime, choose lifts of a basis of its residue vector space, and apply Nakayama to the module and the kernel of the resulting split surjection. Both are finitely generated; the kernel has zero residue space and is zero. Clearing finitely many denominators extends the basis to a basic neighbourhood. Nakayama itself follows by writing a finite generating system in terms of itself with coefficients in the maximal ideal and applying the adjugate matrix to \(I-B\), whose determinant is a unit. This proves the asserted Zariski cover.

After the corresponding completed coefficient change, lift this basis to the formal module. The ideal \((t)\) is in the Jacobson radical of \(R'[[t]]\): every \(1-ta\) has inverse \(\sum_{j\geq0}(ta)^j\). The same adjugate proof of Nakayama makes the lifted map from a finite free module onto the formal module surjective. It splits because the module is projective. Its finite projective kernel has zero reduction, hence is zero by Nakayama again. This constructs the required formal frame. Therefore the Zariski, and also fppf, sheaf right quotient classifies the vector bundles with punctured-curve framing:
\[
 \operatorname{Gr}_{GL_n,x}
 =GL_n((t))/GL_n[[t]].
 \tag{BL.34}
\]
The sheaf qualification allows formal bundles which are not globally framed over \(R\).

For an arbitrary affine \(G\), (BL.28) similarly identifies torsors equipped with both trivializations with \(G(R((t)))\), with the same two actions. To forget the formal trivialization on every torsor, one also needs its formal local triviality after a coefficient cover. The formal lifting argument is precise: reduce the torsor modulo \(t\), choose a coefficient fppf cover on which it has a section, and lift that section successively across \(R'[[t]]/t^n\). If the affine torsor is formally smooth, its defining lifting property supplies the next lift. Compatible lifts give a section over \(R'[[t]]\), since maps from an affine algebra to an inverse limit are compatible maps to its quotients. Section 7.6 proves this formal lifting property for every affine torsor of a smooth group by faithfully flat descent of a split conormal sequence. The vector-bundle construction above proves the needed formal triviality for \(GL_n\) directly.

**Two computations fixing the convention.** For \(X=\mathbf P^1\), take \(x=0\), \(W=\operatorname{Spec}R[t]\), and \(U=\operatorname{Spec}R[t^{-1}]\). For \(g=t^d\) in rank one, (BL.33) gives
\[
 M_g=t^dR[t],\qquad E_g=\mathcal O_{X_R}(-d\,x).
 \tag{BL.35}
\]
Indeed the formal frame has rational image \(t^d\), the generator of the \(d\)-th power of the ideal of \(x\); for negative \(d\) use its inverse line. The geometric degree is \(-d\). This explains the sign relating the lattice convention to the line bundles of §7.

For \(R=k[\epsilon]/(\epsilon^2)\), take
\[
 g=\begin{pmatrix}1&\epsilon t^{-1}\\0&1\end{pmatrix},
 \qquad
 M_g=R[t]\binom{1}{0}\oplus R[t]\binom{\epsilon t^{-1}}{1}.
 \tag{BL.36}
\]
The matrix and its inverse are in \(GL_2(R[t,t^{-1}])\). Multiplication by \(g^{-1}\) identifies the displayed module with \(R[t]^2\), since \(R[t,t^{-1}]\cap R[[t]]=R[t]\), a special case of (BL.5). It becomes the identity over the reduced coefficient field but is not in \(GL_2(R[[t]])\); the pole coefficient \(\epsilon\) remains nonzero. Thus its punctured-framed Grassmannian point is a nontrivial infinitesimal point. The underlying bundle on \(\mathbf P^1_R\) is trivial, because \(g\) also lies in \(GL_2(R[t^{-1}])\) and can be removed by changing the punctured frame. Gluing retains this distinction rather than testing only reduced points.

The following table summarizes the maps and their exact domains.

| Data or operation | Domain and target | Proven mechanism |
|---|---|---|
| Module reconstruction | \((P,Q,\theta)\mapsto\ker(P\to Q_f/Q)\) | Power-torsion tensor exactness, (BL.6)–(BL.14) |
| Vector bundle reconstruction | Finite projective modules on the two affine pieces | Dual basis and rank-one endomorphisms, (BL.21)–(BL.23) |
| Affine torsor reconstruction | Flat coordinate algebras and compatible \(G\)-coactions | Monoidal gluing, faithful flatness and canonical torsor isomorphism, (BL.26)–(BL.28) |
| Parameter change | Every \(R\to R'\), including nonflat maps | New completed ring \(R'[[t]]\), (BL.25), (BL.30) |
| Formal frame change | \(g\mapsto gh\), \(h\in G(R[[t]])\) | Right quotient, (BL.32)–(BL.34) |
| Punctured frame change | \(g\mapsto ag\), \(a\in G(U_R)\) | Left action; it forgets the punctured trivialization |

*The curve square (BL.31), the lattice kernel (BL.33), and the two examples (BL.35)–(BL.36) show what is glued and what the two frame changes forget. All the module and affine-torsor calculations allow arbitrary coefficient rings. The smooth-curve neighbourhood retains its stated curve foundations; §§7.5–7.6 prove affine fppf descent and smooth-torsor formal lifting using the precisely linked earlier scheme-cover results. For the classical source of the gluing theorem, see Beauville–Laszlo, [*Un lemme de descente*, freely accessible author version, §§2–4](https://math.univ-cotedazur.fr/~beauvill/pubs/descente.pdf). The complete algebraic proof used here is (BL.1)–(BL.28).*

This closes the formal-disc gluing calculation. It proves no generic triviality theorem for torsors and supplies no new trivialization on \(U_R\). Section 7.8 now supplies the distinct semisimple family theorem from its full earlier programme proof. The determinant obstruction for \(GL_n\) and the missing degree-zero line bundles for \(\mathbb G_m\) in §7 are unchanged.

### 7.5. Faithfully flat descent, affineness and frames

We now supply the descent and torsor dictionaries used above. The algebraic statements in this section work over every commutative ring. For schemes we use the usual functor of points, affine charts and gluing of schemes along open subsets. The covering refinement used for an arbitrary fppf family is specified below, with its earlier proof.

Let \(R\to B\) be faithfully flat: tensoring with \(B\) is exact and detects a zero module. Flat tensor preserves the kernels, images and quotients defining homology, so it also detects exactness of complexes and isomorphisms of maps. In particular, for every module \(L\), the augmented complex
\[
 0\longrightarrow L\longrightarrow B\otimes_R L
 \longrightarrow B\otimes_R B\otimes_R L\longrightarrow\cdots
 \tag{FD.1}
\]
is exact. The differential is the alternating sum of insertions of \(1\) in the \(B\)-factors. To prove this, tensor once more with \(B\), retaining that extra factor as the coefficient factor. The maps
\[
 \begin{aligned}
 h(a\otimes b_0\otimes\cdots\otimes b_n\otimes l)
   &=ab_0\otimes b_1\otimes\cdots\otimes b_n\otimes l,\\
 hd+dh&=1
 \end{aligned}
 \tag{FD.2}
\]
contract the tensored complex, including its augmentation. The insertion in the first position gives the identity; each other insertion cancels the corresponding term in \(dh\). Exactness descends by faithful flatness. This proves both the injection into the first term and its equalizer description.

**Effective module descent.** A module descent datum consists of a \(B\)-module \(N\) and a \(B\otimes_R B\)-linear isomorphism
\[
 \theta:N\otimes_R B\xrightarrow{\sim}B\otimes_R N,
 \qquad \rho(n)=\theta(n\otimes1).
 \tag{FD.3}
\]
Here the first \(B\)-coordinate acts on \(N\) in the source and on the first factor in the target. The datum satisfies the cocycle identity on three coordinates. Its restriction to the diagonal is the identity: the cocycle makes that invertible diagonal map idempotent. Consequently, writing \(\rho(n)=\sum_i b_i\otimes n_i\), we have
\[
 \mu\rho(n)=n,\qquad
 (1\otimes\rho)\rho(n)=\sum_i b_i\otimes1\otimes n_i,
 \quad\mu(b\otimes n)=bn.
 \tag{FD.4}
\]
The second equality says that transport through the second coordinate and then the third is direct transport to the third. It is exactly the cocycle applied to \(n\otimes1\otimes1\). Also \(\rho(bn)=(b\otimes1)\rho(n)\).

Put
\[
 M=\ker\bigl(\rho-(n\mapsto1\otimes n)\bigr),\qquad
 \lambda:B\otimes_R M\longrightarrow N,\quad b\otimes m\mapsto bm.
 \tag{FD.5}
\]
Flatness identifies \(B\otimes_R M\) with the kernel of the two induced maps from \(B\otimes_R N\) to \(B\otimes_R B\otimes_R N\). Equation (FD.4) puts \(\rho(N)\) in that kernel. Thus \(\rho\) takes values in \(B\otimes_R M\). It is inverse to \(\lambda\): their composite on \(N\) is \(\mu\rho=1\), and on a tensor \(b\otimes m\) the other composite is \(\rho(bm)=b\otimes m\). This proves effectivity. The equality \(\theta(n\otimes b)=(1\otimes b)\rho(n)\) proves that the isomorphism recovers the entire datum.

A compatible map preserves the equalizer and hence descends. Conversely a map of descended modules extends to a compatible map; uniqueness follows from (FD.1). The equalizer of the canonical datum on \(B\otimes_R L\) is exactly \(L\), again by (FD.1). We have therefore proved an equivalence of categories, including every morphism. It is symmetric monoidal: scalar extension preserves tensor products and their canonical data, so full faithfulness identifies the tensor of the descended objects with the descended tensor datum. Associativity, interchange and units are checked after the faithful extension. No flatness of \(M\) or \(N\) is required for this tensor statement.

Finite projectivity descends as well. If \(N\) is finite projective, the inverse transpose of its overlap map supplies descent data on its dual; conjugation supplies the datum on its endomorphisms. The idempotent-matrix calculation in §7.2 verifies that these modules commute with scalar extension. Descend them to \(D,E\). Full faithfulness identifies \(D=\operatorname{Hom}_R(M,R)\) and \(E=\operatorname{End}_R(M)\). The rank-one map from \(M\otimes_R D\) to \(E\) becomes onto over \(B\), since \(N\) has a finite dual basis. Its cokernel is zero by faithful flatness. In particular
\[
 1_M=\sum_{j=1}^q m_j\ell_j,
 \qquad M\ \text{is a direct summand of }R^q.
 \tag{FD.6}
\]
The splitting maps are \(x\mapsto(\ell_j(x))\) and \((a_j)\mapsto\sum a_jm_j\). This proves finite projectivity directly. Flatness descends by testing an injection after \(B\): tensoring it with \(M\), and then with \(B\), is tensoring its base change with the flat \(N\). Faithful flatness detects the resulting injection. The same argument detects faithful flatness of a descended algebra.

For every map \(R\to R'\), set \(B'=B\otimes_R R'\). This is faithfully flat over \(R'\): tensor of a nonzero \(R'\)-module with it is tensor of that module, viewed over \(R\), with \(B\). The base-changed datum is the canonical datum of
\[
 M'=M\otimes_R R',\qquad
 N'=N\otimes_B B'=B'\otimes_{R'}M'.
 \tag{FD.7}
\]
Uniqueness of descent proves the comparison for every map, including nonflat ones. This argument does not assume that such a map preserves an arbitrary kernel.

**From algebras to schemes.** For an algebra datum the equalizer \(C_0\subset C\) of (FD.5) is an algebra: the two maps defining it preserve products and the identity. The isomorphism \(B\otimes_R C_0\simeq C\) is an algebra isomorphism. Algebra maps descend by full faithfulness, and equivariant actions descend by the monoidal statement. Taking spectra proves effective descent for affine schemes over a faithfully flat affine cover.

The comparison with existing schemes requires descent of morphisms. We prove it next. First, a faithfully flat affine map is universally a quotient map on underlying spaces. Here is a proof of the topology needed for this assertion. The spectrum of any ring is compact and Hausdorff for the topology generated by its principal opens and their complements. An ultrafilter has limit the prime consisting of those \(a\) for which \(V(a)\) belongs to the ultrafilter; the identities for \(V(ab)\) and \(V(a+b)\) prove primality, and the prescribed membership in every principal open proves convergence. The usual extension of a family with the finite-intersection property to an ultrafilter proves compactness. Distinct primes are separated by a principal open and its complement. Ring maps are continuous for this topology, so the image of an affine scheme is compact for it.

A constructibly compact subset stable under specialization is Zariski closed. If \(\mathfrak p\) is in its Zariski closure, its intersections with \(D(a)\), \(a\notin\mathfrak p\), have the finite-intersection property. Compactness gives a prime \(\mathfrak q\) in the subset avoiding all such \(a\), so \(\mathfrak q\subset\mathfrak p\); specialization stability gives \(\mathfrak p\) in the subset. Flat maps lift generizations: the local flat map at a chosen point is faithfully flat, and hence surjective on spectra, so a prime below its image lifts to a prime below that point. For the faithful assertion in the local case, a nonzero module contains a nonzero cyclic submodule \(R/I\); flatness preserves its injection, and its tensor is nonzero because \(I\) lies in the maximal ideal whose image lies in the target maximal ideal. Surjectivity on spectra follows because each residue-field tensor is a nonzero algebra and has a prime.

Suppose the inverse image of a subset under a faithfully flat affine map is closed. On an affine target this inverse image is affine, so its image is constructibly compact. Its image is specialization stable: choose a point over a specialization, lift the given generization by flatness, and use closedness upstairs. Surjectivity identifies this image with the original subset, which is therefore closed. Taking complements proves the quotient assertion. The proof survives every base change, because faithful flatness does.

An invariant open upstairs is saturated on points. Two points above the same base point have a common point in the fibre product: their residue fields have a nonzero tensor product over the common residue field. Invariance gives the same membership for both points. The quotient assertion therefore descends that open. We obtain the cartesian square
\[
 \begin{array}{ccc}
 U'&\hookrightarrow&Y_B\\
 \downarrow&&\downarrow\\
 U&\hookrightarrow&Y.
 \end{array}
 \tag{FD.8}
\]
*The horizontal maps are open inclusions. The right map is the faithfully flat affine projection. Invariance means that the two inverse images of \(U'\) agree; the descended open is \(U\), and its inverse image is exactly \(U'\). This is a statement about the given scheme \(Y\), with no separation hypothesis.*

Now let a morphism \(Y_B\to Z_B\) between existing schemes be compatible with the canonical data. The inverse image of each affine open of \(Z\) descends to an open of \(Y\) by (FD.8). On an affine subopen \(W\) of that descended open, its coordinate map takes values in the equalizer (FD.1), namely \(\Gamma(W,\mathcal O_W)\). It defines a unique map from \(W\) to the chosen target affine. These maps agree on intersections. Their images there lie in the intersection of the target opens, as can be checked after the surjective cover; cover that intersection by affines and apply the same equalizer to compare functions. Ordinary open gluing gives the descended morphism. Its structural map to the base agrees after the cover and hence agrees by the same argument. This proves existence and uniqueness, including for nonseparated schemes. An isomorphism descends together with its inverse.

For arbitrary fppf covering families of an affine base, use the finite affine refinement proved in [*Algebraic spaces*](../../AG-AS/src/algebraic-spaces.md), §2.0.2. Its ingredients have the following precise scope. Flat locally finitely presented maps are open by [*Flat morphisms*](../../AG-FSE/src/flat-morphisms.md), Theorem 3.2, using the constructible-image theorem proved in [*Quasi-finite morphisms and Chevalley’s theorem*](../../AG-MO/src/quasi-finite-morphisms-and-chevalley.md), Theorem 5.1. Thus the images of affine pieces of the covering schemes form an open cover of the affine base; quasi-compactness selects finitely many pieces. Their finite disjoint union is an affine faithfully flat finitely presented cover. The finite-presentation localization argument in *Algebraic spaces*, §2.0.2, proves the required finiteness for each affine piece even over a non-Noetherian base. Comparison with every unchosen member is checked after this refinement and follows from uniqueness of morphism descent. Over a general base perform these constructions on affine opens and glue by their unique comparisons. These are the earlier scheme-topological foundations used in passing from a ring cover to an arbitrary fppf family; the affine algebra and morphism descent proofs themselves are given above.

It follows that an affine scheme over a cover, with compatible transition maps, descends to a scheme affine over the base. If an existing scheme becomes affine over that cover, the descended affine scheme is isomorphic to it: descend the comparison isomorphism and its inverse. Thus affineness descends.

Apply this to a \(G\)-torsor, where \(G\) is affine over \(k\) and \(H=k[G]\) is finitely presented. Its local trivializations have coordinate algebras \(B\otimes_k H\); their equivariant transition maps give algebra descent data. The descended algebra \(C\) is faithfully flat by the tensor test following (FD.6), finitely presented by the argument in §7.3, and carries the descended coaction. The canonical map is an isomorphism because it is one after the faithful extension:
\[
 P=\operatorname{Spec}C,\qquad
 C\otimes_R C\xrightarrow{\sim}C\otimes_k H.
 \tag{FD.9}
\]
This also represents a torsor initially defined as an fppf sheaf: the two sheaves are locally the same trivial torsor and their identifications agree by descent. Conversely (FD.9), faithful flatness and finite presentation trivialize the torsor on its own fppf cover, as proved in §7.3. Thus the scheme-theoretic and affine Hopf-algebra descriptions agree. Compatible actions and equivariant arrows descend, so torsors and their isomorphisms form the fppf stack used in §1. All constructions respect arbitrary base change by (FD.7).

For \(GL_n\) the vector-bundle dictionary is equally concrete. For a finite projective rank-\(n\) module \(M\), its frame functor is
\[
 \operatorname{Fr}(M)(T)=
 \operatorname{Isom}_T(T^n,M\otimes_R T).
 \tag{FD.10}
\]
It is an affine scheme of finite presentation. Indeed parametrize a pair of maps \(u:T^n\to M_T\), \(v:M_T\to T^n\) by the symmetric algebra on the dual of the finite projective module of such pairs, and impose \(vu=1\), \(uv=1\). These are finitely many equations: finite dual bases write all their coefficients in finite generating lists. A symmetric algebra on a finite free summand has a finite presentation by its idempotent linear relations. On a finite Zariski cover where \(M\) is free, this scheme is \(GL_n\), with coordinate algebra the polynomial matrix algebra with the determinant inverted. This algebra is flat and finitely presented, and its identity matrix supplies a point of every fibre. Flatness descends by (FD.6) applied to the finite principal-open cover, and the nonzero-fibre test proves faithful flatness. The local freeness and finite-cover assertion is the Nakayama argument already proved in §7.4. Precomposition of a frame gives the right \(GL_n\)-action; two frames differ by a unique invertible matrix, proving the torsor identity.

Conversely trivialize a \(GL_n\)-torsor on a cover and transport its standard free module by the transition matrices. The matrix cocycle is precisely the datum (FD.3), so (FD.5)–(FD.6) produce a finite projective module. It has rank \(n\): after a residue-field extension supplied by a point of the faithful cover its rank is \(n\), and dimension of a finite-dimensional vector space is unchanged by field extension. Its frame torsor has exactly the original local trivializations and comparisons. Linear isomorphisms and equivariant frame isomorphisms correspond locally by the same matrix, hence globally by descent. Gluing on affine charts gives the equivalence
\[
 \begin{gathered}
 \{\text{rank-}n\text{ vector bundles on }S\}
 \simeq\{GL_n\text{-torsors on }S\},\\
 n=1:\ \mathbb G_m\text{-torsors are line bundles}.
 \end{gathered}
 \tag{FD.11}
\]
For completeness, the affine module dictionary used here follows from the same calculation. A locally free sheaf on an affine base has a finite principal-open trivializing cover. Apply (FD.5) to the free modules and their transition matrices on its finite product covering algebra; (FD.6) gives a finite projective module. The equalizer for sections on that cover identifies its associated sheaf with the given bundle. Conversely the local bases of a finite projective module give its locally free sheaf, and linear maps agree by the equalizer. This proves the dictionary used in §§1 and 7.4, including its arrows and arbitrary parameter changes. In (FD.11) the arrows are isomorphisms, so it is an equivalence of groupoids.

### 7.6. Smooth torsors and successive formal lifts

We prove the affine infinitesimal assertion needed for general formal frames. A finitely presented algebra is called smooth here when it lifts maps across every square-zero ideal; this is the algebraic smoothness convention established in [*Formally smooth, unramified and étale ring maps*](../../AG-CA/src/formally-smooth-unramified-and-etale-ring-maps.md), §§3–4. The following calculation proves the lifting and descent properties we use.

Write \(C=R[X_1,\ldots,X_q]/I\), with \(I\) finitely generated. Put \(J=I/I^2\), and define
\[
 \delta:J\longrightarrow C^q,\quad
 [f]\longmapsto(\partial f/\partial X_i)_i\bmod I,
 \qquad \Omega=\operatorname{coker}\delta.
 \tag{FD.12}
\]
The product rule makes this a well-defined \(C\)-linear map. The module \(\Omega\) represents derivations: values on the variables determine a polynomial derivation, and it factors through \(C\) exactly when it kills the displayed derivative relations.

The algebra \(C\) has the square-zero lifting property exactly when \(\delta\) has a \(C\)-linear left inverse. For the forward implication lift \(1_C\) to a section \(s:C\to R[X]/I^2\). The difference
\[
 D(p)=p-s(p\bmod I)\pmod{I^2}
 \tag{FD.13}
\]
is a derivation into \(J\): multiply two such differences and use \(J^2=0\). It restricts to the identity on \(I/I^2\). The universal polynomial derivative therefore factors it as a linear map \(C^q\to J\) whose composite with \(\delta\) is the identity. Conversely a left inverse \(r:C^q\to J\) defines the polynomial derivation \(D=r\,d\), and
\[
 p\longmapsto p-D(p)\pmod{I^2}
 \tag{FD.14}
\]
is an algebra map killing \(I\). It gives a section of the quotient onto \(C\). For any test map \(C\to A/K\), \(K^2=0\), lift the variable images arbitrarily to \(A\). The resulting polynomial map sends \(I\) into \(K\), so factors through \(R[X]/I^2\); composing it with that section is the desired lift. This proves both implications, rather than relying only on projectivity of differentials. A left inverse makes
\[
 0\longrightarrow J\xrightarrow{\delta}C^q
 \longrightarrow\Omega\longrightarrow0
 \quad\text{split exact}.
 \tag{FD.15}
\]
In particular \(J\) and \(\Omega\) are finite projective.

Suppose \(R\to B\) is faithfully flat and \(C_B\) is smooth over \(B\). Flatness identifies the relation ideal of the base-changed polynomial presentation with the extension of \(I\), and its square with the extension of \(I^2\). Polynomial differentiation commutes with the coefficient map, so its conormal map is
\[
 J\otimes_R B\xrightarrow{\delta\otimes1}(C\otimes_R B)^q.
 \tag{FD.16}
\]
The map \(C\to C\otimes_R B\) is faithfully flat. Equation (FD.15) upstairs makes (FD.16) injective with finite projective cokernel. Faithful flatness makes \(\delta\) injective, and (FD.6) makes its cokernel \(\Omega\) finite projective. Projectivity splits \(C^q\to\Omega\); the complementary projection onto \(J\) is a left inverse to \(\delta\). Equations (FD.13)–(FD.14) give every lift over \(R\). We have proved
\[
 C\text{ finitely presented over }R,
 \ C_B\text{ smooth over }B
 \quad\Longrightarrow\quad C\text{ smooth over }R.
 \tag{FD.17}
\]
If finite presentation is known only upstairs, its descent is the finite-generator and finite-relation argument in §7.3. Smoothness also survives any coefficient map: an algebra map out of \(C\otimes_R R'\) restricts to a map out of \(C\), whose lift extends by the prescribed \(R'\)-structure. Finite presentations base change by mapping the coefficients of the finite equations. Thus no flatness is required for this stability assertion.

Let \(G\) now be smooth affine over \(k\), with finitely presented \(H=k[G]\). Smoothness is part of the reductive-group hypotheses of this lesson. For its affine torsor \(P=\operatorname{Spec}C\) over \(R\), the faithful cover \(R\to C\) gives
\[
 C\otimes_R C\simeq C\otimes_k H.
 \tag{FD.18}
\]
The right side is smooth over \(C\) by base change. The algebra \(C\) is finitely presented over \(R\), by §7.3, so (FD.17) shows that \(P\) has the required affine lifting property over \(R\). This proves the smooth-torsor lifting assertion from its coordinate algebra, without importing smooth descent as an unproved theorem.

Take a torsor over \(R[[t]]\). Its reduction \(P_0=\operatorname{Spec}C_0\), \(C_0=C/tC\), is an fppf torsor over \(R\). Use the single coefficient cover \(R'=C_0\), faithfully flat and finitely presented over \(R\). The reduction has its diagonal section after this cover. Pull back the formal torsor along the actual ring map \(R[[t]]\to R'[[t]]\), and write \(C'\) for its coordinate algebra. This coefficient map need not be identified with ordinary tensor of the two power-series rings. The preceding base-change argument makes \(C'\) smooth over \(R'[[t]]\).

For \(n\geq1\), set \(A_n=R'[[t]]/(t^n)\). The exact sequence
\[
 0\longrightarrow(t^n)/(t^{n+1})\longrightarrow A_{n+1}
 \longrightarrow A_n\longrightarrow0
 \tag{FD.19}
\]
has square-zero kernel, since \(2n\geq n+1\). Starting with the diagonal section \(s_1:C'\to A_1=R'\), the lifting property constructs compatible algebra maps \(s_n:C'\to A_n\). At each step the diagram is
\[
 \begin{array}{ccc}
 C'&\xrightarrow{\ s_{n+1}\ }&A_{n+1}\\
 \Vert&&\downarrow\scriptstyle\text{reduction}\\
 C'&\xrightarrow{\ s_n\ }&A_n.
 \end{array}
 \tag{FD.20}
\]
*The vertical arrow on the right has exactly the square-zero kernel (FD.19). The new horizontal map exists by the split conormal calculation (FD.12)–(FD.18). Its reduction is the prescribed preceding section; each stage retains that compatibility.*

Compatible maps to the quotients define an algebra map to their inverse limit. Addition, multiplication and the structural map are checked in each quotient. Hence
\[
 s:C'\longrightarrow\varprojlim_n A_n=R'[[t]],
 \qquad P_{R'[[t]]}\simeq G_{R'[[t]]},\quad g\mapsto s\,g.
 \tag{FD.21}
\]
The second isomorphism follows by pulling the canonical torsor isomorphism (FD.9) back along its first point \(s\); its inverse supplies the unique \(g\) carrying \(s\) to any second point. This proves formal local triviality after an fppf cover of the coefficient scheme for every smooth affine \(G\), including arbitrary non-Noetherian and nonreduced coefficients.

### 7.7. The full formal-frame quotient and its exact limitation

Combine affineness descent in §7.5 with the formal-disc equivalence (BL.28), the open gluing in §7.4, and formal triviality (FD.21). Over the coefficient fppf site, torsors on the curve equipped with a punctured-curve frame are classified by
\[
 \operatorname{Gr}_{G,x}
 \simeq\bigl(R\mapsto G(R((t)))/G(R[[t]])\bigr)^{\mathrm{fppf}}.
 \tag{FD.22}
\]
The superscript means sheafification of the presheaf of right cosets. It does not require a global formal frame for each coefficient ring. Locally (FD.21) supplies that frame, the transition matrix gives a loop, and changing the formal frame gives the right multiplication of (BL.32)–(BL.34). Descent in §7.5 glues the corresponding framed torsors back over the original ring.

There are no automorphisms of a torsor preserving its punctured frame. Such an arrow is the identity on the punctured curve. After a coefficient cover giving a formal frame, its formal arrow is in \(G(R[[t]])\) and restricts to the identity in \(G(R((t)))\). That restriction is injective: for affine \(G\), equality of points is equality of all coordinate functions, and \(R[[t]]\to R((t))\) is injective by the nonzero-divisor calculation (BL.2). Thus the formal arrow is the identity, and gluing makes the global arrow the identity. Equality descends along the coefficient cover. This explains why (FD.22) is a sheaf of sets, although its unframed target is a stack.

For precision, let \(\tau_U,\tau_D\) be right-torsor frames. Their comparison \(\tau_U^{-1}\tau_D\) is left multiplication by \(g\). The frame conventions are
\[
 \tau_D\mapsto\tau_D\circ L_h:\ g\mapsto gh,
 \qquad
 \tau_U\mapsto\tau_U\circ L_{a^{-1}}:\ g\mapsto ag.
 \tag{FD.23}
\]
Here \(h\in G(R[[t]])\), \(a\in G(U_R)\), and \(L\) denotes left multiplication on the trivial right torsor. The first operation forgets a formal frame; the second forgets the punctured frame. With this convention, (BL.33), the degree sign (BL.35) and the infinitesimal example (BL.36) agree.

Consequently there is an equivalence of fppf stacks
\[
 [\,G(U)\backslash\operatorname{Gr}_{G,x}\,]
 \xrightarrow{\ \sim\ }
 \operatorname{Bun}_G^{\,U\text{-triv}},
 \tag{FD.24}
\]
where the target consists of bundles whose restriction to \(U_R\) becomes trivial after a coefficient fppf cover. This is proved on the cover where a punctured frame exists: its choices differ by precisely \(G(U_R)\), and all arrows are the corresponding changes of frames. The descent theorem then gives the equivalence over the original parameter. Stabilizers of the left action are retained, so the brackets denote a stack quotient. This is an equivalence onto that full substack, not an assertion that every bundle lies in it. Sections 7.8–7.9 prove that every semisimple bundle in characteristic zero lies in this substack and establish the stronger étale-local form. No generic torsor triviality or new global trivialization follows from (FD.24).

Smoothness in (FD.21) is necessary. To see the obstruction concretely, change fields for this example to \(k=\mathbf F_p\), with \(p\) prime, and take the non-smooth affine group \(\mu_p\). The algebra
\[
 C=k[[t]][z]/(z^p-(1+t))
 \tag{FD.25}
\]
is free of rank \(p\), with basis \(1,z,\ldots,z^{p-1}\): division by its monic equation gives a unique remainder. It is therefore faithfully flat and finitely presented. The element \(z\) is a unit. It is a \(\mu_p\)-torsor: in the twofold tensor product put \(w=z_2/z_1\), so \(w^p=1\). The substitutions \(z_2=z_1w\) and \(w=z_2/z_1\) give the canonical torsor isomorphism and its inverse. Its reduction has the section \(z=1\), but that section cannot lift to a formal section, even after a nonzero coefficient extension. In characteristic \(p\),
\
 \left(\sum_{n\geq0}a_nt^n\right)^p
   =\sum_{n\geq0}a_n^pt^{np},
 \qquad [t=1.
 \tag{FD.26}
\]
The coefficient of \(t\) on the left is zero, whereas on the right it is one. The identity follows in every finite power-series quotient by the binomial identity and then in the inverse limit, including over nonreduced coefficient rings. This example is outside the characteristic-zero reductive hypotheses; it shows exactly why affineness and finite presentation alone cannot replace smoothness in the formal-frame argument. Faithfulness is also essential in descent: \(\mathbf Z\to\mathbf Z[1/2]\) sends the nonzero module \(\mathbf Z/2\) to zero, so it cannot recover objects or detect their isomorphisms.

| Construction | Coefficients and hypotheses | What the proof supplies |
|---|---|---|
| Module and algebra descent | Every faithfully flat ring cover | Actual equalizer, all arrows, tensor compatibility and arbitrary base change, (FD.1)–(FD.7) |
| Affine torsor dictionary | Affine finitely presented \(G\); arbitrary base schemes | Affineness, effective fppf descent, coordinate coaction and canonical isomorphism, (FD.8)–(FD.9) |
| Vector-bundle dictionary | Finite projective rank \(n\), including nonreduced bases | Frame scheme and its inverse construction, (FD.10)–(FD.11) |
| Formal frame | Smooth affine \(G\); every ordinary coefficient algebra | A single coefficient fppf cover, successive compatible sections, (FD.12)–(FD.21) |
| Curve quotient | The smooth-curve neighbourhood of §7.4 | Right formal quotient and left punctured stack action, (FD.22)–(FD.24) |
| Family uniformization | Semisimple simply connected \(G\) | The full earlier family theorem is applied in §7.8; the whole-stack quotient is proved in §7.9 |

*The invariant-open square (FD.8), lift square (FD.20), and frame maps (FD.23) identify the objects, projections and actions used in the construction. The module, algebra and smoothness arguments are complete arbitrary-ring calculations. The passage to arbitrary fppf families uses the precisely linked earlier cover-refinement and constructible-image proofs above. For further reading, the freely accessible [Stacks project, descent for modules](https://stacks.math.columbia.edu/tag/023N), [descent of affine morphisms](https://stacks.math.columbia.edu/tag/0244), and [smoothness and infinitesimal lifting](https://stacks.math.columbia.edu/tag/00TN) give the corresponding classical statements. The proofs used here are (FD.1)–(FD.21), together with the specified earlier lessons.*

### 7.8. Uniformization over every coefficient algebra

We can now supply the off-point frame needed in (FD.24). The curve remains smooth, projective and connected over an algebraically closed field of characteristic zero. The point \(x\in X(k)\) is fixed throughout; the cover changes the parameter scheme, while the complement remains \(U=X-\{x\}\).

**Theorem 7.8 (one-point family uniformization).** Let \(G/k\) be connected semisimple, and let \(R\) be any commutative \(k\)-algebra. For every \(G\)-torsor \(P\) on \(X_R\), there is a faithfully flat étale \(R\)-algebra \(R'\), of finite presentation, and an isomorphism of right torsors
\[
 P|_{U_{R'}}\simeq G\times U_{R'}.
 \tag{UF.1}
\]
In particular the theorem applies to the original semisimple simply connected case. No Noetherian or reduced hypothesis on the parameter algebra is required.

**Proof.** The earlier programme lesson [*Beauville–Laszlo gluing and the moduli interpretation*](../../GL-SAT/src/GL-SAT-03.md), Theorem 5.3, proves this family statement, with its complete proof in §§6–7. Its hypotheses are a smooth projective connected curve over an algebraically closed field, a rational puncture and a connected semisimple constant group. They agree with the present hypotheses. Its cover is affine, faithfully flat and of finite presentation; it is étale when the length of the central kernel of the simply connected cover is invertible. That kernel has finite length, which is invertible in characteristic zero. Thus its affine cover gives precisely the algebra and frame in (UF.1).

Here are the exact proof dependencies of that theorem. They explain why its family conclusion supplies more than a trivialization at geometric parameter points.

* In §6, the Tsen and Tate-cohomology argument first proves that every torus over the curve function field has trivial first cohomology. The fundamental-weight trace calculation constructs a rational representative of a strongly regular semisimple conjugacy class. Twisting by a torsor and reducing its cocycle to the torus centralizer then proves generic torsor triviality for simply connected groups. The two smooth-kernel central extensions in §6.7 give the semisimple case. In particular, for every algebraically closed extension \(\Omega/k\),
  \[
   H^1(\Omega(X),G)=1.
   \tag{UF.2}
  \]
* Sections 7.3–7.4 extend a generic Borel reduction over the curve and modify its torus part at \(x\) until the root degrees are negative. The tangent bundle of the reduction has positive-degree successive quotients and zero first cohomology, so its reduction parameter scheme is smooth. The modification retains a specified isomorphism with the original torsor on \(U\).
* Sections 7.5–7.6 replace the formal loop by a finite jet, lift it over a strict henselization, glue the resulting algebraic torsor, and descend its finite-presentation torsor and reduction data to an affine étale neighbourhood. The infinite formal series is used to construct the modification; the algebraic torsor, its action, its isomorphism on \(U\) and its reduction are the data descended to that neighbourhood.
* The affine unipotent filtration reduces the modified bundle on \(U\) to its whole-curve torus bundle. Section 7.7 removes the simple-coroot factors by rank-two splitting. For a general semisimple group, §7.8 first normalizes degrees at \(x\) and uses a finite Jacobian division cover to lift the torus bundle to the simply connected torus. The division cover is étale in characteristic zero. Section 7.9 takes finitely many affine charts and their finite disjoint union, producing one affine cover of finite presentation.

The arbitrary-ring step is also part of that proof, in §§7.6 and 7.9. It gives a finitely generated \(k\)-subalgebra \(R_0\subset R\), a genuine smooth surjective torsor \(P_0\) on \(X_{R_0}\), and an identification \(P_0\times_{R_0}R\simeq P\). The action, torsor identity, smooth charts and surjectivity all have finite witnesses at this stage. Apply the Noetherian family construction to obtain its coefficient algebra \(B_0\), then use
\[
 \begin{gathered}
 R'=R\otimes_{R_0}B_0,\\
 \operatorname{Spec}B_0\longrightarrow\operatorname{Spec}R_0
     \text{ faithfully flat, étale, finitely presented},\\
 P|_{U_{R'}}\simeq
 (P_0|_{U_{B_0}})\times_{B_0}R'.
 \end{gathered}
 \tag{UF.3}
\]
Base change preserves the three properties of this cover and pulls back its frame. This proves the asserted conclusion for every \(R\), including nonreduced algebras. \(\square\)

Section 6 of the earlier gluing lesson proves (UF.2). For simply connected constant groups, [Heinloth, Theorem 4](https://arxiv.org/pdf/0711.4450v2) gives the statement for Noetherian parameter schemes. The finite-presentation passage in (UF.3) is why the conclusion here has the stated arbitrary-ring scope.

### 7.9. Étale formal frames and the full stack quotient

The formal-frame theorem (FD.21) can also use an étale coefficient cover. We prove that refinement before changing the topology in the quotient.

**Lemma 7.9.** Let \(R\) be a \(k\)-algebra and let \(Y\to\operatorname{Spec}R\) be smooth, surjective, affine and of finite presentation. There is an affine faithfully flat étale cover of finite presentation on which \(Y\) has a section.

**Proof.** Fix \(s\in\operatorname{Spec}R\) and a point of its nonempty smooth fibre. The local standard form in [*Formally smooth, unramified and étale ring maps*](../../AG-CA/src/formally-smooth-unramified-and-etale-ring-maps.md), Theorem 5.1, gives an affine neighbourhood \(V\subset Y\) and an étale coordinate map
\[
 V\longrightarrow\mathbf A_R^d.
 \tag{UF.4}
\]
Concretely, in the standard smooth equations leave the \(d\) coordinates outside the invertible Jacobian block free. Over their polynomial ring the remaining equations have square invertible Jacobian. The square-zero correction solves those equations uniquely, so this map is formally étale and finitely presented, hence étale. Étale maps are open by the earlier flat-image proof in §7.5.

The image of the nonempty fibre \(V_s\) is a nonempty open of affine space over \(\kappa(s)\). This field is infinite since it contains \(k\). A nonzero polynomial cannot vanish on every tuple over an infinite field: induction on the number of variables reduces this to the fact that a nonzero polynomial in one variable has at most its degree many roots. Thus that open has a \(\kappa(s)\)-rational point \(c\). Lift its finitely many coordinates to \(R_f\) for some \(f\notin s\). Pulling (UF.4) back along these coordinates gives
\[
 \begin{array}{ccc}
 T=V_{R_f}\times_{\mathbf A_{R_f}^d}\operatorname{Spec}R_f
   &\longrightarrow&V_{R_f}\\
 \downarrow&&\downarrow\\
 \operatorname{Spec}R_f&\xrightarrow{\ c\ }&\mathbf A_{R_f}^d.
 \end{array}
 \tag{UF.5}
\]
The left map is affine étale and finitely presented. Its fibre at \(s\) is nonempty, so its open image contains \(s\). The top map gives a \(Y\)-point over \(T\). Repeat at every \(s\); quasi-compactness of \(\operatorname{Spec}R\) selects finitely many such open images. Their corresponding finite disjoint union is affine, étale, finitely presented and surjective over \(R\). It is therefore faithfully flat, and the finitely many \(Y\)-points form its section. The empty base has the identity cover. \(\square\)

Apply the lemma to the special fibre of a formal-disc torsor under smooth affine \(G\). After the resulting étale coefficient cover it has a section modulo \(t\). The square-zero lifting and inverse-limit argument (FD.19)–(FD.21) then gives a section on the actual power-series ring:
\[
 \begin{gathered}
 R\longrightarrow B\quad\text{faithfully flat étale of finite presentation},\\
 P_{B[[t]]}\simeq G_{B[[t]]}.
 \end{gathered}
 \tag{UF.6}
\]
As in §7.6, this construction uses \(B[[t]]\) and its successive quotients directly.

Let \(A_x\) denote the group functor of punctured-curve frames, and let \(L_xG\) and \(L_x^+G\) denote the loop and positive-loop functors. For a coefficient algebra \(R\),
\[
 \begin{gathered}
 A_x(R)=G(U_R),\qquad
 L_xG(R)=G(R((t))),\qquad
 L_x^+G(R)=G(R[[t]]),\\
 \operatorname{Gr}_{G,x}
    =\bigl(L_xG/L_x^+G\bigr)_{\mathrm{\acute et}}
    =\bigl(L_xG/L_x^+G\bigr)_{\mathrm{fppf}}.
 \end{gathered}
 \tag{UF.7}
\]
The last equalities are equalities of the corresponding sheaves. Indeed, §§7.3–7.7 identify the fppf sheaf with bundles carrying a frame on \(U_R\); these framed bundles have no nonidentity automorphisms. By (UF.6), every such object has a formal frame étale locally on the coefficient scheme, and then comes from an actual loop. Two loops determine isomorphic framed objects exactly when they differ by a right positive loop. Thus the étale sheafification has the same objects and identifications as the fppf sheafification.

**Theorem 7.10 (the bundle-stack quotient).** Under the semisimple characteristic-zero hypotheses of Theorem 7.8, there are natural equivalences
\[
 \begin{gathered}
 \left[\,A_x\backslash\operatorname{Gr}_{G,x}\,\right]_{\mathrm{\acute et}}
       \simeq\operatorname{Bun}_G,\\
 \left[\,A_x\backslash\operatorname{Gr}_{G,x}\,\right]_{\mathrm{fppf}}
       \simeq\operatorname{Bun}_G.
 \end{gathered}
 \tag{UF.8}
\]
Here the brackets mean stackification of the action groupoid in the indicated topology. They retain the stabilizers of the left action.

**Proof.** Theorem 7.8 gives every bundle a frame on \(U\) étale locally over its parameter scheme. With that frame it is an object of the Grassmannian sheaf by (UF.6)–(UF.7). The gluing map is therefore locally essentially surjective. For full faithfulness, work on a common coefficient cover with punctured and formal frames. Changing those frames has exactly the actions (FD.23). In loop representatives an isomorphism is expressed as
\[
 g'=a g h,\qquad
 a\in G(U_R),\quad h\in G(R[[t]]).
 \tag{UF.9}
\]
The right factor is forgotten in the Grassmannian sheaf; the left factor is an arrow of its action groupoid. Gluing preserves every torsor arrow by (BL.28), and effective descent in §7.5 glues the arrows on overlapping coefficient charts. Consequently the local equivalence of groupoids descends over every parameter scheme. This proves the étale equivalence. Since étale covers are fppf covers, (FD.24) and Theorem 7.8 also prove the fppf equivalence. \(\square\)

For a bundle represented by an actual loop \(g\), its automorphisms are the actual intersection
\[
 \operatorname{Aut}(P_g)
   \simeq A_x\cap gL_x^+Gg^{-1}\ \subset L_xG.
 \tag{UF.10}
\]
This is a group functor on coefficient extensions. An element of the intersection gives agreeing automorphisms on \(U\) and the disc, hence a unique global automorphism by gluing; the restriction of a global automorphism gives the converse. Thus replacing the stack quotient in (UF.8) by its set of orbits would discard the automorphisms used in the dimension calculations of §§2 and 6.

### 7.10. Rank-two examples and the determinant boundary

For \(SL_n\), the required off-point cover can be chosen Zariski. Theorem 5.2 of [*Beauville–Laszlo gluing and the moduli interpretation*](../../GL-SAT/src/GL-SAT-03.md) proves for any rank-\(n\) bundle on the whole curve, with arbitrary coefficient base, that Zariski locally on that base
\[
 E|_{U_R}\simeq
 \mathcal O_{U_R}^{\,n-1}\oplus\det(E)|_{U_R}.
 \tag{UF.11}
\]
Its proof chooses a nowhere-vanishing section after a sufficiently large twist at \(x\), keeps that section nonvanishing over a parameter neighbourhood by properness, and splits its quotient extension on the affine complement. Induction leaves exactly the determinant summand. A prescribed determinant trivialization makes (UF.11) a frame; multiplying its first vector by the correcting unit makes it respect that trivialization. This proves the \(SL_n\) assertion, including \(n=1\). For \(GL_n\), a chosen trivialization of the determinant on \(U_R\) is sufficient for the same conclusion; taking determinants shows it is also necessary.

For example, let \(M\) be any line bundle on \(X_R\), and give the rank-two bundle
\[
 E=M\oplus M^{-1},\qquad
 \det(E)\simeq\mathcal O_{X_R}
 \tag{UF.12}
\]
its displayed orientation. Although either line may be nontrivial on \(U_R\), the oriented rank-two bundle is trivial there Zariski locally on the coefficient base, by (UF.11). This is the simple-coroot mechanism in the semisimple proof: the two lines are removed together inside a rank-one Levi.

One can also see the Jacobian division step in a \(PGL_2\) example. Suppose \(E\) is a rank-two bundle on \(X_R\). Restrict to a degree locus, put \(d=\deg\det E\), and normalize
\[
 D=\det E,\qquad D_0=D(-dx),\qquad
 N=x^*D_0,\qquad
 \widetilde D=D_0\otimes p_R^*N^{-1}.
 \tag{UF.13}
\]
The line \(\widetilde D\) has degree zero and its canonical rigidification at \(x\). It therefore gives a map to the Jacobian \(J\). Section 7.8 of the earlier gluing lesson proves that multiplication by two on \(J\) is finite faithfully flat and étale in characteristic zero. Its base change gives an étale cover of the coefficient scheme and an actual rigidified line \(M\) with \(M^{\otimes2}\simeq\widetilde D\). Trivialize the base line \(N\) on a Zariski refinement. Then
\[
 \det(E\otimes M^{-1})\simeq\mathcal O_{X_R}(dx),
 \qquad
 \mathbf P(E\otimes M^{-1})\simeq\mathbf P(E).
 \tag{UF.14}
\]
Here the formulas are written after those coefficient changes. The determinant in (UF.14) is canonically trivial on \(U_R\), so (UF.11) gives a frame there. Its projectivization trivializes the associated \(PGL_2\)-torsor on \(U_R\). This example starts with an actual vector bundle; Theorem 7.8 covers all \(PGL_2\)-torsors through its full reduction and modification argument.

The torus obstruction in §7 remains. A nontrivial degree-zero line on a positive-genus curve is absent from the one-point lattice description. In particular the full quotient (UF.8) is justified for semisimple \(G\); for a general smooth affine group, (FD.24) describes the substack with coefficient-locally trivial restriction to \(U\).

| Group and bundle | Off-point frame over the coefficient base | Proof |
|---|---|---|
| \(SL_n\), with its orientation | Zariski locally | Rank splitting and determinant adjustment, (UF.11) |
| Connected semisimple \(G\) in characteristic zero | Étale locally | Theorem 7.8 and the earlier full family proof |
| \(GL_n\), with a trivial determinant on \(U\) | Zariski locally | (UF.11), with the chosen determinant frame |
| \(\mathbf G_m\) on a positive-genus curve | Not every bundle has a frame on \(U\) | The divisor and degree calculation in §7 |

*The square (UF.5) is the base change that supplies an étale section. Equations (UF.3), (UF.6) and (UF.8) distinguish the coefficient cover, formal frame and bundle-stack quotient; (UF.10) records its stabilizers. The field and family proofs used in Theorem 7.8 are the complete earlier programme proofs at the specified locators.*

## 8. Exercises

**Exercise 8.1 (easy).** Derive \(\dim\operatorname{Bun}_n=n^2(g-1)\) directly from \(\operatorname{End}(E)\). For \(E=\mathcal O\oplus\mathcal O(3)\) on \(\mathbb P^1\), compute \(h^0(\operatorname{End}E)\) and \(h^1(\operatorname{End}E)\), and check the difference.

**Exercise 8.2 (easy).** Compute \(\operatorname{Aut}(\mathcal O\oplus\mathcal O(d))\) for all integers \(d\). Explain why \(\mathcal O(m)\oplus\mathcal O(-m)\) proves nonquasicompactness of the degree-zero rank-two stack.

**Exercise 8.3 (medium).** Compute the \(GL_2\) Hitchin-base dimension in all genera. For \(g\ge2\), reconcile it with the bundle-stack dimension and with the stable coarse moduli dimension.

**Exercise 8.4 (medium).** Give a connected-family proof that every degree-\(d\) rank-\(n\) bundle lies in the component of \(\mathcal O(dx)\oplus\mathcal O^{n-1}\). Specify how extensions are split in a family and how a unit of degree is transferred between two summands.

**Exercise 8.5 (hard).** Let \(g=2\) and consider \(SL_2\)-bundles. Compute the stack dimension of the space of reductions with a saturated line subbundle \(L\) of degree \(e\ge0\). Prove that the non-stable locus has codimension exactly one, whereas the non-semistable locus has codimension at least three. Identify where an estimate valid away from the genus-two \(A_1\) case fails.

## 9. Solutions

**Solution 8.1.** The bundle \(\operatorname{End}(E)\) has rank \(n^2\) and degree zero. Riemann–Roch gives \(h^1-h^0=n^2(g-1)\), the dimension of deformations minus infinitesimal automorphisms. For the particular bundle,

\[
\operatorname{End}(E)\simeq
\mathcal O^{\oplus2}\oplus\mathcal O(3)\oplus\mathcal O(-3).
\]

On \(\mathbb P^1\), \(h^0(\mathcal O(3))=4\), \(h^0(\mathcal O(-3))=0\), and \(h^1(\mathcal O(-3))=2\). Thus \(h^0=6\), \(h^1=2\), and \(h^1-h^0=-4=2^2(0-1)\). A large stabilizer is compatible with the same stack dimension as every other rank-two bundle.

**Solution 8.2.** For \(d>0\) the group is the triangular group displayed in section 4, with two nonzero diagonal constants and \(d+1\) lower off-diagonal parameters. Its dimension is \(d+3\). For \(d<0\) it is the analogous upper triangular group, of dimension \(-d+3\). For \(d=0\) it is \(GL_2\), of dimension four; the off-diagonal entries in both directions are allowed. Tensoring \(\mathcal O\oplus\mathcal O(2m)\) by \(\mathcal O(-m)\) preserves its automorphism group, so the degree-zero example has stabilizer dimension \(2m+3\). A finite type inertia morphism on finitely many finite type charts cannot have unbounded fibre dimensions. This is the required contradiction to quasicompactness.

**Solution 8.3.** The base is \(H^0(\omega_X)\oplus H^0(\omega_X^2)\). For \(g\ge2\), the two dimensions are \(g\) and \(3g-3\), so the sum is \(4g-3\). For \(g=1\), both line bundles are trivial and the sum is two. For \(g=0\), both have negative degree and the sum is zero. The bundle stack has dimension \(4g-4\) in every genus. On its stable locus, when nonempty, scalar automorphisms have dimension one, so the coarse stable moduli dimension is \(4g-3\).

For completeness, let \(f\ne0\) be an endomorphism of a stable bundle. If its image has smaller positive rank, stability applied to its kernel makes the image quotient have slope greater than \(\mu(E)\); stability applied to the saturation of its image makes its slope smaller than \(\mu(E)\). This is impossible. Thus \(f\) has full rank; its torsion cokernel has degree zero, since source and target have equal degree, so \(f\) is an isomorphism. For any endomorphism \(u\), choose an eigenvalue \(a\in k\) at one fibre. The determinant of \(u-a\) is a constant function on \(X\) and vanishes at that fibre. It is therefore zero, so \(u-a\) cannot be invertible and must be zero. This proves the scalar assertion. The scalar stabilizer accounts for the one-dimensional difference. The low-genus base values show why the formula \(4g-3\) must not be used there.

**Solution 8.4.** Saturate a generic line to obtain \(0\to L\to E\to Q\to0\). Multiply its extension cocycle by \(t\in\mathbb A^1\) to connect \(E\) with \(L\oplus Q\); induct on \(\operatorname{rk}Q\). Given two resulting line summands \(L,M\), vary the quotient of \(L\oplus M(x)\) at \(x\) over \(\mathbb P^1\). Its universal kernels connect \(L\oplus M\) to \(L(-x)\oplus M(x)\). Reverse this path when needed and repeat to get degree list \((d,0,\ldots,0)\). Connectedness of each Picard degree component, proved using the surjective Abel map, then varies those summands to \(\mathcal O(dx),\mathcal O,\ldots,\mathcal O\). Every family has constant total degree. Conversely, degree is locally constant and every degree occurs, so these are exactly the components.

**Solution 8.5.** An \(SL_2\)-bundle is a rank-two bundle together with a chosen determinant trivialization. A Borel reduction is a line subbundle \(L\subset E\), with quotient canonically \(L^{-1}\). The extension data lie in \(H^1(X,L^2)\), and automorphisms inducing the identity on the two graded terms lie in \(H^0(X,L^2)\). The base of line bundles of degree \(e\) is the Picard stack, of dimension \(g-1=1\). Hence the reduction stack has dimension

\[
1+h^1(L^2)-h^0(L^2)
=1-\chi(L^2)=2-2e.
\]

This remains valid when the individual cohomology dimensions jump: their difference is fixed by Riemann–Roch. A bundle is non-stable precisely when it has such a line with \(e\ge0\). Since \(\dim\operatorname{Bun}_{SL_2}=3\), each of these images has dimension at most two. Locally on a finite type chart only finitely many degrees of subbundles above zero can occur, by boundedness of the family. Thus their union has dimension at most two there. For non-semistability \(e\ge1\), the dimension is at most zero, giving codimension at least three.

To show the dimension-two bound for the non-stable locus is attained, choose \(L\in\operatorname{Pic}^0(X)\) with \(L^2\not\simeq\mathcal O_X\) and choose a nonsplit extension \(0\to L\to E\to L^{-1}\to0\). Such extensions exist: \(h^0(L^2)=0\) and Riemann–Roch gives \(h^1(L^2)=1\). Both line terms are semistable of degree zero, so their extension is semistable. If \(M\subset E\) is another degree-zero line subbundle, its map to \(L^{-1}\) is either zero or an isomorphism. In the first case it equals \(L\); in the second it splits the extension, which is impossible. The degree-zero reduction is therefore unique. Its infinitesimal deformations with fixed \(E\) are \(H^0(\operatorname{Hom}(L,L^{-1}))=H^0(L^{-2})=0\). The forgetful morphism from this open part of the reduction stack has zero-dimensional fibres and therefore a dimension-two image. The full non-stable locus has dimension two and codimension one.

For comparison, a Borel reduction in genus \(g\) has dimension \(2(g-1)-2e\), so the codimension bound is \(g-1+2e\). At \(g=2,e=0\), it equals one. This is the exceptional case in [Gaitsgory–Raskin, §7.2, proof of the estimate for the complement of the stable locus]. Their term “unstable” there means “not stable,” including these strictly semistable bundles. Replacing it by “not semistable” would erase the exception.

## What this lesson does not prove

Sections 1.1–1.6 prove algebraicity, the affine diagonal and formal effectivity of the torsor stack. We still use the general component theorem [Drinfeld–Gaitsgory, §7.2.4]; and the background Harder–Narasimhan, openness and fixed-component boundedness theorems [Drinfeld–Gaitsgory, Theorem 7.4.3, §7.3.2 and Proposition 7.3.5]. [Gaitsgory–Raskin, §9.1] supplies the stability convention. We use Riemann–Roch, Serre duality, the Picard scheme, and proper flat constancy of Euler characteristic from algebraic geometry. The smoothness, dimension, vector-bundle connectedness, cotangent identification, examples and exercise calculations are proved here.

The nilpotent-cone Lagrangian proof is written in §6, relative to its exact stack and recursive programme foundations. Beilinson–Drinfeld, Theorem 2.10.4, and Ginzburg, Main Theorem, are references for the geometric statement. Sections 7.1–7.7 prove module, vector-bundle and affine Hopf-torsor gluing, effective faithfully flat descent, affineness and the vector-bundle dictionary, and smooth-group formal local triviality, including arbitrary coefficient changes. The smooth-curve neighbourhood retains its stated curve foundations. The arbitrary-cover reduction uses the precise earlier scheme-topological proofs linked in §7.5. Sections 7.8–7.10 apply the full earlier semisimple family-uniformization proof and prove the coefficient-étale formal frames and whole-stack quotient, with their determinant and torus boundaries. The smooth spectral-curve correspondence is mentioned only to explain the dimensions; its construction is not proved here. Neither the categorical Langlands theorem nor a theorem about spectral singular support follows from these bundle calculations alone.

## References

- [Beauville–Laszlo] A. Beauville and Y. Laszlo, *Un lemme de descente*. [Freely accessible author version](https://math.univ-cotedazur.fr/~beauvill/pubs/descente.pdf), §§2–4. The full algebraic gluing proof used in this lesson is §§7.1–7.3, (BL.1)–(BL.28).

- [Beilinson–Drinfeld] A. Beilinson and V. Drinfeld, *Quantization of Hitchin's integrable system and Hecke eigensheaves*. [Author's preprint](https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf). Sections 2.1.1, 2.2.3, 2.3.4–2.3.5, and 2.10.2–2.10.4.
- [Gaitsgory–Raskin] D. Gaitsgory and S. Raskin, *Proof of the geometric Langlands conjecture V: the multiplicity one theorem*. [Open preprint](https://arxiv.org/abs/2409.09856). Section 7.2, proof of the complement estimate, and §9.1, stability convention. Section references follow the version with these section titles.
- [Heinloth] J. Heinloth, *Uniformization of \(\mathcal G\)-bundles*. [Open preprint, version 2](https://arxiv.org/abs/0711.4450v2). Proposition 1 and Theorems 2 and 4.
- [Ginzburg] V. Ginzburg, *The global nilpotent variety is Lagrangian*. [Open preprint, version 6](https://arxiv.org/abs/alg-geom/9704005v6). Main Theorem and footnote 1.
- [Drinfeld–Gaitsgory] V. Drinfeld and D. Gaitsgory, *Compact generation of the category of D-modules on the stack of G-bundles on a curve*. [Open preprint, version 8](https://arxiv.org/abs/1112.2402v8). Sections 7.2.4 and 7.3.2, Proposition 7.3.5 and Theorem 7.4.3.
- [Stacks] The [Stacks project](https://stacks.math.columbia.edu/) is freely accessible. The curve cohomology, Picard, descent and representability results used above retain their stated proof hypotheses and unresolved foundations; the cited reference does not replace those proofs.


Section 6 contains the Lie/parabolic isotropy and all-genus component-dimension arguments for the reduced global nilpotent cone. The central equation count, genus-zero orbit-conormal argument and algebraic elliptic tensor/parabolic source construction retain automorphisms and prove each component bound. Sections 1.1–1.6 prove the connected reductive bundle-stack atlas, affine diagonal and complete Noetherian local formal effectivity. The remaining recursive local-algebra, cohomology, Quot, Picard and flag foundations retain their stated boundaries. Sections 7.1–7.7 prove formal-disc gluing, arbitrary-ring faithful descent, torsor affineness, the vector-bundle dictionary, smooth-group formal local triviality and the exact framed/unframed quotient descriptions. Sections 7.8–7.10 now apply the full earlier generic-triviality and modification/family proof, establish the arbitrary-ring étale-local conclusion and derive the full semisimple bundle-stack quotient. Sections 2.1–2.6 prove the square-zero deformation groupoid, smoothness, the adjoint determinant and the all-genus bundle-stack dimension. The remaining recursive Lie/flag and local-algebra foundations stay open. These are active obligations within the original connected reductive and semisimple simply connected scopes.
