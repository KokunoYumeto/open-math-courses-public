# Artin approximation for polynomial equations and its desingularization proof

*Written and self-checked by GPT-6.1 Sol (OpenAI), Codex, Ultra setting, 5 October 2026. This reconstruction draft includes the desingularization proof and its consumed foundations. It retains adapted GNU FDL 1.2 expression.*

The purpose of approximation is to retain exact equations while replacing coefficients in a completed local ring by coefficients on an étale neighbourhood. A coefficient need not itself belong to the local ring, and approximating each coefficient separately generally destroys its equations. Instead, retain all equations in one finite system, including those that impose the desired congruence.

The only mathematical source used to construct the new desingularization material is the freely accessible pinned Stacks exposition and its supporting chapters. Earlier programme proofs are used where their exact statements apply. The source is material for the proof written here; a link to that source does not discharge a mathematical obligation. The original theorem below remains the target until all of its consumed dependencies are proved in this lesson or an earlier programme lesson.

## 1. The exact approximation statement

A map of Noetherian rings is **regular** if it is flat and every fibre is geometrically regular. An algebra over a field is geometrically regular if after every finite field extension its local rings are regular. A **G-ring** is a Noetherian ring whose maps from localizations to their completions are regular. The relevant implication for a local G-ring is therefore immediate from its definition: \(R\to\widehat R\) is regular. The broader local criterion and permanence statements, including the property for local rings essentially of finite type over \(\mathbb Z\), are supplied among the foundation arguments below.

**Theorem 1.1 (Artin approximation in a pointed étale neighbourhood).** Let \((R,\mathfrak m)\) be a Noetherian local G-ring. Let

\[
f_1,\ldots,f_q\in R[X_1,\ldots,X_n],
\qquad \widehat a\in\widehat R^n,
\qquad f_j(\widehat a)=0.
\]

For every positive integer \(N\), there exist a finitely presented étale \(R\)-algebra \(R'\), a maximal ideal \(\mathfrak m'\subset R'\) over \(\mathfrak m\), and a solution \(b\in(R')^n\), such that

\[
\kappa(\mathfrak m')=\kappa(\mathfrak m),\qquad
f_j(b)=0,\qquad
\rho(b_i)-\widehat a_i\in\mathfrak m^N\widehat R.
\tag{1.1}
\]

Here \(\rho:R'\to\widehat R\) is the canonical lift of the specified residue-field point. This is a homomorphism; no assertion that the whole étale algebra embeds into the completion is required. The statement allows arbitrary characteristic, imperfect residue fields, nilpotent base elements, and nonregular local rings.

**Lemma 1.2 (the canonical comparison map).** A finitely presented étale \(R\)-algebra and a specified \(R\)-map \(R'\to R/\mathfrak m\) have a unique compatible map \(R'\to\widehat R\).

**Proof.** Starting with the specified map to \(R/\mathfrak m\), lift successively to \(R/\mathfrak m^r\). The kernel of
\(R/\mathfrak m^{r+1}\to R/\mathfrak m^r\)
is square zero for \(r\geq1\), so existence and uniqueness follow from formal étaleness. The lifts are compatible by uniqueness. Taking their inverse limit gives the desired map. A map into an inverse limit of rings is exactly a compatible collection of maps into the constituent rings, which also proves uniqueness. The equality \(\widehat R/\mathfrak m^r\widehat R=R/\mathfrak m^r\) used here is proved in [AG-CA, Completion, Proposition 2.2 and Theorem 3.3](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/completion.html#2-topology-and-the-powers-of-the-ideal). Formal étaleness of an étale algebra is the defining lifting property in [AG-CA, Formally smooth, unramified and étale ring maps, §6](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/formally-smooth-unramified-and-etale-ring-maps.html). ∎

**Lemma 1.3 (a smooth residue-field point has an étale lift).** If \(B\) is a smooth finitely presented \(R\)-algebra and \(B\to\kappa=R/\mathfrak m\) is an \(R\)-map, there are a finitely presented étale \(R\)-algebra \(R'\), a point \(R'\to\kappa\), and an \(R\)-map \(B\to R'\) inducing the original point.

**Proof.** Use the local standard form proved in [AG-CA, Formally smooth, unramified and étale ring maps, Theorem 5.1 and Solution 8.5](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/formally-smooth-unramified-and-etale-ring-maps.html#5-from-a-split-sequence-to-local-coordinates). At the kernel of the given point, localize once to write

\[
B_g=R[X_1,\ldots,X_s]/(h_1,\ldots,h_c),
\qquad
\Delta=\det(\partial h_i/\partial X_j)_{i,j\leq c}
\quad\text{a unit}.
\]

This presentation includes any localization variable and its equation. Choose \(r_{c+1},\ldots,r_s\in R\) lifting the point's coordinates in the remaining variables. Substitute these elements in the equations, keeping the first \(c\) variables. Localize the resulting algebra at the substituted \(\Delta\) and at any denominators needed for the original presentation. Its number of equations and variables agree, and its square Jacobian determinant is a unit. The direct Newton calculation proving a standard étale presentation is étale appears in the same earlier lesson, Theorem 4.1 and §6: a square-zero error vector is corrected uniquely by the inverse Jacobian matrix. Thus the resulting \(R'\) is finitely presented étale. The original residue coordinates define its map to \(\kappa\), since the inverted elements have nonzero residues. The kernel of that map is maximal and has residue field \(\kappa\), because the structural map from \(R\) already surjects onto \(\kappa\). Substitution gives \(B_g\to R'\), hence \(B\to R'\). ∎

**Proof of Theorem 1.1.** The equality of finite-order quotients of a Noetherian local ring and its completion is proved at the preceding Completion locators. Choose \(c_i\in R\) representing \(\widehat a_i\) modulo \(\mathfrak m^N\widehat R\), and choose finitely many generators \(d_1,\ldots,d_M\) of \(\mathfrak m^N\). Write

\[
\widehat a_i=c_i+\sum_{l=1}^M d_l\widehat u_{il}.
\]

Put

\[
g_j(U)=f_j\left(c_1+\sum_l d_lU_{1l},\ldots,
c_n+\sum_l d_lU_{nl}\right),
\qquad A=R[U_{il}]/(g_j).
\tag{1.2}
\]

The tuple \(\widehat u\) gives an \(R\)-map \(A\to\widehat R\). Since \(R\to\widehat R\) is regular, the desingularization theorem proved by the sequence ending at [Theorem D.38](#smoothing-theorem-popescu), and the elementary factorization criterion proved at [the corresponding foundation lemma](#algebra-lemma-when-colimit), give a factorization

\[
A\longrightarrow B\longrightarrow\widehat R
\tag{1.3}
\]

with \(B\) smooth and finitely presented over \(R\). Compose with the residue map \(\widehat R\to\kappa\), then apply Lemma 1.3. The images \(u_{il}\in R'\) solve the \(g_j\) exactly. Set \(b_i=c_i+\sum_l d_lu_{il}\). Substitution in (1.2) gives \(f_j(b)=0\) exactly. Under the canonical map of Lemma 1.2,

\[
\rho(b_i)-\widehat a_i
=\sum_l d_l\bigl(\rho(u_{il})-\widehat u_{il}\bigr)
\in\mathfrak m^N\widehat R.
\]

This proves the prescribed congruence without demanding that the auxiliary \(u_{il}\) themselves be close to \(\widehat u_{il}\). The exact written foundations and the earlier programme proofs used in this argument are registered in §6. ∎

**Corollary 1.4 (henselian formulation).** If \(R\) is henselian, the solution can be chosen in \(R\). In general it gives a solution in the henselization \(R^h\), descending to the pointed étale neighbourhood just constructed.

**Proof.** The section criterion proved in [AG-CA, Henselian local rings and henselization, Theorem 1.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/henselian-local-rings-and-henselization.html#1-roots-and-maps-with-a-prescribed-residue) gives \(R'\to R\) with the specified residue map. Its composition with \(R\to\widehat R\) is the map \(\rho\) by Lemma 1.2, so (1.1) is preserved. For \(R^h\), use the pointed étale colimit and its universal property proved in that lesson, Lemma 4.1 and Theorem 4.2. Compatibility with the map into the complete henselian ring follows from the same uniqueness. Here the principal monic chart consumed by that section-criterion proof is supplied by the full [earlier structural étale proof, Lemma D2.2](AG-RG-S04.md), whose integral closure input is [the affine conductor theorem, Theorem C4.3](AG-RG-S04.md). Its polynomial normality input is proved in [the preliminary coefficient argument, Corollary B1.2](AG-RG-S04.md). To spell out the actual section step, localize the selected étale algebra
to $(R[T]/(F))_h$, with $F$ monic and $F'$ nonzero at the given residue
root $\bar a$. The henselian simple-root property gives $a\in R$ with
$F(a)=0$ and $a\bmod\mathfrak m=\bar a$. Every denominator has nonzero
residue at $\bar a$, hence is a unit at $a$, and evaluation defines
the section. The resulting map $R'\to R$ induces the prescribed residue
map; formal étale uniqueness along the quotients $R/\mathfrak m^n$
proves its composition with completion is $\rho$. Thus this corollary uses these written earlier proofs rather than an external conductor proof tag. ∎

## 2. Returning from a local model to the original base

**Lemma 2.1 (spreading finite presentation data).** Let \(R_0\) be Noetherian and \(\mathfrak p\subset R_0\). A pointed étale algebra, a finite tuple, and finitely many equations over \((R_0)_{\mathfrak p}\), as in Theorem 1.1, spread to \((R_0)_s\) for some \(s\notin\mathfrak p\). Their solution therefore gives a pointed étale neighbourhood over \(R_0\).

**Proof.** In the construction of Lemma 1.3, every polynomial coefficient, every fixed nonpivot coordinate, and every chosen inverse has a denominator outside \(\mathfrak p\). Invert their product in \(R_0\). The finitely many equations for the tuple and the finitely many witnesses verifying them likewise hold after multiplying by finitely many additional denominators; invert their product too. The standard étale presentation spreads with its invertible Jacobian determinant, so its spread algebra is étale by the same direct Newton calculation. Regard it as an \(R_0\)-algebra through the étale localization \(R_0\to(R_0)_s\); composing two formally étale, finitely presented maps remains étale because a square-zero lifting problem is solved uniquely in two successive steps. The chosen residue map survives and gives a point over \(\mathfrak p\) with unchanged residue field. The defining equations remain exact, and localization at the selected point gives the original local comparison. ∎

This proof uses the specific standard étale algebra produced above and therefore does not invoke an external spreading theorem for an arbitrary presentation. Pulling the resulting neighbourhood back to the original scheme preserves every defining equation and the specified fibre point.

## 3. The finite system for an embedded torus

The approximation step in the torus lesson begins after the formal deformation and effectivity argument has produced an affine torus \(\widehat T\) over the completed local model and a closed homomorphism \(\widehat T\hookrightarrow G_{\widehat R}\). The present lesson proves the approximation input; it does not claim to supply that preceding effectivity argument.

<a id="finite-complete-local-splitting"></a>

**Lemma 3.A (finite splitting over a complete local ring).** Let \((A,\mathfrak m,\kappa)\) be a local ring with
\[
A\simeq\varprojlim_{n\geq1}A/\mathfrak m^n.
\]
No Noetherian, reducedness, normality or perfection hypothesis is imposed. Suppose a torus \(T/A\) has an affine etale splitting chart \(U\to\operatorname{Spec}A\) and a point of its closed fibre with finite separable residue field \(K/\kappa\). Then a finite free, faithfully flat, etale algebra \(E/A\) splits \(T\). We may choose \(E\) local and complete, with residue field a finite Galois extension \(L/\kappa\) containing \(K\), and with an action of \(\Gamma=\operatorname{Gal}(L/\kappa)\) for which
\[
E\otimes_AE\xrightarrow{\sim}\prod_{\sigma\in\Gamma}E,
\qquad x\otimes y\longmapsto\bigl(x\sigma(y)\bigr)_\sigma.
\tag{3.2}
\]
Here a torus is etale locally a product of copies of \(\mathbf G_m\). Starting instead with the fpqc multiplicative-type definition gives this same condition by [AG-GS-05, Theorem 7.7](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-GS/AG-GS-05.html); its finite torsion-free character-group step is proved in [AG-RG-S04, Lemma P0.10](AG-RG-S04.md#finite-torsion-free-lattices). Every torus therefore has such a chart and residue point: choose an affine finite-presentation part of an etale splitting cover meeting the closed fibre, and a closed point of that fibre. Its residue field is finite over \(\kappa\) by the finite-type field-algebra argument in AG-RG-S04, Lemma P0.9. The quotient sequence for differentials gives \(\Omega_{K/\kappa}=0\), because the chart is formally unramified. The finite-field differential calculation in AG-CA-17, Lemma 7.1 then proves separability.

Furthermore, a torus \(T_0/\kappa\), with character lattice split by \(L\), has a torus lift over \(A\) split by this same \(E\). Its character lattice and descent action reduce compatibly modulo every \(\mathfrak m^n\).

**Proof.** A finite separable extension embeds in a finite normal separable extension: adjoin all the roots of the minimal polynomials of a finite generating list. There are finitely many roots and each adjunction has finite separable degree. Every embedding permutes the root sets, so the resulting extension \(L/\kappa\) is normal and separable. Counting embeddings successively gives \(|\Gamma|=[L:\kappa]\). The primitive-element argument of AG-RG-S02, Lemma 4.2, applies also to finite fields, and gives \(L=\kappa(\alpha)\). Let \(\bar f\in\kappa[X]\) be the monic minimal polynomial of \(\alpha\), and lift its coefficients to a monic \(f\in A[X]\). Put
\[
E=A[t]=A[X]/(f),\qquad d=\deg(f).
\]
Successively subtracting leading multiples of the monic polynomial \(f\) reduces every polynomial to degree less than \(d\). A nonzero multiple \(qf\) has degree \(\deg(q)+d\), since its leading coefficient is the nonzero leading coefficient of \(q\). Thus the remainder is unique, and \(1,t,\ldots,t^{d-1}\) is a basis making \(E\) free of positive finite rank over \(A\); it is faithfully flat because tensoring a module with this free module gives a direct sum of \(d\) copies. Its quotient by \(\mathfrak mE\) is \(L\). If \(e\in E\) has nonzero residue, multiplication by \(e\) on this basis is invertible modulo \(\mathfrak m\). Its determinant is a unit of \(A\), and its adjugate gives an inverse to multiplication by \(e\). Thus \(e\) is a unit, \(E\) is local with maximal ideal \(\mathfrak mE\), and coordinatewise completeness gives
\[
E\simeq\varprojlim_n E/\mathfrak m^nE.
\]
Separability makes \(f'(t)\) a unit by the same argument. A root in a quotient by a square-zero ideal lifts uniquely by replacing any lift \(a\) with \(a-f'(a)^{-1}f(a)\). Polynomial expansion proves existence, and
\(f(b)-f(a)=(b-a)(f'(a)+(b-a)H)\) proves uniqueness. Iteration gives the corresponding assertion for every nilpotent ideal. This proves formal etaleness of \(E/A\); its finite presentation makes it etale.

The residue point of \(U\) gives an algebra map \(\mathcal O(U)\to K\to L\). Formal etaleness of \(U/A\) lifts this map uniquely through
\(E/\mathfrak m^{n+1}E\to E/\mathfrak m^nE\), whose kernel is square-zero for \(n\geq1\). Taking the compatible limit gives a map \(\mathcal O(U)\to E\), hence a section of \(U_E\to\operatorname{Spec}E\). Pulling back the splitting on \(U\) therefore splits \(T_E\).

We now construct (3.2), including its automorphisms. For every \(\sigma\in\Gamma\), the residue \(\sigma(\alpha)\in L\) is a simple root of \(\bar f\). In the complete local ring \(E\), Newton's recursion
\[
a_{j+1}=a_j-f'(a_j)^{-1}f(a_j)
\]
starting from any lift of this residue gives
\(f(a_j)\in(\mathfrak mE)^{2^j}\) and
\(a_{j+1}-a_j\in(\mathfrak mE)^{2^j}\). Completeness and separatedness give a root \(a_\sigma\), and the difference formula above gives its uniqueness with that residue. Distinct \(a_\sigma\) have unit differences. If a polynomial \(P\) vanishes at all these roots, monic division by \(X-a_1\) gives \(P=(X-a_1)Q\), since the remainder is \(P(a_1)=0\).
At each other root \(a_\sigma\), the factor \(a_\sigma-a_1\) is a unit, so \(Q(a_\sigma)=0\). Repeating the division shows that \(\prod_\sigma(X-a_\sigma)\) divides \(P\). If \(\deg(P)<d\), monicity forces \(P=0\). The difference between \(f\) and this product has degree less than \(d\) and vanishes at every root, so
\[
f(X)=\prod_{\sigma\in\Gamma}(X-a_\sigma).
\]
The map \(t\mapsto a_\sigma\) defines an \(A\)-algebra endomorphism \(g_\sigma\) of \(E\). The two roots \(g_\sigma g_\tau(t)\) and \(a_{\sigma\tau}\) have the same residue, so uniqueness gives \(g_\sigma g_\tau=g_{\sigma\tau}\). Also \(a_1=t\); hence these maps are automorphisms and lift the Galois action on \(L\).

The isomorphism \(E\otimes_AE=E[X]/(f)\) and evaluation at the \(a_\sigma\) now give (3.2). Explicitly, the polynomials
\[
\ell_\sigma(X)=\prod_{\tau\ne\sigma}
\frac{X-a_\tau}{a_\sigma-a_\tau}
\]
give the inverse to evaluation: a tuple \((b_\sigma)_\sigma\) is represented by \(\sum_\sigma b_\sigma\ell_\sigma(X)\). Thus the isomorphism uses no division by \(|\Gamma|\). Its compatibility on triple products is exactly \(g_\sigma g_\tau=g_{\sigma\tau}\). This is the required finite etale Galois torsor.

For the final assertion choose the finite Galois splitting field of \(T_0\) supplied by AG-GS-05, Lemma 5.1, and let \(M\) be its free finite-rank character lattice, with the resulting \(\Gamma\)-action. On \(E[M]\) put
\[
\sigma(ae^m)=g_\sigma(a)e^{\sigma m}.
\tag{3.3}
\]
The group law and (3.2) make this a descent datum. Multiplication and every Hopf operation commute with it, since addition in \(M\) commutes with its action. The actual module and algebra effectivity proof in AG-RG-S04, Lemmas A1.1--A1.2, gives the invariant Hopf algebra
\[
C=E[M]^\Gamma,\qquad E\otimes_AC\simeq E[M].
\tag{3.4}
\]
Tensor products and Hopf identities descend by this isomorphism and faithful flatness. Finite presentation descends here by a finite-generator argument. Express the finitely many Laurent algebra generators over \(E\) as finite \(E\)-linear combinations of elements of \(C\). Those elements generate \(C\), since the cokernel of their generated subalgebra becomes zero over \(E\). For a resulting finite polynomial surjection \(A[Z]\to C\), its kernel becomes a finite ideal after tensoring with \(E\), because \(E[M]\) is finitely presented. To see that finiteness for this particular surjection, compare it with a finite presentation of \(E[M]\): express each presentation's generators in the other, and substitute these expressions in the finitely many relations and composite-generator identities. They generate the new kernel. Write a finite list of its generators as finite sums of elements of the original kernel with coefficients in \(E\). Their finitely many kernel components generate the original kernel by faithful flatness. Thus \(C\) is finitely presented. It defines a torus \(T_A\), because (3.4) splits it on the finite etale faithfully flat cover.

Put \(A_n=A/\mathfrak m^n\) and \(E_n=E\otimes_AA_n\). Tensoring (3.2)--(3.4) with \(A_n\) gives the same torsor and the same character action over \(E_n\):
\[
E_n\otimes_{A_n}(C\otimes_AA_n)\simeq E_n[M].
\tag{3.5}
\]
The algebra on the left descends the datum (3.3) modulo \(\mathfrak m^n\); uniqueness in Lemma A1.2 proves that it is its effective descent. This proves compatibility for every \(n\), even though \(A\to A_n\) need not be flat. It does not assume that taking invariants commutes with an arbitrary quotient. At \(n=1\), the descent datum is precisely the given one on \(L[M]\), so its descended torus is \(T_0\).

More generally, any compatible character data split by these \(E_n\) and identified with the same lattice have no additional nilpotent transition parameters. Comparing coefficients in
\(\Delta(\sum c_me^m)=(\sum c_me^m)\otimes(\sum c_me^m)\) gives
\(c_m^2=c_m\), \(c_mc_{m'}=0\) for \(m\ne m'\), and \(\sum c_m=1\). Each \(E_n\) is local, so exactly one coefficient is \(1\). A character is therefore one monomial; a torus automorphism is one integral lattice automorphism. A compatible automorphism reducing to a fixed one is that same one. Hence a compatible lattice descent action is the fixed action in (3.3), and (3.5) gives its actual compatible descent. This completes both assertions. \(\square\)

Choose a finite presentation of the Hopf algebra of \(\widehat T\). Lemma 3.A supplies a finite free, etale, faithfully flat splitting algebra \(E/\widehat R\); choose the resulting splitting isomorphism

\[
\mathcal O(\widehat T)\otimes_{\widehat R}E
\simeq E[Z_1^{\pm1},\ldots,Z_r^{\pm1}].
\tag{3.1}
\]

Since the completed base is local, the finite projective \(\widehat R\)-module \(E\) is finite free. Fix a basis. Its multiplication table, unit, and the matrices of multiplication define finitely many coefficient variables; associativity and the unit laws are polynomial equations on those variables. The trace pairing is computed from those matrices. Add the inverse of its determinant. This retains étaleness after approximation, as follows.

For a finite free algebra \(C/A\), a unit determinant of its trace pairing remains a unit in every fibre. A finite-dimensional commutative algebra over a field with nondegenerate trace pairing has zero nilradical: if \(x\) is nilpotent, multiplication by \(xy\) is nilpotent for every \(y\). A basis adapted to the increasing kernels of the powers of a nilpotent operator makes its matrix strictly triangular, so its trace is zero. Consequently every pairing \(\operatorname{Tr}(xy)\) is zero. It is therefore a finite product of fields by the Artinian structure theorem proved in [AG-CA, Noetherian and Artinian rings, Theorem 4.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/noetherian-and-artinian-rings.html#4-what-an-artinian-ring-looks-like). Each field factor is separable: if a finite field factor $L/k$ is inseparable, choose an element $a$ whose minimal polynomial $h$ has a repeated root over an algebraic closure $\Omega$. Then $k(a)\otimes_k\Omega=\Omega[T]/(h)$ contains a nonzero nilpotent: writing $h=(T-\alpha)^e q$ with $e>1$ and $q(\alpha)\ne0$, its factor $\Omega[T]/(T-\alpha)^e$ has the nonzero nilpotent $T-\alpha$, and the Chinese remainder decomposition embeds that factor. The inclusion $k(a)\hookrightarrow L$ remains injective after tensoring with $\Omega$, since tensoring vector spaces over a field is exact. Thus $L\otimes_k\Omega$ still has a nonzero nilpotent. Such an element pairs to zero with every element by the preceding trace calculation. This contradicts invertibility of the scalar-extended trace matrix. Trace matrices and their determinants commute with scalar extension because multiplication matrices do. Hence each field factor is separable. For a separable factor, scalar extension to an algebraic closure splits it into a product of copies of that closure; the trace pairing there is the diagonal pairing with ones on the diagonal. Conversely this shows that a finite product of separable fields has nondegenerate trace pairing. The fibre algebras are thus geometrically regular of dimension zero. Finite freeness gives flatness. The flat-fibre smoothness criterion reproduced in the foundation proof [F, flat fibre smooth](#algebra-lemma-flat-fibre-smooth) then makes \(C/A\) smooth. Moreover \(\Omega_{C/A}\) is finite and its tensor with every residue field of \(C\) is zero: differential base change reduces this to a finite separable field factor, whose differentials vanish by [AG-CA-17, Lemma 7.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/formally-smooth-unramified-and-etale-ring-maps.html). Local Nakayama and local detection give \(\Omega_{C/A}=0\). AG-CA-17, Theorem 2.2, then gives formal unramifiedness; smoothness supplies formal smoothness, so \(C/A\) is étale. Positive fixed rank makes the finite free algebra faithfully flat by [AG-CA, Faithful flatness and the local criterion for flatness, Theorem 2.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/faithful-flatness-and-the-local-criterion-for-flatness.html#2-faithfully-flat-ring-maps).

Add coefficients for the finite presentations, Hopf maps, the isomorphism (3.1), its inverse, and the homomorphism to \(G\). Laurent expressions can be written polynomially by adding inverse variables and relations \(Z_iW_i=1\). The maps need to be specified on finite generating sets. Relations between their images need finitely many witnesses in the finitely generated relation ideals. The two composites of the splitting isomorphism and its inverse are tested on finite generators; equality of these composites with the identity is recorded by their witnesses. The same method records comultiplication, counit, inverse, and the homomorphism identities on a finite list of generators. Coassociativity and every needed descent identity are likewise checked on finite generators, using the finite multiplication tables on the finite overlap algebras. Each expression and witness has finite support.

Retain the closed immersion in this same system. The pullback \(\mathcal O(G_{\widehat R})\to\mathcal O(\widehat T)\) is surjective. Choose preimages of a finite list of algebra generators of \(\mathcal O(\widehat T)\), and include the equations asserting that their images are those generators. After approximation these equations still prove surjectivity; consequently the resulting homomorphism is a closed immersion.

We have obtained one finite polynomial system over the local model, solved by the original completed coefficient tuple. Apply Theorem 1.1 at order one. The defining equations hold exactly after approximation, while all the chosen coefficients retain their original residues. The preserved splitting maps identify the source Hopf algebra with a Laurent polynomial Hopf algebra on the finite étale faithfully flat cover. Thus it is a torus, with the specified special fibre and closed embedding. If a prescribed higher jet is needed, use that order instead. Lemma 2.1 spreads the data and the neighbourhood back to an open part of the finite-type model; base change returns them to the original base.

The local model is essentially of finite type over \(\mathbb Z\). The G-ring permanence argument in §5 is therefore a consumed part of this application, including its coefficient-ring inputs. It must be proved before the approximation step is declared complete. An excellence label or an external Stacks link does not replace this work.

**Scope of the supporting algebra.** The approximation theorem and the desingularization theorem concern Noetherian rings. Every base ring of the finite-type algebra diagrams in their proof is Noetherian. In the foundational complete-intersection arguments below we state and prove the exact Noetherian forms consumed there; arguments explicitly stated over arbitrary rings retain that wider scope. Polynomial presentations with arbitrarily many variables occur only in the two-term cotangent comparison, whose elementary presentation and filtered-colimit proofs are written without Noetherian assumptions. This distinction preserves arbitrary characteristic, imperfect residue fields, and the full Noetherian local G-ring statement.

## 4. Desingularization proof sequence

The following sequence contains the actual lifting, presentation, local descent, separable, and inseparable arguments. It is adapted from the pinned free source. The source’s historical bibliography is not reproduced. Its statements use the conormal definition of smoothness reproduced among the foundation statements below. The displayed arrow lists specify the maps of the original commutative diagrams.

### Singular ideals

<a id="smoothing-section-singular-ideal"></a>

Let $R \to A$ be a ring map. The singular ideal of $A$ over $R$
is the radical ideal in $A$ cutting out the singular locus of the
morphism $\operatorname{Spec}(A) \to \operatorname{Spec}(R)$. Here is a formal definition.

<a id="smoothing-definition-singular-ideal"></a>

#### Definition D.1: singular ideal

*Adapted from the Stacks project, smoothing.tex, lines 124–132.*

Let $R \to A$ be a ring map. The *singular ideal of $A$ over $R$*,
denoted $H_{A/R}$ is the unique radical ideal $H_{A/R} \subset A$ with

$$
V(H_{A/R}) = \{\mathfrak q \in \operatorname{Spec}(A) \mid R \to A
\text{ not smooth at }\mathfrak q\}
$$

This makes sense because the set of primes where $R \to A$ is smooth
is open, see
Algebra, Definition [F.7](#algebra-definition-smooth-at-prime).
In order to find an explicit set
of generators for the singular ideal we first prove the following lemma.

<a id="smoothing-lemma-find-strictly-standard"></a>

#### Lemma D.2: find strictly standard

*Adapted from the Stacks project, smoothing.tex, lines 141–181.*

Let $R$ be a ring. Let $A = R[x_1, \ldots, x_n]/(f_1, \ldots, f_m)$.
Let $\mathfrak q \subset A$ be a prime ideal. Assume $R \to A$ is smooth
at $\mathfrak q$. Then there exists an $a \in A$, $a \not \in \mathfrak q$,
an integer $c$, $0 \leq c \leq \min(n, m)$, subsets
$U \subset \{1, \ldots, n\}$, $V \subset \{1, \ldots, m\}$
of cardinality $c$ such that

$$
a = a' \det(\partial f_j/\partial x_i)_{j \in V, i \in U}
$$

for some $a' \in A$ and

$$
a f_\ell \in (f_j, j \in V) + (f_1, \ldots, f_m)^2
$$

for all $\ell \in \{1, \ldots, m\}$.

**Proof.** 
Set $I = (f_1, \ldots, f_m)$ so that the naive cotangent
complex of $A$ over $R$ is homotopy equivalent to
$I/I^2 \to \bigoplus A\text{d}x_i$, see
Algebra, Lemma [F.11](#algebra-lemma-NL-homotopy).
We will use the formation of the naive cotangent complex commutes with
localization, see Algebra, Section [the cotangent-complex context](#cotangent-context),
especially Algebra, Lemma [F.65](#algebra-lemma-localize-NL).
By Algebra, Definitions [F.6](#algebra-definition-smooth) and
[F.7](#algebra-definition-smooth-at-prime)
we see that $(I/I^2)_a \to \bigoplus A_a\text{d}x_i$
is a split injection for some $a \in A$, $a \not \in \mathfrak q$.
After renumbering $x_1, \ldots, x_n$ and $f_1, \ldots, f_m$ we may
assume that $f_1, \ldots, f_c$ form a basis for
the vector space $I/I^2 \otimes_A \kappa(\mathfrak q)$ and that
$\text{d}x_{c + 1}, \ldots, \text{d}x_n$ map to a basis of
$\Omega_{A/R} \otimes_A \kappa(\mathfrak q)$. Hence after replacing $a$
by $aa'$ for some $a' \in A$, $a' \not \in \mathfrak q$ we may assume
$f_1, \ldots, f_c$ form a basis for $(I/I^2)_a$ and that
$\text{d}x_{c + 1}, \ldots, \text{d}x_n$ map to a basis of
$(\Omega_{A/R})_a$. In this situation $a^N$ for some large integer
$N$ satisfies the conditions of the lemma (with $U = V = \{1, \ldots, c\}$).
 ∎

We will use the notion of a *strictly standard* element in
$A$ over $R$. We also define an *elementary standard* element to be one of the type we found in the lemma above.
We compare the different types of elements in
Lemma [D.15](#smoothing-lemma-compare-standard).

<a id="smoothing-definition-strictly-standard"></a>

#### Definition D.3: strictly standard

*Adapted from the Stacks project, smoothing.tex, lines 191–222.*

Let $R \to A$ be a ring map of finite presentation.
We say an element $a \in A$ is *elementary standard in $A$ over $R$*
if there exists a presentation
$A = R[x_1, \ldots, x_n]/(f_1, \ldots, f_m)$
and $0 \leq c \leq \min(n, m)$ such that

<a id="equation-elementary-standard-one"></a>

$$
a = a' \det(\partial f_j/\partial x_i)_{i, j = 1, \ldots, c}\tag{D.3e1}
$$

for some $a' \in A$ and

<a id="equation-elementary-standard-two"></a>

$$
a f_{c + j} \in (f_1, \ldots, f_c) + (f_1, \ldots, f_m)^2\tag{D.3e2}
$$

for $j = 1, \ldots, m - c$. We say $a \in A$ is
*strictly standard in $A$ over $R$* if there exists a presentation
$A = R[x_1, \ldots, x_n]/(f_1, \ldots, f_m)$
and $0 \leq c \leq \min(n, m)$ such that

<a id="equation-strictly-standard-one"></a>

$$
a = \sum\nolimits_{I \subset \{1, \ldots, n\},\ |I| = c}
a_I \det(\partial f_j/\partial x_i)_{j = 1, \ldots, c,\ i \in I}\tag{D.3s1}
$$

for some $a_I \in A$ and

<a id="equation-strictly-standard-two"></a>

$$
a f_{c + j} \in (f_1, \ldots, f_c) + (f_1, \ldots, f_m)^2\tag{D.3s2}
$$

for $j = 1, \ldots, m - c$.

The following lemma is useful to find implications of
([D.3s1: strict Jacobian-minor condition](#equation-strictly-standard-one)).

<a id="smoothing-lemma-parse-equation-strictly-standard-one"></a>

#### Lemma D.4: parse equation strictly standard one

*Adapted from the Stacks project, smoothing.tex, lines 228–250.*

Let $R$ be a ring. Let $A = R[x_1, \ldots, x_n]/(f_1, \ldots, f_m)$
and write $I = (f_1, \ldots, f_m)$. Let $a \in A$. Then
([D.3s1: strict Jacobian-minor condition](#equation-strictly-standard-one)) implies
there exists an $A$-linear map
$\psi : \bigoplus\nolimits_{i = 1, \ldots, n} A \text{d}x_i \to A^{\oplus c}$
such that the composition

$$
A^{\oplus c} \xrightarrow{(f_1, \ldots, f_c)}
I/I^2 \xrightarrow{f \mapsto \text{d}f}
\bigoplus\nolimits_{i = 1, \ldots, n} A \text{d}x_i
\xrightarrow{\psi}
A^{\oplus c}
$$

is multiplication by $a$. Conversely, if such a $\psi$ exists, then
$a^c$ satisfies ([D.3s1: strict Jacobian-minor condition](#equation-strictly-standard-one)). The relation condition [D.3s2](#equation-strictly-standard-two) is a separate hypothesis. This includes $c=0$: the empty minor is $1$ and the module map is the unique map between zero modules.

**Proof.** Let $M$ be the $n\times c$ differential matrix, with entry $M_{ij}=\partial f_j/\partial x_i$. The $c\times c$ minor on rows indexed by $U$ has the determinant in D.3s1: transposing a square matrix preserves its determinant by reindexing the signed permutation expansion. Thus D.3s1 says that $a$ belongs to the ideal of these minors. Lemma [F.70](#algebra-lemma-matrix-left-inverse), proved below over arbitrary commutative rings, supplies a $c\times n$ matrix $B$ with $BM=a1_c$. This is the required map $\psi$. Conversely the displayed composite being $a1_c$ says $BM=a1_c$, and the same lemma puts $a^c$ in the minor ideal, which is exactly D.3s1 for $a^c$. No relation among the remaining generators is used in this matrix assertion. ∎

<a id="smoothing-lemma-elkik"></a>

#### Lemma D.5: elkik

*Adapted from the Stacks project, smoothing.tex, lines 252–283.*

Let $R \to A$ be a ring map of finite presentation.
The singular ideal $H_{A/R}$ is the radical of the ideal
generated by strictly standard elements in $A$ over $R$
and also the radical of the ideal generated by elementary
standard elements in $A$ over $R$.

**Proof.** 
Assume $a$ is strictly standard in $A$ over $R$. We claim that
$A_a$ is smooth over $R$, which proves that $a \in H_{A/R}$. Namely,
let $A = R[x_1, \ldots, x_n]/(f_1, \ldots, f_m)$ and $c$
be as in Definition [D.3](#smoothing-definition-strictly-standard).
Write $I = (f_1, \ldots, f_m)$ so that the naive cotangent
complex of $A$ over $R$ is given by $I/I^2 \to \bigoplus A\text{d}x_i$.
Assumption ([D.3s2: strict relation condition](#equation-strictly-standard-two))
implies that $(I/I^2)_a$ is generated by the classes of $f_1, \ldots, f_c$.
Assumption ([D.3s1: strict Jacobian-minor condition](#equation-strictly-standard-one)) implies
that the differential $(I/I^2)_a \to \bigoplus A_a\text{d}x_i$
has a left inverse, see
Lemma [D.4](#smoothing-lemma-parse-equation-strictly-standard-one).
Hence $R \to A_a$ is smooth by definition and
Algebra, Lemma [F.65](#algebra-lemma-localize-NL).

Let $H_e, H_s \subset A$ be the radical of the ideal generated by
elementary, resp.\ strictly standard elements of $A$ over $R$.
By definition and what we just proved we have
$H_e \subset H_s \subset H_{A/R}$. The inclusion $H_{A/R} \subset H_e$
follows from Lemma [D.2](#smoothing-lemma-find-strictly-standard).
 ∎

<a id="smoothing-example-not-quasi-compact"></a>

#### Example D.6: not quasi compact

*Adapted from the Stacks project, smoothing.tex, lines 285–292.*

The set of points where a finitely presented ring map is smooth
needn't be a quasi-compact open. For example, let
$R = k[x, y_1, y_2, y_3, \ldots]/(xy_i)$ and $A = R/(x)$.
Then the smooth locus of $R \to A$ is
$\bigcup D(y_i)$ which is not quasi-compact.

<a id="smoothing-lemma-strictly-standard-base-change"></a>

#### Lemma D.7: strictly standard base change

*Adapted from the Stacks project, smoothing.tex, lines 294–309.*

Let $R \to A$ be a ring map of finite presentation.
Let $R \to R'$ be a ring map. If $a \in A$ is elementary,
resp.\ strictly standard in $A$ over $R$, then $a \otimes 1$
is elementary, resp.\ strictly standard in $A \otimes_R R'$ over $R'$.

**Proof.** 
If $A = R[x_1, \ldots, x_n]/(f_1, \ldots, f_m)$ is a presentation
of $A$ over $R$, then
$A \otimes_R R' = R'[x_1, \ldots, x_n]/(f'_1, \ldots, f'_m)$
is a presentation of $A \otimes_R R'$ over $R'$. Here $f'_j$ is
the image of $f_j$ in $R'[x_1, \ldots, x_n]$.
Hence the result follows from the definitions.
 ∎

<a id="smoothing-lemma-final-solve"></a>

#### Lemma D.8: final solve

*Adapted from the Stacks project, smoothing.tex, lines 311–327.*

Let $R \to A \to \Lambda$ be ring maps with $A$ of finite presentation
over $R$. Assume that $H_{A/R} \Lambda = \Lambda$. Then there exists
a factorization $A \to B \to \Lambda$ with $B$ smooth over $R$.

**Proof.** 
Choose $f_1, \ldots, f_r \in H_{A/R}$ and
$\lambda_1, \ldots, \lambda_r \in \Lambda$ such that
$\sum f_i\lambda_i = 1$ in $\Lambda$. Set
$B = A[x_1, \ldots, x_r]/(f_1x_1 + \ldots + f_rx_r - 1)$
and define $B \to \Lambda$ by mapping $x_i$ to $\lambda_i$.
To check that $B$ is smooth over $R$ use that $A_{f_i}$ is smooth
over $R$ by definition of $H_{A/R}$ and that $B_{f_i}$ is smooth
over $A_{f_i}$. Explicitly, in

$$
B=A[t_1,\ldots,t_r]/(\sum_i f_it_i-1)
$$

the equality $\sum_i f_it_i=1$ makes the opens $D(f_i)$ cover $\operatorname{Spec}(B)$. On $D(f_i)$ the defining equation uniquely eliminates $t_i$, giving

$$
B_{f_i}\cong A_{f_i}[t_1,\ldots,\widehat{t_i},\ldots,t_r].
$$

Each of these algebras is smooth over $R$, because $A_{f_i}$ is smooth. Smoothness is local on the target, so $B$ is smooth. The given relation $\sum_i f_i\lambda_i=1$ defines the map $B\to\Lambda$, $t_i\mapsto\lambda_i$, and the factorization.
 ∎

### Presentations of algebras

<a id="smoothing-section-presentations"></a>

Some of the results in this section are due to Elkik. Note that the algebra
$C$ in the following lemma is a symmetric algebra over $A$. Moreover, if
$R$ is Noetherian, then $C$ is of finite presentation over $R$.

<a id="smoothing-lemma-improve-presentation"></a>

#### Lemma D.9: improve presentation

*Adapted from the Stacks project, smoothing.tex, lines 341–439.*

Let $R$ be a ring and let $A$ be a finitely presented $R$-algebra.
There exists a finite type $R$-algebra map $A \to C$ which has a
retraction with the following two properties

1. for each $a \in A$ such that $R \to A_a$ is a local complete
intersection (More on Algebra, Definition
[F.94](#more-algebra-definition-local-complete-intersection))
the ring $C_a$ is smooth over $A_a$ and has a presentation
$C_a = R[y_1, \ldots, y_m]/J$ such that $J/J^2$ is free over $C_a$, and

1. for each $a \in A$ such that $A_a$ is smooth over $R$ the
module $\Omega_{C_a/R}$ is free over $C_a$.

**Proof.**
Choose a presentation $A=R[x_1,\ldots,x_n]/I$ with
$I=(f_1,\ldots,f_m)$, and set $M=I/I^2$. Define $K$ by

$$
0\longrightarrow K\longrightarrow A^{\oplus m}\longrightarrow M
\longrightarrow0,
\qquad e_j\longmapsto f_j\bmod I^2.
$$

Put $C=\operatorname{Sym}_A(M)$. Projection onto degree zero is the
required retraction. The surjection
$R[x_1,\ldots,x_n,y_1,\ldots,y_m]\to C$ sends $y_j$ to the class of
$f_j$. Its kernel $J$ is generated by the $f_j$ and the linear forms
$\sum h_jy_j$ whose coefficient classes $(h_j\bmod I)$ belong to $K$.
This follows directly from the universal property of the symmetric
algebra. In particular $C$ is of finite type over $A$.

Let $h\in R[x_1,\ldots,x_n]$ have image $a\in A$. Use the presentations

$$
A_a=R[x_0,x_1,\ldots,x_n]/I',
\qquad
C_a=R[x_0,x_1,\ldots,x_n,y_1,\ldots,y_m]/J',
$$

where $I'=(hx_0-1,I)$ and $J'=(hx_0-1,J)$. The principal-localization
conormal calculation [F.72](#algebra-lemma-principal-localization-NL)
gives

$$
I'/(I')^2=A_a\oplus M_a,\qquad
J'/(J')^2=C_a\oplus(J/J^2)_a.
$$

Now assume that $A_a$ is a local complete intersection over $R$.
The Koszul-regular local equation lists make $M_a$ locally free.
Indeed, if $(g_i)$ is such a list, a conormal relation
$\sum b_i g_i\in (g)^2$ can first be corrected by coefficients in $(g)$
to an exact relation. Its coefficients are then Koszul boundaries,
by vanishing of first Koszul homology, and hence all belong to $(g)$.
Thus the equation classes form a free conormal basis. Choose a finite
principal cover trivializing $M_a$, using quasi-compactness of its
spectrum. On each chart the kernel $K_a$ of the finite free surjection
onto $M_a$ is a finite direct summand. Clear denominators of these
finitely many chart generators and collect them in $K_a$; their
cokernel vanishes on the cover, so they generate $K_a$ globally.
Consequently $M_a$ is finitely presented. It is flat, because each
ideal tensor map is injective on that same free cover and local
detection proves its global injectivity. The finite-presentation
projectivity theorem [AG-CA-07, Theorem 5.3](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/tor-and-flat-modules.html)
therefore makes $M_a$ finite projective.
The displayed defining sequence of $K$ splits after localization, so
$K_a$ is finite projective and $K_a\oplus M_a\cong A_a^{\oplus m}$.
Only at this point do we apply the symmetric-algebra conormal identity:
the finite-projective quotient hypothesis in
[F.102](#more-algebra-lemma-cotangent-complex-symmetric-algebra)
identifies the conormal module of $A_a[y_j]\to C_a$ with
$K_a\otimes_{A_a}C_a$. Also $C_a=\operatorname{Sym}_{A_a}(M_a)$ is smooth
over $A_a$ by [F.128](#more-algebra-lemma-symmetric-algebra-smooth).
On principal neighborhoods trivializing $K_a$ and $M_a$, the coordinates
in [F.102](#more-algebra-lemma-cotangent-complex-symmetric-algebra) make
the kernel of $A_a[y_j]\to C_a$ an ideal generated by polynomial
variables. That is a regular sequence, so its first Koszul homology
vanishes by the exterior-complex cone calculation. Thus the exact
conormal injectivity theorem [F.130](#more-algebra-lemma-transitive-lci-at-end)
applies to this particular presentation.
The transitivity conormal sequence
[F.42](#algebra-lemma-exact-sequence-NL) for the localized presentations,
with left injectivity supplied by
[F.130](#more-algebra-lemma-transitive-lci-at-end), is therefore

$$
0\longrightarrow C_a\oplus(M\otimes_A C_a)
\longrightarrow C_a\oplus(J/J^2)_a
\longrightarrow K_a\otimes_{A_a}C_a\longrightarrow0.
$$

The right module is projective, so this sequence splits and gives

$$
J'/(J')^2\cong C_a\oplus(M_a\oplus K_a)\otimes_{A_a}C_a
\cong C_a^{\oplus(m+1)}.
$$

This proves (1), including the asserted smoothness over $A_a$.

If $A_a$ is smooth over $R$, its conormal sequence for the original
$n$ variables is split exact by the smoothness definition
[F.6](#algebra-definition-smooth). It makes $M_a$ finite projective and
gives $M_a\oplus\Omega_{A_a/R}\cong A_a^{\oplus n}$ independently of
(1). Now [F.128](#more-algebra-lemma-symmetric-algebra-smooth) and
[F.102](#more-algebra-lemma-cotangent-complex-symmetric-algebra) apply:
$\Omega_{C_a/A_a}=M_a\otimes_{A_a}C_a$ and
$H_1(L_{C_a/A_a})=0$. Thus
[F.42](#algebra-lemma-exact-sequence-NL) gives

$$
0\longrightarrow\Omega_{A_a/R}\otimes_{A_a}C_a
\longrightarrow\Omega_{C_a/R}
\longrightarrow M_a\otimes_{A_a}C_a\longrightarrow0.
$$

The right module is projective, so this sequence splits. Combining
it with the preceding split conormal identity gives

$$
\Omega_{C_a/R}\cong
(M_a\oplus\Omega_{A_a/R})\otimes_{A_a}C_a
\cong C_a^{\oplus n},
$$

which proves (2). ∎

<a id="smoothing-proposition-lift-smooth"></a>

#### Proposition D.10: lift smooth

*Adapted from the Stacks project, smoothing.tex, lines 447–557.*

Let $R \to R_0$ be a surjective map of Noetherian rings with kernel $I$.
This is the auxiliary lifting scope consumed by the Noetherian
desingularization argument below.

1. If $R_0 \to A_0$ is a syntomic ring map, then there exists a syntomic
ring map $R \to A$ such that $A/IA \cong A_0$.

1. If $R_0 \to A_0$ is a smooth ring map, then there exists a smooth
ring map $R \to A$ such that $A/IA \cong A_0$.

**Proof.** 
Assume $R_0 \to A_0$ syntomic, in particular a local complete intersection
(More on Algebra, Lemma [F.129](#more-algebra-lemma-syntomic-lci)).
Choose a presentation $A_0 = R_0[x_1, \ldots, x_n]/J_0$. Set
$C_0 = \text{Sym}^*_{A_0}(J_0/J_0^2)$. Note that $J_0/J_0^2$ is a finite
projective $A_0$-module (Algebra, Lemma
[F.88](#algebra-lemma-syntomic-presentation-ideal-mod-squares)).
By Lemma [D.9](#smoothing-lemma-improve-presentation) the ring map
$A_0 \to C_0$ is smooth and we can find a presentation
$C_0 = R_0[y_1, \ldots, y_m]/K_0$ with $K_0/K_0^2$ free over $C_0$.
By Algebra, Lemma [F.55](#algebra-lemma-huber) we can assume
$C_0 = R_0[y_1, \ldots, y_m]/(\overline{f}_1, \ldots, \overline{f}_c)$
where $\overline{f}_1, \ldots, \overline{f}_c$ maps to a basis of
$K_0/K_0^2$ over $C_0$. Choose
$f_1, \ldots, f_c \in R[y_1, \ldots, y_m]$ lifting
$\overline{f}_1, \ldots, \overline{f}_c$ and set

$$
C = R[y_1, \ldots, y_m]/(f_1, \ldots, f_c)
$$

By construction $C_0 = C/IC$. By Algebra, Lemma
[F.66](#algebra-lemma-localize-relative-complete-intersection)
we can after replacing $C$ by $C_g$ assume that $C$ is a relative
global complete intersection over $R$.
We conclude that there exists a finite projective $A_0$-module
$P_0$ such that $C_0 = \text{Sym}^*_{A_0}(P_0)$
is isomorphic to $C/IC$ for some syntomic $R$-algebra $C$.

Choose an integer $n$ and a direct sum decomposition
$A_0^{\oplus n} = P_0 \oplus Q_0$.
By More on Algebra, Lemma [F.117](#more-algebra-lemma-lift-projective-module)
we can find an étale ring map $C \to C'$ which induces
an isomorphism $C/IC \to C'/IC'$ and a finite projective
$C'$-module $Q$ such that $Q/IQ$ is isomorphic to
$Q_0 \otimes_{A_0} C/IC$.
Then $D = \text{Sym}_{C'}^*(Q)$ is a smooth $C'$-algebra (see
More on Algebra, Lemma [F.128](#more-algebra-lemma-symmetric-algebra-smooth)).
Picture

$$
\begin{gathered}
R \xrightarrow{} R/I \\
R \xrightarrow{} C \\
C \xrightarrow{} C' \\
C \xrightarrow{} C/IC \\
C' \xrightarrow{} D \\
C' \xrightarrow{} C'/IC' \\
D \xrightarrow{} D/ID \\
R/I \xrightarrow{} A_0 \\
A_0 \xrightarrow{} C/IC \\
C/IC \xrightarrow{\cong} C'/IC' \\
C'/IC' \xrightarrow{} D/ID
\end{gathered}
$$

Observe that our choice of $Q$ gives

$$
\begin{aligned}
D/ID & =
\text{Sym}_{C/IC}^*(Q_0 \otimes_{A_0} C/IC) \\
& =
\text{Sym}_{A_0}^*(Q_0) \otimes_{A_0} C/IC \\
& =
\text{Sym}_{A_0}^*(Q_0) \otimes_{A_0}
\text{Sym}_{A_0}^*(P_0) \\
& =
\text{Sym}_{A_0}^*(Q_0 \oplus P_0) \\
& =
\text{Sym}_{A_0}^*(A_0^{\oplus n}) \\
& =
A_0[x_1, \ldots, x_n]
\end{aligned}
$$

Choose $f_1, \ldots, f_n \in D$ which map to $x_1, \ldots, x_n$
in $D/ID = A_0[x_1, \ldots, x_n]$. Set $A = D/(f_1, \ldots, f_n)$.
Note that $A_0 = A/IA$. We claim that $R \to A$ is syntomic
in a neighbourhood of $V(IA)$. If the claim is true, then we can
find a $f \in A$ mapping to $1 \in A_0$ such that $A_f$ is syntomic
over $R$ and the proof of (1) is finished.

Proof of the claim. Observe that $R \to D$ is syntomic as a composition
of the syntomic ring map $R \to C$, the étale ring map $C \to C'$ and the
smooth ring map $C' \to D$ (Algebra, Lemmas
[F.32](#algebra-lemma-composition-syntomic) and
[F.83](#algebra-lemma-smooth-syntomic)).
The question is local on $\operatorname{Spec}(D)$, hence we
may assume that $D$ is a relative global complete intersection
(Algebra, Lemma [F.87](#algebra-lemma-syntomic)).
Say $D = R[y_1, \ldots, y_m]/(g_1, \ldots, g_s)$.
Let $f'_1, \ldots, f'_n \in R[y_1, \ldots, y_m]$ be lifts of
$f_1, \ldots, f_n$. Then we can apply
Algebra, Lemma [F.66](#algebra-lemma-localize-relative-complete-intersection)
to get the claim.

Proof of (2). Since a smooth ring map is syntomic, we can find
a syntomic ring map $R \to A$ such that $A_0 = A/IA$.
By assumption the fibres of $R \to A$ are smooth over primes in $V(I)$
hence $R \to A$ is smooth in an open neighbourhood of $V(IA)$
(Algebra, Lemma [F.45](#algebra-lemma-flat-fibre-smooth)).
Thus we can replace $A$ by a localization to obtain the result we want.
 ∎

We know that any syntomic ring map $R \to A$ is locally a relative global
complete intersection, see
Algebra, Lemma [F.87](#algebra-lemma-syntomic).
The next lemma says that a vector bundle over $\operatorname{Spec}(A)$ is
a relative global complete intersection.

<a id="smoothing-lemma-syntomic-complete-intersection"></a>

#### Lemma D.11: syntomic complete intersection

*Adapted from the Stacks project, smoothing.tex, lines 566–587.*

Let $R \to A$ be a syntomic ring map. Then there exists a smooth $R$-algebra
map $A \to C$ with a retraction such that $C$ is a global relative complete
intersection over $R$, i.e.,

$$
C \cong R[x_1, \ldots, x_n]/(f_1, \ldots, f_c)
$$

flat over $R$ and all fibres of dimension $n - c$.

**Proof.** 
Apply Lemma [D.9](#smoothing-lemma-improve-presentation) to get $A \to C$.
By Algebra, Lemma [F.55](#algebra-lemma-huber)
we can write $C = R[x_1, \ldots, x_n]/(f_1, \ldots, f_c)$
with $f_i$ mapping to a basis of $J/J^2$.
The ring map $R \to C$ is syntomic (hence flat)
as it is a composition of a syntomic and a smooth ring map.
The dimension of the fibres is $n - c$ by
Algebra, Lemma [F.57](#algebra-lemma-lci)
(the fibres are local complete intersections, so the lemma applies).
 ∎

<a id="smoothing-lemma-smooth-standard-smooth"></a>

#### Lemma D.12: smooth standard smooth

*Adapted from the Stacks project, smoothing.tex, lines 589–672.*

Let $R \to A$ be a smooth ring map. Then there exists a smooth $R$-algebra
map $A \to B$ with a retraction such that $B$ is standard smooth over
$R$, i.e.,

$$
B \cong R[x_1, \ldots, x_n]/(f_1, \ldots, f_c)
$$

and $\det(\partial f_j/\partial x_i)_{i, j = 1, \ldots, c}$
is invertible in $B$.

**Proof.** 
Apply Lemma [D.11](#smoothing-lemma-syntomic-complete-intersection)
to get a smooth $R$-algebra map $A \to C$ with a retraction such that
$C = R[x_1, \ldots, x_n]/(f_1, \ldots, f_c)$
is a relative global complete intersection over $R$. As $C$ is smooth
over $R$ we have a short exact sequence

$$
0 \to
\bigoplus\nolimits_{j = 1, \ldots, c} C f_j \to
\bigoplus\nolimits_{i = 1, \ldots, n} C\text{d}x_i \to
\Omega_{C/R} \to 0
$$

Since $\Omega_{C/R}$ is a projective $C$-module this sequence is split.
Choose a left inverse $t$ to the first map. Say
$t(\text{d}x_i) = \sum c_{ij} f_j$
so that $\sum_i \frac{\partial f_j}{\partial x_i} c_{i\ell} = \delta_{j\ell}$
(Kronecker delta). Let

$$
B' = C[y_1, \ldots, y_c] =
R[x_1, \ldots, x_n, y_1, \ldots, y_c]/(f_1, \ldots, f_c)
$$

The $R$-algebra map $C \to B'$ has a retraction given by mapping $y_j$ to zero.
We claim that the map

$$
R[z_1, \ldots, z_n] \longrightarrow B',\quad
z_i \longmapsto x_i - \sum\nolimits_j c_{ij} y_j
$$

is étale at every point in the image of $\operatorname{Spec}(C) \to \operatorname{Spec}(B')$.
In $\Omega_{B'/R[z_1, \ldots, z_n]}$ we have

$$
0 =
\text{d}f_j - \sum\nolimits_i \frac{\partial f_j}{\partial x_i} \text{d}z_i
\equiv
\sum\nolimits_{i, \ell}
\frac{\partial f_j}{\partial x_i} c_{i\ell} \text{d}y_\ell
\equiv
\text{d}y_j \bmod (y_1, \ldots, y_c)\Omega_{B'/R[z_1, \ldots, z_n]}
$$

Since $0 = \text{d}z_i = \text{d}x_i$ modulo
$\sum B'\text{d}y_j + (y_1, \ldots, y_c)\Omega_{B'/R[z_1, \ldots, z_n]}$
we conclude that

$$
\Omega_{B'/R[z_1, \ldots, z_n]}/
(y_1, \ldots, y_c)\Omega_{B'/R[z_1, \ldots, z_n]} = 0.
$$

As $\Omega_{B'/R[z_1, \ldots, z_n]}$ is a finite $B'$-module
by Nakayama's lemma there exists a $g \in 1 + (y_1, \ldots, y_c)$
that $(\Omega_{B'/R[z_1, \ldots, z_n]})_g = 0$. This proves that
$R[z_1, \ldots, z_n] \to B'_g$ is unramified, see
Algebra, Definition [F.8](#algebra-definition-unramified).
For any ring map $R \to k$ where $k$ is a field we obtain an
unramified ring map $k[z_1, \ldots, z_n] \to (B'_g) \otimes_R k$
between smooth $k$-algebras of dimension $n$. It follows that
$k[z_1, \ldots, z_n] \to (B'_g) \otimes_R k$ is flat by
Algebra, Lemmas [F.9](#algebra-lemma-CM-over-regular-flat) and
[F.18](#algebra-lemma-characterize-smooth-kbar). By the crit\`ere
de platitude par fibre
(Algebra, Lemma [F.36](#algebra-lemma-criterion-flatness-fibre))
we conclude that $R[z_1, \ldots, z_n] \to B'_g$ is flat.
Finally, Algebra, Lemma [F.16](#algebra-lemma-characterize-etale)
implies that $R[z_1, \ldots, z_n] \to B'_g$ is étale.
Set $B = B'_g$. Note that $C \to B$ is smooth and has a retraction,
so also $A \to B$ is smooth and has a retraction.
Moreover, $R[z_1, \ldots, z_n] \to B$ is étale.
By Algebra, Lemma [F.41](#algebra-lemma-etale-standard-smooth)
we can write

$$
B = R[z_1, \ldots, z_n, w_1, \ldots, w_m]/(g_1, \ldots, g_m)
$$

with $\det(\partial g_j/\partial w_i)$ invertible in $B$.
This proves the lemma.
 ∎

<a id="smoothing-lemma-colimit-standard-smooth"></a>

#### Lemma D.13: colimit standard smooth

*Adapted from the Stacks project, smoothing.tex, lines 674–691.*

Let $R \to \Lambda$ be a ring map. If $\Lambda$ is a filtered colimit of
smooth $R$-algebras, then $\Lambda$ is a filtered colimit of standard
smooth $R$-algebras.

**Proof.** 
Let $A \to \Lambda$ be an $R$-algebra map with $A$
of finite presentation over $R$. According to
Algebra, Lemma [F.90](#algebra-lemma-when-colimit)
we have to factor this map through a standard smooth algebra, and
we know we can factor it as $A \to B \to \Lambda$ with $B$ smooth
over $R$. Choose an $R$-algebra map $B \to C$ with a retraction
$C \to B$ such that $C$ is standard smooth over $R$, see
Lemma [D.12](#smoothing-lemma-smooth-standard-smooth).
Then the desired factorization is $A \to B \to C \to B \to \Lambda$.
 ∎

<a id="smoothing-lemma-standard-smooth-include-generators"></a>

#### Lemma D.14: standard smooth include generators

*Adapted from the Stacks project, smoothing.tex, lines 693–716.*

Let $R \to A$ be a standard smooth ring map.
Let $E \subset A$ be a finite subset of order $|E| = n$.
Then there exists a presentation
$A = R[x_1, \ldots, x_{n + m}]/(f_1, \ldots, f_c)$ with $c \geq n$,
with $\det(\partial f_j/\partial x_i)_{i, j = 1, \ldots, c}$
invertible in $A$, and such that $E$ is the set of congruence classes of
$x_1, \ldots, x_n$.

**Proof.** 
Choose a presentation $A = R[y_1, \ldots, y_m]/(g_1, \ldots, g_d)$
such that the image of
$\det(\partial g_j/\partial y_i)_{i, j = 1, \ldots, d}$
is invertible in $A$. Choose an enumeration $E = \{a_1, \ldots, a_n\}$
and choose $h_i \in R[y_1, \ldots, y_m]$ whose image in $A$ is $a_i$.
Consider the presentation

$$
A = R[x_1, \ldots, x_n, y_1, \ldots, y_m]/
(x_1 - h_1, \ldots, x_n - h_n, g_1, \ldots, g_d)
$$

and set $c = n + d$.
 ∎

<a id="smoothing-lemma-compare-standard"></a>

#### Lemma D.15: compare standard

*Adapted from the Stacks project, smoothing.tex, lines 718–850.*

Let $R \to A$ be a ring map of finite presentation.
Let $a \in A$. Consider the following conditions on $a$:

1. $A_a$ is smooth over $R$,

1. $A_a$ is smooth over $R$ and $\Omega_{A_a/R}$ is stably free,

1. $A_a$ is smooth over $R$ and $\Omega_{A_a/R}$ is free,

1. $A_a$ is standard smooth over $R$,

1. $a$ is strictly standard in $A$ over $R$,

1. $a$ is elementary standard in $A$ over $R$.

Then we have

1. **(a)** (4) $\Rightarrow$ (3) $\Rightarrow$ (2) $\Rightarrow$ (1),

1. **(b)** (6) $\Rightarrow$ (5),

1. **(c)** (6) $\Rightarrow$ (4),

1. **(d)** (5) $\Rightarrow$ (2),

1. **(e)** (2) $\Rightarrow$ the elements $a^e$, $e \geq e_0$ are
strictly standard in $A$ over $R$,

1. **(f)** (4) $\Rightarrow$ the elements $a^e$, $e \geq e_0$ are
elementary standard in $A$ over $R$.

**Proof.** 
Part (a) is clear from the definitions and
Algebra, Lemma [F.85](#algebra-lemma-standard-smooth).
Part (b) is clear from Definition [D.3](#smoothing-definition-strictly-standard).

Proof of (c). Choose a presentation
$A = R[x_1, \ldots, x_n]/(f_1, \ldots, f_m)$ such that
([D.3e1: elementary Jacobian-minor condition](#equation-elementary-standard-one)) and
([D.3e2: elementary relation condition](#equation-elementary-standard-two)) hold.
Choose $h \in R[x_1, \ldots, x_n]$ mapping to $a$. Then

$$
A_a = R[x_0, x_1, \ldots, x_n]/(x_0h - 1, f_1, \ldots, f_m).
$$

Write $J = (x_0h - 1, f_1, \ldots, f_m)$.
By ([D.3e2: elementary relation condition](#equation-elementary-standard-two)) we see that the $A_a$-module
$J/J^2$ is generated by $x_0h - 1, f_1, \ldots, f_c$
over $A_a$. Hence, as in the proof of Algebra, Lemma [F.55](#algebra-lemma-huber),
we can choose a $g \in 1 + J$ such that

$$
A_a = R[x_0, \ldots, x_n, x_{n + 1}]/
(x_0h - 1, f_1, \ldots, f_c, gx_{n + 1} - 1).
$$

At this point ([D.3e1: elementary Jacobian-minor condition](#equation-elementary-standard-one))
implies that $R \to A_a$ is standard smooth (use the coordinates
$x_0, x_1, \ldots, x_c, x_{n + 1}$ to take derivatives).

Proof of (d). Choose a presentation
$A = R[x_1, \ldots, x_n]/(f_1, \ldots, f_m)$ such that
([D.3s1: strict Jacobian-minor condition](#equation-strictly-standard-one)) and
([D.3s2: strict relation condition](#equation-strictly-standard-two)) hold.
Write $I = (f_1, \ldots, f_m)$.
We already know that $A_a$ is smooth over $R$, see
Lemma [D.5](#smoothing-lemma-elkik). By
Lemma [D.4](#smoothing-lemma-parse-equation-strictly-standard-one)
we see that $(I/I^2)_a$ is free on $f_1, \ldots, f_c$
and maps isomorphically to a direct summand of
$\bigoplus A_a \text{d}x_i$. Since
$\Omega_{A_a/R} = (\Omega_{A/R})_a$
is the cokernel of the map
$(I/I^2)_a \to \bigoplus A_a \text{d}x_i$
we conclude that it is stably free.

Proof of (e). Choose a presentation
$A = R[x_1, \ldots, x_n]/I$ with $I$ finitely generated.
By assumption we have a short exact sequence

$$
0 \to (I/I^2)_a \to \bigoplus\nolimits_{i = 1, \ldots, n} A_a\text{d}x_i \to
\Omega_{A_a/R} \to 0
$$

which is split exact. Hence we see that
$(I/I^2)_a \oplus \Omega_{A_a/R}$ is a free $A_a$-module.
Since $\Omega_{A_a/R}$ is stably free we see that $(I/I^2)_a$
is stably free as well. Thus replacing the presentation chosen
above by $A = R[x_1, \ldots, x_n, x_{n + 1}, \ldots, x_{n + r}]/J$ with
$J = (I, x_{n + 1}, \ldots, x_{n + r})$ for some $r$ we get that $(J/J^2)_a$
is (finite) free. Choose $f_1, \ldots, f_c \in J$ which map to a basis of
$(J/J^2)_a$. Extend this to a list of generators
$f_1, \ldots, f_m \in J$. Consider the presentation
$A = R[x_1, \ldots, x_{n + r}]/(f_1, \ldots, f_m)$.
Then ([D.3s2: strict relation condition](#equation-strictly-standard-two)) holds for $a^e$
for all sufficiently large $e$ by construction. Moreover, since
$(J/J^2)_a \to \bigoplus\nolimits_{i = 1, \ldots, n + r} A_a\text{d}x_i$
is a split injection we can find an $A_a$-linear left inverse.
Writing this left inverse in terms of the basis $f_1, \ldots, f_c$
and clearing denominators we find a linear map
$\psi_0 : A^{\oplus n + r} \to A^{\oplus c}$ such that

$$
A^{\oplus c} \xrightarrow{(f_1, \ldots, f_c)}
J/J^2 \xrightarrow{f \mapsto \text{d}f}
\bigoplus\nolimits_{i = 1, \ldots, n + r} A \text{d}x_i
\xrightarrow{\psi_0}
A^{\oplus c}
$$

is multiplication by $a^{e_0}$ for some $e_0 \geq 1$. By
Lemma [D.4](#smoothing-lemma-parse-equation-strictly-standard-one)
we see ([D.3s1: strict Jacobian-minor condition](#equation-strictly-standard-one))
holds for all $a^{ce_0}$ and hence for $a^e$ for all $e$ with $e \geq ce_0$.

Proof of (f). Choose a presentation
$A_a = R[x_1, \ldots, x_n]/(f_1, \ldots, f_c)$ such that
$\det(\partial f_j/\partial x_i)_{i, j = 1, \ldots, c}$
is invertible in $A_a$. We may assume that for some
$m < n$ the classes of the elements $x_1, \ldots, x_m$
correspond to $a_i/1$ where $a_1, \ldots, a_m \in A$ are generators of $A$
over $R$, see Lemma [D.14](#smoothing-lemma-standard-smooth-include-generators).
After replacing $x_i$ by $a^Nx_i$ for $m < i \leq n$
we may assume the class of $x_i$ is $a_i/1 \in A_a$ for some
$a_i \in A$. Consider the ring map

$$
\Psi : R[x_1, \ldots, x_n] \longrightarrow A,\quad
x_i \longmapsto a_i.
$$

This is a surjective ring map. By replacing $f_j$ by $a^Nf_j$ we may
assume that $f_j \in R[x_1, \ldots, x_n]$ and that
$\Psi(f_j) = 0$ (since after all $f_j(a_1/1, \ldots, a_n/1) = 0$
in $A_a$). Let $J = \ker(\Psi)$. Then $A = R[x_1, \ldots, x_n]/J$
is a presentation and $f_1, \ldots, f_c \in J$ are elements such that
$(J/J^2)_a$ is freely generated by $f_1, \ldots, f_c$ and such
that $\det(\partial f_j/\partial x_i)_{i, j = 1, \ldots, c}$
maps to an invertible element of $A_a$. It follows that
([D.3e1: elementary Jacobian-minor condition](#equation-elementary-standard-one)) and
([D.3e2: elementary relation condition](#equation-elementary-standard-two))
hold for $a^e$ and all large enough $e$ as desired.
 ∎

### The lifting problem

<a id="smoothing-section-lifting"></a>

The goal in this section is to prove (Proposition [D.18](#smoothing-proposition-lift))
that the collection of algebras which are filtered colimits of smooth algebras
is closed under infinitesimal flat deformations. The proof is elementary
and only uses the results on presentations of smooth algebras from
Section [§ presentations](#smoothing-section-presentations).

<a id="smoothing-lemma-lift-once"></a>

#### Lemma D.16: lift once

*Adapted from the Stacks project, smoothing.tex, lines 1237–1305.*

Let $R \to \Lambda$ be a ring map. Let $I \subset R$ be an ideal.
Assume that

1. $I^2 = 0$, and

1. $\Lambda/I\Lambda$ is a filtered colimit of smooth $R/I$-algebras.

Let $\varphi : A \to \Lambda$ be an $R$-algebra map with $A$ of finite
presentation over $R$. Then there exists a factorization

$$
A \to B/J \to \Lambda
$$

where $B$ is a smooth $R$-algebra and $J \subset IB$ is a finitely generated
ideal.

**Proof.** 
Choose a factorization

$$
A/IA \to \bar B \to \Lambda/I\Lambda
$$

with $\bar B$ standard smooth over $R/I$; this is possible by
assumption and Lemma [D.13](#smoothing-lemma-colimit-standard-smooth). Write

$$
\bar B = A/IA[t_1, \ldots, t_r]/(\bar g_1, \ldots, \bar g_s)
$$

and say $\bar B \to \Lambda/I\Lambda$ maps $t_i$ to the class
of $\lambda_i$ modulo $I\Lambda$. Choose
$g_1, \ldots, g_s \in A[t_1, \ldots, t_r]$ lifting
$\bar g_1, \ldots, \bar g_s$. Write
$\varphi(g_i)(\lambda_1, \ldots, \lambda_r) =
\sum \epsilon_{ij} \mu_{ij}$
for some $\epsilon_{ij} \in I$ and $\mu_{ij} \in \Lambda$. Define

$$
A' = A[t_1, \ldots, t_r, \delta_{i, j}]/
(g_i - \sum \epsilon_{ij} \delta_{ij})
$$

and consider the map

$$
A' \longrightarrow \Lambda,\quad
a \longmapsto \varphi(a),\quad
t_i \longmapsto \lambda_i,\quad
\delta_{ij} \longmapsto \mu_{ij}
$$

We have

$$
A'/IA' = A/IA[t_1, \ldots, t_r]/(\bar g_1, \ldots, \bar g_s)[\delta_{ij}]
\cong \bar B[\delta_{ij}]
$$

This is a standard smooth algebra over $R/I$ as $\bar B$ is standard
smooth. Choose a presentation
$A'/IA' = R/I[x_1, \ldots, x_n]/(\bar f_1, \ldots, \bar f_c)$ with
$\det(\partial \bar f_j/\partial x_i)_{i, j = 1, \ldots, c}$ invertible in
$A'/IA'$. Choose lifts $f_1, \ldots, f_c \in R[x_1, \ldots, x_n]$ of
$\bar f_1, \ldots, \bar f_c$. Then

$$
B = R[x_1, \ldots, x_n, x_{n + 1}]/
(f_1, \ldots, f_c,
x_{n + 1}\det(\partial f_j/\partial x_i)_{i, j = 1, \ldots, c} - 1)
$$

is smooth over $R$. Since smooth ring maps are formally smooth
(Algebra, Proposition [AG-CA-17, Theorem 3.1 and the split conormal definition of smoothness in this draft](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/formally-smooth-unramified-and-etale-ring-maps.html))
there exists an $R$-algebra map $B \to A'$ which is an isomorphism
modulo $I$. Then $B \to A'$ is surjective by Nakayama's lemma
(Algebra, Lemma [F.10](#algebra-lemma-NAK)).
Thus $A' = B/J$ with $J \subset IB$ finitely generated (see
Algebra, Lemma [F.44](#algebra-lemma-finite-presentation-independent)).
 ∎

<a id="smoothing-lemma-lift-twice"></a>

#### Lemma D.17: lift twice

*Adapted from the Stacks project, smoothing.tex, lines 1307–1371.*

Let $R \to \Lambda$ be a ring map. Let $I \subset R$ be an ideal.
Assume that

1. $I^2 = 0$,

1. $\Lambda/I\Lambda$ is a filtered colimit of smooth $R/I$-algebras, and

1. $R \to \Lambda$ is flat.

Let $\varphi : B \to \Lambda$ be an $R$-algebra map with $B$
smooth over $R$. Let $J \subset IB$ be a finitely generated ideal
such that $\varphi(J) = 0$.
Then there exists $R$-algebra maps

$$
B \xrightarrow{\alpha} B' \xrightarrow{\beta} \Lambda
$$

such that $B'$ is smooth over $R$, such that $\alpha(J) = 0$ and
such that $\beta \circ \alpha = \varphi$.

**Proof.** 
If we can prove the lemma in case $J = (h)$, then we can prove the
lemma by induction on the number of generators of $J$. Namely, suppose
that $J$ can be generated by $n$ elements $h_1, \ldots, h_n$ and the
lemma holds for all cases where $J$ is generated by $n - 1$ elements.
Then we apply the case $n = 1$ to produce $B \to B' \to \Lambda$
where the first map kills $h_n$. Then we let $J'$ be the
ideal of $B'$ generated by the images of $h_1, \ldots, h_{n - 1}$
and we apply the case for $n - 1$ to produce $B' \to B'' \to \Lambda$.
It is easy to verify that $B \to B'' \to \Lambda$ does the job.

Assume $J = (h)$ and write $h = \sum \epsilon_i b_i$
for some $\epsilon_i \in I$ and $b_i \in B$. Note that
$0 = \varphi(h) = \sum \epsilon_i \varphi(b_i)$.
As $\Lambda$ is flat over $R$, the equational criterion for
flatness (Algebra, Lemma [AG-CA-07, Theorem 5.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/tor-and-flat-modules.html))
implies that we can find $\lambda_j \in \Lambda$,
$j = 1, \ldots, m$ and $a_{ij} \in R$ such that
$\varphi(b_i) = \sum_j a_{ij} \lambda_j$ and $\sum_i \epsilon_i a_{ij} = 0$.
Set

$$
C = B[x_1, \ldots, x_m]/(b_i - \sum a_{ij} x_j)
$$

with $C \to \Lambda$ given by $\varphi$ and $x_j \mapsto \lambda_j$.
Choose a factorization

$$
C \to B'/J' \to \Lambda
$$

as in Lemma [D.16](#smoothing-lemma-lift-once). Since $B$ is smooth over $R$ we can
lift the map $B \to C \to B'/J'$ to a map $\alpha : B \to B'$. Then
$\varphi = \beta \circ \alpha$. To finish the proof we check that
$\alpha(h) = 0$. Namely, the fact that $\alpha$ lifts
$B \to C \to B'/J'$ implies that

$$
\alpha(b_i) = \sum a_{ij} \xi_j + \theta_i
$$

for some $\xi_j \in B'$ and $\theta_i \in J' \subset IB'$.
Hence we see that

$$
\alpha(h) = \alpha(\sum \epsilon_i b_i) =
\sum \epsilon_i a_{ij} \xi_j + \sum \epsilon_i \theta_i = 0
$$

because of the relations above and the fact that $I^2 = 0$.
 ∎

<a id="smoothing-proposition-lift"></a>

#### Proposition D.18: lift

*Adapted from the Stacks project, smoothing.tex, lines 1373–1407.*

Let $R \to \Lambda$ be a ring map. Let $I \subset R$ be an ideal.
Assume that

1. $I$ is nilpotent,

1. $\Lambda/I\Lambda$ is a filtered colimit of smooth $R/I$-algebras, and

1. $R \to \Lambda$ is flat.

Then $\Lambda$ is a filtered colimit of smooth $R$-algebras.

**Proof.** 
Since $I^n = 0$ for some $n$, it follows by induction on $n$ that
it suffices to consider the case where $I^2 = 0$. Let
$\varphi : A \to \Lambda$ be an $R$-algebra map with $A$ of finite
presentation over $R$. We have to find a factorization $A \to B \to \Lambda$
with $B$ smooth over $R$, see Algebra, Lemma [F.90](#algebra-lemma-when-colimit).
By Lemma [D.16](#smoothing-lemma-lift-once) we may assume that
$A = B/J$ with $B$ smooth over $R$ and $J \subset IB$
a finitely generated ideal. By
Lemma [D.17](#smoothing-lemma-lift-twice)
we can find a commutative diagram

$$
\begin{gathered}
B \xrightarrow{\alpha} B' \\
B \xrightarrow{\varphi} \Lambda \\
B' \xrightarrow{\beta} \Lambda
\end{gathered}
$$

of $R$-algebras with $B'$ smooth over $R$ such that $\alpha(J) = 0$.
Thus $\alpha$ factors as $B \to A \to B'$ and the proof is complete.
 ∎

### The lifting lemma

<a id="smoothing-section-lifting-lemma"></a>

The next lemma constructs a finite presentation lifting the smooth locus.

<a id="smoothing-lemma-lifting"></a>

#### Lemma D.19: lifting

*Adapted from the Stacks project, smoothing.tex, lines 1420–1651.*

Let $R$ be a Noetherian ring. Let $\Lambda$ be an $R$-algebra.
Let $\pi \in R$ and assume that $\text{Ann}_R(\pi) = \text{Ann}_R(\pi^2)$ and
$\text{Ann}_\Lambda(\pi) = \text{Ann}_\Lambda(\pi^2)$.
Suppose we have $R$-algebra maps
$R/\pi^2R \to \bar C \to \Lambda/\pi^2\Lambda$
with $\bar C$ of finite presentation.
Then there exists an $R$-algebra homomorphism
$D \to \Lambda$ and a commutative diagram

$$
\begin{gathered}
R/\pi^2R \xrightarrow{} \bar C \\
R/\pi^2R \xrightarrow{} R/\pi R \\
\bar C \xrightarrow{} \Lambda/\pi^2\Lambda \\
\bar C \xrightarrow{} D/\pi D \\
\Lambda/\pi^2\Lambda \xrightarrow{} \Lambda/\pi \Lambda \\
R/\pi R \xrightarrow{} D/\pi D \\
D/\pi D \xrightarrow{} \Lambda/\pi \Lambda
\end{gathered}
$$

with the following properties

1. **(a)** $D$ is of finite presentation,

1. **(b)** $R \to D$ is smooth at any prime $\mathfrak q$ with
$\pi \not \in \mathfrak q$,

1. **(c)** $R \to D$ is smooth at any prime $\mathfrak q$ with
$\pi \in \mathfrak q$ lying over a prime of $\bar C$ where
$R/\pi^2 R \to \bar C$ is smooth, and

1. **(d)** $\bar C/\pi \bar C \to D/\pi D$ is smooth at any prime
lying over a prime of $\bar C$ where $R/\pi^2R \to \bar C$ is smooth.

**Proof.** 
We choose a presentation

$$
\bar C = R[x_1, \ldots, x_n]/(f_1, \ldots, f_m)
$$

We also denote $I = (f_1, \ldots, f_m)$ and $\bar I$ the image of
$I$ in $R/\pi^2R[x_1, \ldots, x_n]$. Since $R$ is Noetherian, so is
$\bar C$. Hence the smooth locus of $R/\pi^2 R \to \bar C$
is quasi-compact, see
Topology, Lemma [F.136](#topology-lemma-Noetherian).
Applying
Lemma [D.2](#smoothing-lemma-find-strictly-standard)
we may choose a finite list of elements
$a_1, \ldots, a_r \in R[x_1, \ldots, x_n]$ such that

1. the union of the open subspaces
$\operatorname{Spec}(\bar C_{a_k}) \subset \operatorname{Spec}(\bar C)$
cover the smooth locus of $R/\pi^2 R \to \bar C$, and

1. for each $k = 1, \ldots, r$ there exists a finite subset
$E_k \subset \{1, \ldots, m\}$ such that
$(\bar I/\bar I^2)_{a_k}$ is freely generated by the classes of
$f_j$, $j \in E_k$.

Set $I_k = (f_j, j \in E_k) \subset I$ and denote $\bar I_k$ the
image of $I_k$ in $R/\pi^2R[x_1, \ldots, x_n]$.
By (2) and Nakayama's lemma we see that $(\bar I/\bar I_k)_{a_k}$
is annihilated by $1 + b'_k$ for some $b'_k \in \bar I_{a_k}$.
Suppose $b'_k$ is the image of $b_k/(a_k)^N$ for some $b_k \in I$
and some integer $N$. After replacing $a_k$ by $a_k((a_k)^N + b_k)$ we get

1. **(3)** $(\bar I_k)_{a_k} = (\bar I)_{a_k}$.

Thus, after possibly replacing $a_k$ by a high power, we may write

1. **(4)** $a_k f_\ell = \sum\nolimits_{j \in E_k} h_{k, \ell}^jf_j + \pi^2 g_{k, \ell}$

for any $\ell \in \{1, \ldots, m\}$ and some
$h_{k, \ell}^j, g_{k, \ell} \in R[x_1, \ldots, x_n]$.
If $\ell \in E_k$ we choose $h_{k, \ell}^j = a_k\delta_{\ell, j}$
(Kronecker delta) and $g_{k, \ell} = 0$. Set

$$
D = R[x_1, \ldots, x_n, z_1, \ldots, z_m]/
(f_j - \pi z_j, p_{k, \ell}).
$$

Here $j \in \{1, \ldots, m\}$, $k \in \{1, \ldots, r\}$,
$\ell \in \{1, \ldots, m\}$, and

$$
p_{k, \ell} = a_k z_\ell - \sum\nolimits_{j \in E_k} h_{k, \ell}^j z_j
- \pi g_{k, \ell}.
$$

Note that for $\ell \in E_k$ we have $p_{k, \ell} = 0$ by our choices above.

The map $R \to D$ is the given one.
Say $\bar C \to \Lambda/\pi^2\Lambda$ maps $x_i$
to the class of $\lambda_i$ modulo $\pi^2$. For an element
$f \in R[x_1, \ldots, x_n]$ we denote $f(\lambda) \in \Lambda$
the result of substituting $\lambda_i$ for $x_i$. Then we know that
$f_j(\lambda) = \pi^2 \mu_j$ for some $\mu_j \in \Lambda$.
Define $D \to \Lambda$ by the rules $x_i \mapsto \lambda_i$ and
$z_j \mapsto \pi\mu_j$. This is well defined because

$$
\begin{aligned}
p_{k, \ell} & \mapsto
a_k(\lambda) \pi \mu_\ell -
\sum\nolimits_{j \in E_k} h_{k, \ell}^j(\lambda) \pi \mu_j
- \pi g_{k, \ell}(\lambda) \\
& =
\pi\left(a_k(\lambda) \mu_\ell -
\sum\nolimits_{j \in E_k} h_{k, \ell}^j(\lambda) \mu_j
- g_{k, \ell}(\lambda)\right)
\end{aligned}
$$

Substituting $x_i = \lambda_i$ in (4) above we see that the expression
inside the brackets is annihilated by $\pi^2$, hence it is annihilated
by $\pi$ as we have assumed
$\text{Ann}_\Lambda(\pi) = \text{Ann}_\Lambda(\pi^2)$.
The map $\bar C \to D/\pi D$ is determined by $x_i \mapsto x_i$
(clearly well defined). Thus we are done if we can prove (b), (c), and (d).

Using (4) we obtain the following key equality

$$
\begin{aligned}
\pi p_{k, \ell} & =
\pi a_k z_\ell - \sum\nolimits_{j \in E_k} \pi h_{k, \ell}^jz_j
- \pi^2 g_{k, \ell} \\
& =
- a_k (f_\ell - \pi z_\ell) + a_k f_\ell +
\sum\nolimits_{j \in E_k} h_{k, \ell}^j (f_j - \pi z_j) -
\sum\nolimits_{j \in E_k} h_{k, \ell}^j f_j - \pi^2 g_{k, \ell} \\
& =
-a_k(f_\ell - \pi z_\ell) +
\sum\nolimits_{j \in E_k} h_{k, \ell}^j(f_j - \pi z_j)
\end{aligned}
$$

The end result is an element of the ideal generated by $f_j - \pi z_j$.
In particular, we see that $D[1/\pi]$ is isomorphic to
$R[1/\pi][x_1, \ldots, x_n, z_1, \ldots, z_m]/(f_j - \pi z_j)$
which is isomorphic to $R[1/\pi][x_1, \ldots, x_n]$ hence smooth
over $R$. This proves (b).

For fixed $k \in \{1, \ldots, r\}$ consider the ring

$$
D_k = R[x_1, \ldots, x_n, z_1, \ldots, z_m]/
(f_j - \pi z_j, j \in E_k, p_{k, \ell})
$$

The number of equations is $m = |E_k| + (m - |E_k|)$ as $p_{k, \ell}$
is zero if $\ell \in E_k$. Also, note that

$$
\begin{aligned}
(D_k/\pi D_k)_{a_k}
& =
R/\pi R[x_1, \ldots, x_n, 1/a_k, z_1, \ldots, z_m]/
(f_j, j \in E_k, p_{k, \ell}) \\
& =
(\bar C/\pi \bar C)_{a_k}[z_1, \ldots, z_m]/
(a_kz_\ell - \sum\nolimits_{j \in E_k} h_{k, \ell}^j z_j) \\
& \cong
(\bar C/\pi \bar C)_{a_k}[z_j, j \in E_k]
\end{aligned}
$$

In particular $(D_k/\pi D_k)_{a_k}$ is smooth over $(\bar C/\pi \bar C)_{a_k}$.
By our choice of $a_k$ we have that $(\bar C/\pi \bar C)_{a_k}$ is smooth
over $R/\pi R$ of relative dimension $n - |E_k|$, see (2). Hence for a prime
$\mathfrak q_k \subset D_k$ containing $\pi$ and lying over
$\operatorname{Spec}(\bar C_{a_k})$ the fibre ring of $R \to D_k$
is smooth at $\mathfrak q_k$ of dimension $n$. Thus $R \to D_k$ is syntomic
at $\mathfrak q_k$ by our count of the number of equations above, see
Algebra, Lemma [F.66](#algebra-lemma-localize-relative-complete-intersection).
Hence $R \to D_k$ is smooth at $\mathfrak q_k$, see
Algebra, Lemma [F.45](#algebra-lemma-flat-fibre-smooth).

To finish the proof, let $\mathfrak q \subset D$ be a prime
containing $\pi$ lying over a prime where $R/\pi^2 R \to \bar C$
is smooth. Then $a_k \not \in \mathfrak q$ for some $k$ by (1).
We will show that the surjection $D_k \to D$ induces
an isomorphism on local rings at $\mathfrak q$. Since we know that
the ring maps $\bar C/\pi \bar C \to D_k/\pi D_k$ and
$R \to D_k$ are smooth at the corresponding prime $\mathfrak q_k$
by the preceding paragraph this will prove (c) and (d) and thus
finish the proof.

First, note that for any $\ell$ the equation
$\pi p_{k, \ell} = -a_k(f_\ell - \pi z_\ell) +
\sum_{j \in E_k} h_{k, \ell}^j (f_j - \pi z_j)$ proved above shows that
$f_\ell - \pi z_\ell$ maps to zero in $(D_k)_{a_k}$ and in particular
in $(D_k)_{\mathfrak q_k}$.
Reducing relations (4) modulo $\pi^2$ kills their
$\pi^2g_{k,\ell}$ term. They therefore give
$a_k\bar f_\ell=\sum_{j\in E_k}\bar h_{k,\ell}^j\bar f_j$
in $\bar I/\bar I^2$; this assertion is made in the reduced
conormal module, not in $I/I^2$.
Since $(\bar I_k/\bar I_k^2)_{a_k}$ is free on $f_j$, $j \in E_k$
we see that

$$
a_{k'} h_{k, \ell}^j -
\sum\nolimits_{j' \in E_{k'}} h_{k', \ell}^{j'} h_{k, j'}^j
$$

is zero in $\bar C_{a_k}$ for every $k, k', \ell$ and $j \in E_k$.
Hence we can find a large integer $N$ such that

$$
a_k^N\left(
a_{k'} h_{k, \ell}^j -
\sum\nolimits_{j' \in E_{k'}} h_{k', \ell}^{j'} h_{k, j'}^j
\right)
$$

is in $I_k + \pi^2R[x_1, \ldots, x_n]$. Computing modulo $\pi$ we have

$$
\begin{aligned}
&
a_kp_{k', \ell} - a_{k'}p_{k, \ell} + \sum h_{k', \ell}^{j'} p_{k, j'}
\\
&
=
- a_k \sum h_{k', \ell}^{j'} z_{j'}
+ a_{k'} \sum h_{k, \ell}^j z_j
+ \sum h_{k', \ell}^{j'} a_k z_{j'}
- \sum \sum h_{k', \ell}^{j'} h_{k, j'}^j z_j \\
&
=
\sum \left(
a_{k'} h_{k, \ell}^j
- \sum h_{k', \ell}^{j'} h_{k, j'}^j
\right) z_j
\end{aligned}
$$

with Einstein summation convention. Combining with the above we see
$a_k^{N + 1} p_{k', \ell}$ is contained in the ideal generated
by $I_k$ and $\pi$ in $R[x_1, \ldots, x_n, z_1, \ldots, z_m]$.
Thus $p_{k', \ell}$ maps into $\pi (D_k)_{a_k}$. On the other hand,
the equation

$$
\pi p_{k', \ell} =
-a_{k'} (f_\ell - \pi z_\ell) +
\sum\nolimits_{j' \in E_{k'}} h_{k', \ell}^{j'}(f_{j'} - \pi z_{j'})
$$

shows that $\pi p_{k', \ell}$ is zero in $(D_k)_{a_k}$.
Since we have assumed that $\text{Ann}_R(\pi) = \text{Ann}_R(\pi^2)$
and since $(D_k)_{\mathfrak q_k}$ is smooth hence flat over $R$
we see that
$\text{Ann}_{(D_k)_{\mathfrak q_k}}(\pi) =
\text{Ann}_{(D_k)_{\mathfrak q_k}}(\pi^2)$.
We conclude that $p_{k', \ell}$ maps to zero as well, hence
$D_{\mathfrak q} = (D_k)_{\mathfrak q_k}$ and we win.
 ∎

### The desingularization lemma

<a id="smoothing-section-desingularization-lemma"></a>

The next construction improves the singular ideal.

<a id="smoothing-lemma-desingularize"></a>

#### Lemma D.20: desingularize

*Adapted from the Stacks project, smoothing.tex, lines 1664–1809.*

Let $R$ be a Noetherian ring.
Let $\Lambda$ be an $R$-algebra. Let $\pi \in R$ and
assume that $\text{Ann}_\Lambda(\pi) = \text{Ann}_\Lambda(\pi^2)$. Let
$A \to \Lambda$ be an $R$-algebra map with $A$ of finite
presentation. Assume

1. the image of $\pi$ is strictly standard in $A$ over $R$, and

1. there exists a section $\rho : A/\pi^4 A \to R/\pi^4 R$
which is compatible with the map to $\Lambda/\pi^4 \Lambda$.

Then we can find $R$-algebra maps $A \to B \to \Lambda$ with $B$
of finite presentation such that $\mathfrak a B \subset H_{B/R}$ where
$\mathfrak a = \text{Ann}_R(\text{Ann}_R(\pi^2)/\text{Ann}_R(\pi))$.

**Proof.** 
Choose a presentation

$$
A = R[x_1, \ldots, x_n]/(f_1, \ldots, f_m)
$$

and $0 \leq c \leq \min(n, m)$ such that
([D.3s1: strict Jacobian-minor condition](#equation-strictly-standard-one)) holds for $\pi$ and such that

$$
\pi f_{c + j} \in (f_1, \ldots, f_c) + (f_1, \ldots, f_m)^2
$$

for $j = 1, \ldots, m - c$. Say $\rho$ maps $x_i$ to the class of
$r_i \in R$. Then we can replace $x_i$ by $x_i - r_i$. Hence we may
assume $\rho(x_i) = 0$ in $R/\pi^4 R$. This implies that
$f_j(0) \in \pi^4R$ and that $A \to \Lambda$ maps $x_i$
to $\pi^4\lambda_i$ for some $\lambda_i \in \Lambda$. Write

$$
f_j = f_j(0) + \sum\nolimits_{i = 1, \ldots, n} r_{ji} x_i + \text{h.o.t.}
$$

This implies that the constant term of $\partial f_j/\partial x_i$ is
$r_{ji}$. Apply $\rho$ to ([D.3s1: strict Jacobian-minor condition](#equation-strictly-standard-one))
for $\pi$ and we see that

$$
\pi = \sum\nolimits_{I \subset \{1, \ldots, n\},\ |I| = c}
r_I \det(r_{ji})_{j = 1, \ldots, c,\ i \in I} \bmod \pi^4R
$$

for some $r_I \in R$. Thus we have

$$
u\pi = \sum\nolimits_{I \subset \{1, \ldots, n\},\ |I| = c}
r_I \det(r_{ji})_{j = 1, \ldots, c,\ i \in I}
$$

for some $u \in 1 + \pi^3R$. By
Algebra, Lemma [F.70](#algebra-lemma-matrix-left-inverse)
this implies there exists a $n \times c$ matrix $(s_{ik})$ such that

$$
u\pi \delta_{jk} = \sum\nolimits_{i = 1, \ldots, n} r_{ji}s_{ik}\quad
\text{for all } j, k = 1, \ldots, c
$$

(Kronecker delta). We introduce auxiliary variables
$v_1, \ldots, v_c, w_1, \ldots, w_n$ and we set

$$
h_i = x_i - \pi^2 \sum\nolimits_{j = 1, \ldots c} s_{ij} v_j - \pi^3 w_i
$$

In the following we will use that

$$
R[x_1, \ldots, x_n, v_1, \ldots, v_c, w_1, \ldots, w_n]/
(h_1, \ldots, h_n) = R[v_1, \ldots, v_c, w_1, \ldots, w_n]
$$

without further mention. In
$R[x_1, \ldots, x_n, v_1, \ldots, v_c, w_1, \ldots, w_n]/
(h_1, \ldots, h_n)$ we have

$$
\begin{aligned}
f_j & = f_j(x_1 - h_1, \ldots, x_n - h_n) \\
& =
\pi^2 \sum\nolimits_{k = 1}^c
\left(\sum\nolimits_{i = 1}^n r_{ji} s_{ik}\right) v_k
+
\pi^3 \sum\nolimits_{i = 1}^n r_{ji}w_i \bmod \pi^4 \\
& =
\pi^3 v_j + \pi^3 \sum\nolimits_{i = 1}^n r_{ji}w_i \bmod \pi^4
\end{aligned}
$$

for $1 \leq j \leq c$. Hence we can choose elements
$g_j \in R[v_1, \ldots, v_c, w_1, \ldots, w_n]$
such that $g_j = v_j + \sum r_{ji}w_i \bmod \pi$
and such that $f_j = \pi^3 g_j$ in $Q/(h_1,\ldots,h_n)$, where

$$
Q=R[x_1,\ldots,x_n,v_1,\ldots,v_c,w_1,\ldots,w_n].
$$

We set

$$
B = R[x_1, \ldots, x_n, v_1, \ldots, v_c, w_1, \ldots, w_n]/
(f_1, \ldots, f_m, h_1, \ldots, h_n, g_1, \ldots, g_c).
$$

The map $A \to B$ is clear. We define $B \to \Lambda$ by mapping
$x_i \to \pi^4\lambda_i$, $v_i \mapsto 0$, and $w_i \mapsto \pi \lambda_i$.
Then it is clear that the elements $f_j$ and $h_i$ are mapped to zero
in $\Lambda$. Moreover, it is clear that $g_i$ is mapped to an element
$t$ of $\pi\Lambda$ such that $\pi^3t = 0$ (as $f_i = \pi^3 g_i$ modulo
the ideal generated by the $h$'s). Hence our assumption that
$\text{Ann}_\Lambda(\pi) = \text{Ann}_\Lambda(\pi^2)$ implies that $t = 0$.
Thus we are done if we can prove the statement about smoothness.

Note that $B_\pi \cong A_\pi[v_1, \ldots, v_c]$ because the equations
$g_i = 0$ are implied by $f_i = 0$. Hence $B_\pi$ is smooth over $R$
as $A_\pi$ is smooth over $R$ by the assumption that $\pi$ is strictly
standard in $A$ over $R$, see
Lemma [D.5](#smoothing-lemma-elkik).

Set $B' = R[v_1, \ldots, v_c, w_1, \ldots, w_n]/(g_1, \ldots, g_c)$.
As $g_i = v_i + \sum r_{ji}w_i \bmod \pi$ we see that
$B'/\pi B' = R/\pi R[w_1, \ldots, w_n]$. Hence
$R \to B'$ is smooth of relative dimension $n$ at every
point of $V(\pi)$ by
Algebra, Lemmas
[F.66](#algebra-lemma-localize-relative-complete-intersection) and
[F.45](#algebra-lemma-flat-fibre-smooth)
(the first lemma shows it is syntomic at those primes, in particular
flat, whereupon the second lemma shows it is smooth).

Let $\mathfrak q \subset B$ be a prime with $\pi \in \mathfrak q$ and
for some $r \in \mathfrak a$, $r \not \in \mathfrak q$.
Denote $\mathfrak q' = B' \cap \mathfrak q$.
We claim the surjection $B' \to B$ induces an isomorphism of local
rings $(B')_{\mathfrak q'} \to B_\mathfrak q$. This will
conclude the proof of the lemma. Note that $B_\mathfrak q$ is the
quotient of $(B')_{\mathfrak q'}$ by the ideal generated by
$f_{c + j}$, $j = 1, \ldots, m - c$. We observe two things:
first the image of $f_{c + j}$ in $(B')_{\mathfrak q'}$ is
divisible by $\pi^2$ and
second the image of $\pi f_{c + j}$ in $(B')_{\mathfrak q'}$
can be written as $\sum b_{j_1 j_2} f_{c + j_1}f_{c + j_2}$ by
([D.20](#smoothing-lemma-desingularize)). Thus we see that the image of each $\pi f_{c + j}$
is contained in the ideal generated by the elements $\pi^2 f_{c + j'}$.
Hence $\pi f_{c + j} = 0$ in $(B')_{\mathfrak q'}$ as this is a
Noetherian local ring, see
Algebra, Lemma [AG-CA-03, Theorem 6.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/noetherian-and-artinian-rings.html).
As $R \to (B')_{\mathfrak q'}$ is flat we see that

$$
\left(\text{Ann}_R(\pi^2)/\text{Ann}_R(\pi)\right)
\otimes_R (B')_{\mathfrak q'}
=
\text{Ann}_{(B')_{\mathfrak q'}}(\pi^2)/\text{Ann}_{(B')_{\mathfrak q'}}(\pi)
$$

Because $r \in \mathfrak a$ is invertible in
$(B')_{\mathfrak q'}$ we see that this module is zero.
Hence we see that the image of $f_{c + j}$ is zero in
$(B')_{\mathfrak q'}$ as desired.
 ∎

<a id="smoothing-lemma-desingularize-strictly-standard"></a>

#### Lemma D.21: desingularize strictly standard

*Adapted from the Stacks project, smoothing.tex, lines 1811–1859.*

Let $R$ be a Noetherian ring. Let $\Lambda$ be an $R$-algebra.
Let $\pi \in R$ and assume that $\text{Ann}_R(\pi) = \text{Ann}_R(\pi^2)$ and
$\text{Ann}_\Lambda(\pi) = \text{Ann}_\Lambda(\pi^2)$.
Let $A \to \Lambda$ and $D \to \Lambda$ be $R$-algebra maps with
$A$ and $D$ of finite presentation. Assume

1. $\pi$ is strictly standard in $A$ over $R$, and

1. there exists an $R$-algebra map $A/\pi^4 A \to D/\pi^4 D$ compatible
with the maps to $\Lambda/\pi^4 \Lambda$.

Then we can find an $R$-algebra map $B \to \Lambda$ with $B$ of finite
presentation and $R$-algebra maps $A \to B$ and $D \to B$
compatible with the maps to $\Lambda$ such that $H_{D/R}B \subset H_{B/D}$
and $H_{D/R}B \subset H_{B/R}$.

**Proof.** 
We apply Lemma [D.20](#smoothing-lemma-desingularize) to

$$
D \longrightarrow A \otimes_R D \longrightarrow \Lambda
$$

and the image of $\pi$ in $D$. By
Lemma [D.7](#smoothing-lemma-strictly-standard-base-change)
we see that $\pi$ is strictly standard in $A \otimes_R D$ over $D$.
As our section $\rho : (A \otimes_R D)/\pi^4 (A \otimes_R D) \to D/\pi^4 D$
we take the map induced by the map in (2). Thus
Lemma [D.20](#smoothing-lemma-desingularize) applies and we obtain a factorization
$A \otimes_R D \to B \to \Lambda$ with $B$ of finite presentation
and $\mathfrak a B \subset H_{B/D}$ where

$$
\mathfrak a = \text{Ann}_D(\text{Ann}_D(\pi^2)/\text{Ann}_D(\pi)).
$$

For any prime $\mathfrak q$ of $D$ such that $D_\mathfrak q$ is flat over $R$
we have
$\text{Ann}_{D_\mathfrak q}(\pi^2)/\text{Ann}_{D_\mathfrak q}(\pi) = 0$
because annihilators of elements commutes with flat base change and
we assumed $\text{Ann}_R(\pi) = \text{Ann}_R(\pi^2)$. Because $D$ is
Noetherian we see that $\text{Ann}_D(\pi^2)/\text{Ann}_D(\pi)$ is a finite
$D$-module, hence formation of its annihilator commutes with localization.
Thus we see that $\mathfrak a \not \subset \mathfrak q$. Hence we see
that $D \to B$ is smooth at any prime of $B$ lying over $\mathfrak q$.
Since any prime of $D$ where $R \to D$ is smooth is one where
$D_\mathfrak q$ is flat over $R$ we conclude that $H_{D/R}B \subset H_{B/D}$.
The final inclusion $H_{D/R}B \subset H_{B/R}$ follows because compositions
of smooth ring maps are smooth
(Algebra, Lemma [F.29](#algebra-lemma-compose-smooth)).
 ∎

<a id="smoothing-lemma-desingularize-lifting-apply"></a>

#### Lemma D.22: desingularize lifting apply

*Adapted from the Stacks project, smoothing.tex, lines 1861–1894.*

Let $R$ be a Noetherian ring. Let $\Lambda$ be an $R$-algebra.
Let $\pi \in R$ and assume that $\text{Ann}_R(\pi) = \text{Ann}_R(\pi^2)$ and
$\text{Ann}_\Lambda(\pi) = \text{Ann}_\Lambda(\pi^2)$.
Let $A \to \Lambda$ be an $R$-algebra map with
$A$ of finite presentation and assume $\pi$ is strictly standard
in $A$ over $R$. Let

$$
A/\pi^8A \to \bar C \to \Lambda/\pi^8\Lambda
$$

be a factorization with $\bar C$ of finite presentation.
Then we can find a factorization $A \to B \to \Lambda$ with $B$ of finite
presentation such that $R_\pi \to B_\pi$ is smooth and such that

$$
H_{\bar C/(R/\pi^8 R)} \cdot \Lambda/\pi^8\Lambda
\subset
\sqrt{H_{B/R} \Lambda} \bmod \pi^8\Lambda.
$$

**Proof.** 
Apply Lemma [D.19](#smoothing-lemma-lifting) to get $R \to D \to \Lambda$
with a factorization
$\bar C/\pi^4\bar C \to D/\pi^4 D \to \Lambda/\pi^4\Lambda$
such that $R \to D$ is smooth at any prime not containing $\pi$
and at any prime lying over a prime of $\bar C/\pi^4\bar C$
where $R/\pi^8 R \to \bar C$ is smooth.
By Lemma [D.21](#smoothing-lemma-desingularize-strictly-standard)
we can find a finitely presented $R$-algebra $B$ and
factorizations $A \to B \to \Lambda$ and $D \to B \to \Lambda$
such that $H_{D/R}B\subset H_{B/R}$. To verify the assertion, first note that equality of the annihilators of $\pi$ and $\pi^2$ implies equality for every positive power: if $\pi^{r+1}x=0$, successive applications of that equality give $\pi x=0$. Thus the lifting lemma applies with $\pi^4$ in place of $\pi$.

At a prime not containing $\pi$, $R\to D$ is smooth; the singular-ideal inclusion then makes $R\to B$ smooth there too. Hence $B[1/\pi]$ is smooth. Let $\mathfrak l$ be a prime of $\Lambda$ containing $H_{B/R}\Lambda$, and let $\mathfrak b$ and $\mathfrak d$ be its contractions to $B$ and $D$. The preceding observation implies $\pi\in\mathfrak l$. The inclusion also implies $H_{D/R}\subset\mathfrak d$, so $D$ is not smooth at $\mathfrak d$. By the lifting lemma's property (c), the corresponding prime of $\bar C/\pi^4\bar C$ cannot come from a smooth prime of $\bar C$ over $R/\pi^8R$. Therefore every element of $H_{\bar C/(R/\pi^8R)}$ maps into $\mathfrak l/\pi^8\Lambda$. Intersect over all such $\mathfrak l$. This gives exactly the stated radical inclusion.
 ∎

### Warmup: reduction to a base field

<a id="smoothing-section-reduction"></a>

In this section we apply the lemmas in the previous sections
to prove that it suffices to prove the main result when the base
ring is a field, see Lemma [D.26](#smoothing-lemma-reduce-to-field).

<a id="smoothing-situation-global"></a>

#### Situation D.23: global

*Adapted from the Stacks project, smoothing.tex, lines 1915–1918.*

Here $R \to \Lambda$ is a regular ring map of Noetherian rings.

Let $R \to \Lambda$ be as in Situation [D.23](#smoothing-situation-global).
We say *PT holds for $R \to \Lambda$* if $\Lambda$ is a
filtered colimit of smooth $R$-algebras.

<a id="smoothing-lemma-product"></a>

#### Lemma D.24: product

*Adapted from the Stacks project, smoothing.tex, lines 1925–1934.*

Let $R_i \to \Lambda_i$, $i = 1, 2$ be as in Situation [D.23](#smoothing-situation-global).
If PT holds for $R_i \to \Lambda_i$, $i = 1, 2$, then PT holds for
$R_1 \times R_2 \to \Lambda_1 \times \Lambda_2$.

**Proof.** 
Write $\Lambda_i=\operatorname*{colim}_{a\in I_i} B_{i,a}$ with $I_i$ filtered and every $B_{i,a}$ smooth over $R_i$. The category $I_1\times I_2$ is filtered: nonemptiness, a common successor for two objects, and an equalizer for two parallel arrows are constructed in the two coordinates. The $R_1\times R_2$-algebra $B_{1,a}\times B_{2,b}$ is smooth, because its spectrum is the disjoint union of the two corresponding smooth spectra. The natural map

$$
\operatorname*{colim}_{(a,b)\in I_1\times I_2}(B_{1,a}\times B_{2,b})
\longrightarrow \Lambda_1\times\Lambda_2
$$

is surjective by choosing representatives of the two components, and injective because any equality of pairs becomes an equality at successors in each coordinate. It is a ring isomorphism, proving the assertion.
 ∎

<a id="smoothing-lemma-delocalize-base"></a>

#### Lemma D.25: delocalize base

*Adapted from the Stacks project, smoothing.tex, lines 1936–2000.*

Let $R \to A \to \Lambda$ be ring maps with $A$ of finite presentation
over $R$. Let $S \subset R$ be a multiplicative
set. Let $S^{-1}A \to B' \to S^{-1}\Lambda$ be a factorization with
$B'$ smooth over $S^{-1}R$. Then we can find a factorization
$A \to B \to \Lambda$ such that some $s \in S$ maps to an
elementary standard element (Definition [D.3](#smoothing-definition-strictly-standard))
in $B$ over $R$.

**Proof.** 
We first apply Lemma [D.12](#smoothing-lemma-smooth-standard-smooth) to $S^{-1}R \to B'$.
Thus we may assume $B'$ is standard smooth over $S^{-1}R$.
Write $A = R[x_1, \ldots, x_n]/(g_1, \ldots, g_t)$ and say
$x_i \mapsto \lambda_i$ in $\Lambda$. We may write
$B' = S^{-1}R[x_1, \ldots, x_{n + m}]/(f_1, \ldots, f_c)$
for some $c \geq n$ where
$\det(\partial f_j/\partial x_i)_{i, j = 1, \ldots, c}$
is invertible in $B'$ and such that $A \to B'$ is given by $x_i \mapsto x_i$,
see Lemma [D.14](#smoothing-lemma-standard-smooth-include-generators).
After multiplying $x_i$, $i > n$ by an element of $S$ and correspondingly
modifying the equations $f_j$ we may assume $B' \to S^{-1}\Lambda$ maps
$x_i$ to $\lambda_i/1$ for some $\lambda_i \in \Lambda$ for $i > n$.
Choose a relation

$$
1 =
a_0 \det(\partial f_j/\partial x_i)_{i, j = 1, \ldots, c}
+
\sum\nolimits_{j = 1, \ldots, c} a_jf_j
$$

for some $a_j \in S^{-1}R[x_1, \ldots, x_{n + m}]$. Since each element of $S$
is invertible in $B'$ we may (by clearing denominators) assume that
$f_j, a_j \in R[x_1, \ldots, x_{n + m}]$ and that

$$
s_0 = a_0 \det(\partial f_j/\partial x_i)_{i, j = 1, \ldots, c}
+
\sum\nolimits_{j = 1, \ldots, c} a_jf_j
$$

for some $s_0 \in S$. Since $g_j$ maps to zero in
$S^{-1}R[x_1, \ldots, x_{n + m}]/(f_1, \ldots, f_c)$
we can find elements $s_j \in S$ such that $s_j g_j = 0$ in
$R[x_1, \ldots, x_{n + m}]/(f_1, \ldots, f_c)$.
Since $f_j$ maps to zero in $S^{-1}\Lambda$ we can find $s'_j \in S$
such that $s'_j f_j(\lambda_1, \ldots, \lambda_{n + m}) = 0$ in
$\Lambda$. Consider the ring

$$
B = R[x_1, \ldots, x_{n + m}]/
(s'_1f_1, \ldots, s'_cf_c, g_1, \ldots, g_t)
$$

and the factorization $A \to B \to \Lambda$ with $B \to \Lambda$ given by
$x_i \mapsto \lambda_i$. We claim that $s = s_0s_1 \ldots s_ts'_1 \ldots s'_c$
is elementary standard in $B$ over $R$ which finishes the proof.
Namely, $s_j g_j \in (f_1, \ldots, f_c)$ and hence
$sg_j \in (s'_1f_1, \ldots, s'_cf_c)$. Finally, we have

$$
a_0\det(\partial s'_jf_j/\partial x_i)_{i, j = 1, \ldots, c}
+
\sum\nolimits_{j = 1, \ldots, c}
(s'_1 \ldots \hat{s'_j} \ldots s'_c) a_j s'_jf_j
=
s_0s'_1\ldots s'_c
$$

which divides $s$ as desired.
 ∎

<a id="smoothing-lemma-reduce-to-field"></a>

#### Lemma D.26: reduce to field

*Adapted from the Stacks project, smoothing.tex, lines 2002–2063.*

If for every Situation [D.23](#smoothing-situation-global) where $R$
is a field PT holds, then PT holds in general.

**Proof.** 
Assume PT holds for any Situation [D.23](#smoothing-situation-global) where $R$ is a field.
Let $R \to \Lambda$ be as in Situation [D.23](#smoothing-situation-global) arbitrary.
Note that $R/I \to \Lambda/I\Lambda$ is another regular ring map
of Noetherian rings, see
More on Algebra, Lemma [F.123](#more-algebra-lemma-regular-base-change).
Consider the set of ideals

$$
\mathcal{I} = \{I \subset R \mid R/I \to \Lambda/I\Lambda
\text{ does not have PT}\}
$$

We have to show that $\mathcal{I}$ is empty. If this set is nonempty,
then it contains a maximal element because $R$ is Noetherian.
Replacing $R$ by $R/I$ and $\Lambda$ by $\Lambda/I$ we obtain a
situation where PT holds for $R/I \to \Lambda/I\Lambda$ for any
nonzero ideal of $R$. In particular, we see by applying
Proposition [D.18](#smoothing-proposition-lift)
that $R$ is a reduced ring.

Let $A \to \Lambda$ be an $R$-algebra homomorphism with $A$ of
finite presentation. We have to find a factorization $A \to B \to \Lambda$
with $B$ smooth over $R$, see Algebra, Lemma [F.90](#algebra-lemma-when-colimit).

Let $S \subset R$ be the set of nonzerodivisors and
consider the total ring of fractions $Q = S^{-1}R$ of $R$. We know that
$Q = K_1 \times \ldots \times K_n$ is a product of fields, see
Algebra, Lemmas [F.89](#algebra-lemma-total-ring-fractions-no-embedded-points) and
[AG-CA-03, Proposition 2.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/noetherian-and-artinian-rings.html).
By Lemma [D.24](#smoothing-lemma-product) and our assumption
PT holds for the ring map $S^{-1}R \to S^{-1}\Lambda$.
Hence we can find a factorization $S^{-1}A \to B' \to S^{-1}\Lambda$
with $B'$ smooth over $S^{-1}R$.

We apply Lemma [D.25](#smoothing-lemma-delocalize-base)
and find a factorization $A \to B \to \Lambda$ such that
some $\pi \in S$ is elementary standard in $B$ over $R$.
After replacing $A$ by $B$ we may assume that $\pi$ is
elementary standard, hence strictly standard in $A$. We know that
$R/\pi^8R \to \Lambda/\pi^8\Lambda$ satisfies PT.
Hence we can find a factorization
$R/\pi^8 R \to A/\pi^8A \to \bar C \to \Lambda/\pi^8\Lambda$
with $R/\pi^8 R \to \bar C$ smooth. By
Lemma [D.19](#smoothing-lemma-lifting)
we can find an $R$-algebra map $D \to \Lambda$ with $D$ smooth over $R$
and a factorization
$R/\pi^4 R \to A/\pi^4A \to D/\pi^4D \to \Lambda/\pi^4\Lambda$.
By Lemma [D.21](#smoothing-lemma-desingularize-strictly-standard)
we can find $A \to B \to \Lambda$ with $B$ smooth over $R$
which finishes the proof.
 ∎

### Local tricks

<a id="smoothing-section-local"></a>

<a id="smoothing-situation-local"></a>

#### Situation D.27: local

*Adapted from the Stacks project, smoothing.tex, lines 2078–2084.*

We are given a Noetherian ring $R$ and an $R$-algebra map $A \to \Lambda$
and a prime $\mathfrak q \subset \Lambda$. We assume $A$ is of
finite presentation over $R$. In this situation we denote
$\mathfrak h_A = \sqrt{H_{A/R} \Lambda}$.

Let $R \to A \to \Lambda \supset \mathfrak q$ be as in
Situation [D.27](#smoothing-situation-local). We say
*$R \to A \to \Lambda \supset \mathfrak q$
can be resolved* if there exists a factorization $A \to B \to \Lambda$
with $B$ of finite presentation and
$\mathfrak h_A \subset \mathfrak h_B \not \subset \mathfrak q$.
In this case we will call the factorization $A \to B \to \Lambda$
a *resolution of $R \to A \to \Lambda \supset \mathfrak q$*.

<a id="smoothing-lemma-lift-solution"></a>

#### Lemma D.28: lift solution

*Adapted from the Stacks project, smoothing.tex, lines 2096–2145.*

Let $R \to A \to \Lambda \supset \mathfrak q$ be as in
Situation [D.27](#smoothing-situation-local). Let $r \geq 1$ and
$\pi_1, \ldots, \pi_r \in R$ map to elements of $\mathfrak q$. Assume

1. for $i = 1, \ldots, r$ we have

$$
\text{Ann}_{R/(\pi_1^8, \ldots, \pi_{i - 1}^8)R}(\pi_i)
=
\text{Ann}_{R/(\pi_1^8, \ldots, \pi_{i - 1}^8)R}(\pi_i^2)
$$

and

$$
\text{Ann}_{\Lambda/(\pi_1^8, \ldots, \pi_{i - 1}^8)\Lambda}(\pi_i)
=
\text{Ann}_{\Lambda/(\pi_1^8, \ldots, \pi_{i - 1}^8)\Lambda}(\pi_i^2)
$$

1. for $i = 1, \ldots, r$ the element $\pi_i$ maps to a strictly
standard element in $A$ over $R$.

Then, if

$$
R/(\pi_1^8, \ldots, \pi_r^8)R \to A/(\pi_1^8, \ldots, \pi_r^8)A
\to \Lambda/(\pi_1^8, \ldots, \pi_r^8)\Lambda \supset
\mathfrak q/(\pi_1^8, \ldots, \pi_r^8)\Lambda
$$

can be resolved, so can $R \to A \to \Lambda \supset \mathfrak q$.

**Proof.** 
We are going to prove this by induction on $r$.

The case $r = 1$. Here the assumption is that there exists a
factorization $A/\pi_1^8 \to \bar C \to \Lambda/\pi_1^8$
which resolves the situation modulo $\pi_1^8$. Conditions (1) and
(2) are the assumptions needed to apply
Lemma [D.22](#smoothing-lemma-desingularize-lifting-apply).
Thus we can ``lift'' the resolution $\bar C$
to a resolution of $R \to A \to \Lambda \supset \mathfrak q$.

The case $r > 1$. In this case we apply the induction hypothesis for $r - 1$
to the situation
$R/\pi_1^8 \to A/\pi_1^8 \to \Lambda/\pi_1^8
\supset \mathfrak q/\pi_1^8\Lambda$.
Note that property (2) is preserved by
Lemma [D.7](#smoothing-lemma-strictly-standard-base-change). The induction
resolves the situation modulo $\pi_1^8$; the already proved case
$r=1$, applied to $\pi_1$, lifts this resolution to the original
situation. ∎

<a id="smoothing-lemma-delocalize-weak"></a>

#### Lemma D.29: delocalize weak

*Adapted from the Stacks project, smoothing.tex, lines 2147–2227.*

Let $R \to A \to \Lambda \supset \mathfrak q$ be as in
Situation [D.27](#smoothing-situation-local). Let $\mathfrak p = R \cap \mathfrak q$.
Assume that $\mathfrak q$ is minimal over $\mathfrak h_A$ and that
$R_\mathfrak p \to A_\mathfrak p \to \Lambda_\mathfrak q
\supset \mathfrak q\Lambda_\mathfrak q$ can be resolved.
Then there exists a factorization $A \to C \to \Lambda$ with $C$ of
finite presentation such that $H_{C/R} \Lambda \not \subset \mathfrak q$.

**Proof.** 
Let $A_\mathfrak p \to C \to \Lambda_\mathfrak q$ be a resolution of
$R_\mathfrak p \to A_\mathfrak p \to \Lambda_\mathfrak q
\supset \mathfrak q\Lambda_\mathfrak q$. By our assumption
that $\mathfrak q$ is minimal over $\mathfrak h_A$ this
means that $H_{C/R_\mathfrak p} \Lambda_\mathfrak q = \Lambda_\mathfrak q$.
By Lemma [D.8](#smoothing-lemma-final-solve)
we may assume that $C$ is smooth over $R_\mathfrak p$.
By Lemma [D.12](#smoothing-lemma-smooth-standard-smooth) we may assume that
$C$ is standard smooth over $R_\mathfrak p$.
Write $A = R[x_1, \ldots, x_n]/(g_1, \ldots, g_t)$ and say
$A \to \Lambda$ is given by $x_i \mapsto \lambda_i$.
Write $C = R_\mathfrak p[x_1, \ldots, x_{n + m}]/(f_1, \ldots, f_c)$
for some $c \geq n$ such that $A \to C$ maps $x_i$ to $x_i$ and such that
$\det(\partial f_j/\partial x_i)_{i, j = 1, \ldots, c}$
is invertible in $C$, see
Lemma [D.14](#smoothing-lemma-standard-smooth-include-generators).
After clearing denominators we may assume
$f_1, \ldots, f_c$ are elements of $R[x_1, \ldots, x_{n + m}]$.
Of course
$\det(\partial f_j/\partial x_i)_{i, j = 1, \ldots, c}$
is not invertible in $R[x_1, \ldots, x_{n + m}]/(f_1, \ldots, f_c)$
but it becomes invertible after inverting some element $s_0 \in R$,
$s_0 \not \in \mathfrak p$.
As $g_j$ maps to zero under $R[x_1, \ldots, x_n] \to A \to C$
we can find $s_j \in R$, $s_j \not \in \mathfrak p$ such that
$s_j g_j$ is zero in $R[x_1, \ldots, x_{n + m}]/(f_1, \ldots, f_c)$.
Write $f_j = F_j(x_1, \ldots, x_{n + m}, 1)$
for some polynomial
$F_j \in R[x_1, \ldots, x_n, X_{n + 1}, \ldots, X_{n + m + 1}]$
homogeneous in $X_{n + 1}, \ldots, X_{n + m + 1}$.
Pick $\lambda_{n + i} \in \Lambda$, $i = 1, \ldots, m + 1$ with
$\lambda_{n + m + 1} \not \in \mathfrak q$ such that $x_{n + i}$ maps to
$\lambda_{n + i}/\lambda_{n + m + 1}$ in $\Lambda_\mathfrak q$.
Then

$$
\begin{aligned}
F_j(\lambda_1, \ldots, \lambda_{n + m + 1})
& =
(\lambda_{n + m + 1})^{\deg(F_j)} F_j(\lambda_1, \ldots, \lambda_n,
\frac{\lambda_{n + 1}}{\lambda_{n + m + 1}}, \ldots,
\frac{\lambda_{n + m}}{\lambda_{n + m + 1}}, 1) \\
& =
(\lambda_{n + m + 1})^{\deg(F_j)} f_j(\lambda_1, \ldots, \lambda_n,
\frac{\lambda_{n + 1}}{\lambda_{n + m + 1}}, \ldots,
\frac{\lambda_{n + m}}{\lambda_{n + m + 1}}) \\
& = 0
\end{aligned}
$$

in $\Lambda_\mathfrak q$. Thus we can find
$\lambda_0 \in \Lambda$, $\lambda_0 \not \in \mathfrak q$ such that
$\lambda_0 F_j(\lambda_1, \ldots, \lambda_{n + m + 1}) = 0$
in $\Lambda$. Now we set $B$ equal to

$$
R[x_0, \ldots, x_{n + m + 1}]/
(g_1, \ldots, g_t, x_0F_1(x_1, \ldots, x_{n + m + 1}), \ldots,
x_0F_c(x_1, \ldots, x_{n + m + 1}))
$$

which we map to $\Lambda$ by mapping $x_i$ to $\lambda_i$.
Let $b$ be the image of $x_0 x_{n + m + 1} s_0 s_1 \ldots s_t$ in $B$.
Then $B_b$ is isomorphic to

$$
R_{s_0s_1 \ldots s_t}[x_0, x_1, \ldots, x_{n + m + 1}, 1/x_0x_{n + m + 1}]/
(f_1, \ldots, f_c)
$$

which is smooth over $R$ by construction.
Since $b$ does not map to an element of $\mathfrak q$, we win.
 ∎

<a id="smoothing-lemma-delocalize-height-zero"></a>

#### Lemma D.30: delocalize height zero

*Adapted from the Stacks project, smoothing.tex, lines 2229–2274.*

Let $R \to A \to \Lambda \supset \mathfrak q$ be as in
Situation [D.27](#smoothing-situation-local). Let $\mathfrak p = R \cap \mathfrak q$.
Assume

1. $\mathfrak q$ is minimal over $\mathfrak h_A$,

1. $R_\mathfrak p \to A_\mathfrak p \to \Lambda_\mathfrak q
\supset \mathfrak q\Lambda_\mathfrak q$ can be resolved, and

1. $\dim(\Lambda_\mathfrak q) = 0$.

Then $R \to A \to \Lambda \supset \mathfrak q$ can be resolved.

**Proof.** 
By (3) the ring $\Lambda_\mathfrak q$ is Artinian local hence
$\mathfrak q\Lambda_\mathfrak q$ is nilpotent. Thus
$(\mathfrak h_A)^N \Lambda_\mathfrak q = 0$ for some $N > 0$.
Thus there exists a $\lambda \in \Lambda$, $\lambda \not \in \mathfrak q$
such that $\lambda (\mathfrak h_A)^N = 0$ in $\Lambda$.
Say $H_{A/R} = (a_1, \ldots, a_r)$ so that $\lambda a_i^N = 0$
in $\Lambda$. By Lemma [D.29](#smoothing-lemma-delocalize-weak) we can find a factorization
$A \to C \to \Lambda$ with $C$ of finite presentation such that
$\mathfrak h_C \not \subset \mathfrak q$.
Write $C = A[x_1, \ldots, x_n]/(f_1, \ldots, f_m)$.
Set

$$
B = A[x_1, \ldots, x_n, y_1, \ldots, y_r, z, t_{ij}]/
(f_j - \sum y_i t_{ij}, zy_i)
$$

where $t_{ij}$ is a set of $rm$ variables.
Note that there is a map $B \to C[y_i, z]/(y_iz)$ given by setting $t_{ij}$
equal to zero. The map $B \to \Lambda$ is the composition
$B \to C[y_i, z]/(y_iz) \to \Lambda$ where $C[y_i, z]/(y_iz) \to \Lambda$
is the given map $C \to \Lambda$, maps $z$ to $\lambda$, and maps
$y_i$ to the image of $a_i^N$ in $\Lambda$.

We claim that $B$ is a solution for $R \to A \to \Lambda \supset \mathfrak q$.
First note that $B_z$ is isomorphic to $C[z, z^{-1}, t_{ij}]$
as a C-algebra. Choose $c \in H_{C/R}$ whose image in $\Lambda$ is not in $\mathfrak q$. Then $B_{zc}$ is smooth over $R$. On the other hand,
$B_{y_\ell} \cong A[x_i, y_i, y_\ell^{-1}, t_{ij}, i \not = \ell]$
which is smooth over $A$. Thus we see that $zc$ and $a_\ell y_\ell$
(compositions of smooth maps are smooth) are all
elements of $H_{B/R}$. This proves the lemma.
 ∎

### Separable residue fields

<a id="smoothing-section-separable"></a>

In this section we explain how to solve a local problem in the case
of a separable residue field extension.

<a id="smoothing-lemma-ogoma"></a>

#### Lemma D.31: ogoma

*Adapted from the Stacks project, smoothing.tex, lines 2286–2303.*

Let $A$ be a Noetherian ring and let $M$ be a finite $A$-module.
Let $S \subset A$ be a multiplicative set. If $\pi \in A$ and
$\ker(\pi : S^{-1}M \to S^{-1}M) =
\ker(\pi^2 : S^{-1}M \to S^{-1}M)$
then there exists an $s \in S$ such that for any $n > 0$ we have
$\ker(s^n\pi : M \to M) = \ker((s^n\pi)^2 : M \to M)$.

**Proof.** 
Let $K = \ker(\pi : M \to M)$ and
$K' = \{m \in M \mid \pi^2 m = 0\text{ in }S^{-1}M\}$ and
$Q = K'/K$. Note that $S^{-1}Q = 0$ by assumption. Since $A$
is Noetherian we see that $Q$ is a finite $A$-module.
Hence we can find an $s \in S$ such that $s$ annihilates $Q$.
If $(s^n\pi)^2m=0$, then $\pi^2m=0$ after localization, so $m\in K'$.
The equality $sQ=0$ gives $sm\in K$, hence $s\pi m=0$, and therefore
$s^n\pi m=0$ for every $n>0$. The reverse kernel inclusion is immediate.
Thus this single $s$ works for every positive power.
 ∎

<a id="smoothing-lemma-find-sequence"></a>

#### Lemma D.32: find sequence

*Adapted from the Stacks project, smoothing.tex, lines 2305–2349.*

Let $\Lambda$ be a Noetherian ring. Let $I \subset \Lambda$ be an ideal.
Let $I \subset \mathfrak q$ be a prime. Let $n, e$ be positive integers.
Assume that $\mathfrak q^n\Lambda_\mathfrak q \subset I\Lambda_\mathfrak q$
and that $\Lambda_\mathfrak q$ is a regular local ring of dimension $d$.
Then there exist
$\pi_1, \ldots, \pi_d \in \Lambda$ such that

1. $(\pi_1, \ldots, \pi_d)\Lambda_\mathfrak q =
\mathfrak q\Lambda_\mathfrak q$,

1. $\pi_1^n, \ldots, \pi_d^n \in I$, and

1. for $i = 1, \ldots, d$ we have

$$
\text{Ann}_{\Lambda/(\pi_1^e, \ldots, \pi_{i - 1}^e)\Lambda}(\pi_i) =
\text{Ann}_{\Lambda/(\pi_1^e, \ldots, \pi_{i - 1}^e)\Lambda}(\pi_i^2).
$$

**Proof.** 
Set $S = \Lambda \setminus \mathfrak q$ so that
$\Lambda_\mathfrak q = S^{-1}\Lambda$.
First pick $\pi_1, \ldots, \pi_d$ with (1) which is possible
as $\Lambda_\mathfrak q$ is regular. By assumption
$\pi_i^n \in I\Lambda_\mathfrak q$. Thus we can find
$s_1, \ldots, s_d \in S$ such that $s_i\pi_i^n \in I$.
Replacing $\pi_i$ by $s_i\pi_i$ we get (2).
Note that (1) and (2) are preserved by further multiplying by elements of $S$.
Suppose that (3) holds for $i = 1, \ldots, t$ for some
$t \in \{0, \ldots, d\}$. Note that
$\pi_1, \ldots, \pi_d$ is a regular sequence in $S^{-1}\Lambda$, see
Algebra, Lemma [AG-CA-12, Theorem 6.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/regular-sequences-depth-and-cohen-macaulay-modules.html).
In particular $\pi_1^e, \ldots, \pi_t^e, \pi_{t + 1}$ is a
regular sequence in $S^{-1}\Lambda = \Lambda_\mathfrak q$ by
Algebra, Lemma [AG-CA-12, Proposition 1.3](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/regular-sequences-depth-and-cohen-macaulay-modules.html).
Hence we see that

$$
\text{Ann}_{S^{-1}\Lambda/(\pi_1^e, \ldots, \pi_{i - 1}^e)}(\pi_i) =
\text{Ann}_{S^{-1}\Lambda/(\pi_1^e, \ldots, \pi_{i - 1}^e)}(\pi_i^2).
$$

Thus we get (3) for $i = t + 1$ after replacing $\pi_{t + 1}$ by $s\pi_{t + 1}$
for some $s \in S$ by Lemma [D.31](#smoothing-lemma-ogoma). By induction on $t$ this
produces a sequence satisfying (1), (2), and (3).
 ∎

<a id="smoothing-lemma-resolve-special"></a>

#### Lemma D.33: resolve special

*Adapted from the Stacks project, smoothing.tex, lines 2351–2430.*

Let $k \to A \to \Lambda \supset \mathfrak q$ be as in
Situation [D.27](#smoothing-situation-local) where

1. $k$ is a field,

1. $\Lambda$ is Noetherian,

1. $\mathfrak q$ is minimal over $\mathfrak h_A$,

1. $\Lambda_\mathfrak q$ is a regular local ring, and

1. the field extension $\kappa(\mathfrak q)/k$ is separable.

Then $k \to A \to \Lambda \supset \mathfrak q$ can be resolved.

**Proof.** 
If $d=\dim(\Lambda_\mathfrak q)=0$, the regular local target is its residue field. The separability assumption in the sense of Definition [F.5](#algebra-definition-separable-field-extension), together with Lemma [F.23](#algebra-lemma-colimit-syntomic), writes this residue field as a filtered colimit of smooth $k$-algebras. Since $A$ is finitely presented over $k$, Lemma [F.90](#algebra-lemma-when-colimit) factors $A\to\Lambda_\mathfrak q$ through one such algebra. Lemma [D.30](#smoothing-lemma-delocalize-height-zero) delocalizes the resulting height-zero solution. Skip the positive-length parameter and sequence-lifting steps. The remaining argument treats $d>0$.

Set $d = \dim \Lambda_\mathfrak q$. Set $R = k[x_1, \ldots, x_d]$.
Put $I=H_{A/k}\Lambda$, so $\mathfrak h_A=\sqrt I$. Since
$\mathfrak q$ is minimal over $\sqrt I$, the radical of
$I\Lambda_\mathfrak q$ is the maximal ideal of the Noetherian local
ring $\Lambda_\mathfrak q$. Choose finitely many generators of that
maximal ideal. Each has a power in $I\Lambda_\mathfrak q$; expanding
monomials of sufficiently high total degree gives an integer $n>0$
with $\mathfrak q^n\Lambda_\mathfrak q\subset I\Lambda_\mathfrak q$.
Choose generators $a_1, \ldots, a_r$ of $H_{A/k}$. Set

$$
B = A[x_1, \ldots, x_d, z_{ij}]/(x_i^n - \sum z_{ij}a_j)
$$

Each $B_{a_j}$ is smooth over $R$ because it is a polynomial
algebra over $A_{a_j}[x_1, \ldots, x_d]$ and $A_{a_j}$ is smooth over $k$.
Hence $B_{x_i}$ is smooth over $R$. Let $B \to C$ be the $R$-algebra
map constructed in Lemma [D.9](#smoothing-lemma-improve-presentation)
which comes with a $R$-algebra retraction $C \to B$. In particular
a map $C \to \Lambda$ fitting into the diagram below.
By construction $C_{x_i}$ is a smooth $R$-algebra with
$\Omega_{C_{x_i}/R}$ free. Hence we can find $c > 0$
such that $x_i^c$ is strictly standard in $C/R$, see
Lemma [D.15](#smoothing-lemma-compare-standard).
Now choose $\pi_1, \ldots, \pi_d \in \Lambda$ as in
Lemma [D.32](#smoothing-lemma-find-sequence)
where $n = n$, $e = 8c$, $\mathfrak q = \mathfrak q$ and $I = H_{A/k}\Lambda$.
Thus $\pi_i^n$ belongs to the actual ideal generated by the images of
$a_j$, rather than merely to its radical.
Write $\pi_i^n = \sum \lambda_{ij} a_j$ for some $\lambda_{ij} \in \Lambda$.
There is a map $B \to \Lambda$ given by $x_i \mapsto \pi_i$
and $z_{ij} \mapsto \lambda_{ij}$. Set $R = k[x_1, \ldots, x_d]$.
Diagram

$$
\begin{gathered}
R \xrightarrow{} B \\
B \xrightarrow{} \Lambda \\
k \xrightarrow{} R \\
k \xrightarrow{} A \\
A \xrightarrow{} B \\
A \xrightarrow{} \Lambda
\end{gathered}
$$

Now we apply
Lemma [D.28](#smoothing-lemma-lift-solution)
to $R \to C \to \Lambda \supset \mathfrak q$
and the sequence of elements $x_1^c, \ldots, x_d^c$ of $R$.
Assumption (2) is clear. Assumption (1) holds for $R$
by inspection and for $\Lambda$ by our choice of
$\pi_1, \ldots, \pi_d$. (Note that if
$\text{Ann}_\Lambda(\pi) = \text{Ann}_\Lambda(\pi^2)$, then we have
$\text{Ann}_\Lambda(\pi) = \text{Ann}_\Lambda(\pi^c)$ for all $c > 0$.)
Thus it suffices to resolve

$$
R/(x_1^e, \ldots, x_d^e) \to C/(x_1^e, \ldots, x_d^e) \to
\Lambda/(\pi_1^e, \ldots, \pi_d^e) \supset
\mathfrak q/(\pi_1^e, \ldots, \pi_d^e)
$$

for $e = 8c$. By
Lemma [D.30](#smoothing-lemma-delocalize-height-zero)
it suffices to resolve this after localizing at $\mathfrak q$.
But since $x_1, \ldots, x_d$ map to a regular sequence
in $\Lambda_\mathfrak q$ we see that $R_\mathfrak p \to \Lambda_\mathfrak q$
is flat, see Algebra, Lemma [F.46](#algebra-lemma-flat-over-regular). Hence

$$
R_\mathfrak p/(x_1^e, \ldots, x_d^e) \to
\Lambda_\mathfrak q/(\pi_1^e, \ldots, \pi_d^e)
$$

is a flat ring map of Artinian local rings.
Moreover, this map induces a separable field extension
on residue fields by assumption. Thus this map is a filtered colimit
of smooth algebras by
Algebra, Lemma [F.23](#algebra-lemma-colimit-syntomic)
and Proposition [D.18](#smoothing-proposition-lift).
Existence of the desired solution follows from
Algebra, Lemma [F.90](#algebra-lemma-when-colimit).
 ∎

### Inseparable residue fields

<a id="smoothing-section-inseparable"></a>

In this section we explain how to solve a local problem in the case
of an inseparable residue field extension.

<a id="smoothing-lemma-helper"></a>

#### Lemma D.34: helper

*Adapted from the Stacks project, smoothing.tex, lines 2444–2549.*

Let $k$ be a field of characteristic $p > 0$.
Let $(\Lambda, \mathfrak m, K)$ be an Artinian local $k$-algebra.
Assume that $\dim H_1(L_{K/k}) < \infty$.
Then $\Lambda$ is a filtered colimit of Artinian
local $k$-algebras $A$ with each map $A \to \Lambda$ flat, with
$\mathfrak m_A \Lambda = \mathfrak m$, and with
$A$ essentially of finite type over $k$.

**Proof.** 
Note that the flatness of $A \to \Lambda$ implies that $A \to \Lambda$
is injective, so the lemma really tells us that $\Lambda$ is a
directed union of these types of subrings $A \subset \Lambda$.
Let $n$ be the minimal integer such that $\mathfrak m^n = 0$.
We will prove this lemma by induction on $n$. The case $n = 1$ is clear
as a field extension is a union of finitely generated field extensions.

Pick $\lambda_1, \ldots, \lambda_d \in \mathfrak m$ which generate
$\mathfrak m$. As $K$ is formally smooth over $\mathbf{F}_p$ (see
Algebra, Lemma [F.49](#algebra-lemma-formally-smooth-extensions-easy)) we can
find a ring map $\sigma : K \to \Lambda$ which is a section of the
quotient map $\Lambda \to K$. In general $\sigma$ is **not**
a $k$-algebra map. Given $\sigma$ we define

$$
\Psi_\sigma : K[x_1, \ldots, x_d] \longrightarrow \Lambda
$$

using $\sigma$ on elements of $K$ and mapping $x_i$ to $\lambda_i$.
Claim: there exists a $\sigma : K \to \Lambda$
and a subfield $k \subset F \subset K$ finitely generated over $k$
such that the image of $k$ in $\Lambda$ is contained in
$\Psi_\sigma(F[x_1, \ldots, x_d])$.

We will prove the claim by induction on the least integer $n$ such that
$\mathfrak m^n = 0$. It is clear for $n = 1$. If $n > 1$ set
$I = \mathfrak m^{n - 1}$ and $\Lambda' = \Lambda/I$.
By induction we may assume
given $\sigma' : K \to \Lambda'$ and $k \subset F' \subset K$ finitely
generated such that the image of $k \to \Lambda \to \Lambda'$
is contained in $A' = \Psi_{\sigma'}(F'[x_1, \ldots, x_d])$.
Denote $\tau' : k \to A'$ the induced map.
Choose a lift $\sigma : K \to \Lambda$ of $\sigma'$ (this is possible
by the formal smoothness of $K/\mathbf{F}_p$ we mentioned above).
For later reference we note that we can change $\sigma$ to
$\sigma + D$ for some derivation $D : K \to I$.
Set $A = F'[x_1, \ldots, x_d]/(x_1, \ldots, x_d)^n$.
Then $\Psi_\sigma$ induces a ring map
$\Psi_\sigma : A \to \Lambda$. The composition with the
quotient map $\Lambda \to \Lambda'$ induces a surjective
map $A \to A'$ with nilpotent kernel.
Choose a lift $\tau : k \to A$ of $\tau'$ (possible as $k/\mathbf{F}_p$
is formally smooth). Thus we obtain two maps $k \to \Lambda$, namely
$\Psi_\sigma \circ \tau : k \to \Lambda$ and the given map $i : k \to \Lambda$.
These maps agree modulo $I$, whence the difference is a
derivation $\theta = i - \Psi_\sigma \circ \tau : k \to I$.
Note that if we change $\sigma$ into $\sigma + D$ then we change
$\theta$ into $\theta - D|_k$.

Choose a set of elements $\{y_j\}_{j \in J}$ of $k$ whose differentials
$\text{d}y_j$ form a basis of $\Omega_{k/\mathbf{F}_p}$. The Jacobi-Zariski
sequence for $\mathbf{F}_p \subset k \subset K$ is

$$
0 \to H_1(L_{K/k}) \to \Omega_{k/\mathbf{F}_p} \otimes K \to
\Omega_{K/\mathbf{F}_p} \to \Omega_{K/k} \to 0
$$

As $\dim H_1(L_{K/k}) < \infty$ we can find a finite subset $J_0 \subset J$
such that the image of the first map is contained in
$\bigoplus_{j \in J_0} K\text{d}y_j$. Hence the elements
$\text{d}y_j$, $j \in J \setminus J_0$ map to $K$-linearly independent
elements of $\Omega_{K/\mathbf{F}_p}$. Therefore we can choose
a $D : K \to I$ such that $\theta - D|_k = \xi \circ \text{d}$
where $\xi$ is a composition

$$
\Omega_{k/\mathbf{F}_p} = \bigoplus\nolimits_{j \in J} k \text{d}y_j
\longrightarrow \bigoplus\nolimits_{j \in J_0} k \text{d}y_j
\longrightarrow I
$$

Let $f_j = \xi(\text{d}y_j) \in I$ for $j \in J_0$.
Change $\sigma$ into $\sigma + D$ as above. Then we see that
$\theta(a) = \sum_{j \in J_0} a_j f_j$ for $a \in k$ where
$\text{d}a = \sum a_j \text{d}y_j$ in $\Omega_{k/\mathbf{F}_p}$.
Note that $I$ is generated by the monomials
$\lambda^E = \lambda_1^{e_1} \ldots \lambda_d^{e_d}$ of
total degree $|E| = \sum e_i = n - 1$ in $\lambda_1, \ldots, \lambda_d$.
Write $f_j = \sum_E c_{j, E} \lambda^E$ with $c_{j, E} \in K$.
Replace $F'$ by $F = F'(c_{j, E})$. Then the claim holds.

Choose $\sigma$ and $F$ as in the claim. The kernel of $\Psi_\sigma$ is
generated by finitely many polynomials
$g_1, \ldots, g_t \in K[x_1, \ldots, x_d]$ and we may assume their
coefficients are in $F$ after enlarging $F$ by adjoining finitely many
elements. In this case it is clear that the map
$A = F[x_1, \ldots, x_d]/(g_1, \ldots, g_t) \to
K[x_1, \ldots, x_d]/(g_1, \ldots, g_t) = \Lambda$ is flat.
By the claim $A$ is a $k$-subalgebra of $\Lambda$.
It is clear that $\Lambda$ is the filtered colimit of these
algebras, as $K$ is the filtered union of the subfields $F$.
Finally, these algebras are essentially of finite type over $k$ by
Algebra, Lemma
[F.40](#algebra-lemma-essentially-of-finite-type-into-artinian-local).
 ∎

<a id="smoothing-artinian-denominator-enlargement"></a>

#### Lemma D.34A: Artinian denominator enlargement

Let $k$ have characteristic $p>0$. Let $A\to B$ be a flat local map
of Noetherian Artinian local $k$-algebras, with
$\mathfrak m_AB=\mathfrak m_B$, and suppose
$\mathfrak m_B^n=0$. Write $F$ and $K$ for their residue fields.
For finitely many units $b_j\in B$, there is a factorization
$A\to A'\to B$ by local maps such that $A\to A'$ is essentially
smooth, $A'\to B$ is faithfully flat,
$\mathfrak m_{A'}B=\mathfrak m_B$, and a $p$-power of each $b_j$
belongs to $A'$. If a residue $\bar b_j$ is transcendental over the
current residue field, the construction adjoins $b_j$ itself. The
residue extension $F'/F$ is a finite tower of simple transcendental
and finite separable extensions.

**Proof.** Treat one unit $b$ at a time. If its residue $\beta$ is
transcendental over $F$, use
$A'=A[T]_{\mathfrak m_AA[T]}$ with $T\mapsto b$.
Its residue field is $F(\beta)$: every nonzero polynomial in $F[T]$
is inverted. Each inverted element maps to a unit of $B$, so the map
is defined and local. This is an essentially smooth Artinian local
ring, with $\mathfrak m_{A'}=\mathfrak m_AA'$.

If $\beta$ is algebraic over $F$, choose a $p$-power $q_0$ for which
$\beta^{q_0}$ is separable over $F$, by the inseparable exponent
calculation already proved. Lift the monic separable minimal
polynomial of $\beta^{q_0}$ from $F[T]$ to $h\in A[T]$ and put
$A'=A[T]/(h)$. It is finite free over $A$. Its quotient modulo
$\mathfrak m_A$ is the field $F(\beta^{q_0})$, and
$\mathfrak m_AA'$ is nilpotent, so $A'$ is Artinian local with this
maximal ideal. Bézout for the relatively prime residue polynomials
$\bar h,\bar h'$ makes $h'$ a unit modulo $\mathfrak m_AA'$; lifting
its inverse across a nilpotent ideal makes it a unit in $A'$.
The square Jacobian calculation, AG-CA-17, Theorem 4.1 and Section 6,
therefore makes $A'$ étale. The simple-root Hensel proof in
AG-CA-19, Theorem 5.1, lifts the specified residue root in the
Artinian local ring $B$ and gives $A'\to B$. This is exactly the
finite étale lifting construction in
[F.54](#algebra-lemma-henselian-cat-finite-etale), written here in
its consumed form. If $\beta\in F$, use instead $A'=A$, $q_0=1$.

In both cases $A'$ is flat over $A$, and
$A'/\mathfrak m_AA'=F'$, its residue field. A free $A$-resolution of
$F$ therefore becomes a free $A'$-resolution of $F'$ after tensoring.
Tensor it further with $B$. Flatness of $B$ over $A$ gives

$$
\operatorname{Tor}^{A'}_1(F',B)=\operatorname{Tor}^{A}_1(F,B)=0.
$$

The Noetherian local criterion, AG-CA-08, Theorem 4.2, applied with
finite $B$-module $B$, proves that $A'\to B$ is flat. It is local and
hence faithfully flat, so in particular injective. Its maximal
ideal still generates $\mathfrak m_B$.

In the algebraic case choose $x\in A'$ with residue
$\beta^{-q_0}$. It is a unit. Then $xb^{q_0}-1\in\mathfrak m_B$.
For a $p$-power $q_1\ge n$, Frobenius gives
$(xb^{q_0})^{q_1}=1$, whence
$b^{q_0q_1}=x^{-q_1}\in A'$. In the transcendental case $b$ is
already present, so any $p$-power may be used. Repeating the finite
construction proves every assertion.

We also record its differential effect, used immediately below.
For a simple transcendental residue extension the polynomial
presentation and localization give
$\Omega_{F(\beta)/k}=(\Omega_{F/k}\otimes_FF(\beta))\oplus
F(\beta)\,d\beta$. A finite separable residue extension gives the
same old differential space after tensoring: its monic separable
presentation has invertible derivative, so its relative conormal
complex is acyclic. The field Jacobi–Zariski sequence
[F.131](#more-algebra-lemma-transitivity-gamma) likewise gives in
both cases

$$
H_1(L_{F'/k})=H_1(L_{F/k})\otimes_FF'.
$$

These are natural identifications, and composition gives them for
the finite tower. Thus the image of this first homology in
$H_1(L_{K/k})$ is unchanged. ∎

<a id="smoothing-lemma-solution-modulo"></a>

#### Lemma D.35: solution modulo

*Adapted from the Stacks project, smoothing.tex, lines 2551–2621.*

Let $k$ be a field of characteristic $p > 0$.
Let $\Lambda$ be a Noetherian geometrically regular $k$-algebra.
Let $\mathfrak q \subset \Lambda$ be a prime ideal.
Let $n \geq 1$ be an integer and let
$E \subset \Lambda_\mathfrak q/\mathfrak q^n\Lambda_\mathfrak q$
be a finite subset.
Then we can find $m \geq 0$ and
$\varphi : k[y_1, \ldots, y_m] \to \Lambda$ with the following properties

1. setting $\mathfrak p = \varphi^{-1}(\mathfrak q)$ we have
$\mathfrak q\Lambda_\mathfrak q = \mathfrak p \Lambda_\mathfrak q$
and $k[y_1, \ldots, y_m]_\mathfrak p \to \Lambda_\mathfrak q$ is flat,

1. there is a factorization by homomorphisms of local Artinian rings

$$
k[y_1, \ldots, y_m]_\mathfrak p/\mathfrak p^n k[y_1, \ldots, y_m]_\mathfrak p
\to D \to
\Lambda_\mathfrak q/\mathfrak q^n\Lambda_\mathfrak q
$$

where the first arrow is essentially smooth and the second is flat,

1. $E$ is contained in $D$ modulo $\mathfrak q^n\Lambda_\mathfrak q$.

**Proof.** Put $L=\Lambda_{\mathfrak q}$, with maximal ideal
$\mathfrak m$ and residue field $K$, and put $B=L/\mathfrak m^n$.
Geometric regularity and
[F.133](#more-algebra-proposition-characterization-geometrically-regular)
give an injection
$H_1(L_{K/k})\hookrightarrow\mathfrak m/\mathfrak m^2$, so this
first homology is finite-dimensional. By
[D.34](#smoothing-lemma-helper) choose an Artinian local subring
$A\subset B$ containing $E$, essentially of finite type over $k$,
such that $A\to B$ is faithfully flat and
$\mathfrak m_AB=\mathfrak m_B$. Write $F$ for its residue field.

Here one must ensure global representatives; an arbitrary such $A$
does not supply them. Choose a basis of the finite-dimensional space
$\Omega_{F/k}$ consisting of differentials $d\theta_j$ of elements
of $F$, and choose lifts $\widetilde\theta_j\in A$. Since
$L\twoheadrightarrow B$, represent each lift by a fraction
$a_j/b_j$ with $a_j\in\Lambda$ and $b_j\in\Lambda\setminus\mathfrak q$.

By the field left injection
[F.131](#more-algebra-lemma-transitivity-gamma),
$H_1(L_{F/k})\otimes_FK$ injects into $H_1(L_{K/k})$. Let $V$ be
its image in $\mathfrak m/\mathfrak m^2$ under the preceding
injection. If $n\ge2$, the equality
$\mathfrak m_AB=\mathfrak m_B$ shows that the images of elements
of $\mathfrak m_A$ span $\mathfrak m/\mathfrak m^2$ over $K$.
Choose finitely many $\widetilde\eta_i\in\mathfrak m_A$ whose images
form a complement to $V$. Lift each to a fraction $c_i/d_i\in L$
with $c_i\in\mathfrak q$ and
$d_i\in\Lambda\setminus\mathfrak q$. If $n=1$, choose instead
elements $c_i\in\mathfrak q$ whose classes form this complement;
their images in $B=K$ are zero, hence already belong to $A$. Use
$d_i=1$ in that case.

Apply [D.34A](#smoothing-artinian-denominator-enlargement) to this
finite list of denominators, as units of $B$. It enlarges $A$ to an
Artinian local subring $A'\subset B$ by an essentially smooth map,
retains faithful flatness to $B$ and the maximal-ideal equality,
and puts $b_j^{q_j},d_i^{r_i}$ in $A'$ for suitable $p$-powers.
Consequently the global elements

$$
a_jb_j^{q_j-1},\quad b_j^{q_j},\quad
c_id_i^{r_i-1},\quad d_i^{r_i}
$$

have images in $A'$: the first and third are the original fractional
lifts multiplied by the indicated powers. Let $F'$ be its residue
field. During the enlargement record also the global denominators
whose residues were adjoined transcendently; those denominators
themselves have images in $A'$.

The differentials of the residues of the first two displayed global
elements, together with those recorded transcendental denominators,
span $\Omega_{F'/k}$. Indeed the quotient identity
$\theta_j=(a_jb_j^{q_j-1})/b_j^{q_j}$ expresses every old
$d\theta_j$ in terms of their differentials. D.34A shows that only
the recorded transcendental differentials must be added; a finite
separable step adds none. Select a basis from this finite spanning
list, and denote its global representatives by
$\lambda_1,\ldots,\lambda_t\in\Lambda$. All their classes lie in
$A'$. This argument does not assert that $d(b_j^{q_j})=0$ inside
$\Omega_{F'/k}$: its root need not lie in $F'$.

The natural first-homology calculation at the end of D.34A gives
$H_1(L_{F'/k})=H_1(L_{F/k})\otimes_FF'$. Hence its image in
$\mathfrak m/\mathfrak m^2$ is still $V$. Define
$P'=k[y_1,\ldots,y_t]\to\Lambda$ using these $\lambda_j$, and let
$\mathfrak p'$ be the inverse image of $\mathfrak q$. Lemma
[F.109](#more-algebra-lemma-geometrically-regular-over-field)
proves that $P'_{\mathfrak p'}\to L$ is flat and that
$L/\mathfrak p'L$ is regular. More precisely, the proof of that
lemma identifies the image of
$(\mathfrak p'/\mathfrak p'^2)\otimes K$ in
$\mathfrak m/\mathfrak m^2$ with $V$. To check this identification,
write $K_0=\kappa(\mathfrak p')$. The chosen differential basis makes
$F'/K_0$ finite separable, by
[F.98](#more-algebra-lemma-cartier-equality) and the field
separability calculation. Its acyclic relative conormal complex
identifies $H_1(L_{K_0/k})\otimes_{K_0}K$ with
$H_1(L_{F'/k})\otimes_{F'}K$. The natural conormal square in F.109
then gives exactly the image $V$.

Set $\lambda_{t+i}=c_id_i^{r_i-1}$. These are global, have classes
in $A'$, and their cotangent classes are those of the original
$\widetilde\eta_i$ multiplied by the nonzero residues $d_i^{r_i}$.
They remain a complement to $V$, so they map to a regular system of
parameters of $L/\mathfrak p'L$. Let
$P=k[y_1,\ldots,y_m]$ append these variables and let
$\mathfrak p$ be its inverse image of $\mathfrak q$.
The local ring $P_{\mathfrak p}$ is obtained from
$P'_{\mathfrak p'}[y_{t+1},\ldots,y_m]$ at the prime generated by
$\mathfrak p'$ and the appended variables, since their residues are
zero. Its regular parameters consist of the old parameters and
these variables. Their images form a regular parameter list in
$L$: the old list is regular by F.109 and the new list is regular
on its regular quotient. The regular-base flatness lemma
[F.46](#algebra-lemma-flat-over-regular) gives flatness of
$P_{\mathfrak p}\to L$. Their classes form a basis of
$\mathfrak m/\mathfrak m^2$, so Nakayama gives
$\mathfrak pL=\mathfrak m$. This proves property (1).

Every global generator has its class in $A'$, so the polynomial map
to $B$ factors through $A'$. The elements outside $\mathfrak p$ map
to units of this local ring. Since
$\mathfrak p^n B=\mathfrak m^nB=0$ and $A'\hookrightarrow B$, the
factorization descends to

$$
P_{\mathfrak p}/\mathfrak p^n\longrightarrow A'\longrightarrow B.
$$

Its composite is flat by the flatness just proved and base change.
Faithful-flat descent of module flatness,
[F.48](#algebra-lemma-flatness-descends-more-general), makes the first
map flat. Also $\mathfrak pA'=\mathfrak m_{A'}$: both ideals become
$\mathfrak m_B$ in $B$, and faithful flatness detects equality of
ideals. The residue extension $F'/\kappa(\mathfrak p)=F'/K_0$ is
finite separable as above. The Artinian length-filtration proof
[F.40](#algebra-lemma-essentially-of-finite-type-into-artinian-local)
therefore makes $A'$ finite over $P_{\mathfrak p}/\mathfrak p^n$.
The source is Noetherian, so this is a finitely presented algebra.
Lemma [F.16](#algebra-lemma-characterize-etale) now proves that the
first map is étale. In particular it is essentially smooth.
Taking $D=A'$ proves properties (2) and (3), since $A\subset A'$
retains $E$. ∎

<a id="smoothing-lemma-enlarge-solution-modulo"></a>

#### Lemma D.36: enlarge solution modulo

*Adapted from the Stacks project, smoothing.tex, lines 2623–2669.*

Let $\varphi : k[y_1, \ldots, y_m] \to \Lambda$, $n$, $\mathfrak q$,
$\mathfrak p$ and

$$
k[y_1, \ldots, y_m]_\mathfrak p/\mathfrak p^n \to
D \to \Lambda_\mathfrak q/\mathfrak q^n \Lambda_\mathfrak q
$$

be as in Lemma [D.35](#smoothing-lemma-solution-modulo). Then for any
$\lambda \in \Lambda \setminus \mathfrak q$
there exists an integer $q > 0$ and a factorization

$$
k[y_1, \ldots, y_m]_\mathfrak p/\mathfrak p^n \to
D \to D' \to \Lambda_\mathfrak q/\mathfrak q^n \Lambda_\mathfrak q
$$

such that $D \to D'$ is an essentially smooth map of local Artinian rings,
the last arrow is flat, and $\lambda^q$ is in $D'$.

**Proof.** Put
$B=\Lambda_{\mathfrak q}/\mathfrak q^n\Lambda_{\mathfrak q}$.
The hypotheses of D.35 make $D\to B$ flat and local, hence
faithfully flat. Its maximal ideal generates that of $B$: the
maximal ideal of the polynomial Artinian source already generates
it by property (1), and its image in $D$ is the maximal ideal
because the first map in property (2) is local and essentially
smooth. Its closed fibre is a localization of a smooth algebra over
a field, hence regular by AG-CA-18, Theorem 2.1. It is Artinian local,
so its regular dimension is zero; its cotangent space is zero and
Nakayama makes its maximal ideal zero. Thus that fibre is a field,
which proves the asserted maximal-ideal equality. The equality also
holds directly in the étale construction of D.35. Apply
[D.34A](#smoothing-artinian-denominator-enlargement) to the unit
image of $\lambda$. It gives the required essentially smooth
Artinian extension $D\to D'$, flat final map, and a $p$-power
$q$ with $\lambda^q\in D'$. Composing with the original polynomial
source supplies the stated factorization. ∎

<a id="smoothing-lemma-resolve-general"></a>

#### Lemma D.37: resolve general

*Adapted from the Stacks project, smoothing.tex, lines 2671–3098.*

Let $k \to A \to \Lambda \supset \mathfrak q$ be as in
Situation [D.27](#smoothing-situation-local) where

1. $k$ is a field of characteristic $p > 0$,

1. $\Lambda$ is Noetherian and geometrically regular over $k$,

1. $\mathfrak q$ is minimal over $\mathfrak h_A$.

Then $k \to A \to \Lambda \supset \mathfrak q$ can be resolved.

**Proof.** 
The lemma is proven by the following steps in the given order.
We will justify each of these steps below.

1. Pick an integer $N > 0$ such that
$\mathfrak q^N\Lambda_\mathfrak q \subset H_{A/k}\Lambda_\mathfrak q$.

1. Pick generators $a_1, \ldots, a_t \in A$ of the ideal $H_{A/k}$.

1. Set $d = \dim(\Lambda_\mathfrak q)$.

1. Set $B = A[x_1, \ldots, x_d, z_{ij}]/(x_i^{2N} - \sum z_{ij}a_j)$.

1. Consider $B$ as a $k[x_1, \ldots, x_d]$-algebra and let
$B \to C$ be as in
Lemma [D.9](#smoothing-lemma-improve-presentation).
We also obtain a section $C \to B$.

1. Choose $c > 0$ such that each $x_i^c$
is strictly standard in $C$ over $k[x_1, \ldots, x_d]$.

1. Set $e=8c$ and $n=\max\{N+dc,\ d(e-1)+1\}$. This choice is made before defining $E$, $D$, and all subsequent factorizations.

1. Let $E \subset \Lambda_\mathfrak q/\mathfrak q^n\Lambda_\mathfrak q$
be the images of generators of $A$ as a $k$-algebra.

1. Choose an integer $m$ and a $k$-algebra map
$\varphi : k[y_1, \ldots, y_m] \to \Lambda$
and a factorization by local Artinian rings

$$
k[y_1, \ldots, y_m]_\mathfrak p/\mathfrak p^n k[y_1, \ldots, y_m]_\mathfrak p
\to D \to
\Lambda_\mathfrak q/\mathfrak q^n\Lambda_\mathfrak q
$$

such that the first arrow is essentially smooth, the second is flat,
$E$ is contained in $D$, with $\mathfrak p = \varphi^{-1}(\mathfrak q)$
the map $k[y_1, \ldots, y_m]_\mathfrak p \to \Lambda_\mathfrak q$ is
flat, and $\mathfrak p \Lambda_\mathfrak q = \mathfrak q \Lambda_\mathfrak q$.

1. Choose $\pi_1, \ldots, \pi_d \in \mathfrak p$ which map to a
regular system of parameters of $k[y_1, \ldots, y_m]_\mathfrak p$.

1. Let $R = k[y_1, \ldots, y_m, t_1, \ldots, t_d]$ and $\gamma_i = \pi_i t_i$.

1. If necessary modify the choice of $\pi_i$ such that
for $i = 1, \ldots, d$ we have 

$$
\text{Ann}_{R/(\gamma_1^e, \ldots, \gamma_{i - 1}^e)R}(\gamma_i)
=
\text{Ann}_{R/(\gamma_1^e, \ldots, \gamma_{i - 1}^e)R}(\gamma_i^2)
$$

1. There exist $\delta_1, \ldots, \delta_d \in \Lambda$,
$\delta_i \not \in \mathfrak q$ and a factorization
$D \to D' \to \Lambda_\mathfrak q/\mathfrak q^n\Lambda_\mathfrak q$
with $D'$ local Artinian, $D \to D'$ essentially smooth, the map
$D' \to \Lambda_\mathfrak q/\mathfrak q^n\Lambda_\mathfrak q$
flat such that, with $\pi_i' = \delta_i \pi_i$, we have for
$i = 1, \ldots, d$

1. $(\pi_i')^{2N} = \sum a_j\lambda_{ij}$ in $\Lambda$ where
$\lambda_{ij} \bmod \mathfrak q^n\Lambda_\mathfrak q$ is an element of $D'$,

1. $\text{Ann}_{\Lambda/({\pi'}_1^e, \ldots, {\pi'}_{i - 1}^e)}({\pi'}_i) =
\text{Ann}_{\Lambda/({\pi'}_1^e, \ldots, {\pi'}_{i - 1}^e)}({\pi'}_i^2)$,

1. $\delta_i \bmod \mathfrak q^n\Lambda_\mathfrak q$ is an element of $D'$.

1. Define $B \to \Lambda$ by sending $x_i$ to $\pi'_i$ and
$z_{ij}$ to $\lambda_{ij}$ found above. Define $C \to \Lambda$
by composing the map $B \to \Lambda$ with the retraction $C \to B$.

1. Map $R \to \Lambda$ by $\varphi$ on $k[y_1, \ldots, y_m]$
and by sending $t_i$ to $\delta_i$. Further introduce a map

$$
k[x_1, \ldots, x_d]
\longrightarrow
R = k[y_1, \ldots, y_m, t_1, \ldots, t_d]
$$

by sending $x_i$ to $\gamma_i = \pi_i t_i$.

1. It suffices to resolve

$$
R
\to
C \otimes_{k[x_1, \ldots, x_d]} R
\to
\Lambda \supset \mathfrak q
$$

1. Set $I = (\gamma_1^e, \ldots, \gamma_d^e) \subset R$.

1. It suffices to resolve

$$
R/I
\to
C \otimes_{k[x_1, \ldots, x_d]} R/I
\to
\Lambda/I\Lambda \supset \mathfrak q/I\Lambda
$$

1. We denote $\mathfrak r \subset R = k[y_1, \ldots, y_m, t_1, \ldots, t_d]$
the inverse image of $\mathfrak q$.

1. It suffices to resolve

$$
(R/I)_\mathfrak r \to
C \otimes_{k[x_1, \ldots, x_d]} (R/I)_\mathfrak r \to
\Lambda_\mathfrak q/I\Lambda_\mathfrak q
\supset
\mathfrak q\Lambda_\mathfrak q/I\Lambda_\mathfrak q
$$

1. Set $J = (\pi_1^e, \ldots, \pi_d^e)$ in $k[y_1, \ldots, y_m]$.

1. It suffices to resolve

$$
(R/JR)_\mathfrak p \to
C \otimes_{k[x_1, \ldots, x_d]} (R/JR)_\mathfrak p \to
\Lambda_\mathfrak q/J\Lambda_\mathfrak q
\supset
\mathfrak q\Lambda_\mathfrak q/J\Lambda_\mathfrak q
$$

1. It suffices to resolve

$$
(R/\mathfrak p^nR)_\mathfrak p \to
C \otimes_{k[x_1, \ldots, x_d]} (R/\mathfrak p^nR)_\mathfrak p \to
\Lambda_\mathfrak q/\mathfrak q^n\Lambda_\mathfrak q
\supset
\mathfrak q\Lambda_\mathfrak q/\mathfrak q^n\Lambda_\mathfrak q
$$

1. It suffices to resolve

$$
(R/\mathfrak p^nR)_\mathfrak p \to
B \otimes_{k[x_1, \ldots, x_d]} (R/\mathfrak p^nR)_\mathfrak p \to
\Lambda_\mathfrak q/\mathfrak q^n\Lambda_\mathfrak q
\supset
\mathfrak q\Lambda_\mathfrak q/\mathfrak q^n\Lambda_\mathfrak q
$$

1. The ring $D'[t_1, \ldots, t_d]$ is given the structure of an
$R_\mathfrak p/\mathfrak p^nR_\mathfrak p$-algebra by the given map
$k[y_1, \ldots, y_m]_\mathfrak p/\mathfrak p^n k[y_1, \ldots, y_m]_\mathfrak p
\to D'$ and by sending $t_i$ to $t_i$. It suffices to find a factorization

$$
B \otimes_{k[x_1, \ldots, x_d]} (R/\mathfrak p^nR)_\mathfrak p
\to D'[t_1, \ldots, t_d] \to
\Lambda_\mathfrak q/\mathfrak q^n\Lambda_\mathfrak q
$$

where the second arrow sends $t_i$ to $\delta_i$ and induces the given
homomorphism $D' \to \Lambda_\mathfrak q/\mathfrak q^n\Lambda_\mathfrak q$.

1. Such a factorization exists by our choice of $D'$ above.

We now give the justification for each of the steps, except that we
skip justifying the steps which just introduce notation.

Ad ([D.37 / power](#smoothing-lemma-resolve-general)). This is possible as $\mathfrak q$ is minimal
over $\mathfrak h_A = \sqrt{H_{A/k}\Lambda}$.

Ad ([D.37 / strictly standard](#smoothing-lemma-resolve-general)). Note that $A_{a_j}$ is smooth
over $k$. Hence $B_{a_j}$, which is isomorphic to a polynomial
algebra over $A_{a_j}[x_1, \ldots, x_d]$, is smooth over
$k[x_1, \ldots, x_d]$. Thus $B_{x_i}$ is smooth over $k[x_1, \ldots, x_d]$.
By Lemma [D.9](#smoothing-lemma-improve-presentation)
we see that $C_{x_i}$ is smooth over $k[x_1, \ldots, x_d]$
with finite free module of differentials. Hence some power of
$x_i$ is strictly standard in $C$ over $k[x_1, \ldots, x_d]$
by Lemma [D.15](#smoothing-lemma-compare-standard).

Ad ([D.37 / NP](#smoothing-lemma-resolve-general)). This follows by applying Lemma [D.35](#smoothing-lemma-solution-modulo).

Ad ([D.37 / choose pii](#smoothing-lemma-resolve-general)). Since
$k[y_1, \ldots, y_m]_\mathfrak p \to \Lambda_\mathfrak q$ is
flat and $\mathfrak p \Lambda_\mathfrak q = \mathfrak q \Lambda_\mathfrak q$
by construction
we see that $\dim(k[y_1, \ldots, y_m]_\mathfrak p) = d$ by
Algebra, Lemma [AG-CA-11, Theorem 5.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/dimension-theory-of-noetherian-local-rings.html).
Thus we can find $\pi_1, \ldots, \pi_d \in \mathfrak p$ which map to
a regular system of parameters in $k[y_1, \ldots, y_m]_\mathfrak p$.

Ad ([D.37 / modify pii](#smoothing-lemma-resolve-general)). By
Algebra, Lemma [AG-CA-12, Theorem 6.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/regular-sequences-depth-and-cohen-macaulay-modules.html)
any permutation of the sequence $\pi_1, \ldots, \pi_d$ is a
regular sequence in $k[y_1, \ldots, y_m]_\mathfrak p$. Hence
$\gamma_1 = \pi_1 t_1, \ldots, \gamma_d = \pi_d t_d$ is a regular
sequence in
$R_\mathfrak p = k[y_1, \ldots, y_m]_\mathfrak p[t_1, \ldots, t_d]$, see
Algebra, Lemma [F.75](#algebra-lemma-regular-sequence-in-polynomial-ring).
Let $S = k[y_1, \ldots, y_m] \setminus \mathfrak p$ so that
$R_\mathfrak p = S^{-1}R$. Note that $\pi_1, \ldots, \pi_d$
and $\gamma_1, \ldots, \gamma_d$
remain regular sequences if we multiply our $\pi_i$ by elements of $S$.
Suppose that

$$
\text{Ann}_{R/(\gamma_1^e, \ldots, \gamma_{i - 1}^e)R}(\gamma_i)
=
\text{Ann}_{R/(\gamma_1^e, \ldots, \gamma_{i - 1}^e)R}(\gamma_i^2)
$$

holds for $i = 1, \ldots, t$ for some $t \in \{0, \ldots, d\}$. Note that
$\gamma_1^e, \ldots, \gamma_t^e, \gamma_{t + 1}$ is a
regular sequence in $S^{-1}R$ by
Algebra, Lemma [AG-CA-12, Proposition 1.3](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/regular-sequences-depth-and-cohen-macaulay-modules.html).
Hence we see that

$$
\text{Ann}_{S^{-1}R/(\gamma_1^e, \ldots, \gamma_{i - 1}^e)}(\gamma_i) =
\text{Ann}_{S^{-1}R/(\gamma_1^e, \ldots, \gamma_{i - 1}^e)}(\gamma_i^2).
$$

Thus we get

$$
\text{Ann}_{R/(\gamma_1^e, \ldots, \gamma_t^e)R}(\gamma_{t + 1})
=
\text{Ann}_{R/(\gamma_1^e, \ldots, \gamma_t^e)R}(\gamma_{t + 1}^2)
$$

after replacing $\pi_{t + 1}$ by $s\pi_{t + 1}$ for some $s \in S$ by
Lemma [D.31](#smoothing-lemma-ogoma). By induction on $t$ this produces the desired
sequence.

Ad ([D.37 / choose deltai](#smoothing-lemma-resolve-general)). Let $S = \Lambda \setminus \mathfrak q$
so that $\Lambda_\mathfrak q = S^{-1}\Lambda$. Set
$\bar \Lambda = \Lambda_\mathfrak q/\mathfrak q^n \Lambda_\mathfrak q$.
Suppose that we have a $t \in \{0, \ldots, d\}$ and
$\delta_1, \ldots, \delta_t \in S$ and a factorization
$D \to D' \to \bar \Lambda$ as in ([D.37 / choose deltai](#smoothing-lemma-resolve-general))
such that (a), (b), (c) hold for $i = 1, \ldots, t$. We have
$\pi_{t + 1}^N \in H_{A/k}\Lambda_\mathfrak q$
as $\mathfrak q^N \Lambda_\mathfrak q \subset H_{A/k}\Lambda_\mathfrak q$
by ([D.37 / power](#smoothing-lemma-resolve-general)). Hence
$\pi_{t + 1}^N \in H_{A/k} \bar\Lambda$. Hence
$\pi_{t + 1}^N \in H_{A/k}D'$ as $D' \to \bar \Lambda$
is faithfully flat, see
Algebra, Lemma [AG-CA-08, Theorem 2.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/faithful-flatness-and-the-local-criterion-for-flatness.html).
Recall that $H_{A/k} = (a_1, \ldots, a_t)$.
Say $\pi_{t + 1}^N = \sum a_j d_j$ in $D'$ and choose
$c_j \in \Lambda_\mathfrak q$ lifting $d_j \in D'$. Then
$\pi_{t + 1}^N = \sum c_j a_j + \epsilon$ with
$\epsilon \in \mathfrak q^n\Lambda_\mathfrak q \subset
\mathfrak q^{n - N}H_{A/k}\Lambda_\mathfrak q$.
Write $\epsilon = \sum a_j c'_j$ for some
$c'_j \in \mathfrak q^{n - N}\Lambda_\mathfrak q$.
Hence $\pi_{t + 1}^{2N} = \sum (\pi_{t + 1}^N c_j + \pi_{t + 1}^N c'_j) a_j$.
Note that $\pi_{t + 1}^Nc'_j$ maps to zero in $\bar \Lambda$; this trivial
but key observation will ensure later that (a) holds.
Now we choose $s \in S$ such that there exist
$\mu_{t + 1j} \in \Lambda$ such that on the one hand
$\pi_{t + 1}^N c_j + \pi_{t + 1}^N c'_j = \mu_{t + 1j}/s^{2N}$
in $S^{-1}\Lambda$ and on the other
$(s \pi_{t + 1})^{2N} = \sum \mu_{t + 1j}a_j$
in $\Lambda$. Here are the exact denominator-clearing details. Let $u_j=\pi_{t+1}^N(c_j+c'_j)$ in $S^{-1}\Lambda$. Choose one $s_0\in S$ with $s_0^{2N}u_j=\widetilde\mu_j\in\Lambda$ for every $j$. The error $r=(s_0\pi_{t+1})^{2N}-\sum_j a_j\widetilde\mu_j$ vanishes in $S^{-1}\Lambda$, so some $v\in S$ annihilates $r$. Set $s=s_0v$ and $\mu_{t+1j}=v^{2N}\widetilde\mu_j$. Then the denominator identity still holds and the relation is exact because its error is $v^{2N}r=0$. Its residue is $s^{2N}\pi_{t+1}^Nd_j$, since $\pi_{t+1}^Nc'_j$ vanishes modulo $\mathfrak q^n$. We may further replace $s$ by
a power and enlarge $D'$ such that $s$ maps to an element of $D'$.
With these choices $\mu_{t + 1j}$ maps to $s^{2N}\pi_{t+1}^N d_j$ which is
an element of $D'$. Note that $\pi_1, \ldots, \pi_d$ are a regular
sequence of parameters in $S^{-1}\Lambda$ by our
choice of $\varphi$. Hence $\pi_1, \ldots, \pi_d$ forms a regular sequence
in $\Lambda_\mathfrak q$ by
Algebra, Lemma [AG-CA-12, Theorem 6.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/regular-sequences-depth-and-cohen-macaulay-modules.html).
It follows that ${\pi'}_1^e, \ldots, {\pi'}_t^e, s\pi_{t + 1}$ is a
regular sequence in $S^{-1}\Lambda$ by
Algebra, Lemma [AG-CA-12, Proposition 1.3](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/regular-sequences-depth-and-cohen-macaulay-modules.html).
Thus we get

$$
\text{Ann}_{S^{-1}\Lambda/({\pi'}_1^e, \ldots, {\pi'}_t^e)}(s\pi_{t + 1}) =
\text{Ann}_{S^{-1}\Lambda/({\pi'}_1^e, \ldots, {\pi'}_t^e)}((s\pi_{t + 1})^2).
$$

Hence we may apply Lemma [D.31](#smoothing-lemma-ogoma) to find an $s' \in S$
such that

$$
\text{Ann}_{\Lambda/({\pi'}_1^e, \ldots, {\pi'}_t^e)}((s')^qs\pi_{t + 1})
=
\text{Ann}_{\Lambda/({\pi'}_1^e, \ldots, {\pi'}_t^e)}(((s')^qs\pi_{t + 1})^2).
$$

for any $q > 0$. By Lemma [D.36](#smoothing-lemma-enlarge-solution-modulo)
we can choose $q$ and enlarge $D'$ such that $(s')^q$ maps to an element
of $D'$. Setting $\delta_{t + 1} = (s')^qs$ we conclude that
(a), (b), (c) hold for $i = 1, \ldots, t + 1$. For (a) note that
$\lambda_{t + 1j} = (s')^{2Nq}\mu_{t + 1j}$ works.
By induction on $t$ we win.

Ad ([D.37 / first solve](#smoothing-lemma-resolve-general)). By construction the radical of
$H_{(C \otimes_{k[x_1, \ldots, x_d]} R)/R} \Lambda$ contains
$\mathfrak h_A$. Namely, the elements $a_j \in H_{A/k}$
map to elements of $H_{B/k[x_1, \ldots, x_d]}$, hence map to elements
of $H_{C/k[x_1, \ldots, x_d]}$, hence $a_j \otimes 1$ map to elements of
$H_{C \otimes_{k[x_1, \ldots, x_d]} R/R}$. Moreover, if we have a solution
$C \otimes_{k[x_1, \ldots, x_d]} R \to T \to \Lambda$ of

$$
R
\to
C \otimes_{k[x_1, \ldots, x_d]} R
\to
\Lambda \supset \mathfrak q
$$

then $H_{T/R} \subset H_{T/k}$ as $R$ is smooth over $k$.
Hence $T$ will also be a solution for
the original situation $k \to A \to \Lambda \supset \mathfrak q$.

Ad ([D.37 / second resolve](#smoothing-lemma-resolve-general)). If $d=0$, the parameter lists and the ideal $I$ are empty, and this step does nothing; the localized regular target is a field. For $d>0$, this follows on applying
Lemma [D.28](#smoothing-lemma-lift-solution) to
$R \to C \otimes_{k[x_1, \ldots, x_d]} R
\to \Lambda \supset \mathfrak q$ and the sequence of
elements $\gamma_1^c, \ldots, \gamma_d^c$. We note that since $x_i^c$
are strictly standard in $C$ over $k[x_1, \ldots, x_d]$ the elements
$\gamma_i^c$ are strictly standard in $C \otimes_{k[x_1, \ldots, x_d]} R$
over $R$ by Lemma [D.7](#smoothing-lemma-strictly-standard-base-change).
The other assumption of Lemma [D.28](#smoothing-lemma-lift-solution) holds by steps
([D.37 / modify pii](#smoothing-lemma-resolve-general)) and ([D.37 / choose deltai](#smoothing-lemma-resolve-general)).

Ad ([D.37 / third resolve](#smoothing-lemma-resolve-general)). Apply Lemma [D.30](#smoothing-lemma-delocalize-height-zero)
to the situation in ([D.37 / second resolve](#smoothing-lemma-resolve-general)). In the rest of the
arguments the target ring is local Artinian, hence we are looking for
a factorization by a smooth algebra $T$ over the source ring.

Ad ([D.37 / fifth resolve](#smoothing-lemma-resolve-general)).
Suppose that $C \otimes_{k[x_1, \ldots, x_d]} (R/JR)_\mathfrak p \to
T \to \Lambda_\mathfrak q/J\Lambda_\mathfrak q$ is a solution to

$$
(R/JR)_\mathfrak p \to
C \otimes_{k[x_1, \ldots, x_d]} (R/JR)_\mathfrak p \to
\Lambda_\mathfrak q/J\Lambda_\mathfrak q
\supset
\mathfrak q\Lambda_\mathfrak q/J\Lambda_\mathfrak q
$$

Then $C \otimes_{k[x_1, \ldots, x_d]} (R/I)_\mathfrak r \to T_\mathfrak r \to
\Lambda_\mathfrak q/I\Lambda_\mathfrak q$
is a solution to the situation in ([D.37 / third resolve](#smoothing-lemma-resolve-general)).

Ad ([D.37 / sixth resolve](#smoothing-lemma-resolve-general)). Our corrected choice $n\geq d(e-1)+1$ is large enough so that
$\mathfrak p^nk[y_1, \ldots, y_m]_\mathfrak p \subset J_\mathfrak p$
and $\mathfrak q^n \Lambda_\mathfrak q \subset J\Lambda_\mathfrak q$.
Hence if we have a solution
$C \otimes_{k[x_1, \ldots, x_d]} (R/\mathfrak p^nR)_\mathfrak p \to
T \to \Lambda_\mathfrak q/\mathfrak q^n\Lambda_\mathfrak q$
of ([D.37 / fifth resolve](#smoothing-lemma-resolve-general))
then we can take $T/JT$ as the solution for
([D.37 / sixth resolve](#smoothing-lemma-resolve-general)).

Ad ([D.37 / seventh resolve](#smoothing-lemma-resolve-general)). This is true because we have a
section $C \to B$ in the category of $R$-algebras.

Ad ([D.37 / eighth resolve](#smoothing-lemma-resolve-general)). This is true because $D'$ is
essentially smooth over the local Artinian ring
$k[y_1, \ldots, y_m]_\mathfrak p/\mathfrak p^n k[y_1, \ldots, y_m]_\mathfrak p$
and

$$
R_\mathfrak p/\mathfrak p^nR_\mathfrak p =
k[y_1, \ldots, y_m]_\mathfrak p/
\mathfrak p^n k[y_1, \ldots, y_m]_\mathfrak p[t_1, \ldots, t_d].
$$

Hence $D'[t_1, \ldots, t_d]$ is a filtered colimit of smooth
$R_\mathfrak p/\mathfrak p^nR_\mathfrak p$-algebras and
$B \otimes_{k[x_1, \ldots, x_d]} (R_\mathfrak p/\mathfrak p^nR_\mathfrak p)$
factors through one of these.

Ad ([D.37 / done](#smoothing-lemma-resolve-general)). The final twist of the proof is that we cannot
just use the map $B \to D'$ which maps $x_i$ to the image of $\pi_i'$
in $D'$ and $z_{ij}$ to the image of $\lambda_{ij}$ in $D'$
because we need the diagram

$$
\begin{gathered}
B \xrightarrow{} D'[t_1, \ldots, t_d] \\
k[x_1, \ldots, x_d] \xrightarrow{} R_\mathfrak p/\mathfrak p^nR_\mathfrak p \\
k[x_1, \ldots, x_d] \xrightarrow{} B \\
R_\mathfrak p/\mathfrak p^nR_\mathfrak p \xrightarrow{} D'[t_1, \ldots, t_d]
\end{gathered}
$$

to commute and we need the composition
$B \to D'[t_1, \ldots, t_d] \to
\Lambda_\mathfrak q/\mathfrak q^n\Lambda_\mathfrak q$
to be the map of ([D.37 / map B Lambda](#smoothing-lemma-resolve-general)).
This requires us to map $x_i$ to the image of
$\pi_i t_i$ in $D'[t_1, \ldots, t_d]$.
Hence we map $z_{ij}$ to the image of
$\lambda_{ij} t_i^{2N} / \delta_i^{2N}$ in $D'[t_1, \ldots, t_d]$
and everything is clear.
 ∎

### The main theorem

<a id="smoothing-section-main"></a>

In this section we wrap up the discussion.

<a id="smoothing-theorem-popescu"></a>

#### Theorem D.38: popescu

*Adapted from the Stacks project, smoothing.tex, lines 3112–3135.*

Any regular homomorphism of Noetherian rings is a filtered colimit
of smooth ring maps.

**Proof.** 
By Lemma [D.26](#smoothing-lemma-reduce-to-field)
it suffices to prove this for $k \to \Lambda$
where $\Lambda$ is Noetherian and geometrically regular over $k$.
Let $k \to A \to \Lambda$ be a factorization with $A$ a finite type
$k$-algebra. It suffices to construct a factorization
$A \to B \to \Lambda$ with $B$ of finite type such that
$\mathfrak h_B = \Lambda$, see Lemma [D.8](#smoothing-lemma-final-solve).
Hence we may perform Noetherian induction on the ideal $\mathfrak h_A$.
Pick a prime $\mathfrak q \supset \mathfrak h_A$ such that
$\mathfrak q$ is minimal over $\mathfrak h_A$.
It now suffices to resolve $k \to A \to \Lambda \supset \mathfrak q$
(as defined in the text following Situation [D.27](#smoothing-situation-local)).
If the characteristic of $k$ is zero, this follows from
Lemma [D.33](#smoothing-lemma-resolve-special).
If the characteristic of $k$ is $p > 0$, this follows from
Lemma [D.37](#smoothing-lemma-resolve-general).
 ∎

## 5. Foundation statements and their free-source proofs

All resolution comparisons, balance of Tor and connecting exact sequences used in the following flatness arguments are proved for arbitrary modules in the earlier [AG-RG-S01, Lemma 1.A](AG-RG-S01.md#tor-calculus). This binds their homological inputs to a written programme proof before the approximation argument.

These proofs are included as mathematical text, rather than cited as substitutes for proofs. Their transitive dependencies are checked against the earlier programme locators and the open-obligation register in §6. Inclusion of a proof does not automatically close its unproved inputs.

<a id="cotangent-context"></a>

**Cotangent-complex context.** For a polynomial presentation $P=R[X_s]\twoheadrightarrow S$ with kernel $I$, write $\operatorname{NL}(P\to S)$ for the two-term complex $[I/I^2\to\bigoplus_sS\,dX_s]$ in degrees $-1,0$. The differential takes the class of $f$ to $df$. The canonical presentation is $R[X_s\mid s\in S]\to S$, $X_s\mapsto s$. For a commuting square of ring maps $R\to R'$, $S\to S'$, a presentation map is a map of these polynomial algebras lifting $S\to S'$. The full comparison and homotopy calculations below show independence of the polynomial presentation. Localization is likewise the displayed two-term localization proved at the corresponding foundation lemma, not an import of the whole cotangent chapter.

<a id="inseparable-exponent-context"></a>

**The inseparable exponent calculation.** Let $\alpha$ be algebraic over a field $F$ of characteristic $p$. Its irreducible polynomial is $f(T)=g(T^{p^s})$ for a maximal $s\geq0$. Such $s$ exists because $f$ has finite positive degree. Maximality gives $g'\ne0$. Any factorization of $g$ would give a factorization of $f$, so $g$ is irreducible, and its relatively prime derivative makes it separable. The element $\alpha^{p^s}$ is a root of $g$, hence is separable over $F$. This proves the field-theoretic exponent choice used in the enlargement argument.

<a id="dimension-context"></a>

**Dimension notation.** Krull dimension is the supremum of the lengths of finite chains of prime ideals; the height of a prime is the dimension of its localization. A system of parameters of a Noetherian local ring of dimension $d$ is a list of $d$ elements generating an ideal whose radical is the maximal ideal. Their existence is AG-CA-11, Theorem 2.1. Minimal primes, irreducible components and the dimension of polynomial local rings are supplied respectively by AG-CA-01, Theorems 4.1–4.3, AG-CA-09, Theorem 4.3, and AG-CA-11, Theorem 6.1. This paragraph fixes notation; it does not assert an additional dimension theorem. The separate dimension-in-a-neighbourhood and codimension arguments consumed below remain separately registered until matched or proved.

<a id="algebra-definition-lci"></a>

#### Definition F.1: lci

*Adapted from the Stacks project, algebra.tex, lines 37874–37881.*

A ring map $R \to S$ is called *syntomic*, or we say $S$ is a
*flat local complete intersection over $R$*
if it is flat, of finite presentation, and if all of its fibre rings
$S \otimes_R \kappa(\mathfrak p)$ are local complete intersections,
see Definition [F.2](#algebra-definition-lci-field).

<a id="algebra-definition-lci-field"></a>

#### Definition F.2: lci field

*Adapted from the Stacks project, algebra.tex, lines 37249–37264.*

Let $k$ be a field.
Let $S$ be a finite type $k$-algebra.

1. We say that $S$ is a *global complete intersection over $k$*
if there exists a presentation $S = k[x_1, \ldots, x_n]/(f_1, \ldots, f_c)$
such that $\dim(S) = n - c$.

1. We say that $S$ is a *local complete intersection over $k$*
if there exists a covering $\operatorname{Spec}(S) = \bigcup D(g_i)$ such
that each of the rings $S_{g_i}$ is a global complete intersection
over $k$.

We will also use the convention that the zero ring is a global
complete intersection over $k$.

<a id="algebra-definition-lci-local-ring"></a>

#### Definition F.3: lci local ring

*Adapted from the Stacks project, algebra.tex, lines 37446–37458.*

Let $k$ be a field. Let $S$ be a local $k$-algebra essentially of finite type
over $k$. We say $S$ is a *complete intersection (over $k$)*
if there exists a local $k$-algebra $R$ and elements
$f_1, \ldots, f_c \in \mathfrak m_R$ such that

1. $R$ is essentially of finite type over $k$,

1. $R$ is a regular local ring,

1. $f_1, \ldots, f_c$ form a regular sequence in $R$, and

1. $S \cong R/(f_1, \ldots, f_c)$ as $k$-algebras.

<a id="algebra-definition-relative-global-complete-intersection"></a>

#### Definition F.4: relative global complete intersection

*Adapted from the Stacks project, algebra.tex, lines 37943–37951.*

Let $R \to S$ be a ring map. We say that $R \to S$ is
a *relative global complete intersection* if there exists
a presentation $S = R[x_1, \ldots, x_n]/(f_1, \ldots, f_c)$ and
every nonempty fibre of $\operatorname{Spec}(S) \to \operatorname{Spec}(R)$ has dimension $n - c$.
We will say ``let $S = R[x_1, \ldots, x_n]/(f_1, \ldots, f_c)$ be a relative
global complete intersection'' to indicate this situation.

<a id="algebra-definition-separable-field-extension"></a>

#### Definition F.5: separable field extension

*Adapted from the Stacks project, algebra.tex, lines 10135–10146.*

Let $K/k$ be a field extension.

1. We say $K$ is *separably generated over $k$* if there exists
a transcendence basis $\{x_i; i \in I\}$ of $K/k$ such that the extension
$K/k(x_i; i \in I)$ is a separable algebraic extension.

1. We say $K$ is *separable over $k$* if for every subextension
$k \subset K' \subset K$ with $K'$ finitely generated
over $k$, the extension $K'/k$ is separably generated.

<a id="algebra-definition-smooth"></a>

#### Definition F.6: smooth

*Adapted from the Stacks project, algebra.tex, lines 38526–38533.*

A ring map $R \to S$ is *smooth* if it is of finite presentation
and the naive cotangent complex $\NL_{S/R}$ is quasi-isomorphic to a
finite projective $S$-module placed in degree $0$: this means
that $H_1(\NL_{S/R}) = 0$ and that $\Omega_{S/R}$ is a finite projective
$S$-module.

<a id="algebra-definition-smooth-at-prime"></a>

#### Definition F.7: smooth at prime

*Adapted from the Stacks project, algebra.tex, lines 38953–38960.*

Let $R \to S$ be a ring map.
Let $\mathfrak q$ be a prime of $S$.
We say $R \to S$ is *smooth at $\mathfrak q$* if there
exists a $g \in S$, $g \not \in \mathfrak q$ such
that $R \to S_g$ is smooth.

<a id="algebra-definition-unramified"></a>

#### Definition F.8: unramified

*Adapted from the Stacks project, algebra.tex, lines 42897–42912.*

Let $R \to S$ be a ring map.

1. We say $R \to S$ is *unramified* if $R \to S$ is of
finite type and $\Omega_{S/R} = 0$.

1. We say $R \to S$ is *G-unramified* if $R \to S$ is of finite
presentation and $\Omega_{S/R} = 0$.

1. Given a prime $\mathfrak q$ of $S$ we say that $S$ is
*unramified at $\mathfrak q$* if there exists a
$g \in S$, $g \not \in \mathfrak q$ such that $R \to S_g$ is unramified.

1. Given a prime $\mathfrak q$ of $S$ we say that $S$ is
*G-unramified at $\mathfrak q$* if there exists a
$g \in S$, $g \not \in \mathfrak q$ such that $R \to S_g$ is G-unramified.

<a id="algebra-lemma-CM-over-regular-flat"></a>

#### Lemma F.9: CM over regular flat

*Adapted from the Stacks project, algebra.tex, lines 34036–34074.*

Let $R \to S$ be a local homomorphism of Noetherian local
rings. Assume

1. $R$ is regular,

1. $S$ is Cohen-Macaulay,

1. $\dim(S) = \dim(R) + \dim(S/\mathfrak m_R S)$.

Then $R \to S$ is flat.

**Proof.** 
By induction on $\dim(R)$. The case $\dim(R) = 0$ is trivial, because
then $R$ is a field. Assume $\dim(R) > 0$. By (3) this implies that
$\dim(S) > 0$. Let $\mathfrak q_1, \ldots, \mathfrak q_r$ be the minimal
primes of $S$. Note that $\mathfrak q_i \not \supset \mathfrak m_R S$ since

$$
\dim(S/\mathfrak q_i) = \dim(S) > \dim(S/\mathfrak m_R S),
$$

the first equality by Lemma [AG-CA-12, Lemma 5.4 and Theorem 5.5](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/regular-sequences-depth-and-cohen-macaulay-modules.html) and the
inequality by (3). Thus
$\mathfrak p_i = R \cap \mathfrak q_i$ is not equal to $\mathfrak m_R$.
Pick $x \in \mathfrak m_R$, $x \not \in \mathfrak m_R^2$, and
$x \not \in \mathfrak p_i$, see
Lemma [F.80](#algebra-lemma-silly).
Hence we see that $x$ is not contained in any of the minimal
primes of $S$. Hence $x$ is a nonzerodivisor on $S$ by (2), see
Lemma [AG-CA-12, Theorem 4.2 and Corollary 4.3](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/regular-sequences-depth-and-cohen-macaulay-modules.html) and
$S/xS$ is Cohen-Macaulay with $\dim(S/xS) = \dim(S) - 1$.
By (1) and Lemma [AG-CA-12, Theorem 6.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/regular-sequences-depth-and-cohen-macaulay-modules.html) the ring $R/xR$ is regular
with $\dim(R/xR) = \dim(R) - 1$.
By induction we see that $R/xR \to S/xS$ is flat. Hence we
conclude by Lemma [AG-CA-08, Corollary 4.4 and equation (6)](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/faithful-flatness-and-the-local-criterion-for-flatness.html)
and the remark following it.
 ∎

<a id="algebra-lemma-NAK"></a>

#### Lemma F.10: NAK

*Adapted from the Stacks project, algebra.tex, lines 3732–3813.*

Let $R$ be a ring with Jacobson radical $\text{rad}(R)$.
Let $M$ be an $R$-module. Let $I \subset R$
be an ideal.

1. If $IM = M$ and $M$ is finite, then there exists an $f \in 1 + I$ such that
$fM = 0$.

1. If $IM = M$, $M$ is finite, and $I \subset \text{rad}(R)$, then $M = 0$.

1. If $N, N' \subset M$, $M = N + IN'$, and $N'$ is finite,
then there exists an $f \in 1 + I$ such that $fM \subset N$ and $M_f = N_f$.

1. If $N, N' \subset M$, $M = N + IN'$, $N'$ is finite, and
$I \subset \text{rad}(R)$, then $M = N$.

1. If $N \to M$ is a module map, $N/IN \to M/IM$ is
surjective, and $M$ is finite, then there exists an $f \in 1 + I$
such that $N_f \to M_f$ is surjective.

1. If $N \to M$ is a module map, $N/IN \to M/IM$ is
surjective, $M$ is finite, and $I \subset \text{rad}(R)$,
then $N \to M$ is surjective.

1. If $x_1, \ldots, x_n \in M$ generate $M/IM$ and $M$ is finite,
then there exists an $f \in 1 + I$ such that $x_1, \ldots, x_n$
generate $M_f$ over $R_f$.

1. If $x_1, \ldots, x_n \in M$ generate $M/IM$, $M$ is finite, and
$I \subset \text{rad}(R)$, then $M$ is generated by $x_1, \ldots, x_n$.

1. If $IM = M$, $I$ is nilpotent, then $M = 0$.

1. If $N, N' \subset M$, $M = N + IN'$, and $I$ is nilpotent then $M = N$.

1. If $N \to M$ is a module map, $I$ is nilpotent, and $N/IN \to M/IM$
is surjective, then $N \to M$ is surjective.

1. If $\{x_\alpha\}_{\alpha \in A}$ is a set of elements of $M$
which generate $M/IM$ and $I$ is nilpotent, then $M$ is generated
by the $x_\alpha$.

**Proof.** 
Proof of ([F.10 / nakayama](#algebra-lemma-NAK)). Choose generators $y_1, \ldots, y_m$ of $M$
over $R$. For each $i$ we can write $y_i = \sum z_{ij} y_j$ with
$z_{ij} \in I$ (since $M = IM$).
In other words $\sum_j (\delta_{ij} - z_{ij})y_j = 0$.
Let $f$ be the determinant of the $m \times m$ matrix
$A = (\delta_{ij} - z_{ij})$. Note that $f \in 1 + I$
(since the matrix $A$ is entrywise congruent to the
$m \times m$ identity matrix modulo $I$).
By Lemma [F.70](#algebra-lemma-matrix-left-inverse) (1),
there exists an $m \times m$
matrix $B$ such that $BA = f 1_{m \times m}$. Writing out we see that
$\sum_{i} b_{hi} a_{ij} = f \delta_{hj}$ for all
$h$ and $j$; hence, $\sum_{i, j} b_{hi} a_{ij} y_j
= \sum_{j} f \delta_{hj} y_j = f y_h$ for every $h$.
In other words, $0 = f y_h$ for every $h$ (since each
$i$ satisfies $\sum_j a_{ij} y_j = 0$).
This implies that $f$ annihilates $M$.

By Lemma [F.34](#algebra-lemma-contained-in-radical) an element of $1 + \text{rad}(R)$ is an
invertible element of $R$. Hence we see that ([F.10 / nakayama](#algebra-lemma-NAK)) implies
(2). We obtain (3) by applying (1) to $M/N$ which is finite as $N'$ is finite.
We obtain (4) by applying (2) to $M/N$ which is finite as $N'$ is finite.
We obtain (5) by applying (3) to $M$ and the submodules $\operatorname{im}(N \to M)$
and $M$. We obtain (6) by applying (4) to $M$ and the submodules
$\operatorname{im}(N \to M)$ and $M$.
We obtain (7) by applying (5) to the map $R^{\oplus n} \to M$,
$(a_1, \ldots, a_n) \mapsto a_1x_1 + \ldots + a_nx_n$.
We obtain (8) by applying (6) to the map $R^{\oplus n} \to M$,
$(a_1, \ldots, a_n) \mapsto a_1x_1 + \ldots + a_nx_n$.

Part (9) holds because if $M = IM$ then $M = I^nM$ for all $n \geq 0$
and $I$ being nilpotent means $I^n = 0$ for some $n \gg 0$. Parts
(10), (11), and (12) follow from (9) by the arguments used above.
 ∎

<a id="algebra-lemma-NL-homotopy"></a>

#### Lemma F.11: NL homotopy

*Adapted from the Stacks project, algebra.tex, lines 36700–36815.*

Let $R\to R'$ and $S\to S'$ be a commutative square of ring maps with structure maps $R\to S$ and $R'\to S'$.
Let $\alpha : P \to S$ and $\alpha' : P' \to S'$ be presentations.

1. There exists a morphism of presentations from $\alpha$ to $\alpha'$.

1. Any two morphisms of presentations induce homotopic
morphisms of complexes $\operatorname{NL}(\alpha) \to \operatorname{NL}(\alpha')$.

1. The construction is compatible with compositions of morphisms
of presentations (see proof for exact statement).

1. If $R \to R'$ and $S \to S'$ are isomorphisms, then
for any map $\varphi$ of presentations from $\alpha$ to $\alpha'$
the induced map $\operatorname{NL}(\alpha) \to \operatorname{NL}(\alpha')$ is a homotopy equivalence
and a quasi-isomorphism.

In particular, comparing $\alpha$ to the canonical presentation
described in the cotangent-complex context above we conclude there is a
quasi-isomorphism $\operatorname{NL}(\alpha) \to \NL_{S/R}$ well defined
up to homotopy and compatible with all functorialities (up to homotopy).

**Proof.** 
Since $P$ is a polynomial algebra over $R$ we can write
$P = R[x_a, a \in A]$ for some set $A$.
As $\alpha'$ is surjective, we can choose
for every $a \in A$ an element $f_a \in P'$
such that $\alpha'(f_a) = \phi(\alpha(x_a))$. Let
$\varphi : P = R[x_a, a \in A] \to P'$ be the
unique $R$-algebra map such that $\varphi(x_a) = f_a$.
This gives the morphism in (1).

Let $\varphi$ and $\varphi'$ be morphisms of presentations from $\alpha$
to $\alpha'$. Let $I = \ker(\alpha)$ and $I' = \ker(\alpha')$.
We have to construct the diagonal map $h$ in the diagram

$$
\begin{gathered}
I/I^2 {\text{d}} \xrightarrow{-} \Omega_{P/R} \otimes_P S \\
I/I^2 {\text{d}} \xrightarrow{\varphi'_1} I'/(I')^2 {\text{d}} \\
I/I^2 {\text{d}} \xrightarrow{\varphi_1} I'/(I')^2 {\text{d}} \\
\Omega_{P/R} \otimes_P S \xrightarrow{\varphi'_0} \Omega_{P'/R'} \otimes_{P'} S' \\
\Omega_{P/R} \otimes_P S \xrightarrow{\varphi_0} \Omega_{P'/R'} \otimes_{P'} S' \\
\Omega_{P/R} \otimes_P S \xrightarrow{h} I'/(I')^2 {\text{d}} \\
I'/(I')^2 {\text{d}} \xrightarrow{-} \Omega_{P'/R'} \otimes_{P'} S'
\end{gathered}
$$

where the vertical maps are induced by $\varphi$ and $\varphi'$, and $h$ must satisfy

$$
\varphi_1 - \varphi'_1 = h \circ \text{d}
\quad\text{and}\quad
\varphi_0 - \varphi'_0 = \text{d} \circ h
$$

Consider the map $\varphi - \varphi' : P \to P'$. Since both $\varphi$
and $\varphi'$ are compatible with $\alpha$ and $\alpha'$ we obtain
$\varphi - \varphi' : P \to I'$. This implies that
$\varphi, \varphi' : P \to P'$ induce the same $P$-module structure
on $I'/(I')^2$, since
$\varphi(p)i' - \varphi'(p)i' = (\varphi - \varphi')(p)i' \in (I')^2$.
Also $\varphi - \varphi'$ is $R$-linear and

$$
(\varphi - \varphi')(fg) =
\varphi(f)(\varphi - \varphi')(g) + (\varphi - \varphi')(f)\varphi'(g)
$$

Hence the induced map $D : P \to I'/(I')^2$ is an $R$-derivation.
Thus we obtain a canonical map $h : \Omega_{P/R} \otimes_P S \to I'/(I')^2$
such that $D = h \circ \text{d}$. 
For $f\in I$, the definition of the universal derivation gives $h(df)=D(f)=\varphi(f)-\varphi'(f)\bmod (I')^2$, so the degree-one difference is $h\circ d$. On a basis element $dx_a$ of $\Omega_{P/R}\otimes_PS$, one has $d(h(dx_a))=d(\varphi(x_a)-\varphi'(x_a))$, exactly the difference of the degree-zero maps. These two identities verify the homotopy on generators, hence on the whole complexes.

Suppose that we have a commutative diagram

$$
\begin{gathered}
S \xrightarrow{\phi} S' \\
S' \xrightarrow{\phi'} S'' \\
R \xrightarrow{} R' \\
R \xrightarrow{} S \\
R' \xrightarrow{} S' \\
R' \xrightarrow{} R'' \\
R'' \xrightarrow{} S''
\end{gathered}
$$

and that

1. $\alpha : P \to S$,

1. $\alpha' : P' \to S'$, and

1. $\alpha'' : P'' \to S''$

are presentations. Suppose that

1. $\varphi : P \to P'$ is a morphism of presentations from
$\alpha$ to $\alpha'$ and

1. $\varphi' : P' \to P''$
is a morphism of presentations from $\alpha'$ to $\alpha''$.

Then it is immediate that
$\varphi' \circ \varphi : P \to P''$
is a morphism of presentations from $\alpha$ to $\alpha''$ and that
the induced map $\operatorname{NL}(\alpha) \to \operatorname{NL}(\alpha'')$ of naive cotangent complexes
is the composition of the maps $\operatorname{NL}(\alpha) \to \operatorname{NL}(\alpha')$ and
$\operatorname{NL}(\alpha') \to \operatorname{NL}(\alpha'')$ induced by $\varphi$ and $\varphi'$.

In the simple case of complexes with 2 terms a quasi-isomorphism
is just a map that induces an isomorphism on both the cokernel
and the kernel of the maps between the terms. Note that homotopic
maps of 2 term complexes (as explained above) define the same maps on
kernel and cokernel. Hence if $\varphi$ is a map from a presentation
$\alpha$ of $S$ over $R$ to itself, then the induced map
$\operatorname{NL}(\alpha) \to \operatorname{NL}(\alpha)$ is a quasi-isomorphism being homotopic
to the identity by part (2). To prove (4) in full generality, consider
a morphism $\varphi'$ from $\alpha'$ to $\alpha$ which exists by (1).
The compositions $\operatorname{NL}(\alpha) \to \operatorname{NL}(\alpha') \to \operatorname{NL}(\alpha)$ and
$\operatorname{NL}(\alpha') \to \operatorname{NL}(\alpha) \to \operatorname{NL}(\alpha')$ are homotopic to the identity
maps by (2) and (3), hence these maps are homotopy equivalences by definition.
It follows formally that both maps
$\operatorname{NL}(\alpha) \to \operatorname{NL}(\alpha')$ and $\operatorname{NL}(\alpha') \to \operatorname{NL}(\alpha)$ are
quasi-isomorphisms. Explicitly, if $uv$ and $vu$ are homotopic to the respective identities, their maps on kernel and cokernel are identities, since a homotopy contributes $hd$ in degree one and $dh$ in degree zero. The maps induced by $u$ and $v$ on both groups are therefore inverse isomorphisms.
 ∎

<a id="algebra-lemma-Noetherian-field-extension"></a>

#### Lemma F.12: Noetherian field extension

*Adapted from the Stacks project, algebra.tex, lines 6331–6347.*

If $A$ is a Noetherian $k$-algebra and $K/k$ is a finitely generated field extension, then $A\otimes_kK$ is Noetherian.

**Proof.** 
Choose finitely many field generators and let $B\subset K$ be the $k$-algebra they generate. Its fraction field is $K$, so $K=(B\setminus\{0\})^{-1}B$. A finite polynomial presentation of $B$ identifies $A\otimes_kB$ with a quotient of a polynomial algebra in finitely many variables over $A$. Hilbert basis AG-CA-03, Theorem 2.1, makes it Noetherian. Tensor and the fraction universal property identify $A\otimes_kK$ with its localization at the images of the nonzero elements of $B$. The same Noetherian permanence proof in that earlier theorem makes this localization Noetherian. In the special case of a finite field extension, one can alternatively use its finite field basis to see a finite free $A$-module, whose ideals are finite submodules. This proves the full finitely generated form consumed in the regularity tests.
 ∎

<a id="algebra-lemma-another-variant-local-criterion-flatness"></a>

#### Lemma F.13: another variant local criterion flatness

*Adapted from the Stacks project, algebra.tex, lines 24942–24990.*

For a local square of Noetherian rings $R\to S$, $R'\to S'$ with $S'$ a localization of $S\otimes_RR'$, a finite $S$-module $M$, and a proper ideal $I\subset R$, assume $M/IM$ is flat over $R/I$ and the map $\operatorname{Tor}_1^R(M,R/I)\to\operatorname{Tor}_1^{R'}(M\otimes_SS',R'/IR')$ is zero. Then $M\otimes_SS'$ is $R'$-flat.

**Proof.** 
Write a free presentation $0\to K\to F\to M\to0$ over $R$, allowing an infinite free $F$. Put $T=\operatorname{Tor}_1^R(M,R/I)$ and let $\bar K$ be the image of $K/IK$ in $F/IF$. The two sequences $0\to T\to K/IK\to\bar K\to0$ and $0\to\bar K\to F/IF\to M/IM\to0$ are exact. The assumed flatness of the last quotient makes $\bar K$ flat by AG-CA-07, Theorem 6.1. Tensor these sequences with any $R/I$-module $N$; their quotient flatness preserves their left injections and identifies
$$\operatorname{Tor}_1^R(M,N)=T\otimes_{R/I}N.$$
This identity follows from the same free-presentation kernel formula for Tor, so does not assume that $K$ is flat.

After base change to $R'$, let $K'$ be the image of $K\otimes_RR'$ in $F\otimes_RR'$. The map onto $K'$ is surjective. Tensor it with $R'/IR'$; every cycle in $\ker(K'\otimes R'/IR'\to F\otimes R'/IR')$ lifts to an element of $K\otimes_RR'/IR'$, and that lift is automatically a cycle because the two free-module targets are identical. Therefore $\operatorname{Tor}_1^R(M,R'/IR')\to\operatorname{Tor}_1^{R'}(M\otimes_RR',R'/IR')$ is surjective. By the preceding identity its source is $T\otimes_RR'$. Localizing at the stipulated prime in the algebra commutes with this kernel calculation by exact localization. Thus $T\otimes_RR'$ surjects onto the Tor group of $M'=M\otimes_SS'$. The assumed zero map annihilates this surjection, so that Tor group is zero.

Base change of flatness makes $M'/IR'M'$ flat over $R'/IR'$. AG-CA-08, Corollary 4.4, is the proved proper-ideal local criterion under these Noetherian local and finite-over-$S'$ hypotheses; it now makes $M'$ flat over $R'$. This proves the transition criterion rather than invoking an unproved change-of-rings spectral sequence.
 ∎

<a id="algebra-lemma-base-change-relative-global-complete-intersection"></a>

#### Lemma F.14: base change relative global complete intersection

*Adapted from the Stacks project, algebra.tex, lines 38076–38106.*

Relative global complete-intersection presentations are preserved by base change, principal localization, and replacing the base by a localization already inverted in the algebra.

**Proof.** 
First record the required field-dimension argument. For a finite-type algebra over a field and any extension field, dimension is unchanged. Quotient by its finitely many minimal primes; their intersection is nilpotent by AG-CA-03, Proposition 2.2. This remains nilpotent after field extension. For each resulting domain, Noether normalization AG-CA-09, Corollary 3.2, gives an injective finite polynomial subalgebra. Field tensor is exact, so the injection and finiteness persist. Dimension is preserved by an injective integral map, AG-CA-05, Theorem 5.1. Thus each component and their maximum retain dimension. This proof applies to an arbitrary, possibly infinite, field extension.

The fibre after any base change is a field extension of the fibre over the contracted base prime. Consequently its dimension stays $n-c$. For localization, each original fibre is equidimensional of dimension $n-c$: the minimal-prime height calculation in [F.77](#algebra-lemma-relative-global-complete-intersection-conormal), applied just to the polynomial algebra over the fibre field, proves this without any base Noetherianity. A nonempty principal open in an irreducible finite-type field scheme has unchanged dimension, since its coordinate domain has the same fraction field and AG-CA-09, Theorem 4.3, identifies dimension with transcendence degree. Therefore every nonempty localized fibre still has dimension $n-c$. The presentation $S_g=R[X,Z]/(f_1,\ldots,f_c,hZ-1)$ has one additional variable and equation, hence the same expected dimension. Finally if a base element is already inverted in $S$, tensoring with that base localization gives back $S$, proving the third assertion.
 ∎

<a id="algebra-lemma-change-base-NL"></a>

#### Lemma F.15: change base NL

*Adapted from the Stacks project, algebra.tex, lines 36963–36981.*

For a flat base change $R\to R'$, the two-term conormal complex of a polynomial presentation $P\twoheadrightarrow S$ base changes to the corresponding complex for $P\otimes_RR'\twoheadrightarrow S\otimes_RR'$.

**Proof.** 
Let $I$ be the presentation kernel. Flatness identifies the new kernel with $I\otimes_RR'$, since it preserves the exact sequence $0\to I\to P\to S\to0$. Its square is the image of $I^2\otimes_RR'$, by writing products of generators. The cokernel description therefore identifies the conormal module with $(I/I^2)\otimes_RR'$. The differential module of the polynomial ring is free on the same $dX_s$ before and after base change. Both differentials send the class of a polynomial $f$ to $df$, so these are an isomorphism of complexes. Comparison of polynomial presentations and its explicit homotopies, proved above, give the canonical homotopy equivalence.
 ∎

<a id="algebra-lemma-characterize-etale"></a>

#### Lemma F.16: characterize etale

*Adapted from the Stacks project, algebra.tex, lines 40942–40975.*

Let $R \to S$ be a ring map. Let $\mathfrak q$ be a prime of $S$
lying over a prime $\mathfrak p$ of $R$. If

1. $R \to S$ is of finite presentation,

1. $R_{\mathfrak p} \to S_{\mathfrak q}$ is flat

1. $\mathfrak p S_{\mathfrak q}$ is the maximal ideal
of the local ring $S_{\mathfrak q}$, and

1. the field extension $\kappa(\mathfrak q)/\kappa(\mathfrak p)$
is finite separable,

then $R \to S$ is étale at $\mathfrak q$.

**Proof.** 
Apply
Lemma [F.56](#algebra-lemma-isolated-point-fibre)
to find a $g \in S$, $g \not \in \mathfrak q$ such that
$\mathfrak q$ is the only prime of $S_g$ lying over $\mathfrak p$.
We may and do replace $S$ by $S_g$. Then
$S \otimes_R \kappa(\mathfrak p)$ has a unique prime, hence is a
local ring, hence is equal to
$S_{\mathfrak q}/\mathfrak pS_{\mathfrak q}
\cong \kappa(\mathfrak q)$.
By Lemma [F.45](#algebra-lemma-flat-fibre-smooth)
there exists a $g \in S$, $g \not \in \mathfrak q$
such that $R \to S_g$ is smooth. Replacing $S$ by $S_g$ again, we may
assume that $R \to S$ is smooth. By
Lemma [F.83](#algebra-lemma-smooth-syntomic) we may even assume that
$R \to S$ is standard smooth, say $S = R[x_1, \ldots, x_n]/(f_1, \ldots, f_c)$.
Since $S \otimes_R \kappa(\mathfrak p) = \kappa(\mathfrak q)$
has dimension $0$ we conclude that $n = c$, i.e., $R \to S$ is étale.
 ∎

<a id="algebra-lemma-characterize-formally-smooth-field-extension"></a>

#### Lemma F.17: characterize formally smooth field extension

*Adapted from the Stacks project, algebra.tex, lines 45959–45969.*

For a field extension $K/k$, formal smoothness is equivalent to $H_1(\operatorname{NL}_{K/k})=0$.

**Proof.** 
Use any polynomial presentation, including an infinite one. Its first homology is the kernel of the conormal differential by definition. If it vanishes, the conormal sequence is short exact and its quotient $\Omega_{K/k}$ is a vector space, hence free and projective; choosing and lifting a basis splits it. AG-CA-17, Theorem 3.1, with arbitrary variable sets then proves formal smoothness. Conversely that theorem gives split exactness and hence zero kernel. Polynomial comparison already proved identifies this homology with the presentation-independent $H_1(L_{K/k})$ used in the statement.
 ∎

<a id="algebra-lemma-characterize-smooth-kbar"></a>

#### Lemma F.18: characterize smooth kbar

*Adapted from the Stacks project, algebra.tex, lines 39962–40064.*

Let $k$ be an algebraically closed field.
Let $S$ be a finite type $k$-algebra.
Let $\mathfrak m \subset S$ be a maximal ideal.
The following are equivalent:

1. The ring $S_{\mathfrak m}$ is a regular local ring.

1. We have
$\dim_{\kappa(\mathfrak m)} \Omega_{S/k} \otimes_S \kappa(\mathfrak m)
\leq \dim(S_{\mathfrak m})$.

1. We have
$\dim_{\kappa(\mathfrak m)} \Omega_{S/k} \otimes_S \kappa(\mathfrak m)
= \dim(S_{\mathfrak m})$.

1. There exists a $g \in S$, $g \not \in \mathfrak m$
such that $S_g$ is smooth over $k$. In other words $S/k$
is smooth at $\mathfrak m$.

**Proof.** 
Note that (1), (2) and (3) are equivalent by Lemma [AG-CA-18, Proposition 3.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/smooth-algebras-over-a-field-and-the-jacobian-criterion.html)
and Definition [AG-CA-14, Section 1, definition](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/regular-local-rings.html).

Assume that $S$ is smooth at $\mathfrak m$.
By Lemma [F.83](#algebra-lemma-smooth-syntomic) we see that
$S_g$ is standard smooth over $k$
for a suitable $g \in S$, $g \not \in \mathfrak m$.
Hence by Lemma [F.85](#algebra-lemma-standard-smooth)
we see that $\Omega_{S_g/k}$ is free of rank $\dim(S_g)$.
Hence by Lemma [AG-CA-18, Proposition 3.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/smooth-algebras-over-a-field-and-the-jacobian-criterion.html)
we see that $\dim(S_{\mathfrak m}) = \dim (\mathfrak m/\mathfrak m^2)$
in other words $S_\mathfrak m$ is regular.

Conversely, suppose that $S_{\mathfrak m}$ is regular.
Let $d = \dim(S_{\mathfrak m}) = \dim \mathfrak m/\mathfrak m^2$.
Choose a presentation $S = k[x_1, \ldots, x_n]/I$
such that $x_i$ maps to an element of $\mathfrak m$ for
all $i$. In other words, $\mathfrak m'' = (x_1, \ldots, x_n)$
is the corresponding maximal ideal of $k[x_1, \ldots, x_n]$.
Note that we have a short exact sequence

$$
I/\mathfrak m''I \to \mathfrak m''/(\mathfrak m'')^2
\to \mathfrak m/(\mathfrak m)^2 \to 0
$$

Pick $c = n - d$ elements $f_1, \ldots, f_c \in I$ such that
their images in $\mathfrak m''/(\mathfrak m'')^2$ span the
kernel of the map to $\mathfrak m/\mathfrak m^2$. This is clearly
possible. Let $J = (f_1, \ldots, f_c)$. So $J \subset I$.
Let $S' = k[x_1, \ldots, x_n]/J$ so there is a surjection
$S' \to S$. Let $\mathfrak m' = \mathfrak m''S'$ be the corresponding
maximal ideal of $S'$. Hence we have

$$
\begin{gathered}
k[x_1, \ldots, x_n] \xrightarrow{} S' \\
S' \xrightarrow{} S \\
\mathfrak m'' \xrightarrow{} k[x_1, \ldots, x_n] \\
\mathfrak m'' \xrightarrow{} \mathfrak m' \\
\mathfrak m' \xrightarrow{} \mathfrak m \\
\mathfrak m' \xrightarrow{} S' \\
\mathfrak m \xrightarrow{} S
\end{gathered}
$$

By our choice of $J$ the exact sequence

$$
J/\mathfrak m''J \to \mathfrak m''/(\mathfrak m'')^2
\to \mathfrak m'/(\mathfrak m')^2 \to 0
$$

shows that $\dim( \mathfrak m'/(\mathfrak m')^2 ) = d$.
Since $S'_{\mathfrak m'}$ surjects onto $S_{\mathfrak m}$
we see that $\dim(S'_{\mathfrak m'}) \geq d$. Hence by
the discussion preceding Definition [AG-CA-14, Section 1, definition](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/regular-local-rings.html)
we conclude that $S'_{\mathfrak m'}$ is
regular of dimension $d$ as well. Because $S'$ was cut out
by $c = n - d$ equations we
conclude that there exists a $g' \in S'$, $g' \not \in \mathfrak m'$
such that $S'_{g'}$ is a global complete intersection over $k$,
see Lemma [F.57](#algebra-lemma-lci).
Also the map $S'_{\mathfrak m'} \to S_{\mathfrak m}$
is a surjection of Noetherian local domains of the same
dimension and hence an isomorphism. Hence $S' \to S$ is surjective
with finitely generated kernel and becomes an isomorphism
after localizing at $\mathfrak m'$. Thus we can find $g' \in S'$,
$g' \not \in \mathfrak m'$ such that $S'_{g'} \to S_{g'}$
is an isomorphism. All in all we conclude that
after replacing $S$ by a principal localization we may
assume that $S$ is a global complete intersection.

At this point we may write $S = k[x_1, \ldots, x_n]/(f_1, \ldots, f_c)$
with $\dim S = n - c$. Recall that the naive cotangent complex
of this algebra is given by

$$
\bigoplus S \cdot f_j
\to
\bigoplus S \cdot \text{d}x_i
$$

see Lemma [F.77](#algebra-lemma-relative-global-complete-intersection-conormal).
By Lemma [F.78](#algebra-lemma-relative-global-complete-intersection-smooth)
in order to show that $S$ is smooth at
$\mathfrak m$ we have to show that one of the $c \times c$
minors $g_I$ of the matrix ``$A$'' giving the map above
does not vanish at $\mathfrak m$. By Lemma [AG-CA-18, Proposition 3.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/smooth-algebras-over-a-field-and-the-jacobian-criterion.html)
the matrix $A \bmod \mathfrak m$ has rank $c$. Thus we win.
 ∎

<a id="algebra-lemma-charpoly"></a>

#### Lemma F.19: charpoly

*Adapted from the Stacks project, algebra.tex, lines 2856–2879.*

If $M$ is an $n\times n$ matrix over a commutative ring, its characteristic polynomial $P(T)=\det(TI-M)$ satisfies $P(M)=0$.

**Proof.** 
The cofactor expansion proves $(TI-M)\operatorname{adj}(TI-M)=P(T)I$ over the polynomial ring. Write the adjugate as $\sum_{j=0}^{n-1}C_jT^j$ and $P(T)=\sum_{j=0}^n p_jT^j$. Comparing coefficients gives $C_{n-1}=I$, $C_{j-1}-MC_j=p_jI$ for $1\le j<n$, and $-MC_0=p_0I$. Multiplying these equations respectively by $M^j$ and adding telescopes to $\sum_{j=0}^n p_jM^j=0$. The case $n=0$ is the identity on the zero module and causes no exception.
 ∎

<a id="algebra-lemma-codimension"></a>

#### Lemma F.20: codimension

*Adapted from the Stacks project, algebra.tex, lines 29578–29596.*

For a surjection of finite-type $k$-algebras $S'\to S$ and corresponding primes, $\dim_{x'}\operatorname{Spec}S'-\dim_x\operatorname{Spec}S=\operatorname{height}(\mathfrak p')-\operatorname{height}(\mathfrak p)$.

**Proof.** 
AG-CA-09, Theorem 6.1, gives point dimension as local dimension plus the transcendence degree of the residue field. The two residue fields here are equal, since the map is a surjection and the primes correspond. The local dimensions are the heights of those primes, by their chain definition. Subtracting the two identities cancels exactly the equal transcendence degrees, giving the asserted formula.
 ∎

<a id="algebra-lemma-colimit-eventually-flat"></a>

#### Lemma F.21: colimit eventually flat

*Adapted from the Stacks project, algebra.tex, lines 34105–34145.*

In the local finite-presentation models constructed above, if the colimit module $M$ is flat over $R$, then some model $M_\mu$ is flat over $R_\mu$.

**Proof.** 
Fix one stage $\lambda$ and set $T=\operatorname{Tor}_1^{R_\lambda}(M_\lambda,R_\lambda/\mathfrak m_\lambda)$. The free-ideal kernel formula identifies it with $\ker(\mathfrak m_\lambda\otimes_{R_\lambda}M_\lambda\to M_\lambda)$. It is finite over $S_\lambda$: the ideal and module are finite, and kernels of maps of finite modules over that Noetherian algebra are finite. Choose finitely many generators. In the limit their images in $(\mathfrak m_\lambda R)\otimes_RM$ vanish, because multiplication into $M$ is injective by its $R$-flatness. Tensor and filtered colimits commute by their finite-expression universal properties. Consequently each such vanishing holds at a later stage; a common successor $\mu$ kills all generators in $(\mathfrak m_\lambda R_\mu)\otimes_{R_\mu}M_\mu$.

Thus the transition map from $T$ to $\operatorname{Tor}_1^{R_\mu}(M_\mu,R_\mu/\mathfrak m_\lambda R_\mu)$ is zero. The module $M_\lambda/\mathfrak m_\lambda M_\lambda$ is flat over the field $R_\lambda/\mathfrak m_\lambda$. The preceding transition criterion applies to the local square $R_\lambda\to S_\lambda$, $R_\mu\to S_\mu$, whose localized tensor description was proved in the model construction, with ideal $I=\mathfrak m_\lambda$. It makes $M_\mu$ flat over $R_\mu$, as required.
 ∎

<a id="algebra-lemma-colimit-formally-etale"></a>

#### Lemma F.22: colimit formally etale

*Adapted from the Stacks project, algebra.tex, lines 42732–42747.*

A filtered colimit of formally etale $R$-algebras is formally etale over $R$.

**Proof.** 
Given a map from the colimit to $A/J$ with $J^2=0$, restrict to each stage. Formal etaleness gives a unique lift from that stage to $A$. Uniqueness makes these maps compatible with every transition arrow, so their colimit supplies a lift. Two such lifts coincide on every stage and hence on the colimit. No finite-presentation assumption is used.
 ∎

<a id="algebra-lemma-colimit-syntomic"></a>

#### Lemma F.23: colimit syntomic

*Adapted from the Stacks project, algebra.tex, lines 46090–46123.*

Every field extension $K/k$ is a filtered union of global complete-intersection $k$-subalgebras. If it is separable, it is a filtered union of smooth subalgebras.

**Proof.** 
Given a finite subset $E\subset K$, form its finitely generated subfield $L/k$. Choose a transcendence basis $T_1,\ldots,T_d$ and a finite algebraic generator tower $y_1,\ldots,y_r$. At the $i$th step the monic minimal polynomial has coefficients in the preceding field, which is spanned over $k(T)$ by the standard monomials in the preceding generators. Represent those coefficients by polynomials in the preceding $y_j$ with rational-function coefficients in $T$. Clearing a common denominator $h(T)$ puts all of these monic polynomials $P_i$ in $k[T,1/h,Y]$. Their successive quotients are free over the preceding coefficient ring on $1,Y_i,\ldots,Y_i^{\deg P_i-1}$, by monic division. In particular each monic polynomial is a nonzerodivisor in the relevant polynomial ring: its highest nonzero coefficient in a putative product cannot disappear. The list is therefore regular.

The resulting algebra $C$ is finite free over $k[T,1/h]$. After passing to $k(T)$ it is exactly the field $L$, by the minimal-polynomial tower. Since the coefficient ring is a domain and $C$ is free, $C\to C\otimes k(T)=L$ is injective. Each member of $E$ is a linear combination of the finite standard monomial basis with coefficients in $k(T)$; enlarging $h$ clears those finitely many denominators and puts $E$ in $C$. This finite injective extension has dimension $d$ by AG-CA-05, Theorem 5.1, and AG-CA-09, Theorem 4.2. Adjoining the localization variable with $hZ-1$ gives a polynomial presentation with $d+r+1$ variables and $r+1$ equations and dimension $d$, so it is a global complete intersection. The collection of these subalgebras is directed: to dominate two, apply the construction to their finite generator lists. Every field element is included, proving that the union is $K$.

In the separable case every finitely generated subfield remains separable, since the $p$-basis monomial independence criterion restricts to subfields (and characteristic zero is automatic). Use its smooth domain model proved above and clear the finitely many fraction denominators for $E$ by principal localization. This remains smooth and gives a containing subalgebra. The same directedness and union argument applies.
 ∎

<a id="algebra-lemma-colimits-NL"></a>

#### Lemma F.24: colimits NL

*Adapted from the Stacks project, algebra.tex, lines 36983–36999.*

The canonical two-term conormal complex commutes with filtered colimits of ring maps.

**Proof.** 
Use the canonical polynomial presentation with one variable for each element of the target ring. Every polynomial is a finite sum in finitely many variables and coefficients, so it occurs at one stage of the filtered system. Its being in the kernel is a finite equality in the target, hence holds at a later stage. An element in the square of the kernel is a finite sum of products of such kernel elements, and that equality also holds at a common later stage. These facts prove that the polynomial rings, their kernels, their squared kernels, and their conormal quotients have the indicated filtered colimits. Polynomial differentials are the direct sums on the same variables, and their derivatives are finite expressions, so the differentials commute with these identifications. Exactness of filtered colimits, proved in the supporting algebra lesson or directly by common-stage representatives, completes the equality of two-term complexes.
 ∎

<a id="algebra-lemma-complete-local-Noetherian-domain-finite-over-regular"></a>

#### Lemma F.25: complete local Noetherian domain finite over regular

*Adapted from the Stacks project, algebra.tex, lines 46654–46712.*

A complete Noetherian local domain $A$ is finite over a regular complete local subring $A_0$ with the same residue field. One may take $A_0$ to be a power-series ring over a field or a Cohen ring.

**Proof.** 
The coefficient-ring existence proof is AG-CA-19S, Theorem 5.1. Since $A$ is a domain its coefficient image is a field in equal characteristic, and is an embedded Cohen DVR in mixed characteristic. Let $D=\dim A$. In the field case choose $D$ parameters $x_i$, by AG-CA-11, Theorem 2.1, and set $A_0=k[[X_1,\ldots,X_D]]$. In the mixed case $p$ is a nonzerodivisor; AG-CA-11, Theorem 3.2, gives $\dim A/pA=D-1$. Choose parameters $x_1,\ldots,x_{D-1}$ of that quotient and set $A_0=C[[X_1,\ldots,X_{D-1}]]$. Here $C$ is its coefficient Cohen ring. In either case the image $I$ of the maximal ideal of $A_0$ is primary to the maximal ideal of $A$. A power of the latter lies in $I$ by AG-CA-03, Proposition 2.2, making the two filtrations cofinal. Thus $A$ is $I$-adically complete and separated. Evaluation of a power series at the $x_i$ is well defined, by the same convergence and multiplication proof as AG-CA-19S, Theorem 6.1.

Choose lifts $a_1,\ldots,a_s$ of a basis of the finite-dimensional residue quotient $A/I$ over $k$. Every $a\in A$ can be expressed modulo $I$ as a coefficient combination of them. Express the error in $I$ as a sum of its chosen generators times elements of $A$, and repeat the same residue decomposition on those elements. After $n$ steps this constructs coefficients $c_{jn}\in A_0$, compatible modulo its $n$-th maximal-ideal power, such that $a-\sum_jc_{jn}a_j\in I^n$. Completeness of $A_0$ gives limits $c_j$ and separatedness gives $a=\sum_jc_ja_j$. Hence $A$ is finite as an $A_0$-module. The quotient $A/I$ is finite-dimensional because its maximal ideal is nilpotent and its finitely many successive maximal-ideal layers are finite-dimensional, by AG-CA-03, Theorem 4.2.

The power-series ring $A_0$ is the maximal-ideal completion of the regular polynomial local ring over its coefficient field or DVR, as is checked directly on the finite quotients. Regularity of the polynomial local ring is AG-CA-14, Proposition 3.3, with the DVR base regular of dimension one; its dimension is the number of displayed parameters, including $p$ in mixed characteristic, by AG-CA-11, Theorem 5.1. Completion preserves dimension and regularity by AG-CA-19, Theorem 4.1. Thus $A_0$ is a regular local domain of dimension $D$. If the evaluation kernel contained $0\ne f$, the quotient $A_0/(f)$ would have dimension $D-1$ by AG-CA-11, Theorem 3.2. The injective finite integral map $A_0/\ker\to A$ preserves dimension by AG-CA-05, Theorem 5.1, but $\dim(A_0/\ker)\le D-1$ would contradict $\dim A=D$. The evaluation is therefore injective. Its residue map is the coefficient-field identification, completing the proof. For $D=0$ the domain is a field and the assertion takes $A_0=A$.
 ∎

<a id="algebra-lemma-completion-at-quasi-finite-prime"></a>

#### Lemma F.26: completion at quasi finite prime

*Adapted from the Stacks project, algebra.tex, lines 32412–32464.*

Let $R$ be Noetherian, $R\to S$ finite type, and $q$ a quasi-finite prime over $p$. Then $\widehat{R_p}\otimes_RS\cong\widehat{S_q}\times D$, with its first projection the natural completed local map.

**Proof.** 
The earlier full affine conductor theorem [Zariski Main, Theorem C4.3](AG-RG-S04.md) gives an integral subalgebra $C\subset S$ and $g\in C\setminus q$ with $C_g=S_g$. Choose finitely many numerators from $C$ that, together with $g^{-1}$, generate $S_g$ over $R$. Let $S'\subset C$ be generated by them and $g$. Its generators are integral, hence it is a finite $R$-module algebra, and $S'_g=S_g$. Put $q'=q\cap S'$. Localizing this equality again gives $S'_{q'}=S_q$, so their maximal-adic completions agree.

The finite-extension completion argument of [F.27](#algebra-lemma-completion-finite-extension) gives a product
$$\widehat{R_p}\otimes_RS'=A\times D',\qquad A=\widehat{S'_{q'}}=\widehat{S_q}.$$
Let $e$ be the central idempotent of this selected factor. Its image splits $T=\widehat{R_p}\otimes_RS$ as $eT\times(1-e)T$. The element $g$ maps to a unit in $A$, because it is outside $q'$, so it is a unit in $eT$ through the map $A\to eT$. Consequently $eT=(eT)_g$. But localizing the tensor map at $g$ is an isomorphism, since $S'_g=S_g$. Its selected $e$-factor therefore identifies $(eT)_g$ with $A_g=A$. This proves $eT=A$ and the desired product decomposition, including its adic factor.

To check its first projection is the natural map, it agrees on $\widehat{R_p}$ and on $S'$ by the finite-extension completion construction. For any $s\in S$, equality after localizing at $g$ supplies an exponent $a$ with $g^as\in S'$: write its fraction using $S'_g$, then multiply by one further power to kill the localization error in $S$. Since $g$ is a unit in $\widehat{S_q}$, agreement on $g^as$ and on $g$ forces agreement on $s$. Pure tensors generate $T$, so its projection is precisely the natural completed-local map. This is an explicit adic comparison, not an identification of finite scheme completion with ring completion.
 ∎

<a id="algebra-lemma-completion-finite-extension"></a>

#### Lemma F.27: completion finite extension

*Adapted from the Stacks project, algebra.tex, lines 24144–24184.*

For a finite map $R\to S$ of Noetherian rings and a prime $\mathfrak p$ of $R$, with primes $\mathfrak q_i$ above it, one has $\widehat{R_{\mathfrak p}}\otimes_RS=\prod_i\widehat{S_{\mathfrak q_i}}$.

**Proof.** 
Localize the base at $\mathfrak p$. All maximal ideals of the finite algebra lie above this maximal ideal, by AG-CA-05, Theorem 3.3, and there are finitely many by Theorem 3.4. For each $n$, the finite algebra $S/\mathfrak p^nS$ is a finite module over the Artinian ring $R/\mathfrak p^n$, hence Artinian by AG-CA-03, Theorem 3.3 and its finite maximal-ideal-layer proof. The product theorem 4.2 of that lesson gives $S/\mathfrak p^nS=\prod_iS_{\mathfrak q_i}/\mathfrak p^nS_{\mathfrak q_i}$. On each factor $\mathfrak pS_{\mathfrak q_i}$ has radical $\mathfrak q_iS_{\mathfrak q_i}$. A power of the latter ideal lies in the former, by AG-CA-03, Proposition 2.2; their adic filtrations are cofinal, so their inverse limits are the same. Taking the finite product of the inverse limits now gives the asserted product of local completions. Finally the completion-tensor equality for the finite $R_{\mathfrak p}$-module $S_{\mathfrak p}$ is AG-CA-19, Theorem 3.1.
 ∎

<a id="algebra-lemma-compose-finite-type"></a>

#### Lemma F.28: compose finite type

*Adapted from the Stacks project, algebra.tex, lines 547–571.*

Finite-type and finitely presented ring maps compose. If $R\to S'\to S$ and $S$ is finite type over $R$, it is finite type over $S'$. If additionally $S/R$ is finitely presented and $S'/R$ finite type, then $S/S'$ is finitely presented.

**Proof.** 
Generators of $S'/R$, followed by generators of $S/S'$, generate the composite. For presentations $S'=R[Y]/(a)$ and $S=S'[X]/(b)$, lift the finitely many coefficients of $b$ to $R[Y]$ to obtain the finite composite presentation $R[Y,X]/(a,\widetilde b)$. The same generators of $S/R$ generate it over $S'$. Finally write $S=R[X]/(f_1,\ldots,f_m)$ and $S'=R[Y]/I$, with finitely many $Y_i$ mapping to polynomials $h_i(X)$ in $S$. Then $S=S'[X]/(f_j,Y_i-h_i(X))$. To check this equality, substitute $Y_i=h_i(X)$; every relation in $I$ vanishes in $S$ and so belongs to the ideal of the $f_j$. This proves both inverse maps directly without assuming $I$ finitely generated.
 ∎

<a id="algebra-lemma-compose-smooth"></a>

#### Lemma F.29: compose smooth

*Adapted from the Stacks project, algebra.tex, lines 39039–39053.*

A composition of smooth ring maps is smooth.

**Proof.** 
Let $R\to S\to T$ be smooth maps. Lemma [F.28](#algebra-lemma-compose-finite-type) gives finite presentation of $T/R$. The Jacobi–Zariski sequence [F.42](#algebra-lemma-exact-sequence-NL) places $H_1(\operatorname{NL}_{T/R})$ between $H_1(\operatorname{NL}_{S/R}\otimes_ST)$ and $H_1(\operatorname{NL}_{T/S})$. The latter is zero by smoothness. For the former, the last assertion of F.42 identifies it with $H_1(\operatorname{NL}_{S/R})\otimes_ST=0$: its two Tor hypotheses hold because $\Omega_{S/R}$ is projective. Hence $H_1(\operatorname{NL}_{T/R})=0$. The same sequence gives

$$0\longrightarrow\Omega_{S/R}\otimes_ST\longrightarrow\Omega_{T/R}\longrightarrow\Omega_{T/S}\longrightarrow0.$$

The last module is projective, so this sequence splits. The first is finite projective because a finite direct-summand presentation for $\Omega_{S/R}$ remains such a presentation after tensoring with $T$; the last is finite projective by smoothness of $T/S$. Their direct sum is therefore finite projective. Definition [F.6](#algebra-definition-smooth) proves smoothness of $T/R$. ∎

<a id="algebra-lemma-compose-standard-smooth"></a>

#### Lemma F.30: compose standard smooth

*Adapted from the Stacks project, algebra.tex, lines 38815–38878.*

A composite of standard smooth ring maps is standard smooth.

**Proof.** 
Write $S=R[X_1,\ldots,X_n]/(f_1,\ldots,f_c)$ and $T=S[Y_1,\ldots,Y_m]/(g_1,\ldots,g_d)$, with their selected Jacobian minors invertible. Lift the coefficients of the $g_i$ to $R[X]$. The resulting $R$-presentation of $T$ has equations $f_i,g_j$ and pivot variables the $c$ selected $X$ variables followed by the $d$ selected $Y$ variables. Its Jacobian matrix is block lower triangular, since $\partial f_i/\partial Y_j=0$. Its determinant is the product of the two given unit determinants. This is the required standard smooth presentation. Any principal localization is encoded by one more variable $z$ and equation $hz-1$, whose additional diagonal Jacobian entry $h$ is a unit. Thus the assertion covers the localized presentations as well.
 ∎

<a id="algebra-lemma-composition-essentially-of-finite-type"></a>

#### Lemma F.31: composition essentially of finite type

*Adapted from the Stacks project, algebra.tex, lines 13129–13138.*

Essentially finite type, and essentially finite presentation, are preserved by composition.

**Proof.** 
Write the first algebra as $U^{-1}R[Y]/(a)$, and the second before its final localization as a polynomial algebra over it modulo finitely many chosen relations in the finite-presentation case. Only finitely many denominators from $U$ occur in those relations; absorb them in one element $u\in U$. This finite algebra then descends to $(R[Y]/(a))_u$, and its further localization gives the original composite. The composite is therefore a localization of a finite-type $R$-algebra, or of a finitely presented one in the second case. The remaining elements of $U$ and the second localization set are simply included in the final localization set. The finite-type argument only needs the finite generator list and uses the same construction with the possibly infinite relation ideal.
 ∎

<a id="algebra-lemma-composition-syntomic"></a>

#### Lemma F.32: composition syntomic

*Adapted from the Stacks project, algebra.tex, lines 38404–38453.*

Let $R \to S$, $S \to S'$ be ring maps.

1. If $R$ is Noetherian and $R \to S$ and $S \to S'$ are syntomic, then $R \to S'$
is syntomic.

1. If $R \to S$ and $S \to S'$ are relative global complete intersections,
then $R \to S'$ is a relative global complete intersection.

**Proof.** 
Proof of (2). Say $R \to S$ and $S \to S'$ are relative global complete
intersections and we have presentations
$S =  R[x_1, \ldots, x_n]/(f_1, \ldots, f_c)$ and
$S' = S[y_1, \ldots, y_m]/(h_1, \ldots, h_d)$ as in
Definition [F.4](#algebra-definition-relative-global-complete-intersection).
Then

$$
S' \cong
R[x_1, \ldots, x_n, y_1, \ldots, y_m]/(f_1, \ldots, f_c, h'_1, \ldots, h'_d)
$$

for some lifts $h_j' \in R[x_1, \ldots, x_n, y_1, \ldots, y_m]$ of the $h_j$.
Hence it suffices to bound the dimensions of the fibre rings.
Thus we may assume $R = k$ is a field.
In this case we see that we have a ring, namely $S$, which is of finite
type over $k$ and equidimensional of dimension $n - c$, and a
finite type ring map $S \to S'$ all of whose nonempty fibre
rings are equidimensional of dimension $m - d$. Then, by
Lemma [AG-CA-11, Theorem 5.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/dimension-theory-of-noetherian-local-rings.html) for example applied
to localizations at maximal ideals of $S'$, we see that
$\dim(S') \leq n - c + m - d$ as desired.

We will reduce part (1) to part (2). Assume $R$ Noetherian and $R \to S$ and $S \to S'$
are syntomic. Their finite presentation makes $S$ and $S'$ Noetherian by the earlier Hilbert basis theorem, so both applications of [F.87](#algebra-lemma-syntomic) have their stated base hypothesis. Let $\mathfrak q' \subset S'$ be a prime ideal lying
over $\mathfrak q \subset S$. By Lemma [F.87](#algebra-lemma-syntomic)
there exists a $g' \in S'$, $g' \not \in \mathfrak q'$ such that
$S \to S'_{g'}$ is a relative global complete intersection.
Similarly, we find $g \in S$, $g \not \in \mathfrak q$ such that
$R \to S_g$ is a relative global complete intersection.
By Lemma [F.14](#algebra-lemma-base-change-relative-global-complete-intersection)
the ring map $S_g \to S'_{gg'}$ is a relative global complete intersection.
By part (2) we see that $R \to S'_{gg'}$ is a relative global
complete intersection and $gg' \not \in \mathfrak q'$.
Since $\mathfrak q'$ was arbitrary
combining Lemmas [F.87](#algebra-lemma-syntomic) and [F.62](#algebra-lemma-local-syntomic)
we see that $R \to S'$ is syntomic (this also uses that the spectrum
of $S'$ is quasi-compact, see Lemma [AG-CA-01, Proposition 2.3](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/spectra-of-rings.html)).
 ∎

<a id="algebra-lemma-conormal-module-localize"></a>

#### Lemma F.33: conormal module localize

*Adapted from the Stacks project, algebra.tex, lines 37203–37225.*

For finite polynomial presentations $R[X_1,\ldots,X_n]\twoheadrightarrow S$ and $R[Y_1,\ldots,Y_m]\twoheadrightarrow S_g$ with kernels $I,J$, there is an isomorphism $(I/I^2)_g\oplus S_g^m\cong J/J^2\oplus S_g^n$.

**Proof.** 
Principal localization of the first presentation adds the one explicitly contractible two-term summand, by [F.72](#algebra-lemma-principal-localization-NL). Comparison of polynomial presentations gives homotopy-equivalent complexes by the proved homotopy calculation [F.11](#algebra-lemma-NL-homotopy). Therefore the original localized complex and the second presentation complex are homotopy equivalent. Their degree-zero modules are respectively $S_g^n$ and $S_g^m$. The full block-matrix calculation [F.86](#algebra-lemma-sum-two-terms) yields exactly the stated conormal stable isomorphism.
 ∎

<a id="algebra-lemma-contained-in-radical"></a>

#### Lemma F.34: contained in radical

*Adapted from the Stacks project, algebra.tex, lines 3648–3678.*

An ideal $I$ is contained in the Jacobson radical exactly when every element of $1+I$ is a unit. In that case units modulo $I$ lift to units.

**Proof.** 
If $I$ lies in every maximal ideal, $1+i$ lies in none and therefore is a unit: a nonunit generates a proper ideal, which lies in a maximal ideal by Zorn's lemma. Conversely, if $I\not\subset\mathfrak m$, write $1=i+x$ with $i\in I$, $x\in\mathfrak m$; then $x=1-i$ is a nonunit, contradiction. If $ab=1+i$ after lifting a modular inverse, its unit status gives an inverse $b(ab)^{-1}$ for $a$.
 ∎

<a id="algebra-lemma-cover-upstairs"></a>

#### Lemma F.35: cover upstairs

*Adapted from the Stacks project, algebra.tex, lines 4346–4405.*

Let $g_1,\ldots,g_r\in S$ generate the unit ideal. Finite type and finite presentation of $S/R$ can be checked on the finitely many $S_{g_i}$.

**Proof.** 
Choose $h_i\in S$ with $\sum h_ig_i=1$. For finite type, include in an $R$-subalgebra $S_0\subset S$ all $h_i,g_i$ and the numerators of finite generator lists for the $S_{g_i}$. Then $(S_0)_{g_i}\to S_{g_i}$ is an isomorphism. Its kernel and cokernel as an $S_0$-module map vanish on this principal cover; the powers of the $g_i$ killing a given element generate one, so the map $S_0\to S$ is an isomorphism.

For finite presentation first use finite type to write $S=P/J$, $P=R[X_1,\ldots,X_n]$. Lift $g_i,h_i$ to $u_i,v_i\in P$. The finite algebra presentation $P[Z]\to S_{g_i}$ has kernel $JP[Z]+(u_iZ-1)$: quotienting first by $J$ and then by $u_iZ-1$ gives precisely $S_{g_i}$ by the fraction universal property. Since $S_{g_i}$ is finitely presented, this kernel is finite. Here is the presentation-independence argument needed for that last assertion: if $C=R[Y]/(a_1,\ldots,a_m)$ and a finite polynomial algebra $R[W]$ maps onto $C$, express the $Y$-images as polynomials in $W$ and the $W$-images as polynomials in $Y$; the finitely many defining $a_j$ and the two finite lists of substitution identities give a finite presentation in the $W$ variables. This follows by substituting the chosen polynomials in both directions, giving inverse quotient maps.

Expand each of the finitely many kernel generators as a finite combination of elements of $J$ and $u_iZ-1$. Collect the finitely many elements $a_{ij}\in J$ occurring for each $i$. They and $u_iZ-1$ generate that kernel. Set $J_0=(\sum v_iu_i-1,a_{ij})\subset J$. The classes of the $u_i$ generate one in $P/J_0$, and each localization $(P/J_0)_{u_i}\to(P/J)_{u_i}$ is an isomorphism. Local detection as above makes $P/J_0\to S$ an isomorphism, so $J=J_0$ is finite.
 ∎

<a id="algebra-lemma-criterion-flatness-fibre"></a>

#### Lemma F.36: criterion flatness fibre

*Adapted from the Stacks project, algebra.tex, lines 34374–34496.*

Let $R$, $S$, $S'$ be local rings and let $R \to S \to S'$ be local ring
homomorphisms. Let $M$ be an $S'$-module. Let $\mathfrak m \subset R$
be the maximal ideal. Assume

1. The ring maps $R \to S$ and $R \to S'$ are essentially
of finite presentation.

1. The module $M$ is of finite presentation over $S'$.

1. The module $M$ is not zero.

1. The module $M/\mathfrak mM$ is a flat $S/\mathfrak mS$-module.

1. The module $M$ is a flat $R$-module.

Then $S$ is flat over $R$ and $M$ is a flat $S$-module.

**Proof.** 
As in the proof of Lemma [F.59](#algebra-lemma-limit-essentially-finite-presentation)
we may first write $R = \operatorname*{colim} R_\lambda$ as a directed colimit
of local $\mathbf{Z}$-algebras which are essentially of finite type.
Denote by $\mathfrak p_\lambda$ the maximal ideal of $R_\lambda$.
Next, we may assume that for some $\lambda_1 \in \Lambda$ there
exist $f_{j, \lambda_1} \in R_{\lambda_1}[x_1, \ldots, x_n]$
such that

$$
S =
\colim_{\lambda \geq \lambda_1} S_\lambda, \text{ with }
S_\lambda =
(R_\lambda[x_1, \ldots, x_n]/
(f_{1, \lambda}, \ldots, f_{u, \lambda}))_{\mathfrak q_\lambda}
$$

For some $\lambda_2 \in \Lambda$,
$\lambda_2 \geq \lambda_1$ there exist
$g_{j, \lambda_2} \in R_{\lambda_2}[x_1, \ldots, x_n, y_1, \ldots, y_m]$
with images
$\overline{g}_{j, \lambda_2} \in S_{\lambda_2}[y_1, \ldots, y_m]$
such that

$$
S' =
\colim_{\lambda \geq \lambda_2} S'_\lambda, \text{ with }
S'_\lambda =
(S_\lambda[y_1, \ldots, y_m]/
(\overline{g}_{1, \lambda}, \ldots,
\overline{g}_{v, \lambda}))_{\overline{\mathfrak q}'_\lambda}
$$

Note that this also implies that

$$
S'_\lambda =
(R_\lambda[x_1, \ldots, x_n, y_1, \ldots, y_m]/
(f_{1, \lambda}, \ldots, f_{u, \lambda},
g_{1, \lambda}, \ldots, g_{v, \lambda}))_{\mathfrak q'_\lambda}
$$

Choose a presentation

$$
(S')^{\oplus s} \to (S')^{\oplus t} \to M \to 0
$$

of $M$ over $S'$. Let $A \in \text{Mat}(t \times s, S')$ be
the matrix of the presentation. For some $\lambda_3 \in \Lambda$,
$\lambda_3 \geq \lambda_2$
we can find a matrix $A_{\lambda_3} \in \text{Mat}(t \times s, S'_{\lambda_3})$
which maps to $A$. For all $\lambda \geq \lambda_3$ we let
$M_\lambda = \operatorname{coker}((S'_\lambda)^{\oplus s} \xrightarrow{A_\lambda}
(S'_\lambda)^{\oplus t})$.

With these choices, we have for each $\lambda_3 \leq \lambda \leq \mu$
that $S_\lambda \otimes_{R_{\lambda}} R_\mu \to S_\mu$ is a localization,
$S'_\lambda \otimes_{S_{\lambda}} S_\mu \to S'_\mu$ is a localization, and
the map $M_\lambda \otimes_{S'_\lambda} S'_\mu \to M_\mu$ is an
isomorphism. This also implies that
$S'_\lambda \otimes_{R_{\lambda}} R_\mu \to S'_\mu$ is a localization.
Thus, since $M$ is flat over $R$ we see by
Lemma [F.21](#algebra-lemma-colimit-eventually-flat) that
for all $\lambda$ big enough the module $M_\lambda$ is
flat over $R_\lambda$.
Moreover, note that
$\mathfrak m = \operatorname*{colim} \mathfrak p_\lambda$,
$S/\mathfrak mS = \operatorname*{colim} S_\lambda/\mathfrak p_\lambda S_\lambda$,
$S'/\mathfrak mS' = \operatorname*{colim} S'_\lambda/\mathfrak p_\lambda S'_\lambda$,
and
$M/\mathfrak mM = \operatorname*{colim} M_\lambda/\mathfrak p_\lambda M_\lambda$. Also, for each $\lambda_3 \leq \lambda \leq \mu$ we see (from the
properties listed above) that

$$
S'_\lambda/\mathfrak p_\lambda S'_\lambda
\otimes_{S_{\lambda}/\mathfrak p_\lambda S_\lambda}
S_\mu/\mathfrak p_\mu S_\mu
\longrightarrow
S'_\mu/\mathfrak p_\mu S'_\mu
$$

is a localization, and the map

$$
M_\lambda / \mathfrak p_\lambda M_\lambda
\otimes_{S'_\lambda/\mathfrak p_\lambda S'_\lambda}
S'_\mu /\mathfrak p_\mu S'_\mu
\longrightarrow
M_\mu/\mathfrak p_\mu M_\mu
$$

is an isomorphism. Hence the system
$(S_\lambda/\mathfrak p_\lambda S_\lambda \to
S'_\lambda/\mathfrak p_\lambda S'_\lambda,
M_\lambda/\mathfrak p_\lambda M_\lambda)$
is a system as in
Lemma [F.60](#algebra-lemma-limit-module-essentially-finite-presentation) as well.
We may apply Lemma [F.21](#algebra-lemma-colimit-eventually-flat) again because
$M/\mathfrak m M$ is assumed flat over $S/\mathfrak mS$ and we see that
$M_\lambda/\mathfrak p_\lambda M_\lambda$ is flat over
$S_\lambda/\mathfrak p_\lambda S_\lambda$ for all $\lambda$ big enough.
Thus for $\lambda$ big enough the data
$R_\lambda \to S_\lambda \to S'_\lambda, M_\lambda$ satisfies
the hypotheses of Lemma [F.37](#algebra-lemma-criterion-flatness-fibre-Noetherian).
Pick such a $\lambda$. Then $S$ is a localization of
$S_\lambda \otimes_{R_\lambda} R$, hence is flat over $R$.
Also $M$ is a localization of $M_\lambda \otimes_{S_\lambda} S$,
hence is flat over $S$ (base change and localization preserve flatness).
 ∎

<a id="algebra-lemma-criterion-flatness-fibre-Noetherian"></a>

#### Lemma F.37: criterion flatness fibre Noetherian

*Adapted from the Stacks project, algebra.tex, lines 24999–25045.*

Let $R\to S\to T$ be local maps of Noetherian local rings, and $M\ne0$ finite over $T$. If $M$ is $R$-flat and $M/\mathfrak m_RM$ is flat over $S/\mathfrak m_RS$, then $M$ is faithfully flat over $S$ and $S$ is flat over $R$.

**Proof.** 
Put $I=\mathfrak m_RS$. The map $\mathfrak m_R\otimes_RM\to I\otimes_SM$ is surjective, because the images of $\mathfrak m_R$ generate $I$. Its composite to $M$ is injective by $R$-flatness, so both maps are injective. Thus $\operatorname{Tor}_1^S(S/I,M)=0$. The ideal form of the local flatness criterion, AG-CA-08, Corollary 4.4, applied to the proper ideal $I$ gives $S$-flatness. Nakayama gives $M/\mathfrak m_TM\ne0$, hence $M/\mathfrak m_SM\ne0$; the faithful-flatness criterion for modules, AG-CA-08, Theorem 1.1, gives faithfulness over $S$.

Tensor the exact sequence $0\to\operatorname{Tor}_1^R(R/\mathfrak m_R,S)\to\mathfrak m_R\otimes_RS\to I\to0$ with this flat $S$-module. Its first term maps to the kernel of the already injective map $\mathfrak m_R\otimes_RM\to I\otimes_SM$, hence is zero. Faithfulness kills the original Tor module. AG-CA-08, Theorem 4.2, then gives $R$-flatness of $S$. All modules to which the local criterion is applied are finite over the stipulated Noetherian local overring.
 ∎

<a id="algebra-lemma-descent-regular"></a>

#### Lemma F.38: descent regular

*Adapted from the Stacks project, algebra.tex, lines 48353–48371.*

Regularity descends along faithfully flat maps of Noetherian rings.

**Proof.** 
Fix a source prime and choose a target prime above it, which exists by faithful flatness. The localized map $A\to B$ is flat local, hence faithfully flat by AG-CA-08, Theorem 2.1. The target is regular local. Take a free resolution of the source residue field $k$ over $A$. After tensoring with $B$ it remains a free resolution of $k\otimes_AB$, by flatness. Consequently
$$\operatorname{Tor}_i^A(k,k)\otimes_AB=\operatorname{Tor}_i^B(k\otimes_AB,k\otimes_AB).$$
AG-CA-14, Theorem 2.2, gives finite global dimension of $B$, so these groups vanish for all sufficiently large $i$. Faithfulness gives vanishing of the original source Tor groups. The minimal-free-resolution calculation AG-CA-13, Theorem 2.2, makes the source residue field have finite projective dimension; AG-CA-14, Theorem 2.2, then makes $A$ regular. Doing this at every prime proves the assertion.
 ∎

<a id="algebra-lemma-dimension-fibres-bounded-open-upstairs"></a>

#### Lemma F.39: dimension fibres bounded open upstairs

*Adapted from the Stacks project, algebra.tex, lines 32674–32690.*

For a finite-type map of Noetherian rings $R\to S$, if the fibre dimension at a point $q$ is $n$, some principal neighbourhood of $q$ has fibre point-dimension at most $n$ everywhere. This is the exact form used here.

**Proof.** 
Let $p=q\cap R$. Choose a principal neighbourhood whose $\kappa(p)$-fibre has dimension exactly $n$, using the point-dimension definition and the finite-type field component formula. Apply Noether normalization to that fibre. The coordinate changes in AG-CA-09, Lemma 2.1 and Corollary 3.2, use polynomials with integer coefficients in the algebra generators: at each step replace a generator by it minus a sufficiently high power of the last generator, so one selected relation has a constant nonzero leading coefficient; dividing that coefficient makes the last generator integral. Inducting yields $n$ such parameters and finiteness over their polynomial algebra. Thus these parameters lift to elements $t_i\in S$, and $R[T_1,\ldots,T_n]\to S$, $T_i\mapsto t_i$, has a finite fibre over $p$. At the chosen point it is quasi-finite: its further fibre over the contracted polynomial prime is a finite algebra over that prime's residue field.

The earlier affine conductor proof [Zariski Main, Theorem C5.1](AG-RG-S04.md) proves the open quasi-finite locus from its full Theorem C4.3. Shrink once more around $q$ so this polynomial map is quasi-finite everywhere. In a fibre over any base prime $p'$, its algebra $U$ is quasi-finite over $\kappa(p')[T_1,\ldots,T_n]$. At a minimal prime $\eta$ of $U$, the residue field is finite over that of its contracted polynomial prime, by the isolated-fibre criterion proved above. Its transcendence degree over $\kappa(p')$ is therefore at most $n$. AG-CA-09, Theorem 4.2, gives $\dim(U/\eta)$ equal to that transcendence degree. Taking the maximum over the finitely many minimal primes gives $\dim U\le n$. Every fibre point-dimension is at most that fibre dimension. This proves the claimed neighbourhood bound. Its earlier conductor input includes the polynomial-normality proof in [Zariski Main over an arbitrary base, Corollary B1.2](AG-RG-S04.md), so no old external proof tag is being substituted.
 ∎

<a id="algebra-lemma-essentially-of-finite-type-into-artinian-local"></a>

#### Lemma F.40: essentially of finite type into artinian local

*Adapted from the Stacks project, algebra.tex, lines 13151–13207.*

Let $R \to S$ be a ring map. Assume $S$ is an Artinian local ring with
maximal ideal $\mathfrak m$. Then

1. $R \to S$ is finite if and only if $R \to S/\mathfrak m$ is finite,

1. $R \to S$ is of finite type if and only if $R \to S/\mathfrak m$
is of finite type.

1. $R \to S$ is essentially of finite type if and
only if the composition $R \to S/\mathfrak m$ is essentially
of finite type.

**Proof.** 
If $R \to S$ is finite, then $R \to S/\mathfrak m$
is finite by Lemma [AG-CA-05, Theorem 1.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/integral-extensions-lying-over-going-up-and-going-down.html).
Conversely, assume $R \to S/\mathfrak m$ is finite.
As $S$ has finite length over itself
(Lemma [AG-CA-03, Theorem 4.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/noetherian-and-artinian-rings.html))
we can choose a filtration

$$
0 \subset I_1 \subset \ldots \subset I_n = S
$$

by ideals such that $I_i/I_{i - 1} \cong S/\mathfrak m$ as $S$-modules.
Thus $S$ has a filtration by $R$-submodules $I_i$ such that each
successive quotient is a finite $R$-module. Thus $S$ is a finite
$R$-module by Lemma [F.43](#algebra-lemma-extension).

If $R \to S$ is of finite type, then $R \to S/\mathfrak m$
is of finite type by Lemma [F.28](#algebra-lemma-compose-finite-type).
Conversely, assume that $R \to S/\mathfrak m$ is of finite type.
Choose $f_1, \ldots, f_n \in S$ which map to generators of $S/\mathfrak m$.
Then $A = R[x_1, \ldots, x_n] \to S$, $x_i \mapsto f_i$ is a ring map such
that $A \to S/\mathfrak m$ is surjective (in particular finite).
Hence $A \to S$ is finite by part (1) and we see that $R \to S$
is of finite type by Lemma [F.28](#algebra-lemma-compose-finite-type).

If $R \to S$ is essentially of finite type, then $R \to S/\mathfrak m$
is essentially of finite type by
Lemma [F.31](#algebra-lemma-composition-essentially-of-finite-type).
Conversely, assume that $R \to S/\mathfrak m$ is essentially
of finite type. Suppose $S/\mathfrak m$ is the localization
of $R[x_1, \ldots, x_n]/I$. Choose $f_1, \ldots, f_n \in S$
whose congruence classes modulo $\mathfrak m$ correspond to
the congruence classes of $x_1, \ldots, x_n$ modulo $I$.
Consider the map $R[x_1, \ldots, x_n] \to S$, $x_i \mapsto f_i$
with kernel $J$. Set $A = R[x_1, \ldots, x_n]/J \subset S$
and $\mathfrak p = A \cap \mathfrak m$. Note that
$A/\mathfrak p \subset S/\mathfrak m$ is equal to the image
of $R[x_1, \ldots, x_n]/I$ in $S/\mathfrak m$. Hence
$\kappa(\mathfrak p) = S/\mathfrak m$. Thus $A_\mathfrak p \to S$
is finite by part (1). We conclude that $S$ is essentially of finite
type by Lemma [F.31](#algebra-lemma-composition-essentially-of-finite-type).
 ∎

<a id="algebra-lemma-etale-standard-smooth"></a>

#### Lemma F.41: etale standard smooth

*Adapted from the Stacks project, algebra.tex, lines 40737–40760.*

Any étale ring map is standard smooth. More precisely, if
$R \to S$ is étale, then there exists a presentation
$S = R[x_1, \ldots, x_n]/(f_1, \ldots, f_n)$ such that
the image of $\det(\partial f_j/\partial x_i)$ is invertible in $S$.

**Proof.** 
Let $R \to S$ be étale. Choose a presentation $S = R[x_1, \ldots, x_n]/I$.
As $R \to S$ is étale we know that

$$
\text{d} :
I/I^2
\longrightarrow
\bigoplus\nolimits_{i = 1, \ldots, n} S\text{d}x_i
$$

is an isomorphism, in particular $I/I^2$ is a free $S$-module.
Thus by Lemma [F.55](#algebra-lemma-huber) we may assume (after possibly changing
the presentation), that $I = (f_1, \ldots, f_c)$ such that the classes
$f_i \bmod I^2$ form a basis of $I/I^2$. It follows immediately from
the fact that the displayed map above is an isomorphism that $c = n$ and
that $\det(\partial f_j/\partial x_i)$ is invertible in $S$.
 ∎

<a id="algebra-lemma-exact-sequence-NL"></a>

#### Lemma F.42: exact sequence NL

*Adapted from the Stacks project, algebra.tex, lines 36838–36913.*

Let $A \to B \to C$ be ring maps. Choose a presentation
$\alpha : A[x_s, s \in S] \to B$ with kernel $I$. Choose a presentation
$\beta : B[y_t, t \in T] \to C$ with kernel $J$. Let
$\gamma : A[x_s, y_t] \to C$ be the induced presentation of $C$ with kernel
$K$. Then we get a canonical commutative diagram

$$
\begin{gathered}
0 \xrightarrow{} \Omega_{A[x_s]/A} \otimes C \\
\Omega_{A[x_s]/A} \otimes C \xrightarrow{} \Omega_{A[x_s, y_t]/A} \otimes C \\
\Omega_{A[x_s, y_t]/A} \otimes C \xrightarrow{} \Omega_{B[y_t]/B} \otimes C \\
\Omega_{B[y_t]/B} \otimes C \xrightarrow{} 0 \\
I/I^2 \otimes C \xrightarrow{} K/K^2 \\
I/I^2 \otimes C \xrightarrow{} \Omega_{A[x_s]/A} \otimes C \\
K/K^2 \xrightarrow{} J/J^2 \\
K/K^2 \xrightarrow{} \Omega_{A[x_s, y_t]/A} \otimes C \\
J/J^2 \xrightarrow{} 0 \\
J/J^2 \xrightarrow{} \Omega_{B[y_t]/B} \otimes C
\end{gathered},
$$

with exact rows. We get the following exact sequence
of homology groups

$$
H_1(\NL_{B/A} \otimes_B C) \to
H_1(L_{C/A}) \to
H_1(L_{C/B}) \to
C \otimes_B \Omega_{B/A} \to
\Omega_{C/A} \to
\Omega_{C/B} \to 0
$$

of $C$-modules extending the sequence of
Lemma [AG-CA-16, Theorem 3.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/kahler-differentials.html).
If $\text{Tor}_1^B(\Omega_{B/A}, C) = 0$ and
$\text{Tor}_2^B(\Omega_{B/A}, C) = 0$, then
$H_1(\NL_{B/A} \otimes_B C) = H_1(L_{B/A}) \otimes_B C$.

**Proof.** 
On differentials, the first map sends $dx_s$ to $dx_s$, the second sends every $dx_s$ to zero and $dy_t$ to $dy_t$. On conormal modules the first map sends $(f\bmod I^2)\otimes c$ to $cf\bmod K^2$, using any lift of $c$ to $A[x_s,y_t]$; the ambiguity changes the answer by $K^2$. The second sends $g\bmod K^2$ to its image in $J/J^2$. Derivatives of these representatives verify every commutative square. The connecting homology map is obtained by lifting a cycle from $J/J^2$ to $K/K^2$, taking its derivative (which lies in the image of the left differential module), and reducing modulo the image of $I/I^2\otimes C$. Changing the lift changes this by a boundary. The same lifting calculation proves exactness at each homology term.
The exactness of the top row follows as the $\text{d}x_s$,
$\text{d}y_t$ form a basis for the middle module.
The map $\gamma$ factors

$$
A[x_s, y_t] \to B[y_t] \to C
$$

with surjective first arrow and second arrow equal to $\beta$.
Thus we see that $K \to J$ is surjective.
Moreover, the kernel of the first displayed arrow is
$IA[x_s, y_t]$. Hence $I/I^2 \otimes C$ surjects onto the
kernel of $K/K^2 \to J/J^2$. Finally, we can use
Lemma [F.11](#algebra-lemma-NL-homotopy)
to identify the terms as homology groups of the naive
cotangent complexes.

The final assertion is a statement in homological algebra.
Recall that $\NL_{B/A} = (N^{-1} \to N^0)$ is a two term
complex of $B$-modules with $N^0$ free and cohomology modules
$H^0 = \Omega_{B/A}$ and $H^{-1} = H_1(L_{B/A})$.
Write $M \subset N^0$ for the image of the differential.
If $\text{Tor}_1^B(H^0, C) = 0$, then we have an exact sequence

$$
0 \to M \otimes_B C \to N^0 \otimes_B C \to H^0 \otimes_B C \to 0
$$

Since $N^0$ is free, we also see that $\text{Tor}_2^B(H^0, C) =
\text{Tor}_1^B(M, C)$. Hence if $\text{Tor}_2^B(H^0, C) = 0$
then we also have an exact sequence

$$
0 \to H^{-1} \otimes_B C \to N^{-1} \otimes_B C \to M \otimes_B C \to 0
$$

Putting everything together we see that if
$\text{Tor}_1^B(H^0, C) = 0$ and $\text{Tor}_2^B(H^0, C) = 0$,
then $H^{-1} \otimes_B C$ is the kernel of
$N^{-1} \otimes_B C \to N^0 \otimes_B C$ as desired.
 ∎

<a id="algebra-lemma-extension"></a>

#### Lemma F.43: extension

*Adapted from the Stacks project, algebra.tex, lines 398–483.*

For $0\to M_1\to M_2\to M_3\to0$, finite generation is preserved under extensions and quotients; finite presentation is preserved under extensions; a quotient of a finitely presented module by a finite submodule is finitely presented; and if $M_3$ is finitely presented and $M_2$ finite, then $M_1$ is finite.

**Proof.** 
Generators of $M_1$ and lifts of generators of $M_3$ generate $M_2$; images of generators generate any quotient. For the last assertion take a finite free surjection $F\to M_2$. Its composite $F\to M_3$ has finite kernel $K$: to see presentation independence, compare it with a fixed finite presentation of $M_3$ by lifting each of the two free bases to the other free module; the finite defining relations and the finite substitution differences generate the kernel. The image of $K$ in $M_2$ is precisely $M_1$, which is consequently finite.

If $M_2=F/K$ has finite generators and relations and $M_1$ is finite, lift its finite generator list to $F$; adjoining those lifts to the finite generator list of $K$ presents $M_3$. Finally for an extension of two finitely presented modules take finite free surjections $F_i\to M_i$ for $i=1,3$ and lift the second basis to $M_2$. Then $F_1\oplus F_3\to M_2$ is surjective. Its kernel fits into a short exact sequence of the two presentation kernels: projection to $F_3$ gives the map onto the third kernel, and subtracting a suitable $F_1$ lift proves surjectivity; its kernel is the first presentation kernel. Both outer kernels are finite, so the generator argument at the start makes the middle kernel finite. This proves finite presentation of $M_2$.
 ∎

<a id="algebra-lemma-finite-presentation-independent"></a>

#### Lemma F.44: finite presentation independent

*Adapted from the Stacks project, algebra.tex, lines 573–589.*

Let $R \to S$ be a ring map of finite presentation.
For any surjection $\alpha : R[x_1, \ldots, x_n] \to S$ the
kernel of $\alpha$ is a finitely generated ideal in $R[x_1, \ldots, x_n]$.

**Proof.** 
Write $S = R[y_1, \ldots, y_m]/(f_1, \ldots, f_k)$.
Choose $g_i \in R[y_1, \ldots, y_m]$ which are lifts
of $\alpha(x_i)$. Then we see that $S = R[x_i, y_j]/(f_l, x_i - g_i)$.
Choose $h_j \in R[x_1, \ldots, x_n]$ such that $\alpha(h_j)$
corresponds to $y_j \bmod (f_1, \ldots, f_k)$. Consider
the map $\psi : R[x_i, y_j] \to R[x_i]$, $x_i \mapsto x_i$,
$y_j \mapsto h_j$. Then the kernel of $\alpha$
is the image of $(f_l, x_i - g_i)$ under $\psi$ and we win.
 ∎

<a id="algebra-lemma-flat-fibre-smooth"></a>

#### Lemma F.45: flat fibre smooth

*Adapted from the Stacks project, algebra.tex, lines 39115–39149.*

Let $R \to S$ be a ring map.
Let $\mathfrak q \subset S$ be a prime lying over the
prime $\mathfrak p$ of $R$. Assume

1. there exists a $g \in S$, $g \not\in \mathfrak q$
such that $R \to S_g$ is of finite presentation,

1. the local ring homomorphism
$R_{\mathfrak p} \to S_{\mathfrak q}$ is flat,

1. the fibre $S \otimes_R \kappa(\mathfrak p)$ is smooth
over $\kappa(\mathfrak p)$ at the prime corresponding
to $\mathfrak q$.

Then $R \to S$ is smooth at $\mathfrak q$.

**Proof.** 
By Lemmas [F.87](#algebra-lemma-syntomic) and [F.82](#algebra-lemma-smooth-over-field)
we see that there exists a $g \in S$, $g \not \in \mathfrak q$, such that $S_g$ is a
relative global complete intersection. Replacing $S$ by $S_g$ we may assume
$S = R[x_1, \ldots, x_n]/(f_1, \ldots, f_c)$ is a relative
global complete intersection.
For any subset $I \subset \{1, \ldots, n\}$ of cardinality
$c$ consider the polynomial
$g_I = \det (\partial f_j/\partial x_i)_{j = 1, \ldots, c, i \in I}$
of Lemma [F.78](#algebra-lemma-relative-global-complete-intersection-smooth).
Note that the image $\overline{g}_I$ of $g_I$ in the polynomial ring
$\kappa(\mathfrak p)[x_1, \ldots, x_n]$ is the determinant
of the partial derivatives of the images $\overline{f}_j$ of the $f_j$
in the ring $\kappa(\mathfrak p)[x_1, \ldots, x_n]$. Thus the lemma follows
by applying Lemma [F.78](#algebra-lemma-relative-global-complete-intersection-smooth)
both to $R \to S$ and to
$\kappa(\mathfrak p) \to S \otimes_R \kappa(\mathfrak p)$.
 ∎

<a id="algebra-lemma-flat-over-regular"></a>

#### Lemma F.46: flat over regular

*Adapted from the Stacks project, algebra.tex, lines 34076–34098.*

Let $R \to S$ be a homomorphism of Noetherian local rings.
Assume that $R$ is a regular local ring and that a regular system
of parameters maps to a regular sequence in $S$. Then $R \to S$
is flat.

**Proof.** 
Suppose that $x_1, \ldots, x_d$ are a system of parameters of $R$
which map to a regular sequence in $S$. Note that
$S/(x_1, \ldots, x_d)S$ is flat over $R/(x_1, \ldots, x_d)$
as the latter is a field. Then $x_d$ is a nonzerodivisor in
$S/(x_1, \ldots, x_{d - 1})S$ hence $S/(x_1, \ldots, x_{d - 1})S$
is flat over $R/(x_1, \ldots, x_{d - 1})$ by the local criterion
of flatness (see Lemma [AG-CA-08, Corollary 4.4 and equation (6)](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/faithful-flatness-and-the-local-criterion-for-flatness.html)
and remarks following). Then $x_{d - 1}$ is a nonzerodivisor in
$S/(x_1, \ldots, x_{d - 2})S$ hence $S/(x_1, \ldots, x_{d - 2})S$
is flat over $R/(x_1, \ldots, x_{d - 2})$ by the local criterion
of flatness (see Lemma [AG-CA-08, Corollary 4.4 and equation (6)](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/faithful-flatness-and-the-local-criterion-for-flatness.html)
and remarks following). Continue till one reaches the conclusion
that $S$ is flat over $R$.
 ∎

<a id="algebra-lemma-flat-over-regular-with-regular-fibre"></a>

#### Lemma F.47: flat over regular with regular fibre

*Adapted from the Stacks project, algebra.tex, lines 28729–28751.*

A flat local map of Noetherian local rings with regular source and regular closed fibre has regular target.

**Proof.** 
Let the source dimension be $d$ and fibre dimension $e$. Choose $d$ source parameters and lift $e$ fibre parameters. Together they generate the target maximal ideal: the fibre generators generate it modulo the source maximal ideal, which the source parameters already generate. The flat local dimension formula AG-CA-11, Theorem 5.1, gives target dimension $d+e$. Its embedding dimension is at most the number $d+e$ of these generators, and at least its dimension by the height theorem AG-CA-11, Theorem 3.1. Equality is the definition of a regular local ring.
 ∎

<a id="algebra-lemma-flatness-descends-more-general"></a>

#### Lemma F.48: flatness descends more general

*Adapted from the Stacks project, algebra.tex, lines 9135–9161.*

Let $R$ be a ring. Let $S \to S'$ be a flat map of $R$-algebras.
Let $M$ be a module over $S$, and set $M' = S' \otimes_S M$.

1. If $M$ is flat over $R$, then $M'$ is flat over $R$.

1. If $S \to S'$ is faithfully flat, then $M$ is flat
over $R$ if and only if $M'$ is flat over $R$.

**Proof.** 
Let $N \to N'$ be an injection of $R$-modules. By the flatness
of $S \to S'$ we have

$$
\ker(N \otimes_R M \to N' \otimes_R M) \otimes_S S'
=
\ker(N \otimes_R M' \to N' \otimes_R M')
$$

If $M$ is flat over $R$, then the left hand side is zero and
we find that $M'$ is flat over $R$ by the second characterization
of flatness in Lemma [AG-CA-07, Theorem 2.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/tor-and-flat-modules.html).
If $M'$ is flat over $R$ then we have the vanishing of the right hand side
and if in addition $S \to S'$ is faithfully flat, this implies that
$\ker(N \otimes_R M \to N' \otimes_R M)$ is zero which in turn
shows that $M$ is flat over $R$.
 ∎

<a id="algebra-lemma-formally-smooth-extensions-easy"></a>

#### Lemma F.49: formally smooth extensions easy

*Adapted from the Stacks project, algebra.tex, lines 45971–46012.*

Let $K/k$ be an extension of fields.

1. If $K$ is purely transcendental over $k$, then
$K$ is formally smooth over $k$.

1. If $K$ is separable algebraic over $k$, then $K$ is
formally smooth over $k$.

1. If $K$ is separable over $k$, then $K$ is formally smooth
over $k$.

**Proof.** 
For (1) write $K = k(x_j; j \in J)$. Suppose that
$A$ is a $k$-algebra, and $I \subset A$ is an ideal of
square zero. Let $\varphi : K \to A/I$ be a $k$-algebra map.
Let $a_j \in A$ be an element such that $a_j \mod I = \varphi(x_j)$.
Then it is easy to see that there is a unique $k$-algebra
map $K \to A$ which maps $x_j$ to $a_j$ and which reduces
to $\varphi$ mod $I$. Hence $k \subset K$ is formally smooth.

In case (2) we see that $k \subset K$ is a colimit of
étale ring extensions. An étale ring map is formally étale
(Lemma [AG-CA-17, Theorem 2.2 and Proposition 6.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/formally-smooth-unramified-and-etale-ring-maps.html)). Hence this case follows from
Lemma [F.22](#algebra-lemma-colimit-formally-etale) and the trivial observation
that a formally étale ring map is formally smooth.

In case (3), write $K = \operatorname*{colim} K_i$ as the filtered colimit of its
finitely generated $k$-subextensions. By
Definition [F.5](#algebra-definition-separable-field-extension)
each $K_i$ is separable algebraic over a purely transcendental
extension of $k$. Hence $K_i/k$ is formally smooth by cases (1) and (2) and
Lemma [AG-CA-17, Theorem 1.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/formally-smooth-unramified-and-etale-ring-maps.html). Thus
$H_1(L_{K_i/k}) = 0$ by
Lemma [F.17](#algebra-lemma-characterize-formally-smooth-field-extension).
Hence $H_1(L_{K/k}) = 0$ by Lemma [F.24](#algebra-lemma-colimits-NL).
Hence $K/k$ is formally smooth by
Lemma [F.17](#algebra-lemma-characterize-formally-smooth-field-extension) again.
 ∎

<a id="algebra-lemma-geometrically-regular"></a>

#### Lemma F.50: geometrically regular

*Adapted from the Stacks project, algebra.tex, lines 48753–48798.*

For a Noetherian $k$-algebra, regularity after every finitely generated field extension is equivalent to regularity after every finite purely inseparable field extension.

**Proof.** 
One implication is immediate. For the other, given a finitely generated $K/k$, choose $k'/k$ and $K'/K$ by the explicit separabilization proof [F.69](#algebra-lemma-make-separably-generated). The assumed $A\otimes_k k'$ is regular and Noetherian. Write $K'$ as the localization of the smooth finite-type $k'$-domain constructed in the field lemma. Base change gives a smooth algebra over $A\otimes_k k'$. Smooth maps are flat by AG-CA-18, Theorem 6.1, and their residue-field fibres are regular by AG-CA-18, Theorem 2.1; regularity ascent proved above makes this base-changed algebra regular. Localization then makes $A\otimes_k K'$ regular. The map $A\otimes_k K\to A\otimes_kK'$ is faithfully flat, so regularity descent proved above makes $A\otimes_k K$ regular. These rings are Noetherian because finitely generated field tensor is a localization of a finite-type polynomial extension, the Noetherian field-tensor argument already written in this lesson.
 ∎

<a id="algebra-lemma-geometrically-regular-descent"></a>

#### Lemma F.51: geometrically regular descent

*Adapted from the Stacks project, algebra.tex, lines 48815–48834.*

Geometric regularity descends through faithfully flat maps of Noetherian $k$-algebras.

**Proof.** 
For a finite purely inseparable $k'/k$, field tensor preserves faithful flatness by AG-CA-08, Proposition 2.3. The target tensor ring is regular by hypothesis, so the regularity descent proof above makes the source tensor ring regular. The finite purely inseparable criterion just proved gives geometric regularity of the source. No additional fibre assertion is assumed.
 ∎

<a id="algebra-lemma-geometrically-regular-over-subfields"></a>

#### Lemma F.52: geometrically regular over subfields

*Adapted from the Stacks project, algebra.tex, lines 48851–48866.*

If $A$ is Noetherian and geometrically regular over $k$, then $A\otimes_kE$ is regular for any field extension $E/k$ for which this tensor product is Noetherian. If $A\otimes_kE$ is Noetherian, it is geometrically regular over $E$. Also if $k$ is a directed union of subfields $k_i$ and $A$ is geometrically regular over every $k_i$, then it is geometrically regular over $k$.

**Proof.** 
Write $E$ as the directed union of its finitely generated subfields $E_i$. Fix a local ring $T=(A\otimes_kE)_{\mathfrak q}$. Its maximal ideal is finite, and a finite generating list lifts from one $A\otimes_k E_i$ after including the finitely many coefficients in the numerators and denominators. Put $B_i=(A\otimes_kE_i)_{\mathfrak q_i}$ at the contracted prime. The map $B_i\to T$ is flat local: field extension is flat, and the localizations preserve flatness. The extended ideal $\mathfrak q_iT$ contains the chosen maximal-ideal generators and lies in that maximal ideal, hence equals it. Its closed fibre is therefore the residue field of $T$, a regular ring. The source $B_i$ is regular by geometric regularity and Noetherian by the finite-type field argument. The already proved flat local ascent makes $T$ regular. This works at every prime.

For any finite purely inseparable $F/E$, the ring $(A\otimes_kE)\otimes_EF=A\otimes_kF$ is Noetherian, being finite over the given Noetherian ring. The argument just proved makes it regular. The finite purely inseparable criterion above now proves geometric regularity over $E$.

For the last assertion let $k'/k$ be finite purely inseparable. Choose its finite generator tower and the finite coefficients of the monic root equations, all in some $k_i$. Enlarge that index to include coefficients expressing products of a fixed $k$-basis of $k'$ and generators in that basis. Linear independence of that finite basis persists over every subfield; the product expressions give a field $k_i'\subset k'$ with the same basis over $k_i$, and $k\otimes_{k_i}k_i'=k'$. The extension $k_i'/k_i$ is finite purely inseparable because the generator powers lie in $k_i$. Therefore $A\otimes_kk'=A\otimes_{k_i}k_i'$ is regular by the hypothesis over $k_i$. The finite purely inseparable criterion proves geometric regularity over $k$.
 ∎

<a id="algebra-lemma-grothendieck-regular-sequence"></a>

#### Lemma F.53: grothendieck regular sequence

*Adapted from the Stacks project, algebra.tex, lines 24513–24526.*

For a flat local map of Noetherian local rings $R\to P$, a list whose reduction is regular in the closed fibre is regular in $P$, and every successive quotient remains flat over $R$.

**Proof.** 
For the first element apply AG-CA-08, Lemma 5.1, to multiplication $P\xrightarrow{f_1}P$. The target is $R$-flat, both modules are finite over the Noetherian local ring $P$, and the map on the closed fibre is injective. That exact proved lemma gives injectivity and flatness of $P/(f_1)$. Repeat on the successive local quotient, whose closed fibre is the corresponding regular quotient. Local Nakayama ensures that every quotient remains nonzero, since the elements belong to the maximal ideal. This proves every assertion by induction.
 ∎

<a id="algebra-lemma-henselian-cat-finite-etale"></a>

#### Lemma F.54: henselian cat finite etale

*Adapted from the Stacks project, algebra.tex, lines 43976–44032.*

For a henselian local ring $(R,\mathfrak m,k)$, reduction modulo $\mathfrak m$ gives an equivalence between finite etale $R$-algebras and finite products of finite separable extensions of $k$.

**Proof.** 
A finite algebra over $R$ is a product of local rings by AG-CA-20, Theorem 2.2. Each factor of a finite etale algebra is etale, by the lifting property restricted by its idempotent, and its residue is a finite separable field by AG-CA-17, Theorem 7.2. For full faithfulness it suffices to treat local factors $S_1,S_2$: a field map between their residues lifts uniquely to $S_1\to S_2$ by AG-CA-20, Theorem 1.2, since a finite local algebra over henselian $R$ is henselian by Proposition 3.1 there. Ring maps to a local factor select one source idempotent; its residue selects the same idempotent. Thus the local-factor statement proves full faithfulness for products.

For essential surjectivity, choose a finite separable tower $k=k_0\subset k_1\subset\cdots\subset k_t=L$ with each step generated by one element. Starting with $S_0=R$, lift the monic minimal polynomial to $S_{i-1}[T]$ and put $S_i=S_{i-1}[T]/(f_i)$. This ring is finite free over $S_{i-1}$ and has residue field $k_i$. Every maximal ideal contracts to the maximal ideal of $S_{i-1}$ by the integral maximal-ideal theorem, so $S_i$ is local with maximal ideal $\mathfrak mS_i$. The derivative $f_i'$ has nonzero residue in this field and hence is a unit. The one-equation Jacobian lift proves $S_i/S_{i-1}$ etale. Its finite etale composite over $R$ lifts $L$. Finite products lift the general object. This proof does not consume a decomposition theorem for arbitrary finite-type algebras over a henselian ring.
 ∎

<a id="algebra-lemma-huber"></a>

#### Lemma F.55: huber

*Adapted from the Stacks project, algebra.tex, lines 37957–37984.*

Let $S$ be a finitely presented $R$-algebra which has a presentation
$S = R[x_1, \ldots, x_n]/I$ such that $I/I^2$ is free over $S$. Then
$S$ has a presentation $S = R[y_1, \ldots, y_m]/(f_1, \ldots, f_c)$
such that $(f_1, \ldots, f_c)/(f_1, \ldots, f_c)^2$ is free with
basis given by the classes of $f_1, \ldots, f_c$.

**Proof.** 
Note that $I$ is a finitely generated ideal by
Lemma [F.44](#algebra-lemma-finite-presentation-independent).
Let $f_1, \ldots, f_c \in I$ be elements which map to a basis of $I/I^2$.
By Nakayama's lemma (Lemma [F.10](#algebra-lemma-NAK))
there exists a $g \in 1 + I$ such that

$$
g \cdot I \subset (f_1, \ldots, f_c)
$$

and $I_g \cong (f_1, \ldots, f_c)_g$. Hence we see that

$$
S \cong R[x_1, \ldots, x_n]/(f_1, \ldots, f_c)[1/g]
\cong R[x_1, \ldots, x_n, x_{n + 1}]/(f_1, \ldots, f_c, gx_{n + 1} - 1)
$$

as desired. It follows that $f_1, \ldots, f_c,gx_{n + 1} - 1$
form a basis for
$(f_1, \ldots, f_c, gx_{n + 1} - 1)/(f_1, \ldots, f_c, gx_{n + 1} - 1)^2$
for example by applying Lemma [F.72](#algebra-lemma-principal-localization-NL).
 ∎

<a id="algebra-lemma-isolated-point-fibre"></a>

#### Lemma F.56: isolated point fibre

*Adapted from the Stacks project, algebra.tex, lines 31543–31578.*

For a finite-type map $R\to S$ and a fibre point $q$, the following are equivalent: it is isolated in its fibre; its local fibre algebra is finite over the residue field; it is a closed fibre point with zero-dimensional local fibre ring; and one principal neighbourhood contains no other point of that fibre. These are also equivalent to zero dimension at that fibre point and to finite residue extension together with zero-dimensional local fibre ring.

**Proof.** 
Work in the finite-type field algebra $T=S\otimes_R\kappa(\mathfrak p)$. Its dimension-at-a-point formula AG-CA-09, Theorem 6.1, is $\dim_x\operatorname{Spec}T=\dim T_q+\operatorname{trdeg}\kappa(q)$. Both summands are nonnegative. Thus zero point-dimension is precisely local dimension zero and finite residue extension; the latter finiteness is equivalent to closedness by AG-CA-06, Theorem 2.1. A zero-dimensional neighbourhood exists by the definition of point-dimension and principal opens forming a basis. Its finite-type field algebra is Noetherian of dimension zero, hence Artinian by AG-CA-03, Theorem 4.2. Its finite product decomposition and finite residue fields imply it is finite-dimensional over the field: its finitely many maximal-ideal-power quotients have finite-dimensional successive layers because each ideal is finite. Its points are finitely many isolated points, and selecting the factor of $q$ gives a principal singleton neighbourhood.

Conversely an isolated point admits such a principal neighbourhood. Its only prime is $q$, so it is a zero-dimensional local finite-type algebra and the same Artinian-layer proof makes it finite-dimensional; localizing it again leaves it unchanged. If the local fibre ring is finite-dimensional, it is Artinian and its residue field is finite, giving the preceding zero-point-dimension criterion. Finally principal opens of $T$ lift to principal opens of $S$, after clearing the one coefficient denominator from the base. This identifies the last neighbourhood statement with the original fibre statement and proves every equivalence.
 ∎

<a id="algebra-lemma-lci"></a>

#### Lemma F.57: lci

*Adapted from the Stacks project, algebra.tex, lines 37341–37441.*

Let $k$ be a field.
Let $S$ be a finite type $k$-algebra.
Let $\mathfrak q$ be a prime of $S$.
Choose any presentation $S = k[x_1, \ldots, x_n]/I$.
Let $\mathfrak q'$ be the prime of $k[x_1, \ldots, x_n]$ corresponding
to $\mathfrak q$. Set
$c = \text{height}(\mathfrak q') - \text{height}(\mathfrak q)$,
in other words $\dim_{\mathfrak q}(S) = n - c$
(see Lemma [F.20](#algebra-lemma-codimension)). The following are equivalent

1. There exists a $g \in S$, $g \not \in \mathfrak q$
such that $S_g$ is a global complete intersection over $k$.

1. The ideal $I_{\mathfrak q'} \subset k[x_1, \ldots, x_n]_{\mathfrak q'}$
can be generated by $c$ elements.

1. The conormal module $(I/I^2)_{\mathfrak q}$ can be generated by
$c$ elements over $S_{\mathfrak q}$.

1. The conormal module $(I/I^2)_{\mathfrak q}$ is a free
$S_{\mathfrak q}$-module of rank $c$.

1. The ideal $I_{\mathfrak q'}$ can be generated by a regular sequence
in the regular local ring $k[x_1, \ldots, x_n]_{\mathfrak q'}$.

In this case any $c$ elements of $I_{\mathfrak q'}$
which generate $I_{\mathfrak q'}/\mathfrak q'I_{\mathfrak q'}$
form a regular sequence in the local
ring $k[x_1, \ldots, x_n]_{\mathfrak q'}$.

**Proof.** 
Set $R = k[x_1, \ldots, x_n]_{\mathfrak q'}$. This is a
Cohen-Macaulay local
ring of dimension $\text{height}(\mathfrak q')$, see for example
Lemma [AG-CA-12, Corollary 6.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/regular-sequences-depth-and-cohen-macaulay-modules.html). Moreover,
$\overline{R} = R/IR = R/I_{\mathfrak q'} = S_{\mathfrak q}$
is a quotient of dimension $\text{height}(\mathfrak q)$.
Let $f_1, \ldots, f_c \in I_{\mathfrak q'}$ be elements
which generate $(I/I^2)_{\mathfrak q}$. By Lemma [F.10](#algebra-lemma-NAK)
we see that $f_1, \ldots, f_c$ generate $I_{\mathfrak q'}$.
Since the dimensions work out, we conclude
by Proposition [AG-CA-12, Theorem 4.2 and Corollary 4.3](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/regular-sequences-depth-and-cohen-macaulay-modules.html) that
$f_1, \ldots, f_c$ is a regular sequence in $R$.
By Lemma [F.74](#algebra-lemma-regular-quasi-regular) we see that
$(I/I^2)_{\mathfrak q}$ is free.
These arguments show that (2), (3), (4) are equivalent and
that they imply the last statement of the lemma, and therefore
they imply (5).

If (5) holds, say $I_{\mathfrak q'}$ is generated by a regular
sequence of length $e$, then
$\text{height}(\mathfrak q) = \dim(S_{\mathfrak q}) =
\dim(k[x_1, \ldots, x_n]_{\mathfrak q'}) - e =
\text{height}(\mathfrak q') - e$ by dimension theory,
see Section [the dimension notation](#dimension-context). We conclude that $e = c$.
Thus (5) implies (2).

We continue with the notation introduced in the first paragraph.
For each $f_i$ we may find $d_i \in k[x_1, \ldots, x_n]$,
$d_i \not \in \mathfrak q'$ such that
$f_i' = d_i f_i \in k[x_1, \ldots, x_n]$.
Then it is still true that $I_{\mathfrak q'} = (f_1', \ldots, f_c')R$.
Hence there exists a $g' \in k[x_1, \ldots, x_n]$, $g' \not \in \mathfrak q'$
such that $I_{g'} = (f_1', \ldots, f_c')$.
Moreover, pick $g'' \in k[x_1, \ldots, x_n]$, $g'' \not \in \mathfrak q'$
such that $\dim(S_{g''}) = \dim_{\mathfrak q} \operatorname{Spec}(S)$.
By Lemma [F.20](#algebra-lemma-codimension) this dimension is equal to $n - c$.
Finally, set $g$ equal to the image of $g'g''$ in $S$.
Then we see that

$$
S_g \cong k[x_1, \ldots, x_n, x_{n + 1}]
/
(f_1', \ldots, f_c', x_{n + 1}g'g'' - 1)
$$

and by our choice of $g''$ this ring has dimension $n - c$.
Therefore it is a global complete intersection.
Thus each of (2), (3), and (4) implies (1).

Assume (1). Let $S_g \cong k[y_1, \ldots, y_m]/(f_1, \ldots, f_t)$
be a presentation of $S_g$ as a global complete intersection.
Write $J = (f_1, \ldots, f_t)$. Let $\mathfrak q'' \subset k[y_1, \ldots, y_m]$
be the prime corresponding to $\mathfrak qS_g$. Note that
$t = m - \dim(S_g) =
\text{height}(\mathfrak q'') - \text{height}(\mathfrak q)$,
see Lemma [F.20](#algebra-lemma-codimension) for the last equality.
As seen in the proof of Lemma [AG-CA-12, Corollary 6.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/regular-sequences-depth-and-cohen-macaulay-modules.html) (and also above) the elements
$f_1, \ldots, f_t$ form a regular sequence in the local ring
$k[y_1, \ldots, y_m]_{\mathfrak q''}$.
By Lemma [F.74](#algebra-lemma-regular-quasi-regular) we see that
$(J/J^2)_{\mathfrak q}$ is free of rank $t$.
By Lemma [F.33](#algebra-lemma-conormal-module-localize) we have

$$
J/J^2 \oplus S_g^n \cong (I/I^2)_g \oplus S_g^m
$$

Thus $(I/I^2)_{\mathfrak q}$ is free of rank
$t + n - m = m - \dim(S_g) + n - m = n - \dim(S_g) =
\text{height}(\mathfrak q') - \text{height}(\mathfrak q) = c$.
Thus we obtain (4).
 ∎

<a id="algebra-lemma-lci-at-prime"></a>

#### Lemma F.58: lci at prime

*Adapted from the Stacks project, algebra.tex, lines 37592–37613.*

For a finite-type algebra $S$ over a field and a prime $\mathfrak q$, being a complete-intersection local ring is equivalent to a global complete-intersection principal neighbourhood and to its polynomial presentation kernel being generated locally by a regular sequence.

**Proof.** 
A polynomial local presentation $P_{\mathfrak q'}\twoheadrightarrow S_{\mathfrak q}$ has regular local ambient ring by AG-CA-14, Proposition 3.3 and Theorem 3.2. If its kernel is a regular list of length $c$, the conormal is free of rank $c$ by [F.74](#algebra-lemma-regular-quasi-regular). Conversely, if the conormal can be generated by $c=\dim P_{\mathfrak q'}-\dim S_{\mathfrak q}$ elements, Nakayama lifts them to generators of the ideal, and the CM expected-dimension criterion AG-CA-12, Theorem 4.2, makes them regular. Stable comparison of conormal modules under a change of polynomial presentation, proved above, preserves this assertion: the two ambient local dimensions differ by the difference of their variable counts, since AG-CA-09, Theorem 4.3, gives $\dim k[X]_{\mathfrak q'}=n-\operatorname{trdeg}_k\kappa(\mathfrak q)$. A stably free finite module over the local quotient is free, with the resulting prescribed rank.

For the definition allowing an arbitrary regular local ambient $Q$ essentially finite type over $k$, present $Q$ as a quotient of a polynomial local ring. Both ambient and quotient are regular. AG-CA-14, Proposition 1.4, proves that its kernel is generated by part of a regular parameter system. Lift the regular equations defining $S_{\mathfrak q}$ from $Q$ and append them to that system. By the definition of successive injectivity this concatenated list is regular. Hence the polynomial criterion applies; the reverse implication uses that polynomial ambient itself as $Q$.

To obtain a principal neighbourhood, clear the finitely many denominators in the local regular generator list. Kill the finite cokernel of its map onto the presentation ideal, then kill its finitely many positive Koszul homology modules by another element outside $\mathfrak q'$. At every prime on this neighbourhood containing the ideal the list is regular by the Noetherian $H_1$ criterion. Every minimal prime of the resulting equation ideal therefore has height exactly $c$: its quotient local ring has dimension zero, while each regular equation lowers dimension by one by AG-CA-12, Corollary 6.2. Each component has dimension $n-c$ by AG-CA-09, Theorem 4.3. Adjoining the localization variable gives a global presentation with $n+1$ variables and $c+1$ equations and this same dimension. This is a global complete intersection. A global complete-intersection presentation in turn has regular local equation lists by the minimal-prime height and CM argument proved above, completing the equivalence.
 ∎

<a id="algebra-lemma-limit-essentially-finite-presentation"></a>

#### Lemma F.59: limit essentially finite presentation

*Adapted from the Stacks project, algebra.tex, lines 33722–33770.*

A local essentially finitely presented map $R\to S$ is a directed colimit of local maps $R_\lambda\to S_\lambda$ essentially of finite type over $\mathbb Z$, with transition maps obtained by tensoring the base and localizing at the contracted prime.

**Proof.** 
Write $S=(R[X_1,\ldots,X_n]/(f_1,\ldots,f_c))_{\mathfrak q}$. For each finite subset of $R$ containing every equation coefficient, let $A_\lambda\subset R$ be the subring it generates over the image of $\mathbb Z$, and set $R_\lambda=(A_\lambda)_{\mathfrak m_R\cap A_\lambda}$. These are local subrings of $R$ with local inclusions. Their directed union is $R$, since each element is included in some finite subset. Form $C_\lambda=R_\lambda[X]/(f_i)$ and localize it at the inverse image $\mathfrak q_\lambda$ of the chosen target prime, giving $S_\lambda$. The maps are local and essentially finite type, and every stage is Noetherian by the Hilbert basis theorem.

Tensoring $C_\lambda$ with $R_\mu$ gives $C_\mu$. After initially inverting the complement of $\mathfrak q_\lambda$, localizing at the contracted prime inverts exactly the additional complement of $\mathfrak q_\mu$; the fraction universal property identifies this with $S_\mu$. Every fraction in $S$ has a numerator and denominator involving finitely many coefficients and hence occurs at one stage. If two fractions become equal, cross multiplication gives an equality in the polynomial quotient after one denominator outside $\mathfrak q$ is multiplied in. Its finite ideal-membership expression uses only finitely many coefficients, so the equality holds at a later stage. This proves both surjectivity and injectivity of $\operatorname{colim}S_\lambda\to S$, completing every claimed colimit identification.
 ∎

<a id="algebra-lemma-limit-module-essentially-finite-presentation"></a>

#### Lemma F.60: limit module essentially finite presentation

*Adapted from the Stacks project, algebra.tex, lines 33804–33859.*

A finitely presented module $M$ over the local algebra in the preceding approximation has finitely presented models $M_\lambda$ at sufficiently large stages, compatible by tensoring with $S_\mu$, with colimit $M$.

**Proof.** 
Choose a finite matrix presentation $S^a\xrightarrow{H}S^b\to M\to0$. Its finitely many entries are fractions and occur in one $S_{\lambda_0}$ by the preceding representative proof. Use their images to define $M_\lambda=\operatorname{coker}(S_\lambda^a\xrightarrow{H_\lambda}S_\lambda^b)$ at all later stages. Tensor is right exact, so $M_\lambda\otimes_{S_\lambda}S_\mu=M_\mu$. Taking the colimit of the finite free presentations gives the original cokernel: a vector represents zero precisely when it equals the image of a finite vector, and this finite equality holds at a common later stage. Thus the colimit is $M$, each model is finitely presented, and all ring-transition assertions remain those proved above.
 ∎

<a id="algebra-lemma-local-dimension-zero-henselian"></a>

#### Lemma F.61: local dimension zero henselian

*Adapted from the Stacks project, algebra.tex, lines 44097–44121.*

Let $(R, \mathfrak m)$ be a local ring of dimension $0$.
Then $R$ is henselian.

**Proof.** 
Let $R \to S$ be a finite ring map. By
Lemma [AG-CA-20, Theorem 1.2 and Theorem 2.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/henselian-local-rings-and-henselization.html)
it suffices to show that $S$ is a product of local rings. By
Lemma [AG-CA-05, Theorem 3.4](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/integral-extensions-lying-over-going-up-and-going-down.html)
$S$ has finitely many primes $\mathfrak m_1, \ldots, \mathfrak m_r$
which all lie over $\mathfrak m$. There are no inclusions among these
primes, see
Lemma [AG-CA-05, Theorem 3.3](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/integral-extensions-lying-over-going-up-and-going-down.html),
hence they are all maximal. Every element of
$\mathfrak m_1 \cap \ldots \cap \mathfrak m_r$ is nilpotent by
Lemma [AG-CA-01, Theorem 1.2 and Proposition 2.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/spectra-of-rings.html).
It follows $S$ is the product of the localizations of $S$ at the primes
$\mathfrak m_i$ by
Lemma [F.73](#algebra-lemma-product-local).
 ∎

<a id="algebra-lemma-local-syntomic"></a>

#### Lemma F.62: local syntomic

*Adapted from the Stacks project, algebra.tex, lines 37927–37941.*

If finitely many principal opens cover $\operatorname{Spec}S$ and $R\to S_{g_i}$ is syntomic on each, then $R\to S$ is syntomic.

**Proof.** 
Finite presentation follows from the finite-cover presentation lemma above. For flatness, tensor any injection of $R$-modules with $S$ and localize its kernel at each $g_i$. Each kernel is zero by the assumed chart flatness; local detection on this principal cover makes the original kernel zero. In every residue-field fibre these same opens cover, and their local complete-intersection covers combine to give a cover by global complete-intersection neighbourhoods. This is precisely the fibre definition of syntomicness. No Noetherian hypothesis is required for this gluing step.
 ∎

<a id="algebra-lemma-localization-colimit"></a>

#### Lemma F.63: localization colimit

*Adapted from the Stacks project, algebra.tex, lines 1260–1278.*

Localization of a module is the filtered colimit of copies of that module with transition maps given by multiplication by denominators. In particular a localization of a ring is the filtered colimit of its principal localizations.

**Proof.** 
For the first assertion, index the copies by finite products of elements of the multiplicative set, ordered with multiplication maps (or use the filtered divisibility category). Send an element $m$ in the copy indexed by $s$ to $m/s$. Every fraction has such a representative. Equality $m/s=n/t$ means $u(tm-sn)=0$ for some denominator $u$, precisely the equality at the common successor $ust$. Thus the map is bijective and respects addition and scalars. For rings use the principal subalgebras $R_s$: two such stages map to $R_{st}$; every element and every equality in the full localization is represented or becomes equal at a principal successor by the same fraction criterion. This proves the ring colimit assertion.
 ∎

<a id="algebra-lemma-localization-smooth-separable"></a>

#### Lemma F.64: localization smooth separable

*Adapted from the Stacks project, algebra.tex, lines 46075–46088.*

A finitely generated separably generated extension $K/k$ is the fraction field of a smooth finite-type $k$-domain. Conversely a fraction field of a smooth finite-type $k$-domain is separably generated.

**Proof.** 
For the forward implication choose a separating transcendence basis $T$, followed by a finite tower of separable simple algebraic generators. At each step its monic minimal polynomial has nonzero derivative at the generator. Clear finitely many coefficient denominators and invert that derivative and the needed denominator polynomials. These operations produce a finite-type domain inside $K$, with fraction field $K$, obtained from a polynomial algebra by a finite succession of standard étale extensions and principal localizations. AG-CA-17, Theorem 1.2 and Proposition 6.1, make it smooth.

For the converse localize the smooth algebra at its generic point; algebraic formal smoothness survives localization by AG-CA-17, Theorem 1.2. The field criterion proved below equates this with separability. Here is also why it supplies the finitely generated separating-basis convention. A standard smooth principal chart has an étale map from the polynomial algebra in the nonpivot variables: its square Jacobian and zero relative differentials prove this by AG-CA-17, Theorems 3.1 and 2.2. This map is flat by AG-CA-18, Corollary 6.2. A nonzero flat algebra over the polynomial domain has zero structural kernel, since tensoring multiplication by any nonzero element stays injective. Thus the nonpivot variables are algebraically independent in the domain. The dimension calculation AG-CA-18, Theorem 2.1, makes their number equal to the transcendence degree, so the fraction-field extension over them is finite algebraic. It is formally étale after localization, so its differentials vanish; the converse for finite fields in AG-CA-17, Lemma 7.1, makes it separable. They are the required separating transcendence basis.
 ∎

<a id="algebra-lemma-localize-NL"></a>

#### Lemma F.65: localize NL

*Adapted from the Stacks project, algebra.tex, lines 37118–37133.*

Let $A \to B$ be a ring map. Let $S \subset B$ be a multiplicative subset.
The canonical map $\NL_{B/A} \otimes_B S^{-1}B \to \NL_{S^{-1}B/A}$
is a quasi-isomorphism.

**Proof.** 
We have $S^{-1}B = \colim_{g \in S} B_g$ where we think of $S$
as a directed set (ordering by divisibility), see
Lemma [F.63](#algebra-lemma-localization-colimit).
By Lemma [F.72](#algebra-lemma-principal-localization-NL) each of the maps
$\NL_{B/A} \otimes_B B_g \to \NL_{B_g/A}$
is a quasi-isomorphism.
The lemma follows from Lemma [F.24](#algebra-lemma-colimits-NL).
 ∎

<a id="algebra-lemma-localize-relative-complete-intersection"></a>

#### Lemma F.66: localize relative complete intersection

*Adapted from the Stacks project, algebra.tex, lines 38108–38158.*

Let $R$ be Noetherian. Let $S = R[x_1, \ldots, x_n]/(f_1, \ldots, f_c)$.
We will find $h \in R[x_1, \ldots, x_n]$ which maps to $g \in S$
such that

$$
S_g = R[x_1, \ldots, x_n, x_{n + 1}]/(f_1, \ldots, f_c, hx_{n + 1} - 1)
$$

is a relative global complete intersection with a presentation as in
Definition [F.4](#algebra-definition-relative-global-complete-intersection)
in each of the following cases:

1. Let $I \subset R$ be an ideal. If the fibres of
$\operatorname{Spec}(S/IS) \to \operatorname{Spec}(R/I)$ have dimension $n - c$, then we can
find $(h, g)$ as above such that $g$ maps to $1 \in S/IS$.

1. Let $\mathfrak p \subset R$ be a prime. If
$\dim(S \otimes_R \kappa(\mathfrak p)) = n - c$, then we can
find $(h, g)$ as above such that $g$ maps to a unit of
$S \otimes_R \kappa(\mathfrak p)$.

1. Let $\mathfrak q \subset S$ be a prime lying over
$\mathfrak p \subset R$. If $\dim_{\mathfrak q}(S/R) = n - c$, then we can
find $(h, g)$ as above such that $g \not \in \mathfrak q$.

**Proof.** 
Ad (1). By Lemma [F.39](#algebra-lemma-dimension-fibres-bounded-open-upstairs)
there exists an open subset $W \subset \operatorname{Spec}(S)$ containing $V(IS)$
such that all fibres of $W \to \operatorname{Spec}(R)$ have dimension $\leq n - c$.
Say $W = \operatorname{Spec}(S) \setminus V(J)$. Then $V(J) \cap V(IS) = \emptyset$
hence we can find a $g \in J$ which maps to $1 \in S/IS$.
Let $h \in R[x_1, \ldots, x_n]$ be any preimage of $g$.

Ad (2). By Lemma [F.39](#algebra-lemma-dimension-fibres-bounded-open-upstairs)
there exists an open subset $W \subset \operatorname{Spec}(S)$ containing
$\operatorname{Spec}(S \otimes_R \kappa(\mathfrak p))$
such that all fibres of $W \to \operatorname{Spec}(R)$ have dimension $\leq n - c$.
Say $W = \operatorname{Spec}(S) \setminus V(J)$. Then
$V(J \cdot S \otimes_R \kappa(\mathfrak p)) = \emptyset$.
Hence we can find a $g \in J$ which maps to a unit in
$S\otimes_R\kappa(\mathfrak p)$. Indeed, the image of $J$ generates the unit ideal in this fibre. Write a finite relation $1=\sum_j\bar a_j\bar g_j$ with $g_j\in J$. Choose a common denominator $s\in R\setminus\mathfrak p$ for the $\bar a_j$. Multiplication gives $g=\sum_j a_jg_j\in J$ whose fibre image is the nonzero scalar $s$, hence is a unit.
Let $h \in R[x_1, \ldots, x_n]$ be any preimage of $g$.

Ad (3). By Lemma [F.39](#algebra-lemma-dimension-fibres-bounded-open-upstairs)
there exists a $g \in S$, $g \not \in \mathfrak q$
such that all nonempty fibres of $R \to S_g$
have dimension $\leq n - c$. Let $h \in R[x_1, \ldots, x_n]$
be any element that maps to $g$.

In every case, a nonempty fibre of this principal localization has dimension at least $n-c$: its ambient polynomial algebra has $n+1$ variables and the displayed ideal has $c+1$ generators, so the height bound [AG-CA-11, Theorem 3.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/dimension-theory-of-noetherian-local-rings.html) and the finite-type field dimension formula give that lower bound. The upper bound already proved therefore gives dimension exactly $n-c$. This is precisely the relative global complete-intersection definition for the displayed presentation.
 ∎

<a id="algebra-lemma-locally-smooth"></a>

#### Lemma F.67: locally smooth

*Adapted from the Stacks project, algebra.tex, lines 39014–39037.*

A ring map is smooth if and only if it is smooth on a principal neighbourhood of every target prime.

**Proof.** 
The forward direction follows from principal localization of standard smooth charts. Conversely, compactness of an affine spectrum gives a finite such cover: if principal opens cover, their elements generate the unit ideal, which has a finite expression for one. The finite-cover presentation argument proved above makes the algebra finitely presented. Its conormal complex has zero first homology on the cover; exact localization and local detection give zero first homology globally. Its degree-zero homology is the finitely presented differential module, free locally on refined standard smooth charts, hence finite projective by AG-CA-07, Theorem 5.3. The resulting conormal sequence splits because its quotient is projective, and AG-CA-17, Theorem 3.1, supplies formal smoothness. Together with finite presentation this is smoothness.
 ∎

<a id="algebra-lemma-make-etale-map-prescribed-residue-field"></a>

#### Lemma F.68: make etale map prescribed residue field

*Adapted from the Stacks project, algebra.tex, lines 41287–41319.*

For a prime $\mathfrak p$ of $R$ and a finite separable extension $L/\kappa(\mathfrak p)$, some finitely presented etale $R$-algebra has a point over $\mathfrak p$ with this prescribed residue field.

**Proof.** 
Choose finitely many elements generating $L$ as a field, and adjoin them one at a time. At a given step their monic minimal polynomial over the preceding residue field has nonzero derivative at the chosen element, since it is separable. Lift its finitely many coefficients to the local ring of the already constructed algebra at the chosen prime. Clear finitely many denominators to obtain that polynomial over one principal neighbourhood. Adjoin a root of this monic polynomial and invert its derivative. The square one-equation Jacobian calculation of AG-CA-17, Proposition 6.1, makes this algebra etale; its chosen residue-field evaluation maps the root to the required element. The kernel of this evaluation at the chosen point has exactly the enlarged residue field, since the localized base residue field and the root generate it. The polynomial coefficients and inverses involved at each of the finitely many steps descend from the local ring by finitely many denominator clearings. Composing the resulting finitely presented etale maps gives the asserted $R$-algebra. This construction uses a finite separable tower and does not assume a primitive element theorem.
 ∎

<a id="algebra-lemma-make-separably-generated"></a>

#### Lemma F.69: make separably generated

*Adapted from the Stacks project, algebra.tex, lines 10182–10253.*

For a finitely generated field extension $K/k$ there are finite purely inseparable extensions $k'/k$ and $K'/K$ with a commutative field square and $K'/k'$ separably generated.

**Proof.** 
Only characteristic $p>0$ needs proof. Choose a transcendence basis $T$; $K/k(T)$ is finite. For any finite extension, its separable elements form a finite separable subfield and the extension over it is purely inseparable: for each algebraic generator repeatedly write its irreducible polynomial as a polynomial in $X^p$ until its derivative is nonzero; the corresponding $p$th power of the generator is separable. Finite composita of separable simple extensions are separable, since they are generated by distinct-root polynomial towers. Thus sufficiently large $p$th powers of all generators lie in that separable subfield. Let $K_s$ be this subfield over $k(T)$ and induct on the finite $p$-power degree $[K:K_s]$.

If that degree exceeds one, choose $\beta\in K\setminus K_s$ with $\alpha=\beta^p\in K_s$. Write the monic separable minimal polynomial of $\alpha$ over $k(T)$ as $P(X)=X^d+\sum a_iX^i$. Each $a_i$ is a rational function involving finitely many coefficients of $k$. Adjoin their $p$th roots to $k$ to obtain a finite purely inseparable $k'/k$, and adjoin $T_j^{1/p}$ to the rational base. Every $a_i$ is now a $p$th power: take the $p$th roots of its numerator and denominator coefficientwise and replace each $T_j$ by $T_j^{1/p}$. Set $F'=k'(T_j^{1/p})$ and let $L=KF'$. It is finite purely inseparable over $K$.

Let $Q(X)$ be the polynomial obtained by taking those coefficient roots, so $Q(X)^p=P(X^p)$. The element $\beta$ is a root of $Q$, and $Q'(\beta)^p=P'(\alpha)\ne0$. Its minimal polynomial over $F'$ is therefore separable. The compositum $K_sF'$ is separable over $F'$, because separable polynomials remain separable under every field extension. Hence $K_s(\beta)F'$ lies in the separable subfield $L_s$ of $L/F'$. Since $[K:K_s(\beta)]=[K:K_s]/p$, the degree $[L:L_s]$ is at most this smaller degree: base change cannot increase finite vector-space degree. Induct on this strictly smaller integer, regarding $T_j^{1/p}$ as a transcendence basis over $k'$. The resulting finite purely inseparable extensions compose to the desired $k'/k$ and $K'/K$. At degree one the extension is already separably generated. This supplies the coefficient-root detail and the strict induction decrease.
 ∎

<a id="algebra-lemma-matrix-left-inverse"></a>

#### Lemma F.70: matrix left inverse

*Adapted from the Stacks project, algebra.tex, lines 2709–2745.*

Let $R$ be a ring. Let $n \geq m$. Let $A$ be an
$n \times m$ matrix with coefficients in $R$. Let $J \subset R$
be the ideal generated by the $m \times m$ minors of $A$.

1. For any $f \in J$ there exists a $m \times n$ matrix $B$
such that $BA = f 1_{m \times m}$.

1. If $f \in R$ and $BA = f 1_{m \times m}$ for some $m \times n$ matrix
$B$, then $f^m \in J$.

**Proof.** For $m=0$, the only minor is the empty determinant $1$, so $J=R$; both assertions hold for the unique matrix between the zero modules. Assume $m>0$. For $I\subset\{1,\ldots,n\}$ with $|I|=m$, let $E_I:R^n\to R^m$ select those coordinates in increasing order, and write $A_I=E_IA$.

For a square matrix $C$, its adjugate is the transpose of its signed cofactor matrix. The $(i,j)$ entry of $C\operatorname{adj}(C)$ is the cofactor expansion along row $j$, replacing that row by row $i$. It is $\det C$ when $i=j$ and zero when $i\ne j$, since then two rows coincide. The analogous column expansion gives $\operatorname{adj}(C)C=(\det C)1_m$ as well. The row and column expansions are obtained by grouping the signed permutation formula according to the chosen entry. Thus both identities hold over every commutative ring.

If $f=\sum_I c_I\det A_I$, set $B=\sum_I c_I\operatorname{adj}(A_I)E_I$. The identity just proved gives $BA=f1_m$, proving (1).

For (2), expand $\det(BA)$ by multilinearity in its $m$ columns, each a linear combination of columns of $B$. Terms selecting a repeated column vanish by alternation. Group the remaining terms by their $m$ distinct selected column indices $I$, in increasing order. The signed sum of the coefficients for each group is $\det A_I$, while its column determinant is $\det B^I$, where $B^I$ consists of columns indexed by $I$. Hence
$$
\det(BA)=\sum_{|I|=m}\det(B^I)\det(A_I).
$$
If $BA=f1_m$, its determinant is $f^m$, so the displayed identity gives $f^m\in J$. This proves (2) with no field, domain or reducedness hypothesis. ∎

<a id="algebra-lemma-presentation-sym-exterior"></a>

#### Lemma F.71: presentation sym exterior

*Adapted from the Stacks project, algebra.tex, lines 2282–2310.*

For $M_2\to M_1\to M\to0$, the kernel of $\operatorname{Sym}^n M_1\to\operatorname{Sym}^nM$ is the image of $M_2\otimes\operatorname{Sym}^{n-1}M_1$; the analogous statement holds for exterior powers.

**Proof.** 
Put $N=\operatorname{im}(M_2\to M_1)$. The symmetric algebra is the tensor algebra modulo the pairwise commutation relations. Quotienting it further by the degree-one elements of $N$ gives the symmetric algebra of $M_1/N=M$, because maps from either quotient to a commutative algebra are exactly linear maps from $M_1$ annihilating $N$. In degree $n$ the ideal generated by $N$ consists precisely of finite sums $n_i u_i$ with $u_i$ of degree $n-1$; lifting each $n_i$ from $M_2$ gives the asserted image. Surjectivity follows from lifting every factor of a pure symmetric tensor. The exterior algebra is the tensor algebra modulo $x\otimes x$ for every degree-one element $x$; the same quotient and degree argument gives the exterior assertion, with product denoted by wedge. This includes $n=1$; for $n=0$ the kernel is zero.
 ∎

<a id="algebra-lemma-principal-localization-NL"></a>

#### Lemma F.72: principal localization NL

*Adapted from the Stacks project, algebra.tex, lines 37031–37116.*

Let $A \to B$ be a ring map. Let $g \in B$. Suppose $\alpha : P \to B$
is a presentation with kernel $I$. Then a presentation of $B_g$ over $A$ is
the map

$$
\beta : P[x] \longrightarrow B_g
$$

extending $\alpha$ and sending $x$ to $1/g$.
The kernel $J$ of $\beta$ is generated by $I$ and the element $f x - 1$
where $f \in P$ is an element mapped to $g \in B$ by $\alpha$. In this
situation we have

1. $J/J^2 = (I/I^2)_g \oplus B_g (f x - 1)$,

1. $\Omega_{P[x]/A} \otimes_{P[x]} B_g =
\Omega_{P/A} \otimes_P B_g \oplus B_g \text{d}x$,

1. $\operatorname{NL}(\beta) \cong
\operatorname{NL}(\alpha) \otimes_B B_g \oplus (B_g \xrightarrow{g} B_g).$

Hence the canonical map $\NL_{B/A} \otimes_B B_g \to \NL_{B_g/A}$
is a homotopy equivalence.

**Proof.** 
Since $P[x]/(I, fx - 1) = B[x]/(gx - 1) = B_g$ we get the statement about
$I$ and $fx - 1$ generating $J$. Consider the commutative diagram

$$
\begin{gathered}
0 \xrightarrow{} \Omega_{P/A} \otimes_P B_g \\
\Omega_{P/A} \otimes_P B_g \xrightarrow{} \Omega_{P[x]/A} \otimes_{P[x]} B_g \\
\Omega_{P[x]/A} \otimes_{P[x]} B_g \xrightarrow{} \Omega_{B[x]/B} \otimes_{B[x]} B_g \\
\Omega_{B[x]/B} \otimes_{B[x]} B_g \xrightarrow{} 0 \\
(I/I^2)_g \xrightarrow{} J/J^2 \\
(I/I^2)_g \xrightarrow{} \Omega_{P/A} \otimes_P B_g \\
J/J^2 \xrightarrow{} (gx - 1)/(gx - 1)^2 \\
J/J^2 \xrightarrow{} \Omega_{P[x]/A} \otimes_{P[x]} B_g \\
(gx - 1)/(gx - 1)^2 \xrightarrow{} 0 \\
(gx - 1)/(gx - 1)^2 \xrightarrow{} \Omega_{B[x]/B} \otimes_{B[x]} B_g
\end{gathered}
$$

with exact rows of Lemma [F.42](#algebra-lemma-exact-sequence-NL).
The $B_g$-module $\Omega_{B[x]/B} \otimes_{B[x]} B_g$ is free of
rank $1$ on $\text{d}x$. The element $\text{d}x$ in the
$B_g$-module $\Omega_{P[x]/A} \otimes_{P[x]} B_g$ provides
a splitting for the top row. The element $gx - 1 \in (gx - 1)/(gx - 1)^2$
is mapped to $g\text{d}x$ in $\Omega_{B[x]/B} \otimes_{B[x]} B_g$
and hence $(gx - 1)/(gx - 1)^2$ is free of rank $1$ over $B_g$.
(This can also be seen by arguing that $gx - 1$ is a nonzerodivisor
in $B[x]$ because it is a polynomial with invertible constant term
and any nonzerodivisor gives a quasi-regular sequence of length $1$
by Lemma [F.74](#algebra-lemma-regular-quasi-regular).)

Let us prove $(I/I^2)_g \to J/J^2$ is injective. Consider the $P$-algebra map

$$
\pi : P[x] \to (P/I^2)_f = P_f/I_f^2
$$

sending $x$ to $1/f$. Since $J$ is generated by $I$ and $fx - 1$
we see that $\pi(J) \subset (I/I^2)_f = (I/I^2)_g$. Since this
is an ideal of square zero we see that $\pi(J^2) = 0$.
If $a \in I$ maps to an element of $J^2$ in $J$, then
$\pi(a) = 0$, which implies that $a$ maps to zero in $I_f/I_f^2$.
This proves the desired injectivity.

Thus we have a short exact sequence of two term complexes

$$
0 \to \operatorname{NL}(\alpha) \otimes_B B_g \to \operatorname{NL}(\beta)
\to (B_g \xrightarrow{g} B_g) \to 0
$$

Such a short exact sequence can always be split in the category of
complexes. In our particular case we can take as splittings

$$
J/J^2 = (I/I^2)_g \oplus B_g (fx - 1)\quad\text{and}\quad
\Omega_{P[x]/A} \otimes B_g = \Omega_{P/A} \otimes B_g \oplus
B_g (g^{-2}\text{d}f + \text{d}x).
$$

This works because
$\text{d}(fx - 1) = x\text{d}f + f \text{d}x =
g(g^{-2}\text{d}f + \text{d}x)$
in $\Omega_{P[x]/A} \otimes B_g$.
 ∎

<a id="algebra-lemma-product-local"></a>

#### Lemma F.73: product local

*Adapted from the Stacks project, algebra.tex, lines 13035–13062.*

A ring with finitely many maximal ideals and locally nilpotent Jacobson radical is the product of its localizations at those ideals; every prime is maximal.

**Proof.** 
Write $I=\bigcap_i\mathfrak m_i$. Every element of $I$ is nilpotent, so every prime contains $I$, hence the product of the finitely many $\mathfrak m_i$, and therefore one maximal ideal. Thus these are all the primes. The Chinese remainder calculation gives $R/I=\prod_iR/\mathfrak m_i$: for two comaximal ideals choose $a+b=1$ with $a$ in the first and $b$ in the second and use $ub+va$ to lift a prescribed pair; induction gives the finite version. Idempotents lift uniquely across a nil ideal by AG-CA-01, Lemma 5.1. Lift the coordinate idempotents to $e_i$. Their products $e_ie_j$ and the difference $\sum e_i-1$ are idempotents in a nil ideal, hence zero. Consequently $R\to\prod_i e_iR$, $r\mapsto(e_ir)$, has inverse $(r_i)\mapsto\sum r_i$. The factor $e_iR$ has just the prime corresponding to $\mathfrak m_i$, so is local and is the localization $R_{\mathfrak m_i}$ by the fraction universal property. This proves the claimed product.
 ∎

<a id="algebra-lemma-regular-quasi-regular"></a>

#### Lemma F.74: regular quasi regular

*Adapted from the Stacks project, algebra.tex, lines 17680–17766.*

If $f_1,\ldots,f_c$ is a regular sequence in $A$, the conormal module of $I=(f_1,\ldots,f_c)$ is free over $A/I$ on the classes of the $f_i$. Only this consequence of quasi-regularity is used here.

**Proof.** 
First prove that every relation $\sum a_if_i=0$ is generated by the pairwise Koszul relations. For $c=1$, injectivity of $f_1$ gives $a_1=0$. For $c>1$, reduction modulo $(f_1,\ldots,f_{c-1})$ and injectivity of $f_c$ give $a_c=\sum_{i<c}b_if_i$. Subtract from the relation the sum of the relations $b_i(f_ie_c-f_ce_i)$, making its last coefficient zero. Apply induction to the remaining coefficients. In particular all coefficients of every relation lie in $I$. Now if $\sum a_if_i\in I^2$, subtract a displayed finite sum of products $f_if_j$, changing each $a_i$ by an element of $I$, to obtain a relation equal to zero. The preceding calculation puts its coefficients in $I$, hence puts the original $a_i$ in $I$. This proves injectivity of $(A/I)^c\to I/I^2$; generation proves surjectivity.
 ∎

<a id="algebra-lemma-regular-sequence-in-polynomial-ring"></a>

#### Lemma F.75: regular sequence in polynomial ring

*Adapted from the Stacks project, algebra.tex, lines 17576–17624.*

Let $R$ be a ring. Let $f_1, \ldots, f_r \in R$ which do not generate
the unit ideal. The following are equivalent:

1. any permutation of $f_1, \ldots, f_r$ is a regular sequence,

1. any subsequence of $f_1, \ldots, f_r$ (in the given order) is
a regular sequence, and

1. $f_1x_1, \ldots, f_rx_r$ is a regular sequence in the polynomial
ring $R[x_1, \ldots, x_r]$.

**Proof.** 
It is clear that (1) implies (2). We prove (2) implies (1) by induction
on $r$. The case $r = 1$ is trivial. The case $r = 2$ says that if
$a, b \in R$ are a regular sequence and $b$ is a nonzerodivisor, then
$b, a$ is a regular sequence. This is clear because the kernel of
$a : R/(b) \to R/(b)$ is isomorphic to the kernel of $b : R/(a) \to R/(a)$
if both $a$ and $b$ are nonzerodivisors. The case $r > 2$. Assume
(2) holds and say we want to prove $f_{\sigma(1)}, \ldots, f_{\sigma(r)}$
is a regular sequence for some permutation $\sigma$. We already know
that $f_{\sigma(1)}, \ldots, f_{\sigma(r - 1)}$ is a regular sequence
by induction. Hence it suffices to show that $f_s$ where $s = \sigma(r)$
is a nonzerodivisor modulo $f_1, \ldots, \hat f_s, \ldots, f_r$.
If $s = r$ we are done. If $s < r$, then note that $f_s$ and $f_r$
are both nonzerodivisors in the ring
$R/(f_1, \ldots, \hat f_s, \ldots, f_{r - 1})$
(by induction hypothesis again). Since we know $f_s, f_r$ is a
regular sequence in that ring we conclude by the case of sequence of length
$2$ that $f_r, f_s$ is too.

Note that $R[x_1, \ldots, x_r]/(f_1x_1, \ldots, f_ix_i)$ as an $R$-module
is a direct sum of the modules

$$
R/I_E \cdot x_1^{e_1} \ldots x_r^{e_r}
$$

indexed by multi-indices $E = (e_1, \ldots, e_r)$ where
$I_E$ is the ideal generated by $f_j$ for $1 \leq j \leq i$
with $e_j > 0$. Hence $f_{i + 1}x_{i + 1}$ is a nonzerodivisor on this if
and only if $f_{i + 1}$ is a nonzerodivisor on $R/I_E$ for all $E$.
Taking $E$ with all positive entries, we see that $f_{i + 1}$
is a nonzerodivisor on $R/(f_1, \ldots, f_i)$. Thus (3) implies (2).
Conversely, if (2) holds, then any subsequence of
$f_1, \ldots, f_i, f_{i + 1}$ is a regular sequence
in particular $f_{i + 1}$ is a nonzerodivisor on all $R/I_E$.
In this way we see that (2) implies (3).
 ∎

<a id="algebra-lemma-relative-global-complete-intersection"></a>

#### Lemma F.76: relative global complete intersection

*Adapted from the Stacks project, algebra.tex, lines 38280–38292.*

A relative global complete intersection over a Noetherian base is syntomic.

**Proof.** 
It is finitely presented by its displayed finite equation list. Its fibres are global complete intersections by the dimension definition. Its flatness is the quotient-flatness conclusion of the conormal and regular-sequence lifting proof above. These are exactly the three syntomic conditions.
 ∎

<a id="algebra-lemma-relative-global-complete-intersection-conormal"></a>

#### Lemma F.77: relative global complete intersection conormal

*Adapted from the Stacks project, algebra.tex, lines 38204–38278.*

Let $R$ be Noetherian and let $S=R[X_1,\ldots,X_n]/(f_1,\ldots,f_c)$ have all its nonempty fibres of dimension $n-c$. At every prime above the equation ideal, the $f_i$ form a regular sequence in the corresponding polynomial local ring, its successive quotients are $R$-flat, and $(f)/(f)^2$ is free over $S$ on their classes. This is the Noetherian form consumed in desingularization.

**Proof.** 
Fix a base prime $\mathfrak p$ and put $k=\kappa(\mathfrak p)$. In $k[X]$ every minimal prime of the equation ideal has height at most $c$, by AG-CA-11, Theorem 3.1. Its component has dimension $n$ minus that height, by AG-CA-09, Theorem 4.3. The asserted fibre dimension $n-c$ forces every such height to equal $c$. At a prime $\mathfrak r$ containing the equations, $k[X]_{\mathfrak r}$ is regular local, hence CM by AG-CA-12, Theorem 6.1. For a minimal equation prime $\mathfrak a\subset\mathfrak r$, the CM dimension formula AG-CA-12, Lemma 5.4, gives dimension of this component of the quotient equal to $\dim k[X]_{\mathfrak r}-c$. Taking the maximum gives that same quotient dimension. The expected-dimension criterion AG-CA-12, Theorem 4.2, makes the $c$ equations a regular sequence in this fibre local ring.

The polynomial local ring over $R_{\mathfrak p}$ is flat, since polynomial extension is free and localization is flat. Apply the preceding regular-sequence lifting lemma to obtain regularity before reduction and flatness of every successive quotient. The elementary regular-sequence relation calculation proved at [F.74](#algebra-lemma-regular-quasi-regular) makes its conormal module free on the classes of the $f_i$ at every prime of $S$. The global map $S^c\to(f)/(f)^2$ is surjective and has zero kernel after every prime localization, so AG-CA-02, Theorem 5.1, makes it an isomorphism. Flatness of the quotient is likewise detected locally by the ideal injection criterion and local detection.
 ∎

<a id="algebra-lemma-relative-global-complete-intersection-smooth"></a>

#### Lemma F.78: relative global complete intersection smooth

*Adapted from the Stacks project, algebra.tex, lines 39071–39113.*

For the preceding Noetherian presentation, smoothness at a prime is equivalent to one $c\times c$ Jacobian minor being outside that prime.

**Proof.** 
The preceding conormal calculation identifies the two-term complex with $S^c\xrightarrow{J}S^n$. If a chosen maximal minor is invertible, the inverse of that square block gives a left inverse to $J$; elimination identifies its cokernel with a free module of rank $n-c$. The split conormal criterion AG-CA-17, Theorem 3.1, gives smoothness on that localization. Conversely smoothness supplies a left inverse after localization by that same criterion. Reducing at the prime preserves the left inverse. Thus the matrix over the residue field has rank $c$, and some $c$-minor is nonzero. Principal localization of the conormal complex is the explicit contractible-summand computation proved at [F.72](#algebra-lemma-principal-localization-NL).
 ∎

<a id="algebra-lemma-section-smooth"></a>

#### Lemma F.79: section smooth

*Adapted from the Stacks project, algebra.tex, lines 39859–39914.*

For a smooth ring map $R\to S$ with section $\sigma:S\to R$, put $I=\ker\sigma$. Then $I/I^2$ is finite projective over $R$. If it is free of rank $d$, the $I$-adic completion is $R[[T_1,\ldots,T_d]]$.

**Proof.** 
The map $s\mapsto s-\sigma(s)\bmod I^2$ is an $R$-derivation to $I/I^2$ and sends each $i\in I$ to its class. Universal differentials give the inverse to the natural map $I/I^2\to\Omega_{S/R}\otimes_SR$: both composites agree on the algebra generators and on the ideal classes. Smoothness makes $\Omega_{S/R}$ finite projective by the split conormal criterion AG-CA-17, Theorem 3.1, so its base change is finite projective. The ideal $I$ is finitely generated: for finite algebra generators $x_j$ of $S/R$, subtracting their section values shows that $x_j-\sigma(x_j)$ generate the section kernel.

Choose $t_i\in I$ representing a free conormal basis. Define a map $b:R[[T]]\to\widehat S$ by convergent evaluation $T_i\mapsto t_i$. It is surjective: start with the residue coefficient in $R$, then successively correct the error in $I^n/I^{n+1}$ by a homogeneous degree-$n$ polynomial in the $t_i$. These monomials generate that quotient because the $t_i$ generate $I/I^2$; expanding products proves this in every degree. The corrections converge in the completion.

The chosen conormal identification defines a first-order $R$-map $S\to R[[T]]/(T)^2$ sending $t_i$ to $T_i$ and reducing to $\sigma$. Formal smoothness of $S/R$, proved equivalent to the split conormal property in AG-CA-17, Theorem 3.1, lifts this map successively through the square-zero kernels $(T)^n/(T)^{n+1}$. Its compatible inverse limit sends $I$ into $(T)$, hence extends to a continuous map $a:\widehat S\to R[[T]]$. The composite $ab$ sends $T_i$ to $T_i$ plus terms of degree at least two. Such a substitution is an automorphism: recursively correct each inverse variable one homogeneous degree at a time; the linear term is identity, so the correction at each degree is uniquely its negative error, and the series converge. The same recursion proves that both composites with the resulting inverse are identity in every finite quotient and hence in the separated limit. Replace $a$ by $(ab)^{-1}a$. Then $ab=1$. Since $b$ is already surjective it is also injective and gives the required isomorphism.
 ∎

<a id="algebra-lemma-silly"></a>

#### Lemma F.80: silly

*Adapted from the Stacks project, algebra.tex, lines 2605–2636.*

Let $I_1,\ldots,I_r,J$ be ideals of a ring with $J\not\subset I_i$ for every $i$, and at most two of the $I_i$ not prime. Then $J$ contains an element outside all $I_i$.

**Proof.** 
For two ideals, choose $x\in J\setminus I_1$ and $y\in J\setminus I_2$. If neither already works, then $x\in I_2$, $y\in I_1$, and $x+y$ works. Remove any $I_i$ contained in another listed ideal, since avoidance of the larger ideal implies avoidance of the smaller. Induct on the number of remaining ideals. For $r\ge3$ renumber so $I_r$ is prime. Choose $x$ avoiding the first $r-1$ by induction. If $x\in I_r$, choose $y\in JI_1\cdots I_{r-1}\setminus I_r$: such $y$ exists because none of these factors is contained in the prime $I_r$, and products of separately chosen elements outside a prime stay outside it. Then $y\in I_i$ for $i<r$, so $x+y$ still avoids them, and it avoids $I_r$ because $x\in I_r$ and $y\notin I_r$.
 ∎

<a id="algebra-lemma-size-extension-pth-roots"></a>

#### Lemma F.81: size extension pth roots

*Adapted from the Stacks project, algebra.tex, lines 45787–45812.*

If $a_1,\ldots,a_n$ in a characteristic-$p$ field have independent absolute differentials, adjoining their $p$th roots has degree $p^n$.

**Proof.** 
First prove the absolute differential calculation used here. A maximal $p$-independent set is a $p$-basis, by the Zorn and degree-$p$ argument in AG-CA-19S, Lemma 1.1. In its monomial expansion define the partial derivation of one basis element by differentiating the corresponding monomial and killing all $p$th-power coefficients. The relations $T_b^p-b^p$ have derivative zero, so these are well-defined derivations. Their values on the basis elements show that their differentials are linearly independent; differentiating every expansion shows that they span. An expansion has all partial derivatives zero precisely when every exponent is zero, hence precisely when it lies in the subfield of $p$th powers. Thus $da=0$ if and only if $a\in k^p$.

For $n=1$ this proves $a_1$ is not a $p$th power. The monic polynomial $T^p-a_1$ is irreducible: any proper factor over $k$ is $(T-\alpha)^e$ in an algebraic closure, $1\le e<p$, and its coefficient $-e\alpha$ would put $\alpha\in k$. Suppose by induction the first $n-1$ roots give degree $p^{n-1}$, with their standard monomial basis. If $a_n$ became a $p$th power there, write a root in that basis and raise its expansion to $p$. Then $a_n=\sum_E\lambda_E^p\prod_{i<n}a_i^{e_i}$. Its differential belongs to the span of the preceding $da_i$, a contradiction. The same degree-$p$ irreducibility argument proves the last extension degree $p$, and multiplication of finite vector-space degrees gives $p^n$.
 ∎

<a id="algebra-lemma-smooth-over-field"></a>

#### Lemma F.82: smooth over field

*Adapted from the Stacks project, algebra.tex, lines 38622–38676.*

A smooth finite-type algebra over a field is locally a complete intersection.

**Proof.** 
At a given prime choose a standard smooth neighbourhood by AG-CA-17, Theorem 5.1. In its polynomial ambient local ring, the classes of its chosen equations in the maximal ideal modulo its square are linearly independent. Indeed, differentiating an element of the square gives zero after reduction to the residue field; a linear relation between those equation classes would therefore give the same relation between their differential rows, contradicting the invertible Jacobian minor. Extend the independent classes to a basis of the maximal ideal modulo its square. The ambient polynomial local ring is regular, so AG-CA-12, Theorem 6.1, makes this full minimal generator list a regular sequence; its initial equation list is regular. The complete-intersection neighbourhood criterion just proved gives a global complete-intersection chart around the prime. Such charts cover the spectrum, proving the local statement without any algebraic-closure reduction or omitted diagram calculation.
 ∎

<a id="algebra-lemma-smooth-syntomic"></a>

#### Lemma F.83: smooth syntomic

*Adapted from the Stacks project, algebra.tex, lines 38880–38951.*

Let $R \to S$ be a smooth ring map.
There exists an open covering of $\operatorname{Spec}(S)$ by
standard opens $D(g)$ such that each $S_g$ is standard smooth
over $R$. If $R$ is Noetherian, then $R \to S$ is syntomic.

**Proof.** 
Choose a presentation $\alpha : R[x_1, \ldots, x_n] \to S$
with kernel $I = (f_1, \ldots, f_m)$. For every subset
$E \subset \{1, \ldots, m\}$ consider the open
subset $U_E$ where the classes $f_e, e\in E$ freely generate
the finite projective $S$-module $I/I^2$. Here is the basis-open calculation: the split conormal sequence for smoothness makes $I/I^2$ a finite direct summand of $S^n$. The earlier [AG-RG-S01, Lemma 1.2](AG-RG-S01.md) makes it locally finite free. At any point choose a basis from the residue classes of the finitely many $f_i$. On a free neighbourhood, the determinant of their coordinate matrix is nonzero at that point; inverting it makes those selected classes a basis. Conversely basis status is exactly invertibility of that determinant there. Thus each $U_E$ is open, and these opens cover the spectrum.
We may cover $\operatorname{Spec}(S)$ by standard opens $D(g)$ each
completely contained in one of the opens $U_E$. For such a $g$
we look at the presentation

$$
\beta : R[x_1, \ldots, x_n, x_{n + 1}] \longrightarrow S_g
$$

mapping $x_{n + 1}$ to $1/g$. Setting $J = \ker(\beta)$ we
use Lemma [F.72](#algebra-lemma-principal-localization-NL) to see that
$J/J^2 \cong (I/I^2)_g \oplus S_g$ is free.
We may and do replace $S$ by $S_g$. Then using
Lemma [F.55](#algebra-lemma-huber) we may assume we have a presentation
$\alpha : R[x_1, \ldots, x_n] \to S$ with kernel $I = (f_1, \ldots, f_c)$
such that $I/I^2$ is free on the classes of $f_1, \ldots, f_c$.

Using the presentation $\alpha$ obtained at the end of the previous
paragraph, we more or less repeat this argument with
the basis elements $\text{d}x_1, \ldots, \text{d}x_n$
of $\Omega_{R[x_1, \ldots, x_n]/R}$.
Namely, for any subset $E \subset \{1, \ldots, n\}$ of cardinality $c$
we may consider the open subset $U_E$ of $\operatorname{Spec}(S)$ where
the differential of $\operatorname{NL}(\alpha)$ composed with the projection

$$
S^{\oplus c} \cong I/I^2
\longrightarrow
\Omega_{R[x_1, \ldots, x_n]/R} \otimes_{R[x_1, \ldots, x_n]} S
\longrightarrow
\bigoplus\nolimits_{i \in E} S\text{d}x_i
$$

is an isomorphism. Again we may find a covering of $\operatorname{Spec}(S)$
by (finitely many) standard opens $D(g)$ such that each $D(g)$
is completely contained in one of the opens $U_E$.
By renumbering, we may assume $E = \{1, \ldots, c\}$.
For a $g$ with $D(g) \subset U_E$ we look at the presentation

$$
\beta : R[x_1, \ldots, x_n, x_{n + 1}] \to S_g
$$

mapping $x_{n + 1}$ to $1/g$. Setting $J = \ker(\beta)$
we conclude from Lemma [F.72](#algebra-lemma-principal-localization-NL)
that $J = (f_1, \ldots, f_c, fx_{n + 1} - 1)$ where $\alpha(f) = g$
and that the composition

$$
J/J^2 \longrightarrow
\Omega_{R[x_1, \ldots, x_{n + 1}]/R} \otimes_{R[x_1, \ldots, x_{n + 1}]} S_g
\longrightarrow
\bigoplus\nolimits_{i = 1}^c S_g\text{d}x_i \oplus S_g \text{d}x_{n + 1}
$$

is an isomorphism. Reordering the coordinates as
$x_1, \ldots, x_c, x_{n + 1}, x_{c + 1}, \ldots, x_n$
we conclude that $S_g$ is standard smooth over $R$ as desired.

For the final consequence, suppose $R$ is Noetherian. Standard smooth algebras are syntomic
(Lemmas [F.85](#algebra-lemma-standard-smooth) and
[F.76](#algebra-lemma-relative-global-complete-intersection))
and being syntomic over $R$ is local on $S$
(Lemma [F.62](#algebra-lemma-local-syntomic)).
 ∎

<a id="algebra-lemma-snake"></a>

#### Lemma F.84: snake

*Adapted from the Stacks project, algebra.tex, lines 311–343.*

Given a commutative diagram

$$
\begin{gathered}
X \xrightarrow{} Y \\
X \xrightarrow{\alpha} U \\
Y \xrightarrow{} Z \\
Y \xrightarrow{\beta} V \\
Z \xrightarrow{} 0 \\
Z \xrightarrow{\gamma} W \\
0 \xrightarrow{} U \\
U \xrightarrow{} V \\
V \xrightarrow{} W
\end{gathered}
$$

of abelian groups with exact rows, there is a canonical exact sequence

$$
\ker(\alpha) \to \ker(\beta) \to \ker(\gamma)
\to
\operatorname{coker}(\alpha) \to \operatorname{coker}(\beta) \to \operatorname{coker}(\gamma)
$$

Moreover: if $X \to Y$ is injective, then the first map is
injective; if $V \to W$ is surjective, then the last
map is surjective.

**Proof.** 
The map $\partial : \ker(\gamma) \to \operatorname{coker}(\alpha)$ is defined
as follows. Take $z \in \ker(\gamma)$. Choose $y \in Y$ mapping to $z$.
Then $\beta(y) \in V$ maps to zero in $W$. Hence $\beta(y)$ is the image of
some $u \in U$. Set $\partial z = \overline{u}$, the class of $u$ in the
cokernel of $\alpha$. Changing the lift $y$ by the image of $x\in X$ changes $u$ by $\alpha(x)$, so the connecting map is well defined and additive. Exactness at $\ker\beta$ follows because a lift in $X$ of an element of $Y$ with zero image in $Z$ has $\alpha(x)=0$, using injectivity $U\to V$. Exactness at $\ker\gamma$ follows because $\partial z=0$ means $u=\alpha(x)$ for some $x$; then $y-x$ has zero image under $\beta$ and still maps to $z$. Conversely any such lift has connecting class zero. At $\operatorname{coker}\alpha$, if the image of $u$ in $V$ equals $\beta(y)$, its image $z$ in $Z$ is in $\ker\gamma$ and has $\partial z=[u]$; conversely this is the definition of $\partial$. At $\operatorname{coker}\beta$, if $v$ maps to $\gamma(z)$ in $W$, lift $z$ to $y\in Y$ and replace $v$ by $v-\beta(y)$. Exactness of the bottom row puts it in the image of $U$, so its class comes from $\operatorname{coker}\alpha$. The converse follows from the row being a complex. If $X\to Y$ is injective, so is its restriction to $\ker\alpha$. If $V\to W$ is surjective, every class modulo $\gamma(Z)$ has a representative lifted from $V$, proving the final surjectivity.
 ∎

<a id="algebra-lemma-standard-smooth"></a>

#### Lemma F.85: standard smooth

*Adapted from the Stacks project, algebra.tex, lines 38716–38780.*

Let
$S = R[x_1, \ldots, x_n]/(f_1, \ldots, f_c) = R[x_1, \ldots, x_n]/I$
be a standard smooth algebra. Then

1. the ring map $R \to S$ is smooth,

1. the $S$-module $\Omega_{S/R}$ is free on
$\text{d}x_{c + 1}, \ldots, \text{d}x_n$,

1. the $S$-module $I/I^2$ is free on the classes of $f_1, \ldots, f_c$,

1. for any $g \in S$ the ring map $R \to S_g$ is standard smooth,

1. for any ring map $R \to R'$ the base change
$R' \to R'\otimes_R S$ is standard smooth,

1. if $f \in R$ maps to an invertible element in $S$, then
$R_f \to S$ is standard smooth, and

1. the ring $S$ is a relative global complete intersection over $R$.

**Proof.** 
Consider the naive cotangent complex of the given presentation

$$
(f_1, \ldots, f_c)/(f_1, \ldots, f_c)^2
\longrightarrow
\bigoplus\nolimits_{i = 1}^n S \text{d}x_i.
$$

Let us compose this map with the projection onto the first $c$ direct summands
of the direct sum. According to the definition of a standard smooth
algebra the classes $f_i \bmod (f_1, \ldots, f_c)^2$ map to a basis of
$\bigoplus_{i = 1}^c S\text{d}x_i$. We conclude that
$(f_1, \ldots, f_c)/(f_1, \ldots, f_c)^2$ is free of rank $c$ with
a basis given by the elements $f_i \bmod (f_1, \ldots, f_c)^2$, and
that the homology in degree $0$, i.e., $\Omega_{S/R}$,
of the naive cotangent complex is a free $S$-module with basis the images of
$\text{d}x_{c + j}$, $j = 1, \ldots, n - c$.
In particular, this proves $R \to S$ is smooth.

For (4), represent $g$ by $h(x)$ and add a variable $z$ and the equation $hz-1$. The Jacobian block on $x_1,\ldots,x_c,z$ is block triangular, with determinant $h\det(\partial f_i/\partial x_j)$. Both factors are units in the localization, proving it standard smooth. For (6), use the same presentation over $R_f$ and the same Jacobian minor: it remains a unit, while $R_f[x]/(f_i)\cong S$ because $f$ was already a unit in $S$.

Let $\varphi : R \to R'$ be any ring map.
Set $S' = R'[x_1, \ldots, x_n]/(f_1^\varphi, \ldots, f_c^\varphi)$
where $f^\varphi$ is the polynomial obtained from $f \in R[x_1, \ldots, x_n]$
by applying $\varphi$ to all the coefficients. Then $S' \cong R' \otimes_R S$.
Moreover, the determinant of Definition [AG-CA-17, Section 4, equations (6) and (7)](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/formally-smooth-unramified-and-etale-ring-maps.html)
for $S'/R'$ is equal to $g^\varphi$. Its image in $S'$ is therefore
the image of $g$ via $R[x_1, \ldots, x_n] \to S \to S'$
and hence invertible. This proves (5).

To prove (7) it suffices to show that
every nonzero fibre $S \otimes_R \kappa(\mathfrak p)$ has dimension $n - c$
for every prime $\mathfrak p \subset R$.
By (5) it suffices to prove that any standard smooth
algebra $k[x_1, \ldots, x_n]/(f_1, \ldots, f_c)$
over a field $k$, if nonzero, has dimension $n - c$. We already
know that $k[x_1, \ldots, x_n]/(f_1, \ldots, f_c)$ is a local
complete intersection by Lemma [F.82](#algebra-lemma-smooth-over-field).
Hence, since $I/I^2$ is free of rank $c$ we see that
$k[x_1, \ldots, x_n]/(f_1, \ldots, f_c)$ has dimension
$n - c$, by Lemma [F.57](#algebra-lemma-lci) for example.
 ∎

<a id="algebra-lemma-sum-two-terms"></a>

#### Lemma F.86: sum two terms

*Adapted from the Stacks project, algebra.tex, lines 37135–37186.*

Two homotopy-equivalent two-term complexes $A_1\xrightarrow{d_A}A_0$ and $B_1\xrightarrow{d_B}B_0$ satisfy $A_1\oplus B_0\cong B_1\oplus A_0$.

**Proof.** 
Let $\varphi,\psi$ be inverse comparison maps up to homotopies $h:A_0\to A_1$, $h':B_0\to B_1$, chosen with $1-\psi\varphi=hd_A$ in degree one and $d_Ah$ in degree zero, and the analogous equations on $B$. Form the block maps

$$
U=\begin{pmatrix}\psi_1&h\\-d_B&\varphi_0\end{pmatrix},\qquad
V=\begin{pmatrix}\varphi_1&-h'\\d_A&\psi_0\end{pmatrix}.
$$

Their product $UV$ has blocks $\psi_1\varphi_1+hd_A=1$, $-\psi_1h'+h\psi_0$, $-d_B\varphi_1+\varphi_0d_A=0$, and $d_Bh'+\varphi_0\psi_0=1$. Reversing the order gives blocks $1$, $\varphi_1h-h'\varphi_0$, $d_A\psi_1-\psi_0d_B=0$, and $1$. Both products are upper triangular with identity diagonal, hence invertible by negating their off-diagonal block. A map with an invertible product on each side has a left and a right inverse, which coincide: $(UV)^{-1}U$ and $U(VU)^{-1}$ are the inverses of $V$. Thus $U$ and $V$ are isomorphisms.
 ∎

<a id="algebra-lemma-syntomic"></a>

#### Lemma F.87: syntomic

*Adapted from the Stacks project, algebra.tex, lines 38315–38381.*

Let $R \to S$ be a ring map with $R$ Noetherian.
Let $\mathfrak q \subset S$ be a prime lying over
the prime $\mathfrak p$ of $R$.
The following are equivalent:

1. There exists an element $g \in S$, $g \not \in \mathfrak q$ such that
$R \to S_g$ is syntomic.

1. There exists an element $g \in S$, $g \not \in \mathfrak q$
such that $S_g$ is a relative global complete intersection over $R$.

1. There exists an element $g \in S$, $g \not \in \mathfrak q$,
such that $R \to S_g$ is of finite presentation,
the local ring map $R_{\mathfrak p} \to S_{\mathfrak q}$ is flat, and
the local ring $S_{\mathfrak q}/\mathfrak pS_{\mathfrak q}$ is
a complete intersection ring over $\kappa(\mathfrak p)$ (see
Definition [F.3](#algebra-definition-lci-local-ring)).

**Proof.** 
The implication (1) $\Rightarrow$ (3) is Lemma [F.58](#algebra-lemma-lci-at-prime).
The implication (2) $\Rightarrow$ (1) is
Lemma [F.76](#algebra-lemma-relative-global-complete-intersection).
It remains to show that (3) implies (2).

Assume (3). After replacing $S$ by $S_g$ for some $g \in S$,
$g\not\in \mathfrak q$, we may assume $S$ is finitely presented over $R$.
Choose a presentation $S = R[x_1, \ldots, x_n]/I$. Let
$\mathfrak q' \subset R[x_1, \ldots, x_n]$ be the prime corresponding
to $\mathfrak q$. Write $\kappa(\mathfrak p) = k$.
Note that $S \otimes_R k = k[x_1, \ldots, x_n]/\overline{I}$ where
$\overline{I} \subset k[x_1, \ldots, x_n]$ is the ideal generated
by the image of $I$. Let $\overline{\mathfrak q}' \subset k[x_1, \ldots, x_n]$
be the prime ideal generated by the image of $\mathfrak q'$.
By Lemma [F.58](#algebra-lemma-lci-at-prime) the equivalent conditions of
Lemma [F.57](#algebra-lemma-lci) hold for $\overline{I}$ and $\overline{\mathfrak q}'$.
Say the dimension of
$\overline{I}_{\overline{\mathfrak q}'}/
\overline{\mathfrak q}'\overline{I}_{\overline{\mathfrak q}'}$
over $\kappa(\overline{\mathfrak q}')$ is $c$.
Pick $f_1, \ldots, f_c \in I$ mapping to a basis of this vector space.
The images $\overline{f}_j \in \overline{I}$ generate
$\overline{I}_{\overline{\mathfrak q}'}$ (by Lemma [F.57](#algebra-lemma-lci)).
Set $S' = R[x_1, \ldots, x_n]/(f_1, \ldots, f_c)$. Let $J$ be the
kernel of the surjection $S' \to S$. Since $S$ is of finite presentation
$J$ is a finitely generated ideal
(Lemma [F.28](#algebra-lemma-compose-finite-type)). Consider the short exact sequence

$$
0 \to J \to S' \to S \to 0.
$$

As $S_\mathfrak q$ is flat over $R$ we see that
$J_{\mathfrak q'} \otimes_R k \to S'_{\mathfrak q'} \otimes_R k$
is injective (Lemma [AG-CA-07, Theorem 2.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/tor-and-flat-modules.html)).
However, by construction $S'_{\mathfrak q'} \otimes_R k$
maps isomorphically to $S_\mathfrak q \otimes_R k$. Hence we
conclude that $J_{\mathfrak q'} \otimes_R k =
J_{\mathfrak q'}/\mathfrak pJ_{\mathfrak q'} = 0$. By Nakayama's
lemma (Lemma [F.10](#algebra-lemma-NAK)) we conclude that there exists a
$g \in R[x_1, \ldots, x_n]$, $g \not \in \mathfrak q'$ such that
$J_g = 0$. In other words $S'_g \cong S_g$. After further localizing
we see that $S'$ (and hence $S$) becomes a relative global complete
intersection by
Lemma [F.66](#algebra-lemma-localize-relative-complete-intersection)
as desired.
 ∎

<a id="algebra-lemma-syntomic-presentation-ideal-mod-squares"></a>

#### Lemma F.88: syntomic presentation ideal mod squares

*Adapted from the Stacks project, algebra.tex, lines 38383–38402.*

Let $R$ be Noetherian. Let $S = R[x_1, \ldots, x_n]/I$ for some
finitely generated ideal $I$. If $g \in S$ is such that
$S_g$ is syntomic over $R$, then $(I/I^2)_g$ is a finite projective
$S_g$-module.

**Proof.** 
By Lemma [F.87](#algebra-lemma-syntomic) there exist finitely many elements
$g_1, \ldots, g_m \in S$ which generate the unit ideal in $S_g$
such that each $S_{gg_j}$ is a relative global complete intersection
over $R$. Since it suffices to prove that $(I/I^2)_{gg_j}$ is
finite projective, see
Lemma [AG-CA-07, Theorem 5.3](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/tor-and-flat-modules.html),
we may assume that $S_g$ is a relative global complete intersection.
In this case the result follows from
Lemmas [F.33](#algebra-lemma-conormal-module-localize) and
[F.77](#algebra-lemma-relative-global-complete-intersection-conormal).
 ∎

<a id="algebra-lemma-total-ring-fractions-no-embedded-points"></a>

#### Lemma F.89: total ring fractions no embedded points

*Adapted from the Stacks project, algebra.tex, lines 4748–4775.*

Let $R$ be a ring.
Assume that $R$ has finitely many minimal primes
$\mathfrak q_1, \ldots, \mathfrak q_t$, and that
$\mathfrak q_1 \cup \ldots \cup \mathfrak q_t$ is the set
of zerodivisors of $R$.
Then the total ring of fractions $Q(R)$ is equal to
$R_{\mathfrak q_1} \times \ldots \times R_{\mathfrak q_t}$.

**Proof.** 
There are natural maps $Q(R) \to R_{\mathfrak q_i}$ since
any nonzerodivisor lies in $R \setminus \mathfrak q_i$.
Hence a natural map
$Q(R) \to R_{\mathfrak q_1} \times \ldots \times R_{\mathfrak q_t}$.
For any nonminimal prime $\mathfrak p \subset R$ we see that
$\mathfrak p \not \subset \mathfrak q_1 \cup \ldots \cup \mathfrak q_t$
by Lemma [F.80](#algebra-lemma-silly). Hence
$\operatorname{Spec}(Q(R)) = \{\mathfrak q_1, \ldots, \mathfrak q_t\}$
(as subsets of $\operatorname{Spec}(R)$, see Lemma [AG-CA-02, Theorem 3.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/localization-local-properties-and-support.html)).
Therefore $\operatorname{Spec}(Q(R))$ is a finite discrete set and
it follows that $Q(R) = A_1 \times \ldots \times A_t$
with $\operatorname{Spec}(A_i) = \{\mathfrak{q}_i\}$, see
Lemma [AG-CA-01, Theorem 5.2 and Corollary 5.3](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/spectra-of-rings.html).
Moreover $A_i$ is a local ring, which is a localization
of $R$. Hence $A_i \cong R_{\mathfrak q_i}$.
 ∎

<a id="algebra-lemma-when-colimit"></a>

#### Lemma F.90: when colimit

*Adapted from the Stacks project, algebra.tex, lines 33328–33357.*

Let $R\to\Lambda$ be a ring map. Then $\Lambda$ is a filtered colimit of smooth $R$-algebras if and only if every map $A\to\Lambda$, with $A$ finitely presented over $R$, factors through a smooth $R$-algebra.

**Proof.** 
For the forward direction, choose finitely many generators and relations for $A$. Representatives of all generator images lie at one stage of the filtered diagram. The finitely many relations become zero at a common later stage, giving the factorization.

Conversely, consider the category of smooth finitely presented $R$-algebras equipped with a map to $\Lambda$, with morphisms commuting with that map. It is nonempty because it contains $R$. Given two objects $B_1,B_2$, their tensor product is finitely presented; factoring its map to $\Lambda$ through a smooth algebra gives a common successor. Given parallel arrows $u,v\colon B\rightrightarrows C$, choose finite algebra generators $b_i$ of $B$ and factor the finitely presented algebra $C/(u(b_i)-v(b_i))$ through a smooth algebra. The resulting arrow out of $C$ equalizes $u,v$. Thus the category is filtered. One may choose a set of representatives of finite presentations, so size causes no difficulty.

Its colimit maps onto $\Lambda$: for $\lambda\in\Lambda$, factor $R[T]\to\Lambda$, $T\mapsto\lambda$, through a smooth algebra. For injectivity, if an element represented by $b\in B$ maps to zero, factor $B/(b)\to\Lambda$ through a smooth algebra; then $b$ is already zero at a successor. Apply this to the difference of any two representatives after moving them to a common stage. This proves the ring map from the colimit to $\Lambda$ is an isomorphism.
 ∎

<a id="algebra-proposition-characterize-separable-field-extensions"></a>

#### Proposition F.91: characterize separable field extensions

*Adapted from the Stacks project, algebra.tex, lines 46037–46069.*

For any field extension $K/k$, separability, geometric reducedness, algebraic formal smoothness, vanishing of $H_1(L_{K/k})$, and injectivity of $K\otimes_k\Omega_{k/P}\to\Omega_{K/P}$ are equivalent; here $P$ is the prime field. In characteristic $p$, separability means that a $p$-basis of $k$ remains $p$-independent over $K^p$. In characteristic zero all these conditions hold. For finitely generated extensions this agrees with having a separating transcendence basis.

**Proof.** 
Every field is formally smooth over its prime field by the full arbitrary-field proof AG-CA-19S, Lemma 1.1. Suppose the displayed differential map is injective. In a square-zero lifting test for $K/k$, first obtain a prime-field lift $u:K\to E$ by that lemma. Its restriction differs from the given map of $k$ by a derivation $D:k\to J$, where $J$ is a $K$-vector space through the map modulo $J$. The corresponding $K$-linear map $K\otimes_k\Omega_{k/P}\to J$ extends to $\Omega_{K/P}$ by choosing a basis complement. Subtract the resulting derivation from $u$. The square-zero product identity shows that this is still a ring map, and its restriction to $k$ is the prescribed one. Thus $K/k$ is formally smooth.

Conversely for any $P$-derivation $D:k\to V$, with $V$ a $K$-vector space, use the test algebra $K\oplus V$ with structural map $a\mapsto(a,D(a))$ and target quotient $K$. A lift of the identity gives a $P$-derivation of $K$ extending $D$. Hence every linear functional on $K\otimes_k\Omega_{k/P}$ extends to $\Omega_{K/P}$. If the displayed map had a nonzero kernel vector, a linear functional nonzero on that vector could not extend. It is therefore injective. The conormal/vector-space argument in the preceding formal-field lemma equates formal smoothness with the $H_1$ condition.

In characteristic zero choose a transcendence basis of $k/P$ and extend it to one of $K/P$. Algebraic extensions in characteristic zero are separable. The polynomial and separable algebraic differential formulas AG-CA-16, Theorem 6.2, identify their absolute differentials with the free spaces on those bases, proving the indicated injection. The same formula for arbitrary algebraic unions follows because each finite polynomial expression and relation occurs in a finite subextension. The lifting proof in the first paragraph consequently applies.

In characteristic $p$, the absolute differential computation in the preceding $p$-root degree proof says that a $p$-basis $B$ of $k$ has independent images of its differentials in $K$ precisely when it is $p$-independent over $K^p$. To verify this assertion directly, extend any maximal independent subset to a $p$-basis of $K$; its partial derivations detect linear independence. If a finite subset is $p$-dependent, take a minimal monomial relation over $K^p$ and differentiate it; a minimal relation has a nonzero partial derivative because its exponents are below $p$, giving differential dependence. This proves the equivalence with the stated separability condition.

That condition is equivalent to $K\otimes_k k^{1/p}$ being reduced. For a finite subset of $B$ the tensor product is $K[T_b]/(T_b^p-b)$, free on the standard monomials. It is a field exactly when those roots have degree $p^{\#B_0}$, which is exactly the indicated monomial independence. If the degree is smaller, its map to the field generated by the roots has a nonzero kernel; every element of that kernel has zero $p$th power, so it is not reduced. The whole tensor product is the directed union of these rings; these inclusions are injective by their monomial bases. Reducedness is therefore equivalent to independence of all finite subsets.

The independence persists at every root height. Indeed, a relation $\sum_a c_a^{p^r}B^a=0$ with $0\le a_b<p^r$ can be grouped by $a=pu+v$. Independence of the monomials $B^v$, $0\le v_b<p$, over $K^p$ makes each grouped coefficient, a $p$th power, zero. Taking its unique $p$th root and induction on $r$ makes every coefficient zero. Iterating the $p$-basis expansion proves that these are the bases for adjoining all $p^r$th roots of $k$. Consequently tensoring $K$ with any finite purely inseparable extension of $k$ gives a field: it injects into the corresponding full-root tensor field and is finite-dimensional over $K$.

For any finitely generated extension $E/k$, the explicit separabilization construction proved below provides finite purely inseparable $k'/k$, $E'/E$, with $E'/k'$ separably generated. Set $F=K\otimes_k k'$, a field by the last paragraph. Write $E'$ as a finite separable tower over $k'(T)$. Tensoring with $F$ gives a localization of a polynomial algebra over $F$, followed by finite étale algebras. These are regular by regularity ascent through flat maps with regular fibres, proved above, hence reduced. Thus $K\otimes_k E'=(K\otimes_k k')\otimes_{k'}E'$ is reduced. The map $K\otimes_kE\to K\otimes_kE'$ is faithfully flat, in particular injective, so the former is reduced. An arbitrary field extension is the directed union of its finitely generated subfields; all the corresponding tensor maps are injective, and a nilpotent element lies at one stage. This proves geometric reducedness for every field extension. Its converse follows by testing $k^{1/p}$.

Finally a finitely generated separable field is the fraction field of a smooth finite-type domain: choose any finite algebra model. In its polynomial local presentation at the generic point, formal smoothness splits the conormal differential; choose a conormal basis, lift it to the finite kernel, and use Nakayama to make these lifts generate the ideal locally. Their independent differential rows give a nonzero Jacobian minor. Clear the finitely many denominators for ideal generation and this minor, obtaining a principal standard smooth model by AG-CA-17, Theorem 4.1. The nonpivot-coordinate argument in the preceding lemma gives a separating transcendence basis. Conversely the polynomial and finite separable tower proves formal smoothness of a separably generated field. This completes all comparisons without imposing finite generation on the initial $K/k$.
 ∎

<a id="more-algebra-definition-G-ring"></a>

#### Definition F.92: G ring

*Adapted from the Stacks project, more-algebra.tex, lines 12788–12793.*

A ring $R$ is called a *G-ring* if $R$ is Noetherian and for every
prime $\mathfrak p$ of $R$ the ring map
$R_\mathfrak p \to (R_\mathfrak p)^\wedge$ is regular.

<a id="more-algebra-definition-excellent"></a>

#### Definition F.93: excellent

*Adapted from the Stacks project, more-algebra.tex, lines 13961–13970.*

Let $R$ be a ring.

1. We say $R$ is *quasi-excellent* if $R$ is Noetherian,
a G-ring, and J-2.

1. We say $R$ is *excellent* if $R$ is quasi-excellent
and universally catenary.

<a id="more-algebra-definition-local-complete-intersection"></a>

#### Definition F.94: local complete intersection

*Adapted from the Stacks project, more-algebra.tex, lines 8947–8952.*

A ring map $A \to B$ is called a *local complete intersection*
if it is of finite type and for some (equivalently any) presentation
$B = A[x_1, \ldots, x_n]/I$ the ideal $I$ is Koszul-regular.

<a id="more-algebra-definition-regular-ideal"></a>

#### Definition F.95: regular ideal

*Adapted from the Stacks project, more-algebra.tex, lines 8710–8731.*

Let $R$ be a ring and let $I \subset R$ be an ideal.

1. We say $I$ is a *regular ideal* if for every
$\mathfrak p \in V(I)$ there exists a $g \in R$, $g \not \in \mathfrak p$
and a regular sequence $f_1, \ldots, f_r \in R_g$ such that $I_g$
is generated by $f_1, \ldots, f_r$.

1. We say $I$ is a *Koszul-regular ideal* if for every
$\mathfrak p \in V(I)$ there exists a $g \in R$, $g \not \in \mathfrak p$
and a Koszul-regular sequence $f_1, \ldots, f_r \in R_g$ such that $I_g$
is generated by $f_1, \ldots, f_r$.

1. We say $I$ is a *$H_1$-regular ideal* if for every
$\mathfrak p \in V(I)$ there exists a $g \in R$, $g \not \in \mathfrak p$
and an $H_1$-regular sequence $f_1, \ldots, f_r \in R_g$ such that $I_g$
is generated by $f_1, \ldots, f_r$.

1. We say $I$ is a *quasi-regular ideal* if for every
$\mathfrak p \in V(I)$ there exists a $g \in R$, $g \not \in \mathfrak p$
and a quasi-regular sequence $f_1, \ldots, f_r \in R_g$ such that $I_g$
is generated by $f_1, \ldots, f_r$.

<a id="more-algebra-lemma-G-ring-goes-up-quasi-finite"></a>

#### Lemma F.96: G ring goes up quasi finite

*Adapted from the Stacks project, more-algebra.tex, lines 12823–12870.*

Let $R \to R'$ be a finite type map of Noetherian rings and let

$$
\begin{gathered}
\mathfrak q' \xrightarrow{} \mathfrak p' \\
\mathfrak p' \xrightarrow{} R' \\
\mathfrak q \xrightarrow{} \mathfrak p \\
\mathfrak q \xrightarrow{} \mathfrak q' \\
\mathfrak p \xrightarrow{} R \\
\mathfrak p \xrightarrow{} \mathfrak p' \\
R \xrightarrow{} R'
\end{gathered}
$$

be primes. Assume $R \to R'$ is quasi-finite at $\mathfrak p'$.

1. If the formal fibre $R_\mathfrak p^\wedge \otimes_R \kappa(\mathfrak q)$
is geometrically regular over $\kappa(\mathfrak q)$, then the formal fibre
$(R'_{\mathfrak p'})^\wedge \otimes_{R'} \kappa(\mathfrak q')$
is geometrically regular over $\kappa(\mathfrak q')$.

1. If the formal fibres of $R_\mathfrak p$ are geometrically regular,
then the formal fibres of $R'_{\mathfrak p'}$ are geometrically regular.

1. If $R \to R'$ is quasi-finite and $R$ is a G-ring, then $R'$ is
a G-ring.

**Proof.** 
It is clear that (1) $\Rightarrow$ (2) $\Rightarrow$ (3).
Assume $R_\mathfrak p^\wedge \otimes_R \kappa(\mathfrak q)$
is geometrically regular over $\kappa(\mathfrak q)$.
By Algebra, Lemma [F.26](#algebra-lemma-completion-at-quasi-finite-prime)
we see that

$$
R_\mathfrak p^\wedge \otimes_R R'
=
(R'_{\mathfrak p'})^\wedge \times B
$$

for some $R_\mathfrak p^\wedge$-algebra $B$. Hence
$R'_{\mathfrak p'} \to (R'_{\mathfrak p'})^\wedge$ is a factor of
a base change of the map $R_\mathfrak p \to R_\mathfrak p^\wedge$.
It follows that $(R'_{\mathfrak p'})^\wedge \otimes_{R'} \kappa(\mathfrak q')$
is a factor of

$$
R_\mathfrak p^\wedge \otimes_R R' \otimes_{R'} \kappa(\mathfrak q') =
R_\mathfrak p^\wedge \otimes_R \kappa(\mathfrak q)
\otimes_{\kappa(\mathfrak q)} \kappa(\mathfrak q').
$$

Thus the result follows as extension of base field preserves
geometric regularity, see
Algebra, Lemma [F.50](#algebra-lemma-geometrically-regular).
 ∎

<a id="more-algebra-lemma-another-helper-G-ring"></a>

#### Lemma F.97: another helper G ring

*Adapted from the Stacks project, more-algebra.tex, lines 13103–13159.*

Let $R$ be any Noetherian complete local domain with fraction field $K$. First, for a prime $q$ of $R[X]$, $\widehat{R[X]_q}\otimes_RK$ is regular. If $q$ lies over the maximal ideal and $0\ne r\subset q$ lies over $(0)\subset R$, then $\widehat{R[X]_q}\otimes_{R[X]}\kappa(r)$ is geometrically regular over $\kappa(r)$.

**Proof.** 
Choose the already proved finite regular complete local subring $A_0\subset R$, and put $F=\operatorname{Frac}(A_0)$. Let $q_0$ contract $q$ to $A_0[X]$. The finite-extension completion decomposition gives
$$\widehat{A_0[X]_{q_0}}\otimes_{A_0[X]}R[X]=\prod_i\widehat{R[X]_{q_i}},$$
with the finitely many primes over $q_0$, one of which is $q$. Tensor with $K$ over $R$. The left side becomes $\widehat{A_0[X]_{q_0}}\otimes_{A_0}K$: the finite domain $R$ over $A_0$ has $R\otimes_{A_0}F=K$, since a finite domain over a field is a field. The strong first assertion of the preceding helper makes $\widehat{A_0[X]_{q_0}}\otimes_{A_0}F$ geometrically regular over $F$. Its base change to the finite extension $K/F$ is regular by the field-extension proof. Each factor, including $\widehat{R[X]_q}\otimes_RK$, is regular. This proves the first assertion without any use of a general formal-smoothness/regularity equivalence.

For the second, $\kappa(r)/K$ is finite, because the nonzero prime $rK[X]$ is generated by an irreducible polynomial. Given a finite purely inseparable $L/\kappa(r)$, choose a finite integral $R$-subalgebra $B\subset L$ with fraction field $L$, by scaling finitely many algebraic generators into monic equations. It is complete by finite-module completion. It is local: a finite algebra over the complete henselian local ring decomposes into local factors by AG-CA-20, Theorem 2.2; this domain has no nontrivial idempotent and hence only one factor. Let $r'$ be the kernel of $B[X]\to L$ sending $X$ to its specified image from $\kappa(r)$; then $\kappa(r')=L=\operatorname{Frac}(B)$.

Finite-extension completion and tensor associativity identify the tested fibre with a product of
$$\widehat{B[X]_{q_i}}\otimes_{B[X]}\kappa(r'),$$
over primes $q_i$ above $q$; factors not meeting this fibre are zero. In each remaining factor, $r'L[X]=(X-a)$ for some $a\in L$, so this is
$$\big(\widehat{B[X]_{q_i}}\otimes_B L\big)/(X-a).$$
The parenthesized ring is regular by the first assertion, applied to the complete local domain $B$. The derivation $\partial/\partial X$ of $B[X]$ extends to its prime localization, completion and localization to $L$, kills $B$ and sends $X-a$ to one. The checked hypersurface quotient argument makes each factor regular. Thus every finite purely inseparable test extension $L$ gives a regular fibre, and the geometric-regularity criterion gives the assertion. This is the exact completion argument consumed by polynomial permanence of G-rings.
 ∎

<a id="more-algebra-lemma-cartier-equality"></a>

#### Lemma F.98: cartier equality

*Adapted from the Stacks project, more-algebra.tex, lines 9182–9206.*

For a finitely generated field extension $K/k$, both $\Omega_{K/k}$ and $H_1(L_{K/k})$ are finite-dimensional and their dimension difference is $\operatorname{trdeg}_kK$.

**Proof.** 
Use the explicit finite global complete-intersection domain $C\subset K$ constructed in the monic-tower proof, with fraction field $K$. Write its polynomial presentation with $n$ variables and $c$ regular equations; the localization variable has already been counted, so $\dim C=n-c$. Its conormal module is free on the equation classes by the regular-relation calculation, and polynomial differentials are free on the variables. Localization and homotopy comparison give the two-term complex $K^c\to K^n$ for $K/k$. If the matrix rank is $r$, its homology dimensions are $c-r$ and $n-r$, respectively. Their difference is $n-c=\dim C=\operatorname{trdeg}_kK$, by AG-CA-09, Theorem 4.2. This also proves their finiteness.
 ∎

<a id="more-algebra-lemma-check-G-ring-easy"></a>

#### Lemma F.99: check G ring easy

*Adapted from the Stacks project, more-algebra.tex, lines 12803–12821.*

A Noetherian ring $R$ is a G-ring if and only if for every $\mathfrak q\subset\mathfrak p$ the ring $(R/\mathfrak q)_{\mathfrak p}^{\wedge}\otimes_{R/\mathfrak q}\kappa(\mathfrak q)$ is geometrically regular over $\kappa(\mathfrak q)$.

**Proof.** 
The completion map of each Noetherian local ring is flat by AG-CA-19, Theorem 3.2. Its fibre at a contracted prime $\mathfrak q$ is $\widehat{R_{\mathfrak p}}\otimes_R\kappa(\mathfrak q)$. Exactness of finite-module completion, AG-CA-19, Theorem 3.1, gives $\widehat{R_{\mathfrak p}}/\mathfrak q\widehat{R_{\mathfrak p}}=\widehat{(R/\mathfrak q)_{\mathfrak p}}$. Tensoring this equality with the fraction field of $R/\mathfrak q$ identifies the displayed fibre with the ring in the assertion. A flat map is regular precisely when all its residue-field fibres are geometrically regular, by the stated definition. Applying this to every local completion gives both directions.
 ∎

<a id="completion-flat-local-map"></a>

#### Lemma F.99A: completion of a flat local map

Let $(A,\mathfrak m)\to(B,\mathfrak n)$ be a flat local map of
Noetherian local rings. Its induced map on maximal-ideal completions
$\widehat A\to\widehat B$ is faithfully flat. The residue fields need
not be equal.

**Proof.** A local map sends $\mathfrak m^r$ into $\mathfrak n^r$;
passing to compatible finite quotients therefore defines the map of
completions. It remains local because their maximal ideals are
$\mathfrak m\widehat A$ and $\mathfrak n\widehat B$, and their residue
fields are $A/\mathfrak m$ and $B/\mathfrak n$, respectively. These
quotient and Noetherian assertions are AG-CA-19, Proposition 2.2 and
Theorem 3.3.

Put $\kappa=A/\mathfrak m$. Choose a free $A$-resolution
$F_\bullet\to\kappa$, as constructed in [AG-CA-06S, Section 1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/resolutions-tor-and-ext.html).
Completion is flat by AG-CA-19, Theorem 3.2, so
$F_\bullet\otimes_A\widehat A$ is a free $\widehat A$-resolution of
$\kappa\otimes_A\widehat A=\kappa$. The ring $\widehat B$ is flat
over $B$ by the same theorem and hence flat over $A$ by composition.
Consequently

$$
\operatorname{Tor}^{\widehat A}_1(\kappa,\widehat B)
=H_1(F_\bullet\otimes_A\widehat B)
=\operatorname{Tor}^{A}_1(\kappa,\widehat B)=0.
$$

Apply the proved local criterion for flatness, AG-CA-08, Theorem 4.2,
to the Noetherian local map $\widehat A\to\widehat B$ and the finite
$\widehat B$-module $\widehat B$. It proves flatness. A flat local map
is faithfully flat by AG-CA-08, Theorem 2.1: its closed fibre is the
nonzero residue-field extension, and the local faithful-flatness
criterion applies. This proves the assertion. ∎

<a id="more-algebra-lemma-check-G-ring-maximal-ideals"></a>

#### Lemma F.100: check G ring maximal ideals

*Adapted from the Stacks project, more-algebra.tex, lines 13001–13037.*

Let $R$ be a Noetherian ring. Then $R$ is a G-ring if and only if
$R_\mathfrak m$ has geometrically regular formal fibres for every
maximal ideal $\mathfrak m$ of $R$.

**Proof.** 
Assume $R_\mathfrak m \to R_\mathfrak m^\wedge$ is regular for every
maximal ideal $\mathfrak m$ of $R$. Let $\mathfrak p$ be a prime of
$R$ and choose a maximal ideal $\mathfrak p \subset \mathfrak m$.
Since $R_\mathfrak m \to R_\mathfrak m^\wedge$ is faithfully flat
we can choose a prime $\mathfrak p'$ in $R_\mathfrak m^\wedge$
lying over $\mathfrak pR_\mathfrak m$. Consider the commutative diagram

$$
\begin{gathered}
R_\mathfrak m^\wedge \xrightarrow{} (R_\mathfrak m^\wedge)_{\mathfrak p'} \\
(R_\mathfrak m^\wedge)_{\mathfrak p'} \xrightarrow{} (R_\mathfrak m^\wedge)_{\mathfrak p'}^\wedge \\
R_\mathfrak m \xrightarrow{} R_\mathfrak m^\wedge \\
R_\mathfrak m \xrightarrow{} R_\mathfrak p \\
R_\mathfrak p \xrightarrow{} (R_\mathfrak m^\wedge)_{\mathfrak p'} \\
R_\mathfrak p \xrightarrow{} R_\mathfrak p^\wedge \\
R_\mathfrak p^\wedge \xrightarrow{} (R_\mathfrak m^\wedge)_{\mathfrak p'}^\wedge
\end{gathered}
$$

By assumption the ring map $R_\mathfrak m \to R_\mathfrak m^\wedge$ is
regular. By Proposition [F.132](#more-algebra-proposition-Noetherian-complete-G-ring)
$(R_\mathfrak m^\wedge)_{\mathfrak p'} \to
(R_\mathfrak m^\wedge)_{\mathfrak p'}^\wedge$ is regular.
The localization
$R_\mathfrak m^\wedge \to (R_\mathfrak m^\wedge)_{\mathfrak p'}$ is regular.
Hence $R_\mathfrak m \to (R_\mathfrak m^\wedge)_{\mathfrak p'}^\wedge$
is regular by Lemma [F.124](#more-algebra-lemma-regular-composition).
Since it factors through the localization $R_\mathfrak p$, also the ring map
$R_\mathfrak p \to (R_\mathfrak m^\wedge)_{\mathfrak p'}^\wedge$
is regular. The local map
$R_\mathfrak p\to(R_\mathfrak m^\wedge)_{\mathfrak p'}$ is flat,
being a localization of the flat completion map. Lemma
[F.99A](#completion-flat-local-map) makes the induced map
$R_\mathfrak p^\wedge\to
(R_\mathfrak m^\wedge)_{\mathfrak p'}^\wedge$ faithfully flat.
Thus Lemma [F.125](#more-algebra-lemma-regular-permanence) applies to
this actual factorization and proves that
$R_\mathfrak p\to R_\mathfrak p^\wedge$ is regular.
 ∎

<a id="more-algebra-lemma-conormal-sequence-H1-regular-ideal"></a>

#### Lemma F.101: conormal sequence H1 regular ideal

*Adapted from the Stacks project, more-algebra.tex, lines 8844–8854.*

If $I\subset J$ and $J/I$ is an $H_1$-regular ideal in $A/I$, then $I\cap J^2=IJ$.

**Proof.** 
This equality of modules is local. Away from $V(J)$ it reads $I=I$, so localize at a prime containing $J$. Choose lifts $g_i\in J$ of local generators whose Koszul first homology over $A/I$ vanishes. For $x\in I\cap J^2$, write $x=\sum_i g_i b_i+u$ with $b_i\in J$, $u\in IJ$; this follows by expanding $J=I+(g_i)$ and grouping products. Modulo $I$, the vector $(b_i)$ is a relation on the $(g_i)$. Vanishing of $H_1$ says that it is a finite sum of the skew Koszul relations. Lift their coefficients to $A$ and subtract those relations from $(b_i)$. Their scalar products with the $g_i$ are zero identically, while the corrected coefficients all lie in $I$. Hence $\sum_i g_i b_i\in IJ$ and $x\in IJ$. The opposite inclusion is immediate. Local detection proves the global identity.
 ∎

<a id="more-algebra-lemma-cotangent-complex-symmetric-algebra"></a>

#### Lemma F.102: cotangent complex symmetric algebra

*Adapted from the Stacks project, more-algebra.tex, lines 2066–2109.*

Let $A$ be a ring and let
$0\to K\to A^{\oplus m}\to M\to0$ be exact, with $M$ a finite
projective $A$-module. Put $C=\operatorname{Sym}_A(M)$ and let
$\alpha:A[y_1,\ldots,y_m]\to C$ be its induced presentation, with
kernel $J$. Then the natural map

$$
K\otimes_A C\longrightarrow J/J^2,
\qquad
(k_1,\ldots,k_m)\otimes c\longmapsto
c\sum_i k_iy_i\bmod J^2,
$$

is an isomorphism. Under it the two-term conormal complex is

$$
\operatorname{NL}(\alpha)=
[K\otimes_A C\longrightarrow C^{\oplus m}],
$$

with differential the tensor of $K\hookrightarrow A^{\oplus m}$.
It follows that $\Omega_{C/A}=M\otimes_A C$.

**Proof.**
Projectivity of $M$ splits the defining exact sequence and makes $K$
a finite projective module too. At each prime of $A$, localize further
on a principal neighborhood on which both summands are free; their
two bases combine to a basis of $A^{\oplus m}$. Its invertible linear
change of variables changes the polynomial presentation into

$$
A[U_1,\ldots,U_r,V_1,\ldots,V_s]\longrightarrow
A[V_1,\ldots,V_s],
\qquad U_i\longmapsto0,\quad V_j\longmapsto V_j.
$$

Here the coefficients denote the localized ring. Its kernel is
$(U_1,\ldots,U_r)$. In the polynomial monomial basis its square
consists of monomials containing at least two $U$ factors, so its
conormal module is free over $A[V]$ on the classes of the $U_i$.
The displayed natural map is exactly the identity on these bases.
It is therefore an isomorphism at every prime; local detection of
the kernel and cokernel proves the global assertion. The derivative
of $\sum k_iy_i$ relative to $A$ is $\sum k_i\,dy_i$, proving the
claimed differential and its cokernel. The finite-projective quotient
hypothesis is essential for this conormal identity. ∎

<a id="more-algebra-lemma-degree-p-extension-regular"></a>

#### Lemma F.103: degree p extension regular

*Adapted from the Stacks project, more-algebra.tex, lines 12453–12467.*

If $R$ is Noetherian regular and $D(f)$ is a unit for some derivation, then $R[Z]/(P(Z)-f)$ is regular for every $P\in\mathbb Z[Z]$.

**Proof.** 
Polynomial extension of a Noetherian regular ring is regular by AG-CA-14, Proposition 3.3. Extend the derivation coefficientwise and set $D(Z)=0$. Every integer and hence $P(Z)$ is annihilated. The derivative of $P(Z)-f$ is $-D(f)$, still a unit in the quotient, so the preceding hypersurface proof applies at every prime. The special case $P(Z)=Z^p$ is the one used in the inseparable induction.
 ∎

<a id="more-algebra-lemma-derivation-extends"></a>

#### Lemma F.104: derivation extends

*Adapted from the Stacks project, more-algebra.tex, lines 12363–12405.*

A derivation $D:R\to R$ extends to every localization and canonically to every ideal-adic completion. If $R\subset R'$ is finite type and $R_g=R'_g$ with $g$ a nonzerodivisor in $R'$, some $g^ND$ preserves $R'$.

**Proof.** 
In a localization the forced formula is $D(r/s)=D(r)/s-rD(s)/s^2$. If $r/s=r'/s'$, a multiplier kills $rs'-r's$; differentiating this equality and using the original equality after localization proves equality of the two displayed values. Direct expansion verifies addition and the product rule; differentiating $s(s^{-1})=1$ proves uniqueness.

For completion, Leibniz gives $D(I^{n+1})\subset I^n$. For a compatible family $a_n\in R/I^n$, choose a representative of $a_{n+1}$ and define the $n$th coordinate of $\widehat D(a)$ by its derivative modulo $I^n$. It is independent of that representative and compatible as $n$ varies. Represent two families modulo $I^{n+1}$; the product rule there reduces modulo $I^n$ to the product rule for the new coordinate. Addition is checked in the same way. Every coordinate therefore satisfies the derivation identities, so their inverse limit does too. This fills the completion verification.

For finite type choose generators $x_i$ of $R'/R$ and $n$ with $g^nx_i\in R$. Inside $R'_g$,
$$g^{n+1}D(x_i)=-ng^nx_iD(g)+gD(g^nx_i)\in R'.$$
Because $R'$ injects into $R'_g$, the extended derivation $g^{n+1}D$ can be restricted to $R'$: it preserves the coefficient subring and the generators, and the product rule shows that it preserves every polynomial in them. All relations continue to hold in this subring. This proves the assertion.
 ∎

<a id="more-algebra-lemma-find-D"></a>

#### Lemma F.105: find D

*Adapted from the Stacks project, more-algebra.tex, lines 12469–12520.*

If a characteristic-$p$ domain $B$ is finite type over a Noetherian complete local ring and $f\in B$ is not a $p$th power in its fraction field, there exists a derivation $D:B\to B$ with $D(f)\ne0$.

**Proof.** 
Replace the complete base by its image in $B$. It is its quotient by a prime, hence again a complete Noetherian local domain by exact completion AG-CA-19, Theorem 3.1. The finite-over-regular-subring construction already proved above reduces it to a finite extension of $R=k[[X_1,\ldots,X_n]]$. Thus $B$ is finite type over $R$.

Apply Noether normalization AG-CA-09, Corollary 3.2, to $B\otimes_R\operatorname{Frac}(R)$, a finite-type domain over that field. Clearing finitely many denominators gives algebraically independent $y_j\in B$ and a nonzero $g\in R$ such that $B_g$ is finite over $R_g[y]$. Here scaling normalized parameters clears their denominators without losing algebraic independence. For each finite generator $b_i$ of $B/R[y]$, take its monic integral equation over $R_g[y]$. For one sufficiently large $N$, the generator $g^Nb_i$ satisfies a monic equation over $R[y]$, because multiplying the coefficient of its degree-$j$ term by $g^{N(d-j)}$ clears that coefficient's denominator. The subalgebra $B'$ generated by these scaled generators is finite over $R[y]$, by reducing monomials with those monic equations, and $B'_g=B_g$.

For a sufficiently large $r$, $f'=g^{pr}f$ belongs to $B'$. It is still not a $p$th power in its fraction field, since the multiplier is a $p$th power. Set $L=\operatorname{Frac}(B')$ and $K=\operatorname{Frac}(R[y])$. By the power-series-subfield lemma the finite coefficient subrings $A_J$ have fraction fields $K_J$ intersecting in $K^p$. By the finite-extension intersection lemma, $\bigcap_JL^pK_J=L^p$. Therefore some $J$ has $f'\notin L^pK_J$. The relative $p$-basis construction extends $f'$ to a $p$-basis of $L/K_J$, and its partial derivation gives a $K_J$-derivation $\delta:L\to L$ with $\delta(f')=1$.

Since $B'$ is finite over $R[y]$ and that ring is finite over $A_J$, it has finitely many $A_J$-module generators $b_1,\ldots,b_t$. Write $\delta(b_i)$ as fractions of $B'$ and multiply $\delta$ by their nonzero denominator product $h$. Then $h\delta(B')\subset B'$: differentiate each finite module expression and use that $\delta$ kills $A_J$. Its value on $f'$ is $h\ne0$. The finite-type derivation-extension proof above now supplies a power $g^s$ for which $D=g^sh\delta$ preserves $B$. The fraction formula gives $D(f)=g^{s-pr}h\delta(f')=g^{s-pr}h\ne0$ in its fraction field, hence in $B$. This proves the required derivation without assuming $k$ perfect or using characteristic zero differentiation.
 ∎

<a id="more-algebra-lemma-formally-smooth"></a>

#### Lemma F.106: formally smooth

*Adapted from the Stacks project, more-algebra.tex, lines 9774–9820.*

Algebraic formal smoothness implies formal smoothness for any continuous map with a pre-adic target topology. For an adic target, changing a continuous adic topology on the base to the discrete topology does not change formal smoothness.

**Proof.** 
In a lifting test with square-zero kernel $J$, continuity of the target map modulo $J$ says some ideal power $\mathfrak n^r$ maps to zero. Every algebraic lift sends $\mathfrak n^r$ into $J$, hence sends $\mathfrak n^{2r}$ to zero; it is continuous. Conversely in a test with discrete base, continuity of the original structural map supplies $\varphi(\mathfrak m^s)\subset\mathfrak n$. Since $\mathfrak n^r$ is killed modulo $J$, the given base map sends $\mathfrak m^{sr}$ into $J$ and consequently kills $\mathfrak m^{2sr}$. It was therefore continuous for the original adic base topology. Applying that version of the lifting property gives exactly the desired lift. These two arguments prove both implications without any finiteness or Noetherian assumption.
 ∎

<a id="more-algebra-lemma-formally-smooth-completion"></a>

#### Lemma F.107: formally smooth completion

*Adapted from the Stacks project, more-algebra.tex, lines 9833–9860.*

For continuous maps between Noetherian rings with finitely generated adic ideals, formal smoothness in the target adic topology is unchanged by completing the target or both rings.

**Proof.** 
AG-CA-19, Proposition 2.2, identifies each finite quotient of a completion with the original quotient: $\widehat R/I^n\widehat R=R/I^n$, and likewise for the target. A continuous map from either ring to a discrete test algebra kills an ideal power, hence factors through one of these common finite quotients. Thus maps from $R$ and $\widehat R$ correspond uniquely, as do maps from the target and its completion. The same is true for each map to the quotient test algebra. The square-zero lifting diagrams and their continuous dotted lifts are consequently in bijection. Existence of a lift in one version is existence in the other. This is the Noetherian version actually used below.
 ∎

<a id="more-algebra-lemma-gamma-commutative-diagram"></a>

#### Lemma F.108: gamma commutative diagram

*Adapted from the Stacks project, more-algebra.tex, lines 9230–9281.*

For a commutative field square $k\to k'$, $k\to K$, $k'\to K'$, $K\to K'$ with $k'/k$ and $K'/K$ finitely generated, let $\alpha:\Omega_{K/k}\otimes_KK'\to\Omega_{K'/k'}$ and $\beta:H_1(L_{K/k})\otimes_KK'\to H_1(L_{K'/k'})$. Their kernels and cokernels are finite-dimensional and $\dim\ker\alpha-\dim\operatorname{coker}\alpha-\dim\ker\beta+\dim\operatorname{coker}\beta=\operatorname{trdeg}_k k'-\operatorname{trdeg}_KK'$.

**Proof.** 
Write the two Jacobi–Zariski sequences, now proved with their left zeros, for $k\subset k'\subset K'$ and $k\subset K\subset K'$. Denote their common first middle space by $V=H_1(L_{K'/k})$ and common last middle space by $U=\Omega_{K'/k}$. Their respective first injected spaces are $P_1=H_1(L_{k'/k})\otimes K'$ and $P_2=H_1(L_{K/k})\otimes K'$. Their next spaces are $W_1=H_1(L_{K'/k'})$ and $W_2=H_1(L_{K'/K})$. The next spaces are $Q_1=\Omega_{k'/k}\otimes K'$ and $Q_2=\Omega_{K/k}\otimes K'$, and the last spaces are $Z_1=\Omega_{K'/k'}$ and $Z_2=\Omega_{K'/K}$. Thus both rows have the form $0\to P_i\to V\to W_i\to Q_i\to U\to Z_i\to0$. The maps in the question are $P_2\to V\to W_1$ and $Q_2\to U\to Z_1$, by their polynomial functorial construction.

Here is the finite-dimensional bookkeeping even when $V,U,P_2,Q_2$ are infinite. Put $I=P_1\cap P_2$, $Y=V/(P_1+P_2)$, $A_i=\ker(Q_i\to U)$, and $B_i=\operatorname{im}(Q_i\to U)$. Set $i=\dim I$, $r=\dim(P_1/I)$, $y=\dim Y$, $a_i=\dim A_i$, $j=\dim(B_1\cap B_2)$, $s=\dim(B_1/(B_1\cap B_2))$, and $z=\dim(U/(B_1+B_2))$. These numbers are finite: $P_1,Q_1,W_2,Z_2$ are finite by Cartier equality, $Y$ is a quotient of $V/P_2\subset W_2$, $A_2$ a quotient of $W_2$, and $U/(B_1+B_2)$ a quotient of $Z_2$.

The kernel of $\beta$ is $I$. Its cokernel has exact sequence $0\to Y\to\operatorname{coker}\beta\to A_1\to0$, giving dimension $y+a_1$. The kernel of $\alpha$ has exact sequence $0\to A_2\to\ker\alpha\to B_1\cap B_2\to0$, giving dimension $a_2+j$; its cokernel is $U/(B_1+B_2)$, of dimension $z$. The rows also give $\dim P_1=i+r$, $\dim W_2=r+y+a_2$, $\dim Q_1=a_1+j+s$, and $\dim Z_2=s+z$. Consequently the required expression is $a_2+j-z-i+y+a_1=\dim Q_1-\dim P_1-\dim Z_2+\dim W_2$. Applying Cartier equality to $k'/k$ and $K'/K$ gives exactly the asserted transcendence-degree difference. No alternating subtraction of infinite dimensions has been used.
 ∎

<a id="more-algebra-lemma-geometrically-regular-over-field"></a>

#### Lemma F.109: geometrically regular over field

*Adapted from the Stacks project, more-algebra.tex, lines 9460–9501.*

Let $k$ be a field of characteristic $p > 0$. Let $(A, \mathfrak m, K)$
be a Noetherian local $k$-algebra. Assume $A$ is geometrically regular
over $k$. Let $K/F/k$ be a finitely generated subextension.
Let $\varphi : k[y_1, \ldots, y_m] \to A$ be a $k$-algebra map
such that $y_i$ maps to an element of $F$ in $K$ and such that
$\text{d}y_1, \ldots, \text{d}y_m$ map to a basis of $\Omega_{F/k}$.
Set $\mathfrak p = \varphi^{-1}(\mathfrak m)$. Then

$$
k[y_1, \ldots, y_m]_\mathfrak p \to A
$$

is flat and $A/\mathfrak pA$ is regular.

**Proof.** 
Set $A_0 = k[y_1, \ldots, y_m]_\mathfrak p$ with maximal ideal
$\mathfrak m_0$ and residue field $K_0$. Note that
$\Omega_{A_0/k}$ is free of rank $m$ and
$\Omega_{A_0/k} \otimes K_0 \to \Omega_{K_0/k}$ is an isomorphism.
It is clear that $A_0$ is geometrically regular over $k$. Hence
$H_1(L_{K_0/k}) \to \mathfrak m_0/\mathfrak m_0^2$ is an isomorphism, see
Proposition [F.133](#more-algebra-proposition-characterization-geometrically-regular).
Now consider

$$
\begin{gathered}
H_1(L_{K_0/k}) \otimes K \xrightarrow{} H_1(L_{K/k}) \\
H_1(L_{K_0/k}) \otimes K \xrightarrow{} \mathfrak m_0/\mathfrak m_0^2 \otimes K \\
\mathfrak m_0/\mathfrak m_0^2 \otimes K \xrightarrow{} \mathfrak m/\mathfrak m^2 \\
H_1(L_{K/k}) \xrightarrow{} \mathfrak m/\mathfrak m^2
\end{gathered}
$$

Since the left vertical arrow is injective by
Lemma [F.131](#more-algebra-lemma-transitivity-gamma)
and the lower horizontal by
Proposition [F.133](#more-algebra-proposition-characterization-geometrically-regular)
we conclude that the right vertical one is too.
Hence a regular system of parameters in $A_0$ maps to
part of a regular system of parameters in $A$.
We win by
Algebra, Lemmas [F.46](#algebra-lemma-flat-over-regular) and
[AG-CA-12, Theorem 6.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/regular-sequences-depth-and-cohen-macaulay-modules.html).
 ∎

<a id="more-algebra-lemma-helper-G-ring"></a>

#### Lemma F.110: helper G ring

*Adapted from the Stacks project, more-algebra.tex, lines 12915–12963.*

Let $A_0$ be a regular complete Noetherian local domain and $P=A_0[Y_1,\ldots,Y_m]$. For every prime $q$ of $P$, both $\widehat{P_q}\otimes_{A_0}\operatorname{Frac}(A_0)$ and $\widehat{P_q}\otimes_P\operatorname{Frac}(P)$ are geometrically regular over their indicated fields. The second assertion includes the original power-series helper; the first is the extra consumed form that removes a general formal-smoothness theorem from the completion proof.

**Proof.** 
The polynomial ring $P$ is regular by AG-CA-14, Proposition 3.3, and its localization is regular. Completion preserves the cotangent dimension and Krull dimension by AG-CA-19, Theorem 4.1, so $\widehat{P_q}$ is regular. Both displayed rings are localizations of it and therefore regular. In characteristic zero the finite purely inseparable test is trivial, so they are geometrically regular by that criterion.

In positive characteristic Cohen structure AG-CA-19S, Theorem 6.1, identifies $A_0$ with a power-series ring over its residue field: its minimal parameter list gives a surjection from that power-series ring, equality of dimensions and the nonzero-prime dimension drop AG-CA-11, Theorem 3.2, make its kernel zero. This is also the regular complete specialization already proved above. Treat either indicated fraction field $F$, and induct on a finite purely inseparable degree $[L:F]$. At a step $F\subset M\subset L$, $L=M(z)$ with $z^p=f\notin M^p$. Let $Q$ denote $A_0$ for the first assertion and $P$ for the second. Choose a finite $Q$-subalgebra $B\subset M$ with fraction field $M$ and $f\in B$. To justify this choice, scale each finite algebraic field generator so it satisfies a monic equation over $Q$, and scale $z$ by an element of $Q$ to put its $p$th power $f$ in that algebra; this does not alter its generated field. Here is the denominator step: write $f=b/d$ with nonzero $d\in B$. A monic integral equation for $d$ may be shortened by cancelling powers of $d$ until its constant coefficient $a\in Q$ is nonzero, since $B$ is a domain. That equation gives $a/d\in B$. Replacing $z$ by $az$ changes its $p$th power to $a^pf=b\,a^{p-1}(a/d)\in B$, as required. The finitely generated integral algebra is finite. Put $C=B[Z]/(Z^p-f)\subset L$; it is a finite domain with fraction field $L$.

For the first assertion use the finite extension $P\subset B[Y]$; for the second use $P\subset B$. The base $Q$ is normal: it is regular Noetherian, and AG-CA-15, Corollary 4.5, proves its normality. If $b\in B$, some $b^{p^r}$ lies in $\operatorname{Frac}(Q)$ by pure inseparability and is integral over $Q$ because $b$ is. Normality puts that power in $Q$. The same applies to $C$. These extensions therefore have every element's sufficiently high $p$th power in the smaller ring. Each prime has exactly one prime above it. Indeed membership of an element in a prime is equivalent to membership of that power in its contracted prime; lying over supplies existence. The finite-extension completion proof already written identifies the tensor of $\widehat{P_q}$ with the finite overring with the completion of its unique local factor. The same holds for $C$ (with the polynomial $Y$ variables in the first assertion). Hence the ring at the $M$ stage is a localization of this completed $B$-ring, and the ring at the $L$ stage is exactly its quotient extension $E[Z]/(Z^p-f)$. Finite-module completion commutes with this monic finite algebra by AG-CA-19, Theorem 3.1; this is the needed equality rather than an assumed equality of unrelated completions.

The induction hypothesis says $E$ is regular. The derivation lemma above applies to $B$, which is finite type over the complete local ring $A_0$ in either case, and gives $D:B\to B$ with $D(f)\ne0$. Extend it coefficientwise over the added $Y$ variables, then through the prime localization, completion and the localization to $M$, using the fully checked derivation extension formula. Its value on $f$ remains the nonzero element $D(f)$ of the field $M$, hence a unit of $E$. The hypersurface derivation proof makes $E[Z]/(Z^p-f)$ regular. This completes the induction for every finite purely inseparable extension, and the criterion gives both geometric-regularity assertions.
 ∎

<a id="more-algebra-lemma-helper-integral"></a>

#### Lemma F.111: helper integral

*Adapted from the Stacks project, more-algebra.tex, lines 1959–1975.*

For an integral map $A\to B$, if $y\in B$ becomes idempotent modulo $IB$, there is a monic annihilating polynomial $f(Y)$ with $f\bmod I=Y^d(Y-1)^d$.

**Proof.** 
Write $z=y^2-y=\sum a_ib_i$ with $a_i\in I$. The algebra generated by $y$ and these finitely many $b_i$ is a finite $A$-module $C$, since all are integral. Choose a finite module generator list including one. Multiplication by $z$ sends $C$ into $IC$, so on these generators it is represented by a matrix with entries in $I$. The adjugate identity for $z\mathbf1-M$ shows that the monic determinant polynomial $g(Z)$ annihilates each generator, including one, so $g(z)=0$. Its reduction is $Z^d$ because every matrix entry belongs to $I$. Set $f(Y)=g(Y^2-Y)$. It is monic, annihilates $y$, and reduces to $(Y^2-Y)^d=Y^d(Y-1)^d$.
 ∎

<a id="more-algebra-lemma-intersection-subfields"></a>

#### Lemma F.112: intersection subfields

*Adapted from the Stacks project, more-algebra.tex, lines 12067–12128.*

Let $K$ have characteristic $p$ and downward directed subfields $F_\lambda$ containing $K^p$ with intersection $K^p$. Then the maps $\Omega_{K/\mathbb F_p}\to\Omega_{K/F_\lambda}$ have zero common kernel. For every finite $L/K$, the fields $L^pF_\lambda$ have intersection $L^p$.

**Proof.** 
A nonzero absolute differential is a finite linear combination of differentials of distinct absolute $p$-basis elements. If it vanishes over every $F_\lambda$, those finitely many elements have dependent relative differentials, hence their monomials have a nonzero relation over every $F_\lambda$ by the preceding $p$-basis proof. Apply the finite-subspace intersection lemma to the space of all monomial coefficient relations inside $K^{p^n}$. It gives a nonzero relation over $K^p$, contradicting the absolute $p$-basis property. This proves the first assertion.

For the second, finite extensions decompose into towers of finite separable simple extensions and degree-$p$ purely inseparable simple extensions by the repeated-minimal-polynomial and separable-subfield construction given above. It suffices to treat one step and iterate: if the assertion holds for an intermediate $M$, then the fields $M^pF_\lambda$ satisfy the same three assumptions inside $M$.

For a separable simple extension $L=K(\theta)$ choose its generator in $L^p$. This is possible because $K(\theta^p)=K(\theta)$: the intervening extension is purely inseparable and also separable, so trivial. Frobenius identifies $[L^p:K^p]=[L:K]=d$. Thus both $L^p$ and each $L^pF_\lambda$ have the common basis $1,\theta,\ldots,\theta^{d-1}$ over $K^p$ and $F_\lambda$, respectively. Independence over $F_\lambda$ follows from independence over the larger field $K$. Uniqueness of coefficient expansions makes the intersection precisely the vectors with all coefficients in $K^p$, namely $L^p$.

For a degree-$p$ step $L=K(\theta)$, $\theta^p=t\notin K^p$, one has $L^p=K^p(t)$. Choose an index with $t\notin F_{\lambda_0}$; it exists by the intersection assumption. On the cofinal family of subfields refined inside $F_{\lambda_0}$, the elements $1,t,\ldots,t^{p-1}$ are independent by the same degree-$p$ argument. Thus $L^pF_\lambda=F_\lambda(t)$ has this basis. The unique expansion coefficients of an element in the intersection lie in the intersection of that cofinal family, which is $K^p$, proving it lies in $K^p(t)$. The opposite inclusion is automatic. This cofinal restriction is necessary: at other indices $t$ may already belong to $F_\lambda$, so a degree-$p$ basis cannot be assumed there.
 ∎

<a id="more-algebra-lemma-intersection-subfields-subspace"></a>

#### Lemma F.113: intersection subfields subspace

*Adapted from the Stacks project, more-algebra.tex, lines 12027–12065.*

If subfields $F_\lambda\subset K$ are downward directed and have intersection $F$, then a $K$-linear subspace $V\subset K^n$ meets every $F_\lambda^n$ nontrivially if and only if it meets $F^n$ nontrivially.

**Proof.** 
The reverse implication is immediate. Induct on $n$ for the other. If $V\cap(0\oplus F^{n-1})\ne0$, the conclusion already holds. Otherwise induction supplies some $\lambda_0$ for which $V\cap(0\oplus F_{\lambda_0}^{n-1})=0$. The nonzero intersection with $F_{\lambda_0}^n$ contains a vector with nonzero first coordinate, which can be normalized to $v=(1,v_2,\ldots,v_n)$. Subtracting the first coordinate times $v$ shows that this intersection is exactly the line $F_{\lambda_0}v$. For every refined subfield inside $F_{\lambda_0}$, the nonzero intersection similarly has a normalized vector; its uniqueness in the larger line makes it the same $v$. Thus all its coordinates belong to every refined subfield. Their intersection is $F$, because downward directedness refines $\lambda_0$ with each arbitrary index. Hence $v\in F^n$. The case $n=1$ is immediate, completing the induction.
 ∎

<a id="more-algebra-lemma-lci-local"></a>

#### Lemma F.114: lci local

*Adapted from the Stacks project, more-algebra.tex, lines 8957–8993.*

For a finitely presented algebra over a Noetherian ring, a polynomial presentation kernel is locally generated by a regular sequence if and only if this holds on a principal cover of the target.

**Proof.** 
Here is the presentation comparison, including the step that stable freeness of the conormal module alone would not prove. Suppose $P=R[X]\twoheadrightarrow S$ and $Q=R[Y]\twoheadrightarrow S$ are two finite polynomial presentations. Choose polynomials $p_j(X)$ representing the images of $Y_j$ and $q_i(Y)$ representing the images of $X_i$. In the common polynomial ring $W=R[X,Y]$ its kernel $K$ is both
$$K=(I,Y_j-p_j(X))=(J,X_i-q_i(Y)).$$
Indeed quotienting either displayed ideal eliminates the added variables and gives $S$, with exactly its stipulated generator images. At the prime of $W$ above a chosen prime of $S$, a regular generator list for $J$ remains regular after polynomial extension and localization, by flatness; appending the $X_i-q_i(Y)$ remains regular, since each successive quotient eliminates one polynomial variable. Thus $K$ has a regular generator list.

The conormal comparison proved above makes $I/I^2$ stably free over the local quotient, hence free by AG-CA-07, Theorems 5.2–5.3. Lift a basis to elements $f_i$ of $I$ in the polynomial local ring. Nakayama makes them generate $I$ there. In the common local ring the classes of the $f_i,Y_j-p_j(X)$ form a conormal basis: translation in the $Y$ variables identifies this conormal module with $(I/I^2)\oplus S^{\#Y}$. Consequently this is a minimal generator list of $K$. Any two minimal lists of generators of a finite ideal over a local ring have equal lengths and an invertible change matrix: reduce to the vector space $K/\mathfrak m_WK$, then lift the invertible residue determinant. Exterior powers of this matrix identify their Koszul complexes. The list $f_i,Y_j-p_j(X)$ therefore has zero first Koszul homology. Permute the list to put the added-variable equations first. The Noetherian first-homology criterion proved above makes this reordered list regular. Quotienting its initial added-variable equations gives the original polynomial local ring, so the remaining $f_i$ are regular there.

For a principal chart $S_g$, first present it by $P[Z]/(I,uZ-1)$, where $u$ lifts $g$. At the prime over the chosen point the same argument compares this presentation with the chart's regular presentation. Its kernel has regular minimal generators $uZ-1,f_i$, because its conormal module is $(I/I^2)_g\oplus S_g$ and the preceding invertible-matrix argument applies. Putting $uZ-1$ first and eliminating $Z$ recovers the required regular list for $I$ in $P_{\mathfrak q}$. Finally clear denominators so the finite list generates $I$ on one principal neighbourhood. Its finitely many positive Koszul homology modules are finite, so one further element outside the prime annihilates them. The same local first-homology criterion proves regularity throughout this neighbourhood. Conversely, restricting such neighbourhoods proves the chart condition.
 ∎

<a id="more-algebra-lemma-lift-factorization-monic"></a>

#### Lemma F.115: lift factorization monic

*Adapted from the Stacks project, more-algebra.tex, lines 1843–1897.*

A coprime monic factorization of a monic polynomial modulo an ideal $I$ lifts after a finitely presented étale base change $A\to A'$ inducing $A/I\cong A'/IA'$.

**Proof.** 
Write the prospective monic factors $G,H$ with respectively $d,e$ indeterminate lower coefficients and impose the $d+e$ coefficient equations $GH=f$. Their Jacobian is the linear map $(u,v)\mapsto Hu+Gv$ on polynomial spaces of degrees below $d,e$. At the stipulated residue factorization this is an isomorphism. Indeed modulo $G$, coprimality makes $H$ a unit, so $u$ is uniquely the remainder of $H^{-1}w$ modulo $G$; then $v=(w-Hu)/G$ is polynomial of degree below $e$. This gives the inverse over $A/I$ by monic division and a Bezout identity. Invert the determinant of that Jacobian in the universal coefficient algebra $C$. AG-CA-17, Theorem 4.1 and Theorem 2.2, make $C/A$ étale. The given coefficients define a section $C/IC\to A/I$.

Here is the component selection needed to make the closed fibre exactly $A/I$. For any finitely presented étale $D$-algebra $E$ with a section $\sigma:E\to D$, its kernel $J$ is finite, generated by $x_i-\sigma(x_i)$ for finite algebra generators. The section conormal calculation gives $J/J^2=\Omega_{E/D}\otimes_ED=0$, hence $J=J^2$. Choose generators $j_i$ and write $j_i=\sum m_{ij}j_j$ with $m_{ij}\in J$. The adjugate identity makes $a=\det(1-M)$ annihilate every $j_i$, and $a\equiv1\pmod J$. Put $e=1-a\in J$. Then $ej=j$ for $j\in J$, and in particular $e^2=e$. Thus $J=eE$ and $E_{1-e}=E/J=D$. Apply this to $E=C/IC$, lift $1-e$ to $h\in C$, and set $A'=C_h$. Its closed fibre is $A/I$, it is still finitely presented étale by principal localization, and its universal $G,H$ give the required lifted factorization.
 ∎

<a id="more-algebra-lemma-lift-idempotent-upstairs"></a>

#### Lemma F.116: lift idempotent upstairs

*Adapted from the Stacks project, more-algebra.tex, lines 1977–2017.*

For an integral map $A\to B$ and an idempotent $\bar e\in B/IB$, there is a finitely presented étale $A\to A'$ inducing $A/I\cong A'/IA'$ and an idempotent in $B\otimes_AA'$ lifting $\bar e$.

**Proof.** 
Choose a lift $y$. The preceding integral determinant construction gives $f(y)=0$ with $f\bmod I=Y^d(Y-1)^d$. These two monic factors are coprime: expand $(Y+(1-Y))^{2d-1}=1$, and each term is divisible by one of $Y^d,(1-Y)^d$. The monic factorization lifting proof above gives an étale base with this factorization $f=GH$, with $G\bmod I=Y^d$ and $H\bmod I=(Y-1)^d$. Replace the base by it, and put $b_1=G(y)$, $b_2=H(y)$; then $b_1b_2=0$ and their residues are $\bar e$ and $(-1)^d(1-\bar e)$.

The closed set $V(b_1,b_2)$ is disjoint from $V(IB)$. Its image in $\operatorname{Spec}A$ is closed by the integral closed-image theorem AG-CA-05, Theorem 3.4: it is $V((b_1,b_2)\cap A)$ by lying over for the quotient. The disjointness says $I+((b_1,b_2)\cap A)=A$. Choose $a\in(b_1,b_2)\cap A$ with $a\equiv1\pmod I$, and localize at $a$. This is another finitely presented étale base change with unchanged quotient modulo $I$. Now $ub_1+vb_2=1$ in $B$ for some $u,v$. The element $e=ub_1$ is idempotent because $e(1-e)=uvb_1b_2=0$. Multiplying the residue of that relation by $\bar e$ gives $\bar u\bar e=\bar e$, so $e$ reduces to $\bar e$. The tensor base change preserves integrality, so every use of the closed-image theorem remains justified. Composing the two étale base changes proves the assertion.
 ∎

<a id="more-algebra-lemma-lift-projective-module"></a>

#### Lemma F.117: lift projective module

*Adapted from the Stacks project, more-algebra.tex, lines 2019–2064.*

Let $A$ be a ring, let $I \subset A$ be an ideal.
Let $\overline{P}$ be a finite projective $A/I$-module.
Then there exists an étale ring map $A \to A'$ which induces
an isomorphism $A/I \to A'/IA'$ and a finite projective
$A'$-module $P'$ lifting $\overline{P}$.

**Proof.** 
We can choose an integer $n$ and a direct sum decomposition
$(A/I)^{\oplus n} = \overline{P} \oplus \overline{K}$
for some $R/I$-module $\overline{K}$. Choose a lift
$\varphi : A^{\oplus n} \to A^{\oplus n}$ of the projector $\overline{p}$
associated to the direct summand $\overline{P}$.
Let $f \in A[x]$ be the characteristic polynomial of $\varphi$.
Set $B = A[x]/(f)$. By Cayley-Hamilton
(Algebra, Lemma [F.19](#algebra-lemma-charpoly)) there is a map
$B \to \text{End}_A(A^{\oplus n})$ mapping $x$ to $\varphi$.
For every prime $\mathfrak p \supset I$ the image of $f$ in
$\kappa(\mathfrak p)$ is $(x - 1)^rx^{n - r}$ where $r$ is the
dimension of $\overline{P} \otimes_{A/I} \kappa(\mathfrak p)$.
Hence $(x - 1)^nx^n$ maps to zero in $B \otimes_A \kappa(\mathfrak p)$
for all $\mathfrak p \supset I$. Thus $x(1 - x)$ is contained
in every prime ideal of $B/IB$. Hence $x^N(1 - x)^N$ is
contained in $IB$ for some $N \geq 1$.
It follows that $x^N + (1 - x)^N$ is a unit in $B/IB$ and that

$$
\overline{e} = \text{image of }\frac{x^N}{x^N + (1 - x)^N}\text{ in }B/IB
$$

is an idempotent as both assertions hold in $\mathbf{Z}[x]/(x^N(x - 1)^N)$.
The image of $\overline{e}$ in $\text{End}_{A/I}((A/I)^{\oplus n})$ is

$$
\frac{\overline{p}^N}{\overline{p}^N + (1 - \overline{p})^N} = \overline{p}
$$

as $\overline{p}$ is an idempotent. After replacing $A$ by an étale
extension $A'$ as in the lemma, we may assume there exists an idempotent
$e \in B$ which maps to $\overline{e}$ in $B/IB$, see
Lemma [F.116](#more-algebra-lemma-lift-idempotent-upstairs).
Then the image of $e$ under the map

$$
B = A[x]/(f) \longrightarrow \text{End}_A(A^{\oplus n}).
$$

is an idempotent element $p$ which lifts $\overline{p}$.
Setting $P = \operatorname{im}(p)$ we win.
 ∎

<a id="more-algebra-lemma-noetherian-finite-all-equivalent"></a>

#### Lemma F.118: noetherian finite all equivalent

*Adapted from the Stacks project, more-algebra.tex, lines 8038–8063.*

For a nonzero finite module over a Noetherian local ring and a list in its maximal ideal, regularity, vanishing of all positive Koszul homology, vanishing of first Koszul homology, and the polynomial associated-graded condition are equivalent.

**Proof.** 
The Koszul complex on $f_1,\ldots,f_r$ is the exterior complex of the free module on $e_i$, with $d(e_i)=f_i$ and the alternating Leibniz rule. It is the mapping cone of multiplication by $f_r$ on the preceding Koszul complex. For a regular list, induction makes the preceding positive homology zero, and injectivity on its degree-zero quotient makes the remaining positive homology zero. The converse from $H_1=0$ uses that same cone sequence: multiplication by $f_r$ is surjective on the preceding $H_1$ and injective on its $H_0$. The preceding $H_1$ is finite, and $f_r$ belongs to the maximal ideal, so Nakayama makes it zero. Induction and the displayed injectivity give the regular list. Koszul vanishing clearly implies $H_1$ vanishing.

For regularity implying the polynomial associated-graded condition, write $J=(f_i)$. The degree-one claim is the explicit relation proof in [F.74](#algebra-lemma-regular-quasi-regular). In degree $n$ it suffices to show that $\sum_{|a|=n}m_af^a\in J^{n+1}M$ forces each $m_a\in JM$. First take the coefficient of $f_r^n$. Group the other terms by their first factor among $f_1,\ldots,f_{r-1}$. Expand the right side $J^{n+1}M$ into terms divisible by two of those first $r-1$ factors, terms divisible by $f_if_r^n$, and a term $m''f_r^{n+1}$. This gives a relation on $f_1,\ldots,f_{r-1},f_r^n$ whose last coefficient is $m_{(0,\ldots,n)}-m''f_r$. The power list is regular by AG-CA-12, Proposition 1.3, hence its relations are Koszul boundaries by the first part of this proof. Its last coefficient lies in $JM$, proving the claim for the pure last monomial.

To extract all coefficients, faithfully extend to $A[U_1,\ldots,U_r,U_r^{-1}]$, and change the basis of the Koszul free module to the list $g_i=f_i-(U_i/U_r)f_r$ for $i<r$, $g_r=f_r/U_r$. Exterior powers of that invertible matrix give an isomorphism of Koszul complexes, so this list has $H_1=0$. At primes containing $J$ it is regular by the already proved local $H_1$ criterion, and its powers are regular there; at primes not containing $J$ the Koszul complex is contractible, since a linear combination of the $g_i$ is one and wedging that vector contracts it. Consequently the powers have vanishing $H_1$ everywhere, by local detection. The pure-last-coefficient argument applies to this changed list. Rewriting $\sum m_af^a$ in the $g_i$ makes the coefficient of $g_r^n$ equal to $\sum m_aU^a$. It lies in $J(M\otimes A[U,U_r^{-1}])$. Laurent monomials are a basis over $A$, so every $m_a\in JM$. This proves the associated-graded condition in every degree.

Finally assume that condition. Krull intersection AG-CA-03, Theorem 6.1, gives every nonzero element of $M$ a finite $J$-order. Multiplication by $f_1$ raises its order exactly by one, since multiplication by $T_1$ is injective in $(M/JM)[T_i]$. Thus $f_1$ is injective. The same order argument gives $f_1M\cap J^nM=f_1J^{n-1}M$ for $n\ge1$. It follows degree by degree that the associated graded module of $M/f_1M$ is $(M/JM)[T_2,\ldots,T_r]$. Repeat with the remaining variables. The final quotient is nonzero by Nakayama. This proves regularity and closes all equivalences.
 ∎

<a id="more-algebra-lemma-p-basis"></a>

#### Lemma F.119: p basis

*Adapted from the Stacks project, more-algebra.tex, lines 11972–12025.*

For a characteristic-$p$ extension $L/F$, a subset is $p$-independent over $F$ if its monomials of exponents below $p$ are independent over $FL^p$. This is equivalent to independence of its relative differentials. Every such subset extends to a $p$-basis, whose differentials are a basis of $\Omega_{L/F}$.

**Proof.** 
A chain of independent subsets has independent union because each relation is finite. A maximal one generates $L$ over $FL^p$: if $x$ lies outside its generated field, $X^p-x^p$ has degree $p$ there and adjoining $x$ preserves independence, contradicting maximality. The degree claim follows from the proper-factor coefficient argument already given for $p$th-root polynomials. Its resulting presentation is $L=FL^p[T_b]/(T_b^p-b^p)$; hence monomial differentiation defines partial $F$-derivations. They show that the basis differentials are independent, and differentiating each monomial expansion shows that they span. Every independent subset extended this way has independent differentials. Conversely if the differentials are independent, their dual coordinate functionals give derivations sending a selected finite subset to the Kronecker delta values. Apply these to a nonzero monomial relation over $FL^p$ of least total degree. A nonconstant monomial has some exponent between one and $p-1$, so the corresponding derivative polynomial is nonzero and has smaller degree. If its evaluation were zero it would contradict minimality. But the derivation says that evaluation is zero, a contradiction. Thus no relation exists. The basis assertion follows by maximality in either equivalent formulation.
 ∎

<a id="more-algebra-lemma-power-series-ring-subfields"></a>

#### Lemma F.120: power series ring subfields

*Adapted from the Stacks project, more-algebra.tex, lines 12130–12171.*

For $A=k[[X_1,\ldots,X_n]][Y_1,\ldots,Y_m]$ in characteristic $p$, choose a $p$-basis $B$ of $k$. For each finite subset $J\subset B$, let $k_J=k^p(B\setminus J)$ and $A_J=k_J[[X_1^p,\ldots,X_n^p]][Y_1^p,\ldots,Y_m^p]$. Then $A$ is finite free over $A_J$ and the fraction fields $K_J$ are downward directed, contain $K^p$, and intersect in $K^p$.

**Proof.** 
The monomials in the finite set $J$, in the $X_i$, and in the $Y_j$, all with exponents below $p$, form a basis of $A$ over $A_J$. Group power-series terms by the $X$ exponents modulo $p$, polynomial terms by the $Y$ exponents modulo $p$, and each coefficient by the finite basis of $k/k_J$; uniqueness of each expansion proves both spanning and independence. This proves finite freeness directly, including imperfect $k$.

Every $p$th power lies in each $A_J$, hence $K^p\subset K_J$, and adjoining more excluded basis elements shrinks $K_J$, proving directedness. To compute the intersection, write $u=f/g^p$ with $f,g\in A$, $g\ne0$; every fraction admits this form by multiplying its numerator by $g^{p-1}$. If $u\in K_J$, write it as $a/b^p$ with $a\in A_J$ and nonzero $b\in A$: the inverse of any denominator $h\in A_J$ is $h^{p-1}/h^p$, so this form is available. Then $b^pf=ag^p\in A_J$. Any $A_J$-derivation of $A$ therefore kills $f$, since differentiating gives $b^pD(f)=0$ in the domain. The power-series and polynomial partial derivatives imply every nonzero exponent of $f$ in the $X,Y$ variables is divisible by $p$. The partial derivations on the excluded coefficient $p$-basis elements, extended coefficientwise to the power series, imply its coefficients lie in $k_J$: their monomial basis expansion shows that their common kernel is $k_J$. For every finite $J$ this holds, so each coefficient lies in $\bigcap_Jk_J=k^p$, again by its finite $p$-basis monomial expansion. Thus $f\in A^p$ (take coefficient roots and divide all exponents by $p$), and $u\in K^p$. This proves the intersection assertion.
 ∎

<a id="more-algebra-lemma-quasi-regular-ideal-finite-projective"></a>

#### Lemma F.121: quasi regular ideal finite projective

*Adapted from the Stacks project, more-algebra.tex, lines 8769–8778.*

Let $I \subset R$ be a quasi-regular ideal of a ring.
Then $I/I^2$ is a finite projective $R/I$-module.

**Proof.** 
This follows from Algebra, Lemma [AG-CA-07, Theorem 5.3](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/tor-and-flat-modules.html)
and the definitions.
 ∎

<a id="more-algebra-lemma-quotient-regular"></a>

#### Lemma F.122: quotient regular

*Adapted from the Stacks project, more-algebra.tex, lines 12407–12424.*

If $R$ is Noetherian regular and a derivation $D:R\to R$ sends $f$ to a unit modulo $(f)$, then $R/(f)$ is regular.

**Proof.** 
At a prime containing $f$, extend $D$ to the local ring by the fraction calculation above. If $f\in\mathfrak m^2$, Leibniz on a finite expression $f=\sum a_ib_i$, $a_i,b_i\in\mathfrak m$, gives $D(f)\in\mathfrak m$, contradicting that its class is a unit. Hence $f\notin\mathfrak m^2$. In the regular local ring its class extends to a regular parameter system, and AG-CA-14, Proposition 1.4, gives regularity of the parameter quotient. These quotients are exactly all local rings of $R/(f)$.
 ∎

<a id="more-algebra-lemma-regular-base-change"></a>

#### Lemma F.123: regular base change

*Adapted from the Stacks project, more-algebra.tex, lines 11022–11047.*

Let $R \to \Lambda$ be a regular ring map.
For any finite type ring map $R \to R'$ the base change
$R' \to \Lambda \otimes_R R'$ is regular too.

**Proof.** 
Flatness is preserved under any base change, see
Algebra, Lemma [AG-CA-07, Proposition 3.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/tor-and-flat-modules.html).
Consider a prime $\mathfrak p' \subset R'$ lying over
$\mathfrak p \subset R$. The residue field extension
$\kappa(\mathfrak p')/\kappa(\mathfrak p)$ is
finitely generated as $R'$ is of finite type over $R$.
Hence the fibre ring

$$
(\Lambda \otimes_R R') \otimes_{R'} \kappa(\mathfrak p') =
\Lambda \otimes_R \kappa(\mathfrak p) \otimes_{\kappa(\mathfrak p)} 
\kappa(\mathfrak p')
$$

is Noetherian by
Algebra, Lemma [F.12](#algebra-lemma-Noetherian-field-extension)
and the assumption on the fibre rings of $R \to \Lambda$.
Geometric regularity of the fibres is preserved by
Algebra, Lemma [F.50](#algebra-lemma-geometrically-regular).
 ∎

<a id="more-algebra-lemma-regular-composition"></a>

#### Lemma F.124: regular composition

*Adapted from the Stacks project, more-algebra.tex, lines 11049–11065.*

A composition of regular maps of Noetherian rings is regular whenever the resulting fibre rings are Noetherian. This is the form used below.

**Proof.** 
Flatness composes by AG-CA-07, Proposition 3.2. Fix a base prime and a finite purely inseparable extension $k$ of its residue field. After tensoring, the intermediate ring $D=B\otimes_Ak$ is Noetherian and regular, by regularity of the first map. The final ring $E=C\otimes_Ak$ is Noetherian by the stipulated fibre hypothesis and finiteness of $k$ over that residue field. The map $D\to E$ is flat by base change. At a prime $\mathfrak r$ of $E$ with contraction $\mathfrak s$ in $D$, its closed fibre is a localization of
$$ (C\otimes_B\kappa(\mathfrak b))\otimes_{\kappa(\mathfrak b)}\kappa(\mathfrak s),$$
where $\mathfrak b$ contracts $\mathfrak s$ to $B$. The original fibre is geometrically regular. The preceding arbitrary-field-extension argument makes this Noetherian extended fibre regular; localizing retains regularity. Thus the flat local map $D_{\mathfrak s}\to E_{\mathfrak r}$ has regular source and regular closed fibre. Regularity ascent makes $E_{\mathfrak r}$ regular. This proves every tested extended composite fibre is regular, hence geometrically regular by the finite purely inseparable criterion. It supplies the full composition argument at every tested fibre.
 ∎

<a id="more-algebra-lemma-regular-permanence"></a>

#### Lemma F.125: regular permanence

*Adapted from the Stacks project, more-algebra.tex, lines 11116–11129.*

If $A\to B\to C$ are maps of Noetherian rings, $A\to C$ is regular and $B\to C$ faithfully flat, then $A\to B$ is regular.

**Proof.** 
For an injection $N_1\to N_2$ of $A$-modules, its tensor with $B$ has a kernel. Tensor that kernel with the flat $B$-module $C$; it becomes the kernel of the tensor map with $C$, which is zero by $A$-flatness of $C$. Faithfulness makes the original kernel zero. This proves $A$-flatness of $B$. In each residue-field fibre the map from the $B$-fibre to the $C$-fibre is faithfully flat by base change. The latter is geometrically regular, so geometric-regularity descent proved above makes the former geometrically regular. Flatness and these fibre conditions are precisely regularity of $A\to B$.
 ∎

<a id="more-algebra-lemma-relative-global-complete-intersection-koszul"></a>

#### Lemma F.126: relative global complete intersection koszul

*Adapted from the Stacks project, more-algebra.tex, lines 8995–9012.*

For the Noetherian relative global complete intersection above, the equation list has zero positive Koszul homology.

**Proof.** 
At primes containing its ideal the conormal lifting proof makes the list regular, and the Koszul cone induction in the preceding equivalence proof makes its positive homology zero. Away from that ideal choose coefficients $a_i$ with $\sum a_if_i=1$ in the local ring. Wedging with $\sum a_ie_i$ gives $dh+hd=1$ by the alternating Leibniz rule, making the Koszul complex contractible there. Its homology thus vanishes at every prime, and local detection makes it zero.
 ∎

<a id="more-algebra-lemma-relative-regular-immersion-algebra"></a>

#### Lemma F.127: relative regular immersion algebra

*Adapted from the Stacks project, more-algebra.tex, lines 8601–8631.*

Let $A\to B$, $A\to A'$, $J=(f_i)\subset B$, and suppose $B/J$ is $A$-flat. Quasi-regularity and $H_1$-regularity of $(f_i)$ are preserved in $B'=B\otimes_AA'$.

**Proof.** 
For quasi-regularity the hypothesis is $\operatorname{gr}_J B\cong(B/J)[T_1,\ldots,T_r]$, with $T_i$ represented by $f_i$. Each graded piece is therefore $A$-flat. Induction on $n$ in $0\to J^n/J^{n+1}\to B/J^{n+1}\to B/J^n\to0$ makes every $B/J^n$ flat, using the extension-of-flat-modules proof AG-CA-07, Theorem 6.1. Tensoring $0\to J^n\to B\to B/J^n\to0$ consequently stays exact on the left. Its kernel identifies $J^n\otimes_AA'$ with $(J')^n$, since products of the images of the $f_i$ generate the latter ideal. Taking consecutive quotients proves $\operatorname{gr}_{J'}B'=\operatorname{gr}_J B\otimes_AA'=(B'/J')[T_i]$.

For $H_1$-regularity set $Z=\ker(B^r\xrightarrow{(f_i)}J)$. The sequences $0\to J\to B\to B/J\to0$, $Z\to B^r\to J\to0$, and $\bigwedge^2B^r\to Z\to H_1\to0$ are exact. After tensoring the first stays injective on the left by quotient flatness, and the last two stay right exact. Thus $Z\otimes_AA'$ surjects onto the new cycle module, and its quotient by the images of the Koszul boundaries is a quotient of $H_1\otimes_AA'$. If $H_1=0$, the new $H_1$ is zero. This proves the assertion over arbitrary rings without assuming $B$ flat.
 ∎

<a id="more-algebra-lemma-symmetric-algebra-smooth"></a>

#### Lemma F.128: symmetric algebra smooth

*Adapted from the Stacks project, more-algebra.tex, lines 2111–2136.*

Let $A$ be a ring. Let $M$ be an $A$-module. Then $C = \text{Sym}_A^*(M)$
is smooth over $A$ if and only if $M$ is a finite projective $A$-module.

**Proof.** 
Let $\sigma : C \to A$ be the projection onto the degree $0$ part of $C$.
Then $J = \ker(\sigma)$ is the part of degree $> 0$ and we see that
$J/J^2 = M$ as an $A$-module. Hence if $A \to C$ is smooth then $M$ is
a finite projective $A$-module by
Algebra, Lemma [F.79](#algebra-lemma-section-smooth).

Conversely, assume that $M$ is finite projective and choose a surjection
$A^{\oplus n} \to M$ with kernel $K$. Of course the sequence
$0 \to K \to A^{\oplus n} \to M \to 0$ is split as $M$ is projective.
In particular we see that $K$ is a finite $A$-module and hence
$C$ is of finite presentation over $A$ as $C$ is a quotient of
$A[x_1, \ldots, x_n]$ by the ideal generated by $K \subset \bigoplus Ax_i$.
The computation of Lemma [F.102](#more-algebra-lemma-cotangent-complex-symmetric-algebra)
applies here because $M$ is finite projective. It identifies the conormal
complex with $[K\otimes_A C\to C^{\oplus n}]$, whose differential is
the tensor of the split inclusion $K\hookrightarrow A^{\oplus n}$.
This conormal sequence is split exact with cokernel $M\otimes_A C$.
Together with the finite presentation just proved, this means that
$C$ is smooth over $A$ by
Algebra, Definition [F.6](#algebra-definition-smooth).
 ∎

<a id="more-algebra-lemma-syntomic-lci"></a>

#### Lemma F.129: syntomic lci

*Adapted from the Stacks project, more-algebra.tex, lines 9014–9061.*

Let $R \to S$ be a ring map with $R$ Noetherian. The following are equivalent

1. $R \to S$ is syntomic
(Algebra, Definition [F.1](#algebra-definition-lci)), and

1. $R \to S$ is flat and a local complete intersection.

**Proof.** 
Assume (1). Then $R \to S$ is flat by definition.
By Algebra, Lemma [F.87](#algebra-lemma-syntomic) and
Lemma [F.114](#more-algebra-lemma-lci-local) we see that it suffices to
show a relative global complete intersection is
a local complete intersection homomorphism which is
Lemma [F.126](#more-algebra-lemma-relative-global-complete-intersection-koszul).

Assume (2). A local complete intersection is of finite presentation
because a Koszul-regular ideal is finitely generated.
Let $R \to k$ be a map to a field. It suffices to show that
$S' = S \otimes_R k$ is a local complete intersection over $k$, see
Algebra, Definition [F.2](#algebra-definition-lci-field).
Choose a prime $\mathfrak q' \subset S'$.
Write $S = R[x_1, \ldots, x_n]/I$.
Then $S' = k[x_1, \ldots, x_n]/I'$ where
$I' \subset k[x_1, \ldots, x_n]$ is the image of $I$.
Let $\mathfrak p' \subset k[x_1, \ldots, x_n]$,
$\mathfrak q \subset S$,
and $\mathfrak p \subset R[x_1, \ldots, x_n]$
be the corresponding primes.
By Definition [F.95](#more-algebra-definition-regular-ideal)
exists an $g \in R[x_1, \ldots, x_n]$, $g \not \in \mathfrak p$
and $f_1, \ldots, f_r \in R[x_1, \ldots, x_n]_g$ which form
a Koszul-regular sequence generating $I_g$.
Since $S$ and hence $S_g$ is flat over $R$
we see that the images $f'_1, \ldots, f'_r$ in
$k[x_1, \ldots, x_n]_g$ form a $H_1$-regular sequence
generating $I'_g$, see
Lemma [F.127](#more-algebra-lemma-relative-regular-immersion-algebra).
Thus $f'_1, \ldots, f'_r$ map to a regular sequence in
$k[x_1, \ldots, x_n]_{\mathfrak p'}$ generating
$I'_{\mathfrak p'}$ by Lemma [F.118](#more-algebra-lemma-noetherian-finite-all-equivalent).
Applying Algebra, Lemma [F.57](#algebra-lemma-lci)
we conclude $S'_{gg'}$ for some $g' \in S$, $g' \not \in \mathfrak q'$
is a global complete intersection over $k$ as desired.
 ∎

<a id="more-algebra-lemma-transitive-lci-at-end"></a>

#### Lemma F.130: transitive lci at end

*Adapted from the Stacks project, more-algebra.tex, lines 9068–9115.*

Let $A \to B \to C$ be ring maps. Assume $B \to C$ is a local complete
intersection homomorphism. Choose a presentation
$\alpha : A[x_s, s \in S] \to B$ with kernel $I$. Choose a presentation
$\beta : B[y_1, \ldots, y_m] \to C$ with kernel $J$. Let
$\gamma : A[x_s, y_t] \to C$ be the induced presentation of $C$ with kernel
$K$. Then we get a canonical commutative diagram

$$
\begin{gathered}
0 \xrightarrow{} \Omega_{A[x_s]/A} \otimes C \\
\Omega_{A[x_s]/A} \otimes C \xrightarrow{} \Omega_{A[x_s, y_t]/A} \otimes C \\
\Omega_{A[x_s, y_t]/A} \otimes C \xrightarrow{} \Omega_{B[y_t]/B} \otimes C \\
\Omega_{B[y_t]/B} \otimes C \xrightarrow{} 0 \\
0 \xrightarrow{} I/I^2 \otimes C \\
I/I^2 \otimes C \xrightarrow{} K/K^2 \\
I/I^2 \otimes C \xrightarrow{} \Omega_{A[x_s]/A} \otimes C \\
K/K^2 \xrightarrow{} J/J^2 \\
K/K^2 \xrightarrow{} \Omega_{A[x_s, y_t]/A} \otimes C \\
J/J^2 \xrightarrow{} 0 \\
J/J^2 \xrightarrow{} \Omega_{B[y_t]/B} \otimes C
\end{gathered}
$$

with exact rows. In particular, the six term exact sequence of
Algebra, Lemma [F.42](#algebra-lemma-exact-sequence-NL)
can be completed with a zero on the left, i.e., the sequence

$$
0 \to H_1(\NL_{B/A} \otimes_B C) \to
H_1(L_{C/A}) \to
H_1(L_{C/B}) \to
\Omega_{B/A} \otimes_B C \to
\Omega_{C/A} \to
\Omega_{C/B} \to 0
$$

is exact.

**Proof.** 
The only thing to prove is the injectivity of the map
$I/I^2 \otimes C \to K/K^2$.
By assumption the ideal $J$ is Koszul-regular.
Hence we have $IA[x_s, y_j] \cap K^2 = IK$ by
Lemma [F.101](#more-algebra-lemma-conormal-sequence-H1-regular-ideal).
This means that the kernel of $K/K^2 \to J/J^2$ is
isomorphic to $IA[x_s, y_j]/IK$. Since
$I/I^2 \otimes_B C = IA[x_s, y_j]/IK$ by right exactness
of tensor product, this provides us with the desired injectivity of
$I/I^2 \otimes_B C \to K/K^2$.
 ∎

<a id="more-algebra-lemma-transitivity-gamma"></a>

#### Lemma F.131: transitivity gamma

*Adapted from the Stacks project, more-algebra.tex, lines 9208–9228.*

For fields $K\subset L\subset M$ the sequence $0\to H_1(L_{L/K})\otimes_LM\to H_1(L_{M/K})\to H_1(L_{M/L})\to\Omega_{L/K}\otimes_LM\to\Omega_{M/K}\to\Omega_{M/L}\to0$ is exact.

**Proof.** 
First suppose the last algebra is a global complete-intersection $L$-algebra $C$. Present $L=P/I$ with $P=K[X_s]$, allowing arbitrary variables, and $C=L[Y]/J$ with $J$ a regular equation ideal. Let $Q=P[Y]$ and $H$ be the kernel of $Q\to C$. The sequence of conormal modules is
$$0\to (I/I^2)\otimes_LC\to H/H^2\to J/J^2\to0.$$
For its left injectivity, the relation calculation already proved at [F.101](#more-algebra-lemma-conormal-sequence-H1-regular-ideal) gives $IQ\cap H^2=IH$. Thus its left module is $IQ/IH$, exactly the kernel in the middle. Surjectivity on the right is lifting ideal representatives. Polynomial differentials give the split short exact sequence $0\to\Omega_{P/K}\otimes C\to\Omega_{Q/K}\otimes C\to\Omega_{L[Y]/L}\otimes C\to0$ on the free $X$ and $Y$ bases. Apply the full snake-lemma proof already written to these two short exact rows and their conormal differentials. Their kernels are the three first homology groups and their cokernels the three differential modules, so it gives precisely the six-term exact sequence with zero at its left.

Now express $M$ as the filtered union of global complete-intersection $L$-subalgebras by the preceding monic-tower proof. The conormal-complex filtered-colimit calculation proved above identifies all three complexes at the limit. Filtered colimits are exact by common-stage representatives. Finally tensoring with the field $M$ over $L$ is exact, so the first kernel in the limit is $H_1(L_{L/K})\otimes_LM$, rather than merely a homology group of an unproved derived base change. This proves every term and the initial injectivity.
 ∎

<a id="more-algebra-proposition-Noetherian-complete-G-ring"></a>

#### Proposition F.132: Noetherian complete G ring

*Adapted from the Stacks project, more-algebra.tex, lines 12965–12999.*

A Noetherian complete local ring is a G-ring.

**Proof.** 
Let $A$ be a Noetherian complete local ring. By
Lemma [F.99](#more-algebra-lemma-check-G-ring-easy)
it suffices to check that $B = A/\mathfrak q$ has geometrically regular
formal fibres over the minimal prime $(0)$ of $B$. Thus we may assume
that $A$ is a domain and it suffices to check the condition for
the formal fibres over the minimal prime $(0)$ of $A$.
Let $K$ be the fraction field of $A$.

We can choose a subring $A_0 \subset A$ which is a regular complete local
ring such that $A$ is finite over $A_0$, see Algebra, Lemma
[F.25](#algebra-lemma-complete-local-Noetherian-domain-finite-over-regular).
Moreover, we may assume that $A_0$ is a power series ring over a
field or a Cohen ring. By Lemma [F.96](#more-algebra-lemma-G-ring-goes-up-quasi-finite)
we see that it suffices to prove the result for $A_0$.

Assume that $A$ is a power series ring over a field or a Cohen ring.
Since $A$ is regular local, each $A_\mathfrak p$ is regular local by the written localization proof
[AG-CA-14, Theorem 3.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/regular-local-rings.html#3-regularity-at-more-general-points).
Hence the completions $A_\mathfrak p^\wedge$ are regular, see
Lemma [AG-CA-19, Theorem 4.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/completion.html).
Hence the fibre $A_{\mathfrak p}^\wedge \otimes_A K$ is, as a localization
of $A_\mathfrak p^\wedge$, also regular. Thus we are done if the
characteristic of $K$ is $0$. The positive characteristic case
is the case $A = k[[x_1, \ldots, x_d]]$ which is a special case of
Lemma [F.110](#more-algebra-lemma-helper-G-ring).
 ∎

<a id="more-algebra-proposition-characterization-geometrically-regular"></a>

#### Proposition F.133: characterization geometrically regular

*Adapted from the Stacks project, more-algebra.tex, lines 9306–9458.*

For a characteristic-$p$ field $k$ and Noetherian local $k$-algebra $(A,\mathfrak m,K)$, the following are equivalent: geometric regularity; regularity after every finite subextension of $k^{1/p}/k$; regularity of $A$ and injectivity of $H_1(L_{K/k})\to\mathfrak m/\mathfrak m^2$; regularity of $A$ and injectivity of $\Omega_{k/\mathbb F_p}\otimes_kK\to\Omega_{A/\mathbb F_p}\otimes_AK$.

**Proof.** 
First identify the last two injections. The general Jacobi–Zariski calculation already proved gives a natural map $H=H_1(L_{K/k})\to E=\mathfrak m/\mathfrak m^2$. For a quotient presentation over $A$ this first homology is exactly the conormal module $E$, since the degree-zero relative polynomial module is zero. Absolute prime-field formal smoothness of $K$, AG-CA-19S, Lemma 1.1, makes $H_1(L_{K/\mathbb F_p})=0$. Thus its Jacobi–Zariski row is $0\to E\to V\to\Omega_{K/\mathbb F_p}\to0$, with $V=\Omega_{A/\mathbb F_p}\otimes_AK$. The field Jacobi–Zariski row is $0\to H\to\Omega_{k/\mathbb F_p}\otimes_kK\to\Omega_{K/\mathbb F_p}\to\Omega_{K/k}\to0$. Naturality gives a square into the first row and identity on $\Omega_{K/\mathbb F_p}$. A vector killed by the middle vertical map lies in the kernel of the bottom map to $\Omega_{K/\mathbb F_p}$, hence comes uniquely from $H$; it is killed precisely when its image in $E$ is zero. Conversely every such vector maps to zero in $V$. The kernels are therefore isomorphic, proving equivalence of the two asserted injectivities.

Assume $A$ regular and $H\to E$ injective. For any finite purely inseparable $k'/k$, the ring $A'=A\otimes_kk'$ is local, since pure inseparability gives a unique prime above each prime as checked above. Let its residue field be $K'$, and write $E'=\mathfrak m'/\mathfrak m'^2$, $H'=H_1(L_{K'/k'})$. The relative conormal rows have the form $0\to H\otimes_KK'\to E\otimes_KK'\to V_0\to W\to0$ and $H'\to E'\to V_0\to W'\to0$, where differential base change identifies the two middle $V_0$ spaces, $W=\Omega_{K/k}\otimes_KK'$ and $W'=\Omega_{K'/k'}$. The induced $\alpha:W\to W'$ is surjective because the map from their common $V_0$ is surjective. The field-square equality proved above says $\dim\ker\alpha-\dim\ker\beta+\dim\operatorname{coker}\beta=0$ for $\beta:H\otimes K'\to H'$. All these defects are finite. Moreover $H\otimes K'$ is finite because it injects into the finite $E\otimes K'$, so $H'$ is finite too.

Let $L,L'$ be the images of $E\otimes K',E'$ in $V_0$. Then $L\subset L'$ and $L'/L=\ker\alpha$. Exactness gives $\dim E'\le\dim H'+\dim L'$. On the top row $\dim E=\dim H+\dim L$. Subtracting yields
$$\dim E'-\dim E\le(\dim H'-\dim H)+\dim\ker\alpha=\dim\operatorname{coker}\beta-\dim\ker\beta+\dim\ker\alpha=0.$$
The finite free map $A\to A'$ is injective and integral, so their dimensions agree by AG-CA-05, Theorem 5.1. Thus $\dim E'\le\dim E=\dim A=\dim A'$, and the height theorem supplies the reverse embedding-dimension inequality. Hence $A'$ is regular. The finite purely inseparable criterion proves geometric regularity.

It remains to derive the absolute injection from regularity after all finite subextensions of $k^{1/p}$. This assumption includes $A$ itself regular. Choose any finite list $a_1,\ldots,a_n\in k$ whose differentials are independent. The proved root-degree lemma gives $k'=k(a_i^{1/p})=k[T_i]/(T_i^p-a_i)$ with degree $p^n$. Its base change $A'$ is regular by assumption and has the same dimension as $A$ by the preceding finite-integral argument. The conormal complex for $A'/A$ is $A'^n\xrightarrow{0}A'^n$, since these monic equations form a regular list and their relative derivatives vanish. The general Jacobi–Zariski calculation sends its $i$th first-homology basis vector to $da_i\otimes1$, up to the harmless common sign convention. Consequently after tensoring with $K'$ the map $\delta:V\otimes_KK'\to V'=\Omega_{A'/\mathbb F_p}\otimes_{A'}K'$ has cokernel $K'^n$ and kernel spanned by the $da_i\otimes1$. This exactness survives tensoring: the relative differential quotient is free, so its short exact quotient row splits; right exactness of tensor preserves the preceding surjection onto its kernel.

Compare the two absolute rows $0\to E\otimes K'\to V\otimes K'\to\Omega_{K/\mathbb F_p}\otimes K'\to0$ and $0\to E'\to V'\to\Omega_{K'/\mathbb F_p}\to0$. The maps on the left have equally dimensional finite spaces, since both local rings are regular of equal dimension, so their kernel and cokernel dimensions agree. The map on the right likewise has equal finite kernel and cokernel dimensions: the field Jacobi–Zariski sequence identifies them with $H_1(L_{K'/K})$ and $\Omega_{K'/K}$, and Cartier equality for the finite field extension gives equality. The full snake sequence for these rows gives
$$\dim\ker\delta-\dim\operatorname{coker}\delta=(\dim\ker\delta_E-\dim\operatorname{coker}\delta_E)+(\dim\ker\delta_K-\dim\operatorname{coker}\delta_K)=0.$$
All its defect spaces are finite; for the middle kernel this also follows from its preceding span by the $n$ displayed vectors. Its cokernel has dimension $n$, so its kernel has dimension $n$ and those $n$ spanning $da_i\otimes1$ are independent. A basis of $\Omega_{k/\mathbb F_p}$ is given by the absolute $p$-basis differentials, and every relation uses finitely many of them. The preceding argument therefore proves the whole absolute injection. Finally geometric regularity implies the stated root-height-one tests by definition. This closes every implication and the two dimension chases explicitly.
 ∎

<a id="more-algebra-proposition-finite-type-over-G-ring"></a>

#### Proposition F.134: finite type over G ring

*Adapted from the Stacks project, more-algebra.tex, lines 13161–13250.*

Let $R$ be a G-ring. If $R \to S$ is essentially of finite type
then $S$ is a G-ring.

**Proof.** 
Since being a G-ring is a property of the local rings it is clear
that a localization of a G-ring is a G-ring. Conversely, if every
localization at a prime is a G-ring, then the ring is a G-ring.
Thus it suffices to show that $S_\mathfrak q$ is a G-ring for every
finite type $R$-algebra $S$ and every prime $\mathfrak q$ of $S$.
Writing $S$ as a quotient of $R[x_1, \ldots, x_n]$ we see from
Lemma [F.96](#more-algebra-lemma-G-ring-goes-up-quasi-finite) that it suffices to prove
that $R[x_1, \ldots, x_n]$ is a G-ring. By induction on $n$ it
suffices to prove that $R[x]$ is a G-ring. Let $\mathfrak q \subset R[x]$
be a maximal ideal. By Lemma [F.100](#more-algebra-lemma-check-G-ring-maximal-ideals)
it suffices to show that

$$
R[x]_\mathfrak q \longrightarrow R[x]_\mathfrak q^\wedge
$$

is regular. If $\mathfrak q$ lies over $\mathfrak p \subset R$, then
we may replace $R$ by $R_\mathfrak p$. Hence we may assume that $R$
is a Noetherian local G-ring with maximal ideal $\mathfrak m$ and
that $\mathfrak q \subset R[x]$ lies over $\mathfrak m$. Note that
there is a unique prime $\mathfrak q' \subset R^\wedge[x]$
lying over $\mathfrak q$. Consider the diagram

$$
\begin{gathered}
R[x]_\mathfrak q^\wedge \xrightarrow{} (R^\wedge[x]_{\mathfrak q'})^\wedge \\
R[x]_\mathfrak q \xrightarrow{} R^\wedge[x]_{\mathfrak q'} \\
R[x]_\mathfrak q \xrightarrow{} R[x]_\mathfrak q^\wedge \\
R^\wedge[x]_{\mathfrak q'} \xrightarrow{} (R^\wedge[x]_{\mathfrak q'})^\wedge
\end{gathered}
$$

Since $R$ is a G-ring the lower horizontal arrow is regular
(as a localization of a base change of the regular ring map
$R \to R^\wedge$). Suppose we can prove the right vertical arrow
is regular. Then it follows that the composition
$R[x]_\mathfrak q \to (R^\wedge[x]_{\mathfrak q'})^\wedge$
is regular. The local map
$R[x]_\mathfrak q\to R^\wedge[x]_{\mathfrak q'}$ is flat by base
change and localization of completion. Its completed map is therefore
faithfully flat by Lemma [F.99A](#completion-flat-local-map).
Lemma [F.125](#more-algebra-lemma-regular-permanence) now proves that
the left vertical arrow is regular.
Hence we see that we may assume $R$ is a Noetherian complete
local ring and $\mathfrak q$ a prime lying over the maximal
ideal of $R$.

Let $R$ be a Noetherian complete local ring and let $\mathfrak q \subset R[x]$
be a maximal ideal lying over the maximal ideal of $R$. Let
$\mathfrak r \subset \mathfrak q$ be a prime ideal. We want to show that
$R[x]_\mathfrak q^\wedge \otimes_{R[x]} \kappa(\mathfrak r)$ is
a geometrically regular algebra over $\kappa(\mathfrak r)$.
Set $\mathfrak p = R \cap \mathfrak r$. Then we can replace $R$
by $R/\mathfrak p$ and $\mathfrak q$ and $\mathfrak r$ by their
images in $R/\mathfrak p[x]$, see
Lemma [F.99](#more-algebra-lemma-check-G-ring-easy).
Hence we may assume that $R$ is a domain and that $\mathfrak r \cap R = (0)$.

Choose the regular complete local subring $R_0\subset R$ supplied
by Lemma [F.25](#algebra-lemma-complete-local-Noetherian-domain-finite-over-regular),
with $R$ finite over $R_0$. For the finite extension
$R_0[x]\to R[x]$, write $\mathfrak q_0,\mathfrak r_0$ for the
contractions of $\mathfrak q,\mathfrak r$. The contraction
$\mathfrak q_0$ is maximal and lies over the maximal ideal of $R_0$:
lying over and the finite integral extension identify the contractions
of the maximal ideals of the complete local rings. Moreover
$\mathfrak r_0\cap R_0=(0)$. The individual-fibre assertion of
Lemma [F.96](#more-algebra-lemma-G-ring-goes-up-quasi-finite), proved
by the finite-completion product decomposition and field base change,
reduces this particular fibre to the corresponding fibre for $R_0$.
This use does not assume that $R_0[x]$ is already a G-ring.

We can therefore assume $R$ regular and complete. If
$\mathfrak r=(0)$, the desired fibre is

$$
\widehat{R[x]_\mathfrak q}\otimes_{R[x]}\operatorname{Frac}(R[x]),
$$

which is geometrically regular by the second assertion of Lemma
[F.110](#more-algebra-lemma-helper-G-ring), in every characteristic.
If $\mathfrak r\ne(0)$, its extension to
$K[x]$, $K=\operatorname{Frac}(R)$, is generated by an irreducible
polynomial, and $\kappa(\mathfrak r)/K$ is finite. Apply the second
assertion of Lemma
[F.97](#more-algebra-lemma-another-helper-G-ring). Its actual proof
extends this residue field to each finite purely inseparable test
field, chooses a finite complete local domain inside that field,
and identifies the tested completed fibre with factors of

$$
\big(\widehat{B[x]_{\mathfrak q_i}}\otimes_B\operatorname{Frac}(B)\big)/(x-a).
$$

The parenthesized ring is regular by the first assertion of F.97;
the extended derivation $\partial/\partial x$ sends $x-a$ to one,
so the proved hypersurface argument makes each quotient regular.
Thus F.97 proves geometric regularity of this nonzero-polynomial
fibre in every characteristic. This quotient is not asserted to be
a localization. The two cases exhaust the primes over $(0)$, proving
the required regular completion map and hence polynomial permanence
of G-rings.
 ∎

<a id="more-algebra-proposition-ubiquity-G-ring"></a>

#### Proposition F.135: ubiquity G ring

*Adapted from the Stacks project, more-algebra.tex, lines 13261–13281.*

Every ring essentially of finite type over $\mathbf Z$ is a G-ring.

**Proof.** 
The localization of $\mathbf Z$ at zero is the field $\mathbf Q$, whose completion map is the identity. At $(p)$ it is a discrete valuation ring; its completion is again a discrete valuation ring, proved by Completion, Theorem 4.1 and the regular one-dimensional description in the earlier valuation-ring lesson. The completion map is flat by Completion, Theorem 3.2. Its closed fibre is $\mathbf F_p$. Its generic fibre is $\mathbf Q_p$ over $\mathbf Q$, hence is geometrically regular: in characteristic zero a finite field extension is separable, and tensoring a field with a finite separable extension is a finite product of separable field extensions, which are regular. Equivalently, the proved finite purely inseparable criterion makes every characteristic-zero extension geometrically regular, because its only purely inseparable test extension is the identity. This proves the generic-fibre assertion with the exact criterion written below. Thus $\mathbf Z$ is a G-ring. Proposition [F.134](#more-algebra-proposition-finite-type-over-G-ring), followed by localization, proves the assertion. This proof does not consume the source's broader complete-local-ring or Dedekind-ring statements.
 ∎

<a id="topology-lemma-Noetherian"></a>

#### Lemma F.136: Noetherian

*Adapted from the Stacks project, topology.tex, lines 1304–1357.*

Let $X$ be a Noetherian topological space.

1. Any subset of $X$ with the induced topology is Noetherian.

1. The space $X$ has finitely many irreducible components.

1. Each irreducible component of $X$ contains a nonempty open of $X$.

**Proof.** 
Let $T \subset X$ be a subset of $X$.
Let $T_1 \supset T_2 \supset \ldots$
be a descending chain of closed subsets of $T$.
Write $T_i =  T \cap Z_i$ with $Z_i \subset X$ closed.
Consider the descending chain of closed subsets
$Z_1 \supset Z_1\cap Z_2 \supset Z_1 \cap Z_2 \cap Z_3 \ldots$
This stabilizes by assumption and hence the original sequence
of $T_i$ stabilizes. Thus $T$ is Noetherian.

Let $A$ be the set of closed subsets of $X$ which do not
have finitely many irreducible components. Assume that
$A$ is not empty to arrive at a contradiction.
The set $A$ is partially ordered by inclusion: $Z \leq Z'
\Leftrightarrow Z \subset Z'$ for $Z, Z' \in A$.
By the descending chain condition we may find a
minimal element of $A$, say $Z$. As $Z$ is not a finite
union of irreducible components, it is not irreducible.
Hence we can write $Z = Z' \cup Z''$ and both are strictly smaller
closed subsets. By construction $Z' = \bigcup Z'_i$ and
$Z'' = \bigcup Z''_j$ are finite unions of their irreducible
components (Lemma [F.137](#topology-lemma-irreducible)).
Hence $Z = \bigcup Z'_i \cup \bigcup Z''_j$ is
a finite union of irreducible closed subsets.
After removing redundant members of this expression,
this will be the decomposition of $Z$ into its irreducible
components (Lemma [F.138](#topology-lemma-pick-irreducible-components)), a contradiction.

Let $Z \subset X$ be an irreducible component of $X$.
Let $Z_1, \ldots, Z_n$ be the other irreducible components
of $X$. Consider $U = Z \setminus (Z_1\cup\ldots\cup Z_n)$.
This is not empty since otherwise the irreducible space
$Z$ would be contained in one of the other $Z_i$.
Because $X = Z \cup Z_1 \cup \ldots \cup Z_n$ (see Lemma [F.137](#topology-lemma-irreducible)),
also $U = X \setminus (Z_1\cup\ldots\cup Z_n)$
and hence open in $X$. Thus $Z$ contains a nonempty
open of $X$.
 ∎

<a id="topology-lemma-irreducible"></a>

#### Lemma F.137: irreducible

*Adapted from the Stacks project, topology.tex, lines 931–968.*

The closure of an irreducible subset is irreducible. Irreducible components are closed, every irreducible subset lies in one, and the components cover the space.

**Proof.** 
If its closure is the union of two relatively closed subsets, intersection with the original irreducible subset puts that subset in one of them. Taking closures puts the entire closure there. Maximality then makes any component equal to its closure. For existence, order irreducible supersets of a fixed irreducible subset by inclusion. The union of a chain is irreducible: two nonempty relatively open subsets of the union meet some two members of the chain; a common larger member meets both, and irreducibility of that member forces their intersection to be nonempty. Thus every chain has an upper bound, and Zorn's lemma gives a maximal member. Apply this to each singleton for the covering assertion.
 ∎

<a id="topology-lemma-pick-irreducible-components"></a>

#### Lemma F.138: pick irreducible components

*Adapted from the Stacks project, topology.tex, lines 970–995.*

If a space is a finite union of irreducible closed subsets, none contained in the union of the others, then those subsets are exactly its irreducible components.

**Proof.** 
Intersect a component with each member of the finite cover. This expresses it as a finite union of closed subsets. Repeatedly applying irreducibility puts it in one member, and maximality makes it equal to that member. Conversely any member lies in a component by the preceding existence proof. That component is a member by the first argument. Inclusion in a different member would make the original member redundant, contrary to the assumption. It is therefore itself a component.
 ∎

## 6. Exact earlier proof dependencies

The statements in Sections 1–5 specify the scope actually used in approximation. The following earlier proofs supply their elementary algebra inputs. [Descent and Zariski Main](AG-RG-S04.md), Lemma D2.2, Theorem C4.3 and Corollary B1.2, precedes the henselian section argument. The broader formal-smoothness/regularity equivalence is not consumed: the explicit completion arguments F.99A, F.110 and F.132–F.135 prove the required G-ring inputs. This dependency list points to the proofs of the results it names; results that it does not name are not covered by it. Finite type and finite presentation on every compatible affine pair, used in the target-descent step of AG-GS-05, Lemma 7.6, have their complete morphism argument in [AG-RG-S04, Lemma A1.8](AG-RG-S04.md#affine-presentation-communication), using the preceding finite-generator and finite-relation algebra patching proof. In the application of AG-GS-05, Theorem 7.7, the fixed-character-group splitting scheme is globally a disjoint union on the splitting cover, so this application uses that case of Lemma 7.6.

### Exact earlier programme proofs used

These locators refer to written programme proofs. They do not claim that an unused, broader source statement has been proved.

| Consumed source label | Earlier programme proof |
| --- | --- |
| definition regular | [AG-CA-14, Section 1, definition](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/regular-local-rings.html) |
| definition regular local | [AG-CA-14, Section 1, definition](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/regular-local-rings.html) |
| definition standard smooth | [AG-CA-17, Section 4, equations (6) and (7)](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/formally-smooth-unramified-and-etale-ring-maps.html) |
| lemma Artin Rees | [AG-CA-03, Theorem 5.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/noetherian-and-artinian-rings.html) |
| lemma Noetherian irreducible components | [AG-CA-03, Proposition 2.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/noetherian-and-artinian-rings.html) |
| lemma Noetherian topology | [AG-CA-03, Proposition 2.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/noetherian-and-artinian-rings.html) |
| lemma Zariski topology | [AG-CA-01, Theorem 1.2 and Proposition 2.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/spectra-of-rings.html) |
| lemma artinian finite length | [AG-CA-03, Theorem 4.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/noetherian-and-artinian-rings.html) |
| lemma characterize henselian | [AG-CA-20, Theorem 1.2 and Theorem 2.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/henselian-local-rings-and-henselization.html) |
| lemma characterize projective | [AG-CA-06S, Section 1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/resolutions-tor-and-ext.html) |
| lemma cokernel flat | [AG-CA-08, Lemma 5.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/faithful-flatness-and-the-local-criterion-for-flatness.html) |
| lemma compose formally smooth | [AG-CA-17, Theorem 1.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/formally-smooth-unramified-and-etale-ring-maps.html) |
| lemma differentials base change | [AG-CA-16, Theorem 2.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/kahler-differentials.html) |
| lemma differentials finitely presented | [AG-CA-16, Theorem 5.1, finite polynomial presentation](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/kahler-differentials.html) |
| lemma dimension base fibre equals total | [AG-CA-11, Theorem 5.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/dimension-theory-of-noetherian-local-rings.html) |
| lemma dimension base fibre total | [AG-CA-11, Theorem 5.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/dimension-theory-of-noetherian-local-rings.html) |
| lemma dimension prime polynomial ring | [AG-CA-09, Theorem 4.3](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/krull-dimension-and-noether-normalization.html) |
| lemma disjoint implies product | [AG-CA-01, Theorem 5.2 and Corollary 5.3](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/spectra-of-rings.html) |
| lemma etale at prime | [AG-CA-17, Theorem 7.2 and Corollary 7.3](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/formally-smooth-unramified-and-etale-ring-maps.html) |
| lemma exact sequence differentials | [AG-CA-16, Theorem 3.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/kahler-differentials.html) |
| lemma faithfully flat universally injective | [AG-CA-08, Theorem 2.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/faithful-flatness-and-the-local-criterion-for-flatness.html) |
| lemma finite finite fibres | [AG-CA-05, Theorem 3.4](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/integral-extensions-lying-over-going-up-and-going-down.html) |
| lemma finite projective | [AG-CA-07, Theorem 5.3](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/tor-and-flat-modules.html) |
| lemma finite transitive | [AG-CA-05, Theorem 1.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/integral-extensions-lying-over-going-up-and-going-down.html) |
| lemma flat | [AG-CA-07, Theorem 2.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/tor-and-flat-modules.html) |
| lemma flat base change | [AG-CA-07, Proposition 3.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/tor-and-flat-modules.html) |
| lemma flat eq | [AG-CA-07, Theorem 5.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/tor-and-flat-modules.html) |
| lemma flat going down | [AG-CA-07, Theorem 6.3](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/tor-and-flat-modules.html) |
| lemma flat tor zero | [AG-CA-07, Theorem 2.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/tor-and-flat-modules.html) |
| lemma formally etale etale | [AG-CA-17, Theorem 2.2 and Proposition 6.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/formally-smooth-unramified-and-etale-ring-maps.html) |
| lemma integral no inclusion | [AG-CA-05, Theorem 3.3](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/integral-extensions-lying-over-going-up-and-going-down.html) |
| lemma intersect powers ideal module zero | [AG-CA-03, Theorem 6.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/noetherian-and-artinian-rings.html) |
| lemma lci CM | [AG-CA-12, Corollary 6.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/regular-sequences-depth-and-cohen-macaulay-modules.html) |
| lemma maximal chain CM | [AG-CA-12, Lemma 5.4 and Theorem 5.5](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/regular-sequences-depth-and-cohen-macaulay-modules.html) |
| lemma quasi compact | [AG-CA-01, Proposition 2.3](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/spectra-of-rings.html) |
| lemma rank omega | [AG-CA-18, Proposition 3.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/smooth-algebras-over-a-field-and-the-jacobian-criterion.html) |
| lemma reformulate CM | [AG-CA-12, Theorem 4.2 and Corollary 4.3](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/regular-sequences-depth-and-cohen-macaulay-modules.html) |
| lemma regular domain | [AG-CA-12, Theorem 6.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/regular-sequences-depth-and-cohen-macaulay-modules.html) |
| lemma regular goes up | [AG-CA-14, Proposition 3.3](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/regular-local-rings.html) |
| lemma regular ring CM | [AG-CA-12, Theorem 6.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/regular-sequences-depth-and-cohen-macaulay-modules.html) |
| lemma regular sequence powers | [AG-CA-12, Proposition 1.3](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/regular-sequences-depth-and-cohen-macaulay-modules.html) |
| lemma spec localization | [AG-CA-02, Theorem 3.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/localization-local-properties-and-support.html) |
| lemma variant local criterion flatness | [AG-CA-08, Corollary 4.4 and equation (6)](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/faithful-flatness-and-the-local-criterion-for-flatness.html) |
| proposition CM module | [AG-CA-12, Theorem 4.2 and Corollary 4.3](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/regular-sequences-depth-and-cohen-macaulay-modules.html) |
| proposition characterize formally smooth | [AG-CA-17, Theorem 3.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/formally-smooth-unramified-and-etale-ring-maps.html) |
| proposition smooth formally smooth | [AG-CA-17, Theorem 3.1 and the split conormal definition of smoothness in this draft](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/formally-smooth-unramified-and-etale-ring-maps.html) |
| lemma completion regular | [AG-CA-19, Theorem 4.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/completion.html) |
| complete-local simple-root lifting | [AG-CA-19, Theorem 5.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/completion.html#5-hensel-lifting-in-every-complete-local-ring) |
| finite residue fields in finite-type fibres | [AG-CA-06, Theorem 2.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/the-nullstellensatz-and-jacobson-rings.html#2-closed-points-detect-radical-equations) |
| minimal resolutions and Tor detection | [AG-CA-13, Theorem 2.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/projective-dimension-and-the-auslander-buchsbaum-formula.html#2-minimal-resolutions-over-a-local-ring) |
| regular Noetherian rings are normal | [AG-CA-15, Corollary 4.5](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/discrete-valuation-rings-normal-rings-and-serres-criterion.html#4-serre-conditions-and-the-normality-criterion) |
| arbitrary fields lift over their prime field | [AG-CA-19S, Lemma 1.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/coefficient-rings-and-cohen-structure.html#1-lifting-maps-from-the-prime-field) |
| complete local coefficient rings | [AG-CA-19S, Theorem 5.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/coefficient-rings-and-cohen-structure.html#5-coefficient-subrings-in-every-complete-local-ring) |
| complete local power-series presentations | [AG-CA-19S, Theorem 6.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/coefficient-rings-and-cohen-structure.html#6-the-power-series-presentation) |

## Sources, attribution, and history

The mathematical exposition reused here is the Stacks Project authors’ free *Smoothing Ring Maps*, *Algebra*, and *More on Algebra*, with categorical, field, and topological support from the same pinned edition. The consulted public source is the [AI Integrated Stacks fork at the pinned commit](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/tree/565b10e987aba5969b21145a0833f42d69f96790). The [source licensing statement](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/README.md#attribution-and-licensing) identifies GNU Free Documentation License 1.2.

Original source edition: *Smoothing Ring Maps* and supporting Stacks Project chapters, Stacks Project Authors and maintainers of the consulted fork. Modified version: *Artin approximation for polynomial equations and its desingularization proof*, programme supporting draft, 5 October 2026. Adaptation, finite-system application, and explicit corrections written by GPT-6.1 Sol (OpenAI) in Codex at Ultra. Self-checked by the writing AI. The authors of the source are not responsible for this adaptation. 

This document contains adapted GFDL expression and is retained under GFDL-1.2-only, with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts. It must not be labelled CC0. The complete unchanged [GNU FDL 1.2 licence](assets/GFDL-1.2.txt) accompanies this edition and its PDF. The free editable source and its copying notice remain accessible at the pinned links above.
