# Cohomological dimension and the Künneth formula

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Links and citations revised by Claude Opus 5.5 (Anthropic), October 2026. Original text released under CC0.*

How far can étale cohomology extend above the dimension of a scheme? The answer depends on both the geometry and the coefficients. An affine scheme has a stronger vanishing theorem than a proper scheme, and a product requires a derived tensor product when the coefficient ring is not a field. We prove those statements, including the steps that pass from sheaves to arbitrary complexes.

## 1. Coefficients and prerequisites

Write \(\operatorname{cd}_{\mathrm{tors}}(X)\) for the least \(D\in\mathbf N\cup\{\infty\}\) such that \(H^q(X,F)=0\) for \(q>D\) and **every torsion abelian étale sheaf** \(F\). Write \(\operatorname{cd}_\ell(X)\) when only \(\ell\)-primary torsion sheaves are tested. Our prime-to-characteristic convention is the supremum of these latter dimensions over primes invertible on the scheme. We prove the stronger all-torsion affine bound. A statement about one constant sheaf is not, by itself, a cohomological-dimension statement.

All schemes in a finite-type assertion are of finite type over the indicated field, with no implicit smoothness or separatedness assumption. They are Noetherian and quasi-compact and quasi-separated. Unless specified otherwise, \(R\Gamma\), inverse images and higher images refer to the small étale topoi. A torsion ring here is a unital ring killed by a positive integer; in the product theorem it is the commutative ring \(\Lambda=\mathbf Z/n\).

We use these exact earlier results: geometric stalks and qcqs cohomological continuity, finite pushforward and finite base change from lesson 7; field-topos comparison from lesson 8; constructible approximation, Noetherian subobjects and exact extension by zero from lesson 11; arbitrary torsion vanishing for affine and proper geometric curves from lesson 12; arbitrary proper base change and finite-constant embeddings from lesson 13; the finite-amplitude resolution argument, unbounded proper base change and proper projection formula from lesson 14; and smooth, pro-smooth and field-extension base change from lesson 15.

The geometric foundations are Noether normalization, finite normalization for varieties, the dimension formula for finite-type algebras over fields, and basic strict-henselization and finite-presentation limit properties. They contain no affine cohomological-vanishing or product theorem. For complexes we use the existence of termwise injective K-injective resolutions and flat resolutions. Étale sheaves have enough flat objects: direct sums of extensions by zero of free constant modules on étale objects surject onto any module sheaf, as is checked on germs.

## 2. Limits, curves and fields

**Lemma 2.1 (limits).** If \(X=\varprojlim X_i\) is a directed inverse limit of qcqs schemes with affine transition maps, and \(\operatorname{cd}_{\mathrm{tors}}(X_i)\leq D\) for every \(i\), then \(\operatorname{cd}_{\mathrm{tors}}(X)\leq D\). The same assertion holds for a fixed prime.

*Proof.* Put \(F_i=(p_i)_*F\), where \(p_i:X\to X_i\). There are compatible maps \(p_{ji}^{-1}F_i\to F_j\), obtained by adjunction. On the finite-presentation affine étale basis,

\[
F=\mathop{\mathrm{colim}}_i p_i^{-1}F_i,
\qquad H^q(X,F)=\mathop{\mathrm{colim}}_i H^q(X_i,F_i).
\tag{2.1}
\]

For the first equality, a germ of \(F\) has a representative on an affine étale object descending to one stage; a germ relation also holds at a sufficiently late stage. This proves surjectivity and injectivity on stalks. The second equality is precisely qcqs continuity for this system. Each \(F_i\) is torsion: a section on the inverse image of a quasi-compact étale object is killed by one integer after taking a finite cover on which its finitely many local annihilators apply. If \(F\) is primary, the integer can be a power of that prime. The terms in (2.1) vanish for \(q>D\). □

**Lemma 2.2 (curves).** If \(C\) is affine of dimension at most one over \(K\), then

\[
\operatorname{cd}_{\mathrm{tors}}(C)\leq 1+\operatorname{cd}_{\mathrm{tors}}(K).
\tag{2.2}
\]

*Proof.* For \(a:C\to\operatorname{Spec}K\), the geometric stalk of \(R^qa_*F\) is \(H^q(C_{K^{\mathrm{sep}}},F)\). Indeed a strict localization of the field is its separable closure, and the strict-local higher-image formula and continuity compute that stalk. Passing from a separable to an algebraic closure changes no étale cohomology. Lesson 12 makes these stalks zero for \(q>1\). The sheaves \(R^qa_*F\) are torsion: their stalk groups commute with the filtered annihilator subsheaves of \(F\). Leray has only rows zero and one and columns through \(\operatorname{cd}_{\mathrm{tors}}(K)\). This proves (2.2). The dimension-zero case also follows directly from exact finite pushforward. □

**Lemma 2.3 (field extensions).** For every extension \(L/K\),

\[
\operatorname{cd}_{\mathrm{tors}}(L)
\leq\operatorname{cd}_{\mathrm{tors}}(K)+\operatorname{trdeg}_K L.
\tag{2.3}
\]

*Proof.* An algebraic extension is the union of its finite subextensions. Each finite field map has exact direct image, so Leray bounds its cohomological dimension by that of \(K\); Lemma 2.1 passes to the union. This includes inseparable extensions.

For an extension of transcendence degree one, every finitely generated \(K\)-subalgebra of \(L\) is a domain of dimension at most one, by the field dimension formula. Lemmas 2.1 and 2.2 therefore give (2.3). For finite transcendence degree \(r\), choose a transcendence basis \(t_1,\ldots,t_r\). Apply the one-variable case successively to the rational extensions and then the algebraic case to \(L/K(t_1,\ldots,t_r)\). If either term on the right is infinite the bound is automatic. □

A strictly henselian local scheme has cohomological dimension zero for **all** abelian étale sheaves. Sections equal the closed geometric stalk: every pointed étale neighbourhood has a section and every open containing the closed point is the whole local scheme. This is an exact functor. Its punctured opens can have positive cohomology; the local scheme and its punctured spectrum must not be confused.

## 3. Support and finite models of a strict localization

For a finite-type \(K\)-scheme put

\[
E_a(X)=\{x\in X:\operatorname{trdeg}_K\kappa(x)\leq a\},
\qquad E_a(X)=\varnothing\quad(a<0).
\tag{3.1}
\]

These sets are stable under specialization. The closure of a point has dimension equal to the transcendence degree of its residue field.

**Lemma 3.1 (closed support approximation).** A torsion sheaf supported in a specialization-stable set \(E\) on a Noetherian scheme is a filtered union of constructible subsheaves, each supported on a closed subset contained in \(E\).

*Proof.* Constructible approximation gives maps from constructible sheaves to \(F\). Their images and finite sums are constructible by the Noetherian subobject and quotient theorem of lesson 11; they form a directed union equal to \(F\) on stalks. Their supports are constructible subsets of \(E\). A constructible subset of a Noetherian scheme contains the generic point of each component of its closure: on each component it is dense and contains an open dense part. All other points of that closure are specializations of such generic points. Its closure is thus still contained in \(E\). Closed pushforward identifies a sheaf with zero stalks off that closure with a sheaf on its reduced closed subscheme. □

**Lemma 3.2 (strict-local models).** Let \(x\in X\), let \(a=\operatorname{trdeg}_K\kappa(x)\), and let \(d\) be the dimension of a sufficiently small affine neighbourhood of \(x\), minimized over such neighbourhoods. For a chosen strict localization \(R=\mathcal O^{\mathrm{sh}}_{X,\bar x}\) there is a compatible embedding

\[
L=K(t_1,\ldots,t_a)^{\mathrm{sep}}\longrightarrow R,
\tag{3.2}
\]

with purely inseparable residue-field extension, and \(R\) is a filtered colimit of finite-type \(L\)-algebras of dimension at most \(d-a\).

*Proof.* Shrink around \(x\) and apply Noether normalization to get a finite map to \(\mathbf A^d_K\). In its polynomial coordinates choose a normalization of the residue quotient at the image of \(x\): after a polynomial change of coordinates, the quotient is finite over the first \(a\) coordinates. For each later coordinate choose a monic relation in the residue quotient and replace that coordinate by its monic polynomial. This defines a finite endomorphism of \(\mathbf A^d\): each old later coordinate is integral over the new coordinates. The image of \(x\) is now the generic point of the linear subspace defined by the last \(d-a\) coordinates. Projection onto the first \(a\) coordinates sends \(x\) to the generic point of \(\mathbf A^a\). Functorial strict localization gives (3.2). Its residue field is algebraic over the separably closed \(L\), hence purely inseparable.

Write \(R=\operatorname{colim}B_j\) over affine pointed étale neighbourhoods of \(x\). Their maps to \(\mathbf A^d\) are quasi-finite, since the original normalization map is finite. Write \(L=\operatorname{colim}A_i\) over affine pointed étale neighbourhoods of the generic point of \(\mathbf A^a\). Every map \(A_i\to R\) factors through some \(B_j\), because \(A_i\) is finitely presented. Order triples \((i,j,A_i\to B_j)\) by compatible enlargement. They form a filtered system: two triples and their finitely many compatibility relations can be realized at one later stage. Its colimit gives

