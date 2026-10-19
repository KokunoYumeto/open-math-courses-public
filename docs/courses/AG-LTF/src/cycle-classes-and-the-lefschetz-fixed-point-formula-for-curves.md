# Cycle classes and the Lefschetz fixed-point formula for curves

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A fixed point of a map of curves is an intersection of its graph with the diagonal. A cohomological trace is a contraction against a dual basis. The cycle class of the diagonal connects these two calculations. Its middle-degree term carries a minus sign, and that sign produces the alternating cohomological trace.

We begin with the two boundary maps behind a divisor class, then establish its trace normalization. The projective-bundle formula constructs Chern classes of every vector bundle, with a Whitney proof that also works with finite coefficients. Supported classes retain the multiplicities of singular cycles and descend through rational equivalence. Specialization to the normal bundle proves compatibility with the full Chow ring, proper pushforward and arbitrary pullback between smooth schemes, over every invertible finite coefficient ring and over \(\mathbf Z_\ell\). We also compare the rational cycle map with the Chern-character construction. The signed diagonal then gives the fixed-point formula, with local lengths, for smooth proper schemes in every dimension. The coherent proof in §2 establishes curve Riemann–Roch, the surface intersection pairing and the Hodge index theorem. Section 5 then proves rationality, integrality, the functional equation and the Riemann hypothesis for curves: the curve trace gives the zeta numerator, and Hodge index bounds the Frobenius graph intersections on \(C\times C\).

## 1. Divisors, support and the sign of their classes

Let \(k\) be algebraically closed. Let \(n\geq1\) be invertible in \(k\), and put \(\Lambda_n=\mathbf Z/n\mathbf Z\). Write \(\Lambda_n(1)=\mu_n\), and use tensor powers for other twists. A surface is smooth and projective of pure dimension two; a curve, unless explicitly stated otherwise, is smooth, projective and connected. Smoothness makes a connected curve integral. Cohomology means étale cohomology.

The Kummer sequence is

\[
1\longrightarrow\mu_n\longrightarrow\mathbf G_m
\xrightarrow{\,u\mapsto u^n\,}\mathbf G_m\longrightarrow1.
\tag{1.1}
\]

Its last map is locally surjective: for a unit \(u\) on an affine scheme, adjoining a root of \(T^n-u\) gives a finite étale cover, since both the root and \(n\) are units. Its kernel is \(\mu_n\) by definition. The connecting homomorphism therefore defines

\[
c_{1,n}:\operatorname{Pic}(S)=H^1(S,\mathbf G_m)
\longrightarrow H^2(S,\Lambda_n(1)).
\tag{1.2}
\]

