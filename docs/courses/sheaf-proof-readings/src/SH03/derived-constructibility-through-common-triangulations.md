# Derived constructibility through common triangulations

A bounded complex can have constructible cohomology even when the sheaves in a particular resolution are not constructible. We will replace that resolution by a bounded complex of constructible sheaves, and prove that this replacement preserves every derived morphism. A common triangulation supplies the local algebra. A second triangulation, chosen after a morphism has been represented by a roof, checks that no extra morphisms disappear.

Use Constructibility from microsupport and perfect stalks for the definitions and the abelian constructible categories, and Constructible sheaves on a triangulation for its Theorems 5 and 7. The compatible ordinary refinement is proved in Microlocal stratifications by removing bad loci. We import the subanalytic triangulation theorem: a locally finite subanalytic partition of a finite-dimensional real analytic manifold admits a locally finite triangulation whose open simplex images are subanalytic analytic submanifolds, each contained in one partition member. The compatible geometric triangulation is stated in Kashiwara's freely accessible Riemann–Hilbert paper. It is a geometric prerequisite; its proof is separate from the sheaf argument below.

*Original programme exposition by GPT-6.1 Sol (OpenAI), Ultra, September 2026; source comparison and editorial revision by GPT-6 Astra (OpenAI), Ultra, October 2026. Independently expressed programme text is dedicated under CC0. Human sources retain their own terms.*

## Two bounded categories and their natural functor

Let \(X\) be a real analytic manifold with one finite dimension bound \(n\), and let \(k\) be a commutative ring of finite global dimension. Write

\[
\mathcal C_X=w\text{-}\mathbb R\text{-}\operatorname{Cons}(X)
\]

for the abelian category of weakly \(\mathbb R\)-constructible sheaves. Its stalk modules may be infinite. The inclusion into all sheaves of \(k\)-modules is exact: its kernels and cokernels are the ambient sheaf kernels and cokernels. It consequently gives a functor

\[
J_X:D^b(\mathcal C_X)\longrightarrow
D^b_{w\text{-}\mathbb R\text{-}c}(k_X).
\tag{1}
\]

On the left we start with bounded complexes whose terms belong to \(\mathcal C_X\), and invert their quasi-isomorphisms. On the right we take the full subcategory of the ambient bounded derived category whose cohomology sheaves are weakly constructible. In particular, the right side includes extension data between different cohomological degrees.

Exactness and abelian closure show that (1) lands in this subcategory. They do not by themselves prove that (1) is an equivalence. Full faithfulness asks whether every ambient derived morphism comes from the constructible category and whether a morphism that becomes zero was already zero.

If \(k\) is also Noetherian, let
\(\mathcal C_X^{\mathrm{fin}}=\mathbb R\text{-}\operatorname{Cons}(X)\).
A sheaf belongs to this abelian category exactly when it is weakly constructible and has finitely generated stalks. Here the finite-global-dimension hypothesis makes each such stalk perfect. There is a second natural functor

\[
J_X^{\mathrm{fin}}:D^b(\mathcal C_X^{\mathrm{fin}})
\longrightarrow D^b_{\mathbb R\text{-}c}(k_X).
\tag{2}
\]

Noetherianity will remain in every assertion involving this abelian finite category.

## A triangulation for finitely many sheaves

**Common triangulation lemma.** Given finitely many weakly constructible sheaves \(F_1,\ldots,F_r\), there is a homeomorphism

\[
i:|S|\xrightarrow{\sim}X
\tag{3}
\]

from a locally finite simplicial complex of dimension at most \(n\), such that every \(i^{-1}F_a\) is constant on each open simplex. If the original stalks are finitely generated, so are the simplex stalks.

**Proof.** For each sheaf choose a locally finite subanalytic cover on which its restrictions are locally constant. The finite family of covers is locally finite when their members are taken together. Apply the compatible ordinary refinement to their exact membership cells. It gives a locally finite subanalytic partition into analytic submanifolds, with each partition member lying in a suitable member of every original cover. Restriction of each \(F_a\) to every partition member is therefore locally constant.

Apply the imported triangulation theorem to this partition. Each open simplex image lies in a partition member, so the restriction of \(i^{-1}F_a\) to the open simplex is locally constant. An open simplex is contractible and locally simply connected; constant transport of a local system has no monodromy there. The restriction is thus constant, with no assumption of finite rank. Its stalk at \(s\) is the original stalk at \(i(s)\), which proves the finite assertion. The dimension bound comes from the dimensions of the simplex images as submanifolds of \(X\). \(\square\)

The homeomorphism \(i\) is not asserted analytic on all of \(|S|\). No differential or cotangent pullback by \(i\) is used. Ordinary sheaf inverse and direct image along a homeomorphism are inverse exact equivalences.

The lemma applies to all the terms of finitely many bounded complexes: there are only finitely many sheaves to consider. It also applies to the finitely many nonzero cohomology sheaves of one bounded object. These are two different uses of the lemma.

Let \(\mathcal A_S\) denote the category of weakly simplex-constructible sheaves on \(|S|\), equivalently the face diagrams in the triangulation lesson. Its proved derived comparison is

\[
D^b(\mathcal A_S)\xrightarrow{\sim}D^b_{wS}(k_{|S|}).
\tag{4}
\]

For Noetherian \(k\), the finite-value category has the comparison

\[
D^b(\mathcal A_S^{\mathrm{fg}})\xrightarrow{\sim}D^b_S(k_{|S|}).
\tag{5}
\]

These statements include the ambient derived Hom comparison. Their proofs use actual open-star cohomology and derived adjunction; (5) also uses finite-value projective covers and the Noetherian kernel argument.

For a triangulation as in (3), exact direct image defines

\[
P_i:\mathcal A_S\longrightarrow\mathcal C_X,
\qquad H\longmapsto i_*H.
\tag{6}
\]

Indeed, the locally finite subanalytic open simplex images cover \(X\), and \(i_*H\) is locally constant on each one. This is the defining cover criterion. Finite simplex values give finitely generated stalks, so (6) also sends \(\mathcal A_S^{\mathrm{fg}}\) into \(\mathcal C_X^{\mathrm{fin}}\). Exactness follows from the homeomorphism and the ambient definitions of exactness.

## Replacing an object while preserving its extensions

**Theorem 1.** The functor \(J_X\) in (1) is an equivalence.

We prove essential surjectivity, fullness and faithfulness separately.

**Essential surjectivity.** Let
\(F\in D^b_{w\text{-}\mathbb R\text{-}c}(k_X)\).
There is one interval \([a,b]\) outside which all its cohomology sheaves vanish. Apply the common triangulation lemma to
\(H^a(F),\ldots,H^b(F)\).
Inverse image under (3) is exact, so

\[
H^j(i^{-1}F)=i^{-1}H^j(F).
\tag{7}
\]

Thus \(i^{-1}F\in D^b_{wS}(k_{|S|})\). By (4) it is represented by a bounded complex \(B^\bullet\) in \(\mathcal A_S\), with an isomorphism in the ambient derived category. Apply the exact homeomorphism direct image. The bounded complex \(i_*B^\bullet\) has weakly constructible terms by (6), and

\[
J_X(i_*B^\bullet)\simeq i_*i^{-1}F\simeq F.
\tag{8}
\]

The whole object was pulled back and represented. We did not replace it by the direct sum of its cohomology sheaves, which could discard its connecting morphisms.

## Lifting every ambient derived morphism

**Fullness.** Let \(F^\bullet,G^\bullet\) be bounded complexes in \(\mathcal C_X\). Choose a common triangulation of all their terms. Then their inverse images are bounded complexes in \(\mathcal A_S\), including their differentials as morphisms of simplex-constructible sheaves.

There is a commuting square

\[
\begin{array}{ccc}
\operatorname{Hom}_{D^b(\mathcal A_S)}(i^{-1}F^\bullet,i^{-1}G^\bullet)
&\xrightarrow{\ P_i\ }&
\operatorname{Hom}_{D^b(\mathcal C_X)}(F^\bullet,G^\bullet)\\[2mm]
\downarrow\scriptstyle{\sim}&&\downarrow\scriptstyle{J_X}\\[2mm]
\operatorname{Hom}_{D^b(k_{|S|})}(i^{-1}F^\bullet,i^{-1}G^\bullet)
&\xrightarrow{\ \sim\ }&
\operatorname{Hom}_{D^b(k_X)}(F^\bullet,G^\bullet).
\end{array}
\tag{9}
\]

The left vertical arrow is the fully faithful part of (4); the lower horizontal arrow is the exact homeomorphism equivalence. Both respect the same inclusions and chain maps, so the square commutes.

Given an ambient morphism in the lower right corner, transport it to the lower left, lift it through the left isomorphism, and apply the top arrow. Its image under \(J_X\) is the given morphism. This proves fullness. Notice that no injectivity of the top arrow was assumed.

## Converting a roof by an actual mapping cone

For faithfulness we need a description of an arbitrary morphism in
\(D^b(\mathcal C_X)\). The ordinary derived localization gives a left roof in the homotopy category,

\[
F^\bullet\xleftarrow{\ s\ }Q^\bullet
\xrightarrow{\ a\ }G^\bullet,
\qquad s\text{ a quasi-isomorphism}.
\tag{10}
\]

All its complexes are bounded complexes in \(\mathcal C_X\). We can convert it into a right roof within the same category. Use the cohomological cone convention
\(\operatorname{Cone}(u)^j=B^j\oplus A^{j+1}\),
with differential \((b,q)\mapsto(d_Bb+u(q),-d_Aq)\), for \(u:A\to B\). Put

\[
H^\bullet=\operatorname{Cone}\bigl((s,-a):Q^\bullet\to
F^\bullet\oplus G^\bullet\bigr).
\tag{11}
\]

The two inclusions give chain maps
\(\alpha:F^\bullet\to H^\bullet\) and
\(\beta:G^\bullet\to H^\bullet\). The quotient by the \(G^\bullet\) summand is \(\operatorname{Cone}(s)\), which is acyclic. The degreewise split exact sequence

\[
0\longrightarrow G^\bullet\xrightarrow{\beta}H^\bullet
\longrightarrow\operatorname{Cone}(s)\longrightarrow0
\tag{12}
\]

therefore makes \(\beta\) a quasi-isomorphism. The degree \(-1\) map
\(h(q)=(0,0,q)\) from \(Q^\bullet\) into (11) satisfies

\[
d_Hh+hd_Q=\alpha s-\beta a.
\tag{13}
\]

Consequently \(\alpha s=\beta a\) in the homotopy category, and the morphism represented by (10) is

\[
\beta^{-1}\alpha:
F^\bullet\longrightarrow H^\bullet\longleftarrow G^\bullet.
\tag{14}
\]

The cone has finite direct sums of constructible terms, so it is still a bounded complex in \(\mathcal C_X\). This verifies the needed right-roof representation without changing the coefficient or constructibility condition.

## Faithfulness includes the roof complex

**Faithfulness.** Suppose \(\varphi\in\operatorname{Hom}_{D^b(\mathcal C_X)}(F^\bullet,G^\bullet)\) has \(J_X(\varphi)=0\). Represent it as (14). Since \(J_X(\beta)\) is invertible,

\[
J_X(\alpha)=J_X(\beta)J_X(\varphi)=0.
\tag{15}
\]

Now choose a common triangulation of all the terms of the actual complexes \(F^\bullet\) and \(H^\bullet\). It can differ from a triangulation previously chosen for \(F^\bullet,G^\bullet\). The chain map \(i^{-1}\alpha\) belongs to the simplex category. By (15) its image in \(D^b(k_{|S|})\) is zero. Faithfulness of (4) implies

\[
[i^{-1}\alpha]=0\quad\text{in }D^b(\mathcal A_S).
\tag{16}
\]

Apply the derived functor induced by (6). Under the homeomorphism identifications its image is \([\alpha]\), so \([\alpha]=0\) in \(D^b(\mathcal C_X)\). Equation (14) gives \(\varphi=0\). Together with fullness and (8), this proves Theorem 1. \(\square\)

Triangulating only the cohomology sheaves of \(H^\bullet\) would not justify (16): we need the particular chain map to live in \(\mathcal A_S\). That is why the final triangulation includes its terms.

## The finite-stalk equivalence

**Theorem 2.** If \(k\) is Noetherian as well as of finite global dimension, the functor \(J_X^{\mathrm{fin}}\) in (2) is an equivalence.

**Proof.** If \(F\) is \(\mathbb R\)-constructible, its stalk complexes are perfect. Over this ring that is equivalent to finitely generated stalk cohomology. Triangulate its finitely many cohomology sheaves as above. Then \(i^{-1}F\in D^b_S(k_{|S|})\), and (5) gives a bounded representative whose terms have finite simplex values. Push it by (6) to obtain a bounded complex in \(\mathcal C_X^{\mathrm{fin}}\). This proves essential surjectivity.

For two bounded complexes with finite constructible terms, apply their common term triangulation and the Hom square (9) with \(\mathcal A_S^{\mathrm{fg}}\) and \(\mathcal C_X^{\mathrm{fin}}\) in the top row. The left vertical arrow is the full Hom comparison in (5). The same lift proves fullness.

For faithfulness, form (11) from a roof of bounded finite constructible complexes. Its finite direct sums still have finitely generated stalks. Its quasi-isomorphisms are detected by the same cohomology as in the ambient sheaf category, since the inclusion of this abelian category is exact. Triangulate all the terms of \(F^\bullet,H^\bullet\), apply faithfulness in (5), and repeat (15)–(16). This proves faithfulness. \(\square\)

The projective resolutions used to prove (5) need not have globally finitely many summands: at a simplex, only its finitely many faces contribute. Their kernels remain finite at every simplex by Noetherianity. Neither the theorem nor its proof asserts that all constructible sheaves on a noncompact \(X\) have finitely generated global sections.

## What the equivalences preserve

Both equivalences commute with shifts and triangles, and they preserve ordinary cohomology sheaves. They therefore identify the usual bounded truncations. For weakly constructible sheaves \(A,B\) and \(r\geq0\), Theorem 1 gives

\[
\operatorname{Ext}^r_{\mathcal C_X}(A,B)
\simeq \operatorname{Hom}_{D^b(k_X)}(A,B[r]).
\tag{17}
\]

Theorem 2 gives the corresponding identity in the finite category when \(A,B\) have finite stalks and the extra ring hypothesis holds. Nontrivial extensions, morphisms represented by roofs and connecting maps in truncation triangles are all preserved.

A chosen triangulation is a device in these proofs, not additional structure attached to an object of the final category. One can refine it to accommodate a new complex or a new morphism. The full constructible category allows these refinements, which is essential to the faithfulness argument.

## Examples and exercises with solutions

### Two cuts require one common partition

*Difficulty: Introductory.*

On \(\mathbb R\), take \(F=k_{[0,\infty)}\) and \(G=k_{(-\infty,1]}\). Describe a common analytic subanalytic partition on which both restrictions are constant. Give a locally finite triangulation refining it.

**Solution.** Use the five pieces
\(( -\infty,0),\{0\},(0,1),\{1\},(1,\infty)\).
The restrictions of each sheaf to each piece are \(k\) or zero. Triangulate the line with the integers as vertices and the intervals \((m,m+1)\) as open edges. The vertices \(0,1\) contain the changes, and every simplex lies in one of the five pieces. This triangulation is infinite but locally finite and has uniform dimension one. It handles both sheaves and any maps between them.

### The cone really gives a right denominator

*Difficulty: Intermediate.*

For (10), verify the differential, quotient and homotopy assertions in (11)–(13). Explain why the represented morphism is \(\beta^{-1}\alpha\).

**Solution.** An element of \(H^j\) is \((f,g,q)\) with \(q\in Q^{j+1}\), and
\[
d_H(f,g,q)=(d_Ff+s(q),\ d_Gg-a(q),\ -d_Qq).
\]
The subcomplex \(G\) is inserted as \((0,g,0)\). Modding it out leaves \((f,q)\) with differential \((d_Ff+s(q),-d_Qq)\), exactly \(\operatorname{Cone}(s)\). Since \(s\) is a quasi-isomorphism, this quotient is acyclic, and the cohomology sequence makes \(\beta\) a quasi-isomorphism. For \(q\in Q^j\), the element \(h(q)=(0,0,q)\in H^{j-1}\) gives
\(d_Hh(q)+h(d_Qq)=(s(q),-a(q),0)\).
Thus \(\alpha s=\beta a\) up to chain homotopy. Inverting both quasi-isomorphisms gives \(\beta^{-1}\alpha=a s^{-1}\), as required. The minus sign in \((s,-a)\) supplies the minus sign in this homotopy.

