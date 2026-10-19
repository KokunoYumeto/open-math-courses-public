# Ext sheaves and Serre duality on projective space

*Written by GPT-6.1 Sol (OpenAI), in Codex, at Ultra effort, October 2026. Self-checked by the writing AI, GPT-6.1 Sol, at Ultra effort. Public domain (CC0).*

A section of a line bundle can pair with a top cohomology class of its inverse twist. On projective space this pairing extracts one Laurent coefficient. Serre duality extends that concrete calculation to every coherent sheaf, including sheaves with torsion. The extension requires Ext: the ordinary dual sheaf of a torsion sheaf can be zero even when the sheaf has nonzero cohomology.

We use enough injectives, their restriction to open subsets, and derived functors from the existing earlier *Injective modules and bounded-below derived functors*, Theorem 2.3, Lemma 1.1, Proposition 1.3 and Theorem 4.1. The preceding lessons provide [projective-space cohomology](cohomology-of-projective-space.md), [Serre generation and vanishing](serres-theorems-on-projective-schemes.md), and [proper finiteness](proper-morphisms-and-coherent-direct-images.md). No finite resolution by sums of line bundles is presumed. All complexes have cohomological grading.

## 1. Two meanings of Ext

For a ringed space \(X\) and two \(\mathcal O_X\)-modules, choose an injective resolution \(G\to I^\bullet\). Define
\[
\operatorname{Ext}^i_X(F,G)
 =H^i\operatorname{Hom}_{\mathcal O_X}(F,I^\bullet),
\qquad
\mathcal E xt^i_X(F,G)
 =\mathcal H^i\mathcal H om_{\mathcal O_X}(F,I^\bullet).
\]
The first is a group, or a vector space over a field. The second is a sheaf. They are respectively the cohomology of global derived Hom and of internal derived Hom. Equivalently, global Ext is \(\operatorname{Hom}_{D(\mathcal O_X)}(F,G[i])\). Negative Ext vanishes when both inputs are sheaves in degree zero.

Injectivity gives an exact contravariant functor \(\operatorname{Hom}(-,I)\). Internal \(\mathcal H om(-,I)\) is also exact: restrict to any open subset, where \(I\) is still injective, and take the resulting Hom groups. Thus a short exact sequence in the first argument produces the usual contravariant long exact Ext sequences, both globally and as sheaves.

**Proposition 1.1 (local computation).** Let \(X\) be Noetherian and let \(F,G\) be coherent. Every \(\mathcal E xt^i_X(F,G)\) is coherent, and
\[
(\mathcal E xt^i_X(F,G))_x
 \cong \operatorname{Ext}^i_{\mathcal O_{X,x}}(F_x,G_x).
\tag{1}
\]
On an open set where \(F\) has a resolution by finite locally free sheaves, sheaf Ext is the cohomology of the Hom complex of that resolution. The resolution may extend indefinitely to the left.

**Proof.** On \(U=\operatorname{Spec}A\), write \(F=\widetilde M\) and \(G=\widetilde N\). Successively surject finite free modules onto \(M\) and onto its kernels. Noetherianity makes each kernel finite, giving
\[
\cdots\longrightarrow P^{-2}\longrightarrow P^{-1}
 \longrightarrow P^0\longrightarrow M\longrightarrow0
\]
with every \(P^{-j}\) finite free. Sheafification is exact. Compare \(\mathcal H om(\widetilde P^\bullet,G)\) with the injective definition by the double complex
\(\mathcal H om(\widetilde P^{-a},I^b)\), \(a,b\geq0\). Each diagonal contains finitely many terms. In the resolution direction, exactness of internal Hom into an injective leaves only \(\mathcal H om(F,I^\bullet)\). In the other direction, internal Hom from a finite locally free sheaf is exact, leaving \(\mathcal H om(\widetilde P^\bullet,G)\). The two first-quadrant comparisons identify their cohomology.

Its terms are sheafifications of the finite modules \(\operatorname{Hom}_A(P^{-a},N)\), so their kernels and quotients are finite. This proves coherence locally. Localization commutes with these Hom modules because the source is finite free, and commutes with cohomology because it is exact. The localized resolution computes the module Ext at every prime. These identifications are the canonical restriction identifications, hence glue to (1). \(\square\)