It is additive under tensor product and natural under pullback. These statements follow from the long exact cohomology sequence and its naturality, including for morphisms that collapse a divisor. Thus \(c_{1,n}(L^{\otimes a})=a\,c_{1,n}(L)\) for every integer \(a\). See [Stacks, Tag 03PK](https://stacks.math.columbia.edu/tag/03PK).

For an effective Cartier divisor \(D\subset S\), the line bundle \(\mathcal O_S(D)\) has a distinguished section \(1\), which trivializes it on \(U=S-D\). A line bundle together with a trivialization on \(U\) defines a class in \(H^1_D(S,\mathbf G_m)\). Apply the Kummer connecting map **with support** to obtain

\[
c_{D,n}\in H^2_D(S,\mu_n).
\tag{1.3}
\]

Forgetting support takes this class to \(c_{1,n}(\mathcal O_S(D))\): the forgetful maps commute with the Kummer connecting maps. This also explains additivity for divisors, including negative coefficients after passing to differences.

There is a sign to check even when \(D\) has one equation. Normalize torsor classes so that the torsor of lifts of a section in a short exact sequence represents its connecting class. Use the localization boundary of Deligne, [Cycle], §1.1.4. If \(D=(f)\), let \(\kappa(f)\in H^1(U,\mu_n)\) be the class of the torsor \(T^n=f\). In these conventions,

\[
c_{D,n}=-\partial_{\mathrm{loc}}\kappa(f).
\tag{1.4}
\]

Indeed the pair \((\mathcal O(D),1)\) is the supported \(\mathbf G_m\)-torsor obtained from \(f\) by the degree-zero localization boundary. Taking its Kummer boundary is the definition (1.3). The Kummer and localization boundaries anticommute: in a double complex, one uses the sign \((-1)^a\) for the second differential on the row of degree \(a\), so interchanging the two degree-one boundaries changes sign. This gives (1.4). It agrees with [Cycle], §§2.1.2–2.1.3, printed pp. 138–139. Declaring the root torsor's localization boundary positive without specifying this convention would give the opposite class.

The divisor valuation sequence has a different boundary. Let \(j:U\hookrightarrow X\) be the complement of a smooth divisor, with positive valuations, and write \(\partial_{\mathrm{div}}\) for the connecting map of

\[
0\longrightarrow\mathbf G_m\longrightarrow j_*\mathbf G_{m,U}
\xrightarrow{\operatorname{ord}_D}i_*\mathbf Z\longrightarrow0.
\]

The last map is locally surjective, since a normal parameter has valuation one. On an overlap, local rational lifts \(f_i,f_j\) of \(D\) give the connecting torsor cocycle \(f_j/f_i\). With frames satisfying \(e_j=e_i g_{ij}\), these are the transition functions of \(\mathcal O_X(-D)\): its local frames are \(f_i\). The frames \(f_i^{-1}\) of \(\mathcal O_X(D)\) have the inverse transition functions. Consequently

\[
\partial_{\mathrm{div}}(D)=[\mathcal O_X(-D)],\qquad
c_{1,n}(\mathcal O_X(D))=-\partial_K\partial_{\mathrm{div}}(D).
\tag{1.4a}
\]

Here \(\partial_K\) is the Kummer connecting map. This is the convention of [The multiplicative group on a curve, §5](course:ag-etale-cohomology/the-multiplicative-group-on-a-curve). The localization boundary in (1.4) instead regards the trivial torsor with the section \(f\) as its trivialization. Its supported class is \((\mathcal O(D),1)\); hence its sign is opposite to the valuation-sequence boundary. In particular, in these localization conventions the positive cycle generator is \(-\partial_{\mathrm{loc}}\kappa(f)\). One cannot identify these two connecting maps while keeping both signs positive.

We use the following exact geometric proof homes. [Poincaré duality for curves, §§3–11](course:ag-etale-cohomology/poincare-duality-for-curves) proves coefficient self-injectivity, curve duality and its compact-support form. [Smooth traces, duality and Gysin maps, §§1–11](course:AG-LTF/smooth-trace-and-duality) proves local concentration, the arbitrary-complex smooth exceptional inverse image, global duality and smooth-pair purity; its §12 constructs Gysin maps from the adjunction counit and proves their projection and trace identities. Its §§1–2 construct the higher-dimensional trace from the curve theorem and prove coordinate independence, base change and smooth composition. Brown representability and the expressly named general finiteness, constructibility and continuity premises remain inherited foundations. The comparison with the Kummer convention is proved next, using (1.4a).

**Proposition 1.1 (normalized traces and divisor compatibility).** For a smooth proper \(d\)-dimensional scheme \(Y/k\), the trace is

\[
\int_Y:H^{2d}(Y,\Lambda_n(d))\longrightarrow\Lambda_n;
\]

on several connected components it is the sum of their traces. On a connected curve it is an isomorphism, a closed point has trace \(1\), and cup product gives the usual perfect duality pairings. If \(i:D\hookrightarrow S\) is a smooth divisor in a smooth surface, purity identifies

\[
H^2_D(S,\Lambda_n(1))\simeq H^0(D,\Lambda_n),
\tag{1.5}
\]

with the class (1.3) corresponding to the section \(1\) on each component. Its image in ordinary cohomology satisfies, for every \(v\in H^2(S,\Lambda_n(1))\),

\[
\int_S c_{1,n}(\mathcal O(D))\cup v
=\int_D i^*v.
\tag{1.6}
\]

These normalizations are compatible with changing \(n\), with the \(\ell\)-adic inverse limit, and with rationalization for \(\ell\ne\operatorname{char}k\).

More generally, for a smooth divisor in a smooth \(d\)-dimensional scheme, the supported class (1.3) is its Gysin class of \(1\). When both schemes are proper, (1.6) holds with \(v\in H^{2d-2}(X,\Lambda_n(d-1))\).

**Proof.** The derived duality theorem in the smooth-variety provider identifies the dualizing complex with \(\Lambda_n(d)[2d]\), and its counit with trace. For a smooth closed immersion of codimension \(c\), composition of right adjoints identifies

\[
Ri^!\Lambda_n=\Lambda_n(-c)[-2c].
\]

Indeed \(p_D=p_Xi\), so \(Ri^!Rp_X^!\Lambda_n=Rp_D^!\Lambda_n\); insert the two smooth formulas and cancel the invertible twist and even shift. For a point this orientation's Gysin class has trace one, since the composite counit is the trace of that point. For a curve the trace is the degree map on \(\operatorname{Pic}(C)/n\), as constructed in §2 of the curve-duality provider and §6 of the multiplicative-group provider. The Kummer class of \(\mathcal O_C(x)\) has degree one. Thus it is the trace-normalized point class. The local group has rank one, and on \(\mathbf P^1\) its map to top cohomology is an isomorphism: the affine complement has only degree-zero constant cohomology, by [The multiplicative group on a curve, Propositions 7.1–7.2](course:ag-etale-cohomology/the-multiplicative-group-on-a-curve), taking \(C=\mathbf P^1\) and \(S=\{\infty\}\). Therefore the equality also holds with support. This proves the local normalization without replacing \(\mathcal O(x)\) by the valuation sequence's \(\mathcal O(-x)\).

Near any point of a smooth divisor \(D\subset X\), its normal parameter \(t\) gives a smooth map to \(\mathbf A^1\), after shrinking. Smooth base change for the complementary open direct image identifies its supported localization triangle with the pullback of that for \(\{0\}\subset\mathbf A^1\). This comparison preserves the orientation just constructed: if \(h:D\to\{0\}\) and \(i_0:\{0\}\hookrightarrow\mathbf A^1\), then \(ti=i_0h\), and composition gives \(Ri^!Rt^!=Rh^!Ri_0^!\). Both \(t\) and \(h\) are smooth of relative dimension \(d-1\). Cancel their common twist and shift. Compatibility of the composite counits identifies this with the supported base-change map. The Kummer pair \((\mathcal O(D),1)\) also pulls back from that normal coordinate, by (1.3)–(1.4). Thus both supported classes agree on these charts. Purity identifies \(H^2_D(X,\mu_n)\) with \(H^0(D,\Lambda_n)\), so their local equality proves their global equality.

The closed adjunction now gives \(i_*1=c_{1,n}(\mathcal O(D))\). Its projection identity gives \(i_*(i^*v)=i_*1\cup v\), and its trace identity gives \(\int_Xi_*i^*v=\int_Di^*v\). These prove (1.6), over every invertible \(n\), including composite \(n\). The corresponding duality pairings are perfect finite-module pairings by the same provider; self-injectivity of \(\mathbf Z/n\) is used, rather than freeness of arbitrary finite modules.

Every map was constructed by Kummer, tensor, or adjunction, so it commutes with coefficient reduction. For the adic passage, [ℓ-adic sheaves and their cohomology, §§5–7](course:AG-LTF/l-adic-sheaves-and-their-cohomology) gives compatible finite-projective models \(P\) with \(P\otimes^L\mathbf Z/\ell^a=R\Gamma(Y,\mathbf Z/\ell^a)\). On these models the finite duality maps identify the reductions of \(P(d)[2d]\) and \(\operatorname{Hom}(P,\mathbf Z_\ell)\). Recovery of compatible morphisms supplies their integral comparison; its cone has every reduction zero, and derived completeness makes that cone zero. Rationalization preserves the comparison and all trace identities. No interchange of an infinite cochain total with inverse limit is needed. \(\square\)

This is the divisor case of Deligne, [Cycle], §§2.1.4–2.1.5, 2.3.2 and Lemma 2.3.6. In (1.4), the localization boundary of the root torsor therefore has trace \(-1\) at a point; the positive degree convention belongs to its negative.

**Lemma 1.2 (the degree of a Chern class on a curve).** For a line bundle \(L\) on a smooth projective curve \(C\),

\[
\int_C c_{1,n}(L)=\deg L\pmod n.
\tag{1.7}
\]

**Proof.** Choose a nonzero rational section of \(L\). Its divisor is \(\sum_x m_x[x]\), and \(L\simeq\mathcal O_C(\sum_xm_x[x])\). Additivity of (1.2) and the trace-\(1\) normalization of a point give \(\int_C c_{1,n}(L)=\sum_xm_x\) in \(\Lambda_n\). Because \(k\) is algebraically closed, every closed point has degree one, so this sum is the degree of \(L\). For a disconnected smooth curve apply this proof component by component. \(\square\)

For later use, a nonconstant map \(\varphi:C\to C\) acts on \(H^2(C,\mathbf Q_\ell)\) by \(\deg\varphi\). To see this at finite level, choose a degree-one line bundle; its Chern class generates \(H^2(C,\mu_n)\) by (1.7). Naturality of \(c_1\), together with \(\deg\varphi^*L=(\deg\varphi)\deg L\), proves the assertion modulo every \(\ell^a\), and hence integrally and rationally. This is [Stacks, Tag 0AMB](https://stacks.math.columbia.edu/tag/0AMB). A constant map acts by zero on \(H^2\), since it factors through a point. We set its degree equal to zero.

### Projective bundles and all Chern classes

The divisor construction extends to vector bundles without assuming that a bundle globally splits into lines. Let \(X/k\) be smooth, separated and finite type, and let \(V\) be a vector bundle of constant rank \(r\geq1\). We use the convention that \(\pi:\mathbf P(V)\to X\) parametrizes lines in \(V\). Its tautological line is \(\mathcal O(-1)\subset\pi^*V\); put \(\xi=c_{1,n}(\mathcal O(1))\).

**Theorem 1.3 (projective-bundle formula).** For every integer \(m,a\), cup product gives an isomorphism

\[
\bigoplus_{j=0}^{r-1}H^{m-2j}(X,\Lambda_n(a-j))
\xrightarrow{\ \sum_j\pi^*(-)\cup\xi^j\ }
H^m(\mathbf P(V),\Lambda_n(a)).
\tag{1.8}
\]

**Proof.** The unit and the powers of \(\xi\) define a map

\[
\bigoplus_{j=0}^{r-1}\Lambda_{n,X}(-j)[-2j]
\longrightarrow R\pi_*\Lambda_{n,\mathbf P(V)}.
\tag{1.9}
\]

Proper base change computes its stalk at \(\bar x\) as the map for \(\mathbf P(V_{\bar x})\). [Smooth traces, duality and Gysin maps, Proposition 14.1](course:AG-LTF/smooth-trace-and-duality) computes the cohomology of projective space: it is one free copy of \(\Lambda_n(-j)\) in degree \(2j\), generated by the \(j\)-th power of the hyperplane class, and zero otherwise. Proposition 1.1 supplies its positive Kummer normalization. Hence (1.9) is an isomorphism at every stalk. Taking derived global sections, and then degree \(m\) after twisting by \(a\), proves (1.8). The construction preserves cup products and pullbacks, since its maps are the unit and cup product with the pulled-back tautological class. \(\square\)

Apply (1.8) to \(\xi^r\). There are unique classes \(c_j^{(n)}(V)\in H^{2j}(X,\Lambda_n(j))\) such that

\[
\xi^r+\pi^*c_1^{(n)}(V)\cup\xi^{r-1}
+\cdots+\pi^*c_r^{(n)}(V)=0.
\tag{1.10}
\]

Set \(c_0^{(n)}(V)=1\), and \(c_j^{(n)}(V)=0\) for \(j>r\). A rank-zero bundle has total class \(1\). These are the Chern classes. For a line \(L\), \(\mathbf P(L)=X\), \(\mathcal O(1)=L^{-1}\), and (1.10) says \(c_1^{(n)}(L)=-c_{1,n}(L^{-1})=c_{1,n}(L)\). The plus signs in (1.10) depend on our lines convention for \(\mathbf P(V)\).

**Theorem 1.4 (functoriality and Whitney formula).** For a morphism \(f:Y\to X\) of smooth schemes,

\[
c_j^{(n)}(f^*V)=f^*c_j^{(n)}(V).
\tag{1.11}
\]

For every exact sequence \(0\to V'\to V\to V''\to0\) of vector bundles, writing \(c_t(V)=\sum_j c_j^{(n)}(V)t^j\), one has

\[
c_t(V)=c_t(V')c_t(V'').
\tag{1.12}
\]

Functoriality, the line normalization and (1.12) characterize the classes uniquely.

**Proof.** Pullback of the tautological line and (1.10) gives (1.11), by uniqueness of its coefficients. We give the splitting argument needed for (1.12), including the injectivity on cohomology.

First, if \(V=\bigoplus_{i=1}^rL_i\), put \(x_i=c_{1,n}(L_i)\). On \(\mathbf P(V)\), projection of the tautological line to \(\pi^*L_i\) is a section of \(\mathcal O(1)\otimes\pi^*L_i\). For \(r>1\) its zero divisor is the smooth projective subbundle \(\mathbf P(\bigoplus_{h\ne i}L_h)\); its supported Kummer class maps to \(\xi+\pi^*x_i\). The supported cup product of all these classes has support in their intersection, which is empty: a line cannot have all coordinates zero. Hence

\[
\prod_{i=1}^r(\xi+\pi^*x_i)=0.
\tag{1.13}
\]

For \(r=1\), the section is nowhere zero and the same identity is the line normalization. Uniqueness in (1.10) now gives

\[
c_t(V)=\prod_i(1+x_it).
\tag{1.14}
\]

Next pull a general bundle to its complete flag bundle, constructed by successively choosing a line in the bundle and a line in the remaining quotient. Each stage is a projective bundle. Its pullback is injective by the \(j=0\) summand of (1.8), so the composite pullback is injective. On the flag bundle the pulled bundle has a filtration by line-bundle quotients, but such a filtration need not split. For each extension \(0\to A\to B\to L\to0\), the scheme of splittings is a torsor under the vector bundle \(\mathcal Hom(L,A)\). It exists because the extension splits on any affine open where \(L\) is free: lift its basis to \(B\). The differences of two lifts lie in \(A\), which gives the torsor charts and transition translations. Pulling to that torsor supplies an actual splitting.

An affine-bundle torsor \(q:T\to Z\) induces an isomorphism on constant-coefficient étale cohomology. To check this, work on its Zariski charts \(T|_W=\mathbf A^s\times W\). [Cohomological dimension and the Künneth formula, Theorem 11.1](course:ag-etale-cohomology/cohomological-dimension-and-the-kunneth-formula) identifies the direct image of the constant sheaf there with the constant complex \(R\Gamma(\mathbf A^s,\Lambda_n)\) on \(W\). The affine-line calculation in [The multiplicative group on a curve, §7](course:ag-etale-cohomology/the-multiplicative-group-on-a-curve), iterated by Künneth, makes that complex \(\Lambda_n\) in degree zero. Thus the unit \(\Lambda_{n,Z}\to Rq_*\Lambda_{n,T}\) is locally, and hence globally, an isomorphism. It proves the asserted cohomology isomorphism, with every twist. Successively taking these splitting torsors therefore keeps the flag pullback injective and makes the pulled bundle a direct sum of lines. All bases remain smooth over \(k\).

For the given sequence, first take its splitting torsor, then flag bundles for \(V'\) and \(V''\), then the splitting torsors of their line filtrations. The resulting pullback on cohomology is injective. On that base the three bundles are direct sums of the same line summands, with those for \(V\) the union of those for \(V'\) and \(V''\). Formula (1.14) proves (1.12) there. Functoriality (1.11) and injectivity prove it on \(X\). This proves the Whitney formula for nonsplit extensions, for every invertible \(n\), without division by a factorial. Finally any classes with the three stated properties give (1.14) after the same injective splitting construction, hence agree with ours on \(X\). This proves uniqueness. \(\square\)

The same argument computes duals, exterior powers and tensor products. On a common splitting base their roots are respectively \(-x_i\), the sums \(\sum_{i\in I}x_i\) for \(|I|=s\), and \(x_i+y_j\). Therefore

\[
\begin{aligned}
c_t(V^\vee)&=\prod_i(1-x_it),\\
c_t(\mathop{\bigwedge}\nolimits^s V)&=
\prod_{|I|=s}\left(1+t\sum_{i\in I}x_i\right),\\
c_t(V\otimes W)&=\prod_{i,j}(1+t(x_i+y_j)).
\end{aligned}
\tag{1.14a}
\]

These are symmetric polynomials separately in the two sets of roots, and hence integer polynomials in the original Chern classes. Injectivity descends them; no division is involved. In particular \(c_j(V^\vee)=(-1)^jc_j(V)\).

Coefficient reduction preserves \(\xi\), (1.9), and the unique relation (1.10). Thus all the Chern classes are compatible at \(n=\ell^a\); their inverse limits and rationalizations give the same formulas over \(\mathbf Z_\ell\) and \(\mathbf Q_\ell\). The finite-to-adic complex comparison of Proposition 1.1 proves (1.8) in those coefficients as well.

Over \(E=\mathbf Q_\ell\), the **Chern character** is a different invariant. If \(x_i\) are the line classes on the injective splitting construction, define it by

\[
\operatorname{ch}(V)=\sum_{i=1}^r\exp(x_i)
=r+c_1(V)+\frac{c_1(V)^2-2c_2(V)}2+\cdots.
\tag{1.15}
\]

Each term is the corresponding symmetric polynomial in the Chern classes, so it is defined already on \(X\), independently of that construction. The exponential is a finite sum in cohomology because positive-degree classes are nilpotent by the finite dimension bound. Splitting proves \(\operatorname{ch}(V)=\operatorname{ch}(V')+\operatorname{ch}(V'')\) for an exact sequence, and \(\operatorname{ch}(V\otimes W)=\operatorname{ch}(V)\operatorname{ch}(W)\): on a common splitting base the tensor roots are \(x_i+y_j\), and \(\exp(x_i+y_j)=\exp(x_i)\exp(y_j)\). Injectivity descends both equalities. Thus it gives a ring homomorphism from \(K_0\) of vector bundles to even rational cohomology. The alternating \(K_0\)-class of a vector-bundle resolution is \(\sum_i(-1)^i[V_i]\); its Chern character is \(\sum_i(-1)^i\operatorname{ch}(V_i)\). These two sums live in different groups.

This completes the projective-bundle and Chern-class assertions used in Milne [LEC], §23. The distinction in the last paragraph also removes the ambiguity noted in that section between a \(K_0\)-class, a total Chern class and a Chern character.

### Supported classes of singular cycles

Purity for a smooth pair also supplies the vanishing needed to define classes of singular subvarieties. No purity theorem for an arbitrary singular pair is assumed.

**Lemma 1.5 (semi-purity).** Let \(X/k\) be smooth of pure dimension \(d\), and let \(Z\subset X\) be closed with \(\dim Z\leq d-c\). Then

\[
Ri^!\Lambda_n\in D^{\geq2c}(Z,\Lambda_n),\qquad
H^r_Z(X,\Lambda_n(a))=0\quad(r<2c).
\tag{1.16}
\]

**Proof.** Put \(m=d-c\). The compact dimension bound gives \(Rp_{Z,!}D^{\leq b}\subset D^{\leq b+2m}\), including unbounded-below complexes; [Cohomology with compact support, §§5 and 7–8](course:ag-etale-cohomology/cohomology-with-compact-support) constructs this bounded derived functor. Its right adjoint is constructed in §8 of the smooth-duality provider. It follows that \(Rp_Z^!\Lambda_n\in D^{\geq-2m}\). Explicitly, for \(B=\tau_{\leq-2m-1}Rp_Z^!\Lambda_n\), adjunction identifies its truncation inclusion with a map from \(Rp_{Z,!}B\in D^{\leq-1}\) to \(\Lambda_n\in D^{\geq0}\), hence with zero. The inclusion induces the identity on the cohomology of \(B\), so those groups vanish. Since \(p_Z=p_Xi\), composition and smooth duality give

\[
Ri^!\Lambda_n(d)[2d]=Rp_Z^!\Lambda_n\in D^{\geq-2m}.
\]

Cancel the twist and shift to obtain the first assertion of (1.16). Derived global sections preserve the lower cohomology bound, and \(R\Gamma_Z(X,-)=R\Gamma(Z,Ri^!(-))\); this proves the second assertion. The same reasoning applies to every invertible twist. \(\square\)

For an integral closed subvariety \(Z\) of codimension \(c\), let \(Z^\circ\) be its smooth locus and \(W=Z-Z^\circ\). It is dense because \(k\) is perfect. Thus \(W\) has codimension at least \(c+1\) in \(X\). The localization sequence for nested supports, together with (1.16), gives

\[
H^{2c}_Z(X,\Lambda_n(c))
\xrightarrow{\sim}H^{2c}_{Z^\circ}(X-W,\Lambda_n(c))
\simeq H^0(Z^\circ,\Lambda_n).
\tag{1.17}
\]

The two groups of support in \(W\) that surround this restriction have degrees \(2c\) and \(2c+1\), both below \(2c+2\), and hence vanish. The second isomorphism is smooth-pair purity. Define the supported fundamental class of \(Z\) to be the unique inverse image of \(1\). Its ordinary image is \(\operatorname{cl}_X(Z)\in H^{2c}(X,\Lambda_n(c))\). Removing a further proper closed subset of \(Z^\circ\) gives the same class, by the same vanishing argument. Extend by integral linearity to cycles, including negative coefficients.

For codimension one, a prime divisor on the regular scheme \(X\) is Cartier. Proposition 1.1 identifies its supported Kummer class with \(1\) on its smooth locus. The uniqueness in (1.17) consequently identifies its global ordinary class with \(c_{1,n}(\mathcal O_X(Z))\), even when the divisor is singular. This gives the divisor normalization for all cycles of codimension one, not just smooth divisors. Reduction of coefficients preserves the construction and its unique support lift.

**Theorem 1.6 (a transverse zero section).** If \(s\) is a section of a rank-\(r\) vector bundle \(V\) on smooth \(X\), transverse to its zero section, its zero scheme \(Z\) is smooth of codimension \(r\), and

\[
\operatorname{cl}_X(Z)=c_r^{(n)}(V).
\tag{1.18}
\]

**Proof.** Compactify the total space of \(V\) by \(\overline V=\mathbf P(V\oplus\mathcal O_X)\). The complement of \(\mathbf P(V)\) is the total space of \(V\), sending \(v\) to the line spanned by \((v,1)\). Write \(\xi=c_1(\mathcal O_{\overline V}(1))\), and \(s_0:X\hookrightarrow\overline V\) for the zero section. We claim

\[
\operatorname{cl}_{\overline V}(s_0(X))
=\xi^r+\pi^*c_1(V)\cup\xi^{r-1}+\cdots+\pi^*c_r(V).
\tag{1.19}
\]

Use the flag and affine splitting construction in Theorem 1.4. It preserves the Gysin class under smooth pullback, by the smooth normal-coordinate comparison in Proposition 1.1 and composition for a smooth flag. The pullback on the cohomology of \(\overline V\) is injective as well: (1.8) decomposes it into the injective pullbacks on \(X\), with the same powers of \(\xi\). We can consequently verify (1.19) for \(V=\bigoplus_i L_i\).

In that case the zero section is the common zero set of the \(r\) tautological coordinate sections of \(\mathcal O(1)\otimes\pi^*L_i\). Their successive zero sets are smooth projective subbundles, ending at \(\mathbf P(\mathcal O_X)=X\). Their normal parameters are independent. Gysin composition and its projection formula therefore identify the zero-section class with \(\prod_i(\xi+\pi^*x_i)\). Expanding by (1.14) gives (1.19), and injectivity proves it for the original bundle.

On the total space \(V\), \(\mathcal O(-1)\) is trivialized by \((v,1)\), so \(\xi\) restricts to zero. Pulling (1.19) along any section \(s:X\to V\) gives \(s^*\operatorname{cl}(s_0(X))=c_r(V)\). If \(s\) is transverse, its pullback of the normal parameters is a regular coordinate system normal to \(Z\). The supported purity class consequently pulls back to the positive class of \(Z\): étale locally this is the product of the divisor normalizations in Proposition 1.1, and their even degrees give no ordering sign. Forgetting support proves (1.18). \(\square\)

### Local multiplicities

For a finite scheme \(Z\) over \(k\), its cycle is \(\sum_x\operatorname{length}(\mathcal O_{Z,x})[x]\). A regular sequence can have such a nonreduced zero scheme. Its cohomological class retains these lengths.

**Lemma 1.7 (pulling back a point orientation).** Let \(x\) be a closed point of a smooth \(d\)-dimensional scheme \(U/k\). Let \(f_1,\ldots,f_d\) be regular functions near \(x\), with an isolated common zero there. Write \(f:U\to\mathbf A^d\) for their map, and let \(\eta_0\in H^{2d}_{\{0\}}(\mathbf A^d,\Lambda_n(d))\) be the positive point class. After restricting support to \(x\),

\[
\begin{aligned}
f^*\eta_0&=e_x\operatorname{cl}_U(x),\\
e_x&=\operatorname{length}(A/I).
\end{aligned}
\tag{1.20}
\]

Here \(A=\mathcal O_{U,x}\) and \(I=(f_1,\ldots,f_d)\). The equality is in supported cohomology, and reduces the integer \(e_x\) modulo \(n\).

**Proof.** Choose étale coordinates \(u_1,\ldots,u_d\) vanishing at \(x\). Introduce a parameter \(a\) and the map \(F:U\times\mathbf A^1\to\mathbf A^d\times\mathbf A^1\) defined by

\[
\begin{aligned}
F_a(u)&=(f_j(u)-au_j)_{j=1}^d,\\
F(u,a)&=(F_a(u),a).
\end{aligned}
\tag{1.21}
\]

At \((x,0)\) its fibre is isolated. The finite-neighbourhood lemma for a quasi-finite morphism supplies an elementary étale neighbourhood \(Y\) of \((0,0)\) in the target and an open \(W\subset (U\times\mathbf A^1)\times_{\mathbf A^d\times\mathbf A^1}Y\), finite over \(Y\), whose fibre at the distinguished point consists just of \((x,0)\). Here elementary means that the distinguished residue field is unchanged. The lemma applies to any isolated point in a finite-type fibre; it does not require that \(F\) be étale. Its algebraic proof uses the integral closure in Zariski's main theorem, separates the chosen finite fibre factor by an idempotent after an étale extension, and removes the closed image of the other factors. Its exact scheme proof homes are the AI Integrated Stacks [finite-neighbourhood lemma for an isolated fibre point](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-etale-makes-quasi-finite-finite-at-point) and [the corresponding finite-algebra decomposition](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-etale-makes-quasi-finite-finite-one-prime); the latter includes the polynomial-factor lifting and finite-algebra argument.

Both \(Y\) and \(W\) are smooth over the parameter line, of relative dimension \(d\): their maps to the corresponding products are étale, followed by an open restriction. Near the distinguished point the finite map \(h:W\to Y\) is flat. To verify this, the target's regular local parameters pull back to a system of parameters in the source's regular local ring. A regular local ring is Cohen–Macaulay, so this system is a regular sequence. Its Koszul complex computes \(\operatorname{Tor}^{\mathcal O_Y}_i(k,\mathcal O_W)=0\) for \(i>0\). A minimal free resolution over the regular target then has no positive terms: after tensoring with its residue field all its differentials are zero, so a positive term would give a nonzero Tor group. Thus \(\mathcal O_W\) is free over \(\mathcal O_Y\). Shrink the target to remove the closed image of the nonflat locus. The rank is \(e_x\), because the distinguished fibre has that length and residue field \(k\). Take the connected component of the target containing that point.

Let \(q:Y\to\mathbf A^1\) and \(p:W\to\mathbf A^1\) be the structure maps. Their smooth exceptional-inverse-image formulas, and \(p=qh\), give

\[
h^!\Lambda_{n,Y}=\Lambda_{n,W}.
\]

We use the orientation defined by these relative smooth formulas. The finite counit gives a trace \(h_*\Lambda_{n,W}\to\Lambda_{n,Y}\). Compose it with the constant-section map \(\Lambda_{n,Y}\to h_*\Lambda_{n,W}\); the result is a locally constant scalar on \(Y\). On the dense étale locus it is the sum over \(e_x\) sheets, hence multiplication by \(e_x\). This locus is nonempty on each source component meeting the distinguished fibre. Indeed, along the section \(x\times\mathbf A^1\) the relative Jacobian is \(df_x-aI\), whose determinant is a polynomial with leading term \((-a)^d\). Each component through \((x,0)\) is regular and contains an open of that lifted section, so this determinant is not identically zero there. Other source components can be removed with their closed finite images before shrinking. The scalar is consequently \(e_x\) everywhere on the connected target.

This trace calculation specializes to \(a=0\). More explicitly, the smooth orientations of \(p\) and \(q\), their traces and the lower-shriek projection and base-change maps all commute with arbitrary base change in the parameter, by [Smooth traces, duality and Gysin maps, §§2 and 9](course:AG-LTF/smooth-trace-and-duality). Their adjoints therefore give the same orientation and counit for \(h_0:W_0\to Y_0\). Thus \(h_{0,*}h_0^*\eta_0=e_x\eta_0\), by the projection formula. These statements hold with support at the distinguished fibre, by applying the same maps to the localization triangles.

Purity makes \(H^{2d}_x(W_0,\Lambda_n(d))\) one free copy of \(\Lambda_n\), generated by its point orientation. The supported pushforward of that generator to \(Y_0\) is its point orientation: composition with the point's closed counit is the counit for the same \(k\)-point in \(Y_0\). Therefore the coefficient of \(h_0^*\eta_0\) is \(e_x\). Étale excision identifies this with the original local pullback by \(f\). This proves (1.20), including when the original map is inseparable. The deformation's étale locus was used to compute the constant scalar; no separability of \(f\) was assumed. \(\square\)

**Corollary 1.8 (a regular section, with multiplicities).** Let a section \(s\) of a rank-\(r\) vector bundle \(V\) on smooth \(X\) have a zero scheme \(Z\) of pure codimension \(r\). Then

\[
c_r^{(n)}(V)=\operatorname{cl}_X([Z]),\qquad
[Z]=\sum_T\operatorname{length}(\mathcal O_{Z,\eta_T})[T],
\tag{1.22}
\]

where \(T\) runs through its reduced irreducible components.

**Proof.** The \(r\) local equations form a regular sequence, since they have height \(r\) in a Cohen–Macaulay regular local ring. The compactified zero-section calculation (1.19) still gives \(s^*\operatorname{cl}(s_0(X))=c_r(V)\); its supported version has support in \(Z\). We calculate its coefficient on a dense smooth open of each \(T\).

Choose \(\dim T\) local functions whose restrictions are étale coordinates on that open of \(T\). They give a map to \(\mathbf A^{\dim T}\) that is smooth on a neighbourhood in \(X\). Pass to its geometric generic fibre. That fibre is smooth of dimension \(r\), and the chosen component contributes isolated zeros of the pulled-back section. The length at each zero is \(\operatorname{length}(\mathcal O_{Z,\eta_T})\): the extension of function fields on \(T\) is finite separable, so each embedding into the geometric generic field gives one point, and its Artinian local algebra has the same length after extending its residue field. Lemma 1.7 calculates the pullback of the zero-section orientation there as exactly that multiple of the point orientation. Formation of the normal-coordinate orientations commutes with this smooth localization and geometric field extension. Purity identifies the coefficient with a locally constant section on the smooth open of \(T\), so the generic calculation determines it throughout that open.

Finally remove the complements of these opens and the intersections of distinct components. Their codimension in \(X\) is at least \(r+1\). Semi-purity makes restriction on degree \(2r\) supported cohomology an isomorphism, as in (1.17). Thus the calculated coefficients uniquely determine the class on all of \(Z\). Forget support to obtain (1.22). \(\square\)

### Rational equivalence and the direct cycle map

For a smooth \(X\), the group \(CH^c(X)\) is the group of codimension-\(c\) cycles modulo the divisors \(\operatorname{div}_W(g)\), pushed into \(X\), for integral codimension-\((c-1)\) subvarieties \(W\) and \(g\in k(W)^\times\). Orders on a possibly nonnormal \(W\) can be computed by its finite normalization: sum the discrete valuations above a codimension-one point, weighted by their residue degrees. This is the usual rational-equivalence relation.

We first record the proper map needed in this argument. If \(f:Y\to X\) is proper between smooth schemes of pure dimensions \(m,d\), composition of their structure-map right adjoints gives

\[
Rf^!\Lambda_{n,X}=\Lambda_{n,Y}(m-d)[2m-2d].
\]

Its counit, after twisting and shifting, defines

\[
f_*:H^j(Y,\Lambda_n(a))\longrightarrow
H^{j+2(d-m)}(X,\Lambda_n(a+d-m)).
\tag{1.23}
\]

It also acts with support in a closed subset of \(Y\), with target support its image. Apply the counit to the support localization triangles to get that version. Counits for composite adjunctions prove composition of these maps. The projection formula and compatibility with trace follow by the same argument as for a closed immersion in Proposition 1.1. This construction is local for an open restriction of the target: proper base change identifies the lower direct images, and the smooth dualizing complexes identify their adjoints. All of these are the proved adjunction operations in the smooth-duality provider, §§8–12.

**Lemma 1.9 (degree for a finite smooth map).** Let \(h:Y\to Z\) be a finite dominant map between connected smooth \(m\)-dimensional schemes. If \(e=[k(Y):k(Z)]\), then \(h_*1=e\) in \(H^0(Z,\Lambda_n)\), also for an inseparable extension.

**Proof.** Finite dominance and the regular local parameters show that \(h\) is flat. More explicitly, localize its finite direct-image algebra at a target point. The target parameters are a system of parameters at each of the finitely many source points above it, so they form a regular sequence in each regular source local ring. Their Koszul complex is consequently acyclic in positive degrees in the entire finite algebra. It computes vanishing of its positive Tor groups with the target residue field. The minimal-resolution argument in Lemma 1.7 then makes this finite target module free. Its constant rank is the function-field degree \(e\). Choose a closed point \(z\). Its fibre's local lengths add to \(e\), since \(k\) is algebraically closed. Lemma 1.7 applied at each point of the fibre gives \(h^*\operatorname{cl}_c(z)=\sum_y e_y\operatorname{cl}_c(y)\). The projection formula, followed by trace, gives

\[
\int_Z(h_*1)\cup\operatorname{cl}_c(z)
=\int_Yh^*\operatorname{cl}_c(z)=\sum_y e_y=e.
\]

Trace of a compact point class is one, and \(h_*1\) is a constant scalar on connected \(Z\). Therefore that scalar is \(e\). The same argument works for \(m=0\); over our algebraically closed field its connected reduced schemes are single points. \(\square\)

In particular, for a finite proper map \(f:Y\to X\) between smooth schemes, the supported pushforward of the class of an integral subvariety \(T\subset Y\) is the class of \([k(T):k(f(T))]\,[f(T)]\). Here is the local verification. Remove the singular loci of \(T\) and \(f(T)\), and the images of the omitted part of \(T\). Their images have codimension at least one more than \(f(T)\). On the remaining open both subvarieties are smooth, and their restricted finite map has the same function-field degree. Compose its counit with the two closed-immersion counits. Lemma 1.9 computes its degree-zero scalar, while smooth-pair purity identifies the resulting supported classes. Semi-purity then uniquely restores the equality over the omitted subset, just as in (1.17). This proves the assertion for singular cycles as well.

**Theorem 1.10 (rational equivalence).** The supported construction induces a homomorphism

\[
\operatorname{cl}_X^c:CH^c(X)\longrightarrow H^{2c}(X,\Lambda_n(c)).
\tag{1.24}
\]

It agrees with \(c_{1,n}\) on \(CH^1(X)=\operatorname{Pic}(X)\), and is compatible with coefficient reduction, the adic limit and rationalization.

**Proof.** Consider a generator \(\operatorname{div}_W(g)\) of rational equivalence, where \(m=\dim W=d-c+1\). Normalize \(W\), giving \(\nu:\widetilde W\to W\). Its normalization is finite, since a finite-type algebra over a field has finite normalization. The normal variety \(\widetilde W\) is regular at every codimension-one point and at its generic point. Over the perfect field \(k\), its nonsmooth locus \(S\) therefore has dimension at most \(m-2\). Put \(B=\nu(S)\), viewed as closed in \(X\). Then \(\operatorname{codim}_X B\geq c+1\). On \(X'=X-B\), the inverse image \(Y=\widetilde W-\nu^{-1}(B)\) is smooth; it maps finitely and properly to \(X'\).

The rational function \(g\) defines a principal Cartier divisor on the regular scheme \(Y\). By the divisor normalization following (1.17), its ordinary cohomological cycle class is

\[
\operatorname{cl}_Y(\operatorname{div}_Y(g))
=c_{1,n}(\mathcal O_Y(\operatorname{div}_Y(g)))=0.
\]

The finite pushforward calculation just proved identifies its image under (1.23) with \(\operatorname{cl}_{X'}(\operatorname{div}_W(g)|_{X'})\). This identification uses exactly the residue-degree weights in the definition of the divisor on \(W\). For completeness, at a codimension-one local domain \(A\) with finite semilocal normalization \(\overline A\), the quotient \(\overline A/A\) has finite length. For a nonzero \(a\in A\), the kernel and cokernel of multiplication by \(a\) on that quotient have equal length. The exact sequence of multiplication by \(a\) therefore gives \(\operatorname{length}(A/aA)=\operatorname{length}(\overline A/a\overline A)\). The latter is the sum of \(\operatorname{ord}_v(a)[\kappa(v):\kappa(A)]\) over its discrete valuation rings. Subtract the identities for numerator and denominator of \(g\). This proves the required normalization formula directly, including for a nonnormal \(W\).

Thus the restricted cycle class is zero. Semi-purity gives \(H^{2c}_B(X,\Lambda_n(c))=0\), so the restriction \(H^{2c}(X,\Lambda_n(c))\to H^{2c}(X',\Lambda_n(c))\) is injective. The original class is zero as well. Every rational-equivalence generator is killed, proving (1.24). Its codimension-one normalization was already established by (1.17). Every construction preserves coefficient reduction. The supported classes and maps have compatible finite-projective adic comparisons as in Proposition 1.1, giving the final assertions. \(\square\)

### Specialization and the full cycle map

We next keep the finite coefficients throughout the intersection argument. An equality over \(\mathbf Q_\ell\) would not determine its possible torsion difference over \(\mathbf Z_\ell\).

**Lemma 1.10a (proper pushforward and smooth pullback).** The direct cycle map commutes with every proper map between smooth separated finite-type schemes, with the degree and twist in (1.23), and with every smooth pullback. These assertions hold with support.

**Proof.** Let \(f:Y\to X\) be proper, with dimensions \(m,d\), and let \(T\subset Y\) be integral of dimension \(t\). Its class has degree \(2(m-t)\). Its supported pushforward has degree \(2(d-t)\), with support in \(V=f(T)\). If \(\dim V<t\), semi-purity makes this support group zero. This agrees with the definition \(f_*[T]=0\) in Chow groups.

Suppose \(\dim V=t\). The proper generically finite map \(T\to V\) is finite over a dense open of \(V\): its quasi-finite locus contains the generic fibre, the complement has closed proper image, and a proper quasi-finite map is finite. Remove that image, the nonsmooth locus of \(V\), and the image of the nonsmooth locus of the resulting finite source. All removed subsets of \(V\) have dimension at most \(t-1\). On the remaining open \(T\) and \(V\) are smooth, and \(T\to V\) is finite of degree \(e=[k(T):k(V)]\). Composition of its counit with the two closed-immersion counits and Lemma 1.9 give \(f_*\operatorname{cl}(T)=e\operatorname{cl}(V)\) there. The omitted target support has codimension at least \(d-t+1\). Its cohomology in degrees \(2(d-t)\) and \(2(d-t)+1\) vanishes, so the equality extends uniquely. This proves the proper assertion for all cycles and hence for Chow classes.

For a smooth map \(p:Y\to X\), the inverse image of the smooth locus of an integral \(T\) is smooth and reduced. Its components have multiplicity one. Smooth base change for normal parameters and purity therefore identifies \(p^*\operatorname{cl}(T)\) with the fundamental classes of these components. The inverse image of the omitted part has one greater codimension, since a smooth map has locally constant relative dimension. Semi-purity extends the supported equality. Linearity gives the assertion. \(\square\)

For a smooth Cartier divisor \(i:D\hookrightarrow M\), smooth-pair purity identifies the counit on \(D\) with a morphism
\(\Lambda_{n,D}(-1)[-2]\to\Lambda_{n,D}\).
Its class is \(i^*i_*1=i^*c_1(\mathcal O_M(D))=c_1(N_{D/M})\), by the supported divisor normalization. This is a morphism of \(\Lambda_{n,D}\)-complexes, so its action on any cohomology class is cup product with that class. Thus

\[
i^*i_*b=c_1(N_{D/M})\cup b.
\tag{1.24a}
\]

This argument also identifies cup product with the supported divisor class as \(i_*i^*\), by the counit's projection formula. Neither identity requires that \(b\) lift from \(M\).

**Lemma 1.10b (a fibre of a cycle).** Let \(M\to\mathbf A^1\) be smooth, and let \(T\subset M\) be integral of codimension \(c\), dominating the parameter line. For a fibre \(M_s\), write \(T_s\) for its scheme-theoretic fibre, retaining the lengths at its generic points. Then, in cohomology with support in \(|T_s|\),

\[
i_s^*\operatorname{cl}_M(T)=\operatorname{cl}_{M_s}([T_s]).
\tag{1.24b}
\]

**Proof.** Normalize \(T\). Its nonsmooth locus has codimension at least two in the normalization. Its finite image \(B\) has codimension at least \(c+2\) in \(M\), and at least \(c+1\) in \(M_s\). Remove \(B\); semi-purity will restore the supported equality on \(M_s\) at the end. The remaining normalization \(Y\) is smooth, and its finite map \(\nu:Y\to M-B\) has generic degree one onto \(T-B\). Lemma 1.10a gives \(\nu_*1=\operatorname{cl}(T)\).

The parameter \(t-s\) is a nonzerodivisor on \(Y\). Its zero divisor \(E\) may be nonreduced, but its supported Kummer class is the weighted fundamental class \(\operatorname{cl}_Y([E])\), by the divisor calculation after (1.17). Pullback of the supported class of \(M_s\) is this supported Kummer class: both are the connecting class of the line bundle with its specified trivialization outside the zero divisor. The projection formula with support consequently gives

\[
\begin{aligned}
\operatorname{cl}_M(T)\cup\operatorname{cl}_M(M_s)
&=\nu_*\operatorname{cl}_Y([E])\\
&=i_{s,*}\operatorname{cl}_{M_s}([T_s]).
\end{aligned}
\tag{1.24c}
\]

The second equality uses Lemma 1.10a twice, first for \(\nu\) and then for \(i_s\). The normalization valuation-length identity in the proof of Theorem 1.10 says precisely that \(\nu_*[E]=[T_s]\) as cycles. Thus it includes every residue degree and nonreduced fibre length. The first member of (1.24c) is \(i_{s,*}i_s^*\operatorname{cl}_M(T)\). Purity for the smooth pair \(M_s\subset M\) makes

\[
H^{2c}_{|T_s|}(M_s,\Lambda_n(c))
\xrightarrow{\ i_{s,*}\ }
H^{2c+2}_{|T_s|}(M,\Lambda_n(c+1))
\]

an isomorphism. Cancel it to obtain (1.24b) on \(M_s-B\). The two support groups for the omitted \(B\cap M_s\) vanish in degrees \(2c,2c+1\), restoring the equality uniquely on the entire fibre. \(\square\)

We recall the algebraic construction of the refined Chow pullback used next. Its exact written homes are the AI Integrated Stacks [vector-bundle homotopy formula](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/chow.html#chow-lemma-vectorbundle), [normal-cone deformation](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/chow.html#chow-section-blowup-Z-first), and [construction of the higher-codimension Gysin operation](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/chow.html#chow-lemma-construction-gysin). These are algebraic Chow constructions; no étale cycle-map compatibility is among their premises. Here is the content needed in the comparison.

For a vector bundle \(p:N\to Z\) of rank \(r\), flat pullback
\(p^*:CH^c(Z)\to CH^c(N)\) is an isomorphism. One can see its surjectivity first for an affine line. An integral cycle \(W\subset Z\times\mathbf A^1\) either is the full inverse image of its image \(V\), or is generically a divisor over \(V\). In the latter case an irreducible polynomial in \(k(V)[t]\) defines that generic divisor with coefficient one. Its rational divisor on \(V\times\mathbf A^1\) expresses \([W]\), modulo rational equivalence, as a sum of vertical divisors. Every vertical divisor is \(V'\times\mathbf A^1\), by dimension. Iteration handles affine space. Local triviality of a vector bundle, Chow localization and Noetherian induction then give surjectivity for \(N\).

For injectivity, compactify \(N\) to \(P=\mathbf P(N\oplus\mathcal O)\), with divisor at infinity \(P(N)\) and hyperplane class \(h\). The Chow projective-bundle formula has the basis \(1,h,\ldots,h^r\) over \(CH^*(Z)\). Its surjectivity follows by the same affine-space argument on the standard projective strata and localization. Its injectivity follows by pushing to \(Z\): powers below \(r\) push to zero and \(h^r\) pushes to one, by the degree of the linear fibre intersection. In a relation, push first to kill the highest coefficient, then multiply by \(h\) and repeat to kill the next; this ends with the constant coefficient. If \(p^*\alpha=0\), localization expresses the pullback of \(\alpha\) on \(P\) as a pushforward from \(P(N)\). The latter has only basis terms \(h,h^2,\ldots,h^r\), because the infinity divisor has class \(h\). Its constant coefficient is therefore zero, giving \(\alpha=0\). This proves the asserted homotopy formula.

For a closed immersion \(i:Z\hookrightarrow X\) between smooth schemes, with normal bundle \(p:N_{Z/X}\to Z\), let

\[
\mathcal D=\operatorname{Bl}_{Z\times\{0\}}(X\times\mathbf A^1)
\setminus\widetilde{X\times\{0\}}.
\tag{1.24d}
\]

It has a map \(q:\mathcal D\to X\). Over the nonzero parameter it is \(X\times\mathbf G_m\); its zero fibre is \(N_{Z/X}\), on which \(q=ip\). If \(I\subset A\) cuts out \(Z\) on an affine open of \(X\), its affine algebra is

\[
A[t,I/t]\subset A[t,t^{-1}],\qquad
A[t,I/t]/(t)=\bigoplus_{a\geq0}I^a/I^{a+1}.
\tag{1.24e}
\]

These identifications follow directly from the chart of the blowup where the generator \(t\) is distinguished. Since \(X,Z\) are smooth, étale coordinates make \(I=(x_1,\ldots,x_r)\). The chart then has coordinates \(v_j=x_j/t\), the remaining coordinates of \(Z\), and \(t\). Thus \(\mathcal D\to\mathbf A^1\) is smooth, and the zero fibre is the normal vector bundle.

For an integral \(W\subset X\), close \(W\times\mathbf G_m\) in \(\mathcal D\), obtaining \(\widetilde W\). It dominates the line and is flat over it: its local algebras are torsion-free \(k[t]\)-modules, hence flat. If \(J\) cuts out \(W\), its chart is
\((A/J)[t,\overline I/t]\).
The zero fibre is therefore the normal cone \(C_{Z\cap W}W\), with its actual scheme multiplicities, regarded as a cycle in \(N_{Z/X}\). Denote its class by \(\operatorname{sp}_i[W]\). The refined Chow pullback, pushed into \(Z\), is

\[
i^![W]=(p^*)^{-1}\operatorname{sp}_i[W].
\tag{1.24f}
\]

This is the normal-cone definition of the Gysin operation in the stated algebraic proof home. Chow localization and the Cartier-divisor operation on the deformation show that it descends through rational equivalence, and the vector-bundle isomorphism makes the inverse in (1.24f) unique. For a map \(f:X'\to X\) between smooth schemes, its Chow pullback is the smooth pullback along \(X'\times X\to X\) followed by the refined pullback along its graph. The diagonal gives the intersection product.

**Theorem 1.10c (the cycle map with finite and integral coefficients).** For every smooth separated finite-type scheme \(X/k\), the maps (1.24) form a graded ring homomorphism

\[
\operatorname{cl}_X:CH^*(X)\longrightarrow
\bigoplus_c H^{2c}(X,\Lambda_n(c)).
\tag{1.24g}
\]

They commute with every pullback between smooth schemes and every proper pushforward, and take the Chow Chern classes to the classes of Theorem 1.4. The same assertions hold with \(\mathbf Z_\ell\) coefficients and after rationalization. No projective embedding or bound on the invertible integer \(n\) is required.

**Proof.** First consider \(i:Z\hookrightarrow X\) between smooth schemes and the deformation just constructed. For a codimension-\(c\) integral \(W\subset X\), both \(q^*\operatorname{cl}_X(W)\) and \(\operatorname{cl}_{\mathcal D}(\widetilde W)\) restrict on \(X\times\mathbf G_m\) to the same class, by Lemma 1.10a. Their difference is the image of a class supported in the zero fibre \(N\). Purity identifies such a class with \(b\in H^{2c-2}(N,\Lambda_n(c-1))\). Its restriction to \(N\) is \(c_1(N_{N/\mathcal D})\cup b\), by (1.24a). This normal line bundle is trivial, since the fibre is the global divisor of \(t\). Consequently the two ordinary classes have the same restriction to \(N\).

Apply Lemma 1.10b to \(\widetilde W\). Its zero fibre is the normal cone with the multiplicities in \(\operatorname{sp}_i[W]\), so

\[
p^*i^*\operatorname{cl}_X(W)
=\operatorname{cl}_{N}(\operatorname{sp}_i[W])
=p^*\operatorname{cl}_Z(i^![W]).
\tag{1.24h}
\]

The last equality uses (1.24f) and smooth pullback compatibility. Constant étale cohomology is invariant under a vector-bundle projection: the affine-bundle argument in Theorem 1.4 identifies \(Rp_*\Lambda_n=\Lambda_n\). Thus \(p^*\) is injective, and (1.24h) proves compatibility with \(i^!\). It includes excess and nonproper intersections, since the normal cone, rather than its reduced support, entered the calculation. Factoring an arbitrary map by its graph and a smooth projection now proves compatibility with all smooth-scheme pullbacks. Proper compatibility is Lemma 1.10a.

For cycles \(V\subset X\), \(W\subset Y\), the exterior cup product of their supported classes is the class of \(V\times W\). On the product of their dense smooth loci this follows from normal parameters and composition of purity; the even degrees introduce no sign. The omitted subset of the product support has one greater codimension, so semi-purity extends the equality. Over the algebraically closed field the product of integral varieties is integral, and each generic multiplicity is one. Linearity gives the formula for all cycles. Apply the just-proved diagonal pullback compatibility:

\[
\begin{aligned}
\operatorname{cl}_X(\alpha\cdot\beta)
&=\Delta^*(\operatorname{cl}_X(\alpha)\boxtimes
                  \operatorname{cl}_X(\beta))\\
&=\operatorname{cl}_X(\alpha)\cup\operatorname{cl}_X(\beta).
\end{aligned}
\tag{1.24i}
\]

The codimension-zero class is the unit on each component. This proves the ring assertion.

The Chow projective-bundle relation, with our convention of lines, is the same relation (1.10), with Chow Chern classes and the Chow hyperplane class. Applying the ring map and pullback compatibility takes the latter to \(c_{1,n}(\mathcal O(1))\), by the divisor normalization. The uniqueness of the coefficients in the cohomological projective-bundle formula then identifies every Chow Chern class with the class in Theorem 1.4. This proves Chern compatibility without division by a factorial.

All support classes, projection maps, Kummer boundaries and counits commute with coefficient reduction. Use them for \(n=\ell^a\). The finite-coefficient finiteness premise recorded before Proposition 1.1 makes each cohomology group finite. Thus the inverse system in any fixed degree is Mittag–Leffler, and its first derived limit vanishes. The adic comparison gives
\(H^j(X,\mathbf Z_\ell(c))=\varprojlim_a H^j(X,\Lambda_{\ell^a}(c))\).
Passing the identities to this limit proves the integral assertions, including any torsion classes. Tensoring with \(\mathbf Q_\ell\) proves the rational assertions. \(\square\)

### The rational Chow ring and the Chern construction

Put \(E=\mathbf Q_\ell\). We now compare the direct map with the rational Chern-character construction. This gives a second proof of the rational ring comparison and explains its relation to \(K_0\). The auxiliary algebraic-geometric results concern Chow groups and coherent sheaves; they do not assume an étale cycle map. Their exact written homes are the AI Integrated Stacks [localized Chern-character isomorphism](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/chow.html#chow-proposition-K-tensor-Q), [its vector-bundle form](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/chow.html#chow-lemma-K-tensor-Q), [agreement with the diagonal intersection product](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/chow.html#chow-lemma-intersection-regular-smooth), and [the blowup formula](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/chow.html#chow-lemma-blow-up-formula), together with [the regular-scheme resolution property](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/perfect.html#perfect-lemma-regular-resolution-property) and [the equality of vector-bundle and perfect-complex \(K_0\)](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/perfect.html#perfect-lemma-K-is-old-K). We use the following precise content.

For a smooth separated finite-type \(X\), vector-bundle, perfect-complex and coherent-sheaf \(K_0\) agree, and

\[
\operatorname{ch}^{CH}:K_0(X)\otimes\mathbf Q
\xrightarrow{\sim}CH^*(X)\otimes\mathbf Q
\tag{1.25}
\]

is a ring isomorphism compatible with pullback. The coherent filtration is by dimension of support. Its associated-graded map takes \(\mathcal O_Z\) to \([Z]\). The proof uses the localized Chow Chern character: support localization puts a sheaf supported on \(Z\) in \(CH_*(Z)\), and the regular-sequence Koszul calculation at a generic point makes its leading term exactly \([Z]\). Thus the two associated-graded maps are inverse; the finite filtration proves (1.25). The Chow product it defines agrees with the usual diagonal intersection product. These are the algebraic assertions, including their localized-Chern construction, in the stated preceding proof homes. They are used at their full Noetherian regular, finite-dimensional, affine-diagonal scope. In particular, projectivity is unnecessary. Smooth separated \(X\) satisfies these hypotheses.

Let \(\operatorname{ch}^H\) be (1.15), and define

\[
\gamma_X=\operatorname{ch}^H\circ(\operatorname{ch}^{CH})^{-1}:
CH^*(X)\otimes\mathbf Q\longrightarrow
\bigoplus_jH^{2j}(X,E(j)).
\tag{1.26}
\]

It is a ring homomorphism and commutes with pullback. To verify that it preserves codimension, use the Adams operator
\(\psi^2[V]=[V\otimes V]-2[\bigwedge^2V]\).
The exterior-square filtration of an extension has graded parts \(\bigwedge^2V'\), \(V'\otimes V''\), and \(\bigwedge^2V''\). Together with the tensor-square identity in \(K_0\), it proves additivity of \(\psi^2\); it is therefore well defined in every characteristic. On a flag bundle \([V]=\sum_i[L_i]\), so \(\psi^2[V]=\sum_i[L_i^{\otimes2}]\). Consequently each degree-\(j\) component of either Chern character is multiplied by \(2^j\). The flag pullbacks are injective in Chow groups and cohomology by their projective-bundle formulas. If \(\alpha\in CH^c(X)\otimes\mathbf Q\), (1.25) therefore implies

\[
\psi^2(\operatorname{ch}^{CH})^{-1}(\alpha)
=2^c(\operatorname{ch}^{CH})^{-1}(\alpha).
\]

The eigenvalues \(2^j\) in the distinct cohomology degrees are distinct in \(E\), so \(\gamma_X(\alpha)\) has only degree \(2c\) and twist \(c\). Notice that this argument uses rational coefficients and does not divide by \(2\) in the base field. In particular it remains valid in characteristic two.

**Theorem 1.11 (comparison with the direct rational cycle map).** For every smooth separated finite-type \(X/k\), \(\gamma_X=\operatorname{cl}_X\otimes\mathbf Q\). Hence

\[
\operatorname{cl}_X(\alpha\cdot\beta)
=\operatorname{cl}_X(\alpha)\cup\operatorname{cl}_X(\beta),\qquad
f^*\operatorname{cl}_X(\alpha)=\operatorname{cl}_Y(f^*\alpha)
\tag{1.27}
\]

for arbitrary Chow classes and arbitrary morphisms \(f:Y\to X\) between such smooth schemes, with coefficients \(E\).

**Proof.** For line bundles, (1.26) sends the Chow first Chern class to the Kummer first Chern class. One can see this directly from the degree-one part of \(\operatorname{ch}^{CH}(L)\) and \(\operatorname{ch}^H(L)\), since \(\gamma\) is graded. Injective flag pullback and the Whitney formulas then show that \(\gamma\) preserves every Chern class, including Chern classes of virtual bundles.

For a projective bundle \(\pi:\mathbf P(V)\to X\) of relative dimension \(r-1\), its Chow groups are generated over \(CH^*(X)\) by \(1,\xi,\ldots,\xi^{r-1}\). The Chow pushforward sends the lower powers to zero and \(\xi^{r-1}\) to \(1\). The same is true in cohomology: degree forces the lower pushforwards to be zero, and the top power has fibre trace one. The projection formula proves that \(\gamma\) commutes with this pushforward on every class. It therefore commutes with pushforward for any succession of projective bundles.

For a smooth closed immersion of codimension zero, the centre is a union of connected components. Both classes are its degree-zero characteristic function, so the comparison is immediate. Suppose next that \(i:Z\hookrightarrow X\) has codimension \(r\geq1\), and that its normal bundle's \(K_0\)-class is the restriction of a virtual bundle \(\alpha\) on \(X\). Blow up \(Z\), writing \(b:X'\to X\), \(j:F\hookrightarrow X'\) and \(\pi:F\to Z\). The blowup is smooth; locally, the equations of the smooth centre are part of a coordinate system, and its usual affine blowup charts are smooth coordinate charts. The exceptional divisor is the lines projective bundle \(\mathbf P(N_{Z/X})\), with \(\mathcal O_{X'}(F)|_F=\mathcal O_F(-1)\). Set

\[
\theta=c_{r-1}^{CH}\bigl(b^*\alpha-[\mathcal O_{X'}(F)]\bigr).
\]

The algebraic blowup formula in the preceding proof home gives

\[
b^*[Z]=[F]\cdot\theta,
\qquad \pi_*j^*\theta=1.
\tag{1.28}
\]

The second identity's normalization can be checked explicitly. The exact normal-bundle sequence on \(F\) is
\(0\to\mathcal O_F(-1)\to\pi^*N_{Z/X}\to Q\to0\).
Thus \(j^*\theta=c_{r-1}(Q)\). If \(\xi=c_1(\mathcal O_F(1))\), its restriction to a fibre is \(\xi^{r-1}\), with coefficient \(1\), since \(c_t(Q)=c_t(\pi^*N)/(1-\xi t)\). Every other term has a lower power of \(\xi\); it pushes to zero. This proves the second identity of (1.28), in Chow groups and in cohomology after applying \(\gamma\). It also supplies the fibre computation left implicit in the formal cycle-map argument of *Weil Cohomology Theories*.

The proper cohomological pushforward has \(b_*1=1\). Indeed it is a degree-zero locally constant section on \(X\); over \(X-Z\) the map \(b\) is an isomorphism, so its counit is the identity. This dense-open calculation determines it on each connected component. Consequently \(b_*b^*=\operatorname{id}\), by the projection formula. Using the divisor comparison for the smooth exceptional divisor and then its Gysin projection formula gives

\[
\begin{aligned}
\gamma_X([Z])
&=b_*b^*\gamma_X([Z])\\
&=b_*\bigl(\gamma_{X'}([F])\cup\gamma_{X'}(\theta)\bigr)\\
&=b_*j_*j^*\gamma_{X'}(\theta)\\
&=i_*\pi_*\gamma_F(j^*\theta)=i_*1.
\end{aligned}
\tag{1.29}
\]

We next arrange the normal-bundle hypothesis for any smooth closed immersion. The resolution property of \(X\) supplies a vector bundle \(A\) on \(X\) surjecting onto \(i_*\mathcal C_{Z/X}\). Its restriction surjects onto the rank-\(r\) conormal bundle. Let \(G\to X\) be the relative Grassmannian of rank-\(r\) quotients of \(A\), with universal quotient \(Q_G\). That quotient on \(Z\) defines a closed immersion \(i':Z\to G\) over \(X\): it is a section of the separated Grassmann bundle over the closed subscheme \(Z\). Its conormal sequence is

\[
0\longrightarrow\mathcal C_{Z/X}\longrightarrow\mathcal C_{Z/G}
\longrightarrow(i')^*\Omega_{G/X}\longrightarrow0.
\]

In \(K_0(Z)\) its conormal class is the restriction of \([Q_G]+[\Omega_{G/X}]\); its dual normal class therefore extends as well. Formula (1.29) applies to \(i'\).

Finally \(\gamma\) commutes with pushforward for \(G\to X\). To prove this, take the flag bundle of the universal quotient and kernel on \(G\). Its map \(h:T\to G\) is a succession of projective bundles, and its composite \(T\to X\) is the full flag bundle of \(A\), also a succession of projective bundles. The Chow pushforward along \(h\) is surjective: at each projective-bundle stage multiply a pulled-back class by the top fibre power \(\xi^{s-1}\). Projective-bundle compatibility for both \(h\) and its composite proves compatibility for \(G\to X\). Push (1.29) for \(i'\) down to \(X\). It gives \(\gamma_X([Z])=i_*1\) for every smooth closed \(Z\), without a projective embedding of \(X\).

For an arbitrary integral \(Z\) of codimension \(c\), remove its nonsmooth locus \(B\). Its codimension in \(X\) is at least \(c+1\). On \(X-B\), the preceding smooth-immersion comparison identifies \(\gamma([Z])\) with the direct cycle class. Both constructions commute with this open restriction. Semi-purity makes restriction of degree \(2c\) cohomology injective, so they agree on \(X\). Integral linearity proves their agreement for every cycle, and Theorem 1.10 passes that agreement to Chow groups. The ring and pullback properties of (1.26) now prove (1.27). \(\square\)

**Corollary 1.12 (numerical equivalence).** If \(X\) is smooth and projective, the group \(N^c(X)\) of codimension-\(c\) cycles modulo numerical equivalence is a finitely generated free abelian group.

**Proof.** Let \(d=\dim X\). Choose cycles \(Y_1,\ldots,Y_s\) of codimension \(d-c\) whose classes form an \(E\)-basis of the \(E\)-span of all classes of that codimension. Such a finite basis exists by finite-dimensional cohomology. By (1.27) and the point trace normalization,
\((Z\cdot Y)=\int_X\operatorname{cl}(Z)\cup\operatorname{cl}(Y)\).
Thus a cycle \(Z\) is numerically zero exactly when all the integers \((Z\cdot Y_j)\) vanish: vanishing on that basis implies vanishing against every cycle class. The map

\[
N^c(X)\longrightarrow\mathbf Z^s,
\qquad[Z]\longmapsto((Z\cdot Y_1),\ldots,(Z\cdot Y_s))
\tag{1.30}
\]

is therefore injective. Every subgroup of \(\mathbf Z^s\) is free and finitely generated. Induct on \(s\): project to the last coordinate, whose image is either zero or a cyclic subgroup; choose one lift of its generator and apply induction to the kernel in \(\mathbf Z^{s-1}\). This proves the assertion, including the possible zero group. An injection only into a finite-dimensional \(E\)-vector space would not prove finite generation; the integer-valued intersection coordinates in (1.30) are essential. \(\square\)

## 2. Cup products compute intersection numbers

For line bundles on a smooth projective surface, write \((L\cdot M)\in\mathbf Z\) for their intersection number. We use its symmetry, additivity in each variable, and the restriction formula

\[
(L\cdot\mathcal O(D))=\deg(L|_D)
\tag{2.1}
\]

for a smooth effective divisor \(D\). Sections 2.1–2.4 below construct this pairing from coherent Euler characteristics and prove its symmetry, bilinearity and restriction formula. In particular they define self-intersections as well as intersections of distinct divisors. The conventional comparison locators are [Stacks, Tag 0BEP](https://stacks.math.columbia.edu/tag/0BEP), [0BER](https://stacks.math.columbia.edu/tag/0BER), [0BEU](https://stacks.math.columbia.edu/tag/0BEU) and [0BEY](https://stacks.math.columbia.edu/tag/0BEY).

**Proposition 2.1.** For any line bundles \(L,M\) on a smooth projective surface \(S/k\),

\[
\int_S c_{1,n}(L)\cup c_{1,n}(M)
=(L\cdot M)\pmod n.
\tag{2.2}
\]

**Proof.** First suppose \(M=\mathcal O(D)\), with \(D\) smooth. The factors have even degree, so they commute without a sign. Proposition 1.1 and naturality of \(c_1\) give

\[
\begin{aligned}
\int_S c_{1,n}(L)\cup c_{1,n}(\mathcal O(D))
&=\int_D c_{1,n}(L|_D)\\
&=\deg(L|_D)\pmod n\\
&=(L\cdot\mathcal O(D))\pmod n.
\end{aligned}
\tag{2.3}
\]

The second equality is Lemma 1.2. It remains to express an arbitrary \(M\) as a difference of such divisors, without requiring \(M\) itself to have sections.

Choose an ample line bundle \(H\). For sufficiently large \(a\), both \(H^{\otimes a}\) and \(M\otimes H^{\otimes a}\) are very ample by the ample-twisting proof in §2.3 (compare [Stacks, Tag 0FVC](https://stacks.math.columbia.edu/tag/0FVC)). Its hypotheses hold for \(S\to\operatorname{Spec}k\), a finite-type morphism with quasi-compact base. Each of these very ample bundles admits a smooth divisor. Here is the smoothness argument in this setting.

Embed \(S\) in \(\mathbf P^N\) by the chosen very ample bundle. A hyperplane section is singular at \(x\in S\) precisely when its hyperplane contains the projective tangent plane \(T_xS\). For \(N\geq3\), the hyperplanes containing this plane form \(\mathbf P^{N-3}\). The incidence variety of pairs \((x,B)\) of this kind has dimension \(2+N-3=N-1\), whereas the space of all hyperplanes has dimension \(N\). Its projection is closed because \(S\) is projective, and its image has dimension at most \(N-1\). Thus the complement is a nonempty open set. Also avoid hyperplanes containing any component of \(S\). Since an algebraically closed field is infinite, this open set has a \(k\)-point. Its section is a smooth Cartier divisor. If \(N=2\), no hyperplane contains a two-dimensional projective tangent plane, so every hyperplane section is smooth; the same conclusion follows. Connectedness or irreducibility of the resulting divisor is unnecessary.

We obtain smooth divisors \(D_1,D_0\) with

\[
\mathcal O(D_1)\simeq M\otimes H^{\otimes a},
\qquad \mathcal O(D_0)\simeq H^{\otimes a},
\qquad M\simeq\mathcal O(D_1-D_0).
\]

Subtract (2.3) for \(D_0\) from that for \(D_1\). Additivity of \(c_1\), bilinearity of cup product, and additivity of intersection numbers yield (2.2). Apply this on each component if \(S\) is disconnected. The proof works for every invertible \(n\), without assuming \(n\) prime. \(\square\)

Fix a prime \(\ell\ne\operatorname{char}k\) and put \(E=\mathbf Q_\ell\). Passing through \(n=\ell^a\) gives classes in \(H^2(S,\mathbf Z_\ell(1))\). Equality (2.2) for every \(a\), with compatible traces, gives the exact \(\mathbf Z_\ell\)-identity, since \(\bigcap_a\ell^a\mathbf Z_\ell=0\). Tensoring with \(E\) therefore gives

\[
\int_S c_1(L)\cup c_1(M)=(L\cdot M)\quad\text{in }E.
\tag{2.4}
\]

Thus the rational statement has been deduced from the finite-coefficient statement, including its normalization.

### 2.1. The surface Hodge theorem and its hypotheses

Let \(X\) be a smooth, projective, geometrically integral surface over a field \(k\). A divisor in this proof is a Cartier divisor, equivalently its invertible sheaf; addition denotes tensor product. Write

\[
\chi(L)=\sum_i(-1)^i\dim_kH^i(X,L),\qquad
L\cdot M=\chi(L+M)-\chi(L)-\chi(M)+\chi(0).
\tag{HI.1}
\]

Section 2.4 proves that (HI.1) is a symmetric integral bilinear pairing, with \(L\cdot C=\deg(L|_C)\) for a smooth divisor \(C\). It is the intersection pairing used in (2.1): the surface Riemann–Roch identity proved below makes it the coefficient of \(mn\) in \(\chi(mL+nM)\), and the alternating formula with inverse twists gives the same coefficient.

**Theorem HI.** If \(H\cdot H>0\) and \(D\cdot H=0\), then \(D\cdot D\leq0\). Equality holds exactly when \(D\) is numerically trivial, meaning \(D\cdot E=0\) for every invertible sheaf \(E\) on \(X\). The hypothesis on \(H\) is positive square; \(H\) need not be ample.

We first prove the result with \(H\) ample, then obtain the stated form by elementary linear algebra. The positive-square form will apply to the two fibre classes on \(C\times C\) in Section 5.

The coherent inputs have exact written proof homes. [Dualizing sheaves and Serre duality for projective schemes, §§3–4](course:AG-QC/dualizing-sheaves-and-serre-duality-for-projective-schemes) proves closed-immersion injective adjunction and the transfer of duality. Its preceding [Ext sheaves and Serre duality on projective space, Theorems 4.1 and 5.1](course:AG-QC/ext-sheaves-and-serre-duality-on-projective-space) proves ambient duality by Laurent coefficients, two-stage presentations and dimension shifting. We supply the smooth canonical-bundle identification and local Ext concentration below by a regular immersion and its Koszul complex; the general Auslander–Buchsbaum reduction is not needed. [Serre's theorems on projective schemes, Theorems 2.1–2.2](course:AG-QC/serres-theorems-on-projective-schemes) proves coherent finiteness, generation and vanishing.

The injective and derived-Hom prerequisites are the actual written [Injective modules, flasque sheaves and bounded-below derived functors, Lemmas 2.1–2.2, Theorem 2.3 and Theorem 4.1](course:derived-categories-and-sheaf-operations/injective-modules-and-bounded-below-derived-functors), with [Sheaves of modules on a ringed space, §§1–3 and Lemmas 5.1–5.2](course:derived-categories-and-sheaf-operations/sheaves-of-modules-on-a-ringed-space). These prove Baer's criterion, enough injectives, restriction of injectives and the bounded-below resolution comparison. [Affine cohomology and Serre's criterion, Theorem 3.1](course:AG-QC/affine-cohomology-and-serres-criterion), using [Čech cohomology, Theorems 3.2 and 4.1](course:AG-QC/cech-cohomology), proves the finite affine-cover computation used next. No étale higher-dimensional trace enters this coherent proof.

The algebraic proof homes used in §§2.2–2.3 are [Regular sequences, depth and Cohen–Macaulay modules, Theorem 6.1](course:AG-CA/AG-CA-12), [Regular local rings, Proposition 1.4](course:AG-CA/AG-CA-14), [Kähler differentials, Theorem 3.3 and Proposition 5.2](course:AG-CA/AG-CA-16), and [Smooth algebras over a field and the Jacobian criterion](course:AG-CA/AG-CA-18). The line-bundle and embedding foundations are [Ample invertible sheaves](course:AG-MO/AG-MO-09), [Very ample sheaves and embeddings](course:AG-MO/AG-MO-08), and [Effective Cartier divisors and invertible sheaves](course:AG-MO/AG-MO-15). The calculations below specify the exact applications of these written arguments.

We may work over an algebraic closure. For a field extension \(K/k\), a finite affine cover with affine intersections computes coherent cohomology; its complex after base change is its tensor product with \(K\). Flatness gives

\[
H^i(X_K,L_K)=H^i(X,L)\otimes_kK,
\qquad \chi(X_K,L_K)=\chi(X,L).
\tag{HI.2}
\]

Consequently all the intersections of bundles originally on \(X\) are preserved. Smoothness, projectivity and geometric integrality are preserved as well. Proving the inequality over \(\bar k\) proves it over \(k\); the equality argument will quantify over the original bundles \(E\). Hence until §2.7 the field is algebraically closed, and therefore infinite, in arbitrary characteristic.

### 2.2. Smooth canonical bundles and coherent duality

Put \(K_X=\det\Omega_{X/k}\). For a smooth projective variety \(Y\) of dimension \(d=1\) or \(2\), embed \(i:Y\hookrightarrow P=\mathbf P^N_k\), and set \(c=N-d\). Smoothness makes the local rings regular. At a closed point, the ambient and quotient local rings are regular of dimensions \(N\) and \(d\). The regular-quotient statement, AG-CA *Regular local rings*, Proposition 1.4, says that the ideal is locally generated by \(c\) elements of a regular system of parameters. They form a regular sequence. After shrinking, they generate the coherent ideal sheaf; hence this embedding is a regular immersion of codimension \(c\).

For clarity, that regular-quotient argument does not merely count equations. The kernel of the map of maximal-ideal cotangent spaces has dimension \(c\). Choose \(c\) ideal elements lifting its basis and complete to parameters in the regular ambient ring. Their quotient is a regular local domain of dimension \(d\), mapping onto the local ring of \(Y\) of dimension \(d\). A nonzero kernel element would be a nonzerodivisor and lower dimension by one, a contradiction. Thus the chosen equations generate the ideal. AG-CA's proof of the domain, parameter and regular-sequence assertions is *Regular sequences, depth and Cohen–Macaulay modules*, Theorem 6.1; these are written proofs, not assumptions about a planned lesson.

The local Koszul resolution on these equations, dualized into the ambient canonical line, gives

\[
\mathcal E xt^j_P(i_*\mathcal O_Y,\omega_P)=0\quad(j\ne c),
\qquad
\mathcal E xt^c_P(i_*\mathcal O_Y,\omega_P)
=\det(I/I^2)^\vee\otimes\omega_P|_Y.
\tag{HI.3}
\]

Here exactness of the Koszul complex is the regular-sequence induction: adjoining a nonzerodivisor forms a mapping cone, whose cohomology is only the new quotient in degree zero. Dualizing that complex puts its quotient in the top degree. The conormal module has the equation classes as a basis (AG-CA *Kähler differentials*, Proposition 5.2). A change of equation basis acts on the last Koszul term by its determinant and on its dual by the inverse determinant; thus the displayed local descriptions glue to the indicated determinant line.

The conormal sequence is short exact in this smooth case:

\[
0\longrightarrow I/I^2\longrightarrow\Omega_{P/k}|_Y
\longrightarrow\Omega_{Y/k}\longrightarrow0.
\tag{HI.4}
\]

Indeed its right exactness is AG-CA *Kähler differentials*, Theorem 3.3. At each closed point its first arrow is the inclusion of the \(c\) independent equation differentials; smoothness gives their rank \(c\) by the Jacobian criterion. An invertible \(c\times c\) minor locally splits this injection. Checking at all closed points suffices for these coherent modules on a finite-type scheme. The ranks of its locally free terms are \(c,N,d\). Taking determinants in (HI.4), and using \(\omega_P=\det\Omega_{P/k}\) (AG-QC's projective-space duality lesson, Exercise 7.4), identifies the nonzero sheaf in (HI.3) with \(\det\Omega_{Y/k}=K_Y\).

Now use precisely the closed-immersion argument written in AG-QC's dualizing lesson, Section 3: the right adjoint \(i^b\) to the exact closed pushforward takes injectives to injectives; the cohomology of \(i^bI^\bullet\) is the ambient sheaf Ext just calculated. Concentration in degree \(c\) gives

\[
\operatorname{Ext}^a_Y(F,K_Y)
\cong\operatorname{Ext}^{c+a}_P(i_*F,\omega_P)
\cong H^{d-a}(Y,F)^\vee
\quad(a\geq0).
\tag{HI.5}
\]

The last arrow is the preceding written projective-space Serre duality, Theorem 5.1. For a line bundle \(L\), its Ext is cohomology of \(L^{-1}\otimes K_Y\), since tensoring by a line bundle is exact (the same preceding lesson, Proposition 1.2). Thus

\[
h^i(Y,L)=h^{d-i}(Y,K_Y-L),\quad 0\leq i\leq d.
\tag{HI.6}
\]

There is no cohomology above \(d\): the concentration calculation makes ambient Ext in degrees \(<c\) zero, and ambient duality gives the corresponding vanishing in degrees \(>d\) up to \(N\); the finite projective affine cover kills degrees \(>N\). In particular, on a surface

\[
h^2(X,L)=h^0(X,K_X-L),\qquad
h^1(X,L)=h^1(X,K_X-L).
\tag{HI.7}
\]

We use the second equality only to obtain one smooth integral restriction curve. No general Grothendieck duality, higher-dimensional trace or étale Poincaré duality is used.

### 2.3. Curve Riemann–Roch, ample twisting and smooth divisors

**Curve Euler formula.** Let \(T\) be a smooth projective integral curve over the algebraically closed field. Finiteness of coherent cohomology gives \(H^0(T,\mathcal O_T)=k\): that ring is a finite-dimensional domain, hence a finite extension field of \(k\), hence \(k\). Define \(g=h^1(T,\mathcal O_T)\).

Every line bundle \(M\) has a nonzero rational frame. At a closed point the regular local ring has dimension one and its maximal ideal is generated by a parameter \(t\); the initial-form and Krull-separation argument gives a finite order for every nonzero element, so it is \(t^a\) times a unit. It is a DVR. The orders of the rational frame therefore give a finite signed divisor \(A=\sum a_pp\) with \(M\cong\mathcal O_T(A)\). Finiteness follows on a finite trivializing cover by writing its coefficient as a fraction of regular functions: the zeros of a nonzero regular function on a curve form a finite closed subset. The fractional sheaf glues because changes of frame are units.

At a rational closed point \(p\), the parameter calculation gives the exact sequence

\[
0\longrightarrow\mathcal O_T(A-p)\longrightarrow\mathcal O_T(A)
\longrightarrow k(p)\longrightarrow0.
\]

The last sheaf has Euler characteristic one. Adding or subtracting the finitely many points in \(A\), and using the long exact cohomology sequence, proves

\[
\chi(T,M)=\deg M+1-g,
\qquad \deg M=\sum_pa_p.
\tag{HI.8}
\]

In particular the degree is independent of the rational frame: applying the same formula to the trivial line bundle makes every principal divisor have degree zero. The tensor-product rule for frame orders makes degree additive. Formula (HI.6) for \(T\) gives the full curve Riemann–Roch form

\[
h^0(T,M)-h^0(T,K_T-M)=\deg M+1-g,
\quad \deg K_T=2g-2,
\tag{HI.9}
\]

since \(h^0(K_T)=g\), \(h^1(K_T)=1\), and (HI.8) applied to \(K_T\) gives its degree. For a smooth curve with finitely many components, these formulas add componentwise; in particular \(\deg K_T=-2\chi(T,\mathcal O_T)\). This proves the curve Riemann–Roch prerequisite used in the restriction and normal-bundle calculations.

A line bundle of degree \(b<0\) on an integral smooth curve has no nonzero section, because the zero divisor of such a section would be effective of degree \(b\). If \(b\geq0\), successive restrictions at a single rational point give

\[
h^0(T,M)\leq b+1:
\tag{HI.10}
\]

after \(b+1\) subtractions the residual line bundle has degree \(-1\), and each point quotient increases the possible dimension by at most one. Thus \(h^0(T,M)\leq\max(0,\deg M+1)\) for every \(M\).

**Ample twisting.** Fix a very ample line bundle \(B\) on \(X\). Given any line bundle \(L\), Serre generation makes \(L+(m-1)B\) globally generated for all sufficiently large \(m\). The tensor product of a very ample line bundle and a globally generated line bundle is very ample: the first defines a closed embedding, the second a map to a finite projective space, their product is a closed embedding by its graph over the first, and Segre is a closed embedding with tensor-product tautological line. The written provider is AG-MO *Very ample sheaves and embeddings*, Theorems 3.1 and 5.3. Consequently \(L+mB\), as well as \(mB\), is very ample for large \(m\).

**Smooth Bertini in the required form.** If a line bundle \(V\) is very ample, embed \(X\hookrightarrow\mathbf P^N\) using it. The hyperplanes whose section is singular at a given closed point \(x\) are exactly the hyperplanes containing the projective tangent plane \(\mathbf T_xX\). They form a projective space of dimension \(N-3\) when \(N\geq3\). The incidence of these pairs over \(X\) is closed and has dimension \(2+(N-3)=N-1\); its projection to the dual projective space is closed by projectivity, and cannot fill that dimension-\(N\) space. Outside it the hyperplane section is smooth by the Jacobian criterion, in every characteristic. For \(N=2\), \(X=\mathbf P^2\) and a hyperplane section is a smooth line. A hyperplane not containing \(X\) cuts an effective Cartier divisor of pure dimension one. It is nonempty: otherwise the embedded projective surface would lie in an affine coordinate chart and all its coordinate ratios would be global regular functions, hence constants, contradicting its dimension. Thus a smooth divisor exists in every very ample system. The argument does not invoke generic smoothness or assume characteristic zero.

Taking smooth divisors \(C_+\in|L+mB|\) and \(C_-\in|mB|\) shows that every line bundle has a presentation

\[
L=C_+-C_-,
\quad C_+,C_-\text{ smooth very ample divisors}.
\tag{HI.11}
\]

Connectedness of these two divisors is unnecessary. We will need one integral smooth divisor proportional to a chosen ample \(H\). An ample \(H\) has all sufficiently large powers very ample (AG-MO *Ample invertible sheaves*, Theorem 4.2). Choose \(r\) large enough that \(rH\) is very ample and \(H^1(X,K_X+rH)=0\), by Serre vanishing. For a smooth \(C\in|rH|\), duality (HI.7) gives \(H^1(X,\mathcal O_X(-C))=0\). Also \(H^0(X,\mathcal O_X(-C))=0\): multiplication by its defining section would turn a nonzero such section into a nonzero global regular function vanishing on the nonempty \(C\), impossible since the global functions are \(k\). The exact sequence

\[
0\longrightarrow\mathcal O_X(-C)\longrightarrow\mathcal O_X
\longrightarrow\mathcal O_C\longrightarrow0
\]

therefore gives \(H^0(C,\mathcal O_C)=k\). A smooth curve is regular, so distinct irreducible components cannot meet (a regular local ring is a domain); its components are disjoint. Each projective component has constants \(k\). The displayed equality implies that there is exactly one component. Thus \(C\) is integral. This proves the particular irreducible Bertini consequence needed for the boundedness argument.

### 2.4. Intersection and surface Riemann–Roch by restriction

Let \(C\) be a smooth effective divisor and \(L\) any line bundle. Its local equation is a nonzerodivisor, so tensoring its ideal sequence gives

\[
0\longrightarrow L-C\longrightarrow L\longrightarrow L|_C
\longrightarrow0,
\qquad
\chi(L)-\chi(L-C)=\chi(C,L|_C).
\tag{HI.12}
\]

By (HI.8), including the componentwise version,

\[
\chi(L+C)-\chi(L)
=\deg(L|_C)+\deg(\mathcal O_C(C))+\chi(\mathcal O_C).
\tag{HI.13}
\]

Subtract the same equation with \(L=0\). Definition (HI.1) gives \(L\cdot C=\deg(L|_C)\), so the intersection with a smooth divisor is additive in \(L\). More generally, the difference \(\chi(L-C)-\chi(L)\) is also a constant plus an additive function of \(L\), by (HI.12). Any \(M\) is a difference of two smooth divisors by (HI.11). Composing their two differences shows that \(\chi(L+M)-\chi(L)\) is a constant plus an additive function of \(L\). Subtracting its value at \(L=0\) proves that \(L\cdot M\) is additive in \(L\) for every \(M\). It is symmetric from (HI.1), hence additive in both variables; its values are integers. This establishes the required pairing without a multivariable Hilbert-polynomial theorem.

For a nonempty effective divisor \(Z\) and ample \(H\),

\[
Z\cdot H>0,\qquad H^2>0.
\tag{HI.14}
\]

To see the first assertion, choose a smooth hyperplane section \(C\in|rH|\) that contains no component of \(Z\), using the nonempty open supplied by Bertini and avoiding the finitely many closed conditions of containing those components. Every projective curve component of \(Z\) meets this hyperplane: if it did not, all affine coordinate ratios would be regular on that projective integral curve, hence constant, contradicting the embedding. The restricted section of \(\mathcal O_X(Z)|_C\) has a nonempty finite zero scheme. At each point its order is the positive local length in the DVR of the smooth \(C\). Thus \(Z\cdot C=\deg\mathcal O_C(Z)>0\), and \(Z\cdot H=(Z\cdot C)/r>0\). The same argument applied to the nonempty \(Z=C\sim rH\) gives \(rH^2>0\). In particular a line bundle of negative intersection with \(H\) has no nonzero global section.

Elementary adjunction supplies the coefficient of the surface formula. For a smooth divisor \(C\subset X\), the short exact conormal sequence

\[
0\longrightarrow\mathcal O_C(-C)\longrightarrow\Omega_{X/k}|_C
\longrightarrow\Omega_{C/k}\longrightarrow0
\]

has the same local Jacobian proof as (HI.4). Its determinant yields

\[
K_C=(K_X+C)|_C,
\qquad
\chi(\mathcal O_C)=-\tfrac12(K_X\cdot C+C^2),
\tag{HI.15}
\]

where the second equality is (HI.9) on each component. Therefore (HI.12) reads

\[
\chi(L)-\chi(L-C)
=L\cdot C-\tfrac12(K_X\cdot C+C^2).
\tag{HI.16}
\]

The quadratic function \(Q(L)=\frac12 L\cdot(L-K_X)\) has exactly this same difference: expanding \(Q(L)-Q(L-C)\) gives the right side of (HI.16). Hence \(\chi(L)-Q(L)\) is invariant under adding or subtracting any smooth very ample divisor. Write \(L=C_+-C_-\) as in (HI.11) and apply this invariance twice to reach zero. We obtain the surface Riemann–Roch identity, with no unproved surface RR input:

\[
\boxed{\chi(X,L)=\chi(X,\mathcal O_X)
+\tfrac12L\cdot(L-K_X).}
\tag{HI.17}
\]

This also verifies the polynomial and the intersection convention claimed after (HI.1).

### 2.5. The ample orthogonal inequality

Suppose \(H\) is ample, \(D\cdot H=0\), and, towards a contradiction, \(D^2>0\). For every integer \(n\geq1\),

\[
h^0(X,nD)=0.
\tag{HI.18}
\]

A nonzero section either vanishes along a nonempty effective divisor \(Z\sim nD\), contradicting \(Z\cdot H=0\) and (HI.14), or is nowhere zero and trivializes \(nD\), contradicting \((nD)^2=n^2D^2>0\).

Choose once and for all the smooth integral \(C\in|rH|\) constructed in §2.3. Let \(K=K_X\), and choose an integer \(t\geq1\) such that

\[
K\cdot H-trH^2<0.
\tag{HI.19}
\]

For every \(n\geq1\), (HI.14) then gives \(h^0(X,K-nD-tC)=0\). Apply (HI.12) to \(K-nD-jC\), for \(j=0,\ldots,t-1\). The initial terms of each cohomology sequence give the inequality

\[
h^0(X,K-nD-jC)\leq h^0(X,K-nD-(j+1)C)
+h^0(C,(K-nD-jC)|_C).
\]

The degree of the curve bundle in the last term is

\[
K\cdot C-nD\cdot C-jC^2=K\cdot C-jC^2,
\tag{HI.20}
\]

because \(D\cdot C=rD\cdot H=0\). It is independent of \(n\). The integral-curve estimate (HI.10) now gives the finite uniform bound

\[
h^0(X,K-nD)\leq
B:=\sum_{j=0}^{t-1}\max\{0,K\cdot C-jC^2+1\}.
\tag{HI.21}
\]

Both \(t\) and \(B\) were fixed before varying \(n\). Smoothness alone of \(C\) would not suffice here: if it had several components, zero total \(D\cdot C\) would not control its degrees on those components. Its integrality was proved explicitly.

Surface duality (HI.7), (HI.18) and the nonnegativity of \(h^1\) imply

\[
\chi(X,nD)=h^0(X,nD)-h^1(X,nD)+h^2(X,nD)
\leq B.
\tag{HI.22}
\]

But (HI.17) gives

\[
\chi(X,nD)=\chi(\mathcal O_X)+\tfrac12n^2D^2-\tfrac12nD\cdot K,
\tag{HI.23}
\]

which tends to \(+\infty\) since \(D^2>0\). This contradiction proves \(D^2\leq0\) on the orthogonal complement of every ample \(H\).

### 2.6. Positive-square \(H\) and the equality clause

Fix an ample bundle \(A\), so \(A^2>0\), and use the inequality just proved on \(A^\perp\). Let now \(H^2>0\), \(D\cdot H=0\). If \(D^2>0\), the span of \(H,D\) has positive definite intersection matrix \(\operatorname{diag}(H^2,D^2)\). At least one of \(A\cdot H,A\cdot D\) is nonzero; if both were zero, \(H\in A^\perp\) would already contradict \(H^2>0\). The nonzero integral bundle

\[
V=(A\cdot D)H-(A\cdot H)D
\]

satisfies \(V\cdot A=0\), while

\[
V^2=(A\cdot D)^2H^2+(A\cdot H)^2D^2>0.
\]

This contradicts the ample orthogonal inequality. Therefore \(D^2\leq0\) for every positive-square \(H\).

Suppose \(D^2=0\), and let \(E\) be any invertible sheaf. Set

\[
E'=H^2E-(E\cdot H)H.
\tag{HI.24}
\]

The integer coefficients make \(E'\) an actual invertible sheaf, and \(E'\cdot H=0\). For every integer \(n\), including both signs, \(nD+E'\in H^\perp\), so the established nonpositivity gives

\[
0\geq(nD+E')^2=2n(D\cdot E')+(E')^2.
\tag{HI.25}
\]

A nonzero coefficient of \(n\) would make the right side positive for one sufficiently large signed integer. Hence \(D\cdot E'=0\). Since \(D\cdot H=0\), (HI.24) gives \(0=H^2(D\cdot E)\), and \(H^2>0\) gives \(D\cdot E=0\). This holds for every \(E\), proving numerical triviality. Conversely numerical triviality includes \(E=D\), hence \(D^2=0\). This proves Theorem HI.

### 2.7. Field scope and the curve product

For a smooth projective geometrically integral surface over any field, (HI.2) transfers the inequality and equality assertion from its algebraic closure. In the equality argument test every line bundle originally on the surface; its intersections are preserved by that extension. The surface consumed in Section 5 is the product of a smooth projective geometrically integral curve with itself, so it satisfies exactly these hypotheses. The argument makes no assertion for singular or nonprojective surfaces, and does not require a descent claim for a surface that ceases to be integral over the algebraic closure.

The classical Hodge statement is [Vakil, *The Rising Sea*, Theorem 20.2.13](https://math.stanford.edu/~vakil/216blog/FOAGjul2724public.pdf). Curve Riemann–Roch may be compared with [Stacks, Tag 0BS6](https://stacks.math.columbia.edu/tag/0BS6). The proof above establishes its needed mechanisms: the Koszul canonical line, coherent duality, curve Euler formula, smooth integral restriction curve, surface quadratic Euler formula, uniform second-cohomology bound and numerical-triviality equality clause.

## 3. The diagonal as a signed dual-basis tensor

We use the curve cohomology and Künneth prerequisites in their precise forms:

\[
\dim_E H^i(C,E)=
\begin{cases}1&i=0,2,\\2g&i=1,\\0&\text{otherwise},\end{cases}
\qquad
H^*(C\times C,E)\simeq H^*(C,E)\otimes_EH^*(C,E).
\tag{3.1}
\]

Künneth sends \(a\otimes b\) to \(p_1^*a\cup p_2^*b\), and multiplication obeys

\[
(a\otimes b)\cup(c\otimes d)
=(-1)^{\deg b\,\deg c}(a\cup c)\otimes(b\cup d).
\tag{3.2}
\]

The exact finite-coefficient rank calculation is [The multiplicative group on a curve, Theorem 6.2](course:ag-etale-cohomology/the-multiplicative-group-on-a-curve), with its explicitly inherited Picard and Brauer inputs in §6.1. It gives free ranks \(1,2g,1\) at every prime-power level; [ℓ-adic sheaves and their cohomology, §§5–7](course:AG-LTF/l-adic-sheaves-and-their-cohomology) carries them to integral and rational cohomology. [Cohomological dimension and the Künneth formula, Theorem 12.3](course:ag-etale-cohomology/cohomological-dimension-and-the-kunneth-formula) proves the derived external-product theorem even for arbitrary unbounded finite-coefficient complexes. In our curve case the free groups make its derived tensor have no Tor terms. Proposition 1.1 supplies duality. The product trace is the tensor product of the two traces by [Smooth traces, duality and Gysin maps, Lemma 13.2](course:AG-LTF/smooth-trace-and-duality): factor the product's structure map through one projection, use base change for the trace on its fibre, then use compatibility of the counits with composition. This gives the normalization directly from the maps. Compare [Stacks, Tags 03RQ](https://stacks.math.columbia.edu/tag/03RQ), [0F1P](https://stacks.math.columbia.edu/tag/0F1P) and [0FGX](https://stacks.math.columbia.edu/tag/0FGX).

For the following calculation choose a compatible generator of \(\mathbf Z_\ell(1)\) over \(k\), to write all twists as \(E\). Traces still mean the normalized maps with their original twists. Changing the generator rescales a class and its dual inversely, so the resulting identities are independent of this choice. This is a calculation over the algebraically closed field; no claim of Galois equivariance is made for the trivialization.

Choose \(e_{i,j}\), \(1\leq j\leq b_i\), a basis of \(H^i(C,E)\). Define its **right dual** \(e_{i,j}^{\vee}\in H^{2-i}(C,E(1))\) by

\[
\int_C e_{i,j}\cup e_{i,j'}^\vee=\delta_{jj'}.
\tag{3.3}
\]

Let \(\delta:C\hookrightarrow C\times C\) be the diagonal, and write \([\Delta]=c_1(\mathcal O(\Delta))\).

**Lemma 3.1 (diagonal convention).**

\[
[\Delta]=\sum_{i=0}^2\sum_{j=1}^{b_i}
(-1)^i e_{i,j}\otimes e_{i,j}^{\vee}.
\tag{3.4}
\]

**Proof.** Since \(\Delta\) is smooth, the divisor trace compatibility gives

\[
\int_{C\times C}[\Delta]\cup(a\otimes b)=\int_C a\cup b
\tag{3.5}
\]

when the degrees of \(a,b\) sum to two. Expand its Künneth component of bidegree \((i,2-i)\) as \(\sum_je_{i,j}\otimes d_{i,j}\). Take \(a\) of degree \(2-i\) and \(b\) of degree \(i\). Formula (3.2) gives

\[
\int_{C\times C}[\Delta]\cup(a\otimes b)
=\sum_j\left(\int_C a\cup e_{i,j}\right)
\left(\int_C d_{i,j}\cup b\right).
\tag{3.6}
\]

To check the sign, the tensor multiplication contributes \((-1)^{(2-i)^2}=(-1)^i\), and reversing \(e_{i,j}\cup a\) contributes another \((-1)^{i(2-i)}=(-1)^i\). Their product is \(1\).

Now take \(a=(-1)^i e_{i,j_0}^\vee\). Graded commutativity and (3.3) give \(\int_C a\cup e_{i,j}=\delta_{j_0j}\). Equations (3.5)–(3.6) imply \(\int_C d_{i,j_0}\cup b=\int_C(-1)^i e_{i,j_0}^\vee\cup b\) for every \(b\). Poincaré duality forces \(d_{i,j_0}=(-1)^i e_{i,j_0}^\vee\). This proves every Künneth component of (3.4). \(\square\)

This is the explicit sign convention behind [Stacks, Tag 0FGZ](https://stacks.math.columbia.edu/tag/0FGZ). A formula without the written sign can use *left* duals; with the right duals (3.3) the sign is essential.

For clarity, let \(\eta\in H^2(C,E(1))\) have trace \(1\), and choose a symplectic basis \(a_1,b_1,\ldots,a_g,b_g\) of \(H^1\), with \(\int_C a_r\cup b_s=\delta_{rs}\). The right duals of \(a_r,b_r\) are \(b_r,-a_r\), respectively. Formula (3.4) becomes

\[
[\Delta]=\eta\otimes1+1\otimes\eta
+\sum_{r=1}^g(b_r\otimes a_r-a_r\otimes b_r).
\tag{3.7}
\]

In genus zero only the first two terms occur. Pulling (3.4) back to the diagonal and integrating gives

\[
(\Delta\cdot\Delta)=\int_C\delta^*[\Delta]
=\sum_i(-1)^i b_i=2-2g.
\tag{3.8}
\]

Here the first equality follows from (2.1) and (1.7) rationally. It also agrees with the normal bundle: the quotient of \(T_C\oplus T_C\) by its diagonal is \(T_C\), of degree \(2-2g\). Compare [Stacks, Tag 0FH0](https://stacks.math.columbia.edu/tag/0FH0).

## 4. The graph–diagonal calculation

Let \(\varphi:C\to C\) be any \(k\)-morphism. Its graph is the smooth Cartier divisor with inclusion

\[
\gamma_\varphi=(\operatorname{id},\varphi):C\longrightarrow C\times C.
\]

In particular the order of the graph coordinates is fixed throughout. Write \(T_i=\varphi^*:H^i(C,E)\to H^i(C,E)\), using the constant coefficient identification.

**Theorem 4.1 (Weil's fixed-point formula).** One has

\[
(\Gamma_\varphi\cdot\Delta)=
\sum_{i=0}^2(-1)^i\operatorname{Tr}(T_i).
\tag{4.1}
\]

If \(\varphi\ne\operatorname{id}\), its fixed-point scheme is finite, and this number is its length:

\[
(\Gamma_\varphi\cdot\Delta)
=\sum_{\varphi(x)=x}
\operatorname{length}_k\mathcal O_{\operatorname{Fix}(\varphi),x}.
\tag{4.2}
\]

**Proof.** By Proposition 2.1 in rational coefficients and the divisor trace identity for the graph,

\[
\begin{aligned}
(\Gamma_\varphi\cdot\Delta)
&=\int_{C\times C}[\Gamma_\varphi]\cup[\Delta]\\
&=\int_C\gamma_\varphi^*[\Delta]\\
&=\sum_{i,j}(-1)^i\int_C e_{i,j}\cup\varphi^*e_{i,j}^{\vee}.
\end{aligned}
\tag{4.3}
\]

The pullback in the last line follows from (3.4): the first projection restricted to the graph is the identity and the second is \(\varphi\).

Expand \(T_{2-i}\) in the basis \(e_{i,j}^{\vee}\) of \(H^{2-i}(C,E(1))\), with twists trivialized as in §3. Say

\[
\varphi^*e_{i,j}^{\vee}=\sum_k A_{kj}e_{i,k}^{\vee}.
\]

Equation (3.3) gives \(\int_Ce_{i,j}\cup\varphi^*e_{i,j}^{\vee}=A_{jj}\). Summing over \(j\) therefore gives \(\operatorname{Tr}(T_{2-i})\). Replacing \(2-i\) by \(r\) does not change parity. This turns (4.3) into \(\sum_r(-1)^r\operatorname{Tr}(T_r)\), proving (4.1).

The fixed-point scheme is \(\gamma_\varphi^{-1}(\Delta)\), so it is closed in \(C\). If it contained the generic point, \(\varphi\) and the identity would agree generically. Their equalizer is closed because \(C\) is separated, and the integral scheme \(C\) is reduced, so this agreement would force equality everywhere. Thus for \(\varphi\ne\operatorname{id}\) the graph and diagonal have no common component and their intersection is zero-dimensional and proper, hence finite.

At a fixed point \(x\), choose a uniformizer \(t\) of \(C\). In the completed local ring \(k[[t]]\), the pulled-back ideal of the diagonal is generated by \(t-\varphi^\#t\). It is nonzero, by the preceding argument. The intersection multiplicity is

\[
\dim_k k[[t]]/(t-\varphi^\#t)
=\operatorname{ord}_t(t-\varphi^\#t).
\tag{4.4}
\]

Completion preserves the length of this finite-length module. Summing these lengths is the intersection number, proving (4.2). This calculation includes inseparable maps and multiple fixed points; it never assumes that the derivative of \(\varphi\) is nonzero. \(\square\)

The identity map also satisfies (4.1), with value \(2-2g\) by (3.8), but its fixed-point scheme is the whole curve. Thus the numerical intersection formula and the finite fixed-point interpretation have different hypotheses. If a smooth projective curve is allowed to be disconnected, the same proof works using its full cohomology and the sum trace: duality, graph compatibility and Künneth still give (4.3). The length interpretation requires isolated fixed points, equivalently that no component is mapped identically to itself. Merely requiring the global map to differ from the identity is insufficient in this disconnected case.

For \(n=\ell^a\), the curve groups \(H^i(C,\Lambda_n)\) are free of ranks \(1,2g,1\), and the duality pairing is perfect. Finite-coefficient Künneth has no Tor terms here because these groups are free. Consequently the dual-basis proof (3.4) and the matrix proof (4.3) work over \(\Lambda_n\) word for word. In particular,

\[
(\Gamma_\varphi\cdot\Delta)\bmod\ell^a
=\sum_i(-1)^i
\operatorname{Tr}_{\Lambda_n}\bigl(\varphi^*;H^i(C,\Lambda_n)\bigr).
\tag{4.5}
\]

This gives the finite-level form needed for the coefficient argument in the next lesson, without replacing a trace on a free module by a trace on an arbitrary torsion module. Compare [Stacks, Tag 03U3](https://stacks.math.columbia.edu/tag/03U3).

**Example 4.2 (the projective line).** Its only nonzero cohomology groups have degrees zero and two. The former has operator \(1\); the latter has operator \(\deg\varphi\), as shown after Lemma 1.2. Thus

\[
(\Gamma_\varphi\cdot\Delta)=1+\deg\varphi.
\tag{4.6}
\]

For a constant map there is one simple fixed point; its differential is zero and (4.4) has order one. For an automorphism distinct from the identity, the total fixed-point length is two, whether it has two simple fixed points or one double fixed point.

**Example 4.3 (multiplication on an elliptic curve).** Let \(C=E_0\) be an elliptic curve over \(k\), and take \(\varphi=[m]\), \(m\in\mathbf Z\). Let \(\mu:E_0\times E_0\to E_0\) be addition. Künneth gives \(H^1(E_0\times E_0,E)=H^1(E_0,E)\oplus H^1(E_0,E)\). Restriction to either axis is the projection to its corresponding summand. Since addition on either axis is the identity, \(\mu^*a=p_1^*a+p_2^*a\) for every \(a\in H^1\). Pull back by \((\operatorname{id},[m])\): the identity \([m+1]=\mu\circ(\operatorname{id},[m])\) gives \([m+1]^*a=a+[m]^*a\). The zero map factors through a point and kills \(H^1\). Recursing upward and downward from \(m=0\) proves \([m]^*a=ma\) for every integer \(m\). This supplies the pullback calculation directly from the group law and Künneth.

The cup pairing of two degree-one classes is nonzero and generates the one-dimensional top cohomology. Pullback respects cup product, so \([m]^*\) on \(H^2\) is the scalar \(m^2\). Its trace on \(H^0\) is \(1\), giving

\[
(\Gamma_{[m]}\cdot\Delta)=1-2m+m^2=(1-m)^2.
\tag{4.7}
\]

For \(m\ne1\), the fixed scheme is the kernel scheme \(E_0[m-1]\), and its length is \((m-1)^2\). This conclusion counts scheme length. Its number of geometric points equals that length when \(m-1\) is prime to the characteristic, since the derivative of \([m-1]\) is then invertible. In characteristic \(p\), taking \(m=p+1\) gives the group scheme \(E_0[p]\), which is nonreduced; counting distinct geometric points would give the wrong intersection number. This is the correction needed in [Stacks, Example 03U2](https://stacks.math.columbia.edu/tag/03U2). The case \(m=1\) belongs to the identity-map numerical formula, not to a finite-point count.

### The diagonal calculation in every dimension

The parity argument does not depend on dimension one or on projectivity. Let \(X/k\) be smooth, proper and purely \(d\)-dimensional, and let \(\varphi:X\to X\) be any morphism. The diagonal and graph are smooth closed immersions of codimension \(d\). Their classes are the images of their supported purity generators in \(H^{2d}(X\times X,E(d))\).

**Theorem 4.4 (cohomological graph pairing).** Define

\[
L_X(\varphi)=\int_{X\times X}
\operatorname{cl}(\Gamma_\varphi)\cup\operatorname{cl}(\Delta_X).
\]

Then

\[
L_X(\varphi)=\sum_{i=0}^{2d}(-1)^i
\operatorname{Tr}(\varphi^*;H^i(X,E)).
\tag{4.8}
\]

**Proof.** Choose right-dual bases with \(\int_Xe_{i,j}\cup e_{i,j'}^\vee=\delta_{jj'}\). The proof of Lemma 3.1 applies with \(2d\) in place of \(2\). Its two exchanged orders both have parity \(i(2d-i)\equiv i\pmod2\), so they cancel in the test pairing. It gives

\[
\operatorname{cl}(\Delta_X)=\sum_{i,j}(-1)^i e_{i,j}\otimes e_{i,j}^\vee.
\tag{4.9}
\]

The Gysin projection and trace identities apply to the smooth graph, in every codimension, by the closed adjunction in Proposition 1.1. Hence

\[
L_X(\varphi)=\int_X\gamma_\varphi^*\operatorname{cl}(\Delta_X)
=\sum_{i,j}(-1)^i\int_Xe_{i,j}\cup\varphi^*e_{i,j}^\vee.
\]

Contraction with the right-dual basis gives \(\operatorname{Tr}(\varphi^*;H^{2d-i})\), exactly as in (4.3). Reindex by \(2d-i\); parity is unchanged. This proves (4.8). Finite dimensionality, perfect duality and Künneth were proved in the exact providers above and passed to rational coefficients in Proposition 1.1. No separability of \(\varphi\) and no choice of a projective embedding entered the proof. \(\square\)

**Theorem 4.5 (isolated fixed points, with multiplicities).** Suppose \(\varphi:X\to X\) has isolated fixed points. Then its fixed scheme is finite and

\[
L_X(\varphi)=\sum_{\varphi(x)=x}
\operatorname{length}_k\mathcal O_{\operatorname{Fix}(\varphi),x}.
\tag{4.9a}
\]

**Proof.** The fixed scheme is a closed zero-dimensional subscheme of the proper scheme \(X\), so it is finite. Near \((x,x)\), choose étale coordinates \(t_1,\ldots,t_d\) on \(X\). The differences of their two pullbacks give smooth normal coordinates for the diagonal. Proposition 1.1, iterated through the smooth coordinate flag, identifies its supported class with the pullback of the positive point class of \(0\in\mathbf A^d\). Pulling this map to the graph gives the functions \(t_j\circ\varphi-t_j\), whose ideal defines the fixed scheme near \(x\). An isolated zero makes this ideal primary for the maximal ideal in the regular local ring \(\mathcal O_{X,x}\). Lemma 1.7 therefore identifies the graph's supported pullback of the diagonal class with

\[
\operatorname{length}_k\mathcal O_{\operatorname{Fix}(\varphi),x}
\cdot\operatorname{cl}_X(x).
\]

Excision decomposes support in the finite fixed set into the sum of these point supports. The Gysin projection formula for the graph and the trace-one normalization of each point show that the pairing in (4.8) is the sum of those lengths, first modulo every invertible \(n\), then integrally at \(\ell^a\), and finally in \(E\). Theorem 4.4 identifies this pairing with \(L_X(\varphi)\). This proves (4.9a). No transversality or separability is required. \(\square\)

This is the full isolated-fixed-point assertion of Deligne [Cycle], Corollary 3.7, and Milne [LEC], Theorem 25.1. Locally its intersection multiplicity can also be written as an alternating Tor length. The diagonal's normal equations form a regular sequence; their restrictions to the smooth graph are a system of parameters and hence a regular sequence. Their Koszul resolution consequently has no positive Tor after tensoring with the graph's local ring. The alternating Tor length is therefore exactly the degree-zero quotient length in (4.9a).

**Corollary 4.5a (transverse fixed points).** If \(1-d\varphi_x\) is invertible on \(T_xX\) at every fixed point, the fixed scheme is finite and reduced, and \(L_X(\varphi)\) is its number of points.

**Proof.** In étale coordinates the pulled-back diagonal equations have linear parts \(1-d\varphi_x\), up to a common sign. Invertibility makes them a regular system of parameters at \(x\); the completed local quotient is \(k\). Thus every fixed point is isolated and has length one. Apply Theorem 4.5. \(\square\)

In particular, the base-changed \(q^r\)-power Frobenius of any smooth proper \(X_0/\mathbf F_q\) has zero differential. [Frobenius morphisms and their action on cohomology, Theorem 5.1](course:AG-LTF/frobenius-morphisms-and-their-action-on-cohomology) identifies its reduced fixed scheme with \(X_0(\mathbf F_{q^r})\). Thus (4.8) gives the constant-coefficient trace formula in every dimension. Disconnected schemes are included through their full cohomology and the sum trace.

There is also a finite-coefficient formulation that does not suppose the cohomology groups are free. Put \(P=R\Gamma(X,\Lambda_n)\). [Traces of perfect complexes and Lefschetz numbers, Theorem 4.3](course:AG-LTF/traces-of-perfect-complexes-and-lefschetz-numbers) proves that \(P\) is perfect. Duality identifies \(P^\vee\) with \(R\Gamma(X,\Lambda_n(d))[2d]\), and derived Künneth identifies the diagonal class with a map \(\Lambda_n\to P\otimes^LP^\vee\). This is the coevaluation: under \(P\otimes^LP^\vee=R\operatorname{Hom}(P,P)\), its induced correspondence is the identity, since both projections composed with the diagonal are the identity and the Gysin projection formula composes their adjunctions. Pulling to the graph and integrating contracts this map with \(\varphi^*\) on its second factor. Evaluation with the Koszul interchange is the trace of that operator on \(P^\vee\). After a generator of \(\mu_n(k)\) is chosen, this factor is \(P(d)[2d]\), on which the operator is the pullback on \(P\) with an even shift and a trivial rank-one twist. Its trace is therefore \(\operatorname{Tr}(\varphi^*;P)\). On a finite-projective representative, a splitting into a finite free module writes coevaluation as the identity idempotent; contraction with a degree-preserving chain map gives \(\sum_j(-1)^j\operatorname{Tr}(u^j;P^j)\). The sign is the interchange of a degree-\(j\) vector with its degree-\(-j\) dual. Theorems 1.2 and 2.2 of that lesson prove independence of the splitting and representative. Thus

\[
\int_{X\times X}\operatorname{cl}_n(\Gamma_\varphi)
\cup\operatorname{cl}_n(\Delta_X)
=\operatorname{Tr}(\varphi^*;R\Gamma(X,\Lambda_n)).
\tag{4.10}
\]

For isolated fixed points the left side is the sum of their local lengths modulo \(n\), by Lemma 1.7 and Theorem 4.5; transverse fixed points each contribute one. Arbitrary torsion cohomology groups never replace the perfect complex in (4.10).

**Corollary 4.6 (a stable open curve).** Let \(\varphi:C\to C\) have isolated fixed points, and let \(U\subset C\) be open with \(\varphi^{-1}(U)=U\). Suppose every fixed point in \(B=C-U\) has multiplicity one. Then

\[
\sum_{\substack{x\in U\\\varphi(x)=x}}
\operatorname{length}_k\mathcal O_{\operatorname{Fix}(\varphi),x}
=\sum_i(-1)^i\operatorname{Tr}(\varphi^*;H^i_c(U,E)).
\tag{4.11}
\]

**Proof.** The restriction \(\varphi:U\to U\) is proper, since it is the base change of \(\varphi:C\to C\) by \(U\hookrightarrow C\). Thus its pullback preserves compact support. The closed-open triangle \(R\Gamma_c(U,E)\to R\Gamma(C,E)\to R\Gamma(B,E)\) is compatible with that action, by the assumed inverse-image equality. The alternating trace of its finite long exact cohomology sequence is zero: split each term into its image from the preceding arrow and the image in the following term, add their traces, and cancel each image's two opposite contributions. Consequently the trace on \(U\) is the trace on \(C\) minus the trace on \(B\). The finite reduced set \(B\) has only degree-zero cohomology. Pullback on its functions has diagonal entry one at each fixed point and zero at every other point, so its trace is the number of its fixed points. Their multiplicities are one by hypothesis. Subtracting them from Theorem 4.1 proves (4.11). This is Deligne [Rapport], Corollary 5.4; it does not apply with the same unweighted subtraction when a boundary fixed point has higher multiplicity. \(\square\)

## 5. Frobenius and the zeta numerator

Let \(C_0/\mathbf F_q\) be smooth, projective and geometrically connected, and put \(C=C_0\times_{\mathbf F_q}k\), where \(k=\overline{\mathbf F}_q\). A smooth connected curve over an algebraically closed field is integral: its regular local rings are domains, so its irreducible components are disjoint, and connectedness permits only one. Thus \(C_0\) is geometrically integral. Let \(F:C\to C\) be the base change of the \(q\)-power Frobenius of \(C_0\), as defined in [Frobenius morphisms and their action on cohomology](course:AG-LTF/frobenius-morphisms-and-their-action-on-cohomology). Write \(F_i\) for its operator on \(H^i(C,E)\) with constant coefficients. It is geometric Frobenius on these groups.

### Degree and point counts

We first prove \(\deg F^r=q^r\). On an affine \(\mathbf F_q\)-algebra generated by \(a_1,\ldots,a_m\), every element is a linear combination over the image of the \(q^r\)-power map of the monomials \(a_1^{e_1}\cdots a_m^{e_m}\), with \(0\leq e_i<q^r\). Group polynomial monomials by these residues; coefficients in \(\mathbf F_q\) are \(q^r\)-th powers. Frobenius is therefore finite. Let \(K_0=\mathbf F_q(C_0)\), choose a transcendental \(u\in K_0\), and put \(e=[K_0:\mathbf F_q(u)]\). Raising to \(q^r\)-th powers is a field isomorphism onto its image and gives

\[
[K_0^{q^r}:\mathbf F_q(u^{q^r})]=e,
\qquad [\mathbf F_q(u):\mathbf F_q(u^{q^r})]=q^r.
\]

For the second equality, \(1,u,\ldots,u^{q^r-1}\) span by grouping exponents and are independent by clearing a common denominator and comparing the distinct exponent residues. Computing \([K_0:\mathbf F_q(u^{q^r})]\) along the two towers gives \([K_0:K_0^{q^r}]=q^r\). This is the degree of Frobenius on \(C_0\). It is also its finite flat rank: over each local DVR of the target curve the finite source algebra is torsion-free by dominance, hence free. To see the last elementary assertion, lift a basis modulo the uniformizer, use Nakayama for generation, and eliminate any relation by dividing its coefficients by their minimum uniformizer order; torsion-freeness allows this division and contradicts independence modulo the uniformizer. Field extension preserves finite flat rank. Hence the base-changed \(k\)-morphism \(F^r\) has degree \(q^r\). It is this base-changed map, rather than absolute Frobenius on the constants of \(k\), that we use.

[Frobenius morphisms and their action on cohomology, Theorem 5.1](course:AG-LTF/frobenius-morphisms-and-their-action-on-cohomology) proves that the fixed scheme of \(F^r\) is reduced and that its geometric points are exactly \(C_0(\mathbf F_{q^r})\). In particular \(F^r\ne\operatorname{id}\), and Theorem 4.1 gives

\[
N_r:=\#C_0(\mathbf F_{q^r})
=1-\operatorname{Tr}(F_1^r)+q^r,\qquad r\geq1.
\tag{5.1}
\]

Here \(H^0\) contributes \(1\) because \(C\) is connected, and \(H^2\) contributes \(q^r\) by the degree calculation. Every fixed point has length one.

The coefficient convention deserves a check. The Chern-class calculation uses pullback by a \(k\)-morphism and its natural \(k\)-linear coefficient map on \(\mu_{\ell^a}\); roots of unity in \(k\) are preserved. After trivializing the twist this gives the same operator as constant-coefficient pullback, so the top-degree operator in (5.1) is \(q^r\). The *descended Frobenius correspondence* on the Tate-twisted sheaf of Lesson 3 additionally acts on its fibre by \(q^{-r}\). Its top-degree operator on \(H^2(C,E(1))\) is therefore \(1\). The twist trivialization is not equivariant for that descended correspondence. Equation (5.1) uses untwisted constant coefficients throughout.

Define the point-counting zeta function as a formal power series

\[
Z(C_0,t)=\exp\left(\sum_{r\geq1}N_r\frac{t^r}{r}\right).
\tag{5.2}
\]

It is also \(\prod_x(1-t^{\deg x})^{-1}\), over closed points \(x\). A point of degree \(d\) gives \(d\) embeddings of its residue field into \(\mathbf F_{q^r}\) when \(d\mid r\), and none otherwise. Expanding the logarithm of the product proves (5.2). The point sets over each finite field are finite, as a finite affine cover and finitely many algebra generators show; consequently there are finitely many closed points of bounded degree. The product is well-defined in \(\mathbf Z[[t]]\): its coefficient counts effective divisors of that degree.

For an endomorphism \(A\) of a finite-dimensional vector space over a characteristic-zero field,

\[
\det(1-tA)=
\exp\left(-\sum_{r\geq1}\operatorname{Tr}(A^r)\frac{t^r}{r}\right).
\tag{5.3}
\]

To prove this without assuming diagonalizability, extend the field to split the characteristic polynomial and triangularize \(A\). Choose an eigenvector and apply induction to the quotient to obtain such a triangularization. Its diagonal entries \(\lambda_j\) give determinant \(\prod_j(1-t\lambda_j)\) and traces \(\sum_j\lambda_j^r\). Taking formal logarithms proves (5.3); both sides descend to the original field.

### Rationality, integrality and the functional equation

**Corollary 5.1 (the numerator and independence of \(\ell\)).** There is a single polynomial \(P(t)\in\mathbf Z[t]\), with \(P(0)=1\), such that

\[
Z(C_0,t)=\frac{P(t)}{(1-t)(1-qt)},\qquad
\det(1-tF_1;H^1(C,E))=P(t)
\tag{5.4}
\]

for every \(\ell\ne p\). Moreover \(\deg P=2g\), its leading coefficient is \(q^g\), and

\[
\det(T-F_1)=T^{2g}P(T^{-1})\in\mathbf Z[T]
\tag{5.5}
\]

is independent of \(\ell\).

**Proof.** Substitute (5.1) into (5.2) and use (5.3). The identities \(\exp(\sum_rt^r/r)=(1-t)^{-1}\) and \(\exp(\sum_rq^rt^r/r)=(1-qt)^{-1}\) give

\[
Z(C_0,t)=\frac{\det(1-tF_1)}{(1-t)(1-qt)}
\quad\text{in }E[[t]].
\tag{5.6}
\]

The series \((1-t)(1-qt)Z(C_0,t)\) has integer coefficients by the Euler product. Its image in \(E[[t]]\) is a polynomial of degree at most \(\dim H^1=2g\); injectivity of \(\mathbf Z\to E\) makes every subsequent integer coefficient zero. Thus it is one integer polynomial \(P\), and the same point-counting series identifies every \(\ell\)-adic determinant with it. Its constant coefficient is one.

Let \(V=H^1(C,E)\), \(A=F_1\), and trivialize \(E(1)\) to view the nondegenerate alternating pairing as \(\langle\ ,\ \rangle:V\times V\to E\). Since the top-degree operator is \(q\), cup-product naturality gives \(\langle Av,Aw\rangle=q\langle v,w\rangle\). It forces \(A\) to be invertible. If \(\omega\in\bigwedge^2V^*\) is this pairing, then \(A^*\omega=q\omega\). A symplectic basis gives \(\omega^g=g!\,a_1^*\wedge b_1^*\wedge\cdots\wedge a_g^*\wedge b_g^*\ne0\) in characteristic zero. Thus \(A^*\omega^g=q^g\omega^g\), while its action on this top exterior power is \(\det A\). Hence \(\det A=q^g\). The even dimension makes this the leading coefficient of \(P\), proving its exact degree and (5.5). For \(g=0\), these statements use the determinant of the zero-dimensional space, which is one. \(\square\)

**Theorem 5.2 (functional equation).** One has

\[
P(t)=q^g t^{2g}P\bigl((qt)^{-1}\bigr),\qquad
Z\bigl(C_0,(qt)^{-1}\bigr)
=q^{1-g}t^{2-2g}Z(C_0,t).
\tag{5.7}
\]

**Proof.** In a basis with pairing matrix \(J\), the multiplier identity is \(A^{\mathsf t}JA=qJ\). Therefore \(A^{\mathsf t}=qJA^{-1}J^{-1}\). Transposition preserves the characteristic polynomial, and similarity does also; the eigenvalue multiset is consequently stable, with multiplicities, under \(\alpha\mapsto q/\alpha\). Write \(P(t)=\prod_{j=1}^{2g}(1-\alpha_jt)\) over a splitting field. The preceding determinant calculation gives \(\prod_j\alpha_j=q^g\), and

\[
q^g t^{2g}P\bigl((qt)^{-1}\bigr)
=\prod_j\bigl(1-(q/\alpha_j)t\bigr)=P(t).
\]

This polynomial equality holds over \(\mathbf Q\) since \(P\) has integer coefficients. The denominator transforms by
\((1-(qt)^{-1})(1-t^{-1})=(1-t)(1-qt)/(qt^2)\), proving the second equality. \(\square\)

The numbers \(\alpha_j\) are algebraic integers, being roots of the monic polynomial (5.5). In \(\mathbf C\) their multiset is stable both under conjugation and under \(\alpha\mapsto q/\alpha\). Comparing logarithms in (5.2) and (5.4) yields

\[
\sum_{j=1}^{2g}\alpha_j^r=q^r+1-N_r,\qquad r\geq1.
\tag{5.8}
\]

### Weil's inequality from the surface Hodge theorem

We now prove the bound needed to locate every \(\alpha_j\). Work on \(S=C\times_k C\), a smooth projective integral surface. Geometric integrality of the factors ensures integrality of the product: its projection is open and its fibres are geometrically integral; the images of two nonempty opens meet on the integral base, and their nonempty open subsets in a fibre meet. Smoothness makes the product reduced. Fix \(x\in C(k)\), and put \(V_x=\{x\}\times C\), \(W_x=C\times\{x\}\). These are smooth Cartier divisors. The restriction formula proved in §2.4 gives

\[
V_x^2=W_x^2=0,\qquad V_x\cdot W_x=1,
\qquad H:=V_x+W_x,\qquad H^2=2.
\tag{5.9}
\]

For example, \(\mathcal O(V_x)|_{V_x}\) is the pullback of a line on the point \(x\), hence trivial, whereas \(\mathcal O(W_x)|_{V_x}=\mathcal O_C(x)\) has degree one. The point \(x\) is chosen over \(k\); no degree-one divisor over \(\mathbf F_q\) is being assumed.

Let \(\Gamma_r\) be the graph of \(F^r\), and let \(\Delta\) be the diagonal. Restriction to these smooth divisors gives

\[
\Gamma_r\cdot V_x=1,\quad
\Gamma_r\cdot W_x=q^r,\quad
\Delta\cdot V_x=\Delta\cdot W_x=1,\quad
\Gamma_r\cdot\Delta=N_r.
\tag{5.10}
\]

For the second equality we use \(\deg f^*L=(\deg f)\deg L\) for a finite flat map of smooth curves. It follows by writing \(L\) as a divisor: the fibre over a point has total length equal to the flat rank, and its DVR lengths are exactly the multiplicities of the pulled-back divisor. For the last equality, restrict the defining section of \(\Gamma_r\) to \(\Delta\). Its zero scheme is precisely the fixed scheme of \(F^r\); that scheme is finite and reduced, so every DVR order is one, and its degree is \(N_r\). The restriction formula gives the asserted intersection directly, in agreement with Theorem 4.1.

The graph's normal bundle is \((F^r)^*T_C\). Indeed its tangent inclusion is \(v\mapsto(v,dF^r(v))\) in \(T_C\oplus(F^r)^*T_C\), and \((v,w)\mapsto w-dF^r(v)\) identifies its quotient with \((F^r)^*T_C\). A smooth curve in the smooth surface is a regular immersion of codimension one, by the regular-quotient calculation in §2.2, so this normal bundle is \(\mathcal O_S(\Gamma_r)|_{\Gamma_r}\). Curve Riemann–Roch in §2.3 gives \(\deg T_C=2-2g\). Consequently

\[
\Gamma_r^2=q^r(2-2g),\qquad \Delta^2=2-2g.
\tag{5.11}
\]

Define two integral divisor classes
\(D_r=\Gamma_r-q^rV_x-W_x\) and \(D_0=\Delta-V_x-W_x\). Equations (5.9)–(5.11) give

\[
D_r\cdot H=D_0\cdot H=0,\qquad
D_r^2=-2gq^r,\quad D_0^2=-2g,\quad
D_r\cdot D_0=N_r-q^r-1.
\]

The positive-square Hodge theorem proved in §2.6 applies to \(H\). For every pair of integers \(a,b\), it gives \((aD_r+bD_0)^2\leq0\). Homogeneity extends this to rational \(a,b\), and continuity to real \(a,b\). If both diagonal terms of this binary form are negative, completing the square gives \((D_r\cdot D_0)^2\leq D_r^2D_0^2\). If either diagonal term is zero, varying its coefficient with both signs forces the mixed term to be zero, and gives the same inequality. Therefore

\[
\boxed{|N_r-q^r-1|\leq2gq^{r/2}\quad(r\geq1).}
\tag{5.12}
\]

**Theorem 5.3 (the Riemann hypothesis for curves).** Every complex root \(\alpha_j\) of (5.5), and hence every complex conjugate of every Frobenius eigenvalue, has absolute value \(q^{1/2}\).

**Proof.** By (5.8) and (5.12), the series \(\sum_{r\geq1}(\sum_j\alpha_j^r)t^r\) converges for \(|t|<q^{-1/2}\). Near zero it is the rational function \(\sum_j\alpha_jt/(1-\alpha_jt)\). Each distinct nonzero value \(\alpha\) gives a pole at \(t=1/\alpha\): equal values add their positive multiplicities, and unequal values have different poles. These poles cannot cancel. A holomorphic power series has no pole in its disc of convergence, so \(|\alpha_j|\leq\sqrt q\). Theorem 5.2 puts \(q/\alpha_j\) in the same multiset and gives the reverse inequality. Thus \(|\alpha_j|=\sqrt q\). For \(g=0\), the multiset is empty and (5.12) already gives \(N_r=q^r+1\). \(\square\)

Corollary 5.1 identifies the Frobenius spectrum with this algebraic multiset, with algebraic multiplicities; it does not assert diagonalizability. Theorem 5.3 says that \(H^1(C,E)\) with geometric Frobenius is **pure of weight \(1\)**. The absolute values are taken after embedding the algebraic numbers into \(\mathbf C\). The argument has proved rationality, the functional equation and the Riemann hypothesis inside this lesson, using its curve trace and the surface inequality proved in §§2.1–2.7.

## 6. Frobenius on an elliptic curve

This section proves the polynomial anticipated in Lesson 3. Let \(E_0/\mathbf F_q\) be an elliptic curve and put

\[
a=q+1-\#E_0(\mathbf F_q).
\]

Formula (5.1) at \(r=1\) gives \(\operatorname{Tr}(F_1)=a\). The two-dimensional space \(H^1(E,E)\) has a nondegenerate alternating cup pairing. Because the top-degree operator is \(q\), pullback of cup products gives

\[
\langle F_1u,F_1v\rangle=q\langle u,v\rangle.
\tag{6.1}
\]

Choose \(u,v\) with \(\langle u,v\rangle=1\). For a two-by-two matrix \(A\), expanding its two columns in this basis gives \(\langle Au,Av\rangle=\det(A)\). Applying this to (6.1) proves \(\det(F_1)=q\). Hence

\[
\det(T-F_1)=T^2-aT+q.
\tag{6.2}
\]

For the smooth projective model of \(y^2+y=x^3+x\) over \(\mathbf F_2\), each of \(x=0,1\) gives \(y=0,1\), and the projective cubic has the unique point \([0:1:0]\) at infinity. There are therefore five rational points. Thus \(a=-2\), and

\[
\det(T-F_1)=T^2+2T+2,\qquad
\alpha_1,\alpha_2=-1+i,-1-i.
\tag{6.3}
\]

This example's former zeta roots are now identified with its \(H^1\) eigenvalues. Their fourth powers are both \(-4\), so (5.1) gives \(N_4=1+16-(-8)=25\), in agreement with the zeta calculation. The sum, determinant, and point counts use geometric Frobenius; arithmetic Frobenius has the inverse eigenvalues.

## 7. Exercises with complete solutions

**Exercise 7.1 (easy: a power map on the projective line).** For \(d\geq2\), consider \(\varphi:\mathbf P^1\to\mathbf P^1\), \(x\mapsto x^d\). Compute both sides of (4.1), retaining fixed-point multiplicities in every characteristic.

**Solution.** The degree is \(d\); \(H^1=0\), \(H^0\) has trace \(1\), and \(H^2\) has trace \(d\). The cohomological answer is \(1+d\). In the affine chart the fixed scheme has equation \(x^d-x=0\), a polynomial of degree \(d\); its sum of root multiplicities over \(k\) is \(d\). At infinity use \(z=1/x\). The fixed equation is \(z^d-z=0\), whose order at \(z=0\) is one, since its linear coefficient is \(-1\). The total length is \(d+1\).

For example, if \(\operatorname{char}k=p\) divides \(d-1\), the nonzero roots of \(x^{d-1}-1\) can be multiple. If \(d-1=p^ab\) with \(p\nmid b\), this polynomial is \((x^b-1)^{p^a}\): there are \(b\) distinct nonzero fixed points, each of multiplicity \(p^a\), as well as the simple fixed points \(0,\infty\). The sum remains \(p^ab+2=d+1\). The excluded \(d=1\) is the identity; its numerical intersection number is two but its fixed scheme is not finite.

**Exercise 7.2 (medium: self-intersection).** Let \(D\subset S\) be a smooth divisor. Prove

\[
\int_S c_{1,n}(\mathcal O(D))^2=(D\cdot D)\pmod n
\]

by restricting to \(D\), and interpret the answer using its normal bundle.

**Solution.** Put \(L=\mathcal O_S(D)\). Equation (1.6) and naturality give \(\int_Sc_{1,n}(L)^2=\int_Dc_{1,n}(L|_D)=\deg(L|_D)\bmod n\) by Lemma 1.2. Formula (2.1) identifies that degree with \((D\cdot D)\). The ideal of \(D\) is \(L^{-1}\), so its conormal bundle is \(L^{-1}|_D\), and its normal bundle is \(L|_D\). Thus the self-intersection is \(\deg N_{D/S}\). The same argument gives the exact integer viewed in \(\mathbf Q_\ell\) after taking the compatible inverse limit.

**Exercise 7.3 (medium: characteristic polynomial).** Explain why (5.4) proves independence of \(\ell\) for the characteristic polynomial, including its degree and leading coefficient. Express its coefficient of \(T^{2g-1}\) in terms of \(N_1\).

**Solution.** The polynomial \(\det(1-tF_1)\) is the fixed integer polynomial \(P(t)\). The dimension of \(H^1\) is \(2g\), and reversing the polynomial gives \(\det(T-F_1)=T^{2g}P(T^{-1})\). Its degree is \(2g\) and its leading coefficient is \(P(0)=1\). Its coefficient of \(T^{2g-1}\) is \(-\operatorname{Tr}(F_1)=N_1-q-1\) by (5.1). In genus zero the characteristic polynomial is \(1\), and there is no such coefficient. Independence concerns the polynomial and eigenvalue multiset; it does not canonically identify the vector spaces for different primes.

**Exercise 7.4 (medium: an involution).** Let \(\iota\ne\operatorname{id}\) be an involution of a connected curve \(C\), with \(b\) fixed points all of multiplicity one. Compute \(\operatorname{Tr}(\iota^*;H^1)\). Deduce the dimensions of its \(+1\) and \(-1\) eigenspaces.

**Solution.** An automorphism has degree one, so its traces in degrees zero and two are both one. The fixed-point formula gives \(b=2-\operatorname{Tr}(\iota^*;H^1)\), or trace \(2-b\). The operator squares to the identity on a characteristic-zero vector space; the polynomial \((T-1)(T+1)\) has distinct roots, so the operator is diagonalizable even when \(\ell=2\). If the two dimensions are \(u,v\), then \(u+v=2g\), \(u-v=2-b\). Hence \(u=g+1-b/2\), \(v=g-1+b/2\). In particular this hypothesis forces \(b\) even and both displayed integers nonnegative.

**Exercise 7.5 (hard: transfer of the curve Riemann hypothesis).** Use Theorem 5.3 and Corollary 5.1 to prove weight \(1\), stating precisely which absolute values are involved.

**Solution.** Corollary 5.1 identifies the characteristic polynomial over every \(E=\mathbf Q_\ell\) with \(T^{2g}P(T^{-1})\). The eigenvalues are therefore the algebraic numbers \(\alpha_j\) defined by \(P(t)=\prod_j(1-\alpha_jt)\). Every conjugate of any \(\alpha_j\) is again a root of this characteristic polynomial, since it has rational coefficients. Theorem 5.3 gives absolute value \(\sqrt q\) for each root in a complex splitting field. Thus every embedding of \(\mathbf Q(\alpha_j)\) into \(\mathbf C\) has \(|\alpha_j|=\sqrt q\), which is weight \(1\). This statement uses the usual complex absolute value, not the \(\ell\)-adic norm. It is empty when \(g=0\).

**Exercise 7.6 (hard: check the diagonal sign).** On a genus-one curve, use (3.7) to compute \(\delta^*[\Delta]\). Explain what the result would be if the middle-degree sign in (3.4) were omitted.

**Solution.** Choose \(a,b\in H^1\) with \(\int_Ca\cup b=1\), so \(a\cup b=\eta\) and \(b\cup a=-\eta\). Pullback of the first two terms in (3.7) gives \(2\eta\). The remaining terms give \(b\cup a-a\cup b=-2\eta\). Thus \(\delta^*[\Delta]=0\), and \(\Delta^2=0\), as required by the trivial tangent bundle of an elliptic curve. If right duals were used but the middle-degree sign omitted, the last two terms would instead pull back to \(2\eta\); the result would be \(4\eta\). Its trace \(4\) contradicts the self-intersection. This test detects the sign, including over \(\mathbf Q_2\), where \(4\ne0\).

**Exercise 7.7 (medium: a nonsplit extension).** Let \(0\to L\to V\to M\to0\) be an extension of line bundles on a smooth scheme. Determine \(c_1(V)\), \(c_2(V)\) and the relation for \(\xi\) on \(\mathbf P(V)\). Explain why a filtration by \(L,M\) does not supply an actual global direct-sum decomposition.

**Solution.** The Whitney formula gives \(c_t(V)=(1+c_1(L)t)(1+c_1(M)t)\). Thus \(c_1(V)=c_1(L)+c_1(M)\), \(c_2(V)=c_1(L)c_1(M)\), and \(\xi^2+\pi^*(c_1(L)+c_1(M))\xi+\pi^*(c_1(L)c_1(M))=0\). A global splitting is a lift \(M\to V\) of the identity of \(M\); locally chosen lifts differ by sections of \(\mathcal Hom(M,L)\), and their Čech cocycle can be nonzero. The splitting torsor in Theorem 1.4 supplies such a lift after pullback, while inducing an isomorphism on constant étale cohomology. This proves the formula without asserting that the original extension is split.

**Exercise 7.8 (medium: the tangent bundle of projective space).** Put \(h=c_1(\mathcal O_{\mathbf P^s}(1))\). Prove that \(c_t(T_{\mathbf P^s})=(1+ht)^{s+1}\) in degrees at most \(s\). Compute its top Chern class.

**Solution.** A tangent vector at a line \(L\subset k^{s+1}\) is a first-order displacement \(L\to k^{s+1}/L\). This description glues on the standard affine coordinate charts, giving \(T=\mathcal Hom(\mathcal O(-1),Q)\), where \(0\to\mathcal O(-1)\to\mathcal O^{s+1}\to Q\to0\) is the tautological sequence. Tensor it by \(\mathcal O(1)\) to obtain \(0\to\mathcal O\to\mathcal O(1)^{s+1}\to T\to0\). Whitney and the line normalization give \(c_t(T)=(1+ht)^{s+1}\). Its term of degree \(s+1\) vanishes because \(h^{s+1}=0\) by the projective-space computation. The term of degree \(s\) is \((s+1)h^s\), over every invertible finite coefficient ring and over \(\mathbf Z_\ell\) or \(\mathbf Q_\ell\). For \(s=0\) the tangent bundle has rank zero and its top class is \(1\), in agreement with the formula.

**Exercise 7.9 (medium: a nonreduced specialization).** In \(M=\mathbf A^1_x\times\mathbf A^1_t\), let \(T\) have equation \(t=x^e\), where \(e\geq1\), and use the projection to the \(t\)-line. Compute the pullback of the supported class of \(T\) to \(M_0=\mathbf A^1_x\). Explain why forgetting support hides this calculation.

**Solution.** The total curve \(T\) is smooth: its equation has derivative one with respect to \(t\), in every characteristic. Its zero fibre is \(\operatorname{Spec}k[x]/(x^e)\). It has one reduced point, whose local length is \(e\). Lemma 1.10b therefore gives \(i_0^*\operatorname{cl}_M(T)=e\,\operatorname{cl}_{\mathbf A^1}(0)\) in \(H^2_{\{0\}}(\mathbf A^1,\Lambda_n(1))\). This coefficient is \(e\bmod n\), even if the characteristic divides \(e\) or the finite coefficient ring has zero divisors. Both divisors are principal, so their ordinary Chern classes vanish. In particular \(H^2(\mathbf A^1,\Lambda_n(1))=0\), while purity makes the supported group one copy of \(\Lambda_n\). The supported comparison retains the scheme length that ordinary restriction alone cannot display.

## Proof dependencies

The finite-coefficient duality, smooth exceptional inverse image and Gysin counits have the exact programme homes stated before Proposition 1.1. The full higher-dimensional trace construction is proved in §§1–2 of the supporting lesson *Smooth traces, duality and Gysin maps*. General finite-coefficient finiteness, Brown representability and the foundational continuity assertions remain the explicitly named foundations of that lesson. Proposition 1.1 supplies the Kummer/Gysin comparison with a consistent divisor sign; Theorems 1.3–1.6 supply the projective-bundle, Chern-class and transverse-section arguments. Lemma 1.5 constructs supported classes for singular cycles by semi-purity. Lemmas 1.7–1.9 retain local lengths under pullback and finite pushforward, and Theorem 1.10 proves descent through rational equivalence. Lemmas 1.10a–1.10b prove arbitrary proper pushforward and specialization with multiplicities. The algebraic normal-cone and Chow homotopy constructions are specified before (1.24d); Theorem 1.10c proves all smooth-scheme pullbacks, the ring map and Chern compatibility at every invertible finite coefficient level and over \(\mathbf Z_\ell\). The algebraic Chow and resolution-property prerequisites are identified precisely before (1.25); Theorem 1.11 proves the rational Chern-character comparison, including the relative-Grassmannian argument when the normal bundle does not extend. Corollary 1.12 proves finite generation modulo numerical equivalence. Theorem 4.5 uses the supported local calculation for every isolated fixed point, including a nonreduced one.

The curve ranks and the general derived Künneth theorem have the exact homes given after (3.2). The Picard/Brauer geometric inputs remain in §6.1 of the multiplicative-group provider. Example 4.3 proves the multiplication operator from addition, without an additional dual-isogeny comparison.

Sections 2.1–2.7 give the coherent surface prerequisite with the algebra and duality proofs cited there: regular equations and their Koszul determinant, curve Riemann–Roch, ample twisting and smooth Bertini, the surface Euler formula, the uniform restriction bound and the Hodge equality clause. Section 5 proves Frobenius degree and finite flat rank; (5.1) and the Euler product prove the integral zeta numerator; the alternating cup pairing proves its functional equation; the surface Hodge theorem proves Weil's bound and the Riemann hypothesis. These classical curve conclusions are proved here. Theorem 5.1 of the Frobenius lesson proves the reduced fixed-scheme assertion. The trace formula for arbitrary constructible coefficient sheaves is developed in the following lessons. The higher-dimensional étale trace has its separate full proof in the supporting lesson cited above.

<a id="references-and-source-record"></a>

## References

James S. Milne, [*Lectures on Étale Cohomology*, version 2.21 (2013)](https://www.jmilne.org/math/CourseNotes/LEC.pdf), §§23–25, pp. 138–149: cycle and Chern classes, duality, and the Lefschetz calculation. The projective-bundle construction, complete Whitney argument, rational Chern/cycle comparison and numerical-equivalence theorem appear in §1 above. Our diagonal formula uses right duals with the explicit sign (3.4); fixed points are counted with scheme lengths in every dimension.

Alexander Grothendieck, [*La théorie des classes de Chern*](https://numdam.org/articles/10.24033/bsmf.1501/), *Bulletin de la Société Mathématique de France* **86** (1958), 137–154, §§2–3, Theorem 1, and §5, Theorem 2. The paper develops the projective-bundle characterization, Whitney formula and transverse-section formula. The proofs here use affine splitting torsors and work in étale cohomology over every invertible finite coefficient ring.

Deligne, *Cohomologie étale* (SGA \(4\frac12\)), [Cycle], §§1–2, especially §§2.1.2–2.1.5, printed pp. 138–139, and §§2.3.2–2.3.6, printed pp. 145–148, fixes the divisor normalization and its compatibility with trace. Theorem 2.3.8, printed pp. 148–150, treats weighted pullback and intersection. Our finite-coefficient Chow comparison gives an independent specialization proof using normalization and the normal cone. [Cycle], §§3.1–3.7, printed pp. 151–152, gives the cohomological correspondence calculation. [Dualité], §3, printed pp. 161–165, relates the diagonal's middle component to Jacobian duality. [Rapport], Theorem 5.3, printed p. 100, is the curve formula with isolated fixed points, followed by its historical attribution on p. 101.

The Stacks locators used here are [Tags 0FGS](https://stacks.math.columbia.edu/tag/0FGS), [0FGX](https://stacks.math.columbia.edu/tag/0FGX), [0FGZ](https://stacks.math.columbia.edu/tag/0FGZ), [0FH0](https://stacks.math.columbia.edu/tag/0FH0), [03U1](https://stacks.math.columbia.edu/tag/03U1), [03U2](https://stacks.math.columbia.edu/tag/03U2), [03U3](https://stacks.math.columbia.edu/tag/03U3), [03PK](https://stacks.math.columbia.edu/tag/03PK), [03RQ](https://stacks.math.columbia.edu/tag/03RQ), [0AMB](https://stacks.math.columbia.edu/tag/0AMB) and [0F1P](https://stacks.math.columbia.edu/tag/0F1P). The chapters are available in [AI Integrated Stacks Project, English, Weil Cohomology Theories](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/weil.html#weil-section-axioms-classical), [The Trace Formula](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/trace.html#trace-theorem-weil-trace-formula), and [Étale Cohomology](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-lemma-cohomology-smooth-projective-curve). The rational cycle-map argument uses the exact Chow and derived-scheme labels stated before (1.25), in the same project's source edition. Its *Weil Cohomology Theories*, `lemma-cycle-classes` and `lemma-done`, supplies the formal Chern and blowup route; the proof above supplies its fibre-degree calculation and uses a relative Grassmannian to cover nonprojective smooth schemes. The Adams computation uses the exterior-square filtration with middle term \(V'\otimes V''\). This corrects the middle-term typo in `lemma-second-adams-operator` and avoids its characteristic-two-sensitive symmetric/exterior sequence formula. This AI-integrated edition retains upstream tags. The human Stacks Project and the credited AI contributions retain their own GFDL terms.

Milne, [*The Riemann Hypothesis over Finite Fields: From Weil to the Present Day* (2015)](https://www.jmilne.org/math/xnotes/pRH.pdf), “The geometric proof of the Riemann hypothesis for curves,” and “Weil cohomology: The Lefschetz trace formula,” provides historical context and the general formal pattern. Our calculation specifies the right-dual convention and proves the surface intersection compatibility needed for curves. The Picard-variety facts behind the curve ranks retain their exact geometric prerequisite status; further background belongs to *Abelian varieties and Néron models* in the planned algebraic-geometry programme.

Ravi Vakil, [*The Rising Sea: Foundations of Algebraic Geometry*, 27 July 2024](https://math.stanford.edu/~vakil/216blog/FOAGjul2724public.pdf), Theorem 20.2.13, gives the classical surface Hodge statement. Sections 2.1–2.7 write the restriction-and-duality proof in full under the geometric-integrality hypothesis consumed by the curve product. The coherent prerequisite lessons retain their own authorship and licenses; they are cited at their exact proved statements. The new surface and curve exposition here retains this lesson's CC0 license.