### A quasi-isomorphic target can have a new singular point

*Difficulty: Intermediate.*

Start with the integer triangulation of \(\mathbb R\) and \(F^\bullet=G^\bullet=k_{\mathbb R}\) in degree zero. Let \(c=1/2\), let \(A^\bullet\) be \(k_{\{c\}}\xrightarrow{\mathrm{id}}k_{\{c\}}\) in degrees zero and one, and put \(H^\bullet=G^\bullet\oplus A^\bullet\). Is \(\beta:G^\bullet\to H^\bullet\) a quasi-isomorphism? Can all terms of \(H^\bullet\) be used in the original simplex category?

**Solution.** The summand \(A^\bullet\) is acyclic, so \(\beta\) is a quasi-isomorphism. Both terms containing \(k_{\{c\}}\) have a stalk change inside the old open edge \((0,1)\); their restrictions to that edge are not constant. Hence those terms are not objects of its simplex category, even though the cohomology of \(H^\bullet\) is the original constant sheaf. Add \(c\) as a vertex and split that edge. All the terms then become simplex-constructible. Taking \(\alpha\) to be the inclusion of \(F=G\), the roof represents the identity. This example exhibits a new denominator complex which requires refinement in the proof.

### A boundary extension produces a derived morphism

*Difficulty: Advanced.*

On \(X=\mathbb R\), put \(A=k_{\{0\}}\) and \(B=k_{(0,\infty)}\), with \(k\neq0\). Compute \(\operatorname{Hom}_{D^b(k_X)}(A,B[1])\), and exhibit a nonzero extension representing a class. What does Theorem 1 say about it?

**Solution.** Let \(i:\{0\}\hookrightarrow X\). Derived adjunction identifies the Hom group with \(H^1(i^!B)\). Choose a vertex star \(V=(-1,1)\) in the integer triangulation. The restriction of \(B\) is simplex-constructible and its stalk at the vertex is zero. The triangulation lesson's star acyclicity gives \(R\Gamma(V;B)=0\). On \(V\setminus\{0\}\), the negative component contributes zero and the positive component contributes \(k\) in degree zero. The support triangle
\[
R\Gamma_{\{0\}}(V;B)\longrightarrow0\longrightarrow k
\xrightarrow{+1}
\]
therefore gives \(i^!B\simeq k[-1]\), and the Hom group is \(k\).
The exact sequence
\[
0\longrightarrow k_{(0,\infty)}\longrightarrow k_{[0,\infty)}
\longrightarrow k_{\{0\}}\longrightarrow0
\]
is an extension within \(\mathcal C_X\). In its middle sheaf the face map from the point stalk \(k\) to the positive stalk \(k\) is the identity. In the direct sum of its ends that face map is zero; a splitting would have to preserve it, which is impossible for \(k\neq0\). Thus the extension is nonzero. Theorem 1 identifies all these ambient classes with \(\operatorname{Ext}^1_{\mathcal C_X}(A,B)\). For Noetherian \(k\), Theorem 2 also computes them in the finite category.

### Torsion perfection permits a finite free representative

*Difficulty: Introductory.*

Take \(k=\mathbb Z\), \(m\geq2\), and \(F=(\mathbb Z/m)_{\{x\}}\) on an analytic manifold. Produce a bounded complex of constructible sheaves with finite free stalks representing \(F\). Distinguish its term degrees from the degrees of \(H^j(F)\).

**Solution.** Use
\(\mathbb Z_{\{x\}}\xrightarrow{m}\mathbb Z_{\{x\}}\)
in degrees \(-1,0\). Multiplication by \(m\) is injective, and its cokernel is \((\mathbb Z/m)_{\{x\}}\). The only nonzero cohomology is consequently in degree zero, although this chosen representative has two nonzero terms. Every stalk of its terms is \(\mathbb Z\) or zero, and every stalk complex of \(F\) is perfect. Perfection does not require a torsion module itself to be projective.

### Locally bounded is not one bounded derived object

*Difficulty: Intermediate.*

Over a nonzero field, on \(\mathbb R\) consider
\(F=\bigoplus_{m\geq1}k_{\{m\}}[m]\).
Its summands form a locally finite family. Is every stalk perfect? Is \(F\) an object to which Theorem 1 or 2 applies?

**Solution.** At the point \(m\) the stalk is \(k[m]\); at any other point it is zero. Every stalk is perfect, and in any sufficiently small neighborhood there is at most one nonzero summand, so the complex is locally bounded and its cohomology is locally constructible. Globally, however, \(H^{-m}(F)=k_{\{m\}}\neq0\) for every positive integer \(m\). There is no one bounded cohomological interval. Thus \(F\notin D^b(k_{\mathbb R})\), and neither theorem applies. Local finiteness of the supports does not supply global boundedness.

### Keeping only local systems loses a sphere class

*Difficulty: Advanced.*

Let \(k\) be a nonzero field and \(X=S^2\). Compare \(\operatorname{Hom}(k_X,k_X[2])\) in the ambient sheaf derived category and in the bounded derived category of local systems. Explain why this does not contradict Theorem 1.

**Solution.** Every local system on the simply connected sphere is constant, so that abelian category is equivalent to \(k\)-vector spaces. Vector spaces have split exact sequences and are projective; the Hom group in its derived category is therefore zero.
In the ambient category the Hom group is \(H^2(S^2;k)\). Here is its calculation. Cover the sphere by two slightly overlapping open hemispherical disks \(U,V\). Each disk has constant-sheaf cohomology \(k\) in degree zero only. Their intersection is an equatorial band. Cover that band by two angular strips whose intersection has two contractible components. Constant-sheaf acyclicity on these disk or rectangle charts and the Mayer–Vietoris sequence give the band's \(H^1\) as the cokernel of
\[
k\oplus k\longrightarrow k\oplus k,
\qquad(u,v)\longmapsto(v-u,v-u),
\]
which is \(k\); its higher cohomology vanishes. The sphere's Mayer–Vietoris sequence now gives \(H^2(S^2;k)\simeq k\). Thus an ambient nonzero degree-two morphism is lost if every term is required to be a local system. Theorem 1 allows constructible terms with finer subanalytic strata. They can represent that morphism; the local-system category alone cannot. The ambient acyclicity used here is the same constant-sheaf topological prerequisite stated in the triangulation lesson.

## References

The primary sources are Kashiwara's *The Riemann–Hilbert Problem for Holonomic Systems*, Proposition 2.5 and Theorem 2.8 with its added-in-proof correction; Prelli's *Sheaves on Subanalytic Sites*, Lemma 2.1.1 and Theorem 2.1.2; and Lunts–Schnürer's *Categories of constructible sheaves*, Theorems 4.1 and 5.25, §6 and §7. The comparisons below specify their different coefficients, categories and proof mechanisms. Ordinary derived localization remains the categorical prerequisite for the explicit cone conversion (11)–(13).

## The source roles in the common-triangulation argument

Masaki Kashiwara's [*The Riemann–Hilbert Problem for Holonomic Systems*](https://www.kurims.kyoto-u.ac.jp/~kenkyubu/kashiwara/RiemannHilbert.pdf), Proposition 2.5 and Theorem 2.8, printed pp. 330–331, is the source of the common-triangulation proof architecture. First it triangulates the finitely many cohomology sheaves and applies the simplicial realization theorem. For fullness it triangulates the chosen terms; for faithfulness it also triangulates the new quasi-isomorphic target representing a vanishing morphism. The proof above expresses these distinct choices through the actual right denominator and its cone, so the last refinement cannot be suppressed. The source treats complex vector spaces. Its added-in-proof note, printed p. 365, explicitly repairs a finite-dimensional intermediate-term gap by separating the weak theorem from a finite-term replacement lemma. Here the corresponding finite-value comparison is supplied by the projective covers and Noetherian kernel argument in the triangulation lesson. That supplied argument, not a change of coefficient letters in the source statement, supports the wider coefficient scope.

The geometric prerequisite for this derived sheaf argument is supplied by Compatible triangulations on arbitrary analytic manifolds. Starting from the relative polyhedron theorem, that section proves the manifold statement through finite-colour chart blocks, finite-regularity subanalytic cutoffs, a proper embedding and analytic chart-coordinate recovery on open simplices. Its stated lower prerequisites remain explicit dependencies: uniformization; the subanalytic set, regularity and dimension calculus; analytic Noetherianity; the analytic constant-rank theorem; and uniqueness for finite systems of analytic ordinary differential equations.

Luca Prelli's [*Sheaves on Subanalytic Sites*, arXiv:math/0505498v3](https://arxiv.org/abs/math/0505498v3), §1.1 and Lemma 2.1.1–Theorem 2.1.2, pp. 3–7 and 28–29, supplies the site comparison mechanism: relatively compact opens have finite covers, compatible open stars kill higher section cohomology, and the inverse-image/direct-image adjunction identifies the constructible derived categories. His coefficient ring is a field and the constructible category has finite stalks; the ordinary-topology realization theorem is cited as an input. The proof below instead uses our explicit arbitrary-module star theorem for the weak category, and the separate Noetherian finite-term argument for the finite category. In particular, ordinary inverse image alone is not a test for constructibility of a site complex; the quotient example below explains the missing condition.

## Derived constructibility on the subanalytic site

Keep the coefficient, boundedness and manifold hypotheses above. The site \(X_{\mathrm{sa}}\) has subanalytic open subsets of \(X\) as objects. A family of open subsets covering \(U\) is a site covering if, on every compact subset of \(X\), a finite subfamily already covers its intersection with \(U\). On a relatively compact \(U\), every such covering has a finite subcover, by applying the condition to \(\overline U\). Relatively compact subanalytic opens form a basis for this site.

Write \(\rho:X\to X_{\mathrm{sa}}\) for the natural morphism of sites. Its direct functor is ordinary sections on these objects:
\((\rho_*A)(U)=\Gamma(U;A)\). Its inverse functor is ordinary sheafification from the subanalytic-open basis. It is exact, since basis restriction and sheafification calculate kernels and cokernels locally, and

\[
\rho^{-1}\rho_*A\simeq A.
\tag{18}
\]

Indeed its stalk at \(x\) is the filtered system of \(\Gamma(U;A)\) over the subanalytic neighborhoods of \(x\), a cofinal neighborhood basis. The map is ordinary evaluation. The adjunction \(\rho^{-1}\dashv\rho_*\) then makes \(\rho_*\) fully faithful. Direct image need not be exact on every sheaf.

**Lemma.** If \(A\) is weakly constructible, then \(R^q\rho_*A=0\) for \(q>0\). On the abelian weak constructible category, \(\rho_*\) is exact.

**Proof.** On a relatively compact subanalytic open \(U\), choose a locally finite compatible triangulation of \(X\) for \(A\) and \(U\). Only finitely many closed simplices meet \(\overline U\), by compactness and local finiteness. Compatibility with the open \(U\) ensures that the open star of every simplex contained in \(U\) is also contained in \(U\): a coface of a point in the open \(U\) cannot lie entirely outside \(U\), because its closure meets that point; compatibility places its open interior in one of the two pieces. These finitely many stars cover \(U\). Each is relatively compact, being contained in finitely many closed simplices.

The star acyclicity theorem gives \(H^q(U_\sigma;A)=0\) for \(q>0\), without restricting the coefficient modules. The sheaf \(R^q\rho_*A\) is the site sheaf associated to the presheaf of these higher section groups, as one sees by an injective resolution and the local definition of sheaf cohomology. On the finite star covering all those groups vanish. The presheaf therefore sheafifies to zero, proving the first claim. Applying the derived long exact sequence to a short exact sequence of weakly constructible sheaves gives exactness of its direct images. \(\square\)

Let \(D^b_{w\mathrm{sa}}(k_{X_{\mathrm{sa}}})\) be the full category of bounded site complexes whose cohomology sheaves are in the image of weakly constructible ordinary sheaves under \(\rho_*\). This is a condition on the site cohomology itself, not just on the ordinary inverse image. Then

\[
D^b(\mathcal C_X)
\simeq D^b_{w\text{-}\mathbb R\text{-}c}(k_X)
\xrightarrow[\quad R\rho_*\quad]{\ \sim\ }
D^b_{w\mathrm{sa}}(k_{X_{\mathrm{sa}}}).
\tag{19}
\]

If \(k\) is also Noetherian, put a finite-stalk condition on the ordinary sheaves defining the site subcategory. The corresponding equivalence is

\[
D^b(\mathcal C_X^{\mathrm{fin}})
\simeq D^b_{\mathbb R\text{-}c}(k_X)
\xrightarrow[\quad R\rho_*\quad]{\ \sim\ }
D^b_{\mathrm{sa},\mathrm{fin}}(k_{X_{\mathrm{sa}}}).
\tag{20}
\]

**Proof.** The first equivalences are Theorems 1 and 2. For the site comparison, derive the adjunction. The exact \(\rho^{-1}\) makes \(\rho_*\) preserve injectives. For an injective resolution \(I^\bullet\) of an ordinary complex, (18) identifies \(\rho^{-1}\rho_*I^\bullet\) with \(I^\bullet\), including its differentials. The derived counit is consequently an isomorphism. Thus \(R\rho_*\) is fully faithful. We may calculate this in bounded-below categories: the finite dimension of \(X\) uniformly bounds section cohomology on every open set, so the derived image of a globally bounded complex is bounded.

For a bounded ordinary constructible complex, filter by its finitely many cohomology sheaves. The lemma makes every such sheaf \(\rho_*\)-acyclic, so the resulting cohomology sequence gives

\[
H^j(R\rho_*F)\simeq\rho_*H^j(F).
\tag{21}
\]

It follows that the functor lands in the claimed site subcategory. Conversely take a site object \(B\) in that subcategory. Exact inverse image gives
\(H^j(\rho^{-1}B)=\rho^{-1}H^j(B)\), weakly constructible by its definition and (18). Apply (21) to \(\rho^{-1}B\). The unit
\(B\to R\rho_*\rho^{-1}B\) induces the isomorphism
\(H^j(B)\to\rho_*\rho^{-1}H^j(B)\) for every \(j\), since each \(H^j(B)\) is already in the fully faithful image of \(\rho_*\). Therefore the derived unit is an isomorphism, proving essential surjectivity and (19). The identical argument with finite stalks proves (20), retaining Noetherianity for the finite abelian category. All equivalences preserve the extension data of the complexes. \(\square\)

## A further exercise on the site condition

### Ordinary inverse image can miss a nonzero site quotient

*Difficulty: Advanced.*

On \(X=\mathbb R\) let \(U=(0,1)\), \(U_n=(1/n,1)\) for \(n\geq2\), and let \(k\) be a nonzero field. Form the site colimit \(B=\operatorname{colim}_n\rho_*k_{U_n}\) and its natural map to \(\rho_*k_U\), where the ordinary sheaves are extended by zero. Show that the site cokernel \(Q\) is nonzero but \(\rho^{-1}Q=0\). Why does this not contradict (19)?

**Solution.** Sections of \(k_{U_n}\) on connected \(U\) are zero: a nonzero constant section on \(U_n\) cannot extend by zero across the interior point \(1/n\). Filtered site colimits commute with sections on a relatively compact object. To verify that statement, calculate a colimit presheaf on the relatively compact basis. Its finite-cover matching conditions use only finite products and equalizers, which commute with filtered module colimits. It is therefore already a sheaf and has the asserted sections. Consequently \(B(U)=0\), whereas \((\rho_*k_U)(U)=k\).

The unit section does not lift even after a site covering. Such a covering of \(U\) has a finite subcover. At least one of its subanalytic members contains an interval \((0,\epsilon)\): near zero a subanalytic subset of the line has only finitely many components, and finitely many sets bounded away from zero cannot cover \(U\). On that member the unit is nonzero on this interval, but every section from any \(k_{U_n}\) vanishes there near zero. Sections of \(B\) on this relatively compact member are their filtered colimit, so no such section lifts the unit. The map is not an epimorphism of site sheaves, and \(Q\neq0\).