The finiteness of the first input matters in this stalk statement: arbitrary Hom need not commute with localization. Conversely, local finite free resolutions suffice for sheaf Ext; a scheme need not have enough globally defined vector bundles for this proposition.

**Proposition 1.2 (a vector bundle in the first input).** For finite locally free \(E\), there are natural isomorphisms
\[
\mathcal E xt^i(E\otimes F,G)
 \cong\mathcal E xt^i(F,E^\vee\otimes G).
\tag{2}
\]
The analogous global Ext isomorphism also holds. In particular
\[
\mathcal E xt^{i}(E,G)=0\quad(i>0),
\qquad
\operatorname{Ext}^i_X(E,G)
 =H^i(X,E^\vee\otimes G).
\tag{3}
\]

**Proof.** The underived tensor-Hom identification is obtained on a trivializing open set by finite direct sums, and therefore glues. Tensoring by \(E\) is exact. Its right adjoint \(E^\vee\otimes-\) consequently takes injectives to injectives: Hom into that functor is Hom from the exact functor \(E\otimes-\). Apply the underived identification to an injective resolution of \(G\). This proves both forms of (2). Setting \(F=\mathcal O_X\), internal Hom becomes the identity functor and global Hom becomes global sections. Their derived functors give (3). \(\square\)

Formula (3) illustrates the distinction. A vector bundle has zero positive sheaf Ext, but its global Ext can be nonzero because global sections are not exact.

## 2. From local Ext to global Ext

**Proposition 2.1.** For sheaves \(F,G\) there is a natural first-quadrant spectral sequence
\[
H^p(X,\mathcal E xt^q_X(F,G))
 \ \Longrightarrow\ \operatorname{Ext}^{p+q}_X(F,G).
\tag{4}
\]

**Proof.** First, \(\mathcal H om(F,I)\) is flasque for injective \(I\). Given \(U\subset V\) open, a morphism \(F|_U\to I|_U\) is a morphism \(j_!(F|_U)\to I|_V\), where \(j:U\hookrightarrow V\). Extension by zero is exact for sheaves of modules, as its stalks are either the given stalk or zero, and there is a stalkwise injection \(j_!(F|_U)\hookrightarrow F|_V\). Injectivity extends the morphism to \(F|_V\). Thus restrictions of Hom sections are surjective.

Apply the hypercohomology spectral sequence to the bounded-below complex \(C^\bullet=\mathcal H om(F,I^\bullet)\). Its terms are flasque, hence acyclic for global sections, so its hypercohomology is \(H^*\Gamma(C^\bullet)=\operatorname{Ext}^*_X(F,G)\). The cohomology-sheaf spectral sequence has precisely the displayed second page. One constructs it with a flasque double resolution; first-quadrant filtrations have finitely many terms in each total degree, so convergence is ordinary convergence in those degrees. This proves (4). \(\square\)

For example, if only \(\mathcal E xt^c(F,G)\) is nonzero, (4) gives
\[
\operatorname{Ext}^{c+p}_X(F,G)
 \cong H^p(X,\mathcal E xt^c_X(F,G)).
\tag{5}
\]
This degeneration will be useful for hypersurfaces. The general spectral sequence also explains why simply taking global sections of a local Ext calculation misses higher cohomology.

## 3. The canonical twist and its trace

Put \(P=\mathbf P^n_k\) for a field \(k\), and define
\[
\omega_P=\mathcal O_P(-n-1).
\]
Its identification with the determinant of the differentials is proved in Exercise 7.4. The cohomological normalization uses the ordered standard affine cover
\(D_+(T_0),\ldots,D_+(T_n)\), with alternating Čech differential. For \(n\geq1\), the projective-space calculation gives
\[
H^n(P,\omega_P)=k\cdot\left[\frac1{T_0\cdots T_n}\right].
\]
Define the trace \(\operatorname{tr}:H^n(P,\omega_P)\to k\) by sending that class to one. For \(n=0\), \(P\) is a point; the same expression is the generator of the degree \(-1\) part of \(k[T_0,T_0^{-1}]\), so this convention still identifies its one-dimensional space of sections with \(k\).

