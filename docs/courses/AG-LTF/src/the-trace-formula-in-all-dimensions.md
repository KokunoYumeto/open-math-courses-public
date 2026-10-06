# The trace formula in all dimensions

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Original explanatory text is public domain (CC0). Human mathematical sources are credited below.*

The curve theorem becomes a theorem in every dimension by applying it to the fibres of a map. This requires coefficients that remember the cohomology of those fibres. They are the derived direct image with proper support, \(Rf_!K\). Its stalks carry both the fibre cohomology and the correct Frobenius operator.

We prove the compatibility of these operators, check that \(Rf_!\) preserves the coefficient class needed for induction, and make the induction explicit. We then pass from finite coefficients to integral adic and characteristic-zero coefficients. The passage uses traces of perfect complexes, so it allows torsion in integral cohomology.

## 1. Coefficients and the compact-support inputs

Put \(k_0=\mathbf F_q\), \(k=\overline{\mathbf F}_q\), and \(p=\operatorname{char}k_0\). A subscript \(0\) indicates a scheme or coefficient object over \(k_0\); its geometric base change has no subscript. Schemes are separated and of finite type over the indicated field. Our torsion coefficient ring \(\Lambda\) is unital and left Noetherian, may be noncommutative, is killed by an integer \(n\) prime to \(p\), and acts on the left. This includes every finite ring with \(p\nmid\#\Lambda\), but also rings such as \(\mathbf F_\ell[t,t^{-1}]\). Constructible \(\Lambda\)-modules have finitely generated stalk modules on finitely many locally constant strata; their underlying sets need not be finite. Their traces lie in

\[
\Lambda^\natural=\Lambda/
\langle ab-ba:a,b\in\Lambda\rangle_{\mathrm{add}}.
\tag{1.1}
\]

As before, \(D_{\mathrm{ctf}}\) means bounded constructible cohomology and finite Tor amplitude. If \(K\) has Tor amplitude \([a,b]\), then for every right \(\Lambda\)-module \(N\), its derived tensor \(N\otimes_\Lambda^{\mathbf L}K\) has cohomology only in that interval. The equivalent stalk criterion permits right module sheaves as well: derived tensors and their vanishing can be checked on geometric stalks.

We use the following compact-support foundations:

- [Cohomology with compact support](course:ag-etale-cohomology/cohomology-with-compact-support), §§6–9, constructs \(Rf_!=R\bar f_*j_!\), independently of the relative compactification, and proves composition and arbitrary base change. Its §§5,10 justify the unbounded-complex comparisons rather than presuming derived tensors are bounded below.
- Its Theorem 12.1 proves the bound \(R^uf_!\mathcal F=0\) for \(u>2c\), if geometric fibres have dimension at most \(c\), for every torsion sheaf, including infinite stalks. The absolute bound is \(2\dim X\).
- Its §12 expressly inherits general torsion constructibility from [Stacks, Tag 0GL0](https://stacks.math.columbia.edu/tag/0GL0). We use that stated foundation for the central finite ring \(A=\mathbf Z/n\), with separated finite-presentation morphisms between quasi-compact quasi-separated schemes. All our schemes are Noetherian and finite type over a field, so these hypotheses hold. Lemma 3.1 below proves the extension to the full left-module coefficient scope.
- [The proper base change theorem](course:ag-etale-cohomology/the-proper-base-change-theorem) and [Pushforward, pullback and finite morphisms](course:ag-etale-cohomology/pushforward-pullback-and-finite-morphisms) provide the geometric stalk and finite-pushforward comparisons. Frobenius morphisms and their action on cohomology, §§1–3, proves topological invariance and the relative-Frobenius equivalence used in §2.

The construction is coefficient-linear. For a noncommutative ring it is performed in left-module sheaves; the adjunction, restrictions of supports and stalk base-change maps still make sense. Lesson 4, Lemma 4.1a, proves that forgetting coefficients computes the same underlying cohomology through the pointwise flasque resolution. Its Lemma 4.2b supplies finite constructible flat generators and their lifting property for left Noetherian rings. Thus no commutativity, finite underlying set or assumption of finite monodromy is hidden in the relative argument below.

The coefficient projection formula for \(R\Gamma_c\), arbitrary-dimensional perfectness with this full torsion-ring scope, and filtered trace additivity are Lesson 4, Theorems 3.1,4.3–4.4. The trace formula in dimension at most one, including these left Noetherian noncommutative coefficients, is Lesson 6, Theorem 1.1. Smooth trace and duality needed for the examples are proved in Smooth traces, duality and Gysin maps, §§10,13–14. The general constructibility premise just identified remains an explicit foundation; reading its source is not a new proof of that premise.

## 2. Frobenius and direct image with proper support

Let \(f_0:X_0\to Y_0\). Denote the geometric scheme Frobenius maps by \(F_X,F_Y\), and the descended coefficient isomorphism of \(K\) by

\[
c_X:F_X^{-1}K\xrightarrow{\sim}K.
\]

It is the coefficient correspondence of Lesson 3, rather than an arbitrary choice of an isomorphism.

**Lemma 2.1 (Frobenius compatibility).** The coefficient correspondence on the geometric pullback of \(Rf_{0!}K_0\) is the map induced by \(c_X\) under compact-support base change. Consequently

\[
R\Gamma_c(Y,Rf_!K)\simeq R\Gamma_c(X,K)
\tag{2.1}
\]

intertwines Frobenius. At \(y\in Y_0(k_0)\), the base-change isomorphism

\[
(Rf_!K)_{\bar y}\simeq
R\Gamma_c(X_{\bar y},K|_{X_{\bar y}})
\tag{2.2}
\]

intertwines local geometric Frobenius with the Frobenius correspondence of the fibre over \(y\). The construction also commutes with proper base change.

**Proof.** The commuting square with horizontal maps \(F_X,F_Y\) is generally not cartesian. Instead form

\[
X'=Y\times_{F_Y,Y,f}X,\qquad
a:X'\to X,\quad f':X'\to Y,
\]

and the map

\[
h:X\longrightarrow X',\qquad
ah=F_X,\quad f'h=f.
\tag{2.3}
\]

Before geometric base change, \(h\) is the relative \(q\)-Frobenius of \(f_0\). It is a finite universal homeomorphism. Indeed the relative \(p\)-Frobenius is a universal homeomorphism, [Stacks, Tag 0CCB](https://stacks.math.columbia.edu/tag/0CCB); its iterates have the same property. Locally, if \(B\) is generated over \(A\) by \(x_1,\ldots,x_s\), the relative \(q\)-Frobenius ring map is

\[
B\otimes_{A,F_A^r}A\longrightarrow B,\qquad
b\otimes a\longmapsto b^qa.
\]

Every generator \(x_i\) satisfies a monic equation \(T^q-x_i^q=0\) over the image, so this map is finite. Both properties persist under base change to \(k\).

Étale topological invariance makes \(h^{-1}\) an exact equivalence with inverse \(h_*\). Since \(h\) is finite, \(Rh_!=h_*\). Apply base change to the cartesian square defining \(X'\), then this equivalence and support composition:

\[
\begin{aligned}
F_Y^{-1}Rf_!K
&\xrightarrow{\sim}Rf'_!a^{-1}K\\
&\xrightarrow{\sim}Rf'_!Rh_!h^{-1}a^{-1}K\\
&\xrightarrow{\sim}Rf_!F_X^{-1}K.
\end{aligned}
\tag{2.4}
\]

The middle map is the inverse of the adjunction counit, which is an isomorphism for the equivalence. Composing (2.4) with \(Rf_!c_X\) gives the induced correspondence.

We check that it is the descended correspondence, including its direction. Compactification and base-change comparisons commute with field automorphisms. This follows directly on the open part from the stalk description of \(j_!\), and on the proper part from the natural proper base-change map. That map is built from the pullback/direct-image adjunction; the unit and counit are natural transformations, so their squares with a field automorphism commute. The derived maps retain this naturality on resolutions. Independence of compactification preserves the comparison after a common proper refinement.

The absolute-Frobenius comparison used in Lesson 3 is natural here as well. On an étale chart \(W\) it is restriction along the inverse of the relative-Frobenius isomorphism of \(W\). Its compatibility with compositions and base change is an equality of maps of charts, hence of restrictions. Every sheaf is a colimit of such represented charts, and the resulting inverse-image comparisons are exact. It follows that (2.4), when combined with the arithmetic field map \(\sigma:c\mapsto c^q\), has precisely the absolute-Frobenius coefficient map. That map is naturally the identity on the étale topos, as proved in Lesson 3. Thus the composite is the identity, and the induced operator is the inverse arithmetic operator \(\rho(\sigma)^{-1}\), the required geometric Frobenius. This also checks that no inverse was lost in (2.4).

For (2.1), support composition applied to \(X\to Y\to\operatorname{Spec}k\) is natural for all the maps in (2.4). Equivalently, compute it as \(R\bar f_*j_!\) on a compactification defined over \(k_0\); both its open and proper comparisons commute with \(\sigma\), and therefore with \(\sigma^{-1}\). This proves the Frobenius assertion for the total cohomology.

For (2.2), base change along \(\bar y\to Y\) gives the asserted fibre complex. When \(y\) is rational, its fibre is the base change of \(X_{0,y}/k_0\). The arithmetic field map fixes \(y\), and the proper base-change and extension-by-zero maps used to construct (2.2) commute with it by the same naturality. Taking inverses identifies its local geometric action with that on the fibre. For a degree-\(d\) point the identical argument uses \(\sigma^d\) and the fibre over \(\mathbf F_{q^d}\).

Finally a further proper base change gives a stacked diagram of cartesian squares. Their base-change maps are obtained by composing the same adjunction transformations; the base-change and support-composition compatibilities identify the two compositions. Both are natural for \(\sigma\). Hence (2.4), (2.1) and (2.2) commute with that proper base change. \(\square\)

## 3. Why the induction keeps the right coefficients

**Lemma 3.1 (constructibility and finite Tor amplitude).** Let \(f:X\to Y\) be separated and of finite type over \(k\), let \(\dim X\leq d\), and let \(K\in D_{\mathrm{ctf}}(X,\Lambda)\) have Tor amplitude \([a,b]\). Then \(Rf_!K\in D_{\mathrm{ctf}}(Y,\Lambda)\). Its Tor amplitude is contained in \([a,b+2d]\). If all geometric fibres have dimension at most \(c\), use \([a,b+2c]\) instead. The assertion holds equally over \(k_0\), by checking geometric stalks over their algebraically closed residue fields.

**Proof.** We first prove constructibility for the larger coefficient rings, using only the finite central coefficient foundation in §1. Set \(A=\mathbf Z/n\). For an affine separated étale map \(a:U\to X\) of finite presentation put \(P_U=a_!\underline\Lambda\) and \(B_U=R(fa)_!\underline A\). Finite \(A\)-coefficient constructibility and the geometric stalk formula give bounded constructible cohomology for \(B_U\). At every stalk, Lesson 4's projection formula puts its Tor amplitude in \([0,2d]\). Thus \(B_U\in D_{\mathrm{ctf}}(Y,A)\).

By Lesson 4, Lemma 4.2b, represent \(B_U\) by a bounded constructible flat \(A\)-complex. Simultaneously stratify its finitely many terms. On each stratum they are finite locally constant projective \(A\)-modules; after a common finite étale trivialization the finitely many differentials are constant too. Tensoring this model with \(\Lambda\) therefore has constructible \(\Lambda\)-cohomology: kernels and cokernels of maps of finite modules are finite by left Noetherianity. The canonical scalar-extension comparison is an isomorphism

\[
R f_!P_U=R(fa)_!\underline\Lambda
\simeq\Lambda\otimes_A^{\mathbf L} B_U.
\tag{3.1a}
\]

Here the tensor retains the left \(\Lambda\)-action. On a geometric stalk it is exactly the absolute projection formula of Lesson 4 for \(U_{\bar y}\); proper-support base change identifies both stalks, so the comparison is an isomorphism of sheaf complexes. This also proves that it is the natural comparison, rather than a separately chosen model.

Resolve \(K\) by a bounded-above complex \(P^v\) of finite sums of the \(P_U\), as in Lesson 4, Lemma 4.2b. The term spectral sequence is

\[
E_1^{v,u}=R^u f_!P^v\Longrightarrow
\mathcal H^{v+u}(Rf_!K),\qquad 0\leq u\leq2d.
\tag{3.1b}
\]

It converges with a finite filtration in each output degree. To justify this with an unbounded left resolution, retain the terms in degrees \(\geq m\); the omitted quotient lies in degrees \(\leq m-1\). The uniform relative bound puts its direct image in degrees \(\leq m-1+2d\). For a fixed output degree, the two adjacent groups in the truncation triangle vanish when \(m\) is sufficiently negative. The finite spectral sequences therefore stabilize. Only \(v=i-2d,\ldots,i\) can contribute to total degree \(i\), and the strip bounds the lengths of its nonzero differentials. All entries are constructible by (3.1a); their subquotients and extensions are constructible over a left Noetherian ring, by Lesson 4, Lemma 4.2b. This proves constructibility without forgetting an infinite \(\Lambda\)-module to a falsely finite abelian sheaf.

The stalk formula and the bounded cohomology spectral sequence now show boundedness. To prove the Tor assertion, fix \(\bar y\) and an arbitrary right \(\Lambda\)-module \(N\). Exactness of geometric inverse image, (2.2), and Lesson 4's coefficient projection formula give

\[
\begin{aligned}
\bigl(N\otimes_\Lambda^{\mathbf L}Rf_!K\bigr)_{\bar y}
&\simeq N\otimes_\Lambda^{\mathbf L}
R\Gamma_c(X_{\bar y},K_{\bar y})\\
&\simeq R\Gamma_c
\bigl(X_{\bar y},N\otimes_\Lambda^{\mathbf L}K_{\bar y}\bigr).
\end{aligned}
\tag{3.1}
\]

The sheaf cohomology of the coefficient complex on the last line is zero outside \([a,b]\). Its hypercohomology spectral sequence has terms

\[
H_c^u\bigl(X_{\bar y},
\mathcal H^v(N\otimes_\Lambda^{\mathbf L}K_{\bar y})\bigr),
\qquad 0\leq u\leq2\dim X_{\bar y},\quad a\leq v\leq b.
\]

It is bounded, so its abutment is zero outside \([a,b+2\dim X_{\bar y}]\). No finiteness assumption on \(N\) is used; the torsion dimension bound applies to these sheaves. The same interval \([a,b+2d]\), or \([a,b+2c]\), works for every stalk and \(N\). For a right module sheaf, apply the argument to its stalk \(N_{\bar y}\). This is exactly finite Tor amplitude of \(Rf_!K\). \(\square\)

**Lemma 3.2 (a projection with curve fibres).** A nonempty affine \(X_0/k_0\) of dimension \(d\geq2\) admits a separated finite-type map

\[
f_0:X_0\longrightarrow\mathbf A^{d-1}_{k_0}
\tag{3.2}
\]

whose geometric fibres have dimension at most one.

**Proof.** We give the finite-field normalization argument. Let \(B\ne0\) be the coordinate algebra, generated by \(x_1,\ldots,x_s\). If these generators are algebraically independent, \(B\) is a polynomial ring and we are done. Otherwise choose a nonzero polynomial relation \(P(x_1,\ldots,x_s)=0\). Choose an integer \(M\) larger than every exponent in its monomials. Set

\[
y_i=x_i-x_s^{M^i}\quad(1\leq i<s).
\tag{3.3}
\]

Substitute \(X_i=Y_i+T^{M^i}\) and \(X_s=T\) in \(P\). The highest \(T\)-degree of a monomial with exponent vector \((a_1,\ldots,a_s)\) is \(a_s+\sum_{i<s}a_iM^i\). Base-\(M\) uniqueness makes these degrees distinct. The greatest one consequently has a nonzero constant leading coefficient; all other terms in its binomial expansion have smaller degree. Dividing by that field coefficient gives a monic equation for \(x_s\) over \(B'=k_0[y_1,\ldots,y_{s-1}]\). Thus \(B=B'[x_s]\) is finite over \(B'\). Repeat with its smaller generating set. This process terminates at an embedded polynomial algebra \(k_0[z_1,\ldots,z_t]\) over which \(B\) is finite. It uses no choice of a generic field-valued linear projection, so works over the finite field and for nilpotents and multiple components.

For clarity, a finite integral inclusion preserves dimension. Primes lie over primes after localization and taking a maximal ideal of the nonzero integral algebra over the residue field; contractions of those maximal ideals are the residue-field zero prime. The same argument after quotienting by a prime gives going up. Two comparable primes over one prime must coincide: after localization and quotient by the smaller prime, the remaining algebra is integral over a field and has only maximal primes. Chains upstairs and downstairs therefore have the same possible maximal length. Hence \(t=\dim B=d\), and the inclusion gives the finite map \(n_0:X_0\to\mathbf A^d_{k_0}\).

Compose it with projection onto the first \(d-1\) coordinates. On any geometric fibre its base change is finite over \(\mathbf A^1\). Its coordinate algebra is integral over a quotient of the line's coordinate algebra; the same incomparability argument bounds its dimension by one. The composite is separated and of finite type. \(\square\)

It is not necessary that \(f_0\) be smooth, that every fibre be a curve, or that \(X_0\) be normal. The curve theorem already allows all its singular and zero-dimensional fibres.

## 4. The finite-coefficient theorem

**Theorem 4.1 (Grothendieck–Lefschetz, torsion coefficients).** Let \(X_0/k_0\) be separated and of finite type, let \(\Lambda\) have the full left Noetherian torsion scope of §1, and let \(K_0\in D_{\mathrm{ctf}}(X_0,\Lambda)\). Then \(R\Gamma_c(X,K)\) is perfect over \(\Lambda\), and

\[
\operatorname{Tr}_\Lambda(F_X^*;R\Gamma_c(X,K))
=\sum_{x\in X_0(k_0)}
\operatorname{Tr}_\Lambda(F_x;K_{\bar x})
\quad\text{in }\Lambda^\natural.
\tag{4.1}
\]

**Proof.** Perfectness, including noncommutative infinite coefficient rings, was proved in Lesson 4, Theorems 4.3–4.4, in arbitrary dimension. We prove the equality by induction on \(d=\dim X_0\). The empty scheme has two zero quantities. For \(d\leq1\) use Lesson 6, Theorem 1.1.

To reduce to affines without assuming a dimension drop, choose a finite affine open cover \(U_1,\ldots,U_m\). Put

\[
S_i=U_i\cap\left(X_0-\bigcup_{j<i}U_j\right).
\tag{4.2}
\]

Each \(S_i\) is closed in the affine \(U_i\), hence affine. It is open in the closed remainder after removing \(U_1,\ldots,U_{i-1}\). Repeated open–closed additivity of Lesson 6 therefore expresses each side of (4.1) as the sum of its values on the restrictions to the \(S_i\). The restriction has finite Tor amplitude and constructible cohomology. This finite stratification covers \(X_0\), even if several strata have dimension \(d\).

It remains to prove the formula for an affine stratum of dimension \(d\geq2\). Choose (3.2) and write \(Y_0=\mathbf A^{d-1}_{k_0}\). By Lemma 3.1,

\[
L_0=Rf_{0!}K_0\in D_{\mathrm{ctf}}(Y_0,\Lambda).
\]

The induction hypothesis applies to \(L_0\) on \(Y_0\). Lemma 2.1 and that hypothesis give

\[
\begin{aligned}
\operatorname{Tr}_\Lambda(F_X^*;R\Gamma_c(X,K))
&=\operatorname{Tr}_\Lambda(F_Y^*;R\Gamma_c(Y,L))\\
&=\sum_{y\in Y_0(k_0)}
\operatorname{Tr}_\Lambda(F_y;L_{\bar y})\\
&=\sum_{y\in Y_0(k_0)}
\operatorname{Tr}_\Lambda
\bigl(F_{X_y}^*;R\Gamma_c(X_{\bar y},K_{\bar y})\bigr).
\end{aligned}
\tag{4.3}
\]

For every rational \(y\), \(X_{0,y}\) is a separated finite-type \(k_0\)-scheme of dimension at most one; its coefficient restriction is in \(D_{\mathrm{ctf}}\). The curve theorem changes its term on the last line to

\[
\sum_{x\in X_{0,y}(k_0)}
\operatorname{Tr}_\Lambda(F_x;K_{\bar x}).
\]

Every rational point of \(X_0\) lies over a unique rational point of \(Y_0\), so these finite sums together are the right side of (4.1). This completes the affine case and, using (4.2), the induction. \(\square\)

This proves the step abbreviated in [Stacks, Tag 03V3](https://stacks.math.columbia.edu/tag/03V3). The proof needs compact-support base change, the operator compatibility and preservation of finite Tor amplitude, in addition to the known curve case.

## 5. From finite coefficients to adic coefficients

Let \(O\) be the ring of integers in a finite extension \(E/\mathbf Q_\ell\), let \(\varpi\) be a uniformizer, and put \(O_n=O/\varpi^n\), with \(\ell\ne p\). This includes \(O=\mathbf Z_\ell\) and \(E=\mathbf Q_\ell\). Adic sheaves and their rationalizations have the meanings of Lesson 1.

**Theorem 5.1 (adic trace formula).** If \(\mathcal F_0\) is a constructible \(E\)-sheaf on \(X_0\), then

\[
\dim_EH_c^i(X,\mathcal F)<\infty,\qquad
H_c^i(X,\mathcal F)=0\quad(i<0\text{ or }i>2\dim X),
\tag{5.1}
\]

and

\[
\sum_{x\in X_0(k_0)}
\operatorname{Tr}_E(F_x;\mathcal F_{\bar x})
=\sum_i(-1)^i
\operatorname{Tr}_E(F_X^*;H_c^i(X,\mathcal F)).
\tag{5.2}
\]

For a constructible \(O\)-sheaf \(\mathcal L_0\), including one with torsion, \(R\Gamma_c(X,\mathcal L)\) and its finite stalks are perfect over \(O\), and the same formula holds in \(O\), with perfect-complex traces.

**Proof for a torsion-free lattice.** Choose a constructible adic model of \(\mathcal F_0\), and quotient it by its torsion subobject. Lesson 1, Corollary 3.3, proves that this torsion is killed by a uniform power of \(\varpi\), and that the quotient is an adic sheaf with torsion-free finite stalks. It still rationalizes to \(\mathcal F_0\). Denote it by \(\mathcal L_0\). Its normalized finite levels \(\mathcal L_{0,n}\) have finite free stalks over \(O_n\), and

\[
\mathcal L_{0,n+1}\otimes_{O_{n+1}}^{\mathbf L}O_n
\simeq\mathcal L_{0,n}.
\tag{5.3}
\]

Flatness makes this derived reduction the ordinary strict reduction. Put

\[
C_n=R\Gamma_c(X,\mathcal L_n).
\]

Theorem 4.1 and coefficient projection give perfect \(O_n\)-complexes and isomorphisms

\[
C_{n+1}\otimes_{O_{n+1}}^{\mathbf L}O_n\simeq C_n
\tag{5.4}
\]

compatible with Frobenius. The compatibility follows from naturality of coefficient extension and the operator maps; it does not require a choice of resolutions commuting strictly at the outset.

Lesson 1, Theorem 6.1, produces a bounded finite free \(O\)-complex \(C\) and a chain endomorphism \(F_C\) realizing these reductions and their Frobenius maps. Its proof uses minimal free complexes to force common term ranks and a common finite degree range, then lifts the compatibility homotopies to make the endomorphisms commute under reduction. Replacing \(\ell\) by \(\varpi\) gives the identical argument over this complete discrete valuation ring. Finite residue rings give the same Mittag–Leffler argument. Thus

\[
H^i(C)=\varprojlim_nH^i(C_n)=H_c^i(X,\mathcal L).
\tag{5.5}
\]

Each finite-level group is zero outside \([0,2\dim X]\), so (5.5) has the same vanishing. Its cohomology is finite over \(O\), since \(C\) has finite free terms. Tensoring with \(E\) proves (5.1).

Write \(t=\operatorname{Tr}_O(F_C;C)\). Termwise matrix traces reduce to those of \(C_n\). The finite-ring theorem says for every \(n\)

\[
t\bmod\varpi^n
=\sum_{x\in X_0(k_0)}
\operatorname{Tr}_{O_n}
(F_x;(\mathcal L_n)_{\bar x}).
\tag{5.6}
\]

The rational point set is finite. Its stalk operators are reductions of the operators on the finite free \(O\)-stalks \(\mathcal L_{\bar x}\), so the right sides of (5.6) are reductions of their integral trace sum. Since \(O\) is separated for its \(\varpi\)-adic topology, equality at every level implies

\[
t=\sum_{x\in X_0(k_0)}
\operatorname{Tr}_O(F_x;\mathcal L_{\bar x}).
\tag{5.7}
\]

Over the field \(E\), the trace of \(C\otimes_OE\) is the alternating trace on its cohomology, by Lesson 4, (2.4). This is the right side of (5.2), proving that formula and the torsion-free integral case.

The proof also shows lattice independence: two integral models have the same rationalized sheaf, hence the same rationalized cohomology by Lesson 1, Theorem 7.2. All comparisons are natural for Frobenius. One may also place two lattices inside a common lattice after multiplying by a power of \(\varpi\); the intervening quotients are uniformly torsion and disappear after tensoring with \(E\).

**The integral case with torsion.** For a general \(\mathcal L_0\), use its exact sequence

\[
0\longrightarrow\mathcal T_0
\longrightarrow\mathcal L_0
\longrightarrow\mathcal L_{0,\mathrm{free}}
\longrightarrow0,
\tag{5.8}
\]

where \(\varpi^a\mathcal T_0=0\) for some \(a\), and the quotient has torsion-free stalks. Lesson 1's finite-cohomology and localization arguments show that all three objects have bounded finite \(O\)-cohomology with compact support. A finite module over the discrete valuation ring \(O\) has a finite free resolution of length at most one. Resolving the finitely many cohomology modules, or applying the perfectness criterion of Lesson 1, Lemma 5.1, shows that their compact-support complexes and stalks are perfect over \(O\).

Every endomorphism of a perfect \(O\)-complex with torsion cohomology has trace zero: after tensoring with \(E\) the complex is acyclic, so its trace is zero in \(E\), and \(O\hookrightarrow E\) is injective. This applies to \(R\Gamma_c(X,\mathcal T)\) and to each \(\mathcal T_{\bar x}\). Sequence (5.8) supplies an actual Frobenius-preserved filtration. Filtered trace additivity shows that both sides for \(\mathcal L_0\) equal those for its torsion-free quotient. Formula (5.7) for that quotient proves the integral assertion. \(\square\)

For a torsion model, ordinary finite levels need not be flat over \(O_n\). For example \(O/\varpi\) is not perfect as an \(O_n\)-module when \(n>1\). One must not apply Theorem 4.1 to those levels without checking \(D_{\mathrm{ctf}}\). The preceding proof uses the torsion-free quotient and a perfect \(O\)-trace for the torsion part. Equivalently, a derived reduction of the perfect complex \([O\xrightarrow{\varpi}O]\) uses the two-term free complex \([O_n\xrightarrow{\varpi}O_n]\); both terms are necessary.

The same proof applies to bounded constructible adic complexes supplied with compatible perfect finite-level models: use their finite-level complex trace formula and the compatible-perfect-complex theorem. For an ordinary sheaf, the interval (5.1) is \([0,2d]\); for a complex it shifts according to its coefficient cohomological degrees.

### Complete local coefficient rings

The modern constructible category is larger than classical flat sheaves. We make its trace statement precise. Let \((A,\mathfrak m)\) be a commutative complete Noetherian local ring with finite residue field \(\kappa\) of characteristic \(\ell\ne p\), and put \(A_n=A/\mathfrak m^n\). In Lesson 2, §6, \(D_{\mathrm{cons}}(X_0,\widehat A)\) consists of derived \(\mathfrak m\)-complete pro-étale complexes whose derived residue-field reduction is a bounded constructible finite-Tor étale complex. Its completed pullback to a geometric point is the derived limit of its finite reductions. A finite ordinary stalk need not itself belong to this category when \(A\) is singular.

**Theorem 5.2.** For \(K_0\) in this category, define the completed compact-support complex by

\[
C=R\varprojlim_n R\Gamma_c(X,K_n),\qquad
K_n=K\otimes_A^{\mathbf L}A_n.
\tag{5.9}
\]

Then \(C\) and each completed geometric stalk \(K_{\bar x}\) are perfect over \(A\). The Frobenius correspondence gives

\[
\operatorname{Tr}_A(F_X^*;C)
=\sum_{x\in X_0(k_0)}\operatorname{Tr}_A(F_x;K_{\bar x})
\quad\text{in }A.
\tag{5.10}
\]

If the residue-field reduction has Tor amplitude \([a,b]\), \(C\) has Tor amplitude \([a,b+2\dim X]\). No assumption that the rings \(A_n\) are perfect as \(A\)-modules is required. The completed \(Rf_!K\) preserves this constructible category and commutes with arbitrary completed base change for separated finite-type \(f\) between the schemes in §1.

**Proof.** Each \(A_n\) is finite: its successive \(\mathfrak m\)-power layers are finite-dimensional over the finite field \(\kappa\), by Noetherianity. Also \(\ell^n A_n=0\). Filtering any \(A_n\)-module by its \(\mathfrak m\)-powers and using associativity of derived tensor on the \(\kappa\)-module layers gives the common Tor interval \([a,b]\) for every \(K_n\). The coefficient filtration has finite \(\kappa\)-module layers; its triangles and the constructible Serre-category property give bounded constructible cohomology for every \(K_n\). These are the explicit reduction arguments in Lesson 2, §6.

Put \(C_n=R\Gamma_c(X,K_n)\). Theorem 4.1 makes \(C_n\) perfect and gives its trace formula. Scalar extension, with its coefficient-ring action retained, gives

\[
C_{n+1}\otimes_{A_{n+1}}^{\mathbf L}A_n\simeq C_n.
\tag{5.11}
\]

The maps commute with Frobenius by §2 and the natural projection maps. Lesson 4 gives their common Tor interval \([a,b+2\dim X]\).

Here is the compatible-perfect-complex argument for these coefficient rings. Over the local Artinian ring \(A_n\), choose a bounded finite free model \(P_n\) for \(C_n\). When a differential has a unit entry, elementary row and column operations split off a contractible rank-one pair. Removing such pairs leaves a minimal complex: every differential entry is in \(\mathfrak m A_n\). A homotopy equivalence between minimal complexes is a degreewise isomorphism, because after reduction to \(\kappa\) both differentials and homotopies are zero; its two maps are inverse degreewise there, and a square matrix invertible modulo the maximal ideal is invertible over the local ring. Derived isomorphisms of bounded projective complexes are such homotopy equivalences. Hence (5.11) is represented by a degreewise isomorphism \(P_{n+1}/\mathfrak m^n\simeq P_n\). All ranks and the finite degree range are those of \(P_1\). Its nonzero degrees lie in the stated Tor interval, since minimal reduction has zero differential.

Lift compatible bases successively. The transition maps become coordinate reduction, so

\[
P=\varprojlim_nP_n
\]

is a bounded finite free \(A\)-complex, and \(P/\mathfrak m^nP=P_n\). Represent Frobenius by chain maps \(u_n\). Having chosen \(u_n\), choose any representative \(v_{n+1}\) of the next derived operator. Compatibility says

\[
u_n-(v_{n+1}\bmod\mathfrak m^n)=dh+hd.
\tag{5.11a}
\]

Lift every matrix entry of \(h\) to level \(n+1\) and set \(u_{n+1}=v_{n+1}+d\widetilde h+\widetilde h d\). This changes no derived operator and makes the square commute strictly, with precisely the sign in (5.11a). Induction gives a chain map \(u:P\to P\).

The term towers are onto, and their cycles, boundaries and cohomology at each level are finite groups. These towers are Mittag–Leffler. The product description of derived limit, or the finite-system exactness proof of Lesson 1, Theorem 6.1, therefore gives

\[
R\varprojlim C_n\simeq P,
\qquad H^i(P)=\varprojlim H^i(C_n).
\tag{5.12}
\]

Indeed \(1-\mathrm{shift}\) is onto on the term products by successive lifting; its resulting cohomology sequence has kernel \(\varprojlim H^i\) and cokernel \(\varprojlim{}^1H^{i-1}=0\). This proves (5.12), perfectness and the Tor bound. The identical argument for the compatible perfect stalk complexes proves stalk perfectness and lifts their operators.

Termwise matrix trace reduces to the perfect trace of every \(C_n\) and every stalk reduction. The finite-level trace formula therefore reduces (5.10) to zero modulo every \(\mathfrak m^n\). The rational point set is finite, so the local trace sum reduces termwise. Completeness includes separation, \(A=\varprojlim A_n\), and proves (5.10).

Finally Lemma 3.1 puts \(Rf_!K_n\) in \(D_{\mathrm{ctf}}(Y,A_n)\) with common interval \([a,b+2c]\) for a fibre bound \(c\). Scalar extension gives a coherent compatible system. Lesson 2, §6, reconstructs its derived complete constructible object and proves that it is the compactification-defined completed \(Rf_!\); its reduction is exactly \(Rf_!K_n\). Finite-level arbitrary base change from §1 commutes with these scalar maps and all iterated base changes. Taking the coherent derived limit gives the completed base-change map and its isomorphism, with the same Frobenius compatibility. \(\square\)

For example \(A=\mathbf Z_\ell[\epsilon]/(\epsilon^2)\), with \(\mathfrak m=(\ell,\epsilon)\), is permitted. Its residue field has infinite projective dimension over \(A\), as shown in Lesson 2, §6. Nevertheless constant \(\widehat A\) has a free coefficient model and satisfies (5.10). On \(\mathbf A^2\), its compact complex is \(A(-2)[-4]\), obtained by the compatible finite-level affine-space calculation, and its trace is \(q^2\in A\). This illustrates why the theorem requires derived constructible coefficients rather than perfection of the quotient rings. It also explains why an alternating trace on arbitrary nonprojective \(A\)-cohomology modules cannot replace the perfect-complex trace.

**Corollary 5.3 (local rational lattices).** Let \(E/\mathbf Q_\ell\) be finite with \(\ell\ne p\), and let \(K_0\) be a bounded constructible pro-étale \(\widehat E\)-complex: on finitely many locally closed strata its cohomology sheaves are finite-rank \(E\)-local systems in the sense of Lesson 2, §7. Its compact-support cohomology is finite-dimensional, and the trace formula holds with the alternating cohomology trace in \(E\). A global integral lattice on \(X_0\) is unnecessary.

**Proof.** Refine the finitely many coefficient strata to smooth connected locally closed \(k_0\)-schemes. Such a finite refinement exists: over the perfect field \(k_0\), each reduced irreducible component has a dense smooth open; first remove its intersections with other components, then repeat on the closed complement. Dimension drops at every repetition. Nilpotents do not change the sites.

Each smooth connected stratum is geometrically unibranch. Lesson 2, Corollary 7.11, identifies its pro-étale local-system representation with a representation of its profinite étale fundamental group and supplies a global integral lattice. Explicitly the continuous image in \(\mathrm{GL}_r(E)\) is compact, so the orbit of a chosen basis lattice is bounded. The sum of its translates lies between that lattice and a fixed multiple \(\varpi^{-a}O^r\); it is a finite \(O\)-module, is torsion-free, spans \(E^r\), and is invariant. This gives the required lattice on the stratum.

Theorem 5.1 proves the finite-dimensional compact-support and trace assertions for each of these cohomology local systems. Their finite truncation filtration proves the assertion for the restricted complex, with the degree signs. Arrange the strata as successive opens in closed remainders; the preceding dimension induction constructs such an ordering. Repeated compact-support localization gives bounded finite cohomology for \(K\) and the global trace as the sum of the stratum traces. The actual support and truncation filtrations are Frobenius-preserved, so their trace additivity also sums the local stalk traces. This is the desired formula. It concerns the usual completed compact-support operation with its localization maps from Lesson 2; it does not identify \(\widehat E\) with the discrete constant \(E\)-sheaf. \(\square\)

Lesson 2's nodal example shows that a rational local system may lack a global lattice on a singular scheme. Corollary 5.3 handles it by strata.

**Corollary 5.4 (algebraic rational coefficients).** The conclusion of Corollary 5.3 also holds for an algebraic extension \(L/\mathbf Q_\ell\), including \(\overline{\mathbf Q}_\ell\), with the final coefficient topology of Lesson 2. Constructible means bounded cohomology which, on finitely many locally closed strata, consists of finite-rank local systems over the coefficient sheaf \(L_X\) of that lesson.

**Proof.** Use the smooth finite stratification of Corollary 5.3. Each stratum is quasi-compact and quasi-separated. Lesson 2, Proposition 7.12, therefore descends each of its finitely many cohomology local systems to a finite subextension of \(L\). Enlarge these finitely many fields to one finite extension \(E\subset L\). On a stratum each local system is then the scalar extension of an \(E\)-local system with a global integral lattice. Theorem 5.1 gives its bounded finite-dimensional compact-support complex.

The coefficient sheaf \(L_X\) is the filtered colimit of the finite-extension coefficient sheaves: on a quasi-compact w-contractible object this follows from the finite-stage property for continuous functions on its compact component space, proved in Lesson 2, Lemma 7.6f. Here is the compact-support comparison with this colimit. Choose a proper compactification of the stratum. The qcqs pro-étale basis has finite covering refinements, so filtered colimits of sheaves are evaluated sectionwise on its qcqs objects. Construct an affine w-contractible hypercover of the compactification with finitely many pieces in each degree: every matching object is qcqs, and Lesson 2's affine-cover theorem supplies finitely many such pieces. Its augmented free sheaf chain complex is exact. Indeed a finite chain cycle can be filled locally, degree by degree, by lifting the finitely many matching simplices along the covering maps. Apply Hom into an injective resolution; the first-quadrant double-complex comparison then gives the usual hypercover cohomology spectral sequence. Sections on the w-contractible pieces are exact by Lesson 2, §2, so its positive vertical rows vanish. The hypercover cochains therefore compute derived sections of the extension-by-zero sheaf.

Filtered colimits commute with those cochains and their cohomology. For any finite extension \(E'/E\), tensor with \(E'\) is a finite direct sum after choosing a basis, so compact-support coefficient extension commutes with it. Pass to the filtered colimit over these \(E'\). Open extension by zero commutes with that extension, as is checked on its open part and its zero boundary stalks. The resulting compact-support complex is the finite \(E\)-cohomology complex tensored with \(L\). Its \(L\)-cohomology is finite-dimensional, and its alternating trace is the image of its \(E\)-trace. The same extension applies to every local stalk operator.

Apply the finite truncation and support filtrations from Corollary 5.3. Their Frobenius-preserved graded pieces have the trace formula just proved, so additivity proves it for \(K\). This argument does not require the extension maps of the entire complex to descend to \(E\), or a global integral lattice on the singular scheme. The topology is the stated final topology, with its finite-stage compactness; the assertion makes no replacement by a discrete constant coefficient sheaf. \(\square\)

## 6. All powers and two families of examples

Apply Theorems 4.1 and 5.1 to \(X_0\times_{k_0}\mathbf F_{q^r}\). Its geometric space is \(X\), and its Frobenius is \(F_X^r\), with the iterated coefficient map. Thus

\[
\sum_{x\in X_0(\mathbf F_{q^r})}
\operatorname{Tr}(F_X^{r*};K_x)
=\operatorname{Tr}(F_X^{r*};R\Gamma_c(X,K)).
\tag{6.1}
\]

Use the alternating cohomology trace on the right for \(E\)-coefficients. For a closed point of degree \(d\mid r\), the contribution is \(d\operatorname{Tr}(F_x^{r/d};K_{\bar x})\). The \(d\) geometric points have conjugate operators, as proved in Lesson 3. This explains the exponent and multiplicity in the later Euler product.

**Affine space.** The compact-support Künneth formula and
\(R\Gamma_c(\mathbf A^1,E)=E(-1)[-2]\) give

\[
R\Gamma_c(\mathbf A^n,E)=E(-n)[-2n].
\tag{6.2}
\]

Geometric Frobenius acts on \(E(-n)\) by \(q^n\), so (6.1) reads
\(\#\mathbf A^n(\mathbf F_{q^r})=q^{rn}\). This includes \(n=0\).

**Grassmannians and flag varieties.** Here are the cell geometry and counts. Write \(F_j=\langle e_1,\ldots,e_j\rangle\) in \(k_0^n\). An \(m\)-plane has jump positions \(J=(j_1<\cdots<j_m)\) for \(\dim(V\cap F_j)\). It has a unique ordered echelon basis

\[
v_i=e_{j_i}+\sum_{\substack{a<j_i\\ a\notin\{j_1,\ldots,j_m\}}}c_{ia}e_a.
\tag{6.2a}
\]

To obtain it, choose in \(V\cap F_{j_i}\) a vector with coefficient one at \(e_{j_i}\), and subtract the earlier basis vectors to kill their pivot entries. The remaining coefficients are unrestricted; two such normalized bases differ by a triangular combination whose pivot entries force every coefficient to be zero. There are \(j_i-i\) free entries in row \(i\), so these planes form a cell \(\mathbf A^{a_J}\), where \(a_J=\sum_i(j_i-i)\). On the Grassmannian pivot chart this construction and its inverse are polynomial: the pivot submatrix is the identity, and the plane is the row span of the displayed matrix. Thus it is an isomorphism of schemes, defined over \(k_0\), rather than only a bijection of points.

The inequalities \(\dim(V\cap F_{j_i})\geq i\) are closed determinantal conditions. Their common locus is exactly the union of cells with pivots \(t_i\leq j_i\): the echelon basis reads off those dimensions. Any downward-closed set of pivot tuples is a finite union of these closed loci, one for each of its maximal tuples. A linear ordering extending componentwise order consequently gives a closed filtration whose successive open pieces are precisely the cells. Localization and (6.2) now prove that cohomology is zero in odd degrees and that

\[
\dim_EH^{2i}(\operatorname{Gr}(m,n)_k,E)=b_{2i},
\quad
\det(T-F^*;H^{2i})=(T-q^i)^{b_{2i}},
\tag{6.3}
\]

where \(b_{2i}\) is the number of cells of dimension \(i\). To see the induction, a cell has compact-support cohomology only in its even degree \(2a\). In the localization long exact sequence, the odd groups on both sides vanish; the even groups are short exact extensions of the previous groups by this single Tate module. The sequence is Frobenius-equivariant, so characteristic polynomials multiply. Properness identifies compact-support and ordinary cohomology. This argument determines traces without assuming that the extensions split as Frobenius representations; their semisimplifications are \(E(-i)^{b_{2i}}\).

Formula (6.1) therefore gives

\[
\#\operatorname{Gr}(m,n)(\mathbf F_{q^r})
=\sum_i b_{2i}q^{ri}
=\binom{n}{m}_{q^r},
\tag{6.4}
\]

where the polynomial is also obtained directly by counting each affine cell. To identify the last notation independently, put \(Q=q^r\) and \(C_{m,n}(Q)=\sum_JQ^{a_J}\). Splitting pivot tuples according to whether \(j_m=n\) gives

\[
C_{m,n}=C_{m,n-1}+Q^{n-m}C_{m-1,n-1},
\qquad C_{0,n}=C_{n,n}=1.
\tag{6.5}
\]

The product \(\prod_{i=1}^m(Q^{n-m+i}-1)/(Q^i-1)\) satisfies the same recurrence: after division by that product the two terms have respective factors \((Q^{n-m}-1)/(Q^n-1)\) and \(Q^{n-m}(Q^m-1)/(Q^n-1)\), whose sum is one. Induction identifies it with \(C_{m,n}\), the Gaussian binomial in (6.4). For \(\operatorname{Gr}(2,4)\) the cell dimensions are \(0,1,2,2,3,4\), giving \(1+Q+2Q^2+Q^3+Q^4\).

For complete flags project to the first line. The base \(\mathbf P^{n-1}\) has the closed coordinate filtration with pieces \(\mathbf A^i\), \(0\leq i<n\). On a line's pivot cell its normalized vector is \(e_j+\sum_{a<j}c_ae_a\); the coordinate vectors other than \(e_j\) give a basis of the quotient by that line, algebraically in the \(c_a\). Thus above this cell the flag projection is the product with the flag variety of an \((n-1)\)-dimensional space. Induction gives affine pieces of dimensions \(i+a\), where \(a\) ranges through the previous flag cells. They admit a closed filtration: within the preimage of each closed base stage, first retain the preimage of the previous stage, then the successive closed fibre stages over its open cell. The complement of each such union is open in that open cell, hence open in the closed base stage. All constructions are over \(k_0\). The flag variety is proper, being the closed incidence locus in the product of the relevant Grassmannians. The same localization proof therefore yields only even cohomology with Tate characteristic polynomials and point-count polynomial

\[
\prod_{j=1}^n(1+Q+\cdots+Q^{j-1})=[n]_Q!.
\tag{6.6}
\]

These arguments supply the geometry, counts and cohomological interpretation within this lesson.

## 7. Exercises with complete solutions

**Exercise 7.1 (easy: affine and projective spaces).** Verify the trace formula for \(\mathbf A^n\) and \(\mathbf P^n\), with constant \(E\)-coefficients and all powers of Frobenius.

**Solution.** For affine space use (6.2), obtained at finite levels from Smooth traces, duality and Gysin maps, Proposition 14.1 and its proof, and passed to \(E\) by §5. Its only contribution is the even-degree trace \(q^{rn}\). The same proposition gives \(H^{2i}(\mathbf P^n,E)=E(-i)\), \(0\leq i\leq n\), and zero odd cohomology, with the hyperplane powers as generators. Frobenius to the \(r\)-th power acts by \(q^{ri}\), so its alternating trace is \(\sum_{i=0}^nq^{ri}\). Independently, projective points over \(\mathbf F_Q\) are lines in \(\mathbf F_Q^{n+1}\): its \(Q^{n+1}-1\) nonzero vectors partition into sets of \(Q-1\) on each line. Hence the count is \((Q^{n+1}-1)/(Q-1)=\sum_{i=0}^nQ^i\), with \(Q=q^r\). Affine space has \(Q^n\) points by its coordinate tuples. In both cases the local coefficient trace is \(1\) at each rational point.

**Exercise 7.2 (medium: the proper compatibility).** Prove the Frobenius assertion of Lemma 2.1 when \(f_0\) is proper, explaining which comparison carries the operator.

**Solution.** Here \(Rf_!=Rf_*\). Form \(X'\), \(a,f',h\) as in (2.3). Proper base change identifies \(F_Y^{-1}Rf_*K\) with \(Rf'_*a^{-1}K\). The finite universal-homeomorphism equivalence identifies the latter with \(Rf_*F_X^{-1}K\). Composing with \(Rf_*c_X\) gives the operator on the direct image. Its comparison with the descended operator follows either on étale charts and their resolutions, as in the proof, or by observing that these adjunction maps commute with arithmetic \(\sigma\) and using \(F^*=\rho(\sigma)^{-1}\). Stalk base change at a rational \(y\) commutes with \(\sigma\), so it transports the inverse arithmetic operator to the fibre cohomology. This identifies both the map and its direction.

**Exercise 7.3 (medium: every Frobenius power).** Deduce the formula for \(F^r\), and reorganize it by closed points.

**Solution.** Base change to \(\mathbf F_{q^r}\) in Theorem 4.1 or 5.1; its scheme Frobenius and coefficient map are the \(r\)-fold iterates. A degree-\(d\) closed point acquires rational geometric points precisely when \(d\mid r\). It then gives \(d\) points and the conjugate local maps \(F_x^{r/d}\). Consequently the formula reads

\[
\operatorname{Tr}(F_X^{r*};R\Gamma_c(X,K))
=\sum_{d\mid r}d
\sum_{\substack{x\in|X_0|\\\deg x=d}}
\operatorname{Tr}(F_x^{r/d};K_{\bar x}).
\tag{7.1}
\]

All sums for a fixed \(r\) are finite. This is the closed-point trace identity, not an assertion that a degree-\(d\) point contributes for every \(r\).

**Exercise 7.4 (medium: top compact-support cohomology).** Let \(X\) be nonempty and \(\dim X=d\geq0\). Prove \(H_c^i(X,E)=0\) for \(i>2d\) and
\[
\dim_EH_c^{2d}(X,E)=
\#\{\text{irreducible components of }X\text{ of dimension }d\}.
\tag{7.2}
\]
Explain why the components are those of the geometric scheme \(X\).

**Solution.** Vanishing is (5.1). Reduction does not change the étale topos. Remove the intersections of the top-dimensional components, their nonsmooth loci, and all smaller-dimensional components. Over the perfect field \(k\), this leaves a disjoint union \(U=\coprod U_j\) of smooth connected \(d\)-dimensional schemes, one dense open in each top component. The complement \(Z\) has dimension at most \(d-1\).

For \(d\geq1\), localization has the exact segment
\[
H_c^{2d-1}(Z,E)\longrightarrow H_c^{2d}(U,E)
\longrightarrow H_c^{2d}(X,E)
\longrightarrow H_c^{2d}(Z,E).
\]
The outside groups vanish, since their degrees exceed \(2(d-1)\). Smooth Poincaré duality with its trace map gives
\(H_c^{2d}(U_j,E)=E(-d)\), dual to \(H^0(U_j,E)=E\).
The finite-level trace isomorphism is proved in Smooth traces, duality and Gysin maps, Corollary 10.2. Its compatible trace maps pass to \(O\), then \(E\), by §5; no properness of \(U_j\) is required. Taking the direct sum proves (7.2). For \(d=0\), use the finite geometric-point calculation of Lesson 6 directly.

For example \(X_0=\operatorname{Spec}\mathbf F_{q^2}\times\mathbf A^d\) is irreducible over \(\mathbf F_q\), but \(X\) has two components and its top cohomology has dimension two. Frobenius interchanges their generators and multiplies by \(q^d\), so its first-power top trace is zero. This agrees with the absence of \(\mathbf F_q\)-points.

**Exercise 7.5 (hard: a surface with a singular fibre).** Carry out the reduction for
\[
X_0=\{(x,y,t):xy=t\}\subset\mathbf A^3,\qquad
f_0:X_0\to\mathbf A^1,\quad(x,y,t)\mapsto t.
\]
Use constant \(E\)-coefficients and compute every rational fibre contribution.

**Solution.** The surface is isomorphic to \(\mathbf A^2\), by eliminating \(t\). A nonzero rational fibre is \(\mathbf G_m\), with traces \(1\) in \(H_c^1\) and \(q\) in \(H_c^2\); its alternating trace is \(q-1\). The zero fibre is two affine lines meeting at the origin. Its open part consists of two copies of \(\mathbf G_m\), and its closed part is that point. Additivity gives
\[
2(q-1)+1=2q-1.
\]
More explicitly its \(H_c^1\) is the cokernel of the diagonal \(E\to E^2\), with trace \(1\), and its \(H_c^2\) is \(E(-1)^2\), with trace \(2q\). These give the same answer.

By (2.2), these are precisely the local traces of \(Rf_{0!}E\). There are \(q-1\) nonzero rational base points and one zero point. The base trace formula and support composition yield
\[
(q-1)(q-1)+(2q-1)=q^2,
\]
which is the trace of \(F^*\) on \(H_c^4(\mathbf A^2,E)=E(-2)\). The singular fibre is handled as a constructible stalk complex; the induction never assumed smooth fibres.

**Exercise 7.6 (hard: torsion and finite levels).** At a point, let \(\mathcal T=O/\varpi\), with the identity operator. Compare its perfect \(O\)-trace, the ordinary \(O_n\)-module reduction, and its derived \(O_n\)-reduction.

**Solution.** A perfect \(O\)-representative is \([O\xrightarrow{\varpi}O]\) in degrees \(-1,0\), with identity on both terms. Its trace is \(-1+1=0\). The ordinary reduction is the module \(O/\varpi\); for \(n>1\) this has infinite projective dimension over \(O_n\), as its periodic free resolution alternates multiplication by \(\varpi\) and \(\varpi^{n-1}\). Thus its ordinary-module trace is not the perfect-complex trace used in Theorem 4.1.

The derived reduction is \([O_n\xrightarrow{\varpi}O_n]\), with trace zero. For \(n>1\) it has nonzero cohomology in degrees \(-1\) and \(0\), both isomorphic to the residue field, so dropping the negative-degree contribution would lose the integral trace. After tensoring with \(E\), the original complex is acyclic. This explains the torsion treatment in Theorem 5.1.

**Exercise 7.7 (medium: an infinite noncommutative coefficient ring).** Let \(\ell\ne p\), \(R=\mathbf F_\ell[t,t^{-1}]\), \(\Lambda=M_2(R)\), and \(K_0=\underline\Lambda\) on \(\mathbf A^d_{k_0}\). Compute both sides of Theorem 4.1. Explain why forgetting coefficients to finite abelian stalks would not prove this example.

**Solution.** The ring is left Noetherian and killed by \(\ell\), while its stalk set is infinite. The constant coefficient complex is free of rank one as a left \(\Lambda\)-module. The central scalar-extension projection formula from \(\mathbf F_\ell\), together with (6.2), gives \(R\Gamma_c(\mathbf A^d,K)=\Lambda(-d)[-2d]\). Its Frobenius is multiplication by the central scalar \(q^d\); the perfect left-module trace is therefore the class \([q^d1_\Lambda]\in\Lambda^\natural\). Each rational stalk has trace \([1_\Lambda]\), and the \(q^d\) points sum to the same class. The bracket denotes the additive commutator quotient, so no determinant or multiplication of arbitrary quotient classes is involved. Theorem 3.1's generator and spectral-sequence argument, rather than finite underlying abelian constructibility, provides the coefficient passage. The calculation is valid also if this particular class vanishes in the quotient.

**Exercise 7.8 (hard: singular adic coefficients).** Let \(A=\mathbf Z_\ell[\epsilon]/(\epsilon^2)\), with \(\mathfrak m=(\ell,\epsilon)\), and on a rational point take the perfect coefficient complex \(P=[A\xrightarrow{\epsilon}A]\) in degrees \(-1,0\). Let Frobenius multiply both terms by \(a\in A^\times\). Compute its trace at every level and over \(A\); explain why its cohomology is not a substitute for the projective model.

**Solution.** The endomorphism commutes with the differential because \(A\) is commutative. The perfect trace is \(-a+a=0\); reduction to \(A_n\) gives the same two-term free complex and trace zero. Its degree-minus-one cohomology is \((\epsilon)\), and its degree-zero cohomology is \(A/(\epsilon)\). Both have infinite projective dimension over \(A\): the free resolution of \(A/(\epsilon)\) has differential multiplication by \(\epsilon\) in every positive step, since the kernel and image of this multiplication both equal \((\epsilon)\), and \((\epsilon)\simeq A/(\epsilon)\). Tensoring that resolution with the residue field makes every differential zero. Thus individual cohomology modules have no projective-module trace of the kind used here. The compatible free models recover the perfect complex and its zero trace exactly as in Theorem 5.2. On a point the global and local complexes are the same, so the trace formula holds without discarding either degree.

## What this lesson does not prove

The geometric inputs are identified in §1. General central finite-coefficient torsion constructibility is an expressly inherited theorem there. We do not claim to prove that finiteness foundation in this lesson. The proof here supplies Frobenius compatibility, relative constructibility for the larger left-module coefficients, finite Tor preservation, finite-field normalization, full dimension induction and the complete-local adic trace passage. Lesson 1 supplies the written compatible-perfect-complex theorem and adic torsion decomposition; Lesson 2 supplies derived completion, the local rational coefficient category and finite scalar descent. Corollaries 5.3–5.4 use these actual local lattices and fields on a finite stratification, covering the full constructible algebraic rational coefficient scope without a global-lattice assumption. The smooth trace and duality proof supplies the affine/projective cohomology and top-degree orientation. Projective-space, Grassmannian and flag counts and cells are written above, using the stated earlier results.

The trace theorem requires separated finite-type schemes over a finite field and prime-to-characteristic torsion or adic coefficients. The relative constructibility comparison has the Noetherian coefficient and finite-presentation conditions in §1. The complete-local generalization assumes a finite residue field and finite-Tor derived constructibility; it does not assert that every finite module over a singular coefficient ring is perfect. Proper base change in Lesson 2 permits broader bases and characteristic torsion, but that fact alone does not extend the Frobenius trace theorem to them. The Euler-product identity, finite-characteristic determinant difficulties and rationality of general \(L\)-functions are treated in the next lesson.

<a id="references-and-source-record"></a>

## References

Pierre Deligne, [*La conjecture de Weil. I*](https://publications.ias.edu/sites/default/files/Number23.pdf), §1, especially (1.3), (1.5), (1.9)–(1.15), printed pp. 274–279: finite compact-support cohomology, the trace formula with its iterates, constructible rational coefficients and the geometric/Galois Frobenius dictionary. These are recalled Grothendieck theorems there; the article does not give the missing all-dimensional finite-coefficient induction.

Deligne, [*Cohomologie étale* (SGA \(4\frac12\))](https://publications.ias.edu/sites/default/files/Number32.pdf), [Rapport], Theorems 3.1–3.2, printed p. 86; Theorems 4.9–4.10 and §§4.11–4.13, pp. 95–99; §6, pp. 107–108. The left Noetherian torsion theorem, compatible-perfect-complex passage and filtered fibre reduction occur at these locators. Our relative extension and induction retain its right/left module roles and actual filtered additivity.

The Stacks project authors, [Cohomological interpretation, Tag 03UY](https://stacks.math.columbia.edu/tag/03UY), contains the finite-ring trace statement [03V3](https://stacks.math.columbia.edu/tag/03V3), its rational adic passage [03V2](https://stacks.math.columbia.edu/tag/03V2) and the compatible-complex lemma [03V4](https://stacks.math.columbia.edu/tag/03V4). Its all-dimensional finite-coefficient proof is only a reduction sketch. The corresponding [AI Integrated Stacks Project, English, The Trace Formula](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/trace.html#trace-section-L-cohomological) passage and its [source](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/trace.tex#L2180) retain the explicit omitted-foundation list [03V5](https://stacks.math.columbia.edu/tag/03V5). The chapter credits Johan de Jong's 2009 course and note takers Thibaut Pugin, Zachary Maddock and Min Lee. Upstream Stacks mathematics and the credited AI additions retain their GNU FDL terms. This lesson's explanatory text has the CC0 dedication stated above.

Bhargav Bhatt and Peter Scholze, [*The pro-étale topology for schemes*](https://arxiv.org/abs/1309.1198), §§6.5–6.8, provide the modern coefficient-category comparison, especially Definitions 6.5.1 and 6.8.6, Lemma 6.7.5, and Proposition 6.8.4. Its exact completion, finite-Tor, proper-base-change, local-lattice and finite scalar-descent proof homes in this course are Lesson 2. Theorem 5.2 proves the trace statement in the specified complete-local scope, Corollary 5.3 explains why local rational lattices suffice, and Corollary 5.4 treats all constructible algebraic rational coefficients with their stated topology.

Grothendieck, SGA 5, Exposé XV, §2, “Statement of the rationality theorem and reduction to the case of a curve,” gives the original fibre reduction in its \(L\)-function form. Milne, *The Riemann Hypothesis over Finite Fields: From Weil to the Present Day* (2015), subsection “Grothendieck's theorem,” describes the same dévissage. These historical passages motivate the argument; §§2–5 give its proof here.