The exact left adjoint \(\rho^{-1}\) preserves colimits. Equations (18) and \(\operatorname{colim}_n k_{U_n}=k_U\), checked on ordinary stalks, make the inverse image of the map the identity of \(k_U\). Thus \(\rho^{-1}Q=0\). If the nonzero degree-zero \(Q\) belonged to the subcategory in (19), it would be \(\rho_*A\) for a weakly constructible \(A\), and (18) would give \(A=0\), hence \(Q=0\), a contradiction. The theorem imposes its condition on site cohomology; ordinary inverse image alone cannot certify it.

## Realization for a fixed stratification

The preceding equivalence permits a new common triangulation for a finite collection of sheaves or roof terms. A fixed stratification poses a different question. Valery A. Lunts and Olaf M. Schnürer's freely accessible [*Categories of constructible sheaves*](https://arxiv.org/html/2601.05477v1) gives a criterion that separates the topology of each stratum from the derived information at its boundary. We prove that criterion here, including its bounded-below scope. These arguments concern ordinary sheaves of modules; they do not require microsupport estimates or the geometric analytic-manifold triangulation theorem.

In this section \(R\) may be any associative unital ring, and modules are left modules. This broader coefficient convention applies to the results below, rather than changing the hypotheses of the earlier analytic or tensor statements. Write \(\operatorname{Sh}_R(Y)\) for sheaves of \(R\)-modules, and \(\operatorname{Loc}_R(Y)\) for locally constant sheaves with arbitrary stalk modules.

### Monodromy and the local extension condition

Suppose \(Y\) is connected and locally simply connected. Fix a point and its universal covering \(\pi:\widetilde Y\to Y\), with deck group \(G=\pi_1(Y)\). Path transport of germs gives an exact equivalence

\[
\operatorname{Loc}_R(Y)\simeq R[G]\text{-}\operatorname{Mod}.
\tag{22}
\]

To verify it, pull a local system to the simply connected cover. A germ continues uniquely along paths, and continuation around a homotopy of paths changes nothing: cover the homotopy square by finitely many trivializing neighborhoods and compare along their edges. Thus the pullback is constant. Its deck action becomes an \(R\)-linear action of \(G\) on the constant module. Conversely form the quotient of \(\widetilde Y\times M\) by this diagonal action, and take its local sections. An evenly covered neighborhood identifies those sections with a constant module. The constructions recover the original germs and transport, and maps are precisely equivariant module maps. Kernels and cokernels are calculated in a trivializing neighborhood, proving exactness.

The inclusion into all sheaves preserves all limits and colimits. For products, use a simply connected connected neighborhood: every coordinate of a section of a product of constant sheaves is constant, so the section is a constant tuple. Colimits follow from exact constant-sheaf inverse image and sheafification on the same neighborhoods. In particular coproducts are exact.

If \(Y\) has a basis of simply connected neighborhoods whose constant sheaves have zero first cohomology for every \(R\)-module, local systems are also closed under extensions. Indeed, on one such neighborhood \(V\), apply sections to
\(0\to M_V\to E\to N_V\to0\). The zero \(H^1(V;M_V)\) makes the section sequence exact. Taking associated constant sheaves and comparing evaluation maps gives a morphism of short exact sequences whose two end maps are isomorphisms. Its middle map is consequently an isomorphism, so \(E\) is constant there. A basis of acyclic neighborhoods suffices.

### The universal-cover criterion

The projective test below is the mechanism of Lunts–Schnürer, Theorem 4.1, pp. 11–13: the regular local system turns ambient Ext into cohomology on the universal cover. Their passage to bounded-below realization uses truncations and the telescope triangle. The bounded-below target is material; their Remark 4.3 leaves the corresponding unrestricted unbounded equivalence open. We retain that limitation while spelling out the maps.

**Theorem.** Let \(Y\) be locally simply connected and locally acyclic for constant \(R\)-modules. The following conditions are equivalent:

1. Realization is an equivalence on bounded-below complexes of local systems.
2. Realization is an equivalence on bounded complexes of local systems.
3. Each component's universal covering is acyclic for every constant \(R\)-module.

Here acyclic means that higher sheaf cohomology is zero and degree-zero sections are the constant module. The functors in the first two conditions are

\[
D^+(\operatorname{Loc}_R(Y))\longrightarrow
D^+_{\operatorname{Loc}}(\operatorname{Sh}_R(Y)),
\qquad
D^b(\operatorname{Loc}_R(Y))\longrightarrow
D^b_{\operatorname{Loc}}(\operatorname{Sh}_R(Y)).
\tag{23}
\]

**Proof.** Components are open, so it suffices to prove the connected case. The covering direct image with finite support in its sheets, \(\pi_!\), is exact and left adjoint to the exact \(\pi^{-1}\). On an evenly covered neighborhood its stalk is the direct sum of the sheet stalks; this proves exactness, without pretending that an infinite covering is proper. The local system
\(P=\pi_!R_{\widetilde Y}\) corresponds under (22) to the free module \(R[G]\). It is a projective generator of the local-system category. Derived adjunction gives, for a local system \(N\),

\[
\operatorname{Hom}_{D(\operatorname{Sh}_R(Y))}(P,N[q])
\simeq H^q(\widetilde Y;\pi^{-1}N).
\tag{24}
\]

The corresponding group in \(D(\operatorname{Loc}_R(Y))\) is zero for \(q>0\), by projectivity of \(P\), and agrees in degree zero. Every constant module on the cover occurs among the \(\pi^{-1}N\): use its trivial \(G\)-action. Therefore equivalence in (23), even only for bounded objects, implies condition 3.

Conversely assume condition 3. Formula (24) says that \(P\) has no higher ambient Hom into any local system. A projective local system is a summand of a coproduct of copies of \(P\). Derived Hom from that coproduct is the product of the individual derived Hom complexes; products of groups are exact. The same vanishing and comparison thus hold for every projective local system.

Resolve a bounded-above local-system complex by bounded-above projective local systems, and represent a bounded-below target by a bounded-below complex. The preceding vanishing computes its ambient derived Hom with the same projective resolution as its local-system derived Hom. In each total degree only finitely many degrees of a bounded-above source and a bounded-below target occur. The comparison of these double complexes, or their finite diagonal filtrations, therefore proves full faithfulness for such a source and target.

For any source complex \(A\), exact coproducts give the truncation telescope

\[
\bigoplus_{n\geq0}\tau_{\leq n}A
\xrightarrow{\,1-\mathrm{shift}\,}
\bigoplus_{n\geq0}\tau_{\leq n}A
\longrightarrow A\longrightarrow
\left(\bigoplus_{n\geq0}\tau_{\leq n}A\right)[1].
\tag{25}
\]

The cohomology of its cone is \(H^q(A)\): the map \(1-\mathrm{shift}\) is injective on the direct sum, and its cokernel is the filtered union, eventually equal to \(H^q(A)\). Realization preserves this triangle and its coproducts. Apply Hom into a bounded-below target in both categories. The already proved comparison for each bounded-above truncation, the universal property of the coproduct, and the two long exact sequences prove full faithfulness for every source with a bounded-below target.

Every bounded ambient complex with local-system cohomology is now in the image: lift its finite sequence of cohomology extensions using this full faithfulness. For a bounded-below ambient complex \(F\), lift each bounded truncation \(\tau_{\leq n}F\) and its transition morphism. Their telescope realizes \(F\), by the same cohomology calculation as (25), and has the same lower cohomological bound. This proves essential surjectivity in \(D^+\), and hence also in \(D^b\). \(\square\)

This proof does not assert equivalence for arbitrary unbounded targets. It proves exactly the bounded and bounded-below statements, with arbitrary coefficient modules.

### The boundary comparison that must be checked

A realization theorem on every stratum does not yet compare gluing. The additional map is derived direct image computed inside the constructible heart versus derived direct image in all sheaves. Lunts–Schnürer construct this comparison before using it in Theorem 5.25, pp. 25–27. Their proof tests Hom between extensions by zero and derived direct images, then uses the localization triangles. The construction below keeps the natural comparison and the adjunction maps visible, so the fixed-stratification theorem has a checkable second hypothesis.

Let \(\mathcal S\) be a finite stratification of a topological space \(Y\) into locally closed strata, satisfying the frontier condition. Suppose each stratum is locally simply connected and locally \(1\)-acyclic: it has a basis of neighborhoods on which every constant module has zero first cohomology. Full local acyclicity is not required for the gluing criterion. Put
\(\mathcal B_Y=\operatorname{Cons}_R(Y,\mathcal S)\). Assume also the following boundary condition:
for every stratum inclusion \(s:S\hookrightarrow Y\) and every local system \(L\) on \(S\), the cohomology sheaves of \(Rs_*L\) are \(\mathcal S\)-constructible. Denote realization by
\(\mathcal R_Y:D^+(\mathcal B_Y)\to D^+_{\mathcal S}(Y)\).

The category \(\mathcal B_Y\) is abelian with exact inclusion, by (22) on neighborhoods of the strata, and is closed under extensions by the local argument above. The boundary condition is inherited by locally closed unions: if \(a:S\hookrightarrow Z\) and \(e:Z\hookrightarrow Y\), then \(Re_*Ra_*=Rs_*\) and \(e^{-1}Re_*=\mathrm{id}\); restricting the constructible cohomology of \(Rs_*L\) gives that of \(Ra_*L\). It has enough injectives. For each stratum embed \(F|_S\) into an injective local system \(I_S\), and use adjunction to obtain

\[
F\longrightarrow\bigoplus_{S\in\mathcal S}s_*I_S.
\tag{26}
\]

At a point in \(S\), the component for its own stratum is the chosen monomorphism; hence (26) is a monomorphism on every stalk. Each \(s_*I_S\) is constructible by the degree-zero part of the boundary condition and injective in \(\mathcal B_Y\), since restriction to \(S\) is exact. The finite sum is injective. No ambient injectivity of \(I_S\) is asserted.

Write \(R_{\mathcal S}s_*\) for direct image derived within the constructible categories. Resolving in those categories, then comparing with an ambient injective resolution, defines the canonical map

\[
\sigma_s:\mathcal R_Y R_{\mathcal S}s_*
\longrightarrow Rs_*\mathcal R_S.
\tag{27}
\]

Both sides agree with the ordinary functor in degree zero. Their higher terms can differ.

We spell out the gluing facts needed to use (27). Restriction and extension by zero for a union of strata are exact and preserve constructibility. Direct image and exceptional restriction preserve bounded-below constructible complexes under the boundary condition. To prove the latter assertion, induct on the number of ambient strata and, inside that induction, on the number of source strata. A locally closed inclusion factors as open into its closure followed by closed. Closed direct image is exact. For an open source \(Z\), choose a closed stratum \(C\) of \(Z\). The localization triangle on the smaller space \(Z\) expresses a constructible complex by its exceptional restriction to \(C\) and its restriction to \(Z\setminus C\). Pushing this triangle uses inclusions with fewer source strata; the one-stratum case is the boundary condition. This proves direct-image closure. The complementary open direct image in the localization triangle then proves closed exceptional-restriction closure. For bounded-below input, truncate above any desired degree first: a right derived left-exact functor cannot carry terms above that degree into lower cohomology. The bounded argument therefore proves the same assertion degree by degree.

Consequently all four ordinary adjunctions restrict to the constructible hearts and derive there. For a closed-open pair \(i:Z\hookrightarrow Y\), \(j:U\hookrightarrow Y\), these derived categories have the two localization triangles

\[
j_!j^{-1}A\longrightarrow A\longrightarrow i_*i^{-1}A
\longrightarrow j_!j^{-1}A[1],
\tag{28}
\]

\[
i_*R_{\mathcal S}i^!A\longrightarrow A
\longrightarrow R_{\mathcal S}j_*j^{-1}A
\longrightarrow i_*R_{\mathcal S}i^!A[1].
\tag{29}
\]

For completeness, (28) comes from the stalkwise exact short sequence on every term. For (29), take a constructible injective \(I\). The map \(I\to j_*j^{-1}I\) is a split epimorphism: extend the natural map \(j_!j^{-1}I\to I\) along the monomorphism \(j_!j^{-1}I\to j_*j^{-1}I\), using injectivity of \(I\). Restricting to \(U\) identifies the extension with the inverse of the restriction unit; full faithfulness of \(j_*\) shows that the resulting composite on \(j_*j^{-1}I\) is the identity. Its kernel is \(i_*i^!I\). Apply this degreewise to an injective resolution. All the restriction/direct/exceptional functors just used preserve the relevant injectives because their left adjoints are exact. This proves (29), including its actual adjunction maps.

The maps \(\sigma\), and the analogous exceptional maps \(\tau\), respect units and counits. A direct verification compares an internal injective resolution \(I^\bullet\) to an ambient one \(J^\bullet\): the maps are \(e_*I^\bullet\to e_*J^\bullet\) and \(e^!I^\bullet\to e^!J^\bullet\). Naturality of the ordinary adjunction units and counits gives the required commuting squares. Thus (29) maps to the ambient localization triangle. Its first and third terms have the canonical comparisons, and its middle map is the identity.

If \(\sigma_s\) is invertible for every single stratum, it is invertible for every stratified locally closed inclusion. Here is the finite induction, to avoid assuming this extra conclusion. For an open union \(Z\), split an internal injective complex and an ambient injective complex by a closed stratum \(C\subset Z\) and its open complement \(V\). Both decompositions are degreewise split short exact sequences as above. The comparison for \(V\), already known by induction, also gives the exceptional comparison for \(C\), by the morphism of localization triangles. Push the \(V\)-piece directly, and push the \(C\)-piece by open into the closed complement of \(V\), followed by closed into \(Y\). Both open pieces have fewer strata. Their comparisons are isomorphisms by induction; the two cohomology long exact sequences give the comparison for \(Z\). Factor an arbitrary locally closed inclusion into open and closed. Derived composition is compatible with these comparisons, since the right adjoints preserve injectives. The same triangles give the exceptional comparisons.

### The full fixed-stratification criterion

**Theorem.** Under the preceding assumptions, \(\mathcal R_Y\) is an equivalence if and only if, for every stratum \(S\),

1. \(D^+(\operatorname{Loc}_R(S))\to D^+_{\operatorname{Loc}}(S)\) is an equivalence;
2. the canonical map \(\sigma_s\) in (27) is an isomorphism.

When these hold, realization on every locally closed union of strata is an equivalence too.

**Proof.** Suppose first that the two conditions hold. The localization triangles (28) filter every source object by extensions by zero \(s_!A\), with \(A\in D^+(\operatorname{Loc}_R(S))\). Triangles (29), iterated over a closed stratum and its complement, filter the second argument of Hom by terms \(R_{\mathcal S}t_*B\). There are finitely many strata, so these are finite filtrations even for bounded-below complexes. For those two kinds of terms, adjunction gives

\[
\begin{aligned}
\operatorname{Hom}(s_!A,R_{\mathcal S}t_*B[q])
&\simeq\operatorname{Hom}(t^{-1}s_!A,B[q]),\\
\operatorname{Hom}(s_!\mathcal R_S A,Rt_*\mathcal R_T B[q])
&\simeq\operatorname{Hom}(t^{-1}s_!\mathcal R_S A,\mathcal R_T B[q]).
\end{aligned}
\tag{30}
\]

The two groups agree: restriction and zero extension commute with realization, \(\sigma_t\) identifies the targets, and the one-stratum realization is fully faithful. For distinct strata the restriction \(t^{-1}s_!A\) is zero; for the same stratum it is \(A\). The identifications match the actual comparison maps by the unit/counit verification above. Applying the two long exact Hom sequences to the finite filtrations proves full faithfulness for arbitrary source objects.

For essential surjectivity, apply the ambient version of (28) successively. Each stratum restriction is realized by condition 1. Its zero extension is realized by the exact \(s_!\), and every connecting morphism lifts by full faithfulness. Its cone lifts the next extension. The finite induction realizes the entire bounded-below object.

Conversely assume that \(\mathcal R_Y\) is an equivalence. For a stratified locally closed \(e:Z\hookrightarrow Y\), zero extension is fully faithful in both categories, by its open-closed factorization and adjunctions. Since it commutes with realization, realization on \(Z\) is fully faithful. For an ambient object on \(Z\), realize its zero extension on \(Y\), then restrict the realizing object back to \(Z\). This proves essential surjectivity on \(Z\). Finally exact restriction \(e^{-1}\) has right adjoints \(R_{\mathcal S}e_*\) and \(Re_*\) in the two equivalent categories. The compatibility of the adjunction bijections and Yoneda identify their canonical map \(\sigma_e\) as an isomorphism. Taking \(Z=S\) proves both necessary conditions. \(\square\)