Multiplication followed by this trace pairs
\[
H^0(P,\mathcal O(d))\ \times\
H^n(P,\mathcal O(-d-n-1))\longrightarrow k.
\tag{6}
\]
For \(n\geq1\) and \(d\geq0\), the first basis consists of \(T^b\), where \(b_i\geq0\) and \(\sum b_i=d\). The matching top-cohomology basis consists of
\(T_0^{-b_0-1}\cdots T_n^{-b_n-1}\). Their products have trace one precisely for matching exponent vectors, and zero otherwise. For \(d<0\), both spaces in (6) vanish. Thus (6) is perfect for every \(d\). When \(n=0\), both spaces are one-dimensional for every twist, and multiplication has the same conclusion. Negative twists on a point do not vanish.

More generally, projective-space cohomology and this coefficient computation give perfect pairings
\[
H^j(P,\mathcal O(d))\ \times\
H^{n-j}(P,\mathcal O(-d-n-1))\longrightarrow k
\]
for all \(j\): intermediate groups vanish and the two end cases are the computed pairing and its transpose. Maps between direct sums of twists are matrices of homogeneous polynomials. Multiplication is associative, so these pairings commute with all such matrices, including matrices between different twists. This naturality is the part needed to pass from twists to arbitrary coherent sheaves.

## 4. Duality in degree zero

For any coherent \(F\), a morphism \(u:F\to\omega_P\) induces a functional on its top cohomology:
\[
\theta_F^0(u)=\operatorname{tr}\circ H^n(u).
\tag{7}
\]
This construction is contravariantly natural in \(F\).

**Theorem 4.1.** The map (7) is an isomorphism
\[
\operatorname{Hom}_P(F,\omega_P)
 \ \cong\ H^n(P,F)^\vee
\]
for every coherent \(F\).

**Proof.** Choose a surjection \(P_0\twoheadrightarrow F\) with \(P_0\) a finite sum of twists, by Serre generation. Its coherent kernel \(K\) is likewise a quotient of a finite sum of twists \(P_1\). Thus
\(P_1\to P_0\to F\to0\) is a presentation. Hom into \(\omega_P\) gives
\[
0\to\operatorname{Hom}(F,\omega_P)
 \to\operatorname{Hom}(P_0,\omega_P)
 \to\operatorname{Hom}(P_1,\omega_P).
\]
The standard cover has \(n+1\) affine opens with affine intersections. Consequently cohomology of quasi-coherent sheaves vanishes above \(n\). The two short exact sequences defining this presentation therefore give
\[
H^n(P,P_1)\to H^n(P,P_0)\to H^n(P,F)\to0.
\]
Dualizing gives another left-exact sequence in the same direction as the Hom sequence. All spaces are finite-dimensional, by proper finiteness. The maps \(\theta^0\) give a morphism of these sequences. The two maps for \(P_0,P_1\) are isomorphisms by (6), and commute with the presentation map by its polynomial-matrix description. Their kernels are therefore isomorphic, which proves the assertion. \(\square\)

Only two stages of a presentation were used. In particular, this argument does not claim that repeated coherent kernels eventually become sums of line bundles.

## 5. Serre duality in every degree

**Theorem 5.1 (Serre duality on projective space).** For every coherent sheaf \(F\) and every integer \(i\), there are natural isomorphisms
\[
\operatorname{Ext}^i_P(F,\omega_P)
 \ \cong\ H^{n-i}(P,F)^\vee.
\tag{8}
\]
They extend (7), using its fixed trace.

**Proof.** For \(i\geq0\), consider the contravariant cohomological sequences
\[
A^i(F)=\operatorname{Ext}^i_P(F,\omega_P),
\qquad B^i(F)=H^{n-i}(P,F)^\vee.
\]
Exactness of vector-space duality and vanishing above \(n\) make the second a contravariant delta functor starting in degree zero, just as Ext is. Choose \(q>0\) sufficiently large so that \(F(q)\) is generated by its sections and all positive cohomology of \(\omega_P(q)\) vanishes. There is an epimorphism
\[
Q=\mathcal O_P(-q)^{\oplus m}\twoheadrightarrow F
\]
with coherent kernel \(K\). Formula (3) and Serre vanishing give \(A^j(Q)=0\) for every \(j>0\). The twist calculation gives \(B^j(Q)=0\) for every \(j>0\): if \(0\leq n-j<n\), the corresponding cohomology of a strictly negative twist vanishes, and if \(n-j<0\) it vanishes by convention. This also covers \(n=0\), where every positive \(B^j\) is zero.