\[
R=\mathop{\mathrm{colim}}_{(i,j)}(B_j\otimes_{A_i}L).
\tag{3.3}
\]

Each tensor algebra is quasi-finite over \(L[t_{a+1},\ldots,t_d]\), so has dimension at most \(d-a\). Cofinality in (3.3) follows directly by representing any finite list of elements of \(R\) in a \(B_j\) and any equality in a later one. □

For a smooth \(d\)-dimensional neighbourhood, \(R\) is a regular local domain and its fraction field has transcendence degree \(d-a\) over \(L\). Indeed an affine étale neighbourhood has the same function-field transcendence degree \(d\) over \(K\), and adjoining the embedded \(L\) removes \(a\) independent variables. In particular, if \(0\ne f\in\mathfrak m_R\), then \(f\) is transcendental over \(L\). A nonzero element algebraic over a field has its inverse in that field algebra, and would be a unit of \(R\).

## 4. Proper vanishing before affine vanishing

**Theorem 4.1.** If \(p:T\to S\) is proper with geometric fibres of dimension at most \(r\), then \(R^qp_*F=0\) for \(q>2r\) and every torsion sheaf \(F\).

*Proof.* The complete proof is Theorem 4.1 of lesson 14; here is its induction, to fix its logical position. Prove the assertion for all proper maps at once. Relative dimension zero is exact finite pushforward. Proper base change reduces each other case to a proper scheme over an algebraically closed field. Dimension one is the proper curve theorem.

For a reduced scheme of dimension \(r\), finite normalization gives a monomorphism \(F\to\nu_*\nu^{-1}F\), an isomorphism on a dense open containing every generic point. Its cokernel is a closed pushforward from a proper subset of dimension at most \(r-1\). The long exact sequence and induction reduce to a normal integral component of dimension \(r\).

Choose a nonconstant rational function and take its graph closure

\[
T\xleftarrow{b}T'\xrightarrow{v}\mathbf P^1.
\tag{4.1}
\]