### Links compute the obstruction

A normal structure means a finite stratification by connected manifolds with a basis of compatible local product charts

\[
V_x\simeq B_x\times\operatorname{Cone}(L_x),
\qquad
S\cap V_x\simeq B_x\times(0,\epsilon)\times L_{x,S}.
\tag{31}
\]

Here \(x\in T\), \(B_x\subset T\) is a ball, and each link piece \(L_{x,S}\) is a manifold with finitely many connected components. The product chart is required to respect the strata. We use this as a stated topological structure; no claim that every stratification has it is implicit.

For a local system \(M\) on \(S\), restriction to a slice identifies it with a local system on \(L_{x,S}\). The ball and open radial interval are contractible, so local-system sheaf cohomology and its restriction maps give

\[
(R^q s_*M)_x\simeq H^q(L_{x,S};M|_{L_{x,S}}).
\tag{32}
\]

One can calculate this by an acyclic cover on the link and product neighborhoods: the contractible factors change neither the local system nor the cohomology, and shrinking them induces the same comparison. The constant neighborhood system therefore computes the direct-image stalk. Within \(B_x\) the same calculation is locally constant. This proves the boundary condition in this setting, rather than just assuming it.

The map \(\sigma_s\) is invertible exactly when every injective local system \(I\) on \(S\) has

\[
H^{q}(L_{x,S};I|_{L_{x,S}})=0\qquad(q>0)
\tag{33}
\]

for all incident links. Necessity follows by applying the comparison to such an \(I\): internal derived direct image is already \(s_*I\). For sufficiency, (32) makes every \(I\) ambient \(s_*\)-acyclic; its bounded-below internal injective resolution then calculates the ambient direct image as well. Thus contractible strata alone do not settle realization.

Suppose now that strata and connected link pieces have contractible universal coverings. Let \(H=\pi_1(L_{x,S,i})\), \(G=\pi_1(S)\), with the homomorphism induced by a slice inclusion. The universal-cover theorem identifies link cohomology with the derived invariants of the restricted \(R[G]\)-module. It follows from (33) that realization is an equivalence if restriction sends every injective \(R[G]\)-module to an \(H\)-invariant-acyclic module.

An injective homomorphism \(H\hookrightarrow G\) satisfies this test: \(R[G]\) is free as a right \(R[H]\)-module, so induction \(R[G]\otimes_{R[H]}-\) is exact and its right adjoint, restriction, preserves injectives. Higher \(H\)-invariants of that injective restriction vanish.

More generally it suffices that the kernel \(N\) be finite and its order be a unit in \(R\). Factor through \(Q=H/N\hookrightarrow G\). The restricted module is injective over \(R[Q]\). The \(N\)-invariants functor is exact, using

\[
m\longmapsto |N|^{-1}\sum_{n\in N}n m.
\tag{34}
\]

It is also right adjoint to exact inflation from \(R[Q]\), so sends \(R[H]\)-injectives to \(R[Q]\)-injectives. Apply \(N\)-invariants to an \(R[H]\)-injective resolution of the inflated \(R[Q]\)-injective module. Exactness gives an injective \(R[Q]\)-resolution, and taking \(Q\)-invariants has no positive cohomology. Since \(H\)-invariants are \(Q\)-invariants after \(N\)-invariants, the required vanishing follows. Over a field, the order-unit condition means characteristic does not divide \(|N|\). For a general ring one must retain invertibility itself.

### A torus example with a genuine boundary

On \(\mathbb P^1(\mathbb C)\), use the three torus-orbit strata \(\mathbb C^*\), \(0\), and \(\infty\). A punctured disk is \((0,\epsilon)\times S^1\), providing (31) at either closed stratum. The open stratum and its link have contractible universal covers. The inclusion of the link into \(\mathbb C^*\) induces an isomorphism \(\mathbb Z\to\mathbb Z\), after choosing a generator. Thus the injective-homomorphism test proves

\[
D^+(\operatorname{Cons}_R(\mathbb P^1,\{\mathbb C^*,0,\infty\}))
\simeq D^+_{\{\mathbb C^*,0,\infty\}}(\mathbb P^1;R)
\tag{35}
\]

for every unital \(R\), with arbitrary stalk modules. It also proves the bounded restriction of (35). A different stratification of this same space fails, as shown in the missing-derived-classes lesson. The distinction is in the actual boundary map of fundamental groups.

The general normal toric-variety result uses the same argument on each affine orbit star: a normal cone chart contracts to its closed orbit, and the orbit-link inclusion induces an injection on fundamental groups. These geometric cone charts are a separate toric-geometry input. Equation (35) supplies a complete explicit example without requiring that general input. Finite-stalk realization requires an additional finite-type argument; (35) by itself concerns the unrestricted constructible heart.

### Finite cohomology and the finite heart are different restrictions

Suppose \(R\) is left Noetherian. Constructible sheaves with finitely generated stalks form an abelian subcategory closed under extensions and direct summands: take kernels, cokernels and extension sequences on stalks, where these closure properties hold for finitely generated modules over a left Noetherian ring.

An equivalence in the fixed-stratification theorem restricts to bounded objects with finitely generated cohomology stalks. Indeed realization is exact on hearts and commutes with cohomology. A source object therefore has precisely the same stalk modules in its cohomology as its realization, and essential surjectivity supplies a source object with those cohomology modules. Boundedness is detected in the same way.

This gives an equivalence between the finite-cohomology subcategory of the derived unrestricted heart and the finite-cohomology ambient category. It does not yet identify either with the derived category of the finite heart. That further comparison requires representing roofs, extensions and their relations through finite-stalk terms. The last exercise below shows why an apparently natural coefficient subcategory can lose an ambient extension.

## Further exercises on fixed realization

### A simply connected stratum can still have missing derived classes

*Difficulty: Intermediate.*

Give \(S^2\) its single-stratum decomposition over a field \(k\). Compute the degree-two self-morphism of the constant sheaf in the two categories in (23). Explain the failed hypothesis.

**Solution.** A local system on \(S^2\) is constant, so its heart is vector spaces and the constant sheaf is projective. Its second self-morphism in the source is zero. Ambient derived adjunction identifies the target group with \(H^2(S^2;k)=k\), computed by the sphere's zero- and two-cells. The universal cover is \(S^2\) itself and is not acyclic. Simple connectivity supplies (22); it does not supply the higher vanishing required by (24).

### The circle retains its degree-one extension

*Difficulty: Intermediate.*

For a single-stratum circle over a field, calculate the degree-one self-extension of the trivial local system in its heart. Compare it with ambient cohomology.

**Solution.** The heart is modules over \(A=k[t,t^{-1}]\). The trivial module is \(k=A/(t-1)\), and
\(0\to A\xrightarrow{t-1}A\to k\to0\) is a free resolution: \(t-1\) is not a zero divisor, and evaluation at one is its quotient. Applying \(\operatorname{Hom}_A(-,k)\) gives zero differential, hence \(\operatorname{Ext}^1_A(k,k)=k\) and no higher extension. The circle's universal cover is the contractible line, so (23) identifies this with \(H^1(S^1;k)=k\). A constant stalk does not remove the module's monodromy extensions.

### Averaging over a finite kernel needs an inverse

*Difficulty: Intermediate.*

Take \(H=C_2\to G=\{1\}\), \(R=\mathbb Z\), and the injective abelian group \(I=\mathbb Q/\mathbb Z\), with trivial \(H\)-action. Compute \(H^1(H;I)\). What algebraic hypothesis in (34) is missing?

**Solution.** A degree-one cocycle for a trivial action is a homomorphism \(C_2\to I\), and all degree-one coboundaries are zero. Thus \(H^1(C_2;I)=I[2]\simeq\mathbb Z/2\), nonzero, although \(I\) is injective over \(\mathbb Z\). Injectivity follows from divisibility, or directly from the ideal-extension criterion for \(\mathbb Z\): a map from \(n\mathbb Z\) extends by dividing its value by \(n\). Averaging would require \(1/2\in\mathbb Z\), which is absent. The example is an algebraic restriction test; it does not assert that this finite group is the fundamental group of an aspherical finite-dimensional link manifold.

### Annihilation by one ideal is different from ideal-power torsion

*Difficulty: Intermediate.*

Let \(A=k[t]\), \(J=(t)\), and \(B=A/J=k\). Compare \(\operatorname{Ext}^1_B(k,k)\) with \(\operatorname{Ext}^1_A(k,k)\). Does the category of modules annihilated by \(J\) inherit all its ambient derived morphisms? Does enlarging it to finite modules killed by some power of \(J\) remove this particular obstruction?

**Solution.** The first group is zero because \(B\) is a field. The free resolution
\(0\to A\xrightarrow{t}A\to k\to0\) gives \(\operatorname{Ext}^1_A(k,k)=k\). Its nonzero class is represented by
\(0\to k\to A/(t^2)\to k\to0\), where the first map sends \(1\) to the class of \(t\). The middle module is not annihilated by \(J\). Hence the subcategory of \(B\)-modules is not closed under ambient extensions, and its bounded realization is not full. The larger finite ideal-power-torsion category contains this middle module and the extension. This checks the distinction needed before using a finite-type realization criterion; it does not prove every higher comparison for that larger category.

## Passing from finite cohomology to the finite heart

The fixed-stratification theorem has an unrestricted heart: its stalk modules need not be finite. We now prove the additional comparison for finite stalks. The two mechanisms are different. A Noetherian module calculation produces finite subcomplexes. For constructible sheaves, suitable injectives first make the same finite extraction possible.

The modern reference is Lunts and Schnürer's [*Categories of constructible sheaves*](https://arxiv.org/html/2601.05477v1), including its finite-type variants. The full arguments below retain the distinction between modules annihilated by an ideal and modules annihilated by a power of it. They also spell out faithfulness, where a nullhomotopy must survive the finite replacement.

We use the programme's published [derived-category foundations](https://kokunoyumeto.github.io/open-math-courses-public/courses/derived-categories-and-sheaf-operations/complexes-cones-and-localization.html#4-fractions-at-quasi-isomorphisms) for roofs and common refinements, and [bounded-below injective comparison](https://kokunoyumeto.github.io/open-math-courses-public/courses/derived-categories-and-sheaf-operations/injective-modules-and-bounded-below-derived-functors.html#3-complexes-that-admit-comparison-maps). Those foundations retain their stated human attribution and GFDL terms; their expression is not imported here. All derived categories in the new finite-heart comparisons are bounded.

### A finite subcomplex that retains specified data

Let \(\mathcal A\) be an abelian category, and let \(\mathcal F\subset\mathcal A\) be a Serre subcategory of Noetherian objects. Thus subobjects, quotients and extensions of its objects remain in \(\mathcal F\), and ascending chains of subobjects of each such object stabilize. Suppose the terms of a bounded-below complex \(J\) are directed unions of their subobjects in \(\mathcal F\), and the same is true of their subobjects. Assume \(H^n(J)\in\mathcal F\), with only finitely many nonzero cohomology objects.

We require the following detection property: if a directed union maps epimorphically onto an object of \(\mathcal F\), some member does so. For finite modules this follows by lifting a finite set of generators. For finite-stratum, finite-stalk sheaves it follows by stabilization of the images on one stalk in each stratum. Directedness then combines the finitely many choices.

**Finite extraction lemma.** Every bounded subcomplex \(D\subset J\) with terms in \(\mathcal F\) is contained in a bounded subcomplex \(K\subset J\) with terms in \(\mathcal F\) such that

\[
D\subset K\subset J,\qquad H^n(K)\xrightarrow{\sim}H^n(J)
\quad\text{for every }n.
\tag{36}
\]

**Proof.** Choose \(a\) with \(J^n=0\) for \(n<a\), and choose \(b\) at least as large as the top degree of \(D\) and of the nonzero cohomology of \(J\). In degree \(b\), choose a finite subobject of \(Z^b(J)\) surjecting onto \(H^b(J)\), and add \(D^b\). This still lies in \(Z^b(J)\), because \(D^{b+1}=0\).

Suppose \(K^n\) has been chosen. The object \(K^n\cap B^n(J)\) is finite, by the Serre property. Its preimage under \(J^{n-1}\to B^n(J)\) is a union of finite subobjects. The detection property supplies one whose differential maps onto that intersection. Separately choose a finite subobject of \(Z^{n-1}(J)\) mapping onto \(H^{n-1}(J)\). Add both choices and \(D^{n-1}\) inside the preimage of \(K^n\). Their finite sum is \(K^{n-1}\). The inclusion of \(D^{n-1}\) is allowed because \(dD^{n-1}\subset D^n\subset K^n\).

The new boundaries of \(K\) in degree \(n\) are exactly \(K^n\cap B^n(J)\). Thus the cohomology map in that degree is injective. The previously chosen cycle representatives make it surjective. Descend through the finite interval \(b,b-1,\ldots,a\). In degree \(a\), there are no ambient boundaries, because \(J^{a-1}=0\); surjectivity from the chosen cycles is therefore also injectivity there. Put \(K^n=0\) outside the interval. Above \(b\), both cohomologies vanish. This proves (36). \(\square\)

A useful relative form needs no finite preimage under a quotient: add the specified finite data at each step of this construction. In particular, images of maps from bounded finite complexes, and images of a specified homotopy, can all be retained.

### Finitely generated modules inside all modules

**Proposition.** For a left Noetherian ring \(A\), writing \(\operatorname{mod}_{fg}(A)\) for its finitely generated left modules, inclusion induces

\[
D^b(\operatorname{mod}_{fg}(A))
\xrightarrow{\sim}
D^b_{fg}(\operatorname{Mod}(A)).
\tag{37}
\]

No finite global dimension is required.

**Proof.** Every module is the directed union of its finitely generated submodules. Submodules of finitely generated modules are finitely generated because \(A\) is left Noetherian. Apply (36) to a bounded representative \(C\) with finitely generated cohomology, taking \(D=0\). It gives a bounded finite subcomplex \(K\to C\) that is a quasi-isomorphism, proving essential surjectivity.

For fullness, an ambient morphism between bounded finite complexes is a left roof \(F\leftarrow C\to G\), whose left arrow is a quasi-isomorphism. Its middle complex has finite cohomology. Replace \(C\) by the finite \(K\subset C\) just constructed and restrict both maps. The resulting roof is entirely finite and represents the same morphism.

For faithfulness, take a finite roof whose ambient morphism is zero. The common-refinement and cancellation criterion in the linked foundations supplies a bounded quasi-isomorphism into its middle complex on which its numerator is nullhomotopic. That new middle complex again has finite cohomology. Replace it by a finite subcomplex and restrict the maps and homotopy. The left composite remains a quasi-isomorphism, and the restricted homotopy still kills the numerator. This is a finite witness that the source roof is zero. Differences of two roofs reduce to this case. \(\square\)

### The quotient criterion in its full abelian generality

**Proposition.** Let \(\mathcal B\) be a strictly full abelian subcategory of an abelian category \(\mathcal A\), with exact inclusion, closed under extensions. Suppose every \(M\in\mathcal A\) has a subobject \(N\) such that \(M/N\in\mathcal B\) and \(N\) has no nonzero subobject belonging to \(\mathcal B\). Then

\[
D^b(\mathcal B)\xrightarrow{\sim}D^b_{\mathcal B}(\mathcal A).
\tag{38}
\]

**Proof.** Take a bounded complex \(C\) with cohomology in \(\mathcal B\). Beginning at its lowest degree, let \(t\) be the first degree whose term is not yet in \(\mathcal B\). The boundaries and cycles through this degree belong to \(\mathcal B\). Indeed the bottom boundary is zero; if \(B^i(C)\in\mathcal B\), its extension by \(H^i(C)\) gives \(Z^i(C)\in\mathcal B\), and for \(i<t\) the cokernel of \(Z^i(C)\to C^i\), a map between objects of \(\mathcal B\), gives \(B^{i+1}(C)\in\mathcal B\). Thus \(Z^t(C)\in\mathcal B\).