Both long exact sequences consequently identify their degree-one value on \(F\) with the cokernel of their degree-zero map from \(Q\) to \(K\). Theorem 4.1 identifies these cokernels. For \(i\geq2\), the sequences give
\[
A^i(F)\cong A^{i-1}(K),
\qquad B^i(F)\cong B^{i-1}(K).
\]
Induction gives the desired isomorphisms for every \(i\geq0\).

These isomorphisms are canonical. The epimorphisms just used efface all positive values of both delta functors. The usual uniqueness argument for effaceable delta functors applies: a morphism in degree zero determines the cokernel map in degree one and then every dimension-shifted map. For two choices of epimorphism, take their fiber product over \(F\), which is coherent, and an epimorphism from sufficiently negative twists onto that fiber product. The resulting maps of short exact sequences compare both choices. The same construction over a morphism of coherent sheaves proves naturality, and compatibility with connecting maps follows from the exact sequences. Thus the induction is the unique extension of (7).

If \(i<0\), the left side vanishes, and the right side is cohomology above dimension \(n\), hence also zero. This proves (8) for all integers. \(\square\)

The pairing may also be written as Yoneda composition:
\[
\operatorname{Ext}^i(F,\omega_P)\times
\operatorname{Ext}^{n-i}(\mathcal O_P,F)
 \longrightarrow\operatorname{Ext}^{n}(\mathcal O_P,\omega_P)
 \xrightarrow{\operatorname{tr}}k.
\]
In derived notation the composition of \(\beta:\mathcal O_P\to F[n-i]\) with \(\alpha[n-i]:F[n-i]\to\omega_P[n]\) has that target. With the usual connecting-map conventions it is the delta-functor extension above. This description relates the abstract Ext classes directly to the Laurent-coefficient trace.

**Corollary 5.2 (vector-bundle form).** If \(E\) is finite locally free, then
\[
H^i(P,E)\cong H^{n-i}(P,E^\vee\otimes\omega_P)^\vee.
\tag{9}
\]

**Proof.** Apply (8) with Ext degree \(n-i\), then use (3) and finite-dimensional biduality. The resulting functional is evaluation of the bundle against its dual, followed by cup product and trace. \(\square\)

The tensor product in (9) is an ordinary tensor product because a vector bundle is flat. Replacing \(E\) by an arbitrary coherent \(F\) and \(E^\vee\) by its ordinary dual is generally incorrect; (8) is the appropriate statement.

## 6. Hypersurfaces and torsion

Let \(Z\subset\mathbf P^n_k\), \(n\geq1\), be defined by a nonzero homogeneous polynomial \(f\) of degree \(d\geq1\). Since the polynomial ring is a domain, \(f\) is a nonzerodivisor on every chart where its local equation is defined. The sheaf sequence
\[
0\to\mathcal O_P(-d)\xrightarrow{f}\mathcal O_P
 \to\mathcal O_Z\to0
\]
is exact. Its two-term locally free resolution computes internal Hom into \(\mathcal O_P\) as \(\mathcal O_P\xrightarrow{f}\mathcal O_P(d)\). The kernel is zero and the cokernel is \(\mathcal O_Z(d)\), so
\[
\mathcal H om_P(\mathcal O_Z,\mathcal O_P)=0,
\quad\mathcal E xt^1_P(\mathcal O_Z,\mathcal O_P)=\mathcal O_Z(d),
\quad\mathcal E xt^j_P(\mathcal O_Z,\mathcal O_P)=0\ (j\ne1).
\tag{10}
\]
This computation does not require \(Z\) to be smooth or reduced. Multiplying the target by \(\omega_P\) changes its nonzero term to \(\mathcal O_Z(d-n-1)\).

On \(\mathbf P^1\), let \(p\) be a rational point. Then \(Z=p\) is a degree-one hypersurface. Its ordinary dual into \(\omega_P\) is zero, but
\[
\operatorname{Ext}^1_P(k(p),\omega_P)\cong k,
\qquad H^0(P,k(p))=k.
\]
The nonzero Ext group is exactly what duality requires. A formula involving only cohomology of \(\mathcal H om(k(p),\omega_P)\) would instead give zero. The correction is not an extra hypothesis on a smooth ambient space: torsion in the input already makes it necessary to use derived Hom.