The indeterminacy locus \(Z\) has codimension at least two: the map extends over every codimension-one discrete valuation ring by properness of \(\mathbf P^1\). The fibres of \(b\) have dimension at most one. The cone \(Q\) of \(F\to Rb_*b^{-1}F\) consequently has torsion cohomology in degrees \(0,1,2\), supported on \(Z\); there is no degree minus one because the degree-zero unit is injective. Induction on \(Z\) bounds \(H^m(T,Q)\) by \(m\leq2(r-2)+2=2r-2\). Thus high-degree cohomology of \(T\) reduces to that of \(T'\). The dominant \(v\) has fibres of dimension at most \(r-1\), so its higher images stop at \(2r-2\); Leray over the proper curve \(\mathbf P^1\) stops two degrees later. This proves the absolute bound and, by proper base change, the relative one. □

This proof uses no affine vanishing in dimensions greater than one. It is therefore available inside the affine induction below. Over a quasi-compact base, any finite-type proper map has some uniform finite fibre-dimension bound: finitely many affine presentations give bounds by their numbers of algebra generators.

## 5. The affine vanishing theorem

**Theorem 5.1 (Artin's affine vanishing, Gabber-style proof).** For \(X\) affine of finite type over any field \(K\),

\[
\operatorname{cd}_{\mathrm{tors}}(X)
\leq\dim X+\operatorname{cd}_{\mathrm{tors}}(K).
\tag{5.1}
\]

The proof follows the modern dimension-and-support argument used in the Stacks Project. It proves Artin's theorem without claiming to reproduce Artin's original strict-local induction word for word.

*Proof.* If \(\operatorname{cd}_{\mathrm{tors}}(K)=\infty\), the assertion is vacuous; suppose it is finite. Induct on \(d=\dim X\), **for schemes over all fields simultaneously**. Dimension zero is finite pushforward and dimension one is Lemma 2.2. Assume the assertion in all dimensions below \(d>1\).

Noether normalization gives a finite map \(X\to\mathbf A^d_K\). Finite pushforward is exact, so Leray reduces the problem to any torsion sheaf \(F\) on \(\mathbf A^d\). We establish the two interludes needed for that sheaf.

**Interlude A: boundary stalks.** Let \(j:U\to W\) be the complement of an effective Cartier divisor in a smooth \(d\)-dimensional variety. At a point \(w\) on the divisor put \(a=\operatorname{trdeg}_K\kappa(w)\). Then

\[
(R^qj_*F)_{\bar w}=0\quad(q>d-a).
\tag{5.2}
\]

The strict-local stalk is \(H^q(\operatorname{Spec}R[1/f],F)\), where \(R=\mathcal O^{\mathrm{sh}}_{W,\bar w}\) and \(f\) is a local nonzero equation. Lemma 3.2 embeds a separably closed \(L\) into \(R\). The preceding domain observation embeds \(L(f)\) into \(R[1/f]\). Its cohomological dimension is at most one by Lemma 2.3. The ring \(R[1/f]\) is the union of its finitely generated \(L(f)\)-subalgebras, domains of dimension at most \(d-a-1\): their fraction fields lie in \(\operatorname{Frac}R\), whose transcendence degree over \(L(f)\) is \(d-a-1\). The induction hypothesis bounds their cohomological dimensions by \(d-a\). Lemma 2.1 proves (5.2). Off the divisor all positive higher images vanish because \(j\) is an isomorphism locally. Thus \(R^qj_*F\) has support in \(E_{d-q}(W)\) for \(q>0\).

**Interlude B: support on a smaller affine scheme.** If \(Z\) is affine of dimension below \(d\) and \(G\) is supported in \(E_a(Z)\), then

\[
H^p(Z,G)=0\quad(p>a+\operatorname{cd}_{\mathrm{tors}}(K)).
\tag{5.3}
\]

Lemma 3.1 writes \(G\) as a union of sheaves supported on closed subschemes \(Z_i\subset Z\) of dimension at most \(a\). Closed pushforward and Leray identify their cohomology with cohomology on \(Z_i\). The dimension is also below \(d\), so the induction hypothesis applies. Filtered cohomology proves (5.3). Only the **affine** version of this interlude is asserted at this stage.

Now factor the projection onto \(B=\mathbf A^{d-1}_K\) as

\[
\mathbf A^d_K\xrightarrow{j}\mathbf P^1_K\times_K B
\xrightarrow{g}B,
\qquad f=g j.
\tag{5.4}
\]

The boundary divisor is the section at infinity, isomorphic to \(B\). For \(q>0\), \(R^qj_*F\) is a closed pushforward from that section. Therefore \(R^pg_*R^qj_*F=0\) if \(p,q>0\). Also \(R^qj_*F=0\) for \(q>d\), by (5.2). The proper relative curve bound gives \(R^pg_*j_*F=0\) for \(p>2\). In the relative Leray spectral sequence

\[
R^pg_*R^qj_*F\Longrightarrow R^{p+q}f_*F
\tag{5.5}
\]

the only possible entries are the row \(q=0\), in columns zero to two, and the column \(p=0\). For \(q>2\), the term \((0,q)\) has no incoming differential; its possible outgoing \(d_r\) has target \((r,q-r+1)\), which is zero either because both indices are positive, because \(r>2\), or because the second index is negative. Thus

\[
R^qf_*F=g_*R^qj_*F\quad(q>2).
\tag{5.6}
\]

Interlude A puts this sheaf on \(E_{d-q}(B)\). Interlude B then says \(H^p(B,R^qf_*F)=0\) for \(p>d-q+\operatorname{cd}_{\mathrm{tors}}(K)\).

For \(q=2\), its stalk at the generic point of \(B\) is the second cohomology of an affine line over a separable closure of \(K(B)\). The affine curve theorem makes it zero. There is only one generic point, so the support is contained in \(E_{d-2}(B)\). Interlude B gives the same inequality with \(q=2\). For \(q=0,1\), ordinary induction on the affine \((d-1)\)-dimensional \(B\) gives vanishing for \(p>d-1+\operatorname{cd}_{\mathrm{tors}}(K)\).

Finally use

\[
H^p(B,R^qf_*F)\Longrightarrow H^{p+q}(\mathbf A^d_K,F).
\tag{5.7}
\]

Every entry of total degree greater than \(d+\operatorname{cd}_{\mathrm{tors}}(K)\) is zero, in all four ranges just considered. Both spectral sequences are first-quadrant, with bounded relevant rows, so their filtrations in each degree are finite. This proves (5.1) and closes the simultaneous induction. □

## 6. Affine direct images lower support dimension

**Corollary 6.1.** On an affine finite-type \(K\)-scheme, a torsion sheaf supported in \(E_a\) has zero cohomology above \(a+\operatorname{cd}_{\mathrm{tors}}(K)\).

*Proof.* Apply Lemma 3.1, exact closed pushforward, Theorem 5.1 on each closed support of dimension at most \(a\), and filtered cohomology. There is now no induction restriction on the dimension of the ambient affine scheme. □

**Theorem 6.2 (affine support drop).** If \(f:X\to Y\) is affine between finite-type \(K\)-schemes and \(F\) is supported in \(E_a(X)\), then \(R^qf_*F\) is supported in \(E_{a-q}(Y)\).

*Proof.* Work on an affine neighbourhood of \(y\in Y\); its inverse image in \(X\) is affine. Put \(b=\operatorname{trdeg}_K\kappa(y)\) and \(R=\mathcal O^{\mathrm{sh}}_{Y,\bar y}\). We must show

\[
H^q(X\times_Y\operatorname{Spec}R,F)=0\quad(q>a-b).
\tag{6.1}
\]

First take a constructible subsheaf of \(F\) with closed support \(Z\subset X\), \(\dim Z\leq a\); Lemma 3.1 and continuity will recover \(F\). The local model construction of Lemma 3.2 provides a map \(Y\to\mathbf A^b_K\) sending \(y\) to its generic point and embeds \(L=K(t_1,\ldots,t_b)^{\mathrm{sep}}\) in \(R\). Form the compatible triples \(A_i\to B_j\) used in (3.3). Before tensoring with \(L\), the schemes \(Z\times_Y\operatorname{Spec}B_j\) are étale over \(Z\), hence have dimension at most \(a\). Their maps to \(\operatorname{Spec}A_i\), an étale \(b\)-dimensional neighbourhood of the generic point of \(\mathbf A^b\), have generic fibres of dimension at most \(a-b\): every component dominating this base loses exactly \(b\) transcendence variables; components not dominating it disappear on the generic fibre. Tensoring that generic fibre with the algebraic separable closure \(L\) preserves dimension.

Thus the closed supports in the affine \(L\)-models of \(X_R\) have dimension at most \(a-b\). By Corollary 6.1 over the separably closed field \(L\), their cohomology vanishes for \(q>a-b\). Continuity over the triples gives (6.1) for each constructible subsheaf. Filtered cohomology gives it for \(F\). If \(a-b<0\), all those generic supports are empty, so the assertion includes degree zero. The strict-local stalk formula now proves the claimed support inclusion. □

This argument justifies the algebraicity and dimension step in the affine-image interlude; it does not use ordinary geometric-fibre cohomology as a substitute for strict-local stalks of a nonproper map.

## 7. The bound for all finite-type schemes

We need a topological fact to include nonseparated schemes in the ordinary-cohomology bound.

**Lemma 7.1 (Noetherian Zariski vanishing).** On a Noetherian topological space of dimension at most \(d\), every abelian sheaf has zero cohomology in degrees greater than \(d\).

*Proof.* We give the generator argument. Suppose cohomology above \(d\) vanishes for all \(j_!\mathbf Z_U\), where \(U\) is open. Any sheaf is the filtered union of subobjects generated by finitely many local sections; all opens and their intersections are quasi-compact, so cohomology commutes with these unions. Removing one generator gives a short exact sequence with a quotient generated by one section. It therefore suffices to treat a quotient of \(j_!\mathbf Z_U\).

Its kernel is the filtered union of finitely generated subsheaves of \(j_!\mathbf Z_U\subset\mathbf Z_X\). A finite list of such generators can be made constant integers \(n_i>0\) on opens \(U_i\), by decomposing their locally constant sections. Add the intersections of all sublists with their greatest common divisors. For each point the least available positive generator then divides all the others at that point. Filter by the size of the integer generators. The successive quotient at integer \(n\) is \(\mathbf Z\) on \(U\setminus V\), zero on \(V\), and fits into

\[
0\to j_{V!}\mathbf Z_V\to j_{U!}\mathbf Z_U
\to Q_n\to0,
\tag{7.1}
\]

where \(U\) is the union of opens with generators at most \(n\), and \(V\) the union with generators less than \(n\). The generator \(n\) on its own opens and zero on \(V\) glue in this quotient; the gcd condition makes the overlap values zero. Thus each finite kernel has zero cohomology above \(d\), by its finite filtration and (7.1). The same holds for the whole kernel by filtered cohomology, and the quotient has the required vanishing by its long exact sequence. This proves the generator reduction.

Now induct on \(d\) and on the finite number of irreducible components. For a component \(Z\) and \(U=X\setminus Z\), the closed-open exact sequence reduces the assertion to the sheaf on \(Z\) and the extension from \(U\), which is supported on the union of the other components. Closed pushforward is exact. We thus reduce to irreducible \(X\). For \(d=0\), every nonempty open has the same points as \(X\), and sections are exact. For irreducible \(X\) of positive dimension, the constant sheaf \(\mathbf Z_X\) is flasque: every nonempty open is connected and its sections are \(\mathbf Z\). For nonempty \(U\), its complement \(Z\) has dimension below \(d\). The exact sequence

\[
0\to j_!\mathbf Z_U\to\mathbf Z_X\to i_*\mathbf Z_Z\to0
\tag{7.2}
\]

and induction show that \(j_!\mathbf Z_U\) has zero cohomology above \(d\). The empty open contributes zero. Apply the generator reduction to finish the proof. □

**Corollary 7.2.** If \(X\) is finite type of dimension \(d\) over a separably closed field, then

\[
H^q(X,F)=0\quad(q>2d)
\tag{7.3}
\]

for every torsion sheaf. If \(X\) is affine, it vanishes for \(q>d\).

*Proof.* Let \(\epsilon:X_{\mathrm{ét}}\to X_{\mathrm{Zar}}\). The sheaf \(R^q\epsilon_*F\) is obtained from \(U\mapsto H^q(U_{\mathrm{ét}},F)\). On the affine-open basis Theorem 5.1 gives zero for \(q>d\), so these higher images vanish. Lemma 7.1 gives \(H^p_{\mathrm{Zar}}(X,G)=0\) for \(p>d\) for any abelian \(G\). Leray for \(\epsilon\) has neither rows nor columns beyond \(d\), proving (7.3). The affine assertion is Theorem 5.1. No separatedness is needed. □

For separated \(X\), Nagata compactification and lesson 14 also give

\[
H^q_c(X,F)=0\quad(q>2d):\qquad
R\Gamma_c(X,F)=R\Gamma(\bar X,j_!F),\quad\dim\bar X=d.
\tag{7.4}
\]

Theorem 4.1 applies to the torsion sheaf \(j_!F\). This is a compact-support assertion. Ordinary cohomology uses \(Rj_*F\), whose positive cohomology sheaves need not vanish; (7.4) cannot alone prove (7.3). Section 7 supplies the needed additional argument.

## 8. Finite dimension and arbitrary complexes

For a qcqs map \(f\), define \(\operatorname{cd}_{\mathrm{tors}}(f)\) by vanishing of \(R^qf_*F\) for every torsion sheaf. It is a bound on higher images, without the extra cohomology of the base.

**Proposition 8.1.** A map between finite-type schemes over a field has finite cohomological dimension. A finite-type scheme \(X/K\) has finite absolute cohomological dimension if \(K\) does.

*Proof.* Locally make the target affine. An affine source has higher-image bound \(\dim X\) by Theorem 6.2, since every point of its support lies in \(E_{\dim X}\). Cover a general source by finitely many affine opens. Each nonempty multiple intersection is a quasi-compact open of an affine scheme, hence separated over the field. Cover that intersection by finitely many affine opens; their multiple intersections are affine by separatedness. The finite Čech-to-derived-image spectral sequence for this inner cover bounds its higher images by \(\dim X\) plus the length of the cover minus one. The outer finite-cover spectral sequence now bounds \(Rf_*\) by the maximum of finitely many such integers plus its own finite length. Finite affine target covering makes this a uniform bound. This works when the original source is nonseparated. For the absolute statement, the proof of Corollary 7.2 instead bounds the rows by \(\dim X+\operatorname{cd}_{\mathrm{tors}}(K)\) and the columns by \(\dim X\), giving a finite bound. □

**Lemma 8.2 (unbounded acyclic complexes).** Let \(T\) be left exact with enough injectives and \(R^qT=0\) for \(q>N\). A termwise \(T\)-acyclic complex computes \(RT\). For arbitrary complexes,

\[
RT(D^{\geq a})\subset D^{\geq a},\qquad
RT(D^{\leq b})\subset D^{\leq b+N}.
\tag{8.1}
\]

*Proof.* For an exact complex \(A^\bullet\) of acyclic objects, put \(Z^i=\ker d^i\). Its exact cycle sequences give \(R^qT(Z^{i+1})=R^{q+1}T(Z^i)\) for \(q\geq1\). Iterating to the left beyond \(N\) makes all cycles acyclic. Therefore \(T(A^\bullet)\) is exact. The cone of a quasi-isomorphism between acyclic complexes is another such exact complex, so termwise application preserves that quasi-isomorphism. Compare with a termwise injective K-injective resolution to obtain the computation claim.

The lower bound follows from a bounded-below injective resolution. For the upper bound use a termwise injective K-injective resolution \(I^\bullet\) exact above \(b\). For \(i>b+N\), its cycle sequences identify

\[
H^i(TI^\bullet)=R^1T(Z^{i-1})
=R^{N+1}T(Z^{i-N-1})=0.
\tag{8.2}
\]

All sequences used are in the exact part of the complex; the last one may start at \(I^b\). If \(N=0\), exactness of \(T\) gives the assertion immediately. This is the finite-amplitude argument proved in lesson 14. □

**Proposition 8.3 (coproducts).** For a qcqs map of finite cohomological dimension, \(Rf_*:D(X_{\mathrm{ét}},\Lambda)\to D(Y_{\mathrm{ét}},\Lambda)\) commutes with arbitrary direct sums, where \(\Lambda\) is a torsion ring. The analogous assertion holds for \(R\Gamma\) on a qcqs scheme of finite cohomological dimension.

*Proof.* Module-sheaf cohomology agrees with underlying abelian-sheaf cohomology, so the dimension bound applies to \(\Lambda\)-modules. Choose a termwise injective K-injective resolution \(I_\alpha^\bullet\) of each input. Higher images commute with filtered colimits of sheaves; a direct sum is the filtered union of finite subsums. Thus every \(\bigoplus_\alpha I_\alpha^t\) is \(f_*\)-acyclic, and \(f_*\bigoplus_\alpha I_\alpha^t=\bigoplus_\alpha f_*I_\alpha^t\). Lemma 8.2 permits this unbounded termwise computation. It identifies the canonical sum map with an isomorphism. The global-section proof is identical, using absolute qcqs continuity instead of relative continuity. □

Proper maps have this property locally on any base: on a quasi-compact target Theorem 4.1 provides finite amplitude. Local isomorphisms of the coproduct comparison glue.

**Lemma 8.4 (pulling out a constant complex).** If \(X\) is qcqs with finite cohomological dimension, then for any \(E\in D(X_{\mathrm{ét}},\Lambda)\) and \(V\in D(\Lambda)\),

\[
R\Gamma(X,E)\otimes^L_\Lambda V
\xrightarrow{\sim}R\Gamma(X,E\otimes^L_\Lambda\underline V).
\tag{8.3}
\]

*Proof.* The arrow is the canonical tensor-and-adjunction map. Both functors in \(V\) preserve triangles and direct sums by Proposition 8.3. It is an isomorphism for every shift of the free module \(\Lambda\), hence for free sums and their bounded complexes. Every bounded-above complex admits a bounded-above free resolution, which is the homotopy colimit of its bounded brutal truncations from below. Every complex is the homotopy colimit of its good truncations from above. These are actual homotopy colimits: the telescope is the cone of \(1-\text{shift}\) on the direct sum of the stages, and exactness of filtered colimits shows its cohomology is the colimit of their cohomologies. The two functors preserve those telescopes. This proves (8.3) for every \(V\), with no finite Tor-dimension assumption. □

**Proposition 8.5 (proper projection formula).** For proper \(p:T\to S\) and arbitrary complexes over a torsion ring,

\[
Rp_*E\otimes^L_\Lambda K
\xrightarrow{\sim}Rp_*(E\otimes^L_\Lambda p^{-1}K).
\tag{8.4}
\]

*Proof.* Check a geometric stalk of \(S\). Unbounded proper base change, proved in lesson 14 from proper base change and finite amplitude, reduces the map to (8.3) on the proper geometric fibre. Theorem 4.1 bounds that fibre's cohomological dimension. Exact inverse image commutes with derived tensor products, so the stalk map is precisely (8.3). All stalks are isomorphisms. □

For a proper morphism, neither (8.4) nor its geometric-fibre proof requires \(n\) prime to the characteristic. That restriction will enter the nonproper product argument.

## 9. The product map and one proper factor

For maps \(X\xrightarrow{f}S\), \(Y\xrightarrow{g}S\), write \(p,q\) for the projections of \(X\times_S Y\), and \(c\) for its map to \(S\). There is a canonical map

\[
Rf_*E\otimes^L_\Lambda Rg_*K
\longrightarrow Rc_*(p^{-1}E\otimes^L_\Lambda q^{-1}K).
\tag{9.1}
\]

It is adjoint to the tensor product of the counits \(f^{-1}Rf_*E\to E\), \(g^{-1}Rg_*K\to K\). Over a separably closed field its degree components are the usual external cup products. We prove that this specific map is an isomorphism.

**Theorem 9.1 (one proper factor).** Let \(k\) be separably closed, \(X/k\) proper and \(Y/k\) finite type. For any positive \(n\), including \(n\) divisible by the characteristic, and arbitrary complexes over \(\Lambda=\mathbf Z/n\),

\[
R\Gamma(X,E)\otimes^L_\Lambda R\Gamma(Y,K)
\xrightarrow{\sim}
R\Gamma(X\times_kY,p^{-1}E\otimes^L_\Lambda q^{-1}K).
\tag{9.2}
\]

*Proof.* The projection \(q\) is proper. Proper base change over the point gives \(Rq_*p^{-1}E=\underline{R\Gamma(X,E)}\). Proposition 8.5 then gives

\[
Rq_*(p^{-1}E\otimes^L q^{-1}K)
=\underline{R\Gamma(X,E)}\otimes^L K.
\tag{9.3}
\]

Apply \(R\Gamma(Y,-)\). Composition of derived direct images identifies the left with cohomology of the product, and (8.3) identifies the right with the tensor of the two cohomology complexes. Proposition 8.1 makes (8.3) applicable. These isomorphisms use the same counits as (9.1), so prove the canonical comparison. □

There is also a bounded-below version over \(\mathbf Z\): if \(E\) has torsion cohomology, \(E,K\) are bounded below and \(Y\) is merely qcqs, the same formula holds over \(\mathbf Z\). Here are the additional details, since finite cohomological dimension of \(Y\) is not assumed.

For any qcqs \(W\), \(D\in D^+(W_{\mathrm{ét}})\) and \(V\in D^+(\mathbf Z)\), the constant-tensor comparison holds. Represent \(V\) by a bounded-below complex of flat groups: global dimension one of \(\mathbf Z\) permits a flat resolution truncated one degree below its lower cohomology bound, with flat bottom quotient. Represent \(D\) by a bounded-below complex. A brutal upper tail of the flat complex starts arbitrarily high; its tensor with \(D\), and its tensor with \(R\Gamma(W,D)\), start correspondingly high. Right derived sections preserve lower bounds. Thus, in each fixed degree, bounded brutal truncations reduce the comparison to a bounded flat complex, then to one flat group \(M\). Good upper truncations of \(D\), followed by their finite cohomology triangles, reduce to one abelian sheaf. A flat abelian group is torsion free and is the filtered union of its finitely generated free subgroups. Qcqs cohomological continuity reduces this last case to finite free groups, for which the comparison is the finite-sum identity. This proves the bounded-below constant-tensor formula without an absolute dimension bound.

The proper projection formula over \(\mathbf Z\) now follows on geometric stalks from this formula and lesson 13's bounded-below proper base change. Both tensors remain bounded below, since \(\mathbf Z\) has Tor dimension one. The tensor involving \(E\) still has torsion cohomology: its derived rationalization is zero because that of \(E\) is zero. Thus proper base change applies to it as well. Applying this projection formula to \(q\) gives (9.3), over \(\mathbf Z\); apply the just-proved constant-tensor formula on \(Y\) to finish. The maps are the canonical ones in (9.1). □

## 10. Products preserve open-immersion base change

**Lemma 10.1 (closed-point detection).** On a finite-type scheme \(Z\) over a separably closed field, an abelian sheaf supported on closed points has no positive cohomology and is generated by global sections. A complex over a torsion ring, or a bounded-below abelian complex, with all cohomology sheaves so supported is zero if all its global cohomology groups vanish.

*Proof.* Lemma 3.1, in the Noetherian module version over \(\mathbf Z\), expresses such a sheaf as a union of finitely generated constructible sheaves supported on finite closed subsets. These subsets are disjoint unions of spectra of separably closed fields: their finite residue extensions are purely inseparable. Closed pushforward is exact and each point's sections are exact. Each finite-support sheaf therefore has no positive cohomology and is globally generated. Filtered cohomology and the lifting of a germ to a finite stage give both assertions for the union.

The scheme has finite cohomological dimension for torsion modules by Corollary 7.2. For a torsion complex, Lemma 8.2 reduces each degree to a finite cohomology window; the hypercohomology spectral sequence on that window has only its column zero. Thus \(H^i(Z,Q)=\Gamma(Z,H^iQ)\). The same calculation for bounded-below arbitrary abelian complexes uses the first-quadrant spectral sequence. These are the two forms needed below. Global generation makes a nonzero cohomology sheaf produce a nonzero group, proving detection. □

**Theorem 10.2 (open-product comparison).** Let \(j:U\to X\) be an open immersion between finite-type schemes over a field \(K\), and let \(Y/K\) be finite type. In

\[
\begin{array}{ccc}
Y\times_K U&\xrightarrow{h}&Y\times_K X\\
\downarrow p&&\downarrow q\\
U&\xrightarrow{j}&X,
\end{array}
\tag{10.1}
\]

the canonical map \(q^{-1}Rj_*F\to Rh_*p^{-1}F\) is an isomorphism for every torsion sheaf whose orders are invertible in \(K\).

*Proof.* Filter by annihilator integers and use qcqs higher-image continuity to reduce to \(nF=0\), \(n\) invertible. Induct on \(\dim X+\dim Y\), over all fields. If \(\dim X=0\), its open \(U\) is also closed, so exact open-and-closed pushforward proves the assertion.

Let \(z\) map to \(x\in X\), \(y\in Y\). If \(a=\operatorname{trdeg}_K\kappa(x)>0\), pass to \(X'=\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{X,\bar x}\). Pro-étale base change from lesson 15 identifies the pullback of the comparison with the comparison for \(U'\subset X'\). Lemma 3.2 writes \(X'\) as a limit of finite-type schemes over a separably closed extension \(L/K\), of dimensions at most \(\dim X-a<\dim X\). The quasi-compact open \(U'\) descends to an open in one stage, since its complement has finitely generated ideal locally on this affine scheme. The diagrams at these stages are products over \(L\) with \(Y_L\), which has dimension \(\dim Y\). Apply induction and relative continuity to get the comparison on the limit and hence at \(\bar z\).

If instead \(b=\operatorname{trdeg}_K\kappa(y)>0\), use the strict localization of **\(Y\) at \(y\)**. Its smaller-dimensional models are over a separably closed \(L/K\). Field-extension base change from lesson 15 identifies the original open comparison over \(L\); pro-étale base change identifies it over that strict localization. The models of \(Y'\), together with \(X_L,U_L\), have smaller dimension sum, so induction and continuity again apply. Naturality and composition of base-change maps identify these maps with the original one. The formula with a strict localization of \(X\) in this second step would be a typing error.

Consequently any failure is supported where both \(x\) and \(y\) are closed. Such a \(z\) is closed: the tensor product of their finite residue extensions is a finite-dimensional \(K\)-algebra. Localize to affine \(X,Y\). Compactify the affine \(Y\) by its dense projective closure \(\bar Y\), of the same dimension. The preceding smaller-dimensional arguments apply to this projective product too, so the cone of its comparison is supported only on closed points. The original comparison is its restriction to \(Y\). Field-extension base change allows \(K\) to be replaced by its separable closure, conservatively, and then \(\bar Y\) is still proper.

Let \(Q\) be the cone of the comparison for \(\bar Y\). Lemma 10.1 reduces \(Q=0\) to its global cohomology. Theorem 9.1 computes both sides canonically as

\[
R\Gamma(U,F)\otimes^L_{\mathbf Z/n}
R\Gamma(\bar Y,\mathbf Z/n).
\tag{10.2}
\]

For the left use \(R\Gamma(X,Rj_*F)=R\Gamma(U,F)\); for the right use derived composition for \(h\). The map between (10.2)'s two descriptions is the identity by the counit definition of external products. Thus its cone has zero global cohomology, and closed-point detection gives \(Q=0\). Restricting back proves the affine comparison, and locality proves the theorem. □

## 11. Punctual base change

The open-product theorem has a stronger consequence. For any scheme \(A/K\), any \(S'/K\) and qcqs \(g:T\to S'\), form

\[
X'=A\times_K S',\quad Y=A\times_K T,
\qquad Y\xrightarrow{h}X',\quad Y\xrightarrow{e}T,
\quad X'\xrightarrow{f'}S'.
\tag{11.1}
\]

**Theorem 11.1 (punctual comparison).** For torsion \(F\) on \(T\) of orders invertible in \(K\),

\[
(f')^{-1}Rg_*F\xrightarrow{\sim}Rh_*e^{-1}F.
\tag{11.2}
\]

*Proof.* Localize to affine \(A\), write it as a limit of finite-type affine \(K\)-schemes, and use relative continuity to reduce to finite-type \(A\). Filter by annihilators to assume \(nF=0\). Field-extension base change from lesson 15, for both \(g\) and \(h\), lets us assume \(K\) algebraically closed. Topological invariance lets us replace \(A\) by its reduction. The resulting \(A\to\operatorname{Spec}K\) is flat, finitely presented and geometrically reduced.

Degree zero holds for any flat finitely presented map with geometrically reduced fibres. The geometric connected-component construction gives an étale covering whose members factor through étale base neighbourhoods with flat, quasi-compact geometrically connected fibres. Lemma 2.1 of lesson 15 identifies sections of pulled sheaves along such fibres with sections downstairs, before and after base change. The two identifications prove the degree-zero comparison. This uses only the stated geometric covering fact, with no higher-cohomology assertion.

Suppose there is a least failing degree \(q>0\), with all comparisons in lower degrees valid for every square of the form (11.1). We give the reduction of a failure to a generic field; this is needed because \(g\) need not be finite type.

For an \(n\)-torsion sheaf \(M\), denote the degree-\(q\) comparison's cokernel by \(D_q(M)\). Embedding \(M\) into an injective \(I\), the two long exact sequences for \(0\to M\to I\to C\to0\) and the lower-degree comparisons show that the degree-\(q\) map is injective and

\[
D_q(M)\hookrightarrow R^qh_*e^{-1}I.
\tag{11.3}
\]

For \(M\subset N\), choose \(M\subset N\subset I\); the same embeddings in (11.3) show \(D_q(M)\hookrightarrow D_q(N)\). The diagram chase uses the identical cokernels of the two maps in degree \(q-1\); the source \(R^qg_*I\) is zero.

Choose a nonzero defect germ \(\xi\), on an affine base so \(T\) is qcqs. For a qcqs \(T'\to T\), let \(P(T')\) say that the image of this germ is still nonzero in the defect for the pulled sheaf. Nil-thickenings do not change \(P\). If \(T'\) is a limit of affine-transition schemes on all of which \(P\) holds, then \(P(T')\) holds: relative continuity and exact filtered colimits identify the defect groups, and an element is zero in such a colimit only if it becomes zero at a stage.

For a closed \(Z\subset T'\) with quasi-compact open complement \(V\), choose \(F|_V\hookrightarrow J\) with \(J\) injective. The stalk-exact monomorphism

\[
F|_{T'}\longrightarrow j_*J\oplus i_*F|_Z
\tag{11.4}
\]

preserves the defect by (11.3). If it remains nonzero in the closed summand, exact closed pushforward and its base change show \(P(Z)\). In the open summand, lower-degree comparison identifies the pulled \(j_*J\) with \(j'_*e_V^{-1}J\) and gives \(R^aj'_*e_V^{-1}J=0\) for \(1\leq a<q\). The relative Leray edge map

\[
R^qh'_*j'_*e_V^{-1}J\longrightarrow
R^q(h'j')_*e_V^{-1}J
\tag{11.5}
\]

is injective: its \((q,0)\) term has no outgoing differential, and every possible incoming term has second degree between one and \(q-1\). If \(P(V)\) failed, the restricted germ for \(F|_V\) would come from \(R^q(g'j)_*F|_V\); its image for \(J\) would be zero, since \(J\) is injective. This contradicts the nonzero image under (11.5). Hence \(P(V)\) holds. We have proved that a defect persists on either the closed or the open part.

Apply this to closed subschemes of \(T\). A descending chain has a closed inverse-limit intersection with affine transitions, on which \(P\) persists. Zorn's lemma gives a minimal closed subscheme with \(P\); replace it by its reduction. Every affine neighbourhood of any generic point in it has \(P\), because its proper closed complement cannot have \(P\). Their inverse limit is the spectrum of the residue field at that generic point. Indeed the local ring at a generic point of a reduced scheme is a field. Thus a failure exists with \(T=\operatorname{Spec}H\) a field.

Here are the integral replacements in this step, including their justification. An integral pushforward is exact, conservative, and commutes with arbitrary base change. To see exactness, on a strict-local target express the integral source as a limit of finite sources, and express an arbitrary sheaf as the colimit of its push-pull sheaves on those stages, as in (2.1). Continuity computes its higher cohomology by that on schemes finite over the strict-local target, which is zero by lesson 7. For conservativity, if the integral pushforward of \(M\) is zero, at every finite stage the finite pushforward of the stage sheaf \(p_{i*}M\) is zero. Finite pushforward is conservative by its product-of-stalks formula, so every stage sheaf is zero; (2.1) makes \(M=0\). Exactness then reflects kernels and cokernels. For base change, the same limit formula for degree-zero images, followed by finite base change at every stage, gives the canonical comparison. These arguments work for non-finite integral maps.

An integral surjection on the top allows replacement of \(F\) by its pulled sheaf: the unit \(F\to\pi_*\pi^{-1}F\) is injective (a geometric lift evaluates it as the identity), defects embed by (11.3), and exact integral pushforward and its comparison identify the new defect. Replace \(H\) by an algebraic closure. The sheaf then becomes a module over \(\mathbf Z/n\), a direct sum of finite cyclic groups \(\mathbf Z/d\), \(d\mid n\). Higher images commute with sums of sheaves, so one summand witnesses failure.

Replace the affine base by the normalization of the schematic closure of the image of \(\operatorname{Spec}H\), inside \(H\). This is an integral map; exact integral pushforward and conservativity transport the comparison and detect its failure. The resulting base is \(S'=\operatorname{Spec}B\), a normal domain whose fraction field \(L\) is algebraically closed. In fact it is the relative algebraic closure of the original fraction field inside \(H\); any algebraic element becomes integral after multiplication by a denominator. The extension \(H/L\) of separably closed fields has derived constant-sheaf unit an isomorphism by lesson 15. Derived composition therefore leaves the nonzero \(R^qh_*\mathbf Z/d\) unchanged if the top field is replaced by \(L\).

On a normal integral scheme with separably closed fraction field, separated étale charts split as disjoint unions of opens, by Lemma 6.1 of lesson 13. All local rings are strictly henselian, and on each irreducible open a constant sheaf is Zariski flasque. Étale and Zariski cohomology agree there, by the strict-local stalk argument. Hence

\[
R^q(\operatorname{Spec}L\to\operatorname{Spec}B)_*
\mathbf Z/d=0\quad(q>0).
\tag{11.6}
\]

Finally write \(B=\bigcup B_i\) as its finite-type \(K\)-subalgebras. Its fraction field is the colimit of the rings \((B_i)_b\), for nonzero \(b\in B_i\), ordered by enlargement and further inversion. The square for \(\operatorname{Spec}L\to\operatorname{Spec}B\) is the inverse limit of the squares for the open immersions \(\operatorname{Spec}(B_i)_b\to\operatorname{Spec}B_i\), with product factor \(A\). Theorem 10.2 proves comparison at every such stage. Relative continuity proves comparison on the limit. By (11.6) its positive target higher images must be zero, contradicting the surviving defect. There is no least failing degree. This proves (11.2). □

The theorem also holds for bounded-below complexes with admissible torsion cohomology: compare the hypercohomology spectral sequences, whose diagonals are finite. The unbounded tensor version below requires the separate finite-dimension argument.

## 12. Tensor comparison and the general Künneth formula

Use (11.1), and let \(p:X'\to A\). For \(n\) invertible in \(K\), the canonical tensor comparison is

\[
p^{-1}E\otimes^L_\Lambda(f')^{-1}Rg_*F
\longrightarrow
Rh_*(h^{-1}p^{-1}E\otimes^L_\Lambda e^{-1}F),
\qquad\Lambda=\mathbf Z/n.
\tag{12.1}
\]

**Lemma 12.1 (bounded-below tensor upgrade).** Map (12.1) is an isomorphism if \(E,F\) are bounded below and \(E\) has Tor amplitude bounded below.

*Proof.* First work over \(\mathbf F_\ell\), with both inputs sheaves and \(\ell\) invertible. For fixed \(F\), compare the degree-\(q\) functors

\[
A^q(E)=p^{-1}E\otimes(f')^{-1}R^qg_*F,
\quad
B^q(E)=R^qh_*(h^{-1}p^{-1}E\otimes e^{-1}F).
\tag{12.2}
\]

The \(A^q\) are exact in \(E\); the \(B^q\) form a cohomological sequence because tensor over a field is exact. Both commute with filtered colimits. Work locally on affine \(A\), approximate \(E\) by constructible sheaves, and use the finite-constant embedding of lesson 13:

\[
0\to E\to I=\bigoplus_i(\pi_i)_*\mathbf F_\ell\to C\to0,
\tag{12.3}
\]

where the \(\pi_i:A_i\to A\) are finite of finite presentation and \(C\) is constructible. For each summand, finite base change, finite exact pushforward and its projection formula identify (12.2) with the finite pushforward of the comparison (11.2) for \(A_i\). Thus it is an isomorphism in every degree for \(I\).

The following two-step induction fills in the dimension shifting. In degree zero, injectivity for every constructible \(E\) follows by embedding in \(I\) and using left exactness of \(B^0\). Once this also gives injectivity for \(C\), the exact source row and the left-exact target row in (12.3) give surjectivity for \(E\). Suppose all comparisons below \(q\) are isomorphisms. Since \(A^{q-1}(I)\to A^{q-1}(C)\) is surjective, the same is true for \(B^{q-1}\), and its connecting arrow is zero. Consequently \(B^q(E)\to B^q(I)\) is injective, which proves injectivity of the comparison for every \(E\). Apply that new injectivity to \(C\). An element of \(B^q(E)\), viewed in \(B^q(I)\), lifts through the comparison for \(I\); its image in \(A^q(C)\) is zero by injectivity for \(C\), hence it comes from \(A^q(E)\). This proves surjectivity. Filtered colimits recover all \(E\).

For \(\Lambda=\mathbf Z/n\), first take a flat sheaf \(E\). Filter a sheaf \(F\) by successive sheaves killed by prime factors \(\ell\) of \(n\): \(F[\ell]\) and \(F/F[\ell]\) have smaller annihilators when the original annihilator exceeds \(\ell\). In an \(\ell\)-killed case, flatness identifies

\[
E\otimes^L_\Lambda Rg_*F
=(E/\ell E)\otimes^L_{\mathbf F_\ell}Rg_*F,
\tag{12.4}
\]

and similarly on the target. Here derived pushforward of the \(\mathbf F_\ell\)-sheaf computes the same underlying cohomology; it may be regarded as a \(\Lambda\)-complex by restriction of scalars. The field-coefficient result applies. Long exact sequences and induction on the annihilator give the result for every sheaf \(F\).

Represent the given \(E\) by a bounded-below K-flat complex of flat sheaves, using its lower Tor-amplitude bound. Let its terms start in degree \(a\), and let \(F\in D^{\geq b}\). Its brutal tail above \(N\), tensored with either \(Rg_*F\) or \(F\), starts in degree \(N+1+b\). Right derived images preserve lower bounds. Thus the tail cannot affect degrees below \(N+b\) of either side or their comparison. Bounded brutal truncations and finite triangles reduce to a single flat sheaf \(E\). In this case good upper truncations of \(F\) give a similar degreewise reduction to a bounded complex of sheaves, then to single sheaves. The already proved case identifies the map in every fixed degree, proving the lemma. □

**Lemma 12.2 (unbounded tensor upgrade).** If \(A,S',T\) are finite type over \(K\), (12.1) is an isomorphism for arbitrary \(E,F\in D(-,\mathbf Z/n)\).

*Proof.* Propositions 8.1 and 8.3 make \(Rg_*\) and \(Rh_*\) preserve direct sums. Derived inverse images and derived tensor preserve them too. Both sides of (12.1) therefore preserve triangles and homotopy colimits in each variable.

Write \(E\) as the homotopy colimit of \(\tau_{\leq N}E\), reducing to bounded above. Resolve this bounded-above object by a bounded-above complex of flat sheaves on **\(A\)**. Its bounded brutal truncations from below have a lower Tor-amplitude bound and have homotopy colimit equal to the resolution. Thus we may take \(E\) a bounded complex of flat sheaves. Independently write \(F\) as the homotopy colimit of its good upper truncations, represent a bounded-above stage by a bounded-above complex of sheaves, and take its bounded brutal truncations from below. We reduce to \(F\) bounded. Lemma 12.1 applies at each stage. Preserving the telescopes proves the arbitrary-complex assertion. Choosing a flat resolution only in \(F\) would not justify the Tor-amplitude requirement on \(E\); the factor choice above is deliberate. □

**Theorem 12.3 (general Künneth).** Let \(k\) be separably closed, \(X,Y\) finite type over \(k\), and \(n\) invertible in \(k\). For arbitrary \(E\in D(X_{\mathrm{ét}},\mathbf Z/n)\), \(K\in D(Y_{\mathrm{ét}},\mathbf Z/n)\), the external-product map is an isomorphism:

\[
R\Gamma(X,E)\otimes^L_{\mathbf Z/n}R\Gamma(Y,K)
\xrightarrow{\sim}
R\Gamma(X\times_kY,
\operatorname{pr}_1^{-1}E\otimes^L_{\mathbf Z/n}
\operatorname{pr}_2^{-1}K).
\tag{12.5}
\]

*Proof.* In Lemma 12.2 take \(A=X\), \(S'=\operatorname{Spec}k\), \(T=Y\), \(F=K\). Exact global sections on the separably closed field identify its direct image with the complex of groups \(R\Gamma(Y,K)\). The lemma gives

\[
R\operatorname{pr}_{1*}(\operatorname{pr}_1^{-1}E\otimes^L
\operatorname{pr}_2^{-1}K)
=E\otimes^L\underline{R\Gamma(Y,K)}.
\tag{12.6}
\]

Apply \(R\Gamma(X,-)\), use derived composition, and then Lemma 8.4, valid by Proposition 8.1. This gives (12.5). All arrows were defined by adjunction and tensor, so the comparison is (9.1), compatible with pullbacks, units and external cup products. Neither input has been assumed bounded, constructible or of finite Tor dimension. □

If \(\Lambda=\mathbf F_\ell\) and the inputs are sheaves, taking cohomology gives the familiar direct-sum formula

\[
H^r(X\times Y,E\boxtimes K)
=\bigoplus_{i+j=r}H^i(X,E)\otimes_{\mathbf F_\ell}H^j(Y,K).
\tag{12.7}
\]

Over \(\mathbf Z/n\), (12.5) is the assertion; Tor groups may contribute to its degree groups. Replacing its derived tensor by an ordinary tensor for arbitrary modules would lose those contributions.

## 13. Three examples, with sharp bounds

**Example 13.1 (affine and projective space).** Let \(k\) be separably closed and \(\ell\) invertible in \(k\). Then

\[
\operatorname{cd}_\ell(\mathbf A^r_k)=r,
\qquad\operatorname{cd}_\ell(\mathbf P^r_k)=2r.
\tag{13.1}
\]

The upper bounds are Theorems 5.1 and 4.1. Here is a proof that they are attained. Put \(j:U=\mathbf A^1\setminus\{0,1\}\to\mathbf A^1\) and \(Q=j_!\mathbf F_\ell\). The closed-open sequence gives

\[
H^1(\mathbf A^1,Q)=\operatorname{coker}
(\mathbf F_\ell\xrightarrow{\mathrm{diag}}\mathbf F_\ell^2)
=\mathbf F_\ell.
\tag{13.2}
\]

Indeed the constant affine-line cohomology has only degree zero by lesson 15, and each closed point is acyclic. The same sequence gives \(H^0(Q)=0\) and no higher groups. Apply Theorem 12.3 repeatedly to \(Q\boxtimes\cdots\boxtimes Q\) on \(\mathbf A^r\): its degree-\(r\) cohomology is \(\mathbf F_\ell\). Thus affine cohomological dimension is attained by a nonconstant sheaf, even though the constant sheaf has no positive cohomology.

For projective space, lesson 14 computed

\[
R\Gamma_c(\mathbf A^1,\mathbf F_\ell)
=\mathbf F_\ell(-1)[-2].
\tag{13.3}
\]

On the proper compactification \((\mathbf P^1)^r\), the external product of the \(j_!\mathbf F_\ell\) for \(j:\mathbf A^1\to\mathbf P^1\) is extension by zero from \(\mathbf A^r\): every stalk is constant if all its coordinates lie in the open, and zero otherwise. The proper-factor Künneth theorem gives

\[
R\Gamma_c(\mathbf A^r,\mathbf F_\ell)
=\mathbf F_\ell(-r)[-2r].
\tag{13.4}
\]

Use the closed-open triangle for \(\mathbf P^{r-1}\subset\mathbf P^r\), with complement \(\mathbf A^r\). The proper dimension bound kills \(H^{2r-1}\) and \(H^{2r}\) of \(\mathbf P^{r-1}\), so the triangle identifies \(H^{2r}(\mathbf P^r,\mathbf F_\ell)\) with (13.4)'s nonzero top group. This proves the second equality in (13.1). In fact induction in the same triangle gives

\[
H^{2i}(\mathbf P^r,\mathbf F_\ell)=\mathbf F_\ell(-i)
\ (0\leq i\leq r),\qquad H^{2i+1}=0.
\tag{13.5}
\]

The proof does not use a later purity or duality theorem. For \(r=0\), both equalities in (13.1) mean the acyclic separably closed point.

**Example 13.2 (a product of projective lines).** For \(k\) as above, Theorem 9.1 and the projective-line calculation give groups of ranks

\[
1,\ 0,\ 2,\ 0,\ 1
\tag{13.6}
\]

in degrees zero through four on \(\mathbf P^1\times\mathbf P^1\). In degree two the summands have twist \((-1)\), and in degree four the group has twist \((-2)\). Choose a primitive \(\ell\)-th root to trivialize twists. If \(a,b\) are the pullbacks of the projective-line degree-two generator, then external cup products give

\[
H^*(\mathbf P^1\times\mathbf P^1,\mathbf F_\ell)
=\mathbf F_\ell[a,b]/(a^2,b^2),\qquad\deg a=\deg b=2.
\tag{13.7}
\]

Both squares vanish by pullback from a curve with no degree-four cohomology; \(ab\) generates the one-dimensional degree-four group by Künneth. Together \(1,a,b,ab\) give the listed ranks, so there are no further relations. No choice of roots is needed for the version retaining the twists.

**Example 13.3 (all affine characteristic-\(p\) coefficients).** On **every affine scheme** of characteristic \(p\),

\[
\operatorname{cd}_p(X)\leq1.
\tag{13.8}
\]

We prove the arbitrary-sheaf assertion as well as its constant-coefficient special case. First let \(Y\) be affine Noetherian, \(v:V\to Y\) open, and let \(J\subset\mathcal O_Y\) be a coherent ideal defining the closed complement. There is an exact sequence of étale abelian sheaves

\[
0\to v_!\mathbf F_p\to J\xrightarrow{z\mapsto z^p-z}J\to0.
\tag{13.9}
\]

At a geometric point in \(V\), \(J=\mathcal O\) and this is Artin–Schreier. At a point on the complement use its strictly henselian local ring \(R\), with ideal \(I\). For \(c\in I\), the polynomial \(Z^p-Z-c\) has a unique root with closed residue zero. Reducing that root modulo \(I\) gives zero: in the local ring \(R/I\), all roots of \(Z^p-Z\) are the constant elements of \(\mathbf F_p\), and only zero has that closed residue. Hence the root lies in \(I\). This proves surjectivity on the stalk. A kernel root in \(I\) has the same property and is zero. Thus the kernel stalks are \(\mathbf F_p\) on \(V\) and zero off \(V\), exactly those of extension by zero, proving (13.9).

Quasi-coherent étale cohomology equals Zariski quasi-coherent cohomology, the descent comparison used for Artin–Schreier in lesson 12. Since \(Y\) is affine, \(J\) has no positive cohomology. Consequently

\[
H^q(Y,v_!\mathbf F_p)=0\quad(q\geq2).
\tag{13.10}
\]

Now let \(F\) be a constructible \(\mathbf F_p\)-sheaf on an affine Noetherian \(X\). We prove this same bound by induction on its finite locally constant stratification. Choose an open part \(U\) containing all generic points on which \(F\) is locally constant, and apply the closed-open sequence. The closed term is handled by induction on the proper closed remainder, which is still affine.

For a connected component of \(U\), lesson 11's Sylow reduction supplies a finite étale \(r:V\to U\) of degree prime to \(p\), such that \(r^{-1}F\) has a finite filtration with constant \(\mathbf F_p\) quotients. Trace makes \(F|_U\) a direct summand of \(r_*r^{-1}F\). Extend the quasi-finite separated \(V\to X\) by Zariski's Main Theorem as \(V\xrightarrow{v}Y\xrightarrow{\pi}X\), with \(v\) open and \(\pi\) finite. Taking the schematic closure of \(V\) in \(Y\) ensures \(Y_U=V\): \(V\) is both open and closed in \(Y_U\), since it is finite over \(U\), and no extra part belongs to its closure. Finite base change and its zero boundary stalks therefore give

\[
j_!r_*r^{-1}F=\pi_*v_!r^{-1}F,
\tag{13.11}
\]

where \(j:U\to X\). The finite \(Y\) over affine \(X\) is affine. Exact \(v_!\) transports the filtration; (13.10) kills cohomology above one for each quotient, and hence for \(v_!r^{-1}F\). Exact finite pushforward and Leray give the same bound for (13.11). The trace splitting remains a splitting after exact \(j_!\), proving it for \(j_!F|_U\). Finitely many connected components cause only finite sums. The closed-open long exact sequence now proves \(H^q(X,F)=0\) for \(q\geq2\).

Constructible approximation and filtered cohomology recover every \(\mathbf F_p\)-sheaf on affine Noetherian \(X\). For \(p^mF=0\), the filtration by \(F[p]\) and successive quotients reduces to that case, with long exact sequences; for arbitrary primary torsion, take the filtered union of \(F[p^m]\). Finally an arbitrary affine \(\mathbf F_p\)-algebra is a filtered union of its finite-type subalgebras. The fixed-prime version of Lemma 2.1 passes this uniform bound to its spectrum. This proves (13.8) at the stated generality.

The bound is sharp for \(\mathbf A^r_k\), \(r\geq1\), in characteristic \(p\): the Artin–Schreier class of the first coordinate is nonzero. Restricting it to the first affine line reduces to the fact that a nonconstant \(b^p-b\) has degree divisible by \(p\), so cannot equal a coordinate. Thus \(\operatorname{cd}_p(\mathbf A^r_k)=1\), while \(\operatorname{cd}_\ell(\mathbf A^r_k)=r\) for \(\ell\ne p\).

The nonproper Künneth coefficient restriction is real. Over algebraically closed \(k\) of characteristic \(p\), the degree-one Artin–Schreier class of \(xy\) on \(\mathbf A^1\times\mathbf A^1\) is outside the sum of the two factors' classes. In the polynomial Artin–Schreier quotient, mixed monomials split into chains \((x^a y^b)^{p^i}\), with \(a,b>0\) and not both divisible by \(p\). If a polynomial \(c^p-c\) had mixed part equal to \(xy\), the highest occupied term of its chain through \(xy\) would contribute a still higher nonzero term under Frobenius, a contradiction. Pure-variable polynomials cannot cancel a mixed chain. Hence a characteristic-\(p\) version of (12.7) for these nonproper constant sheaves fails already in degree one.

## 14. Exercises

1. **Easy.** Over a separably closed \(k\), with \(\ell\ne\operatorname{char}k\), compute the groups, twists and cup-product algebra of \(\mathbf P^1\times\mathbf P^1\) with \(\mathbf F_\ell\)-coefficients.
2. **Medium.** Prove \(H^q(X,\mathbf Z/p)=0\) for \(q\geq2\) on every affine scheme of characteristic \(p\). Explain what additional argument extends this from the constant sheaf to \(\operatorname{cd}_p(X)\leq1\).
3. **Medium.** For separated finite-type \(X\) of dimension \(d\) over a separably closed field, use Nagata compactification and proper vanishing to prove \(H^q_c(X,F)=0\) for \(q>2d\). Then prove the requested ordinary bound \(H^q(X,F)=0\) for \(q>2d\), including nonseparated \(X\), and explain why compactification alone does not identify the two cohomologies.
4. **Medium.** For finite-type \(X\) over separably closed \(k\) and \(\ell\ne\operatorname{char}k\), prove that pullback gives \(H^*(X,\mathbf F_\ell)\simeq H^*(X\times\mathbf A^1,\mathbf F_\ell)\), compatibly with cup products.
5. **Hard.** Prove the affine curve bound \(\operatorname{cd}_{\mathrm{tors}}(C)\leq1+\operatorname{cd}_{\mathrm{tors}}(K)\) over arbitrary \(K\). Identify the geometric-stalk step and state why no prime-to-characteristic hypothesis is needed for this bound.

## 15. Full solutions

**Solution 1.** The projective-line theorem gives \(H^0=\mathbf F_\ell\), \(H^1=0\), \(H^2=\mathbf F_\ell(-1)\), with all later groups zero. Künneth over the field \(\mathbf F_\ell\) has no Tor terms. Degree zero is \(H^0\otimes H^0\); degree two has \(H^2\otimes H^0\) and \(H^0\otimes H^2\); degree four is \(H^2\otimes H^2\). These give ranks \(1,0,2,0,1\) and twists \(0,-1,-2\), with zero groups in every other degree.

Choose a twist trivialization and let \(a,b\) be the pullbacks of the degree-two generator on each factor. Their squares are pullbacks of zero degree-four groups on \(\mathbf P^1\). Their product is the external product of two generators, hence a generator in degree four. Graded commutativity has sign \((-1)^{2\cdot2}=1\), also for \(\ell=2\). The four basis elements \(1,a,b,ab\) establish \(\mathbf F_\ell[a,b]/(a^2,b^2)\). Retaining the twists avoids the choice of a root of unity. □

**Solution 2.** On the small étale site there is a short exact sequence

\[
0\to\mathbf Z/p\to\mathcal O_X
\xrightarrow{F-1}\mathcal O_X\to0.
\tag{15.1}
\]

Its kernel consists étale locally of the constant roots \(0,\ldots,p-1\). Surjectivity follows because adjoining a root of \(T^p-T-c\) gives a monic finite étale algebra with derivative \(-1\); its geometric fibres are nonempty, so it gives an étale cover. Quasi-coherent étale cohomology of \(\mathcal O_X\) is its Zariski cohomology, which is zero in positive degrees on affine \(X\). The long exact sequence makes every \(H^q(X,\mathbf Z/p)\), \(q\geq2\), zero and identifies

\[
H^1(X,\mathbf Z/p)=\Gamma(X,\mathcal O_X)/(F-1)\Gamma(X,\mathcal O_X).
\tag{15.2}
\]

This proves the exercise even for non-Noetherian affine rings. It does not alone test every primary torsion sheaf. For that assertion use the complete argument (13.9)–(13.11): apply Artin–Schreier to a coherent boundary ideal for open extension by zero, use a prime-to-\(p\) Sylow trace cover and its constant-quotient filtration, extend the cover into a finite affine scheme by Zariski's Main Theorem, then perform closed-open constructible dévissage. Primary-power filtrations and the limit theorem recover all affine schemes and all primary torsion sheaves. Each step was proved in Example 13.3. □

**Solution 3.** For separated \(X\), take a dense Nagata compactification \(j:X\to\bar X\), where \(\bar X\) is proper and has dimension \(d\); discard components not met by the open. Exact \(j_!\) preserves torsion. Thus \(H^q_c(X,F)=H^q(\bar X,j_!F)=0\) for \(q>2d\), by Theorem 4.1. This is the conclusion furnished by the stated compactification hint.

For ordinary cohomology, use \(\epsilon:X_{\mathrm{ét}}\to X_{\mathrm{Zar}}\). On every affine open, Theorem 5.1 over the separably closed field makes the cohomology presheaf zero above \(d\), so \(R^q\epsilon_*F=0\) for \(q>d\). Lemma 7.1 gives \(H^p_{\mathrm{Zar}}(X,G)=0\) for \(p>d\). The spectral sequence \(H^p_{\mathrm{Zar}}(X,R^q\epsilon_*F)\Rightarrow H^{p+q}(X,F)\) has no total degrees above \(2d\). It proves the ordinary bound even if \(X\) is nonseparated. Ordinary compactification instead gives \(R\Gamma(\bar X,Rj_*F)\), and positive \(R^qj_*F\) can occur. Substituting \(j_!F\) there would change the groups; for \(\mathbf A^1\), the constant ordinary group in degree zero is already different from its degree-zero compact-support group. □

**Solution 4.** Lesson 15 gives \(R\Gamma(\mathbf A^1,\mathbf F_\ell)=\mathbf F_\ell[0]\), with its degree-zero identification the constant-section map. Theorem 12.3 consequently identifies cohomology of \(X\times\mathbf A^1\) with \(R\Gamma(X,\mathbf F_\ell)\otimes^L\mathbf F_\ell=R\Gamma(X,\mathbf F_\ell)\). The canonical external-product definition sends \(u\) to \(\operatorname{pr}_1^*u\cup1\), so this is the actual projection pullback. Its inverse is restriction along the zero section, since that section followed by projection is the identity and pullback is already an isomorphism. Pullback preserves cup products, proving the ring assertion. Properness of \(X\) is unnecessary; invertibility of \(\ell\) is essential, as the characteristic-\(p\) example shows. □

**Solution 5.** Let \(f:C\to\operatorname{Spec}K\) and \(F\) be any torsion sheaf. Its higher-image geometric stalk is

\[
(R^qf_*F)_{\overline K}=H^q(C_{K^{\mathrm{sep}}},F|_{C_{K^{\mathrm{sep}}}}).
\tag{15.3}
\]

Use the strict-local stalk formula, expressing the separable closure as the limit of pointed field neighbourhoods; this is valid for a nonproper \(f\) because the base is a field. Purely inseparable passage to an algebraic closure preserves the étale topos. The arbitrary-torsion affine curve theorem of lesson 12 therefore kills (15.3) for \(q>1\), even for \(p\)-torsion in characteristic \(p\). Each remaining higher-image sheaf is torsion, by annihilator approximation and qcqs continuity. In Leray, \(H^i(K,R^qf_*F)\) vanishes for \(i>\operatorname{cd}_{\mathrm{tors}}(K)\), and rows \(q>1\) are zero. Thus \(H^m(C,F)=0\) for \(m>1+\operatorname{cd}_{\mathrm{tors}}(K)\). If the field dimension is infinite the inequality is automatic. This is the full coefficient scope of Lemma 2.2, rather than only a constant-sheaf computation. □

## 16. Sources, proof choices and corrections

- **[Modern dimension argument]** The Stacks Project Authors, [cohomological dimension, Tags 0F0P–0F0X](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-cd), and [proper dimension bound, Tag 095U](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-lemma-cohomological-dimension-proper). Sections 2–6 supply the limits, algebraic field-extension case, strict-local finite models, both interludes, all spectral-sequence ranges and the affine-image support bound. The induction's support interlude is stated on an affine scheme, where its use of affine induction is valid.
- **[Finite dimension and products]** [Finite cohomological dimension, Tags 0F0Y–0F0G](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-finite-cd), and [Künneth, Tags 0F13–0F1P](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-kunneth). Sections 8–12 prove the arbitrary-complex result in full. The inverse-limit reduction, closed-point detection, minimal defect argument, finite-constant dimension shifting and truncations are given explicitly, rather than replacing the general proof by its tag. The flat resolution in the unbounded tensor upgrade is taken in the factor required to have lower Tor amplitude.
- **[Auxiliary foundations]** [Noetherian topological vanishing](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-section-vanishing-Noetherian), [integral pushforward](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-lemma-what-integral), [finite-constant embeddings](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-lemma-constructible-maps-into-constant-general), [flat geometrically reduced connected-fibre covers](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-cover-by-geometrically-connected), and [finite Zariski main factorization](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-quasi-finite-separated-pass-through-finite). The latter geometric factorization is the explicit foundation in Example 13.3. Sections 7 and 11 give the topological and integral cohomological arguments; the finite-constant embedding is the proved earlier lesson 13 prerequisite.
- **[Artin–Schreier]** [The Artin–Schreier sequence](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-artin-schreier) gives the constant-coefficient affine computation. The stronger arbitrary-primary-sheaf assertion in Example 13.3 includes the boundary-ideal and Sylow trace steps.
- **[Historical affine theorem]** M. Artin, *[SGA 4](https://www.normalesup.org/~forgogozo/SGA4/)*, Exposé XIV, especially §§2–4, Théorème 3.1 and Corollaire 3.2. Its route uses strict-local dimension and a punctured strict-local model. The present proof follows the modern Gabber-style form named above. Exposé X, §5, contains the boundary-ideal Artin–Schreier mechanism used and proved in Example 13.3.
- **[Arcata statement]** P. Deligne, *[SGA 4½](https://publications.ias.edu/sites/default/files/Number32.pdf)*, “Cohomologie étale: les points de départ,” IV, 6.4: the affine-vanishing statement \(H^q(X,F)=0\) for \(q>\dim X\), proved here, and the Morse-theory analogy that follows it.

The examples distinguish cohomological dimension from constant cohomology, and the compactification exercise distinguishes ordinary from compact support. Finite \(n\) is invertible in the general nonproper Künneth theorem; one proper factor permits every \(n\). The linked AI Integrated Stacks Project reader contains AI-proposed corrections and additions and is not reviewed by the maintainers of the [official Stacks Project](https://stacks.math.columbia.edu/).