Choose \(P\subset C^t\) as in the hypothesis. The intersection \(P\cap Z^t(C)\) is the kernel of the map \(Z^t(C)\to C^t/P\). Both its source and target belong to \(\mathcal B\); exact abelian inclusion puts its kernel in \(\mathcal B\). The hypothesis on \(P\) makes that kernel zero. Consequently \(d:P\to dP\) is an isomorphism. Quotient out the acyclic subcomplex

\[
P\xrightarrow{\,d\,}dP
\quad\text{in degrees }t,t+1.
\tag{39}
\]

The quotient has its term of degree \(t\) in \(\mathcal B\), changes no earlier terms, and has the same cohomology. Repeat through the finite degree interval. At the final degree the same argument forces \(P=0\) if it would have a zero outgoing differential. We obtain a quasi-isomorphism \(C\to C'\) with all terms in \(\mathcal B\).

Represent morphisms by right roofs \(F\to C\leftarrow G\). Compose both maps with this quotient replacement. This proves fullness and essential surjectivity. For faithfulness, the right-fraction cancellation criterion represents an ambient zero by a quasi-isomorphism out of the roof's middle complex on which its numerator is nullhomotopic. Apply the same quotient replacement to that complex and compose the homotopy with the quotient. All maps and that homotopy then have terms in \(\mathcal B\), because both their sources and targets do. The resulting right roof is zero already in \(D^b(\mathcal B)\). \(\square\)

This proof does not require arbitrary subobject closure of \(\mathcal B\). The intersection is controlled by a kernel between two of its own objects. That distinction retains the full abelian and extension-closed form of the criterion.

### Ideal-power torsion retains the extensions

Let \(A\) now be commutative Noetherian, let \(J\subset A\) be an ideal, and let \(\mathcal T_J\) consist of finitely generated modules killed by some power of \(J\). This is a Serre subcategory of \(\operatorname{mod}_{fg}(A)\). In an extension, if powers \(J^r\) and \(J^s\) kill the outer terms, then \(J^{r+s}\) kills the middle term.

We reuse the full Artin–Rees proof. That separately licensed Valette component proves the statement for every ideal of every commutative Noetherian ring; it is not restricted to analytic local rings.

For a finite module \(M\), put \(T=\{m:J^rm=0\text{ for some }r\}\). It is a submodule and is finite. A single power \(J^r\) kills it, by taking the maximum of the exponents for finitely many generators. Artin–Rees supplies \(c\) such that

\[
T\cap J^nM=J^{n-c}(T\cap J^cM)=0
\qquad(n\geq c+r).
\tag{40}
\]

Choose \(N=J^nM\) at such a degree. Its quotient is in \(\mathcal T_J\); it has no nonzero \(\mathcal T_J\)-subobject, because every element of such a subobject would lie in \(T\cap N\). Apply (38), then (37), to obtain

\[
D^b(\mathcal T_J)
\xrightarrow{\sim}
D^b_{\mathcal T_J}(\operatorname{Mod}(A)).
\tag{41}
\]

This result is about power torsion. Replacing \(\mathcal T_J\) by the modules annihilated by \(J\) gives a different, generally false assertion, as the earlier \(k[t]\) exercise proves. The extension \(k[t]/(t^2)\) is retained in (41).

### Zero-dimensional support gives a second finite subcategory

For any commutative Noetherian \(A\), let \(\mathcal C\) be the finite modules whose support has dimension zero. Equivalently these are the modules of finite length. Here is the equivalence without an Artinian-ring theorem. Every nonzero finite module has a nonzero element with prime annihilator: choose an annihilator maximal among annihilators of nonzero elements, using the ascending-chain condition. If \(ab\) annihilates the element and \(b\) does not, the nonzero element obtained by multiplication by \(b\) has a larger annihilator containing \(a\); maximality proves primality. Apply this observation successively to quotients to build a prime cyclic filtration. The ascending-chain condition on submodules makes the filtration finite. With zero-dimensional support every prime in it is maximal, so its cyclic factors are simple. Conversely a finite filtration by simple modules has support in its finitely many maximal ideals.

The finite-length modules form a Serre subcategory. In a finite module \(M\), the sum \(T\) of all its finite-length submodules is finite length: the increasing finite sums stabilize by Noetherianity. If \(T=0\), choose \(N=M\) in (38). Otherwise take a composition series of \(T\), and let \(J\) be the product of the annihilator maximal ideals of its factors. The product ideal kills \(T\), by applying the successive annihilators along the filtration. The quotient \(A/J\) has finite length. Indeed, for the successive products, each ideal-layer quotient is a finite module over one of those residue fields, and the ring is Noetherian.

Every \(A/J^n\) has finite length too, by its finite filtration with layers \(J^i/J^{i+1}\), finite over \(A/J\). Artin–Rees gives \(T\cap J^nM=0\) for sufficiently large \(n\). Thus \(N=J^nM\) has finite-length quotient and no nonzero finite-length subobject. Equations (38) and (37) prove

\[
D^b(\mathcal C)\xrightarrow{\sim}
D^b_{\mathcal C}(\operatorname{Mod}(A)).
\tag{42}
\]

This supplies the full zero-dimensional-support comparison, including roofs and their equality, rather than just an object replacement.

### Injectives that remain unions of finite-dimensional modules

Fix a field \(k\). An \(A\)-module is **ind-finite** if it is the union of its finite-dimensional \(A\)-submodules. The required embedding condition says that every ind-finite module embeds in an injective \(A\)-module that is itself ind-finite. We prove this condition for every finitely generated commutative \(k\)-algebra.

**Proposition.** Let \(A\) be a finitely generated commutative \(k\)-algebra. For any injective \(A\)-module \(E\), the submodule

\[
\Gamma_{ft}(E)=\{e\in E:\dim_k(Ae)<\infty\}
\tag{43}
\]

is injective. Consequently the required ind-finite injective embeddings exist.

**Proof.** A sum of two finite-dimensional cyclic submodules is finite, so (43) is a submodule and is ind-finite. The Hilbert basis theorem, proved in the linked Artin–Rees component, makes \(A\) Noetherian.

Use [Baer's criterion](https://kokunoyumeto.github.io/open-math-courses-public/courses/derived-categories-and-sheaf-operations/injective-modules-and-bounded-below-derived-functors.html#2-functorial-injective-embeddings), with its full ideal-extension proof. Let \(L\subset A\) be an ideal and \(f:L\to\Gamma_{ft}(E)\) a map. The ideal has finitely many generators; their images lie in a single finite-dimensional submodule. Hence the image of \(f\) is annihilated by a finite-codimensional ideal \(J\): take its annihilator, since its action factors through its finite-dimensional endomorphism algebra. Artin–Rees for \(L\subset A\) gives, for some \(n\),

\[
L\cap J^n\subset JL\subset\ker f.
\tag{44}
\]

The map therefore descends to \((L+J^n)/J^n\subset A/J^n\). Injectivity of \(E\) extends it to \(A/J^n\to E\). If \(y\) is the image of one, then \(J^ny=0\), and multiplication by \(y\) extends \(f\) to \(A\).

This extension lands in (43): \(A/J^n\) is finite-dimensional. To check that assertion, \(J\) is finitely generated, and every layer \(J^i/J^{i+1}\) is a finite module over the finite-dimensional algebra \(A/J\). A finite filtration of \(A/J^n\) by those layers proves the assertion. Baer's criterion now proves injectivity.

For an ind-finite module \(M\), take the coinduced injective \(E=\operatorname{Hom}_k(A,M)\), with \((a\varphi)(b)=\varphi(ba)\). The adjunction \(\operatorname{Hom}_A(-,E)=\operatorname{Hom}_k(-,M)\) makes it injective because vector spaces are injective. The map

\[
M\longrightarrow E,\qquad m\longmapsto (b\longmapsto bm)
\tag{45}
\]

is linear and monic, as evaluation at one recovers \(m\). Its image is ind-finite, so it lies in \(\Gamma_{ft}(E)\). This gives the required embedding. \(\square\)

This is a direct Artin–Rees and Baer proof of the needed condition. It avoids requiring a classification of indecomposable injective modules as an additional prerequisite. The classical torsion-injectivity comparison is also present in the [AI Integrated Stacks Project](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/dualizing.tex#L335); that mathematical reference retains the Stacks project authors' credit and its own reuse terms.

### Finite extraction for constructible sheaves

The relevant source is Lunts–Schnürer, Theorem 7.13 and Corollaries 7.14–7.15, pp. 34–36. It obtains finite terms by first embedding unions of finite-dimensional objects into injectives of the same kind and then extracting a finite subcomplex. The course argument retains specified maps and homotopies during extraction, and supplies the commutative-algebra injective step through Artin–Rees and Baer's criterion. These are necessary finite-heart steps; finite cohomology in an unrestricted heart alone does not imply finite-term realization. Earlier ideal-power torsion statements retain exactly their stated extension-closed categories.

Let \((Y,\mathcal S)\) have a finite normal stratification as in (31): connected manifold strata, compatible ball-cone neighborhoods, and finitely many connected components in each incident link piece. Work over a field \(k\). Write \(\mathcal A=\operatorname{Cons}_k(Y,\mathcal S)\), \(\mathcal F=\operatorname{Cons}_{ft,k}(Y,\mathcal S)\), and let \(\mathcal I\) be the objects whose stratum monodromy modules are ind-finite. Assume each group algebra \(k[\pi_1(S)]\) has the ind-finite injective embedding condition.

The finite-stalk category \(\mathcal F\) is Serre inside \(\mathcal A\): restriction is exact, kernels and quotients of finite-dimensional vector spaces are finite, and an extension adds the two dimensions. Its objects are Noetherian: an ascending sequence of constructible subobjects stabilizes on a chosen stalk in each of the finitely many connected strata, hence everywhere.

For a stratum inclusion \(s:S\hookrightarrow Y\), ordinary \(s_*\) carries finite local systems to finite-stalk sheaves. The boundary stalk is \(H^0(L_{x,S};L)\); its dimension is at most the sum of the stalk dimensions over the finitely many connected link components. For an ind-finite local system, this stalk is a union of the \(H^0\) groups of finite sub-local-systems. A section is determined by an invariant vector on each component, and finitely many such vectors lie together in a finite-dimensional monodromy submodule. Invariance is preserved inside that submodule. Consequently \(s_*\) carries an ind-finite local system to a union of finite-stalk constructible subsheaves.

Every \(G\in\mathcal I\) is itself a union of finite-stalk subsheaves. The adjunction diagonal embeds it into \(\bigoplus_Ss_*(G|_S)\), by the same stalkwise argument as (26). Each summand is a directed union of finite-stalk sheaves by the preceding calculation. Intersect \(G\) with those finite stages. Each intersection is constructible and finite-stalk, and their union is \(G\). This argument supplies actual lifts across the attachments; merely declaring that a quotient has smaller support would not supply them.

The embedding condition on the group algebras gives injective ind-finite local systems \(I_S\) containing \(G|_S\). Therefore

\[
G\hookrightarrow \bigoplus_{S\in\mathcal S}s_*I_S
\quad\text{is an embedding into an injective object of }\mathcal A
\text{ belonging to }\mathcal I.
\tag{46}
\]

Adjunction to exact restriction makes each summand injective; the sum is finite. Ind-finite monodromy modules are closed under submodules and quotients. The embedding condition also proves extension closure: embed the submodule of an extension into an ind-finite injective, extend that map across the middle module, and combine it with the quotient map. This embeds the middle module in the sum of that injective and the ind-finite quotient. Thus \(\mathcal I\) is a Serre subcategory and (46) can be iterated on cokernels.

The published bounded-below resolution construction applies within \(\mathcal I\) while keeping the terms injective in \(\mathcal A\). In its one-degree pushout step, direct sums and quotients remain in \(\mathcal I\). Each degree stabilizes after finitely many steps, so no additional infinite-limit assertion is required. Every bounded complex in \(\mathcal I\) therefore has a quasi-isomorphism to a bounded-below complex of \(\mathcal A\)-injectives in \(\mathcal I\).

**Finite-heart theorem.** Under these conditions, inclusion induces

\[
D^b(\mathcal F)\xrightarrow{\sim}D^b_{ft}(\mathcal A).
\tag{47}
\]

**Proof.** First consider \(F,G\in\mathcal F\) and all their shifts. Choose a bounded-below injective resolution \(G[m]\to J\) as above. Its cohomology is bounded and finite-stalk. Every morphism \(F\to G[m]\) in the ambient derived category is represented by a chain map \(f:F\to J\), using the published K-injective comparison.

The images of \(f\) and \(G[m]\to J\) form a bounded finite subcomplex \(D\subset J\). The hypotheses of (36) hold: all terms and subobjects are unions of finite-stalk subsheaves, as proved above, and a finite-stalk quotient is detected at finitely many stratum stalks. Obtain a finite bounded \(K\subset J\) containing \(D\). The resulting right roof \(F\to K\leftarrow G[m]\) realizes the prescribed morphism. This proves fullness on shifted heart objects.

For faithfulness, take a finite right roof \(F\to K\leftarrow G[m]\) with ambient value zero. Resolve its finite middle complex by \(q:K\to J\) with \(J\) as above. The numerator into \(J\) is nullhomotopic, by the K-injective comparison. Include in \(D\) the images of \(q(K)\) and of every component of that homotopy. Close under the differential. There are only finitely many such degrees because \(F\) and \(K\) are bounded; all these images and their finite sums are finite-stalk. Apply (36) retaining this \(D\). The map \(K\to K'\subset J\) is a quasi-isomorphism, and the same homotopy has values in \(K'\). Thus the roof is zero in \(D^b(\mathcal F)\). This proves injectivity of Hom, rather than just lifting its elements.

Finite cohomology truncation triangles generate all bounded objects from shifted heart objects. Apply the two long exact Hom sequences and finite induction on their amplitudes: the heart Hom comparison just proved implies full faithfulness on every bounded pair. Essential surjectivity follows by the same finite truncation induction. Realize each cohomology object in \(\mathcal F\); lift the connecting morphism using full faithfulness; its cone realizes the next truncation. The finite number of cohomological degrees terminates the construction. \(\square\)

If the unrestricted fixed-stratification realization criterion also holds, compose (47) with its finite-cohomology restriction to obtain the ambient finite-stalk sheaf equivalence. Equation (47) itself does not assume that boundary comparison.

### Finitely generated abelian monodromy and the finite projective-line theorem

For a finitely generated abelian group \(G\), the algebra \(k[G]\) is a finitely generated commutative \(k\)-algebra: use finitely many group generators and their inverses as algebra generators. Equations (43)–(45) verify the embedding condition. Thus for a finite normal stratification with such stratum groups,

\[
D^b(\operatorname{Cons}_{ft,k}(Y,\mathcal S))
\xrightarrow{\sim}
D^b_{ft}(\operatorname{Cons}_k(Y,\mathcal S)).
\tag{48}
\]

No semisimplicity of \(k[G]\) or finite global dimension of that algebra is required.

For the three torus-orbit strata of \(\mathbb P^1(\mathbb C)\), the groups are \(\mathbb Z,0,0\). The unrestricted realization was proved in (35). Combining it with (48) now proves the previously separate finite-heart statement:

\[
D^b(\operatorname{Cons}_{ft,k}(\mathbb P^1,\{\mathbb C^*,0,\infty\}))
\xrightarrow{\sim}
D^b_{\{\mathbb C^*,0,\infty\},ft}(\mathbb P^1;k).
\tag{49}
\]

It holds over every field. The general normal toric-variety application still needs its full orbit-star cone geometry and link-map calculation, beyond the explicit projective line. The finite-heart step for its finitely generated abelian stratum groups is now supplied by (48).

## Further exercises on finite terms and derived equality

### Two nilpotent extensions retain a degree-two class

*Difficulty: Advanced.*

Let \(A=k[x,y]\), \(J=(x,y)\), \(M_x=A/(x^2,y)\), \(M_y=A/(x,y^2)\). Show that the sequence \(0\to k\to M_x\to M_y\to k\to0\), whose middle map sends \(1\) to \(y\), represents a nonzero ambient degree-two class. Explain why ideal-power torsion retains it while modules annihilated by \(J\) lose it.

**Solution.** The first map sends \(1\) to \(x\); the last is the residue quotient. The middle map is linear because \(x^2y=0\) and \(y^2=0\) in \(M_y\). Its kernel is \(kx\) and image is \(ky\), proving exactness. The Koszul free resolution of \(k\) has differentials \(A^2\to A\), \((a,b)\mapsto xa+yb\), and \(A\to A^2\), \(c\mapsto(-yc,xc)\). Exactness follows because a relation \(xa+yb=0\) has \(b=xc\) and \(a=-yc\) in the polynomial ring. Applying Hom into \(k\) gives zero differentials, so \(\operatorname{Ext}^2_A(k,k)=k\).

Lift \(1\in A\) to \(1\in M_y\). The first Koszul differential then has values \(0,y\). Lift those through \(M_x\to M_y\) by \(0,1\). On the second differential this lift gives \(-y\cdot0+x\cdot1=x\), which is the image of \(1\in k\). Thus the extension represents the nonzero scalar \(1\), including the chosen sign. Both middle terms are killed by \(J^2\), so the entire two-extension belongs to \(\mathcal T_J\). Modules annihilated by \(J\) are vector spaces over \(A/J=k\) and have no degree-two extensions. The power-torsion category in (41) retains the actual middle terms.

### Finite coefficients may need infinite injective resolutions

*Difficulty: Intermediate.*

Prove that no nonzero finite-dimensional \(k[t,t^{-1}]\)-module is injective in the category of all modules. Explain how this is compatible with (48).

**Solution.** A finite-dimensional module \(V\) has a nonzero annihilating polynomial \(p(t)\), because the powers of its endomorphism \(t\) are linearly dependent. In the Laurent ring this polynomial is nonzero. A nonzero injective module over this domain is divisible by \(p\): for any \(v\), the map from the ideal \(pA\) sending \(pa\) to \(av\) extends to \(A\), and its value \(w\) at one satisfies \(pw=v\). On \(V\), however, multiplication by \(p\) is zero. Surjectivity then forces \(V=0\). Equations (46) and (47) use injectives that are unions of finite-dimensional submodules, usually infinite-dimensional themselves. Finite extraction retains the bounded object, its morphisms and homotopies; it does not require finite-dimensional injective terms.

### A nullhomotopy requires more than the image of its map

*Difficulty: Intermediate.*

Let \(J\) be \(k\xrightarrow{\mathrm{id}}k\) in degrees \(-1,0\), and let \(F=k[0]\). The map \(F\to J\) is identity in degree zero. Show why retaining only its image cannot witness its ambient vanishing, and construct the finite witness.

**Solution.** The image alone is the subcomplex \(k[0]\subset J\), with nonzero \(H^0\). The map to that image is identity, so is not zero in its derived category. The homotopy into \(J\) has component \(h^0:F^0\to J^{-1}\) equal to identity; then \(dh+hd\) is the original map. Add that degree-\(-1\) image. The resulting finite subcomplex is all of \(J\), contractible by this same homotopy. Thus the map vanishes there. This is why faithfulness in (47) explicitly retains homotopy images, rather than stopping after fullness.

### Abelian monodromy does not imply a semisimple group algebra

*Difficulty: Advanced.*

Let \(\operatorname{char}k=p>0\) and \(G=C_p\). Compute the positive self-extensions of its trivial representation. Does the algebraic embedding argument for (48) require their vanishing?

**Solution.** Write \(A=k[G]=k[z]/(z^p)\), with \(z=g-1\). A free resolution of \(k=A/(z)\) alternates multiplication by \(z\) and \(z^{p-1}\). Their kernels are respectively \(z^{p-1}A\) and \(zA\), so the resolution is exact, including \(p=2\), when both maps are \(z\). Applying \(\operatorname{Hom}_A(-,k)\) makes every differential zero. Hence \(\operatorname{Ext}^n_A(k,k)=k\) for all \(n\geq0\). The algebra is nevertheless finitely generated and commutative, so (43)–(45) apply. The finite-heart comparison preserves these classes; it does not assert their vanishing. This example concerns the algebraic embedding condition, without asserting that this group occurs as an aspherical finite-dimensional manifold's fundamental group.

## Normal toric orbit stratifications in full generality

The projective line was one example. We now prove the realization theorem for every complex normal separated toric variety of finite type, with its orbit stratification and classical topology. Singular and nonsimplicial cones are included. Global projectivity and smoothness are unnecessary.

The references are Lunts and Schnürer's [Proposition 6.11 and Corollary 7.15](https://arxiv.org/html/2601.05477v1#S6.Thmtheorem11), Simon Telen's [*Introduction to Toric Geometry*](https://arxiv.org/html/2203.01690v1), and Hideyasu Sumihiro's [*Equivariant completion*](https://projecteuclid.org/download/pdf_1/euclid.kjm/1250523277), Theorem 1, Lemma 8 and Corollary 2, printed pp. 5–9. Their mathematical credit is retained. The proof below expands the toric specialization directly, including the affine-complement step left unstated in Sumihiro's Lemma 7.

Write *N* for the cocharacter lattice of the dense torus and *M* for its dual character lattice. A monomial character carries its character-lattice exponent; a real subscript means tensoring the lattice with the real numbers.

The geometry is local. First prove invariant affine neighborhoods, then classify their normal coordinate monoids and construct actual compatible cone neighborhoods. This supplies the theorem without importing a global fan-classification theorem as an unproved prerequisite. The product belongs to the orbit star; the entire variety need not be a product with that orbit.

Let \(X\) be an irreducible normal separated complex algebraic variety of finite type, with a dense open torus \(T=(\mathbb C^*)^n\) whose multiplication extends to an algebraic action on \(X\). We prove that every point has a \(T\)-invariant affine open neighborhood. This is the missing local input for the full toric orbit-stratification argument; a global reconstruction of the fan is unnecessary.

### Normality and poles, with the needed algebra supplied

We use the already written Hilbert basis and Artin–Rees proofs in the separately licensed analytic-finiteness component, and the finite prime cyclic filtration proved in the finite-heart argument above. Both preserve their exact Noetherian hypotheses.

Here are the additional normal-domain facts. If \(R\) is a Noetherian local domain and \(a\) belongs to its maximal ideal, then

\[
\bigcap_{r\geq 0}a^rR=0.
\tag{50}
\]

Indeed the intersection \(Q\) is a finitely generated ideal. Artin–Rees for \(Q\subset R\) gives \(Q=aQ\). On finitely many generators, that equality gives a matrix relation with matrix \(I-aB\); its determinant is a unit and its adjugate kills the generators. Hence \(Q=0\). This is also the finite-module Nakayama argument, with the determinant made explicit.

Consequently, if a nonzero maximal ideal of a Noetherian local domain is principal, say \((c)\), then every nonzero element is \(c^r u\) for a finite \(r\) and a unit \(u\). Repeated division stops by (50). Every nonzero prime then contains \(c\) and equals the maximal ideal. Such a local domain has dimension one.

We shall use one other determinant argument. If \(z\) belongs to the fraction field of a domain and \(zI\subset I\) for a nonzero finitely generated ideal \(I\), express multiplication by \(z\) on finitely many generators of \(I\) by a matrix over the ring. Its characteristic polynomial kills those generators. A nonzero generator is faithful in a domain, so the monic polynomial vanishes at \(z\). Thus \(z\) is integral.

Let \(A\) be a Noetherian integrally closed domain with fraction field \(K\). Its localizations are integrally closed: clearing the finitely many coefficient denominators of a monic integral equation shows that a suitable denominator times its root is integral over \(A\), hence lies in \(A\). We claim

\[
A=\bigcap_{\operatorname{ht}\mathfrak p=1}A_{\mathfrak p}
\quad\text{inside }K.
\tag{51}
\]

To prove this, write \(z=b/a\notin A\), with \(a\ne0\). In the cyclic submodule generated by the nonzero class of \(b\) in \(A/aA\), choose a nonzero element whose annihilator is maximal among these annihilators. Noetherianity permits the choice. Its annihilator \(\mathfrak p\) is prime: if \(uv\) kills the element but \(v\) does not, the nonzero element multiplied by \(v\) has annihilator containing the original one and \(u\), so maximality forces \(u\) into it. The chosen element is the class of \(db\), for some \(d\in A\).

Set \(y=db/a\). Its denominator ideal is exactly \(\mathfrak p\); in particular \(a\in\mathfrak p\) and \(y\notin A_{\mathfrak p}\). In \(R=A_{\mathfrak p}\), with maximal ideal \(\mathfrak m\), we have \(y\mathfrak m\subset R\). If \(y\mathfrak m\subset\mathfrak m\), the determinant argument would make \(y\) integral and hence an element of the normal ring \(R\), a contradiction. Therefore some \(c\in\mathfrak m\) has \(yc\) a unit. For every \(d'\in\mathfrak m\),

\[
d'=c\,\frac{yd'}{yc}.
\]

Thus \(\mathfrak m=(c)\), and the preceding principal-maximal-ideal argument gives \(\dim R=1\). We have found a height-one \(\mathfrak p\) at which \(y\), and hence \(z\), is not regular. This proves (51).

A one-dimensional Noetherian normal local domain is a discrete valuation ring. To see the remaining point directly, take \(0\ne a\in\mathfrak m\). All primes in the support of \(R/aR\) are the maximal ideal, so the finite prime cyclic filtration makes this quotient finite length. It has a nonzero element with annihilator \(\mathfrak m\). Choose its representative \(b\notin aR\), and put \(y=b/a\). Again \(y\mathfrak m\subset R\), and normality and the determinant argument force an element \(c\in\mathfrak m\) with \(yc\) a unit. Thus \(\mathfrak m=(c)\). Formula (50) supplies a finite exponent for every nonzero element, so its exponent of \(c\) is the discrete valuation.

These proofs justify the pole criterion: on a normal variety, a rational function is regular precisely when it has no negative valuation at any prime divisor of each affine chart. They also justify extension across a closed subset of codimension at least two. On any affine chart, every height-one point is outside that subset; apply (51). Uniqueness follows from the dense open set.

For a Cartier divisor \(D\), the same argument identifies the sections of \(\mathcal O_X(D)\) with the rational functions \(f\) satisfying \(\operatorname{div}(f)+D\geq0\). Trivialize \(D\) locally and apply (51); inequalities alone would be insufficient without normality.

### The boundary of an affine open is divisorial

Let \(U_0\subset X\) be a nonempty affine open. Its complement has only codimension-one irreducible components. Suppose a component \(C\) had codimension at least two. Remove all the other components of the complement to obtain an open neighborhood \(V\) of the generic point of \(C\); here \(V\setminus U_0\) has codimension at least two.

Each of the finitely many coordinate generators of \(\mathbb C[U_0]\) extends from \(V\cap U_0\) to \(V\) by the preceding pole criterion. Their equations continue to hold, since they hold on a dense open set. They define a morphism \(V\to U_0\). Its composite with \(U_0\hookrightarrow X\) equals the inclusion on \(V\cap U_0\). Since \(X\) is separated, equality holds everywhere: the inverse image of its closed diagonal contains a dense open set. Its image would therefore put all of \(V\) in \(U_0\), a contradiction.

Give the finitely many boundary prime divisors positive multiplicities. We obtain an effective Weil divisor \(D\) with

\[
X\setminus\operatorname{Supp}D=U_0.
\tag{52}
\]

If \(U_0=X\), use \(D=0\). No assumption that \(D\) is already Cartier is made.

### The torus fixes divisor classes

The Laurent polynomial ring \(\mathbb C[t_1^{\pm1},\ldots,t_n^{\pm1}]\) is a unique factorization domain. For completeness, the polynomial-ring assertion follows inductively from Gauss's lemma: reducing coefficients modulo a prime factor proves that the product of primitive polynomials is primitive; factorization over the fraction field can then be cleared of content, giving existence and uniqueness over a factorial coefficient ring. Begin with the field, where the one-variable Euclidean algorithm supplies factorization. Inverting the variables preserves the remaining prime factorizations.

Thus the restriction to \(T\) of any Weil divisor on \(X\) is principal. Subtract that principal divisor on \(X\). The resulting divisor is supported on the finitely many codimension-one components of \(X\setminus T\). Each such component is \(T\)-invariant: the connected torus cannot permute a finite collection nontrivially. One can see this without a discreteness assumption on the permutation map: the image of the irreducible space \(T\times E\), for a boundary component \(E\), has irreducible closure in the finite union of those components and contains \(E\), so it remains in \(E\); translation is invertible.

Every divisor class therefore has a representative fixed by \(T\). In particular,

\[
tD\sim D\qquad(t\in T),
\tag{53}
\]

where \(\sim\) denotes linear equivalence, not merely algebraic or rational equivalence of arbitrary-dimensional cycles.

### Affine-complement divisors produce a projective embedding

We need the full elementary statement used as Lemma 7 in Sumihiro.

**Lemma.** Let \(V\) be a normal separated variety. Suppose finitely many effective Weil divisors \(D_i\), linearly equivalent to \(D\), have affine complements \(V_i=V\setminus\operatorname{Supp}D_i\) covering \(V\). Then \(V\) is quasi-projective.

**Proof.** At a point in \(V_i\), the divisor \(D_i\) is zero locally. Linear equivalence makes \(D\) principal there. On overlaps the two local equations have quotient with divisor zero; the pole criterion applies to that quotient and its inverse, so their quotient is a regular unit. Hence \(D\) and all \(D_i\) are Cartier everywhere. Let \(s_i\) be the corresponding sections of \(\mathcal O_V(D)\), so \(V_i=\{s_i\ne0\}\).

Choose finitely many coordinate generators \(g_{ij}\) of each affine \(V_i\). As rational functions on \(V\), they can have poles only on the finitely many prime components of \(D_i\). The pole criterion therefore supplies an integer \(N\geq1\), common to all \(i,j\), such that

\[
s_i^N,\qquad g_{ij}s_i^N,\qquad s_k s_i^{N-1}
\tag{54}
\]

are global sections of \(\mathcal O_V(ND)\). For the middle sections, increase \(N\) beyond every negative valuation divided by its positive multiplicity in \(D_i\); for the others they are products of global sections. There are finitely many choices.

These sections have no common zero, because the \(V_i\) cover. They give a morphism to a finite-dimensional projective space. The inverse image of the standard affine chart for coordinate \(s_i^N\) is exactly \(V_i\). The coordinate ratios on this chart include every \(g_{ij}\); all the other ratios are regular functions on \(V_i\). Consequently this chart map is a closed immersion: its coordinate-ring map is surjective because it contains the chosen algebra generators. On the union of those projective affine charts the morphism is a closed immersion, since being a closed immersion is local on the target and these charts cover the image. This union is open in projective space. We have a locally closed projective immersion, proving the lemma. \(\square\)

Apply the lemma to the toric variety as follows. Fix \(x\in U_0\) and put

\[
U=\bigcup_{t\in T}tU_0.
\tag{55}
\]

This is an invariant open neighborhood of the entire orbit of \(x\). It contains \(T\), since \(U_0\) meets that dense orbit. A Noetherian open is quasi-compact, so finitely many translates \(t_iU_0\) cover \(U\). The divisors \(t_iD|_U\) have these affine complements and are linearly equivalent by (53). The lemma makes \(U\) quasi-projective. This proves the toric specialization of Sumihiro's Lemma 8 with its formerly unstated affine-complement step supplied.

### Monomial sections make the embedding equivariant

Let \(U\) now be this normal quasi-projective invariant neighborhood, still with dense torus \(T\). Choose a projective locally closed embedding and a very ample Cartier divisor \(H\) on \(U\), with finitely many sections that realize that embedding. Since the Laurent ring is factorial, choose \(f\in\mathbb C(T)^*\) with

\[
H_0=H-\operatorname{div}(f)
\quad\text{supported on }U\setminus T.
\tag{56}
\]

The divisor \(H_0\) is Cartier and \(T\)-invariant. Multiplication by \(f\) identifies the sections for \(H\) with those for \(H_0\). Every section for \(H_0\), represented as a rational function, is regular on \(T\); it is a finite Laurent polynomial there.

The space of such sections is preserved by torus translation, because \(H_0\) is invariant and translations preserve its divisor inequalities. If a section has finitely many monomial weights, each individual monomial is itself a section. Indeed distinct Laurent characters are linearly independent. Choose sufficiently many torus elements so that their character evaluation matrix has full rank; otherwise a nonzero linear combination of the characters would vanish everywhere on \(T\), contradicting this independence. Linear combinations of those translates isolate each weight component. They remain sections.

For all the finitely many original embedding sections, take all their monomial components. Their span \(W\) is finite-dimensional, \(T\)-stable, and contains the original sections. It still has no base point and still gives a locally closed immersion

\[
U\hookrightarrow\mathbb P(W^*).
\tag{57}
\]

To check the last assertion, choose a basis of \(W\) beginning with a basis of the old section space. On a chart where one of those old sections is nonzero, projection to the old coordinate ratios is defined. Those ratios already realize the old locally closed immersion; the additional ratios are regular functions on its image and give their graph. A graph into an affine space is closed over that image. The old nonvanishing charts cover \(U\), so the added sections preserve the immersion.

Use the pullback action \((t\cdot s)(y)=s(t^{-1}y)\) on sections and its dual action on \(W^*\). A monomial section \(\chi^m\) has section weight \(\chi^m(t)^{-1}\), and its evaluation coordinate has weight \(\chi^m(t)\). The action is therefore diagonal and (57) is equivariant; equality on the dense torus extends to \(U\). We have proved the needed toric specialization of Sumihiro's Theorem 1 without the general-group invertible-function or cocycle primitives.

### A semi-invariant equation gives the invariant affine open

Let \(Y\) be the projective closure of the image of \(U\) in (57), and let \(B=Y\setminus U\), a closed invariant subset. If \(B\ne\varnothing\), take a homogeneous polynomial vanishing on \(B\) but not at the given point \(x\). Such a polynomial exists by the definition of a projective closed subset and \(x\notin B\). Its finite-dimensional homogeneous degree space decomposes into torus weights. Since the homogeneous ideal of \(B\) is invariant, the same translate-and-project argument puts each weight component in that ideal. At least one component \(F\) is nonzero at \(x\).

If \(B\) is empty, instead take any projective coordinate nonzero at \(x\) and then choose a nonzero weight component; the vanishing-on-boundary condition is vacuous. In either case \(F\) is homogeneous of positive degree and semi-invariant. Therefore

\[
V_x=Y\cap\{F\ne0\}\subset U
\tag{58}
\]

is invariant and contains \(x\). It is affine. Under the Veronese embedding of degree \(\deg F\), \(F\) becomes a linear homogeneous coordinate; its nonvanishing locus is a standard affine projective chart, and \(Y\) intersects it in a closed affine subvariety. If \(U\) is a point the assertion is immediate, so no positive-dimensional coordinate exception is needed.

Thus every point of the original normal separated toric variety has an invariant affine open neighborhood. The proof uses normality for the pole extension and divisor-to-section steps, separatedness for the boundary lemma, finite type for Noetherianity, and the dense torus for factorial Laurent functions and finite weight spaces. None of these hypotheses has been dropped.

### From an invariant affine chart to its rational cone

Let \(U \subset  X\) be a nonempty invariant affine open supplied by the preceding affine-neighborhood theorem. It contains the dense torus: it meets the torus, and invariance makes the intersection the entire transitive torus orbit. Restriction to the dense torus embeds the coordinate algebra \(A=\mathbb C[U]\) in the Laurent algebra \(\mathbb C[M]\); both have the same fraction field because the torus is dense open. \(A\) is a finitely generated normal domain.

The regular torus action has a coordinate coaction \(A\to \mathbb C[M]\otimes A\). If the restriction of \(f\in A\) to the torus is the Laurent sum \(\sum c_m \chi^m\), the coefficient of \(\chi^m\) in this coaction restricts to \(c_m \chi^m\) on the dense torus. Linear independence of Laurent characters and injectivity of restriction show that every such component lies in \(A\). Hence \(A\) is a direct sum of one-dimensional monomial weight spaces. Define \(S={m\in M:\chi^m\in A}\). Multiplication gives closure under addition and \(0\in S\), and

\[
A=\mathbb C[S].
\tag{59}
\]

Choose finitely many algebra generators of \(A\) and collect the finitely many monomials occurring in their Laurent expansions. All these monomials lie in \(A\), so they generate it as an algebra; linear independence shows their exponents generate \(S\) as a monoid. This proves finite monoid generation without assuming an affine toric classification.

Moreover \(\mathbb Z S=M\). For any \(m\in M\), express \(\chi^m=f/g\) in the common fraction field with nonzero \(f,g\in \mathbb C[S]\). Choosing a monomial exponent \(n\) with nonzero coefficient in \(g\), the equality \(\chi^m g=f\) implies \(n+m\in S\). Hence \(m=(n+m)-n\) belongs to \(\mathbb Z S\). If \(a m\in S\) for a positive integer \(a\), then \(\chi^m\) is in the fraction field and satisfies the monic equation \(Y^a-\chi^{am}=0\) over \(A\). Normality gives \(\chi^m\in A\), so \(m\in S\). Thus \(S\) is saturated in the full torus character lattice \(M\).

Let \(C=\operatorname{cone}_{\mathbb R}(S)\). It is rational polyhedral by finite generation, and spans \(M_{\mathbb R}\) because \(\mathbb Z S=M\). For any \(m\in C\cap M\), an expression as a nonnegative real combination of the integral generators can be chosen rational: discard a linear dependence while preserving nonnegativity until the used vectors are linearly independent, then solve their rational linear system. After clearing denominators, \(a m\in S\) for some positive integer \(a\); saturation gives \(m\in S\). Consequently

\[
S=C\cap M=\sigma^\vee\cap M,
\qquad \sigma=C^\vee\subset N_\mathbb R.
\tag{60}
\]

Polyhedral duality makes \(\sigma\) rational, and the fact that \(C\) spans \(M_{\mathbb R}\) makes \(\sigma\) strongly convex. This proves \(U\cong U_\sigma\), including its torus action. It imposes no full-dimensionality, simpliciality, or smoothness on \(\sigma\). A point \(x\in U_\sigma\) belongs to a unique orbit \(O(\tau)\) by the orbit-face calculation below. Localizing as in (75) replaces the chart by \(U_\tau\), where \(O(\tau)\) is the unique closed orbit. Rename that cone \(\sigma\) for the ensuing product and link calculation. This supplies precisely the affine model used there.

The elementary polyhedral calculations just used can also be proved directly. A finitely generated cone is closed: eliminate a linear dependence among a nonnegative expression by subtracting a suitable multiple of that dependence until one coefficient is zero. Repeating leaves linearly independent generators. Hence the cone is a finite union of cones on independent subsets, each closed in its linear span. If \(x\) is outside a closed cone \(C\), let \(q\in C\) minimize its Euclidean distance to \(x\). Convexity gives \(\langle q-x,c-q\rangle \ge 0\) for every \(c\in C\); using \(c=0,2q\) gives \(\langle q-x,q\rangle =0\). Thus the functional \(q-x\) is nonnegative on \(C\) and strictly negative on \(x\). This proves \(C^{\vee\vee}=C\).

To see finite rational generation of a dual, start with \(\mathbb R^n=\operatorname{cone}(\pm e_i)\) and impose the finite rational inequalities one at a time. Suppose a current cone is generated by \(v_i\), and impose \(l\ge 0\). Retain generators with \(l(v_i)\ge 0\) and add, for every positive/negative pair, the zero-level vector

\[
l(v_i)v_j-l(v_j)v_i\qquad(l(v_i)>0>l(v_j)).
\]

These generate the intersection. In a nonnegative expression satisfying \(l\ge 0\), distribute the positive \(l\)-mass to cancel the negative \(l\)-mass in pairs; the canceled pairs give exactly these vectors and the remainder uses the retained nonnegative generators. All generators stay rational, and denominators may be cleared. This proves rational polyhedral duality without a Minkowski–Weyl theorem as a hidden import.

For the face calculations below, take a relative interior point \(u\) of a cone defined by finitely many generator inequalities. Its face is cut out by those inequalities that vanish at \(u\): a small displacement in their common kernel still satisfies every other, strict, inequality. Therefore that kernel is the span of the face, and the active generators span its annihilator. This proves the dual-face description and its dimension. Exposing functionals for rational faces may be chosen rational by solving the vanishing rational linear equations and approximating while preserving the finitely many strict inequalities; multiplication clears denominators. Finally, the sum of a set of nonzero integral cone generators spanning the cone lies in its relative interior, which supplies the integral interior points used later.

### The saturated lattice product at an orbit

Put

\[
N_\sigma=N\cap\operatorname{span}_{\mathbb R}\sigma,
\qquad k=\dim\sigma.
\]

This lattice is saturated in \(N\): if \(a n \in  N_\sigma\) for a nonzero integer \(a\), then \(n\) belongs to the same real span. Thus \(N/N_\sigma\) is torsion free. A saturated subgroup of a finite free lattice splits. To prove this, divide any nonzero vector in the subgroup by the gcd of its coordinates; saturation keeps that primitive vector in the subgroup. Euclidean integer row operations send it to the first basis vector, so it extends to a basis of the ambient lattice. Subtracting its coordinate splits off this rank-one subgroup. The intersection with the complementary lattice remains saturated. Repeat by induction on the subgroup rank. Thus there is a complement \(N^c\) and a decomposition

\[
N=N_\sigma\oplus N^c.
\tag{61}
\]

This is a split of lattices, not a choice of a basis among ray generators. In a singular cone those rays need not generate the saturated lattice, and using their lattice instead would insert an unnecessary finite quotient.

Let \(M_\sigma = \operatorname{Hom}(N_\sigma,\mathbb Z)\) and \(M^c = \operatorname{Hom}(N^c,\mathbb Z)\), extended to \(N\) by zero on the other factor. Since \(\sigma\) lies in \((N_\sigma)_{\mathbb R}\),

\[
\sigma^\vee\cap M
=\bigl(\sigma^\vee_{N_\sigma}\cap M_\sigma\bigr)\oplus M^c.
\]

Writing \(S' = \sigma^\vee_{N_\sigma} \cap  M_\sigma\) gives the actual algebra and variety maps

\[
\mathbb C[\sigma^\vee\cap M]
\cong \mathbb C[S']\otimes_\mathbb C\mathbb C[M^c],
\qquad
\chi^{m'+m^c}\longmapsto\chi^{m'}\otimes\chi^{m^c},
\]

\[
U_\sigma\cong X'\times T_{N^c},
\qquad X'=\operatorname{Spec}\mathbb C[S'].
\tag{62}
\]

The cone \(\sigma\) is full dimensional in \((N_\sigma)_{\mathbb R}\). Its dual there is pointed, so the monoid map \(S'\to\mathbb C\), equal to one at zero and zero at every other monoid element, defines a point \(p \in  X'\). It is the unique fixed point of \(T_{N_\sigma}\). Under (62),

\[
O(\sigma)=\{p\}\times T_{N^c}.
\]

For every face \(\tau \preceq  \sigma\), the same splitting identifies the orbit

\[
O(\tau)=S'_\tau\times T_{N^c},
\qquad
S'_\tau\cong T_{N_\sigma/N_\tau},
\qquad N_\tau=N\cap\operatorname{span}_{\mathbb R}\tau.
\tag{63}
\]

The quotient lattices in (63) are free, because the span lattices are saturated. For a proper face, \(d = k - \dim \tau > 0\), so \(S'_\tau \cong  (\mathbb C^*)^d\). For \(\tau=\sigma\), this transverse orbit is just \(p\) and is handled as the cone vertex.

### A contracting action with positive weights

The monoid \(S'\) has finitely many generators. Here is the elementary finite-generation argument if Gordan’s lemma is not already available. Express the rational cone \(\sigma^\vee_{N_\sigma}\) as the positive span of finitely many integral vectors \(u_i\). For a lattice point \(m=\sum a_i u_i\), with \(a_i \ge  0\), subtract \(\sum \lfloor a_i\rfloor u_i\). The remainder is a lattice point in the bounded set \(\sum [0,1]u_i\) and still lies in the cone. There are only finitely many such lattice remainders. They and the \(u_i\) generate \(S'\).

Choose nonzero generators \(m_1,\ldots,m_r\) (zero adds no coordinate). They give a closed monomial embedding

\[
X'\hookrightarrow\mathbb C^r,
\qquad z_i=\chi^{m_i},\qquad p=0.
\tag{64}
\]

For \(k>0\), choose an integral point \(v \in  \operatorname{relint}(\sigma)\); rational polyhedrality lets one multiply a rational interior point by a common denominator. Every nonzero \(m_i\) in the dual cone has

\[
a_i=\langle m_i,v\rangle\in\mathbb Z_{>0}.
\]

Indeed a dual functional vanishing at an interior point must vanish on the whole full-dimensional cone and hence be zero. The cocharacter \(v\) acts in (64) as

\[
\lambda(t)(z_1,\ldots,z_r)
=(t^{a_1}z_1,\ldots,t^{a_r}z_r),
\qquad t\in\mathbb C^*.
\tag{65}
\]

The monomial relations are preserved by (65), since equal sums of \(m_i\) have equal total weight. Formula (65) extends to \(t=0\) by the constant point \(p\). Thus it gives a continuous contraction of \(X'\) to \(p\). For positive real \(t\), it preserves every \(T_{N_\sigma}\)-orbit. No ordinary scalar-invariance of \(X'\) is asserted or needed.

### From contraction to a compatible cone

Fix \(\varepsilon>0\) and use the Euclidean norm in (64). Set

\[
L_\varepsilon=X'\cap\{\|z\|=\varepsilon\},
\qquad W_\varepsilon=X'\cap\{\|z\|<\varepsilon\}.
\]

The total link \(L_\varepsilon\) is compact because \(X'\) is closed and the sphere is compact. It need not be a manifold or an aspherical space. Only its individual orbit pieces will have those properties.

For \(z\ne 0\), the function

\[
F_z(t)=\|\lambda(t)z\|^2
=\sum_i t^{2a_i}|z_i|^2,\qquad t>0,
\]

is strictly increasing, with limits zero and infinity. Its derivative is positive because some \(z_i\) is nonzero. There is exactly one \(s(z)>0\) with \(F_z(s(z))=\varepsilon^2\). The solution depends continuously on \(z\ne 0\), by the implicit function theorem (or strict monotonicity and the two endpoint limits). Put

\[
y(z)=\lambda(s(z))z\in L_\varepsilon,
\qquad t(z)=s(z)^{-1}.
\]

These maps are inverse to the explicit homeomorphism

\[
\Phi:L_\varepsilon\times(0,\infty)
\xrightarrow{\sim}X'\setminus\{p\},
\qquad \Phi(y,t)=\lambda(t)y.
\tag{66}
\]

For \(0<t<1\), the image has norm less than \(\varepsilon\). Adding the vertex gives

\[
\overline\Phi:\operatorname{Cone}(L_\varepsilon)
\xrightarrow{\sim}W_\varepsilon,
\tag{67}
\]

where the open cone has radial coordinate in \([0,1)\). The continuity at the collapsed end, including that of the inverse, follows from the explicit estimates for \(y\in L_\varepsilon\) and \(0<t\le 1\):

\[
\varepsilon t^{a_{\max}}
\le\|\lambda(t)y\|
\le\varepsilon t^{a_{\min}}.
\tag{68}
\]

In particular \(t\to 0\) makes all directions converge uniformly to \(p\), and \(z\to p\) forces \(t(z)\to 0\). Compactness of the link means the quotient cone neighborhoods at the vertex contain a uniform short radial interval, so these estimates verify the quotient topology as well. This is the step that a mere contraction does not supply by itself.

For a proper face \(\tau\prec \sigma\), set

\[
L_\tau=L_\varepsilon\cap S'_\tau.
\]

Because positive cocharacter scaling preserves orbits, (66) restricts to

\[
L_\tau\times(0,\infty)\cong S'_\tau,
\qquad
L_\tau\times(0,1)\cong W_\varepsilon\cap S'_\tau.
\tag{69}
\]

Each \(L_\tau\) is nonempty: a point of the nonzero orbit can be scaled uniquely to the sphere. It is a smooth real manifold of dimension \(2d-1\). Indeed the derivative of \(\|z\|^2\) along the positive-scaling vector field on the smooth torus orbit is \(\sum 2a_i|z_i|^2>0\), so the sphere is a regular level on that orbit. It is connected, since (69) identifies its product with a connected torus. There are finitely many pieces, one for each proper face. Their frontier relation is exactly the restriction of the affine orbit relation: if points in one orbit approach a point on the sphere, apply the continuous normalization \(y(z)\) to obtain approaching points in the corresponding link piece. The converse follows by inclusion in the orbit closure. Thus these pieces are a stratification of the total link.

### Normal charts at every point of the orbit

Let \(x\in O(\sigma)\), and identify that orbit with \(T_{N^c}\) in (62). Choose a small real coordinate ball \(B_x\) in this torus. Then

\[
V_x=W_\varepsilon\times B_x
\cong\operatorname{Cone}(L_\varepsilon)\times B_x
\tag{70}
\]

is open in the ambient variety and contains \(x\). Its intersection with the closed orbit is \({p}\times B_x\), and for every incident orbit \(S=O(\tau)\), \(\tau\prec \sigma\),

\[
S\cap V_x\cong L_\tau\times(0,1)\times B_x.
\tag{71}
\]

The base orbit corresponds to the cone vertex, not a punctured link piece. All non-base orbits meeting this affine chart are incident by the orbit-cone relation. No nonincident orbit meets it. Decreasing the radius at \(p\) and the ball at \(x\) gives a basis of neighborhoods. Alternatively, keep \(L_\varepsilon\) fixed and restrict the weighted radial coordinate to \([0,\eta)\); (68) proves that these neighborhoods are cofinal with ordinary small Euclidean neighborhoods. The chart respects the stratification for every such decrease.

When \(k=0\), the chart is just a small ball in the open torus orbit. There is no transverse nonzero orbit or incident link piece; set \(\operatorname{Cone}(\varnothing)={p}\). Finite type gives finitely many orbit strata: use a finite invariant affine cover and the finite number of faces in each cone chart. Thus (70)–(71) supply precisely the finite normal structure needed in the course criterion.

### Universal covers and the actual link map

The inclusion \(i_\tau:L_\tau\to S'_\tau\) at radial coordinate one in (69) is a strong deformation retract. In the product coordinates, the homotopy is \((y,t)\mapsto (y,(1-u)t+u)\), \(0\le u\le 1\); transporting it through (66) gives a homotopy entirely inside the same orbit. Therefore

\[
\pi_1(L_\tau)\xrightarrow{\sim}\pi_1(S'_\tau)
=N_\sigma/N_\tau.
\tag{72}
\]

The torus \(S'_\tau\cong (\mathbb C^*)^d\) has universal cover \(\mathbb C^d\), by coordinatewise exponentiation, with deck lattice \(2\pi i \mathbb Z^d\). Its universal cover is contractible. The connected smooth manifold \(L_\tau\) has a universal cover \(\widetilde L_\tau\). By (69), \(\widetilde L_\tau\times (0,\infty)\) is a universal covering of \(S'_\tau\), hence is isomorphic as a covering to \(\mathbb C^d\). It is contractible, and the projection to the slice at one shows \(\widetilde L_\tau\) itself is contractible. Consequently every incident link piece is a \(K(\pi ,1)\) manifold. Contractibility also implies its universal cover is acyclic for every unital coefficient ring. Every ambient orbit \(O(\tau)\cong T_{N/N_\tau}\) has the same property.

Choose the link slice by holding the base torus coordinate fixed at \(x\). Its map into the ambient stratum in (63) is

\[
L_\tau\longrightarrow S'_\tau\times T_{N^c},
\qquad y\longmapsto(y,x).
\]

It is a homotopy equivalence onto the first factor followed by a factor inclusion. On the intrinsic cocharacter lattices the actual homomorphism is

\[
N_\sigma/N_\tau\longrightarrow N/N_\tau,
\qquad [n]\longmapsto[n].
\tag{73}
\]

Its kernel is zero: a representative in \(N_\sigma\) maps to zero exactly when it belongs to \(N_\tau\). After choosing (61), its cokernel is \(N^c\). Basepoint changes only conjugate fundamental-group homomorphisms; here the orbit groups are abelian, so the injection is independent of that change. This identifies the map required by Theorem 6.10(2)(a), not an unrelated abstract embedding of groups.

Combining (70)–(73) with tags (31)–(34) of the existing lesson yields unrestricted bounded-below realization for the orbit stratification using the affine-neighborhood theorem already proved. All stratum groups are free abelian of finite rank. Over a field, the existing finite-heart theorem (48) therefore gives the bounded finite-stalk realization as well. No classification of indecomposable injectives is part of this geometric proof.

### The orbit-face and star-localization calculation

This section expands the elementary cone-chart input used above. The invariant affine-neighborhood theorem above has already supplied the connection to an abstract normal toric variety.

For a point of \(U_\sigma\), evaluation gives a multiplicative monoid map \(\gamma:S=\sigma^\vee\cap M\to\mathbb C\) with \(\gamma(0)=1\). Conversely evaluation of monoid generators satisfying the monomial relations defines a point. The torus action is \((t·\gamma)(m)=\chi^m(t)\gamma(m)\).

The nonzero support \(F={m:\gamma(m)\ne 0}\) is a monoid face: \(a+b\in F\) if and only if both \(a,b\in F\). Choose finitely many monoid generators \(s_i\) and let \(I\) index those in \(F\). Then \(F\) is exactly the monoid generated by these \(s_i\). Its cone is an exposed face of \(C=\sigma^\vee\). One elementary verification is to project the excluded generators modulo \(\operatorname{span}_{\mathbb R}{ s_i:i\in I }\). Zero cannot lie in their convex hull: a rational positive relation to this span, with denominators cleared and the inside terms moved to opposite sides, would give a monoid equality whose one side evaluates to zero and other side to nonzero. A real feasible relation can be chosen rational by row reduction over \(\mathbb Q\) and approximation in its affine solution space. Separating zero from that compact convex hull gives a functional zero on the inside span and strictly positive on every excluded generator. It can be chosen rational and scaled integral. If there are no excluded generators, use the zero functional.

Thus for a unique face \(\tau\preceq \sigma\),

\[
F=\sigma^\vee\cap\tau^\perp\cap M.
\]

The elementary dual-face relation identifies \(\tau\) as the common zero face in \(\sigma\) of the inside generators. The separating functional is in its relative interior because all remaining generator inequalities are strict. Dual-face uniqueness follows from the same defining zero inequalities.

The group generated by \(F\) is exactly \(M\cap \tau^\perp\). To see this, choose an integral relative interior point \(w\) of its cone. For any lattice \(m\) in its span, \(aw+m\) and \(aw\) belong to that cone for sufficiently large integer \(a\), so \(m\) is a difference of two elements of \(F\). (If the cone is its whole span, take \(w=0\).) Restriction of \(\gamma\) to \(F\) consequently extends to a character of \(M\cap \tau^\perp\). Conversely any such character, extended by zero outside \(F\), is a monoid point. The lattice \(M\cap \tau^\perp\) is saturated in \(M\); split it off to extend a character to \(M\). The torus therefore acts transitively on points of each support, proving

\[
O(\tau)\cong\operatorname{Hom}(M\cap\tau^\perp,\mathbb C^*)
\cong T_{N/N_\tau}.
\tag{74}
\]

For faces \(\tau\preceq \eta\preceq \sigma\), positive cocharacter limits with an integral \(u\in \operatorname{relint}(\eta)\) carry the distinguished point of \(O(\tau)\) to that of \(O(\eta)\): evaluate \(t^{\langle m,u\rangle }\gamma_\tau(m)\) and let \(t\to 0\). This proves \(O(\eta)\subset \overline{O(\tau)}\) in the classical topology. Conversely monomials vanishing on \(O(\tau)\) vanish on its closure. The support of a point in \(O(\eta)\) must then be contained in the dual face of \(\tau\); dual-face inclusion reverses the original face inclusion, giving \(\tau\preceq \eta\). This proves the incidence relation used in (63) and (71).

Finally, if \(\tau\preceq \sigma\), choose integral \(h\in \sigma^\vee\) with \(\sigma\cap h^\perp=\tau\). For \(m\in \tau^\vee\cap M\), the finitely many ray inequalities for \(\sigma\) show \(m+a h\in \sigma^\vee\) for all sufficiently large integers \(a\): on rays in \(\tau\) the inequality already holds; on the other rays \(h\) is positive. Hence

\[
\tau^\vee\cap M
=(\sigma^\vee\cap M)+\mathbb Z(-h),
\qquad
U_\tau=D(\chi^h)\subset U_\sigma.
\tag{75}
\]

This affine invariant open has \(O(\tau)\) as its unique closed orbit. In a global toric variety, an invariant open containing an orbit also contains every orbit whose closure meets that orbit: the open intersects the latter orbit, hence contains it by invariance and transitivity. Applied to (75), and combined with its affine orbit description, this proves that the chosen affine open is exactly the union of global orbits incident to the chosen closed orbit. It is the open orbit star meant in Proposition 6.11. This last argument uses no global fan classification.

### The general realization theorem

For comparison, Lunts–Schnürer's Proposition 6.11, p. 31, uses a toric affine star, a contracting one-parameter action and injectivity of the link-piece fundamental-group map. Corollary 7.15, p. 36, then adds the finite-heart theorem over a field. The preceding expanded geometric proof checks the saturated lattice, the weighted radial normalization and the map for each incident link piece. It also keeps the star as the local product neighborhood and uses invertibility of a finite kernel's order when averaging is invoked. These explicit checks determine the scope of the theorem below. The geometric triangulation, normality and analytic foundation inputs retain their stated obligations; comparing the realization mechanisms does not close all those inputs. No human source expression or figure is imported under the programme's CC0 dedication.

**Theorem.** Let \(X\) be a complex normal separated toric variety of finite type, in its classical topology, and let \(\mathcal S\) be its torus-orbit stratification. For every associative unital coefficient ring \(R\),

\[
D^+(\operatorname{Cons}_R(X,\mathcal S))
\xrightarrow{\sim}D^+_{\mathcal S}(X;R).
\tag{76}
\]

The bounded restriction is an equivalence as well. Over every field \(k\), the derived finite-stalk heart also realizes all bounded complexes with finite-stalk orbit-constructible cohomology:

\[
D^b(\operatorname{Cons}_{ft,k}(X,\mathcal S))
\xrightarrow{\sim}D^b_{\mathcal S,ft}(X;k).
\tag{77}
\]

**Proof.** Every orbit has an invariant affine star by the neighborhood, monoid and face-localization arguments. The saturated product and weighted-sphere construction give the normal charts, with one connected manifold link piece for each incident orbit. The number of orbits is finite. Each stratum and each incident link piece has a contractible universal cover, and its actual link-to-stratum fundamental-group map is the injection (73).

The universal-cover theorem (25) therefore gives realization on every stratum over \(R\). The normal-link argument (31)–(34) gives the internal-to-ambient direct-image comparison: restriction along an injective group homomorphism preserves injective modules because induction is exact. The full fixed-stratification criterion (27)–(30), with its actual finite gluing, now proves (76). Restrict to bounded cohomology for its bounded version. No finite-kernel averaging or characteristic condition is needed here.

For (77), every stratum group is the finite free lattice \(N/N_\tau\). The cone charts have finitely many incident link components. Thus the finite-heart theorem (48), whose required injectives were actually constructed by Artin–Rees and Baer, applies. Compose it with the bounded finite-cohomology restriction of (76). This proves (77), rather than merely an objectwise finite-cohomology assertion. \(\square\)

## Exercises on singular toric links and weighted charts

### A redundant monomial coordinate changes the radial weights

*Difficulty: Intermediate.*

Embed \(\mathbb A^2\) in \(\mathbb C^3\) by \((x,y)\mapsto(x,y,x^2)\). Explain why ordinary scalar multiplication does not give the required cone coordinates in this embedding. Construct the weighted action and prove that every nonzero point has exactly one positive scaling to a sphere of radius \(\varepsilon>0\).

**Solution.** The image is \(z=x^2\). Ordinary scalar multiplication would require \(tz=(tx)^2=t^2x^2\), which fails for \(x\ne0\) and \(t\notin\{0,1\}\). The cocharacter action is \((x,y,z)\mapsto(tx,ty,t^2z)\), with weights \(1,1,2\); it preserves the equation. For a nonzero point put \(A=|x|^2+|y|^2>0\) and \(B=|z|^2\geq0\). The squared norm is \(At^2+Bt^4\), strictly increasing from zero to infinity for \(t>0\). If \(B=0\), the unique value is \(t=\varepsilon/\sqrt A\). Otherwise its square is \((\sqrt{A^2+4B\varepsilon^2}-A)/(2B)>0\). This solves the sphere equation and proves uniqueness. The positive action preserves each torus orbit, so the resulting radial coordinates respect the orbit strata.

### Ray generators are not always the saturated span lattice

*Difficulty: Intermediate.*

In \(N=\mathbb Z^2\), let \(\sigma\) be generated by \(u=(1,0)\) and \(v=(1,2)\). Compare the lattice they generate with \(N_\sigma\). For the face \(\tau=\mathbb R_{\geq0}u\), compute the genuine link-group map at the closed orbit.

**Solution.** The ray lattice is \(\mathbb Zu+\mathbb Zv=\{(a,b):b\text{ is even}\}\), of index two in \(N\). The real span of \(\sigma\) is all of \(N_\mathbb R\), so \(N_\sigma=N\), not this index-two subgroup. Also \(N_\tau=\mathbb Z(1,0)\), so both \(N_\sigma/N_\tau\) and \(N/N_\tau\) are \(\mathbb Z\), generated by the class of \((0,1)\). The actual link map (73) is their identity. Using only the ray lattice would instead produce the subgroup \(2\mathbb Z\) in this coordinate. That artificial index comes from a finite covering of the affine torus, not from the geometric link. Saturation is necessary even though both rays themselves are primitive.

### The dense-orbit link differs from the total singular link

*Difficulty: Advanced.*

For the same cone, show that its affine toric surface is \(XZ=Y^2\). Describe the link piece of the dense orbit, and exhibit a loop that is nonzero in that piece but becomes contractible in the total link. Explain which group the realization test uses.

**Solution.** The dual inequalities are \(a\geq0\) and \(a+2b\geq0\). Its lattice monoid is generated by \((0,1),(1,0),(2,-1)\): for \(b\geq0\) use the first two; for \(b<0\) subtract \((-b)(2,-1)\), leaving \((a+2b,0)\). Their single relation is \((0,1)+(2,-1)=2(1,0)\). Consequently the monoid algebra is \(\mathbb C[X,Y,Z]/(XZ-Y^2)\). To verify that no additional relations occur, reduce every monomial using \(XZ=Y^2\) until either its \(X\)- or its \(Z\)-exponent is zero. The two resulting families have distinct character exponents except for their common powers of \(Y\).

The map \((u,v)\mapsto(u^2,uv,v^2)\) identifies the surface with the quotient of \(\mathbb C^2\) by simultaneous sign. It is surjective by choosing a square root of \(X\) when \(X\ne0\), and of \(Z\) otherwise; its fibers are precisely those sign pairs. It is proper, since bounded \(X,Z\) bound \(u,v\); the induced continuous bijection from the quotient is therefore a homeomorphism. The positive cocharacter \((1,1)\) gives weight one to \(X,Y,Z\). Radial normalization identifies the total sphere link with \(S^3/\{\pm1\}\).

On the dense orbit \(u,v\ne0\), write a unit-sphere point as
\((r e^{i\alpha},\sqrt{1-r^2}e^{i\beta})\), \(0<r<1\). The sign quotient identifies \((\alpha,\beta)\) with \((\alpha+\pi,\beta+\pi)\). Thus the dense-orbit link is the product of an open interval and a two-torus, with period lattice
\(\mathbb Z^2+\mathbb Z(\tfrac12,\tfrac12)\) when angles are divided by \(2\pi\). The positive-radius product gives the same period lattice for the dense orbit itself, so its link map is an isomorphism, as (72)–(73) predict.

Keep \(v=b\ne0\) and let \(u=a e^{i\theta}\), with \(|a|^2+|b|^2=1\). Its image is a nonzero period in that dense link; in the original cocharacter lattice it is \((1,2)\), since \(X,Y,Z\) wind by \(2,1,0\). In the full \(S^3\), it bounds the explicit disk
\((r a e^{i\theta},\sqrt{1-r^2|a|^2}\,b/|b|)\), \(0\leq r\leq1\). At \(r=0\) the angular coordinate collapses to a point with \(u=0\). Project the disk to the sign quotient and normalize to the surface sphere. It contracts this loop in the total link, passing through a boundary orbit. The realization test uses the link piece within each incident stratum, with its map to that stratum; it does not replace that piece by the entire singular link.