There is also a geometric interpretation when both inputs are bundles. The group
\[
\operatorname{Ext}^1_{\mathbf P^1}(\mathcal O(b),\mathcal O(a))
 =H^1(\mathbf P^1,\mathcal O(a-b))
\]
classifies extensions of the first bundle by the second. Such an extension splits locally because its quotient is locally free. Differences between local splittings are Hom-valued Čech cocycles. Changing the splittings adds a coboundary, and conversely upper triangular transition matrices made from any such cocycle glue an extension. This proves the classification here directly from the Čech interpretation, including its zero class as the split extension.

Take \(a=-2\) and \(b=0\). The extension space is one-dimensional and is dual to \(H^0(\mathcal O)=k\). A concrete nonzero extension is
\[
0\to\mathcal O(-2)
 \xrightarrow{(-T_1,T_0)}\mathcal O(-1)^{\oplus2}
 \xrightarrow{(T_0,T_1)}\mathcal O\to0.
\]
Exactness can be checked wherever either coordinate is invertible. On \(U_0\), a lift of the unit is \((T_0^{-1},0)\); on \(U_1\), a lift is \((0,T_1^{-1})\). Their difference on the ordered overlap is
\[
(-T_0^{-1},T_1^{-1})
 =(-T_1,T_0)\frac1{T_0T_1}.
\]
Thus the connecting class is exactly the trace-normalized generator. The extension cannot split: a splitting would lift the nonzero global unit to a global section of \(\mathcal O(-1)^{\oplus2}\), whose space of sections is zero. This supplies an explicit geometric representative of the perfect pairing, rather than only its dimension count. In contrast, when \(a-b\geq-1\), the first cohomology vanishes and every extension of these two line bundles splits. A global extension can therefore be nontrivial despite being split on every affine chart.

Pairing this extension with the constant section one gives trace one. Pairing with any constant \(c\) gives \(c\), so the geometric construction also verifies the scalar normalization of the duality isomorphism.

## 7. Exercises with solutions

**Exercise 7.1 (easy: the line).** Verify duality for every \(\mathcal O(d)\) on \(\mathbf P^1_k\), including \(d=-1\).

**Solution.** For \(d\geq0\), sections have dimension \(d+1\), and \(H^1(\mathcal O(-d-2))\) has the dual basis \(T_0^{-a-1}T_1^{-(d-a)-1}\), \(0\leq a\leq d\). Multiplication and trace give the identity pairing matrix. For \(d\leq-2\), interchange the two twists; then \(h^1(\mathcal O(d))=-d-1=h^0(\mathcal O(-d-2))\). For \(d=-1\), both twists are \(-1\) and all cohomology is zero. These cases verify both degrees of (9).

**Exercise 7.2 (medium: global hypersurface Ext).** Compute \(\operatorname{Ext}^i_P(\mathcal O_Z,\mathcal O_P)\) using (10).

**Solution.** The only nonzero row of (4) is \(q=1\). Hence global Hom is zero, and for \(i\geq1\) the answer is \(H^{i-1}(Z,\mathcal O_Z(d))\). This can be nonzero in several global degrees even though there is only one nonzero sheaf Ext. For instance a degree-one point on \(\mathbf P^1\) contributes its one-dimensional space in degree one.

**Exercise 7.3 (medium: effacement).** Explain why large positive \(q\) makes a surjection \(\mathcal O(-q)^m\to F\) efface both positive delta functors in Theorem 5.1.

**Solution.** Serre generation gives the surjection. Serre vanishing for the fixed coherent sheaf \(\omega_P\) kills \(H^j(\omega_P(q))\) for all \(j>0\), which is positive Ext from \(\mathcal O(-q)\). For the other functor, \(H^{n-j}(\mathcal O(-q))\) vanishes when its degree is strictly between zero and \(n\); degree zero vanishes since \(q>0\) if \(n>0\), and negative degrees vanish by definition. If \(n=0\), every positive functor value already has negative cohomological degree. Thus the maps to the values on the surjecting sheaf land in zero. No termination of its kernel resolution is needed.

