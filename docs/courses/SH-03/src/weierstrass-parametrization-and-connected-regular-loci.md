# Weierstrass parametrization and connected regular loci

*Written by GPT-6 Astra (OpenAI), Ultra, with exercises developed from GPT-6.1 Sol's programme material, October 2026; the division section by Claude Opus 5.5 (Anthropic). Self-checked by the writing AI. Public domain (CC0).*

A local branch and a global component answer different questions. A local branch records which holomorphic equations remain inseparable near one point. A global component can return to the same point through several such branches. The curve \(y^2=x^2(x+1)\), for example, has a connected regular locus but two branches at its node. We will prove that the connected components of the regular locus of an analytic set determine its global irreducible components, and then find a connected dense region on each component where a holomorphic map has constant maximal rank.

All analytic subsets in this lesson are reduced and closed in their ambient complex manifold. Regularity means that the underlying subset is a complex submanifold near the point. The ambient manifold is Hausdorff and second countable. No pure-dimensional hypothesis or codimension-one restriction is imposed. When a union has several components, being regular on one component is weaker than being regular on the union.

## Local tools and where their proofs enter

Here are the local results used in the global argument. The links lead to complete earlier programme proofs; the assertions below specify the exact inputs rather than asking a citation to stand in for a proof.

1. Preparation and division, and Lemma 2.1 on Noetherianity establish Weierstrass preparation and division for \(\mathcal O_n=\mathbb C\{z_1,\ldots,z_n\}\). The proof counts fibre zeros with multiplicity by a contour integral, obtains the coefficients from Newton's identities, and proves uniqueness by divisibility with multiplicity. The bounded common-domain version is supplied in the next section.
2. The local ring of holomorphic germs, §§2–4 proves the coefficient-order estimate, the correspondence between analytic and polynomial factorizations, factoriality, and finite generation over a coordinate subring. The estimate is \(a_j(z')=O(|z'|^j)\) when the chosen vertical order equals the total order of the germ; an arbitrary regular vertical direction does not supply that stronger hypothesis. A common such direction for finitely many nonzero germs exists by avoiding the zeros of the product of their first nonzero homogeneous parts. Integral closedness follows directly: if a reduced fraction \(a/b\) in a factorial domain satisfies a monic equation of degree \(s\), multiplying by \(b^s\) shows that \(b\mid a^s\), so \(b\) is a unit.
3. Analytic germs, Propositions 1.1–1.2 identifies irreducibility with a prime vanishing ideal and gives a finite irredundant decomposition of every analytic germ. Proposition 2.2 and Corollary 2.3 choose adapted linear coordinates and prove the cone estimate \(|z''|\leq C|z'|\). Taking the base radius small enough that \(Cr'<r''\) keeps the vertical coordinates away from the boundary and makes the projection proper.
4. The finite-extension construction, Lemmas 3.1–3.4 works for a prime ideal \(J\) in arbitrary codimension. Put \(K=\operatorname{Frac}\mathcal O_d\), \(L=\operatorname{Frac}(\mathcal O_n/J)\), and \(q=[L:K]\). Localization of the finite domain \(\mathcal O_n/J\) at the nonzero elements of \(\mathcal O_d\) is a finite-dimensional domain over \(K\). Multiplication by a nonzero element is an injective linear endomorphism, hence surjective; that element is invertible. This localization is therefore the field \(L\), establishing the finite degree. A constant linear combination \(u\) of the transverse coordinates is primitive; with the \(q\) distinct embeddings denoted by \(\sigma_\mu\), its monic minimal polynomial \(W_u\) has discriminant \(\delta=\prod_{\mu<\nu}(\sigma_\mu u-\sigma_\nu u)^2\ne0\). The construction gives polynomials \(B_k\) of degree less than \(q\) in \(u\) and an ideal

\[
G=(W_u,\,\delta z_{d+1}-B_{d+1},\ldots,\delta z_n-B_n),
\qquad
G\subset J,\quad \delta^mJ\subset G,
\quad m=\max\{q,(n-d)(q-1)\}.
\tag{1}
\]

   This denominator-clearing statement identifies the analytic set with the reconstructed roots over \(\delta\ne0\). It is needed for more than hypersurfaces.
5. Local parametrization, Theorem 4.1 and Lemma 4.2 provides a sufficiently small representative \(B\) of each irreducible germ and a proper finite projection \(\pi:B\to\Delta'\). The subset \(B^\circ=B\setminus\pi^{-1}\{\delta=0\}\) is a connected complex manifold, dense and open in \(B\), and is a \(q\)-sheeted covering of the discriminant complement. Every exceptional fibre has at most \(q\) points. The proof establishes connectedness using the symmetric polynomials of hypothetical covering components, extends their bounded coefficients across the discriminant, and applies primality. Its separate density argument treats exceptional fibres; it does not assume density merely from finiteness of the projection.
6. Dimension and proper analytic subgerms, Theorem 5.4 and Proposition 5.5 identify the dimension with \(\dim\mathcal O_n/I(B)\) and show that a proper analytic subgerm of an irreducible germ has smaller dimension and empty interior. The Riemann extension theorem and Corollary 4.4 prove that deleting a proper analytic subset of a connected complex manifold leaves a connected dense subset. They also extend locally bounded holomorphic functions across that subset. These statements pass to manifolds by coordinate charts.

The projection in item 5 is surjective also over the discriminant. Indeed, approach any base point by points outside the discriminant, take one preimage of each, and use properness over the compact set formed by that sequence and its limit to obtain a limiting preimage. The finite-sheet statement alone would not justify this conclusion without properness.

For \(d=0\), an irreducible reduced germ has a representative consisting of one point; the covering and connectedness assertions are interpreted accordingly. When \(J=0\), there are no transverse coordinates, the representative is a polydisc, and the discriminant can be taken to be \(1\). These cases require no deletion.

## Division with one domain for all bounded inputs

Let \(D\subset\mathbb C^{n-1}\) be an open polydisc, \(s\geq1\), and

\[
P(z',w)=w^s+a_1(z')w^{s-1}+\cdots+a_s(z')
\]

a monic polynomial in \(w\) whose coefficients are holomorphic on \(D\). Suppose there are numbers \(0\leq a<R\) such that, for every \(z'\in D\), every root of \(P(z',\cdot)\) has modulus at most \(a\). For a bounded function \(f\) on \(D\times\{|w|<R\}\) write \(\|f\|\) for its supremum.

**Proposition (division with one domain).** Every bounded holomorphic \(f\) on \(D\times\{|w|<R\}\) has exactly one expression \(f=PQ+T\), where \(Q\) is holomorphic on \(D\times\{|w|<R\}\) and \(T\) is a polynomial in \(w\) of degree less than \(s\) whose coefficients are holomorphic on \(D\). Moreover

\[
\|T\|\leq C_1\|f\|,\qquad\|Q\|\leq C_2\|f\|,\qquad
C_1=\frac{sR(R+a)^{s-1}}{(R-a)^s},\qquad C_2=\frac{1+C_1}{(R-a)^s}.
\tag{2}
\]

The constants depend only on \(s\), \(a\) and \(R\). One domain therefore serves for every bounded input, and the outputs are controlled on that whole domain.

**Proof.** For \(a<\sigma<R\), \(z'\in D\) and \(|w|<\sigma\), define

\[
\begin{aligned}
Q(z',w)&=\frac1{2\pi i}\int_{|\zeta|=\sigma}\frac{f(z',\zeta)}{P(z',\zeta)(\zeta-w)}\,d\zeta,\\
T(z',w)&=\frac1{2\pi i}\int_{|\zeta|=\sigma}\frac{f(z',\zeta)}{P(z',\zeta)}\,\frac{P(z',\zeta)-P(z',w)}{\zeta-w}\,d\zeta.
\end{aligned}
\tag{3}
\]

Write \(P(z',\cdot)=\prod_{l=1}^s(\cdot-b_l)\) with \(|b_l|\leq a\). On the circle \(|\zeta|=\sigma\) every factor has modulus at least \(\sigma-a\), so \(|P(z',\zeta)|\geq(\sigma-a)^s\). The integrands are therefore continuous, and holomorphic in \((z',w)\) for fixed \(\zeta\); integrals of this kind over a fixed circle are holomorphic in the parameters by Lemma A of the reading cited below. The divided difference in (3) is a polynomial in \(w\) of degree less than \(s\), whose coefficients are polynomials in \(\zeta\) and the \(a_k(z')\). Hence \(T\) has the stated form. Since

\[
\frac1{\zeta-w}=\frac{P(z',w)}{P(z',\zeta)(\zeta-w)}+\frac{P(z',\zeta)-P(z',w)}{P(z',\zeta)(\zeta-w)},
\]

Cauchy's formula for \(f(z',\cdot)\) on the circle gives \(f=PQ+T\) on \(D\times\{|w|<\sigma\}\).

For uniqueness, suppose \(PQ'+T'=0\) on \(D\times\{|w|<\sigma\}\), with \(Q'\) holomorphic and \(T'\) of degree less than \(s\) in \(w\). For fixed \(z'\), the polynomial \(T'(z',\cdot)=-P(z',\cdot)Q'(z',\cdot)\) vanishes at each root \(b\) of \(P(z',\cdot)\) to at least the multiplicity of \(b\). It therefore has at least \(s\) zeros counted with multiplicity, so \(T'(z',\cdot)=0\). Then \(Q'(z',\cdot)\) vanishes off the finitely many roots, hence everywhere. Uniqueness on the smaller disc shows that the functions defined with different radii \(\sigma\) agree. Together they give \(Q\) and \(T\) on \(D\times\{|w|<R\}\), and the expression is unique there.

For the bounds, change the factors of \(\prod_l(\zeta-b_l)\) into those of \(\prod_l(w-b_l)\) one at a time. Each step contributes one term, and

\[
\frac{P(z',\zeta)-P(z',w)}{\zeta-w}=\sum_{\ell=1}^s\ \prod_{i<\ell}(w-b_i)\prod_{i>\ell}(\zeta-b_i).
\]

For \(|\zeta|=\sigma\geq|w|\) its modulus is at most \(s(\sigma+a)^{s-1}\). The circle has length \(2\pi\sigma\), so (3) gives \(|T|\leq s\sigma(\sigma+a)^{s-1}(\sigma-a)^{-s}\|f\|\) on \(D\times\{|w|<\sigma\}\). Letting \(\sigma\to R\) gives the bound for \(T\) in (2). On the circle \(|w|=\sigma\), \(|Q|=|f-T|/|P|\leq(1+C_1)\|f\|(\sigma-a)^{-s}\). The maximum principle on the closed disc \(|w|\leq\sigma\) extends this bound to the disc, and \(\sigma\to R\) gives the bound for \(Q\). \(\square\)

The preparation theorem that produces such polynomials, and this division with the same constants, are proved in Weierstrass preparation and division, Theorems 1 and 2.

For division by a prepared function \(g=vP\), where \(v\) is holomorphic on \(D\times\{|w|<R\}\) and \(|v^{-1}|\leq L\) there, replace \(Q\) by \(Q/v\); the bound for the quotient is multiplied by \(L\). Degree zero is division by a unit with zero remainder.

## Continuing local branches across the whole analytic set

Let \(A\) be a closed reduced complex analytic subset of a Hausdorff complex manifold \(M\). A *global irreducible analytic subset* is a nonempty closed analytic subset which cannot be written as the union of two proper closed analytic subsets. This is a global condition; its germ at a point may have several irreducible branches.

We use two local conclusions already proved in Analytic germs, local parametrization and the Nullstellensatz. Proposition 1.2 gives the finite irredundant decomposition of an analytic germ. Theorem 4.1 gives, for each irreducible germ, arbitrarily small representatives \(B\) containing an open connected smooth subset \(H\) dense in \(B\). This is the smooth part over the complement of the discriminant in the local parametrization theorem. The construction below requires neither a globally chosen projection nor an analytic description of the singular locus.

We will prove that the closures of the connected components of \(A_{\mathrm{reg}}\) are exactly the global irreducible components of \(A\), and that this family is locally finite in \(M\). We will then isolate a connected region on each component where a holomorphic map has maximal rank and the whole set \(A\) is regular.

### Deleting a proper analytic subset preserves connectedness

We first record the deletion argument in the form needed below. If \(P\) is a connected complex manifold and \(Z\subsetneq P\) is closed analytic, then \(P\setminus Z\) is connected and dense. This conclusion is also proved by bounded holomorphic extension in Holomorphic functions of several variables, Corollary 4.4 and §5.

An analytic subset with interior in \(P\) equals \(P\). Indeed its interior is also closed: near a limit of interior points, take a connected coordinate neighborhood on which finitely many holomorphic equations define the subset. Each equation vanishes on a nonempty open part of that neighborhood, hence everywhere there by the identity theorem. Connectedness now proves the assertion. Thus a proper analytic subset has empty interior, and its complement is dense.

For connectedness of the complement, first work in a convex coordinate polydisc with two points \(a,b\notin Z\). A linear combination of the local defining equations can be chosen nonzero at both points: the excluded coefficient choices are at most two proper complex hyperplanes. Restrict that function to the affine complex line through \(a,b\). It is not identically zero, so its zeros near the compact segment from \(a\) to \(b\) are finite. Small detours in that line around these zeros give a path inside the polydisc avoiding its zero set, and therefore avoiding \(Z\).

A connected manifold is path connected. Cover a path in \(P\) by finitely many such polydiscs, ordered with successive open overlaps. Density supplies intermediate points outside \(Z\) in those overlaps. The local paths join them in \(P\setminus Z\). The dimension-zero case is a single point and an empty deletion.

Finite unions of closed analytic subsets are analytic: locally, products of their defining functions give equations for the union. The same is true for a locally finite union, since near any ambient point only finitely many members occur. Consequently the deletion argument also applies to such a union whenever it is proper.

### A finite branch calculation controls global continuation

Fix \(x\in A\). On a neighborhood \(W\) represent the distinct irreducible germs of \(A\) at \(x\) by closed analytic sets \(B_1,\ldots,B_s\), with
\[
A\cap W=B_1\cup\cdots\cup B_s.
\tag{GC1}
\]
The representatives can be chosen on one neighborhood because the list is finite and the germ equalities hold after shrinking.

For each \(i\), apply local parametrization to its branch, inside \(W\). Obtain a neighborhood \(W_i\) of \(x\) and an open connected smooth subset
\[
H_i\subset B_i\cap W_i,
\qquad
\overline{H_i}^{\,W_i}=B_i\cap W_i.
\tag{GC2}
\]
For \(j\ne i\), the analytic subset \(H_i\cap B_j\) is proper. Otherwise closedness of \(B_j\) and (GC2) would give \(B_i\cap W_i\subset B_j\), contradicting the irredundant germ decomposition. A proper analytic subset of the connected \(H_i\) has empty interior. Their finite union is therefore proper, and the deletion argument shows that
\[
K_i=H_i\setminus\bigcup_{j\ne i}B_j
\tag{GC3}
\]
is connected and dense in \(H_i\), hence dense in \(B_i\cap W_i\).

Every point of \(K_i\) is regular for \(A\): near it the other finitely many closed branches are absent, and \(A\) agrees with the smooth branch \(B_i\). Thus \(K_i\) lies in one connected component \(R_i\) of \(A_{\mathrm{reg}}\). These sets also show that \(A_{\mathrm{reg}}\) is dense in \(A\).

Choose a common neighborhood \(U\) of \(x\) contained in all \(W_i\). We retain the full connected \(K_i\) in its original neighborhood. The smaller set \(K_i\cap U\) is not required to be connected.

For every connected component \(R\) of \(A_{\mathrm{reg}}\), we claim
\[
\overline R^{\,M}\cap U
=\bigcup_{\{i:R_i=R\}}(B_i\cap U).
\tag{GC4}
\]
Here is the point that makes the formula global. If \(a\in R\cap B_i\cap U\), choose an ambient neighborhood \(V\subset W_i\) of \(a\) whose intersection with \(A\) lies in \(R\). Such a neighborhood exists because \(R\) is open in \(A_{\mathrm{reg}}\), and \(A_{\mathrm{reg}}\) is open in \(A\). Density in (GC3) gives \(V\cap K_i\ne\varnothing\). Since \(K_i\) is connected, its assigned component is \(R_i=R\). Therefore
\[
R\cap U\subset\bigcup_{\{i:R_i=R\}}(B_i\cap U).
\]
The right side is closed relative to \(U\); taking closure inside \(U\) proves one inclusion in (GC4). For the reverse inclusion, each assigned \(K_i\subset R\) is dense in \(B_i\cap W_i\), so every point of \(B_i\cap U\) belongs to \(\overline R^{\,M}\).

No assertion about analytic continuation through an arbitrary small intersection was used: the larger connected sets \(K_i\) determine the assignments, and only the final equality is restricted to \(U\).

### The global component theorem

For each connected component \(R\) of \(A_{\mathrm{reg}}\), set \(C_R=\overline R^{\,M}\). Formula (GC4) shows that \(C_R\) is analytic near every point of \(A\). It is absent near a point outside \(A\), because \(A\) is closed. Thus \(C_R\) is a closed analytic subset of \(M\).

Only finitely many \(C_R\) meet the neighborhood \(U\) in (GC4): each such \(R\) is one of the finitely many assignments \(R_i\). The family \(\{C_R\}\) is therefore locally finite in the ambient manifold, including at singular points and points outside its members. It covers \(A\), again by (GC4).

Connected components are closed in any topological space. Since \(A_{\mathrm{reg}}\) is open in \(A\), this gives the useful identity
\[
C_R\cap A_{\mathrm{reg}}=R.
\tag{GC5}
\]
In particular, distinct \(C_R\) do not contain one another: a point of \(R\) belongs to \(C_R\) and, by (GC5), to no \(C_{R'}\) with \(R'\ne R\).

Each \(C_R\) is globally irreducible. To see this, suppose \(C_R=D\cup E\) with \(D,E\) closed analytic. Their intersections with the connected complex manifold \(R\) are analytic. If both were proper, they would be closed with empty interior and their finite union could not cover \(R\). Hence one contains \(R\), and its closedness makes it contain \(C_R\).

Apply the construction to any nonempty globally irreducible analytic set \(B\). If \(B_{\mathrm{reg}}\) had two or more connected components, choose one closure \(C_R\) and let \(E\) be the union of all the other closures. Local finiteness makes \(E\) closed analytic. Both \(C_R\) and \(E\) are proper by (GC5), contradicting irreducibility of \(B=C_R\cup E\). Thus
\[
B_{\mathrm{reg}}\ \text{is connected and dense in }B.
\tag{GC6}
\]
This conclusion applies in particular to every \(C_R\). Its intrinsic regular locus may contain points singular for the larger union \(A\).

It remains to verify maximality, so that the constructed sets really are the global irreducible components. Let \(B\subset A\) be any nonempty globally irreducible closed analytic subset. By (GC6), \(B_{\mathrm{reg}}\) is connected and dense in \(B\). Near one of its points, only finitely many \(C_R\) occur. Their intersections with a small regular neighborhood cover that neighborhood. One of those intersections has interior; otherwise finitely many closed analytic subsets with empty interior would cover a manifold. The identity theorem on the connected \(B_{\mathrm{reg}}\) then gives \(B_{\mathrm{reg}}\subset C_R\), and closedness gives \(B\subset C_R\). Together with noncontainment, this proves maximality and uniqueness.

We have established the global component theorem in arbitrary codimension. It also proves the equivalence
\[
A\ne\varnothing\text{ is globally irreducible}
\quad\Longleftrightarrow\quad
A_{\mathrm{reg}}\text{ is connected}.
\tag{GC7}
\]
If \(M\) is second countable, the family of components is at most countable: its indexing sets \(R\) are disjoint nonempty open subsets of the second-countable manifold \(A_{\mathrm{reg}}\). Local finiteness, rather than global finiteness, is the conclusion used below.

### A connected maximal-rank region inside the regular carrier

Let \(f:M\to N\) be holomorphic, and let \(C=C_R\) be one global component of \(A\). The connected manifold \(P=C_{\mathrm{reg}}\) has one complex dimension \(d\). The integer rank of
\[
df_p|_{T_pC}:T_pC\longrightarrow T_{f(p)}N
\]
lies in \(\{0,\ldots,d\}\); its maximum \(r\) is therefore attained without any compactness assumption.

The rank-drop set \(Z_f=\{p\in P:\operatorname{rank}(df_p|_{T_pC})<r\}\) is closed analytic in \(P\): in manifold and target coordinates it is cut out by the \(r\)-minors. These equations agree in their zero loci under coordinate changes. For \(r=0\), put \(Z_f=\varnothing\). It is proper by the definition of \(r\).

Also put
\[
Z_{\mathrm{int}}
=P\cap\bigcup_{D\ne C}D,
\qquad
U_C=P\setminus(Z_f\cup Z_{\mathrm{int}}),
\tag{GC8}
\]
where \(D\) ranges over the other global components. Their union is closed analytic by ambient local finiteness, so \(Z_{\mathrm{int}}\) is analytic in \(P\). It is proper: every point of the nonempty \(R\subset P\) avoids the other components by (GC5).

Both deleted sets are proper analytic subsets of connected \(P\); their union is still proper. The deletion lemma proves that \(U_C\) is nonempty, connected and dense in \(P\), hence dense in \(C\). It is a complex submanifold, and \(f|_{U_C}\) has constant rank \(r\).

At any point of \(P\setminus Z_{\mathrm{int}}\), ambient local finiteness supplies a neighborhood meeting no other component. There \(A=C\), so the point is regular for \(A\) and the tangent spaces of \(A\) and \(C\) agree. Conversely every point of \(R\) has these properties. Consequently
\[
P\setminus Z_{\mathrm{int}}=R,
\qquad
U_C=\{p\in R:\operatorname{rank}(df_p|_{T_pA})=r\}.
\tag{GC9}
\]
Deleting intersections is thus exactly what makes the rank statement concern the regular locus of the whole carrier.

For a holomorphic cotangent projection, this gives one connected dense region on each irreducible analytic component where the carrier is regular and the projection has its maximal rank. Any propagation of a sheaf coefficient type from that region still uses the separate microlocal continuity theorem. Neither a hypersurface equation nor local irreducibility of the global component has been assumed.

## Exercises with complete solutions

### 1. Multiplicities determine the remainder

*Difficulty: Introductory.* Divide \(e^w\) by \(w^3\) in the ring of holomorphic germs at zero. Why would testing only the distinct roots of the divisor give an insufficient uniqueness argument?

**Solution.** Taylor expansion gives

\[
e^w=w^3Q(w)+1+w+\tfrac12w^2,
\qquad Q(w)=\sum_{j=0}^{\infty}\frac{w^j}{(j+3)!}.
\]

The series for \(Q\) converges everywhere and has value \(1/6\) at zero. A polynomial remainder difference must vanish to order at least three, not just vanish at zero. The polynomial \(w\) passes the latter test but fails the former. A polynomial of degree at most two with a triple zero is zero, which gives uniqueness.

### 2. Sheets can belong to one component

*Difficulty: Intermediate.* For the cusp \(y^2=x^3\), describe a parametrization, the regular locus and the covering over a punctured \(x\)-disc. Decide whether the two sheets define two irreducible germs.

**Solution.** Set \(x=t^2\), \(y=t^3\). If a point of the curve is nonzero, then \(x\ne0\), and \(t=y/x\) is its unique parameter. At the origin use \(t=0\). The gradient of \(y^2-x^3\) is \((-3x^2,2y)\), which vanishes on the curve only at the origin; the implicit-function theorem therefore proves smoothness away from that point. Over a nonzero \(x\), the two choices \(t=\pm\sqrt{x}\) are exchanged by a loop around zero. The resulting two-sheeted covering is connected.

For an algebraic check of germ irreducibility, a factorization of the monic quadratic \(y^2-x^3\) over \(\mathbb C\{x\}\) would give a holomorphic root \(h(x)\). Then \(2\operatorname{ord}_0h=3\), an impossibility. The polynomial is irreducible, and the Weierstrass factorization result in the local-ring prerequisite makes it irreducible in \(\mathbb C\{x,y\}\). That ring is factorial, so its principal ideal is prime. The two sheets therefore belong to one irreducible germ.

The origin is singular for a further reason. The finite projection gives dimension one. If the curve were a submanifold there, choose a holomorphic local coordinate \(s\) on that smooth curve. Neither ambient coordinate function is identically zero, and \(y(s)^2=x(s)^3\) gives \(2\operatorname{ord}_s y=3\operatorname{ord}_s x\). Hence both orders are at least two. The derivative of the inclusion into \(\mathbb C^2\) would vanish, contradicting the immersion property of a submanifold. The regular locus is therefore exactly the punctured curve, biholomorphic to the punctured parameter disc.

### 3. One global component, two branches at a node

*Difficulty: Advanced.* Study \(C=\{y^2=x^2(x+1)\}\subset\mathbb C^2\) by the parameter \(x=t^2-1\), \(y=t(t^2-1)\). Determine its global components and its local branches at the origin.

**Solution.** The only point with \(x=0\) is \((0,0)\). Elsewhere \(t=y/x\), and the equation gives \(t^2=x+1\), proving that the parameter recovers every such point uniquely. Its derivative \((2t,3t^2-1)\) is never zero. The defining function has gradient \((-3x^2-2x,2y)\); solving the gradient equations together with the curve equation leaves only \((0,0)\). The two parameters \(t=1,-1\) map to that node. Consequently

\[
C_{\mathrm{reg}}\cong\mathbb C\setminus\{-1,1\}.
\]

This is connected, and its closure is \(C\), so the global-component theorem makes \(C\) irreducible. On a disc about \(x=0\), a holomorphic square root of \(1+x\) exists, for example by its convergent binomial series. The two distinct germs \(y=x\sqrt{1+x}\) and \(y=-x\sqrt{1+x}\) are smooth and form the curve germ. Global irreducibility does not require every germ to be irreducible.

![A connected complex parameter plane and the two local branches of a nodal curve](figures/global-branches.svg)

The left panel shows the complex parameter plane with \(t=\pm1\) omitted. A path between the two punctured neighbourhoods stays in this connected domain. The right panel shows only the real trace of \(C\); the full complex curve lies in \(\mathbb C^2\). Both omitted parameters map to the node, and their neighbourhoods produce its two local branches. This is the distinction proved in (GC4)–(GC7), with the exact parametrization checked in this solution. Figure by GPT-6 Astra (OpenAI), Ultra, CC0. Full-size figure · Reproducible plotting source.

### 4. A margin that makes a projection proper

*Difficulty: Intermediate.* Intersect the line \(w=z\) with \(\Delta_{r_z}\times\Delta_{r_w}\). Compare the projection to \(\Delta_{r_z}\) when \(r_z<r_w\) and when \(r_w<r_z\).

**Solution.** If \(r_z<r_w\), the intersection is the graph over the entire base disc. The projection is a homeomorphism, so every compact base set has compact inverse image. The strict vertical margin is uniform on compact subsets of the base.

If \(r_w<r_z\), the image omits the points with \(r_w\leq|z|<r_z\). Choose real \(z_j\uparrow r_w\) and the compact base subset \(K=\{z_j:j\geq1\}\cup\{r_w\}\). Its inverse image consists of \((z_j,z_j)\), whose only ambient limit is \((r_w,r_w)\), outside the product of open discs. That inverse image is not compact. The projection is neither surjective nor proper in this second case.

### 5. Intrinsic regularity and regularity of the carrier

*Difficulty: Intermediate.* Let \(A=\{xy=0\}\) and \(f(x,y)=x\). Find the intrinsic regular locus and maximal-rank region of each global component, then require the points also to be regular on \(A\).

**Solution.** Write \(C_h=\{y=0\}\) and \(C_v=\{x=0\}\). Each is a smooth complex line, and each is its own intrinsic regular locus. The restriction of \(f\) has rank one on \(C_h\) and rank zero on \(C_v\), with no rank-drop points on either. The origin nevertheless fails to be regular on the union: a submanifold germ is irreducible, whereas these two distinct line germs meet there. Removing that intersection leaves \(C_h\setminus\{0\}\) and \(C_v\setminus\{0\}\), both connected and dense. For the vertical component the deletion is needed for carrier regularity even though rank zero is already constant.

### 6. Infinite components and ambient accumulation

*Difficulty: Advanced.* Compare the zero set of \(\sin(\pi z)\) in \(\mathbb C\) with \(E=\{0\}\cup\{1/j:j\geq1\}\). Which admits a locally finite analytic component decomposition near zero?

**Solution.** Using \(\sin(\pi z)=(e^{i\pi z}-e^{-i\pi z})/(2i)\), its zeros satisfy \(e^{2\pi iz}=1\), hence are exactly the integers. Each integer is an isolated point and an irreducible component. Each such component is smooth and zero-dimensional, and every map restricted to it has rank zero. A bounded neighbourhood meets only finitely many integers, so the family is locally finite in the ambient plane, although it is globally infinite.

In contrast, every neighbourhood of zero meets infinitely many singleton subsets of \(E\). If finitely many holomorphic equations defined \(E\) near zero, each defining function would vanish at all sufficiently small \(1/j\). The one-variable identity theorem would make every one of those functions identically zero near zero. Their common zero set would contain a whole disc, a contradiction. Local finiteness must hold near every ambient point, not merely near each isolated member of a proposed family.

## Human sources and the microlocal application

Jean-Pierre Demailly's freely available *[Complex Analytic and Differential Geometry](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf)*, version of 21 June 2012, treats the preparation and finite-parametrization mathematics developed in the earlier analytic prerequisites, presenting preparation and division by C. L. Siegel's contour method. The global-component argument, rank argument and exercises are programme exposition, and the exact earlier proofs used by them are listed at the start.

For an analytic Lagrangian subset of \(T^*X\), take the holomorphic map to be \(\pi:T^*X\to X\). The maximal-rank region proved above is the geometric input for how simple sheaf shifts change along a Lagrangian. The sheaf comparison and continuity arguments in that lesson are separate from the analytic component theorem.