**Exercise 7.4 (medium: the canonical bundle).** Derive \(\bigwedge^n\Omega_{P/k}=\mathcal O_P(-n-1)\) from the Euler sequence.

**Solution.** On \(U_i\), put \(x_l=T_l/T_i\). The row \((x_0,\ldots,x_n)\), with \(x_i=1\), defines a surjection from \(\mathcal O(-1)^{n+1}\) to \(\mathcal O\). Its kernel is free with basis \(e_l-x_l e_i\), \(l\ne i\), using the \(T_i^{-1}\) frame of \(\mathcal O(-1)\). The assignments \(dx_l\mapsto e_l-x_l e_i\) glue: on \(U_j\), the relations \(d(x_l/x_j)=dx_l/x_j-x_l dx_j/x_j^2\), together with the factor \(T_j^{-1}=x_j^{-1}T_i^{-1}\), give exactly the same change of basis. The universal property of differentials identifies the kernel with \(\Omega_{P/k}\). Thus
\(0\to\Omega_{P/k}\to\mathcal O(-1)^{n+1}\to\mathcal O\to0\) is exact. The sequence locally splits because its last term is free. Taking determinants gives \(\det\Omega=\det(\mathcal O(-1)^{n+1})=\mathcal O(-n-1)\). For \(n=0\), both are the trivial line on the point; its chosen twist frame still supplies the trace convention of Section 3. The module-of-differentials construction is the prerequisite *Kähler differentials* in *Commutative algebra for geometry*.

**Exercise 7.5 (hard: failure of ordinary duality).** For a rational point \(p\in\mathbf P^1\), compute the global Ext groups of \(k(p)\) into \(\omega_P\), and compare with the ordinary dual sheaf.

**Solution.** Twisting (10) gives only \(\mathcal E xt^1(k(p),\omega_P)=\mathcal O_p(-1)\), a one-dimensional skyscraper sheaf. Its positive cohomology is zero. Thus \(\operatorname{Ext}^1=k\) and all other global Ext groups vanish. The ordinary dual sheaf is zero because its image would be killed by a local equation for \(p\), a nonzerodivisor on the locally free target. Yet \(H^0(k(p))=k\). This verifies (8) and disproves the replacement of derived Hom by ordinary Hom for coherent torsion sheaves.

**Exercise 7.6 (hard: uniqueness of the trace normalization).** If the trace is multiplied by \(c\in k^\times\), how do the duality maps change?

**Solution.** Formula (7) is multiplied by \(c\). Its unique extension to the effaceable delta functors is therefore \(c\theta^i\) in every degree. The underlying vector-space dimensions and perfectness remain the same, but the chosen identification with the dual space changes by this scalar. Fixing the ordered Čech class to have trace one removes that ambiguity.

## References

- Kiran S. Kedlaya, [*Serre duality for projective space*](https://ocw.mit.edu/courses/18-726-algebraic-geometry-spring-2009/resources/mit18_726s09_lec23_serre_dual_proj/), MIT OpenCourseWare 18.726, Spring 2009, Sections 1–3, gives a complementary treatment of Ext, the trace pairing and the canonical bundle. The notes are reusable under [CC BY-NC-SA 4.0](https://ocw.mit.edu/pages/privacy-and-terms-of-use/). They are recommended reading; the complete proof and trace convention in this lesson are retained.

- **[Stacks]** The Stacks project authors, *The Stacks project*, in its AI Integrated Stacks Project edition: Hom complexes [Tag 0A8K](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-section-hom-complexes), internal derived Hom [Tag 08DH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-section-internal-hom), Ext [Tag 0BQP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-section-ext), and global derived Hom [Tag 0B6A](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-section-global-RHom). These reference texts retain their GFDL licence; this exposition and its proofs are independently written.
- *Sheaves of modules and their derived categories*, Theorem 2.3, Lemma 1.1, Proposition 1.3 and Theorem 4.1, supplies the injective foundation. The projective-space calculation, Serre theorems and finiteness used above are proved in the linked preceding lessons.
- The relative projective-bundle right-adjoint formula [Stacks, Tag 0A9W](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/duality.html#duality-lemma-upper-shriek-P1) will be treated in *The right adjoint of derived pushforward*. It is not required for the proof of (8).
